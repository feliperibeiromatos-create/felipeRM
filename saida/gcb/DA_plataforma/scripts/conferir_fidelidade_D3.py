# conferir_fidelidade_D3.py — T-76 (ordem DA 20/10/2026) — 2026-10-20 — gerado por gcb-cpp
# Conferência própria de fidelidade: reconstrói, a partir do texto de origem (saida/gcb/D3_v2_1.md) e de uma lista de
# passagens e marcas registradas INDEPENDENTE da usada no formatador, o texto que a saída deve ter, e compara com
# D3_plataforma.json palavra a palavra, na ordem (difflib). Palavra acrescentada, suprimida ou fora de lugar = defeito.
# Confere também itens (enunciado e gabarito literais), tópicos (números, dispositivos e baseLegal letra a letra no mapa).
# Uso: python3 -I saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D3.py
import collections, difflib, json, pathlib, re, sys

RAIZ = pathlib.Path(__file__).resolve().parents[4]
L = (RAIZ / 'saida/gcb/D3_v2_1.md').read_text(encoding='utf-8').split('\n')
D = json.loads((RAIZ / 'saida/gcb/DA_plataforma/D3_plataforma.json').read_text(encoding='utf-8'))
MAPA = (RAIZ / 'saida/gcb/D3_anexo_N_mapa_normativo.md').read_text(encoding='utf-8')

def tok(t): return re.findall(r'[^\W_]+', t.lower())

SAIDA, DEF = [], 0
def reg(m): SAIDA.append(m)

def seq_igual(esperado, obtido):
    """None se as sequências de palavras são idênticas; senão, descrição curta da primeira diferença."""
    a, b = tok(esperado), tok(obtido)
    if a == b: return None
    ops = [op for op in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if op[0] != 'equal']
    op = ops[0]
    return f'{len(ops)} diferença(s); 1ª: {op[0]} esperado={a[op[1]:op[2]][:8]} obtido={b[op[3]:op[4]][:8]}'

# ------------------------------------------------------------ passagens registradas (independentes do formatador)
# por bloco do curso: trechos do texto de origem (título + corpo do bloco) que a especificação manda tirar, ou trocas mínimas
PASSAGENS = {
 'C5.1-01': [('O texto legal do recorte', 'O texto legal do curso'), ('Nenhum dispositivo do recorte', 'Nenhum dispositivo do curso')],
 'C5.1-05': [('Nenhum dispositivo do recorte', 'Nenhum dispositivo do curso'), ('; o regime disciplinar da Lei 8.112/1990 não faz parte deste lote ([SEM FONTE — não afirmar])', '')],
 'C5.1-07': [(' O instrumento formal da sustação não consta do Anexo N: [SEM FONTE — não afirmar].', '')],
 'C6.2-02': [(' A ação regressiva é desta folha.', '')],                      # errata de forma 20/10/2026 (achado 1): frase de organização da produção
 'C6.4-04': [('é da folha 6.1.', 'é do subitem 6.1.')],                      # errata de forma 20/10/2026 (achado 1): remissão "folha" → "subitem"
 'C6.3-01': [(' O curso não afirma o regime aplicável à omissão: [SEM FONTE — não afirmar] (ver C6.3-06).', '')],
 'C6.5-01': [(' e ausência de texto no recorte', ''), ('; o despacho não pede outros artigos do Código Civil', '')],
 'C6.5-02': [(' A distinção entre os dois, e entre caso fortuito interno e externo: [SEM FONTE — não afirmar].', ''),
             (', ou condicionar sua eficácia a distinções sem fonte', '')],
 'C6.5-04': [(' Ônus da prova da excludente: [SEM FONTE — não afirmar].', '')],
 'C6.5-05': [(' Hipóteses concretas de risco integral: [SEM FONTE — não afirmar].', '')],
 'C7-01': [('; Anexo N, seção 2.1)', ')')],
 'C7-19': [(' Tema jurisprudencial do ressarcimento: [SEM FONTE — não afirmar].', '')],
 'C7-20': [(' no Anexo N, seção 2.1', ''), (' Tratamento jurisprudencial do tema: [SEM FONTE — não afirmar].', '')],
 'C7-23': [(' (o texto do § 1º do art. 37 da CF não consta do Anexo N e não é afirmado aqui)', '')],
}
DESCARTADOS = {'C5.1-10', 'C6.1-06', 'C6.2-04', 'C6.3-06'}
G_DESCARTADAS = {10, 22, 26, 32}

