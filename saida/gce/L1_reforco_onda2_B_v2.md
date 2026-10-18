# L1_reforco_onda2_B_v2.md — T-96 — 2026-10-18 — gerado por gce-cpp

## RESPOSTA AO PARECER QA_T96B_R1_2026-10-18_gce-cqfp.md (rodada 2 de no máximo 2)

| ponto do parecer | resposta |
|---|---|
| L1-R58 REPROVADO (escopo: top-K é parâmetro genérico de LLM, tema de P1-5.1) | acatado. Substituído, com o mesmo id, por item novo de 1.3, gabarito C, formato definição (mantém D 3, TS 3, SH 4, NP 3, PC 3, AP 4 na folha), sobre áudio/fala conversacional dentro do texto "LLMs multimodais de áudio nativo": a conexão bidirecional em fluxo contínuo (áudio do usuário enviado enquanto o modelo processa e gera a resposta), em oposição ao padrão requisição-resposta. Ponto distinto dos 19 restantes e de P1-5.1. Base aberta hoje: AWS, Amazon Nova Sonic, Using the Speech-to-Speech model, com trecho literal (Parte 3). VOLÁTIL: não. |
| A-1 (L1-R48) | acatado. Enunciado, Parte 3 (duas substituições) e ponto do mapa aplicados com o texto exato; gabarito E, [TS] e formato PC mantidos. |
| A-2 (L1-R54) | acatado. Enunciado, Parte 3 (frase de abertura) e ponto do mapa aplicados com o texto exato; gabarito E, [TS], VOLÁTIL (médio) e concessiva em E (O-8) mantidos. |
| A-3 (L1-R60) | acatado. Última frase do enunciado e a justificativa (16 × 8 = 128 min) aplicadas com o texto exato; gabarito E e [TS] mantidos. |
| A-4 (L1-R62) | acatado. Enunciado substituído sem o nome da ferramenta; Parte 3 e base inalteradas. |
| A-5 (L1-R70) | acatado. Enunciado substituído (contexto de comissão); formato AP mantido; Parte 3 inalterada. |
| A-6 (L1-R73) | acatado. Enunciado substituído sem o nome da ferramenta; Parte 3 e base inalteradas. |
| Correção de registro (extensão: "E média 39,9 (de 32 a 51)") | acatado. Linha "Extensão" da Parte 3 refeita por contagem sobre a Parte 2 desta v2 (valores na seção "Contagens"). |
| URLs redirecionadas (Vertex AI para Gemini Enterprise Agent Platform; Azure OpenAI para Azure Foundry) | acatado. URLs finais registradas na tabela de proveniência (colunas "URL final"), reabertas em 18/10/2026 (HTTP 200); a justificativa de R48 nomeia a página pelo título atual (A-1). Entram na conferência de base de 4–8/1/2027. |
| Registros para a D1 (coerência VOLÁTIL R65 × R71; R57 conservador; R62 × L1-Q20/Q18; concentração no README do pyannote, ramo develop; R49 com base de console; R68 baixa discriminação; estilo opcional de R63) | registrados, sem alteração de texto (o parecer não pede ajuste). R63 fica como está ("não mude mais nada"). |

Nada mais foi alterado. As folhas 1.1, 1.2 (parte A), 1.5–1.8 (partes C e D) não são repetidas aqui.

Objeto: REFORÇO onda 2, parte B (D-REFORCO-2; T-96), ciclo 2026-10-18 s12c3. Folhas P2-1.3 (LLMs multimodais de áudio nativo) e P2-1.4 (diarização de falantes): +14 itens AUTORAL em cada uma, ids L1-R47 a L1-R60 (1.3) e L1-R61 a L1-R74 (1.4). Cada folha vai de 6 para 20 itens.
Rótulo de todos os itens: AUTORAL (produtor gce-cpp, lote L1-R, onda 2 do reforço, D-REFORCO-1/2). Nenhum item existente foi alterado.
QA PENDENTE: nenhum item deste arquivo entra em simulado antes do parecer da gce-cqfp (máximo de 2 rodadas) e da reconciliação da gce-gerencia (D-QA-PENDENTE).
Convenção: "verificado em 18/10/2026" = página aberta e lida nesta data, na íntegra do trecho citado. Nenhum item usa base de data anterior (D-FONTE-DATA-ANTERIOR não foi acionada). Nenhum item cita norma, versão, preço ou limite de produto como dado do gabarito: os números dos itens NP são hipóteses do enunciado.
Instruções aplicadas: T89_reconciliacao (seções 1 e 3: critério de VOLÁTIL; [TS] em pelo menos metade dos itens da onda mais 2; na 1.4, nenhum item de definição nem de par confundível); T93_reconciliacao e estilo_onda_1 (registros O-1 a O-8).

=====================================================================
PARTE 1/3 — MAPA
=====================================================================

