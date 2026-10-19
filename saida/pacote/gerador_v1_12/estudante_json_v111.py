# -*- coding: utf-8 -*-
"""T-108 (gerador_v1_11; cópia do estudante_json.py da v1.10 com as mudanças da D1 da GBQ, saida/pacote/T108_D1_pacote_M2_2026-10-18.md, seção 1.6: a fonte é out/pacote.json já limpo, sem o `interno`; as listas de deleção herdadas passam a verificação residual; `mesmas_chaves` e `mascara` não veem o `interno`) — T-104 (v1.10; cópia do estudante_json.py da T-94 com as mudanças da D1 da GBQ, saida/pacote/T104_D1_v1_10_2026-10-18.md, seções 3 e 4: nome e data de config_v110,
os 225 itens novos só com as deleções fechadas de reforco_marcas_v110.py, e o campo "nucleo" (nucleo.py) em todos os itens) — T-94 (v1.9; cópia do estudante_json.py da T-81 com as mudanças da D1 da GBQ, saida/pacote/T94_D1_v1_9_2026-10-18.md, seção 3: nome, data, e os 48 itens de reforço
só com as deleções fechadas de reforco_marcas.py) — T-81 (v1.8) — gera out/pacote_estudante.json (v1.8-E) a partir de out/pacote.json (fonte única), conforme a D1 da GBQ (saida/pacote/T81_D1_escopo_v1_8_2026-10-17.md, seções 2, 3 e 6.1).
Só deleção (estudante_marcas.strip_text, mais as 3 regras fechadas da seção 2.2: nota, url e aviso do SIM-0), com as exceções fechadas CAIXA e REALINHA da v1.7 e a fusão 1-C/4-C/5-C
(única inserção de texto: o separador mandado pela D-T12-V13 (c)). Falha (sys.exit(1)) se qualquer asserção de 6.1 (a) a (f) não valer.
Saídas: out/pacote_estudante.json, out/estudante_json.json (contagens por regra e por campo, casamentos de R, termos fora da lista) e, redirecionada pelo runner, out/estudante_json_stdout.txt."""
import collections, copy, json, os, re, sys
import estudante_marcas as em
import estudante_gen as gen
import estudante_fidelidade as F
import marcas_processo as mp
import reforco_marcas as rm
import reforco_marcas_v110 as rm2
import config_v110 as cfg0
import config_v111 as cfg
import nucleo as NU
import marcas_x_v110 as mx
import marcas_x_v111 as mx1

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'out', 'pacote.json')
DST = os.path.join(HERE, 'out', 'pacote_estudante.json')
REL = os.path.join(HERE, 'out', 'estudante_json.json')
NOME_E = cfg.NOME_E
GERADO_EM = cfg.GERADO_EM
REF_IDS2 = list(json.load(open(os.path.join(HERE, 'out', 'stats_%s.json' % cfg.TAG), encoding='utf-8'))['reforco'])      # T-104: os 225 ids novos
ESC_REF = 'REFORCO'      # escopo próprio dos itens de reforço da onda 1 (reforco_marcas.strip_reforco)
ESC_REF2 = 'REFORCO_V110'      # T-104: escopo dos 225 itens novos (reforco_marcas_v110.strip_reforco)
NOTA_DEL = ' (D-LEI-15352)'
AVISO_ANTES, AVISO_DEPOIS = '(D-ADERENCIA: parcial só em diagnóstico)', '(parcial só em diagnóstico)'
TOPO = ['versao', 'geradoEm', 'nome', 'edital', 'itens', 'simulados', 'lotes', 'discursivas']
ORDEM_LOTES = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6A', 'L6B']
FALHAS = []
HITS_CAMPO = []      # (campo, regras que casaram) no pacote.json já limpo
RESIDUAL_EXTRA = collections.OrderedDict()      # casamentos das regras fixas (nota, aviso) no pacote.json já limpo

def falha(msg):
    FALHAS.append(msg)
    print('FALHA:', msg)

