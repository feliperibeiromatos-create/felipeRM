# -*- coding: utf-8 -*-
"""T-56 (v1.3; evolução do gerador T-48) — fidelidade da edição do estudante.
Lê os .md da edição do estudante (parser independente do gerador) e compara, campo a campo,
com o pacote.json v1.3 (fonte única):
  (1) texto do estudante == texto do pacote com as deleções das regras (estudante_marcas.strip_text);
  (2) independentemente das regras: o texto do estudante é obtido do texto do pacote SOMENTE por deleção
      (difflib: só opcodes equal/delete; nenhum insert/replace);
  (3) campos de prova (comando, textoBase, enunciado), metadados e gabaritos idênticos ao pacote;
  (4) higiene: nenhuma marca da lista nos arquivos; itens sem gabarito/justificativa."""
import json, os, re, sys, difflib, collections
import estudante_marcas as em
import estudante_gen as gen

AVISO = gen.AVISO
LEGENDAS = {}      # lote -> legenda literal (v1.3)
DIFFS = []     # (arquivo, campo, tipo, detalhe)
NCOMP = collections.Counter()   # campos comparados por categoria

def rd(path):
    return open(path, encoding='utf-8').read().split('\n')

CASE_LOG = []     # R1: trocas de caixa aceitas (exceção fechada da C-15): (arquivo, campo, antes, depois)

def only_deletions(orig, new, arq=None, campo=None):
    """R1: só deleção, com UMA exceção fechada: troca minúscula → maiúscula da primeira letra (lista CAIXA, C-15),
    registrada em CASE_LOG. Comparação sensível à caixa; a troca aparece como 'replace' cujo trecho novo é UMA letra
    maiúscula = a última letra (minúscula) do trecho antigo (o resto do trecho antigo é deleção)."""
    sm = difflib.SequenceMatcher(None, orig, new, autojunk=False)
    bad = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op in ('equal', 'delete'):
            continue
        old, nw = orig[i1:i2], new[j1:j2]
        if op == 'replace' and len(nw) == 1 and old[-1].islower() and nw == old[-1].upper():
            CASE_LOG.append((arq, campo, orig[i1 - 12:i2 + 20], new[j1 - 12:j2 + 20]))
        else:
            bad.append((op, old, nw))
    return bad

def cmp_text(arq, campo, student, pacote_text, regras=True, cat='texto'):
    """student: texto lido do .md; pacote_text: texto do pacote (original)."""
    NCOMP[cat] += 1
    if regras:
        esperado = em.strip_text(pacote_text, collections.Counter(), arq)
        if student != esperado:
            DIFFS.append((arq, campo, 'difere da regra', (student[:80], esperado[:80])))
        bad = only_deletions(pacote_text, student, arq, campo)
        if bad:
            DIFFS.append((arq, campo, 'não é só deleção', bad[:3]))
    else:
        if student != pacote_text:
            DIFFS.append((arq, campo, 'difere do pacote (campo de prova/metadado)', (student[:80], pacote_text[:80])))

def fences(lines, i):
    """lines[i] é a abertura; devolve (texto, índice após o fechamento)."""
    m = re.match(r'^(`{3,})text$', lines[i])
    assert m, (i, lines[i])
    f = m.group(1)
    j = i + 1
    buf = []
    while lines[j] != f:
        buf.append(lines[j]); j += 1
    return '\n'.join(buf), j + 1

def parse_estudo(lines):
    r = {'secoes': {}}
    r['titulo'] = lines[0][2:]
    r['prova'] = lines[2].split(': ', 1)[1]
    i = lines.index('## Itens do edital') + 2
    ed = []
    while lines[i].startswith('- '):
        ed.append(lines[i][2:]); i += 1
    r['edital'] = ed
    i = lines.index('## Resumo') + 2
    r['resumo'], i = fences(lines, i)
    i = lines.index('## Curso') + 2
    r['curso'], i = fences(lines, i)
    i = lines.index('## Pares') + 2
    pares = []
    while lines[i].startswith('- **'):
        # R1 / C-24: ' × **…**' e ' — …' são omitidos quando b / como são vazios
        m = re.match(r'^- \*\*(.*?)\*\*(?: × \*\*(.*?)\*\*)?(?: — (.*))?$', lines[i]); assert m, lines[i]
        pares.append(tuple(g or '' for g in m.groups())); i += 1
    r['pares'] = pares
    i = lines.index('## Pegadinhas') + 2
    peg = []
    while i < len(lines) and lines[i].startswith('- ['):
        m = re.match(r'^- \[(\S+)\] \*\*(.*?)\*\* — (.*)$', lines[i]); assert m, lines[i]
        peg.append(m.groups()); i += 1
    r['pegadinhas'] = peg
    return r

