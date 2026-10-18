# -*- coding: utf-8 -*-
"""T-94 (v1.9) — leitor dos 4 arquivos finais da onda 1 do reforço (D-REFORCO-1), aceitos pelas D-T89-R1-ACEITE, D-T90-R2-ACEITE, D-T91-R3-ACEITE e D-T92-R4-PARCIAL.
Só leitura. Devolve os 48 itens no formato de item do contrato (14 campos + `volatil` quando verdadeiro), na ordem L1-R01…R18, L2-R01…R18, L3-R01…R11, L6A-R01,
e os metadados de registro (folha, [TS], formato, ponto de julgamento, aderência, VOLÁTIL). Falha (SystemExit) se qualquer contagem divergir das declaradas nas decisões de aceite
(constantes ACEITE abaixo, transcritas das decisões em DECISOES.md, não do arquivo lido) ou se o SHA-256 do arquivo divergir do aceito.
Mapeamento (D1 da GBQ, saida/pacote/T94_D1_v1_9_2026-10-18.md):
- comando: o literal do arquivo ("Julgue o item."; no L6A-R01, a situação hipotética com o comando, que fica inteira no `comando`, regra (h) da v1.2); textoBase "";
- enunciado: a linha do item na Parte 2 (d);
- justificativa: o texto da justificativa na Parte 3 (d-G), literal, sem o cabeçalho (id, gabarito, [TS]) e sem o rótulo ("Justificativa:", "Justificativa (duas linhas):");
  as linhas rotuladas "Base: …" (L1, L2, L3) e "Aderência: …" (L3) NÃO entram: a base fica no arquivo canônico (campo `url`) e a aderência vai para o campo `aderencia`;
- aderencia: "parcial" só nos ids que a decisão de aceite declara (L2-R02, R14, R15; L3-R01, R02, R05), conferido contra o arquivo; demais "direta";
- volatil: true só em L2-R07 e L2-R18 (D-T90-R2-ACEITE), conferido contra o arquivo;
- cargo "Lote 1", "Lote 2", "Lote 3", "Lote 6a" (o do lote de origem no pacote); certame "Projeto Câmara 2026"; ano 2026; numero = o nn do id; url = o caminho do arquivo final;
- ponto de julgamento de L1-R10 e L1-R16: o VIGENTE da seção 4 de saida/gce/T89_reconciliacao_2026-10-18.md, que prevalece sobre a coluna do mapa do v2 (D-T89-R1-ACEITE)."""
import collections, hashlib, re
from common import read, P

ARQ = collections.OrderedDict([
    ('L1', ('saida/gce/L1_reforco_onda1_v2.md', '75e4a5350016482d37f157796a536579614a043e899e3c1239e3262cb0725e05', 'Lote 1', 'P2')),
    ('L2', ('saida/gce/L2_reforco_onda1_v3.md', 'cff8b71e1cf54c910cb16ca3303d86823eeafdfae5507ba7e062b86ae3fe2332', 'Lote 2', 'P2')),
    ('L3', ('saida/gce/L3_reforco_onda1_v3.md', '79404c22205746c18a837b2649c2f5400650cd2a25f104b3b0d8b053cce40db3', 'Lote 3', 'P2')),
    ('L6A', ('saida/gcb/L6_reforco_onda1_v3.md', '58933b0ae7e5729b10ecc03177d88eab355f7963d5b77017e83153c742756e35', 'Lote 6a', 'P1')),
])
T89 = ('saida/gce/T89_reconciliacao_2026-10-18.md', 'L1-R10', 'L1-R16')

# Constantes transcritas das decisões de aceite (DECISOES.md, linhas D-T89-R1-ACEITE, D-T90-R2-ACEITE, D-T91-R3-ACEITE, D-T92-R4-PARCIAL)
ACEITE = {
    'L1': dict(n=18, C=9, E=9, ts=['R01', 'R03', 'R07', 'R09', 'R12', 'R13', 'R17'], vol=[], parcial=[],
               folha={'P2-1.1': (1, 1), 'P2-1.2': (1, 1), 'P2-1.3': (1, 1), 'P2-1.4': (1, 0), 'P2-1.5': (1, 1), 'P2-1.6': (1, 2), 'P2-1.7': (1, 2), 'P2-1.8': (2, 1)}),
    'L2': dict(n=18, C=8, E=10, ts=['R02', 'R03', 'R04', 'R05', 'R09', 'R12', 'R14', 'R15', 'R16', 'R17'], vol=['R07', 'R18'], parcial=['R02', 'R14', 'R15'],
               folha={'P2-2.1': (2, 0), 'P2-2.2': (0, 2), 'P2-2.3': (1, 1), 'P2-2.4': (1, 1), 'P2-2.5': (1, 1), 'P2-2.6': (2, 1), 'P2-2.7': (0, 2), 'P2-2.8': (1, 2)}),
    'L3': dict(n=11, C=6, E=5, ts=['R02', 'R03', 'R06', 'R10', 'R11'], vol=[], parcial=['R01', 'R02', 'R05'],
               folha={'P2-3.1': (1, 1), 'P2-3.2': (1, 1), 'P2-3.3': (1, 1), 'P2-3.4': (2, 0), 'P2-4.2': (1, 0), 'P2-4.3': (0, 2)}),
    'L6A': dict(n=1, C=0, E=1, ts=['R01'], vol=[], parcial=[], folha={'P1-3': (0, 1)}),
}
LOG = []


