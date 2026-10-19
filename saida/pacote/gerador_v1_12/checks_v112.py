# -*- coding: utf-8 -*-
"""T-115 (gerador_v1_12, D1 da GBQ, seção 4) — conferências como funções puras sobre um pacote P (dict) e um contexto `Ctx` lido das FONTES (os 23 insumos, o blob da v1.11 e DECISOES.md), para
servirem tanto a validate_v112.py e conferencias_v112.py (sobre os arquivos de out/) quanto aos testes de mutação (fidelidade_mutacao_v112.py: P ou a fonte alterados em cópia). Cada função devolve
uma lista de (id, ok, mensagem). Nada é gravado aqui. A leitura das fontes passa por fontes_v112 (SHA-256 LF); o contexto repete, por código próprio, a montagem esperada dos itens novos, das pegadinhas
e dos tópicos (comparação byte a byte com o P), em vez de reusar o objeto que o build gerou."""
import collections, copy, csv, hashlib, json, os, re
from common import OUT, REPO, P as PATH
import refs, config_v112 as cfg
import fontes_v112 as F
from fontes_v112 import Falha
import reforco_v112 as R
import limpeza_v112 as L
import pegadinhas_v112 as PG
import topicos_v112 as TP
import inventario_v112 as I
import nucleo as NU


def dumps(o):
    return json.dumps(o, ensure_ascii=False)


class Ctx:
    """Fontes lidas uma vez: base v1.11 (pacote e -E), itens novos esperados (com erratas e limpeza), pegadinhas, tópicos, VOLÁTEIS da T-11, DECISOES.md."""

    def __init__(self):
        raw = refs.git_show(cfg.BASE[0], cfg.BASE[1])
        self.raw0 = raw
        self.P0 = json.loads(raw.decode('utf-8'), object_pairs_hook=collections.OrderedDict)
        self.E0 = json.loads(refs.git_show(cfg.BASE_E[0], cfg.BASE_E[1]).decode('utf-8'), object_pairs_hook=collections.OrderedDict)
        self.ids0 = {i['id'] for i in self.P0['itens']}
        itens, meta, info = R.carrega(self.ids0)
        self.erratas, self.urls = L.aplica_erratas(itens, meta)
        self.just_arquivo = {i['id']: i['justificativa'] for i in itens}
        self.enun_arquivo = {}
        self.linhas_limpeza = L.limpa_itens(itens)
        self.itens, self.meta, self.vl = itens, meta, info
        self.entradas = PG.le_entradas()
        self.edital_ids = [e['id'] for e in self.P0['edital']]
        self.topicos, self.fontes_top = TP.monta(self.edital_ids)
        self.estilo = F.le_insumo(cfg.ESTILO_ARQUIVO)
        self.dec = open(PATH('DECISOES.md'), encoding='utf-8').read()
        self.vol_t11 = self.le_t11()
        self.banco = self.le_banco()

    def le_t11(self):
        t = open(PATH(cfg.T11_VOLATEIS), encoding='utf-8').read().replace('\r\n', '\n')
        sec = t.split('## 1.')[1].split('\n## 2.')[0]
        return re.findall(r'^\| \d+ \| (L\d-R\d+) \|', sec, re.M)

    def le_banco(self):
        rows = list(csv.DictReader(open(PATH('banco/banco.csv'), encoding='utf-8', newline=''), delimiter=';'))
        return rows


def ok_(res, i, c, m):
    res.append((i, bool(c), m))


# ---------------------------------------------------------------- pegadinhas esperadas (código próprio)
def pegadinhas_esperadas(P0, entradas):
    out = {}
    for L_ in P0['lotes']:
        lt = L_['id']
        base = [dict(g) for g in L_['pegadinhas']]
        ult = {}
        for k, g in enumerate(base):
            ult[g['itemEdital']] = k
        grupo = collections.defaultdict(list)
        for e in entradas:
            if e['lote'] == lt:
                grupo[ult[e['itemEdital']]].append(e)
        lista = []
        for k, g in enumerate(base):
            lista.append(collections.OrderedDict(g))
            for e in grupo.get(k, []):
                lista.append(collections.OrderedDict([('itemEdital', e['itemEdital']), ('rotulo', e['rotulo']), ('texto', e['texto'])]))
        out[lt] = lista
    return out


