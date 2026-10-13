# T44_T46_reconciliacao_2026-10-13.md — T-44 e T-46 — 2026-10-13 — gerado por gce-gerencia

Objeto: reconciliação e decisão D1 da GCE sobre a T-44 (errata de forma do Lote 3, D-L3-ERRATA-FORMA, + conferência das erratas D1 G1/G2) e a T-46 (Adendo 5, errata E12, D-E12-L1).
Entradas: produção saida/gce/lote3_errata2_2026-10-13.md e saida/gce/lote1_adendo5_2026-10-13.md (gce-cpp); QA saida/gce/QA_T44_T46_2026-10-13_gce-cqfp.md (gce-cqfp, APROVADO COM RESSALVAS; 0 itens reprovados).
Decisões consideradas: D-L3-ERRATA-FORMA, D-E12-L1, D-T12-V12, D-TRANSPORTE-B, D-TRANSPORTE-FUNDADOR.
Nenhum item, gabarito, fonte, [TS] de item, VOLÁTIL de item ou marca [V] alterado nesta reconciliação.

## 1. Reconciliação

| Objeto | Produção | QA (gce-cqfp) | Reconciliação GCE |
|---|---|---|---|
| T-44 (1) título e nota do curso 3.1 (L3) | 3 operações (tabela +6 linhas; título; nota) | APROVADO COM RESSALVA (achado 3) | Aceito; ressalva resolvida (seção 2) |
| T-44 (2) G1-a, G1-b, G1-c (L3) e G2 (L2) | — (erratas D1 de 10/10) | CONFERIDO (4/4) | Erratas D1 de 10/10 passam a ter QA; pendência do item RESERVADA de transporte sanada |
| T-44 (3) de "(c) PARES" ao fim, L2 e L3 | idêntico | CONFERIDO | Reconferido após a correção (seção 2) |
| T-46 Adendo 5 / E12 (L1) | acréscimo final, prefixo exato | APROVADO (achados 6–10) | Aceito sem ressalva |

Divergência CPP × CQFP: nenhuma. Os números de linha e tamanhos declarados pela produção conferem com o QA.

## 2. Decisão D1 sobre a ressalva principal (achado 3) — APLICADA

Decisão: aplicar a correção literal proposta pela gce-cqfp (opção principal, AGORA), não a alternativa de registrar nova base de contagem.
Motivo: (a) a convenção desta Gerência desde a G1 (GCE_erratas_reconciliacao_2026-10-10.md, seção 4) é escrever menções do cabeçalho sem a marca, para que a contagem bruta por grep reflita só os itens; (b) o arquivo vai ao Projeto (D-TRANSPORTE-B) e deve chegar com a mesma base de contagem do canônico ([TS] 19, VOLÁTIL 4); (c) a correção é de forma, só no cabeçalho, que o pacote não exporta.
Natureza: errata mínima de forma. O texto aplicado é o literal prescrito pela própria gce-cqfp no QA (seção 4), com o resultado esperado também fixado por ela; a conferência abaixo contra esse resultado fecha a ressalva sem nova rodada de QA (esta Gerência não redigiu texto).

Arquivo: saida/gce/GCE_Lote3_v2_CPP.md, linha 32 (Tabela de Correções, linha T-44).
- onde se lia: `     gabarito, fonte, [TS], VOLÁTIL ou marca V): (1) título "CONTEXTO`
- lê-se: `     gabarito, fonte, troca sutil, volatilidade ou marca V): (1) título "CONTEXTO`

Conferência por script (python3 -I; cópia "antes" em scratchpad/gce_t44/GCE_Lote3_v2_CPP.antes_gerencia.md):
- ocorrência do trecho antigo antes da troca: 1 (na linha 32, confirmada por índice).
- diff por linhas: 1 operação (replace da linha 32); nenhuma outra linha mudou; 1029 → 1029 linhas.
- contagens no arquivo inteiro, antes → depois: [TS] 20 → 19; VOLÁTIL 5 → 4; NORMATIVO — QA 36 → 36; "[V " 2 → 2; REVERIFICAR 4 → 4; QA PENDENTE 0 → 0; SEM FONTE 0 → 0. Igual ao resultado esperado pela gce-cqfp (19; 4; 36; 2).
- SHA-256 de "(c) PARES" ao fim (método da Gerência): bf7bd79300b3a3f05ec615a9398b1228dd8e14139f937ff65b93996f553ca984, antes = depois = valor registrado em 10/10 e no QA.
- bytes: 56918 → 56929 (+11); terminação de arquivo preservada (sem quebra final, como antes).
- SHA-256 do arquivo inteiro após a correção (para o registro de transporte): a9c3fba59aafd21ed9d1f502cc16c610b6cd1389a22da2a350184080358e8ab7.
- A linha 32 ficou com 81 colunas (cosmético; absorvido pela pendência BACKLOG do achado 5).

## 3. Classificação das demais observações

