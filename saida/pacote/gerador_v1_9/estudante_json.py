# -*- coding: utf-8 -*-
"""T-81 (v1.8) — gera out/pacote_estudante.json (v1.8-E) a partir de out/pacote.json (fonte única), conforme a D1 da GBQ (saida/pacote/T81_D1_escopo_v1_8_2026-10-17.md, seções 2, 3 e 6.1).
Só deleção (estudante_marcas.strip_text, mais as 3 regras fechadas da seção 2.2: nota, url e aviso do SIM-0), com as exceções fechadas CAIXA e REALINHA da v1.7 e a fusão 1-C/4-C/5-C
(única inserção de texto: o separador mandado pela D-T12-V13 (c)). Falha (sys.exit(1)) se qualquer asserção de 6.1 (a) a (f) não valer.
Saídas: out/pacote_estudante.json, out/estudante_json.json (contagens por regra e por campo, casamentos de R, termos fora da lista) e, redirecionada pelo runner, out/estudante_json_stdout.txt."""
import collections, copy, json, os, sys
import estudante_marcas as em
import estudante_gen as gen
import estudante_fidelidade as F
import marcas_processo as mp

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'out', 'pacote.json')
DST = os.path.join(HERE, 'out', 'pacote_estudante.json')
REL = os.path.join(HERE, 'out', 'estudante_json.json')
NOME_E = 'Câmara 2026 — pacote do estudante (v1.8-E)'
GERADO_EM = '2026-10-17'
NOTA_DEL = ' (D-LEI-15352)'
AVISO_ANTES, AVISO_DEPOIS = '(D-ADERENCIA: parcial só em diagnóstico)', '(parcial só em diagnóstico)'
TOPO = ['versao', 'geradoEm', 'nome', 'edital', 'itens', 'simulados', 'lotes', 'discursivas']
ORDEM_LOTES = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6A', 'L6B']
FALHAS = []

def falha(msg):
    FALHAS.append(msg)
    print('FALHA:', msg)

def asserta(ok, msg):
    if not ok:
        falha(msg)

raw = open(SRC, 'rb').read().decode('utf-8')
P = json.loads(raw, object_pairs_hook=collections.OrderedDict)
asserta(json.dumps(P, ensure_ascii=False, indent=1) + '\n' == raw, 'out/pacote.json não é a serialização canônica (indent=1, ensure_ascii=False, newline final)')
asserta(P['geradoEm'] == GERADO_EM, 'geradoEm do pacote.json != %s' % GERADO_EM)

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
    novo = em.strip_text(texto, c, escopo)
    r = reg(cat)
    if novo != texto:
        r['campos'] += 1
    r['remocoes'] += sum(c.values()); r['regras'].update(c); REGRAS.update(c)
    OPS.append((cat, caminho, escopo, texto, novo))
    return novo

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
n_nota = 0
for it in E['itens']:
    if it['rotulo'] == 'AUTORAL':
        if it['justificativa']:
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
        asserta(it['nota'].count(NOTA_DEL) == 1 and it['id'] == 'BQ-0003', 'nota com %r fora de BQ-0003 ou repetida (%s)' % (NOTA_DEL, it['id']))
        it['nota'] = it['nota'].replace(NOTA_DEL, '')
        reg('itens[].nota')['campos'] += 1; reg('itens[].nota')['remocoes'] += 1; reg('itens[].nota')['regras'].update(['id de decisão na nota (D-LEI-15352)'])
        REGRAS.update(['id de decisão na nota (D-LEI-15352)'])
asserta(n_nota == 1, 'a deleção " (D-LEI-15352)" da nota deve ocorrer 1 vez (BQ-0003); ocorreu %d' % n_nota)

