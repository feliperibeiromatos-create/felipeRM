# -*- coding: utf-8 -*-
"""T-104 (v1.10) — campo "nucleo" (D-REFORCO-2: "true para os 10 primeiros de cada folha (por ordem de canonização) e false para os demais").
Critério de ordem (D1 da GBQ, saida/pacote/T104_D1_v1_10_2026-10-18.md, seção 3), aplicado a TODOS os itens do pacote (banco e AUTORAL), por itemEdital:
  k1 = data de canonização do item: banco = coluna data_verificacao de banco/banco.csv (entrada do item real verificado);
       lotes canônicos legados (L1, L1C, L2, L3, L4, 4C, A5, 5C, 6A, 6B) = 2026-10-09 (D-CANONICOS; D-LOTE6A-CANONICO e D-LOTE6B-CANONICO: "aceito como canônico em 9/10/2026");
       reforço = 2026-10-18 (data das decisões de aceite);
  k2 = ordem do ato no dia: banco 0 (a verificação precede o ato de aceite do mesmo dia); demais = número da linha da decisão de aceite em DECISOES.md (ordem cronológica);
  k3 = aderência: "direta" antes de "parcial" (T97_reconciliacao, seção 3.5; piso de diretas da D-T97-META-FUNDADOR-RESP);
  k4 = posição do item na lista `itens` do pacote.json (ordem do contrato).
Os 10 primeiros por (k1, k2, k3, k4) em cada folha têm nucleo = true; os demais, false. Folha com menos de 10 itens: todos true."""
import collections, csv, re
from common import P
import config_v110 as cfg

N = 10
ATO_LEGADO = {'L1': 'D-CANONICOS', 'L1C': 'D-CANONICOS', 'L2': 'D-CANONICOS', 'L3': 'D-CANONICOS', 'L4': 'D-CANONICOS', '4C': 'D-CANONICOS',
              'A5': 'D-CANONICOS', '5C': 'D-CANONICOS', '6A': 'D-LOTE6A-CANONICO', '6B': 'D-LOTE6B-CANONICO'}
ATO_REFORCO = [  # (regex do id, decisão de aceite)
    (r'^L1-R(0[1-9]|1[0-8])$', 'D-T89-R1-ACEITE'), (r'^L2-R(0[1-9]|1[0-8])$', 'D-T90-R2-ACEITE'), (r'^L3-R(0[1-9]|1[01])$', 'D-T91-R3-ACEITE'),
    (r'^L6A-R01$', 'D-T92-R4-PARCIAL'), (r'^L6B-R0[12]$', 'D-T102-R4-SALDO'), (r'^L1-R(19|[2-9]\d|1[0-2]\d|130)$', 'D-T96-ONDA2-ACEITE'),
    (r'^L1-R131$', 'D-T103-SALDO-ACEITE'), (r'^L2-R(19|[2-9]\d|1[0-2]\d|130)$', 'D-T97-ONDA3-ACEITE'), (r'^L2-R131$', cfg.ATO_L2R131)]
DATA_LEGADO, DATA_REFORCO = '2026-10-09', '2026-10-18'
# v1.12 (T-115, D1 da GBQ, 4: C-NU): os 189 ids novos (onda 4; onda 1 da ORDEM_V15_F, P1 e P2) e a decisão de aceite de cada um, na ordem dos atos D-T98-ONDA4-ACEITE -> D-V112-BAEF-P1-ACEITE ->
# D-V112-BAEF-P2-ACEITE (linhas de DECISOES.md, depois de todos os atos da v1.11). Preenchido por registra_extra() ou lido de out/stats_<TAG>.json (campo `atos_novos`).
ATOS_EXTRA = {}


def registra_extra(d):
    ATOS_EXTRA.clear()
    ATOS_EXTRA.update(d)


def _carrega_extra():
    import json, os
    from common import OUT
    import config_v112 as c2
    p = os.path.join(OUT, 'stats_%s.json' % c2.TAG)
    if os.path.exists(p):
        registra_extra(json.load(open(p, encoding='utf-8'))['atos_novos'])


def linhas_atos():
    out = {}
    for k, l in enumerate(open(P('DECISOES.md'), encoding='utf-8').read().split('\n'), 1):
        m = re.match(r'^APLICADA [^|]*\| (D-[A-Z0-9-]+) \|', l)
        if m and m.group(1) not in out:
            out[m.group(1)] = k
    return out


def ato_de(iid):
    if not ATOS_EXTRA:
        _carrega_extra()
    if iid in ATOS_EXTRA:
        return ATOS_EXTRA[iid]
    pre = iid.split('-')[0]
    if pre == 'BQ':
        return None
    if '-R' in iid:
        for rx, d in ATO_REFORCO:
            if re.match(rx, iid):
                return d
        raise SystemExit('NUCLEO: id de reforço sem ato: %s' % iid)
    return ATO_LEGADO[pre]


def chaves(pacote):
    banco = {r['id']: r for r in csv.DictReader(open(P('banco/banco.csv'), encoding='utf-8'), delimiter=';')}
    atos = linhas_atos()
    K = collections.OrderedDict()
    for pos, it in enumerate(pacote['itens']):
        iid = it['id']; a = ato_de(iid)
        if a is None:
            k1, k2, a = banco[iid]['data_verificacao'], 0, 'banco (data_verificacao)'
            if not re.match(r'^2026-\d\d-\d\d$', k1):
                raise SystemExit('NUCLEO: data_verificacao ilegível em %s: %r' % (iid, k1))
        else:
            if a not in atos:
                raise SystemExit('NUCLEO: decisão %s ausente de DECISOES.md' % a)
            k1, k2 = (DATA_REFORCO if '-R' in iid else DATA_LEGADO), atos[a]
        K[iid] = dict(folha=it['itemEdital'], chave=(k1, k2, 0 if it['aderencia'] == 'direta' else 1, pos), ato=a)
    return K


def calcula(pacote):
    """{id: bool} e relatório por folha."""
    K = chaves(pacote)
    por_folha = collections.defaultdict(list)
    for iid, v in K.items():
        por_folha[v['folha']].append(iid)
    nuc, rel = {}, collections.OrderedDict()
    for f in sorted(por_folha, key=lambda s: (s[:2], [int(x) for x in s[3:].split('.')])):
        ids = sorted(por_folha[f], key=lambda i: K[i]['chave'])
        for k, iid in enumerate(ids):
            nuc[iid] = k < N
        top = ids[:N]
        rel[f] = dict(itens=len(ids), nucleo=len(top), ids_nucleo=top,
                      parciais_no_nucleo=[i for i in top if K[i]['chave'][2] == 1],
                      atos=dict(collections.Counter(K[i]['ato'] for i in top)))
    return nuc, rel, K
