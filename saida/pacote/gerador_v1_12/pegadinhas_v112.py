# -*- coding: utf-8 -*-
"""T-115 (gerador_v1_12, D1 da GBQ, seção 3.6) — pegadinhas de pares (ORDEM B) em `lotes[].pegadinhas`. Entrada: GCB, bloco json de T110_pegadinhas_P1_v2.md ({L4, L5, L6A, L6B}: `apos`, `itemEdital`,
`rotulo`, `texto`; `apos` = índice base 0 da última pegadinha existente do mesmo `itemEdital` no lote) e GCE, bloco json de T110_pares_P2_v2.md ({"pegadinhas_novas"}: `lote`, `inserirDepois`,
`itemEdital`, `rotulo`, `texto`; `inserirDepois` = posição base 1 da mesma pegadinha). Normalização (contrato v1.2.9, ponto 2): o gerador calcula, sobre a lista da v1.11, a posição da última pegadinha do
mesmo `itemEdital` no lote e falha se ela não for igual a `apos` (GCB) ou a `inserirDepois − 1` (GCE); insere logo depois (várias no mesmo ponto, na ordem do arquivo); grava só `itemEdital`, `rotulo`,
`texto`, nesta ordem. Rastro: o CSV da GCB (72 linhas) e a tabela "(a) Tabela de rastro" da GCE (67 linhas), uma linha por par no registro de alterações. Não lê relógio."""
import collections, csv, io, re
import fontes_v112 as F
from fontes_v112 import Falha
import config_v112 as cfg

GCB_JSON, GCB_CSV, GCE_MD = 'saida/gcb/T110_pegadinhas_P1_v2.md', 'saida/gcb/T110_registro_P1_v2.csv', 'saida/gce/T110_pares_P2_v2.md'
PREFIXO = 'Não confunda '


def le_entradas():
    """-> lista de dicts (lote, itemEdital, rotulo, texto, apos0 [posição base 0 esperada da última existente], origem, ger), GCB depois GCE, na ordem dos arquivos."""
    out = []
    tb = F.le_insumo(GCB_JSON)
    d = F.bloco_json(tb, GCB_JSON)
    if list(d) != ['L4', 'L5', 'L6A', 'L6B']:
        raise Falha('C-T', '%s: lotes %s' % (GCB_JSON, list(d)))
    for lt, lista in d.items():
        if len(lista) != cfg.PEG_P1[lt]:
            raise Falha('C-T', '%s: %s com %d pegadinhas (esperado %d)' % (GCB_JSON, lt, len(lista), cfg.PEG_P1[lt]))
        for x in lista:
            if list(x) != ['apos', 'itemEdital', 'rotulo', 'texto']:
                raise Falha('C-T', '%s: campos %s' % (GCB_JSON, list(x)))
            out.append(dict(lote=lt, itemEdital=x['itemEdital'], rotulo=x['rotulo'], texto=x['texto'], apos0=x['apos'], origem=GCB_JSON, ger='GCB'))
    tg = F.le_insumo(GCE_MD)
    d = F.bloco_json(tg, GCE_MD)
    if list(d) != ['pegadinhas_novas']:
        raise Falha('C-T', '%s: chaves %s' % (GCE_MD, list(d)))
    c = collections.Counter(x['lote'] for x in d['pegadinhas_novas'])
    if dict(c) != cfg.PEG_P2:
        raise Falha('C-T', '%s: pegadinhas por lote %s (esperado %s)' % (GCE_MD, dict(c), cfg.PEG_P2))
    for x in d['pegadinhas_novas']:
        if list(x) != ['lote', 'inserirDepois', 'itemEdital', 'rotulo', 'texto']:
            raise Falha('C-T', '%s: campos %s' % (GCE_MD, list(x)))
        out.append(dict(lote=x['lote'], itemEdital=x['itemEdital'], rotulo=x['rotulo'], texto=x['texto'], apos0=x['inserirDepois'] - 1, origem=GCE_MD, ger='GCE'))
    return out


