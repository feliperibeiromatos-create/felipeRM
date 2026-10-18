# T90_reconciliacao_2026-10-18.md — T-90 — 2026-10-18 — gerado por gce-gerencia

Objeto: reconciliação da T-90 (R2, Lote 2, onda 1 do reforço; D-REFORCO-1 e D-REFORCO-2), ciclo 2026-10-18 s12c1.
Base lida: TAREFAS.md (T-90); DECISOES.md (D-REFORCO-1, D-REFORCO-2, D-ADERENCIA, D-QA-PENDENTE); saida/gce/L2_reforco_onda1_v1.md e v2.md (gce-cpp); saida/gce/QA_T90_R1_2026-10-18_gce-cqfp.md (3/18 reprovados = 16,7%: R09, R10, R11 da v1, substituídos na v2); saida/gce/QA_T90_R2_2026-10-18_gce-cqfp.md (0/18 = 0%; última rodada; ajuste de justificativa do R07 com texto exato; redirecionamento das URLs do Google); saida/gce/QA_T90_normativo_2026-10-18_qa-normativo.md (7 CONFERE, 0 DIVERGE); critérios já fixados em saida/gce/T89_reconciliacao_2026-10-18.md (VOLÁTIL, legado, salvaguarda) e saida/gce/T91_reconciliacao_2026-10-18.md (formato, teto, Legin, transcrição em v3); saida/gcb/T92_reconciliacao_2026-10-18.md (gabarito do R4, para o agregado).
A GCE não escreve em PARA_PRESIDENCIA.md nem em TAREFAS.md: os textos das seções 7 e 8 são para o orquestrador colar. Esta reconciliação não muda enunciado, gabarito nem [TS]; a única mudança de texto de (d-G) é a justificativa do R07, por transcrição literal do texto do parecer R2 (seção 3).

## 1. D1 — retirada da marca PENDENTE NORMATIVO de R01, R02, R05, R07, R08, R14 e R15: RETIRADA
- O qa-normativo abriu as fontes em 18/10/2026 (HTTP 200) e conferiu o literal contra o gabarito: RICD no Legin — art. 98, § 2º (R01, C); art. 57, XVIII (R02, C); art. 176, § 5º (R05, E); art. 41, XXII (R07, só na justificativa); art. 73, VII e VIII (R08, C); Lei 14.133/2021 no planalto — art. 117, caput e § 4º, I e II (R14, E); art. 140, § 3º, com varredura da lei inteira (R15, E). Resultado: 7 CONFERE, 0 DIVERGE. Nenhum dispositivo tem marca de alteração; a Lei 15.266/2025 não altera os arts. 117 e 140; o "quinze dias" do distrator de R15 vem da Lei 8.666/1993, art. 73, I, "a", revogada.
- O texto conferido (enunciado da v1 com o ajuste do R1) coincide com os enunciados da v2, conforme o diff da R2 da gce-cqfp. A condição da R1 está cumprida; a marca sai dos sete itens.
- Base, pelo critério da T-91 (seção 2): RICD no Legin (norma da Câmara, OUTRA_OFICIAL); lei federal no planalto, conferida pelo qa-normativo. Ambos cumpridos.
- Ressalvas do qa-normativo: R02 ("modalidades distintas de registro") já resolvida na v2 ("alternativas distintas"); R07 tratada na seção 3. Nenhuma toca gabarito.

## 2. D1 — aderência de R02, R14 e R15: PARCIAL MANTIDA (só simulado diagnóstico)
- R02 (2.1): o art. 57, XVIII, trata das formas de publicação dos trabalhos de Comissão, não da diferença entre transcrição automática, degravação e revisão. Mesmo critério aplicado a L3-R01, R02 e R05 na T-91 (ponto regimental em folha que não é de norma).
- R14 (2.7) e R15 (2.7): tema de P1-DA 10.6 (papel do fiscal) e 10.4 (recebimento do objeto). Estão na folha 2.7 pelo ângulo de contrato de transcrição, mas o ponto julgado é de Direito Administrativo.
- Decisão: os três ficam no lote, com aderência PARCIAL e uso restrito a simulado diagnóstico (D-ADERENCIA). Contam para a meta de 6 da folha, como na T-91.
- Registro para a onda 3 (P2 2.1 a 2.8): a folha 2.7 fica com 2 de 6 itens de aderência parcial. Até 2.7 ter pelo menos 10 itens, os itens novos dessa folha têm aderência direta (qualidade, revisão, amostragem, SLA), sem novo ponto da Lei 14.133. Vizinhança de escopo com P1-DA 10.4 e 10.6 registrada, sem efeito na regra 1 (que é por folha).

