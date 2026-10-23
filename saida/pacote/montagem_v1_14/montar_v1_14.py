# montar_v1_14.py — T-123 fase 2 — 2026-10-23 — gerado por gbq-csc
# -*- coding: utf-8 -*-
"""Monta o pacote v1.14 = v1.13 canônica (82c4117c…/04cbd593…) + 238 itens de reforço de DA + 36 itens de banco P1-DA (D1 da GBQ, saida/pacote/T123_D1_v1_14_2026-10-23.md, seções 1 a 6 e 13).
Insumos (lidos como bytes com CRLF->LF; SHA-256 sobre os bytes LF; divergência -> exit 2): base v1.13 (pacote e estudante), out/reforco_bruto.json (extrator da fase 1), DA_reforco_substituicoes.csv
(limpeza da GCB, aceita), banco/banco.csv, DECISOES.md (linhas dos atos do `nucleo`). Saídas: out/pacote.json e out/pacote_estudante.json (json.dumps(ensure_ascii=False, indent=1)+LF, UTF-8, 0 CR).
Também é módulo de apoio de conferir_t123.py e mutacao_t123.py (funções `ler_insumos`, `carregar`, `aplica_substituicoes`, `construir`). Uso: python -I montar_v1_14.py. Não lê relógio."""
import sys
sys.dont_write_bytecode = True
import collections, copy, csv, hashlib, io, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import nucleo_v114 as NU
from nucleo_v114 import Aborta

R = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
OUT = os.path.join(HERE, 'out')
GERADO_EM = '2026-10-23'
NOME_P = 'Câmara 2026 — pacote F4 (v1.14)'
NOME_E = 'Câmara 2026 — pacote do estudante (v1.14-E)'
TOP = ['versao', 'geradoEm', 'nome', 'edital', 'itens', 'simulados', 'lotes', 'discursivas', 'topicos']

PATH = collections.OrderedDict([
    ('base_pacote', 'saida/pacote/montagem_v1_13/out/pacote.json'),
    ('base_estudante', 'saida/pacote/montagem_v1_13/out/pacote_estudante.json'),
    ('banco', 'banco/banco.csv'),
    ('csv', 'saida/gcb/DA_plataforma/DA_reforco_substituicoes.csv'),
    ('registro', 'saida/gcb/DA_plataforma/DA_reforco_registro_formato.md'),
    ('formato', 'saida/gcb/DA_plataforma/FORMATO_PLATAFORMA_DA.md'),
    ('bruto', 'saida/pacote/montagem_v1_14/out/reforco_bruto.json'),
    ('dec', 'DECISOES.md'),
] + [('leva%d' % n, 'saida/gcb/DA_reforco_leva%d_v2.md' % n) for n in range(1, 9)])
SHA_FIXO = collections.OrderedDict([
    ('base_pacote', '82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240'),
    ('base_estudante', '04cbd593fdd30404ecb7f91f6b6722da6b2fc24e58d3c0eb68b10a4e792a0c40'),
    ('banco', 'b1c1588f8b4a80a233e7b8d485992d07e9adeb2570fb2343573ab7fde9a5721f'),
    ('csv', 'df9f53bd7dc3f18631c77528b32683dd89e77e27dea167918fd1edee014db501'),
    ('registro', 'a511fd8d3b79b806dc3a87f06d294ed346d05f2d05766089b80103d6374b820e'),
    ('formato', 'f3fd4667af5b1c0ad8d8ef9e21259074599a3f09b7c3610f36923de029d75068'),
    ('bruto', '87264c2f3f1dc5447127bba6757b5b31432e85beb0a743fac4e304589adee497'),
])
BANCO_FORA = ('BQ-0141', 'BQ-0151')           # D-BQ0141-REVERIFICAR (QA PENDENTE) e D-BQ0151-DIVERGE (4)
FLIPS_ESP = ['D1-07', 'D1-08', 'D3-79', 'D3-80', 'D6-07', 'D6-08', 'D6-09', 'D6-10', 'D6-37', 'D6-38', 'D6-39', 'D6-40']
NUC18 = ['D4-R01', 'D4-R02', 'D4-R03', 'D4-R04', 'D3-R02', 'D3-R03', 'D3-R05', 'D4-R15', 'D4-R16', 'D4-R17', 'D1-R01', 'D1-R02', 'D3-R14', 'D3-R15', 'D3-R26', 'D3-R27', 'D3-R38', 'D3-R49']
ERRATAS = [  # (id, ato, campo, antes, depois) — seção 2.2 da D1; já aplicadas por extrair_reforco_da.py em out/reforco_bruto.json
    ('D3-R13', 'AJ-E1 (D-T116-LEVA2-ACEITE, II)', 'enunciado', 'são obrigados a fornecer serviços adequados, eficientes, seguros e, quanto aos essenciais, contínuos os órgãos públicos, por si ou suas empresas, concessionárias, permissionárias ou sob qualquer outra forma de empreendimento.',
     'os órgãos públicos, por si ou suas empresas, concessionárias, permissionárias ou sob qualquer outra forma de empreendimento, são obrigados a fornecer serviços adequados, eficientes, seguros e, quanto aos essenciais, contínuos.'),
    ('D3-R18', 'AJ-L2-E1 (D-T116-LEVA3-ACEITE, II)', 'enunciado', 'tenha causado dano ao erário e falecido.', 'tenha causado dano ao erário e, posteriormente, tenha falecido.'),
    ('D3-R75', 'AJ-L7-E1 (D-D3R75-AJL7E1-ACEITE)', 'justificativa', '; a tentação é lembrar de outro limite de desconto fora desta lei (o valor “terço” não ocorre na Lei 4.619).',
     '; o valor “terço” não ocorre na Lei 4.619, cujo único limite de desconto é o do art. 6º.'),
]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def abort(msg):
    raise Aborta(msg)


