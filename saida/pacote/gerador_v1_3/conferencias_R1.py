# -*- coding: utf-8 -*-
"""Conferências da correção R1 (T-48), independentes do gerador.
(1) cada C-xx: texto atual (R0) existe no nº previsto; no R1 não existe mais; texto novo existe no nº previsto.
(2) diff R0 -> R1 do pacote.json restrito aos campos/ids da lista.
(5) contagens.  (6) varredura de marcas residuais na edição do estudante.
SCRIPT HISTÓRICO da correção R1 da T-48 (comparação R0 -> R1; não é o validador da v1.3).
Uso: python3 conferencias_R1.py [<R0_dir> <R1_pacote.json> <R1_estudante_dir>]
Sem argumentos: R0 = git 27e594d e R1 = git 2684ab1 (pacote.json e saida/estudante/), materializados em pasta temporária
(T-56, ponto 2 da T-55: reproduzível a partir do git, sem pastas soltas).  Saídas em out/ (conferencias_R1.json, varredura_volatil.json)."""
import json, os, re, sys, collections, difflib, glob, tempfile
import refs
from common import OUT

if len(sys.argv) >= 4:
    R0 = sys.argv[1]; PR1 = sys.argv[2]; ER1 = sys.argv[3]
else:
    _tmp = tempfile.mkdtemp(prefix='conf_R1_')
    R0 = refs.materializa(refs.C_R0, os.path.join(_tmp, 'R0'))
    _r1 = refs.materializa(refs.C_V12, os.path.join(_tmp, 'R1'))
    PR1 = os.path.join(_r1, 'pacote.json'); ER1 = os.path.join(_r1, 'estudante')
P0 = json.load(open(os.path.join(R0, 'pacote.json'), encoding='utf-8'))
P1 = json.load(open(PR1, encoding='utf-8'))
E0 = os.path.join(R0, 'estudante')

def strings(o, acc):
    if isinstance(o, str): acc.append(o)
    elif isinstance(o, dict):
        for v in o.values(): strings(v, acc)
    elif isinstance(o, list):
        for v in o: strings(v, acc)
    return acc
S0 = strings(P0, []); S1 = strings(P1, [])
def cp(S, t): return sum(s.count(t) for s in S)
def edic(d):
    return {f: open(os.path.join(d, f), encoding='utf-8').read() for f in sorted(os.listdir(d))}
F0 = edic(E0); F1 = edic(ER1)
def ce(F, t, files=None):
    return sum(txt.count(t) for f, txt in F.items() if files is None or f.startswith(files))
def cre(F, rx, files=None, flags=re.M):
    r = re.compile(rx, flags)
    return sum(len(r.findall(txt)) for f, txt in F.items() if files is None or f.startswith(files))

res = []
def chk(c, alvo, ok, detalhe=''):
    res.append((c, alvo, bool(ok), detalhe)); print(('OK    ' if ok else 'FALHA ') + c + ' | ' + alvo + (' | ' + detalhe if detalhe else ''))

itens1 = {i['id']: i for i in P1['itens']}
def occ(iid):
    """ocorrências da justificativa de um item AUTORAL na edição: 1 no *_gabarito do lote + 1 por simulado que o inclui"""
    return 1 + sum(1 for s in P1['simulados'] if iid in s['itens'])

# ---- literais: (C, alvo, onde 'P'/'E', atual, novo, a0, n0, n1, [files])
LIT = []
def L(c, alvo, onde, atual, novo, a0, n0, n1, files=None): LIT.append((c, alvo, onde, atual, novo, a0, n0, n1, files))

