# QA_DA_reforco_leva3_R1_2026-10-22_gcb-cqfp.md — T-116 — 2026-10-22 — gerado por gcb-cqfp

# PARECER QA R1 — REFORÇO DA, LEVA 3 (v1) — ciclo s16c1
Objeto: saida/gcb/DA_reforco_leva3_v1.md (30 itens: D3-R22 a D3-R25, folha 6.4, segunda parte; D3-R26 a D3-R37, folha 6.5; D3-R38 a D3-R48, folha 5.2; D3-R49 a D3-R51, folha 6.2, primeira parte). Critérios: ficha saida/gcb/DA_reforco_ficha_2026-10-20.md, seções 1, 4 (4.1 a 4.4), 7, 8.4 e 9 (o adendo 9 prevalece; L3-1 a L3-5 da seção 9.3). A gcb-cqfp não produziu este texto e não o reescreve: o ajuste vem em texto exato (ficha, seção 4.3). Sem commit nem push; nenhum outro arquivo foi alterado.

## 0. Resultado
- **APROVADO: 29. AJUSTAR: 1** (D3-R37; 1 AJ de texto exato). **REPROVADO: 0.**
- **Taxa de reprovação: 0/30 = 0,0%** (limite 30%): sem gate. A leva segue para a v2.
- Conferências de leva (ficha 4.4): 8 de 8 CONFEREM; a (4) e a (5) conferem com o registro do AJ-1 (seção 5).
- Errata AJ-L2-E1 (D3-R18, leva 2): **CONFERIDO** (seção 6, veredito separado do da leva 3).

## 1. Entradas (SHA-256 em disco, 22/10/2026) e método
| objeto | SHA-256 |
|---|---|
| saida/gcb/DA_reforco_leva3_v1.md | 7214e588c14f69b1acb72a8d3701efc77ab666824bfa487095c4389923fa91bb (= despacho) |
| saida/gcb/DA_reforco_ficha_2026-10-20.md | a09139bc3c05a68230f3aea5746490debb4418840d629574622927e1f2bc8493 (= despacho) |
| saida/gcb/D3_anexo_N_adendo_2026-10-20.md | bbfd3eed1a69edef189a1fb8f07fee901daaf5bb636d8192bb1442e53a3fa797 (= ficha 8.1) |
| saida/gcb/D3_v2_1.md | 0f7a8b090fe6f2243ae55b36273dacdb719aaf04b19548dce70aad4867798930 (= ficha 8.1) |
| saida/gcb/DA_reforco_leva2_v2.md | 5baec20d81eea47f50e79275375668284d58ff5649f85a06c37552cd0f161bbe (= ficha 9.4; D-T116-LEVA2-ACEITE) |
| saida/banco/estilo_DA_reforco_leva2.md | ff94acfdc76ef000a13e18624dba6bbd4b2546b4cff2fb503718bf40033a0300 (= ficha 9.4) |
| normativo_cache/Lei_4619_1965_2026-10-20.txt | b91ef03df94717e00602b1b5195f73176c1c5cf5bebe6d80fba1cbaf37a9082f (= adendo, seção 1) |
| normativo_cache/Lei_8078_1990_CDC_compilada_2026-10-20.txt | 575478df6643d0495446b41db6828975477d8e7f57cadaca403b3dfe07784526 (= adendo) |
| normativo_cache/Lei_10406_2002_CodigoCivil_compilada_2026-10-20.txt | 97e0ffaa7e5b92d072622c9bde5ebdab9121cd32913c4292cb0c5f74a914a828 (= adendo) |
| normativo_cache/Lei_8112_1990_compilada_2026-10-20.txt | 72f45d30dcf096207898d143ba551758e3ffac89e87d6dd2d42044fe65202efe (= adendo) |
| normativo_cache/CF_1988_compilada_2026-10-20.txt | d6580cb327147e1beb69ccd09cd930613c06f39e1791b235729930a01cacb51d (= adendo) |
| normativo_cache/Lei_13869_2019_2026-10-20.txt | fb3b95c117e64fc0f26f0a915af3ae433d6ceb3aad2434fc5dcae72a64f04a33 (= Adendo 2, A2.1) |
| normativo_cache/Lei_9494_1997_2026-10-20.txt | e0cde6a9c898133d726ae193d1bc589b72e1bd1a47ca4e6361c6d0f51102ee94 (= Adendo 2) |
| normativo_cache/Decreto_9830_2019_2026-10-20.txt | ae022402edcf1e5dfb951947d3f9c9f4323c957a2adeb7ac87f3601a213fb232 (= Adendo 2) |
| saida/banco/moldura_ce_itens_2026-10-20.csv | (lido; DA com moldura 44 C / 9 E; D3 6/1 — iguais à ficha) |