def asserta(ok, msg):
    if not ok:
        falha(msg)

raw = open(SRC, 'rb').read().decode('utf-8')
P_INT = json.loads(raw, object_pairs_hook=collections.OrderedDict)
asserta(json.dumps(P_INT, ensure_ascii=False, indent=1) + '\n' == raw, 'out/pacote.json não é a serialização canônica (indent=1, ensure_ascii=False, newline final)')
asserta(P_INT['geradoEm'] == GERADO_EM and P_INT['nome'] == cfg.NOME, 'geradoEm/nome do pacote.json != config_v111')


def tira_interno(o):
    """Seção 1.6, passo 2, ponto 1: o `interno` é retirado de todos os objetos antes de qualquer outra regra (só existe no pacote.json)."""
    o = copy.deepcopy(o)
    n = 0
    for lista in ('itens', 'lotes', 'simulados', 'discursivas'):
        for x in o[lista]:
            if 'interno' in x:
                del x['interno']; n += 1
    return o, n


P, N_INTERNO = tira_interno(P_INT)

# ------------------------------------------------------------------ passagem de deleção
E = copy.deepcopy(P)
REGRAS = collections.Counter()            # tipo de regra -> ocorrências
POR_CAMPO = collections.OrderedDict()     # categoria de campo -> {'campos': n de campos tocados, 'remocoes': n, 'regras': Counter}
OPS = []                                  # (categoria, caminho, escopo, antes, depois)
em.CAIXA_HITS.clear(); em.REALINHA_HITS.clear()

def reg(cat):
    return POR_CAMPO.setdefault(cat, {'campos': 0, 'remocoes': 0, 'regras': collections.Counter()})

def S(cat, caminho, texto, escopo):
    """aplica strip_text com o escopo de origem e registra a operação."""
    c = collections.Counter()
    novo = rm.strip_reforco(texto, c, caminho) if escopo == ESC_REF else rm2.strip_reforco(texto, c, caminho) if escopo == ESC_REF2 else em.strip_text(texto, c, escopo)
    r = reg(cat)
    if novo != texto:
        r['campos'] += 1
    r['remocoes'] += sum(c.values()); r['regras'].update(c); REGRAS.update(c)
    if c:
        HITS_CAMPO.append((caminho, dict(c)))
    OPS.append((cat, caminho, escopo, texto, texto))      # D1 pré-FINAL 2.2: as regras herdadas só contam; o texto do -E é o do pacote.json
    return texto

# lotes (escopo = <lid>_estudo.md, o do lote de ORIGEM na v1.7)
for L in E['lotes']:
    lid = L['id']; esc = '%s_estudo.md' % lid; b = 'lotes[%s]' % lid
    L['resumo'] = S('lotes[].resumo', b + '.resumo', L['resumo'], esc)
    L['curso'] = S('lotes[].curso', b + '.curso', L['curso'], esc)
    for k, p in enumerate(L['pares']):
        for f in ('a', 'b', 'como'):
            p[f] = S('lotes[].pares[].' + f, '%s.pares[%d].%s' % (b, k, f), p[f], esc)
    for k, g in enumerate(L['pegadinhas']):
        for f in ('rotulo', 'texto'):
            g[f] = S('lotes[].pegadinhas[].' + f, '%s.pegadinhas[%d].%s' % (b, k, f), g[f], esc)

