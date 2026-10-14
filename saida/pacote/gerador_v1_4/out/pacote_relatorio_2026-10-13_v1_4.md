# pacote_relatorio_2026-10-13_v1_4.md — T-57 — EXPORTAR v1.4 — 2026-10-13 — gerado por gbq-csc

Saídas: `saida/pacote/pacote.json` (versao 1, nome "Câmara 2026 — pacote F4 (v1.4)", geradoEm 2026-10-13, 621744 bytes UTF-8, SHA-256 `f8c0c131f16dab52b1646b3d302670a3afc498b23ac03a7b34a8ff97520ffa54`, indent=1, newline final), este relatório (gerado por inteiro pelo gerador, `relatorio_v1_4.py`, N-3) e a edição do estudante em `saida/estudante/` (43 arquivos). Contrato: `regras/pacote_contrato.md` v1.2.2 (errata de forma da T-57, registro em `saida/pacote/contrato_v1_2_2_2026-10-13.md`) sobre a v1.2.1 + Regras da v1.2 (a–j) e as D1 da GBQ em `saida/pacote/T48_reconciliacao_R2_2026-10-13.md`, seção 2. Escopo desta ocorrência: D-V14-AGORA (Fundador, 13/10/2026) = a lista PARA A PRÓXIMA T-12 de `saida/pacote/T56_reconciliacao_2026-10-13.md`, seção 2 (O-1, O-2, nome v1.4, não regressão, avisos do SIM-0 não exibidos) + a LISTA PARA A T-57 de `saida/pacote/T54_decisoes_2026-10-13.md`, seção 3 (T54-1 a T54-8) + a D1 da GCE sobre o item 5 (`saida/gce/T54_item5_decisao_2026-10-13.md`). Gerador: `saida/pacote/gerador_v1_4/` (cópia alterada de `gerador_v1_3/`, que ficou intacto). Nada foi commitado; TAREFAS.md, PARA_PRESIDENCIA.md, DECISOES.md, estado/, banco/ e os canônicos dos lotes (`saida/gce`, `saida/gcb`) não foram alterados; em `regras/` só `pacote_contrato.md` (errata v1.2.2). A v1.3 (SHA-256 `fdcb7afdb4fb449229c6d530e877d839f8d334cd9667731e1b7222c9c7fb0eca`, 620956 bytes) foi guardada antes de ser sobrescrita e é lida do git (commit 9622604). Nada deste pacote nem da edição do estudante vai à candidata sem decisão do Fundador; a edição do estudante NÃO é entrega à candidata (a entrega da v1.3 e da v1.4 continua reservada ao Fundador, D-ENTREGA-V13-ESPERA).

Resultado em uma linha: **286 itens** (106 de banco + 180 AUTORAL), 10 lotes (6 com `legendaMecanismo`), 5 discursivas, 4 simulados com `n` e `versao` (SIM-0 com `avisos`); 32 registros de errata (31 APLICADA, 1 JÁ PRESENTE, 0 NÃO ENCONTRADA) e 6 erratas com alvo fora do pacote; validação por script: 112 verificações, 0 falhas; conferências da ocorrência: 117, 0 falhas; edição do estudante: 43 arquivos, fidelidade textual 5793 comparações, 0 diferenças. Diff v1.3 → v1.4 do pacote: só `nome`, o campo novo `id` em 72 pares (L4, L5, L6A, L6B), o `padrao` da D5 (anexo sem a nota R2) e o `curso` do L3 (uma palavra, "eu" → "se"); da edição: 15 de 43 arquivos mudam (pares com os separadores do canônico, 2 linhas do quadro do L1, rótulo "Nota:", 6B-06, legenda no `SIM-1_gabarito.md`, D5 sem a nota R2, L3 "se possa afirmar", versão no README); os outros 28 são idênticos.

## 1. Fontes

Lidas em 13/10/2026 (SHA-256, 12 primeiros dígitos). O arquivo canônico de cada lote é o da tabela de fonte do contrato (regra 4 da v1.1); os `saida/lote*/RECONCILIADO.md` não existem e não são fonte.

| Objeto | Arquivo(s) | Versão / observação | SHA-256 (12) |
|---|---|---|---|
| Contrato | `regras/pacote_contrato.md` | v1.2.2 (errata de forma da T-57: `id` de par e regras de exibição) sobre a v1.2.1 (T-53) + Regras da v1.2 (a–j) + v1.1.1 + v1.1 | `678cfe6da9c1` |
| Registro do contrato | `saida/pacote/contrato_v1_2_2_2026-10-13.md` | SHA-256 antes e depois, cópia literal das alterações, conferência (T-57) | `d70d2045dfa7` |
| Escopo da T-57 | `saida/pacote/T56_reconciliacao_2026-10-13.md` | seção 2 (PARA A PRÓXIMA T-12: O-1, O-2, nome v1.4, não regressão, avisos) e D-T56-02 a D-T56-06 | `41f6fcbd1bbc` |
| Escopo da T-57 | `saida/pacote/T54_decisoes_2026-10-13.md` | D-T54-01 a D-T54-08; seção 2 (texto da errata do contrato); seção 3 (LISTA PARA A T-57, T54-1 a T54-8) | `bc0915dbbca5` |
| Item 5 da T-54 (GCE) | `saida/gce/T54_item5_decisao_2026-10-13.md` | D1-T54-a (nota R2 só na D4; D5 com R3–R4) e D1-T54-b (errata do curso do L3); seção 3.2 (ajuste de exportação) | `c267048b2472` |
| Errata do L3 (T-58) | `saida/gce/lote3_errata3_2026-10-13.md` | registro da errata E-1/E-2 aplicada pela gce-cpp em `GCE_Lote3_v2_CPP.md` | `c5bf460a6690` |
| Conferências do QA da T-56 | `saida/pacote/QA_T56_2026-10-13_gbq-cqe.md` | N-1, legendas, avisos não exibidos (conferências de não regressão) | `5a50907f449d` |
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
| L3 | `saida/gce/GCE_Lote3_v2_CPP.md` | v2 canônico, com a T-44 (título e nota do 3.1) e a errata T-58 (curso 4.2) já gravadas | `58b0dbedb358` |
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
| Relatório anterior | `saida/pacote/pacote_relatorio_2026-10-13_v1_3.md` | relatório da v1.3 (T-56; fica como registro) | `e70a1fdaec50` |
| Relatório anterior | `saida/pacote/pacote_relatorio_2026-10-13.md` | relatório da v1.2 (R0 + seção 13 da R1) | `7baececd7443` |
| v1.1 | `git show e97ab1f:saida/pacote/pacote.json` | referência de comparação, lida do git | `d318382639ee` |
| v1.2 (antes) | `git show 2684ab1:saida/pacote/pacote.json` | pacote canônico da D-PACOTE-V12, lido do git | `f46ed9f8e43d` |
| v1.3 (antes) | `git show 9622604:saida/pacote/pacote.json` | pacote canônico da D-PACOTE-V13, guardado antes de sobrescrever (cópia no scratchpad e no git) | `fdcb7afdb4fb` |
| Edição do estudante v1.2 | `git archive 2684ab1 saida/estudante` | 43 arquivos; manifesto ordenado (SHA-256 das linhas "<sha>  <nome>") | `1a8267796baa` |
| Edição do estudante v1.3 (antes) | `git archive 9622604 saida/estudante` | 43 arquivos; mesmo manifesto | `6a60f28116d9` |
| Contrato v1.2.1 (antes) | `git show 9622604:regras/pacote_contrato.md` | lido do git | `47e3c290646f` |

Condições do contrato (regra 5 e instrução da T-48), que continuam válidas: T-13, T-25, T-29, T-36, T-38, T-42, T-43, T-44, T-46 e T-47 CONCLUÍDAS e reconciliadas; T-40 CONCLUÍDA (BQ-0072, 0077, 0084, 0109, 0110 e 0111 entram, com 6/6 gabaritos sustentados). Simulados canônicos por D-SIM1-CANONICO, D-SIM2-CANONICO e D-SIM0P2-DIAGNOSTICO; SIM-0 v0.2 sem pendência (T-36 aplicada). T-48, T-53, T-55 e T-56 CONCLUÍDAS (a T-56 reconciliada em `T56_reconciliacao_2026-10-13.md`, aceite da v1.3 pela D-PACOTE-V13). T-58 (errata de forma do curso do L3, D1-T54-b da GCE) gravada em `saida/gce/GCE_Lote3_v2_CPP.md` e lida pelo pacote. Nenhuma errata nem texto canônico de simulado mudou desde a v1.3; do canônico dos lotes mudou só a T-58 (uma palavra no curso do L3, mais o registro "T-54" na Tabela de Correções, que não é exportado). Liberar qualquer simulado à candidata continua reservado ao Fundador.

## 2. Contagens v1.1 → v1.2 → v1.3 → v1.4

| Medida | v1.1 | v1.2 | v1.3 | v1.4 |
|---|---|---|---|---|
| `versao` / `nome` | 1 / "Câmara 2026 — pacote F4 (v1.1)" | 1 / "Câmara 2026 — pacote F4 (v1.2)" | 1 / "Câmara 2026 — pacote F4 (v1.3)" | 1 / "Câmara 2026 — pacote F4 (v1.4)" |
| `geradoEm` | 2026-10-10 | 2026-10-13 | 2026-10-13 | 2026-10-13 |
| edital (entradas) | 47 | 47 | 47 | 47 |
| itens (total) | 240 | 286 | 286 | 286 |
| itens CEBRASPE_ANALOGA (banco) | 60 | 106 | 106 | 106 |
| itens AUTORAL | 180 | 180 | 180 | 180 |
| gabarito C / E (total) | 122 / 118 | 149 / 137 | 149 / 137 | 149 / 137 |
| gabarito C / E (banco) | 33 / 27 | 60 / 46 | 60 / 46 | 60 / 46 |
| gabarito C / E (AUTORAL) | 89 / 91 | 89 / 91 | 89 / 91 | 89 / 91 |
| aderência direta / parcial (total) | 217 / 23 | 247 / 39 | 247 / 39 | 247 / 39 |
| aderência direta / parcial (banco; AUTORAL todos direta) | 37 / 23 | 67 / 39 | 67 / 39 | 67 / 39 |
| `volatil: true` (total; banco + AUTORAL) | 19 (4 + 15) | 23 (8 + 15) | 23 (8 + 15) | 23 (8 + 15) |
| `nota` (itens) | 0 | 2 (BQ-0003, BQ-0040) | 2 (BQ-0003, BQ-0040) | 2 (BQ-0003, BQ-0040) |
| `comandoOriginal` (itens) | 0 | 90 | 90 | 90 |
| `textoBase` "nenhum" / "" / texto | 237 / 0 / 3 | 0 / 283 / 3 | 0 / 283 / 3 | 0 / 283 / 3 |
| lotes / discursivas | 10 / 5 | 10 / 5 | 10 / 5 | 10 / 5 |
| pares (total) | 139 | 139 | 139 | 139 |
| pares com `id` (opcional, v1.2.2 ponto 1) | 0 | 0 | 0 | 72 (L4 20, L5 15, L6A 19, L6B 18) |
| lotes com `legendaMecanismo` (opcional, v1.2.1 ponto 4) | 0 | 0 | 6 (L4, L4C, L5, L5C, L6A, L6B) | 6 (L4, L4C, L5, L5C, L6A, L6B) |
| pegadinhas (total) | 144 | 262 | 262 | 262 |
| simulados | 2 (SIM-0, SIM-1) | 4 (SIM-0, SIM-1, SIM-2, SIM-0-P2) | 4 (SIM-0, SIM-1, SIM-2, SIM-0-P2) | 4 (SIM-0, SIM-1, SIM-2, SIM-0-P2) |
| simulados `n` | — / — | 60 / 40 / 40 / 25 | 60 / 40 / 40 / 25 | 60 / 40 / 40 / 25 |
| simulados com `avisos` (opcional, v1.2.1 ponto 5) | 0 | 0 | SIM-0 (3 avisos) | SIM-0 (3 avisos) |
| bytes | 541533 | 618673 | 620956 | 621744 |
| SHA-256 (12) | d318382639ee | f46ed9f8e43d | fdcb7afdb4fb | f8c0c131f16d |

