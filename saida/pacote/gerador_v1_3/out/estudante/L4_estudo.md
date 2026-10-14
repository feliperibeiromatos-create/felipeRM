# Lote 4 — TID-IA (P1 5.1–5.3 e 6)

Prova: P1

## Itens do edital

- P1-5.1 — Engenharia de prompts
- P1-5.2 — Aprendizado supervisionado, não supervisionado e por reforço
- P1-5.3 — IA generativa: conceitos, exemplos e casos de uso
- P1-6 — Ética e responsabilidade digital no serviço público

## Resumo

```text
NOTA DO EDITAL (8.11.2): na prova objetiva, cada item vale +1,00 ponto se a marcação concordar com o gabarito oficial definitivo, −1,00 ponto se discordar e 0,00 se não houver marcação ou houver marcação dupla (C e E) (Edital nº 1/2026, subitem 8.11.2). Só o fato e a fonte.

5.1 ENGENHARIA DE PROMPTS. Prompt = entrada em linguagem natural; engenharia de prompts = projetar e iterar a ENTRADA, sem mexer nos parâmetros (isso é fine-tuning). Elementos: papel, instrução, contexto, exemplos, formato, restrições, delimitadores (Markdown/XML, para separar instruções de dados). Técnicas: zero-shot (sem exemplo), one-shot (um), few-shot (vários; costuma render mais); chain-of-thought (raciocínio passo a passo em UM prompt); prompt chaining (VÁRIOS prompts encadeados); role prompting; RAG (recuperar documentos e inseri-los no prompt). Temperatura: alta = mais variação; baixa = mais previsível, não "mais verdadeira". Alucinação: saída plausível e falsa; bom prompt reduz, não elimina. Injeção de prompt: instrução maliciosa dentro do conteúdo lido.

5.2 TIPOS DE APRENDIZADO. SUPERVISIONADO: dados rotulados; regressão (número) e classificação (categoria; binária/multiclasse). NÃO SUPERVISIONADO: sem rótulos; clustering (o modelo encontra os grupos; o humano pode nomeá-los com base em seu entendimento dos dados), redução de dimensionalidade, anomalias, associação; "não supervisionado" = sem rótulos, não "sem humano" (o humano escolhe dados e parâmetros e interpreta resultados). POR REFORÇO: agente, ambiente, ação, recompensa/penalidade, política; sem rótulo por entrada; robôs, AlphaGo. RLHF = reforço com feedback humano, usado em ciclos de AJUSTE de LLMs. Modelos generativos: pré-treinados com grandes volumes de dados sem rótulos atribuídos manualmente → ajuste supervisionado ou por reforço. "IA generativa baseia-se prioritariamente em supervisionado" = ERRADO.

5.3 IA GENERATIVA. Cria conteúdo novo (texto, imagem, áudio, vídeo, código). Classificar é TAREFA; generativo/discriminativo é TIPO DE MODELO. Generativo modela p(X,Y)/p(X) — a distribuição — e gera (e pode classificar: Naive Bayes); discriminativo modela p(Y|X) — a fronteira. Modelo de fundação: enorme, pré-treinado em dados diversos, base para ajustes; LLM: modelo de linguagem com muitíssimos parâmetros; LLMs de uso geral costumam ser modelos de fundação de linguagem; nem todo modelo de fundação é LLM. Modalidades: texto→texto, →imagem, →vídeo, →código, →fala; imagem→texto; imagem-e-texto→imagem; multimodal. Conceitos: token, janela de contexto, temperatura, alucinação, RAG ≠ fine-tuning, agentes, data de corte (o modelo em si não consulta nada em tempo real). Casos de uso: sumarização, apoio à degravação, minutas, atendimento ao cidadão, busca semântica, acessibilidade, código. Riscos: alucinação, viés, vazamento, dependência, autoria, opacidade.

6 ÉTICA E RESPONSABILIDADE DIGITAL. O servidor responde pelo que faz com meios digitais e IA; a ferramenta não responde. CF art. 37: LIMPE. Decreto 1.171/1994: ética além da legalidade (Seção I, II); vedado DEIXAR DE usar avanços técnicos (XV, "e"). Lei 8.112: sigilo sobre assunto da repartição (116, VIII). LGPD: aplica-se ao Poder Público (art. 1º; Cap. IV, arts. 23–32); dado pessoal / sensível (5º, I, II); encarregado = canal entre controlador, titulares e a Agência Nacional de Proteção de Dados — ANPD (5º, VIII, redação da Lei 15.352/2026); anonimizado não é dado pessoal, salvo reversão (12, caput); princípios (6º, I–X); bases além do consentimento (7º, II, III); revisão de decisão automatizada (20) — sem exigência de pessoa natural (expressão retirada pela MP 869/2018; § 3º da Lei 13.853/2019 vetado); segurança (46) e incidentes (48). LAI: publicidade regra, sigilo exceção (3º, I); informações pessoais (31); prazos 25/15/5 anos (24, § 1º). Lei 9.610: atos oficiais sem proteção autoral (8º, IV). Princípios de IA (síntese autoral): supervisão humana, transparência, não discriminação, privacidade, accountability, segurança, veracidade, recursos públicos, acessibilidade, antidesinformação. Vale a redação em vigor em 2/10/2026 (13.33); legislação sem vigência só se explicitada nos objetos de avaliação (13.34) — o PL 2338/2023 não está, e fica só como contexto VOLÁTIL.
```

## Curso

