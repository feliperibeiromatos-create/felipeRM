# -*- coding: utf-8 -*-
"""Validação do pacote.json v1.4 (T-57; evolução do validador v1.3/T-56 e T-48). Lê out/pacote.json (ou o caminho dado) e as fontes; grava out/validate.json e imprime.
Caminhos: raiz do repositório e pasta out/ determinadas a partir de __file__; a v1.1 de referência vem do git (refs.py), não de arquivo solto."""
import json, re, csv, collections, sys, os, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import read, P, REPO, OUT
import refs
from edital_p import build_edital
from registry import REG
PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(OUT, 'pacote.json')
R = REPO + '/'
raw = open(PATH, encoding='utf-8').read()
new = json.loads(raw)
old = refs.v11()      # `git show e97ab1f:saida/pacote/pacote.json` (SHA-256 d3183826…)
stats = json.load(open(os.path.join(OUT, 'stats.json'), encoding='utf-8'))
res = []
def chk(n, ok, extra=''):
    res.append(dict(n=n, ok=bool(ok), extra=extra)); print('OK   ' if ok else 'FALHA', n, extra)
def nzs(s): return re.sub(r'\s+', ' ', s)

items = new['itens']; byid = {i['id']: i for i in items}
ids = [i['id'] for i in items]
# ---------------- forma ----------------
chk('JSON parseia sem erro; termina em newline; UTF-8', raw.endswith('\n') and not raw.endswith('\n\n'))
chk('formato: indent=1 e ensure_ascii=False (reserialização idêntica)', json.dumps(new, ensure_ascii=False, indent=1) + '\n' == raw)
chk('chaves de topo e valores', list(new.keys()) == ['versao', 'geradoEm', 'nome', 'edital', 'itens', 'simulados', 'lotes', 'discursivas'] and new['versao'] == 1 and new['nome'] == 'Câmara 2026 — pacote F4 (v1.4)' and new['geradoEm'] == '2026-10-13')
chk('0 id duplicado (%d ids)' % len(ids), len(ids) == len(set(ids)))
OBR = ['id', 'rotulo', 'certame', 'cargo', 'ano', 'numero', 'comando', 'textoBase', 'enunciado', 'gabarito', 'justificativa', 'itemEdital', 'aderencia', 'url']
chk('14 campos obrigatórios presentes em todos os itens', all(all(k in i for k in OBR) for i in items))
chk('tipos: ano/numero int; demais str', all(isinstance(i['ano'], int) and isinstance(i['numero'], int) and all(isinstance(i[k], str) for k in OBR if k not in ('ano', 'numero')) for i in items))
chk('campos extras só dentre comandoOriginal, volatil, nota', all(set(i) - set(OBR) <= {'comandoOriginal', 'volatil', 'nota'} for i in items))
bad = [i['id'] for i in items if not (i['id'] and i['enunciado'].strip() and i['gabarito'] in ('C', 'E'))]
chk('nenhum item sem id, enunciado e gabarito C/E', not bad, str(bad))
chk('0 "QA PENDENTE" no JSON', 'QA PENDENTE' not in raw)
eids = [e['id'] for e in build_edital()]
chk('edital: 47 entradas = v1.1 (idêntico)', new['edital'] == old['edital'] and len(new['edital']) == 47)
chk('todo itemEdital existe no edital', all(i['itemEdital'] in eids for i in items))
chk('aderencia só direta|parcial; rotulo permitido', all(i['aderencia'] in ('direta', 'parcial') for i in items) and all(i['rotulo'] in ('CEBRASPE_OFICIAL', 'CEBRASPE_ANALOGA', 'OUTRA_OFICIAL', 'AUTORAL') for i in items))
chk('volatil só true; nota só str não vazia; comandoOriginal só str não vazia', all(i.get('volatil', True) is True for i in items) and all(isinstance(i['nota'], str) and i['nota'] for i in items if 'nota' in i) and all(isinstance(i['comandoOriginal'], str) and i['comandoOriginal'] for i in items if 'comandoOriginal' in i))
for pat in ['ENTREGA DE LOTE', 'FIM DA PARTE', 'FIM DO LOTE', '=====', 'Fundador: gravar', 'Observação para a GCB-CQFP', 'Derep, antigo DETAQ']:
    chk('0 ocorrência de %r' % pat, pat not in raw)