def le_rastro():
    """-> (linhas GCB, linhas GCE): GCB do CSV (dict por linha); GCE da tabela (a)."""
    raw = F.le_insumo(GCB_CSV)
    gcb = list(csv.DictReader(io.StringIO(raw, newline='')))
    if len(gcb) != cfg.RASTRO_P1[0] or sum(1 for r in gcb if r['decisao'] == 'CONVERTIDO') != cfg.RASTRO_P1[1] or sum(1 for r in gcb if r['decisao'] == 'DESCARTADO') != cfg.RASTRO_P1[2]:
        raise Falha('C-T', '%s: %d linhas / CONVERTIDO %d / DESCARTADO %d' % (GCB_CSV, len(gcb), sum(1 for r in gcb if r['decisao'] == 'CONVERTIDO'), sum(1 for r in gcb if r['decisao'] == 'DESCARTADO')))
    t = F.le_insumo(GCE_MD)
    i = t.index('## (a) Tabela de rastro')
    gce = []
    for l in t[i:].split('\n'):
        m = re.match(r'^\| (L\d)#(\d+) \| (.*) \| (.*) \| (P2-[\d.]+) \| (CONVERTIDO|DESCARTADO) \| (.*?) \| (.*) \|$', l)
        if m:
            gce.append(dict(lote=m.group(1), n=m.group(2), a=m.group(3), b=m.group(4), itemEdital=m.group(5), decisao=m.group(6), motivo=m.group(7), obs=m.group(8)))
    if len(gce) != cfg.RASTRO_P2[0] or sum(1 for r in gce if r['decisao'] == 'CONVERTIDO') != cfg.RASTRO_P2[1] or sum(1 for r in gce if r['decisao'] == 'DESCARTADO') != cfg.RASTRO_P2[2]:
        raise Falha('C-T', '%s: tabela (a) com %d linhas / CONVERTIDO %d / DESCARTADO %d' % (GCE_MD, len(gce), sum(1 for r in gce if r['decisao'] == 'CONVERTIDO'), sum(1 for r in gce if r['decisao'] == 'DESCARTADO')))
    return gcb, gce


