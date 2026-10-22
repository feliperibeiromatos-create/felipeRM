# QA_DA_reforco_leva5_R2_2026-10-22_gcb-cqfp.md — T-116 — 2026-10-22 — gerado por gcb-cqfp

# PARECER QA R2 (ÚLTIMA RODADA) — REFORÇO DA, LEVA 5 (v2) — ciclo s16c3
A gcb-cqfp (opus) faz este QA de forma independente. Ela não produziu o texto revisado e não reescreve itens. Nenhum outro arquivo do repositório foi alterado; não houve commit nem push.

O exame segue:
- a ficha, seção 4.3: "o R2 confere cada AJ aplicado literalmente e examina só o que a v2 mudou além dos AJ";
- o R1, seção 8, itens 1 a 3;
- a ficha, seção 9.3, item 6: os AJ do R1 e da auditoria de estilo vão juntos para a v2 e são conferidos aqui.

Pontos examinados:
- os AJ-1 a AJ-10 do R1 e o AJ-L5-E1 do estilo;
- os 28 itens não alterados;
- a Resposta à R1;
- a seção 4 refeita, inclusive o efeito do AJ-L5-E1 que o R1 não previu;
- os reflexos de texto fora da seção 4;
- as notas (ay) e (bf).

## 0. Objeto, entradas e método
| objeto | SHA-256 (em disco, 22/10/2026) |
|---|---|
| saida/gcb/DA_reforco_leva5_v2.md (objeto do R2; 30 itens; 147.110 bytes; 941 linhas) | b531014bcf2cf158890ffa4293062e796e505151a57dced14e8462875a8f81c4 (= despacho) |
| saida/gcb/DA_reforco_leva5_v1.md (objeto do R1; base do diff; 131.868 bytes; 866 linhas) | 3062f7cecdb62a7037234f30bae87f51b610ec0131c0b6a4eb3a39108254e591 (= despacho e R1) |
| saida/gcb/QA_DA_reforco_leva5_R1_2026-10-22_gcb-cqfp.md | f2374c2de64e561387a801012de198c21e9ee2ef3abcda5a60da300f02d3205a (= despacho) |
| saida/banco/estilo_DA_reforco_leva5.md | 4195f97807e42bee7e8f37e641243fddcaa7ffa08b42e54f0e6a9693adf4f0cf (= despacho) |
| saida/gcb/DA_reforco_ficha_2026-10-20.md | 2e676c62d45487ed5f267f40d8f70d9761e2e67534991aa9564a9550c88a4899 (= despacho) |
| saida/gcb/D2_anexo_N_mapa_normativo.md | b0a54fff4ddcf21a693e01ba71032efccf72e0a6fdf912221ff05413cc0e340a (= R1) |
| saida/gcb/D2_anexo_N_adendo_2026-10-22.md | abed6f934ca9d8881e9d2c6944de86a453018e90ee9e2a8ac139d876d1a8af61 (= R1) |
| normativo_cache/Lei_8112_1990_compilada_2026-10-20.txt | 72f45d30dcf096207898d143ba551758e3ffac89e87d6dd2d42044fe65202efe (= R1) |
| normativo_cache/Lei_9784_1999_2026-10-20.txt | f9452916c03521a8435caae49c8feb690ae2b02086424b641204374f38f9ae19 (= R1) |
| saida/pacote/pacote.json v1.13 | 82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240 (= R1) |

Também foram lidos:
- da ficha, as seções 4, 7.6, 9.3, 10.2, 10.3, 11.1 a 11.6 (11.4.4 a 11.4.9);
- regras/ e CLAUDE.md.

Modelo de forma: saida/gcb/QA_DA_reforco_leva4_R2_2026-10-22_gcb-cqfp.md.

Método: scripts próprios aj.py, cnt.py e ext.py, em python3 -I, somente leitura, no scratchpad da sessão, fora do repositório.
- (a) Os 11 AJ foram extraídos por regex do texto literal do R1 (seção 4) e do estilo (seção 5), com "\n" lido como LF. Foram aplicados em memória à v1, uma vez cada e na ordem AJ-1 a AJ-10 e AJ-L5-E1. O resultado foi comparado com a v2 por diff.
- (b) Os 30 enunciados (seção 1) e os 30 blocos (seção 2) da v1 e da v2 foram comparados por id. As seções 3 e 4 foram comparadas inteiras.
- (c) Foram refeitos sobre a v2:
  - gabarito e sequência;
  - [TS];
  - formatos por folha e na leva;
  - mecanismos;
  - moldura S;
  - abertura × gabarito e fórmula;
  - lista de SUJ;
  - E com "não", "nem" ou "sem";
  - absolutos por gabarito (L3-2);
  - extensão;
  - linha 1 e última linha.