# ---------------- banco ----------------
rows = list(csv.DictReader(open(R + 'banco/banco.csv', encoding='utf-8', newline=''), delimiter=';'))
ce = [r for r in rows if r['gabarito'] in ('C', 'E') and r['anulado'] == 'nao']
bq = {k: v for k, v in byid.items() if k.startswith('BQ-')}
chk('banco: 112 linhas no CSV; %d exportáveis (C/E, não anuladas); exportados = exportáveis' % len(ce), len(rows) == 112 and len(ce) == 106 and set(bq) == {r['id'] for r in ce})
chk('banco: 6 anuladas fora (BQ-0029, 0030, 0031, 0060, 0062, 0063)', sorted(r['id'] for r in rows if r['id'] not in bq) == ['BQ-0029', 'BQ-0030', 'BQ-0031', 'BQ-0060', 'BQ-0062', 'BQ-0063'])
chk('banco: id, gabarito, enunciado, itemEdital, certame, cargo, url, ano, numero = CSV (106/106)', all(bq[r['id']]['gabarito'] == r['gabarito'] and bq[r['id']]['enunciado'] == r['texto_integral'] and bq[r['id']]['itemEdital'] == r['item_edital_camara'] and bq[r['id']]['certame'] == r['certame'] and bq[r['id']]['cargo'] == r['cargo'] and bq[r['id']]['url'] == r['url_caderno'] and bq[r['id']]['ano'] == int(r['ano_aplicacao']) and bq[r['id']]['numero'] == int(r['numero_item']) for r in ce))
cb = collections.Counter(v['gabarito'] for v in bq.values())
chk('banco: 60 C / 46 E', cb['C'] == 60 and cb['E'] == 46, str(dict(cb)))
chk('banco: comando = texto_comando; textoBase = texto_base ou "" (106/106)', all(bq[r['id']]['comando'] == r['texto_comando'] and bq[r['id']]['textoBase'] == r['texto_base'] for r in ce))
chk('banco: aderencia = coluna aderencia do CSV (106/106), sem recálculo', all(bq[r['id']]['aderencia'] == r['aderencia'] for r in ce))
ad = collections.Counter(v['aderencia'] for v in bq.values())
chk('banco: 67 direta / 39 parcial', ad['direta'] == 67 and ad['parcial'] == 39, str(dict(ad)))
o60 = {i['id']: i for i in old['itens'] if i['id'].startswith('BQ-')}
chk('banco: os 60 da v1.1 com o MESMO comando (60/60)', all(bq[k]['comando'] == o60[k]['comando'] for k in o60) and len(o60) == 60)
chk('banco: os 60 da v1.1 com aderência igual (37 direta/23 parcial)', all(bq[k]['aderencia'] == o60[k]['aderencia'] for k in o60) and collections.Counter(bq[k]['aderencia'] for k in o60) == collections.Counter({'direta': 37, 'parcial': 23}))
chk('banco: textoBase não vazio só em BQ-0049, 0050, 0051; os 60 da v1.1: textoBase = texto da v1.1 ou ""', sorted(k for k, v in bq.items() if v['textoBase']) == ['BQ-0049', 'BQ-0050', 'BQ-0051'] and all(bq[k]['textoBase'] == ('' if o60[k]['textoBase'] == 'nenhum' else o60[k]['textoBase']) for k in o60))
chk('banco: volatil = 8 (BQ-0015, 0017, 0035, 0064, 0075, 0076, 0086, 0089)', sorted(k for k, v in bq.items() if v.get('volatil')) == ['BQ-0015', 'BQ-0017', 'BQ-0035', 'BQ-0064', 'BQ-0075', 'BQ-0076', 'BQ-0086', 'BQ-0089'])
contrato = open(R + 'regras/pacote_contrato.md', encoding='utf-8').read()
notas_contrato = {m.group(1): m.group(2) for m in re.finditer(r'^   - (BQ-\d{4}) \([^)]*\): `(nota de vigência: .*?)`$', contrato, re.M)}
chk('nota: só BQ-0003 e BQ-0040; valor = texto do contrato (regra 4 da v1.1.1) e = trecho final de observacoes', sorted(k for k, v in byid.items() if 'nota' in v) == ['BQ-0003', 'BQ-0040'] and all(byid[k]['nota'] == v for k, v in notas_contrato.items()) and len(notas_contrato) == 2 and all([r for r in rows if r['id'] == k][0]['observacoes'].endswith(byid[k]['nota']) for k in ('BQ-0003', 'BQ-0040')))
chk('banco: BQ-0072, 0077, 0084, 0109, 0110, 0111 presentes; BQ-0110 sem nota', all(k in bq for k in ('BQ-0072', 'BQ-0077', 'BQ-0084', 'BQ-0109', 'BQ-0110', 'BQ-0111')) and 'nota' not in bq['BQ-0110'])
chk('banco: 0 item normalizado; BQ-0070, 0071, 0112 com comando inteiro e sem comandoOriginal', not any('comandoOriginal' in v for v in bq.values()) and all(k in bq and 'comandoOriginal' not in bq[k] for k in ('BQ-0070', 'BQ-0071', 'BQ-0112')) and 'julgue' not in bq['BQ-0070']['comando'].lower()[:0])
# ---------------- AUTORAL ----------------
aut = {k: v for k, v in byid.items() if v['rotulo'] == 'AUTORAL'}
regf = {}
for lot, d in REG.items():
    regf.update(d)
chk('AUTORAL: 180 ids = registro v3 (180/180)', len(aut) == 180 and set(aut) == set(regf))
chk('AUTORAL: gabarito = registro v3 (180/180)', all(aut[k]['gabarito'] == regf[k]['gab'] for k in regf))
bad = []
for k, v in regf.items():
    if k.split('-')[0] in ('L1', 'L1C', 'L2', 'L3'):
        if aut[k]['itemEdital'] != 'P2-' + v['sub']: bad.append(k)
    elif not (aut[k]['itemEdital'] == 'P1-' + v['sub'] or aut[k]['itemEdital'] == 'P1-' + v['sub'].split('.')[0]): bad.append(k)
chk('AUTORAL: subitem compatível com o registro (180/180)', not bad, str(bad))
volreg = {k for k, v in regf.items() if 'VOLÁTIL' in v['marca'] or 'REVERIF' in v['marca']}
chk('AUTORAL: volatil = VOLÁTIL + REVERIFICAR do registro (15)', {k for k, v in aut.items() if v.get('volatil')} == volreg and len(volreg) == 15, str(sorted(volreg)))
ca = collections.Counter(v['gabarito'] for v in aut.values())
chk('AUTORAL: 89 C / 91 E', ca['C'] == 89 and ca['E'] == 91, str(dict(ca)))
chk('AUTORAL: [TS] no registro = 91; [TS] lido dos d-G dos arquivos canônicos = registro (180/180)', sum(v['ts'] for v in regf.values()) == 91 and sum(len(v) for v in stats['ts'].values()) == 91 and all((k in sum(stats['ts'].values(), [])) == regf[k]['ts'] for k in regf))
chk('AUTORAL: justificativa não vazia; banco: justificativa vazia', all((i['justificativa'].strip() != '') == (i['rotulo'] == 'AUTORAL') for i in items))
chk('AUTORAL: textoBase "" em 180/180 (F2); 0 "nenhum" em textoBase (286)', all(v['textoBase'] == '' for v in aut.values()) and not any(i['textoBase'] == 'nenhum' for i in items))
chk('F2: textoBase vazio em %d de 286 itens (283 = 286 − 3 de BQ-0049..51)' % sum(1 for i in items if i['textoBase'] == ''), sum(1 for i in items if i['textoBase'] == '') == 283)
vol = [k for k, v in byid.items() if v.get('volatil')]
chk('volatil total = 23 (banco 8 + AUTORAL 15), L3-Q21 marcado', len(vol) == 23 and byid['L3-Q21'].get('volatil') is True)
# comandoOriginal / normalização (h)
NORM_RX = re.compile(r'(?i)(julgue os itens) (?:de )?(?:[0-9A-Z]+-)?\d+ a (?:[0-9A-Z]+-)?\d+\.')
co = {k: v for k, v in byid.items() if 'comandoOriginal' in v}
lotes_of = lambda k: stats['item_lote'][k]
cc = collections.Counter(lotes_of(k) for k in co)
chk('normalização: 90 itens com comandoOriginal = L4 20, A5/L5 20, 4C/L4C 10, 5C/L5C 10, L6A 15, L6B 15', len(co) == 90 and dict(cc) == {'L4': 20, 'L4C': 10, 'L5': 20, 'L5C': 10, 'L6A': 15, 'L6B': 15}, str(dict(cc)))
chk('normalização: comando = comandoOriginal com só o trecho da numeração trocado por "julgue os itens a seguir."', all(NORM_RX.sub(lambda m: m.group(1) + ' a seguir.', v['comandoOriginal']) == v['comando'] and NORM_RX.search(v['comandoOriginal']) for v in co.values()))
def so_numeracao(a, b):
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    return all(a[i1:i2].lower().startswith(('de ', '')) for t, i1, i2, j1, j2 in sm.get_opcodes() if t != 'equal')
dif_ok = True
for v in co.values():
    a, b = v['comandoOriginal'], v['comando']
    pre = a[:NORM_RX.search(a).start()]
    dif_ok &= b.startswith(pre) and a.endswith('.') and b.endswith('julgue os itens a seguir.') and b[:len(pre)] == a[:len(pre)]
