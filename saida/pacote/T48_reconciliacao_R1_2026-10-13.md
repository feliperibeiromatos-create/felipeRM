# T48_reconciliacao_R1_2026-10-13.md — T-48 (rodada 1 de QA) e T-50 — 2026-10-13 — gerado por gbq-gerencia

REMETENTE: GBQ (gbq-gerencia, opus; não produziu nem revisou o objeto)
DESTINATÁRIO: gbq-csc (rodada de correção R1); depois gbq-cqe (QA, rodada 2). Cópia: gce-gerencia, gcb-gerencia (ressalvas dos seus QAs fechadas aqui).

## 0. Objeto e base

- T-48 (EXPORTAR v1.2; D-T12-V12, D-PACOTE-V11): `saida/pacote/pacote.json` v1.2 (SHA-256 `ae2f346830f8`), `saida/pacote/pacote_relatorio_2026-10-13.md` (`cef11163faf2`, 13 DÚVIDAS) e `saida/estudante/` (43 arquivos). Contrato: `regras/pacote_contrato.md` v1.1.1 + "Regras da v1.2" (a)–(j) (`d8ab26b6c3de`).
- QA lido: `QA_T48_2026-10-13_gbq-cqe.md` (`74ac61d4034a`; dados APROVADO, edição APROVADA COM RESSALVAS), `QA_T48_P2_2026-10-13_gce-cqfp.md` (`17fe1877e614`; R1–R4), `QA_T48_P1_2026-10-13_gcb-cqfp.md` (`8dfb994ca34f`; A-1 a A-5, O-1 a O-4).
- T-50: `saida/banco/T50_estilo_v1_1_3_2026-10-13.md` e `regras/estilo_banca.md` v1.1.3.
- Gates: nenhum. Reprovação 0/180 AUTORAL e 0/106 banco (limite 30%); nenhuma fonte não oficial; nenhum conflito entre Gerências; nenhum gatilho D (nenhum gabarito em causa).
- Verificação da gerência (somente leitura, `python3 -I`): cada texto "atual" da lista da seção 3 foi localizado no arquivo indicado com a contagem informada (1 ocorrência por alvo, salvo onde se diz outra); os scripts do gerador (`scratchpad/s4/t48/`: `f4.py`, `peg.py`, `estudante_gen.py`, `estudante_marcas.py`, `literais.py`) foram lidos para indicar o ponto de correção. A causa do ";)" foi confirmada: a regra genérica `,? conferid…(?=\))` casa antes da regra `;[ \t]*conferid…(?=\))` e deixa o ";".

## 1. Síntese

O `pacote.json` v1.2 está íntegro: os três QAs dão 0 divergência de gabarito, enunciado, comando, itemEdital, aderência e contagem, e todas as erratas foram aplicadas. As ressalvas são de forma: marcas de tramitação que sobraram em 4 justificativas, inicial minúscula em 2, 3 desdobramentos de pegadinha que não se leem sozinhos, e na edição do estudante sintaxe quebrada por deleção, ids nas folhas dos simulados, ordem texto-base/comando e marcas fora da lista. Tudo isso se corrige por deleção, por ajuste de caixa ou pontuação, ou por reunião de fragmentos já existentes. Nenhuma correção muda enunciado, comando, gabarito ou texto canônico de lote.

Decisão de fluxo: rodada de correção R1 pela gbq-csc (lista AGORA da seção 3), corrigindo o gerador e regenerando pacote e edição, e depois o QA da rodada 2 pela gbq-cqe (seção 5). O gatilho A da v1.2 só sai depois do veredito APROVADO/CONFERIDO da rodada 2.

## 2. Decisões (D1 da GBQ)

Legenda: aceitar = a ressalva procede e entra na correção; manter = aceito como está; adiar = vira tarefa.

### 2.1 Achados de QA

