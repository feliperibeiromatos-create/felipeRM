# -*- coding: utf-8 -*-
"""T-56 — conferências da ocorrência v1.3 do pacote e da edição do estudante (independentes do gerador).
Lê out/pacote.json e out/estudante/ (v1.3 gerada) e compara com a v1.2 canônica lida do git (refs.py: commit 2684ab1, SHA-256 f46ed9f8…).
(1) diff v1.2 -> v1.3 do pacote.json, restrito a: nome, geradoEm, legendaMecanismo (6 lotes) e avisos (SIM-0); qualquer outra diferença = falha.
(3) diff v1.2 -> v1.3 da edição: só L6B_estudo.md (N-1), topo dos 6 L<lote>_gabarito.md (legenda) e README (versão); fidelidade (0 diferenças,
    lida de out/estudante_fidelidade.json); varredura: 0 "Nesta produção", 0 "especificação previa".
(4) varreduras de não regressão da seção 3.5 de QA_T48_R2_2026-10-13_gbq-cqe.md e exceções fechadas da R1 (CAIXA C-05/C-15; reunião C-06 a C-08; C-13; C-18).
(5) contagens iguais às da v1.2.
Saída: out/conferencias_v13.txt e out/conferencias_v13.json; código de saída 1 se houver falha.
Uso: python3 conferencias_v13.py [<pacote.json> <pasta_estudante>]  (padrão: out/pacote.json e out/estudante)"""
import collections, difflib, hashlib, json, os, re, sys
import refs
import estudante_marcas as em
from common import OUT

PAC = sys.argv[1] if len(sys.argv) > 2 else os.path.join(OUT, 'pacote.json')
EST = sys.argv[2] if len(sys.argv) > 2 else os.path.join(OUT, 'estudante')

raw13 = open(PAC, 'rb').read()
P13 = json.loads(raw13.decode('utf-8'))
raw12 = refs.git_show(refs.C_V12, refs.PACOTE)
P12 = json.loads(raw12.decode('utf-8'))
E12 = refs.estudante(refs.C_V12)
E13 = {f: open(os.path.join(EST, f), encoding='utf-8').read() for f in sorted(os.listdir(EST))}

res = []
def chk(c, alvo, ok, detalhe=''):
    res.append((c, alvo, bool(ok), detalhe))
    print(('OK    ' if ok else 'FALHA ') + c + ' | ' + alvo + (' | ' + detalhe if detalhe else ''))

chk('BASE', 'v1.2 (git %s) tem SHA-256 f46ed9f8e43db76aaeb96eda0b2924028fb7145c048c5eb0189396c9f67304fe e a edição v1.2 tem 43 arquivos' % refs.C_V12,
    hashlib.sha256(raw12).hexdigest() == 'f46ed9f8e43db76aaeb96eda0b2924028fb7145c048c5eb0189396c9f67304fe' and len(E12) == 43,
    'v1.2 %s | v1.3 %s' % (hashlib.sha256(raw12).hexdigest()[:12], hashlib.sha256(raw13).hexdigest()[:12]))

# ======================================================================= (1) diff do pacote
def walk_diff(a, b, path, out):
    if type(a) != type(b):
        out.append((path, 'tipo', a, b)); return
    if isinstance(a, dict):
        for k in a:
            if k not in b: out.append((path + '.' + k, 'removido', a[k], None))
            else: walk_diff(a[k], b[k], path + '.' + k, out)
        for k in b:
            if k not in a: out.append((path + '.' + k, 'acrescentado', None, b[k]))
    elif isinstance(a, list):
        if len(a) != len(b): out.append((path, 'tamanho', len(a), len(b))); return
        for i, (x, y) in enumerate(zip(a, b)): walk_diff(x, y, '%s[%d]' % (path, i), out)
    elif a != b:
        out.append((path, 'valor', a, b))