chk('normalização: parte da frase anterior a "julgue os itens" idêntica (resto literal)', dif_ok)
chk('normalização: nenhum comando restante com faixa de itens; L1–L3 (90) sem comandoOriginal e com comando literal', not any(NORM_RX.search(v['comando']) for v in items) and all('comandoOriginal' not in v for k, v in aut.items() if lotes_of(k) in ('L1', 'L1C', 'L2', 'L3')))
v11 = {i['id']: i for i in old['itens']}
chk('normalização: base v1.1 também 90 (mesma contagem por lote)', len([k for k, v in v11.items() if v['rotulo'] == 'AUTORAL' and NORM_RX.search(v['comando'])]) == 90 and all(co[k]['comandoOriginal'] == v11[k]['comando'] for k in co))
# AUTORAL: diferenças campo a campo contra a v1.1
camp = collections.Counter()
for k, v in aut.items():
    for f in sorted(set(v) | set(v11[k])):      # T-56: ordem determinística (antes: iteração de conjunto, ordem variável entre execuções)
        if v.get(f) != v11[k].get(f): camp[f] += 1
chk('AUTORAL v1.1 → v1.2: campos alterados só textoBase(180), comando/comandoOriginal(90), justificativa(21), enunciado(1: L1-Q04)', dict(camp) == {'textoBase': 180, 'comando': 90, 'comandoOriginal': 90, 'justificativa': 21, 'enunciado': 1}, str(dict(sorted(camp.items()))))
chk('F1: L1-Q04 contém "áudio–texto"; 0 "áudio– texto" no JSON', 'áudio–texto' in byid['L1-Q04']['enunciado'] and 'áudio– texto' not in raw)
chk('F1: nenhuma outra letra+"– "+letra no JSON (efeito de quebra de linha)', not re.search(r'[A-Za-zÀ-ú]– [A-Za-zÀ-ú]', raw))
# F4
f4 = stats['f4']
chk('F4 (R1): %d justificativas alteradas (21 = 18 da R0 + 6B-06, 6B-15, L2-Q21)' % len(f4), len(f4) == 21 and sorted(f['id'] for f in f4) == sorted(['L2-Q21', 'L2-Q23', 'L4-08', 'L4-09', 'L4-13', 'L4-15', 'L4-17', 'L4-18', 'L4-19', 'L4-20', '4C-06', '4C-08', '4C-09', 'A5-14', 'A5-15', 'A5-16', 'A5-17', '5C-03', '5C-06', '6B-06', '6B-15']))
def so_delecao_ou_caixa(f):
    a, d = f['antes'], f['depois']
    sm = difflib.SequenceMatcher(None, a.lower(), d.lower(), autojunk=False)
    ops = sm.get_opcodes()
    if not all(t in ('equal', 'delete') for t, *_ in ops): return False
    dif = 0
    for t, i1, i2, j1, j2 in ops:
        if t == 'equal':
            for x, y in zip(a[i1:i2], d[j1:j2]):
                if x != y:
                    if not (x.islower() and y == x.upper()): return False
                    dif += 1
    return dif == len(f.get('caixa', []))
