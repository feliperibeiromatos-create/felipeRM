# L1_reforco_onda2_D_v3.md — T-96 — 2026-10-18 — gerado por gce-cpp

Versão v3: transcrição da reconciliação saida/gce/T96_reconciliacao_2026-10-18.md, seção 5.2. Mudam só a regência da justificativa de L1-R129 (texto aceito pela gce-cqfp na R2, seção 3) e a localização dos trechos-base de L1-R126 e L1-R124 na seção "Evaluated Use" do model card. Enunciados, gabaritos, [TS] e VOLÁTEIS não mudam. A resposta ao parecer e os registros que vêm a seguir são histórico da v2.

## RESPOSTA AO PARECER QA_T96D_R1_2026-10-18_gce-cqfp (rodada 2, item a item)

Os 28 itens permanecem AUTORAL e QA PENDENTE. Só mudaram os itens abaixo; os demais 22 APROVADOS ficam byte a byte como na v1 (inclusive R105, R106 a R113, R115 a R118, R120 a R122, R125 a R128, R130).

| id | parecer | resposta | o que mudou |
|---|---|---|---|
| L1-R103 | AJUSTAR | acatado | Enunciado ancorado no Amazon Transcribe: "No Amazon Transcribe em streaming, que permite estabilizar os resultados parciais, o nível de estabilidade mais alto produz o texto mais preciso, enquanto o nível mais baixo entrega o texto com maior rapidez, ainda que com acurácia ligeiramente menor." Gabarito E, [TS] e ponto inalterados; mapa e justificativa ajustados. |
| L1-R104 | AJUSTAR (a) cauda, (b) fornecedor | acatado (a) e (b) | Cauda "como ocorre nos intervalos de uma sessão suspensa" retirada; fornecedor posto no enunciado; elemento parlamentar no sujeito: "Na transmissão de áudio PCM de uma reunião de comissão ao Amazon Transcribe em streaming, o cliente deve enviar a mesma quantidade de áudio, independentemente de haver fala, codificando o silêncio como bytes zero." Gabarito C; formato AP e "independentemente" em C (O-2) mantidos. |
| L1-R114 | AJUSTAR | acatado | Enunciado ancorado: "...fluxo de transcrição em streaming do Amazon Transcribe. Nesse caso, o procedimento correto é solicitar à AWS o aumento desse limite de duração, que pode ser ampliado sob pedido." Gabarito E; VOLÁTIL médio mantido (limite de serviço). Justificativa passa a dizer "No Amazon Transcribe". |
| L1-R119 | APROVADO (âncora indispensável) | acatado | Nenhuma mudança: "De acordo com o model card do Whisper" permanece no enunciado; REVERIFICAR mantido. |
| L1-R123 | AJUSTAR (só justificativa) | acatado | Retirada a frase sobre "fast transcription" e a menção ao contêiner de armazenamento (o parecer constatou que a página citada não traz "fast transcription"; a menção ao contêiner não consta do trecho literal conferido; só "retrieve transcription results asynchronously" é base). Enunciado e gabarito E inalterados. |
| L1-R124 | REPROVADO | acatado: item substituído (mesmo id, folha 1.8) | Novo ponto: advertência do model card do Whisper contra transcrever gravações de pessoas feitas sem consentimento. Enunciado: "Ao planejar a degravação de reuniões reservadas das comissões com o Whisper, a equipe deve levar em conta que o model card adverte contra o uso dos modelos para transcrever gravações de pessoas feitas sem o consentimento delas." Gabarito C; formato AP (o mesmo do item retirado); não [TS]; não VOLÁTIL (artefato publicado; nenhum fato mutável); sem restritivo e sem exemplo discutível. Base: model-card.md, seção "Evaluated Use", aberto e lido hoje (HTTP 200): "we caution against using Whisper models to transcribe recordings of individuals taken without their consent". Ponto distinto dos canônicos da 1.8 (Q18 a Q20, R16 a R18), dos demais 13 novos da folha e das partes A, B e C (conferido por busca; "sem consentimento" só aparece, no acervo, em itens de LGPD). Proximidades com R126, R122 e R106 registradas na seção 1.3. A linha da fonte AWS "Custom language models" saiu da tabela de proveniência (nenhum item a usa mais). |
| L1-R129 | AJUSTAR | acatado | Predicado avaliativo explícito: "Uma equipe estimou o tempo de degravação do acervo com as velocidades relativas da tabela do Whisper, medidas com fala em inglês em GPU A100, e agiu corretamente ao ressalvar que a velocidade real pode variar muito com o idioma e o hardware." Gabarito C. Formato passa a SH: a 1.8 fica com SH 6/20 = 30% (no teto) e AP 3/20; tabela de formatos atualizada. |

Registros para a Gerência, sem alterar nada (competência D1/D2 da gce-gerencia, D-T89-R1-ACEITE): (1) R120 (phrase list) e R128 (custom speech e WER) seguem marcados não VOLÁTEIS, como na v1. A letra da D-T89-R1-ACEITE inclui "existência de recurso", e o parecer (seção 4) assinala que o C de ambos pressupõe que o recurso nomeado exista. Se a Gerência os enquadrar como VOLÁTEIS, a 1.8 vai a 4/20 = 20% (Q18, Q19, R120, R128), no teto da regra 4, mas com 2 VOLÁTEIS novos, contra a restrição da T89_reconciliacao, seção 3; sem esse enquadramento, nada muda. Pedido: registro expresso de que funcionamento documentado de recurso central, sem número, versão, preço ou disponibilidade, é não VOLÁTIL (fica com REVERIFICAR). (2) A substituição do R124 eliminou o terceiro caso (custom language model do Amazon Transcribe) da mesma questão. (3) Contagem: parte D mantém 14 C / 14 E, [TS] 17/28, VOLÁTEIS novos 2 (R110, R114; ambos na 1.7). Por folha, a 1.7 tem 6 C / 8 E e a 1.8 tem 8 C / 6 E (R124 continua C); o equilíbrio 7/7 por folha não é alcançável sem inverter o gabarito de um item aprovado, o que não foi feito (mantido o 14/14 da parte).

