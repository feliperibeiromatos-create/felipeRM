# T91_reconciliacao_2026-10-18.md — T-91 — 2026-10-18 — gerado por gce-gerencia

Objeto: reconciliação da T-91 (R3, Lote 3, onda 1 do reforço; D-REFORCO-1 e D-REFORCO-2), ciclo 2026-10-18 s12c1.
Base lida: TAREFAS.md (T-91); DECISOES.md (D-REFORCO-1, D-REFORCO-2, D-ADERENCIA, D-QA-PENDENTE); regras/proveniencia.md; regras/estilo_banca.md (5.1); saida/gce/L3_reforco_onda1_v1.md e v2.md (gce-cpp); saida/gce/QA_T91_R1_2026-10-18_gce-cqfp.md (1 reprovado em 11 = 9,1%); saida/gce/QA_T91_R2_2026-10-18_gce-cqfp.md (0 em 11 = 0%; última rodada); saida/gce/QA_T91_normativo_2026-10-18_qa-normativo.md (R09, R10, R11 CONFEREM no planalto, 18/10/2026); saida/gce/T09_decisao_2026-10-13.md (precedente Legin); saida/gcb/T92_D1_2026-10-18.md e T92_reconciliacao_2026-10-18.md (critério da GCB para o teto); PARA_PRESIDENCIA.md (gatilho D da GCB pendente).
A GCE não escreve em PARA_PRESIDENCIA.md nem em TAREFAS.md: os textos das seções 6 e 7 são para o orquestrador colar. Esta reconciliação não muda enunciado, gabarito, [TS] nem justificativa de item (nenhum item canônico é tocado).

## 1. D1 — retirada da marca PENDENTE NORMATIVO de L3-R09, R10, R11: RETIRADA
- O qa-normativo abriu o planalto.gov.br em 18/10/2026 (HTTP 200) e conferiu o literal e o gabarito: Lei 9.610/1998, art. 41 (R09, C); LGPD compilada, art. 48, caput e § 1º (R10, E); LGPD, art. 47 (R11, E). Os três dispositivos estão na redação original. A Lei 15.352/2026 não altera os arts. 47 e 48.
- A condição da R1/R2 ("não canonizar antes da reconferência do qa-normativo") está cumprida. A marca sai dos três itens. A base passa a ser o planalto, com "verificado em 18/10/2026 (qa-normativo)". O Legin fica só como leitura de produção.
- R10 continua sem citar prazo regulamentar da ANPD. A resolução não foi aberta (in.gov.br negado) e segue [SEM FONTE — não afirmar]. O gabarito E não depende dela.
- Grafia: a lei é a 15.352/2026. A nota "15.452" do l13709.htm é erro do planalto e não se cita.
- O gatilho D da GCB (fonte verificada em data anterior) NÃO afeta a T-91. Todas as bases dos 11 itens foram abertas em 18/10/2026: Legin, Microsoft Learn, raw.githubusercontent.com e planalto (pelo qa-normativo).

## 2. D1 — Legin como base do RICD: ACEITO
- O RICD (Resolução nº 17/1989) é norma da Câmara e não está no planalto. O Legin (www2.camara.leg.br/legin, "norma atualizada") é a fonte oficial dele (OUTRA_OFICIAL). Há precedente na D1 GCE de 13/10/2026 (T-09, ADENDO 1 do Lote 2, conferência da GCE-CQFP no Legin).
- A gce-cqfp reabriu e conferiu os literais na R1: art. 73, VI; art. 78; art. 80; art. 97, caput; art. 98, § 2º. Valem para R01, R02, R05 e R06, verificados em 18/10/2026.
- Limite fixado para as próximas ondas: o Legin é base aceita só para normas da Câmara (RICD, resoluções, atos da Mesa). Para lei federal, a base é o planalto conferido pelo qa-normativo (regras/proveniencia.md). Sem essa conferência, o item leva PENDENTE NORMATIVO.