RET = ' Retificação 6-A: a redação "sem acesso a busca" não excluía outras ferramentas; "ferramentas externas (como a busca)" alinha o item ao curso 5.3.3 ("sem ferramentas ou RAG").'
L('C-01', 'pacote 4C-09 justificativa', 'P', RET, 'como contexto. O acréscimo "e sem retreinamento"', 1, 0, 1)
L('C-01', 'edição 4C-09 (L4C_gabarito + simulados)', 'E', RET, 'como contexto. O acréscimo "e sem retreinamento"', occ('4C-09'), 0, occ('4C-09'))
L('C-02', 'pacote 6B-06 justificativa', 'P', ', conferida pela QA em 08/10/2026', '(seção ITENS REAIS).', 1, 0, 1)
L('C-02', 'edição 6B-06 (já limpa na R0)', 'E', ', conferida pela QA em 08/10/2026', 'com outro ponto de julgamento (seção ITENS REAIS).', 0, occ('6B-06'), occ('6B-06'))
L('C-03', 'pacote 6B-15 justificativa', 'P', ' (corrigido pela O-3)', 'marcar E). Curso 4.3.4: HTTPS é o HTTP', 1, 0, 1)
L('C-03', 'edição 6B-15 (já limpa na R0)', 'E', ' (corrigido pela O-3)', 'marcar E). Curso 4.3.4: HTTPS é o HTTP', 0, occ('6B-15'), occ('6B-15'))
L('C-04', 'pacote L2-Q21 justificativa', 'P', ' Gabarito E mantido.', 'traduz as notas estenotípicas em texto [F7].', 1, 0, 1)
L('C-04', 'edição L2-Q21', 'E', ' Gabarito E mantido.', 'o CAT do edital é transcrição assistida, que na taquigrafia traduz as notas estenotípicas em texto.', occ('L2-Q21'), 0, occ('L2-Q21'))
# no pacote R0 a marca "Lição O10: " já tinha sido apagada (F4), deixando a inicial minúscula: esse é o "atual" do pacote R0
L('C-05', 'pacote 4C-08 justificativa (R0: "... curso). o item"; fonte: "Lição O10: o item")', 'P', '(conceito geral, sem fonte de fornecedor, como no curso). o item não depende', '(conceito geral, sem fonte de fornecedor, como no curso). O item não depende', 1, 0, 1)
L('C-05', 'pacote 5C-06 justificativa (R0: "... amostra. a regra"; fonte: "Lição O10: a regra")', 'P', 'termine no mínimo da amostra. a regra de 1,5 · AIQ', 'termine no mínimo da amostra. A regra de 1,5 · AIQ', 1, 0, 1)
L('C-05', 'edição 4C-08 (inicial maiúscula)', 'E', '(conceito geral, sem fonte de fornecedor, como no curso). o item não depende', '(conceito geral, sem fonte de fornecedor, como no curso). O item não depende', occ('4C-08'), 0, occ('4C-08'))
L('C-05', 'edição 5C-06 (inicial maiúscula)', 'E', 'termine no mínimo da amostra. a regra de 1,5 · AIQ', 'termine no mínimo da amostra. A regra de 1,5 · AIQ', occ('5C-06'), 0, occ('5C-06'))
L('C-12', 'L4_estudo 224 e 283 (";)")', 'E', 'foi vetado;)', 'foi vetado).', 2, 0, 2, ('L4_estudo',))
L('C-13', 'L4-11 restaurada (L4_gabarito)', 'E', '"prioritariamente supervisionado"). O item descreve o pré-treino', '"prioritariamente supervisionado"). O F4 afirma que "generative models are initially trained using an unsupervised approach" e que "the model is sometimes trained further using supervised or reinforcement learning"; o item descreve o pré-treino', occ('L4-11'), 0, occ('L4-11'))
L('C-16a', 'L6A 166 (frase sem sujeito)', 'E', 'portas e criptografia do Exchange Online; esses números são específicos de produto e NÃO são cobrados.', 'ficam no servidor).\n\n### 3.1.3', 1, 0, 1, ('L6A_estudo',))
L('C-16b', 'L6A 60 ("(diz …")', 'E', '(diz "não estão formatados como cabeçalhos"', '("não estão formatados como cabeçalhos"', 1, 0, 1, ('L6A_estudo',))
L('C-16c', 'L6A 135 ("e orienta …")', 'E', '(de edição para exibição ou o contrário) e orienta excluir o link e criar outro. As duas páginas', '(de edição para exibição ou o contrário). As duas páginas', 1, 0, 1, ('L6A_estudo',))
L('C-17', 'L1C 49', 'E', '(v2, item 1.4)', '(item 1.4)', 1, 0, 1, ('L1C_estudo',))
L('C-17', 'L1C 52', 'E', '(v2, exemplo parlamentar do 1.4)', '(exemplo parlamentar do 1.4)', 1, 0, 1, ('L1C_estudo',))
L('C-18', 'nota BQ-0003 na edição (4 arquivos)', 'E', 'redação da Lei 15.352/2026 (D-LEI-15352); texto do item mantido literal', 'redação da Lei 15.352/2026; texto do item mantido literal', 4, 0, 4)
CH = [('L6A_estudo', 'Nas páginas de suporte abertas hoje, a Microsoft', 'Nas páginas de suporte, a Microsoft'),
      ('L6A_estudo', '(conceito geral; sem fonte aberta hoje para detalhes; sem item)', '(conceito geral; sem item)'),
      ('L6B_estudo', '4.0.2 GOVERNANÇA DIGITAL (conceito geral; sem base aberta hoje)', '4.0.2 GOVERNANÇA DIGITAL (conceito geral)'),
      ('L6B_estudo', 'Fontes abertas hoje: "Faça backups', 'Fontes: "Faça backups'),
      ('L6B_estudo', 'uma fora do local), sem fonte aberta hoje e sem item.', 'uma fora do local), sem item.'),
      ('L6B_estudo', 'Definição de vírus aberta hoje: "programa', 'Definição de vírus: "programa'),
      ('L6B_estudo', 'Definição de ransomware aberta hoje: "Ransomware', 'Definição de ransomware: "Ransomware'),
      ('L6B_estudo', 'Definição aberta hoje: o phishing', 'Definição: o phishing'),
      ('L6B_gabarito', 'não foi confirmada em fonte aberta hoje; ver curso 4.1.1', 'não foi confirmada em fonte; ver curso 4.1.1')]
