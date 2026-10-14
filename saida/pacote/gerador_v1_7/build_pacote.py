# -*- coding: utf-8 -*-
"""T-71 — gerador do pacote.json v1.7 (evolução do gerador v1.6/T-67, v1.5/T-61, v1.4/T-57, v1.3/T-56 e T-48). Saída em out/pacote.json; não toca o repositório."""
import json, re, os, sys, collections
from common import *
import common
from p1 import build_lote_p1, LOTES as L1S, to_edital
from p2 import build_lote_p2, LOTES as L2S, discursivas_p2
from banco import build_banco
from edital_p import build_edital
import peg, f4

os.makedirs(OUT, exist_ok=True)

edital = build_edital()
eids = [e['id'] for e in edital]
banco, binfo = build_banco()

# ---------- simulados ----------
def tab_rows(rel):
    rows = []
    for l in read(rel).split('\n'):
        if l.startswith('| ') and re.match(r'^\| \d+ \|', l):
            rows.append([x.strip() for x in l.strip().strip('|').split('|')])
    return rows

def sim_header(rel):
    t = read(rel).split('\n')
    return t[0], t[2]

SIMS = []
GAB_SIM = {}

def avisos_sim0():
    """T-56 / v1.2.1 ponto 5: avisos de montagem 1, 2 e 4 do SIM-0, literais da folha canônica (seção "Avisos de montagem" de
    saida/simulados/simulado_0_v0.2.md), sem a numeração, sem edição. A sublista de um aviso fica na mesma string, com quebras de
    linha e o recuo da folha (3 espaços; D-T53-03)."""
    L = read('saida/simulados/simulado_0_v0.2.md').split('\n')
    i = L.index('## Avisos de montagem') + 1
    fim = i
    while fim < len(L) and not L[fim].startswith('## '):
        fim += 1
    av = {}
    cur = None
    for l in L[i:fim]:
        m = re.match(r'^(\d+)\. (.*)$', l)
        if m:
            cur = int(m.group(1)); av[cur] = m.group(2)
        elif cur is not None and l.startswith(' '):
            av[cur] += '\n' + l
        elif not l.strip():
            cur = None
    assert sorted(av) == list(range(1, 9)), sorted(av)
    return [av[1], av[2], av[4]]

# SIM-0 v0.2 (banco): gabarito.md: | nº | comando | BQ-id | ... ; gab na coluna 10 (conferência na validação)
r0 = tab_rows('saida/simulados/simulado_0_v0.2_gabarito.md')
r0 = [r for r in r0 if re.match(r'^BQ-\d{4}$', r[2])]
assert len(r0) == 60, len(r0)
SIM0 = dict(id='SIM-0', nome='Simulado 0 — diagnóstico (v0.2)', tipo='diagnóstico', versao='v0.2', n=60, itens=[r[2] for r in sorted(r0, key=lambda r: int(r[0]))], avisos=avisos_sim0())
GAB_SIM['SIM-0'] = {r[2]: r[10] for r in r0}
# SIM-1 / SIM-2 / SIM-0-P2 (AUTORAL): | nº | id | lote | [comando] | subitem | gab | ts | just |
def sim_autoral(rel, sid, nome, tipo, n_esp):
    rows = tab_rows(rel)
    rows = [r for r in rows if re.match(r'^(L[123]C?|4C|A5|5C|6A|6B|L4)-', r[1]) or re.match(r'^(L\d+C?-Q\d+|L4-\d+|4C-\d+|A5-\d+|5C-\d+|6[AB]-\d+)$', r[1])]
    ids = [r[1] for r in sorted(rows, key=lambda r: int(r[0]))]
    assert len(ids) == n_esp and len(set(ids)) == n_esp, (sid, len(ids))
    return ids, rows

ids1, rows1 = sim_autoral('saida/simulados/simulado_1_gabarito.md', 'SIM-1', '', '', 40)
gab1 = {r[1]: r[4] for r in rows1}
ids2, rows2 = sim_autoral('saida/simulados/simulado_2_gabarito.md', 'SIM-2', '', '', 40)
gab2 = {r[1]: r[5] for r in rows2}
idsp, rowsp = sim_autoral('saida/simulados/simulado_0_P2_gabarito.md', 'SIM-0-P2', '', '', 25)
gabp = {r[1]: r[5] for r in rowsp}
GAB_SIM['SIM-1'] = gab1; GAB_SIM['SIM-2'] = gab2; GAB_SIM['SIM-0-P2'] = gabp
SIM1 = dict(id='SIM-1', nome='Simulado 1 — P1 final (TI e Dados, itens 5 a 8)', tipo='final', versao='v1', n=40, itens=ids1)
SIM2 = dict(id='SIM-2', nome='Simulado 2 — P2 final (Reconhecimento de Fala, Transcrição e IA, itens 1 a 4)', tipo='final', versao='v1', n=40, itens=ids2)
SIMP = dict(id='SIM-0-P2', nome='Simulado 0-P2 — P2 diagnóstico (Reconhecimento de Fala, Transcrição e IA, itens 1 a 4)', tipo='diagnóstico', versao='v1', n=25, itens=idsp)
simulados = [SIM0, SIM1, SIM2, SIMP]

