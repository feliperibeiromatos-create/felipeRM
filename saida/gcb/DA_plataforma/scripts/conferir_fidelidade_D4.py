# conferir_fidelidade_D4.py — T-77 (ordem DA 20/10/2026) — 2026-10-20 — gerado por gcb-cpp
# Conferência própria de fidelidade do Lote D4: compara as palavras do texto de saída (D4_plataforma.json) com as do texto
# de origem (saida/gcb/D4_v2_1.md). Método independente do formatador (que edita por trocas de texto): aqui as duas
# sequências de palavras são alinhadas (difflib) e cada diferença é classificada:
#   - supressão: só vale se a frase de origem que a contém traz uma marca de produção (SEM FONTE, Anexo N, ficha, BQ-, código de
#     bloco, "lote", "item real", R-id, F-id...) — as passagens tiradas pela seção 6;
#   - acréscimo ou troca: só vale com palavras do vocabulário de identificação das publicações (colunas da seção 5 do Anexo N)
#     e com os conectivos mínimos ("o trecho", "o artigo", "mesmo", "curso"), mais "Base" no lugar de "Desfeita por";
#   - códigos R1…R31 e F1…F22 desaparecem da origem antes do alinhamento e não podem reaparecer na saída.
# Confere ainda: itens (enunciado e gabarito idênticos ao canônico), quadros BASE LEGAL (dispositivos citados no bloco, artigos
# revogados sem letra, linhas "Fonte:" contra a seção 5 do Anexo N) e tópicos (números e dispositivos no curso da folha;
# baseLegal letra a letra no mapa, data de consulta, sem artigo revogado).
# Uso: python3 -I saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D4.py
import collections, difflib, json, pathlib, re, sys

RAIZ = pathlib.Path(__file__).resolve().parents[4]
L = (RAIZ / 'saida/gcb/D4_v2_1.md').read_text(encoding='utf-8').split('\n')
D = json.loads((RAIZ / 'saida/gcb/DA_plataforma/D4_plataforma.json').read_text(encoding='utf-8'))
MAPA = (RAIZ / 'saida/gcb/D4_anexo_N_mapa_normativo.md').read_text(encoding='utf-8')

SAIDA, DEF = [], 0
def reg(m): SAIDA.append(m)

# ---------------------------------------------------------------- referencial (seção 5 do Anexo N)
REF = {}
for x in MAPA.split('\n'):
    m = re.match(r'^\| (R\d+) \| ', x)
    if m:
        c = [y.strip() for y in x.strip().strip('|').split(' | ')]
        REF[m.group(1)] = c[3]       # "F4: ENAP, RSP 73 (Especial 85 Anos), 2022 (orig. 1996), Bresser-Pereira, p. 58"
assert len(REF) == 31, len(REF)

def tok(t): return re.findall(r'[^\W_]+', t.lower())

# vocabulário de identificação das publicações: colunas "Publicação, órgão, ano, página" da seção 5 + o título por extenso
VOC = set()
for v in REF.values(): VOC |= set(tok(v))
VOC |= set(tok('ENAP Revista do Serviço Público Boletim de Análise Político-Institucional Reformas do Estado no Brasil Diálogos para uma PNDU '
               'capítulo de Lui et al Bresser-Pereira Bouckaert Cavalcante Martins Ipea Casa Civil da Presidência da República Guia da Política de '
               'Governança Pública Avaliação de Políticas Públicas guia prático de análise ex post Tribunal Referencial Básico de Governança '
               'Organizacional TCU CGU Controladoria-Geral da União documento didático Cadeia de valor da CGU arquivo PDF sem numeração impressa '
               'edição ed volume v. n. pp. p.'))
CONECT = set(tok('o a os as de do da dos das em no na nos nas ao pelo pela e trecho texto artigo mesmo curso documento análise capítulo guia publicação obra nota'))
CONECT |= set(tok('neste subitem subitens'))   # errata de forma de 20/10/2026 (achado 1): "folha" -> "subitem"
BASE = {'base'}
RX_PAG = re.compile(r'^(?:p|pp)\.\s')

MARCA = re.compile(r'\b[Ff]olhas?\b|SEM FONTE|não afirmar|Anexo N|\bficha\b|BQ-\d|\bC\d\.\d-\d\d|\blote\b|item real|\bR\d{1,2}\b|\bF\d{1,2}\b|bloqueado|\bv[12]\b|QA PENDENTE|\bG-\d\d|\bP-\d\d|REVERIFICAR|Desfeita por|Dispositivo ou trecho|\bD6\b|\bN9\b|acréscimo|leitura externa|\bTS\b|\[TS\]|inapto|\(subitem|decisão|banca de produção|só curso|só no curso', re.I)