Onda 2 do reforço, parte D (ciclo 2026-10-18 s12c3). Escopo: P2-1.7 (+14, ids L1-R103 a L1-R116) e P2-1.8 (+14, ids L1-R117 a L1-R130). Cada folha passa de 6 para 20. Total: 28 itens.
Rótulo de todos os itens: AUTORAL (produtor gce-cpp, lote L1-R, onda 2 do reforço, D-REFORCO-2). QA PENDENTE: nenhum item deste arquivo entra em simulado antes da QA e da reconciliação (D-QA-PENDENTE). Nenhum item existente foi alterado.
Convenção: "verificado em 18/10/2026" = página aberta e lida nesta data (curl, HTTP 200; trechos conferidos no texto extraído). Nenhuma base de data anterior foi usada (D-FONTE-DATA-ANTERIOR não se aplica). Nenhum item cita número de versão, preço ou limite numérico de produto; os dois itens que dependem de comportamento ou limite documentado de serviço estão marcados VOLÁTIL.
Critérios aplicados: D-REFORCO-1/2 (um ponto de julgamento por item, único na folha, inclusive frente aos canônicos); D1 da T-89 (VOLÁTIL = fato mutável; nome de produto com propriedade fixa ou divisão estrutural não é VOLÁTIL); restrições da reconciliação T-89 (na 1.8, nenhum VOLÁTIL novo; [TS] em ao menos metade dos itens mais 2); registros O-1 a O-8 da T-93 (extensão, "independentemente" em C, "pode" em E, restritivo em C, concessiva em E, remissão sem vínculo extra, sem cauda que denuncia).

=====================================================================
PARTE 1/3 — MAPA
=====================================================================

## 1.1 P2-1.7 Transcrição em tempo real — itens novos (um ponto de julgamento por item)

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL |
|---|---|---|---|---|---|
| L1-R103 | P2-1.7 | No Amazon Transcribe em streaming, na estabilização de resultados parciais, o nível de estabilidade mais alto reduz a latência com acurácia ligeiramente menor; o nível mais baixo dá a maior acurácia (e não o inverso) | par confundível | https://docs.aws.amazon.com/transcribe/latest/dg/streaming-partial-results.html | n |
| L1-R104 | P2-1.7 | No Amazon Transcribe em streaming, sem fala, o cliente continua enviando a mesma quantidade de áudio, com o silêncio codificado (bytes zero no PCM), em vez de interromper o envio; elemento parlamentar no sujeito (reunião de comissão) | aplicação parlamentar | https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html (boas práticas) | n |
| L1-R105 | P2-1.7 | 16.000 Hz é a taxa indicada para áudio de transcrição em streaming (compromisso entre qualidade e volume enviado pela rede), embora microfones de alta qualidade gravem a 44.100 ou 48.000 Hz | número ou prazo | https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html (boas práticas) | n |
| L1-R106 | P2-1.7 | Os modelos Whisper publicados, tal como distribuídos, não realizam transcrição em tempo real; isso exige aplicação construída sobre eles | situação hipotética | https://raw.githubusercontent.com/openai/whisper/main/model-card.md (seção "Broader Implications") | n (propriedade do artefato publicado) |
| L1-R107 | P2-1.7 | No Google Speech-to-Text, o reconhecimento síncrono responde só após processar todo o áudio; é o streaming que entrega resultados intermediários durante a captação | troca de sujeito | https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-requests | n (divisão estrutural de operações) |
| L1-R108 | P2-1.7 | No reconhecimento contínuo do Speech SDK (Azure), Recognizing traz os resultados intermediários e Recognized traz os finais | troca de sujeito | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech | n (semântica de evento do SDK publicado) |
| L1-R109 | P2-1.7 | Enunciado único termina por silêncio ao final ou por limite de áudio processado; no reconhecimento contínuo, a aplicação decide quando parar | definição | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech | n (estrutural; sem número) |
| L1-R110 | P2-1.7 | A API REST para áudio curto do Azure Speech devolve apenas o resultado final, sem parciais; texto parcial ao vivo exige o Speech SDK | aplicação parlamentar | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-speech-to-text-short | S (limitação documentada de serviço; risco médio) |
| L1-R111 | P2-1.7 | Na segmentação só por silêncio, o orador que fala longamente sem pausas gera bloco longo sem quebras (subsegmentação), e não texto fragmentado | par confundível | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech (seção "Semantic segmentation") | n (conceito de segmentação) |
| L1-R112 | P2-1.7 | Streaming descreve a entrega do áudio em blocos sequenciais e pode ser aplicado também a mídia previamente gravada, não só a transmissão ao vivo | definição | https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html | n |
| L1-R113 | P2-1.7 | Cota de fluxos concorrentes excedida: repetir com espera exponencial (backoff) e, persistindo, solicitar aumento da cota | situação hipotética | https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html (seção LimitExceededException) | n (procedimento, sem número) |
| L1-R114 | P2-1.7 | No Amazon Transcribe, a duração máxima de um fluxo de streaming é limite fixo que não se amplia por pedido; é preciso iniciar nova sessão | situação hipotética | https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html (seção LimitExceededException) | S (limite de serviço; risco médio) |
| L1-R115 | P2-1.7 | A diarização em tempo real do Azure Speech rotula os falantes com identificador genérico atribuído durante o reconhecimento, e não pelo nome do orador | definição | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-stt-diarization | n (propriedade do resultado) |
| L1-R116 | P2-1.7 | Para streaming no Amazon Transcribe, a documentação recomenda os SDKs, e não conexões HTTP/2 ou WebSocket montadas diretamente | aplicação parlamentar | https://docs.aws.amazon.com/transcribe/latest/dg/streaming-setting-up.html | n (recomendação documentada, sem versão) |