Lidos também: regras/ (PADRAO_UNICO_v1.md, proveniencia.md, padrao_resposta_cebraspe.md, estilo_banca_semente.md), CLAUDE.md e, em DECISOES.md, D-REFORCO-DA (l. 173), D-REFORCO-2 (l. 95), D-MOLDURA-CE (l. 171), D-T116-LEVA1-ACEITE (l. 175) e D-T116-LEVA2-ACEITE (l. 176). Modelo de forma: saida/gcb/QA_DA_reforco_leva2_R1_2026-10-20_gcb-cqfp.md.

Método: leitura integral das seções 0 a 6 da v1; cada item confrontado com a linha do adendo do D3 (seção 3.2, 3.3 e 4; Adendo 2, A2.3 e A2.4) e com a cópia em saida/gcb/normativo_cache/; canônicos das quatro folhas relidos no D3_v2_1.md (enunciados da seção 5.1 e pontos da seção 7.3: D3-11 a D3-20; D3-32 a D3-40 e D3-81; D3-51 a D3-59; D3-61 a D3-70) e itens das levas 1 e 2 (DA_reforco_leva1_v2.md; DA_reforco_leva2_v2.md, D3-R14 a D3-R21). Scripts próprios (python3 -I, somente leitura, no scratchpad da sessão, fora do repositório): check.py (blocos, campos, trechos × adendo × cópia, URL × primeira linha da cópia, data, palavras por trecho, marcadores no enunciado), seq.py (folhas acumuladas reconstruídas do pacote.json v1.13 na ordem do pacote + levas 1 e 2 + leva 3; teste de sequência da regra 6; moldura das três levas), errata.py (AJ-L2-E1).

Rede: tentativa de abrir https://www.planalto.gov.br/ccivil_03/leis/l4619.htm em 22/10/2026 por curl: "Empty reply from server", código 000 (bloqueado, como diz o despacho). Nenhuma página oficial foi reaberta; nada foi substituído por memória. As bases foram conferidas nas cópias oficiais gravadas em 20/10/2026 (seção 5, conferência 8).

## 2. Veredito por item
Legenda: G = gabarito pela letra; P = ponto único; T = troca legítima e única / [TS]; F = sem pista de forma; Pe = pertinência à folha; Gê = não gêmeo (canônico da folha, levas 1 e 2, própria leva); M = moldura; J = justificativa e proveniência. ✓ confere; ✗ não confere; ~ confere com ajuste.

### Folha 6.4 — D3-R22 a D3-R25 (segunda parte; todos de aderência parcial, ficha 8.2, item 2)
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D3-R22 | C ✓ | ✓ | sem [TS] ✓ | ✓ | parcial ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Decreto 20.910, art. 1º, literal (cópia, l. do art. 1º; adendo 4.10). Absolutos "todo e qualquer" e "seja qual for" são letra (C com absoluto literal, L3-2). Sem extensão às prestadoras (A10) nem termo do art. 1º-C (C8). Nota (n) com D3-R49. |
| D3-R23 | E ✓ | ✓ | [TS] "qualquer pessoa investida em função pública" → "apenas … cargo efetivo" ✓ | ✓ | parcial ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Lei 4.619, art. 1º, parágrafo único (cópia, l. 11). Troca única por restrição do conceito; "apenas" inserido coberto pelo D3-R22 (L3-2). Só "nos termos da Lei nº 4.619/1965" (A8). |
| D3-R24 | E ✓ | ✓ | [TS] sessenta → noventa ✓ | ✓ | parcial ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 2º (cópia, l. 12). Não usa "cinco anos" (ficha 8.4.4) nem os "Procuradores da República" (A8). Amostra da gbq-estilo. |
| D3-R25 | C ✓ | ✓ | sem [TS] ✓ | ✓ | parcial ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CDC, art. 14, caput (cópia, l. 108). L3-1 cumprida: CQ, SIT, sem a fórmula "Nessa situação, nos termos d…", cenário (hospedagem) diferente do D3-R17, sem menção ao Legislativo. Registro: pertinência à 6.4 só por contraste de regime (A7), como o adendo classifica. Acréscimo de nota D3-R17 × D3-R25 aceito. |