def limpa_geral(t):
    t = re.sub(r'\s?\(Anexo N, [^)]*\)', '', t)
    t = t.replace('BASE DOUTRINÁRIA (ponto pacífico): ', '')
    return t

def base_limpa(b):
    """b = texto entre 'Desfeita por:' e ']' (ou depois de 'Dispositivo:'); devolve '' se só restava a marca doutrinária."""
    b = b.strip()
    if b == 'BASE DOUTRINÁRIA (ponto pacífico).': return ''
    b = b.replace('BASE DOUTRINÁRIA (ponto pacífico); ', '').replace('; BASE DOUTRINÁRIA (ponto pacífico)', '').replace('; Anexo N, seção 2.1', '')
    return b

# ------------------------------------------------------------ curso, bloco a bloco
ini = next(i for i, x in enumerate(L) if x.startswith('## 1. (a) CURSO')); fim = next(i for i, x in enumerate(L) if x.startswith('## 2. (b) RESUMO'))
BO, cur = [], None
for ln in L[ini + 1:fim]:
    m = re.match(r'^\*\*(C[\d.]+-\d\d) (.+?)\*\*(.*)$', ln)
    if m and ln.startswith('**C'):
        cur = {'cod': m.group(1), 'titulo': m.group(2), 'corpo': {}}
        BO.append(cur)
    elif cur is not None and ln.startswith('- '):
        for k, p in (('def', '- Definição: '), ('ex', '- Exemplo (Legislativo, hipotético): '), ('peg', '- Pegadinha provável: ')):
            if ln.startswith(p): cur['corpo'][k] = ln[len(p):]
assert len(BO) == 67 and all(set(b['corpo']) == {'def', 'ex', 'peg'} for b in BO)

curso = D['lote']['curso']
secoes = re.split(r'^## ', curso, flags=re.M)[1:]
SAIDA_BLOCOS = []
for s in secoes:
    folha = s.split(' ', 1)[0]
    for p in re.split(r'^### ', s, flags=re.M)[1:]:
        SAIDA_BLOCOS.append((folha, p))
