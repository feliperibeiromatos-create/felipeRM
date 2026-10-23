# conferir_t123.py — T-123 fase 2 (script 4 da seção 4; passo 6) — 2026-10-23 — gerado por gbq-csc
# -*- coding: utf-8 -*-
"""Conferência do pacote v1.14 (D1 da GBQ, seção 8.1): C-SHA, C-INTACTA, C-TOTAIS, C-REFORCO, C-JUST, C-MARCAS, C-BANCO, C-ESTUDANTE, C-FOLHAS, C-DIAG30, C-MOLDURA, C-MD e C-MANIFESTO.
Cada critério tem id, esperado e obtido; resultado OK, FALHA ou PENDENTE (C-MANIFESTO enquanto o MANIFESTO não existe). Relê as levas, o CSV da GCB, o banco e DECISOES.md por leitura independente da do montar_v1_14.py.
A função `executa(ctx, fs)` é usada por mutacao_t123.py (fs=False pula os critérios que leem arquivos fora de `ctx`). Grava out/conferencia_t123.json; exit 0 só com 0 FALHA e 0 PENDENTE.
Uso: python -I conferir_t123.py. Não lê relógio."""
import sys
sys.dont_write_bytecode = True
import collections, copy, csv, hashlib, io, json, os, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import montar_v1_14 as M
import marcas_v114 as MV

R = M.R; OUT = M.OUT
SHA_CONTRATO_DEPOIS = '3916ad994cd06ee74b13ba545de5af3b6c241d0004eb0625e922973ab76c38df'
ESP_LEVA = {1: (30, 15, 15, 16, 8), 2: (30, 17, 13, 13, 2), 3: (30, 16, 14, 14, 11), 4: (28, 15, 13, 13, 5), 5: (30, 16, 14, 14, 0), 6: (30, 14, 16, 15, 0), 7: (30, 15, 15, 13, 8), 8: (30, 14, 16, 16, 1)}   # n, C, E, [TS], parciais
ESP_LOTE = {'D1': (12, 6, 6), 'D2': (80, 40, 40), 'D3': (89, 49, 40), 'D4': (57, 27, 30)}
ESP_LOTE_V114 = {'D1': 72, 'D2': 160, 'D3': 160, 'D4': 136, 'D5': 70, 'D6': 50}
PARCIAIS = ['D3-R01', 'D3-R04', 'D3-R06', 'D3-R08', 'D3-R09', 'D3-R10', 'D3-R12', 'D3-R13', 'D3-R18', 'D3-R20', 'D3-R22', 'D3-R23', 'D3-R24', 'D3-R25', 'D3-R31', 'D3-R36', 'D3-R37', 'D3-R42', 'D3-R44', 'D3-R46', 'D3-R48',
            'D3-R52', 'D3-R53', 'D3-R56', 'D3-R57', 'D3-R58', 'D3-R70', 'D3-R72', 'D3-R73', 'D3-R75', 'D3-R76', 'D3-R77', 'D3-R78', 'D3-R79', 'D4-R44']
D3R75_LINHA2 = 'O item troca “uma quinta parte” por “um terço”, teto maior, o que contradiz o limite da letra; o valor “terço” não ocorre na Lei 4.619, cujo único limite de desconto é o do art. 6º.'
E3E4 = [('D4-R42', 'AJ-L8-E3', 'Considere que um expositor, em audiência pública de comissão da Câmara dos Deputados, trate da participação social.'),
        ('D4-R52', 'AJ-L8-E4', 'Considere que um expositor, ouvido em audiência pública de comissão da Câmara dos Deputados, afirme que,')]
ATO_DATA = {'D1': ('D-LOTED1-CANONICO', '2026-10-18'), 'D6': ('D-LOTED6-CANONICO', '2026-10-18'), 'D5': ('D-LOTED5-CANONICO', '2026-10-20'), 'D2': ('D-LOTED2-CANONICO', '2026-10-20'),
            'D3': ('D-LOTED3-CANONICO', '2026-10-20'), 'D4': ('D-LOTED4-CANONICO', '2026-10-20'),
            1: ('D-T116-LEVA1-ACEITE', '2026-10-20'), 2: ('D-T116-LEVA2-ACEITE', '2026-10-20'), 3: ('D-T116-LEVA3-ACEITE', '2026-10-22'), 4: ('D-T116-LEVA4-ACEITE', '2026-10-22'),
            5: ('D-T116-LEVA5-ACEITE', '2026-10-22'), 6: ('D-T116-LEVA6-ACEITE', '2026-10-22'), 7: ('D-T116-LEVA7-ACEITE', '2026-10-22'), 8: ('D-T116-LEVA8-ACEITE', '2026-10-22'),
            'R75': ('D-D3R75-AJL7E1-ACEITE', '2026-10-22')}
CAMPOS_DA = ['id', 'rotulo', 'certame', 'cargo', 'ano', 'numero', 'comando', 'textoBase', 'enunciado', 'gabarito', 'justificativa', 'itemEdital', 'aderencia', 'url']
RX_REF = re.compile(r'D[1-6]-R\d\d')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def lj(b):
    return json.loads(b.decode('utf-8'))


# ------------------------------------------------------------------ leitura independente das levas
def releitura(ins):
    """{id: dict(leva, enun_raw, gab, ader, ie, j1, j2)} (na ordem da seção 1 de cada leva), sem aplicar erratas."""
    out = collections.OrderedDict()
    for n in range(1, 9):
        L = ins['leva%d' % n].decode('utf-8').split('\n')
        h = [i for i, l in enumerate(L) if re.match(r'^## \d+\. ', l)]
        sec = {int(re.match(r'^## (\d+)\.', L[i]).group(1)): (i, h[k + 1] if k + 1 < len(h) else len(L)) for k, i in enumerate(h)}
        for l in L[sec[1][0]:sec[1][1]]:
            m = re.match(r'^\*\*(D[1-6]-R\d{2})\.\*\* (.+)$', l)
            if m:
                out[m.group(1)] = dict(leva=n, enun_raw=m.group(2))
        cur = None
        for l in L[sec[2][0]:sec[2][1]]:
            m = re.match(r'^\*\*(D[1-6]-R\d{2})\*\* \(folha', l)
            if m:
                cur = m.group(1); continue
            if cur:
                m = re.match(r'^- (itemEdital|Aderência|Gabarito|Justificativa \(linha 1\)|Justificativa \(linha 2\)): (.*)$', l)
                if m:
                    k = {'itemEdital': 'ie', 'Aderência': 'ader', 'Gabarito': 'gab', 'Justificativa (linha 1)': 'j1', 'Justificativa (linha 2)': 'j2'}[m.group(1)]
                    out[cur][k] = m.group(2)
    return out