def parse_itens(lines):
    """blocos de comando / texto-base / itens '**id** — enunciado' (+ aviso)."""
    out = []; cmd = None; tb = ''; tb_pend = None
    i = 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith('**Comando.** '):      # R1 / C-11: o texto-base vem ANTES do comando
            cmd = ln[len('**Comando.** '):]; tb = tb_pend or ''; tb_pend = None
        elif ln.startswith('**Texto-base.** '):
            tb_pend = ln[len('**Texto-base.** '):]
        elif re.match(r'^\*\*[^\s*]+\*\* — ', ln):
            m = re.match(r'^\*\*([^\s*]+)\*\* — (.*)$', ln)
            it = {'id': m.group(1), 'enunciado': m.group(2), 'comando': cmd, 'textoBase': tb, 'aviso': False}
            if i + 2 < len(lines) and lines[i + 2] == '> ' + AVISO:
                it['aviso'] = True
            out.append(it)
        i += 1
    return out

def nota_exib(it):
    """R1 / C-18: exceção fechada — a nota de BQ-0003 sai da edição sem ' (D-LEI-15352)' (única diferença admitida)."""
    n = it.get('nota')
    if n is None: return None
    if ' (D-LEI-15352)' in n:
        assert it['id'] == 'BQ-0003' and n.count(' (D-LEI-15352)') == 1
        NOTA_EXC.append(it['id'])
        return n.replace(' (D-LEI-15352)', '')
    return n

NOTA_EXC = []

def parse_gab(lines, sim=False):
    out = []; cur = None
    for ln in lines:
        m = re.match(r'^### (?:(\d+) — )?(\S+) — Gabarito: ([CE])$', ln)
        if m:
            cur = {'n': m.group(1), 'id': m.group(2), 'gabarito': m.group(3), 'justificativa': None, 'nota': None,
                   'edital': None, 'aderencia': None, 'aviso': False}
            out.append(cur); continue
        if cur is None: continue
        if ln.startswith('- Item do edital: '):
            v = ln[len('- Item do edital: '):]
            mm = re.match(r'^(\S+) \(aderência: (\S+)\)$', v)
            if mm: cur['edital'], cur['aderencia'] = mm.groups()
            else: cur['edital'] = v
        elif ln.startswith('- Justificativa: '): cur['justificativa'] = ln[len('- Justificativa: '):]
        elif ln.startswith('- Nota: '): cur['nota'] = ln[len('- Nota: '):]
        elif ln == '> ' + AVISO: cur['aviso'] = True
    return out

