# conferir_fidelidade_D5.py — T-74 (ordem DA 20/10/2026) — 2026-10-20 — gerado por gcb-cpp
# Conferência própria de fidelidade: compara as palavras do texto de saída (D5_plataforma.json) com as do texto de
# origem (saida/gcb/D5_v2_1.md), depois de remover as passagens e marcas registradas (lista INDEPENDENTE da usada no
# formatador). Palavra acrescentada ou suprimida fora das trocas registradas = defeito.
# Confere também os tópicos (números e dispositivos no curso da folha; baseLegal letra a letra no mapa normativo).
# Uso: python3 -I saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D5.py
import collections, difflib, json, pathlib, re, sys

RAIZ = pathlib.Path(__file__).resolve().parents[4]
L = (RAIZ / 'saida/gcb/D5_v2_1.md').read_text(encoding='utf-8').split('\n')
D = json.loads((RAIZ / 'saida/gcb/DA_plataforma/D5_plataforma.json').read_text(encoding='utf-8'))
MAPA = (RAIZ / 'saida/gcb/D5_anexo_N_mapa_normativo.md').read_text(encoding='utf-8')

# passagens e marcas que a seção 6/7 da especificação manda tirar (removidas da origem antes de comparar)
REMOVIDOS = [
 ' (nota do Anexo N, seção 7, item 11)',
 '; aqui, os cobrados no lote',
 '; os valores atualizados em vigor em 2/10/2026 estão NÃO CONFERIDOS no Anexo N: [SEM FONTE — não afirmar]',
 '; os valores vigentes em 2/10/2026 estão NÃO CONFERIDOS no Anexo N: [SEM FONTE — não afirmar]',
 'REVERIFICAR: ',
 ' Nenhum item deste lote se apoia nesse inciso.',
 '; afirmar valor atualizado sem conferência',
 ' e não é desenvolvido neste lote (ver o registro de acatamento, seção 0.1)',
 ' O art. 79, que trata das hipóteses de uso do credenciamento, tem o inciso IV, o § 1º (caput e inciso VII, com as alíneas) e o § 2º com redação dada ou incluída pela Lei 15.266/2025, marcados REVERIFICAR no Anexo N; o artigo não é usado neste lote.',
 ' (O inciso I e o § 1º, fornecedor exclusivo e documento idôneo, são ponto do item real BQ-0113 e não são repetidos em item; o inciso III e o § 4º estão em C10.1-07.)',
 ' (usados em C10.1-08)',
 '; valor atualizado NÃO CONFERIDO no Anexo N: [SEM FONTE — não afirmar]',
 '; valor atualizado NÃO CONFERIDO no Anexo N',
 ' Qualquer afirmação sobre atribuições do gestor vem de regulamento não aberto neste Anexo: [SEM FONTE — não afirmar].',
 ' (A regra e a ressalva do art. 121, §§ 1º e 2º, estão em C10.4-03.)',
 ' (O recebimento provisório e definitivo, a rejeição do objeto e a responsabilidade pela solidez e segurança estão em C10.4-04.)',
 ' (O planejamento de compras está em C10.5-04.)',
 ', que já é objeto de item real do banco (BQ-0134) e não é repetido neste lote',
 ' (ponto do item real BQ-0135, não repetido)',
 ' Este é o ponto do item real BQ-0134, que não é repetido em item deste lote; entra no curso e nas pegadinhas para completar o quadro das atribuições do fiscal (§ 1º em C10.6-02, § 3º em C10.6-03, § 4º em C10.6-04).',
 ' (Requisitos da contratação e parcelamento, incisos III e VIII, são o ponto do item real BQ-0142.)',
 '; qualquer afirmação além da letra desses dispositivos fica fora do lote',
 ' (O § 2º é o ponto do item real BQ-0134; este par não gera item.)',
 '; atribuições do gestor: [SEM FONTE — não afirmar]',
 '; só no curso, no par P-27 e na pegadinha G-71, sem item',
 'Acrescentado na v2: ',
 ' do Anexo N |',        # cabeçalho da tabela do resumo: "Número literal do Anexo N |"
 ' [alterada na v2]',
 ' [acréscimo da v2]',
]
REMOVIDOS.sort(key=len, reverse=True)
SUFIXOS = [re.compile(r' — acréscimo da v2 \(leitura externa [^()]*; QA PENDENTE \(R2\)\)'), re.compile(r' \[alterado na v2: [^\]]*\]')]