# simulados: só SIM-0.avisos[0]
for s in E['simulados']:
    if s['id'] == 'SIM-0':
        asserta(s['avisos'][0].count(AVISO_ANTES) == 1, 'SIM-0.avisos[0]: o trecho %r deve ocorrer 1 vez' % AVISO_ANTES)
        s['avisos'][0] = s['avisos'][0].replace(AVISO_ANTES, AVISO_DEPOIS)
        reg('simulados[SIM-0].avisos[0]')['campos'] += 1; reg('simulados[SIM-0].avisos[0]')['remocoes'] += 1
        reg('simulados[SIM-0].avisos[0]')['regras'].update(['D-ADERENCIA no aviso do SIM-0 (deleção literal única)'])
        REGRAS.update(['D-ADERENCIA no aviso do SIM-0 (deleção literal única)'])

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
dk = mesmas_chaves(Pf, saida)
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
asserta(json.dumps(mascara(Pf), ensure_ascii=False) == json.dumps(mascara(saida), ensure_ascii=False), '(b) há diferença fora dos campos da lista da 2.2 (edital, ids, ordem dos itens, enunciado, comando, textoBase, gabarito, itemEdital, aderencia, volatil, url de banco, simulados, itensEdital, legendaMecanismo, pares[].id, valores)')
asserta(saida['edital'] == P['edital'] and [i['id'] for i in saida['itens']] == [i['id'] for i in P['itens']], '(b) edital ou ordem dos itens')
for campo in ('enunciado', 'comando', 'comandoOriginal', 'textoBase', 'gabarito', 'itemEdital', 'aderencia', 'volatil', 'rotulo', 'certame', 'cargo', 'ano', 'numero'):
    asserta(all(a.get(campo) == b.get(campo) and (campo in a) == (campo in b) for a, b in zip(P['itens'], saida['itens'])), '(b) item: campo %s difere' % campo)
asserta(all(a['url'] == b['url'] for a, b in zip(P['itens'], saida['itens']) if a['rotulo'] != 'AUTORAL'), '(b) url dos itens de banco difere')
asserta(sum(1 for b in saida['itens'] if b['rotulo'] == 'AUTORAL' and b['url'] == '') == 180, '(b) url vazia em 180 AUTORAL')

# ------------------------------------------------------------------ (c) cada campo = strip_text com o escopo de origem; só deleção (subsequência), salvo CAIXA, REALINHA e fusão
casos_antes = len(F.CASE_LOG); realinha_antes = len(F.REALINHA_LOG)
ncomp = 0
for cat, caminho, esc, antes, depois in OPS:
    ncomp += 1
    c = collections.Counter()
    esperado = em.strip_text(antes, c, esc)           # segunda aplicação, independente do valor guardado
    if esperado != depois:
        falha('(c) %s: strip_text com escopo %s difere do valor gravado' % (caminho, esc))
    bad = F.only_deletions(antes, depois, esc, caminho)
    if bad:
        falha('(c) %s: não é só deleção (%s)' % (caminho, bad[:2]))
em.CAIXA_HITS.clear(); em.CAIXA_HITS.update(SNAP_CAIXA); em.REALINHA_HITS.clear(); em.REALINHA_HITS.update(SNAP_REALINHA)      # a reaplicação não conta nas exceções
n_caixa_c = len(F.CASE_LOG) - casos_antes

# ------------------------------------------------------------------ (d) CAIXA 8/8 e REALINHA 2/2, exatamente 1 cada
for esc, antes, depois in em.CAIXA:
    asserta(SNAP_CAIXA.get((esc, antes), 0) == 1, '(d) CAIXA %r ocorreu %d vez(es)' % (antes, SNAP_CAIXA.get((esc, antes), 0)))
for esc, antes, depois in em.REALINHA:
    asserta(SNAP_REALINHA.get((esc, antes), 0) == 1, '(d) REALINHA %r ocorreu %d vez(es)' % (antes[:40], SNAP_REALINHA.get((esc, antes), 0)))
