# -*- coding: utf-8 -*-
"""T-115 (gerador_v1_12, D1 da GBQ, seção 3.3) — leitor dos itens novos da v1.12: onda 4 (D-T98-ONDA4-ACEITE, 84 itens, L3-R12 a L3-R95), onda 1 da ORDEM_V15_F, P1 (D-V112-BAEF-P1-ACEITE, 7 itens,
L4-R01 a L4-R07, bloco json de 14 campos) e P2 (D-V112-BAEF-P2-ACEITE, 98 itens; fora os 5 vagos e os 2 diferidos). Só leitura. Os 3 formatos dos arquivos da GCE são aceitos:
- partes: "PARTE n/3" até a primeira linha entre "FIM DA PARTE n/3", "PARTE n+1/3" e "FIM DO LOTE"; a última linha não vazia é "FIM DO LOTE";
- MAPA (Parte 1): primeira linha de tabela de cada id; formato novo (Parte 2 "**id** (folha)" + enunciado; Parte 3 "**id** (folha)[ —] Gabarito: G[.][ [TS]][ (espelho)]…" + "Justificativa: texto");
  formato antigo (Parte 2 "id. Julgue o item." + linha única; Parte 3 "id. G[ [TS]][ (espelho)]. texto", a justificativa é o texto, literal).
Falha (Falha, código de saída 1) se ids ou ordem diferirem entre MAPA, Parte 2 e Parte 3, se a folha do MAPA diferir da das Partes 2 e 3, se faltar "Justificativa:" no formato novo, se um id já existir no pacote
v1.11 ou se uma constante de aceite (config_v112.ACEITE, transcrita das decisões) divergir do lido. Não lê relógio."""
import collections, re
import fontes_v112 as F
from fontes_v112 import Falha
import config_v112 as cfg

LOG = []
RX_PARTE = r'^(?:## )?PARTE %d/3\b[^\n]*$'


def num(iid):
    return int(iid.split('-R')[1])


def lote_de(iid):
    return iid.split('-')[0]


def particiona(t, rel):
    """{1: texto, 2: texto, 3: texto} das três partes."""
    ls = t.split('\n')
    nz = [l for l in ls if l.strip()]
    if not nz or nz[-1].strip() != 'FIM DO LOTE':
        raise Falha('C-N1', '%s: a última linha não vazia não é "FIM DO LOTE"' % rel)
    ini = {}
    for n in (1, 2, 3):
        c = [k for k, l in enumerate(ls) if re.match(RX_PARTE % n, l)]
        if len(c) != 1:
            raise Falha('C-N1', '%s: %d linha(s) de abertura da PARTE %d/3 (esperado 1)' % (rel, len(c), n))
        ini[n] = c[0]
    if not ini[1] < ini[2] < ini[3]:
        raise Falha('C-N1', '%s: partes fora de ordem' % rel)
    out = {}
    for n in (1, 2, 3):
        fim = len(ls)
        for k in range(ini[n] + 1, len(ls)):
            l = ls[k].strip()
            if l == 'FIM DA PARTE %d/3' % n or re.match(RX_PARTE % (n + 1), ls[k]) or l == 'FIM DO LOTE':
                fim = k
                break
        out[n] = '\n'.join(ls[ini[n] + 1:fim])
    return out


def mapa(p1):
    """id -> colunas [folha, ponto, formato, base, VOLÁTIL, aderência], primeira linha de tabela de cada id."""
    m = collections.OrderedDict()
    for l in p1.split('\n'):
        mm = re.match(r'^\| (L\d-R\d{2,3}) \| (.*)\|$', l)
        if mm and mm.group(1) not in m:
            c = [x.strip() for x in mm.group(2).split('|')]
            if len(c) < 6:
                raise Falha('C-N1', '%s: linha do MAPA com %d colunas' % (mm.group(1), len(c)))
            m[mm.group(1)] = c
    return m


def vol_mapa(iid, c):
    v = c[4].strip().lower()
    if v.startswith('n'):
        return False
    if v.startswith('s') or v.startswith('volátil'):
        return True
    raise Falha('C-N1', '%s: coluna VOLÁTIL ilegível: %r' % (iid, c[4]))