```text
## ITEM 5.1 — ENGENHARIA DE PROMPTS

### 5.1.1 DEFINIÇÃO
Prompt é a entrada em linguagem natural (instrução, pergunta, contexto, exemplos) fornecida a um modelo de linguagem para obter uma resposta. Engenharia de prompts é a prática de projetar, testar e iterar prompts para que o modelo produza a saída desejada, SEM alterar os parâmetros internos do modelo. O glossário oficial do Google a define como "the art of creating prompts that elicit the desired responses from a large language model", acrescentando que é atividade humana e que o resultado depende, entre outros fatores, dos dados de treinamento e da temperatura.
Ponto central para a prova: engenharia de prompts atua na ENTRADA; fine-tuning atua nos PARÂMETROS. O glossário do Google define fine-tuning como "a second, task-specific training pass performed on a pre-trained model to refine its parameters".

### 5.1.2 ANATOMIA DE UM PROMPT
1. Papel ou persona — quem o modelo deve "ser". A Anthropic chama isso de role prompting; a OpenAI o coloca na mensagem de papel developer/system, que, segundo o guia oficial, tem prioridade sobre a mensagem do usuário.
2. Instrução ou tarefa — o verbo da ação (resuma, classifique, extraia, reescreva).
3. Contexto ou material de referência — o texto sobre o qual o modelo deve trabalhar. O guia da OpenAI recomenda "include relevant context information", inclusive dados externos ao treinamento recuperados por busca (RAG).
4. Exemplos — demonstrações de entrada e saída (zero-shot / few-shot, abaixo).
5. Formato de saída — tabela, JSON, número de linhas, "responda apenas C ou E". A OpenAI documenta controle de formato e Structured Outputs.
6. Restrições e critérios — o que NÃO fazer ("não invente nomes", "marque trechos inaudíveis como [inaudível]").
7. Delimitadores — separação das partes do prompt com Markdown ou tags XML, para que o modelo distinga instruções de dados de referência; recomendação explícita da Anthropic ("XML structuring") e da OpenAI ("Message formatting with Markdown and XML").

### 5.1.3 TÉCNICAS NOMEADAS
- Zero-shot: prompt sem nenhum exemplo de resposta esperada; só a instrução.
- One-shot: um único exemplo.
- Few-shot: "a prompt that contains more than one (a 'few') example"; segundo o glossário do Google, costuma produzir resultados melhores que zero-shot e one-shot, ao custo de um prompt mais longo. A OpenAI chama de "few-shot learning" e recomenda exemplos diversos.
- Chain-of-thought (cadeia de pensamento): "a prompt engineering technique that encourages a large language model to explain its reasoning, step by step". A Anthropic menciona a técnica como "thinking".
- Prompt chaining (encadeamento de prompts): dividir uma tarefa complexa em vários prompts sequenciais, em que a saída de um alimenta o seguinte ("prompt chaining"). NÃO confundir com chain-of-thought: no chaining há vários prompts; no chain-of-thought há um prompt que pede raciocínio explícito.
- Role prompting / system prompt: atribuição de papel.
- Instruções claras e diretas: primeira técnica mencionada pela Anthropic ("clarity"); a OpenAI recomenda instruções explícitas para modelos GPT e objetivos de alto nível para modelos de raciocínio.
- Fornecer contexto / RAG (retrieval-augmented generation): recuperar documentos relevantes (por exemplo, de um banco vetorial) e inseri-los no prompt antes de o modelo responder. RAG injeta conhecimento NA ENTRADA; fine-tuning altera o MODELO.
- Iteração e avaliação: a Anthropic condiciona a engenharia de prompts a critérios de sucesso claros e testes empíricos; a OpenAI recomenda fixar a versão (snapshot) do modelo em produção e medir o comportamento a cada mudança de prompt.

### 5.1.4 PARÂMETROS E LIMITES
- Temperatura: "a hyperparameter that controls the degree of randomness of a model's output"; valores altos geram respostas mais variadas, valores baixos, mais previsíveis. Temperatura baixa não significa resposta "mais verdadeira": significa resposta mais determinística.
- Janela de contexto: limite de tokens que o modelo processa por requisição; a OpenAI recomenda planejar o prompt em função desse limite. Token é a unidade em que o texto é fragmentado para o modelo (conceito geral).
- Alucinação: "the production of plausible-seeming but factually incorrect output by a generative AI model". Um prompt bem construído REDUZ, mas não ELIMINA alucinações.
- Injeção de prompt (conceito geral, sem fonte de fornecedor neste lote): instruções maliciosas embutidas em textos que o modelo lê e que tentam sobrepor-se às instruções legítimas. Mitigação: delimitar dados e tratar conteúdo externo como dado, não como instrução.

### 5.1.5 EXEMPLO APLICADO AO LEGISLATIVO
Situação: servidor do Derep (antigo DETAQ), departamento de registro e redação da Câmara, precisa de um resumo de três páginas de notas taquigráficas de uma audiência pública para subsidiar o relator.
Prompt fraco: "Resuma isso." (sem papel, sem formato, sem restrições, sem delimitação do texto)
Prompt estruturado:
  [Papel] Você é assessor de redação legislativa.
  [Tarefa] Resuma as notas taquigráficas abaixo em até 15 linhas.
  [Formato] Um parágrafo por orador, na ordem das falas; ao final, lista das propostas concretas apresentadas.
  [Restrições] Não atribua a um orador fala que ele não tenha feito; não acrescente informação externa; trechos marcados [inaudível] permanecem assim.
  [Contexto] <notas> ... texto ... </notas>
O que mudou: papel, instrução clara, formato de saída, restrições contra alucinação e delimitação do contexto com tags — as técnicas. Se o resumo precisasse ainda ser comparado com o relatório do relator, caberia um segundo prompt, encadeado (prompt chaining).

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
Aprendizado de máquina (ML) é o campo em que sistemas aprendem padrões a partir de dados, em vez de seguir regras explicitamente programadas. A página oficial do Google classifica os sistemas de ML por COMO aprendem, em quatro categorias: supervisionado, não supervisionado, por reforço e IA generativa. O edital pede os três primeiros aqui e a IA generativa no item 5.3.
Vocabulário transversal (conceitos gerais): atributos ou features, rótulo ou target, conjuntos de treino / validação / teste, generalização, sobreajuste (overfitting) e subajuste (underfitting).

### 5.2.2 APRENDIZADO SUPERVISIONADO
Definição: o modelo aprende a partir de dados ROTULADOS, isto é, exemplos que já trazem a resposta correta, e descobre a relação entre entradas e saídas. O Google compara a um estudante que se prepara com provas antigas já gabaritadas.
Duas tarefas clássicas:
- Regressão: prevê um VALOR NUMÉRICO contínuo. Exemplos: quantidade de chuva "in inches or millimeters"; preço futuro de uma casa a partir de metragem, CEP, número de quartos e banheiros e taxa de juros do financiamento ("Future house price"); tempo futuro de viagem até um destino, em minutos e segundos ("Future ride time").
- Classificação: prevê uma CATEGORIA. Exemplos: e-mail é spam ou não; a foto contém um gato. Pode ser binária ("rain" ou "no rain") ou multiclasse ("rain", "hail", "snow" ou "sleet").
Chave de prova: "o que o modelo devolve?" Número → regressão. Categoria → classificação. Ambas supervisionadas, porque exigem rótulos no treino.

### 5.2.3 APRENDIZADO NÃO SUPERVISIONADO
Definição: o modelo recebe dados SEM rótulos e busca padrões ou estruturas significativas. A técnica mais citada é o clustering (agrupamento), que reúne dados semelhantes; exemplo: agrupar dados meteorológicos por temperatura e descobrir as estações do ano.
Distinção decisiva — clustering × classificação: na classificação, as categorias são DEFINIDAS PREVIAMENTE pelo humano e o modelo atribui cada dado a uma delas; no clustering, os grupos NÃO são definidos previamente: o modelo os encontra, e o humano pode nomear os grupos com base em seu entendimento dos dados ("You might then attempt to name those clusters").
Outras tarefas não supervisionadas (conceitos gerais): redução de dimensionalidade, detecção de anomalias e regras de associação.
Armadilha de vocabulário: "não supervisionado" significa SEM RÓTULOS, não "sem participação humana". O humano escolhe os dados e os parâmetros e interpreta os resultados.

### 5.2.4 APRENDIZADO POR REFORÇO
Definição: o modelo (agente) aprende por tentativa e erro, interagindo com um AMBIENTE: executa AÇÕES, recebe RECOMPENSAS ou PENALIDADES e, com isso, constrói uma POLÍTICA (policy), a melhor estratégia para acumular recompensas. Exemplos: treinar robôs a caminhar por uma sala e o programa AlphaGo.
Diferença essencial: não há rótulo com a "resposta certa" para cada entrada; há um SINAL DE RECOMPENSA, muitas vezes atrasado. Isso distingue reforço de supervisionado.
Ponte com LLMs — RLHF (aprendizado por reforço com feedback humano): "using feedback from human raters to improve the quality of a model's responses"; o glossário do Google cita avaliações como 👍 e 👎. RLHF é uma etapa de AJUSTE de modelos generativos, não o método de pré-treinamento.

### 5.2.5 COMO OS TRÊS SE COMBINAM NOS MODELOS ATUAIS
Os modelos de IA generativa são, em regra, pré-treinados com grandes volumes de dados sem rótulos atribuídos manualmente e, em etapa posterior, podem ser ajustados por aprendizado supervisionado ou por reforço para tarefas específicas. É o que afirma: "generative models are initially trained using an unsupervised approach" e "the model is sometimes trained further using supervised or reinforcement learning". Conclusão para a prova: afirmar que a IA generativa se baseia PRIORITARIAMENTE em aprendizado supervisionado é ERRADO. Mecanismo semelhante aparece no item 81 do TRF6 2024, Cargo 2 (CEBRASPE_ANALOGA; gabarito definitivo E, conferido no GAB_DEFINITIVO_034_TRF6_002_01).
Observação de prudência: a literatura também chama o pré-treinamento de LLMs de "auto-supervisionado" (o próprio texto fornece o alvo). O enquadramento desse termo como subtipo do "não supervisionado" é disputado; o candidato deve ficar com a formulação e evitar itens que dependam da classificação do "auto-supervisionado".
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
P6. "Os modelos de IA generativa são pré-treinados predominantemente por aprendizado supervisionado em pares pergunta-resposta rotulados manualmente" → ERRADO (pré-treino sem rótulos; supervisionado e reforço no ajuste).
P7. "Na classificação, o modelo descobre as categorias por conta própria" → ERRADO (isso é clustering).

## ITEM 5.3 — IA GENERATIVA: CONCEITOS, EXEMPLOS E CASOS DE USO

### 5.3.1 DEFINIÇÃO
IA generativa é o ramo da IA cujos modelos CRIAM conteúdo novo — texto, imagem, áudio, vídeo, código — a partir de uma entrada do usuário, tendo aprendido os padrões dos dados de treinamento. O glossário do Google registra que se trata de "an emerging transformative field with no formal definition" e caracteriza os modelos pela capacidade de produzir conteúdo complexo, coerente e original. Definição operacional para a prova: gera conteúdo novo, em oposição a prever um valor ou uma categoria sobre conteúdo existente.
Distinção de vocabulário: CLASSIFICAR é uma TAREFA; GENERATIVO e DISCRIMINATIVO são TIPOS DE MODELO. Modelos generativos também podem ser usados para classificar: um classificador generativo (exemplo clássico: Naive Bayes, usado em filtros de spam) aprende a distribuição dos dados em cada classe e decide pela classe mais provável. Logo, "classifica" não implica "discriminativo".

### 5.3.2 GENERATIVA × DISCRIMINATIVA
- Modelo generativo modela a distribuição conjunta p(X, Y) — ou p(X), sem rótulos —, isto é, aprende COMO OS DADOS SE DISTRIBUEM e por isso consegue gerar novas instâncias realistas (fotos novas de animais; a próxima palavra de uma sequência). "Generative models have to model more."
- Modelo discriminativo modela a probabilidade condicional p(Y | X): aprende apenas a FRONTEIRA entre categorias ("discriminative models try to draw boundaries in the data space"), sem se importar com a plausibilidade de uma instância. Exemplo: distinguir cachorro de gato.
Tradução didática: o discriminativo responde "isto é A ou B?" traçando a fronteira; o generativo responde "como seria um novo exemplar de A?" — e, por conhecer a distribuição de cada classe, também pode responder "isto é A ou B?" (classificador generativo). Nenhum dos dois precisa necessariamente retornar uma probabilidade.

### 5.3.3 CONCEITOS ESTRUTURANTES
- Modelo de fundação (foundation model): "a very large pre-trained model trained on an enormous and diverse training set", que responde bem a pedidos variados e pode servir de base para ajustes posteriores. Pode ser multimodal.
- Grande modelo de linguagem (LLM): "at a minimum, a language model having a very high number of parameters"; informalmente, modelos de linguagem baseados em Transformer, como Gemini e GPT. Relação entre os termos: LLMs de uso geral costumam ser modelos de fundação de linguagem; nem todo modelo de fundação é LLM (há modelos de fundação de imagem ou multimodais).
- Modalidades: a lista em tópicos traz texto→texto, texto→imagem, texto→vídeo, texto→código, texto→fala e imagem-e-texto→imagem; a tabela de exemplos traz texto→texto, texto→imagem, texto→vídeo, texto→código e imagem→texto. "Multimodal" = aceita ou produz mais de um tipo de dado.
- Ciclo de treinamento: pré-treino sem rótulos atribuídos manualmente → ajuste supervisionado ou por reforço; fine-tuning; RLHF. Ver 5.2.5.
- Token, janela de contexto, temperatura: ver 5.1.4.
- Alucinação: saída plausível, porém factualmente incorreta. É propriedade do mecanismo (o modelo gera o provável, não o verificado).
- RAG: recuperação de documentos externos ao treinamento inseridos no prompt. Fine-tuning e RAG NÃO são sinônimos: um altera o modelo; o outro, a entrada.
- Agentes (conceito geral; a OpenAI documenta "agentic tasks"): modelos que planejam, usam ferramentas e executam tarefas em várias etapas.
- Conhecimento paramétrico e data de corte (conceito geral): sem ferramentas ou RAG, o modelo responde com o que incorporou no treinamento; o modelo em si não consulta a internet ou bancos de dados.
- Deepfake, marca d'água e proveniência (conceitos gerais).

### 5.3.4 EXEMPLOS E CASOS DE USO NO SERVIÇO PÚBLICO E NO LEGISLATIVO
Sumarização de discursos, audiências e documentos extensos; apoio à degravação e à revisão de notas taquigráficas (correção, padronização, pontuação), sempre com revisão humana e sem material sigiloso em ferramenta não homologada (ver item 6); redação de minutas a partir de modelo institucional; atendimento ao cidadão por assistentes conversacionais; busca semântica e classificação em acervos; extração de dados de PDFs; tradução e acessibilidade (descrição de imagens, legendas, linguagem simples); geração e revisão de código.
Riscos associados: alucinação (citar lei inexistente), viés, vazamento de dados pessoais ou sigilosos, dependência sem verificação, direitos autorais e falta de transparência sobre o uso de IA.

### 5.3.5 EXEMPLO APLICADO
Um gabinete pede a um assistente generativo "a jurisprudência do STF sobre CPI e quebra de sigilo". O modelo devolve três ementas com números de processo. Duas são reais; uma é inventada, com numeração verossímil. Diagnóstico: alucinação, inerente ao mecanismo generativo. Procedimento correto: usar RAG com base oficial ou ferramenta de busca verificável, pedir citação da fonte e CONFERIR cada ementa no sítio do tribunal antes de usar. Temperatura baixa não resolveria: tornaria a invenção apenas mais repetível.

### 5.3.6 PEGADINHAS PROVÁVEIS
P1. "Modelo generativo e modelo discriminativo são o mesmo tipo de modelo, distinguindo-se apenas pela tarefa executada" → ERRADO (são tipos distintos: um modela a distribuição, o outro, a fronteira; a tarefa de classificar pode ser feita por ambos).
P2. "A IA generativa baseia-se prioritariamente em aprendizado supervisionado" → ERRADO (mecanismo semelhante no TRF6 2024, item 81, gabarito definitivo E).
P3. "Por padrão, um LLM consulta a internet e bases de dados atualizadas antes de responder" → ERRADO.
P4. "Fine-tuning e RAG são denominações equivalentes da mesma técnica" → ERRADO.
P5. "Com temperatura zero, o modelo deixa de produzir informações falsas" → ERRADO.
P6. "Modelos de fundação restringem-se à geração de texto" → ERRADO (podem ser multimodais).
P7. "Alucinação é o erro de digitação ou de formatação da resposta" → ERRADO.
P8. "Todo modelo de fundação é um LLM" → ERRADO (há modelos de fundação de imagem e multimodais).

## ITEM 6 — ÉTICA E RESPONSABILIDADE DIGITAL NO SERVIÇO PÚBLICO

### 6.1 DEFINIÇÃO E ENQUADRAMENTO
Ética digital é a aplicação dos deveres éticos do servidor ao ambiente digital: uso de sistemas, dados, redes, ferramentas de IA e comunicação eletrônica. Responsabilidade digital é a contrapartida: o servidor permanece RESPONSÁVEL pelos atos que pratica com meios digitais, inclusive quando usa IA. A ferramenta não responde; o agente público responde.
Base constitucional: princípios da administração pública — legalidade, impessoalidade, moralidade, publicidade e eficiência (N8, CF art. 37, caput).
Base deontológica: o Código de Ética do Servidor Público Civil Federal (N4, Decreto 1.171/1994, Anexo, Capítulo I) dispõe, na Seção I (regras deontológicas), inciso II, que o servidor "não poderá jamais desprezar o elemento ético de sua conduta", decidindo não apenas entre o legal e o ilegal, mas "principalmente entre o honesto e o desonesto". A ética vai ALÉM da legalidade.
Observação de aplicabilidade: o Decreto 1.171/1994 é norma do Poder Executivo federal; na Câmara, o regime do servidor é a Lei 8.112/1990 (N5) e os atos internos da Casa. O candidato deve conhecer o Decreto como referência de ética no serviço público, sem afirmar que ele vincula diretamente o Legislativo.

6.2 PRINCÍPIOS ÉTICOS PARA USO DE IA E TECNOLOGIA — síntese autoral
1. Supervisão humana: decisões relevantes passam por pessoa responsável; a IA apoia, não decide sozinha.
2. Transparência e explicabilidade: informar quando há uso de IA; poder explicar critérios de uma decisão.
3. Não discriminação e equidade: vigilância contra viés algorítmico.
4. Privacidade e proteção de dados: minimização, finalidade, segurança (LGPD, abaixo).
5. Responsabilização (accountability): há sempre um responsável humano identificável.
6. Segurança: credenciais, phishing, engenharia social, deepfakes, ferramentas não homologadas.
7. Integridade e veracidade: verificar saídas de IA antes de usar.
8. Uso adequado de recursos públicos: equipamentos, redes e licenças institucionais servem ao interesse público.
9. Acessibilidade e inclusão digital (N9, Lei 13.146/2015, art. 63).
10. Combate à desinformação, inclusive conteúdo sintético.

6.3 MAPA NORMATIVO (artigo e inciso)
LGPD (N1, Lei 13.709/2018):
- Aplica-se a pessoa natural ou jurídica, de direito público ou privado (art. 1º, caput). O Capítulo IV ("Do Tratamento de Dados Pessoais pelo Poder Público") abrange os arts. 23 a 32 — Seção I (regras), arts. 23–30; Seção II (responsabilidade), arts. 31–32.
- Fundamentos (art. 2º): I respeito à privacidade; II autodeterminação informativa; III liberdade de expressão, de informação, de comunicação e de opinião; IV inviolabilidade da intimidade, da honra e da imagem; V desenvolvimento econômico e tecnológico e inovação; VI livre iniciativa, livre concorrência e defesa do consumidor; VII direitos humanos, livre desenvolvimento da personalidade, dignidade e exercício da cidadania pelas pessoas naturais.
- Definições (art. 5º): I dado pessoal; II dado pessoal sensível (origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico); III dado anonimizado (definição); VI controlador; VII operador; VIII encarregado — pela Lei 15.352, de 25/02/2026 (conversão da MP 1.317/2025; em vigor na publicação, DOU de 25/02/2026), o inciso passou a ter a redação: "encarregado: pessoa indicada pelo controlador e operador para atuar como canal de comunicação entre o controlador, os titulares dos dados e a Agência Nacional de Proteção de Dados (ANPD)" (vale para a prova, edital 13.33); X tratamento; XI anonimização; XII consentimento; XVII relatório de impacto; XIX autoridade nacional: "entidade da administração pública responsável por zelar, implementar e fiscalizar o cumprimento desta Lei em todo o território nacional" (redação dada pela Lei 15.352/2026; a redação anterior não foi conferida, e nada se afirma sobre o que mudou; sem item).
- Dados anonimizados (art. 12, caput): não são considerados dados pessoais para os fins da lei, SALVO quando o processo de anonimização for revertido com meios próprios ou puder ser revertido com esforços razoáveis. O art. 5º, III, apenas define o termo; o efeito jurídico está no art. 12.
- Princípios (art. 6º): I finalidade; II adequação; III necessidade; IV livre acesso; V qualidade dos dados; VI transparência; VII segurança; VIII prevenção; IX não discriminação; X responsabilização e prestação de contas.
- Bases legais (art. 7º): I consentimento; II cumprimento de obrigação legal ou regulatória pelo controlador; III pela administração pública, para o tratamento e uso compartilhado de dados necessários à execução de políticas públicas previstas em leis e regulamentos ou respaldadas em contratos, convênios ou instrumentos congêneres; (...) IX legítimo interesse (incisos I, II e III). Chave de prova: CONSENTIMENTO NÃO É A ÚNICA BASE, nem a principal para o Poder Público.
- Decisões automatizadas (art. 20, caput): direito do titular a solicitar a REVISÃO de decisões tomadas unicamente com base em tratamento automatizado que afetem seus interesses; § 1º: informações claras sobre os critérios. Histórico da expressão "por pessoa natural": o texto original de 2018 previa revisão "por pessoa natural"; a MP 869/2018 retirou a expressão; o § 3º incluído pela Lei 13.853/2019 foi vetado. Logo, o texto vigente não exige revisão por pessoa natural; item que afirme "revisão obrigatoriamente por pessoa natural" é ERRADO.
- Tratamento pelo Poder Público (art. 23, caput): atendimento de finalidade pública, na persecução do interesse público, para executar competências legais ou cumprir atribuições legais do serviço público; inciso I: dever de informar as hipóteses de tratamento, com informações claras e atualizadas.
- Segurança e incidentes: art. 46 (medidas técnicas e administrativas de segurança); art. 48 (comunicação de incidente de segurança à ANPD e ao titular).
LAI (N2, Lei 12.527/2011):
- Diretrizes (art. 3º): I publicidade como preceito geral e sigilo como exceção; II divulgação independentemente de solicitação (transparência ativa); III uso de meios de comunicação viabilizados pela tecnologia da informação; IV fomento à cultura de transparência; V controle social.
- Informações pessoais (art. 31, caput): tratamento transparente e com respeito à intimidade, vida privada, honra e imagem; § 1º, I: acesso restrito, pelo prazo máximo de 100 anos, a agentes públicos legalmente autorizados e à pessoa a que se referirem (caput e § 1º, I).
- Classificação de sigilo: art. 23, caput (informações imprescindíveis à segurança da sociedade ou do Estado, passíveis de classificação); art. 24, § 1º: I ultrassecreta 25 anos; II secreta 15 anos; III reservada 5 anos.
Governo Digital (N3, Lei 14.129/2021): aplica-se aos órgãos da administração pública direta federal, abrangendo os Poderes Executivo, Judiciário e Legislativo (art. 2º, I); entre os princípios e diretrizes do art. 3º estão a desburocratização (I), a transparência na execução dos serviços públicos (IV), o uso da tecnologia para otimizar processos de trabalho da administração pública (VIII), a proteção de dados pessoais nos termos da LGPD (XVII) e a acessibilidade da pessoa com deficiência ou com mobilidade reduzida (XIX). Não usada em item.
Código de Ética (N4, Decreto 1.171/1994, Anexo, Cap. I):
- Seção I, regras deontológicas: inciso II (elemento ético; honesto × desonesto); inciso VII (salvo os casos de segurança nacional, investigações policiais ou interesse superior do Estado e da Administração Pública, a serem preservados em processo previamente declarado sigiloso, nos termos da lei, a publicidade de qualquer ato administrativo constitui requisito de eficácia e moralidade); inciso VIII (direito à verdade: o servidor não pode omiti-la ou falseá-la).
- Seção II, deveres: inciso XIV, alíneas "m" (comunicar imediatamente a seus superiores todo e qualquer ato ou fato contrário ao interesse público), "g" (ser cortês, ter urbanidade, disponibilidade e atenção) e "q" (manter-se atualizado com as instruções, as normas de serviço e a legislação pertinentes ao órgão).
- Seção III, vedações: inciso XV, alínea "e": "deixar de utilizar os avanços técnicos e científicos ao seu alcance ou do seu conhecimento para atendimento do seu mister" — a OMISSÃO tecnológica também é vedada; alínea "a": uso do cargo para obter favorecimento; alínea "l": "retirar da repartição pública, sem estar legalmente autorizado, qualquer documento, livro ou bem pertencente ao patrimônio público" (o inciso XV não tem alínea "k").
Lei 8.112/1990 (N5): deveres (art. 116): II lealdade às instituições; III observância das normas legais e regulamentares; VIII guardar sigilo sobre assunto da repartição. Proibições (art. 117): IX valer-se do cargo para lograr proveito pessoal ou de outrem, em detrimento da dignidade da função pública; XVI utilizar pessoal ou recursos materiais da repartição em serviços ou atividades particulares. Responsabilidade (art. 121): o servidor responde civil, penal e administrativamente pelo exercício irregular de suas atribuições. Não fundamenta item.
Marco Civil da Internet (N6, Lei 12.965/2014): princípios (art. 3º): I liberdade de expressão; II proteção da privacidade; III proteção dos dados pessoais; direitos do usuário (art. 7º).
Direitos autorais (N7, Lei 9.610/1998): art. 8º, IV — textos de tratados, leis, decretos, regulamentos, decisões judiciais e demais atos oficiais NÃO são objeto de proteção autoral; art. 8º, I — ideias, procedimentos normativos, sistemas e métodos também não.
Norma interna da Câmara (N10): Ato da Mesa nº 225, de 15/12/2025 (DCD, Ed. Extra A, 18/12/2025): estabelece diretrizes gerais para a política de governança de inteligência artificial no âmbito da Câmara dos Deputados e determina sua implementação pela Diretoria-Geral. Em síntese, o art. 3º orienta a política para: princípios éticos, entre eles transparência, proteção de dados, não discriminação e supervisão humana (I); conformidade com a LGPD (III); disciplina do uso de IA generativa, com requisitos para prompts, para agentes autônomos ou semiautônomos e para revisão humana (V); informação ao usuário quando interage com agentes de IA (VIII); supervisão que inclui o monitoramento de vieses e alucinações (IX). O art. 4º, IV, prevê comitê de ética de uso da IA. Norma interna; referência de contexto; sem item.

Contexto VOLÁTIL: legislação sem vigência só pode ser cobrada se estiver explicitada nos objetos de avaliação (edital, 13.34: "A legislação que não esteja em vigor poderá ser cobrada, desde que devidamente explicitada nos objetos de avaliação"); como o item 14 do edital não explicita o PL 2338/2023 (marco legal da IA; situação de tramitação não verificada), ele fica só como contexto VOLÁTIL e não entra em item. Estratégia Brasileira de Inteligência Artificial, instituída pela Portaria MCTI nº 4.617, de 6/4/2021 (Anexo com redação dada pela Portaria MCTI nº 4.979/2021); vigência atual não conferida; sem item.

### 6.4 EXEMPLO APLICADO AO LEGISLATIVO
Situação: servidora do Derep (antigo DETAQ) recebe o áudio e a transcrição bruta de reunião reservada de comissão e pensa em colar o texto integral em um assistente de IA gratuito, acessado pela conta pessoal, para "limpar" a redação em dois minutos.
Análise:
1. Sigilo funcional: a reunião é reservada; expor o conteúdo a terceiro (o provedor da ferramenta) viola o dever de guardar sigilo sobre assunto da repartição (N5, art. 116, VIII) e a lógica da LAI, em que o sigilo legalmente previsto é exceção protegida (N2, art. 3º, I).
2. Dados pessoais: as falas contêm nomes, opiniões políticas (dado sensível, N1, art. 5º, II) e eventualmente dados de terceiros; o envio a serviço externo, por conta pessoal, tende a não encontrar base legal (art. 7º) e não atende às medidas de segurança do art. 46.
3. Responsabilidade: se o texto "limpo" contiver falas inventadas pela IA (alucinação) e for publicado, a responsabilidade é da servidora, não da ferramenta (supervisão humana; dever de verdade, N4, Seção I, VIII).
4. Recursos e ferramentas: usar ferramenta institucional homologada, se existir; se não existir, não é aceitável "resolver" com conta pessoal.
5. O que NÃO é a resposta: proibir toda IA. A vedação do Decreto 1.171/1994 (XV, "e") desaconselha a omissão tecnológica; a conduta correta é usar IA dentro de canais autorizados, com dados minimizados e revisão humana.

### 6.5 PEGADINHAS PROVÁVEIS
P1. "Dado anonimizado é espécie de dado pessoal sensível" → ERRADO (art. 12, caput: anonimizado não é dado pessoal, salvo reversão; art. 5º, III, define; sensível é o do art. 5º, II).
P2. "A LGPD não se aplica aos órgãos do Poder Legislativo" → ERRADO (art. 1º, caput; Capítulo IV, arts. 23 a 32).
P3. "O titular tem direito à revisão de decisões automatizadas obrigatoriamente por pessoa natural" → ERRADO (a expressão "por pessoa natural" foi retirada pela MP 869/2018 e o § 3º da Lei 13.853/2019 foi vetado).
P4. "Na LAI, o sigilo é a regra e a publicidade, a exceção" → ERRADO (art. 3º, I).
P5. "O consentimento do titular é a única base legal que autoriza a administração pública a tratar dados pessoais" → ERRADO (art. 7º, II e III).
P6. "O Código de Ética veda ao servidor o uso de avanços técnicos e científicos" → ERRADO (veda DEIXAR DE utilizá-los — XV, "e").
P7. "Quando a decisão é sugerida por sistema de IA, a responsabilidade pelo ato transfere-se ao sistema" → ERRADO.
P8. "Opinião política e filiação sindical não são dados sensíveis" → ERRADO (art. 5º, II).
P9. "Textos de leis e de atos oficiais são protegidos por direito autoral" → ERRADO (Lei 9.610/1998, art. 8º, IV).
P10. "Ética digital no serviço público limita-se às regras de uso de redes sociais" → ERRADO.
```

