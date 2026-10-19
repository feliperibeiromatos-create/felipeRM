# -*- coding: utf-8 -*-
"""T-115 (gerador_v1_12, D1 da GBQ, seções 3.4 e 3.5) — erratas de forma (aplicadas na leitura, antes da limpeza; aborto se o "antes" não ocorrer exatamente o número de vezes indicado) e
limpeza da ORDEM C nos textos novos: só deleção, sem texto novo, nas `justificativa` dos itens novos, na ordem L-2, L-1, L-5, L-3, L-4 (config_v112.LIMPEZA). Cada deleção vira um registro do
`interno` do item (`regra` "L-n", `antes` o trecho apagado, `depois` "", `pos` a posição no texto novo) e uma linha T115-L-nnnn do registro de alterações (numeradas na ordem de aplicação das regras
e, dentro da regra, na ordem dos itens no pacote). A conferência `reverte_item` aplica o `interno` ao contrário e devolve a justificativa lida do arquivo final. Não lê relógio."""
import collections, re
import fontes_v112 as F
from fontes_v112 import Falha
import config_v112 as cfg


def aplica_erratas(itens, meta):
    """Troca o enunciado de L1-R137, L1-R167 e L3-R108 (erratas T115-E-01 a 03) e confere a URL (T115-U-01 e 02). Devolve (registros de errata, registros de URL)."""
    por_id = {i['id']: i for i in itens}
    estilo = F.le_insumo(cfg.ESTILO_ARQUIVO)
    regs = []
    for rid, iid, antes, depois, n in cfg.ERRATAS:
        it = por_id.get(iid)
        if it is None:
            raise Falha('C-E', '%s: item %s ausente' % (rid, iid))
        arq = F.le_insumo(meta[iid]['arquivo'])
        if arq.count(antes) != n or it['enunciado'].count(antes) != n:
            raise Falha('C-E', '%s: o "antes" ocorre %d vez(es) no arquivo e %d no enunciado (esperado %d)' % (rid, arq.count(antes), it['enunciado'].count(antes), n))
        if estilo.count(depois) != 1:
            raise Falha('C-E', '%s: o "depois" ocorre %d vez(es) em %s (esperado 1)' % (rid, estilo.count(depois), cfg.ESTILO_ARQUIVO))
        en0 = it['enunciado']
        it['enunciado'] = en0.replace(antes, depois)
        regs.append(dict(edicao=rid, item=iid, antes=en0, depois=it['enunciado'], trecho_antes=antes, trecho_depois=depois, arquivo=meta[iid]['arquivo']))
    # URL (fora do pacote): 3 ocorrências em T113_onda1_D_v2.md (L3-R105: MAPA e Base; L3-R108: Base), a nova 0 vez
    d = F.le_insumo(cfg.URL_ARQUIVO)
    if d.count(cfg.URL_ANTES) != 3 or d.count(cfg.URL_DEPOIS) != 0:
        raise Falha('C-E', 'URL: %d ocorrência(s) da antiga e %d da nova em %s (esperado 3 e 0)' % (d.count(cfg.URL_ANTES), d.count(cfg.URL_DEPOIS), cfg.URL_ARQUIVO))
    dono = collections.Counter()
    atual = None
    for l in d.split('\n'):
        m = re.match(r'^\| (L\d-R\d+) \|', l) or re.match(r'^\*\*(L\d-R\d+)\*\*', l)
        if m:
            atual = m.group(1)
        dono[atual] += l.count(cfg.URL_ANTES)
    esp = {iid: n for _, iid, n in cfg.URL_ERRATA}
    if {k: v for k, v in dono.items() if v} != esp:
        raise Falha('C-E', 'URL: ocorrências por item %s (esperado %s)' % ({k: v for k, v in dono.items() if v}, esp))
    urls = [dict(edicao=e, item=iid, ocorrencias=n, antes=cfg.URL_ANTES, depois=cfg.URL_DEPOIS, arquivo=cfg.URL_ARQUIVO) for e, iid, n in cfg.URL_ERRATA]
    return regs, urls


def limpa_texto(t, regras=None):
    """-> (texto novo, [dict(regra, antes, pos)]) com pos em coordenadas do texto novo (final)."""
    recs = []
    for regra, pad, cat, _ in (regras or cfg.LIMPEZA):
        ms = list(re.finditer(pad, t))
        if len(ms) > 1:
            raise Falha('C-L', 'a regra %s casa %d vezes (no máximo 1 por justificativa)' % (regra, len(ms)))
        if not ms:
            continue
        s, e = ms[0].start(), ms[0].end()
        for r in recs:
            if s < r['pos'] < e:
                raise Falha('C-L', 'a regra %s apaga o ponto de reinserção de outra' % regra)
            if r['pos'] >= e:
                r['pos'] -= e - s
        recs.append(dict(regra=regra, antes=ms[0].group(0), pos=s, cat=cat))
        t = t[:s] + t[e:]
    return t, recs


def limpa_itens(itens):
    """Aplica a limpeza às justificativas; devolve as linhas do registro (T115-L-nnnn) e grava o `interno` em cada item. Confere os itens esperados por regra."""
    por_regra = collections.OrderedDict((r[0], []) for r in cfg.LIMPEZA)
    achados = collections.OrderedDict()
    for it in itens:
        novo, recs = limpa_texto(it['justificativa'])
        if recs:
            achados[it['id']] = (it['justificativa'], novo, recs)
            for r in recs:
                por_regra[r['regra']].append(it['id'])
    for regra, pad, cat, esperado in cfg.LIMPEZA:
        if sorted(por_regra[regra]) != sorted(esperado):
            raise Falha('C-L', '%s: itens %s (esperado %s)' % (regra, sorted(por_regra[regra]), sorted(esperado)))
    linhas = []
    ordem = {i['id']: k for k, i in enumerate(itens)}
    n = 0
    for regra, pad, cat, _ in cfg.LIMPEZA:
        for iid in sorted(por_regra[regra], key=lambda x: ordem[x]):
            n += 1
            r = [x for x in achados[iid][2] if x['regra'] == regra][0]
            r['edicao'] = 'T115-L-%04d' % n
            linhas.append(dict(edicao=r['edicao'], item=iid, regra=regra, cat=cat, antes=r['antes'], pos=r['pos']))
    for it in itens:
        if it['id'] in achados:
            orig, novo, recs = achados[it['id']]
            it['justificativa'] = novo
            lista = sorted(recs, key=lambda r: ('justificativa', r['pos']))
            it['interno'] = [collections.OrderedDict([('edicao', r['edicao']), ('campo', 'justificativa'), ('pos', r['pos']), ('antes', r['antes']), ('depois', ''), ('regra', r['regra']), ('ocorrencias', [])])
                             for r in lista]
    if n != cfg.TOTAIS['delecoes'] or len(achados) != cfg.TOTAIS['itens_limpeza']:
        raise Falha('C-L', '%d deleções em %d itens (esperado %d em %d)' % (n, len(achados), cfg.TOTAIS['delecoes'], cfg.TOTAIS['itens_limpeza']))
    return linhas


def reverte_item(it):
    """Texto da justificativa antes da limpeza, aplicando o `interno` ao contrário (o último registro primeiro)."""
    t = it['justificativa']
    for rc in reversed(it.get('interno', [])):
        p = rc['pos']
        if t[p:p + len(rc['depois'])] != rc['depois']:
            raise Falha('C-5', '%s: texto[pos:pos+len(depois)] != depois' % rc['edicao'])
        t = t[:p] + rc['antes'] + t[p + len(rc['depois']):]
    return t
