# L1_reforco_onda2_A_v3.md — T-96 — 2026-10-18 — gerado por gce-cpp

Versão v3: transcrição da reconciliação saida/gce/T96_reconciliacao_2026-10-18.md, seção 5.1. L1-R43 foi retirado (reprovado na R2 da gce-cqfp; id não reutilizado) e não integra esta versão; a parte A tem 27 itens (P2-1.1: 14; P2-1.2: 13). R24 e R29 passam a não VOLÁTEIS (D1 da gce-gerencia, seção 2). A resposta ao parecer, a descrição de escopo e de QA PENDENTE (linhas 29–30), a verificação de não repetição, a linha de registros de estilo O-1 a O-8 e as dúvidas são histórico da v2.

=====================================================================
RESPOSTA AO PARECER (QA_T96A_R1_2026-10-18_gce-cqfp.md, rodada 1; v1 -> v2)
=====================================================================
Alterações da v2, e só elas: A-1 a A-4 aplicados com o texto exato do parecer; R40, R43 e R44 substituídos por 3 itens novos (mesmos ids, folha 1.2); mapa, contagens, proveniência e dúvidas atualizados em consequência. Os demais 21 itens não mudam (enunciado, gabarito, [TS], justificativa). Estrutura e blocos mantidos.

| ponto do parecer | resposta | o que mudou na v2 |
|---|---|---|
| A-1 (L1-R20, texto exato) | acatado | Parte 2: segunda oração passa a "...e atribui o excesso de supressões, em regra, ao sinal de áudio fraco." Parte 3 sem mudança, como o parecer manda. Mapa: ponto passa a "...e o excesso de supressões associa-se ao sinal fraco". |
| A-2 (L1-R31, texto exato) | acatado | Parte 2: enunciado inteiro substituído. Parte 3: "de modo que um único erro de palavra torna o par incorreto, sejam quantas forem as palavras certas do par" substituído por "e não o número de palavras erradas pelo total de palavras"; frase sobre a "leitura par incorreto" apagada. Gabarito C mantido. Dúvida 4 da v1 fica encerrada. |
| A-3 (L1-R45, texto exato) | acatado | Parte 2: enunciado inteiro substituído (sem "blocos sequenciais"). Parte 3: trecho do NeMo sem "processamento em blocos (buffered chunked)". Mapa: ponto passa a "Para áudio longo, modelos end-to-end recorrem a atenção local ou restrita no codificador". Gabarito C mantido. |
| A-4 (L1-R46, texto exato) | acatado | Parte 2: enunciado inteiro substituído (atribuído aos modelos do toolkit). Parte 3: "reproduz o que a documentação afirma sobre os modelos do toolkit". Gabarito C e [TS] espelho mantidos. |
| R40 reprovado (escopo: checkpoint específico, tema de 3.4) | acatado | Item substituído. Novo L1-R40: papel do Conformer nos modelos híbridos CTC/atenção do ESPnet (codificador, não decodificador). Gabarito E, [TS] (troca de papel), formato troca de sujeito, sem "definição". |
| R43 reprovado (ponto é o tema de 1.6, sotaques) | acatado | Item substituído. Novo L1-R43: menor conjunto de ajuste fino listado para os checkpoints do wav2vec 2.0 (10 minutos, não 10 horas). Gabarito E, [TS] (unidade), formato número ou prazo. A transferência do texto antigo a 1.6/1.7 é decisão da Gerência (D1), sem nova QA de texto; não fiz. Conferi que a parte C já tem o ponto de sotaques em L1-R98 e a parte D o de tempo real em L1-R106. |
| R44 reprovado (ponto é o tema de 1.7, tempo real) | acatado | Item substituído. Novo L1-R44: no ESPnet, a abordagem híbrida combina CTC e atenção no treinamento (multitarefa) e na decodificação, e não só na decodificação. Gabarito E, [TS], formato par confundível. |
| Recomendação de gabarito (voltar a 50% de C) | acatado | Os 3 novos são E; parte volta a 14 C / 14 E (50%); 1.2 com 7 C / 7 E. |
| Recomendação de [TS] (voltar a 16/28) | acatado | Os 3 novos levam [TS] com troca única; [TS] 16/28 (57%). |
| Recomendação de formato em 1.2 (sem "definição"; troca de sujeito de preferência; máximo 6) | acatado | Os 3 novos: TS, NP, PC; nenhuma definição nova. 1.2 fica D 2, PC 5, TS 2, NP 3, SH 4, AP 4; maior formato 25%. |
| Escopo de fairseq, NeMo e ESPnet (parecer: admissível; R34, R39, R41, R42, R45, R46 dentro de 1.2) | acatado | Mantidos. Os 3 novos citam README oficial de fairseq e ESPnet e tratam de conceito de modelo end-to-end (arquitetura de codificador e decodificador, treinamento multitarefa, ajuste fino após pré-treinamento). |
| VOLÁTIL (R24, R29 VOLÁTEIS; R23, R25 não) | acatado | Sem mudança. Os 3 novos são não VOLÁTEIS (propriedade de artefato publicado, critério T89 seção 1) e entram na CONFERÊNCIA DE BASE de janeiro. |
| Registro R34 x L1-Q04 | acatado | Mantida a menção ao ajuste fino com áudio transcrito na justificativa do R34. O novo R43 também fala de ajuste fino com áudio transcrito (tamanho do menor conjunto); julga ponto diferente de R34 (pré-treinamento sem rótulos) e de L1-Q04 (pares áudio-texto continuam necessários); sem contradição. |
| Registro R37 x L2-R04 (mesmo trecho-base, folhas distintas) | acatado | Registrado; sem mudança. Item de baixa dificuldade, mantido. |
| Registro R35/R36 x produção paralela de 1.8 | acatado | Conferido contra L1_reforco_onda2_D_v1.md: L1-R119 (1.8) julga os 65% de inglês do model card, mesma base de R35 (1.2); folhas diferentes, regra 1 da D-REFORCO-2 não violada. Conferência de duplicata na consolidação fica com a Gerência. R36 (correlação com dados de treino por idioma) não aparece em 1.8. |
| Registro: arXiv de R42 não aberto | acatado | Registrado; R42 só cita o texto do README. |
| Nenhuma base de data anterior; sem PENDENTE NORMATIVO | acatado | Mantido; as bases dos 3 novos foram reabertas hoje (18/10/2026). |


