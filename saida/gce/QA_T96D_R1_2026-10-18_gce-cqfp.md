# QA_T96D_R1_2026-10-18_gce-cqfp.md — T-96 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L1_reforco_onda2_D_v1.md (gce-cpp), 28 itens AUTORAL, L1-R103 a L1-R130 (P2-1.7: R103–R116; P2-1.8: R117–R130). Rodada 1 de no máximo 2 (D-REFORCO-1/2). Ciclo 2026-10-18 s12c3.
Critérios: linha T-96 (TAREFAS.md); D-REFORCO-1/2; D-FONTE-DATA-ANTERIOR; D-T89-R1-ACEITE (VOLÁTIL = fato mutável — versão, limite, preço, disponibilidade, modelo padrão, existência de recurso —, não o mero nome de produto); D-ONDA2-FILA; T89_reconciliacao, seções 1 e 3 (na 1.8, nenhum VOLÁTIL novo até a folha voltar a ≤ 20%; [TS] ≥ metade + 2); T93_reconciliacao, O-1 a O-8; edital/modulo_RF_IA_P2.md (1.7 "Transcrição em tempo real"; 1.8 "Ferramentas e APIs: Whisper (Open AI), Google Speech-to-text, Azure Speech, AWS Transcribe"); canônicos das folhas no pacote.json v1.9 (L1-Q15 a Q20, L1-R13 a R18).
A gce-cqfp revisa e aponta; não reescreve. Os trechos de texto abaixo são indicações de onde está o defeito; a redação final é da gce-cpp.

## 1. Evidência — reabertura das bases (18/10/2026, curl, todas HTTP 200; texto extraído e conferido)

Reabri as 16 URLs da tabela de proveniência. Nenhuma ficou sem reabrir.

| # | URL | trecho conferido | resultado |
|---|---|---|---|
| 1 | docs.aws.amazon.com/transcribe/latest/dg/streaming.html | "When your audio stream contains no speech, encode and send the same amount of silence. For example, silence for PCM is a stream of zero bytes."; "If possible, record at a sampling rate of 16,000 Hz; this provides the best compromise…"; "most high-end microphones record at 44,100 Hz or 48,000 Hz"; "Streaming can include pre-recorded media…"; "retry with exponential backoff. If you consistently hit this limit, request a service quota increase"; "This is a hard limit that cannot be increased. To continue transcribing, start a new streaming session." | CONFERE (R104, R105, R112, R113, R114) |
| 2 | …/streaming-partial-results.html | "Low stability provides the highest accuracy. High stability transcribes faster, but with slightly lower accuracy." | CONFERE (R103) |
| 3 | …/streaming-setting-up.html | "We strongly recommend using SDKs rather than using HTTP/2 and WebSockets directly. SDKs are the simplest and most reliable method…" | CONFERE (R116) |
| 4 | …/custom-language-models.html | "The best data for training a model are accurate transcripts." — mas a mesma página diz também: "If you have accurate, in-domain transcript text that contains less than 10,000 words and are not getting the desired results, consider augmenting your training data with domain-related written texts" e prevê transcrições como tuning data | CONFERE o trecho citado; a página CONTRADIZ o "somente na falta delas" do R124 (ver 3) |
| 5 | …/vocabulary-filtering.html | "Vocabulary filtering has three display methods: mask, remove, and tag." | CONFERE (R127) |
| 6 | …/custom-vocabulary.html | "Use custom vocabularies to improve transcription accuracy for one or more specific words." | CONFERE (R127) |
| 7 | docs.cloud.google.com/speech-to-text/docs/speech-to-text-requests ("Last updated 2026-10-13 UTC") | síncrono "returns results after all audio has been processed"; streaming "provides interim results while audio is being captured"; "Model selection … you can improve the results … by specifying the source of the original audio" | CONFERE (R107, R130) |
| 8 | docs.cloud.google.com/speech-to-text/docs/best-practices ("Last updated 2026-10-13 UTC") | "Use a lossless codec … FLAC or LINEAR16 is recommended. Using mp3 … may reduce accuracy"; "avoid re-sampling … 8000 Hz, which is the rate that should be sent"; "applying noise-reduction … typically reduces recognition accuracy"; "Do not use automatic gain control (AGC)." | CONFERE (R118, R121, R125) |
| 9 | learn.microsoft.com/…/how-to-recognize-speech ("Last updated on 2026-06-05") | "Recognizing: Signal for events that contain intermediate recognition results. Recognized: … final recognition results, which indicate a successful recognition attempt"; single-shot termina "by listening for silence at the end or until a maximum of 15 seconds of audio is processed"; "Under-segmentation: When users speak for a long time without pauses … a long sequence of text without breaks" | CONFERE (R108, R109, R111) |
| 10 | …/rest-speech-to-text-short ("Last updated on 2026-06-05") | "The REST API for short audio returns only final results. It doesn't provide partial results." | CONFERE (R110) |
| 11 | …/get-started-stt-diarization ("Last updated on 2026-01-31") | "The speaker ID is a generic identifier assigned to each conversation participant by the service during the recognition" | CONFERE (R115) |
| 12 | …/improve-accuracy-phrase-list ("Last updated on 2026-06-29") | "You provide a phrase list just before starting the speech recognition, so you don't need to train a custom model." | CONFERE (R120) |
| 13 | …/batch-transcription ("Last updated on 2026-06-25") | "you submit the audio data, and then retrieve transcription results asynchronously" | CONFERE (R123); a página NÃO menciona "fast transcription" (ver R123) |
| 14 | …/custom-speech-overview ("Last updated on 2026-02-25") | "compare it with a human-generated transcript for the same audio … obtain a word error rate (WER) score. If the WER score is high, training a custom model … is recommended." | CONFERE (R128) |
| 15 | raw.githubusercontent.com/openai/whisper/main/README.md | "four with English-only versions"; ".en models for English-only applications"; "The relative speeds below are measured by transcribing English speech on a A100, and the real-world speed may vary significantly depending on … the language, the speaking speed, and the available hardware." | CONFERE (R117, R129) |
| 16 | raw.githubusercontent.com/openai/whisper/main/model-card.md | "cannot be used for real-time transcription out of the box"; "trained on 680,000 hours … 65% of this data (or 438,000 hours) represents English-language audio and matched English transcripts … the final 17% (or 117,000 hours) represents non-English audio and the corresponding transcript"; hallucination; "may exhibit additional capabilities … speaker diarization but have not been robustly evaluated" | CONFERE (R106, R119, R122, R126) |

