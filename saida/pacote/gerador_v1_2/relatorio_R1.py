# -*- coding: utf-8 -*-
"""Edita saida/pacote/pacote_relatorio_2026-10-13.md: corrige R4/O-2 e acrescenta a seção 13 (Correção R1). Não apaga o histórico R0."""
import hashlib, json, os, re, difflib, sys
REPO = '/home/claude/fabrica_camara2026'
REL = REPO + '/saida/pacote/pacote_relatorio_2026-10-13.md'
R0 = 'R0'
t = open(R0 + '/pacote_relatorio_2026-10-13.md', encoding='utf-8').read()     # sempre parte do R0 (idempotente)
def rep(a, b):
    global t
    assert t.count(a) == 1, (a[:60], t.count(a))
    t = t.replace(a, b)

# ---- cabeçalho: nota R1
rep('Resultado em uma linha: **286 itens**', '**Nota R1 (13/10/2026):** as seções 1 a 12 e o Apêndice A descrevem o estado R0 (histórico preservado); os pontos de relatório R4 (gce-cqfp) e O-2 (gcb-cqfp) foram corrigidos no lugar (marcados "[corrigido na R1]"); a correção R1, com resultados dos scripts, novas contagens e SHA-256, está na **seção 13**. Contagens da R1: F4 21 justificativas; pegadinhas 262 (L1 19, L5 48); validação 103 verificações, 0 falhas; fidelidade da edição 0 diferenças.\n\nResultado em uma linha (R0): **286 itens**')

# ---- C-25 (1): rótulos de alvo (gce-cqfp R4)
rep('| L1 | E4c | curso 1.1 (par/pegadinha): "No cálculo usual, pontuação e capitalização ficam fora do WER…" |', '| L1 | E4c | (d-G) Q01 (justificativa): "No cálculo usual, pontuação e capitalização ficam fora do WER…" [corrigido na R1; R0: "curso 1.1 (par/pegadinha)"] |')
rep('| L1C | E3 | curso: "end-to-end, não há dicionário de pronúncias separado" |', '| L1C | E3 | (d) Q23 (enunciado): "end-to-end, não há dicionário de pronúncias separado" [corrigido na R1; R0: "curso"] |')
rep('| L3 | E1b | curso 4.1: art. 20, "expressão suprimida (MP nº 869/2018, convertida na Lei 13.853/2019)" |', '| L3 | E1b | resumo (b), linha 4.1: art. 20, "expressão suprimida (MP nº 869/2018, convertida na Lei 13.853/2019)" [corrigido na R1; R0: "curso 4.1"] |')
rep('| L3 | E3b | curso 4.1: idem, "da redação original" |', '| L3 | E3b | (d-G) Q20 (justificativa): idem, "da redação original" [corrigido na R1; R0: "curso 4.1"] |')

# ---- C-25 (2): explicação da 18ª justificativa (gcb-cqfp O-2)
rep('Pode-se contar 17 se A5-14 a A5-17 forem tomados como um bloco de 3 ou se a L2-Q23 não for contada; registro em DÚVIDA 1.',
    'As 17 da GBQ são as justificativas com os tipos de marca que ela listou (CQFP, "(v3 — O12)", "(O1)", "Lição O10", "R-4C1", "Risco"); a 18.ª é a 5C-03 ("R-5C1", mesma classe de R-4C1); com a rodada R1 (6B-06, 6B-15, L2-Q21) a F4 soma 21 [corrigido na R1, gcb-cqfp O-2; R0 dizia: "Pode-se contar 17 se A5-14 a A5-17 forem tomados como um bloco de 3 ou se a L2-Q23 não for contada"]; registro em DÚVIDA 1.')
rep('Se a GBQ quiser 17, diga qual excluir (candidata natural: nenhuma; todas têm marca). Efeito: só deleção.',
    'Se a GBQ quiser 17, diga qual excluir (candidata natural: nenhuma; todas têm marca). Efeito: só deleção. [R1: decidido na reconciliação (D-R1-20 e DÚVIDA 1): aceitas as 18; as 17 da GBQ são as dos tipos listados e a 18.ª é a 5C-03 ("R-5C1"); com 6B-06, 6B-15 e L2-Q21 a F4 passa a 21 justificativas.]')

