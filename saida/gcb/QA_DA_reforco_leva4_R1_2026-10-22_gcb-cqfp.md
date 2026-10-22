# QA_DA_reforco_leva4_R1_2026-10-22_gcb-cqfp.md — T-116 — 2026-10-22 — gerado por gcb-cqfp

# PARECER QA R1 — REFORÇO DA, LEVA 4 (v1) — ciclo s16c2
Objeto: saida/gcb/DA_reforco_leva4_v1.md (28 itens: D3-R52 a D3-R59, folha 6.2, segunda parte; D2-R01 a D2-R10, folha 3.1; D2-R11 a D2-R20, folha 3.2). Critérios: ficha saida/gcb/DA_reforco_ficha_2026-10-20.md, seção 4 (4.1 a 4.4) e seção 10.4, com as seções 1, 7, 8.2 (itens 4 e 7), 9.3 e 10.2 (o adendo 10 prevalece). A gcb-cqfp não produziu este texto e não o reescreve: o ajuste vem em texto exato (ficha, seção 4.3). Esta leva não tem errata a conferir (ficha, seção 10.3). Sem commit nem push; nenhum outro arquivo foi alterado.

## 0. Resultado
- **APROVADO: 27. AJUSTAR: 1** (D3-R54; 1 AJ de texto exato). **REPROVADO: 0.**
- **Taxa de reprovação: 0/28 = 0,0%** (limite 30%): sem gate. A leva segue para a v2.
- Conferências de leva (ficha 4.4): 8 de 8 CONFEREM. Nenhuma conferência NÃO CONFERE. Grafia do host da Fonte 4 registrada (seção 1).
- Errata: nenhuma a conferir nesta leva (ficha 10.3).

## 1. Entradas (SHA-256 em disco, 22/10/2026) e método
| objeto | SHA-256 |
|---|---|
| saida/gcb/DA_reforco_leva4_v1.md | 7b0c1dc7c38d1b92de08b3e4c21676df9591a5a13122b5de7670d65642e0f3d8 (= despacho) |
| saida/gcb/DA_reforco_ficha_2026-10-20.md | 777e6eb6a2d871f5d6afc26b22a479a9ccfcb9ede3285d68ab06e391c761a03a (= despacho) |
| saida/gcb/D2_anexo_N_mapa_normativo.md | b0a54fff4ddcf21a693e01ba71032efccf72e0a6fdf912221ff05413cc0e340a (= ficha 10.4.2) |
| saida/gcb/D3_anexo_N_adendo_2026-10-20.md | bbfd3eed1a69edef189a1fb8f07fee901daaf5bb636d8192bb1442e53a3fa797 (= ficha 10.4.2) |
| saida/gcb/D2_v2_1.md | 59cffaa689ea869cd11c13e6a833470b0b91d24b0f25ea2cc2e100ac9be8bd2c |
| saida/gcb/D3_v2_1.md | 0f7a8b090fe6f2243ae55b36273dacdb719aaf04b19548dce70aad4867798930 |
| saida/gcb/DA_reforco_leva1_v2.md / leva2_v2.md / leva3_v2.md | 2c431529…4f04 / 5baec20d…1bbe / e4c2a911…3237 (= D-T116-LEVA1/2/3-ACEITE) |
| normativo_cache/CF_1988_compilada_2026-10-20.txt | d6580cb327147e1beb69ccd09cd930613c06f39e1791b235729930a01cacb51d |
| normativo_cache/Lei_8112_1990_compilada_2026-10-20.txt | 72f45d30dcf096207898d143ba551758e3ffac89e87d6dd2d42044fe65202efe |
| normativo_cache/Lei_10406_2002_CodigoCivil_compilada_2026-10-20.txt | 97e0ffaa7e5b92d072622c9bde5ebdab9121cd32913c4292cb0c5f74a914a828 |
| normativo_cache/Lei_13869_2019_2026-10-20.txt | fb3b95c117e64fc0f26f0a915af3ae433d6ceb3aad2434fc5dcae72a64f04a33 |
| normativo_cache/Lei_9494_1997_2026-10-20.txt | e0cde6a9c898133d726ae193d1bc589b72e1bd1a47ca4e6361c6d0f51102ee94 |
| normativo_cache/Decreto_9830_2019_2026-10-20.txt | ae022402edcf1e5dfb951947d3f9c9f4323c957a2adeb7ac87f3601a213fb232 |
| saida/banco/moldura_ce_itens_2026-10-20.csv | (lido; DA com moldura 44 C / 9 E; D2 9/1; 3.1 D2-05 e D2-10 (C); 3.2 D2-19 (E) — iguais à v1, 4.4) |