def falha(msg):
    raise SystemExit('REFORCO: ' + msg)


def texto(rel, sha):
    raw = open(P(rel), 'rb').read()
    h = hashlib.sha256(raw.replace(b'\r\n', b'\n')).hexdigest()
    if h != sha:
        falha('%s: SHA-256 (LF) %s != aceito %s' % (rel, h, sha))
    return raw.decode('utf-8').replace('\r\n', '\n')


def entre(t, ini, fim):
    a = t.index(ini)
    b = t.index(fim, a)
    return t[a + len(ini):b]


def mapa_gce(t, lote):
    """tabela da Parte 1 (1.1 / 1.): id -> colunas."""
    m = collections.OrderedDict()
    for l in t.split('\n'):
        mm = re.match(r'^\| (%s-R\d{2})(?: \(novo\))? \| (.*)\|$' % lote, l)
        if mm and mm.group(1) not in m:      # só a 1ª tabela (mapa dos itens novos); as tabelas por folha repetem ids com outras colunas
            m[mm.group(1)] = [c.strip() for c in mm.group(2).split('|')]
    return m


def parse_l1_l2(lote, t):
    p2 = entre(t, 'PARTE 2/3 — (d) ITENS DO ESTUDANTE', 'FIM DA PARTE 2/3')
    p3 = entre(t, 'PARTE 3/3 — (d-G) GABARITO COMENTADO', 'FIM DA PARTE 3/3')
    mp = mapa_gce(entre(t, 'PARTE 1/3 — MAPA', 'FIM DA PARTE 1/3'), lote)
    L2 = p2.split('\n'); itens = collections.OrderedDict()
    for k, l in enumerate(L2):
        m = re.match(r'^(%s-R\d{2})\. (Julgue o item\.)$' % lote, l)
        if m:
            en = L2[k + 1]
            if not en.strip() or L2[k + 2].strip():
                falha('%s: enunciado não é uma linha única' % m.group(1))
            itens[m.group(1)] = dict(comando=m.group(2), enunciado=en)
    L3 = p3.split('\n')
    for k, l in enumerate(L3):
        m = re.match(r'^(%s-R\d{2})\. ([CE])( \[TS\])?\. (.+)$' % lote, l)
        if m:
            base = L3[k + 1]
            if not base.startswith('Base: ') or L3[k + 2].strip():
                falha('%s: linha "Base:" ausente ou bloco com mais de 2 linhas' % m.group(1))
            d = itens[m.group(1)]
            d.update(gab=m.group(2), ts=bool(m.group(3)), just1=m.group(4), base=base)
    for iid, d in itens.items():
        c = mp[iid]
        d['folha'] = c[0]; d['ponto'] = c[1]; d['formato'] = c[2]
        d['vol_mapa'] = c[4].startswith('S')
        d['parcial_mapa'] = (len(c) > 5 and c[5].upper().startswith('PARCIAL'))
        d['parcial_base'] = bool(re.search(r'Aderência: PARCIAL', d['base']))
        d['vol_gab'] = d['just1'].startswith('VOLÁTIL')
    return itens