- (d) O diff residual (v1 + AJ → v2) foi lido linha a linha. Ele tem 14 blocos de diferença: 3 no cabeçalho e na Resposta à R1, e 11 fora dela.

**Rede — reabertura no www.planalto.gov.br (22/10/2026).** Comando: `curl -sS -m 60 -A "Mozilla/5.0"`, com as URLs exatas dos itens e do Anexo N do D2, seção 1. O HTML ficou só no scratchpad.

| hora (UTC) | URL | HTTP | bytes (Anexo) | SHA-256 do HTML |
|---|---|---|---|---|
| 2026-10-22T21:51:02Z | https://planalto.gov.br/ccivil_03/leis/l8112compilado.htm (Fonte 4; D2-R32) | 200 | 343.733 (343.733) | 6bee93db9e2f5aca801b30a43ee31d2a44de0631f1a17aa2f2f53936d7814a2d |
| 2026-10-22T21:51:04Z | https://www.planalto.gov.br/ccivil_03/leis/l9784.htm (Fonte 6; D2-R44) | 200 | 74.941 (74.941) | 258c183363253b4422e1c323fe8aefd3ce31f7b85b4556aa54adf77bd56dc9f9 |
| 2026-10-22T21:51:05Z | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/decreto/d10835.htm (Fonte 7; folha 3.3, só tamanho) | 200 | 71.902 (71.902) | 65759f36ba82b1ccb2e7b918644662d2eb4265b1f96508386e58744dafc2152d |

O SHA do HTML muda a cada download (script de medição; R1, seção 1). A comparação se faz sobre o texto: html.parser, cp1252, tachado excluído, 0 U+FFFD.
- **Lei 8.112:** «Sem qualquer prejuízo, poderá o servidor ausentar-se do serviço» ocorre 1 vez e «por 8 (oito) dias consecutivos em razão de» também 1 vez. Igual à cópia, linhas 481 a 485.
- **Lei 9.784:** «divulgação oficial dos atos administrativos, ressalvadas as hipóteses de sigilo previstas na Constituição» ocorre 1 vez (cópia, linha 24). "regulamento" ocorre 0 vez na página e na cópia.

A reabertura é conferência, não base. A Base dos itens continua a consulta de 20/10/2026 (ficha 11.4.2 e 11.6).

## 1. Veredito geral
- **Leva: APROVADA.**
- Os 2 itens alterados: **D2-R44 APROVADO** (AJ-1 aplicado) e **D2-R32 APROVADO** (AJ-L5-E1 aplicado).
- Os 28 itens não alterados ficam APROVADOS, como no R1. São idênticos aos da v1 no enunciado e no bloco.
- **Reprovação final: 0/30 = 0,0%** (limite 30%). No acumulado do rito (R1 + R2), também 0/30. Sem GATE.
- Itens aprovados no R1 e mudados sem pedido: **nenhum**. O D2-R32 mudou só pelo AJ-L5-E1, pedido pelo estilo e conferido aqui (ficha 9.3, item 6).
- Conferências do despacho:
  - (1) AJ por substituição exata: CONFERE.
  - (2) 28 itens idênticos: CONFERE.
  - (3) resposta item a item: CONFERE.
  - (4) seção 4 refeita: CONFERE.
  - (5) reflexos de texto: CONFERE, com 2 ressalvas de registro (seção 6).
  - (6) notas (ay) e (bf): CONFEREM; a (ay) tem ressalva de escopo.
- **NÃO CONFERE (1 ponto, de registro, sem efeito em item, gabarito, contagem ou aprovação).** A v2 diz, na R.3, que da seção 4 "mudam só estas linhas", e a lista omite uma frase nova no parágrafo de abertura da seção 4 (l. 688). A R.7, item 2, também não a lista. Ver a seção 3.

