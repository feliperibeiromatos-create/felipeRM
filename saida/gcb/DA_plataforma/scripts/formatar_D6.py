# formatar_D6.py — T-72 (ordem DA 20/10/2026, alínea e) — 2026-10-20 — gerado por gcb-cpp
# Reformata o canônico saida/gcb/D6_v2_1.md para o formato da plataforma (FORMATO_PLATAFORMA_DA.md).
# Determinístico; só reformata (mover, trocar rótulos, deletar marcas/códigos, trocas mínimas registradas).
# Uso: python3 -I saida/gcb/DA_plataforma/scripts/formatar_D6.py
# Saídas: D6_plataforma.json e a parte automática de D6_registro_formato.md (o orquestrador/produção anexa validador e fidelidade).
import hashlib, json, pathlib, re, sys

RAIZ = pathlib.Path(__file__).resolve().parents[4]
CANON = RAIZ / 'saida/gcb/D6_v2_1.md'
DIR = RAIZ / 'saida/gcb/DA_plataforma'
SHA_ESPERADO = 'a983105818ad84e96a57a4f70ff19baa12224e11e939d023c6f7a29ca5414090'

bruto = CANON.read_bytes()
sha = hashlib.sha256(bruto).hexdigest()
if sha != SHA_ESPERADO:
    sys.exit(f'PARAR: SHA-256 do canônico diverge ({sha})')
L = bruto.decode('utf-8').split('\n')

def idx(prefixo, ini=0):
    for i in range(ini, len(L)):
        if L[i].startswith(prefixo):
            return i
    raise SystemExit('não achei: ' + prefixo)

edital = {e['id']: e['texto'] for e in json.loads((DIR / 'edital_DA.json').read_text(encoding='utf-8'))}

# ---------------------------------------------------------------- trocas e deleções (registradas)
# (id, regex, substituição, tipo, motivo)
TROCAS = [
 ('T01', r' ?\[QA PENDENTE — trecho importado\]', '', 'deleção de marca', 'marca de produção (seção 6)'),
 ('T02', r' ?\[QA PENDENTE — par importado\]', '', 'deleção de marca', 'marca de produção (seção 6)'),
 ('T03', r' ?\[QA PENDENTE — pegadinha importada\]', '', 'deleção de marca', 'marca de produção (seção 6)'),
 ('T04', r'\(REVERIFICAR\) ', '', 'deleção de marca', 'marca REVERIFICAR (seção 6)'),
 ('T05', r'\*\*(Encarregado|Autoridade nacional) \(REVERIFICAR\)\*\*', r'**\1**', 'deleção de marca', 'marca REVERIFICAR (seção 6)'),
 ('T06', r' — REVERIFICAR\.\)', '.)', 'deleção de marca', 'marca REVERIFICAR (seção 6)'),
 ('T07', r', REVERIFICAR\)', ')', 'deleção de marca', 'marca REVERIFICAR no título do bloco (seção 6)'),
 ('T08', r' \(REVERIFICAR para os dispositivos assinalados\)', '', 'deleção de marca', 'marca REVERIFICAR no título do bloco (seção 6)'),
 ('T09', r'\(REVERIFICAR — incluído', '(incluído', 'deleção de marca', 'marca REVERIFICAR (seção 6); mantido "incluído pela Lei 15.141/2025"'),
 ('T10', r', nos termos do texto transcrito no Anexo N \(art\. 7º', ' (art. 7º', 'troca mínima (op. 6)', 'a deleção de "Anexo N" (seção 6) quebraria a oração; omitido o trecho que cita o Anexo, mantidos os dispositivos da Lei 12.965/2014'),
 ('T11', r' Este lote não cobra datas de vigência de leis alteradoras\.', '', 'deleção de frase inteira', 'frase só de processo (alude a "lote"; seção 6)'),
 ('T12', r'; dispositivo vigente, em redação original, conforme a errata T-82 do Anexo N, seção 8\)', ')', 'deleção de trecho', 'trecho que cita errata T-82 e "Anexo N" (seção 6); permanece "(§ 5º)"'),
 ('T13', r'\*\[Acréscimo sobre o Anexo N — QA PENDENTE\.\]\* ', '', 'deleção de frase inteira', 'frase só de processo (cita "Anexo N" e "QA PENDENTE"; seção 6)'),
 ('T14', r' — REVERIFICAR\)', ')', 'deleção de marca', 'marca REVERIFICAR no resumo (seção 6)'),
 ('T15', r' \(REVERIFICAR\)', '', 'deleção de marca', 'marca REVERIFICAR (seção 6)'),
 ('T16', r' \(REVERIFICAR para o art\. 55-A\)', '', 'deleção de marca', 'marca REVERIFICAR (seção 6)'),
 ('T17', r' \(REVERIFICAR para o art\. 5º, VIII\)', '', 'deleção de marca', 'marca REVERIFICAR (seção 6)'),
 ('T18', r' \(REVERIFICAR quanto à denominação em 55-A\)', '', 'deleção de marca', 'marca REVERIFICAR (seção 6)'),
 ('T19', r' REVERIFICAR: art\. 8º-A', ' Art. 8º-A', 'troca mínima (op. 6)', 'deletada a marca "REVERIFICAR:"; "art." inicial de frase passa a "Art."'),
]
LOG = []   # (onde, id_troca, n)