# itens
REF_IDS = [i['id'] for i in E['itens'][:334] if '-R' in i['id']]       # T-104: os 48 da onda 1 (v1.9)
assert len(REF_IDS) == 48 and not set(REF_IDS) & set(REF_IDS2) and [i['id'] for i in E['itens'][334:]] == REF_IDS2
n_nota = 0
for it in E['itens']:
    if it['rotulo'] == 'AUTORAL':
        if it['justificativa'] and it['id'] in REF_IDS:      # T-94: reforço da onda 1 (lista fechada de reforco_marcas.py)
            it['justificativa'] = S('itens[].justificativa (AUTORAL, reforço)', 'itens[%s].justificativa' % it['id'], it['justificativa'], ESC_REF)
        elif it['justificativa'] and it['id'] in REF_IDS2:      # T-104: os 225 novos (lista fechada de reforco_marcas_v110.py)
            it['justificativa'] = S('itens[].justificativa (AUTORAL, reforço v1.10)', 'itens[%s].justificativa' % it['id'], it['justificativa'], ESC_REF2)
        elif it['justificativa']:
            esc = gen.lote_of(it['id']) + '_gabarito.md'
            it['justificativa'] = S('itens[].justificativa (AUTORAL)', 'itens[%s].justificativa' % it['id'], it['justificativa'], esc)
        asserta(it['url'] != '', '%s: url AUTORAL já vazia' % it['id'])
        it['url'] = ''
        reg('itens[].url (AUTORAL)')['campos'] += 1; reg('itens[].url (AUTORAL)')['remocoes'] += 1; reg('itens[].url (AUTORAL)')['regras'].update(['url AUTORAL (valor inteiro apagado)'])
        REGRAS.update(['url AUTORAL (valor inteiro apagado)'])
    else:
        asserta(it['justificativa'] == '', '%s: justificativa de item de banco não está vazia' % it['id'])
    if 'nota' in it and NOTA_DEL in it['nota']:
        n_nota += it['nota'].count(NOTA_DEL)
RESIDUAL_EXTRA['nota (D-LEI-15352)'] = n_nota

# simulados: só SIM-0.avisos[0]
for s in E['simulados']:
    if s['id'] == 'SIM-0':
        RESIDUAL_EXTRA['aviso SIM-0 (D-ADERENCIA)'] = s['avisos'][0].count(AVISO_ANTES)

# discursivas
for d in E['discursivas']:
    b = 'discursivas[%s]' % d['id']
    d['comando'] = S('discursivas[].comando', b + '.comando', d['comando'], 'DISCURSIVAS.md')
    d['padrao'] = S('discursivas[].padrao', b + '.padrao', d['padrao'], 'DISCURSIVAS_padrao.md')
    for a in d['aspectos']:
        a['texto'] = S('discursivas[].aspectos[].texto', '%s.aspectos[%d].texto' % (b, a['n']), a['texto'], 'DISCURSIVAS_padrao.md')
    for q in d['quesitos']:
        q['nome'] = S('discursivas[].quesitos[].nome', '%s.quesitos[%s].nome' % (b, q['id']), q['nome'], 'DISCURSIVAS_padrao.md')
        q['conceitos'] = [S('discursivas[].quesitos[].conceitos[]', '%s.quesitos[%s].conceitos[%d]' % (b, q['id'], k), c, 'DISCURSIVAS_padrao.md') for k, c in enumerate(q['conceitos'])]

SNAP_CAIXA, SNAP_REALINHA = dict(em.CAIXA_HITS), dict(em.REALINHA_HITS)

# ------------------------------------------------------------------ T-104: campo "nucleo" (D-REFORCO-2; nucleo.py), em todo item, depois de todos os campos
NUC, NUC_REL, NUC_K = NU.calcula(P)
for it in E['itens']:
    it['nucleo'] = NUC[it['id']]

def sem_nucleo(o):
    o = copy.deepcopy(o)
    for it in o['itens']:
        it.pop('nucleo', None)
    return o