asserta(len(em.CAIXA) == 8 and len(em.REALINHA) == 2 and n_caixa_c == 8 and len(F.REALINHA_LOG) - realinha_antes == 2, '(d) contagem de CAIXA/REALINHA: %d/%d' % (n_caixa_c, len(F.REALINHA_LOG) - realinha_antes))

# ------------------------------------------------------------------ (e) varredura R
strings = list(mp.walk(saida))
res = mp.classifica(strings, mp.X, mp.Y)
for f in res['falhas']:
    falha('(e) ' + f)
if res['processo']:
    for c_, lab, g, ctx in res['processo']:
        falha('(e) PROCESSO fora de X/Y: %s | %s | %r | …%s…' % (c_, lab, g, ctx))
n_cont = sum(v for k, v in res['contagem'].items() if k.startswith('X')); n_dur = sum(v for k, v in res['contagem'].items() if k.startswith('Y'))
asserta(n_cont == 8 and n_dur == 1 and len(res['todos']) == 9, '(e) esperado 9 casamentos (X1–X8, Y1) e 0 de processo; achados: %d' % len(res['todos']))
fora = mp.fora_da_lista(strings)

# ------------------------------------------------------------------ (f) fusão
asserta([L['id'] for L in saida['lotes']] == ORDEM_LOTES and 'L1C' not in {L['id'] for L in saida['lotes']}, '(f) lotes')
cont_antes = collections.Counter(gen.lote_of(i['id']) for i in P['itens'] if i['rotulo'] == 'AUTORAL')
cont_depois = collections.Counter(gen.lote_fund(i['id']) for i in saida['itens'] if i['rotulo'] == 'AUTORAL')
asserta(cont_antes == collections.Counter({'L1': 20, 'L1C': 10, 'L2': 30, 'L3': 30, 'L4': 20, 'L4C': 10, 'L5': 20, 'L5C': 10, 'L6A': 15, 'L6B': 15}), '(f) contagem v1.7: %s' % dict(cont_antes))
asserta(cont_depois == collections.Counter({'L1': 30, 'L2': 30, 'L3': 30, 'L4': 30, 'L5': 30, 'L6A': 15, 'L6B': 15}), '(f) contagem v1.8-E: %s' % dict(cont_depois))
L1s = {L['id']: L for L in saida['lotes']}['L1']
L1o = {L['id']: L for L in P['lotes']}
op = {c: d for _, c, _, _, d in OPS}
asserta(L1s['curso'] == op['lotes[L1].curso'] + gen.SEP_COMPL + op['lotes[L1C].curso'] and L1s['curso'].count(gen.SEP_COMPL) == 1, '(f) L1.curso deve ser strip(L1.curso, "L1_estudo.md") + separador + strip(L1C.curso, "L1C_estudo.md"), com 1 separador')
asserta(len(L1s['pegadinhas']) == len(L1o['L1']['pegadinhas']) + len(L1o['L1C']['pegadinhas']) == 23, '(f) pegadinhas do L1: %d' % len(L1s['pegadinhas']))
for lid in ('L4', 'L5'):
    asserta(list(L1o[lid].keys()) == list({L['id']: L for L in saida['lotes']}[lid].keys()), '(f) %s: chaves' % lid)
asserta(all(gen.lote_fund(i['id']) in ORDEM_LOTES for i in saida['itens'] if i['rotulo'] == 'AUTORAL'), '(f) todo item AUTORAL se associa a um lote da lista pelo prefixo')

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
rel['itens_por_lote'] = {'antes_v1_7': dict(cont_antes), 'depois_v1_8_E': dict(cont_depois), 'banco': sum(1 for i in P['itens'] if i['rotulo'] != 'AUTORAL')}
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
print('itens por lote (v1.7 -> v1.8-E):', dict(sorted(cont_antes.items())), '->', dict(sorted(cont_depois.items())))
print('%d falhas' % len(FALHAS))
sys.exit(1 if FALHAS else 0)