## 3. D1 — justificativa do R07, base do R02 e URLs do Google
3.1 R07: ACEITO o texto exato do parecer R2 (§6), que adota a formulação do qa-normativo. Sem efeito no gabarito E (que se apoia na página "Como pesquisar"). A frase "nem toda reunião de comissão tem nota taquigráfica, pois…" sai, porque o art. 41, XXII, não sustenta a afirmação de fato. Passadas as 2 rodadas de QA, a decisão é desta Gerência (D-REFORCO-1); não há R3, porque o texto é o do próprio QA, conferido contra o literal do artigo pelo qa-normativo.
3.2 R02: ACEITO o acréscimo opcional do art. 57, caput, à base (sugestão do qa-normativo, repetida pela R2). Só metadado de base; enunciado, gabarito e [TS] não mudam.
3.3 URLs do Google: as duas URLs citadas por R10 e R11 (RecognitionConfig e speech.recognize, REST v1) redirecionam com HTTP 301 para docs.cloud.google.com, com destino 200 e "Last updated 2025-10-23 UTC" (gce-cqfp, R2). Destino confirmado por esta Gerência em 18/10/2026 (cabeçalho de redirecionamento): https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig e https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/recognize. Decisão: a URL citada continua válida e permanece nas bases dos itens; a tabela de proveniência registra o destino ao lado. As outras URLs do Google (async-time-offsets, word-confidence; R12 e R13) não tiveram o redirecionamento registrado e ficam como estão; entram na conferência de base de 4–8/1/2027, que registra o destino se houver.
3.4 VOLÁTIL (critério da T-89, seção 1): R07 = VOLÁTIL baixo (organização de um sistema do portal = existência ou organização de recurso que pode mudar); R18 = VOLÁTIL ALTO (limite numérico de produto); R16 = não VOLÁTIL (o gabarito decorre da definição de tesauro); R09, R10, R11 = não VOLÁTEIS (não nomeiam produto; gabarito lógico ou existencial com dois fornecedores). Lote: 2 VOLÁTEIS (teto 4), 1 de risco alto (teto 1). Salvaguarda sem efeito de VOLÁTIL (como na T-89): R03, R04, R09, R10, R11, R12, R13 e R17 na lista de conferência de base de 4–8/1/2027.

## 4. D1 — formato e LEGADO (2.1, 2.2, 2.4, 2.5, 2.6, 2.7)
- Critério de classificação (T-91, 3.1) e de teto (T-91, 3.3, igual ao da GCB na T-92): o formato segue a construção do ponto; o teto de 30% se mede na folha de 6, contando os canônicos pela classificação da CPP; o item novo só entra se o seu formato não passar de 30% depois da inclusão. Classificações da gce-cpp aceitas sem reclassificação (conferidas pela gce-cqfp nas duas rodadas).
- Resultado: nenhum item novo acrescenta ocorrência a formato saturado; em todas as folhas, cada formato dos novos fica em 1/6 ou já era o único da sua classe. Em 2.3 e 2.8, os seis formatos com 1/6 cada.
- LEGADO registrado e não imputado à onda 1 (nenhum item existente muda): 2.1 aplicação parlamentar 2/6 (Q02, Q03); definição 2/6 em 2.2 (Q05, Q06), 2.4 (Q13, Q16), 2.5 (Q17, Q18), 2.6 (Q22, Q23) e 2.7 (Q25, Q27).
- Diluição: na onda 3 (folhas 2.1 a 2.8), até a folha voltar a 30% ou menos, nenhum item de reforço usa "aplicação parlamentar" em 2.1 nem "definição" em 2.2, 2.4, 2.5, 2.6 e 2.7. Com folhas de 20, o legado de 2/6 dilui-se sem restrição adicional depois de 7 itens na folha.
- Ponto único (regra 1): sem duplicata entre os 18 nem contra Q01 a Q30 (gce-cqfp, R1 e R2). Vizinhanças aceitas e distintas: R12 × Q22; R15 × Q27; R17 × Q28; R03 × Q06; R05 × Q14 (mesmo artigo, outro parágrafo e outra folha); R09 × Q17, Q18 e R06; R10 × Q19, Q20; R11 × R13 e Q06. Nenhuma rejeição.