# ------------------------------------------------------------------ fusão 1-C/4-C/5-C (seção 3.1)
por_id = {L['id']: L for L in E['lotes']}
for lid, cid in gen.COMPL.items():
    L, C = por_id[lid], por_id[cid]
    asserta(set(C['itensEdital']) <= set(L['itensEdital']), 'itensEdital de %s não está contido no de %s' % (cid, lid))
    asserta(not any(l.startswith('## ') for l in C['curso'].split('\n')), 'o curso de %s tem linha que começa por "## "' % cid)
    if lid == 'L1':
        asserta(C['curso'] != '' and len(C['pegadinhas']) == 4 and not C['resumo'] and not C['pares'], 'L1C: esperado curso não vazio, 4 pegadinhas, resumo e pares vazios')
        L['curso'] = L['curso'] + gen.SEP_COMPL + C['curso']
        L['pegadinhas'] = L['pegadinhas'] + C['pegadinhas']
    else:
        asserta(C['curso'] == '' and not C['resumo'] and not C['pares'] and not C['pegadinhas'], '%s: curso, resumo, pares e pegadinhas devem estar vazios' % cid)
E['lotes'] = [L for L in E['lotes'] if L['id'] not in gen.FUSAO]
asserta([L['id'] for L in E['lotes']] == ORDEM_LOTES, 'ordem dos lotes: %s' % [L['id'] for L in E['lotes']])

saida = collections.OrderedDict([('versao', P['versao']), ('geradoEm', P['geradoEm']), ('nome', NOME_E), ('edital', E['edital']), ('itens', E['itens']),
                                 ('simulados', E['simulados']), ('lotes', E['lotes']), ('discursivas', E['discursivas'])])
txt = json.dumps(saida, ensure_ascii=False, indent=1) + '\n'

# ------------------------------------------------------------------ (a) estrutura
asserta(list(saida.keys()) == TOPO, '(a) chaves de topo: %s' % list(saida.keys()))
asserta(saida['versao'] == 1 and saida['geradoEm'] == GERADO_EM and saida['nome'] == NOME_E, '(a) versao/geradoEm/nome')

# P_f: o pacote.json com a fusão aplicada SEM deleção (referência para estrutura e identidade)
Pf = copy.deepcopy(P)
pf = {L['id']: L for L in Pf['lotes']}
for lid, cid in gen.COMPL.items():
    if pf[cid]['curso']:
        pf[lid]['curso'] = pf[lid]['curso'] + gen.SEP_COMPL + pf[cid]['curso']
    pf[lid]['pegadinhas'] = pf[lid]['pegadinhas'] + pf[cid]['pegadinhas']
Pf['lotes'] = [L for L in Pf['lotes'] if L['id'] not in gen.FUSAO]

def mesmas_chaves(a, b, caminho=''):
    if isinstance(a, dict):
        if not isinstance(b, dict) or list(a.keys()) != list(b.keys()):
            return [caminho or '$']
        return [x for k in a for x in mesmas_chaves(a[k], b[k], caminho + '.' + k)]
    if isinstance(a, list):
        if not isinstance(b, list) or len(a) != len(b):
            return [caminho + ' (tamanho)']
        return [x for i, (u, v) in enumerate(zip(a, b)) for x in mesmas_chaves(u, v, '%s[%d]' % (caminho, i))]
    return []
asserta(all(list(it.keys())[-1] == 'nucleo' and isinstance(it['nucleo'], bool) for it in saida['itens']), '(a) T-104: "nucleo" booleano e último campo de todo item')
asserta(not any('interno' in x for l_ in ('itens', 'lotes', 'simulados', 'discursivas') for x in saida[l_]) and N_INTERNO > 0, '(a) T-108: `interno` ausente de todo objeto do -E (e presente no pacote.json)')
dk = mesmas_chaves(Pf, sem_nucleo(saida))
asserta(not dk, '(a) objetos com chaves/ordem diferentes das do pacote.json: %s' % dk[:5])