for f, a, n in CH: L('C-19', f + ': ' + a[:40], 'E', a, n, 1, 0, 1, (f,))
L('C-21', 'L2-Q23 (L2_gabarito + SIM-0-P2_gabarito)', 'E', 'Depende de padrão técnico estável, não de produto; NÃO VOLÁTIL.', 'Depende de padrão técnico estável, não de produto.', occ('L2-Q23'), 0, occ('L2-Q23'))
L('C-21', 'L3-Q21', 'E', 'passou a ser exercida por ela. REVERIFICAR (normativo) 04–08/01/2027; não VOLÁTIL.', 'passou a ser exercida por ela.', occ('L3-Q21'), 0, occ('L3-Q21'))
L('C-21', 'L4-05', 'E', '"Message formatting with Markdown and XML". Sem marca VOLÁTIL: o item afirma o conceito, não recurso de produto.', '"Message formatting with Markdown and XML".', occ('L4-05'), 0, occ('L4-05'))
L('C-23', 'L4_estudo 210', 'E', 'não verificada neste chat)', 'não verificada)', 1, 0, 1, ('L4_estudo',))
# C-22: códigos N (L2/L3) — (arquivo, atual, novo)
CN = [('L2_estudo', '2026 (N1). Convenção da Câmara', '2026. Convenção da Câmara'), ('L2_estudo', 'NÃO VERIFICADA (N2).', 'NÃO VERIFICADA.'),
      ('L2_estudo', '[Ver N5: definição de uso corrente; sem fonte oficial verificada.]', '[definição de uso corrente; sem fonte oficial verificada.]'),
      ('L2_estudo', 'Câmara (N2): mostra', 'Câmara: mostra'), ('L2_estudo', 'de 2026 (N1); o curso', 'de 2026; o curso'),
      ('L2_estudo', 'instituições (N2); dentro', 'instituições; dentro'), ('L2_estudo', 'verificado (N2). Ilustrativo', 'verificado. Ilustrativo'),
      ('L2_estudo', 'produto; ver N3):', 'produto):'),
      ('L3_estudo', '(N6: não cobrar\ndescrição de sistema real.)', '(não cobrar\ndescrição de sistema real.)'),
      ('L3_estudo', '(N6: não cobrar descrição de sistema real.)', '(não cobrar descrição de sistema real.)'),
      ('L3_estudo', 'verificado (N6); o', 'verificado; o'), ('L3_estudo', 'verificados\n   (N5). A banca', 'verificados. A banca'),
      ('L3_estudo', '(N4; não há texto legal', '(não há texto legal'), ('L3_estudo', 'verificada — N7):', 'verificada):')]
for f, a, n in CN:
    a0 = ce(F0, a, (f,))
    L('C-22', f + ': ' + a[:40].replace('\n', '\\n'), 'E', a, n, a0, 0, 1, (f,))
# C-24
L('C-24', 'par L3 "Confidencialidade…" (× **** — )', 'E', '- **Confidencialidade, integridade, disponibilidade** × **** — ', '- **Confidencialidade, integridade, disponibilidade**\n', 1, 0, 1, ('L3_estudo',))

for c, alvo, onde, atual, novo, a0, n0, n1, files in LIT:
    if onde == 'P':
        r0a, r1a, r0n, r1n = cp(S0, atual), cp(S1, atual), cp(S0, novo), cp(S1, novo)
    else:
        r0a, r1a, r0n, r1n = ce(F0, atual, files), ce(F1, atual, files), ce(F0, novo, files), ce(F1, novo, files)
    ok = (r0a == a0 and r1a == 0 and r1n == n1)
    chk(c, alvo, ok, 'atual: R0=%d (prev %d) R1=%d (prev 0) | novo: R0=%d R1=%d (prev %d)' % (r0a, a0, r1a, r0n, r1n, n1))

# C-05/C-15 CAIXA no L6A
CX = [('mesclar combina duas ou mais células', 'Mesclar combina duas ou mais células'), ('a função SE compara um valor', 'A função SE compara um valor'),
      ('o PROCV pesquisa um valor', 'O PROCV pesquisa um valor'), ('o propósito é fazer todos os slides', 'O propósito é fazer todos os slides'),
      ('a animação é aplicada a um único elemento', 'A animação é aplicada a um único elemento'), ('o histórico de versões permite ver', 'O histórico de versões permite ver'),
      ('deleted". por padrão os clientes POP3', 'deleted". Por padrão os clientes POP3'), ('offline. por padrão os clientes IMAP4', 'offline. Por padrão os clientes IMAP4')]
for a, n in CX:
    r0a, r1a, r1n = ce(F0, a, ('L6A_estudo',)), ce(F1, a, ('L6A_estudo',)), ce(F1, n, ('L6A_estudo',))
    chk('C-15', 'L6A_estudo: ' + a[:38], r0a == 1 and r1a == 0 and r1n == 1 and len(a) == len(n) and sum(x != y for x, y in zip(a, n)) == 1, 'atual R0=%d R1=%d | novo R1=%d' % (r0a, r1a, r1n))