## 5. D1 — versão final: v2 no mérito, transcrita num v3 com metadados de base e a justificativa do R07 (FIXADA)
A R2 não pede ajuste de enunciado, gabarito nem [TS]. Por causa das seções 1 e 3, mudam as marcas PENDENTE NORMATIVO, as bases conferidas, a justificativa do R07 e duas linhas da proveniência. A gce-gerencia não reescreve item: fixa as linhas abaixo. A gce-cpp grava saida/gce/L2_reforco_onda1_v3.md = v2 com só estas trocas, por transcrição literal (números de linha da v2):

L1 (cabeçalho) →
# L2_reforco_onda1_v3.md — T-90 — 2026-10-18 — gerado por gce-cpp

Inserir, logo depois da linha 1, uma linha em branco e a linha:
Versão v3: transcrição da reconciliação saida/gce/T90_reconciliacao_2026-10-18.md, seção 5. R01, R02, R05, R07, R08, R14 e R15 foram conferidos pelo qa-normativo em 18/10/2026 (7 CONFERE), e a marca PENDENTE NORMATIVO foi retirada; a justificativa de R07 segue o texto exato do parecer R2 da gce-cqfp. A resposta ao parecer R1 e as conferências que vêm a seguir são histórico da v2.

L3 →
Rótulo de todos os itens: AUTORAL (produtor gce-cpp, lote L2-R, onda 1 do reforço, D-REFORCO-1/2). QA concluído em 2 rodadas (gce-cqfp: R1 com 3/18 reprovados, substituídos; R2 com 0/18) e reconciliado pela gce-gerencia em 18/10/2026 (saida/gce/T90_reconciliacao_2026-10-18.md); sem QA PENDENTE.

L53 →
| L2-R01 | P2-2.1 | O Deputado que retira o discurso para revisão e não o devolve em cinco sessões tem o texto publicado sem a revisão do orador (RICD) | SH | RICD, art. 98, § 2º: https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html (conferido pelo qa-normativo em 18/10/2026) | n | direta |

L54 →
| L2-R02 | P2-2.1 | Extratos redigidos pelos próprios autores e notas taquigráficas constam do RICD como alternativas distintas de publicação dos trabalhos de Comissão | PC | RICD, art. 57, caput e XVIII (mesma URL do RICD; conferido pelo qa-normativo em 18/10/2026) | n | PARCIAL (D-ADERENCIA: só simulado diagnóstico) |

L57 →
| L2-R05 | P2-2.3 | O aparteante só pode rever o seu aparte se o orador permitir | TS | RICD, art. 176, § 5º (mesma URL do RICD; conferido pelo qa-normativo em 18/10/2026) | n | direta |

L59 →
| L2-R07 | P2-2.4 | Nas reuniões de comissão não há discursos individualizados, só a íntegra das notas taquigráficas (diferente do Plenário) | PC | Câmara, "Como pesquisar" (Banco de Discursos): https://www2.camara.leg.br/atividade-legislativa/discursos-e-notas-taquigraficas/pesquisa/como-pesquisar ; RICD, art. 41, XXII (só na justificativa; conferido pelo qa-normativo em 18/10/2026) | S (BAIXO): descreve a organização de um sistema do portal, em página ainda com o nome anterior do departamento; REVERIFICAR | direta |

L60 →
| L2-R08 | P2-2.4 | Dado o discurso por terminado pelo Presidente, os taquígrafos deixam de registrá-lo | SH | RICD, art. 73, VII e VIII (mesma URL do RICD; conferido pelo qa-normativo em 18/10/2026) | n | direta |

L66 →
| L2-R14 | P2-2.7 | O terceiro contratado pela Administração para assistir o fiscal do contrato não pode exercer atribuição própria e exclusiva de fiscal | AP | Lei 14.133/2021, art. 117, caput e § 4º, I: https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm (verificado em 18/10/2026, qa-normativo) | n | PARCIAL (P1-DA 10.6; D-ADERENCIA: só simulado diagnóstico) |