# ---------------------------------------------------------------- conferências sobre o pacote.json (P)
def checa_pacote(P, ctx):
    res = []
    P0 = ctx.P0
    n0 = cfg.BASE_ITENS
    ids = [i['id'] for i in P['itens']]
    ok_(res, 'A1', list(P) == list(P0) + ['topicos'] and P['versao'] == 1 and P['nome'] == cfg.NOME and P['geradoEm'] == cfg.GERADO_EM and list(P)[-1] == 'topicos',
        'pacote.json: versao 1, nome e geradoEm de config_v112, chaves de topo da v1.11 mais `topicos` (último)')
    ok_(res, 'C-1p', len(P['itens']) >= n0 and dumps(P['itens'][:n0]) == dumps(P0['itens']), 'C-1\': os %d itens da v1.11: id, ordem e todos os campos iguais ao blob v1.11 (byte a byte na serialização)' % n0)
    # lotes
    esp_peg = pegadinhas_esperadas(P0, ctx.entradas)
    dif = []
    lp = {L_['id']: L_ for L_ in P['lotes']}
    for L0 in P0['lotes']:
        L1 = lp.get(L0['id'])
        if L1 is None:
            dif.append(L0['id'] + ' ausente'); continue
        for c in ('itensEdital', 'prova', 'resumo', 'curso', 'pares'):
            if dumps(L0[c]) != dumps(L1[c]):
                dif.append('%s.%s' % (L0['id'], c))
        if dumps(esp_peg[L0['id']]) != dumps(L1['pegadinhas']):
            dif.append('%s.pegadinhas' % L0['id'])
        if L1['nome'] != cfg.NOMES_LOTE[L0['id']][1]:
            dif.append('%s.nome' % L0['id'])
        if 'legendaMecanismo' in L1:
            dif.append('%s.legendaMecanismo' % L0['id'])
        k0 = [c for c in L0 if c not in ('legendaMecanismo', 'interno')]
        k1 = [c for c in L1 if c != 'interno']
        if k0 != k1:
            dif.append('%s chaves' % L0['id'])
        if 'interno' in L1 and list(L1)[-1] != 'interno':
            dif.append('%s interno não é o último' % L0['id'])
    ok_(res, 'C-2p', not dif and [L_['id'] for L_ in P['lotes']] == [L_['id'] for L_ in P0['lotes']] and sum(len(L_['pegadinhas']) for L_ in P['lotes']) == cfg.TOTAIS['pegadinhas'],
        "C-2': lotes: curso, resumo, pares, itensEdital e prova iguais; pegadinhas = lista da v1.11 com as 73 inseridas nas posições da seção 3.6 (por código próprio); nome e legendaMecanismo só como na seção 3.8 (%s)" % (dif[:3] or 'sem diferença'))
    # simulados e discursivas
    ds = []
    sp = {s['id']: s for s in P['simulados']}
    for s0 in P0['simulados']:
        s1 = sp.get(s0['id'])
        if s1 is None:
            ds.append(s0['id']); continue
        a, b = dict(s0), dict(s1)
        for x in (a, b):
            x.pop('interno', None)
        if s0['id'] == 'SIM-0':
            if b['nome'] != cfg.SIM0_NOME[1] or a['nome'] != cfg.SIM0_NOME[0]:
                ds.append('SIM-0 nome')
            a.pop('nome'); b.pop('nome')
        if dumps(a) != dumps(b):
            ds.append(s0['id'])
    if dumps([{k: v for k, v in d.items()} for d in P['discursivas']]) != dumps(P0['discursivas']):
        ds.append('discursivas')
    if dumps(P['edital']) != dumps(P0['edital']):
        ds.append('edital')
    ok_(res, 'C-3p', not ds, "C-3': simulados e discursivas iguais à v1.11, salvo o `nome` do SIM-0 e o `interno` dele (%s)" % (ds or 'sem diferença'))
    # itens novos
    novos = P['itens'][n0:]
    esp_ids = [i['id'] for i in ctx.itens]
    ok_(res, 'C-N1a', len(P['itens']) == cfg.TOTAIS['itens'] and len(set(ids)) == len(ids) and [i['id'] for i in novos] == esp_ids,
        'C-N1: %d itens, ids únicos; os 189 novos na ordem da seção 3.3 (onda 4, F1 P1, F1 P2 A–D)' % len(P['itens']))
    esp_itens = []
    for it in ctx.itens:
        x = collections.OrderedDict(it)
        esp_itens.append(x)
    ok_(res, 'C-N1b', dumps(novos) == dumps(esp_itens), 'C-N1: cada item novo = o lido do arquivo final, com a errata (se houver), a limpeza L-1 a L-5 e o `interno` (comparação byte a byte com a montagem própria da fonte)')
    cC = collections.Counter(i['gabarito'] for i in P['itens'])
    nv = [i for i in novos]
    cn = collections.Counter(i['gabarito'] for i in nv)
    gr = collections.OrderedDict()
    okg = True
    for gk, A in cfg.ACEITE.items():
        gi = [i for i in nv if ctx.meta.get(i['id'], {}).get('grupo') == gk]
        c = collections.Counter(i['gabarito'] for i in gi)
        vol = [i['id'] for i in gi if i.get('volatil')]
        par = [i['id'] for i in gi if i['aderencia'] == 'parcial']
        ts = sum(1 for i in gi if ctx.meta[i['id']]['ts'])
        f = dict(collections.Counter(i['itemEdital'] for i in gi))
        g_ok = len(gi) == A['n'] and (c['C'], c['E']) == (A['C'], A['E']) and vol == A['vol'] and sorted(par) == sorted(A['parcial']) and ts == A['ts'] and f == A['folha']
        okg &= g_ok
        gr[gk] = (len(gi), c['C'], c['E'], len(vol), len(par), ts)
    ok_(res, 'C-N1c', okg and (cC['C'], cC['E']) == (cfg.TOTAIS['C'], cfg.TOTAIS['E']), 'C-N1: por grupo (n, C, E, VOLÁTEIS, PARCIAIS, [TS]) %s e folhas conforme as constantes de aceite; total C/E %d/%d' % (dict(gr), cC['C'], cC['E']))
    # C-N2: folhas
    fol = collections.OrderedDict()
    for i in P['itens']:
        fol.setdefault(i['itemEdital'], []).append(i)
    d2 = []
    for f_, (v0, v1, c_, e_, dir_, par_, vol_) in cfg.FOLHAS_V112.items():
        its = fol.get(f_, [])
        its0 = [i for i in P0['itens'] if i['itemEdital'] == f_]
        got = (len(its0), len(its), sum(1 for i in its if i['gabarito'] == 'C'), sum(1 for i in its if i['gabarito'] == 'E'), sum(1 for i in its if i['aderencia'] == 'direta'),
               sum(1 for i in its if i['aderencia'] == 'parcial'), sum(1 for i in its if i.get('volatil')))
        if got != (v0, v1, c_, e_, dir_, par_, vol_):
            d2.append((f_, got, (v0, v1, c_, e_, dir_, par_, vol_)))
    ok_(res, 'C-N2', not d2, 'C-N2: as 19 folhas que mudam (total da base e da versão nova, C/E, diretos, PARCIAIS, VOLÁTEIS) = seção 8 da D1 %s' % (d2[:2] or ''))
    # C-E: erratas
    de = []
    pi = {i['id']: i for i in P['itens']}
    for rid, iid, antes, depois, n in cfg.ERRATAS:
        en = pi[iid]['enunciado'] if iid in pi else ''
        if antes in en or en.count(depois) != 1 or ctx.estilo.count(depois) != 1:
            de.append(rid)
    arqd = F.le_insumo(cfg.URL_ARQUIVO)
    ok_(res, 'C-E', not de and arqd.count(cfg.URL_ANTES) == 3 and arqd.count(cfg.URL_DEPOIS) == 0,
        'C-E: as 3 erratas (antes 1/1/1 vez na fonte; depois literal 1 vez no enunciado e na seção 2 do estilo) e a URL (3 ocorrências da antiga, 0 da nova no D_v2; fora do pacote) %s' % (de or ''))
    # C-L: limpeza
    dl, cont = [], collections.Counter()
    for it in novos:
        rec = it.get('interno', [])
        try:
            orig = L.reverte_item(it)
        except Falha as e:
            dl.append('%s %s' % (it['id'], e)); continue
        if orig != ctx.just_arquivo.get(it['id']):
            dl.append('%s: reverter o `interno` não devolve a justificativa lida do arquivo' % it['id'])
        for r in rec:
            cont[r['regra']] += 1
            if r['depois'] != '' or r['campo'] != 'justificativa' or not r['edicao'].startswith('T115-L-'):
                dl.append('%s: registro fora da forma' % it['id'])
    n_it = sum(1 for it in novos if it.get('interno'))
    esp = {r[0]: len(r[3]) for r in cfg.LIMPEZA}
    ok_(res, 'C-L', not dl and dict(cont) == esp and sum(cont.values()) == cfg.TOTAIS['delecoes'] and n_it == cfg.TOTAIS['itens_limpeza'],
        'C-L: limpeza: %d deleções por regra %s em %d itens; reverter o `interno` de cada item devolve a justificativa lida do arquivo final %s' % (sum(cont.values()), dict(cont), n_it, dl[:2] or ''))
    # C-R: varredura residual
    insp = I.varre(P, 'D')
    novos_ids = {i['id'] for i in novos}
    esp_novas = set()
    texts_novas = {(e['lote'], e['texto']) for e in ctx.entradas}
    for L_ in P['lotes']:
        for k, g in enumerate(L_['pegadinhas']):
            if (L_['id'], g['texto']) in texts_novas:
                esp_novas.add('lotes[%s].pegadinhas[%d].rotulo' % (L_['id'], k)); esp_novas.add('lotes[%s].pegadinhas[%d].texto' % (L_['id'], k))
    def no_escopo(cam):
        m = re.match(r'itens\[([^\]]+)\]\.justificativa$', cam)
        return (m and m.group(1) in novos_ids) or cam.startswith('topicos[') or cam in esp_novas
    sel = [o for o in insp if no_escopo(o['caminho'])]
    sujo = [o for o in sel if o['classe'] in ('PROCESSO', 'VERIFICAR')]
    cont_m = collections.Counter((o['caminho'], o['categoria'], o['casamento']) for o in sel if (o['caminho'], o['categoria'], o['casamento']) in cfg.MANTER)
    fora = collections.Counter((o['caminho'], o['categoria'], o['casamento']) for o in sujo if (o['caminho'], o['categoria'], o['casamento']) not in cfg.MANTER)
    f4 = [o for o in sel if (o['caminho'], o['categoria'], o['casamento']) in cfg.MANTER_FP_ESPERADO]
    ok_(res, 'C-R', not fora and dict(cont_m) == dict(cfg.MANTER) and len(f4) >= 1,
        'C-R: varredura residual (regras do inventario_v111, sem mudança, sobre justificativas dos 189, pegadinhas novas e `topicos`): 0 PROCESSO e 0 VERIFICAR fora da lista MANTER da seção 3.5 (%d ocorrências MANTER presentes, esperado %d; fora da lista: %s)' % (
            sum(cont_m.values()), sum(cfg.MANTER.values()), dict(fora) or 0))
    # C-T: topicos
    ok_(res, 'C-T', 'topicos' in P and dumps(P['topicos']) == dumps(ctx.topicos) and list(P['topicos']) == [k for k in ctx.edital_ids if k in P['topicos']] and len(P['topicos']) == cfg.TOTAIS['topicos']
        and not TP.valida_topicos(P['topicos'], ctx.edital_ids) and sum(1 for t in P['topicos'].values() if 'emUmMinuto' in t) == cfg.TOTAIS['pilotos'],
        'C-T: `topicos`: 40 chaves na ordem do edital; campos e regras do contrato v1.2.9, ponto 1; textos iguais aos blocos json dos arquivos 8 a 16 da tabela (só a fusão por chave)')
    # C-V, C-A
    vol = [i['id'] for i in P['itens'] if i.get('volatil')]
    vol0 = [i['id'] for i in P0['itens'] if i.get('volatil')]
    ok_(res, 'C-V', len(vol) == cfg.TOTAIS['volatil'] and sorted(vol) == sorted(vol0 + ctx.vol_t11) and len(ctx.vol_t11) == cfg.TOTAIS['volatil_novos'],
        'C-V: `volatil: true` em exatamente %d itens: os %d da v1.11 + os %d de %s, seção 1' % (len(vol), len(vol0), len(ctx.vol_t11), cfg.T11_VOLATEIS))
    par = sum(1 for i in P['itens'] if i['aderencia'] == 'parcial')
    ok_(res, 'C-A', par == cfg.TOTAIS['parcial'] and sum(1 for i in P0['itens'] if i['aderencia'] == 'parcial') == 88, 'C-A: `aderencia` "parcial" em %d itens (88 da v1.11 + 6)' % par)
    # C-S
    sims = P['simulados']
    em_sim = {x for s in sims for x in s['itens']}
    volp = set(vol)
    ok_(res, 'C-S', not (em_sim & novos_ids) and all(not ({'L4-11', 'BQ-0010'} <= set(s['itens'])) for s in sims) and all(not (set(s['itens']) & volp) for s in sims if s['tipo'] == 'final')
        and not any('QA PENDENTE' in dumps(i) for i in P['itens']),
        'C-S: nenhum dos 189 em simulado; L4-11 e o item 81 do TRF6 (BQ-0010) não estão no mesmo simulado; nenhum VOLÁTIL em simulado final; nenhum item com "QA PENDENTE"')
    # C-5
    try:
        Q = reverte_base(P, ctx)
        ok_(res, 'C-5', json.dumps(Q, ensure_ascii=False, indent=1).encode('utf-8') + b'\n' == ctx.raw0,
            'C-5: reversão: desfeitos os registros T115 do `interno` (ordem inversa), retirados os 189 itens, as 73 pegadinhas e `topicos`, obtém-se a v1.11 byte a byte (%s…)' % cfg.BASE[2][:8])
    except Falha as e:
        ok_(res, 'C-5', False, 'C-5: %s' % e)
    # forma do interno (A3)
    forma, n_rec, n_obj = True, 0, 0
    for lista in ('itens', 'lotes', 'simulados', 'discursivas'):
        for o in P[lista]:
            if 'interno' in o:
                n_obj += 1
                forma &= list(o)[-1] == 'interno' and isinstance(o['interno'], list) and len(o['interno']) > 0
                for r in o['interno']:
                    n_rec += 1
                    forma &= list(r) == ['edicao', 'campo', 'pos', 'antes', 'depois', 'regra', 'ocorrencias'] and isinstance(r['pos'], int) and isinstance(r['ocorrencias'], list)
    n_rec0 = sum(len(o.get('interno', [])) for lista in ('itens', 'lotes', 'simulados', 'discursivas') for o in P0[lista])
    ok_(res, 'A3', forma and n_rec == n_rec0 + cfg.TOTAIS['delecoes'] + 10 + 1 + 6, '`interno`: último campo do objeto, nunca vazio, registros {edicao, campo, pos, antes, depois, regra, ocorrencias}; %d registros em %d objetos (v1.11 %d + 53 + 10 + 1 + 6)' % (n_rec, n_obj, n_rec0))
    return res


