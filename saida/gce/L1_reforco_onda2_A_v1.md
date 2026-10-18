# L1_reforco_onda2_A_v1.md — T-96 — 2026-10-18 — gerado por gce-cpp

Tarefa T-96, onda 2 do reforço, parte A (ciclo s12c3). Escopo: P2 folhas 1.1 e 1.2, 28 itens AUTORAL novos, ids L1-R19 a L1-R46 (L1-R19 a L1-R32 na folha 1.1; L1-R33 a L1-R46 na folha 1.2). Cada folha passa de 6 para 20 itens. As folhas 1.3 a 1.8 são das outras produtoras da onda 2 e não aparecem aqui.
Rótulo de todos os itens: AUTORAL (produtora gce-cpp, lote L1-R, onda 2 do reforço, D-REFORCO-2). QA PENDENTE: nenhum item deste arquivo passou por QA (D-QA-PENDENTE); não entra em simulado antes disso.
Convenção de base: "verificado em 18/10/2026" significa página aberta e lida nesta data, nesta sessão. Nenhuma base de data anterior (D-FONTE-DATA-ANTERIOR) foi usada. Nenhuma norma foi citada. Itens não citam versão, preço ou limite de produto.
Critérios aplicados: D-REFORCO-1 e D-REFORCO-2 (um ponto de julgamento por item, único na folha; formato declarado; no máximo 30% de um formato por folha de 20; no máximo 20% de VOLÁTEIS por folha; gabarito da parte entre 40% e 60% de C); critério de VOLÁTIL da T89_reconciliacao seção 1 (D-T89-R1-ACEITE); restrições da T-89 para a onda 2 ([TS] em pelo menos metade dos itens mais 2; nenhum item com formato "definição" na folha 1.2); registros O-1 a O-8 da T-93.

=====================================================================
PARTE 1/3 — MAPA
=====================================================================

## 1.1 Itens novos (um ponto de julgamento por item)

Formatos: D = definição; TS = troca de sujeito; SH = situação hipotética; NP = número ou prazo; PC = par confundível; AP = aplicação parlamentar.

### Folha P2-1.1 (L1-R19 a L1-R32)

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL |
|---|---|---|---|---|---|
| L1-R19 | P2-1.1 | O denominador do WER é o número de palavras da transcrição de referência, e não o da hipótese (N = 50, 6 erros: WER = 12%) | NP | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data (seção "Evaluate word error rate (WER)"); https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm (seção "Scoring process": percentuais sobre palavras de referência) | n |
| L1-R20 | P2-1.1 | O padrão dos erros orienta a correção: substituições em termos do domínio associam-se a amostra insuficiente de termos do domínio, e o sinal fraco associa-se às supressões | AP | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data (seção "Resolve errors and improve WER") | n |
| L1-R21 | P2-1.1 | Falhas da transcrição de referência distorcem o WER também quando o sistema acerta e a referência erra; a precisão da medida acompanha a precisão da referência | SH | https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm (seção "Dynamic Programming string alignment": precisão das estatísticas diretamente correlacionada à acurácia do texto de referência) | n |
| L1-R22 | P2-1.1 | Testar a acurácia com áudio diferente do usado no ajuste do modelo dá noção mais realista do desempenho | SH | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data (nota do passo de criação do teste) | n |
| L1-R23 | P2-1.1 | Recomendação coincidente de dois fornecedores: áudio em formato sem perda (FLAC; WAV PCM 16 bits); codecs com perda podem reduzir a acurácia | AP | https://cloud.google.com/speech-to-text/docs/best-practices (tabela de recomendações); https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html (seção "Media formats") | n |
| L1-R24 | P2-1.1 | Segundo a documentação do Google, o processamento de redução de ruído aplicado antes do envio tende a reduzir, e não a elevar, a acurácia | PC | https://cloud.google.com/speech-to-text/docs/best-practices (seção "Audio preprocessing") | S (baixo) |
| L1-R25 | P2-1.1 | Não reamostrar: capturar a 16.000 Hz ou mais quando possível, e enviar áudio de telefonia (nativo comum de 8.000 Hz) na taxa nativa | NP | https://cloud.google.com/speech-to-text/docs/best-practices (tabela e seção "Sampling rate"); https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html (seção "Sample rates") | n |
| L1-R26 | P2-1.1 | O alinhamento entre hipótese e referência, prévio à contagem de erros, é feito por programação dinâmica que minimiza globalmente uma distância de edição ponderada | D | https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm (seção "Step 2: Text Alignments") | n |
| L1-R27 | P2-1.1 | Inserção é palavra acrescentada na hipótese; supressão é palavra pronunciada e não reconhecida (papéis trocados no item) | TS | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data (seção "Evaluate word error rate (WER)") | n |
| L1-R28 | P2-1.1 | Ferramentas de pontuação admitem transcrições alternativas de referência para trechos ambíguos, sem penalizar o sistema que emite qualquer delas | AP | https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm (seção "Step 2": transcrições de referência alternativas) | n |
| L1-R29 | P2-1.1 | Segundo a documentação do Google, vozes simultâneas ou em volumes diferentes, em canal único, podem ser interpretadas como ruído de fundo e ignoradas | AP | https://cloud.google.com/speech-to-text/docs/best-practices (tabela de recomendações) | S (baixo) |
| L1-R30 | P2-1.1 | A pontuação-padrão trata todos os erros de palavra com o mesmo peso; a ponderação por palavra é variação opcional | PC | https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm (seções "Word Error Scoring" e "Weighted-Word Scoring") | n |
| L1-R31 | P2-1.1 | A taxa de erro de sentença é a razão entre pares referência–hipótese incorretos e o total de pares, e não de palavras erradas sobre palavras | PC | https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm (seção "Scoring process", "Percent of sentence errors") | n |
| L1-R32 | P2-1.1 | O sistema pode produzir versões alternativas do mesmo trecho, cada uma com pontuação de confiança; em regra, entrega a de maior confiança | D | https://docs.aws.amazon.com/transcribe/latest/dg/alternatives.html | n |

