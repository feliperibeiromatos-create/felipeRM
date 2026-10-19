# Lote 1 — Reconhecimento de Fala e Transcrição de Áudio (P2 1.1–1.8) — itens

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

## Itens de reforço

**L1-R01** — Um sistema de reconhecimento automático de fala obteve WER baixo em testes com gravações de reuniões de comissão, captadas em sala silenciosa. Com base nesse resultado, a equipe concluiu que o desempenho será equivalente no Plenário, em sessões com apartes, ruído de fundo e microfones variados, uma vez que o WER é propriedade do modelo e independe do conjunto de áudio avaliado.

**L1-R02** — Sistemas de reconhecimento automático de fala podem entregar, além do texto, marcas de tempo e uma medida de confiança associadas às palavras reconhecidas, informações que, no registro de sessões da Câmara, podem ser usadas para sincronizar o texto com o vídeo e para orientar a revisão humana para os trechos de menor confiança.

**L1-R03** — Em modelos de fala end-to-end multitarefa, como o Whisper, a escolha entre transcrever, traduzir a fala ou identificar o idioma é definida por módulos externos encadeados ao modelo, e não por tokens especiais processados pelo próprio decodificador.

**L1-R04** — Na implementação de referência do Whisper, um arquivo de áudio longo é transcrito por meio de janelas sucessivas de 30 segundos, porque o modelo processa trechos de áudio de duração fixa, e não o arquivo inteiro de uma só vez.

**L1-R05** — Uma equipe da Casa envia a um LLM multimodal de áudio nativo a gravação de uma audiência pública e, em requisições separadas, pede ao mesmo modelo a transcrição, um resumo e uma tradução da fala, alterando apenas a instrução em linguagem natural enviada junto com o áudio. Esse uso é compatível com o funcionamento desse tipo de modelo.

**L1-R06** — Considere que um LLM de áudio nativo converta cada segundo de áudio em 30 tokens de entrada. Nessa hipótese, a gravação integral de uma sessão de 2 horas ocuparia 108.000 tokens do contexto do modelo.

**L1-R07** — Em uma reunião de comissão na qual cada parlamentar fala em um microfone gravado em canal de áudio próprio, a atribuição das falas pode apoiar-se na separação por canais, abordagem distinta da diarização, que distingue os falantes a partir das características da voz em um mesmo canal.

**L1-R08** — Ao planejar o uso de pontuação e capitalização automáticas na transcrição do Plenário, a equipe deve confirmar, na documentação do fornecedor, se o recurso é suportado para o português do Brasil e para o modo de uso pretendido (em lote ou em tempo real), pois a disponibilidade de recursos pode variar conforme o idioma e o modo.

**L1-R09** — Em serviços de reconhecimento de fala que devolvem mais de uma representação do mesmo trecho reconhecido, a forma lexical já incorpora capitalização e pontuação, ao passo que a forma de exibição traz apenas as palavras como reconhecidas, sem esses ajustes.

**L1-R10** — Na montagem de um vocabulário personalizado para o ASR usado nas comissões, a equipe deve limitar a lista a termos úteis ao reconhecimento, como siglas, nomes de proposições e nomes próprios de parlamentares, e evitar nela informações confidenciais e dados pessoais que nada acrescentam ao reconhecimento, como números de documentos e informações de saúde, ainda que a finalidade da lista seja apenas melhorar o reconhecimento.

**L1-R11** — Um fornecedor divulga que seu modelo multilíngue de ASR alcança baixo WER em inglês. Com base apenas nessa informação, a equipe da Câmara conclui que o desempenho em português brasileiro será igualmente bom, pois, em modelos multilíngues, o desempenho independe do idioma.

**L1-R12** — Para escolher entre as grafias de palavras homófonas, como "sessão", "seção" e "cessão", o ASR recorre sobretudo ao modelo acústico, responsável por usar o contexto das palavras vizinhas para decidir a grafia.

**L1-R13** — Na transcrição em streaming, o tamanho dos blocos de áudio enviados pelo cliente não influencia a latência, que é determinada exclusivamente pelo modelo de reconhecimento no servidor.

**L1-R14** — Em transmissão de áudio para reconhecimento em streaming, com áudio PCM de 16 bits (2 bytes por amostra), um canal e taxa de amostragem de 16.000 Hz, cada bloco de 100 ms de áudio equivale a 3.200 bytes.

**L1-R15** — Na cobertura ao vivo de uma sessão plenária, a transcrição em streaming, por entregar o texto mais rápido, tem acurácia garantidamente igual ou superior à da transcrição em lote do mesmo áudio.

**L1-R16** — A Câmara pretende obter, diretamente do áudio em português de uma sessão, um texto em inglês para a imprensa estrangeira. De acordo com a documentação do repositório do Whisper, isso é possível por meio da tarefa de tradução dos modelos multilíngues treinados para essa tarefa, que converte fala em outro idioma em texto em inglês.

**L1-R17** — No Amazon Transcribe, a transcrição em lote exige que o áudio seja entregue em blocos sequenciais e que a resposta seja devolvida em tempo real, ao passo que a transcrição em streaming opera sobre arquivos de mídia previamente enviados ao serviço.

**L1-R18** — O Whisper é distribuído em modelos de tamanhos diferentes, que trocam velocidade por acurácia: o modelo tiny tem cerca de 39 milhões de parâmetros e o modelo large, cerca de 1.550 milhões.

**L1-R19** — Na avaliação de um sistema de reconhecimento automático de fala, a transcrição de referência de um trecho de comissão tem 50 palavras. A hipótese gerada pelo sistema contém 3 substituições, 1 supressão e 2 inserções, de modo que tem 51 palavras. Nesse caso, o WER é de cerca de 11,8%, resultado da divisão do total de erros (6) pelo número de palavras da hipótese.

**L1-R20** — A equipe constatou que, na transcrição automática de sessões de comissão, predominavam substituições em nomes de proposições e de parlamentares. A documentação da Microsoft costuma associar esse padrão de erro à amostra insuficiente de termos do domínio, e atribui o excesso de supressões, em regra, ao sinal de áudio fraco.

**L1-R21** — Em avaliação do WER de um sistema, a degravação usada como referência continha omissões e erros de grafia. Como o WER resulta da comparação entre hipótese e referência, tais falhas da referência só distorcem a medida nos trechos em que o sistema comete exatamente o mesmo erro da referência.

**L1-R22** — Depois de ajustar um modelo de reconhecimento de fala com gravações de sessões da Casa, a equipe avaliou sua acurácia com áudios diferentes dos usados no ajuste, porque, segundo a documentação da Microsoft, essa escolha dá uma noção mais realista do desempenho do modelo.

**L1-R23** — Para obter melhores resultados na transcrição automática do acervo de áudio das sessões, as documentações do Google Cloud Speech-to-Text e do Amazon Transcribe recomendam usar formato com perda, como o MP3, em vez de formatos sem perda, como o FLAC.

**L1-R24** — Em gravações de Plenário com muito ruído de fundo, a documentação do Google Cloud Speech-to-Text recomenda aplicar processamento de redução de ruído ao áudio antes de enviá-lo ao serviço, pois isso tende a elevar a acurácia do reconhecimento.

