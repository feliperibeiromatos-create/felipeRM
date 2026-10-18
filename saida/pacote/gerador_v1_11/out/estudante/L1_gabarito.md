# Lote 1 — RF-ASR (reconhecimento de fala e transcrição, P2 1.1–1.8) — gabarito e justificativas

### L1-Q01 — Gabarito: E

- Item do edital: P2-1.1
- Justificativa: No cálculo usual, pontuação e capitalização ficam fora do WER, e a atribuição de locutor fica fora em qualquer convenção, então WER 0% não garante fidelidade nesses aspectos. Erro por extrapolação.

### L1-Q02 — Gabarito: E

- Item do edital: P2-1.1
- Justificativa: ASR produz texto; atribuir falas a locutores é diarização (rótulos) ou identificação (nomes), módulos distintos.

### L1-Q03 — Gabarito: E

- Item do edital: P2-1.2
- Justificativa: Modelos end-to-end podem produzir trechos fluentes porém falsos onde o áudio é ruim; a arquitetura não imuniza contra alucinação. Erro por generalização.

### L1-Q04 — Gabarito: C

- Item do edital: P2-1.2
- Justificativa: Falsa pegadinha: "supervisão fraca" parece sugerir ausência de rótulos, mas significa transcrições preexistentes; pares áudio–texto continuam necessários.

### L1-Q05 — Gabarito: C

- Item do edital: P2-1.3
- Justificativa: É o que distingue o modelo nativo da arquitetura em cascata: áudio como entrada do próprio LLM (documentação do Google sobre áudio e transcrição na API Gemini, verificado em 07/10/2026).

### L1-Q06 — Gabarito: E

- Item do edital: P2-1.3
- Justificativa: Na cascata o LLM recebe apenas o texto do ASR; prosódia se perde — justamente a limitação que o áudio nativo pretende superar.

### L1-Q07 — Gabarito: E

- Item do edital: P2-1.4
- Justificativa: Diarização entrega rótulos genéricos (Locutor 1, 2...); exibir nomes exige identificação (amostra cadastrada ou revisão humana). Erro por extrapolação.

### L1-Q08 — Gabarito: C

- Item do edital: P2-1.4
- Justificativa: Falsa pegadinha: a frase soa invertida mas está correta — verificação é 1:1 contra identidade alegada; diarizar não exige verificar nem identificar.

### L1-Q09 — Gabarito: C

- Item do edital: P2-1.4
- Justificativa: DER soma erro de falante, fala perdida e falso alarme; WER soma substituições, deleções e inserções de palavras. Métricas distintas para tarefas distintas.

### L1-Q10 — Gabarito: C

- Item do edital: P2-1.5
- Justificativa: Modelos end-to-end podem emitir texto já pontuado e capitalizado; pipelines clássicos em geral restauram pontuação em etapa posterior.

### L1-Q11 — Gabarito: C

- Item do edital: P2-1.5
- Justificativa: Falsa pegadinha: o item parece confundir os dois recursos, mas os distingue corretamente — ditado do sinal versus inferência do sinal.

### L1-Q12 — Gabarito: E

- Item do edital: P2-1.6
- Justificativa: Adaptação de vocabulário enviesa o reconhecimento para termos esperados; não garante acerto em qualquer condição acústica nem corrige sotaque. Erro por generalização.

### L1-Q13 — Gabarito: E

- Item do edital: P2-1.6
- Justificativa: Adaptação é lista de termos que enviesa o reconhecimento, não retreino acústico; sotaque pede dados acústicos/modelo customizado.

### L1-Q14 — Gabarito: C

- Item do edital: P2-1.6
- Justificativa: Distinção documentada pela AWS: custom vocabulary amplia o vocabulário base (visão geral da documentação do Amazon Transcribe); custom language model é treinado com dados de texto (documentação do Amazon Transcribe sobre modelos de linguagem personalizados).

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-Q15 — Gabarito: C

- Item do edital: P2-1.7
- Justificativa: Funcionamento padrão do streaming: parciais revisáveis e final em geral consolidado após o fim do enunciado.

### L1-Q16 — Gabarito: E

- Item do edital: P2-1.7
- Justificativa: stream=true devolve texto incremental de um arquivo já completo; áudio ao vivo usa a transcrição Realtime, fluxo distinto (documentação da OpenAI sobre fala para texto).

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-Q17 — Gabarito: C

- Item do edital: P2-1.7
- Justificativa: Falsa pegadinha: o item parece afirmar ganho duplo, mas afirma o trade-off correto — menor latência, risco de fragmentar enunciados.

### L1-Q18 — Gabarito: C

- Item do edital: P2-1.8
- Justificativa: Código e pesos abertos no repositório openai/whisper, licença MIT (repositório openai/whisper no GitHub); a API recomenda gpt-transcribe para transcrição geral e reserva whisper-1 a timestamps, legendas e tradução (documentação da OpenAI sobre fala para texto).

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-Q19 — Gabarito: E

- Item do edital: P2-1.8
- Justificativa: A documentação oficial prevê implantação em nuvem ou on-premises via contêineres (documentação da Microsoft sobre o Azure AI Speech).

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-Q20 — Gabarito: E

- Item do edital: P2-1.8
- Justificativa: Em serviço em nuvem o áudio é enviado a infraestrutura de terceiro; só a execução local mantém o áudio sob controle exclusivo da instituição. Equivalência de custódia é falsa.

### L1C-Q21 — Gabarito: E

- Item do edital: P2-1.1
- Justificativa: Inverte as funções: o modelo acústico liga o áudio a unidades sonoras; o de linguagem estima sequências de palavras.

### L1C-Q22 — Gabarito: E