def parse_l3(t):
    p2 = entre(t, '## PARTE 2/3 — (d) Itens do estudante', 'FIM DA PARTE 2/3')
    p3 = entre(t, '## PARTE 3/3 — (d-G) Gabarito comentado', 'FIM DA PARTE 3/3')
    cmd = [l for l in p2.split('\n') if l.strip()][0]
    if cmd != 'Julgue o item.':
        falha('L3: comando %r' % cmd)
    L2 = p2.split('\n'); itens = collections.OrderedDict()
    for k, l in enumerate(L2):
        m = re.match(r'^\*\*(L3-R\d{2})\*\* \((P2-\d\.\d)\)$', l)
        if m:
            en = L2[k + 1]
            if not en.strip() or L2[k + 2].strip():
                falha('%s: enunciado não é uma linha única' % m.group(1))
            itens[m.group(1)] = dict(comando=cmd, enunciado=en, folha=m.group(2))
    L3 = p3.split('\n')
    for k, l in enumerate(L3):
        m = re.match(r'^\*\*(L3-R\d{2})\*\* \((P2-\d\.\d)\) Gabarito: ([CE])\.( \[TS\])?$', l)
        if m:
            j, b, a = L3[k + 1], L3[k + 2], L3[k + 3]
            if not (j.startswith('Justificativa: ') and b.startswith('Base: ') and a.startswith('Aderência: ') and not L3[k + 4].strip()):
                falha('%s: bloco do gabarito fora do formato' % m.group(1))
            d = itens[m.group(1)]
            if d['folha'] != m.group(2):
                falha('%s: folha na Parte 2 != Parte 3' % m.group(1))
            d.update(gab=m.group(3), ts=bool(m.group(4)), just1=j[len('Justificativa: '):], base=b,
                     parcial_base=a.startswith('Aderência: parcial'), vol_gab=('Não VOLÁTIL' not in b))
    mp = mapa_gce(entre(t, '## PARTE 1/3 — Mapa', 'FIM DA PARTE 1/3'), 'L3')
    for iid, d in itens.items():
        c = mp[iid]
        if c[0] != d['folha']:
            falha('%s: folha do mapa %s != %s' % (iid, c[0], d['folha']))
        d['ponto'], d['formato'] = c[1], c[2]
        d['vol_mapa'] = c[4].startswith('S'); d['parcial_mapa'] = d['parcial_base']      # o mapa do L3 não tem coluna de aderência: vale a linha "Aderência:" do (d-G)
    return itens


def parse_l6(t):
    p1 = entre(t, '## PARTE 1/3 — Mapa', 'FIM DA PARTE 1/3')
    p2 = entre(t, '## PARTE 2/3 — (d) Itens do estudante', 'FIM DA PARTE 2/3')
    p3 = entre(t, '## PARTE 3/3 — (d-G) Gabarito comentado', 'FIM DA PARTE 3/3')
    L2 = [l for l in p2.split('\n') if l.strip()]
    m = re.match(r'^(L6A-R01) \((P1-3)\)\. AUTORAL\. (.+)$', L2[0])
    if not m or len(L2) != 2:
        falha('L6A: Parte 2 fora do formato')
    d = dict(comando=m.group(3), enunciado=L2[1], folha=m.group(2))
    g = re.search(r'^### L6A-R01 — Gabarito: ([CE])\n(Justificativa \(duas linhas\): (.+))\n\[TS\]: (sim|não)', p3, re.M)
    if not g:
        falha('L6A: gabarito fora do formato')
    d.update(gab=g.group(1), ts=(g.group(4) == 'sim'), just1=g.group(3), base=None,
             vol_gab=bool(re.search(r'^VOLÁTIL: sim', p3, re.M)), parcial_base=False)
    if not re.search(r'^VOLÁTIL: não', p3, re.M):
        falha('L6A: linha "VOLÁTIL: não" ausente')
    c = mapa_gce(p1, 'L6A')['L6A-R01']
    d['ponto'], d['formato'] = c[1], c[2]
    d['vol_mapa'] = c[4].startswith('S'); d['parcial_mapa'] = False
    if c[0] != 'P1-3' or c[5] != 'PRODUZIDO':
        falha('L6A: mapa %r' % c)
    for s in ('L6B-R01', 'L6B-R02'):
        if not re.search(r'^\| %s \|.*\| SUSPENSO' % s, p1, re.M):
            falha('%s deveria estar SUSPENSO' % s)
        if ('%s.' % s) in p2 or ('### %s' % s) in p3:
            falha('%s tem texto/gabarito (não aceito)' % s)
    return collections.OrderedDict([('L6A-R01', d)])


def ponto_t89():
    t = read(T89[0]).replace('\r\n', '\n')
    sec = entre(t, '## 4. Tabela de Correções', '## 5.')
    out = {}
    for l in sec.split('\n'):
        mm = re.match(r'^\| (L1-R1[06]) \| (P2-1\.\d) \| (.+?) \| (.+?) \|$', l)
        if mm:
            out[mm.group(1)] = dict(folha=mm.group(2), antigo=mm.group(3), vigente=mm.group(4))
    if sorted(out) != ['L1-R10', 'L1-R16']:
        falha('T89 seção 4: %s' % sorted(out))
    return out


