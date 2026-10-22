# QA_DA_reforco_leva4_R2_2026-10-22_gcb-cqfp.md — T-116 — 2026-10-22 — gerado por gcb-cqfp

# PARECER QA R2 (ÚLTIMA RODADA) — REFORÇO DA, LEVA 4 (v2) — ciclo s16c2
A gcb-cqfp (opus) faz este QA de forma independente. Ela não produziu o texto revisado e não reescreve itens. Nenhum arquivo de produção foi alterado; não houve commit nem push. O exame segue a ficha (seção 4.3: "o R2 confere cada AJ aplicado literalmente e examina só o que a v2 mudou além dos AJ"), o R1 (seção 8, itens 1 a 3) e a ficha (seção 9.3, item 6): os AJ do R1 e da auditoria de estilo, conferidos literalmente; o que a v2 mudou além deles; a resposta item a item; a seção 4 refeita; as notas (af), (ao) e (ap).

## 0. Objeto, entradas e método
| objeto | SHA-256 (em disco, 22/10/2026) |
|---|---|
| saida/gcb/DA_reforco_leva4_v2.md (objeto do R2; 28 itens; 125.224 bytes) | 57203ae3a68042012989b549d19f2dbd5703623b5de3619275b3f05a2f8338da (= despacho) |
| saida/gcb/DA_reforco_leva4_v1.md (objeto do R1; base do diff; 112.361 bytes) | 7b0c1dc7c38d1b92de08b3e4c21676df9591a5a13122b5de7670d65642e0f3d8 (= R1, seção 1) |
| saida/gcb/QA_DA_reforco_leva4_R1_2026-10-22_gcb-cqfp.md | dd2c8efc22c7a15c813e7864f1ea2a469db4c68085e2595401fad8aadbf96b69 (= despacho) |
| saida/banco/estilo_DA_reforco_leva4.md | 358de121df6b16f8d2471141874e0b002f2203f0275753697b2753f455906cae (= despacho) |
| saida/gcb/DA_reforco_ficha_2026-10-20.md | 777e6eb6a2d871f5d6afc26b22a479a9ccfcb9ede3285d68ab06e391c761a03a (= despacho) |
| normativo_cache/Decreto_9830_2019_2026-10-20.txt | ae022402edcf1e5dfb951947d3f9c9f4323c957a2adeb7ac87f3601a213fb232 (= R1) |
| normativo_cache/CF_1988_compilada_2026-10-20.txt | d6580cb327147e1beb69ccd09cd930613c06f39e1791b235729930a01cacb51d (= R1) |
| normativo_cache/Lei_10406_2002_CodigoCivil_compilada_2026-10-20.txt | 97e0ffaa7e5b92d072622c9bde5ebdab9121cd32913c4292cb0c5f74a914a828 (= R1) |
| normativo_cache/Lei_9494_1997_2026-10-20.txt | e0cde6a9c898133d726ae193d1bc589b72e1bd1a47ca4e6361c6d0f51102ee94 (= R1) |
| normativo_cache/Lei_8112_1990_compilada_2026-10-20.txt | 72f45d30dcf096207898d143ba551758e3ffac89e87d6dd2d42044fe65202efe (= R1) |

Registro do SHA do despacho: a forma abreviada da v1 no despacho ("7b0c1dc7…3f8") não reproduz o final do valor em disco (…42e0f3d8); o valor completo em disco é igual ao do R1, seção 1. É grafia da abreviação, sem efeito.

**REGISTRO DO ORQUESTRADOR (transcrito e conferido).** A gcb-cpp informou primeiro o SHA f89c7974… (125.205 bytes), calculado antes de uma regravação; a diferença de 19 bytes é a troca, só na seção "Resposta à R1", R.3, de «O D2-R05 deixa de ser o único E acima do teto de 62;» por «O D2-R05 era o único item acima do teto de 62 e passa a caber na faixa;». **Conferido por esta QA:** a frase nova ocorre 1 vez na v2 e a antiga 0 vez; a nova tem 72 bytes e a antiga 53 (diferença 19); revertida em memória só essa frase, o arquivo tem 125.205 bytes e SHA-256 **f89c79745fd1d2898df5588312be6111f34a0eb533bd9851bb0a3896ab1ad0d2**, que começa por f89c7974. Logo, a versão informada primeiro e a gravada diferem só por essa frase. As duas redações são verdadeiras (o D2-R05, com 67 palavras na v1, era o único item da leva acima de 62, C ou E; os C vão até 60). Vale o SHA em disco (57203ae3…8da), objeto deste R2.