def parse_p2(p2, rel):
    """-> (formato, [(id, folha ou None, enunciado)])."""
    ls = p2.split('\n')
    novo = [k for k, l in enumerate(ls) if re.match(r'^\*\*L\d-R\d+\*\* \(', l)]
    out = []
    if novo:
        corpo = [l for l in ls[:novo[0]] if l.strip() and not set(l.strip()) <= {'='}]
        if corpo != ['Julgue o item.']:
            raise Falha('C-N1', '%s: a abertura da Parte 2 não é só "Julgue o item." (%r)' % (rel, corpo[:2]))
        for k in novo:
            m = re.match(r'^\*\*(L\d-R\d+)\*\* \((P\d-[\d.]+)\)$', ls[k])
            if not m:
                raise Falha('C-N1', '%s: cabeçalho de item fora do formato: %r' % (rel, ls[k][:60]))
            j = k + 1
            par = []
            while j < len(ls) and ls[j].strip():
                par.append(ls[j]); j += 1
            if len(par) != 1:
                raise Falha('C-N1', '%s: o enunciado de %s não é um parágrafo de uma linha (%d linhas)' % (rel, m.group(1), len(par)))
            out.append((m.group(1), m.group(2), par[0]))
        return 'novo', out
    for k, l in enumerate(ls):
        m = re.match(r'^(L\d-R\d{2,3})\. (.*)$', l)
        if m:
            if m.group(2) != 'Julgue o item.':
                raise Falha('C-N1', '%s: comando de %s: %r' % (rel, m.group(1), m.group(2)))
            en = ls[k + 1] if k + 1 < len(ls) else ''
            if not en.strip() or (k + 2 < len(ls) and ls[k + 2].strip()):
                raise Falha('C-N1', '%s: o enunciado de %s não é uma linha única' % (rel, m.group(1)))
            out.append((m.group(1), None, en))
    return 'antigo', out


def parse_p3(p3, fmt, rel):
    """-> [(id, folha ou None, gab, ts, espelho, just)]."""
    ls = p3.split('\n')
    out = []
    if fmt == 'novo':
        for k, l in enumerate(ls):
            if re.match(r'^\*\*L\d-R\d+\*\*', l):
                m = re.match(r'^\*\*(L\d-R\d+)\*\* \((P\d-[\d.]+)\)(?: —)? Gabarito: ([CE])\.?( \[TS\])?( \(espelho\))?(?:[ .—].*)?$', l)
                if not m:
                    raise Falha('C-N1', '%s: cabeçalho do gabarito fora do formato: %r' % (rel, l[:80]))
                nx = ls[k + 1] if k + 1 < len(ls) else ''
                if not nx.startswith('Justificativa: ') or not nx[len('Justificativa: '):].strip():
                    raise Falha('C-N1', '%s: %s sem a linha "Justificativa:"' % (rel, m.group(1)))
                out.append((m.group(1), m.group(2), m.group(3), bool(m.group(4)), bool(m.group(5)), nx[len('Justificativa: '):]))
    else:
        for k, l in enumerate(ls):
            m = re.match(r'^(L\d-R\d{2,3})\. ([CE])( \[TS\])?( \(espelho\))?\. (.+)$', l)
            if m:
                out.append((m.group(1), None, m.group(2), bool(m.group(3)), bool(m.group(4)), m.group(5)))
            elif re.match(r'^L\d-R\d', l):
                raise Falha('C-N1', '%s: linha de cabeçalho fora do formato na Parte 3: %r' % (rel, l[:60]))
    return out


def le_arquivo_gce(rel):
    """-> OrderedDict id -> dict(enunciado, gab, ts, espelho, just, folha, ponto, formato, vol, parcial, arquivo)."""
    t = F.le_insumo(rel)
    P = particiona(t, rel)
    mp = mapa(P[1])
    fmt, p2 = parse_p2(P[2], rel)
    p3 = parse_p3(P[3], fmt, rel)
    i1, i2, i3 = list(mp), [x[0] for x in p2], [x[0] for x in p3]
    if not (i1 == i2 == i3):
        raise Falha('C-N1', '%s: ids ou ordem diferentes entre MAPA (%d), Parte 2 (%d) e Parte 3 (%d)' % (rel, len(i1), len(i2), len(i3)))
    d = collections.OrderedDict()
    for (iid, f2, en), (iid3, f3, g, ts, esp, just) in zip(p2, p3):
        c = mp[iid]
        if f2 is not None and (f2 != c[0] or f3 != c[0]):
            raise Falha('C-N1', '%s: folha do MAPA (%s) diferente da das Partes 2 e 3 (%s, %s)' % (iid, c[0], f2, f3))
        d[iid] = dict(enunciado=en, gab=g, ts=ts, espelho=esp, just=just, folha=c[0], ponto=c[1], formato=c[2], vol=vol_mapa(iid, c), parcial=c[5].strip().lower().startswith('parcial'),
                      arquivo=rel, fmt_arquivo=fmt, base_mapa=c[3])
    return d


