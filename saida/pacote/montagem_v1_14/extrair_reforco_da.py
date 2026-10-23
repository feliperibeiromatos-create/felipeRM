# extrair_reforco_da.py — T-123 fase 1 — 2026-10-23 — gerado por gbq-csc
# -*- coding: utf-8 -*-
"""T-123, fase 1 (D1 da GBQ, secoes 2.1, 2.2, 3.1 e 13): extracao dos 238 itens de reforco de DA e inventario das marcas de producao
(texto que a candidata le: enunciado e justificativa; mais enunciado/comando/textoBase dos 36 itens de banco P1-DA).
Uso: python -I extrair_reforco_da.py <raiz do repositorio> <pasta montagem_v1_14>
Leitura: todo insumo de texto e lido como bytes, com CRLF->LF antes do decode; SHA-256 sobre os bytes LF. Divergencia -> exit 2.
Grava: out/reforco_bruto.json, out/reforco_marcas.json, out/extracao_t123.json, T123_ocorrencias_DA.csv, T123_ocorrencias_DA_resumo.md.
Nao altera nenhum insumo."""
import collections, csv, hashlib, io, json, os, re, sys

RAIZ = os.path.abspath(sys.argv[1]); SAIDA = os.path.abspath(sys.argv[2])
OUT = os.path.join(SAIDA, 'out'); os.makedirs(OUT, exist_ok=True)

def lf(path):
    b = open(path, 'rb').read().replace(b'\r\n', b'\n')
    return b, hashlib.sha256(b).hexdigest()

def abort(msg):
    sys.stderr.write('ABORTA: ' + msg + '\n'); sys.exit(2)

# ---------------------------------------------------------------- SHA-256 esperados: linhas de aceite de DECISOES.md
dec_b, _ = lf(os.path.join(RAIZ, 'DECISOES.md')); dec = dec_b.decode('utf-8')
LEVAS = {}
for n in range(1, 9):
    nome = 'DA_reforco_leva%d_v2.md' % n
    m = re.findall(re.escape(nome) + r' \(SHA-256 ([0-9a-f]{64})', dec)
    if not m or len(set(m)) != 1:
        abort('SHA-256 de %s nao achado de forma unica em DECISOES.md: %r' % (nome, m))
    LEVAS[n] = (nome, m[0])

# ---------------------------------------------------------------- parse das levas
RX_S1 = re.compile(r'^\*\*(D[1-6]-R\d{2})\.\*\* (.+)$')
RX_S2 = re.compile(r'^\*\*(D[1-6]-R\d{2})\*\* \(folha')
ERRATAS = [  # (id, leva, secao, campo, antes, depois, ato)
    ('D3-R13', 1, 1, 'enunciado', 'são obrigados a fornecer serviços adequados, eficientes, seguros e, quanto aos essenciais, contínuos os órgãos públicos, por si ou suas empresas, concessionárias, permissionárias ou sob qualquer outra forma de empreendimento.',
     'os órgãos públicos, por si ou suas empresas, concessionárias, permissionárias ou sob qualquer outra forma de empreendimento, são obrigados a fornecer serviços adequados, eficientes, seguros e, quanto aos essenciais, contínuos.', 'AJ-E1 (D-T116-LEVA2-ACEITE, II)'),
    ('D3-R18', 2, 1, 'enunciado', 'tenha causado dano ao erário e falecido.', 'tenha causado dano ao erário e, posteriormente, tenha falecido.', 'AJ-L2-E1 (D-T116-LEVA3-ACEITE, II)'),
    ('D3-R75', 7, 2, 'j2', '; a tentação é lembrar de outro limite de desconto fora desta lei (o valor “terço” não ocorre na Lei 4.619).',
     '; o valor “terço” não ocorre na Lei 4.619, cujo único limite de desconto é o do art. 6º.', 'AJ-L7-E1 (D-D3R75-AJL7E1-ACEITE)'),
]
EXT = collections.OrderedDict()   # criterios de extracao
itens = []                        # ordem da secao 1 de cada leva
shas = {}
for n in range(1, 9):
    nome, esp = LEVAS[n]
    caminho = os.path.join(RAIZ, 'saida', 'gcb', nome)
    b, h = lf(caminho)
    shas[n] = dict(arquivo='saida/gcb/' + nome, sha256_lf=h, bytes=len(b), linhas=b.count(b'\n'), esperado=esp)
    if h != esp:
        abort('SHA-256 LF de %s: esperado %s, obtido %s' % (nome, esp, h))
    linhas = b.decode('utf-8').split('\n')
    if linhas and linhas[-1] == '': linhas.pop()
    # limites de secao
    sec = {}
    atual = None
    for i, l in enumerate(linhas, 1):
        m = re.match(r'^## (\d+)\.', l)
        if m: atual = int(m.group(1)); sec.setdefault(atual, [i, None])
        if re.match(r'^## ', l) and atual is not None and not m: atual = None
        if atual is not None: sec[atual][1] = i
    s1 = {}; ordem = []
    for i in range(sec[1][0], sec[1][1] + 1):
        m = RX_S1.match(linhas[i - 1])
        if m:
            if m.group(1) in s1: abort('id duplicado na secao 1 de %s: %s' % (nome, m.group(1)))
            s1[m.group(1)] = (i, m.group(2)); ordem.append(m.group(1))
    s2 = {}
    marcas_ini = [(i, RX_S2.match(linhas[i - 1]).group(1)) for i in range(sec[2][0], sec[2][1] + 1) if RX_S2.match(linhas[i - 1])]
    for k, (i, iid) in enumerate(marcas_ini):
        fim = marcas_ini[k + 1][0] - 1 if k + 1 < len(marcas_ini) else sec[2][1]
        campos = {}
        for j in range(i, fim + 1):
            m = re.match(r'^- (itemEdital|Aderência|Gabarito|Justificativa \(linha 1\)|Justificativa \(linha 2\)): (.*)$', linhas[j - 1])
            if m: campos[m.group(1)] = (j, m.group(2))
        header = linhas[i - 1]
        s2[iid] = dict(campos=campos, ts=('[TS]' in header), header_linha=i)
    if set(s1) != set(s2): abort('%s: ids da secao 1 e da secao 2 diferem: %s' % (nome, sorted(set(s1) ^ set(s2))))
    for iid in ordem:
        c = s2[iid]['campos']
        for k in ('itemEdital', 'Aderência', 'Gabarito', 'Justificativa (linha 1)', 'Justificativa (linha 2)'):
            if k not in c: abort('%s %s sem campo %s' % (nome, iid, k))
        itens.append(dict(id=iid, lote=iid.split('-')[0], leva=n, itemEdital=c['itemEdital'][1], gabarito=c['Gabarito'][1], aderencia=c['Aderência'][1],
                          enunciado=s1[iid][1], j1=c['Justificativa (linha 1)'][1], j2=c['Justificativa (linha 2)'][1], ts=s2[iid]['ts'],
                          arquivo='saida/gcb/' + nome, l_enunciado=s1[iid][0], l_j1=c['Justificativa (linha 1)'][0], l_j2=c['Justificativa (linha 2)'][0]))

