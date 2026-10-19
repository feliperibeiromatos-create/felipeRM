# T113_onda1_A_v1.md — T-113 onda 1, parte A (ORDEM F; D-REFORCO-2; D-V15-ENCOMENDA) — 2026-10-18 — gerado por gce-cpp

Objeto. Reforço da onda 1 da ordem F (T-113), parte A, versão 1 (produção). Trinta itens AUTORAL novos nas folhas P2-1.1, P2-1.2 e P2-1.3, dez por folha, ids L1-R132 a L1-R141 (P2-1.1), L1-R142 a L1-R151 (P2-1.2) e L1-R152 a L1-R161 (P2-1.3), exatamente como na D1 da GBQ (seção 4.2) e na D1 da GCE (seção 4, parte A). Cada folha vai de 20 para 30 itens. Nenhum item existente foi alterado. Rótulo AUTORAL em todos. QA PENDENTE em todos (D-QA-PENDENTE): nenhum item passou por QA, e nenhum entra em simulado antes da R1 da gce-cqfp. VOLÁTEIS nunca vão a simulado final.

Lido antes: CLAUDE.md; regras/proveniencia.md; regras/estilo_banca.md; edital/modulo_RF_IA_P2.md (1.1 "Reconhecimento automático de fala (ASR – Automatic Speech Recognition)"; 1.2 "Modelos de fala end-to-end"; 1.3 "LLMs multimodais de áudio nativo"); ordens/ORDEM_V15_F_BANCO40.md; DECISOES.md (D-REFORCO-2, D-FONTE-DATA-ANTERIOR, D-ADERENCIA, D-QA-PENDENTE); saida/gce/V15_BAEF_D1_GCE_2026-10-18.md (seção 4) e saida/pacote/V15_BAE_D1_GBQ_2026-10-18.md (seção 4); saida/pacote/pacote.json v1.11 (os 60 itens vigentes das três folhas e o curso do Lote 1, blocos 1.1 a 1.3); mapas de formato de saida/gce/L1_reforco_onda2_A_v3.md (1.1 e 1.2), L1_reforco_onda2_B_v2.md (1.3) e L1_reforco_onda2_saldo_v2.md (L1-R131); saida/gce/L3_reforco_onda4_A_v3.md (modelo do arquivo).

Aderência. DIRETA em todos os 30: o ponto de cada item incide sobre o texto literal do edital da folha (ASR e métricas de reconhecimento em 1.1; arquitetura, treinamento e decodificação de modelos end-to-end em 1.2; LLM que recebe o áudio como entrada em 1.3). Nenhum item é PARCIAL. Nenhum item cita norma (lei, regimento ou ato): não há dispositivo a enviar ao qa-normativo.

Bases. Todos os 12 documentos e páginas citados foram abertos em 18/10/2026 (HTTP 200; curl com User-Agent de navegador). O artigo do Whisper foi lido no HTML do arXiv e conferido também no PDF oficial, por pdftotext (as diferenças são só de hifenização e de quebra de página). Todos os 43 trechos entre aspas das justificativas foram conferidos por script contra o texto baixado nesse dia (0 ausentes). Nenhuma data anterior de verificação foi usada: a D-FONTE-DATA-ANTERIOR não é invocada. As páginas de fornecedor trazem a data "Last updated" registrada na tabela de proveniência; as do NIST, do CMUSphinx, da AWS e da Mistral AI e os resumos do arXiv não exibem data de atualização. Fontes: artigos do arXiv (Whisper, wav2vec 2.0, AudioPaLM, SALMONN, Qwen2-Audio), documentação do NIST (sclite), do CMUSphinx, do Google Cloud (2 páginas), da Microsoft (1 página), da AWS (Amazon Nova) e da Mistral AI. Concentração por fonte: o maior número de itens numa mesma fonte é o do artigo do Whisper (9 de 30); a Microsoft tem 2 itens; o Google, 3.

