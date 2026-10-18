import csv, json, re, collections, copy, hashlib, sys, subprocess, os, tempfile, shutil
rows = list(csv.DictReader(open(r'saida\gcb\T108_substituicoes_GCB_parteA.csv', encoding='utf-8', newline='')))
raw = open(r'saida\pacote\pacote.json', 'rb').read()
sha = hashlib.sha256(raw.replace(b'\r\n', b'\n')).hexdigest()
p = json.loads(raw.decode('utf-8'))
occ = list(csv.DictReader(open(r'saida\pacote\T108_ocorrencias.csv', encoding='utf-8')))
LOTES = ('4', '4-C')
univ = [x for x in occ if x['gerencia'] == 'GCB' and x['arquivo'] == 'pacote.json' and x['classe'] in ('PROCESSO', 'VERIFICAR') and x['lote'] in LOTES]
res = {}
def ok(name, cond, det=''):
    res[name] = bool(cond)
    print(('OK    ' if cond else 'FALHA '), name, det)

def nav(root, path):
    m = re.match(r'(itens|lotes)\[([^\]]+)\]\.(.*)', path)
    kind, key, rest = m.groups()
    o = [i for i in root[kind] if i['id'] == key][0]
    parts = re.findall(r'[^.\[\]]+', rest)
    for part in parts[:-1]:
        o = o[int(part)] if part.isdigit() else o[part]
    last = parts[-1]
    return o, (int(last) if last.isdigit() else last)

def locate_fp(x):
    o, k = nav(p, x['caminho']); t = o[k]
    tr = x['trecho'].replace(' ⏎ ', '\n').replace('⏎', '\n')
    i = t.find(tr)
    if i < 0: return None
    cands = [m for m in range(len(tr)) if tr.startswith(x['casamento'], m)]
    c = min(cands, key=lambda m: abs(m - (len(tr) - len(x['casamento'])) / 2))
    return i + c, i + c + len(x['casamento'])

ok('SHA-256 LF do pacote.json = d43c32de...', sha.startswith('d43c32de4b8afb22'), sha[:16])
bad = []
for r in rows:
    o, k = nav(p, r['caminho'])
    if o[k].count(r['antes']) != 1: bad.append(r['id_edicao'])
ok('(a) antes literal e unico no campo (v1.10)', not bad, str(bad))
ids = collections.Counter(i for r in rows for i in r['ids_ocorrencia'].split(';'))
U = {x['id_ocorrencia'] for x in univ}
ok('(b) %d ocorrencias do universo cobertas exatamente 1x' % len(U), set(ids) == U and all(v == 1 for v in ids.values()),
   'faltam %d, extras %d, repetidos %d' % (len(U - set(ids)), len(set(ids) - U), len([1 for v in ids.values() if v > 1])))
by = {x['id_ocorrencia']: x for x in univ}
bad = []
for r in rows:
    o, k = nav(p, r['caminho']); a = o[k].find(r['antes'])
    for i in r['ids_ocorrencia'].split(';'):
        x = by[i]
        if x['caminho'] != r['caminho'] or x['lote'] != r['lote']: bad.append((r['id_edicao'], i, 'caminho/lote'))
        sp = locate_fp(x)
        if sp is None or not (a <= sp[0] and sp[1] <= a + len(r['antes'])): bad.append((r['id_edicao'], i, 'fora do antes'))
ok('(b2) cada ocorrencia esta dentro do antes da sua edicao (posicao), mesmo caminho e lote', not bad, str(bad[:5]))
byp = collections.defaultdict(list)
for r in rows:
    o, k = nav(p, r['caminho']); s = o[k].find(r['antes']); byp[r['caminho']].append((s, s + len(r['antes']), r['id_edicao']))
ov = [(a, b) for v in byp.values() for a, b in zip(sorted(v), sorted(v)[1:]) if b[0] < a[1]]
ok('(b3) edicoes sem sobreposicao no campo', not ov, str(ov[:3]))
fp = [x for x in occ if x['gerencia'] == 'GCB' and x['arquivo'] == 'pacote.json' and x['lote'] in LOTES and x['classe'].startswith('FP')]
n = []
for x in fp:
    sp = locate_fp(x)
    if sp is None: continue
    for r in rows:
        if r['caminho'] == x['caminho']:
            o, k = nav(p, r['caminho']); a = o[k].find(r['antes'])
            if a <= sp[0] and sp[1] <= a + len(r['antes']): n.append((x['id_ocorrencia'], r['id_edicao']))
ok('(c) FP-R1/FP-CONTEUDO dos lotes 4 e 4-C (n=%d; FP-R1 = %d) fora de todo antes' % (len(fp), len([x for x in fp if x['classe'] == 'FP-R1'])), not n, str(n))

q = copy.deepcopy(p)
for path in {r['caminho'] for r in rows}:
    o, k = nav(q, path); t = o[k]
    for r in sorted([r for r in rows if r['caminho'] == path], key=lambda r: -t.find(r['antes'])):
        a = t.find(r['antes']); t = t[:a] + r['depois'] + t[a + len(r['antes']):]
    o[k] = t
chg = []
for kind in ('itens', 'lotes'):
    for a, b in zip(p[kind], q[kind]):
        for k in a:
            if a[k] != b[k]: chg.append((kind, a['id'], k))
for k in p:
    if k not in ('itens', 'lotes') and p[k] != q[k]: chg.append(('raiz', k, ''))