# errata de forma de 20/10/2026 (achado 1): remissão "folha" -> "subitem" (trocas, não remoções)
TROCAS_ERRATA = [('estão na folha 10.6.', 'estão no subitem 10.6.'), ('estão na folha 10.7.)', 'estão no subitem 10.7.)'), ('está na folha 10.7.)', 'está no subitem 10.7.)')]

def tira(t):
    for r in REMOVIDOS:
        t = t.replace(r, ' |' if r.endswith('|') else ' ')
    for a, b in TROCAS_ERRATA:
        t = t.replace(a, b)
    return t

def tok(t):
    return re.findall(r'[^\W_]+', t.lower())

def compara(origem, saida, permitido=()):
    co, cs = collections.Counter(tok(origem)), collections.Counter(tok(saida))
    add = cs - co
    falta = co - cs
    add_ruim = {w: n for w, n in add.items() if w not in permitido}
    ops = [op for op in difflib.SequenceMatcher(None, tok(origem), tok(saida), autojunk=False).get_opcodes() if op[0] != 'equal']
    return add, add_ruim, falta, ops

SAIDA, DEF = [], 0
def reg(m): SAIDA.append(m)

# ------------------------------------------------------------ curso, bloco a bloco
ini = next(i for i, x in enumerate(L) if x.startswith('## 1. (a) CURSO')); fim = next(i for i, x in enumerate(L) if x.startswith('## 2. (b) RESUMO'))
BO, cur = [], None
for ln in L[ini + 1:fim]:
    m = re.match(r'^\*\*(C10\.(\d)-\d\d) (.+?)\*\*(.*)$', ln)
    if m:
        t = m.group(3)
        cur = {'cod': m.group(1), 'folha': '10.' + m.group(2), 'titulo': t, 'corpo': []}
        BO.append(cur)
    elif cur is not None and ln.startswith('- '):
        cur['corpo'].append(ln)
assert len(BO) == 58, len(BO)

curso = D['lote']['curso']
secoes = re.split(r'^## ', curso, flags=re.M)[1:]
SAIDA_BLOCOS = []
for s in secoes:
    folha = s.split(' ', 1)[0]
    for p in re.split(r'^### ', s, flags=re.M)[1:]:
        SAIDA_BLOCOS.append((folha, p))
assert len(SAIDA_BLOCOS) == 58, len(SAIDA_BLOCOS)

ROT = {'DEFINIÇÃO', 'EXEMPLO PARLAMENTAR', 'PEGADINHA PROVÁVEL'}
reg('### 6.1 Curso: palavras do bloco de saída × bloco de origem (58 blocos)')
reg('')
reg('Origem = título (sem o código C10.x-NN e sem a marca de versão) + definição + exemplo + pegadinha, sem os rótulos "Definição:", "Exemplo (Legislativo, hipotético):", "Pegadinha provável:", "[Desfeita por:" e sem as passagens registradas. Saída = título + texto dos três quadros, sem os rótulos de quadro e sem a lista BASE LEGAL. Contagem de palavras por multiconjunto (maiúsculas ignoradas) e por sequência (difflib). Única palavra acrescentada permitida: "Base" (no lugar de "[Desfeita por:").')
reg('')
tot_add = tot_falta = 0
for b, (folha, p) in zip(BO, SAIDA_BLOCOS):
    assert folha == b['folha'], (b['cod'], folha)
    titulo_o = b['titulo']
    corpo = '\n'.join(b['corpo'])
    corpo = corpo.replace('- Definição: ', '').replace('- Exemplo (Legislativo, hipotético): ', '').replace('- Pegadinha provável: ', '').replace('[Desfeita por: ', ' ')
    corpo = re.sub(r'\]\s*$', '', corpo, flags=re.M)
    origem = tira(titulo_o + '\n' + corpo)
    linhas = p.split('\n')
    titulo = linhas[0]
    resto, em_base, base = [], False, []
    for ln in linhas[1:]:
        s = ln.strip()
        if s in ROT: em_base = False; continue
        if s == 'BASE LEGAL': em_base = True; continue
        if em_base:
            if s == '': em_base = False
            else: base.append(s)
            continue
        resto.append(re.sub(r'^- ', '', ln))
    saida = titulo + '\n' + '\n'.join(resto)
    add, add_ruim, falta, ops = compara(origem, saida, permitido={'base'})
    voc = set(tok(origem))
    fora = sorted({w for ln in base for w in tok(ln) if w not in voc})
    nbase = add.get('base', 0)
    ok = not add_ruim and not falta and nbase == 1 and len(ops) == 1 and not fora
    if not ok: DEF += 1
    tot_add += sum(add_ruim.values()); tot_falta += sum(falta.values())
    reg(f'- {b["cod"]}: palavras acrescentadas fora de "Base" {sum(add_ruim.values())}; "Base" acrescentada {nbase}; suprimidas {sum(falta.values())}; operações de inserção/troca/remoção na sequência {len(ops)}; palavras de BASE LEGAL fora do vocabulário do bloco {len(fora)}' + ('' if ok else f' — ACRESCENTADAS {add_ruim}; SUPRIMIDAS {dict(falta)}; OPS {ops[:3]}; FORA {fora}'))