dif = []
walk_diff(P12, P13, '', dif)
# identifica cada diferença por caminho com ids: lotes[i] -> id, simulados[i] -> id
def nome_caminho(p):
    m = re.match(r'^\.(lotes|simulados)\[(\d+)\](.*)$', p)
    if m: return '%s[%s]%s' % (m.group(1), P13[m.group(1)][int(m.group(2))]['id'], m.group(3))
    return p
dif_n = sorted((nome_caminho(d[0]), d[1]) for d in dif)
esperado_lotes = sorted(('lotes[%s].legendaMecanismo' % l, 'acrescentado') for l in ('L4', 'L4C', 'L5', 'L5C', 'L6A', 'L6B'))
esperado = sorted([('.nome', 'valor'), ('simulados[SIM-0].avisos', 'acrescentado')] + esperado_lotes)
chk('(1) DIFF', 'v1.2 -> v1.3 do pacote: só nome (valor), legendaMecanismo em 6 lotes e avisos no SIM-0 (acrescentados); geradoEm igual (2026-10-13)', dif_n == esperado and P12['geradoEm'] == P13['geradoEm'] == '2026-10-13',
    'diferenças: %d (%s)' % (len(dif_n), '; '.join('%s %s' % x for x in dif_n)))
nome_d = [d for d in dif if d[0] == '.nome'][0]
chk('(1) DIFF', 'nome: "%s" -> "%s"; versao 1 nas duas' % (nome_d[2], nome_d[3]), nome_d[2] == 'Câmara 2026 — pacote F4 (v1.2)' and nome_d[3] == 'Câmara 2026 — pacote F4 (v1.3)' and P12['versao'] == P13['versao'] == 1)
# o que não é campo novo permanece idêntico, inclusive a ordem de chaves
def sem_novos(P):
    q = json.loads(json.dumps(P))
    q['nome'] = ''
    for l in q['lotes']: l.pop('legendaMecanismo', None)
    for s in q['simulados']: s.pop('avisos', None)
    return q
chk('(1) DIFF', 'sem os campos novos e o nome, v1.3 = v1.2 estruturalmente (itens, edital, pegadinhas, pares, cursos, resumos, discursivas, simulados)', sem_novos(P12) == sem_novos(P13))
def ordem_chaves(P):
    return [list(P.keys())] + [list(i.keys()) for i in P['itens']] + [list(l.keys()) for l in P['lotes']] + [list(s.keys()) for s in P['simulados']] + [list(d.keys()) for d in P['discursivas']]
oc12 = ordem_chaves(P12); oc13 = ordem_chaves(P13)
chk('(1) DIFF', 'ordem das chaves: as mesmas, salvo legendaMecanismo (última chave do lote) e avisos (última chave do SIM-0)',
    len(oc12) == len(oc13) and all(a == [k for k in b if k not in ('legendaMecanismo', 'avisos')] for a, b in zip(oc12, oc13)) and all((b[-1] in ('legendaMecanismo', 'avisos')) for a, b in zip(oc12, oc13) if a != b))
chk('(1) DIFF', 'serialização: indent=1, ensure_ascii=False, newline final; sem campo vazio nem null nos campos novos', json.dumps(P13, ensure_ascii=False, indent=1) + '\n' == raw13.decode('utf-8')
    and all(isinstance(l['legendaMecanismo'], str) and l['legendaMecanismo'] for l in P13['lotes'] if 'legendaMecanismo' in l) and all(a for s in P13['simulados'] for a in s.get('avisos', [])))

