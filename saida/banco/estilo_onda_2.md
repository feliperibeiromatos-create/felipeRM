# estilo_onda_2.md — T-96 — 2026-10-18 — gerado por gbq-estilo

Esta é a auditoria de estilo da onda 2 do reforço (D-REFORCO-2, regras 5 e 6; T96_reconciliacao_2026-10-18.md, seção 7). Ciclo 2026-10-18 s12c3. Destino: gce-gerencia, que fecha a T-96.

Referências:
- regras/estilo_banca.md v1.1.3 (tipologia E1–E6 e C1–C6, marcadores na seção 4, recomendações na seção 5);
- saida/banco/estilo_onda_1.md;
- registros O-1 a O-8 de saida/banco/T93_reconciliacao_2026-10-18.md;
- registros de estilo da seção 3 de saida/gce/T96_reconciliacao_2026-10-18.md.

Objeto, lido em modo somente leitura: saida/gce/L1_reforco_onda2_A_v3.md, B_v2.md, C_v2.md e D_v3.md, com 111 itens, de L1-R19 a L1-R130, sem o L1-R43. Nenhum item foi alterado. O L1-R131 (saldo) fica fora da amostra, como manda a seção 7.

**Resultado:** 12 itens auditados, 12 APROVADOS e 0 REPROVADOS (0%). Não há GATE. Gabarito da onda por contagem própria: 56 C / 55 E, ou 50,5% de C. CONFERE com o esperado e está dentro da faixa de 40% a 60% (regra 5).

## 1. Amostra e critério

- **Universo:** 111 ids. Saem da Parte 2 (enunciado) e da Parte 3 (gabarito) dos quatro arquivos finais, extraídos por script (`python3 -I`).
- **Folhas:** a folha de cada id vem da faixa de numeração do mapa, com 14 ids por folha a partir do L1-R19. A 1.2 tem 13 ids, porque não tem o R43.
- **Tamanho da amostra:** 10% de 111 = 11,1. A seção 7 fixou 12 itens.
- **Sorteio estratificado, com semente registrada:** `rng = random.Random(20261018)`.
  1. Um item por folha, de 1.1 a 1.8, nessa ordem, com `rng.choice` sobre os ids da folha em ordem crescente.
  2. Depois, 4 itens com `rng.sample(restantes, 4)`, entre os 103 que sobraram, em ordem crescente.
- **Amostra:**
  - pela etapa 1: L1-R32 (1.1), R46 (1.2), R50 (1.3), R66 (1.4), R87 (1.5), R90 (1.6), R116 (1.7) e R124 (1.8);
  - pela etapa 2: R89 (1.6), R95 (1.6), R129 (1.8) e R34 (1.2).
- **Composição da amostra:** 9 C e 3 E. Cobre todas as 8 folhas e as 4 partes (A 3, B 2, C 4, D 3).

Critérios de estilo, os mesmos da onda 1:
- comando "Julgue o item";
- uma afirmação e um só ponto de erro;
- mecanismo reconhecível na tipologia;
- marca [TS] coerente com a convenção (O-6);
- marcadores que não denunciam o gabarito;
- extensão dentro do observado (O-1);
- nenhuma pista textual que entregue a resposta.

Os registros O-1 a O-8 entram como critério, mas não são regra de reprovação (T93_reconciliacao, seção 2).

## 2. Vereditos por item

Contagem de palavras: só o enunciado, sem o comando.

