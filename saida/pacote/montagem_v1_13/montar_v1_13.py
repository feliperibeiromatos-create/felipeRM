# montar_v1_13.py — ordem do Fundador de 20/10/2026 — monta o pacote v1.13 = v1.12 (intacto) + Direito Administrativo (P1-DA)
# Entradas: saida/pacote/gerador_v1_12/out/pacote.json e pacote_estudante.json; saida/gcb/DA_plataforma/edital_DA.json;
#           saida/gcb/DA_plataforma/D1..D6_plataforma.json. Saídas em saida/pacote/montagem_v1_13/out/.
import json, hashlib, pathlib, re, sys, collections
R = pathlib.Path(__file__).resolve().parents[3]
V12 = R/'saida/pacote/gerador_v1_12/out'; DA = R/'saida/gcb/DA_plataforma'; OUT = pathlib.Path(__file__).parent/'out'
def lj(p): return json.loads(pathlib.Path(p).read_text(encoding='utf-8'))
def sha(b): return hashlib.sha256(b).hexdigest()
edital_da = lj(DA/'edital_DA.json')
lotes_da = {n: lj(DA/f'D{n}_plataforma.json') for n in range(1, 7)}
ORDEM_LOTES = [1, 2, 3, 4, 5, 6]  # ordem do edital: D1 (1–2), D2 (3–4), D3 (5–7), D4 (8–9), D5 (10), D6 (11–12)
def montar(base, estudante=False):
    p = json.loads(json.dumps(base))
    ed = p['edital']; k = max(i for i, e in enumerate(ed) if e['id'].startswith('P1-')) + 1
    p['edital'] = ed[:k] + edital_da + ed[k:]
    for n in ORDEM_LOTES:
        d = lotes_da[n]; p['lotes'].append(d['lote'])
        if not estudante: p['itens'].extend(d['itens']); continue
        # edição do estudante (contrato v1.2.5 e v1.2.7, ponto 3): url vazia nos AUTORAL; nucleo = 10 primeiros por itemEdital
        cont = collections.Counter(i['itemEdital'] for i in p['itens'])
        for it in d['itens']:
            it = dict(it); it['url'] = ''
            cont[it['itemEdital']] += 1; it['nucleo'] = cont[it['itemEdital']] <= 10
            p['itens'].append(it)
    top = dict(p.get('topicos', {}))
    for n in ORDEM_LOTES:  # contrato v1.2.10, ponto 7: chaves do valor na ordem do ponto 1 da v1.2.9
        top.update({t: {c: v[c] for c in ('resumo', 'emUmMinuto', 'visuais') if c in v} for t, v in lotes_da[n]['topicos'].items()})
    p['topicos'] = {e['id']: top[e['id']] for e in p['edital'] if e['id'] in top}
    p['geradoEm'] = '2026-10-20'; p['nome'] = 'Câmara 2026 — pacote do estudante (v1.13-E)' if estudante else 'Câmara 2026 — pacote F4 (v1.13)'
    # campo de topo 'topicos' continua o último
    return {k2: p[k2] for k2 in ['versao','geradoEm','nome','edital','itens','simulados','lotes','discursivas','topicos']}
F = []
def chk(c, m):
    print(('OK   ' if c else 'FALHA ') + m)
    if not c: F.append(m)