A v1.4 é a v1.3 (SHA-256 `fdcb7afdb4fb`) mais `nome`, o campo opcional `id` nos 72 pares de L4, L5, L6A e L6B, o `padrao` da D5 (anexo de notas sem a R2) e uma troca de uma palavra no `curso` do L3 (errata T-58): as medidas de itens, simulados, lotes, pegadinhas e discursivas são idênticas (seção 13, conferências (1) e (5)). Banco: 112 linhas em `banco/banco.csv`; 106 exportadas (60 C / 46 E) e 6 excluídas por anulação (gabarito X): BQ-0029, BQ-0030, BQ-0031, BQ-0060, BQ-0062, BQ-0063. Os 60 itens da v1.1 mantêm o mesmo `comando` e a mesma aderência (37 direta / 23 parcial, conferido); os 46 novos são BQ-0061… do terceiro lote de varredura (inclui BQ-0072, 0077, 0084, 0109, 0110 e 0111, liberados pela T-40). BQ-0049 a 0051 são os únicos com `textoBase` (a coluna `texto_base`); nos 283 demais `textoBase` é `""` (F2).

### 2.1 Itens por lote (AUTORAL) e `comandoOriginal`

| Lote | AUTORAL | C | E | `volatil` | `comandoOriginal` | pegadinhas v1.1 → v1.4 | pares | pares com `id` |
|---|---|---|---|---|---|---|---|---|
| L1 | 20 | 10 | 10 | 4 | 0 | 8 → 19 | 17 | 0 |
| L1C | 10 | 4 | 6 | 0 | 0 | 1 → 4 | 0 | 0 |
| L2 | 30 | 15 | 15 | 0 | 0 | 8 → 43 | 22 | 0 |
| L3 | 30 | 16 | 14 | 1 | 0 | 7 → 42 | 28 | 0 |
| L4 | 20 | 10 | 10 | 1 | 20 | 32 → 32 | 20 | 20 |
| L4C | 10 | 5 | 5 | 0 | 10 | 0 → 0 | 0 | 0 |
| L5 | 20 | 10 | 10 | 4 | 20 | 14 → 48 | 15 | 15 |
| L5C | 10 | 5 | 5 | 0 | 10 | 0 → 0 | 0 | 0 |
| L6A | 15 | 7 | 8 | 5 | 15 | 35 → 35 | 19 | 19 |
| L6B | 15 | 7 | 8 | 0 | 15 | 39 → 39 | 18 | 18 |

`volatil` no banco (8): BQ-0015, BQ-0017, BQ-0035, BQ-0064, BQ-0075, BQ-0076, BQ-0086, BQ-0089. Em AUTORAL (15): L1-Q14, L1-Q16, L1-Q18, L1-Q19, L3-Q21, L4-15, A5-14, A5-15, A5-16, A5-17, 6A-01, 6A-09, 6A-10, 6A-14, 6A-15. Total 23; os AUTORAL são os VOLÁTIL + REVERIFICAR normativo do registro GBQ v3 (regra R1-N), com L3-Q21.

### 2.2 Simulados (regra (e): `n` e `versao`)

| id | nome | tipo | `versao` | `n` | itens | C / E | `volatil` | parcial | `avisos` |
|---|---|---|---|---|---|---|---|---|---|
| SIM-0 | Simulado 0 — diagnóstico (v0.2) | diagnóstico | v0.2 | 60 | 60 | 33 / 27 | 4 | 23 | 3 |
| SIM-1 | Simulado 1 — P1 final (TI e Dados, itens 5 a 8) | final | v1 | 40 | 40 | 20 / 20 | 0 | 0 | — |
| SIM-2 | Simulado 2 — P2 final (Reconhecimento de Fala, Transcrição e IA, itens 1 a 4) | final | v1 | 40 | 40 | 20 / 20 | 0 | 0 | — |
| SIM-0-P2 | Simulado 0-P2 — P2 diagnóstico (Reconhecimento de Fala, Transcrição e IA, itens 1 a 4) | diagnóstico | v1 | 25 | 25 | 13 / 12 | 0 | 0 | — |

`n` = tamanho da lista `itens` em 4/4. `avisos` (v1.2.1 ponto 5): só o SIM-0, com os avisos 1, 2 e 4 da folha canônica, literais (seção 13.4). `versao`: SIM-0 "v0.2" (cabeçalho do arquivo); SIM-1, SIM-2 e SIM-0-P2 "v1" (sem versão declarada, regra (e)). Nenhum simulado final contém item `volatil` ou `parcial`. O gabarito de cada posição do simulado (arquivos `*_gabarito.md`) é igual ao `gabarito` do item no pacote em 165/165 posições (60 + 40 + 40 + 25).

### 2.3 Discursivas

D1–D4 idênticas às da v1.1, da v1.2 e da v1.3 (D1 questão (L1), D2 questão e D3 peça (L2), D4 questão (L3)); a **D5** (peça, L3) é igual à da v1.3 em comando, aspectos, quesitos e conceitos e difere só no anexo de notas do `padrao`: a v1.3 acrescentava "Notas de correção (GCE, R2–R4)" (cópia das linhas 14–23 de `GCE_Lote3_padroes_GCE.md`, as mesmas da D4); a v1.4 acrescenta "Notas de correção (GCE, R3–R4)" com as linhas 21–23 literais, sem o trecho da R2 (linhas 14–20, 7 linhas; a R2 trata da alínea c da questão da D4 e não tem objeto na peça; D1-T54-a da GCE). `padrao` da D5: 5094 → 4644 caracteres. A D4 mantém o anexo R2–R4. Aspectos e quesitos conferidos: soma dos aspectos das questões 14,30 + 0,70 de apresentação = 15,00; peças 28,50 + 1,50 = 30,00. A observação "inferido pela EXEC" da D1 (Adendo 4) não é exportada: 0 ocorrência de "EXEC" nas discursivas. D3 e D5 são pareceres técnicos (gênero confirmado para analista e técnico; hipótese por analogia para o Cargo 11). Pesos por quesito são HIPÓTESE do Projeto.

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
| L3 | T-58 (D1-T54-b da GCE) | curso 4.2, bloco "CONTROVERSO / NÃO GABARITO": "jurisprudência firmada que se possa afirmar):" (antes "que eu possa afirmar") | JÁ PRESENTE | errata de forma gravada pela gce-cpp em `GCE_Lote3_v2_CPP.md` (registro `saida/gce/lote3_errata3_2026-10-13.md`); o pacote lê o arquivo atual: 1 troca de uma palavra no `curso` do L3 (27731 → 27731 caracteres). O "que eu possa afirmar" que resta no canônico é o da linha de limites N4, não exportada |

Totais: os registros de substituição do gerador são 32 (31 APLICADA e 1 JÁ PRESENTE, a única sendo o Adendo 2 no 3.1); 0 NÃO ENCONTRADA. As quatro últimas linhas da tabela (E8, T-44, T-47, T-58) são informativas: E8 é a montagem da D1 (APLICADA, sem substituição) e T-44, T-47 e T-58 já estavam gravadas nos arquivos canônicos (JÁ PRESENTE); somadas, a tabela tem 36 linhas, das quais 32 APLICADA ou JÁ PRESENTE por substituição do gerador. Para cada APLICADA o script confere depois que Y consta do JSON e X não consta (fora das ocorrências de Y): validação "erratas: Y presente / X ausente", OK.

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

## 5. Diff textual resumido v1.1 → v1.4 por lote

Campos de lote comparados caractere a caractere (difflib), v1.1 (git e97ab1f) contra a v1.4. O diff v1.3 → v1.4 é menor: os campos de texto dos lotes (`resumo`, `curso`, `pares` (`a`, `b`, `como`), `pegadinhas`, `itensEdital`) são idênticos (conferência (1), seção 13), salvo a troca de uma palavra no `curso` do L3; o único acréscimo é o campo `id` nos 72 pares de L4, L5, L6A e L6B. Campos não citados: idênticos.

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
- curso: 26978 → 27731 caracteres, 5 operações:
  - remove "ERRATA T-08, 10/10/2026; "
  - remove " (registro da GCB-CQFP, 08/10/2026)"
  - insere "Contexto institucional — Ato da Mesa nº 225, de 15/12/2025 (DCD, Ed.⏎Extra A, 18/12/2025): estabelece diretrizes gerais para a política de⏎governança de intelig"
  - insere "s"
  - remove "u"
- pares: 28 pares; 1 com texto alterado (`a`, `b`, `como`).
- pegadinhas: 7 → 42 entradas (desdobramento da F3, com as reuniões da errata v1.2.1 ponto 2 quando houve), todas com `rotulo`.

**L4**
- pares: 20 pares; 0 com texto alterado (`a`, `b`, `como`); todos com `id` (novo na v1.4, C1 a C20).
- `legendaMecanismo` (novo na v1.3): "Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC)".

**L4C**
- resumo, curso, pares e itensEdital idênticos; pegadinhas: mesma contagem (0), agora com `rotulo`.
- `legendaMecanismo` (novo na v1.3): "Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC)".

**L5**
- curso: 18901 → 19003 caracteres, 1 operações:
  - insere " O fator 1,5·AIQ é a convenção usual (Tukey); outras convenções existem e a prova costuma cobrar esta."
- pares: 15 pares; 0 com texto alterado (`a`, `b`, `como`); todos com `id` (novo na v1.4, C1 a C15).
- pegadinhas: 14 → 48 entradas (desdobramento da F3, com as reuniões da errata v1.2.1 ponto 2 quando houve), todas com `rotulo`.
- `legendaMecanismo` (novo na v1.3): "Mecanismos: TC troca de conceito; GI generalização indevida; AT atribuição errada de técnica; IC inversão de causa e efeito".

**L5C**
- resumo, curso, pares e itensEdital idênticos; pegadinhas: mesma contagem (0), agora com `rotulo`.
- `legendaMecanismo` (novo na v1.3): "Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC)".

**L6A**
- pares: 19 pares; 0 com texto alterado (`a`, `b`, `como`); todos com `id` (novo na v1.4, C1 a C19).
- `legendaMecanismo` (novo na v1.3): "Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada (AT), inversão de causa e efeito (IC)".

**L6B**
- pares: 18 pares; 0 com texto alterado (`a`, `b`, `como`); todos com `id` (novo na v1.4, C1 a C18).
- `legendaMecanismo` (novo na v1.3): "Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada (AT), inversão de causa e efeito (IC)".

Itens (campo a campo, v1.1 → v1.4): `textoBase` 237 (F2, "nenhum" → ""), `comando` 90 e `comandoOriginal` 90 (D1-c), `justificativa` 21 (F4), `nota` 2 (BQ-0003, BQ-0040), `enunciado` 1 (L1-Q04, F1). `gabarito`, `aderencia` (nos 60 da v1.1), `itemEdital`, `rotulo`, `certame`, `cargo`, `ano`, `numero` e `url`: 0 diferença. Discursivas: D1–D4 sem diferença; D5 com o anexo de notas da v1.4 (seção 2.3). Edital: igual. Da v1.3 para a v1.4, nenhum item muda. Nos lotes, além do que está acima: `id` nos 72 pares de L4, L5, L6A e L6B e uma troca de palavra no `curso` do L3 ("eu" → "se", T-58).

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