### Folha P2-1.2 (L1-R33 a L1-R46)

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL |
|---|---|---|---|---|---|
| L1-R33 | P2-1.2 | No Whisper, a previsão em cada janela é autorregressiva (sequência a sequência): cada token depende dos anteriores | PC | https://raw.githubusercontent.com/openai/whisper/main/README.md (repositório oficial openai/whisper, seção "Python usage") | n |
| L1-R34 | P2-1.2 | O wav2vec 2.0 aprende representações de fala a partir de dados não rotulados (pré-treinamento auto-supervisionado), o que permite aproveitar acervo sem transcrição | AP | https://raw.githubusercontent.com/facebookresearch/fairseq/main/examples/wav2vec/README.md (repositório oficial facebookresearch/fairseq) | n |
| L1-R35 | P2-1.2 | Composição dos dados do Whisper: 680 mil horas; a maior parcela (65%) é áudio em inglês com transcrição em inglês | NP | https://raw.githubusercontent.com/openai/whisper/main/model-card.md (seção "Training Data") | n |
| L1-R36 | P2-1.2 | O desempenho de transcrição em um idioma se correlaciona diretamente com a quantidade de dados de treino nesse idioma | SH | https://raw.githubusercontent.com/openai/whisper/main/model-card.md (seção "Training Data") | n |
| L1-R37 | P2-1.2 | O fornecedor recomenda avaliação robusta no contexto e no domínio de uso antes de implantar o modelo | AP | https://raw.githubusercontent.com/openai/whisper/main/model-card.md (seção "Evaluated Use") | n |
| L1-R38 | P2-1.2 | A repetição de texto é propensão da arquitetura sequência a sequência, mitigada em parte, e não eliminada, por beam search e ajuste de temperatura | AP | https://raw.githubusercontent.com/openai/whisper/main/model-card.md (seção "Performance and Limitations") | n |
| L1-R39 | P2-1.2 | Modelo end-to-end CTC ou de transdutor admite, na decodificação, modelo de linguagem treinado só com texto, sem retreinar o modelo de fala | SH | https://raw.githubusercontent.com/NVIDIA/NeMo/main/docs/source/asr/intro.rst (item "Language Modeling"); https://raw.githubusercontent.com/espnet/espnet/master/README.md (seção "ASR: Automatic Speech Recognition") | n |
| L1-R40 | P2-1.2 | O XLSR-53, variante multilíngue do wav2vec 2.0, foi pré-treinado com 53 idiomas, entre os quais o português | NP | https://raw.githubusercontent.com/facebookresearch/fairseq/main/examples/wav2vec/README.md (tabela do XLSR e lista de conjuntos MLS e CommonVoice) | n |
| L1-R41 | P2-1.2 | Em modelos híbridos CTC/atenção, a decodificação conjunta com CTC serve para reforçar o alinhamento monotônico entre áudio e texto | PC | https://raw.githubusercontent.com/espnet/espnet/master/README.md (seção "ASR: Automatic Speech Recognition", item "Hybrid CTC/attention") | n |
| L1-R42 | P2-1.2 | Combinar dados de múltiplos domínios no pré-treinamento é estratégia documentada diante da mudança de domínio | AP | https://raw.githubusercontent.com/facebookresearch/fairseq/main/examples/wav2vec/README.md (parágrafo "Robust wav2vec 2.0") | n |
| L1-R43 | P2-1.2 | O desempenho do modelo é desigual entre sotaques e dialetos de um mesmo idioma (e entre grupos de falantes) | AP | https://raw.githubusercontent.com/openai/whisper/main/model-card.md (seção "Performance and Limitations") | n |
| L1-R44 | P2-1.2 | Em sua forma original, o Whisper não pode ser usado para transcrição em tempo real "out of the box" | SH | https://raw.githubusercontent.com/openai/whisper/main/model-card.md (seção "Broader Implications") | n |
| L1-R45 | P2-1.2 | Para áudio longo, modelos end-to-end recorrem a atenção local ou restrita no codificador e a processamento em blocos | SH | https://raw.githubusercontent.com/NVIDIA/NeMo/main/docs/source/asr/intro.rst (item "Long Audio"); https://raw.githubusercontent.com/espnet/espnet/master/README.md (item "Restricted Self-Attention") | n |
| L1-R46 | P2-1.2 | Em vários benchmarks, o desempenho end-to-end é comparável ou superior ao dos sistemas híbridos DNN/HMM, o que não equivale a superioridade em qualquer condição | PC | https://raw.githubusercontent.com/espnet/espnet/master/README.md (item "State-of-the-art performance in several ASR benchmarks") | n |

VOLÁTIL novos: 2 (R24 e R29, ambos da folha 1.1, risco baixo; dependem de recomendação vigente na documentação do Google, página com "Last updated 2026-10-13"). Risco alto: 0.

## 2 Itens já existentes por folha e contagem da folha de 20

Fonte dos existentes: saida/pacote/pacote.json v1.9 (itemEdital P2-1.1 e P2-1.2), conferido contra saida/gce/GCE_Lote1_v2_CPP.md, GCE_Lote1C_v2_CPP.md, GCE_Lote1_consolidacao_GCE.md e L1_reforco_onda1_v2.md. Formato dos existentes: classificação do mapa canônico da onda 1 (L1_reforco_onda1_v2.md, seção "Itens já existentes").