# ---------------------------------------------------------------- erratas (antes 1x na secao e 1x no arquivo; depois 0x)
erratas_res = []
for (iid, leva, secao, campo, antes, depois, ato) in ERRATAS:
    it = next(x for x in itens if x['id'] == iid and x['leva'] == leva)
    alvo = it['enunciado'] if campo == 'enunciado' else it[campo]
    b, _ = lf(os.path.join(RAIZ, 'saida', 'gcb', LEVAS[leva][0])); txt = b.decode('utf-8')
    r = dict(id=iid, ato=ato, antes_na_secao=alvo.count(antes), antes_no_arquivo=txt.count(antes), depois_antes_de_aplicar=txt.count(depois))
    if r['antes_na_secao'] != 1 or r['antes_no_arquivo'] != 1 or r['depois_antes_de_aplicar'] != 0:
        abort('errata %s: %r' % (iid, r))
    novo = alvo.replace(antes, depois)
    if campo == 'enunciado': it['enunciado'] = novo
    else: it[campo] = novo
    r['depois_depois_de_aplicar'] = novo.count(depois)
    erratas_res.append(r)
for it in itens:
    it['justificativa'] = it['j1'] + ' ' + it['j2']
sem_e3e4 = {}
for iid, fr in (('D4-R42', 'AJ-L8-E3'), ('D4-R52', 'AJ-L8-E4')):
    sem_e3e4[iid] = fr
# "antes" de E3/E4: lido do texto da errata nas secoes de resposta nao e fixado pela D1; registra-se so a presenca do id.

# ---------------------------------------------------------------- criterios da secao 2.1
ids = [x['id'] for x in itens]
tot_leva = collections.OrderedDict()
for n in range(1, 9):
    L = [x for x in itens if x['leva'] == n]
    tot_leva[n] = dict(n=len(L), C=sum(x['gabarito'] == 'C' for x in L), E=sum(x['gabarito'] == 'E' for x in L), TS=sum(x['ts'] for x in L), parciais=sum(x['aderencia'] == 'parcial' for x in L))
tot_lote = collections.OrderedDict()
for l in ('D1', 'D2', 'D3', 'D4'):
    L = [x for x in itens if x['lote'] == l]
    tot_lote[l] = dict(n=len(L), C=sum(x['gabarito'] == 'C' for x in L), E=sum(x['gabarito'] == 'E' for x in L))
