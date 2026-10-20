# D5_registro_formato.md — T-74 (ordem DA 20/10/2026) — 2026-10-20 — gerado por gcb-cpp

Reformatação do Lote D5 (Licitações e contratos, item 10 do edital) para o formato da plataforma (FORMATO_PLATAFORMA_DA.md). Só forma; nenhum conteúdo novo. Gerado por `saida/gcb/DA_plataforma/scripts/formatar_D5.py --registro`; fidelidade por `saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D5.py`.

## 1. Fontes e conferências
- Canônico: saida/gcb/D5_v2_1.md, SHA-256 44ddcc982642df66b246108cb7e3ef86031e8a99762aa2262a6c0bdde24e1333 (igual ao esperado 44ddcc98…e1333: o script confere antes de ler e pararia se divergisse).
- Base normativa: saida/gcb/D5_anexo_N_mapa_normativo.md (consulta de 18/10/2026), SHA-256 497af8e63ecc78ba838927191235ebace582d69b4b482598130aa484508d76eb; usado só pelo validador e pelo visual baseLegal (texto copiado letra a letra, `literal: true`, `conferido: 2026-10-18`).
- Seções do canônico NÃO usadas: 0 e 0.1 (resposta ao R1 e registro de acatamento), o parágrafo introdutório da seção 1, o cabeçalho das seções 3 e 4 (contagens de produção), 6 (proveniência), 7 (contagens), 8 (bloco à GCB), as linhas Folha, Ponto de julgamento, Formato, Base, Mecanismo, Troca, Alteração na v2, "Difere de BQ-…" e Marcas de cada item, e a coluna "Código"/"Base" dos pares.
- JSON gerado: D5_plataforma.json, SHA-256 1ab79b5cdb234d7c9cf445cf8ceeae1b95c27d5299c234ca36653919208ac374; tópicos incorporados de D5_topicos_fonte.json, SHA-256 7c42ddf4565c24ea4920c36939eecef94285cfa7693bfcd687a5a28d7e339a66 (escritos à mão).