def dumps(obj):
    return (json.dumps(obj, ensure_ascii=False, indent=1) + '\n').encode('utf-8')


def grava(caminho, dados):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, 'wb') as f:
        f.write(dados)


def ler_insumos(raiz=R):
    """{nome: bytes LF}. Lê como bytes e troca CRLF por LF antes de qualquer decode."""
    out = collections.OrderedDict()
    for nome, rel in PATH.items():
        out[nome] = open(os.path.join(raiz, rel), 'rb').read().replace(b'\r\n', b'\n')
    return out


def shas_levas(dec_texto):
    """SHA-256 completos das 8 levas nas linhas de aceite de DECISOES.md (aborta se não forem únicos)."""
    out = {}
    for n in range(1, 9):
        nome = 'DA_reforco_leva%d_v2.md' % n
        m = re.findall(re.escape(nome) + r' \(SHA-256 ([0-9a-f]{64})', dec_texto)
        if not m or len(set(m)) != 1:
            abort('SHA-256 de %s nao achado de forma unica em DECISOES.md: %r' % (nome, m))
        out[n] = m[0]
    return out


def verifica_sha(ins):
    """[(nome, esperado, obtido, ok)] para os insumos de SHA fixo e para as 8 levas (SHA das linhas de aceite)."""
    res = []
    for nome, esp in SHA_FIXO.items():
        ob = sha(ins[nome])
        res.append((nome, esp, ob, esp == ob))
    sl = shas_levas(ins['dec'].decode('utf-8'))
    for n in range(1, 9):
        ob = sha(ins['leva%d' % n])
        res.append(('leva%d' % n, sl[n], ob, sl[n] == ob))
    return res


def le_csv(b, delim=';'):
    rd = csv.reader(io.StringIO(b.decode('utf-8'), newline=''), delimiter=delim)
    cab = next(rd)
    return cab, [dict(zip(cab, row)) for row in rd]


def banco_rows(b):
    rd = csv.reader(io.StringIO(b.decode('utf-8'), newline=''), delimiter=';')
    cab = next(rd); out = []; ant = rd.line_num
    for row in rd:
        d = dict(zip(cab, row)); d['_linha'] = ant + 1; ant = rd.line_num
        out.append(d)
    return out


def carregar(ins):
    """ctx a partir dos bytes dos insumos (já verificados)."""
    cab, subs = le_csv(ins['csv'])
    if cab != ['id', 'campo', 'antes', 'depois', 'operacao', 'motivo']:
        abort('cabecalho do CSV da GCB: %r' % cab)
    return dict(base_pac=json.loads(ins['base_pacote'].decode('utf-8')), base_est=json.loads(ins['base_estudante'].decode('utf-8')),
                bruto=json.loads(ins['bruto'].decode('utf-8')), subs=subs, banco=banco_rows(ins['banco']), dec=ins['dec'].decode('utf-8'))


def aplica_substituicoes(bruto, subs):
    """aplica as substituições da GCB na justificativa (cada `antes` exatamente 1 vez no texto corrente; senão Aborta). Devolve ({id: justificativa}, log)."""
    just = {b['id']: b['justificativa'] for b in bruto}
    log = []
    for s in subs:
        iid = s['id']
        if iid not in just:
            abort('substituicao da GCB para id fora do reforco: %s' % iid)
        if s['campo'] != 'justificativa':
            abort('substituicao da GCB com campo %r (so justificativa): %s' % (s['campo'], iid))
        n = just[iid].count(s['antes'])
        if s['antes'] == '' or n != 1:
            abort('substituicao da GCB: o antes %r ocorre %d vez(es) na justificativa de %s (esperado 1)' % (s['antes'], n, iid))
        just[iid] = just[iid].replace(s['antes'], s['depois'])
        log.append(dict(id=iid, antes=s['antes'], depois=s['depois'], operacao=s['operacao'], motivo=s['motivo'], ocorrencias=n))
    return just, log