Tarefa T-96, onda 2 do reforço, parte A (ciclo s12c3), v2 após o parecer R1. Escopo: P2 folhas 1.1 e 1.2, 28 itens AUTORAL novos, ids L1-R19 a L1-R46 (L1-R19 a L1-R32 na folha 1.1; L1-R33 a L1-R46 na folha 1.2). Cada folha passa de 6 para 20 itens. As folhas 1.3 a 1.8 são das outras produtoras da onda 2 e não aparecem aqui.
Rótulo de todos os itens: AUTORAL (produtora gce-cpp, lote L1-R, onda 2 do reforço, D-REFORCO-2). QA PENDENTE: nenhum item deste arquivo passou por QA da rodada 2 (D-QA-PENDENTE); os 21 itens aprovados na R1 e os 4 ajustes aguardam a conferência da R2, e os 3 itens novos (R40, R43, R44) passam por QA pela primeira vez; não entra em simulado antes disso.
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
| L1-R20 | P2-1.1 | O padrão dos erros orienta a correção: substituições em termos do domínio associam-se a amostra insuficiente de termos do domínio, e o excesso de supressões associa-se ao sinal fraco | AP | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data (seção "Resolve errors and improve WER") | n |
| L1-R21 | P2-1.1 | Falhas da transcrição de referência distorcem o WER também quando o sistema acerta e a referência erra; a precisão da medida acompanha a precisão da referência | SH | https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm (seção "Dynamic Programming string alignment": precisão das estatísticas diretamente correlacionada à acurácia do texto de referência) | n |
| L1-R22 | P2-1.1 | Testar a acurácia com áudio diferente do usado no ajuste do modelo dá noção mais realista do desempenho | SH | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data (nota do passo de criação do teste) | n |
| L1-R23 | P2-1.1 | Recomendação coincidente de dois fornecedores: áudio em formato sem perda (FLAC; WAV PCM 16 bits); codecs com perda podem reduzir a acurácia | AP | https://cloud.google.com/speech-to-text/docs/best-practices (tabela de recomendações); https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html (seção "Media formats") | n |
| L1-R24 | P2-1.1 | Segundo a documentação do Google, o processamento de redução de ruído aplicado antes do envio tende a reduzir, e não a elevar, a acurácia | PC | https://cloud.google.com/speech-to-text/docs/best-practices (seção "Audio preprocessing") | n |
| L1-R25 | P2-1.1 | Não reamostrar: capturar a 16.000 Hz ou mais quando possível, e enviar áudio de telefonia (nativo comum de 8.000 Hz) na taxa nativa | NP | https://cloud.google.com/speech-to-text/docs/best-practices (tabela e seção "Sampling rate"); https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html (seção "Sample rates") | n |
| L1-R26 | P2-1.1 | O alinhamento entre hipótese e referência, prévio à contagem de erros, é feito por programação dinâmica que minimiza globalmente uma distância de edição ponderada | D | https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm (seção "Step 2: Text Alignments") | n |
| L1-R27 | P2-1.1 | Inserção é palavra acrescentada na hipótese; supressão é palavra pronunciada e não reconhecida (papéis trocados no item) | TS | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data (seção "Evaluate word error rate (WER)") | n |
| L1-R28 | P2-1.1 | Ferramentas de pontuação admitem transcrições alternativas de referência para trechos ambíguos, sem penalizar o sistema que emite qualquer delas | AP | https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm (seção "Step 2": transcrições de referência alternativas) | n |
| L1-R29 | P2-1.1 | Segundo a documentação do Google, vozes simultâneas ou em volumes diferentes, em canal único, podem ser interpretadas como ruído de fundo e ignoradas | AP | https://cloud.google.com/speech-to-text/docs/best-practices (tabela de recomendações) | n |
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
| L1-R40 | P2-1.2 | Nos modelos híbridos CTC/atenção do ESPnet, o Conformer é opção de codificador, e não de decodificador (decodificador: RNN, Transformer ou S4) | TS | https://raw.githubusercontent.com/espnet/espnet/master/README.md (seção "ASR: Automatic Speech Recognition", item "Hybrid CTC/attention based end-to-end ASR", linhas "Encoder" e "Decoder") | n |
| L1-R41 | P2-1.2 | Em modelos híbridos CTC/atenção, a decodificação conjunta com CTC serve para reforçar o alinhamento monotônico entre áudio e texto | PC | https://raw.githubusercontent.com/espnet/espnet/master/README.md (seção "ASR: Automatic Speech Recognition", item "Hybrid CTC/attention") | n |
| L1-R42 | P2-1.2 | Combinar dados de múltiplos domínios no pré-treinamento é estratégia documentada diante da mudança de domínio | AP | https://raw.githubusercontent.com/facebookresearch/fairseq/main/examples/wav2vec/README.md (parágrafo "Robust wav2vec 2.0") | n |
| L1-R44 | P2-1.2 | Na abordagem híbrida CTC/atenção do ESPnet, as duas se combinam no treinamento (multitarefa) e na decodificação (decodificação conjunta), e não só na decodificação | PC | https://raw.githubusercontent.com/espnet/espnet/master/README.md (seção "ASR: Automatic Speech Recognition", item "Hybrid CTC/attention based end-to-end ASR") | n |
| L1-R45 | P2-1.2 | Para áudio longo, modelos end-to-end recorrem a atenção local ou restrita no codificador | SH | https://raw.githubusercontent.com/NVIDIA/NeMo/main/docs/source/asr/intro.rst (item "Long Audio"); https://raw.githubusercontent.com/espnet/espnet/master/README.md (item "Restricted Self-Attention") | n |
| L1-R46 | P2-1.2 | Em vários benchmarks, o desempenho end-to-end é comparável ou superior ao dos sistemas híbridos DNN/HMM, o que não equivale a superioridade em qualquer condição | PC | https://raw.githubusercontent.com/espnet/espnet/master/README.md (item "State-of-the-art performance in several ASR benchmarks") | n |