**L1-R25** — Segundo a documentação do Google Cloud Speech-to-Text, deve-se capturar o áudio com taxa de amostragem de 16.000 Hz ou superior, sempre que possível; no caso de gravações telefônicas, cuja taxa nativa costuma ser de 8.000 Hz, a orientação é enviar o áudio nessa taxa, sem reamostragem.

**L1-R26** — Para calcular o WER, é preciso alinhar a hipótese à transcrição de referência. Esse alinhamento, feito em ferramentas como o sclite, do NIST, consiste em uma programação dinâmica que minimiza globalmente uma distância de edição ponderada entre as sequências de palavras.

**L1-R27** — Na avaliação da transcrição automática de uma sessão, o erro em que o sistema deixa de reconhecer uma palavra efetivamente pronunciada é classificado como inserção, ao passo que o erro em que o sistema acrescenta ao texto uma palavra não pronunciada é classificado como supressão.

**L1-R28** — Ferramentas de pontuação como o sclite, do NIST, admitem transcrições alternativas de referência para trechos ambíguos da fala, o que permitiria, na avaliação de sessões da Câmara, que o sistema não fosse penalizado por emitir "para" ou "pra", desde que ambas as formas fossem previstas como corretas na referência.

**L1-R29** — Quando vários parlamentares falam ao mesmo tempo ou em volumes muito diferentes e o áudio é gravado em um único canal, a documentação do Google Cloud Speech-to-Text informa que o reconhecedor transcreve normalmente as vozes simultâneas, tratando-as como fala válida.

**L1-R30** — No cálculo-padrão do WER, os erros de palavra recebem pesos diferentes conforme a importância da palavra, de modo que um erro em número ou em nome próprio pesa mais que um erro em artigo; a ponderação uniforme é uma variação opcional prevista em ferramentas como o sclite.

**L1-R31** — Na taxa de erro de sentença, calculada em ferramentas de pontuação como o sclite, do NIST, divide-se o número de pares de referência e hipótese incorretos pelo total de pares, independentemente do número de palavras de cada par.

**L1-R32** — Um sistema de reconhecimento automático de fala pode gerar diferentes versões do mesmo trecho transcrito, associando a cada versão uma pontuação de confiança; em geral, o resultado entregue ao usuário é a versão de maior confiança.

**L1-R33** — No Whisper, a decodificação de cada janela de áudio é não autorregressiva: o modelo prevê todos os tokens da janela de uma só vez, sem que cada token dependa dos tokens previstos anteriormente.

**L1-R34** — Um acervo extenso de áudios de sessões sem transcrição pode ser aproveitado no pré-treinamento de modelos como o wav2vec 2.0, que aprende representações de fala a partir de dados não rotulados.

**L1-R35** — O cartão do modelo Whisper informa que o treinamento usou 680 mil horas de áudio e transcrições coletadas da internet, e que a maior parte desses dados, cerca de 65%, é de áudio em idiomas diferentes do inglês com transcrição no mesmo idioma.

**L1-R36** — Uma equipe pretende usar um modelo end-to-end multilíngue para transcrever um idioma que teve pouca representação nos dados de treino do modelo. Segundo o cartão do modelo Whisper, é esperada, em regra, acurácia menor nesse idioma, pois o desempenho em cada idioma se correlaciona diretamente com a quantidade de dados de treino nele.

**L1-R37** — Antes de adotar o Whisper para apoiar o registro das sessões da Câmara, é prudente avaliá-lo com gravações do Plenário e das comissões, pois o cartão do modelo recomenda avaliações robustas no contexto e no domínio de uso antes da implantação.

**L1-R38** — Um revisor encontrou, em transcrição produzida pelo Whisper, trechos em que a mesma frase se repetia. Esse comportamento, a que modelos sequência a sequência são propensos, pode ser eliminado por completo com o uso de busca em feixe (beam search) e de ajuste de temperatura na decodificação.

**L1-R39** — Em um modelo de reconhecimento de fala end-to-end já treinado, com decodificador CTC ou de transdutor, é possível incorporar na decodificação um modelo de linguagem treinado apenas com texto, como o das notas taquigráficas, o que pode aumentar a acurácia sem retreinar o modelo de fala.

**L1-R40** — Ao escolher a arquitetura de um modelo end-to-end híbrido CTC/atenção, a equipe consultou a documentação do ESPnet, segundo a qual o Conformer é uma das opções de decodificador desses modelos, e não de codificador.

**L1-R41** — Em modelos end-to-end híbridos CTC/atenção, como os documentados no ESPnet, a decodificação conjunta com CTC é empregada para permitir que as palavras transcritas surjam em ordem diferente da dos trechos de fala correspondentes.

**L1-R42** — Combinar dados de fala de múltiplos domínios no pré-treinamento do wav2vec 2.0 é uma das estratégias documentadas para tratar a mudança de domínio entre os dados de treino e os de uso, como a diferença entre o material de treinamento e a fala das sessões da Câmara.

**L1-R44** — Segundo a documentação do ESPnet, nos modelos end-to-end híbridos CTC/atenção a combinação das duas abordagens ocorre apenas na decodificação, pois o treinamento é feito somente com o objetivo de atenção.

**L1-R45** — Na transcrição de uma sessão do Plenário com várias horas de duração, modelos end-to-end podem recorrer a mecanismos de atenção local ou restrita no codificador, documentados em toolkits abertos, para processar sequências longas de áudio.

**L1-R46** — Segundo a documentação do ESPnet, os modelos end-to-end desse toolkit alcançam, em vários benchmarks de reconhecimento de fala, desempenho comparável ou superior ao de sistemas híbridos DNN/HMM, o que não implica superioridade em qualquer condição de uso.

**L1-R47** — No LLM multimodal de áudio nativo, a palavra multimodal indica que o mesmo modelo aceita mais de uma modalidade de entrada, como texto e áudio, e o áudio é apenas uma delas.

**L1-R48** — Um LLM multimodal que recebe o áudio diretamente como modalidade de entrada só é capaz de devolver a resposta em áudio sintetizado, e não em texto.

**L1-R49** — Uma equipe envia a um LLM de áudio nativo, em uma única requisição, a gravação de uma sessão cuja duração excede o limite de entrada do modelo. Nessa situação, a parte excedente pode ser truncada e não ser processada, razão pela qual convém conferir se o texto devolvido cobre toda a gravação.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R50** — Ao transcrever repetidamente a mesma gravação com um LLM de áudio nativo, uma equipe configura a temperatura em zero. Nessa situação, as respostas de todas as execuções serão rigorosamente idênticas, pois a temperatura zero elimina toda a aleatoriedade do processo de geração.

**L1-R51** — Em gravações do Plenário, aplausos, vaias e ruídos de fundo não constituem fala, e um LLM de áudio nativo pode errar ao reconhecê-los, o que recomenda a conferência, na revisão, das marcações de ruído do texto.

**L1-R52** — Em uma sessão conversacional com LLM de áudio nativo, a transcrição da fala do usuário que o serviço entrega ao cliente, quando habilitada, é o texto que o modelo recebe como entrada, no lugar do áudio, e é por meio dele que a resposta é elaborada.

**L1-R53** — Considere que, em determinado LLM de áudio nativo, 100 tokens correspondam a cerca de 75 palavras e que o limite de saída de cada resposta seja de 8.000 tokens. Nessa hipótese, a transcrição integral de uma exposição de 12.000 palavras não cabe em uma única resposta, sendo necessárias ao menos duas.

