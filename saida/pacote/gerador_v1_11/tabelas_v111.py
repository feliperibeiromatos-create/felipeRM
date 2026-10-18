# -*- coding: utf-8 -*-
"""T-108 (gerador_v1_11, seção 1.3 da D1) — leitura e validação das tabelas de substituição, do inventário de ocorrências e dos caminhos.
Falha = exceção Falha(tag, mensagem); a mensagem começa pela conferência (C-1, C-2, C-3, C-7) e pelo motivo. Nada é gravado aqui."""
import collections, csv, hashlib, io, re
from common import P as PATH


class Falha(Exception):
    def __init__(self, tag, msg):
        super().__init__('%s: %s' % (tag, msg))
        self.tag, self.msg = tag, msg


OBRIGATORIAS = ['id_edicao', 'ids_ocorrencia', 'caminho', 'antes', 'depois', 'acao', 'regra']
OPCIONAIS = ['lote', 'categoria', 'fonte_origem', 'nota', 'trecho', 'modo']
ACOES = ('DELETAR', 'SUBSTITUIR', 'MANTER')
SEP_IDS = ';'


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def le_bytes(rel_ou_abs):
    import os
    p = rel_ou_abs if os.path.isabs(rel_ou_abs) else PATH(rel_ou_abs)
    with open(p, 'rb') as f:
        return f.read()


def le_csv(raw, nome, ger=None, prefixos=None, erros=None):
    """Bytes -> lista de dicts, com as conferências de forma da seção 1.3 (pontos 1 a 3). Com `erros` (lista), os erros de linha são acumulados e a linha é descartada (modo tolerante)."""
    if raw.startswith(b'\xef\xbb\xbf'):
        raise Falha('C-1', '%s: BOM no início do arquivo' % nome)
    try:
        txt = raw.decode('utf-8')
    except UnicodeDecodeError as e:
        raise Falha('C-1', '%s: não é UTF-8 (%s)' % (nome, e))
    rd = csv.DictReader(io.StringIO(txt, newline=''))
    cols = rd.fieldnames or []
    falta = [c for c in OBRIGATORIAS if c not in cols]
    if falta:
        raise Falha('C-1', '%s: coluna obrigatória ausente: %s' % (nome, ', '.join(falta)))
    rows = []
    vistos = set()
    for k, r in enumerate(rd, 2):
        if None in r or any(v is None for v in r.values()):
            raise Falha('C-1', '%s linha %d: número de campos diferente do cabeçalho' % (nome, k))
        try:
            iid = r['id_edicao']
            ctx = '%s %s' % (nome, iid)
            if not iid:
                raise Falha('C-1', '%s linha %d: id_edicao vazio' % (nome, k))
            if iid in vistos:
                raise Falha('C-2', '%s: id_edicao duplicado' % ctx)
            vistos.add(iid)
            if prefixos is not None and not iid.startswith(prefixos):
                raise Falha('C-2', '%s: prefixo do id_edicao fora da Gerência %s' % (ctx, ger))
            if r['acao'] not in ACOES:
                raise Falha('C-1', '%s: acao inválida %r' % (ctx, r['acao']))
            regs = r['regra'].split(';')
            if not all(x.strip() in ('1', '2', '3', '4', '5') for x in regs):
                raise Falha('C-1', '%s: regra inválida %r' % (ctx, r['regra']))
            if '\r' in r['antes'] or '\r' in r['depois']:
                raise Falha('C-1', '%s: caractere \\r em antes ou depois' % ctx)
            if r['acao'] == 'DELETAR' and r['depois'] != '':
                raise Falha('C-1', '%s: DELETAR com depois não vazio' % ctx)
            if r['acao'] == 'SUBSTITUIR' and (r['depois'] == '' or r['depois'] == r['antes']):
                raise Falha('C-1', '%s: SUBSTITUIR com depois vazio ou igual ao antes' % ctx)
            if r['acao'] == 'MANTER' and not (r.get('nota') or '').strip():
                raise Falha('C-1', '%s: MANTER sem nota' % ctx)
            if not r['antes']:
                raise Falha('C-1', '%s: antes vazio' % ctx)
            ids = [x for x in r['ids_ocorrencia'].split(SEP_IDS) if x]
            if not ids or len(ids) != len(set(ids)):
                raise Falha('C-2', '%s: ids_ocorrencia vazio ou com id repetido na própria linha' % ctx)
        except Falha as e:
            if erros is None:
                raise
            erros.append((r.get('id_edicao', ''), str(e)))
            continue
        r['_ids'] = ids
        r['_ger'] = ger
        r['_tabela'] = nome
        rows.append(r)
    return rows


