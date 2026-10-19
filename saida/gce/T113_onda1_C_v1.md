# T113_onda1_C_v1.md — T-113 onda 1 (F1), parte C: P2-1.7, P2-1.8 e P2-2.1 — 2026-10-18 — gerado por gce-cpp

Versão v1 (produção). Trinta itens AUTORAL novos: L1-R192 a L1-R201 (P2-1.7), L1-R202 a L1-R211 (P2-1.8) e L2-R133 a L2-R142 (P2-2.1), com os ids e as cotas de saida/gce/V15_BAEF_D1_GCE_2026-10-18.md (seção 4) e de saida/pacote/V15_BAE_D1_GBQ_2026-10-18.md (seção 4.2). Nenhum item existente foi alterado. Estado de QA: QA PENDENTE em todos (D-QA-PENDENTE); não entram em simulado antes da QA da gce-cqfp.

Lido antes: CLAUDE.md; regras/proveniencia.md; regras/estilo_banca.md; regras/padrao_resposta_cebraspe.md (formato de item); edital/modulo_RF_IA_P2.md (1.7 "Transcrição em tempo real"; 1.8 "Ferramentas e APIs: Whisper (Open AI), Google Speech-to-text, Azure Speech, AWS Transcribe"; 2.1 "Diferença entre transcrição automática, degravação e revisão humana"); ordens/ORDEM_V15_F_BANCO40.md; D-REFORCO-2 (regras 1 a 6), D-FONTE-DATA-ANTERIOR e D-ADERENCIA em DECISOES.md; as duas D1 acima (seção 4); saida/pacote/pacote.json v1.11 (as 60 linhas das três folhas, com enunciado e justificativa); L1_reforco_onda1_v2.md, L1_reforco_onda2_D_v3.md, L2_reforco_onda1_v3.md e L2_reforco_onda3_A_v3.md (mapas e formatos dos existentes); L3_reforco_onda4_A_v3.md (formato do arquivo).

Bases: todas as páginas abaixo foram abertas e lidas em 18/10/2026 (HTTP 200, curl com User-Agent de navegador) e cada trecho entre aspas das justificativas foi conferido por script contra o texto baixado nesse dia (normalizando espaços e aspas); nenhuma data de verificação anterior foi usada (D-FONTE-DATA-ANTERIOR não é invocada). As páginas do Google e da Microsoft trazem a data "Last updated" registrada na tabela; as páginas da AWS e os arquivos do repositório do Whisper não exibem data de atualização; as duas reportagens da Agência Senado trazem a data de publicação. Nenhum item cita lei, regimento ou ato normativo (sem remessa ao qa-normativo nesta parte). Nenhum item usa número de versão, preço, nome de modelo de API, limite numérico de cota ou prazo de serviço; os números que aparecem são aritmética sobre regra documentada (L1-R193, L2-R138), o dado de uma tabela de artefato publicado (L1-R204) ou a contagem de profissionais de uma reportagem (L2-R138).

Aderência: DIRETA em todos os 30 (regra 4 da seção 4.1 da D1 da GCE). Em 2.1, nenhum item usa o Ato da Mesa nº 251/2026 nem o RICD (o legado dessas bases é PARCIAL); a base é documentação de fornecedor sobre a relação entre o texto automático, a referência e a correção humana, e reportagens da Agência Senado sobre taquigrafia, degravação, revisão e montagem. Nenhuma folha tem mais de 5 de 10 itens novos do mesmo fornecedor ou fonte (1.7: AWS 5, Google 4, Azure 1; 1.8: Whisper 4, AWS 2, Google 2, Azure 2; 2.1: Google 3, Agência Senado 5, Azure 2).

