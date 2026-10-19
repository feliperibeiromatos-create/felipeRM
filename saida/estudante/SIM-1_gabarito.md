# Simulado 1 — P1 final (TI e Dados, itens 5 a 8) — gabarito

- Versão: v1
- Número de itens: 40

### 1 — 4C-02 — Gabarito: C

- Item do edital: P1-5.1 (aderência: direta)
- Justificativa: Item de fixação do efeito do few-shot sobre o resultado. Curso 5.1.3: o few-shot costuma produzir resultados melhores que o zero-shot e o one-shot, ao custo de um prompt mais longo (Google for Developers, "Machine Learning Glossary: Generative AI"). O item usa "costuma", como o curso, e não afirma ganho garantido. Fonte: Google for Developers, "Machine Learning Glossary: Generative AI".

### 2 — L4-04 — Gabarito: C

- Item do edital: P1-5.1 (aderência: direta)
- Justificativa: Armadilha: inversão de causa e efeito. Temperatura controla a aleatoriedade: baixa = mais previsível; nada garante correção factual; alucinação é saída plausível e incorreta. Fonte: Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 7/10/2026.

### 3 — 4C-05 — Gabarito: E

- Item do edital: P1-5.1 (aderência: direta)
- Justificativa: Armadilha: generalização indevida. Curso 5.1.4 e 5.1.6: um prompt bem construído REDUZ, mas não ELIMINA alucinações; o curso 5.3.5 e o princípio 7 do curso 6.2 exigem conferir a saída antes de usá-la. "Elimina" e "dispensável a conferência humana" são generalização indevida. Fonte: curso 5.1.4 (conceito consistente com a definição de alucinação do glossário do Google for Developers, "Machine Learning Glossary: Generative AI").

### 4 — L4-03 — Gabarito: E

- Item do edital: P1-5.1 (aderência: direta)
- Justificativa: Armadilha: atribuição errada de técnica. A descrição é do chain-of-thought; prompt chaining é a sequência de vários prompts. Fontes: Google for Developers, "Machine Learning Glossary: Generative AI"; Anthropic, "Prompt engineering overview", verificadas em 7/10/2026.

### 5 — 4C-08 — Gabarito: E

- Item do edital: P1-5.1 (aderência: direta)
- Justificativa: Armadilha: generalização indevida (restrição indevida do conceito; tentação: tratar a injeção de prompt como sinônimo do ataque direto do usuário). Curso 5.1.4: injeção de prompt = instruções maliciosas embutidas em textos que o modelo lê e que tentam sobrepor-se às instruções legítimas (conceito geral, sem fonte de fornecedor, como no curso). O item não depende de a literatura tratar o jailbreak como espécie de injeção ou como categoria distinta; basta que a injeção abranja as instruções embutidas em textos lidos, o que o curso afirma e o termo "restringe-se" nega. O item não usa o par injeção × jailbreak como critério. Fonte: curso 5.1.4.

### 6 — 4C-07 — Gabarito: C

- Item do edital: P1-5.1 (aderência: direta)
- Justificativa: Item de fixação do conceito de engenharia de prompts. Curso 5.1.1: engenharia de prompts é a prática de projetar, testar e iterar prompts; curso 5.1.3: a iteração e avaliação pressupõem critérios de sucesso claros e testes empíricos (Anthropic, "Prompt engineering overview") e a medição do comportamento a cada mudança de prompt (OpenAI, "Prompt engineering"). O item afirma só o conceito geral, sem recurso de produto. Fonte: Anthropic, "Prompt engineering overview"; OpenAI, "Prompt engineering".

### 7 — L4-01 — Gabarito: C

- Item do edital: P1-5.1 (aderência: direta)
- Justificativa: Armadilha: troca de conceito (tentação: fine-tuning). Engenharia de prompts atua na entrada e não altera parâmetros; alterar parâmetros é fine-tuning. Fonte: Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 7/10/2026.