As datas "Last updated" declaradas pela produção conferem todas. Nenhuma base de data anterior (D-FONTE-DATA-ANTERIOR não incide). Nenhuma norma citada (sem PENDENTE NORMATIVO). Rede: github.com (página), openai.com e arxiv.org não foram usados nem precisavam ser.

## 2. Veredito por item

| id | folha | gab. | [TS] | formato | VOLÁTIL | veredito | motivo (onde e por quê) |
|---|---|---|---|---|---|---|---|
| R103 | 1.7 | E | sim | PC | n | AJUSTAR | Base é de um fornecedor só (AWS: níveis low/medium/high de partial-result stabilization), mas o enunciado generaliza ("Em serviços … que permitem estabilizar"). No Google, "stability" é escore de resultado intermediário, não nível configurado: o recurso abre por aí. Ancorar no Amazon Transcribe. Gabarito, ponto e [TS] corretos; proximidade com R15 aceita (níveis dentro do streaming × streaming/lote). |
| R104 | 1.7 | C | não | AP | n | AJUSTAR | (a) A cauda "como ocorre nos intervalos de uma sessão suspensa" acrescenta um vínculo que a fonte não traz (O-4/O-5): a boa prática da AWS trata de trechos sem fala dentro do fluxo. Manter fluxo de silêncio durante suspensão longa colide com o limite fixo de duração da sessão (R114), e o C fica contestável. (b) "o cliente deve", sem fornecedor, estende a todos os serviços uma boa prática documentada só para o Amazon Transcribe. Ancorar no Amazon Transcribe e pôr o elemento parlamentar no sujeito (por exemplo, áudio de reunião de comissão), não na cauda. Assim o formato AP e o "independentemente" em C (O-2) continuam. |
| R105 | 1.7 | C | não | NP | n | APROVADO | Literal. Proximidade com R14 aceita (R14 calcula bytes; R105 julga a taxa indicada). |
| R106 | 1.7 | E | sim | SH | n | APROVADO | Literal ("out of the box"); "pode" em E (O-3). Propriedade do artefato publicado: não VOLÁTIL, pelo critério da T-89. |
| R107 | 1.7 | E | sim | TSj | n | APROVADO | Troca de papéis síncrono × streaming; literal. |
| R108 | 1.7 | E | sim | TSj | n | APROVADO | Troca Recognizing × Recognized; literal. |
| R109 | 1.7 | C | não | D | n | APROVADO | Literal; não cobra o número de 15 s. |
| R110 | 1.7 | E | sim | AP | S médio | APROVADO | Literal; VOLÁTIL correto, porque o gabarito depende de uma limitação de serviço que pode mudar. E de 48 palavras, o mais longo (O-1). |
| R111 | 1.7 | E | sim | PC | n | APROVADO | Literal (subsegmentação). Proximidade com Q17 aceita: Q17 julga pausas curtas com endpointing sensível, R111 julga fala longa sem pausa. |
| R112 | 1.7 | C | sim (espelho) | D | n | APROVADO | Literal; restritivo em C (O-7); espelho admitido (O-6). |
| R113 | 1.7 | C | não | SH | n | APROVADO | Literal (primeira das três causas do erro LimitExceededException). Procedimento sem número: não VOLÁTIL. |
| R114 | 1.7 | E | sim | SH | S médio | AJUSTAR | Sem fornecedor no enunciado, o E só vale para o Amazon Transcribe. O "hard limit that cannot be increased" é da AWS, e o gabarito genérico depende de cada serviço. Ancorar no Amazon Transcribe. VOLÁTIL médio correto, porque o gabarito depende de limite de serviço. |
| R115 | 1.7 | E | sim | D | n | APROVADO | Literal; o E resiste mesmo se o recurso mudar. |
| R116 | 1.7 | C | não | AP | n | APROVADO | Literal. |
| R117 | 1.8 | E | sim | SH | n | APROVADO | README: ".en" = English-only. Uma troca. |
| R118 | 1.8 | C | não | PC | n | APROVADO | Literal. |
| R119 | 1.8 | E | sim | NP | n | APROVADO | 680 mil horas, 65% (438 mil) inglês/inglês e 17% (117 mil) não inglês no próprio idioma conferem literalmente no model card. "Maior parte" = 65%, então o E é unívoco. A âncora "De acordo com o model card" é indispensável e deve ficar: o card atribui as 680 mil horas a "the models" sem distinguir large-v3/turbo. Se outra fonte dá outro volume para o large-v3, isso não se verifica aqui (github.com/discussions não abre; [SEM FONTE — não afirmar]), e a âncora neutraliza. Não VOLÁTIL (artefato publicado). REVERIFICAR mantido. |
| R120 | 1.8 | C | sim (espelho) | D | n* | APROVADO (registro D2) | Literal. *Ver seção 4: o C pressupõe que o recurso nomeado exista. |
| R121 | 1.8 | E | sim | SH | n | APROVADO | Literal ("avoid re-sampling … 8000 Hz"). Proximidade com R105 aceita (outra folha, outro ponto). |
| R122 | 1.8 | C | não | AP | n | APROVADO | Literal. A inferência de revisão humana fica fora de remissão ao card (O-4 cumprido). |
| R123 | 1.8 | E | sim | TSj | n | AJUSTAR (só justificativa) | Item e gabarito corretos e literais. A justificativa afirma que a "fast transcription" é o modo síncrono, mas a página citada (batch-transcription) não traz isso: afirmação sem base. Retirar a frase ou citar página própria com "verificado em". Proximidade com R17 aceita (R17: papéis lote × streaming na AWS; R123: caráter assíncrono do lote no Azure). |
| R124 | 1.8 | C | não | AP | n* | REPROVADO | Gabarito C contestável: a mesma página da base refuta o "somente na falta delas se recorre a textos apenas relacionados ao tema". A AWS manda acrescentar textos de domínio relacionado quando as transcrições in-domain existem mas são poucas (menos de 10.000 palavras) e não dão o resultado desejado. Por isso, o restritivo torna o item E pela própria fonte. Segundo defeito: o exemplo "notas taquigráficas revisadas" é discutível como "accurate transcripts". Notas revisadas são texto editado, não literal, e o recurso pode sustentar que não são transcrição precisa do áudio. Na R2: retirar o restritivo e o exemplo, ou trocar o ponto. |
| R125 | 1.8 | E | sim | SH | n | APROVADO | Literal (redução de ruído e AGC: polaridade). Uma troca (pré-processamento). |
| R126 | 1.8 | C | sim (espelho) | D | n | APROVADO | Literal. |
| R127 | 1.8 | E | sim | PC | n | APROVADO | Troca de papéis literal; o E subsiste mesmo que um dos recursos mude. Não VOLÁTIL (ver seção 4). |
| R128 | 1.8 | C | não | SH | n* | APROVADO (registro D2) | Literal. *Ver seção 4. |
| R129 | 1.8 | C | não | AP | n | AJUSTAR | Base literal, mas o enunciado narra o que a equipe fez ("estimou …, ressalvando …") sem predicado avaliativo. Não fica claro se o candidato julga a conduta ou a premissa sobre a tabela, e item narrativo é verdadeiro por estipulação. Explicitar o juízo (por exemplo, "agiu corretamente ao ressalvar…"). Se virar SH, a 1.8 fica com SH 6/20 = 30%, ainda no teto. Proximidade com R18 aceita (coluna de velocidade × parâmetros). |
| R130 | 1.8 | C | não | D | n | APROVADO | Literal; não nomeia modelo. "Model" é parâmetro estrutural da requisição, não recurso avulso: não VOLÁTIL. |