ROT = {'DEFINIÇÃO', 'EXEMPLO PARLAMENTAR', 'PEGADINHA PROVÁVEL'}
reg('### 6.1 Curso: palavras do bloco de saída × bloco de origem (67 blocos de origem; 4 não entram; 63 de saída)')
reg('')
reg('Esperado = título + definição + exemplo + pegadinha do bloco de origem, sem os códigos e rótulos, depois de aplicar, de forma independente do formatador, as passagens e marcas registradas (Anexo N, BASE DOUTRINÁRIA, "[SEM FONTE — não afirmar]" com a frase marcada, "recorte" → "curso", "[Desfeita por: X]" → "Base: X", "O exemplo é hipotético." onde o rótulo era a única qualificação, exemplo "não se aplica" omitido). Obtido = título + texto dos quadros DEFINIÇÃO, EXEMPLO PARLAMENTAR e PEGADINHA PROVÁVEL (sem a lista BASE LEGAL). Critério: sequências de palavras idênticas (maiúsculas e pontuação ignoradas).')
reg('')
ruim = 0; n_saida = 0; blocos_ok = 0
fila = list(SAIDA_BLOCOS)
for b in BO:
    cod = b['cod']
    if cod in DESCARTADOS:
        assert 'SEM FONTE' in b['corpo']['def'] and b['corpo']['ex'].strip() == 'não se aplica.'
        continue
    folha_o = cod[1:].split('-')[0]
    folha_s, p = fila.pop(0)
    t_o = b['titulo']; d, e, g = b['corpo']['def'], b['corpo']['ex'], b['corpo']['peg']
    junto = '\n'.join([t_o, d, e, g])
    for ant, nov in PASSAGENS.get(cod, []):
        assert junto.count(ant) == 1, (cod, ant[:60], junto.count(ant))
        junto = junto.replace(ant, nov)
    t_o, d, e, g = junto.split('\n')
    d, e, g = limpa_geral(d), limpa_geral(e), limpa_geral(g)
    m = re.fullmatch(r'(.*?) \[Desfeita por: (.+)\]', g)
    assert m, cod
    bs = base_limpa(m.group(2))
    g = m.group(1) + (' Base: ' + bs if bs else '')
    if e.strip().rstrip('.') == 'não se aplica': e = ''
    elif 'O exemplo é hipotético' not in e: e = e + ' O exemplo é hipotético.'
    esperado = '\n'.join([t_o, d, e, g])
    linhas = p.split('\n')
    titulo = linhas[0]
    resto, em_base, base, rotulos = [], False, [], []
    for ln in linhas[1:]:
        s_ = ln.strip()
        if s_ in ROT: em_base = False; rotulos.append(s_); continue
        if s_ == 'BASE LEGAL': em_base = True; rotulos.append(s_); continue
        if em_base:
            if s_ == '': em_base = False
            else: base.append(s_)
            continue
        resto.append(re.sub(r'^- ', '', ln))
    obtido = titulo + '\n' + '\n'.join(resto)
    dif = seq_igual(esperado, obtido)
    voc = set(tok('\n'.join([b['titulo'], *b['corpo'].values()])))
    fora = sorted({w for ln in base for w in tok(ln) if w not in voc})
    # quadros presentes: DEFINIÇÃO sempre; EXEMPLO só se há exemplo; BASE LEGAL só se a base tem dispositivo (exceção: ver abaixo)
    esp_rot = ['DEFINIÇÃO'] + (['BASE LEGAL'] if bs else []) + (['EXEMPLO PARLAMENTAR'] if e else []) + ['PEGADINHA PROVÁVEL']
    rot_ok = rotulos == esp_rot
    folha_ok = folha_s == folha_o
    ok = dif is None and not fora and rot_ok and folha_ok
    n_saida += 1
    if ok: blocos_ok += 1
    else:
        ruim += 1
        reg(f'- {cod}: DIFERENÇA {dif}; BASE LEGAL fora do vocabulário do bloco {fora}; quadros {rotulos} (esperado {esp_rot}); folha {folha_s} (esperado {folha_o})')
assert not fila, len(fila)
reg(f'- Blocos conferidos: {n_saida}; sem diferença: {blocos_ok}; com diferença: {ruim}. Blocos de origem que não entram: {sorted(DESCARTADOS)}.')
DEF += ruim
reg('')

# ------------------------------------------------------------ resumo
r1 = next(i for i, x in enumerate(L) if x.startswith('## 2. (b) RESUMO')); r3 = next(i for i in range(r1, len(L)) if L[i] == '---')
orig = '\n'.join(L[r1 + 1:r3])
for ant in ('### 2.1 ', '### 2.2 ', '### 2.3 Item 7 — Improbidade administrativa\n', 'BASE DOUTRINÁRIA: ', ' (BASE DOUTRINÁRIA)', ' do Anexo N |'):
    assert ant in orig, ant
    orig = orig.replace(ant, ' |' if ant.endswith('|') else '')
