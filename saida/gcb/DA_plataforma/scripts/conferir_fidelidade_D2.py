# conferir_fidelidade_D2.py — T-75 (ordem DA 20/10/2026) — 2026-10-20 — gerado por gcb-cpp
# Conferência própria de fidelidade do Lote D2: compara, palavra por palavra e na ordem, o texto de saída
# (D2_plataforma.json) com o texto de origem (saida/gcb/D2_v2_1.md), depois de aplicar à origem SOMENTE as edições
# registradas em D2_log_edicoes.json. Cada edição registrada é conferida contra o canônico: o trecho "antes" tem de
# existir uma única vez no campo de origem, e toda palavra que a edição acrescenta tem de estar declarada em
# "adicionado". Palavra acrescentada ou suprimida fora do registro = defeito. Confere também os tópicos (números e
# artigos no curso da folha; baseLegal letra a letra no mapa normativo, com a data da consulta).
# Uso: python3 -I saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D2.py
import collections, hashlib, json, pathlib, re, sys

RAIZ = pathlib.Path(__file__).resolve().parents[4]
DA = RAIZ / 'saida/gcb/DA_plataforma'
CANON_P = RAIZ / 'saida/gcb/D2_v2_1.md'
SHA_CANON = '59cffaa689ea869cd11c13e6a833470b0b91d24b0f25ea2cc2e100ac9be8bd2c'
if hashlib.sha256(CANON_P.read_bytes()).hexdigest() != SHA_CANON:
    print('PARAR: SHA-256 do canônico diverge'); sys.exit(2)
L = CANON_P.read_text(encoding='utf-8').replace('\r\n', '\n').split('\n')
D = json.loads((DA / 'D2_plataforma.json').read_text(encoding='utf-8'))
LOGJ = json.loads((DA / 'D2_log_edicoes.json').read_text(encoding='utf-8'))
MAPA = (RAIZ / 'saida/gcb/D2_anexo_N_mapa_normativo.md').read_text(encoding='utf-8')
EDITAL = {e['id']: e['texto'] for e in json.loads((DA / 'edital_DA.json').read_text(encoding='utf-8'))}
DATA_CONSULTA = '2026-10-20'

SAIDA, DEF = [], 0
def reg(m): SAIDA.append(m)
def defeito(m):
    global DEF
    DEF += 1; reg('  DEFEITO: ' + m)

def tok(t): return re.findall(r'[^\W_]+', t.lower())

def achar(prefixo, ini=0):
    for i in range(ini, len(L)):
        if L[i].startswith(prefixo): return i
    raise SystemExit('PARAR: seção não encontrada: ' + prefixo)

# ------------------------------------------------------------ o registro, conferido contra ele mesmo
POR_CTX = collections.defaultdict(list)
for e in LOGJ['log']: POR_CTX[e['ctx']].append(e)
USADOS = set()

def aplica(ctx, txt):
    """aplica à origem, na ordem, as edições registradas para o ctx; cada 'antes' tem de existir uma vez"""
    for e in POR_CTX.get(ctx, []):
        if txt.count(e['antes']) != 1:
            defeito(f'[{ctx}] o trecho "antes" aparece {txt.count(e["antes"])} vez(es) no campo de origem (esperado 1): {e["antes"][:70]!r}')
            continue
        USADOS.add(id(e))
        txt = txt.replace(e['antes'], e['depois'])
    return txt

def confere_registro():
    ruim = 0
    for e in LOGJ['log']:
        a, b = collections.Counter(tok(e['antes'])), collections.Counter(tok(e['depois']))
        novas = b - a
        decl = collections.Counter(tok(e['adicionado']))
        if novas - decl:
            ruim += 1; defeito(f'[{e["ctx"]}] a edição acrescenta palavra não declarada em "adicionado": {dict(novas - decl)}')
        if e['tipo'].startswith('deleção') and novas and e['tipo'] != 'deleção de marca':
            ruim += 1; defeito(f'[{e["ctx"]}] deleção que acrescenta palavra: {dict(novas)}')
        if e['tipo'].startswith('pontuação') and (a != b):
            ruim += 1; defeito(f'[{e["ctx"]}] "pontuação" que muda palavra')
    return ruim

