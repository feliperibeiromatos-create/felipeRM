# -*- coding: utf-8 -*-
"""T-108 (gerador_v1_11, seções 1.4 e 1.5 da D1) — aplicação, ocorrência a ocorrência, das linhas SUBSTITUIR/DELETAR das tabelas ao pacote.json (texto-base = v1.10) e
gravação do campo `interno`. `aplica` devolve o pacote novo e o resultado; em modo tolerante (usado só pelo montador de tabelas de ensaio e pelo relatório de leitura real)
as linhas que falham são descartadas e listadas, em vez de parar. Nada é gravado aqui."""
import collections, copy, re
import config_v111 as cfg
from tabelas_v111 import Falha, resolve, _split

# união das expressões das D1 da GCE e da GCB (ponto 7 da seção 1.4)
PROIBICOES = [
    ('F/N nn', re.compile(r'\b[FN]\d{1,2}\b')), ('U/GG/TB', re.compile(r'\bU\d\b|\bGG\d\b|\bTB\d\b')),
    ('código de item', re.compile(r'L\d[A-C]?-[QR]?\d+')), ('código nA-nn', re.compile(r'\b\d[A-C]-\d{2}\b')), ('A5-nn', re.compile(r'\bA5-\d{2}\b')), ('BQ-nnnn', re.compile(r'\bBQ-\d{4}\b')),
    ('[V ', re.compile(r'\[V ')), ('NORMATIVO', re.compile(r'NORMATIVO')), ('REVERIFICAR', re.compile(r'REVERIFICAR')), ('QA', re.compile(r'\bQA\b')), ('CQFP', re.compile(r'CQFP')), ('CPP', re.compile(r'CPP')),
    ('GCE', re.compile(r'\bGCE\b')), ('GCB', re.compile(r'\bGCB\b')), ('GBQ', re.compile(r'\bGBQ\b')), ('D-id', re.compile(r'\bD-[A-Z0-9-]+')), ('T-n', re.compile(r'\bT-\d+')),
    ('Lote n', re.compile(r'\bLote \d')), ('TC/IC/GI/AT no início', re.compile(r'^(?:TC|IC|GI|AT)\b', re.M)), ('TC/IC/GI/AT rótulo', re.compile(r'\b(?:TC|IC|GI|AT)\s*[—:-]')),
    ('[TS]', re.compile(r'\[TS\]')), ('Difere do item', re.compile(r'Difere do item')), ('VOLÁTIL', re.compile(r'VOLÁT(?:IL|EIS)\b')),
]
VERIF_EM = re.compile(r'verificado em \d{2}/\d{2}/\d{4}')
BASE_LEGAL = re.compile(r'\b(?:Lei|Decreto|art\.|inciso)|§')


def _fp_regras():
    import inventario_v111 as I
    return I.FP


def _erro(tolerante, descartadas, rid, tag, msg):
    f = Falha(tag, '%s: %s' % (rid, msg))
    if not tolerante:
        raise f
    descartadas.append((rid, str(f)))
    return True


