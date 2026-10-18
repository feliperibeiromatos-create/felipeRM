# estilo_onda_4.md — T-98 — 2026-10-18 — gerado por gbq-estilo

Auditoria de estilo da onda 4 do reforço (D-REFORCO-2, regras 5 e 6; T98_reconciliacao_2026-10-18.md, seção 7). Destino: gce-gerencia, que fecha a T-98.

Referências: regras/estilo_banca.md v1.1.3 (tipologia E1–E6 e C1–C6; marcadores, seção 4; extensão da base: C média 31,6, de 8 a 65; E média 34,7, de 19 a 62); saida/banco/estilo_onda_3.md (recomendações 1 a 8 da seção 5); registros O-1 a O-8 (T93_reconciliacao).

Objeto, lido em modo somente leitura: saida/gce/L3_reforco_onda4_A_v3.md, L3_reforco_onda4_B_v2.md e L3_reforco_onda4_C_v3.md (84 itens, L3-R12 a L3-R95) e, como item fixo fora do sorteio, o L2-R131 de saida/gce/L2_reforco_onda3_saldo_v2.md (T-105). Nenhum item foi alterado nem reescrito.

**Resultado:** 9 itens sorteados auditados: 5 CONFORMES, 4 CONFORMES COM RESSALVA, 0 NÃO CONFORMES (0%). Não há GATE. Item fixo L2-R131: CONFORME (não condicionante, fora da taxa). Gabarito da onda por contagem própria: 42 C / 42 E = 50,0%. CONFERE com a reconciliação e está dentro da faixa de 40% a 60% (regra 5).

## 1. Amostra e critério

- **Universo:** 84 ids, extraídos por script (`python3 -I`) dos enunciados e do gabarito comentado dos três finais. Os 84 têm gabarito; nenhum id falta.
- **Folhas:** 3.1 R12–R25; 3.2 R26–R39; 3.3 R40–R53; 3.4 R54–R67; 4.2 R68–R81; 4.3 R82–R95 (14 ids novos por folha).
- **Sorteio reproduzido:** `rng = random.Random(20261098)`; um `rng.choice` por folha, na ordem acima, sobre os ids em ordem crescente; depois `rng.sample(restantes, 3)` sobre os 78 restantes em ordem crescente.
  - etapa 1: L3-R16 (3.1), R26 (3.2), R42 (3.3), R55 (3.4), R72 (4.2), R95 (4.3);
  - etapa 2: R81, R62, R64.
  - CONFERE com a seção 7 da reconciliação (mesmos 9 ids). A semente mudou em relação à onda 3 (rec. 8 cumprida).
- **Composição:** 4 C (R16, R42, R62, R95) e 5 E (R26, R55, R64, R72, R81); [TS] em 7 (R42 e R62 espelho em C; os 5 E). Cobre as 6 folhas e as 3 partes (A 2, B 4, C 3).
- **Item fixo:** L2-R131 — saldo da onda 3 (D-T105-SALDO-ACEITE), fora do sorteio e da taxa.

Critérios de estilo (os mesmos das ondas 1 a 3): comando "Julgue o item"; uma afirmação e um só ponto de erro; mecanismo reconhecível na tipologia; [TS] de troca única ou espelho declarado; marcadores que não denunciam o gabarito; extensão dentro do observado (O-1); cenário que pese no juízo (rec. 4 da onda 3); nenhuma pista textual que entregue a resposta. Os registros O-1 a O-8 são critério, não regra de reprovação. NÃO CONFORME seria: dois pontos de erro, [TS] com mais de uma troca, pista que entrega o gabarito, ou mecanismo sem paralelo na tipologia.

## 2. Vereditos por item

Palavras: só o enunciado, sem o comando.