## 1.2 P2-1.8 Ferramentas e APIs — itens novos (um ponto de julgamento por item; nenhum VOLÁTIL novo)

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL |
|---|---|---|---|---|---|
| L1-R117 | P2-1.8 | Os modelos Whisper com sufixo .en são as versões somente em inglês; para o português serve um modelo multilíngue | situação hipotética | https://raw.githubusercontent.com/openai/whisper/main/README.md (seção "Available models and languages") | n (artefato publicado) |
| L1-R118 | P2-1.8 | Boas práticas do Google: gravar e transmitir em codec sem perdas (FLAC, LINEAR16); codecs com perdas, como MP3, podem reduzir a acurácia | par confundível | https://docs.cloud.google.com/speech-to-text/docs/best-practices | n (boa prática; sem versão ou número) |
| L1-R119 | P2-1.8 | No model card do Whisper, a maior parte das 680 mil horas de treinamento é fala em inglês com transcrição em inglês (65%), e não fala não inglesa no próprio idioma | número ou prazo | https://raw.githubusercontent.com/openai/whisper/main/model-card.md (seção "Training Data") | n (artefato publicado) |
| L1-R120 | P2-1.8 | A lista de frases (phrase list) do Azure Speech é informada em tempo de execução e favorece nomes e siglas sem treinar modelo | definição | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/improve-accuracy-phrase-list | n (conceito de funcionamento; sem limite nem versão) |
| L1-R121 | P2-1.8 | Áudio gravado em taxa nativa menor (8.000 Hz) não deve ser reamostrado para 16.000 Hz; envia-se na taxa original | situação hipotética | https://docs.cloud.google.com/speech-to-text/docs/best-practices (seção "Sampling rate") | n (boa prática) |
| L1-R122 | P2-1.8 | Treinamento fracamente supervisionado com dados ruidosos faz o Whisper poder gerar texto não falado no áudio (alucinação) | aplicação parlamentar | https://raw.githubusercontent.com/openai/whisper/main/model-card.md (seção "Performance and Limitations") | n (artefato publicado) |
| L1-R123 | P2-1.8 | A transcrição em lote do Azure Speech devolve o resultado de forma assíncrona (consulta posterior), e não síncrona na própria chamada | troca de sujeito | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription | n (divisão estrutural de operações) |
| L1-R124 | P2-1.8 | O model card do Whisper adverte contra o uso dos modelos para transcrever gravações de pessoas feitas sem o seu consentimento (ponto novo, substitui o da v1) | aplicação parlamentar | https://raw.githubusercontent.com/openai/whisper/main/model-card.md (seção "Evaluated Use") | n (artefato publicado; nenhum fato mutável) |
| L1-R125 | P2-1.8 | Pré-processar com redução de ruído e controle automático de ganho tende a reduzir a acurácia; essas funções devem ser desativadas | situação hipotética | https://docs.cloud.google.com/speech-to-text/docs/best-practices (seção "Audio preprocessing") | n (boa prática) |
| L1-R126 | P2-1.8 | Segundo o model card, a diarização não foi avaliada de forma robusta no Whisper (pode surgir, sobretudo com ajuste fino) | definição | https://raw.githubusercontent.com/openai/whisper/main/model-card.md (seção "Evaluated Use") | n (artefato publicado) |
| L1-R127 | P2-1.8 | No Amazon Transcribe, o vocabulário personalizado melhora o reconhecimento de termos; o filtro de vocabulário mascara, remove ou marca palavras na saída (papéis trocados no enunciado) | par confundível | https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html ; https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html | n (conceito de funcionamento) |
| L1-R128 | P2-1.8 | Para saber se o modelo base do Azure Speech basta, compara-se sua transcrição com a humana por WER; WER alto recomenda treinar modelo personalizado | situação hipotética | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-speech-overview (seção "Choose your model") | n (método documentado) |
| L1-R129 | P2-1.8 | As razões de velocidade relativa da tabela do Whisper foram medidas com fala em inglês em GPU A100 e podem variar significativamente com idioma, fala e hardware; julga-se a conduta de ressalvar | situação hipotética | https://raw.githubusercontent.com/openai/whisper/main/README.md (seção "Available models and languages") | n (artefato publicado) |
| L1-R130 | P2-1.8 | No Google Speech-to-Text, indicar o modelo de reconhecimento conforme o tipo ou a fonte do áudio tende a melhorar os resultados | definição | https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-requests (seção "Model selection") | n (sem citar nome de modelo) |

## 1.3 Verificação de não repetição, formatos e VOLÁTEIS por folha de 20

Pontos já usados (conferidos item a item contra pacote.json v1.9, GCE_Lote1_v2_CPP, GCE_Lote1C_v2_CPP, GCE_Lote1_consolidacao_GCE e L1_reforco_onda1_v2).
- P2-1.7 existentes: Q15 (parciais revisáveis; final após fim do enunciado), Q16 (OpenAI stream=true em arquivo × Realtime), Q17 (sensibilidade de endpointing: latência × fragmentação), R13 (tamanho dos blocos influencia a latência), R14 (100 ms de PCM 16 bits mono a 16 kHz = 3.200 bytes), R15 (streaming mais rápido sem garantia de acurácia ≥ lote). Nenhum dos 14 novos repete esses pontos.
- P2-1.8 existentes: Q18 (Whisper aberto, MIT, e API com modelos mais recentes), Q19 (Azure AI Speech admite contêineres on-premises), Q20 (custódia do áudio: local × nuvem), R16 (tradução do Whisper para inglês, turbo excluído), R17 (lote × streaming do Amazon Transcribe: papéis), R18 (tamanhos tiny e large em parâmetros). Nenhum dos 14 novos repete esses pontos.
- Entre os 14 novos de cada folha, os pontos são todos distintos (comparação feita aos pares).
- Proximidades que a Gerência pode querer ver (nenhuma é duplicata; todas por ponto próprio):
  - R105 × R14 (1.7): mesma página da AWS, mas R14 calcula bytes de bloco; R105 julga a taxa de amostragem indicada.
  - R111 × Q17 (1.7): ambos tocam segmentação, mas Q17 julga a sensibilidade do endpointing (pausas curtas fragmentam); R111 julga o efeito da segmentação só por silêncio sobre fala longa sem pausas.
  - R103 × R15 (1.7): ambos tratam de latência × acurácia; R15 compara streaming × lote; R103 compara níveis de estabilidade dentro do streaming.
  - R129 × R18 (1.8): mesma tabela do README do Whisper, colunas distintas (velocidade relativa × parâmetros).
  - R129 × R11 (1.6) e R119 × R11 (1.6): folhas diferentes; R11 julga o WER em inglês não se transferir ao pt-BR; R129 julga a medição de velocidade; R119 julga a composição dos dados de treino.
  - R121 × R105 (folhas 1.8 × 1.7): ambos tocam taxa de amostragem; pontos distintos (não reamostrar × 16 kHz indicado).
  - R124 × R126 (1.8) e R124 × R122 (1.8): mesmo model card; R126 julga a diarização não avaliada de forma robusta (seção "Evaluated Use", segundo parágrafo), R122 julga a alucinação (seção "Performance and Limitations"); R124 julga a advertência sobre gravações feitas sem consentimento (seção "Evaluated Use", terceiro parágrafo). R124 × R106 (1.7): R106 julga a ausência de tempo real fora da caixa; ponto distinto. Nenhuma das partes A, B e C usa o ponto.
  - R123 × R17 (1.8): R17 julga os papéis de lote e streaming no Amazon Transcribe; R123 julga o caráter assíncrono do lote no Azure Speech.
  - R112 × R17 (1.7 × 1.8): R112 julga que o streaming vale também para mídia gravada; R17 julga os papéis (arquivo previamente enviado × blocos).

