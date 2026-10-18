# QA_T96B_R1_2026-10-18_gce-cqfp.md — T-96 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L1_reforco_onda2_B_v1.md (gce-cpp; SHA-256 22100f046d269bdb491ede1a31d83e9566caef83ded7a7db4b92765b34cbe2f9; 28 itens AUTORAL, L1-R47 a L1-R74; folhas P2-1.3 e P2-1.4). Rodada 1 de no máximo 2 (D-REFORCO-1/2).
Critérios: D-REFORCO-1 e 2 (regras 1 a 6), D-FONTE-DATA-ANTERIOR, D-T89-R1-ACEITE (critério de VOLÁTIL, T89_reconciliacao seção 1), D-ONDA2-FILA, T89_reconciliacao seção 3 (onda 2: [TS] ≥ metade + 2; na 1.4, nenhuma "definição" nem "par confundível" novos), T93_reconciliacao O-1 a O-8 (O-6: [TS] em C admitido), edital/modulo_RF_IA_P2.md, pacote.json v1.9 (334 itens; existentes de 1.3 e 1.4 e busca de proximidade em todas as folhas) e canônicos do Lote 1. Coerência de critério com QA_T96A_R1 (parte A).
A QA revisa; não reescreve. Os textos de ajuste abaixo são o texto exato a aplicar; nada mais muda.

## 1. Evidência — URLs reabertas pela QA em 18/10/2026 (curl, todas HTTP 200; 13/13)

| fonte citada | resultado | trechos conferidos (literal) |
|---|---|---|
| docs.cloud.google.com/vertex-ai/…/multimodal/audio-understanding | CONFERE; REDIRECIONA para docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/audio-understanding (título "Audio understanding (speech only) — Gemini Enterprise Agent Platform"; "Last updated 2026-10-15 UTC") | "the tokens are truncated and aren't included in processing your data" (passo do CONSOLE); "mostly deterministic, but a small amount of variation is still possible"; "Non-speech sound recognition: … might make mistakes recognizing sound that's not speech"; "To accurately generate timestamps for audio-only files, you must configure the audio_timestamp parameter in generation_config"; "To reduce the perception of latency to a human audience, stream the response…"; "A top-K of 1 means … (also called greedy decoding)"; "100 tokens correspond to roughly 60-80 words"; "Maximum audio length per prompt: Approximately 8.4 hours, or up to 1 million tokens"; usageMetadata com promptTokenCount/candidatesTokenCount (R48–R51, R53, R54, R56, R58, R59) |
| docs.cloud.google.com/vertex-ai/…/live-api | CONFERE; REDIRECIONA para …/gemini-enterprise-agent-platform/models/live-api ("Last updated 2026-10-15 UTC") | "Input modalities Audio …, images/video …, text"; "Output modalities Audio …, text"; "Barge-in: Users can interrupt the model at any time"; "Tool use: Integrates tools like function calling and Google Search"; "Audio transcriptions … rather than as a side channel of a conversation". Achado: a página usa "Native audio" como rótulo de recurso dos modelos Live conversacionais (com saída em áudio); o modelo gemini-3.5-transcribe-live ("Returns text, not audio") não traz o rótulo (ver R48) |
| docs.aws.amazon.com/nova/latest/userguide/speech.html | CONFERE | "Graceful handling of user interruptions without dropping conversational context"; "Knowledge grounding … (RAG)"; "Function calling and agentic workflow support"; "Text transcriptions of user speech (ASR)" (R52, R55, R57) |
| docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html | CONFERE | "Cross-modal input support for both audio and text inputs"; "Connection limit of 8 minutes, with connection renewal and session continuation pattern" (R47, R55, R60) |
| learn.microsoft.com/…/ai-services/openai/how-to/audio-real-time | CONFERE; REDIRECIONA para learn.microsoft.com/en-us/azure/foundry/openai/how-to/realtime-audio (ms.date 2026-09-21) | "Opt in to transcription of user input audio by using the session's input_audio_transcription property" (R52) |
| docs.cloud.google.com/speech-to-text/docs/multiple-voices ("Last updated 2026-10-13 UTC") | CONFERE | "You must set the min_speaker_count and max_speaker_count values"; "tags each word with a number assigned to individual speakers"; "labels by number the individual voices detected in the audio"; "Review the language support page…" (R66, R67, R71, R72) |
| docs.cloud.google.com/speech-to-text/docs/models/chirp-3 ("Last updated 2026-10-13 UTC") | CONFERE | Speaker Diarization "Available only in Speech.BatchRecognize"; Utterance-level timestamps "Available only in Speech.StreamingRecognize"; lista de diarização com pt-BR e sem pt-PT; pt-PT na lista de transcrição (R63, R72) |
| docs.aws.amazon.com/transcribe/latest/dg/diarization.html | CONFERE | "a maximum of 30 unique speakers … (spk_0 through spk_29)"; items com "speaker_label" (R71, R74) |
| docs.aws.amazon.com/transcribe/latest/dg/channel-id.html | CONFERE | "timestamps for each channel overlap while the individuals are speaking over each other" (R64) |
| docs.aws.amazon.com/transcribe/latest/dg/feature-matrix.html | CONFERE | "Speaker diarization batch, streaming | batch, streaming | post-call" (R63) |
| learn.microsoft.com/…/speech-service/get-started-stt-diarization (ms.date 2026-01-30) | CONFERE | saída "Speaker ID=Unknown" nos primeiros TRANSCRIBING, depois "Guest-1"; "generic identifier assigned … from the provided audio content"; SpeechServiceResponse_DiarizeIntermediateResults (R65, R66) |
| learn.microsoft.com/…/speech-service/fast-transcription-create (ms.date 2026-03-10) | CONFERE | "By default, the fast transcription API merges all input channels into a single channel…" (R69) |
| raw.githubusercontent.com/pyannote/pyannote-audio/develop/README.md | CONFERE | l. 10 "pretrained models and pipelines, that can be further finetuned to your own data for even better performance"; l. 46 "# runs locally"; l. 70 "# runs on pyannoteAI servers"; l. 51 "start=0.2s stop=1.5s speaker_0"; l. 100 "Diarization error rate (in %, the lower, the better)"; l. 107–108 "31s/37s per hour of audio" (R61, R62, R68, R70, R73) |