# ------------------------------------------------------------ curso, bloco a bloco
def parse_origem():
    ini = achar('## 1. (a) CURSO'); fim = achar('## 2. (b) RESUMO', ini)
    BO, cur, folha = [], None, None
    for ln in L[ini + 1:fim]:
        m = re.match(r'^### Caput 3 — ', ln)
        if m: folha = '3.0'; continue
        m = re.match(r'^### Folha (\d\.\d) — ', ln)
        if m: folha = m.group(1); continue
        m = re.match(r'^\*\*(C\d\.\d-\d\d) (.+?)\*\*(.*)$', ln)
        if m:
            cur = dict(cod=m.group(1), titulo=m.group(2), suf=m.group(3), folha=folha, campos={}); BO.append(cur); continue
        if cur is not None and ln.startswith('- '):
            for k, p in (('def', '- Definição: '), ('ex', '- Exemplo (Legislativo, hipotético): '), ('peg', '- Pegadinha provável: ')):
                if ln.startswith(p): cur['campos'][k] = ln[len(p):]; break
            else:
                cur['campos']['solto'] = ln[2:]
    return BO

def parse_saida(curso):
    secs = re.split(r'^## ', curso, flags=re.M)[1:]
    out = []
    for s in secs:
        cab, _, resto = s.partition('\n')
        num = cab.split(' ', 1)[0]
        for p in re.split(r'^### ', resto, flags=re.M)[1:]:
            linhas = p.split('\n')
            b = dict(folha=num, titulo=linhas[0].strip(), def_=[], ex=[], peg=[], base=[], solto=[])
            modo = 'solto'
            for ln in linhas[1:]:
                st = ln.strip()
                if st == 'DEFINIÇÃO': modo = 'def_'; continue
                if st == 'BASE LEGAL': modo = 'base'; continue
                if st == 'EXEMPLO PARLAMENTAR': modo = 'ex'; continue
                if st == 'PEGADINHA PROVÁVEL': modo = 'peg'; continue
                if st == '': continue
                b[modo].append(re.sub(r'^- ', '', st) if modo in ('def_', 'base') else st)
            out.append(b)
        out[-1:]  # noqa
    return secs, out

reg('### 6.0 Registro das edições, conferido contra o canônico')
reg('')
n_reg = len(LOGJ['log'])
r_ruim = confere_registro()
reg(f'- {n_reg} edições registradas em D2_log_edicoes.json; edições que acrescentam palavra sem declarar, deleção que acrescenta palavra ou "pontuação" que muda palavra: {r_ruim}.')
reg('')

BO = parse_origem()
secs, SB = parse_saida(D['lote']['curso'])
reg('### 6.1 Curso: palavras do bloco de saída × bloco de origem (com as edições registradas)')
reg('')
reg('Origem = título (com a marca de versão, que o registro manda tirar) + campos do bloco, sem os rótulos "Definição:", "Exemplo (Legislativo, hipotético):" e "Pegadinha provável:"; aplicam-se à origem as edições registradas do bloco. Saída = título + texto dos quadros DEFINIÇÃO, EXEMPLO PARLAMENTAR e PEGADINHA PROVÁVEL (sem os rótulos de quadro e sem a lista BASE LEGAL). Comparação palavra por palavra, na ordem (maiúsculas ignoradas).')
reg('')
if len(BO) != len(SB):
    defeito(f'número de blocos: origem {len(BO)} × saída {len(SB)}')