def toks_spans(t):
    out = []
    for m in re.finditer(r'[^\W_]+', t):
        w = m.group(0).lower()
        if re.fullmatch(r'[rf]\d{1,2}', w): continue          # R-id e F-id saem da origem antes do alinhamento
        out.append((w, m.start(), m.end()))
    return out

def contexto(t, a, b):
    """Frase da origem que contém o trecho [a, b): do fim da frase anterior ao fim da própria."""
    i = max(t.rfind('. ', 0, a), t.rfind('] ', 0, a), t.rfind('\n', 0, a))
    j = min([k for k in (t.find('. ', b), t.find('\n', b)) if k != -1] or [len(t)])
    return t[(i + 1 if i != -1 else 0):j + 1]

def alinha(origem, saida, extra=frozenset(), onde=''):
    """Devolve a lista de problemas (vazia = fiel) e contagens."""
    to = toks_spans(origem); ts = tok(saida)
    wo = [w for w, _, _ in to]
    sm = difflib.SequenceMatcher(None, wo, ts, autojunk=False)
    prob, n_del, n_ins, n_rep = [], 0, 0, 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal': continue
        antigo = wo[i1:i2]; novo = ts[j1:j2]
        ctx = contexto(origem, to[i1][1], to[i2 - 1][2]) if antigo else ''
        if tag == 'delete':
            n_del += 1
            if not MARCA.search(ctx): prob.append(f'supressão sem marca de produção: {" ".join(antigo)!r} em «{ctx.strip()[:120]}»')
        else:
            if tag == 'insert': n_ins += 1
            else:
                n_rep += 1
                if not MARCA.search(ctx) and set(antigo) - {'lote'}: prob.append(f'troca sem marca de produção: {" ".join(antigo)!r} → {" ".join(novo)!r}')
            fora = [w for w in novo if w not in VOC and w not in CONECT and w not in extra and not w.isdigit()]
            if fora: prob.append(f'palavras acrescentadas fora do vocabulário de identificação: {fora}')
    return prob, (n_del, n_ins, n_rep)

# ---------------------------------------------------------------- curso: origem
ini = next(i for i, x in enumerate(L) if x.startswith('## 1. (a) CURSO')); fim = next(i for i, x in enumerate(L) if x.startswith('## 2. (b) RESUMO'))
BO, cur = [], None
for ln in L[ini + 1:fim]:
    m = re.match(r'^\*\*(C(\d)\.(\d)-\d\d) (.+?)\*\*(.*)$', ln)
    if m:
        cod = m.group(1)
        folha = '8' if cod.startswith('C8.0-') else f'{m.group(2)}.{m.group(3)}'
        cur = {'cod': cod, 'folha': folha, 'titulo': m.group(4) + m.group(5), 'corpo': []}
        BO.append(cur)
    elif cur is not None and ln.startswith('- '):
        cur['corpo'].append(ln)
assert len(BO) == 62, len(BO)

curso = D['lote']['curso']
secoes = re.split(r'^## ', curso, flags=re.M)[1:]
SAIDA_BLOCOS = []
for s in secoes:
    folha = s.split(' ', 1)[0]
    for p in re.split(r'^### ', s, flags=re.M)[1:]:
        SAIDA_BLOCOS.append((folha, p))
assert len(SAIDA_BLOCOS) == 62, len(SAIDA_BLOCOS)
ROT = {'DEFINIÇÃO', 'EXEMPLO PARLAMENTAR', 'PEGADINHA PROVÁVEL'}
# exceções documentadas no registro: palavras acrescentadas por troca de uma Base que só citava o Anexo N; remissões de R-id retiradas por supérfluas
EXTRA_BLOCO = {'C8.4-05': {'decreto', 'art', '2º', 'ii'}}
SEM_FONTE_OK = {'C8.2-02': {'R7'}, 'C9.4-07': {'R27'}}

# artigos do Decreto 9.203 revogados (só com letra valem): 7 a 15 e 20
RX_REVOGADO = re.compile(r'(?<![\dº-])(?:7|8|9|10|11|12|13|14|15|20)º?(?!-[A-Z]|\d)')

