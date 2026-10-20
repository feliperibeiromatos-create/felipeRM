# T74_reconciliacao_2026-10-20.md — T-74 — 2026-10-20 — gerado por gcb-gerencia

Objeto: reconciliação do Lote D5 — Licitações e contratos, Lei 14.133/2021 (P1-DA, item 10; folhas 10.1 a 10.7). Rito da ficha (seções 9 e 11): Anexo N → v1 → arquivo neutro → leitura externa → R1 → v2 (com acatamento) → R2 → reconciliação → gatilho A. Precedentes: T73_reconciliacao_2026-10-17.md (seção 3, errata de forma) e T101_reconciliacao_2026-10-18.md (seção 2, substituição exata com hash esperado). Scripts em python3 -I, no scratchpad, somente leitura do repositório; navegador não usado; sem commit.

Ordem do Fundador (20/10/2026): entregar os seis lotes de Direito Administrativo no formato da plataforma ("Autorizado a fazer tudo"). Ficam ratificados por essa autorização, e registrados aqui, dois desvios declarados: (a) o R1 começou (20/10/2026, 08:41 UTC) antes de a leitura externa chegar (08:45 UTC, dentro do prazo de 48 horas, que vencia às 16:11:47 UTC), e a leitura entrou na v2 pelo registro de acatamento (ficha, seção 9, última frase); (b) os lotes D2 a D4 foram abertos com o D5 ainda em QA (D-DA-LOTES, "abre após o lote anterior"). Nenhum dos dois afeta item, gabarito ou contagem do D5.

## 1. Conferência própria (script da GCB)
### 1.1 SHA-256 dos objetos (em disco, 20/10/2026)
| Arquivo | SHA-256 | Bytes; linhas | Autor (linha 1; modelo em .claude/agents) |
|---|---|---|---|
| saida/gcb/D5_v2.md (objeto do R2) | 4c61c5cf0c28aae533f8dc1510493e4db633f4423daabdea1c34c0cc1ea7d409 | 313.079; 1.747; LF, sem CR | gcb-cpp (sonnet) |
| saida/gcb/D5_parecer_R2_gcb-cqfp.md | d7a90354821428612626e3e89c548a5dd5284df9131012ed39607daa183becf4 | 36.258; 308 | gcb-cqfp (opus) |
| saida/gcb/D5_parecer_R1_gcb-cqfp.md | e34e66fac3df533ad9ef6bfb8313b80dadb525f06556bd10d7f9202abac80b40 | 31.047; 167 | gcb-cqfp (opus) |
| saida/gcb/D5_leitura_critica.md | 29be8d3cc5c491299e90a4fdb260ed92912c0770b20a04b501da63c51812aaf3 | 17.196; 138 | leitor externo (outro fornecedor), fora da fábrica |
| saida/gcb/D5_ficha_lote.md | 50260772ded9babd3d6d6698011df81bf2ccaab5ffe665f4688b7f4b99fd4a95 | 26.475; 147 | gcb-gerencia (opus) |
| saida/gcb/D5_anexo_N_mapa_normativo.md | 497af8e63ecc78ba838927191235ebace582d69b4b482598130aa484508d76eb | 533.003; 1.746 | qa-normativo-da (opus) |
| saida/gcb/D5_v1.md (objeto do R1) | efcf3aba443006b0bf98f204d5c1bf2cd975c43a361a8c377cdc12218d764d2b | 191.740; 1.405 | gcb-cpp (sonnet) |
| saida/gcb/D5_para_leitura_critica.md (arquivo neutro de 18/10/2026) | 83915866133d6909af626a8355333f6f403681033edb1b0d669d59fcb9439da1 | 102.243; 354 | gcb-gerencia (cabeçalho neutro, D-CABECALHO-NEUTRO) |
| saida/gcb/D5_para_leitura_critica_gen.py | f862cd26fdfdd3568663fe511b0ab28d8d4e35c37aef639ce72539c398d717c8 | 2.875; 42 | gcb-gerencia |

