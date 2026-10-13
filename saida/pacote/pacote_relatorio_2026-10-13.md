# pacote_relatorio_2026-10-13.md — T-48 — EXPORTAR v1.2 — gerado por gbq-csc

Saídas: `saida/pacote/pacote.json` (versao 1, nome "Câmara 2026 — pacote F4 (v1.2)", geradoEm 2026-10-13, 619485 bytes UTF-8, indent=1, newline final), este relatório e a edição do estudante em `saida/estudante/` (43 arquivos). Contrato: `regras/pacote_contrato.md` v1.1.1 + Regras da v1.2 (D-T12-V12; D1 da GBQ, 13/10/2026). Gerador e validadores: scripts Python no scratchpad da sessão (fora do repositório). Nada foi commitado; TAREFAS.md, PARA_PRESIDENCIA.md, DECISOES.md, estado/, banco/, regras/ e os canônicos dos lotes não foram alterados. A v1.1 foi guardada antes de ser sobrescrita (SHA-256 `d318382639ee`, 541533 bytes). Nada deste pacote nem da edição do estudante vai à candidata sem gatilho A e decisão do Fundador; a edição do estudante NÃO é entrega à candidata.

**Nota R1 (13/10/2026):** as seções 1 a 12 e o Apêndice A descrevem o estado R0 (histórico preservado); os pontos de relatório R4 (gce-cqfp) e O-2 (gcb-cqfp) foram corrigidos no lugar (marcados "[corrigido na R1]"); a correção R1, com resultados dos scripts, novas contagens e SHA-256, está na **seção 13**. Contagens da R1: F4 21 justificativas; pegadinhas 262 (L1 19, L5 48); validação 103 verificações, 0 falhas; fidelidade da edição 0 diferenças.

Resultado em uma linha (R0): **286 itens** (106 de banco + 180 AUTORAL), 10 lotes, 5 discursivas, 4 simulados com `n` e `versao`; 32 registros de errata (31 APLICADA, 1 JÁ PRESENTE, 0 NÃO ENCONTRADA) e 6 erratas com alvo fora do pacote; validação por script: 102 verificações, 0 falhas; edição do estudante: 43 arquivos, fidelidade textual 5477 comparações, 0 diferenças.

## 1. Fontes

Lidas em 13/10/2026 (SHA-256, 12 primeiros dígitos). O arquivo canônico de cada lote é o da tabela de fonte do contrato (regra 4 da v1.1); os `saida/lote*/RECONCILIADO.md` não existem e não são fonte.