## 1.1 Itens novos — P2-1.3 (um ponto de julgamento por item)

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL |
|---|---|---|---|---|---|
| L1-R47 | P2-1.3 | "Multimodal" indica que o mesmo modelo aceita mais de uma modalidade de entrada (texto, áudio etc.); o áudio é uma delas | definição | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/live-api (tabela "Input modalities"); https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html ("Cross-modal input support") | n |
| L1-R48 | P2-1.3 | Receber áudio como entrada não obriga a resposta em áudio; a saída pode ser texto ou áudio | par confundível | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/audio-understanding (compreensão de fala devolve texto); https://docs.cloud.google.com/vertex-ai/generative-ai/docs/live-api (saída em áudio ou texto) | n |
| L1-R49 | P2-1.3 | Gravação que excede o limite de entrada pode ter a parte excedente truncada e não processada; convém conferir a cobertura do texto devolvido | situação hipotética | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/audio-understanding (passo do console: "the tokens are truncated and aren't included in processing your data") | S (baixo) |
| L1-R50 | P2-1.3 | Temperatura zero reduz a variação, mas não garante respostas idênticas entre execuções | situação hipotética | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/audio-understanding (parâmetro Temperature: "mostly deterministic, but a small amount of variation is still possible") | n |
| L1-R51 | P2-1.3 | O modelo pode errar ao reconhecer sons que não são fala (aplausos, ruído); as marcações de ruído exigem conferência | aplicação parlamentar | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/audio-understanding (seção "Limitations", non-speech sound recognition) | n |
| L1-R52 | P2-1.3 | Em sessão conversacional, a transcrição da fala do usuário é recurso complementar (canal lateral); a entrada do modelo continua sendo o áudio | troca de sujeito | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/live-api ("Audio transcriptions ... side channel of a conversation"); https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/audio-real-time (transcrição da entrada por opt-in com modelo de transcrição); https://docs.aws.amazon.com/nova/latest/userguide/speech.html (transcrições de texto da fala do usuário como evento de saída) | n |
| L1-R53 | P2-1.3 | O limite de tokens de saída por resposta pode ser menor que o texto da transcrição integral; com a conversão dada (100 tokens ≈ 75 palavras) e limite de 8.000, 12.000 palavras exigem ao menos 2 respostas | número ou prazo | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/audio-understanding (parâmetro Output token limit: "100 tokens correspond to roughly 60-80 words"); valores do enunciado são hipótese | n (aritmética) |
| L1-R54 | P2-1.3 | Nos modelos Gemini (Google Cloud), carimbos de tempo precisos em arquivo só de áudio exigem configurar o parâmetro de geração; pedir na instrução não basta | situação hipotética | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/audio-understanding (seção "Limitations", audio-only timestamps; "Audio transcription") | S (médio) |
| L1-R55 | P2-1.3 | O modelo conversacional pode ser combinado a RAG e chamada de funções, para apoiar respostas em dados consultados e não só no conhecimento do modelo | aplicação parlamentar | https://docs.aws.amazon.com/nova/latest/userguide/speech.html ("Knowledge grounding with enterprise data using Retrieval Augmented Generation (RAG)"; "Function calling"); https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html; https://docs.cloud.google.com/vertex-ai/generative-ai/docs/live-api ("Tool use") | n |
| L1-R56 | P2-1.3 | Transmitir a resposta à medida que é gerada reduz a percepção de latência, não o tempo total de processamento | troca de sujeito | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/audio-understanding ("To reduce the perception of latency to a human audience, stream the response as it's being generated") | n |
| L1-R57 | P2-1.3 | O modelo conversacional de áudio nativo pode permitir interrupção da resposta falada (barge-in) mantendo o contexto da conversa | aplicação parlamentar | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/live-api ("Barge-in: Users can interrupt the model at any time"); https://docs.aws.amazon.com/nova/latest/userguide/speech.html ("Graceful handling of user interruptions without dropping conversational context") | S (baixo) |
| L1-R58 | P2-1.3 | Em modelo conversacional de áudio nativo, a conexão bidirecional em fluxo contínuo permite enviar o áudio do usuário enquanto o modelo processa a fala e gera a resposta, em oposição ao padrão requisição-resposta | definição | https://docs.aws.amazon.com/nova/latest/userguide/speech.html ("Bidirectional event streaming ... Unlike traditional request-response patterns, this approach permits ... Continuous audio streaming from the user to the model; Concurrent speech processing and generation") | n |
| L1-R59 | P2-1.3 | O áudio enviado conta como tokens do prompt (entrada), não como tokens da resposta gerada (saída) | par confundível | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/audio-understanding (limite de áudio "per prompt" expresso em tokens; amostra com promptTokenCount e candidatesTokenCount) | n |
| L1-R60 | P2-1.3 | Com limite de duração por conexão, a sessão longa exige renovação e continuação; 130 min com limite de 8 min exigem 17 conexões (arredondamento para cima), não 16 | número ou prazo | https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html ("Connection limit of 8 minutes, with connection renewal and session continuation pattern"); valores do enunciado são hipótese | n (aritmética) |

## 1.2 Itens novos — P2-1.4 (um ponto de julgamento por item; sem definição e sem par confundível, T89 seção 3)

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL |
|---|---|---|---|---|---|
| L1-R61 | P2-1.4 | A DER é taxa de erro (em %): quanto menor, melhor; o sistema de maior DER nas mesmas gravações é o pior | troca de sujeito | https://raw.githubusercontent.com/pyannote/pyannote-audio/develop/README.md ("Diarization error rate (in %, the lower, the better)") | n |
| L1-R62 | P2-1.4 | Pipeline de código aberto de diarização pode ser executado localmente, sem enviar o áudio a serviço de terceiros | aplicação parlamentar | https://raw.githubusercontent.com/pyannote/pyannote-audio/develop/README.md (exemplo "community-1", comentário "# runs locally") | n |
| L1-R63 | P2-1.4 | Oferecer diarização em um modo (lote) não implica oferecê-la em outro (streaming): o recurso varia por modelo e método de reconhecimento | situação hipotética | https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3 (tabela de recursos: diarização "Available only in Speech.BatchRecognize"; carimbos por enunciado "Available only in Speech.StreamingRecognize"); https://docs.aws.amazon.com/transcribe/latest/dg/feature-matrix.html | n |
| L1-R64 | P2-1.4 | Na transcrição por canais, falas simultâneas em canais distintos aparecem com intervalos de tempo sobrepostos | troca de sujeito | https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html ("timestamps for each channel overlap while the individuals are speaking over each other") | n |
| L1-R65 | P2-1.4 | Na diarização em tempo real, resultados parciais podem trazer falante ainda desconhecido; o rótulo vem depois | troca de sujeito | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-stt-diarization (saída de exemplo: "Speaker ID=Unknown" nos primeiros parciais, depois "Guest-1"; propriedade DiarizeIntermediateResults) | S (baixo) |
| L1-R66 | P2-1.4 | Rótulos genéricos valem dentro do áudio processado; em arquivos processados separadamente, o mesmo rótulo pode designar oradores diferentes | aplicação parlamentar | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-stt-diarization ("generic identifier assigned ... from the provided audio content"); https://docs.cloud.google.com/speech-to-text/docs/multiple-voices ("labels by number the individual voices detected in the audio") | n |
| L1-R67 | P2-1.4 | No Google Cloud Speech-to-Text a diarização pede as contagens mínima e máxima de falantes esperados (não apenas o máximo) | troca de sujeito | https://docs.cloud.google.com/speech-to-text/docs/multiple-voices ("You must set the min_speaker_count and max_speaker_count values") | S (médio) |
| L1-R68 | P2-1.4 | Tempo de processamento proporcional à duração: 36 s por hora de áudio × 50 h = 1.800 s = 30 min | número ou prazo | https://raw.githubusercontent.com/pyannote/pyannote-audio/develop/README.md (velocidade expressa em "s per hour of audio"); valores do enunciado são hipótese | n (aritmética) |
| L1-R69 | P2-1.4 | Na transcrição rápida do Azure Speech, por padrão os canais de entrada são mesclados em um só antes da transcrição; transcrever por canal exige configurar | situação hipotética | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/fast-transcription-create ("By default, the fast transcription API merges all input channels into a single channel") | S (médio) |
| L1-R70 | P2-1.4 | Saída só com intervalos de tempo e rótulos não traz texto; a transcrição com falantes exige combinar com a saída do ASR | aplicação parlamentar | https://raw.githubusercontent.com/pyannote/pyannote-audio/develop/README.md (saída de exemplo: "start=0.2s stop=1.5s speaker_0") | n |
| L1-R71 | P2-1.4 | Há serviços que rotulam o falante palavra a palavra, o que permite representar a troca de orador no meio da frase; não é verdade que todo serviço só rotule trechos inteiros | troca de sujeito | https://docs.cloud.google.com/speech-to-text/docs/multiple-voices ("tags each word with a number assigned to individual speakers"); https://docs.aws.amazon.com/transcribe/latest/dg/diarization.html (itens com speaker_label) | n |
| L1-R72 | P2-1.4 | A oferta de transcrição em pt-BR não garante, por si só, a de diarização no idioma: a lista de idiomas com diarização pode ser mais restrita | situação hipotética | https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3 (seções "Language availability" e "Language availability for diarization"); https://docs.cloud.google.com/speech-to-text/docs/multiple-voices ("Review the language support page") | n |
| L1-R73 | P2-1.4 | Pipelines pré-treinados de código aberto podem ser ajustados com dados próprios (como gravações da Casa) para buscar melhor desempenho | aplicação parlamentar | https://raw.githubusercontent.com/pyannote/pyannote-audio/develop/README.md ("pretrained models and pipelines, that can be further finetuned to your own data for even better performance") | n |
| L1-R74 | P2-1.4 | Serviço com máximo de falantes distintos por arquivo (30, rótulos spk_0 a spk_29) não distingue 45 oradores em um único arquivo | número ou prazo | https://docs.aws.amazon.com/transcribe/latest/dg/diarization.html ("a maximum of 30 unique speakers ... spk_0 through spk_29"); os 45 oradores do enunciado são hipótese | n |