**L1-R54** — Segundo a documentação do Google Cloud para os modelos Gemini, uma equipe que deseje carimbos de tempo precisos na transcrição de um arquivo que contenha somente áudio pode obtê-los apenas pedindo os tempos na instrução em texto, ainda que não faça nenhuma configuração específica de geração.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R55** — Em um assistente de voz da Casa, um LLM de áudio nativo conversacional pode ser combinado à recuperação de dados do acervo (RAG) e à chamada de funções, de modo que a resposta sobre uma proposição se apoie em dados consultados, e não apenas no conhecimento do modelo.

**L1-R56** — Em um LLM de áudio nativo, transmitir a resposta à medida que é gerada (streaming) reduz o tempo total de processamento da requisição, e não apenas a percepção de latência de quem aguarda o texto.

**L1-R57** — Em um serviço de atendimento por voz da Casa, um LLM de áudio nativo conversacional pode permitir que o usuário interrompa a resposta falada e retome o diálogo sem que o modelo perca o contexto da conversa.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R58** — Em um LLM de áudio nativo conversacional, a conexão bidirecional em fluxo contínuo permite que o áudio do usuário seja enviado ao modelo enquanto este processa a fala e gera a resposta, diferentemente do padrão de requisição e resposta, em que o modelo só responde depois de receber o conteúdo completo.

**L1-R59** — Ao enviar a um LLM de áudio nativo a gravação de uma sessão acompanhada de uma instrução de resumo, os tokens correspondentes ao áudio são contabilizados como tokens da resposta gerada, e não como tokens do prompt.

**L1-R60** — Considere que um serviço de áudio nativo em tempo real limite cada conexão a 8 minutos e permita renová-la, com continuação da sessão. Nessa hipótese, 16 conexões consecutivas bastam para o acompanhamento ininterrupto de uma sessão de 130 minutos.

**L1-R61** — Na comparação entre dois sistemas de diarização avaliados sobre as mesmas gravações, o sistema que apresenta a maior taxa de erro de diarização (DER), expressa em percentual, é o de melhor desempenho.

**L1-R62** — Um pipeline de diarização de código aberto pode ser executado localmente, sem que o áudio seja enviado a serviço de terceiros, o que é relevante para gravações de reuniões reservadas.

**L1-R63** — Um órgão verifica que o modelo de reconhecimento de fala de um serviço de nuvem oferece diarização no processamento em lote de arquivos. Nessa situação, ele pode concluir, necessariamente, que o mesmo modelo também oferece diarização no reconhecimento em fluxo contínuo (streaming).

**L1-R64** — Na transcrição por canais, quando dois parlamentares falam ao mesmo tempo em microfones gravados em canais distintos, os intervalos de tempo das falas de cada canal se sobrepõem, o que reflete a simultaneidade das falas.

**L1-R65** — Na diarização em tempo real, em que os resultados parciais são revistos à medida que mais áudio é processado, o primeiro resultado parcial de cada fala já traz o rótulo definitivo do falante, de modo que não há resultado parcial com falante ainda desconhecido.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R66** — Se uma sessão longa for dividida em vários arquivos, processados separadamente por um serviço de diarização, o mesmo rótulo genérico, como Locutor 1, pode designar oradores diferentes em arquivos distintos, independentemente de os arquivos pertencerem à mesma sessão.

**L1-R67** — No Google Cloud Speech-to-Text, a configuração da diarização exige que o cliente informe apenas o número máximo de falantes esperado na gravação, sendo o número mínimo sempre definido pelo próprio serviço a partir do áudio.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R68** — Considere que um sistema de diarização processe cada hora de áudio em 36 segundos. Nessa hipótese, o processamento de 50 horas de gravações de comissões leva cerca de 30 minutos.

**L1-R69** — Para atribuir as falas aos oradores pelos canais, uma equipe envia à API de transcrição rápida do Azure Speech um arquivo estéreo, com um orador em cada canal, sem configurar o tratamento de canais. Nessa situação, cada canal é transcrito de forma independente, por padrão.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R70** — Na transcrição de uma reunião de comissão, uma ferramenta de diarização que devolve apenas intervalos de tempo com rótulos de falante não fornece o texto das falas; a transcrição com a indicação de quem falou exige combinar esses intervalos com a saída de um sistema de reconhecimento de fala.

**L1-R71** — Em todos os serviços de diarização, o rótulo de falante é atribuído apenas a trechos inteiros de fala, e nunca a palavras individuais, o que impede representar a troca de orador no meio de uma frase, como em um aparte.

**L1-R72** — Uma equipe constata que um modelo de reconhecimento de fala oferece transcrição em português do Brasil. Nessa situação, isso não garante, por si só, que o mesmo modelo ofereça diarização nesse idioma, pois a relação de idiomas com diarização pode ser mais restrita que a de transcrição.

**L1-R73** — Há ferramentas de diarização de código aberto com pipelines pré-treinados que podem ser ajustados com dados próprios, como gravações de sessões da Casa, para buscar melhor desempenho nesse tipo de áudio.

**L1-R74** — Considere um serviço de diarização que diferencie, no máximo, 30 falantes distintos por arquivo, rotulados de spk_0 a spk_29. Nessa hipótese, uma sessão gravada em um único arquivo, com 45 oradores diferentes, terá todos eles distinguidos, desde que o áudio tenha boa qualidade.

**L1-R75** — Nos resultados do Amazon Transcribe, os sinais de pontuação inseridos na transcrição não constam como itens próprios da saída: cada sinal é anexado ao texto da palavra anterior, e somente as palavras recebem marcas de tempo e medida de confiança.

**L1-R76** — O Speech-to-Text do Google, com a pontuação automática habilitada, capitaliza a primeira letra após cada ponto final e cada ponto de interrogação inseridos. Em um trecho com 9 pontos finais e 4 pontos de interrogação, cada um seguido de outra palavra, essa regra resulta na capitalização de 13 palavras.

**L1-R77** — Na formatação do texto de exibição do Azure Speech, a capitalização automática restringe-se à primeira palavra de cada frase, de modo que nomes próprios, como o de um parlamentar citado da tribuna, não são capitalizados por esse recurso.

**L1-R78** — Em um serviço de ASR multilíngue, a capitalização automática de palavras somente se aplica aos idiomas cujo sistema de escrita distingue letras maiúsculas e minúsculas.

**L1-R79** — Em legenda ao vivo, os resultados parciais do segmento em andamento podem ser revistos, inclusive quanto à pontuação: há serviços que indicam, para cada palavra ou sinal, se o item já é estável, e a legenda pode exibir de forma distinta os ainda instáveis.

**L1-R80** — Segundo a documentação do Amazon Transcribe, a pontuação automática é inserida somente nos idiomas que contam com suporte à transcrição de números em algarismos; nos demais, a saída da transcrição vem sem sinais de pontuação.

**L1-R81** — No Azure Speech, o WER é a medida estendida que avalia o texto final de exibição, com pontuação, capitalização e normalização de números, enquanto o TER, por sua vez, limita-se às palavras do formato lexical.

**L1-R82** — Em um teste do Azure Speech, a referência feita por revisores tinha 80 tokens, e o texto reconhecido teve 1 token inserido, 2 omitidos e 3 substituídos. Nessa situação, o TER, calculado pela soma dos erros dividida pelo número de tokens da referência, é de 7,5%.