Formatos da folha P2-1.7 (20 itens = 6 existentes + 14 novos; teto de 30% = 6 por formato):
| formato | existentes | novos | total | % |
|---|---|---|---|---|
| definição (D) | Q15 | R109, R112, R115 | 4 | 20% |
| troca de sujeito (TSj) | R13 | R107, R108 | 3 | 15% |
| situação hipotética (SH) | Q17 | R106, R113, R114 | 4 | 20% |
| número ou prazo (NP) | R14 | R105 | 2 | 10% |
| par confundível (PC) | Q16 | R103, R111 | 3 | 15% |
| aplicação parlamentar (AP) | R15 | R104, R110, R116 | 4 | 20% |
| soma | 6 | 14 | 20 | 100% |
Maior formato: 20% (teto de 30% cumprido). VOLÁTIL da folha: Q16 (existente, risco alto), R110 e R114 (novos, risco médio) = 3/20 = 15% (teto de 20% cumprido).

Formatos da folha P2-1.8 (20 itens = 6 existentes + 14 novos):
| formato | existentes | novos | total | % |
|---|---|---|---|---|
| definição (D) | Q19 | R120, R126, R130 | 4 | 20% |
| troca de sujeito (TSj) | R17 | R123 | 2 | 10% |
| situação hipotética (SH) | R16 | R117, R121, R125, R128, R129 | 6 | 30% |
| número ou prazo (NP) | R18 | R119 | 2 | 10% |
| par confundível (PC) | Q18 | R118, R127 | 3 | 15% |
| aplicação parlamentar (AP) | Q20 | R122, R124 | 3 | 15% |
| soma | 6 | 14 | 20 | 100% |
Maior formato: SH com 30% (R129 passa a SH; teto de 30% cumprido, sem folga). VOLÁTIL da folha: Q18 e Q19 (existentes) = 2/20 = 10% (teto de 20% cumprido; legado diluído de 33,3% para 10%); novos 0 (restrição da T-89, seção 3, cumprida).

Tetos da parte D: VOLÁTEIS novos 2 (R110, R114), ambos de risco médio; risco alto novo 0 (máximo de 1 cumprido). Nenhum item usa número de versão, preço ou nome de modelo da API de um fornecedor.

FIM DA PARTE 1/3

=====================================================================
PARTE 2/3 — (d) ITENS DO ESTUDANTE
=====================================================================

L1-R103. Julgue o item.
No Amazon Transcribe em streaming, que permite estabilizar os resultados parciais, o nível de estabilidade mais alto produz o texto mais preciso, enquanto o nível mais baixo entrega o texto com maior rapidez, ainda que com acurácia ligeiramente menor.

L1-R104. Julgue o item.
Na transmissão de áudio PCM de uma reunião de comissão ao Amazon Transcribe em streaming, o cliente deve enviar a mesma quantidade de áudio, independentemente de haver fala, codificando o silêncio como bytes zero.

L1-R105. Julgue o item.
A taxa de amostragem de 16.000 Hz é indicada para a transcrição em streaming por equilibrar qualidade e volume de dados na rede, embora microfones de alta qualidade gravem a 44.100 ou 48.000 Hz.

L1-R106. Julgue o item.
Uma equipe da Câmara pretende legendar sessões ao vivo com os modelos Whisper publicados pela OpenAI e supõe que eles, tal como distribuídos, já realizam transcrição em tempo real, de modo que pode dispensar qualquer aplicação construída sobre os modelos para esse fim.

L1-R107. Julgue o item.
No Google Cloud Speech-to-Text, o reconhecimento síncrono devolve resultados intermediários enquanto o áudio ainda está sendo captado, ao passo que o reconhecimento em streaming, próprio para áudio ao vivo, só responde depois de processado todo o áudio enviado.

L1-R108. Julgue o item.
No reconhecimento contínuo do Speech SDK, do Azure Speech, o evento Recognizing traz os resultados finais, que indicam uma tentativa de reconhecimento bem-sucedida, enquanto o evento Recognized traz os resultados intermediários.

L1-R109. Julgue o item.
No Speech SDK, o reconhecimento de enunciado único termina por silêncio ao final da fala ou por limite de áudio processado, enquanto no reconhecimento contínuo a aplicação decide quando parar.

L1-R110. Julgue o item.
Para exibir ao público, durante a sessão, o texto parcial da fala de cada orador, a Câmara pode usar a API REST para áudio curto do Azure Speech, que devolve resultados parciais à medida que o áudio é enviado, e não apenas o resultado final de cada trecho.

L1-R111. Julgue o item.
Quando a segmentação do reconhecimento em tempo real se baseia apenas no silêncio, um orador que fala por longo tempo sem pausas tende a ter a sua fala fragmentada em trechos muito curtos.

L1-R112. Julgue o item.
Na transcrição em streaming, o áudio chega ao serviço em uma sequência de blocos, de modo que o recurso pode ser aplicado também a mídia previamente gravada, e não apenas a transmissões ao vivo.

L1-R113. Julgue o item.
Se a transcrição simultânea de várias comissões exceder a cota de fluxos concorrentes, é adequado repetir a tentativa com espera exponencialmente crescente e, se o limite for atingido de forma recorrente, pedir aumento da cota.

L1-R114. Julgue o item.
Uma sessão plenária longa ultrapassou a duração máxima permitida para um único fluxo de transcrição em streaming do Amazon Transcribe. Nesse caso, o procedimento correto é solicitar à AWS o aumento desse limite de duração, que pode ser ampliado sob pedido.