| id | folha | gab. | mecanismo (estilo_banca) | marcadores | palavras | veredito | motivo |
|---|---|---|---|---|---|---|---|
| L3-R16 | 3.1 | C | C1 em situação hipotética (detecção de alterações em blobs); cenário pesa (a fonte é blob) | "pode", "apenas", ", e não todo o acervo", "pois" | 59 | CONFORME COM RESSALVA | Fiel a "can usually detect and retrieve just the data that has changed. For blob data, change detection is automatic" ("pode" respeita o "usually"). Ressalva: "apenas" e ", e não todo o acervo" duplicam a marca de restrição num C, e o "pois" soma um terceiro marcador — o registro da parte A ("um único restritivo") não confere para este item. É o padrão que a rec. 5 da onda 3 pediu para evitar (R95 e R116 da onda 3). Errata opcional: suprimir ", e não todo o acervo". |
| L3-R26 | 3.2 | E [TS] | E1 (mesmo modelo → mesma dimensão) em moldura E4 ("essa prática é adequada") | "pode", "só exige", "pois" | 55 | CONFORME | Troca única: o erro está na causa ("só exige vetores de mesma dimensão"), que sustenta o juízo de adequação; o resto do cenário é neutro e pesa no juízo. "pois" com causa falsa num E é a forma da base (BQ-0003 é o caso inverso), e há "pois" também em C na onda (R16, R48). |
| L3-R42 | 3.3 | C [TS] (espelho) | C1/par confundível (sumarização de conversas × de texto) | "Segundo", "ao passo que" | 61 | CONFORME COM RESSALVA | Fiel ao trecho ("can operate on both chat text and speech transcripts, which have speakers and their utterances. Text summarization operates using simple text…"). "ao passo que" num C diversifica a construção (3 C / 3 E na onda). Ressalva: o cenário da primeira frase é decorativo — a própria R1 o registrou ao reclassificar para PC —, contra a rec. 4 da onda 3; e o item está no quartil longo dos C. |
| L3-R55 | 3.4 | E [TS] | E3/E6 (facultativo convertido em condição: "só pode ser usada se … informar previamente a lista") | "Segundo", "só" | 30 | CONFORME | Troca única (lista opcional → exigência prévia), fiel ao par de trechos ("without you having to specify a language code"; "you can optionally provide"). Um só restritivo. Curto, sem pista de extensão. |
| L3-R62 | 3.4 | C [TS] (espelho) | C2 (reprodução próxima do README) | "Segundo" | 27 | CONFORME | Depois da supressão de ", e não em um corpus multilíngue" (R1), uma afirmação só, literal ("trained on the BrWaC … a large Portuguese corpus"). Observação: C curto e de memória factual; discriminação moderada, compensada pelo espelho plausível (corpus multilíngue). |
| L3-R64 | 3.4 | E [TS] | E2 (inversão do par métrica × tarefa: Pearson/STS ↔ F1/NER) | "ao passo que" | 36 | CONFORME | Um mecanismo só (troca dentro do par), como o L2-R89 da onda 3; as duas orações ficam falsas por efeito da mesma inversão, não por dois erros independentes. A aderência PARCIAL não é matéria de estilo. |
| L3-R72 | 4.2 | E [TS] | E1 (troca de sujeito: Estado → sucessores do autor) | "De acordo com", ", e não ao Estado" | 29 | CONFORME | Troca única do art. 24, § 2º. O contraste final nomeia o sujeito correto num E, forma que a onda 3 marcou como pista quando concentrada; na onda 4 ela está equilibrada (3 C / 3 E, seção 4), e o efeito é neutro. |
| L3-R81 | 4.2 | E [TS] | E2 (inversão de polaridade: "pode variar" → "é uniforme") com conclusão derivada | "Conforme", "ainda que", "razão pela qual", "dispensa" | 61 | CONFORME COM RESSALVA | O erro de base é um só (uniformidade), e a conclusão ("dispensa a verificação por grupos") decorre dele; por isso não se conta como segundo erro. Ressalva: (i) a cadeia premissa falsa + conclusão falsa dobra a superfície de recurso; (ii) "uniforme" e "dispensa" são termos fortes que, somados à concessiva, inclinam a leitura para E — discriminação baixa; (iii) o cenário ("sessões da Câmara") é cauda decorativa, embora o mapa o classifique como aplicação parlamentar. A concessiva tem contraste real (rec. 3 cumprida). |
| L3-R95 | 4.3 | C | C1 em situação hipotética (dever de registro, art. 37 da LGPD) | "Nessa situação, segundo", "tanto … quanto" | 62 | CONFORME COM RESSALVA | Uma afirmação, fiel ao art. 37; sem [TS], o que é admissível em C. Ressalva: o cenário (contratada que trata dados em nome da Câmara) não pesa no juízo, porque o dever vale para os dois agentes qualquer que seja a qualificação; a moldura "Nessa situação, segundo a Lei…" repete-se em 10 itens da onda, 9 deles na parte C (seção 4), versão da moldura que a rec. 4 da onda 3 pediu para variar. Extensão no topo dos C da amostra. |
| **L2-R131 — saldo da onda 3** | 2.4 | E [TS] | E1 (troca do conteúdo do campo: trechos de fala contínua → pausas) em moldura verdadeira (oração de items correta) | — | 50 | CONFORME (não condicionante) | Troca única na segunda oração coordenada; a primeira ("items, com dados de cada palavra e de cada sinal de pontuação") é literal e verdadeira, sem segundo erro. Observação: a ambientação "de uma reunião de comissão" é decorativa; risco baixo. |