def item_reforco(b, just):
    return collections.OrderedDict([
        ('id', b['id']), ('rotulo', 'AUTORAL'), ('certame', 'Projeto Câmara 2026'), ('cargo', 'Noções de Direito Administrativo e Administração Pública'),
        ('ano', 2026), ('numero', int(b['id'].split('-R')[1])), ('comando', 'Julgue o item a seguir.'), ('textoBase', ''),
        ('enunciado', b['enunciado']), ('gabarito', b['gabarito']), ('justificativa', just), ('itemEdital', b['itemEdital']),
        ('aderencia', b['aderencia']), ('url', 'saida/gcb/DA_reforco_leva%d_v2.md' % b['leva'])])


def item_banco(d):
    return collections.OrderedDict([
        ('id', d['id']), ('rotulo', d['rotulo']), ('certame', d['certame']), ('cargo', d['cargo']), ('ano', int(d['ano_aplicacao'])), ('numero', int(d['numero_item'])),
        ('comando', d['texto_comando']), ('textoBase', d['texto_base']), ('enunciado', d['texto_integral']), ('gabarito', d['gabarito']), ('justificativa', ''),
        ('itemEdital', d['item_edital_camara']), ('aderencia', d['aderencia']), ('url', d['url_caderno'])])


def seleciona_banco(rows):
    return sorted((d for d in rows if d['item_edital_camara'].startswith('P1-DA') and d['anulado'] == 'nao' and d['id'] not in BANCO_FORA), key=lambda d: d['id'])


def construir(ctx):
    """(pacote, estudante, info). Aborta (Aborta) em qualquer divergência de insumo."""
    bp, be = ctx['base_pac'], ctx['base_est']
    just, log = aplica_substituicoes(ctx['bruto'], ctx['subs'])
    bq_new = [item_banco(d) for d in seleciona_banco(ctx['banco'])]
    ref = [item_reforco(b, just[b['id']]) for b in ctx['bruto']]
    base_bq = [i for i in bp['itens'] if i['id'].startswith('BQ-')]
    base_resto = [i for i in bp['itens'] if not i['id'].startswith('BQ-')]
    if [i['id'] for i in bp['itens'][:len(base_bq)]] != [i['id'] for i in base_bq]:
        abort('o bloco de banco da v1.13 nao e contiguo no inicio de itens')
    itens = [copy.deepcopy(i) for i in base_bq] + bq_new + [copy.deepcopy(i) for i in base_resto] + ref
    pac = collections.OrderedDict((k, copy.deepcopy(bp[k])) for k in TOP)
    pac['itens'] = itens; pac['geradoEm'] = GERADO_EM; pac['nome'] = NOME_P
    # --- estudante
    eb = {i['id']: i for i in be['itens']}
    if [i['id'] for i in be['itens']] != [i['id'] for i in bp['itens']]:
        abort('ids/ordem de itens da v1.13 diferem entre pacote e estudante')
    leva_de = {b['id']: b['leva'] for b in ctx['bruto']}
    datas = {d['id']: d['data_verificacao'] for d in ctx['banco']}
    est_itens = []
    for it in itens:
        if it['id'] in eb:
            e = copy.deepcopy(eb[it['id']])
        else:
            e = copy.deepcopy(it)
            if e['rotulo'] == 'AUTORAL':
                e['url'] = ''
            e['nucleo'] = False
        est_itens.append(e)
    nuc, K = NU.calcula(est_itens, datas, leva_de, ctx['dec'])
    for e in est_itens:
        if e['itemEdital'].startswith('P1-DA-'):
            e['nucleo'] = nuc[e['id']]
    est = collections.OrderedDict((k, copy.deepcopy(be[k])) for k in TOP)
    est['itens'] = est_itens; est['geradoEm'] = GERADO_EM; est['nome'] = NOME_E
    flips = [i['id'] for i in be['itens'] if i['nucleo'] and not next(e for e in est_itens if e['id'] == i['id'])['nucleo']]
    info = dict(subs_log=log, flips=flips, chaves=K, n_banco_novo=len(bq_new), ids_banco_novo=[i['id'] for i in bq_new])
    return pac, est, info