ESP_LEVA = {1: (30, 15, 15, 16, 8), 2: (30, 17, 13, 13, 2), 3: (30, 16, 14, 14, 11), 4: (28, 15, 13, 13, 5), 5: (30, 16, 14, 14, 0), 6: (30, 14, 16, 15, 0), 7: (30, 15, 15, 13, 8), 8: (30, 14, 16, 16, 1)}
ESP_LOTE = {'D1': (12, 6, 6), 'D2': (80, 40, 40), 'D3': (89, 49, 40), 'D4': (57, 27, 30)}
crit = collections.OrderedDict()
crit['n_ids'] = dict(esperado=238, obtido=len(ids))
crit['ids_unicos'] = dict(esperado=238, obtido=len(set(ids)))
crit['C_E'] = dict(esperado=[122, 116], obtido=[sum(x['gabarito'] == 'C' for x in itens), sum(x['gabarito'] == 'E' for x in itens)])
crit['parciais'] = dict(esperado=35, obtido=sum(x['aderencia'] == 'parcial' for x in itens))
crit['itemEdital_P1_DA'] = dict(esperado=238, obtido=sum(x['itemEdital'] == 'P1-DA-' + x['itemEdital'].split('P1-DA-')[-1] and x['itemEdital'].startswith('P1-DA-') for x in itens))
crit['por_leva'] = {str(n): dict(esperado=list(ESP_LEVA[n]), obtido=[tot_leva[n]['n'], tot_leva[n]['C'], tot_leva[n]['E'], tot_leva[n]['TS'], tot_leva[n]['parciais']], ok=list(ESP_LEVA[n]) == [tot_leva[n]['n'], tot_leva[n]['C'], tot_leva[n]['E'], tot_leva[n]['TS'], tot_leva[n]['parciais']]) for n in range(1, 9)}
crit['por_lote'] = {l: dict(esperado=list(ESP_LOTE[l]), obtido=[tot_lote[l]['n'], tot_lote[l]['C'], tot_lote[l]['E']], ok=list(ESP_LOTE[l]) == [tot_lote[l]['n'], tot_lote[l]['C'], tot_lote[l]['E']]) for l in ESP_LOTE}
crit['vagos_ausentes'] = dict(esperado=['D1-R03', 'D4-R12'], obtido_presentes=[v for v in ('D1-R03', 'D4-R12') if v in ids])
crit['D3-R75_apos_D3-R74'] = dict(ok=ids.index('D3-R75') == ids.index('D3-R74') + 1)
crit['erratas'] = erratas_res
crit['E3_E4_ids_presentes'] = dict(D4_R42='D4-R42' in ids, D4_R52='D4-R52' in ids)
for k in ('crit',): pass

# ---------------------------------------------------------------- banco P1-DA (36)
bb, bh = lf(os.path.join(RAIZ, 'banco', 'banco.csv'))
if bh != 'b1c1588f8b4a80a233e7b8d485992d07e9adeb2570fb2343573ab7fde9a5721f': abort('SHA-256 LF de banco/banco.csv: obtido ' + bh)
btxt = bb.decode('utf-8')
rd = csv.reader(io.StringIO(btxt, newline=''), delimiter=';')
cab = next(rd); banco = []; ant = rd.line_num
for row in rd:
    ini = ant + 1; ant = rd.line_num
    d = dict(zip(cab, row)); d['_linha'] = ini
    if d['item_edital_camara'].startswith('P1-DA') and d['anulado'] == 'nao' and d['id'] not in ('BQ-0141', 'BQ-0151'):
        banco.append(d)
crit['banco_P1_DA'] = dict(esperado=36, obtido=len(banco), CE=[sum(d['gabarito'] == 'C' for d in banco), sum(d['gabarito'] == 'E' for d in banco)], esperado_CE=[26, 10])