Todos os hashes batem com os declarados no R1 e no R2 (v2 4c61c5cf…d409; v1 efcf3aba…4d2b; R1 e34e66fa…0b40; leitura 29be8d3c…aaf3; ficha 50260772…4a95; Anexo N 497af8e6…76eb; arquivo neutro 83915866…a1; script f862cd26…17c8).

### 1.2 Contagens (parser próprio sobre a seção 5.2 da v2; marca do cabeçalho de cada bloco conferida com a linha "Marcas:" nos 70)
| Folha | Itens | C | E | [TS] (E / C) | REVERIFICAR | VOLÁTIL | QA PENDENTE | QA PENDENTE (R2) |
|---|---|---|---|---|---|---|---|---|
| 10.1 | 10 | 5 | 5 | 5 (4 / 1) | 0 | 0 | 10 | 2 |
| 10.2 | 10 | 5 | 5 | 5 (4 / 1) | 0 | 0 | 10 | 3 |
| 10.3 | 10 | 5 | 5 | 5 (4 / 1) | 0 | 0 | 10 | 4 |
| 10.4 | 10 | 5 | 5 | 5 (4 / 1) | 0 | 0 | 10 | 0 |
| 10.5 | 10 | 5 | 5 | 5 (4 / 1) | 0 | 0 | 10 | 1 |
| 10.6 | 10 | 5 | 5 | 5 (4 / 1) | 0 | 0 | 10 | 5 |
| 10.7 | 10 | 5 | 5 | 5 (4 / 1) | 0 | 0 | 10 | 1 |
| Lote | 70 | 35 (50%) | 35 | 35 (28 / 7) | 0 | 0 | 70 | 16 |
- Ids: 70 na versão do estudante (5.1) e 70 no gabarito comentado (5.2), na mesma ordem; o conjunto é exatamente D5-01 a D5-71 menos o D5-54 (reprovado no R1; id não reutilizado); o D5-71 ocupa a posição 54. Primeira linha no formato do CLAUDE.md; última linha "FIM DO LOTE D5".
- Todo [TS] tem campo "Troca"; 70 pontos de julgamento distintos. Sequência de gabaritos na ordem de apresentação: CEECCECEECCEEECCECCEECCCEEECECCEECECCECEECCECCEECEECCECEEECCCEECCECCEE (igual à da v2, seção 7, e à do R2, seção 7).
- Não regressão v1 → v2 (script próprio; enunciado do 5.1 e campos do 5.2, sem cabeçalho, marcas e "Alteração na v2"): 60 itens idênticos (54 sem toque e os 6 renumerados, pelo mapa da seção 8 da v2: 13↔15, 23↔25, 58↔60); 9 alterados (D5-03, 08, 12, 22, 30, 43, 51, 59 e 65); 1 novo (D5-71); nenhum gabarito alterado. Confere com o R2, seção 1.
- Moldura "Considere que um órgão do Poder Legislativo da União…" (abertura "Considere que" com "Poder Legislativo da União" nas primeiras palavras): 22 enunciados — 13 APL (12 C / 1 E, só o D5-06) e 9 SIT (D5-08, 09, 14, 28, 37, 40, 47, 68, 70: 3 C / 6 E); total 15 C / 7 E. Nenhum APL rotulado fora da moldura. Confere com a v2 (seção 7) e o R2 (seção 8).
- Reprovação: R1 1/70 = 1,4% (D5-54); R2 0/70 = 0%. Gate não acionado.
- Separação produção × QA (critério 9): produção gcb-cpp (sonnet: v1 e v2); QA gcb-cqfp (opus: R1 e R2); normativo qa-normativo-da (Anexo N); gerência gcb-gerencia (ficha, arquivo neutro, script e esta reconciliação); leitura externa de outro fornecedor, fora da fábrica. Nenhum agente revisou texto que produziu.
- Conferências de apoio às decisões: (a) Anexo N, linhas 941 a 958: art. 79, caput e incisos I a III na redação original; inciso IV, § 1º (caput), § 1º, VII e alíneas, e § 2º com redação dada ou incluída pela Lei 15.266/2025, REVERIFICAR — o ajuste 1 do R2 está certo; (b) Anexo N, linhas 116, 118 e 193: art. 6º, XIII, XV e XLIII sem marca "Edital:" — o ajuste 4 do R2 está certo; (c) das 19 substituições de neutralização do script, uma ("Mínimo da ficha: 14, com os 12 obrigatórios (P-01 a P-12). Entregues: 16.") já não existe nas seções 1 a 4 da v2, que trazem ainda 43 ocorrências de "acréscimo da v2", 15 de "QA PENDENTE", 17 de "leitura externa" e 6 de "BQ-" (insumo da D1 do ponto 18).