chk('F4 (R1): cada alteração é SÓ deleção, salvo as 2 trocas de caixa fechadas da C-05 (4C-08, 5C-06: minúscula → maiúscula na inicial)', all(so_delecao_ou_caixa(f) for f in f4) and sum(len(f['caixa']) for f in f4) == 2)
chk('F4: justificativas finais = depois', all(byid[f['id']]['justificativa'] == f['depois'] for f in f4))
residual = re.compile(r'CQFP|CQE|\bCPP\b|\bGCE\b|\bGCB\b|\bGBQ\b|\bEXEC\b|\bT-\d+|\(v\d|\bO\d{1,2}\b|Lição|R-[45]C\d|\bRisco (BAIXO|MÉDIO|ALTO)|(?<!NORMATIVO — )\bQA\b|\bO-\d+\b|Retificação|[Gg]abarito [CE] mantido')
chk('F4 (R1/C-09): 0 marca de processo (CQFP/CQE/CPP/GCE/GCB/GBQ/EXEC/T-xx/(vN/Oxx/Lição/R-4C1/Risco + QA, O-n, Retificação, "Gabarito C|E mantido") nas 180 justificativas AUTORAL', not [k for k, v in aut.items() if residual.search(v['justificativa'])] and len(aut) == 180, str([k for k, v in aut.items() if residual.search(v['justificativa'])]))
# F5
n_ok = len(re.findall(r'Derep \(antigo DETAQ\)', raw))
chk('F5: 0 "Derep, antigo DETAQ"; "Derep (antigo DETAQ)" no L1 (curso, E10)', 'Derep, antigo DETAQ' not in raw and 'Derep (antigo DETAQ); Ato da Mesa nº 251/2026' in [l for l in new['lotes'] if l['id'] == 'L1'][0]['curso'].replace('\n', ' '), 'ocorrências totais da forma correta: %d' % n_ok)
# ---------------- registro AUTORAL x enunciado/justificativa vs lotes (texto do item) ----------------
# ---------------- lotes ----------------
L = {l['id']: l for l in new['lotes']}
DECL = {'L1': 20, 'L1C': 10, 'L2': 30, 'L3': 30, 'L4': 20, 'L4C': 10, 'L5': 20, 'L5C': 10, 'L6A': 15, 'L6B': 15}
chk('contagem por lote = declarada %s' % DECL, dict(collections.Counter(stats['item_lote'].values())) == DECL)
chk('lotes: itensEdital, pares e pegadinhas são listas JSON em 10/10 lotes; itensEdital ⊂ edital', all(isinstance(l['itensEdital'], list) and isinstance(l['pares'], list) and isinstance(l['pegadinhas'], list) for l in new['lotes']) and all(x in eids for l in new['lotes'] for x in l['itensEdital']) and len(new['lotes']) == 10)
LEG_LOTES = ['L4', 'L4C', 'L5', 'L5C', 'L6A', 'L6B']
LEG = {
 'L4': 'Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC)',
 'L4C': 'Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC)',
 'L5': 'Mecanismos: TC troca de conceito; GI generalização indevida; AT atribuição errada de técnica; IC inversão de causa e efeito',
 'L5C': 'Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC)',
 'L6A': 'Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada (AT), inversão de causa e efeito (IC)',
 'L6B': 'Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada (AT), inversão de causa e efeito (IC)',
}
BASE_L = ['id', 'nome', 'prova', 'itensEdital', 'resumo', 'curso', 'pares', 'pegadinhas']
chk('lotes: campos id, nome, prova, itensEdital, resumo, curso, pares, pegadinhas (+ legendaMecanismo, opcional, só em L4, L4C, L5, L5C, L6A, L6B)', all(list(l.keys()) == BASE_L + (['legendaMecanismo'] if l['id'] in LEG_LOTES else []) for l in new['lotes']))
chk('v1.3 legendaMecanismo: 6 lotes, string não vazia, literal da tabela 2.3 do QA da T-53 (L4 = L4C = L5C; L5 "Mecanismos: …"; L6A = L6B "atribuição errada (AT)"); L1, L1C, L2, L3 sem o campo', {l['id']: l['legendaMecanismo'] for l in new['lotes'] if 'legendaMecanismo' in l} == LEG and all('legendaMecanismo' not in l for l in new['lotes'] if l['id'] in ('L1', 'L1C', 'L2', 'L3')))
chk('v1.3 legendaMecanismo: sem ponto final, sem quebra de linha, e ocorre literal (1 vez, em linha "Legenda:") no arquivo canônico do lote', all(not v.endswith('.') and '\n' not in v for v in LEG.values()) and all(sum(1 for ln in read({'L4': 'saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md', 'L4C': 'saida/gcb/GCB_Lote4C_v1_GCB-CPP.md', 'L5': 'saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md', 'L5C': 'saida/gcb/GCB_Lote5C_v1_GCB-CPP.md', 'L6A': 'saida/gcb/GCB_Lote6a_v2_producao_auto.md', 'L6B': 'saida/gcb/GCB_Lote6b_v2_producao_auto.md'}[k]).split('\n') if ln.startswith('Legenda:') and v in ln) == 1 for k, v in LEG.items()))
chk('lotes: itensEdital iguais aos da v1.1 (10/10)', all(l['itensEdital'] == o['itensEdital'] for l, o in zip(new['lotes'], old['lotes'])))
ID_LOTES = {'L4': 20, 'L5': 15, 'L6A': 19, 'L6B': 18}
def _canon_ids(lid):
    # rótulos "C<n>." da seção (c) do arquivo canônico do lote (independente do gerador)
    ln = read({'L4': 'saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md', 'L5': 'saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md', 'L6A': 'saida/gcb/GCB_Lote6a_v2_producao_auto.md', 'L6B': 'saida/gcb/GCB_Lote6b_v2_producao_auto.md'}[lid]).split('\n')
    c0 = next(i for i, l in enumerate(ln) if l.startswith('(c) PARES'))
    e2 = next(i for i in range(c0, len(ln)) if ln[i].startswith('FIM DA PARTE 2/3'))
    return [m.group(1) for m in (re.match(r'^(C\d+)\.\s', l) for l in ln[c0 + 1:e2]) if m]
chk('v1.4 `id` de par (contrato v1.2.2 ponto 1): chaves [id, a, b, como] só em L4, L5, L6A e L6B (72 pares); L1, L1C, L2, L3 sem `id` (67 pares: [a, b, como])',
    all(all(list(p.keys()) == ['id', 'a', 'b', 'como'] for p in l['pares']) for l in new['lotes'] if l['id'] in ID_LOTES) and all(all(list(p.keys()) == ['a', 'b', 'como'] for p in l['pares']) for l in new['lotes'] if l['id'] not in ID_LOTES)
    and sum(len(l['pares']) for l in new['lotes'] if l['id'] in ID_LOTES) == 72 and sum(len(l['pares']) for l in new['lotes'] if l['id'] not in ID_LOTES) == 67)
chk('v1.4 `id` de par: string não vazia que casa ^C\\d+$, C1…Cn em sequência, igual (e na mesma ordem) aos rótulos "C<n>." da seção (c) do arquivo canônico: L4 20, L5 15, L6A 19, L6B 18',
    all([p['id'] for p in L[lid]['pares']] == ['C%d' % k for k in range(1, n + 1)] == _canon_ids(lid) and all(re.match(r'^C\d+$', p['id']) for p in L[lid]['pares']) for lid, n in ID_LOTES.items()))
_ref = {('L5', 'C1'): ('Histograma', 'gráfico de barras'), ('L5', 'C14'): ('Storytelling', 'dashboard'), ('L4', 'C19'): ('Injeção de prompt', 'jailbreak (conceitos gerais)')}
chk('v1.4 remissões a par por id: L5 C1 = Histograma × gráfico de barras; L5 C14 = Storytelling × dashboard; L4 C19 = Injeção de prompt × jailbreak (conceitos gerais)',
    all(any(p['id'] == k[1] and (p['a'], p['b']) == v for p in L[k[0]]['pares']) for k, v in _ref.items()))