### Folha 6.5 — D3-R26 a D3-R37 (base: adendo do D3, seção 4.2 a 4.8)
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D3-R26 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CC, art. 393, parágrafo único, literal; não distingue fortuito × força maior (A3, A11). Difere do D3-63 (excludente, base doutrinária). |
| D3-R27 | E ✓ | ✓ | [TS] "tendo-se em conta" → "sem se levar em conta" ✓ | ~ | ✓ | ✓ | S, órgão/servidor ✓ | ✓ | **APROVADO** | CC, art. 945 (cópia, l. 1829). Moldura decorativa (servidor vítima), não decide o gabarito. Observação (sem AJ): o cenário traz a única hipótese do art. 945 e o fecho nega a consequência com "sem"; é a forma que a seção 7.4.5 pede evitar, mas a linha da ficha 8.4.4 a fixou ("troca: sem considerar a culpa da vítima"), e a seção 8 é posterior e específica. Recomendação à reconciliação (seção 8). |
| D3-R28 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Lei 8.987, art. 25, caput, parte final; a parte inicial é do D3-R14 (6.4). Nota (t). |
| D3-R29 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CC, art. 930, literal; não envolve o Estado (A3). Nota (r). |
| D3-R30 | E ✓ | ✓ | [TS] "não se podendo questionar mais" → "podendo-se questionar" ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CC, art. 935 (cópia, l. 1815); primeira oração verdadeira e troca na segunda (E3). Não usa o art. 126 da Lei 8.112 (A5). Formato: a construção está mais para DEF que para PAR; reclassificar leva a 6.5 a DEF 6 / PAR 3, no teto — sem AJ (dúvida (ii) da produção). |
| D3-R31 | E ✓ | ✓ | [TS] "cumular-se, independentes" → "a administrativa afasta a civil" ✓ | ✓ | parcial ✓ | ✓ | S, órgão/servidor ✓ | ✓ | **APROVADO** | Lei 8.112, art. 125, literal; sujeito nomeado (A1); sem regime próprio da Câmara. A menção ao art. 126 na justificativa (linha 2) é contraste dentro do adendo (4.3), não ponto. |
| D3-R32 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CF, art. 21, XXIII, d (cópia, l. 371; EC 49/2006, anterior a 2/10/2026, sem REVERIFICAR). Sem "risco integral" nem afirmação sobre excludentes (A6). Acréscimo de nota D3-R32 × D3-64 aceito. |
| D3-R33 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | S, órgão/servidor ✓ | ✓ | **APROVADO** | CC, art. 188, parágrafo único (cópia, l. 465); "somente" e "absolutamente" literais. C com moldura em par R3 com um dos 3 E com moldura da folha (cota 1). Amostra da gbq-estilo. |
| D3-R34 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CC, art. 944, parágrafo único, literal ("poderá"). Nota (l) com D3-R19. Formato SUJ aceitável ("o juiz"); DEF também caberia, sem efeito de teto. |
| D3-R35 | E ✓ | ✓ | [TS] condição inexistente ("só … se provar a culpa do servidor") ✓ | ✓ | ✓ | ✓ | S, órgão/servidor ✓ | ✓ | **APROVADO** | CC, art. 929 (cópia, l. 1803). Dúvida (i) da produção respondida: o E é nítido pela letra — o art. 929 assegura o direito ao lesado não culpado do perigo, no caso do art. 188, II (ato que não é ilícito), sem outra condição; a condição de prova de culpa contradiz o "assistir-lhes-á direito". Cenário sem a condição de lesado não culpado (7.4.5 cumprida). O item não diz contra quem a vítima age (nada de "dupla garantia", C12). "só" inserido coberto pelo D3-R33 (L3-2). |
| D3-R36 | C ✓ | ✓ | ✓ | ✓ | parcial ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Lei 4.619, art. 5º (cópia, l. 17); "por exoneração" é uma das "formas". Observação (sem AJ): o cenário fala em lesão "à Fazenda", ao passo que a lei trata de lesão a terceiros reparada pela Fazenda (art. 1º); o art. 5º é genérico ("responsabilidade perante a Fazenda") e o C não fica discutível. |
| D3-R37 | E ✓ | ✓ | **✗ → ~** | ✓ | parcial ✓ | ✓ | N ✓ | ✓ | **AJUSTAR** (AJ-1) | CDC, art. 14, § 3º (cópia, l. 114 e 116). A troca declarada (exclusiva → concorrente) não é a única fonte do erro: com o "só" literal do caput do § 3º, o enunciado faz da culpa (de qualquer espécie) do consumidor ou de terceiro a **única** excludente e apaga o inciso I (inexistência do defeito). Mesmo com "exclusiva", a frase "só não será responsabilizado quando provar a culpa exclusiva do consumidor ou de terceiro" seria E. Há duas trocas, não uma (ficha, seção 1, regras 7 e 9; critério 4.2, "[TS] sem troca real" / troca não única). O AJ-1 retira o "só" e deixa a troca única exclusiva → concorrente, com o E pela letra do rol fechado do § 3º ("só não será responsabilizado quando provar:"; regra 8). Ponto, gabarito, [TS], formato, mecanismo E1, aderência, abertura, Troca e Justificativa ficam. Nota (p) com D3-61 mantida. |