## 2. D1 da GCB — ponto 20 (moldura do Legislativo)
**Decisão: opção (i).** O teto de "aplicação parlamentar" da ficha, seção 6.3 ("no máximo 2 por folha"), conta os itens rotulados APL; em item SIT, a moldura é cenário. Leitura autêntica da ficha para o D5, no texto do R2 (seção 8, n. 4, (i)): "APL = rótulo; a moldura em SIT é cenário". O arquivo da ficha não é alterado (seu hash é objeto desta reconciliação); a leitura fica registrada aqui, como as dispensas da T-73.
Fundamentos:
1. É a única opção que não exige reescrever item: nenhum enunciado, gabarito, ponto de julgamento ou [TS] muda, e não há nova rodada de QA.
2. Parecer técnico do R2 (seção 8, n. 3 e 5): a opção (ii) na forma proposta (neutralizar os 8 SIT que excedem) tiraria da moldura 6 E e 2 C e a deixaria com 12 C / 2 E (86% de C), marcador visível coincidente com o gabarito, o que o estilo_banca, 5.1, manda evitar; a (ii) "neutralizar os C" não basta para o teto nas folhas 10.1 e 10.4; a (iii) mexe em 2 ou 3 APL C aprovados e exige nova rodada sobre eles, contra a ordem de entrega do Fundador.
3. Finalidade do teto: é teto de formato, cumprido pelo rótulo em todas as folhas (APL ≤ 2). Nos 9 SIT, o gabarito não depende do Legislativo; o ponto de julgamento é o dispositivo (R2, seção 8, n. 2). A seção 4 da ficha manda o exemplo dizer que é hipotético ("considere que um órgão do Poder Legislativo da União…"); não manda contar toda moldura como APL.
Mitigação do viés da moldura (15 C / 7 E), nota à GBQ que acompanha a opção (i) do R2 ("não concentrar itens com a moldura no mesmo simulado"), em forma operacional: (a) no mesmo simulado, no máximo 2 itens com a moldura por folha; (b) simulado com 3 ou mais itens com a moldura leva ao menos 1 E com a moldura (D5-06, 08, 09, 14, 40, 47 ou 70). Os 22 itens com a moldura: D5-01, 06 (10.1 APL); 08, 09 (10.1 SIT); 16 (10.2 APL); 14 (10.2 SIT); 22, 24 (10.3 APL); 28 (10.3 SIT); 34, 39 (10.4 APL); 37, 40 (10.4 SIT); 43, 46 (10.5 APL); 47 (10.5 SIT); 53, 60 (10.6 APL); 64, 67 (10.7 APL); 68, 70 (10.7 SIT).
Registro para o reforço da T-100 (D5-R; sem tarefa nova, D-COMPLEMENTOS): a ficha do reforço deve pedir que item novo com a moldura seja preferencialmente E, até o conjunto com a moldura ficar entre 40% e 60% de C.
Efeito documental: as menções "DIVERGÊNCIA PARA A GCB" das seções 0, 7 e 8 da v2 ficam como histórico, resolvidas por esta D1; não se reescrevem.