## 3. Taxa

- REPROVADO: 1/28 (R124) = 3,6%. Abaixo do gate de 30%: sem GATE.
- AJUSTAR: 5/28 (R103, R104, R114, R129 no texto; R123 só na justificativa).
- APROVADO: 22/28, dos quais R120 e R128 dependem do registro D2 da seção 4.
- Rodada 2 necessária para R124 (substituição ou reescrita do ponto) e para os 5 ajustes. Nenhum ajuste muda gabarito: R103 E, R104 C, R114 E, R123 E e R129 C ficam como estão. Se R124 for reescrito sem o restritivo e sem o exemplo, ele continua C. Se for trocado por E, a parte D fica com 13 C / 15 E = 46,4%, ainda na faixa.

## 4. VOLÁTIL — resposta ao ponto de julgamento da orquestração

- R110 e R114 (1.7), VOLÁTIL médio: CONCORDO. Os dois gabaritos dependem de limitação ou limite de serviço que pode mudar (critério da T-89: "limite", "disponibilidade"). A 1.7 fica com Q16, R110 e R114 = 3/20 = 15%, abaixo do teto de 20%.
- R127: NÃO VOLÁTIL. O E vem da troca de papéis e continua falso mesmo que um dos recursos mude ou desapareça.
- R120, R124 e R128: ENQUADRAM-SE NA LETRA do critério "existência de recurso" da D-T89-R1-ACEITE. O gabarito C de cada um pressupõe que exista o recurso nomeado do serviço gerenciado: phrase list do Azure Speech, custom language model do Amazon Transcribe, custom speech e o método recomendado. É o mesmo tipo de dependência do precedente L1-Q19 (opção de implantação em contêiner do Azure). O risco de mudança até 4–8/1/2027 é baixo: são recursos centrais, e o ponto é o mecanismo (tempo de execução × treino; dados de treino; WER × transcrição humana), não número, versão ou disponibilidade regional.
- Consequência se forem marcados VOLÁTEIS: a 1.8 vai de 2/20 (Q18, Q19) a 5/20 = 25%. Isso fere o teto de 20% da regra 4 da D-REFORCO-2 e a restrição "nenhum VOLÁTIL novo em 1.8" da T89_reconciliacao, seção 3. Já com R124 retirado ou trocado, R120 e R128 dão 4/20 = 20%, no teto, mas ainda ferem a restrição de nenhum VOLÁTIL novo.
- Posição da QA: o enquadramento é matéria de rótulo (D1/D2 da gce-gerencia, competência ratificada na D-T89-R1-ACEITE). Pelo critério de mecanismo, a não VOLATILIDADE é defensável, por analogia com R17 (divisão estrutural de serviço, não VOLÁTIL) e com a razão declarada na seção 1 da T-89 (não tornar a 1.8 incumprível). Mas a letra ratificada inclui "existência de recurso", então a Gerência deve registrar expressamente que funcionamento documentado de recurso central, sem número, versão, preço ou disponibilidade, é não VOLÁTIL e fica com REVERIFICAR. Sem esse registro, R120 e R128 (e R124, se mantido) precisam ser substituídos por itens cujo ponto não pressuponha recurso de serviço gerenciado, já que a 1.8 não comporta VOLÁTIL novo.
- Demais itens da 1.8 com nome de produto (R117, R119, R122, R126, R129: artefato publicado do Whisper; R118, R121, R125: boa prática; R123: divisão estrutural; R130: parâmetro estrutural): não VOLÁTEIS pelo critério da T-89.