### P2-1.1 (6 existentes + 14 novos = 20)
| id | ponto | formato | VOL |
|---|---|---|---|
| L1-Q01 | WER 0% não garante fidelidade em pontuação, capitalização e locutor | D | n |
| L1-Q02 | ASR não atribui falas a locutores (isso é diarização/identificação) | PC | n |
| L1C-Q21 | Funções invertidas: modelo acústico × modelo de linguagem | TS | n |
| L1C-Q22 | WER pode ultrapassar 100% (inserções) | NP | n |
| L1-R01 | WER depende do conjunto de áudio avaliado; não se transfere a outras condições | SH | n |
| L1-R02 | Saída do ASR traz marcas de tempo e confiança por palavra | AP | n |
| L1-R19 a R32 | ver tabela acima | NP, AP, SH, SH, AP, PC, NP, D, TS, AP, AP, PC, PC, D | n (12) / S (2) |

Contagem de formatos na folha de 20: D 3 (Q01, R26, R32) = 15%; PC 4 (Q02, R24, R30, R31) = 20%; TS 2 (Q21, R27) = 10%; NP 3 (Q22, R19, R25) = 15%; SH 3 (R01, R21, R22) = 15%; AP 5 (R02, R20, R23, R28, R29) = 25%. Soma 20. Maior formato: AP com 25% (teto de 30% cumprido).
VOLÁTEIS na folha: 2/20 = 10% (R24, R29; teto de 20% cumprido); existentes: 0.

### P2-1.2 (6 existentes + 14 novos = 20)
| id | ponto | formato | VOL |
|---|---|---|---|
| L1-Q03 | End-to-end não é imune a alucinação | D | n |
| L1-Q04 | "Supervisão fraca" ainda usa pares áudio–texto | PC | n |
| L1C-Q23 | Sem dicionário de pronúncias; correção de nome próprio passa por adaptação ou mais dados | SH | n |
| L1C-Q24 | Em muitos sistemas há espectrograma antes da rede (não universal) | D | n |
| L1-R03 | Tarefa do Whisper definida por tokens especiais do decodificador | TS | n |
| L1-R04 | Whisper processa áudio longo em janelas sucessivas de 30 segundos | NP | n |
| L1-R33 a R46 | ver tabela acima | PC, AP, NP, SH, AP, AP, SH, NP, PC, AP, AP, SH, SH, PC | n (14) |

Contagem de formatos na folha de 20: D 2 (Q03, Q24) = 10%, sem item novo de definição (restrição da T-89, seção 3); PC 4 (Q04, R33, R41, R46) = 20%; TS 1 (R03) = 5%; NP 3 (R04, R35, R40) = 15%; SH 5 (Q23, R36, R39, R44, R45) = 25%; AP 5 (R34, R37, R38, R42, R43) = 25%. Soma 20. Maior formato: SH e AP com 25% (teto de 30% cumprido).
VOLÁTEIS na folha: 0/20.

### Verificação de não repetição
Em cada folha, o ponto de cada item novo foi comparado, um a um, com os pontos listados acima (existentes) e entre si; nenhum repete ponto. Proximidades que a Gerência pode querer ver:
- R19 × L1C-Q22 (1.1): ambos tocam o cálculo do WER; Q22 julga o limite superior (WER pode passar de 100%), R19 julga o denominador (referência, não hipótese).
- R32 × L1-R02 (1.1): ambos citam confiança; R02 julga a confiança e o tempo por palavra na saída e seus usos; R32 julga a existência de versões alternativas do trecho, com a de maior confiança entregue em regra.
- R27, R30, R31 × R19 (1.1): todos usam termos do cálculo de erro, mas cada um julga um ponto distinto (classificação inserção/supressão; peso uniforme × ponderado; taxa por sentença × por palavra).
- R39 × L1C-Q23 (1.2): ambos tratam de adaptação em modelo end-to-end; Q23 julga a ausência de dicionário de pronúncias separado, R39 julga a incorporação de modelo de linguagem externo na decodificação.
- R36 × L1-R11 (1.6, outra folha): R11 julga a variação entre idiomas e a não transferência do WER do inglês; R36 julga a correlação com a quantidade de dados de treino. Folhas diferentes, sem conflito de regra.
- R43 (1.2) toca o tema de sotaques da folha 1.6 e R44 (1.2) toca o de tempo real da folha 1.7; em ambos o enunciado julga uma limitação documentada do modelo end-to-end, em outra folha. A Gerência decide se mantém (dúvida registrada na Parte 3).
- R45 × L1-R04 (1.2): R04 julga a janela deslizante de 30 s do Whisper; R45 julga estratégias arquiteturais de outros toolkits para áudio longo.

### Tetos (resumo da parte)
- Formato: maior formato por folha = 25% (AP em 1.1; SH e AP em 1.2); teto de 30% cumprido; "definição" em 1.2: 0 novos.
- VOLÁTIL: 2 novos (1.1), 0 de risco alto; 1.1 = 2/20 (10%); 1.2 = 0/20.
- Gabarito da parte: 14 C e 14 E (50% de C), dentro de 11 a 17 C. Por folha: 1.1 com 7 C e 7 E; 1.2 com 7 C e 7 E.
- [TS]: 16/28 (57%), acima do mínimo de metade mais 2 (16). 12 em itens E e 4 em itens C (espelho); 2 itens E sem [TS] (R21, R38).

FIM DA PARTE 1/3

=====================================================================
PARTE 2/3 — (d) ITENS DO ESTUDANTE
=====================================================================

L1-R19. Julgue o item.
Na avaliação de um sistema de reconhecimento automático de fala, a transcrição de referência de um trecho de comissão tem 50 palavras. A hipótese gerada pelo sistema contém 3 substituições, 1 supressão e 2 inserções, de modo que tem 51 palavras. Nesse caso, o WER é de cerca de 11,8%, resultado da divisão do total de erros (6) pelo número de palavras da hipótese.

L1-R20. Julgue o item.
A equipe constatou que, na transcrição automática de sessões de comissão, predominavam substituições em nomes de proposições e de parlamentares. A documentação da Microsoft costuma associar esse padrão de erro à amostra insuficiente de termos do domínio, e relaciona o sinal de áudio fraco, sobretudo, às supressões.

