# conferir_fidelidade_D6.py — T-72 (ordem DA 20/10/2026, passo 5) — 2026-10-20 — gerado por gcb-cpp
# Conferência própria de fidelidade: compara as palavras do texto de saída (D6_plataforma.json) com as do texto de
# origem (saida/gcb/D6_v2_1.md), depois de remover as marcas permitidas (lista independente da usada no formatador).
# Palavra acrescentada fora das trocas registradas = defeito. Uso: python3 -I saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D6.py
import collections, difflib, json, pathlib, re, sys

RAIZ = pathlib.Path(__file__).resolve().parents[4]
L = (RAIZ / 'saida/gcb/D6_v2_1.md').read_text(encoding='utf-8').split('\n')
D = json.loads((RAIZ / 'saida/gcb/DA_plataforma/D6_plataforma.json').read_text(encoding='utf-8'))

MARCAS = [  # marcas e trechos de processo permitidos pela seção 6/7 da especificação (removidos da origem antes de comparar)
    r' ?\[QA PENDENTE — (trecho|par|pegadinha) importad[oa]\]',
    r'\*\[Acréscimo sobre o Anexo N — QA PENDENTE\.\]\*',
    r', nos termos do texto transcrito no Anexo N',
    r'; dispositivo vigente, em redação original, conforme a errata T-82 do Anexo N, seção 8',
    r' Este lote não cobra datas de vigência de leis alteradoras\.',
    r'REVERIFICAR para (os dispositivos assinalados|o art\. 55-A|o art\. 5º, VIII)',
    r'REVERIFICAR quanto à denominação em 55-A',
    r'REVERIFICAR',
]

def tira_marcas(t):
    for m in MARCAS:
        t = re.sub(m, ' ', t)
    return t

def tok(t):
    return re.findall(r'[^\W_]+', t.lower())

def compara(origem, saida, nome, permitido=()):
    co, cs = collections.Counter(tok(origem)), collections.Counter(tok(saida))
    add = cs - co
    falta = co - cs
    add_ruim = {w: n for w, n in add.items() if w not in permitido}
    ops = [op for op in difflib.SequenceMatcher(None, tok(origem), tok(saida), autojunk=False).get_opcodes() if op[0] in ('insert', 'replace')]
    return add, add_ruim, falta, ops

SAIDA = []
DEFEITOS = 0
def reg(m):
    SAIDA.append(m)

# ------------------------------------------------------------ curso, bloco a bloco
def blocos_origem():
    out, cur = [], None
    for ln in L[L.index(next(x for x in L if x.startswith('## 1.1'))):L.index('# 2. (b) RESUMO')]:
        m = re.match(r'### ([LG]\d+)\. (.*)$', ln)
        if m:
            cur = {'cod': m.group(1), 'titulo': m.group(2), 'corpo': []}
            out.append(cur)
        elif cur is not None and not ln.startswith('#') and ln.strip() and ln.strip() != '---':
            cur['corpo'].append(ln)
    return out

BO = blocos_origem()
curso = D['lote']['curso']
pedacos = [x.split('\n## ')[0] for x in re.split(r'^### ', curso, flags=re.M)[1:]]
assert len(BO) == len(pedacos) == 47, (len(BO), len(pedacos))
ROTULOS = {'DEFINIÇÃO', 'EXEMPLO PARLAMENTAR', 'PEGADINHA PROVÁVEL'}
tot_add = tot_falta = 0
reg('### 6.1 Curso: palavras do bloco de saída × bloco de origem (47 blocos)')
reg('')
reg('Origem = título (sem código) + parágrafos do bloco, sem rótulos "Definição.", "Exemplo.", "Pegadinha provável." e sem as marcas permitidas. Saída = título + texto do bloco, sem os rótulos de quadro e sem as listas BASE LEGAL. Contagem de palavras por multiconjunto (maiúsculas ignoradas) e sequência (difflib).')
reg('')
for b, p in zip(BO, pedacos):
    pai = 'LEI DE ACESSO À INFORMAÇÃO (Lei 12.527/2011)' if b['cod'][0] == 'L' else 'LEI GERAL DE PROTEÇÃO DE DADOS PESSOAIS (Lei 13.709/2018, texto compilado)'
    corpo = '\n'.join(b['corpo'])
    corpo = corpo.replace('**Definição.** ', '').replace('**Exemplo.** ', '').replace('**Pegadinha provável.** ', '')
    origem = tira_marcas(b['titulo'] + '\n' + corpo)
    linhas = p.split('\n')
    titulo = linhas[0]
    resto, em_base, base = [], False, []
    for ln in linhas[1:]:
        if ln.strip() in ROTULOS:
            em_base = False; continue
        if ln.strip() == 'BASE LEGAL':
            em_base = True; continue
        if em_base:
            if ln.strip() == '':
                em_base = False
            else:
                base.append(ln)
            continue
        resto.append(ln)
    saida = titulo + '\n' + '\n'.join(resto)
    add, add_ruim, falta, ops = compara(origem, saida, b['cod'])
    # BASE LEGAL: vocabulário do bloco de origem + título da seção-mãe
    voc = set(tok(origem + ' ' + pai))
    fora = sorted({w for ln in base for w in tok(ln) if w not in voc})
    ok = not add and not falta and not ops and not fora
    if not ok:
        DEFEITOS += 1
    tot_add += sum(add.values()); tot_falta += sum(falta.values())
    reg(f'- {b["cod"]}: palavras acrescentadas {sum(add.values())}; suprimidas {sum(falta.values())}; operações de inserção/troca na sequência {len(ops)}; palavras de BASE LEGAL fora do vocabulário do bloco {len(fora)}' + ('' if ok else f' — ACRESCENTADAS {dict(add)}; SUPRIMIDAS {dict(falta)}; FORA {fora}'))