def carrega():
    """(itens_pacote, meta): lista de dicts de item na ordem do contrato e metadados por id."""
    itens, meta = [], collections.OrderedDict()
    for lote, (rel, sha, cargo, prova) in ARQ.items():
        t = texto(rel, sha)
        if not t.rstrip().endswith('FIM DO LOTE'):
            falha('%s: sem FIM DO LOTE' % rel)
        if lote in ('L1', 'L2'):
            d = parse_l1_l2(lote, t)
        elif lote == 'L3':
            d = parse_l3(t)
        else:
            d = parse_l6(t)
        A = ACEITE[lote]
        ids = list(d)
        esp_ids = ['%s-R%02d' % (lote, k) for k in range(1, A['n'] + 1)]
        if ids != esp_ids:
            falha('%s: ids %s != %s' % (lote, ids, esp_ids))
        if any('gab' not in x for x in d.values()):
            falha('%s: item sem gabarito' % lote)
        cg = collections.Counter(x['gab'] for x in d.values())
        if (cg['C'], cg['E']) != (A['C'], A['E']):
            falha('%s: C/E %s' % (lote, dict(cg)))
        if sorted(k.split('-')[1] for k, x in d.items() if x['ts']) != A['ts']:
            falha('%s: [TS] %s' % (lote, [k for k, x in d.items() if x['ts']]))
        for k, x in d.items():
            r = k.split('-')[1]
            vol = r in A['vol']; par = r in A['parcial']
            if x['vol_mapa'] != vol or x['vol_gab'] != vol:
                falha('%s: VOLÁTIL (mapa %s, gabarito %s, aceite %s)' % (k, x['vol_mapa'], x['vol_gab'], vol))
            if x['parcial_mapa'] != par or x['parcial_base'] != par:
                falha('%s: aderência parcial (mapa %s, base %s, aceite %s)' % (k, x['parcial_mapa'], x['parcial_base'], par))
            x['volatil'] = vol; x['aderencia'] = 'parcial' if par else 'direta'
        pf = collections.defaultdict(lambda: [0, 0])
        for x in d.values():
            pf[x['folha']][0 if x['gab'] == 'C' else 1] += 1
        if {k: tuple(v) for k, v in pf.items()} != A['folha']:
            falha('%s: C/E por folha %s' % (lote, dict(pf)))
        if lote == 'L1':
            pt = ponto_t89()
            for k, v in pt.items():
                if d[k]['ponto'] != v['antigo'] or d[k]['folha'] != v['folha']:
                    falha('%s: ponto do mapa v2 != "desatualizado" da T89 seção 4' % k)
                d[k]['ponto_mapa'] = d[k]['ponto']; d[k]['ponto'] = v['vigente']
                LOG.append('%s: ponto de julgamento = VIGENTE da T89_reconciliacao seção 4' % k)
        for k, x in d.items():
            just = x['just1']
            it = collections.OrderedDict(id=k, rotulo='AUTORAL', certame='Projeto Câmara 2026', cargo=cargo, ano=2026, numero=int(k[-2:]),
                                         comando=x['comando'], textoBase='', enunciado=x['enunciado'], gabarito=x['gab'], justificativa=just,
                                         itemEdital=x['folha'], aderencia=x['aderencia'], url=rel)
            if x['volatil']:
                it['volatil'] = True
            if not it['itemEdital'].startswith(prova + '-'):
                falha('%s: itemEdital %s fora de %s' % (k, it['itemEdital'], prova))
            itens.append(it)
            meta[k] = dict(lote=lote, arquivo=rel, folha=x['folha'], gab=x['gab'], ts=x['ts'], volatil=x['volatil'], aderencia=x['aderencia'],
                           formato=x.get('formato', ''), ponto=x.get('ponto', ''), just1=x['just1'], base=x['base'])
    if len(itens) != 48:
        falha('total %d != 48' % len(itens))
    return itens, meta


if __name__ == '__main__':
    its, mt = carrega()
    c = collections.Counter(i['gabarito'] for i in its)
    print(len(its), dict(c), 'TS', sum(m['ts'] for m in mt.values()), 'vol', [k for k, m in mt.items() if m['volatil']],
          'parcial', [k for k, m in mt.items() if m['aderencia'] == 'parcial'])
    print(LOG)