# ---------------------------------------------------------------- inventario de marcas
def R(p, f=0): return re.compile(p, f)
FN = r'F\d{1,2}'
# (cat, subtipo, regex, origem)  origem: CM = C-MARCAS (D1 8.1); T108 = inventario T-108; PR = marcas_processo.py (R)
REGRAS = [
    # C-MARCAS (D1, secao 8.1)
    ('C05', 'codigo de fonte R/F/G/H', R(r'\b[RFGH]\d{1,3}[a-e]?\b'), 'CM'),
    ('C02', 'ponto de julgamento A<folha>-<n>', R(r'\bA\d+(?:\.\d+)?-\d+'), 'CM'),
    ('C03', 'alerta', R(r'(?i)\balertas?\b(?: (?:[A-Z]{1,2}\d+|\d+)(?:(?:,| e) (?:[A-Z]{1,2}\d+|\d+))*)?'), 'CM'),
    ('C05', 'Anexo N', R(r'\bAnexos? N\d*(?: d[oa] D[1-6])?(?:, seção [\d.]+)?'), 'CM'),
    ('C05', 'Anexo (generico)', R(r'\bAnexos?\b'), 'CM'),
    ('C02', 'id de item', R(r'\b(?:D[1-6]|L\d|BQ)-R?\d+'), 'CM'),
    ('C10', 'moldura', R(r'(?i)\bmoldura\b'), 'CM'),
    ('C10', 'cota', R(r'(?i)\bcotas?\b'), 'CM'),
    ('C10', 'ficha', R(r'(?i)\bfichas?\b'), 'CM'),
    ('C01', 'leva N', R(r'(?i)\blevas? \d'), 'CM'),
    ('C10', '[TS] / TS=', R(r'\[TS\]|TS='), 'CM'),
    ('C06', 'mecanismo (C|E)n', R(r'\((?:C|E)\d\)'), 'CM'),
    ('C07', 'QA', R(r'\bQA\b'), 'CM'),
    ('C10', 'PENDENTE', R(r'PENDENTE'), 'CM'),
    ('C10', 'REVERIFICAR', R(r'REVERIFICAR'), 'CM'),
    ('C10', 'VOLATIL', R(r'VOLÁTIL|VOLÁTEIS'), 'CM'),
    ('C10', 'SEM FONTE', R(r'SEM FONTE'), 'CM'),
    ('C05', 'url', R(r'https?://\S+'), 'CM'),
    ('C10', 'folha', R(r'(?i)\bfolhas?\b'), 'CM'),
    ('C10', 'negrito **', R(r'\*\*'), 'CM'),
    # T-108 (ORDEM C): categorias C01-C10
    ('C04', '[V ...]', R(r'\[V\s[^\]]*\]'), 'T108'),
    ('C04', '[NORMATIVO ...]', R(r'\[NORMATIVO[^\]]*\]'), 'T108'),
    ('C04', '[Fn ...]', R(r'\[' + FN + r'(?:[^\]\w][^\]]*)?\]'), 'T108'),
    ('C04', '[Nn ...]', R(r'\[N\d(?:[^\]\w][^\]]*)?\]'), 'T108'),
    ('C10', '[nao cobrar ...]', R(r'\[não cobrar[^\]]*\]'), 'T108'),
    ('C01', 'lote', R(r'(?i)(?<![\w])lotes?(?![\w])'), 'T108'),
    ('C02', 'codigo de item (T108)', R(r'(?<![\w-])(?:L\dC?-[QR]?\d{2,3}|L6[AB]-R\d{2}|(?:4C|5C|A5|6A|6B)-\d{2}|BQ-\d{4})(?![\w])'), 'T108'),
    ('C02', 'espelho da troca', R(r'(?i)espelho da troca'), 'T108'),
    ('C02', 'Qnn', R(r'(?<![\w-])Q\d{2}(?![\w])'), 'T108'),
    ('C03', 'par Cn', R(r'(?<![\w])par(?:es)? C\d{1,2}(?:(?:, | e )C\d{1,2})*(?![\w])'), 'T108'),
    ('C03', '(Cn)', R(r'\(C\d{1,2}\)'), 'T108'),
    ('C03', 'Pn', R(r'(?<![\w/])P\d{1,2}(?![\w-])'), 'T108'),
    ('C05', 'Fn (T108)', R(r'(?<![\w\[])' + FN + r'(?![\w])'), 'T108'),
    ('C05', 'Nn', R(r'(?<![\w\[])N\d{1,2}(?![\w])'), 'T108'),
    ('C05', 'U/GG/TB', R(r'(?<![\w])(?:U\d|GG\d|TB\d)(?![\w])'), 'T108'),
    ('C06', 'TC/IC/GI/AT', R(r'(?<![\w])(?:TC|IC|GI|AT)(?= invertida|[ .(:;,)]|$)'), 'T108'),
    ('C06', 'sem armadilha (ancoragem)', R(r'(?i)sem armadilha \(ancoragem\)'), 'T108'),
    ('C07', 'conferido por script/QA', R(r'(?i)(?:conferid|verificad|confirmad|reconfirmad)[oa]s? (?:por script|pel[ao] (?:CQFP|QA|CQE|produção))'), 'T108'),
    ('C07', 'agente', R(r'(?i)(?<![\w])(?:gbq-[a-z]+|gce-[a-z]+|gcb-[a-z]+|qa-normativo(?:-da)?|corretor-[ab])(?![\w])'), 'T108'),
    ('C07', 'unidade/QA', R(r'(?<![\w])(?:QA|CQFP|CQE|CPP|GCE|GCB|GBQ|CSC)(?![\w])'), 'T108'),
    ('C08', 'errata', R(r'(?i)(?<![\w])erratas?(?![\w])'), 'T108'),
    ('C08', 'producao', R(r'(?i)(?<![\w])(?:produção|produtor[a]?|fábrica)(?![\w])'), 'T108'),
    ('C08', 'id de decisao/tarefa', R(r'(?<![\w])(?:D-[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*|T-\d{1,3})(?![\w])'), 'T108'),
    ('C08', 'rotulo ou arquivo interno', R(r'CEBRASPE_ANALOGA|GAB_DEFINITIVO_\w+|(?<![\w])AUTORAL(?![\w])'), 'T108'),
    ('C09', 'vN', R(r'(?<![\w.])v\d+(?:\.\d+)*(?![\w])'), 'T108'),
    ('C09', 'versao N do lote', R(r'(?i)versão \d+ d[oa] (?:lote|curso|item)'), 'T108'),
    ('C10', 'So o fato e a fonte', R(r'Só o fato e a fonte\.?'), 'T108'),
    ('C10', 'SEM ITEM', R(r'(?i)(?<![\w])(?:sem item|não vira item|não entra em item|não há item|nenhum item)(?![\w])'), 'T108'),
    ('C10', 'NAO GABARITO / CONTROVERSO', R(r'NÃO GABARITO|CONTROVERSO'), 'T108'),
    ('C10', 'nao cobrar', R(r'(?i)(?<![\w])não (?:são |é )?cobr(?:ar|a|am|ado|ados|ada|adas)(?![\w])'), 'T108'),
    ('C10', 'nao afirmar', R(r'\(não afirmar\)|(?i:nunca dizer)'), 'T108'),
    ('C10', 'CONTEXTO NORMATIVO INTERNO', R(r'CONTEXTO NORMATIVO INTERNO'), 'T108'),
    # PROCESSO (gerador_v1_12/marcas_processo.py, lista R)
    ('C04', 'PR:V', R(r'\[V\s'), 'PR'),
    ('C07', 'PR:NORMATIVO', R(r'NORMATIVO — QA'), 'PR'),
    ('C05', 'PR:Fn', R(r'(?<![\w])F\d{1,2}(?![\w])'), 'PR'),
    ('C07', 'PR:unidade', R(r'(?<![\w])(?:CQFP|CQE|CPP|GCE|GCB|GBQ|CSC|QA)(?![\w])'), 'PR'),
    ('C07', 'PR:agente', R(r'(?i)(?<![\w])(?:gbq-[a-z]+|gce-[a-z]+|gcb-[a-z]+|qa-normativo(?:-da)?|corretor-[ab]|presidencia|orquestrador)(?![\w])'), 'PR'),
    ('C08', 'PR:id', R(r'(?<![\w])(?:[TEORN]-\d{1,3}|D-[A-Z0-9][A-Z0-9-]*)(?![\w])'), 'PR'),
    ('C10', 'PR:Rn', R(r'(?m)^R\d\. '), 'PR'),
    ('C08', 'PR:ampliada', R(r'(?<![\w])(?:Presidência|Fundador|Secretaria|PRES-S|EXEC|BIP|FV)(?![\w])'), 'PR'),
    ('C08', 'PR:fabrica', R(r'(?i)(?<![\w])fábrica(?![\w])'), 'PR'),
    ('C08', 'PR:modelo', R(r'(?<![\w])(?:Claude|Sonnet|Opus|Haiku|ChatGPT)(?![\w])'), 'PR'),
    ('C08', 'PR:ferramenta', R(r'(?i)claude\.ai|Insumo_'), 'PR'),
    ('C07', 'PR:carimbo', R(r'(?:re)?verificad[oa]s? em \d{1,2}/\d{1,2}/\d{4}|conferid[oa]s? pel[ao]|\(leitura de \d|[Vv]erificado em \d'), 'PR'),
]
FP = [  # (regex sobre janela [-60,+60], classe, motivo)
    (R(r'tecla F4'), 'FP', 'tecla F4 do Excel (regra 1)'),
    (R(r'(?i)em produção|reprodução|reproduz'), 'FP', 'producao no sentido tecnico do conteudo'),
    (R(r'(?i)é cobrad[oa] (?:pela|pelo)|cobra (?:o|a) taxa'), 'FP', 'cobrar no sentido do conteudo'),
]
LOTE_PROC = R(r'(?<![\w])(?:Lotes? (?:\d|6[ab])|(?:neste|deste|este|desse|nesse|esse) lote|(?:o|do) lote (?:NÃO|são|usa)|lote D[1-6])')
LOTE_TEC = R(r'(?i)em lote|entre lote e|só no lote|batch|tempo real (?:e|×) lote|→ lote|lote e limites|lote, submete|à do lote|lote sem erro')