Também foram lidos: ficha, seções 4, 7.6, 9.3, 10.2, 10.3 e 10.4 (10.4.4, 10.4.8 e 10.4.9); regras/ (PADRAO_UNICO_v1.md, proveniencia.md, estilo_banca.md) e CLAUDE.md. Modelo de forma: saida/gcb/QA_DA_reforco_leva3_R2_2026-10-22_gcb-cqfp.md.

Método (scripts próprios r2.py, cnt.py e rev.py; python3 -I, somente leitura, no scratchpad da sessão, fora do repositório):
- (a) aplica à v1, em memória, os 2 AJ distintos (AJ-1 do R1 = AJ-L4-E2 do estilo; AJ-L4-E1), com o texto literal dos pareceres, uma vez cada, e compara com a v2;
- (b) compara por id os 28 enunciados (seção 1) e os 28 blocos (seção 2) da v1 e da v2, e as seções 0, 3 e 4 inteiras;
- (c) refaz sobre a v2 gabarito, sequência, [TS], abertura × gabarito, fórmula, fecho, absolutos (L3-2), contraste e qualificador (L3-4, L3-5), moldura, termos do Legislativo e extensão;
- (d) reverte a frase da R.3 para conferir o registro do orquestrador.
O diff integral v1 → v2 (105 linhas de saída do diff) foi lido linha a linha.

Rede: em 22/10/2026, 20h37 UTC, curl para https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d9830.htm terminou em timeout de 15 s, código 000 (bloqueado, como diz o despacho). As bases foram conferidas nas cópias de 20/10/2026 em normativo_cache/; a URL está na linha 1 de cada cópia, com "verificado em 20/10/2026". Nada foi suprido de memória.

## 1. Veredito geral
- **Leva: APROVADA.**
- Os 2 itens alterados: **D3-R54 APROVADO** e **D2-R05 APROVADO**.
- Os 26 itens não alterados ficam APROVADOS, como no R1, e são idênticos aos da v1 (enunciado e bloco).
- **Reprovação final: 0/28 = 0,0%** (limite 30%). No acumulado do rito (R1 + R2), também 0/28 = 0,0%. Não há GATE.
- Itens aprovados no R1 e mudados sem pedido: **nenhum** (o D2-R05 mudou só pelo AJ-L4-E1, pedido pelo estilo e mandado aplicar pelo R1, seção 8, item 1).
- Conferências pedidas pelo despacho: (1) AJ por substituição exata, (2) 26 blocos idênticos, (3) resposta item a item, (4) seção 4 refeita, (5) notas (af), (ao), (ap): **CONFEREM**.
- **NÃO CONFERE (1 ponto, de registro, sem efeito em item):** na v2, bloco 5, linha "Arquivo" (l. 843), o SHA abreviado da v1 está escrito «7b0c1dc7…03d8»; o valor em disco termina em …f3d8, e a própria v2 o grafa certo na linha de entradas (l. 5) e no método da Resposta à R1 (l. 9). Ver seção 6.

## 2. Conferência (1) — AJ aplicados por substituição exata, sem efeito colateral
| AJ | item / campo | "substituir" na v1 | "por" na v1 | "substituir" na v2 | "por" na v2 | v1 + AJ = v2 (enunciado e bloco) | veredito |
|---|---|---|---|---|---|---|---|
| AJ-1 (R1) = AJ-L4-E2 (estilo) | D3-R54 / enunciado | 1 | 0 | 1, só na tabela da R.2 (l. 17), como citação do "antes" | 2: no item (l. 87) e na R.2 (l. 17) | idêntico | **APLICADO** (uma vez) |
| AJ-L4-E1 (estilo) | D2-R05 / enunciado | 1 | 0 | 1, só na tabela da R.2 (l. 18) | 2: no item (l. 109) e na R.2 (l. 18) | idêntico | **APLICADO** |