# ------------------------------------------------------------------ (b) identidade fora da lista da 2.2
def mascara(o):
    """zera os campos da lista da 2.2 (deleções), para comparar o resto."""
    o = copy.deepcopy(o)
    for L in o['lotes']:
        L['resumo'] = L['curso'] = ''
        for p in L['pares']:
            p['a'] = p['b'] = p['como'] = ''
        for g in L['pegadinhas']:
            g['rotulo'] = g['texto'] = ''
    for it in o['itens']:
        it['justificativa'] = '' if it['rotulo'] == 'AUTORAL' else it['justificativa']
        if 'nota' in it: it['nota'] = ''
        if it['rotulo'] == 'AUTORAL': it['url'] = ''
    for s in o['simulados']:
        if s['id'] == 'SIM-0': s['avisos'][0] = ''
    for d in o['discursivas']:
        d['comando'] = d['padrao'] = ''
        for a in d['aspectos']: a['texto'] = ''
        for q in d['quesitos']:
            q['nome'] = ''; q['conceitos'] = ['' for _ in q['conceitos']]
    o['nome'] = ''
    return o
asserta(json.dumps(mascara(Pf), ensure_ascii=False) == json.dumps(mascara(sem_nucleo(saida)), ensure_ascii=False), '(b) há diferença fora dos campos da lista da 2.2 (edital, ids, ordem dos itens, enunciado, comando, textoBase, gabarito, itemEdital, aderencia, volatil, url de banco, simulados, itensEdital, legendaMecanismo, pares[].id, valores)')
asserta(saida['edital'] == P['edital'] and [i['id'] for i in saida['itens']] == [i['id'] for i in P['itens']], '(b) edital ou ordem dos itens')
for campo in ('enunciado', 'comando', 'comandoOriginal', 'textoBase', 'gabarito', 'itemEdital', 'aderencia', 'volatil', 'rotulo', 'certame', 'cargo', 'ano', 'numero'):
    asserta(all(a.get(campo) == b.get(campo) and (campo in a) == (campo in b) for a, b in zip(P['itens'], saida['itens'])), '(b) item: campo %s difere' % campo)
asserta(all(a['url'] == b['url'] for a, b in zip(P['itens'], saida['itens']) if a['rotulo'] != 'AUTORAL'), '(b) url dos itens de banco difere')
asserta(sum(1 for b in saida['itens'] if b['rotulo'] == 'AUTORAL' and b['url'] == '') == 453 + cfg0.E_L2R131, '(b) url vazia em 453 AUTORAL (180 + 48 da onda 1 + 225 da v1.10; +1 com o L2-R131)')

# ------------------------------------------------------------------ (c) cada campo = strip_text com o escopo de origem; só deleção (subsequência), salvo CAIXA, REALINHA e fusão
casos_antes = len(F.CASE_LOG); realinha_antes = len(F.REALINHA_LOG)
ncomp = 0
for cat, caminho, esc, antes, depois in OPS:
    ncomp += 1
    c = collections.Counter()
    esperado = rm.strip_reforco(antes, c) if esc == ESC_REF else rm2.strip_reforco(antes, c) if esc == ESC_REF2 else em.strip_text(antes, c, esc)           # segunda aplicação, independente do valor guardado
    if depois != antes:
        falha('(c) %s: o texto do -E difere do do pacote.json (as regras herdadas só contam)' % caminho)
    bad = F.only_deletions(antes, depois, esc, caminho)
    if bad:
        falha('(c) %s: não é só deleção (%s)' % (caminho, bad[:2]))
em.CAIXA_HITS.clear(); em.CAIXA_HITS.update(SNAP_CAIXA); em.REALINHA_HITS.clear(); em.REALINHA_HITS.update(SNAP_REALINHA)      # a reaplicação não conta nas exceções
n_caixa_c = len(F.CASE_LOG) - casos_antes

# ------------------------------------------------------------------ (d) CAIXA e REALINHA: na v1.10 eram 8/8 e 2/2, exatamente 1 cada; com o pacote.json limpo viram verificação residual (informativa)
CAIXA_REAL = [(e_, a_[:40], SNAP_CAIXA.get((e_, a_), 0)) for e_, a_, d_ in em.CAIXA]
REALINHA_REAL = [(e_, a_[:40], SNAP_REALINHA.get((e_, a_), 0)) for e_, a_, d_ in em.REALINHA]