## 2. Conferência (1) — AJ aplicados por substituição exata, sem efeito colateral
| AJ | item / campo | "substituir" na v1 | "por" na v1 | "substituir" na v2 | "por" na v2 | veredito |
|---|---|---|---|---|---|---|
| AJ-1 | D2-R44 / Formato | 1 | 0 | 0 | 1 | **APLICADO** |
| AJ-2 | seção 0, linha da 4.1 | 1 | 0 | 0 | 1 | **APLICADO** |
| AJ-3 | seção 0, linha da leva | 1 | 0 | 0 | 1 | **APLICADO** |
| AJ-4 | 4.1, linha da 4.1 | 1 | 0 | 0 | 1 | **APLICADO** |
| AJ-5 | 4.6, SUJ | 1 | 0 | 0 | 1 | **APLICADO** |
| AJ-6 | 4.7, linha da 4.1 | 1 | 0 | 0 | 1 | **APLICADO** |
| AJ-7 | 4.7, formatos da leva | 1 | 0 | 0 | 1 | **APLICADO** |
| AJ-8 | 4.7, formatos finais | 1 | 0 | 0 | 1 | **APLICADO** |
| AJ-9 | 4.8, comparação com a ficha | 1 | 0 | 0 | 1 | **APLICADO** |
| AJ-10 | 6.2, item 10 | 1 | 0 | 0 | 1 | **APLICADO** |
| AJ-L5-E1 (estilo) | D2-R32 / enunciado | 1 | 0 | 1, só na tabela da R.2 (l. 27), como citação do "antes" | 2: no item (l. 122) e na R.2 (l. 27) | **APLICADO** |

- Os 11 AJ são distintos. O AJ-L5-E1 não repete texto do R1, porque o item e o campo são outros. A regra "texto igual aplicado uma vez" (ficha 11.3) não se aplica, como a R.2 diz. CONFERE.
- Na cadeia AJ-1 → AJ-10 → AJ-L5-E1, cada "antes" ocorreu 1 vez no texto corrente, e nenhum AJ afetou o "antes" de outro. CONFERE.
- Aplicados os 11 AJ em memória à v1, os 30 enunciados, os 30 blocos e a seção 3 ficam iguais aos da v2. Fora da Resposta à R1, só restam as linhas da seção 3 deste parecer.
- Efeito colateral nos 2 itens: **nenhum**.
  - D2-R44: no bloco, muda só «- Formato: SUJ» → «- Formato: DEF» (16 linhas; 1 diferente). Enunciado, ponto, gabarito E, [TS], Troca, mecanismo E3, moldura N, Base e justificativas ficam como estavam.
  - D2-R32: muda só o enunciado. O bloco da seção 2 é idêntico ao da v1, inclusive APL, moldura S, Troca e justificativas.
- Extensão (script, só o enunciado): D2-R32 vai de 36 para 37 palavras; D2-R44 fica em 31. Iguais à R.2 e ao estilo, seção 5.

## 3. Conferência (2) — os 28 itens não alterados e o que a v2 mudou além dos AJ
**CONFERE quanto aos itens.** Na comparação por id, 29 enunciados e 29 blocos são idênticos aos da v1. Diferem só o enunciado do D2-R32 e o bloco do D2-R44, cada um apenas pelo texto do seu AJ. A seção 3 (proveniência) é idêntica à da v1, byte a byte.

Fora dos itens e dos AJ, o diff residual tem estas mudanças:

| local (v2) | mudança | declarada na v2? |
|---|---|---|
| l. 1, 3, 5 | nome do arquivo, parágrafo de abertura ("Esta é a v2…") e linha de entradas, com a v1, o R1 e o estilo | sim (R.7, item 2) |
| l. 7 a 79 | nova seção "Resposta à R1" | sim |
| **l. 688 (abertura da seção 4)** | frase nova no início: «Refeitas na v2 (rodada de correção) por script sobre este arquivo gravado, depois dos AJ (ver Resposta à R1, R.3).»; o resto do parágrafo é igual | **não** |
| l. 836 (4.6, negação frontal) | «D2-R32: “sem prejuízo”, da letra» → «D2-R32: “sem qualquer prejuízo”, da letra, reposto pelo AJ-L5-E1» | sim (R.3, (c)) |
| l. 845 (4.6, tabela L3-2) | linha nova do D2-R32 (E, "qualquer", literal da fonte, não é a troca) | sim (R.3, (a)) |
| l. 851 (4.6, contagem L3-2) | "E com absoluto literal que não é a troca": 0 → 1 (D2-R32), com "“qualquer” na 3.4: 1 C / 1 E" | sim (R.3, (a)) |
| l. 863 (4.6, palavras) | D2-R32 36 → 37 | sim (R.3, (b)) |
| l. 905 (bloco 5, Arquivo) | v1 → v2 no nome | sim (R.7, item 2) |
| l. 908 (bloco 5, pistas) | (4) acrescenta o D2-R32 como E com absoluto literal; (8) "os dois SUJ com gabarito E" → "o único SUJ com gabarito E (D2-R22) … o D2-R44 passou a DEF" | sim (R.3) |
| l. 911 (bloco 5, notas) | (ay) com a marca "OBRIGATÓRIA pelo R1…"; (bf) nova depois da (be) | sim (R.6 e R.7) |
| l. 912 (bloco 5, dúvidas) | só a dúvida (v) muda: acrescenta «(R1: formato não aceito como estava; AJ-1 aplicado, DEF)» | sim (R.3) |
| l. 917 (6.1) | "nenhum desvio" → "29 de 30 iguais…"; "CONFEREM" → "CONFEREM, salvo os formatos (11.4.5) da leva e da folha 4.1…" | sim (R.3) |
| l. 935, 936, 938 (6.4, itens 1, 2 e 4) | remissões ao resultado do R1; notas "(at) a (bf), com (ay) obrigatória e (bf) nova" | sim (R.3) |

