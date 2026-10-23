# estudante_md_v114.py — T-123 fase 2 (script 8) — 2026-10-23 — gerado por gbq-csc
# -*- coding: utf-8 -*-
"""Edição do estudante v1.14-E em .md (out/estudante/, 53 arquivos), a partir de out/pacote_estudante.json (D1 da GBQ, seção 10). Base: os 53 arquivos da v1.13-E (saida/pacote/montagem_v1_13/out/estudante/),
conferidos contra saida/estudante/ (promovida) quando existir. Mudam 12 arquivos e só eles: README.md (v1.14-E, data, linha de DA com 684 itens, sendo 36 de provas anteriores), NUCLEO.md (775 ids núcleo),
BANCO_itens.md e BANCO_gabarito.md (os 36 itens novos depois do BQ-0112, na forma vigente) e DA_D1 a DA_D4 _itens.md e _gabarito.md (seção "## Itens de reforço" ao fim, na ordem do pacote). Os 41 outros ficam
byte a byte iguais (entre eles os 6 DA_D<n>_estudo.md e os 4 arquivos de D5 e D6). Grava out/estudante/ e out/estudante_md_v1_14.json (conferências, listagem e digest R2-D). exit 1 se alguma conferência FALHAR.
Uso: python -I estudante_md_v114.py. Não lê relógio."""
import sys
sys.dont_write_bytecode = True
import collections, difflib, hashlib, json, os, re, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import montar_v1_14 as M
import marcas_v114 as MV

R = M.R
OUT = M.OUT; OUTE = os.path.join(OUT, 'estudante')
BASE = os.path.join(R, 'saida', 'pacote', 'montagem_v1_13', 'out', 'estudante')
PROMOVIDA = os.path.join(R, 'saida', 'estudante')
VERSAO, DATA = '1.14-E', '2026-10-23'
AVISO = 'Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.'
LOTES = [1, 2, 3, 4, 5, 6]
MUDAM = ['README.md', 'NUCLEO.md', 'BANCO_itens.md', 'BANCO_gabarito.md'] + ['DA_D%d_%s.md' % (n, t) for n in (1, 2, 3, 4) for t in ('itens', 'gabarito')]
CHK = []


def chk(cid, desc, esperado, obtido, ok=None):
    ok = (esperado == obtido) if ok is None else ok
    CHK.append(dict(id=cid, criterio=desc, esperado=esperado, obtido=obtido, resultado='OK' if ok else 'FALHA'))
    print(('OK    ' if ok else 'FALHA ') + cid + ' — ' + desc + ('' if ok else '  [esperado=%r obtido=%r]' % (esperado, obtido)))
    return ok


def le(path):
    return open(path, 'rb').read().replace(b'\r\n', b'\n').decode('utf-8')


def banco_itens_bloco(it):
    L = ['### ' + it['id'], '', '- Certame: ' + it['certame'], '- Cargo: ' + it['cargo'], '- Ano: %d' % it['ano'], '- Número: %d' % it['numero'], '- URL oficial: ' + it['url'], '']
    if it['textoBase']:
        L += ['**Texto-base.** ' + it['textoBase'], '']
    L += ['**Comando.** ' + it['comando'], '', '**Enunciado.** ' + it['enunciado'], '']
    if it.get('volatil'):
        L += ['> ' + AVISO, '']
    if it.get('nota'):
        L += ['> ' + it['nota'].replace(' (D-LEI-15352)', ''), '']
    if it.get('volatil') or it.get('nota'):
        L += ['']
    return L


def banco_gab_bloco(it):
    L = ['### %s — Gabarito: %s' % (it['id'], it['gabarito']), '', '- Item do edital: %s (aderência: %s)' % (it['itemEdital'], it['aderencia'])]
    if it.get('nota'):
        L.append('- ' + it['nota'].replace(' (D-LEI-15352)', ''))
    L.append('')
    if it.get('volatil'):
        L += ['> ' + AVISO, '']
    return L