forb = [c for c in chg if (c[0] == 'itens' and c[2] != 'justificativa') or (c[0] == 'lotes' and c[2] not in ('curso', 'resumo', 'pegadinhas', 'pares')) or c[0] == 'raiz']
ok('(f) so mudam justificativa, curso, resumo, pegadinhas[].texto, pares[].como; enunciado, gabarito e itemEdital intactos', not forb, str(forb[:5]))
ok('(f2) so itens L4-* e 4C-* e o lote L4 mudaram', all(c[1].startswith(('L4-', '4C-')) or c[1] == 'L4' for c in chg), '%d campos alterados' % len(chg))
a = [l for l in p['lotes'] if l['id'] == 'L4'][0]; b = [l for l in q['lotes'] if l['id'] == 'L4'][0]
pg = [i for i, (x, y) in enumerate(zip(a['pegadinhas'], b['pegadinhas'])) if {k: v for k, v in x.items() if k != 'texto'} != {k: v for k, v in y.items() if k != 'texto'}]
pr = [i for i, (x, y) in enumerate(zip(a['pares'], b['pares'])) if {k: v for k, v in x.items() if k != 'como'} != {k: v for k, v in y.items() if k != 'como'}]
ok('(f3) pegadinhas (salvo texto) e pares (salvo como) intactos', not pg and not pr)

pats = collections.OrderedDict([
 ('codigo de fonte', r'(?<![\w.])(F\d{1,2}|N\d{1,2}|U\d|GG\d|TB\d)(?![\w])'),
 ('codigo de item/par/pegadinha', r'\b(L\d-\d{2}|[4-6][A-C]?-\d{2}|A\d-\d{2}|C\d{2}|P\d{1,2})\b'),
 ('Lote N / lote de producao', r'(?i)\blotes?\s+\d|\b(neste|do|este|o|no) lote\b'),
 ('QA/CQFP/CPP/GCB/GCE/GBQ', r'\b(QA|CQFP|CQE|CPP|GCB|GCE|GBQ)\b'),
 ('TC/IC/GI/AT', r'\b(TC|IC|GI|AT)\b'),
 ('[TS]', r'\[TS\]'),
 ('VOLATIL', r'VOL.T[IE]'),
 ('Difere do item', r'Difere do item'),
 ('instrucao interna', r'(?i)só o fato|sem item|não gabarito|não cobrar|reverificar|CEBRASPE_ANALOGA|GAB_DEFINITIVO|sem armadilha'),
 ('versao/errata', r'\bv\d(\.\d+)?\b|(?i:errata)'),
 ('etiqueta [V ..]/[NORMATIVO ..]', r'\[(V|NORMATIVO)\b'),
])
hits = []
for r in rows:
    for nm, rx in pats.items():
        m = re.search(rx, r['depois'])
        if m: hits.append((r['id_edicao'], nm, m.group(0)))
ok('(e) nenhum depois com codigo de fonte/item/par/pegadinha, Lote N, QA/CQFP, TC/IC/GI/AT, [TS], VOLATIL, Difere, instrucao interna, versao', not hits, str(hits[:8]))

d = tempfile.mkdtemp(prefix='t108a_')
json.dump(q, open(os.path.join(d, 'pacote.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
shutil.copy(r'saida\pacote\T108_inventario.py', os.path.join(d, 'T108_inventario.py'))
shutil.copy(r'saida\pacote\pacote_estudante.json', os.path.join(d, 'pacote_estudante.json'))
rr = subprocess.run([sys.executable, '-I', '-X', 'utf8', os.path.join(d, 'T108_inventario.py'), d, os.path.join(d, 'cont.json')], capture_output=True, text=True, encoding='utf-8')
print('inventario rc', rr.returncode, (rr.stdout or '')[-300:], (rr.stderr or '')[-300:])
csvs = [f for f in os.listdir(d) if f.endswith('.csv')]
if csvs:
    o2 = list(csv.DictReader(open(os.path.join(d, csvs[0]), encoding='utf-8')))
    rem = [x for x in o2 if x['arquivo'] == 'pacote.json' and x['lote'] in LOTES and x['classe'] in ('PROCESSO', 'VERIFICAR')]
    fp2 = [x for x in o2 if x['arquivo'] == 'pacote.json' and x['lote'] in LOTES and x['classe'].startswith('FP')]
    ok('(d) varredura (T108_inventario.py) no texto aplicado: PROCESSO+VERIFICAR dos lotes 4 e 4-C = 0', not rem,
       'restantes %d: %s' % (len(rem), [(x['id_ocorrencia'], x['casamento']) for x in rem[:6]]))
    ok('(d2) FP dos lotes 4 e 4-C: mesmo numero antes e depois (%d, %d)' % (len(fp), len(fp2)), len(fp) == len(fp2))
else:
    ok('(d) varredura executada', False, 'sem CSV do inventario em ' + d)
cnt = collections.Counter((r['lote'], r['categoria'], r['acao']) for r in rows)
print()
for k in sorted(cnt): print(k, cnt[k])
print('por lote', dict(collections.Counter(r['lote'] for r in rows)), 'modo', dict(collections.Counter(r['modo'] for r in rows)), 'regra', dict(collections.Counter(r['regra'] for r in rows)), 'acao', dict(collections.Counter(r['acao'] for r in rows)))
print('ocorrencias por lote', dict(collections.Counter(x['lote'] for x in univ)))
print('MANTER:', [r['id_edicao'] for r in rows if r['acao'] == 'MANTER'], '| NAO IDENTIFICADO:', [r['id_edicao'] for r in rows if 'IDENTIFICADO' in r['fonte_origem'].upper()])
print('TUDO OK' if all(res.values()) else 'HA FALHAS')