## 2. Correspondência bloco de origem → ## / ###
| Origem (D5_v2_1.md, seção 1) | Destino no curso |
|---|---|
| PARTE 1.1 — 10.1 Licitação pública: conceito, princípios, finalidade do procedimento licitatório, modalidades, dispensa e inexigibilidade | `## 10.1 LICITAÇÃO PÚBLICA` |
| C10.1-01 Âmbito de aplicação da lei (arts. 1º a 3º) | `### Âmbito de aplicação da lei (arts. 1º a 3º)` |
| C10.1-02 Princípios (art. 5º) | `### Princípios (art. 5º)` |
| C10.1-03 Conceito, finalidade e objetivos do processo licitatório (art. 11) | `### Conceito, finalidade e objetivos do processo licitatório (art. 11)` |
| C10.1-04 Fases do processo de licitação (art. 17) | `### Fases do processo de licitação (art. 17)` |
| C10.1-05 Modalidades (art. 28; arts. 29 a 32; art. 6º, XXXVIII a XLII) | `### Modalidades (art. 28; arts. 29 a 32; art. 6º, XXXVIII a XLII)` |
| C10.1-06 Processo de contratação direta (arts. 72 e 73) | `### Processo de contratação direta (arts. 72 e 73)` |
| C10.1-07 Inexigibilidade (art. 74) | `### Inexigibilidade (art. 74)` |
| C10.1-08 Dispensa de licitação (art. 75) | `### Dispensa de licitação (art. 75)` |
| C10.1-09 Licitação dispensada (art. 76) × licitação dispensável (art. 75) | `### Licitação dispensada (art. 76) × licitação dispensável (art. 75)` |
| C10.1-10 Bens e serviços comuns e especiais; critérios de julgamento (art. 6º, XIII e XIV; arts. 33 e 34) — acréscimo da v2 (leitura externa A1, A2, A4, C1; QA PENDENTE (R2)) | `### Bens e serviços comuns e especiais; critérios de julgamento (art. 6º, XIII e XIV; arts. 33 e 34)` |
| C10.1-11 Impedimentos de participação na licitação e na execução do contrato (art. 14) — acréscimo da v2 (leitura externa B11, C2; QA PENDENTE (R2)) | `### Impedimentos de participação na licitação e na execução do contrato (art. 14)` |
| C10.1-12 Procedimentos auxiliares e credenciamento (art. 28, § 1º; art. 78; art. 6º, XLIII; art. 74, IV) — acréscimo da v2 (leitura externa A3, A7, C2; QA PENDENTE (R2)) | `### Procedimentos auxiliares e credenciamento (art. 28, § 1º; art. 78; art. 6º, XLIII; art. 74, IV)` |
| C10.1-13 Inexigibilidade: artista, notória especialização e imóvel (art. 74, II, III, V e §§ 2º, 3º e 5º) — acréscimo da v2 (leitura externa B5, B6, B7, C3; QA PENDENTE (R2)) | `### Inexigibilidade: artista, notória especialização e imóvel (art. 74, II, III, V e §§ 2º, 3º e 5º)` |
| C10.1-14 Dispensa: licitação anterior e dispensa por valor (art. 75, III, §§ 1º, 2º, 3º e 7º) — acréscimo da v2 (leitura externa A6, B2, B3, B4, C3; QA PENDENTE (R2)) | `### Dispensa: licitação anterior e dispensa por valor (art. 75, III, §§ 1º, 2º, 3º e 7º)` |
| PARTE 1.2 — 10.2 Contratos administrativos | `## 10.2 CONTRATOS ADMINISTRATIVOS` |
| C10.2-01 Regime jurídico do contrato (art. 89) | `### Regime jurídico do contrato (art. 89)` |
| C10.2-02 Cláusulas necessárias (art. 92) [alterado na v2: R1, ponto 16] | `### Cláusulas necessárias (art. 92)` |
| C10.2-03 Garantias (arts. 96 a 102) | `### Garantias (arts. 96 a 102)` |
| C10.2-04 Alocação de riscos e matriz de riscos (art. 103; art. 6º, XXVII) | `### Alocação de riscos e matriz de riscos (art. 103; art. 6º, XXVII)` |
| C10.2-05 Nulidade (arts. 147 a 150) | `### Nulidade (arts. 147 a 150)` |
| C10.2-06 Meios alternativos de prevenção e resolução de controvérsias (arts. 151 a 154) | `### Meios alternativos de prevenção e resolução de controvérsias (arts. 151 a 154)` |
| C10.2-07 Infrações e sanções (arts. 155 e 156) | `### Infrações e sanções (arts. 155 e 156)` |
| C10.2-08 Defesa, processo de responsabilização, prescrição e reabilitação (arts. 157, 158 e 163) — acréscimo da v2 (leitura externa B23, B24, C4; QA PENDENTE (R2)) | `### Defesa, processo de responsabilização, prescrição e reabilitação (arts. 157, 158 e 163)` |
| PARTE 1.3 — 10.3 Características do contrato administrativo | `## 10.3 CARACTERÍSTICAS DO CONTRATO ADMINISTRATIVO` |
| C10.3-01 Prerrogativas da Administração (art. 104) | `### Prerrogativas da Administração (art. 104)` |
| C10.3-02 Duração dos contratos (arts. 105 a 114) | `### Duração dos contratos (arts. 105 a 114)` |
| C10.3-03 Alteração unilateral e por acordo, e seus limites (arts. 124 a 126, 130 a 133) | `### Alteração unilateral e por acordo, e seus limites (arts. 124 a 126, 130 a 133)` |
| C10.3-04 Equilíbrio econômico-financeiro, reajuste e repactuação (art. 124, II, d; arts. 131 a 136; art. 6º, LVIII e LIX) | `### Equilíbrio econômico-financeiro, reajuste e repactuação (art. 124, II, d; arts. 131 a 136; art. 6º, LVIII e LIX)` |
| C10.3-05 Extinção do contrato (arts. 137 a 139) | `### Extinção do contrato (arts. 137 a 139)` |
| C10.3-06 Regimes de execução, contratação integrada e semi-integrada, seguro-garantia com cláusula de retomada (art. 6º, XXXII e XXXIII; arts. 46, 99 e 102) — acréscimo da v2 (leitura externa A15, C5; QA PENDENTE (R2)) | `### Regimes de execução, contratação integrada e semi-integrada, seguro-garantia com cláusula de retomada (art. 6º, XXXII e XXXIII; arts. 46, 99 e 102)` |
| PARTE 1.4 — 10.4 Formalização, gestão e fiscalização do contrato | `## 10.4 FORMALIZAÇÃO, GESTÃO E FISCALIZAÇÃO DO CONTRATO` |
| C10.4-01 Formalização do contrato (arts. 89 a 95) | `### Formalização do contrato (arts. 89 a 95)` |
| C10.4-02 Designação de agentes, gestão por competências e segregação de funções (arts. 7º e 8º) | `### Designação de agentes, gestão por competências e segregação de funções (arts. 7º e 8º)` |
| C10.4-03 Execução do contrato (arts. 115, 116 e 118 a 123) | `### Execução do contrato (arts. 115, 116 e 118 a 123)` |
| C10.4-04 Recebimento do objeto (art. 140) | `### Recebimento do objeto (art. 140)` |
| C10.4-05 Fiscalização como dever geral de acompanhamento (art. 117, caput) e gestor × fiscal | `### Fiscalização como dever geral de acompanhamento (art. 117, caput) e gestor × fiscal` |
| C10.4-06 Convocação dos remanescentes, contrato de urgência e instrumentos substitutivos (art. 90, §§ 2º a 7º; art. 94, § 1º; art. 95, § 1º) — acréscimo da v2 (leitura externa A17, B13, B14, B15, C6; QA PENDENTE (R2)) | `### Convocação dos remanescentes, contrato de urgência e instrumentos substitutivos (art. 90, §§ 2º a 7º; art. 94, § 1º; art. 95, § 1º)` |
| C10.4-07 Reserva de cargos, medidas trabalhistas e subcontratação (art. 116; art. 121, §§ 3º e 4º; art. 122) — acréscimo da v2 (leitura externa B16, B17, B18, C7; QA PENDENTE (R2)) | `### Reserva de cargos, medidas trabalhistas e subcontratação (art. 116; art. 121, §§ 3º e 4º; art. 122)` |
| C10.4-08 Pagamentos: ordem cronológica, parcela incontroversa e pagamento antecipado (arts. 141, 143 e 145) — acréscimo da v2 (leitura externa B20, B21, B22, C7; QA PENDENTE (R2)) | `### Pagamentos: ordem cronológica, parcela incontroversa e pagamento antecipado (arts. 141, 143 e 145)` |
| C10.4-09 Ensaios, testes e provas no recebimento do objeto (art. 140, § 4º) — acréscimo da v2 (leitura externa B19; QA PENDENTE (R2)) | `### Ensaios, testes e provas no recebimento do objeto (art. 140, § 4º)` |
| PARTE 1.5 — 10.5 Planejamento e fiscalização contratual | `## 10.5 PLANEJAMENTO E FISCALIZAÇÃO CONTRATUAL` |
| C10.5-01 Planejamento como princípio e governança das contratações (art. 5º; art. 11, parágrafo único) | `### Planejamento como princípio e governança das contratações (art. 5º; art. 11, parágrafo único)` |
| C10.5-02 Plano de contratações anual (art. 12, VII e § 1º) | `### Plano de contratações anual (art. 12, VII e § 1º)` |
| C10.5-03 Fase preparatória (art. 18, caput e incisos) | `### Fase preparatória (art. 18, caput e incisos)` |
| C10.5-04 Planejamento de compras (art. 40, caput e incisos) | `### Planejamento de compras (art. 40, caput e incisos)` |
| C10.5-05 Modelo de gestão do contrato como peça do planejamento (art. 6º, XXIII, f; art. 92, XVIII) | `### Modelo de gestão do contrato como peça do planejamento (art. 6º, XXIII, f; art. 92, XVIII)` |
| C10.5-06 Gestão de riscos e linhas de defesa (art. 169) | `### Gestão de riscos e linhas de defesa (art. 169)` |
| C10.5-07 Estimativa de valor, sigilo do orçamento e licitações de serviços (art. 23; art. 24; art. 47) — acréscimo da v2 (leitura externa B9, B27, A14, C8; QA PENDENTE (R2)) | `### Estimativa de valor, sigilo do orçamento e licitações de serviços (art. 23; art. 24; art. 47)` |
| PARTE 1.6 — 10.6 Papel do fiscalizador do contrato | `## 10.6 PAPEL DO FISCALIZADOR DO CONTRATO` |
| C10.6-01 Designação do fiscal: requisitos e segregação de funções (art. 7º; art. 117, caput) | `### Designação do fiscal: requisitos e segregação de funções (art. 7º; art. 117, caput)` |
| C10.6-02 Atribuições do fiscal: registro e determinação de providências (art. 117, § 1º) | `### Atribuições do fiscal: registro e determinação de providências (art. 117, § 1º)` |
| C10.6-03 Apoio dos órgãos de assessoramento jurídico e de controle interno (art. 117, § 3º; art. 8º, § 3º) | `### Apoio dos órgãos de assessoramento jurídico e de controle interno (art. 117, § 3º; art. 8º, § 3º)` |
| C10.6-04 Terceiros contratados para assistir o fiscal e responsabilidade (art. 117, caput e § 4º) | `### Terceiros contratados para assistir o fiscal e responsabilidade (art. 117, caput e § 4º)` |
| C10.6-05 Recebimento provisório pelo responsável pelo acompanhamento e fiscalização (art. 140, I, a, e II, a) | `### Recebimento provisório pelo responsável pelo acompanhamento e fiscalização (art. 140, I, a, e II, a)` |
| C10.6-06 Prerrogativa de fiscalizar e efeitos da fiscalização (art. 104, III; art. 137, caput e II; art. 120) [alterado na v2: base do D5-71] | `### Prerrogativa de fiscalizar e efeitos da fiscalização (art. 104, III; art. 137, caput e II; art. 120)` |
| C10.6-07 Dever de informar os superiores (art. 117, § 2º) — acréscimo da v2 (leitura externa B1, C9; QA PENDENTE (R2)) | `### Dever de informar os superiores (art. 117, § 2º)` |
| PARTE 1.7 — 10.7 Estudo Técnico Preliminar e Termo de Referência | `## 10.7 ESTUDO TÉCNICO PRELIMINAR E TERMO DE REFERÊNCIA` |
| C10.7-01 Estudo técnico preliminar (art. 6º, XX; art. 18, I) | `### Estudo técnico preliminar (art. 6º, XX; art. 18, I)` |
| C10.7-02 Elementos do ETP (art. 18, § 1º) e elementos obrigatórios × justificáveis (art. 18, § 2º) | `### Elementos do ETP (art. 18, § 1º) e elementos obrigatórios × justificáveis (art. 18, § 2º)` |
| C10.7-03 Termo de referência: definição e alíneas (art. 6º, XXIII, a a j) | `### Termo de referência: definição e alíneas (art. 6º, XXIII, a a j)` |
| C10.7-04 Conteúdo do termo de referência em compras (art. 40, § 1º, e § 4º) | `### Conteúdo do termo de referência em compras (art. 40, § 1º, e § 4º)` |
| C10.7-05 Anteprojeto, projeto básico e projeto executivo (art. 6º, XXIV a XXVI; art. 18, § 3º) [alterado na v2: R1, ponto 14] | `### Anteprojeto, projeto básico e projeto executivo (art. 6º, XXIV a XXVI; art. 18, § 3º)` |
| C10.7-06 Plano de contratações anual × ETP × TR na sequência do planejamento | `### Plano de contratações anual × ETP × TR na sequência do planejamento` |
| C10.7-07 Compra ou locação no ETP e providências prévias (art. 44; art. 18, § 1º, V e X) — acréscimo da v2 (leitura externa B25, B26, C10; QA PENDENTE (R2)) | `### Compra ou locação no ETP e providências prévias (art. 44; art. 18, § 1º, V e X)` |