- Item do edital: P2-1.1
- Justificativa: Erro por extrapolação: inserções entram no numerador, e o WER pode ultrapassar 100%.

### L1C-Q23 — Gabarito: C

- Item do edital: P2-1.2
- Justificativa: Sem léxico separado, a correção passa, em regra, por adaptação (1.6) ou mais dados; dados de pronúncia são recurso de custom speech (Azure, documentação da Microsoft sobre o Azure AI Speech).

### L1C-Q24 — Gabarito: C

- Item do edital: P2-1.2
- Justificativa: Falsa pegadinha: em muitos sistemas há espectrograma (ex.: Whisper, artigo do Whisper, "Robust Speech Recognition via Large-Scale Weak Supervision"), mas não é universal; o wav2vec 2.0 recebe áudio bruto (artigo do wav2vec 2.0, arXiv 2006.11477, verificado em 08/10/2026).

### L1C-Q25 — Gabarito: E

- Item do edital: P2-1.3
- Justificativa: Erro por generalização: o LLM nativo gera texto plausível, não copia; o edital mantém a revisão humana (2.2).

### L1C-Q26 — Gabarito: E

- Item do edital: P2-1.3
- Justificativa: ASR reforçado por LLM não é LLM nativo: reforço por LLM não implica, por si, que o áudio entre como modalidade do próprio LLM; o nexo 'por esse motivo' é falso.

### L1C-Q27 — Gabarito: C

- Item do edital: P2-1.4
- Justificativa: Falsa pegadinha: "identificar" no sentido amplo é distinguir; nomes exigem cadastro ou atribuição humana.

### L1C-Q28 — Gabarito: E

- Item do edital: P2-1.4
- Justificativa: O OBJETO decide: "que há três oradores" = distinguir; "pelo nome" = identificação própria (amostras ou atribuição humana).

### L1C-Q29 — Gabarito: C

- Item do edital: P2-1.5
- Justificativa: A pontuação é inferida e pode mudar o sentido ("Aprovado." × "Aprovado?"); a revisão a confere.

### L1C-Q30 — Gabarito: E

- Item do edital: P2-1.5
- Justificativa: Erro por generalização: a capitalização estima e pode errar (Câmara × câmara).

## Itens de reforço

### L1-R01 — Gabarito: E

- Item do edital: P2-1.1
- Justificativa: O WER é medido sobre um conjunto de áudio e depende da semelhança entre as condições de teste e de uso; ele não é propriedade fixa do modelo.

### L1-R02 — Gabarito: C

- Item do edital: P2-1.1
- Justificativa: Os resultados costumam trazer confiança e tempo por palavra, que servem para sincronizar com o vídeo e para priorizar a conferência humana.

### L1-R03 — Gabarito: E

- Item do edital: P2-1.2
- Justificativa: A tarefa é especificada por tokens especiais do formato de treinamento multitarefa, previstos pelo decodificador; um único modelo substitui várias etapas do pipeline tradicional.

### L1-R04 — Gabarito: C

- Item do edital: P2-1.2
- Justificativa: O método transcribe() processa o arquivo com janela deslizante de 30 segundos, e o áudio é ajustado (pad/trim) a 30 s para o modelo.

### L1-R05 — Gabarito: C

- Item do edital: P2-1.3
- Justificativa: LLM de áudio nativo recebe o áudio como entrada e é guiado por instrução em texto; a documentação lista compreensão de fala para sumarização, transcrição e tradução no mesmo modelo.

### L1-R06 — Gabarito: E

- Item do edital: P2-1.3
- Justificativa: A conta é 2 h × 3.600 s × 30 tokens/s = 216.000 tokens; 108.000 corresponde a 1 hora. O consumo de contexto cresce em proporção à duração.

### L1-R07 — Gabarito: C

- Item do edital: P2-1.4
- Justificativa: Falsa pegadinha: separação por canal e diarização são recursos distintos, e a primeira não depende de inferir a voz; ela revela o canal (microfone), não o nome.

### L1-R08 — Gabarito: C

- Item do edital: P2-1.5
- Justificativa: A documentação remete à lista de recursos por idioma, e o suporte pode diferir entre lote e streaming; a verificação para o pt-BR é prudente antes da adoção.

### L1-R09 — Gabarito: E

- Item do edital: P2-1.5
- Justificativa: Trocados os papéis: a forma lexical é a das palavras sem capitalização e pontuação, e a de exibição é a que as aplica (além de normalização e máscara de palavrões).

### L1-R10 — Gabarito: C

- Item do edital: P2-1.6
- Justificativa: A documentação do fornecedor indica o vocabulário personalizado para termos de domínio, inclusive nomes próprios, e orienta a não inserir nele informação confidencial, identificadores pessoais (PII) ou informação de saúde (PHI).

### L1-R11 — Gabarito: E

- Item do edital: P2-1.6
- Justificativa: O desempenho de um mesmo modelo multilíngue varia amplamente conforme o idioma, e o WER em inglês não se transfere ao pt-BR; é preciso avaliar com áudio do domínio.

### L1-R12 — Gabarito: E

- Item do edital: P2-1.6
- Justificativa: Quem usa o contexto das palavras vizinhas é o modelo de linguagem; o acústico liga som a unidades sonoras e não separa homófonas.

### L1-R13 — Gabarito: E

- Item do edital: P2-1.7
- Justificativa: A documentação afirma que a latência depende do tamanho dos blocos de áudio enviados e recomenda blocos de tamanho uniforme; o erro está em atribuir a latência só ao servidor.

### L1-R14 — Gabarito: C

- Item do edital: P2-1.7
- Justificativa: 100/1000 × 16.000 × 2 = 3.200 bytes (a fórmula de tamanho de bloco considera 2 bytes por amostra, áudio mono).