## 5. Conferências de forma

- Cobertura do edital: os 14 itens da 1.7 tratam de transcrição em tempo real (parciais, estabilização, eventos, segmentação, limites, diarização em tempo real, envio de áudio). Os 14 da 1.8 cobrem as quatro ferramentas nomeadas no edital (Whisper 5, Google 4, Azure 3, AWS 2). Nenhuma extrapolação do edital. O peso desigual da AWS na 1.8 (2/14) fica registrado sem efeito.
- Ponto único na folha: conferido contra Q15–Q17 e R13–R15 (1.7) e contra Q18–Q20 e R16–R18 (1.8) no pacote.json v1.9, e entre os 14 novos de cada folha, aos pares. Não há duplicata. As proximidades declaradas (R105×R14, R111×Q17, R103×R15, R129×R18, R129/R119×R11, R123×R17, R112×R17, R121×R105, R124×R12) estão aceitas, cada uma com motivo na tabela.
- Formatos (teto de 30%): 1.7 tem máximo de 4/20 = 20% (D, SH, AP); 1.8 tem SH 5/20 = 25%. Ambas cumprem. Se o R129 virar SH, a 1.8 fica com SH 6/20 = 30%, no teto. Nenhum formato saturado de legado foi usado (a regra de diluição da T-89 não incide em 1.7 e 1.8).
- VOLÁTIL por folha: 1.7 = 3/20 = 15%; 1.8 = 2/20 = 10%, com 0 novos, sujeito à seção 4.
- [TS]: 17/28 = 60,7%, acima da meta de metade + 2 (16), conferido por script. Os 14 E são todos [TS], e em cada um há exatamente um conceito trocado (papéis ou polaridade). R125 junta redução de ruído e AGC numa polaridade só, e R123 desdobra o mesmo conceito: aceitos. Os 3 C [TS] (R112, R120, R126) são espelho (O-6).
- C/E: 14 C / 14 E = 50,0% (conferido), dentro da faixa de 40% a 60%. A faixa da onda inteira se confere com as partes A a C.
- Estilo (O-1 a O-8): média de palavras C 35,4 (30–42) × E 37,2 (31–48), conferida por script, com E mais longo que C. Também presentes: "independentemente" em C (R104), "pode" em E (R106, R110, R114, R117), restritivos em C (R112, R124) e concessiva em E (R103). O-4: a cauda do R104 e o "somente" do R124 são os dois casos que ferem a fidelidade à fonte (ver 2).
- Estrutura: PARTE 1/3 a 3/3, FIM DA PARTE n/3 e FIM DO LOTE presentes. A Parte 2 não tem gabarito, [TS], VOLÁTIL nem REVERIFICAR (conferido por script). Linha 1 no formato. Rótulo AUTORAL e QA PENDENTE declarados. 28 REVERIFICAR, todos com URL reaberta hoje.