# ------------------------------------------------------------------ (e) varredura R
# T-108 (decisão pendente da GBQ, registrada no relatório do ensaio): na v1.10 o "verificado em dd/mm/aaaa" era carimbo de processo e a edição o retirava; na M2 ele é texto de fonte
# ("nome, verificado em dd/mm/aaaa"; seção 1.4, ponto 8) e fica. A varredura R deixa de tratar esse literal como PROCESSO e passa a contá-lo; o resto de "carimbo" continua.
VERIF_RX = re.compile(r'(?<![\w])(?:re)?verificad[oa]s? em \d{1,2}/\d{1,2}/\d{4}|\(leitura de \d{1,2}/\d{1,2}/\d{4}\)')
mp.R['carimbo'] = re.compile(r'conferid[oa]s? pel[ao]')
strings = list(mp.walk(saida))
N_VERIF_EM = sum(len(VERIF_RX.findall(t)) for _, t in strings)
res = mp.classifica(strings, mp.X + mx.X_V110 + mx1.X_V111, [y for y in mp.Y if y[0] != 'Y1'])      # T-104: X9–X14 (marcas_x_v110.py)
CONT_DIF = [f for f in res['falhas'] if ': contagem real' in f]      # X/Y com contagem diferente da v1.10: o texto do campo foi editado pela tabela (informativo)
for f in res['falhas']:
    if f not in CONT_DIF:
        falha('(e) ' + f)
if res['processo']:
    for c_, lab, g, ctx in res['processo']:
        falha('(e) PROCESSO fora de X/Y: %s | %s | %r | …%s…' % (c_, lab, g, ctx))
n_cont = sum(v for k, v in res['contagem'].items() if k.startswith('X')); n_dur = sum(v for k, v in res['contagem'].items() if k.startswith('Y'))
ACHADOS_XY = len(res['todos'])      # v1.10: 15 (X1–X14, Y1); informativo
fora = mp.fora_da_lista(strings)

# ------------------------------------------------------------------ (f) fusão
asserta([L['id'] for L in saida['lotes']] == ORDEM_LOTES and 'L1C' not in {L['id'] for L in saida['lotes']}, '(f) lotes')
cont_antes = collections.Counter(gen.lote_of(i['id']) for i in P['itens'] if i['rotulo'] == 'AUTORAL')
cont_depois = collections.Counter(gen.lote_fund(i['id']) for i in saida['itens'] if i['rotulo'] == 'AUTORAL')
asserta(cont_antes == collections.Counter({'L1': 150, 'L1C': 10, 'L2': 159 + cfg0.E_L2R131, 'L3': 41, 'L4': 20, 'L4C': 10, 'L5': 20, 'L5C': 10, 'L6A': 16, 'L6B': 17}), '(f) contagem por lote de origem (pacote.json v1.10): %s' % dict(cont_antes))
asserta(cont_depois == collections.Counter({'L1': 160, 'L2': 159 + cfg0.E_L2R131, 'L3': 41, 'L4': 30, 'L5': 30, 'L6A': 16, 'L6B': 17}), '(f) contagem v1.10-E: %s' % dict(cont_depois))
# (g) T-94/T-104: as deleções das listas fechadas do reforço eram conferidas contra ESPERADO; com o pacote.json limpo são verificação residual (informativas)
asserta(all(k[len('itens['):-len('].justificativa')] in REF_IDS + REF_IDS2 for k, _ in list(rm.HITS) + list(rm2.HITS)), '(g) deleção das listas fechadas fora dos itens de reforço')
L1s = {L['id']: L for L in saida['lotes']}['L1']
L1o = {L['id']: L for L in P['lotes']}
op = {c: d for _, c, _, _, d in OPS}
asserta(L1s['curso'] == op['lotes[L1].curso'] + gen.SEP_COMPL + op['lotes[L1C].curso'] and L1s['curso'].count(gen.SEP_COMPL) == 1, '(f) L1.curso deve ser strip(L1.curso, "L1_estudo.md") + separador + strip(L1C.curso, "L1C_estudo.md"), com 1 separador')
asserta(len(L1s['pegadinhas']) == len(L1o['L1']['pegadinhas']) + len(L1o['L1C']['pegadinhas']) == 23, '(f) pegadinhas do L1: %d' % len(L1s['pegadinhas']))
for lid in ('L4', 'L5'):
    asserta(list(L1o[lid].keys()) == list({L['id']: L for L in saida['lotes']}[lid].keys()), '(f) %s: chaves' % lid)