- Identidade dos textos: o AJ-1 do R1 (seção 4) e o AJ-L4-E2 do estilo (seção 5) são iguais letra por letra (mesmo item, campo, "substituir" e "por"). A v2 aplicou a substituição **uma só vez**, como o R1 mandou (seção 8, item 1). CONFERE.
- Com os 2 AJ aplicados em memória à v1, os 28 enunciados e os 28 blocos ficam iguais aos da v2. Fora dos itens, só diferem as linhas listadas na seção 3.
- Efeito colateral nos 2 itens: **nenhum**. Os blocos da seção 2 do D3-R54 e do D2-R05 são **idênticos** aos da v1 (gabarito, [TS], ponto, formato, moldura, aderência, justificativas, Base, mecanismo, Troca, "Difere de"). Só o enunciado da seção 1 mudou.
- Os dois AJ mudam enunciado, e não Troca, gabarito ou construção; entraram antes do R2 (ficha 9.3, item 6), e este R2 é a QA deles. CONFERE.
- Extensão (script, só o enunciado): D3-R54 42 → 45 palavras; D2-R05 67 → 53. Iguais às da R.2 da v2 e às do estilo (seção 5).

## 3. Conferência (2) — os 26 blocos não alterados e o que a v2 mudou além dos AJ
**CONFERE.** Na comparação por id, 26 enunciados e 28 blocos da seção 2 são idênticos aos da v1; só os enunciados do D3-R54 e do D2-R05 diferem, e apenas pelo texto dos AJ. As seções 0, 3 (proveniência) e 4 (contagens) são **idênticas byte a byte** às da v1.

Fora dos itens, o diff tem só estas mudanças, todas declaradas na Resposta à R1 (parágrafo de método e R.6, item 2):
- linha 1 (nome do arquivo), parágrafo de abertura (l. 3) e linha de entradas (l. 5, agora com v1, R1 e estilo);
- nova seção "Resposta à R1" (l. 7 a 64);
- bloco 5: "Arquivo" (l. 843), amostra da gbq-estilo (l. 848), notas de simulado (l. 850) e dúvidas de conteúdo (l. 851; só a dúvida (i) muda, conferido por segmento: 12 segmentos, 1 diferente);
- seção 6: linhas 6.2.1 (l. 859), 6.2.6 (l. 864) e 6.4.3 (l. 877).

Nenhuma outra linha diverge do que a v2 declara. As ocorrências remanescentes de "depende de" no bloco do D3-R54 (Ponto de julgamento, l. 179) e na seção 4.5 (l. 730) descrevem a letra do art. 14 ("somente será exercido … dolo ou erro grosseiro" = depende de dolo ou erro grosseiro) e são verdadeiras; o "com a habilitação e a escolaridade exigidas" no Ponto do D2-R05 (l. 336) descreve a letra do § 13 e é verdadeiro. Não são resíduo a harmonizar (e a ficha 10.3 veda harmonizar rótulos de "Ponto de julgamento" depois do R2).

## 4. Conferência (3) — resposta item a item da v2
**CONFERE.** As 8 partes da Resposta à R1 batem com o R1 e com o estilo:
- **R.1:** números do R1 (27/1/0; 0,0%; 8 de 8) e do estilo (2 CONFORMES, 2 AJUSTE, 0 NÃO CONFORME) corretos.
- **R.2:** 2 AJ distintos, 3 linhas de origem, nenhum recusado; "antes" 1 / "depois" 0 na v1 (confere); textos citados iguais aos pareceres; extensões 42 → 45 e 67 → 53 conferem.
- **R.3:** seções 0 e 4 sem diferença (confere, seção 5 deste parecer). A frase final, objeto do registro do orquestrador, é verdadeira (D2-R05 era o único item da v1 acima de 62 palavras; o D2-R11, com 14, segue abaixo da faixa de E).
- **R.4:** 27 linhas, os 26 "mantido" de fato não mudaram; o D2-R05 está corretamente descrito como alterado só pelo AJ-L4-E1. O D3-R54 está na R.2, não na R.4 (é o AJUSTAR do R1).
- **R.5:** mapeia corretamente a seção 7 do R1 (dúvidas i a xi, 6.1, 6.2.2 a 6.2.12). A dúvida (i) perdeu o objeto com o AJ-1.
- **R.6:** itens 1 a 5 da seção 8 do R1 cumpridos; a lista de mudanças além dos AJ (item 2) é exatamente a do diff (seção 3).
- **R.7:** as 8 conferências de leva iguais às do R1, o que foi refeito (seção 5).
- **R.8:** sem errata nesta leva (ficha 10.3); L5-1 e L5-2 do estilo registradas como recomendação, sem efeito em item; sem GATE.