def aplica(P0, rows, inv, excecoes_depois=None, tolerante=False):
    """P0: pacote base (OrderedDict; não é alterado). rows: linhas das tabelas. inv: {id_ocorrencia: ocorrência com _a,_b,caminho,classe} do pacote.json base.
    Devolve (P, res): res = dict(linhas=[...], manter=[...], registros=[...], descartadas=[...], totais=...)."""
    excecoes_depois = excecoes_depois or {}
    P = copy.deepcopy(P0)
    fp_rx = _fp_regras()
    descartadas = []
    por_campo = collections.OrderedDict()
    for r in rows:
        por_campo.setdefault(r['caminho'], []).append(r)
    fps_campo = collections.defaultdict(list)
    for i, o in inv.items():
        if o['classe'] in ('FP-R1', 'FP-CONTEUDO'):
            fps_campo[o['caminho']].append((o['_a'], o['_b'], i))
    registros, linhas, manter = [], [], []
    for cam, rs in por_campo.items():
        obj, rel, cont, chave = resolve(P, cam)
        texto = cont[chave]
        ok = []
        # fase 2 e 3: antes único; casamentos dentro do intervalo (C-2b: cobertura posicional; EXCECAO_INTERVALO; ids extras sem posição)
        todas = []
        for r in rs:
            rid = r['id_edicao']
            pos_ant = _acha(texto, r['antes'])
            if len(pos_ant) != 1:
                if _erro(tolerante, descartadas, rid, 'C-3', 'antes ocorre %d vez(es) em %s (esperado 1)' % (len(pos_ant), cam)):
                    continue
            i = pos_ant[0]; j = i + len(r['antes'])
            r['_i'], r['_j'] = i, j
            todas.append(r)
        por_id = {r['id_edicao']: r for r in todas}
        for r in todas:
            rid, i, j = r['id_edicao'], r['_i'], r['_j']
            fora = [x for x in r['_ids'] if x in inv and not (i <= inv[x]['_a'] and inv[x]['_b'] <= j)]
            if rid in cfg.EXCECAO_INTERVALO:
                alvo = por_id.get(cfg.EXCECAO_INTERVALO[rid])
                bad = (not fora) or alvo is None or any(not (alvo['_i'] <= inv[x]['_a'] and inv[x]['_b'] <= alvo['_j']) for x in fora)
                if bad and _erro(tolerante, descartadas, rid, 'C-2b', 'EXCECAO_INTERVALO: o casamento citado (%s) não está no antes da linha %s' % (','.join(fora) or '(nenhum fora)', cfg.EXCECAO_INTERVALO[rid])):
                    continue
            elif fora:
                if _erro(tolerante, descartadas, rid, 'C-3', 'casamento(s) %s fora do intervalo do antes em %s' % (','.join(fora), cam)):
                    continue
            ok.append(r)
        # fase 4: sobreposição
        ok.sort(key=lambda x: x['_i'])
        sem = []
        fim = -1
        for r in ok:
            if r['_i'] < fim:
                if _erro(tolerante, descartadas, r['id_edicao'], 'C-3', 'intervalo do antes se sobrepõe ao de outra linha em %s' % cam):
                    continue
            fim = max(fim, r['_j'])
            sem.append(r)
        ok = sem
        if not tolerante:
            # C-2b: cada id do inventário (PROCESSO ou VERIFICAR) da Gerência dona cai no antes de exatamente uma linha dela, neste caminho
            for xid, o in inv.items():
                if o['classe'] not in ('PROCESSO', 'VERIFICAR') or o['caminho'] != cam:
                    continue
                n = sum(1 for r in todas if r['_ger'] == o['gerencia'] and r['_i'] <= o['_a'] and o['_b'] <= r['_j'])
                if n != 1:
                    raise Falha('C-2b', 'o id %s cai no antes de %d linha(s) da %s em %s (esperado 1)' % (xid, n, o['gerencia'], cam))
        # fase 5: FP intactos; fase 7: proibições no depois; fase 8: verificado em e base legal
        ok2 = []
        for r in ok:
            rid, i, j = r['id_edicao'], r['_i'], r['_j']
            if r['acao'] == 'MANTER':
                ok2.append(r); continue
            bad = None
            for a, b, fid in fps_campo.get(cam, []):
                if a < j and i < b:
                    if not (i <= a and b <= j):
                        bad = 'o FP %s fica parcialmente dentro do antes' % fid
                        break
                    lit = texto[a:b]
                    if r['depois'].count(lit) < r['antes'].count(lit):
                        bad = 'o FP %s (%r) não reaparece no depois' % (fid, lit)
                        break
            if bad:
                if _erro(tolerante, descartadas, rid, 'C-3', bad):
                    continue
            dep = r['depois']
            exc = [re.compile(x) for x in excecoes_depois.get(rid, [])]
            achou = None
            for nome, rx in PROIBICOES:
                for m in rx.finditer(dep):
                    if _fp_declarado(dep, m, fp_rx):
                        continue
                    if any(e.search(m.group(0)) for e in exc):
                        continue
                    achou = '%s em %r' % (nome, m.group(0))
                    break
                if achou:
                    break
            if achou:
                if _erro(tolerante, descartadas, rid, 'C-7', 'proibição no depois: %s' % achou):
                    continue
            if '3' not in [x.strip() for x in r['regra'].split(';')]:
                perda = None
                isentos = cfg.EXCECAO_BASE_LEGAL.get(rid, [])
                for lit in set(VERIF_EM.findall(r['antes'])):
                    if dep.count(lit) < r['antes'].count(lit):
                        perda = '"%s" perdido' % lit
                for rx in (BASE_LEGAL,):
                    ca = collections.Counter(rx.findall(r['antes'])); cd = collections.Counter(rx.findall(dep))
                    for k, v in ca.items():
                        if cd[k] < v and k not in isentos:
                            perda = 'base legal %r perdida (%d -> %d)' % (k, v, cd[k])
                if perda:
                    if _erro(tolerante, descartadas, rid, 'C-7', 'verificado em / base legal: %s' % perda):
                        continue
            ok2.append(r)
        # aplicação: da primeira à última para calcular `pos`; texto novo montado em peças
        ok2.sort(key=lambda x: x['_i'])
        pecas, cur, delta = [], 0, 0
        recs = []
        for r in ok2:
            if r['acao'] == 'MANTER':
                manter.append(dict(id_edicao=r['id_edicao'], ids=r['_ids'], caminho=cam, nota=r.get('nota', ''), antes=r['antes']))
                linhas.append(dict(id_edicao=r['id_edicao'], caminho=cam, pos=None, acao='MANTER', resultado='mantido'))
                continue
            pecas.append(texto[cur:r['_i']]); pecas.append(r['depois'])
            pos = r['_i'] + delta
            delta += len(r['depois']) - len(r['antes'])
            cur = r['_j']
            recs.append(dict(edicao=r['id_edicao'], campo=rel, pos=pos, antes=r['antes'], depois=r['depois'], regra=r['regra'], ocorrencias=list(r['_ids'])))
            linhas.append(dict(id_edicao=r['id_edicao'], caminho=cam, pos=pos, acao=r['acao'], resultado='aplicado'))
        if recs:
            pecas.append(texto[cur:])
            novo = ''.join(pecas)
            cont[chave] = novo
            for rc in recs:
                rc['_obj'] = _split(cam)[0]
            registros += recs
    # interno por objeto de topo
    por_obj = collections.OrderedDict()
    for rc in registros:
        por_obj.setdefault(rc['_obj'], []).append(rc)
    for chave_obj, recs in por_obj.items():
        lista, ident = re.fullmatch(r'([A-Za-z]+)\[([^\]]+)\]', chave_obj).groups()
        obj = [o for o in P[lista] if o['id'] == ident][0]
        recs_ord = sorted(recs, key=lambda x: (x['campo'], x['pos']))      # empate de pos: ordem de entrada (primeiro ao último no texto-base)
        obj['interno'] = [collections.OrderedDict([('edicao', x['edicao']), ('campo', x['campo']), ('pos', x['pos']), ('antes', x['antes']), ('depois', x['depois']),
                                                   ('regra', x['regra']), ('ocorrencias', x['ocorrencias'])]) for x in recs_ord]
    totais = collections.Counter(r['acao'] for r in rows)
    res = dict(linhas=linhas, manter=manter, registros=registros, descartadas=descartadas, aplicadas=len(registros), mantidas=len(manter), por_acao=dict(totais))
    return P, res