reg('### 6.1 Curso: palavras do bloco de saída × bloco de origem (62 blocos)')
reg('')
reg('Origem = título + definição + exemplo + pegadinha do bloco, com os rótulos "Definição:", "Exemplo (Legislativo, hipotético):", "Pegadinha provável:" e "[Desfeita por:" mantidos na origem (o alinhamento os classifica), e com os códigos R1 a R31 e F1 a F22 retirados. Saída = título + texto dos três quadros, sem os rótulos de quadro e sem a lista BASE LEGAL. Cada diferença é supressão (só frase com marca de produção) ou acréscimo (só vocabulário de identificação das publicações, conectivos mínimos e "Base").')
reg('')
tot = collections.Counter(); ruim_curso = 0
for b, (folha, p) in zip(BO, SAIDA_BLOCOS):
    assert folha == b['folha'], (b['cod'], folha, b['folha'])
    corpo = '\n'.join(b['corpo'])
    corpo = corpo.replace('- Definição: ', '').replace('- Exemplo (Legislativo, hipotético): ', '').replace('- Pegadinha provável: ', '')
    origem = b['titulo'] + '\n' + corpo
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
    prob, (nd, ni, nr) = alinha(origem, saida, extra=BASE | {'8', '1'} | EXTRA_BLOCO.get(b['cod'], set()), onde=b['cod'])
    tot.update(dict(supressoes=nd, insercoes=ni, trocas=nr))
    # código, R-id e marca de produção não podem estar na saída
    if re.search(r'\bR\d{1,2}\b|\bF\d{1,2}\b|\bC\d\.\d-\d\d|Anexo N|SEM FONTE|\blote\b|\bficha\b|BQ-\d|QA PENDENTE|\bv[12]\b', saida):
        prob.append('resta código ou marca de produção na saída: ' + re.search(r'\bR\d{1,2}\b|\bF\d{1,2}\b|\bC\d\.\d-\d\d|Anexo N|SEM FONTE|\blote\b|\bficha\b|BQ-\d|QA PENDENTE|\bv[12]\b', saida).group(0))
    # "Base" aparece uma vez, na pegadinha
    if len(re.findall(r'\bBase: ', saida)) != 1: prob.append('"Base:" não aparece exatamente uma vez')
    # BASE LEGAL
    nfonte = 0
    cit_orig = set('R' + n for n in re.findall(r'\bR(\d{1,2})\b', origem))
    pares_saida = set()
    for ln in base:
        t = re.sub(r'^- ', '', ln)
        if t.startswith('Fonte: '):
            nfonte += 1
            m = re.search(r', (pp?)\. (.+)$', t)
            if not m: prob.append(f'linha Fonte sem página: {t}'); continue
            pgs = [x.strip() for x in m.group(2).split(',')] if m.group(1) == 'pp' else [m.group(2).strip()]
            for pg in pgs:
                pgn = re.match(r'\d+(?:-\d+)?', pg).group(0)
                achou = [r for r in sorted(cit_orig, key=lambda z: int(z[1:])) if re.search(r', p\. ' + re.escape(pgn) + r'(?:\s|$)', REF[r])]
                ok = False
                for r in achou:
                    org = REF[r].split(': ', 1)[1].split(',')[0].split('/')[0].strip().lower()
                    ano = re.search(r'\b(19|20)\d\d\b', REF[r])
                    if org in t.lower() and (ano is None or ano.group(0) in t):
                        ok = True; pares_saida.add(r)
                if not ok: prob.append(f'linha Fonte «{t}»: p. {pg} não corresponde a nenhum R-id citado pelo bloco na seção 5 do Anexo N')
        else:
            # dispositivo: leis e artigos citados no texto do bloco; sem artigo revogado
            lei = re.match(r'(Decreto|Lei) ([\d.]+)', t)
            if not lei: prob.append(f'dispositivo sem norma: {t}'); continue
            if lei.group(2) not in saida: prob.append(f'dispositivo {t}: norma {lei.group(2)} não aparece no texto do bloco')
            resto_t = t.split(', art', 1)[1] if ', art' in t else ''
            # números de artigo do dispositivo: os que vêm antes da primeira vírgula depois de "art(s)." (a lista "7º-A, 8º-A, ..." é tratada à parte)
            lista = re.sub(r'^s?\. ?', '', resto_t)
            if 'arts' in t.split(', ', 1)[1][:6]:
                arts = re.findall(r'\d+º?(?:-[A-Z])?', re.split(r' \(|, §|, caput', lista)[0])
            else:
                arts = re.findall(r'\d+º?(?:-[A-Z])?', lista.split(',')[0])[:1]
            for a in arts:
                if a not in saida: prob.append(f'dispositivo {t}: «{a}» não aparece no texto do bloco')
                if lei.group(2) == '9.203/2017':
                    m = re.fullmatch(r'(\d+)º?(-[A-Z])?', a)
                    if m and not m.group(2) and (7 <= int(m.group(1)) <= 15 or int(m.group(1)) == 20):
                        prob.append(f'dispositivo {t}: artigo revogado sem letra')
    faltam = {r for r in cit_orig if r not in pares_saida} - SEM_FONTE_OK.get(b['cod'], set())
    # R-ids que o bloco só citava dentro de passagem tirada (SEM FONTE/Anexo N) podem não ter linha Fonte; qualquer outro falta
    if faltam:
        so_removido = set()
        for r in faltam:
            tem = False
            for ln in (origem.split('\n')):
                for frase in re.split(r'(?<=[.\]])\s+', ln):
                    if re.search(r'\b' + r + r'\b', frase) and not MARCA.search(re.sub(r'\bR\d{1,2}\b', '', frase)):
                        tem = True
            if not tem: so_removido.add(r)
        resto_f = faltam - so_removido
        # R-ids de mesma publicação e mesma página já representados por outro R-id
        resto_f = {r for r in resto_f if not any(REF[r].split(', p. ')[0] == REF[q].split(', p. ')[0] and REF[r].split(', p. ')[1] == REF[q].split(', p. ')[1] for q in pares_saida)}
        if resto_f: prob.append(f'R-ids citados no bloco sem linha Fonte no quadro BASE LEGAL: {sorted(resto_f, key=lambda z: int(z[1:]))}')
    if prob: ruim_curso += 1
    reg(f'- {b["cod"]}: supressões {nd}; acréscimos {ni}; trocas {nr}; linhas Fonte {nfonte}' + ('' if not prob else ' — DEFEITOS: ' + ' | '.join(prob)))