**L1-R83** — Em sistema de ASR que interpreta a pontuação falada, a palavra "vírgula", dita por um parlamentar ao se referir ao texto de um dispositivo, pode ser convertida no sinal gráfico, independentemente de ter sido citada como assunto, o que exige atenção do revisor.

**L1-R84** — Há serviços de ASR em que o vocabulário personalizado permite associar a cada termo a forma como ele deve aparecer na saída, o que possibilita fazer constar da transcrição siglas e nomes próprios da Casa com a grafia e as maiúsculas desejadas.

**L1-R85** — Uma equipe pretende medir o TER do ASR da Casa, no Azure Speech, usando como referência transcrições de sessões revisadas apenas quanto às palavras, sem pontuação nem letras maiúsculas. Nessa situação, a referência é adequada, ainda que não tenha esses elementos, pois o TER avalia o texto reconhecido contra as palavras da referência.

**L1-R86** — Na transcrição ao vivo de uma sessão com o Azure Speech, a segmentação semântica do reconhecimento contínuo devolve resultados finais apenas quando detecta silêncio prolongado, sem levar em conta a pontuação de fim de frase, que é irrelevante para o fechamento do segmento.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R87** — Considere que uma equipe pretenda fazer o Azure Speech escrever com iniciais maiúsculas o nome de um órgão, como Câmara dos Deputados, quando o texto reconhecido o apresentar em minúsculas. Nessa situação, deve cadastrar a regra no arquivo de formato de exibição personalizado do custom speech, na seção #itn, que se destina a trocar palavras por motivos como capitalização e correção de grafia.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R88** — Considere que uma equipe precise da forma lexical do texto reconhecido, sem pontuação e sem capitalização. Nessa situação, a API de transcrição rápida do Azure Speech não atende à necessidade, porque produz apenas a forma de exibição, ao contrário da API de transcrição em lote.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R89** — Uma equipe configura o reconhecimento de uma audiência pública para o português do Brasil, mas um convidado estrangeiro passa a falar em espanhol. Nessa situação, a acurácia da transcrição tende a diminuir no trecho em espanhol, pois o idioma configurado deve corresponder ao efetivamente falado no áudio.

**L1-R90** — Segundo a nota de transparência do Azure Speech, na captação do áudio do Plenário para o ASR, o microfone muito afastado do orador reduz a acurácia do reconhecimento, ao passo que o microfone muito próximo da boca a melhora, por captar a voz com mais nitidez.

**L1-R91** — Nos apartes, em que dois parlamentares falam ao mesmo tempo, a acurácia do ASR tende a cair, e há orientação de fornecedor segundo a qual pessoas que falam simultaneamente podem ser interpretadas como ruído de fundo e ignoradas, o que recomenda a conferência desses trechos pelo revisor.

**L1-R92** — Segundo a nota de transparência do Azure Speech, quando uma palavra que não existe no modelo aparece no áudio, o resultado é um erro de transcrição; por isso, siglas, jargões e nomes próprios específicos da Casa estão entre os termos mais sujeitos a erro e justificam o uso de listas de termos.

**L1-R93** — Na análise dos erros de um teste de ASR com termos da Casa, quando predominam as omissões de palavras, a causa mais provável é a amostra insuficiente de termos do domínio nos dados de treino, ao passo que as substituições costumam decorrer de sinal de áudio fraco.

**L1-R94** — No Azure Speech, a lista de frases (phrase list) exige o treinamento prévio de um modelo com dados da Casa, ao passo que o custom speech é aplicado em tempo de execução, imediatamente antes do reconhecimento, sem necessidade de treinar modelo.

**L1-R95** — Considere que, em teste do ASR com gravações de comissão feitas com ruído de fundo e falas cruzadas, o texto reconhecido tenha apresentado muitas palavras inseridas que ninguém disse. Nessa situação, o resultado é compatível com a orientação de que erros de inserção indicam gravação em ambiente ruidoso.

**L1-R96** — Quando o vocabulário usado em áreas de atuação distintas da Casa difere de modo significativo, pode ser vantajoso treinar modelos customizados separados para cada área, em vez de um modelo único, desde que haja dados de treinamento com variedade suficiente em cada uma.

**L1-R97** — Nas ferramentas de adaptação de vocabulário que permitem atribuir peso (boost) às frases, elevar muito o valor do boost para o nome de um parlamentar reduz os falsos positivos, isto é, os casos em que o nome aparece na transcrição sem ter sido dito, mas aumenta os falsos negativos.

**L1-R98** — Em razão de ter sido treinado com grande volume de dados diversos, o Whisper apresenta desempenho uniforme entre sotaques e dialetos de um mesmo idioma, de modo que a avaliação do modelo com um grupo de falantes pode dispensar testes com os demais grupos regionais.

**L1-R99** — Segundo a documentação do Azure Speech, para siglas e outros termos da Casa cuja pronúncia não é a padrão, a personalização indicada é a de dados de pronúncia, que definem a forma fonética e a forma de exibição do termo, e não a de texto simples, que se destina ao vocabulário e à gramática específicos do setor.

**L1-R100** — Uma forma de orientar o Whisper de código aberto a grafar corretamente nomes próprios e termos específicos da Casa é fornecer, como prompt inicial da primeira janela, um texto com esse vocabulário, o que torna mais provável a grafia correta, mas não a garante.

**L1-R101** — Considere que a equipe monte o vocabulário personalizado do Amazon Transcribe para as audiências públicas e queira incluir, como uma única entrada, o nome Comissão de Constituição e Justiça. Nessa situação, deve separar as palavras da entrada por espaços, e não por hífen.

**L1-R102** — Segundo a documentação do Speech-to-Text do Google, ao atribuir valor de boost a uma frase de várias palavras, como o nome completo de um órgão da Casa, o peso incide também sobre cada trecho do nome, o que dispensa cadastrar como entradas adicionais as combinações de palavras que o compõem.

**L1-R103** — No Amazon Transcribe em streaming, que permite estabilizar os resultados parciais, o nível de estabilidade mais alto produz o texto mais preciso, enquanto o nível mais baixo entrega o texto com maior rapidez, ainda que com acurácia ligeiramente menor.

**L1-R104** — Na transmissão de áudio PCM de uma reunião de comissão ao Amazon Transcribe em streaming, o cliente deve enviar a mesma quantidade de áudio, independentemente de haver fala, codificando o silêncio como bytes zero.

**L1-R105** — A taxa de amostragem de 16.000 Hz é indicada para a transcrição em streaming por equilibrar qualidade e volume de dados na rede, embora microfones de alta qualidade gravem a 44.100 ou 48.000 Hz.

**L1-R106** — Uma equipe da Câmara pretende legendar sessões ao vivo com os modelos Whisper publicados pela OpenAI e supõe que eles, tal como distribuídos, já realizam transcrição em tempo real, de modo que pode dispensar qualquer aplicação construída sobre os modelos para esse fim.

**L1-R107** — No Google Cloud Speech-to-Text, o reconhecimento síncrono devolve resultados intermediários enquanto o áudio ainda está sendo captado, ao passo que o reconhecimento em streaming, próprio para áudio ao vivo, só responde depois de processado todo o áudio enviado.