L67 →
| L2-R15 | P2-2.7 | Os prazos e métodos do recebimento provisório e definitivo são definidos em regulamento ou no contrato, não fixados pela Lei 14.133 | NP | Lei 14.133/2021, art. 140, § 3º (mesma URL de R14; verificado em 18/10/2026, qa-normativo) | n | PARCIAL (P1-DA 10.4; D-ADERENCIA: só simulado diagnóstico) |

L240 →
Base: RICD, art. 98, § 2º ("Caso o orador não devolva o discurso dentro de cinco sessões, a Taquigrafia dará à publicação o texto sem revisão do orador"); a denominação atual do órgão é Derep, antigo DETAQ, Ato da Mesa nº 251/2026, o que não altera o artigo. Conferido pelo qa-normativo no Legin em 18/10/2026. Aderência: direta.

L243 →
Base: RICD, art. 57, caput ("No desenvolvimento dos seus trabalhos, as Comissões observarão as seguintes normas") e XVIII ("poderão ser publicadas as exposições escritas e os resumos das orais, os extratos redigidos pelos próprios Autores, ou as notas taquigráficas, se assim entender a Comissão"). Espelho da troca sutil "extrato = nota taquigráfica". Conferido pelo qa-normativo no Legin em 18/10/2026. Aderência: PARCIAL (o inciso trata das formas de publicação dos trabalhos de Comissão, não da diferença entre transcrição automática, degravação e revisão; D-ADERENCIA: só simulado diagnóstico).

L252 →
Base: RICD, art. 176, § 5º ("Os apartes só serão sujeitos a revisão do Autor se permitida pelo orador, que não poderá modificá-los"). Conferido pelo qa-normativo no Legin em 18/10/2026. Aderência: direta.

L257 →
L2-R07. E. VOLÁTIL (baixo); REVERIFICAR. Nas sessões plenárias há discursos individualizados; nas reuniões de comissão "não há discursos individualizados", apenas a íntegra das notas taquigráficas. Além disso, o registro taquigráfico dos debates em comissão depende de determinação do Presidente da Comissão, quando julgá-lo necessário (RICD, art. 41, XXII).

L258 →
Base: Câmara, "Como pesquisar" (informações sobre notas taquigráficas de Comissões; descrição da organização do sistema, em página ainda com o nome anterior do departamento e sem data de edição, o que a torna sujeita a reorganização); RICD, art. 41, XXII ("determinar o registro taquigráfico dos debates quando julgá-lo necessário"), conferido pelo qa-normativo no Legin em 18/10/2026 (a parte normativa é só a justificativa). Aderência: direta.

L261 →
Base: RICD, art. 73, VII e VIII. Conferido pelo qa-normativo no Legin em 18/10/2026. Aderência: direta.

L279 →
Base: Lei 14.133/2021, art. 117, caput ("permitida a contratação de terceiros para assisti-los") e § 4º, I e II, planalto.gov.br (https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm), verificado em 18/10/2026 (qa-normativo; redação original, não alterada pela Lei 15.266/2025). Aderência: PARCIAL (tema de P1-DA 10.6, "Papel do fiscalizador do contrato"; D-ADERENCIA: só simulado diagnóstico).

L282 →
Base: Lei 14.133/2021, art. 140, § 3º ("Os prazos e os métodos para a realização dos recebimentos provisório e definitivo serão definidos em regulamento ou no contrato"; leitura do art. 140 inteiro: não há prazo numérico para o recebimento provisório), planalto.gov.br, verificado em 18/10/2026 (qa-normativo; redação original, não alterada pela Lei 15.266/2025; o "quinze dias" vem da Lei 8.666/1993, art. 73, I, "a", revogada). Aderência: PARCIAL (tema de P1-DA 10.4; D-ADERENCIA: só simulado diagnóstico).

L305 →
| PENDENTE NORMATIVO | nenhum (marca retirada de R01, R02, R05, R07, R08, R14 e R15 pela D1 da gce-gerencia de 18/10/2026, depois da conferência do qa-normativo: 7 CONFERE). Estado de QA: APROVADO (gce-cqfp, R2, 18/10/2026; reprovação 0%) |