**NÃO CONFERE (registro).** A R.3 diz que da seção 4 "mudam só estas linhas" e lista 4.1, 4.6, 4.7 e 4.8, mais as linhas do AJ-L5-E1. A frase nova da l. 688 fica fora dessa lista e da lista da R.7, item 2.
- A frase é verdadeira: a seção 4 foi refeita por script, e a recontagem desta QA confere (seção 5).
- Não toca item, contagem nem campo que vá ao pacote.json.
- É omissão numa declaração, como o SHA abreviado da leva 4 (R2 da leva 4, seção 6, item 2; ficha 11.3). Não pede errata. A reconciliação registra.

## 4. Conferência (3) — resposta item a item da v2
**CONFERE.** As 8 partes da Resposta à R1 batem com o R1 e com o estilo:
- **R.1:** os números do R1 (29/1/0; 0,0%; 8 de 8) e do estilo (3 CONFORMES, 1 AJUSTE, 0 NÃO CONFORME) estão corretos. Os 11 ajustes foram acatados.
- **R.2:** 11 AJ, todos acatados. Para cada um, "antes" 1 e "depois" 0 na v1, o que confere (seção 2). A interação com o R1 prevista pelo estilo (seção 5) foi lida certo: o R1 aceitou "dez dias", e o "antes" do AJ-L5-E1 continuou a ocorrer.
- **R.3:** as contagens e as mudanças da seção 4 conferem (seção 5), salvo a omissão da l. 688 (seção 3). A R.3 nomeia corretamente as três mudanças que o AJ-L5-E1 causou e que o R1 não previu (absolutos, palavras, negação frontal).
- **R.4:** 30 linhas. Os 28 "mantido" não mudaram de fato. O D2-R32 está descrito como alterado só pelo AJ-L5-E1, e o D2-R44 só no campo Formato.
- **R.5:** mapeia a seção 7 do R1. Os desvios dos D2-R32 e D2-R33 foram aceitos. A dúvida (v) não foi aceita e levou ao AJ-1. A dúvida (vii) foi aceita com a leitura do R1 (cota da 3.4 = 1 E).
- **R.6:** reproduz a seção 8, itens 3 a 6, do R1. A (ay) é obrigatória "para o par D2-R36 × D2-39", o escopo certo. A (bf) é nova.
- **R.7:** os itens 1 a 6 da seção 8 do R1 foram cumpridos. A lista de mudanças além dos AJ (item 2) omite a l. 688 (seção 3).
- **R.8:** as contagens finais conferem (seção 5).