| # | Achado (origem) | Decisão | Classe | Correção |
|---|---|---|---|---|
| D-R1-01 | 4C-09: frase de tramitação "Retificação 6-A: …" (gcb-cqfp A-1) | aceitar; deleção no pacote e na edição (precedente QA EXEC-01 L4C, R-1) | AGORA | C-01 |
| D-R1-02 | 6B-06 ", conferida pela QA em 08/10/2026" e 6B-15 " (corrigido pela O-3)" no pacote (gcb-cqfp A-2) | aceitar; deleção no pacote (a edição já está limpa); F4 do validador ganha `\bQA\b` (fora de "NORMATIVO — QA") e `\bO-\d+\b` | AGORA | C-02, C-03, C-09 |
| D-R1-03 | L2-Q21 " Gabarito E mantido." (gce-cqfp R3, classificado PRÓXIMO) | aceitar e antecipar para AGORA: é marca de tramitação da errata E1 do L2, sai por deleção pura e vai na mesma regeração | AGORA | C-04 |
| D-R1-04 | Inicial minúscula depois da deleção de "Lição O10: " em 4C-08 e 5C-06 (gcb-cqfp A-3; gbq-cqe achado 3; DÚVIDA 2) | aceitar; autorizo a "capitalização de inicial deixada por deleção" como ajuste mínimo de caixa, sem troca de palavra, no pacote e na edição | AGORA | C-05 |
| D-R1-05 | F3, L5: fragmentos [29] e [34]–[36] dependem do verbo do fragmento anterior (gcb-cqfp A-4; DÚVIDA 3) | aceitar. A própria regra (d) manda que "texto corrido que não se separa sem reescrever fica como uma entrada só"; a enumeração elíptica não se separa. Reunir com o separador original "; ", sem texto novo | AGORA | C-07, C-08 |
| D-R1-06 | F3, L1 P2-1.5: o segundo fragmento é ilustração do primeiro e não é pegadinha (gce-cqfp R2, classificado PRÓXIMO) | aceitar e antecipar para AGORA: mesma operação da D-R1-05 e mesmo fundamento na regra (d) | AGORA | C-06 |
| D-R1-07 | L4-11, edição do estudante: a regra literal nº 6 do apêndice A apagou a única frase que fundamenta o gabarito C (gcb-cqfp A-5; DÚVIDA 7) | aceitar, opção (a): RESTAURAR a frase. Retira-se a regra literal nº 6 e a frase volta literal. Continua apagada pela regra genérica só a marca interna separada " Fonte: F4, reverificado em 7/10/2026.". A sigla "F4", sujeito da frase restaurada, não sai: tirá-la quebra a sintaxe e trocá-la seria reescrita (opção (b) recusada). É exceção registrada à varredura de códigos F | AGORA | C-13 |
| D-R1-08 | Ids de origem nas folhas dos 4 simulados (gce-cqfp R1 AGORA; gbq-cqe achado 5 PRÓXIMO) | aceitar como AGORA: o id leva ao gabarito na mesma edição e quebra a prova cega; sai por deleção pura | AGORA | C-10 |
| D-R1-09 | Texto-base depois do comando: BQ-0049/0050/0051 em `BANCO_itens.md` e Comando 8 de `SIM-0_folha.md` (gbq-cqe achado 1) | aceitar; o gerador emite "Texto-base" antes de "Comando" em todos os pontos de emissão. A errata da regra (b) do contrato vira tarefa PRÓXIMO | AGORA | C-11 |
| D-R1-10 | ";)" órfão em `L4_estudo.md` 224 e 283 (gbq-cqe achado 2) | aceitar; corrigir a ordem das regras genéricas (deleção pura) | AGORA | C-12 |
| D-R1-11 | Inicial minúscula no curso do L6A depois da deleção de "Conforme a Fn…:"/"Segundo a F14," (8 pontos; gbq-cqe achado 3; DÚVIDA 8) | aceitar; mesmo ajuste de caixa da D-R1-04, com lista fechada | AGORA | C-15 |
| D-R1-12 | L6A: frase sem sujeito (linha 166), "(diz …" (linha 60) e "e orienta …" sem sujeito (linha 135) (gbq-cqe achado 4; DÚVIDA 8) | aceitar, sempre por deleção: apagar a frase da linha 166 inteira; apagar "diz " da linha 60; na linha 135 apagar " e orienta excluir o link e criar outro". A troca mínima "A página avisa que" proposta pela gbq-cqe é recusada por ser texto novo. O procedimento continua na justificativa da 6A-09 ("exclui-se o link e cria-se outro"), e o curso já diz que o lote não o cobra. Linhas 149/273, 195, 212 e 53: manter | AGORA | C-16 |
| D-R1-13 | Avisos 1, 2 e 4 da folha canônica do SIM-0 ausentes da folha do estudante (gbq-cqe achado 10) | adiar: o pacote não tem campo de avisos, e incluí-los exige campo de contrato. O que se compartilha com a candidata é do Fundador | PRÓXIMO | tarefa nova (BLOCO TAREFAS) |
| D-R1-14 | Pares: o separador canônico vira "×"/"—" e cai o ponto final (gbq-cqe achado 7) | adiar a troca de separador. Corrigir já só o defeito do gerador: " — " pendurado quando `como` é vazio (27 linhas: L1 1, L2 9, L3 17) e "× ****" quando `b` é vazio (L3, par 26). Isso é formatação do gerador, não texto canônico, e sai por deleção | AGORA (parte do gerador); BACKLOG (separador) | C-24 |
| D-R1-15 | Parêntese aninhado "(Derep (antigo DETAQ); …)" no L1 (gbq-cqe achado 8) | manter: literal pela F5 (D-T12-V12) | DESCARTADO | — |
| D-R1-16 | Quadro-síntese do L1 desalinhado (gbq-cqe achado 9; DÚVIDA 9) | manter agora; realinhar só com espaços depois | BACKLOG | tarefa nova |
| D-R1-17 | Nota R2 da D4 repetida na D5 (gbq-cqe achado 11) | manter: cópia literal de R2–R4 decidida na T-27; mexer exige errata da GCE | BACKLOG | tarefa nova (informar a GCE) |
| D-R1-18 | 29 justificativas que começam em minúscula depois do prefixo de campo "C — 5.1 —" (gbq-cqe, nota do achado 3) | manter: forma do arquivo canônico, não efeito de deleção | DESCARTADO | — |
| D-R1-19 | Rótulo de alvo errado em 4 linhas da tabela de erratas do relatório (gce-cqfp R4) | aceitar; corrigir na regeração do relatório | AGORA | C-25 |
| D-R1-20 | Explicação da 18.ª justificativa F4 no relatório (gcb-cqfp O-2) | aceitar; as 17 da GBQ são as dos tipos listados, e a 18.ª é a 5C-03 ("R-5C1"). Com D-R1-02 e D-R1-03 a F4 passa a 21 justificativas | AGORA | C-25 |
| D-R1-21 | Remissões a pares por id não exportado ("par C1", "par C14", "C19") (gcb-cqfp O-1) | adiar | BACKLOG | tarefa nova |
| D-R1-22 | O-3 (forma do registro da 5C-06) e O-4 (frase Tukey sobre a banca, literal de decisão do Fundador) (gcb-cqfp) | manter | DESCARTADO | — |
| D-R1-23 | " neste chat" no curso do L4 (5.3.x, PL 2338/2023): marca de processo da mesma natureza das da DÚVIDA 5, achada na verificação desta reconciliação | aceitar; deleção pura na edição; a gbq-cqe confirma na rodada 2 | AGORA | C-23 |

### 2.2 DÚVIDAS do relatório da produção