Taxa de NÃO CONFORME da amostra: 0/9 = 0%, abaixo do gate de 30%. Ressalvas em 4/9 (R16, R42, R81, R95); nenhuma exige mudança de gabarito.

## 3. Faixa de C da onda (regra 5), por contagem própria

| parte | arquivo | itens | C | E | %C |
|---|---|---|---|---|---|
| A (3.1–3.2) | L3_reforco_onda4_A_v3.md | 28 | 14 | 14 | 50,0 |
| B (3.3–3.4) | L3_reforco_onda4_B_v2.md | 28 | 14 | 14 | 50,0 |
| C (4.2–4.3) | L3_reforco_onda4_C_v3.md | 28 | 14 | 14 | 50,0 |
| Onda 4 | 3 arquivos | 84 | 42 | 42 | 50,0 |

- CONFERE com a reconciliação (42 C / 42 E). Por folha: 7 C / 7 E nas seis folhas.
- [TS] por contagem própria: 61 (CONFERE). Em C (espelho), 19: R13, R24, R30, R39, R40, R42, R45, R50, R52, R54, R56, R58, R61, R62, R65, R76, R77, R84, R92.
- O L2-R131 (E) não entra nesta contagem (saldo da onda 3).

## 4. Conferências da seção 7 e recomendações da onda 3

Método: expressão regular sem distinção de maiúsculas sobre o enunciado dos 84 itens; um item conta uma vez. AVISO da seção 4 do estilo_banca: nenhum marcador decide o gabarito.

| ponto | situação na onda 4 | avaliação |
|---|---|---|
| Extensão C × E (O-1) | C: média 47,1, mediana 49, de 27 a 74. E: média 42,9, mediana 42,5, de 23 a 62. Por parte (C × E): A 52,4 × 47,7 (+4,7); B 40,6 × 35,9 (+4,7); C 48,1 × 45,1 (+3,0). Único C acima de 65: R80 (74), situação hipotética de duas frases. | CONFERE com a seção 7 (A +4,7; B 40,6 × 35,9). REGISTRO: C mais longo que E nas três partes (4,2 palavras na onda, contra 1,0 na onda 3), o inverso da base (31,6 × 34,7); é o sinal que o O-1 pediu para não criar. O R80 cabe na exceção do O-1 (duas frases), mas é o C mais longo das quatro ondas auditadas. Na amostra, os C longos são R16 (59), R42 (61) e R95 (62). Sem efeito; na onda 5, aparar C e escrever E longos. |
| Rec. 1: contraste ", e não …" | C 3 (R13, R16, R92); E 3 (R31, R33, R72). | CUMPRIDO (na onda 3, 4 C / 10 E). |
| Rec. 2: "independentemente" e abertura "Segundo" | "independentemente": C 1 (R74), E 1 (R25). Abertura "Segundo / De acordo com / Conforme": C 16, E 17. Parte B: abertura "Segundo" em 10 itens (6 C, 4 E). | CUMPRIDO. A contagem de 10 da parte B CONFERE; a repetição é de forma, sem pista de gabarito. |
| Rec. 3: concessiva também em E | "ainda que": C 2 (R60, R68), E 5 (R21, R47, R59, R81, R83); "embora": E 1 (R35); "mesmo que": 0. Concessiva em E nas três partes. | CUMPRIDO; a distribuição agora pende para E (6:2) — na onda 5, equilibrar. Concessivas sem contraste real: R47 ("Ainda que o serviço forneça os modelos… o modelo é treinado com os dados do usuário": a concessão não se opõe à principal) e R60 ("ainda que se trate de recurso opcional": contraste fraco); R59 ("Ainda que fale principalmente em português, ele insere palavras em inglês") tem contraste, mas forçado. CONFERE o registro da seção 7. Errata textual opcional (D1), sem mudança de gabarito. |
| Rec. 4: molduras formulares; cenário que pese | "o revisor deve considerar" e "Uma equipe…": 0. "Nessa situação": C 6 (R74, R77, R80, R86, R89, R95), E 4 (R57, R73, R75, R94) — 9 na parte C, quase sempre "Nessa situação, segundo a Lei n.º …". Pares de moldura: R17 × R18 (mesma abertura literal "No enriquecimento por IA de transcrições de sessões feito pelo Azure AI Search"); R50 × R51 ("minuta de ata gerada automaticamente" + "segundo o Regimento Interno"); R19 × R23 ("notas taquigráficas de um acervo"); R74 × R80 ("sobre o uso de inteligência artificial na transcrição de sessões" + "Nessa situação, segundo a Lei n.º 9.610/1998"). | PARCIALMENTE CUMPRIDO. As molduras da onda 3 sumiram, mas a parte C criou uma nova ("Nessa situação, segundo a Lei…", 9 itens). Os quatro pares CONFEREM com a seção 7; em três deles os gabaritos se opõem (R17 E × R18 C; R50 C × R51 E; R19 E × R23 C) e no quarto ambos são C (R74, R80); não há pista, mas os pares não devem cair no mesmo simulado sem variação de abertura. Cenário decorativo na amostra: R42, R95 e a cauda do R81. |
| Rec. 5: um restritivo por item | Duplos encontrados: R16 (C: "apenas" + ", e não todo o acervo") e R90 (E: "pode apenas recomendar …, sem poder determiná-la"). | PARCIALMENTE CUMPRIDO. O R90 CONFERE com a seção 7; o R16 é achado desta auditoria (a parte A o declarou com um restritivo só). Errata opcional nos dois. |
| Rec. 6: dado do teste fora do enunciado | Nenhum item da amostra dá equivalência ou conta pronta. | CUMPRIDO na amostra (registro da parte A não contestado). |
| Rec. 7: discriminação dos C genéricos | R23 (C de enumeração dos quatro estágios da consulta) fora da amostra; lido: uma afirmação de lista, sem contraste nem ressalva. Na amostra, R62 (memória factual) é o C de menor discriminação. | Registro CONFERE para o R23; sem defeito de estilo. A rec. 7 avançou (C com ressalva fina, R16; com contraste, R42), mas os C de lista persistem. |
| Rec. 8: semente | 20261098, distinta da 20261018. | CUMPRIDO. |
| Outros marcadores (O-3, O-7) | "pode/podem/poderá": C 14, E 8 (64% C). "apenas": C 6, E 4. "só": C 1, E 3. "somente": C 1, E 0. "todo/toda(s)": C 2, E 5. "qualquer": C 1, E 2. "pois": C 2, E 1. "porque": C 3, E 0. "ao passo que": C 3, E 3. "tanto … quanto": C 1 (R95). "sempre", "nunca", "prioritariamente", "mesmo que", "exclusiv-": 0. | Restritivos e causais nos dois gabaritos. "pode" segue com viés para C (62% na onda 3, 64% aqui) e "porque" aparece só em C (3/0); "todo/toda" pende para E (5/2). Sem efeito; nenhum marcador decide o gabarito. |