def carrega_de_bytes(itens, verifica_sha=False):
    """itens: [(gerência, nome, bytes, sha|None)] -> lista de linhas de todas as tabelas, com `_ger`, `_tabela` e `_sha`."""
    import config_v111 as cfg
    out, vistos = [], {}
    for ger, nome, raw, sha in itens:
        h = sha256_bytes(raw)
        if sha and h != sha:
            raise Falha('C-1', 'SHA-256 de %s = %s != fixado %s' % (nome, h, sha))
        if verifica_sha and not sha:
            raise Falha('C-1', 'SHA-256 de %s não fixado (FINAL)' % nome)
        rows = le_csv(raw, nome, ger, cfg.PREFIXOS[ger])
        for r in rows:
            r['_sha'] = h
            if r['id_edicao'] in vistos:
                raise Falha('C-2', 'id_edicao %s repetido em %s e %s' % (r['id_edicao'], vistos[r['id_edicao']], nome))
            vistos[r['id_edicao']] = nome
        out += rows
    return out


def carrega_tabelas(tabs, verifica_sha=False):
    """tabs: [(gerência, caminho, sha|None)] lidos do disco."""
    return carrega_de_bytes([(g, c, le_bytes(c), h) for g, c, h in tabs], verifica_sha)


def le_ocorrencias(raw):
    """T108_ocorrencias.csv -> {id: linha} só do pacote.json."""
    txt = raw.decode('utf-8')
    rd = csv.DictReader(io.StringIO(txt, newline=''))
    return collections.OrderedDict((r['id_ocorrencia'], r) for r in rd if r['arquivo'] == 'pacote.json')


# ---------------------------------------------------------------- caminhos (ponto 5)
_TOK = re.compile(r'([A-Za-z]+)(?:\[([^\]]+)\])?')
TOPO = {'itens': ('justificativa', 'nota'), 'lotes': ('curso', 'resumo'), 'simulados': (), 'discursivas': ('comando', 'padrao')}


def _split(cam):
    partes, atual, prof = [], '', 0
    for ch in cam:
        if ch == '[':
            prof += 1
        elif ch == ']':
            prof -= 1
        if ch == '.' and prof == 0:
            partes.append(atual); atual = ''
        else:
            atual += ch
    partes.append(atual)
    return partes


def _tokens(cam):
    partes = _split(cam)
    toks = []
    for p in partes:
        m = _TOK.fullmatch(p)
        if not m:
            raise Falha('C-3', 'caminho %r: sintaxe inválida' % cam)
        toks.append((m.group(1), m.group(2)))
    return toks