def reverte_base(P, ctx):
    import build_v112 as B
    return B.reverte_para_base(P, [e['texto'] for e in ctx.entradas], [i['id'] for i in ctx.itens], ctx.P0)


# ---------------------------------------------------------------- núcleo (código próprio)
def nucleo_esperado(P, ctx):
    banco = {r['id']: r for r in ctx.banco}
    linhas = {}
    for k, l in enumerate(ctx.dec.split('\n'), 1):
        m = re.match(r'^APLICADA [^|]*\| (D-[A-Z0-9-]+) \|', l)
        if m and m.group(1) not in linhas:
            linhas[m.group(1)] = k
    chaves = {}
    for pos, it in enumerate(P['itens']):
        iid = it['id']
        if iid in ctx.meta:
            k1, k2 = '2026-10-18', linhas[ctx.meta[iid]['ato']]
        elif iid.startswith('BQ-'):
            k1, k2 = banco[iid]['data_verificacao'], 0
        else:
            a = NU.ato_de(iid)
            k1, k2 = ('2026-10-18' if '-R' in iid else '2026-10-09'), linhas[a]
        chaves[iid] = (it['itemEdital'], (k1, k2, 0 if it['aderencia'] == 'direta' else 1, pos))
    por = collections.defaultdict(list)
    for iid, (f_, ch) in chaves.items():
        por[f_].append((ch, iid))
    nuc = {}
    for f_, lst in por.items():
        lst.sort()
        for k, (ch, iid) in enumerate(lst):
            nuc[iid] = k < 10
    return nuc