ant = 'Alterações da v2 no resumo: item 7, "Sistema e dolo" (texto fixado no R1, seção 5.4, letra a; ponto 22) e linha de 40 salários mínimos da tabela (letra b; ponto 22). O resto do resumo é o da v1.'
assert ant in orig; orig = orig.replace(ant, '')
dif = seq_igual(orig, D['lote']['resumo'])
reg('### 6.2 Resumo (seção 2)')
reg('')
reg(f'- Sequência de palavras da origem (menos "2.1/2.2/2.3", o título repetido do item 7, as marcas BASE DOUTRINÁRIA, "do Anexo N" do cabeçalho da tabela e a nota "Alterações da v2 no resumo…") × resumo da saída: ' + ('idênticas.' if dif is None else 'DIFERENÇA ' + dif))
if dif: DEF += 1
reg('')

# ------------------------------------------------------------ pares
ip = next(i for i, x in enumerate(L) if x.startswith('## 3. (c) PARES')); ip2 = next(i for i, x in enumerate(L) if x.startswith('## 4. (d) PEGADINHAS'))
rows = []
for x in L[ip:ip2]:
    if re.match(r'^\| P-\d\d', x):
        rows.append([y.strip() for y in x.strip().strip('|').split('|')])
assert len(rows) == 31 == len(D['lote']['pares'])
reg('### 6.3 Pares (31)')
reg('')
reg('Esperado = Diferença + " Como a banca troca: " + Como a banca troca, sem as marcas BASE DOUTRINÁRIA entre parênteses e sem a frase "Ângulo diferente do mero exercício da função (art. 1º, § 3º)." de P-53; termos a e b reconstituem o campo "Par".')
reg('')
ruim = 0
for r, p in zip(rows, D['lote']['pares']):
    dif_ = r[2].replace(' (BASE DOUTRINÁRIA, ponto pacífico)', '')
    banca = r[4].replace(' Ângulo diferente do mero exercício da função (art. 1º, § 3º).', '')
    esperado = dif_ + ' Como a banca troca: ' + banca
    d1 = seq_igual(esperado, p['como'])
    if d1 or p['a'] + ' × ' + p['b'] != r[1]:
        ruim += 1; reg(f'- {r[0]}: DIFERENÇA {d1}')
reg(f'- Pares com diferença: {ruim}.')
DEF += ruim
reg('')

# ------------------------------------------------------------ pegadinhas
i0 = next(i for i, x in enumerate(L) if x.startswith('## 4. (d) PEGADINHAS')); i1 = next(i for i in range(i0, len(L)) if L[i] == '---')
orig_p = []
for x in L[i0:i1]:
    m = re.match(r'^G-(\d\d)\. \[(C[\d.]+-\d\d)\] (.+)$', x)
    if m: orig_p.append((int(m.group(1)), m.group(2), m.group(3)))
assert len(orig_p) == 71
usadas = [(n, cb, t) for n, cb, t in orig_p if n not in G_DESCARTADAS]
assert len(usadas) == 67 == len(D['lote']['pegadinhas']) and {n for n, _, _ in orig_p} - {n for n, _, _ in usadas} == G_DESCARTADAS
reg('### 6.4 Pegadinhas (67 de 71; G-10, G-22, G-26 e G-32 não entram)')
reg('')
ruim = 0
for (n, cb, t), p in zip(usadas, D['lote']['pegadinhas']):
    t = t.replace(' [acréscimo da v2 (QA PENDENTE (R2))]', '')
    if n == 39: t = t.replace(', ou condicionar sua eficácia a distinções sem fonte', '')
    if n == 69: t = t.replace(' Tema jurisprudencial do ressarcimento: [SEM FONTE — não afirmar].', '')
    claim, sep, disp = t.rpartition(' — Dispositivo: ')
    bs = base_limpa(disp)
    esperado = claim + (' Base: ' + bs if bs else '')
    d1 = seq_igual(esperado, p['texto'])
    eid = 'P1-DA-' + cb[1:].split('-')[0]
    if d1 or p['itemEdital'] != eid:
        ruim += 1; reg(f'- pegadinha {n}: DIFERENÇA {d1}; itemEdital {p["itemEdital"]} (esperado {eid})')