## 5. Conferência (4) — seção 4 refeita, conferida contra o arquivo (script próprio sobre a v2)
| verificação | refeito pela QA | v2 | resultado |
|---|---|---|---|
| gabarito da leva | 16 C / 14 E (53,3%; faixa 12–18) | 16/14 | CONFERE |
| sequência da leva | CEECCCECCE·CEECCCECEE·ECCECCEECE | igual à 4.3, à ficha 11.4.7 e à v1 | CONFERE (nenhum gabarito mudou; o teste da regra 6 fica como no R1) |
| [TS] | 14, todos E; 0 C-isca | 14 / 0 | CONFERE |
| formatos da leva por folha | 3.3 2/2/3/2/1/0; 3.4 1/1/2/1/1/4; 4.1 3/1/2/0/1/3; leva 6/4/7/3/3/7 | iguais (seção 0, 4.7, R.8) | CONFERE |
| formatos da folha final | 4.1: canônicos 3/0/3/0/2/2 + leva 3/1/2/0/1/3 = 6/1/5/0/3/5; DEF 6 = 30,0%, no teto de 6 | iguais (4.1, 4.7) | CONFERE |
| SUJ | D2-R22 (E), R29, R34, R49 (C); SUJ E só o D2-R22 | igual (4.6, AJ-5) | CONFERE |
| mecanismos | C2 10, C3 5, C6 1, E1 4, E3 10 | iguais (R.3) | CONFERE |
| moldura S | 1 C / 6 E (D2-R35 / R32, R37, R39, R41, R47, R50) | igual | CONFERE; DA 50/34 e D2 10/10 como no R1 |
| abertura × gabarito | "Considere que" 7 C / 7 E; declarativos 9 C / 7 E | iguais | CONFERE |
| "Nessa situação, nos termos d…" | 7 dos 14 CQ (D2-R24, R31, R32, R39, R41, R42, R47) | igual | CONFERE (no limite da orientação, ficha 11.4.6) |
| absolutos (L3-2; marcadores da v2, 4.6) | C literal: R25 somente, R31 qualquer, R34 nenhum, R36 somente, R49 ninguém (5); E inserido: R47 vedada (1); **E literal que não é a troca: R32 qualquer (1)** | iguais (tabela e contagem da 4.6) | CONFERE; L3-2 continua cumprida (o R47 tem C literal na 4.1) |
| E com "não", "nem" ou "sem" | D2-R30, R32, R33 | iguais | CONFERE |
| extensão | E de 26 a 56; C de 15 a 53; D2-R32 37 | 30 contagens declaradas = recontadas, 30/30 | CONFERE (L5-1) |
| linha 1 / última linha | "# DA_reforco_leva5_v2.md — T-116 — 2026-10-22 — gerado por gcb-cpp" / "FIM DA LEVA 05 — REFORÇO DA" com LF | — | CONFERE |

**Mudanças que o AJ-L5-E1 causou e que o R1 não previu.** O R1, seção 4, disse que "nenhuma outra contagem muda" com o AJ-1. Isso vale para o AJ-1. Não cobria o AJ-L5-E1, que corria em paralelo e que o R1 não tinha diante de si. A v2 tratou as três mudanças, e as três conferem:
- **(a) Absolutos (L3-2).** "E com absoluto literal que não é a troca" vai de 0 para 1, e a tabela da 4.6 ganha a linha do D2-R32. "C com absoluto literal" continua 5, e "E com absoluto inserido" continua 1. É o efeito que o estilo previu (seção 5).
  - **Observação de escopo, sem efeito:** a frase "“qualquer” na 3.4: 1 C / 1 E", vinda do estilo, vale para os itens da leva. Na folha 3.4 fechada, "qualquer" fica 1 C / 2 E. Entram o D2-R31 (C, literal), o D2-R32 (E, literal) e o canônico D2-36 (E: «poderá ser cedido para ocupar qualquer cargo de provimento em comissão»; pacote v1.13). A L3-2 fica cumprida nas duas leituras, e a série "absoluto literal → C" que o estilo apontou continua quebrada.
- **(b) Extensão.** O D2-R32 vai de 36 para 37 palavras. As faixas da leva não mudam.
- **(c) Negação frontal.** O D2-R32 continua na lista de E com "sem", agora "sem qualquer prejuízo" (letra do art. 97, caput). O "sem" é a moldura da regra literal, e não negação do fecho: o fecho troca o número (10.2, item 5). A conferência continua CONFERE.

Nenhuma contagem fixada pelo R1 (formatos: 4.1 DEF 6 / SUJ 1; leva DEF 6 / SUJ 4) foi alterada pelo AJ-L5-E1.

## 6. Conferência (5) — reflexos de texto fora da seção 4 (acrescentados pela produção)
A pergunta do despacho é se cada reflexo é só consequência dos AJ ou se introduz algo novo. Cada "antes" ocorre 1 vez na v1, conferido no diff. As frases foram lidas inteiras.

