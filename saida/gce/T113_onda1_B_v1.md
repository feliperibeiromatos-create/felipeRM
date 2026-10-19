# T113_onda1_B_v1.md — T-113 onda 1 (F1), parte B (P2-1.4, P2-1.5, P2-1.6) — 2026-10-18 — gerado por gce-cpp

Reforço onda 1 da ordem F (T-113; D-REFORCO-2; D-V15-F-AJUSTE; D1 da GCE V15_BAEF, seção 4), parte B, Lote 1, P2 itens 1.4, 1.5 e 1.6. Trinta itens AUTORAL novos: L1-R162 a L1-R171 (P2-1.4), L1-R172 a L1-R181 (P2-1.5) e L1-R182 a L1-R191 (P2-1.6). Nenhum item existente foi alterado. Rótulo AUTORAL em todos, aderência DIRETA em todos, QA PENDENTE em todos (D-QA-PENDENTE). Partida: pacote v1.11 (cada folha com 20 itens, todos diretos), mais a onda 4 (que não toca as folhas 1.4 a 1.6).

**Contagens da parte.** Gabarito: 14 C / 16 E (46.7% de C; faixa da parte, 12 a 18 C). [TS]: 15 de 30. VOLÁTIL novo: 10.

| folha | itens novos | C | E | [TS] | VOLÁTIL novos (teto) | VOLÁTEIS existentes | VOLÁTIL na folha final | aderência |
|---|--:|--:|--:|--:|--|--:|--|---|
| P2-1.4 | 10 | 4 | 6 | 5 | 3 (3) | 3 | 6 de 30 (20.0%) | 10 diretos de 10 |
| P2-1.5 | 10 | 5 | 5 | 5 | 2 (3) | 3 | 5 de 30 (16.7%) | 10 diretos de 10 |
| P2-1.6 | 10 | 5 | 5 | 5 | 5 (5) | 1 | 6 de 30 (20.0%) | 10 diretos de 10 |

