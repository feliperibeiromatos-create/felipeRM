# Lote 4 — TID-IA (P1 5.1–5.3 e 6) — gabarito e justificativas

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
- Justificativa: GI invertida (tentação: ver delimitadores como preciosismo). Delimitar instruções, exemplos e dados ajuda o modelo a tratar o conteúdo de referência como dado, não como instrução; é recomendação de documentação oficial — Anthropic, "XML structuring" e OpenAI, "Message formatting with Markdown and XML". Sem marca VOLÁTIL: o item afirma o conceito, não recurso de produto.

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
- Justificativa: GI invertida (tentação: "prioritariamente supervisionado"). O item descreve o pré-treino como "sem rótulos atribuídos manualmente", sem classificar o "auto-supervisionado". Mecanismo semelhante: TRF6 2024, Cargo 2, item 81 (CEBRASPE_ANALOGA; gabarito definitivo E, conferido no GAB_DEFINITIVO_034_TRF6_002_01) — referência, não fundamento.

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