| DÚVIDA | Decisão | Classe |
|---|---|---|
| 1 — F4: 18 em vez de 17 | aceitar as 18; com D-R1-02 e D-R1-03 passam a 21 (18 + 6B-06, 6B-15, L2-Q21). O "17" do gatilho era aproximado ("entre outras") | AGORA (C-25: relatório) |
| 2 — minúscula depois de "Lição O10: " | autorizada a capitalização (D-R1-04) | AGORA (C-05) |
| 3 — fragmentos dependentes / entradas não desdobradas | aceitar a regra geral; exceções: L1 P2-1.5 e L5 barras/box plot voltam a entrada única (D-R1-05, D-R1-06). Os demais fragmentos se leem sozinhos (inclusive os que começam por minúscula, L1 P2-1.6 e P2-1.8) | AGORA (C-06 a C-08) |
| 4 — rótulo por hierarquia | aceitar (267 rótulos literais; posição conferida pela gbq-cqe e pela gcb-cqfp) | — |
| 5 — marcas fora da lista | decidido item a item na tabela 2.3, sempre por deleção e só na edição do estudante; o pacote conserva as marcas por desenho (dado canônico, D-PACOTE-V11), salvo a F4 | AGORA (C-17 a C-23) |
| 6 — "Risco" | confirmar: as 10 ocorrências que restam são conteúdo de estudo | — |
| 7 — conteúdo substantivo perdido | aceitar as deleções, salvo a L4-11 (D-R1-07, restaurar) | AGORA (C-13) |
| 8 — minúscula e sujeito oculto no L6A | D-R1-11 e D-R1-12 | AGORA (C-15, C-16) |
| 9 — tabelas de colunas fixas | aceitar; realinhamento BACKLOG (D-R1-16) | BACKLOG |
| 10 — aviso único para REVERIFICAR normativo | aceitar o aviso fixo; sai da justificativa da L3-Q21 a classificação interna que o contradiz (tabela 2.3, f) | AGORA (C-21) |
| 11 — aderência no gabarito do estudante | manter só no gabarito, não na folha (informa D-ADERENCIA); o que se compartilha é do Fundador | — |
| 12 — quarto estado "FORA DO PACOTE" | aceitar como rótulo de relatório (não é campo do pacote); as 6 classificações foram confirmadas pela gce-cqfp | — |
| 13 — alvo duplicado da E3a do L3 | aceitar sem consulta à GCE: a E3 delimita o alvo (4.1 e Q20), e o resultado foi conferido pela gbq-cqe e pela gce-cqfp | — |

### 2.3 DÚVIDA 5, item a item (edição do estudante; só deleção)

| Item | Marca | Decisão | Correção |
|---|---|---|---|
| a | "(v2, …)" em `L1C_estudo.md` 49 e 52 | apagar "v2, " | C-17 |
| b | " (D-LEI-15352)" na nota de BQ-0003 (`BANCO_itens.md` 41, `BANCO_gabarito.md` 14, `SIM-0_folha.md` 158, `SIM-0_gabarito.md` 178) | apagar só na edição. Exceção à regra (i), que fica registrada para a errata do contrato (tarefa nova). No pacote a nota fica literal | C-18 |
| c | "aberta(s) hoje" (carimbo de leitura): L6A 31 e 188; L6B 142, 163, 170, 175, 187 e 245; `L6B_gabarito.md` 31 (6B-06) | apagar (lista de 9 alvos; a gbq-cqe listou 6, e 3 da mesma forma foram achados nesta verificação) | C-19 |
| d | Códigos de fonte do L5 (U1–U6, GG4, TB2, CI) e "(verificado em 8/10/2026)"/"Verificado em 8/10/2026." | apagar (mesma natureza das F1…F22) | C-20 |
| e | Códigos N do L2 e do L3 (N1–N7) | apagar quando são só remissão; manter N1–N4 do L4 (definidos no texto: "LGPD (N1, Lei 13.709/2018)") | C-22 |
| f | Classificação interna nas justificativas: L2-Q23 "; NÃO VOLÁTIL"; L3-Q21 " REVERIFICAR (normativo) 04–08/01/2027; não VOLÁTIL."; L4-05 " Sem marca VOLÁTIL: o item afirma o conceito, não recurso de produto." | apagar (o aviso fixo cobre a reverificação; na L3-Q21 a classificação contradiz o aviso) | C-21 |
| g | "VOLÁTIL" em títulos do curso (L4, L5, L6A) | manter (orientação de estudo) | — |
| h | Etiquetas de mecanismo GI/TC/IC/AT sem legenda | manter. A legenda literal do (d-G) canônico ("Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC)") é texto que não está no pacote: entra como campo opcional de lote na errata do contrato | PRÓXIMO (tarefa nova) |
| i | "que eu possa afirmar" (L3, curso 4.x, "CONTROVERSO / NÃO GABARITO") | manter: a deleção tornaria a afirmação absoluta; é texto canônico da GCE | BACKLOG (informar a GCE) |

## 3. LISTA DE CORREÇÕES AGORA (para a gbq-csc)

### 3.0 Regras de execução

1. Antes de tudo, copiar o estado R0 para o scratchpad (`s4/t48r1/r0/`: `pacote.json`, `pacote_relatorio_2026-10-13.md`, `saida/estudante/`) e trabalhar sobre cópias dos scripts em `s4/t48r1/` (os de `s4/t48/` ficam intactos como prova da R0).
2. Corrigir o gerador e regenerar. Não editar à mão `pacote.json` nem os arquivos de `saida/estudante/`. Saídas: `saida/pacote/pacote.json` (mesmo caminho, `versao` 1, `nome` "Câmara 2026 — pacote F4 (v1.2)", `geradoEm` 2026-10-13), `saida/estudante/` (os mesmos 43 nomes), `saida/pacote/pacote_relatorio_2026-10-13.md` regenerado e `saida/pacote/T48_correcao_R1_2026-10-13.md` (relatório da rodada: correção a correção, antes → depois, diff R0 → R1 e saída dos validadores).
3. Vedado: mudar enunciado, comando, `comandoOriginal`, `textoBase`, gabarito, itemEdital, aderência, `volatil`, `nota` do pacote, rótulos, ordem e `n` dos simulados, ou qualquer arquivo canônico de lote, `banco/`, `regras/`, `TAREFAS.md`, `DECISOES.md`, `PARA_PRESIDENCIA.md` e `estado/`. Nada é commitado.
4. A regra de "só deleção" continua valendo, com duas exceções fechadas: (i) a lista CAIXA (C-05 e C-15), em que a única mudança é minúscula → maiúscula na primeira letra indicada; (ii) a reunião de fragmentos de pegadinha (C-06 a C-08), em que o texto novo é a junção literal dos fragmentos com "; ". O validador de fidelidade (`estudante_fidelidade.py`) e o validador F4 passam a aceitar exatamente essas exceções, listadas, e nada além delas.