reg('')
reg(f'Total curso: supressões {tot["supressoes"]}; acréscimos {tot["insercoes"]}; trocas {tot["trocas"]}; blocos com defeito {ruim_curso}.')
DEF += ruim_curso
reg('')

# ---------------------------------------------------------------- resumo
r1 = next(i for i, x in enumerate(L) if x.startswith('## 2. (b) RESUMO')); r3 = next(i for i in range(r1, len(L)) if L[i] == '---')
orig = '\n'.join(x for x in L[r1 + 1:r3] if x.strip())
prob, (nd, ni, nr) = alinha(orig, D['lote']['resumo'], extra={'8', '1'})
if re.search(r'\bR\d{1,2}\b|\bF\d{1,2}\b|Anexo N|SEM FONTE', D['lote']['resumo']): prob.append('resta código ou marca de produção')
reg('### 6.2 Resumo (seção 2)')
reg('')
reg(f'- Supressões {nd}; acréscimos {ni}; trocas {nr}.' + ('' if not prob else ' DEFEITOS: ' + ' | '.join(prob)))
if prob: DEF += 1
reg('')

# ---------------------------------------------------------------- pares
ip = next(i for i, x in enumerate(L) if x.startswith('## 3. (c) PARES')); ip2 = next(i for i, x in enumerate(L) if x.startswith('## 4. (d) PEGADINHAS'))
rows = []
for x in L[ip:ip2]:
    if re.match(r'^\| P-\d\d', x):
        rows.append([y.strip() for y in x.strip().strip('|').split('|')])
assert len(rows) == 24 == len(D['lote']['pares']), (len(rows), len(D['lote']['pares']))
reg('### 6.3 Pares (24)')
reg('')
reg('Origem = campos "Par", "Diferença" e "Como a banca troca" (a coluna "Base de cada lado" não entra); saída = a + b + como. Palavras acrescentadas permitidas: as do rótulo " Como a banca troca: ".')
reg('')
ruim = 0
for r, p in zip(rows, D['lote']['pares']):
    origem = ' '.join([r[1], r[2], r[4]])
    saida = ' '.join([p['a'], p['b'], p['como']])
    prob, _ = alinha(origem, saida, extra=set(tok('Como a banca troca')) | {'8', '1'})
    rot = collections.Counter(tok('Como a banca troca'))
    if (collections.Counter(tok(saida)) - collections.Counter(tok(origem))) & rot != rot and 'como a banca troca' not in saida.lower():
        prob.append('rótulo "Como a banca troca" ausente')
    if ' × '.join([p['a'], p['b']]) != re.sub(r' — acréscimo da v2 \(leitura externa [^()]*; QA PENDENTE \(R2\)\)$', '', r[1]):
        prob.append('termos a/b não reconstituem o campo Par')
    if re.search(r'\bR\d{1,2}\b|\bF\d{1,2}\b|Anexo N|SEM FONTE|BQ-', saida): prob.append('resta código ou marca de produção')
    if prob: ruim += 1; reg(f'- {r[0]}: ' + ' | '.join(prob))