Bases não reabertas: nenhuma. Nenhuma base de data anterior (D-FONTE-DATA-ANTERIOR não aplicável). Nenhuma norma citada: sem PENDENTE NORMATIVO.
Registro de proveniência (sem efeito de veredito): três URLs citadas redirecionam (Vertex AI → Gemini Enterprise Agent Platform; Azure OpenAI → Azure Foundry). O conteúdo confere após o redirecionamento; a tabela de proveniência deve registrar a URL final, e a justificativa de R48 ("compreensão de áudio do Vertex") deve nomear a página pelo título atual. Os três casos entram na conferência de base de 4–8/1/2027.

## 2. Pontos de julgamento levantados pela orquestração e pela produtora

1. pyannote (R61, R62, R68, R70, R73). Fonte: o README do repositório oficial pyannote/pyannote-audio, lido em raw.githubusercontent.com, é documentação do próprio mantenedor do toolkit. Vale como "documento oficial / documentação do fornecedor" na regra 2 da D-REFORCO-2, pelo mesmo critério já aplicado ao Whisper (T-89) e a fairseq, NeMo e ESPnet (QA_T96A, seção 2). Não é espelho de terceiro. Escopo: o conceito julgado (DER, execução local, forma da saída, ajuste fino de pipeline) está dentro do 1.4. A ferramenta, porém, não consta do edital: o 1.4 não nomeia ferramentas, e o 1.8 traz lista fechada (Whisper, Google, Azure, AWS). Nomeá-la no enunciado (R62, R73) é extrapolação evitável, punível em recurso. Por isso, AJUSTAR para retirar o nome do enunciado e mantê-lo só na base. R61, R68 e R70 não nomeiam a ferramenta: sem ajuste por este motivo. Registros: (a) 5 das 14 bases da 1.4 vêm de um único README (36%), o que não viola regra mas concentra o risco de reverificação; (b) o ramo "develop" é mutável: a reverificação de 4–8/1/2027 deve reabrir o arquivo e, se possível, a Gerência registra o commit ou a tag lida.
2. VOLÁTIL (Dúvidas 1 e 2). R54, R67 e R69 estão corretos como VOLÁTEIS (risco médio): o gabarito depende de parâmetro ou de padrão de produto nomeado. R49 baixo é aceitável, porque a base é comportamento de console de um fornecedor. R57 é genérico ("pode permitir") e, pelo critério da T-89, poderia ser não VOLÁTIL, mas a marcação conservadora cabe no teto. R65 e R71 usam a mesma lógica (afirmação absoluta refutada por um caso documentado) e receberam tratamento diferente (R65 VOLÁTIL, R71 não): registro de coerência para D1 da Gerência. Em qualquer leitura, as folhas ficam em 3/20 ou menos (≤ 15%). Concordo com R63, R66, R70, R71 e R72 não VOLÁTEIS, com conferência de base em janeiro.
3. [TS] em C (Dúvida 3). R49, R64 e R72 seguem a convenção O-6, admitida. Conferi os 17 um a um: os 14 em E trocam exatamente um conceito (R48 entrada/saída; R50 reduz/elimina; R52 canal lateral/entrada; R54 exige/não exige configuração; R56 percepção/tempo total; R59 prompt/resposta; R60 arredondamento; R61 menor/maior é melhor; R63 "necessariamente"; R65 desconhecido/definitivo; R67 mínimo e máximo/só máximo; R69 mesclado/independente; R71 por palavra/só por trecho; R74 limite/qualidade). Os 3 em C são falsas pegadinhas coerentes.
4. Proximidade não registrada pela produtora: R62 (1.4, execução local sem envio a terceiros) × L1-Q20 (1.8, custódia do áudio em modelo local × nuvem) e L1-Q18 (1.8, Whisper executável localmente). As folhas são diferentes, então a regra 1 não é violada, mas o ponto é quase o mesmo do Q20. Fica registrado para D1, como no precedente R12 × L1C-Q21.