### 3.1 pacote.json (propaga à edição do estudante na regeração)

| C | Campo / id | Texto atual (literal) | Texto novo (literal) | Onde corrigir |
|---|---|---|---|---|
| C-01 | `justificativa` 4C-09 | `… como contexto. Retificação 6-A: a redação "sem acesso a busca" não excluía outras ferramentas; "ferramentas externas (como a busca)" alinha o item ao curso 5.3.3 ("sem ferramentas ou RAG"). O acréscimo "e sem retreinamento" …` | `… como contexto. O acréscimo "e sem retreinamento" …` (deleção de ` Retificação 6-A: … ("sem ferramentas ou RAG").`, com o espaço inicial) | `f4.py`, `F4_DEL['4C-09']`: 2.º trecho |
| C-02 | `justificativa` 6B-06 | `… com outro ponto de julgamento (seção ITENS REAIS, conferida pela QA em 08/10/2026).` | `… com outro ponto de julgamento (seção ITENS REAIS).` | `f4.py`, entrada nova |
| C-03 | `justificativa` 6B-15 | `… → marcar E). Curso 4.3.4 (corrigido pela O-3): HTTPS é o HTTP …` | `… → marcar E). Curso 4.3.4: HTTPS é o HTTP …` | `f4.py`, entrada nova |
| C-04 | `justificativa` L2-Q21 | `… traduz as notas estenotípicas em texto [F7]. Gabarito E mantido.` | `… traduz as notas estenotípicas em texto [F7].` | `f4.py`, entrada nova |
| C-05 | `justificativa` 4C-08 e 5C-06 (CAIXA) | 4C-08: `(conceito geral, sem fonte de fornecedor, como no curso). Lição O10: o item não depende` · 5C-06: `termine no mínimo da amostra. Lição O10: a regra de 1,5 · AIQ` | 4C-08: `(conceito geral, sem fonte de fornecedor, como no curso). O item não depende` · 5C-06: `termine no mínimo da amostra. A regra de 1,5 · AIQ` | `f4.py`: trocar a deleção `'Lição O10: '` pelo par (`'Lição O10: o item'` → `'O item'`; `'Lição O10: a regra'` → `'A regra'`), cada um com 1 ocorrência |
| C-06 | `lotes[L1].pegadinhas`, P2-1.5 | 2 entradas: `Dizer que a pontuação automática "detecta os sinais pronunciados" (isso é pontuação falada). Dizer que capitalização automática identifica nomes próprios "com certeza" — ela estima` e `"Câmara" (instituição) vs "câmara" (sala) é decisão de contexto que o modelo pode errar.` | 1 entrada `{"itemEdital": "P2-1.5", "rotulo": "Pontuação automática e capitalização em transcrições", "texto": "Dizer que a pontuação automática \"detecta os sinais pronunciados\" (isso é pontuação falada). Dizer que capitalização automática identifica nomes próprios \"com certeza\" — ela estima; \"Câmara\" (instituição) vs \"câmara\" (sala) é decisão de contexto que o modelo pode errar."}` | `peg.py`: lista de não desdobramento (entrada que fica única), com motivo "ilustração do fragmento anterior" |
| C-07 | `lotes[L5].pegadinhas`, Gráfico de barras (colunas) | 2 entradas: `usar para distribuição de variável contínua agrupada em classes` e `empilhado quando se quer comparar as partes entre si.` | 1 entrada `{"itemEdital": "P1-8.2", "rotulo": "Gráfico de barras (colunas)", "texto": "usar para distribuição de variável contínua agrupada em classes; empilhado quando se quer comparar as partes entre si."}`. As entradas "confundir com histograma" e "aceitar eixo truncado" ficam como estão | `peg.py`: junção dos fragmentos que dependem do verbo do anterior |
| C-08 | `lotes[L5].pegadinhas`, Box plot (diagrama de caixa) | 4 entradas: `dizer que a linha central é a média` · `que a caixa vai do mínimo ao máximo ou contém todos os dados` · `que os bigodes vão até 1,5 desvio padrão` · `que mostra frequência por intervalo (isso é histograma).` | 1 entrada `{"itemEdital": "P1-8.2", "rotulo": "Box plot (diagrama de caixa)", "texto": "dizer que a linha central é a média; que a caixa vai do mínimo ao máximo ou contém todos os dados; que os bigodes vão até 1,5 desvio padrão; que mostra frequência por intervalo (isso é histograma)."}` | `peg.py`: idem |
| C-09 | validador F4 (`validate.py`) | padrões sem `QA` nem `O-n` | acrescentar `(?<!NORMATIVO — )\bQA\b`, `\bO-\d+\b`, `Retificação` e `[Gg]abarito [CE] mantido`; esperado 0 ocorrência nas 180 justificativas AUTORAL | `validate.py` |

Efeito esperado no pacote, de R0 para R1: só mudam `justificativa` de 6 itens (4C-08, 4C-09, 5C-06, 6B-06, 6B-15, L2-Q21) e `pegadinhas` de L1 (20 → 19) e L5 (52 → 48). Total de pegadinhas 267 → 262. Justificativas alteradas de v1.1 para v1.2: 21. Todos os demais campos, os 286 itens, os simulados, as discursivas e o edital ficam idênticos à R0. A junção de cada entrada reunida é igual à entrada da v1.1, salvo o ponto final.

### 3.2 Edição do estudante (gerador `estudante_gen.py`, `estudante_marcas.py`, `literais.py`)