L312 →
| Câmara dos Deputados, Regimento Interno (Resolução nº 17/1989, texto atualizado, Legin) | https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html | verificado em 18/10/2026 (arts. 41, XXII; 57, caput e XVIII; 73, VI a VIII; 98, §§ 1º e 2º; 176, §§ 4º e 5º); reaberto pela gce-cqfp e conferido pelo qa-normativo na mesma data | R01, R02, R05, R07, R08 |

L314 →
| Presidência da República, Lei nº 14.133/2021 (compilada) | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm | verificado em 18/10/2026 (arts. 117 e 140; abre só com User-Agent de navegador; o endereço l14133compilado.htm retorna 404, e o l14133.htm já traz as alterações da Lei 15.266/2025); reaberto pela gce-cqfp e conferido pelo qa-normativo na mesma data | R14, R15 |

L320 →
| Google Cloud, Speech-to-Text, RecognitionConfig (REST v1) | https://cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig (redireciona com HTTP 301 para https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig, HTTP 200) | verificado em 18/10/2026 ("Last updated 2025-10-23 UTC"); redirecionamento registrado pela gce-cqfp na R2 | R10 (transcriptNormalization), R11 (maxAlternatives) |

L321 →
| Google Cloud, Speech-to-Text, speech.recognize (REST v1), SpeechRecognitionResult | https://cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/recognize (redireciona com HTTP 301 para https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/recognize, HTTP 200) | verificado em 18/10/2026 ("Last updated 2025-10-23 UTC"); redirecionamento registrado pela gce-cqfp na R2 | R11 |

Nada mais muda. As linhas 8 a 43 (resposta ao parecer R1 e conferências) ficam como histórico da v2, e a linha nova inserida depois da linha 1 as marca assim. A legenda da linha 237 (definição de PENDENTE NORMATIVO) fica, porque é legenda.

Conferência do v3: é feita pela gce-gerencia ou pelo orquestrador, por diff textual v2 → v3. O critério é que só mudem as 22 linhas listadas (L1, L3, L53, L54, L57, L59, L60, L66, L67, L240, L243, L252, L257, L258, L261, L279, L282, L305, L312, L314, L320, L321), com texto idêntico ao fixado aqui, mais a linha em branco e a linha inseridas depois da linha 1. Texto idêntico: não há R3 de QA, porque nenhum enunciado, gabarito ou [TS] muda, a justificativa do R07 é o texto do próprio QA e as bases novas são a própria conferência do qa-normativo; valem a seção 7 (CONCLUÍDA) e o gatilho A da seção 8. Texto divergente: a gce-cpp refaz a transcrição; nada vai à Presidência antes disso.

## 6. Contagens finais (v3 = v2 no mérito)
Lote R2: 18 itens AUTORAL. C = 8 (R01, R02, R06, R08, R10, R11, R13, R18); E = 10 (R03, R04, R05, R07, R09, R12, R14, R15, R16, R17). 44,4% de C: faixa de 7 a 11 C cumprida. [TS] = 10 (R02, R03, R04, R05, R09, R12, R14, R15, R16, R17; 1 com gabarito C, R02, falsa pegadinha). VOLÁTIL = 2 (R07 baixo; R18 ALTO, inapto a simulado final até 4–8/1/2027); existentes no lote 0. Aderência: 15 direta, 3 parcial (R02, R14, R15). QA: R1 com 3/18 reprovados (16,7%; R09, R10, R11 da v1, substituídos por itens de 2.5 e 2.6); R2 com 0/18 (0%). Gate de 30% não atingido.