## 3. D1 da GCB — ajustes residuais (R2, seção 9) e pendentes
| Objeto | Decisão | Motivo | Substituição (seção 4) |
|---|---|---|---|
| R2 9, n. 1 — art. 79 em C10.1-12 e na linha A7 da seção 0.1 | APLICAR, texto exato da QA | Imprecisão confirmada no Anexo N (1.2, (a)); fora dos itens | n. 4 e 5 |
| R2 9, n. 2 — pegadinha de C10.5-07 e G-68 (proximidade com a sugestão B9 do leitor; ficha 9: "texto do leitor não é copiado") | APLICAR, texto exato da QA, nas duas ocorrências | Regra da ficha; dispositivo inalterado (art. 24, caput, I e parágrafo único). Como a frase ocorre 2 vezes, cada texto_antigo leva o prefixo da sua linha, que não muda | n. 6 e 8 |
| R2 9, n. 3 — seção 8 da v2, fronteira do art. 117 | APLICAR, texto exato da QA | Após a renumeração, a segregação é o D5-60, e o D5-58 é a prerrogativa | n. 10 |
| R2 9, n. 4 — lista dos dispositivos sem marca "Edital:" (seções 0 e 8) | APLICAR, texto exato da QA, nas duas ocorrências | Lista incompleta confirmada (1.2, (b)); cada texto_antigo leva o trecho seguinte da sua linha, que não muda | n. 3 e 9 |
| R2 9, n. 5 (opcional) — resumo, linha 10.6 | APLICAR, texto exato da QA | Forma; a frase atual omite a pegadinha G-71, que também carrega o § 2º; sem item | n. 7 |
| Linhas 1 e 2 | APLICAR (ordem da T-74) | Linha de controle da v2.1 e versão no título; o arquivo é interno (ficha, seção 2, item 0), e a D-CABECALHO-NEUTRO só vale para versão que sai da fábrica | n. 1 e 2 |
| Ponto 18 — regerar o D5_para_leitura_critica.md | NÃO APLICAR | A leitura externa já foi feita sobre o arquivo de 18/10/2026 (gravado às 16:11:47 UTC; SHA-256 83915866…a1), como registra a linha 2 do D5_leitura_critica.md ("enviado: D5_para_leitura_critica.md (SHA-256 8391…)"), e a resposta chegou no prazo. O arquivo cumpriu a única função que a ficha (seção 9) lhe dá; nenhuma segunda leitura está ordenada. Regerar exigiria nova neutralização (1.2, (c)), isto é, texto novo da gerência e nova conferência de neutralidade, sem destinatário. O arquivo de 18/10 fica intacto como prova do que o leitor recebeu. | — |
| Ponto 23 — parametrizar os caminhos do script | NÃO APLICAR agora | Depende do ponto 18; o script não precisa rodar (o R1 já o reproduziu byte a byte numa cópia). Condição: se o Fundador ou a Presidência ordenarem nova leitura externa ou entrega do D5 para fora da fábrica, a gcb-gerencia gera, a partir da D5_v2_1.md, um arquivo com nome novo (sem sobrescrever o de 18/10), com script de caminhos relativos à raiz do repositório, e a gcb-cqfp confere a neutralidade antes da saída (D-CABECALHO-NEUTRO). | — |
| Ponto 24 — arquivo de acatamento em separado | NÃO APLICAR (não extrair) | A seção 0.1 da v2 é aceita como o registro de acatamento da ficha, seção 9, e do critério 7: está item a item, com motivo, e o R2 a aprovou com ressalvas; a única ressalva de conteúdo (art. 79) é corrigida pelas substituições 4 e 5. Extrair criaria um segundo arquivo com o mesmo texto (PADRÃO ÚNICO, seção 9: um editor por arquivo canônico). Dispensa só de forma, para o D5. | — |
| R2 5.4 — blocos de curso sem marca "Edital:" | MANTER | A ficha (seção 8) admite esses temas no curso, sem item, se servirem a uma folha; cada artigo está presente e vigente no Anexo N (R2, 5.3 e 5.4). Retirá-los exigiria reescrever curso, pares e pegadinhas aprovados. A lista fica completa pelas substituições 3 e 9. | — |
| Pendentes (d) e (e) da v2 — P-30 redundante; rótulos "deserta"/"fracassada" | ACEITOS | P-30 só preenche a tabela de pares; rótulo doutrinário ao lado do artigo é permitido (ficha, seção 3) | — |

