# Lote 4 — TID-IA (P1 5.1–5.3 e 6) — gabarito e justificativas

Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC)

### L4-01 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: Armadilha: troca de conceito (tentação: fine-tuning). Engenharia de prompts atua na entrada e não altera parâmetros; alterar parâmetros é fine-tuning. Fonte: Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 7/10/2026.

### L4-02 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: Armadilha: troca de conceito. Um único exemplo é one-shot; few-shot é "more than one (a 'few') example"; a parte sobre zero-shot está correta, mas o item é errado pela troca. Fonte: Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 7/10/2026.

### L4-03 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: Armadilha: atribuição errada de técnica. A descrição é do chain-of-thought; prompt chaining é a sequência de vários prompts. Fontes: Google for Developers, "Machine Learning Glossary: Generative AI"; Anthropic, "Prompt engineering overview", verificadas em 7/10/2026.

### L4-04 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: Armadilha: inversão de causa e efeito. Temperatura controla a aleatoriedade: baixa = mais previsível; nada garante correção factual; alucinação é saída plausível e incorreta. Fonte: Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 7/10/2026.

### L4-05 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: Armadilha: generalização indevida invertida (tentação: ver delimitadores como preciosismo). Delimitar instruções, exemplos e dados ajuda o modelo a tratar o conteúdo de referência como dado, não como instrução; é recomendação de documentação oficial — Anthropic, "XML structuring" (em "Prompt engineering overview") e OpenAI, "Message formatting with Markdown and XML" (em "Prompt engineering"), verificadas em 7/10/2026. O item afirma o conceito, não recurso de produto; não depende de informação sujeita a mudança.

### L4-06 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: Armadilha: troca de conceito. RAG recupera documentos externos e os insere no prompt; retreinar o modelo é fine-tuning. Fontes: OpenAI, "Prompt engineering"; Google for Developers, "Machine Learning Glossary: Generative AI", verificadas em 7/10/2026.

### L4-07 — Gabarito: C

- Item do edital: P1-5.2
- Justificativa: Item de fixação do aprendizado supervisionado e da regressão. Supervisionado usa dados com a resposta correta; regressão prevê valor numérico; a página do Google for Developers ("Introduction to ML: What is Machine Learning?") cita a chuva "in inches or millimeters". Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", reverificado em 7/10/2026.

### L4-08 — Gabarito: E

- Item do edital: P1-5.2
- Justificativa: Armadilha: troca de conceito. A descrição é da classificação (categorias definidas antes pelo humano); no clustering, o modelo encontra os grupos, e o humano pode nomeá-los com base em seu entendimento dos dados (Google for Developers, "Introduction to ML: What is Machine Learning?": "You might then attempt to name those clusters"). Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 7/10/2026.

### L4-09 — Gabarito: E

- Item do edital: P1-5.2
- Justificativa: Armadilha: generalização indevida. "Não supervisionado" significa ausência de rótulos nos dados; o humano escolhe os dados e os parâmetros e interpreta os resultados — e pode nomear os grupos encontrados (Google for Developers, "Introduction to ML: What is Machine Learning?"). Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 7/10/2026.

### L4-10 — Gabarito: C

- Item do edital: P1-5.2
- Justificativa: Armadilha: troca de conceito. O reforço aprende por recompensas e penalidades de ações no ambiente, gerando uma política; não há rótulo da ação correta por entrada. Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 7/10/2026.

### L4-11 — Gabarito: C

- Item do edital: P1-5.2
- Justificativa: Armadilha: generalização indevida invertida (tentação: "prioritariamente supervisionado"). A página do Google for Developers ("Introduction to ML: What is Machine Learning?") afirma que "generative models are initially trained using an unsupervised approach" e que "the model is sometimes trained further using supervised or reinforcement learning"; o item descreve o pré-treino como "sem rótulos atribuídos manualmente", sem classificar o "auto-supervisionado". Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", reverificado em 7/10/2026. Mecanismo semelhante: TRF6 2024, Cargo 2, item 81 (item análogo do Cebraspe; gabarito definitivo E, conferido no gabarito definitivo do TRF6) — referência, não fundamento.

### L4-12 — Gabarito: C

- Item do edital: P1-5.3
- Justificativa: Armadilha: troca de conceito (tentação: inverter os papéis). Discriminativo modela p(Y|X) e "tries to draw boundaries in the data space"; generativo modela p(X,Y) ou p(X), a distribuição, e por isso gera instâncias novas. O item fala só de "um modelo discriminativo", sem exemplo de spam. Fonte: Google for Developers, "GAN — Background: What is a Generative Model?", verificado em 7/10/2026.