| Origem | Observação | Classe | Decisão |
|---|---|---|---|
| QA achado 3 | "[TS]" e "VOLÁTIL" literais na Tabela de Correções | AGORA | Aplicada e conferida (seção 2) |
| QA achado 5 | Linhas curtas/longas no L3 (148–149, 154; e 32 após esta errata) | BACKLOG | Reembrulho só na próxima errata do arquivo, se houver; tarefa BACKLOG registrada |
| QA achado 4 | "errata T-08" em F4 (l. 52) e N7 (l. 82) do cabeçalho | DESCARTADO | Cabeçalho não exportado; a T-44 visava só o texto do curso, cumprido; F4/N7 são registro de evidência legítimo |
| QA obs. final | "Sem git" nos relatórios de produção | DESCARTADO | Significa "nenhuma operação git pela produtora"; sem efeito |
| Reconciliação | Aplicação de T-44 e E12 no pacote | PRÓXIMO | Já prevista na T-48 (D-T12-V12); sem tarefa nova |
| Reconciliação | Projeto sem o Adendo 5 no GCE_Lote1_consolidacao_GCE.md | AGORA (matéria do Fundador) | Gatilho E (bloco abaixo) |

## 4. Efeitos

- T-48: as condições T-44 e T-46 ficam satisfeitas (fontes: GCE_Lote3_v2_CPP.md no estado da seção 2; GCE_Lote1_consolidacao_GCE.md com Adendo 5, SHA-256 8304882d57c6fcd445439720b932c09337c4704cbe4c60ec1b4a6543b95b2031).
- D-TRANSPORTE-B: a condição para transportar o GCE_Lote3_v2_CPP.md ("só depois da T-44") está cumprida. As erratas D1 G1/G2, que o item RESERVADA registrava como "sem QA", agora estão CONFERIDAS.
- GCE_Lote2_v2_CPP.md: não mudou nesta rodada (SHA-256 6bb88330fe0f92009eba5dcee7b4926d100920d3050066c92bed057a883ae41a).
- Canônico do Projeto: até o transporte, prevalece como registro (D-TRANSPORTE-FUNDADOR); os espelhos da fábrica diferem só em curso, cabeçalho, resumo e adendo, sem item, gabarito, [TS] ou VOLÁTIL diferente.

## 5. Estado final proposto
- T-44: CONCLUÍDA (reconciliada pela GCE em 13/10/2026; ressalva do achado 3 aplicada e conferida).
- T-46: CONCLUÍDA (reconciliada pela GCE em 13/10/2026; sem ressalva).

## BLOCO PARA_PRESIDENCIA
GATILHO E | GCE | Transporte ao Projeto do claude.ai dos espelhos da GCE após T-44 e T-46 (matéria do Fundador): (i) GCE_Lote3_v2_CPP.md — condição da D-TRANSPORTE-B ("só depois da T-44") cumprida, só execução, já decidida; (ii) GCE_Lote1_consolidacao_GCE.md com o Adendo 5 (E12, D-E12-L1) — não coberto pela D-TRANSPORTE-B, o Projeto está sem o Adendo 5 | saida/gce/GCE_Lote3_v2_CPP.md (SHA-256 a9c3fba5…); saida/gce/GCE_Lote1_consolidacao_GCE.md (SHA-256 8304882d…); saida/gce/T44_T46_reconciliacao_2026-10-13.md; saida/gce/QA_T44_T46_2026-10-13_gce-cqfp.md | T-44: 3 operações da produção + 1 errata de forma da Gerência (linha 32); L3 [TS] 19, VOLÁTIL 4, NORMATIVO — QA 36, [V 2, de "(c) PARES" ao fim inalterado; G1-a/b/c e G2 CONFERIDAS (4/4); T-46: +497 bytes, prefixo exato, 0 gabaritos; itens reprovados 0 | Encaminhar ao Fundador: além de executar o transporte já decidido de (i), transportar agora também (ii) GCE_Lote1_consolidacao_GCE.md com o Adendo 5, substituindo o de mesmo nome no Projeto — sim ou não?

## BLOCO TAREFAS
T-?; GCE; Reembrulho cosmético de linhas em saida/gce/GCE_Lote3_v2_CPP.md (linha 32 da Tabela de Correções, 81 colunas; linhas 148–149 e 154 do curso 3.1), sem mudar texto, item, gabarito, [TS], VOLÁTIL ou marca [V]; executar só junto da próxima errata do arquivo, se houver (QA_T44_T46, achado 5); conferência por script: texto com espaços normalizados idêntico e de "(c) PARES" ao fim inalterado; BACKLOG; PENDENTE; gce-cpp → gce-cqfp → gce-gerencia; saida/gce/GCE_Lote3_v2_CPP.md + saida/gce/lote3_reembrulho_<data>.md

## ESTADO FINAL PROPOSTO
T-44: CONCLUÍDA
T-46: CONCLUÍDA

FIM — gce-gerencia, 13/10/2026.
