# -*- coding: utf-8 -*-
"""T-94 — validação do pacote.json v1.9 e do pacote_estudante.json v1.9-E (passo 4 do rodar_tudo.sh da v1_9). Substitui, na v1.9, o validate.py herdado (que valida a v1.8 contra
as fontes da v1.8 e não se aplica às fontes de hoje: banco/banco.csv e Lotes 4/5-C/2 mudaram depois da v1.8; D1 da GBQ, T94_D1_v1_9_2026-10-18.md, seção 1.3).
Três blocos: (A) forma e contrato sobre os 334 itens; (B) os 48 itens de reforço contra os arquivos finais (leitura própria, sem reforco.py: busca literal do enunciado,
do comando e da justificativa e regex própria de gabarito, folha, [TS], VOLÁTIL e aderência) e contra as decisões de aceite; (C) registro GBQ adendo 1 e camada do estudante.
Uso: python3 -I -B _run.py validate_v19.py [pacote.json] [pacote_estudante.json]. Grava out/validate_v19.json só quando roda sobre out/. Código 1 se houver falha."""
import collections, json, os, re, sys
from common import OUT, REPO, read
from edital_p import build_edital

PJ = sys.argv[1] if len(sys.argv) > 1 else os.path.join(OUT, 'pacote.json')
PE = sys.argv[2] if len(sys.argv) > 2 else os.path.join(OUT, 'pacote_estudante.json')
raw = open(PJ, encoding='utf-8').read()
new = json.loads(raw)
res = []


def chk(n, ok, extra=''):
    res.append(dict(n=n, ok=bool(ok), extra=extra))
    print('OK   ' if ok else 'FALHA', n, extra)


items = new['itens']; byid = {i['id']: i for i in items}; ids = [i['id'] for i in items]
REF = [i['id'] for i in items if re.match(r'^L(?:1|2|3|6A|6B)-R\d{2}$', i['id'])]
# ------------------------------------------------------------------ (A) forma e contrato (334)
chk('(A) JSON termina em 1 newline; serialização canônica (indent=1, ensure_ascii=False)', raw.endswith('\n') and not raw.endswith('\n\n') and json.dumps(new, ensure_ascii=False, indent=1) + '\n' == raw)
chk('(A) chaves de topo, versao 1, nome "(v1.9)", geradoEm 2026-10-18', list(new) == ['versao', 'geradoEm', 'nome', 'edital', 'itens', 'simulados', 'lotes', 'discursivas']
    and new['versao'] == 1 and new['nome'] == 'Câmara 2026 — pacote F4 (v1.9)' and new['geradoEm'] == '2026-10-18')
chk('(A) 334 itens, 0 id duplicado', len(ids) == 334 and len(set(ids)) == 334, str(len(ids)))
OBR = ['id', 'rotulo', 'certame', 'cargo', 'ano', 'numero', 'comando', 'textoBase', 'enunciado', 'gabarito', 'justificativa', 'itemEdital', 'aderencia', 'url']
chk('(A) 14 campos obrigatórios em todos; tipos (ano/numero int; demais str)', all(all(k in i for k in OBR) for i in items)
    and all(isinstance(i['ano'], int) and isinstance(i['numero'], int) and all(isinstance(i[k], str) for k in OBR if k not in ('ano', 'numero')) for i in items))
chk('(A) campos extras só comandoOriginal, volatil, nota (nenhum campo novo; "nucleo" ausente)', all(set(i) - set(OBR) <= {'comandoOriginal', 'volatil', 'nota'} for i in items) and '"nucleo"' not in raw)
chk('(A) gabarito C/E, enunciado e id não vazios', all(i['id'] and i['enunciado'].strip() and i['gabarito'] in ('C', 'E') for i in items))
chk('(A) aderencia direta|parcial; rotulo permitido (0 CEBRASPE_ESTILO); volatil só true', all(i['aderencia'] in ('direta', 'parcial') for i in items)
    and all(i['rotulo'] in ('CEBRASPE_OFICIAL', 'CEBRASPE_ANALOGA', 'OUTRA_OFICIAL', 'AUTORAL') for i in items) and all(i.get('volatil', True) is True for i in items))
eids = [e['id'] for e in build_edital()]
chk('(A) todo itemEdital existe no edital (47 entradas)', all(i['itemEdital'] in eids for i in items) and len(new['edital']) == 47)
for pat in ['QA PENDENTE', 'ENTREGA DE LOTE', 'FIM DA PARTE', 'FIM DO LOTE', 'PARTE 2/3', 'PARTE 3/3', '=====', 'Derep, antigo DETAQ', 'CEBRASPE_ESTILO']:
    chk('(A) 0 ocorrência de %r' % pat, pat not in raw)