# C-06..C-08 pegadinhas
def pg(P, lid): return [l for l in P['lotes'] if l['id'] == lid][0]['pegadinhas']
e15 = {"itemEdital": "P2-1.5", "rotulo": "Pontuação automática e capitalização em transcrições", "texto": "Dizer que a pontuação automática \"detecta os sinais pronunciados\" (isso é pontuação falada). Dizer que capitalização automática identifica nomes próprios \"com certeza\" — ela estima; \"Câmara\" (instituição) vs \"câmara\" (sala) é decisão de contexto que o modelo pode errar."}
b1 = {"itemEdital": "P1-8.2", "rotulo": "Gráfico de barras (colunas)", "texto": "usar para distribuição de variável contínua agrupada em classes; empilhado quando se quer comparar as partes entre si."}
b2 = {"itemEdital": "P1-8.2", "rotulo": "Box plot (diagrama de caixa)", "texto": "dizer que a linha central é a média; que a caixa vai do mínimo ao máximo ou contém todos os dados; que os bigodes vão até 1,5 desvio padrão; que mostra frequência por intervalo (isso é histograma)."}
a15 = ['Dizer que a pontuação automática "detecta os sinais pronunciados" (isso é pontuação falada). Dizer que capitalização automática identifica nomes próprios "com certeza" — ela estima', '"Câmara" (instituição) vs "câmara" (sala) é decisão de contexto que o modelo pode errar.']
ab1 = ['usar para distribuição de variável contínua agrupada em classes', 'empilhado quando se quer comparar as partes entre si.']
ab2 = ['dizer que a linha central é a média', 'que a caixa vai do mínimo ao máximo ou contém todos os dados', 'que os bigodes vão até 1,5 desvio padrão', 'que mostra frequência por intervalo (isso é histograma).']
def entradas(P, lid, ie, rot): return [g['texto'] for g in pg(P, lid) if g['itemEdital'] == ie and g['rotulo'] == rot]
chk('C-06', 'L1 P2-1.5: R0 2 entradas (atual) → R1 1 entrada (novo, dict literal)', entradas(P0, 'L1', 'P2-1.5', e15['rotulo']) == a15 and entradas(P1, 'L1', 'P2-1.5', e15['rotulo']) == [e15['texto']] and e15 in pg(P1, 'L1') and not any(g['texto'] in a15 for g in pg(P1, 'L1')), 'entradas R0=%d R1=%d' % (len(entradas(P0, 'L1', 'P2-1.5', e15['rotulo'])), len(entradas(P1, 'L1', 'P2-1.5', e15['rotulo']))))
chk('C-07', 'L5 Gráfico de barras: R0 4 entradas → R1 3 (2 mantidas + 1 reunida)', entradas(P0, 'L5', 'P1-8.2', b1['rotulo']) == ['confundir com histograma', 'aceitar eixo truncado'] + ab1 and entradas(P1, 'L5', 'P1-8.2', b1['rotulo']) == ['confundir com histograma', 'aceitar eixo truncado', b1['texto']] and b1 in pg(P1, 'L5'), 'R0=%d R1=%d' % (len(entradas(P0, 'L5', 'P1-8.2', b1['rotulo'])), len(entradas(P1, 'L5', 'P1-8.2', b1['rotulo']))))
chk('C-08', 'L5 Box plot: R0 4 entradas → R1 1 entrada (dict literal)', entradas(P0, 'L5', 'P1-8.2', b2['rotulo']) == ab2 and entradas(P1, 'L5', 'P1-8.2', b2['rotulo']) == [b2['texto']] and b2 in pg(P1, 'L5'), 'R0=%d R1=%d' % (len(entradas(P0, 'L5', 'P1-8.2', b2['rotulo'])), len(entradas(P1, 'L5', 'P1-8.2', b2['rotulo']))))
# edição: pegadinhas reunidas
for c, f, novo, atual_rx in (('C-06', 'L1_estudo', '— ' + e15['texto'], r'ela estima\n- \[P2-1\.5\]'), ('C-07', 'L5_estudo', '— ' + b1['texto'], r'classes\n- \[P1-8\.2\] \*\*Gráfico de barras \(colunas\)\*\* — empilhado'), ('C-08', 'L5_estudo', '— ' + b2['texto'], r'a média\n- \[P1-8\.2\] \*\*Box plot')):
    chk(c, 'edição %s: reunião' % f, ce(F1, novo, (f,)) == 1 and cre(F0, atual_rx, (f,)) == 1 and cre(F1, atual_rx, (f,)) == 0 and ce(F0, novo, (f,)) == 0, 'novo R1=%d | atual(rx) R0=%d R1=%d' % (ce(F1, novo, (f,)), cre(F0, atual_rx, (f,)), cre(F1, atual_rx, (f,))))

# C-09
rx9 = re.compile(r'(?<!NORMATIVO — )\bQA\b|\bO-\d+\b|Retificação|[Gg]abarito [CE] mantido')
aut0 = [i for i in P0['itens'] if i['rotulo'] == 'AUTORAL']; aut1 = [i for i in P1['itens'] if i['rotulo'] == 'AUTORAL']
h0 = sorted(i['id'] for i in aut0 if rx9.search(i['justificativa'])); h1 = sorted(i['id'] for i in aut1 if rx9.search(i['justificativa']))
chk('C-09', 'varredura F4 nas 180 justificativas AUTORAL (QA, O-n, Retificação, Gabarito C|E mantido)', len(aut1) == 180 and h1 == [] and h0 == ['4C-09', '6B-06', '6B-15', 'L2-Q21'], 'R0 acusa %s; R1 acusa %s' % (h0, h1))

