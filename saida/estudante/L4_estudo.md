# Lote 4 — Conceitos básicos de inteligência artificial; Ética e responsabilidade digital no serviço público (P1 5.1–5.3 e 6)

Prova: P1

## Itens do edital

- P1-5.1 — Engenharia de prompts
- P1-5.2 — Aprendizado supervisionado, não supervisionado e por reforço
- P1-5.3 — IA generativa: conceitos, exemplos e casos de uso
- P1-6 — Ética e responsabilidade digital no serviço público

## Resumo

```text
NOTA DO EDITAL (8.11.2): na prova objetiva, cada item vale +1,00 ponto se a marcação concordar com o gabarito oficial definitivo, −1,00 ponto se discordar e 0,00 se não houver marcação ou houver marcação dupla (C e E) (Edital nº 1/2026, subitem 8.11.2).

5.1 ENGENHARIA DE PROMPTS. Prompt = entrada em linguagem natural; engenharia de prompts = projetar e iterar a ENTRADA, sem mexer nos parâmetros (isso é fine-tuning). Elementos: papel, instrução, contexto, exemplos, formato, restrições, delimitadores (Markdown/XML, para separar instruções de dados). Técnicas: zero-shot (sem exemplo), one-shot (um), few-shot (vários; costuma render mais); chain-of-thought (raciocínio passo a passo em UM prompt); prompt chaining (VÁRIOS prompts encadeados); role prompting; RAG (recuperar documentos e inseri-los no prompt). Temperatura: alta = mais variação; baixa = mais previsível, não "mais verdadeira". Alucinação: saída plausível e falsa; bom prompt reduz, não elimina. Injeção de prompt: instrução maliciosa dentro do conteúdo lido.

5.2 TIPOS DE APRENDIZADO. SUPERVISIONADO: dados rotulados; regressão (número) e classificação (categoria; binária/multiclasse). NÃO SUPERVISIONADO: sem rótulos; clustering (o modelo encontra os grupos; o humano pode nomeá-los com base em seu entendimento dos dados — Google for Developers, "Introduction to ML: What is Machine Learning?"), redução de dimensionalidade, anomalias, associação; "não supervisionado" = sem rótulos, não "sem humano" (o humano escolhe dados e parâmetros e interpreta resultados). POR REFORÇO: agente, ambiente, ação, recompensa/penalidade, política; sem rótulo por entrada; robôs, AlphaGo. RLHF = reforço com feedback humano, usado em ciclos de AJUSTE de LLMs. Modelos generativos (Google for Developers, "Introduction to ML: What is Machine Learning?"): pré-treinados com grandes volumes de dados sem rótulos atribuídos manualmente → ajuste supervisionado ou por reforço. "IA generativa baseia-se prioritariamente em supervisionado" = ERRADO.

5.3 IA GENERATIVA. Cria conteúdo novo (texto, imagem, áudio, vídeo, código). Classificar é TAREFA; generativo/discriminativo é TIPO DE MODELO. Generativo modela p(X,Y)/p(X) — a distribuição — e gera (e pode classificar: Naive Bayes); discriminativo modela p(Y|X) — a fronteira. Modelo de fundação: enorme, pré-treinado em dados diversos, base para ajustes; LLM: modelo de linguagem com muitíssimos parâmetros; LLMs de uso geral costumam ser modelos de fundação de linguagem; nem todo modelo de fundação é LLM. Modalidades: texto→texto, →imagem, →vídeo, →código, →fala; imagem→texto; imagem-e-texto→imagem; multimodal. Conceitos: token, janela de contexto, temperatura, alucinação, RAG ≠ fine-tuning, agentes, data de corte (o modelo em si não consulta nada em tempo real). Casos de uso: sumarização, apoio à degravação, minutas, atendimento ao cidadão, busca semântica, acessibilidade, código. Riscos: alucinação, viés, vazamento, dependência, autoria, opacidade.

6 ÉTICA E RESPONSABILIDADE DIGITAL. O servidor responde pelo que faz com meios digitais e IA; a ferramenta não responde. CF art. 37: LIMPE. Decreto 1.171/1994: ética além da legalidade (Seção I, II); vedado DEIXAR DE usar avanços técnicos (XV, "e"). Lei 8.112: sigilo sobre assunto da repartição (116, VIII). LGPD: aplica-se ao Poder Público (art. 1º; Cap. IV, arts. 23–32); dado pessoal / sensível (5º, I, II); encarregado = canal entre controlador, titulares e a Agência Nacional de Proteção de Dados — ANPD (5º, VIII, redação da Lei 15.352/2026); anonimizado não é dado pessoal, salvo reversão (12, caput); princípios (6º, I–X); bases além do consentimento (7º, II, III); revisão de decisão automatizada (20) — sem exigência de pessoa natural (expressão retirada pela MP 869/2018; § 3º da Lei 13.853/2019 vetado); segurança (46) e incidentes (48). LAI: publicidade regra, sigilo exceção (3º, I); informações pessoais (31); prazos 25/15/5 anos (24, § 1º). Lei 9.610: atos oficiais sem proteção autoral (8º, IV). Princípios de IA (síntese autoral): supervisão humana, transparência, não discriminação, privacidade, accountability, segurança, veracidade, recursos públicos, acessibilidade, antidesinformação. Vale a redação em vigor em 2/10/2026 (13.33); legislação sem vigência só se explicitada nos objetos de avaliação (13.34) — o PL 2338/2023 não está, e fica só como contexto, sujeito a mudança.
```

## Curso