| C | Arquivo / ponto | Texto atual (literal) | Texto novo (literal) ou regra | Onde corrigir |
|---|---|---|---|---|
| C-10 | `SIM-0_folha.md`, `SIM-1_folha.md`, `SIM-2_folha.md`, `SIM-0-P2_folha.md`: as 165 linhas de item | `**1** — L3-Q25 — Os direitos morais…` (modelo `**{n}** — {id} — {enunciado}`) | `**1** — Os direitos morais…` (modelo `**{n}** — {enunciado}`); o id fica só nos `*_gabarito.md` | `estudante_gen.py`, emissão da linha de item da folha |
| C-11 | `BANCO_itens.md` (BQ-0049, 0050, 0051) e `SIM-0_folha.md` (bloco do item 12) | linha `**Comando.** A partir da situação hipotética precedente, …` antes de `**Texto-base.** Uma empresa recebe …` | `**Texto-base.** …` (e a linha em branco) antes de `**Comando.** …`, sem mudar palavra. Regra: em todo ponto de emissão (banco, folhas, `*_itens.md`), o texto-base vem antes do comando | `estudante_gen.py`: os 3 pontos de emissão |
| C-12 | `L4_estudo.md` 224 (curso 6.5, P3) e 283 (pegadinha P1-6) | `… o § 3º da Lei 13.853/2019 foi vetado;).` | `… o § 3º da Lei 13.853/2019 foi vetado).` | `estudante_marcas.py`, `GENERIC`: pôr a regra `;[ \t]*conferid…(?=\))` antes da regra `,? conferid…(?=\))` (ou trocar o prefixo desta por `[,;]?`); deleção pura |
| C-13 | `L4_gabarito.md`, L4-11 (restauração, D-R1-07) | `GI invertida (tentação: "prioritariamente supervisionado"). O item descreve o pré-treino como …` | `GI invertida (tentação: "prioritariamente supervisionado"). O F4 afirma que "generative models are initially trained using an unsupervised approach" e que "the model is sometimes trained further using supervised or reinforcement learning"; o item descreve o pré-treino como "sem rótulos atribuídos manualmente", sem classificar o "auto-supervisionado". Mecanismo semelhante: TRF6 2024, Cargo 2, item 81 (CEBRASPE_ANALOGA; gabarito definitivo E, conferido no GAB_DEFINITIVO_034_TRF6_002_01) — referência, não fundamento.` Isto é a justificativa do pacote menos só ` Fonte: F4, reverificado em 7/10/2026.` | `literais.py`: retirar a regra literal nº 6 do apêndice A (`'). O ⟦F4 afirma que … ; o ⟧item descreve'`) |
| C-14 | regras literais sem objeto depois de C-02/C-03 | nº 26 `Curso 4.3.4⟦ (corrigido pela O-3)⟧:` e nº 63 `seção ITENS REAIS⟦, conferida pela QA em 08/10/2026⟧)` | retirar as duas regras (o gerador aborta quando uma regra literal não ocorre); o resultado na edição é o mesmo da R0 | `literais.py` |
| C-15 | `L6A_estudo.md` (CAIXA, lista fechada; 1 ocorrência cada) | 56 `mesclar combina duas ou mais células` · 88 `a função SE compara um valor` · 92 `o PROCV pesquisa um valor` · 112 `o propósito é fazer todos os slides` · 115 `a animação é aplicada a um único elemento` · 139 `o histórico de versões permite ver` · 163 `deleted". por padrão os clientes POP3` · 164 `offline. por padrão os clientes IMAP4` | `Mesclar combina…` · `A função SE…` · `O PROCV…` · `O propósito…` · `A animação…` · `O histórico de versões…` · `deleted". Por padrão os clientes POP3` · `offline. Por padrão os clientes IMAP4` | `estudante_marcas.py`: fase nova CAIXA, depois de `strip_text`, com estes 8 pares; cada par garante 1 ocorrência e diferença de 1 caractere (minúscula → maiúscula) |
| C-16 | `L6A_estudo.md` (deleção) | (a) 166 `portas e criptografia do Exchange Online; esses números são específicos de produto e NÃO são cobrados.` (no pacote: `A F14 lista portas e criptografia do Exchange Online; …` em linha própria) · (b) 60 `(diz "não estão formatados como cabeçalhos", …` · (c) 135 `(de edição para exibição ou o contrário) e orienta excluir o link e criar outro. As duas páginas` | (a) a linha inteira some, com a quebra de linha que a precede; a linha seguinte é a linha em branco antes de `### 3.1.3` · (b) `("não estão formatados como cabeçalhos", …` · (c) `(de edição para exibição ou o contrário). As duas páginas` | `literais.py`: (a) a regra nº 51 passa a apagar `\nA F14 lista portas e criptografia do Exchange Online; esses números são específicos de produto e NÃO são cobrados.`; (b) a regra nº 42 passa a apagar `a F3 diz ` (fica `(⟦a F3 diz ⟧"não estão…`); (c) a regra nº 44 estende a deleção a ` e orienta excluir o link e criar outro` |
| C-17 | `L1C_estudo.md` 49 e 52 (DÚVIDA 5-a) | `(v2, item 1.4)` · `(v2, exemplo parlamentar do 1.4)` | `(item 1.4)` · `(exemplo parlamentar do 1.4)` | `literais.py`: 2 regras |
| C-18 | nota de BQ-0003 na edição (DÚVIDA 5-b): `BANCO_itens.md` 41, `BANCO_gabarito.md` 14, `SIM-0_folha.md` 158, `SIM-0_gabarito.md` 178 | `…, redação da Lei 15.352/2026 (D-LEI-15352); texto do item mantido literal` | `…, redação da Lei 15.352/2026; texto do item mantido literal` | `estudante_gen.py`/`estudante_marcas.py`: deleção de ` (D-LEI-15352)` aplicada só à exibição da `nota`; o validador de fidelidade aceita exatamente essa diferença na nota de BQ-0003 |
| C-19 | "aberta(s) hoje" (DÚVIDA 5-c), 9 alvos | L6A 31 `Nas páginas de suporte abertas hoje, a Microsoft` · L6A 188 `(conceito geral; sem fonte aberta hoje para detalhes; sem item)` · L6B 142 `(conceito geral; sem base aberta hoje)` · L6B 163 `Fontes abertas hoje: "Faça backups` · L6B 170 `uma fora do local), sem fonte aberta hoje e sem item.` · L6B 175 `Definição de vírus aberta hoje: "programa` · L6B 187 `Definição de ransomware aberta hoje: "Ransomware` · L6B 245 `Definição aberta hoje: o phishing` · `L6B_gabarito.md` 31 (6B-06) `não foi confirmada em fonte aberta hoje; ver curso 4.1.1` | `Nas páginas de suporte, a Microsoft` · `(conceito geral; sem item)` · `(conceito geral)` · `Fontes: "Faça backups` · `uma fora do local), sem item.` · `Definição de vírus: "programa` · `Definição de ransomware: "Ransomware` · `Definição: o phishing` · `não foi confirmada em fonte; ver curso 4.1.1` | `literais.py`: 9 regras de deleção |
| C-20 | Códigos do L5 (DÚVIDA 5-d): `L5_estudo.md` 24, 109–113, 117–119, 123–127, 131; `L5_gabarito.md` 71, 78, 85, 92 | ex.: `Power BI (Microsoft) — fonte principal U1 en-us; U2 só para a natureza Windows do Desktop (verificado em 8/10/2026)`; `Família de produtos (U3):`; `("no-cost", U4)`; `(U4, seção "Upgrade to Data Studio Pro"; U6: "Data Studio Pro is designed for scaling teams"; anunciada como Looker Studio Pro em 11/10/2022, GG4)`; `(TB2, módulo "Data Presentation…")`; `Três componentes e fluxo conforme U1 en-us (…); natureza Windows do Desktop conforme U2. Verificado em 8/10/2026.` | Regras, só nos campos do L5 (curso, resumo, justificativas A5): (1) literais: apagar ` — fonte principal U1 en-us; U2 só para a natureza Windows do Desktop (verificado em 8/10/2026)`, ` — U3; dashboards por TB2 (verificado em 8/10/2026)`, ` — U4, U5, U6, GG4 (verificado em 8/10/2026)`, `; verificado em 8/10/2026` (resumo 8.3), ` conforme U1 en-us` e ` conforme U2` (A5-14); (2) genéricas: `LEAD + \((?:U\d|GG\d|TB\d)(?:, (?:U\d|GG\d|TB\d))*\)` → apagar; `, (?:U\d|GG\d)(?=\))` → apagar; `(?<=\()(?:U\d|TB\d), ` → apagar; `(?<=; )U\d: ` → apagar; ` Verificado em 8/10/2026\.` → apagar. Resultados obrigatórios: títulos `Power BI (Microsoft)`, `Tableau (Salesforce)`, `Data Studio (Google)`; A5-14 = `Três componentes e fluxo ("three primary components"; Desktop = "development tool"; serviço "allows you to organize, manage, and distribute"); natureza Windows do Desktop.`; A5-15 = `TC (descontinuado no lugar de renomeado). Em 11/10/2022 o Data Studio foi renomeado Looker Studio ("Data Studio is now Looker Studio"), não descontinuado; em abril de 2026 o nome voltou a ser Data Studio, nome vigente.`; A5-16 = `Public "A free platform to explore, create, and publicly share"; Server "A self-hosted platform"; Cloud "A fully hosted cloud-based" platform.`; A5-17 = `IC (fluxo invertido). "First, you start with Power BI Desktop to connect to data and create the report. Then you publish the report to the Power BI service".`; 0 ocorrência de `\b(U[1-6]|GG\d|TB\d|CI)\b` e de `erificado em 8/10/2026` em `L5_*.md` | `estudante_marcas.py` + `literais.py` |
| C-21 | Classificação interna (DÚVIDA 5-f) | L2-Q23 (`L2_gabarito.md` 116, `SIM-0-P2_gabarito.md` 114): `Depende de padrão técnico estável, não de produto; NÃO VOLÁTIL.` · L3-Q21 (`L3_gabarito.md` 106): `… passou a ser exercida por ela. REVERIFICAR (normativo) 04–08/01/2027; não VOLÁTIL.` · L4-05 (`L4_gabarito.md` 26): `… e OpenAI, "Message formatting with Markdown and XML". Sem marca VOLÁTIL: o item afirma o conceito, não recurso de produto.` | `Depende de padrão técnico estável, não de produto.` · `… passou a ser exercida por ela.` · `… e OpenAI, "Message formatting with Markdown and XML".` | `literais.py`: 3 regras |
| C-22 | Códigos N do L2 e do L3 (DÚVIDA 5-e) | L2: 36 `(N1)` e `(N2)`; 75 `[Ver N5: definição de uso corrente; sem fonte oficial verificada.]`; 179 `Câmara (N2):`; 218 `de 2026 (N1);`; 229 `instituições (N2);`; 280 `verificado (N2).`; 320 `produto; ver N3):` · L3: 100 e 575 `(N6: não cobrar descrição de sistema real.)`; 172 `verificado (N6);`; 240 `(N5). A banca`; 422 `(N4; não há texto legal`; 438 `verificada — N7):` | `[definição de uso corrente; sem fonte oficial verificada.]`; `Câmara:`; `de 2026;`; `instituições;`; `verificado.`; `produto):`; `(não cobrar descrição de sistema real.)`; `verificado;`; `verificados. A banca`; `(não há texto legal`; `verificada):`. Regras só nos campos de L2 e L3: `LEAD + \(N\d\)` → apagar; `; ver N\d(?=\))` → apagar; `Ver N\d: ` → apagar; `(?<=\()N\d[:;] ` → apagar; ` — N\d(?=\))` → apagar. L4 não muda (N1–N4 ficam) | `estudante_marcas.py` (escopo L2/L3) |
| C-23 | `L4_estudo.md` 210 (D-R1-23) | `(marco legal da IA; situação de tramitação não verificada neste chat)` | `(marco legal da IA; situação de tramitação não verificada)` | `literais.py`: 1 regra |
| C-24 | pares com `como` ou `b` vazio (D-R1-14) | 27 linhas terminadas em ` — ` (L1 466; L2 9; L3 17) e `- **Confidencialidade, integridade, disponibilidade** × **** — ` (L3 565) | sem ` — ` quando `como` é vazio; sem ` × **…**` quando `b` é vazio: `- **Tradução (whisper-1, só para inglês)** × **transcrição (idioma original)**` · `- **Confidencialidade, integridade, disponibilidade**` | `estudante_gen.py`, emissão dos pares |