| Lote | entradas v1.1 → v1.4 | modos de origem (entradas da v1.1) |
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

## 9. Validação por script (112 verificações, 0 falhas)

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
- OK v1.4 `id` de par (contrato v1.2.2 ponto 1): chaves [id, a, b, como] só em L4, L5, L6A e L6B (72 pares); L1, L1C, L2, L3 sem `id` (67 pares: [a, b, como])
- OK v1.4 `id` de par: string não vazia que casa ^C\d+$, C1…Cn em sequência, igual (e na mesma ordem) aos rótulos "C<n>." da seção (c) do arquivo canônico: L4 20, L5 15, L6A 19, L6B 18
- OK v1.4 remissões a par por id: L5 C1 = Histograma × gráfico de barras; L5 C14 = Storytelling × dashboard; L4 C19 = Injeção de prompt × jailbreak (conceitos gerais)
- OK v1.4 `a`, `b` e `como` de todos os pares iguais aos da v1.1, fora o `id`, salvo a errata oficial já aplicada na v1.1 (L3 par 20 = E4; o par 15 do L2, E1c, já estava aplicado na v1.1) — {'L3': [20]}
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
- OK L3 T-58 (D1-T54-b da GCE, errata de forma): curso do L3 com "jurisprudência firmada que se possa afirmar):" (1×) e 0 "que eu possa afirmar"; o canônico atual tem a errata no curso (1×) e o registro "T-54" na Tabela de Correções do cabeçalho (o "que eu possa afirmar" que resta no canônico é o da linha de limites N4, não exportada)
- OK L5 Tukey (T-47): curso do L5 8.2 contém "O fator 1,5·AIQ é a convenção usual (Tukey); outras convenções existem e a prova costuma cobrar esta."
- OK INFO DETAQ fora da forma "Derep (antigo DETAQ)" em curso/resumo
- OK discursivas: 5 (D1–D5); D1 a D4 idênticas às da v1.1; D5 igual à da v1.1 exceto o anexo de notas: sem a R2 (trecho literal removido) e com o rótulo "Notas de correção (GCE, R3–R4)" (D1-T54-a da GCE); comando, aspectos e quesitos da D5 iguais
- OK discursivas: sem observação "inferido pela EXEC" (0 ocorrência)
- OK discursivas: "14,30" (E11) não aparece em comando/padrão (E11 sem efeito no exportado)
- OK D4: anexo R2–R4 é cópia literal das linhas 14–23 do arquivo de padrões
- OK D5 (v1.4, D1-T54-a da GCE): anexo R3–R4 é cópia literal das linhas 21–23 do arquivo de padrões; 0 "R2." e 0 "Alínea c da discursiva" na D5; rótulo "Notas de correção (GCE, R3–R4)"
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

Gerada a partir do `pacote.json` v1.4 (fonte única). **43 arquivos**, os mesmos nomes da v1.2 e da v1.3: `README.md` (índice, versão v1.4, data 2026-10-13, aviso "material de estudo; gabaritos em arquivo separado"); por lote, `<ID>_estudo.md` (itens do edital, resumo, curso, pares, pegadinhas com rótulo), `<ID>_itens.md` (texto-base se houver, comando e enunciado, nessa ordem; sem gabarito, justificativa nem marcas) e `<ID>_gabarito.md` (gabarito, item do edital e justificativa; **no topo, a `legendaMecanismo` literal do lote, nos 6 lotes que a têm**) para L1, L1C, L2, L3, L4, L4C, L5, L5C, L6A e L6B (30 arquivos); `BANCO_itens.md` e `BANCO_gabarito.md` (certame, cargo, ano, número, URL oficial, aviso VOLÁTIL e `nota` literal, **sem o rótulo "Nota:" do gerador e** sem o identificador de decisão); por simulado `<SIM>_folha.md` (sem o id de origem dos itens) e `<SIM>_gabarito.md` (SIM-0, SIM-1, SIM-2, SIM-0-P2; **v1.4: no topo, depois de "Número de itens", a `legendaMecanismo` de cada lote de origem que a tenha, sem repetir string igual**); `DISCURSIVAS.md` e `DISCURSIVAS_padrao.md`. **Pares (v1.4):** cada linha de par usa os separadores e a pontuação do canônico do próprio lote (`- **a** vs **b**: como` / `- **a** vs **b**.` nos lotes GCE; `- Cn. **a** × **b** | como` nos lotes GCB, com o `id` do pacote). Resumo e curso vão em blocos de texto cercados, para preservar quebras, recuos e tabelas. **Os `avisos` do SIM-0 não são exibidos** (D-T53-02/item 3 da lista; D-T56-03: até decisão do Fundador sobre o que se compartilha com a candidata); a fidelidade confere que o texto dos três avisos não aparece em arquivo algum.

**Regra:** as marcas internas saem SOMENTE POR DELEÇÃO (nunca reescrita) por `estudante_marcas.py` e `literais.py`, com as exceções fechadas da reconciliação R1: (i) CAIXA (C-05 e C-15): minúscula → maiúscula da primeira letra de um trecho, lista de 8 pares só em `L6A_estudo` (e as 2 trocas de caixa na F4 do pacote); (ii) reunião de fragmentos de pegadinha com "; " (C-06 a C-08, só no pacote); (iii) a `nota` de BQ-0003 sai da edição sem " (D-LEI-15352)" (C-18; errata v1.2.1 ponto 3), só na exibição; (iv) **v1.4:** o realinhamento só com espaços de 2 linhas do quadro-síntese do L1 (D-T54-02; apêndice A), que não apaga nada. A marca VOLÁTIL vira, nos itens `volatil: true`, o aviso fixo "Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027."; a `nota` (BQ-0003, BQ-0040) é exibida junto do item. Enunciado, comando e texto-base de item não são tocados (afirmado por teste: nenhuma marca da lista neles). **Novidade da v1.3 (N-1, D-R2-01):** duas regras literais, só em `L6B_estudo`, apagam "Nesta produção " e " (a especificação previa o item "se houver base")" do curso 4.0.2 (o "NÃO" que segue já tem inicial maiúscula); no pacote a marca fica, por desenho (D-PACOTE-V11). **Novidade da v1.4 (T-57):** (a) o realinhamento só com espaços de 2 linhas do quadro-síntese do L1 (D-T54-02; exceção (iv): não apaga nada, insere 6 espaços antes de `|` para recompor as posições do canônico; lista no apêndice A); (b) a regra do 6B-06 passa a apagar o parêntese de verificação inteiro, "Fonte: conceito geral⟦ (a definição da tríade não foi confirmada em fonte aberta hoje; ver curso 4.1.1)⟧. Tema da tríade" (D-T54-06 c); (c) o anexo "Notas de correção" da D5 perde, por desenho do gerador, a nota R2 (D1-T54-a da GCE) e o rótulo apagado passa a " (GCE, R3–R4)"; (d) o rótulo "Nota: " do gerador não é mais emitido (D-T54-04) e as legendas de lote entram nos `SIM-*_gabarito.md` (D-T54-07). Regras genéricas (por tipo) e regras literais (frase ou cláusula a apagar, `⟦…⟧` na especificação; 111 regras literais vigentes, apêndice A):

- `[V dd/mm/aaaa — …]` apagado inteiro, com o espaço anterior (o colchete pode quebrar linha entre "[V" e a data); duas exceções que mantêm a orientação ao estudante: `[V … — F4; NORMATIVO — QA; norma de caráter experimental, não cobrar o texto]` fica `[norma de caráter experimental, não cobrar o texto]` e `[V … contexto histórico]` fica `[contexto histórico]`.
- `[NORMATIVO — QA: base legal]` perde o prefixo e o colchete e fica a base legal ("LGPD, art. 5º, I."); `[NORMATIVO — QA]` e as variantes com ";" são apagadas (`[NORMATIVO — QA; não cobrar além do texto]` fica `[não cobrar além do texto]`); a frase "…com a marca [NORMATIVO — QA]. Fontes: F1 … lidas em 08/10/2026." do L3 sai, ficando "Todos os dispositivos abaixo estão em paráfrase."
- Referências de fonte F1…F22: `[Fn]`, `(Fn)`, `(Fn, Fm)`, `(Fn, verificado em …)`, `(Fn, seção …)`, `, Fn)` no fim de parêntese, `; Fn)`, `(Fn: ` e `(Fn, "…")` (mantém o parêntese e o conteúdo), "Conforme a Fn (leitura de …):", frases "Fonte(s): Fn, …verificado em …." e, em trechos de prosa, a cláusula ou palavra que só existe por causa da referência (lista completa no apêndice A). "A tecla F4" (Excel) NÃO é referência e permanece; a frase restaurada da L4-11 ("O F4 afirma que …") permanece (D-R1-07, opção (a)).
- Agentes e unidades (CQFP, QA, GCB, GCE, CPP) em carimbos como "(conferido pela CQFP em 08/10/2026)", "conforme a CQFP", "(GCB-CPP)", "Decisão da GCE", "versão da CPP", "para o QA Normativo", "Síntese da CQFP … colado pelo Fundador"; ids internos "(errata E1)", "; E3" em "(N1; E3)", "(O11)", "(D-T2)", "(R4 do Projeto)" e, nos padrões D4/D5, "(GCE, R2–R4)" e os enumeradores "R2. ", "R3. ", "R4. ".
- Carimbos datados ligados a uma referência apagada ("verificadas em 7/10/2026", "(reverificado em …)", "conforme a leitura de 08/10/2026", "(conferido no Planalto em …)") e, na R1, "aberta(s) hoje" (9 pontos, L6A e L6B), "(v2, …)" no L1C (2), " neste chat" no L4 (1), classificação interna de VOLÁTIL nas justificativas (4), carimbo "Verificado em 8/10/2026" do L5 (4).
- Códigos de fonte do L5 (U1–U6, GG4, TB2; só `L5_*`, 33 remoções) e códigos de nota N do L2 e do L3 (`(N1)`, `Ver N5:` etc.; só `L2_*` e `L3_*`, 14 remoções); os códigos N1–N4 do L4 ficam (definidos no próprio texto).

### 10.1 Marcas removidas por tipo e por arquivo

Contagem de ocorrências apagadas, por arquivo gerado (um item presente em lote e em simulado é contado nos dois arquivos). Total nos arquivos: **568**.

| Tipo | Ocorrências |
|---|---|
| F (parêntese) | 87 |
| V | 58 |
| F (prosa: referência a fonte) | 54 |
| F (fim de parêntese) | 48 |
| F (frase "Fonte(s): …") | 42 |
| código de fonte do L5 (U/GG/TB) | 33 |
| F (colchete) | 26 |
| F (parêntese com verificação) | 26 |
| agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | 25 |
| NORMATIVO — QA (prefixo da base legal) | 23 |
| NORMATIVO — QA | 18 |
| código N do L2/L3 | 14 |
| F (início de parêntese) | 14 |
| F (fim de parêntese, após vírgula) | 13 |
| F (frase de fonte) | 11 |
| F ("Conforme a Fn (leitura …):") | 11 |
| id interno (R-xx, E-xx, O-xx, D-xx) | 10 |
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
| **Total** | **568** |