def banco_md(items):
    I = ['# Banco de itens Cebraspe — itens (sem gabarito)', '', 'Itens de provas anteriores (rótulo CEBRASPE_ANALOGA). Gabaritos no arquivo BANCO_gabarito.md.', '']
    G = ['# Banco de itens Cebraspe — gabarito', '']
    for it in items:
        I += banco_itens_bloco(it); G += banco_gab_bloco(it)
    return '\n'.join(I).rstrip('\n') + '\n', '\n'.join(G).rstrip('\n') + '\n'


def da_itens_gab_md(L, canon, reforco):
    """forma dos itens DA da v1.13-E (estudante_md_v113.itens_gab_md); os itens de reforço vêm depois, sob '## Itens de reforço', mantendo o agrupamento por (comando, textoBase)."""
    I = ['# %s — itens' % L['nome'], '', 'Itens para julgar (C = certo, E = errado). Gabarito e justificativas no arquivo DA_%s_gabarito.md.' % L['id'], '']
    G = ['# %s — gabarito e justificativas' % L['nome'], '']
    cur = None
    for secao, its in (('', canon), ('## Itens de reforço', reforco)):
        if secao and its:
            I += [secao, '']; G += [secao, '']
        for it in its:
            key = (it['comando'], it['textoBase'])
            if key != cur:
                if it['textoBase']:
                    I += ['**Texto-base.** %s' % it['textoBase'], '']
                I += ['**Comando.** %s' % it['comando'], '']
                cur = key
            I += ['**%s** — %s' % (it['id'], it['enunciado']), '']
            if it.get('volatil'):
                I += ['> %s' % AVISO, '']
            G += ['### %s — Gabarito: %s' % (it['id'], it['gabarito']), '', '- Item do edital: %s' % it['itemEdital']]
            if it['justificativa']:
                G.append('- Justificativa: %s' % it['justificativa'])
            G.append('')
            if it.get('volatil'):
                G += ['> %s' % AVISO, '']
    return '\n'.join(I).rstrip('\n') + '\n', '\n'.join(G).rstrip('\n') + '\n'


def nucleo_md(E, ordem):
    pf = collections.OrderedDict()
    for it in E['itens']:
        pf.setdefault(it['itemEdital'], []).append(it)
    N = ['# Câmara 2026 — Núcleo de estudo por item do edital', '',
         'Em cada item do edital, os itens marcados como núcleo são os 10 primeiros pela ordem em que foram incorporados ao material (itens de provas anteriores e itens de lotes de estudo; '
         'havendo empate, os de aderência direta antes dos de aderência parcial). Item do edital com 10 itens ou menos: todos são núcleo.', '']
    for f in sorted(pf, key=lambda s: ordem[s]):
        ids = [i['id'] for i in pf[f] if i['nucleo']]
        N.append('- %s (%d de %d): %s' % (f, len(ids), len(pf[f]), ', '.join(ids)))
    return '\n'.join(N) + '\n'


def mascara(linha):
    """máscara de ids de item só em títulos de item e listas de ids (seção 8.2 da D1)."""
    rx = re.compile(r'\bD[1-6]-R?\d{2}\b|\bBQ-\d{4}\b')
    m = re.match(r'^\*\*(?:D[1-6]-R?\d{2}|BQ-\d{4})\*\* — (.*)$', linha)
    if m:
        return '«id» — ' + m.group(1)           # a marcação de negrito do rótulo é da edição .md, não do texto do item
    m = re.match(r'^\*\*(?:Comando|Enunciado|Texto-base)\.\*\* (.*)$', linha)
    if m:
        return m.group(1)
    if linha.startswith('### '):
        return rx.sub('«id»', linha, count=1)
    if re.match(r'^- P1-[\w.-]+ \(\d+ de \d+\): ', linha):
        return linha.split(': ', 1)[0] + ': ' + rx.sub('«id»', linha.split(': ', 1)[1])
    return linha