### L1-R15 — Gabarito: E

- Item do edital: P2-1.7
- Justificativa: A documentação afirma que o streaming é mais rápido, mas que essa velocidade pode trazer limitações de acurácia em alguns casos; não há garantia de acurácia igual ou superior à do lote.

### L1-R16 — Gabarito: C

- Item do edital: P2-1.8
- Justificativa: A tarefa de tradução do Whisper (--task translate) converte fala não inglesa em texto em inglês nos modelos multilíngues treinados para essa tarefa; o modelo turbo não foi treinado para tradução.

### L1-R17 — Gabarito: E

- Item do edital: P2-1.8
- Justificativa: Papéis trocados: o lote opera sobre arquivos de mídia previamente enviados, e o streaming recebe blocos sequenciais com resposta em tempo real.

### L1-R18 — Gabarito: C

- Item do edital: P2-1.8
- Justificativa: A tabela do README traz tiny com 39 milhões e large com 1.550 milhões de parâmetros, com relação de velocidade e acurácia entre tamanhos.

### L1-R19 — Gabarito: E

- Item do edital: P2-1.1
- Justificativa: O denominador do WER é o número de palavras da transcrição de referência (50), e não o da hipótese (51); o WER correto é 6/50 = 12%.

### L1-R20 — Gabarito: C

- Item do edital: P2-1.1
- Justificativa: A documentação associa muitas supressões a sinal de áudio fraco e substituições a amostra insuficiente de termos do domínio, em transcrições rotuladas ou texto relacionado; o item reproduz essa associação.

### L1-R21 — Gabarito: E

- Item do edital: P2-1.1
- Justificativa: A falha da referência distorce o WER também quando o sistema acerta e a referência erra: o acerto vira erro contado. A precisão das estatísticas acompanha a acurácia do texto de referência, e não só os casos de erro coincidente.

### L1-R22 — Gabarito: C

- Item do edital: P2-1.1
- Justificativa: Segundo a página, convém escolher, para o teste, um conjunto acústico diferente do usado com o modelo, o que dá uma noção mais realista do desempenho.

### L1-R23 — Gabarito: E

- Item do edital: P2-1.1
- Justificativa: As duas documentações recomendam o oposto: usar codec sem perda (FLAC ou LINEAR16; no Amazon Transcribe, FLAC ou WAV com PCM de 16 bits) e evitar MP3 e outros codecs com perda, que podem reduzir a acurácia.

### L1-R24 — Gabarito: E

- Item do edital: P2-1.1
- Justificativa: A documentação diz que o reconhecedor foi projetado para áudio ruidoso e que aplicar redução de ruído antes do envio costuma reduzir, e não elevar, a acurácia; recomenda microfone próximo e desligar a redução de ruído.

### L1-R25 — Gabarito: C

- Item do edital: P2-1.1
- Justificativa: O item parece uma troca de taxas, mas reproduz a documentação: capturar a 16.000 Hz ou mais quando possível e, para telefonia (nativa comum de 8.000 Hz), enviar na taxa nativa, evitando reamostragem.

### L1-R26 — Gabarito: C

- Item do edital: P2-1.1
- Justificativa: A sclite alinha hipótese e referência por programação dinâmica, que faz uma minimização global de uma função de distância de Levenshtein com pesos (0, 3, 3 e 4 para acerto, inserção, supressão e substituição).

### L1-R27 — Gabarito: E

- Item do edital: P2-1.1
- Justificativa: Os papéis estão trocados: palavra pronunciada e não reconhecida é supressão, e palavra acrescentada que não foi dita é inserção.

### L1-R28 — Gabarito: C

- Item do edital: P2-1.1
- Justificativa: O item parece afrouxar a avaliação, mas a sclite prevê transcrições alternativas de referência: o sistema pode emitir qualquer uma delas e continuar correto. O exemplo "para"/"pra" é aplicação do item; a documentação traz o caso inglês "what are"/"what're".

### L1-R29 — Gabarito: E

- Item do edital: P2-1.1
- Justificativa: A documentação diz o contrário: vozes simultâneas ou em volumes diferentes podem ser interpretadas como ruído de fundo e ignoradas, e, se cada pessoa estiver em canal próprio, envia-se cada canal separadamente.

### L1-R30 — Gabarito: E

- Item do edital: P2-1.1
- Justificativa: O cálculo-padrão trata todos os erros de palavra com o mesmo peso; a ponderação por palavra é a variação (Weighted-Word Scoring). O item inverte padrão e variação.

### L1-R31 — Gabarito: C

- Item do edital: P2-1.1
- Justificativa: A taxa de erro de sentença divide os pares referência–hipótese incorretos pelo total de pares, e não o número de palavras erradas pelo total de palavras.

### L1-R32 — Gabarito: C

- Item do edital: P2-1.1
- Justificativa: O Amazon Transcribe cria versões diferentes do mesmo trecho com pontuação de confiança; em uma transcrição típica entrega apenas a de maior confiança, e as demais podem ser pedidas como alternativas.

### L1-R33 — Gabarito: E

- Item do edital: P2-1.2
- Justificativa: O Whisper faz previsões autorregressivas sequência a sequência em cada janela: cada token depende dos anteriores. O item troca "autorregressiva" por "não autorregressiva".

### L1-R34 — Gabarito: C

- Item do edital: P2-1.2
- Justificativa: O wav2vec 2.0 aprende representações de fala a partir de dados não rotulados, o que permite aproveitar áudio sem transcrição no pré-treinamento; o ajuste fino é feito depois, com áudio transcrito.

### L1-R35 — Gabarito: E