| Arquivo | Total | Detalhe por tipo |
|---|---|---|
| BANCO_gabarito.md | 1 | id de decisão na nota (D-LEI-15352) 1 |
| BANCO_itens.md | 1 | id de decisão na nota (D-LEI-15352) 1 |
| DISCURSIVAS_padrao.md | 11 | id interno (R-xx, E-xx, O-xx, D-xx) 7; agente/unidade interna (CQFP, QA, GCB, GCE, CPP) 4 |
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

Referência: na v1.2 as remoções somaram 569; na v1.3, 571; a v1.4 soma 568 (571 − 3: saem as 3 deleções que só existiam por causa da nota R2 na D5 — "Alínea c … (R4 do Projeto)", "R2. " e " da versão da CPP" —; a regra do 6B-06 passa a apagar o parêntese inteiro e a do rótulo do anexo da D5 apaga " (GCE, R3–R4)", ambas com a mesma contagem das anteriores; o realinhamento do quadro do L1 não é remoção).

Arquivos sem nenhuma remoção: os `*_itens.md`, `BANCO_*`, `*_folha.md`, `README.md` e os `*_gabarito.md` cujos itens não tinham marca (a tabela só lista os arquivos com remoção).

### 10.2 Fidelidade (script `estudante_fidelidade.py`)

O script lê os 43 arquivos com um parser próprio (independente do gerador) e confere, campo a campo, o texto do estudante com o do pacote: (1) igual ao texto do pacote com as deleções das regras; (2) obtido do texto do pacote só por deleção (teste de subsequência linear e, depois, difflib: apenas `equal`/`delete`, salvo as 8 trocas de caixa da lista CAIXA, C-15, e, **v1.4**, o desfazimento dos 2 realinhamentos de espaço do quadro do L1, D-T54-02, exceção fechada de 2 regras com 1 ocorrência cada); (3) comando, texto-base, enunciado, gabarito, item do edital, aderência, nota (com a única exceção da C-18), aviso VOLÁTIL, certame, cargo, ano, número, URL, ordem e `n` dos simulados, valores dos aspectos e conceitos dos quesitos idênticos ao pacote; (4) a `legendaMecanismo` de cada lote com o campo está literal, sozinha, no topo do `*_gabarito.md` do próprio lote (antes do primeiro item) e em nenhum outro arquivo (salvo, **v1.4**, as legendas dos lotes de origem no topo de cada `SIM-*_gabarito.md`, uma vez cada, na ordem de `lotes`); lote sem o campo não tem texto antes do primeiro item; o texto dos `avisos` não aparece na edição; (5) **v1.4:** o parser lê a linha de par nos dois formatos e compara `a`, `b`, `como` e o `id` exibido com o pacote (linha fora do formato é DIFERENÇA); a `nota` é exibida sem rótulo (`- `/`> ` seguido do valor, com a única deleção do identificador da C-18); o README declara v1.4. Teste negativo (`fidelidade_mutacao.py`: 11 mutações aplicadas isoladamente, cada uma em cópia nova da edição — `BANCO_gabarito.md`, `DISCURSIVAS_padrao.md`, `L1_estudo.md`, `L1_itens.md`, `L2_estudo.md`, `L2_gabarito.md`, `L3_estudo.md`, `L4_estudo.md`, `L5_gabarito.md`, `L6B_gabarito.md`, `SIM-1_gabarito.md`) detectou 255 diferenças no total; todas as mutações foram detectadas: sim; portanto o script não é cego.

- comparações: texto 1380, metadado 941, estrutura 48, prova/metadado 1883, aviso/nota 1067, gabarito 451, legenda 20, avisos não exibidos 3 (total 5793)
- **diferenças: 0** (texto do estudante == texto do pacote com as deleções aplicadas)
- marcas residuais nos arquivos pela varredura de higiene (V, NORMATIVO — QA, [TS], CQFP/CQE/CPP/GCE/GCB/GBQ/EXEC, F1…F22, T-/R-/E-/O-xx, "(errata En)"): 2, a saber: L4_gabarito.md linha 58 "F4" (sujeito da frase restaurada da L4-11 (exceção registrada, D-R1-07 opção (a))); L6A_estudo.md linha 83 "F4" (tecla do Excel, não é referência).

## 11. Marcas que permanecem (varredura)

**No `pacote.json` (por desenho):** curso, resumo, pegadinhas e justificativas AUTORAL conservam as marcas de processo do arquivo canônico, porque o pacote é dado, não edição do estudante (decisão do gatilho A: só a edição do estudante as retira, e a F4 limpou apenas as 18 justificativas com marca de agente/risco/lição). Contagem no JSON: `[V …]` 57; `[NORMATIVO — QA…]` 33; referências F1…F22 402; CQFP/CPP/GCE/GCB/QA em texto de lote 23.

**Na edição do estudante** as varreduras da seção 3.5 do QA da R2 dão 0 (conferência (4), seção 13): `;)`, ` — $`, `****`, `abertas? hoje`, `(v2,`, `D-LEI-15352`, `neste chat`, `Retificação`, `Gabarito [CE] mantido`, códigos U/GG/TB/CI, códigos N (L1, L1C, L2, L3, SIM-2, SIM-0-P2), ` — <id>` nas folhas, `erificado em 8/10/2026` (L5); mais [TS], `[V `, CQFP/CQE/GCE/GCB/GBQ/CPP, `T-n`, QA, `O-n`, "Lição O", `R-nCn`, "NÃO VOLÁTIL", "Sem marca VOLÁTIL", REVERIFICAR e `\bD-XX`; da N-1, "Nesta produção" e "especificação previa"; e, da v1.4, "Nota: nota de vigência", "não foi confirmada em fonte", "R2." e "Alínea c da discursiva" na D5 e "que eu possa afirmar" no curso do L3 (0 em todos).

**Permanecem na edição, por decisão da reconciliação (D1 da GBQ):** `a tecla F4` (`L6A_estudo.md` 83) e `O F4 afirma que …` (`L4_gabarito.md`, L4-11; D-R1-07); "VOLÁTIL" fora do aviso fixo em 7 linhas de títulos, rubricas e orientação de estudo (L4_estudo.md:23; L4_estudo.md:210; L5_estudo.md:24; L5_estudo.md:104; L5_estudo.md:107; L6A_estudo.md:125; L6A_estudo.md:268; D-R1, 2.3-g); etiquetas GI/TC/AT/IC nas justificativas (2.3-h), com a legenda literal do lote no topo do `*_gabarito.md` dos 6 lotes que a têm **e, na v1.4, no `SIM-1_gabarito.md`**; códigos N1–N4 do L4 (2.3-e); `(Derep (antigo DETAQ); …)` no `L1_estudo.md` (literal pela F5; D-R1-15 DESCARTADO); 29 justificativas iniciadas em minúscula depois do prefixo de campo (forma do canônico; D-R1-18 DESCARTADO); referentes perdidos em deleções que a D-T54-06 mandou **não mexer**: L6A 135 "As duas páginas" (alínea a; referente recuperável em `L6A_estudo.md` 31), L5 119 e 126 (alínea b; citações nominais entre aspas) e L3 101 e 574 "(não cobrar descrição de sistema real.)" (alínea d; "N6:" é código N vedado). **Saíram desta lista na v1.4:** "que eu possa afirmar" no curso do L3 (T-58); as remissões a pares por id ("par C1", "par C14", "C19" em A5-09, 5C-03, 5C-07 e 4C-08), resolvidas pelo `id` de par (os rótulos "C1…Cn" aparecem agora nos pares de L4, L5, L6A e L6B, na edição e no pacote); o referente perdido da 6B-06 (parêntese apagado); a nota R2 repetida na D5; o rótulo "Nota: nota de vigência:"; o quadro-síntese do L1 desalinhado nas duas linhas afetadas e o separador "×"/" — " dos pares. **Continua no canônico, e portanto na edição:** o desalinhamento da linha "Tradução p/ inglês" do quadro do L1 (posições de `|` iguais às do canônico). **Os avisos 1, 2 e 4 do SIM-0** estão no pacote (campo `avisos`) e continuam fora da edição (decisão do Fundador).

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

**DÚVIDAS da v1.3 (14 a 16), decididas na reconciliação `T56_reconciliacao_2026-10-13.md`:**

| DÚVIDA (v1.3) | Decisão que a resolve | Efeito nesta ocorrência |
|---|---|---|
| 14 — forma de exibição da `legendaMecanismo` | D-T56-02 (aceita; sem título "Legenda"; extensão aos `SIM-*_gabarito.md` passa a ser o item 7 da T-54) | legenda no topo dos 6 `L<lote>_gabarito.md` (inalterado) e, v1.4, no `SIM-1_gabarito.md` (D-T54-07) |
| 15 — aviso 2 do SIM-0 remete a marca ausente da folha | D-T56-03 (BACKLOG, condicionado ao Fundador) | `avisos` continuam literais no pacote e não exibidos na edição |
| 16 — varredura `D-[A-Z]{2,}` sem `\b` | D-T56-04 (DESCARTADO; errata de registro) | a conferência usa `\bD-[A-Z]{2,}` (0); sem `\b` são 14 ocorrências, as mesmas das versões anteriores (TID-IA, TID-DADOS-VIZ, END-TO-END) |

**DÚVIDAS desta ocorrência (v1.4), cada uma com a decisão que a resolve; nenhuma impede o aceite:**

17. **6B-06 está na linha 33 de `L6B_gabarito.md`, não na 31.** A LISTA (T54-6) e a D-T54-06 (c) citam a linha 31. A legenda de 2 linhas do topo do `L6B_gabarito.md` (D-T56-02) desloca a justificativa da 6B-06 para a linha 33, na v1.3 e na v1.4. Apliquei a regra da LISTA (apagar o parêntese inteiro, 1 ocorrência, deleção pura); só o número de linha difere. O mesmo vale para o exemplo do L3 da T54-3 (a LISTA diz linha 565; o par sem `b` nem `como` está na linha 564 da v1.3, dentro da faixa 539–566 da própria LISTA). Sem decisão a tomar; proposta: DESCARTADO (registro). Remissão: D-T54-06 (c).
18. **O realinhamento do quadro do L1 é a única operação da edição que não é deleção.** A D-T54-02 manda inserir 6 espaços em 2 linhas. O gerador, a fidelidade e as conferências passaram a aceitar essa exceção fechada (REALINHA: 2 regras, 1 ocorrência cada, só espaços inseridos num único ponto imediatamente antes de um `|`; a fidelidade desfaz o realinhamento antes do teste de subsequência e recusa qualquer outra inserção). Registro para o aceite; nenhuma decisão pendente. Remissão: D-T54-02; apêndice A.
19. **Rótulo do anexo da D5: "Notas de correção (GCE, R3–R4)" no pacote.** A GCE sugeriu o rótulo (T54_item5_decisao, 3.2) "salvo D1 diversa da GBQ"; a D-T54-05 manda aplicar o que a GCE fixar e a T54_decisoes não fixa outro rótulo. Apliquei "(GCE, R3–R4)" no pacote (a D4 mantém "(GCE, R2–R4)"); na edição o trecho entre parênteses sai por deleção, como já saía na D4 (a edição exibe "Notas de correção"). Remissão: D-T54-05; D1-T54-a. Proposta: aceitar.
20. **Par sem `b` e sem `como` (L3, "Confidencialidade, integridade, disponibilidade").** A LISTA cobre o caso (`- **{a}**.`). O gerador registra o caso no LOG ("par sem " vs " (b vazio)") e a edição exibe `- **Confidencialidade, integridade, disponibilidade**.`, igual ao canônico sem o numeral. Sem decisão a tomar. Remissão: D-T54-01.
21. **Escopo do `id` de par.** O `id` só existe onde o canônico rotula o par "C<n>." (L4, L5, L6A, L6B: 72 pares). L4C e L5C não têm pares próprios; as remissões de 4C-08, 5C-03, 5C-07 e A5-09 apontam para pares de L4 e L5, que têm `id`. Os lotes GCE (67 pares) não têm `id` e nenhuma justificativa remete a eles por número. Sem decisão a tomar. Remissão: D-T54-03.
22. **Scripts históricos: "marcar" em vez de "mover".** A D-T56-05 deixa a escolha à produção. Escolhi marcar, no `MANIFESTO.md` (coluna "Papel": "não executável; registro da R0/R1"), os 5 scripts `relatorio_R1.py`, `report.py`, `report2.py`, `diff.py` e `diff2.py`, sem alterá-los e sem mover (mover mudaria os caminhos relativos do próprio histórico). Conferido: cada um sai com código 1 sem gravar nada. Sem decisão a tomar. Remissão: D-T56-05.