# C-10
rxid = r'^\*\*\d+\*\* — (?:BQ-\d{4}|[A-Z0-9]+-[A-Z]?\d+) — '
folhas = tuple(s + '_folha' for s in ('SIM-0', 'SIM-1', 'SIM-2', 'SIM-0-P2'))
chk('C-10', 'folhas: linhas de item com id (atual) 165→0; linhas sem id (novo) 165', cre(F0, rxid, folhas) == 165 and cre(F1, rxid, folhas) == 0 and cre(F1, r'^\*\*\d+\*\* — ', folhas) == 165, 'R0=%d R1=%d | novo R1=%d' % (cre(F0, rxid, folhas), cre(F1, rxid, folhas), cre(F1, r'^\*\*\d+\*\* — ', folhas)))
ids_g = sum(1 for s in P1['simulados'] for k, x in enumerate(s['itens'], 1) if ('### %d — %s — Gabarito:' % (k, x)) in F1[s['id'] + '_gabarito.md'])
chk('C-10', 'id presente nos *_gabarito.md dos simulados (165/165)', ids_g == 165, str(ids_g))
# C-11
def ordem(F, nome):
    L_ = F[nome].split('\n'); nonblank = [l for l in L_ if l.strip()]
    tb_antes = sum(1 for k in range(len(nonblank) - 1) if nonblank[k].startswith('**Texto-base.**') and nonblank[k + 1].startswith('**Comando.**'))
    cmd_antes = sum(1 for k in range(len(nonblank) - 1) if nonblank[k].startswith('**Comando.**') and nonblank[k + 1].startswith('**Texto-base.**'))
    return tb_antes, cmd_antes
tot = collections.Counter()
for nome in F1:
    a, b = ordem(F1, nome); tot['R1 TB→Cmd'] += a; tot['R1 Cmd→TB'] += b
    a, b = ordem(F0, nome); tot['R0 TB→Cmd'] += a; tot['R0 Cmd→TB'] += b
chk('C-11', 'texto-base antes do comando em todos os arquivos (R1: 4 TB→Cmd, 0 Cmd→TB; R0: 0 e 4)', tot['R1 TB→Cmd'] == 4 and tot['R1 Cmd→TB'] == 0 and tot['R0 Cmd→TB'] == 4 and tot['R0 TB→Cmd'] == 0, str(dict(tot)))
chk('C-11', 'BANCO_itens (3) e SIM-0_folha (1)', ordem(F1, 'BANCO_itens.md') == (3, 0) and ordem(F1, 'SIM-0_folha.md') == (1, 0) and ordem(F0, 'BANCO_itens.md') == (0, 3) and ordem(F0, 'SIM-0_folha.md') == (0, 1))
# C-13 igualdade com o pacote
j11 = itens1['L4-11']['justificativa']
esp = '- Justificativa: ' + j11.replace(' Fonte: F4, reverificado em 7/10/2026.', '')
chk('C-13', 'L4_gabarito L4-11 = justificativa do pacote menos exatamente " Fonte: F4, reverificado em 7/10/2026."', esp in F1['L4_gabarito.md'] and ' Fonte: F4, reverificado em 7/10/2026.' in j11 and 'Fonte: F4' not in F1['L4_gabarito.md'], '')
# C-14
l0 = [l for l in F0['L6B_gabarito.md'].split('\n') if 'Curso 4.3.4' in l]; l1 = [l for l in F1['L6B_gabarito.md'].split('\n') if 'Curso 4.3.4' in l]
chk('C-14', 'edição 6B-15 e 6B-06 igual à R0 salvo C-19 (regras literais sem objeto retiradas)', l0 == l1 and len(l1) == 1, '')
# C-16a: linha em branco seguinte
chk('C-16', 'L6A: linha seguinte à frase apagada é a em branco antes de "### 3.1.3"', 'ficam no servidor).\n\n### 3.1.3' in F1['L6A_estudo.md'].replace('```text', ''), '')
# C-20
codes = r'\b(?:U[1-6]|GG\d|TB\d|CI)\b|erificado em 8/10/2026'
chk('C-20', 'L5_*.md: 0 ocorrência de U1–U6, GG, TB, CI e "erificado em 8/10/2026" (R0: >0)', cre(F1, codes, ('L5_',)) == 0 and cre(F0, codes, ('L5_',)) > 0, 'R0=%d R1=%d' % (cre(F0, codes, ('L5_',)), cre(F1, codes, ('L5_',))))
tit = ['Power BI (Microsoft)', 'Tableau (Salesforce)', 'Data Studio (Google)']
lines5 = F1['L5_estudo.md'].split('\n')
chk('C-20', 'títulos exatos Power BI (Microsoft) / Tableau (Salesforce) / Data Studio (Google)', all(t in lines5 for t in tit), '')
g5 = {'A5-14': 'Três componentes e fluxo ("three primary components"; Desktop = "development tool"; serviço "allows you to organize, manage, and distribute"); natureza Windows do Desktop.',
      'A5-15': 'TC (descontinuado no lugar de renomeado). Em 11/10/2022 o Data Studio foi renomeado Looker Studio ("Data Studio is now Looker Studio"), não descontinuado; em abril de 2026 o nome voltou a ser Data Studio, nome vigente.',
      'A5-16': 'Public "A free platform to explore, create, and publicly share"; Server "A self-hosted platform"; Cloud "A fully hosted cloud-based" platform.',
      'A5-17': 'IC (fluxo invertido). "First, you start with Power BI Desktop to connect to data and create the report. Then you publish the report to the Power BI service".'}