def le_p1():
    """Bloco json único de T113_onda1_P1_v2.md: 7 itens com os 14 campos, tomados como estão."""
    rel = cfg.GRUPOS['F1P1']['arquivos'][0]
    t = F.le_insumo(rel)
    lista = F.bloco_json(t, rel, 0, 1)
    cols = ['id', 'rotulo', 'certame', 'cargo', 'ano', 'numero', 'comando', 'textoBase', 'enunciado', 'gabarito', 'justificativa', 'itemEdital', 'aderencia', 'url']
    if not isinstance(lista, list) or len(lista) != 7:
        raise Falha('C-N1', '%s: o bloco json não é uma lista de 7 itens' % rel)
    for x in lista:
        if list(x) != cols:
            raise Falha('C-N1', '%s: %s com campos %s (esperado os 14 do contrato)' % (rel, x.get('id'), list(x)))
    # conferência cruzada com a Parte 4 (gabarito e [TS])
    p4 = t.split('## PARTE 4/4')[1].split('### Tabela de proveniência')[0]
    ts = {}
    gab = {}
    fmt = {}
    for blk in re.split(r'^### (?=L4-R\d\d )', p4, flags=re.M)[1:]:
        iid = blk[:6]
        gab[iid] = re.search(r'^Gabarito: ([CE])', blk, re.M).group(1)
        ts[iid] = re.search(r'^\[TS\]: (sim|não)\.', blk, re.M).group(1) == 'sim'
        fmt[iid] = re.search(r'Formato: ([^.]*)\.', blk).group(1)
        j = re.search(r'^Justificativa \(duas linhas\): (.*)$', blk, re.M).group(1)
        x = [y for y in lista if y['id'] == iid][0]
        if j != x['justificativa']:
            LOG.append('%s: justificativa do bloco json difere da da Parte 4 (vale o bloco json, "tomado como está")' % iid)
    for x in lista:
        if gab.get(x['id']) != x['gabarito']:
            raise Falha('C-N1', '%s: gabarito do json (%s) difere da Parte 4 (%s)' % (x['id'], x['gabarito'], gab.get(x['id'])))
    return lista, ts, rel, fmt