```text
## ITEM 5.1 — ENGENHARIA DE PROMPTS

### 5.1.1 DEFINIÇÃO
Prompt é a entrada em linguagem natural (instrução, pergunta, contexto, exemplos) fornecida a um modelo de linguagem para obter uma resposta. Engenharia de prompts é a prática de projetar, testar e iterar prompts para que o modelo produza a saída desejada, SEM alterar os parâmetros internos do modelo. O glossário oficial do Google a define como "the art of creating prompts that elicit the desired responses from a large language model", acrescentando que é atividade humana e que o resultado depende, entre outros fatores, dos dados de treinamento e da temperatura (Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 7/10/2026).
Ponto central para a prova: engenharia de prompts atua na ENTRADA; fine-tuning atua nos PARÂMETROS. O glossário do Google define fine-tuning como "a second, task-specific training pass performed on a pre-trained model to refine its parameters" (Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 7/10/2026).

### 5.1.2 ANATOMIA DE UM PROMPT
1. Papel ou persona — quem o modelo deve "ser". A Anthropic chama isso de role prompting (Anthropic, "Prompt engineering overview"); a OpenAI o coloca na mensagem de papel developer/system, que, segundo o guia oficial, tem prioridade sobre a mensagem do usuário (OpenAI, "Prompt engineering", verificado em 7/10/2026).
2. Instrução ou tarefa — o verbo da ação (resuma, classifique, extraia, reescreva).
3. Contexto ou material de referência — o texto sobre o qual o modelo deve trabalhar. O guia da OpenAI recomenda "include relevant context information", inclusive dados externos ao treinamento recuperados por busca (RAG) (OpenAI, "Prompt engineering", verificado em 7/10/2026).
4. Exemplos — demonstrações de entrada e saída (zero-shot / few-shot, abaixo).
5. Formato de saída — tabela, JSON, número de linhas, "responda apenas C ou E". A OpenAI documenta controle de formato e Structured Outputs (OpenAI, "Prompt engineering").
6. Restrições e critérios — o que NÃO fazer ("não invente nomes", "marque trechos inaudíveis como [inaudível]").
7. Delimitadores — separação das partes do prompt com Markdown ou tags XML, para que o modelo distinga instruções de dados de referência; recomendação explícita da Anthropic ("XML structuring", Anthropic, "Prompt engineering overview") e da OpenAI ("Message formatting with Markdown and XML", OpenAI, "Prompt engineering"), ambas verificadas em 7/10/2026.

### 5.1.3 TÉCNICAS NOMEADAS
- Zero-shot: prompt sem nenhum exemplo de resposta esperada; só a instrução (Google for Developers, "Machine Learning Glossary: Generative AI").
- One-shot: um único exemplo.
- Few-shot: "a prompt that contains more than one (a 'few') example"; segundo o glossário do Google, costuma produzir resultados melhores que zero-shot e one-shot, ao custo de um prompt mais longo (Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 7/10/2026). A OpenAI chama de "few-shot learning" e recomenda exemplos diversos (OpenAI, "Prompt engineering").
- Chain-of-thought (cadeia de pensamento): "a prompt engineering technique that encourages a large language model to explain its reasoning, step by step" (Google for Developers, "Machine Learning Glossary: Generative AI"). A Anthropic menciona a técnica como "thinking" (Anthropic, "Prompt engineering overview").
- Prompt chaining (encadeamento de prompts): dividir uma tarefa complexa em vários prompts sequenciais, em que a saída de um alimenta o seguinte (Anthropic, "Prompt engineering overview", "prompt chaining"). NÃO confundir com chain-of-thought: no chaining há vários prompts; no chain-of-thought há um prompt que pede raciocínio explícito.
- Role prompting / system prompt: atribuição de papel (Anthropic, "Prompt engineering overview"; OpenAI, "Prompt engineering").
- Instruções claras e diretas: primeira técnica mencionada pela Anthropic ("clarity", Anthropic, "Prompt engineering overview"); a OpenAI recomenda instruções explícitas para modelos GPT e objetivos de alto nível para modelos de raciocínio (OpenAI, "Prompt engineering", verificado em 7/10/2026).
- Fornecer contexto / RAG (retrieval-augmented generation): recuperar documentos relevantes (por exemplo, de um banco vetorial) e inseri-los no prompt antes de o modelo responder (OpenAI, "Prompt engineering"). RAG injeta conhecimento NA ENTRADA; fine-tuning altera o MODELO.
- Iteração e avaliação: a Anthropic condiciona a engenharia de prompts a critérios de sucesso claros e testes empíricos (Anthropic, "Prompt engineering overview"); a OpenAI recomenda fixar a versão (snapshot) do modelo em produção e medir o comportamento a cada mudança de prompt (OpenAI, "Prompt engineering", verificado em 7/10/2026).

### 5.1.4 PARÂMETROS E LIMITES
- Temperatura: "a hyperparameter that controls the degree of randomness of a model's output"; valores altos geram respostas mais variadas, valores baixos, mais previsíveis (Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 7/10/2026). Temperatura baixa não significa resposta "mais verdadeira": significa resposta mais determinística.
- Janela de contexto: limite de tokens que o modelo processa por requisição; a OpenAI recomenda planejar o prompt em função desse limite (OpenAI, "Prompt engineering"). Token é a unidade em que o texto é fragmentado para o modelo (conceito geral).
- Alucinação: "the production of plausible-seeming but factually incorrect output by a generative AI model" (Google for Developers, "Machine Learning Glossary: Generative AI"). Um prompt bem construído REDUZ, mas não ELIMINA alucinações.
- Injeção de prompt (conceito geral, sem fonte de fornecedor no tópico 5.1 de TI e Dados): instruções maliciosas embutidas em textos que o modelo lê e que tentam sobrepor-se às instruções legítimas. Mitigação: delimitar dados e tratar conteúdo externo como dado, não como instrução.

### 5.1.5 EXEMPLO APLICADO AO LEGISLATIVO
Situação: servidor do Derep (antigo DETAQ), departamento de registro e redação da Câmara, precisa de um resumo de três páginas de notas taquigráficas de uma audiência pública para subsidiar o relator.
Prompt fraco: "Resuma isso." (sem papel, sem formato, sem restrições, sem delimitação do texto)
Prompt estruturado:
  [Papel] Você é assessor de redação legislativa.
  [Tarefa] Resuma as notas taquigráficas abaixo em até 15 linhas.
  [Formato] Um parágrafo por orador, na ordem das falas; ao final, lista das propostas concretas apresentadas.
  [Restrições] Não atribua a um orador fala que ele não tenha feito; não acrescente informação externa; trechos marcados [inaudível] permanecem assim.
  [Contexto] <notas> ... texto ... </notas>
O que mudou: papel, instrução clara, formato de saída, restrições contra alucinação e delimitação do contexto com tags — as técnicas descritas pela Anthropic ("Prompt engineering overview") e pela OpenAI ("Prompt engineering"). Se o resumo precisasse ainda ser comparado com o relatório do relator, caberia um segundo prompt, encadeado (prompt chaining).

### 5.1.6 PEGADINHAS PROVÁVEIS
P1. "A engenharia de prompts ajusta os pesos do modelo para a tarefa" → ERRADO (isso é fine-tuning).
P2. "Few-shot é o prompt que traz um único exemplo" → ERRADO (um exemplo é one-shot).
P3. "Chain-of-thought consiste em dividir a tarefa em prompts sucessivos" → ERRADO (isso é prompt chaining).
P4. "Temperatura mais baixa produz saídas mais variadas e criativas" → ERRADO (é o inverso).
P5. "Um prompt bem elaborado elimina a possibilidade de alucinação" → ERRADO (reduz, não elimina).
P6. "RAG consiste em retreinar o modelo com os documentos da organização" → ERRADO (RAG recupera documentos e os insere no prompt).
P7. "Zero-shot é a técnica em que o modelo recebe exemplos sem rótulo" → ERRADO (zero-shot = nenhum exemplo).

## ITEM 5.2 — APRENDIZADO SUPERVISIONADO, NÃO SUPERVISIONADO E POR REFORÇO

### 5.2.1 DEFINIÇÃO GERAL
Aprendizado de máquina (ML) é o campo em que sistemas aprendem padrões a partir de dados, em vez de seguir regras explicitamente programadas. A página oficial do Google classifica os sistemas de ML por COMO aprendem, em quatro categorias: supervisionado, não supervisionado, por reforço e IA generativa (Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 7/10/2026). O edital pede os três primeiros aqui e a IA generativa no item 5.3.
Vocabulário transversal (conceitos gerais): atributos ou features, rótulo ou target, conjuntos de treino / validação / teste, generalização, sobreajuste (overfitting) e subajuste (underfitting).

### 5.2.2 APRENDIZADO SUPERVISIONADO
Definição: o modelo aprende a partir de dados ROTULADOS, isto é, exemplos que já trazem a resposta correta, e descobre a relação entre entradas e saídas. O Google compara a um estudante que se prepara com provas antigas já gabaritadas (Google for Developers, "Introduction to ML: What is Machine Learning?").
Duas tarefas clássicas:
- Regressão: prevê um VALOR NUMÉRICO contínuo. Exemplos da página do Google for Developers, "Introduction to ML: What is Machine Learning?" (reverificados em 7/10/2026): quantidade de chuva "in inches or millimeters"; preço futuro de uma casa a partir de metragem, CEP, número de quartos e banheiros e taxa de juros do financiamento ("Future house price"); tempo futuro de viagem até um destino, em minutos e segundos ("Future ride time").
- Classificação: prevê uma CATEGORIA. Exemplos da página do Google for Developers, "Introduction to ML: What is Machine Learning?": e-mail é spam ou não; a foto contém um gato. Pode ser binária ("rain" ou "no rain") ou multiclasse ("rain", "hail", "snow" ou "sleet") (Google for Developers, "Introduction to ML: What is Machine Learning?", reverificado em 7/10/2026).
Chave de prova: "o que o modelo devolve?" Número → regressão. Categoria → classificação. Ambas supervisionadas, porque exigem rótulos no treino.

### 5.2.3 APRENDIZADO NÃO SUPERVISIONADO
Definição: o modelo recebe dados SEM rótulos e busca padrões ou estruturas significativas. A técnica mais citada é o clustering (agrupamento), que reúne dados semelhantes; exemplo da página do Google for Developers, "Introduction to ML: What is Machine Learning?": agrupar dados meteorológicos por temperatura e descobrir as estações do ano.
Distinção decisiva — clustering × classificação (Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 7/10/2026): na classificação, as categorias são DEFINIDAS PREVIAMENTE pelo humano e o modelo atribui cada dado a uma delas; no clustering, os grupos NÃO são definidos previamente: o modelo os encontra, e o humano pode nomear os grupos com base em seu entendimento dos dados (Google for Developers, "Introduction to ML: What is Machine Learning?": "You might then attempt to name those clusters").
Outras tarefas não supervisionadas (conceitos gerais): redução de dimensionalidade, detecção de anomalias e regras de associação.
Armadilha de vocabulário: "não supervisionado" significa SEM RÓTULOS, não "sem participação humana". O humano escolhe os dados e os parâmetros e interpreta os resultados.

### 5.2.4 APRENDIZADO POR REFORÇO
Definição: o modelo (agente) aprende por tentativa e erro, interagindo com um AMBIENTE: executa AÇÕES, recebe RECOMPENSAS ou PENALIDADES e, com isso, constrói uma POLÍTICA (policy), que a página do Google for Developers, "Introduction to ML: What is Machine Learning?", descreve como a melhor estratégia para acumular recompensas (verificado em 7/10/2026). Exemplos da página do Google for Developers, "Introduction to ML: What is Machine Learning?": treinar robôs a caminhar por uma sala e o programa AlphaGo.
Diferença essencial: não há rótulo com a "resposta certa" para cada entrada; há um SINAL DE RECOMPENSA, muitas vezes atrasado. Isso distingue reforço de supervisionado.
Ponte com LLMs — RLHF (aprendizado por reforço com feedback humano): "using feedback from human raters to improve the quality of a model's responses"; o glossário do Google cita avaliações como 👍 e 👎 (Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 7/10/2026). RLHF é uma etapa de AJUSTE de modelos generativos, não o método de pré-treinamento.

### 5.2.5 COMO OS TRÊS SE COMBINAM NOS MODELOS ATUAIS
Os modelos de IA generativa são, em regra, pré-treinados com grandes volumes de dados sem rótulos atribuídos manualmente e, em etapa posterior, podem ser ajustados por aprendizado supervisionado ou por reforço para tarefas específicas. É o que afirma a página do Google for Developers, "Introduction to ML: What is Machine Learning?": "generative models are initially trained using an unsupervised approach" e "the model is sometimes trained further using supervised or reinforcement learning" (reverificado em 7/10/2026). Conclusão para a prova: afirmar que a IA generativa se baseia PRIORITARIAMENTE em aprendizado supervisionado é ERRADO. Mecanismo semelhante aparece no item 81 do TRF6 2024, Cargo 2 (item análogo do Cebraspe; gabarito definitivo E, conferido no gabarito definitivo do TRF6); o tópico 5.2 de TI e Dados usa a página do Google for Developers, "Introduction to ML: What is Machine Learning?", como fundamento, não o TRF6.
Observação de prudência: a literatura também chama o pré-treinamento de LLMs de "auto-supervisionado" (o próprio texto fornece o alvo). O enquadramento desse termo como subtipo do "não supervisionado" é disputado; o candidato deve ficar com a formulação da página do Google for Developers, "Introduction to ML: What is Machine Learning?", e evitar itens que dependam da classificação do "auto-supervisionado".
Variantes que a banca pode citar (conceitos gerais): semi-supervisionado (poucos dados rotulados + muitos sem rótulo) e auto-supervisionado (rótulos derivados dos próprios dados).

### 5.2.6 EXEMPLO APLICADO AO LEGISLATIVO
- Supervisionado (classificação): treinar um modelo para indexar automaticamente proposições por tema, usando como rótulo a indexação já feita pela unidade de documentação da Câmara em anos anteriores.
- Supervisionado (regressão): estimar o número de dias que uma proposição levará até o parecer da comissão, a partir de atributos como tipo, autoria e regime de tramitação.
- Não supervisionado (clustering): receber 40 mil contribuições de uma consulta pública e agrupá-las por semelhança para descobrir os temas emergentes — os grupos não existem antes; o servidor pode nomeá-los depois, com base em seu entendimento dos dados.
- Por reforço (RLHF): revisores do Derep (antigo DETAQ) avaliam, com aprovação ou reprovação, as minutas geradas por um assistente de redação; essas avaliações são acumuladas e usadas em CICLOS DE AJUSTE do modelo pelo fornecedor ou pela equipe técnica — não há aprendizado em tempo real a cada clique.

### 5.2.7 PEGADINHAS PROVÁVEIS
P1. "No aprendizado não supervisionado não há participação humana" → ERRADO.
P2. "Clustering é tarefa de aprendizado supervisionado" → ERRADO.
P3. "Regressão é a tarefa supervisionada que prevê a categoria à qual o dado pertence" → ERRADO.
P4. "No aprendizado por reforço, o agente recebe, para cada ação, o rótulo da ação correta" → ERRADO.
P5. "RLHF é uma técnica de aprendizado não supervisionado" → ERRADO.
P6. "Os modelos de IA generativa são pré-treinados predominantemente por aprendizado supervisionado em pares pergunta-resposta rotulados manualmente" → ERRADO (Google for Developers, "Introduction to ML: What is Machine Learning?": pré-treino sem rótulos; supervisionado e reforço no ajuste).
P7. "Na classificação, o modelo descobre as categorias por conta própria" → ERRADO (isso é clustering).

## ITEM 5.3 — IA GENERATIVA: CONCEITOS, EXEMPLOS E CASOS DE USO

### 5.3.1 DEFINIÇÃO
IA generativa é o ramo da IA cujos modelos CRIAM conteúdo novo — texto, imagem, áudio, vídeo, código — a partir de uma entrada do usuário, tendo aprendido os padrões dos dados de treinamento (Google for Developers, "Introduction to ML: What is Machine Learning?"). O glossário do Google registra que se trata de "an emerging transformative field with no formal definition" e caracteriza os modelos pela capacidade de produzir conteúdo complexo, coerente e original (Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 7/10/2026). Definição operacional para a prova: gera conteúdo novo, em oposição a prever um valor ou uma categoria sobre conteúdo existente.
Distinção de vocabulário: CLASSIFICAR é uma TAREFA; GENERATIVO e DISCRIMINATIVO são TIPOS DE MODELO. Modelos generativos também podem ser usados para classificar: um classificador generativo (exemplo clássico: Naive Bayes, usado em filtros de spam) aprende a distribuição dos dados em cada classe e decide pela classe mais provável. Logo, "classifica" não implica "discriminativo".

### 5.3.2 GENERATIVA × DISCRIMINATIVA
Segundo a página do Google for Developers, "GAN — Background: What is a Generative Model?" (verificado em 7/10/2026):
- Modelo generativo modela a distribuição conjunta p(X, Y) — ou p(X), sem rótulos —, isto é, aprende COMO OS DADOS SE DISTRIBUEM e por isso consegue gerar novas instâncias realistas (fotos novas de animais; a próxima palavra de uma sequência). "Generative models have to model more."
- Modelo discriminativo modela a probabilidade condicional p(Y | X): aprende apenas a FRONTEIRA entre categorias ("discriminative models try to draw boundaries in the data space"), sem se importar com a plausibilidade de uma instância. Exemplo: distinguir cachorro de gato.
Tradução didática: o discriminativo responde "isto é A ou B?" traçando a fronteira; o generativo responde "como seria um novo exemplar de A?" — e, por conhecer a distribuição de cada classe, também pode responder "isto é A ou B?" (classificador generativo). Nenhum dos dois precisa necessariamente retornar uma probabilidade (Google for Developers, "GAN — Background: What is a Generative Model?").

### 5.3.3 CONCEITOS ESTRUTURANTES
- Modelo de fundação (foundation model): "a very large pre-trained model trained on an enormous and diverse training set", que responde bem a pedidos variados e pode servir de base para ajustes posteriores (Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 7/10/2026). Pode ser multimodal.
- Grande modelo de linguagem (LLM): "at a minimum, a language model having a very high number of parameters"; informalmente, modelos de linguagem baseados em Transformer, como Gemini e GPT (Google for Developers, "Machine Learning Glossary: Generative AI"). Relação entre os termos: o glossário do Google for Developers, "Machine Learning Glossary: Generative AI", os define separadamente; LLMs de uso geral costumam ser modelos de fundação de linguagem; nem todo modelo de fundação é LLM (há modelos de fundação de imagem ou multimodais).
- Modalidades (Google for Developers, "Introduction to ML: What is Machine Learning?", reverificado em 7/10/2026): a lista em tópicos dessa página traz texto→texto, texto→imagem, texto→vídeo, texto→código, texto→fala e imagem-e-texto→imagem; a tabela de exemplos dessa página traz texto→texto, texto→imagem, texto→vídeo, texto→código e imagem→texto. "Multimodal" = aceita ou produz mais de um tipo de dado.
- Ciclo de treinamento: pré-treino sem rótulos atribuídos manualmente → ajuste supervisionado ou por reforço (Google for Developers, "Introduction to ML: What is Machine Learning?"); fine-tuning (Google for Developers, "Machine Learning Glossary: Generative AI"); RLHF (Google for Developers, "Machine Learning Glossary: Generative AI"). Ver 5.2.5.
- Token, janela de contexto, temperatura: ver 5.1.4 (glossário do Google for Developers, "Machine Learning Glossary: Generative AI", para temperatura).
- Alucinação: saída plausível, porém factualmente incorreta (Google for Developers, "Machine Learning Glossary: Generative AI"). É propriedade do mecanismo (o modelo gera o provável, não o verificado).
- RAG: recuperação de documentos externos ao treinamento inseridos no prompt (OpenAI, "Prompt engineering"). Fine-tuning e RAG NÃO são sinônimos: um altera o modelo; o outro, a entrada.
- Agentes (conceito geral; a OpenAI documenta "agentic tasks" em "Prompt engineering"): modelos que planejam, usam ferramentas e executam tarefas em várias etapas.
- Conhecimento paramétrico e data de corte (conceito geral): sem ferramentas ou RAG, o modelo responde com o que incorporou no treinamento; o modelo em si não consulta a internet ou bancos de dados.
- Deepfake, marca d'água e proveniência (conceitos gerais).

### 5.3.4 EXEMPLOS E CASOS DE USO NO SERVIÇO PÚBLICO E NO LEGISLATIVO
Sumarização de discursos, audiências e documentos extensos; apoio à degravação e à revisão de notas taquigráficas (correção, padronização, pontuação), sempre com revisão humana e sem material sigiloso em ferramenta não homologada (ver item 6); redação de minutas a partir de modelo institucional; atendimento ao cidadão por assistentes conversacionais; busca semântica e classificação em acervos; extração de dados de PDFs; tradução e acessibilidade (descrição de imagens, legendas, linguagem simples); geração e revisão de código.
Riscos associados: alucinação (citar lei inexistente), viés, vazamento de dados pessoais ou sigilosos, dependência sem verificação, direitos autorais e falta de transparência sobre o uso de IA.

### 5.3.5 EXEMPLO APLICADO
Um gabinete pede a um assistente generativo "a jurisprudência do STF sobre CPI e quebra de sigilo". O modelo devolve três ementas com números de processo. Duas são reais; uma é inventada, com numeração verossímil. Diagnóstico: alucinação, inerente ao mecanismo generativo. Procedimento correto: usar RAG com base oficial ou ferramenta de busca verificável, pedir citação da fonte e CONFERIR cada ementa no sítio do tribunal antes de usar. Temperatura baixa não resolveria: tornaria a invenção apenas mais repetível.

### 5.3.6 PEGADINHAS PROVÁVEIS
P1. "Modelo generativo e modelo discriminativo são o mesmo tipo de modelo, distinguindo-se apenas pela tarefa executada" → ERRADO (são tipos distintos: um modela a distribuição, o outro, a fronteira; a tarefa de classificar pode ser feita por ambos).
P2. "A IA generativa baseia-se prioritariamente em aprendizado supervisionado" → ERRADO (Google for Developers, "Introduction to ML: What is Machine Learning?"; mecanismo semelhante no TRF6 2024, item 81, gabarito definitivo E).
P3. "Por padrão, um LLM consulta a internet e bases de dados atualizadas antes de responder" → ERRADO.
P4. "Fine-tuning e RAG são denominações equivalentes da mesma técnica" → ERRADO.
P5. "Com temperatura zero, o modelo deixa de produzir informações falsas" → ERRADO.
P6. "Modelos de fundação restringem-se à geração de texto" → ERRADO (podem ser multimodais).
P7. "Alucinação é o erro de digitação ou de formatação da resposta" → ERRADO.
P8. "Todo modelo de fundação é um LLM" → ERRADO (há modelos de fundação de imagem e multimodais; o glossário do Google for Developers, "Machine Learning Glossary: Generative AI" define os termos separadamente).

## ITEM 6 — ÉTICA E RESPONSABILIDADE DIGITAL NO SERVIÇO PÚBLICO

### 6.1 DEFINIÇÃO E ENQUADRAMENTO
Ética digital é a aplicação dos deveres éticos do servidor ao ambiente digital: uso de sistemas, dados, redes, ferramentas de IA e comunicação eletrônica. Responsabilidade digital é a contrapartida: o servidor permanece RESPONSÁVEL pelos atos que pratica com meios digitais, inclusive quando usa IA. A ferramenta não responde; o agente público responde.
Base constitucional: princípios da administração pública — legalidade, impessoalidade, moralidade, publicidade e eficiência (Constituição Federal, art. 37, caput).
Base deontológica: o Código de Ética do Servidor Público Civil Federal (Decreto 1.171/1994, Anexo, Capítulo I) dispõe, na Seção I (regras deontológicas), inciso II, que o servidor "não poderá jamais desprezar o elemento ético de sua conduta", decidindo não apenas entre o legal e o ilegal, mas "principalmente entre o honesto e o desonesto" (conferido no Planalto em 08/10/2026). A ética vai ALÉM da legalidade.
Observação de aplicabilidade: o Decreto 1.171/1994 é norma do Poder Executivo federal; na Câmara, o regime do servidor é a Lei 8.112/1990 e os atos internos da Casa. O candidato deve conhecer o Decreto como referência de ética no serviço público, sem afirmar que ele vincula diretamente o Legislativo.

6.2 PRINCÍPIOS ÉTICOS PARA USO DE IA E TECNOLOGIA — síntese autoral
1. Supervisão humana: decisões relevantes passam por pessoa responsável; a IA apoia, não decide sozinha.
2. Transparência e explicabilidade: informar quando há uso de IA; poder explicar critérios de uma decisão.
3. Não discriminação e equidade: vigilância contra viés algorítmico.
4. Privacidade e proteção de dados: minimização, finalidade, segurança (LGPD, abaixo).
5. Responsabilização (accountability): há sempre um responsável humano identificável.
6. Segurança: credenciais, phishing, engenharia social, deepfakes, ferramentas não homologadas.
7. Integridade e veracidade: verificar saídas de IA antes de usar.
8. Uso adequado de recursos públicos: equipamentos, redes e licenças institucionais servem ao interesse público.
9. Acessibilidade e inclusão digital (Lei 13.146/2015, art. 63).
10. Combate à desinformação, inclusive conteúdo sintético.

6.3 MAPA NORMATIVO (artigo e inciso)
LGPD (Lei 13.709/2018):
- Aplica-se a pessoa natural ou jurídica, de direito público ou privado (art. 1º, caput). O Capítulo IV ("Do Tratamento de Dados Pessoais pelo Poder Público") abrange os arts. 23 a 32 — Seção I (regras), arts. 23–30; Seção II (responsabilidade), arts. 31–32 (conferido em 07/10/2026).
- Fundamentos (art. 2º): I respeito à privacidade; II autodeterminação informativa; III liberdade de expressão, de informação, de comunicação e de opinião; IV inviolabilidade da intimidade, da honra e da imagem; V desenvolvimento econômico e tecnológico e inovação; VI livre iniciativa, livre concorrência e defesa do consumidor; VII direitos humanos, livre desenvolvimento da personalidade, dignidade e exercício da cidadania pelas pessoas naturais.
- Definições (art. 5º): I dado pessoal; II dado pessoal sensível (origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico); III dado anonimizado (definição); VI controlador; VII operador; VIII encarregado — pela Lei 15.352, de 25/02/2026 (conversão da MP 1.317/2025; em vigor na publicação, DOU de 25/02/2026), o inciso passou a ter a redação: "encarregado: pessoa indicada pelo controlador e operador para atuar como canal de comunicação entre o controlador, os titulares dos dados e a Agência Nacional de Proteção de Dados (ANPD)" (fonte: Planalto, Lei 15.352/2026 e LGPD compilada, verificadas em 08/10/2026; vale para a prova, edital 13.33); X tratamento; XI anonimização; XII consentimento; XVII relatório de impacto; XIX autoridade nacional: "entidade da administração pública responsável por zelar, implementar e fiscalizar o cumprimento desta Lei em todo o território nacional" (redação dada pela Lei 15.352/2026; conferido no Planalto em 08/10/2026; a redação anterior não foi conferida, e nada se afirma sobre o que mudou).
- Dados anonimizados (art. 12, caput): não são considerados dados pessoais para os fins da lei, SALVO quando o processo de anonimização for revertido com meios próprios ou puder ser revertido com esforços razoáveis. O art. 5º, III, apenas define o termo; o efeito jurídico está no art. 12 (conferido em 07/10/2026).
- Princípios (art. 6º): I finalidade; II adequação; III necessidade; IV livre acesso; V qualidade dos dados; VI transparência; VII segurança; VIII prevenção; IX não discriminação; X responsabilização e prestação de contas.
- Bases legais (art. 7º): I consentimento; II cumprimento de obrigação legal ou regulatória pelo controlador; III pela administração pública, para o tratamento e uso compartilhado de dados necessários à execução de políticas públicas previstas em leis e regulamentos ou respaldadas em contratos, convênios ou instrumentos congêneres; (...) IX legítimo interesse (incisos I, II e III conferidos no Planalto em 08/10/2026). Chave de prova: CONSENTIMENTO NÃO É A ÚNICA BASE, nem a principal para o Poder Público.
- Decisões automatizadas (art. 20, caput): direito do titular a solicitar a REVISÃO de decisões tomadas unicamente com base em tratamento automatizado que afetem seus interesses; § 1º: informações claras sobre os critérios. Histórico da expressão "por pessoa natural": o texto original de 2018 previa revisão "por pessoa natural"; a MP 869/2018 retirou a expressão; o § 3º incluído pela Lei 13.853/2019 foi vetado (conferido no Planalto em 07/10/2026). Logo, o texto vigente não exige revisão por pessoa natural; item que afirme "revisão obrigatoriamente por pessoa natural" é ERRADO.
- Tratamento pelo Poder Público (art. 23, caput): atendimento de finalidade pública, na persecução do interesse público, para executar competências legais ou cumprir atribuições legais do serviço público; inciso I: dever de informar as hipóteses de tratamento, com informações claras e atualizadas.
- Segurança e incidentes: art. 46 (medidas técnicas e administrativas de segurança); art. 48 (comunicação de incidente de segurança à ANPD e ao titular).
LAI (Lei 12.527/2011):
- Diretrizes (art. 3º): I publicidade como preceito geral e sigilo como exceção (conferido em 08/10/2026); II divulgação independentemente de solicitação (transparência ativa); III uso de meios de comunicação viabilizados pela tecnologia da informação; IV fomento à cultura de transparência; V controle social.
- Informações pessoais (art. 31, caput): tratamento transparente e com respeito à intimidade, vida privada, honra e imagem; § 1º, I: acesso restrito, pelo prazo máximo de 100 anos, a agentes públicos legalmente autorizados e à pessoa a que se referirem (caput e § 1º, I, conferidos em 08/10/2026).
- Classificação de sigilo: art. 23, caput (informações imprescindíveis à segurança da sociedade ou do Estado, passíveis de classificação); art. 24, § 1º: I ultrassecreta 25 anos; II secreta 15 anos; III reservada 5 anos (conferidos em 08/10/2026).
Governo Digital (Lei 14.129/2021): aplica-se aos órgãos da administração pública direta federal, abrangendo os Poderes Executivo, Judiciário e Legislativo (art. 2º, I); entre os princípios e diretrizes do art. 3º estão a desburocratização (I), a transparência na execução dos serviços públicos (IV), o uso da tecnologia para otimizar processos de trabalho da administração pública (VIII), a proteção de dados pessoais nos termos da LGPD (XVII) e a acessibilidade da pessoa com deficiência ou com mobilidade reduzida (XIX).
Código de Ética (Decreto 1.171/1994, Anexo, Cap. I):
- Seção I, regras deontológicas: inciso II (elemento ético; honesto × desonesto); inciso VII (salvo os casos de segurança nacional, investigações policiais ou interesse superior do Estado e da Administração Pública, a serem preservados em processo previamente declarado sigiloso, nos termos da lei, a publicidade de qualquer ato administrativo constitui requisito de eficácia e moralidade); inciso VIII (direito à verdade: o servidor não pode omiti-la ou falseá-la).
- Seção II, deveres: inciso XIV, alíneas "m" (comunicar imediatamente a seus superiores todo e qualquer ato ou fato contrário ao interesse público), "g" (ser cortês, ter urbanidade, disponibilidade e atenção) e "q" (manter-se atualizado com as instruções, as normas de serviço e a legislação pertinentes ao órgão).
- Seção III, vedações: inciso XV, alínea "e": "deixar de utilizar os avanços técnicos e científicos ao seu alcance ou do seu conhecimento para atendimento do seu mister" — a OMISSÃO tecnológica também é vedada; alínea "a": uso do cargo para obter favorecimento; alínea "l": "retirar da repartição pública, sem estar legalmente autorizado, qualquer documento, livro ou bem pertencente ao patrimônio público" (o inciso XV não tem alínea "k").
Lei 8.112/1990: deveres (art. 116): II lealdade às instituições; III observância das normas legais e regulamentares; VIII guardar sigilo sobre assunto da repartição. Proibições (art. 117): IX valer-se do cargo para lograr proveito pessoal ou de outrem, em detrimento da dignidade da função pública; XVI utilizar pessoal ou recursos materiais da repartição em serviços ou atividades particulares. Responsabilidade (art. 121): o servidor responde civil, penal e administrativamente pelo exercício irregular de suas atribuições.
Marco Civil da Internet (Lei 12.965/2014): princípios (art. 3º): I liberdade de expressão; II proteção da privacidade; III proteção dos dados pessoais; direitos do usuário (art. 7º).
Direitos autorais (Lei 9.610/1998): art. 8º, IV — textos de tratados, leis, decretos, regulamentos, decisões judiciais e demais atos oficiais NÃO são objeto de proteção autoral; art. 8º, I — ideias, procedimentos normativos, sistemas e métodos também não.
Norma interna da Câmara: Ato da Mesa nº 225, de 15/12/2025 (DCD, Ed. Extra A, 18/12/2025): estabelece diretrizes gerais para a política de governança de inteligência artificial no âmbito da Câmara dos Deputados e determina sua implementação pela Diretoria-Geral. Em síntese, o art. 3º orienta a política para: princípios éticos, entre eles transparência, proteção de dados, não discriminação e supervisão humana (I); conformidade com a LGPD (III); disciplina do uso de IA generativa, com requisitos para prompts, para agentes autônomos ou semiautônomos e para revisão humana (V); informação ao usuário quando interage com agentes de IA (VIII); supervisão que inclui o monitoramento de vieses e alucinações (IX). O art. 4º, IV, prevê comitê de ética de uso da IA. Norma interna; referência de contexto. (Síntese a partir do texto consultado em 08/10/2026; não é transcrição literal.)

Contexto sujeito a mudança: legislação sem vigência só pode ser cobrada se estiver explicitada nos objetos de avaliação (edital, 13.34: "A legislação que não esteja em vigor poderá ser cobrada, desde que devidamente explicitada nos objetos de avaliação"); como o item 14 do edital não explicita o PL 2338/2023 (marco legal da IA; situação de tramitação não verificada), ele fica só como contexto, sujeito a mudança. Estratégia Brasileira de Inteligência Artificial, instituída pela Portaria MCTI nº 4.617, de 6/4/2021 (Anexo com redação dada pela Portaria MCTI nº 4.979/2021); vigência atual não conferida.

### 6.4 EXEMPLO APLICADO AO LEGISLATIVO
Situação: servidora do Derep (antigo DETAQ) recebe o áudio e a transcrição bruta de reunião reservada de comissão e pensa em colar o texto integral em um assistente de IA gratuito, acessado pela conta pessoal, para "limpar" a redação em dois minutos.
Análise:
1. Sigilo funcional: a reunião é reservada; expor o conteúdo a terceiro (o provedor da ferramenta) viola o dever de guardar sigilo sobre assunto da repartição (Lei 8.112/1990, art. 116, VIII) e a lógica da LAI, em que o sigilo legalmente previsto é exceção protegida (Lei 12.527/2011, art. 3º, I).
2. Dados pessoais: as falas contêm nomes, opiniões políticas (dado sensível, Lei 13.709/2018, art. 5º, II) e eventualmente dados de terceiros; o envio a serviço externo, por conta pessoal, tende a não encontrar base legal (art. 7º) e não atende às medidas de segurança do art. 46.
3. Responsabilidade: se o texto "limpo" contiver falas inventadas pela IA (alucinação) e for publicado, a responsabilidade é da servidora, não da ferramenta (supervisão humana; dever de verdade, Decreto 1.171/1994, Seção I, VIII).
4. Recursos e ferramentas: usar ferramenta institucional homologada, se existir; se não existir, não é aceitável "resolver" com conta pessoal.
5. O que NÃO é a resposta: proibir toda IA. A vedação do Decreto 1.171/1994 (XV, "e") desaconselha a omissão tecnológica; a conduta correta é usar IA dentro de canais autorizados, com dados minimizados e revisão humana.

### 6.5 PEGADINHAS PROVÁVEIS
P1. "Dado anonimizado é espécie de dado pessoal sensível" → ERRADO (art. 12, caput: anonimizado não é dado pessoal, salvo reversão; art. 5º, III, define; sensível é o do art. 5º, II).
P2. "A LGPD não se aplica aos órgãos do Poder Legislativo" → ERRADO (art. 1º, caput; Capítulo IV, arts. 23 a 32).
P3. "O titular tem direito à revisão de decisões automatizadas obrigatoriamente por pessoa natural" → ERRADO (a expressão "por pessoa natural" foi retirada pela MP 869/2018 e o § 3º da Lei 13.853/2019 foi vetado; conferido em 07/10/2026).
P4. "Na LAI, o sigilo é a regra e a publicidade, a exceção" → ERRADO (art. 3º, I).
P5. "O consentimento do titular é a única base legal que autoriza a administração pública a tratar dados pessoais" → ERRADO (art. 7º, II e III).
P6. "O Código de Ética veda ao servidor o uso de avanços técnicos e científicos" → ERRADO (veda DEIXAR DE utilizá-los — XV, "e").
P7. "Quando a decisão é sugerida por sistema de IA, a responsabilidade pelo ato transfere-se ao sistema" → ERRADO.
P8. "Opinião política e filiação sindical não são dados sensíveis" → ERRADO (art. 5º, II).
P9. "Textos de leis e de atos oficiais são protegidos por direito autoral" → ERRADO (Lei 9.610/1998, art. 8º, IV).
P10. "Ética digital no serviço público limita-se às regras de uso de redes sociais" → ERRADO.
```