## 2 Folhas de 20 itens: ponto, formato e VOLÁTIL (existentes + novos)

Classificação dos 6 itens existentes de cada folha conforme o mapa canônico (T89 reconciliação, seção 6, e L1_reforco_onda1_v2.md, seção 2). D = definição; TS = troca de sujeito; SH = situação hipotética; NP = número ou prazo; PC = par confundível; AP = aplicação parlamentar.

### P2-1.3 (6 existentes + 14 novos = 20)
| id | ponto | formato | VOL |
|---|---|---|---|
| L1-Q05 | Áudio nativo entra no próprio LLM, sem ASR separado | D | n |
| L1-Q06 | Na cascata o LLM recebe só texto; prosódia se perde | TS | n |
| L1C-Q25 | LLM nativo não copia literalmente a fala; revisão humana permanece | AP | n |
| L1C-Q26 | ASR reforçado por LLM não é LLM de áudio nativo | PC | n |
| L1-R05 | Mesmo áudio, instruções diferentes: transcrição, resumo, tradução | SH | n |
| L1-R06 | Tokens de áudio proporcionais à duração (2 h = 216.000) | NP | n |
| L1-R47 a L1-R60 | ver tabela 1.1 | D, PC, SH, SH, AP, TS, NP, SH, AP, TS, AP, D, PC, NP | R49, R54, R57 = S |

Contagem de formatos da folha (20): D 3 (Q05, R47, R58) = 15%; TS 3 (Q06, R52, R56) = 15%; SH 4 (R05, R49, R50, R54) = 20%; NP 3 (R06, R53, R60) = 15%; PC 3 (Q26, R48, R59) = 15%; AP 4 (Q25, R51, R55, R57) = 20%. Soma 20. Teto de 30% (6 itens) cumprido por todos; o maior é 20%.
Contagem de VOLÁTEIS da folha (20): existentes 0; novos 3 (R49 baixo, R54 médio, R57 baixo) = 15%. Teto de 20% (4 itens) cumprido. Risco alto: 0.

### P2-1.4 (6 existentes + 14 novos = 20)
| id | ponto | formato | VOL |
|---|---|---|---|
| L1-Q07 | Diarização entrega rótulos genéricos; nomes exigem identificação | AP | n |
| L1-Q08 | Verificação de locutor é 1:1; diarizar não exige verificar | PC | n |
| L1-Q09 | DER (falante, fala perdida, falso alarme) distinto de WER | D | n |
| L1C-Q27 | "Identificar" no sentido amplo = distinguir, não nomear | D | n |
| L1C-Q28 | O objeto de "identificar" decide o sentido (que há 3 × pelo nome) | PC | n |
| L1-R07 | Separação por canais, distinta da diarização | SH | n |
| L1-R61 a L1-R74 | ver tabela 1.2 | TS, AP, SH, TS, TS, AP, TS, NP, SH, AP, TS, SH, AP, NP | R65 = S (baixo); R67 = S (médio); R69 = S (médio) |

Contagem de formatos da folha (20): D 2 (Q09, L1C-Q27) = 10%; PC 2 (Q08, L1C-Q28) = 10%; AP 5 (Q07, R62, R66, R70, R73) = 25%; SH 4 (R07, R63, R69, R72) = 20%; TS 5 (R61, R64, R65, R67, R71) = 25%; NP 2 (R68, R74) = 10%. Soma 20. Teto de 30% (6 itens) cumprido; o maior é 25%. Os excessos legados da 1.4 (D e PC a 33,3% na folha de 6) ficam diluídos a 10% cada, sem nenhum D nem PC novo.
Contagem de VOLÁTEIS da folha (20): existentes 0; novos 3 (R65 baixo, R67 médio, R69 médio) = 15%. Teto de 20% cumprido. Risco alto: 0.

### Resumo da parte B (28 itens)
- VOLÁTEIS novos: 6 (R49, R54, R57; R65, R67, R69). Risco alto: 0 (teto de 1 nesta parte). Nenhum VOLÁTIL em item de norma (nenhuma norma citada).
- Gabarito: 14 C / 14 E (50,0%; faixa de 11 a 17 C cumprida). 1.3: 7 C / 7 E. 1.4: 7 C / 7 E.
- [TS]: 17 de 28 (60,7%; meta da T89: metade da onda mais 2 = 16): 14 com gabarito E (todos os E) e 3 com gabarito C ("falsa pegadinha", convenção O-6).

## 3 Verificação de não repetição e proximidades