### 3.3 Relatório

| C | Objeto | Correção |
|---|---|---|
| C-25 | `pacote_relatorio_2026-10-13.md` (regenerado) | (1) seção 3, coluna "Alvo" (gce-cqfp R4): L1 E4c → `(d-G) Q01 (justificativa): …`; L1C E3 → `(d) Q23 (enunciado): …`; L3 E1b → `resumo (b), linha 4.1: …`; L3 E3b → `(d-G) Q20 (justificativa): …`. (2) Seção 6 e DÚVIDA 1 (gcb-cqfp O-2): onde se lê "Pode-se contar 17 se A5-14 a A5-17 forem tomados como um bloco de 3 ou se a L2-Q23 não for contada", leia-se "As 17 da GBQ são as justificativas com os tipos de marca que ela listou (CQFP, "(v3 — O12)", "(O1)", "Lição O10", "R-4C1", "Risco"); a 18.ª é a 5C-03 ("R-5C1", mesma classe de R-4C1); com a rodada R1 (6B-06, 6B-15, L2-Q21) a F4 soma 21". (3) Seções 2, 5, 6, 8, 9, 10 e 11 com as contagens da R1 (F4 21; pegadinhas L1 19, L5 48, total 262; marcas removidas; varreduras). (4) Seção 12: cada DÚVIDA remete à decisão desta reconciliação. (5) Seção nova "13. Rodada de correção R1", que remete a `T48_correcao_R1_2026-10-13.md` |