def resolve(P, cam):
    """-> (objeto_de_topo, caminho_relativo, container, chave): P[container][chave] é a string do campo. Falha se não resolve a uma string ou fora dos campos exibidos."""
    toks = _tokens(cam)
    (lista, ident) = toks[0]
    if lista not in TOPO or ident is None:
        raise Falha('C-3', 'caminho %r: lista de topo inválida' % cam)
    objs = [o for o in P[lista] if o['id'] == ident]
    if len(objs) != 1:
        raise Falha('C-3', 'caminho %r: objeto %s[%s] não encontrado' % (cam, lista, ident))
    obj = objs[0]
    rel = '.'.join(_split(cam)[1:])
    cur, chave = obj, None
    resto = toks[1:]
    if not resto:
        raise Falha('C-3', 'caminho %r: sem campo' % cam)
    for k, (nome, idx) in enumerate(resto):
        ultimo = k == len(resto) - 1
        if not isinstance(cur, dict) or nome not in cur:
            raise Falha('C-3', 'caminho %r: campo %s ausente' % (cam, nome))
        if idx is None:
            if not ultimo:
                raise Falha('C-3', 'caminho %r: %s sem índice' % (cam, nome))
            chave = nome
            break
        lst = cur[nome]
        if not isinstance(lst, list):
            raise Falha('C-3', 'caminho %r: %s não é lista' % (cam, nome))
        if nome == 'aspectos':
            alvo = [x for x in lst if str(x['n']) == idx]
        elif nome == 'quesitos':
            alvo = [x for x in lst if x['id'] == idx]
        else:
            if not idx.isdigit() or int(idx) >= len(lst):
                raise Falha('C-3', 'caminho %r: índice %s fora da lista %s' % (cam, idx, nome))
            alvo = [lst[int(idx)]]
        if len(alvo) != 1:
            raise Falha('C-3', 'caminho %r: %s[%s] não encontrado' % (cam, nome, idx))
        if ultimo:
            if nome in ('avisos', 'conceitos'):
                cur, chave = lst, int(idx)
                break
            raise Falha('C-3', 'caminho %r: termina em objeto e não em string' % cam)
        cur = alvo[0]
    if chave is None:
        raise Falha('C-3', 'caminho %r: não termina em campo de texto' % cam)
    v = cur[chave]
    if not isinstance(v, str):
        raise Falha('C-3', 'caminho %r: não resolve a uma string' % cam)
    exibido = False
    if lista == 'itens' and chave in ('justificativa', 'nota'):
        exibido = True
    elif lista == 'lotes' and (rel in ('curso', 'resumo') or re.fullmatch(r'pegadinhas\[\d+\]\.(rotulo|texto)', rel) or re.fullmatch(r'pares\[\d+\]\.(a|b|como)', rel)):
        exibido = True
    elif lista == 'simulados' and re.fullmatch(r'avisos\[\d+\]', rel):
        exibido = True
    elif lista == 'discursivas' and (rel in ('comando', 'padrao') or re.fullmatch(r'aspectos\[[^\]]+\]\.texto', rel) or re.fullmatch(r'quesitos\[[^\]]+\]\.nome', rel)
                                      or re.fullmatch(r'quesitos\[[^\]]+\]\.conceitos\[\d+\]', rel)):
        exibido = True
    if not exibido:
        raise Falha('C-3', 'caminho %r: fora dos campos de texto exibidos (ponto 2 da v1.2.5)' % cam)
    return obj, rel, cur, chave


def valida_cobertura(rows, oc, inv, completa=True, ger_por_tabela=None):
    """Seção 1.3, ponto 4. oc: {id: linha de T108_ocorrencias.csv (pacote.json)}; inv: {id: ocorrência recalculada} (para conferir caminho). Devolve dict de estatísticas.
    completa=False (ENSAIO com tabelas em produção): não exige que todo id do universo apareça, só que nenhuma linha cite id fora dele."""
    universo = {i for i, o in oc.items() if o['classe'] in ('PROCESSO', 'VERIFICAR')}
    fps = {i for i, o in oc.items() if o['classe'] in ('FP-R1', 'FP-CONTEUDO')}
    cont = collections.Counter()
    for r in rows:
        for i in r['_ids']:
            cont[i] += 1
            if i in fps:
                raise Falha('C-2', '%s: cita o id %s, que é FP (FP-R1/FP-CONTEUDO não entra em linha)' % (r['id_edicao'], i))
            if i not in universo:
                raise Falha('C-2', '%s: cita o id %s, fora do universo (PROCESSO ou VERIFICAR do pacote.json)' % (r['id_edicao'], i))
            o = oc[i]
            if o['caminho'] != r['caminho']:
                raise Falha('C-2', '%s: o id %s é do caminho %s e a linha diz %s' % (r['id_edicao'], i, o['caminho'], r['caminho']))
            if o['gerencia'] != r['_ger']:
                raise Falha('C-2', '%s: o id %s é da Gerência %s e a tabela é da %s' % (r['id_edicao'], i, o['gerencia'], r['_ger']))
    rep = [i for i, n in cont.items() if n > 1]
    if rep:
        raise Falha('C-2', 'id de ocorrência em mais de uma linha: %s' % ', '.join(sorted(rep)[:5]))
    faltam = sorted(universo - set(cont))
    if completa and faltam:
        raise Falha('C-2', 'cobertura: %d ids do universo sem linha (ex.: %s)' % (len(faltam), ', '.join(faltam[:3])))
    return dict(universo=len(universo), cobertos=len(cont), faltam=len(faltam), fp=len(fps), por_gerencia={g: sum(1 for i in cont if oc[i]['gerencia'] == g) for g in ('GCE', 'GCB', 'GBQ')})