## Pares

- C1. **Supervisionado** × **não supervisionado × por reforço** | rótulos | sem rótulos, busca de estrutura | sem rótulos, recompensa por ação e política | Troca: chamar clustering de supervisionado; dizer que reforço usa rótulos; dizer que não supervisionado dispensa humano.
- C2. **Modelo generativo** × **modelo discriminativo** | modela p(X,Y) ou p(X), a distribuição; gera conteúdo novo; pode também classificar (classificador generativo, ex.: Naive Bayes) | modela p(Y|X), traça fronteiras; usado para classificar | Troca: "toda tarefa de classificação usa modelo discriminativo" (generalização indevida); "a generativa baseia-se prioritariamente em supervisionado".
- C3. **Zero-shot** × **one-shot × few-shot** | nenhum exemplo | um exemplo | vários exemplos | Troca: definir few-shot como um exemplo.
- C4. **Chain-of-thought** × **prompt chaining** | um prompt pedindo raciocínio passo a passo | vários prompts encadeados | Troca: descrever um com o nome do outro.
- C5. **Engenharia de prompts** × **fine-tuning × RAG** | atua na entrada | altera parâmetros | recupera documentos e os insere na entrada | Troca: "prompt ajusta pesos"; "RAG retreina o modelo"; "fine-tuning e RAG são sinônimos".
- C6. **Temperatura alta** × **baixa** | mais aleatória | mais previsível | Troca: inverter; ou "temperatura baixa garante veracidade".
- C7. **Regressão** × **classificação** | valor numérico | categoria | Troca: inverter as saídas.
- C8. **Clustering** × **classificação** | grupos encontrados pelo modelo; o humano pode nomeá-los com base em seu entendimento dos dados (Google for Developers, "Introduction to ML: What is Machine Learning?"); sem rótulos | categorias definidas antes; com rótulos | Troca: "na classificação o modelo descobre as categorias".
- C9. **Alucinação** × **viés** | conteúdo plausível e falso | tratamento sistematicamente desigual herdado dos dados | Troca: chamar viés de alucinação; reduzir alucinação a erro de formatação.
- C10. **Modelo de fundação** × **LLM** | modelo enorme pré-treinado em dados diversos, inclusive imagem ou multimodal | modelo de linguagem com muitíssimos parâmetros; os de uso geral costumam ser modelos de fundação de linguagem | Troca: "todo modelo de fundação é LLM"; "modelo de fundação só gera texto".
- C11. **Conhecimento paramétrico** × **consulta em tempo real** | o que o modelo incorporou até a data de corte | só com RAG, busca ou ferramentas | Troca: "por padrão o LLM consulta a internet".
- C12. **Dado pessoal** × **dado sensível × dado anonimizado (LGPD 5º, I, II, III; 12, caput)** | identifica pessoa natural | categorias do 5º, II | não é dado pessoal, salvo reversão (12, caput) | Troca: anonimizado como sensível; opinião política como "não sensível".
- C13. **Controlador** × **operador × encarregado (LGPD 5º, VI, VII, VIII)** | decide sobre o tratamento | trata em nome do controlador | pessoa indicada pelo controlador e operador como canal de comunicação entre o controlador, os titulares e a Agência Nacional de Proteção de Dados (ANPD) — redação do 5º, VIII, dada pela Lei 15.352/2026, verificada em 08/10/2026 | Troca: atribuir ao operador a decisão; ao encarregado, a execução.
- C14. **Consentimento** × **demais bases legais (LGPD 7º)** | uma das bases (I) | obrigação legal (II), políticas públicas (III), legítimo interesse (IX) etc. | Troca: "consentimento é a única base para o Poder Público".
- C15. **Publicidade** × **sigilo (LAI 3º, I)** | regra | exceção | Troca: inverter.
- C16. **Legal** × **ético (Decreto 1.171, Seção I, II)** | conforme a lei | conforme a honestidade e o interesse público, além da lei | Troca: "se é legal, é ético".
- C17. **Supervisão humana** × **automação total** | IA apoia; humano decide e responde | sistema decide sem revisão | Troca: "a responsabilidade transfere-se ao sistema"; "revisão obrigatoriamente por pessoa natural" (LGPD art. 20 não exige: expressão retirada pela MP 869/2018; § 3º da Lei 13.853/2019 vetado).
- C18. **Usar IA** × **omitir tecnologia (Decreto 1.171, XV, "e")** | permitido e esperado, em canais autorizados | vedado deixar de usar avanços técnicos | Troca: "o Código de Ética veda o uso de avanços técnicos".
- C19. **Injeção de prompt** × **jailbreak (conceitos gerais)** | instrução maliciosa embutida em conteúdo lido | tentativa direta do usuário de burlar restrições | Troca: usar um termo pelo outro.
- C20. **Texto oficial** × **obra protegida (Lei 9.610, 8º, IV × 7º)** | atos oficiais sem proteção autoral | criações intelectuais protegidas | Troca: "atos oficiais são protegidos por direito autoral".