### Folha 5.2 — D3-R38 a D3-R48 (base: Adendo 2, A2.4.1 a A2.4.4)
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D3-R38 | E ✓ | ✓ | [TS] "ilegalidade ou abuso de poder" → "somente por ilegalidade" ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CF, art. 5º, LXVIII (cópia, l. 138). Não diz que a CF define abuso de poder (C3). Primeiro item da folha: completa o piso de 10 diretos (núcleo). |
| D3-R39 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CF, art. 5º, LXIX, parte do sujeito, literal. Acréscimo de nota D3-R39 × D3-R41 aceito. |
| D3-R40 | E ✓ | ✓ | [TS] "independentemente do pagamento de taxas" → "mediante" ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CF, art. 5º, XXXIV, caput do inciso e a (cópia, l. 88). Observação (sem AJ): a citação no enunciado "(art. 5º, XXXIV, a)" não nomeia o caput do inciso, onde está a gratuidade; a alínea se lê sob o caput, e o gabarito não muda. A5.2-01 fora (ficha 8.4.4). |
| D3-R41 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CF, art. 5º, LXIX, parte do direito protegido (ponto distinto do D3-R39: A5.2-05 × A5.2-04). |
| D3-R42 | C ✓ | ✓ | ✓ | ✓ | parcial ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Lei 8.112, art. 116, XII, literal; sem afirmar que a Lei 8.112 define abuso de poder (C1). |
| D3-R43 | E ✓ | ✓ | [TS] "sofrer violação ou houver justo receio" → "somente … já tiver sofrido" ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Lei 12.016, art. 1º, caput, pela letra; nada sobre a ADI 4296 (C2; ficha 8.2, item 3). Nota (q). |
| D3-R44 | E ✓ | ✓ | [TS] "compreendendo, mas não se limitando a" → "exaustivo" ✓ | ✓ | parcial ✓ | ✓ | S, comissão/sessão da Câmara (cota da 5.2) ✓ | ✓ | **APROVADO** | Lei 13.869, art. 2º, caput e II (cópia, l. 22 e 24). Afirma só a inclusão dos membros do Legislativo; nada de imunidade, tipo penal ou norma interna (C4); não diz que a lei define o abuso de poder administrativo (C1). Moldura não decide. Dúvida (vi): o fecho "é correto afirmar que" no D3 não entra em K1 a K4 — confere. Amostra da gbq-estilo. |
| D3-R45 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Lei 12.016, art. 1º, caput, com os termos amplos literais (L3-2; desvio 6.2.4 aceito). |
| D3-R46 | C ✓ | ✓ | ✓ | ✓ | parcial ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Lei 13.869, art. 1º, § 2º, literal; "abuso de autoridade" (o crime), não abuso de poder administrativo (C1). |
| D3-R47 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Lei 12.016, art. 1º, § 1º, parcial sem marcador de exclusividade (C6); § 1º sem "Vide ADIN" (C2). "e" no lugar de "ou" entre os dois sujeitos não altera o sentido. |
| D3-R48 | E ✓ | ✓ | [TS] "autoridade superior àquela" → "própria autoridade" ✓ | ~ | parcial ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Lei 8.112, art. 116, parágrafo único. Observação (sem AJ): o sujeito trocado é ator que o próprio dispositivo menciona (7.4.4, primeira parte), mas a apreciação pela própria autoridade representada é implausível à primeira leitura, o que facilita o E; a troca foi fixada na ficha 8.4.4. Recomendação à reconciliação (seção 8). |

### Folha 6.2 — D3-R49 a D3-R51 (primeira parte; base: Adendo 2, A2.4.1, A2.4.5, A2.4.6)
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D3-R49 | E ✓ | ✓ | [TS] inclusão das prestadoras → "prazo que não alcança" ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Lei 9.494, art. 1º-C (cópia, l. 14); sem termo inicial nem prevalência sobre o Decreto 20.910 (C8). Primeiro item da folha: fecha o bloco de período 4 do legado (posições 2 a 9). |
| D3-R50 | E ✓ | ✓ | [TS] hipótese autônoma ("assim como") → "depende de erro judiciário" ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CF, art. 5º, LXXV (cópia, l. 149). A6.4-03/04 não usados na 6.4 (leva 2 conferida: A6.4-01, 02, 05, 06, 08, 12, 13, 17), C7 cumprido. Nada sobre atos jurisdicionais em geral. Amostra da gbq-estilo. |
| D3-R51 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Decreto 9.830, art. 14 (cópia, l. 109), parte final, com o nome e o alcance ("No âmbito do Poder Executivo federal"), sem moldura (C6); parcial verdadeira (C6). Nota (o). |

## 3. Reprovação e substituto
Nenhum item reprovado. Nenhuma reposição de E com moldura é necessária (seção 2.2 da ficha: a margem da leva 5 fica como planejada).