| local | leitura | é só consequência? |
|---|---|---|
| bloco 5, pista (4) (l. 908) | acrescenta «E com absoluto literal que não é a troca: D2-R32 (‘qualquer’, reposto pelo AJ-L5-E1)»; o resto é igual | **sim** — efeito direto do AJ-L5-E1; verdadeiro (seção 5) |
| bloco 5, pista (8) (l. 908) | «os dois SUJ com gabarito E usam ator mencionado pela fonte» → «o único SUJ com gabarito E (D2-R22) usa ator mencionado pela fonte, e o D2-R44 passou a DEF pelo AJ-1 do R1» | **sim** — sem a troca, a frase da v1 ficaria falsa depois do AJ-1; a nova é verdadeira |
| bloco 5, dúvida (v) (l. 912) | acrescenta só «(R1: formato não aceito como estava; AJ-1 aplicado, DEF)» ao fim; o texto da dúvida fica | **sim** — remissão ao resultado do R1, sem conteúdo novo |
| seção 6.1 (l. 917) | "nenhum desvio" → "29 de 30 iguais; a diferença é o formato do D2-R44…"; "CONFEREM" → "CONFEREM, salvo os formatos (11.4.5) da leva e da folha 4.1…" | **sim** — o R1 deixou essa regravação à v2 (seção 4, último parágrafo); a ressalva é exata: a ficha 11.4.5 diz 4.1 5/2/5/0/3/5, leva DEF 5 / SUJ 5, "maior formato 25%", e o arquivo diz 6/1/5/0/3/5, DEF 6 / SUJ 4, 30%; a 11.4.6 (incl. "E com absoluto inserido: só o D2-R47") continua verdadeira com o AJ-L5-E1 |
| seção 6.4, item 1 (l. 935) | acrescenta «R1: desvios aceitos» | **sim** — registro do R1, seção 7 |
| seção 6.4, item 2 (l. 936) | «do SUJ do D2-R44» → «do formato do D2-R44», com «R1: pertinência do D2-R35 aceita; D2-R44 passa a DEF pelo AJ-1» | **sim** — registro do R1, seções 2 e 7 |
| seção 6.4, item 4 (l. 938) | «(at) a (be)» → «(at) a (bf), com (ay) obrigatória e (bf) nova (sem decisão da produção)» | **sim**, com a mesma ressalva de escopo da (ay) (abaixo) |
| seção 4.6 (l. 836, 845, 851, 863) | negação frontal, linha e contagem de L3-2, palavras | **sim** — seção 5 deste parecer |
| seção 4, abertura (l. 688) | frase "Refeitas na v2…" | **sim** no conteúdo; **não declarada** (NÃO CONFERE de registro, seção 3) |

Conclusão: **nenhum reflexo introduz conteúdo novo** de item, de regra ou de contagem. Todos são consequência do AJ-1 ou do AJ-L5-E1, ou registro do resultado do R1. As ressalvas são de registro:
1. A l. 688 não foi declarada (seção 3).
2. A marca de obrigatoriedade da (ay) tem escopo literal mais largo que o do R1 (item 1 abaixo).

**Notas (ay) e (bf): CONFEREM** (bloco 5, l. 911; 6.4, item 4; R.6).
1. **(ay).** A nota da ficha 11.4.9 (D2-R36 × D2-31, D2-36 e D2-39) foi mantida e ganhou a marca «— OBRIGATÓRIA pelo R1: o rol fechado do art. 20, § 4º, afirmado no D2-R36 (C), entrega o E do D2-39 (art. 91, licença para trato de assuntos particulares no estágio); a produção a registra e não decide por ela».
   - O motivo é o do R1. A descrição do D2-39 confere com o pacote v1.13 («requeira licença para o trato de assuntos particulares») e com a Lei 8.112, art. 91 (cópia, l. 426).
   - **Ressalva de escopo, sem efeito em item.** O R1 (seções 2 e 8.3) fez obrigatório só o par D2-R36 × D2-39, e a R.6 (1) da v2 diz o mesmo. No bloco 5 e na 6.4, item 4, a marca está posta na nota inteira, que também lista D2-31 e D2-36.
   - Leitura desta QA, para a reconciliação: obrigatório é o par D2-R36 × D2-39. D2-R36 × D2-31 e × D2-36 ficam como nota comum da ficha 11.4.9. A leitura mais larga é só mais restritiva no simulado e não cria conflito. A GCB decide.