## Pares

- **Supervisionado** × **não supervisionado × por reforço** — rótulos | sem rótulos, busca de estrutura | sem rótulos, recompensa por ação e política | Troca: chamar clustering de supervisionado; dizer que reforço usa rótulos; dizer que não supervisionado dispensa humano.
- **Modelo generativo** × **modelo discriminativo** — modela p(X,Y) ou p(X), a distribuição; gera conteúdo novo; pode também classificar (classificador generativo, ex.: Naive Bayes) | modela p(Y|X), traça fronteiras; usado para classificar | Troca: "toda tarefa de classificação usa modelo discriminativo" (generalização indevida); "a generativa baseia-se prioritariamente em supervisionado".
- **Zero-shot** × **one-shot × few-shot** — nenhum exemplo | um exemplo | vários exemplos | Troca: definir few-shot como um exemplo.
- **Chain-of-thought** × **prompt chaining** — um prompt pedindo raciocínio passo a passo | vários prompts encadeados | Troca: descrever um com o nome do outro.
- **Engenharia de prompts** × **fine-tuning × RAG** — atua na entrada | altera parâmetros | recupera documentos e os insere na entrada | Troca: "prompt ajusta pesos"; "RAG retreina o modelo"; "fine-tuning e RAG são sinônimos".
- **Temperatura alta** × **baixa** — mais aleatória | mais previsível | Troca: inverter; ou "temperatura baixa garante veracidade".
- **Regressão** × **classificação** — valor numérico | categoria | Troca: inverter as saídas.
- **Clustering** × **classificação** — grupos encontrados pelo modelo; o humano pode nomeá-los com base em seu entendimento dos dados; sem rótulos | categorias definidas antes; com rótulos | Troca: "na classificação o modelo descobre as categorias".
- **Alucinação** × **viés** — conteúdo plausível e falso | tratamento sistematicamente desigual herdado dos dados | Troca: chamar viés de alucinação; reduzir alucinação a erro de formatação.
- **Modelo de fundação** × **LLM** — modelo enorme pré-treinado em dados diversos, inclusive imagem ou multimodal | modelo de linguagem com muitíssimos parâmetros; os de uso geral costumam ser modelos de fundação de linguagem | Troca: "todo modelo de fundação é LLM"; "modelo de fundação só gera texto".
- **Conhecimento paramétrico** × **consulta em tempo real** — o que o modelo incorporou até a data de corte | só com RAG, busca ou ferramentas | Troca: "por padrão o LLM consulta a internet".
- **Dado pessoal** × **dado sensível × dado anonimizado (LGPD 5º, I, II, III; 12, caput)** — identifica pessoa natural | categorias do 5º, II | não é dado pessoal, salvo reversão (12, caput) | Troca: anonimizado como sensível; opinião política como "não sensível".
- **Controlador** × **operador × encarregado (LGPD 5º, VI, VII, VIII)** — decide sobre o tratamento | trata em nome do controlador | pessoa indicada pelo controlador e operador como canal de comunicação entre o controlador, os titulares e a Agência Nacional de Proteção de Dados (ANPD) — redação do 5º, VIII, dada pela Lei 15.352/2026 | Troca: atribuir ao operador a decisão; ao encarregado, a execução.
- **Consentimento** × **demais bases legais (LGPD 7º)** — uma das bases (I) | obrigação legal (II), políticas públicas (III), legítimo interesse (IX) etc. | Troca: "consentimento é a única base para o Poder Público".
- **Publicidade** × **sigilo (LAI 3º, I)** — regra | exceção | Troca: inverter.
- **Legal** × **ético (Decreto 1.171, Seção I, II)** — conforme a lei | conforme a honestidade e o interesse público, além da lei | Troca: "se é legal, é ético".
- **Supervisão humana** × **automação total** — IA apoia; humano decide e responde | sistema decide sem revisão | Troca: "a responsabilidade transfere-se ao sistema"; "revisão obrigatoriamente por pessoa natural" (LGPD art. 20 não exige: expressão retirada pela MP 869/2018; § 3º da Lei 13.853/2019 vetado).
- **Usar IA** × **omitir tecnologia (Decreto 1.171, XV, "e")** — permitido e esperado, em canais autorizados | vedado deixar de usar avanços técnicos | Troca: "o Código de Ética veda o uso de avanços técnicos".
- **Injeção de prompt** × **jailbreak (conceitos gerais)** — instrução maliciosa embutida em conteúdo lido | tentativa direta do usuário de burlar restrições | Troca: usar um termo pelo outro.
- **Texto oficial** × **obra protegida (Lei 9.610, 8º, IV × 7º)** — atos oficiais sem proteção autoral | criações intelectuais protegidas | Troca: "atos oficiais são protegidos por direito autoral".