# ---------------------------------------------------------------- conferências sobre o pacote_estudante.json (E)
def checa_estudante(E, P, ctx):
    res = []
    ok_(res, 'A4', not any('interno' in x for l_ in ('itens', 'lotes', 'simulados', 'discursivas') for x in E[l_]), '`interno` ausente do pacote_estudante.json')
    ok_(res, 'C-9b', all(list(i)[-1] == 'nucleo' and isinstance(i['nucleo'], bool) for i in E['itens']), '"nucleo" booleano e último campo de todo item do -E')
    ok_(res, 'C-9c', [l_['id'] for l_ in E['lotes']] == ['L1', 'L2', 'L3', 'L4', 'L5', 'L6A', 'L6B'], 'fusão 1-C/4-C/5-C: lotes L1, L2, L3, L4, L5, L6A, L6B')
    ok_(res, 'C-9d', all(i['url'] == '' for i in E['itens'] if i['rotulo'] == 'AUTORAL') and sum(1 for i in E['itens'] if i['rotulo'] == 'AUTORAL') == sum(1 for i in P['itens'] if i['rotulo'] == 'AUTORAL'), 'url vazia nos AUTORAL do -E (todos)')
    _ep = {i['id']: i for i in E['itens']}
    dif = []
    for i in P['itens']:
        for c in ('justificativa', 'nota', 'enunciado', 'comando', 'textoBase'):
            if c in i and _ep[i['id']].get(c) != i[c]:
                dif.append('%s.%s' % (i['id'], c))
    lp = {l_['id']: l_ for l_ in P['lotes']}
    for l_ in E['lotes']:
        if l_['id'] == 'L1':
            continue
        for c in ('resumo', 'curso', 'nome'):
            if l_[c] != lp[l_['id']][c]:
                dif.append('%s.%s' % (l_['id'], c))
        if l_['pares'] != lp[l_['id']]['pares'] or l_['pegadinhas'] != lp[l_['id']]['pegadinhas']:
            dif.append('%s.pares/pegadinhas' % l_['id'])
    L1e, L1p, L1c = [x for x in E['lotes'] if x['id'] == 'L1'][0], lp['L1'], lp['L1C']
    if L1e['pegadinhas'] != L1p['pegadinhas'] + L1c['pegadinhas'] or L1e['nome'] != L1p['nome']:
        dif.append('L1.pegadinhas/nome')
    dp = {d['id']: d for d in P['discursivas']}
    for d in E['discursivas']:
        x = dp[d['id']]
        if (d['comando'], d['padrao'], d['aspectos'], d['quesitos']) != (x['comando'], x['padrao'], x['aspectos'], x['quesitos']):
            dif.append(d['id'])
    sp = {x['id']: x for x in P['simulados']}
    dif += [x['id'] for x in E['simulados'] if x.get('avisos') != sp[x['id']].get('avisos') or x['nome'] != sp[x['id']]['nome']]
    ok_(res, 'C-9f', not dif, 'cada campo de texto exibido do -E é igual ao do pacote.json sem `interno` (fora a fusão 1-C/4-C/5-C no L1 e a url vazia): %s' % (dif[:5] or '0 diferença'))
    ok_(res, 'C-E1', list(E) == ['versao', 'geradoEm', 'nome', 'edital', 'itens', 'simulados', 'lotes', 'discursivas', 'topicos'] and dumps(E['topicos']) == dumps(P['topicos']) and E['nome'] == cfg.NOME_E
        and [i['id'] for i in E['itens']] == [i['id'] for i in P['itens']] and not any('legendaMecanismo' in l_ for l_ in E['lotes']),
        'C-E1: pacote_estudante.json: estrutura do pacote.json sem `interno` e com `nucleo`; `topicos` idêntico; sem legendaMecanismo; url "" nos AUTORAL; textos exibidos iguais')
    # C-NU
    nuc = nucleo_esperado(P, ctx)
    got = {i['id']: i['nucleo'] for i in E['itens']}
    iguais = got == nuc
    por = collections.defaultdict(list)
    for i in E['itens']:
        por[i['itemEdital']].append(i)
    f_ok = all(sum(1 for i in v if i['nucleo']) == min(10, len(v)) for v in por.values())
    n40 = {i['id'] for i in ctx.E0['itens'] if i['nucleo']}
    # nas folhas 3.2 a 3.4, 4.2 e 4.3 entram os 4 primeiros diretos da onda 4; na 3.1, os 7 da v1.11 e L3-R15, R16, R17
    o4 = [i for i in ctx.itens if ctx.meta[i['id']]['grupo'] == 'ONDA4']
    alvo_ok = True
    for f_ in ('P2-3.2', 'P2-3.3', 'P2-3.4', 'P2-4.2', 'P2-4.3'):
        prim = [i['id'] for i in o4 if i['itemEdital'] == f_ and i['aderencia'] == 'direta'][:4]
        alvo_ok &= {i['id'] for i in por[f_] if i['nucleo']} == {i['id'] for i in ctx.P0['itens'] if i['itemEdital'] == f_} | set(prim)
    alvo_ok &= {i['id'] for i in por['P2-3.1'] if i['nucleo']} == {i['id'] for i in ctx.P0['itens'] if i['itemEdital'] == 'P2-3.1'} | {'L3-R15', 'L3-R16', 'L3-R17'}
    mudou = {i['itemEdital'] for i in ctx.E0['itens'] for j in [got[i['id']]] if j != i['nucleo']}
    ok_(res, 'C-NU', iguais and f_ok and alvo_ok and mudou <= {'P2-3.1', 'P2-3.2', 'P2-3.3', 'P2-3.4', 'P2-4.2', 'P2-4.3'},
        'C-NU: `nucleo` = 10 primeiros por (k1, k2, k3, k4) em cada folha (recálculo próprio; atos D-T98-ONDA4-ACEITE -> D-V112-BAEF-P1-ACEITE -> D-V112-BAEF-P2-ACEITE depois dos atos da v1.11); folha com ≤10 toda true; 3.2 a 3.4, 4.2 e 4.3 com os 4 primeiros diretos da onda 4; 3.1 com os 7 da v1.11 e L3-R15, R16, R17; só essas folhas mudam (%s)' % sorted(mudou))
    return res