def carrega(ids_base):
    """-> (itens, meta). itens: lista de OrderedDict de item (14 campos + volatil quando verdadeiro), na ordem do D1 3.3; meta: id -> dict. ids_base: ids do pacote v1.11."""
    itens, meta = [], collections.OrderedDict()
    vagos_lidos, dif_lidos = [], []
    for gk, g in cfg.GRUPOS.items():
        A = cfg.ACEITE[gk]
        d = collections.OrderedDict()
        if gk == 'F1P1':
            lista, ts, rel, fmt = le_p1()
            for x in lista:
                it = collections.OrderedDict(x)
                d[x['id']] = dict(item=it, gab=x['gabarito'], ts=ts[x['id']], espelho=False, vol=False, parcial=x['aderencia'] == 'parcial', folha=x['itemEdital'], arquivo=rel,
                                  just_arquivo=x['justificativa'], formato=fmt[x['id']], ponto='', fmt_arquivo='json')
        else:
            for rel in g['arquivos']:
                x = le_arquivo_gce(rel)
                for iid, v in x.items():
                    if iid in d:
                        raise Falha('C-N1', '%s: id repetido entre arquivos' % iid)
                    d[iid] = v
            if gk == 'F1P2':
                for iid in list(d):
                    if iid in cfg.VAGOS:
                        vagos_lidos.append(iid); del d[iid]
                    elif iid in cfg.DIFERIDOS:
                        dif_lidos.append(iid); del d[iid]
        # constantes de aceite
        if len(d) != A['n']:
            raise Falha('C-N1', '%s: %d itens (esperado %d)' % (gk, len(d), A['n']))
        cg = collections.Counter(v['gab'] for v in d.values())
        if (cg['C'], cg['E']) != (A['C'], A['E']):
            raise Falha('C-N1', '%s: C/E %s (esperado %d/%d)' % (gk, dict(cg), A['C'], A['E']))
        nts = sum(1 for v in d.values() if v['ts'])
        if nts != A['ts']:
            raise Falha('C-N1', '%s: [TS] %d (esperado %d)' % (gk, nts, A['ts']))
        vol = [k for k, v in d.items() if v['vol']]
        if vol != A['vol']:
            raise Falha('C-N1', '%s: VOLÁTEIS %s (esperado %s)' % (gk, vol, A['vol']))
        par = [k for k, v in d.items() if v['parcial']]
        if sorted(par) != sorted(A['parcial']):
            raise Falha('C-N1', '%s: PARCIAIS %s (esperado %s)' % (gk, par, A['parcial']))
        pf = collections.Counter(v['folha'] for v in d.values())
        if dict(pf) != A['folha']:
            raise Falha('C-N1', '%s: itens por folha %s (esperado %s)' % (gk, dict(pf), A['folha']))
        if gk == 'ONDA4':
            esp = ['L3-R%d' % k for k in range(12, 96)]
            if list(d) != esp:
                raise Falha('C-N1', 'ONDA4: ids lidos diferem de L3-R12 a L3-R95 (ou a ordem)')
        if gk == 'F1P1' and list(d) != ['L4-R0%d' % k for k in range(1, 8)]:
            raise Falha('C-N1', 'F1P1: ids diferem de L4-R01 a L4-R07')
        if gk == 'F1P2':
            pt = []
            for rel in g['arquivos']:
                pt.append(sum(1 for k, v in d.items() if v['arquivo'] == rel))
            esp = [a[0] for a in A['partes']]
            if pt != esp:
                raise Falha('C-N1', 'F1P2: itens por parte %s (esperado %s)' % (pt, esp))
            for rel, (n, c, e) in zip(g['arquivos'], A['partes']):
                ce = collections.Counter(v['gab'] for v in d.values() if v['arquivo'] == rel)
                if (ce['C'], ce['E']) != (c, e):
                    raise Falha('C-N1', 'F1P2: C/E da parte %s %s (esperado %d/%d)' % (rel, dict(ce), c, e))
            if sorted(vagos_lidos) != sorted(cfg.VAGOS) or sorted(dif_lidos) != sorted(cfg.DIFERIDOS):
                raise Falha('C-N1', 'F1P2: vagos/diferidos lidos %s %s diferem da decisão' % (vagos_lidos, dif_lidos))
        if gk == 'ONDA4':
            pt = [sum(1 for v in d.values() if v['arquivo'] == rel) for rel in g['arquivos']]
            if pt != A['partes']:
                raise Falha('C-N1', 'ONDA4: itens por parte %s (esperado %s)' % (pt, A['partes']))
        for iid, v in d.items():
            if iid in ids_base:
                raise Falha('C-N1', '%s já existe no pacote v1.11' % iid)
            if gk == 'F1P1':
                it = v['item']
            else:
                lt = lote_de(iid)
                it = collections.OrderedDict(id=iid, rotulo='AUTORAL', certame='Projeto Câmara 2026', cargo=cfg.CARGO[lt], ano=2026, numero=num(iid), comando='Julgue o item.',
                                             textoBase='', enunciado=v['enunciado'], gabarito=v['gab'], justificativa=v['just'], itemEdital=v['folha'],
                                             aderencia='parcial' if v['parcial'] else 'direta', url=v['arquivo'])
                v['just_arquivo'] = v['just']
                if v['vol']:
                    it['volatil'] = True
                if not it['itemEdital'].startswith(('P2-' if lt in ('L1', 'L2', 'L3') else 'P1-')):
                    raise Falha('C-N1', '%s: itemEdital %s fora da prova' % (iid, it['itemEdital']))
            if iid in meta:
                raise Falha('C-N1', '%s: id repetido entre grupos' % iid)
            itens.append(it)
            meta[iid] = dict(grupo=gk, ato=g['ato'], lote=lote_de(iid), arquivo=v['arquivo'], folha=v['folha'], gab=v['gab'], ts=v['ts'], espelho=v['espelho'], volatil=v['vol'],
                             aderencia='parcial' if v['parcial'] else 'direta', formato=v['formato'], ponto=v['ponto'], just_arquivo=v['just_arquivo'], fmt_arquivo=v['fmt_arquivo'],
                             base_mapa=v.get('base_mapa', ''))
    if len(itens) != cfg.TOTAIS['novos']:
        raise Falha('C-N1', 'total de itens novos %d (esperado %d)' % (len(itens), cfg.TOTAIS['novos']))
    return itens, meta, dict(vagos=vagos_lidos, diferidos=dif_lidos)


if __name__ == '__main__':
    import json, os
    sys_ids = set()
    its, mt, info = carrega(sys_ids)
    c = collections.Counter(i['gabarito'] for i in its)
    print(len(its), dict(c), 'vol', sum(1 for m in mt.values() if m['volatil']), 'parcial', sum(1 for m in mt.values() if m['aderencia'] == 'parcial'), 'ts', sum(1 for m in mt.values() if m['ts']))
    print(info, LOG)
