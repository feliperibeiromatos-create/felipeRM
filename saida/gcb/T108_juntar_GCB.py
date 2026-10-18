# T108_juntar_GCB.py — T-108, GCB: junção das partes A, B e C (v2, aprovadas na R2) em
# saida/gcb/T108_substituicoes_GCB.csv, com conferência mecânica e SHA-256.
# Uso (na raiz do repositório): python -I -X utf8 saida/gcb/T108_juntar_GCB.py
# Lê pacote.json v1.10 e T108_ocorrencias.csv só para leitura; grava apenas o CSV consolidado.
import csv, json, re, collections, copy, hashlib, importlib.util, io, os, sys

R = os.getcwd()
P_ = lambda *a: os.path.join(R, *a)
PARTES = [('A', 'saida/gcb/T108_substituicoes_GCB_parteA_v2.csv'),
          ('B', 'saida/gcb/T108_substituicoes_GCB_parteB_v2.csv'),
          ('C', 'saida/gcb/T108_substituicoes_GCB_parteC_v2.csv')]
ALVO = 'saida/gcb/T108_substituicoes_GCB.csv'
SHA_BASE = 'd43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed'
EXTRA = {'GCB-EXTRA-%02d' % i for i in range(1, 23)}
res = collections.OrderedDict()

def ok(nome, cond, det=''):
    res[nome] = bool(cond)
    print('OK    ' if cond else 'FALHA ', nome, det)

def sha(b): return hashlib.sha256(b).hexdigest()

# 1. leitura das partes
cab, linhas, por_parte = None, [], collections.OrderedDict()
for p, f in PARTES:
    b = open(P_(f), 'rb').read()
    ok('parte %s sem BOM' % p, not b.startswith(b'\xef\xbb\xbf'))
    rd = list(csv.reader(io.StringIO(b.decode('utf-8'), newline='')))
    h, rows = rd[0], [r for r in rd[1:] if r]
    if cab is None: cab = h
    ok('parte %s: cabeçalho igual ao da parte A' % p, h == cab, str(h))
    ok('parte %s: todas as linhas com %d colunas' % (p, len(cab)), all(len(r) == len(cab) for r in rows))
    ok('parte %s: prefixo GCB-%s em todos os ids' % (p, p), all(r[0].startswith('GCB-' + p) for r in rows))
    por_parte[p] = (len(rows), sha(b))
    linhas += rows
    print('   parte %s: %d linhas, SHA-256 %s' % (p, len(rows), sha(b)))
ids = [r[0] for r in linhas]
ok('ids de edição únicos no consolidado', len(ids) == len(set(ids)), str([i for i, c in collections.Counter(ids).items() if c > 1]))
ok('contagem = soma das partes (%s = %d)' % ('+'.join(str(v[0]) for v in por_parte.values()), len(linhas)),
   len(linhas) == sum(v[0] for v in por_parte.values()))
D = [dict(zip(cab, r)) for r in linhas]
ok('nenhum \\r em antes/depois', not [d['id_edicao'] for d in D if '\r' in d['antes'] or '\r' in d['depois']])
ok('acao em {DELETAR, SUBSTITUIR}; regra 1-5 com ;', all(d['acao'] in ('DELETAR', 'SUBSTITUIR') and re.fullmatch(r'[1-5](;[1-5])*', d['regra']) for d in D))
ok('DELETAR com depois vazio; SUBSTITUIR com depois não vazio e diferente de antes',
   not [d['id_edicao'] for d in D if (d['acao'] == 'DELETAR' and d['depois']) or (d['acao'] == 'SUBSTITUIR' and (not d['depois'] or d['depois'] == d['antes']))])

# 2. gravação (RFC 4180, CRLF entre registros, aspas mínimas, UTF-8 sem BOM) e releitura
buf = io.StringIO(newline='')
w = csv.writer(buf, lineterminator='\r\n', quoting=csv.QUOTE_MINIMAL)
w.writerow(cab); w.writerows(linhas)
out = buf.getvalue().encode('utf-8')
open(P_(ALVO), 'wb').write(out)
back = list(csv.reader(io.StringIO(open(P_(ALVO), 'rb').read().decode('utf-8'), newline='')))
ok('releitura do consolidado = cabeçalho único + linhas das partes, na ordem A, B, C', back[0] == cab and back[1:] == linhas and sum(1 for r in back if r == cab) == 1)
SHA_ALVO = sha(open(P_(ALVO), 'rb').read())

# 3. conferência contra o pacote v1.10 e o inventário
raw = open(P_('saida/pacote/pacote.json'), 'rb').read()
ok('SHA-256 LF do pacote.json v1.10', sha(raw.replace(b'\r\n', b'\n')) == SHA_BASE)
P = json.loads(raw.decode('utf-8'))
spec = importlib.util.spec_from_file_location('inv', P_('saida/pacote/T108_inventario.py'))
inv = importlib.util.module_from_spec(spec); spec.loader.exec_module(inv)
occ = list(csv.DictReader(open(P_('saida/pacote/T108_ocorrencias.csv'), encoding='utf-8', newline='')))
U = {x['id_ocorrencia']: x for x in occ if x['arquivo'] == 'pacote.json' and x['gerencia'] == 'GCB' and x['classe'] in ('PROCESSO', 'VERIFICAR')}
FPs = [x for x in occ if x['arquivo'] == 'pacote.json' and x['gerencia'] == 'GCB' and x['classe'].startswith('FP')]

