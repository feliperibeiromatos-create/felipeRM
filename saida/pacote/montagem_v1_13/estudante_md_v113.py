# estudante_md_v113.py — T-118 (D1 da GBQ, saida/pacote/T118_D1_v1_13_2026-10-20.md, passo 4.3.4) — 2026-10-20 — gerado por gbq-csc
# Edição do estudante v1.13-E em .md (out/estudante/, 53 arquivos), a partir de out/pacote_estudante.json. Base: os 35 .md de saida/estudante/ (SHA-256 em saida/pacote/T115_promocao_v1_12_2026-10-18.md).
# Segue estudante_md_v112.py (gerador_v1_12, congelado). Mudanças, e só elas:
#   (1) 18 arquivos novos DA_D<n>_estudo.md, DA_D<n>_itens.md, DA_D<n>_gabarito.md (n = 1 a 6);
#       estudo = "# " + nome do lote; Prova; Itens do edital; Resumo e Curso (em bloco de texto, como os L<n>); Pares ("a × b | como", sem marcas); Pegadinhas ("[item] rótulo — texto", sem marcas);
#       por tópico: "## Tópico <id> — <texto do edital>", "### Resumo do tópico", "### Em 1 minuto" e os visuais em texto (compare = tabela "Aspecto | a | b" com a legenda; baseLegal = lista
#       "ref — texto (conferido AAAA-MM-DD)" sob a norma; tabela, fluxo, esquema e linha como na v1.12);
#       itens e gabarito no formato dos L<n>_itens.md e L<n>_gabarito.md, com o texto do pacote_estudante.json;
#   (2) NUCLEO.md recalculado (as linhas dos itens do edital já existentes não mudam);
#   (3) README.md: versão v1.13-E, data e as linhas de DA.
# O resto fica byte a byte igual ao da base. Id de lote qualificado como "lote D<n>" fora da plataforma (achado 4): os arquivos se chamam DA_D<n>_*.md e o texto dos arquivos DA não traz D<n> solto.
# Grava sempre os arquivos e out/estudante_md_v1_13.json (com todas as conferências); exit 1 se alguma conferência der FALHA. Não lê relógio.
# Uso: python3 -I estudante_md_v113.py
import collections, hashlib, json, pathlib, re, shutil, sys
R = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).parent
OUT = HERE / 'out'; OUTE = OUT / 'estudante'
BASE = R / 'saida/estudante'
PROMO = R / 'saida/pacote/T115_promocao_v1_12_2026-10-18.md'
VERSAO, DATA = '1.13-E', '2026-10-20'
AVISO = 'Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.'
LOTES = [1, 2, 3, 4, 5, 6]
CHK = []


def sha(b): return hashlib.sha256(b).hexdigest()
def chk(cid, desc, esperado, obtido, ok=None):
    ok = (esperado == obtido) if ok is None else ok
    CHK.append(dict(id=cid, criterio=desc, esperado=esperado, obtido=obtido, resultado='OK' if ok else 'FALHA'))
    print(('OK    ' if ok else 'FALHA ') + cid + ' — ' + desc + ('' if ok else '  [esperado=%r obtido=%r]' % (esperado, obtido)))
    return ok


def fence(text):
    f = '```'
    while f in text:
        f += '`'
    return f + 'text\n' + text + ('\n' if text else '') + f


def cel(s): return str(s).replace('\n', ' ').replace('|', '\\|')