L1-R21. Julgue o item.
Em avaliação do WER de um sistema, a degravação usada como referência continha omissões e erros de grafia. Como o WER resulta da comparação entre hipótese e referência, tais falhas da referência só distorcem a medida nos trechos em que o sistema comete exatamente o mesmo erro da referência.

L1-R22. Julgue o item.
Depois de ajustar um modelo de reconhecimento de fala com gravações de sessões da Casa, a equipe avaliou sua acurácia com áudios diferentes dos usados no ajuste, porque, segundo a documentação da Microsoft, essa escolha dá uma noção mais realista do desempenho do modelo.

L1-R23. Julgue o item.
Para obter melhores resultados na transcrição automática do acervo de áudio das sessões, as documentações do Google Cloud Speech-to-Text e do Amazon Transcribe recomendam usar formato com perda, como o MP3, em vez de formatos sem perda, como o FLAC.

L1-R24. Julgue o item.
Em gravações de Plenário com muito ruído de fundo, a documentação do Google Cloud Speech-to-Text recomenda aplicar processamento de redução de ruído ao áudio antes de enviá-lo ao serviço, pois isso tende a elevar a acurácia do reconhecimento.

L1-R25. Julgue o item.
Segundo a documentação do Google Cloud Speech-to-Text, deve-se capturar o áudio com taxa de amostragem de 16.000 Hz ou superior, sempre que possível; no caso de gravações telefônicas, cuja taxa nativa costuma ser de 8.000 Hz, a orientação é enviar o áudio nessa taxa, sem reamostragem.

L1-R26. Julgue o item.
Para calcular o WER, é preciso alinhar a hipótese à transcrição de referência. Esse alinhamento, feito em ferramentas como o sclite, do NIST, consiste em uma programação dinâmica que minimiza globalmente uma distância de edição ponderada entre as sequências de palavras.

L1-R27. Julgue o item.
Na avaliação da transcrição automática de uma sessão, o erro em que o sistema deixa de reconhecer uma palavra efetivamente pronunciada é classificado como inserção, ao passo que o erro em que o sistema acrescenta ao texto uma palavra não pronunciada é classificado como supressão.

L1-R28. Julgue o item.
Ferramentas de pontuação como o sclite, do NIST, admitem transcrições alternativas de referência para trechos ambíguos da fala, o que permitiria, na avaliação de sessões da Câmara, que o sistema não fosse penalizado por emitir "para" ou "pra", desde que ambas as formas fossem previstas como corretas na referência.

L1-R29. Julgue o item.
Quando vários parlamentares falam ao mesmo tempo ou em volumes muito diferentes e o áudio é gravado em um único canal, a documentação do Google Cloud Speech-to-Text informa que o reconhecedor transcreve normalmente as vozes simultâneas, tratando-as como fala válida.

L1-R30. Julgue o item.
No cálculo-padrão do WER, os erros de palavra recebem pesos diferentes conforme a importância da palavra, de modo que um erro em número ou em nome próprio pesa mais que um erro em artigo; a ponderação uniforme é uma variação opcional prevista em ferramentas como o sclite.

L1-R31. Julgue o item.
Na taxa de erro de sentença, calculada em ferramentas de pontuação como o sclite, um par de referência e hipótese com um único erro de palavra é contado como incorreto, independentemente de quantas palavras do par estejam corretas; a taxa se obtém dividindo-se o número de pares incorretos pelo total de pares.

L1-R32. Julgue o item.
Um sistema de reconhecimento automático de fala pode gerar diferentes versões do mesmo trecho transcrito, associando a cada versão uma pontuação de confiança; em geral, o resultado entregue ao usuário é a versão de maior confiança.

L1-R33. Julgue o item.
No Whisper, a decodificação de cada janela de áudio é não autorregressiva: o modelo prevê todos os tokens da janela de uma só vez, sem que cada token dependa dos tokens previstos anteriormente.

L1-R34. Julgue o item.
Um acervo extenso de áudios de sessões sem transcrição pode ser aproveitado no pré-treinamento de modelos como o wav2vec 2.0, que aprende representações de fala a partir de dados não rotulados.

L1-R35. Julgue o item.
O cartão do modelo Whisper informa que o treinamento usou 680 mil horas de áudio e transcrições coletadas da internet, e que a maior parte desses dados, cerca de 65%, é de áudio em idiomas diferentes do inglês com transcrição no mesmo idioma.

L1-R36. Julgue o item.
Uma equipe pretende usar um modelo end-to-end multilíngue para transcrever um idioma que teve pouca representação nos dados de treino do modelo. Segundo o cartão do modelo Whisper, é esperada, em regra, acurácia menor nesse idioma, pois o desempenho em cada idioma se correlaciona diretamente com a quantidade de dados de treino nele.

L1-R37. Julgue o item.
Antes de adotar o Whisper para apoiar o registro das sessões da Câmara, é prudente avaliá-lo com gravações do Plenário e das comissões, pois o cartão do modelo recomenda avaliações robustas no contexto e no domínio de uso antes da implantação.

L1-R38. Julgue o item.
Um revisor encontrou, em transcrição produzida pelo Whisper, trechos em que a mesma frase se repetia. Esse comportamento, a que modelos sequência a sequência são propensos, pode ser eliminado por completo com o uso de busca em feixe (beam search) e de ajuste de temperatura na decodificação.

L1-R39. Julgue o item.
Em um modelo de reconhecimento de fala end-to-end já treinado, com decodificador CTC ou de transdutor, é possível incorporar na decodificação um modelo de linguagem treinado apenas com texto, como o das notas taquigráficas, o que pode aumentar a acurácia sem retreinar o modelo de fala.

L1-R40. Julgue o item.
O XLSR-53, variante multilíngue do wav2vec 2.0, foi pré-treinado com dados de 53 idiomas, entre os quais o inglês, mas não o português.