def aplica(P):
    """Insere as pegadinhas no pacote P (modifica-o). -> dict com: novas = [(lote, indice final, entrada)], remap = {lote: {indice da base: indice novo}}, rastro = linhas do registro."""
    ent = le_entradas()
    por_lote = collections.OrderedDict((L['id'], L) for L in P['lotes'])
    ins = collections.defaultdict(list)       # (lote, posição base 0 da última existente) -> [entradas na ordem do arquivo]
    for e in ent:
        L = por_lote[e['lote']]
        peg = L['pegadinhas']
        mesmas = [k for k, g in enumerate(peg) if g['itemEdital'] == e['itemEdital']]
        if not mesmas:
            raise Falha('C-2', '%s/%s: nenhuma pegadinha existente do itemEdital %s' % (e['lote'], e['ger'], e['itemEdital']))
        ult = mesmas[-1]
        if ult != e['apos0']:
            raise Falha('C-2', '%s: a última pegadinha existente de %s está na posição %d (base 0), mas o arquivo manda %d' % (e['lote'], e['itemEdital'], ult, e['apos0']))
        if e['rotulo'] not in {peg[k]['rotulo'] for k in mesmas}:
            raise Falha('C-2', '%s: rótulo %r não é o de nenhuma pegadinha existente de %s' % (e['lote'], e['rotulo'], e['itemEdital']))
        if not e['texto'].startswith(PREFIXO):
            raise Falha('C-2', '%s: o texto não começa por "Não confunda "' % e['lote'])
        ins[(e['lote'], ult)].append(e)
    novas, remap = [], {}
    for lt, L in por_lote.items():
        antigo = L['pegadinhas']
        novo, rm = [], {}
        for k, g in enumerate(antigo):
            rm[k] = len(novo)
            novo.append(g)
            for e in ins.get((lt, k), []):
                novas.append((lt, len(novo), e))
                novo.append(collections.OrderedDict([('itemEdital', e['itemEdital']), ('rotulo', e['rotulo']), ('texto', e['texto'])]))
        L['pegadinhas'] = novo
        remap[lt] = rm
    for lt, (a, b) in cfg.RAIZ_PEGADINHAS.items():
        if len(por_lote[lt]['pegadinhas']) != b:
            raise Falha('C-2', '%s: %d pegadinhas (esperado %d)' % (lt, len(por_lote[lt]['pegadinhas']), b))
    if len(novas) != cfg.TOTAIS['pegadinhas_novas'] or sum(len(L['pegadinhas']) for L in P['lotes']) != cfg.TOTAIS['pegadinhas']:
        raise Falha('C-2', 'total de pegadinhas')
    # rastro: GCB (CSV; " || " separa as pegadinhas de um par), GCE (tabela (a); a n-ésima CONVERTIDA do lote é a n-ésima pegadinha do lote no arquivo)
    gcb, gce = le_rastro()
    rastro = []
    usadas = set()
    for r in gcb:
        lt = r['lote']
        if r['decisao'] == 'CONVERTIDO':
            caminhos, textos = [], r['texto'].split(' || ')
            for tx in textos:
                ach = [(l_, i_, e) for (l_, i_, e) in novas if l_ == lt and e['ger'] == 'GCB' and e['texto'] == tx and (l_, i_) not in usadas]
                if not ach:
                    raise Falha('C-T', 'rastro %s/%s: texto sem correspondente na lista de pegadinhas' % (lt, r['par_id']))
                usadas.add((ach[0][0], ach[0][1]))
                caminhos.append('lotes[%s].pegadinhas[%d]' % (lt, ach[0][1]))
                if ach[0][2]['itemEdital'] != r['itemEdital']:
                    raise Falha('C-T', 'rastro %s/%s: itemEdital' % (lt, r['par_id']))
            rastro.append(dict(ger='GCB', arquivo=GCB_CSV, par='%s/%s' % (lt, r['par_id']), lote=lt, a=r['a'], b=r['b'], itemEdital=r['itemEdital'], decisao='CONVERTIDO', motivo='', caminhos=caminhos, textos=textos))
        else:
            rastro.append(dict(ger='GCB', arquivo=GCB_CSV, par='%s/%s' % (lt, r['par_id']), lote=lt, a=r['a'], b=r['b'], itemEdital=r['itemEdital'], decisao='DESCARTADO', motivo=r['motivo'], caminhos=[], textos=[]))
    nao_usadas_gcb = [(l_, i_) for (l_, i_, e) in novas if e['ger'] == 'GCB' and (l_, i_) not in usadas]
    if nao_usadas_gcb:
        raise Falha('C-T', 'pegadinhas da GCB sem linha de rastro: %s' % nao_usadas_gcb[:3])
    fila = collections.defaultdict(list)      # (lote, itemEdital) -> [(índice final, entrada)] na ordem do arquivo (as linhas do rastro vêm na ordem dos pares; casam por itemEdital, em ordem)
    for e in ent:
        if e['ger'] == 'GCE':
            ach = [(l_, i_, x) for (l_, i_, x) in novas if x is e]
            fila[(e['lote'], e['itemEdital'])].append((ach[0][1], e))
    for r in gce:
        lt = r['lote']
        if r['decisao'] == 'CONVERTIDO':
            if not fila[(lt, r['itemEdital'])]:
                raise Falha('C-T', 'rastro %s#%s: CONVERTIDO sem pegadinha correspondente em %s' % (lt, r['n'], r['itemEdital']))
            i_, e = fila[(lt, r['itemEdital'])].pop(0)
            rastro.append(dict(ger='GCE', arquivo=GCE_MD, par='%s#%s' % (lt, r['n']), lote=lt, a=r['a'], b=r['b'], itemEdital=r['itemEdital'], decisao='CONVERTIDO', motivo='',
                               caminhos=['lotes[%s].pegadinhas[%d]' % (lt, i_)], textos=[e['texto']]))
        else:
            rastro.append(dict(ger='GCE', arquivo=GCE_MD, par='%s#%s' % (lt, r['n']), lote=lt, a=r['a'], b=r['b'], itemEdital=r['itemEdital'], decisao='DESCARTADO', motivo=r['motivo'], caminhos=[], textos=[]))
    if any(fila.values()):
        raise Falha('C-T', 'pegadinhas da GCE sem linha de rastro')
    return dict(novas=novas, remap=remap, rastro=rastro)