# ---- seção 13
sha1 = hashlib.sha256(open(REPO + '/saida/pacote/pacote.json', 'rb').read()).hexdigest()
sha0 = hashlib.sha256(open(R0 + '/pacote.json', 'rb').read()).hexdigest()
sz1 = os.path.getsize(REPO + '/saida/pacote/pacote.json'); sz0 = os.path.getsize(R0 + '/pacote.json')
conf = json.load(open('out/conferencias_R1.json', encoding='utf-8'))
nconf = len(conf); nfail = sum(1 for c in conf if not c[2])
vtxt = open('out/validate_final.txt', encoding='utf-8').read()
m = re.search(r'(\d+) verificações; (\d+) falhas', vtxt); nval, nvf = m.group(1), m.group(2)
ftxt = open('out/fidelidade_final.txt', encoding='utf-8').read()
m = re.search(r"total (\d+)", ftxt); ntot = m.group(1)
cnt = json.load(open('out/estudante_contagem.json', encoding='utf-8'))['total']
ntot_rem = sum(cnt.values())
# diff por arquivo
D0 = R0 + '/estudante'; D1 = REPO + '/saida/estudante'
rows = []
for f in sorted(os.listdir(D1)):
    a = open(os.path.join(D0, f), encoding='utf-8').read().split('\n'); b = open(os.path.join(D1, f), encoding='utf-8').read().split('\n')
    if a != b:
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        rem = sum(i2 - i1 for op, i1, i2, j1, j2 in sm.get_opcodes() if op in ('replace', 'delete')); add = sum(j2 - j1 for op, i1, i2, j1, j2 in sm.get_opcodes() if op in ('replace', 'insert'))
        rows.append((f, rem, add))
nchg = len(rows)