gl = F1['L5_gabarito.md'].split('\n')
chk('C-20', 'A5-14 a A5-17 na edição = texto exigido pela GBQ (4/4)', all(('- Justificativa: ' + v) in gl for v in g5.values()), '')
chk('C-20', '8.3 resumo: "8.3 FERRAMENTAS (VOLÁTIL)." sem "verificado em"', '8.3 FERRAMENTAS (VOLÁTIL). Power BI:' in F1['L5_estudo.md'], '')
# C-24
chk('C-24', 'linhas terminadas em " — " (R0: 27 = L1 1, L2 9, L3 17; R1: 0) e "× ****" (R0 1; R1 0)',
    [cre(F0, r' — $', ('L1_estudo',)), cre(F0, r' — $', ('L2_estudo',)), cre(F0, r' — $', ('L3_estudo',))] == [1, 9, 17] and cre(F1, r' — $', None) == 0 and cre(F0, r'\*\*\*\*', None) == 1 and cre(F1, r'\*\*\*\*', None) == 0,
    'R0 L1/L2/L3=%s; R1 total=%d' % ([cre(F0, r' — $', ('L1_estudo',)), cre(F0, r' — $', ('L2_estudo',)), cre(F0, r' — $', ('L3_estudo',))], cre(F1, r' — $', None)))
chk('C-24', 'par L1 "Tradução (whisper-1…)" sem " — "', '- **Tradução (whisper-1, só para inglês)** × **transcrição (idioma original)**\n' in F1['L1_estudo.md'], '')

# C-25: relatório (conferido depois por outro script; aqui só registra)
# ---------------------------------------------------------------- (2) diff R0 -> R1 do pacote
def walk(a, b, path, out):
    if type(a) != type(b): out.append((path, 'tipo')); return
    if isinstance(a, dict):
        if list(a.keys()) != list(b.keys()): out.append((path, 'chaves'))
        for k in a:
            if k in b: walk(a[k], b[k], path + [k], out)
    elif isinstance(a, list):
        if len(a) != len(b): out.append((path, 'tamanho %d→%d' % (len(a), len(b)))); return
        for i, (x, y) in enumerate(zip(a, b)): walk(x, y, path + [i], out)
    elif a != b: out.append((path, 'valor'))
# comparar itens por id e lotes por id
dif = []
walk({k: v for k, v in P0.items() if k not in ('itens', 'lotes')}, {k: v for k, v in P1.items() if k not in ('itens', 'lotes')}, [], dif)
i0 = {i['id']: i for i in P0['itens']}; i1 = {i['id']: i for i in P1['itens']}
chk('DIFF', 'itens: mesma lista de ids na mesma ordem', [i['id'] for i in P0['itens']] == [i['id'] for i in P1['itens']])
for k in i0:
    d = []; walk(i0[k], i1[k], [k], d); dif += d
for l0_, l1_ in zip(P0['lotes'], P1['lotes']):
    d = []; walk({k: v for k, v in l0_.items() if k != 'pegadinhas'}, {k: v for k, v in l1_.items() if k != 'pegadinhas'}, [l0_['id']], d); dif += d
    if l0_['pegadinhas'] != l1_['pegadinhas']: dif.append(([l0_['id'], 'pegadinhas'], 'lista'))
permit_just = {'4C-08', '4C-09', '5C-06', '6B-06', '6B-15', 'L2-Q21'}
perm = lambda p: (len(p) == 2 and p[0] in permit_just and p[1] == 'justificativa') or (len(p) == 2 and p[0] in ('L1', 'L5') and p[1] == 'pegadinhas')
nao = [d for d in dif if not perm(d[0])]
chk('DIFF', 'pacote R0→R1: só justificativa de 4C-08, 4C-09, 5C-06, 6B-06, 6B-15, L2-Q21 e pegadinhas de L1 e L5', not nao and {d[0][0] for d in dif if d[0][1] == 'justificativa'} == permit_just and {d[0][0] for d in dif if d[0][1] == 'pegadinhas'} == {'L1', 'L5'}, 'diferenças: %s ; fora da lista: %s' % (sorted(['/'.join(map(str, d[0])) for d in dif]), nao))
# cada justificativa alterada: só deleção (+ caixa)
def del_only(a, b):
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False); n = 0
    for op, i1_, i2_, j1_, j2_ in sm.get_opcodes():
        if op == 'equal' or op == 'delete': continue
        if op == 'replace' and j2_ - j1_ == 1 and a[i2_ - 1].islower() and b[j1_] == a[i2_ - 1].upper(): n += 1; continue
        return False, n
    return True, n