Comparação feita item a item contra o pacote v1.9 (filtro P2-1.3 e P2-1.4) e contra os canônicos GCE_Lote1_v2_CPP, GCE_Lote1C_v2_CPP, GCE_Lote1_consolidacao_GCE e L1_reforco_onda1_v2.
- 1.3: nenhum ponto repete Q05 (áudio entra no LLM sem ASR), Q06 (cascata e prosódia), L1C-Q25 (cópia literal e revisão), L1C-Q26 (ASR reforçado por LLM), R05 (instruções diferentes) ou R06 (tokens proporcionais à duração). Proximidades que a Gerência pode querer ver: R47 × Q05 (multimodal = várias modalidades × áudio entra no próprio modelo); R48 × Q05 (o que "nativo" qualifica: entrada × ausência de ASR); R49 e R53 × R06 (mesma família "tokens e limites", mas o ponto é truncamento do excedente e limite de saída, não a conversão duração–tokens); R58 × R57 (fluxo bidirecional contínuo × interrupção da resposta falada com manutenção do contexto) e R58 × R56 (conexão em fluxo nos dois sentidos × transmissão da resposta de uma requisição); a R58 não julga interrupção nem redução de latência; R52 × R59 (transcrição lateral × contagem de tokens); R60 × R06 (arredondamento de conexões × conversão de tokens). Fora da folha: R50 × L4-04 (P1-5.1, temperatura e factualidade): pontos distintos. O item substituído na R2 (top-K, tema de P1-5.1) saiu da folha.
- 1.4: nenhum ponto repete Q07 (rótulos genéricos; nomes exigem identificação), Q08 (verificação 1:1), Q09 (composição da DER × WER), L1C-Q27, L1C-Q28 ou R07 (separação por canais distinta da diarização). Proximidades: R66 × Q07 (consistência de rótulos entre arquivos × nomes exigem identificação); R61 × Q09 (sentido "menor é melhor" × composição da DER); R64 × R07 (sobreposição de tempos em canais distintos × canal distinto da diarização); R64 × R71 (simultaneidade em canais × troca de orador no meio da frase, rotulagem palavra a palavra); R63 × R72 (recurso por modo × recurso por idioma); R62, R70 e R73 usam o mesmo README, mas julgam coisas distintas (execução local, forma da saída, ajuste com dados próprios).
- Proximidades entre folhas desta parte e outras folhas (só registro): R65 × L1-Q15 (1.7; parciais revisáveis × rótulo de falante em parcial); R69 × L1-R07 (mesma folha, 1.4; canal × padrão de mesclagem do Azure).

## 4 Conformidade com os registros de estilo (O-1 a O-8) e com a D-REFORCO-2

- O-1 (extensão): C encurtados e E mais longos; médias de palavras por gabarito conferidas por contagem na Parte 3 (seção "Contagens"). Nenhum C passa de 65 palavras.
- O-2: C com "independentemente" em L1-R66.
- O-3: "pode/podem" também em E (L1-R54, L1-R63).
- O-4: nenhuma oração depois de "Segundo..." ou "Na documentação..." carrega vínculo alheio à fonte; os itens que nomeiam produto (R67, R69) afirmam só o conteúdo da página citada.
- O-5: sem cauda autocontraditória; nos E, o erro é uma só afirmação.
- O-6: [TS] em C usado em 3 itens (R49, R64, R72), como falsa pegadinha.
- O-7: restritivos também em C ("apenas": R47, R55, R70); causais "pois"/"razão pela qual" em C (R49, R72) e em E (R48, R50).
- O-8: concessiva em E (L1-R54, "Ainda que").
- Regra 1 (D-REFORCO-2): um ponto por item, único na folha (seção 3). Regra 2: base por item com URL aberta hoje. Regra 3: no máximo 25% de um formato na folha de 20 (teto 30%). Regra 4: VOLÁTIL 15% por folha (teto 20%). Regra 5: 50,0% de C na parte B.

FIM DA PARTE 1/3

=====================================================================
PARTE 2/3 — (d) ITENS DO ESTUDANTE
=====================================================================

L1-R47. Julgue o item.
No LLM multimodal de áudio nativo, a palavra multimodal indica que o mesmo modelo aceita mais de uma modalidade de entrada, como texto e áudio, e o áudio é apenas uma delas.

L1-R48. Julgue o item.
Um LLM multimodal que recebe o áudio diretamente como modalidade de entrada só é capaz de devolver a resposta em áudio sintetizado, e não em texto.

L1-R49. Julgue o item.
Uma equipe envia a um LLM de áudio nativo, em uma única requisição, a gravação de uma sessão cuja duração excede o limite de entrada do modelo. Nessa situação, a parte excedente pode ser truncada e não ser processada, razão pela qual convém conferir se o texto devolvido cobre toda a gravação.

L1-R50. Julgue o item.
Ao transcrever repetidamente a mesma gravação com um LLM de áudio nativo, uma equipe configura a temperatura em zero. Nessa situação, as respostas de todas as execuções serão rigorosamente idênticas, pois a temperatura zero elimina toda a aleatoriedade do processo de geração.

L1-R51. Julgue o item.
Em gravações do Plenário, aplausos, vaias e ruídos de fundo não constituem fala, e um LLM de áudio nativo pode errar ao reconhecê-los, o que recomenda a conferência, na revisão, das marcações de ruído do texto.

L1-R52. Julgue o item.
Em uma sessão conversacional com LLM de áudio nativo, a transcrição da fala do usuário que o serviço entrega ao cliente, quando habilitada, é o texto que o modelo recebe como entrada, no lugar do áudio, e é por meio dele que a resposta é elaborada.

L1-R53. Julgue o item.
Considere que, em determinado LLM de áudio nativo, 100 tokens correspondam a cerca de 75 palavras e que o limite de saída de cada resposta seja de 8.000 tokens. Nessa hipótese, a transcrição integral de uma exposição de 12.000 palavras não cabe em uma única resposta, sendo necessárias ao menos duas.

L1-R54. Julgue o item.
Segundo a documentação do Google Cloud para os modelos Gemini, uma equipe que deseje carimbos de tempo precisos na transcrição de um arquivo que contenha somente áudio pode obtê-los apenas pedindo os tempos na instrução em texto, ainda que não faça nenhuma configuração específica de geração.

L1-R55. Julgue o item.
Em um assistente de voz da Casa, um LLM de áudio nativo conversacional pode ser combinado à recuperação de dados do acervo (RAG) e à chamada de funções, de modo que a resposta sobre uma proposição se apoie em dados consultados, e não apenas no conhecimento do modelo.

L1-R56. Julgue o item.
Em um LLM de áudio nativo, transmitir a resposta à medida que é gerada (streaming) reduz o tempo total de processamento da requisição, e não apenas a percepção de latência de quem aguarda o texto.

L1-R57. Julgue o item.
Em um serviço de atendimento por voz da Casa, um LLM de áudio nativo conversacional pode permitir que o usuário interrompa a resposta falada e retome o diálogo sem que o modelo perca o contexto da conversa.

L1-R58. Julgue o item.
Em um LLM de áudio nativo conversacional, a conexão bidirecional em fluxo contínuo permite que o áudio do usuário seja enviado ao modelo enquanto este processa a fala e gera a resposta, diferentemente do padrão de requisição e resposta, em que o modelo só responde depois de receber o conteúdo completo.

L1-R59. Julgue o item.
Ao enviar a um LLM de áudio nativo a gravação de uma sessão acompanhada de uma instrução de resumo, os tokens correspondentes ao áudio são contabilizados como tokens da resposta gerada, e não como tokens do prompt.