reg(f'- Pegadinhas com diferença na sequência de palavras ou com itemEdital divergente do bloco: {ruim}. (Só "Base:" foi acrescentada, no lugar do rótulo " — Dispositivo: ", e só quando havia dispositivo.)')
DEF += ruim
reg('')

# ------------------------------------------------------------ itens: enunciado, gabarito, justificativa
i51 = next(i for i, x in enumerate(L) if x.startswith('### 5.1')); i52 = next(i for i, x in enumerate(L) if x.startswith('### 5.2')); fim5 = next(i for i, x in enumerate(L) if x.startswith('## 6.'))
enun = {}
for x in L[i51:i52]:
    m = re.match(r'^\*\*(D3-\d\d)\.\*\* (.+)$', x)
    if m: enun[m.group(1)] = m.group(2)
just, gab, folha_i, marcas = {}, {}, {}, {}
cur = None
for x in L[i52:fim5]:
    m = re.match(r'^\*\*(D3-\d\d)\*\* \(folha ([\d.]+)\)', x)
    if m: cur = m.group(1); folha_i[cur] = m.group(2); just[cur] = ['', '']; continue
    if cur and x.startswith('- Justificativa (linha 1): '): just[cur][0] = x[len('- Justificativa (linha 1): '):]
    if cur and x.startswith('- Justificativa (linha 2): '): just[cur][1] = x[len('- Justificativa (linha 2): '):]
    if cur and x.startswith('- Gabarito: '): gab[cur] = x[len('- Gabarito: '):].strip()
    if cur and x.startswith('- Marcas: '): marcas[cur] = x
reg('### 6.5 Itens (71): enunciado, gabarito, itemEdital, justificativa e ordem')
reg('')
ids = [it['id'] for it in D['itens']]
ordem_ok = ids == sorted(ids) and len(ids) == 71 and set(ids) == set(enun) == set(just)
retirados = {f'D3-{n:02d}' for n in (19, 31, 39, 42, 48, 50, 57, 60, 65, 69)}
ids_ok = set(ids) == {f'D3-{n:02d}' for n in range(1, 82)} - retirados
ruim = 0; n_troca = 0
for it in D['itens']:
    i = it['id']
    e_ok = it['enunciado'] == enun[i] and it['gabarito'] == gab[i] and it['itemEdital'] == 'P1-DA-' + folha_i[i]
    o_j = ' '.join(x.strip() for x in just[i])
    if 'troca:' in o_j: n_troca += 1
    dif = seq_igual(o_j, it['justificativa'])
    vol_ok = ('volatil' in it) == ('REVERIFICAR=sim' in marcas[i] or 'VOLÁTIL=sim' in marcas[i])
    if not e_ok or dif or not vol_ok:
        ruim += 1; reg(f'- {i}: enunciado/gabarito/itemEdital ok={e_ok}; justificativa {dif}; volatil coerente={vol_ok}')
reg(f'- Ids em ordem crescente: {ordem_ok}; conjunto = D3-01 a D3-81 sem os 10 retirados: {ids_ok}. Justificativas com a sequência literal "troca:" na origem (pontuação trocada por ";"): {n_troca} (esperado: 2).')
reg(f'- Itens com enunciado, gabarito ou itemEdital diferente do canônico, ou justificativa com palavra acrescentada ou suprimida: {ruim}. (Enunciado e gabarito: iguais caractere a caractere; justificativa: iguais em palavras, só a pontuação de D3-73 e D3-79.)')
if not (ordem_ok and ids_ok and n_troca == 2): ruim += 1
DEF += ruim
reg('')

# ------------------------------------------------------------ tópicos
mapa_txt = {}
for x in MAPA.split('\n'):
    if x.startswith('| art.'):
        c = [y.strip() for y in x.strip().strip('|').split(' | ')]
        mapa_txt[c[1]] = c