def visual_md(v, falhas):
    L = ['#### %s' % v['titulo'], '']
    t = v['tipo']
    if t == 'tabela':
        L.append('| ' + ' | '.join(cel(c) for c in v['colunas']) + ' |')
        L.append('|' + '|'.join('---' for _ in v['colunas']) + '|')
        for r in v['linhas']:
            L.append('| ' + ' | '.join(cel(c) for c in r) + ' |')
        if v.get('legenda'):
            L += ['', '*%s*' % v['legenda']]
    elif t == 'compare':
        L.append('| Aspecto | %s | %s |' % (cel(v['a']), cel(v['b'])))
        L.append('|---|---|---|')
        for r in v['linhas']:
            L.append('| ' + ' | '.join(cel(c) for c in r) + ' |')
        L += ['', '*%s*' % v['legenda']]
    elif t == 'baseLegal':
        L.append('**%s**' % v['norma'])
        L.append('')
        for d in v['dispositivos']:
            L.append('- %s — %s (conferido %s)' % (d['ref'], d['texto'], d['conferido']))
    elif t == 'fluxo':
        L += ['%d. %s' % (k, p) for k, p in enumerate(v['passos'], 1)]
    elif t == 'esquema':
        L.append('- **%s**' % v['centro'])
        L += ['  - %s' % r for r in v['ramos']]
    elif t == 'linha':
        L += ['- %s — %s' % (m['quando'], m['texto']) for m in v['marcos']]
    elif t == 'barras':
        L += ['- %s: %s%s' % (d['rotulo'], d['valor'], (' ' + v['unidade']) if v['unidade'] else '') for d in v['dados']]
        L += ['', 'Fonte: %s' % v['fonte']]
    else:
        falhas.append('visual de tipo desconhecido: %s' % t)
    return L


def lote_do_topico(k, lote):
    return k in lote['itensEdital'] or any(x.startswith(k + '.') for x in lote['itensEdital'])


def estudo_md(L, E, edital, falhas):
    out = ['# %s' % L['nome'], '', 'Prova: %s' % L['prova'], '', '## Itens do edital', '']
    for e in L['itensEdital']:
        out.append('- %s — %s' % (e, edital[e]))
    out += ['', '## Resumo', '', fence(L['resumo']), '', '## Curso', '', fence(L['curso']), '', '## Pares', '']
    if L['pares']:
        for p in L['pares']:
            for k in ('a', 'b', 'como'):
                if '\n' in p[k]: falhas.append('par com quebra de linha em %s' % L['id'])
            linha = '- %s' % p['a']
            if p['b']:
                linha += ' × %s' % p['b']
            out.append(linha + ' | %s' % p['como'])
    else:
        out.append('_Nenhum par neste lote._')
    out += ['', '## Pegadinhas', '']
    if L['pegadinhas']:
        for g in L['pegadinhas']:
            if '\n' in g['texto'] or '\n' in g['rotulo']: falhas.append('pegadinha com quebra de linha em %s' % L['id'])
            out.append('- [%s] %s — %s' % (g['itemEdital'], g['rotulo'], g['texto']))
    else:
        out.append('_Nenhuma pegadinha registrada neste lote._')
    out.append('')
    n = 0
    for k, t in E['topicos'].items():
        if not k.startswith('P1-DA-') or not lote_do_topico(k, L):
            continue
        n += 1
        out += ['## Tópico %s — %s' % (k, edital[k]), '', '### Resumo do tópico', '']
        for p in t['resumo'].split('\n\n'):
            out += [p, '']
        out += ['### Em 1 minuto', ''] + ['- %s' % x for x in t['emUmMinuto']] + ['']
        for v in t['visuais']:
            out += visual_md(v, falhas) + ['']
    return '\n'.join(out).rstrip('\n') + '\n', n


def itens_gab_md(L, its):
    I = ['# %s — itens' % L['nome'], '', 'Itens para julgar (C = certo, E = errado). Gabarito e justificativas no arquivo DA_%s_gabarito.md.' % L['id'], '']
    G = ['# %s — gabarito e justificativas' % L['nome'], '']
    cur = None
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