- Item do edital: P2-1.2
- Justificativa: Segundo o cartão do modelo, cerca de 65% dos dados são áudio em inglês com transcrição em inglês; áudio em outros idiomas com transcrição no mesmo idioma é cerca de 17%. O item troca o grupo majoritário.

### L1-R36 — Gabarito: C

- Item do edital: P2-1.2
- Justificativa: O cartão do modelo registra que o desempenho de transcrição em um idioma se correlaciona diretamente com a quantidade de dados de treino nesse idioma; por isso, idioma pouco representado tende a ter acurácia menor.

### L1-R37 — Gabarito: C

- Item do edital: P2-1.2
- Justificativa: O cartão do modelo recomenda fortemente que os usuários façam avaliações robustas no contexto e no domínio de uso antes de implantar os modelos; avaliar com gravações do Plenário e das comissões aplica a recomendação.

### L1-R38 — Gabarito: E

- Item do edital: P2-1.2
- Justificativa: O cartão diz que a arquitetura sequência a sequência torna o modelo propenso a textos repetitivos, o que pode ser mitigado em certa medida por beam search e ajuste de temperatura, "mas não perfeitamente". O item afirma eliminação completa.

### L1-R39 — Gabarito: C

- Item do edital: P2-1.2
- Justificativa: O item parece contradizer a ideia de modelo único, mas as documentações do NeMo e do ESPnet descrevem a fusão de modelo de linguagem (treinado só com texto) em decodificadores CTC, de transdutor e outros, para elevar a acurácia sem retreinar o modelo de fala. "Notas taquigráficas" é aplicação do item.

### L1-R40 — Gabarito: E

- Item do edital: P2-1.2
- Justificativa: A documentação do ESPnet lista o Conformer entre as opções de codificador dos modelos híbridos CTC/atenção (com Transformer, Branchformer e E-Branchformer), e as opções de decodificador são RNN, Transformer ou S4. O item troca o papel do Conformer, de codificador para decodificador.

### L1-R41 — Gabarito: E

- Item do edital: P2-1.2
- Justificativa: Na documentação do ESPnet, a decodificação conjunta CTC/atenção serve para reforçar o alinhamento monotônico (as palavras seguem a ordem da fala). O item troca esse objetivo pela ordem diferente.

### L1-R42 — Gabarito: C

- Item do edital: P2-1.2
- Justificativa: O README do wav2vec 2.0 lista a combinação de dados de fala de múltiplos domínios em "Robust wav2vec 2.0: Analyzing Domain Shift in Self-Supervised Pre-Training"; tratar a mudança de domínio entre treino e uso é o ponto. O item não afirma ganho numérico.

### L1-R44 — Gabarito: E

- Item do edital: P2-1.2
- Justificativa: A documentação do ESPnet registra a combinação nas duas etapas: treinamento multitarefa CTC/atenção e decodificação conjunta. O item restringe a combinação à decodificação e atribui o treinamento só à atenção.

### L1-R45 — Gabarito: C

- Item do edital: P2-1.2
- Justificativa: O NeMo documenta inferência em áudio com mais de uma hora por atenção local, e o ESPnet lista codificador de autoatenção restrita (Longformer) para sequências longas.

### L1-R46 — Gabarito: C

- Item do edital: P2-1.2
- Justificativa: O item parece subestimar o end-to-end, mas reproduz o que a documentação afirma sobre os modelos do toolkit ("comparable/superior to hybrid DNN/HMM and CTC" em vários benchmarks) e acrescenta, com razão, que isso não equivale a superioridade em qualquer condição.

### L1-R47 — Gabarito: C

- Item do edital: P2-1.3
- Justificativa: Multimodal = o mesmo modelo aceita várias modalidades de entrada; o áudio é uma delas, ao lado de texto e, em alguns modelos, imagem e vídeo.

### L1-R48 — Gabarito: E

- Item do edital: P2-1.3
- Justificativa: Receber o áudio como entrada não determina a modalidade de saída. A saída pode ser texto ou áudio; a compreensão de áudio do Google Cloud (Gemini Enterprise Agent Platform, Audio understanding) devolve texto (resumo, transcrição, tradução), e a saída falada é capacidade adicional dos modelos fala-para-fala.

### L1-R49 — Gabarito: C

- Item do edital: P2-1.3
- Justificativa: Falsa pegadinha: soa como erro dizer que o modelo ignora parte do áudio, mas a documentação prevê o truncamento do excedente do limite de tokens; por isso a cobertura do texto deve ser conferida. O item usa "pode" e "convém", sem afirmar que sempre ocorre.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-R50 — Gabarito: E

- Item do edital: P2-1.3
- Justificativa: Temperatura zero escolhe sempre o token mais provável, e as respostas ficam "em grande parte determinísticas", mas "ainda é possível uma pequena variação"; não há garantia de textos rigorosamente idênticos.

### L1-R51 — Gabarito: C

- Item do edital: P2-1.3
- Justificativa: A página limita a compreensão de áudio à fala ("speech only") e adverte que os modelos podem errar ao reconhecer sons que não são fala; aplausos e ruídos do Plenário entram nessa advertência, e as marcações de ruído pedem conferência na revisão.

### L1-R52 — Gabarito: E

- Item do edital: P2-1.3
- Justificativa: O modelo recebe o áudio; a transcrição da fala do usuário é um recurso complementar, ligado por configuração, e não a entrada que o modelo processa.

### L1-R53 — Gabarito: C

- Item do edital: P2-1.3
- Justificativa: 12.000 palavras × 100/75 = 16.000 tokens; 16.000 ÷ 8.000 = 2 respostas, no mínimo. Os valores são hipóteses do enunciado.

### L1-R54 — Gabarito: E