reg(f'- Pares com defeito: {ruim}.')
DEF += ruim
reg('')

# ---------------------------------------------------------------- pegadinhas
i0 = next(i for i, x in enumerate(L) if x.startswith('## 4. (d) PEGADINHAS')); i1 = next(i for i in range(i0, len(L)) if L[i] == '---')
orig_p = []
for x in L[i0:i1]:
    m = re.match(r'^G-(\d\d)\. \[(C\d\.\d-\d\d)\] (.+)$', x)
    if m: orig_p.append((m.group(1), m.group(2), m.group(3)))
assert len(orig_p) == 62 == len(D['lote']['pegadinhas']), (len(orig_p), len(D['lote']['pegadinhas']))
reg('### 6.4 Pegadinhas (62)')
reg('')
ruim = 0
for (n, cb, o), p in zip(orig_p, D['lote']['pegadinhas']):
    prob, _ = alinha(o, p['texto'], extra=BASE | {'8', '1'} | EXTRA_BLOCO.get(cb, set()))
    folha = 'P1-DA-8' if cb.startswith('C8.0-') else f'P1-DA-{cb[1]}.{cb[3]}'
    if p['itemEdital'] != folha: prob.append(f'itemEdital {p["itemEdital"]} ≠ {folha}')
    if len(re.findall(r'\bBase: ', p['texto'])) != 1: prob.append('"Base:" não aparece exatamente uma vez')
    if re.search(r'\bR\d{1,2}\b|\bF\d{1,2}\b|Anexo N|SEM FONTE|BQ-|QA PENDENTE|\bv[12]\b', p['texto']): prob.append('resta código ou marca de produção')
    if prob: ruim += 1; reg(f'- pegadinha {int(n)} ({cb}): ' + ' | '.join(prob))
reg(f'- Pegadinhas com defeito: {ruim}.')
DEF += ruim
reg('')

# ---------------------------------------------------------------- itens
i51 = next(i for i, x in enumerate(L) if x.startswith('### 5.1')); i52 = next(i for i, x in enumerate(L) if x.startswith('### 5.2')); fim5 = next(i for i, x in enumerate(L) if x.startswith('## 6.'))
enun = {}
for x in L[i51:i52]:
    m = re.match(r'^\*\*(D4-\d\d)\.\*\* (.+)$', x)
    if m: enun[m.group(1)] = m.group(2)
just, gab, folha_i = {}, {}, {}
cur = None
for x in L[i52:fim5]:
    m = re.match(r'^\*\*(D4-\d\d)\*\* \((folha [\d.]+|caput[^)]*)\)', x)
    if m: cur = m.group(1); folha_i[cur] = m.group(2); just[cur] = ['', '']; continue
    if cur and x.startswith('- Justificativa (linha 1): '): just[cur][0] = x[len('- Justificativa (linha 1): '):]
    if cur and x.startswith('- Justificativa (linha 2): '): just[cur][1] = x[len('- Justificativa (linha 2): '):]
    if cur and x.startswith('- Gabarito: '): gab[cur] = x[len('- Gabarito: '):].strip()
assert len(enun) == 79 == len(gab) == len(D['itens']), (len(enun), len(gab), len(D['itens']))
reg('### 6.5 Itens (79): enunciado, gabarito, itemEdital e justificativa')
reg('')
ruim = 0
for it in D['itens']:
    i = it['id']
    fo = folha_i[i]
    eid = 'P1-DA-8' if fo.startswith('caput') else 'P1-DA-' + fo[6:]
    prob = []
    if it['enunciado'] != enun[i]: prob.append('enunciado difere do canônico')
    if it['gabarito'] != gab[i]: prob.append('gabarito difere do canônico')
    if it['itemEdital'] != eid: prob.append(f'itemEdital {it["itemEdital"]} ≠ {eid}')
    pj, _ = alinha(' '.join(just[i]), it['justificativa'], extra={'8', '1'})
    prob += pj
    if re.search(r'\bR\d{1,2}\b|\bF\d{1,2}\b|Anexo N|SEM FONTE|BQ-|QA PENDENTE|\bficha\b|\[TS\]|elemento-isca', it['justificativa'] + it['enunciado']): prob.append('resta código ou marca de produção')
    if prob: ruim += 1; reg(f'- {i}: ' + ' | '.join(prob))
