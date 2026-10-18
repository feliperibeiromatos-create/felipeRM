# estilo_onda_3.md — T-97 — 2026-10-18 — gerado por gbq-estilo

Auditoria de estilo da onda 3 do reforço (D-REFORCO-2, regras 5 e 6; T97_reconciliacao_2026-10-18.md, seção 8). Ciclo 2026-10-18 s12c4. Destino: gce-gerencia, que fecha a T-97.

Referências: regras/estilo_banca.md v1.1.3 (tipologia E1–E6 e C1–C6; marcadores, seção 4; recomendações, seção 5); saida/banco/estilo_onda_1.md; saida/banco/estilo_onda_2.md (O-1 a O-8 e recomendações 1 a 7 da seção 5); D-REFORCO-2 (regras 5 e 6); D-T103-SALDO-ACEITE.

Objeto, lido em modo somente leitura: saida/gce/L2_reforco_onda3_A_v3.md, B_v3.md, C_v3.md e D_v3.md (111 itens, L2-R19 a L2-R130, sem o L2-R67) e, como item fixo fora do sorteio, o L1-R131 de saida/gce/L1_reforco_onda2_saldo_v2.md. Nenhum item foi alterado nem reescrito.

**Resultado:** 12 itens sorteados auditados, 12 APROVADOS e 0 REPROVADOS (0%). Não há GATE. Item fixo L1-R131 — saldo da onda 2: APROVADO (não condicionante, fora da taxa). Gabarito da onda por contagem própria: 56 C / 55 E = 50,5% de C. CONFERE com o esperado e está dentro da faixa de 40% a 60% (regra 5).

## 1. Amostra e critério

- **Universo:** 111 ids, extraídos por script (`python3 -I`) da Parte 2 (enunciado) e da Parte 3 (gabarito) dos quatro v3. Todos os 111 têm gabarito; o L2-R67 não aparece em nenhum arquivo; os 111 enunciados usam "Julgue o item."
- **Folhas:** pela faixa de numeração da seção 7 da reconciliação, 14 ids por folha a partir do L2-R19 (2.1 R19–R32; 2.2 R33–R46; 2.3 R47–R60; 2.4 R61–R74 sem R67, 13 ids; 2.5 R75–R88; 2.6 R89–R102; 2.7 R103–R116; 2.8 R117–R130).
- **Tamanho:** 10% de 111 = 11,1; a seção 8 fixou 12.
- **Sorteio estratificado, semente registrada:** `rng = random.Random(20261018)`.
  1. Um item por folha, de 2.1 a 2.8, nessa ordem, com `rng.choice` sobre os ids da folha em ordem crescente.
  2. Depois, `rng.sample(restantes, 4)` entre os 103 restantes, listados em ordem crescente.
- **Amostra:**
  - etapa 1: L2-R32 (2.1), R45 (2.2), R50 (2.3), R66 (2.4), R87 (2.5), R90 (2.6), R116 (2.7), R124 (2.8);
  - etapa 2: R34 (2.2), R89 (2.6), R95 (2.6), R129 (2.8).
- **Nota de reprodutibilidade:** os números sorteados coincidem com os da onda 2 (L1-R32, R46…), porque a semente, o procedimento e a estrutura de 14 ids por folha com um id a menos são os mesmos; a única diferença é a folha com 13 ids (2.4 aqui, 1.2 lá), que muda o sorteio de 2.2 (R45) e da etapa 2. A semente foi a pedida pela tarefa; registra-se o efeito para que a GBQ decida se, na onda 4, a semente muda (ex.: 20261019).
- **Composição:** 8 C e 4 E; [TS] em 6 (R45 e R116 espelho em C; R50, R89, R95, R129 em E). Cobre as 8 folhas e as 4 partes (A 3, B 2, C 4, D 3).
- **Item fixo:** L1-R131 — saldo da onda 2 (D-T103-SALDO-ACEITE), fora do sorteio e da taxa.

Critérios de estilo (os mesmos das ondas 1 e 2): comando "Julgue o item"; uma afirmação e um só ponto de erro; mecanismo reconhecível na tipologia; [TS] coerente com a convenção (O-6); marcadores que não denunciam o gabarito; extensão dentro do observado (O-1); nenhuma pista textual que entregue a resposta. Os registros O-1 a O-8 são critério, não regra de reprovação.