### L4-13 — Gabarito: E

- Item do edital: P1-5.3
- Justificativa: Armadilha: generalização indevida. Modelo de fundação é "a very large pre-trained model trained on an enormous and diverse training set", não necessariamente texto; LLM é modelo de linguagem com muitíssimos parâmetros; o glossário do Google for Developers, "Machine Learning Glossary: Generative AI" define os termos separadamente. Fonte: Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 7/10/2026.

### L4-14 — Gabarito: C

- Item do edital: P1-5.3
- Justificativa: Item de fixação da definição de alucinação. Definição literal: "the production of plausible-seeming but factually incorrect output by a generative AI model". Fonte: Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 7/10/2026.

### L4-15 — Gabarito: E

- Item do edital: P1-5.3
- Justificativa: Armadilha: generalização indevida e inversão de causa e efeito. O modelo, por si só, responde com o conhecimento incorporado no treinamento; consulta a dados externos só com RAG, busca ou ferramentas acopladas (OpenAI, "Prompt engineering"); "sempre a informação mais atual" é generalização indevida. Fonte: OpenAI, "Prompt engineering", verificado em 7/10/2026.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L4-16 — Gabarito: E

- Item do edital: P1-5.3
- Justificativa: Armadilha: troca de conceito. Fine-tuning altera parâmetros; RAG insere documentos na entrada; não são equivalentes nem diferem "apenas no custo". Fontes: Google for Developers, "Machine Learning Glossary: Generative AI"; OpenAI, "Prompt engineering", verificadas em 7/10/2026.

### L4-17 — Gabarito: C

- Item do edital: P1-6
- Justificativa: Armadilha: troca de conceito (tentação: ler a ressalva como erro). LGPD, art. 12, caput: dados anonimizados não são dados pessoais, salvo quando a anonimização for revertida ou puder sê-lo com esforços razoáveis; art. 5º, III, apenas define. Base: Lei 13.709/2018 (LGPD), art. 12, caput; art. 5º, III.

### L4-18 — Gabarito: E

- Item do edital: P1-6
- Justificativa: Armadilha: generalização indevida. O consentimento (art. 7º, I) é uma das bases; a execução de políticas públicas pela administração tem base própria no art. 7º, III, além da obrigação legal (art. 7º, II). Base: Lei 13.709/2018 (LGPD), art. 7º, I, II e III.

### L4-19 — Gabarito: E

- Item do edital: P1-6
- Justificativa: Armadilha: inversão de causa e efeito (responsabilidade deslocada para o instrumento). A ferramenta não é agente público; quem pratica o ato responde por ele; supervisão humana é o princípio aplicável (curso 6.1 e 6.2). Gabarito E sem dependência de norma; o item não se apoia em dispositivo legal.

### L4-20 — Gabarito: C

- Item do edital: P1-6
- Justificativa: Armadilha: generalização indevida invertida. LAI, art. 3º, I: publicidade como preceito geral e sigilo como exceção; exceções legais incluem informações pessoais (art. 31, caput, e § 1º, I) e informações classificadas (art. 23, caput; art. 24, § 1º, I a III). Base: Lei 12.527/2011 (LAI), arts. 3º, I; 23, caput; 24, § 1º, I a III; 31, caput, e § 1º, I.

### 4C-01 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: Armadilha: troca de conceito (elementos do prompt trocados). Curso 5.1.2: o CONTEXTO (ou material de referência) é o texto sobre o qual o modelo deve trabalhar; os EXEMPLOS são demonstrações de entrada e saída. O item troca as definições. Fonte: curso 5.1.2 (itens 3 e 4).

### 4C-02 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: Item de fixação do efeito do few-shot sobre o resultado. Curso 5.1.3: o few-shot costuma produzir resultados melhores que o zero-shot e o one-shot, ao custo de um prompt mais longo (Google for Developers, "Machine Learning Glossary: Generative AI"). O item usa "costuma", como o curso, e não afirma ganho garantido. Fonte: Google for Developers, "Machine Learning Glossary: Generative AI".

### 4C-03 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: Armadilha: generalização indevida invertida (tentação: "engenharia de prompts controla a saída; logo o prompt é o único fator" → marcar E). Curso 5.1.1: o resultado depende, entre outros fatores, dos dados de treinamento e da temperatura (Google for Developers, "Machine Learning Glossary: Generative AI"). O item diz que o prompt não é o único fator, sem afirmar que o texto do prompt é irrelevante. Fonte: Google for Developers, "Machine Learning Glossary: Generative AI".