**Leituras.** CLAUDE.md; ordens/ORDEM_V15_F_BANCO40.md; regras/proveniencia.md; regras/estilo_banca.md; edital/modulo_RF_IA_P2.md (1.4 "Diarização de falantes: identificação e separação de múltiplos oradores"; 1.5 "Pontuação automática e capitalização em transcrições"; 1.6 "Desafios do ASR em Português Brasileiro: sotaques, vocabulário técnico e parlamentar"); D-REFORCO-2 (regras 1 a 6), D-FONTE-DATA-ANTERIOR, D-ADERENCIA; D1 da GCE V15_BAEF (seções 0 e 4) e D1 da GBQ V15_BAE (seção 4); saida/pacote/pacote.json v1.11 (itens das três folhas, e os 560 itens para a busca de repetição); saida/gce/L3_reforco_onda4_A_v3.md (modelo de formato); todos os saida/gce/*reforco*.md e GCE_Lote*.md; saida/gcb/*reforco*.md.

**Bases.** Todas as páginas e arquivos abaixo foram abertos em 18/10/2026 (HTTP 200) e baixados com curl/urllib; cada trecho literal citado nas justificativas e no mapa foi conferido por script contra o texto baixado nesse dia (espaços normalizados). Nenhuma data de verificação anterior foi usada (D-FONTE-DATA-ANTERIOR não é invocada). Nenhum item cita dispositivo legal nem norma da Câmara: a parte não vai ao qa-normativo. As páginas do Google trazem a data "Last updated" registrada na tabela de proveniência; as da AWS e as do repositório de código não exibem data; nas páginas do Microsoft Learn a data de atualização não ficou legível na extração e fica registrada assim.

**Verificação de não repetição.** (1) Script próprio, somente leitura: sequências de 6 palavras do enunciado e da justificativa de cada item (texto normalizado, sem acento) e trechos literais de 30 ou mais caracteres das bases, contra os 560 itens de saida/pacote/pacote.json v1.11 (enunciado e justificativa), todos os saida/gce/*reforco*.md (inclusive a onda 4, L3_reforco_onda4_A/B/C), saida/gce/GCE_Lote*.md e saida/gcb/*reforco*.md. Resultado final: nenhum trecho literal de base repetido; as únicas coincidências de 6 palavras são fórmulas de remissão ("segundo a documentação do…", "o item aplica a regra a…", "nota de transparência do Azure Speech", "transcrição em lote do Azure Speech", "vocabulário personalizado do Amazon Transcribe", "contagens mínima e máxima de falantes"). (2) Candidatos descartados nessa busca por repetirem ponto ou trecho de item existente ou de rascunho: ruído e ganho automático do Google (L1-R24, L1-R125), codec e reamostragem (L1-R23, L1-R118, L1-R25, L1-R121), classe personalizada do Google (L2-R119), dados de treinamento e de ajuste do Amazon Transcribe (L2-R17, L2-R123, L2-R124), região do vocabulário (L2-R125), diarização acumulada do Google (L2-R70), pontuação falada × automática do Azure (L1-Q11, rascunho L1-R87 da v1), pontuação mesclada às palavras do Whisper (rascunho L1-R80 da v1), usos da adaptação "ruído ou áudio pouco claro" e "frase de várias palavras" (onda 3, parte D, e T106), advertência de imprecisão (L2-R23) e de equidade (onda 4, parte C). (3) Pontos conferidos por leitura contra os 20 itens existentes de cada folha. Proximidades registradas, com o ponto distinto: L1-R181 (normalizador básico do Whisper: o que o código faz com pontuação e caixa) × L1-R81 e L1-R85 (TER × WER no Azure); L1-R168 e L1-R170 (limites de canal de dois fornecedores) × L1-R69 (canais na transcrição rápida do Azure); L1-R167 (WDER) × L1-R09/L1-R61 (DER); L1-R187, L1-R190 (efeito da adaptação, igualdade de probabilidade sem boost) × L1-R97 e L1-R102 (sentido do boost e alcance sobre a frase); L1-R188 (descrição dos dados de treinamento, nota de transparência) × L1-R98 (desempenho desigual entre sotaques, Whisper).

Legenda dos formatos: D = definição; TSj = troca de sujeito; SH = situação hipotética; NP = número ou prazo; PC = par confundível; AP = aplicação parlamentar. Critério de classificação: o da T91_reconciliacao, seção 3.1 (o formato segue a construção do ponto, e não o gabarito; o formato de um item C é o da sua contraparte E). Legenda do [TS]: troca sutil de um único conceito; em item C, a convenção "espelho" (a versão verdadeira de uma troca sutil, com o contraste à vista), declarada na justificativa. Os 20 itens existentes de cada folha foram classificados por esta produtora pelo mesmo critério (o mapa dos arquivos de reforço anteriores onde existe: L1-R07 a R12 e R61 a R102; os itens L1-Q e L1C-Q, e L1-R65, R67 a R69, pela leitura).

**Tabela formato × existentes × novos × total (teto de 9 por formato na folha de 30).**

P2-1.4

| formato | existentes | novos | total | % da folha |
|---|--:|--:|--:|--:|
| D | 4 | 0 | 4 | 13.3% |
| TSj | 4 | 2 | 6 | 20.0% |
| SH | 4 | 4 | 8 | 26.7% |
| NP | 2 | 2 | 4 | 13.3% |
| PC | 2 | 1 | 3 | 10.0% |
| AP | 4 | 1 | 5 | 16.7% |
| total | 20 | 10 | 30 | 100% |

P2-1.5

| formato | existentes | novos | total | % da folha |
|---|--:|--:|--:|--:|
| D | 3 | 4 | 7 | 23.3% |
| TSj | 5 | 1 | 6 | 20.0% |
| SH | 4 | 2 | 6 | 20.0% |
| NP | 2 | 0 | 2 | 6.7% |
| PC | 2 | 2 | 4 | 13.3% |
| AP | 4 | 1 | 5 | 16.7% |
| total | 20 | 10 | 30 | 100% |

P2-1.6

| formato | existentes | novos | total | % da folha |
|---|--:|--:|--:|--:|
| D | 6 | 1 | 7 | 23.3% |
| TSj | 5 | 2 | 7 | 23.3% |
| SH | 4 | 4 | 8 | 26.7% |
| NP | 0 | 2 | 2 | 6.7% |
| PC | 1 | 1 | 2 | 6.7% |
| AP | 4 | 0 | 4 | 13.3% |
| total | 20 | 10 | 30 | 100% |

Legado registrado: nenhuma folha passa de 8 itens de um mesmo formato (26,7%); o teto de 30% (9 de 30) é cumprido nas três.

=====================================================================
PARTE 1/3 — MAPA
=====================================================================

| id | folha | ponto de julgamento | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL | aderência |
|---|---|---|---|---|---|---|
| L1-R162 | P2-1.4 | Se a mídia tem mais falantes que o número máximo informado para a partição, vários falantes são tratados como um só | SH | AWS, Amazon Transcribe API Reference, "Settings" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/APIReference/API_Settings.html; verificado em 18/10/2026) | n | direta |
| L1-R163 | P2-1.4 | Motivo da remoção de um colar em torno das fronteiras de turno na avaliação: a imprecisão das anotações manuais, e não a dos sistemas | TSj | pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) (https://pyannote.github.io/pyannote-metrics/reference.html; verificado em 18/10/2026) | n | direta |
| L1-R164 | P2-1.4 | Denominador da DER: soma, sobre todos os falantes, da duração da fala de referência, e não a duração do arquivo | NP | pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) (https://pyannote.github.io/pyannote-metrics/reference.html; verificado em 18/10/2026) | n | direta |
| L1-R165 | P2-1.4 | Os nomes dos rótulos do sistema não precisam coincidir com os da referência: a DER usa mapeamento um a um entre falantes, na versão ótima pelo algoritmo húngaro | SH | pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) (https://pyannote.github.io/pyannote-metrics/reference.html; verificado em 18/10/2026) | n | direta |
| L1-R166 | P2-1.4 | Segmentação excessiva dá alta pureza e baixa cobertura; subsegmentação (dois falantes fundidos) dá baixa pureza e cobertura maior | PC | pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) (https://pyannote.github.io/pyannote-metrics/reference.html; verificado em 18/10/2026) | n | direta |
| L1-R167 | P2-1.4 | Métrica de qualidade da diarização no Azure Speech: WDER (taxa de erro de diarização por palavra), e não o WER | TSj | Microsoft Learn, Azure Speech, "Transparency note: speech to text" (data de atualização não legível na extração) (https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note; verificado em 18/10/2026) | n | direta |
| L1-R168 | P2-1.4 | Na transcrição em lote do Azure Speech, a diarização espera gravação em canal único (mono) e não está disponível em gravações estéreo | SH | Microsoft Learn, Azure Speech, "Create a batch transcription" (data de atualização não legível na extração) (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription-create; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R169 | P2-1.4 | Com três ou mais falantes esperados, o Azure Speech em lote exige a propriedade diarization com contagens mínima e máxima; para dois falantes, habilitar basta | SH | Microsoft Learn, Azure Speech, "Create a batch transcription" (data de atualização não legível na extração) (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription-create; verificado em 18/10/2026) | n | direta |
| L1-R170 | P2-1.4 | A identificação de canais do Amazon Transcribe não admite áudio com mais de dois canais | NP | AWS, Amazon Transcribe Developer Guide, "Transcribing multi-channel audio" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R171 | P2-1.4 | Modelo de diarização que aceita trechos de áudio de referência de falantes conhecidos, com nomes, para associar os segmentos a esses falantes | AP | OpenAI, Speech to text (guia da API), seção "Speaker diarization" (sem data de atualização na página) (https://developers.openai.com/api/docs/guides/speech-to-text; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R172 | P2-1.5 | Para cada palavra, o modelo de pontuação e capitalização prevê a marca que se segue à palavra e se ela deve ser capitalizada | D | NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst; verificado em 18/10/2026) | n | direta |
| L1-R173 | P2-1.5 | Por padrão, o modelo considera só vírgulas, pontos e interrogações; outros sinais exigem novos rótulos | AP | NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst; verificado em 18/10/2026) | n | direta |
| L1-R174 | P2-1.5 | Na restauração por segmentos de texto longo, o desempenho é pior perto das bordas dos segmentos; o parâmetro margin descarta essas previsões | SH | NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst; verificado em 18/10/2026) | n | direta |
| L1-R175 | P2-1.5 | O modelo é composto de dois classificadores de token treinados em conjunto sobre um modelo de linguagem pré-treinado e opera sobre texto | D | NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst; verificado em 18/10/2026) | n | direta |
| L1-R176 | P2-1.5 | A avaliação do modelo gera dois relatórios de classificação (capitalização e pontuação) com precisão, revocação e F1, e não um relatório de WER | PC | NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst; verificado em 18/10/2026) | n | direta |
| L1-R177 | P2-1.5 | Quando os segmentos se sobrepõem, as probabilidades de um token presente em mais de um segmento são multiplicadas (e não somadas) antes da escolha do melhor candidato | TSj | NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst; verificado em 18/10/2026) | n | direta |
| L1-R178 | P2-1.5 | Por padrão o Google Speech-to-Text não inclui pontuação nos resultados; a pontuação automática precisa ser solicitada | D | Google Cloud, "Enable automatic punctuation" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/automatic-punctuation; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R179 | P2-1.5 | Para treinar o modelo de pontuação e capitalização, recomenda-se balancear os dados, sobretudo para a tarefa de pontuação | D | NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst; verificado em 18/10/2026) | n | direta |
| L1-R180 | P2-1.5 | Na legenda ao vivo com o Azure Speech, a pontuação dos resultados parciais não está disponível | SH | Microsoft Learn, Azure Speech, "Captioning with speech to text" (data de atualização não legível na extração) (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/captioning-concepts; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R181 | P2-1.5 | O normalizador básico de texto do Whisper converte para minúsculas e troca símbolos e pontuação por espaço, de modo que o texto normalizado não distingue pontuação nem caixa | PC | OpenAI, repositório oficial openai/whisper, whisper/normalizers/basic.py (ramo main) (https://raw.githubusercontent.com/openai/whisper/main/whisper/normalizers/basic.py; verificado em 18/10/2026) | n | direta |
| L1-R182 | P2-1.6 | O Whisper detecta o idioma uma vez, com base em até os primeiros 30 s, quando o idioma não é informado | SH | OpenAI, repositório oficial openai/whisper, whisper/transcribe.py (ramo main) (https://raw.githubusercontent.com/openai/whisper/main/whisper/transcribe.py; verificado em 18/10/2026) | n | direta |
| L1-R183 | P2-1.6 | Na tabela de vocabulário personalizado do Amazon Transcribe, SoundsLike e IPA não são mais suportados | TSj | AWS, Amazon Transcribe Developer Guide, "Creating custom vocabulary tables" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-table.html; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R184 | P2-1.6 | Com modelo de linguagem personalizado ativo na mesma requisição, o DisplayAs do vocabulário personalizado não é aplicado | SH | AWS, Amazon Transcribe Developer Guide, "Improving transcription accuracy with custom vocabularies and custom language models" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/improving-accuracy.html; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R185 | P2-1.6 | Ao incluir um modelo de linguagem personalizado na requisição, não se pode habilitar a identificação de idioma | SH | AWS, Amazon Transcribe Developer Guide, "Custom language models" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R186 | P2-1.6 | Com mais de 10.000 palavras de transcrição precisa do domínio, usar tudo como treinamento, sem dados de ajuste | NP | AWS, Amazon Transcribe Developer Guide, "Custom language models" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R187 | P2-1.6 | Por padrão, a adaptação de modelo do Google tem efeito relativamente pequeno, sobretudo em frases de uma palavra | TSj | Google Cloud, "Improve transcription results with model adaptation" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/adaptation-model; verificado em 18/10/2026) | n | direta |
| L1-R188 | P2-1.6 | Os modelos de fala são treinados com dados que incluem diversos estilos de fala, sotaques, dialetos e entonações e variações acústicas de dispositivos de gravação | D | Microsoft Learn, Azure Speech, "Transparency note: speech to text" (data de atualização não legível na extração) (https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note; verificado em 18/10/2026) | n | direta |
| L1-R189 | P2-1.6 | A lista de idiomas do Whisper de código aberto traz um único código para o português (pt), sem variante brasileira | PC | OpenAI, repositório oficial openai/whisper, whisper/tokenizer.py (ramo main) (https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py; verificado em 18/10/2026) | n | direta |
| L1-R190 | P2-1.6 | Sem boost, as palavras da frase de adaptação são reconhecidas com igual probabilidade | SH | Google Cloud, "Improve transcription results with model adaptation" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/adaptation-model; verificado em 18/10/2026) | n | direta |
| L1-R191 | P2-1.6 | A detecção automática de idioma do SDK identifica só um entre quatro locais especificados; a aplicação ainda precisa conhecer o local falado | NP | Microsoft Learn, Azure Speech, "Transparency note: speech to text" (data de atualização não legível na extração) (https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note; verificado em 18/10/2026) | VOLÁTIL baixo | direta |

=====================================================================
PARTE 2/3 — (d) ITENS DO ESTUDANTE
=====================================================================

Julgue o item.

**L1-R162** (P2-1.4)
Uma comissão grava a reunião em um único arquivo, com 14 oradores distintos, e a equipe configura o Amazon Transcribe para a partição de falantes com o máximo de 10 falantes. Nessa situação, segundo a documentação do serviço, como a mídia tem mais falantes que o número especificado, vários falantes são tratados como um único falante.

**L1-R163** (P2-1.4)
Na avaliação de sistemas de diarização, é comum remover da avaliação uma faixa (colar) em torno de cada fronteira de turno de fala, porque os sistemas automáticos não conseguem determinar essas fronteiras com precisão no nível da amostra de áudio.

**L1-R164** (P2-1.4)
Considere um arquivo de 100 s em que a fala de referência soma 80 s. Um sistema de diarização apresentou 4 s de falso alarme, 2 s de fala perdida e 6 s de confusão de falantes. Nessa situação, segundo a definição de DER da documentação do pyannote.metrics, a DER é de 12%, resultado de 12 s de erro divididos pelos 100 s de duração do arquivo.

**L1-R165** (P2-1.4)
Na avaliação de um sistema de diarização, o sistema rotulou como spk_0 o orador que a anotação de referência chama de Presidente. Nessa situação, a diferença entre os nomes dos rótulos não constitui, por si só, erro de confusão, pois a DER se apoia em um mapeamento um a um entre os falantes da referência e os do sistema, que, na versão ótima, é calculado pelo algoritmo húngaro de modo a minimizar a confusão.

**L1-R166** (P2-1.4)
Segundo a documentação do pyannote.metrics, resultados com segmentação excessiva (muitos agrupamentos de falantes) tendem a produzir alta cobertura e baixa pureza, ao passo que resultados com subsegmentação (dois falantes fundidos em um grande agrupamento) levam a alta pureza e cobertura menor.

**L1-R167** (P2-1.4)
Segundo a nota de transparência do Azure Speech, a qualidade da diarização é medida pela taxa de erro de palavras (WER), de modo que o serviço não adota métrica específica para a atribuição das palavras aos falantes.

**L1-R168** (P2-1.4)
Uma equipe envia à transcrição em lote do Azure Speech, com a diarização habilitada, um arquivo estéreo que traz dois oradores. Nessa situação, segundo a documentação, a diarização é aplicada normalmente, pois o recurso foi concebido para gravações com mais de um canal.

**L1-R169** (P2-1.4)
Uma equipe prepara a transcrição em lote, no Azure Speech, de uma audiência com cinco participantes. Nessa situação, segundo a documentação, habilitar a diarização não basta: é preciso informar também as contagens mínima e máxima de falantes, ao passo que, para dois falantes, habilitar a diarização é suficiente.

**L1-R170** (P2-1.4)
O sistema de som de um comitê grava o áudio, com um microfone por canal, em um arquivo de quatro canais. Nessa situação, segundo a documentação do Amazon Transcribe, a identificação de canais pode ser usada para transcrever separadamente cada um dos quatro canais.

**L1-R171** (P2-1.4)
Para que a transcrição de uma audiência exiba o nome do presidente da sessão, a API de transcrição da OpenAI, no modelo especializado em diarização, aceita o envio de trechos curtos de áudio de referência de falantes conhecidos, acompanhados dos respectivos nomes, para associar os segmentos de fala a esses falantes.

**L1-R172** (P2-1.5)
No modelo de pontuação e capitalização documentado pelo NeMo, para cada palavra do texto de entrada o modelo prevê a marca de pontuação que deve preceder a palavra e se ela deve ser grafada com inicial maiúscula.

**L1-R173** (P2-1.5)
Segundo a documentação do NeMo, por padrão o modelo de pontuação e capitalização considera vírgulas, pontos finais e pontos de interrogação, tendo os demais sinais sido removidos dos dados; para que sinais como o ponto e vírgula e os dois-pontos fossem restaurados em transcrições, seria preciso introduzir novos rótulos.

**L1-R174** (P2-1.5)
Uma equipe usa o script de inferência de pontuação e capitalização do NeMo em um texto de transcrição muito longo. Nessa situação, segundo a documentação, o texto é dividido em segmentos, e a divisão melhora o desempenho do modelo junto às bordas dos segmentos, razão pela qual o parâmetro margin serve para reforçar as previsões feitas nessas bordas.

**L1-R175** (P2-1.5)
O modelo de pontuação e capitalização do NeMo é composto de dois classificadores no nível de token, um para a pontuação e outro para a capitalização, treinados em conjunto sobre um modelo de linguagem pré-treinado, e opera sobre texto, e não sobre o sinal de áudio.

**L1-R176** (P2-1.5)
A avaliação do modelo de pontuação e capitalização do NeMo gera um único relatório de taxa de erro de palavras (WER), que cobre ao mesmo tempo a pontuação e a capitalização.

**L1-R177** (P2-1.5)
Segundo a documentação do NeMo, no script de inferência de pontuação e capitalização, quando os segmentos de um texto longo se sobrepõem, as probabilidades previstas para um token presente em mais de um segmento são somadas antes da escolha do melhor candidato.

**L1-R178** (P2-1.5)
Segundo a documentação do Google Cloud Speech-to-Text, por padrão o serviço já insere pontuação nos resultados do reconhecimento, de modo que a pontuação automática precisa ser desabilitada quando não for desejada.

**L1-R179** (P2-1.5)
Segundo a documentação do NeMo, no treinamento do modelo de pontuação e capitalização recomenda-se balancear os dados, especialmente para a tarefa de pontuação.

**L1-R180** (P2-1.5)
Em legenda ao vivo de uma sessão produzida com o Azure Speech, a equipe percebe que os resultados parciais (evento Recognizing) chegam sem pontuação. Segundo a documentação do serviço, isso é esperado, pois a pontuação dos resultados parciais não está disponível.

**L1-R181** (P2-1.5)
O normalizador de texto básico do repositório oficial do Whisper, usado para uniformizar textos antes de compará-los, converte o texto em minúsculas e substitui por espaço símbolos e sinais de pontuação; por isso, uma comparação feita sobre textos assim normalizados não distingue diferenças de pontuação nem de capitalização.

**L1-R182** (P2-1.6)
Uma sessão do Plenário começa em português e, em certo momento, um convidado passa a falar em espanhol. Se o idioma não for informado ao Whisper de código aberto, segundo o código de referência, o modelo detecta o idioma a cada janela de 30 segundos, o que faz o trecho em espanhol ser transcrito como espanhol.

**L1-R183** (P2-1.6)
Para melhorar o reconhecimento de siglas da Casa, a equipe pode preencher, na tabela de vocabulário personalizado do Amazon Transcribe, as colunas SoundsLike e IPA, que o serviço usa para orientar a pronúncia dos termos.

**L1-R184** (P2-1.6)
Uma equipe do Amazon Transcribe envia, na mesma requisição, um modelo de linguagem personalizado e um vocabulário personalizado com formas de exibição (DisplayAs) para siglas da Casa. Nessa situação, segundo a documentação, as formas de exibição do vocabulário não são aplicadas à saída enquanto o modelo de linguagem personalizado estiver ativo.

**L1-R185** (P2-1.6)
Uma equipe pretende usar, na transcrição de audiências, um modelo de linguagem personalizado do Amazon Transcribe e, ao mesmo tempo, a identificação automática de idioma. Nessa situação, segundo a documentação, ao se incluir um modelo de linguagem personalizado na requisição não é possível habilitar a identificação de idioma, sendo preciso especificar o código do idioma.

**L1-R186** (P2-1.6)
Uma equipe dispõe de 15.000 palavras de transcrições precisas de sessões, do próprio domínio, para criar um modelo de linguagem personalizado do Amazon Transcribe. Nessa situação, segundo a documentação, o ideal é usar esse texto como dados de treinamento, sem necessidade de incluir dados de ajuste.

**L1-R187** (P2-1.6)
Segundo a documentação do Google Cloud Speech-to-Text, a adaptação de modelo tem, por padrão, efeito forte sobre o reconhecimento, sobretudo para frases de uma só palavra.

**L1-R188** (P2-1.6)
Segundo a nota de transparência do Azure Speech, os modelos de fala são treinados com dados de voz que incluem diversos estilos de fala, idiomas, sotaques, dialetos e entonações, além de variações acústicas geradas por diferentes tipos de dispositivos de gravação.

**L1-R189** (P2-1.6)
A lista de idiomas do Whisper de código aberto traz códigos de idioma distintos para o português do Brasil e para o português de Portugal, o que permite informar ao modelo a variante regional da fala a ser transcrita.

**L1-R190** (P2-1.6)
Uma equipe do Google Cloud Speech-to-Text inclui sessão e seção em um conjunto de frases de adaptação, sem atribuir valores de boost. Nessa situação, segundo a documentação, o modelo passa a reconhecer sessão com probabilidade maior que seção.

**L1-R191** (P2-1.6)
Segundo a nota de transparência do Azure Speech, o SDK oferece detecção automática de idioma, mas esta identifica apenas um entre quatro locais especificados em tempo de execução, de modo que a aplicação ainda precisa conhecer o local que os usuários falarão.

=====================================================================
PARTE 3/3 — (d-G) GABARITO COMENTADO
=====================================================================

**L1-R162** (P2-1.4) Gabarito: C.
Justificativa: Documentação do campo MaxSpeakerLabels: "if your media contains more speakers than the specified number, multiple speakers are treated as a single speaker". O item aplica a regra ao caso de 14 oradores com limite de 10 (C espelho).
Base: AWS, Amazon Transcribe API Reference, "Settings" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/APIReference/API_Settings.html), seção/ponto: campo MaxSpeakerLabels; verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R163** (P2-1.4) Gabarito: E. [TS]
Justificativa: Segundo a documentação, "Because manual annotations cannot be precise at the audio sample level", é comum remover da avaliação um colar em torno de cada fronteira de turno de fala. O item troca a causa (anotações manuais, que servem de referência) pela imprecisão dos sistemas automáticos.
Base: pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) (https://pyannote.github.io/pyannote-metrics/reference.html), seção/ponto: seção sobre colar (collar); verificado em 18/10/2026. Não VOLÁTIL. Formato: TSj.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R164** (P2-1.4) Gabarito: E. [TS]
Justificativa: Na definição da documentação, a DER é a soma de falso alarme, detecção perdida e confusão dividida por "total", que é "the sum over all speakers of their reference speech duration"; logo, 12 s divididos por 80 s resultam em 15%. O item troca o denominador (fala de referência) pela duração do arquivo, o que daria 12%.
Base: pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) (https://pyannote.github.io/pyannote-metrics/reference.html), seção/ponto: seção "Diarization error rate"; verificado em 18/10/2026. Não VOLÁTIL. Formato: NP.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R165** (P2-1.4) Gabarito: C.
Justificativa: A documentação informa que a DER depende de um "one-to-one mapping between reference and hypothesized speakers" e que a versão ótima "uses the Hungarian algorithm to compute the mapping that minimize the confusion term". O item aplica a regra ao caso de rótulos com nomes diferentes (C espelho).
Base: pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) (https://pyannote.github.io/pyannote-metrics/reference.html), seção/ponto: seção "Optimal vs. greedy"; verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R166** (P2-1.4) Gabarito: E. [TS]
Justificativa: Segundo a documentação, a segmentação excessiva tende a "high purity and low coverage", e a subsegmentação, a "low purity and higher coverage". O item inverte, nos dois casos, o efeito sobre a pureza e a cobertura.
Base: pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) (https://pyannote.github.io/pyannote-metrics/reference.html), seção/ponto: seção sobre pureza e cobertura (purity e coverage); verificado em 18/10/2026. Não VOLÁTIL. Formato: PC.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R167** (P2-1.4) Gabarito: E. [TS]
Justificativa: A nota de transparência afirma: "For diarization, we measure the quality by using word diarization error rate (WDER)", e que, quanto menor o WDER, melhor a diarização. O item troca a métrica específica (WDER) pelo WER.
Base: Microsoft Learn, Azure Speech, "Transparency note: speech to text" (data de atualização não legível na extração) (https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note), seção/ponto: seção "System performance"; verificado em 18/10/2026. Não VOLÁTIL. Formato: TSj.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R168** (P2-1.4) Gabarito: E.
Justificativa: Segundo a documentação da propriedade diarization, a entrada é "expected to be a mono channel that contains multiple voices" e "The feature isn't available with stereo recordings". O item afirma que o recurso se aplica a gravações com mais de um canal.
Base: Microsoft Learn, Azure Speech, "Create a batch transcription" (data de atualização não legível na extração) (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription-create), seção/ponto: propriedade diarization; verificado em 18/10/2026. VOLÁTIL baixo. Formato: SH.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R169** (P2-1.4) Gabarito: C.
Justificativa: A documentação diz: "You need to use this property when you expect three or more speakers. For two speakers, setting diarizationEnabled property to true is enough." O item aplica a regra a uma audiência de cinco participantes (C espelho).
Base: Microsoft Learn, Azure Speech, "Create a batch transcription" (data de atualização não legível na extração) (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription-create), seção/ponto: propriedades diarization e diarizationEnabled; verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R170** (P2-1.4) Gabarito: E. [TS]
Justificativa: A documentação informa que, com dois canais, é possível transcrever a fala de cada canal separadamente, e que o "Amazon Transcribe doesn't currently support audio with more than two channels". O item troca o limite de dois canais por quatro.
Base: AWS, Amazon Transcribe Developer Guide, "Transcribing multi-channel audio" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html), seção/ponto: abertura da página; verificado em 18/10/2026. VOLÁTIL baixo. Formato: NP.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R171** (P2-1.4) Gabarito: C.
Justificativa: A documentação informa: "You can optionally supply up to four short audio references with known_speaker_names[] and known_speaker_references[] to map segments onto known speakers". O item aplica o recurso ao caso do nome do presidente da sessão (C espelho).
Base: OpenAI, Speech to text (guia da API), seção "Speaker diarization" (sem data de atualização na página) (https://developers.openai.com/api/docs/guides/speech-to-text), seção/ponto: seção "Speaker diarization"; verificado em 18/10/2026. VOLÁTIL baixo. Formato: AP.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R172** (P2-1.5) Gabarito: E. [TS]
Justificativa: Segundo a documentação, para cada palavra o modelo "predicts a punctuation mark that should follow the word (if any)" e "predicts if the word should be capitalized or not". O item troca a marca que se segue à palavra pela que a precede.
Base: NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst), seção/ponto: seção "Model Description"; verificado em 18/10/2026. Não VOLÁTIL. Formato: D.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R173** (P2-1.5) Gabarito: C.
Justificativa: A documentação informa que "By default, the following punctuation marks are considered: commas, periods, and question marks", e que "This can be changed by introducing new labels". O item aplica a regra ao ponto e vírgula e aos dois-pontos (C espelho).
Base: NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst), seção/ponto: seção "Raw Data Format"; verificado em 18/10/2026. Não VOLÁTIL. Formato: AP.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R174** (P2-1.5) Gabarito: E. [TS]
Justificativa: A documentação afirma que a divisão em segmentos leva a desempenho pior "near edges of segments" e que o parâmetro margin serve para descartar ("discard") as probabilidades previstas para os tokens "near segment edges". O item inverte o efeito da divisão (melhora, e não piora) e a função do margin (reforçar, e não descartar).
Base: NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst), seção/ponto: seção "Inference"; verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R175** (P2-1.5) Gabarito: C.
Justificativa: A documentação descreve "two token-level classifiers on top of a pre-trained" modelo de linguagem, treinados em conjunto, e informa que o modelo "can work with any text dataset". O item reúne as duas características documentadas (C espelho).
Base: NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst), seção/ponto: seção "Model Description"; verificado em 18/10/2026. Não VOLÁTIL. Formato: D.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R176** (P2-1.5) Gabarito: E. [TS]
Justificativa: Segundo a documentação, a avaliação gera "two classification reports: one for capitalization task and another one for punctuation task", com as métricas Precision, Recall e F1. O item troca os dois relatórios de classificação por um único relatório de WER.
Base: NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst), seção/ponto: seção "Model Evaluation"; verificado em 18/10/2026. Não VOLÁTIL. Formato: PC.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R177** (P2-1.5) Gabarito: E. [TS]
Justificativa: A documentação informa que, se os segmentos se sobrepõem, "predicted probabilities for a token present in several segments are multiplied" antes da escolha do melhor candidato. O item troca a multiplicação das probabilidades pela soma.
Base: NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst), seção/ponto: seção "Inference"; verificado em 18/10/2026. Não VOLÁTIL. Formato: TSj.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R178** (P2-1.5) Gabarito: E. [TS]
Justificativa: A documentação afirma que "By default, Speech-to-Text does not include punctuation marks in the results from speech recognition", sendo necessário solicitar a inserção automática. O item troca o padrão (sem pontuação) pelo oposto.
Base: Google Cloud, "Enable automatic punctuation" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/automatic-punctuation), seção/ponto: abertura da página; verificado em 18/10/2026. VOLÁTIL baixo. Formato: D.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R179** (P2-1.5) Gabarito: C.
Justificativa: A documentação informa que o modelo "can work with any text dataset, although it is recommended to balance the data, especially for the punctuation task". O item reproduz a recomendação documentada (C espelho).
Base: NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst), seção/ponto: seção "Raw Data Format"; verificado em 18/10/2026. Não VOLÁTIL. Formato: D.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R180** (P2-1.5) Gabarito: C.
Justificativa: A documentação sobre legendas registra a nota: "Punctuation of partial results isn't available." O item aplica a nota ao caso da legenda ao vivo (C espelho).
Base: Microsoft Learn, Azure Speech, "Captioning with speech to text" (data de atualização não legível na extração) (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/captioning-concepts), seção/ponto: seção "Get partial results"; verificado em 18/10/2026. VOLÁTIL baixo. Formato: SH.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R181** (P2-1.5) Gabarito: C.
Justificativa: No código do normalizador, "s = s.lower()" e a função de limpeza "Replace any other markers, symbols, punctuations with a space". O item extrai a consequência para a comparação de textos normalizados (C espelho).
Base: OpenAI, repositório oficial openai/whisper, whisper/normalizers/basic.py (ramo main) (https://raw.githubusercontent.com/openai/whisper/main/whisper/normalizers/basic.py), seção/ponto: classe BasicTextNormalizer; verificado em 18/10/2026. Não VOLÁTIL. Formato: PC.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R182** (P2-1.6) Gabarito: E. [TS]
Justificativa: O código de referência registra: "Detecting language using up to the first 30 seconds. Use `--language` to specify the language". O item troca a detecção única, com base nos primeiros 30 segundos, pela detecção a cada janela.
Base: OpenAI, repositório oficial openai/whisper, whisper/transcribe.py (ramo main) (https://raw.githubusercontent.com/openai/whisper/main/whisper/transcribe.py), seção/ponto: função transcribe(); verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R183** (P2-1.6) Gabarito: E. [TS]
Justificativa: A documentação informa: "SoundsLike is no longer supported for Custom Vocabulary" e "IPA is no longer supported for Custom Vocabulary", devendo as colunas ficar vazias. O item afirma que o serviço usa as duas colunas, o que a documentação nega.
Base: AWS, Amazon Transcribe Developer Guide, "Creating custom vocabulary tables" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-table.html), seção/ponto: seção sobre as colunas da tabela; verificado em 18/10/2026. VOLÁTIL baixo. Formato: TSj.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R184** (P2-1.6) Gabarito: C.
Justificativa: A documentação alerta: "Custom vocabulary features (such as the DisplayAs field) are not applied to transcription output when a custom language model is active in the same request". O item aplica o alerta ao caso das siglas da Casa (C espelho).
Base: AWS, Amazon Transcribe Developer Guide, "Improving transcription accuracy with custom vocabularies and custom language models" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/improving-accuracy.html), seção/ponto: nota "Important"; verificado em 18/10/2026. VOLÁTIL baixo. Formato: SH.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R185** (P2-1.6) Gabarito: C.
Justificativa: A documentação alerta: "if you include a custom language model in your request, you can't enable language identification (you must specify a language code)". O item aplica o alerta ao caso de uso simultâneo dos dois recursos (C espelho).
Base: AWS, Amazon Transcribe Developer Guide, "Custom language models" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html), seção/ponto: abertura da página; verificado em 18/10/2026. VOLÁTIL baixo. Formato: SH.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R186** (P2-1.6) Gabarito: C.
Justificativa: A documentação orienta: "If you have more than 10,000 words of accurate, in-domain transcript text, use it as training data. In this case, there is no need to include tuning data." O item aplica o limite de 10.000 palavras ao caso de 15.000 palavras (C espelho).
Base: AWS, Amazon Transcribe Developer Guide, "Custom language models" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html), seção/ponto: seção "Training versus tuning data"; verificado em 18/10/2026. VOLÁTIL baixo. Formato: NP.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R187** (P2-1.6) Gabarito: E. [TS]
Justificativa: A documentação afirma: "By default model adaptation provides a relatively small effect, especially for one-word phrases". O item troca o efeito relativamente pequeno por efeito forte.
Base: Google Cloud, "Improve transcription results with model adaptation" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/adaptation-model), seção/ponto: seção "Fine-tune transcription results using boost"; verificado em 18/10/2026. Não VOLÁTIL. Formato: TSj.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R188** (P2-1.6) Gabarito: C.
Justificativa: A nota de transparência afirma: "Speech models are trained on voice data that includes various speech styles, languages, accents, dialects, and intonations, and on acoustic variations that are generated by using different types of recording devices". O item reproduz a descrição dos dados de treinamento (C espelho).
Base: Microsoft Learn, Azure Speech, "Transparency note: speech to text" (data de atualização não legível na extração) (https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note), seção/ponto: glossário (speech model); verificado em 18/10/2026. Não VOLÁTIL. Formato: D.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R189** (P2-1.6) Gabarito: E. [TS]
Justificativa: No arquivo de idiomas do repositório, o português consta com um único código: "pt": "portuguese". O item afirma haver códigos distintos para as variantes do Brasil e de Portugal.
Base: OpenAI, repositório oficial openai/whisper, whisper/tokenizer.py (ramo main) (https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py), seção/ponto: dicionário LANGUAGES; verificado em 18/10/2026. Não VOLÁTIL. Formato: PC.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R190** (P2-1.6) Gabarito: E. [TS]
Justificativa: No exemplo de "fair" e "fare" da documentação: "Without boost values, the recognition model will recognize" as duas palavras "with equal probability". O item troca a igualdade de probabilidade por probabilidade maior para uma das palavras.
Base: Google Cloud, "Improve transcription results with model adaptation" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/adaptation-model), seção/ponto: seção "Fine-tune transcription results using boost"; verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R191** (P2-1.6) Gabarito: C.
Justificativa: A nota de transparência afirma que o SDK "supports automatic language detection", mas que "it detects only one out of four locales that are specified at runtime", e que ainda é preciso saber o local falado. O item reproduz a limitação documentada (C espelho).
Base: Microsoft Learn, Azure Speech, "Transparency note: speech to text" (data de atualização não legível na extração) (https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note), seção/ponto: seção "Best practices for improving system performance"; verificado em 18/10/2026. VOLÁTIL baixo. Formato: NP.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

### Tabela de proveniência

| fonte | URL | data de verificação | usada em |
|---|---|---|---|
| AWS, Amazon Transcribe API Reference, "Settings" (a página não exibe data de atualização) | https://docs.aws.amazon.com/transcribe/latest/APIReference/API_Settings.html | 18/10/2026 | R162 |
| pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) | https://pyannote.github.io/pyannote-metrics/reference.html | 18/10/2026 | R163, R164, R165, R166 |
| Microsoft Learn, Azure Speech, "Transparency note: speech to text" (data de atualização não legível na extração) | https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note | 18/10/2026 | R167, R188, R191 |
| Microsoft Learn, Azure Speech, "Create a batch transcription" (data de atualização não legível na extração) | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription-create | 18/10/2026 | R168, R169 |
| AWS, Amazon Transcribe Developer Guide, "Transcribing multi-channel audio" (a página não exibe data de atualização) | https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html | 18/10/2026 | R170 |
| OpenAI, Speech to text (guia da API), seção "Speaker diarization" (sem data de atualização na página) | https://developers.openai.com/api/docs/guides/speech-to-text | 18/10/2026 | R171 |
| NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) | https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst | 18/10/2026 | R172, R173, R174, R175, R176, R177, R179 |
| Google Cloud, "Enable automatic punctuation" (Last updated 2026-10-13 UTC) | https://docs.cloud.google.com/speech-to-text/docs/automatic-punctuation | 18/10/2026 | R178 |
| Microsoft Learn, Azure Speech, "Captioning with speech to text" (data de atualização não legível na extração) | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/captioning-concepts | 18/10/2026 | R180 |
| OpenAI, repositório oficial openai/whisper, whisper/normalizers/basic.py (ramo main) | https://raw.githubusercontent.com/openai/whisper/main/whisper/normalizers/basic.py | 18/10/2026 | R181 |
| OpenAI, repositório oficial openai/whisper, whisper/transcribe.py (ramo main) | https://raw.githubusercontent.com/openai/whisper/main/whisper/transcribe.py | 18/10/2026 | R182 |
| AWS, Amazon Transcribe Developer Guide, "Creating custom vocabulary tables" (a página não exibe data de atualização) | https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-table.html | 18/10/2026 | R183 |
| AWS, Amazon Transcribe Developer Guide, "Improving transcription accuracy with custom vocabularies and custom language models" (a página não exibe data de atualização) | https://docs.aws.amazon.com/transcribe/latest/dg/improving-accuracy.html | 18/10/2026 | R184 |
| AWS, Amazon Transcribe Developer Guide, "Custom language models" (a página não exibe data de atualização) | https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html | 18/10/2026 | R185, R186 |
| Google Cloud, "Improve transcription results with model adaptation" (Last updated 2026-10-13 UTC) | https://docs.cloud.google.com/speech-to-text/docs/adaptation-model | 18/10/2026 | R187, R190 |
| OpenAI, repositório oficial openai/whisper, whisper/tokenizer.py (ramo main) | https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py | 18/10/2026 | R189 |

Observações de proveniência: (1) o texto de cada página foi baixado em 18/10/2026 (HTTP 200) e os trechos entre aspas foram conferidos por script contra esse texto; (2) as afirmações sobre Whisper (L1-R181, R182, R189), Google Speech-to-Text (L1-R178, R187, R190), Azure Speech (L1-R167, R168, R169, R180, R188, R191), AWS Transcribe (L1-R162, R170, R183 a R186) e sobre a API da OpenAI (L1-R171) têm cada uma a URL oficial e a data acima; as afirmações sobre pyannote.metrics (R163 a R166) e NVIDIA NeMo (R172 a R177, R179) vêm da documentação oficial das próprias ferramentas; (3) nenhuma versão de modelo, preço ou limite numérico foi afirmada sem a fonte datada; os limites citados (dois canais, 10.000 palavras, quatro locais, quatro referências de áudio) estão em itens marcados VOLÁTIL baixo; (4) a documentação do NeMo é a da versão r1.23.0 do repositório oficial (URL fixada na etiqueta), de modo que os itens R172 a R177 e R179 não dependem de página mutável, mas entram na lista de conferência de base de janeiro; (5) nenhum item cita lei, ato ou regimento.

FIM DO LOTE