v11p = {l['id']: l['pares'] for l in old['lotes']}
_dp = {l['id']: [k for k, (p, q) in enumerate(zip(l['pares'], v11p[l['id']]), 1) if {a_: b_ for a_, b_ in p.items() if a_ != 'id'} != q] for l in new['lotes']}
chk('v1.4 `a`, `b` e `como` de todos os pares iguais aos da v1.1, fora o `id`, salvo a errata oficial já aplicada na v1.1 (L3 par 20 = E4; o par 15 do L2, E1c, já estava aplicado na v1.1)', {k: v for k, v in _dp.items() if v} == {'L3': [20]}, str({k: v for k, v in _dp.items() if v}))
chk('pares por lote iguais à v1.1 (L1 17, L2 22, L3 28, L4 20, L5 15, L6A 19, L6B 18)', all(len(l['pares']) == len(o['pares']) for l, o in zip(new['lotes'], old['lotes'])) and [len(l['pares']) for l in new['lotes']] == [17, 0, 22, 28, 20, 0, 15, 0, 19, 18])
chk('pegadinhas.itemEdital existem no edital', all(p['itemEdital'] in eids for l in new['lotes'] for p in l['pegadinhas']))
# pegadinhas: F3
chk('F3: toda pegadinha tem itemEdital, rotulo (não vazio) e texto (não vazio), nessa ordem', all(list(p.keys()) == ['itemEdital', 'rotulo', 'texto'] and p['rotulo'].strip() and p['texto'].strip() for l in new['lotes'] for p in l['pegadinhas']))
fontes = {'L1': 'saida/gce/GCE_Lote1_v2_CPP.md', 'L1C': 'saida/gce/GCE_Lote1C_v2_CPP.md', 'L2': 'saida/gce/GCE_Lote2_v2_CPP.md', 'L3': 'saida/gce/GCE_Lote3_v2_CPP.md',
          'L4': 'saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md', 'L5': 'saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md', 'L6A': 'saida/gcb/GCB_Lote6a_v2_producao_auto.md', 'L6B': 'saida/gcb/GCB_Lote6b_v2_producao_auto.md', 'L4C': 'saida/gcb/GCB_Lote4C_v1_GCB-CPP.md', 'L5C': 'saida/gcb/GCB_Lote5C_v1_GCB-CPP.md'}
def unh(s):   # texto do arquivo: junta quebras (com/sem hífen de quebra) e normaliza espaços
    return nzs(re.sub(r'-\n\s*', '-', s))
edmd = nzs(read('edital/TI_itens_1_4_P1.md') + ' ' + read('edital/TI_itens_5_8_P1.md') + ' ' + read('edital/modulo_RF_IA_P2.md'))
badrot = []
for lid, l in L.items():
    if not l['pegadinhas']: continue
    src = unh(read(fontes[lid])); src2 = nzs(read(fontes[lid]))
    for p in l['pegadinhas']:
        r = nzs(p['rotulo'])
        if not (r in src or r in src2 or r in edmd or r.lower() in src.lower() or r in edmd):
            badrot.append((lid, p['itemEdital'], p['rotulo']))
chk('F3: todo rotulo é trecho literal do arquivo canônico do lote ou do edital (sem marcas internas)', not badrot, str(badrot[:5]))
chk('F3: nenhum rotulo com marca interna ([V, [TS], F1.., U1.., verificado em, ITEM)', not [p for l in new['lotes'] for p in l['pegadinhas'] if re.search(r'\[V |\[TS\]|\bF\d+\b|\bU\d\b|verificado em|^ITEM|^\d+(\.\d+)*\s', p['rotulo'])])
chk('F3 (R1): pegadinhas L1 19, L5 48, total 262 (R0: 20, 52, 267); 5 reuniões registradas (C-06 a C-08)', len(L['L1']['pegadinhas']) == 19 and len(L['L5']['pegadinhas']) == 48 and sum(len(l['pegadinhas']) for l in new['lotes']) == 262 and len(stats['merge']) == 5, str({l['id']: len(l['pegadinhas']) for l in new['lotes']}))
# conferência: junção dos fragmentos reproduz cada entrada da v1.1 (salvo o ponto final)
import peg as PG
recon_bad = []
cnt_v11, cnt_v12 = {}, {}
for lid in L:
    ol = [x for x in old['lotes'] if x['id'] == lid][0]
    cnt_v11[lid] = len(ol['pegadinhas']); cnt_v12[lid] = len(L[lid]['pegadinhas'])
    nps = list(L[lid]['pegadinhas'])
    pos = 0
    for og in ol['pegadinhas']:
        t = og['texto'].strip()
        # consome fragmentos consecutivos com o mesmo itemEdital até reconstruir t
        acc = []
        while pos < len(nps) and nps[pos]['itemEdital'] == og['itemEdital']:
            acc.append(nps[pos]['texto']); pos += 1
            for modo in ('enumeradores', 'ponto-e-virgula', 'unica'):
                if modo == 'enumeradores':
                    j = ' '.join('(%d) %s' % (n + 1, f) for n, f in enumerate(acc))
                elif modo == 'ponto-e-virgula':
                    j = '; '.join(acc)
                else:
                    j = acc[0] if len(acc) == 1 else None
                if j is not None and (j.rstrip('.') == t.rstrip('.') or j == t):
                    break
            else:
                continue
            break
        else:
            recon_bad.append((lid, og['itemEdital'], t[:60]))
            continue
        # entradas v1.1 que não casaram: já registradas; segue
    if pos != len(nps): recon_bad.append((lid, 'sobra', len(nps) - pos))
chk('F3: a junção dos fragmentos (separador original) reproduz cada entrada da v1.1, salvo o ponto final', not recon_bad, str(recon_bad[:5]))
# ---------------- erratas ----------------
errs = stats['errata']
chk('erratas: %d aplicações registradas; 0 FALHA; estados %s' % (len(errs), dict(collections.Counter(e['estado'] for e in errs))), all(e['estado'] in ('APLICADA', 'JÁ PRESENTE') for e in errs))
fulltxt = nzs('\n'.join(json.loads(json.dumps(v, ensure_ascii=False)) if False else '' for v in []))
def collect(o, acc):
    if isinstance(o, str): acc.append(o)
    elif isinstance(o, dict):
        for v in o.values(): collect(v, acc)
    elif isinstance(o, list):
        for v in o: collect(v, acc)
