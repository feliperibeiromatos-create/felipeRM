# -*- coding: utf-8 -*-
"""T-115 (gerador_v1_12, D1 da GBQ, seção 4) — passo 7: conferências C-1, C-3, C-6, C-8, C-11, C-12, C-14, C-15, C-17, C-D, C-RG, C-G1 e C-G2 (as demais estão em validate_v112.py, que usa checks_v112.py;
o bloco M, em fidelidade_mutacao_v112.py). Estados: OK, FALHA e PENDENTE (condição de entrada da geração final ainda não cumprida: DECISOES.md sem o ato, contrato fora da v1.2.9, código da plataforma
não disponível). Só FALHA dá código de saída 1; FINAL exige 0 FALHA e 0 PENDENTE. Saídas: out/conferencias_<TAG>.json, out/similaridade_<TAG>.csv e, pelo runner, out/conferencias_stdout.txt."""
import collections, csv, difflib, hashlib, io, json, os, re, subprocess, sys
from common import OUT, HERE, REPO, P as PATH
import refs, config_v112 as cfg
import fontes_v112 as F
from fontes_v112 import Falha
import checks_v112 as C
import build_v112 as B
import estudante_md_v112 as MD
import inventario_v112 as I

R = []


def reg(i, estado, m):
    R.append((i, estado, m))


def ok(i, c, m):
    reg(i, 'OK' if c else 'FALHA', m)


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def carrega(nome):
    return json.load(open(os.path.join(OUT, nome), encoding='utf-8'), object_pairs_hook=collections.OrderedDict)


def palavras(t):
    return re.findall(r'\w+', t.lower())


def shingles(t, k=7):
    w = palavras(t)
    return {tuple(w[i:i + k]) for i in range(max(0, len(w) - k + 1))}