# ---------- lotes ----------
lotes_raw = [build_lote_p2(s) for s in L2S] + [build_lote_p1(s) for s in L1S]
SRC = {s['id']: s['file'] for s in L2S + L1S}
disc = discursivas_p2([l for l in lotes_raw if l['prova'] == 'P2'])

# D1-c / regra (h): normalização do comando com faixa/lista de numeração de itens
NORM_RX = re.compile(r'(?i)(julgue os itens) (?:de )?(?:[0-9A-Z]+-)?\d+ a (?:[0-9A-Z]+-)?\d+\.')
NORM_LOG = []
def normaliza(cmd, iid):
    m = NORM_RX.search(cmd)
    if not m:
        return cmd, None
    novo = NORM_RX.sub(lambda mm: mm.group(1) + ' a seguir.', cmd)
    NORM_LOG.append((iid, cmd, novo))
    return novo, cmd

autoral = []
ITEM_LOTE = {}
for l in lotes_raw:
    spec = [s for s in L2S + L1S if s['id'] == l['id']][0]
    for it in l['_items']:
        sub = it['sub']
        ie = ('P2-' + sub) if l['prova'] == 'P2' else to_edital(sub)
        cmd, orig = normaliza(it['comando'] or '', it['regid'])
        just = f4.clean(it['regid'], it['justificativa'])
        d = collections.OrderedDict(id=it['regid'], rotulo='AUTORAL', certame='Projeto Câmara 2026', cargo=spec['cargo'], ano=2026,
                 numero=it['numero'], comando=cmd)
        if orig is not None:
            d['comandoOriginal'] = orig
        d.update(textoBase='', enunciado=it['enunciado'], gabarito=it['gabarito'], justificativa=just, itemEdital=ie,
                 aderencia='direta', url=SRC[l['id']])
        if it['volatil']:
            d['volatil'] = True
        autoral.append(dict(d)); ITEM_LOTE[d['id']] = l['id']

# banco: comando com faixa? (esperado 0)
banco_norm = []
for b in banco:
    c, o = normaliza(b['comando'], b['id'])
    if o is not None:
        banco_norm.append(b['id'])
# reordena campos dos itens de banco (comando, [comandoOriginal], textoBase ...) = mesma ordem do AUTORAL
def ordena(d):
    order = ['id', 'rotulo', 'certame', 'cargo', 'ano', 'numero', 'comando', 'comandoOriginal', 'textoBase', 'enunciado', 'gabarito',
             'justificativa', 'itemEdital', 'aderencia', 'url', 'volatil', 'nota']
    return collections.OrderedDict((k, d[k]) for k in order if k in d)
banco = [ordena(b) for b in banco]
autoral = [ordena(a) for a in autoral]
itens = banco + autoral

lotes = []
for l in lotes_raw:
    lote = collections.OrderedDict(id=l['id'], nome=l['nome'], prova=l['prova'], itensEdital=list(l['itensEdital']),
                      resumo=l['resumo'], curso=l['curso'], pares=list(l['pares']),
                      pegadinhas=[collections.OrderedDict(itemEdital=p['itemEdital'], rotulo=p['rotulo'], texto=p['texto']) for p in l['pegadinhas']])
    if l.get('legendaMecanismo'):      # opcional (v1.2.1 ponto 4): só nos lotes cujo arquivo canônico a traz
        lote['legendaMecanismo'] = l['legendaMecanismo']
    lotes.append(lote)
discursivas = [{k: v for k, v in d.items() if not k.startswith('_')} for d in disc]

pacote = collections.OrderedDict(versao=1, geradoEm='2026-10-14', nome='Câmara 2026 — pacote F4 (v1.7)', edital=edital, itens=itens,
              simulados=simulados, lotes=lotes, discursivas=discursivas)
txt = json.dumps(pacote, ensure_ascii=False, indent=1)
with open(os.path.join(OUT, 'pacote.json'), 'w', encoding='utf-8') as f:
    f.write(txt + '\n')

# estatísticas para validação/relatório
stats = dict(errata=common.ERRATA_LOG, f1=common.F1_LOG, f4=f4.F4_LOG, norm=NORM_LOG, banco_norm=banco_norm,
             peg=peg.PEG_INFO, merge=peg.MERGE_LOG, hy=len(common.LOG_HY), log=common.LOG, binfo={k: v for k, v in binfo.items()},
             item_lote=ITEM_LOTE, ts={l['id']: [it['regid'] for it in l['_items'] if it.get('ts')] for l in lotes_raw}, volreg={l['id']: [it['regid'] for it in l['_items'] if it['volatil']] for l in lotes_raw}, gab_sim=GAB_SIM, size=len(txt.encode('utf-8')) + 1,
             adendo2=ADENDO2_TXT if (ADENDO2_TXT := None) else None)
from p2 import ADENDO2
stats['adendo2'] = ADENDO2.get('texto')
json.dump(stats, open(os.path.join(OUT, 'stats.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
print('itens', len(itens), 'banco', len(banco), 'autoral', len(autoral), 'norm', len(NORM_LOG), 'F4', len(f4.F4_LOG), 'F1', len(common.F1_LOG))
print('LOG:', common.LOG)