Lidos também: regras/ (PADRAO_UNICO_v1.md, proveniencia.md, padrao_resposta_cebraspe.md, estilo_banca_semente.md), CLAUDE.md e, em DECISOES.md, D-REFORCO-DA (l. 173), D-REFORCO-2 (l. 95), D-MOLDURA-CE (l. 171), D-T116-LEVA1-ACEITE (l. 175), D-T116-LEVA2-ACEITE (l. 176) e D-T116-LEVA3-ACEITE (l. 177). Modelo de forma: saida/gcb/QA_DA_reforco_leva3_R1_2026-10-22_gcb-cqfp.md.

Método: leitura integral das seções 0 a 6 da v1; cada item confrontado com a linha do Anexo N do D2 (seção 3, mapa; seções 4.1 e 4.3, texto; 5.2, alertas) ou do Adendo 2 do adendo do D3 (A2.3.2, A2.4.1, A2.4.4 a A2.4.7, A2.5.2) e com a cópia em saida/gcb/normativo_cache/; canônicos das três folhas relidos no pacote.json v1.13 (ordem do pacote) e no D2_v2_1.md / D3_v2_1.md ([TS]); itens das levas 1 a 3 relidos nos finais. Scripts próprios (python3 -I, somente leitura, no scratchpad da sessão, fora do repositório): check.py (blocos, 13 campos, trechos × seção do Anexo/adendo × cópia, URL × primeira linha da cópia, data, palavras por trecho), seq.py (folhas acumuladas reconstruídas do pacote.json v1.13 + levas 1 a 3 + leva 4; teste da regra 6), e verificações de enunciado (abertura, fórmula, absolutos, termos do Legislativo, unicidade do texto do AJ).

Rede: tentativas de abrir https://www.planalto.gov.br/ccivil_03/leis/l8112compilado.htm e https://planalto.gov.br/ccivil_03/leis/l8112compilado.htm em 22/10/2026 (20h26 UTC) por curl: "Empty reply from server", código 000 nas duas (bloqueado, como diz o despacho). Nenhuma página oficial foi reaberta; nada foi substituído por memória. As bases foram conferidas nas cópias oficiais gravadas em 20/10/2026.

Grafia do host da Fonte 4 (Lei 8.112): no Anexo N do D2, seção 1, a Fonte 4 está grafada **https://planalto.gov.br/ccivil_03/leis/l8112compilado.htm** (sem "www"); a primeira linha da cópia Lei_8112_1990_compilada_2026-10-20.txt traz **URL: https://www.planalto.gov.br/ccivil_03/leis/l8112compilado.htm** (com "www"). Mesma página, diferença só de grafia do host; os 9 itens da Lei 8.112 (D2-R11, R12, R13, R15, R16, R17, R18, R19, R20) usam a URL do Anexo, como a ficha 10.4.2 manda. Comparação sem o prefixo "www.": igual em 28 de 28; comparação literal: igual em 19 de 28 (as 9 diferenças são todas desta grafia). Registrado; não é desvio.

## 2. Veredito por item
Legenda: G = gabarito pela letra; P = ponto único; T = troca legítima e única / [TS]; F = sem pista de forma; Pe = pertinência à folha; Gê = não gêmeo (canônico da folha, levas 1 a 3, própria leva); M = moldura; J = justificativa e proveniência. ✓ confere; ✗ não confere; ~ confere com ajuste. "l." = linha da cópia em normativo_cache/; "Anexo l." / "adendo l." = linha do arquivo de lastro.