bloc_ruim = 0
for b, s in zip(BO, SB):
    cod = b['cod']; ctx = 'curso ' + cod
    esperado_folha = '3.1' if b['folha'] == '3.0' else b['folha']
    ok = True; msgs = []
    if s['folha'] != esperado_folha: ok = False; msgs.append(f'folha {s["folha"]} ≠ {esperado_folha}')
    tit = aplica(ctx + ' (título)', b['titulo'] + b['suf']).strip()
    if 'solto' in b['campos']:
        txt_o = tit + ' ' + aplica(ctx + ' (texto)', b['campos']['solto'])
        txt_s = s['titulo'] + ' ' + ' '.join(s['solto'])
        if s['def_'] or s['ex'] or s['peg']: ok = False; msgs.append('quadros no bloco do caput 3')
    else:
        d = aplica(ctx + ' (definição)', b['campos']['def'])
        e = aplica(ctx + ' (exemplo)', b['campos']['ex'])
        g = aplica(ctx + ' (pegadinha)', b['campos']['peg'])
        txt_o = ' '.join([tit, d, e, g])
        txt_s = ' '.join([s['titulo'], ' '.join(s['def_']), ' '.join(s['ex']), ' '.join(s['peg'])])
        voc = set(tok(b['titulo'] + ' ' + ' '.join(b['campos'].values())))
        fora = sorted({w for ln in s['base'] for w in tok(ln) if w not in voc})
        if fora: ok = False; msgs.append(f'palavras de BASE LEGAL fora do bloco: {fora}')
        if not s['base']: ok = False; msgs.append('BASE LEGAL vazia')
    to, ts = tok(txt_o), tok(txt_s)
    if to != ts:
        ok = False
        co, cs = collections.Counter(to), collections.Counter(ts)
        msgs.append(f'palavras acrescentadas {dict(cs - co)}; suprimidas {dict(co - cs)}')
        if not (cs - co) and not (co - cs):
            for i, (x, y) in enumerate(zip(to, ts)):
                if x != y: msgs.append(f'ordem diverge na palavra {i}: {x!r} × {y!r}'); break
    if not ok:
        bloc_ruim += 1; defeito(f'{cod}: ' + '; '.join(msgs))
reg(f'- {len(BO)} blocos conferidos (109 regulares + o bloco do caput 3, que abre a folha 3.1); blocos com divergência: {bloc_ruim}.')
# cabeçalhos ##
cab_ruim = 0
heads = re.findall(r'^## (\d+\.\d) (.+)$', D['lote']['curso'], re.M)
for num, t in heads:
    tt = EDITAL['P1-DA-' + num]
    if len(tt) > 90 and ':' in tt: tt = tt.split(':')[0]
    if t != tt.upper(): cab_ruim += 1; defeito(f'## {num}: título {t!r} ≠ edital em maiúsculas')
reg(f'- Cabeçalhos `##`: {len(heads)}, com o texto do edital em maiúsculas; divergências: {cab_ruim}.')
pf = LOGJ.get('linhas_de_processo_fora', [])
pf_ruim = sum(1 for x in pf if x not in L)
if pf_ruim: defeito(f'{pf_ruim} linhas de processo registradas que não existem no canônico')
reg(f'- Parágrafos de convenção de produção que não entram ("Cada bloco: …"): {len(pf)} registrados, todos existem no canônico: {"sim" if not pf_ruim else "não"}.')
reg('')

# ------------------------------------------------------------ resumo
r1 = achar('## 2. (b) RESUMO'); r3 = next(i for i in range(r1, len(L)) if L[i] == '---')
bruto = '\n'.join(L[r1 + 1:r3])
bruto = aplica('resumo', bruto)
to, ts = tok(bruto), tok(D['lote']['resumo'])
reg('### 6.2 Resumo (seção 2 do canônico)')
reg('')
if to != ts:
    co, cs = collections.Counter(to), collections.Counter(ts)
    defeito(f'resumo: acrescentadas {dict(cs - co)}; suprimidas {dict(co - cs)}')
reg(f'- Palavras da origem (com as 5 edições registradas) × palavras da saída: {len(to)} × {len(ts)}; divergência: {"nenhuma" if to == ts else "SIM"}.')
reg('')

# ------------------------------------------------------------ pares
ip = achar('## 3. (c) PARES'); ip2 = achar('## 4. (d) PEGADINHAS', ip)
rows, cab_ok = [], False
for x in L[ip:ip2]:
    if x.startswith('| Código |'):
        cab_ok = [y.strip() for y in x.strip().strip('|').split('|')] == ['Código', 'Par', 'Diferença', 'Base', 'Como a banca troca']
    if re.match(r'^\| P-\d\d', x): rows.append([y.strip() for y in x.strip().strip('|').split('|')])