- Item do edital: P2-1.3
- Justificativa: Segundo a documentação do Google Cloud, para gerar carimbos de tempo precisos em arquivos só de áudio nos modelos Gemini é preciso configurar o parâmetro próprio (audio_timestamp); pedir os tempos na instrução não basta.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-R55 — Gabarito: C

- Item do edital: P2-1.3
- Justificativa: Modelos de fala conversacionais anunciam ancoragem em dados da organização por RAG e chamada de funções (ferramentas); a combinação permite que a resposta venha de dados consultados.

### L1-R56 — Gabarito: E

- Item do edital: P2-1.3
- Justificativa: A documentação indica o streaming para reduzir a percepção de latência de quem aguarda; o processamento total da requisição não diminui por isso.

### L1-R57 — Gabarito: C

- Item do edital: P2-1.3
- Justificativa: Os modelos conversacionais de fala descrevem a interrupção pelo usuário (barge-in) com manutenção do contexto. O item usa "pode permitir", sem afirmar a presença do recurso em todo modelo.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-R58 — Gabarito: C

- Item do edital: P2-1.3
- Justificativa: Em serviço conversacional de áudio nativo, a conexão bidirecional persistente permite enviar o áudio do usuário em fluxo contínuo enquanto o modelo processa a fala e gera a resposta, sem esperar o conteúdo completo, como ocorre no padrão de requisição e resposta. O item afirma o que a conexão "permite", sem generalizar a todo produto.

### L1-R59 — Gabarito: E

- Item do edital: P2-1.3
- Justificativa: O áudio enviado compõe o prompt: o limite de áudio por prompt é dado em duração e em tokens. Tokens da resposta são os gerados pelo modelo (o resumo, por exemplo).

### L1-R60 — Gabarito: E

- Item do edital: P2-1.3
- Justificativa: 16 × 8 = 128 minutos, menos que 130; como 130 ÷ 8 = 16,25 e não existe fração de conexão, são necessárias 17 conexões (arredondamento para cima). Os valores são hipóteses do enunciado.

### L1-R61 — Gabarito: E

- Item do edital: P2-1.4
- Justificativa: A DER é taxa de erro, expressa em percentual: quanto menor, melhor. O sistema com maior DER nas mesmas gravações é o de pior desempenho.

### L1-R62 — Gabarito: C

- Item do edital: P2-1.4
- Justificativa: O pipeline de código aberto é executado na máquina do usuário (o exemplo traz o comentário "runs locally"), em oposição ao serviço premium, executado nos servidores do fornecedor; o áudio não precisa sair do ambiente do órgão.

### L1-R63 — Gabarito: E

- Item do edital: P2-1.4
- Justificativa: Recursos variam por modelo e por método: no Chirp 3, a diarização consta como disponível só no lote (BatchRecognize), e os carimbos por enunciado só no streaming. Oferta em um modo não permite concluir "necessariamente" a oferta no outro.

### L1-R64 — Gabarito: C

- Item do edital: P2-1.4
- Justificativa: Falsa pegadinha: a sobreposição de tempos não é defeito; é o modo de a transcrição por canais registrar a fala simultânea de pessoas em canais distintos.

### L1-R65 — Gabarito: E

- Item do edital: P2-1.4
- Justificativa: Na saída de exemplo, os primeiros resultados parciais trazem "Speaker ID=Unknown" e só depois "Guest-1"; o rótulo do falante pode vir depois, com mais áudio processado.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-R66 — Gabarito: C

- Item do edital: P2-1.4
- Justificativa: Os rótulos genéricos são atribuídos pelo serviço a partir do áudio fornecido a cada processamento; arquivos separados podem renumerar os falantes. Por isso o item usa "pode", e não afirma coincidência nem divergência.

### L1-R67 — Gabarito: E

- Item do edital: P2-1.4
- Justificativa: A documentação pede os dois valores, mínimo e máximo ("You must set the min_speaker_count and max_speaker_count values according to how many speakers you expect"); não é só o máximo.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-R68 — Gabarito: C

- Item do edital: P2-1.4
- Justificativa: 50 × 36 s = 1.800 s = 30 min. Valores do enunciado são hipótese.

### L1-R69 — Gabarito: E

- Item do edital: P2-1.4
- Justificativa: Por padrão a API de transcrição rápida mescla todos os canais de entrada em um só antes de transcrever; para transcrever cada canal de forma independente é preciso configurar.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-R70 — Gabarito: C

- Item do edital: P2-1.4
- Justificativa: Saídas só com tempo e rótulo (como "start=0.2s stop=1.5s speaker_0") não trazem texto; é preciso alinhá-las, por tempo, à saída do ASR para compor a transcrição com falantes.

### L1-R71 — Gabarito: E

- Item do edital: P2-1.4
- Justificativa: Há serviços que marcam cada palavra com o rótulo de falante, o que permite representar a troca de orador no meio de uma frase. "Todos" e "nunca" tornam a afirmação falsa.

### L1-R72 — Gabarito: C

- Item do edital: P2-1.4
- Justificativa: Falsa pegadinha: parece óbvio que transcrever em pt-BR implicaria diarizar em pt-BR. A documentação mantém listas separadas de idiomas para transcrição e para diarização; no Chirp 3, por exemplo, pt-PT consta na de transcrição e não na de diarização. O item afirma só que a oferta não é garantida "por si só".

### L1-R73 — Gabarito: C

- Item do edital: P2-1.4
- Justificativa: O README informa que os modelos e pipelines pré-treinados "can be further finetuned to your own data for even better performance"; o item usa "para buscar melhor desempenho", sem prometer ganho.

### L1-R74 — Gabarito: E