## 3. D1 — formato (R04, novo R07) e teto de 30% (3.1, 3.2, 3.4)
3.1 Critério de classificação (vale para esta e para as próximas ondas da GCE; registrado):
(a) O formato é definido pela construção do ponto de julgamento, e não pelo gabarito. O formato de um item C é o da sua contraparte E.
(b) "Troca de sujeito": o ponto é a atribuição de ação, competência ou propriedade a um sujeito, com um sujeito alternativo explícito ou implícito. Vale para item E (troca feita) e para item C (atribuição correta com o contraste à vista). Sem isso, toda "troca de sujeito" seria E, o que contraria "sem relação fixa entre [TS] e gabarito" (D-REFORCO-1).
(c) "Número ou prazo": o ponto é um valor, prazo, quantidade ou expressão numérica (fórmula incluída), e a versão E se obtém trocando esse valor ou essa expressão. "Definição": o ponto é o conteúdo conceitual de um termo, sem elemento numérico julgado.
3.2 Aplicação:
- L3-R04 (3.2, C) = "número ou prazo". O ponto julgado é a expressão "1 menos a similaridade" e a relação inversa que ela produz. A contraparte E troca a expressão (ex.: "igual à similaridade"). A opinião da gce-cqfp ("na substância, definição") fica registrada como vencida, sem efeito sobre o item, que tem gabarito e base corretos.
- L3-R07 novo (3.4, C) = "troca de sujeito". Atribui as tarefas a "um único modelo", com o contraste explícito "e não por módulos independentes encadeados".
3.3 Teto de 30%. O critério é o mesmo da GCB (T92_D1, 2.1 a 2.4), aplicado para não haver divergência entre Gerências:
- O teto se mede já na folha de 6, contando os itens canônicos com a classificação declarada pela gce-cpp (v2, 1.2).
- O item novo só entra se o seu formato não passar de 30% da folha depois da inclusão.
- O excesso preexistente é LEGADO, registrado e não imputado à onda 1. A correção é por diluição nas ondas seguintes, sem tocar item existente.
Resultado:
- 3.1: aplicação parlamentar 2/6 (Q03, Q04) = LEGADO. R01 (situação hipotética) e R02 (troca de sujeito) usam formatos que tinham 0 ocorrência. Cumpre.
- 3.2: os 6 formatos com 1/6 cada (R03 troca de sujeito; R04 número ou prazo). Cumpre.
- 3.3: os 6 formatos com 1/6 cada. Cumpre.
- 3.4: aplicação parlamentar 2/6 (Q15, Q16) = LEGADO. R07 (troca de sujeito) e R08 (situação hipotética) usam formatos que tinham 0 ocorrência. Cumpre.
- 4.2 e 4.3: os 6 formatos com 1/6 cada. Cumpre.
Até a folha voltar ao teto, nenhum item de reforço usa "aplicação parlamentar" em 3.1 nem em 3.4. A conferência se repete na onda 4.
3.4 Aderência (ajuste da R1, aplicado na v2): parcial em R01, R02 e R05 (ponto regimental em folha de IA; só simulado diagnóstico, D-ADERENCIA); direta nos outros 8. Mantida.
3.5 Ponto único (regra 1 da D-REFORCO-2): sem duplicata, conferido pela gce-cqfp nas duas rodadas, contra os existentes e entre os novos. Vizinhanças aceitas e distintas: R04 × Q05; R07 × Q13; R09 × Q24; R10 × Q29, mesmo artigo, outro parágrafo e outro ponto. Nenhuma rejeição.
3.6 Lapso sem efeito: a R1 fala em "26 itens existentes". As folhas somam 25 (4+4+4+4+5+4 = partida v1.8 da linha T-91). Valem 25.

