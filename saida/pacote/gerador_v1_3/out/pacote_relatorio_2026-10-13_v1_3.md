# pacote_relatorio_2026-10-13_v1_3.md — T-56 — EXPORTAR v1.3 — 2026-10-13 — gerado por gbq-csc

Saídas: `saida/pacote/pacote.json` (versao 1, nome "Câmara 2026 — pacote F4 (v1.3)", geradoEm 2026-10-13, 620956 bytes UTF-8, SHA-256 `fdcb7afdb4fb449229c6d530e877d839f8d334cd9667731e1b7222c9c7fb0eca`, indent=1, newline final), este relatório (gerado por inteiro pelo gerador, `relatorio_v1_3.py`, N-3) e a edição do estudante em `saida/estudante/` (43 arquivos). Contrato: `regras/pacote_contrato.md` v1.2.1 (inclusive a "Errata de forma da v1.2.1") + Regras da v1.2 (a–j) e as D1 da GBQ em `saida/pacote/T48_reconciliacao_R2_2026-10-13.md`, seção 2 (D-T53-01 a D-T53-08 e D-R2-01 a D-R2-06). Escopo desta ocorrência: D-V13-AGORA (Fundador, 13/10/2026) = lista PARA A PRÓXIMA T-12 (reconciliação R2, seção 4, itens 1 a 5) e pontos de caminho da `T55_conferencia_2026-10-13.md`, seção 4. Gerador: `saida/pacote/gerador_v1_3/` (cópia alterada de `gerador_v1_2/`, que ficou intacto). Nada foi commitado; TAREFAS.md, PARA_PRESIDENCIA.md, DECISOES.md, estado/, banco/, regras/ e os canônicos dos lotes não foram alterados. A v1.2 (SHA-256 `f46ed9f8e43db76aaeb96eda0b2924028fb7145c048c5eb0189396c9f67304fe`, 618673 bytes) foi guardada antes de ser sobrescrita e é lida do git (commit 2684ab1). Nada deste pacote nem da edição do estudante vai à candidata sem decisão do Fundador; a edição do estudante NÃO é entrega à candidata (a entrega da v1.2 foi decidida em D-ENTREGA-V12-A; a da v1.3 continua reservada ao Fundador).

Resultado em uma linha: **286 itens** (106 de banco + 180 AUTORAL), 10 lotes (6 com `legendaMecanismo`), 5 discursivas, 4 simulados com `n` e `versao` (SIM-0 com `avisos`); 32 registros de errata (31 APLICADA, 1 JÁ PRESENTE, 0 NÃO ENCONTRADA) e 6 erratas com alvo fora do pacote; validação por script: 107 verificações, 0 falhas; conferências da ocorrência: 91, 0 falhas; edição do estudante: 43 arquivos, fidelidade textual 5650 comparações, 0 diferenças. Diff v1.2 → v1.3 do pacote: só `nome` e os campos novos `legendaMecanismo` (6 lotes) e `avisos` (SIM-0); da edição: só N-1 (`L6B_estudo.md`), a legenda no topo de 6 `*_gabarito.md` e a versão no README.

## 1. Fontes

Lidas em 13/10/2026 (SHA-256, 12 primeiros dígitos). O arquivo canônico de cada lote é o da tabela de fonte do contrato (regra 4 da v1.1); os `saida/lote*/RECONCILIADO.md` não existem e não são fonte.