# ---------------------------------------------------------------- C-14 (contrato) e C-16 (literais de versão)
def checa_contrato(texto_lf, ctx_base_bytes=None):
    import difflib
    res = []
    c0 = refs.git_show(cfg.CONTRATO_BASE[0], cfg.CONTRATO_BASE[1]).replace(b'\r\n', b'\n').decode('utf-8').split('\n')
    c1 = texto_lf.split('\n')
    ops = [(t, i1, i2, j1, j2) for t, i1, i2, j1, j2 in difflib.SequenceMatcher(None, c0, c1, autojunk=False).get_opcodes() if t != 'equal']
    esp = [('replace', 0, 1, 0, 1), ('replace', 2, 3, 2, 3), ('insert', 206, 206, 206, 218)]
    ok_(res, 'C-14', ops == esp and cfg.CONTRATO_VERSAO in c1[0] and hashlib.sha256(texto_lf.encode('utf-8')).hexdigest() == cfg.CONTRATO_SHA_LF,
        'C-14: diff de regras/pacote_contrato.md (LF) contra o blob de %s só com os opcodes replace 0–1, replace 2–3, insert 206 → 206–218, "%s" na linha 1 e SHA-256 LF = o da D1: %s' % (cfg.CONTRATO_BASE[0], cfg.CONTRATO_VERSAO, ops))
    return res