# ======================================================================= (3) diff da edição
chk('(3) EDIÇÃO', 'mesmos 43 nomes de arquivo', sorted(E12) == sorted(E13) and len(E13) == 43)
mudados = sorted(f for f in E13 if E12[f] != E13[f])
esp_m = sorted(['L6B_estudo.md', 'README.md'] + ['%s_gabarito.md' % l for l in ('L4', 'L4C', 'L5', 'L5C', 'L6A', 'L6B')])
chk('(3) EDIÇÃO', 'arquivos que mudam da v1.2 para a v1.3: exatamente 8 (L6B_estudo.md, README.md e os 6 L<lote>_gabarito.md com legenda); os outros 35 idênticos', mudados == esp_m, str(mudados))
# L6B_estudo: duas deleções puras em uma linha
a = E12['L6B_estudo.md'].split('\n'); b = E13['L6B_estudo.md'].split('\n')
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
ops = [o for o in sm.get_opcodes() if o[0] != 'equal']
ok6 = len(a) == len(b) and len(ops) == 1 and ops[0][0] == 'replace' and ops[0][2] - ops[0][1] == 1 and ops[0][4] - ops[0][3] == 1 and ops[0][1] == 142
if ok6:
    x, y = a[142], b[142]
    D1_, D2_ = 'Nesta produção ', ' (a especificação previa o item "se houver base")'
    # só deleção (o difflib pode alinhar o "N" de "Nesta" com o de "NÃO"; por isso se confere pela remoção exata dos dois trechos)
    o2 = [o for o in difflib.SequenceMatcher(None, x, y, autojunk=False).get_opcodes() if o[0] != 'equal']
    ok6 = all(o[0] == 'delete' for o in o2) and x.count(D1_) == 1 and x.count(D2_) == 1 and x.replace(D1_, '', 1).replace(D2_, '', 1) == y
    det6 = 'apagado: %s e %s (%d caracteres)' % (repr(D1_), repr(D2_), len(x) - len(y))
    fim = y.endswith('conscientização dos usuários). NÃO foi aberta fonte institucional que defina o termo, e o edital não o detalha; por isso, NÃO HÁ ITEM sobre governança digital neste lote.')
    ok6 = ok6 and fim
else:
    det6 = str(ops)[:200]
chk('(3) EDIÇÃO', 'N-1: L6B_estudo.md muda só na linha 143, por duas deleções puras ("Nesta produção " e " (a especificação previa o item \\"se houver base\\")"); resultado = "NÃO foi aberta fonte institucional que defina o termo, e o edital não o detalha; por isso, NÃO HÁ ITEM sobre governança digital neste lote."', ok6, det6)
# gabaritos: inserção das 2 linhas da legenda logo depois do título
okg = True; detg = []
for l in P13['lotes']:
    f = '%s_gabarito.md' % l['id']
    if 'legendaMecanismo' not in l: okg &= E12[f] == E13[f]; continue
    a = E12[f].split('\n'); b = E13[f].split('\n')
    ok = a[0] == '# %s — gabarito e justificativas' % l['nome'] and a[1] == '' and a[2].startswith('### ') and b == a[:2] + [l['legendaMecanismo'], ''] + a[2:]
    okg &= ok; detg.append('%s %s' % (l['id'], 'ok' if ok else 'FALHA'))