L1-R41. Julgue o item.
Em modelos end-to-end híbridos CTC/atenção, como os documentados no ESPnet, a decodificação conjunta com CTC é empregada para permitir que as palavras transcritas surjam em ordem diferente da dos trechos de fala correspondentes.

L1-R42. Julgue o item.
Combinar dados de fala de múltiplos domínios no pré-treinamento do wav2vec 2.0 é uma das estratégias documentadas para tratar a mudança de domínio entre os dados de treino e os de uso, como a diferença entre o material de treinamento e a fala das sessões da Câmara.

L1-R43. Julgue o item.
Ao planejar o uso do Whisper com oradores de todas as regiões do país, a equipe registrou que o cartão do modelo informa desempenho uniforme entre sotaques e dialetos de um mesmo idioma, ainda que varie entre idiomas.

L1-R44. Julgue o item.
Para transcrever ao vivo uma sessão do Plenário, a equipe concluiu que o Whisper, em sua forma original, já pode ser usado em tempo real, porque o cartão do modelo o apresenta como adequado a esse uso.

L1-R45. Julgue o item.
Na transcrição de uma sessão do Plenário com várias horas de duração, modelos end-to-end podem recorrer a estratégias documentadas em toolkits abertos, como a atenção local ou restrita no codificador e o processamento do áudio em blocos sequenciais.

L1-R46. Julgue o item.
Segundo a documentação do ESPnet, em vários benchmarks de reconhecimento de fala a abordagem end-to-end tem desempenho comparável ou superior ao de sistemas híbridos DNN/HMM, o que não implica superioridade em qualquer condição de uso.

FIM DA PARTE 2/3

=====================================================================
PARTE 3/3 — (d-G) GABARITO COMENTADO
=====================================================================
Legenda: [TS] = troca sutil de um único conceito. Em item C, [TS] indica "espelho": o item é verdadeiro, mas imita o padrão de uma troca (convenção admitida, O-6 da T-93). VOLÁTIL = gabarito depende de recomendação vigente em página de fornecedor. REVERIFICAR = reabrir a URL em 4–8/1/2027. CONFERÊNCIA DE BASE = item não VOLÁTIL cuja base entra na lista de conferência da reverificação de janeiro (D-T89-R1-ACEITE; T-11). Todas as páginas foram abertas e lidas em 18/10/2026.

## Folha P2-1.1

L1-R19. E [TS]. O denominador do WER é o número de palavras da transcrição de referência (50), e não o da hipótese (51); o WER correto é 6/50 = 12%.
Base: Microsoft, "Test accuracy of a custom speech model", seção "Evaluate word error rate (WER)" (WER = (I+D+S)/N, com N o número de palavras da transcrição rotulada por humanos), https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data; NIST, sclite (percentuais calculados sobre o número de palavras de referência), https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm. Verificado em 18/10/2026. Conta: 3 + 1 + 2 = 6 erros; hipótese = 50 − 1 + 2 = 51 palavras. CONFERÊNCIA DE BASE.

L1-R20. C. A documentação associa muitas supressões a sinal de áudio fraco e substituições a amostra insuficiente de termos do domínio, em transcrições rotuladas ou texto relacionado; o item reproduz essa associação.
Base: Microsoft, mesma página, seção "Resolve errors and improve WER" (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data), verificado em 18/10/2026. O item usa "costuma" porque a página usa "often" e "usually". CONFERÊNCIA DE BASE.

L1-R21. E. A falha da referência distorce o WER também quando o sistema acerta e a referência erra: o acerto vira erro contado. A precisão das estatísticas acompanha a acurácia do texto de referência, e não só os casos de erro coincidente.
Base: NIST, sclite, seção "Dynamic Programming string alignment" ("the precision of generated statistics is directly correlated to the reference text accuracy"), https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R22. C. Segundo a página, convém escolher, para o teste, um conjunto acústico diferente do usado com o modelo, o que dá uma noção mais realista do desempenho.
Base: Microsoft, "Test accuracy of a custom speech model", nota do passo de criação do teste ("select an acoustic dataset that's different from the one you used with your model"), https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data, verificado em 18/10/2026 (página com "Last updated" de 29/12/2025). CONFERÊNCIA DE BASE.