def aplica_erratas(rel):
    """erratas aceitas (D1, 2.2) sobre a releitura; devolve ({id: enunciado}, {id: j2}) e anota ocorrências."""
    enun = {i: v['enun_raw'] for i, v in rel.items()}; j2 = {i: v['j2'] for i, v in rel.items()}; oc = {}
    for (iid, ato, campo, antes, depois) in M.ERRATAS:
        alvo = enun if campo == 'enunciado' else j2
        oc[iid] = (alvo[iid].count(antes), alvo[iid].count(depois))
        alvo[iid] = alvo[iid].replace(antes, depois)
    return enun, j2, oc


def justificativas(rel, j2, csv_bytes):
    """justificativa esperada: j1 + ' ' + j2, depois cada substituição da GCB exatamente 1 vez (ordem do CSV)."""
    just = {i: v['j1'] + ' ' + j2[i] for i, v in rel.items()}
    rd = csv.reader(io.StringIO(csv_bytes.decode('utf-8'), newline=''), delimiter=';')
    next(rd)
    n = 0; ruins = []
    for row in rd:
        iid, campo, antes, depois = row[0], row[1], row[2], row[3]
        if campo != 'justificativa' or antes == '' or just[iid].count(antes) != 1:
            ruins.append((iid, antes)); continue
        just[iid] = just[iid].replace(antes, depois); n += 1
    return just, n, ruins


# ------------------------------------------------------------------ contexto
def carregar_ctx():
    ins = M.ler_insumos()
    pb = open(os.path.join(OUT, 'pacote.json'), 'rb').read(); eb = open(os.path.join(OUT, 'pacote_estudante.json'), 'rb').read()
    return dict(ins=ins, pac_b=pb, est_b=eb, pac=lj(pb), est=lj(eb), base_pac=lj(ins['base_pacote']), base_est=lj(ins['base_estudante']), banco=M.banco_rows(ins['banco']))