- Item do edital: P2-1.4
- Justificativa: O limite do enunciado (30 falantes, de spk_0 a spk_29) é excedido por 45 oradores; a qualidade do áudio não ultrapassa o limite. Os valores são hipóteses; o formato dos rótulos (30 rótulos de spk_0 a spk_29) vem da documentação.

### L1-R75 — Gabarito: E

- Item do edital: P2-1.5
- Justificativa: Na documentação, a saída traz confiança e marcas de tempo para cada palavra ou sinal de pontuação, e o exemplo de resultado mostra o ponto como item de tipo "punctuation". O item troca o item próprio pelo sinal anexado à palavra.

### L1-R76 — Gabarito: C

- Item do edital: P2-1.5
- Justificativa: Segundo a documentação, ao habilitar a pontuação automática o serviço capitaliza a primeira letra após cada ponto final e cada ponto de interrogação; 9 + 4 = 13. A contagem inclui os dois sinais, e não apenas o ponto final.

### L1-R77 — Gabarito: E

- Item do edital: P2-1.5
- Justificativa: Segundo a documentação, o serviço capitaliza automaticamente nomes próprios e palavras no início de frase. O item troca o alcance do recurso, reduzindo-o ao início de frase.

### L1-R78 — Gabarito: C

- Item do edital: P2-1.5
- Justificativa: A documentação do Amazon Transcribe informa que as palavras são capitalizadas nos idiomas que usam distinção de caixa em seus sistemas de escrita. Em escritas sem essa distinção, não há o que capitalizar.

### L1-R79 — Gabarito: C

- Item do edital: P2-1.5
- Justificativa: No Amazon Transcribe, com a estabilização de resultados parciais, cada item, palavra ou sinal de pontuação, recebe o campo Stable, e os itens não estáveis têm mais chance de mudar. A legenda pode exibi-los em formato diferente, como itálico.

### L1-R80 — Gabarito: E

- Item do edital: P2-1.5
- Justificativa: Na documentação, o Amazon Transcribe adiciona pontuação automaticamente em todos os idiomas suportados; a condição de haver suporte à transcrição de números diz respeito ao formato dos números (algarismos, e não palavras). O item atribui à pontuação a condição que vale para os números.

### L1-R81 — Gabarito: E

- Item do edital: P2-1.5
- Justificativa: A documentação define o WER sobre as palavras e o TER como a medida estendida para o formato final de exibição, com pontuação, capitalização e ITN. O item inverte as atribuições.

### L1-R82 — Gabarito: C

- Item do edital: P2-1.5
- Justificativa: A documentação define TER = (I + D + S) ÷ N sobre os tokens da transcrição de referência: (1 + 2 + 3) ÷ 80 = 0,075, ou 7,5%. O denominador é o total de tokens da referência.

### L1-R83 — Gabarito: C

- Item do edital: P2-1.5
- Justificativa: No modo de ditado do Azure Speech, descrições verbais de pontuação, como "question mark", viram o sinal correspondente. Como a conversão não depende da intenção do orador, a revisão deve conferir os trechos em que a palavra é citada como assunto.

### L1-R84 — Gabarito: C

- Item do edital: P2-1.5
- Justificativa: No Amazon Transcribe, a coluna DisplayAs da tabela do vocabulário personalizado define como a entrada aparece na saída, como em "DynamoDB" e "ABCs". Assim, grafia e caixa do termo podem ser fixadas pela equipe.

### L1-R85 — Gabarito: E

- Item do edital: P2-1.5
- Justificativa: Para medir o TER, a documentação exige que os dados de teste incluam transcrições com formatação de exibição, como pontuação, capitalização e ITN. Sem esses elementos na referência, a medida deixa de refletir o formato final, que é o seu objeto.

### L1-R86 — Gabarito: E

- Item do edital: P2-1.5
- Justificativa: Segundo a documentação, em vez de depender somente de limites de silêncio, a segmentação semântica devolve resultados finais, na maioria dos casos, ao detectar pontuação de fim de frase, como "." ou "?". O item atribui a ela o critério da segmentação por silêncio.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-R87 — Gabarito: E

- Item do edital: P2-1.5
- Justificativa: Na documentação do custom speech, a seção #rewrite do arquivo de formato de exibição reúne pares de reescrita para trocar palavras por motivos como capitalização e correção de grafia; a seção #itn traz padrões de exibição como números, endereços e datas. O item troca a seção.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-R88 — Gabarito: C

- Item do edital: P2-1.5
- Justificativa: A documentação informa que a transcrição rápida, diferentemente da transcrição em lote, produz apenas a forma de exibição, que inclui pontuação e capitalização, e não a forma lexical.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-R89 — Gabarito: C

- Item do edital: P2-1.6
- Justificativa: A nota de transparência do Azure Speech lista o local incompatível entre os fatores que reduzem a acurácia e exige que o idioma especificado corresponda ao falado. O espanhol falado sob configuração pt-BR é o caso.

### L1-R90 — Gabarito: E

- Item do edital: P2-1.6
- Justificativa: A nota de transparência do Azure Speech indica que tanto o orador muito distante quanto o muito próximo do microfone podem prejudicar a qualidade do áudio e a acurácia. O item troca o efeito da proximidade excessiva.

### L1-R91 — Gabarito: C

- Item do edital: P2-1.6
- Justificativa: A nota de transparência da Microsoft cita a fala sobreposta entre os fatores de perda de acurácia, e a documentação do Google informa que pessoas falando ao mesmo tempo podem ser tratadas como ruído de fundo e ignoradas. Convém revisar os apartes.

### L1-R92 — Gabarito: C