VOLÁTIL novos: 0 (R24 e R29 reclassificados como não VOLÁTEIS: boa prática documentada, sem número, versão ou padrão de produto, com o mesmo rótulo dos gêmeos L1-R125 e L1-R91; D1 da gce-gerencia, reconciliação T-96, seção 2). Risco alto: 0.

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
| L1-R19 a R32 | ver tabela acima | NP, AP, SH, SH, AP, PC, NP, D, TS, AP, AP, PC, PC, D | n (14) |

Contagem de formatos na folha de 20: D 3 (Q01, R26, R32) = 15%; PC 4 (Q02, R24, R30, R31) = 20%; TS 2 (Q21, R27) = 10%; NP 3 (Q22, R19, R25) = 15%; SH 3 (R01, R21, R22) = 15%; AP 5 (R02, R20, R23, R28, R29) = 25%. Soma 20. Maior formato: AP com 25% (teto de 30% cumprido).
VOLÁTEIS na folha: 0/20; existentes: 0.

### P2-1.2 (6 existentes + 14 novos = 20)
| id | ponto | formato | VOL |
|---|---|---|---|
| L1-Q03 | End-to-end não é imune a alucinação | D | n |
| L1-Q04 | "Supervisão fraca" ainda usa pares áudio–texto | PC | n |
| L1C-Q23 | Sem dicionário de pronúncias; correção de nome próprio passa por adaptação ou mais dados | SH | n |
| L1C-Q24 | Em muitos sistemas há espectrograma antes da rede (não universal) | D | n |
| L1-R03 | Tarefa do Whisper definida por tokens especiais do decodificador | TS | n |
| L1-R04 | Whisper processa áudio longo em janelas sucessivas de 30 segundos | NP | n |
| L1-R33 a R46 (sem R43) | ver tabela acima | PC, AP, NP, SH, AP, AP, SH, TS, PC, AP, PC, SH, PC | n (13) |