## Pegadinhas

- [P1-5.1] **Engenharia de prompts** — "A engenharia de prompts ajusta os pesos do modelo para a tarefa" → ERRADO (isso é fine-tuning).
- [P1-5.1] **Engenharia de prompts** — "Few-shot é o prompt que traz um único exemplo" → ERRADO (um exemplo é one-shot).
- [P1-5.1] **Engenharia de prompts** — "Chain-of-thought consiste em dividir a tarefa em prompts sucessivos" → ERRADO (isso é prompt chaining).
- [P1-5.1] **Engenharia de prompts** — "Temperatura mais baixa produz saídas mais variadas e criativas" → ERRADO (é o inverso).
- [P1-5.1] **Engenharia de prompts** — "Um prompt bem elaborado elimina a possibilidade de alucinação" → ERRADO (reduz, não elimina).
- [P1-5.1] **Engenharia de prompts** — "RAG consiste em retreinar o modelo com os documentos da organização" → ERRADO (RAG recupera documentos e os insere no prompt).
- [P1-5.1] **Engenharia de prompts** — "Zero-shot é a técnica em que o modelo recebe exemplos sem rótulo" → ERRADO (zero-shot = nenhum exemplo).
- [P1-5.1] **Engenharia de prompts** — Não confunda zero-shot com one-shot e few-shot: o zero-shot traz só a instrução, sem nenhum exemplo; o one-shot traz um único exemplo; o few-shot traz mais de um. Armadilha: definir few-shot como um único exemplo, o que é one-shot.
- [P1-5.1] **Engenharia de prompts** — Não confunda chain-of-thought com prompt chaining: o chain-of-thought é um único prompt que pede ao modelo que explique o raciocínio passo a passo; o prompt chaining divide a tarefa em vários prompts sequenciais, em que a saída de um alimenta o seguinte.
- [P1-5.1] **Engenharia de prompts** — Não confunda engenharia de prompts com fine-tuning e RAG: a engenharia de prompts atua na entrada, sem alterar os parâmetros do modelo; o fine-tuning altera os parâmetros; o RAG recupera documentos e os insere no prompt, sem retreinar o modelo.
- [P1-5.2] **Aprendizado supervisionado, não supervisionado e por reforço** — "No aprendizado não supervisionado não há participação humana" → ERRADO.
- [P1-5.2] **Aprendizado supervisionado, não supervisionado e por reforço** — "Clustering é tarefa de aprendizado supervisionado" → ERRADO.
- [P1-5.2] **Aprendizado supervisionado, não supervisionado e por reforço** — "Regressão é a tarefa supervisionada que prevê a categoria à qual o dado pertence" → ERRADO.
- [P1-5.2] **Aprendizado supervisionado, não supervisionado e por reforço** — "No aprendizado por reforço, o agente recebe, para cada ação, o rótulo da ação correta" → ERRADO.
- [P1-5.2] **Aprendizado supervisionado, não supervisionado e por reforço** — "RLHF é uma técnica de aprendizado não supervisionado" → ERRADO.
- [P1-5.2] **Aprendizado supervisionado, não supervisionado e por reforço** — "Os modelos de IA generativa são pré-treinados predominantemente por aprendizado supervisionado em pares pergunta-resposta rotulados manualmente" → ERRADO (Google for Developers, "Introduction to ML: What is Machine Learning?": pré-treino sem rótulos; supervisionado e reforço no ajuste).
- [P1-5.2] **Aprendizado supervisionado, não supervisionado e por reforço** — "Na classificação, o modelo descobre as categorias por conta própria" → ERRADO (isso é clustering).
- [P1-5.2] **Aprendizado supervisionado, não supervisionado e por reforço** — Não confunda aprendizado supervisionado com não supervisionado: o supervisionado aprende com dados rotulados, que já trazem a resposta correta; o não supervisionado recebe dados sem rótulos e busca padrões ou estruturas. Armadilha: não supervisionado significa sem rótulos, não sem participação humana.
- [P1-5.2] **Aprendizado supervisionado, não supervisionado e por reforço** — Não confunda aprendizado não supervisionado com aprendizado por reforço: o não supervisionado busca estrutura em dados sem rótulos; no reforço, o agente age em um ambiente, recebe recompensas ou penalidades e constrói uma política. Armadilha: no reforço não há rótulo com a resposta certa para cada entrada.
- [P1-5.2] **Aprendizado supervisionado, não supervisionado e por reforço** — Não confunda regressão com classificação: a regressão prevê um valor numérico contínuo, como o preço futuro de uma casa; a classificação prevê uma categoria, como um e-mail ser spam ou não. Armadilha: atribuir à regressão a previsão de categorias; ambas são supervisionadas.
- [P1-5.2] **Aprendizado supervisionado, não supervisionado e por reforço** — Não confunda clustering com classificação: na classificação, as categorias são definidas previamente pelo humano e o modelo atribui cada dado a uma delas; no clustering, o modelo encontra os grupos em dados sem rótulos, e o humano pode nomeá-los depois.
- [P1-5.3] **IA generativa: conceitos, exemplos e casos de uso** — "Modelo generativo e modelo discriminativo são o mesmo tipo de modelo, distinguindo-se apenas pela tarefa executada" → ERRADO (são tipos distintos: um modela a distribuição, o outro, a fronteira; a tarefa de classificar pode ser feita por ambos).
- [P1-5.3] **IA generativa: conceitos, exemplos e casos de uso** — "A IA generativa baseia-se prioritariamente em aprendizado supervisionado" → ERRADO (Google for Developers, "Introduction to ML: What is Machine Learning?"; mecanismo semelhante no TRF6 2024, item 81, gabarito definitivo E).
- [P1-5.3] **IA generativa: conceitos, exemplos e casos de uso** — "Por padrão, um LLM consulta a internet e bases de dados atualizadas antes de responder" → ERRADO.
- [P1-5.3] **IA generativa: conceitos, exemplos e casos de uso** — "Fine-tuning e RAG são denominações equivalentes da mesma técnica" → ERRADO.
- [P1-5.3] **IA generativa: conceitos, exemplos e casos de uso** — "Com temperatura zero, o modelo deixa de produzir informações falsas" → ERRADO.
- [P1-5.3] **IA generativa: conceitos, exemplos e casos de uso** — "Modelos de fundação restringem-se à geração de texto" → ERRADO (podem ser multimodais).
- [P1-5.3] **IA generativa: conceitos, exemplos e casos de uso** — "Alucinação é o erro de digitação ou de formatação da resposta" → ERRADO.
- [P1-5.3] **IA generativa: conceitos, exemplos e casos de uso** — "Todo modelo de fundação é um LLM" → ERRADO (há modelos de fundação de imagem e multimodais; o glossário do Google for Developers, "Machine Learning Glossary: Generative AI" define os termos separadamente).
- [P1-5.3] **IA generativa: conceitos, exemplos e casos de uso** — Não confunda modelo de fundação com LLM: o modelo de fundação é um modelo muito grande, pré-treinado em um conjunto enorme e diverso, que pode ser multimodal; o LLM é, no mínimo, um modelo de linguagem com número muito alto de parâmetros. Armadilha: nem todo modelo de fundação é LLM.
- [P1-5.3] **IA generativa: conceitos, exemplos e casos de uso** — Não confunda conhecimento paramétrico com consulta em tempo real: o conhecimento paramétrico é o que o modelo incorporou no treinamento, até a data de corte; sem ferramentas ou RAG, o modelo em si não consulta a internet nem bancos de dados.
- [P1-6] **Ética e responsabilidade digital no serviço público** — "Dado anonimizado é espécie de dado pessoal sensível" → ERRADO (art. 12, caput: anonimizado não é dado pessoal, salvo reversão; art. 5º, III, define; sensível é o do art. 5º, II).
- [P1-6] **Ética e responsabilidade digital no serviço público** — "A LGPD não se aplica aos órgãos do Poder Legislativo" → ERRADO (art. 1º, caput; Capítulo IV, arts. 23 a 32).
- [P1-6] **Ética e responsabilidade digital no serviço público** — "O titular tem direito à revisão de decisões automatizadas obrigatoriamente por pessoa natural" → ERRADO (a expressão "por pessoa natural" foi retirada pela MP 869/2018 e o § 3º da Lei 13.853/2019 foi vetado; conferido em 07/10/2026).
- [P1-6] **Ética e responsabilidade digital no serviço público** — "Na LAI, o sigilo é a regra e a publicidade, a exceção" → ERRADO (art. 3º, I).
- [P1-6] **Ética e responsabilidade digital no serviço público** — "O consentimento do titular é a única base legal que autoriza a administração pública a tratar dados pessoais" → ERRADO (art. 7º, II e III).
- [P1-6] **Ética e responsabilidade digital no serviço público** — "O Código de Ética veda ao servidor o uso de avanços técnicos e científicos" → ERRADO (veda DEIXAR DE utilizá-los — XV, "e").
- [P1-6] **Ética e responsabilidade digital no serviço público** — "Quando a decisão é sugerida por sistema de IA, a responsabilidade pelo ato transfere-se ao sistema" → ERRADO.
- [P1-6] **Ética e responsabilidade digital no serviço público** — "Opinião política e filiação sindical não são dados sensíveis" → ERRADO (art. 5º, II).
- [P1-6] **Ética e responsabilidade digital no serviço público** — "Textos de leis e de atos oficiais são protegidos por direito autoral" → ERRADO (Lei 9.610/1998, art. 8º, IV).
- [P1-6] **Ética e responsabilidade digital no serviço público** — "Ética digital no serviço público limita-se às regras de uso de redes sociais" → ERRADO.
- [P1-6] **Ética e responsabilidade digital no serviço público** — Não confunda o que é legal com o que é ético: o juízo legal separa o legal do ilegal; o ético, pelo Decreto 1.171/1994 (Código de Ética do servidor do Executivo federal, Seção I, II, verificado em 08/10/2026), separa principalmente o honesto do desonesto. Armadilha: a ética vai além da legalidade.
- [P1-6] **Ética e responsabilidade digital no serviço público** — Não confunda supervisão humana com automação total: com supervisão humana, a IA apoia e a pessoa responsável decide e responde pelo ato; a IA não decide sozinha. Armadilha: a responsabilidade não se transfere ao sistema, pois a ferramenta não responde e o agente público responde.