### Folha 6.2 — D3-R52 a D3-R59 (segunda parte; Adendo 2 do adendo do D3)
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D3-R52 | C ✓ | ✓ | sem [TS] ✓ | ✓ | parcial ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CC, art. 932, caput e III, literal (cópia l. 1807 e 1810; adendo l. 456–457). Sujeito da letra ("o empregador ou comitente"); nada diz do Estado (C9). Pertinência parcial aceita (seção 7, dúvida viii). |
| D3-R53 | C ✓ | ✓ | sem [TS] ✓ | ✓ | parcial ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CF, art. 5º, XXIV (cópia l. 76; adendo l. 406). "far-se-á mediante justa e prévia indenização" é a leitura direta de "procedimento para desapropriação …, mediante justa e prévia indenização em dinheiro"; ressalva final literal. Não chama a desapropriação de responsabilidade civil (C9). Cenário com a União, sem órgão do Legislativo. Único CQ da 6.2 com a fórmula "Nessa situação, nos termos d…" (1 de 2; 7.4.3). |
| D3-R54 | E ✗ → ~ | ✓ | [TS] erro grosseiro → culpa ✓ | ✓ | direta ✓ | ✓ (nota) | N ✓ | ✓ | **AJUSTAR** (AJ-1) | Decreto 9.830, art. 14 (cópia l. 109; adendo l. 451). Dúvida (i) da produção respondida: com "depende de", o E fica **discutível**. "Depende de X" afirma só condição necessária; o art. 14 exige dolo ou erro grosseiro, e o próprio Decreto, art. 12, § 1º (cópia l. 96; usado no D1-R02, leva 2, aceito), define erro grosseiro como o "praticado com culpa grave". Quem tem dolo ou erro grosseiro tem dolo ou culpa; logo "o regresso depende de dolo ou culpa" é verdadeiro como condição necessária, e o item admite recurso (ficha 4.1, item 2). O AJ-1 põe a moldura da própria letra sem o absoluto ("será exercido na hipótese de"), que a ficha 10.4.4 manda tirar: o item passa a afirmar que a culpa (qualquer) basta para o regresso, o que contradiz o "somente … dolo ou erro grosseiro" da letra. O E então sai da letra do art. 14 e não depende de afirmar a relação com o "dolo ou culpa" da CF (C6, [SEM FONTE] mantido). Ponto, gabarito, [TS], Troca, mecanismo E1, formato DEF, abertura DC, Base e Justificativa ficam. O texto do AJ-1 é idêntico, letra por letra, ao AJ-L4-E2 da gbq-estilo (saida/banco/estilo_DA_reforco_leva4.md, que deixa a decisão ao R1): é um só ajuste, aplicado uma vez. Nota nova (ao): D3-R54 com D1-58 (LINDB, "dolo ou culpa, ainda que leve") e D1-R02 (erro grosseiro = culpa grave). |
| D3-R55 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota af) | N ✓ | ✓ | **APROVADO** | Lei 9.494, art. 1º-C (cópia l. 14; adendo l. 446). Parte verdadeira por si, sem marcador de exclusividade (C6). Sem termo inicial (C8). Dúvida (ii): **não é gêmeo** do D3-R49. A regra 2 da ficha veda o mesmo dispositivo com o mesmo elemento, e o adendo mapeia A6.2-01 e A6.2-02 como pontos distintos; o D3-R49 julga a inclusão das prestadoras. Registro: o enunciado do D3-R49 contém, como primeira oração verdadeira, a proposição do D3-R55; juntos no mesmo simulado, um entrega o outro, e por isso a nota (af) é **obrigatória**, não facultativa. |
| D3-R56 | C ✓ | ✓ | sem [TS] ✓ | ✓ | parcial ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CC, art. 949, literal (cópia l. 1835; adendo l. 465). "o ofensor" é o sujeito da letra; nada diz do Estado (C9). CQ com C (L4-2) e norma no fim ("conforme o art. 949"), sem a fórmula. Amostra da gbq-estilo. |
| D3-R57 | E ✓ | ✓ | [TS] a requerimento do ofendido → de ofício ✓ | ✓ | parcial ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Lei 13.869, art. 4º, caput e I (cópia l. 40–41; adendo l. 439–440). Uma só troca (impulso), E pela letra. O obrigado é o condenado (C11); o item não fala do Estado. Pertinência parcial aceita com registro (seção 7, dúvida viii). É o indireto mais fraco da folha: o alerta C11 diz "só como contraste". |
| D3-R58 | E ✓ | ✓ | [TS] solidariamente → na proporção da participação ✓ | ✓ | parcial ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CC, art. 942, caput (cópia l. 1822; adendo l. 460). Troca única de conceito vizinho (E1); o parágrafo único não é usado. C9 cumprido. |
| D3-R59 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota ae) | N ✓ | ✓ | **APROVADO** | CF, art. 5º, LXXV, primeira hipótese (cópia l. 149; adendo l. 407). Parte verdadeira por si, sem "somente" (C6). Nada sobre atos jurisdicionais em geral (C7). Ponto distinto do D3-R50 (A6.2-05 × A6.2-06). |