### 8 — L4-06 — Gabarito: E

- Item do edital: P1-5.1 (aderência: direta)
- Justificativa: Armadilha: troca de conceito. RAG recupera documentos externos e os insere no prompt; retreinar o modelo é fine-tuning. Fontes: OpenAI, "Prompt engineering"; Google for Developers, "Machine Learning Glossary: Generative AI", verificadas em 7/10/2026.

### 9 — L4-08 — Gabarito: E

- Item do edital: P1-5.2 (aderência: direta)
- Justificativa: Armadilha: troca de conceito. A descrição é da classificação (categorias definidas antes pelo humano); no clustering, o modelo encontra os grupos, e o humano pode nomeá-los com base em seu entendimento dos dados (Google for Developers, "Introduction to ML: What is Machine Learning?": "You might then attempt to name those clusters"). Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 7/10/2026.

### 10 — L4-07 — Gabarito: C

- Item do edital: P1-5.2 (aderência: direta)
- Justificativa: Item de fixação do aprendizado supervisionado e da regressão. Supervisionado usa dados com a resposta correta; regressão prevê valor numérico; a página do Google for Developers ("Introduction to ML: What is Machine Learning?") cita a chuva "in inches or millimeters". Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", reverificado em 7/10/2026.

### 11 — L4-09 — Gabarito: E

- Item do edital: P1-5.2 (aderência: direta)
- Justificativa: Armadilha: generalização indevida. "Não supervisionado" significa ausência de rótulos nos dados; o humano escolhe os dados e os parâmetros e interpreta os resultados — e pode nomear os grupos encontrados (Google for Developers, "Introduction to ML: What is Machine Learning?"). Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 7/10/2026.

### 12 — L4-10 — Gabarito: C

- Item do edital: P1-5.2 (aderência: direta)
- Justificativa: Armadilha: troca de conceito. O reforço aprende por recompensas e penalidades de ações no ambiente, gerando uma política; não há rótulo da ação correta por entrada. Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 7/10/2026.

### 13 — L4-14 — Gabarito: C

- Item do edital: P1-5.3 (aderência: direta)
- Justificativa: Item de fixação da definição de alucinação. Definição literal: "the production of plausible-seeming but factually incorrect output by a generative AI model". Fonte: Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 7/10/2026.

### 14 — L4-12 — Gabarito: C

- Item do edital: P1-5.3 (aderência: direta)
- Justificativa: Armadilha: troca de conceito (tentação: inverter os papéis). Discriminativo modela p(Y|X) e "tries to draw boundaries in the data space"; generativo modela p(X,Y) ou p(X), a distribuição, e por isso gera instâncias novas. O item fala só de "um modelo discriminativo", sem exemplo de spam. Fonte: Google for Developers, "GAN — Background: What is a Generative Model?", verificado em 7/10/2026.

### 15 — L4-13 — Gabarito: E

- Item do edital: P1-5.3 (aderência: direta)
- Justificativa: Armadilha: generalização indevida. Modelo de fundação é "a very large pre-trained model trained on an enormous and diverse training set", não necessariamente texto; LLM é modelo de linguagem com muitíssimos parâmetros; o glossário do Google for Developers, "Machine Learning Glossary: Generative AI" define os termos separadamente. Fonte: Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 7/10/2026.

### 16 — L4-16 — Gabarito: E

- Item do edital: P1-5.3 (aderência: direta)
- Justificativa: Armadilha: troca de conceito. Fine-tuning altera parâmetros; RAG insere documentos na entrada; não são equivalentes nem diferem "apenas no custo". Fontes: Google for Developers, "Machine Learning Glossary: Generative AI"; OpenAI, "Prompt engineering", verificadas em 7/10/2026.

### 17 — L4-17 — Gabarito: C