def limpa(txt, onde):
    for tid, rx, sub, _tipo, _mot in TROCAS:
        txt, n = re.subn(rx, sub, txt)
        if n:
            LOG.append((onde, tid, n))
    return txt

def confere_resto(txt, onde):
    for m in ('REVERIFICAR', 'QA PENDENTE', 'Anexo N', 'T-82', 'trecho importado', '[TS]', 'VOLÁTIL'):
        if m in txt:
            sys.exit(f'PARAR: resíduo "{m}" em {onde}')

# ---------------------------------------------------------------- curso
i11 = idx('## 1.1 ')
i12 = idx('## 1.2 ')
iresumo = idx('# 2. (b) RESUMO')

def blocos(ini, fim):
    out, cur = [], None
    for ln in L[ini:fim]:
        m = re.match(r'### ([LG]\d+)\. (.*)$', ln)
        if m:
            cur = {'cod': m.group(1), 'titulo': m.group(2), 'linhas': []}
            out.append(cur)
        elif cur is not None and not ln.startswith('#') and ln.strip() != '---':
            cur['linhas'].append(ln)
    return out

B_L = blocos(i11, i12)
B_G = blocos(i12, iresumo)
assert len(B_L) == 24 and len(B_G) == 23, (len(B_L), len(B_G))

NORMA = {'L': 'Lei 12.527/2011', 'G': 'Lei 13.709/2018'}
EXTRA_BASE = {   # dispositivos de outras normas que o próprio bloco já cita, com o nome da norma no texto
 'L1': ['Constituição Federal, art. 5º, XXXIII', 'Constituição Federal, art. 37, § 3º, II', 'Constituição Federal, art. 216, § 2º'],
 'L7': ['Lei de Responsabilidade Fiscal, art. 73-B'],
 'G14': ['LAI, art. 1º, parágrafo único'],
}
CORRESP = []   # (origem, destino)