## 5. Conferência (4) — seção 4 refeita, conferida contra o arquivo (script próprio sobre a v2)
| verificação | refeito pela QA | v2 | resultado |
|---|---|---|---|
| gabarito da leva | 15 C / 13 E (53,6%; faixa 12–16) | 15/13 (seções 0 e 4.2) | CONFERE |
| sequência da leva | CCECCEECCCEEECECCEECEECCCECE | igual à 4.3, à ficha 10.4.7 e à v1 | CONFERE (nenhum gabarito mudou; a 4.3 e o teste da regra 6 ficam inalterados) |
| [TS] | 13, todos E; 0 C-isca | 13 / 0 | CONFERE |
| moldura S | 0 C / 3 E (D2-R03, R05, R10); termos do Legislativo só nesses 3 | 0/3; o D2-R05 mantém "em órgão do Poder Legislativo da União" | CONFERE; DA 49/28 (63,6%) e D2 9/4 (69,2%) inalterados |
| abertura × gabarito | "Considere que" 6 C / 5 E; declarativos 9 C / 8 E | iguais (4.6) | CONFERE |
| "Nessa situação, nos termos d…" | D3-R53; D2-R03, R08, R19 (3 C / 1 E) | iguais | CONFERE (o D2-R05 usa "de acordo com a Constituição Federal", sem a fórmula) |
| fecho "é correto afirmar que" | 0 / 0 | 0 / 0 | CONFERE (L4-1) |
| absolutos L3-2 | só "sempre" no D2-R15 (C, literal); os 2 enunciados novos sem "somente", "apenas" ou "só" | igual | CONFERE (ficha 10.4.4 cumprida no D3-R54) |
| L3-4 e L3-5 | 0 "mas não", ", e não", "mero", "por si só", "simples" | 0 | CONFERE |
| extensão | E de 14 a 53; C até 60; fora da faixa da base só o D2-R11 (14, E) | a 4 não tabela extensão; a R.3 dá D3-R54 45 e D2-R05 53 | CONFERE |
| Base | 39 trechos; seção 3 e coluna Base idênticas à v1 | 39/39 | CONFERE (os AJ não tocam a Base) |

## 6. Conferência (5) — notas e registros; o ponto que NÃO CONFERE
1. **Notas (af), (ao), (ap): CONFEREM.** No bloco 5 (l. 850): (af) marcada "OBRIGATÓRIA, por registro da R1", com o motivo do R1 (o D3-R49 contém a proposição do D3-R55); (ao) NOVA: D3-R54 × D1-58 × D1-R02, com o texto do R1 (seção 8, item 3); (ap) NOVA: D2-R15 × D2-38. As demais notas (ae), (ag) a (an), (v), (w), (x) e os acréscimos da produção são idênticos aos da v1 (comparação por segmento: 13 → 15 segmentos; só o (af) muda e o (ao) e o (ap) entram). A 6.4.3 lista "(ae) a (ap)". A produção não decide por nenhuma.
2. **NÃO CONFERE (registro, sem efeito em item, gabarito, contagem ou aprovação):** bloco 5, linha "Arquivo" (l. 843): «Esta v2 é a v1 (7b0c1dc7…03d8)». O SHA da v1 em disco termina em …42e0**f3d8**; a v2 o grafa certo nas l. 5 e 9. É erro de transcrição numa linha declarada, não mudança não declarada. Cadeia única para errata da reconciliação, se a GCB quiser corrigir: «7b0c1dc7…03d8» (1 ocorrência na v2, conferido por contagem) → «7b0c1dc7…f3d8». O campo não é Troca, gabarito nem construção (ficha 7.6). Esta QA não redige nem decide a errata.
3. **Registro fora do objeto do R2 (sem veredito):** o D2-R11 (E, 14 palavras) fica abaixo da faixa de E da base (19 a 62), como o estilo apontou fora da amostra (seção 4) e a v2 registra no bloco 5. O R1 o aprovou sem tratar da extensão; o item não mudou na v2, e o R2 examina só o que a v2 mudou (ficha 4.3). Fica para a reconciliação, como registro; a recomendação L5-1 do estilo cobre só o teto.

