# Lote 4 — TID-IA (P1 5.1–5.3 e 6) — gabarito e justificativas

Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC)

### L4-01 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: TC (tentação: fine-tuning). Engenharia de prompts atua na entrada e não altera parâmetros; alterar parâmetros é fine-tuning.

### L4-02 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: TC. Um único exemplo é one-shot; few-shot é "more than one (a 'few') example"; a parte sobre zero-shot está correta, mas o item é errado pela troca.

### L4-03 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: AT. A descrição é do chain-of-thought; prompt chaining é a sequência de vários prompts.

### L4-04 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: IC. Temperatura controla a aleatoriedade: baixa = mais previsível; nada garante correção factual; alucinação é saída plausível e incorreta.

### L4-05 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: GI invertida (tentação: ver delimitadores como preciosismo). Delimitar instruções, exemplos e dados ajuda o modelo a tratar o conteúdo de referência como dado, não como instrução; é recomendação de documentação oficial — Anthropic, "XML structuring" e OpenAI, "Message formatting with Markdown and XML".

### L4-06 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: TC. RAG recupera documentos externos e os insere no prompt; retreinar o modelo é fine-tuning.

### L4-07 — Gabarito: C

- Item do edital: P1-5.2
- Justificativa: sem armadilha (ancoragem). Supervisionado usa dados com a resposta correta; regressão prevê valor numérico.

### L4-08 — Gabarito: E

- Item do edital: P1-5.2
- Justificativa: TC. A descrição é da classificação (categorias definidas antes pelo humano); no clustering, o modelo encontra os grupos, e o humano pode nomeá-los com base em seu entendimento dos dados ("You might then attempt to name those clusters").

### L4-09 — Gabarito: E

- Item do edital: P1-5.2
- Justificativa: GI. "Não supervisionado" significa ausência de rótulos nos dados; o humano escolhe os dados e os parâmetros e interpreta os resultados — e pode nomear os grupos encontrados.

### L4-10 — Gabarito: C

- Item do edital: P1-5.2
- Justificativa: TC. O reforço aprende por recompensas e penalidades de ações no ambiente, gerando uma política; não há rótulo da ação correta por entrada.

### L4-11 — Gabarito: C

- Item do edital: P1-5.2
- Justificativa: GI invertida (tentação: "prioritariamente supervisionado"). O F4 afirma que "generative models are initially trained using an unsupervised approach" e que "the model is sometimes trained further using supervised or reinforcement learning"; o item descreve o pré-treino como "sem rótulos atribuídos manualmente", sem classificar o "auto-supervisionado". Mecanismo semelhante: TRF6 2024, Cargo 2, item 81 (CEBRASPE_ANALOGA; gabarito definitivo E, conferido no GAB_DEFINITIVO_034_TRF6_002_01) — referência, não fundamento.

### L4-12 — Gabarito: C

- Item do edital: P1-5.3
- Justificativa: TC (tentação: inverter os papéis). Discriminativo modela p(Y|X) e "tries to draw boundaries in the data space"; generativo modela p(X,Y) ou p(X), a distribuição, e por isso gera instâncias novas. O item fala só de "um modelo discriminativo", sem exemplo de spam.

### L4-13 — Gabarito: E

- Item do edital: P1-5.3
- Justificativa: GI. Modelo de fundação é "a very large pre-trained model trained on an enormous and diverse training set", não necessariamente texto; LLM é modelo de linguagem com muitíssimos parâmetros.

### L4-14 — Gabarito: C

- Item do edital: P1-5.3
- Justificativa: sem armadilha (ancoragem). Definição literal: "the production of plausible-seeming but factually incorrect output by a generative AI model".

### L4-15 — Gabarito: E

- Item do edital: P1-5.3
- Justificativa: GI + IC. O modelo, por si só, responde com o conhecimento incorporado no treinamento; consulta a dados externos só com RAG, busca ou ferramentas acopladas; "sempre a informação mais atual" é generalização indevida.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L4-16 — Gabarito: E

- Item do edital: P1-5.3
- Justificativa: TC. Fine-tuning altera parâmetros; RAG insere documentos na entrada; não são equivalentes nem diferem "apenas no custo".

### L4-17 — Gabarito: C

- Item do edital: P1-6
- Justificativa: TC (tentação: ler a ressalva como erro). LGPD, art. 12, caput: dados anonimizados não são dados pessoais, salvo quando a anonimização for revertida ou puder sê-lo com esforços razoáveis; art. 5º, III, apenas define. Base: N1, art. 12, caput; art. 5º, III.

### L4-18 — Gabarito: E

- Item do edital: P1-6
- Justificativa: GI. O consentimento (art. 7º, I) é uma das bases; a execução de políticas públicas pela administração tem base própria no art. 7º, III, além da obrigação legal (art. 7º, II). Base: N1, art. 7º, I, II e III.

### L4-19 — Gabarito: E

- Item do edital: P1-6
- Justificativa: IC (responsabilidade deslocada para o instrumento). A ferramenta não é agente público; quem pratica o ato responde por ele; supervisão humana é o princípio aplicável (curso 6.1 e 6.2). Gabarito E sem dependência de norma; o item não se apoia em dispositivo legal.

### L4-20 — Gabarito: C

- Item do edital: P1-6
- Justificativa: GI invertida. LAI, art. 3º, I: publicidade como preceito geral e sigilo como exceção; exceções legais incluem informações pessoais (art. 31, caput, e § 1º, I) e informações classificadas (art. 23, caput; art. 24, § 1º, I a III). Base: N2, arts. 3º, I; 23, caput; 24, § 1º, I a III; 31, caput, e § 1º, I.