def bloco_md(b):
    cod = b['cod']
    titulo = limpa(b['titulo'], cod + ' (título)')
    confere_resto(titulo, cod + ' título')
    definicao = exemplo = pegadinha = None
    extras = []
    for ln in b['linhas']:
        if not ln.strip():
            continue
        if ln.startswith('**Definição.** '):
            definicao = ln[len('**Definição.** '):]
        elif ln.startswith('**Exemplo.** '):
            exemplo = ln[len('**Exemplo.** '):]
        elif ln.startswith('**Pegadinha provável.** '):
            pegadinha = ln[len('**Pegadinha provável.** '):]
        else:
            if definicao is None or exemplo is not None:
                sys.exit('linha fora de lugar em ' + cod)
            extras.append(ln)
    assert definicao and exemplo and pegadinha, cod
    definicao = limpa(definicao, cod + ' (definição)')
    extras = [limpa(x, cod + ' (parágrafo adicional)') for x in extras]
    exemplo = limpa(exemplo, cod + ' (exemplo)')
    pegadinha = limpa(pegadinha, cod + ' (pegadinha)')
    for t in [definicao, exemplo, pegadinha] + extras:
        confere_resto(t, cod)
    # BASE LEGAL: do título ("— art. Xº") e dos dispositivos de outras normas já citados no bloco
    disp = titulo.rsplit(' — ', 1)[1]
    m = re.match(r'^(art\. [^()]*?) \(e (arts\. [^()]*)\)$', disp)
    partes = [m.group(1), m.group(2)] if m else disp.split('; ')
    base = ['- ' + NORMA[cod[0]] + ', ' + p for p in partes] + ['- ' + x for x in EXTRA_BASE.get(cod, [])]
    sub = titulo
    md = [f'### {sub}', 'DEFINIÇÃO', definicao, '']
    for x in extras:
        md += [x, '']
    md += ['BASE LEGAL'] + base + ['', 'EXEMPLO PARLAMENTAR', exemplo, '', 'PEGADINHA PROVÁVEL', pegadinha, '']
    CORRESP.append((f'{cod}. {b["titulo"]}', f'### {sub}'))
    return '\n'.join(md)

curso = ['## 11 ' + edital['P1-DA-11'].upper(), '']
curso += [bloco_md(b) for b in B_L]
curso += ['## 12 ' + edital['P1-DA-12'].upper(), '']
curso += [bloco_md(b) for b in B_G]
curso_md = '\n'.join(curso).rstrip('\n') + '\n'
CORRESP.insert(0, ('1.1 LEI DE ACESSO À INFORMAÇÃO (Lei 12.527/2011) — blocos L1 a L24', '## 11 ' + edital['P1-DA-11'].upper()))
CORRESP.insert(25, ('1.2 LEI GERAL DE PROTEÇÃO DE DADOS PESSOAIS (Lei 13.709/2018, texto compilado) — blocos G1 a G23', '## 12 ' + edital['P1-DA-12'].upper()))

# ---------------------------------------------------------------- resumo
r1 = idx('## 2.1 Resumo'); r2 = idx('## 2.2 Resumo'); r3 = idx('---', r2)
def corpo_resumo(a, b):
    return '\n'.join(x for x in L[a + 1:b] if x.strip())
res = ('**LAI (Lei 12.527/2011)**\n\n' + limpa(corpo_resumo(r1, r2), 'resumo LAI') +
       '\n\n**LGPD (Lei 13.709/2018, compilada)**\n\n' + limpa(corpo_resumo(r2, r3), 'resumo LGPD'))
confere_resto(res, 'resumo')

# ---------------------------------------------------------------- pares
def pares_tabela(ini):
    out = []
    i = ini
    while i < len(L) and not L[i].startswith('|'):
        i += 1
    while i < len(L) and L[i].startswith('|'):
        c = [x.strip() for x in L[i].strip().strip('|').split('|')]
        if len(c) == 5 and re.match(r'^[LGI]-P\d+$', c[0]):
            out.append(c)
        i += 1
    return out

LISTA_PARES = pares_tabela(idx('## 3.1')) + pares_tabela(idx('## 3.2')) + pares_tabela(idx('## 3.3'))
assert len(LISTA_PARES) == 43, len(LISTA_PARES)
PARES = []
PAR_ESPECIAL = []
for cod, par, dif, _base, troca in LISTA_PARES:
    par = limpa(par, 'par ' + cod); dif = limpa(dif, 'par ' + cod); troca = limpa(troca, 'par ' + cod)
    confere_resto(par + dif + troca, 'par ' + cod)
    termos = par.split(' × ')
    if len(termos) >= 2:
        a, b = termos[0], ' × '.join(termos[1:])
    else:
        # I-P5 não tem " × ": a = o título do par; b = a "Diferença" vira o segundo termo (legislação específica)
        a = par
        b = 'Legislação específica, em especial Habeas Data, Processo Administrativo e LAI'
        PAR_ESPECIAL.append(cod)
    if not dif.endswith('.'):
        dif += '.'
        LOG.append(('par ' + cod, 'P-PONTO', 1))
    PARES.append({'a': a, 'b': b, 'como': dif + ' Como a banca troca: ' + troca})