Contagem de formatos na folha de 19 (L1-R43 retirado): D 2 (Q03, Q24) = 10,5%, sem item novo de definição (restrição da T-89, seção 3); PC 5 (Q04, R33, R41, R44, R46) = 26,3%; TS 2 (R03, R40) = 10,5%; NP 2 (R04, R35) = 10,5%; SH 4 (Q23, R36, R39, R45) = 21,1%; AP 4 (R34, R37, R38, R42) = 21,1%. Soma 19. Maior formato: PC com 26,3% (teto de 30% cumprido).
VOLÁTEIS na folha: 0/19.

### Verificação de não repetição
Em cada folha, o ponto de cada item novo foi comparado, um a um, com os pontos listados acima (existentes) e entre si; nenhum repete ponto. Proximidades que a Gerência pode querer ver:
- R19 × L1C-Q22 (1.1): ambos tocam o cálculo do WER; Q22 julga o limite superior (WER pode passar de 100%), R19 julga o denominador (referência, não hipótese).
- R32 × L1-R02 (1.1): ambos citam confiança; R02 julga a confiança e o tempo por palavra na saída e seus usos; R32 julga a existência de versões alternativas do trecho, com a de maior confiança entregue em regra.
- R27, R30, R31 × R19 (1.1): todos usam termos do cálculo de erro, mas cada um julga um ponto distinto (classificação inserção/supressão; peso uniforme × ponderado; taxa por sentença × por palavra).
- R39 × L1C-Q23 (1.2): ambos tratam de adaptação em modelo end-to-end; Q23 julga a ausência de dicionário de pronúncias separado, R39 julga a incorporação de modelo de linguagem externo na decodificação.
- R36 × L1-R11 (1.6, outra folha): R11 julga a variação entre idiomas e a não transferência do WER do inglês; R36 julga a correlação com a quantidade de dados de treino. Folhas diferentes, sem conflito de regra.
- R40 × R41 e R46 (1.2, mesma seção do README do ESPnet): R41 julga o propósito da decodificação conjunta com CTC; R46 julga o desempenho frente aos híbridos DNN/HMM; R40 julga a arquitetura (papel do Conformer como codificador). Pontos distintos.
- R44 × R41 (1.2): R41 julga para que serve a decodificação conjunta com CTC (alinhamento monotônico); R44 julga o momento da combinação CTC/atenção (treinamento multitarefa e decodificação). Pontos distintos.
- R43 × R34 e L1-Q04 (1.2): R34 julga o pré-treinamento sem rótulos; Q04 julga que pares áudio-texto continuam necessários; R43 julga o tamanho do menor conjunto de ajuste fino listado no README. Pontos distintos, sem contradição.
- R45 × L1-R04 (1.2): R04 julga a janela deslizante de 30 s do Whisper; R45 julga a atenção local ou restrita no codificador (sem a menção a blocos, após o ajuste A-3).
- R40, R43 e R44 × partes B, C e D da onda 2: conferidos contra os pontos de L1-R47 a R130; nenhum trata de Conformer, de tamanho de conjunto de ajuste fino ou de treinamento multitarefa CTC/atenção. Os pontos de sotaques (L1-R98, parte C) e de tempo real (L1-R106, parte D) já estão nas folhas 1.6 e 1.7 e saíram desta folha.