def classifica(cat, sub, t, a, b, g):
    """MARCA (marca de producao a limpar), VERIFICAR (decisao da GCB) ou FP (falso positivo)."""
    jan = t[max(0, a - 60):b + 60]
    for rx, cl, mot in FP:
        if rx.search(jan) and cat in ('C05', 'C08', 'C10') and (cl == 'FP'):
            if 'F4' in mot and not re.search(r'tecla F4', jan): continue
            if 'produção' in mot and cat != 'C08': continue
            if 'cobrar' in mot and cat != 'C10': continue
            return 'FP', mot
    if cat == 'C01' and sub == 'lote':
        if LOTE_PROC.search(t[max(0, a - 12):b + 8]): return 'MARCA', 'lote de producao'
        if LOTE_TEC.search(t[max(0, a - 25):b + 25]): return 'FP', 'lote/batch tecnico (regra 1)'
        return 'VERIFICAR', 'lote: decisao da GCB'
    if sub == 'folha':
        if re.search(r'(?i)folha de pagamento|desconto em folha|folhas? de ponto', t[max(0, a - 12):b + 20]): return 'FP', 'folha no sentido do conteudo (folha de pagamento)'
        return 'MARCA', 'folha (D1 8.1)'
    if sub == 'cota':
        if re.search(r'(?i)cota da folha|cota d[ae] (?:leva|simulado)|cotas? por simulado', jan): return 'MARCA', 'cota de producao'
        return 'VERIFICAR', 'cota: possivel sentido de conteudo'
    if sub == 'Anexo (generico)':
        return 'VERIFICAR', 'Anexo sem N: pode ser anexo de norma; decisao da GCB'
    if cat == 'C08' and sub in ('producao', 'ampliada'):
        return 'VERIFICAR', 'produtor/producao/Presidencia: pode ser sentido de conteudo; decisao da GCB'
    if sub in ('alerta',) and not re.search(r'(?i)alertas? (?:[A-Z]{1,2}\d+|\d+)', g):
        return 'VERIFICAR', 'alerta sem codigo: pode ser sentido de conteudo'
    return 'MARCA', ''