L1-R115. Julgue o item.
No Azure Speech, a diarização em tempo real devolve, para cada trecho transcrito, o nome do orador, o que dispensa a equipe da Casa de associar, depois, o falante identificado ao parlamentar correspondente.

L1-R116. Julgue o item.
Na integração do sistema de transcrição das comissões ao Amazon Transcribe em streaming, a documentação recomenda fortemente usar os SDKs da AWS, e não montar diretamente conexões HTTP/2 ou WebSocket, por serem o método mais simples e confiável.

L1-R117. Julgue o item.
Ao planejar a degravação automática das sessões do Plenário em português, a equipe da Câmara pode usar o modelo medium.en do Whisper, pois os modelos com sufixo .en são as versões multilíngues de cada tamanho.

L1-R118. Julgue o item.
Segundo as boas práticas do Google Cloud Speech-to-Text, é preferível gravar e transmitir o áudio em codec sem perdas, como FLAC ou LINEAR16, pois codecs com perdas, como o MP3, podem reduzir a acurácia do reconhecimento.

L1-R119. Julgue o item.
De acordo com o model card do Whisper, a maior parte das 680 mil horas de áudio coletadas na internet para o treinamento corresponde a fala não inglesa com transcrição no próprio idioma.

L1-R120. Julgue o item.
No Azure Speech, a lista de frases (phrase list) é informada em tempo de execução, pouco antes do reconhecimento, e favorece o reconhecimento de nomes e siglas sem exigir o treinamento de um modelo personalizado.

L1-R121. Julgue o item.
Uma gravação antiga de audiência pública foi captada com taxa de amostragem de 8.000 Hz. Segundo as boas práticas do Google Cloud Speech-to-Text, para melhorar a acurácia a equipe deve reamostrar o áudio para 16.000 Hz antes de enviá-lo ao serviço.

L1-R122. Julgue o item.
Como o Whisper foi treinado de forma fracamente supervisionada com dados ruidosos em larga escala, a saída pode conter trechos não falados no áudio, o que reforça a necessidade de revisão humana da degravação.

L1-R123. Julgue o item.
Na transcrição em lote (batch) do Azure Speech, a aplicação envia o áudio e recebe o resultado de forma síncrona, na própria chamada, sem necessidade de consultar o andamento da tarefa nem de recuperar o resultado depois.

L1-R124. Julgue o item.
Ao planejar a degravação de reuniões reservadas das comissões com o Whisper, a equipe deve levar em conta que o model card adverte contra o uso dos modelos para transcrever gravações de pessoas feitas sem o consentimento delas.

L1-R125. Julgue o item.
Antes de enviar ao Google Cloud Speech-to-Text a gravação de uma comissão feita em sala ruidosa, a equipe deve aplicar redução de ruído e controle automático de ganho, pois esse pré-processamento tende a elevar a acurácia do reconhecimento.

L1-R126. Julgue o item.
De acordo com o model card do Whisper, a diarização de falantes é uma capacidade que os modelos podem apresentar, sobretudo se ajustados para essa tarefa, mas que não foi avaliada de forma robusta.

L1-R127. Julgue o item.
No Amazon Transcribe, o filtro de vocabulário serve para melhorar o reconhecimento das palavras listadas, ao passo que o vocabulário personalizado serve para mascarar, remover ou marcar palavras específicas na saída da transcrição.

L1-R128. Julgue o item.
Uma equipe da Câmara avalia se o modelo base do Azure Speech atende ao Plenário. Segundo a documentação, ela pode comparar a transcrição do modelo com a humana do mesmo áudio pelo WER e, se este for alto, treinar um modelo personalizado.

L1-R129. Julgue o item.
Uma equipe estimou o tempo de degravação do acervo com as velocidades relativas da tabela do Whisper, medidas com fala em inglês em GPU A100, e agiu corretamente ao ressalvar que a velocidade real pode variar muito com o idioma e o hardware.

L1-R130. Julgue o item.
No Google Cloud Speech-to-Text, a requisição pode indicar o modelo de reconhecimento, treinado para determinado tipo de áudio, o que tende a melhorar os resultados quando a fonte do áudio é conhecida.

FIM DA PARTE 2/3

=====================================================================
PARTE 3/3 — (d-G) GABARITO COMENTADO
=====================================================================
Legenda: [TS] = troca sutil de um único conceito (em item C, a convenção "espelho" da GCE: a versão verdadeira de uma troca sutil). VOLÁTIL = gabarito depende de fato mutável de serviço; inapto a simulado final até a reverificação de 4–8/1/2027. REVERIFICAR = reabrir a URL da base e conferir o trecho em 4–8/1/2027 (conferência de base, sem efeito de VOLÁTIL, D-T89-R1-ACEITE). Todas as páginas foram abertas em 18/10/2026. QA PENDENTE em todos.

### P2-1.7