CODIGOS_MD = ['RF-ASR', 'RF-DEGRAVACAO', 'RF-IA-PARLAMENTAR', 'RF-PROTECAO', 'TID-IA', 'TID-DADOS-VIZ', 'TI-FERRAMENTAS', 'TI-REDES-SEGURANCA', '(v0.2)']
LEGENDA_MD_RX = re.compile(r'^(Mecanismo: troca de conceito \(TC\)|Mecanismos: TC troca de conceito)', re.M)


def checa_md(F1, E):
    """C-MD1 e C-MD2 sobre {nome: texto} dos 35 .md e o pacote_estudante.json E (dict). Devolve [(id, ok, msg)]."""
    res = []
    antigos = [a for a, d in cfg.NOMES_LOTE.values()] + [cfg.SIM0_NOME[0]]
    maus = []
    for n, t in sorted(F1.items()):
        for a in antigos + CODIGOS_MD:
            if a in t:
                maus.append('%s: %s' % (n, a[:40]))
    nome = {l_['id']: l_['nome'] for l_ in E['lotes']}
    l1 = []
    for lid in ('L1', 'L2', 'L3', 'L4', 'L5', 'L6A', 'L6B'):
        a = '%s_estudo.md' % lid
        if a not in F1 or F1[a].split('\n', 1)[0] != '# ' + nome[lid]:
            l1.append(a)
    res.append(('C-MD1', not maus and not l1 and len(F1) == 35, 'C-MD1: nos %d .md, 0 ocorrência dos nomes antigos de lote, dos códigos de produção e de "(v0.2)"%s; linha 1 dos 7 _estudo.md = "# " + nome do lote no -E%s' % (
        len(F1), (' (achados: %s)' % maus[:3]) if maus else '', (' (divergem: %s)' % l1) if l1 else '')))
    leg = [n for n, t in sorted(F1.items()) if LEGENDA_MD_RX.search(t)]
    res.append(('C-MD2', not leg, 'C-MD2: 0 linha começando por "Mecanismo: troca de conceito (TC)" ou "Mecanismos: TC troca de conceito" nos .md%s' % ((' (há em %s)' % leg) if leg else '')))
    return res