L1-R60. Julgue o item.
Considere que um serviço de áudio nativo em tempo real limite cada conexão a 8 minutos e permita renová-la, com continuação da sessão. Nessa hipótese, 16 conexões consecutivas bastam para o acompanhamento ininterrupto de uma sessão de 130 minutos.

L1-R61. Julgue o item.
Na comparação entre dois sistemas de diarização avaliados sobre as mesmas gravações, o sistema que apresenta a maior taxa de erro de diarização (DER), expressa em percentual, é o de melhor desempenho.

L1-R62. Julgue o item.
Um pipeline de diarização de código aberto pode ser executado localmente, sem que o áudio seja enviado a serviço de terceiros, o que é relevante para gravações de reuniões reservadas.

L1-R63. Julgue o item.
Um órgão verifica que o modelo de reconhecimento de fala de um serviço de nuvem oferece diarização no processamento em lote de arquivos. Nessa situação, ele pode concluir, necessariamente, que o mesmo modelo também oferece diarização no reconhecimento em fluxo contínuo (streaming).

L1-R64. Julgue o item.
Na transcrição por canais, quando dois parlamentares falam ao mesmo tempo em microfones gravados em canais distintos, os intervalos de tempo das falas de cada canal se sobrepõem, o que reflete a simultaneidade das falas.

L1-R65. Julgue o item.
Na diarização em tempo real, em que os resultados parciais são revistos à medida que mais áudio é processado, o primeiro resultado parcial de cada fala já traz o rótulo definitivo do falante, de modo que não há resultado parcial com falante ainda desconhecido.

L1-R66. Julgue o item.
Se uma sessão longa for dividida em vários arquivos, processados separadamente por um serviço de diarização, o mesmo rótulo genérico, como Locutor 1, pode designar oradores diferentes em arquivos distintos, independentemente de os arquivos pertencerem à mesma sessão.

L1-R67. Julgue o item.
No Google Cloud Speech-to-Text, a configuração da diarização exige que o cliente informe apenas o número máximo de falantes esperado na gravação, sendo o número mínimo sempre definido pelo próprio serviço a partir do áudio.

L1-R68. Julgue o item.
Considere que um sistema de diarização processe cada hora de áudio em 36 segundos. Nessa hipótese, o processamento de 50 horas de gravações de comissões leva cerca de 30 minutos.

L1-R69. Julgue o item.
Para atribuir as falas aos oradores pelos canais, uma equipe envia à API de transcrição rápida do Azure Speech um arquivo estéreo, com um orador em cada canal, sem configurar o tratamento de canais. Nessa situação, cada canal é transcrito de forma independente, por padrão.

L1-R70. Julgue o item.
Na transcrição de uma reunião de comissão, uma ferramenta de diarização que devolve apenas intervalos de tempo com rótulos de falante não fornece o texto das falas; a transcrição com a indicação de quem falou exige combinar esses intervalos com a saída de um sistema de reconhecimento de fala.

L1-R71. Julgue o item.
Em todos os serviços de diarização, o rótulo de falante é atribuído apenas a trechos inteiros de fala, e nunca a palavras individuais, o que impede representar a troca de orador no meio de uma frase, como em um aparte.

L1-R72. Julgue o item.
Uma equipe constata que um modelo de reconhecimento de fala oferece transcrição em português do Brasil. Nessa situação, isso não garante, por si só, que o mesmo modelo ofereça diarização nesse idioma, pois a relação de idiomas com diarização pode ser mais restrita que a de transcrição.

L1-R73. Julgue o item.
Há ferramentas de diarização de código aberto com pipelines pré-treinados que podem ser ajustados com dados próprios, como gravações de sessões da Casa, para buscar melhor desempenho nesse tipo de áudio.

L1-R74. Julgue o item.
Considere um serviço de diarização que diferencie, no máximo, 30 falantes distintos por arquivo, rotulados de spk_0 a spk_29. Nessa hipótese, uma sessão gravada em um único arquivo, com 45 oradores diferentes, terá todos eles distinguidos, desde que o áudio tenha boa qualidade.

FIM DA PARTE 2/3

=====================================================================
PARTE 3/3 — (d-G) GABARITO COMENTADO
=====================================================================
Legenda: [TS] = troca sutil de um único conceito (em item C, "falsa pegadinha", convenção O-6). VOLÁTIL = gabarito dependente de fato mutável até a reverificação de 4–8/1/2027 (critério da T-89, seção 1), com o risco entre parênteses. REVERIFICAR = conferência de base em 4–8/1/2027 (T-11, parte P2, gce-cqfp), com reabertura obrigatória da URL: "sim (VOLÁTIL)" nos seis itens VOLÁTEIS; "sim (sem efeito de VOLÁTIL)" nos itens que afirmam propriedade documentada de produto ou ferramenta publicada; "não" nos itens de conceito ou de aritmética com valores do enunciado. Todas as páginas foram abertas e lidas em 18/10/2026.

## P2-1.3

L1-R47. C. Multimodal = o mesmo modelo aceita várias modalidades de entrada; o áudio é uma delas, ao lado de texto e, em alguns modelos, imagem e vídeo.
Base: Google Cloud, Gemini Live API overview, tabela "Input modalities" (áudio, imagens/vídeo, texto); AWS, Amazon Nova 2 Sonic: "Cross-modal input support for both audio and text inputs within the same conversation". VOLÁTIL: não. REVERIFICAR: não (conceito; as páginas só ilustram).

L1-R48. E [TS]. Receber o áudio como entrada não determina a modalidade de saída. A saída pode ser texto ou áudio; a compreensão de áudio do Google Cloud (Gemini Enterprise Agent Platform, Audio understanding) devolve texto (resumo, transcrição, tradução), e a saída falada é capacidade adicional dos modelos fala-para-fala.
Base: Google Cloud, Audio understanding ("Speech understanding for: Audio summarization, transcription, and translation"; exemplos com response.text); Gemini Live API overview (tabela "Output modalities": áudio, texto). VOLÁTIL: não. REVERIFICAR: sim (sem efeito de VOLÁTIL).

L1-R49. C [TS]. Falsa pegadinha: soa como erro dizer que o modelo ignora parte do áudio, mas a documentação prevê o truncamento do excedente do limite de tokens; por isso a cobertura do texto deve ser conferida. O item usa "pode" e "convém", sem afirmar que sempre ocorre.
Base: Google Cloud, Audio understanding, passo do console: "If your prompt data exceeds the token limit, the tokens are truncated and aren't included in processing your data." VOLÁTIL (baixo): o comportamento de truncamento descreve o console e pode mudar (por exemplo, rejeição da requisição). REVERIFICAR: sim (VOLÁTIL).