# ---------------------------------------------------------------- pegadinhas
p1 = idx('## LAI', idx('# 4. PEGADINHAS')); p2 = idx('## LGPD', p1); p3 = idx('---', p2)
PEG = []
for k in range(p1 + 1, p3):
    m = re.match(r'^(\d+)\. (.*)$', L[k])
    if not m:
        continue
    n = int(m.group(1)); t = m.group(2)
    t = limpa(t, f'pegadinha {n}')
    confere_resto(t, f'pegadinha {n}')
    claim, _, base = t.partition(' — ')
    if not base.startswith('art'):
        sys.exit(f'pegadinha {n}: base inesperada')
    if not claim.rstrip('"”').endswith(('.', '?', '!')):
        claim += '.'
    ie = 'P1-DA-11' if n <= 32 else 'P1-DA-12'
    PEG.append({'itemEdital': ie, 'rotulo': edital[ie], 'texto': claim + ' Base: ' + base})
assert len(PEG) == 63 and sum(1 for p in PEG if p['itemEdital'] == 'P1-DA-11') == 32

# ---------------------------------------------------------------- itens
j1 = idx('## 5.1'); j2 = idx('## 5.2'); j3 = idx('---', j2)
ENUN = {}
for k in range(j1, j2):
    m = re.match(r'^\*\*(D6-\d\d)\*\* (.*)$', L[k])
    if m:
        ENUN[m.group(1)] = m.group(2)
assert len(ENUN) == 50

ITEM_LOG = {'I1': [], 'I2': [], 'I3': [], 'I4': []}
ITENS = []
k = j2
HDR = re.compile(r'^\*\*(D6-\d\d)\*\* — Gabarito: \*\*([CE])\*\* — Marcas: (.*)$')
while k < j3:
    m = HDR.match(L[k])
    if not m:
        k += 1; continue
    iid, gab, marcas = m.groups()
    assert L[k + 1].startswith('Base: ') and L[k + 2].startswith('Justificativa: ')
    ls = [L[k + 2][len('Justificativa: '):], L[k + 3]]
    assert L[k + 4].strip() == '' or L[k + 4].startswith('###') or L[k + 4].startswith('**D6')
    novas = []
    for ln in ls:
        orig = ln
        ln, n = re.subn(r'\s*Difere de BQ-.*$', '', ln)
        if n: ITEM_LOG['I1'].append(iid)
        ln, n = re.subn(r'; confirmar o texto (vigente )?antes do simulado final', '', ln)
        if n: ITEM_LOG['I3' if 'confirmar o texto vigente' in orig else 'I4'].append(iid)
        ln, n = re.subn(r'do \[TS\]', 'da troca sutil', ln)
        if n: ITEM_LOG['I2'].append(iid)
        if ln.strip():
            novas.append(ln.strip())
    just = ' '.join(novas)
    confere_resto(just, iid + ' justificativa')
    num = int(iid.split('-')[1])
    item = {
        'id': iid, 'rotulo': 'AUTORAL', 'certame': 'Projeto Câmara 2026',
        'cargo': 'Noções de Direito Administrativo e Administração Pública', 'ano': 2026,
        'numero': num, 'comando': 'Julgue o item a seguir.', 'textoBase': '',
        'enunciado': ENUN[iid], 'gabarito': gab, 'justificativa': just,
        'itemEdital': 'P1-DA-11' if num <= 30 else 'P1-DA-12', 'aderencia': 'direta',
        'url': 'saida/gcb/D6_v2_1.md',
    }
    if 'REVERIFICAR' in marcas or 'VOLÁTIL' in marcas:
        item['volatil'] = True
    confere_resto(item['enunciado'], iid + ' enunciado')
    ITENS.append(item)
    k += 4