def nav(root, path):
    kind, key, rest = re.match(r'(itens|lotes)\[([^\]]+)\]\.(.*)', path).groups()
    o = [i for i in root[kind] if i['id'] == key][0]
    parts = re.findall(r'[^.\[\]]+', rest)
    for part in parts[:-1]: o = o[int(part)] if part.isdigit() else o[part]
    return o, (int(parts[-1]) if parts[-1].isdigit() else parts[-1])

base = {cam: t for _, _, cam, t, _ in inv.campos(P, 'D')}
ok('caminhos resolvem a string', all(d['caminho'] in base for d in D), str([d['id_edicao'] for d in D if d['caminho'] not in base][:5]))
ok('antes literal e único no campo da v1.10', not [d['id_edicao'] for d in D if base[d['caminho']].count(d['antes']) != 1])
esp = collections.defaultdict(list)
for d in D:
    a = base[d['caminho']].find(d['antes']); esp[d['caminho']].append((a, a + len(d['antes']), d['id_edicao']))
sob = [(x[2], y[2]) for v in esp.values() for x, y in zip(sorted(v), sorted(v)[1:]) if y[0] < x[1]]
ok('sem sobreposição entre edições do mesmo campo', not sob, str(sob))
cit = collections.Counter(i for d in D for i in d['ids_ocorrencia'].split(';'))
fora = set(cit) - set(U) - EXTRA
ok('cobertura: %d do CSV + 22 EXTRA = %d, cada um uma vez' % (len(U), len(U) + 22),
   set(cit) == set(U) | EXTRA and all(v == 1 for v in cit.values()), 'faltam %d; fora %s' % (len((set(U) | EXTRA) - set(cit)), sorted(fora)))
ok('id do CSV com o mesmo caminho da linha', not [(d['id_edicao'], i) for d in D for i in d['ids_ocorrencia'].split(';') if i in U and U[i]['caminho'] != d['caminho']])
ok('nenhum FP citado em linha', not ({x['id_ocorrencia'] for x in FPs} & set(cit)))

# proibições do depois (D1 da GBQ, 1.4, item 7) e preservação de "verificado em"/base legal (item 8)
PROIB = [r'\b[FN]\d{1,2}\b', r'\bU\d\b', r'\bGG\d\b', r'\bTB\d\b', r'L\d[A-C]?-[QR]?\d+', r'\b\d[A-C]-\d{2}\b', r'\bA5-\d{2}\b',
         r'\bBQ-\d{4}\b', r'\[V ', r'NORMATIVO', r'REVERIFICAR', r'\bQA\b', r'CQFP', r'CPP', r'\bGCE\b', r'\bGCB\b', r'\bGBQ\b',
         r'\bD-[A-Z0-9-]+', r'\bT-\d+', r'\bLote \d', r'^(TC|IC|GI|AT)\b', r'\b(TC|IC|GI|AT)\s*[—:-]', r'\[TS\]', r'Difere do item', r'VOLÁTE?IS?\b']
hits = [(d['id_edicao'], rx, m.group(0)) for d in D for rx in PROIB for m in [re.search(rx, d['depois'], re.M)] if m]
ok('proibições do depois (1.4, item 7): 0 casamentos', not hits, str(hits))
perda = []
for d in D:
    if '3' in d['regra'].split(';'): continue
    for rx in (r'verificado em \d{2}/\d{2}/\d{4}', r'\b(?:Lei|Decreto|art\.|inciso|§)'):
        for g in set(m.group(0) for m in re.finditer(rx, d['antes'])):
            if d['depois'].count(g) < d['antes'].count(g): perda.append((d['id_edicao'], g))
ok('"verificado em" e base legal preservados (1.4, item 8)', not perda, str(perda))
def locate_fp(x):
    t = base.get(x['caminho'], ''); tr = x['trecho'].replace(' ⏎ ', '\n').replace('⏎', '\n')
    i = t.find(tr)
    if i < 0: return None
    c = min((m for m in range(len(tr)) if tr.startswith(x['casamento'], m)), key=lambda m: abs(m - (len(tr) - len(x['casamento'])) / 2))
    return i + c, i + c + len(x['casamento'])
dentro, nloc = [], []
for x in FPs:
    sp = locate_fp(x)
    if sp is None: nloc.append(x['id_ocorrencia']); continue
    for a, b, i in esp.get(x['caminho'], []):
        dd = [d for d in D if d['id_edicao'] == i][0]
        if a <= sp[0] and sp[1] <= b and dd['depois'].count(x['casamento']) < dd['antes'].count(x['casamento']): dentro.append((x['id_ocorrencia'], i, x['casamento']))