def _fp_declarado(dep, m, fp_rx):
    """O casamento proibido m do depois é falso positivo declarado se uma regra FP do inventário casa na janela de contexto (±25) e o seu casamento cobre o de m."""
    lo = max(0, m.start() - 25)
    ctx = dep[lo:m.end() + 25]
    for cat, frx, cl, mot in fp_rx:
        for mm in frx.finditer(ctx):
            if lo + mm.start() <= m.start() and m.end() <= lo + mm.end():
                return True
    return False


def _acha(texto, sub):
    """Posições (com sobreposição) de `sub` em `texto`."""
    out, k = [], texto.find(sub)
    while k != -1:
        out.append(k)
        k = texto.find(sub, k + 1)
    return out


def reverte(P):
    """Aplica o `interno` ao contrário (seção 1.5) e o retira. Devolve cópia."""
    Q = copy.deepcopy(P)
    for lista in ('itens', 'lotes', 'simulados', 'discursivas'):
        for o in Q[lista]:
            if 'interno' not in o:
                continue
            for rc in reversed(o['interno']):
                cont_cam = '%s[%s].%s' % (lista, o['id'], rc['campo'])
                obj, rel, cont, chave = resolve(Q, cont_cam)
                t = cont[chave]
                p = rc['pos']
                if t[p:p + len(rc['depois'])] != rc['depois']:
                    raise Falha('C-5', '%s: texto[pos:pos+len(depois)] != depois em %s' % (rc['edicao'], cont_cam))
                cont[chave] = t[:p] + rc['antes'] + t[p + len(rc['depois']):]
            del o['interno']
    return Q