- Item do edital: P2-1.6
- Justificativa: A nota de transparência do Azure Speech afirma que termos e jargões de uma organização podem não constar do vocabulário padrão e que palavra inexistente no modelo gera erro de transcrição. Recomenda, então, adicionar vocabulário personalizado.

### L1-R93 — Gabarito: E

- Item do edital: P2-1.6
- Justificativa: Segundo a documentação do Azure Speech, muitas omissões costumam vir de sinal de áudio fraco, e as substituições, de amostra insuficiente de termos do domínio nas transcrições ou no texto relacionado. O item troca as causas.

### L1-R94 — Gabarito: E

- Item do edital: P2-1.6
- Justificativa: A documentação descreve a lista de frases como personalização em tempo de execução, aplicada antes de iniciar o reconhecimento e sem treinamento, e o custom speech como personalização prévia, com treino do modelo. O item inverte os dois.

### L1-R95 — Gabarito: C

- Item do edital: P2-1.6
- Justificativa: A documentação do Azure Speech relaciona os erros de inserção a áudio gravado em ambiente ruidoso, possivelmente com diafonia (crosstalk). A associação está correta: as omissões é que se ligam a sinal fraco.

### L1-R96 — Gabarito: C

- Item do edital: P2-1.6
- Justificativa: A documentação do Azure Speech recomenda múltiplos modelos quando o vocabulário varia entre as áreas do domínio, pois o modelo não precisa filtrar dados de assuntos alheios, mas lembra que o treino exige variedade de dados.

### L1-R97 — Gabarito: E

- Item do edital: P2-1.6
- Justificativa: A documentação do Google informa que valores de boost mais altos tendem a reduzir os falsos negativos, mas podem aumentar os falsos positivos, isto é, a palavra aparecer sem ter sido dita. O item troca os dois efeitos.

### L1-R98 — Gabarito: E

- Item do edital: P2-1.6
- Justificativa: O cartão do modelo Whisper informa que o desempenho é desigual entre sotaques e dialetos de um mesmo idioma e recomenda avaliações robustas no contexto e no domínio de uso. Logo, não há uniformidade que dispense testes por grupo.

### L1-R99 — Gabarito: C

- Item do edital: P2-1.6
- Justificativa: A tabela de uso e tipo de dado do custom speech indica dados de pronúncia (ou pronúncia fonética em texto estruturado) para definir a forma fonética e a de exibição de termo de pronúncia não padrão, como siglas, e texto simples ou estruturado para vocabulário e gramática do setor. O item descreve corretamente o par que costuma ser invertido (falsa pegadinha).

### L1-R100 — Gabarito: C

- Item do edital: P2-1.6
- Justificativa: A documentação de transcribe() descreve initial_prompt como texto de contexto para a primeira janela, como vocabulários personalizados ou nomes próprios, para tornar mais provável a grafia correta. "Mais provável" não equivale a garantia.

### L1-R101 — Gabarito: E

- Item do edital: P2-1.6
- Justificativa: Na documentação do Amazon Transcribe, a entrada de várias palavras do vocabulário personalizado tem as palavras ligadas por hífen (como em Los-Angeles), e a coluna da tabela não admite espaços. O item troca o hífen pelo espaço.

### L1-R102 — Gabarito: E

- Item do edital: P2-1.6
- Justificativa: Segundo a documentação do Google, o boost atribuído a uma frase de várias palavras se aplica à frase inteira e somente a ela; para favorecer trechos, sugere-se acrescentar como entradas adicionais, cada uma com seu boost, os bigramas que a compõem. O item estende o peso aos trechos.

### L1-R103 — Gabarito: E

- Item do edital: P2-1.7
- Justificativa: . Os papéis dos níveis estão trocados (no Amazon Transcribe): o nível de estabilidade alto transcreve mais rápido, com acurácia ligeiramente menor, e o baixo dá a maior acurácia.

### L1-R104 — Gabarito: C

- Item do edital: P2-1.7
- Justificativa: . A boa prática do Amazon Transcribe é, quando o fluxo não contém fala, enviar a mesma quantidade de silêncio; no PCM, o silêncio é uma sequência de bytes zero.

### L1-R105 — Gabarito: C

- Item do edital: P2-1.7
- Justificativa: . A documentação indica gravar a 16.000 Hz quando possível, como melhor compromisso entre qualidade e volume de dados pela rede, e observa que microfones de alta qualidade gravam a 44.100 ou 48.000 Hz.

### L1-R106 — Gabarito: E

- Item do edital: P2-1.7
- Justificativa: . O model card diz que os modelos Whisper não podem ser usados para transcrição em tempo real fora da caixa; terceiros podem construir aplicações de tempo quase real sobre eles. A equipe não pode dispensar a aplicação adicional.

### L1-R107 — Gabarito: E

- Item do edital: P2-1.7
- Justificativa: . Trocados os papéis: o síncrono é bloqueante e responde só depois de processar todo o áudio; o streaming fornece resultados intermediários enquanto o áudio é captado.

### L1-R108 — Gabarito: E

- Item do edital: P2-1.7
- Justificativa: . Trocados os papéis: Recognizing carrega os resultados intermediários e Recognized, os finais (tentativa de reconhecimento bem-sucedida).

### L1-R109 — Gabarito: C

- Item do edital: P2-1.7
- Justificativa: . No enunciado único o fim é determinado por silêncio ao final ou por um máximo de áudio processado; no contínuo, a aplicação controla quando parar.

### L1-R110 — Gabarito: E

- Item do edital: P2-1.7
- Justificativa: Dado sujeito a mudança (risco médio; limitação documentada de serviço, verificado em 18/10/2026). A API REST para áudio curto devolve apenas resultados finais e não oferece resultados parciais; para texto parcial ao vivo usa-se o Speech SDK.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-R111 — Gabarito: E