acc = []; collect(new, acc)
allt = nzs('\n'.join(acc))
from p2 import ERRATA, NAO_EXPORTADAS
okY = []; badX = []
for lote, lst in ERRATA.items():
    for eid, x, y, src in lst:
        if eid == 'E10': y = y.replace('Derep, antigo DETAQ', 'Derep (antigo DETAQ)')      # F5 sobre a Y da E10
        if nzs(y) not in allt and not (src == 'cons-cap'):
            okY.append((lote, eid, 'Y ausente'))
        if src == 'cons-cap' and nzs(y) not in allt:
            okY.append((lote, eid, 'Y(cap) ausente'))
        # X (sem Y) não pode permanecer: remove ocorrências de Y e procura X
        t2 = allt.replace(nzs(y), '')
        if nzs(x) in t2: badX.append((lote, eid))
chk('erratas: Y de cada errata presente no JSON (27 aplicações com Y)', not okY, str(okY))
chk('erratas: X de cada errata ausente do JSON (fora das ocorrências de Y)', not badX, str(badX))
nao = []
for e in NAO_EXPORTADAS:
    x = e.get('x'); y = e.get('y')
    if x:
        src = nzs(read(e['arquivo'])) if e.get('arquivo') else None
        em_arquivo = (nzs(x) in nzs(re.sub(r'-\n\s*', '-', read(e['arquivo'])))) if e.get('arquivo') else True
        no_json = nzs(x) in allt or (y and nzs(y) in allt)
        nao.append(dict(lote=e['lote'], id=e['id'], em_arquivo=em_arquivo, no_json=bool(no_json)))
chk('erratas fora do exportado: alvo existe no arquivo e X/Y NÃO vai ao JSON', all(n['em_arquivo'] and not n['no_json'] for n in nao), str(nao))
# E12, E7, E4, Adendo 2
chk('L1 E12: resumo do L1 contém a Y e não contém "não mede pontuação nem locutor"', 'no cálculo usual, sobre texto normalizado, não mede pontuação nem capitalização; locutor fica fora do WER em qualquer convenção' in nzs(L['L1']['resumo']) and 'não mede pontuação nem locutor' not in nzs(L['L1']['resumo']))
chk('L2 E7: resumo do L2 (2.4) com Y', 'Forma de identificar o orador: observada nas notas oficiais de 2026 (N1; E3). Convenção da Câmara para marcação de pausas e eventos não falados e para grafia: NÃO VERIFICADA (N2).' in nzs(L['L2']['resumo']))
p20 = [p for p in L['L3']['pares'] if 'suprimida pela MP' in (p['a'] + p['b'] + p['como'])]
chk('L3 E4: par 20 com "suprimida pela MP nº 869/2018, convertida na Lei 13.853/2019" e 0 "suprimida pela Lei 13.853/2019)"', len(p20) == 1 and 'suprimida pela Lei 13.853/2019)' not in nzs(json.dumps(L['L3']['pares'], ensure_ascii=False)))
c3 = L['L3']['curso']
chk('L3 Adendo 2: "Contexto institucional — Ato da Mesa nº 225" 1 vez no curso (4.1), 3.1 sem duplicata; bloco T-08/T-44 do 3.1 intacto',
    c3.count('Contexto institucional — Ato da Mesa nº 225') == 1 and c3.count('CONTEXTO NORMATIVO INTERNO (SEM ITEM)') == 1 and 'ERRATA T-08' not in c3 and 'registro da GCB-CQFP' not in c3
    and c3.index('Contexto institucional — Ato da Mesa nº 225') > c3.index('4.1 LGPD E PROTEÇÃO') and c3.index('Contexto institucional — Ato da Mesa nº 225') < c3.index('4.2 DIREITOS AUTORAIS'))
chk('L3 Adendo 2: texto inserido = texto literal do Adendo 2 da consolidação', stats['adendo2'] in c3)
_l3c = read('saida/gce/GCE_Lote3_v2_CPP.md')
chk('L3 T-58 (D1-T54-b da GCE, errata de forma): curso do L3 com "jurisprudência firmada que se possa afirmar):" (1×) e 0 "que eu possa afirmar"; o canônico atual tem a errata no curso (1×) e o registro "T-54" na Tabela de Correções do cabeçalho (o "que eu possa afirmar" que resta no canônico é o da linha de limites N4, não exportada)',
    nzs(c3).count('jurisprudência firmada que se possa afirmar):') == 1 and 'que eu possa afirmar' not in c3 and nzs(_l3c).count('jurisprudência firmada que se possa afirmar):') == 1
    and nzs(_l3c).count('"que eu possa afirmar" → "que se possa afirmar"') == 1 and nzs(_l3c).count('que eu possa afirmar') == 2)
chk('L5 Tukey (T-47): curso do L5 8.2 contém "O fator 1,5·AIQ é a convenção usual (Tukey); outras convenções existem e a prova costuma cobrar esta."', 'O fator 1,5·AIQ é a convenção usual (Tukey); outras convenções existem e a prova costuma cobrar esta.' in nzs(L['L5']['curso']))
# DETAQ
bare = []
for lid, l in L.items():
    for f in ('curso', 'resumo'):
        for m in re.finditer(r'DETAQ', l[f]):
            ctx = l[f][max(0, m.start() - 22):m.end() + 3]
            if 'Derep (antigo DETAQ)' not in l[f][max(0, m.start() - 14):m.end() + 1]:
                bare.append((lid, f, ctx.replace('\n', ' ')))