def main(pacote_path, dir_est):
    P = json.load(open(pacote_path, encoding='utf-8'))
    itens = {i['id']: i for i in P['itens']}
    edital = {e['id']: e['texto'] for e in P['edital']}
    esperados = {'README.md'}

    # ---- lotes
    for L in P['lotes']:
        lid = L['id']
        a = f'{lid}_estudo.md'; esperados.add(a)
        e = parse_estudo(rd(os.path.join(dir_est, a)))
        cmp_text(a, 'nome', e['titulo'], L['nome'])
        cmp_text(a, 'prova', e['prova'], L['prova'], regras=False, cat='metadado')
        want_ed = [f'{x} — {edital[x]}' for x in L['itensEdital']]
        NCOMP['metadado'] += 1
        if e['edital'] != want_ed: DIFFS.append((a, 'itensEdital', 'difere', (e['edital'][:2], want_ed[:2])))
        cmp_text(a, 'resumo', e['resumo'], L['resumo'])
        cmp_text(a, 'curso', e['curso'], L['curso'])
        if len(e['pares']) != len(L['pares']): DIFFS.append((a, 'pares', 'quantidade', (len(e['pares']), len(L['pares']))))
        for k, (pe, pp) in enumerate(zip(e['pares'], L['pares'])):
            for fld, val in zip(('a', 'b', 'como'), pe):
                cmp_text(a, f'pares[{k}].{fld}', val, pp[fld])
        if len(e['pegadinhas']) != len(L['pegadinhas']): DIFFS.append((a, 'pegadinhas', 'quantidade', (len(e['pegadinhas']), len(L['pegadinhas']))))
        for k, (pe, pp) in enumerate(zip(e['pegadinhas'], L['pegadinhas'])):
            NCOMP['metadado'] += 1
            if pe[0] != pp['itemEdital']: DIFFS.append((a, f'pegadinhas[{k}].itemEdital', 'difere', (pe[0], pp['itemEdital'])))
            cmp_text(a, f'pegadinhas[{k}].rotulo', pe[1], pp['rotulo'])
            cmp_text(a, f'pegadinhas[{k}].texto', pe[2], pp['texto'])
        # itens e gabarito do lote
        its = [i for i in P['itens'] if i['rotulo'] == 'AUTORAL' and gen.lote_of(i['id']) == lid]
        fi = f'{lid}_itens.md'; fg = f'{lid}_gabarito.md'; esperados |= {fi, fg}
        pi = parse_itens(rd(os.path.join(dir_est, fi)))
        pg = parse_gab(rd(os.path.join(dir_est, fg)))
        check_itens(fi, pi, its)
        check_gab(fg, pg, its)
        # v1.3 (D-T53-01): legenda literal do lote só no topo do *_gabarito.md, antes do primeiro item; lote sem o campo, sem legenda
        gl = rd(os.path.join(dir_est, fg))
        NCOMP['legenda'] += 1
        if L.get('legendaMecanismo'):
            if not (gl[0] == f'# {L["nome"]} — gabarito e justificativas' and gl[1] == '' and gl[2] == L['legendaMecanismo'] and gl[3] == '' and gl[4].startswith('### ')):
                DIFFS.append((fg, 'legendaMecanismo', 'não está literal no topo', gl[:5]))
            LEGENDAS[lid] = L['legendaMecanismo']
        elif not (gl[2].startswith('### ')):
            DIFFS.append((fg, 'legendaMecanismo', 'lote sem o campo, mas há texto antes do primeiro item', gl[:3]))

    # ---- banco
    bq = [i for i in P['itens'] if i['rotulo'] != 'AUTORAL']
    fb, fbg = 'BANCO_itens.md', 'BANCO_gabarito.md'; esperados |= {fb, fbg}
    lines = rd(os.path.join(dir_est, fb))
    blocos = []
    cur = None
    for ln in lines:
        m = re.match(r'^### (BQ-\d+)$', ln)
        if m: cur = {'id': m.group(1), 'aviso': False, 'nota': None, 'tb': ''}; blocos.append(cur); continue
        if cur is None: continue
        for key, lab in (('certame', '- Certame: '), ('cargo', '- Cargo: '), ('ano', '- Ano: '), ('numero', '- Número: '), ('url', '- URL oficial: '),
                         ('comando', '**Comando.** '), ('tb', '**Texto-base.** '), ('enunciado', '**Enunciado.** ')):
            if ln.startswith(lab): cur[key] = ln[len(lab):]
        if ln == '> ' + AVISO: cur['aviso'] = True
        if ln.startswith('> Nota: '): cur['nota'] = ln[len('> Nota: '):]
    NCOMP['estrutura'] += 1
    if [b['id'] for b in blocos] != [i['id'] for i in bq]: DIFFS.append((fb, 'ids', 'ordem/quantidade', (len(blocos), len(bq))))
    for b, it in zip(blocos, bq):
        for key in ('certame', 'cargo', 'url', 'comando', 'enunciado'):
            cmp_text(fb, f'{it["id"]}.{key}', b.get(key), it[key], regras=False, cat='prova/metadado')
        cmp_text(fb, f'{it["id"]}.textoBase', b['tb'], it['textoBase'], regras=False, cat='prova/metadado')
        cmp_text(fb, f'{it["id"]}.ano', b.get('ano'), str(it['ano']), regras=False, cat='prova/metadado')
        cmp_text(fb, f'{it["id"]}.numero', b.get('numero'), str(it['numero']), regras=False, cat='prova/metadado')
        NCOMP['aviso/nota'] += 1
        if b['aviso'] != bool(it.get('volatil')): DIFFS.append((fb, it['id'], 'aviso VOLÁTIL', (b['aviso'], it.get('volatil'))))
        if b['nota'] != nota_exib(it): DIFFS.append((fb, it['id'], 'nota', (b['nota'], nota_exib(it))))
    check_gab(fbg, parse_gab(rd(os.path.join(dir_est, fbg))), bq)

    # ---- simulados
    for s in P['simulados']:
        sid = s['id']
        ff, fg = f'{sid}_folha.md', f'{sid}_gabarito.md'; esperados |= {ff, fg}
        itl = [itens[x] for x in s['itens']]
        lines = rd(os.path.join(dir_est, ff))
        pf = []
        cmd = None; tb = ''; tb_pend = None
        for k, ln in enumerate(lines):
            if ln.startswith('**Comando.** '): cmd = ln[13:]; tb = tb_pend or ''; tb_pend = None     # R1 / C-11
            elif ln.startswith('**Texto-base.** '): tb_pend = ln[len('**Texto-base.** '):]
            else:
                m = re.match(r'^\*\*(\d+)\*\* — (.*)$', ln)      # R1 / C-10: a folha NÃO traz o id
                if m:
                    nota = None; j = k + 1
                    while j < len(lines) and (lines[j] == '' or lines[j].startswith('> ')):
                        if lines[j].startswith('> Nota: '): nota = lines[j][len('> Nota: '):]
                        j += 1
                    pf.append({'n': int(m.group(1)), 'id': s['itens'][int(m.group(1)) - 1] if int(m.group(1)) - 1 < len(s['itens']) else None,
                               'enunciado': m.group(2), 'comando': cmd, 'textoBase': tb, 'nota': nota,
                               'aviso': lines[k + 2] == '> ' + AVISO if k + 2 < len(lines) else False})
        NCOMP['estrutura'] += 1
        if len(pf) != s['n'] or [x['n'] for x in pf] != list(range(1, s['n'] + 1)):
            DIFFS.append((ff, 'itens', 'ordem/quantidade', (len(pf), s['n'])))
        NCOMP['estrutura'] += 1
        ids_folha = [it['id'] for it in itl if it['id'] in '\n'.join(lines)]
        if ids_folha: DIFFS.append((ff, 'ids', 'a folha traz id de origem', ids_folha[:3]))
        for x, it in zip(pf, itl):
            NCOMP['aviso/nota'] += 1
            if x['nota'] != nota_exib(it): DIFFS.append((ff, it['id'], 'nota (folha)', (x['nota'], nota_exib(it))))
            for key in ('comando', 'textoBase', 'enunciado'):
                cmp_text(ff, f'{it["id"]}.{key}', x[key], it[key], regras=False, cat='prova/metadado')
            NCOMP['aviso/nota'] += 1
            if x['aviso'] != bool(it.get('volatil')): DIFFS.append((ff, it['id'], 'aviso VOLÁTIL', (x['aviso'], it.get('volatil'))))
        txt = '\n'.join(lines)
        NCOMP['metadado'] += 3
        for lab, val in (('- Tipo: ', s['tipo']), ('- Versão: ', s['versao']), ('- Número de itens: ', str(s['n']))):
            if (lab + val) not in lines: DIFFS.append((ff, lab, 'cabeçalho', val))
        pg = parse_gab(rd(os.path.join(dir_est, fg)))
        check_gab(fg, pg, itl, sim=True)

    # ---- discursivas
    fd, fdp = 'DISCURSIVAS.md', 'DISCURSIVAS_padrao.md'; esperados |= {fd, fdp}
    tipos = {'questao': 'Questão', 'peca': 'Peça técnica'}
    L1 = rd(os.path.join(dir_est, fd)); L2 = rd(os.path.join(dir_est, fdp))
    for d in P['discursivas']:
        h = f'## {d["id"]} — {tipos[d["tipo"]]}'
        i = L1.index(h) + 2
        txt, _ = fences(L1, i)
        cmp_text(fd, f'{d["id"]}.comando', txt, d['comando'])
        i = L2.index(h) + 4
        txt, i = fences(L2, i)
        cmp_text(fdp, f'{d["id"]}.padrao', txt, d['padrao'])
        i = L2.index('### Aspectos (valor)', i) + 2
        asp = []
        while L2[i].startswith('- ('):
            m = re.match(r'^- \((\d+)\) (.*) — valor: ([\d,]+)$', L2[i]); assert m, L2[i]
            asp.append(m.groups()); i += 1
        if len(asp) != len(d['aspectos']): DIFFS.append((fdp, d['id'], 'aspectos qtd', (len(asp), len(d['aspectos']))))
        for (n, t, v), a in zip(asp, d['aspectos']):
            NCOMP['metadado'] += 2
            if int(n) != a['n'] or abs(float(v.replace(',', '.')) - a['valor']) > 1e-9: DIFFS.append((fdp, d['id'], 'aspecto n/valor', (n, v, a['n'], a['valor'])))
            cmp_text(fdp, f'{d["id"]}.aspectos[{a["n"]}]', t, a['texto'])
        i = L2.index('### Quesitos', i) + 2
        qs = []
        while i < len(L2) and L2[i].startswith('- **'):
            m = re.match(r'^- \*\*(\S+)\*\* — (.*)$', L2[i]); assert m, L2[i]
            q = {'id': m.group(1), 'nome': m.group(2), 'conceitos': []}; i += 1
            while i < len(L2) and L2[i].startswith('  - '):
                q['conceitos'].append(L2[i][4:]); i += 1
            qs.append(q)
        if len(qs) != len(d['quesitos']): DIFFS.append((fdp, d['id'], 'quesitos qtd', (len(qs), len(d['quesitos']))))
        for q, pq in zip(qs, d['quesitos']):
            NCOMP['metadado'] += 1
            if q['id'] != pq['id']: DIFFS.append((fdp, d['id'], 'quesito id', (q['id'], pq['id'])))
            cmp_text(fdp, f'{d["id"]}.quesito {pq["id"]}.nome', q['nome'], pq['nome'])
            if len(q['conceitos']) != len(pq['conceitos']): DIFFS.append((fdp, d['id'], 'conceitos qtd', (pq['id'],)))
            for k, (c, pc) in enumerate(zip(q['conceitos'], pq['conceitos'])):
                cmp_text(fdp, f'{d["id"]}.quesito {pq["id"]}.conceito[{k}]', c, pc)

    # ---- README e conjunto de arquivos
    files = set(os.listdir(dir_est))
    NCOMP['estrutura'] += 1
    if files != esperados: DIFFS.append(('(pasta)', 'arquivos', 'conjunto', (sorted(files - esperados), sorted(esperados - files))))
    rd_ = '\n'.join(rd(os.path.join(dir_est, 'README.md')))
    for k in ('v1.3', P['geradoEm'], 'material de estudo; gabaritos em arquivo separado'):
        NCOMP['estrutura'] += 1
        if k not in rd_: DIFFS.append(('README.md', k, 'ausente', ''))

    # ---- v1.3: a legenda de cada lote aparece só no *_gabarito.md do próprio lote; os avisos do SIM-0 não aparecem em arquivo algum
    todos = {f: '\n'.join(rd(os.path.join(dir_est, f))) for f in sorted(files)}
    for lid, leg in LEGENDAS.items():
        NCOMP['legenda'] += 1
        onde = sorted(f for f, tx in todos.items() if leg in tx)
        # a mesma legenda literal vale em mais de um lote (L4 = L4C = L5C; L6A = L6B): só *_gabarito.md de lote com o campo
        esperado = sorted(f'{l}_gabarito.md' for l, g in LEGENDAS.items() if g == leg)
        if onde != esperado: DIFFS.append(('(legenda)', lid, 'legenda fora do topo do gabarito do próprio lote', (onde, esperado)))
    for s in P['simulados']:
        for av in s.get('avisos', []):
            NCOMP['avisos não exibidos'] += 1
            fragmentos = [av[:40], av.split('\n')[0][-40:]]
            onde = [f for f, tx in todos.items() if any(fr in tx for fr in fragmentos)]
            if onde: DIFFS.append(('(avisos)', s['id'], 'aviso exibido na edição', onde))

    # ---- higiene: marcas em qualquer arquivo
    marca = re.compile(r'\[V\s|NORMATIVO — QA|\[TS\]|\b(?:CQFP|CQE|CPP|GCE|GCB|GBQ|EXEC)\b|\bF\d{1,2}\b|\b[TREO]-\d+\b|\(errata E\d+\)')
    restos = []
    for f in sorted(files):
        for k, ln in enumerate(rd(os.path.join(dir_est, f)), 1):
            for m in marca.finditer(ln):
                restos.append((f, k, m.group(0), ln[max(0, m.start() - 40):m.end() + 40]))
    return P, restos