### Folha 3.1 — D2-R01 a D2-R10 (Anexo N do D2, seção 4.1; Fonte 1)
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D2-R01 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CF, art. 37, XVII (cópia l. 606; Anexo l. 201), literal; a vírgula omitida antes de "e sociedades controladas" não muda o sentido. Fecha a alternância de 4 do fim dos canônicos. |
| D2-R02 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CF, art. 37, IV (cópia l. 590; Anexo l. 185). Prioridade no prazo do edital; não toca o inciso III (D2-02). |
| D2-R03 | E ✓ | ✓ | [TS] afastado → regime do inciso III ✓ | ✓ | direta ✓ | ✓ (nota ah) | S, órgão/servidor ✓ | ✓ | **APROVADO** | CF, art. 38, I (cópia l. 635; contraste l. 637; Anexo l. 230). E pela letra: o inciso I manda afastar, sem exceção de compatibilidade, e o regime das vantagens com compatibilidade é o do vereador (inciso III). A moldura não decide: o cenário só põe o servidor em órgão do Legislativo. Dúvida (x): "servidor público da administração direta, ocupante de cargo efetivo em órgão do Poder Legislativo da União" é claro, porque o órgão do Legislativo da União integra a administração direta; não nomeia parlamentar nem Casa. Os "sem" do fecho são letra do inciso III. |
| D2-R04 | E ✓ | ✓ | [TS] lei específica → lei complementar ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CF, art. 37, VII (cópia l. 593; Anexo l. 188). Troca única de instrumento; sem jurisprudência. |
| D2-R05 | E ✓ | ✓ | [TS] cargo de origem → cargo de destino ✓ | ✓ | direta ✓ | ✓ (nota aj) | S, órgão/servidor ✓ | ✓ | **APROVADO** | CF, art. 37, § 13 (cópia l. 630; Anexo l. 225). Troca única, por contradição expressa; a moldura não decide. Amostra da gbq-estilo; o AJ-L4-E1 do estilo (só extensão: retira "desde que possua a habilitação…") não muda ponto, gabarito, Troca nem trecho da Base e não conflita com o AJ-1. O R2 confere os dois. |
| D2-R06 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CF, art. 37, XIV, literal (cópia l. 600; Anexo l. 195). C3 (dupla negação literal). |
| D2-R07 | E ✓ | ✓ | [TS] 70 → 65 ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CF, art. 40, § 1º, II (cópia l. 659; Anexo l. 253; EC 88/2015). Dúvida (iii): manter "ou aos 75 anos, na forma de lei complementar" não denuncia a troca. É a estrutura literal do inciso, e a troca de um só número é o modelo da regra 7. Não usa o § 4º nem o § 5º-A (alerta 1; EC 140/2026). Observação, sem AJ: a justificativa (linha 2) chama a idade do inciso III de "aposentadoria voluntária". O inciso III não traz a palavra, mas o § 19 do mesmo art. 40 (cópia l. 682) fala em "aposentadoria voluntária", e a classificação decorre da estrutura do § 1º; não é afirmação fora da base que afete o gabarito. |
| D2-R08 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CF, art. 37, § 10 (cópia l. 627; Anexo l. 222). Aplica a ressalva dos cargos em comissão; "Vide EC 20/1998" não afeta. O "comissão" do enunciado é "cargo em comissão", não comissão legislativa. |
| D2-R09 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CF, art. 39, § 2º (cópia l. 648; Anexo l. 242; EC 19/1998; sem "Vide" no parágrafo; a "Vide ADI 2.135" é do caput, que não é usado). |
| D2-R10 | E ✓ | ✓ | [TS] reconduzido → reintegrado ✓ | ✓ | direta ✓ | ✓ (nota ai) | S, órgão/servidor ✓ | ✓ | **APROVADO** | CF, art. 41, § 2º (cópia l. 701; Anexo l. 296). Dúvida (iv): repetir "reintegrado" é a própria troca (E1). Reintegração e recondução são institutos distintos da letra, e o E é nítido; não é pista de forma. O "sem direito a indenização" é letra. A moldura não decide. |

### Folha 3.2 — D2-R11 a D2-R20 (Anexo N do D2, seções 4.3 e 4.1; Fontes 4 e 1)
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D2-R11 | E ✓ | ✓ | [TS] posse → nomeação ✓ | ✓ | direta ✓ | ✓ (nota an) | N ✓ | ✓ | **APROVADO** | Lei 8.112, art. 7º (cópia l. 43; Anexo l. 337; "compl. 3.2"). Troca única. |
| D2-R12 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Lei 8.112, art. 4º, literal (cópia l. 25; Anexo l. 319; "núcleo 3.2"). |
| D2-R13 | E ✓ | ✓ | [TS] quarenta → quarenta e quatro ✓ | ✓ | direta ✓ | ✓ (nota ak) | N ✓ | ✓ | **APROVADO** | Lei 8.112, art. 19, caput (cópia l. 90; Anexo l. 384; Lei 8.270/1991). Dúvida (v): o formato fica **NUM**, como declarado. O que se julga é o número, e o cenário só repete a primeira parte da regra; sem AJ. Se a reconciliação o lesse como SIT, a 3.2 ficaria com SIT 6 (no teto) e NUM 2, ainda dentro da regra 4. |
| D2-R14 | E ✓ | ✓ | [TS] a lei → o edital do concurso ✓ | ✓ | direta ✓ | ✓ (nota am) | N ✓ | ✓ | **APROVADO** | CF, art. 39, § 3º (cópia l. 649; Anexo l. 243: "Edital: núcleo 3.1; compl. 3.2"). Dúvida (vii): a pertinência **direta** à 3.2 é aceita. O dispositivo está marcado "compl. 3.2" e trata da admissão ao cargo (ficha 10.4.2). O item atribui ao art. 39, § 3º, uma faculdade do edital que a letra dá à lei: troca de elemento (regra 8), não "E por ausência". O ator posto é plausível e conhecido pela fonte do tema (10.2, item 6). Observação, sem AJ: "requisitos diferenciados de admissão de servidores ocupantes de cargo público" segue a letra do § 3º ("Aplica-se aos servidores ocupantes de cargo público…") e não muda o gabarito. Amostra da gbq-estilo. |
| D2-R15 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Lei 8.112, art. 19, § 1º (cópia l. 91; Anexo l. 385). "sempre que" é literal (C com absoluto literal; L3-2). A omissão da remissão ao art. 120 e da "função de confiança" deixa uma parte verdadeira por si. Registro: a abertura "Considere que servidor ocupe cargo em comissão" repete quase literalmente a do canônico D2-38 (3.4), de outra folha (fora da L3-3); nota sugerida (ap). |
| D2-R16 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota al) | N ✓ | ✓ | **APROVADO** | Lei 8.112, art. 5º, § 3º, literal (cópia l. 41; Anexo l. 335). |
| D2-R17 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Lei 8.112, art. 15, caput, literal (cópia l. 79; Anexo l. 373; Lei 9.527/1997). Nenhum canônico do D2 julga o art. 15 (busca no pacote v1.13). |
| D2-R18 | E ✓ | ✓ | [TS] até 20% → no mínimo 20% ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Lei 8.112, art. 5º, § 2º (cópia l. 40; Anexo l. 334). Dúvida (vi): "pessoas portadoras de deficiência" é o termo literal do dispositivo, e o enunciado nomeia a lei; fica por fidelidade à letra (regra 9). Reserva CF, art. 37, VIII: nunca no mesmo simulado. |
| D2-R19 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Lei 8.112, art. 120, caput, literal (cópia l. 605; Anexo l. 893; "compl. 3.2"). |
| D2-R20 | E ✓ | ✓ | [TS] exonerado → demitido ✓ | ✓ | direta ✓ | ✓ (nota an) | N ✓ | ✓ | **APROVADO** | Lei 8.112, art. 34, parágrafo único, II (cópia l. 164–167; Anexo l. 458 e 460); o art. 15, § 2º (cópia l. 81) diz o mesmo. Dúvida (xi): o "não" do cenário é a hipótese da letra, e o fecho troca a consequência por conceito vizinho (E1), sem negá-la. Cumpre a 10.2, item 5. |

