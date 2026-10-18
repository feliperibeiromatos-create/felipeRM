# -*- coding: utf-8 -*-
"""T-108 e T-109 (gerador_v1_11, seção 4 da D1) — passo 7: conferências C-1, C-2, C-3, C-5, C-6, C-7, C-8, C-11, C-12, C-14, C-15 e C-17 (C-4, C-9, C-10, C-13 e C-16 estão em validate_v111.py;
o bloco M, em fidelidade_mutacao_v111.py). Estados: OK, FALHA e PENDENTE (condição de entrada da geração final ainda não cumprida: SHA da tabela não fixado, contrato v1.2.8 não gravado,
código da plataforma não disponível). Só FALHA dá código de saída 1. Saídas: out/conferencias_<TAG>.json e, pelo runner, out/conferencias_stdout.txt."""
import collections, copy, difflib, hashlib, json, os, subprocess, sys, csv
from common import OUT, HERE, REPO, P as PATH
import refs, config_v111 as cfg
import tabelas_v111 as T
import limpeza_v111 as L
import inventario_v111 as I
import build_v111 as B
import estudante_md_v111 as MD

R = []


def reg(i, estado, m):
    R.append((i, estado, m))


def ok(i, c, m):
    reg(i, 'OK' if c else 'FALHA', m)


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def carrega(nome):
    return json.load(open(os.path.join(OUT, nome), encoding='utf-8'), object_pairs_hook=collections.OrderedDict)