def executa(ctx, fs=True):
    CRIT = []

    def chk(cid, desc, esperado, obtido, ok=None, estado=None):
        ok = (esperado == obtido) if ok is None else ok
        r = estado or ('OK' if ok else 'FALHA')
        CRIT.append(dict(id=cid, criterio=desc, esperado=esperado, obtido=obtido, resultado=r))
        return ok

    ins = ctx['ins']; pac = ctx['pac']; est = ctx['est']; bp = ctx['base_pac']; be = ctx['base_est']
    itens = pac['itens']; by = {i['id']: i for i in itens}; ebid = {i['id']: i for i in est['itens']}
    bids = [i['id'] for i in bp['itens']]; bset = set(bids)
    # ============================================================== C-SHA
    sl = M.shas_levas(ins['dec'].decode('utf-8'))
    for nome, esp in M.SHA_FIXO.items():
        chk('C-SHA.' + nome, '%s: SHA-256 LF' % M.PATH[nome], esp, sha(ins[nome]))
    for n in range(1, 9):
        chk('C-SHA.leva%d' % n, '%s: SHA-256 LF = o da linha de aceite em DECISOES.md' % M.PATH['leva%d' % n], sl[n], sha(ins['leva%d' % n]))
    chk('C-SHA.pacote', 'out/pacote.json = json.dumps(ensure_ascii=False, indent=1)+LF do objeto lido; 0 CR', [True, 0], [ctx['pac_b'] == M.dumps(pac), ctx['pac_b'].count(b'\r')])
    chk('C-SHA.estudante', 'out/pacote_estudante.json = json.dumps(ensure_ascii=False, indent=1)+LF do objeto lido; 0 CR', [True, 0], [ctx['est_b'] == M.dumps(est), ctx['est_b'].count(b'\r')])
    if fs:
        c = open(os.path.join(R, 'regras', 'pacote_contrato.md'), 'rb').read().replace(b'\r\n', b'\n')
        chk('C-SHA.contrato', 'regras/pacote_contrato.md (v1.2.12): SHA-256 LF', SHA_CONTRATO_DEPOIS, sha(c))
        chk('C-SHA.contrato_titulo', 'regras/pacote_contrato.md: linha 1 com (v1.2.12, 2026-10-23)', True, '(v1.2.12, 2026-10-23)' in c.decode('utf-8').split('\n')[0])
    # ============================================================== C-INTACTA
    chk('C-INTACTA.itens', 'os 1.159 itens da v1.13 são iguais como objeto e estão na mesma ordem relativa no pacote.json', True, [i for i in itens if i['id'] in bset] == bp['itens'] and len(bp['itens']) == 1159)
    for k in ('versao', 'edital', 'simulados', 'lotes', 'discursivas', 'topicos'):
        chk('C-INTACTA.' + k, '%s do pacote.json e do estudante iguais aos da v1.13' % k, [True, True], [pac[k] == bp[k], est[k] == be[k]])
    eit = [{k: v for k, v in i.items() if k != 'nucleo'} for i in est['itens'] if i['id'] in bset]
    chk('C-INTACTA.estudante', 'itens da v1.13 no pacote_estudante: iguais aos da v1.13-E, salvo o nucleo (mesma ordem)', True, eit == [{k: v for k, v in i.items() if k != 'nucleo'} for i in be['itens']])
    chk('C-INTACTA.simulados', 'nenhum item de DA entra em simulados (simulados iguais aos da v1.13)', True, pac['simulados'] == bp['simulados'] and not any(x in by and by[x]['itemEdital'].startswith('P1-DA-') for s in pac['simulados'] for x in s['itens']))
    if fs:
        man = open(os.path.join(R, 'saida', 'pacote', 'montagem_v1_13', 'MANIFESTO_v1_13.md'), 'rb').read().replace(b'\r\n', b'\n').decode('utf-8').split('\n')
        rows = [re.match(r'^\| (saida/pacote/montagem_v1_13/\S+) \| (\d+) \| ([0-9a-f]{64}) \|$', l) for l in man]
        rows = [m.groups() for m in rows if m]
        tot = [re.search(r'Total: (\d+) arquivos', l) for l in man]; tot = [int(m.group(1)) for m in tot if m]
        chk('C-INTACTA.manifesto13_n', 'MANIFESTO_v1_13: 70 arquivos listados (e o total declarado)', [70, [70]], [len(rows), tot])
        dif = []
        for (rel, nb, h) in rows:
            p = os.path.join(R, rel)
            if not os.path.isfile(p):
                dif.append((rel, 'ausente')); continue
            raw = open(p, 'rb').read(); lf = raw.replace(b'\r\n', b'\n')
            if not ((len(raw) == int(nb) and sha(raw) == h) or (len(lf) == int(nb) and sha(lf) == h)):
                dif.append((rel, 'bytes/SHA difere'))
        chk('C-INTACTA.manifesto13', 'os 70 arquivos do MANIFESTO_v1_13 têm bytes e SHA-256 inalterados (em disco ou em LF, conforme o fim de linha da árvore)', [], dif)
        sec4 = [re.match(r'^\| (saida/gcb/DA_plataforma/D[1-6]_plataforma\.json) \| ([0-9a-f]{64}) \|$', l) for l in man]
        sec4 = [m.groups() for m in sec4 if m]
        chk('C-INTACTA.plataforma_json', 'os 6 D<n>_plataforma.json têm o SHA-256 (LF) da seção 4 do MANIFESTO_v1_13', [6, []], [len(sec4), [r for (r, h) in sec4 if sha(open(os.path.join(R, r), 'rb').read().replace(b'\r\n', b'\n')) != h]])
        alvos = ['saida/gcb/DA_reforco_leva%d_v2.md' % n for n in range(1, 9)] + ['saida/gcb/DA_plataforma/D%d_plataforma.json' % n for n in range(1, 7)] + [
            'saida/plataforma/plataforma_v16_final_template.html', 'saida/plataforma/plataforma_v16_template.html', 'saida/plataforma/plataforma_v16_publicar.html', 'saida/plataforma/build_plataforma_v16.py', 'saida/pacote/montagem_v1_13', 'saida/pacote/gerador_v1_12']
        try:
            g = subprocess.run(['git', '-C', R, 'status', '--porcelain', '--'] + alvos, capture_output=True, check=True).stdout.decode('utf-8', 'replace').strip().split('\n')
            g = [x for x in g if x]
        except Exception as e:      # git indisponível
            g = ['git: %s' % e]
        chk('C-INTACTA.git', 'levas, D<n>_plataforma.json, plataforma v16, montagem_v1_13 e gerador_v1_12 sem modificação no git (git status --porcelain vazio)', [], g)
    # ============================================================== C-TOTAIS
    ids = [i['id'] for i in itens]
    chk('C-TOTAIS.itens', '1.433 itens, ids únicos', [1433, 1433], [len(itens), len(set(ids))])
    chk('C-TOTAIS.ce', 'C/E no pacote', [730, 703], [sum(i['gabarito'] == 'C' for i in itens), sum(i['gabarito'] == 'E' for i in itens)])
    da = [i for i in itens if i['itemEdital'].startswith('P1-DA-')]
    chk('C-TOTAIS.da', 'DA: 684 itens, C/E 350/334', [684, 350, 334], [len(da), sum(i['gabarito'] == 'C' for i in da), sum(i['gabarito'] == 'E' for i in da)])
    refo = [i for i in itens if RX_REF.fullmatch(i['id'])]
    chk('C-TOTAIS.reforco', 'reforço: 238 itens, C/E 122/116', [238, 122, 116], [len(refo), sum(i['gabarito'] == 'C' for i in refo), sum(i['gabarito'] == 'E' for i in refo)])
    # tabela por leva e por lote a partir da releitura independente
    rel = releitura(ins)
    por_leva = {n: [x for x in rel if rel[x]['leva'] == n] for n in range(1, 9)}
    obt_leva = {n: [len(por_leva[n]), sum(by[x]['gabarito'] == 'C' for x in por_leva[n] if x in by), sum(by[x]['gabarito'] == 'E' for x in por_leva[n] if x in by),
                    sum(rel[x].get('ader') == 'parcial' for x in por_leva[n])] for n in range(1, 9)}
    chk('C-TOTAIS.por_leva', 'reforço por leva no pacote (n, C, E, parciais) = tabela da seção 2.1', {n: [ESP_LEVA[n][0], ESP_LEVA[n][1], ESP_LEVA[n][2], ESP_LEVA[n][4]] for n in ESP_LEVA}, obt_leva)
    chk('C-TOTAIS.por_leva_ts', '[TS] por leva (cabeçalho do bloco da seção 2 de cada leva) = tabela da seção 2.1', {n: ESP_LEVA[n][3] for n in ESP_LEVA},
        {n: sum(1 for x in por_leva[n] if re.search(r'^\*\*%s\*\* \(folha[^\n]*\[TS\]' % re.escape(x), ins['leva%d' % n].decode('utf-8'), re.M)) for n in range(1, 9)})
    por_lote = {l: [i for i in refo if i['id'].startswith(l + '-')] for l in ESP_LOTE}
    chk('C-TOTAIS.por_lote', 'reforço por lote (n, C, E) = tabela da seção 2.1', {l: list(v) for l, v in ESP_LOTE.items()}, {l: [len(v), sum(i['gabarito'] == 'C' for i in v), sum(i['gabarito'] == 'E' for i in v)] for l, v in por_lote.items()})
    chk('C-TOTAIS.lote_v114', 'itens por lote na v1.14 (D1 72, D2 160, D3 160, D4 136, D5 70, D6 50)', ESP_LOTE_V114, {l: sum(1 for i in itens if i['id'].startswith(l + '-')) for l in ESP_LOTE_V114})
    bq_ids = [i['id'] for i in itens[:142]]
    chk('C-TOTAIS.banco', 'banco: 142 itens (106 + 36) no bloco contíguo inicial, em ordem de id; nenhum BQ depois', [142, True, True], [sum(1 for i in itens if i['id'].startswith('BQ-')), all(x.startswith('BQ-') for x in bq_ids) and bq_ids == sorted(bq_ids), not any(i['id'].startswith('BQ-') for i in itens[142:])])
    eds = {e['id'] for e in pac['edital']}
    chk('C-TOTAIS.edital', 'todo itemEdital existe no edital', [], sorted({i['itemEdital'] for i in itens if i['itemEdital'] not in eds}))
    chk('C-TOTAIS.ordem', 'ordem de itens: bloco de banco da v1.13 (106), 36 novos, 1.053 não-banco da v1.13 e 238 de reforço', True,
        ids == [x for x in bids if x.startswith('BQ-')] + sorted(x for x in ids if x.startswith('BQ-') and x not in bset) + [x for x in bids if not x.startswith('BQ-')] + [x for x in rel])
    # ============================================================== C-REFORCO
    enun, j2, oc = aplica_erratas(rel)
    chk('C-REFORCO.ids', 'os 238 ids do pacote = os 238 ids das levas, na ordem das levas', [x for x in rel], [i['id'] for i in refo])
    dif = []
    for x, v in rel.items():
        it = by.get(x)
        if it is None or it['enunciado'] != enun[x] or it['gabarito'] != v['gab'] or it['itemEdital'] != v['ie'] or it['aderencia'] != v['ader']:
            dif.append(x)
    chk('C-REFORCO.texto', 'enunciado, gabarito, itemEdital e aderência de cada um dos 238 = releitura independente da leva, com as erratas', [], dif)
    chk('C-REFORCO.erratas', 'erratas D3-R13, D3-R18 e D3-R75: antes 1 vez e depois 0 vez antes de aplicar', {'D3-R13': [1, 0], 'D3-R18': [1, 0], 'D3-R75': [1, 0]}, {k: list(v) for k, v in oc.items()})
    chk('C-REFORCO.d3r13_r18', 'D3-R13 e D3-R18: enunciado esperado inteiro (o "depois" ocorre 1 vez e o "antes" 0)', [[1, 0], [1, 0]],
        [[by['D3-R13']['enunciado'].count(M.ERRATAS[0][4]), by['D3-R13']['enunciado'].count(M.ERRATAS[0][3])], [by['D3-R18']['enunciado'].count(M.ERRATAS[1][4]), by['D3-R18']['enunciado'].count(M.ERRATAS[1][3])]] if 'D3-R13' in by and 'D3-R18' in by else None)
    chk('C-REFORCO.d3r75', 'D3-R75: linha 2 da justificativa = texto da seção 2.2 da D1 (por igualdade) e contida na justificativa do item', [D3R75_LINHA2, True], [j2.get('D3-R75'), D3R75_LINHA2 in by['D3-R75']['justificativa'] if 'D3-R75' in by else None])
    chk('C-REFORCO.e3e4', 'AJ-L8-E3 e AJ-L8-E4 sem aceite: o "antes" ocorre 1 vez no enunciado do D4-R42 e do D4-R52', [1, 1], [by['D4-R42']['enunciado'].count(E3E4[0][2]) if 'D4-R42' in by else None, by['D4-R52']['enunciado'].count(E3E4[1][2]) if 'D4-R52' in by else None])
    chk('C-REFORCO.vagos', 'D1-R03 e D4-R12 ausentes; D3-R75 logo depois do D3-R74', [False, False, True], [
        'D1-R03' in by, 'D4-R12' in by, ('D3-R74' in ids and 'D3-R75' in ids and ids.index('D3-R75') == ids.index('D3-R74') + 1)])
    chk('C-REFORCO.parciais', 'aderencia "parcial" exatamente nos 35 ids; nenhum volatil nos 238', [sorted(PARCIAIS), 0], [sorted(i['id'] for i in refo if i['aderencia'] == 'parcial'), sum('volatil' in i for i in refo)])
    chk('C-REFORCO.fixos', 'campos fixos e ordem dos campos dos 238 (rotulo AUTORAL; certame; cargo; ano 2026; numero = o nn do id; comando; textoBase ""; url = arquivo da leva)', [],
        [i['id'] for i in refo if not (list(i) == CAMPOS_DA and i['rotulo'] == 'AUTORAL' and i['certame'] == 'Projeto Câmara 2026' and i['cargo'] == 'Noções de Direito Administrativo e Administração Pública' and i['ano'] == 2026
                                          and i['numero'] == int(i['id'].split('-R')[1]) and i['comando'] == 'Julgue o item a seguir.' and i['textoBase'] == '' and rel.get(i['id']) and i['url'] == 'saida/gcb/DA_reforco_leva%d_v2.md' % rel[i['id']]['leva'])])
    # ============================================================== C-JUST
    jx, nsub, ruins = justificativas(rel, j2, ins['csv'])
    chk('C-JUST.subs', 'as 91 substituições da GCB: cada antes exatamente 1 vez (texto corrente), campo justificativa', [91, []], [nsub, ruins])
    chk('C-JUST.texto', 'justificativa dos 238 = j1 + " " + j2, depois das erratas e das substituições da GCB', [], [x for x in rel if x not in by or by[x]['justificativa'] != jx[x]])
    # ============================================================== C-MARCAS
    novos = refo + [i for i in itens if i['id'].startswith('BQ-') and i['id'] not in bset]
    hits = []; hproc = []; xs = collections.Counter()
    for it in novos:
        for campo in ('enunciado', 'justificativa'):
            t = it[campo]
            for r in MV.cmarcas(t):
                hits.append((it['id'], campo, r[0], r[1]))
            o, x = MV.processo(it['id'] + '.' + campo, t)
            xs.update(x)
            for r in o:
                hproc.append((it['id'], campo, r[0], r[1]))
    chk('C-MARCAS.n', 'itens novos varridos (238 de reforço + 36 de banco)', 274, len(novos))
    chk('C-MARCAS.cm', 'C-MARCAS (D1, 8.1) em enunciado e justificativa dos 274: 0 ocorrências', [], hits)
    chk('C-MARCAS.processo', 'PROCESSO (marcas_processo.py, lista R; SHA-256 LF 7ee30de4…c140) em enunciado e justificativa dos 274: 0 fora da lista X de conteúdo', [], hproc)
    chk('C-MARCAS.x', 'lista X de conteúdo ("Presidência da República" em D2-R21 e D2-R24, justificativa): contagem real = esperada', {r[0]: r[5] for r in MV.X_CONTEUDO}, dict(xs))
    # ============================================================== C-BANCO
    rows = {d['id']: d for d in ctx['banco']}
    sel = sorted(d['id'] for d in ctx['banco'] if d['item_edital_camara'].startswith('P1-DA') and d['anulado'] == 'nao' and d['id'] not in M.BANCO_FORA)
    novos_bq = [i for i in itens if i['id'].startswith('BQ-') and i['id'] not in bset]
    chk('C-BANCO.ids', 'os 36 ids do banco P1-DA (BQ-0113 a BQ-0130, 0132, 0134 a 0140, 0142 a 0150, 0152), na ordem do id', [36, sel], [len(novos_bq), [i['id'] for i in novos_bq]])
    exp_ids = ['BQ-%04d' % k for k in list(range(113, 131)) + [132] + list(range(134, 141)) + list(range(142, 151)) + [152]]
    chk('C-BANCO.lista_D1', 'os 36 ids = a lista da seção 2.3 da D1', exp_ids, sel)

    def mapa(d):
        return collections.OrderedDict([('id', d['id']), ('rotulo', d['rotulo']), ('certame', d['certame']), ('cargo', d['cargo']), ('ano', int(d['ano_aplicacao'])), ('numero', int(d['numero_item'])), ('comando', d['texto_comando']),
                                        ('textoBase', d['texto_base']), ('enunciado', d['texto_integral']), ('gabarito', d['gabarito']), ('justificativa', ''), ('itemEdital', d['item_edital_camara']), ('aderencia', d['aderencia']), ('url', d['url_caderno'])])
    chk('C-BANCO.campos', 'os 13 campos (e o id) de cada um dos 36 = colunas de banco.csv (mapeamento da seção 2.3); ordem dos campos', [], [i['id'] for i in novos_bq if i != mapa(rows[i['id']]) or list(i) != CAMPOS_DA])
    chk('C-BANCO.sem_opcionais', 'nenhum dos 36 tem nota, volatil, interno nem comandoOriginal', 0, sum(1 for i in novos_bq for k in ('nota', 'volatil', 'interno', 'comandoOriginal') if k in i))
    chk('C-BANCO.atributos', '36: CEBRASPE_ANALOGA, aderência direta, C/E 26/10', [36, 36, 26, 10], [sum(i['rotulo'] == 'CEBRASPE_ANALOGA' for i in novos_bq), sum(i['aderencia'] == 'direta' for i in novos_bq), sum(i['gabarito'] == 'C' for i in novos_bq), sum(i['gabarito'] == 'E' for i in novos_bq)])
    chk('C-BANCO.ausentes', 'BQ-0131, BQ-0133, BQ-0141 e BQ-0151 ausentes do pacote', [], [x for x in ('BQ-0131', 'BQ-0133', 'BQ-0141', 'BQ-0151') if x in by])
    chk('C-BANCO.linhas', 'os 36 não têm "QA PENDENTE" em observacoes e não são anulados', [], [i['id'] for i in novos_bq if 'QA PENDENTE' in rows[i['id']]['observacoes'] or rows[i['id']]['anulado'] != 'nao'])
    antigos = [i for i in bp['itens'] if i['id'].startswith('BQ-')]
    chk('C-BANCO.mapeamento_106', 'o mesmo mapeamento reproduz os 13 campos dos 106 itens de banco da v1.13 (campos de dados; ignorando interno/nota/volatil/comandoOriginal)', [106, []],
        [len(antigos), [i['id'] for i in antigos if {k: v for k, v in i.items() if k in CAMPOS_DA} != {k: v for k, v in mapa(rows[i['id']]).items()}]])
    # ============================================================== C-ESTUDANTE
    chk('C-ESTUDANTE.cabecalho', 'nome v1.14-E; versao e geradoEm iguais aos do pacote.json; geradoEm > 2026-10-20', [M.NOME_E, pac['versao'], pac['geradoEm'], True], [est['nome'], est['versao'], est['geradoEm'], est['geradoEm'] > '2026-10-20'])
    chk('C-ESTUDANTE.nome_pacote', 'pacote.json: nome v1.14', M.NOME_P, pac['nome'])
    dif = []
    for i in itens:
        e = ebid.get(i['id'])
        if e is None: dif.append(i['id']); continue
        if i['id'] in bset:
            ok = True            # itens da v1.13: conferidos em C-INTACTA.estudante
        else:
            esp = {k: v for k, v in i.items()}
            if esp['rotulo'] == 'AUTORAL': esp['url'] = ''
            ok = {k: v for k, v in e.items() if k != 'nucleo'} == esp
        if not ok or list(e)[-1] != 'nucleo': dif.append(i['id'])
    chk('C-ESTUDANTE.texto', 'pacote_estudante: os 274 itens novos iguais aos do pacote.json, salvo url "" nos AUTORAL e nucleo como último campo; itens da v1.13 verificados em C-INTACTA', [], dif)
    chk('C-ESTUDANTE.url', 'url "" nos 238 de reforço do estudante; os 36 de banco mantêm a URL oficial', [238, 36], [sum(1 for i in est['itens'] if RX_REF.fullmatch(i['id']) and i['url'] == ''), sum(1 for i in est['itens'] if i['id'].startswith('BQ-') and i['id'] not in bset and i['url'].startswith('https://cdn.cebraspe.org.br/'))])
    nuc = {i['id']: i['nucleo'] for i in est['itens']}
    dae = [i for i in est['itens'] if i['itemEdital'].startswith('P1-DA-')]
    chk('C-ESTUDANTE.nucleo_totais', 'nucleo: 775 no total; DA 408 true / 276 false; banco P1-DA 36/36 true', [775, 408, 276, 36], [sum(nuc.values()), sum(i['nucleo'] for i in dae), sum(not i['nucleo'] for i in dae), sum(nuc[i['id']] for i in novos_bq)])
    flips = [i['id'] for i in be['itens'] if i['nucleo'] and not nuc[i['id']]]
    chk('C-ESTUDANTE.nucleo_12', 'itens da v1.13 que passam de true para false: os 12 (D1-07, D1-08, D3-79, D3-80, D6-07 a D6-10, D6-37 a D6-40); nenhum de false para true', [M.FLIPS_ESP, []], [flips, [i['id'] for i in be['itens'] if not i['nucleo'] and nuc[i['id']]]])
    chk('C-ESTUDANTE.nucleo_18', 'reforço com nucleo true: os 18 ids da seção 6', sorted(M.NUC18), sorted(i['id'] for i in est['itens'] if RX_REF.fullmatch(i['id']) and i['nucleo']))
    chk('C-ESTUDANTE.nucleo_fora_DA', 'nucleo fora de DA igual ao da v1.13, por id', [], [i['id'] for i in be['itens'] if not i['itemEdital'].startswith('P1-DA-') and nuc[i['id']] != i['nucleo']])
    # recontagem independente k1 a k4 (DA por implementação própria; fora de DA pelo nucleo.py do gerador_v1_12)
    dec = ins['dec'].decode('utf-8').split('\n')

    def linha_do_ato(ato):
        for k, l in enumerate(dec, 1):
            if l.startswith('APLICADA') and ('| %s |' % ato) in l:
                return k
        return None
    rb = {x: v['leva'] for x, v in rel.items()}
    datas = {d['id']: d['data_verificacao'] for d in ctx['banco']}
    chaves = {}
    for pos, i in enumerate(est['itens']):
        if not i['itemEdital'].startswith('P1-DA-'): continue
        x = i['id']
        if x.startswith('BQ-'): k1, k2 = datas[x], 0
        else:
            m = re.fullmatch(r'D([1-6])-(R)?(\d\d)', x)
            ch = ('R75' if x == 'D3-R75' else rb.get(x)) if m.group(2) else 'D' + m.group(1)
            if ch not in ATO_DATA:      # id de reforço sem ato de aceite (fora das levas): chave sentinela, a recontagem acusa
                chaves[x] = (i['itemEdital'], ('9999-99-99', 0, 0, pos)); continue
            ato, k1 = ATO_DATA[ch]; k2 = linha_do_ato(ato)
        chaves[x] = (i['itemEdital'], (k1, k2, 0 if i['aderencia'] == 'direta' else 1, pos))
    rec = {}
    pf = collections.defaultdict(list)
    for x, (f, k) in chaves.items(): pf[f].append((k, x))
    for f, L in pf.items():
        for r, (k, x) in enumerate(sorted(L)): rec[x] = r < 10
    try:
        sys.path.insert(0, os.path.join(R, 'saida', 'pacote', 'gerador_v1_12'))
        import nucleo as NV12
        sub = {'itens': [i for i in itens if not i['itemEdital'].startswith('P1-DA-')]}
        nuc12, _rel, _K = NV12.calcula(sub)
        rec.update(nuc12); fonte12 = 'nucleo.py do gerador_v1_12 sobre os 749 itens fora de DA'
    except Exception as e:      # sem o módulo: cai para a v1.13 por id
        rec.update({i['id']: i['nucleo'] for i in be['itens'] if not i['itemEdital'].startswith('P1-DA-')}); fonte12 = 'v1.13 por id (nucleo.py indisponível: %s)' % e
    chk('C-ESTUDANTE.recontagem', 'recontagem independente k1 a k4 (DA: implementação própria; fora de DA: %s) = nucleo do pacote_estudante em 1.433/1.433' % fonte12, 1433, sum(1 for i in est['itens'] if rec.get(i['id']) == i['nucleo']))
    # ============================================================== C-FOLHAS (números da seção 9, recontados)
    leaf = lambda f, ids_: not any(j != f and j.startswith(f + '.') for j in ids_)
    eids = [e['id'] for e in pac['edital']]
    f_p1 = [e['id'] for e in pac['edital'] if e['prova'] == 'P1' and not e['id'].startswith('P1-DA-') and leaf(e['id'], eids)]
    f_p2 = [e['id'] for e in pac['edital'] if e['prova'] == 'P2' and leaf(e['id'], eids)]
    f_da = [e['id'] for e in pac['edital'] if e['id'].startswith('P1-DA-') and leaf(e['id'], eids)]
    cnt = collections.Counter(i['itemEdital'] for i in itens)
    chk('C-FOLHAS.folhas', '75 folhas (P1 15, P2 23, DA 37)', [15, 23, 37, 75], [len(f_p1), len(f_p2), len(f_da), len(f_p1) + len(f_p2) + len(f_da)])
    em_folha = sum(cnt[f] for f in f_da); fora = {k: v for k, v in cnt.items() if k.startswith('P1-DA-') and k not in f_da}
    chk('C-FOLHAS.da', 'DA: 684 itens, 644 em folha, 40 fora (P1-DA-1 12, 2 3, 3 5, 4 4, 5 3, 6 1, 8 7, 9 1, 10 4)', [684, 644, {'P1-DA-1': 12, 'P1-DA-2': 3, 'P1-DA-3': 5, 'P1-DA-4': 4, 'P1-DA-5': 3, 'P1-DA-6': 1, 'P1-DA-8': 7, 'P1-DA-9': 1, 'P1-DA-10': 4}], [em_folha + sum(fora.values()), em_folha, fora])
    chk('C-FOLHAS.20', 'DA: 25 folhas com 20 ou mais e 12 abaixo (1.1 e 1.2 com 11; 9.2, 9.3, 9.4 e 10.1 a 10.7 com 10)', [25, {'P1-DA-1.1': 11, 'P1-DA-1.2': 11, 'P1-DA-9.2': 10, 'P1-DA-9.3': 10, 'P1-DA-9.4': 10, **{'P1-DA-10.%d' % k: 10 for k in range(1, 8)}}],
        [sum(cnt[f] >= 20 for f in f_da), {f: cnt[f] for f in f_da if cnt[f] < 20}])
    pa = collections.Counter(i['itemEdital'] for i in da if i['aderencia'] == 'parcial')
    chk('C-FOLHAS.reais_vol_parc', 'DA: 36 reais, 5 VOLÁTEIS, 35 parciais (5.2 4, 6.1 8, 6.2 5, 6.3 8, 6.4 6, 6.5 3, 8.3 1)', [36, 5, 35, {'P1-DA-5.2': 4, 'P1-DA-6.1': 8, 'P1-DA-6.2': 5, 'P1-DA-6.3': 8, 'P1-DA-6.4': 6, 'P1-DA-6.5': 3, 'P1-DA-8.3': 1}],
        [sum(i['rotulo'] != 'AUTORAL' for i in da), sum(bool(i.get('volatil')) for i in da), sum(pa.values()), dict(pa)])
    chk('C-FOLHAS.p1p2', 'P1 de TI e P2: contagens por folha (total, parciais, voláteis) iguais às da v1.13', [], [f for f in f_p1 + f_p2 if (cnt[f], sum(1 for i in itens if i['itemEdital'] == f and i['aderencia'] == 'parcial'), sum(1 for i in itens if i['itemEdital'] == f and i.get('volatil')))
                                                                                                          != (sum(1 for i in bp['itens'] if i['itemEdital'] == f), sum(1 for i in bp['itens'] if i['itemEdital'] == f and i['aderencia'] == 'parcial'), sum(1 for i in bp['itens'] if i['itemEdital'] == f and i.get('volatil')))])
    if fs:
        cj = lj(open(os.path.join(OUT, 'cobertura_v1_14.json'), 'rb').read())
        chk('C-FOLHAS.cobertura_json', 'out/cobertura_v1_14.json (insumo da secretaria): todas as conferências OK', [], [c['id'] for c in cj['criterios'] if c['resultado'] != 'OK'])
    # ============================================================== C-DIAG30
    bd = lj(open(os.path.join(R, 'saida', 'pacote', 'montagem_v1_13', 'out', 'diag30_DA.json'), 'rb').read().replace(b'\r\n', b'\n'))
    sim = {x for s in pac['simulados'] for x in s['itens']}
    d30 = [by.get(x) for x in bd['ids']]
    chk('C-DIAG30.da', 'DIAG30.DA: os 30 ids existem; todos DA, diretos, não voláteis e fora de simulado; folhas = as de diag30_DA.json; C/E 15/15', [30, [], bd['folhas'], 15, 15],
        [sum(x is not None for x in d30), [x['id'] for x in d30 if x and not (x['itemEdital'].startswith('P1-DA-') and x['aderencia'] == 'direta' and not x.get('volatil') and x['id'] not in sim)], [x['itemEdital'] for x in d30 if x],
         sum(x['gabarito'] == 'C' for x in d30 if x), sum(x['gabarito'] == 'E' for x in d30 if x)])
    if fs:
        tpl = open(os.path.join(R, 'saida', 'plataforma', 'plataforma_v16_final_template.html'), 'rb').read().replace(b'\r\n', b'\n').decode('utf-8')
        D = json.loads(re.findall(r'const DIAG30 = (\{.*?\});\n', tpl, re.S)[0])
        chk('C-DIAG30.p1p2', 'DIAG30.P1 e P2: os ids continuam existindo, com os mesmos atributos da v1.13', [], [x for m in ('P1', 'P2') for x in D[m] if x not in by or x not in bset or by[x] != next(b for b in bp['itens'] if b['id'] == x)])
        chk('C-DIAG30.da_ids', 'DIAG30.DA do template = ids de diag30_DA.json', bd['ids'], D['DA'])
        dc = lj(open(os.path.join(OUT, 'diag30_check_v1_14.json'), 'rb').read())
        chk('C-DIAG30.json', 'out/diag30_check_v1_14.json: 0 FALHA', 0, dc['falhas'])
    # ============================================================== C-MOLDURA
    if fs:
        import moldura_v1_14 as MO
        classificar, materia, hmo = MO.carrega_criterio()
        L14 = MO.classifica_pacote(itens, classificar, materia)
        t14, u14 = MO.totais(L14)
        mj = lj(open(os.path.join(OUT, 'moldura_v1_14.json'), 'rb').read())
        chk('C-MOLDURA.totais', 'totais por matéria (moldura S: itens, C, E, %C) recontados e gravados em out/moldura_v1_14.json', json.loads(json.dumps(t14)), mj['totais_por_materia_v1_14'])
        chk('C-MOLDURA.universo', 'universo por matéria (itens, S, %S) gravado', json.loads(json.dumps(u14)), mj['universo_por_materia_v1_14'])
        chk('C-MOLDURA.divergencias', 'divergências do campo "Moldura:" das 8 levas (238 itens) listadas no JSON, sem corrigir (n registrado; a decisão é da gbq-gerencia)', 'listadas', 'listadas' if isinstance(mj['divergencias_campo_moldura_das_levas']['itens'], list) and mj['divergencias_campo_moldura_das_levas']['de'] == 238 else None)
        chk('C-MOLDURA.criterio', 'critério de saida/banco/moldura_ce.py aplicado sem alteração (SHA-256 LF 5723698e…ca96)', [True, True], [hmo.startswith('5723698e') and hmo.endswith('ca96'), mj['criterio']['sha256_lf'] == hmo])
        # ============================================================== C-MD
        mdj = lj(open(os.path.join(OUT, 'estudante_md_v1_14.json'), 'rb').read())
        chk('C-MD.json', 'out/estudante_md_v1_14.json: 0 FALHA e 53 arquivos', [0, 53], [mdj['falhas'], mdj['arquivos']])
        pasta = os.path.join(OUT, 'estudante')
        arqs = sorted(os.listdir(pasta))
        txt = {n: open(os.path.join(pasta, n), 'rb').read().decode('utf-8') for n in arqs}
        base_dir = os.path.join(R, 'saida', 'pacote', 'montagem_v1_13', 'out', 'estudante')
        bt = {n: open(os.path.join(base_dir, n), 'rb').read().decode('utf-8') for n in sorted(os.listdir(base_dir))}
        chk('C-MD.arquivos', '53 arquivos com os mesmos nomes da v1.13-E; mudam 12; 41 iguais byte a byte', [bt.keys() == txt.keys(), 12, 41], [bt.keys() == txt.keys(), sum(txt[n] != bt[n] for n in txt if n in bt), sum(txt[n] == bt[n] for n in txt if n in bt)])
        ids_novos = [i['id'] for i in novos]
        ci = collections.Counter(); cg = collections.Counter()
        for n, t in txt.items():
            if n.endswith('_itens.md'):
                for x in ids_novos:
                    ci[x] += len(re.findall(r'^(?:\*\*%s\*\* — |### %s\n)' % (re.escape(x), re.escape(x)), t, re.M))
            if n.endswith('_gabarito.md'):
                for x in ids_novos:
                    cg[x] += len(re.findall(r'^### %s — Gabarito: ' % re.escape(x), t, re.M))
        chk('C-MD.ids', 'cada um dos 274 ids novos aparece exatamente 1 vez nos _itens e 1 vez nos _gabarito', [], [x for x in ids_novos if ci[x] != 1 or cg[x] != 1])
        chk('C-MD.texto', 'enunciado, gabarito e justificativa dos 274 nos .md = pacote_estudante (conferido por estudante_md_v114.py: M6.1 a M6.3)', [], [c['id'] for c in mdj['conferencias'] if c['id'].startswith('M6') and c['resultado'] != 'OK'])
        chk('C-MD.marcas', 'C-MARCAS nos 12 arquivos que mudam, com a máscara de ids (estudante_md_v114.py: M7.1 a M7.3)', [], [c['id'] for c in mdj['conferencias'] if c['id'].startswith('M7') and c['resultado'] != 'OK'])
        chk('C-MD.sem_dupla_negrito', 'pares e pegadinhas de DA sem ** (ponto 2 da v1.2.11): 0 nas seções dos 6 DA_D<n>_estudo.md', 0,
            sum(t[t.index('\n## Pares\n'):(t.find('\n## Tópico ') if t.find('\n## Tópico ') > 0 else len(t))].count('**') for n, t in txt.items() if n.startswith('DA_D') and n.endswith('_estudo.md')))
        linhas = ''.join('estudante/%s\t%s\n' % (n, sha(txt[n].encode('utf-8'))) for n in sorted(txt, key=lambda s: ('estudante/' + s).encode('utf-8')))
        chk('C-MD.digest', 'digest da .md (forma R2-D: linhas "estudante/<nome>.md" TAB sha256, em ordem de bytes, com \\n final) recalculado = o gravado', mdj['digest_md_R2D'], sha(linhas.encode('utf-8')))
        nm = txt['NUCLEO.md']
        chk('C-MD.nucleo', 'NUCLEO.md: 775 ids núcleo', 775, sum(len(l.split(': ', 1)[1].split(', ')) for l in nm.split('\n') if l.startswith('- ')))
        chk('C-MD.readme', 'README: v1.14-E, data 2026-10-23 e linha de DA com 684 itens, sendo 36 de provas anteriores', [True, True, True], ['- Versão: v1.14-E' in txt['README.md'], '- Data: 2026-10-23' in txt['README.md'], '684 itens, sendo 36 de provas anteriores' in txt['README.md']])
        # ============================================================== C-MANIFESTO
        mp = os.path.join(HERE, 'MANIFESTO_v1_14.md')
        if not os.path.isfile(mp):
            chk('C-MANIFESTO', 'a pasta real é igual ao MANIFESTO_v1_14.md (bytes e SHA-256 de cada arquivo; contagem pela pasta real)', 'igual', 'MANIFESTO ainda não gerado', estado='PENDENTE')
        else:
            mt = open(mp, 'rb').read().replace(b'\r\n', b'\n').decode('utf-8').split('\n')
            mrows = {m.group(1): (int(m.group(2)), m.group(3)) for m in (re.match(r'^\| (saida/pacote/montagem_v1_14/\S+) \| (\d+) \| ([0-9a-f]{64}) \|$', l) for l in mt) if m}
            real = {}
            for dp, dn, fnn in os.walk(HERE):
                dn[:] = [d for d in dn if d != '__pycache__']
                for f in fnn:
                    if f == 'MANIFESTO_v1_14.md': continue
                    p = os.path.join(dp, f); rel_ = os.path.relpath(p, R).replace(os.sep, '/')
                    b = open(p, 'rb').read()
                    real[rel_] = (len(b), sha(b))
            auto = 'saida/pacote/montagem_v1_14/out/conferencia_t123.json'     # o próprio resultado não entra na comparação (não pode conter o seu SHA-256)
            dif = sorted(k for k in set(real) | set(mrows) if k != auto and real.get(k) != mrows.get(k))
            tot_decl = [int(m.group(1)) for m in (re.search(r'Total: (\d+) arquivos', l) for l in mt) if m]
            chk('C-MANIFESTO', 'a pasta real é igual ao MANIFESTO_v1_14.md (bytes e SHA-256 de cada arquivo, exceto a própria conferencia_t123.json); total declarado = arquivos da pasta real', [[], [len(real)]], [dif, tot_decl])
    return CRIT