## 3. Reprovação e substituto
Nenhum item reprovado. Nenhuma reposição de E com moldura é necessária (ficha 10.5, item 3). A 6.2 fecha em 20 com os 5 parciais aceitos; nenhuma reserva da 6.2 é chamada.

## 4. Ajuste em texto exato (ficha, seção 4.3; o "substituir" ocorre 1 vez no arquivo e o "por" 0 vez, conferido por script)
`AJ-1 | D3-R54 | enunciado (seção 1) | substituir: «depende de o agente público ter agido com dolo ou culpa em suas decisões ou opiniões técnicas.» | por: «será exercido na hipótese de o agente público ter agido com dolo ou culpa em suas decisões ou opiniões técnicas.»`

Efeito: o enunciado vira «Segundo o Decreto nº 9.830/2019, no âmbito do Poder Executivo federal, o direito de regresso previsto no § 6º do art. 37 da Constituição Federal será exercido na hipótese de o agente público ter agido com dolo ou culpa em suas decisões ou opiniões técnicas.» Gabarito E, [TS], Troca (dolo ou erro grosseiro → dolo ou culpa), mecanismo E1, formato DEF, aderência direta, abertura declarativa, Base e Justificativa ficam. O enunciado continua sem "somente", "apenas" ou "só" (ficha 10.4.4). Simulação por script: só a linha 28 do arquivo muda. Nenhuma contagem da seção 4 muda (abertura, absolutos, fórmula, moldura, sequência); o enunciado passa de 42 para 45 palavras. **O AJ-1 e o AJ-L4-E2 da gbq-estilo têm o mesmo texto: a v2 aplica a substituição uma única vez**, e a reconciliação a registra como um só ajuste, com as duas origens.

