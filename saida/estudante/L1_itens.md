# Lote 1 — RF-ASR (reconhecimento de fala e transcrição, P2 1.1–1.8) — itens

Itens para julgar (C = certo, E = errado). Gabarito e justificativas no arquivo L1_gabarito.md.

**Comando.** Julgue os itens a seguir (C = certo, E = errado).

**L1-Q01** — Como o WER é a razão entre erros e palavras de referência, uma transcrição com WER igual a 0% é necessariamente fiel ao áudio também em pontuação, capitalização e atribuição de locutor.

**L1-Q02** — Um sistema ASR, ao converter em texto o áudio de uma sessão, identifica necessariamente qual parlamentar proferiu cada fala, por ser essa uma etapa intrínseca do reconhecimento de fala.

**L1-Q03** — Por integrarem acústica e linguagem em uma rede única, os modelos de fala end-to-end são imunes a erros de "alucinação", pois só transcrevem o que foi efetivamente pronunciado.

**L1-Q04** — Modelos de fala end-to-end continuam dependendo de pares áudio–texto para treinamento, ainda que a supervisão possa ser "fraca", isto é, obtida de transcrições preexistentes não produzidas para esse fim.

**L1-Q05** — LLMs multimodais de áudio nativo recebem o áudio como modalidade de entrada do próprio modelo, sem que o fluxo dependa de um módulo ASR separado para converter a fala em texto antes do processamento.

**L1-Q06** — Na arquitetura em cascata (ASR → LLM → TTS), o LLM processa diretamente as características acústicas da fala, razão pela qual preserva informação prosódica como entonação e hesitação.

**L1-Q07** — Como a diarização atribui a cada falante um rótulo próprio, um sistema com diarização habilitada, por si só, sem amostras de voz de referência, é suficiente para que a transcrição de uma audiência pública exiba o nome de cada convidado que falou.

**L1-Q08** — A verificação de locutor difere da diarização por operar em comparação um-para-um contra uma identidade alegada, e um sistema pode diarizar uma sessão inteira sem verificar nem identificar ninguém.

**L1-Q09** — A métrica DER (diarization error rate) agrega erros de atribuição de falante, fala não detectada e falsos alarmes, sendo distinta do WER, que mede erros de palavras.

**L1-Q10** — Modelos end-to-end modernos podem gerar pontuação e capitalização como parte da própria saída de texto, ao passo que arquiteturas tradicionais de ASR em geral recorrem a etapa posterior de restauração de pontuação.

**L1-Q11** — Pontuação falada e pontuação automática são recursos distintos: na primeira, o orador dita o sinal de pontuação; na segunda, o sistema infere o sinal a partir da estrutura da frase e, eventualmente, de pistas prosódicas.

**L1-Q12** — Uma vez carregada uma lista de termos parlamentares por adaptação de vocabulário, o sistema ASR passa a reconhecer corretamente esses termos em qualquer condição acústica, independentemente do sotaque do orador.

**L1-Q13** — A adaptação de vocabulário (speech adaptation ou custom vocabulary) consiste no retreinamento do modelo acústico com gravações do domínio, sendo, por isso, a técnica indicada para corrigir erros causados por sotaques regionais.

**L1-Q14** — No Amazon Transcribe, o custom vocabulary amplia o vocabulário base com termos do domínio, enquanto o custom language model é construído a partir de dados de texto fornecidos pelo usuário.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-Q15** — Na transcrição em tempo real (streaming), o sistema pode emitir resultados parciais sujeitos a revisão, e o resultado final de um trecho em geral é consolidado após a detecção do fim do enunciado (endpointing).

**L1-Q16** — Na API de transcrição de arquivos da OpenAI, o parâmetro stream=true transforma a requisição em transcrição em tempo real de áudio ao vivo, equivalendo ao uso de uma sessão da Realtime API.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-Q17** — Elevar a sensibilidade de endpointing no reconhecimento em streaming reduz a latência de finalização dos resultados, mas pode fragmentar enunciados quando o orador faz pausas, de modo que latência e acurácia não melhoram simultaneamente.

**L1-Q18** — O Whisper, da OpenAI, foi disponibilizado como modelo de código aberto executável localmente, enquanto a API da OpenAI oferece, além do whisper-1, modelos de transcrição mais recentes recomendados para transcrição geral de arquivos.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-Q19** — O Azure AI Speech oferece transcrição em tempo real e em lote, mas, por tratar-se de serviço exclusivamente em nuvem, não permite execução em contêineres on-premises.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-Q20** — Modelo de ASR de código aberto executado localmente e serviço de ASR em nuvem são equivalentes quanto à custódia do áudio, pois em ambos os casos a instituição mantém controle exclusivo sobre os dados processados.

**L1C-Q21** — No pipeline clássico de reconhecimento automático de fala, o modelo de linguagem associa trechos de áudio a unidades sonoras, ao passo que o modelo acústico estima quais sequências de palavras são mais prováveis.

**L1C-Q22** — Como o WER é calculado pela divisão do número de erros pelo número de palavras da transcrição de referência, ele nunca ultrapassa 100%.

**L1C-Q23** — Em sistemas de reconhecimento de fala end-to-end, não há dicionário de pronúncias separado a ser editado, de modo que corrigir o reconhecimento de um nome próprio passa, em regra, por adaptação de vocabulário ou por mais dados, e não pela edição de um dicionário de pronúncias do próprio modelo.

**L1C-Q24** — Embora o modelo end-to-end mapeie o áudio diretamente ao texto em uma rede única, em muitos sistemas o sinal continua sendo convertido em representação acústica, como um espectrograma, antes de entrar na rede.

**L1C-Q25** — Por receber o áudio diretamente como entrada, um LLM multimodal de áudio nativo produz sempre uma cópia literal da fala, o que dispensa a revisão humana em registros oficiais.

**L1C-Q26** — Um serviço de reconhecimento de fala cuja qualidade é reforçada por um LLM, mas que apenas converte áudio em texto, é, por esse motivo, um LLM de áudio nativo.

**L1C-Q27** — Quando se afirma que a diarização "identifica" os diferentes oradores de uma gravação, o verbo pode ser entendido no sentido de distinguir um orador do outro, sem que isso implique saber o nome de cada um.

**L1C-Q28** — Em um enunciado que use o verbo "identificar", o sentido da expressão depende do verbo, e não do seu objeto; assim, "identificar que há três oradores" e "identificar os oradores pelo nome" exigem, igualmente, apenas que as vozes sejam distinguidas umas das outras.

**L1C-Q29** — Em registro oficial, a pontuação inserida automaticamente pode alterar o sentido de um enunciado, como na diferença entre uma afirmação e uma pergunta, razão pela qual a revisão deve conferir a pontuação, e não apenas as palavras.

**L1C-Q30** — A capitalização automática distingue com segurança os nomes próprios das palavras comuns, de modo que "Câmara", como instituição, e "câmara", como sala, nunca são confundidas por esse recurso.