## 2. Vereditos por item

Palavras: só o enunciado, sem o comando.

| id | folha | gab. | mecanismo (estilo_banca) | palavras | veredito | motivo |
|---|---|---|---|---|---|---|
| L2-R32 | 2.1 | C | C1 em situação hipotética (competência do Derep em reunião de comissão) | 42 | APROVADO | Uma afirmação, fiel ao art. 2º, I. Observação: a primeira frase ("…é reunião de comissão") já resolve a subsunção, e o juízo restante é a competência genérica do Derep; discriminação baixa (família dos C genéricos, rec. 7 da onda 2). |
| L2-R45 | 2.2 | C [TS] (espelho) | C3 (competência condicionada que parece trocada) | 30 | APROVADO | Ponto único (o registro "quando solicitado pela Secretaria-Geral da Mesa"), espelho declarado. Curto, sem pista de extensão. |
| L2-R50 | 2.3 | E [TS] | E1 (troca de conceito vizinho: Presidente → Mesa Diretora) | 46 | APROVADO | Uma troca só; a oração final ("medida que impede o registro…") é verdadeira e não cria segundo erro. Observação: usa a moldura formular "o revisor deve considerar que", registrada pela QA (seção 4). |
| L2-R66 | 2.4 | C | C1 (descrição de campo de pesquisa), VOLÁTIL baixo | 48 | APROVADO | Fiel à página "Como pesquisar". Observação: são dois predicados coordenados ("pode ser usada como critério, e cada fase caracteriza…"); num C não há ponto de erro, mas a conjunção dobra a superfície de recurso. Está na lista de C de baixa discriminação da QA, o que se confirma: o primeiro predicado é intuitivo. |
| L2-R87 | 2.5 | C | C1 (função de coluna documentada: DisplayAs) | 43 | APROVADO | Uma afirmação, remissão nomeada ("Segundo a documentação do Amazon Transcribe"); o E vizinho (Phrase) fica fora do texto, sem eco. |
| L2-R90 | 2.6 | C | C1 com cálculo (NP) | 46 | APROVADO | Conta correta (12.500.000 × 100 ns = 1,25 s). Observação: o enunciado dá a equivalência do tick, de modo que o item mede aritmética e não o conhecimento da documentação; baixa discriminação, como a QA registrou (mesma família do L1-R68 da onda 2). |
| L2-R116 | 2.7 | C [TS] (espelho) | C3 (restritivo verdadeiro: "só … em todos os cenários, e não apenas em alguns") | 50 | APROVADO | Fiel a "A model is considered better only when it shows significant improvements … in all scenarios". Diversifica restritivos em C (O-7). Observação: três restritivos empilhados ("só", "todos", "e não apenas") num C podem atrair a leitura "absoluto = E" — é o mecanismo pretendido (C3), mas a densidade é alta; um restritivo bastaria. |
| L2-R124 | 2.8 | C | C1/par confundível (dados de treinamento × ajuste) | 45 | APROVADO | Fiel aos trechos literais ("not required"; "recommended when you lack in-domain training data"). Observação: "ao contrário dos dados de treinamento" sugere, sem afirmar, que estes são obrigatórios; o item não depende disso. |
| L2-R34 | 2.2 | C | C2 (recomendação documentada reproduzida) | 46 | APROVADO | Fonte nomeada (rec. 4 da onda 2 cumprida). Observação: boa prática intuitiva; discriminação baixa. |
| L2-R89 | 2.6 | E [TS] | E2 (inversão de relação: separadores SRT × WebVTT) | 46 | APROVADO | Um só mecanismo (inversão do par), "ao passo que" sem se denunciar. A abertura "Um revisor importa…" é ambientação neutra. |
| L2-R95 | 2.6 | E [TS] | E6 (regra geral convertida em restrita: "somente para o formato SubRip, e não para o WebVTT") | 42 | APROVADO | Ponto único, fiel à base ("applies to both WebVTT and SubRip"). Observação: "somente" + "e não" duplicam a marca de restrição num E; "somente" está 3 E / 1 C na onda (seção 4) — convém um restritivo só. |
| L2-R129 | 2.8 | E [TS] | E1 (troca de espécie de emenda: modificativa → aditiva) | 44 | APROVADO | Troca única, o resto reproduz o § 8º do art. 118. A ambientação ("Ao revisar uma nota taquigráfica sobre emendas…") é decorativa, mas fica fora do escopo da remissão (rec. 6 da onda 2 cumprida). |
| **L1-R131 — saldo da onda 2** | 1.2 | E [TS] | E2 (inversão de relação: complementares → excludentes) | 40 | APROVADO (não condicionante) | Troca única depois do ajuste da R1 (oração E4 suprimida); fiel ao README ("Complementary"). Observação 1: usa a moldura "Uma equipe da Câmara… Nessa situação, segundo o README…", e o cenário não interfere no juízo (decorativo). Observação 2: "excludentes" é termo forte que, sozinho, inclina a leitura para E; risco baixo. |