## 5. Conferências de leva (ficha, seção 4.4)
| # | conferência | resultado |
|---|---|---|
| 1 | C/E da leva | **CONFERE**: 15 C / 13 E (53,6%; faixa 12–16 em 28). Sequência CCECCEECCCEEECECCEECEECCCECE, igual à ficha 10.4.7. Folhas fechadas: 6.2 10/10; 3.1 10/10; 3.2 10/10 (faixa 8–12 C). |
| 2 | tetos por folha | **CONFERE**: formatos da leva 6.2 1/2/2/1/2/0, 3.1 2/2/2/1/0/3, 3.2 2/2/3/2/1/0 (DEF/SUJ/SIT/NUM/PAR/APL), iguais à ficha 10.4.4; com os canônicos (ficha 10.4.5): 6.2 5/3/6/1/5/0 (SIT 6, no teto), 3.1 5/3/3/3/1/5, 3.2 5/5/5/3/1/1 (teto 6 de 20). VOLÁTIL 0; REVERIFICAR 0 (nenhuma redação de 2025/2026; EC 88/2015, EC 103/2019, EC 19/1998 e EC 20/1998 anteriores a 2/10/2026). Moldura por folha: 6.2 0, 3.1 5, 3.2 1 (≤ 6). Piso de 10 diretos: 6.2 15; 3.1 20; 3.2 20. |
| 3 | moldura acumulada e conjuntos | **CONFERE**: moldura nova 0 C / 3 E (D2-R03, R05, R10; tipo "órgão/servidor do Poder Legislativo da União", cota da 3.1). CSV: DA 44/9, D2 9/1. Levas 1 a 3: 2/9 + 2/3 + 1/4. DA 49/25 → **49/28 (63,6%)**, igual à ficha 2.2 e 10.4.6. D2 9/1 → **9/4 (69,2%)**. D3 9/11 sem item novo com moldura. K1 a K4, fecho neutro e ", e não" do D4 sem item novo. Termos do Legislativo só nos 3 itens S; os "comissão" de D2-R08, R15 e R19 são "cargo em comissão". |
| 4 | pontos sem duplicata | **CONFERE**: 28 pontos distintos. Na 6.2: A6.2-01, 03, 05, 07, 10, 12, 13, 14, distintos dos da leva 3 (02, 04, 06) e dos canônicos (CF, art. 37, § 6º; CC, art. 43; base doutrinária). Na 3.1 e na 3.2, nenhum dispositivo coincide com os pontos dos canônicos (ficha 10.4.3). Os mesmos dispositivos com outro elemento (D3-R54 × R51; R55 × R49; R59 × R50) têm "Difere de" e nota. Excluídos respeitados: CC, arts. 186 e 927; Lei 8.112, art. 122; CF, art. 37, XVI, b; art. 40, §§ 4º e 5º-A; art. 39, caput; art. 37, § 6º, XII; art. 39, § 6º; Lei 8.112, arts. 20, § 4º, 41, § 5º, 49, § 1º, e 135; estágio probatório. |
| 5 | exigências da leva | **CONFERE**: aderência parcial em 5 (D3-R52, R53, R56, R57, R58), igual à 10.4.6, pertinência aceita (seção 7). L4-1: 0 fecho "é correto afirmar que". L4-2: a 6.2 fecha com CQ 3 C / 3 E (D3-R53 e R56, ambos C). L3-1/7.4.2: leva CQ 6 C / 5 E (54,5% de C); declarativos 9 C / 8 E (47,1% de E). Folhas fechadas: 6.2 CQ 3/3 e DC 7/7; 3.1 CQ 4/4 e DC 6/6; 3.2 CQ 4/3 e DC 6/7. Fórmula "Nessa situação, nos termos d…": na 6.2 em 1 de 2 CQ (D3-R53); no D2 em 3 de 9 (D2-R03, R08, R19). L3-2: um só absoluto, "sempre que" no D2-R15, literal, em C; nenhum E com absoluto inserido. L3-3: nenhum cenário idêntico até o fecho na mesma folha. L3-4 e L3-5: 0 "mas não" ou ", e não"; 0 "mero", "por si só" ou "simples". L4-3 e L4-4: nenhum E6 e nenhum E3 que condicione hipótese autônoma. 10.2, itens 5 e 6: conferidos (D2-R03, R10, R20; D2-R14). |
| 6 | primeiro e último id por lote | **CONFERE**: D3-R52 a D3-R59 (6.2) e D2-R01 a D2-R20 (3.1, 3.2), contínuos, como na ficha 10.1 e 10.4.1. Nenhum id no pacote.json v1.13 (1.159 itens) nem nas levas 1 a 3. Primeiro id do D2 = D2-R01 (regra 12). |
| 7 | linha 1 e última linha | **CONFERE**: "# DA_reforco_leva4_v1.md — T-116 — 2026-10-22 — gerado por gcb-cpp"; "FIM DA LEVA 04 — REFORÇO DA". |
| 8 | bases reabertas no cache | **CONFERE**: os 39 trechos dos 28 itens são subcadeia da seção citada do Anexo ou do adendo (39/39) e da cópia em normativo_cache/ (39/39; espaços normalizados), cada um 1 vez na cópia. Maior soma por item: 25 palavras (D3-R52, D2-R09; limite 25). "consulta 20/10/2026" em 28/28. URL igual à do Anexo/adendo em 28/28 e à da primeira linha da cópia, sem "www.", em 28/28 (grafia da Fonte 4 na seção 1). Reabertas com linha (amostra ≥ 5): CF (l. 76, 149, 590, 593, 600, 606, 627, 630, 635, 637, 648, 649, 659, 660, 682, 701); Lei 8.112 (l. 25, 40, 41, 43, 79, 81, 90, 91, 164–167, 605); CC (l. 1807, 1810, 1822, 1835); Lei 13.869 (l. 40–41); Lei 9.494 (l. 14); Decreto 9.830 (l. 95–96, 109). |
| — | teste de sequência (regra 6; 7.3; 8.2, item 7) | **CONFERE** (seq.py; folhas reconstruídas do pacote v1.13 na ordem do pacote + levas 1 a 3 + leva 4). Leva e folhas da leva passam, no gabarito e no [TS]. Acumuladas: 6.2 gabarito ECEECCEECEECCCECCEEC reprova só por p4 8/8 nas posições 2–9, legado canônico já registrado (8.2, item 7), sem janela que inclua item novo; [TS] passa. 3.1 passa: o p6 chega a 11/12, mais perto do limite. 3.2 passa. Valores iguais aos da v1, 4.3. O AJ-1 não muda gabarito nem [TS]. |
| — | integridade dos blocos | 28 blocos com os 13 campos; Troca ⇔ [TS] ⇔ "TS=sim" (13/13, todos E; 0 C-isca); itemEdital P1-DA-<folha>, AUTORAL e QA PENDENTE em 28/28; seção 1 sem gabarito, [TS], URL ou marcas; 0 "exceto", "R$", "NGP", "Vide", "STF" em enunciado; núcleo false em 28/28 (ficha 10.1). |