chk('(A) justificativa não vazia em AUTORAL e vazia no banco', all((i['justificativa'].strip() != '') == (i['rotulo'] == 'AUTORAL') for i in items))
c = collections.Counter(i['gabarito'] for i in items)
cont = dict(itens=len(items), C=c['C'], E=c['E'], banco=sum(i['rotulo'] != 'AUTORAL' for i in items), AUTORAL=sum(i['rotulo'] == 'AUTORAL' for i in items),
            volatil=sum(bool(i.get('volatil')) for i in items), parcial=sum(i['aderencia'] == 'parcial' for i in items), reforco=len(REF))
chk('(A) contagens: 334 itens, 172 C / 162 E, banco 106, AUTORAL 228, volatil 25, parcial 45 (39 banco + 6 reforço), reforço 48',
    cont == dict(itens=334, C=172, E=162, banco=106, AUTORAL=228, volatil=25, parcial=45, reforco=48), str(cont))
chk('(A) os 48 de reforço são os 48 últimos itens, na ordem L1-R01…R18, L2-R01…R18, L3-R01…R11, L6A-R01; nenhum L6B-R',
    REF == ids[286:] == ['L1-R%02d' % k for k in range(1, 19)] + ['L2-R%02d' % k for k in range(1, 19)] + ['L3-R%02d' % k for k in range(1, 12)] + ['L6A-R01'])
S = {s['id']: s for s in new['simulados']}
chk('(A) simulados: 4 (SIM-0, SIM-1, SIM-2, SIM-0-P2); nenhum item de reforço em simulado; todo id de simulado existe', list(S) == ['SIM-0', 'SIM-1', 'SIM-2', 'SIM-0-P2']
    and not any(x in REF for s in S.values() for x in s['itens']) and all(x in byid for s in S.values() for x in s['itens']))
fin = [x for sid in ('SIM-1', 'SIM-2') for x in S[sid]['itens']]
chk('(A) simulados finais sem item VOLÁTIL ou parcial; nenhum simulado com L4-11 e BQ-0010 (TRF6 2024, Cargo 2, item 81) juntos (regra R2 do registro)',
    not any(byid[x].get('volatil') or byid[x]['aderencia'] == 'parcial' for x in fin) and not any({'L4-11', 'BQ-0010'} <= set(s['itens']) for s in S.values())
    and byid['BQ-0010']['numero'] == 81 and byid['BQ-0010']['certame'].startswith('TRF6'))
# ------------------------------------------------------------------ (B) reforço × arquivos finais e decisões de aceite (leitura própria)
ARQ = {'L1': 'saida/gce/L1_reforco_onda1_v2.md', 'L2': 'saida/gce/L2_reforco_onda1_v3.md', 'L3': 'saida/gce/L3_reforco_onda1_v3.md', 'L6A': 'saida/gcb/L6_reforco_onda1_v3.md'}
TXT = {k: read(v).replace('\r\n', '\n') for k, v in ARQ.items()}
CARGO = {'L1': 'Lote 1', 'L2': 'Lote 2', 'L3': 'Lote 3', 'L6A': 'Lote 6a'}
def lote(iid): return iid.split('-')[0]
def parte(t, n):
    a = t.index('PARTE %d/3' % n); b = t.index('FIM DA PARTE %d/3' % n, a); return t[a:b]