## Pegadinhas

- [P1-5.1] **Engenharia de prompts** — "A engenharia de prompts ajusta os pesos do modelo para a tarefa" → ERRADO (isso é fine-tuning).
- [P1-5.1] **Engenharia de prompts** — "Few-shot é o prompt que traz um único exemplo" → ERRADO (um exemplo é one-shot).
- [P1-5.1] **Engenharia de prompts** — "Chain-of-thought consiste em dividir a tarefa em prompts sucessivos" → ERRADO (isso é prompt chaining).
- [P1-5.1] **Engenharia de prompts** — "Temperatura mais baixa produz saídas mais variadas e criativas" → ERRADO (é o inverso).
- [P1-5.1] **Engenharia de prompts** — "Um prompt bem elaborado elimina a possibilidade de alucinação" → ERRADO (reduz, não elimina).
- [P1-5.1] **Engenharia de prompts** — "RAG consiste em retreinar o modelo com os documentos da organização" → ERRADO (RAG recupera documentos e os insere no prompt).
- [P1-5.1] **Engenharia de prompts** — "Zero-shot é a técnica em que o modelo recebe exemplos sem rótulo" → ERRADO (zero-shot = nenhum exemplo).
- [P1-5.2] **Aprendizado supervisionado, não supervisionado e por reforço** — "No aprendizado não supervisionado não há participação humana" → ERRADO.
- [P1-5.2] **Aprendizado supervisionado, não supervisionado e por reforço** — "Clustering é tarefa de aprendizado supervisionado" → ERRADO.
- [P1-5.2] **Aprendizado supervisionado, não supervisionado e por reforço** — "Regressão é a tarefa supervisionada que prevê a categoria à qual o dado pertence" → ERRADO.
- [P1-5.2] **Aprendizado supervisionado, não supervisionado e por reforço** — "No aprendizado por reforço, o agente recebe, para cada ação, o rótulo da ação correta" → ERRADO.
- [P1-5.2] **Aprendizado supervisionado, não supervisionado e por reforço** — "RLHF é uma técnica de aprendizado não supervisionado" → ERRADO.
- [P1-5.2] **Aprendizado supervisionado, não supervisionado e por reforço** — "Os modelos de IA generativa são pré-treinados predominantemente por aprendizado supervisionado em pares pergunta-resposta rotulados manualmente" → ERRADO (pré-treino sem rótulos; supervisionado e reforço no ajuste).
- [P1-5.2] **Aprendizado supervisionado, não supervisionado e por reforço** — "Na classificação, o modelo descobre as categorias por conta própria" → ERRADO (isso é clustering).
- [P1-5.3] **IA generativa: conceitos, exemplos e casos de uso** — "Modelo generativo e modelo discriminativo são o mesmo tipo de modelo, distinguindo-se apenas pela tarefa executada" → ERRADO (são tipos distintos: um modela a distribuição, o outro, a fronteira; a tarefa de classificar pode ser feita por ambos).
- [P1-5.3] **IA generativa: conceitos, exemplos e casos de uso** — "A IA generativa baseia-se prioritariamente em aprendizado supervisionado" → ERRADO (mecanismo semelhante no TRF6 2024, item 81, gabarito definitivo E).
- [P1-5.3] **IA generativa: conceitos, exemplos e casos de uso** — "Por padrão, um LLM consulta a internet e bases de dados atualizadas antes de responder" → ERRADO.
- [P1-5.3] **IA generativa: conceitos, exemplos e casos de uso** — "Fine-tuning e RAG são denominações equivalentes da mesma técnica" → ERRADO.
- [P1-5.3] **IA generativa: conceitos, exemplos e casos de uso** — "Com temperatura zero, o modelo deixa de produzir informações falsas" → ERRADO.
- [P1-5.3] **IA generativa: conceitos, exemplos e casos de uso** — "Modelos de fundação restringem-se à geração de texto" → ERRADO (podem ser multimodais).
- [P1-5.3] **IA generativa: conceitos, exemplos e casos de uso** — "Alucinação é o erro de digitação ou de formatação da resposta" → ERRADO.
- [P1-5.3] **IA generativa: conceitos, exemplos e casos de uso** — "Todo modelo de fundação é um LLM" → ERRADO (há modelos de fundação de imagem e multimodais).
- [P1-6] **Ética e responsabilidade digital no serviço público** — "Dado anonimizado é espécie de dado pessoal sensível" → ERRADO (art. 12, caput: anonimizado não é dado pessoal, salvo reversão; art. 5º, III, define; sensível é o do art. 5º, II).
- [P1-6] **Ética e responsabilidade digital no serviço público** — "A LGPD não se aplica aos órgãos do Poder Legislativo" → ERRADO (art. 1º, caput; Capítulo IV, arts. 23 a 32).
- [P1-6] **Ética e responsabilidade digital no serviço público** — "O titular tem direito à revisão de decisões automatizadas obrigatoriamente por pessoa natural" → ERRADO (a expressão "por pessoa natural" foi retirada pela MP 869/2018 e o § 3º da Lei 13.853/2019 foi vetado).
- [P1-6] **Ética e responsabilidade digital no serviço público** — "Na LAI, o sigilo é a regra e a publicidade, a exceção" → ERRADO (art. 3º, I).
- [P1-6] **Ética e responsabilidade digital no serviço público** — "O consentimento do titular é a única base legal que autoriza a administração pública a tratar dados pessoais" → ERRADO (art. 7º, II e III).
- [P1-6] **Ética e responsabilidade digital no serviço público** — "O Código de Ética veda ao servidor o uso de avanços técnicos e científicos" → ERRADO (veda DEIXAR DE utilizá-los — XV, "e").
- [P1-6] **Ética e responsabilidade digital no serviço público** — "Quando a decisão é sugerida por sistema de IA, a responsabilidade pelo ato transfere-se ao sistema" → ERRADO.
- [P1-6] **Ética e responsabilidade digital no serviço público** — "Opinião política e filiação sindical não são dados sensíveis" → ERRADO (art. 5º, II).
- [P1-6] **Ética e responsabilidade digital no serviço público** — "Textos de leis e de atos oficiais são protegidos por direito autoral" → ERRADO (Lei 9.610/1998, art. 8º, IV).
- [P1-6] **Ética e responsabilidade digital no serviço público** — "Ética digital no serviço público limita-se às regras de uso de redes sociais" → ERRADO.