### 4C-04 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: Armadilha: troca de conceito (definições trocadas). Curso 5.1.4: temperatura é o hiperparâmetro que controla o grau de aleatoriedade da saída (Google for Developers, "Machine Learning Glossary: Generative AI"); janela de contexto é o limite de tokens que o modelo processa por requisição. O item inverte as duas definições. Fonte: Google for Developers, "Machine Learning Glossary: Generative AI" (temperatura) e curso 5.1.4 (janela de contexto, conceito geral).

### 4C-05 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: Armadilha: generalização indevida. Curso 5.1.4 e 5.1.6: um prompt bem construído REDUZ, mas não ELIMINA alucinações; o curso 5.3.5 e o princípio 7 do curso 6.2 exigem conferir a saída antes de usá-la. "Elimina" e "dispensável a conferência humana" são generalização indevida. Fonte: curso 5.1.4 (conceito consistente com a definição de alucinação do glossário do Google for Developers, "Machine Learning Glossary: Generative AI").

### 4C-06 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: Armadilha: atribuição errada de técnica (tentação: tomar a instrução longa ou a descrição do formato desejado por "exemplo" e concluir que o prompt é one-shot → marcar E). Curso 5.1.2 (itens 4 e 5): exemplos são demonstrações de entrada e saída; o formato de saída é a forma da resposta (tabela, JSON, número de linhas) e, descrito em palavras, não é demonstração. Curso 5.1.3: zero-shot = prompt sem nenhum exemplo de resposta esperada, só a instrução (Google for Developers, "Machine Learning Glossary: Generative AI"). A extensão da instrução e a descrição do formato não a transformam em exemplo. Fonte: Google for Developers, "Machine Learning Glossary: Generative AI", zero-shot ("A prompt that does not provide an example of how you want the large language model to respond"), e curso 5.1.2 e 5.1.3.

### 4C-07 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: Item de fixação do conceito de engenharia de prompts. Curso 5.1.1: engenharia de prompts é a prática de projetar, testar e iterar prompts; curso 5.1.3: a iteração e avaliação pressupõem critérios de sucesso claros e testes empíricos (Anthropic, "Prompt engineering overview") e a medição do comportamento a cada mudança de prompt (OpenAI, "Prompt engineering"). O item afirma só o conceito geral, sem recurso de produto. Fonte: Anthropic, "Prompt engineering overview"; OpenAI, "Prompt engineering".

### 4C-08 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: Armadilha: generalização indevida (restrição indevida do conceito; tentação: tratar a injeção de prompt como sinônimo do ataque direto do usuário). Curso 5.1.4: injeção de prompt = instruções maliciosas embutidas em textos que o modelo lê e que tentam sobrepor-se às instruções legítimas (conceito geral, sem fonte de fornecedor, como no curso). O item não depende de a literatura tratar o jailbreak como espécie de injeção ou como categoria distinta; basta que a injeção abranja as instruções embutidas em textos lidos, o que o curso afirma e o termo "restringe-se" nega. O item não usa o par injeção × jailbreak  como critério. Fonte: curso 5.1.4.

### 4C-09 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: Item de fixação da aplicação do material de referência como contexto do prompt. Curso 5.1.2 (item 3): o contexto é o texto sobre o qual o modelo deve trabalhar; curso 5.1.3: o RAG recupera documentos e os insere no prompt; curso 5.3.3: sem ferramentas ou RAG, o modelo responde com o que incorporou no treinamento (conhecimento paramétrico). Um relatório elaborado depois do treinamento não integra esse conhecimento; sem ferramentas externas (como a busca), sem RAG e sem retreinamento, o caminho é incluí-lo no prompt, como contexto. O acréscimo "e sem retreinamento" existe porque o curso (5.1.1; 5.3.3) prevê o fine-tuning como outra forma de incorporar conhecimento: sem a ressalva, o "deve" ficaria vulnerável a recurso. Fonte: curso 5.1.2, 5.1.3 e 5.3.3.

### 4C-10 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: Armadilha: troca de conceito (formato × restrição; não sutil). Curso 5.1.2 (item 6): restrições e critérios indicam o que o modelo NÃO deve fazer ("não invente nomes"); curso 5.1.5: no exemplo, "não atribua a um orador fala que ele não tenha feito" é restrição, e não formato. Formato de saída (item 5 do curso 5.1.2) é a forma da resposta (tabela, JSON, número de linhas). O item julga apenas a natureza da determinação negativa, sem depender da fronteira entre formato e restrição em instruções mistas. Fonte: curso 5.1.2 e 5.1.5.