| id | folha | gab. | mecanismo (estilo_banca) | palavras | veredito | motivo |
|---|---|---|---|---|---|---|
| L1-R32 | 1.1 | C | C1 (descrição correta de funcionamento), com hedge "em geral" | 36 | APROVADO | Uma afirmação, comando certo. "pode" e "em geral" são possibilidade afirmativa e hedge, compatíveis com C (seção 4) sem decidir o gabarito. Observação, sem reprovar: a discriminação é baixa, porque o enunciado genérico não exige o detalhe da base. |
| L1-R46 | 1.2 | C [TS] (espelho) | C3 (C que parece E: atribui desempenho "comparável ou superior" ao end-to-end) | 37 | APROVADO | O ponto é único e a remissão "Segundo a documentação do ESPnet" é fiel. "qualquer" num C diversifica os absolutos (O-7). Observação: a cauda de ressalva ("o que não implica superioridade em qualquer condição de uso") é verdadeira. Para quem lê ressalva como sinal de C, ela aproxima o item de uma pista. Convém não repetir esse fecho como padrão. |
| L1-R50 | 1.3 | E [TS] | E1 (extrapolação por absoluto: "rigorosamente idênticas", "elimina toda a aleatoriedade") | 42 | APROVADO | Situação hipotética no formato Cebraspe ("Nessa situação"). O erro é um só (a garantia de determinismo), e o "pois" repete o mesmo erro sem criar outro. Usa "pois" num E (O-7). Observação: são dois absolutos empilhados ("rigorosamente", "toda"). O mecanismo é legítimo, mas a ênfase dupla facilita o atalho "absoluto = E". Um absoluto basta (O-5). |
| L1-R66 | 1.4 | C | C1, com aplicação parlamentar | 38 | APROVADO | Cumpre o O-2: "independentemente" num C, em uso próprio. "pode" calibra a afirmação ao que a base sustenta. Não há pista de extensão. |
| L1-R87 | 1.5 | E [TS] | E4 (troca de componente × função: #itn no lugar de #rewrite) | 63 | APROVADO | Situação hipotética com uma troca só. A oração "que se destina a trocar palavras…" atribui à #itn a função da #rewrite, ou seja, é a mesma troca, não um segundo erro. É um E longo, como pede o O-1. O VOLÁTIL (baixo/médio) não é matéria de estilo. |
| L1-R90 | 1.6 | E [TS] | E5 (moldura verdadeira, "afastado reduz", com contraparte falsa, "próximo melhora") | 46 | APROVADO | O ponto é único e "ao passo que" separa a parte verdadeira da falsa sem se denunciar. Observação, ligada ao O-4 por analogia (documentação, não norma): a ambientação "na captação do áudio do Plenário para o ASR" ficou dentro do escopo de "Segundo a nota de transparência", e a nota não fala de Plenário. Não muda o gabarito. É uma das 5 aberturas "Segundo a…" da parte C (seção 4). |
| L1-R116 | 1.7 | C | C2 (recomendação documentada, reproduzida com o contraste "e não") | 38 | APROVADO | O contraste "…e não montar diretamente conexões HTTP/2 ou WebSocket" num C funciona como espelho de troca sem marca [TS], o que é coerente. A causal "por serem…" num C cumpre o O-7. A afirmação é fiel ao trecho literal da base. |
| L1-R124 | 1.8 | C | C1, com aplicação parlamentar (advertência do model card) | 38 | APROVADO | O juízo pedido é a existência da advertência, e "deve levar em conta" é verdadeiro qualquer que seja o caráter da reunião. Observação, que confirma o registro da QA (seção 3 da T96_reconciliacao): "reuniões reservadas" pode sugerir que essas gravações são feitas sem consentimento. É um vínculo implícito que o model card não faz. O risco de recurso é baixo. Nas próximas ondas, a ambientação não deve sugerir a qualificação que a fonte adverte. |
| L1-R89 | 1.6 | C | C1, em situação hipotética | 47 | APROVADO | O ponto é único e "pois" num C cumpre o O-7. Observação: a discriminação é baixa, porque o efeito (acurácia menor com idioma não configurado) é intuitivo. |
| L1-R95 | 1.6 | C [TS] (espelho) | C3 (associação correta que parece trocada: inserção ↔ ruído) | 48 | APROVADO | Situação hipotética com predicado "compatível com", que é afirmação única. Observação 1: "a orientação de que…" não nomeia a fonte (documentação do Azure Speech), e o artigo definido pressupõe uma orientação que o candidato precisa reconhecer. Recomenda-se nomear a documentação. Observação 2: "ruído de fundo" no cenário e "ambiente ruidoso" na conclusão são eco lexical que facilita o C. |
| L1-R129 | 1.8 | C | C2 (conduta correta, com predicado avaliativo explícito) | 43 | APROVADO | "agiu corretamente ao ressalvar" fixa um só juízo, e "pode variar muito" num C é fiel ao "may vary significantly" da base. A extensão está na média. |
| L1-R34 | 1.2 | C | C1, com aplicação ao acervo | 31 | APROVADO | Uma afirmação, comando certo, extensão curta (O-1). Observação: a discriminação é baixa, como no L1-R32. |

Taxa de reprovação da amostra: 0/12 = 0%, abaixo do gate de 30%.

## 3. Faixa de C da onda (regra 5), por contagem própria

Contagem por script sobre a Parte 3 dos quatro arquivos, com uma entrada por id. Todos os 111 ids da Parte 2 têm gabarito na Parte 3, e todos os 111 enunciados usam o comando "Julgue o item."

| parte | arquivo | itens | C | E | %C |
|---|---|---|---|---|---|
| A (1.1–1.2) | L1_reforco_onda2_A_v3.md | 27 | 14 | 13 | 51,9 |
| B (1.3–1.4) | L1_reforco_onda2_B_v2.md | 28 | 14 | 14 | 50,0 |
| C (1.5–1.6) | L1_reforco_onda2_C_v2.md | 28 | 14 | 14 | 50,0 |
| D (1.7–1.8) | L1_reforco_onda2_D_v3.md | 28 | 14 | 14 | 50,0 |
| Onda 2 | 4 arquivos | 111 | 56 | 55 | 50,5 |

- CONFERE com o esperado (56 C / 55 E = 50,5%), dentro da faixa de 40% a 60%.
- C/E por folha, também CONFERE com a tabela da seção 6 da reconciliação:
  - 1.1: 7/7;
  - 1.2: 7/6;
  - 1.3 a 1.6: 7/7 cada;
  - 1.7: 6/8;
  - 1.8: 8/6.
- Com o saldo L1-R131 (E): 56/112 = 50,0%.
- [TS] por contagem própria: 65 (CONFERE). Destes, 13 estão em itens C, com espelho declarado: R25, R28, R39, R46, R49, R64, R72, R79, R95, R99, R112, R120 e R126.

## 4. Cumprimento de O-1 a O-8 na onda e registros da seção 3

Método: expressão regular sobre o enunciado (Parte 2) dos 111 itens, com revisão manual dos falsos positivos indicados. O AVISO da seção 4 do estilo_banca continua valendo: nenhum marcador decide o gabarito.

| registro | situação na onda 2 | avaliação |
|---|---|---|
| O-1 Extensão | C: média 40,9, mediana 41,5, de 25 a 57. E: média 40,8, mediana 40, de 26 a 64. Na onda 1 eram 49,6 contra 40,4. Nenhum C passa de 65 palavras. Há E longos: R19 (64) e R87 (63). Médias por parte (C × E): A 42,4 × 41,8; B 40,5 × 39,4; C 45,1 × 44,9; D 35,6 × 37,4. | CUMPRIDO. A pista de extensão foi neutralizada: a diferença é de 0,1 palavra. A relação da base (E um pouco mais longo que C) só aparece na parte D. O registro da QA para a parte B (C 40,5 × E 39,4) CONFERE e não é pista relevante. |
| O-2 "independe" | "independentemente" aparece em 4 C (R31, R66, R83, R104) e em 0 E em uso próprio. O R69 (E) tem o adjetivo "de forma independente", que não conta. | CUMPRIDO, mas agora o marcador está só em C. Na onda 3, escrever também E com "independe" para não criar a pista inversa. |
| O-3 Possibilidade afirmativa | "pode/podem/poderá…": 23 C e 8 E (R38, R54, R63, R98, R106, R110, R114, R117). | CUMPRIDO quanto a usar "pode" em E. O viés para C continua (74%, contra 73% na onda 1 e 75% na base) e não é motivo de reprovação. |
| O-4 Remissão à norma | Nenhum enunciado cita norma: o único acerto da busca, "Constituição" no R101, é nome de comissão. Por analogia, em remissão a documentação, a ambientação parlamentar fica dentro de "Segundo a…" no R90 (amostra) e no R92 ("por isso, siglas… da Casa… justificam"). | CUMPRIDO quanto à norma. Fica o registro por analogia, sem efeito. |
| O-5 Cauda que se denuncia | Não há cauda autocontraditória na amostra. Há absolutos empilhados no R50 ("rigorosamente", "toda") e "por completo" no R38 (fora da amostra). | CUMPRIDO, com a observação do R50. |
| O-6 [TS] em C | 13 C com [TS] espelho, declarado na legenda de cada parte. | CUMPRIDO (convenção admitida). |
| O-7 Restritivos e causais | "apenas": 6 C e 9 E. "somente": 1 C e 4 E. "só" restritivo: 2 C (R58, R72) e 3 E (R21, R48, R107); o "de uma só vez" do R33 não conta. "sempre": 1 C e 1 E. "qualquer": 1 C e 1 E. "nunca": 0 C e 1 E. "pois": 5 C e 6 E. "porque": 2 C e 0 E. "prioritariamente", "exclusiv-" e "uma vez que" não aparecem. | CUMPRIDO: há restritivos em C e causas em C e em E. |
| O-8 Concessiva | "ainda que": 0 C e 3 E (R54, R85, R103). "embora": 1 C (R105). "mesmo que": nenhum. | CUMPRIDO: há concessiva em E. A distribuição inverteu em relação à onda 1 (onde "ainda que" estava só em C). Na onda 3, alternar. |
| Seção 3: abertura "Segundo a…" (parte C) | CONFERE: 5 na parte C (R80 E, R90 E, R92 C, R99 C, R102 E). Na onda inteira, 10 aberturas "Segundo", 5 em C e 5 em E. | Repetição de forma, sem pista de gabarito. Na onda 3, variar a abertura. |
| Seção 3: R124 | Confirmado como observação (seção 2). | Sem efeito. |
| Seção 3: R68 (fora da amostra) | Conta direta (50 h × 36 s = 30 min), C. | Registro de baixa discriminação confirmado, sem efeito. Mesma família de R32, R34 e R89. |

## 5. Encaminhamento

- **À gce-gerencia:** a auditoria da seção 7 está concluída sem GATE (0/12; faixa de 50,5% conferida). Pela ordem da seção 10 da T96_reconciliacao, a T-96 pode passar a CONCLUÍDA, e o gatilho A da seção 9 pode ser colado depois do diff idêntico dos v3, que já foi conferido pelo orquestrador.
- **Recomendações à onda 3 (T-97), sem efeito sobre os 111 itens:**
  1. pôr "independe" também em E;
  2. alternar a concessiva entre C e E;
  3. variar a abertura "Segundo a…";
  4. nomear a fonte quando o item usar "a orientação"/"a recomendação";
  5. não empilhar absolutos num E;
  6. manter a ambientação parlamentar fora do escopo da remissão;
  7. subir a discriminação dos C genéricos.
- A incorporação dos O-1 a O-8 e destas recomendações a uma v1.1.4 do estilo_banca continua sendo opção da GBQ, em tarefa própria.

AVISO: os vereditos e a atribuição de mecanismo são julgamento deste agente (gbq-estilo) e exigem revisão da GBQ. As contagens de C/E, [TS], extensão e marcadores vêm de script sobre os arquivos finais. Os marcadores tiveram revisão manual só nos falsos positivos indicados. O sorteio é reproduzível com a semente e o procedimento da seção 1.