## 4. Ajuste em texto exato (ficha, seção 4.3; o "substituir" ocorre 1 vez no arquivo, conferido por script)
`AJ-1 | D3-R37 | enunciado (seção 1) | substituir: «o fornecedor de serviços só não será responsabilizado quando provar a culpa concorrente do consumidor ou de terceiro.» | por: «o fornecedor de serviços não será responsabilizado quando provar a culpa concorrente do consumidor ou de terceiro.»`

Efeito: o enunciado vira «Segundo o Código de Defesa do Consumidor, o fornecedor de serviços não será responsabilizado quando provar a culpa concorrente do consumidor ou de terceiro.» Gabarito E, [TS], Troca (exclusiva → concorrente), mecanismo E1, formato PAR, aderência parcial, abertura declarativa e Base ficam. Na seção 4.6 da v2 (refeita por script, como na leva 2), o D3-R37 sai da tabela L3-2 ("só" literal em E: 1 → 0); nenhuma outra contagem muda.

## 5. Conferências de leva (ficha, seção 4.4)
| # | conferência | resultado |
|---|---|---|
| 1 | C/E da leva | **CONFERE**: 16 C / 14 E (53,3%; faixa 12–18). Sequência da leva CEECCECCEECCCECEECECCEECCCEEEC, igual à ficha 8.4.7. Folhas: 6.4 10/10 (fechada); 6.5 10/10; 5.2 10/10; 6.2 5/7 (12 de 20; fecha na leva 4). |
| 2 | tetos por folha | **CONFERE**: formatos da leva 6.4 0/1/1/2/0/0, 6.5 2/2/2/0/2/4, 5.2 2/4/3/0/1/1, 6.2 1/1/1/0/0/0 (DEF/SUJ/SIT/NUM/PAR/APL), iguais à ficha 8.4.4 com a L3-1 (D3-R25 SIT); folha final: 6.4 5/2/4/2/2/5, 6.5 5/2/4/0/4/5, 5.2 5/5/5/0/3/2 (maior 25%; teto 6 de 20), 6.2 4/1/4/0/3/0 (de 12; a leva 4 admite no máximo DEF 2, SIT 2 e PAR 3). VOLÁTIL 0; REVERIFICAR 0. Moldura por folha: 6.4 5, 6.5 5, 5.2 2, 6.2 0 (≤ 6). Piso de 10 diretos: 6.4 14; 6.5 17; 5.2 16; 6.2 12 (de 12). |
| 3 | moldura acumulada e conjuntos | **CONFERE**: moldura nova 1 C / 4 E (D3-R33 / D3-R27, R31, R35, R44), recontada nos blocos das três levas (L1 2/9; L2 2/3; L3 1/4) e no CSV (DA 44/9; D3 6/1): DA 48/21 → **49/25 (66,2%)**, igual à seção 2.2; D3 8/7 → **9/11 (45,0%)**, igual à 8.4.6. K1 a K4, fecho neutro e ", e não" do D4 sem item novo (14/6; 7/7; 5/4; 25/18; 2/3; 1/2). Termos do Legislativo só nos 5 itens S (busca própria: "Legislativo", "Câmara", "Congresso", "parlament", "comissão", "sessão"). Cotas da T-122: 6.5 (1 E) e 5.2 (1 E) cumpridas; R3 do D3-R33 cumprida. |
| 4 | pontos sem duplicata | **CONFERE**: 30 códigos distintos (A6.4-15, 09, 11, 16; A6.5-01, 05, 06, 07, 08, 09, 11, 12, 14, 17, 19, 20; A5.2-02, 03, 04, 05, 06, 07, 08, 12, 13, 17, 18; A6.2-02, 04, 06); nenhum da leva 1 nem da leva 2; nenhum dispositivo coincide com ponto canônico das quatro folhas (D3_v2_1.md, 7.3); excluídos respeitados (A6.5-13, A6.5-18, A6.4-03/04/14; CC, arts. 186 e 927; Lei 8.112, art. 122; Lei 12.016, art. 1º, § 2º, e art. 23). Pares de mesmo dispositivo com elementos distintos, com "Difere de" e nota: D3-R39 × R41; D3-R43 × R45; D3-R14 × R28; D3-R19 × R34. O AJ-1 não toca ponto. |
| 5 | exigências da leva | **CONFERE**: (d) aderência parcial declarada em 11 (D3-R22 a R25, R31, R36, R37, R42, R44, R46, R48), igual à 8.4.6, pertinência dos indiretos aceita (adendo 3.2, 3.3 e A2.3.1); L3-1 (D3-R25) aplicada; L3-2: todo E com absoluto inserido tem C com absoluto literal na mesma folha (6.4 R23 × R22; 6.5 R35 × R33; 5.2 R38, R43, R44 × R45, R47); L3-3: nenhum cenário idêntico até o fecho (as três aberturas "Considere que servidor de órgão do Poder Legislativo da União" da 6.5 são a moldura da cota; cenários seguintes distintos); L3-4: 0 contraste "mas não" / ", e não"; L3-5: 0 "mero", "por si só", "simples". Abertura × gabarito: CQ 6 C / 6 E (50%), declarativos 10 C / 8 E (44,4% de E); folhas fechadas 6.4 CQ 4/5, 6.5 CQ 5/4 e DC 5/6, 5.2 CQ 5/2 e DC 5/8 (mínimos de 40% cumpridos). Fórmula "Nessa situação, nos termos d…": 3 de 12 CQ (D3-R27, R33, R36; limite 5); 0 na 6.4. |
| 6 | primeiro e último id por lote | **CONFERE**: D3-R22–R25, D3-R26–R37, D3-R38–R48, D3-R49–R51 (ficha 8.4.1 e 9.1; sem substituto na leva 2); nenhum id no pacote.json v1.13 nem nas levas 1 e 2. |
| 7 | linha 1 e última linha | **CONFERE**: "# DA_reforco_leva3_v1.md — T-116 — 2026-10-22 — gerado por gcb-cpp"; "FIM DA LEVA 03 — REFORÇO DA". |
| 8 | bases reabertas no cache | **CONFERE**: os 37 trechos (30 itens) são subcadeia do adendo (37/37) e da cópia em normativo_cache/ (37/37; espaços normalizados); maior soma por item 24 palavras (limite 25); URL de cada item igual à do adendo e à primeira linha da cópia (30/30); "consulta 20/10/2026" em 30/30. Reabertas com linha (amostra ≥ 5): Lei 4.619 (l. 11, 12, 17 — D3-R23, R24, R36); CDC (l. 108, 114, 116 — D3-R25, R37; o "culpa exclusiva" do art. 12, § 3º, III, l. 102, não é a base); CC (l. 465, 1803, 1815, 1829 — D3-R33, R35, R30, R27); Lei 13.869 (l. 22, 24 — D3-R44); Lei 9.494 (l. 14 — D3-R49); Decreto 9.830 (l. 109 — D3-R51); CF (l. 88, 138, 149, 371 — D3-R40, R38, R50, R32). |
| — | teste de sequência (regra 6; 7.3; 8.2, item 7) | **CONFERE** (seq.py, folhas reconstruídas do pacote v1.13 + levas): leva e folhas da leva passam (gabarito e [TS]); acumuladas: 6.4 gabarito só p3 nas posições 1–8 (legado), [TS] passa; 6.5 gabarito e [TS] só a alternância 2–6 (legado); 5.2 passa; 6.2 gabarito só p4 nas posições 2–9 (legado), [TS] passa. Nenhuma janela reprovada inclui item novo. O AJ-1 não muda gabarito nem [TS]. |
| — | integridade dos blocos | 30 blocos com os 13 campos; Troca ⇔ [TS] ⇔ "TS=sim" (14/14); itemEdital P1-DA-<folha>, AUTORAL e QA PENDENTE em 30/30; seção 1 sem gabarito, [TS], URL ou marcas; 0 "exceto", "R$", "NGP", "Vide", "STF" em enunciado. |