## 3. Veredito por item

| id | folha | gab. | [TS] | formato | VOL | veredito | motivo |
|---|---|---|---|---|---|---|---|
| L1-R47 | 1.3 | C | não | D | n | APROVADO | literal Live API (modalidades de entrada) e Nova 2 Sonic; distinto de Q05 (o que "nativo" qualifica); D em 1.3 permitido |
| L1-R48 | 1.3 | E | sim | PC | n | AJUSTAR (A-1) | a cláusula "pois o termo nativo se refere à saída falada…" põe o gabarito na DEFINIÇÃO de "nativo", que nenhuma base traz literalmente; a própria Live API usa "Native audio" como rótulo dos modelos conversacionais com saída em áudio, o que expõe o E a recurso. O ponto (receber áudio não obriga resposta em áudio) se sustenta sem definir o termo |
| L1-R49 | 1.3 | C | sim (O-6) | SH | S baixo | APROVADO | literal, mas o trecho é do passo do console; "pode" e "convém" seguram o C. Registro: base de console generalizada para "requisição"; manter VOLÁTIL e REVERIFICAR |
| L1-R50 | 1.3 | E | sim | SH | n | APROVADO | literal ("small amount of variation is still possible"); aplicação à transcrição repetida mantém o item na folha; distinto de L4-04 (P1-5.1) |
| L1-R51 | 1.3 | C | não | AP | n | APROVADO | literal "Limitations"; contexto do Plenário |
| L1-R52 | 1.3 | E | sim | TS | n | APROVADO | três fornecedores literais (canal lateral; opt-in com modelo de transcrição; evento ASR de saída) |
| L1-R53 | 1.3 | C | não | NP | n | APROVADO | 12.000 × 100/75 = 16.000 tokens > 8.000, portanto pelo menos 2 respostas; 75 palavras dentro da faixa de 60–80 da base |
| L1-R54 | 1.3 | E | sim | SH | S médio | AJUSTAR (A-2) | a base exige configuração para gerar carimbos "accurately" em um produto (Gemini/Google Cloud); o item diz "um LLM de áudio nativo" qualquer e "carimbos de tempo" sem "precisos". Com "pode obtê-los", o E é contestável (o modelo pode emitir tempos imprecisos por instrução, e outro fornecedor pode não exigir parâmetro). Ambiguidade e generalização de regra de produto |
| L1-R55 | 1.3 | C | não | AP | n | APROVADO | literal Nova Sonic, Nova 2 Sonic e Live API; distinto dos itens de RAG de P1-5 (L4-06, L4-16, 4C-09) |
| L1-R56 | 1.3 | E | sim | TS | n | APROVADO | literal ("reduce the perception of latency"); a inferência "não reduz o tempo total" é conceito, não extrapolação |
| L1-R57 | 1.3 | C | não | AP | S baixo | APROVADO | literal Live API e Nova Sonic; "pode permitir". VOLÁTIL conservador (seção 2) |
| L1-R58 | 1.3 | C | não | D | n | REPROVADO | escopo da folha: o ponto (top-K = 1 = decodificação gulosa) é parâmetro genérico de amostragem de qualquer LLM, e o enunciado não tem nada de áudio ("Em modelos de linguagem que geram o texto token a token"). O tema é de P1-5.1 (IA generativa; cf. L4-04, 4C-04), não de 1.3. Mesmo critério de escopo de QA_T96A (R40, R43, R44) |
| L1-R59 | 1.3 | E | sim | PC | n | APROVADO | "per prompt" e promptTokenCount/candidatesTokenCount literais; aplicação a áudio própria da folha |
| L1-R60 | 1.3 | E | sim | NP | n | AJUSTAR (A-3) | "exige, no mínimo, 16 conexões" é ambíguo: como 17 são necessárias, a leitura "exige pelo menos 16" também é verdadeira (17 ≥ 16). Gabarito E exposto a recurso; reescrever sem o "no mínimo" |
| L1-R61 | 1.4 | E | sim | TS | n | APROVADO | literal README l. 100; distinto de Q09 (composição da DER) |
| L1-R62 | 1.4 | C | não | AP | n | AJUSTAR (A-4) | nome de ferramenta fora do edital no enunciado (seção 2.1). Registro: proximidade com L1-Q20 e L1-Q18 (1.8) para D1 (seção 2.4) |
| L1-R63 | 1.4 | E | sim | SH | n | APROVADO | literal Chirp 3 e matriz AWS; princípio não VOLÁTIL. Registro de estilo (opcional): "ele pode concluir, necessariamente," fica melhor como "é correto concluir que, necessariamente," |
| L1-R64 | 1.4 | C | sim (O-6) | TS | n | APROVADO | literal AWS channel-id; distinto de R07 (canal × diarização) e de R71 |
| L1-R65 | 1.4 | E | sim | TS | S baixo | APROVADO | saída de exemplo literal ("Speaker ID=Unknown" e depois "Guest-1") e nota "Without intermediate diarization results … always 'Unknown'". VOLÁTIL: coerência com R71 para D1 (seção 2.2) |
| L1-R66 | 1.4 | C | não | AP | n | APROVADO | literal MS e Google; "pode" e "independentemente" (O-2); distinto de Q07 |
| L1-R67 | 1.4 | E | sim | TS | S médio | APROVADO | literal ("You must set the min_speaker_count and max_speaker_count"); VOLÁTIL correto (parâmetro de produto nomeado) |
| L1-R68 | 1.4 | C | não | NP | n | APROVADO | 50 × 36 s = 1.800 s = 30 min; valores hipotéticos (README traz 31 e 37 s/h). Registro: baixa discriminação, porque o item é aritmética com tema de diarização apenas no enunciado; a base só dá a unidade |
| L1-R69 | 1.4 | E | sim | SH | S médio | APROVADO | literal ("By default … merges all input channels"); VOLÁTIL correto (padrão de produto) |
| L1-R70 | 1.4 | C | não | AP | n | AJUSTAR (A-5) | gabarito e base corretos, mas o formato declarado é "aplicação parlamentar" e o enunciado não tem nenhum contexto parlamentar. Sem o ajuste, o item seria classificado como definição, vedada na 1.4 nesta onda (T89, seção 3) |
| L1-R71 | 1.4 | E | sim | TS | n | APROVADO | literal Google ("tags each word") e AWS (speaker_label por item); "todos… nunca" |
| L1-R72 | 1.4 | C | sim (O-6) | SH | n | APROVADO | conferido: pt-PT na lista de transcrição e fora da de diarização; pt-BR nas duas; "por si só" segura o C |
| L1-R73 | 1.4 | C | não | AP | n | AJUSTAR (A-6) | literal README l. 10; nome de ferramenta fora do edital no enunciado (seção 2.1) |
| L1-R74 | 1.4 | E | sim | NP | n | APROVADO | limite fixado como hipótese; formato dos rótulos literal AWS |