L1-R50. E [TS]. Temperatura zero escolhe sempre o token mais provável, e as respostas ficam "em grande parte determinísticas", mas "ainda é possível uma pequena variação"; não há garantia de textos rigorosamente idênticos.
Base: Google Cloud, Audio understanding, parâmetro Temperature: "A temperature of 0 means that the highest probability tokens are always selected. In this case, responses for a given prompt are mostly deterministic, but a small amount of variation is still possible." VOLÁTIL: não (a propriedade é do método de amostragem). REVERIFICAR: sim (sem efeito de VOLÁTIL).

L1-R51. C. A página limita a compreensão de áudio à fala ("speech only") e adverte que os modelos podem errar ao reconhecer sons que não são fala; aplausos e ruídos do Plenário entram nessa advertência, e as marcações de ruído pedem conferência na revisão.
Base: Google Cloud, Audio understanding, seção "Limitations": "Non-speech sound recognition: The models that support audio might make mistakes recognizing sound that's not speech." VOLÁTIL: não. REVERIFICAR: sim (sem efeito de VOLÁTIL).

L1-R52. E [TS]. O modelo recebe o áudio; a transcrição da fala do usuário é um recurso complementar, ligado por configuração, e não a entrada que o modelo processa.
Base: Google Cloud, Gemini Live API overview: "Audio transcriptions: Provides text transcripts of both user input and model output. For transcription as the end goal rather than as a side channel of a conversation ..."; Microsoft, GPT Realtime API: a transcrição da entrada é ativada em "input_audio_transcription" com um modelo de transcrição (opt-in); AWS, Amazon Nova Sonic: o modelo devolve, entre os eventos de saída, "Text transcriptions of user speech (ASR)". VOLÁTIL: não (conceito comum às três documentações). REVERIFICAR: sim (sem efeito de VOLÁTIL).

L1-R53. C. 12.000 palavras × 100/75 = 16.000 tokens; 16.000 ÷ 8.000 = 2 respostas, no mínimo. Os valores são hipóteses do enunciado.
Base: Google Cloud, Audio understanding, parâmetro Output token limit ("Maximum number of tokens that can be generated in the response ... 100 tokens correspond to roughly 60-80 words"). VOLÁTIL: não (aritmética; os valores não vêm do produto). REVERIFICAR: não.

L1-R54. E [TS]. Segundo a documentação do Google Cloud, para gerar carimbos de tempo precisos em arquivos só de áudio nos modelos Gemini é preciso configurar o parâmetro próprio (audio_timestamp); pedir os tempos na instrução não basta.
Base: Google Cloud, Audio understanding, seção "Limitations": "Audio-only timestamps: To accurately generate timestamps for audio-only files, you must configure the audio_timestamp parameter in generation_config." VOLÁTIL (médio): depende do nome e da exigência de um parâmetro de produto. REVERIFICAR: sim (VOLÁTIL).

L1-R55. C. Modelos de fala conversacionais anunciam ancoragem em dados da organização por RAG e chamada de funções (ferramentas); a combinação permite que a resposta venha de dados consultados.
Base: AWS, Amazon Nova Sonic: "Knowledge grounding with enterprise data using Retrieval Augmented Generation (RAG)" e "Function calling and agentic workflow support"; Nova 2 Sonic (mesmos recursos); Google, Gemini Live API: "Tool use: Integrates tools like function calling and Google Search". VOLÁTIL: não (o item afirma "pode ser combinado", possibilidade comum a três fornecedores). REVERIFICAR: sim (sem efeito de VOLÁTIL).

L1-R56. E [TS]. A documentação indica o streaming para reduzir a percepção de latência de quem aguarda; o processamento total da requisição não diminui por isso.
Base: Google Cloud, Audio understanding: "To reduce the perception of latency to a human audience, stream the response as it's being generated by using the streamGenerateContent method." VOLÁTIL: não. REVERIFICAR: sim (sem efeito de VOLÁTIL).

L1-R57. C. Os modelos conversacionais de fala descrevem a interrupção pelo usuário (barge-in) com manutenção do contexto. O item usa "pode permitir", sem afirmar a presença do recurso em todo modelo.
Base: Google Cloud, Gemini Live API overview: "Barge-in: Users can interrupt the model at any time for responsive interactions"; AWS, Amazon Nova Sonic: "Graceful handling of user interruptions without dropping conversational context". VOLÁTIL (baixo): depende da existência de recurso de serviço gerenciado. REVERIFICAR: sim (VOLÁTIL).

L1-R58. C. Em serviço conversacional de áudio nativo, a conexão bidirecional persistente permite enviar o áudio do usuário em fluxo contínuo enquanto o modelo processa a fala e gera a resposta, sem esperar o conteúdo completo, como ocorre no padrão de requisição e resposta. O item afirma o que a conexão "permite", sem generalizar a todo produto.
Base: AWS, Amazon Nova Sonic, Using the Speech-to-Speech model, "Bidirectional event streaming: Amazon Nova Sonic uses a persistent bidirectional connection that allows simultaneous event streaming in both directions. Unlike traditional request-response patterns, this approach permits the following: Continuous audio streaming from the user to the model; Concurrent speech processing and generation; Real-time model responses without waiting for complete utterances", verificado em 18/10/2026. VOLÁTIL: não (conceito de arquitetura de fala em fluxo). REVERIFICAR: sim (sem efeito de VOLÁTIL).

L1-R59. E [TS]. O áudio enviado compõe o prompt: o limite de áudio por prompt é dado em duração e em tokens. Tokens da resposta são os gerados pelo modelo (o resumo, por exemplo).
Base: Google Cloud, Audio understanding: "Maximum audio length per prompt: Approximately 8.4 hours, or up to 1 million tokens"; amostra de resposta com "promptTokenCount" (entrada) e "candidatesTokenCount" (saída), verificado em 18/10/2026. O item não usa o valor do limite. VOLÁTIL: não. REVERIFICAR: sim (sem efeito de VOLÁTIL).

L1-R60. E [TS]. 16 × 8 = 128 minutos, menos que 130; como 130 ÷ 8 = 16,25 e não existe fração de conexão, são necessárias 17 conexões (arredondamento para cima). Os valores são hipóteses do enunciado.
Base: AWS, Amazon Nova 2 Sonic: "Connection limit of 8 minutes, with connection renewal and session continuation pattern available in code samples" (a renovação com continuação da sessão é o padrão que o enunciado supõe; o valor de 8 minutos é usado só como hipótese). VOLÁTIL: não (aritmética). REVERIFICAR: não.

## P2-1.4

L1-R61. E [TS]. A DER é taxa de erro, expressa em percentual: quanto menor, melhor. O sistema com maior DER nas mesmas gravações é o de pior desempenho.
Base: pyannote.audio, README, seção "Benchmark": "Diarization error rate (in %, the lower, the better)". VOLÁTIL: não. REVERIFICAR: sim (sem efeito de VOLÁTIL).