def varre(texto):
    """lista de dicts (cat, sub, a, b, trecho, origens, classe, motivo) com fusao de sobrepostos na mesma categoria."""
    hits = []
    for cat, sub, rx, org in REGRAS:
        for m in rx.finditer(texto):
            if m.end() == m.start(): continue
            hits.append([cat, sub, m.start(), m.end(), {org + ':' + sub}])
    # fusao: mesma categoria, spans que se tocam/sobrepoem
    por_cat = collections.defaultdict(list)
    for h in hits: por_cat[h[0]].append(h)
    out = []
    for cat, L in por_cat.items():
        L.sort(key=lambda h: (h[2], -h[3]))
        cur = None
        for h in L:
            if cur and h[2] < cur[3]:
                cur[3] = max(cur[3], h[3]); cur[4] |= h[4]
                cur[1].append(h[1]) if h[1] not in cur[1] else None
            else:
                if cur: out.append(cur)
                cur = [h[0], [h[1]], h[2], h[3], set(h[4])]
        if cur: out.append(cur)
    out.sort(key=lambda h: (h[2], h[0]))
    res = []
    for cat, subs, a, b, orig in out:
        g = texto[a:b]
        # subtipo principal: o mais especifico (mais longo) dentre os subtipos fundidos que nao sejam os genericos
        subs_sorted = sorted(subs, key=lambda s: (s.startswith('PR:'), s == 'Anexo (generico)', -len(s)))
        sub = subs_sorted[0]
        cl, mot = classifica(cat, sub.split(':')[-1] if sub.startswith('PR:') else sub, texto, a, b, g)
        res.append(dict(cat=cat, sub=sub, a=a, b=b, trecho=g, regras=sorted(orig), classe=cl, motivo=mot))
    return res

def antes_unico(campo, a, b):
    """menor janela simetrica em torno de [a,b) que ocorre exatamente 1 vez no campo."""
    k = 0
    while True:
        s, e = max(0, a - k), min(len(campo), b + k)
        w = campo[s:e]
        if campo.count(w) == 1 or (s == 0 and e == len(campo)): return w
        k += 3