### 3.4 Validação da produção (antes de entregar à gbq-cqe)

- Os 102 testes da R0 refeitos, ajustados só nas contagens da R1, com 0 falha.
- `estudante_fidelidade.py` com 0 diferença, só com as exceções do item 3.0.4 e da C-18.
- Diff R0 → R1 do pacote igual ao "efeito esperado" da seção 3.1.
- Diff R0 → R1 da edição, linha a linha, contido nas linhas C-01 a C-24, mais o rearranjo de linhas das C-11 e C-16(a) e as entradas reunidas de C-06 a C-08.
- Varreduras na edição com 0 ocorrência em todas: `;)`, ` — $`, `\*\*\*\*`, `abertas? hoje`, `(v2,`, `D-LEI-15352`, `neste chat`, `Retificação`, `Gabarito [CE] mantido`, `\b(U[1-6]|GG\d|TB\d|CI)\b`, `\bN\d\b` nos arquivos L1*, L1C*, L2*, L3*, SIM-2* e SIM-0-P2*, e ` — (BQ|L\d|4C|5C|6A|6B|A5)` nas folhas.
- Códigos F: só `a tecla F4` (L6A) e `O F4 afirma` (L4-11).
- "VOLÁTIL" fora do aviso fixo: só em títulos e rubricas de curso e resumo.

## 4. Pontos que NÃO mudam (para evitar retrabalho)

- Pacote: as marcas de processo de curso, resumo, pegadinhas e justificativas fora da F4 ficam por desenho (dado canônico; D-PACOTE-V11). A nota de BQ-0003 fica literal com "(D-LEI-15352)" (regra (i)).
- Edição: GI/TC/IC/AT, "VOLÁTIL" em títulos, N1–N4 do L4, aderência no gabarito, aviso fixo único, "(Derep (antigo DETAQ); …)", 29 justificativas iniciadas em minúscula após o prefixo de campo, separadores dos pares e quadro-síntese do L1.

## 5. Roteiro da rodada 2 de QA (gbq-cqe)

Objeto: `pacote.json` R1, `saida/estudante/` R1, `pacote_relatorio_2026-10-13.md` R1 e `T48_correcao_R1_2026-10-13.md`. Base de comparação: R0 (cópia da gbq-csc em `s4/t48r1/r0/`, conferida pelo SHA-256 `ae2f346830f8` do pacote) e os arquivos canônicos. Scripts próprios; os da produção não servem de prova.

1. Integridade do pacote, refazendo `q1_integridade.py` e `q2_ponto11.py`, com 0 falha. Diff R0 → R1 por campo: só `justificativa` de 4C-08, 4C-09, 5C-06, 6B-06, 6B-15 e L2-Q21, e `pegadinhas` de L1 e L5. 286 itens, 60 C / 46 E no banco e 89 C / 91 E no AUTORAL. Simulados, discursivas e edital idênticos à R0.
2. Cada correção C-01 a C-08 contra o literal da seção 3.1. Nas 6 justificativas: só deleção, mais as 2 trocas de caixa. Nas pegadinhas reunidas: junção = entrada da v1.1 (salvo o ponto final). Contagens: L1 19, L5 48, total 262. Os demais fragmentos ficam inalterados entrada a entrada.
3. Varredura F4 nas 180 justificativas do pacote: 0 marca de tramitação (padrões da C-09 e os da R0).
4. Fidelidade da edição, refazendo `q3_fidelidade.py` e `q6_banco_sim.py`:
   - inserções = só as erratas oficiais já aceitas na rodada 1, mais as 10 trocas de caixa (C-05 e C-15) e a restauração da L4-11 (C-13);
   - deleções novas = só as das C-12, C-16 a C-23;
   - 165/165 posições dos simulados com texto e gabarito iguais aos canônicos.