def check_itens(arq, parsed, its):
    NCOMP['estrutura'] += 1
    if [x['id'] for x in parsed] != [i['id'] for i in its]: DIFFS.append((arq, 'ids', 'ordem/quantidade', (len(parsed), len(its))))
    for x, it in zip(parsed, its):
        for key in ('comando', 'textoBase', 'enunciado'):
            cmp_text(arq, f'{it["id"]}.{key}', x[key], it[key], regras=False, cat='prova/metadado')
        NCOMP['aviso/nota'] += 1
        if x['aviso'] != bool(it.get('volatil')): DIFFS.append((arq, it['id'], 'aviso VOLÁTIL', (x['aviso'], it.get('volatil'))))
    # sem gabarito nem justificativa
    txt = open(os.path.join(DIR, arq), encoding='utf-8').read()
    NCOMP['estrutura'] += 1
    if re.search(r'Gabarito:|Justificativa:|Item do edital', txt.split('\n', 4)[-1]): DIFFS.append((arq, '(arquivo)', 'tem gabarito/justificativa', ''))

def check_gab(arq, parsed, its, sim=False):
    NCOMP['estrutura'] += 1
    if [x['id'] for x in parsed] != [i['id'] for i in its]: DIFFS.append((arq, 'ids', 'ordem/quantidade', (len(parsed), len(its))))
    for k, (x, it) in enumerate(zip(parsed, its), 1):
        NCOMP['gabarito'] += 1
        if x['gabarito'] != it['gabarito']: DIFFS.append((arq, it['id'], 'gabarito', (x['gabarito'], it['gabarito'])))
        if sim and x['n'] != str(k): DIFFS.append((arq, it['id'], 'numeração', (x['n'], k)))
        NCOMP['metadado'] += 1
        if x['edital'] != it['itemEdital']: DIFFS.append((arq, it['id'], 'itemEdital', (x['edital'], it['itemEdital'])))
        if x['aderencia'] is not None and x['aderencia'] != it['aderencia']: DIFFS.append((arq, it['id'], 'aderencia', (x['aderencia'], it['aderencia'])))
        if it['justificativa']:
            cmp_text(arq, f'{it["id"]}.justificativa', x['justificativa'] or '', it['justificativa'])
        elif x['justificativa'] is not None: DIFFS.append((arq, it['id'], 'justificativa inesperada', ''))
        NCOMP['aviso/nota'] += 1
        if x['nota'] != nota_exib(it): DIFFS.append((arq, it['id'], 'nota', (x['nota'], nota_exib(it))))
        if x['aviso'] != bool(it.get('volatil')): DIFFS.append((arq, it['id'], 'aviso VOLÁTIL', (x['aviso'], it.get('volatil'))))