reg('')
reg(f'Total curso: palavras acrescentadas {tot_add}; suprimidas {tot_falta}; blocos com divergência {DEFEITOS}.')
reg('')

# ------------------------------------------------------------ resumo
r1 = next(i for i, x in enumerate(L) if x.startswith('## 2.1 Resumo')); r3 = next(i for i in range(r1, len(L)) if L[i] == '---')
orig = tira_marcas('\n'.join(x for x in L[r1:r3] if x.strip()))
add, add_ruim, falta, ops = compara(orig, D['lote']['resumo'], 'resumo')
reg('### 6.2 Resumo (seções 2.1 e 2.2)')
reg('')
reg(f'- Acrescentadas {dict(add)}; suprimidas {dict(falta)}. Esperado: nenhuma acrescentada (os cabeçalhos "Resumo — LAI/LGPD" perdem a palavra "Resumo"; "art." inicial vira "Art.", sem mudar a palavra).')
if add: DEFEITOS += 1
reg('')

# ------------------------------------------------------------ pares
def tab(prefixo):
    i = next(k for k, x in enumerate(L) if x.startswith(prefixo))
    out = []
    while i < len(L) and not L[i].startswith('|'): i += 1
    while i < len(L) and L[i].startswith('|'):
        c = [x.strip() for x in L[i].strip().strip('|').split('|')]
        if len(c) == 5 and re.match(r'^[LGI]-P\d+$', c[0]): out.append(c)
        i += 1
    return out
rows = tab('## 3.1') + tab('## 3.2') + tab('## 3.3')
reg('### 6.3 Pares (43)')
reg('')
reg('Origem = campos "Par", "Diferença" e "Como a banca troca" (sem marcas); saída = a + b + como. Palavras permitidas por construção: "como", "a", "banca", "troca" (rótulo " Como a banca troca: " da especificação).')
reg('')
ruim = 0
for r, p in zip(rows, D['lote']['pares']):
    origem = tira_marcas(' '.join([r[1], r[2], r[4]]))
    add, add_ruim, falta, ops = compara(origem, ' '.join([p['a'], p['b'], p['como']]), r[0], permitido={'como', 'a', 'banca', 'troca'})
    # a palavra "a" também existe na origem; o multiconjunto já desconta as ocorrências da origem
    if r[0] == 'I-P5':
        reg(f'- {r[0]} (sem " × " no campo Par): b = "{p["b"]}" — palavras tiradas da coluna "Diferença" do próprio par.')
        add_ruim = {w: n for w, n in add_ruim.items() if w not in tok(r[2])}
    if add_ruim:
        ruim += 1; reg(f'- {r[0]}: ACRESCENTADAS {add_ruim}')
reg(f'- Pares com palavra acrescentada fora do rótulo permitido: {ruim}.')
DEFEITOS += ruim
reg('')

# ------------------------------------------------------------ pegadinhas
i0 = next(i for i, x in enumerate(L) if x.startswith('# 4. PEGADINHAS')); i1 = next(i for i in range(i0, len(L)) if L[i] == '---')
orig_p = [re.sub(r'^\d+\. ', '', x) for x in L[i0:i1] if re.match(r'^\d+\. ', x)]
reg('### 6.4 Pegadinhas (63)')
reg('')
ruim = 0
for k, (o, p) in enumerate(zip(orig_p, D['lote']['pegadinhas']), 1):
    add, add_ruim, falta, ops = compara(tira_marcas(o), p['texto'], f'peg {k}', permitido={'base'})
    if add_ruim:
        ruim += 1; reg(f'- pegadinha {k}: ACRESCENTADAS {add_ruim}')
reg(f'- Pegadinhas com palavra acrescentada além de "Base": {ruim}. (Só "Base:" foi acrescentada, no lugar do separador " — ".)')
DEFEITOS += ruim
reg('')

# ------------------------------------------------------------ justificativas
j2 = next(i for i, x in enumerate(L) if x.startswith('## 5.2'))
orig_j = {}
for i in range(j2, len(L)):
    m = re.match(r'^\*\*(D6-\d\d)\*\* — Gabarito', L[i])
    if m:
        orig_j[m.group(1)] = (L[i + 2][len('Justificativa: '):] + ' ' + L[i + 3])
reg('### 6.5 Justificativas (50)')
reg('')
tot = collections.Counter(); ruim = 0
for it in D['itens']:
    add, add_ruim, falta, ops = compara(tira_marcas(orig_j[it['id']]), it['justificativa'], it['id'], permitido={'troca', 'sutil', 'da'})
    tot.update(add)
    if add_ruim:
        ruim += 1; reg(f'- {it["id"]}: ACRESCENTADAS {add_ruim}')
reg(f'- Palavras acrescentadas em todas as justificativas (contagem total): {dict(tot)} — todas da troca mínima registrada "do [TS]" → "da troca sutil". Itens com palavra fora dessa troca: {ruim}.')
DEFEITOS += ruim
reg('')
reg(f'RESULTADO DA CONFERÊNCIA DE FIDELIDADE: {DEFEITOS} defeito(s).')
print('\n'.join(SAIDA))
sys.exit(1 if DEFEITOS else 0)