### 4C-01 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: TC (elementos do prompt trocados). Curso 5.1.2: o CONTEXTO (ou material de referência) é o texto sobre o qual o modelo deve trabalhar; os EXEMPLOS são demonstrações de entrada e saída. O item troca as definições. Difere do item 2 do Lote 4 porque aquele julga o número de exemplos que define o few-shot; este julga o que é "contexto" e o que é "exemplo" na anatomia do prompt. Fonte: curso 5.1.2 (itens 3 e 4).

### 4C-02 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: sem armadilha (ancoragem). Curso 5.1.3: o few-shot costuma produzir resultados melhores que o zero-shot e o one-shot, ao custo de um prompt mais longo. O item usa "costuma", como o curso, e não afirma ganho garantido. Difere do item 2 do Lote 4 porque aquele julga a definição de few-shot pelo número de exemplos; este julga o efeito relatado e o custo.

### 4C-03 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: GI invertida (tentação: "engenharia de prompts controla a saída; logo o prompt é o único fator" → marcar E). Curso 5.1.1: o resultado depende, entre outros fatores, dos dados de treinamento e da temperatura. O item diz que o prompt não é o único fator, sem afirmar que o texto do prompt é irrelevante. Difere do item 4 do Lote 4 porque aquele julga a relação entre temperatura baixa e veracidade; este julga a pluralidade de fatores que determinam a saída.

### 4C-04 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: TC (definições trocadas). Curso 5.1.4: temperatura é o hiperparâmetro que controla o grau de aleatoriedade da saída; janela de contexto é o limite de tokens que o modelo processa por requisição. O item inverte as duas definições. Difere do item 4 do Lote 4 porque aquele julga se temperatura baixa assegura veracidade; este julga a definição de temperatura e a de janela de contexto. Fonte: curso 5.1.4 (janela de contexto, conceito geral).

### 4C-05 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: GI. Curso 5.1.4 e 5.1.6, P5: um prompt bem construído REDUZ, mas não ELIMINA alucinações; o curso 5.3.5 e o princípio 7 do curso 6.2 exigem conferir a saída antes de usá-la. "Elimina" e "dispensável a conferência humana" são generalização indevida. Difere do item 14 do Lote 4 porque aquele julga a definição de alucinação; este julga o alcance do prompt como medida contra ela. Fonte: curso 5.1.4 (conceito consistente com a definição de alucinação).

### 4C-06 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: AT (tentação: tomar a instrução longa ou a descrição do formato desejado por "exemplo" e concluir que o prompt é one-shot → marcar E). Curso 5.1.2 (itens 4 e 5): exemplos são demonstrações de entrada e saída; o formato de saída é a forma da resposta (tabela, JSON, número de linhas) e, descrito em palavras, não é demonstração. Curso 5.1.3: zero-shot = prompt sem nenhum exemplo de resposta esperada, só a instrução. A extensão da instrução e a descrição do formato não a transformam em exemplo. Difere do item 2 do Lote 4 porque aquele julga o few-shot pelo número de exemplos (um único exemplo é one-shot); este julga o zero-shot pela ausência de qualquer demonstração, ainda que a instrução seja longa e detalhada. Fonte: curso 5.1.2 e 5.1.3.

### 4C-07 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: sem armadilha (ancoragem). Curso 5.1.1: engenharia de prompts é a prática de projetar, testar e iterar prompts; curso 5.1.3: a iteração e avaliação pressupõem critérios de sucesso claros e testes empíricos e a medição do comportamento a cada mudança de prompt. O item afirma só o conceito geral, sem recurso de produto.

### 4C-08 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: GI (restrição indevida do conceito; tentação: tratar a injeção de prompt como sinônimo do ataque direto do usuário). Curso 5.1.4: injeção de prompt = instruções maliciosas embutidas em textos que o modelo lê e que tentam sobrepor-se às instruções legítimas (conceito geral, sem fonte de fornecedor, como no curso). O item não depende de a literatura tratar o jailbreak como espécie de injeção ou como categoria distinta; basta que a injeção abranja as instruções embutidas em textos lidos, o que o curso afirma e o termo "restringe-se" nega. O item não usa o par injeção × jailbreak (C19) como critério. Fonte: curso 5.1.4.

### 4C-09 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: sem armadilha (ancoragem). Curso 5.1.2 (item 3): o contexto é o texto sobre o qual o modelo deve trabalhar; curso 5.1.3: o RAG recupera documentos e os insere no prompt; curso 5.3.3: sem ferramentas ou RAG, o modelo responde com o que incorporou no treinamento (conhecimento paramétrico). Um relatório elaborado depois do treinamento não integra esse conhecimento; sem ferramentas externas (como a busca), sem RAG e sem retreinamento, o caminho é incluí-lo no prompt, como contexto. O acréscimo "e sem retreinamento" existe porque o curso (5.1.1; 5.3.3) prevê o fine-tuning como outra forma de incorporar conhecimento: sem a ressalva, o "deve" ficaria vulnerável a recurso. Difere do item 15 do Lote 4 porque aquele julga se o modelo consulta fontes externas por si só; este julga a aplicação (o material entra como contexto do prompt). Difere do item 6 do Lote 4 porque aquele julga RAG × retreinamento. Fonte: curso 5.1.2, 5.1.3 e 5.3.3.

### 4C-10 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: TC (formato × restrição; não sutil). Curso 5.1.2 (item 6): restrições e critérios indicam o que o modelo NÃO deve fazer ("não invente nomes"); curso 5.1.5: no exemplo, "não atribua a um orador fala que ele não tenha feito" é restrição, e não formato. Formato de saída (item 5 do curso 5.1.2) é a forma da resposta (tabela, JSON, número de linhas). O item julga apenas a natureza da determinação negativa, sem depender da fronteira entre formato e restrição em instruções mistas. Fonte: curso 5.1.2 e 5.1.5.