## 4. D1 — versão final: v2 no mérito, transcrita num v3 com só a troca de metadados de base (FIXADA)
A R2 não pede ajuste de texto de item. Enunciados (Parte 2), gabaritos, [TS] e justificativas da v2 são finais. Por causa da seção 1, a marca e as bases de R09 a R11 têm de mudar. A gce-gerencia não reescreve item. Ela fixa as linhas de metadados abaixo. A gce-cpp grava saida/gce/L3_reforco_onda1_v3.md = v2 com só estas trocas, por transcrição literal (números de linha da v2):

L1 (cabeçalho) →
# L3_reforco_onda1_v3.md — T-91 — 2026-10-18 — gerado por gce-cpp

Inserir, logo depois da linha 1, uma linha em branco e a linha:
Versão v3: transcrição da reconciliação saida/gce/T91_reconciliacao_2026-10-18.md, seção 4. R09, R10 e R11 foram conferidos no planalto pelo qa-normativo em 18/10/2026, e a marca PENDENTE NORMATIVO foi retirada. A resposta ao parecer e os avisos que vêm a seguir são histórico da v2.

L45 →
| L3-R09 | P2-4.2 | Prazo dos direitos patrimoniais: setenta anos, contados de 1º de janeiro do ano subsequente ao do falecimento (aplicável também às obras póstumas). | número ou prazo | Lei 9.610/1998, art. 41, caput e parágrafo único. https://www.planalto.gov.br/ccivil_03/leis/l9610.htm (verificado em 18/10/2026, qa-normativo); leitura de produção no Legin, mesma data | n |

L46 →
| L3-R10 | P2-4.3 | A LGPD não fixa prazo em horas para comunicar incidente: o prazo é "razoável, conforme definido pela autoridade nacional" (art. 48, § 1º). | número ou prazo | Lei 13.709/2018 (LGPD), art. 48, caput e § 1º. https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm (verificado em 18/10/2026, qa-normativo); leitura de produção no Legin, mesma data; ANPD como Agência (Lei 15.352/2026), sem efeito no item | n |

L47 →
| L3-R11 | P2-4.3 | O dever de garantir a segurança da informação persiste mesmo após o término do tratamento (art. 47). | situação hipotética | LGPD, art. 47. https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm (verificado em 18/10/2026, qa-normativo); leitura de produção no Legin, mesma data | n |

L114 →
- Base normativa: o RICD foi lido no Legin, fonte oficial da norma da Câmara (precedente: D1 GCE de 13/10/2026, T-09; D1 da gce-gerencia de 18/10/2026). Para a Lei 9.610/1998 e a LGPD, a base é o planalto.gov.br, conferido pelo qa-normativo em 18/10/2026 (QA_T91_normativo_2026-10-18_qa-normativo.md: R09, R10 e R11 CONFEREM); o Legin fica como leitura de produção. A marca PENDENTE NORMATIVO foi retirada (D1 da gce-gerencia, 18/10/2026).