Verificação de não repetição. (1) Por script (python -I, somente leitura), as sequências de 6 palavras do enunciado e da justificativa de cada item, e os trechos literais em inglês de 30 ou mais caracteres, foram confrontados com os 560 itens de saida/pacote/pacote.json v1.11 (enunciado e justificativa), com todos os saida/gce/*reforco*.md, saida/gce/GCE_Lote*.md e saida/gcb/*reforco*.md e com as linhas de banco/banco.csv (622 documentos): nenhum trecho-base literal repetido; as únicas coincidências são fórmulas de remissão e nomes de produto ("a documentação do Google Cloud Speech-to-Text", "um serviço de atendimento por voz da Casa", "no pré-treinamento do wav2vec 2.0", "sistema de reconhecimento de fala"). (2) Os pontos foram conferidos item a item, por leitura, contra os 20 existentes de cada folha, entre os 10 novos de cada folha e contra o pacote inteiro, com busca por termo (sclite, utterance, TER, NoMatch, BabbleTimeout, AGC, gzip, nospeech, transcript-ese, AudioPaLM, SALMONN, Q-Former, Qwen, Mistral, Nova, xRT, lattice, N-best, entre outros): sem ocorrência além dos pontos adjacentes declarados abaixo. (3) Pontos candidatos descartados por duplicarem item de outra folha, antes da redação final: a padronização do texto antes do WER (adjacente a L2-R09, L2-R79, L2-R83 a R85, da 2.5); o sclite pontuar só os enunciados presentes na hipótese (igual a L2-R113, da 2.7); a TER cobrir o formato de exibição (igual a L1-R81, da 1.5); as faixas de WER do Azure Speech (igual a L2-R56, da 2.3); o Offset em unidades de 100 ns (igual a L2-R90, da 2.6); o sclite totalizar por locutor (igual a L2-R112, da 2.7). (4) Pontos adjacentes, mantidos por julgarem coisas distintas: L1-R136 (não usar AGC) e L1-R24 (redução de ruído), mesma seção "Audio preprocessing" do Google; L1-R137 (a configuração da requisição descreve o áudio) e L1-R25 (não reamostrar); L1-R151 (tarefa contrastiva do wav2vec 2.0) e L1-R34/L1-R42/L1-R131 (áudio sem rótulos, múltiplos domínios, autotreinamento); L1-R146 (janela e passo do espectrograma) e L1C-Q24 (existência do espectrograma); L1-R142 (texto bruto dispensa ITN no treinamento) e L2-Q17 (ITN como etapa posterior ao reconhecimento); L1-R149 (carimbo de tempo inicial) e L1-R04 (janelas de 30 s); L1-R160 (um arquivo por prompt) e L1-R49/L1-R59 (truncamento e contagem de tokens); L1-R159 (resposta falada adaptativa) e L1-Q06/L1-R57 (prosódia na cascata; interrupção pelo usuário).

Legenda dos formatos: D = definição; TSj = troca de sujeito; SH = situação hipotética; NP = número ou prazo; PC = par confundível; AP = aplicação parlamentar. Critério de classificação: o da T91_reconciliacao, seção 3.1 (o formato segue a construção do ponto, e não o gabarito; o formato de um item C é o da sua contraparte E). Legenda do [TS]: troca sutil de um único conceito, em item E; nesta parte, todo [TS] é de item E, e não há item C marcado como espelho.

Contagens da parte (script próprio sobre o texto final):

| folha | novos | C | E | % C (novos) | [TS] | VOLÁTIL novos | VOLÁTIL na folha de 30 (teto 6) | aderência DIRETA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| P2-1.1 | 10 | 5 | 5 | 50% | 5 | 2 | 2 (7%) | 10 |
| P2-1.2 | 10 | 5 | 5 | 50% | 5 | 0 | 0 (0%) | 10 |
| P2-1.3 | 10 | 6 | 4 | 60% | 4 | 3 | 6 (20%) | 10 |
| parte A | 30 | 16 | 14 | 53.3% | 14 | 5 | - | 30 |

Gabarito da parte: 16 C / 14 E (53.3% de C), dentro da faixa de 12 a 18 C da D1 da GCE e de 40% a 60% da regra 5 da D-REFORCO-2; por folha, de 4 a 6 C (regra 7 da D1 da GCE). [TS]: 14 de 30. VOLÁTIL novos: 5 (1.1: 2, 1.2: 0, 1.3: 3, dentro dos máximos de 6, 6 e 3 da D1); risco alto: 0; risco médio: 1 (L1-R160, limite de produto).

Formato × existentes × novos × total, por folha (teto de 30% da folha inteira depois da onda: 9 de 30). Existentes: mapas canônicos citados em "Lido antes"; L1-R131 (P2-1.2) como SH, conforme o mapa do saldo.

P2-1.1 (Reconhecimento automático de fala (ASR)):

| formato | existentes | novos | total | % de 30 |
|---|--:|--:|--:|--:|
| D | 3 | 2 | 5 | 17% |
| TSj | 2 | 1 | 3 | 10% |
| SH | 3 | 2 | 5 | 17% |
| NP | 3 | 1 | 4 | 13% |
| PC | 4 | 3 | 7 | 23% |
| AP | 5 | 1 | 6 | 20% |
| soma | 20 | 10 | 30 | 100% |

Maior formato: 7 de 30 (23%), abaixo do teto de 30% (9).

P2-1.2 (Modelos de fala end-to-end):

| formato | existentes | novos | total | % de 30 |
|---|--:|--:|--:|--:|
| D | 2 | 2 | 4 | 13% |
| TSj | 2 | 3 | 5 | 17% |
| SH | 5 | 2 | 7 | 23% |
| NP | 2 | 3 | 5 | 17% |
| PC | 5 | 0 | 5 | 17% |
| AP | 4 | 0 | 4 | 13% |
| soma | 20 | 10 | 30 | 100% |

Maior formato: 7 de 30 (23%), abaixo do teto de 30% (9).

P2-1.3 (LLMs multimodais de áudio nativo):

| formato | existentes | novos | total | % de 30 |
|---|--:|--:|--:|--:|
| D | 3 | 3 | 6 | 20% |
| TSj | 3 | 3 | 6 | 20% |
| SH | 4 | 1 | 5 | 17% |
| NP | 3 | 0 | 3 | 10% |
| PC | 3 | 2 | 5 | 17% |
| AP | 4 | 1 | 5 | 17% |
| soma | 20 | 10 | 30 | 100% |

Maior formato: 6 de 30 (20%), abaixo do teto de 30% (9).

Observações para a Gerência e a QA: (a) L1-R159 (Amazon Nova 2 Sonic), L1-R160 (limite de um arquivo de áudio por prompt) e L1-R161 (catálogo de modelos da Mistral AI) dependem de produto e estão marcados VOLÁTIL; L1-R139 e L1-R140 dependem de valores de status de uma API. (b) Os itens L1-R142 a L1-R158 têm como base artigos publicados no arXiv (L1-R156 a L1-R158, resumos), cujo texto não muda; a conferência de base de janeiro vale como reabertura da URL. (c) Os itens L1-R152 a L1-R158 não afirmam desempenho numérico nem comparação entre modelos. (d) Nenhum item afirma versão, preço ou limite além do L1-R160, que traz o limite com fonte e data (regras/proveniencia.md).

=====================================================================
PARTE 1/3 — MAPA
=====================================================================

### 1.1 Itens novos

| id | folha | ponto de julgamento | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL | aderência |
|---|---|---|---|---|---|---|
| L1-R132 | P2-1.1 | Enunciado (utterance) é o trecho de áudio entre pausas, formado por palavras e sons não linguísticos; não corresponde necessariamente a uma sentença | SH | CMUSphinx, "Basic concepts of speech recognition", seção "Structure Of Speech" (https://cmusphinx.github.io/wiki/tutorialconcepts/; verificado em 18/10/2026) | n | direta |
| L1-R133 | P2-1.1 | Velocidade em xRT = tempo de decodificação dividido pelo tempo de gravação (6 h para 2 h de áudio = 3xRT) | NP | CMUSphinx, "Basic concepts of speech recognition", seção "What Is Optimized" (https://cmusphinx.github.io/wiki/tutorialconcepts/; verificado em 18/10/2026) | n | direta |
| L1-R134 | P2-1.1 | Com a opção -D, a palavra opcional da referência que o sistema omite conta como correta, e não como supressão | D | NIST SCTK, sclite, seção "Optional Word Scoring" (https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm; verificado em 18/10/2026) | n | direta |
| L1-R135 | P2-1.1 | O alinhamento mediado por tempo usa os instantes de início e de fim das palavras, e não pesos predefinidos por palavra (que caracterizam o alinhamento mediado por peso de palavra) | PC | NIST SCTK, sclite, seções "Time-Mediated Alignment" e "Word-Weight-Mediated Alignment" (https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm; verificado em 18/10/2026) | n | direta |
| L1-R136 | P2-1.1 | Recomendação de não usar o controle automático de ganho (AGC) na captação do áudio enviado ao reconhecedor | AP | Google Cloud, "Best practices", seção "Audio preprocessing" (https://cloud.google.com/speech-to-text/docs/best-practices; verificado em 18/10/2026) | n | direta |
| L1-R137 | P2-1.1 | A configuração da requisição deve descrever fielmente o áudio enviado (codificação, idioma e modelo) para que a transcrição seja a mais precisa | SH | Google Cloud, "Best practices", seção "Request configuration" (https://cloud.google.com/speech-to-text/docs/best-practices; verificado em 18/10/2026) | n | direta |
| L1-R138 | P2-1.1 | A acurácia (accuracy) é quase igual ao WER, exceto por não levar em conta as inserções | PC | CMUSphinx, "Basic concepts of speech recognition", seção "What Is Optimized" (https://cmusphinx.github.io/wiki/tutorialconcepts/; verificado em 18/10/2026) | n | direta |
| L1-R139 | P2-1.1 | Status NoMatch: fala detectada, mas nenhuma palavra do idioma-alvo reconhecida; costuma indicar idioma de reconhecimento diferente do falado | D | Microsoft Learn, "Speech to text REST API for short audio", campo RecognitionStatus (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-speech-to-text-short; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R140 | P2-1.1 | InitialSilenceTimeout: início do fluxo só com silêncio; BabbleTimeout: início do fluxo só com ruído | TSj | Microsoft Learn, "Speech to text REST API for short audio", campo RecognitionStatus (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-speech-to-text-short; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R141 | P2-1.1 | Lattice (grafo dirigido, representação mais densa) × lista N-best (representação menos densa) | PC | CMUSphinx, "Basic concepts of speech recognition", seção "Other Concepts Used" (https://cmusphinx.github.io/wiki/tutorialconcepts/; verificado em 18/10/2026) | n | direta |
| L1-R142 | P2-1.2 | Treinar para prever o texto bruto das transcrições, sem padronização significativa, dispensa etapa separada de normalização inversa de texto | D | Radford et al., seção 2.1 (Data Processing) (https://arxiv.org/abs/2212.04356; verificado em 18/10/2026) | n | direta |
| L1-R143 | P2-1.2 | As transcrições geradas por outros sistemas de ASR foram detectadas por heurísticas e removidas do conjunto de treinamento | TSj | Radford et al., seção 2.1 (Data Processing) (https://arxiv.org/abs/2212.04356; verificado em 18/10/2026) | n | direta |
| L1-R144 | P2-1.2 | Par áudio-transcrição com idiomas diferentes não é exemplo de reconhecimento de fala; se a transcrição é em inglês, vira exemplo de tradução | SH | Radford et al., seção 2.1 (Data Processing) (https://arxiv.org/abs/2212.04356; verificado em 18/10/2026) | n | direta |
| L1-R145 | P2-1.2 | Os segmentos sem fala entram no treinamento (com amostragem reduzida) e servem de dados para a detecção de atividade de voz | TSj | Radford et al., seção 2.1 (Data Processing) (https://arxiv.org/abs/2212.04356; verificado em 18/10/2026) | n | direta |
| L1-R146 | P2-1.2 | Entrada do modelo: reamostragem a 16.000 Hz e espectrograma log-Mel de 80 canais em janelas de 25 ms com deslocamento de 10 ms | NP | Radford et al., seção 2.2 (Model) (https://arxiv.org/abs/2212.04356; verificado em 18/10/2026) | n | direta |
| L1-R147 | P2-1.2 | Na versão multilíngue, o vocabulário do tokenizador foi reajustado (mesmo tamanho) porque o vocabulário BPE do GPT-2 é só inglês e fragmentaria outros idiomas | SH | Radford et al., seção 2.2 (Model) (https://arxiv.org/abs/2212.04356; verificado em 18/10/2026) | n | direta |
| L1-R148 | P2-1.2 | A temperatura de decodificação sobe (de 0 a 1,0, em passos de 0,2) quando a taxa de compressão gzip do texto é superior a 2,4 (repetição) ou a probabilidade logarítmica média é baixa | NP | Radford et al., seção 4.5 (Strategies for Reliable Long-form Transcription) (https://arxiv.org/abs/2212.04356; verificado em 18/10/2026) | n | direta |
| L1-R149 | P2-1.2 | Restringir o carimbo de tempo inicial ao intervalo de 0,0 a 1,0 s evita que o modelo ignore as primeiras palavras da entrada | NP | Radford et al., seção 4.5 (Strategies for Reliable Long-form Transcription) (https://arxiv.org/abs/2212.04356; verificado em 18/10/2026) | n | direta |
| L1-R150 | P2-1.2 | A probabilidade do token de ausência de fala, isolada, não basta para distinguir segmento sem fala; combina-se com limiar de probabilidade logarítmica média | TSj | Radford et al., seção 4.5 (Strategies for Reliable Long-form Transcription) (https://arxiv.org/abs/2212.04356; verificado em 18/10/2026) | n | direta |
| L1-R151 | P2-1.2 | O wav2vec 2.0 mascara a entrada no espaço latente e resolve uma tarefa contrastiva sobre uma quantização das representações latentes, aprendidas em conjunto | D | Baevski et al., "wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations", resumo (https://arxiv.org/abs/2006.11477; verificado em 18/10/2026) | n | direta |
| L1-R152 | P2-1.3 | O AudioPaLM herda do AudioLM a capacidade de preservar informações paralinguísticas (identidade do falante, entonação) e processa e gera texto e fala | D | Rubenstein et al., "AudioPaLM: A Large Language Model That Can Speak and Listen", resumo (https://arxiv.org/abs/2306.12925; verificado em 18/10/2026) | n | direta |
| L1-R153 | P2-1.3 | Inicializar o modelo com os pesos de um LLM treinado só com texto melhora (e não prejudica) o processamento de fala | TSj | Rubenstein et al., resumo (https://arxiv.org/abs/2306.12925; verificado em 18/10/2026) | n | direta |
| L1-R154 | P2-1.3 | O SALMONN integra um LLM textual pré-treinado a codificadores de fala e de áudio em um único modelo, para entradas de áudio gerais (fala, eventos sonoros, música) | D | Tang et al., "SALMONN: Towards Generic Hearing Abilities for Large Language Models", resumo (https://arxiv.org/abs/2310.13289; verificado em 18/10/2026) | n | direta |
| L1-R155 | P2-1.3 | O módulo de conexão entre o codificador de áudio e o LLM gera número variável de tokens de áudio, conforme a duração da entrada (e não número fixo) | TSj | Tang et al., seção 1 (Introdução) (https://arxiv.org/abs/2310.13289; verificado em 18/10/2026) | n | direta |
| L1-R156 | P2-1.3 | Modo de conversa por voz (interação por voz, sem entrada de texto) × modo de análise de áudio (áudio mais instruções em texto) | PC | Chu et al., "Qwen2-Audio Technical Report", resumo (https://arxiv.org/abs/2407.10759; verificado em 18/10/2026) | n | direta |
| L1-R157 | P2-1.3 | Capacidade documentada de compreender diretamente um comando de voz em áudio que contém também sons e conversa de vários falantes | D | Chu et al., resumo (https://arxiv.org/abs/2407.10759; verificado em 18/10/2026) | n | direta |
| L1-R158 | P2-1.3 | O pré-treinamento do Qwen2-Audio foi simplificado com prompts em linguagem natural no lugar de tags hierárquicas complexas (e não o contrário) | TSj | Chu et al., resumo (https://arxiv.org/abs/2407.10759; verificado em 18/10/2026) | n | direta |
| L1-R159 | P2-1.3 | Recurso documentado de resposta falada adaptativa, que ajusta a forma de entrega conforme a prosódia da fala de entrada | AP | AWS, Amazon Nova 2 User Guide, "Speech-to-Speech (Amazon Nova 2 Sonic)", seção "Key features" (https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R160 | P2-1.3 | Limite documentado de um arquivo de áudio por prompt na compreensão de áudio dos modelos Gemini no Google Cloud | SH | Google Cloud, "Audio understanding (speech only)", seção "Supported models" (https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/audio-understanding; verificado em 18/10/2026) | VOLÁTIL médio | direta |
| L1-R161 | P2-1.3 | O fornecedor distingue modelo de entrada de áudio otimizado para transcrição de modelo de entrada de áudio para uso por instruções | PC | Mistral AI, documentação, "Audio", seção "Models" (https://docs.mistral.ai/capabilities/audio/; verificado em 18/10/2026) | VOLÁTIL baixo | direta |

FIM DA PARTE 1/3

=====================================================================
PARTE 2/3 — (d) ITENS DO ESTUDANTE
=====================================================================

Julgue o item.

**L1-R132** (P2-1.1)
Ao segmentar o áudio de uma sessão por silêncios para submetê-lo ao reconhecimento, a equipe obtém trechos que, na terminologia da documentação do CMUSphinx, são chamados de utterances: trechos de áudio separados por pausas, formados por palavras e sons não linguísticos, que não correspondem necessariamente a sentenças.

**L1-R133** (P2-1.1)
Segundo a documentação do CMUSphinx, a velocidade de um decodificador pode ser expressa em múltiplos do tempo de gravação (xRT). Nessa convenção, um arquivo de áudio com 2 horas de gravação cuja decodificação levou 6 horas tem velocidade de 3xRT.

**L1-R134** (P2-1.1)
No sclite, do NIST, palavras da referência podem ser marcadas como opcionais, colocando-as entre parênteses. De acordo com a documentação, quando se usa a opção -D, a palavra opcional da referência que o sistema deixa de emitir é tratada como correta, e não como supressão.

**L1-R135** (P2-1.1)
Ao pontuar a transcrição de uma sessão com o sclite, do NIST, a equipe usa referência e hipótese no formato ctm e a opção -T, que ativa o alinhamento mediado por tempo. Segundo a documentação, esse alinhamento substitui os pesos fixos de distância entre palavras por medidas baseadas em pesos predefinidos atribuídos a cada palavra.

**L1-R136** (P2-1.1)
Para a captação do áudio das sessões do Plenário, a documentação do Google Cloud Speech-to-Text recomenda manter ativado o controle automático de ganho (AGC) nos microfones.

**L1-R137** (P2-1.1)
Ao enviar as gravações de uma comissão ao Google Cloud Speech-to-Text, a equipe descreve na configuração da requisição a codificação do áudio, o idioma falado e o modelo de reconhecimento realmente adequados a essas gravações. De acordo com a documentação do Google Cloud, descrever com exatidão os dados de áudio enviados contribui para a obtenção da transcrição mais precisa e da cobrança correta da requisição.

**L1-R138** (P2-1.1)
Entre as medidas de desempenho de um sistema de reconhecimento de fala citadas na documentação do CMUSphinx, a acurácia (accuracy) equivale quase ao WER, exceto por não levar em conta as supressões.

**L1-R139** (P2-1.1)
Na API REST de reconhecimento de áudio curto do Azure Speech, o resultado com status NoMatch indica que foi detectada fala no fluxo de áudio, mas nenhuma palavra do idioma-alvo foi reconhecida, o que normalmente significa que o idioma de reconhecimento configurado é diferente do idioma falado pelo usuário.

**L1-R140** (P2-1.1)
Na API REST de reconhecimento de áudio curto do Azure Speech, o status InitialSilenceTimeout indica que o início do fluxo de áudio continha somente ruído, ao passo que o status BabbleTimeout indica que o início continha somente silêncio, em ambos os casos com o esgotamento do tempo de espera por fala.

**L1-R141** (P2-1.1)
Segundo a documentação do CMUSphinx, o lattice é um grafo dirigido que representa variantes do reconhecimento, ao passo que a lista N-best representa essas variantes de forma mais densa que o lattice.

**L1-R142** (P2-1.2)
O artigo que apresenta o Whisper informa que os modelos são treinados para prever o texto bruto das transcrições, sem padronização significativa, o que dispensa uma etapa separada de normalização inversa de texto para a obtenção de transcrições de aspecto natural.

**L1-R143** (P2-1.2)
Segundo o artigo que apresenta o Whisper, os autores mantiveram no conjunto de treinamento as transcrições geradas por outros sistemas de reconhecimento automático de fala, em vez de removê-las por meio de heurísticas de detecção.

**L1-R144** (P2-1.2)
Ao montar os dados de treinamento de um modelo de fala end-to-end como o Whisper, um par formado por áudio em francês e transcrição em inglês não é incluído como exemplo de reconhecimento de fala, pois o idioma falado não corresponde ao da transcrição. Conforme o artigo do Whisper, esse par pode ser aproveitado como exemplo de tradução da fala para o inglês.

**L1-R145** (P2-1.2)
De acordo com o artigo do Whisper, os trechos de áudio sem fala foram excluídos do conjunto de treinamento.

**L1-R146** (P2-1.2)
Segundo o artigo do Whisper, o áudio é reamostrado a 16.000 Hz e convertido em um espectrograma log-Mel de 80 canais, calculado em janelas de 10 milissegundos com deslocamento de 25 milissegundos.

**L1-R147** (P2-1.2)
No treinamento da versão multilíngue de um modelo end-to-end como o Whisper, que também transcreve o português, o vocabulário do tokenizador foi reajustado, mantendo-se o mesmo tamanho, porque o vocabulário usado na versão apenas em inglês fragmentaria excessivamente outros idiomas.

**L1-R148** (P2-1.2)
Na transcrição de áudio longo, o artigo do Whisper descreve que a temperatura de decodificação parte de 0 e é elevada em 0,2, até o máximo de 1,0, sempre que o texto gerado apresenta taxa de compressão gzip inferior a 2,4.

**L1-R149** (P2-1.2)
Para evitar que o modelo ignore as primeiras palavras do áudio na transcrição de gravações longas, o artigo do Whisper restringe o token de carimbo de tempo inicial a um valor entre 0,0 e 1,0 segundo.

**L1-R150** (P2-1.2)
Segundo o artigo do Whisper, na detecção de trechos sem fala em áudio longo, a probabilidade do token de ausência de fala é, por si só, suficiente para distinguir um segmento sem fala.

**L1-R151** (P2-1.2)
No pré-treinamento do wav2vec 2.0, a entrada de fala é mascarada no espaço latente, e o modelo resolve uma tarefa contrastiva definida sobre uma quantização das representações latentes, aprendidas em conjunto.

**L1-R152** (P2-1.3)
O artigo que apresenta o AudioPaLM descreve um modelo que funde um modelo de linguagem textual e um de fala em uma arquitetura multimodal única, capaz de processar e gerar texto e fala, e que herda do AudioLM a capacidade de preservar informações paralinguísticas, como a identidade do falante e a entonação.

**L1-R153** (P2-1.3)
Segundo o artigo do AudioPaLM, inicializar o modelo com os pesos de um grande modelo de linguagem treinado somente com texto prejudica o processamento de fala.

**L1-R154** (P2-1.3)
O SALMONN integra um grande modelo de linguagem textual pré-treinado a codificadores de fala e de áudio em um único modelo multimodal, o que permite ao LLM processar diretamente entradas de áudio de natureza geral, entre elas fala, eventos sonoros e música.

**L1-R155** (P2-1.3)
No SALMONN, o módulo de conexão entre os codificadores de áudio e o LLM converte a saída do codificador em um número fixo de tokens de áudio, qualquer que seja a duração da gravação.

**L1-R156** (P2-1.3)
O Qwen2-Audio apresenta dois modos de interação com áudio: no modo de conversa por voz, o usuário interage com o modelo por voz, sem entrada de texto; no modo de análise de áudio, o usuário fornece áudio e instruções em texto para a análise.

**L1-R157** (P2-1.3)
Segundo o artigo do Qwen2-Audio, diante de um trecho de áudio que contém ao mesmo tempo sons, conversa entre vários falantes e um comando de voz, o modelo é capaz de entender diretamente o comando e fornecer uma interpretação e uma resposta ao áudio.

**L1-R158** (P2-1.3)
Segundo o artigo do Qwen2-Audio, o pré-treinamento foi simplificado com o uso de tags hierárquicas complexas no lugar de prompts em linguagem natural para os diferentes dados e tarefas.

**L1-R159** (P2-1.3)
Em um serviço de atendimento por voz da Casa baseado em modelo de fala para fala, segundo a documentação do Amazon Nova 2 Sonic, a resposta falada pode ter a forma de entrega ajustada dinamicamente de acordo com a prosódia da fala do usuário.

**L1-R160** (P2-1.3)
Uma equipe pretende enviar, em um único prompt a modelo Gemini por meio do Google Cloud, os arquivos de áudio de três reuniões de comissão. Segundo a documentação sobre compreensão de áudio, o número máximo de arquivos de áudio por prompt é um, de modo que as três gravações não podem ser enviadas, como três arquivos, no mesmo prompt.

**L1-R161** (P2-1.3)
Segundo a documentação de áudio da Mistral AI, a oferta de modelos para tratamento de áudio inclui apenas modelo de entrada de áudio voltado a tarefas por instrução, não havendo modelo de áudio otimizado especificamente para transcrição.

FIM DA PARTE 2/3

=====================================================================
PARTE 3/3 — (d-G) GABARITO COMENTADO
=====================================================================

**L1-R132** (P2-1.1) Gabarito: C.
Justificativa: A documentação define as "utterances" como trechos de áudio separados por pausas, formados por palavras e sons não linguísticos (fillers), e acrescenta que "don't necessarily match sentences". O item aplica a definição à segmentação por silêncios.
Base: CMUSphinx, "Basic concepts of speech recognition", seção "Structure Of Speech" (https://cmusphinx.github.io/wiki/tutorialconcepts/), verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R133** (P2-1.1) Gabarito: C.
Justificativa: A página dá o exemplo: gravação de 2 horas e decodificação de 6 horas, "the speed is counted as 3xRT". A velocidade é a razão entre o tempo de decodificação e o de gravação: 6 ÷ 2 = 3.
Base: CMUSphinx, "Basic concepts of speech recognition", seção "What Is Optimized" (https://cmusphinx.github.io/wiki/tutorialconcepts/), verificado em 18/10/2026. Não VOLÁTIL. Formato: NP.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R134** (P2-1.1) Gabarito: C.
Justificativa: A documentação descreve a opção -D como a que faz "treat as correct any word identified as optional IFF it is deleted by the system (for an optional reference word)". No exemplo da página, a palavra opcional omitida deixa de contar como supressão.
Base: NIST SCTK, sclite, seção "Optional Word Scoring" (https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm), verificado em 18/10/2026. Não VOLÁTIL. Formato: D.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R135** (P2-1.1) Gabarito: E. [TS]
Justificativa: No alinhamento mediado por tempo, os pesos fixos 0, 3, 3 e 4 são trocados por "measures based on beginning and ending word times". Pesos predefinidos por palavra caracterizam outra variação, o alinhamento mediado por peso de palavra.
Base: NIST SCTK, sclite, seções "Time-Mediated Alignment" e "Word-Weight-Mediated Alignment" (https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm), verificado em 18/10/2026. Não VOLÁTIL. Formato: PC.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R136** (P2-1.1) Gabarito: E. [TS]
Justificativa: A página de boas práticas orienta "Do not use automatic gain control (AGC)", ao lado de evitar o corte (clipping) do áudio. O item inverte a recomendação.
Base: Google Cloud, "Best practices", seção "Audio preprocessing" (https://cloud.google.com/speech-to-text/docs/best-practices; página com "Last updated" em 2026-10-13), verificado em 18/10/2026. Não VOLÁTIL. Formato: AP.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R137** (P2-1.1) Gabarito: C.
Justificativa: A documentação afirma que descrever a codificação correta e usar o reconhecedor com o idioma e o modelo corretos "will result in the most accurate transcription and billing for your request". O item reproduz essa orientação.
Base: Google Cloud, "Best practices", seção "Request configuration" (https://cloud.google.com/speech-to-text/docs/best-practices; página com "Last updated" em 2026-10-13), verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R138** (P2-1.1) Gabarito: E. [TS]
Justificativa: A documentação diz que a acurácia "is almost the same as the word error rate, but it doesn't take insertions into account", calculada como (N − D − S) ÷ N. O item troca as inserções pelas supressões.
Base: CMUSphinx, "Basic concepts of speech recognition", seção "What Is Optimized" (https://cmusphinx.github.io/wiki/tutorialconcepts/), verificado em 18/10/2026. Não VOLÁTIL. Formato: PC.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R139** (P2-1.1) Gabarito: C.
Justificativa: A tabela de status define NoMatch como "Speech was detected in the audio stream, but no words from the target language were matched", o que "usually" indica idioma de reconhecimento diferente do falado. O item reproduz a definição.
Base: Microsoft Learn, "Speech to text REST API for short audio", campo RecognitionStatus (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-speech-to-text-short; página com "Last updated" em 2026-06-05), verificado em 18/10/2026. VOLÁTIL baixo. Formato: D.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir a definição do status NoMatch na tabela do campo RecognitionStatus. VOLÁTIL baixo, valor de status documentado de API de fornecedor (dependência de produto). Inapto a simulado final até a reverificação.
Aderência: direta.

**L1-R140** (P2-1.1) Gabarito: E. [TS]
Justificativa: Na tabela de status, InitialSilenceTimeout é o início do fluxo com "only silence", e BabbleTimeout, o início com "only noise". O item troca silêncio e ruído entre os dois status.
Base: Microsoft Learn, "Speech to text REST API for short audio", campo RecognitionStatus (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-speech-to-text-short; página com "Last updated" em 2026-06-05), verificado em 18/10/2026. VOLÁTIL baixo. Formato: TSj.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir as definições dos status InitialSilenceTimeout e BabbleTimeout na tabela do campo RecognitionStatus. VOLÁTIL baixo, valor de status documentado de API de fornecedor (dependência de produto). Inapto a simulado final até a reverificação.
Aderência: direta.

**L1-R141** (P2-1.1) Gabarito: E. [TS]
Justificativa: Na documentação, "N-best lists of variants are like lattices, though their representations are not as dense as the lattice ones". O item atribui à lista N-best a maior densidade, que é do lattice.
Base: CMUSphinx, "Basic concepts of speech recognition", seção "Other Concepts Used" (https://cmusphinx.github.io/wiki/tutorialconcepts/), verificado em 18/10/2026. Não VOLÁTIL. Formato: PC.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R142** (P2-1.2) Gabarito: C.
Justificativa: O artigo diz que o treinamento prevê "the raw text of transcripts without any significant standardization" e que isso "removes the need for a separate inverse text normalization step". O item reproduz as duas informações.
Base: Radford et al., seção 2.1 (Data Processing) (https://arxiv.org/abs/2212.04356), verificado em 18/10/2026. Não VOLÁTIL. Formato: D.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R143** (P2-1.2) Gabarito: E. [TS]
Justificativa: O artigo relata: "we developed many heuristics to detect and remove machine-generated transcripts from the training dataset", para evitar o aprendizado do "transcript-ese". O item afirma que elas foram mantidas.
Base: Radford et al., seção 2.1 (Data Processing) (https://arxiv.org/abs/2212.04356), verificado em 18/10/2026. Não VOLÁTIL. Formato: TSj.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R144** (P2-1.2) Gabarito: C.
Justificativa: Se os idiomas não coincidem, "we don't include the (audio, transcript) pair as a speech recognition training example"; há exceção quando a transcrição é em inglês, caso em que o par vira exemplo de tradução. O item aplica a regra e a exceção.
Base: Radford et al., seção 2.1 (Data Processing) (https://arxiv.org/abs/2212.04356), verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R145** (P2-1.2) Gabarito: E. [TS]
Justificativa: O artigo diz: "We train on all audio, including segments where there is no speech (though with sub-sampled probability)", e usa esses trechos como dados de treinamento para a detecção de atividade de voz. O item afirma a exclusão.
Base: Radford et al., seção 2.1 (Data Processing) (https://arxiv.org/abs/2212.04356), verificado em 18/10/2026. Não VOLÁTIL. Formato: TSj.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R146** (P2-1.2) Gabarito: E. [TS]
Justificativa: O artigo descreve janelas de 25 milissegundos com deslocamento ("stride") de 10 milissegundos, após a reamostragem a 16.000 Hz. O item troca os valores da janela e do deslocamento.
Base: Radford et al., seção 2.2 (Model) (https://arxiv.org/abs/2212.04356), verificado em 18/10/2026. Não VOLÁTIL. Formato: NP.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R147** (P2-1.2) Gabarito: C.
Justificativa: O artigo explica que o vocabulário foi refeito ("refit the vocabulary (but keep the same size)") nos modelos multilíngues "to avoid excessive fragmentation on other languages", pois o vocabulário BPE do GPT-2 é só inglês. O item reproduz a razão.
Base: Radford et al., seção 2.2 (Model) (https://arxiv.org/abs/2212.04356), verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R148** (P2-1.2) Gabarito: E. [TS]
Justificativa: O procedimento eleva a temperatura quando o texto tem "a gzip compression rate higher than 2.4" (sinal de repetição) ou probabilidade logarítmica média baixa. O item troca superior por inferior.
Base: Radford et al., seção 4.5 (Strategies for Reliable Long-form Transcription) (https://arxiv.org/abs/2212.04356), verificado em 18/10/2026. Não VOLÁTIL. Formato: NP.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R149** (P2-1.2) Gabarito: C.
Justificativa: O artigo descreve a medida contra o modo de falha em que "the model ignores the first few words in the input": "we constrained the initial timestamp token to be between 0.0 and 1.0 second". O item reproduz a medida.
Base: Radford et al., seção 4.5 (Strategies for Reliable Long-form Transcription) (https://arxiv.org/abs/2212.04356), verificado em 18/10/2026. Não VOLÁTIL. Formato: NP.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R150** (P2-1.2) Gabarito: E. [TS]
Justificativa: O artigo afirma que "the probability of the <|nospeech|> token alone is not sufficient" e que combiná-la com um limiar de probabilidade logarítmica média torna a detecção mais confiável. O item afirma o contrário.
Base: Radford et al., seção 4.5 (Strategies for Reliable Long-form Transcription) (https://arxiv.org/abs/2212.04356), verificado em 18/10/2026. Não VOLÁTIL. Formato: TSj.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R151** (P2-1.2) Gabarito: C.
Justificativa: O resumo do artigo diz que o wav2vec 2.0 "masks the speech input in the latent space and solves a contrastive task defined over a quantization of the latent representations which are jointly learned". O item reproduz o mecanismo.
Base: Baevski et al., "wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations", resumo (https://arxiv.org/abs/2006.11477), verificado em 18/10/2026. Não VOLÁTIL. Formato: D.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R152** (P2-1.3) Gabarito: C.
Justificativa: O resumo do artigo diz que o AudioPaLM "inherits the capability to preserve paralinguistic information such as speaker identity and intonation from AudioLM", em arquitetura que "can process and generate text and speech". O item reproduz ambas as informações.
Base: Rubenstein et al., "AudioPaLM: A Large Language Model That Can Speak and Listen", resumo (https://arxiv.org/abs/2306.12925), verificado em 18/10/2026. Não VOLÁTIL. Formato: D.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R153** (P2-1.3) Gabarito: E. [TS]
Justificativa: O resumo afirma que "initializing AudioPaLM with the weights of a text-only large language model improves speech processing", ao aproveitar o maior volume de dados de texto do pré-treinamento. O item afirma que prejudica.
Base: Rubenstein et al., resumo (https://arxiv.org/abs/2306.12925), verificado em 18/10/2026. Não VOLÁTIL. Formato: TSj.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R154** (P2-1.3) Gabarito: C.
Justificativa: O resumo descreve o SALMONN como modelo que integra "a pre-trained text-based large language model (LLM) with speech and audio encoders into a single multimodal model" para sons de três tipos: fala, eventos de áudio e música. O item reproduz a descrição.
Base: Tang et al., "SALMONN: Towards Generic Hearing Abilities for Large Language Models", resumo (https://arxiv.org/abs/2310.13289), verificado em 18/10/2026. Não VOLÁTIL. Formato: D.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R155** (P2-1.3) Gabarito: E. [TS]
Justificativa: O artigo usa o Q-Former em janelas como módulo de conexão para converter "a variable-length encoder output sequence to a variable number of augmented audio tokens". O item afirma número fixo, independente da duração.
Base: Tang et al., seção 1 (Introdução) (https://arxiv.org/abs/2310.13289), verificado em 18/10/2026. Não VOLÁTIL. Formato: TSj.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R156** (P2-1.3) Gabarito: C.
Justificativa: O resumo define: "In the voice chat mode, users can freely engage in voice interactions with Qwen2-Audio without text input", e, na análise de áudio, o usuário fornece áudio e instruções em texto. O item reproduz a distinção.
Base: Chu et al., "Qwen2-Audio Technical Report", resumo (https://arxiv.org/abs/2407.10759), verificado em 18/10/2026. Não VOLÁTIL. Formato: PC.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R157** (P2-1.3) Gabarito: C.
Justificativa: O resumo afirma que, "in an audio segment that simultaneously contains sounds, multi-speaker conversations, and a voice command", o modelo "can directly understand the command and provide an interpretation and response to the audio". O item reproduz a capacidade.
Base: Chu et al., resumo (https://arxiv.org/abs/2407.10759), verificado em 18/10/2026. Não VOLÁTIL. Formato: D.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R158** (P2-1.3) Gabarito: E. [TS]
Justificativa: O resumo diz: "In contrast to complex hierarchical tags, we have simplified the pre-training process by utilizing natural language prompts for different data and tasks". O item inverte os papéis das tags e dos prompts.
Base: Chu et al., resumo (https://arxiv.org/abs/2407.10759), verificado em 18/10/2026. Não VOLÁTIL. Formato: TSj.
CONFERÊNCIA DE BASE em 4–8/1/2027 (sem efeito de VOLÁTIL): reabrir a URL e conferir o trecho literal citado.
Aderência: direta.

**L1-R159** (P2-1.3) Gabarito: C.
Justificativa: O guia lista, entre os recursos, "Adaptive speech response that dynamically adjusts delivery based on the prosody of the input speech". O item descreve esse recurso, que é de um produto e pode mudar.
Base: AWS, Amazon Nova 2 User Guide, "Speech-to-Speech (Amazon Nova 2 Sonic)", seção "Key features" (https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html), verificado em 18/10/2026. VOLÁTIL baixo. Formato: AP.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir a linha "Adaptive speech response" da lista de recursos. VOLÁTIL baixo, recurso documentado de produto de fornecedor (existência de recurso). Inapto a simulado final até a reverificação.
Aderência: direta.

**L1-R160** (P2-1.3) Gabarito: C.
Justificativa: A tabela de modelos compatíveis informa "Maximum number of audio files per prompt: 1". Logo, três arquivos distintos não cabem no mesmo prompt. É limite de produto e pode mudar.
Base: Google Cloud, "Audio understanding (speech only)", seção "Supported models" (https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/audio-understanding; página com "Last updated" em 2026-10-15), verificado em 18/10/2026. VOLÁTIL médio. Formato: SH.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir a linha "Maximum number of audio files per prompt" da tabela de modelos compatíveis. VOLÁTIL médio, limite de produto de fornecedor, valor numérico que pode mudar. Inapto a simulado final até a reverificação.
Aderência: direta.

**L1-R161** (P2-1.3) Gabarito: E. [TS]
Justificativa: A página lista um modelo de entrada de áudio "optimized for transcription purposes" e outro, com entrada de áudio, "for instruct use cases". O item nega a existência do modelo voltado à transcrição.
Base: Mistral AI, documentação, "Audio", seção "Models" (https://docs.mistral.ai/capabilities/audio/), verificado em 18/10/2026. VOLÁTIL baixo. Formato: PC.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir as descrições dos modelos de entrada de áudio na seção "Models". VOLÁTIL baixo, catálogo de modelos do fornecedor (existência de modelo). Inapto a simulado final até a reverificação.
Aderência: direta.

### Tabela de proveniência

| Fonte | URL oficial | Verificado em | Data exibida pela página | Itens |
|---|---|---|---|---|
| Radford et al., Robust Speech Recognition via Large-Scale Weak Supervision (OpenAI; arXiv:2212.04356) (texto lido na versão HTML https://ar5iv.labs.arxiv.org/html/2212.04356 e conferido no PDF oficial https://arxiv.org/pdf/2212.04356) | https://arxiv.org/abs/2212.04356 | 18/10/2026 | não exibida | R142, R143, R144, R145, R146, R147, R148, R149, R150 |
| NIST SCTK, sclite (repositório oficial usnistgov/SCTK) (página sem data de atualização) | https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm | 18/10/2026 | não exibida | R134, R135 |
| CMUSphinx, Basic concepts of speech recognition (documentação oficial do projeto) (página sem data de atualização) | https://cmusphinx.github.io/wiki/tutorialconcepts/ | 18/10/2026 | não exibida | R132, R133, R138, R141 |
| Google Cloud, Speech-to-Text, Best practices (redireciona a https://docs.cloud.google.com/speech-to-text/docs/best-practices; a página exibe "Last updated 2026-10-13 UTC") | https://cloud.google.com/speech-to-text/docs/best-practices | 18/10/2026 | 2026-10-13 | R136, R137 |
| Microsoft Learn, Speech to text REST API for short audio (a página exibe "Last updated on 2026-06-05") | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-speech-to-text-short | 18/10/2026 | 2026-06-05 | R139, R140 |
| Baevski et al., wav2vec 2.0 (arXiv:2006.11477), resumo (página de resumo do arXiv) | https://arxiv.org/abs/2006.11477 | 18/10/2026 | não exibida | R151 |
| Rubenstein et al., AudioPaLM (arXiv:2306.12925), resumo (página de resumo do arXiv) | https://arxiv.org/abs/2306.12925 | 18/10/2026 | não exibida | R152, R153 |
| Tang et al., SALMONN (arXiv:2310.13289), resumo (página de resumo do arXiv) | https://arxiv.org/abs/2310.13289 | 18/10/2026 | não exibida | R154 |
| Tang et al., SALMONN (arXiv:2310.13289), texto integral (texto integral lido em https://ar5iv.labs.arxiv.org/html/2310.13289) | https://arxiv.org/abs/2310.13289 | 18/10/2026 | não exibida | R155 |
| Chu et al., Qwen2-Audio Technical Report (arXiv:2407.10759), resumo (página de resumo do arXiv) | https://arxiv.org/abs/2407.10759 | 18/10/2026 | não exibida | R156, R157, R158 |
| AWS, Amazon Nova 2 User Guide, Speech-to-Speech (Amazon Nova 2 Sonic) (página sem data de atualização) | https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html | 18/10/2026 | não exibida | R159 |
| Google Cloud, Audio understanding (speech only) (redireciona a https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/audio-understanding; a página exibe "Last updated 2026-10-15 UTC") | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/audio-understanding | 18/10/2026 | 2026-10-15 | R160 |
| Mistral AI, documentação, Audio (redireciona a https://docs.mistral.ai/studio/audio/overview; página sem data de atualização) | https://docs.mistral.ai/capabilities/audio/ | 18/10/2026 | não exibida | R161 |

Observações de proveniência: (1) o texto de cada página foi baixado em 18/10/2026 e os trechos entre aspas das justificativas foram conferidos por script contra esse texto; (2) afirmações sobre Whisper: apenas as dos itens L1-R142 a L1-R150, todas do artigo "Robust Speech Recognition via Large-Scale Weak Supervision" (arXiv:2212.04356), sem versão, preço nem limite de produto; nenhuma afirmação sobre a API da OpenAI; (3) afirmações sobre Google Speech-to-Text: L1-R136 e L1-R137, da página de boas práticas; sobre o Gemini no Google Cloud: L1-R160 (limite com data da página); (4) afirmações sobre Azure Speech: L1-R139 e L1-R140, da página da API REST de áudio curto; nenhuma sobre AWS Transcribe; sobre a AWS, apenas o recurso do Amazon Nova 2 Sonic (L1-R159); (5) nenhum item afirma versão de modelo, preço ou região; o único limite numérico de produto é o do L1-R160, com fonte e data; (6) os nomes AudioPaLM, SALMONN, Qwen2-Audio e Amazon Nova 2 Sonic aparecem só como objetos das respectivas fontes, e a prova pode cobrar o conceito, e não o nome do produto; (7) nada nesta parte é "[SEM FONTE — não afirmar]": todo item tem fonte, URL e data.

FIM DA PARTE 3/3

FIM DO LOTE