reg(f'- Itens com defeito: {ruim}. (Enunciado e gabarito: iguais caractere a caractere; justificativa: alinhada por palavras.)')
DEF += ruim
reg('')

# ---------------------------------------------------------------- tópicos
mapa_rows = {}
sec = None
for x in MAPA.split('\n'):
    m = re.match(r'^### (4\.\d) ', x)
    if m: sec = m.group(1); continue
    if x.startswith('## '): sec = None
    if sec and x.startswith('| art.'):
        c = [y.strip() for y in x.strip().strip('|').split(' | ')]
        mapa_rows.setdefault(sec, []).append(c)
secoes_c = {}
for s in secoes:
    secoes_c['P1-DA-' + s.split(' ', 1)[0]] = s
reg('### 6.6 Tópicos (9)')
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
                achou = [c for lst in mapa_rows.values() for c in lst if re.sub(r'\s+', ' ', q['texto']).rstrip('.;:') in re.sub(r'\s+', ' ', c[1])]
                vig = [c for c in achou if not c[1].startswith('[REVOGADO') and not c[1].startswith('[REDAÇÃO ANTERIOR')]
                if not (vig and q['literal'] is True and q['conferido'] == vig[0][4] == '2026-10-20'):
                    ruim += 1; reg(f'- {k}: baseLegal {q["ref"]} não bate letra a letra com linha vigente do mapa (ou data diferente de 2026-10-20)')
                m = re.search(r'art\. (\d+)(?:º)?(-[A-Z])?', q['ref'])
                a = m.group(1) + (m.group(2) or '')
                if (q['ref'].startswith('Decreto') or (v['norma'].startswith('Decreto 9.203/2017') and ' e ' not in v['norma'])) and not m.group(2) and (7 <= int(m.group(1)) <= 15 or int(m.group(1)) == 20):
                    ruim += 1; reg(f'- {k}: baseLegal {q["ref"]}: artigo revogado sem letra')
                if not re.search(r'\bart(?:s)?\. ' + m.group(1) + r'º?' + re.escape(m.group(2) or '') + r'(?![\d-]|-[A-Z])', cs) and not re.search(r'\barts?\.[^.;]*' + m.group(1) + r'º?' + re.escape(m.group(2) or ''), cs):
                    ruim += 1; reg(f'- {k}: baseLegal {q["ref"]}: artigo não citado no curso da folha')
        else:
            textos.append(json.dumps(v, ensure_ascii=False))
    nums = set(re.findall(r'\d+', ' '.join(textos)))
    fora = sorted(nums - num_curso, key=int)
    if fora:
        ruim += 1; reg(f'- {k}: números que não aparecem no curso da folha: {fora}')
    if re.search(r'\bR\d{1,2}\b|\bF\d{1,2}\b|Anexo N|SEM FONTE|QA PENDENTE', ' '.join(textos)):
        ruim += 1; reg(f'- {k}: código ou marca de produção em texto de tópico')
    n = len(t['resumo'].split())
    if not 150 <= n <= 250: ruim += 1; reg(f'- {k}: resumo com {n} palavras')
reg(f'- Problemas nos tópicos (número ausente do curso da folha; dispositivo de baseLegal que não bate letra a letra com o mapa, sem a data 2026-10-20, revogado ou fora do curso): {ruim}.')
DEF += ruim
reg('')
# R-id ou F-id em qualquer parte do JSON
todo = json.dumps(D, ensure_ascii=False)
rid = sorted(set(re.findall(r'\bR\d{1,2}\b|\bF\d{1,2}\b', todo)))
reg(f'### 6.7 Códigos internos no JSON inteiro: {rid if rid else "nenhum R-id nem F-id"}.')
if rid: DEF += 1
reg('')
reg(f'RESULTADO DA CONFERÊNCIA DE FIDELIDADE: {DEF} defeito(s).')
print('\n'.join(SAIDA))
sys.exit(1 if DEF else 0)