assert [i['id'] for i in ITENS] == [f'D6-{n:02d}' for n in range(1, 51)]

# ---------------------------------------------------------------- tópicos (escritos à mão)
TOP = json.loads((DIR / 'D6_topicos_fonte.json').read_text(encoding='utf-8'))

lote = {
    'id': 'D6',
    'nome': 'Direito Administrativo — LAI e LGPD (itens 11 e 12 do edital)',
    'prova': 'P1',
    'itensEdital': ['P1-DA-11', 'P1-DA-12'],
    'resumo': res,
    'curso': curso_md,
    'pares': PARES,
    'pegadinhas': PEG,
}
saida = {'lote': lote, 'itens': ITENS, 'topicos': TOP}
(DIR / 'D6_plataforma.json').write_text(json.dumps(saida, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

# ---------------------------------------------------------------- registro (parte automática)
from collections import OrderedDict
agr = OrderedDict()
for onde, tid, n in LOG:
    if tid == 'P-PONTO':
        continue
    agr.setdefault(tid, []).append(f'{onde}' + (f' ×{n}' if n > 1 else ''))
desc = {t[0]: t for t in TROCAS}
R = []
R.append('# D6_registro_formato.md — T-72 (ordem DA 20/10/2026) — 2026-10-20 — gerado por gcb-cpp')
R.append('')
R.append(f'Fonte canônica única: saida/gcb/D6_v2_1.md (SHA-256 {sha}, conferido antes de formatar). Base normativa dos tópicos: saida/gcb/D6_anexo_N_mapa_normativo.md (com a errata T-82). Script: saida/gcb/DA_plataforma/scripts/formatar_D6.py (python3 -I). A seção 0 do canônico (registro de acatamento) é processo e não entra.')
R.append('')
R.append('## 1. Correspondência bloco de origem → destino (curso)')
R.append('')
R.append('| Origem no canônico | Destino no curso |')
R.append('|---|---|')
for o, d in CORRESP:
    R.append(f'| {o} | {d} |')
R.append('')
R.append('Seção 2.1 e 2.2 (resumos) → `lote.resumo` (cabeçalhos "Resumo — LAI/LGPD" trocados por "**LAI (…)**" e "**LGPD (…)**"). Seções 3.1, 3.2 e 3.3 → `lote.pares` (43). Seção 4 → `lote.pegadinhas` (63). Seção 5.1 (enunciado) e 5.2 (gabarito, justificativa, marcas) → `itens`. Seções 6 (proveniência) e 7 (contagens) não entram (processo). Cada bloco: "**Definição.**" → quadro DEFINIÇÃO (um só parágrafo); parágrafos adicionais do bloco (L7: arts. 8º-A e 8º-B) vêm depois, como texto normal; quadro BASE LEGAL derivado do título do bloco ("— art. Xº") e, onde o bloco já cita expressamente outra norma com dispositivo, dessa citação (L1: Constituição Federal; L7: Lei de Responsabilidade Fiscal, art. 73-B; G14: LAI, art. 1º, parágrafo único); "**Exemplo.**" → EXEMPLO PARLAMENTAR; "**Pegadinha provável.**" → PEGADINHA PROVÁVEL.')
R.append('')
R.append('## 2. Deleções de marcas e trocas mínimas (curso, resumo, pares, pegadinhas)')
R.append('')
R.append('| Id | Tipo | Regra | Onde | Motivo |')
R.append('|---|---|---|---|---|')
for tid in sorted(agr):
    t = desc[tid]
    onde = '; '.join(agr[tid])
    regra = f'`{t[1]}` → `{t[2] or "(vazio)"}`'.replace('|', '\\|')
    R.append(f'| {tid} | {t[3]} | {regra} | {onde} | {t[4]} |')
R.append('')
R.append('Demais operações nos textos acima: (a) códigos de bloco ("L1.", "G12."), de par ("L-P1") e de pegadinha (numeração "1.", "21." …) removidos; (b) em `pegadinhas`, o separador " — " entre a afirmação e o dispositivo foi trocado por " Base: " (operação 2 da seção 7) e, quando a afirmação não terminava em ponto, acrescentou-se o ponto final; (c) em `pares`, `a`/`b` = os termos do campo "Par" (a = primeiro termo; b = demais, unidos por " × "), `como` = "Diferença" (com ponto final acrescentado onde faltava: ' + str(sum(1 for o, t, n in LOG if t == "P-PONTO")) + ' pares) + " Como a banca troca: " + coluna "Como a banca troca"; a coluna "Base" não é carregada (a especificação só prevê diferença e troca); (d) par I-P5 ("Prazos e procedimentos do titular perante o Poder Público") não tem " × " no campo "Par": a = esse título; b = "Legislação específica, em especial Habeas Data, Processo Administrativo e LAI", tirado da própria coluna "Diferença" do par.')
R.append('')
R.append('## 3. Itens: justificativa e campos')
R.append('')
R.append('- `comando`: "Julgue o item a seguir." (o canônico traz o comando só como cabeçalho coletivo da seção 5.1; nenhum item tem comando próprio). `textoBase`: "" (o canônico não separa texto-base). `enunciado`: literal da seção 5.1 (nenhum caractere alterado).')
R.append('- `justificativa` = as duas linhas da seção 5.2 unidas por um espaço, sem o rótulo "Justificativa:". A linha "Base: … Mecanismo: …" não entra (só processo).')
R.append(f'- Deleção de frase inteira "Difere de BQ-… porque …" (comparação com item do banco; processo): {", ".join(ITEM_LOG["I1"])} ({len(ITEM_LOG["I1"])} itens; em D6-31, D6-38, D6-39, D6-40, D6-46, D6-47 e D6-48 a frase era a linha inteira, e a justificativa ficou com uma só linha).')
R.append(f'- Troca mínima (op. 6) "[TS]" → "troca sutil" ("A tentação do [TS] é" → "A tentação da troca sutil é"): {", ".join(ITEM_LOG["I2"])} ({len(ITEM_LOG["I2"])} itens).')
R.append(f'- Deleção do trecho de processo "; confirmar o texto vigente antes do simulado final": {", ".join(ITEM_LOG["I3"])}; "; confirmar o texto antes do simulado final": {", ".join(ITEM_LOG["I4"])}.')
vol = [i['id'] for i in ITENS if i.get('volatil')]
R.append(f'- Itens com `volatil: true` (marca REVERIFICAR no canônico; nenhum com VOLÁTIL): {", ".join(vol)}.')
R.append('')
R.append('## 4. Contagens')
R.append('')
nc = sum(1 for i in ITENS if i['gabarito'] == 'C'); ne = len(ITENS) - nc
R.append(f'- Itens: {len(ITENS)} (D6-01 a D6-30 → P1-DA-11: 30; D6-31 a D6-50 → P1-DA-12: 20); C {nc} / E {ne}.')
R.append(f'- Pares: {len(PARES)} (LAI 16; LGPD 20; interface 7). Pegadinhas: {len(PEG)} (P1-DA-11: 32; P1-DA-12: 31).')
R.append(f'- Curso: 2 blocos ## (11 e 12); {len(B_L)} ### no 11 e {len(B_G)} ### no 12.')
R.append(f'- Tópicos: {len(TOP)} (P1-DA-11, P1-DA-12), escritos à mão em D6_topicos_fonte.json e incorporados pelo script.')
(DIR / 'D6_registro_formato.md').write_text('\n'.join(R) + '\n', encoding='utf-8')
print('OK: D6_plataforma.json e D6_registro_formato.md (parte automática) gravados; itens', len(ITENS), 'pares', len(PARES), 'pegadinhas', len(PEG))