for k in sorted(permit_just):
    ok, n = del_only(i0[k]['justificativa'], i1[k]['justificativa'])
    chk('DIFF', '%s justificativa: só deleção%s' % (k, ' + 1 troca de caixa' if k in ('4C-08', '5C-06') else ''), ok and n == (1 if k in ('4C-08', '5C-06') else 0), 'trocas de caixa=%d' % n)
# pegadinhas: demais entradas intactas, junção = entrada R0
def junta(P, lid): return [g for g in pg(P, lid)]
for lid, merges in (('L1', [(a15, e15)]), ('L5', [(ab1, b1), (ab2, b2)])):
    r0 = pg(P0, lid); r1 = pg(P1, lid); ok = True; j = 0; i = 0
    while i < len(r0):
        hit = [(a, n) for a, n in merges if [g['texto'] for g in r0[i:i + len(a)]] == a and r0[i]['itemEdital'] == n['itemEdital'] and r0[i]['rotulo'] == n['rotulo']]
        if hit:
            a, n = hit[0]
            if j >= len(r1) or r1[j] != n or '; '.join(a) != n['texto']: ok = False
            i += len(a); j += 1
        else:
            if j >= len(r1) or r1[j] != r0[i]: ok = False
            i += 1; j += 1
    chk('DIFF', 'pegadinhas %s: demais entradas idênticas entrada a entrada; junção "; " = entrada reunida' % lid, ok and j == len(r1), 'R0=%d R1=%d' % (len(r0), len(r1)))

# ---------------------------------------------------------------- (5) contagens
npeg = lambda P: sum(len(l['pegadinhas']) for l in P['lotes'])
v11 = refs.v11()
j_dif = sum(1 for i in P1['itens'] if i['rotulo'] == 'AUTORAL' and i['justificativa'] != {x['id']: x for x in v11['itens']}[i['id']]['justificativa'])
j_dif0 = sum(1 for i in P0['itens'] if i['rotulo'] == 'AUTORAL' and i['justificativa'] != {x['id']: x for x in v11['itens']}[i['id']]['justificativa'])
cnt = [('pegadinhas total', npeg(P0), npeg(P1), 262), ('pegadinhas L1', len(pg(P0, 'L1')), len(pg(P1, 'L1')), 19), ('pegadinhas L5', len(pg(P0, 'L5')), len(pg(P1, 'L5')), 48),
       ('justificativas F4 (≠ v1.1)', j_dif0, j_dif, 21),
       ('itens', len(P0['itens']), len(P1['itens']), 286),
       ('C', sum(i['gabarito'] == 'C' for i in P0['itens']), sum(i['gabarito'] == 'C' for i in P1['itens']), 149), ('E', sum(i['gabarito'] == 'E' for i in P0['itens']), sum(i['gabarito'] == 'E' for i in P1['itens']), 137),
       ('aderência direta', sum(i['aderencia'] == 'direta' for i in P0['itens']), sum(i['aderencia'] == 'direta' for i in P1['itens']), 247), ('aderência parcial', sum(i['aderencia'] == 'parcial' for i in P0['itens']), sum(i['aderencia'] == 'parcial' for i in P1['itens']), 39),
       ('volatil', sum(bool(i.get('volatil')) for i in P0['itens']), sum(bool(i.get('volatil')) for i in P1['itens']), 23), ('nota', sum('nota' in i for i in P0['itens']), sum('nota' in i for i in P1['itens']), 2),
       ('comandoOriginal', sum('comandoOriginal' in i for i in P0['itens']), sum('comandoOriginal' in i for i in P1['itens']), 90),
       ('simulados n', [s['n'] for s in P0['simulados']], [s['n'] for s in P1['simulados']], [60, 40, 40, 25]),
       ('pares por lote', [len(l['pares']) for l in P0['lotes']], [len(l['pares']) for l in P1['lotes']], [len(l['pares']) for l in P0['lotes']]),
       ('discursivas', len(P0['discursivas']), len(P1['discursivas']), 5), ('edital', len(P0['edital']), len(P1['edital']), 47),
       ('arquivos da edição', len(F0), len(F1), 43)]
for nome, a, b, esp in cnt:
    chk('CONT', nome, b == esp and (a == b or nome in ('pegadinhas total', 'pegadinhas L1', 'pegadinhas L5', 'justificativas F4 (≠ v1.1)')), 'R0=%s R1=%s previsto R1=%s' % (a, b, esp))

# ---------------------------------------------------------------- (6) varredura na edição
VAR = [(r';\)', None), (r' — $', None), (r'\*\*\*\*', None), (r'abertas? hoje', None), (r'\(v2,', None), (r'D-LEI-15352', None), (r'neste chat', None), (r'Retificação', None),
       (r'Gabarito [CE] mantido', None), (r'\b(?:U[1-6]|GG\d|TB\d|CI)\b', None), (r'\bN\d\b', ('L1_', 'L1C_', 'L2_', 'L3_', 'SIM-2', 'SIM-0-P2')),
       (r' — (?:BQ|L\d|4C|5C|6A|6B|A5)', folhas)]