linhas_csv = []
marcas_por_item = collections.OrderedDict()
vistos = collections.Counter()
def registra(iid, origem, lote, leva, campo, texto, arquivo, linha_de, ato_linha):
    """linha_de: funcao (offset)->(arquivo:linha, parte)"""
    for h in varre(texto):
        key = (iid, campo, h['cat'], h['trecho'])
        k = vistos[key]; vistos[key] += 1
        oid = 'T123-%s-%s' % (h['cat'], hashlib.sha1(('%s|%s|%s|%s|%d' % (iid, campo, h['cat'], h['trecho'], k)).encode('utf-8')).hexdigest()[:8])
        ref, parte = linha_de(h['a'])
        row = dict(id_ocorrencia=oid, item=iid, origem=origem, lote=lote, leva=leva, campo=campo, parte=parte, posicao=h['a'], categoria=h['cat'], subtipo=h['sub'], regras='+'.join(h['regras']),
                   classe=h['classe'], motivo=h['motivo'], trecho_antes=h['trecho'], ocorrencias_do_trecho_no_campo=texto.count(h['trecho']),
                   antes_unico=antes_unico(texto, h['a'], h['b']), arquivo_linha=ref)
        linhas_csv.append(row)
        marcas_por_item.setdefault(iid, []).append(row)

for it in itens:
    arq = it['arquivo']
    registra(it['id'], 'reforco', it['lote'], it['leva'], 'enunciado', it['enunciado'], arq, lambda a, it=it, arq=arq: ('%s:%d' % (arq, it['l_enunciado']), 'enunciado'), None)
    j1 = it['j1']
    registra(it['id'], 'reforco', it['lote'], it['leva'], 'justificativa', it['justificativa'], arq,
             lambda a, it=it, arq=arq, n1=len(j1): (('%s:%d' % (arq, it['l_j1']), 'linha 1') if a < n1 else ('%s:%d' % (arq, it['l_j2']), 'linha 2')), None)
for d in banco:
    iid = d['id']
    for campo, col in (('enunciado', 'texto_integral'), ('comando', 'texto_comando'), ('textoBase', 'texto_base')):
        if d[col]:
            registra(iid, 'banco', 'BANCO', '', campo, d[col], 'banco/banco.csv', lambda a, d=d: ('banco/banco.csv:%d' % d['_linha'], campo), None)

# ---------------------------------------------------------------- saidas
def grava(nome, obj):
    open(os.path.join(OUT, nome), 'wb').write((json.dumps(obj, ensure_ascii=False, indent=1) + '\n').encode('utf-8'))