### Tetos (resumo da parte)
- Formato: maior formato por folha = 25% (AP em 1.1; PC em 1.2); teto de 30% cumprido; "definição" em 1.2: 0 novos.
- VOLÁTIL: 0 novos; 1.1 = 0/20; 1.2 = 0/19.
- Gabarito da parte: 14 C e 13 E (51,9% de C). Por folha: 1.1 com 7 C e 7 E; 1.2 com 7 C e 6 E.
- [TS]: 15/27 (55,6%); a meta de metade dos itens mais 2 é conferida na onda inteira (reconciliação T-96, seção 6). 11 em itens E e 4 em itens C (espelho); 2 itens E sem [TS] (R21, R38).

FIM DA PARTE 1/3

=====================================================================
PARTE 2/3 — (d) ITENS DO ESTUDANTE
=====================================================================

L1-R19. Julgue o item.
Na avaliação de um sistema de reconhecimento automático de fala, a transcrição de referência de um trecho de comissão tem 50 palavras. A hipótese gerada pelo sistema contém 3 substituições, 1 supressão e 2 inserções, de modo que tem 51 palavras. Nesse caso, o WER é de cerca de 11,8%, resultado da divisão do total de erros (6) pelo número de palavras da hipótese.

L1-R20. Julgue o item.
A equipe constatou que, na transcrição automática de sessões de comissão, predominavam substituições em nomes de proposições e de parlamentares. A documentação da Microsoft costuma associar esse padrão de erro à amostra insuficiente de termos do domínio, e atribui o excesso de supressões, em regra, ao sinal de áudio fraco.

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
Na taxa de erro de sentença, calculada em ferramentas de pontuação como o sclite, do NIST, divide-se o número de pares de referência e hipótese incorretos pelo total de pares, independentemente do número de palavras de cada par.

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
Ao escolher a arquitetura de um modelo end-to-end híbrido CTC/atenção, a equipe consultou a documentação do ESPnet, segundo a qual o Conformer é uma das opções de decodificador desses modelos, e não de codificador.

L1-R41. Julgue o item.
Em modelos end-to-end híbridos CTC/atenção, como os documentados no ESPnet, a decodificação conjunta com CTC é empregada para permitir que as palavras transcritas surjam em ordem diferente da dos trechos de fala correspondentes.

L1-R42. Julgue o item.
Combinar dados de fala de múltiplos domínios no pré-treinamento do wav2vec 2.0 é uma das estratégias documentadas para tratar a mudança de domínio entre os dados de treino e os de uso, como a diferença entre o material de treinamento e a fala das sessões da Câmara.

L1-R44. Julgue o item.
Segundo a documentação do ESPnet, nos modelos end-to-end híbridos CTC/atenção a combinação das duas abordagens ocorre apenas na decodificação, pois o treinamento é feito somente com o objetivo de atenção.

L1-R45. Julgue o item.
Na transcrição de uma sessão do Plenário com várias horas de duração, modelos end-to-end podem recorrer a mecanismos de atenção local ou restrita no codificador, documentados em toolkits abertos, para processar sequências longas de áudio.