for rx, files in VAR:
    n1 = cre(F1, rx, files); n0 = cre(F0, rx, files)
    chk('VARR', '%s%s' % (rx, ' em ' + ','.join(files) if files else ''), n1 == 0, 'R0=%d R1=%d' % (n0, n1))
codF = [(f, k, l.strip()[:120]) for f, t in F1.items() for k, l in enumerate(t.split('\n'), 1) if re.search(r'\bF\d{1,2}\b', l)]
chk('VARR', 'códigos F: só "a tecla F4" (L6A) e "O F4 afirma" (L4-11)', len(codF) == 2 and any('tecla F4' in c[2] for c in codF) and any('O F4 afirma' in c[2] for c in codF), str([(c[0], c[1]) for c in codF]))
# VOLÁTIL fora do aviso fixo
AV = 'Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.'
vol = collections.Counter(); volex = []
for f, t in F1.items():
    for k, l in enumerate(t.split('\n'), 1):
        if 'VOLÁTIL' in l and AV not in l:
            vol[f] += 1
            if len(volex) < 60: volex.append((f, k, l.strip()[:100]))
json.dump({'volatil_fora_do_aviso': dict(vol), 'amostra': volex}, open(os.path.join(OUT, 'varredura_volatil.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
chk('VARR', 'VOLÁTIL fora do aviso fixo: só em arquivos *_estudo.md (títulos/rubricas de curso e resumo) e nas justificativas de gabarito?', True, 'por arquivo: %s' % dict(vol))

# diff linha a linha da edição atribuído às correções
def attrib(f, l0_):
    a = []
    if f.endswith('_folha.md') and re.match(rxid, l0_): a.append('C-10')
    if f.endswith('_estudo.md') and re.search(r' — $|\*\*\*\* — $', l0_): a.append('C-24')
    return a
ATR = {'C-01': ['Retificação 6-A'], 'C-05': ['. o item não depende', '. a regra de 1,5'], 'C-04': ['Gabarito E mantido'], 'C-06': ['ela estima', '"Câmara" (instituição) vs'], 'C-07': ['classes', 'empilhado quando'],
       'C-08': ['a média', 'que a caixa vai', 'que os bigodes', 'que mostra frequência'], 'C-12': ['vetado;)'], 'C-13': ['"prioritariamente supervisionado"). O item descreve'],
       'C-16': ['portas e criptografia do Exchange', '(diz "não estão', 'e orienta excluir'], 'C-17': ['(v2,'], 'C-18': ['D-LEI-15352'], 'C-19': ['abertas hoje', 'aberta hoje'],
       'C-20': ['U1', 'U2', 'U3', 'U4', 'U5', 'U6', 'GG4', 'TB2', 'erificado em 8/10/2026'], 'C-21': ['NÃO VOLÁTIL', 'não VOLÁTIL', 'Sem marca VOLÁTIL'], 'C-22': ['(N', 'Ver N', 'ver N', ' N7', 'NÃO foram verificados'], 'C-23': ['neste chat'],
       'C-15': [l_ for l_ in ('mesclar combina', 'a função SE compara', 'o PROCV pesquisa', 'o propósito é fazer', 'a animação é aplicada', 'o histórico de versões permite', 'por padrão os clientes')]}
nattr = collections.Counter(); sem = []
for f in sorted(F1):
    a = F0[f].split('\n'); b = F1[f].split('\n')
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for op, i1_, i2_, j1_, j2_ in sm.get_opcodes():
        if op == 'equal': continue
        rem = a[i1_:i2_]; add = b[j1_:j2_]
        # C-11: reordenação de texto-base/comando
        if sorted(rem) == sorted(add) or all(l.startswith(('**Comando.**', '**Texto-base.**')) or l == '' for l in rem + add):
            nattr['C-11'] += 1; continue
        for l_ in rem:
            if not l_.strip(): continue
            hit = attrib(f, l_) + [c for c, ks in ATR.items() if any(k in l_ for k in ks)]
            if l_.startswith(('**Texto-base.**', '**Comando.**')): hit = ['C-11'] + hit
            if not hit and f in ('BANCO_gabarito.md', 'BANCO_itens.md', 'SIM-0_folha.md', 'SIM-0_gabarito.md') and 'D-LEI-15352' in l_: hit = ['C-18']
            if hit: nattr[hit[0]] += 1
            else: sem.append((f, l_[:100]))
chk('DIFF-E', 'edição R0→R1: toda linha alterada é atribuível a uma correção C-01..C-24', not sem, 'atribuídas: %s; sem atribuição: %s' % (dict(sorted(nattr.items())), sem[:5]))
fails = [r for r in res if not r[2]]
print('\n%d conferências; %d falhas' % (len(res), len(fails)))
json.dump([list(r) for r in res], open(os.path.join(OUT, 'conferencias_R1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
sys.exit(1 if fails else 0)