L202 →
Base: Lei 9.610/1998, art. 41, planalto.gov.br (https://www.planalto.gov.br/ccivil_03/leis/l9610.htm), verificado em 18/10/2026 (qa-normativo); leitura de produção no Legin (norma atualizada), mesma data. Sem [TS]. Não VOLÁTIL.
L203 →
Aderência: direta.

L207 →
Base: LGPD, art. 48, caput e § 1º, planalto.gov.br, texto compilado (https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm), verificado em 18/10/2026 (qa-normativo); leitura de produção no Legin (norma atualizada), mesma data. Não VOLÁTIL.
L208 →
Aderência: direta.

L212 →
Base: LGPD, art. 47, planalto.gov.br, texto compilado (https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm), verificado em 18/10/2026 (qa-normativo); leitura de produção no Legin (norma atualizada), mesma data. Não VOLÁTIL.
L213 →
Aderência: direta.

L222 →
- PENDENTE NORMATIVO: nenhum (marca retirada de R09, R10 e R11 pela D1 da gce-gerencia de 18/10/2026, depois da conferência do qa-normativo no planalto).
L223 →
- Rótulo: AUTORAL em todos. Estado de QA: APROVADO (gce-cqfp, R2, 18/10/2026; reprovação 0%); R09, R10 e R11 CONFEREM no planalto (qa-normativo, 18/10/2026). Aderência parcial em R01, R02 e R05: só simulado diagnóstico (D-ADERENCIA).

L235 →
| planalto.gov.br (Lei 9.610; LGPD, texto compilado; Lei 15.352/2026) | https://www.planalto.gov.br/ccivil_03/leis/l9610.htm; https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm; https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/L15352.htm | 18/10/2026 (qa-normativo; HTTP 200) | R09 (art. 41), R10 (art. 48, caput e § 1º), R11 (art. 47): CONFEREM; a Lei 15.352/2026 não altera os arts. 47 e 48 |

Nada mais muda. As linhas 15, 17, 23 e 27 (resposta ao parecer e avisos) ficam como histórico da v2, e a linha nova inserida depois da linha 1 as marca assim.

Conferência do v3: é feita pela gce-gerencia ou pelo orquestrador, por diff textual v2 → v3. O critério é que só mudem as linhas listadas, com texto idêntico ao fixado aqui, mais a linha inserida. Texto idêntico: não há R3 de QA, porque nenhum enunciado, gabarito, [TS] ou justificativa muda e a nova base é a própria conferência do qa-normativo; valem a seção 6 (CONCLUÍDA) e o gatilho A da seção 7. Texto divergente: a gce-cpp refaz a transcrição; nada vai à Presidência antes disso.

## 5. Contagens finais (v3 = v2 no mérito)
Lote R3: 11 itens AUTORAL. C = 6 (R01, R04, R05, R07, R08, R09); E = 5 (R02, R03, R06, R10, R11). Faixa de 4 a 7 C cumprida; 54,5% fica dentro de 40% a 60% (a regra 5 é da onda e fica para a T-93). [TS] = 5 (R02, R03, R06, R10, R11). VOLÁTIL = 0 (risco alto 0; REVERIFICAR 0). Aderência: 8 direta e 3 parcial (R01, R02, R05). QA: R1 com 1/11 reprovado (9,1%, R07 da v1, substituído); R2 com 0/11 (0%). Gate de 30% não atingido.

| folha | partida v1.8 | novos | nova | C/E novos | [TS] novos | VOLÁTIL folha | formatos (nova folha) | aderência novos |
|---|---|---|---|---|---|---|---|---|
| P2-3.1 | 4 | R01, R02 | 6 | 1 C / 1 E | 1 (R02) | 0/6 | aplicação parlamentar 2/6 (LEGADO), demais ≤ 1 | 2 parcial |
| P2-3.2 | 4 | R03, R04 | 6 | 1 C / 1 E | 1 (R03) | 0/6 | 6 × 1/6 | 2 direta |
| P2-3.3 | 4 | R05, R06 | 6 | 1 C / 1 E | 1 (R06) | 0/6 | 6 × 1/6 | 1 parcial (R05), 1 direta |
| P2-3.4 | 4 | R07, R08 | 6 | 2 C / 0 E | 0 | 0/6 | aplicação parlamentar 2/6 (LEGADO), demais ≤ 1 | 2 direta |
| P2-4.2 | 5 | R09 | 6 | 1 C / 0 E | 0 | 0/6 | 6 × 1/6 | 1 direta |
| P2-4.3 | 4 | R10, R11 | 6 | 0 C / 2 E | 2 (R10, R11) | 0/6 | 6 × 1/6 | 2 direta |
| total | 25 | 11 | 36 | 6 C / 5 E | 5 | 0 | — | 8 direta / 3 parcial |

Pacote: 286 (v1.8) + 11 = 297, só com a R3. A soma das R1, R2 e R4 cabe à T-94 (v1.9).

## 6. Estado da T-91 (texto para o campo de estado da linha T-91; o orquestrador substitui)
Enquanto o v3 não estiver conferido:
EM CURSO (ciclo 2026-10-18 s12c1; QA R2 = 0%; PENDENTE NORMATIVO retirado depois da conferência do qa-normativo no planalto; versão final fixada em saida/gce/T91_reconciliacao_2026-10-18.md, seção 4; aguarda a transcrição literal no v3 pela gce-cpp e a conferência por diff)
Depois do v3 conferido como idêntico:
CONCLUÍDA (18/10/2026, s12c1): 11 de 11 itens L3-R01 a L3-R11 (6 C / 5 E; 5 [TS]; 0 VOLÁTIL; 3 com aderência parcial); folhas 3.1, 3.2, 3.3, 3.4, 4.2 e 4.3 com 6 cada (meta da onda atingida); QA R1 9,1% e R2 0%; R09 a R11 CONFEREM no planalto (qa-normativo); final em saida/gce/L3_reforco_onda1_v3.md; reconciliação e D1 em saida/gce/T91_reconciliacao_2026-10-18.md; gatilho A emitido

## 7. Gatilho A (texto para PARA_PRESIDENCIA.md; colar só depois de conferido o v3)
GATILHO A | GCE | T-91 (R3, Lote 3, onda 1 do reforço, D-REFORCO-1) — aceite INTEGRAL: 11 de 11 itens | saida/gce/L3_reforco_onda1_v3.md; saida/gce/QA_T91_R1_2026-10-18_gce-cqfp.md; saida/gce/QA_T91_R2_2026-10-18_gce-cqfp.md; saida/gce/QA_T91_normativo_2026-10-18_qa-normativo.md; saida/gce/T91_reconciliacao_2026-10-18.md | L3-R01 a L3-R11, todos AUTORAL. Folhas (partida v1.8 → nova): 3.1 4→6, 3.2 4→6, 3.3 4→6, 3.4 4→6, 4.2 5→6, 4.3 4→6; total 25→36; pacote 286→297 só com a R3. Gabarito: 6 C / 5 E (54,5%; faixa de 4 a 7 cumprida). Por folha (C/E novos): 1/1, 1/1, 1/1, 2/0, 1/0, 0/2. [TS]: 5 (R02, R03, R06, R10, R11). VOLÁTEIS: 0 no lote e 0/6 em cada folha. Aderência: 8 direta; 3 parcial (R01, R02, R05; ponto regimental em folha de IA; só simulado diagnóstico, D-ADERENCIA). QA: R1 com 9,1% (R07 da v1 reprovado e substituído); R2 com 0%. Bases abertas em 18/10/2026: RICD no Legin (D1, precedente T-09); Lei 9.610 e LGPD no planalto, conferidas pelo qa-normativo, com PENDENTE NORMATIVO retirado; Microsoft Learn; README oficial openai/whisper (raw.githubusercontent.com). A T-91 não depende do gatilho D da GCB. D1 registradas: critério de formato (o formato segue a construção do ponto, não o gabarito; R04 = número ou prazo; R07 = troca de sujeito); teto de 30% medido já na folha de 6, contando os canônicos, com o mesmo critério da GCB na T-92; LEGADO não imputado: aplicação parlamentar 2/6 em 3.1 (Q03, Q04) e em 3.4 (Q15, Q16), com diluição na onda 4 e sem novo item desse formato nessas folhas até lá. | Pergunta fechada: aceitar os 11 itens L3-R01 a L3-R11 (v3) para consolidação no pacote v1.9 (T-94), com os 3 de aderência parcial restritos a simulado diagnóstico — SIM ou NÃO?

## 8. Ordem imediata
gce-cpp: gravar saida/gce/L3_reforco_onda1_v3.md conforme a seção 4, por transcrição literal, sem nenhuma outra mudança. Em seguida, o orquestrador ou a gce-gerencia confere por diff. Texto idêntico: estado CONCLUÍDA e gatilho A colado.