def main():
    st = carrega('stats_%s.json' % cfg.TAG)
    P = carrega('pacote.json')
    praw = open(os.path.join(OUT, 'pacote.json'), 'rb').read()
    base_raw = refs.git_show(cfg.BASE[0], cfg.BASE[1])
    P0 = json.loads(base_raw.decode('utf-8'), object_pairs_hook=collections.OrderedDict)
    tabs = [(g, c, T.le_bytes(c), h) for g, c, h in cfg.TABELAS]
    ocorr_raw = T.le_bytes(cfg.OCORRENCIAS[0]); t109_raw = T.le_bytes(cfg.T109[0])

    # C-1 SHA-256
    ok('C-1a', hashlib.sha256(base_raw).hexdigest() == cfg.BASE[2] and hashlib.sha256(refs.git_show(cfg.BASE_E[0], cfg.BASE_E[1])).hexdigest() == cfg.BASE_E[2], 'BASE (git %s): pacote.json e pacote_estudante.json = SHA-256 do config' % cfg.BASE[0])
    ok('C-1b', hashlib.sha256(ocorr_raw).hexdigest() == cfg.OCORRENCIAS[1] and hashlib.sha256(t109_raw).hexdigest() == cfg.T109[1], 'inventário de ocorrências e T109 = SHA-256 do config')
    sem = [g for g, c, raw, h in tabs if not h]
    ruim = [c for g, c, raw, h in tabs if h and hashlib.sha256(raw).hexdigest() != h]
    if ruim:
        reg('C-1c', 'FALHA', 'tabela(s) com SHA-256 diferente do fixado: %s' % ruim)
    elif sem:
        reg('C-1c', 'PENDENTE', 'SHA-256 das tabelas %s não fixado (gatilho A da Gerência pendente; ENSAIO lê as tabelas de ensaio: %s)' % (sem, [c for g, c, raw, h in tabs]))
    else:
        reg('C-1c', 'OK', 'SHA-256 das tabelas = os do config')
    ok('C-1d', all(st['tabelas'][k]['sha256'] == hashlib.sha256(tabs[k][2]).hexdigest() for k in range(len(tabs))) and st['ocorrencias']['sha256'] == hashlib.sha256(ocorr_raw).hexdigest()
       and st['t109']['sha256'] == hashlib.sha256(t109_raw).hexdigest(), 'SHA-256 gravados em out/stats_%s.json = os dos arquivos lidos agora' % cfg.TAG)

    # C-2 cobertura
    inv_l = I.varre(P0, 'D'); inv = {o['id_ocorrencia']: o for o in inv_l}
    oc = T.le_ocorrencias(ocorr_raw)
    rows = T.carrega_de_bytes(tabs)
    try:
        cob = T.valida_cobertura(rows, oc, inv, completa=True)
        ok('C-2', cob['universo'] == cfg.UNIVERSO and cob['faltam'] == 0 and cob['fp'] == cfg.FP_R1 + cfg.FP_CONTEUDO,
           'cobertura: %d ids do universo, cada um em exatamente uma linha (GCE %d, GCB %d, GBQ %d); nenhum dos %d FP em linha' % (cob['universo'], cob['por_gerencia']['GCE'], cob['por_gerencia']['GCB'], cob['por_gerencia']['GBQ'], cob['fp']))
    except T.Falha as e:
        reg('C-2', 'FALHA', str(e))

    # C-3 e C-7: refaz a limpeza e compara com out/pacote.json; C-5: reversibilidade
    try:
        Pn, res = L.aplica(P0, rows, inv, cfg.EXCECOES_DEPOIS)
        Pn['nome'] = cfg.NOME; Pn['geradoEm'] = cfg.GERADO_EM
        if cfg.E_L2R16:
            [i for i in Pn['itens'] if i['id'] == 'L2-R16'][0]['itemEdital'] = 'P2-3.1'
        ok('C-3', (json.dumps(Pn, ensure_ascii=False, indent=1) + '\n').encode('utf-8') == praw, 'antes único, casamentos dentro do intervalo, sem sobreposição e FP intactos (%d edições, %d MANTER); a limpeza refeita é igual ao out/pacote.json byte a byte' % (res['aplicadas'], res['mantidas']))
        ok('C-7', True, 'proibições do depois, "verificado em" e base legal: 0 violação em %d edições (exceções do depois registradas: %d)' % (res['aplicadas'], len(cfg.EXCECOES_DEPOIS)))
        Q = L.reverte(P)
        if cfg.E_L2R16:
            [i for i in Q['itens'] if i['id'] == 'L2-R16'][0]['itemEdital'] = 'P2-2.8'
        Q['nome'], Q['geradoEm'] = P0['nome'], P0['geradoEm']
        ok('C-5', (json.dumps(Q, ensure_ascii=False, indent=1) + '\n').encode('utf-8') == base_raw, 'reversibilidade: o `interno` aplicado em ordem decrescente de pos devolve o pacote.json v1.10 byte a byte')
    except T.Falha as e:
        reg('C-3', 'FALHA', str(e)); reg('C-7', 'FALHA', str(e)); reg('C-5', 'FALHA', str(e))

    # C-6 inventário
    Pj, oj, _ = I.varre_pacote(os.path.join(OUT, 'pacote.json'), 'D')
    Ej, oe, _ = I.varre_pacote(os.path.join(OUT, 'pacote_estudante.json'), 'E')
    ids_item = [i['id'] for i in Pj['itens']]
    om = []
    for nome in sorted(os.listdir(os.path.join(OUT, 'estudante'))):
        if nome.endswith('.md') and nome != 'README.md':
            om += I.varre_md(nome, open(os.path.join(OUT, 'estudante', nome), encoding='utf-8').read(), ids_item)
    cj, ce, cm = I.contagem(oj), I.contagem(oe), I.contagem(om)
    manter = [r for r in rows if r['acao'] == 'MANTER']
    nv = []
    for o in oj:
        if o['classe'] == 'VERIFICAR' and not any(r['caminho'] == o['caminho'] and o['casamento'] in r['antes'] for r in manter):
            nv.append((o['caminho'], o['casamento']))
    fp_old = collections.Counter((o['caminho'], o['classe'], o['casamento']) for o in oc.values() if o['classe'] in ('FP-R1', 'FP-CONTEUDO'))
    fp_new = collections.Counter((o['caminho'], o['classe'], o['casamento']) for o in oj if o['classe'] in ('FP-R1', 'FP-CONTEUDO'))
    ids_old = {i for i, o in oc.items() if o['classe'] in ('FP-R1', 'FP-CONTEUDO')}
    ids_new = {o['id_ocorrencia'] for o in oj if o['classe'] in ('FP-R1', 'FP-CONTEUDO')}
    ok('C-6b', cj.get('FP-R1', 0) == cfg.FP_R1 and cj.get('FP-CONTEUDO', 0) == cfg.FP_CONTEUDO and fp_old == fp_new,
       'pacote.json: FP-R1 %d (esperado %d), FP-CONTEUDO %d (esperado %d), os mesmos %d FP por (campo, classe, casamento); ids de ocorrência diferentes: %d (o índice k do hash muda quando uma ocorrência anterior do mesmo literal sai do campo)' % (
           cj.get('FP-R1', 0), cfg.FP_R1, cj.get('FP-CONTEUDO', 0), cfg.FP_CONTEUDO, sum(fp_old.values()), len(ids_old ^ ids_new) // 2))
    ok('C-6c', ce.get('PROCESSO', 0) == 0, 'pacote_estudante.json: PROCESSO %d (meta 0); VERIFICAR %d; FP-R1 %d; FP-CONTEUDO %d' % (ce.get('PROCESSO', 0), ce.get('VERIFICAR', 0), ce.get('FP-R1', 0), ce.get('FP-CONTEUDO', 0)))
    F0md = MD.pasta_blob(cfg.BASE[0], cfg.BASE_ESTUDANTE_DIR)
    om0 = []
    for nome in sorted(F0md):
        if nome.endswith('.md') and nome != 'README.md':
            om0 += I.varre_md(nome, F0md[nome], ids_item)
    pm0 = collections.Counter((o['arquivo'], o['categoria'], o['subtipo'], o['casamento']) for o in om0 if o['classe'] == 'PROCESSO')
    pm1 = collections.Counter((o['arquivo'], o['categoria'], o['subtipo'], o['casamento']) for o in om if o['classe'] == 'PROCESSO')
    novos_md = pm1 - pm0
    ok('C-6d', cm.get('PROCESSO', 0) == 0 or not novos_md and cj.get('PROCESSO', 0) == 0 and ce.get('PROCESSO', 0) == 0,
       'edição .md (34 arquivos, fora README.md; ids de item exatos desconsiderados): PROCESSO %d (v1.10: %d), nenhum novo; os que restam são cabeçalho, metadado, legenda de mecanismo (TC/IC/GI/AT) e texto de enunciado, fora dos campos do inventário JSON, que tem 0 PROCESSO no pacote.json e no -E (por categoria: %s); VERIFICAR %d; FP-R1 %d; FP-CONTEUDO %d' % (
           cm.get('PROCESSO', 0), sum(pm0.values()), dict(collections.Counter(k[1] + ' ' + k[2] for k in pm1.elements())), cm.get('VERIFICAR', 0), cm.get('FP-R1', 0), cm.get('FP-CONTEUDO', 0)))

    # C-8 residual
    er = carrega('estudante_json.json')['verificacao_residual']
    if er['liquido'] == 0:
        reg('C-8', 'OK', 'listas de deleção herdadas com 0 casamento no pacote.json limpo')
    elif cfg.FINAL:
        reg('C-8', 'FALHA', '%d casamento(s) residual(is): %s' % (er['liquido'], dict(er['regras_herdadas'])))
    else:
        reg('C-8', 'PENDENTE', 'ENSAIO: %d casamento(s) residual(is) das listas de deleção herdadas no pacote.json limpo (%s); a geração final exige 0 ou lista fechada declarada na reconciliação' % (er['liquido'], dict(er['regras_herdadas'])))

    # C-11 edição .md
    F0 = MD.pasta_blob(cfg.BASE[0], cfg.BASE_ESTUDANTE_DIR)
    dmd = os.path.join(OUT, 'estudante')
    F1 = {n: open(os.path.join(dmd, n), encoding='utf-8', newline='').read() for n in sorted(os.listdir(dmd))}
    mdj = carrega('estudante_md_%s.json' % cfg.TAG)
    mudou = sorted(n for n in F1 if F1[n] != F0.get(n))
    esperado_mudar = set(t['arquivo'] for t in mdj['trocas']) | {'NUCLEO.md', 'README.md'}
    ok('C-11a', len(F1) == 35 and set(F1) == set(F0) | {'NUCLEO.md'} | set(F0) and set(mudou) <= esperado_mudar, '%d arquivos; mudam %d: só os dos campos alterados, NUCLEO.md, L2_gabarito.md e README.md' % (len(F1), len(mudou)))
    E_old = json.loads(refs.git_show(cfg.BASE_E[0], cfg.BASE_E[1]).decode('utf-8'), object_pairs_hook=collections.OrderedDict)
    E_new = carrega('pacote_estudante.json')
    mud = [m for m in MD.muda(E_old, E_new) if m[0] not in ('nome', 'geradoEm', 'itens[L2-R16].itemEdital')]
    por_campo = {m[0]: m for m in mud}
    rev = dict(F1)
    for t in mdj['trocas']:
        if t['campo'] == 'itens[L2-R16].itemEdital':
            g = rev['L2_gabarito.md']; ini = g.find('### L2-R16 — Gabarito'); fim = g.find('\n### ', ini + 5); fim = len(g) if fim < 0 else fim
            rev['L2_gabarito.md'] = g[:ini] + g[ini:fim].replace('Item do edital: P2-3.1', 'Item do edital: P2-2.8') + g[fim:]
        else:
            _, old, new = por_campo[t['campo']]
            rev[t['arquivo']] = rev[t['arquivo']].replace(new, old)
    difs = [n for n in F0 if n not in ('README.md', 'NUCLEO.md') and rev[n] != F0[n]]
    ok('C-11b', not difs, 'a troca de volta (valor novo -> antigo; L2-R16 P2-3.1 -> P2-2.8) devolve a v1.10 byte a byte, salvo NUCLEO.md e README.md%s' % (' (diferem: %s)' % difs[:3] if difs else ''))

    # C-12 registro por id
    rows_csv = list(csv.DictReader(open(os.path.join(OUT, 'registro_alteracoes_%s.csv' % cfg.TAG), encoding='utf-8', newline='')))
    n_int = sum(len(o.get('interno', [])) for l in ('itens', 'lotes', 'simulados', 'discursivas') for o in P[l])
    intern = {(r['edicao'], r['antes'], r['depois']) for l in ('itens', 'lotes', 'simulados', 'discursivas') for o in P[l] for r in o.get('interno', [])}
    csvset = {(r['id_edicao'], r['antes'], r['depois']) for r in rows_csv if r['id_edicao'] != 'T109-0001'}
    ok('C-12', len(rows_csv) == n_int + (1 if cfg.E_L2R16 else 0) and csvset == intern, 'registro por id: %d linhas = %d edições aplicadas + %d (L2-R16); conjunto (edicao, antes, depois) igual ao do `interno`' % (len(rows_csv), n_int, 1 if cfg.E_L2R16 else 0))

    # C-14 contrato
    if not cfg.FINAL:
        reg('C-14', 'PENDENTE', 'só na geração final: diff de regras/pacote_contrato.md contra a v1.2.7 do commit %s, restrito ao cabeçalho e à seção da v1.2.8 (ENSAIO não grava o contrato)' % cfg.BASE[0])
    else:
        c7 = refs.git_show(cfg.BASE[0], 'regras/pacote_contrato.md').replace(b'\r\n', b'\n').decode('utf-8').split('\n')
        c8 = open(PATH('regras/pacote_contrato.md'), 'rb').read().replace(b'\r\n', b'\n').decode('utf-8').split('\n')
        sm = difflib.SequenceMatcher(None, c7, c8, autojunk=False)
        ancora = next((k for k, l in enumerate(c8) if l.startswith('Errata de forma da v1.2.8')), None)
        ops = [(t, i1, i2, j1, j2) for t, i1, i2, j1, j2 in sm.get_opcodes() if t != 'equal']
        bom = ancora is not None and all((j2 <= 3) or (j1 >= ancora - 1) for t, i1, i2, j1, j2 in ops)
        ok('C-14', bom and c8[0].find('v1.2.8') >= 0, 'diff contra a v1.2.7 restrito às linhas 1 a 3 (cabeçalho) e à seção da v1.2.8: %s' % ops)

    # C-15 exportação de erros
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
        reg('C-17', 'OK' if ignora else 'PENDENTE', 'informativa, sem efeito no aceite (leitura somente do código %s, o mais novo em saida/plataforma; pode não ser o publicado): validar(j) exige só itens[] e simulados[] como listas e, em cada item, id, enunciado e gabarito C/E; não enumera chaves e a palavra "interno" não ocorre no código; chave desconhecida é aceita e nada a exibe. Confirmar na plataforma publicada fica com o Fundador (D-V15-PLATAFORMA).' % cod[-1] if ignora else
            'informativa: a leitura de %s não permitiu concluir (revisar validar(j))' % cod[-1])

    # extras: lista de arquivos do gerador frente ao v1_10 e pastas/promovidos intactos
    g10 = os.path.join(HERE, '..', 'gerador_v1_10')
    a10 = {f for f in os.listdir(g10) if os.path.isfile(os.path.join(g10, f))}
    a11 = {f for f in os.listdir(HERE) if os.path.isfile(os.path.join(HERE, f))}
    NOVOS = {'config_v111.py', 'tabelas_v111.py', 'limpeza_v111.py', 'build_v111.py', 'estudante_json_v111.py', 'registro_adendo_v111.py', 'estudante_md_v111.py', 'registro_alteracoes_v111.py',
             'validate_v111.py', 'conferencias_v111.py', 'inventario_v111.py', 'fidelidade_mutacao_v111.py', 'manifesto_%s.py' % cfg.TAG, 'marcas_x_v111.py'}
    alt = {f for f in a10 & a11 if f != 'MANIFESTO.md' and sha(os.path.join(g10, f)) != sha(os.path.join(HERE, f))}
    ok('C-G1', (a11 - a10) - {'MANIFESTO.md'} == NOVOS and alt == {'_run.py', 'rodar_tudo.sh', 'validar_erros_teste.py'} and not (a10 - a11 - {'MANIFESTO.md'}),
       'arquivos do gerador frente ao v1_10: novos %s; alterados %s; removidos %s' % (sorted((a11 - a10) - {'MANIFESTO.md'} - NOVOS), sorted(alt), sorted(a10 - a11 - {'MANIFESTO.md'})))
    st_git = subprocess.run(['git', '-C', REPO, 'status', '--porcelain', '--untracked-files=all', '--', 'saida/pacote/gerador_v1_10', 'saida/pacote/pacote.json', 'saida/pacote/pacote_estudante.json',
                             'saida/estudante', 'saida/gbq', 'saida/simulados', 'regras'], capture_output=True, text=True).stdout.strip()
    ok('C-G2', st_git == '' or cfg.FINAL, 'gerador_v1_10, pacote.json, pacote_estudante.json, saida/estudante, saida/gbq, saida/simulados, regras  no disco (%r)' % st_git[:160])

    falhas = [r for r in R if r[1] == 'FALHA']
    for i, e, m in R:
        print('%-7s %-8s %s' % (i, e, m))
    print('conferencias_%s: %d OK, %d PENDENTE, %d FALHA (modo %s)' % (cfg.TAG, sum(1 for r in R if r[1] == 'OK'), sum(1 for r in R if r[1] == 'PENDENTE'), len(falhas), 'FINAL' if cfg.FINAL else 'ENSAIO'))
    with open(os.path.join(OUT, 'conferencias_%s.json' % cfg.TAG), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(dict(total=len(R), ok=sum(1 for r in R if r[1] == 'OK'), pendentes=sum(1 for r in R if r[1] == 'PENDENTE'), falhas=len(falhas), conferencias=[dict(id=i, estado=e, msg=m) for i, e, m in R]), f, ensure_ascii=False, indent=1); f.write('\n')
    sys.exit(1 if falhas else 0)


if __name__ == '__main__':
    main()