## 4. Ajustes (texto exato)

A-1 (L1-R48, Parte 2). Substituir o enunciado inteiro por
"Um LLM multimodal que recebe o áudio diretamente como modalidade de entrada só é capaz de devolver a resposta em áudio sintetizado, e não em texto."
Parte 3: substituir a primeira frase ""Nativo" qualifica a entrada: a fala é modalidade do próprio modelo." por "Receber o áudio como entrada não determina a modalidade de saída."; substituir "a compreensão de áudio do Vertex devolve texto" por "a compreensão de áudio do Google Cloud (Gemini Enterprise Agent Platform, Audio understanding) devolve texto". Mapa: o ponto passa a "Receber áudio como entrada não obriga a resposta em áudio; a saída pode ser texto ou áudio". Gabarito E, [TS] e formato PC mantidos.

A-2 (L1-R54, Parte 2). Substituir o enunciado inteiro por
"Segundo a documentação do Google Cloud para os modelos Gemini, uma equipe que deseje carimbos de tempo precisos na transcrição de um arquivo que contenha somente áudio pode obtê-los apenas pedindo os tempos na instrução em texto, ainda que não faça nenhuma configuração específica de geração."
Parte 3: substituir "Para gerar carimbos de tempo corretos em arquivos só de áudio é preciso configurar o parâmetro próprio (audio_timestamp)" por "Segundo a documentação do Google Cloud, para gerar carimbos de tempo precisos em arquivos só de áudio nos modelos Gemini é preciso configurar o parâmetro próprio (audio_timestamp)". Mapa: o ponto passa a "Nos modelos Gemini (Google Cloud), carimbos de tempo precisos em arquivo só de áudio exigem configurar o parâmetro de geração; pedir na instrução não basta". Gabarito E, [TS], VOLÁTIL (médio) e concessiva em E (O-8) mantidos.