2. **(bf).** A nota nova D2-R47 × D2-R50 foi posta depois da (be), com o texto e o motivo do R1, seção 8.3 (mesma cena-tipo, mesmo esqueleto de fecho; a (be) sozinha não os separa). Vem marcada "sem decisão da produção". CONFERE.
3. As demais notas, (at) a (be), (w), (x) e os acréscimos da produção, são idênticas às da v1. Só a (ay) muda e só a (bf) entra.

**Registros fora do objeto, sem veredito e sem efeito.**
- Bloco 5, l. 909: a v2 manteve «Auditoria sobre esta v1». O fato é verdadeiro (a auditoria foi feita sobre a v1), mas "esta" agora designa a v2. Não é reflexo de AJ. A ficha 10.3 veda harmonizar rótulos do bloco à GCB depois do R2.
- D2-R44, Base, nota (bloco idêntico à v1 salvo o Formato): «o regulamento do órgão é ator plausível, que o dispositivo não menciona como fonte da ressalva». "Ator" é vocabulário do SUJ. A afirmação é verdadeira ("regulamento": 0 na cópia e na página de 22/10), e o R1 não pediu mudar a Base. Fica como está.

## 7. Veredito por item (os 2 alterados)
| id | folha | gab. | [TS] | enunciado da v2 (lido inteiro) | base (cópia; página de 22/10) | veredito | nota |
|---|---|---|---|---|---|---|---|
| D2-R32 | 3.4 | E | sim | «Considere que servidor de órgão do Poder Legislativo da União tenha contraído casamento. Nessa situação, nos termos da Lei nº 8.112/1990, ele poderá ausentar-se do serviço, sem qualquer prejuízo, por dez dias consecutivos em razão do casamento.» | Lei 8.112, art. 97 (l. 481 e 484–485): «Sem qualquer prejuízo, poderá o servidor ausentar-se do serviço: … III - por 8 (oito) dias consecutivos em razão de : a) casamento»; 1 ocorrência na página de 22/10 | **APROVADO** | Uma só troca, oito → dez dias (E3); o desvio foi aceito no R1. "Sem qualquer prejuízo" é letra do caput e é verdadeiro. Não cria segundo ponto de erro nem pista: o absoluto literal agora está também em E, como o estilo pediu (estilo_banca 5.1). A moldura não decide: o cenário só põe o servidor em órgão do Legislativo da União, e o fecho é neutro. A abertura CQ e a fórmula continuam (7 de 14). 37 palavras, dentro de 19 a 62. A justificativa, linha 1, já trazia "sem qualquer prejuízo" e fica literal ao enunciado. Bloco idêntico à v1. |
| D2-R44 | 4.1 | E | sim | «Entre os critérios a serem observados nos processos administrativos regidos pela Lei nº 9.784/1999 consta a divulgação oficial dos atos administrativos, ressalvadas as hipóteses de sigilo previstas em regulamento do órgão.» (igual à v1) | Lei 9.784, art. 2º, parágrafo único, V (l. 24): «divulgação oficial dos atos administrativos, ressalvadas as hipóteses de sigilo previstas na Constituição»; 1 ocorrência na página de 22/10; "regulamento" 0 | **APROVADO** | Formato DEF, pelo AJ-1. A troca é do instrumento que prevê o sigilo (Constituição → regulamento do órgão), como no D2-R04 da leva 4. O gabarito E sai da letra, e há um só ponto. Com DEF, a 10.2, item 6, não se aplica mais. A 4.1 fica com DEF 6 de 20, no teto de 6 (regra 4). Ponto, enunciado, Troca, E3, moldura N e Base não mudaram. Nota (be) mantida. |