**L1-R108** — No reconhecimento contínuo do Speech SDK, do Azure Speech, o evento Recognizing traz os resultados finais, que indicam uma tentativa de reconhecimento bem-sucedida, enquanto o evento Recognized traz os resultados intermediários.

**L1-R109** — No Speech SDK, o reconhecimento de enunciado único termina por silêncio ao final da fala ou por limite de áudio processado, enquanto no reconhecimento contínuo a aplicação decide quando parar.

**L1-R110** — Para exibir ao público, durante a sessão, o texto parcial da fala de cada orador, a Câmara pode usar a API REST para áudio curto do Azure Speech, que devolve resultados parciais à medida que o áudio é enviado, e não apenas o resultado final de cada trecho.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R111** — Quando a segmentação do reconhecimento em tempo real se baseia apenas no silêncio, um orador que fala por longo tempo sem pausas tende a ter a sua fala fragmentada em trechos muito curtos.

**L1-R112** — Na transcrição em streaming, o áudio chega ao serviço em uma sequência de blocos, de modo que o recurso pode ser aplicado também a mídia previamente gravada, e não apenas a transmissões ao vivo.

**L1-R113** — Se a transcrição simultânea de várias comissões exceder a cota de fluxos concorrentes, é adequado repetir a tentativa com espera exponencialmente crescente e, se o limite for atingido de forma recorrente, pedir aumento da cota.

**L1-R114** — Uma sessão plenária longa ultrapassou a duração máxima permitida para um único fluxo de transcrição em streaming do Amazon Transcribe. Nesse caso, o procedimento correto é solicitar à AWS o aumento desse limite de duração, que pode ser ampliado sob pedido.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R115** — No Azure Speech, a diarização em tempo real devolve, para cada trecho transcrito, o nome do orador, o que dispensa a equipe da Casa de associar, depois, o falante identificado ao parlamentar correspondente.

**L1-R116** — Na integração do sistema de transcrição das comissões ao Amazon Transcribe em streaming, a documentação recomenda fortemente usar os SDKs da AWS, e não montar diretamente conexões HTTP/2 ou WebSocket, por serem o método mais simples e confiável.

**L1-R117** — Ao planejar a degravação automática das sessões do Plenário em português, a equipe da Câmara pode usar o modelo medium.en do Whisper, pois os modelos com sufixo .en são as versões multilíngues de cada tamanho.

**L1-R118** — Segundo as boas práticas do Google Cloud Speech-to-Text, é preferível gravar e transmitir o áudio em codec sem perdas, como FLAC ou LINEAR16, pois codecs com perdas, como o MP3, podem reduzir a acurácia do reconhecimento.

**L1-R119** — De acordo com o model card do Whisper, a maior parte das 680 mil horas de áudio coletadas na internet para o treinamento corresponde a fala não inglesa com transcrição no próprio idioma.

**L1-R120** — No Azure Speech, a lista de frases (phrase list) é informada em tempo de execução, pouco antes do reconhecimento, e favorece o reconhecimento de nomes e siglas sem exigir o treinamento de um modelo personalizado.

**L1-R121** — Uma gravação antiga de audiência pública foi captada com taxa de amostragem de 8.000 Hz. Segundo as boas práticas do Google Cloud Speech-to-Text, para melhorar a acurácia a equipe deve reamostrar o áudio para 16.000 Hz antes de enviá-lo ao serviço.

**L1-R122** — Como o Whisper foi treinado de forma fracamente supervisionada com dados ruidosos em larga escala, a saída pode conter trechos não falados no áudio, o que reforça a necessidade de revisão humana da degravação.

**L1-R123** — Na transcrição em lote (batch) do Azure Speech, a aplicação envia o áudio e recebe o resultado de forma síncrona, na própria chamada, sem necessidade de consultar o andamento da tarefa nem de recuperar o resultado depois.

**L1-R124** — Ao planejar a degravação de reuniões reservadas das comissões com o Whisper, a equipe deve levar em conta que o model card adverte contra o uso dos modelos para transcrever gravações de pessoas feitas sem o consentimento delas.

**L1-R125** — Antes de enviar ao Google Cloud Speech-to-Text a gravação de uma comissão feita em sala ruidosa, a equipe deve aplicar redução de ruído e controle automático de ganho, pois esse pré-processamento tende a elevar a acurácia do reconhecimento.

**L1-R126** — De acordo com o model card do Whisper, a diarização de falantes é uma capacidade que os modelos podem apresentar, sobretudo se ajustados para essa tarefa, mas que não foi avaliada de forma robusta.

**L1-R127** — No Amazon Transcribe, o filtro de vocabulário serve para melhorar o reconhecimento das palavras listadas, ao passo que o vocabulário personalizado serve para mascarar, remover ou marcar palavras específicas na saída da transcrição.

**L1-R128** — Uma equipe da Câmara avalia se o modelo base do Azure Speech atende ao Plenário. Segundo a documentação, ela pode comparar a transcrição do modelo com a humana do mesmo áudio pelo WER e, se este for alto, treinar um modelo personalizado.

**L1-R129** — Uma equipe estimou o tempo de degravação do acervo com as velocidades relativas da tabela do Whisper, medidas com fala em inglês em GPU A100, e agiu corretamente ao ressalvar que a velocidade real pode variar muito com o idioma e o hardware.

**L1-R130** — No Google Cloud Speech-to-Text, a requisição pode indicar o modelo de reconhecimento, treinado para determinado tipo de áudio, o que tende a melhorar os resultados quando a fonte do áudio é conhecida.

**L1-R131** — Uma equipe da Câmara dispõe de extenso acervo de áudio de sessões sem transcrição e de poucas horas de áudio transcrito. Nessa situação, segundo o README oficial do wav2vec 2.0, o pré-treinamento auto-supervisionado e o autotreinamento (self-training) são técnicas excludentes.

**L1-R132** — Ao segmentar o áudio de uma sessão por silêncios para submetê-lo ao reconhecimento, a equipe obtém trechos que, na terminologia da documentação do CMUSphinx, são chamados de utterances: trechos de áudio separados por pausas, formados por palavras e sons não linguísticos, que não correspondem necessariamente a sentenças.

**L1-R133** — Segundo a documentação do CMUSphinx, a velocidade de um decodificador pode ser expressa em múltiplos do tempo de gravação (xRT). Nessa convenção, um arquivo de áudio com 2 horas de gravação cuja decodificação levou 6 horas tem velocidade de 3xRT.

**L1-R134** — No sclite, do NIST, palavras da referência podem ser marcadas como opcionais, colocando-as entre parênteses. De acordo com a documentação, quando se usa a opção -D, a palavra opcional da referência que o sistema deixa de emitir é tratada como correta, e não como supressão.

**L1-R135** — Ao pontuar a transcrição de uma sessão com o sclite, do NIST, a equipe usa referência e hipótese no formato ctm e a opção -T, que ativa o alinhamento mediado por tempo. Segundo a documentação, esse alinhamento substitui os pesos fixos de distância entre palavras por medidas baseadas em pesos predefinidos atribuídos a cada palavra.