| folha | partida v1.8 | novos (gab.) | nova | C/E novos | [TS] novos | VOLÁTIL folha | formatos (nova folha) | aderência novos |
|---|---|---|---|---|---|---|---|---|
| P2-2.1 | 4 | R01 C, R02 C | 6 | 2 C / 0 E | 1 (R02) | 0/6 | aplicação parlamentar 2/6 (LEGADO), demais ≤ 1 | 1 direta, 1 parcial (R02) |
| P2-2.2 | 4 | R03 E, R04 E | 6 | 0 C / 2 E | 2 (R03, R04) | 0/6 | definição 2/6 (LEGADO), demais ≤ 1 | 2 direta |
| P2-2.3 | 4 | R05 E, R06 C | 6 | 1 C / 1 E | 1 (R05) | 0/6 | 6 × 1/6 | 2 direta |
| P2-2.4 | 4 | R07 E, R08 C | 6 | 1 C / 1 E | 0 | 1/6 (R07, baixo) | definição 2/6 (LEGADO), demais ≤ 1 | 2 direta |
| P2-2.5 | 4 | R09 E, R10 C | 6 | 1 C / 1 E | 1 (R09) | 0/6 | definição 2/6 (LEGADO), demais ≤ 1 | 2 direta |
| P2-2.6 | 3 | R11 C, R12 E, R13 C | 6 | 2 C / 1 E | 1 (R12) | 0/6 | definição 2/6 (LEGADO), demais ≤ 1 | 3 direta |
| P2-2.7 | 4 | R14 E, R15 E | 6 | 0 C / 2 E | 2 (R14, R15) | 0/6 | definição 2/6 (LEGADO), demais ≤ 1 | 2 parcial |
| P2-2.8 | 3 | R16 E, R17 E, R18 C | 6 | 1 C / 2 E | 2 (R16, R17) | 1/6 (R18, ALTO) | 6 × 1/6 | 3 direta |
| total | 30 | 18 | 48 | 8 C / 10 E | 10 | 2 (1 alto) | — | 15 direta / 3 parcial |

Pacote: 286 (v1.8) + 18 = 304, só com a R2. A soma das R1, R3 e R4 cabe à T-94 (v1.9).

## 7. Estado da T-90 (texto para o campo de estado da linha T-90; o orquestrador substitui)
Enquanto o v3 não estiver conferido:
EM CURSO (ciclo 2026-10-18 s12c1; QA R1 16,7% e R2 0%; PENDENTE NORMATIVO retirado dos 7 itens depois da conferência do qa-normativo (7 CONFERE); versão final fixada em saida/gce/T90_reconciliacao_2026-10-18.md, seção 5; aguarda a transcrição literal no v3 pela gce-cpp e a conferência por diff)
Depois do v3 conferido como idêntico:
CONCLUÍDA (18/10/2026, s12c1): 18 de 18 itens L2-R01 a L2-R18 (8 C / 10 E; 10 [TS]; 2 VOLÁTEIS, R07 baixo e R18 alto; 3 com aderência parcial, R02, R14, R15, só simulado diagnóstico); folhas 2.1 a 2.8 de 4, 4, 4, 4, 4, 3, 4, 3 para 6 cada (30 → 48; meta da onda atingida); QA R1 16,7% (R09 a R11 da v1 substituídos) e R2 0%; 7 itens CONFEREM (qa-normativo; RICD no Legin, Lei 14.133 no planalto); legado de formato registrado (2.1 AP; 2.2, 2.4, 2.5, 2.6, 2.7 D); final em saida/gce/L2_reforco_onda1_v3.md; reconciliação e D1 em saida/gce/T90_reconciliacao_2026-10-18.md; gatilho A emitido

## 8. Gatilho A (texto para PARA_PRESIDENCIA.md; colar só depois de conferido o v3)
GATILHO A | GCE | T-90 (R2, Lote 2, onda 1 do reforço, D-REFORCO-1) — aceite INTEGRAL: 18 de 18 itens | saida/gce/L2_reforco_onda1_v3.md; saida/gce/QA_T90_R1_2026-10-18_gce-cqfp.md; saida/gce/QA_T90_R2_2026-10-18_gce-cqfp.md; saida/gce/QA_T90_normativo_2026-10-18_qa-normativo.md; saida/gce/T90_reconciliacao_2026-10-18.md | L2-R01 a L2-R18, todos AUTORAL. Folhas (partida v1.8 → nova): 2.1 4→6, 2.2 4→6, 2.3 4→6, 2.4 4→6, 2.5 4→6, 2.6 3→6, 2.7 4→6, 2.8 3→6; total 30→48; pacote 286→304 só com a R2. Gabarito: 8 C / 10 E (44,4%; faixa de 7 a 11 cumprida). Por folha (C/E novos): 2/0, 0/2, 1/1, 1/1, 1/1, 2/1, 0/2, 1/2. [TS]: 10 (R02, R03, R04, R05, R09, R12, R14, R15, R16, R17; 1 C). VOLÁTEIS: 2 no lote (R07 baixo, 2.4 = 1/6; R18 ALTO, 2.8 = 1/6, inapto a simulado final até 4–8/1/2027); teto de 4 e de 1 alto cumpridos. Aderência: 15 direta; 3 parcial (R02, ponto regimental em 2.1; R14 e R15, temas de P1-DA 10.6 e 10.4 em 2.7; só simulado diagnóstico, D-ADERENCIA). QA: R1 com 16,7% (R09, R10, R11 da v1 reprovados por escopo e substituídos); R2 com 0%. Normativo: R01, R02, R05, R07, R08 (RICD, Legin) e R14, R15 (Lei 14.133, planalto) CONFEREM (qa-normativo, 18/10/2026), PENDENTE NORMATIVO retirado. Demais bases abertas em 18/10/2026 (Microsoft Learn, AWS, Google Cloud — 2 URLs com 301 para docs.cloud.google.com, destino registrado —, repositório oficial openai/whisper). D1 registradas: justificativa do R07 pelo texto exato da R2; LEGADO não imputado de formato (2.1 aplicação parlamentar 2/6; definição 2/6 em 2.2, 2.4, 2.5, 2.6 e 2.7), com diluição na onda 3 e sem novo item desses formatos nessas folhas até lá; critérios de formato, teto e VOLÁTIL iguais aos das T-89 e T-91. | Pergunta fechada: aceitar os 18 itens L2-R01 a L2-R18 (v3) para consolidação no pacote v1.9 (T-94), com os 3 de aderência parcial restritos a simulado diagnóstico e o R18 inapto a simulado final até a reverificação — SIM ou NÃO?

