# Simulado 2 — P2 final (Reconhecimento de Fala, Transcrição e IA, itens 1 a 4) — folha

- Tipo: final
- Versão: v1
- Número de itens: 40

Julgue cada item (C = certo, E = errado). Gabarito no arquivo SIM-2_gabarito.md.

**Comando.** Julgue os itens a seguir (C = certo, E = errado).

**1** — Os direitos morais do autor, como o de ter seu nome indicado na utilização da obra, são inalienáveis e irrenunciáveis, de modo que não se transmitem com a cessão total dos direitos patrimoniais.

**2** — Em contrato de serviço de transcrição, o SLA (acordo de nível de serviço) pode fixar metas de prazo e de qualidade, de modo que a entrega no prazo, isoladamente, não comprova o cumprimento do acordo se a meta de qualidade não for atingida.

**3** — Por integrarem acústica e linguagem em uma rede única, os modelos de fala end-to-end são imunes a erros de "alucinação", pois só transcrevem o que foi efetivamente pronunciado.

**4** — Se uma obra está disponível publicamente na internet, seus direitos patrimoniais encontram-se em domínio público, e ela pode ser reproduzida livremente por terceiros.

**5** — Editores de transcrição costumam sincronizar texto e áudio por marcações de tempo, o que permite ao revisor ouvir o trecho correspondente a cada passagem do texto e corrigi-lo no próprio editor.

**6** — Em um enunciado que use o verbo "identificar", o sentido da expressão depende do verbo, e não do seu objeto; assim, "identificar que há três oradores" e "identificar os oradores pelo nome" exigem, igualmente, apenas que as vozes sejam distinguidas umas das outras.

**7** — Em sistemas que reconhecem a forma falada, converter "vinte e cinco por cento" em "25%" é operação de normalização inversa de texto, aplicada sobre palavras já reconhecidas, e não etapa de reconhecimento acústico.

**8** — No jargão da área, "transcrição automática" designa a conversão de gravação em texto feita por uma pessoa que ouve o áudio e redige o conteúdo, ao passo que "degravação" designa a conversão feita por software de reconhecimento de fala, sem intervenção humana.

**9** — A sumarização automática de uma sessão equivale à transcrição da sessão em versão reduzida, pois ambas reproduzem as falas dos oradores, diferindo apenas no tamanho do texto produzido.

**10** — Elevar a sensibilidade de endpointing no reconhecimento em streaming reduz a latência de finalização dos resultados, mas pode fragmentar enunciados quando o orador faz pausas, de modo que latência e acurácia não melhoram simultaneamente.

**11** — A busca semântica sempre retorna resultados mais precisos do que a busca por palavras-chave, inclusive quando o usuário procura o número exato de uma proposição ou um nome próprio específico.

**12** — Substituir o nome de cada orador por um código e manter, em arquivo separado sob controle do próprio órgão, a tabela que relaciona códigos e nomes equivale à anonimização, de modo que os dados passam a não ser considerados pessoais para os fins da LGPD.

**13** — Resumos gerados automaticamente a partir de transcrições podem omitir ou distorcer informações relevantes, razão pela qual, em documentos de caráter oficial, devem passar por revisão humana antes de sua publicação.

**14** — LLMs multimodais de áudio nativo recebem o áudio como modalidade de entrada do próprio modelo, sem que o fluxo dependa de um módulo ASR separado para converter a fala em texto antes do processamento.

**15** — Na busca semântica, a consulta e os trechos do acervo são representados em um espaço vetorial, no qual textos de significado próximo ficam próximos, o que permite recuperar documentos relevantes mesmo quando não compartilham as mesmas palavras da consulta.

**16** — Na sumarização extrativa, o sistema redige frases novas que não constam do texto original, ao passo que, na sumarização abstrativa, seleciona e copia trechos que já existem no original.

**17** — Modelos de fala end-to-end continuam dependendo de pares áudio–texto para treinamento, ainda que a supervisão possa ser "fraca", isto é, obtida de transcrições preexistentes não produzidas para esse fim.

**18** — A fidelidade da transcrição exige que toda e qualquer pausa do orador seja registrada no texto, independentemente de sua duração ou relevância, sob pena de omissão de conteúdo.

**19** — A indexação de pronunciamentos consiste em associar a cada documento metadados e termos que permitam recuperá-lo posteriormente, e pode ser apoiada por inteligência artificial, por exemplo na extração de temas e de entidades mencionadas, como nomes de pessoas e números de proposições.