## Tópico P1-5.1 — Engenharia de prompts

### Resumo do tópico

Prompt é a entrada em linguagem natural fornecida a um modelo de linguagem, e a engenharia de prompts projeta, testa e itera prompts sem alterar os parâmetros internos do modelo. Ela atua na entrada; o fine-tuning, que o glossário do Google for Developers (verificado em 7/10/2026) define como segunda passagem de treinamento, atua nos parâmetros.

Um prompt estruturado reúne papel, instrução, contexto, exemplos, formato de saída, restrições e delimitadores, que separam as instruções dos dados de referência.

Zero-shot não traz exemplo, one-shot traz um e few-shot traz mais de um. No chain-of-thought, um prompt pede raciocínio passo a passo; no prompt chaining, vários prompts se encadeiam e a saída de um alimenta o seguinte. O RAG recupera documentos e os insere no prompt, sem retreinar o modelo.

A temperatura controla a aleatoriedade da saída: baixa dá respostas mais previsíveis, não mais verdadeiras. Um prompt bem construído reduz as alucinações, mas não as elimina. Na injeção de prompt, instruções maliciosas vêm embutidas em textos que o modelo lê; o conteúdo externo deve ser tratado como dado, não como instrução.

## Tópico P1-5.2 — Aprendizado supervisionado, não supervisionado e por reforço