**L1-R136** — Segundo a documentação do CMUSphinx sobre os conceitos básicos do reconhecimento de fala, os trifones, que são fones considerados em contexto, com o fone vizinho à esquerda e o da direita, correspondem a partes de fones entre dois fones consecutivos, ao passo que os difones ocupam o mesmo trecho da forma de onda que o fone isolado e diferem deste apenas pelo nome.

**L1-R137** — De acordo com a documentação do Google Cloud Speech-to-Text, descrever na configuração da requisição a codificação correta do áudio e usar o idioma e o modelo de reconhecimento corretos contribui para a transcrição mais precisa e para a cobrança correta da requisição.

**L1-R138** — Entre as medidas de desempenho de um sistema de reconhecimento de fala citadas na documentação do CMUSphinx, a acurácia (accuracy) é calculada com as mesmas contagens de erros usadas no WER, exceto por não levar em conta as supressões.

**L1-R139** — Na API REST de reconhecimento de áudio curto do Azure Speech, o resultado com status NoMatch indica que foi detectada fala no fluxo de áudio, mas nenhuma palavra do idioma-alvo foi reconhecida, o que normalmente significa que o idioma de reconhecimento configurado é diferente do idioma falado pelo usuário.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R141** — Segundo a documentação do CMUSphinx, o lattice é um grafo dirigido que representa variantes do reconhecimento, ao passo que a lista N-best representa essas variantes de forma mais densa que o lattice.

**L1-R142** — O artigo que apresenta o Whisper informa que os modelos são treinados para prever o texto bruto das transcrições, sem padronização significativa, o que dispensa uma etapa separada de normalização inversa de texto para a obtenção de transcrições de aspecto natural.

**L1-R143** — Segundo o artigo que apresenta o Whisper, os autores mantiveram no conjunto de treinamento as transcrições geradas por outros sistemas de reconhecimento automático de fala, em vez de removê-las por meio de heurísticas de detecção.

**L1-R144** — Na montagem dos dados de treinamento do Whisper, segundo o artigo que apresenta o modelo, um par formado por áudio em francês e transcrição em inglês não é incluído como exemplo de reconhecimento de fala, pois o idioma falado não corresponde ao da transcrição; esse par é aproveitado como exemplo de tradução da fala para o inglês.

**L1-R145** — De acordo com o artigo do Whisper, os trechos de áudio sem fala foram excluídos do conjunto de treinamento.

**L1-R146** — Segundo o artigo do Whisper, o áudio é reamostrado a 16.000 Hz e convertido em um espectrograma log-Mel de 80 canais, calculado em janelas de 10 milissegundos com deslocamento de 25 milissegundos.

**L1-R147** — Uma equipe pretende usar a versão multilíngue do Whisper para transcrever sessões em português. Segundo o artigo que apresenta o modelo, nos modelos multilíngues o vocabulário do tokenizador foi reajustado, mantido o mesmo tamanho, porque o vocabulário BPE do GPT-2, usado nos modelos apenas em inglês, fragmentaria excessivamente outros idiomas.

**L1-R148** — Na transcrição de áudio longo, o artigo do Whisper descreve que a temperatura de decodificação parte de 0 e é elevada em 0,2, até o máximo de 1,0, sempre que o texto gerado apresenta taxa de compressão gzip inferior a 2,4.

**L1-R149** — Para evitar que o modelo ignore as primeiras palavras do áudio na transcrição de gravações longas, o artigo do Whisper restringe o token de carimbo de tempo inicial a um valor entre 0,0 e 1,0 segundo.

**L1-R150** — Segundo o artigo do Whisper, na detecção de trechos sem fala em áudio longo, a probabilidade do token de ausência de fala é, por si só, suficiente para distinguir um segmento sem fala.

**L1-R151** — No pré-treinamento do wav2vec 2.0, a entrada de fala é mascarada no espaço latente, e o modelo resolve uma tarefa contrastiva definida sobre uma quantização das representações latentes, aprendidas em conjunto.

**L1-R152** — O artigo que apresenta o AudioPaLM descreve um modelo que funde um modelo de linguagem textual e um de fala em uma arquitetura multimodal única, capaz de processar e gerar texto e fala, e que herda do AudioLM a capacidade de preservar informações paralinguísticas, como a identidade do falante e a entonação.

**L1-R153** — Segundo o artigo do AudioPaLM, inicializar o modelo com os pesos de um grande modelo de linguagem treinado somente com texto prejudica o processamento de fala.

**L1-R154** — O SALMONN integra um grande modelo de linguagem textual pré-treinado a codificadores de fala e de áudio em um único modelo multimodal, o que permite ao LLM processar diretamente entradas de áudio de natureza geral, entre elas fala, eventos sonoros e música.

**L1-R155** — No SALMONN, o módulo de conexão entre os codificadores de áudio e o LLM converte a saída do codificador em um número fixo de tokens de áudio, qualquer que seja a duração da gravação.

**L1-R156** — O Qwen2-Audio apresenta dois modos de interação com áudio: no modo de conversa por voz, o usuário interage com o modelo por voz, sem entrada de texto; no modo de análise de áudio, o usuário fornece áudio e instruções em texto para a análise.

**L1-R157** — Segundo o artigo do Qwen2-Audio, diante de um trecho de áudio que contém ao mesmo tempo sons, conversa entre vários falantes e um comando de voz, o modelo é capaz de entender diretamente o comando e fornecer uma interpretação e uma resposta ao áudio.

**L1-R158** — Segundo o artigo do Qwen2-Audio, o pré-treinamento foi simplificado com o uso de tags hierárquicas complexas no lugar de prompts em linguagem natural para os diferentes dados e tarefas.

**L1-R159** — Em um serviço de atendimento por voz da Casa baseado em modelo de fala para fala, segundo a documentação do Amazon Nova 2 Sonic, a resposta falada pode ter a forma de entrega ajustada dinamicamente de acordo com a prosódia da fala do usuário.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R160** — Uma equipe pretende enviar, em um único prompt a modelo Gemini por meio do Google Cloud, os arquivos de áudio de três reuniões de comissão. Segundo a documentação sobre compreensão de áudio, o número máximo de arquivos de áudio por prompt é um, de modo que as três gravações não podem ser enviadas, como três arquivos, no mesmo prompt.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R161** — Segundo a documentação de áudio da Mistral AI, a oferta de modelos para tratamento de áudio inclui apenas modelo de entrada de áudio voltado a tarefas por instrução, não havendo modelo de áudio otimizado especificamente para transcrição.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R162** — Uma equipe avalia, com a taxa de erro de diarização (DER) do pyannote.metrics em sua configuração padrão, um sistema de diarização que não inclui módulo de detecção de fala sobreposta, usando gravações de comissão com muitos apartes. Nessa situação, segundo a documentação, a métrica leva em conta a fala sobreposta, o que pode aumentar a detecção perdida atribuída ao sistema.

**L1-R163** — Na avaliação de sistemas de diarização, é comum remover da avaliação uma faixa (colar) em torno de cada fronteira de turno de fala, porque os sistemas automáticos não conseguem determinar essas fronteiras com precisão no nível da amostra de áudio.

**L1-R164** — Considere um arquivo de 100 s em que a fala de referência soma 80 s. Um sistema de diarização apresentou 4 s de falso alarme, 2 s de fala perdida e 6 s de confusão de falantes. Nessa situação, segundo a definição de DER da documentação do pyannote.metrics, a DER é de 12%, resultado de 12 s de erro divididos pelos 100 s de duração do arquivo.