def main():
    ctx = carregar_ctx()
    C = executa(ctx, fs=True)
    for c in C:
        print('%-8s %s — %s%s' % (c['resultado'], c['id'], c['criterio'], '' if c['resultado'] == 'OK' else '  [esperado=%s obtido=%s]' % (json.dumps(c['esperado'], ensure_ascii=False)[:400], json.dumps(c['obtido'], ensure_ascii=False)[:600])))
    nf = sum(c['resultado'] == 'FALHA' for c in C); npend = sum(c['resultado'] == 'PENDENTE' for c in C); nok = sum(c['resultado'] == 'OK' for c in C)
    grupos = collections.OrderedDict()
    for c in C:
        g = c['id'].split('.')[0]
        grupos.setdefault(g, collections.Counter())[c['resultado']] += 1
    res = collections.OrderedDict(tarefa='T-123 (D1 da GBQ, seção 8.1)', script='saida/pacote/montagem_v1_14/conferir_t123.py',
                                  entradas={M.PATH[k]: sha(v) for k, v in ctx['ins'].items() if k != 'dec'}, saidas={'out/pacote.json': sha(ctx['pac_b']), 'out/pacote_estudante.json': sha(ctx['est_b'])},
                                  total_criterios=len(C), OK=nok, FALHA=nf, PENDENTE=npend, por_grupo={g: dict(v) for g, v in grupos.items()}, criterios=C)
    M.grava(os.path.join(OUT, 'conferencia_t123.json'), (json.dumps(res, ensure_ascii=False, indent=1) + '\n').encode('utf-8'))
    print('RESULTADO: %d critérios, %d OK, %d FALHA, %d PENDENTE' % (len(C), nok, nf, npend))
    sys.exit(1 if (nf or npend) else 0)


if __name__ == '__main__':
    main()