## 6. Errata AJ-L2-E1 (D3-R18, leva 2) — seção própria (ficha, seção 9.4; rito da D-T116-LEVA1-ACEITE, parte (II), e da D-T116-LEVA2-ACEITE)
Texto conferido: saida/banco/estilo_DA_reforco_leva2.md (ff94acfd…0300), seção 5 — antes «tenha causado dano ao erário e falecido.» — depois «tenha causado dano ao erário e, posteriormente, tenha falecido.»; idêntico ao da ficha 9.4 e ao da reconciliação da leva 2 (cada um com 1 ocorrência do "antes" e 1 do "depois").
1. Ocorrência: o "antes" ocorre **1 vez** na seção 1 de saida/gcb/DA_reforco_leva2_v2.md (5baec20d…1bbe, linha 142) e **1 vez** no arquivo inteiro; o "depois" ocorre **0 vez** (seção 1 e arquivo). A substituição simulada (errata.py, em memória) muda só a linha 142. **CONFERE.**
2. Campos do bloco: a errata toca só o enunciado da seção 1; no bloco do D3-R18 (linhas 559–573) ficam gabarito E, ponto A6.4-13, Troca «até o limite do valor da herança recebida → sem limite de valor», mecanismo E3, formato APL, moldura S (órgão/servidor do Poder Legislativo da União, fecho neutro), aderência parcial, abertura CQ ("Considere que"), Base e Marcas. **CONFERE.**
3. Leitura do enunciado resultante: «Considere que servidor público civil da União lotado em órgão do Poder Legislativo da União tenha causado dano ao erário e, posteriormente, tenha falecido. Nessa situação, a obrigação de reparar o dano estende-se aos sucessores, que respondem sem limite de valor, conforme a Lei nº 8.112/1990.» Sentido inalterado (a troca continua só em "sem limite de valor"); "posteriormente" só explicita a ordem dos fatos e não é marcador de gabarito (nem absoluto, nem negação, nem possibilidade); a leitura de passagem "dano ao erário e falecido" (que admitia ler "falecido" como qualificação de "erário" ou fatos simultâneos) desaparece. Extensão: +2 palavras (44 → 46 por separação simples em espaços; 47 → 49 na contagem da gbq-estilo — diferença de método, sem efeito, como no precedente da D-T105-SALDO-ACEITE), dentro da faixa dos enunciados da leva 2 (22 a 57 palavras). **CONFERE.**
4. Ordem dos fatos: a Lei 8.112, art. 122, § 3º («A obrigação de reparar o dano estende-se aos sucessores e contra eles será executada, até o limite do valor da herança recebida.»), na cópia saida/gcb/normativo_cache/Lei_8112_1990_compilada_2026-10-20.txt (72f45d30…202efe) e no adendo do D3, seção 4.3, pressupõe obrigação de reparar já nascida (dano) e transmitida aos sucessores (falecimento posterior, herança recebida): dano, depois falecimento, é a ordem do dispositivo. **CONFERE.**