**L1-R165** — Na avaliação de um sistema de diarização, o sistema rotulou como spk_0 o orador que a anotação de referência chama de Presidente. Nessa situação, a diferença entre os nomes dos rótulos não constitui, por si só, erro de confusão, pois a DER se apoia em um mapeamento um a um entre os falantes da referência e os do sistema, que, na versão ótima, é calculado pelo algoritmo húngaro de modo a minimizar a confusão.

**L1-R166** — Segundo a documentação do pyannote.metrics, resultados com segmentação excessiva (muitos agrupamentos de falantes) tendem a produzir alta cobertura e baixa pureza, ao passo que resultados com subsegmentação (dois falantes fundidos em um grande agrupamento) levam a alta pureza e cobertura menor.

**L1-R167** — Segundo a nota de transparência do Azure Speech, a qualidade da diarização é medida pela taxa de erro de palavras (WER).

**L1-R168** — Uma equipe envia à transcrição em lote do Azure Speech, com a diarização habilitada, um arquivo estéreo que traz dois oradores. Nessa situação, segundo a documentação, a diarização é aplicada normalmente, pois o recurso foi concebido para gravações com mais de um canal.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R169** — Uma comissão grava a reunião em um único arquivo, com todos os parlamentares falando para um microfone comum na mesma sala, e envia a gravação ao Azure Speech para obter a transcrição com a indicação de quem falou. Nessa situação, segundo a nota de transparência, estar todos os falantes no mesmo ambiente acústico, como o de uma sala em que falam para um microfone comum, é a condição em que o sistema tende a ter melhor desempenho.

**L1-R170** — O sistema de som de um comitê grava o áudio, com um microfone por canal, em um arquivo de quatro canais. Nessa situação, segundo a documentação do Amazon Transcribe, a identificação de canais pode ser usada para transcrever separadamente cada um dos quatro canais.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R171** — Para que a transcrição de uma audiência exiba o nome do presidente da sessão, a API de transcrição da OpenAI, no modelo especializado em diarização, aceita o envio de trechos curtos de áudio de referência de falantes conhecidos, acompanhados dos respectivos nomes, para associar os segmentos de fala a esses falantes.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R172** — No modelo de pontuação e capitalização documentado pelo NeMo, para cada palavra do texto de entrada o modelo prevê a marca de pontuação que deve preceder a palavra e se ela deve ser grafada com inicial maiúscula.

**L1-R173** — Segundo a documentação do NeMo, por padrão o modelo de pontuação e capitalização considera vírgulas, pontos finais e pontos de interrogação, tendo os demais sinais sido removidos dos dados; para que sinais como o ponto e vírgula e os dois-pontos fossem restaurados em transcrições, seria preciso introduzir novos rótulos.

**L1-R174** — Uma equipe usa o script de inferência de pontuação e capitalização do NeMo em um texto de transcrição muito longo, que é dividido em segmentos. Nessa situação, segundo a documentação, como o desempenho do modelo é pior junto às bordas dos segmentos, as previsões feitas para os tokens próximos dessas bordas são privilegiadas no cálculo das previsões finais.

**L1-R175** — O modelo de pontuação e capitalização do NeMo é composto de dois classificadores no nível de token, um para a pontuação e outro para a capitalização, treinados em conjunto sobre um modelo de linguagem pré-treinado, e opera sobre texto, e não sobre o sinal de áudio.

**L1-R176** — A avaliação do modelo de pontuação e capitalização do NeMo gera um único relatório de taxa de erro de palavras (WER), que cobre ao mesmo tempo a pontuação e a capitalização.

**L1-R177** — Uma equipe percebe que a transcrição de audiências, feita com um modelo de transcrição da API da OpenAI que aceita prompt, vem sem a pontuação e as iniciais maiúsculas adotadas na Casa. Nessa situação, segundo o guia da API, o prompt não é recurso adequado para isso, pois serve apenas para melhorar o reconhecimento de nomes, siglas e vocabulário específico da gravação, e não para preservar pontuação nem capitalização.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R178** — Segundo a documentação do Google Cloud Speech-to-Text, por padrão o serviço já insere pontuação nos resultados do reconhecimento, de modo que a pontuação automática precisa ser desabilitada quando não for desejada.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R179** — Segundo a documentação do NeMo, no treinamento do modelo de pontuação e capitalização recomenda-se balancear os dados, especialmente para a tarefa de pontuação.

**L1-R180** — Em legenda ao vivo de uma sessão produzida com o Azure Speech, a equipe percebe que os resultados parciais (evento Recognizing) chegam sem pontuação. Segundo a documentação do serviço, isso é esperado, pois a pontuação dos resultados parciais não está disponível.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R181** — O normalizador de texto básico do repositório oficial do Whisper, usado para uniformizar textos antes de compará-los, converte o texto em minúsculas e substitui por espaço símbolos e sinais de pontuação; por isso, depois dessa normalização, os trechos "Senhor Presidente, a sessão" e "senhor presidente a sessão" tornam-se idênticos, e a comparação não registra a diferença de vírgula nem de maiúsculas entre eles.

**L1-R182** — Uma sessão do Plenário começa em português e, em certo momento, um convidado passa a falar em espanhol. Se o idioma não for informado ao Whisper de código aberto, segundo o código de referência, o modelo detecta o idioma a cada janela de 30 segundos, o que faz o trecho em espanhol ser transcrito como espanhol.

**L1-R183** — Para melhorar o reconhecimento de siglas da Casa, a equipe pode preencher, na tabela de vocabulário personalizado do Amazon Transcribe, as colunas SoundsLike e IPA, que o serviço usa para orientar a pronúncia dos termos.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R184** — Uma equipe do Amazon Transcribe envia, na mesma requisição, um modelo de linguagem personalizado e um vocabulário personalizado com formas de exibição (DisplayAs) para siglas da Casa. Nessa situação, segundo a documentação, as formas de exibição do vocabulário não são aplicadas à saída enquanto o modelo de linguagem personalizado estiver ativo.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R185** — Uma equipe pretende usar, na transcrição de audiências, um modelo de linguagem personalizado do Amazon Transcribe e, ao mesmo tempo, a identificação automática de idioma. Nessa situação, segundo a documentação, ao se incluir um modelo de linguagem personalizado na requisição não é possível habilitar a identificação de idioma, sendo preciso especificar o código do idioma.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R186** — Segundo o cartão do modelo Whisper, os estudos indicam que, em comparação com muitos sistemas de ASR existentes, os modelos exibem robustez melhorada a sotaques e a ruído de fundo, mas essa melhora não alcança a linguagem técnica.

**L1-R187** — Segundo a documentação do Google Cloud Speech-to-Text, a adaptação de modelo tem, por padrão, efeito forte sobre o reconhecimento, sobretudo para frases de uma só palavra.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R188** — Segundo a nota de transparência do Azure Speech, os modelos de fala são treinados com dados de voz que incluem diversos estilos de fala, idiomas, sotaques, dialetos e entonações, além de variações acústicas geradas por diferentes tipos de dispositivos de gravação.

**L1-R189** — A lista de idiomas do Whisper de código aberto traz códigos de idioma distintos para o português do Brasil e para o português de Portugal, o que permite informar ao modelo a variante regional da fala a ser transcrita.