## 6. Errata
Nenhuma errata a conferir nesta leva (ficha, seção 10.3: AJ-L2-E1 já CONFERIDA no R1 da leva 3; o estilo da leva 3 não propôs errata pós-R2).

## 7. Dúvidas e desvios declarados pela produção (seções 5 e 6 da v1)
| # | dúvida ou desvio | avaliação |
|---|---|---|
| (i) / 6.2.1 | D3-R54: "depende de" e alerta C6 | **Não aceito como está** → AJ-1. Com "depende de", o E é discutível, porque o próprio Decreto (art. 12, § 1º) faz do erro grosseiro uma culpa grave. Com "será exercido na hipótese de", o E sai da letra. C6 cumprido: nome, alcance, sem moldura, sem afirmar a relação com a CF. |
| (ii) | D3-R55, possível gêmeo do D3-R49 | **Aceito**: não é gêmeo pela regra 2 (A6.2-01 × A6.2-02). A nota (af) é obrigatória, porque o D3-R49 contém a proposição do D3-R55. |
| (iii) | D2-R07: "aos 65 anos de idade, ou aos 75 anos" | **Aceito**: estrutura literal; troca única de número. |
| (iv) | D2-R10: "reintegrado" repetido | **Aceito**: é a troca (E1) fixada pela ficha. |
| (v) | D2-R13: formato NUM com "Considere que" | **Aceito** como NUM; sem AJ. |
| (vi) | D2-R18: "portadoras de deficiência" | **Aceito** (literal; regra 9). |
| (vii) | D2-R14: pertinência direta à 3.2 | **Aceita** (Anexo l. 243, "compl. 3.2"; ficha 10.4.2). |
| (viii) | 5 parciais da 6.2 (C9, C11) | **Aceitos os 5**: D3-R52 (CC, art. 932, III), R53 (CF, art. 5º, XXIV), R56 (CC, art. 949), R58 (CC, art. 942) e R57 (Lei 13.869, art. 4º, I). O adendo os classifica como "indireta" (A2.3.2), nenhum afirma que o Estado responde por esses artigos, e o R53 não chama a desapropriação de responsabilidade civil. Registro: o D3-R57 é o de pertinência mais fraca. O C11 o admite "só como contraste", e o item cumpre isso porque nomeia o condenado e não o Estado. Os 5 vão só a simulado diagnóstico (nota v). Nenhuma reserva é chamada. |
| (ix) | grafia do host da Fonte 4 | **Registrada** (seção 1); URL do Anexo mantida, como manda a ficha 10.4.2. |
| (x) | D2-R03: "administração direta" com moldura | **Aceito**: leitura clara (seção 2). |
| (xi) | D2-R20: "não" no cenário | **Aceito**: é hipótese, e a consequência é trocada, não negada (10.2, item 5). |
| 6.1 | 28 linhas iguais à ficha 10.4.4 | **Conferido** (formato, moldura, gabarito, [TS], aderência, abertura e ponto). |
| 6.2.2–6.2.12 | redação, fórmula, moldura, D2-R05, D2-R08, D2-R13, D2-R15, mecanismos, SUJ/PAR, trechos com "[…]" | **Aceitos**. Cada trecho com "[…]" é subcadeia contínua do lastro e da cópia, e a soma fica ≤ 25 palavras. Mecanismos sem reclassificação. |

## 8. Lista para a v2 (gcb-cpp) e notas à GCB
1. Aplicar o AJ-1 por substituição exata, sem outra mudança. Ele é o mesmo texto do AJ-L4-E2 do estilo: aplicar uma só vez. Aplicar também o AJ-L4-E1 do estilo (D2-R05), que não conflita com o AJ-1. Refazer por script as seções 0 e 4; nenhuma contagem deve mudar.
2. O R2 confere os ajustes aplicados literalmente e examina só o que a v2 mudar além deles.
3. Notas de simulado, à GCB e sem decisão desta QA:
   - aceitas com os ids finais: (ae), (af) (obrigatória: o D3-R49 contém o D3-R55), (ag), (ah) a (an), (v), (w), (x), e os acréscimos da produção (D2-R19 × D2-15; D2-R04 × D2-09; D3-R57 × D3-R44/R46; A6.2-08 × D3-R52; D2-R17 no conjunto (an));
   - nova (ao): D3-R54 × D1-58 × D1-R02 (Decreto 9.830, art. 14, × LINDB, art. 28, "culpa, ainda que leve", × conceito de erro grosseiro). É gêmeo entre lotes evitado (regra 2): a troca do D3-R54 é a mesma família da troca do D1-58;
   - nova (ap): D2-R15 × D2-38. A abertura de cenário quase idêntica ("Considere que servidor ocupe cargo em comissão…") fica em folhas distintas (3.2 e 3.4).