chk('(3) EDIÇÃO', 'legenda: nos 6 L<lote>_gabarito.md é a única diferença (inserção de 2 linhas após o título: legenda literal e linha em branco, antes do primeiro item); L1, L1C, L2, L3 idênticos', okg, ', '.join(detg))
leg_fora = [f for f, tx in E13.items() if any(l['legendaMecanismo'] in tx for l in P13['lotes'] if 'legendaMecanismo' in l) and not re.match(r'^L(4|4C|5|5C|6A|6B)_gabarito\.md$', f)]
chk('(3) EDIÇÃO', 'legenda exibida só no topo dos L<lote>_gabarito.md desses lotes: 0 ocorrência em SIM-*_gabarito.md, BANCO_gabarito.md, *_estudo.md, *_itens.md, *_folha.md, README.md', not leg_fora, str(leg_fora))
a = E12['README.md'].split('\n'); b = E13['README.md'].split('\n')
o = [x for x in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if x[0] != 'equal']
chk('(3) EDIÇÃO', 'README: só a linha de versão ("v1.2" -> "v1.3"); data e demais linhas iguais', len(a) == len(b) and len(o) == 1 and a[o[0][1]] == '- Versão: v1.2 (pacote.json versão 1)' and b[o[0][3]] == '- Versão: v1.3 (pacote.json versão 1)')
avs = [a for s in P13['simulados'] for a in s.get('avisos', [])]
exib = [f for f, tx in E13.items() if any(fr in tx for av in avs for fr in (av[:40], av.split('\n')[0][-40:]))]
chk('(3) EDIÇÃO', 'avisos do SIM-0 não exibidos na edição (0 arquivo com o texto dos 3 avisos; SIM-0_folha.md e SIM-0_gabarito.md iguais aos da v1.2)', not exib and E12['SIM-0_folha.md'] == E13['SIM-0_folha.md'] and E12['SIM-0_gabarito.md'] == E13['SIM-0_gabarito.md'], str(exib))
fid = json.load(open(os.path.join(OUT, 'estudante_fidelidade.json'), encoding='utf-8'))
chk('(3) EDIÇÃO', 'fidelidade (estudante_fidelidade.py): 0 diferenças', fid['diferencas'] == 0 and fid['total'] > 0, 'comparações %d, diferenças %d, marcas residuais %d' % (fid['total'], fid['diferencas'], len(fid['restos'])))
n1 = sum(tx.count('Nesta produção') + tx.count('nesta produção') for tx in E13.values()); n2 = sum(tx.lower().count('especificação previa') for tx in E13.values())
chk('(3) EDIÇÃO', 'varredura nos 43 arquivos: 0 "Nesta produção" e 0 "especificação previa"', n1 == 0 and n2 == 0, '"Nesta produção" %d; "especificação previa" %d' % (n1, n2))
v12_n1 = sum(tx.count('Nesta produção') for tx in E12.values()); v12_n2 = sum(tx.count('especificação previa') for tx in E12.values())
chk('(3) EDIÇÃO', 'controle: a v1.2 tinha 1 e 1 (a varredura enxerga o que deve enxergar); no pacote v1.3 a marca fica (D-PACOTE-V11): 1 e 1', (v12_n1, v12_n2) == (1, 1) and sum(l['curso'].count('Nesta produção') for l in P13['lotes']) == 1 and sum(l['curso'].count('especificação previa') for l in P13['lotes']) == 1, 'v1.2 %d/%d' % (v12_n1, v12_n2))
conta = json.load(open(os.path.join(OUT, 'estudante_contagem.json'), encoding='utf-8'))
chk('(3) EDIÇÃO', 'remoções por deleção da edição: 569 (v1.2) + 2 da N-1 = 571; a regra literal da N-1 ocorre 2 vezes', sum(conta['total'].values()) == 571 and conta['total'].get('marca de processo de produção do lote ("Nesta produção" / "a especificação previa")') == 2, str(sum(conta['total'].values())))

# ======================================================================= (4) varreduras de não regressão (seção 3.5 do QA R2) e exceções fechadas da R1
def cre(rx, prefixos=None, F=E13, flags=re.M):
    r = re.compile(rx, flags)
    return sum(len(r.findall(tx)) for f, tx in F.items() if prefixos is None or f.startswith(tuple(prefixos)))
folhas = [f for f in E13 if f.endswith('_folha.md')]
V0 = [(r';\)', None), (r' — $', None), (r'\*\*\*\*', None), (r'abertas? hoje', None), (r'\(v2,', None), (r'D-LEI-15352', None), (r'neste chat', None), (r'Retificação', None),
      (r'Gabarito [CE] mantido', None), (r'\b(?:U[1-6]|GG\d|TB\d|CI)\b', None), (r'\bN\d\b', ('L1_', 'L1C_', 'L2_', 'L3_', 'SIM-2', 'SIM-0-P2')),
      (r' — (?:BQ|L\d|4C|5C|6A|6B|A5)', tuple(folhas)), (r'erificado em 8/10/2026', ('L5_', 'L5C_'))]