Critérios da ficha, seção 10: 1 a 6 e 8 a 9 cumpridos (seção 1); 7 cumprido com a dispensa de forma do ponto 24; o critério 3 ("formatos dentro do teto") cumprido pela leitura da seção 2.

## 4. Tabela de substituições exatas para a D5_v2_1.md
Regras para o orquestrador: (1) ler saida/gcb/D5_v2.md (4c61c5cf…d409) em UTF-8; (2) para cada linha do bloco CSV abaixo (separador ";", campos entre aspas), na ordem de n, conferir que texto_antigo ocorre exatamente uma vez e trocá-lo por texto_novo; (3) gravar saida/gcb/D5_v2_1.md em UTF-8, LF, sem outra mudança; a D5_v2.md não é alterada. A GCB conferiu por script que cada texto_antigo ocorre uma única vez na v2, também na aplicação sequencial, e que nenhum reaparece depois.

```csv
"n";"linha_aprox";"texto_antigo";"texto_novo";"origem"
"1";"1";"# D5_v2.md — T-74 — 2026-10-20 — gerado por gcb-cpp";"# D5_v2_1.md — T-74 — 2026-10-20 — gerado por gcb-cpp; errata de forma da gcb-gerencia (T74_reconciliacao_2026-10-20.md)";"ordem da T-74 (linha 1); D1 GCB, seção 4"
"2";"2";"LOTE D5 — Licitações e contratos (Lei 14.133/2021) — v2 — 2026-10-20";"LOTE D5 — Licitações e contratos (Lei 14.133/2021) — v2.1 — 2026-10-20";"ordem da T-74 (linha 2); D1 GCB, seção 4"
"3";"40";"C10.1-10 (arts. 33, 34 e 24, parágrafo único), C10.1-12 (art. 78), C10.3-06 (arts. 46 e 6º, XXXII e XXXIII; art. 99";"C10.1-10 (art. 6º, XIII e XIV; arts. 33, 34 e 24, parágrafo único), C10.1-12 (art. 78; art. 6º, XLIII), pares P-17 (art. 6º, XIII e XIV), P-22 (art. 6º, XLIII) e P-23 (art. 6º, XV e XVII), C10.3-06 (arts. 46 e 6º, XXXII e XXXIII; art. 99";"R2, seção 9, n. 4 (seção 0, pendente (c)); contexto final inalterado só para unicidade"
"4";"56";"O art. 79 (redação de 2025, REVERIFICAR no Anexo N, fora dos núcleos) foi retirado da base e não é usado.";"O art. 79 (inciso IV e §§ 1º e 2º com redação de 2025, REVERIFICAR no Anexo N; artigo fora dos núcleos) foi retirado da base e não é usado.";"R2, seção 9, n. 1 (seção 0.1, linha A7)"
"5";"171";"O art. 79, que trata das hipóteses de uso do credenciamento, tem redação de 2025 (Lei 15.266/2025) e está marcado REVERIFICAR no Anexo N: não é usado neste lote.";"O art. 79, que trata das hipóteses de uso do credenciamento, tem o inciso IV, o § 1º (caput e inciso VII, com as alíneas) e o § 2º com redação dada ou incluída pela Lei 15.266/2025, marcados REVERIFICAR no Anexo N; o artigo não é usado neste lote.";"R2, seção 9, n. 1 (C10.1-12, definição)"
"6";"341";"- Pegadinha provável: Afirmar que o sigilo do orçamento estimado pode ser imposto sem justificativa, que prevalece perante os órgãos de controle interno e externo ou que o preço estimado ou o máximo aceitável pode ser omitido do edital quando o julgamento for por maior desconto";"- Pegadinha provável: Dar caráter sigiloso ao orçamento estimado sem justificativa, opor o sigilo aos órgãos de controle interno e externo ou deixar fora do edital, na licitação por maior desconto, o preço estimado ou o máximo aceitável";"R2, seção 9, n. 2 (C10.5-07); prefixo inalterado só para unicidade"
"7";"426";"(art. 117, § 2º; só no curso e nos pares)";"(art. 117, § 2º; só no curso, no par P-27 e na pegadinha G-71, sem item)";"R2, seção 9, n. 5 (opcional; resumo, linha 10.6)"
"8";"567";"G-68. [C10.5-07] Afirmar que o sigilo do orçamento estimado pode ser imposto sem justificativa, que prevalece perante os órgãos de controle interno e externo ou que o preço estimado ou o máximo aceitável pode ser omitido do edital quando o julgamento for por maior desconto";"G-68. [C10.5-07] Dar caráter sigiloso ao orçamento estimado sem justificativa, opor o sigilo aos órgãos de controle interno e externo ou deixar fora do edital, na licitação por maior desconto, o preço estimado ou o máximo aceitável";"R2, seção 9, n. 2 (G-68); prefixo inalterado só para unicidade"
"9";"1739";"C10.1-10 (arts. 33, 34 e 24, parágrafo único), C10.1-12 (art. 78), C10.3-06 (arts. 46 e 6º, XXXII e XXXIII) e";"C10.1-10 (art. 6º, XIII e XIV; arts. 33, 34 e 24, parágrafo único), C10.1-12 (art. 78; art. 6º, XLIII), pares P-17 (art. 6º, XIII e XIV), P-22 (art. 6º, XLIII) e P-23 (art. 6º, XV e XVII), C10.3-06 (arts. 46 e 6º, XXXII e XXXIII) e";"R2, seção 9, n. 4 (seção 8, pendente (b)); contexto final inalterado só para unicidade"
"10";"1743";"(requisitos e segregação, D5-51, D5-52, D5-58, D5-59)";"(requisitos e segregação, D5-51, D5-52, D5-59, D5-60)";"R2, seção 9, n. 3 (seção 8, fronteira do art. 117)"
```

