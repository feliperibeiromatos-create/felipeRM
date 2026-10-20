# conferir_t118.py — T-118 (D1 da GBQ, saida/pacote/T118_D1_v1_13_2026-10-20.md, passo 4.3.2 e letra (e)) — 2026-10-20 — gerado por gbq-csc
# Conferência de contagens do pacote v1.13 (out/pacote.json e out/pacote_estudante.json) contra os canônicos D1_v2.md, D2..D5_v2_1.md, D6_v2_1.md
# (SHA-256 conferido contra DECISOES.md), o edital, o banco e a v1.12. Só leitura do repositório; grava só out/conferencia_t118.json.
# Uso: python3 -I conferir_t118.py   (exit 0 só com 0 FALHA). Não lê relógio.
import json, hashlib, pathlib, re, sys, csv, collections
R = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).parent
OUT = HERE / 'out'
V12 = R / 'saida/pacote/gerador_v1_12/out'
GCB = R / 'saida/gcb'
DA = GCB / 'DA_plataforma'
CANON = {1: 'D1_v2.md', 2: 'D2_v2_1.md', 3: 'D3_v2_1.md', 4: 'D4_v2_1.md', 5: 'D5_v2_1.md', 6: 'D6_v2_1.md'}
ATO = {1: ('D-LOTED1-CANONICO', 93, '2026-10-18'), 6: ('D-LOTED6-CANONICO', 117, '2026-10-18'), 5: ('D-LOTED5-CANONICO', 162, '2026-10-20'),
       2: ('D-LOTED2-CANONICO', 163, '2026-10-20'), 3: ('D-LOTED3-CANONICO', 164, '2026-10-20'), 4: ('D-LOTED4-CANONICO', 165, '2026-10-20')}
# valores do preâmbulo da D1 (T118_D1_v1_13_2026-10-20.md)
CE = {1: (30, 30), 2: (40, 40), 3: (31, 40), 4: (41, 38), 5: (35, 35), 6: (25, 25)}
NITENS = {1: 60, 2: 80, 3: 71, 4: 79, 5: 70, 6: 50}
VOLATEIS = ['D2-01', 'D2-28', 'D6-09', 'D6-32', 'D6-34']
NUCLEO_FALSE = {'P1-DA-1.1': 1, 'P1-DA-1.2': 1, 'P1-DA-2.1': 12, 'P1-DA-11': 20, 'P1-DA-12': 10}
VAGOS = ['D3-19', 'D3-31', 'D3-39', 'D3-42', 'D3-48', 'D3-50', 'D3-57', 'D3-60', 'D3-65', 'D3-69', 'D5-54']
HASH_PACOTE = ('82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240', 2906558)
HASH_ESTUD = ('04cbd593fdd30404ecb7f91f6b6722da6b2fc24e58d3c0eb68b10a4e792a0c40', 2644822)
HASH_ANTES = {'pacote': '007787e3ed13b87bdcbbf384a40a41182b78e2f977fb4cc090bc4b84c931c192', 'pacote_estudante': '8b5489b9828a9b3cde25fb27546cc155987b320cd63fd31381cad9cb0442b8dd'}


def sha(b): return hashlib.sha256(b).hexdigest()
def lj(p): return json.loads(pathlib.Path(p).read_text(encoding='utf-8'))


CRIT = []
ORDEM_DIFERE = []   # lotes cuja ordem de apresentação (canônico, 5.1) difere da ordem numérica do id (informativo: contrato v1.2.10, seção 2.2; não é critério)
def chk(cid, desc, esperado, obtido, ok=None):
    ok = (esperado == obtido) if ok is None else ok
    CRIT.append(dict(id=cid, criterio=desc, esperado=esperado, obtido=obtido, resultado='OK' if ok else 'FALHA'))
    print(('OK    ' if ok else 'FALHA ') + cid + ' — ' + desc + ('' if ok else '  [esperado=%r obtido=%r]' % (esperado, obtido)))
    return ok