### Resumo do tópico

Aprendizado de máquina é o campo em que sistemas aprendem padrões a partir de dados, em vez de seguir regras explicitamente programadas. Segundo a página do Google for Developers, verificada em 7/10/2026, os sistemas se classificam por como aprendem: supervisionado, não supervisionado, por reforço e IA generativa.

No supervisionado, o modelo aprende com dados rotulados; a regressão prevê um valor numérico e a classificação prevê uma categoria, ambas com rótulos no treino.

No não supervisionado, os dados não têm rótulos e o modelo busca padrões, como no clustering. Na classificação, as categorias são definidas previamente; no clustering, o modelo encontra os grupos e o humano pode nomeá-los. Não supervisionado significa sem rótulos, e não sem participação humana.

No reforço, um agente aprende por tentativa e erro num ambiente: age, recebe recompensas ou penalidades e constrói uma política, a melhor estratégia para acumular recompensas. Não há rótulo da resposta certa para cada entrada, e a recompensa muitas vezes é atrasada. O RLHF, com feedback humano, é uma etapa de ajuste, não o pré-treinamento.

Os modelos de IA generativa são pré-treinados sem rótulos atribuídos manualmente e depois podem ser ajustados por aprendizado supervisionado ou por reforço; dizer que se baseiam prioritariamente no supervisionado é erro.