for rx, fl in V0:
    n = cre(rx, fl)
    chk('(4) VARR 3.5', '%s%s: 0' % (rx, ' em ' + ','.join(fl) if fl and len(fl) < 8 else (' nas folhas' if fl else '')), n == 0, str(n))
VX = [r'\[TS\]', r'\[V ', r'\bCQFP\b', r'\bCQE\b', r'\bGCE\b', r'\bGCB\b', r'\bGBQ\b', r'\bCPP\b', r'T-\d', r'\bQA\b', r'O-\d', r'Lição O', r'R-\dC\d', r'NÃO VOLÁTIL', r'não VOLÁTIL', r'Sem marca VOLÁTIL', r'REVERIFICAR', r'\bD-[A-Z]{2,}']
for rx in VX:
    n = cre(rx)
    chk('(4) VARR 3.5 extra', '%s: 0' % rx, n == 0, str(n))
# `D-[A-Z]{2,}` sem \b casa dentro de nomes ("TID-IA", "TID-DADOS-VIZ" nos títulos dos lotes, "END-TO-END"): mesma contagem da v1.2, nenhum id de decisão
sem_b13 = cre(r'D-[A-Z]{2,}'); sem_b12 = cre(r'D-[A-Z]{2,}', None, E12)
chk('(4) VARR 3.5 extra', 'D-[A-Z]{2,} (sem \\b): mesma contagem da v1.2 (só "TID-IA", "TID-DADOS-VIZ", "END-TO-END"); com \\b: 0', sem_b13 == sem_b12 and cre(r'\bD-[A-Z]{2,}', None, E12) == 0, 'v1.2 %d; v1.3 %d' % (sem_b12, sem_b13))
codF = sorted((f, k) for f, tx in E13.items() for k, l in enumerate(tx.split('\n'), 1) if re.search(r'\bF\d{1,2}\b', l))
chk('(4) VARR 3.5', 'códigos F: só L6A_estudo.md:83 ("a tecla F4") e L4_gabarito.md:56/58 (L4-11, "O F4 afirma")', len(codF) == 2 and codF[0][0] == 'L4_gabarito.md' and codF[1] == ('L6A_estudo.md', 83) and 'O F4 afirma' in E13['L4_gabarito.md'].split('\n')[codF[0][1] - 1] and 'tecla F4' in E13['L6A_estudo.md'].split('\n')[82], str(codF))
AV = 'Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.'
volx = sorted((f, k) for f, tx in E13.items() for k, l in enumerate(tx.split('\n'), 1) if 'VOLÁTIL' in l and AV not in l)
volx12 = sorted((f, k) for f, tx in E12.items() for k, l in enumerate(tx.split('\n'), 1) if 'VOLÁTIL' in l and AV not in l)
chk('(4) VARR 3.5', '"VOLÁTIL" fora do aviso fixo: só L4_estudo 23 e 210; L5_estudo 24, 104 e 107; L6A_estudo 125 e 268 (em v1.2 igual); os gabaritos com legenda não ganham a palavra', volx == sorted([('L4_estudo.md', 23), ('L4_estudo.md', 210), ('L5_estudo.md', 24), ('L5_estudo.md', 104), ('L5_estudo.md', 107), ('L6A_estudo.md', 125), ('L6A_estudo.md', 268)]) and volx == volx12, str(volx))
json.dump({'volatil_fora_do_aviso': volx}, open(os.path.join(OUT, 'varredura_volatil_v13.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# exceções fechadas da R1
S13 = []
def strings(o):
    if isinstance(o, str): yield o
    elif isinstance(o, dict):
        for v in o.values(): yield from strings(v)
    elif isinstance(o, list):
        for v in o: yield from strings(v)
S13 = list(strings(P13))
def cp(t): return sum(s.count(t) for s in S13)
def ce(t, pref=None): return sum(tx.count(t) for f, tx in E13.items() if pref is None or f.startswith(tuple(pref)))
# CAIXA C-05 (pacote e edição) e C-15 (edição)
it = {i['id']: i for i in P13['itens']}
c05 = [('4C-08', '(conceito geral, sem fonte de fornecedor, como no curso). O item não depende', '(conceito geral, sem fonte de fornecedor, como no curso). o item não depende'),
       ('5C-06', 'termine no mínimo da amostra. A regra de 1,5 · AIQ', 'termine no mínimo da amostra. a regra de 1,5 · AIQ')]
for iid, novo, antigo in c05:
    j = it[iid]['justificativa']
    ocorr = 1 + sum(1 for s in P13['simulados'] if iid in s['itens'])
    chk('(4) CAIXA C-05', '%s: pacote com inicial maiúscula (1 vez), sem a minúscula; edição: %d ocorrências (gabarito do lote + simulados), 0 da minúscula' % (iid, ocorr), j.count(novo) == 1 and j.count(antigo) == 0 and ce(novo) == ocorr and ce(antigo) == 0, 'edição %d' % ce(novo))
for esc, antes, depois in em.CAIXA:
    chk('(4) CAIXA C-15', 'L6A_estudo: "%s" -> "%s": antes 0, depois 1' % (antes[:34], depois[:34]), ce(antes, (esc,)) == 0 and ce(depois, (esc,)) == 1 and len(antes) == len(depois) and sum(x != y for x, y in zip(antes, depois)) == 1)
chk('(4) CAIXA C-15', 'lista CAIXA: 8 pares, todos em L6A_estudo; 8 trocas na regeração', len(em.CAIXA) == 8 and all(c[0] == 'L6A_estudo' for c in em.CAIXA) and conta['total'].get('caixa (minúscula → maiúscula na inicial deixada por deleção)') == 8)
# reunião C-06 a C-08
def peg(P, lid, rot): return [g['texto'] for l in P['lotes'] if l['id'] == lid for g in l['pegadinhas'] if g['rotulo'] == rot]
e15 = peg(P13, 'L1', 'Pontuação automática e capitalização em transcrições')
b1 = peg(P13, 'L5', 'Gráfico de barras (colunas)'); b2 = peg(P13, 'L5', 'Box plot (diagrama de caixa)')
chk('(4) REUNIÃO C-06', 'L1 P2-1.5: 1 entrada, com os dois fragmentos unidos por "; " (a de "\\"Câmara\\" (instituição) vs …" não é entrada própria)', len(e15) == 1 and '"Câmara" (instituição) vs "câmara" (sala)' in e15[0] and e15 == peg(P12, 'L1', 'Pontuação automática e capitalização em transcrições'))
chk('(4) REUNIÃO C-07', 'L5 Gráfico de barras (colunas): 3 entradas (confundir com histograma; aceitar eixo truncado; reunida "usar para distribuição…; empilhado quando…")', len(b1) == 3 and 'usar para distribuição de variável contínua agrupada em classes; empilhado quando se quer comparar as partes entre si.' in b1 and 'confundir com histograma' in b1 and 'aceitar eixo truncado' in b1)
chk('(4) REUNIÃO C-08', 'L5 Box plot (diagrama de caixa): 1 entrada com os 4 fragmentos unidos por "; "', len(b2) == 1 and b2[0].startswith('dizer que a linha central é a média; que a caixa vai do mínimo ao máximo') and b2[0].endswith('que mostra frequência por intervalo (isso é histograma).'))
npg = {l['id']: len(l['pegadinhas']) for l in P13['lotes']}
chk('(4) REUNIÃO', 'pegadinhas por lote = v1.2 (L1 19, L1C 4, L2 43, L3 42, L4 32, L4C 0, L5 48, L5C 0, L6A 35, L6B 39; total 262)', npg == {'L1': 19, 'L1C': 4, 'L2': 43, 'L3': 42, 'L4': 32, 'L4C': 0, 'L5': 48, 'L5C': 0, 'L6A': 35, 'L6B': 39} and sum(npg.values()) == 262)
l1e = E13['L1_estudo.md']; l5e = E13['L5_estudo.md']
chk('(4) REUNIÃO', 'edição: L1_estudo com 1 linha para P2-1.5 "Pontuação automática…"; L5_estudo com 3 linhas "Gráfico de barras (colunas)" e 1 "Box plot (diagrama de caixa)"',
    sum(1 for l in l1e.split('\n') if l.startswith('- [P2-1.5] **Pontuação automática e capitalização em transcrições**')) == 1 and sum(1 for l in l5e.split('\n') if l.startswith('- [P1-8.2] **Gráfico de barras (colunas)**')) == 3 and sum(1 for l in l5e.split('\n') if l.startswith('- [P1-8.2] **Box plot (diagrama de caixa)**')) == 1)
# C-13: L4-11
j = it['L4-11']['justificativa']; ed = [l for l in E13['L4_gabarito.md'].split('\n') if l.startswith('- Justificativa: ') and 'O F4 afirma que "generative models are initially trained using an unsupervised approach"' in l]
chk('(4) C-13', 'L4-11: justificativa da edição = a do pacote menos exatamente " Fonte: F4, reverificado em 7/10/2026." (1 ocorrência no pacote); frase que fundamenta o gabarito C presente; gabarito C',
    len(ed) == 1 and j.count(' Fonte: F4, reverificado em 7/10/2026.') == 1 and ed[0] == '- Justificativa: ' + j.replace(' Fonte: F4, reverificado em 7/10/2026.', '') and it['L4-11']['gabarito'] == 'C' and 'L4-11' not in [x for s in P13['simulados'] for x in s['itens']])
# C-18: nota de BQ-0003
n3 = it['BQ-0003']['nota']
chk('(4) C-18', 'BQ-0003: `nota` no pacote com " (D-LEI-15352)" literal; na edição, sem ele, nos 4 pontos (BANCO_itens, BANCO_gabarito, SIM-0_folha, SIM-0_gabarito); BQ-0040 sem o identificador',
    n3.count(' (D-LEI-15352)') == 1 and ce(n3.replace(' (D-LEI-15352)', '')) == 4 and ce('D-LEI-15352') == 0 and all(ce(n3.replace(' (D-LEI-15352)', ''), (f,)) == 1 for f in ('BANCO_itens', 'BANCO_gabarito', 'SIM-0_folha', 'SIM-0_gabarito')) and '(D-' not in it['BQ-0040']['nota'])
# C-10 / C-11 (folhas sem id; texto-base antes do comando)
rxid = r'^\*\*[^\s*]+\*\* — (?:BQ|L\d|4C|5C|6A|6B|A5)'
chk('(4) C-10', 'folhas: 165 linhas de item sem id de origem; 0 com id (id só no *_gabarito.md)', cre(r'^\*\*\d+\*\* — ', tuple(folhas)) == 165 and cre(r'^\*\*(?:BQ-|L\d|4C-|5C-|6A-|6B-|A5-)\S*\*\*', tuple(folhas)) == 0)
def tb_antes(tx):
    nb = [l for l in tx.split('\n') if l.strip()]
    return (sum(1 for k in range(len(nb) - 1) if nb[k].startswith('**Texto-base.**') and nb[k + 1].startswith('**Comando.**')), sum(1 for k in range(len(nb) - 1) if nb[k].startswith('**Comando.**') and nb[k + 1].startswith('**Texto-base.**')))
chk('(4) C-11', 'texto-base antes do comando: BANCO_itens 3 e SIM-0_folha 1; 0 comando antes de texto-base', tb_antes(E13['BANCO_itens.md']) == (3, 0) and tb_antes(E13['SIM-0_folha.md']) == (1, 0) and sum(tb_antes(tx)[1] for tx in E13.values()) == 0)

# ======================================================================= (5) contagens iguais às da v1.2
def cnt(P):
    it_ = P['itens']
    c = collections.OrderedDict()
    c['itens'] = len(it_); c['ids únicos'] = len({i['id'] for i in it_})
    c['C'] = sum(i['gabarito'] == 'C' for i in it_); c['E'] = sum(i['gabarito'] == 'E' for i in it_)
    c['banco'] = sum(i['rotulo'] != 'AUTORAL' for i in it_); c['AUTORAL'] = sum(i['rotulo'] == 'AUTORAL' for i in it_)
    c['aderência direta'] = sum(i['aderencia'] == 'direta' for i in it_); c['aderência parcial'] = sum(i['aderencia'] == 'parcial' for i in it_)
    c['volatil'] = sum(bool(i.get('volatil')) for i in it_); c['nota'] = sum('nota' in i for i in it_); c['comandoOriginal'] = sum('comandoOriginal' in i for i in it_)
    c['pegadinhas'] = sum(len(l['pegadinhas']) for l in P['lotes']); c['pares'] = sum(len(l['pares']) for l in P['lotes'])
    c['simulados n'] = [s['n'] for s in P['simulados']]; c['simulados itens'] = [len(s['itens']) for s in P['simulados']]
    c['lotes'] = len(P['lotes']); c['discursivas'] = len(P['discursivas']); c['edital'] = len(P['edital'])
    c['aspectos'] = sum(len(d['aspectos']) for d in P['discursivas']); c['quesitos'] = sum(len(d['quesitos']) for d in P['discursivas'])
    return c
c12 = cnt(P12); c13 = cnt(P13)
ESP = collections.OrderedDict([('itens', 286), ('ids únicos', 286), ('C', 149), ('E', 137), ('banco', 106), ('AUTORAL', 180), ('aderência direta', 247), ('aderência parcial', 39), ('volatil', 23), ('nota', 2),
                               ('comandoOriginal', 90), ('pegadinhas', 262), ('simulados n', [60, 40, 40, 25]), ('simulados itens', [60, 40, 40, 25]), ('lotes', 10), ('discursivas', 5), ('edital', 47)])
for k, v in ESP.items():
    chk('(5) CONT', '%s = %s (v1.2: %s; v1.3: %s)' % (k, v, c12[k], c13[k]), c13[k] == v == c12[k])
chk('(5) CONT', 'pares, aspectos e quesitos das discursivas iguais à v1.2', c13['pares'] == c12['pares'] and c13['aspectos'] == c12['aspectos'] and c13['quesitos'] == c12['quesitos'], '%s/%s/%s' % (c13['pares'], c13['aspectos'], c13['quesitos']))
cs = collections.Counter(i['gabarito'] for s in P13['simulados'] if s['id'] in ('SIM-1', 'SIM-2') for x in s['itens'] for i in [it[x]])
chk('(5) CONT', 'SIM-0 33 C/27 E (diagnóstico, 23 parciais, 4 voláteis); SIM-1 e SIM-2 20 C/20 E; SIM-0-P2 13 C/12 E', [tuple(collections.Counter(it[x]['gabarito'] for x in s['itens']).get(g, 0) for g in 'CE') for s in P13['simulados']] == [(33, 27), (20, 20), (20, 20), (13, 12)])
chk('(5) CONT', 'edição: 43 arquivos; itens por lote e por simulado iguais aos da v1.2', len(E13) == 43 and [c for c in c13['simulados itens']] == [60, 40, 40, 25])

fails = [r for r in res if not r[2]]
print('\n%d conferências; %d falhas' % (len(res), len(fails)))
with open(os.path.join(OUT, 'conferencias_v13.txt'), 'w', encoding='utf-8') as f:
    for c, alvo, ok, det in res:
        f.write(('OK    ' if ok else 'FALHA ') + c + ' | ' + alvo + (' | ' + det if det else '') + '\n')
    f.write('\n%d conferências; %d falhas\n' % (len(res), len(fails)))
json.dump([list(r) for r in res], open(os.path.join(OUT, 'conferencias_v13.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
sys.exit(1 if fails else 0)