| Objeto | Arquivo(s) | Versão / observação | SHA-256 (12) |
|---|---|---|---|
| Contrato | `regras/pacote_contrato.md` | v1.1.1 + Regras da v1.2 (a–j) | `d8ab26b6c3de` |
| Instruções da T-48 | `saida/banco/GBQ_reconciliacao_2026-10-13.md` | seção "INSTRUÇÕES PARA A T-48" e D1-a/b/c | `1c9c364c3d8a` |
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
| L4 | `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | v3.4 (cabeçalho: Despacho 9, 09/10/2026) | `d7d820364ac5` |
| L4C | `saida/gcb/GCB_Lote4C_v1_GCB-CPP.md` | v1.1 (só itens AUTORAL) | `b412bf79842b` |
| L5 | `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` | v3 com a errata Tukey (T-47) já gravada | `5f7f736cd369` |
| L5C | `saida/gcb/GCB_Lote5C_v1_GCB-CPP.md` | v1.1 (só itens AUTORAL) | `390ae7eee2af` |
| L6A | `saida/gcb/GCB_Lote6a_v2_producao_auto.md` | v2 (T-17) | `0d3cc8073603` |
| L6B | `saida/gcb/GCB_Lote6b_v2_producao_auto.md` | v2 com errata A-6b-1 (T-17) | `e89dfc4e12c2` |
| Banco | `banco/banco.csv` | 112 linhas; colunas texto_comando, texto_base, aderencia (T-29/T-42, D1-b) | `b0906e1d91c3` |
| SIM-0 | `saida/simulados/simulado_0_v0.2.md` | v0.2 com o ajuste T-36 | `03db759dd129` |
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
| Relatório anterior | `saida/pacote/pacote_relatorio_2026-10-10.md` | base de comparação (v1.1) | `1eb869850098` |
| v1.1 (antes) | `saida/pacote/pacote.json` | sobrescrito só depois de validado; cópia no scratchpad | `d318382639ee` |

Condições do contrato (regra 5 e instrução da T-48), conferidas em `TAREFAS.md`: T-13, T-25, T-29, T-36, T-38, T-42, T-43, T-44, T-46 e T-47 CONCLUÍDAS e reconciliadas; T-40 CONCLUÍDA (BQ-0072, 0077, 0084, 0109, 0110 e 0111 entram, com 6/6 gabaritos sustentados). Simulados canônicos por D-SIM1-CANONICO, D-SIM2-CANONICO e D-SIM0P2-DIAGNOSTICO; SIM-0 v0.2 sem pendência (T-36 aplicada). Liberar qualquer simulado à candidata continua reservado ao Fundador.

## 2. Contagens v1.1 → v1.2

| Medida | v1.1 | v1.2 |
|---|---|---|
| `versao` / `nome` | 1 / "Câmara 2026 — pacote F4 (v1.1)" | 1 / "Câmara 2026 — pacote F4 (v1.2)" |
| `geradoEm` | 2026-10-10 | 2026-10-13 |
| edital (entradas) | 47 | 47 |
| itens (total) | 240 | 286 |
| itens CEBRASPE_ANALOGA (banco) | 60 | 106 |
| itens AUTORAL | 180 | 180 |
| gabarito C / E (total) | 122 / 118 | 149 / 137 |
| gabarito C / E (banco) | 33 / 27 | 60 / 46 |
| gabarito C / E (AUTORAL) | 89 / 91 | 89 / 91 |
| aderência direta / parcial (total) | 217 / 23 | 247 / 39 |
| aderência direta / parcial (banco; AUTORAL todos direta) | 37 / 23 | 67 / 39 |
| `volatil: true` (total; banco + AUTORAL) | 19 (4 + 15) | 23 (8 + 15) |
| `nota` (itens) | 0 | 2 (BQ-0003, BQ-0040) |
| `comandoOriginal` (itens) | 0 | 90 |
| `textoBase` "nenhum" / "" / texto | 237 / 0 / 3 | 0 / 283 / 3 |
| lotes / discursivas | 10 / 5 | 10 / 5 |
| pegadinhas (total) | 144 | 267 |
| simulados | 2 (SIM-0, SIM-1) | 4 (SIM-0, SIM-1, SIM-2, SIM-0-P2) |
| bytes | 541533 | 619485 |

Banco: 112 linhas em `banco/banco.csv`; 106 exportadas (60 C / 46 E) e 6 excluídas por anulação (gabarito X): BQ-0029, BQ-0030, BQ-0031, BQ-0060, BQ-0062, BQ-0063. Os 60 itens da v1.1 mantêm o mesmo `comando` e a mesma aderência (37 direta / 23 parcial, conferido); os 46 novos são BQ-0061… do terceiro lote de varredura (inclui BQ-0072, 0077, 0084, 0109, 0110 e 0111, liberados pela T-40). BQ-0049 a 0051 são os únicos com `textoBase` (a coluna `texto_base`); nos 283 demais `textoBase` é `""` (F2).

### 2.1 Itens por lote (AUTORAL) e `comandoOriginal`

| Lote | AUTORAL | C | E | `volatil` | `comandoOriginal` | pegadinhas v1.1 → v1.2 | pares |
|---|---|---|---|---|---|---|---|
| L1 | 20 | 10 | 10 | 4 | 0 | 8 → 20 | 17 |
| L1C | 10 | 4 | 6 | 0 | 0 | 1 → 4 | 0 |
| L2 | 30 | 15 | 15 | 0 | 0 | 8 → 43 | 22 |
| L3 | 30 | 16 | 14 | 1 | 0 | 7 → 42 | 28 |
| L4 | 20 | 10 | 10 | 1 | 20 | 32 → 32 | 20 |
| L4C | 10 | 5 | 5 | 0 | 10 | 0 → 0 | 0 |
| L5 | 20 | 10 | 10 | 4 | 20 | 14 → 52 | 15 |
| L5C | 10 | 5 | 5 | 0 | 10 | 0 → 0 | 0 |
| L6A | 15 | 7 | 8 | 5 | 15 | 35 → 35 | 19 |
| L6B | 15 | 7 | 8 | 0 | 15 | 39 → 39 | 18 |

`volatil` no banco (8): BQ-0015, BQ-0017, BQ-0035, BQ-0064, BQ-0075, BQ-0076, BQ-0086, BQ-0089. Em AUTORAL (15): L1-Q14, L1-Q16, L1-Q18, L1-Q19, L3-Q21, L4-15, A5-14, A5-15, A5-16, A5-17, 6A-01, 6A-09, 6A-10, 6A-14, 6A-15. Total 23; os AUTORAL são os VOLÁTIL + REVERIFICAR normativo do registro GBQ v3 (regra R1-N), com L3-Q21.

### 2.2 Simulados (regra (e): `n` e `versao`)

| id | nome | tipo | `versao` | `n` | itens | C / E | `volatil` | parcial |
|---|---|---|---|---|---|---|---|---|
| SIM-0 | Simulado 0 — diagnóstico (v0.2) | diagnóstico | v0.2 | 60 | 60 | 33 / 27 | 4 | 23 |
| SIM-1 | Simulado 1 — P1 final (TI e Dados, itens 5 a 8) | final | v1 | 40 | 40 | 20 / 20 | 0 | 0 |
| SIM-2 | Simulado 2 — P2 final (Reconhecimento de Fala, Transcrição e IA, itens 1 a 4) | final | v1 | 40 | 40 | 20 / 20 | 0 | 0 |
| SIM-0-P2 | Simulado 0-P2 — P2 diagnóstico (Reconhecimento de Fala, Transcrição e IA, itens 1 a 4) | diagnóstico | v1 | 25 | 25 | 13 / 12 | 0 | 0 |

`n` = tamanho da lista `itens` em 4/4. `versao`: SIM-0 "v0.2" (cabeçalho do arquivo); SIM-1, SIM-2 e SIM-0-P2 "v1" (sem versão declarada, regra (e)). Nenhum simulado final contém item `volatil` ou `parcial`. O gabarito de cada posição do simulado (arquivos `*_gabarito.md`) é igual ao `gabarito` do item no pacote em 165/165 posições (60 + 40 + 40 + 25).

### 2.3 Discursivas

D1–D5 idênticas às da v1.1 (nada mudou nas 5): D1 questão (L1), D2 questão e D3 peça (L2), D4 questão e D5 peça (L3). Aspectos e quesitos conferidos: soma dos aspectos das questões 14,30 + 0,70 de apresentação = 15,00; peças 28,50 + 1,50 = 30,00. A observação "inferido pela EXEC" da D1 (Adendo 4) não é exportada: 0 ocorrência de "EXEC" nas discursivas. D3 e D5 são pareceres técnicos (gênero confirmado para analista e técnico; hipótese por analogia para o Cargo 11). Pesos por quesito são HIPÓTESE do Projeto.

## 3. Erratas (consolidações sincronizadas) — estado por errata

Método: substituição exata do trecho "onde se lê" (X) pelo "leia-se" (Y), tolerante a quebra de linha, na ordem do arquivo; cada X deve ter exatamente 1 ocorrência livre (não contida em Y). Estados: **APLICADA** (X encontrado 1 vez e trocado por Y); **JÁ PRESENTE** (X ausente e Y já presente na fonte); **NÃO ENCONTRADA** (nem X nem Y: o script aborta); **FORA DO PACOTE** (o alvo da errata não é exportado; checado: X/Y não vão ao JSON). O gerador aborta em qualquer falha; **0 NÃO ENCONTRADA**. Conferência prévia: `sync_check` leu cada X/Y contra o texto da consolidação sincronizada em `saida/gce/` (resultado: TUDO OK, 27 linhas).

| Lote | Errata | Alvo | Estado | Nota |
|---|---|---|---|---|
| L1 | E1 | Q07 (d): "diarização habilitada, por si só, sem amostras de voz de referência" | APLICADA |  |
| L1 | E2 | Q08 (d): "e um sistema pode diarizar" | APLICADA |  |
| L1 | E3 | Q11 (d): "e, eventualmente, de pistas prosódicas" | APLICADA |  |
| L1 | E4a | curso 1.1: WER "no cálculo usual, sobre texto normalizado…" | APLICADA |  |
| L1 | E4b | curso 1.1: "no cálculo usual ele ignora pontuação, e em qualquer convenção ignora locutores" | APLICADA |  |
| L1 | E4c | (d-G) Q01 (justificativa): "No cálculo usual, pontuação e capitalização ficam fora do WER…" [corrigido na R1; R0: "curso 1.1 (par/pegadinha)"] | APLICADA | Y começa com maiúscula porque X abre a frase (como na v1.1) |
| L1 | E5 | resumo (b), "CLM (texto; indisponível para pt-BR na AWS)" | APLICADA |  |
| L1 | E7a | D1 padrão, quesito 2.3: "[valor máximo: 5,30]" | APLICADA | E7 também insere a linha "Apresentação e estrutura textual: 0,70" |
| L1 | E7b | D1 padrão, nota de correção: "(5,00 / 4,00 / 5,30), mais 0,70 de apresentação" | APLICADA |  |
| L1 | E9 | curso 1.2: espectrograma "em geral (por exemplo, no Whisper)" | APLICADA |  |
| L1 | E10 | curso 1.8: "departamento de registro da Câmara (Derep, antigo DETAQ; Ato da Mesa nº 251/2026)" | APLICADA |  |
| L1 | E12 | resumo (b), WER: "no cálculo usual, sobre texto normalizado, não mede pontuação nem capitalização; locutor fica fora…" (T-46) | APLICADA |  |
| L1 | F5 | F5: "Derep, antigo DETAQ" → "Derep (antigo DETAQ)" (depois da E10) | APLICADA | aplicada depois da E10 |
| L1C | E1 | (d-G) justificativa: reforço por LLM não implica áudio como modalidade do próprio LLM | APLICADA |  |
| L1C | E3 | (d) Q23 (enunciado): "end-to-end, não há dicionário de pronúncias separado" [corrigido na R1; R0: "curso"] | APLICADA |  |
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
| L3 | E1b | resumo (b), linha 4.1: art. 20, "expressão suprimida (MP nº 869/2018, convertida na Lei 13.853/2019)" [corrigido na R1; R0: "curso 4.1"] | APLICADA | o Y usa aspas duplas do arquivo (a consolidação escreve aspas simples) |
| L3 | E2 | curso 4.1: "o art. 5º, II, enumera origem" | APLICADA |  |
| L3 | E3a | curso 4.1: "a MP nº 869/2018, convertida na Lei 13.853/2019, suprimiu a expressão" | APLICADA | o X tem 2 ocorrências no texto bruto; 1 depois da E1b (aplicação em sequência), que é a que a errata visa |
| L3 | E3b | (d-G) Q20 (justificativa): idem, "da redação original" [corrigido na R1; R0: "curso 4.1"] | APLICADA |  |
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
- **F4 (marcas internas das justificativas): feita em 18 justificativas** (a gatilho A dizia 17 "entre outras"), ver seção 6.
- **F5 ("Derep (antigo DETAQ)"): feita.** 1 substituição no L1 (curso 1.8, E10 já com a forma "Derep, antigo DETAQ" → "Derep (antigo DETAQ)"); 0 "Derep, antigo DETAQ" no JSON; a forma correta ocorre 13 vezes no JSON e nenhuma outra grafia de DETAQ fora dela.
- **D1-b (aderência explícita): feita.** Todo item de banco recebe `aderencia` da coluna do `banco.csv`, sem recálculo (106/106 iguais à coluna: 67 direta / 39 parcial). A regra por texto de `observacoes` deixou de valer para a exportação.
- **D1-c (comando normalizado + `comandoOriginal`): feita em 90 itens** (L4 20, 4C 10, A5/L5 20, 5C 10, 6A 15, 6B 15; L1–L3 e banco: 0). Regex `(?i)(julgue os itens) (?:de )?(?:[0-9A-Z]+-)?\d+ a (?:[0-9A-Z]+-)?\d+\.` → "julgue os itens a seguir."; o resto da frase fica literal e o literal vai em `comandoOriginal`. Conferido: só o trecho da numeração muda; BQ-0070, 0071 e 0112 ficam com o comando inteiro e sem `comandoOriginal`; nenhum comando restante com faixa de itens.

## 5. Diff textual resumido v1.1 → v1.2 por lote

Campos de lote comparados caractere a caractere (difflib). Campos não citados: idênticos.

**L1**
- resumo: 2446 → 2543 caracteres, 3 operações:
  - insere "o cálculo usual, sobre texto normalizado, n"
  - insere "capitalização; "
  - insere " fica fora do WER em qualquer convenção"
- curso: 22641 → 22642 caracteres, 3 operações:
  - remove ","
  - insere "("
  - insere ")"
- pegadinhas: 8 → 20 entradas (desdobramento da F3), todas com `rotulo`.

**L1C**
- pegadinhas: 1 → 4 entradas (desdobramento da F3), todas com `rotulo`.

**L2**
- resumo: 2609 → 2746 caracteres, 4 operações:
  - insere "Forma de identificar o orador: observada nas notas oficiais de 2026 (N1; E3). "
  - remove "exata "
  - insere "a para marcação de pausas e eventos não falados e para grafi"
  - insere " (N2)"
- pegadinhas: 8 → 43 entradas (desdobramento da F3), todas com `rotulo`.

**L3**
- curso: 26978 → 27731 caracteres, 3 operações:
  - remove "ERRATA T-08, 10/10/2026; "
  - remove " (registro da GCB-CQFP, 08/10/2026)"
  - insere "Contexto institucional — Ato da Mesa nº 225, de 15/12/2025 (DCD, Ed.⏎Extra A, 18/12/2025): estabelece diretrizes gerais para a política de⏎governança de intelig"
- pares: 28 pares; 1 com texto alterado.
- pegadinhas: 7 → 42 entradas (desdobramento da F3), todas com `rotulo`.

**L4**
- resumo, curso, pares e itensEdital idênticos; pegadinhas: mesma contagem (32), agora com `rotulo`.

**L4C**
- resumo, curso, pares e itensEdital idênticos; pegadinhas: mesma contagem (0), agora com `rotulo`.

**L5**
- curso: 18901 → 19003 caracteres, 1 operações:
  - insere " O fator 1,5·AIQ é a convenção usual (Tukey); outras convenções existem e a prova costuma cobrar esta."
- pegadinhas: 14 → 52 entradas (desdobramento da F3), todas com `rotulo`.

**L5C**
- resumo, curso, pares e itensEdital idênticos; pegadinhas: mesma contagem (0), agora com `rotulo`.

**L6A**
- resumo, curso, pares e itensEdital idênticos; pegadinhas: mesma contagem (35), agora com `rotulo`.

**L6B**
- resumo, curso, pares e itensEdital idênticos; pegadinhas: mesma contagem (39), agora com `rotulo`.

Itens (campo a campo, v1.1 → v1.2): `textoBase` 237 (F2, "nenhum" → ""), `comando` 90 e `comandoOriginal` 90 (D1-c), `justificativa` 18 (F4), `nota` 2 (BQ-0003, BQ-0040), `enunciado` 1 (L1-Q04, F1). `gabarito`, `aderencia` (nos 60 da v1.1), `itemEdital`, `rotulo`, `certame`, `cargo`, `ano`, `numero` e `url`: 0 diferença. Discursivas: 0 diferença. Edital: igual.

## 6. F4 — justificativas alteradas (antes / depois)

Só deleção (conferido por difflib: nenhuma inserção nem troca); cada trecho a apagar ocorre exatamente 1 vez; depois da deleção, sem espaço duplo nem espaço antes de pontuação; 0 marca de processo (CQFP/CQE/CPP/GCE/GCB/GBQ/EXEC, T-xx, "(vN", Oxx, "Lição", R-4C1, "Risco") remanescente nas justificativas. **18 justificativas** (o gatilho A dizia 17 e listava 12 nominalmente, "entre outras"): as 12 nomeadas (L2-Q23, L4-08, 09, 13, 15, 17, 18, 19, 20, 4C-06, 08, 09) mais A5-14, 15, 16, 17, 5C-03 e 5C-06, que também tinham "Risco …", "R-5C1" ou "Lição O10". As 17 da GBQ são as justificativas com os tipos de marca que ela listou (CQFP, "(v3 — O12)", "(O1)", "Lição O10", "R-4C1", "Risco"); a 18.ª é a 5C-03 ("R-5C1", mesma classe de R-4C1); com a rodada R1 (6B-06, 6B-15, L2-Q21) a F4 soma 21 [corrigido na R1, gcb-cqfp O-2; R0 dizia: "Pode-se contar 17 se A5-14 a A5-17 forem tomados como um bloco de 3 ou se a L2-Q23 não for contada"]; registro em DÚVIDA 1.

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
- depois: GI (restrição indevida do conceito; tentação: tratar a injeção de prompt como sinônimo do ataque direto do usuário). Curso 5.1.4: injeção de prompt = instruções maliciosas embutidas em textos que o modelo lê e que tentam sobrepor-se às instruções legítimas (conceito geral, sem fonte de fornecedor, como no curso). o item não depende de a literatura tratar o jailbreak como espécie de injeção ou como categoria distinta; basta que a injeção abranja as instruções embutidas em textos lidos, o que o curso afirma e o termo "restringe-se" nega. O item não usa o par injeção × jailbreak (C19) como critério. Fonte: curso 5.1.4.
- apagado: "Lição O10: "

**4C-09**
- antes: sem armadilha (ancoragem; R-4C1). Curso 5.1.2 (item 3): o contexto é o texto sobre o qual o modelo deve trabalhar; curso 5.1.3: o RAG recupera documentos e os insere no prompt; curso 5.3.3: sem ferramentas ou RAG, o modelo responde com o que incorporou no treinamento (conhecimento paramétrico). Um relatório elaborado depois do treinamento não integra esse conhecimento; sem ferramentas externas (como a busca), sem RAG e sem retreinamento, o caminho é incluí-lo no prompt, como contexto. Retificação 6-A: a redação "sem acesso a busca" não excluía outras ferramentas; "ferramentas externas (como a busca)" alinha o item ao curso 5.3.3 ("sem ferramentas ou RAG"). O acréscimo "e sem retreinamento" existe porque o curso (5.1.1; 5.3.3) prevê o fine-tuning como outra forma de incorporar conhecimento: sem a ressalva, o "deve" ficaria vulnerável a recurso. Difere do item 15 do Lote 4 porque aquele julga se o modelo consulta fontes externas por si só; este julga a aplicação (o material entra como contexto do prompt). Difere do item 6 do Lote 4 porque aquele julga RAG × retreinamento. Fonte: curso 5.1.2, 5.1.3 e 5.3.3.
- depois: sem armadilha (ancoragem). Curso 5.1.2 (item 3): o contexto é o texto sobre o qual o modelo deve trabalhar; curso 5.1.3: o RAG recupera documentos e os insere no prompt; curso 5.3.3: sem ferramentas ou RAG, o modelo responde com o que incorporou no treinamento (conhecimento paramétrico). Um relatório elaborado depois do treinamento não integra esse conhecimento; sem ferramentas externas (como a busca), sem RAG e sem retreinamento, o caminho é incluí-lo no prompt, como contexto. Retificação 6-A: a redação "sem acesso a busca" não excluía outras ferramentas; "ferramentas externas (como a busca)" alinha o item ao curso 5.3.3 ("sem ferramentas ou RAG"). O acréscimo "e sem retreinamento" existe porque o curso (5.1.1; 5.3.3) prevê o fine-tuning como outra forma de incorporar conhecimento: sem a ressalva, o "deve" ficaria vulnerável a recurso. Difere do item 15 do Lote 4 porque aquele julga se o modelo consulta fontes externas por si só; este julga a aplicação (o material entra como contexto do prompt). Difere do item 6 do Lote 4 porque aquele julga RAG × retreinamento. Fonte: curso 5.1.2, 5.1.3 e 5.3.3.
- apagado: "; R-4C1"

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
- depois: TC (tentação: "bigodes vão sempre do mínimo ao máximo" ou "outlier de um lado afeta os dois bigodes" → marcar E). Curso 8.2, box plot: cada bigode vai até o dado mais extremo do seu lado que esteja dentro do limite respectivo; a regra vale por lado; um outlier superior não impede que o bigode inferior termine no mínimo da amostra. a regra de 1,5 · AIQ é convenção usual adotada por muitos programas e pode variar; por isso o item abre com "segundo a regra usual" e não afirma que todo box plot a usa. Sem atribuição a autor. Difere dos itens A5-12 e A5-13 porque aqueles julgam a forma da distribuição e a posição da mediana; este julga a regra dos bigodes por lado.
- apagado: "Lição O10: "

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

| Lote | entradas v1.1 → v1.2 | modos de origem (entradas da v1.1) |
|---|---|---|
| L1 | 8 → 20 | unica 4, enumeradores 1, ponto-e-virgula 3 |
| L1C | 1 → 4 | enumeradores 1 |
| L2 | 8 → 43 | enumeradores 8 |
| L3 | 7 → 42 | enumeradores 7 |
| L4 | 32 → 32 | unica 32 |
| L4C | 0 → 0 | — |
| L5 | 14 → 52 | ponto-e-virgula 14 |
| L5C | 0 → 0 | — |
| L6A | 35 → 35 | unica 35 |
| L6B | 39 → 39 | unica 39 |

Texto corrido que não se separa sem reescrever (ficou como uma entrada só, por contrato): L1 P2-1.1, P2-1.2, P2-1.4 e P2-1.7 (frases soltas "Outra:", "Também:", sem separador marcado). Enumeradores cujo conteúdo tem ";" interno ficaram íntegros (precedência do enumerador): L1 P2-1.3 (1), L2 P2-2.6 (6) e L3 P2-4.3 (2). Assertiva única com ";" dentro do parêntese, mantida inteira: L6A, slide mestre (`"…" → ERRADO (guia Exibir; F7) — VOLÁTIL`). L4, L6A e L6B já tinham uma pegadinha por entrada (contagem igual).

Fragmentos que dependem do verbo ou do sujeito do fragmento anterior (efeito do ";" sem reescrita; DÚVIDA 3): L5 [29] (Gráfico de barras (colunas)) "empilhado quando se quer comparar as partes entre si."; L5 [34] (Box plot (diagrama de caixa)) "que a caixa vai do mínimo ao máximo ou contém todos os "; L5 [35] (Box plot (diagrama de caixa)) "que os bigodes vão até 1,5 desvio padrão"; L5 [36] (Box plot (diagrama de caixa)) "que mostra frequência por intervalo (isso é histograma)". Os demais fragmentos de L5 começam por infinitivo e se leem soltos.

## 9. Validação por script (102 verificações, 0 falhas)

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
- OK AUTORAL v1.1 → v1.2: campos alterados só textoBase(180), comando/comandoOriginal(90), justificativa(18), enunciado(1: L1-Q04) — {'textoBase': 180, 'enunciado': 1, 'justificativa': 18, 'comandoOriginal': 90, 'comando': 90}
- OK F1: L1-Q04 contém "áudio–texto"; 0 "áudio– texto" no JSON
- OK F1: nenhuma outra letra+"– "+letra no JSON (efeito de quebra de linha)
- OK F4: 18 justificativas alteradas (≈17 esperado; ver relatório)
- OK F4: cada alteração é SÓ deleção (antes → depois: nenhuma inserção nem troca de caracteres)
- OK F4: justificativas finais = depois
- OK F4: 0 marca de processo (CQFP/CQE/CPP/GCE/GCB/GBQ/EXEC/T-xx/(vN/Oxx/Lição/R-4C1/Risco) em justificativas
- OK F5: 0 "Derep, antigo DETAQ"; "Derep (antigo DETAQ)" no L1 (curso, E10) — ocorrências totais da forma correta: 13
- OK contagem por lote = declarada {'L1': 20, 'L1C': 10, 'L2': 30, 'L3': 30, 'L4': 20, 'L4C': 10, 'L5': 20, 'L5C': 10, 'L6A': 15, 'L6B': 15}
- OK lotes: itensEdital, pares e pegadinhas são listas JSON em 10/10 lotes; itensEdital ⊂ edital
- OK lotes: campos id, nome, prova, itensEdital, resumo, curso, pares, pegadinhas
- OK lotes: itensEdital iguais aos da v1.1 (10/10)
- OK pares por lote iguais à v1.1 (L1 17, L2 22, L3 28, L4 20, L5 15, L6A 19, L6B 18)
- OK pegadinhas.itemEdital existem no edital
- OK F3: toda pegadinha tem itemEdital, rotulo (não vazio) e texto (não vazio), nessa ordem
- OK F3: todo rotulo é trecho literal do arquivo canônico do lote ou do edital (sem marcas internas)
- OK F3: nenhum rotulo com marca interna ([V, [TS], F1.., U1.., verificado em, ITEM)
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
- OK simulados: n = tamanho de itens = 60, 40, 40, 25; chaves id,nome,tipo,versao,n,itens
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

Gerada a partir do `pacote.json` v1.2 (fonte única). **43 arquivos**: `README.md` (índice, versão v1.2, data 2026-10-13, aviso "material de estudo; gabaritos em arquivo separado"); por lote, `<ID>_estudo.md` (itens do edital, resumo, curso, pares, pegadinhas com rótulo), `<ID>_itens.md` (comando, texto-base se houver, enunciado; sem gabarito, justificativa nem marcas) e `<ID>_gabarito.md` (gabarito, item do edital e justificativa) para L1, L1C, L2, L3, L4, L4C, L5, L5C, L6A e L6B (30 arquivos); `BANCO_itens.md` e `BANCO_gabarito.md` (certame, cargo, ano, número, URL oficial, aviso VOLÁTIL e `nota` literal); por simulado `<SIM>_folha.md` e `<SIM>_gabarito.md` (SIM-0, SIM-1, SIM-2, SIM-0-P2); `DISCURSIVAS.md` e `DISCURSIVAS_padrao.md`. Resumo e curso vão em blocos de texto cercados, para preservar quebras, recuos e tabelas.

**Regra:** as marcas internas saem SOMENTE POR DELEÇÃO (nunca reescrita) por `estudante_marcas.py`; a marca VOLÁTIL vira, nos itens `volatil: true`, o aviso fixo "Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027."; a `nota` (BQ-0003, BQ-0040) é exibida literal junto do item. Enunciado, comando e texto-base de item não são tocados (afirmado por teste: nenhuma marca da lista neles). Regras genéricas (por tipo) e regras literais (frase ou cláusula a apagar, `⟦…⟧` na especificação):

- `[V dd/mm/aaaa — …]` apagado inteiro, com o espaço anterior (o colchete pode quebrar linha entre "[V" e a data); duas exceções que mantêm a orientação ao estudante: `[V … — F4; NORMATIVO — QA; norma de caráter experimental, não cobrar o texto]` fica `[norma de caráter experimental, não cobrar o texto]` e `[V … contexto histórico]` fica `[contexto histórico]`.
- `[NORMATIVO — QA: base legal]` perde o prefixo e o colchete e fica a base legal ("LGPD, art. 5º, I."); `[NORMATIVO — QA]` e as variantes com ";" são apagadas (`[NORMATIVO — QA; não cobrar além do texto]` fica `[não cobrar além do texto]`); a frase "…com a marca [NORMATIVO — QA]. Fontes: F1 … lidas em 08/10/2026." do L3 sai, ficando "Todos os dispositivos abaixo estão em paráfrase."
- Referências de fonte F1…F22: `[Fn]`, `(Fn)`, `(Fn, Fm)`, `(Fn, verificado em …)`, `(Fn, seção …)`, `, Fn)` no fim de parêntese, `; Fn)`, `(Fn: ` e `(Fn, "…")` (mantém o parêntese e o conteúdo), "Conforme a Fn (leitura de …):", frases "Fonte(s): Fn, …verificado em …." e, em trechos de prosa (89 regras literais no total), a cláusula ou palavra que só existe por causa da referência (lista completa no apêndice A). "A tecla F4" (Excel) NÃO é referência e permanece.
- Agentes e unidades (CQFP, QA, GCB, GCE, CPP) em carimbos como "(conferido pela CQFP em 08/10/2026)", "conforme a CQFP", "(GCB-CPP)", "Decisão da GCE", "versão da CPP", "para o QA Normativo", "Síntese da CQFP … colado pelo Fundador"; ids internos "(errata E1)", "; E3" em "(N1; E3)", "(O11)", "(corrigido pela O-3)", "(D-T2)", "(R4 do Projeto)" e, nos padrões D4/D5, "(GCE, R2–R4)" e os enumeradores "R2. ", "R3. ", "R4. ".
- Carimbos datados ligados a uma referência apagada ("verificadas em 7/10/2026", "(reverificado em …)", "conforme a leitura de 08/10/2026", "(conferido no Planalto em …)").

### 10.1 Marcas removidas por tipo e por arquivo

Contagem de ocorrências apagadas, por arquivo gerado (um item presente em lote e em simulado é contado nos dois arquivos). Total nos arquivos: **492**.

| Tipo | Ocorrências |
|---|---|
| F (parêntese) | 87 |
| V | 58 |
| F (prosa: referência a fonte) | 54 |
| F (fim de parêntese) | 48 |
| F (frase "Fonte(s): …") | 42 |
| agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | 27 |
| F (colchete) | 26 |
| F (parêntese com verificação) | 26 |
| NORMATIVO — QA (prefixo da base legal) | 23 |
| NORMATIVO — QA | 18 |
| F (início de parêntese) | 14 |
| F (fim de parêntese, após vírgula) | 13 |
| id interno (R-xx, E-xx, O-xx, D-xx) | 12 |
| F (frase de fonte) | 11 |
| F ("Conforme a Fn (leitura …):") | 11 |
| carimbo datado de verificação/leitura (ligado a F-ref) | 7 |
| F (parêntese com seção/verificação) | 5 |
| V (parcial: mantém a orientação ao estudante) | 2 |
| F (fim de parêntese, "com Fn") | 2 |
| NORMATIVO — QA (parcial: mantém a orientação ao estudante) | 1 |
| NORMATIVO — QA (frase de marca e fontes) | 1 |
| F (fim de parêntese, após travessão) | 1 |
| F (início de parêntese, antes de aspas) | 1 |
| F (parêntese com leitura) | 1 |
| id interno (O-xx) | 1 |
| **Total** | **492** |

| Arquivo | Total | Detalhe por tipo |
|---|---|---|
| DISCURSIVAS_padrao.md | 14 | id interno (R-xx, E-xx, O-xx, D-xx) 9; agente/unidade interna (CQFP, QA, GCB, GCE, CPP) 5 |
| L1C_estudo.md | 2 | V 1; id interno (R-xx, E-xx, O-xx, D-xx) 1 |
| L1C_gabarito.md | 3 | F (colchete) 2; V 1 |
| L1_estudo.md | 52 | V 37; F (colchete) 15 |
| L1_gabarito.md | 7 | F (colchete) 6; V 1 |
| L2_estudo.md | 17 | V 12; V (parcial: mantém a orientação ao estudante) 2; F (colchete) 1; id interno (R-xx, E-xx, O-xx, D-xx) 1; F (parêntese) 1 |
| L2_gabarito.md | 3 | V 2; F (colchete) 1 |
| L3_estudo.md | 24 | NORMATIVO — QA 18; agente/unidade interna (CQFP, QA, GCB, GCE, CPP) 2; NORMATIVO — QA (parcial: mantém a orientação ao estudante) 1; NORMATIVO — QA (frase de marca e fontes) 1; V 1; F (fim de parêntese, após vírgula) 1 |
| L3_gabarito.md | 13 | NORMATIVO — QA (prefixo da base legal) 13 |
| L4C_gabarito.md | 12 | F (parêntese) 6; F (frase de fonte) 3; F (prosa: referência a fonte) 3 |
| L4_estudo.md | 83 | F (parêntese) 22; agente/unidade interna (CQFP, QA, GCB, GCE, CPP) 16; F (parêntese com verificação) 15; F (prosa: referência a fonte) 15; F (início de parêntese) 5; F (fim de parêntese, após vírgula) 4; carimbo datado de verificação/leitura (ligado a F-ref) 3; F (fim de parêntese, após travessão) 1; F (início de parêntese, antes de aspas) 1; id interno (R-xx, E-xx, O-xx, D-xx) 1 |
| L4_gabarito.md | 24 | F (frase "Fonte(s): …") 15; F (parêntese) 4; F (prosa: referência a fonte) 3; carimbo datado de verificação/leitura (ligado a F-ref) 1; F (início de parêntese) 1 |
| L5_estudo.md | 1 | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) 1 |
| L6A_estudo.md | 128 | F (fim de parêntese) 48; F (parêntese) 39; F (prosa: referência a fonte) 19; F ("Conforme a Fn (leitura …):") 11; F (fim de parêntese, após vírgula) 4; F (início de parêntese) 4; carimbo datado de verificação/leitura (ligado a F-ref) 2; F (parêntese com leitura) 1 |
| L6A_gabarito.md | 20 | F (frase "Fonte(s): …") 15; F (parêntese) 2; F (prosa: referência a fonte) 2; F (início de parêntese) 1 |
| L6B_estudo.md | 41 | F (parêntese com verificação) 11; F (parêntese) 9; F (parêntese com seção/verificação) 5; F (fim de parêntese, após vírgula) 4; F (prosa: referência a fonte) 4; F (início de parêntese) 2; F (fim de parêntese, "com Fn") 2; agente/unidade interna (CQFP, QA, GCB, GCE, CPP) 2; F (frase de fonte) 1; carimbo datado de verificação/leitura (ligado a F-ref) 1 |
| L6B_gabarito.md | 12 | F (prosa: referência a fonte) 5; F (frase de fonte) 5; agente/unidade interna (CQFP, QA, GCB, GCE, CPP) 1; id interno (O-xx) 1 |
| SIM-0-P2_gabarito.md | 5 | NORMATIVO — QA (prefixo da base legal) 4; V 1 |
| SIM-1_gabarito.md | 22 | F (frase "Fonte(s): …") 12; F (parêntese) 4; F (prosa: referência a fonte) 3; F (frase de fonte) 2; F (início de parêntese) 1 |
| SIM-2_gabarito.md | 9 | NORMATIVO — QA (prefixo da base legal) 6; V 2; F (colchete) 1 |

Contagem única por campo do pacote (sem repetir a justificativa que aparece em lote e em simulado): **456** ocorrências.

Arquivos sem nenhuma remoção: os `*_itens.md`, `BANCO_*`, `*_folha.md`, `README.md` e os `*_gabarito.md` cujos itens não tinham marca (a tabela só lista os arquivos com remoção).

### 10.2 Fidelidade (script `estudante_fidelidade.py`)

O script lê os 43 arquivos com um parser próprio (independente do gerador) e confere, campo a campo, o texto do estudante com o do pacote: (1) igual ao texto do pacote com as deleções das regras; (2) obtido do texto do pacote só por deleção (difflib: apenas `equal`/`delete`; 0 `insert`/`replace`); (3) comando, texto-base, enunciado, gabarito, item do edital, aderência, nota, aviso VOLÁTIL, certame, cargo, ano, número, URL, ordem e `n` dos simulados, valores dos aspectos e conceitos dos quesitos idênticos ao pacote. Teste negativo (mutação de 3 arquivos) detectou 9 diferenças, portanto o script não é cego.

- comparações: texto 1390, metadado 807, estrutura 44, prova/metadado 1883, aviso/nota 902, gabarito 451 (total 5477)
- **diferenças: 0** (texto do estudante == texto do pacote com as deleções aplicadas)
- marcas residuais nos arquivos pela varredura de higiene (V, NORMATIVO — QA, [TS], CQFP/CQE/CPP/GCE/GCB/GBQ/EXEC, F1…F22, T-/R-/E-/O-xx, "(errata En)"): 1, a saber: L6A_estudo.md linha 83 "F4" (tecla do Excel, não é referência).

## 11. Marcas que permanecem (varredura)

**No `pacote.json` (por desenho):** curso, resumo, pegadinhas e justificativas AUTORAL conservam as marcas de processo do arquivo canônico, porque o pacote é dado, não edição do estudante (decisão do gatilho A: só a edição do estudante as retira, e a F4 limpou apenas as 18 justificativas com marca de agente/risco/lição). Contagem no JSON: `[V …]` 57; `[NORMATIVO — QA…]` 33; referências F1…F22 402; CQFP/CPP/GCE/GCB/QA em texto de lote 24.

**Na edição do estudante, fora da lista de marcas pedida, permanecem (DÚVIDA 5):** códigos de nota "N1…N9" do curso de L2, L3 e L4 (definidos no próprio texto; ex.: "LGPD (N1, Lei 13.709/2018)"); códigos de fonte do L5 "U1…U6", "TB2", "GG4", "CI" e o carimbo "(verificado em 8/10/2026)" que os acompanha; as etiquetas de mecanismo das justificativas ("GI", "TC", "IC", "AT"); "REVERIFICAR (normativo) 04–08/01/2027; não VOLÁTIL" (L3-Q21) e "NÃO VOLÁTIL"/"não VOLÁTIL"/"Sem marca VOLÁTIL" nas justificativas L2-Q23, L3-Q21 e L4-05; as palavras "VOLÁTIL" de títulos do curso do L4, L5 e L6A (ex.: "— VOLÁTIL"); e a expressão "aberta hoje" (leitura de fonte) no curso do L6B.

## 12. DÚVIDAS para a GBQ

1. **F4: 18 em vez de 17.** A varredura achou 18 justificativas com marca de agente, risco ou lição; o gatilho A falava em 17 "entre outras". Apliquei as 18. Se a GBQ quiser 17, diga qual excluir (candidata natural: nenhuma; todas têm marca). Efeito: só deleção. [R1: decidido na reconciliação (D-R1-20 e DÚVIDA 1): aceitas as 18; as 17 da GBQ são as dos tipos listados e a 18.ª é a 5C-03 ("R-5C1"); com 6B-06, 6B-15 e L2-Q21 a F4 passa a 21 justificativas.]
2. **F4: inicial minúscula depois de "Lição O10: ".** 4C-08 e 5C-06 ficam com a frase começando em minúscula, porque a deleção pura impede maiúscula. Aceitar, ou autorizar a capitalização (seria troca de letra, contra a regra de só deleção).
3. **F3: fragmentos dependentes e entradas não desdobradas.** O desdobramento por ";" dá fragmentos que começam por "que …" (L5, box plot [34]–[36]) e "empilhado quando…" (L5 [29]), que só se leem junto do verbo do fragmento anterior. As entradas P2 em texto corrido (L1 P2-1.1, 1.2, 1.4, 1.7) e os enumeradores com ";" interno (L1 P2-1.3, L2 P2-2.6, L3 P2-4.3) ficaram íntegros. Aceitar como está, ou mandar reescrita (fora da regra de literalidade).
4. **F3: rótulo por hierarquia.** Onde o texto canônico não tem bloco próprio usei o texto do edital (P2 e L4/L6B) ou o título do item do lote (L6A: WORD, EXCEL, …). Dois rótulos terminam em dois-pontos porque o texto do edital termina assim ("Desafios do ASR em Português Brasileiro:", "Ferramentas e APIs: …"). Aceitar.
5. **Marcas fora da lista (edição do estudante).** Não apaguei N1…N9, U1…U6/TB/GG/CI (L5), GI/TC/IC/AT, "NÃO VOLÁTIL", "REVERIFICAR", "aberta hoje" nem o carimbo "(verificado em 8/10/2026)" do L5, porque não estão na lista (F1..F9, [V…], [TS], NORMATIVO — QA, agentes, T/R/E/O-xx, Risco). Os códigos U/TB/GG/CI são o equivalente das F do L5; apagá-los é uma ampliação simples (flag no script). Decidir.
6. **"Risco …".** Nas justificativas AUTORAL a marca "Risco BAIXO/MÉDIO" foi apagada (F4). No curso e no resumo, "Risco/Riscos" é conteúdo de estudo (riscos de IA, de segurança) e foi mantido. Confirmar.
7. **Texto de lote que perdeu conteúdo substantivo ao apagar a fonte.** Algumas deleções tiraram citação ou observação de fonte além da etiqueta (ex.: L6A, "A F9 também usa os rótulos "Pode editar" e "Pode exibir""; L6A, a frase da F19 sobre a experiência do Teams; as citações em inglês da F4 na L4-11; justificativas 4C-02, 4C-03, 4C-07, 6B-07, 6B-08, 6B-09, 6B-10 e 6B-13 com a frase "Fonte: …" inteira; citações de fonte em L4-07, L4-11, L4-13, 4C-04 a 4C-06, 6A-09, 6A-11, 6B-04, 6B-05, 6B-11, 6B-14 e 6B-15). Todas estão no apêndice A com o trecho apagado. Se a GBQ preferir manter alguma, o ajuste é remover a regra literal correspondente.
8. **Inicial minúscula e sujeito oculto após deleção.** Em poucos trechos do curso do L6A a deleção deixa a frase começando em minúscula ("por padrão os clientes POP3…", "mesclar combina…") ou sem sujeito explícito ("NÃO é possível mudar… e orienta excluir o link…"). Está no apêndice A; a leitura continua clara, mas o texto não foi retocado.
9. **Tabelas de colunas fixas.** Ao apagar `[F10]`, `[F12]` etc. de linhas do QUADRO-SÍNTESE do curso do L1, o alinhamento das colunas de texto monoespaçado desloca. Só estético; não retocado.
10. **Aviso VOLÁTIL em item de lote com `volatil` por REVERIFICAR normativo.** L3-Q21 e L4-15 etc. recebem o mesmo aviso fixo (janeiro de 2027). Confirmar que o aviso único serve também para REVERIFICAR normativo.
11. **Aderência dos itens de banco no estudante.** Mostrei "(aderência: direta|parcial)" no gabarito do banco e dos simulados. A GBQ pode preferir não mostrar. Decidir.
12. **Itens fora do exportado.** As seis erratas FORA DO PACOTE (seção 3.1) não têm um dos três estados do contrato; criei o quarto rótulo para elas. Confirmar.
13. **Alvo duplicado da E3a do L3.** O X da E3a tem 2 ocorrências no texto bruto do L3 (uma é eliminada pela E1b na aplicação em sequência). O gerador aplica em sequência e a ocorrência restante é a visada. Confirmar com a GCE se a ordem E1b → E3a é a pretendida.

## 13. Correção R1 (13/10/2026)

Rodada de correção R1 da T-48 (lista C-01 a C-25, seção 3 de `saida/pacote/T48_reconciliacao_R1_2026-10-13.md`, D1 da GBQ). Corrigido o GERADOR (cópia em `s4/t48r1/` do scratchpad; os scripts de `s4/t48/` ficam intactos como prova da R0) e REGERADOS `saida/pacote/pacote.json` e `saida/estudante/` por inteiro (43 arquivos, mesmos nomes); nenhum arquivo foi editado à mão. A saída R0 (pacote.json, relatório e `estudante/`) está guardada em `s4/t48r1/R0/`. Nada foi commitado; TAREFAS.md, PARA_PRESIDENCIA.md, DECISOES.md, estado/, banco/, regras/ e os canônicos dos lotes não foram tocados por esta rodada.

Regras de execução: continua "só deleção", com as duas exceções fechadas da reconciliação (3.0.4): (i) CAIXA (C-05 e C-15): minúscula → maiúscula na primeira letra indicada (2 no pacote, 8 na edição); (ii) reunião de fragmentos de pegadinha com "; " (C-06 a C-08: 5 reuniões, 267 → 262). Mais a exceção da C-18 (nota de BQ-0003 sai da edição sem " (D-LEI-15352)"; no pacote a nota continua literal).

### 13.1 Pacote R0 → R1

| | R0 | R1 |
|---|---|---|
| SHA-256 do `pacote.json` | `ae2f346830f8dea1301a1c78b11ea55fcbb19527727c667bc2fd95a5462b6d19` (619485 bytes) | `f46ed9f8e43db76aaeb96eda0b2924028fb7145c048c5eb0189396c9f67304fe` (618673 bytes) |
| SHA-256 (12 primeiros) | `ae2f346830f8` | `f46ed9f8e43d` |

### 13.2 Tabela C-xx (alvo, resultado, ocorrências)

"Ocorrências" = texto atual R0 → R1 (previsto: 0 no R1) e texto novo no R1. Fonte: `conferencias_R1.py` (118 conferências, 0 falhas), independente do gerador. Onde o texto atual está no pacote e na edição, aparecem os dois.

| C | Alvo | Resultado | Ocorrências |
|---|---|---|---|
| C-01 | 4C-09 `justificativa` (pacote; edição: `L4C_gabarito.md`) | APLICADA (deleção de " Retificação 6-A: … RAG").") | pacote 1 → 0, novo 1; edição 1 → 0, novo 1 |
| C-02 | 6B-06 `justificativa` (pacote); edição já limpa | APLICADA (deleção de ", conferida pela QA em 08/10/2026") | pacote 1 → 0, novo 1; edição 0 → 0 (novo 1 nas duas) |
| C-03 | 6B-15 `justificativa` (pacote); edição já limpa | APLICADA (deleção de " (corrigido pela O-3)") | pacote 1 → 0, novo 1; edição 0 → 0 (novo 1 nas duas) |
| C-04 | L2-Q21 `justificativa` (pacote; edição: `L2_gabarito.md`) | APLICADA (deleção de " Gabarito E mantido.") | pacote 1 → 0, novo 1; edição 1 → 0, novo 1 |
| C-05 | 4C-08 e 5C-06 `justificativa` (CAIXA) | APLICADA: "Lição O10: o item" → "O item"; "Lição O10: a regra" → "A regra" (no pacote R0 a marca já estava apagada e a inicial ficara minúscula: o "atual" medido é "… curso). o item não depende" e "… amostra. a regra de 1,5") | pacote 4C-08 1 → 0 e 5C-06 1 → 0 (novo 1 + 1); edição 4C-08 2 → 0 (`L4C_gabarito.md` e `SIM-1_gabarito.md`) e 5C-06 1 → 0 |
| C-06 | `lotes[L1].pegadinhas`, P2-1.5 | APLICADA: 2 entradas → 1 (dict literal da lista) | entradas 2 → 1; L1 20 → 19; edição `L1_estudo.md` 2 linhas → 1 |
| C-07 | `lotes[L5].pegadinhas`, Gráfico de barras (colunas) | APLICADA: "usar para distribuição…; empilhado quando…" reunida; "confundir com histograma" e "aceitar eixo truncado" ficam | entradas do rótulo 4 → 3; edição `L5_estudo.md` 2 linhas → 1 |
| C-08 | `lotes[L5].pegadinhas`, Box plot (diagrama de caixa) | APLICADA: 4 fragmentos → 1 entrada (dict literal da lista) | entradas 4 → 1; L5 52 → 48; edição `L5_estudo.md` 4 linhas → 1 |
| C-09 | validador F4 (`validate.py`) | APLICADA: padrões `(?<!NORMATIVO — )\bQA\b`, `\bO-\d+\b`, `Retificação`, `[Gg]abarito [CE] mantido` acrescentados | R0 acusaria 4 justificativas (4C-09, 6B-06, 6B-15, L2-Q21); R1: 0 nas 180 AUTORAL |
| C-10 | folhas SIM-0, SIM-1, SIM-2, SIM-0-P2 (linhas de item) | APLICADA: `**{n}** — {enunciado}`; o id fica só nos `*_gabarito.md` | linhas com id 165 → 0; linhas sem id 165; id presente nos gabaritos 165/165 |
| C-11 | `BANCO_itens.md` (BQ-0049, 0050, 0051) e `SIM-0_folha.md` (item 12) | APLICADA: "Texto-base" antes de "Comando" nos três pontos de emissão (banco, folha, `*_itens.md`) | pares Comando→Texto-base 4 → 0; Texto-base→Comando 0 → 4 (BANCO_itens 3, SIM-0_folha 1) |
| C-12 | `L4_estudo.md` 224 e 283 (";)") | APLICADA: regra genérica com ";" vem antes da regra com ",?" | "vetado;)" 2 → 0; "vetado)." 2 |
| C-13 | `L4_gabarito.md`, L4-11 (restauração, D-R1-07) | APLICADA: regra literal nº 6 do apêndice A retirada; a frase "O F4 afirma que …" volta literal; só " Fonte: F4, reverificado em 7/10/2026." continua apagada | trecho sem a frase 1 → 0; com a frase 0 → 1; edição = justificativa do pacote menos exatamente a "Fonte: F4…" (conferido) |
| C-14 | regras literais nº 26 ("Curso 4.3.4⟦ (corrigido pela O-3)⟧:") e nº 63 ("seção ITENS REAIS⟦, conferida pela QA…⟧)") | APLICADA: as duas regras retiradas; o resultado na edição é o mesmo da R0 | linhas de 6B-06 e 6B-15 na edição: R0 = R1 (a C-19 só mexe em "aberta hoje" da 6B-06) |
| C-15 | `L6A_estudo.md` (CAIXA, lista fechada de 8) | APLICADA: 8 pares minúscula → maiúscula (1 caractere cada), fase CAIXA depois de `strip_text`, só no arquivo `L6A_estudo` | 8 pares, cada 1 → 0 (novo 1) |
| C-16 | `L6A_estudo.md` (a) 166, (b) 60, (c) 135 | APLICADA: (a) a linha "portas e criptografia do Exchange Online; …" some inteira com a quebra anterior (a seguinte é a em branco antes de "### 3.1.3"); (b) "diz " apagado ("(\"não estão formatados…"); (c) " e orienta excluir o link e criar outro" apagado | (a) 1 → 0; (b) 1 → 0; (c) 1 → 0 (novos 1 cada) |
| C-17 | `L1C_estudo.md` 49 e 52 (DÚVIDA 5-a) | APLICADA: "(v2, item 1.4)" → "(item 1.4)"; "(v2, exemplo parlamentar do 1.4)" → "(exemplo parlamentar do 1.4)" | 2 → 0 (novos 2) |
| C-18 | nota de BQ-0003 na edição (`BANCO_itens.md`, `BANCO_gabarito.md`, `SIM-0_folha.md`, `SIM-0_gabarito.md`) | APLICADA: " (D-LEI-15352)" apagado só na exibição; no pacote a nota continua literal | 4 → 0 (novos 4); `D-LEI-15352` no pacote: igual à R0 |
| C-19 | carimbo "aberta(s) hoje": L6A 31 e 188; L6B 142, 163, 170, 175, 187 e 245; `L6B_gabarito.md` 31 (6B-06) | APLICADA: 9 deleções | 9 alvos, cada 1 → 0 (novos 1 cada); `abertas? hoje` na edição 9 → 0 |
| C-20 | códigos do L5 (U1–U6, GG4, TB2) e carimbos "verificado em 8/10/2026" (`L5_estudo.md`, `L5_gabarito.md`) | APLICADA: 6 regras literais + 5 genéricas só para `L5_*`; títulos `Power BI (Microsoft)`, `Tableau (Salesforce)`, `Data Studio (Google)`; A5-14 a A5-17 iguais ao texto exigido | ocorrências de `\b(U[1-6]|GG\d|TB\d|CI)\b` e "erificado em 8/10/2026" em `L5_*.md`: 49 → 0; remoções por tipo: 33 (códigos) + 4 (carimbo) |
| C-21 | classificação interna: L2-Q23 (`L2_gabarito.md`, `SIM-0-P2_gabarito.md`), L3-Q21 (`L3_gabarito.md`), L4-05 (`L4_gabarito.md`) | APLICADA: 3 regras | L2-Q23 2 → 0; L3-Q21 1 → 0; L4-05 1 → 0 (novos 2, 1, 1) |
| C-22 | códigos N do L2 (8 pontos) e do L3 (6 pontos); N1–N4 do L4 ficam | APLICADA: 5 regras genéricas só para `L2_*` e `L3_*` (depois das literais); resultados iguais aos da tabela da reconciliação | 14 alvos, cada 1 → 0; `\bN\d\b` em L1*, L1C*, L2*, L3*, SIM-2*, SIM-0-P2*: 14 → 0 |
| C-23 | `L4_estudo.md` 210 | APLICADA: " neste chat" apagado | 1 → 0 (novo 1) |
| C-24 | pares com `como` ou `b` vazio (L1 1, L2 9, L3 17) e L3 "× ****" | APLICADA: sem " — " quando `como` é vazio e sem " × **…**" quando `b` é vazio | linhas terminadas em " — " 27 → 0; "× ****" 1 → 0; os dois exemplos literais da lista conferidos |
| C-25 | este relatório | APLICADA: R4 (4 rótulos de alvo, seção 3), O-2 (seção 6 e DÚVIDA 1) e esta seção 13; o histórico R0 foi preservado | 4 linhas; 2 trechos; 1 seção |

### 13.3 Resultados dos scripts (saídas gravadas em `s4/t48r1/out/`)

1. **Cada C-xx (texto atual some, texto novo no número previsto):** `conferencias_R1.py` → `conferencias_final.txt`: 118 conferências, 0 falhas (inclui as 8 do C-15, as 3 reuniões, as varreduras e o diff).
2. **Diff R0 → R1 do `pacote.json`:** só `justificativa` de 4C-08, 4C-09, 5C-06, 6B-06, 6B-15 e L2-Q21 (cada uma só deleção; 4C-08 e 5C-06 com 1 troca de caixa) e `pegadinhas` de L1 (20 → 19) e L5 (52 → 48); nas pegadinhas, as demais entradas são idênticas entrada a entrada e a junção com "; " é a entrada reunida. Nenhuma outra diferença (itens, simulados, discursivas, edital, `nota`, `volatil`, `comandoOriginal`, ordem de campos).
3. **`validate.py` (R1):** 103 verificações, 0 falhas (as 102 da R0 com as contagens ajustadas — F4 21, justificativas alteradas 21, padrões da C-09 — mais 1 verificação nova: pegadinhas L1 19, L5 48, total 262, 5 reuniões registradas).
4. **`estudante_fidelidade.py` (R1):** 5631 comparações, 0 diferenças, só com as exceções fechadas: CAIXA do L6A (8 trocas, todas em `L6A_estudo.md`), nota de BQ-0003 (4 exibições) e, no pacote, as 2 trocas de caixa da C-05. Edição = pacote com as deleções da lista ampliada; fora disso, só deleção.
5. **Contagens:** pegadinhas 262 (R0 267); justificativas alteradas da v1.1 para a v1.2 (F4) 21 (R0 18); iguais à R0: itens 286, C/E 149/137, aderência direta/parcial 247/39, `volatil` 23, `nota` 2, `comandoOriginal` 90, simulados `n` 60/40/40/25, pares por lote, discursivas 5, edital 47, arquivos da edição 43.
6. **Varredura de marcas na edição do estudante:** 0 ocorrência de `;)`, ` — $`, `****`, `abertas? hoje`, `(v2,`, `D-LEI-15352`, `neste chat`, `Retificação`, `Gabarito [CE] mantido`, `\b(U[1-6]|GG\d|TB\d|CI)\b`, `\bN\d\b` em L1*, L1C*, L2*, L3*, SIM-2*, SIM-0-P2*, e ` — (BQ|L\d|4C|5C|6A|6B|A5)` nas folhas. Na R0 as ocorrências eram, na ordem: 2, 27, 1, 9, 2, 4, 1, 1, 1, 41, 14 e 165 (ver `conferencias_final.txt`).

**Marcas que restam na edição e por quê:**

| Resto | Onde | Por quê |
|---|---|---|
| `a tecla F4` | `L6A_estudo.md` 83 | tecla de função do Excel, não é código de fonte |
| `O F4 afirma que "generative models …"` | `L4_gabarito.md` 56 (L4-11) | exceção registrada à varredura de códigos F (D-R1-07, opção (a)): "F4" é o sujeito da frase restaurada; apagá-lo quebra a sintaxe e trocá-lo seria reescrita |
| `VOLÁTIL` fora do aviso fixo (7 linhas: `L4_estudo.md` 23 e 210; `L5_estudo.md` 24, 104 e 107; `L6A_estudo.md` 125 e 268) | títulos, rubricas e orientação de estudo | mantido por decisão (2.3-g): orientação de estudo, não marca de processo |
| Etiquetas GI/TC/IC/AT | justificativas dos `*_gabarito.md` | mantidas (2.3-h); legenda como campo opcional de lote vai à errata do contrato (tarefa nova) |
| Códigos N1–N4 do L4 | `L4_estudo.md` 169–217; `L4_gabarito.md` 88, 93, 103; `SIM-1_gabarito.md` | mantidos (2.3-e): definidos no próprio texto ("LGPD (N1, Lei 13.709/2018)") |
| `(Derep (antigo DETAQ); …)` | `L1_estudo.md` | literal pela F5 (D-T12-V12); D-R1-15 DESCARTADO |
| 29 justificativas iniciadas em minúscula depois do prefixo de campo "C — 5.1 —" | `*_gabarito.md` | forma do arquivo canônico, não efeito de deleção (D-R1-18 DESCARTADO) |
| "que eu possa afirmar" | `L3_estudo.md` 422 | texto canônico da GCE; a deleção tornaria a afirmação absoluta (2.3-i, BACKLOG) |
| Remissões a pares por id não exportado ("par C1", "par C14", "C19") | justificativas de A5-09, 5C-03, 5C-07 e 4C-08 (`L4C_gabarito.md`, `L5C_gabarito.md`, `L5_gabarito.md`, `SIM-1_gabarito.md`) | adiado (D-R1-21, BACKLOG) |
| Avisos 1, 2 e 4 da folha canônica do SIM-0 | ausentes das folhas | adiado (D-R1-13): exige campo de contrato; o que se compartilha é do Fundador |
| Nota R2 da D4 repetida na D5; rótulo "Nota: nota de vigência:" | `DISCURSIVAS_padrao.md`; notas do banco | cópia literal decidida na T-27 (D-R1-17); rótulo duplicado entra na tarefa "forma da edição" |
| Quadro-síntese do L1 desalinhado; separador "×" dos pares | `L1_estudo.md`; `*_estudo.md` | BACKLOG (D-R1-14/16) |

### 13.4 Novas contagens da edição do estudante

Remoções por deleção na regeração: **569** (R0: 492). Por tipo novo: códigos do L5 33; códigos N do L2/L3 14; "aberta(s) hoje" 9; caixa 8; classificação interna 4; carimbo "Verificado em 8/10/2026" 4; id de decisão na nota 4; "(v2, …)" 2; "neste chat" 1. Arquivos alterados em relação à R0: 24 de 43 (linhas removidas/inseridas por arquivo):

| Arquivo | linhas R0 alteradas | linhas R1 |
|---|---|---|
| `BANCO_gabarito.md` | 1 | 1 |
| `BANCO_itens.md` | 7 | 7 |
| `L1C_estudo.md` | 2 | 2 |
| `L1_estudo.md` | 3 | 2 |
| `L2_estudo.md` | 16 | 16 |
| `L2_gabarito.md` | 2 | 2 |
| `L3_estudo.md` | 24 | 23 |
| `L3_gabarito.md` | 1 | 1 |
| `L4C_gabarito.md` | 2 | 2 |
| `L4_estudo.md` | 3 | 3 |
| `L4_gabarito.md` | 2 | 2 |
| `L5C_gabarito.md` | 1 | 1 |
| `L5_estudo.md` | 21 | 17 |
| `L5_gabarito.md` | 4 | 4 |
| `L6A_estudo.md` | 13 | 12 |
| `L6B_estudo.md` | 6 | 6 |
| `L6B_gabarito.md` | 1 | 1 |
| `SIM-0-P2_folha.md` | 25 | 25 |
| `SIM-0-P2_gabarito.md` | 1 | 1 |
| `SIM-0_folha.md` | 63 | 63 |
| `SIM-0_gabarito.md` | 1 | 1 |
| `SIM-1_folha.md` | 40 | 40 |
| `SIM-1_gabarito.md` | 1 | 1 |
| `SIM-2_folha.md` | 40 | 40 |

### 13.5 Observações (fora da lista C-01 a C-25; nada foi aplicado)

1. **C-05, texto "atual" do pacote.** A lista cita o fonte ("… curso). Lição O10: o item não depende"); no `pacote.json` R0 a marca já estava apagada (F4 da R0) e o texto era "… curso). o item não depende". A conferência usa o texto R0 do pacote; o resultado coincide com o texto novo da lista.
2. **C-22 e L3 239–240.** Por causa da regra `LEAD + \(N\d\)` (que absorve a quebra de linha antes do parêntese), as duas linhas "… NÃO foram verificados / (N5). A banca …" viram uma só ("… verificados. A banca …"), exatamente como na tabela da reconciliação ("`verificados. A banca`").
3. **Marcas de processo candidatas, fora da lista:** `L4_estudo.md` 59 "(conceito geral, sem fonte de fornecedor neste lote)" e `L6B_estudo.md` 143 ("a especificação previa o item …"). Não aplicado; a GBQ decide se entram numa próxima rodada.
4. **Arquivos do repositório alterados por outro processo durante a rodada:** `regras/pacote_contrato.md` e `saida/pacote/contrato_v1_2_1_2026-10-13.md` têm data posterior ao início desta rodada; não foram tocados por esta correção. `validate.py` leu o contrato e passou (103/103).
5. **`T48_correcao_R1_2026-10-13.md`** (item 3.0.2 da reconciliação): não foi criado nesta rodada, por instrução da tarefa; esta seção 13 e as saídas em `s4/t48r1/out/` cobrem o conteúdo (correção a correção, diff R0 → R1, validadores).
6. **Relatório.** Foi editado no lugar (R4, O-2 e esta seção); as contagens das seções 2, 5, 6, 8, 9, 10 e 11 e o Apêndice A continuam as da R0, por serem histórico, e as da R1 estão acima. O gerador do relatório (`report2.py`) não foi reexecutado.

## Apêndice A — regras literais da edição do estudante (trecho apagado em ⟦ ⟧)

Cada linha: tipo, contexto e trecho apagado; todas verificadas como deleção pura (a especificação é uma subsequência do original) e com pelo menos 1 ocorrência no texto (conferido pelo gerador, que aborta se alguma regra não ocorrer).

| # | Fase | Tipo | Original (contexto) → apagado |
|---|---|---|---|
| 1 | pre | V (parcial: mantém a orientação ao estudante) | antes⏎da versão definitiva [⟦V 08/10/2026 — F4; NORMATIVO — QA; ⟧norma de⏎caráter experimental, não cobrar o texto]. |
| 2 | pre | V (parcial: mantém a orientação ao estudante) | outro⏎idioma [⟦V 08/10/2026 — F4; NORMATIVO — QA; ⟧contexto histórico]. |
| 3 | pre | NORMATIVO — QA (parcial: mantém a orientação ao estudante) | [⟦NORMATIVO — QA; ⟧não cobrar além do texto] |
| 4 | pre | NORMATIVO — QA (frase de marca e fontes) | Todos os dispositivos abaixo estão em paráfrase⟦, com a marca⏎[NORMATIVO — QA]⟧.⟦ Fontes: F1 (LGPD compilada) e F2 (Lei 9.610/1998),⏎lidas em 08/10/2026.⟧ |
| 5 | post | F (prosa: referência a fonte) | valor numérico⟦; o F4 cita a chuva "in inches or millimeters"⟧. |
| 6 | post | F (prosa: referência a fonte) | ). O⟦ F4 afirma que "generative models are initially trained using an unsupervised approach" e que "the model is sometimes trained further using supervised or reinforcement learning"; o⟧ item descreve |
| 7 | post | F (prosa: referência a fonte) | ⟦; o F3 define os termos separadamente⟧ |
| 8 | post | F (frase de fonte) | ⟦ Fonte: F3, conforme o curso 5.1.3.⟧ |
| 9 | post | F (frase de fonte) | ⟦ Fonte: F3, conforme o curso 5.1.1.⟧ |
| 10 | post | F (frase de fonte) | ⟦ Fonte: F1 e F2, conforme o curso 5.1.3.⟧ |
| 11 | post | F (prosa: referência a fonte) | Fonte:⟦ F3 (temperatura) e⟧ curso 5.1.4 (janela de contexto, conceito geral). |
| 12 | post | F (prosa: referência a fonte) | definição de alucinação⟦ do F3⟧). |
| 13 | post | F (prosa: referência a fonte) | Fonte:⟦ F3, zero-shot ("A prompt that does not provide an example of how you want the large language model to respond"), e⟧ curso 5.1.2 e 5.1.3. |
| 14 | post | F (prosa: referência a fonte) | (⟦a F10 informa que ela não é possível; ⟧exclui-se o link e cria-se outro; ver curso 1.4.2) |
| 15 | post | F (prosa: referência a fonte) | conceito geral⟦; a F13 descreve o Outlook para PC como aplicativo de e-mail⟧) |
| 16 | post | F (prosa: referência a fonte) | Fonte: conceito geral⟦; F7 (RFC 1034) descreve os "domain style names" e seu uso para "host address support" (trecho lido em 08/10/2026)⟧. |
| 17 | post | F (prosa: referência a fonte) | Fonte: conceito geral⟦; F11 descreve o HTTP como "a stateless application-level protocol"⟧. |
| 18 | post | F (frase de fonte) | (o de quarta-feira). ⟦Fonte: F12 (Microsoft Learn, "Types of backup", verificado em 08/10/2026): "If you are performing a combination of normal and differential backups, restoring files and folders requires that you have the last normal as well as the last differential backup." ⟧O item não depende |
| 19 | post | F (frase de fonte) | reduz o impacto.⟦ Fonte: F2 (verificado em 08/10/2026).⟧ |
| 20 | post | F (frase de fonte) | pela rede.⟦ Fonte: F13 (worm: "Propaga-se automaticamente pelas redes, explorando vulnerabilidades nos sistemas e aplicativos instalados"; verificado em 08/10/2026) e F4 (vírus, seção 4.1: "se propaga inserindo cópias de si mesmo").⟧ |
| 21 | post | F (frase de fonte) | por regras.⟦ Fonte: F14 (firewall: "protege seu computador contra ataques vindos pela rede"; antivírus: "Ferramentas antivírus (antimalware) podem ajudar a detectar uma infecção"; verificado em 08/10/2026) e F5 (a Firewall do Windows "ajuda a proteger o seu dispositivo ao filtrar o tráfego de rede que entra e sai do dispositivo").⟧ |
| 22 | post | F (prosa: referência a fonte) | Fonte⟦: F13 (spyware: "Projetado para monitorar as atividades de um sistema e enviar as informações coletadas para terceiros."; verificado em 08/10/2026); o antispyware não é mencionado no F13⟧: conceito geral. |
| 23 | post | F (frase de fonte) | código malicioso.⟦ Fonte: F4 (livro, seção 2.3, verificado em 08/10/2026; paráfrase: as mensagens induzem o usuário a fornecer dados por páginas falsas, pela instalação de códigos maliciosos ou pelo preenchimento de formulários; entre as situações, "mensagens com links para código malicioso").⟧ |
| 24 | post | F (prosa: referência a fonte) | Fonte:⟦ F4, seção 2.3.1 (DNS confirmado: "por meio de alterações no serviço de DNS"); F7;⟧ arquivo hosts: conceito geral. |
| 25 | post | F (prosa: referência a fonte) | também podem usar HTTPS. Fonte: ⟦F11, seção 4.2.2 (verificado em 08/10/2026); ⟧o restante é conceito geral. |
| 26 | post | id interno (O-xx) | Curso 4.3.4⟦ (corrigido pela O-3)⟧: |
| 27 | post | F (prosa: referência a fonte) | — as técnicas⟦ de F1 e F2⟧. Se o resumo |
| 28 | post | F (prosa: referência a fonte) | Exemplos⟦ do F4 (reverificados em 7/10/2026)⟧: quantidade de chuva |
| 29 | post | F (prosa: referência a fonte) | Exemplos⟦ do F4⟧: e-mail é spam |
| 30 | post | F (prosa: referência a fonte) | exemplo⟦ do F4⟧: agrupar dados |
| 31 | post | F (prosa: referência a fonte) | POLÍTICA (policy),⟦ que o F4 descreve como⟧ a melhor estratégia para acumular recompensas⟦ (verificado em 7/10/2026)⟧. Exemplos⟦ do F4⟧: treinar robôs |
| 32 | post | F (prosa: referência a fonte) | É o que afirma⟦ o F4⟧: "generative models |
| 33 | post | F (prosa: referência a fonte) | conferido no GAB_DEFINITIVO_034_TRF6_002_01)⟦; o lote usa o F4 como fundamento, não o TRF6⟧. |
| 34 | post | F (prosa: referência a fonte) | ficar com a formulação ⟦do F4 ⟧e evitar itens |
| 35 | post | F (prosa: referência a fonte) | ⟦Segundo o F5 (verificado em 7/10/2026):⏎⟧- Modelo generativo |
| 36 | post | F (prosa: referência a fonte) | Relação entre os termos: ⟦o F3 os define separadamente; ⟧LLMs de uso geral |
| 37 | post | F (prosa: referência a fonte) | a lista em tópicos ⟦do F4 ⟧traz texto→texto |
| 38 | post | F (prosa: referência a fonte) | a tabela de exemplos ⟦do F4 ⟧traz texto→texto |
| 39 | post | F (prosa: referência a fonte) | ver 5.1.4⟦ (F3 para temperatura)⟧. |
| 40 | post | F (prosa: referência a fonte) | ⟦O que a F1 afirma (leitura de 08/10/2026):⏎⟧- Na guia "Revisão" |
| 41 | post | F (prosa: referência a fonte) | Limite do curso:⟦ a F1⟧ NÃO descreve como ativar |
| 42 | post | F (prosa: referência a fonte) | (⟦a F3 ⟧diz "não estão formatados como cabeçalhos" |
| 43 | post | F (prosa: referência a fonte) | apenas visualizar.⟦ A F9 também usa os rótulos "Pode editar" e "Pode exibir".⟧ |
| 44 | post | F (prosa: referência a fonte) | -⟦ A F10 trata de "Interromper o compartilhamento" e de alternar permissões "entre exibir e editar" para quem tem acesso direto; ela ainda avisa que⟧ NÃO é possível |
| 45 | post | F (prosa: referência a fonte) | ERRADO (⟦a F11 ⟧descreve os dois caminhos) |
| 46 | post | F (prosa: referência a fonte) | (conceito geral⟦; F14 para os protocolos⟧) |
| 47 | post | F (prosa: referência a fonte) | é conceito geral⟦; a F13 não usa a palavra "instalado"⟧. |
| 48 | post | F (prosa: referência a fonte) | RFCs DA IETF⟦ E F14⟧) |
| 49 | post | F (prosa: referência a fonte) | ⟦Segundo a F14, ⟧por padrão os clientes POP3 |
| 50 | post | F (prosa: referência a fonte) | ⟦Segundo a F14, ⟧por padrão os clientes IMAP4 |
| 51 | post | F (prosa: referência a fonte) | ⟦A F14 lista ⟧portas e criptografia |
| 52 | post | F (prosa: referência a fonte) | Cco (cópia oculta): ⟦conforme a F12 (leitura de 08/10/2026), ⟧quem é inserido |
| 53 | post | F (prosa: referência a fonte) | Microsoft. ⟦A página da F19 descreve a nova experiência como a que "simplifica as conversas ao colocar o chat, as equipas e os canais num único local" (leitura de 08/10/2026). ⟧Reuniões |
| 54 | post | F (prosa: referência a fonte) | Limite:⟦ a F18⟧ não define o canal padrão |
| 55 | post | F (prosa: referência a fonte) | mais próxima) e⟦ a F19⟧ não diz quem pode ver |
| 56 | post | F (prosa: referência a fonte) | conceito geral⟦; as páginas de ajuda F20–F22 descrevem o uso⟧) |
| 57 | post | F (prosa: referência a fonte) | Google Agenda (⟦a F22, ⟧em pt-PT, chama-o |
| 58 | post | F (frase de fonte) | Fonte: conceito geral.⟦ A leitura de hoje do F4 (Cartilha, livro) menciona confidencialidade e integridade apenas de passagem e associa ataques de negação de serviço a "indisponibilidades ao alvo"; essas passagens NÃO definem a tríade e não foram usadas como definição.⟧ |
| 59 | post | F (prosa: referência a fonte) | "Instale um antivírus antes de qualquer aplicativo"⟦ (F3, verificado em 08/10/2026, seção de celulares)⟧. |
| 60 | post | F (prosa: referência a fonte) | (⟦F11, ⟧RFC 9110, seção 4.2.2: "secured" significa que "the server has been authenticated as acting on behalf of the identified authority" e que a comunicação tem "confidentiality and integrity protection"⟦; verificado em 08/10/2026⟧) |
| 61 | post | F (prosa: referência a fonte) | Fonte:⟦ F11 (seção 4.2.2), verificado em 08/10/2026;⟧ o restante é conceito geral. |
| 62 | post | F (prosa: referência a fonte) | (⟦F4, seção 2.3.1, paráfrase: ⟧desconfiar de site de banco |
| 63 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | seção ITENS REAIS⟦, conferida pela QA em 08/10/2026⟧) |
| 64 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | suprimiu a expressão (⟦conforme a conferência da CQFP; ⟧na |
| 65 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | Lei 15.352/2026⟦, conforme a⏎   CQFP⟧). A autoridade |
| 66 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | — síntese autoral⟦ (GCB-CPP)⟧⏎ |
| 67 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | (artigo e inciso⟦, para o QA Normativo⟧) |
| 68 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | (⟦fonte: Planalto, Lei 15.352/2026 e LGPD compilada, verificadas pela CQFP em 08/10/2026; ⟧vale para a prova, edital 13.33) |
| 69 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | dada pela Lei 15.352/2026⟦, verificada pela CQFP em 08/10/2026⟧ \| Troca |
| 70 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | Não usada em item⟦, por despacho da GCB⟧. |
| 71 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | sem item.⟦ (Síntese da CQFP a partir do texto colado pelo Fundador em 08/10/2026; não é transcrição literal.)⟧ |
| 72 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | visualizations" ⟦(CI, verificado pela CQFP em 8/10/2026) ⟧— exemplo |
| 73 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | cujo ponto de julgamento foi conferido ⟦pela QA ⟧contra o caderno |
| 74 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | (trecho confirmado ⟦pela QA e reconfirmado pela produção ⟧em 08/10/2026) |
| 75 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | Decisão⟦ da GCE⟧: sem trava |
| 76 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | Notas de correção⟦ (GCE, R2–R4)⟧⏎ |
| 77 | post | agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | afirmação⏎    categórica⟦ da versão da CPP⟧, segundo |
| 78 | post | id interno (R-xx, E-xx, O-xx, D-xx) | Alínea c da discursiva⟦ (R4 do Projeto)⟧: |
| 79 | post | id interno (R-xx, E-xx, O-xx, D-xx) | amostras de referência⟦ (errata E1)⟧, não basta |
| 80 | post | id interno (R-xx, E-xx, O-xx, D-xx) | (N1⟦; E3⟧) |
| 81 | post | id interno (R-xx, E-xx, O-xx, D-xx) | Distinção de vocabulário⟦ (O11)⟧: |
| 82 | post | id interno (R-xx, E-xx, O-xx, D-xx) | para o Cargo 11⟦ (D-T2)⟧. |
| 83 | post | carimbo datado de verificação/leitura (ligado a F-ref) | Anthropic, "XML structuring" e OpenAI, "Message formatting with Markdown and XML"⟦, verificadas em 7/10/2026⟧. |
| 84 | post | carimbo datado de verificação/leitura (ligado a F-ref) | "Message formatting with Markdown and XML")⟦, ambas verificadas em 7/10/2026⟧. |
| 85 | post | carimbo datado de verificação/leitura (ligado a F-ref) | reinforcement learning"⟦ (reverificado em 7/10/2026)⟧. Conclusão |
| 86 | post | carimbo datado de verificação/leitura (ligado a F-ref) | "principalmente entre o honesto e o desonesto"⟦ (conferido no Planalto em 08/10/2026)⟧. |
| 87 | post | carimbo datado de verificação/leitura (ligado a F-ref) | Microsoft 365"⟦, conforme a leitura de 08/10/2026⟧) |
| 88 | post | carimbo datado de verificação/leitura (ligado a F-ref) | (seção 1.1⟦; leitura de 08/10/2026⟧) |
| 89 | post | carimbo datado de verificação/leitura (ligado a F-ref) | seus dados"⟦, ambos verificados em 08/10/2026⟧. |

Nota: "n" não é repetido aqui porque as regras da fase "post" casam com o texto já tratado pelas regras genéricas; as ocorrências efetivas de cada tipo estão na seção 10.1.

## Pendências

- QA: a gbq-cqe confere a fidelidade textual das edições do estudante e do pacote às fontes; o QA independente (modelo que não produziu) confere a aplicação das erratas por lote; depois a gbq-gerencia reconcilia e emite o gatilho A da v1.2 (T-48). Nada disso foi feito aqui.
- Nenhum arquivo do repositório fora de `saida/pacote/pacote.json`, `saida/pacote/pacote_relatorio_2026-10-13.md` e `saida/estudante/` foi criado ou alterado; a secretaria deve atualizar o estado.