bad = collections.defaultdict(list)
for k in REF:
    i = byid[k]; L = lote(k); t = TXT[L]; p2, p3 = parte(t, 2), parte(t, 3)
    if i['url'] != ARQ[L] or i['cargo'] != CARGO[L] or i['certame'] != 'Projeto Câmara 2026' or i['ano'] != 2026 or i['numero'] != int(k[-2:]) or i['rotulo'] != 'AUTORAL' or i['textoBase'] != '' or 'comandoOriginal' in i or 'nota' in i:
        bad['metadados'].append(k)
    if ('\n' + i['enunciado'] + '\n') not in p2:
        bad['enunciado = linha literal da parte (d)'].append(k)
    if i['comando'] not in p2:
        bad['comando literal da parte (d)'].append(k)
    if L == 'L6A':
        if not ('L6A-R01 (P1-3). AUTORAL. ' + i['comando'] + '\n' + i['enunciado'] + '\n') in p2: bad['L6A: situação+comando e enunciado'].append(k)
    elif i['comando'] != 'Julgue o item.':
        bad['comando "Julgue o item."'].append(k)
    if i['enunciado'] in p3:
        bad['enunciado não aparece na parte (d-G)'].append(k)
    if i['justificativa'] not in p3 or 'Base:' in i['justificativa'] or 'Aderência:' in i['justificativa']:
        bad['justificativa literal da parte (d-G), sem "Base:"/"Aderência:"'].append(k)
    # gabarito, [TS] e folha por regex própria
    if L in ('L1', 'L2'):
        m = re.search(r'^%s\. ([CE])( \[TS\])?\. (.*)$' % re.escape(k), p3, re.M)
        ok = m and m.group(1) == i['gabarito'] and m.group(3) == i['justificativa']
        ts = bool(m and m.group(2))
        fm = re.search(r'^\| %s(?: \(novo\))? \| (P2-\d\.\d) \|' % re.escape(k), parte(t, 1), re.M)
    elif L == 'L3':
        m = re.search(r'^\*\*%s\*\* \((P2-\d\.\d)\) Gabarito: ([CE])\.( \[TS\])?\nJustificativa: (.*)$' % re.escape(k), p3, re.M)
        ok = m and m.group(2) == i['gabarito'] and m.group(4) == i['justificativa'] and m.group(1) == i['itemEdital']
        ts = bool(m and m.group(3)); fm = m
    else:
        m = re.search(r'^### L6A-R01 — Gabarito: ([CE])\nJustificativa \(duas linhas\): (.*)\n\[TS\]: (sim|não)', p3, re.M)
        ok = m and m.group(1) == i['gabarito'] and m.group(2) == i['justificativa']
        ts = bool(m and m.group(3) == 'sim'); fm = re.search(r'^\| L6A-R01 \| (P1-3) \|', parte(t, 1), re.M)
    if not ok:
        bad['gabarito e justificativa pela regex do (d-G)'].append(k)
    if not fm or fm.group(1) != i['itemEdital']:
        bad['itemEdital = folha do mapa'].append(k)
    i['_ts'] = ts
for n, v in [('metadados', None), ('enunciado = linha literal da parte (d)', None), ('comando literal da parte (d)', None), ('comando "Julgue o item."', None), ('L6A: situação+comando e enunciado', None),
             ('enunciado não aparece na parte (d-G)', None), ('justificativa literal da parte (d-G), sem "Base:"/"Aderência:"', None), ('gabarito e justificativa pela regex do (d-G)', None), ('itemEdital = folha do mapa', None)]:
    chk('(B) reforço: %s (48/48)' % n, not bad[n], str(bad[n]))
# Parte 2 sem marcas (D-REFORCO-1 (d))
chk('(B) arquivos finais: Parte 2 (d) sem gabarito, [TS], VOLÁTIL nem REVERIFICAR; FIM DO LOTE presente (4/4)',
    all(not re.search(r'\[TS\]|VOLÁTIL|REVERIFICAR|Gabarito', parte(t, 2)) and t.rstrip().endswith('FIM DO LOTE') for t in TXT.values()))
# decisões de aceite (constantes transcritas de DECISOES.md)
DEC = {'L1': (9, 9, 'R01 R03 R07 R09 R12 R13 R17', '', ''), 'L2': (8, 10, 'R02 R03 R04 R05 R09 R12 R14 R15 R16 R17', 'R07 R18', 'R02 R14 R15'),
       'L3': (6, 5, 'R02 R03 R06 R10 R11', '', 'R01 R02 R05'), 'L6A': (0, 1, 'R01', '', '')}
for L, (nc, ne, ts, vol, par) in DEC.items():
    xs = [byid[k] for k in REF if lote(k) == L]
    cc = collections.Counter(x['gabarito'] for x in xs)
    chk('(B) %s: C/E %d/%d; [TS] %s; volatil {%s}; parcial {%s} (decisão de aceite)' % (L, nc, ne, ts, vol, par),
        (cc['C'], cc['E']) == (nc, ne) and ' '.join(x['id'].split('-')[1] for x in xs if x['_ts']) == ts
        and ' '.join(x['id'].split('-')[1] for x in xs if x.get('volatil')) == vol and ' '.join(x['id'].split('-')[1] for x in xs if x['aderencia'] == 'parcial') == par,
        'C/E %d/%d' % (cc['C'], cc['E']))