## 13. Ocorrência v1.4 (T-57)

Ocorrência da D-V14-AGORA (Fundador, 13/10/2026), com o gerador de `saida/pacote/gerador_v1_3/` copiado para `saida/pacote/gerador_v1_4/` (a v1.3 ficou intacta; `refs.py` ganhou a referência da v1.3, commit 9622604). Despacho: T-57, com a lista da `T56_reconciliacao_2026-10-13.md`, seção 2, a LISTA PARA A T-57 de `T54_decisoes_2026-10-13.md`, seção 3 (T54-1 a T54-8), e a D1 da GCE sobre o item 5 (`saida/gce/T54_item5_decisao_2026-10-13.md`, com a errata T-58 já gravada no canônico do L3). Toda mudança saiu do gerador (`pacote.json` e `saida/estudante/` não foram editados à mão).

### 13.1 Itens da lista PARA A PRÓXIMA T-12 (`T56_reconciliacao`, seção 2)

| Item | Como foi feito | Onde se confere |
|---|---|---|
| 1 — O-1 (D-T56-05) | os 5 scripts históricos que não rodam no estado atual (`relatorio_R1.py`, `report.py`, `report2.py`, `diff.py`, `diff2.py`) ficam em `gerador_v1_4/` **marcados** no `MANIFESTO.md` como "não executável; registro da R0/R1" (opção "marcar"; ver DÚVIDA 22); os históricos que ainda rodam (`conferencias_R1.py`, `texts.py`, `probe.py`, `resid.py`, `review.py`) continuam como "histórico (executável; lê do git)"; nenhum script ativo foi alterado por este item. Conferido: cada um dos 5 sai com código 1 e não grava nada | `MANIFESTO.md`, coluna "Papel" |
| 2 — O-2 (D-T56-06) | a "Ordem de execução" do `MANIFESTO.md` descreve o redirecionamento de cada `out/*_stdout.txt` (runner `rodar_tudo.sh`: `gen_stdout.txt` = saída de `build_pacote.py` (`>`) mais a de `estudante_gen.py` (`>>`); `fidelidade_stdout.txt`, `sync_stdout.txt`, `validate_stdout.txt`, `conferencias_stdout.txt`, `mutacao_stdout.txt` e `relatorio_stdout.txt` = a saída-padrão do script homônimo). O caminho absoluto de `fidelidade_stdout.txt` saiu: `estudante_fidelidade.py` imprime `pacote:` e `estudante:` relativos à raiz do repositório (`saida/pacote/gerador_v1_4/out/…`); `grep` por caminho absoluto em `out/*.txt`: 0 | `rodar_tudo.sh`, `MANIFESTO.md`, `out/fidelidade_stdout.txt` |
| 3 — nome (T56, seção 2, item 3) | `nome` "Câmara 2026 — pacote F4 (v1.4)", `versao` 1, `geradoEm` 2026-10-13 (igual ao da v1.3); só o canônico com gatilho aceito entra (aqui: a T-58, errata do curso do L3) | conferência (1) |
| 4 — não regressão | varreduras da seção 3.5 do QA R2 (com `\bD-[A-Z]{2,}`), exceções fechadas da R1 (CAIXA C-05/C-15, reunião C-06 a C-08, C-13, C-18) e conferências do QA da T-56 (N-1, legendas, avisos não exibidos); diff v1.3 → v1.4 restrito ao previsto (itens abaixo) | conferências (1), (3), (4) |
| 5 — avisos do SIM-0 | continuam no pacote (3 strings) e **não** são exibidos na edição (0 arquivo com o texto dos avisos; fidelidade: "avisos não exibidos" 3) | conferência (4), fidelidade |

### 13.2 T-54, item a item (LISTA PARA A T-57; antes = v1.3, depois = v1.4)

| Item | Antes → depois | Contagem / verificação |
|---|---|---|
| T54-1 contrato v1.2.2 (D-T54-08) | `regras/pacote_contrato.md` v1.2.1 → v1.2.2: linha 1 (título), acréscimo no fim da linha 3 e seção nova "Errata de forma da v1.2.2" (9 linhas + 1 em branco) depois do ponto 6 da errata v1.2.1; registro `saida/pacote/contrato_v1_2_2_2026-10-13.md` | SHA-256 `47e3c290646f` → `678cfe6da9c1`; diff por linha: 2 substituições + 1 inserção; seção nova igual, caractere a caractere, ao bloco (iii) da T54_decisoes; **nenhum campo obrigatório mudou** (exemplo JSON, "Regras:", v1.1, v1.1.1, v1.2, tabela de fonte e PROMPT DE PARTIDA idênticos; `versao` 1) |
| T54-2 `id` de par (D-T54-03) | `p1.py` `pares_gcb`: `dict(id='C' + m.group(1), a=…, b=…, como=…)`; 72 pares ganham `id` como primeira chave; `a`, `b`, `como` iguais | L4 C1–C20 (20), L5 C1–C15 (15), L6A C1–C19 (19), L6B C1–C18 (18) = 72; L1, L2, L3: 0 `id`; ids = rótulos `^C\d+\.` da seção (c) do canônico, na ordem; remissões: L5 C1 = Histograma × gráfico de barras, L5 C14 = Storytelling × dashboard, L4 C19 = Injeção de prompt × jailbreak (conceitos gerais) |
| T54-3 pares na edição (D-T54-01) | GCE: `- **a** × **b** — como` → `- **a** vs **b**: como` (ou `.` se `como` vazio); GCB: `- **a** × **b** — como` → `- Cn. **a** × **b** \| como` | **139** linhas (L1 17, L2 22, L3 28, L4 20, L5 15, L6A 19, L6B 18); o teste da D-T54-01 dá 0 diferença de caractere nas 139; GCE (67 linhas): 0 com `** × **`, todas terminam em ".", 27 com `como` vazio (L1 1, L2 9, L3 17); GCB (72): todas casam `^- C\d+\. \*\*`; 136 linhas iguais à linha canônica (erratas aplicadas) e 3 só com deleção de marca (L4 "Clustering", L4 "Controlador", L6B "Backup completo"); fora de "## Pares" nenhuma linha muda por este item |
| T54-4 quadro do L1 (D-T54-02) | `L1_estudo.md` 424 e 427: 6 espaços inseridos antes de `\|` em cada linha (exceção fechada REALINHA) | comprimentos 82 e 71 e posições de todos os `\|` iguais às de `GCE_Lote1_v2_CPP.md` 475 e 478; as demais linhas do quadro (419–430) iguais às da v1.3; o desalinhamento canônico da linha "Tradução p/ inglês" permanece |
| T54-5 rótulo da nota (D-T54-04) | `> Nota: nota de vigência: …` → `> nota de vigência: …` (e `- Nota: …` → `- …`) | 8 linhas: BANCO_itens 2, BANCO_gabarito 2, SIM-0_folha 2, SIM-0_gabarito 2 (BQ-0003 e BQ-0040); 0 "Nota: nota de vigência"; 4 linhas `^> nota de vigência: ` e 4 `^- nota de vigência: `; o resto de cada linha igual à v1.3; " (D-LEI-15352)" continua ausente; o pacote não muda |
| T54-6 6B-06 (D-T54-06 c) | `Fonte: conceito geral (a definição da tríade não foi confirmada em fonte; ver curso 4.1.1). Tema da tríade…` → `Fonte: conceito geral. Tema da tríade…` | deleção pura, 1 ocorrência, `L6B_gabarito.md` linha 33 (DÚVIDA 17); 0 "não foi confirmada em fonte" e 0 "abertas? hoje" na edição; o pacote não muda (justificativa igual à da v1.3); pontos a), b) e d) da D-T54-06: não mexer |
| T54-7 legenda nos `SIM-*_gabarito.md` (D-T54-07) | `SIM-1_gabarito.md`: depois de "- Número de itens: 40", as legendas de L4 (= L4C = L5C) e de L5, literais, em linha própria, sem título | +4 linhas (2 legendas e 2 em branco); iguais, caractere a caractere, a `lotes[L4].legendaMecanismo` e `lotes[L5].legendaMecanismo`; `SIM-0_gabarito.md` (só BQ), `SIM-2_gabarito.md` e `SIM-0-P2_gabarito.md` sem legenda (a única mudança do SIM-0 é a da T54-5); folhas não mudam por este item |
| T54-8a D5 (D1-T54-a da GCE) | `p2.py`: anexo da D5 = só R3–R4 (linhas 21–23 literais de `GCE_Lote3_padroes_GCE.md`), rótulo "Notas de correção (GCE, R3–R4)"; D4 mantém R2–R4 (linhas 14–23) | pacote: `padrao` da D5 sem as 7 linhas da R2 (5094 → 4644 caracteres); edição: `DISCURSIVAS_padrao.md` perde exatamente as 7 linhas 507–513 da v1.3; `validate.py` exige D4 = linhas 14–23 e D5 = linhas 21–23 |
| T54-8b curso do L3 (D1-T54-b da GCE; T-58) | `lotes[L3].curso` relido do canônico atual: "jurisprudência firmada que eu possa afirmar):" → "…que se possa afirmar):" | uma troca de uma palavra no pacote (27731 → 27731 caracteres); na edição, `L3_estudo.md` linha 422 é a única linha que muda fora de "## Pares"; 0 "que eu possa afirmar" no pacote e na edição |

Exemplos literais (v1.3 → v1.4) da primeira linha de par alterada de cada lote (linha da v1.3):

- L1, linha 452:
  - antes: `- **ASR** × **diarização vs identificação de locutor** — texto / quem-quando / quem-é.`
  - depois: `- **ASR** vs **diarização vs identificação de locutor**: texto / quem-quando / quem-é.`
- L2, linha 439:
  - antes: `- **Transcrição automática** × **degravação** — software sem humano / pessoa a partir da gravação.`
  - depois: `- **Transcrição automática** vs **degravação**: software sem humano / pessoa a partir da gravação.`
- L3, linha 539:
  - antes: `- **Transcrição** × **sumarização** — reproduz / condensa e reformula.`
  - depois: `- **Transcrição** vs **sumarização**: reproduz / condensa e reformula.`
- L4, linha 236:
  - antes: `- **Supervisionado** × **não supervisionado × por reforço** — rótulos | sem rótulos, busca de estrutura | sem rótulos, recompensa por ação e política | Troca: chamar clustering de supervisionado; dizer que reforço usa rótulos; dizer que não supervisionado disp…`
  - depois: `- C1. **Supervisionado** × **não supervisionado × por reforço** | rótulos | sem rótulos, busca de estrutura | sem rótulos, recompensa por ação e política | Troca: chamar clustering de supervisionado; dizer que reforço usa rótulos; dizer que não supervisionado …`