L1-R62. C. O pipeline de código aberto é executado na máquina do usuário (o exemplo traz o comentário "runs locally"), em oposição ao serviço premium, executado nos servidores do fornecedor; o áudio não precisa sair do ambiente do órgão.
Base: pyannote.audio, README: `output = pipeline("audio.wav", hook=hook) # runs locally` (pipeline de código aberto) e `# runs on pyannoteAI servers` (serviço premium). VOLÁTIL: não (propriedade de ferramenta de código aberto publicada; sem versão no enunciado). REVERIFICAR: sim (sem efeito de VOLÁTIL).

L1-R63. E [TS]. Recursos variam por modelo e por método: no Chirp 3, a diarização consta como disponível só no lote (BatchRecognize), e os carimbos por enunciado só no streaming. Oferta em um modo não permite concluir "necessariamente" a oferta no outro.
Base: Google Cloud, Chirp 3, tabela "Feature support and limitations" (Speaker Diarization: "Available only in Speech.BatchRecognize"; Utterance-level timestamps: "Available only in Speech.StreamingRecognize"); AWS, Amazon Transcribe features (diarização em lote e streaming no serviço padrão, só pós-chamada no Call Analytics). O enunciado não afirma disponibilidade de nenhum produto. VOLÁTIL: não (o gabarito vem do princípio, não de um produto). REVERIFICAR: sim (sem efeito de VOLÁTIL).

L1-R64. C [TS]. Falsa pegadinha: a sobreposição de tempos não é defeito; é o modo de a transcrição por canais registrar a fala simultânea de pessoas em canais distintos.
Base: AWS, Transcribing multi-channel audio: "if a person on one channel speaks at the same time as a person on a separate channel, timestamps for each channel overlap while the individuals are speaking over each other." VOLÁTIL: não. REVERIFICAR: sim (sem efeito de VOLÁTIL).

L1-R65. E [TS]. Na saída de exemplo, os primeiros resultados parciais trazem "Speaker ID=Unknown" e só depois "Guest-1"; o rótulo do falante pode vir depois, com mais áudio processado.
Base: Microsoft, Real-time diarization quickstart: saída de exemplo ("TRANSCRIBING: ... Speaker ID=Unknown", depois "Speaker ID=Guest-1") e propriedade SpeechServiceResponse_DiarizeIntermediateResults. VOLÁTIL (baixo): o item generaliza o comportamento ilustrado em saída de exemplo de um serviço. REVERIFICAR: sim (VOLÁTIL).

L1-R66. C. Os rótulos genéricos são atribuídos pelo serviço a partir do áudio fornecido a cada processamento; arquivos separados podem renumerar os falantes. Por isso o item usa "pode", e não afirma coincidência nem divergência.
Base: Microsoft, Real-time diarization quickstart: "The speaker ID is a generic identifier assigned to each conversation participant by the service during the recognition as different speakers are being identified from the provided audio content"; Google, Detect different speakers: "labels by number the individual voices detected in the audio". VOLÁTIL: não. REVERIFICAR: sim (sem efeito de VOLÁTIL).

L1-R67. E [TS]. A documentação pede os dois valores, mínimo e máximo ("You must set the min_speaker_count and max_speaker_count values according to how many speakers you expect"); não é só o máximo.
Base: Google Cloud, Detect different speakers in an audio recording, seção "Enable speaker diarization in a request". VOLÁTIL (médio): depende de exigência de parâmetro de API de produto. REVERIFICAR: sim (VOLÁTIL).

L1-R68. C. 50 × 36 s = 1.800 s = 30 min. Valores do enunciado são hipótese.
Base: pyannote.audio, README, seção "Benchmark" (velocidade expressa em segundos por hora de áudio: "s per hour of audio"). VOLÁTIL: não (aritmética). REVERIFICAR: não.

L1-R69. E [TS]. Por padrão a API de transcrição rápida mescla todos os canais de entrada em um só antes de transcrever; para transcrever cada canal de forma independente é preciso configurar.
Base: Microsoft, Use the fast transcription API: "By default, the fast transcription API merges all input channels into a single channel and then performs the transcription. If this isn't desirable, channels can be transcribed independently without merging." VOLÁTIL (médio): depende do comportamento padrão de produto. REVERIFICAR: sim (VOLÁTIL).

L1-R70. C. Saídas só com tempo e rótulo (como "start=0.2s stop=1.5s speaker_0") não trazem texto; é preciso alinhá-las, por tempo, à saída do ASR para compor a transcrição com falantes.
Base: pyannote.audio, README: saída de exemplo `start=0.2s stop=1.5s speaker_0`. VOLÁTIL: não (o item descreve uma classe de ferramenta). REVERIFICAR: sim (sem efeito de VOLÁTIL).

L1-R71. E [TS]. Há serviços que marcam cada palavra com o rótulo de falante, o que permite representar a troca de orador no meio de uma frase. "Todos" e "nunca" tornam a afirmação falsa.
Base: Google, Detect different speakers: "The transcription result tags each word with a number assigned to individual speakers"; AWS, Partitioning speakers (diarization): segmentos com itens que trazem "speaker_label". VOLÁTIL: não (basta um serviço documentado com rótulo por palavra; a afirmação "todos... nunca" é refutada por definição). REVERIFICAR: sim (sem efeito de VOLÁTIL).

L1-R72. C [TS]. Falsa pegadinha: parece óbvio que transcrever em pt-BR implicaria diarizar em pt-BR. A documentação mantém listas separadas de idiomas para transcrição e para diarização; no Chirp 3, por exemplo, pt-PT consta na de transcrição e não na de diarização. O item afirma só que a oferta não é garantida "por si só".
Base: Google Cloud, Chirp 3, seções "Language availability" e "Language availability for diarization"; Google, Detect different speakers: "Review the language support page to see if this feature is available for your language." VOLÁTIL: não (o gabarito vem do princípio). REVERIFICAR: sim (sem efeito de VOLÁTIL).

L1-R73. C. O README informa que os modelos e pipelines pré-treinados "can be further finetuned to your own data for even better performance"; o item usa "para buscar melhor desempenho", sem prometer ganho.
Base: pyannote.audio, README, seção inicial: "it comes with state-of-the-art pretrained models and pipelines, that can be further finetuned to your own data for even better performance". VOLÁTIL: não. REVERIFICAR: sim (sem efeito de VOLÁTIL).

L1-R74. E [TS]. O limite do enunciado (30 falantes, de spk_0 a spk_29) é excedido por 45 oradores; a qualidade do áudio não ultrapassa o limite. Os valores são hipóteses; o formato dos rótulos (30 rótulos de spk_0 a spk_29) vem da documentação.
Base: AWS, Partitioning speakers (diarization): "Amazon Transcribe can differentiate between a maximum of 30 unique speakers and labels the text from each unique speaker with a unique value (spk_0 through spk_29)". VOLÁTIL: não (o enunciado fixa o limite como hipótese). REVERIFICAR: não.