asserta(all(gen.lote_fund(i['id']) in ORDEM_LOTES for i in saida['itens'] if i['rotulo'] == 'AUTORAL'), '(f) todo item AUTORAL se associa a um lote da lista pelo prefixo')

# ------------------------------------------------------------------ verificação residual (seção 1.6, passo 2, ponto 2): casamento das regras herdadas sobre o pacote.json limpo
RES = collections.OrderedDict((k, v) for k, v in REGRAS.items() if not k.startswith('url AUTORAL') and not k.startswith('caixa'))      # url AUTORAL e caixa (ajuste de maiúscula depois de deleção) não são marcas
for k, v in RESIDUAL_EXTRA.items():
    if v:
        RES[k] = v
RES_LIQ = sum(max(0, v - cfg.EXCECOES_RESIDUAL.get(k, 0)) for k, v in RES.items())
if cfg.FINAL:
    asserta(RES_LIQ == 0, 'verificação residual: %d casamento(s) das listas de deleção herdadas no pacote.json limpo (%s)' % (RES_LIQ, dict(RES)))
    asserta(not res['processo'], 'varredura R: PROCESSO residual')

# C-9f: cada campo de texto exibido do -E é igual ao do pacote.json sem `interno` (fora a fusão 1-C/4-C/5-C, já em Pf, e a `url` vazia dos AUTORAL)
Pu = sem_nucleo(copy.deepcopy(Pf))
for it_ in Pu['itens']:
    if it_['rotulo'] == 'AUTORAL':
        it_['url'] = ''
Pu['nome'] = NOME_E
asserta(json.dumps(Pu, ensure_ascii=False) == json.dumps(sem_nucleo(saida), ensure_ascii=False), 'C-9f: o -E difere do pacote.json sem `interno` fora da fusão 1-C/4-C/5-C e da url vazia')
# lista fechada do residual: mesmo conjunto de regras, mesmos números e mesmos campos (outro campo ou outro número = falha)
if cfg.FINAL:
    asserta(dict(RES) == dict(cfg.EXCECOES_RESIDUAL), 'C-8: residual %s != lista fechada %s' % (dict(RES), dict(cfg.EXCECOES_RESIDUAL)))
    _campos = collections.defaultdict(set)
    for _c, _d in HITS_CAMPO:
        for _r in _d:
            if _r in cfg.EXCECOES_RESIDUAL:
                _campos[_r].add(_c)
    asserta({k: sorted(v) for k, v in _campos.items()} == {k: sorted(v) for k, v in cfg.EXCECOES_RESIDUAL_CAMPOS.items()}, 'C-8: campos do residual %s != %s' % ({k: sorted(v) for k, v in _campos.items()}, cfg.EXCECOES_RESIDUAL_CAMPOS))