- L5, linha 149:
  - antes: `- **Histograma** × **gráfico de barras** — variável quantitativa em classes adjacentes de escala numérica; barras contíguas; ordem fixa; mostra distribuição | categorias discretas; ordem livre; compara valores; espaçamento entre barras é convenção de desenho |…`
  - depois: `- C1. **Histograma** × **gráfico de barras** | variável quantitativa em classes adjacentes de escala numérica; barras contíguas; ordem fixa; mostra distribuição | categorias discretas; ordem livre; compara valores; espaçamento entre barras é convenção de desen…`
- L6A, linha 231:
  - antes: `- **Referência relativa** × **absoluta × mista (Excel)** — relativa: muda ao copiar (padrão) | absoluta ($B$2): fixa coluna e linha; mista: fixa só uma ($B2 coluna; B$2 linha) | Troca: dizer que B$2 fixa a coluna; que a referência é absoluta por padrão.`
  - depois: `- C1. **Referência relativa** × **absoluta × mista (Excel)** | relativa: muda ao copiar (padrão) | absoluta ($B$2): fixa coluna e linha; mista: fixa só uma ($B2 coluna; B$2 linha) | Troca: dizer que B$2 fixa a coluna; que a referência é absoluta por padrão.`
- L6B, linha 275:
  - antes: `- **LAN** × **WAN** — área geográfica restrita (sala, edifício, campus) | áreas geograficamente distantes (cidades, países); a Internet é a maior | Troca: inverter as duas definições.`
  - depois: `- C1. **LAN** × **WAN** | área geográfica restrita (sala, edifício, campus) | áreas geograficamente distantes (cidades, países); a Internet é a maior | Troca: inverter as duas definições.`
- L3, linha 564 (par sem `b` nem `como`):
  - antes: `- **Confidencialidade, integridade, disponibilidade**`
  - depois: `- **Confidencialidade, integridade, disponibilidade**.`

Quadro-síntese do L1 (T54-4), linhas da v1.3 (antes) e da v1.4 (depois):

```text
v1.3 424:                     |               | streaming)     | e fast)* | streaming)
v1.4 424:                     |               | streaming)     | e fast)*       | streaming)
v1.3 427:                     |         |                |                |
v1.4 427:                     |               |                |                |
```

6B-06 (T54-6), parte final da justificativa:

- antes: `…Fonte: conceito geral (a definição da tríade não foi confirmada em fonte; ver curso 4.1.1). Tema da tríade CIA também nos itens reais 96 e 98 do TRF6 2024, com outro ponto de julgamento (seção ITENS REAIS).`
- depois: `…Fonte: conceito geral. Tema da tríade CIA também nos itens reais 96 e 98 do TRF6 2024, com outro ponto de julgamento (seção ITENS REAIS).`

D5 (T54-8a): linhas apagadas de `DISCURSIVAS_padrao.md` (v1.3, 507–513), idênticas às 407–413 da D4, que ficam:

```text
507: Alínea c da discursiva: NÃO se exige enquadrar o
508:     pronunciamento parlamentar como obra protegida (Lei 9.610/1998, art.
509:     7º, II) nem como ato oficial (art. 8º, IV). Não há texto legal nem
510:     jurisprudência firmada sobre isso. Fica descartada a afirmação
511:     categórica, segundo a qual os pronunciamentos "são
512:     obras intelectuais protegidas". Basta uma razão da lista (ix), com
513:     o dispositivo correto.
```

L3 (T54-8b), `L3_estudo.md` linha 422:

- antes: `jurisprudência firmada que eu possa afirmar):`
- depois: `jurisprudência firmada que se possa afirmar):`

### 13.3 Arquivos da edição que mudam (v1.3 → v1.4)

15 arquivos mudam; os outros 28 são idênticos byte a byte. A reconstrução da v1.4 aplicando à v1.3 só as operações da lista dá 43/43 arquivos iguais (conferência (3)).

| Arquivo | linhas substituídas | inseridas | apagadas | operações da lista |
|---|---|---|---|---|
| BANCO_gabarito.md | 2 | 0 | 0 | T54-5 |
| BANCO_itens.md | 2 | 0 | 0 | T54-5 |
| DISCURSIVAS_padrao.md | 0 | 0 | 7 | T54-8a |
| L1_estudo.md | 19 | 0 | 0 | T54-3 (17 pares) + T54-4 (2 linhas) |
| L2_estudo.md | 22 | 0 | 0 | T54-3 (pares) |
| L3_estudo.md | 29 | 0 | 0 | T54-3 (28 pares) + T54-8b (1 linha) |
| L4_estudo.md | 20 | 0 | 0 | T54-3 (pares) |
| L5_estudo.md | 15 | 0 | 0 | T54-3 (pares) |
| L6A_estudo.md | 19 | 0 | 0 | T54-3 (pares) |
| L6B_estudo.md | 18 | 0 | 0 | T54-3 (pares) |
| L6B_gabarito.md | 1 | 0 | 0 | T54-6 |
| README.md | 1 | 0 | 0 | versão v1.3 → v1.4 |
| SIM-0_folha.md | 2 | 0 | 0 | T54-5 |
| SIM-0_gabarito.md | 2 | 0 | 0 | T54-5 |
| SIM-1_gabarito.md | 0 | 4 | 0 | T54-7 |
| **Total** | **152** | **4** | **7** | |

### 13.4 Campos do pacote e literais

**`id` de par (novo, opcional; contrato v1.2.2 ponto 1):**

| Lote | pares | com `id` | primeiro → último | exemplo (`id`: a × b) |
|---|---|---|---|---|
| L1 | 17 | 0 | — | — |
| L1C | 0 | — | — | — |
| L2 | 22 | 0 | — | — |
| L3 | 28 | 0 | — | — |
| L4 | 20 | 20 | C1 → C20 | C1: Supervisionado × não supervisionado × por reforço |
| L4C | 0 | — | — | — |
| L5 | 15 | 15 | C1 → C15 | C1: Histograma × gráfico de barras |
| L5C | 0 | — | — | — |
| L6A | 19 | 19 | C1 → C19 | C1: Referência relativa × absoluta × mista (Excel) |
| L6B | 18 | 18 | C1 → C18 | C1: LAN × WAN |

Remissões que o `id` resolve: A5-09 ("curso 8.2; par C1") e 5C-03 ("do par C1") → L5 C1; 5C-07 ("par C14") → L5 C14; 4C-08 ("o par injeção × jailbreak (C19)") → L4 C19. Nenhuma justificativa foi tocada.

**`legendaMecanismo` por lote** (literal do canônico; inalterada desde a v1.3):

| Lote | `legendaMecanismo` |
|---|---|
| L4 | Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC) |
| L4C | Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC) |
| L5 | Mecanismos: TC troca de conceito; GI generalização indevida; AT atribuição errada de técnica; IC inversão de causa e efeito |
| L5C | Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC) |
| L6A | Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada (AT), inversão de causa e efeito (IC) |
| L6B | Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada (AT), inversão de causa e efeito (IC) |

L1, L1C, L2 e L3 não têm o campo (o arquivo canônico não traz legenda de mecanismo). **Topo do `SIM-1_gabarito.md` na v1.4** (T54-7):

```text
# Simulado 1 — P1 final (TI e Dados, itens 5 a 8) — gabarito

- Versão: v1
- Número de itens: 40

Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC)

Mecanismos: TC troca de conceito; GI generalização indevida; AT atribuição errada de técnica; IC inversão de causa e efeito

```

`avisos` do SIM-0 (3 strings, inalteradas; aviso 2 com a sublista; **não exibidos**):

1. **Simulado diagnóstico, não final.** Contém 37 itens de aderência DIRETA e 23 de aderência PARCIAL (D-ADERENCIA: parcial só em diagnóstico), nenhum em arbitragem, e 4 itens VOLÁTEIS (inaptos a simulado final até a reverificação de 4–8/1/2027). Não use esta montagem como simulado final.
2. **Aderência PARCIAL (23 itens).** Cada um traz, logo abaixo do item, a marca `[ADERÊNCIA PARCIAL ...]` com o motivo; o mapa do gabarito repete a marca. Eles testam o tema vizinho, não o texto exato do subitem do edital da Câmara.
      - Dos 23, 17 estão em P2-4.1 (LGPD geral; o item 51 cobra o Marco Civil da Internet, Lei 12.965/2014, não a LGPD), 2 em P1-8.3 (Grafana/Kibana), 1 em P1-5.3 (item 18), 1 em P1-6 (item 26), 1 em P1-7.1 (KPIs) e 1 em P1-8.1 (item 31). **Toda a cobertura do módulo P2 do edital neste simulado é PARCIAL** (só o 4.1 tem item).
3. **Desequilíbrio C/E (contagem real).** Total: **33 C e 27 E** (55,0% C / 45,0% E). P1: 21 C e 18 E (53,8% C). P2: 12 C e 9 E (57,1% C). Por módulo do edital: P1 (43 itens) 23 C e 20 E (53,5% C); P2 (17 itens) 10 C e 7 E (58,8% C). O banco aprovado e utilizável é assim; nenhum item aprovado foi removido para equilibrar. Quem marcasse C em todos os itens acertaria 55,0%; **não calibre o desempenho por esta proporção**.

### 13.5 Conferências por script (`conferencias_v14.py`; saídas em `saida/pacote/gerador_v1_4/out/`)

117 conferências, 0 falhas. Resultado por grupo:

| Grupo | Conferências | OK |
|---|---|---|
| base: SHA-256 da v1.3 | 1 | 1 |
| (1) diff v1.3 → v1.4 do pacote (nome, `id`, D5, curso do L3) | 11 | 11 |
| (2) contrato v1.2.1 → v1.2.2 (T54-1) | 5 | 5 |
| (3) diff v1.3 → v1.4 da edição, fidelidade, reconstrução 43/43 e testes T54-3 a T54-8 | 20 | 20 |
| (4) varreduras de não regressão, exceções fechadas da R1 e conferências do QA da T-56 | 60 | 60 |
| (5) contagens iguais às da v1.3 e da v1.2 | 20 | 20 |

Conferências dos grupos BASE, (1), (2) e (3), na íntegra (as demais estão em `out/conferencias_v14.txt`):