## Contagens

| quesito | valor |
|---|---|
| total | 28 (P2-1.3: 14; P2-1.4: 14) |
| C | 14 (1.3: R47, R49, R51, R53, R55, R57, R58; 1.4: R62, R64, R66, R68, R70, R72, R73) |
| E | 14 (1.3: R48, R50, R52, R54, R56, R59, R60; 1.4: R61, R63, R65, R67, R69, R71, R74) |
| % de C | 50,0% (faixa de 40% a 60% e de 11 a 17 C cumprida) |
| [TS] | 17 (60,7%; meta 16): 14 com gabarito E (R48, R50, R52, R54, R56, R59, R60, R61, R63, R65, R67, R69, R71, R74) e 3 com gabarito C (R49, R64, R72) |
| VOLÁTIL | 6 novos: R49 (baixo), R54 (médio), R57 (baixo), R65 (baixo), R67 (médio), R69 (médio); risco alto 0 |
| VOLÁTIL por folha de 20 | P2-1.3: 3/20 = 15%; P2-1.4: 3/20 = 15% (teto 20%) |
| formatos novos | 1.3: D 2, PC 2, SH 3, AP 3, TS 2, NP 2; 1.4: TS 5, AP 4, SH 3, NP 2, D 0, PC 0 |
| REVERIFICAR | sim (VOLÁTIL): R49, R54, R57, R65, R67, R69; sim (sem efeito de VOLÁTIL): R48, R50, R51, R52, R55, R56, R58, R59, R61, R62, R63, R64, R66, R70, R71, R72, R73; não: R47, R53, R60, R68, R74 |
| PENDENTE NORMATIVO | nenhum (nenhuma norma citada) |

Extensão (O-1), contagem por script sobre a Parte 2 desta v2, em palavras do enunciado sem o comando: C média 40,5 (de 30 a 52; maior: L1-R49); E média 39,4 (de 26 a 46; maior: L1-R54). Nenhum C passa de 65 palavras, e os C não são mais longos que os E por mais de 1,1 palavra em média (a onda 1 tinha C 49,6 e E 40,4). Correção de registro do parecer: o v1 trazia E "de 32 a 51" por erro.

## Tabela de proveniência (todas abertas e lidas em 18/10/2026)
| fonte | URL oficial | data da página / verificação | usada em |
|---|---|---|---|
| Google Cloud, Audio understanding (speech only), Gemini Enterprise Agent Platform (antes Vertex AI) | URL citada: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/audio-understanding; URL final após redirecionamento: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/audio-understanding | "Last updated 2026-10-15 UTC"; verificado em 18/10/2026 (HTTP 200) | R48, R49, R50, R51, R53, R54, R56, R59 |
| Google Cloud, Gemini Live API overview, Gemini Enterprise Agent Platform | URL citada: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/live-api; URL final após redirecionamento: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/live-api | "Last updated 2026-10-15 UTC"; verificado em 18/10/2026 (HTTP 200) | R47, R48, R52, R55, R57 |
| AWS, Amazon Nova Sonic (Nova versão 1), Using the Speech-to-Speech model | https://docs.aws.amazon.com/nova/latest/userguide/speech.html (sem redirecionamento) | verificado em 18/10/2026 (HTTP 200) | R52, R55, R57, R58 |
| AWS, Amazon Nova 2 Sonic, Speech-to-Speech | https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html | verificado em 18/10/2026 | R47, R55, R60 |
| Microsoft, Azure OpenAI, GPT Realtime API for speech and audio (Azure Foundry) | URL citada: https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/audio-real-time; URL final após redirecionamento: https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/realtime-audio | metadado ms.date 2026-09-21; verificado em 18/10/2026 (HTTP 200) | R52 |
| Google Cloud, Speech-to-Text, Detect different speakers in an audio recording | https://docs.cloud.google.com/speech-to-text/docs/multiple-voices | "Last updated 2026-10-13 UTC"; verificado em 18/10/2026 | R66, R67, R71, R72 |
| Google Cloud, Speech-to-Text, Chirp 3 | https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3 | "Last updated 2026-10-13 UTC"; verificado em 18/10/2026 | R63, R72 |
| AWS, Amazon Transcribe, Partitioning speakers (diarization) | https://docs.aws.amazon.com/transcribe/latest/dg/diarization.html | verificado em 18/10/2026 | R71, R74 |
| AWS, Amazon Transcribe, Transcribing multi-channel audio | https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html | verificado em 18/10/2026 | R64 |
| AWS, Amazon Transcribe features | https://docs.aws.amazon.com/transcribe/latest/dg/feature-matrix.html | verificado em 18/10/2026 | R63 |
| Microsoft, Azure Speech, Real-time diarization quickstart | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-stt-diarization | metadado ms.date 2026-01-30; verificado em 18/10/2026 | R65, R66 |
| Microsoft, Azure Speech, Use the fast transcription API | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/fast-transcription-create | metadado ms.date 2026-03-10; verificado em 18/10/2026 | R69 |
| pyannote, repositório oficial pyannote/pyannote-audio (README, ramo develop) | https://raw.githubusercontent.com/pyannote/pyannote-audio/develop/README.md | arquivo aberto e lido em 18/10/2026 (HTTP 200); a página github.com não foi usada | R61, R62, R68, R70, R73 |

Fontes não abertas (nenhum item delas entrou): developers.openai.com e platform.openai.com (documentação da API da OpenAI), arxiv.org, huggingface.co (cartões dos modelos do pyannote), ai.google.dev, github.com (páginas), planalto.gov.br e camara.leg.br (nenhuma norma foi usada). Nenhuma base de data anterior foi usada (D-FONTE-DATA-ANTERIOR não acionada).

Nota da R2: as 3 URLs redirecionadas (Google audio-understanding, Google live-api, Microsoft audio-real-time) entram na conferência de base de 4–8/1/2027, reabrindo a URL final.

Dúvidas para a Gerência: (1) R57 e R49 foram marcados VOLÁTIL baixo por depender de existência de recurso e de comportamento de console; se a Gerência preferir tratá-los como propriedade de classe, o teto da folha 1.3 continua cumprido em qualquer das duas leituras. (2) R63, R66, R70, R71 e R72 afirmam princípio e usam produto só como exemplo na justificativa; foram tratados como não VOLÁTEIS, com conferência de base em janeiro. (3) R64, R49 e R72 levam [TS] com gabarito C por convenção (O-6), para atingir 16 [TS]; se a Gerência não aceitar [TS] em C, o mínimo da instrução (16) não se cumpre sem substituir itens.

FIM DA PARTE 3/3
FIM DO LOTE