## Tópico P1-5.3 — IA generativa: conceitos, exemplos e casos de uso

### Resumo do tópico

IA generativa é o ramo da IA cujos modelos criam conteúdo novo, como texto, imagem, áudio, vídeo e código, a partir de uma entrada do usuário. Não consiste em prever valor ou categoria de conteúdo existente.

Classificar é uma tarefa; generativo e discriminativo são tipos de modelo. Segundo a página do Google for Developers, verificada em 7/10/2026, o generativo modela a distribuição dos dados e por isso gera novas instâncias; o discriminativo aprende apenas a fronteira entre categorias. A tarefa de classificar pode ser feita pelos dois.

Modelo de fundação é um modelo muito grande, pré-treinado em conjunto enorme e diverso, serve de base para ajustes e pode ser multimodal. LLM é um modelo de linguagem com número muito alto de parâmetros, e nem todo modelo de fundação é LLM.

A alucinação é a saída plausível, porém factualmente incorreta, e é propriedade do mecanismo: o modelo gera o provável, não o verificado. Temperatura baixa não a resolve, apenas torna a invenção mais repetível. O RAG insere documentos externos no prompt, e o fine-tuning altera o modelo; não são sinônimos.

Sem ferramentas ou RAG, o modelo responde com o que incorporou no treinamento e não consulta a internet.