print('   FP localizados por posição: %d de %d (não localizados: %s)' % (len(FPs) - len(nloc), len(FPs), nloc))
ok('FP-R1/FP-CONTEUDO fora de todo antes ou intactos (1.4, item 5; por posição)', not dentro and not nloc, str(dentro))

# aplicação numa cópia e nova varredura
Q = copy.deepcopy(P)
for cam, v in esp.items():
    o, k = nav(Q, cam); t = o[k]
    for a, b, i in sorted(v, reverse=True):
        dd = [d for d in D if d['id_edicao'] == i][0]
        assert t[a:b] == dd['antes']; t = t[:a] + dd['depois'] + t[b:]
    o[k] = t
LOT = ('4', '4-C', '5', '5-C', '6a', '6b')
r0 = [x for x in inv.varre(P, 'D') if x['gerencia'] == 'GCB']
r1 = [x for x in inv.varre(Q, 'D') if x['gerencia'] == 'GCB']
c0 = collections.Counter((x['lote'], x['classe']) for x in r0); c1 = collections.Counter((x['lote'], x['classe']) for x in r1)
ok('re-varredura: 0 PROCESSO e 0 VERIFICAR na GCB', not [x for x in r1 if x['classe'] in ('PROCESSO', 'VERIFICAR')],
   str([(x['caminho'], x['casamento']) for x in r1 if x['classe'] in ('PROCESSO', 'VERIFICAR')][:8]))
ok('FP-CONTEUDO por lote iguais antes e depois', all(c0[(l, 'FP-CONTEUDO')] == c1[(l, 'FP-CONTEUDO')] for l in LOT),
   str({l: (c0[(l, 'FP-CONTEUDO')], c1[(l, 'FP-CONTEUDO')]) for l in LOT}))
ok('FP-R1 "A tecla F4" intacta (casada por texto, 1 → 1)',
   sum(t.count('A tecla F4') for _, _, _, t, _ in inv.campos(P, 'D')) == 1 == sum(t.count('A tecla F4') for _, _, _, t, _ in inv.campos(Q, 'D')))
mud = []
for kind in ('itens', 'lotes'):
    for a, b in zip(P[kind], Q[kind]):
        for k in a:
            if a[k] != b[k]: mud.append((kind, a['id'], k))
ok('só mudam justificativa, curso, resumo, pegadinhas, pares (itens/lotes da GCB)',
   all((k == 'justificativa' if kd == 'itens' else k in ('curso', 'resumo', 'pegadinhas', 'pares')) for kd, _, k in mud)
   and all(k2 not in ('enunciado', 'gabarito', 'itemEdital') for _, _, k2 in mud) and all(P[k] == Q[k] for k in P if k not in ('itens', 'lotes')),
   '%d campos alterados' % len(mud))
TX = '\n'.join(t for lo, _, _, t, _ in inv.campos(Q, 'D') if inv.GER.get(lo) == 'GCB')
for k in ['(O11)', 'fundamenta item', 'neste chat', 'não sutil', 'entra em item', 'entram em item', '(CI,', 'ITENS REAIS', 'TC invertida', 'indevida invertida', 'Não usada em item', 'invertida (']:
    ok('resíduo 0: %r' % k, k not in TX, str(TX.count(k)))
print('   "hoje" minúsculo:', len(re.findall(r'\bhoje\b', TX)), '| "Hoje" maiúsculo:', [TX[m.start():m.start() + 60] for m in re.finditer(r'\bHoje\b', TX)])
print('   ", às avessas":', TX.count(', às avessas'))

# 4. contagens
print('\nContagens do consolidado')
for nome, chave in (('parte', lambda d: d['id_edicao'][4]), ('lote', lambda d: d['lote']), ('categoria', lambda d: d['categoria']),
                    ('acao', lambda d: d['acao']), ('regra', lambda d: d['regra']), ('modo', lambda d: d['modo'])):
    print('  por %s:' % nome, dict(sorted(collections.Counter(chave(d) for d in D).items())))
print('  ocorrências do CSV por lote:', dict(sorted(collections.Counter(x['lote'] for x in U.values()).items())))
print('  ocorrências do CSV por categoria:', dict(sorted(collections.Counter(x['categoria'] for x in U.values()).items())))
print('  antes da aplicação (lote, classe):', dict(sorted(c0.items())))
print('  depois da aplicação (lote, classe):', dict(sorted(c1.items())))
print('  EXTRA → linha:', {i: d['id_edicao'] for d in D for i in d['ids_ocorrencia'].split(';') if i in EXTRA})
print('\n%s: %d linhas + cabeçalho, %d bytes, SHA-256 %s' % (ALVO, len(linhas), len(out), SHA_ALVO))
print('TUDO OK' if all(res.values()) else 'HÁ FALHAS: ' + str([k for k, v in res.items() if not v]))
sys.exit(0 if all(res.values()) else 1)