## 8. Tabela-resumo dos 30 itens (v2)
| id | folha | ponto | gab. | [TS] | formato | moldura | aderência | R1 | R2 |
|---|---|---|---|---|---|---|---|---|---|
| D2-R21 | 3.3 | Decreto 10.835, art. 9º, § 4º | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico à v1) |
| D2-R22 | 3.3 | Decreto 10.835, art. 29, caput | E | sim | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R23 | 3.3 | Lei 6.999, art. 3º, caput | E | sim | NUM | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R24 | 3.3 | Lei 6.999, art. 9º | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R25 | 3.3 | Lei 6.999, art. 3º, § 3º | C | não | NUM | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R26 | 3.3 | Decreto 10.835, art. 30-A, III | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R27 | 3.3 | Decreto 10.835, art. 9º, § 5º, II, e § 6º | E | sim | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R28 | 3.3 | Decreto 10.835, art. 10 | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R29 | 3.3 | Decreto 10.835, art. 1º, § 1º, III | C | não | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R30 | 3.3 | Lei 6.999, art. 4º, caput | E | sim | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R31 | 3.4 | Lei 8.112, art. 49, § 1º | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R32 | 3.4 | Lei 8.112, art. 97, III, a | E | sim | APL | S | direta | APROVADO | **APROVADO** (AJ-L5-E1 aplicado) |
| D2-R33 | 3.4 | Lei 8.112, art. 46, § 1º | E | sim | NUM | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R34 | 3.4 | Lei 8.112, art. 41, § 5º | C | não | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R35 | 3.4 | Lei 8.112, art. 76 | C | não | APL | S | direta | APROVADO | APROVADO (idêntico) |
| D2-R36 | 3.4 | Lei 8.112, art. 20, § 4º | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico; nota (ay) obrigatória com o D2-39) |
| D2-R37 | 3.4 | Lei 8.112, art. 87, caput | E | sim | APL | S | direta | APROVADO | APROVADO (idêntico) |
| D2-R38 | 3.4 | Lei 8.112, art. 30 | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R39 | 3.4 | Lei 8.112, art. 77, caput | E | sim | APL | S | direta | APROVADO | APROVADO (idêntico) |
| D2-R40 | 3.4 | Lei 8.112, art. 53, caput | E | sim | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R41 | 4.1 | CF, art. 41, § 1º, I | E | sim | APL | S | direta | APROVADO | APROVADO (idêntico) |
| D2-R42 | 4.1 | CF, art. 5º, LV (adendo) | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R43 | 4.1 | Lei 9.784, art. 2º, par. ún., IV | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R44 | 4.1 | Lei 9.784, art. 2º, par. ún., V | E | sim | DEF | N | direta | AJUSTAR (AJ-1 a AJ-10) | **APROVADO** (AJ-1 aplicado; AJ-2 a AJ-10 nos registros) |
| D2-R45 | 4.1 | Lei 9.784, art. 2º, par. ún., VII | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R46 | 4.1 | CF, art. 41, § 1º, II | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R47 | 4.1 | Lei 9.784, art. 2º, par. ún., XII | E | sim | APL | S | direta | APROVADO | APROVADO (idêntico; nota (bf)) |
| D2-R48 | 4.1 | Lei 9.784, art. 2º, par. ún., IX | E | sim | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R49 | 4.1 | CF, art. 5º, LIV (adendo) | C | não | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R50 | 4.1 | Lei 9.784, art. 2º, par. ún., VIII | E | sim | APL | S | direta | APROVADO | APROVADO (idêntico; nota (bf)) |

Percentual de reprovados: **0/30 = 0,0%**. APROVADO: 30 (100%). REPROVADO: 0.

## 9. Notas à GCB (sem decisão desta QA)
1. A leva segue para a reconciliação e o gatilho A. São 11 ajustes distintos (AJ-1 a AJ-10 do R1; AJ-L5-E1 do estilo), e não há texto duplicado entre o R1 e o estilo.
2. Registros para a reconciliação:
   - (a) a frase da l. 688, não declarada na R.3 nem na R.7 (seção 3);
   - (b) o escopo da marca "OBRIGATÓRIA" da (ay): para esta QA, só o par D2-R36 × D2-39 (seção 6);
   - (c) "qualquer" na 3.4 fechada fica 1 C / 2 E, com o canônico D2-36 (seção 5);
   - (d) «esta v1» no bloco 5, l. 909, e o vocabulário "ator" na Base do D2-R44 (seção 6).

   Nenhum deles pede errata: são campos que não vão ao pacote.json ou afirmações verdadeiras (ficha 10.3 e 11.3).
3. Continuam os registros do R1, seção 8, item 4:
   - os desvios de número dos D2-R32 e D2-R33;
   - o formato do D2-R44;
   - a "cota da T-122 na 3.4 (3 E)" da ficha 11.4.6;
   - a reabertura de 22/10 como conferência.

   A reabertura deste R2 (Fontes 4, 6 e 7) confere as bases dos 2 itens alterados.
4. As recomendações L6-1 e L6-2 do estilo (seção 6) vão para a ficha da leva 6, se a GCB aceitar. Não têm efeito sobre esta leva.
5. Núcleo (ficha 11.1): os 30 itens ficam false, como na v1.

FIM DO PARECER QA R2 — LEVA 5 — REFORÇO DA