A-3 (L1-R60, Parte 2). Substituir a última frase "Nessa hipótese, o acompanhamento ininterrupto de uma sessão de 130 minutos exige, no mínimo, 16 conexões consecutivas." por
"Nessa hipótese, 16 conexões consecutivas bastam para o acompanhamento ininterrupto de uma sessão de 130 minutos."
Parte 3: substituir "130 ÷ 8 = 16,25; como não existe fração de conexão, são necessárias 17 conexões, no mínimo (arredondamento para cima)." por "16 × 8 = 128 minutos, menos que 130; como 130 ÷ 8 = 16,25 e não existe fração de conexão, são necessárias 17 conexões (arredondamento para cima)." Gabarito E e [TS] mantidos.

A-4 (L1-R62, Parte 2). Substituir o enunciado inteiro por
"Um pipeline de diarização de código aberto pode ser executado localmente, sem que o áudio seja enviado a serviço de terceiros, o que é relevante para gravações de reuniões reservadas."
Parte 3 e base: sem mudança (o README do pyannote.audio continua como exemplo na justificativa). Gabarito C mantido.

A-5 (L1-R70, Parte 2). Substituir o enunciado inteiro por
"Na transcrição de uma reunião de comissão, uma ferramenta de diarização que devolve apenas intervalos de tempo com rótulos de falante não fornece o texto das falas; a transcrição com a indicação de quem falou exige combinar esses intervalos com a saída de um sistema de reconhecimento de fala."
Parte 3: sem mudança. Gabarito C e formato AP mantidos (47 palavras; abaixo de 65, O-1).

A-6 (L1-R73, Parte 2). Substituir o enunciado inteiro por
"Há ferramentas de diarização de código aberto com pipelines pré-treinados que podem ser ajustados com dados próprios, como gravações de sessões da Casa, para buscar melhor desempenho nesse tipo de áudio."
Parte 3 e base: sem mudança. Gabarito C mantido.

Correção de registro (Parte 3, seção "Contagens", linha de extensão): "E média 39,9 (de 32 a 51)" está errado. O maior E tem 46 palavras (R52); o item de 51 palavras é R53, que é C. Conferido por script: C 39,4 (30–52) e E 39,9 (32–46).

## 5. Tetos, gabarito, [TS], estilo e estrutura