Verificação de não repetição (script próprio, somente leitura): sequências de 6 palavras do enunciado e da justificativa de cada item contra os 560 itens do pacote.json v1.11 (enunciado e justificativa), 61 arquivos saida/gce/*reforco*.md, saida/gce/GCE_Lote*.md, saida/gcb/*reforco*.md e saida/gce/T113_onda1_*.md já gravados por outras produtoras, e as 153 linhas de banco/banco.csv; e trechos literais de 30 ou mais caracteres das bases (em inglês e português) contra o mesmo corpus. Resultado: nenhum trecho-base literal já usado; as únicas coincidências de 6 palavras são fórmulas de remissão ("segundo a documentação do Google Cloud Speech-to-Text", "ao vivo de uma sessão com o Azure Speech", "segundo a referência da API"). Pontos conferidos item a item por leitura contra os 20 existentes de cada folha e entre os 10 novos de cada folha; um ponto candidato foi descartado por gemelidade antes da escrita (ground truth como transcrição humana, que já é o L2-R103 de 2.7; realce de palavras instáveis, que é o L1-R79; semântica de segmentação, que é o L1-R86; tempos de início e fim para sincronizar com vídeo, que é o L1-R02; confiança por palavra, que é o L2-R13; janela de 30 segundos do Whisper, que é o L1-R04; vozes simultâneas e canais do Google, que são o L1-R29 e o L1-R91; textos repetitivos do Whisper, que é o L1-R38; supervisão humana do Azure, que é o L2-R33; exatidão no divisor do WER, que é o L1C-Q22).

Legenda dos formatos: D = definição; TSj = troca de sujeito; SH = situação hipotética; NP = número ou prazo; PC = par confundível; AP = aplicação parlamentar. Critério de classificação: o da T91_reconciliacao, seção 3.1 (o formato segue a construção do ponto, e não o gabarito; o formato de um item C é o da sua contraparte E). Legenda do [TS]: troca sutil de um único conceito.

Contagens da parte:
- Total: 30 itens. C = 15 (R192, R194, R196, R198, R200, R202, R204, R206, R208, R210, R133, R135, R137, R139, R141); E = 15. Gabarito C da parte: 15/30 = 50,0% (faixa de 12 a 18 e de 40% a 60%, regra 5 da D-REFORCO-2).
- P2-1.7: 10 novos, 5 C / 5 E (faixa de 4 a 6 C).
- P2-1.8: 10 novos, 5 C / 5 E (faixa de 4 a 6 C).
- P2-2.1: 10 novos, 5 C / 5 E (faixa de 4 a 6 C).
- [TS]: 15/30 (R193, R195, R197, R199, R201, R203, R205, R207, R209, R211, R134, R136, R138, R140, R142), todos em itens E; cada um troca um único conceito (ver a justificativa). Os itens C não levam [TS].
- VOLÁTIL novos: 7, todos de risco baixo e nenhum de risco alto (L1-R194, L1-R200, L1-R201, L2-R134, L2-R138, L2-R141, L2-R142). Por folha depois da onda: 1.7 = 3 existentes + 3 novos = 6/30 = 20,0%; 1.8 = 2 + 0 = 2/30 = 6,7%; 2.1 = 2 + 4 = 6/30 = 20,0% (teto de 20%; tetos de novos da D1: 1.7 = 3, 1.8 = 4, 2.1 = 4). Todos levam REVERIFICAR em 4–8/1/2027 e são inaptos a simulado final até lá.
- Aderência: direta nos 30; parcial 0.
- Fornecedor por folha (novos): 1.7 = AWS 5 (R192, R193, R195, R198, R201), Google 4 (R194, R196, R197, R199), Azure 1 (R200); 1.8 = Whisper 4, AWS 2, Google 2, Azure 2; 2.1 = Google 3 (R133, R139, R140), Agência Senado 5 (R135, R137, R138, R141, R142), Azure 2 (R134, R136); nenhuma folha passa de 5 de 10 do mesmo fornecedor.

Tabelas "formato × existentes × novos × total" (teto de 30% de um formato = 9 de 30):

**P2-1.7** (20 existentes + 10 novos = 30)

| formato | existentes | novos | total | % |
|---|---|---|---|---|
| definição (D) | 4 | 1 | 5 | 16,7% |
| troca de sujeito (TSj) | 3 | 1 | 4 | 13,3% |
| situação hipotética (SH) | 4 | 3 | 7 | 23,3% |
| número ou prazo (NP) | 2 | 1 | 3 | 10,0% |
| par confundível (PC) | 3 | 1 | 4 | 13,3% |
| aplicação parlamentar (AP) | 4 | 3 | 7 | 23,3% |
| soma | 20 | 10 | 30 | 100% |

Maior formato: 7/30 = 23,3% (teto de 30% cumprido).

**P2-1.8** (20 existentes + 10 novos = 30)

| formato | existentes | novos | total | % |
|---|---|---|---|---|
| definição (D) | 4 | 2 | 6 | 20,0% |
| troca de sujeito (TSj) | 2 | 1 | 3 | 10,0% |
| situação hipotética (SH) | 6 | 2 | 8 | 26,7% |
| número ou prazo (NP) | 2 | 1 | 3 | 10,0% |
| par confundível (PC) | 3 | 2 | 5 | 16,7% |
| aplicação parlamentar (AP) | 3 | 2 | 5 | 16,7% |
| soma | 20 | 10 | 30 | 100% |

Maior formato: 8/30 = 26,7% (teto de 30% cumprido).

**P2-2.1** (20 existentes + 10 novos = 30)

| formato | existentes | novos | total | % |
|---|---|---|---|---|
| definição (D) | 4 | 3 | 7 | 23,3% |
| troca de sujeito (TSj) | 5 | 1 | 6 | 20,0% |
| situação hipotética (SH) | 5 | 2 | 7 | 23,3% |
| número ou prazo (NP) | 0 | 1 | 1 | 3,3% |
| par confundível (PC) | 4 | 0 | 4 | 13,3% |
| aplicação parlamentar (AP) | 2 | 3 | 5 | 16,7% |
| soma | 20 | 10 | 30 | 100% |

Maior formato: 7/30 = 23,3% (teto de 30% cumprido).

Classificação dos existentes (pelo mapa dos arquivos de reforço e, nos legados Q, pelo mesmo critério): 1.7 = D (Q15, R109, R112, R115), TSj (R13, R107, R108), SH (Q17, R106, R113, R114), NP (R14, R105), PC (Q16, R103, R111), AP (R15, R104, R110, R116); 1.8 = D (Q19, R120, R126, R130), TSj (R17, R123), SH (R16, R117, R121, R125, R128, R129), NP (R18, R119), PC (Q18, R118, R127), AP (Q20, R122, R124); 2.1 = D (Q04, R22, R26, R31), TSj (Q01, R20, R21, R25, R29), SH (R01, R19, R23, R27, R32), PC (R02, R24, R28, R30), AP (Q02, Q03), NP (nenhum).

=====================================================================
PARTE 1/3 — MAPA
=====================================================================

| id | folha | ponto de julgamento | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL | aderência |
|---|---|---|---|---|---|---|
| L1-R192 | P2-1.7 | Na transcrição em streaming do Amazon Transcribe, o áudio é dividido em segmentos naturais de fala (troca de orador ou pausa) e os parciais de cada segmento são devolvidos até a sua conclusão | D | AWS, Amazon Transcribe Developer Guide, "Streaming and partial results" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/streaming-partial-results.html; verificado em 18/10/2026) | n | direta |
| L1-R193 | P2-1.7 | Em PCM de dois canais, cada amostra tem quatro bytes e o bloco enviado em streaming deve ser múltiplo de 4 bytes (e não apenas ter número par de bytes) | NP | AWS, Amazon Transcribe Developer Guide, "Transcribing streaming audio" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html; verificado em 18/10/2026) | n | direta |
| L1-R194 | P2-1.7 | O reconhecimento em streaming do Google Cloud Speech-to-Text está disponível apenas por gRPC, e não por chamadas REST | SH | Google Cloud, Speech-to-Text, "Transcribe audio from streaming input" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R195 | P2-1.7 | Na LimitExceededException causada por aumento rápido do número de fluxos, a solução é repetir com espera exponencial e aumentar os fluxos gradualmente, e não pedir aumento de cota | SH | AWS, Amazon Transcribe Developer Guide, "Transcribing streaming audio" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html; verificado em 18/10/2026) | n | direta |
| L1-R196 | P2-1.7 | No Google Cloud Speech-to-Text (API v2), sem habilitar os resultados intermediários o cliente recebe só a resposta final, o que impede a legenda ao vivo à medida que o orador fala | AP | Google Cloud, Speech-to-Text, referência RPC da API v2, "StreamingRecognitionFeatures", "StreamingRecognitionResult" e "SpeechEventType" (Last updated 2025-10-23 UTC) (https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2; verificado em 18/10/2026) | n | direta |
| L1-R197 | P2-1.7 | No tempo limite por atividade de voz do streaming do Google (API v2), speech_start_timeout encerra o fluxo se a fala não começa, e speech_end_timeout, se a fala termina e não volta dentro da duração | PC | Google Cloud, Speech-to-Text, referência RPC da API v2, "StreamingRecognitionFeatures", "StreamingRecognitionResult" e "SpeechEventType" (Last updated 2025-10-23 UTC) (https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2; verificado em 18/10/2026) | n | direta |
| L1-R198 | P2-1.7 | Na identificação automática de idioma em streaming do Amazon Transcribe, informar um idioma preferencial pode acelerar a identificação | AP | AWS, Amazon Transcribe API Reference, "StartStreamTranscription" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_StartStreamTranscription.html; verificado em 18/10/2026) | n | direta |
| L1-R199 | P2-1.7 | No streaming do Google (API v2), SPEECH_ACTIVITY_BEGIN indica o início da voz humana e SPEECH_ACTIVITY_END, o seu fim (e não o inverso) | TSj | Google Cloud, Speech-to-Text, referência RPC da API v2, "StreamingRecognitionFeatures", "StreamingRecognitionResult" e "SpeechEventType" (Last updated 2025-10-23 UTC) (https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2; verificado em 18/10/2026) | n | direta |
| L1-R200 | P2-1.7 | No Azure Speech, o refinamento pós-fluxo mantém parciais de baixa latência e substitui só o resultado final por versão mais precisa, obtida em segunda passagem paralela com contexto de áudio mais amplo | AP | Microsoft Learn, Azure Speech, "How to recognize speech" (Last updated on 2026-06-05) (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R201 | P2-1.7 | No Amazon Transcribe em streaming, a identificação automática de idioma não pode ser combinada com modelo de linguagem personalizado nem com redação | SH | AWS, Amazon Transcribe API Reference, "StartStreamTranscription" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_StartStreamTranscription.html; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R202 | P2-1.8 | Segundo o model card do Whisper, os usuários primários pretendidos são pesquisadores de IA, embora o modelo também possa servir como solução de ASR para desenvolvedores, sobretudo para o inglês | D | OpenAI, repositório openai/whisper, model-card.md (arquivo do repositório; sem data de atualização na página) (https://raw.githubusercontent.com/openai/whisper/main/model-card.md; verificado em 18/10/2026) | n | direta |
| L1-R203 | P2-1.8 | O model card do Whisper desaconselha o uso dos modelos para classificação e para inferir atributos humanos a partir do áudio (e não o considera avaliado e apropriado) | AP | OpenAI, repositório openai/whisper, model-card.md (arquivo do repositório; sem data de atualização na página) (https://raw.githubusercontent.com/openai/whisper/main/model-card.md; verificado em 18/10/2026) | n | direta |
| L1-R204 | P2-1.8 | A tabela do repositório do Whisper indica cerca de 5 GB de VRAM para o modelo medium, o que torna insuficiente uma placa de 4 GB | NP | OpenAI, repositório openai/whisper, README.md (arquivo do repositório; sem data de atualização na página) (https://raw.githubusercontent.com/openai/whisper/main/README.md; verificado em 18/10/2026) | n | direta |
| L1-R205 | P2-1.8 | O Whisper requer a ferramenta de linha de comando ffmpeg instalada no sistema (e não a dispensa) | D | OpenAI, repositório openai/whisper, README.md (arquivo do repositório; sem data de atualização na página) (https://raw.githubusercontent.com/openai/whisper/main/README.md; verificado em 18/10/2026) | n | direta |
| L1-R206 | P2-1.8 | No Google Cloud Speech-to-Text, o reconhecimento assíncrono inicia uma operação de longa duração, consultada periodicamente, ao contrário do síncrono, que é bloqueante | SH | Google Cloud, Speech-to-Text, "Cloud Speech-to-Text overview" (guia de requisições; Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-requests; verificado em 18/10/2026) | n | direta |
| L1-R207 | P2-1.8 | A transcrição rápida (fast transcription) do Azure Speech devolve os resultados de forma síncrona, e não assíncrona por consulta posterior | TSj | Microsoft Learn, Azure Speech, "Speech to Text Overview" (Last updated on 2026-07-13) (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text; verificado em 18/10/2026) | n | direta |
| L1-R208 | P2-1.8 | O filtro de palavrões do Google substitui as palavras filtradas pela primeira letra e asteriscos e opera sobre palavras isoladas, sem detectar fala ofensiva expressa em frase | AP | Google Cloud, Speech-to-Text, "Cloud Speech-to-Text overview" (guia de requisições; Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-requests; verificado em 18/10/2026) | n | direta |
| L1-R209 | P2-1.8 | No Amazon Transcribe, o modelo de linguagem personalizado aprende o contexto da palavra, e o vocabulário personalizado aumenta o reconhecimento por dicas, como pronúncias (e não o inverso) | PC | AWS, Amazon Transcribe Developer Guide, "Custom language models" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html; verificado em 18/10/2026) | n | direta |
| L1-R210 | P2-1.8 | Na transcrição em lote do Azure Speech, que agenda os trabalhos em regime de melhor esforço, enviar as requisições em taxa mais alta não acelera o processamento, e convém distribuí-las ao longo do tempo | SH | Microsoft Learn, Azure Speech, "Batch transcription overview" (Last updated on 2026-06-25) (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription; verificado em 18/10/2026) | n | direta |
| L1-R211 | P2-1.8 | No Amazon Transcribe, a identificação de PII e a redação de PII não podem ser definidas na mesma requisição (a combinação gera BadRequestException) | PC | AWS, Amazon Transcribe API Reference, "StartStreamTranscription" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_StartStreamTranscription.html; verificado em 18/10/2026) | n | direta |
| L2-R133 | P2-2.1 | Sem arquivo de referência, o Google admite baixar a transcrição automática, editá-la (revisão humana) e usá-la como ground truth, desde que verificada, pois afeta as métricas | SH | Google Cloud, Speech-to-Text, "Measure and improve accuracy" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/measure-accuracy; verificado em 18/10/2026) | n | direta |
| L2-R134 | P2-2.1 | Para termos raros, corrige-se manualmente a transcrição (revisão humana); para termos frequentes ou de domínio, considera-se modelo de fala personalizado (e não o inverso) | SH | Microsoft Learn (previous-versions), Azure AI Video Indexer, "Speech model training best practices" (Last updated on 2025-10-06) (https://learn.microsoft.com/en-us/previous-versions/azure/azure-video-indexer/speech-model-training-best-practices; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L2-R135 | P2-2.1 | Segundo a Agência Senado, a taquigrafia é técnica de escrita rápida e abreviada que permite registrar tudo o que se fala praticamente em tempo real | D | Agência Senado, "Diretores ressaltam a confiabilidade da taquigrafia do Senado" (publicada em 03/05/2018) (https://www12.senado.leg.br/noticias/materias/2018/05/03/diretores-ressaltam-a-confiabilidade-da-taquigrafia-do-senado; verificado em 18/10/2026) | n | direta |
| L2-R136 | P2-2.1 | Segundo a nota de transparência do Azure Speech, os erros de inserção da transcrição automática são limitados no serviço Speech e um pouco mais frequentes no modelo de transcrição da OpenAI (e não o inverso) | D | Microsoft Learn, Azure Speech, "Transparency note and use cases for speech to text" (Last updated on 2026-03-31) (https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/speech-service/speech-to-text/transparency-note; verificado em 18/10/2026) | n | direta |
| L2-R137 | P2-2.1 | Segundo a diretora da Secretaria de Registro e Redação Parlamentar do Senado, o profissional precisa de "ouvido de taquígrafo" para reconhecer vocalmente os parlamentares, que muitas vezes têm falas sobrepostas | AP | Agência Senado, "Modelo digital traz velocidade à taquigrafia do Senado" (publicada em 26/11/2021) (https://www12.senado.leg.br/noticias/materias/2021/11/26/modelo-digital-traz-velocidade-a-taquigrafia-do-senado; verificado em 18/10/2026) | n | direta |
| L2-R138 | P2-2.1 | Segundo o Senado, uma fala de 20 minutos é degravada por cinco profissionais, cada um registrando trecho de quatro minutos (20 ÷ 5), e não de dez | NP | Agência Senado, "Modelo digital traz velocidade à taquigrafia do Senado" (publicada em 26/11/2021) (https://www12.senado.leg.br/noticias/materias/2021/11/26/modelo-digital-traz-velocidade-a-taquigrafia-do-senado; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L2-R139 | P2-2.1 | Para depender do ASR (transcrição de máquina) em sistemas críticos, o Google considera muito importante medir sua acurácia, pois sistemas de aprendizado de máquina raramente são 100% precisos | AP | Google Cloud, Speech-to-Text, "Measure and improve speech accuracy" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/speech-accuracy; verificado em 18/10/2026) | n | direta |
| L2-R140 | P2-2.1 | Segundo o Google, um índice único de acurácia para todos os clientes e casos de uso é impraticável, pois a medição depende do caso de uso e da qualidade do áudio | AP | Google Cloud, Speech-to-Text, "Measure and improve accuracy" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/measure-accuracy; verificado em 18/10/2026) | n | direta |
| L2-R141 | P2-2.1 | No modelo digital descrito pelo Senado, depois de transcrito o texto é revisado e, por fim, passa pela montagem final das notas (degravação, revisão e montagem, nessa ordem) | D | Agência Senado, "Modelo digital traz velocidade à taquigrafia do Senado" (publicada em 26/11/2021) (https://www12.senado.leg.br/noticias/materias/2021/11/26/modelo-digital-traz-velocidade-a-taquigrafia-do-senado; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L2-R142 | P2-2.1 | Segundo o Senado, no Plenário o registro é presencial, conferido com o áudio e depois revisado, e nas comissões é feita a degravação do áudio, com revisão (e não o inverso) | TSj | Agência Senado, "Diretores ressaltam a confiabilidade da taquigrafia do Senado" (publicada em 03/05/2018) (https://www12.senado.leg.br/noticias/materias/2018/05/03/diretores-ressaltam-a-confiabilidade-da-taquigrafia-do-senado; verificado em 18/10/2026) | VOLÁTIL baixo | direta |

### Vizinhanças declaradas (pontos distintos, mesma página, mesmo tema ou mesmo fornecedor)

- L1-R192 × L1-R103, R111 (1.7) e L1-R79 (1.5): o R103 julga os níveis da estabilização, o R111 julga a segmentação só por silêncio no Azure e o R79 julga o campo Stable; o R192 julga o critério de segmentação do Amazon Transcribe (troca de orador ou pausa), que nenhum deles julga.
- L1-R193 × L1-R14 e L1-R13 (1.7): mesma página; o R14 calcula o bloco de 100 ms em PCM mono e o R13 julga que o tamanho do bloco influencia a latência; o R193 julga a regra de múltiplo de 4 bytes em dois canais.
- L1-R194 × L1-R107 (1.7): ambos tratam do Google, mas o R107 julga os papéis do síncrono e do streaming e o R194 julga o protocolo (gRPC) em que o streaming é oferecido.
- L1-R195 × L1-R113 e L1-R114 (1.7): mesma seção LimitExceededException, causas diferentes (cota de fluxos concorrentes, duração máxima, aumento rápido do número de fluxos); o R195 julga a terceira causa e a solução própria dela.
- L1-R196, R197 e R199 (1.7, Google API v2): mesma página de referência e pontos distintos (opção de resultados intermediários; tempos limite de início e de fim de fala; eventos de início e fim de voz). R197 e R199 não repetem entre si o juízo (duração do tempo limite × significado de evento).
- L1-R196 × L1-R107 e L1-R79: o R107 julga síncrono × streaming e o R79 julga a estabilidade; o R196 julga a consequência de não habilitar parciais.
- L1-R198 e L1-R201 × L3-R07 (3.4): o R07 julga a identificação de idioma como tarefa de modelo multitarefa; os dois itens de 1.7 julgam parâmetros da API de streaming do Amazon Transcribe (idioma preferencial; restrição de combinação).
- L1-R200 × L1-R86 (1.5): o R86 julga a segmentação semântica do Azure; o R200 julga o refinamento pós-fluxo, recurso distinto da mesma página.
- L1-R201 × L1-R211 (1.8): mesma página da API do Amazon Transcribe, em folhas distintas e com restrições diferentes (identificação de idioma × CLM ou redação; identificação × redação de PII).
- L1-R203 × L1-R124 e L1-R126 (1.8) e L2-R27 (2.1): mesmo model card do Whisper; o R124 julga o consentimento, o R126 a diarização e o L2-R27 o uso em decisões de alto risco; o R203 julga a classificação e a inferência de atributos humanos (frase própria do model card).
- L1-R202 × L1-R98 (1.6) e L1-Q18 (1.8): o R98 julga a uniformidade entre sotaques e o Q18 a abertura do código; o R202 julga os usuários primários pretendidos.
- L1-R204 × L1-R18 e L1-R129 (1.8): mesma tabela do README; o R18 julga parâmetros e o R129 as velocidades relativas; o R204 julga a memória (VRAM) requerida.
- L1-R205 (1.8): requisito de instalação do README; nenhum item existente o julga.
- L1-R206 × L1-R107 (1.7): o R107 julga o síncrono como bloqueante em contraposição ao streaming; o R206 julga o modo assíncrono (operação de longa duração consultada periodicamente), que o R107 não julga.
- L1-R207 × L1-R123 (1.8) e L1-R69, R88 (1.4, 1.5): o R123 julga que o lote é assíncrono (e não síncrono); o R207 julga que a transcrição rápida é síncrona (e não assíncrona), modo distinto; R69 e R88 julgam canais e forma lexical na transcrição rápida.
- L1-R208 × L1-R127 (1.8): o R127 julga vocabulário personalizado × filtro de vocabulário da AWS; o R208 julga o filtro de palavrões do Google (substituição e alcance sobre palavras isoladas).
- L1-R209 × L1-R127, L1-R101 e L2-R80: mesma família de vocabulário da AWS; o R127 julga vocabulário × filtro, o R101 o formato de entrada de várias palavras e o L2-R80 números na tabela; o R209 julga vocabulário × modelo de linguagem personalizado.
- L1-R210 × L1-R123 (1.8): ambos tratam do lote do Azure; o R123 julga o modo assíncrono e o R210 julga a política de agendamento (melhor esforço; taxa de envio não acelera).
- L1-R211 × L1-R10 (1.6): o R10 julga a conduta de evitar informações sensíveis no vocabulário personalizado; o R211 julga a incompatibilidade, na mesma requisição, entre identificação e redação de PII.
- L2-R133 × L1-Q01, L1C-Q22 e L1-R21 (1.1) e L2-R103, R104 (2.7): os de 1.1 julgam o WER e o efeito de uma referência defeituosa; o L2-R103 julga que a referência costuma ser obtida por transcrição humana e o R104 que suas convenções devem aproximar-se das do sistema; o R133 julga o procedimento de, sem referência, editar a transcrição automática, e verificar o resultado, para usá-la como referência.
- L2-R136 × L2-R23 e L2-R30 (2.1): mesma nota de transparência do Azure; o R23 julga a expectativa de imprecisão e o R30 o áudio com voz, silêncio e ruído; o R136 julga os erros de inserção e sua frequência relativa.
- L2-R135, R137, R138, R141 e R142 (2.1): as cinco vêm das duas reportagens da Agência Senado e julgam pontos distintos (taquigrafia como registro praticamente em tempo real; reconhecimento vocal em falas sobrepostas; divisão da fala entre cinco profissionais; ordem transcrição, revisão e montagem; Plenário × comissões).
- L2-R139 e R140 × L2-Q03 e L2-R23 (2.1): o Q03 julga a dispensa da revisão humana; o R23 a expectativa de imprecisão; o R139 julga a orientação de medir a acurácia ao depender do ASR em sistema crítico, e o R140 a impraticabilidade de um índice único.
- L2-R134 (2.1) × L1-R96 e L2-R119 (1.6 e 2.8): esses julgam a adaptação do vocabulário; o R134 julga a escolha entre a correção manual (revisão humana) e o modelo personalizado, conforme a frequência do termo.

### Pontos para D1 da Gerência titular

- Aderência de L2-R136, R139 e R140 (2.1): a base é documentação de fornecedor sobre limitações e medição da acurácia da transcrição automática, em contraste com o texto de referência humano; o produtor entende como direta (diferença entre transcrição automática e revisão humana), mas a Gerência pode julgá-la lateral (tema também de 1.1 e 2.3).
- L2-R135, R137, R138, R141 e R142 (2.1): bases são reportagens da Agência Senado (órgão público, não norma); descrevem a prática do Senado em 2018 e 2021 e não a da Câmara. Por isso R138, R141 e R142 são VOLÁTIL baixo (procedimento descrito pode mudar) e R135 e R137 são conferência de base. A Gerência pode trocá-los por saldo se preferir só base normativa ou da Câmara (o Rol do DETAQ de 2009 foi excluído por decisão anterior).
- L2-R134 (2.1): a página está em "previous-versions" da Microsoft Learn; mantido como VOLÁTIL baixo. A Gerência pode trocá-lo se julgar a base arquivada insuficiente.
- L1-R201 e L1-R194 (1.7) são VOLÁTIL baixo (restrição de recurso do serviço e disponibilidade por protocolo); L1-R200 é VOLÁTIL baixo (existência e disponibilidade de recurso). Total de VOLÁTEIS de 1.7 depois da onda: 6/30 = 20% (no teto).
- 1.8 não tem VOLÁTIL novo (2/30 = 6,7%): os pontos são conceituais (modo assíncrono, política de agendamento, papéis de vocabulário e modelo de linguagem), de artefato publicado (model card, README) ou restrição documentada de parâmetro; todos entram na conferência de base de 4–8/1/2027 (T-11), sem efeito de VOLÁTIL.
- L1-R204 (VRAM do README) e L1-R193 (aritmética de bloco) dependem de tabela e regra documentadas; conferir a base em 4–8/1/2027.
- Gabarito: 15 C / 15 E (50,0%). [TS] 15/30 (todos em itens E).

FIM DA PARTE 1/3

=====================================================================
PARTE 2/3 — (d) ITENS DO ESTUDANTE
=====================================================================

Julgue o item.

**L1-R192** (P2-1.7)
Segundo a documentação do Amazon Transcribe, na transcrição em streaming de uma sessão, o serviço divide o áudio recebido em segmentos naturais de fala, como a troca de orador ou uma pausa no áudio, e devolve os resultados parciais de cada segmento até que ele seja integralmente transcrito.

**L1-R193** (P2-1.7)
Uma equipe da Câmara transmite ao Amazon Transcribe, em streaming, áudio PCM de dois canais, um por microfone, em blocos de 2.002 bytes. Segundo a documentação, esse tamanho é adequado, pois, com dois canais, cada amostra ocupa dois bytes e basta que o bloco tenha número par de bytes.

**L1-R194** (P2-1.7)
Uma equipe pretende legendar ao vivo as sessões do Plenário com o Cloud Speech-to-Text, do Google, mas dispõe apenas de aplicações que fazem chamadas REST. Segundo a documentação do serviço, o reconhecimento em streaming está disponível somente por gRPC, de modo que essas aplicações não poderão usá-lo para esse fim.

**L1-R195** (P2-1.7)
Durante um teste de carga, a equipe da Câmara aumentou rapidamente o número de fluxos simultâneos de transcrição em streaming no Amazon Transcribe e recebeu o erro LimitExceededException. Segundo a documentação, nessa causa específica do erro, a solução é pedir o aumento da cota de fluxos simultâneos pelo console de Service Quotas.

**L1-R196** (P2-1.7)
Para exibir ao público a legenda de uma sessão à medida que o orador fala, a equipe deve habilitar, na configuração do reconhecimento em streaming do Google Cloud Speech-to-Text (API v2), o envio de resultados intermediários; sem essa opção, apenas a resposta final é devolvida ao cliente.

**L1-R197** (P2-1.7)
Na configuração de tempo limite por atividade de voz do reconhecimento em streaming do Google Cloud Speech-to-Text (API v2), o speech_start_timeout encerra o fluxo quando, depois de detectada a fala, não se detecta mais fala dentro da duração definida, ao passo que o speech_end_timeout encerra o fluxo quando a fala não começa dentro dessa duração.

**L1-R198** (P2-1.7)
Uma equipe da Câmara usa a identificação automática de idioma do Amazon Transcribe em streaming em reuniões de comissão nas quais predomina o português, com falas ocasionais em outro idioma. Segundo a referência da API, informar um idioma preferencial pode ajudar o serviço a identificar o idioma mais rapidamente do que se esse parâmetro fosse omitido.

**L1-R199** (P2-1.7)
No reconhecimento em streaming do Google Cloud Speech-to-Text (API v2), com os eventos de atividade de voz habilitados, o evento SPEECH_ACTIVITY_END indica que o servidor detectou o início da voz humana no fluxo, e o evento SPEECH_ACTIVITY_BEGIN, o seu fim.

**L1-R200** (P2-1.7)
Na legenda ao vivo de uma sessão com o Azure Speech, a equipe quer manter a baixa latência dos resultados parciais e obter resultados finais mais precisos. Segundo a documentação, o refinamento pós-fluxo (post-stream refinement) atende a esse objetivo: executa uma segunda passagem de reconhecimento em paralelo ao streaming e substitui apenas o resultado final por uma versão mais precisa, que usa contexto de áudio mais amplo.

**L1-R201** (P2-1.7)
Uma equipe da Câmara pretende transcrever em streaming, no Amazon Transcribe, reuniões com falas em mais de um idioma, com redação automática de dados pessoais (PII). Segundo a referência da API, a identificação automática de idioma em streaming pode ser combinada com a redação de conteúdo na mesma requisição.

**L1-R202** (P2-1.8)
Ao avaliar o Whisper para a degravação de sessões em português, a equipe da Câmara deve considerar que, segundo o model card, os usuários primários pretendidos dos modelos são pesquisadores de IA que estudam sua robustez, generalização, capacidades, vieses e restrições, embora o Whisper também possa ser útil como solução de ASR para desenvolvedores, especialmente para o inglês.

**L1-R203** (P2-1.8)
Segundo o model card do Whisper, a Câmara pode usar os modelos, além de transcrever os pronunciamentos, para inferir atributos dos oradores, como o estado emocional, a partir do áudio das sessões, pois a classificação é um uso avaliado e apropriado para esses modelos.

**L1-R204** (P2-1.8)
Uma equipe pretende executar localmente o modelo medium multilíngue do Whisper para degravar sessões em português, em estação cuja placa de vídeo tem 4 GB de memória. Segundo a tabela de modelos do repositório do Whisper, que indica cerca de 5 GB de memória (VRAM) para esse modelo, a placa é insuficiente.

**L1-R205** (P2-1.8)
Ao instalar o Whisper em servidor do órgão para degravar as sessões, a equipe constata, pelo repositório do projeto, que o uso do pacote dispensa a instalação, no sistema, da ferramenta de linha de comando ffmpeg.

**L1-R206** (P2-1.8)
Para degravar a gravação de uma reunião longa de comissão, a equipe usará o reconhecimento assíncrono do Google Cloud Speech-to-Text. Segundo a documentação, esse modo inicia uma operação de longa duração, cujos resultados a aplicação pode consultar periodicamente, ao contrário do reconhecimento síncrono, que é bloqueante.

**L1-R207** (P2-1.8)
Para obter a transcrição de um arquivo de áudio de audiência o mais rápido possível, com latência previsível, a equipe usa a API de transcrição rápida (fast transcription) do Azure Speech, que, segundo a documentação, devolve os resultados de forma assíncrona, por consulta posterior.

**L1-R208** (P2-1.8)
Ao usar o Cloud Speech-to-Text, do Google, na degravação de sessões, a equipe deve considerar que o filtro de palavrões, quando ativado, substitui as palavras filtradas por sua primeira letra seguida de asteriscos e opera sobre palavras isoladas, sem detectar fala ofensiva expressa em frase ou em combinação de palavras.

**L1-R209** (P2-1.8)
No Amazon Transcribe, o vocabulário personalizado aprende o contexto associado a uma palavra, isto é, como e quando ela é usada e sua relação com outras palavras, ao passo que o modelo de linguagem personalizado aumenta o reconhecimento da palavra por meio de dicas, como pronúncias.

**L1-R210** (P2-1.8)
A Câmara pretende degravar um grande acervo de gravações com a transcrição em lote do Azure Speech. Segundo a documentação, como o serviço agenda os trabalhos em regime de melhor esforço e cada região processa as requisições uma de cada vez, enviá-las em taxa mais alta não acelera o processamento, sendo recomendável distribuí-las ao longo do tempo.

**L1-R211** (P2-1.8)
Para que o texto de uma reunião reservada, transcrita em streaming no Amazon Transcribe, traga os dados pessoais (PII) sinalizados e, ao mesmo tempo, ocultados, a equipe pode incluir na mesma requisição a identificação de conteúdo (ContentIdentificationType) e a redação de conteúdo (ContentRedactionType); segundo a referência da API, o serviço aceita as duas opções juntas.

**L2-R133** (P2-2.1)
Uma equipe quer medir a acurácia da transcrição automática de uma audiência no Google Cloud Speech-to-Text, mas não dispõe de arquivo de referência (ground truth). Segundo a documentação, ela pode baixar a transcrição em formato de texto, editá-la conforme necessário e enviá-la como referência, devendo verificar se o arquivo representa com exatidão as transcrições corretas, pois isso afeta diretamente as métricas de acurácia.

**L2-R134** (P2-2.1)
Uma equipe da Câmara constata que alguns nomes e termos aparecem raramente nas gravações das sessões. Segundo a documentação do Azure AI Video Indexer, nesse caso deve criar e treinar um modelo de fala personalizado, reservando a correção manual da transcrição no site para os termos frequentes ou específicos do domínio.

**L2-R135** (P2-2.1)
Segundo a Agência Senado, a taquigrafia é uma técnica de escrita rápida e abreviada que permite o registro de tudo o que se fala praticamente em tempo real.

**L2-R136** (P2-2.1)
Segundo a nota de transparência do Azure Speech, a transcrição automática pode apresentar erros de inserção na presença de ruído ou de fala de fundo suave, e esses erros são um pouco menos frequentes com o modelo de transcrição da OpenAI do que com o serviço Speech.

**L2-R137** (P2-2.1)
Segundo a diretora da Secretaria de Registro e Redação Parlamentar do Senado, em reportagem da Agência Senado de 2021, o profissional que transcreve do oral para o escrito precisa ter "ouvido de taquígrafo" para reconhecer vocalmente os parlamentares, que muitas vezes têm falas sobrepostas.

**L2-R138** (P2-2.1)
Segundo a Agência Senado, no registro das notas taquigráficas do Senado, uma fala de 20 minutos é degravada por cinco profissionais diferentes, simultânea e sucessivamente, e cada taquígrafo registra um trecho de dez minutos.

**L2-R139** (P2-2.1)
A Câmara pretende confiar o registro de reuniões a um sistema de reconhecimento automático de fala (ASR), também chamado de transcrição de máquina. Segundo a documentação do Google Cloud Speech-to-Text, como os sistemas de aprendizado de máquina raramente são 100% precisos, é muito importante medir a acurácia do ASR quando se pretende depender dele em sistemas críticos.

**L2-R140** (P2-2.1)
A Câmara considera adotar, para todas as suas audiências, o índice único de acurácia divulgado pelo fornecedor da transcrição automática. Segundo a documentação do Google Cloud Speech-to-Text, esse procedimento é adequado, pois a medição da acurácia independe do caso de uso e das condições acústicas, e um único índice vale para todos os clientes.

**L2-R141** (P2-2.1)
Segundo a Agência Senado, no modelo digital de registro das notas taquigráficas do Senado, depois de transcrito o texto é revisado e, por fim, passa pela montagem final das notas.

**L2-R142** (P2-2.1)
Segundo a Agência Senado, no Senado o registro em Plenário é feito por degravação do áudio, seguida de revisão, ao passo que nas comissões o registro é feito presencialmente, conferido com o áudio e depois revisado para a versão final.

FIM DA PARTE 2/3

=====================================================================
PARTE 3/3 — GABARITO E JUSTIFICATIVA
=====================================================================

**L1-R192** (P2-1.7) — Gabarito: C
Justificativa: O serviço "breaks up the incoming audio stream based on natural speech segments, such as a change in speaker or a pause in the audio". O item reproduz o critério de segmentação e o retorno incremental dos parciais.
Base: AWS, Amazon Transcribe Developer Guide, "Streaming and partial results" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/streaming-partial-results.html), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L1-R193** (P2-1.7) — Gabarito: E [TS]
Justificativa: Com dois canais, "each sample consists of four bytes, so each chunk should be a multiple of 4 bytes"; 2.002 bytes não é múltiplo de 4 (2.002 ÷ 4 = 500,5). O item troca o tamanho da amostra e a regra do bloco.
Base: AWS, Amazon Transcribe Developer Guide, "Transcribing streaming audio" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L1-R194** (P2-1.7) — Gabarito: C — VOLÁTIL (baixo); REVERIFICAR em 4–8/1/2027.
Justificativa: A página traz "Streaming speech recognition is available through gRPC only". Sem gRPC não há streaming; o item aplica o dado ao cenário. VOLÁTIL baixo: existência de recurso por protocolo.
Base: Google Cloud, Speech-to-Text, "Transcribe audio from streaming input" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize), verificado em 18/10/2026.
Aderência: direta.

**L1-R195** (P2-1.7) — Gabarito: E [TS]
Justificativa: Nessa causa há "a system-level protection mechanism with no adjustable quota"; a solução é "retry with exponential backoff and gradually increase your number of concurrent streams". O item atribui a esta causa a solução da cota excedida.
Base: AWS, Amazon Transcribe Developer Guide, "Transcribing streaming audio" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L1-R196** (P2-1.7) — Gabarito: C
Justificativa: A referência da API v2 define a opção de resultados intermediários e informa: "Otherwise, only the final response will be streamed back". O item aplica a regra à legenda ao vivo.
Base: Google Cloud, Speech-to-Text, referência RPC da API v2, "StreamingRecognitionFeatures", "StreamingRecognitionResult" e "SpeechEventType" (Last updated 2025-10-23 UTC) (https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L1-R197** (P2-1.7) — Gabarito: E [TS]
Justificativa: O speech_start_timeout é a "Duration to timeout the stream if no speech begins" e o speech_end_timeout, a "Duration to timeout the stream after speech ends". Os papéis foram trocados.
Base: Google Cloud, Speech-to-Text, referência RPC da API v2, "StreamingRecognitionFeatures", "StreamingRecognitionResult" e "SpeechEventType" (Last updated 2025-10-23 UTC) (https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L1-R198** (P2-1.7) — Gabarito: C
Justificativa: "Adding a preferred language can help Amazon Transcribe identify the language faster than if you omit this parameter". O item aplica a orientação à reunião de predominância do português.
Base: AWS, Amazon Transcribe API Reference, "StartStreamTranscription" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_StartStreamTranscription.html), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L1-R199** (P2-1.7) — Gabarito: E [TS]
Justificativa: O evento BEGIN indica "the beginning of human voice activity in the stream" e o evento END, "the end of human voice activity in the stream". O item troca os dois eventos.
Base: Google Cloud, Speech-to-Text, referência RPC da API v2, "StreamingRecognitionFeatures", "StreamingRecognitionResult" e "SpeechEventType" (Last updated 2025-10-23 UTC) (https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L1-R200** (P2-1.7) — Gabarito: C — VOLÁTIL (baixo); REVERIFICAR em 4–8/1/2027.
Justificativa: O recurso "runs a second recognition pass in parallel with real-time streaming, so intermediate and partial results stay low-latency", e "Only the final result is replaced with a more accurate version that uses broader audio context". VOLÁTIL baixo: existência e disponibilidade do recurso.
Base: Microsoft Learn, Azure Speech, "How to recognize speech" (Last updated on 2026-06-05) (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech), verificado em 18/10/2026.
Aderência: direta.

**L1-R201** (P2-1.7) — Gabarito: E [TS] — VOLÁTIL (baixo); REVERIFICAR em 4–8/1/2027.
Justificativa: "Streaming language identification can't be combined with custom language models or redaction". O item afirma que a combinação é possível. VOLÁTIL baixo: restrição de recurso do serviço.
Base: AWS, Amazon Transcribe API Reference, "StartStreamTranscription" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_StartStreamTranscription.html), verificado em 18/10/2026.
Aderência: direta.

**L1-R202** (P2-1.8) — Gabarito: C
Justificativa: "The primary intended users of these models are AI researchers"; o model card acrescenta que o Whisper é "potentially quite useful as an ASR solution for developers, especially for English speech recognition".
Base: OpenAI, repositório openai/whisper, model-card.md (arquivo do repositório; sem data de atualização na página) (https://raw.githubusercontent.com/openai/whisper/main/model-card.md), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L1-R203** (P2-1.8) — Gabarito: E [TS]
Justificativa: O model card diz que "use of the model for classification is not only not evaluated but also not appropriate, particularly to infer human attributes". O item inverte a avaliação desse uso.
Base: OpenAI, repositório openai/whisper, model-card.md (arquivo do repositório; sem data de atualização na página) (https://raw.githubusercontent.com/openai/whisper/main/model-card.md), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L1-R204** (P2-1.8) — Gabarito: C
Justificativa: A tabela traz o modelo medium com "~5 GB" de VRAM requerida; 4 GB é menos que 5 GB. O item aplica o dado da tabela ao cenário.
Base: OpenAI, repositório openai/whisper, README.md (arquivo do repositório; sem data de atualização na página) (https://raw.githubusercontent.com/openai/whisper/main/README.md), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L1-R205** (P2-1.8) — Gabarito: E [TS]
Justificativa: O README afirma: "It also requires the command-line tool" ffmpeg "to be installed on your system". O item troca a exigência pela dispensa.
Base: OpenAI, repositório openai/whisper, README.md (arquivo do repositório; sem data de atualização na página) (https://raw.githubusercontent.com/openai/whisper/main/README.md), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L1-R206** (P2-1.8) — Gabarito: C
Justificativa: O modo assíncrono "initiates a Long-Running Operation" e permite "periodically poll for recognition results"; já "A synchronous request is blocking".
Base: Google Cloud, Speech-to-Text, "Cloud Speech-to-Text overview" (guia de requisições; Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-requests), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L1-R207** (P2-1.8) — Gabarito: E [TS]
Justificativa: A transcrição rápida serve para "return results synchronously and faster than real-time audio"; o modo assíncrono, de consulta posterior, é o da transcrição em lote. O item troca síncrono por assíncrono.
Base: Microsoft Learn, Azure Speech, "Speech to Text Overview" (Last updated on 2026-07-13) (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L1-R208** (P2-1.8) — Gabarito: C
Justificativa: "The profanity filter operates on single words, it does not detect abusive or offensive speech that is a phrase or a combination of words"; as palavras filtradas "will contain their first letter and asterisks for the remaining characters".
Base: Google Cloud, Speech-to-Text, "Cloud Speech-to-Text overview" (guia de requisições; Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-requests), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L1-R209** (P2-1.8) — Gabarito: E [TS]
Justificativa: "Unlike custom vocabularies, which increase recognition of a word by providing hints (such as pronunciations), custom language models learn the context associated with a given word". Os papéis foram trocados.
Base: AWS, Amazon Transcribe Developer Guide, "Custom language models" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L1-R210** (P2-1.8) — Gabarito: C
Justificativa: "The service schedules batch transcription jobs on a best-effort basis"; "each region processes requests one at a time" e "Submitting jobs at a higher rate doesn't speed up processing"; a página recomenda "Distribute your requests over time".
Base: Microsoft Learn, Azure Speech, "Batch transcription overview" (Last updated on 2026-06-25) (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L1-R211** (P2-1.8) — Gabarito: E [TS]
Justificativa: "You can’t set ContentIdentificationType and ContentRedactionType in the same request"; com ambos, a requisição retorna BadRequestException. O item afirma que o serviço aceita as duas juntas.
Base: AWS, Amazon Transcribe API Reference, "StartStreamTranscription" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_StartStreamTranscription.html), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L2-R133** (P2-2.1) — Gabarito: C
Justificativa: O Google recomenda baixar a transcrição, "Edit the transcription file as needed" e enviá-la como referência, e manda "Verify that the ground truth file accurately represents the correct transcriptions, as it directly affects the accuracy metrics".
Base: Google Cloud, Speech-to-Text, "Measure and improve accuracy" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/measure-accuracy), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L2-R134** (P2-2.1) — Gabarito: E [TS] — VOLÁTIL (baixo); REVERIFICAR em 4–8/1/2027.
Justificativa: Para termos raros, "you can manually edit and correct the transcript directly in the Azure AI Video Indexer website"; para os frequentes ou de domínio, "consider creating a custom speech model". O item inverte as condutas. VOLÁTIL baixo: página em previous-versions.
Base: Microsoft Learn (previous-versions), Azure AI Video Indexer, "Speech model training best practices" (Last updated on 2025-10-06) (https://learn.microsoft.com/en-us/previous-versions/azure/azure-video-indexer/speech-model-training-best-practices), verificado em 18/10/2026.
Aderência: direta.

**L2-R135** (P2-2.1) — Gabarito: C
Justificativa: A reportagem descreve a taquigrafia como "Técnica de escrita rápida e abreviada" que "permite o registro de tudo o que se fala praticamente em tempo real". O item reproduz a descrição.
Base: Agência Senado, "Diretores ressaltam a confiabilidade da taquigrafia do Senado" (publicada em 03/05/2018) (https://www12.senado.leg.br/noticias/materias/2018/05/03/diretores-ressaltam-a-confiabilidade-da-taquigrafia-do-senado), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L2-R136** (P2-2.1) — Gabarito: E [TS]
Justificativa: A nota diz que os modelos "can produce insertion errors in the presence of noise or soft background speech" e que o erro "is limited when you use the Speech service, but it's slightly more frequent when you use the transcription model". O item inverte a frequência.
Base: Microsoft Learn, Azure Speech, "Transparency note and use cases for speech to text" (Last updated on 2026-03-31) (https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/speech-service/speech-to-text/transparency-note), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L2-R137** (P2-2.1) — Gabarito: C
Justificativa: A reportagem registra a necessidade de "ouvido de taquígrafo" para fazer "o reconhecimento vocal dos parlamentares, que muitas vezes têm falas sobrepostas". O item reproduz a afirmação, sem acrescentar condição.
Base: Agência Senado, "Modelo digital traz velocidade à taquigrafia do Senado" (publicada em 26/11/2021) (https://www12.senado.leg.br/noticias/materias/2021/11/26/modelo-digital-traz-velocidade-a-taquigrafia-do-senado), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L2-R138** (P2-2.1) — Gabarito: E [TS] — VOLÁTIL (baixo); REVERIFICAR em 4–8/1/2027.
Justificativa: A reportagem informa que a fala de 20 minutos é "degravada por cinco profissionais diferentes" e que "cada taquígrafo registra um trecho de quatro minutos" (20 ÷ 5 = 4). O item troca quatro por dez. VOLÁTIL baixo: procedimento descrito em reportagem de 2021.
Base: Agência Senado, "Modelo digital traz velocidade à taquigrafia do Senado" (publicada em 26/11/2021) (https://www12.senado.leg.br/noticias/materias/2021/11/26/modelo-digital-traz-velocidade-a-taquigrafia-do-senado), verificado em 18/10/2026.
Aderência: direta.

**L2-R139** (P2-2.1) — Gabarito: C
Justificativa: O Google informa que o ASR é "also known as machine transcription" e que, "If you plan to rely on ASR for critical systems, it's very important to measure its accuracy". O item reproduz a orientação.
Base: Google Cloud, Speech-to-Text, "Measure and improve speech accuracy" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/speech-accuracy), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L2-R140** (P2-2.1) — Gabarito: E [TS]
Justificativa: O Google afirma que "a singular accuracy score for all customers and use cases is impractical", pois a medição se acopla a casos de uso e às condições de gravação. O item afirma o contrário.
Base: Google Cloud, Speech-to-Text, "Measure and improve accuracy" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/measure-accuracy), verificado em 18/10/2026.
Conferência de base em 4–8/1/2027 (T-11, gce-cqfp), sem efeito de VOLÁTIL.
Aderência: direta.

**L2-R141** (P2-2.1) — Gabarito: C — VOLÁTIL (baixo); REVERIFICAR em 4–8/1/2027.
Justificativa: A reportagem informa: "Depois de transcrito, o texto é revisado e, por fim, passa pela montagem final das notas". O item reproduz a ordem das etapas. VOLÁTIL baixo: procedimento descrito em reportagem de 2021.
Base: Agência Senado, "Modelo digital traz velocidade à taquigrafia do Senado" (publicada em 26/11/2021) (https://www12.senado.leg.br/noticias/materias/2021/11/26/modelo-digital-traz-velocidade-a-taquigrafia-do-senado), verificado em 18/10/2026.
Aderência: direta.

**L2-R142** (P2-2.1) — Gabarito: E [TS] — VOLÁTIL (baixo); REVERIFICAR em 4–8/1/2027.
Justificativa: A reportagem informa: "O registro em Plenário é feito presencialmente, conferido com o áudio" e "depois é revisado"; "Nas comissões, é feita degravação e revisão do áudio". O item troca Plenário e comissões. VOLÁTIL baixo: procedimento descrito em reportagem de 2018.
Base: Agência Senado, "Diretores ressaltam a confiabilidade da taquigrafia do Senado" (publicada em 03/05/2018) (https://www12.senado.leg.br/noticias/materias/2018/05/03/diretores-ressaltam-a-confiabilidade-da-taquigrafia-do-senado), verificado em 18/10/2026.
Aderência: direta.

### Tabela de proveniência

| fonte | URL | data de verificação | usada em |
|---|---|---|---|
| AWS, Amazon Transcribe Developer Guide, "Streaming and partial results" (a página não exibe data de atualização) | https://docs.aws.amazon.com/transcribe/latest/dg/streaming-partial-results.html | 18/10/2026 | L1-R192 |
| AWS, Amazon Transcribe Developer Guide, "Transcribing streaming audio" (a página não exibe data de atualização) | https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html | 18/10/2026 | L1-R193, L1-R195 |
| Google Cloud, Speech-to-Text, "Transcribe audio from streaming input" (Last updated 2026-10-13 UTC) | https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize | 18/10/2026 | L1-R194 |
| Google Cloud, Speech-to-Text, referência RPC da API v2, "StreamingRecognitionFeatures", "StreamingRecognitionResult" e "SpeechEventType" (Last updated 2025-10-23 UTC) | https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2 | 18/10/2026 | L1-R196, L1-R197, L1-R199 |
| AWS, Amazon Transcribe API Reference, "StartStreamTranscription" (a página não exibe data de atualização) | https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_StartStreamTranscription.html | 18/10/2026 | L1-R198, L1-R201, L1-R211 |
| Microsoft Learn, Azure Speech, "How to recognize speech" (Last updated on 2026-06-05) | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech | 18/10/2026 | L1-R200 |
| OpenAI, repositório openai/whisper, model-card.md (arquivo do repositório; sem data de atualização na página) | https://raw.githubusercontent.com/openai/whisper/main/model-card.md | 18/10/2026 | L1-R202, L1-R203 |
| OpenAI, repositório openai/whisper, README.md (arquivo do repositório; sem data de atualização na página) | https://raw.githubusercontent.com/openai/whisper/main/README.md | 18/10/2026 | L1-R204, L1-R205 |
| Google Cloud, Speech-to-Text, "Cloud Speech-to-Text overview" (guia de requisições; Last updated 2026-10-13 UTC) | https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-requests | 18/10/2026 | L1-R206, L1-R208 |
| Microsoft Learn, Azure Speech, "Speech to Text Overview" (Last updated on 2026-07-13) | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text | 18/10/2026 | L1-R207 |
| AWS, Amazon Transcribe Developer Guide, "Custom language models" (a página não exibe data de atualização) | https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html | 18/10/2026 | L1-R209 |
| Microsoft Learn, Azure Speech, "Batch transcription overview" (Last updated on 2026-06-25) | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription | 18/10/2026 | L1-R210 |
| Google Cloud, Speech-to-Text, "Measure and improve accuracy" (Last updated 2026-10-13 UTC) | https://docs.cloud.google.com/speech-to-text/docs/measure-accuracy | 18/10/2026 | L2-R133, L2-R140 |
| Microsoft Learn (previous-versions), Azure AI Video Indexer, "Speech model training best practices" (Last updated on 2025-10-06) | https://learn.microsoft.com/en-us/previous-versions/azure/azure-video-indexer/speech-model-training-best-practices | 18/10/2026 | L2-R134 |
| Agência Senado, "Diretores ressaltam a confiabilidade da taquigrafia do Senado" (publicada em 03/05/2018) | https://www12.senado.leg.br/noticias/materias/2018/05/03/diretores-ressaltam-a-confiabilidade-da-taquigrafia-do-senado | 18/10/2026 | L2-R135, L2-R142 |
| Microsoft Learn, Azure Speech, "Transparency note and use cases for speech to text" (Last updated on 2026-03-31) | https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/speech-service/speech-to-text/transparency-note | 18/10/2026 | L2-R136 |
| Agência Senado, "Modelo digital traz velocidade à taquigrafia do Senado" (publicada em 26/11/2021) | https://www12.senado.leg.br/noticias/materias/2021/11/26/modelo-digital-traz-velocidade-a-taquigrafia-do-senado | 18/10/2026 | L2-R137, L2-R138, L2-R141 |
| Google Cloud, Speech-to-Text, "Measure and improve speech accuracy" (Last updated 2026-10-13 UTC) | https://docs.cloud.google.com/speech-to-text/docs/speech-accuracy | 18/10/2026 | L2-R139 |

Observações de proveniência: (1) o texto de cada página foi baixado em 18/10/2026 com curl e User-Agent de navegador (HTTP 200) e os trechos entre aspas das justificativas foram conferidos por script contra esse texto; (2) afirmações sobre ferramentas: Whisper (model card e README do repositório openai/whisper: usuários primários, classificação e atributos humanos, VRAM do modelo medium, exigência do ffmpeg), Google Cloud Speech-to-Text (streaming só por gRPC; opção de resultados intermediários; tempos limite e eventos de atividade de voz na API v2; reconhecimento assíncrono; filtro de palavrões; documentação de acurácia e ground truth), Azure Speech (refinamento pós-fluxo; transcrição rápida síncrona; lote em regime de melhor esforço; nota de transparência sobre erros de inserção) e AWS Transcribe (segmentação do streaming; regra de bloco PCM; LimitExceededException; idioma preferencial; restrição de identificação de idioma; vocabulário × modelo de linguagem personalizados; identificação × redação de PII), todas com URL oficial e data acima; nada sem fonte; (3) nenhum limite numérico de cota, preço, versão ou nome de modelo de API foi afirmado; (4) o Azure AI Video Indexer (L2-R134) e as reportagens da Agência Senado (L2-R135, R137, R138, R141, R142) são fontes oficiais de órgão ou fornecedor, citadas pela data de publicação ou de atualização da página; as reportagens descrevem a prática do Senado e não a da Câmara, o que os itens declaram no enunciado; (5) nenhuma base é documento de unidade extinta nem espelho de terceiros; (6) o Ato da Mesa nº 251/2026, o RICD e o Rol do DETAQ não são usados.

FIM DA PARTE 3/3

FIM DO LOTE