- Item do edital: P2-1.7
- Justificativa: . Fala longa sem pausas, na segmentação só por silêncio, gera subsegmentação (bloco longo de texto sem quebras); a fragmentação por pausas curtas é a sobressegmentação, outro problema.

### L1-R112 — Gabarito: C

- Item do edital: P2-1.7
- Justificativa: . Falsa pegadinha: "streaming" descreve a entrega do áudio em blocos sequenciais e inclui mídia pré-gravada, além de transmissões ao vivo.

### L1-R113 — Gabarito: C

- Item do edital: P2-1.7
- Justificativa: . Ao exceder a cota de fluxos simultâneos, repete-se com backoff exponencial e, se o limite for atingido de forma recorrente, solicita-se aumento da cota.

### L1-R114 — Gabarito: E

- Item do edital: P2-1.7
- Justificativa: Dado sujeito a mudança (risco médio; limite de serviço, verificado em 18/10/2026). No Amazon Transcribe, a duração máxima é limite fixo que não pode ser aumentado; para continuar, inicia-se nova sessão de streaming.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-R115 — Gabarito: E

- Item do edital: P2-1.7
- Justificativa: . O identificador do falante é genérico, atribuído pelo serviço durante o reconhecimento; o nome do parlamentar não vem do serviço, e a associação continua necessária.

### L1-R116 — Gabarito: C

- Item do edital: P2-1.7
- Justificativa: . A documentação recomenda fortemente os SDKs em vez de HTTP/2 ou WebSockets diretos, por serem o método mais simples e confiável.

### L1-R117 — Gabarito: E

- Item do edital: P2-1.8
- Justificativa: . Os modelos .en são as versões somente em inglês (tiny, base, small, medium); para transcrever português é preciso um modelo multilíngue.

### L1-R118 — Gabarito: C

- Item do edital: P2-1.8
- Justificativa: . A boa prática é usar codec sem perdas (FLAC ou LINEAR16); MP3 e outros codecs com perdas podem reduzir a acurácia.

### L1-R119 — Gabarito: E

- Item do edital: P2-1.8
- Justificativa: . Cerca de 65% (438 mil horas) é áudio em inglês com transcrição em inglês; a fala não inglesa com transcrição no próprio idioma é cerca de 17% (117 mil horas).

### L1-R120 — Gabarito: C

- Item do edital: P2-1.8
- Justificativa: . Falsa pegadinha: a lista de frases é recurso de tempo de execução, fornecido pouco antes do reconhecimento, e não exige treinar modelo (diferente do custom speech).

### L1-R121 — Gabarito: E

- Item do edital: P2-1.8
- Justificativa: . A orientação é evitar reamostrar e enviar o áudio na taxa nativa (por exemplo, 8.000 Hz da telefonia); o ideal de 16.000 Hz vale para a captação, não para conversão posterior.

### L1-R122 — Gabarito: C

- Item do edital: P2-1.8
- Justificativa: . O model card atribui a alucinação ao treinamento fracamente supervisionado com dados ruidosos em larga escala; a revisão humana cobre esse risco.

### L1-R123 — Gabarito: E

- Item do edital: P2-1.8
- Justificativa: . Trocado o modo: no lote, submete-se o áudio e recupera-se o resultado depois, de forma assíncrona; o item o descreve como síncrono, na própria chamada.

### L1-R124 — Gabarito: C

- Item do edital: P2-1.8
- Justificativa: . O model card adverte contra o uso dos modelos Whisper para transcrever gravações de pessoas feitas sem o consentimento delas; o item reproduz a advertência, sem acrescentar vínculo.

### L1-R125 — Gabarito: E

- Item do edital: P2-1.8
- Justificativa: . Polaridade invertida: aplicar redução de ruído antes do envio tende a reduzir a acurácia, e o controle automático de ganho não deve ser usado; o serviço foi projetado para áudio ruidoso.

### L1-R126 — Gabarito: C

- Item do edital: P2-1.8
- Justificativa: . Falsa pegadinha: o model card admite que os modelos podem apresentar diarização, sobretudo se ajustados, mas diz que não foi avaliada de forma robusta; não é capacidade validada.

### L1-R127 — Gabarito: E

- Item do edital: P2-1.8
- Justificativa: . Papéis trocados: o vocabulário personalizado melhora a acurácia de palavras específicas; o filtro de vocabulário altera palavras na saída (mascarar, remover ou marcar).

### L1-R128 — Gabarito: C

- Item do edital: P2-1.8
- Justificativa: . A documentação recomenda comparar a transcrição do modelo base com a transcrição humana do mesmo áudio, obter o WER e, se alto, treinar um modelo personalizado.

### L1-R129 — Gabarito: C

- Item do edital: P2-1.8
- Justificativa: . O README informa, e a conduta de ressalvar é a correta, porque as velocidades relativas foram medidas com fala em inglês em uma A100 e a velocidade real pode variar significativamente com idioma, velocidade da fala e hardware.

### L1-R130 — Gabarito: C

- Item do edital: P2-1.8
- Justificativa: . A documentação diz que o serviço usa modelos treinados para tipos de áudio específicos e que informar a fonte do áudio na requisição pode melhorar os resultados; nenhum nome de modelo é cobrado.

### L1-R131 — Gabarito: E

- Item do edital: P2-1.2
- Justificativa: O README do wav2vec 2.0 trata o pré-treinamento auto-supervisionado (aprendizado de representações a partir de áudio sem rótulos) e o autotreinamento como técnicas complementares, tanto que registra a combinação das duas. O item troca "complementares" por "excludentes". "Complementary" consta do próprio README, no texto do link da linha 7.