bruto = [{k: it[k] for k in ('id', 'lote', 'leva', 'itemEdital', 'gabarito', 'aderencia', 'enunciado', 'j1', 'j2', 'justificativa')} for it in itens]
grava('reforco_bruto.json', bruto)
CAMPOS = ['id_ocorrencia', 'item', 'origem', 'lote', 'leva', 'campo', 'parte', 'posicao', 'categoria', 'subtipo', 'regras', 'classe', 'motivo', 'trecho_antes', 'ocorrencias_do_trecho_no_campo', 'antes_unico', 'arquivo_linha']
grava('reforco_marcas.json', dict(campos=CAMPOS, por_item={k: v for k, v in marcas_por_item.items()}))
with open(os.path.join(SAIDA, 'T123_ocorrencias_DA.csv'), 'wb') as f:
    buf = io.StringIO(newline='')
    w = csv.DictWriter(buf, fieldnames=CAMPOS, delimiter=';', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
    w.writeheader(); [w.writerow(r) for r in linhas_csv]
    f.write(buf.getvalue().encode('utf-8'))

def cont(rows, chave): return collections.Counter(r[chave] for r in rows)
def itens_com(rows): return len({r['item'] for r in rows})
M = [r for r in linhas_csv if r['classe'] == 'MARCA']
CATN = collections.OrderedDict([('C01', 'lote/leva de producao'), ('C02', 'codigo de item / ponto'), ('C03', 'codigo de par, pegadinha, alerta'), ('C04', 'etiqueta entre colchetes'), ('C05', 'codigo de fonte, Anexo, url'),
    ('C06', 'mecanismo TC/IC/GI/AT, (C|E)n'), ('C07', 'QA, unidade, agente'), ('C08', 'producao, errata, fabrica, id de decisao'), ('C09', 'versao de producao'), ('C10', 'instrucao interna (moldura, cota, ficha, [TS], folha, PENDENTE, **...)')])
ex = collections.OrderedDict()
ex['criterios'] = crit
ex['shas_levas'] = shas
ex['banco_sha256_lf'] = bh
ex['ocorrencias'] = dict(total=len(linhas_csv), por_classe=dict(cont(linhas_csv, 'classe')),
                         MARCA_por_categoria={c: sum(1 for r in M if r['categoria'] == c) for c in CATN},
                         MARCA_por_origem=dict(cont(M, 'origem')), MARCA_reforco_por_lote={l: sum(1 for r in M if r['origem'] == 'reforco' and r['lote'] == l) for l in ('D1', 'D2', 'D3', 'D4')},
                         MARCA_reforco_por_leva={str(n): sum(1 for r in M if r['origem'] == 'reforco' and r['leva'] == n) for n in range(1, 9)},
                         itens_com_MARCA_reforco=itens_com([r for r in M if r['origem'] == 'reforco']), itens_com_MARCA_banco=itens_com([r for r in M if r['origem'] == 'banco']),
                         itens_com_MARCA_em_enunciado_reforco=itens_com([r for r in M if r['origem'] == 'reforco' and r['campo'] == 'enunciado']),
                         ids_reforco_com_marca=sorted({r['item'] for r in M if r['origem'] == 'reforco'}, key=lambda s: ids.index(s)))
grava('extracao_t123.json', ex)

o = ex['ocorrencias']
res = []
res.append('# T123_ocorrencias_DA_resumo.md — T-123 fase 1 — 2026-10-23 — gerado por gbq-csc\n')
res.append('Extracao por script (`python -I extrair_reforco_da.py`), leitura CRLF->LF, SHA-256 LF das 8 levas e de banco/banco.csv conferidos. Insumo da limpeza da GCB (D1, secao 3). Nada foi corrigido.\n')
res.append('Campos lidos: enunciado e justificativa (j1 + " " + j2) dos 238 de reforco; enunciado, comando e textoBase dos 36 de banco P1-DA. Regras: C-MARCAS (D1 8.1) + inventario T-108 (categorias C01-C10 da ORDEM C) + lista R de marcas_processo.py. Sobrepostos na mesma categoria sao fundidos. Classe: MARCA (limpar), VERIFICAR (decisao da GCB), FP (falso positivo).\n')
res.append('## Totais\n')
res.append('- Ocorrencias: %d (%s).' % (o['total'], ', '.join('%s %d' % kv for kv in sorted(o['por_classe'].items()))))
res.append('- Itens de reforco com ao menos 1 MARCA: %d de 238 (a D1 estimou 85 com padrao mais largo). Em enunciado: %d.' % (o['itens_com_MARCA_reforco'], o['itens_com_MARCA_em_enunciado_reforco']))
res.append('- Itens de banco com MARCA: %d de 36.\n' % o['itens_com_MARCA_banco'])
res.append('## MARCA por categoria\n\n| Categoria | Descricao | Ocorrencias | Reforco | Banco |\n|---|---|--:|--:|--:|')
for c, dsc in CATN.items():
    res.append('| %s | %s | %d | %d | %d |' % (c, dsc, o['MARCA_por_categoria'][c], sum(1 for r in M if r['categoria'] == c and r['origem'] == 'reforco'), sum(1 for r in M if r['categoria'] == c and r['origem'] == 'banco')))
res.append('\n## MARCA por lote e por leva (reforco)\n\n| Lote | D1 | D2 | D3 | D4 |\n|---|--:|--:|--:|--:|\n| ocorrencias | %s |' % ' | '.join(str(o['MARCA_reforco_por_lote'][l]) for l in ('D1', 'D2', 'D3', 'D4')))
res.append('\n| Leva | ' + ' | '.join(str(n) for n in range(1, 9)) + ' |\n|---|' + '--:|' * 8 + '\n| ocorrencias | ' + ' | '.join(str(o['MARCA_reforco_por_leva'][str(n)]) for n in range(1, 9)) + ' |')
res.append('\n## Subtipos de MARCA (reforco e banco)\n\n| Categoria | Subtipo | n |\n|---|---|--:|')
for (c, s), n in sorted(collections.Counter((r['categoria'], r['subtipo']) for r in M).items()): res.append('| %s | %s | %d |' % (c, s, n))
res.append('\n## Ids de reforco com MARCA (%d)\n\n%s\n' % (len(o['ids_reforco_com_marca']), ', '.join(o['ids_reforco_com_marca'])))
res.append('## Conferencias\n')
res.append('- 238 ids unicos; C/E %s; parciais %s; erratas AJ-E1, AJ-L2-E1, AJ-L7-E1 com antes 1x / depois 0x antes de aplicar.' % (crit['C_E']['obtido'], crit['parciais']['obtido']))
res.append('- Colunas do CSV (";" UTF-8 LF): ' + ', '.join(CAMPOS) + '. `antes_unico` = menor trecho em torno da ocorrencia que ocorre 1 vez no campo (para a coluna `antes` das substituicoes).')
open(os.path.join(SAIDA, 'T123_ocorrencias_DA_resumo.md'), 'wb').write(('\n'.join(res) + '\n').encode('utf-8'))
print(json.dumps(ex['ocorrencias'], ensure_ascii=False, indent=1))
print(json.dumps({k: v for k, v in crit.items() if k not in ('por_leva', 'por_lote')}, ensure_ascii=False))
print('por_leva ok:', all(v['ok'] for v in crit['por_leva'].values()), 'por_lote ok:', all(v['ok'] for v in crit['por_lote'].values()))