## 5. Encaminhamento

- **À gce-gerencia:** a auditoria da seção 7 está concluída sem GATE (0/9 NÃO CONFORME; 4 ressalvas; L2-R131 CONFORME, não condicionante; faixa de 50,0% conferida; [TS] 61 conferido). A T-98 pode seguir pela ordem da seção 10 da reconciliação. Nenhum defeito exige errata; são opcionais, como errata textual (D1), sem mudança de gabarito: suprimir ", e não todo o acervo" no R16; reduzir a um restritivo o R90; dar contraste real ou retirar a concessiva no R47 e no R60.
- **Recomendações à onda 5 (T-99), sem efeito sobre os 84 itens:**
  1. inverter o sinal da extensão: C mais curtos, alguns E longos (diferença atual de +4,2 palavras para C, nas três partes);
  2. variar a moldura "Nessa situação, segundo a Lei…" (9 itens na parte C) e não abrir dois itens vizinhos com a mesma frase (R17 × R18, R74 × R80);
  3. fazer o cenário pesar no juízo, ou dispensá-lo (R42, R95, cauda do R81);
  4. um restritivo por item, também em C (R16, R90);
  5. equilibrar as concessivas (agora 2 C / 6 E) e usá-las só com contraste real (R47, R60);
  6. evitar a cadeia premissa falsa + conclusão falsa com termos fortes ("uniforme", "dispensa") num mesmo E (R81);
  7. continuar a subir a discriminação dos C de lista ou de memória factual (R23, R62).
- A incorporação destes registros a uma v1.1.4 do estilo_banca continua opção da GBQ, em tarefa própria.

AVISO: os vereditos e a atribuição de mecanismo são julgamento deste agente (gbq-estilo) e exigem revisão da GBQ. As contagens de C/E, [TS], extensão e marcadores vêm de script sobre os arquivos finais (`python3 -I`, somente leitura), com revisão manual só dos casos citados. O sorteio é reproduzível com a semente e o procedimento da seção 1. A fidelidade às bases foi lida nos trechos literais transcritos no gabarito comentado; nenhuma página foi reaberta nesta auditoria (matéria da QA e do qa-normativo).