**Veredito: CONFERIDO.** Não é terceira rodada da leva 2, não altera o arquivo da leva 2 e não é QA aberto que impeça a leva 4; a GCB a leva ao gatilho A da leva 3 como item separado (ficha 9.4).

## 7. Desvios e dúvidas declarados pela produção (seções 5 e 6 da v1)
| # | desvio ou dúvida | avaliação |
|---|---|---|
| 6.1 | D3-R25: SUJ → SIT, DC → CQ (L3-1) | **Aceito** (determinado pela ficha 9.3); demais 29 linhas iguais à ficha 8.4.4 (conferido). |
| 6.2.1 | D3-R24: sessenta → noventa | **Aceito**. |
| 6.2.2 / dúvida (i) | D3-R35: condição no fecho, não no cenário | **Aceito**; E nítido (seção 2). |
| 6.2.3 / dúvida (iii) | D3-R23: "cargo efetivo" só na troca | **Aceito** (E1 com restrição; L3-2 coberto). |
| 6.2.4 | D3-R45: letra em vez do resumo da ficha | **Aceito** (C com absoluto literal, L3-2). |
| 6.2.5 / dúvidas (iv), (v) | D3-R47 e D3-R51 parciais, C6 | **Aceito** (sem marcador de exclusividade; verdadeiros por si). |
| 6.2.6 | trechos múltiplos com "[…]" (6 itens) | **Aceito**: cada trecho é subcadeia contínua do adendo e da cópia; soma ≤ 24 palavras. |
| 6.2.7 | mecanismo escolhido pela produção | **Aceito**; sem reclassificação (D3-R41 C1 ou C2, indiferente). |
| 6.2.8 / dúvida (ii) | formatos SUJ e PAR | **Aceito**; D3-R30 e D3-R34 admitem DEF sem passar do teto (seção 2). |
| 6.2.9 | fechos "conforme …" | **Aceito** (cumpre 7.4.3). |
| dúvida (vi) | fecho "é correto afirmar que" no D3-R44 | **Aceito**; fora de K1–K4 (conjuntos do D4). |
| dúvida (vii) | pertinência dos parciais | **Aceita** para os 11 (adendo 3.2, 3.3, A2.3.1); a 6.4 fecha em 20 com 14 diretos. |
| 6.4.1 | 7 de 12 itens da 6.5 do Código Civil | Registro à reconciliação (sem teto por norma na 6.5; ficha 9.2 limita o teto de composição à 2.2). |
| — | não declarado: D3-R37 com duas fontes de erro | **Não aceito** → AJ-1. |