- OK BASE — v1.3 (git 9622604) tem SHA-256 fdcb7afdb4fb449229c6d530e877d839f8d334cd9667731e1b7222c9c7fb0eca, 620956 bytes, e a edição v1.3 tem 43 arquivos com manifesto ordenado 6a60f28116d9ec35 — v1.3 fdcb7afdb4fb | v1.4 f8c0c131f16d
- OK (1) DIFF — v1.3 -> v1.4 do pacote: só nome (valor), `id` em 72 pares (acrescentado), padrao da D5 (valor) e curso do L3 (valor); geradoEm igual (2026-10-13); qualquer outra diferença = falha — diferenças: 75 (1 nome + 72 id + 1 D5 + 1 curso L3)
- OK (1) DIFF — nome: "Câmara 2026 — pacote F4 (v1.3)" -> "Câmara 2026 — pacote F4 (v1.4)"; versao 1 nas duas
- OK (1) DIFF — cada `id` de par (72) é o rótulo "C<n>." da seção (c) do canônico do lote, na ordem (L4 C1–C20, L5 C1–C15, L6A C1–C19, L6B C1–C18), é a primeira chave, e a/b/como são idênticos aos da v1.3 — L4 20 ok, L5 15 ok, L6A 19 ok, L6B 18 ok
- OK (1) DIFF — L1, L1C, L2 e L3 sem `id` (0 de 67 pares); L4C e L5C sem pares
- OK (1) DIFF — remissões: L5 C1 = Histograma × gráfico de barras; L5 C14 = Storytelling × dashboard; L4 C19 = Injeção de prompt × jailbreak (conceitos gerais)
- OK (1) DIFF — curso do L3: igual ao da v1.3 com UMA troca ("eu" -> "se" em "jurisprudência firmada que eu possa afirmar):"); 0 "que eu possa afirmar" no pacote — caracteres 27731 -> 27731
- OK (1) DIFF — o canônico atual do L3 (GCE_Lote3_v2_CPP.md, T-58) traz a errata no curso (1x) e o registro "T-54" na Tabela de Correções; o curso do pacote = curso lido do canônico (sem outra mudança desde a v1.3)
- OK (1) DIFF — D5: padrao v1.4 = padrao v1.3 sem o trecho literal da nota R2 (linhas 14–20 de GCE_Lote3_padroes_GCE.md, 7 linhas) e com o rótulo "Notas de correção (GCE, R3–R4)"; anexo v1.4 = linhas 21–23 literais; comando, aspectos e quesitos da D5 iguais
- OK (1) DIFF — D4 inalterada: padrao com o anexo R2–R4 (linhas 14–23 literais) e rótulo "Notas de correção (GCE, R2–R4)"; D1, D2, D3 também idênticas
- OK (1) DIFF — ordem das chaves: as mesmas da v1.3, salvo `id` como primeira chave dos 72 pares
- OK (1) DIFF — serialização: indent=1, ensure_ascii=False, newline final; 286 itens idênticos (enunciado, comando, comandoOriginal, textoBase, gabarito, justificativa, itemEdital, aderencia, volatil, nota); simulados idênticos
- OK (2) CONTRATO T54-1 — diff linha a linha de regras/pacote_contrato.md v1.2.1 -> v1.2.2: só a linha 1 (título), a linha 3 (acréscimo no fim do parágrafo) e uma inserção contígua (seção nova); 0 outra linha alterada — operações: replace antes[0:1] depois[0:1]; replace antes[2:3] depois[2:3]; insert antes[93:93] depois[93:103]
- OK (2) CONTRATO T54-1 — linha 1: "(v1.2.1, 2026-10-13)" -> "(v1.2.2, 2026-10-13)"; linha 3 = linha 3 antiga + texto (ii) literal da seção 2 de T54_decisoes (a partir de `ver a seção "Errata de forma da v1.2.1".`)
- OK (2) CONTRATO T54-1 — a seção nova é igual, caractere a caractere, ao bloco da seção 2 de T54_decisoes (iii): 1 linha em branco + 9 linhas; entra depois do ponto 6 da "Errata de forma da v1.2.1" e antes da linha `---` — 9 linhas, 3099 caracteres
- OK (2) CONTRATO T54-1 — nenhum campo obrigatório mudou: exemplo JSON, parágrafo "Regras:" (campos obrigatórios), Regras da v1.1, v1.1.1 e v1.2, tabela de fonte e PROMPT DE PARTIDA idênticos caractere a caractere; `versao` continua 1; a seção nova diz que não muda nome, tipo nem obrigatoriedade de nenhum campo
- OK (2) CONTRATO T54-1 — SHA-256 do contrato: v1.2.1 (git 9622604) 47e3c290646f…; v1.2.2 (arquivo atual) 678cfe6da9c1
- OK (3) EDIÇÃO — mesmos 43 nomes de arquivo
- OK (3) EDIÇÃO — arquivos que mudam da v1.3 para a v1.4: exatamente 15 (7 *_estudo.md com pares, BANCO_itens, BANCO_gabarito, SIM-0_folha, SIM-0_gabarito, L6B_gabarito, SIM-1_gabarito, DISCURSIVAS_padrao, README); os outros 28 idênticos byte a byte — ['BANCO_gabarito.md', 'BANCO_itens.md', 'DISCURSIVAS_padrao.md', 'L1_estudo.md', 'L2_estudo.md', 'L3_estudo.md', 'L4_estudo.md', 'L5_estudo.md', 'L6A_estudo.md', 'L6B_estudo.md', 'L6B_gabarito.md', 'README.md', 'SIM-0_folha.md', 'SIM-0_gabarito.md', 'SIM-1_gabarito.md']
- OK (3) EDIÇÃO — reconstrução exata: aplicando à v1.3 SÓ as operações da LISTA (pares com os separadores do canônico e `id`; 2 linhas do quadro do L1; rótulo "Nota:"; 6B-06; legendas no SIM-1_gabarito; 7 linhas da D5; L3 "que se possa afirmar"; README) o resultado é igual à v1.4 em 43/43 arquivos — divergentes: []
- OK (3) EDIÇÃO — linhas alteradas por arquivo (v1.3 -> v1.4): pares 139 (L1 17, L2 22, L3 28, L4 20, L5 15, L6A 19, L6B 18) + L1 quadro 2 + L3 curso 1; nota 8; 6B-06 1; SIM-1_gabarito +4; D5 -7; README 1 (total 163) — {'BANCO_gabarito.md': 2, 'BANCO_itens.md': 2, 'DISCURSIVAS_padrao.md': 7, 'L1_estudo.md': 19, 'L2_estudo.md': 22, 'L3_estudo.md': 29, 'L4_estudo.md': 20, 'L5_estudo.md': 15, 'L6A_estudo.md': 19, 'L6B_estudo.md': 18, 'L6B_gabarito.md': 1, 'README.md': 1, 'SIM-0_folha.md': 2, 'SIM-0_gabarito.md': 2, '
- OK (3) T54-3 — teste da D-T54-01: em cada linha de par, sem "- " e sem "**", a v1.4 = a v1.3 com o 1.º " × " -> " vs " e o 1.º " — " -> ": " (ou "." quando `como` vazio) nos lotes GCE, e 1.º " — " -> " | " com "{id}. " na frente nos lotes GCB: 0 diferença de caractere em 139 linhas — linhas por lote {'L1': 17, 'L2': 22, 'L3': 28, 'L4': 20, 'L5': 15, 'L6A': 19, 'L6B': 18}; diferenças []
- OK (3) T54-3 — lotes GCE (67 linhas): 0 com "** × **"; todas casam ^- \*\*, e terminam em "." ou em aspas; lotes GCB (72 linhas): todas casam ^- C\d+\. \*\*, sem " — " como separador a/como na posição do canônico — GCE terminam em: {'.': 67}
- OK (3) T54-3 — fora das seções "## Pares", só mudam as 2 linhas do quadro do L1 (T54-4) e a linha 422 do L3 (T54-8b): 3 linhas nos 7 *_estudo.md (as mesmas contagens de linha; nenhuma linha acrescentada ou removida) — linhas alteradas fora de "## Pares": 3
- OK (3) T54-3 — a linha do par na v1.4, sem "- " e sem "**", é igual à linha do par do arquivo canônico (erratas aplicadas; quebras juntadas; sem o numeral dos lotes GCE): 136 linhas iguais e 3 com só deleção de marca (L4 "Clustering", L4 "Controlador", L6B "Backup completo") — iguais 136; só deleção de marca 3; divergentes []
- OK (3) T54-4 — quadro-síntese do L1 (L1_estudo.md 424 e 427): posições de todos os "|" e comprimento (82 e 71) iguais aos de GCE_Lote1_v2_CPP.md 475 e 478; diferença para a v1.3 = só 6 espaços inseridos em cada linha — v1.4 l.424 vs canônico l.475: comprimento 82/82, |: iguais; v1.4 l.427 vs canônico l.478: comprimento 71/71, |: iguais
- OK (3) T54-4 — as demais linhas do quadro (419–430) iguais às da v1.3; o desalinhamento canônico da linha "Tradução p/ inglês" permanece (a linha 428 é igual à v1.3)
- OK (3) T54-5 — rótulo da nota: 0 "Nota: nota de vigência"; 4 linhas "^> nota de vigência: " (BANCO_itens 2, SIM-0_folha 2) e 4 "^- nota de vigência: " (BANCO_gabarito 2, SIM-0_gabarito 2); resto de cada linha = v1.3; " (D-LEI-15352)" ausente — [('BANCO_gabarito.md', 2), ('BANCO_itens.md', 2), ('SIM-0_folha.md', 2), ('SIM-0_gabarito.md', 2)]
- OK (3) T54-6 — 6B-06: deleção pura do parêntese "(a definição da tríade não foi confirmada em fonte; ver curso 4.1.1)" na edição; 0 "não foi confirmada em fonte" e 0 "abertas? hoje" na edição; o pacote não muda (justificativa da 6B-06 igual à da v1.3) — linha 33 de L6B_gabarito.md (a LISTA diz 31; as 2 linhas da legenda de 6B do topo deslocam para 33 na v1.3 e na v1.4)
- OK (3) T54-7 — SIM-1_gabarito.md ganha exatamente 4 linhas (2 legendas e 2 linhas em branco): legenda do L4 (= L4C = L5C) e depois a do L5, literais; depois de "- Número de itens: 40" e antes de "### 1 — "; a ordem é a da lista `lotes`
- OK (3) T54-7 — SIM-2_gabarito.md e SIM-0-P2_gabarito.md (L1, L1C, L2, L3; sem legenda) iguais aos da v1.3; SIM-0_gabarito.md (só BQ) muda só pela nota (T54-5); as folhas não mudam por este item (SIM-1_folha, SIM-2_folha, SIM-0-P2_folha iguais; SIM-0_folha muda só pela nota)
- OK (3) T54-8a — DISCURSIVAS_padrao.md: só saem as 7 linhas da nota R2 da D5 (507–513 da v1.3); D1 a D4 e o resto da D5 idênticos; a D4 mantém as 7 linhas (407–413); "Notas de correção" da D5 continua (R3 e R4) — [('delete', 506, 513, 506, 506)]
- OK (3) T54-8b — L3_estudo.md: a única linha que muda fora de "## Pares" é a 422: "jurisprudência firmada que eu possa afirmar):" -> "…que se possa afirmar):"; 0 "que eu possa afirmar" na edição
- OK (3) EDIÇÃO — README: só a linha de versão ("v1.3" -> "v1.4"); data e demais linhas iguais
- OK (3) EDIÇÃO — fidelidade (estudante_fidelidade.py): 0 diferenças contra o pacote com as regras de deleção e as exceções fechadas (CAIXA, nota de BQ-0003, realinhamento do quadro do L1) — comparações 5793, diferenças 0, marcas residuais 2
- OK (3) EDIÇÃO — remoções por deleção: 571 (v1.3) - 3 (a nota R2 da D5: "Alínea c … (R4 do Projeto)", "R2. " e "da versão da CPP") = 568; a regra literal do 6B-06 e o rótulo "(GCE, R3–R4)" substituem as anteriores com a mesma contagem; o realinhamento do L1 (2 linhas) não é remoção — 568
- OK (3) EDIÇÃO — realinhamento do quadro do L1: exceção fechada, 2 linhas, 1 ocorrência cada (REALINHA_HITS), só espaços

Resultados dos demais scripts: `validate.py` 112 verificações, 0 falhas (as 107 da v1.3 com os rótulos de v1.4, mais 5 novas: chaves dos pares com `id`, ids contra o canônico, remissões por id, `a`/`b`/`como` iguais aos da v1.1 salvo a errata oficial já aplicada, errata T-58 do L3; e 2 ajustadas: discursivas e anexo da D5); `estudante_fidelidade.py` 5793 comparações, 0 diferenças (exceções fechadas usadas: CAIXA 8 trocas, nota de BQ-0003 4 exibições, REALINHA 2 linhas; marcas residuais 2, as mesmas da v1.3: "a tecla F4" e "O F4 afirma que"); `sync_check.py` TUDO OK; `fidelidade_mutacao.py` 11 mutações, todas detectadas (255 diferenças no total).

Conferência (f), regeração byte a byte numa cópia limpa do repositório (`git clone` + contrato v1.2.2, registro do contrato e fontes do `gerador_v1_4/` sem `out/`, em outra pasta e com `PYTHONHASHSEED` variados), está registrada no `MANIFESTO.md` (o relatório não pode conter o resultado da própria regeração).

### 13.6 Estado e SHA-256

| Objeto | SHA-256 | bytes |
|---|---|---|
| `saida/pacote/pacote.json` v1.3 (git `9622604`) | `fdcb7afdb4fb449229c6d530e877d839f8d334cd9667731e1b7222c9c7fb0eca` | 620956 |
| `saida/pacote/pacote.json` v1.4 | `f8c0c131f16dab52b1646b3d302670a3afc498b23ac03a7b34a8ff97520ffa54` | 621744 |
| `saida/estudante/` v1.3 (43 arquivos; manifesto ordenado) | `6a60f28116d9ec35d86b476eeff7f133ee8ffe12532a45ea03afab283209d26b` | — |
| `saida/estudante/` v1.4 (43 arquivos; manifesto ordenado) | `562c51398d1e64f8baa6d40932b7344b40639ffdf384783bbdc81064db12cb06` | — |
| `regras/pacote_contrato.md` v1.2.1 (git `9622604`) | `47e3c290646f57ffd985d302f7f16747c1d694abc4ff3660a1825e17ef288f93` | 23286 |
| `regras/pacote_contrato.md` v1.2.2 | `678cfe6da9c156fe4823d2443db6fe9a50b17f1bded73bd3360d0de1d2ca30da` | 26823 |

O SHA-256 do próprio relatório e o manifesto de arquivos do gerador estão em `saida/pacote/gerador_v1_4/MANIFESTO.md` (o relatório não pode conter o próprio hash).

### 13.7 O que NÃO mudou (T54, "Pontos que NÃO mudam")

L6A 135, L5 119 e 126, L3 101 e 574 (D-T54-06 a, b, d); os campos `a`, `b`, `como` dos pares no pacote; o valor da `nota` no pacote; o desalinhamento canônico da linha "Tradução p/ inglês" do quadro do L1; a legenda nos gabaritos de lote (D-T56-02); os avisos do SIM-0 (não exibidos; matéria do Fundador, D-T56-03). Itens: 286 com enunciado, comando, `comandoOriginal`, `textoBase`, gabarito, justificativa, itemEdital, aderência, `volatil` e `nota` idênticos; simulados idênticos; pegadinhas 262.

## Apêndice A — regras literais da edição do estudante (trecho apagado em ⟦ ⟧)

Só as regras **vigentes** da v1.4 (111 regras literais), na ordem de aplicação. Cada linha: fase, tipo, escopo, contexto e trecho apagado; todas verificadas como deleção pura (a especificação é uma subsequência do original). Fora desta lista, por desenho: as regras nº 6 ("O F4 afirma que …", restaurada na L4-11, C-13), nº 26 ("(corrigido pela O-3)" do curso 4.3.4) e nº 63 ("conferida pela QA" da seção ITENS REAIS), retiradas na R1 (C-13, C-14); as nº 42, 44 e 51 da R0 (L6A) constam abaixo na forma da C-16; as duas regras da N-1 (`L6B_estudo`) vieram da v1.3. **Mudanças da v1.4 nesta lista:** a regra do 6B-06 passa a apagar o parêntese inteiro (T54-6); o rótulo do anexo da D5 apaga " (GCE, R3–R4)" (a regra " (GCE, R2–R4)" vale para a D4); as regras que só existiam por causa da nota R2 na D5 deixam de casar nesse trecho (a nota não está mais lá). Conferido por programa: nenhuma regra vigente contém os textos das três retiradas.

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
| 75 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | todos | Notas de correção⟦ (GCE, R3–R4)⟧⏎ |
| 76 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | todos | afirmação⏎    categórica⟦ da versão da CPP⟧, segundo |
| 77 | post | id interno (R-xx, E-xx, O-xx, D-xx) | todos | Alínea c da discursiva⟦ (R4 do Projeto)⟧: |
| 78 | post | id interno (R-xx, E-xx, O-xx, D-xx) | todos | amostras de referência⟦ (errata E1)⟧, não basta |
| 79 | post | id interno (R-xx, E-xx, O-xx, D-xx) | todos | (N1⟦; E3⟧) |
| 80 | post | id interno (R-xx, E-xx, O-xx, D-xx) | todos | Distinção de vocabulário⟦ (O11)⟧: |
| 81 | post | id interno (R-xx, E-xx, O-xx, D-xx) | todos | para o Cargo 11⟦ (D-T2)⟧. |
| 82 | post | carimbo datado de verificação/leitura (ligado a F-ref) | todos | Anthropic, "XML structuring" e OpenAI, "Message formatting with Markdown and XML"⟦, verificadas em 7/10/2026⟧. |
| 83 | post | carimbo datado de verificação/leitura (ligado a F-ref) | todos | "Message formatting with Markdown and XML")⟦, ambas verificadas em 7/10/2026⟧. |
| 84 | post | carimbo datado de verificação/leitura (ligado a F-ref) | todos | reinforcement learning"⟦ (reverificado em 7/10/2026)⟧. Conclusão |
| 85 | post | carimbo datado de verificação/leitura (ligado a F-ref) | todos | "principalmente entre o honesto e o desonesto"⟦ (conferido no Planalto em 08/10/2026)⟧. |
| 86 | post | carimbo datado de verificação/leitura (ligado a F-ref) | todos | Microsoft 365"⟦, conforme a leitura de 08/10/2026⟧) |
| 87 | post | carimbo datado de verificação/leitura (ligado a F-ref) | todos | (seção 1.1⟦; leitura de 08/10/2026⟧) |
| 88 | post | carimbo datado de verificação/leitura (ligado a F-ref) | todos | seus dados"⟦, ambos verificados em 08/10/2026⟧. |
| 89 | post | id interno / versão do lote (v2) | todos | (⟦v2, ⟧item 1.4) |
| 90 | post | id interno / versão do lote (v2) | todos | (⟦v2, ⟧exemplo parlamentar do 1.4) |
| 91 | post | carimbo de leitura "aberta(s) hoje" | todos | Nas páginas de suporte⟦ abertas hoje⟧, a Microsoft |
| 92 | post | carimbo de leitura "aberta(s) hoje" | todos | (conceito geral; sem ⟦fonte aberta hoje para detalhes; sem ⟧item) |
| 93 | post | carimbo de leitura "aberta(s) hoje" | todos | (conceito geral⟦; sem base aberta hoje⟧) |
| 94 | post | carimbo de leitura "aberta(s) hoje" | todos | Fontes⟦ abertas hoje⟧: "Faça backups |
| 95 | post | carimbo de leitura "aberta(s) hoje" | todos | uma fora do local), sem ⟦fonte aberta hoje e sem ⟧item. |
| 96 | post | carimbo de leitura "aberta(s) hoje" | todos | Definição de vírus⟦ aberta hoje⟧: "programa |
| 97 | post | carimbo de leitura "aberta(s) hoje" | todos | Definição de ransomware⟦ aberta hoje⟧: "Ransomware |
| 98 | post | carimbo de leitura "aberta(s) hoje" | todos | Definição⟦ aberta hoje⟧: o phishing |
| 99 | post | carimbo de leitura "aberta(s) hoje" | todos | Fonte: conceito geral⟦ (a definição da tríade não foi confirmada em fonte aberta hoje; ver curso 4.1.1)⟧. Tema da tríade |
| 100 | l5 | código de fonte do L5 (U/GG/TB) | L5_ | Power BI (Microsoft)⟦ — fonte principal U1 en-us; U2 só para a natureza Windows do Desktop (verificado em 8/10/2026)⟧ |
| 101 | l5 | código de fonte do L5 (U/GG/TB) | L5_ | Tableau (Salesforce)⟦ — U3; dashboards por TB2 (verificado em 8/10/2026)⟧ |
| 102 | l5 | código de fonte do L5 (U/GG/TB) | L5_ | Data Studio (Google)⟦ — U4, U5, U6, GG4 (verificado em 8/10/2026)⟧ |
| 103 | l5 | código de fonte do L5 (U/GG/TB) | L5_ | 8.3 FERRAMENTAS (VOLÁTIL⟦; verificado em 8/10/2026⟧) |
| 104 | l5 | código de fonte do L5 (U/GG/TB) | L5_ | Três componentes e fluxo ⟦conforme U1 en-us ⟧("three primary |
| 105 | l5 | código de fonte do L5 (U/GG/TB) | L5_ | natureza Windows do Desktop⟦ conforme U2⟧. |
| 106 | post | classificação interna de VOLÁTIL na justificativa | todos | Depende de padrão técnico estável, não de produto⟦; NÃO VOLÁTIL⟧. |
| 107 | post | classificação interna de VOLÁTIL na justificativa | todos | passou a ser exercida por ela.⟦ REVERIFICAR (normativo) 04–08/01/2027; não VOLÁTIL.⟧ |
| 108 | post | classificação interna de VOLÁTIL na justificativa | todos | "Message formatting with Markdown and XML".⟦ Sem marca VOLÁTIL: o item afirma o conceito, não recurso de produto.⟧ |
| 109 | post | marca de processo ("neste chat") | todos | situação de tramitação não verificada⟦ neste chat⟧) |
| 110 | post | marca de processo de produção do lote ("Nesta produção" / "a especificação previa") | L6B_estudo | ⟦Nesta produção ⟧NÃO foi aberta fonte institucional que defina o termo |
| 111 | post | marca de processo de produção do lote ("Nesta produção" / "a especificação previa") | L6B_estudo | NÃO HÁ ITEM sobre governança digital neste lote⟦ (a especificação previa o item "se houver base")⟧. |

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