secoes_c = {}
for s in secoes:
    secoes_c['P1-DA-' + s.split(' ', 1)[0]] = s
reg('### 6.6 Tópicos (8)')
reg('')
ruim = 0
for k, t in D['topicos'].items():
    cs = secoes_c[k]
    num_curso = set(re.findall(r'\d+', cs))
    textos = list(t['emUmMinuto']) + [t['resumo']]
    for v in t['visuais']:
        if v['tipo'] == 'baseLegal':
            textos.append(v['titulo'] + ' ' + v['norma'] + ' ' + ' '.join(q['ref'] for q in v['dispositivos']))
            for q in v['dispositivos']:
                c = mapa_txt.get(q['texto'])
                if not (c and q['literal'] is True and q['conferido'] == c[4] == '2026-10-20' and 'Vide ADI' not in ' '.join(c) and 'Revogado' not in c[1]):
                    ruim += 1; reg(f'- {k}: baseLegal {q["ref"]} não bate letra a letra com uma linha do mapa (ou data, ou nota de ADI, ou revogado)')
                art = re.search(r'art\. (\d+)', q['ref']).group(1)
                if not re.search(r'\bart(?:s)?\. ' + art + r'(?!\d)', cs, re.I):
                    ruim += 1; reg(f'- {k}: baseLegal {q["ref"]}: artigo não citado no curso da folha')
        else:
            textos.append(json.dumps(v, ensure_ascii=False))
    todo = ' '.join(textos)
    nums = set(re.findall(r'\d+', todo))
    fora = sorted(nums - num_curso, key=int)
    if fora:
        ruim += 1; reg(f'- {k}: números que não aparecem no curso da folha: {fora}')
    # artigos citados nos textos têm de constar do curso da folha
    for a in set(re.findall(r'\bart(?:s)?\. (\d+(?:-[A-Z])?)', todo)):
        if not re.search(r'\bart(?:s)?\. (?:[^.;:]*?\b)?' + re.escape(a) + r'(?![\dº-])|\b' + re.escape(a) + r'º', cs):
            ruim += 1; reg(f'- {k}: artigo {a} citado no tópico e ausente do curso da folha')
    # vocabulário: toda palavra do resumo e do "em um minuto" deve existir no curso da folha ou numa lista curta de palavras de ligação
    voc = set(tok(cs))
    LIGACAO = set(tok('a o as os e ou de do da dos das em no na nos nas por pela pelo para com sem se que como mas um uma é são ao aos à às sua seu suas seus nem já também só mais entre sobre até quando nessa nesse esse essa cada outro outra isso ele ela eles elas lhe quem qual quais onde ser sendo foi ter há não'))
    # palavras novas são listadas (revisão humana); nenhuma é defeito por si
    novas = sorted({w for w in tok(' '.join(t['emUmMinuto']) + ' ' + t['resumo']) if w not in voc and w not in LIGACAO and not w.isdigit()})
    reg(f'- {k}: palavras de emUmMinuto e resumo que não aparecem no curso da folha (para revisão; não são defeito por si): {novas}')
    n = len(t['resumo'].split())
    if not 150 <= n <= 250 or len(t['emUmMinuto']) != 3 or any(len(x) > 210 for x in t['emUmMinuto']):
        ruim += 1; reg(f'- {k}: resumo com {n} palavras ou emUmMinuto fora do formato')
reg(f'- Problemas nos tópicos (número ausente do curso da folha; artigo ausente do curso; dispositivo de baseLegal que não bate letra a letra com o mapa, sem data 2026-10-20, com nota de ADI ou revogado; tamanhos): {ruim}.')
DEF += ruim
reg('')
reg(f'RESULTADO DA CONFERÊNCIA DE FIDELIDADE: {DEF} defeito(s).')
print('\n'.join(SAIDA))
sys.exit(1 if DEF else 0)