res.append(dict(n='INFO DETAQ fora da forma "Derep (antigo DETAQ)" em curso/resumo', ok=True, extra=str(bare)))
print('INFO DETAQ residual:', bare)
# ---------------- discursivas ----------------
_ant_d5 = old['discursivas'][4]['padrao']
_i5 = _ant_d5.index('R2. Alínea c'); _i3 = _ant_d5.index('R3. Voz como dado sensível')
chk('discursivas: 5 (D1–D5); D1 a D4 idênticas às da v1.1; D5 igual à da v1.1 exceto o anexo de notas: sem a R2 (trecho literal removido) e com o rótulo "Notas de correção (GCE, R3–R4)" (D1-T54-a da GCE); comando, aspectos e quesitos da D5 iguais',
    len(new['discursivas']) == 5 and new['discursivas'][:4] == old['discursivas'][:4] and {k: v for k, v in new['discursivas'][4].items() if k != 'padrao'} == {k: v for k, v in old['discursivas'][4].items() if k != 'padrao'}
    and new['discursivas'][4]['padrao'] == _ant_d5[:_i5].replace('Notas de correção (GCE, R2–R4)\n', 'Notas de correção (GCE, R3–R4)\n') + _ant_d5[_i3:])
chk('discursivas: sem observação "inferido pela EXEC" (0 ocorrência)', not re.search(r'itensEdital[^"]{0,40}inferid|inferid[^"]{0,40}EXEC|pela EXEC|\bEXEC\b', raw))
chk('discursivas: "14,30" (E11) não aparece em comando/padrão (E11 sem efeito no exportado)', not any('14,30' in d['comando'] or '14,30' in d['padrao'] for d in new['discursivas']))
for d in new['discursivas']:
    s = sum(a['valor'] or 0 for a in d['aspectos']); print('INFO', d['id'], d['tipo'], 'aspectos', len(d['aspectos']), 'soma', round(s, 2))
_src3 = read('saida/gce/GCE_Lote3_padroes_GCE.md').split('\n')
for d in new['discursivas']:
    if d['id'] == 'D4':
        a = d['padrao'].split('Notas de correção (GCE, R2–R4)\n', 1)[1]
        chk('D4: anexo R2–R4 é cópia literal das linhas 14–23 do arquivo de padrões', a == '\n'.join(_src3[13:23]) and d['padrao'].count('R2. Alínea c') == 1)
    if d['id'] == 'D5':
        a = d['padrao'].split('Notas de correção (GCE, R3–R4)\n', 1)[1]
        chk('D5 (v1.4, D1-T54-a da GCE): anexo R3–R4 é cópia literal das linhas 21–23 do arquivo de padrões; 0 "R2." e 0 "Alínea c da discursiva" na D5; rótulo "Notas de correção (GCE, R3–R4)"',
            a == '\n'.join(_src3[20:23]) and 'R2.' not in d['padrao'] and 'Alínea c da discursiva' not in d['padrao'] and 'Notas de correção (GCE, R2–R4)' not in d['padrao'] and a.startswith('R3. ') and a.rstrip().endswith('o art. 7º, II ou III.'))
# ---------------- simulados ----------------
S = {s['id']: s for s in new['simulados']}
chk('simulados: ids [SIM-0, SIM-1, SIM-2, SIM-0-P2]; tipos; versões', [s['id'] for s in new['simulados']] == ['SIM-0', 'SIM-1', 'SIM-2', 'SIM-0-P2'] and [s['tipo'] for s in new['simulados']] == ['diagnóstico', 'final', 'final', 'diagnóstico'] and [s['versao'] for s in new['simulados']] == ['v0.2', 'v1', 'v1', 'v1'])
chk('simulados: n = tamanho de itens = 60, 40, 40, 25; chaves id,nome,tipo,versao,n,itens (+ avisos, opcional, só no SIM-0)', [s['n'] for s in new['simulados']] == [60, 40, 40, 25] and all(s['n'] == len(s['itens']) for s in new['simulados']) and all(list(s.keys()) == ['id', 'nome', 'tipo', 'versao', 'n', 'itens'] + (['avisos'] if s['id'] == 'SIM-0' else []) for s in new['simulados']))
_s0 = read('saida/simulados/simulado_0_v0.2.md').split('\n')
_i0 = _s0.index('## Avisos de montagem'); _av = {}; _cur = None
for _l in _s0[_i0 + 1:]:
    if _l.startswith('## '): break
    _m = re.match(r'^(\d+)\. (.*)$', _l)
    if _m: _cur = int(_m.group(1)); _av[_cur] = [_m.group(2)]
    elif _cur is not None and _l.startswith(' '): _av[_cur].append(_l)
    elif not _l.strip(): _cur = None
_av = {k: '\n'.join(v) for k, v in _av.items()}
_s0av = [s for s in new['simulados'] if s['id'] == 'SIM-0'][0].get('avisos')
chk('v1.3 avisos (SIM-0): lista de 3 strings = avisos 1, 2 e 4 da folha canônica, sem a numeração; aviso 2 com a sublista na mesma string, recuo de 3 espaços; avisos 3, 5, 6, 7 e 8 não entram', _s0av == [_av[1], _av[2], _av[4]] and len(_s0av) == 3 and _s0av[1].count('\n') == 1 and _s0av[1].split('\n')[1].startswith('   - Dos 23, 17 estão em P2-4.1') and all(isinstance(a, str) and a for a in _s0av) and all(_av[k] not in _s0av for k in (3, 5, 6, 7, 8)))
chk('v1.3 avisos: início literal "**Simulado diagnóstico, não final.**", "**Aderência PARCIAL (23 itens).**", "**Desequilíbrio C/E (contagem real).**"; aviso 1 mantém "(D-ADERENCIA: parcial só em diagnóstico)" no campo (D-T53-07); só o SIM-0 tem o campo', _s0av[0].startswith('**Simulado diagnóstico, não final.** ') and _s0av[1].startswith('**Aderência PARCIAL (23 itens).** ') and _s0av[2].startswith('**Desequilíbrio C/E (contagem real).** ') and '(D-ADERENCIA: parcial só em diagnóstico)' in _s0av[0] and all('avisos' not in s for s in new['simulados'] if s['id'] != 'SIM-0'))
chk('simulados: todo id de simulado existe em itens; 0 repetido dentro de cada simulado', all(x in byid for s in new['simulados'] for x in s['itens']) and all(len(set(s['itens'])) == len(s['itens']) for s in new['simulados']))
chk('simulados: gabarito do simulado (arquivo *_gabarito.md) = gabarito do item no pacote (165/165)', all(byid[x]['gabarito'] == stats['gab_sim'][sid][x] for sid, g in stats['gab_sim'].items() for x in g) and sum(len(g) for g in stats['gab_sim'].values()) == 165)
chk('SIM-0: 60 do banco; = banco (comando+texto da folha); 33 C/27 E; 4 volatil (BQ-0015, 0017, 0035, 0064); 23 parcial', all(x.startswith('BQ-') for x in S['SIM-0']['itens']) and collections.Counter(byid[x]['gabarito'] for x in S['SIM-0']['itens']) == collections.Counter({'C': 33, 'E': 27}) and sorted(x for x in S['SIM-0']['itens'] if byid[x].get('volatil')) == ['BQ-0015', 'BQ-0017', 'BQ-0035', 'BQ-0064'] and sum(byid[x]['aderencia'] == 'parcial' for x in S['SIM-0']['itens']) == 23)
chk('SIM-0 = os 60 BQ da v1.1 (mesma lista e ordem)', S['SIM-0']['itens'] == [s for s in old['simulados'] if s['id'] == 'SIM-0'][0]['itens'])
chk('SIM-1 = v1.1 (40 ids, mesma ordem)', S['SIM-1']['itens'] == [s for s in old['simulados'] if s['id'] == 'SIM-1'][0]['itens'])
for sid in ('SIM-1', 'SIM-2', 'SIM-0-P2'):
    s = S[sid]; c = collections.Counter(byid[x]['gabarito'] for x in s['itens'])
    chk('%s: só AUTORAL; sem volatil; sem parcial; C/E=%s' % (sid, dict(c)), all(byid[x]['rotulo'] == 'AUTORAL' for x in s['itens']) and not any(byid[x].get('volatil') or byid[x]['aderencia'] != 'direta' for x in s['itens']))