Taxa de reprovação da amostra: 0/12 = 0%, abaixo do gate de 30%.

## 3. Faixa de C da onda (regra 5), por contagem própria

| parte | arquivo | itens | C | E | %C |
|---|---|---|---|---|---|
| A (2.1–2.2) | L2_reforco_onda3_A_v3.md | 28 | 14 | 14 | 50,0 |
| B (2.3–2.4) | L2_reforco_onda3_B_v3.md | 27 | 14 | 13 | 51,9 |
| C (2.5–2.6) | L2_reforco_onda3_C_v3.md | 28 | 14 | 14 | 50,0 |
| D (2.7–2.8) | L2_reforco_onda3_D_v3.md | 28 | 14 | 14 | 50,0 |
| Onda 3 | 4 arquivos | 111 | 56 | 55 | 50,5 |

- CONFERE com o esperado (56 C / 55 E = 50,5%) e com a seção 7 (A 14/14, B 14/13, C 14/14, D 14/14). Com o L1-R131 (E, onda 2), a onda 2 fica 56/112 = 50,0% (D-T103-SALDO-ACEITE); o L2-R131 (onda 3, saldo) não foi contado aqui (seção 8: vai à amostra da onda 4).
- C/E por folha (novos): 7/7 em 2.1, 2.2, 2.3, 2.5, 2.6, 2.7 e 2.8; 7/6 em 2.4. CONFERE.
- [TS] por contagem própria: 69 (CONFERE). Em C (espelho), 15: R26, R37, R39, R45, R48, R58, R81, R83, R92, R102, R107, R113, R116, R119, R126 (CONFERE com "15 C espelho").

## 4. Correções pedidas na onda 2 e registros das QAs

Método: expressão regular sobre o enunciado dos 111 itens; contagem por item (um item conta uma vez). AVISO da seção 4 do estilo_banca: nenhum marcador decide o gabarito.