**20** — Em fluxo com human in the loop, é suficiente que o revisor confira apenas os trechos que o sistema marcou com baixa confiança, uma vez que os trechos de alta confiança estão, por definição, corretos.

**21** — Como o WER é calculado pela divisão do número de erros pelo número de palavras da transcrição de referência, ele nunca ultrapassa 100%.

**22** — Quando um trecho da gravação é inaudível, o revisor pode completá-lo com a palavra mais provável segundo o contexto, sem nenhuma marcação no texto, desde que o resultado seja coerente com o restante do pronunciamento.

**23** — Embora o modelo end-to-end mapeie o áudio diretamente ao texto em uma rede única, em muitos sistemas o sinal continua sendo convertido em representação acústica, como um espectrograma, antes de entrar na rede.

**24** — No pipeline clássico de reconhecimento automático de fala, o modelo de linguagem associa trechos de áudio a unidades sonoras, ao passo que o modelo acústico estima quais sequências de palavras são mais prováveis.

**25** — A revisão humana de uma transcrição parlamentar pode apoiar-se em informações externas ao áudio, como a pauta, a lista de oradores inscritos e glossários da Casa, para corrigir nomes, siglas e atribuição de falas que o reconhecimento automático tenha errado.

**26** — Em transcrições de reuniões com vários oradores, cada fala deve ser atribuída a um orador identificado de forma padronizada, e a troca de orador deve ser sinalizada de modo que o leitor distinga quem falou em cada trecho.

**27** — Um modelo geral multilíngue pode ser adaptado a um domínio, como o legislativo, por meio de técnicas como o ajuste fino com textos do domínio ou o uso de recuperação de documentos oficiais, sem que isso exija treiná-lo do zero.

**28** — Na revisão em dupla, o mesmo revisor relê o texto em dois momentos distintos, o que é equivalente à revisão por dois profissionais independentes, pois o segundo exame repete o primeiro.

**29** — As siglas pronunciadas pelo orador devem ser sempre expandidas por extenso na transcrição, por ser essa a única forma de registro admitida em textos parlamentares.

**30** — Os agentes de tratamento devem adotar medidas de segurança, técnicas e administrativas, aptas a proteger os dados pessoais contra acessos não autorizados e contra situações acidentais ou ilícitas de destruição, perda, alteração, comunicação ou tratamento inadequado, e essas medidas devem ser observadas desde a concepção do produto ou serviço até a sua execução.

**31** — A gravação da voz de um parlamentar identificado e a transcrição de suas falas constituem informação relacionada a pessoa natural identificada e, portanto, dados pessoais para os fins da LGPD.

**32** — Termo fora do vocabulário (OOV) é aquele que o sistema reconhece com baixa confiança, e não aquele que está ausente do vocabulário do modelo.

**33** — Alimentar o sistema com as correções feitas pelos revisores, por exemplo acrescentando nomes e termos corrigidos a um glossário, faz parte da melhoria contínua do fluxo, mas não elimina a necessidade de revisão humana das transcrições seguintes.

**34** — A capitalização automática distingue com segurança os nomes próprios das palavras comuns, de modo que "Câmara", como instituição, e "câmara", como sala, nunca são confundidas por esse recurso.

**35** — A métrica DER (diarization error rate) agrega erros de atribuição de falante, fala não detectada e falsos alarmes, sendo distinta do WER, que mede erros de palavras.

**36** — Em um serviço de transcrição contratado por um órgão público, quem decide as finalidades do tratamento dos dados pessoais é o operador, ao passo que o controlador limita-se a executar as instruções do operador.

**37** — Modelos end-to-end modernos podem gerar pontuação e capitalização como parte da própria saída de texto, ao passo que arquiteturas tradicionais de ASR em geral recorrem a etapa posterior de restauração de pontuação.

**38** — A adaptação de vocabulário (speech adaptation ou custom vocabulary) consiste no retreinamento do modelo acústico com gravações do domínio, sendo, por isso, a técnica indicada para corrigir erros causados por sotaques regionais.

**39** — Na revisão de uma transcrição, um erro que altere o sentido da fala, como a omissão de uma negação ou a troca de um número, é mais grave do que uma falha de grafia que não comprometa a compreensão, razão pela qual critérios de qualidade costumam distinguir a gravidade dos erros.

**40** — Modelo de ASR de código aberto executado localmente e serviço de ASR em nuvem são equivalentes quanto à custódia do áudio, pois em ambos os casos a instituição mantém controle exclusivo sobre os dados processados.