## 9. Gabarito agregado da onda 1 na GCE (para a T-93; última reconciliação da onda na GCE)

| tarefa | lote | itens | C | E | % C | [TS] | VOLÁTEIS novos | aderência parcial | QA (R1 / R2) | versão final |
|---|---|---|---|---|---|---|---|---|---|---|
| T-89 | R1 (L1-R01 a R18) | 18 | 9 | 9 | 50,0% | 7 | 0 | 0 | 0% / 0% | L1_reforco_onda1_v2.md |
| T-90 | R2 (L2-R01 a R18) | 18 | 8 | 10 | 44,4% | 10 | 2 (R07 baixo; R18 alto) | 3 (R02, R14, R15) | 16,7% / 0% | L2_reforco_onda1_v3.md (após conferência) |
| T-91 | R3 (L3-R01 a R11) | 11 | 6 | 5 | 54,5% | 5 | 0 | 3 (L3-R01, R02, R05) | 9,1% / 0% | L3_reforco_onda1_v3.md |
| GCE | R1 + R2 + R3 | 47 | 23 | 24 | 48,9% | 22 (46,8%) | 2 | 6 | — | — |

- Regra 5 (40% a 60% de C na onda): a parte da GCE fica em 48,9%. Com o R4 efetivo da GCB (T-92: L6A-R01, 0 C / 1 E), a onda soma 48 itens, 23 C / 25 E = 47,9%. O saldo da T-102 (L6B-R01, R02) não muda a faixa: com 0, 1 ou 2 C nos 2 itens, a onda fica entre 46,0% e 50,0%. A conferência formal é da T-93.
- Amostra da T-93: há itens aceitáveis de R1, R2 e R3 na GCE; R2 entra com 18 itens.
- [TS] acumulado de reforço na GCE: 22/47 (46,8%). A instrução da T-89 para a onda 2 (pelo menos metade dos itens da onda mais 2 com [TS]) continua.
- VOLÁTEIS por lote depois da onda: Lote 1 = 4 (1 alto; sem folga); Lote 2 = 2 (1 alto, R18); Lote 3 = 0.
- LEGADOS de formato a diluir: onda 2 (1.2 e 1.4 D; 1.4, 1.5 e 1.6 PC; 1.8 VOLÁTIL 2/6); onda 3 (2.1 AP; 2.2, 2.4, 2.5, 2.6, 2.7 D; 2.7 aderência parcial 2/6); onda 4 (3.1 e 3.4 AP).

## 10. Ordem imediata
gce-cpp: gravar saida/gce/L2_reforco_onda1_v3.md conforme a seção 5, por transcrição literal, sem nenhuma outra mudança. Em seguida, o orquestrador ou a gce-gerencia confere por diff. Texto idêntico: estado CONCLUÍDA (seção 7) e gatilho A (seção 8) colados.