reg('### 6.3 Pares')
reg('')
if not cab_ok: defeito('cabeçalho da tabela de pares diferente do esperado (Código | Par | Diferença | Base | Como a banca troca)')
if len(rows) != len(D['lote']['pares']): defeito(f'pares: origem {len(rows)} × saída {len(D["lote"]["pares"])}')
ruim = 0
for r, p in zip(rows, D['lote']['pares']):
    dif = aplica('par ' + r[0], r[2])
    exp = tok(r[1]) + tok(dif) + tok('Como a banca troca') + tok(r[4])
    got = tok(p['a']) + tok(p['b']) + tok(p['como'])
    if exp != got or p['a'] + ' × ' + p['b'] != r[1]:
        ruim += 1; defeito(f'{r[0]}: palavras ou termos a/b divergentes')
reg(f'- {len(rows)} pares: termos a/b reconstituem a coluna "Par" (a + " × " + b); "como" = Diferença (com as edições registradas) + "Como a banca troca:" + coluna "Como a banca troca"; a coluna Base não entra. Pares com divergência: {ruim}.')
reg('')

# ------------------------------------------------------------ pegadinhas
i0 = achar('## 4. (d) PEGADINHAS'); i1 = next(i for i in range(i0, len(L)) if L[i] == '---')
orig_p = []
for x in L[i0:i1]:
    m = re.match(r'^G-(\d{2,3})\. \[(C\d\.\d-\d\d)(?:; (C\d\.\d-\d\d))?\] (.+)$', x)
    if m: orig_p.append((int(m.group(1)), m.group(2), m.group(4)))
reg('### 6.4 Pegadinhas')
reg('')
if len(orig_p) != len(D['lote']['pegadinhas']): defeito(f'pegadinhas: origem {len(orig_p)} × saída {len(D["lote"]["pegadinhas"])}')
ruim = 0
for (n, cb, t), p in zip(orig_p, D['lote']['pegadinhas']):
    t2 = aplica(f'pegadinha {n}', t)
    if tok(t2) != tok(p['texto']) or p['itemEdital'] != 'P1-DA-' + cb[1:4] or p['rotulo'] != EDITAL[p['itemEdital']]:
        ruim += 1; defeito(f'pegadinha {n}: palavras, itemEdital ({p["itemEdital"]}) ou rótulo divergentes')
reg(f'- {len(orig_p)} pegadinhas: texto = origem com as edições registradas (marca de versão sai; " — Dispositivo:" vira " Base:"); itemEdital = folha do bloco; rótulo = texto do edital. Divergências: {ruim}.')
reg('')

# ------------------------------------------------------------ itens
i51 = achar('### 5.1'); i52 = achar('### 5.2', i51); fim5 = achar('## 6.', i52)
enun = {}
for x in L[i51:i52]:
    m = re.match(r'^\*\*(D2-\d\d)\.\*\* (.+)$', x)
    if m: enun[m.group(1)] = m.group(2)
blocos, cur = {}, None
for x in L[i52:fim5]:
    m = re.match(r'^\*\*(D2-\d\d)\*\* \(folha (\d\.\d)\) — AUTORAL — (.*)$', x)
    if m: cur = m.group(1); blocos[cur] = dict(folha=m.group(2), F={}); continue
    if cur and x.startswith('- '):
        k, _, v = x[2:].partition(': '); blocos[cur]['F'][k] = v
reg('### 6.5 Itens: enunciado, gabarito, itemEdital, volatil e justificativa')
reg('')
if len(D['itens']) != len(blocos) or len(enun) != len(blocos): defeito(f'itens: saída {len(D["itens"])}, blocos {len(blocos)}, enunciados {len(enun)}')
ruim = 0
for it in D['itens']:
    i = it['id']; b = blocos[i]
    j = b['F']['Justificativa (linha 1)'].strip() + ' ' + b['F']['Justificativa (linha 2)'].strip()
    j = aplica('justificativa ' + i, j)
    vol = ('REVERIFICAR=sim' in b['F']['Marcas']) or ('VOLÁTIL=sim' in b['F']['Marcas'])
    ok = (it['enunciado'] == enun[i] and it['gabarito'] == b['F']['Gabarito'].strip() and it['itemEdital'] == 'P1-DA-' + b['folha']
          and tok(j) == tok(it['justificativa']) and bool(it.get('volatil')) == vol)
    if not ok:
        ruim += 1; defeito(f'{i}: enunciado/gabarito/itemEdital/volatil/justificativa divergentes do canônico')