reg('')
reg(f'Total curso: palavras acrescentadas (fora de "Base") {tot_add}; suprimidas {tot_falta}; blocos com divergência {DEF}.')
reg('')

# ------------------------------------------------------------ resumo
r1 = next(i for i, x in enumerate(L) if x.startswith('## 2. (b) RESUMO')); r3 = next(i for i in range(r1, len(L)) if L[i] == '---')
orig = tira('\n'.join(x for x in L[r1 + 1:r3] if x.strip()))
add, add_ruim, falta, ops = compara(orig, D['lote']['resumo'])
reg('### 6.2 Resumo (seção 2)')
reg('')
reg(f'- Acrescentadas {dict(add)}; suprimidas {dict(falta)}; operações na sequência {len(ops)}. Esperado: nenhuma (só deleções registradas; a letra minúscula após "Acrescentado na v2:" passa a maiúscula, o que não muda a palavra).')
if add or falta or ops: DEF += 1
reg('')

# ------------------------------------------------------------ pares
ip = next(i for i, x in enumerate(L) if x.startswith('## 3. (c) PARES')); ip2 = next(i for i, x in enumerate(L) if x.startswith('## 4. (d) PEGADINHAS'))
rows = []
for x in L[ip:ip2]:
    if re.match(r'^\| P-\d\d', x):
        c = [y.strip() for y in x.strip().strip('|').split('|')]
        rows.append(c)
assert len(rows) == 31 == len(D['lote']['pares'])
reg('### 6.3 Pares (31)')
reg('')
reg('Origem = campos "Par", "Diferença" e "Como a banca troca" (sem as passagens registradas); saída = a + b + como. Palavras permitidas por construção: as do rótulo " Como a banca troca: " da especificação.')
reg('')
ruim = 0
for r, p in zip(rows, D['lote']['pares']):
    origem = tira(' '.join([r[1], r[2], r[4]]))
    co, cs = collections.Counter(tok(origem)), collections.Counter(tok(' '.join([p['a'], p['b'], p['como']])))
    rot = collections.Counter(tok('Como a banca troca'))
    add, falta = (cs - co) - rot, co - cs
    # o rótulo é acrescentado uma única vez: cs deve conter as palavras do rótulo além das da origem
    if add or falta or ((cs - co) & rot) != rot or ' × '.join([p['a'], p['b']]) != r[1]:
        ruim += 1; reg(f'- {r[0]}: ACRESCENTADAS {dict(add)}; SUPRIMIDAS {dict(falta)}')
reg(f'- Pares com palavra acrescentada fora do rótulo permitido, ou suprimida: {ruim}. Termos a/b reconstituem o campo "Par" (a + " × " + b).')
DEF += ruim
reg('')

# ------------------------------------------------------------ pegadinhas
i0 = next(i for i, x in enumerate(L) if x.startswith('## 4. (d) PEGADINHAS')); i1 = next(i for i in range(i0, len(L)) if L[i] == '---')
orig_p = []
for x in L[i0:i1]:
    m = re.match(r'^G-(\d\d)\. \[(C10\.\d-\d\d)\] (.+)$', x)
    if m: orig_p.append((m.group(1), m.group(2), m.group(3).replace(' — Dispositivo: ', ' ')))
assert len(orig_p) == 73 == len(D['lote']['pegadinhas'])
reg('### 6.4 Pegadinhas (73)')
reg('')
ruim = 0
for (n, cb, o), p in zip(orig_p, D['lote']['pegadinhas']):
    add, add_ruim, falta, ops = compara(tira(o), p['texto'], permitido={'base'})
    if add_ruim or falta or add.get('base', 0) != 1 or p['itemEdital'] != 'P1-DA-10.' + cb[4]:
        ruim += 1; reg(f'- pegadinha {int(n)}: ACRESCENTADAS {add_ruim}; SUPRIMIDAS {dict(falta)}; itemEdital {p["itemEdital"]}')
reg(f'- Pegadinhas com palavra acrescentada além de "Base", ou suprimida, ou com itemEdital divergente do bloco: {ruim}. (Só "Base:" foi acrescentada, no lugar do rótulo " — Dispositivo: ".)')
DEF += ruim
reg('')