| Objeto | Arquivo(s) | Versão / observação | SHA-256 (12) |
|---|---|---|---|
| Contrato | `regras/pacote_contrato.md` | v1.2.1 (Errata de forma, T-53) + Regras da v1.2 (a–j) + v1.1.1 + v1.1 | `47e3c290646f` |
| Instruções da T-48 | `saida/banco/GBQ_reconciliacao_2026-10-13.md` | seção "INSTRUÇÕES PARA A T-48" e D1-a/b/c | `1c9c364c3d8a` |
| Escopo da T-56 | `saida/pacote/T48_reconciliacao_R2_2026-10-13.md` | seção 2 (D1: D-T53-01 a 08, D-R2-01 a 06) e seção 4 (PARA A PRÓXIMA T-12, itens 1 a 5) | `44520d71c295` |
| Escopo da T-56 | `saida/pacote/T55_conferencia_2026-10-13.md` | seção 4 (pontos de caminho do gerador) | `cb9738787cbd` |
| Tabela 2.3 (legendas) | `saida/pacote/QA_T53_2026-10-13_gbq-cqe.md` | literais de legendaMecanismo por lote e dos avisos | `6ee99e3a9acd` |
| Varreduras 3.5 | `saida/pacote/QA_T48_R2_2026-10-13_gbq-cqe.md` | seção 3.5 (varreduras de não regressão) e N-1 | `76e1600a36e4` |
| Reconciliação R1 | `saida/pacote/T48_reconciliacao_R1_2026-10-13.md` | D-R1-xx e C-01 a C-25 (exceções fechadas) | `c6aa45d25842` |
| L1 | `saida/gce/GCE_Lote1_v2_CPP.md` | v2 canônico; erratas pela consolidação | `5ac069292b12` |
| L1 | `saida/gce/GCE_Lote1_consolidacao_GCE.md` | E1–E12 (Adendos 1–5); padrão D1 | `8304882d57c6` |
| L1C | `saida/gce/GCE_Lote1C_v2_CPP.md` | v2 canônico | `a25e6e0b6298` |
| L1C | `saida/gce/GCE_Lote1C_consolidacao_GCE.md` | E1–E4 | `eb1ca37bee12` |
| L2 | `saida/gce/GCE_Lote2_v2_CPP.md` | v2 canônico | `6bb88330fe0f` |
| L2 | `saida/gce/GCE_Lote2_consolidacao_GCE.md` | E1–E7 | `1d680f9e90bb` |
| L2 | `saida/gce/GCE_Lote2_padroes_GCE.md` | padrões D2 e D3 | `732e062c5c4e` |
| L3 | `saida/gce/GCE_Lote3_v2_CPP.md` | v2 canônico, com a T-44 já gravada (título e nota do 3.1) | `a9c3fba59aaf` |
| L3 | `saida/gce/GCE_Lote3_consolidacao_GCE.md` | E1–E4 e Adendo 2 (Ato nº 225) | `61fdf619267f` |
| L3 | `saida/gce/GCE_Lote3_padroes_GCE.md` | padrões D4 e D5 | `cc17ec964b53` |
| L4 | `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | v3.4 (cabeçalho: Despacho 9, 09/10/2026); linha "Legenda:" → legendaMecanismo | `d7d820364ac5` |
| L4C | `saida/gcb/GCB_Lote4C_v1_GCB-CPP.md` | v1.1 (só itens AUTORAL); "Legenda:" → legendaMecanismo | `b412bf79842b` |
| L5 | `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` | v3.2 (errata Tukey, T-47, já gravada; D-TRANSPORTE-L5-V32); "Legenda:" (forma "Mecanismos:") → legendaMecanismo | `5f7f736cd369` |
| L5C | `saida/gcb/GCB_Lote5C_v1_GCB-CPP.md` | v1.1 (só itens AUTORAL); "Legenda:" → legendaMecanismo | `390ae7eee2af` |
| L6A | `saida/gcb/GCB_Lote6a_v2_producao_auto.md` | v2 (T-17); "Legenda:" ("atribuição errada (AT)") → legendaMecanismo | `0d3cc8073603` |
| L6B | `saida/gcb/GCB_Lote6b_v2_producao_auto.md` | v2 com errata A-6b-1 (T-17); "Legenda:" ("atribuição errada (AT)") → legendaMecanismo | `e89dfc4e12c2` |
| Banco | `banco/banco.csv` | 112 linhas; colunas texto_comando, texto_base, aderencia (T-29/T-42, D1-b) | `b0906e1d91c3` |
| SIM-0 | `saida/simulados/simulado_0_v0.2.md` | v0.2 com o ajuste T-36; seção "Avisos de montagem" (avisos 1, 2 e 4) → avisos | `03db759dd129` |
| SIM-0 | `saida/simulados/simulado_0_v0.2_gabarito.md` | gabarito e mapa | `e4cff2063c31` |
| SIM-1 | `saida/simulados/simulado_1.md` | v1 (sem versão declarada) | `e0d8627c0c79` |
| SIM-1 | `saida/simulados/simulado_1_gabarito.md` |  | `2eb45fb11f39` |
| SIM-2 | `saida/simulados/simulado_2.md` | v1 (D-SIM2-CANONICO) | `47ddd4bfe6b7` |
| SIM-2 | `saida/simulados/simulado_2_gabarito.md` |  | `a2a3ce823e00` |
| SIM-0-P2 | `saida/simulados/simulado_0_P2.md` | v1 (D-SIM0P2-DIAGNOSTICO) | `2415c3c58e06` |
| SIM-0-P2 | `saida/simulados/simulado_0_P2_gabarito.md` |  | `d8a2832ce33a` |
| Registro AUTORAL | `saida/gbq/claude_GBQ_Registro_AUTORAL_v3.md` | v3 (180 itens; gabarito, subitem, [TS], VOLÁTIL) | `1c159213c93a` |
| Edital | `edital/TI_itens_1_4_P1.md` | texto literal | `7376fd259311` |
| Edital | `edital/TI_itens_5_8_P1.md` | texto literal | `036bb384f3a8` |
| Edital | `edital/modulo_RF_IA_P2.md` | texto literal | `2c6341fe94b3` |
| Relatório anterior | `saida/pacote/pacote_relatorio_2026-10-13.md` | relatório da v1.2 (R0 + seção 13 da R1; substituído por este) | `7baececd7443` |
| Relatório anterior | `saida/pacote/pacote_relatorio_2026-10-10.md` | base de comparação (v1.1) | `1eb869850098` |
| v1.1 | `git show e97ab1f:saida/pacote/pacote.json` | referência de comparação, lida do git | `d318382639ee` |
| v1.2 (antes) | `git show 2684ab1:saida/pacote/pacote.json` | pacote canônico da D-PACOTE-V12, guardado antes de sobrescrever (cópia no scratchpad e no git) | `f46ed9f8e43d` |
| Edição do estudante v1.2 (antes) | `git archive 2684ab1 saida/estudante` | 43 arquivos; manifesto ordenado (SHA-256 das linhas "<sha>  <nome>") | `1a8267796baa` |

Condições do contrato (regra 5 e instrução da T-48), que continuam válidas: T-13, T-25, T-29, T-36, T-38, T-42, T-43, T-44, T-46 e T-47 CONCLUÍDAS e reconciliadas; T-40 CONCLUÍDA (BQ-0072, 0077, 0084, 0109, 0110 e 0111 entram, com 6/6 gabaritos sustentados). Simulados canônicos por D-SIM1-CANONICO, D-SIM2-CANONICO e D-SIM0P2-DIAGNOSTICO; SIM-0 v0.2 sem pendência (T-36 aplicada). T-48 e T-53 CONCLUÍDAS (reconciliação R2); T-55 CONCLUÍDA (gerador persistido). Nenhuma errata nem texto canônico de lote ou de simulado mudou desde a v1.2: a v1.3 só acrescenta o que a lista da T-12 manda. Liberar qualquer simulado à candidata continua reservado ao Fundador.

## 2. Contagens v1.1 → v1.2 → v1.3

| Medida | v1.1 | v1.2 | v1.3 |
|---|---|---|---|
| `versao` / `nome` | 1 / "Câmara 2026 — pacote F4 (v1.1)" | 1 / "Câmara 2026 — pacote F4 (v1.2)" | 1 / "Câmara 2026 — pacote F4 (v1.3)" |
| `geradoEm` | 2026-10-10 | 2026-10-13 | 2026-10-13 |
| edital (entradas) | 47 | 47 | 47 |
| itens (total) | 240 | 286 | 286 |
| itens CEBRASPE_ANALOGA (banco) | 60 | 106 | 106 |
| itens AUTORAL | 180 | 180 | 180 |
| gabarito C / E (total) | 122 / 118 | 149 / 137 | 149 / 137 |
| gabarito C / E (banco) | 33 / 27 | 60 / 46 | 60 / 46 |
| gabarito C / E (AUTORAL) | 89 / 91 | 89 / 91 | 89 / 91 |
| aderência direta / parcial (total) | 217 / 23 | 247 / 39 | 247 / 39 |
| aderência direta / parcial (banco; AUTORAL todos direta) | 37 / 23 | 67 / 39 | 67 / 39 |
| `volatil: true` (total; banco + AUTORAL) | 19 (4 + 15) | 23 (8 + 15) | 23 (8 + 15) |
| `nota` (itens) | 0 | 2 (BQ-0003, BQ-0040) | 2 (BQ-0003, BQ-0040) |
| `comandoOriginal` (itens) | 0 | 90 | 90 |
| `textoBase` "nenhum" / "" / texto | 237 / 0 / 3 | 0 / 283 / 3 | 0 / 283 / 3 |
| lotes / discursivas | 10 / 5 | 10 / 5 | 10 / 5 |
| lotes com `legendaMecanismo` (opcional, v1.2.1 ponto 4) | 0 | 0 | 6 (L4, L4C, L5, L5C, L6A, L6B) |
| pegadinhas (total) | 144 | 262 | 262 |
| simulados | 2 (SIM-0, SIM-1) | 4 (SIM-0, SIM-1, SIM-2, SIM-0-P2) | 4 (SIM-0, SIM-1, SIM-2, SIM-0-P2) |
| simulados `n` | — / — | 60 / 40 / 40 / 25 | 60 / 40 / 40 / 25 |
| simulados com `avisos` (opcional, v1.2.1 ponto 5) | 0 | 0 | SIM-0 (3 avisos) |
| bytes | 541533 | 618673 | 620956 |
| SHA-256 (12) | d318382639ee | f46ed9f8e43d | fdcb7afdb4fb |

A v1.3 é a v1.2 (R1, SHA-256 `f46ed9f8e43d`) mais `nome`, `legendaMecanismo` e `avisos`: as medidas de itens, simulados, lotes e discursivas são idênticas (seção 13, conferência (5)). Banco: 112 linhas em `banco/banco.csv`; 106 exportadas (60 C / 46 E) e 6 excluídas por anulação (gabarito X): BQ-0029, BQ-0030, BQ-0031, BQ-0060, BQ-0062, BQ-0063. Os 60 itens da v1.1 mantêm o mesmo `comando` e a mesma aderência (37 direta / 23 parcial, conferido); os 46 novos são BQ-0061… do terceiro lote de varredura (inclui BQ-0072, 0077, 0084, 0109, 0110 e 0111, liberados pela T-40). BQ-0049 a 0051 são os únicos com `textoBase` (a coluna `texto_base`); nos 283 demais `textoBase` é `""` (F2).

### 2.1 Itens por lote (AUTORAL) e `comandoOriginal`

| Lote | AUTORAL | C | E | `volatil` | `comandoOriginal` | pegadinhas v1.1 → v1.3 | pares |
|---|---|---|---|---|---|---|---|
| L1 | 20 | 10 | 10 | 4 | 0 | 8 → 19 | 17 |
| L1C | 10 | 4 | 6 | 0 | 0 | 1 → 4 | 0 |
| L2 | 30 | 15 | 15 | 0 | 0 | 8 → 43 | 22 |
| L3 | 30 | 16 | 14 | 1 | 0 | 7 → 42 | 28 |
| L4 | 20 | 10 | 10 | 1 | 20 | 32 → 32 | 20 |
| L4C | 10 | 5 | 5 | 0 | 10 | 0 → 0 | 0 |
| L5 | 20 | 10 | 10 | 4 | 20 | 14 → 48 | 15 |
| L5C | 10 | 5 | 5 | 0 | 10 | 0 → 0 | 0 |
| L6A | 15 | 7 | 8 | 5 | 15 | 35 → 35 | 19 |
| L6B | 15 | 7 | 8 | 0 | 15 | 39 → 39 | 18 |

`volatil` no banco (8): BQ-0015, BQ-0017, BQ-0035, BQ-0064, BQ-0075, BQ-0076, BQ-0086, BQ-0089. Em AUTORAL (15): L1-Q14, L1-Q16, L1-Q18, L1-Q19, L3-Q21, L4-15, A5-14, A5-15, A5-16, A5-17, 6A-01, 6A-09, 6A-10, 6A-14, 6A-15. Total 23; os AUTORAL são os VOLÁTIL + REVERIFICAR normativo do registro GBQ v3 (regra R1-N), com L3-Q21.

### 2.2 Simulados (regra (e): `n` e `versao`)

| id | nome | tipo | `versao` | `n` | itens | C / E | `volatil` | parcial | `avisos` |
|---|---|---|---|---|---|---|---|---|---|
| SIM-0 | Simulado 0 — diagnóstico (v0.2) | diagnóstico | v0.2 | 60 | 60 | 33 / 27 | 4 | 23 | 3 |
| SIM-1 | Simulado 1 — P1 final (TI e Dados, itens 5 a 8) | final | v1 | 40 | 40 | 20 / 20 | 0 | 0 | — |
| SIM-2 | Simulado 2 — P2 final (Reconhecimento de Fala, Transcrição e IA, itens 1 a 4) | final | v1 | 40 | 40 | 20 / 20 | 0 | 0 | — |
| SIM-0-P2 | Simulado 0-P2 — P2 diagnóstico (Reconhecimento de Fala, Transcrição e IA, itens 1 a 4) | diagnóstico | v1 | 25 | 25 | 13 / 12 | 0 | 0 | — |

`n` = tamanho da lista `itens` em 4/4. `avisos` (v1.2.1 ponto 5): só o SIM-0, com os avisos 1, 2 e 4 da folha canônica, literais (seção 13.2). `versao`: SIM-0 "v0.2" (cabeçalho do arquivo); SIM-1, SIM-2 e SIM-0-P2 "v1" (sem versão declarada, regra (e)). Nenhum simulado final contém item `volatil` ou `parcial`. O gabarito de cada posição do simulado (arquivos `*_gabarito.md`) é igual ao `gabarito` do item no pacote em 165/165 posições (60 + 40 + 40 + 25).

### 2.3 Discursivas

D1–D5 idênticas às da v1.1 e da v1.2 (nada mudou nas 5): D1 questão (L1), D2 questão e D3 peça (L2), D4 questão e D5 peça (L3). Aspectos e quesitos conferidos: soma dos aspectos das questões 14,30 + 0,70 de apresentação = 15,00; peças 28,50 + 1,50 = 30,00. A observação "inferido pela EXEC" da D1 (Adendo 4) não é exportada: 0 ocorrência de "EXEC" nas discursivas. D3 e D5 são pareceres técnicos (gênero confirmado para analista e técnico; hipótese por analogia para o Cargo 11). Pesos por quesito são HIPÓTESE do Projeto.

## 3. Erratas (consolidações sincronizadas) — estado por errata

Método: substituição exata do trecho "onde se lê" (X) pelo "leia-se" (Y), tolerante a quebra de linha, na ordem do arquivo; cada X deve ter exatamente 1 ocorrência livre (não contida em Y). Estados: **APLICADA** (X encontrado 1 vez e trocado por Y); **JÁ PRESENTE** (X ausente e Y já presente na fonte); **NÃO ENCONTRADA** (nem X nem Y: o script aborta); **FORA DO PACOTE** (o alvo da errata não é exportado; checado: X/Y não vão ao JSON). O gerador aborta em qualquer falha; **0 NÃO ENCONTRADA**. Conferência prévia: `sync_check` leu cada X/Y contra o texto da consolidação sincronizada em `saida/gce/` (resultado: TUDO OK, 28 linhas).

| Lote | Errata | Alvo | Estado | Nota |
|---|---|---|---|---|
| L1 | E1 | Q07 (d): "diarização habilitada, por si só, sem amostras de voz de referência" | APLICADA |  |
| L1 | E2 | Q08 (d): "e um sistema pode diarizar" | APLICADA |  |
| L1 | E3 | Q11 (d): "e, eventualmente, de pistas prosódicas" | APLICADA |  |
| L1 | E4a | curso 1.1: WER "no cálculo usual, sobre texto normalizado…" | APLICADA |  |
| L1 | E4b | curso 1.1: "no cálculo usual ele ignora pontuação, e em qualquer convenção ignora locutores" | APLICADA |  |
| L1 | E4c | (d-G) Q01 (justificativa): "No cálculo usual, pontuação e capitalização ficam fora do WER…" | APLICADA | Y começa com maiúscula porque X abre a frase (como na v1.1) |
| L1 | E5 | resumo (b), "CLM (texto; indisponível para pt-BR na AWS)" | APLICADA |  |
| L1 | E7a | D1 padrão, quesito 2.3: "[valor máximo: 5,30]" | APLICADA | E7 também insere a linha "Apresentação e estrutura textual: 0,70" |
| L1 | E7b | D1 padrão, nota de correção: "(5,00 / 4,00 / 5,30), mais 0,70 de apresentação" | APLICADA |  |
| L1 | E9 | curso 1.2: espectrograma "em geral (por exemplo, no Whisper)" | APLICADA |  |
| L1 | E10 | curso 1.8: "departamento de registro da Câmara (Derep, antigo DETAQ; Ato da Mesa nº 251/2026)" | APLICADA |  |
| L1 | E12 | resumo (b), WER: "no cálculo usual, sobre texto normalizado, não mede pontuação nem capitalização; locutor fica fora…" (T-46) | APLICADA |  |
| L1 | F5 | F5: "Derep, antigo DETAQ" → "Derep (antigo DETAQ)" (depois da E10) | APLICADA | aplicada depois da E10 |
| L1C | E1 | (d-G) justificativa: reforço por LLM não implica áudio como modalidade do próprio LLM | APLICADA |  |
| L1C | E3 | (d) Q23 (enunciado): "end-to-end, não há dicionário de pronúncias separado" | APLICADA |  |
| L2 | E1a-curso | curso 2.6: "traduz as notas… em texto" | APLICADA |  |
| L2 | E1b-resumo | resumo 2.6: "traduz as notas estenotípicas em texto" | APLICADA |  |
| L2 | E1c-par15 | par 15: "(traduz as notas estenotípicas em texto)" | APLICADA |  |
| L2 | E1d-dgQ21 | (d-G) justificativa de Q21 (G2 da T-44) | APLICADA |  |
| L2 | E2 | curso: acréscimo "Lista variável conforme a consulta à página (08/10/2026)." | APLICADA | consolidação diz "acrescentar": X = frase-âncora; o acréscimo foi conferido |
| L2 | E3b | curso: "foi observada nas notas oficiais de 2026 (N1)" | APLICADA |  |
| L2 | E5 | curso: acréscimo da definição de aparte (RICD, art. 176) | APLICADA | idem ("acrescentar") |
| L2 | E6 | curso: acréscimo (RICD, art. 176: interrupção…) | APLICADA | idem ("acrescentar") |
| L2 | E7 | resumo 2.4: "Forma de identificar o orador: observada nas notas oficiais de 2026 (N1; E3)…" | APLICADA |  |
| L3 | E1a | curso 4.1: § 3º "consta como vetado na página compilada, com remissão à VEP nº 288/2019" | APLICADA |  |
| L3 | E1b | resumo (b), linha 4.1: art. 20, "expressão suprimida (MP nº 869/2018, convertida na Lei 13.853/2019)" | APLICADA | o Y usa aspas duplas do arquivo (a consolidação escreve aspas simples) |
| L3 | E2 | curso 4.1: "o art. 5º, II, enumera origem" | APLICADA |  |
| L3 | E3a | curso 4.1: "a MP nº 869/2018, convertida na Lei 13.853/2019, suprimiu a expressão" | APLICADA | o X tem 2 ocorrências no texto bruto; 1 depois da E1b (aplicação em sequência), que é a que a errata visa |
| L3 | E3b | (d-G) Q20 (justificativa): idem, "da redação original" | APLICADA |  |
| L3 | E4 | par 20: "(redação original, suprimida pela MP nº 869/2018, convertida na Lei 13.853/2019)" | APLICADA |  |
| L3 | Adendo 2 (3.1) | Ato da Mesa nº 225/2025 no curso 3.1 | JÁ PRESENTE | bloco "CONTEXTO NORMATIVO INTERNO (SEM ITEM)" (T-08/T-44) já cobre o Ato nº 225/2025 no 3.1 (art. 3º, I, III, V, VIII, IX; art. 4º, IV): NÃO duplicado |
| L3 | Adendo 2 (4.1) | Ato da Mesa nº 225/2025 no curso 4.1 ("Contexto institucional") | APLICADA | texto literal do Adendo 2 inserido ao final do item 4.1 (antes de "--- 4.2") |
| L1 | E8 | D1 (comando): preâmbulo "Ao domínio do conteúdo serão atribuídos até 15,00 pontos…" e [valor: 5,00/4,00/5,30 pontos] por alínea | APLICADA | montagem da D1; resultado idêntico ao da v1.1 |
| L3 | T-44 | título e nota do curso 3.1; G1/G2 (erratas D1 de 10/10) | JÁ PRESENTE | gravada em `GCE_Lote3_v2_CPP.md`; o pacote lê o arquivo atual (v1.1 ainda trazia "ERRATA T-08" e "registro da GCB-CQFP", ver seção 5) |
| L5 | T-47 (Tukey) | curso 8.2, "Bigodes e outliers": "O fator 1,5·AIQ é a convenção usual (Tukey)…" | JÁ PRESENTE | gravada em `GCB_Lote5_v3_canonica_GCB-CPP.md`; o pacote lê o arquivo atual (+102 caracteres no curso do L5) |

Totais: os registros de substituição do gerador são 32 (31 APLICADA e 1 JÁ PRESENTE, a única sendo o Adendo 2 no 3.1); 0 NÃO ENCONTRADA. As três últimas linhas da tabela (E8, T-44, T-47) são informativas: E8 é a montagem da D1 (APLICADA, sem substituição) e T-44 e T-47 já estavam gravadas nos arquivos canônicos (JÁ PRESENTE); somadas, a tabela tem 35 linhas, das quais 32 APLICADA ou JÁ PRESENTE por substituição do gerador. Para cada APLICADA o script confere depois que Y consta do JSON e X não consta (fora das ocorrências de Y): validação "erratas: Y presente / X ausente", OK.

### 3.1 Erratas cujo alvo não é exportado (estado FORA DO PACOTE)

| Lote | Errata | Onde fica o alvo | Verificação |
|---|---|---|---|
| L1 | E6 | (d-G), nota de produção final do arquivo (contagens e risco), não é justificativa de item | alvo existe na fonte; X/Y não vão ao JSON |
| L1 | E11 | texto do "Motivo" do Adendo (E7/E8) na própria consolidação; nada do Adendo é exportado | alvo existe na fonte; X/Y não vão ao JSON |
| L1C | E2 | Tabela de correções do cabeçalho do arquivo (linha N2); cabeçalho não é exportado | alvo existe na fonte; X/Y não vão ao JSON |
| L1C | E4 | lista de fontes da seção de evidência (acréscimo sem texto-âncora); evidência não é exportada | sem texto-âncora; checado por varredura do JSON |
| L2 | E3a | Limites de evidência, nota N1 (cabeçalho); não é exportado | alvo existe na fonte; X/Y não vão ao JSON |
| L2 | E4 | regra geral de denominação (DETAQ → Derep (antigo DETAQ)); verificada por varredura do JSON | sem texto-âncora; checado por varredura do JSON |

L1 E11 (Adendo 4): o texto "Motivo" do Adendo (E7/E8) só existe na consolidação; o que vai ao pacote (comando e padrão da D1) não contém "14,30" (validado). A confirmação do Adendo 4 sobre os itens do edital da D1 ("CONFIRMADO o que a EXEC inferiu, P2-1.4, P2-1.6 e P2-1.7") não é exportada (0 "EXEC" nas discursivas).

### 3.2 Adendo 2 — Ato da Mesa nº 225/2025 (decisão)

- **Curso 3.1: JÁ PRESENTE, não duplicado.** O bloco "CONTEXTO NORMATIVO INTERNO (SEM ITEM)" (T-08, com o título e a nota da T-44) já resume o Ato nº 225 no 3.1 (art. 3º, I, III, V, VIII, IX; art. 4º, IV). Inserir o Adendo 2 ali duplicaria o conteúdo; o instruído pela T-48 foi justamente "sem duplicar o bloco já aplicado pela T-08".
- **Curso 4.1: APLICADA.** O texto literal do Adendo 2, com o título "Contexto institucional — Ato da Mesa nº 225, de 15/12/2025…", foi inserido ao fim do 4.1, antes de "--- 4.2" (811 caracteres). Ocorre 1 vez no curso do L3; conferido que é igual ao Adendo 2 da consolidação.

## 4. F1 a F5 e D1-b/D1-c

- **F1 (L1-Q04 "áudio–texto"): feita, 1 junção.** O arquivo canônico tem o travessão (en dash) no fim da linha ("áudio–" / "texto"); a quebra virava espaço ("áudio– texto"). A regra do gerador passou a juntar sem espaço quando uma linha termina em en dash colado a letra. Resultado: `enunciado` de L1-Q04 = "…pares áudio–texto para treinamento…"; 0 "áudio– texto" no JSON; nenhuma outra sequência letra+"– "+letra no JSON (validado). É a única alteração de `enunciado` da v1.1 para a v1.2.
- **F2 (`textoBase` vazio): feita.** `textoBase` = `""` em 283 de 286 itens (a v1.1 tinha "nenhum" em 237); 0 "nenhum"; texto literal só em BQ-0049, 0050 e 0051 (coluna `texto_base`).
- **F3 (pegadinhas, uma por entrada, com `rotulo`): feita**, ver seção 8.
- **F4 (marcas internas das justificativas): feita em 21 justificativas** (18 da R0 mais 6B-06, 6B-15 e L2-Q21 acrescentadas na correção R1; D-R1-02, D-R1-03 e D-R1-20), ver seção 6.
- **F5 ("Derep (antigo DETAQ)"): feita.** 1 substituição no L1 (curso 1.8, E10 já com a forma "Derep, antigo DETAQ" → "Derep (antigo DETAQ)"); 0 "Derep, antigo DETAQ" no JSON; a forma correta ocorre 13 vezes no JSON e nenhuma outra grafia de DETAQ fora dela.
- **D1-b (aderência explícita): feita.** Todo item de banco recebe `aderencia` da coluna do `banco.csv`, sem recálculo (106/106 iguais à coluna: 67 direta / 39 parcial). A regra por texto de `observacoes` deixou de valer para a exportação.
- **D1-c (comando normalizado + `comandoOriginal`): feita em 90 itens** (L4 20, 4C 10, A5/L5 20, 5C 10, 6A 15, 6B 15; L1–L3 e banco: 0). Regex `(?i)(julgue os itens) (?:de )?(?:[0-9A-Z]+-)?\d+ a (?:[0-9A-Z]+-)?\d+\.` → "julgue os itens a seguir."; o resto da frase fica literal e o literal vai em `comandoOriginal`. Conferido: só o trecho da numeração muda; BQ-0070, 0071 e 0112 ficam com o comando inteiro e sem `comandoOriginal`; nenhum comando restante com faixa de itens.

## 5. Diff textual resumido v1.1 → v1.3 por lote

Campos de lote comparados caractere a caractere (difflib), v1.1 (git e97ab1f) contra a v1.3. O diff v1.2 → v1.3 é menor: os campos de texto dos lotes (`resumo`, `curso`, `pares`, `pegadinhas`, `itensEdital`) são idênticos (conferência (1), seção 13); o único acréscimo é `legendaMecanismo` em 6 lotes. Campos não citados: idênticos.

**L1**
- resumo: 2446 → 2543 caracteres, 3 operações:
  - insere "o cálculo usual, sobre texto normalizado, n"
  - insere "capitalização; "
  - insere " fica fora do WER em qualquer convenção"
- curso: 22641 → 22642 caracteres, 3 operações:
  - remove ","
  - insere "("
  - insere ")"
- pegadinhas: 8 → 19 entradas (desdobramento da F3, com as reuniões da errata v1.2.1 ponto 2 quando houve), todas com `rotulo`.

**L1C**
- pegadinhas: 1 → 4 entradas (desdobramento da F3, com as reuniões da errata v1.2.1 ponto 2 quando houve), todas com `rotulo`.

**L2**
- resumo: 2609 → 2746 caracteres, 4 operações:
  - insere "Forma de identificar o orador: observada nas notas oficiais de 2026 (N1; E3). "
  - remove "exata "
  - insere "a para marcação de pausas e eventos não falados e para grafi"
  - insere " (N2)"
- pegadinhas: 8 → 43 entradas (desdobramento da F3, com as reuniões da errata v1.2.1 ponto 2 quando houve), todas com `rotulo`.

**L3**
- curso: 26978 → 27731 caracteres, 3 operações:
  - remove "ERRATA T-08, 10/10/2026; "
  - remove " (registro da GCB-CQFP, 08/10/2026)"
  - insere "Contexto institucional — Ato da Mesa nº 225, de 15/12/2025 (DCD, Ed.⏎Extra A, 18/12/2025): estabelece diretrizes gerais para a política de⏎governança de intelig"
- pares: 28 pares; 1 com texto alterado.
- pegadinhas: 7 → 42 entradas (desdobramento da F3, com as reuniões da errata v1.2.1 ponto 2 quando houve), todas com `rotulo`.

**L4**
- resumo, curso, pares e itensEdital idênticos; pegadinhas: mesma contagem (32), agora com `rotulo`.
- `legendaMecanismo` (novo na v1.3): "Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC)".

**L4C**
- resumo, curso, pares e itensEdital idênticos; pegadinhas: mesma contagem (0), agora com `rotulo`.
- `legendaMecanismo` (novo na v1.3): "Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC)".

**L5**
- curso: 18901 → 19003 caracteres, 1 operações:
  - insere " O fator 1,5·AIQ é a convenção usual (Tukey); outras convenções existem e a prova costuma cobrar esta."
- pegadinhas: 14 → 48 entradas (desdobramento da F3, com as reuniões da errata v1.2.1 ponto 2 quando houve), todas com `rotulo`.
- `legendaMecanismo` (novo na v1.3): "Mecanismos: TC troca de conceito; GI generalização indevida; AT atribuição errada de técnica; IC inversão de causa e efeito".

**L5C**
- resumo, curso, pares e itensEdital idênticos; pegadinhas: mesma contagem (0), agora com `rotulo`.
- `legendaMecanismo` (novo na v1.3): "Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC)".

**L6A**
- resumo, curso, pares e itensEdital idênticos; pegadinhas: mesma contagem (35), agora com `rotulo`.
- `legendaMecanismo` (novo na v1.3): "Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada (AT), inversão de causa e efeito (IC)".

**L6B**
- resumo, curso, pares e itensEdital idênticos; pegadinhas: mesma contagem (39), agora com `rotulo`.
- `legendaMecanismo` (novo na v1.3): "Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada (AT), inversão de causa e efeito (IC)".

Itens (campo a campo, v1.1 → v1.3): `textoBase` 237 (F2, "nenhum" → ""), `comando` 90 e `comandoOriginal` 90 (D1-c), `justificativa` 21 (F4), `nota` 2 (BQ-0003, BQ-0040), `enunciado` 1 (L1-Q04, F1). `gabarito`, `aderencia` (nos 60 da v1.1), `itemEdital`, `rotulo`, `certame`, `cargo`, `ano`, `numero` e `url`: 0 diferença. Discursivas: 0 diferença. Edital: igual. Da v1.2 para a v1.3, nenhum item muda.

## 6. F4 — justificativas alteradas (antes / depois)

Só deleção (conferido por difflib: nenhuma inserção nem troca, salvo as duas trocas de caixa fechadas da C-05, em 4C-08 e 5C-06, "Lição O10: o item" → "O item" e "Lição O10: a regra" → "A regra", D-R1-04); cada trecho a apagar ocorre exatamente 1 vez; depois da deleção, sem espaço duplo nem espaço antes de pontuação; 0 marca de processo (CQFP/CQE/CPP/GCE/GCB/GBQ/EXEC, T-xx, "(vN", Oxx, "Lição", R-4C1, "Risco", QA, O-n, "Retificação", "Gabarito C|E mantido") remanescente nas 180 justificativas AUTORAL. **21 justificativas**: as 17 da GBQ são as justificativas com os tipos de marca que ela listou (CQFP, "(v3 — O12)", "(O1)", "Lição O10", "R-4C1", "Risco"); a 18.ª é a 5C-03 ("R-5C1", mesma classe de R-4C1); com a rodada R1 (6B-06, 6B-15, L2-Q21) a F4 soma 21 (gcb-cqfp O-2; D-R1-20).

**L2-Q21**
- antes: Memória de tradução reaproveita segmentos já traduzidos entre idiomas e é recurso de ferramentas de tradução; o CAT do edital é transcrição assistida, que na taquigrafia traduz as notas estenotípicas em texto [F7]. Gabarito E mantido.
- depois: Memória de tradução reaproveita segmentos já traduzidos entre idiomas e é recurso de ferramentas de tradução; o CAT do edital é transcrição assistida, que na taquigrafia traduz as notas estenotípicas em texto [F7].
- apagado: " Gabarito E mantido."

**L2-Q23**
- antes: Falsa pegadinha: o formato é de legenda, mas organiza segmentos com intervalo de tempo e admite indicar o falante [V 08/10/2026 — F3]. Depende de padrão técnico estável, não de produto; NÃO VOLÁTIL (classificação final da CQFP).
- depois: Falsa pegadinha: o formato é de legenda, mas organiza segmentos com intervalo de tempo e admite indicar o falante [V 08/10/2026 — F3]. Depende de padrão técnico estável, não de produto; NÃO VOLÁTIL.
- apagado: " (classificação final da CQFP)"

**L4-08**
- antes: TC. A descrição é da classificação (categorias definidas antes pelo humano); no clustering, o modelo encontra os grupos, e o humano pode nomeá-los com base em seu entendimento dos dados (F4: "You might then attempt to name those clusters"). Fonte: F4, verificado em 7/10/2026. (v3 — O12)
- depois: TC. A descrição é da classificação (categorias definidas antes pelo humano); no clustering, o modelo encontra os grupos, e o humano pode nomeá-los com base em seu entendimento dos dados (F4: "You might then attempt to name those clusters"). Fonte: F4, verificado em 7/10/2026.
- apagado: " (v3 — O12)"

**L4-09**
- antes: GI. "Não supervisionado" significa ausência de rótulos nos dados; o humano escolhe os dados e os parâmetros e interpreta os resultados — e pode nomear os grupos encontrados (F4). Fonte: F4, verificado em 7/10/2026. (v3 — O12)
- depois: GI. "Não supervisionado" significa ausência de rótulos nos dados; o humano escolhe os dados e os parâmetros e interpreta os resultados — e pode nomear os grupos encontrados (F4). Fonte: F4, verificado em 7/10/2026.
- apagado: " (v3 — O12)"

**L4-13**
- antes: GI. Modelo de fundação é "a very large pre-trained model trained on an enormous and diverse training set", não necessariamente texto; LLM é modelo de linguagem com muitíssimos parâmetros; o F3 define os termos separadamente (O1). Fonte: F3, verificado em 7/10/2026.
- depois: GI. Modelo de fundação é "a very large pre-trained model trained on an enormous and diverse training set", não necessariamente texto; LLM é modelo de linguagem com muitíssimos parâmetros; o F3 define os termos separadamente. Fonte: F3, verificado em 7/10/2026.
- apagado: " (O1)"

**L4-15**
- antes: GI + IC. O modelo, por si só, responde com o conhecimento incorporado no treinamento; consulta a dados externos só com RAG, busca ou ferramentas acopladas (F2); "sempre a informação mais atual" é generalização indevida. Fonte: F2, verificado em 7/10/2026. Risco MÉDIO; mantido como está (conferido pela CQFP: "por si só" e "sempre" sustentam o E).
- depois: GI + IC. O modelo, por si só, responde com o conhecimento incorporado no treinamento; consulta a dados externos só com RAG, busca ou ferramentas acopladas (F2); "sempre a informação mais atual" é generalização indevida. Fonte: F2, verificado em 7/10/2026.
- apagado: " Risco MÉDIO; mantido como está (conferido pela CQFP: "por si só" e "sempre" sustentam o E)."

**L4-17**
- antes: TC (tentação: ler a ressalva como erro). LGPD, art. 12, caput: dados anonimizados não são dados pessoais, salvo quando a anonimização for revertida ou puder sê-lo com esforços razoáveis; art. 5º, III, apenas define. Base: N1, art. 12, caput; art. 5º, III. Aprovado pela CQFP (art. 12, caput, conferido no Planalto em 07/10/2026).
- depois: TC (tentação: ler a ressalva como erro). LGPD, art. 12, caput: dados anonimizados não são dados pessoais, salvo quando a anonimização for revertida ou puder sê-lo com esforços razoáveis; art. 5º, III, apenas define. Base: N1, art. 12, caput; art. 5º, III.
- apagado: " Aprovado pela CQFP (art. 12, caput, conferido no Planalto em 07/10/2026)."

**L4-18**
- antes: GI. O consentimento (art. 7º, I) é uma das bases; a execução de políticas públicas pela administração tem base própria no art. 7º, III, além da obrigação legal (art. 7º, II). Base: N1, art. 7º, I, II e III — conferido pela CQFP no Planalto em 08/10/2026.
- depois: GI. O consentimento (art. 7º, I) é uma das bases; a execução de políticas públicas pela administração tem base própria no art. 7º, III, além da obrigação legal (art. 7º, II). Base: N1, art. 7º, I, II e III.
- apagado: " — conferido pela CQFP no Planalto em 08/10/2026"

**L4-19**
- antes: IC (responsabilidade deslocada para o instrumento). A ferramenta não é agente público; quem pratica o ato responde por ele; supervisão humana é o princípio aplicável (curso 6.1 e 6.2). Gabarito E aprovado pela CQFP sem dependência de norma; o item não se apoia em dispositivo legal.
- depois: IC (responsabilidade deslocada para o instrumento). A ferramenta não é agente público; quem pratica o ato responde por ele; supervisão humana é o princípio aplicável (curso 6.1 e 6.2). Gabarito E sem dependência de norma; o item não se apoia em dispositivo legal.
- apagado: " aprovado pela CQFP"

**L4-20**
- antes: GI invertida. LAI, art. 3º, I: publicidade como preceito geral e sigilo como exceção; exceções legais incluem informações pessoais (art. 31, caput, e § 1º, I) e informações classificadas (art. 23, caput; art. 24, § 1º, I a III). Base: N2, arts. 3º, I; 23, caput; 24, § 1º, I a III; 31, caput, e § 1º, I — conferidos pela CQFP no Planalto em 08/10/2026.
- depois: GI invertida. LAI, art. 3º, I: publicidade como preceito geral e sigilo como exceção; exceções legais incluem informações pessoais (art. 31, caput, e § 1º, I) e informações classificadas (art. 23, caput; art. 24, § 1º, I a III). Base: N2, arts. 3º, I; 23, caput; 24, § 1º, I a III; 31, caput, e § 1º, I.
- apagado: " — conferidos pela CQFP no Planalto em 08/10/2026"

**4C-06**
- antes: AT (tentação: tomar a instrução longa ou a descrição do formato desejado por "exemplo" e concluir que o prompt é one-shot → marcar E). Curso 5.1.2 (itens 4 e 5): exemplos são demonstrações de entrada e saída; o formato de saída é a forma da resposta (tabela, JSON, número de linhas) e, descrito em palavras, não é demonstração. Curso 5.1.3: zero-shot = prompt sem nenhum exemplo de resposta esperada, só a instrução (F3). A extensão da instrução e a descrição do formato não a transformam em exemplo. Difere do item 2 do Lote 4 porque aquele julga o few-shot pelo número de exemplos (um único exemplo é one-shot); este julga o zero-shot pela ausência de qualquer demonstração, ainda que a instrução seja longa e detalhada. Fonte: F3, zero-shot ("A prompt that does not provide an example of how you want the large language model to respond", conferido pela CQFP em 07/10/2026, conforme o parecer da rodada 1), e curso 5.1.2 e 5.1.3.
- depois: AT (tentação: tomar a instrução longa ou a descrição do formato desejado por "exemplo" e concluir que o prompt é one-shot → marcar E). Curso 5.1.2 (itens 4 e 5): exemplos são demonstrações de entrada e saída; o formato de saída é a forma da resposta (tabela, JSON, número de linhas) e, descrito em palavras, não é demonstração. Curso 5.1.3: zero-shot = prompt sem nenhum exemplo de resposta esperada, só a instrução (F3). A extensão da instrução e a descrição do formato não a transformam em exemplo. Difere do item 2 do Lote 4 porque aquele julga o few-shot pelo número de exemplos (um único exemplo é one-shot); este julga o zero-shot pela ausência de qualquer demonstração, ainda que a instrução seja longa e detalhada. Fonte: F3, zero-shot ("A prompt that does not provide an example of how you want the large language model to respond"), e curso 5.1.2 e 5.1.3.
- apagado: ", conferido pela CQFP em 07/10/2026, conforme o parecer da rodada 1"

**4C-08**
- antes: GI (restrição indevida do conceito; tentação: tratar a injeção de prompt como sinônimo do ataque direto do usuário). Curso 5.1.4: injeção de prompt = instruções maliciosas embutidas em textos que o modelo lê e que tentam sobrepor-se às instruções legítimas (conceito geral, sem fonte de fornecedor, como no curso). Lição O10: o item não depende de a literatura tratar o jailbreak como espécie de injeção ou como categoria distinta; basta que a injeção abranja as instruções embutidas em textos lidos, o que o curso afirma e o termo "restringe-se" nega. O item não usa o par injeção × jailbreak (C19) como critério. Fonte: curso 5.1.4.
- depois: GI (restrição indevida do conceito; tentação: tratar a injeção de prompt como sinônimo do ataque direto do usuário). Curso 5.1.4: injeção de prompt = instruções maliciosas embutidas em textos que o modelo lê e que tentam sobrepor-se às instruções legítimas (conceito geral, sem fonte de fornecedor, como no curso). O item não depende de a literatura tratar o jailbreak como espécie de injeção ou como categoria distinta; basta que a injeção abranja as instruções embutidas em textos lidos, o que o curso afirma e o termo "restringe-se" nega. O item não usa o par injeção × jailbreak (C19) como critério. Fonte: curso 5.1.4.
- apagado: 

**4C-09**
- antes: sem armadilha (ancoragem; R-4C1). Curso 5.1.2 (item 3): o contexto é o texto sobre o qual o modelo deve trabalhar; curso 5.1.3: o RAG recupera documentos e os insere no prompt; curso 5.3.3: sem ferramentas ou RAG, o modelo responde com o que incorporou no treinamento (conhecimento paramétrico). Um relatório elaborado depois do treinamento não integra esse conhecimento; sem ferramentas externas (como a busca), sem RAG e sem retreinamento, o caminho é incluí-lo no prompt, como contexto. Retificação 6-A: a redação "sem acesso a busca" não excluía outras ferramentas; "ferramentas externas (como a busca)" alinha o item ao curso 5.3.3 ("sem ferramentas ou RAG"). O acréscimo "e sem retreinamento" existe porque o curso (5.1.1; 5.3.3) prevê o fine-tuning como outra forma de incorporar conhecimento: sem a ressalva, o "deve" ficaria vulnerável a recurso. Difere do item 15 do Lote 4 porque aquele julga se o modelo consulta fontes externas por si só; este julga a aplicação (o material entra como contexto do prompt). Difere do item 6 do Lote 4 porque aquele julga RAG × retreinamento. Fonte: curso 5.1.2, 5.1.3 e 5.3.3.
- depois: sem armadilha (ancoragem). Curso 5.1.2 (item 3): o contexto é o texto sobre o qual o modelo deve trabalhar; curso 5.1.3: o RAG recupera documentos e os insere no prompt; curso 5.3.3: sem ferramentas ou RAG, o modelo responde com o que incorporou no treinamento (conhecimento paramétrico). Um relatório elaborado depois do treinamento não integra esse conhecimento; sem ferramentas externas (como a busca), sem RAG e sem retreinamento, o caminho é incluí-lo no prompt, como contexto. O acréscimo "e sem retreinamento" existe porque o curso (5.1.1; 5.3.3) prevê o fine-tuning como outra forma de incorporar conhecimento: sem a ressalva, o "deve" ficaria vulnerável a recurso. Difere do item 15 do Lote 4 porque aquele julga se o modelo consulta fontes externas por si só; este julga a aplicação (o material entra como contexto do prompt). Difere do item 6 do Lote 4 porque aquele julga RAG × retreinamento. Fonte: curso 5.1.2, 5.1.3 e 5.3.3.
- apagado: "; R-4C1" | " Retificação 6-A: a redação "sem acesso a busca" não excluía outras ferramentas; "ferramentas externas (como a busca)" alinha o item ao curso 5.3.3 ("sem ferramentas ou RAG")."

**A5-14**
- antes: Três componentes e fluxo conforme U1 en-us ("three primary components"; Desktop = "development tool"; serviço "allows you to organize, manage, and distribute"); natureza Windows do Desktop conforme U2. Verificado em 8/10/2026. Risco BAIXO.
- depois: Três componentes e fluxo conforme U1 en-us ("three primary components"; Desktop = "development tool"; serviço "allows you to organize, manage, and distribute"); natureza Windows do Desktop conforme U2. Verificado em 8/10/2026.
- apagado: " Risco BAIXO."

**A5-15**
- antes: TC (descontinuado no lugar de renomeado). Em 11/10/2022 o Data Studio foi renomeado Looker Studio ("Data Studio is now Looker Studio", GG4), não descontinuado; em abril de 2026 o nome voltou a ser Data Studio (U4, U5, U6), nome vigente. Verificado em 8/10/2026. Risco MÉDIO (nome de produto).
- depois: TC (descontinuado no lugar de renomeado). Em 11/10/2022 o Data Studio foi renomeado Looker Studio ("Data Studio is now Looker Studio", GG4), não descontinuado; em abril de 2026 o nome voltou a ser Data Studio (U4, U5, U6), nome vigente. Verificado em 8/10/2026.
- apagado: " Risco MÉDIO (nome de produto)."

**A5-16**
- antes: Public "A free platform to explore, create, and publicly share"; Server "A self-hosted platform"; Cloud "A fully hosted cloud-based" platform (U3). Verificado em 8/10/2026. Risco BAIXO.
- depois: Public "A free platform to explore, create, and publicly share"; Server "A self-hosted platform"; Cloud "A fully hosted cloud-based" platform (U3). Verificado em 8/10/2026.
- apagado: " Risco BAIXO."

**A5-17**
- antes: IC (fluxo invertido). "First, you start with Power BI Desktop to connect to data and create the report. Then you publish the report to the Power BI service" (U1). Verificado em 8/10/2026. Risco BAIXO.
- depois: IC (fluxo invertido). "First, you start with Power BI Desktop to connect to data and create the report. Then you publish the report to the Power BI service" (U1). Verificado em 8/10/2026.
- apagado: " Risco BAIXO."

**5C-03**
- antes: TC (agrupado e empilhado trocados). Curso 8.2, gráfico de barras: agrupado = subcategorias lado a lado; empilhado = partes de um total; pegadinha do curso: empilhado quando se quer comparar as partes entre si. O item inverte os papéis (redação da v1.1, R-5C1: sem a expressão "lado a lado", que denunciava a troca). Difere do item A5-09 e do par C1 porque estes julgam barras × histograma; este julga as duas variantes do gráfico de barras.
- depois: TC (agrupado e empilhado trocados). Curso 8.2, gráfico de barras: agrupado = subcategorias lado a lado; empilhado = partes de um total; pegadinha do curso: empilhado quando se quer comparar as partes entre si. O item inverte os papéis. Difere do item A5-09 e do par C1 porque estes julgam barras × histograma; este julga as duas variantes do gráfico de barras.
- apagado: " (redação da v1.1, R-5C1: sem a expressão "lado a lado", que denunciava a troca)"

**5C-06**
- antes: TC (tentação: "bigodes vão sempre do mínimo ao máximo" ou "outlier de um lado afeta os dois bigodes" → marcar E). Curso 8.2, box plot: cada bigode vai até o dado mais extremo do seu lado que esteja dentro do limite respectivo; a regra vale por lado; um outlier superior não impede que o bigode inferior termine no mínimo da amostra. Lição O10: a regra de 1,5 · AIQ é convenção usual adotada por muitos programas e pode variar; por isso o item abre com "segundo a regra usual" e não afirma que todo box plot a usa. Sem atribuição a autor. Difere dos itens A5-12 e A5-13 porque aqueles julgam a forma da distribuição e a posição da mediana; este julga a regra dos bigodes por lado.
- depois: TC (tentação: "bigodes vão sempre do mínimo ao máximo" ou "outlier de um lado afeta os dois bigodes" → marcar E). Curso 8.2, box plot: cada bigode vai até o dado mais extremo do seu lado que esteja dentro do limite respectivo; a regra vale por lado; um outlier superior não impede que o bigode inferior termine no mínimo da amostra. A regra de 1,5 · AIQ é convenção usual adotada por muitos programas e pode variar; por isso o item abre com "segundo a regra usual" e não afirma que todo box plot a usa. Sem atribuição a autor. Difere dos itens A5-12 e A5-13 porque aqueles julgam a forma da distribuição e a posição da mediana; este julga a regra dos bigodes por lado.
- apagado: 

**6B-06**
- antes: TC (integridade e disponibilidade trocadas). Curso 4.1.1: integridade = não alteração indevida; disponibilidade = acesso sempre que necessário. Fonte: conceito geral (a definição da tríade não foi confirmada em fonte aberta hoje; ver curso 4.1.1). Tema da tríade CIA também nos itens reais 96 e 98 do TRF6 2024, com outro ponto de julgamento (seção ITENS REAIS, conferida pela QA em 08/10/2026).
- depois: TC (integridade e disponibilidade trocadas). Curso 4.1.1: integridade = não alteração indevida; disponibilidade = acesso sempre que necessário. Fonte: conceito geral (a definição da tríade não foi confirmada em fonte aberta hoje; ver curso 4.1.1). Tema da tríade CIA também nos itens reais 96 e 98 do TRF6 2024, com outro ponto de julgamento (seção ITENS REAIS).
- apagado: ", conferida pela QA em 08/10/2026"

**6B-15**
- antes: GI invertida (tentação: saber que o HTTPS autentica o servidor e concluir que ele garante que o site é o da instituição pretendida → marcar E). Curso 4.3.4 (corrigido pela O-3): HTTPS é o HTTP sobre conexão TLS; o servidor é autenticado para o domínio acessado e a comunicação ganha confidencialidade e integridade, mas isso não garante que o domínio seja o da instituição pretendida nem a boa-fé do titular; páginas fraudulentas, em domínios próprios, também podem usar HTTPS. Fonte: F11, seção 4.2.2 (verificado em 08/10/2026); o restante é conceito geral.
- depois: GI invertida (tentação: saber que o HTTPS autentica o servidor e concluir que ele garante que o site é o da instituição pretendida → marcar E). Curso 4.3.4: HTTPS é o HTTP sobre conexão TLS; o servidor é autenticado para o domínio acessado e a comunicação ganha confidencialidade e integridade, mas isso não garante que o domínio seja o da instituição pretendida nem a boa-fé do titular; páginas fraudulentas, em domínios próprios, também podem usar HTTPS. Fonte: F11, seção 4.2.2 (verificado em 08/10/2026); o restante é conceito geral.
- apagado: " (corrigido pela O-3)"

## 7. Método de contagem de [TS] e VOLÁTIL

Contados **somente nas seções de itens e gabaritos** dos arquivos canônicos: a linha de cada item da seção (d-G) dos lotes GCE e da seção de itens/gabarito dos lotes GCB (formato "C — [TS] — v3 — 5.1 — TC (…)" ou "E [TS]. …"), onde a marca vem logo depois da letra do gabarito. Ficam de fora, por não serem item: o cabeçalho, a Tabela de Correções, a legenda ("[TS] = troca sutil de conceito; VOLÁTIL = …") e os adendos, que citam as palavras sem marcar item (no L3 a T-44 trocou as menções do cabeçalho por "troca sutil, volatilidade", justamente para a contagem bruta por grep refletir só os itens). Cada item lido é conferido contra o registro GBQ v3.

| Lote | [TS] | VOLÁTIL (+REVERIFICAR) | itens VOLÁTEIS |
|---|---|---|---|
| L1 | 10 | 4 | L1-Q14, L1-Q16, L1-Q18, L1-Q19 |
| L1C | 5 | 0 | — |
| L2 | 15 | 0 | — |
| L3 | 15 | 1 | L3-Q21 |
| L4 | 10 | 1 | L4-15 |
| L4C | 5 | 0 | — |
| L5 | 10 | 4 | A5-14, A5-15, A5-16, A5-17 |
| L5C | 5 | 0 | — |
| L6A | 8 | 5 | 6A-01, 6A-09, 6A-10, 6A-14, 6A-15 |
| L6B | 8 | 0 | — |
| **Total** | **91** | **15** | |

Resultado: 91 [TS] (registro v3: 91) e 15 VOLÁTIL em AUTORAL (registro: 15), 180/180 sem divergência. [TS] não é campo do pacote nem aparece em texto exportado (0 ocorrência de "[TS]" no JSON); `volatil: true` é a única marca exportada.

## 8. Pegadinhas (F3, regra (d))

Uma pegadinha por entrada, no formato `{itemEdital, rotulo, texto}`. **`rotulo`**: título do bloco ou subseção que contém a linha "Pegadinha"/"Pegadinha provável", sem numeração inicial e sem marcas, cortado em " — " quando o título tem aposto; quando a pegadinha está direto sob um item que é id do edital, o texto do edital do `itemEdital`; no L6A, sob o título do item do lote (WORD, EXCEL, POWERPOINT, ONEDRIVE, CORREIO ELETRÔNICO…, MICROSOFT TEAMS, GOOGLE MEET). **Desdobramento** só nas fronteiras marcadas pelo texto: enumeradores "(1)", "(2)"… (precedência) ou ";" fora de parênteses e de aspas; assertivas `"…" → ERRADO (…; …)` não se desdobram. A junção dos fragmentos com o separador original reproduz cada entrada da v1.1 (salvo o ponto final): validado em todas as entradas.

| Lote | entradas v1.1 → v1.3 | modos de origem (entradas da v1.1) |
|---|---|---|
| L1 | 8 → 19 | unica 4, enumeradores 1, ponto-e-virgula 3 |
| L1C | 1 → 4 | enumeradores 1 |
| L2 | 8 → 43 | enumeradores 8 |
| L3 | 7 → 42 | enumeradores 7 |
| L4 | 32 → 32 | unica 32 |
| L4C | 0 → 0 | — |
| L5 | 14 → 48 | ponto-e-virgula 14 |
| L5C | 0 → 0 | — |
| L6A | 35 → 35 | unica 35 |
| L6B | 39 → 39 | unica 39 |

Texto corrido que não se separa sem reescrever (ficou como uma entrada só, por contrato): L1 P2-1.1, P2-1.2, P2-1.4 e P2-1.7 (frases soltas "Outra:", "Também:", sem separador marcado). Enumeradores cujo conteúdo tem ";" interno ficaram íntegros (precedência do enumerador): L1 P2-1.3 (1), L2 P2-2.6 (6) e L3 P2-4.3 (2). Assertiva única com ";" dentro do parêntese, mantida inteira: L6A, slide mestre (`"…" → ERRADO (guia Exibir; F7) — VOLÁTIL`). L4, L6A e L6B já tinham uma pegadinha por entrada (contagem igual).

**Reuniões da errata v1.2.1 ponto 2 (fragmento que só se lê com o verbo ou o sujeito do anterior, ou que ilustra o anterior; D-R1-05, D-R1-06; C-06 a C-08): 5 fragmentos reunidos, todos com o separador original "; ":**

- ""Câmara" (instituição) vs "câmara" (sala) é decisão de contexto que o modelo pode errar." — ilustração do fragmento anterior (L1 P2-1.5)
- "empilhado quando se quer comparar as partes entre si." — depende do verbo do fragmento anterior (L5 barras)
- "que a caixa vai do mínimo ao máximo ou contém todos os dados" — depende do verbo do fragmento anterior (L5 box plot)
- "que os bigodes vão até 1,5 desvio padrão" — depende do verbo do fragmento anterior (L5 box plot)
- "que mostra frequência por intervalo (isso é histograma)." — depende do verbo do fragmento anterior (L5 box plot)

Fragmentos que dependem do verbo ou do sujeito do fragmento anterior e ficaram como entrada própria: **0** (na R0 eram 5, resolvidos pelas reuniões acima; contagem de pegadinhas 267 → 262). Os fragmentos de L5 que restam começam por infinitivo e se leem soltos; L1 P2-1.6 e P2-1.8 começam por minúscula mas se leem sozinhos (fronteira mantida).

## 9. Validação por script (107 verificações, 0 falhas)

- OK JSON parseia sem erro; termina em newline; UTF-8
- OK formato: indent=1 e ensure_ascii=False (reserialização idêntica)
- OK chaves de topo e valores
- OK 0 id duplicado (286 ids)
- OK 14 campos obrigatórios presentes em todos os itens
- OK tipos: ano/numero int; demais str
- OK campos extras só dentre comandoOriginal, volatil, nota
- OK nenhum item sem id, enunciado e gabarito C/E
- OK 0 "QA PENDENTE" no JSON
- OK edital: 47 entradas = v1.1 (idêntico)
- OK todo itemEdital existe no edital
- OK aderencia só direta|parcial; rotulo permitido
- OK volatil só true; nota só str não vazia; comandoOriginal só str não vazia
- OK 0 ocorrência de 'ENTREGA DE LOTE'
- OK 0 ocorrência de 'FIM DA PARTE'
- OK 0 ocorrência de 'FIM DO LOTE'
- OK 0 ocorrência de '====='
- OK 0 ocorrência de 'Fundador: gravar'
- OK 0 ocorrência de 'Observação para a GCB-CQFP'
- OK 0 ocorrência de 'Derep, antigo DETAQ'
- OK banco: 112 linhas no CSV; 106 exportáveis (C/E, não anuladas); exportados = exportáveis
- OK banco: 6 anuladas fora (BQ-0029, 0030, 0031, 0060, 0062, 0063)
- OK banco: id, gabarito, enunciado, itemEdital, certame, cargo, url, ano, numero = CSV (106/106)
- OK banco: 60 C / 46 E — {'C': 60, 'E': 46}
- OK banco: comando = texto_comando; textoBase = texto_base ou "" (106/106)
- OK banco: aderencia = coluna aderencia do CSV (106/106), sem recálculo
- OK banco: 67 direta / 39 parcial — {'parcial': 39, 'direta': 67}
- OK banco: os 60 da v1.1 com o MESMO comando (60/60)
- OK banco: os 60 da v1.1 com aderência igual (37 direta/23 parcial)
- OK banco: textoBase não vazio só em BQ-0049, 0050, 0051; os 60 da v1.1: textoBase = texto da v1.1 ou ""
- OK banco: volatil = 8 (BQ-0015, 0017, 0035, 0064, 0075, 0076, 0086, 0089)
- OK nota: só BQ-0003 e BQ-0040; valor = texto do contrato (regra 4 da v1.1.1) e = trecho final de observacoes
- OK banco: BQ-0072, 0077, 0084, 0109, 0110, 0111 presentes; BQ-0110 sem nota
- OK banco: 0 item normalizado; BQ-0070, 0071, 0112 com comando inteiro e sem comandoOriginal
- OK AUTORAL: 180 ids = registro v3 (180/180)
- OK AUTORAL: gabarito = registro v3 (180/180)
- OK AUTORAL: subitem compatível com o registro (180/180)
- OK AUTORAL: volatil = VOLÁTIL + REVERIFICAR do registro (15) — ['6A-01', '6A-09', '6A-10', '6A-14', '6A-15', 'A5-14', 'A5-15', 'A5-16', 'A5-17', 'L1-Q14', 'L1-Q16', 'L1-Q18', 'L1-Q19', 'L3-Q21', 'L4-15']
- OK AUTORAL: 89 C / 91 E — {'E': 91, 'C': 89}
- OK AUTORAL: [TS] no registro = 91; [TS] lido dos d-G dos arquivos canônicos = registro (180/180)
- OK AUTORAL: justificativa não vazia; banco: justificativa vazia
- OK AUTORAL: textoBase "" em 180/180 (F2); 0 "nenhum" em textoBase (286)
- OK F2: textoBase vazio em 283 de 286 itens (283 = 286 − 3 de BQ-0049..51)
- OK volatil total = 23 (banco 8 + AUTORAL 15), L3-Q21 marcado
- OK normalização: 90 itens com comandoOriginal = L4 20, A5/L5 20, 4C/L4C 10, 5C/L5C 10, L6A 15, L6B 15 — {'L4': 20, 'L4C': 10, 'L5': 20, 'L5C': 10, 'L6A': 15, 'L6B': 15}
- OK normalização: comando = comandoOriginal com só o trecho da numeração trocado por "julgue os itens a seguir."
- OK normalização: parte da frase anterior a "julgue os itens" idêntica (resto literal)
- OK normalização: nenhum comando restante com faixa de itens; L1–L3 (90) sem comandoOriginal e com comando literal
- OK normalização: base v1.1 também 90 (mesma contagem por lote)
- OK AUTORAL v1.1 → v1.2: campos alterados só textoBase(180), comando/comandoOriginal(90), justificativa(21), enunciado(1: L1-Q04) — {'comando': 90, 'comandoOriginal': 90, 'enunciado': 1, 'justificativa': 21, 'textoBase': 180}
- OK F1: L1-Q04 contém "áudio–texto"; 0 "áudio– texto" no JSON
- OK F1: nenhuma outra letra+"– "+letra no JSON (efeito de quebra de linha)
- OK F4 (R1): 21 justificativas alteradas (21 = 18 da R0 + 6B-06, 6B-15, L2-Q21)
- OK F4 (R1): cada alteração é SÓ deleção, salvo as 2 trocas de caixa fechadas da C-05 (4C-08, 5C-06: minúscula → maiúscula na inicial)
- OK F4: justificativas finais = depois
- OK F4 (R1/C-09): 0 marca de processo (CQFP/CQE/CPP/GCE/GCB/GBQ/EXEC/T-xx/(vN/Oxx/Lição/R-4C1/Risco + QA, O-n, Retificação, "Gabarito C|E mantido") nas 180 justificativas AUTORAL
- OK F5: 0 "Derep, antigo DETAQ"; "Derep (antigo DETAQ)" no L1 (curso, E10) — ocorrências totais da forma correta: 13
- OK contagem por lote = declarada {'L1': 20, 'L1C': 10, 'L2': 30, 'L3': 30, 'L4': 20, 'L4C': 10, 'L5': 20, 'L5C': 10, 'L6A': 15, 'L6B': 15}
- OK lotes: itensEdital, pares e pegadinhas são listas JSON em 10/10 lotes; itensEdital ⊂ edital
- OK lotes: campos id, nome, prova, itensEdital, resumo, curso, pares, pegadinhas (+ legendaMecanismo, opcional, só em L4, L4C, L5, L5C, L6A, L6B)
- OK v1.3 legendaMecanismo: 6 lotes, string não vazia, literal da tabela 2.3 do QA da T-53 (L4 = L4C = L5C; L5 "Mecanismos: …"; L6A = L6B "atribuição errada (AT)"); L1, L1C, L2, L3 sem o campo
- OK v1.3 legendaMecanismo: sem ponto final, sem quebra de linha, e ocorre literal (1 vez, em linha "Legenda:") no arquivo canônico do lote
- OK lotes: itensEdital iguais aos da v1.1 (10/10)
- OK pares por lote iguais à v1.1 (L1 17, L2 22, L3 28, L4 20, L5 15, L6A 19, L6B 18)
- OK pegadinhas.itemEdital existem no edital
- OK F3: toda pegadinha tem itemEdital, rotulo (não vazio) e texto (não vazio), nessa ordem
- OK F3: todo rotulo é trecho literal do arquivo canônico do lote ou do edital (sem marcas internas)
- OK F3: nenhum rotulo com marca interna ([V, [TS], F1.., U1.., verificado em, ITEM)
- OK F3 (R1): pegadinhas L1 19, L5 48, total 262 (R0: 20, 52, 267); 5 reuniões registradas (C-06 a C-08) — {'L1': 19, 'L1C': 4, 'L2': 43, 'L3': 42, 'L4': 32, 'L4C': 0, 'L5': 48, 'L5C': 0, 'L6A': 35, 'L6B': 39}
- OK F3: a junção dos fragmentos (separador original) reproduz cada entrada da v1.1, salvo o ponto final
- OK erratas: 32 aplicações registradas; 0 FALHA; estados {'APLICADA': 31, 'JÁ PRESENTE': 1}
- OK erratas: Y de cada errata presente no JSON (27 aplicações com Y)
- OK erratas: X de cada errata ausente do JSON (fora das ocorrências de Y)
- OK erratas fora do exportado: alvo existe no arquivo e X/Y NÃO vai ao JSON — [{'lote': 'L1', 'id': 'E6', 'em_arquivo': True, 'no_json': False}, {'lote': 'L1', 'id': 'E11', 'em_arquivo': True, 'no_json': False}, {'lote': 'L1C', 'id': 'E2', 'em_arquivo': True, 'no_json': False},
- OK L1 E12: resumo do L1 contém a Y e não contém "não mede pontuação nem locutor"
- OK L2 E7: resumo do L2 (2.4) com Y
- OK L3 E4: par 20 com "suprimida pela MP nº 869/2018, convertida na Lei 13.853/2019" e 0 "suprimida pela Lei 13.853/2019)"
- OK L3 Adendo 2: "Contexto institucional — Ato da Mesa nº 225" 1 vez no curso (4.1), 3.1 sem duplicata; bloco T-08/T-44 do 3.1 intacto
- OK L3 Adendo 2: texto inserido = texto literal do Adendo 2 da consolidação
- OK L5 Tukey (T-47): curso do L5 8.2 contém "O fator 1,5·AIQ é a convenção usual (Tukey); outras convenções existem e a prova costuma cobrar esta."
- OK INFO DETAQ fora da forma "Derep (antigo DETAQ)" em curso/resumo
- OK discursivas: 5 (D1–D5) idênticas à v1.1
- OK discursivas: sem observação "inferido pela EXEC" (0 ocorrência)
- OK discursivas: "14,30" (E11) não aparece em comando/padrão (E11 sem efeito no exportado)
- OK D4: anexo R2–R4 é cópia literal das linhas 14–23 do arquivo de padrões
- OK D5: anexo R2–R4 é cópia literal das linhas 14–23 do arquivo de padrões
- OK simulados: ids [SIM-0, SIM-1, SIM-2, SIM-0-P2]; tipos; versões
- OK simulados: n = tamanho de itens = 60, 40, 40, 25; chaves id,nome,tipo,versao,n,itens (+ avisos, opcional, só no SIM-0)
- OK v1.3 avisos (SIM-0): lista de 3 strings = avisos 1, 2 e 4 da folha canônica, sem a numeração; aviso 2 com a sublista na mesma string, recuo de 3 espaços; avisos 3, 5, 6, 7 e 8 não entram
- OK v1.3 avisos: início literal "**Simulado diagnóstico, não final.**", "**Aderência PARCIAL (23 itens).**", "**Desequilíbrio C/E (contagem real).**"; aviso 1 mantém "(D-ADERENCIA: parcial só em diagnóstico)" no campo (D-T53-07); só o SIM-0 tem o campo
- OK simulados: todo id de simulado existe em itens; 0 repetido dentro de cada simulado
- OK simulados: gabarito do simulado (arquivo *_gabarito.md) = gabarito do item no pacote (165/165)
- OK SIM-0: 60 do banco; = banco (comando+texto da folha); 33 C/27 E; 4 volatil (BQ-0015, 0017, 0035, 0064); 23 parcial
- OK SIM-0 = os 60 BQ da v1.1 (mesma lista e ordem)
- OK SIM-1 = v1.1 (40 ids, mesma ordem)
- OK SIM-1: só AUTORAL; sem volatil; sem parcial; C/E={'C': 20, 'E': 20}
- OK SIM-2: só AUTORAL; sem volatil; sem parcial; C/E={'C': 20, 'E': 20}
- OK SIM-0-P2: só AUTORAL; sem volatil; sem parcial; C/E={'C': 13, 'E': 12}
- OK SIM-1 20 C/20 E; SIM-2 20 C/20 E; SIM-0-P2 13 C/12 E
- OK simulados finais SIM-1 e SIM-2 sem item de L4-11 nem BQ-0010; SIM-2 (P2) só L1–L3
- OK simulados: SIM-0-P2 ∩ SIM-2 = ∅; SIM-1 ∩ SIM-2 = ∅; SIM-0 ∩ (SIM-1, SIM-2, SIM-0-P2) = ∅
- OK SIM-1: ordem dos ids = ordem do mapa (40); texto da folha = enunciado do pacote (40/40)
- OK SIM-2: ordem dos ids = ordem do mapa (40); texto da folha = enunciado do pacote (40/40)
- OK SIM-0-P2: ordem dos ids = ordem do mapa (25); texto da folha = enunciado do pacote (25/25)
- OK SIM-0: ordem dos ids = ordem do mapa (60); texto da folha = enunciado do pacote (60/60)
- OK SIM-0: bloco "Comando" da folha = textoBase + comando do pacote (60/60; 57 só comando, 3 com texto-base)
- OK SIM-0 v0.2: Aviso 6 com a frase da errata de forma (T-36) e 0 "aguardam a conferência"

## 10. Edição do estudante (`saida/estudante/`)

Gerada a partir do `pacote.json` v1.3 (fonte única). **43 arquivos**, os mesmos nomes da v1.2: `README.md` (índice, versão v1.3, data 2026-10-13, aviso "material de estudo; gabaritos em arquivo separado"); por lote, `<ID>_estudo.md` (itens do edital, resumo, curso, pares, pegadinhas com rótulo), `<ID>_itens.md` (texto-base se houver, comando e enunciado, nessa ordem; sem gabarito, justificativa nem marcas) e `<ID>_gabarito.md` (gabarito, item do edital e justificativa; **no topo, a `legendaMecanismo` literal do lote, nos 6 lotes que a têm**) para L1, L1C, L2, L3, L4, L4C, L5, L5C, L6A e L6B (30 arquivos); `BANCO_itens.md` e `BANCO_gabarito.md` (certame, cargo, ano, número, URL oficial, aviso VOLÁTIL e `nota` literal, sem o identificador de decisão); por simulado `<SIM>_folha.md` (sem o id de origem dos itens) e `<SIM>_gabarito.md` (SIM-0, SIM-1, SIM-2, SIM-0-P2); `DISCURSIVAS.md` e `DISCURSIVAS_padrao.md`. Resumo e curso vão em blocos de texto cercados, para preservar quebras, recuos e tabelas. **Os `avisos` do SIM-0 não são exibidos** (D-T53-02/item 3 da lista: até decisão do Fundador sobre o que se compartilha com a candidata); a fidelidade confere que o texto dos três avisos não aparece em arquivo algum.

**Regra:** as marcas internas saem SOMENTE POR DELEÇÃO (nunca reescrita) por `estudante_marcas.py` e `literais.py`, com as exceções fechadas da reconciliação R1: (i) CAIXA (C-05 e C-15): minúscula → maiúscula da primeira letra de um trecho, lista de 8 pares só em `L6A_estudo` (e as 2 trocas de caixa na F4 do pacote); (ii) reunião de fragmentos de pegadinha com "; " (C-06 a C-08, só no pacote); (iii) a `nota` de BQ-0003 sai da edição sem " (D-LEI-15352)" (C-18; errata v1.2.1 ponto 3), só na exibição. A marca VOLÁTIL vira, nos itens `volatil: true`, o aviso fixo "Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027."; a `nota` (BQ-0003, BQ-0040) é exibida junto do item. Enunciado, comando e texto-base de item não são tocados (afirmado por teste: nenhuma marca da lista neles). **Novidade da v1.3 (N-1, D-R2-01):** duas regras literais, só em `L6B_estudo`, apagam "Nesta produção " e " (a especificação previa o item "se houver base")" do curso 4.0.2 (o "NÃO" que segue já tem inicial maiúscula); no pacote a marca fica, por desenho (D-PACOTE-V11). Regras genéricas (por tipo) e regras literais (frase ou cláusula a apagar, `⟦…⟧` na especificação; 110 regras literais vigentes, apêndice A):

- `[V dd/mm/aaaa — …]` apagado inteiro, com o espaço anterior (o colchete pode quebrar linha entre "[V" e a data); duas exceções que mantêm a orientação ao estudante: `[V … — F4; NORMATIVO — QA; norma de caráter experimental, não cobrar o texto]` fica `[norma de caráter experimental, não cobrar o texto]` e `[V … contexto histórico]` fica `[contexto histórico]`.
- `[NORMATIVO — QA: base legal]` perde o prefixo e o colchete e fica a base legal ("LGPD, art. 5º, I."); `[NORMATIVO — QA]` e as variantes com ";" são apagadas (`[NORMATIVO — QA; não cobrar além do texto]` fica `[não cobrar além do texto]`); a frase "…com a marca [NORMATIVO — QA]. Fontes: F1 … lidas em 08/10/2026." do L3 sai, ficando "Todos os dispositivos abaixo estão em paráfrase."
- Referências de fonte F1…F22: `[Fn]`, `(Fn)`, `(Fn, Fm)`, `(Fn, verificado em …)`, `(Fn, seção …)`, `, Fn)` no fim de parêntese, `; Fn)`, `(Fn: ` e `(Fn, "…")` (mantém o parêntese e o conteúdo), "Conforme a Fn (leitura de …):", frases "Fonte(s): Fn, …verificado em …." e, em trechos de prosa, a cláusula ou palavra que só existe por causa da referência (lista completa no apêndice A). "A tecla F4" (Excel) NÃO é referência e permanece; a frase restaurada da L4-11 ("O F4 afirma que …") permanece (D-R1-07, opção (a)).
- Agentes e unidades (CQFP, QA, GCB, GCE, CPP) em carimbos como "(conferido pela CQFP em 08/10/2026)", "conforme a CQFP", "(GCB-CPP)", "Decisão da GCE", "versão da CPP", "para o QA Normativo", "Síntese da CQFP … colado pelo Fundador"; ids internos "(errata E1)", "; E3" em "(N1; E3)", "(O11)", "(D-T2)", "(R4 do Projeto)" e, nos padrões D4/D5, "(GCE, R2–R4)" e os enumeradores "R2. ", "R3. ", "R4. ".
- Carimbos datados ligados a uma referência apagada ("verificadas em 7/10/2026", "(reverificado em …)", "conforme a leitura de 08/10/2026", "(conferido no Planalto em …)") e, na R1, "aberta(s) hoje" (9 pontos, L6A e L6B), "(v2, …)" no L1C (2), " neste chat" no L4 (1), classificação interna de VOLÁTIL nas justificativas (4), carimbo "Verificado em 8/10/2026" do L5 (4).
- Códigos de fonte do L5 (U1–U6, GG4, TB2; só `L5_*`, 33 remoções) e códigos de nota N do L2 e do L3 (`(N1)`, `Ver N5:` etc.; só `L2_*` e `L3_*`, 14 remoções); os códigos N1–N4 do L4 ficam (definidos no próprio texto).

### 10.1 Marcas removidas por tipo e por arquivo

Contagem de ocorrências apagadas, por arquivo gerado (um item presente em lote e em simulado é contado nos dois arquivos). Total nos arquivos: **571**.

| Tipo | Ocorrências |
|---|---|
| F (parêntese) | 87 |
| V | 58 |
| F (prosa: referência a fonte) | 54 |
| F (fim de parêntese) | 48 |
| F (frase "Fonte(s): …") | 42 |
| código de fonte do L5 (U/GG/TB) | 33 |
| F (colchete) | 26 |
| agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | 26 |
| F (parêntese com verificação) | 26 |
| NORMATIVO — QA (prefixo da base legal) | 23 |
| NORMATIVO — QA | 18 |
| código N do L2/L3 | 14 |
| F (início de parêntese) | 14 |
| F (fim de parêntese, após vírgula) | 13 |
| id interno (R-xx, E-xx, O-xx, D-xx) | 12 |
| F (frase de fonte) | 11 |
| F ("Conforme a Fn (leitura …):") | 11 |
| carimbo de leitura "aberta(s) hoje" | 9 |
| caixa (minúscula → maiúscula na inicial deixada por deleção) | 8 |
| carimbo datado de verificação/leitura (ligado a F-ref) | 7 |
| F (parêntese com seção/verificação) | 5 |
| classificação interna de VOLÁTIL na justificativa | 4 |
| carimbo "Verificado em 8/10/2026" (L5) | 4 |
| id de decisão na nota (D-LEI-15352) | 4 |
| id interno / versão do lote (v2) | 2 |
| V (parcial: mantém a orientação ao estudante) | 2 |
| F (fim de parêntese, "com Fn") | 2 |
| marca de processo de produção do lote ("Nesta produção" / "a especificação previa") | 2 |
| NORMATIVO — QA (parcial: mantém a orientação ao estudante) | 1 |
| NORMATIVO — QA (frase de marca e fontes) | 1 |
| F (fim de parêntese, após travessão) | 1 |
| F (início de parêntese, antes de aspas) | 1 |
| marca de processo ("neste chat") | 1 |
| F (parêntese com leitura) | 1 |
| **Total** | **571** |

| Arquivo | Total | Detalhe por tipo |
|---|---|---|
| BANCO_gabarito.md | 1 | id de decisão na nota (D-LEI-15352) 1 |
| BANCO_itens.md | 1 | id de decisão na nota (D-LEI-15352) 1 |
| DISCURSIVAS_padrao.md | 14 | id interno (R-xx, E-xx, O-xx, D-xx) 9; agente/unidade interna (CQFP, QA, GCB, GCE, CPP) 5 |
| L1C_estudo.md | 4 | id interno / versão do lote (v2) 2; V 1; id interno (R-xx, E-xx, O-xx, D-xx) 1 |
| L1C_gabarito.md | 3 | F (colchete) 2; V 1 |
| L1_estudo.md | 52 | V 37; F (colchete) 15 |
| L1_gabarito.md | 7 | F (colchete) 6; V 1 |
| L2_estudo.md | 25 | V 12; código N do L2/L3 8; V (parcial: mantém a orientação ao estudante) 2; F (colchete) 1; id interno (R-xx, E-xx, O-xx, D-xx) 1; F (parêntese) 1 |
| L2_gabarito.md | 4 | V 2; F (colchete) 1; classificação interna de VOLÁTIL na justificativa 1 |
| L3_estudo.md | 30 | NORMATIVO — QA 18; código N do L2/L3 6; agente/unidade interna (CQFP, QA, GCB, GCE, CPP) 2; NORMATIVO — QA (parcial: mantém a orientação ao estudante) 1; NORMATIVO — QA (frase de marca e fontes) 1; V 1; F (fim de parêntese, após vírgula) 1 |
| L3_gabarito.md | 14 | NORMATIVO — QA (prefixo da base legal) 13; classificação interna de VOLÁTIL na justificativa 1 |
| L4C_gabarito.md | 12 | F (parêntese) 6; F (frase de fonte) 3; F (prosa: referência a fonte) 3 |
| L4_estudo.md | 84 | F (parêntese) 22; agente/unidade interna (CQFP, QA, GCB, GCE, CPP) 16; F (parêntese com verificação) 15; F (prosa: referência a fonte) 15; F (início de parêntese) 5; F (fim de parêntese, após vírgula) 4; carimbo datado de verificação/leitura (ligado a F-ref) 3; F (fim de parêntese, após travessão) 1; F (início de parêntese, antes de aspas) 1; id interno (R-xx, E-xx, O-xx, D-xx) 1; marca de processo ("neste chat") 1 |
| L4_gabarito.md | 24 | F (frase "Fonte(s): …") 15; F (parêntese) 4; F (prosa: referência a fonte) 2; carimbo datado de verificação/leitura (ligado a F-ref) 1; classificação interna de VOLÁTIL na justificativa 1; F (início de parêntese) 1 |
| L5_estudo.md | 28 | código de fonte do L5 (U/GG/TB) 27; agente/unidade interna (CQFP, QA, GCB, GCE, CPP) 1 |
| L5_gabarito.md | 10 | código de fonte do L5 (U/GG/TB) 6; carimbo "Verificado em 8/10/2026" (L5) 4 |
| L6A_estudo.md | 139 | F (fim de parêntese) 48; F (parêntese) 39; F (prosa: referência a fonte) 20; F ("Conforme a Fn (leitura …):") 11; caixa (minúscula → maiúscula na inicial deixada por deleção) 8; F (fim de parêntese, após vírgula) 4; F (início de parêntese) 4; carimbo datado de verificação/leitura (ligado a F-ref) 2; carimbo de leitura "aberta(s) hoje" 2; F (parêntese com leitura) 1 |
| L6A_gabarito.md | 20 | F (frase "Fonte(s): …") 15; F (parêntese) 2; F (prosa: referência a fonte) 2; F (início de parêntese) 1 |
| L6B_estudo.md | 49 | F (parêntese com verificação) 11; F (parêntese) 9; carimbo de leitura "aberta(s) hoje" 6; F (parêntese com seção/verificação) 5; F (fim de parêntese, após vírgula) 4; F (prosa: referência a fonte) 4; F (início de parêntese) 2; F (fim de parêntese, "com Fn") 2; agente/unidade interna (CQFP, QA, GCB, GCE, CPP) 2; marca de processo de produção do lote ("Nesta produção" / "a especificação previa") 2; F (frase de fonte) 1; carimbo datado de verificação/leitura (ligado a F-ref) 1 |
| L6B_gabarito.md | 11 | F (prosa: referência a fonte) 5; F (frase de fonte) 5; carimbo de leitura "aberta(s) hoje" 1 |
| SIM-0-P2_gabarito.md | 6 | NORMATIVO — QA (prefixo da base legal) 4; V 1; classificação interna de VOLÁTIL na justificativa 1 |
| SIM-0_folha.md | 1 | id de decisão na nota (D-LEI-15352) 1 |
| SIM-0_gabarito.md | 1 | id de decisão na nota (D-LEI-15352) 1 |
| SIM-1_gabarito.md | 22 | F (frase "Fonte(s): …") 12; F (parêntese) 4; F (prosa: referência a fonte) 3; F (frase de fonte) 2; F (início de parêntese) 1 |
| SIM-2_gabarito.md | 9 | NORMATIVO — QA (prefixo da base legal) 6; V 2; F (colchete) 1 |

Referência: na v1.2 as remoções somaram 569; a v1.3 soma 571 (as 2 a mais são as da N-1, em `L6B_estudo.md`).

Arquivos sem nenhuma remoção: os `*_itens.md`, `BANCO_*`, `*_folha.md`, `README.md` e os `*_gabarito.md` cujos itens não tinham marca (a tabela só lista os arquivos com remoção).

### 10.2 Fidelidade (script `estudante_fidelidade.py`)

O script lê os 43 arquivos com um parser próprio (independente do gerador) e confere, campo a campo, o texto do estudante com o do pacote: (1) igual ao texto do pacote com as deleções das regras; (2) obtido do texto do pacote só por deleção (difflib: apenas `equal`/`delete`, salvo as 8 trocas de caixa da lista CAIXA, C-15); (3) comando, texto-base, enunciado, gabarito, item do edital, aderência, nota (com a única exceção da C-18), aviso VOLÁTIL, certame, cargo, ano, número, URL, ordem e `n` dos simulados, valores dos aspectos e conceitos dos quesitos idênticos ao pacote; (4) **v1.3:** a `legendaMecanismo` de cada lote com o campo está literal, sozinha, no topo do `*_gabarito.md` do próprio lote (antes do primeiro item) e em nenhum outro arquivo; lote sem o campo não tem texto antes do primeiro item; o texto dos `avisos` não aparece na edição. Teste negativo (`fidelidade_mutacao.py`: mutação de 4 arquivos — um enunciado, um gabarito, um trecho de curso e uma legenda) detectou 5 diferenças em `(legenda)`, `L1_itens.md`, `L2_gabarito.md`, `L3_estudo.md`, `L5_gabarito.md`, portanto o script não é cego.

- comparações: texto 1380, metadado 802, estrutura 48, prova/metadado 1883, aviso/nota 1067, gabarito 451, legenda 16, avisos não exibidos 3 (total 5650)
- **diferenças: 0** (texto do estudante == texto do pacote com as deleções aplicadas)
- marcas residuais nos arquivos pela varredura de higiene (V, NORMATIVO — QA, [TS], CQFP/CQE/CPP/GCE/GCB/GBQ/EXEC, F1…F22, T-/R-/E-/O-xx, "(errata En)"): 2, a saber: L4_gabarito.md linha 58 "F4" (sujeito da frase restaurada da L4-11 (exceção registrada, D-R1-07 opção (a))); L6A_estudo.md linha 83 "F4" (tecla do Excel, não é referência).

## 11. Marcas que permanecem (varredura)

**No `pacote.json` (por desenho):** curso, resumo, pegadinhas e justificativas AUTORAL conservam as marcas de processo do arquivo canônico, porque o pacote é dado, não edição do estudante (decisão do gatilho A: só a edição do estudante as retira, e a F4 limpou apenas as 18 justificativas com marca de agente/risco/lição). Contagem no JSON: `[V …]` 57; `[NORMATIVO — QA…]` 33; referências F1…F22 402; CQFP/CPP/GCE/GCB/QA em texto de lote 24.

**Na edição do estudante** as varreduras da seção 3.5 do QA da R2 dão 0 (conferência (4), seção 13): `;)`, ` — $`, `****`, `abertas? hoje`, `(v2,`, `D-LEI-15352`, `neste chat`, `Retificação`, `Gabarito [CE] mantido`, códigos U/GG/TB/CI, códigos N (L1, L1C, L2, L3, SIM-2, SIM-0-P2), ` — <id>` nas folhas, `erificado em 8/10/2026` (L5); mais [TS], `[V `, CQFP/CQE/GCE/GCB/GBQ/CPP, `T-n`, QA, `O-n`, "Lição O", `R-nCn`, "NÃO VOLÁTIL", "Sem marca VOLÁTIL", REVERIFICAR e `\bD-XX`; e, da N-1, "Nesta produção" e "especificação previa".

**Permanecem na edição, por decisão da reconciliação (D1 da GBQ):** `a tecla F4` (`L6A_estudo.md` 83) e `O F4 afirma que …` (`L4_gabarito.md`, L4-11; D-R1-07); "VOLÁTIL" fora do aviso fixo em 7 linhas de títulos, rubricas e orientação de estudo (L4_estudo.md:23; L4_estudo.md:210; L5_estudo.md:24; L5_estudo.md:104; L5_estudo.md:107; L6A_estudo.md:125; L6A_estudo.md:268; D-R1, 2.3-g); etiquetas GI/TC/AT/IC nas justificativas (2.3-h), **agora com a legenda literal do lote no topo do `*_gabarito.md` dos 6 lotes que a têm**; códigos N1–N4 do L4 (2.3-e); `(Derep (antigo DETAQ); …)` no `L1_estudo.md` (literal pela F5; D-R1-15 DESCARTADO); 29 justificativas iniciadas em minúscula depois do prefixo de campo (forma do canônico; D-R1-18 DESCARTADO); "que eu possa afirmar" em `L3_estudo.md` 422 (texto canônico da GCE; 2.3-i, BACKLOG); remissões a pares por id não exportado ("par C1", "par C14", "C19") em justificativas de A5-09, 5C-03, 5C-07 e 4C-08 (D-R1-21, BACKLOG); referentes perdidos em deleções (L6A 135 "As duas páginas"; L5 seção/módulo; 6B-06; L3 101/574; QA R2 N-5, BACKLOG, aditamento à T-54); nota R2 da D4 repetida na D5 e rótulo "Nota: nota de vigência:" (D-R1-17); quadro-síntese do L1 desalinhado e separador "×" dos pares (D-R1-14/16, BACKLOG). **Os avisos 1, 2 e 4 do SIM-0 saíram do "adiado" da R1 para o pacote** (campo `avisos`), mas continuam fora da edição (decisão do Fundador).

## 12. DÚVIDAS para a GBQ

**DÚVIDAS da v1.2 (R0), decididas na reconciliação R1 (`T48_reconciliacao_R1_2026-10-13.md`, tabela 2.2) e fechadas na R2 (`T48_reconciliacao_R2_2026-10-13.md`, D-R2-06):**

| DÚVIDA (R0) | Decisão que a resolve | Efeito nesta ocorrência |
|---|---|---|
| 1 — F4: 18 em vez de 17 | D-R1-02, D-R1-03, D-R1-20 (aceitar as 18; com 6B-06, 6B-15 e L2-Q21, 21) | F4 = 21 justificativas (seção 6) |
| 2 — minúscula depois de "Lição O10: " | D-R1-04 (capitalização autorizada, C-05) | 2 trocas de caixa na F4 do pacote (4C-08, 5C-06) |
| 3 — fragmentos dependentes / entradas não desdobradas | D-R1-05, D-R1-06 (C-06 a C-08); errata v1.2.1 ponto 2 | pegadinhas 262 (seção 8) |
| 4 — rótulo por hierarquia | tabela 2.2 (aceitar) | rótulos literais mantidos |
| 5 — marcas fora da lista | tabela 2.3 (C-17 a C-23), só na edição | seção 10; apêndice A |
| 6 — "Risco" | tabela 2.2 (confirmar; conteúdo de estudo) | sem mudança |
| 7 — conteúdo substantivo perdido | D-R1-07 (restaurar a frase da L4-11) | frase restaurada na edição |
| 8 — minúscula e sujeito oculto no L6A | D-R1-11, D-R1-12 (C-15, C-16) | 8 trocas de caixa; 3 deleções |
| 9 — tabelas de colunas fixas | D-R1-16 (BACKLOG) | sem mudança |
| 10 — aviso único para REVERIFICAR normativo | tabela 2.3 (f), C-21 | classificação interna apagada |
| 11 — aderência no gabarito do estudante | tabela 2.2 (manter só no gabarito) | sem mudança |
| 12 — quarto estado "FORA DO PACOTE" | tabela 2.2 (aceitar como rótulo de relatório) | seção 3.1 |
| 13 — alvo duplicado da E3a do L3 | tabela 2.2 (aceitar) | sem mudança |

**DÚVIDAS desta ocorrência (v1.3), cada uma com a decisão que a resolve; nenhuma impede o aceite:**

14. **Forma de exibição da `legendaMecanismo`.** No topo de cada `L<lote>_gabarito.md` com o campo, como uma linha própria, o literal do canônico sem rótulo novo ("Mecanismo: troca de conceito (TC), …" ou "Mecanismos: TC troca de conceito; …"), seguida de linha em branco. Acrescentar um título ("Legenda") seria texto novo. Remissão: D-T53-01 (leitura conservadora, sem texto novo); extensão aos `SIM-*_gabarito.md` e `BANCO_gabarito.md` é BACKLOG (D-T53-01). Se a GBQ quiser moldura, decide em D1.
15. **Aviso 2 do SIM-0 remete a uma marca ausente da folha.** A string do aviso 2 no campo `avisos` diz que cada item parcial traz, logo abaixo, a marca `[ADERÊNCIA PARCIAL ...]`, e o aviso 1 traz "(D-ADERENCIA: parcial só em diagnóstico)". Ambos ficam literais no campo (v1.2.1 ponto 5). Remissão: D-T53-03 e D-T53-07 (BACKLOG, condicionados à decisão do Fundador de exibir os avisos; a deleção mínima, se exibir, é só "D-ADERENCIA: " no aviso 1).
16. **Varredura `D-[A-Z]{2,}` da seção 3.5 do QA da R2 sem `\b`.** Sem fronteira de palavra o padrão casa dentro de "TID-IA", "TID-DADOS-VIZ" (títulos dos lotes) e "END-TO-END": 14 ocorrências, as mesmas da v1.2. A conferência usa `\bD-[A-Z]{2,}` (0 ocorrência). Sem decisão a tomar; proposta: DESCARTADO. Remissão: QA_T48_R2, seção 3.5 (resultado 0 lido com fronteira de palavra).

## 13. Ocorrência v1.3 (T-56)

Ocorrência antecipada da T-12 (D-V13-AGORA, Fundador, 13/10/2026), com o gerador de `saida/pacote/gerador_v1_2/` copiado para `saida/pacote/gerador_v1_3/` (a v1.2 ficou intacta). Despacho: PROMPT DE PARTIDA lido com as Regras da v1.2 (a)–(j), a errata v1.2.1 (pontos 1–5) e as D1 da GBQ da reconciliação R2, seção 2 (D-T53-02, item 4 da lista).

### 13.1 Itens da lista PARA A PRÓXIMA T-12 (reconciliação R2, seção 4) e pontos de caminho da T-55 (seção 4)

| Item | Como foi feito | Onde se confere |
|---|---|---|
| 1 — N-1 (D-R2-01) | deleção pura em `L6B_estudo.md` (curso 4.0.2): "Nesta produção " e " (a especificação previa o item \"se houver base\")"; só na edição; o pacote conserva a marca (D-PACOTE-V11). 2 regras literais novas (apêndice A, últimas) | conferência (3), seção 13.3 |
| 2 — N-3 (D-R2-02) | este relatório é gerado por inteiro por `relatorio_v1_3.py`, com as contagens da v1.3 em todas as seções; o Apêndice A lista só as regras vigentes (sem as nº 6, 26 e 63 da R0, retiradas na R1; as nº 42, 44 e 51 da R0 na forma da C-16; mais as regras do item 1); as DÚVIDAS novas levam remissão à decisão que as resolve (seção 12) | seções 1 a 12 e Apêndice A |
| 3 — T-53 pontos 4 e 5 (D-T53-01) | `legendaMecanismo` em L4, L4C, L5, L5C, L6A e L6B, literal do canônico de cada lote (tabela 2.3 do QA da T-53); `avisos` no SIM-0 (avisos 1, 2 e 4 literais da folha, aviso 2 com a sublista em 3 espaços de recuo); legenda exibida só no topo dos `L<lote>_gabarito.md` desses 6 lotes; `avisos` não exibidos na edição | conferências (1), (3), validação |
| 4 — A-2 (D-T53-02) | `nome` "Câmara 2026 — pacote F4 (v1.3)", `versao` 1, `geradoEm` 2026-10-13 (igual ao da v1.2); contrato lido na v1.2.1 | conferência (1) |
| 5 — não regressão | varreduras da seção 3.5 do QA R2 e exceções fechadas da R1 (CAIXA C-05/C-15; reunião C-06 a C-08; C-13; C-18), mais as do item 1; diff v1.2 → v1.3 restrito aos campos novos | conferência (4), (1) |
| T-55 §4.1 | `validate.py` lê a v1.1 de `git show e97ab1f:saida/pacote/pacote.json` (`refs.py`), não de arquivo solto | `validate.py`, `refs.py` |
| T-55 §4.2 | `conferencias_R1.py` marcado como script histórico (R0 → R1) e passa a obter R0 e R1 do git (`27e594d` e `2684ab1`) quando chamado sem argumentos; as conferências desta ocorrência estão em `conferencias_v13.py` | `conferencias_R1.py`, `conferencias_v13.py` |
| T-55 §4.3 | `relatorio_R1.py`, `report.py` e `report2.py` marcados como históricos e sem gravação no repositório (saem em `out/historico_*`); o relatório novo sai em `out/pacote_relatorio_2026-10-13_v1_3.md` e é promovido ao repositório por passo explícito | os três scripts; `relatorio_v1_3.py` |
| T-55 §4.4 | raiz do repositório e `out/` derivados de `__file__` (`common.py`: `REPO`, `HERE`, `OUT`); nenhum caminho absoluto nem relativo ao cwd nos scripts (varredura por `grep` na entrega) | `common.py` e demais |
| T-55 §4.5 | `validate.json`: iteração de conjuntos substituída por `sorted(...)` e serialização com `sort_keys=True`; três execuções com `PYTHONHASHSEED` distintos dão arquivos byte a byte iguais | `validate.py` |

### 13.2 Campos novos do pacote (literais)

| Lote | `legendaMecanismo` |
|---|---|
| L4 | Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC) |
| L4C | Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC) |
| L5 | Mecanismos: TC troca de conceito; GI generalização indevida; AT atribuição errada de técnica; IC inversão de causa e efeito |
| L5C | Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC) |
| L6A | Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada (AT), inversão de causa e efeito (IC) |
| L6B | Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada (AT), inversão de causa e efeito (IC) |

L1, L1C, L2 e L3 não têm o campo (o arquivo canônico não traz legenda de mecanismo). `avisos` do SIM-0 (3 strings; aviso 2 com a sublista):

1. **Simulado diagnóstico, não final.** Contém 37 itens de aderência DIRETA e 23 de aderência PARCIAL (D-ADERENCIA: parcial só em diagnóstico), nenhum em arbitragem, e 4 itens VOLÁTEIS (inaptos a simulado final até a reverificação de 4–8/1/2027). Não use esta montagem como simulado final.
2. **Aderência PARCIAL (23 itens).** Cada um traz, logo abaixo do item, a marca `[ADERÊNCIA PARCIAL ...]` com o motivo; o mapa do gabarito repete a marca. Eles testam o tema vizinho, não o texto exato do subitem do edital da Câmara.
      - Dos 23, 17 estão em P2-4.1 (LGPD geral; o item 51 cobra o Marco Civil da Internet, Lei 12.965/2014, não a LGPD), 2 em P1-8.3 (Grafana/Kibana), 1 em P1-5.3 (item 18), 1 em P1-6 (item 26), 1 em P1-7.1 (KPIs) e 1 em P1-8.1 (item 31). **Toda a cobertura do módulo P2 do edital neste simulado é PARCIAL** (só o 4.1 tem item).
3. **Desequilíbrio C/E (contagem real).** Total: **33 C e 27 E** (55,0% C / 45,0% E). P1: 21 C e 18 E (53,8% C). P2: 12 C e 9 E (57,1% C). Por módulo do edital: P1 (43 itens) 23 C e 20 E (53,5% C); P2 (17 itens) 10 C e 7 E (58,8% C). O banco aprovado e utilizável é assim; nenhum item aprovado foi removido para equilibrar. Quem marcasse C em todos os itens acertaria 55,0%; **não calibre o desempenho por esta proporção**.

### 13.3 Conferências por script (`conferencias_v13.py`; saídas em `saida/pacote/gerador_v1_3/out/`)

91 conferências, 0 falhas. Resultado por grupo:

| Grupo | Conferências | OK |
|---|---|---|
| base: SHA-256 da v1.2 | 1 | 1 |
| (1) diff v1.2 → v1.3 do pacote | 5 | 5 |
| (3) diff v1.2 → v1.3 da edição, fidelidade e varredura N-1 | 11 | 11 |
| (4) varreduras de não regressão e exceções fechadas da R1 | 54 | 54 |
| (5) contagens iguais às da v1.2 | 20 | 20 |

Conferências do grupo (1), na íntegra (as demais estão em `out/conferencias_v13.txt`):

- OK v1.2 (git 2684ab1) tem SHA-256 f46ed9f8e43db76aaeb96eda0b2924028fb7145c048c5eb0189396c9f67304fe e a edição v1.2 tem 43 arquivos — v1.2 f46ed9f8e43d | v1.3 fdcb7afdb4fb
- OK v1.2 -> v1.3 do pacote: só nome (valor), legendaMecanismo em 6 lotes e avisos no SIM-0 (acrescentados); geradoEm igual (2026-10-13) — diferenças: 8 (.nome valor; lotes[L4C].legendaMecanismo acrescentado; lotes[L4].legendaMecanismo acrescentado; lotes[L5C].legendaMecanismo acrescentado; lotes[L5].legendaMecanismo acrescentado; lotes[L6A].legendaMecanismo acrescentado; lotes[L6B].legendaMecanismo acrescentado; simulados[SIM-0].aviso
- OK nome: "Câmara 2026 — pacote F4 (v1.2)" -> "Câmara 2026 — pacote F4 (v1.3)"; versao 1 nas duas
- OK sem os campos novos e o nome, v1.3 = v1.2 estruturalmente (itens, edital, pegadinhas, pares, cursos, resumos, discursivas, simulados)
- OK ordem das chaves: as mesmas, salvo legendaMecanismo (última chave do lote) e avisos (última chave do SIM-0)
- OK serialização: indent=1, ensure_ascii=False, newline final; sem campo vazio nem null nos campos novos

Diff da edição v1.2 → v1.3 (linha a linha): 8 arquivos mudam (`L6B_estudo.md` 1 linha; `README.md` 1 linha; 6 `*_gabarito.md` com 2 linhas inseridas cada); os outros 35 são idênticos. Manifesto ordenado (SHA-256 das linhas "<sha>  <nome>"): v1.2 `1a8267796baa`; v1.3 `6a60f28116d9`.

Resultados dos demais scripts: `validate.py` 107 verificações, 0 falhas (as 103 da v1.2 com os rótulos de v1.3, 2 delas ajustadas (chaves de lote com `legendaMecanismo`; chaves de simulado com `avisos`), mais 4 novas: literais das 6 legendas, forma das 6 legendas no canônico, literais dos 3 avisos, início literal dos avisos); `estudante_fidelidade.py` 5650 comparações, 0 diferenças; `sync_check.py` TUDO OK; `fidelidade_mutacao.py` 5 diferenças detectadas em 4 mutações.

### 13.4 Estado e SHA-256

| Objeto | SHA-256 | bytes |
|---|---|---|
| `saida/pacote/pacote.json` v1.2 (git `2684ab1`) | `f46ed9f8e43db76aaeb96eda0b2924028fb7145c048c5eb0189396c9f67304fe` | 618673 |
| `saida/pacote/pacote.json` v1.3 | `fdcb7afdb4fb449229c6d530e877d839f8d334cd9667731e1b7222c9c7fb0eca` | 620956 |
| `saida/estudante/` v1.3 (43 arquivos; manifesto ordenado) | `6a60f28116d9ec35d86b476eeff7f133ee8ffe12532a45ea03afab283209d26b` | — |

O SHA-256 do próprio relatório e o manifesto de arquivos do gerador estão em `saida/pacote/gerador_v1_3/MANIFESTO.md` (o relatório não pode conter o próprio hash).

## Apêndice A — regras literais da edição do estudante (trecho apagado em ⟦ ⟧)

Só as regras **vigentes** da v1.3 (110 regras literais), na ordem de aplicação. Cada linha: fase, tipo, escopo, contexto e trecho apagado; todas verificadas como deleção pura (a especificação é uma subsequência do original). Fora desta lista, por desenho: as regras nº 6 ("O F4 afirma que …", restaurada na L4-11, C-13), nº 26 ("(corrigido pela O-3)" do curso 4.3.4) e nº 63 ("conferida pela QA" da seção ITENS REAIS), retiradas na R1 (C-13, C-14); as nº 42, 44 e 51 da R0 (L6A) constam abaixo na forma da C-16; as duas últimas linhas são as regras da N-1 (item 1 da lista). Conferido por programa: nenhuma regra vigente contém os textos das três retiradas.

Verificação das regras retiradas: "O F4 afirma que": 0 regra(s) vigente(s) a contêm; "(corrigido pela O-3)": 0 regra(s) vigente(s) a contêm; "conferida pela QA em 08/10/2026": 0 regra(s) vigente(s) a contêm.

| # | Fase | Tipo | Escopo | Original (contexto) → apagado |
|---|---|---|---|---|
| 1 | pre | V (parcial: mantém a orientação ao estudante) | todos | antes⏎da versão definitiva [⟦V 08/10/2026 — F4; NORMATIVO — QA; ⟧norma de⏎caráter experimental, não cobrar o texto]. |
| 2 | pre | V (parcial: mantém a orientação ao estudante) | todos | outro⏎idioma [⟦V 08/10/2026 — F4; NORMATIVO — QA; ⟧contexto histórico]. |
| 3 | pre | NORMATIVO — QA (parcial: mantém a orientação ao estudante) | todos | [⟦NORMATIVO — QA; ⟧não cobrar além do texto] |
| 4 | pre | NORMATIVO — QA (frase de marca e fontes) | todos | Todos os dispositivos abaixo estão em paráfrase⟦, com a marca⏎[NORMATIVO — QA]⟧.⟦ Fontes: F1 (LGPD compilada) e F2 (Lei 9.610/1998),⏎lidas em 08/10/2026.⟧ |
| 5 | post | F (prosa: referência a fonte) | todos | valor numérico⟦; o F4 cita a chuva "in inches or millimeters"⟧. |
| 6 | post | F (prosa: referência a fonte) | todos | ⟦; o F3 define os termos separadamente⟧ |
| 7 | post | F (frase de fonte) | todos | ⟦ Fonte: F3, conforme o curso 5.1.3.⟧ |
| 8 | post | F (frase de fonte) | todos | ⟦ Fonte: F3, conforme o curso 5.1.1.⟧ |
| 9 | post | F (frase de fonte) | todos | ⟦ Fonte: F1 e F2, conforme o curso 5.1.3.⟧ |
| 10 | post | F (prosa: referência a fonte) | todos | Fonte:⟦ F3 (temperatura) e⟧ curso 5.1.4 (janela de contexto, conceito geral). |
| 11 | post | F (prosa: referência a fonte) | todos | definição de alucinação⟦ do F3⟧). |
| 12 | post | F (prosa: referência a fonte) | todos | Fonte:⟦ F3, zero-shot ("A prompt that does not provide an example of how you want the large language model to respond"), e⟧ curso 5.1.2 e 5.1.3. |
| 13 | post | F (prosa: referência a fonte) | todos | (⟦a F10 informa que ela não é possível; ⟧exclui-se o link e cria-se outro; ver curso 1.4.2) |
| 14 | post | F (prosa: referência a fonte) | todos | conceito geral⟦; a F13 descreve o Outlook para PC como aplicativo de e-mail⟧) |
| 15 | post | F (prosa: referência a fonte) | todos | Fonte: conceito geral⟦; F7 (RFC 1034) descreve os "domain style names" e seu uso para "host address support" (trecho lido em 08/10/2026)⟧. |
| 16 | post | F (prosa: referência a fonte) | todos | Fonte: conceito geral⟦; F11 descreve o HTTP como "a stateless application-level protocol"⟧. |
| 17 | post | F (frase de fonte) | todos | (o de quarta-feira). ⟦Fonte: F12 (Microsoft Learn, "Types of backup", verificado em 08/10/2026): "If you are performing a combination of normal and differential backups, restoring files and folders requires that you have the last normal as well as the last differential backup." ⟧O item não depende |
| 18 | post | F (frase de fonte) | todos | reduz o impacto.⟦ Fonte: F2 (verificado em 08/10/2026).⟧ |
| 19 | post | F (frase de fonte) | todos | pela rede.⟦ Fonte: F13 (worm: "Propaga-se automaticamente pelas redes, explorando vulnerabilidades nos sistemas e aplicativos instalados"; verificado em 08/10/2026) e F4 (vírus, seção 4.1: "se propaga inserindo cópias de si mesmo").⟧ |
| 20 | post | F (frase de fonte) | todos | por regras.⟦ Fonte: F14 (firewall: "protege seu computador contra ataques vindos pela rede"; antivírus: "Ferramentas antivírus (antimalware) podem ajudar a detectar uma infecção"; verificado em 08/10/2026) e F5 (a Firewall do Windows "ajuda a proteger o seu dispositivo ao filtrar o tráfego de rede que entra e sai do dispositivo").⟧ |
| 21 | post | F (prosa: referência a fonte) | todos | Fonte⟦: F13 (spyware: "Projetado para monitorar as atividades de um sistema e enviar as informações coletadas para terceiros."; verificado em 08/10/2026); o antispyware não é mencionado no F13⟧: conceito geral. |
| 22 | post | F (frase de fonte) | todos | código malicioso.⟦ Fonte: F4 (livro, seção 2.3, verificado em 08/10/2026; paráfrase: as mensagens induzem o usuário a fornecer dados por páginas falsas, pela instalação de códigos maliciosos ou pelo preenchimento de formulários; entre as situações, "mensagens com links para código malicioso").⟧ |
| 23 | post | F (prosa: referência a fonte) | todos | Fonte:⟦ F4, seção 2.3.1 (DNS confirmado: "por meio de alterações no serviço de DNS"); F7;⟧ arquivo hosts: conceito geral. |
| 24 | post | F (prosa: referência a fonte) | todos | também podem usar HTTPS. Fonte: ⟦F11, seção 4.2.2 (verificado em 08/10/2026); ⟧o restante é conceito geral. |
| 25 | post | F (prosa: referência a fonte) | todos | — as técnicas⟦ de F1 e F2⟧. Se o resumo |
| 26 | post | F (prosa: referência a fonte) | todos | Exemplos⟦ do F4 (reverificados em 7/10/2026)⟧: quantidade de chuva |
| 27 | post | F (prosa: referência a fonte) | todos | Exemplos⟦ do F4⟧: e-mail é spam |
| 28 | post | F (prosa: referência a fonte) | todos | exemplo⟦ do F4⟧: agrupar dados |
| 29 | post | F (prosa: referência a fonte) | todos | POLÍTICA (policy),⟦ que o F4 descreve como⟧ a melhor estratégia para acumular recompensas⟦ (verificado em 7/10/2026)⟧. Exemplos⟦ do F4⟧: treinar robôs |
| 30 | post | F (prosa: referência a fonte) | todos | É o que afirma⟦ o F4⟧: "generative models |
| 31 | post | F (prosa: referência a fonte) | todos | conferido no GAB_DEFINITIVO_034_TRF6_002_01)⟦; o lote usa o F4 como fundamento, não o TRF6⟧. |
| 32 | post | F (prosa: referência a fonte) | todos | ficar com a formulação ⟦do F4 ⟧e evitar itens |
| 33 | post | F (prosa: referência a fonte) | todos | ⟦Segundo o F5 (verificado em 7/10/2026):⏎⟧- Modelo generativo |
| 34 | post | F (prosa: referência a fonte) | todos | Relação entre os termos: ⟦o F3 os define separadamente; ⟧LLMs de uso geral |
| 35 | post | F (prosa: referência a fonte) | todos | a lista em tópicos ⟦do F4 ⟧traz texto→texto |
| 36 | post | F (prosa: referência a fonte) | todos | a tabela de exemplos ⟦do F4 ⟧traz texto→texto |
| 37 | post | F (prosa: referência a fonte) | todos | ver 5.1.4⟦ (F3 para temperatura)⟧. |
| 38 | post | F (prosa: referência a fonte) | todos | ⟦O que a F1 afirma (leitura de 08/10/2026):⏎⟧- Na guia "Revisão" |
| 39 | post | F (prosa: referência a fonte) | todos | Limite do curso:⟦ a F1⟧ NÃO descreve como ativar |
| 40 | post | F (prosa: referência a fonte) | todos | (⟦a F3 diz ⟧"não estão formatados como cabeçalhos" |
| 41 | post | F (prosa: referência a fonte) | todos | apenas visualizar.⟦ A F9 também usa os rótulos "Pode editar" e "Pode exibir".⟧ |
| 42 | post | F (prosa: referência a fonte) | todos | -⟦ A F10 trata de "Interromper o compartilhamento" e de alternar permissões "entre exibir e editar" para quem tem acesso direto; ela ainda avisa que⟧ NÃO é possível |
| 43 | post | F (prosa: referência a fonte) | todos | ERRADO (⟦a F11 ⟧descreve os dois caminhos) |
| 44 | post | F (prosa: referência a fonte) | todos | (conceito geral⟦; F14 para os protocolos⟧) |
| 45 | post | F (prosa: referência a fonte) | todos | é conceito geral⟦; a F13 não usa a palavra "instalado"⟧. |
| 46 | post | F (prosa: referência a fonte) | todos | RFCs DA IETF⟦ E F14⟧) |
| 47 | post | F (prosa: referência a fonte) | todos | ⟦Segundo a F14, ⟧por padrão os clientes POP3 |
| 48 | post | F (prosa: referência a fonte) | todos | ⟦Segundo a F14, ⟧por padrão os clientes IMAP4 |
| 49 | post | F (prosa: referência a fonte) | todos | ficam no servidor).⏎⟦A F14 lista portas e criptografia do Exchange Online; esses números são específicos de produto e NÃO são cobrados.⏎⟧⏎### 3.1.3 |
| 50 | post | F (prosa: referência a fonte) | todos | (de edição para exibição ou o contrário)⟦ e orienta excluir o link e criar outro⟧. As duas páginas |
| 51 | post | F (prosa: referência a fonte) | todos | Cco (cópia oculta): ⟦conforme a F12 (leitura de 08/10/2026), ⟧quem é inserido |
| 52 | post | F (prosa: referência a fonte) | todos | Microsoft. ⟦A página da F19 descreve a nova experiência como a que "simplifica as conversas ao colocar o chat, as equipas e os canais num único local" (leitura de 08/10/2026). ⟧Reuniões |
| 53 | post | F (prosa: referência a fonte) | todos | Limite:⟦ a F18⟧ não define o canal padrão |
| 54 | post | F (prosa: referência a fonte) | todos | mais próxima) e⟦ a F19⟧ não diz quem pode ver |
| 55 | post | F (prosa: referência a fonte) | todos | conceito geral⟦; as páginas de ajuda F20–F22 descrevem o uso⟧) |
| 56 | post | F (prosa: referência a fonte) | todos | Google Agenda (⟦a F22, ⟧em pt-PT, chama-o |
| 57 | post | F (frase de fonte) | todos | Fonte: conceito geral.⟦ A leitura de hoje do F4 (Cartilha, livro) menciona confidencialidade e integridade apenas de passagem e associa ataques de negação de serviço a "indisponibilidades ao alvo"; essas passagens NÃO definem a tríade e não foram usadas como definição.⟧ |
| 58 | post | F (prosa: referência a fonte) | todos | "Instale um antivírus antes de qualquer aplicativo"⟦ (F3, verificado em 08/10/2026, seção de celulares)⟧. |
| 59 | post | F (prosa: referência a fonte) | todos | (⟦F11, ⟧RFC 9110, seção 4.2.2: "secured" significa que "the server has been authenticated as acting on behalf of the identified authority" e que a comunicação tem "confidentiality and integrity protection"⟦; verificado em 08/10/2026⟧) |
| 60 | post | F (prosa: referência a fonte) | todos | Fonte:⟦ F11 (seção 4.2.2), verificado em 08/10/2026;⟧ o restante é conceito geral. |
| 61 | post | F (prosa: referência a fonte) | todos | (⟦F4, seção 2.3.1, paráfrase: ⟧desconfiar de site de banco |
| 62 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | todos | suprimiu a expressão (⟦conforme a conferência da CQFP; ⟧na |
| 63 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | todos | Lei 15.352/2026⟦, conforme a⏎   CQFP⟧). A autoridade |
| 64 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | todos | — síntese autoral⟦ (GCB-CPP)⟧⏎ |
| 65 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | todos | (artigo e inciso⟦, para o QA Normativo⟧) |
| 66 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | todos | (⟦fonte: Planalto, Lei 15.352/2026 e LGPD compilada, verificadas pela CQFP em 08/10/2026; ⟧vale para a prova, edital 13.33) |
| 67 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | todos | dada pela Lei 15.352/2026⟦, verificada pela CQFP em 08/10/2026⟧ \| Troca |
| 68 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | todos | Não usada em item⟦, por despacho da GCB⟧. |
| 69 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | todos | sem item.⟦ (Síntese da CQFP a partir do texto colado pelo Fundador em 08/10/2026; não é transcrição literal.)⟧ |
| 70 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | todos | visualizations" ⟦(CI, verificado pela CQFP em 8/10/2026) ⟧— exemplo |
| 71 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | todos | cujo ponto de julgamento foi conferido ⟦pela QA ⟧contra o caderno |
| 72 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | todos | (trecho confirmado ⟦pela QA e reconfirmado pela produção ⟧em 08/10/2026) |
| 73 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | todos | Decisão⟦ da GCE⟧: sem trava |
| 74 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | todos | Notas de correção⟦ (GCE, R2–R4)⟧⏎ |
| 75 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | todos | afirmação⏎    categórica⟦ da versão da CPP⟧, segundo |
| 76 | post | id interno (R-xx, E-xx, O-xx, D-xx) | todos | Alínea c da discursiva⟦ (R4 do Projeto)⟧: |
| 77 | post | id interno (R-xx, E-xx, O-xx, D-xx) | todos | amostras de referência⟦ (errata E1)⟧, não basta |
| 78 | post | id interno (R-xx, E-xx, O-xx, D-xx) | todos | (N1⟦; E3⟧) |
| 79 | post | id interno (R-xx, E-xx, O-xx, D-xx) | todos | Distinção de vocabulário⟦ (O11)⟧: |
| 80 | post | id interno (R-xx, E-xx, O-xx, D-xx) | todos | para o Cargo 11⟦ (D-T2)⟧. |
| 81 | post | carimbo datado de verificação/leitura (ligado a F-ref) | todos | Anthropic, "XML structuring" e OpenAI, "Message formatting with Markdown and XML"⟦, verificadas em 7/10/2026⟧. |
| 82 | post | carimbo datado de verificação/leitura (ligado a F-ref) | todos | "Message formatting with Markdown and XML")⟦, ambas verificadas em 7/10/2026⟧. |
| 83 | post | carimbo datado de verificação/leitura (ligado a F-ref) | todos | reinforcement learning"⟦ (reverificado em 7/10/2026)⟧. Conclusão |
| 84 | post | carimbo datado de verificação/leitura (ligado a F-ref) | todos | "principalmente entre o honesto e o desonesto"⟦ (conferido no Planalto em 08/10/2026)⟧. |
| 85 | post | carimbo datado de verificação/leitura (ligado a F-ref) | todos | Microsoft 365"⟦, conforme a leitura de 08/10/2026⟧) |
| 86 | post | carimbo datado de verificação/leitura (ligado a F-ref) | todos | (seção 1.1⟦; leitura de 08/10/2026⟧) |
| 87 | post | carimbo datado de verificação/leitura (ligado a F-ref) | todos | seus dados"⟦, ambos verificados em 08/10/2026⟧. |
| 88 | post | id interno / versão do lote (v2) | todos | (⟦v2, ⟧item 1.4) |
| 89 | post | id interno / versão do lote (v2) | todos | (⟦v2, ⟧exemplo parlamentar do 1.4) |
| 90 | post | carimbo de leitura "aberta(s) hoje" | todos | Nas páginas de suporte⟦ abertas hoje⟧, a Microsoft |
| 91 | post | carimbo de leitura "aberta(s) hoje" | todos | (conceito geral; sem ⟦fonte aberta hoje para detalhes; sem ⟧item) |
| 92 | post | carimbo de leitura "aberta(s) hoje" | todos | (conceito geral⟦; sem base aberta hoje⟧) |
| 93 | post | carimbo de leitura "aberta(s) hoje" | todos | Fontes⟦ abertas hoje⟧: "Faça backups |
| 94 | post | carimbo de leitura "aberta(s) hoje" | todos | uma fora do local), sem ⟦fonte aberta hoje e sem ⟧item. |
| 95 | post | carimbo de leitura "aberta(s) hoje" | todos | Definição de vírus⟦ aberta hoje⟧: "programa |
| 96 | post | carimbo de leitura "aberta(s) hoje" | todos | Definição de ransomware⟦ aberta hoje⟧: "Ransomware |
| 97 | post | carimbo de leitura "aberta(s) hoje" | todos | Definição⟦ aberta hoje⟧: o phishing |
| 98 | post | carimbo de leitura "aberta(s) hoje" | todos | não foi confirmada em fonte⟦ aberta hoje⟧; ver curso 4.1.1 |
| 99 | l5 | código de fonte do L5 (U/GG/TB) | L5_ | Power BI (Microsoft)⟦ — fonte principal U1 en-us; U2 só para a natureza Windows do Desktop (verificado em 8/10/2026)⟧ |
| 100 | l5 | código de fonte do L5 (U/GG/TB) | L5_ | Tableau (Salesforce)⟦ — U3; dashboards por TB2 (verificado em 8/10/2026)⟧ |
| 101 | l5 | código de fonte do L5 (U/GG/TB) | L5_ | Data Studio (Google)⟦ — U4, U5, U6, GG4 (verificado em 8/10/2026)⟧ |
| 102 | l5 | código de fonte do L5 (U/GG/TB) | L5_ | 8.3 FERRAMENTAS (VOLÁTIL⟦; verificado em 8/10/2026⟧) |
| 103 | l5 | código de fonte do L5 (U/GG/TB) | L5_ | Três componentes e fluxo ⟦conforme U1 en-us ⟧("three primary |
| 104 | l5 | código de fonte do L5 (U/GG/TB) | L5_ | natureza Windows do Desktop⟦ conforme U2⟧. |
| 105 | post | classificação interna de VOLÁTIL na justificativa | todos | Depende de padrão técnico estável, não de produto⟦; NÃO VOLÁTIL⟧. |
| 106 | post | classificação interna de VOLÁTIL na justificativa | todos | passou a ser exercida por ela.⟦ REVERIFICAR (normativo) 04–08/01/2027; não VOLÁTIL.⟧ |
| 107 | post | classificação interna de VOLÁTIL na justificativa | todos | "Message formatting with Markdown and XML".⟦ Sem marca VOLÁTIL: o item afirma o conceito, não recurso de produto.⟧ |
| 108 | post | marca de processo ("neste chat") | todos | situação de tramitação não verificada⟦ neste chat⟧) |
| 109 | post | marca de processo de produção do lote ("Nesta produção" / "a especificação previa") | L6B_estudo | ⟦Nesta produção ⟧NÃO foi aberta fonte institucional que defina o termo |
| 110 | post | marca de processo de produção do lote ("Nesta produção" / "a especificação previa") | L6B_estudo | NÃO HÁ ITEM sobre governança digital neste lote⟦ (a especificação previa o item "se houver base")⟧. |

**Regras genéricas por escopo de arquivo (R1, C-20 e C-22):**

| Escopo | Tipo | Expressão |
|---|---|---|
| `L5_*` | código de fonte do L5 (U/GG/TB) | `(?:[ \t]*\n[ \t]*\|[ \t]+)?\((?:U\d\|GG\d\|TB\d)(?:, (?:U\d\|GG\d\|TB\d))*\)` |
| `L5_*` | código de fonte do L5 (U/GG/TB) | `, (?:U\d\|GG\d)(?=\))` |
| `L5_*` | código de fonte do L5 (U/GG/TB) | `(?<=\()(?:U\d\|TB\d), ` |
| `L5_*` | código de fonte do L5 (U/GG/TB) | `(?<=; )U\d: ` |
| `L5_*` | carimbo "Verificado em 8/10/2026" (L5) | ` Verificado em 8/10/2026\.` |
| `L2_*` | código N do L2/L3 | `(?:[ \t]*\n[ \t]*\|[ \t]+)?\(N\d\)` |
| `L3_*` | código N do L2/L3 | `(?:[ \t]*\n[ \t]*\|[ \t]+)?\(N\d\)` |
| `L2_*` | código N do L2/L3 | `; ver N\d(?=\))` |
| `L3_*` | código N do L2/L3 | `; ver N\d(?=\))` |
| `L2_*` | código N do L2/L3 | `Ver N\d: ` |
| `L3_*` | código N do L2/L3 | `Ver N\d: ` |
| `L2_*` | código N do L2/L3 | `(?<=\()N\d[:;] ` |
| `L3_*` | código N do L2/L3 | `(?<=\()N\d[:;] ` |
| `L2_*` | código N do L2/L3 | ` — N\d(?=\))` |
| `L3_*` | código N do L2/L3 | ` — N\d(?=\))` |

**Lista CAIXA (R1, C-15; minúscula → maiúscula da primeira letra, só em `L6A_estudo`):**

- `mesclar combina duas ou mais células` → `Mesclar combina duas ou mais células`
- `a função SE compara um valor` → `A função SE compara um valor`
- `o PROCV pesquisa um valor` → `O PROCV pesquisa um valor`
- `o propósito é fazer todos os slides` → `O propósito é fazer todos os slides`
- `a animação é aplicada a um único elemento` → `A animação é aplicada a um único elemento`
- `o histórico de versões permite ver` → `O histórico de versões permite ver`
- `deleted". por padrão os clientes POP3` → `deleted". Por padrão os clientes POP3`
- `offline. por padrão os clientes IMAP4` → `offline. Por padrão os clientes IMAP4`

Nota: "n" não é repetido aqui porque as regras da fase "post" casam com o texto já tratado pelas regras genéricas; as ocorrências efetivas de cada tipo estão na seção 10.1.

## Pendências

- QA: a gbq-cqe confere a v1.3 (fidelidade do pacote e da edição às fontes e à v1.2, e o escopo exato da ocorrência); a gbq-gerencia reconcilia e emite o gatilho A da v1.3 (D-V13-AGORA; a produção não decide o aceite). Nada disso foi feito aqui.
- Arquivos do repositório criados ou alterados por esta ocorrência: `saida/pacote/pacote.json`, `saida/estudante/` (regerada), `saida/pacote/pacote_relatorio_2026-10-13_v1_3.md` e `saida/pacote/gerador_v1_3/` (com `MANIFESTO.md`). Nenhum outro; a secretaria deve atualizar o estado. A promoção de `out/` para o repositório foi um passo explícito, depois de todas as conferências com 0 falhas.