Resultado esperado (simulado pela GCB no scratchpad, aplicando o bloco acima extraído deste arquivo): **saida/gcb/D5_v2_1.md, SHA-256 44ddcc982642df66b246108cb7e3ef86031e8a99762aa2262a6c0bdde24e1333**, 313.486 bytes, 1.747 linhas, LF, sem CR. Diff v2 → v2.1 só nas linhas 1, 2, 40, 56, 171, 341, 426, 567, 1.739 e 1.743. A seção 5 (itens) fica idêntica; da seção 6 até "FIM DO LOTE D5", mudam só as linhas 1.739 e 1.743 (seção 8). Nenhum item, gabarito, [TS], marca ou contagem muda.
Conferência: o orquestrador confere o hash e o diff; a gcb-cqfp confere só os 10 trechos (R2, seção 9, fecho: "a QA confere só os trechos acima (diff), sem nova rodada sobre os itens"). Se o hash ou o diff divergirem, a transcrição é refeita e o gatilho A não é emitido.

## 5. Lista final, marcas, divergências e proveniência
### 5.1 Itens aprovados (70; R2 APROVADO 70/70; ordem de apresentação; "(R2)" = alterado, renumerado ou criado na v2)
| Folha | Itens | Item (número NN de D5-NN), gabarito e [TS] |
|---|---|---|
| 10.1 | 10 | 01 C; 02 E [TS]; 03 E [TS] (R2); 04 C; 05 C; 06 E [TS]; 07 C; 08 E (R2); 09 E [TS]; 10 C [TS] |
| 10.2 | 10 | 11 C; 12 E [TS] (R2); 13 E [TS] (R2); 14 E; 15 C (R2); 16 C; 17 E [TS]; 18 C [TS]; 19 C; 20 E [TS] |
| 10.3 | 10 | 21 E; 22 C (R2); 23 C [TS] (R2); 24 C; 25 E [TS] (R2); 26 E [TS]; 27 E [TS]; 28 C; 29 E [TS]; 30 C (R2) |
| 10.4 | 10 | 31 C; 32 E [TS]; 33 E [TS]; 34 C; 35 E [TS]; 36 C [TS]; 37 C; 38 E; 39 C; 40 E [TS] |
| 10.5 | 10 | 41 E [TS]; 42 C [TS]; 43 C (R2); 44 E [TS]; 45 C; 46 C; 47 E; 48 E [TS]; 49 C; 50 E [TS] |
| 10.6 | 10 | 51 E [TS] (R2); 52 C [TS]; 53 C; 71 E (R2); 55 C; 56 E [TS]; 57 E [TS]; 58 E [TS] (R2); 59 C (R2); 60 C (R2) |
| 10.7 | 10 | 61 C; 62 E [TS]; 63 E [TS]; 64 C; 65 C (R2); 66 E [TS]; 67 C; 68 C [TS]; 69 E [TS]; 70 E |
Todos AUTORAL, "QA PENDENTE" no arquivo de trabalho até o aceite do gatilho A (D-QA-PENDENTE; precedente D-LOTED6-CANONICO): a GBQ retira as marcas no pacote e na edição do estudante, na exportação do módulo m-da; a GCB não reedita o canônico.