c = sum(1 for it in D['itens'] if it['gabarito'] == 'C')
reg(f'- {len(D["itens"])} itens (C {c} / E {len(D["itens"]) - c}): enunciado e gabarito iguais caractere a caractere ao canônico; itemEdital = folha do item; volatil conforme a linha "Marcas" ({", ".join(it["id"] for it in D["itens"] if it.get("volatil")) or "nenhum"}); justificativa = linhas 1 e 2 com as edições registradas. Divergências: {ruim}.')
reg('')

# ------------------------------------------------------------ todas as edições registradas foram aplicadas?
nao = [e for e in LOGJ['log'] if id(e) not in USADOS and not e['ctx'].startswith('curso') or (e['ctx'].startswith('curso') and id(e) not in USADOS)]
if nao:
    defeito(f'{len(nao)} edições registradas que não foram aplicadas a nenhum campo de origem: {[e["ctx"] for e in nao[:5]]}')
reg(f'- Edições registradas aplicadas ao canônico: {len(USADOS)} de {n_reg}.')
reg('')

# ------------------------------------------------------------ tópicos
linhas_mapa = []
for x in MAPA.split('\n'):
    if x.startswith('| art.'):
        c = [y.strip() for y in x.strip().strip('|').split(' | ')]
        if len(c) >= 5: linhas_mapa.append(c)
secoes_c = {}
for s in secs:
    secoes_c['P1-DA-' + s.split(' ', 1)[0]] = s
reg('### 6.6 Tópicos')
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
                achados = [c for c in linhas_mapa if c[1] == q['texto']]
                art = re.search(r'art\. (\d+(?:-[A-Z])?)', q['ref']).group(1)
                if not (achados and q['literal'] is True and q['conferido'] == DATA_CONSULTA and any(c[4] == DATA_CONSULTA and re.match(r'art\. ' + re.escape(art) + r'(?!\d)', c[0]) for c in achados)):
                    ruim += 1; defeito(f'{k}: baseLegal {q["ref"]} não bate letra a letra com linha do mapa (artigo, texto, consulta {DATA_CONSULTA})')
                if not re.search(r'\barts?\. [^.;:]*?(?<!\d)' + re.escape(art) + r'(?!\d)', cs, re.I):
                    ruim += 1; defeito(f'{k}: baseLegal {q["ref"]}: artigo não citado no curso da folha')
        else:
            textos.append(json.dumps(v, ensure_ascii=False))
    nums = set(re.findall(r'\d+', ' '.join(textos)))
    fora = sorted(nums - num_curso, key=int)
    if fora:
        ruim += 1; defeito(f'{k}: números que não aparecem no curso da folha: {fora}')
    # artigos citados no texto corrido
    for m in re.finditer(r'\barts?\. ([\d]+)(?:-[A-Z])?', ' '.join(textos), re.I):
        if not re.search(r'\barts?\. [^.;:]*?(?<!\d)' + m.group(1) + r'(?!\d)', cs, re.I):
            ruim += 1; defeito(f'{k}: art. {m.group(1)} citado no tópico e ausente do curso da folha'); break
reg(f'- {len(D["topicos"])} tópicos: números e artigos dos textos e dos visuais presentes no curso da folha; baseLegal com `literal: true` bate letra a letra com a coluna de texto do mapa normativo e traz a data da consulta ({DATA_CONSULTA}). Problemas: {ruim}.')
reg('')
reg(f'RESULTADO DA CONFERÊNCIA DE FIDELIDADE: {DEF} defeito(s).')
print('\n'.join(SAIDA))
sys.exit(1 if DEF else 0)