def main():
    falhas = []
    E = json.loads((OUT / 'pacote_estudante.json').read_text(encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
    # --- base: 35 .md, SHA-256 contra a promoção da v1.12
    promo = dict((m.group(2), m.group(1)) for m in re.finditer(r'^([0-9a-f]{64}) \*(\S+\.md)$', PROMO.read_text(encoding='utf-8'), re.M))
    F0 = {p.name: p.read_text(encoding='utf-8') for p in sorted(BASE.glob('*.md'))}
    chk('M0.1', 'base: 35 arquivos .md em saida/estudante/ (e 35 SHA-256 na promoção da v1.12)', [35, 35], [len(F0), len(promo)])
    chk('M0.2', 'base: SHA-256 de cada arquivo = o da T115_promocao_v1_12', [], sorted(n for n in F0 if sha((BASE / n).read_bytes()) != promo.get(n)))
    edital = {e['id']: e['texto'] for e in E['edital']}
    ordem = {e['id']: k for k, e in enumerate(E['edital'])}
    lotes = {l['id']: l for l in E['lotes']}
    F = dict(F0)
    novos = []; secoes = 0
    for n in LOTES:
        L = lotes['D%d' % n]
        its = [i for i in E['itens'] if i['id'].startswith('D%d-' % n)]
        est, nt = estudo_md(L, E, edital, falhas); secoes += nt
        it_md, gab_md = itens_gab_md(L, its)
        for nome, t in (('DA_D%d_estudo.md' % n, est), ('DA_D%d_itens.md' % n, it_md), ('DA_D%d_gabarito.md' % n, gab_md)):
            F[nome] = t; novos.append(nome)
    # --- NUCLEO.md
    F['NUCLEO.md'] = nucleo_md(E, ordem)
    ant = [l for l in F0['NUCLEO.md'].split('\n') if l.startswith('- ')]
    nov = [l for l in F['NUCLEO.md'].split('\n') if l.startswith('- ')]
    chk('M2.1', 'NUCLEO.md: as linhas dos itens do edital já existentes não mudam (e vêm na mesma ordem)', ant, [l for l in nov if not l.startswith('- P1-DA-')])
    chk('M2.2', 'NUCLEO.md: cabeçalho igual ao da base', F0['NUCLEO.md'].split('\n- ', 1)[0], F['NUCLEO.md'].split('\n- ', 1)[0])
    nuc_json = {i['id'] for i in E['itens'] if i['nucleo']}
    lista = [x for l in nov for x in l.split(': ', 1)[1].split(', ')]
    chk('M2.3', 'NUCLEO.md: 733 ids núcleo (367 da v1.12 + 366 de DA), iguais ao campo nucleo do pacote_estudante', [733, 367, 366, True], [len(lista), len([x for x in lista if not x.startswith('D')]), len([x for x in lista if x.startswith('D')]), set(lista) == nuc_json and len(lista) == len(set(lista))])
    # --- README.md
    r = F0['README.md']
    ov = [l for l in r.split('\n') if l.startswith('- Versão: v')]; od = [l for l in r.split('\n') if l.startswith('- Data: ')]
    chk('M3.1', 'README: linha de versão e de data únicas', [1, 1], [len(ov), len(od)])
    r = r.replace(ov[0], '- Versão: v%s (pacote.json versão %s)' % (VERSAO, E['versao'])).replace(od[0], '- Data: %s' % DATA)
    ancora = '- L6B: [L6B_estudo.md](L6B_estudo.md) (resumo, curso, pares, pegadinhas); [L6B_itens.md](L6B_itens.md) (itens sem gabarito); [L6B_gabarito.md](L6B_gabarito.md) (gabarito e justificativas)\n'
    chk('M3.2', 'README: linha do L6B ocorre 1 vez (âncora das linhas de DA)', 1, r.count(ancora))
    da_lin = ''.join('- DA, lote D%d: [DA_D%d_estudo.md](DA_D%d_estudo.md) (resumo, curso, pares, pegadinhas, tópicos); [DA_D%d_itens.md](DA_D%d_itens.md) (itens sem gabarito); [DA_D%d_gabarito.md](DA_D%d_gabarito.md) (gabarito e justificativas)\n' % ((n,) * 7) for n in LOTES)
    r = r.replace(ancora, ancora + da_lin)
    ancora2 = '- Cada arquivo _estudo.md traz, ao fim, uma seção "Tópico" por tópico do lote: o resumo ("Resumo do tópico") e, em alguns tópicos, "Em 1 minuto" e os visuais em texto.\n'
    chk('M3.3', 'README: linha dos tópicos ocorre 1 vez', 1, r.count(ancora2))
    r = r.replace(ancora2, ancora2 + '- Direito Administrativo (P1-DA): seis lotes, em arquivos DA_D<n>_estudo.md, DA_D<n>_itens.md e DA_D<n>_gabarito.md; o id de lote vai sempre qualificado como "lote D<n>" (não confundir com as discursivas D1 a D5). Em todos os tópicos de DA há "Resumo do tópico", "Em 1 minuto" e dois visuais em texto.\n')
    F['README.md'] = r
    # --- conferências da edição
    mudou = sorted(n for n in F if F.get(n) != F0.get(n))
    nao_mudou = sorted(n for n in F0 if F[n] == F0[n])
    chk('M4.1', '53 arquivos na saída', 53, len(F))
    chk('M4.2', '33 arquivos da base não mudam (byte a byte)', 33, len(nao_mudou))
    chk('M4.3', 'mudam: NUCLEO.md, README.md; novos: 18 DA_D<n>_*.md', [['NUCLEO.md', 'README.md'], 18], [[n for n in mudou if n not in novos], len(novos)])
    chk('M4.4', 'nenhum dos 33 inalterados foi tocado (SHA-256 igual ao da promoção)', [], sorted(n for n in nao_mudou if sha(F[n].encode('utf-8')) != promo.get(n)))
    da_arq = {n: t for n, t in F.items() if n.startswith('DA_D')}
    # ids: 1 vez nos _itens e 1 vez nos _gabarito; texto igual ao pacote_estudante
    ok_itens = ok_gab = 0; dif = []
    for n in LOTES:
        its = [i for i in E['itens'] if i['id'].startswith('D%d-' % n)]
        ti = da_arq['DA_D%d_itens.md' % n]; tg = da_arq['DA_D%d_gabarito.md' % n]
        mi = re.findall(r'^\*\*(D%d-\d\d)\*\* — (.*)$' % n, ti, re.M)
        mg = re.findall(r'^### (D%d-\d\d) — Gabarito: ([CE])\n\n- Item do edital: (\S+)\n- Justificativa: (.*)$' % n, tg, re.M)
        di = dict(mi); dg = {a: (b, c, d) for a, b, c, d in mg}
        for it in its:
            if len([1 for a, _ in mi if a == it['id']]) == 1 and di.get(it['id']) == it['enunciado']: ok_itens += 1
            else: dif.append(('itens', it['id']))
            if len([1 for a, _, _, _ in mg if a == it['id']]) == 1 and dg.get(it['id']) == (it['gabarito'], it['itemEdital'], it['justificativa']): ok_gab += 1
            else: dif.append(('gabarito', it['id']))
    chk('M5.1', '410 ids, cada um 1 vez nos _itens, com enunciado igual ao do pacote_estudante', 410, ok_itens)
    chk('M5.2', '410 ids, cada um 1 vez nos _gabarito, com gabarito, item do edital e justificativa iguais', 410, ok_gab)
    chk('M5.3', 'divergências de item', [], dif)
    tot_ocor = sum(len(re.findall(r'D%d-\d\d' % n, '\n'.join(t for k, t in da_arq.items() if k.endswith('_itens.md') or k.endswith('_gabarito.md')))) for n in LOTES)
    chk('M5.4', 'ocorrências de ids D<n>-NN nos _itens e _gabarito: 820 (410 × 2; nenhuma remissão cruzada no texto)', 820, tot_ocor)
    chk('M6.1', 'linha 1 de cada DA_D<n>_estudo.md = "# " + lotes[D<n>].nome', [], [n for n in LOTES if da_arq['DA_D%d_estudo.md' % n].split('\n', 1)[0] != '# ' + lotes['D%d' % n]['nome']])
    # dispositivos literais
    disp = [(d['ref'], d['texto'], d['conferido']) for k, t in E['topicos'].items() if k.startswith('P1-DA-') for v in t['visuais'] if v['tipo'] == 'baseLegal' for d in v['dispositivos']]
    estudo_all = '\n'.join(da_arq['DA_D%d_estudo.md' % n] for n in LOTES)
    chk('M6.2', '105 dispositivos de baseLegal, literais (ref — texto (conferido data)) nos DA_D<n>_estudo.md', [105, []], [len(disp), [d[0] for d in disp if '- %s — %s (conferido %s)' % d not in estudo_all]])
    n_comp = sum(1 for k, t in E['topicos'].items() if k.startswith('P1-DA-') for v in t['visuais'] if v['tipo'] == 'compare')
    n_bl = sum(1 for k, t in E['topicos'].items() if k.startswith('P1-DA-') for v in t['visuais'] if v['tipo'] == 'baseLegal')
    n_tab_asp = sum(1 for k, t in E['topicos'].items() if k.startswith('P1-DA-') for v in t['visuais'] if v['tipo'] == 'tabela' and v['colunas'][:1] == ['Aspecto'])      # tabelas cuja 1ª coluna também se chama Aspecto
    chk('M6.3', 'visuais compare (tabela "Aspecto | a | b", fora as tabelas de 1ª coluna "Aspecto") e baseLegal (lista): 23 e 29', [23, 29, 23, 29], [n_comp, n_bl, estudo_all.count('| Aspecto | ') - n_tab_asp, len(re.findall(r'^\*\*[^\n]+\*\*\n\n- [^\n]+ — [^\n]+ \(conferido \d{4}-\d\d-\d\d\)$', estudo_all, re.M))])
    chk('M6.4', 'tópicos DA renderizados', 39, secoes)
    chk('M6.5', 'seções "## Tópico" nos 6 estudos', 39, estudo_all.count('\n## Tópico '))
    # proibições nos arquivos DA
    todo = {n: t for n, t in da_arq.items()}
    def hits(rx, flags=0, so_estudo=False):
        c = []
        for n, t in todo.items():
            for m in re.finditer(rx, t, flags):
                c.append((n, m.group(0)))
        return c
    chk('M7.1', 'DA: 0 ocorrências de "folha" (sem distinção de caixa)', [], hits(r'folha', re.I))
    chk('M7.2', 'DA: 0 ocorrências de \\bR\\d{1,2}\\b', [], hits(r'\bR\d{1,2}\b'))
    chk('M7.3', 'DA: 0 ocorrências de \\bF\\d{1,2}\\b', [], hits(r'\bF\d{1,2}\b'))
    chk('M7.4', 'DA: 0 ocorrências de "QA PENDENTE"', [], hits(r'QA PENDENTE'))
    chk('M7.5', 'DA: 0 url (http, https, www)', [], hits(r'https?://|www\.'))
    iso = [(n, m.group(0), t[max(0, m.start() - 6):m.start()]) for n, t in todo.items() for m in re.finditer(r'(?<![\w-])D[1-6](?![\w-])', t) if t[max(0, m.start() - 5):m.start()] != 'lote ']
    chk('M7.6', 'DA: 0 "D<n>" isolado que não seja precedido de "lote "', [], iso)
    # pares e pegadinhas sem **
    sec_bad = []
    for n in LOTES:
        t = da_arq['DA_D%d_estudo.md' % n]
        a = t.index('\n## Pares\n'); b = t.index('\n## Pegadinhas\n'); c = t.find('\n## Tópico ', b)
        c = len(t) if c < 0 else c
        if '**' in t[a:b] or '**' in t[b:c]: sec_bad.append(n)
        if not (a < b < c): sec_bad.append(n)
    chk('M7.7', 'DA: 0 "**" nas seções Pares e Pegadinhas dos 6 estudos', [], sec_bad)
    chk('M7.8', 'conferências internas de montagem (quebras de linha, tipos de visual)', [], falhas)
    # --- grava
    if OUTE.is_dir():
        shutil.rmtree(OUTE)
    OUTE.mkdir(parents=True)
    for nome, t in sorted(F.items()):
        with open(OUTE / nome, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(t)
    nf = sum(1 for c in CHK if c['resultado'] == 'FALHA')
    rel = collections.OrderedDict(tarefa='T-118 (D1 da GBQ, 4.3.4)', script='saida/pacote/montagem_v1_13/estudante_md_v113.py', arquivos=len(F), arquivos_novos=novos, arquivos_alterados=[n for n in mudou if n not in novos],
                                  arquivos_inalterados=len(nao_mudou), topicos_renderizados=secoes, conferencias=CHK, total_conferencias=len(CHK), falhas=nf)
    (OUT / 'estudante_md_v1_13.json').write_text(json.dumps(rel, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('edição .md v%s: %d arquivos; %d novos; %d alterados; %d tópicos; %d conferências, %d FALHA' % (VERSAO, len(F), len(novos), len(rel['arquivos_alterados']), secoes, len(CHK), nf))
    sys.exit(1 if nf else 0)


if __name__ == '__main__':
    main()