L1-R46. Julgue o item.
Segundo a documentação do ESPnet, os modelos end-to-end desse toolkit alcançam, em vários benchmarks de reconhecimento de fala, desempenho comparável ou superior ao de sistemas híbridos DNN/HMM, o que não implica superioridade em qualquer condição de uso.

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
Base: Google Cloud, "Best practices", seção "Audio preprocessing" (https://cloud.google.com/speech-to-text/docs/best-practices; "Last updated 2026-10-13"), verificado em 18/10/2026. Não VOLÁTIL (boa prática documentada, sem número, versão ou padrão de produto; D1 da gce-gerencia, reconciliação T-96, seção 2). CONFERÊNCIA DE BASE em 4–8/1/2027: reabrir a URL e conferir "applying noise-reduction signal processing to the audio before sending it to the service typically reduces recognition accuracy".

L1-R25. C [TS] (espelho). O item parece uma troca de taxas, mas reproduz a documentação: capturar a 16.000 Hz ou mais quando possível e, para telefonia (nativa comum de 8.000 Hz), enviar na taxa nativa, evitando reamostragem.
Base: Google Cloud, "Best practices", tabela de recomendações e seção "Sampling rate" (https://cloud.google.com/speech-to-text/docs/best-practices); AWS, "Data input and output", seção "Sample rates" (áudio de baixa fidelidade, como telefone, em geral a 8.000 Hz) (https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html), verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R26. C. A sclite alinha hipótese e referência por programação dinâmica, que faz uma minimização global de uma função de distância de Levenshtein com pesos (0, 3, 3 e 4 para acerto, inserção, supressão e substituição).
Base: NIST, sclite, seção "Step 2: Text Alignments" ("Dynamic Programming string alignment"), https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm, verificado em 18/10/2026. O item não cita os pesos. CONFERÊNCIA DE BASE.

L1-R27. E [TS]. Os papéis estão trocados: palavra pronunciada e não reconhecida é supressão, e palavra acrescentada que não foi dita é inserção.
Base: Microsoft, "Test accuracy of a custom speech model", seção "Evaluate word error rate (WER)" (Insertion: palavras incorretamente acrescentadas na hipótese; Deletion: palavras não detectadas na hipótese), https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R28. C [TS] (espelho). O item parece afrouxar a avaliação, mas a sclite prevê transcrições alternativas de referência: o sistema pode emitir qualquer uma delas e continuar correto. O exemplo "para"/"pra" é aplicação do item; a documentação traz o caso inglês "what are"/"what're".
Base: NIST, sclite, seção "Step 2: Text Alignments" (transcrições de referência alternativas para palavras ambíguas), https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R29. E [TS]. A documentação diz o contrário: vozes simultâneas ou em volumes diferentes podem ser interpretadas como ruído de fundo e ignoradas, e, se cada pessoa estiver em canal próprio, envia-se cada canal separadamente.
Base: Google Cloud, "Best practices", tabela de recomendações (https://cloud.google.com/speech-to-text/docs/best-practices; "Last updated 2026-10-13"), verificado em 18/10/2026. Não VOLÁTIL (boa prática documentada, sem número, versão ou padrão de produto; D1 da gce-gerencia, reconciliação T-96, seção 2). CONFERÊNCIA DE BASE em 4–8/1/2027: reabrir a URL e conferir "Multiple people talking at the same time, or at different volumes may be interpreted as background noise and ignored".

L1-R30. E [TS]. O cálculo-padrão trata todos os erros de palavra com o mesmo peso; a ponderação por palavra é a variação (Weighted-Word Scoring). O item inverte padrão e variação.
Base: NIST, sclite, seções "Word Error Scoring" ("treating word errors with equal weight") e "Weighted-Word Scoring", https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R31. C. A taxa de erro de sentença divide os pares referência–hipótese incorretos pelo total de pares, e não o número de palavras erradas pelo total de palavras.
Base: NIST, sclite, seção "The scoring process" ("Percent of sentence errors = # incorrect ref and hyp pairs / # ref and hyp pairs"), https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

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

L1-R40. E [TS]. A documentação do ESPnet lista o Conformer entre as opções de codificador dos modelos híbridos CTC/atenção (com Transformer, Branchformer e E-Branchformer), e as opções de decodificador são RNN, Transformer ou S4. O item troca o papel do Conformer, de codificador para decodificador.
Base: ESPnet, README, seção "ASR: Automatic Speech Recognition", item "Hybrid CTC/attention based end-to-end ASR" ("Encoder: VGG-like CNN + BiRNN (LSTM/GRU), sub-sampling BiRNN (LSTM/GRU), Transformer, Conformer, Branchformer, or E-Branchformer"; "Decoder: RNN (LSTM/GRU), Transformer, or S4"), https://raw.githubusercontent.com/espnet/espnet/master/README.md, verificado em 18/10/2026. Propriedade do artefato publicado: não VOLÁTIL. CONFERÊNCIA DE BASE.

L1-R41. E [TS]. Na documentação do ESPnet, a decodificação conjunta CTC/atenção serve para reforçar o alinhamento monotônico (as palavras seguem a ordem da fala). O item troca esse objetivo pela ordem diferente.
Base: ESPnet, README, seção "ASR", item "Hybrid CTC/attention based end-to-end ASR" ("CTC/attention joint decoding to boost monotonic alignment decoding"), https://raw.githubusercontent.com/espnet/espnet/master/README.md, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R42. C. O README do wav2vec 2.0 lista a combinação de dados de fala de múltiplos domínios em "Robust wav2vec 2.0: Analyzing Domain Shift in Self-Supervised Pre-Training"; tratar a mudança de domínio entre treino e uso é o ponto. O item não afirma ganho numérico.
Base: repositório oficial facebookresearch/fairseq, README do wav2vec 2.0, parágrafo inicial e linha da tabela "(LV-60 + CV + SWBD + FSH)", https://raw.githubusercontent.com/facebookresearch/fairseq/main/examples/wav2vec/README.md, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L1-R44. E [TS]. A documentação do ESPnet registra a combinação nas duas etapas: treinamento multitarefa CTC/atenção e decodificação conjunta. O item restringe a combinação à decodificação e atribui o treinamento só à atenção.
Base: ESPnet, README, seção "ASR: Automatic Speech Recognition", item "Hybrid CTC/attention based end-to-end ASR" ("Fast/accurate training with CTC/attention multitask training"; "CTC/attention joint decoding to boost monotonic alignment decoding"), https://raw.githubusercontent.com/espnet/espnet/master/README.md, verificado em 18/10/2026. Propriedade do artefato publicado: não VOLÁTIL. CONFERÊNCIA DE BASE.

L1-R45. C. O NeMo documenta inferência em áudio com mais de uma hora por atenção local, e o ESPnet lista codificador de autoatenção restrita (Longformer) para sequências longas.
Base: NVIDIA NeMo, docs/source/asr/intro.rst, item "Long Audio", https://raw.githubusercontent.com/NVIDIA/NeMo/main/docs/source/asr/intro.rst; ESPnet, README, item "Restricted Self-Attention based on Longformer as an encoder for long sequences", https://raw.githubusercontent.com/espnet/espnet/master/README.md. Verificado em 18/10/2026. O item não cita limite de duração. CONFERÊNCIA DE BASE.

L1-R46. C [TS] (espelho). O item parece subestimar o end-to-end, mas reproduz o que a documentação afirma sobre os modelos do toolkit ("comparable/superior to hybrid DNN/HMM and CTC" em vários benchmarks) e acrescenta, com razão, que isso não equivale a superioridade em qualquer condição.
Base: ESPnet, README, seção "ASR", item "State-of-the-art performance in several ASR benchmarks", https://raw.githubusercontent.com/espnet/espnet/master/README.md, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

## Contagens

| quesito | valor |
|---|---|
| total | 27 (14 em P2-1.1, 13 em P2-1.2; L1-R43 retirado) |
| C | 14 (R20, R22, R25, R26, R28, R31, R32, R34, R36, R37, R39, R42, R45, R46) = 51,9% |
| E | 13 (R19, R21, R23, R24, R27, R29, R30, R33, R35, R38, R40, R41, R44) = 48,1% |
| C por folha | 1.1: 7 C / 7 E; 1.2: 7 C / 6 E |
| [TS] | 15 (R19, R23, R24, R25, R27, R28, R29, R30, R33, R35, R39, R40, R41, R44, R46): 11 em E e 4 em C (R25, R28, R39, R46); E sem [TS]: R21 e R38 |
| VOLÁTIL | 0 novos (R24 e R29 reclassificados; reconciliação T-96, seção 2); risco alto: 0 |
| VOLÁTEIS por folha | P2-1.1: 0/20; P2-1.2: 0/19 |
| Formatos P2-1.1 (de 20) | D 3, PC 4, TS 2, NP 3, SH 3, AP 5 (maior: 25%) |
| Formatos P2-1.2 (de 19) | D 2, PC 5, TS 2, NP 2, SH 4, AP 4 (maior: 26,3%); definição nova: 0 |
| CONFERÊNCIA DE BASE (jan/2027) | R19 a R42 e R44 a R46 (todos os 27; nenhum VOLÁTIL) |
| REVERIFICAR (VOLÁTEIS) | nenhum |

Registros de estilo da T-93 (O-1 a O-8), conferidos na produção. O-1 (extensão): média de 42,4 palavras nos itens C (máximo 53) e de 41,4 nos itens E (máximo 64), isto é, diferença de 1 palavra (recontada na v2 com os ajustes e os 3 itens novos), contra 9 palavras a mais nos C da onda 1; nenhum C acima de 65 palavras. Os E não ficaram mais longos que os C em média (limite registrado, sem pista de extensão relevante). O-2: R31 (C) usa "independentemente". O-3: "pode" também em E (R38). O-4: sem remissão a norma. O-5: caudas falsas sem autodenúncia (R21, R38 revistos para não se entregarem). O-6: [TS] em quatro itens C (espelho), declarados. O-7: "apenas" em C (R39) e também em E (R44); causais "porque" e "pois" em C (R22, R36, R37) e em E (R24, R44). O-8: concessiva em E: nenhum item na v2 (o "ainda que" do R43 saiu com a substituição).

## Tabela de proveniência (todas as páginas abertas e lidas em 18/10/2026)
| fonte | URL oficial | data da página / verificação | usada em |
|---|---|---|---|
| Microsoft, Azure Speech, Test accuracy of a custom speech model | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | página com "Last updated on 2025-12-29"; verificado em 18/10/2026 | R19, R20, R22, R27 |
| NIST, SCTK, documento do sclite (repositório oficial usnistgov/SCTK) | https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm | "NIST SCLITE Scoring Package Version 1.5"; arquivo aberto e lido em 18/10/2026 (HTTP 200) | R19, R21, R26, R28, R30, R31 |
| Google Cloud, Speech-to-Text, Best practices | https://cloud.google.com/speech-to-text/docs/best-practices | "Last updated 2026-10-13"; verificado em 18/10/2026 | R23, R24, R25, R29 |
| AWS, Amazon Transcribe, Data input and output | https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html | verificado em 18/10/2026 | R23, R25 |
| AWS, Amazon Transcribe, Alternative transcriptions | https://docs.aws.amazon.com/transcribe/latest/dg/alternatives.html | verificado em 18/10/2026 | R32 |
| OpenAI, repositório oficial openai/whisper, README (ramo main) | https://raw.githubusercontent.com/openai/whisper/main/README.md | arquivo aberto e lido em 18/10/2026 (HTTP 200) | R33 |
| OpenAI, repositório oficial openai/whisper, model-card.md (ramo main) | https://raw.githubusercontent.com/openai/whisper/main/model-card.md | arquivo aberto e lido em 18/10/2026 (HTTP 200) | R35, R36, R37, R38 |
| Meta, repositório oficial facebookresearch/fairseq, README do wav2vec 2.0 | https://raw.githubusercontent.com/facebookresearch/fairseq/main/examples/wav2vec/README.md | arquivo aberto e lido em 18/10/2026 (HTTP 200) | R34, R42 |
| NVIDIA, repositório oficial NVIDIA/NeMo, documentação de ASR (intro.rst) | https://raw.githubusercontent.com/NVIDIA/NeMo/main/docs/source/asr/intro.rst | arquivo aberto e lido em 18/10/2026 (HTTP 200) | R39, R45 |
| ESPnet, repositório oficial espnet/espnet, README (ramo master) | https://raw.githubusercontent.com/espnet/espnet/master/README.md | arquivo aberto e lido em 18/10/2026 (HTTP 200) | R39, R40, R41, R44, R45, R46 |

Fontes que tentei abrir e não abri (nenhum item depende delas): aws.amazon.com (FAQ do Amazon Transcribe: resposta vazia), docs.nvidia.com, kaldi-asr.org, espnet.github.io, pytorch.org e speechbrain.readthedocs.io (conexão recusada pelo proxy do ambiente), www.camara.leg.br (recusado). Não tentei os hosts sabidamente fechados: github.com (página), openai.com, arxiv.org, w3.org, huggingface.co. Nenhum item cita artigo do arXiv nem usa base de data anterior.

## Dúvidas à Gerência (D1 da gce-gerencia)
1. Natureza da base em R34, R39, R40, R41, R42, R43, R44, R45 e R46: os READMEs do fairseq, do NeMo e do ESPnet são documentação oficial dos projetos, mas esses toolkits não são as ferramentas nomeadas no edital (item 1.8). O parecer da QA é pela admissibilidade (o texto do edital em 1.2 é conceitual). Se a Gerência exigir fornecedor do edital, esses nove itens precisam ser trocados; os demais não são afetados.
2. Reclassificação de VOLÁTIL: R23, R25 e R30 a R32 dependem de documentação de fornecedor e foram tratados como não VOLÁTEIS por serem propriedade de artefato ou prática coincidente de dois fornecedores (R23, R25) ou método de avaliação (NIST). Se R23 e R25 forem reclassificados, 1.1 vai a 4/20 (20%), ainda dentro do teto.
3. Encerrada pelo parecer R1: R43 e R44 da v1 (sotaques e tempo real) foram reprovados por escopo e substituídos por itens de 1.2; a transferência do texto antigo a 1.6/1.7 é decisão da Gerência (D1), e esses pontos já constam de L1-R98 (1.6) e L1-R106 (1.7) nas partes C e D.
4. Encerrada pelo parecer R1: R31 reescrito pelo ajuste A-2, sem a leitura de "par incorreto" que a página do NIST não escreve literalmente.

FIM DA PARTE 3/3
FIM DO LOTE