# ------------------------------------------------------------ itens: enunciado, gabarito, justificativa
i51 = next(i for i, x in enumerate(L) if x.startswith('### 5.1')); i52 = next(i for i, x in enumerate(L) if x.startswith('### 5.2')); fim5 = next(i for i, x in enumerate(L) if x.startswith('## 6.'))
enun = {}
for x in L[i51:i52]:
    m = re.match(r'^\*\*(D5-\d\d)\.\*\* (.+)$', x)
    if m: enun[m.group(1)] = m.group(2)
just, gab, folha_i = {}, {}, {}
cur = None
for x in L[i52:fim5]:
    m = re.match(r'^\*\*(D5-\d\d)\*\* \(folha (10\.\d)\)', x)
    if m: cur = m.group(1); folha_i[cur] = m.group(2); just[cur] = ['', '']; continue
    if cur and x.startswith('- Justificativa (linha 1): '): just[cur][0] = x[len('- Justificativa (linha 1): '):]
    if cur and x.startswith('- Justificativa (linha 2): '): just[cur][1] = x[len('- Justificativa (linha 2): '):]
    if cur and x.startswith('- Gabarito: '): gab[cur] = x[len('- Gabarito: '):].strip()
reg('### 6.5 Itens (70): enunciado, gabarito, itemEdital e justificativa')
reg('')
ruim = 0; tot = collections.Counter(); n_isca = 0
for it in D['itens']:
    i = it['id']
    e_ok = it['enunciado'] == enun[i] and it['gabarito'] == gab[i] and it['itemEdital'] == 'P1-DA-' + folha_i[i]
    o_j = ' '.join(just[i])
    n_isca += o_j.count('elemento-isca')
    o_j = o_j.replace('elemento-isca', 'elemento que parece trocado')   # troca mínima registrada (op. 6)
    add, add_ruim, falta, ops = compara(o_j, it['justificativa'])
    tot.update(add)
    if not e_ok or add or falta or ops:
        ruim += 1; reg(f'- {i}: enunciado/gabarito/itemEdital ok={e_ok}; justificativa ACRESCENTADAS {dict(add)} SUPRIMIDAS {dict(falta)}')
reg(f'- Trocas mínimas "elemento-isca" → "elemento que parece trocado" nas justificativas de origem: {n_isca} (esperado: 7).')
if n_isca != 7: DEF += 1
reg(f'- Itens com enunciado, gabarito ou itemEdital diferente do canônico, ou justificativa com palavra acrescentada ou suprimida: {ruim}. (Enunciado e gabarito: iguais caractere a caractere; justificativa: a pontuação de D5-04, que não altera palavra, e a troca registrada de "elemento-isca".)')
DEF += ruim
reg('')

# ------------------------------------------------------------ tópicos
mapa_txt, mapa_data = {}, {}
for x in MAPA.split('\n'):
    if x.startswith('| art.'):
        c = [y.strip() for y in x.strip().strip('|').split(' | ')]
        mapa_txt[c[1]] = c;
secoes_c = {}
for s in secoes:
    secoes_c['P1-DA-' + s.split(' ', 1)[0]] = s
reg('### 6.6 Tópicos (7)')
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
                if not (c and q['literal'] is True and q['conferido'] == c[4] == '2026-10-18' and c[2] == 'redação original'):
                    ruim += 1; reg(f'- {k}: baseLegal {q["ref"]} não bate letra a letra com uma linha do mapa (ou data/redação)')
                art = re.match(r'art\. (\d+)', q['ref']).group(1)
                if not re.search(r'\bart(?:s)?\. ' + art + r'(?!\d)', cs, re.I):
                    ruim += 1; reg(f'- {k}: baseLegal {q["ref"]}: artigo não citado no curso da folha')
        else:
            textos.append(json.dumps(v, ensure_ascii=False))
    nums = set(re.findall(r'\d+', ' '.join(textos)))
    fora = sorted(nums - num_curso, key=int)
    if fora:
        ruim += 1; reg(f'- {k}: números que não aparecem no curso da folha: {fora}')
reg(f'- Problemas nos tópicos (número ausente do curso da folha; dispositivo de baseLegal que não bate letra a letra com o mapa, sem data 2026-10-18 ou fora do curso): {ruim}.')
DEF += ruim
reg('')
reg(f'RESULTADO DA CONFERÊNCIA DE FIDELIDADE: {DEF} defeito(s).')
print('\n'.join(SAIDA))
sys.exit(1 if DEF else 0)