## 8. Lista para a v2 (gcb-cpp) e notas à GCB
1. Aplicar o AJ-1 por substituição exata, sem outra mudança; refazer por script as seções 0 e 4 (só a tabela L3-2 da 4.6 muda: D3-R37 sai).
2. O R2 confere o AJ-1 aplicado literalmente e examina só o que a v2 mudar além dele.
3. Coordenação com a gbq-estilo (ficha 9.3, item 6): a amostra (D3-R33, R44, R50, R24) não inclui o D3-R37; os AJ de estilo que vierem da auditoria sobre a v1 seguem com o AJ-1 para a v2.
4. Recomendações à reconciliação, sem decisão desta QA: (a) D3-R27 — a linha da ficha 8.4.4 ("sem considerar a culpa da vítima") produz a forma que a 7.4.5 desaconselha (cenário com a hipótese inteira + fecho que nega com "sem"); para as levas seguintes, prefere-se trocar o critério por conceito vizinho em vez de negá-lo; (b) D3-R48 — a 7.4.4 pede ator "plausível na função"; a "própria autoridade representada" é mencionada pela fonte, mas implausível, e facilita o E; (c) notas de simulado da produção aceitas: (l), (n), (o), (p), (q), (r), (t), (v), (w), (x) com os ids finais, e os acréscimos D3-R17 × D3-R25, D3-R27 × D3-61, D3-R32 × D3-64, D3-R39 × D3-R41, D3-R50 × A6.2-05 (leva 4).
5. Núcleo (seções 7.2 e 8.2, item 9): 6.5 D3-R26 e D3-R27; 5.2 D3-R38; 6.2 D3-R49; 6.4 sem núcleo novo — confere com a v1 (nenhum reprovado).

## 9. Tabela-resumo dos 30 itens
| id | folha | ponto | gab. | [TS] | formato | moldura | aderência | veredito |
|---|---|---|---|---|---|---|---|---|
| D3-R22 | 6.4 | A6.4-15 | C | não | NUM | N | parcial | APROVADO |
| D3-R23 | 6.4 | A6.4-09 | E | sim | SUJ | N | parcial | APROVADO |
| D3-R24 | 6.4 | A6.4-11 | E | sim | NUM | N | parcial | APROVADO |
| D3-R25 | 6.4 | A6.4-16 | C | não | SIT | N | parcial | APROVADO |
| D3-R26 | 6.5 | A6.5-01 | C | não | DEF | N | direta | APROVADO |
| D3-R27 | 6.5 | A6.5-08 | E | sim | APL | S | direta | APROVADO |
| D3-R28 | 6.5 | A6.5-12 | C | não | SIT | N | direta | APROVADO |
| D3-R29 | 6.5 | A6.5-07 | C | não | SUJ | N | direta | APROVADO |
| D3-R30 | 6.5 | A6.5-17 | E | sim | PAR | N | direta | APROVADO |
| D3-R31 | 6.5 | A6.5-19 | E | sim | APL | S | parcial | APROVADO |
| D3-R32 | 6.5 | A6.5-14 | C | não | DEF | N | direta | APROVADO |
| D3-R33 | 6.5 | A6.5-05 | C | não | APL | S | direta | APROVADO |
| D3-R34 | 6.5 | A6.5-09 | C | não | SUJ | N | direta | APROVADO |
| D3-R35 | 6.5 | A6.5-06 | E | sim | APL | S | direta | APROVADO |
| D3-R36 | 6.5 | A6.5-20 | C | não | SIT | N | parcial | APROVADO |
| D3-R37 | 6.5 | A6.5-11 | E | sim | PAR | N | parcial | AJUSTAR (AJ-1) |
| D3-R38 | 5.2 | A5.2-03 | E | sim | DEF | N | direta | APROVADO |
| D3-R39 | 5.2 | A5.2-04 | C | não | SUJ | N | direta | APROVADO |
| D3-R40 | 5.2 | A5.2-02 | E | sim | SIT | N | direta | APROVADO |
| D3-R41 | 5.2 | A5.2-05 | C | não | PAR | N | direta | APROVADO |
| D3-R42 | 5.2 | A5.2-12 | C | não | SIT | N | parcial | APROVADO |
| D3-R43 | 5.2 | A5.2-06 | E | sim | DEF | N | direta | APROVADO |
| D3-R44 | 5.2 | A5.2-18 | E | sim | APL | S | parcial | APROVADO |
| D3-R45 | 5.2 | A5.2-07 | C | não | SUJ | N | direta | APROVADO |
| D3-R46 | 5.2 | A5.2-17 | C | não | SIT | N | parcial | APROVADO |
| D3-R47 | 5.2 | A5.2-08 | C | não | SUJ | N | direta | APROVADO |
| D3-R48 | 5.2 | A5.2-13 | E | sim | SUJ | N | parcial | APROVADO |
| D3-R49 | 6.2 | A6.2-02 | E | sim | SUJ | N | direta | APROVADO |
| D3-R50 | 6.2 | A6.2-06 | E | sim | SIT | N | direta | APROVADO |
| D3-R51 | 6.2 | A6.2-04 | C | não | DEF | N | direta | APROVADO |

Percentual de reprovados: **0/30 = 0,0%**. APROVADO 29 (96,7%); AJUSTAR 1 (3,3%); REPROVADO 0.

FIM DO PARECER QA R1 — LEVA 3 — REFORÇO DA