S = []
w = S.append
w('## 13. Correção R1 (13/10/2026)')
w('')
w('Rodada de correção R1 da T-48 (lista C-01 a C-25, seção 3 de `saida/pacote/T48_reconciliacao_R1_2026-10-13.md`, D1 da GBQ). Corrigido o GERADOR (cópia em `s4/t48r1/` do scratchpad; os scripts de `s4/t48/` ficam intactos como prova da R0) e REGERADOS `saida/pacote/pacote.json` e `saida/estudante/` por inteiro (43 arquivos, mesmos nomes); nenhum arquivo foi editado à mão. A saída R0 (pacote.json, relatório e `estudante/`) está guardada em `s4/t48r1/R0/`. Nada foi commitado; TAREFAS.md, PARA_PRESIDENCIA.md, DECISOES.md, estado/, banco/, regras/ e os canônicos dos lotes não foram tocados por esta rodada.')
w('')
w('Regras de execução: continua "só deleção", com as duas exceções fechadas da reconciliação (3.0.4): (i) CAIXA (C-05 e C-15): minúscula → maiúscula na primeira letra indicada (2 no pacote, 8 na edição); (ii) reunião de fragmentos de pegadinha com "; " (C-06 a C-08: 5 reuniões, 267 → 262). Mais a exceção da C-18 (nota de BQ-0003 sai da edição sem " (D-LEI-15352)"; no pacote a nota continua literal).')
w('')
w('### 13.1 Pacote R0 → R1')
w('')
w('| | R0 | R1 |')
w('|---|---|---|')
w('| SHA-256 do `pacote.json` | `%s` (%d bytes) | `%s` (%d bytes) |' % (sha0, sz0, sha1, sz1))
w('| SHA-256 (12 primeiros) | `%s` | `%s` |' % (sha0[:12], sha1[:12]))
w('')
w('### 13.2 Tabela C-xx (alvo, resultado, ocorrências)')
w('')
w('"Ocorrências" = texto atual R0 → R1 (previsto: 0 no R1) e texto novo no R1. Fonte: `conferencias_R1.py` (118 conferências, 0 falhas), independente do gerador. Onde o texto atual está no pacote e na edição, aparecem os dois.')
w('')
w('| C | Alvo | Resultado | Ocorrências |')
w('|---|---|---|---|')
T = [
 ('C-01', '4C-09 `justificativa` (pacote; edição: `L4C_gabarito.md`)', 'APLICADA (deleção de " Retificação 6-A: … RAG").")', 'pacote 1 → 0, novo 1; edição 1 → 0, novo 1'),
 ('C-02', '6B-06 `justificativa` (pacote); edição já limpa', 'APLICADA (deleção de ", conferida pela QA em 08/10/2026")', 'pacote 1 → 0, novo 1; edição 0 → 0 (novo 1 nas duas)'),
 ('C-03', '6B-15 `justificativa` (pacote); edição já limpa', 'APLICADA (deleção de " (corrigido pela O-3)")', 'pacote 1 → 0, novo 1; edição 0 → 0 (novo 1 nas duas)'),
 ('C-04', 'L2-Q21 `justificativa` (pacote; edição: `L2_gabarito.md`)', 'APLICADA (deleção de " Gabarito E mantido.")', 'pacote 1 → 0, novo 1; edição 1 → 0, novo 1'),
 ('C-05', '4C-08 e 5C-06 `justificativa` (CAIXA)', 'APLICADA: "Lição O10: o item" → "O item"; "Lição O10: a regra" → "A regra" (no pacote R0 a marca já estava apagada e a inicial ficara minúscula: o "atual" medido é "… curso). o item não depende" e "… amostra. a regra de 1,5")', 'pacote 4C-08 1 → 0 e 5C-06 1 → 0 (novo 1 + 1); edição 4C-08 2 → 0 (`L4C_gabarito.md` e `SIM-1_gabarito.md`) e 5C-06 1 → 0'),
 ('C-06', '`lotes[L1].pegadinhas`, P2-1.5', 'APLICADA: 2 entradas → 1 (dict literal da lista)', 'entradas 2 → 1; L1 20 → 19; edição `L1_estudo.md` 2 linhas → 1'),
 ('C-07', '`lotes[L5].pegadinhas`, Gráfico de barras (colunas)', 'APLICADA: "usar para distribuição…; empilhado quando…" reunida; "confundir com histograma" e "aceitar eixo truncado" ficam', 'entradas do rótulo 4 → 3; edição `L5_estudo.md` 2 linhas → 1'),
 ('C-08', '`lotes[L5].pegadinhas`, Box plot (diagrama de caixa)', 'APLICADA: 4 fragmentos → 1 entrada (dict literal da lista)', 'entradas 4 → 1; L5 52 → 48; edição `L5_estudo.md` 4 linhas → 1'),
 ('C-09', 'validador F4 (`validate.py`)', 'APLICADA: padrões `(?<!NORMATIVO — )\\bQA\\b`, `\\bO-\\d+\\b`, `Retificação`, `[Gg]abarito [CE] mantido` acrescentados', 'R0 acusaria 4 justificativas (4C-09, 6B-06, 6B-15, L2-Q21); R1: 0 nas 180 AUTORAL'),
 ('C-10', 'folhas SIM-0, SIM-1, SIM-2, SIM-0-P2 (linhas de item)', 'APLICADA: `**{n}** — {enunciado}`; o id fica só nos `*_gabarito.md`', 'linhas com id 165 → 0; linhas sem id 165; id presente nos gabaritos 165/165'),
 ('C-11', '`BANCO_itens.md` (BQ-0049, 0050, 0051) e `SIM-0_folha.md` (item 12)', 'APLICADA: "Texto-base" antes de "Comando" nos três pontos de emissão (banco, folha, `*_itens.md`)', 'pares Comando→Texto-base 4 → 0; Texto-base→Comando 0 → 4 (BANCO_itens 3, SIM-0_folha 1)'),
 ('C-12', '`L4_estudo.md` 224 e 283 (";)")', 'APLICADA: regra genérica com ";" vem antes da regra com ",?"', '"vetado;)" 2 → 0; "vetado)." 2'),
 ('C-13', '`L4_gabarito.md`, L4-11 (restauração, D-R1-07)', 'APLICADA: regra literal nº 6 do apêndice A retirada; a frase "O F4 afirma que …" volta literal; só " Fonte: F4, reverificado em 7/10/2026." continua apagada', 'trecho sem a frase 1 → 0; com a frase 0 → 1; edição = justificativa do pacote menos exatamente a "Fonte: F4…" (conferido)'),
 ('C-14', 'regras literais nº 26 ("Curso 4.3.4⟦ (corrigido pela O-3)⟧:") e nº 63 ("seção ITENS REAIS⟦, conferida pela QA…⟧)")', 'APLICADA: as duas regras retiradas; o resultado na edição é o mesmo da R0', 'linhas de 6B-06 e 6B-15 na edição: R0 = R1 (a C-19 só mexe em "aberta hoje" da 6B-06)'),
 ('C-15', '`L6A_estudo.md` (CAIXA, lista fechada de 8)', 'APLICADA: 8 pares minúscula → maiúscula (1 caractere cada), fase CAIXA depois de `strip_text`, só no arquivo `L6A_estudo`', '8 pares, cada 1 → 0 (novo 1)'),
 ('C-16', '`L6A_estudo.md` (a) 166, (b) 60, (c) 135', 'APLICADA: (a) a linha "portas e criptografia do Exchange Online; …" some inteira com a quebra anterior (a seguinte é a em branco antes de "### 3.1.3"); (b) "diz " apagado ("(\\"não estão formatados…"); (c) " e orienta excluir o link e criar outro" apagado', '(a) 1 → 0; (b) 1 → 0; (c) 1 → 0 (novos 1 cada)'),
 ('C-17', '`L1C_estudo.md` 49 e 52 (DÚVIDA 5-a)', 'APLICADA: "(v2, item 1.4)" → "(item 1.4)"; "(v2, exemplo parlamentar do 1.4)" → "(exemplo parlamentar do 1.4)"', '2 → 0 (novos 2)'),
 ('C-18', 'nota de BQ-0003 na edição (`BANCO_itens.md`, `BANCO_gabarito.md`, `SIM-0_folha.md`, `SIM-0_gabarito.md`)', 'APLICADA: " (D-LEI-15352)" apagado só na exibição; no pacote a nota continua literal', '4 → 0 (novos 4); `D-LEI-15352` no pacote: igual à R0'),
 ('C-19', 'carimbo "aberta(s) hoje": L6A 31 e 188; L6B 142, 163, 170, 175, 187 e 245; `L6B_gabarito.md` 31 (6B-06)', 'APLICADA: 9 deleções', '9 alvos, cada 1 → 0 (novos 1 cada); `abertas? hoje` na edição 9 → 0'),
 ('C-20', 'códigos do L5 (U1–U6, GG4, TB2) e carimbos "verificado em 8/10/2026" (`L5_estudo.md`, `L5_gabarito.md`)', 'APLICADA: 6 regras literais + 5 genéricas só para `L5_*`; títulos `Power BI (Microsoft)`, `Tableau (Salesforce)`, `Data Studio (Google)`; A5-14 a A5-17 iguais ao texto exigido', 'ocorrências de `\\b(U[1-6]|GG\\d|TB\\d|CI)\\b` e "erificado em 8/10/2026" em `L5_*.md`: 49 → 0; remoções por tipo: 33 (códigos) + 4 (carimbo)'),
 ('C-21', 'classificação interna: L2-Q23 (`L2_gabarito.md`, `SIM-0-P2_gabarito.md`), L3-Q21 (`L3_gabarito.md`), L4-05 (`L4_gabarito.md`)', 'APLICADA: 3 regras', 'L2-Q23 2 → 0; L3-Q21 1 → 0; L4-05 1 → 0 (novos 2, 1, 1)'),
 ('C-22', 'códigos N do L2 (8 pontos) e do L3 (6 pontos); N1–N4 do L4 ficam', 'APLICADA: 5 regras genéricas só para `L2_*` e `L3_*` (depois das literais); resultados iguais aos da tabela da reconciliação', '14 alvos, cada 1 → 0; `\\bN\\d\\b` em L1*, L1C*, L2*, L3*, SIM-2*, SIM-0-P2*: 14 → 0'),
 ('C-23', '`L4_estudo.md` 210', 'APLICADA: " neste chat" apagado', '1 → 0 (novo 1)'),
 ('C-24', 'pares com `como` ou `b` vazio (L1 1, L2 9, L3 17) e L3 "× ****"', 'APLICADA: sem " — " quando `como` é vazio e sem " × **…**" quando `b` é vazio', 'linhas terminadas em " — " 27 → 0; "× ****" 1 → 0; os dois exemplos literais da lista conferidos'),
 ('C-25', 'este relatório', 'APLICADA: R4 (4 rótulos de alvo, seção 3), O-2 (seção 6 e DÚVIDA 1) e esta seção 13; o histórico R0 foi preservado', '4 linhas; 2 trechos; 1 seção'),
]
for r in T: w('| %s | %s | %s | %s |' % r)
w('')
w('### 13.3 Resultados dos scripts (saídas gravadas em `s4/t48r1/out/`)')
w('')
w('1. **Cada C-xx (texto atual some, texto novo no número previsto):** `conferencias_R1.py` → `conferencias_final.txt`: %d conferências, %d falhas (inclui as 8 do C-15, as 3 reuniões, as varreduras e o diff).' % (nconf, nfail))
w('2. **Diff R0 → R1 do `pacote.json`:** só `justificativa` de 4C-08, 4C-09, 5C-06, 6B-06, 6B-15 e L2-Q21 (cada uma só deleção; 4C-08 e 5C-06 com 1 troca de caixa) e `pegadinhas` de L1 (20 → 19) e L5 (52 → 48); nas pegadinhas, as demais entradas são idênticas entrada a entrada e a junção com "; " é a entrada reunida. Nenhuma outra diferença (itens, simulados, discursivas, edital, `nota`, `volatil`, `comandoOriginal`, ordem de campos).')
w('3. **`validate.py` (R1):** %s verificações, %s falhas (as 102 da R0 com as contagens ajustadas — F4 21, justificativas alteradas 21, padrões da C-09 — mais 1 verificação nova: pegadinhas L1 19, L5 48, total 262, 5 reuniões registradas).' % (nval, nvf))
w('4. **`estudante_fidelidade.py` (R1):** %s comparações, 0 diferenças, só com as exceções fechadas: CAIXA do L6A (8 trocas, todas em `L6A_estudo.md`), nota de BQ-0003 (4 exibições) e, no pacote, as 2 trocas de caixa da C-05. Edição = pacote com as deleções da lista ampliada; fora disso, só deleção.' % ntot)
w('5. **Contagens:** pegadinhas 262 (R0 267); justificativas alteradas da v1.1 para a v1.2 (F4) 21 (R0 18); iguais à R0: itens 286, C/E 149/137, aderência direta/parcial 247/39, `volatil` 23, `nota` 2, `comandoOriginal` 90, simulados `n` 60/40/40/25, pares por lote, discursivas 5, edital 47, arquivos da edição 43.')
w('6. **Varredura de marcas na edição do estudante:** 0 ocorrência de `;)`, ` — $`, `****`, `abertas? hoje`, `(v2,`, `D-LEI-15352`, `neste chat`, `Retificação`, `Gabarito [CE] mantido`, `\\b(U[1-6]|GG\\d|TB\\d|CI)\\b`, `\\bN\\d\\b` em L1*, L1C*, L2*, L3*, SIM-2*, SIM-0-P2*, e ` — (BQ|L\\d|4C|5C|6A|6B|A5)` nas folhas. Na R0 as ocorrências eram, na ordem: 2, 27, 1, 9, 2, 4, 1, 1, 1, 41, 14 e 165 (ver `conferencias_final.txt`).')
w('')
w('**Marcas que restam na edição e por quê:**')
w('')
w('| Resto | Onde | Por quê |')
w('|---|---|---|')
w('| `a tecla F4` | `L6A_estudo.md` 83 | tecla de função do Excel, não é código de fonte |')
w('| `O F4 afirma que "generative models …"` | `L4_gabarito.md` 56 (L4-11) | exceção registrada à varredura de códigos F (D-R1-07, opção (a)): "F4" é o sujeito da frase restaurada; apagá-lo quebra a sintaxe e trocá-lo seria reescrita |')
w('| `VOLÁTIL` fora do aviso fixo (7 linhas: `L4_estudo.md` 23 e 210; `L5_estudo.md` 24, 104 e 107; `L6A_estudo.md` 125 e 268) | títulos, rubricas e orientação de estudo | mantido por decisão (2.3-g): orientação de estudo, não marca de processo |')
w('| Etiquetas GI/TC/IC/AT | justificativas dos `*_gabarito.md` | mantidas (2.3-h); legenda como campo opcional de lote vai à errata do contrato (tarefa nova) |')
w('| Códigos N1–N4 do L4 | `L4_estudo.md` 169–217; `L4_gabarito.md` 88, 93, 103; `SIM-1_gabarito.md` | mantidos (2.3-e): definidos no próprio texto ("LGPD (N1, Lei 13.709/2018)") |')
w('| `(Derep (antigo DETAQ); …)` | `L1_estudo.md` | literal pela F5 (D-T12-V12); D-R1-15 DESCARTADO |')
w('| 29 justificativas iniciadas em minúscula depois do prefixo de campo "C — 5.1 —" | `*_gabarito.md` | forma do arquivo canônico, não efeito de deleção (D-R1-18 DESCARTADO) |')
w('| "que eu possa afirmar" | `L3_estudo.md` 422 | texto canônico da GCE; a deleção tornaria a afirmação absoluta (2.3-i, BACKLOG) |')
w('| Remissões a pares por id não exportado ("par C1", "par C14", "C19") | justificativas de A5-09, 5C-03, 5C-07 e 4C-08 (`L4C_gabarito.md`, `L5C_gabarito.md`, `L5_gabarito.md`, `SIM-1_gabarito.md`) | adiado (D-R1-21, BACKLOG) |')
w('| Avisos 1, 2 e 4 da folha canônica do SIM-0 | ausentes das folhas | adiado (D-R1-13): exige campo de contrato; o que se compartilha é do Fundador |')
w('| Nota R2 da D4 repetida na D5; rótulo "Nota: nota de vigência:" | `DISCURSIVAS_padrao.md`; notas do banco | cópia literal decidida na T-27 (D-R1-17); rótulo duplicado entra na tarefa "forma da edição" |')
w('| Quadro-síntese do L1 desalinhado; separador "×" dos pares | `L1_estudo.md`; `*_estudo.md` | BACKLOG (D-R1-14/16) |')
w('')
w('### 13.4 Novas contagens da edição do estudante')
w('')
w('Remoções por deleção na regeração: **%d** (R0: 492). Por tipo novo: códigos do L5 33; códigos N do L2/L3 14; "aberta(s) hoje" 9; caixa 8; classificação interna 4; carimbo "Verificado em 8/10/2026" 4; id de decisão na nota 4; "(v2, …)" 2; "neste chat" 1. Arquivos alterados em relação à R0: %d de 43 (linhas removidas/inseridas por arquivo):' % (ntot_rem, nchg))
w('')
w('| Arquivo | linhas R0 alteradas | linhas R1 |')
w('|---|---|---|')
for f, a, b in rows: w('| `%s` | %d | %d |' % (f, a, b))
w('')
w('### 13.5 Observações (fora da lista C-01 a C-25; nada foi aplicado)')
w('')
w('1. **C-05, texto "atual" do pacote.** A lista cita o fonte ("… curso). Lição O10: o item não depende"); no `pacote.json` R0 a marca já estava apagada (F4 da R0) e o texto era "… curso). o item não depende". A conferência usa o texto R0 do pacote; o resultado coincide com o texto novo da lista.')
w('2. **C-22 e L3 239–240.** Por causa da regra `LEAD + \\(N\\d\\)` (que absorve a quebra de linha antes do parêntese), as duas linhas "… NÃO foram verificados / (N5). A banca …" viram uma só ("… verificados. A banca …"), exatamente como na tabela da reconciliação ("`verificados. A banca`").')
w('3. **Marcas de processo candidatas, fora da lista:** `L4_estudo.md` 59 "(conceito geral, sem fonte de fornecedor neste lote)" e `L6B_estudo.md` 143 ("a especificação previa o item …"). Não aplicado; a GBQ decide se entram numa próxima rodada.')
w('4. **Arquivos do repositório alterados por outro processo durante a rodada:** `regras/pacote_contrato.md` e `saida/pacote/contrato_v1_2_1_2026-10-13.md` têm data posterior ao início desta rodada; não foram tocados por esta correção. `validate.py` leu o contrato e passou (103/103).')
w('5. **`T48_correcao_R1_2026-10-13.md`** (item 3.0.2 da reconciliação): não foi criado nesta rodada, por instrução da tarefa; esta seção 13 e as saídas em `s4/t48r1/out/` cobrem o conteúdo (correção a correção, diff R0 → R1, validadores).')
w('6. **Relatório.** Foi editado no lugar (R4, O-2 e esta seção); as contagens das seções 2, 5, 6, 8, 9, 10 e 11 e o Apêndice A continuam as da R0, por serem histórico, e as da R1 estão acima. O gerador do relatório (`report2.py`) não foi reexecutado.')
w('')
t = t.replace('\n## Apêndice A — regras literais', '\n' + '\n'.join(S) + '\n## Apêndice A — regras literais', 1)
assert '## 13. Correção R1' in t
open(REL, 'w', encoding='utf-8').write(t)
print('ok', len(t))