- Item do edital: P1-6 (aderência: direta)
- Justificativa: Armadilha: troca de conceito (tentação: ler a ressalva como erro). LGPD, art. 12, caput: dados anonimizados não são dados pessoais, salvo quando a anonimização for revertida ou puder sê-lo com esforços razoáveis; art. 5º, III, apenas define. Base: Lei 13.709/2018 (LGPD), art. 12, caput; art. 5º, III.

### 18 — L4-18 — Gabarito: E

- Item do edital: P1-6 (aderência: direta)
- Justificativa: Armadilha: generalização indevida. O consentimento (art. 7º, I) é uma das bases; a execução de políticas públicas pela administração tem base própria no art. 7º, III, além da obrigação legal (art. 7º, II). Base: Lei 13.709/2018 (LGPD), art. 7º, I, II e III.

### 19 — L4-20 — Gabarito: C

- Item do edital: P1-6 (aderência: direta)
- Justificativa: Armadilha: generalização indevida, às avessas. LAI, art. 3º, I: publicidade como preceito geral e sigilo como exceção; exceções legais incluem informações pessoais (art. 31, caput, e § 1º, I) e informações classificadas (art. 23, caput; art. 24, § 1º, I a III). Base: Lei 12.527/2011 (LAI), arts. 3º, I; 23, caput; 24, § 1º, I a III; 31, caput, e § 1º, I.

### 20 — L4-19 — Gabarito: E

- Item do edital: P1-6 (aderência: direta)
- Justificativa: Armadilha: inversão de causa e efeito (responsabilidade deslocada para o instrumento). A ferramenta não é agente público; quem pratica o ato responde por ele; supervisão humana é o princípio aplicável (curso 6.1 e 6.2). Gabarito E sem dependência de norma; o item não se apoia em dispositivo legal.

### 21 — A5-03 — Gabarito: E

- Item do edital: P1-7.1 (aderência: direta)
- Justificativa: Armadilha: generalização indevida (restrição indevida). Filtragem e criação de campos calculados são operações típicas de transformação, ao lado de junção, pivotagem e agregação.

### 22 — A5-02 — Gabarito: C

- Item do edital: P1-7.1 (aderência: direta)
- Justificativa: Armadilha: troca de conceito (tentação: "modifica valores, logo é transformação" → marcar E). Padronizar grafias divergentes corrige um problema de qualidade (formatos inconsistentes), o que é limpeza; agregação é somar ou contar registros. O ponto seguro do curso 7.1.4: limpeza corrige qualidade; agregar e derivar não é limpar.

### 23 — A5-04 — Gabarito: E

- Item do edital: P1-7.1 (aderência: direta)
- Justificativa: Armadilha: troca de conceito. Texto livre e áudio são dados não estruturados; estruturados seguem esquema fixo, como tabelas.

### 24 — A5-01 — Gabarito: C

- Item do edital: P1-7.1 (aderência: direta)
- Justificativa: O partido qualifica o registro (atributo); a contagem mensal é valor quantitativo agregado (métrica).

### 25 — A5-06 — Gabarito: E

- Item do edital: P1-8.1 (aderência: direta)
- Justificativa: Armadilha: troca de conceito (recomendada no lugar de desaconselhada). O comprimento da barra codifica o valor; truncar a base distorce a proporção; barras partem de zero.

### 26 — A5-07 — Gabarito: E

- Item do edital: P1-8.1 (aderência: direta)
- Justificativa: Armadilha: troca de conceito (sequencial no lugar de qualitativa). Categorias sem ordem pedem paleta qualitativa; a sequencial sugere magnitude ordenada.

### 27 — A5-05 — Gabarito: C

- Item do edital: P1-8.1 (aderência: direta)
- Justificativa: Clareza e alta razão dados/tinta são princípios centrais de visualização.

### 28 — A5-12 — Gabarito: E

- Item do edital: P1-8.2 (aderência: direta)
- Justificativa: Armadilha: generalização indevida. O box plot resume por quartis e mediana e oculta a forma detalhada (bimodalidade); quem a mostra é o histograma.

### 29 — 5C-03 — Gabarito: E