5. C-10 e C-11: 165 linhas de item das folhas sem id, e o id presente nos `*_gabarito.md`. Ordem texto-base → comando em `BANCO_itens.md` (3) e `SIM-0_folha.md` (1). Nenhuma outra ordem mudou.
6. C-13: a justificativa da L4-11 na edição é igual à do pacote menos exatamente ` Fonte: F4, reverificado em 7/10/2026.`, e o gabarito C continua fundamentado.
7. Leitura de 100% das linhas alteradas da edição (diff R0 → R1): gramática, sentido e nenhuma afirmação nova. Atenção especial a L6A 135 e 166, L5 109–131 e A5-14 a A5-17, e L2/L3 nos pontos dos códigos N.
8. As varreduras da seção 3.4, com os resultados lá exigidos.
9. Relatório: C-25 (1)–(5), com contagens iguais às do pacote R1.
10. Fechamento das ressalvas da rodada 1:
    - gce-cqfp: R1–R4;
    - gcb-cqfp: A-1 a A-5 e O-2;
    - gbq-cqe: achados 1–4, 5, 6 (salvo os itens mantidos em 2.3) e a parte AGORA do 7.

    Não é preciso nova rodada da gce-cqfp nem da gcb-cqfp: nenhuma errata nem texto canônico de lote mudou.
11. Veredito: APROVADO/CONFERIDO ou CORRIGIR, com lista literal. Gate se a reprovação passar de 30%.

## 6. T-50 — regras/estilo_banca.md v1.1.3

Conferência da gerência, por script e somente leitura:
- SHA-256: antes `530c580d…2517` (igual ao "depois" da T-37), depois `9f9237f5…4caf`, iguais aos do relatório.
- `diff`: só as linhas 1–2, 6–7, 117 e 245, mais a subseção nova "### v1.1.2 → v1.1.3 (T-50)" na seção 7.
- As duas frases novas fixadas pela D1 (3-b) ocorrem literalmente: 1 vez no corpo e 1 vez na citação da seção 7.
- As frases antigas ficam só na citação histórica da seção 7.
- AVISO final inalterado. 12 contagens de padrão e somas 27 E / 33 C mantidas, conforme o script da gbq-estilo.
- As atribuições (T-13 para BQ-0006, 0024, 0037 e 0056; T-21 para BQ-0036; 10/10/2026) conferem com os relatórios do qa-normativo.

Decisão: T-50 reconciliada, sem ressalva. **Estado proposto: CONCLUÍDA** (ciclo 2026-10-13, reconciliada pela GBQ em T48_reconciliacao_R1_2026-10-13.md, seção 6). O nome do relatório (`T50_estilo_v1_1_3_2026-10-13.md` em vez de `T_estilo_v1_1_3_<data>.md`) fica aceito.

## 7. Estado proposto da T-48

EM CURSO: rodada 1 de QA reconciliada em 13/10 (T48_reconciliacao_R1_2026-10-13.md). Próximos passos: correção R1 pela gbq-csc (C-01 a C-25), depois QA da rodada 2 pela gbq-cqe, depois reconciliação da GBQ e gatilho A da v1.2. Classe AGORA mantida.

## BLOCO TAREFAS

T-?; GBQ; Errata de forma de regras/pacote_contrato.md (v1.1.1 + Regras da v1.2 → v1.2.1; D1 GBQ, saida/pacote/T48_reconciliacao_R1_2026-10-13.md, D-R1-05/06/09/13 e 2.3-b/h), sem mudar campo obrigatório nem "versao": (1) regra (b): quando houver `textoBase`, a plataforma e a edição do estudante o exibem antes do `comando`; (2) regra (d): fragmento que só se lê com o verbo ou o sujeito do fragmento anterior, ou que é ilustração do anterior, não é fronteira de desdobramento (casos: L1 P2-1.5; L5 Gráfico de barras e Box plot); (3) regra (i): na edição do estudante a `nota` sai sem id de decisão entre parênteses ("(D-LEI-15352)"); no pacote continua literal; (4) campo opcional de lote `legendaMecanismo` (literal da legenda do (d-G) canônico: "Mecanismo: troca de conceito (TC), generalização indevida (GI), …"), exibido no topo dos `*_gabarito.md`; (5) campo opcional de simulado `avisos` (literais da folha canônica; SIM-0: avisos 1, 2 e 4), sem decidir exibição à candidata (matéria do Fundador); aplicação na próxima regeração (T-12); PRÓXIMO; PENDENTE; gbq-csc → gbq-cqe → gbq-gerencia; regras/pacote_contrato.md v1.2.1 + saida/pacote/contrato_v1_2_1_<data>.md

T-?; GBQ; Forma da edição do estudante, resíduos da T-48 (D1 GBQ, T48_reconciliacao_R1_2026-10-13.md, D-R1-14/16/17/21 e 2.3-i), sem mudar texto canônico: (1) pares: separador canônico ("vs", ":", "|") e ponto final do arquivo do lote no lugar de "×"/"—" (gbq-cqe achado 7); (2) quadro-síntese do L1 realinhado só com espaços (achado 9); (3) remissões a pares por id não exportado ("par C1" em A5-09 e 5C-03, "par C14" em 5C-07, "C19" em 4C-08): campo opcional `id` de par ou deleção (gcb-cqfp O-1); (4) rótulo "Nota: nota de vigência:" duplicado na exibição da nota (gerador); (5) informar à GCE, para eventual errata dela: nota R2 da D4 repetida na D5 (achado 11) e "que eu possa afirmar" no curso do L3 ("CONTROVERSO / NÃO GABARITO"); BACKLOG; PENDENTE; gbq-csc → gbq-cqe → gbq-gerencia; saida/estudante/ + saida/pacote/estudante_forma_<data>.md

## BLOCO PARA_PRESIDENCIA

nenhum. O gatilho A da v1.2 só sai depois do veredito da rodada 2 e da reconciliação da GBQ.