Regras gerais do curso: "- Definição:" → quadro DEFINIÇÃO (em lista, sem linha em branco, quando a definição tem 3 ou mais frases: operação 4; em parágrafo único nos demais casos); quadro BASE LEGAL em lista com os dispositivos que o próprio título do bloco cita entre parênteses ("(art. 28; arts. 29 a 32; art. 6º, XXXVIII a XLII)" → três linhas "- Lei 14.133/2021, art. 28" etc.; no bloco sem parêntese de artigo no título, C10.7-06, os dispositivos da lista "[Desfeita por: …]"); "- Exemplo (Legislativo, hipotético):" → EXEMPLO PARLAMENTAR (o canônico já termina cada exemplo com "O exemplo é hipotético." ou equivalente: mantido); "- Pegadinha provável: … [Desfeita por: X]" → PEGADINHA PROVÁVEL com "Base: X". Código de bloco ("C10.x-NN ") removido do título. Títulos `##`: texto do edital em maiúsculas (P1-DA-10.1 cortado no primeiro ":" por passar de 90 caracteres). Resumo: seção 2 inteira. Pares: seção 3, 31; `a`/`b` = termos do campo "Par" (a = primeiro; b = demais unidos por " × ", caso do P-14); `como` = coluna Diferença + " Como a banca troca: " + coluna "Como a banca troca"; a coluna Base não entra. Pegadinhas: seção 4, 73, sem número, sem código do bloco e sem marca de versão; " — Dispositivo: X" vira " Base: X"; `itemEdital` pelo bloco ([C10.x-NN] → P1-DA-10.x).