## 7. Veredito por item (os 2 alterados)
| id | folha | gab. | [TS] | enunciado da v2 (lido inteiro) | base (cópia) | veredito | nota |
|---|---|---|---|---|---|---|---|
| D3-R54 | 6.2 | E | sim | «Segundo o Decreto nº 9.830/2019, no âmbito do Poder Executivo federal, o direito de regresso previsto no § 6º do art. 37 da Constituição Federal será exercido na hipótese de o agente público ter agido com dolo ou culpa em suas decisões ou opiniões técnicas.» | Decreto 9.830, art. 14 (cópia l. 109): «No âmbito do Poder Executivo federal, o direito de regresso previsto no § 6º do art. 37 da Constituição somente será exercido na hipótese de o agente público ter agido com dolo ou erro grosseiro em suas decisões ou opiniões técnicas»; art. 12, § 1º (l. 96): erro grosseiro é o «praticado com culpa grave» | **APROVADO** | Uma só troca, erro grosseiro → culpa (E1), na mesma moldura da letra. "Será exercido na hipótese de" afirma que a culpa, sem qualificação (inclusive a leve), abre o regresso, o que a letra fecha ("somente … dolo ou erro grosseiro"): o E sai da letra do art. 14. A leitura de condição necessária, que deixava o E discutível com "depende de" (R1, dúvida i), não se sustenta com o novo verbo. O item não afirma a relação entre "erro grosseiro" e "culpa" (C6, [SEM FONTE] mantido) e não usa "somente", "apenas" nem "só" (10.4.4). Nome do Decreto e alcance no enunciado; sem moldura; nada sobre a Câmara. Justificativas (linhas 1 e 2) seguem verdadeiras ("condição que ele não traz"). Mesma abertura do D3-R51 (C), separada pela nota (ag); nota (ao) registrada. |
| D2-R05 | 3.1 | E | sim | «Considere que, em órgão do Poder Legislativo da União, servidor titular de cargo efetivo tenha sofrido limitação em sua capacidade física. Nessa situação, de acordo com a Constituição Federal, ele poderá ser readaptado para cargo cujas atribuições e responsabilidades sejam compatíveis com a limitação, passando a perceber a remuneração do cargo de destino.» | CF, art. 37, § 13 (cópia l. 630): «poderá ser readaptado para exercício de cargo cujas atribuições e responsabilidades sejam compatíveis com a limitação … desde que possua a habilitação e o nível de escolaridade exigidos para o cargo de destino, mantida a remuneração do cargo de origem» | **APROVADO** | Uma só troca, remuneração do cargo de origem → do cargo de destino (E3), por contradição expressa. A condição de habilitação e escolaridade, retirada pelo AJ, é verdadeira e acessória: omiti-la num E não cria segundo ponto de erro ("incompleto não é errado", C6), e o resto do fecho é letra. O fecho fica literal ao campo Troca. A moldura não decide: o cenário só põe o servidor em órgão do Legislativo da União (tipo da cota); nada sobre parlamentar, Casa ou prática da Câmara. 53 palavras, dentro da faixa de E (19 a 62). Sem absoluto ("poderá" é letra); sem a fórmula "nos termos d…". Nota (aj) com D2-33 mantida; conta para a nota (x). |