def main():
    ins = ler_insumos()
    falhas = []

    def chk(c, m):
        print(('OK    ' if c else 'FALHA ') + m)
        if not c:
            falhas.append(m)
    try:
        res = verifica_sha(ins)
        for nome, esp, ob, ok in res:
            if not ok:
                sys.stderr.write('ABORTA: SHA-256 LF de %s: esperado %s, obtido %s\n' % (PATH[nome], esp, ob)); sys.exit(2)
            chk(ok, 'SHA-256 LF %s = %s…%s' % (PATH[nome], ob[:8], ob[-4:]))
        ctx = carregar(ins)
        pac, est, info = construir(ctx)
    except Aborta as e:
        sys.stderr.write('ABORTA: %s\n' % e); sys.exit(2)
    bp, be = ctx['base_pac'], ctx['base_est']
    chk(ins['base_pacote'] == dumps(bp) and ins['base_estudante'] == dumps(be), 'a base v1.13 e json.dumps(ensure_ascii=False, indent=1)+LF (ida e volta)')
    for nome, p, base in (('pacote', pac, bp), ('pacote_estudante', est, be)):
        its = p['itens']; ids = [i['id'] for i in its]; bids = {i['id'] for i in base['itens']}
        chk(len(its) == 1433 and len(set(ids)) == 1433, '%s: 1.433 itens, ids unicos' % nome)
        chk([i for i in its if i['id'] in bids] == base['itens'] or nome == 'pacote_estudante', '%s: itens da v1.13 identicos e na mesma ordem' % nome)
        chk(all(p[k] == base[k] for k in ('versao', 'edital', 'simulados', 'lotes', 'discursivas', 'topicos')), '%s: versao, edital, simulados, lotes, discursivas e topicos iguais aos da v1.13' % nome)
        chk(list(p) == TOP and list(p)[-1] == 'topicos', '%s: chaves de topo na ordem da v1.13' % nome)
        chk(p['geradoEm'] > '2026-10-20', '%s: geradoEm %s > 2026-10-20' % (nome, p['geradoEm']))
        chk((sum(i['gabarito'] == 'C' for i in its), sum(i['gabarito'] == 'E' for i in its)) == (730, 703), '%s: C/E 730/703' % nome)
        da = [i for i in its if i['itemEdital'].startswith('P1-DA-')]
        chk(len(da) == 684 and (sum(i['gabarito'] == 'C' for i in da), sum(i['gabarito'] == 'E' for i in da)) == (350, 334), '%s: DA 684 itens, C/E 350/334' % nome)
        chk([i['id'] for i in its[:142]] == sorted(i for i in ids if i.startswith('BQ-'))[:142] and all(i['id'].startswith('BQ-') for i in its[:142]) and not any(i['id'].startswith('BQ-') for i in its[142:]), '%s: 142 itens de banco no bloco inicial, em ordem de id' % nome)
    eds = {e['id'] for e in pac['edital']}
    chk(all(i['itemEdital'] in eds for i in pac['itens']), 'todo itemEdital existe no edital')
    chk(info['n_banco_novo'] == 36, '36 itens de banco P1-DA')
    chk(len(info['subs_log']) == 91, '91 substituicoes da GCB aplicadas, cada antes 1 vez')
    neu = {i['id']: i['nucleo'] for i in est['itens']}
    chk(sum(neu.values()) == 775, 'nucleo true no pacote: %d (esperado 775)' % sum(neu.values()))
    da_e = [i for i in est['itens'] if i['itemEdital'].startswith('P1-DA-')]
    chk((sum(i['nucleo'] for i in da_e), sum(not i['nucleo'] for i in da_e)) == (408, 276), 'nucleo DA true/false %d/%d (esperado 408/276)' % (sum(i['nucleo'] for i in da_e), sum(not i['nucleo'] for i in da_e)))
    chk(all(neu[i] for i in info['ids_banco_novo']), 'nucleo true nos 36 de banco')
    chk(info['flips'] == FLIPS_ESP, 'itens da v1.13 que passam a false: %s' % info['flips'])
    RX_R = re.compile(r'D[1-6]-R\d\d')
    ref_true = [i['id'] for i in est['itens'] if RX_R.fullmatch(i['id']) and i['nucleo']]
    chk(sorted(ref_true) == sorted(NUC18), 'nucleo true do reforco (%d): %s' % (len(ref_true), ref_true))
    chk(all(i['url'] == '' for i in est['itens'] if RX_R.fullmatch(i['id'])) and all(list(i)[-1] == 'nucleo' for i in est['itens']), 'estudante: url "" no reforco; nucleo ultimo campo')
    chk(all('nucleo' not in i for i in pac['itens']), 'pacote.json sem nucleo')
    for nome, p in (('pacote', pac), ('pacote_estudante', est)):
        b = dumps(p)
        chk(b'\r' not in b, '%s.json: 0 CR' % nome)
        grava(os.path.join(OUT, nome + '.json'), b)
        print('%s.json' % nome, len(b), 'bytes; SHA-256', sha(b))
    print('RESULTADO: %d FALHA' % len(falhas))
    sys.exit(1 if falhas else 0)


if __name__ == '__main__':
    main()