## 3. Deleções e trocas (cada uma registrada)
Tipos: deleção de marca (v2, R1/R2, QA PENDENTE, leitura externa, Anexo N, REVERIFICAR, códigos); deleção de frase inteira ou de oração (processo, "[SEM FONTE]", cobertura do lote, cruzamento com item real do banco); troca mínima (op. 6); troca de rótulo (operação 2).

Contagem por tipo: deleção de frase inteira: 11; deleção de marca: 60; deleção de oração de processo: 12; pontuação (nenhuma palavra alterada): 1; troca de rótulo: 131; troca mínima (op. 6): 7.

1. [curso C10.1-03 (definição)] deleção de marca: `(nota do Anexo N, seção 7, item 11)` → (nada). Motivo: referência ao Anexo N e à sua seção (seção 6); fica "Conceito e finalidade: o art. 6º não traz definição isolada…".
2. [curso C10.1-08 (definição)] deleção de oração de processo: `; aqui, os cobrados no lote` → (nada). Motivo: fala do lote (cobertura de itens, cruzamento com item do banco ou nota de produção); não é conteúdo para a candidata (seção 6); fica "(rol de incisos)".
3. [curso C10.1-08 (definição)] deleção de oração de processo: `; os valores atualizados em vigor em 2/10/2026 estão NÃO CONFERIDOS no Anexo N: [SEM FONTE — não afirmar]` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); a oração também cita o Anexo N ("NÃO CONFERIDOS no Anexo N"); ficam o que a lei fixa em reais e a regra de atualização do art. 182.
4. [curso C10.1-08 (definição)] deleção de marca: `REVERIFICAR: o art. 75, XVI` → `O art. 75, XVI`. Motivo: marca REVERIFICAR (seção 6); a letra minúscula inicial passa a maiúscula; o conteúdo do inciso XVI é mantido.
5. [curso C10.1-08 (definição)] deleção de frase inteira: `Nenhum item deste lote se apoia nesse inciso.` → (nada). Motivo: fala do lote (cobertura de itens, cruzamento com item do banco ou nota de produção); não é conteúdo para a candidata (seção 6).
6. [curso C10.1-08 (pegadinha)] deleção de oração de processo: `; afirmar valor atualizado sem conferência` → (nada). Motivo: a oração só faz sentido com a frase "[SEM FONTE — não afirmar]" sobre os valores atualizados, que a seção 6 manda tirar; sem ela a pegadinha ficaria sem objeto (registrada também na lista consolidada, pegadinha 8).
7. [curso C10.1-10 (título)] deleção de marca: `— acréscimo da v2 (leitura externa A1, A2, A4, C1; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa", código de item).
8. [curso C10.1-10 (definição)] deleção de oração de processo: `e não é desenvolvido neste lote (ver o registro de acatamento, seção 0.1)` → (nada). Motivo: fala do lote (cobertura de itens, cruzamento com item do banco ou nota de produção); não é conteúdo para a candidata (seção 6); cita "lote" e a seção 0.1 do canônico; fica "O modo de disputa (aberto ou fechado) pertence à fase de propostas e lances.".
9. [curso C10.1-11 (título)] deleção de marca: `— acréscimo da v2 (leitura externa B11, C2; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa", código de item).
10. [curso C10.1-12 (título)] deleção de marca: `— acréscimo da v2 (leitura externa A3, A7, C2; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa", código de item).
11. [curso C10.1-12 (definição)] deleção de frase inteira: `O art. 79, que trata das hipóteses de uso do credenciamento, tem o inciso IV, o § 1º (caput e inciso VII, com as alíneas) e o § 2º com redação dada ou incluída pela Lei 15.266/2025, marcados REVERIFICAR no Anexo N; o artigo não é usado neste lote.` → (nada). Motivo: frase só de processo: marca REVERIFICAR, "Anexo N" e "lote" (seção 6); sobre artigo que o próprio texto diz não usar.
12. [curso C10.1-13 (título)] deleção de marca: `— acréscimo da v2 (leitura externa B5, B6, B7, C3; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa", código de item).
13. [curso C10.1-13 (definição)] deleção de frase inteira: `(O inciso I e o § 1º, fornecedor exclusivo e documento idôneo, são ponto do item real BQ-0113 e não são repetidos em item; o inciso III e o § 4º estão em C10.1-07.)` → (nada). Motivo: fala do lote (cobertura de itens, cruzamento com item do banco ou nota de produção); não é conteúdo para a candidata (seção 6); cita item do banco (BQ-0113) e código de bloco (C10.1-07).
14. [curso C10.1-14 (título)] deleção de marca: `— acréscimo da v2 (leitura externa A6, B2, B3, B4, C3; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa", código de item).
15. [curso C10.1-14 (definição)] deleção de marca: `(usados em C10.1-08)` → (nada). Motivo: remissão a código de bloco do curso (seção 6).
16. [curso C10.1-14 (definição)] deleção de oração de processo: `; valor atualizado NÃO CONFERIDO no Anexo N: [SEM FONTE — não afirmar]` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); a oração também cita o Anexo N; fica "(sujeito à atualização do art. 182)".
17. [curso C10.2-02 (título)] deleção de marca: `[alterado na v2: R1, ponto 16]` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa", código de item).
18. [curso C10.2-08 (título)] deleção de marca: `— acréscimo da v2 (leitura externa B23, B24, C4; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa", código de item).
19. [curso C10.3-06 (título)] deleção de marca: `— acréscimo da v2 (leitura externa A15, C5; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa", código de item).
20. [curso C10.4-01 (definição)] deleção de oração de processo: `; valor atualizado NÃO CONFERIDO no Anexo N` → (nada). Motivo: cita "Anexo N" (seção 6) e é a mesma ressalva "NÃO CONFERIDO" (sem fonte); fica "(a Lei 14.133 fixa o valor-limite em reais, sujeito à atualização do art. 182)".
21. [curso C10.4-05 (definição)] deleção de frase inteira: `Qualquer afirmação sobre atribuições do gestor vem de regulamento não aberto neste Anexo: [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); a frase também cita o Anexo.
22. [curso C10.4-06 (título)] deleção de marca: `— acréscimo da v2 (leitura externa A17, B13, B14, B15, C6; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa", código de item).
23. [curso C10.4-07 (título)] deleção de marca: `— acréscimo da v2 (leitura externa B16, B17, B18, C7; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa", código de item).
24. [curso C10.4-07 (definição)] deleção de frase inteira: `(A regra e a ressalva do art. 121, §§ 1º e 2º, estão em C10.4-03.)` → (nada). Motivo: remissão a código de bloco do curso (seção 6).
25. [curso C10.4-08 (título)] deleção de marca: `— acréscimo da v2 (leitura externa B20, B21, B22, C7; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa", código de item).
26. [curso C10.4-09 (título)] deleção de marca: `— acréscimo da v2 (leitura externa B19; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa", código de item).
27. [curso C10.4-09 (definição)] deleção de frase inteira: `(O recebimento provisório e definitivo, a rejeição do objeto e a responsabilidade pela solidez e segurança estão em C10.4-04.)` → (nada). Motivo: remissão a código de bloco do curso (seção 6).
28. [curso C10.5-07 (título)] deleção de marca: `— acréscimo da v2 (leitura externa B9, B27, A14, C8; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa", código de item).
29. [curso C10.5-07 (definição)] deleção de frase inteira: `(O planejamento de compras está em C10.5-04.)` → (nada). Motivo: remissão a código de bloco do curso (seção 6).
30. [curso C10.6-02 (definição)] deleção de oração de processo: `, que já é objeto de item real do banco (BQ-0134) e não é repetido neste lote` → (nada). Motivo: fala do lote (cobertura de itens, cruzamento com item do banco ou nota de produção); não é conteúdo para a candidata (seção 6); fica "está no § 2º.".
31. [curso C10.6-04 (definição)] deleção de frase inteira: `(ponto do item real BQ-0135, não repetido)` → (nada). Motivo: fala do lote (cobertura de itens, cruzamento com item do banco ou nota de produção); não é conteúdo para a candidata (seção 6); cita item do banco (BQ-0135).
32. [curso C10.6-06 (título)] deleção de marca: `[alterado na v2: base do D5-71]` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa", código de item).
33. [curso C10.6-07 (título)] deleção de marca: `— acréscimo da v2 (leitura externa B1, C9; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa", código de item).
34. [curso C10.6-07 (definição)] deleção de frase inteira: `Este é o ponto do item real BQ-0134, que não é repetido em item deste lote; entra no curso e nas pegadinhas para completar o quadro das atribuições do fiscal (§ 1º em C10.6-02, § 3º em C10.6-03, § 4º em C10.6-04).` → (nada). Motivo: fala do lote (cobertura de itens, cruzamento com item do banco ou nota de produção); não é conteúdo para a candidata (seção 6); cita item do banco (BQ-0134) e códigos de bloco.
35. [curso C10.7-02 (definição)] deleção de frase inteira: `(Requisitos da contratação e parcelamento, incisos III e VIII, são o ponto do item real BQ-0142.)` → (nada). Motivo: fala do lote (cobertura de itens, cruzamento com item do banco ou nota de produção); não é conteúdo para a candidata (seção 6); cita item do banco (BQ-0142).
36. [curso C10.7-05 (título)] deleção de marca: `[alterado na v2: R1, ponto 14]` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa", código de item).
37. [curso C10.7-05 (definição)] deleção de oração de processo: `; qualquer afirmação além da letra desses dispositivos fica fora do lote` → (nada). Motivo: fala do lote (cobertura de itens, cruzamento com item do banco ou nota de produção); não é conteúdo para a candidata (seção 6); fica "A lei não restringe, no art. 6º, XXV, o projeto básico a uma categoria de objeto (fala em 'a obra ou o serviço').".
38. [curso C10.7-07 (título)] deleção de marca: `— acréscimo da v2 (leitura externa B25, B26, C10; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa", código de item).
39. [resumo] deleção de marca: `Acrescentado na v2: bens e serviços comuns (padrão …` → `Bens e serviços comuns (padrão …`. Motivo: marca "v2" (seção 6): sai "Acrescentado na v2:" e a letra minúscula inicial passa a maiúscula; o texto que segue é mantido.
40. [resumo] deleção de marca: `Acrescentado na v2: defesa em 15 dias úteis na mult…` → `Defesa em 15 dias úteis na mult…`. Motivo: marca "v2" (seção 6): sai "Acrescentado na v2:" e a letra minúscula inicial passa a maiúscula; o texto que segue é mantido.
41. [resumo] deleção de marca: `Acrescentado na v2: regimes de execução de obras e …` → `Regimes de execução de obras e …`. Motivo: marca "v2" (seção 6): sai "Acrescentado na v2:" e a letra minúscula inicial passa a maiúscula; o texto que segue é mantido.
42. [resumo] deleção de marca: `Acrescentado na v2: convocação dos licitantes reman…` → `Convocação dos licitantes reman…`. Motivo: marca "v2" (seção 6): sai "Acrescentado na v2:" e a letra minúscula inicial passa a maiúscula; o texto que segue é mantido.
43. [resumo] deleção de marca: `Acrescentado na v2: estimativa de valor compatível …` → `Estimativa de valor compatível …`. Motivo: marca "v2" (seção 6): sai "Acrescentado na v2:" e a letra minúscula inicial passa a maiúscula; o texto que segue é mantido.
44. [resumo] deleção de marca: `Acrescentado na v2: o fiscal informa os superiores,…` → `O fiscal informa os superiores,…`. Motivo: marca "v2" (seção 6): sai "Acrescentado na v2:" e a letra minúscula inicial passa a maiúscula; o texto que segue é mantido.
45. [resumo] deleção de marca: `Acrescentado na v2: compra ou locação de bens: o ET…` → `Compra ou locação de bens: o ET…`. Motivo: marca "v2" (seção 6): sai "Acrescentado na v2:" e a letra minúscula inicial passa a maiúscula; o texto que segue é mantido.
46. [resumo] deleção de oração de processo: `; só no curso, no par P-27 e na pegadinha G-71, sem item` → (nada). Motivo: remissão a códigos de par (P-27) e de pegadinha (G-71) e fala de cobertura de itens (seção 6).
47. [resumo] deleção de marca: `| Número literal do Anexo N | Dispositivo |` → `| Número literal | Dispositivo |`. Motivo: sai "do Anexo N" do cabeçalho da tabela (seção 6); a tabela é mantida.
48. [resumo] deleção de oração de processo: `; os valores vigentes em 2/10/2026 estão NÃO CONFERIDOS no Anexo N: [SEM FONTE — não afirmar]` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); a oração também cita o Anexo N; fica "Valores em reais: a Lei 14.133 fixa valores-limite (art. 75, I e II e § 7º; art. 95, § 2º), atualizados a cada 1º de janeiro pelo Poder Executivo federal (art. 182).".
49. [par P-08] deleção de oração de processo: `; atribuições do gestor: [SEM FONTE — não afirmar]` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
50. [par P-27] deleção de frase inteira: `(O § 2º é o ponto do item real BQ-0134; este par não gera item.)` → (nada). Motivo: fala do lote (cobertura de itens, cruzamento com item do banco ou nota de produção); não é conteúdo para a candidata (seção 6); cita item do banco (BQ-0134).
51. [pegadinha 8] deleção de oração de processo: `; afirmar valor atualizado sem conferência` → (nada). Motivo: ver a mesma edição no bloco do curso (a oração dependia da frase "[SEM FONTE — não afirmar]").
52. [pegadinha 11] deleção de marca: `[alterada na v2]` → (nada). Motivo: marca "v2" (seção 6).
53. [pegadinha 38] deleção de marca: `[alterada na v2]` → (nada). Motivo: marca "v2" (seção 6).
54. [pegadinha 43] deleção de marca: `[alterada na v2]` → (nada). Motivo: marca "v2" (seção 6).
55. [pegadinha 45] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
56. [pegadinha 46] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
57. [pegadinha 47] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
58. [pegadinha 48] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
59. [pegadinha 49] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
60. [pegadinha 50] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
61. [pegadinha 51] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
62. [pegadinha 52] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
63. [pegadinha 53] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
64. [pegadinha 54] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
65. [pegadinha 55] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
66. [pegadinha 56] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
67. [pegadinha 57] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
68. [pegadinha 58] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
69. [pegadinha 59] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
70. [pegadinha 60] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
71. [pegadinha 61] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
72. [pegadinha 62] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
73. [pegadinha 63] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
74. [pegadinha 64] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
75. [pegadinha 65] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
76. [pegadinha 66] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
77. [pegadinha 67] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
78. [pegadinha 68] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
79. [pegadinha 69] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
80. [pegadinha 70] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
81. [pegadinha 71] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
82. [pegadinha 72] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
83. [pegadinha 73] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
84. [justificativa D5-04] pontuação (nenhuma palavra alterada): `Não há troca: o item` → `Não há troca; o item`. Motivo: a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula (mesmo tratamento dado no D1, item D1-01).
85. [justificativa D5-10] troca mínima (op. 6): `elemento-isca:` → `elemento que parece trocado:`. Motivo: "elemento-isca" é marca de produção (seção 6); trocado pela expressão equivalente "elemento que parece trocado" (o canônico define o elemento-isca como o que a candidata tende a achar trocado); o restante da frase fica igual.
86. [justificativa D5-18] troca mínima (op. 6): `elemento-isca:` → `elemento que parece trocado:`. Motivo: "elemento-isca" é marca de produção (seção 6); trocado pela expressão equivalente "elemento que parece trocado" (o canônico define o elemento-isca como o que a candidata tende a achar trocado); o restante da frase fica igual.
87. [justificativa D5-23] troca mínima (op. 6): `elemento-isca:` → `elemento que parece trocado:`. Motivo: "elemento-isca" é marca de produção (seção 6); trocado pela expressão equivalente "elemento que parece trocado" (o canônico define o elemento-isca como o que a candidata tende a achar trocado); o restante da frase fica igual.
88. [justificativa D5-36] troca mínima (op. 6): `elemento-isca:` → `elemento que parece trocado:`. Motivo: "elemento-isca" é marca de produção (seção 6); trocado pela expressão equivalente "elemento que parece trocado" (o canônico define o elemento-isca como o que a candidata tende a achar trocado); o restante da frase fica igual.
89. [justificativa D5-42] troca mínima (op. 6): `elemento-isca:` → `elemento que parece trocado:`. Motivo: "elemento-isca" é marca de produção (seção 6); trocado pela expressão equivalente "elemento que parece trocado" (o canônico define o elemento-isca como o que a candidata tende a achar trocado); o restante da frase fica igual.
90. [justificativa D5-52] troca mínima (op. 6): `elemento-isca:` → `elemento que parece trocado:`. Motivo: "elemento-isca" é marca de produção (seção 6); trocado pela expressão equivalente "elemento que parece trocado" (o canônico define o elemento-isca como o que a candidata tende a achar trocado); o restante da frase fica igual.
91. [justificativa D5-68] troca mínima (op. 6): `elemento-isca:` → `elemento que parece trocado:`. Motivo: "elemento-isca" é marca de produção (seção 6); trocado pela expressão equivalente "elemento que parece trocado" (o canônico define o elemento-isca como o que a candidata tende a achar trocado); o restante da frase fica igual.

Trocas de rótulo (operação 2): 58 pegadinhas do curso ("[Desfeita por: X]" → "Base: X") e 73 pegadinhas da lista consolidada (" — Dispositivo: X" → " Base: X").

Decisões de leitura que o orquestrador pode querer revisar (nenhuma altera conteúdo normativo):
- Valores em reais: o curso mantém o que a lei fixa (R$ 100.000,00 e R$ 50.000,00 no art. 75, I e II) e a regra de atualização do art. 182; saíram as orações "valor atualizado NÃO CONFERIDO … [SEM FONTE]". A pegadinha "afirmar valor atualizado sem conferência" (curso C10.1-08 e pegadinha 8) saiu pelo mesmo motivo.
- Marca REVERIFICAR em C10.1-08 (art. 75, XVI, redação da Lei 15.471/2026): a marca saiu e o conteúdo do inciso foi mantido, como o D6 fez com a Lei 15.141/2025. A frase sobre o art. 79 (C10.1-12), toda de marca e de cobertura, saiu inteira.
- Remissões "folha 10.6" e "folha 10.7" (C10.4-05, C10.5-03, C10.5-04) foram mantidas: "folha" não está na lista da seção 6 e os números 10.6 e 10.7 são os dos títulos `##` do curso. As remissões a código de bloco (C10.x-NN) saíram.
- Enunciados começam com "Considere…" e trazem a situação no próprio enunciado; o canônico não separa texto-base: `textoBase` "" e `comando` "Julgue o item a seguir." (o canônico só traz "Julgue cada item como Certo ou Errado." no cabeçalho da seção 5.1).
- Ordem dos itens no JSON: crescente pelo id (D5-01 a D5-53, D5-55 a D5-71), como pede a seção 4 da especificação; no canônico o D5-71 ocupa a posição 54.

## 4. Itens
- Total 70; C 35 / E 35.
- Por itemEdital: P1-DA-10.1: 10; P1-DA-10.2: 10; P1-DA-10.3: 10; P1-DA-10.4: 10; P1-DA-10.5: 10; P1-DA-10.6: 10; P1-DA-10.7: 10.
- volatil true: nenhum (todas as linhas "Marcas:" trazem REVERIFICAR=não e VOLÁTIL=não; coerente com a seção 7 do canônico).
- Justificativa: linhas 1 e 2 unidas por um espaço; edições: a pontuação de D5-04 ("Não há troca:" → "Não há troca;") e a troca mínima "elemento-isca:" → "elemento que parece trocado:" em 7 itens (D5-10, D5-18, D5-23, D5-36, D5-42, D5-52, D5-68); as demais 62 são idênticas às duas linhas. As linhas "Difere de BQ-…" e "Mecanismo" são campos à parte no canônico e não entram.
- Pares: 31; pegadinhas: 73 (P1-DA-10.1: 18; P1-DA-10.2: 10; P1-DA-10.3: 6; P1-DA-10.4: 15; P1-DA-10.5: 9; P1-DA-10.6: 7; P1-DA-10.7: 8); tópicos: 7 (P1-DA-10.1, P1-DA-10.2, P1-DA-10.3, P1-DA-10.4, P1-DA-10.5, P1-DA-10.6, P1-DA-10.7).

## 5. Saída do validador
Comando: `python3 -I saida/gcb/DA_plataforma/scripts/validar_da.py saida/gcb/DA_plataforma/D5_plataforma.json saida/gcb/D5_v2_1.md saida/gcb/D5_anexo_N_mapa_normativo.md`
```
D5_plataforma.json: lote D5; itensEdital 7; blocos ## 7; itens 70 (C 35 / E 35); pares 31; pegadinhas 73; topicos 7
quadros: {'PEGADINHA PROVÁVEL': 58, 'EXEMPLO PARLAMENTAR': 58, 'DEFINIÇÃO': 58, 'BASE LEGAL': 58}
RESULTADO: 0 FALHA, 0 AVISO
```

## 6. Conferência de fidelidade
Comando: `python3 -I saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D5.py`

### 6.1 Curso: palavras do bloco de saída × bloco de origem (58 blocos)

Origem = título (sem o código C10.x-NN e sem a marca de versão) + definição + exemplo + pegadinha, sem os rótulos "Definição:", "Exemplo (Legislativo, hipotético):", "Pegadinha provável:", "[Desfeita por:" e sem as passagens registradas. Saída = título + texto dos três quadros, sem os rótulos de quadro e sem a lista BASE LEGAL. Contagem de palavras por multiconjunto (maiúsculas ignoradas) e por sequência (difflib). Única palavra acrescentada permitida: "Base" (no lugar de "[Desfeita por:").

- C10.1-01: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.1-02: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.1-03: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.1-04: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.1-05: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.1-06: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.1-07: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.1-08: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.1-09: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.1-10: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.1-11: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.1-12: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.1-13: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.1-14: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.2-01: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.2-02: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.2-03: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.2-04: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.2-05: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.2-06: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.2-07: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.2-08: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.3-01: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.3-02: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.3-03: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.3-04: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.3-05: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.3-06: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.4-01: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.4-02: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.4-03: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.4-04: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.4-05: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.4-06: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.4-07: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.4-08: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.4-09: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.5-01: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.5-02: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.5-03: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.5-04: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.5-05: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.5-06: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.5-07: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.6-01: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.6-02: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.6-03: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.6-04: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.6-05: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.6-06: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.6-07: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.7-01: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.7-02: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.7-03: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.7-04: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.7-05: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.7-06: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0
- C10.7-07: palavras acrescentadas fora de "Base" 0; "Base" acrescentada 1; suprimidas 0; operações de inserção/troca/remoção na sequência 1; palavras de BASE LEGAL fora do vocabulário do bloco 0

Total curso: palavras acrescentadas (fora de "Base") 0; suprimidas 0; blocos com divergência 0.

### 6.2 Resumo (seção 2)

- Acrescentadas {}; suprimidas {}; operações na sequência 0. Esperado: nenhuma (só deleções registradas; a letra minúscula após "Acrescentado na v2:" passa a maiúscula, o que não muda a palavra).

### 6.3 Pares (31)

Origem = campos "Par", "Diferença" e "Como a banca troca" (sem as passagens registradas); saída = a + b + como. Palavras permitidas por construção: as do rótulo " Como a banca troca: " da especificação.

- Pares com palavra acrescentada fora do rótulo permitido, ou suprimida: 0. Termos a/b reconstituem o campo "Par" (a + " × " + b).

### 6.4 Pegadinhas (73)

- Pegadinhas com palavra acrescentada além de "Base", ou suprimida, ou com itemEdital divergente do bloco: 0. (Só "Base:" foi acrescentada, no lugar do rótulo " — Dispositivo: ".)

### 6.5 Itens (70): enunciado, gabarito, itemEdital e justificativa

- Trocas mínimas "elemento-isca" → "elemento que parece trocado" nas justificativas de origem: 7 (esperado: 7).
- Itens com enunciado, gabarito ou itemEdital diferente do canônico, ou justificativa com palavra acrescentada ou suprimida: 0. (Enunciado e gabarito: iguais caractere a caractere; justificativa: a pontuação de D5-04, que não altera palavra, e a troca registrada de "elemento-isca".)

### 6.6 Tópicos (7)

- Problemas nos tópicos (número ausente do curso da folha; dispositivo de baseLegal que não bate letra a letra com o mapa, sem data 2026-10-18 ou fora do curso): 0.

RESULTADO DA CONFERÊNCIA DE FIDELIDADE: 0 defeito(s).