def main():
    E = json.loads(open(os.path.join(OUT, 'pacote_estudante.json'), 'rb').read().decode('utf-8'), object_pairs_hook=collections.OrderedDict)
    P = json.loads(open(os.path.join(OUT, 'pacote.json'), 'rb').read().decode('utf-8'), object_pairs_hook=collections.OrderedDict)
    nomes_base = sorted(os.listdir(BASE))
    F0 = {n: le(os.path.join(BASE, n)) for n in nomes_base}
    chk('M0.1', 'base: 53 arquivos .md da v1.13-E', 53, len(F0))
    if os.path.isdir(PROMOVIDA):
        pr = {n: le(os.path.join(PROMOVIDA, n)) for n in sorted(os.listdir(PROMOVIDA)) if n.endswith('.md')}
        chk('M0.2', 'base = saida/estudante/ (v1.13-E promovida), arquivo a arquivo, em LF', [], sorted(n for n in set(F0) | set(pr) if F0.get(n) != pr.get(n)))
    edital = {e['id']: e['texto'] for e in E['edital']}
    ordem = {e['id']: k for k, e in enumerate(E['edital'])}
    lotes = {l['id']: l for l in E['lotes']}
    F = dict(F0)
    # --- regeneração da base (sanidade): a forma vigente reproduz a v1.13-E
    bq_antigos = [i for i in E['itens'] if i['id'].startswith('BQ-') and i['id'] <= 'BQ-0112']
    chk('M1.1', 'BANCO_itens.md e BANCO_gabarito.md da base são reproduzidos pela forma vigente com os 106 itens', [True, True], [banco_md(bq_antigos)[0] == F0['BANCO_itens.md'], banco_md(bq_antigos)[1] == F0['BANCO_gabarito.md']])
    bq_todos = [i for i in E['itens'] if i['id'].startswith('BQ-')]
    chk('M1.2', '142 itens de banco no pacote_estudante (106 + 36), em ordem de id', [142, True], [len(bq_todos), [i['id'] for i in bq_todos] == sorted(i['id'] for i in bq_todos)])
    F['BANCO_itens.md'], F['BANCO_gabarito.md'] = banco_md(bq_todos)
    chk('M1.3', 'BANCO_itens.md e BANCO_gabarito.md novos começam pela base (os 106 antigos ficam byte a byte)', [True, True], [F['BANCO_itens.md'].startswith(F0['BANCO_itens.md']), F['BANCO_gabarito.md'].startswith(F0['BANCO_gabarito.md'])])
    # --- DA_D<n>_itens/gabarito
    for n in LOTES:
        L = lotes['D%d' % n]
        its = [i for i in E['itens'] if i['id'].startswith('D%d-' % n)]
        canon = [i for i in its if not re.fullmatch(r'D%d-R\d\d' % n, i['id'])]; refo = [i for i in its if re.fullmatch(r'D%d-R\d\d' % n, i['id'])]
        a, b = da_itens_gab_md(L, canon, [])
        chk('M2.%d' % n, 'lote D%d: a forma vigente reproduz DA_D%d_itens.md e DA_D%d_gabarito.md da base (itens canônicos)' % (n, n, n), [True, True], [a == F0['DA_D%d_itens.md' % n], b == F0['DA_D%d_gabarito.md' % n]])
        if refo:
            F['DA_D%d_itens.md' % n], F['DA_D%d_gabarito.md' % n] = da_itens_gab_md(L, canon, refo)
    # --- NUCLEO.md
    F['NUCLEO.md'] = nucleo_md(E, ordem)
    ant = [l for l in F0['NUCLEO.md'].split('\n') if l.startswith('- ')]
    nov = [l for l in F['NUCLEO.md'].split('\n') if l.startswith('- ')]
    chk('M3.1', 'NUCLEO.md: linhas fora de DA iguais às da base, na mesma ordem', [l for l in ant if not l.startswith('- P1-DA-')], [l for l in nov if not l.startswith('- P1-DA-')])
    chk('M3.2', 'NUCLEO.md: cabeçalho igual ao da base', F0['NUCLEO.md'].split('\n- ', 1)[0], F['NUCLEO.md'].split('\n- ', 1)[0])
    nuc_json = {i['id'] for i in E['itens'] if i['nucleo']}
    lista = [x for l in nov for x in l.split(': ', 1)[1].split(', ')]
    chk('M3.3', 'NUCLEO.md: 775 ids núcleo (367 fora de DA + 408 de DA), iguais ao campo nucleo do pacote_estudante, sem repetição', [775, 367, 408, True],
        [len(lista), sum(1 for i in E['itens'] if i['nucleo'] and not i['itemEdital'].startswith('P1-DA-')), sum(1 for i in E['itens'] if i['nucleo'] and i['itemEdital'].startswith('P1-DA-')), set(lista) == nuc_json and len(lista) == len(set(lista))])
    # --- README.md
    r = F0['README.md']
    ov = [l for l in r.split('\n') if l.startswith('- Versão: v')]; od = [l for l in r.split('\n') if l.startswith('- Data: ')]
    chk('M4.1', 'README: linha de versão e de data únicas', [1, 1], [len(ov), len(od)])
    r = r.replace(ov[0], '- Versão: v%s (pacote.json versão %s)' % (VERSAO, E['versao'])).replace(od[0], '- Data: %s' % DATA)
    antiga = '- Direito Administrativo (P1-DA): seis lotes, em arquivos DA_D<n>_estudo.md, DA_D<n>_itens.md e DA_D<n>_gabarito.md; o id de lote vai sempre qualificado como "lote D<n>" (não confundir com as discursivas D1 a D5). Em todos os tópicos de DA há "Resumo do tópico", "Em 1 minuto" e dois visuais em texto.\n'
    chk('M4.2', 'README: a linha de DA ocorre 1 vez (âncora)', 1, r.count(antiga))
    da_p = [i for i in P['itens'] if i['itemEdital'].startswith('P1-DA-')]
    n_real = sum(i['rotulo'] != 'AUTORAL' for i in da_p)
    nova = ('- Direito Administrativo (P1-DA): %d itens, sendo %d de provas anteriores (em BANCO_itens.md e BANCO_gabarito.md) e %d dos seis lotes de estudo, em arquivos DA_D<n>_estudo.md, DA_D<n>_itens.md e DA_D<n>_gabarito.md; '
            'o id de lote vai sempre qualificado como "lote D<n>" (não confundir com as discursivas D1 a D5). Os itens de reforço de DA estão ao fim de cada arquivo DA_D<n>_itens.md e DA_D<n>_gabarito.md dos lotes que os têm, na seção "Itens de reforço". '
            'Em todos os tópicos de DA há "Resumo do tópico", "Em 1 minuto" e dois visuais em texto.\n') % (len(da_p), n_real, len(da_p) - n_real)
    r = r.replace(antiga, nova)
    F['README.md'] = r
    # --- conferências da edição
    mudou = sorted(n for n in F if F.get(n) != F0.get(n))
    nao_mudou = sorted(n for n in F0 if F[n] == F0[n])
    chk('M5.1', '53 arquivos na saída', 53, len(F))
    chk('M5.2', 'mudam exatamente os 12 arquivos da D1 (seção 10)', sorted(MUDAM), mudou)
    chk('M5.3', '41 arquivos ficam byte a byte iguais à v1.13-E (entre eles os 6 DA_D<n>_estudo.md e os 4 arquivos de D5 e D6)', 41, len(nao_mudou))
    chk('M5.4', 'os 6 DA_D<n>_estudo.md e os arquivos de D5 e D6 não mudam', [], [n for n in ['DA_D%d_estudo.md' % k for k in LOTES] + ['DA_D5_itens.md', 'DA_D5_gabarito.md', 'DA_D6_itens.md', 'DA_D6_gabarito.md'] if n not in nao_mudou])
    # ids novos: 1 vez nos _itens e 1 vez nos _gabarito, com o texto do pacote_estudante
    novos = [i for i in E['itens'] if re.fullmatch(r'D[1-6]-R\d\d', i['id'])] + [i for i in bq_todos if i['id'] > 'BQ-0112']
    chk('M6.0', '274 ids novos (238 de reforço + 36 de banco)', [274, 238, 36], [len(novos), sum(1 for i in novos if i['id'].startswith('D')), sum(1 for i in novos if i['id'].startswith('BQ-'))])
    dif = []; ok_i = ok_g = 0
    for it in novos:
        iid = it['id']
        if iid.startswith('BQ-'):
            ti, tg = F['BANCO_itens.md'], F['BANCO_gabarito.md']
            bi = re.findall(r'^### %s\n\n(?:- [^\n]*\n)+\n(?:\*\*Texto-base\.\*\* ([^\n]*)\n\n)?\*\*Comando\.\*\* ([^\n]*)\n\n\*\*Enunciado\.\*\* ([^\n]*)$' % re.escape(iid), ti, re.M)
            bg = re.findall(r'^### %s — Gabarito: ([CE])\n\n- Item do edital: (\S+) \(aderência: (\w+)\)$' % re.escape(iid), tg, re.M)
            if len(bi) == 1 and bi[0] == (it['textoBase'], it['comando'], it['enunciado']) and ti.count('### %s\n' % iid) == 1: ok_i += 1
            else: dif.append(('itens', iid))
            if len(bg) == 1 and bg[0] == (it['gabarito'], it['itemEdital'], it['aderencia']) and tg.count('### %s —' % iid) == 1: ok_g += 1
            else: dif.append(('gabarito', iid))
        else:
            n = int(iid[1]); ti, tg = F['DA_D%d_itens.md' % n], F['DA_D%d_gabarito.md' % n]
            mi = re.findall(r'^\*\*%s\*\* — (.*)$' % re.escape(iid), ti, re.M)
            mg = re.findall(r'^### %s — Gabarito: ([CE])\n\n- Item do edital: (\S+)\n- Justificativa: (.*)$' % re.escape(iid), tg, re.M)
            if len(mi) == 1 and mi[0] == it['enunciado']: ok_i += 1
            else: dif.append(('itens', iid))
            if len(mg) == 1 and mg[0] == (it['gabarito'], it['itemEdital'], it['justificativa']): ok_g += 1
            else: dif.append(('gabarito', iid))
    chk('M6.1', '274 ids, cada um 1 vez nos _itens, com o texto do pacote_estudante (enunciado; comando e texto-base nos de banco)', 274, ok_i)
    chk('M6.2', '274 ids, cada um 1 vez nos _gabarito, com gabarito, item do edital e justificativa (aderência nos de banco) iguais', 274, ok_g)
    chk('M6.3', 'divergências de item', [], dif)
    sec_ok = []
    for n in (1, 2, 3, 4):
        refo = [i['id'] for i in E['itens'] if re.fullmatch(r'D%d-R\d\d' % n, i['id'])]
        for suf, rx in (('itens', r'^\*\*(D%d-R\d\d)\*\* — '), ('gabarito', r'^### (D%d-R\d\d) — Gabarito')):
            t = F['DA_D%d_%s.md' % (n, suf)]
            i0 = t.index('\n## Itens de reforço\n') if t.count('\n## Itens de reforço\n') == 1 else -1
            ids_sec = re.findall(rx % n, t[i0:], re.M) if i0 >= 0 else None
            sec_ok.append((n, suf, ids_sec == refo, len(refo)))
    chk('M6.4', 'seção "## Itens de reforço" (1 vez, ao fim) de DA_D1 a DA_D4 _itens e _gabarito lista os ids de reforço do lote, na ordem do pacote', [], [x for x in sec_ok if not x[2]])
    chk('M6.5', 'DA_D5 e DA_D6 sem seção "Itens de reforço"', 0, sum(F['DA_D%d_%s.md' % (n, s)].count('## Itens de reforço') for n in (5, 6) for s in ('itens', 'gabarito')))
    # --- C-MARCAS nos 12 arquivos que mudam (linhas acrescentadas; máscara de ids só em títulos e listas de ids)
    marcas = []
    for nome in MUDAM:
        base_l = collections.Counter(F0[nome].split('\n')); novas = []
        for l in F[nome].split('\n'):
            if base_l[l] > 0: base_l[l] -= 1
            else: novas.append(l)
        for l in novas:
            if l.startswith('- URL oficial: '):
                continue          # URL oficial do item de banco (campo da edição; a regra de url vale para o texto de item)
            for r_ in MV.cmarcas(mascara(l)):
                marcas.append((nome, r_[0], r_[1], l[:80]))
    chk('M7.1', 'C-MARCAS (D1, 8.1) nas linhas acrescentadas dos 12 arquivos que mudam, com a máscara de ids (títulos de item e listas de ids); linhas "- URL oficial:" de banco fora', [], marcas)
    iso = [(n, m.group(0)) for n in MUDAM if n.startswith('DA_') for m in re.finditer(r'(?<![\w-])D[1-6](?![\w-])', F[n]) if F[n][max(0, m.start() - 5):m.start()] != 'lote ']
    chk('M7.2', 'DA_D<n>_itens/gabarito: 0 "D<n>" isolado que não seja precedido de "lote " (ids com hífen não contam)', [], iso)
    chk('M7.3', 'DA: 0 "**" nos itens e gabaritos de reforço (pares e pegadinhas dos estudos não mudam)', 0, sum(F[n].count('**') for n in MUDAM if n.startswith('DA_D') and n.endswith('gabarito.md')))
    # --- grava
    if os.path.isdir(OUTE):
        shutil.rmtree(OUTE)
    os.makedirs(OUTE)
    for nome, t in sorted(F.items()):
        with open(os.path.join(OUTE, nome), 'wb') as fh:
            fh.write(t.encode('utf-8'))
    lista_arq = [(nome, len(F[nome].encode('utf-8')), hashlib.sha256(F[nome].encode('utf-8')).hexdigest()) for nome in sorted(F, key=lambda s: s.encode('utf-8'))]
    chk('M8.1', 'nenhum CR nos 53 arquivos gravados', 0, sum(open(os.path.join(OUTE, n), 'rb').read().count(b'\r') for n in F))
    linhas_dig = ''.join('estudante/%s\t%s\n' % (n, h) for (n, _b, h) in sorted(lista_arq, key=lambda x: ('estudante/' + x[0]).encode('utf-8')))
    digest = hashlib.sha256(linhas_dig.encode('utf-8')).hexdigest()
    nf = sum(1 for c in CHK if c['resultado'] == 'FALHA')
    rel = collections.OrderedDict(tarefa='T-123 (D1 da GBQ, seção 10)', script='saida/pacote/montagem_v1_14/estudante_md_v114.py', arquivos=len(F), arquivos_alterados=mudou, arquivos_inalterados=len(nao_mudou),
                                  digest_md_R2D=digest, forma_digest='linhas "estudante/<nome>.md" TAB sha256, em ordem de bytes, unidas por \\n com \\n final; SHA-256 desse texto (R2-D)',
                                  listagem=[dict(arquivo=n, bytes=b, sha256=h) for (n, b, h) in lista_arq], conferencias=CHK, total_conferencias=len(CHK), falhas=nf)
    M.grava(os.path.join(OUT, 'estudante_md_v1_14.json'), (json.dumps(rel, ensure_ascii=False, indent=1) + '\n').encode('utf-8'))
    print('edição .md v%s: %d arquivos; %d alterados; %d inalterados; digest %s; %d conferências, %d FALHA' % (VERSAO, len(F), len(mudou), len(nao_mudou), digest, len(CHK), nf))
    sys.exit(1 if nf else 0)


if __name__ == '__main__':
    main()