4. Núcleo (ficha 10.1): todos os 28 ficam false. Confere com a v1.
5. Para a leva 5, só registro: a moldura de DA fica em 49 C / 28 E (63,6%) e a do D2 em 9/4 (69,2%), como a ficha prevê. A meta da D-MOLDURA-CE continua na leva 5.

## 9. Tabela-resumo dos 28 itens
| id | folha | ponto | gab. | [TS] | formato | moldura | aderência | veredito |
|---|---|---|---|---|---|---|---|---|
| D3-R52 | 6.2 | A6.2-07 (CC, art. 932, III) | C | não | SUJ | N | parcial | APROVADO |
| D3-R53 | 6.2 | A6.2-12 (CF, art. 5º, XXIV) | C | não | SIT | N | parcial | APROVADO |
| D3-R54 | 6.2 | A6.2-03 (Decreto 9.830, art. 14) | E | sim | DEF | N | direta | AJUSTAR (AJ-1) |
| D3-R55 | 6.2 | A6.2-01 (Lei 9.494, art. 1º-C) | C | não | NUM | N | direta | APROVADO |
| D3-R56 | 6.2 | A6.2-14 (CC, art. 949) | C | não | SIT | N | parcial | APROVADO |
| D3-R57 | 6.2 | A6.2-13 (Lei 13.869, art. 4º, I) | E | sim | PAR | N | parcial | APROVADO |
| D3-R58 | 6.2 | A6.2-10 (CC, art. 942) | E | sim | PAR | N | parcial | APROVADO |
| D3-R59 | 6.2 | A6.2-05 (CF, art. 5º, LXXV) | C | não | SUJ | N | direta | APROVADO |
| D2-R01 | 3.1 | CF, art. 37, XVII | C | não | SUJ | N | direta | APROVADO |
| D2-R02 | 3.1 | CF, art. 37, IV | C | não | SIT | N | direta | APROVADO |
| D2-R03 | 3.1 | CF, art. 38, I | E | sim | APL | S | direta | APROVADO |
| D2-R04 | 3.1 | CF, art. 37, VII | E | sim | DEF | N | direta | APROVADO |
| D2-R05 | 3.1 | CF, art. 37, § 13 | E | sim | APL | S | direta | APROVADO |
| D2-R06 | 3.1 | CF, art. 37, XIV | C | não | DEF | N | direta | APROVADO |
| D2-R07 | 3.1 | CF, art. 40, § 1º, II | E | sim | NUM | N | direta | APROVADO |
| D2-R08 | 3.1 | CF, art. 37, § 10 | C | não | SIT | N | direta | APROVADO |
| D2-R09 | 3.1 | CF, art. 39, § 2º | C | não | SUJ | N | direta | APROVADO |
| D2-R10 | 3.1 | CF, art. 41, § 2º | E | sim | APL | S | direta | APROVADO |
| D2-R11 | 3.2 | Lei 8.112, art. 7º | E | sim | PAR | N | direta | APROVADO |
| D2-R12 | 3.2 | Lei 8.112, art. 4º | C | não | DEF | N | direta | APROVADO |
| D2-R13 | 3.2 | Lei 8.112, art. 19, caput | E | sim | NUM | N | direta | APROVADO |
| D2-R14 | 3.2 | CF, art. 39, § 3º | E | sim | SUJ | N | direta | APROVADO |
| D2-R15 | 3.2 | Lei 8.112, art. 19, § 1º | C | não | SIT | N | direta | APROVADO |
| D2-R16 | 3.2 | Lei 8.112, art. 5º, § 3º | C | não | SUJ | N | direta | APROVADO |
| D2-R17 | 3.2 | Lei 8.112, art. 15, caput | C | não | DEF | N | direta | APROVADO |
| D2-R18 | 3.2 | Lei 8.112, art. 5º, § 2º | E | sim | NUM | N | direta | APROVADO |
| D2-R19 | 3.2 | Lei 8.112, art. 120 | C | não | SIT | N | direta | APROVADO |
| D2-R20 | 3.2 | Lei 8.112, art. 34, par. ún., II | E | sim | SIT | N | direta | APROVADO |

Percentual de reprovados: **0/28 = 0,0%**. APROVADO 27 (96,4%); AJUSTAR 1 (3,6%); REPROVADO 0.

FIM DO PARECER QA R1 — LEVA 4 — REFORÇO DA