Os usos incluem sumarização e apoio à revisão, sempre com revisão humana; os riscos, alucinação, viés e vazamento de dados sigilosos.

## Tópico P1-6 — Ética e responsabilidade digital no serviço público

### Resumo do tópico

Ética digital aplica os deveres éticos do servidor ao ambiente digital; com meios digitais, inclusive com IA, a ferramenta não responde: o agente público responde.

Os princípios do art. 37, caput, da Constituição são a base. O Decreto 1.171/1994 (Anexo, Seção I, inciso II), norma do Executivo federal, mostra que a ética vai além da legalidade; na Câmara, o regime do servidor é a Lei 8.112/1990.

A LGPD vale para pessoas de direito público ou privado, inclusive o Legislativo (art. 1º, caput). Opinião política e filiação sindical são dados sensíveis (art. 5º, II), e o dado anonimizado não é pessoal, salvo se revertido (art. 12).

O consentimento não é a única base legal, nem a principal para o Poder Público (art. 7º). O titular pode pedir revisão de decisão automatizada (art. 20), não necessariamente por pessoa natural. Incidente de segurança é comunicado à Agência Nacional de Proteção de Dados (ANPD) e ao titular (art. 48).

Na LAI, a publicidade é a regra e o sigilo, a exceção (art. 3º, I). A Lei 8.112/1990 impõe sigilo sobre assunto da repartição (art. 116, VIII) e responsabiliza o servidor civil, penal e administrativamente (art. 121).

O mesmo decreto veda deixar de usar os avanços técnicos (inciso XV, alínea e); a conduta correta é usar IA em canais autorizados, com revisão humana.