if __name__ == '__main__':
    pacote = sys.argv[1] if len(sys.argv) > 1 else gen.SRC
    DIR = sys.argv[2] if len(sys.argv) > 2 else gen.OUT
    P, restos = main(pacote, DIR)
    tot = sum(NCOMP.values())
    print(f'pacote: {pacote}\nestudante: {DIR}')
    print('comparações:', dict(NCOMP), '| total', tot)
    print('DIFERENÇAS:', len(DIFFS))
    for d in DIFFS[:40]: print('  ', d)
    print('exceções fechadas usadas: CAIXA (C-15) %d trocas; nota de BQ-0003 (C-18) %d exibições (%s)' % (len(CASE_LOG), len(NOTA_EXC), sorted(set(NOTA_EXC))))
    for c in CASE_LOG: print('   CAIXA', c)
    if len(CASE_LOG) != 8 or any(c[0] != 'L6A_estudo.md' for c in CASE_LOG) or len(NOTA_EXC) != 4:
        DIFFS.append(('(exceções)', 'CAIXA/nota', 'contagem inesperada', (len(CASE_LOG), len(NOTA_EXC))))
        print('DIFERENÇA: contagem de exceções inesperada')
    print('marcas residuais nos arquivos:', len(restos))
    for r in restos: print('  ', r)
    json.dump({'comparacoes': dict(NCOMP), 'total': tot, 'diferencas': len(DIFFS), 'detalhe': [list(map(str, d)) for d in DIFFS],
               'restos': [list(map(str, r)) for r in restos]},
              open(os.path.join(gen.HERE, 'out', 'estudante_fidelidade.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    sys.exit(1 if DIFFS else 0)