chk('SIM-1 20 C/20 E; SIM-2 20 C/20 E; SIM-0-P2 13 C/12 E', [collections.Counter(byid[x]['gabarito'] for x in S[s]['itens']) for s in ('SIM-1', 'SIM-2', 'SIM-0-P2')] == [collections.Counter({'C': 20, 'E': 20}), collections.Counter({'C': 20, 'E': 20}), collections.Counter({'C': 13, 'E': 12})])
chk('simulados finais SIM-1 e SIM-2 sem item de L4-11 nem BQ-0010; SIM-2 (P2) só L1–L3', 'L4-11' not in S['SIM-1']['itens'] and all(stats['item_lote'][x] in ('L1', 'L1C', 'L2', 'L3') for x in S['SIM-2']['itens'] + S['SIM-0-P2']['itens']))
inter = lambda a, b: set(S[a]['itens']) & set(S[b]['itens'])
chk('simulados: SIM-0-P2 ∩ SIM-2 = ∅; SIM-1 ∩ SIM-2 = ∅; SIM-0 ∩ (SIM-1, SIM-2, SIM-0-P2) = ∅', not inter('SIM-0-P2', 'SIM-2') and not inter('SIM-1', 'SIM-2') and not (inter('SIM-0', 'SIM-1') | inter('SIM-0', 'SIM-2') | inter('SIM-0', 'SIM-0-P2')))
# texto da folha = enunciado do pacote
def folha(rel):
    d = {}
    for m in re.finditer(r'^\*\*(\d+)\.\*\* (.*)$', read(rel), re.M): d[int(m.group(1))] = nzs(m.group(2))
    return d
def mapa(rel, col):
    out = {}
    for l in read(rel).split('\n'):
        if l.startswith('| ') and re.match(r'^\| \d+ \|', l):
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            out[int(c[0])] = c[col]
    return out
for sid, fp, gp, col in (('SIM-1', 'saida/simulados/simulado_1.md', 'saida/simulados/simulado_1_gabarito.md', 1), ('SIM-2', 'saida/simulados/simulado_2.md', 'saida/simulados/simulado_2_gabarito.md', 1), ('SIM-0-P2', 'saida/simulados/simulado_0_P2.md', 'saida/simulados/simulado_0_P2_gabarito.md', 1), ('SIM-0', 'saida/simulados/simulado_0_v0.2.md', 'saida/simulados/simulado_0_v0.2_gabarito.md', 2)):
    f = folha(fp); mp = mapa(gp, col)
    mp = {n: i for n, i in mp.items() if re.match(r'^(BQ-\d{4}|[A-Z0-9]+-[A-Z]?\d+)$', i)}
    ordem = [mp[n] for n in sorted(mp)]
    okt = all(f[n] == nzs(byid[mp[n]]['enunciado']) for n in mp if n in f)
    chk('%s: ordem dos ids = ordem do mapa (%d); texto da folha = enunciado do pacote (%d/%d)' % (sid, len(mp), sum(f[n] == nzs(byid[mp[n]]['enunciado']) for n in mp if n in f), len(mp)), ordem == S[sid]['itens'] and okt and len(f) == len(mp))
# comando dos itens de banco no SIM-0 = texto_comando (60/60)
from banco import parse_sim0
cmds, sit, mp0 = parse_sim0()
chk('SIM-0: bloco "Comando" da folha = textoBase + comando do pacote (60/60; 57 só comando, 3 com texto-base)', all(cmds[mp0[n][0]] == nzs((byid[mp0[n][1]]['textoBase'] + ' ' + byid[mp0[n][1]]['comando']).strip()) for n in mp0))
# Aviso 6 / T-36
s0 = read('saida/simulados/simulado_0_v0.2.md')
chk('SIM-0 v0.2: Aviso 6 com a frase da errata de forma (T-36) e 0 "aguardam a conferência"', 'passaram pela conferência do qa-normativo (T-13, 10/10/2026), com gabarito mantido diante do texto vigente' in s0 and 'aguardam a conferência' not in s0)
# ---------------- contagens finais ----------------
c = collections.Counter(v['rotulo'] for v in items)
print('INFO rótulos:', dict(c)); print('INFO C/E total:', collections.Counter(v['gabarito'] for v in items))
fails = [r for r in res if not r['ok']]
print(len(res), 'verificações;', len(fails), 'falhas')
json.dump(res, open(os.path.join(OUT, 'validate.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)