def diff_json(a, b, p=''):
    if type(a) != type(b): yield p or '/'; return
    if isinstance(a, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b: yield p + '/' + k
            else: yield from diff_json(a[k], b[k], p + '/' + k)
    elif isinstance(a, list):
        if len(a) != len(b): yield p + '[len %d≠%d]' % (len(a), len(b)); return
        for i, (x, y) in enumerate(zip(a, b)): yield from diff_json(x, y, p + '[%d]' % i)
    elif a != b: yield p


def parse_canon(n):
    """{id: dict(gab, ts, rev, vol)} da seção 5.2 (gabarito comentado) do canônico do lote n."""
    L = (GCB / CANON[n]).read_text(encoding='utf-8').split('\n')
    s = [i for i, l in enumerate(L) if re.match(r'^#{1,3} 5\.2 Gabarito comentado', l)]
    assert len(s) == 1, (n, s)
    fim = next((i for i in range(s[0] + 1, len(L)) if re.match(r'^#{1,2} 6\.', L[i])), len(L))
    hdr = [i for i in range(s[0], fim) if re.match(r'^\*\*D%d-\d\d\*\*' % n, L[i])]
    out = collections.OrderedDict()
    for k, i in enumerate(hdr):
        j = hdr[k + 1] if k + 1 < len(hdr) else fim
        blk = '\n'.join(L[i:j])
        iid = re.match(r'^\*\*(D%d-\d\d)\*\*' % n, L[i]).group(1)
        g = re.search(r'Gabarito:\s*\**\s*([CE])\b', blk)
        marcas = re.search(r'Marcas:([^\n]*)', blk)
        mt = marcas.group(1) if marcas else ''
        ts = ('[TS]' in L[i]) or ('TS=sim' in mt) or ('[TS]' in mt)
        rev = ('REVERIFICAR=sim' in mt) or bool(re.search(r'REVERIFICAR(?!=)', mt))
        vol = ('VOLÁTIL=sim' in mt) or bool(re.search(r'VOLÁTIL(?!=)', mt))
        out[iid] = dict(gab=g.group(1) if g else None, ts=ts, rev=rev, vol=vol)
    return out


def ordem_apresentacao(n):
    """ids na ordem da seção 5.1 (versão do estudante: só enunciado) do canônico do lote n."""
    L = (GCB / CANON[n]).read_text(encoding='utf-8').split('\n')
    a = next(i for i, l in enumerate(L) if re.match(r'^#{1,3} 5\.1 ', l))
    b = next(i for i, l in enumerate(L) if re.match(r'^#{1,3} 5\.2 Gabarito comentado', l))
    return [m.group(1) for l in L[a:b] for m in [re.match(r'^\*\*(D%d-\d\d)\.?\*\*' % n, l)] if m]


def main():
    pac = lj(OUT / 'pacote.json'); est = lj(OUT / 'pacote_estudante.json')
    v12p = lj(V12 / 'pacote.json'); v12e = lj(V12 / 'pacote_estudante.json')
    # --- 0. bytes e SHA-256 dos dois pacotes
    bp = (OUT / 'pacote.json').read_bytes(); be = (OUT / 'pacote_estudante.json').read_bytes()
    chk('P0a', 'pacote.json: bytes e SHA-256', list(HASH_PACOTE), [sha(bp), len(bp)])
    chk('P0b', 'pacote_estudante.json: bytes e SHA-256', list(HASH_ESTUD), [sha(be), len(be)])
    chk('P0c', 'os dois arquivos são json.dumps(ensure_ascii=False, indent=1)+LF', True, bp.decode('utf-8') == json.dumps(pac, ensure_ascii=False, indent=1) + '\n' and be.decode('utf-8') == json.dumps(est, ensure_ascii=False, indent=1) + '\n')
    chk('P0d', 'diag30_DA.json intocado (eb1ced6d…)', 'eb1ced6df3d624ae62b82337db6a4cfe29b86baa9494e96aed1b3defe61a6800', sha((OUT / 'diag30_DA.json').read_bytes()))
    # --- 1. canônicos: SHA-256 contra DECISOES.md
    dec = (R / 'DECISOES.md').read_text(encoding='utf-8').split('\n')
    shas = {}
    for n in range(1, 7):
        h = sha((GCB / CANON[n]).read_bytes()); shas[n] = h
        ato, linha, k1 = ATO[n]
        l = dec[linha - 1]
        chk('C1.D%d' % n, '%s: SHA-256 do canônico presente na linha %d de DECISOES.md (ato %s)' % (CANON[n], linha, ato), True, (('| %s |' % ato) in l) and (h in l))
    # --- 2. itens DA: ids e gabaritos iguais aos do canônico; C/E por lote; [TS]; volátil
    canon = {n: parse_canon(n) for n in range(1, 7)}
    da_p = [i for i in pac['itens'] if i['itemEdital'].startswith('P1-DA-')]
    da_e = [i for i in est['itens'] if i['itemEdital'].startswith('P1-DA-')]
    chk('C2.0', 'itens DA no pacote.json', 410, len(da_p)); chk('C2.0e', 'itens DA no pacote_estudante.json', 410, len(da_e))
    ids_p = [i['id'] for i in da_p]
    chk('C2.1', 'itens DA: ids únicos, todos D<n>-NN, na ordem D1..D6', True, len(set(ids_p)) == 410 and all(re.fullmatch(r'D[1-6]-\d{2}', x) for x in ids_p) and ids_p == sorted(ids_p, key=lambda x: (int(x[1]), int(x[3:]))))
    chk('C2.2', 'itens DA: todos AUTORAL e "direta"', True, all(i['rotulo'] == 'AUTORAL' and i['aderencia'] == 'direta' for i in da_p))
    ce_obt = {}
    for n in range(1, 7):
        c = canon[n]
        pid = [i for i in da_p if i['id'].startswith('D%d-' % n)]
        chk('C2.D%d.n' % n, 'lote D%d: itens do pacote' % n, NITENS[n], len(pid))
        chk('C2.D%d.ids' % n, 'lote D%d: conjunto de ids do pacote = conjunto de ids do canônico (seção 5.2)' % n, sorted(c), sorted(i['id'] for i in pid))
        chk('C2.D%d.ord' % n, 'lote D%d: itens do pacote em ordem numérica do id (contrato v1.2.10, ponto 3)' % n, sorted(c, key=lambda x: int(x[3:])), [i['id'] for i in pid])
        if ordem_apresentacao(n) != [i['id'] for i in pid]: ORDEM_DIFERE.append('D%d' % n)
        chk('C2.D%d.gab' % n, 'lote D%d: gabarito de cada item (por id) = o do canônico' % n, {x: c[x]['gab'] for x in sorted(c)}, {i['id']: i['gabarito'] for i in sorted(pid, key=lambda z: z['id'])})
        ce = (sum(i['gabarito'] == 'C' for i in pid), sum(i['gabarito'] == 'E' for i in pid)); ce_obt['D%d' % n] = ce
        chk('C2.D%d.ce' % n, 'lote D%d: C/E (preâmbulo da D1)' % n, list(CE[n]), list(ce))
    # D-ID no estudante: ids e gabaritos iguais aos do pacote.json
    chk('C2.E', 'pacote_estudante: ids, gabaritos, enunciados e justificativas DA = pacote.json', True,
        [(i['id'], i['gabarito'], i['enunciado'], i['justificativa'], i['itemEdital']) for i in da_p] == [(i['id'], i['gabarito'], i['enunciado'], i['justificativa'], i['itemEdital']) for i in da_e])
    # itens = arquivos de plataforma
    plat = {n: lj(DA / ('D%d_plataforma.json' % n)) for n in range(1, 7)}
    ok = True
    for n in range(1, 7):
        its = [i for i in da_p if i['id'].startswith('D%d-' % n)]
        ok = ok and its == plat[n]['itens']
    chk('C2.P', 'itens DA do pacote.json = itens dos D<n>_plataforma.json (objeto a objeto)', True, ok)
    vol_p = [i['id'] for i in da_p if i.get('volatil')]
    chk('C2.V', 'volatil (pacote.json) = lista do preâmbulo', VOLATEIS, vol_p)
    chk('C2.Ve', 'volatil (pacote_estudante) = lista do preâmbulo', VOLATEIS, [i['id'] for i in da_e if i.get('volatil')])
    vol_c = [x for n in range(1, 7) for x, v in canon[n].items() if v['vol'] or v['rev']]
    chk('C2.Vc', 'volatil = itens com REVERIFICAR ou VOLÁTIL no canônico', VOLATEIS, vol_c)
    # ids vagos
    vagos = []
    for n in (3, 5):
        pres = {int(x[3:]) for x in canon[n]}
        vagos += ['D%d-%02d' % (n, k) for k in range(1, max(pres) + 1) if k not in pres]
    chk('C2.vagos', 'ids vagos (não reutilizados) = preâmbulo', VAGOS, vagos)
    chk('C2.vagos2', 'D1, D2, D4 e D6 sem ids vagos (numeração contínua)', True, all(sorted(int(x[3:]) for x in canon[n]) == list(range(1, NITENS[n] + 1)) for n in (1, 2, 4, 6)))
    # --- 3. edital P1-DA
    ed = pac['edital']; ed_e = est['edital']
    eda = json.load(open(DA / 'edital_DA.json', encoding='utf-8'))
    pos = [k for k, e in enumerate(ed) if e['id'].startswith('P1-DA-')]
    chk('C3.1', '46 entradas P1-DA no pacote.json', 46, len(pos)); chk('C3.1e', '46 entradas P1-DA no pacote_estudante.json', 46, len([e for e in ed_e if e['id'].startswith('P1-DA-')]))
    chk('C3.2', 'entradas P1-DA em bloco contíguo nas posições 20 a 65 (base 0)', [20, 65, True], [pos[0], pos[-1], pos == list(range(pos[0], pos[-1] + 1))])
    chk('C3.3', 'entradas P1-DA = edital_DA.json', eda, [ed[k] for k in pos])
    chk('C3.3e', 'edital do pacote_estudante = edital do pacote.json', ed, ed_e)
    txt = (R / 'edital/DA_itens_1_12_P1.md').read_text(encoding='utf-8')
    corpo = txt.split('\n\n', 1)[1] if '\n\n' in txt else txt
    p0 = 0; okord = True; falhas = []
    for e in eda:
        num = e['id'][len('P1-DA-'):]
        m = [mm.start() for mm in re.finditer(re.escape(num + ' ' + e['texto']), corpo)]
        m = [x for x in m if x >= p0 and (x == 0 or corpo[x - 2:x] == '. ' or corpo[x - 1] == '\n')]
        if not m: okord = False; falhas.append(e['id']); continue
        p0 = m[0] + 1
    chk('C3.4', '46 entradas = texto literal de edital/DA_itens_1_12_P1.md (número + texto, na ordem)', [], falhas)
    chk('C3.5', 'edital: ordem P1 (TI), P1-DA, P2 (bloco DA entre a última P1-<n> e a primeira P2-)', True,
        all(not e['id'].startswith('P1-DA-') and e['id'].startswith('P1-') for e in ed[:pos[0]]) and all(e['id'].startswith('P2-') for e in ed[pos[-1] + 1:]))
    chk('C3.6', 'edital P1/P2 idêntico ao da v1.12', v12p['edital'], [e for e in ed if not e['id'].startswith('P1-DA-')])
    # --- 4. lotes
    lids = [l['id'] for l in pac['lotes']]
    chk('C4.1', 'lotes no pacote.json', 16, len(lids)); chk('C4.1e', 'lotes no pacote_estudante.json (13)', 13, len(est['lotes']))
    chk('C4.2', 'lotes DA (D1..D6) no fim do pacote.json, nesta ordem', ['D1', 'D2', 'D3', 'D4', 'D5', 'D6'], lids[-6:])
    chk('C4.2e', 'lotes DA no fim do pacote_estudante.json', ['D1', 'D2', 'D3', 'D4', 'D5', 'D6'], [l['id'] for l in est['lotes']][-6:])
    chk('C4.3', 'lotes DA = D<n>_plataforma.json[lote] (objeto a objeto, nos dois pacotes)', True,
        all(pac['lotes'][-6 + k] == plat[k + 1]['lote'] and est['lotes'][-6 + k] == plat[k + 1]['lote'] for k in range(6)))
    chk('C4.4', 'lotes da v1.12 idênticos', v12p['lotes'], pac['lotes'][:10])
    # --- 5. tópicos
    top_da = {t: v for t, v in pac['topicos'].items() if t.startswith('P1-DA-')}
    plat_top = {}
    for n in range(1, 7): plat_top.update(plat[n]['topicos'])
    chk('C5.1', 'tópicos DA no pacote.json', 39, len(top_da)); chk('C5.2', 'tópicos no total', 79, len(pac['topicos']))
    chk('C5.3', 'tópicos DA = os dos D<n>_plataforma.json (como objeto)', plat_top, top_da)
    chk('C5.3e', 'tópicos do pacote_estudante = os do pacote.json', pac['topicos'], est['topicos'])
    chk('C5.4', 'tópicos da v1.12 idênticos', v12p['topicos'], {t: v for t, v in pac['topicos'].items() if not t.startswith('P1-DA-')})
    # --- 6. nucleo
    nuc = [i['nucleo'] for i in da_e]
    chk('C6.1', 'nucleo DA: true / false', [366, 44], [sum(nuc), len(nuc) - sum(nuc)])
    nf = collections.Counter(i['itemEdital'] for i in da_e if not i['nucleo'])
    chk('C6.2', 'nucleo false por itemEdital (preâmbulo: 1.1:1, 1.2:1, 2.1:12, 11:20, 12:10)', NUCLEO_FALSE, dict(nf))
    chk('C6.3', 'nucleo total no pacote_estudante (367 da v1.12 + 366 de DA)', [733, 367, 366], [sum(i['nucleo'] for i in est['itens']), sum(i['nucleo'] for i in est['itens'][:749]), sum(nuc)])
    chk('C6.4', 'pacote.json sem campo nucleo', True, all('nucleo' not in i for i in pac['itens']))
    # (e) nucleo_k1k4: critério completo do nucleo.py (k1..k4) com os atos D1..D6 mapeados
    atos = {}
    for k, l in enumerate(dec, 1):
        m = re.match(r'^APLICADA [^|]*\| (D-[A-Z0-9-]+) \|', l)
        if m and m.group(1) not in atos: atos[m.group(1)] = k
    for n in range(1, 7):
        chk('E.linha.D%d' % n, 'linha do ato %s em DECISOES.md (primeira ocorrência APLICADA)' % ATO[n][0], ATO[n][1], atos.get(ATO[n][0]))
    chave = {}
    for pos_, it in enumerate(est['itens']):
        if it['itemEdital'].startswith('P1-DA-'):
            n = int(it['id'][1]); ato, linha, k1 = ATO[n]
            chave[it['id']] = (it['itemEdital'], (k1, atos[ato], 0 if it['aderencia'] == 'direta' else 1, pos_))
    por = collections.defaultdict(list)
    for iid, (f, k) in chave.items(): por[f].append(iid)
    calc = {}
    for f, ids in por.items():
        for r, iid in enumerate(sorted(ids, key=lambda x: chave[x][1])): calc[iid] = r < 10
    iguais = sum(calc[i['id']] == i['nucleo'] for i in da_e)
    chk('E.nucleo', 'nucleo recalculado (k1..k4, atos D1..D6 mapeados) = nucleo do pacote_estudante', 410, iguais)
    chk('E.nucleo.cont', 'nucleo recalculado: true / false', [366, 44], [sum(calc.values()), 410 - sum(calc.values())])
    nucleo_k1k4 = dict(criterio='nucleo.py: 10 primeiros por itemEdital pela chave (k1 data, k2 linha do ato em DECISOES.md, k3 aderência direta<parcial, k4 posição); atos D1..D6 mapeados pela D1 (seção 4.3)',
                       mapeamento={'D%d' % n: dict(ato=ATO[n][0], linha=ATO[n][1], k1=ATO[n][2]) for n in sorted(ATO)}, iguais=iguais, de=410,
                       true=sum(calc.values()), false=410 - sum(calc.values()), distribuicao_false=dict(nf),
                       folhas_com_mais_de_um_lote=[f for f, ids in por.items() if len({x.split('-')[0] for x in ids}) > 1])
    chk('E.1lote', 'cada itemEdital DA tem itens de um só lote (k1 e k2 constantes na folha)', [], nucleo_k1k4['folhas_com_mais_de_um_lote'])
    # --- 7. v1.12 byte a byte
    ok = all(json.dumps(a, ensure_ascii=False, indent=1) == json.dumps(b, ensure_ascii=False, indent=1) for a, b in zip(pac['itens'][:749], v12p['itens'])) and len(v12p['itens']) == 749
    chk('C7.1', '749 itens da v1.12 byte a byte no pacote.json', True, ok)
    ok = all(json.dumps(a, ensure_ascii=False, indent=1) == json.dumps(b, ensure_ascii=False, indent=1) for a, b in zip(est['itens'][:749], v12e['itens'])) and len(v12e['itens']) == 749
    chk('C7.2', '749 itens da v1.12 byte a byte no pacote_estudante (com nucleo)', True, ok)
    chk('C7.3', 'simulados e discursivas idênticos aos da v1.12 (nos dois)', True, pac['simulados'] == v12p['simulados'] and pac['discursivas'] == v12p['discursivas'] and est['simulados'] == v12e['simulados'] and est['discursivas'] == v12e['discursivas'])
    chk('C7.4', 'nome e versão: pacote F4 (v1.13) / estudante (v1.13-E); geradoEm 2026-10-20', ['Câmara 2026 — pacote F4 (v1.13)', 'Câmara 2026 — pacote do estudante (v1.13-E)', '2026-10-20', '2026-10-20'], [pac['nome'], est['nome'], pac['geradoEm'], est['geradoEm']])
    # --- 8. diff contra a montagem anterior ao achado 10 (cópia no scratchpad não é usada: o diff é contra os SHA-256 da D1)
    chk('C8.1', 'SHA-256 anterior à errata (D1, seção 4.3.1) diferem dos atuais', True, HASH_ANTES['pacote'] != sha(bp) and HASH_ANTES['pacote_estudante'] != sha(be))
    # --- 9. folhas
    pa = [e['id'] for e in ed if e['id'].startswith('P1-DA-')]
    folhas = [x for x in pa if not any(y.startswith(x + '.') for y in pa)]
    chk('C9.1', 'folhas de DA (entradas sem subentrada)', 37, len(folhas))
    cont = collections.Counter(i['itemEdital'] for i in da_p)
    em_folha = sum(cont[f] for f in folhas); fora = {k: v for k, v in cont.items() if k not in folhas}
    chk('C9.2', 'itens em folha / fora de folha', [396, 14], [em_folha, sum(fora.values())])
    chk('C9.3', 'fora de folha: P1-DA-1 = 8 e P1-DA-8 = 6', {'P1-DA-1': 8, 'P1-DA-8': 6}, fora)
    ge20 = {f: cont[f] for f in folhas if cont[f] >= 20}
    chk('C9.4', 'folhas com 20 ou mais: 2.1 = 22, 11 = 30, 12 = 20', {'P1-DA-2.1': 22, 'P1-DA-11': 30, 'P1-DA-12': 20}, ge20)
    chk('C9.5', 'folhas abaixo de 20', 34, sum(1 for f in folhas if cont[f] < 20))
    chk('C9.6', 'entradas de topicos DA = 37 folhas + P1-DA-1 + P1-DA-8', sorted(folhas + ['P1-DA-1', 'P1-DA-8']), sorted(top_da))
    pa_all = collections.Counter(i['itemEdital'] for i in pac['itens'])
    todas = [e['id'] for e in ed]
    folhas_all = [x for x in todas if not any(y.startswith(x + '.') for y in todas)]
    fora_all = sum(v for k, v in pa_all.items() if k not in folhas_all)
    chk('C9.7', 'pacote inteiro: itens fora de folha (13 da v1.12 + 14 de DA)', 27, fora_all)
    chk('C9.8', 'pacote inteiro: itens e C/E', [1159, 582, 577], [len(pac['itens']), sum(i['gabarito'] == 'C' for i in pac['itens']), sum(i['gabarito'] == 'E' for i in pac['itens'])])
    # --- 10. banco
    bq = [r for r in csv.DictReader(open(R / 'banco/banco.csv', encoding='utf-8'), delimiter=';') if r['item_edital_camara'].startswith('P1-DA')]
    ids_all = {i['id'] for i in pac['itens']} | {i['id'] for i in est['itens']}
    chk('C10.1', 'banco: 40 linhas P1-DA (BQ-0113 a BQ-0152), 2 anuladas (BQ-0131, BQ-0133), 38 vigentes', [40, ['BQ-0131', 'BQ-0133'], 38], [len(bq), [r['id'] for r in bq if r['anulado'] == 'sim'], sum(r['anulado'] != 'sim' for r in bq)])
    chk('C10.2', 'os 38 do banco (e as 2 anuladas) ausentes dos dois pacotes', [], sorted(r['id'] for r in bq if r['id'] in ids_all))
    chk('C10.3', 'nenhum item de banco com itemEdital P1-DA nos pacotes', 0, sum(1 for i in pac['itens'] if i['id'].startswith('BQ-') and i['itemEdital'].startswith('P1-DA-')))
    # --- 11. estruturas
    chk('C11.1', 'campos de topo e ordem', ['versao', 'geradoEm', 'nome', 'edital', 'itens', 'simulados', 'lotes', 'discursivas', 'topicos'], list(pac))
    falhas = sum(1 for c in CRIT if c['resultado'] == 'FALHA')
    res = collections.OrderedDict(
        tarefa='T-118 (D1 da GBQ, 4.3.2)', script='saida/pacote/montagem_v1_13/conferir_t118.py',
        entradas={'out/pacote.json': sha(bp), 'out/pacote_estudante.json': sha(be), **{CANON[n]: shas[n] for n in shas}},
        contagens=dict(itens_da=410, da_por_lote={('D%d' % n): NITENS[n] for n in NITENS}, ce_por_lote={k: list(v) for k, v in ce_obt.items()}, entradas_edital_da=46, lotes_da=6, lotes_total=len(lids), topicos_da=len(top_da), topicos_total=len(pac['topicos']),
                       nucleo_true=sum(nuc), nucleo_false=len(nuc) - sum(nuc), nucleo_total_estudante=sum(i['nucleo'] for i in est['itens']), folhas_da=len(folhas), itens_em_folha=em_folha, itens_fora_de_folha=sum(fora.values()),
                       itens_por_folha={f: cont[f] for f in folhas}, itens_fora_por_entrada=fora, volateis=vol_p, ids_vagos=vagos, itens_total=len(pac['itens'])),
        marcas_canonico={('D%d' % n): dict(ts=sum(v['ts'] for v in canon[n].values()), reverificar=[x for x, v in canon[n].items() if v['rev']], volatil_marca=[x for x, v in canon[n].items() if v['vol']]) for n in range(1, 7)},
        nucleo_k1k4=nucleo_k1k4, informativo=dict(lotes_com_ordem_de_apresentacao_diferente_da_ordem_dos_ids=ORDEM_DIFERE, nota='D1 da GBQ/contrato v1.2.10 e FORMATO seção 4 mandam a ordem numérica do id; k4 usa a posição no pacote.json'), criterios=CRIT, total_criterios=len(CRIT), falhas=falhas)
    (OUT / 'conferencia_t118.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('RESULTADO: %d critérios, %d FALHA' % (len(CRIT), falhas))
    sys.exit(1 if falhas else 0)


if __name__ == '__main__':
    main()