## 8. Tabela-resumo dos 28 itens (v2)
| id | folha | ponto | gab. | [TS] | formato | moldura | aderência | R1 | R2 |
|---|---|---|---|---|---|---|---|---|---|
| D3-R52 | 6.2 | A6.2-07 (CC, art. 932, III) | C | não | SUJ | N | parcial | APROVADO | APROVADO (idêntico à v1) |
| D3-R53 | 6.2 | A6.2-12 (CF, art. 5º, XXIV) | C | não | SIT | N | parcial | APROVADO | APROVADO (idêntico) |
| D3-R54 | 6.2 | A6.2-03 (Decreto 9.830, art. 14) | E | sim | DEF | N | direta | AJUSTAR (AJ-1) | **APROVADO** (AJ-1 = AJ-L4-E2 aplicado uma vez) |
| D3-R55 | 6.2 | A6.2-01 (Lei 9.494, art. 1º-C) | C | não | NUM | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R56 | 6.2 | A6.2-14 (CC, art. 949) | C | não | SIT | N | parcial | APROVADO | APROVADO (idêntico) |
| D3-R57 | 6.2 | A6.2-13 (Lei 13.869, art. 4º, I) | E | sim | PAR | N | parcial | APROVADO | APROVADO (idêntico) |
| D3-R58 | 6.2 | A6.2-10 (CC, art. 942) | E | sim | PAR | N | parcial | APROVADO | APROVADO (idêntico) |
| D3-R59 | 6.2 | A6.2-05 (CF, art. 5º, LXXV) | C | não | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R01 | 3.1 | CF, art. 37, XVII | C | não | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R02 | 3.1 | CF, art. 37, IV | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R03 | 3.1 | CF, art. 38, I | E | sim | APL | S | direta | APROVADO | APROVADO (idêntico) |
| D2-R04 | 3.1 | CF, art. 37, VII | E | sim | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R05 | 3.1 | CF, art. 37, § 13 | E | sim | APL | S | direta | APROVADO | **APROVADO** (AJ-L4-E1 aplicado) |
| D2-R06 | 3.1 | CF, art. 37, XIV | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R07 | 3.1 | CF, art. 40, § 1º, II | E | sim | NUM | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R08 | 3.1 | CF, art. 37, § 10 | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R09 | 3.1 | CF, art. 39, § 2º | C | não | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R10 | 3.1 | CF, art. 41, § 2º | E | sim | APL | S | direta | APROVADO | APROVADO (idêntico) |
| D2-R11 | 3.2 | Lei 8.112, art. 7º | E | sim | PAR | N | direta | APROVADO | APROVADO (idêntico; extensão registrada, seção 6, item 3) |
| D2-R12 | 3.2 | Lei 8.112, art. 4º | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R13 | 3.2 | Lei 8.112, art. 19, caput | E | sim | NUM | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R14 | 3.2 | CF, art. 39, § 3º | E | sim | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R15 | 3.2 | Lei 8.112, art. 19, § 1º | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R16 | 3.2 | Lei 8.112, art. 5º, § 3º | C | não | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R17 | 3.2 | Lei 8.112, art. 15, caput | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R18 | 3.2 | Lei 8.112, art. 5º, § 2º | E | sim | NUM | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R19 | 3.2 | Lei 8.112, art. 120 | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R20 | 3.2 | Lei 8.112, art. 34, par. ún., II | E | sim | SIT | N | direta | APROVADO | APROVADO (idêntico) |

Percentual de reprovados: **0/28 = 0,0%**. APROVADO: 28 (100%). REPROVADO: 0.

## 9. Bases reabertas no cache (ficha 4.4, item 8; amostra ≥ 5)
Decreto 9.830, art. 12, § 1º (l. 96) e art. 14 (l. 109); CF, art. 37, § 13 (l. 630); CC, art. 949 (l. 1835); Lei 9.494, art. 1º-C (l. 14); Lei 8.112, art. 7º (l. 43). Texto igual ao trecho da coluna Base dos itens correspondentes (D3-R54, D2-R05, D3-R56, D3-R55, D2-R11); URL da linha 1 de cada cópia igual à do item (Lei 8.112: igual sem o "www.", grafia da Fonte 4 já registrada no R1, seção 1). Planalto não reaberto (bloqueado; seção 0).

## 10. Notas à GCB (sem decisão desta QA)
1. A leva segue para a reconciliação e o gatilho A. Os AJ-1 e AJ-L4-E2 se registram como um só ajuste, com duas origens.
2. Errata opcional de registro: o SHA abreviado da v1 na l. 843 (seção 6, item 2), pela via da ficha 7.6, a critério da GCB.
3. D2-R11 (14 palavras, abaixo da faixa de E): registro para a reconciliação (seção 6, item 3).
4. Notas de simulado (ae) a (ap), com (af) obrigatória e (ao) e (ap) novas, para a T-119 e a T-123; L5-1 e L5-2 do estilo para a ficha da leva 5, se a GCB aceitar.
5. Núcleo (ficha 10.1): os 28 ficam false, como na v1.

FIM DO PARECER QA R2 — LEVA 4 — REFORÇO DA