- Item do edital: P1-8.2 (aderência: direta)
- Justificativa: Armadilha: troca de conceito (agrupado e empilhado trocados). Curso 8.2, gráfico de barras: agrupado = subcategorias lado a lado; empilhado = partes de um total; pegadinha do curso: empilhado quando se quer comparar as partes entre si. O item inverte os papéis.

### 30 — 5C-04 — Gabarito: C

- Item do edital: P1-8.2 (aderência: direta)
- Justificativa: Item de fixação: a disposição horizontal do gráfico de barras. Curso 8.2, gráfico de barras: vertical (colunas) ou horizontal, esta melhor para rótulos longos. O item usa "preferível", equivalente ao "melhor" do curso, e não proíbe a vertical.

### 31 — 5C-05 — Gabarito: C

- Item do edital: P1-8.2 (aderência: direta)
- Justificativa: Item de fixação: o que o gráfico de bolhas acrescenta ao de dispersão. Curso 8.2, gráfico de dispersão: o gráfico de bolhas acrescenta uma terceira variável no tamanho.

### 32 — A5-11 — Gabarito: C

- Item do edital: P1-8.2 (aderência: direta)
- Justificativa: Armadilha: inversão de causa e efeito (tentação: alinhamento quase perfeito → "prova causa" → marcar E). Dispersão mostra associação; correlação, por mais forte, não comprova causalidade.

### 33 — A5-10 — Gabarito: E

- Item do edital: P1-8.2 (aderência: direta)
- Justificativa: Armadilha: atribuição errada de técnica. Linha pressupõe eixo horizontal ordenado (tempo); ligar categorias sem ordem sugere continuidade inexistente; comparação entre categorias pede gráfico de barras.

### 34 — A5-09 — Gabarito: C

- Item do edital: P1-8.2 (aderência: direta)
- Justificativa: Armadilha: troca de conceito (tentação: quem decorou "barras separadas" como regra marca E). As barras do histograma são contíguas porque as classes são intervalos adjacentes de uma escala numérica; no gráfico de barras, o espaçamento é convenção de desenho; o que distingue os dois é a natureza da variável (curso 8.2).

### 35 — A5-20 — Gabarito: C

- Item do edital: P1-8.4 (aderência: direta)
- Justificativa: Destaque e anotação guiam o olhar do público ao que sustenta a conclusão.

### 36 — A5-18 — Gabarito: C

- Item do edital: P1-8.4 (aderência: direta)
- Justificativa: Definição essencial: dados, visual e narrativa a serviço de uma mensagem.

### 37 — A5-19 — Gabarito: E

- Item do edital: P1-8.4 (aderência: direta)
- Justificativa: Armadilha: troca de conceito (exploratória no lugar de explanatória). O perfil descrito é o da análise explanatória; na exploratória o analista ainda investiga.

### 38 — 5C-10 — Gabarito: E

- Item do edital: P1-8.4 (aderência: direta)
- Justificativa: Armadilha: inversão de causa e efeito (inversão da ordem: a mensagem vem antes da escolha dos gráficos). Curso 8.4, método: entender o contexto; definir a mensagem principal antes de escolher gráficos; depois, escolher a visualização adequada. O item inverte a ordem.

### 39 — 5C-09 — Gabarito: C

- Item do edital: P1-8.4 (aderência: direta)
- Justificativa: Item de fixação: a estrutura narrativa do storytelling. Curso 8.4, estrutura narrativa: contexto (público e o que está em jogo), conflito ou problema (o que os dados revelam), resolução ou chamada à ação (o que fazer).

### 40 — 5C-07 — Gabarito: E

- Item do edital: P1-8.4 (aderência: direta)
- Justificativa: Armadilha: troca de conceito (storytelling e dashboard trocados). Curso 8.4: o storytelling tem uma mensagem central; o dashboard é exploração aberta, com muitos indicadores. O item inverte as duas caracterizações.