### 5.2 VOLÁTIL e REVERIFICAR
- Itens VOLÁTIL: nenhum (0/70). Itens REVERIFICAR: nenhum (0/70). Nenhum item fica inapto a simulado final por VOLÁTIL ou REVERIFICAR.
- Fora dos itens, com REVERIFICAR: curso C10.1-08 (art. 75, XVI, redação da Lei 15.471/2026). Mencionado só para dizer que não é usado: art. 79 (C10.1-12; seção 0.1, A7, B8 e C2). Para a T-11 (acréscimo pedido ao orquestrador, parte DA): reabrir, em 4–8/1/2027, o art. 75, XVI, no compilado do planalto.gov.br, com "verificado em [data]" (qa-normativo-da → gcb-gerencia); nenhum item depende dele.

### 5.3 Divergências remanescentes CPP × CQFP (registro; nenhuma pede decisão de mérito)
1. Ponto 20: a produtora não acolheu e remeteu à GCB; a QA deu parecer técnico. Resolvida pela D1 da seção 2.
2. Pontos 18, 23 e 24: a produtora não acolheu (18, 23) ou acolheu em parte (24) por escopo; a QA aceitou o motivo e remeteu à GCB. Resolvidas pela seção 3.
3. Ponto 19: a afirmação da produtora de que nenhuma combinação de até três trocas C×E reduz mais os períodos 5 a 8 não foi refeita pela QA (R2, seção 2). É informativa; a ficha (6.4) só testa os períodos 2 a 4, aprovados. Fica sem decisão, por não ter efeito.
4. Seção 0.1 (art. 79), G-68 e seção 8 (D5-58): apontados pela QA, sem resposta da produtora (a rodada encerrou no R2); corrigidos pelas substituições com o texto exato da QA.
5. Registro sem divergência: o SHA-256 do HTML da Lei 14.133 aberto em 20/10/2026 (R1 553c842b…a7f2; R2 3d747214…1d13) difere do Anexo N (c8c14fdb…5f6f), com o mesmo tamanho e o mesmo texto dos dispositivos (R1: 1.435/1.435; R2: 315/315). Não afeta item.