def main():
    ctx = C.Ctx()
    st = carrega('stats_%s.json' % cfg.TAG)
    P = carrega('pacote.json')
    praw = open(os.path.join(OUT, 'pacote.json'), 'rb').read()
    E = carrega('pacote_estudante.json')

    # C-1 SHA-256
    ok('C-1a', hashlib.sha256(ctx.raw0).hexdigest() == cfg.BASE[2] and hashlib.sha256(refs.git_show(cfg.BASE_E[0], cfg.BASE_E[1])).hexdigest() == cfg.BASE_E[2],
       'BASE (git %s): pacote.json e pacote_estudante.json = SHA-256 do config (1b5657c7… e 8533b0c0…)' % cfg.BASE[0])
    try:
        ins = F.confere_todos()
        ok('C-1b', len(ins) == 23 and all(h == cfg.SHA[a] for n, a, h, b in ins), 'os 23 insumos lidos com CRLF → LF: SHA-256 LF de cada um = o da tabela da seção 1 (%d conferidos)' % len(ins))
    except Falha as e:
        ok('C-1b', False, str(e))
    ok('C-1d', [x['sha256_lf'] for x in st['insumos']] == [h for n, a, h, at in cfg.INSUMOS] and st['base']['sha256'] == cfg.BASE[2], 'SHA-256 gravados em out/stats_%s.json = os da tabela de config_v112' % cfg.TAG)
    # decisões e contrato
    falta = [d for d in cfg.DECISOES_EXIGIDAS if ('| %s |' % d) not in ctx.dec]
    if falta:
        reg('C-1e', 'FALHA' if cfg.FINAL else 'PENDENTE', 'DECISOES.md sem a linha "| id |" de %s' % falta)
    else:
        ok('C-1e', True, 'DECISOES.md traz os três atos de aceite (%s)' % ', '.join(cfg.DECISOES_EXIGIDAS))
    # C-3: o gerador refeito reproduz o out/pacote.json
    P0, _ = B.le_base()
    Pn, info = B.gera(P0)
    ok('C-3', (json.dumps(Pn, ensure_ascii=False, indent=1) + '\n').encode('utf-8') == praw, 'o pacote.json regerado das fontes pelo build é igual ao out/pacote.json byte a byte')

    # C-6 inventário
    Pj, oj, _ = I.varre_pacote(os.path.join(OUT, 'pacote.json'), 'D')
    Ej, oe, _ = I.varre_pacote(os.path.join(OUT, 'pacote_estudante.json'), 'E')
    ids_item = [i['id'] for i in Pj['itens']]
    om = []
    for nome in sorted(os.listdir(os.path.join(OUT, 'estudante'))):
        if nome.endswith('.md') and nome != 'README.md':
            om += I.varre_md(nome, open(os.path.join(OUT, 'estudante', nome), encoding='utf-8').read(), ids_item)
    cj, ce, cm = I.contagem(oj), I.contagem(oe), I.contagem(om)
    proc_j = collections.Counter((o['caminho'], o['categoria'], o['casamento']) for o in oj if o['classe'] == 'PROCESSO')
    permitidos = set(cfg.MANTER) | {(c, k, m) for (c, k, m) in cfg.ENUNCIADOS_FP}
    ok('C-6b', set(proc_j) <= permitidos and sum(proc_j.values()) == 3 and cj.get('FP-R1', 0) == 28 + 8 and cj.get('FP-CONTEUDO', 0) == 115,
       'pacote.json: PROCESSO %d, todos na lista MANTER da seção 3.5 (%s); VERIFICAR %d (1 MANTER da v1.11 + 1 em `topicos`); FP-R1 %d (28 da v1.11 + 8 nos textos novos); FP-CONTEUDO %d (115, sem mudança)' % (
           sum(proc_j.values()), sorted(c for c, k, m in proc_j), cj.get('VERIFICAR', 0), cj.get('FP-R1', 0), cj.get('FP-CONTEUDO', 0)))
    proc_e = collections.Counter((o['caminho'], o['categoria'], o['casamento']) for o in oe if o['classe'] == 'PROCESSO')
    ok('C-6c', proc_e == proc_j and {k: v for k, v in ce.items() if k != 'PROCESSO'} == {k: v for k, v in cj.items() if k != 'PROCESSO'} and sum(proc_e.values()) == 3,
       'pacote_estudante.json: as mesmas ocorrências do pacote.json (PROCESSO %d, VERIFICAR %d, FP-R1 %d, FP-CONTEUDO %d)' % (ce.get('PROCESSO', 0), ce.get('VERIFICAR', 0), ce.get('FP-R1', 0), ce.get('FP-CONTEUDO', 0)))
    F0md = MD.pasta_blob(cfg.BASE[0], cfg.BASE_ESTUDANTE_DIR)
    om0 = []
    for nome in sorted(F0md):
        if nome.endswith('.md') and nome != 'README.md':
            om0 += I.varre_md(nome, F0md[nome], ids_item)
    pm0 = collections.Counter((o['arquivo'], o['categoria'], o['subtipo'], o['casamento']) for o in om0 if o['classe'] == 'PROCESSO')
    pm1 = collections.Counter((o['arquivo'], o['categoria'], o['subtipo'], o['casamento']) for o in om if o['classe'] == 'PROCESSO')
    novos_md = pm1 - pm0
    # os novos PROCESSO do .md vêm só dos casamentos de conteúdo registrados na D1 (F1 = medida F1; v2 = API v2; lote = transcrição em lote) e das tecla F4 etc.
    perm_cas = {'F1', 'v2', 'lote', 'F4'}
    ok('C-6d', all(k[3] in perm_cas for k in novos_md) and cm.get('PROCESSO', 0) <= sum(pm0.values()) + sum(novos_md.values()),
       'edição .md (34 arquivos, fora README.md; ids de item exatos desconsiderados): PROCESSO %d (v1.11: %d); os novos (%d) são só homônimos de conteúdo dos MANTER/enunciados da D1 (%s); VERIFICAR %d; FP-R1 %d; FP-CONTEUDO %d' % (
           cm.get('PROCESSO', 0), sum(pm0.values()), sum(novos_md.values()), sorted(collections.Counter((k[0], k[3]) for k in novos_md.elements()).items())[:6], cm.get('VERIFICAR', 0), cm.get('FP-R1', 0), cm.get('FP-CONTEUDO', 0)))

    # C-8 residual
    er = carrega('estudante_json.json')['verificacao_residual']
    if er['liquido'] == 0 and er['regras_herdadas'] == cfg.EXCECOES_RESIDUAL and er['total'] == 9:
        reg('C-8', 'OK', 'listas de deleção herdadas: 9 casamentos no pacote.json limpo, todos na lista fechada EXCECOES_RESIDUAL %s; líquido 0' % dict(cfg.EXCECOES_RESIDUAL))
    else:
        reg('C-8', 'FALHA', '%d casamento(s) residual(is): %s' % (er['liquido'], dict(er['regras_herdadas'])))

    # C-11 edição .md
    dmd = os.path.join(OUT, 'estudante')
    F1 = {n: open(os.path.join(dmd, n), encoding='utf-8', newline='').read() for n in sorted(os.listdir(dmd))}
    mdj = carrega('estudante_md_%s.json' % cfg.TAG)
    mudou = sorted(n for n in F1 if F1[n] != F0md.get(n))
    esp_mud = sorted({'%s_%s.md' % (l_, s) for l_ in ('L1', 'L2', 'L3', 'L4', 'L5', 'L6A', 'L6B') for s in ('estudo', 'itens', 'gabarito')} | {'SIM-0_folha.md', 'SIM-0_gabarito.md', 'SIM-1_gabarito.md', 'NUCLEO.md', 'README.md'})
    ok('C-11a', len(F1) == 35 and set(F1) == set(F0md) and mudou == esp_mud and mudou == mdj['arquivos_alterados'],
       '%d arquivos; mudam %d: os 21 de lote (nome do lote), SIM-0_folha e SIM-0_gabarito (nome), SIM-1_gabarito (legendas), NUCLEO.md e README.md; os outros 9 são byte a byte os da v1.11' % (len(F1), len(mudou)))
    # reversão independente
    rev = dict(F1)
    LEG_REPOR = {'L4_gabarito.md': (2, 4), 'L5_gabarito.md': (2, 4), 'L6A_gabarito.md': (2, 4), 'L6B_gabarito.md': (2, 4)}
    nomes = {lid: cfg.NOMES_LOTE[lid] for lid in ('L1', 'L2', 'L3', 'L4', 'L5', 'L6A', 'L6B')}
    textos_novos = {e['texto'] for e in ctx.entradas}
    difs = []
    for lid, (antes, depois) in nomes.items():
        for s in ('estudo', 'itens', 'gabarito'):
            a = '%s_%s.md' % (lid, s)
            t = rev[a]
            if s == 'estudo':
                i = t.find('\n\n## Tópico ')
                t = t[:i] + '\n' if i >= 0 else t
                lin = t.split('\n')
                t = '\n'.join(l for l in lin if not (l.startswith('- [') and any(l.endswith('— ' + x) for x in textos_novos)))
            else:
                if lid in ('L1', 'L2', 'L3', 'L4'):
                    novos_lote = [i for i in E['itens'][cfg.BASE_ITENS:] if MD.gen.lote_fund(i['id']) == lid]
                    Ib, Gb = MD.bloco_itens(novos_lote)
                    extra = '\n'.join(Ib if s == 'itens' else Gb).rstrip('\n')
                    k = t.rfind(extra)
                    t0 = F0md[a].replace(antes, depois)
                    if lid == 'L4':
                        sufixo = '\n\n## Itens de reforço\n\n' + extra + '\n'
                    else:
                        sufixo = '\n\n' + extra + '\n'
                    if not t.endswith(sufixo):
                        difs.append(a + ' (sufixo dos itens novos)'); continue
                    t = t[:len(t) - len(sufixo)] + '\n'
            if s == 'gabarito' and a in LEG_REPOR:     # legendas retiradas pelo passo (6): repostas da v1.11 (linhas a:b do blob)
                lin = t.split('\n'); i0, i1 = LEG_REPOR[a]
                t = '\n'.join(lin[:i0] + F0md[a].split('\n')[i0:i1] + lin[i0:])
            rev[a] = t.replace(depois, antes, 1)
    for a in ('SIM-0_folha.md', 'SIM-0_gabarito.md'):
        rev[a] = rev[a].replace(cfg.SIM0_NOME[1] + ' —', cfg.SIM0_NOME[0] + ' —', 1)
    lin = rev['SIM-1_gabarito.md'].split(chr(10))
    rev['SIM-1_gabarito.md'] = chr(10).join(lin[:5] + F0md['SIM-1_gabarito.md'].split(chr(10))[5:9] + lin[5:])
    for n in F0md:
        if n in ('README.md', 'NUCLEO.md'):
            continue
        if rev[n] != F0md[n]:
            difs.append(n)
    ok('C-11b', not difs, 'a troca de volta (nome novo → antigo; retirados os tópicos, as pegadinhas novas e os itens novos) devolve a v1.11 byte a byte, salvo NUCLEO.md e README.md%s' % (' (diferem: %s)' % difs[:3] if difs else ''))
    for rid, rok, rmsg in C.checa_md(F1, E):
        ok(rid, rok, rmsg)
    cr = sorted(f for r_, ds, fs in os.walk(HERE) for f in fs if b'\r' in open(os.path.join(r_, f), 'rb').read() and 'out' not in os.path.relpath(r_, HERE).split(os.sep)[:1] and '__pycache__' not in r_)
    ok('C-LF', not cr, 'C-LF: 0 arquivo com o byte CR em gerador_v1_12/ fora de out/ e __pycache__/%s' % ((' (com CR: %s)' % cr[:3]) if cr else ''))
    # os blocos novos do .md vêm do -E
    resumos_ok = all(all(p in F1['%s_estudo.md' % MD.lote_do_topico(k, E['lotes'])] for p in t['resumo'].split('\n\n')) for k, t in E['topicos'].items())
    n_h = sum(F1['%s_estudo.md' % l_].count('\n### Resumo do tópico\n') for l_ in ('L1', 'L2', 'L3', 'L4', 'L5', 'L6A', 'L6B'))
    n_m = sum(F1['%s_estudo.md' % l_].count('\n### Em 1 minuto\n') for l_ in ('L1', 'L2', 'L3', 'L4', 'L5', 'L6A', 'L6B'))
    ok('C-11c', resumos_ok and n_h == 40 and n_m == 3, '.md: 40 "Resumo do tópico" (parágrafos do -E) e 3 "Em 1 minuto" nos _estudo.md; cada item novo tem o enunciado e a justificativa do -E nos _itens.md e _gabarito.md')
    itens_ok = True
    for i in E['itens'][cfg.BASE_ITENS:]:
        lid = MD.gen.lote_fund(i['id'])
        if ('**%s** — %s' % (i['id'], i['enunciado'])) not in F1['%s_itens.md' % lid] or ('- Justificativa: %s' % i['justificativa']) not in F1['%s_gabarito.md' % lid]:
            itens_ok = False
    ok('C-11d', itens_ok, 'os 189 itens novos aparecem com enunciado (_itens.md) e justificativa (_gabarito.md) do -E')
    ok('C-11e', F1['NUCLEO.md'] == MD.nucleo_md(E) and ('- Versão: v%s ' % cfg.VERSAO) in F1['README.md'] and ('- Data: %s' % cfg.GERADO_EM) in F1['README.md'], 'NUCLEO.md = o recalculado do campo `nucleo` do -E; README.md com a versão e a data de config_v112')

    # C-12 registro por id
    rows_csv = list(csv.DictReader(open(os.path.join(OUT, 'registro_alteracoes_%s.csv' % cfg.TAG), encoding='utf-8', newline='')))
    intern = {(r['edicao'], r['antes'], r['depois']) for l_ in ('itens', 'lotes', 'simulados', 'discursivas') for o in P[l_] for r in o.get('interno', []) if r['edicao'].startswith('T115-')}
    csvset = {(r['id_edicao'], r['antes'], r['depois']) for r in rows_csv if r['id_edicao'].split('-')[1] in ('L', 'N', 'S', 'LM')}
    cont = collections.Counter('-'.join(r['id_edicao'].split('-')[:2]) for r in rows_csv)
    esp = {'T115-I': 189, 'T115-L': 53, 'T115-E': 3, 'T115-U': 2, 'T115-P': 139, 'T115-T': 43, 'T115-N': 10, 'T115-S': 1, 'T115-LM': 6, 'T115-R': 1}
    ids_c = [r['id_edicao'] for r in rows_csv]
    objs = {i['id'] for i in P['itens']} | {L_['id'] for L_ in P['lotes']} | {s['id'] for s in P['simulados']} | set(P['topicos']) | {'registro_alteracoes_v1_11.csv'}
    ok('C-12', len(rows_csv) == cfg.TOTAIS['registro'] and dict(cont) == esp and len(set(ids_c)) == len(ids_c) and csvset == intern and all(r['objeto'] in objs for r in rows_csv),
       'registro por id: %d linhas = 447 (%s); id único em cada linha; objetos existentes; conjunto (edicao, antes, depois) dos registros T115 do `interno` (%d) = o das linhas L, N, S e LM' % (len(rows_csv), dict(cont), len(intern)))
    cp = collections.Counter(r['acao'] for r in rows_csv if r['id_edicao'].startswith('T115-P-'))
    ok('C-RG', cp['ADICIONAR'] == 70 and cp['DESCARTAR'] == 69 and sum(1 for r in rows_csv if r['id_edicao'].startswith('T115-P-') and r['acao'] == 'ADICIONAR' for _ in r['caminho'].split(';')) == 73,
       'C-RG: T115-P: %d CONVERTIDO (73 pegadinhas, com o caminho `lotes[Lx].pegadinhas[k]` de cada uma) e %d DESCARTADO (com motivo); a contagem por prefixo é a da seção 5' % (cp['ADICIONAR'], cp['DESCARTAR']))
    # as pegadinhas do rastro estão onde dizem
    cam_ok = True
    for r in rows_csv:
        if r['id_edicao'].startswith('T115-P-') and r['acao'] == 'ADICIONAR':
            for c_, tx in zip(r['caminho'].split(';'), r['depois'].split(' || ')):
                m = re.fullmatch(r'lotes\[(\w+)\]\.pegadinhas\[(\d+)\]', c_)
                cam_ok &= bool(m) and [L_ for L_ in P['lotes'] if L_['id'] == m.group(1)][0]['pegadinhas'][int(m.group(2))]['texto'] == tx
    ok('C-RGb', cam_ok, 'cada caminho `lotes[Lx].pegadinhas[k]` do rastro aponta para a pegadinha de mesmo texto no pacote.json')

    # C-14 contrato
    ct = open(PATH('regras/pacote_contrato.md'), 'rb').read().replace(b'\r\n', b'\n').decode('utf-8')
    for i, o, m in C.checa_contrato(ct):
        if o:
            ok(i, True, m)
        else:
            reg(i, 'FALHA' if cfg.FINAL else 'PENDENTE', m)
    # C-15
    r = subprocess.run([sys.executable, '-I', '-B', os.path.join(HERE, '_run.py'), 'validar_erros_teste.py'], capture_output=True, text=True, encoding='utf-8')
    with open(os.path.join(OUT, 'validar_erros_stdout.txt'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(r.stdout)
    ok('C-15', r.returncode == 0, 'validar_erros_teste.py com o pacote novo (ids inalterados): código %d; %s' % (r.returncode, r.stdout.strip().split('\n')[-1] if r.stdout.strip() else r.stderr[-200:]))
    # C-17 informativa
    cod = [f for f in sorted(os.listdir(PATH('saida/plataforma'))) if f.startswith('plataforma_v') and f.endswith('.html')]
    if not cod:
        reg('C-17', 'PENDENTE', 'informativa: código da plataforma não encontrado em saida/plataforma')
    else:
        html = open(PATH('saida/plataforma/' + cod[-1]), encoding='utf-8').read()
        i0 = html.find('function validar(j)'); i1 = html.find('function usarPacote', i0)
        corpo = html[i0:i1]
        ignora = i0 >= 0 and i1 > i0 and 'Object.keys' not in corpo and 'for(const' not in corpo and ' in j' not in corpo and 'interno' not in html
        reg('C-17', 'OK' if ignora else 'PENDENTE', ('informativa, sem efeito no aceite (leitura somente do código %s, o mais novo em saida/plataforma; pode não ser o publicado): validar(j) não enumera chaves e a palavra "interno" não ocorre no código; chave de topo desconhecida (`topicos`) é aceita. Confirmar na plataforma publicada fica com o Fundador (D-V15-PLATAFORMA).' % cod[-1]) if ignora else
            'informativa: a leitura de %s não permitiu concluir (revisar validar(j))' % cod[-1])

    # C-D: gêmeos
    banco_ids = {r['id'] for r in ctx.banco}
    novos = P['itens'][cfg.BASE_ITENS:]
    ok('C-D1', not ({i['id'] for i in novos} & (banco_ids | ctx.ids0)), 'C-D: nenhum id novo no banco/banco.csv nem no pacote v1.11')
    alvo = []
    for i in P['itens']:
        alvo.append((i['id'], 'pacote', shingles((i['textoBase'] + ' ' + i['enunciado']).strip())))
    ja = {x[0] for x in alvo}
    for r in ctx.banco:
        if r['id'] not in ja:
            alvo.append((r['id'], 'banco', shingles(r['texto_integral'])))
    pares = []
    maxj = 0.0
    ids_novos = {i['id'] for i in novos}
    for a_id, a_t, a_s in alvo:
        if a_id not in ids_novos or not a_s:
            continue
        for b_id, b_t, b_s in alvo:
            if b_id == a_id or not b_s:
                continue
            if b_id in ids_novos and b_id < a_id:
                continue
            j = len(a_s & b_s) / len(a_s | b_s)
            maxj = max(maxj, j)
            if j >= 0.30:
                pares.append((a_id, b_id, b_t, round(j, 3)))
    with open(os.path.join(OUT, 'similaridade_%s.csv' % cfg.TAG), 'w', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh, quoting=csv.QUOTE_ALL, lineterminator='\n')
        w.writerow(['id_novo', 'id_comparado', 'origem_comparado', 'jaccard_7_palavras'])
        for p in sorted(pares):
            w.writerow(p)
    reg('C-D', 'OK', 'C-D (informativa, não falha; insumo da fidelidade): Jaccard de 7 palavras ≥ 0,30 entre os 189 enunciados e os %d itens do pacote v1.11 + %d linhas do banco fora do pacote: %d par(es) em out/similaridade_%s.csv (maior Jaccard medido: %.3f)' % (
        cfg.BASE_ITENS, sum(1 for a in alvo if a[1] == 'banco'), len(pares), cfg.TAG, maxj))

    # C-G1 / C-G2
    g11 = os.path.join(HERE, '..', cfg.GERADOR_ANTERIOR)
    mani = open(os.path.join(g11, 'MANIFESTO.md'), encoding='utf-8').read()
    tabela = dict(re.findall(r'^\| `([^`]+)` \| `([0-9a-f]{64})` \|', mani.split('## Arquivos da pasta')[1].split('## ensaio/')[0], re.M))
    tabela_ens = dict(re.findall(r'^\| `ensaio/([^`]+)` \| `([0-9a-f]{64})` \|', mani.split('## ensaio/')[1].split('## out/')[0], re.M))
    maus = []
    arqs = sorted(f for f in os.listdir(g11) if os.path.isfile(os.path.join(g11, f)) and f != 'MANIFESTO.md')
    if set(arqs) != set(tabela):
        maus.append('lista de arquivos: %s' % sorted(set(arqs) ^ set(tabela))[:3])
    def lf(b):
        return b.replace(b'\r\n', b'\n')
    for f in arqs:
        disco = open(os.path.join(g11, f), 'rb').read()
        blob = subprocess.run(['git', '-C', REPO, 'show', '%s:saida/pacote/%s/%s' % (cfg.BASE[0], cfg.GERADOR_ANTERIOR, f)], capture_output=True).stdout
        h_ok = hashlib.sha256(disco).hexdigest() == tabela.get(f) or hashlib.sha256(lf(disco)).hexdigest() == tabela.get(f) or hashlib.sha256(lf(disco).replace(b'\n', b'\r\n')).hexdigest() == tabela.get(f)
        if not h_ok or lf(disco) != lf(blob):
            maus.append(f)
    ens = os.path.join(g11, 'ensaio')
    for f in sorted(os.listdir(ens)) if os.path.isdir(ens) else []:
        disco = open(os.path.join(ens, f), 'rb').read()
        blob = subprocess.run(['git', '-C', REPO, 'show', '%s:saida/pacote/%s/ensaio/%s' % (cfg.BASE[0], cfg.GERADOR_ANTERIOR, f)], capture_output=True).stdout
        if lf(disco) != lf(blob) or (f in tabela_ens and hashlib.sha256(disco).hexdigest() != tabela_ens[f] and hashlib.sha256(lf(disco)).hexdigest() != tabela_ens[f] and hashlib.sha256(lf(disco).replace(b'\n', b'\r\n')).hexdigest() != tabela_ens[f]):
            maus.append('ensaio/' + f)
    st_g = subprocess.run(['git', '-C', REPO, 'status', '--porcelain', '--untracked-files=all', '--', 'saida/pacote/' + cfg.GERADOR_ANTERIOR], capture_output=True, text=True).stdout.strip()
    mani_sha = hashlib.sha256(lf(open(os.path.join(g11, 'MANIFESTO.md'), 'rb').read())).hexdigest()
    mani_blob = hashlib.sha256(subprocess.run(['git', '-C', REPO, 'show', '%s:saida/pacote/%s/MANIFESTO.md' % (cfg.BASE[0], cfg.GERADOR_ANTERIOR)], capture_output=True).stdout).hexdigest()
    ok('C-G1', not maus and mani_sha.startswith(cfg.MANIFESTO_ANTERIOR_SHA) and mani_sha == mani_blob and not st_g,
       'gerador_v1_11 intacto: %d arquivos (fora out/) = a tabela "Arquivos da pasta" do MANIFESTO v1.11 e o blob de %s (comparação em LF; SHA em disco, LF ou CRLF); o MANIFESTO tem SHA-256 %s… (D1: %s…) = o do blob; divergentes: %s; git status da pasta: %r' % (len(arqs), cfg.BASE[0], mani_sha[:8], cfg.MANIFESTO_ANTERIOR_SHA, maus[:3] or 'nenhum', st_g[:60]))
    sg = subprocess.run(['git', '-C', REPO, 'status', '--porcelain', '--', 'regras/'], capture_output=True, text=True).stdout.strip()
    reg('C-G2', 'OK', 'git status de regras/ (impresso, não falha): %r' % sg)

    falhas = [r_ for r_ in R if r_[1] == 'FALHA']
    for i, e, m in R:
        print('%-7s %-8s %s' % (i, e, m))
    print('conferencias_%s: %d OK, %d PENDENTE, %d FALHA (modo %s)' % (cfg.TAG, sum(1 for r_ in R if r_[1] == 'OK'), sum(1 for r_ in R if r_[1] == 'PENDENTE'), len(falhas), 'FINAL' if cfg.FINAL else 'ENSAIO'))
    with open(os.path.join(OUT, 'conferencias_%s.json' % cfg.TAG), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(dict(total=len(R), ok=sum(1 for r_ in R if r_[1] == 'OK'), pendentes=sum(1 for r_ in R if r_[1] == 'PENDENTE'), falhas=len(falhas), conferencias=[dict(id=i, estado=e, msg=m) for i, e, m in R]), f, ensure_ascii=False, indent=1); f.write('\n')
    sys.exit(1 if falhas else 0)


if __name__ == '__main__':
    try:
        main()
    except Falha as e:
        print('FALHA:', e)
        sys.exit(1)