# ------------------------------------------------------------------ saídas
if not FALHAS:
    with open(DST, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(txt)
rel = collections.OrderedDict()
rel['arquivo'] = 'out/pacote_estudante.json'
rel['bytes'] = len(txt.encode('utf-8'))
rel['regras'] = collections.OrderedDict(sorted(REGRAS.items(), key=lambda kv: (-kv[1], kv[0])))
rel['total_remocoes'] = sum(REGRAS.values())
rel['por_campo'] = collections.OrderedDict((k, {'campos_alterados': v['campos'], 'remocoes': v['remocoes'], 'regras': dict(v['regras'])}) for k, v in POR_CAMPO.items())
rel['campos_comparados_so_delecao'] = ncomp
rel['caixa'] = {'pares': len(em.CAIXA), 'ocorrencias': sum(SNAP_CAIXA.values())}
rel['realinha'] = {'pares': len(em.REALINHA), 'ocorrencias': sum(SNAP_REALINHA.values())}
rel['casamentos_R'] = [dict(campo=c_, rotulo=lab, casamento=g, contexto=ctx, destino=d) for c_, lab, g, ctx, d in res['todos']]
rel['contagem_X_Y'] = dict(res['contagem'])
rel['processo'] = len(res['processo'])
rel['termos_fora_da_lista'] = dict(fora)
rel['reforco_delecoes'] = {'%s | %s' % k: v for k, v in sorted(rm.HITS.items())}
rel['reforco_v110_delecoes'] = {'%s | %s' % k: v for k, v in sorted(rm2.HITS.items())}
rel['nucleo'] = collections.OrderedDict((f, dict(itens=v['itens'], nucleo=v['nucleo'], ids_nucleo=v['ids_nucleo'], parciais_no_nucleo=v['parciais_no_nucleo'], atos=v['atos'])) for f, v in NUC_REL.items())
rel['nucleo_total'] = sum(1 for v in NUC.values() if v)
rel['itens_por_lote'] = {'origem_v1_10': dict(cont_antes), 'depois_v1_10_E': dict(cont_depois), 'banco': sum(1 for i in P['itens'] if i['rotulo'] != 'AUTORAL')}
rel['verificacao_residual'] = collections.OrderedDict(modo='FINAL' if cfg.FINAL else 'ENSAIO', regras_herdadas=dict(RES), campos_com_casamento=[[c_, d_] for c_, d_ in HITS_CAMPO], total=sum(RES.values()), liquido=RES_LIQ, excecoes=dict(cfg.EXCECOES_RESIDUAL),
                                                     caixa=[list(x) for x in CAIXA_REAL], realinha=[list(x) for x in REALINHA_REAL], achados_X_Y=ACHADOS_XY, verificado_em_mantidos=N_VERIF_EM, XY_contagem_diferente=CONT_DIF, X=n_cont, Y=n_dur,
                                                     reforco_hits=sum(rm.HITS.values()), reforco_v110_hits=sum(rm2.HITS.values()), objetos_com_interno_no_pacote=N_INTERNO)
rel['falhas'] = FALHAS
with open(REL, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(rel, fh, ensure_ascii=False, indent=1)
    fh.write('\n')
print('pacote_estudante.json: %d bytes; %d remoções em %d regras; %d campos comparados (só deleção)' % (rel['bytes'], rel['total_remocoes'], len(REGRAS), ncomp))
print('CAIXA %d/%d, REALINHA %d/%d (exatamente 1 cada)' % (sum(SNAP_CAIXA.values()), len(em.CAIXA), sum(SNAP_REALINHA.values()), len(em.REALINHA)))
print('varredura R: %d casamentos (X %d, Y %d), %d de processo' % (len(res['todos']), n_cont, n_dur, len(res['processo'])))
for c_, lab, g, ctx, d in res['todos']:
    print('   %s | %s | %r | %s' % (d, c_, g, ctx))
print('termos fora da lista:', dict(fora))
print('nucleo: %d itens true em %d folhas' % (rel['nucleo_total'], len(NUC_REL)))
print('itens por lote (origem -> v1.10-E):', dict(sorted(cont_antes.items())), '->', dict(sorted(cont_depois.items())))
print('verificação residual (%s): %d casamento(s) das regras herdadas no pacote.json limpo (líquido %d); varredura R: %d de processo fora de X/Y' % (rel['verificacao_residual']['modo'], sum(RES.values()), RES_LIQ, len(res['processo'])))
print('%d falhas' % len(FALHAS))
sys.exit(1 if FALHAS else 0)