## 6. Veredito geral

APROVADO COM RESSALVAS — R1: 1/28 reprovado (3,6%), sem GATE. R2 obrigatória para o R124 e para os ajustes de R103, R104, R114, R123 (justificativa) e R129. Antes da R2, a gce-gerencia registra D1/D2 sobre o enquadramento de R120 e R128 (e do R124, se mantido) no critério de VOLÁTIL (seção 4). Sem esse registro, a 1.8 não fecha sem substituição.

| id | veredito | id | veredito |
|---|---|---|---|
| L1-R103 | AJUSTAR | L1-R117 | APROVADO |
| L1-R104 | AJUSTAR | L1-R118 | APROVADO |
| L1-R105 | APROVADO | L1-R119 | APROVADO |
| L1-R106 | APROVADO | L1-R120 | APROVADO (registro D2) |
| L1-R107 | APROVADO | L1-R121 | APROVADO |
| L1-R108 | APROVADO | L1-R122 | APROVADO |
| L1-R109 | APROVADO | L1-R123 | AJUSTAR (justificativa) |
| L1-R110 | APROVADO (VOLÁTIL médio) | L1-R124 | REPROVADO |
| L1-R111 | APROVADO | L1-R125 | APROVADO |
| L1-R112 | APROVADO | L1-R126 | APROVADO |
| L1-R113 | APROVADO | L1-R127 | APROVADO |
| L1-R114 | AJUSTAR (VOLÁTIL médio) | L1-R128 | APROVADO (registro D2) |
| L1-R115 | APROVADO | L1-R129 | AJUSTAR |
| L1-R116 | APROVADO | L1-R130 | APROVADO |