cw = collections.Counter(byid[k]['gabarito'] for k in REF)
chk('(B) onda 1: 23 C / 25 E (47,9% de C, faixa 40–60%, regra 5 da D-REFORCO-2)', (cw['C'], cw['E']) == (23, 25) and 0.40 <= cw['C'] / 48 <= 0.60)
FOLHAS = ['P2-1.%d' % k for k in range(1, 9)] + ['P2-2.%d' % k for k in range(1, 9)] + ['P2-3.%d' % k for k in range(1, 5)] + ['P2-4.2', 'P2-4.3', 'P1-3']
cf = collections.Counter(i['itemEdital'] for i in items)
chk('(B) meta intermediária da D-REFORCO-1: 6 itens por folha nas 23 folhas com item novo da onda 1 (a onda tem 24; P1-4.3 fica com 4 até a T-102)', all(cf[f] == 6 for f in FOLHAS), str({f: cf[f] for f in FOLHAS if cf[f] != 6}))
vf = collections.Counter(byid[k]['itemEdital'] for k in REF if byid[k].get('volatil'))
chk('(B) VOLÁTEIS do reforço: 1 de 6 em P2-2.4 e 1 de 6 em P2-2.8 (teto 20% por folha, regra 4)', dict(vf) == {'P2-2.4': 1, 'P2-2.8': 1})
chk('(B) L1-R10/L1-R16: correção de registro do ponto não toca o item (enunciado, gabarito e justificativa = arquivo v2)', not any(x in v for v in bad.values() for x in ('L1-R10', 'L1-R16')))
# ------------------------------------------------------------------ (C) registro adendo 1 e camada do estudante
RA = read('saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo1_2026-10-18.md')
rows = {}
for l in RA.split('\n'):
    m = re.match(r'^\| (L(?:1|2|3|6A)-R\d{2}) \| ([CE]) \| (P[12]-[\d.]+) \| (TS)? \| (VOLÁTIL)? \| (direta|parcial) \| ', l)
    if m:
        rows[m.group(1)] = m.groups()[1:]
chk('(C) registro adendo 1: 48 linhas; gabarito, folha, [TS], VOLÁTIL e aderência = pacote (48/48)', sorted(rows) == sorted(REF)
    and all(rows[k] == (byid[k]['gabarito'], byid[k]['itemEdital'], 'TS' if byid[k]['_ts'] else None, 'VOLÁTIL' if byid[k].get('volatil') else None, byid[k]['aderencia']) for k in REF))
if os.path.exists(os.path.join(OUT, 'registro_adendo1.md')):
    chk('(C) registro adendo 1 promovido = out/registro_adendo1.md (registro_adendo_v19.py), byte a byte', RA == open(os.path.join(OUT, 'registro_adendo1.md'), encoding='utf-8').read())
v10 = 'L1-R10' in RA and 'excluir informações confidenciais e dados pessoais que nada acrescentam' in RA and 'o modelo turbo não é treinado para tradução' in RA
chk('(C) registro adendo 1: ponto VIGENTE de L1-R10 e L1-R16 (T89_reconciliacao, seção 4)', v10)
E = json.load(open(PE, encoding='utf-8'))
eb = {i['id']: i for i in E['itens']}
chk('(C) pacote_estudante: nome "(v1.9-E)", geradoEm 2026-10-18, 334 itens com ids e ordem iguais, lotes L1 L2 L3 L4 L5 L6A L6B',
    E['nome'] == 'Câmara 2026 — pacote do estudante (v1.9-E)' and E['geradoEm'] == '2026-10-18' and [i['id'] for i in E['itens']] == ids and [l['id'] for l in E['lotes']] == ['L1', 'L2', 'L3', 'L4', 'L5', 'L6A', 'L6B'])
chk('(C) pacote_estudante, 48 de reforço: url "", demais campos iguais salvo justificativa', all(eb[k]['url'] == '' and all(eb[k].get(f) == byid[k].get(f) for f in OBR + ['volatil'] if f not in ('url', 'justificativa')) and set(eb[k]) == set(byid[k]) - {'_ts'} for k in REF))
DEL = {'L2-R07': ['VOLÁTIL (baixo); REVERIFICAR. '], 'L2-R18': ['VOLÁTIL (ALTO: limite numérico de produto); REVERIFICAR. ', ' Inapto a simulado final até a reverificação de 4–8/1/2027; se a página mudar o número antes de janeiro, reescrever o item sem o limite.']}
def esperado(k):
    t = byid[k]['justificativa']
    for d in DEL.get(k, []):
        assert t.count(d) == 1, (k, d); t = t.replace(d, '')
    return t
chk('(C) pacote_estudante, 48 de reforço: justificativa = a do pacote.json; só L2-R07 e L2-R18 com as deleções literais da D1 (seção 3)', all(eb[k]['justificativa'] == esperado(k) for k in REF))
chk('(C) pacote_estudante, 48 de reforço: 0 "VOLÁTIL", "REVERIFICAR", "[TS]", "verificado em", "Base:" na justificativa', not any(re.search(r'VOLÁTIL|REVERIFICAR|\[TS\]|verificado em|Base:', eb[k]['justificativa']) for k in REF))
if PJ == os.path.join(OUT, 'pacote.json'):
    for i in items:
        i.pop('_ts', None)
    json.dump(dict(total=len(res), falhas=sum(not r['ok'] for r in res), res=res, contagens=cont), open(os.path.join(OUT, 'validate_v19.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('%d verificações, %d falhas' % (len(res), sum(not r['ok'] for r in res)))
sys.exit(1 if any(not r['ok'] for r in res) else 0)