**L1-R190** — Uma equipe do Google Cloud Speech-to-Text inclui sessão e seção em um conjunto de frases de adaptação, sem atribuir valores de boost. Nessa situação, segundo a documentação, o modelo passa a reconhecer sessão com probabilidade maior que seção.

**L1-R191** — Ao cadastrar, no vocabulário personalizado do Amazon Transcribe para o português, termos da Casa como Constituição e proposições, a equipe verifica que, segundo a documentação, só podem ser usados os caracteres do conjunto do idioma e que o conjunto do português para o campo Phrase inclui, além das letras de A a Z, o apóstrofo, o hífen e o ponto, letras acentuadas e o cedilha.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R192** — Segundo a documentação do Amazon Transcribe, na transcrição em streaming de uma sessão, o serviço divide o áudio recebido em segmentos naturais de fala, como a troca de orador ou uma pausa no áudio, e devolve os resultados parciais de cada segmento até que ele seja integralmente transcrito.

**L1-R193** — Uma equipe da Câmara transmite ao Amazon Transcribe, em streaming, áudio PCM de dois canais, um por microfone, em blocos de 2.002 bytes. Segundo a documentação, esse tamanho é adequado, pois, com dois canais, cada amostra ocupa dois bytes e basta que o bloco tenha número par de bytes.

**L1-R194** — Uma equipe pretende legendar ao vivo as sessões do Plenário com o Cloud Speech-to-Text, do Google, mas dispõe apenas de aplicações que fazem chamadas REST. Segundo a documentação do serviço, o reconhecimento em streaming está disponível somente por gRPC, de modo que essas aplicações não poderão usá-lo para esse fim.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R195** — Durante um teste de carga, a equipe da Câmara aumentou rapidamente o número de fluxos simultâneos de transcrição em streaming no Amazon Transcribe e recebeu o erro LimitExceededException. Segundo a documentação, nessa causa específica do erro, a solução é pedir o aumento da cota de fluxos simultâneos pelo console de Service Quotas.

**L1-R196** — Para exibir ao público a legenda de uma sessão à medida que o orador fala, a equipe deve habilitar, na configuração do reconhecimento em streaming do Google Cloud Speech-to-Text (API v2), o envio de resultados intermediários; sem essa opção, apenas a resposta final é devolvida ao cliente.

**L1-R197** — Na configuração de tempo limite por atividade de voz do reconhecimento em streaming do Google Cloud Speech-to-Text (API v2), o speech_start_timeout encerra o fluxo quando, depois de detectada a fala, não se detecta mais fala dentro da duração definida, ao passo que o speech_end_timeout encerra o fluxo quando a fala não começa dentro dessa duração.

**L1-R198** — Uma equipe da Câmara usa a identificação automática de idioma do Amazon Transcribe em streaming em reuniões de comissão nas quais predomina o português, com falas ocasionais em outro idioma. Segundo a referência da API, informar um idioma preferencial pode ajudar o serviço a identificar o idioma mais rapidamente do que se esse parâmetro fosse omitido.

**L1-R199** — No reconhecimento em streaming do Google Cloud Speech-to-Text (API v2), com os eventos de atividade de voz habilitados, o evento SPEECH_ACTIVITY_END indica que o servidor detectou o início da voz humana no fluxo, e o evento SPEECH_ACTIVITY_BEGIN, o seu fim.

**L1-R200** — Na legenda ao vivo de uma sessão com o Azure Speech, a equipe quer manter a baixa latência dos resultados parciais e obter resultados finais mais precisos. Segundo a documentação, o refinamento pós-fluxo (post-stream refinement) atende a esse objetivo: executa uma segunda passagem de reconhecimento em paralelo ao streaming e substitui apenas o resultado final por uma versão mais precisa, que usa contexto de áudio mais amplo.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R201** — Uma equipe da Câmara pretende transcrever em streaming, no Amazon Transcribe, reuniões com falas em mais de um idioma, com redação automática de dados pessoais (PII). Segundo a referência da API, a identificação automática de idioma em streaming pode ser combinada com a redação de conteúdo na mesma requisição.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L1-R202** — Ao avaliar o Whisper para a degravação de sessões em português, a equipe da Câmara deve considerar que, segundo o model card, os usuários primários pretendidos dos modelos são pesquisadores de IA que estudam sua robustez, generalização, capacidades, vieses e restrições, embora o Whisper também possa ser útil como solução de ASR para desenvolvedores, especialmente para o inglês.

**L1-R203** — Segundo o model card do Whisper, a Câmara pode usar os modelos, além de transcrever os pronunciamentos, para inferir atributos dos oradores, como o estado emocional, a partir do áudio das sessões, pois a classificação é um uso avaliado e apropriado para esses modelos.

**L1-R204** — Uma equipe pretende executar localmente o modelo medium multilíngue do Whisper para degravar sessões em português, em estação cuja placa de vídeo tem 4 GB de memória. Segundo a tabela de modelos do repositório do Whisper, a memória de vídeo (VRAM) requerida por esse modelo é superior à dessa placa.

**L1-R205** — Ao instalar o Whisper em servidor do órgão para degravar as sessões, a equipe constata, pelo repositório do projeto, que o uso do pacote dispensa a instalação, no sistema, da ferramenta de linha de comando ffmpeg.

**L1-R206** — Para degravar a gravação de uma reunião longa de comissão, a equipe usará o reconhecimento assíncrono do Google Cloud Speech-to-Text. Segundo a documentação, esse modo inicia uma operação de longa duração, cujos resultados a aplicação pode consultar periodicamente, ao contrário do reconhecimento síncrono, que é bloqueante.

**L1-R207** — Para obter a transcrição de um arquivo de áudio de audiência o mais rápido possível, com latência previsível, a equipe usa a API de transcrição rápida (fast transcription) do Azure Speech, que, segundo a documentação, devolve os resultados de forma assíncrona, por consulta posterior.

**L1-R208** — Ao usar o Cloud Speech-to-Text, do Google, na degravação de sessões, a equipe deve considerar que o filtro de palavrões, quando ativado, substitui as palavras filtradas por sua primeira letra seguida de asteriscos e opera sobre palavras isoladas, sem detectar fala ofensiva expressa em frase ou em combinação de palavras.

**L1-R209** — No Amazon Transcribe, o vocabulário personalizado aprende o contexto associado a uma palavra, isto é, como e quando ela é usada e sua relação com outras palavras, ao passo que o modelo de linguagem personalizado aumenta o reconhecimento da palavra por meio de dicas, como pronúncias.

**L1-R210** — A Câmara pretende degravar um grande acervo de gravações com a transcrição em lote do Azure Speech. Segundo a documentação, como o serviço agenda os trabalhos em regime de melhor esforço e cada região processa as requisições uma de cada vez, enviá-las em taxa mais alta não acelera o processamento, sendo recomendável distribuí-las ao longo do tempo.

**L1-R211** — Para que o texto de uma reunião reservada, transcrita em streaming no Amazon Transcribe, traga os dados pessoais (PII) sinalizados e, ao mesmo tempo, ocultados, a equipe pode incluir na mesma requisição a identificação de conteúdo (ContentIdentificationType) e a redação de conteúdo (ContentRedactionType); segundo a referência da API, o serviço aceita as duas opções juntas.