L1-R23. E [TS]. As duas documentações recomendam o oposto: usar codec sem perda (FLAC ou LINEAR16; no Amazon Transcribe, FLAC ou WAV com PCM de 16 bits) e evitar MP3 e outros codecs com perda, que podem reduzir a acurácia.
Base: Google Cloud, "Best practices" (https://cloud.google.com/speech-to-text/docs/best-practices; "Last updated 2026-10-13"); AWS, "Data input and output", seção "Media formats" (https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html), verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R24. E [TS]. A documentação diz que o reconhecedor foi projetado para áudio ruidoso e que aplicar redução de ruído antes do envio costuma reduzir, e não elevar, a acurácia; recomenda microfone próximo e desligar a redução de ruído.
Base: Google Cloud, "Best practices", seção "Audio preprocessing" (https://cloud.google.com/speech-to-text/docs/best-practices; "Last updated 2026-10-13"), verificado em 18/10/2026. VOLÁTIL (risco baixo): depende de recomendação vigente de um fornecedor. REVERIFICAR em 4–8/1/2027: reabrir a URL e conferir "applying noise-reduction signal processing to the audio before sending it to the service typically reduces recognition accuracy".

L1-R25. C [TS] (espelho). O item parece uma troca de taxas, mas reproduz a documentação: capturar a 16.000 Hz ou mais quando possível e, para telefonia (nativa comum de 8.000 Hz), enviar na taxa nativa, evitando reamostragem.
Base: Google Cloud, "Best practices", tabela de recomendações e seção "Sampling rate" (https://cloud.google.com/speech-to-text/docs/best-practices); AWS, "Data input and output", seção "Sample rates" (áudio de baixa fidelidade, como telefone, em geral a 8.000 Hz) (https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html), verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R26. C. A sclite alinha hipótese e referência por programação dinâmica, que faz uma minimização global de uma função de distância de Levenshtein com pesos (0, 3, 3 e 4 para acerto, inserção, supressão e substituição).
Base: NIST, sclite, seção "Step 2: Text Alignments" ("Dynamic Programming string alignment"), https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm, verificado em 18/10/2026. O item não cita os pesos. CONFERÊNCIA DE BASE.

L1-R27. E [TS]. Os papéis estão trocados: palavra pronunciada e não reconhecida é supressão, e palavra acrescentada que não foi dita é inserção.
Base: Microsoft, "Test accuracy of a custom speech model", seção "Evaluate word error rate (WER)" (Insertion: palavras incorretamente acrescentadas na hipótese; Deletion: palavras não detectadas na hipótese), https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R28. C [TS] (espelho). O item parece afrouxar a avaliação, mas a sclite prevê transcrições alternativas de referência: o sistema pode emitir qualquer uma delas e continuar correto. O exemplo "para"/"pra" é aplicação do item; a documentação traz o caso inglês "what are"/"what're".
Base: NIST, sclite, seção "Step 2: Text Alignments" (transcrições de referência alternativas para palavras ambíguas), https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R29. E [TS]. A documentação diz o contrário: vozes simultâneas ou em volumes diferentes podem ser interpretadas como ruído de fundo e ignoradas, e, se cada pessoa estiver em canal próprio, envia-se cada canal separadamente.
Base: Google Cloud, "Best practices", tabela de recomendações (https://cloud.google.com/speech-to-text/docs/best-practices; "Last updated 2026-10-13"), verificado em 18/10/2026. VOLÁTIL (risco baixo): recomendação vigente de um fornecedor. REVERIFICAR em 4–8/1/2027: reabrir a URL e conferir "Multiple people talking at the same time, or at different volumes may be interpreted as background noise and ignored".

L1-R30. E [TS]. O cálculo-padrão trata todos os erros de palavra com o mesmo peso; a ponderação por palavra é a variação (Weighted-Word Scoring). O item inverte padrão e variação.
Base: NIST, sclite, seções "Word Error Scoring" ("treating word errors with equal weight") e "Weighted-Word Scoring", https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R31. C. A taxa de erro de sentença divide os pares referência–hipótese incorretos pelo total de pares, de modo que um único erro de palavra torna o par incorreto, sejam quantas forem as palavras certas do par.
Base: NIST, sclite, seção "The scoring process" ("Percent of sentence errors = # incorrect ref and hyp pairs / # ref and hyp pairs"), https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm, verificado em 18/10/2026. A leitura "par incorreto = par com ao menos um erro de palavra" é a do cálculo; a página não a escreve literalmente. CONFERÊNCIA DE BASE.

L1-R32. C. O Amazon Transcribe cria versões diferentes do mesmo trecho com pontuação de confiança; em uma transcrição típica entrega apenas a de maior confiança, e as demais podem ser pedidas como alternativas.
Base: AWS, "Alternative transcriptions", https://docs.aws.amazon.com/transcribe/latest/dg/alternatives.html, verificado em 18/10/2026. O item não cita o limite de alternativas nem a restrição ao modo em lote. CONFERÊNCIA DE BASE.

## Folha P2-1.2

L1-R33. E [TS]. O Whisper faz previsões autorregressivas sequência a sequência em cada janela: cada token depende dos anteriores. O item troca "autorregressiva" por "não autorregressiva".
Base: repositório oficial openai/whisper, README, seção "Python usage" ("performing autoregressive sequence-to-sequence predictions on each window"), https://raw.githubusercontent.com/openai/whisper/main/README.md, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R34. C. O wav2vec 2.0 aprende representações de fala a partir de dados não rotulados, o que permite aproveitar áudio sem transcrição no pré-treinamento; o ajuste fino é feito depois, com áudio transcrito.
Base: repositório oficial facebookresearch/fairseq, README do wav2vec 2.0 ("learns speech representations on unlabeled data"; tabela com "No finetuning" e splits de ajuste), https://raw.githubusercontent.com/facebookresearch/fairseq/main/examples/wav2vec/README.md, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R35. E [TS]. Segundo o cartão do modelo, cerca de 65% dos dados são áudio em inglês com transcrição em inglês; áudio em outros idiomas com transcrição no mesmo idioma é cerca de 17%. O item troca o grupo majoritário.
Base: repositório oficial openai/whisper, model-card.md, seção "Training Data" (680.000 horas; 65% inglês; cerca de 18% áudio não inglês com transcrição em inglês; 17% áudio não inglês com transcrição correspondente), https://raw.githubusercontent.com/openai/whisper/main/model-card.md, verificado em 18/10/2026. Propriedade do artefato publicado (D-T89-R1-ACEITE, seção 1): não VOLÁTIL. CONFERÊNCIA DE BASE.

L1-R36. C. O cartão do modelo registra que o desempenho de transcrição em um idioma se correlaciona diretamente com a quantidade de dados de treino nesse idioma; por isso, idioma pouco representado tende a ter acurácia menor.
Base: repositório oficial openai/whisper, model-card.md, seção "Training Data" ("performance on transcription in a given language is directly correlated with the amount of training data we employ in that language"), https://raw.githubusercontent.com/openai/whisper/main/model-card.md, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R37. C. O cartão do modelo recomenda fortemente que os usuários façam avaliações robustas no contexto e no domínio de uso antes de implantar os modelos; avaliar com gravações do Plenário e das comissões aplica a recomendação.
Base: repositório oficial openai/whisper, model-card.md, seção "Evaluated Use" ("We strongly recommend that users perform robust evaluations of the models in a particular context and domain before deploying them"), https://raw.githubusercontent.com/openai/whisper/main/model-card.md, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R38. E. O cartão diz que a arquitetura sequência a sequência torna o modelo propenso a textos repetitivos, o que pode ser mitigado em certa medida por beam search e ajuste de temperatura, "mas não perfeitamente". O item afirma eliminação completa.
Base: repositório oficial openai/whisper, model-card.md, seção "Performance and Limitations", https://raw.githubusercontent.com/openai/whisper/main/model-card.md, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R39. C [TS] (espelho). O item parece contradizer a ideia de modelo único, mas as documentações do NeMo e do ESPnet descrevem a fusão de modelo de linguagem (treinado só com texto) em decodificadores CTC, de transdutor e outros, para elevar a acurácia sem retreinar o modelo de fala. "Notas taquigráficas" é aplicação do item.
Base: NVIDIA NeMo, docs/source/asr/intro.rst, item "Language Modeling" ("n-gram LM fusion ... for CTC, RNN-T, TDT, and AED models improves transcription accuracy without retraining"), https://raw.githubusercontent.com/NVIDIA/NeMo/main/docs/source/asr/intro.rst; ESPnet, README, seção "ASR" ("Incorporate RNNLM/LSTMLM/TransformerLM/N-gram trained only with text data"), https://raw.githubusercontent.com/espnet/espnet/master/README.md. Verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R40. E [TS]. O XLSR-53 foi pré-treinado com 53 idiomas, e o português consta dos conjuntos MLS e CommonVoice usados no pré-treinamento. O item troca "entre os quais o português" por "mas não o português".
Base: repositório oficial facebookresearch/fairseq, README do wav2vec 2.0, tabela do XLSR-53 (53 idiomas) e listas dos conjuntos MLS e CommonVoice (ambas trazem Portuguese), https://raw.githubusercontent.com/facebookresearch/fairseq/main/examples/wav2vec/README.md, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R41. E [TS]. Na documentação do ESPnet, a decodificação conjunta CTC/atenção serve para reforçar o alinhamento monotônico (as palavras seguem a ordem da fala). O item troca esse objetivo pela ordem diferente.
Base: ESPnet, README, seção "ASR", item "Hybrid CTC/attention based end-to-end ASR" ("CTC/attention joint decoding to boost monotonic alignment decoding"), https://raw.githubusercontent.com/espnet/espnet/master/README.md, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R42. C. O README do wav2vec 2.0 lista a combinação de dados de fala de múltiplos domínios em "Robust wav2vec 2.0: Analyzing Domain Shift in Self-Supervised Pre-Training"; tratar a mudança de domínio entre treino e uso é o ponto. O item não afirma ganho numérico.
Base: repositório oficial facebookresearch/fairseq, README do wav2vec 2.0, parágrafo inicial e linha da tabela "(LV-60 + CV + SWBD + FSH)", https://raw.githubusercontent.com/facebookresearch/fairseq/main/examples/wav2vec/README.md, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R43. E [TS]. O cartão do modelo informa desempenho desigual entre sotaques e dialetos de um mesmo idioma, inclusive taxa de erro de palavras mais alta para certos grupos de falantes. A concessiva final ("varie entre idiomas") é verdadeira; o erro é a uniformidade.
Base: repositório oficial openai/whisper, model-card.md, seção "Performance and Limitations" ("exhibit disparate performance on different accents and dialects"), https://raw.githubusercontent.com/openai/whisper/main/model-card.md, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R44. E [TS]. O cartão do modelo informa o contrário: em sua forma original, o Whisper não pode ser usado para transcrição em tempo real; terceiros podem construir aplicações de quase tempo real sobre ele.
Base: repositório oficial openai/whisper, model-card.md, seção "Broader Implications" ("cannot be used for real-time transcription out of the box"), https://raw.githubusercontent.com/openai/whisper/main/model-card.md, verificado em 18/10/2026. Propriedade do artefato publicado: não VOLÁTIL. CONFERÊNCIA DE BASE.

L1-R45. C. O NeMo documenta inferência em áudio com mais de uma hora por atenção local ou processamento em blocos (buffered chunked), e o ESPnet lista codificador de autoatenção restrita (Longformer) para sequências longas.
Base: NVIDIA NeMo, docs/source/asr/intro.rst, item "Long Audio", https://raw.githubusercontent.com/NVIDIA/NeMo/main/docs/source/asr/intro.rst; ESPnet, README, item "Restricted Self-Attention based on Longformer as an encoder for long sequences", https://raw.githubusercontent.com/espnet/espnet/master/README.md. Verificado em 18/10/2026. O item não cita limite de duração. CONFERÊNCIA DE BASE.

L1-R46. C [TS] (espelho). O item parece subestimar o end-to-end, mas reproduz a documentação ("comparable/superior to hybrid DNN/HMM and CTC" em vários benchmarks) e acrescenta, com razão, que isso não equivale a superioridade em qualquer condição.
Base: ESPnet, README, seção "ASR", item "State-of-the-art performance in several ASR benchmarks", https://raw.githubusercontent.com/espnet/espnet/master/README.md, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

## Contagens

| quesito | valor |
|---|---|
| total | 28 (14 em P2-1.1, 14 em P2-1.2) |
| C | 14 (R20, R22, R25, R26, R28, R31, R32, R34, R36, R37, R39, R42, R45, R46) = 50% |
| E | 14 (R19, R21, R23, R24, R27, R29, R30, R33, R35, R38, R40, R41, R43, R44) = 50% |
| C por folha | 1.1: 7 C / 7 E; 1.2: 7 C / 7 E |
| [TS] | 16 (R19, R23, R24, R25, R27, R28, R29, R30, R33, R35, R39, R40, R41, R43, R44, R46): 12 em E e 4 em C (R25, R28, R39, R46); E sem [TS]: R21 e R38 |
| VOLÁTIL | 2 novos (R24, R29; ambos de P2-1.1, risco baixo); risco alto: 0 |
| VOLÁTEIS por folha de 20 | P2-1.1: 2/20 (10%); P2-1.2: 0/20 |
| Formatos P2-1.1 (de 20) | D 3, PC 4, TS 2, NP 3, SH 3, AP 5 (maior: 25%) |
| Formatos P2-1.2 (de 20) | D 2, PC 4, TS 1, NP 3, SH 5, AP 5 (maior: 25%); definição nova: 0 |
| CONFERÊNCIA DE BASE (jan/2027) | R19 a R23, R25 a R28, R30 a R46 (todos os não VOLÁTEIS; ver lista) |
| REVERIFICAR (VOLÁTEIS) | R24, R29 |

Registros de estilo da T-93 (O-1 a O-8), conferidos na produção. O-1 (extensão): média de 43,3 palavras nos itens C (máximo 53) e de 41,2 nos itens E (máximo 64), isto é, diferença de 2 palavras, contra 9 palavras a mais nos C da onda 1; nenhum C acima de 65 palavras. Os E não ficaram mais longos que os C em média (limite registrado, sem pista de extensão relevante). O-2: R31 (C) usa "independentemente". O-3: "pode" também em E (R38, R44). O-4: sem remissão a norma. O-5: caudas falsas sem autodenúncia (R21, R38 revistos para não se entregarem). O-6: [TS] em quatro itens C (espelho), declarados. O-7: "apenas" em C (R39) e causais "porque" e "pois" em C (R22, R36, R37). O-8: concessiva em E (R43, "ainda que").

## Tabela de proveniência (todas as páginas abertas e lidas em 18/10/2026)
| fonte | URL oficial | data da página / verificação | usada em |
|---|---|---|---|
| Microsoft, Azure Speech, Test accuracy of a custom speech model | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | página com "Last updated on 2025-12-29"; verificado em 18/10/2026 | R19, R20, R22, R27 |
| NIST, SCTK, documento do sclite (repositório oficial usnistgov/SCTK) | https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm | "NIST SCLITE Scoring Package Version 1.5"; arquivo aberto e lido em 18/10/2026 (HTTP 200) | R19, R21, R26, R28, R30, R31 |
| Google Cloud, Speech-to-Text, Best practices | https://cloud.google.com/speech-to-text/docs/best-practices | "Last updated 2026-10-13"; verificado em 18/10/2026 | R23, R24, R25, R29 |
| AWS, Amazon Transcribe, Data input and output | https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html | verificado em 18/10/2026 | R23, R25 |
| AWS, Amazon Transcribe, Alternative transcriptions | https://docs.aws.amazon.com/transcribe/latest/dg/alternatives.html | verificado em 18/10/2026 | R32 |
| OpenAI, repositório oficial openai/whisper, README (ramo main) | https://raw.githubusercontent.com/openai/whisper/main/README.md | arquivo aberto e lido em 18/10/2026 (HTTP 200) | R33 |
| OpenAI, repositório oficial openai/whisper, model-card.md (ramo main) | https://raw.githubusercontent.com/openai/whisper/main/model-card.md | arquivo aberto e lido em 18/10/2026 (HTTP 200) | R35, R36, R37, R38, R43, R44 |
| Meta, repositório oficial facebookresearch/fairseq, README do wav2vec 2.0 | https://raw.githubusercontent.com/facebookresearch/fairseq/main/examples/wav2vec/README.md | arquivo aberto e lido em 18/10/2026 (HTTP 200) | R34, R40, R42 |
| NVIDIA, repositório oficial NVIDIA/NeMo, documentação de ASR (intro.rst) | https://raw.githubusercontent.com/NVIDIA/NeMo/main/docs/source/asr/intro.rst | arquivo aberto e lido em 18/10/2026 (HTTP 200) | R39, R45 |
| ESPnet, repositório oficial espnet/espnet, README (ramo master) | https://raw.githubusercontent.com/espnet/espnet/master/README.md | arquivo aberto e lido em 18/10/2026 (HTTP 200) | R39, R41, R45, R46 |

Fontes que tentei abrir e não abri (nenhum item depende delas): aws.amazon.com (FAQ do Amazon Transcribe: resposta vazia), docs.nvidia.com, kaldi-asr.org, espnet.github.io, pytorch.org e speechbrain.readthedocs.io (conexão recusada pelo proxy do ambiente), www.camara.leg.br (recusado). Não tentei os hosts sabidamente fechados: github.com (página), openai.com, arxiv.org, w3.org, huggingface.co. Nenhum item cita artigo do arXiv nem usa base de data anterior.

## Dúvidas à Gerência (D1 da gce-gerencia)
1. Natureza da base em R34, R39, R40, R41, R42, R45 e R46: os READMEs do fairseq, do NeMo e do ESPnet são documentação oficial dos projetos, mas esses toolkits não são as ferramentas nomeadas no edital (item 1.8). Se a Gerência exigir fornecedor do edital, esses sete itens precisam ser trocados; os demais não são afetados.
2. Reclassificação de VOLÁTIL: R23, R25 e R30 a R32 dependem de documentação de fornecedor e foram tratados como não VOLÁTEIS por serem propriedade de artefato ou prática coincidente de dois fornecedores (R23, R25) ou método de avaliação (NIST). Se R23 e R25 forem reclassificados, 1.1 vai a 4/20 (20%), ainda dentro do teto.
3. R43 (sotaques, folha 1.6) e R44 (tempo real, folha 1.7) julgam limitação do modelo end-to-end documentada no cartão do Whisper; se a Gerência preferir evitar a proximidade com as folhas 1.6 e 1.7 (produzidas em paralelo por outras produtoras), são os dois primeiros candidatos à troca.
4. R31: a leitura "par incorreto = par com ao menos um erro de palavra" não está escrita literalmente na página do NIST; se a QA exigir texto literal, o enunciado pode perder "um único erro" sem mudar o gabarito.

FIM DA PARTE 3/3
FIM DO LOTE