### 5.4 Proveniência (Anexo N, seção 1; URLs sem parâmetro, idênticas às da v2, seção 6)
| Norma | URL oficial | Anexo N (verificado em 18/10/2026): bytes; SHA-256 | Reabertura pela QA (20/10/2026) | Uso no lote |
|---|---|---|---|---|
| Lei 14.133/2021 (compilada) | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm | 649.705; c8c14fdb…5f6f | R1 08:41 UTC e R2 09:42 UTC: HTTP 200, mesmos bytes | Base única de todos os 70 itens (dispositivos vigentes da seção 4 do Anexo N) |
| Lei 15.266/2025 (alteradora) | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15266.htm | 22.251; 14f94d49…7a0d | HTTP 200, mesmos bytes | REVERIFICAR; nenhum dispositivo alterado por ela é usado |
| Lei 15.471/2026 (alteradora) | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15471.htm | 72.507; f710a39a…f479 | HTTP 200, mesmos bytes | REVERIFICAR; só C10.1-08 (art. 75, XVI), sem item |
| Lei 15.210/2025 (alteradora) | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15210.htm | 14.239; badd33a8…080a | HTTP 200, mesmos bytes | REVERIFICAR; art. 44-A não usado |
- Leis 6.404/1976 e 12.846/2013: só remissão do próprio texto da Lei 14.133 (C10.1-11; C10.2-08), sem texto aberto nem usado. Valores em reais atualizados (art. 182; Decretos 12.343/2024 e 12.807/2025), atribuições do gestor, promulgação dos vetos e ADI 6890: "[SEM FONTE — não afirmar]", só no curso; nenhum em item.
- Itens reais (Anexo R; CEBRASPE_ANALOGA; só calibragem e "difere de"): BQ-0113 (TRF6 2024, aplicação 19/1/2025), BQ-0134 e BQ-0135 (CNJ 2024, aplicação 30/6/2024), BQ-0142 (FUB 2025, aplicação 29/6/2025); fontes em cdn.cebraspe.org.br (banco/banco.csv). Itens com "difere de": D5-08, 09, 40, 53, 55, 56, 65, 66 e 67.

### 5.5 Notas à GBQ (para depois do aceite; módulo m-da)
- Não pôr no mesmo simulado: D5-61 com D5-62 ou D5-70; D5-39 com D5-57; D5-24 com D5-26; D5-66 com D5-67; D5-43 com D5-49; D5-13 com D5-15; D5-23 com D5-25 (R1, ponto 22; v2 e R2).
- Moldura do Legislativo: regras (a) e (b) da seção 2.
- Campo "nucleo": true nos 70 (ficha, seção 5.1; D-REFORCO-2). Nada vai à plataforma nem à candidata sem a exportação da GBQ após o gatilho A e o sim do Fundador para a publicação.

## 6. Veredito, estado e gatilho A
- **Lote D5 RECONCILIADO.** Fica PRONTO para o gatilho A quando o orquestrador conferir o hash e o diff da D5_v2_1.md (seção 4) e a gcb-cqfp conferir os 10 trechos. Versão final: saida/gcb/D5_v2_1.md; a D5_v2.md fica como objeto do R2.
- Estado da T-74: EM CURSO até a transcrição e as conferências; CONCLUÍDA pelo orquestrador depois do aceite (esta Gerência não altera a linha da T-74). Tarefas novas: nenhuma (D-COMPLEMENTOS).

Texto do gatilho A (emitir só se o hash e o diff conferirem):
GATILHO A | GCB | Lote D5 v2.1 — Licitações e contratos, Lei 14.133/2021 (P1-DA item 10; ordem do Fundador de 20/10/2026) — v1 → R1 gcb-cqfp 1/70 (1,4%) → v2 → R2 gcb-cqfp APROVADO COM RESSALVAS 70/70, 0% → errata de forma com texto exato da QA (10 substituições; ponto 20 pela opção (i)) | saida/gcb/D5_v2_1.md (SHA-256 44ddcc98…1333); D5_v2.md (4c61c5cf…d409); D5_parecer_R2_gcb-cqfp.md (d7a90354…ecf4); D5_parecer_R1_gcb-cqfp.md (e34e66fa…0b40); D5_anexo_N_mapa_normativo.md (497af8e6…76eb); T74_reconciliacao_2026-10-20.md | 70 itens (D5-01 a D5-71, sem o D5-54); 35 C / 35 E; [TS] 35; VOLÁTIL 0; REVERIFICAR 0; diff v2 → v2.1 só nas linhas 1, 2, 40, 56, 171, 341, 426, 567, 1739 e 1743 | Aceita como canônico o Lote D5 v2.1 (saida/gcb/D5_v2_1.md, SHA-256 44ddcc982642df66b246108cb7e3ef86031e8a99762aa2262a6c0bdde24e1333), incluindo "D5 (v2.1)" na D-CANONICOS, para exportação pela GBQ no módulo m-da? SIM / NÃO

FIM DA RECONCILIAÇÃO T-74