- Estrutura: PARTE 1/3 a 3/3, FIM DA PARTE e FIM DO LOTE presentes; Parte 2 com 28 ids, comando "Julgue o item." e 0 ocorrências de gabarito, [TS], VOLÁTIL ou REVERIFICAR; Parte 3 com 28 gabaritos. Cabeçalho na forma do CLAUDE.md, rótulo AUTORAL e QA PENDENTE declarados. CONFERE.
- Ponto único na folha: conferido contra os 6 existentes de cada folha (pacote v1.9: Q05, Q06, L1C-Q25, L1C-Q26, R05, R06; Q07, Q08, Q09, L1C-Q27, L1C-Q28, R07) e entre os novos. Nenhuma duplicata. As proximidades declaradas pela produtora procedem. A proximidade acrescida (R62 × Q20/Q18) está na seção 2.4.
- Gabarito: 14 C / 14 E (50%) como entregue. Sem R58 (C): 13 C / 14 E (48,1%), na faixa de 40–60%. A substituição em 1.3 deve ser preferencialmente C, para voltar a 7/7 na folha.
- [TS]: 17/28 (60,7%; meta 16) como entregue. R58 não tem [TS], então ficam 17/27, com a meta cumprida.
- Formato 1.3 (20, como entregue): D 3, TS 3, SH 4, NP 3, PC 3, AP 4, com máximo de 20%. Sem R58, D fica em 2. CONFERE. A substituição pode ser de qualquer formato, desde que nenhum passe de 6.
- Formato 1.4 (20): TS 5, AP 5, SH 4, NP 2, D 2, PC 2, com máximo de 25%. Nenhum D ou PC novo, desde que se aplique o A-5 (R70). CONFERE com o ajuste.
- VOLÁTIL: 1.3 tem 3/20 e 1.4 tem 3/20 (15%), sem nenhum de risco alto. CONFERE.
- Estilo (O-1 a O-8): extensão equilibrada (C 39,4 × E 39,9, sem C acima de 65 palavras); O-2 cumprido (R66); O-3, O-7 e O-8 cumpridos; O-4 e O-5 conferidos; O-6 conforme a seção 2.3. CONFERE.
- Normativo: nenhuma lei citada. Sem PENDENTE NORMATIVO.

## 6. Taxa e veredito

Reprovados: 1/28 = 3,6% (R58), abaixo do gate de 30%. AJUSTAR: 6 (R48, R54, R60, R62, R70, R73). Aprovados sem ajuste: 21.
Veredito geral: APROVADO COM RESSALVAS. Para a R2: aplicar A-1 a A-6 literalmente e a correção de registro da extensão; substituir R58 por um item novo de 1.3, preferencialmente C, com ponto próprio de áudio nativo, distinto dos 19 restantes e de P1-5.1, e base aberta e literal; atualizar na proveniência as 3 URLs redirecionadas.
Registros para D1 da Gerência: coerência VOLÁTIL entre R65 e R71 e VOLÁTIL conservador em R57; R62 × L1-Q20/Q18; concentração no README do pyannote (5/14, ramo develop); R49 com base de console; R68 com baixa discriminação; estilo opcional em R63.

## 7. Tabela final (28 itens)

| id | veredito | id | veredito |
|---|---|---|---|
| L1-R47 | APROVADO | L1-R61 | APROVADO |
| L1-R48 | AJUSTAR (A-1) | L1-R62 | AJUSTAR (A-4) |
| L1-R49 | APROVADO | L1-R63 | APROVADO |
| L1-R50 | APROVADO | L1-R64 | APROVADO |
| L1-R51 | APROVADO | L1-R65 | APROVADO |
| L1-R52 | APROVADO | L1-R66 | APROVADO |
| L1-R53 | APROVADO | L1-R67 | APROVADO |
| L1-R54 | AJUSTAR (A-2) | L1-R68 | APROVADO |
| L1-R55 | APROVADO | L1-R69 | APROVADO |
| L1-R56 | APROVADO | L1-R70 | AJUSTAR (A-5) |
| L1-R57 | APROVADO | L1-R71 | APROVADO |
| L1-R58 | REPROVADO | L1-R72 | APROVADO |
| L1-R59 | APROVADO | L1-R73 | AJUSTAR (A-6) |
| L1-R60 | AJUSTAR (A-3) | L1-R74 | APROVADO |