L1-R103. E [TS]. REVERIFICAR. Os papéis dos níveis estão trocados (no Amazon Transcribe): o nível de estabilidade alto transcreve mais rápido, com acurácia ligeiramente menor, e o baixo dá a maior acurácia.
Base: AWS, "Streaming and partial results", seção "Partial-result stabilization" (https://docs.aws.amazon.com/transcribe/latest/dg/streaming-partial-results.html), verificado em 18/10/2026: "Low stability provides the highest accuracy. High stability transcribes faster, but with slightly lower accuracy."

L1-R104. C. REVERIFICAR. A boa prática do Amazon Transcribe é, quando o fluxo não contém fala, enviar a mesma quantidade de silêncio; no PCM, o silêncio é uma sequência de bytes zero.
Base: AWS, "Transcribing streaming audio", boas práticas (https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html), verificado em 18/10/2026: "When your audio stream contains no speech, encode and send the same amount of silence. For example, silence for PCM is a stream of zero bytes."

L1-R105. C. REVERIFICAR. A documentação indica gravar a 16.000 Hz quando possível, como melhor compromisso entre qualidade e volume de dados pela rede, e observa que microfones de alta qualidade gravam a 44.100 ou 48.000 Hz.
Base: AWS, "Transcribing streaming audio", boas práticas (https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html), verificado em 18/10/2026: "If possible, record at a sampling rate of 16,000 Hz; this provides the best compromise between quality and data volume sent over the network."

L1-R106. E [TS]. REVERIFICAR. O model card diz que os modelos Whisper não podem ser usados para transcrição em tempo real fora da caixa; terceiros podem construir aplicações de tempo quase real sobre eles. A equipe não pode dispensar a aplicação adicional.
Base: repositório oficial openai/whisper, model card, seção "Broader Implications" (https://raw.githubusercontent.com/openai/whisper/main/model-card.md), arquivo aberto e lido em 18/10/2026 (HTTP 200): "Whisper models cannot be used for real-time transcription out of the box".

L1-R107. E [TS]. REVERIFICAR. Trocados os papéis: o síncrono é bloqueante e responde só depois de processar todo o áudio; o streaming fornece resultados intermediários enquanto o áudio é captado.
Base: Google Cloud, Speech-to-Text, "Cloud Speech-to-Text overview" (https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-requests), verificado em 18/10/2026 (página com "Last updated 2026-10-13 UTC"): reconhecimento síncrono "returns results after all audio has been processed"; streaming "provides interim results while audio is being captured".

L1-R108. E [TS]. REVERIFICAR. Trocados os papéis: Recognizing carrega os resultados intermediários e Recognized, os finais (tentativa de reconhecimento bem-sucedida).
Base: Microsoft, Azure Speech, "How to recognize speech" (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech), seção "Use continuous recognition", verificado em 18/10/2026: "Recognizing: Signal for events that contain intermediate recognition results. Recognized: Signal for events that contain final recognition results".

L1-R109. C. REVERIFICAR. No enunciado único o fim é determinado por silêncio ao final ou por um máximo de áudio processado; no contínuo, a aplicação controla quando parar (o número do limite não é cobrado).
Base: Microsoft, Azure Speech, "How to recognize speech" (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech), seção "Use continuous recognition", verificado em 18/10/2026.

L1-R110. E [TS]. VOLÁTIL (risco médio; limitação documentada de serviço, verificado em 18/10/2026). REVERIFICAR. A API REST para áudio curto devolve apenas resultados finais e não oferece resultados parciais; para texto parcial ao vivo usa-se o Speech SDK.
Base: Microsoft, Azure Speech, "Speech to text REST API for short audio" (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-speech-to-text-short), verificado em 18/10/2026 (página com "Last updated on 2026-06-05"): "returns only final results. It doesn't provide partial results."

L1-R111. E [TS]. REVERIFICAR. Fala longa sem pausas, na segmentação só por silêncio, gera subsegmentação (bloco longo de texto sem quebras); a fragmentação por pausas curtas é a sobressegmentação, outro problema.
Base: Microsoft, Azure Speech, "How to recognize speech", seção "Semantic segmentation" (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech), verificado em 18/10/2026: "Under-segmentation: When users speak for a long time without pauses, they can see a long sequence of text without breaks".

L1-R112. C [TS]. REVERIFICAR. Falsa pegadinha: "streaming" descreve a entrega do áudio em blocos sequenciais e inclui mídia pré-gravada, além de transmissões ao vivo.
Base: AWS, "Transcribing streaming audio" (https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html), verificado em 18/10/2026: "Streaming can include pre-recorded media (movies, music, and podcasts) and real-time media (live news broadcasts)."

L1-R113. C. REVERIFICAR. Ao exceder a cota de fluxos simultâneos, repete-se com backoff exponencial e, se o limite for atingido de forma recorrente, solicita-se aumento da cota.
Base: AWS, "Transcribing streaming audio", seção "Handling LimitExceededException errors" (https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html), verificado em 18/10/2026: "retry with exponential backoff. If you consistently hit this limit, request a service quota increase".

L1-R114. E [TS]. VOLÁTIL (risco médio; limite de serviço, verificado em 18/10/2026). REVERIFICAR. No Amazon Transcribe, a duração máxima é limite fixo que não pode ser aumentado; para continuar, inicia-se nova sessão de streaming.
Base: AWS, "Transcribing streaming audio", seção "Handling LimitExceededException errors" (https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html), verificado em 18/10/2026: "This is a hard limit that cannot be increased. To continue transcribing, start a new streaming session."

L1-R115. E [TS]. REVERIFICAR. O identificador do falante é genérico, atribuído pelo serviço durante o reconhecimento; o nome do parlamentar não vem do serviço, e a associação continua necessária.
Base: Microsoft, Azure Speech, "Real-time diarization quickstart" (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-stt-diarization), verificado em 18/10/2026: "The speaker ID is a generic identifier assigned to each conversation participant by the service during the recognition".

L1-R116. C. REVERIFICAR. A documentação recomenda fortemente os SDKs em vez de HTTP/2 ou WebSockets diretos, por serem o método mais simples e confiável.
Base: AWS, "Setting up a streaming transcription" (https://docs.aws.amazon.com/transcribe/latest/dg/streaming-setting-up.html), verificado em 18/10/2026: "We strongly recommend using SDKs rather than using HTTP/2 and WebSockets directly. SDKs are the simplest and most reliable method for transcribing data streams."

### P2-1.8

L1-R117. E [TS]. REVERIFICAR. Os modelos .en são as versões somente em inglês (tiny, base, small, medium); para transcrever português é preciso um modelo multilíngue.
Base: repositório oficial openai/whisper, README, seção "Available models and languages" (https://raw.githubusercontent.com/openai/whisper/main/README.md), arquivo aberto e lido em 18/10/2026 (HTTP 200): colunas "English-only model" e "Multilingual model"; "The .en models for English-only applications tend to perform better".

L1-R118. C. REVERIFICAR. A boa prática é usar codec sem perdas (FLAC ou LINEAR16); MP3 e outros codecs com perdas podem reduzir a acurácia.
Base: Google Cloud, Speech-to-Text, "Best practices" (https://docs.cloud.google.com/speech-to-text/docs/best-practices), verificado em 18/10/2026 (página com "Last updated 2026-10-13 UTC"): "Use a lossless codec to record and transmit audio. FLAC or LINEAR16 is recommended."

L1-R119. E [TS]. REVERIFICAR. Cerca de 65% (438 mil horas) é áudio em inglês com transcrição em inglês; a fala não inglesa com transcrição no próprio idioma é cerca de 17% (117 mil horas).
Base: repositório oficial openai/whisper, model card, seção "Training Data" (https://raw.githubusercontent.com/openai/whisper/main/model-card.md), aberto e lido em 18/10/2026 (HTTP 200): "65% of this data (or 438,000 hours) represents English-language audio and matched English transcripts". Os valores de 680 mil e de 65% são os do model card.

L1-R120. C [TS]. REVERIFICAR. Falsa pegadinha: a lista de frases é recurso de tempo de execução, fornecido pouco antes do reconhecimento, e não exige treinar modelo (diferente do custom speech).
Base: Microsoft, Azure Speech, "Improve recognition accuracy with phrase list" (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/improve-accuracy-phrase-list), verificado em 18/10/2026 (página com "Last updated on 2026-06-29"): "You provide a phrase list just before starting the speech recognition, so you don't need to train a custom model."

L1-R121. E [TS]. REVERIFICAR. A orientação é evitar reamostrar e enviar o áudio na taxa nativa (por exemplo, 8.000 Hz da telefonia); o ideal de 16.000 Hz vale para a captação, não para conversão posterior.
Base: Google Cloud, Speech-to-Text, "Best practices" (https://docs.cloud.google.com/speech-to-text/docs/best-practices), verificado em 18/10/2026: "However, avoid re-sampling. For example, in telephony the native rate is commonly 8000 Hz, which is the rate that should be sent to the service."

L1-R122. C. REVERIFICAR. O model card atribui a alucinação ao treinamento fracamente supervisionado com dados ruidosos em larga escala; a revisão humana cobre esse risco.
Base: repositório oficial openai/whisper, model card, seção "Performance and Limitations" (https://raw.githubusercontent.com/openai/whisper/main/model-card.md), aberto e lido em 18/10/2026: "the predictions may include texts that are not actually spoken in the audio input (i.e. hallucination)".

L1-R123. E [TS]. REVERIFICAR. Trocado o modo: no lote, submete-se o áudio e recupera-se o resultado depois, de forma assíncrona; o item o descreve como síncrono, na própria chamada.
Base: Microsoft, Azure Speech, "What is batch transcription?" (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription), verificado em 18/10/2026 (página com "Last updated on 2026-06-25"): "you submit the audio data, and then retrieve transcription results asynchronously".

L1-R124. C. REVERIFICAR. O model card adverte contra o uso dos modelos Whisper para transcrever gravações de pessoas feitas sem o consentimento delas; o item reproduz a advertência, sem acrescentar vínculo.
Base: repositório oficial openai/whisper, model card, seção "Evaluated Use" (https://raw.githubusercontent.com/openai/whisper/main/model-card.md), aberto e lido em 18/10/2026 (HTTP 200): "we caution against using Whisper models to transcribe recordings of individuals taken without their consent".

L1-R125. E [TS]. REVERIFICAR. Polaridade invertida: aplicar redução de ruído antes do envio tende a reduzir a acurácia, e o controle automático de ganho não deve ser usado; o serviço foi projetado para áudio ruidoso.
Base: Google Cloud, Speech-to-Text, "Best practices", seção "Audio preprocessing" (https://docs.cloud.google.com/speech-to-text/docs/best-practices), verificado em 18/10/2026: "applying noise-reduction signal processing to the audio before sending it to the service typically reduces recognition accuracy".

L1-R126. C [TS]. REVERIFICAR. Falsa pegadinha: o model card admite que os modelos podem apresentar diarização, sobretudo se ajustados, mas diz que não foi avaliada de forma robusta; não é capacidade validada.
Base: repositório oficial openai/whisper, model card, seção "Evaluated Use" (https://raw.githubusercontent.com/openai/whisper/main/model-card.md), aberto e lido em 18/10/2026: "They may exhibit additional capabilities, particularly if fine-tuned on certain tasks like voice activity detection, speaker classification, or speaker diarization but have not been robustly evaluated in these areas."

L1-R127. E [TS]. REVERIFICAR. Papéis trocados: o vocabulário personalizado melhora a acurácia de palavras específicas; o filtro de vocabulário altera palavras na saída (mascarar, remover ou marcar).
Base: AWS, "Using custom vocabulary filters to delete, mask, or flag words" (https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html) e "Custom vocabularies" (https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html), verificado em 18/10/2026: "Vocabulary filtering has three display methods: mask, remove, and tag."; "Use custom vocabularies to improve transcription accuracy for one or more specific words."

L1-R128. C. REVERIFICAR. A documentação recomenda comparar a transcrição do modelo base com a transcrição humana do mesmo áudio, obter o WER e, se alto, treinar um modelo personalizado.
Base: Microsoft, Azure Speech, "What is custom speech?", seção "Choose your model" (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-speech-overview), verificado em 18/10/2026 (página com "Last updated on 2026-02-25").

L1-R129. C. REVERIFICAR. O README informa, e a conduta de ressalvar é a correta, porque as velocidades relativas foram medidas com fala em inglês em uma A100 e a velocidade real pode variar significativamente com idioma, velocidade da fala e hardware.
Base: repositório oficial openai/whisper, README, seção "Available models and languages" (https://raw.githubusercontent.com/openai/whisper/main/README.md), aberto e lido em 18/10/2026: "the real-world speed may vary significantly depending on many factors including the language, the speaking speed, and the available hardware".

L1-R130. C. REVERIFICAR. A documentação diz que o serviço usa modelos treinados para tipos de áudio específicos e que informar a fonte do áudio na requisição pode melhorar os resultados; nenhum nome de modelo é cobrado.
Base: Google Cloud, Speech-to-Text, "Cloud Speech-to-Text overview", seção "Model selection" (https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-requests), verificado em 18/10/2026.

## Contagens
| quesito | valor |
|---|---|
| total | 28 (P2-1.7: 14; P2-1.8: 14) |
| C | 14 (P2-1.7: R104, R105, R109, R112, R113, R116; P2-1.8: R118, R120, R122, R124, R126, R128, R129, R130) = 50,0% (faixa de 11 a 17 C cumprida); por folha: 1.7 com 6 C / 8 E; 1.8 com 8 C / 6 E (R124 segue C, mesmo id: sem mudança na contagem da v1) |
| E | 14 (P2-1.7: R103, R106, R107, R108, R110, R111, R114, R115; P2-1.8: R117, R119, R121, R123, R125, R127) |
| [TS] | 17 de 28 = 60,7% (meta "metade mais 2" = 16, cumprida): P2-1.7: R103, R106, R107, R108, R110, R111, R112, R114, R115 (9; 8 E e 1 C); P2-1.8: R117, R119, R120, R121, R123, R125, R126, R127 (8; 6 E e 2 C) |
| [TS] com gabarito C | 3 (R112, R120, R126), por convenção "espelho"; sem relação fixa entre [TS] e gabarito |
| VOLÁTIL | 2 novos, ambos em P2-1.7: R110 e R114 (risco médio); risco alto novo 0. P2-1.8: 0 novos |
| VOLÁTIL por folha de 20 | P2-1.7: Q16, R110, R114 = 3/20 = 15%; P2-1.8: Q18, Q19 = 2/20 = 10% |
| formato máximo por folha de 20 | P2-1.7: 20% (D, SH, AP com 4); P2-1.8: 30% (SH com 6, no teto) |
| REVERIFICAR (4–8/1/2027) | 28 (todos têm base em página de fornecedor); 2 desses também VOLÁTEIS (R110, R114) |
| extensão (palavras do enunciado) | C: média 35,6 (de 30 a 43); E: média 37,4 (de 31 a 48); nenhum C acima de 65 palavras (O-1) |

Observações de estilo (registros O-1 a O-8 da T-93):
- O-1: nenhum C passa de 65 palavras (máximo 43); o E mais longo (R110, 48 palavras) supera o C mais longo (R129, 43); a média de E (37,4) é maior que a de C (35,6).
- O-2: "independentemente" em C (R104).
- O-3: "pode" também em E (R106, R110, R114, R117), além de C (R112, R118, R122, R126, R129, R130).
- O-4: as remissões a documentos ("Segundo as boas práticas", "De acordo com o model card", "o model card adverte") não têm, na mesma oração, vínculo que a fonte não traga.
- O-5: nenhuma cauda falsa se denuncia; os erros são trocas de papel, de sujeito ou de polaridade.
- O-6: [TS] em três itens C (R112, R120, R126), convenção da GCE.
- O-7: restritivo em C ("apenas" em R112); o "somente" do R124 da v1 saiu com a substituição do item.
- O-8: concessiva em E ("ainda que" em R103).

## Tabela de proveniência (todas abertas e lidas em 18/10/2026)
| fonte | URL oficial | data da página / verificação | usada em |
|---|---|---|---|
| AWS, Amazon Transcribe, Transcribing streaming audio | https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html | verificado em 18/10/2026 (HTTP 200) | R104, R105, R112, R113, R114 |
| AWS, Amazon Transcribe, Streaming and partial results | https://docs.aws.amazon.com/transcribe/latest/dg/streaming-partial-results.html | verificado em 18/10/2026 (HTTP 200) | R103 |
| AWS, Amazon Transcribe, Setting up a streaming transcription | https://docs.aws.amazon.com/transcribe/latest/dg/streaming-setting-up.html | verificado em 18/10/2026 (HTTP 200) | R116 |
| AWS, Amazon Transcribe, Using custom vocabulary filters to delete, mask, or flag words | https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html | verificado em 18/10/2026 (HTTP 200) | R127 |
| AWS, Amazon Transcribe, Custom vocabularies | https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html | verificado em 18/10/2026 (HTTP 200) | R127 |
| Google Cloud, Speech-to-Text, Cloud Speech-to-Text overview (tipos de requisição, seleção de modelo) | https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-requests | "Last updated 2026-10-13 UTC"; verificado em 18/10/2026 (HTTP 200) | R107, R130 |
| Google Cloud, Speech-to-Text, Best practices | https://docs.cloud.google.com/speech-to-text/docs/best-practices | "Last updated 2026-10-13 UTC"; verificado em 18/10/2026 (HTTP 200) | R118, R121, R125 |
| Microsoft, Azure Speech, How to recognize speech | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech | "Last updated on 2026-06-05"; verificado em 18/10/2026 (HTTP 200) | R108, R109, R111 |
| Microsoft, Azure Speech, Speech to text REST API for short audio | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-speech-to-text-short | "Last updated on 2026-06-05"; verificado em 18/10/2026 (HTTP 200) | R110 |
| Microsoft, Azure Speech, Real-time diarization quickstart | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-stt-diarization | "Last updated on 2026-01-31"; verificado em 18/10/2026 (HTTP 200) | R115 |
| Microsoft, Azure Speech, Improve recognition accuracy with phrase list | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/improve-accuracy-phrase-list | "Last updated on 2026-06-29"; verificado em 18/10/2026 (HTTP 200) | R120 |
| Microsoft, Azure Speech, What is batch transcription? | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription | "Last updated on 2026-06-25"; verificado em 18/10/2026 (HTTP 200) | R123 |
| Microsoft, Azure Speech, What is custom speech? | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-speech-overview | "Last updated on 2026-02-25"; verificado em 18/10/2026 (HTTP 200) | R128 |
| OpenAI, repositório oficial openai/whisper (README, ramo main) | https://raw.githubusercontent.com/openai/whisper/main/README.md | arquivo aberto e lido em 18/10/2026 (HTTP 200); a página github.com/openai/whisper não foi usada como base | R117, R129 |
| OpenAI, repositório oficial openai/whisper (model card, ramo main) | https://raw.githubusercontent.com/openai/whisper/main/model-card.md | arquivo aberto e lido em 18/10/2026 (HTTP 200) | R106, R119, R122, R124, R126 |

Fontes que não abri (nenhum item delas entrou): developers.openai.com e platform.openai.com (documentação da API da OpenAI), openai.com, arxiv.org (artigo do Whisper), github.com (páginas), huggingface.co, w3.org. Nenhuma norma foi usada (nenhum PENDENTE NORMATIVO). Nenhum item cita data de verificação em que a página não foi aberta.
Discrepância observada e evitada: o README do Whisper (809 M) e o model card (798 M) divergem na contagem de parâmetros do modelo turbo; nenhum item usa essa contagem.

FIM DA PARTE 3/3
FIM DO LOTE