| ponto | situação na onda 3 | avaliação |
|---|---|---|
| Rec. 1 (onda 2): "independentemente" também em E | C 2 (R92, R118); E 4 (R20, R53, R85, R125). Na onda 2 era 4 C / 0 E. | CUMPRIDO. A distribuição agora pende para E (4:2); na onda 4, equilibrar. |
| Rec. 2: "ainda que" também em C (alternar concessiva) | "ainda que": C 4 (R36, R57, R76, R126); E 3 (R64, R84, R109). "embora" e "mesmo que": 0. | CUMPRIDO na onda. Na parte A, a única concessiva é C (R36) e não há concessiva em E — confirma o registro da QA ("concessiva também em E não cumprida na parte A"); sem efeito, porque a onda está equilibrada. |
| Extensão C × E (O-1) | C: média 46,0, mediana 46, de 25 a 62. E: média 45,0, mediana 44, de 27 a 62. Por parte (C × E): A 41,4 × 38,9; B 46,0 × 44,9; C 50,1 × 48,6; D 46,3 × 47,6. Nenhum C passa de 65 palavras. | CUMPRIDO: diferença de 1 palavra na onda. C um pouco mais longo que E nas partes A, B e C (até 2,5 palavras na A), o inverso da base; não é pista relevante. |
| Rec. 3: variar a abertura "Segundo a…" | Abertura "Segundo": C 3 / E 7 (R20, R24, R28, R33, R41, R64, R75 em E). | Repetição contida, mas a abertura pende para E (70%). Registro, sem efeito; na onda 4, abrir C também com "Segundo". |
| Contraste final ", e não …" | C 4 (R26, R39, R94, R116); E 10 (R19, R20, R24, R29, R33, R35, R38, R40, R95, R101). | ACHADO NOVO (registro): a construção "X, e não Y" está 71% em E — é a forma natural da troca de sujeito, mas, repetida, vira pista. Na onda 4, usar o contraste em C (espelho) com a mesma frequência ou dispensá-lo nos E. |
| Moldura "o revisor deve considerar" (R50, R54, R55, R63, R68) | "deve considerar": C 2 (R55, R92), E 3 (R50, R63, R68); o R54 usa a variante "deve ter em conta" (C). | Registro da QA CONFERE. Forma formular, sem pista de gabarito (C 3 / E 3 contando o R54). Variar. |
| Moldura "Uma equipe… Nessa situação, segundo a documentação" (R56, R59, R70, R72, R73) | Aberturas "Uma equipe": C 10, E 7. "Nessa situação": C 11, E 10. A sequência literal "Nessa situação, segundo a documentação": C 2 (R72, R73), E 3 (R56, R59, R70). | Registro da QA CONFERE. Repetição de forma em 17 itens, sem pista de gabarito; o cenário é decorativo na maior parte (também no L1-R131). Variar e fazer o cenário pesar no juízo. |
| C de baixa discriminação (R54, R66, R72, R73, R74, R88, R90, R98) | R66 e R90 estão na amostra: confirmados (seção 2), sem reprovação. | Registro CONFERE. Mesma família dos L1-R32, R34, R68 e R89 da onda 2; a rec. 7 da onda 2 (subir a discriminação dos C genéricos) não foi plenamente atendida. |
| R24 (tensão "revisar × transcrever do zero") | Fora da amostra; lido: E com "consiste em as pessoas transcreverem o áudio do zero, e não em revisarem…". O erro é único e fiel ao trecho ("Have humans review … transcriptions"). | Sem defeito de estilo; a tensão é de base (o que "revisar" abrange), já decidida pela QA. Entra na contagem de ", e não". |
| R40 ("Uma equipe da Casa") | Fora da amostra; "da Casa" aparece também no R78 (C). | Registro: "Casa" é jargão interno; em prova, preferir "da Câmara dos Deputados". Errata textual opcional (D1 da GCE), sem mudança de gabarito. |
| Outros marcadores (O-3, O-7) | "pode/podem/poderá": C 13, E 8. "apenas": C 5, E 2. "somente": C 1, E 3. "só" restritivo: C 1 (R116), E 0. "sempre": C 1, E 0. "qualquer": C 0, E 2. "exclusiv-": C 2, E 1. "todo/toda(s)": C 5, E 4. "pois": C 3, E 2. "porque": C 1, E 1. "nunca", "prioritariamente", "mesmo que": 0. | CUMPRIDO: restritivos e causais nos dois gabaritos; "pode" segue com viés para C (62%), sem efeito. |

## 5. Encaminhamento

- **À gce-gerencia:** a auditoria da seção 8 está concluída sem GATE (0/12; L1-R131 APROVADO, não condicionante; faixa de 50,5% conferida). A T-97 pode fechar pela ordem da seção 11 da reconciliação. Nenhum defeito exige errata; a troca de "da Casa" no R40 (e no R78) é opcional, como errata textual (D1), sem mudança de gabarito.
- **Recomendações à onda 4 (T-98), sem efeito sobre os 111 itens:**
  1. equilibrar o contraste ", e não …" entre C e E;
  2. equilibrar "independentemente" (agora 2 C / 4 E) e a abertura "Segundo" (3 C / 7 E);
  3. pôr concessiva em E em todas as partes;
  4. variar as molduras "o revisor deve considerar" e "Uma equipe… Nessa situação, segundo a documentação", e fazer o cenário pesar no juízo;
  5. um só restritivo por item (R95, R116);
  6. evitar dar no enunciado o dado que o item deveria testar (R90);
  7. subir a discriminação dos C genéricos (R32, R34, R66);
  8. considerar outra semente na onda 4 (seção 1).
- A incorporação destes registros a uma v1.1.4 do estilo_banca continua opção da GBQ, em tarefa própria.

AVISO: os vereditos e a atribuição de mecanismo são julgamento deste agente (gbq-estilo) e exigem revisão da GBQ. As contagens de C/E, [TS], extensão e marcadores vêm de script sobre os arquivos finais (`python3 -I`, somente leitura), com revisão manual só dos casos citados. O sorteio é reproduzível com a semente e o procedimento da seção 1.