**Lista REALINHA (v1.4, D-T54-02; exceção fechada, só espaços inseridos num único ponto imediatamente antes de um `|`; não é remoção; escopo `L1_estudo`; cada regra casa exatamente 1 vez):**

- `                    |               | streaming)     | e fast)* | streaming)` → `                    |               | streaming)     | e fast)*       | streaming)` (+6 espaços)
- `                    |         |                |                |` → `                    |               |                |                |` (+6 espaços)

Nota: "n" não é repetido aqui porque as regras da fase "post" casam com o texto já tratado pelas regras genéricas; as ocorrências efetivas de cada tipo estão na seção 10.1.

## Pendências

- QA: a gbq-cqe confere a v1.4 (fidelidade do pacote e da edição às fontes e à v1.3, o escopo exato da ocorrência, a errata do contrato v1.2.2 e os itens T54-1 a T54-8); a gce-cqfp confere a parte da GCE (item 5: a errata do curso do L3 e o anexo da D5) por script próprio; a gbq-gerencia reconcilia e emite o gatilho A da v1.4. Nada disso foi feito aqui.
- Arquivos do repositório criados ou alterados por esta ocorrência: `saida/pacote/pacote.json`, `saida/estudante/` (regerada), `saida/pacote/pacote_relatorio_2026-10-13_v1_4.md`, `saida/pacote/gerador_v1_4/` (com `MANIFESTO.md`), `regras/pacote_contrato.md` (só a errata v1.2.2) e `saida/pacote/contrato_v1_2_2_2026-10-13.md`. Nenhum outro; a secretaria deve atualizar o estado. A promoção de `out/` para o repositório foi um passo explícito, depois de todas as conferências com 0 falhas.