for nome in ('pacote', 'pacote_estudante'):
    b = lj(V12/f'{nome}.json'); n = montar(b, nome == 'pacote_estudante')
    # 1. v1.12 intacta
    chk(n['itens'][:len(b['itens'])] == b['itens'], f'{nome}: {len(b["itens"])} itens da v1.12 idênticos e na mesma ordem')
    chk(n['lotes'][:len(b['lotes'])] == b['lotes'], f'{nome}: {len(b["lotes"])} lotes da v1.12 idênticos')
    chk([e for e in n['edital'] if not e['id'].startswith('P1-DA-')] == b['edital'], f'{nome}: edital P1/P2 idêntico')
    chk(n['simulados'] == b['simulados'] and n['discursivas'] == b['discursivas'], f'{nome}: simulados e discursivas idênticos')
    chk(all(n['topicos'][t] == v for t, v in b['topicos'].items()), f'{nome}: {len(b["topicos"])} tópicos da v1.12 idênticos')
    # 2. DA
    ids = [i['id'] for i in n['itens']]
    chk(len(ids) == len(set(ids)), f'{nome}: ids únicos ({len(ids)})')
    eds = {e['id'] for e in n['edital']}
    chk(all(i['itemEdital'] in eds for i in n['itens']), f'{nome}: todo itemEdital existe no edital')
    chk(len([e for e in n['edital'] if e['id'].startswith('P1-DA-')]) == 46, f'{nome}: 46 entradas P1-DA')
    da = [i for i in n['itens'] if i['itemEdital'].startswith('P1-DA-')]
    chk(all(re.fullmatch(r'D[1-6]-\d{2}', i['id']) for i in da) and len(da) == sum(len(lotes_da[x]['itens']) for x in lotes_da), f'{nome}: {len(da)} itens DA')
    chk(list(n['topicos']) == [e['id'] for e in n['edital'] if e['id'] in n['topicos']], f'{nome}: topicos na ordem do edital ({len(n["topicos"])})')
    chk(list(n)[-1] == 'topicos', f'{nome}: topicos é o último campo')
    # 3. contrato v1.2.10 (D1 da GBQ, saida/pacote/contrato_v1_2_10_2026-10-20.md)
    chk(not [i for i in b['itens'] if i['itemEdital'].startswith('P1-DA-')], f'{nome}: nenhum item da v1.12 em P1-DA (ponto 8, condição iii)')
    lote_de = collections.defaultdict(set)
    for x in lotes_da:
        for i in lotes_da[x]['itens']: lote_de[i['itemEdital']].add(x)
    chk(all(len(v) == 1 for v in lote_de.values()) and all(i['aderencia'] == 'direta' for i in da), f'{nome}: cada itemEdital DA com itens de um só lote e todos "direta" (ponto 8, condições i e ii)')
    chk(all(set(v) == {'resumo', 'emUmMinuto', 'visuais'} for x in lotes_da.values() for v in x['topicos'].values()) and all(list(n['topicos'][t]) == ['resumo', 'emUmMinuto', 'visuais'] for t in n['topicos'] if t.startswith('P1-DA-')), f'{nome}: tópicos DA só com resumo, emUmMinuto, visuais, nesta ordem (ponto 7)')
    vis = [v for t in n['topicos'] if t.startswith('P1-DA-') for v in n['topicos'][t]['visuais']]
    chk(all(1 <= len(v['linhas']) <= 6 and all(len(l) == 3 for l in v['linhas']) and v['legenda'] for v in vis if v['tipo'] == 'compare') and all(1 <= len(v['dispositivos']) <= 4 and all(list(d) == ['ref', 'texto', 'literal', 'conferido'] and re.fullmatch(r'\d{4}-\d{2}-\d{2}', d['conferido']) for d in v['dispositivos']) for v in vis if v['tipo'] == 'baseLegal'), f'{nome}: compare e baseLegal na forma do ponto 6')
    if nome == 'pacote_estudante':
        cf = collections.Counter(i['itemEdital'] for i in da)
        chk(n['nome'] == 'Câmara 2026 — pacote do estudante (v1.13-E)' and all(i['url'] == '' and list(i)[-1] == 'nucleo' for i in da) and sum(i['nucleo'] for i in da) == sum(min(10, c) for c in cf.values()), f'{nome}: nome v1.13-E; itens DA com url "" e nucleo ({sum(i["nucleo"] for i in da)} true)')
    else:
        chk(all('nucleo' not in i for i in n['itens']) and all(i['url'] for i in da), f'{nome}: sem nucleo; itens DA com url do arquivo canônico')
    txt = json.dumps(n, ensure_ascii=False, indent=1) + '\n'
    (OUT/f'{nome}.json').write_text(txt, encoding='utf-8')
    print(f'{nome}.json', len(txt.encode()), 'bytes; SHA-256', sha(txt.encode()))
# estatísticas DA
st = collections.OrderedDict()
for n_ in ORDEM_LOTES:
    d = lotes_da[n_]; it = d['itens']
    st[f'D{n_}'] = dict(itens=len(it), C=sum(i['gabarito']=='C' for i in it), E=sum(i['gabarito']=='E' for i in it),
                       volateis=sum(1 for i in it if i.get('volatil')), topicos=len(d['topicos']), pares=len(d['lote']['pares']),
                       pegadinhas=len(d['lote']['pegadinhas']), sha_json=sha((DA/f'D{n_}_plataforma.json').read_bytes()))
folhas = collections.Counter(i['itemEdital'] for d in lotes_da.values() for i in d['itens'])
(OUT/'stats_v1_13_DA.json').write_text(json.dumps({'lotes': st, 'itens_por_itemEdital': {e['id']: folhas.get(e['id'], 0) for e in edital_da}}, ensure_ascii=False, indent=1), encoding='utf-8')
print(json.dumps(st, ensure_ascii=False)); print('RESULTADO:', len(F), 'FALHA'); sys.exit(1 if F else 0)
