# simulado_1_gabarito.md — T-06; T-31 — 2026-10-10 — gerado por gbq-csc

# Simulado 1 (P1 — final) — Gabarito, mapa e verificação

Folha separada do `saida/simulados/simulado_1.md`. Nada deste arquivo vai à candidata sem gatilho da GBQ. Gabarito e justificativas copiados literalmente do (d-G) GABARITO COMENTADO dos arquivos canônicos (a justificativa é a entrada integral do d-G, sem o identificador inicial; [TS] = troca sutil de conceito, conforme a legenda do lote).

## Gabarito

| nº | gab | nº | gab | nº | gab | nº | gab | nº | gab |
|---|---|---|---|---|---|---|---|---|---|
| 1 | C | 9 | E | 17 | C | 25 | E | 33 | E |
| 2 | C | 10 | C | 18 | E | 26 | E | 34 | C |
| 3 | E | 11 | E | 19 | C | 27 | C | 35 | E |
| 4 | E | 12 | C | 20 | E | 28 | E | 36 | C |
| 5 | E | 13 | C | 21 | E | 29 | E | 37 | C |
| 6 | C | 14 | C | 22 | C | 30 | C | 38 | E |
| 7 | C | 15 | E | 23 | E | 31 | C | 39 | C |
| 8 | E | 16 | E | 24 | C | 32 | C | 40 | E |

## Mapa item → fonte

Rótulo de todos os itens: AUTORAL. Aderência direta por construção (registro AUTORAL v2, R4). Pontuação: +1,00 / −1,00 / 0,00 (edital 8.11.2).

| nº | id do lote | lote (arquivo) | subitem do edital | gab | [TS] | justificativa (copiada do d-G do lote) |
|---|---|---|---|---|---|---|
| 1 | 4C-02 | Lote 4-C — `saida/gcb/GCB_Lote4C_v1_GCB-CPP.md` | P1-5.1 (5.1 Engenharia de prompts) | C | não | C — 5.1 — sem armadilha (ancoragem). Curso 5.1.3: o few-shot costuma produzir resultados melhores que o zero-shot e o one-shot, ao custo de um prompt mais longo (F3). O item usa "costuma", como o curso, e não afirma ganho garantido. Difere do item 2 do Lote 4 porque aquele julga a definição de few-shot pelo número de exemplos; este julga o efeito relatado e o custo. Fonte: F3, conforme o curso 5.1.3. |
| 2 | L4-04 | Lote 4 — `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | P1-5.1 (5.1 Engenharia de prompts) | C | sim | C — [TS] — 5.1 — IC. Temperatura controla a aleatoriedade: baixa = mais previsível; nada garante correção factual; alucinação é saída plausível e incorreta. Fonte: F3, verificado em 7/10/2026. |
| 3 | 4C-05 | Lote 4-C — `saida/gcb/GCB_Lote4C_v1_GCB-CPP.md` | P1-5.1 (5.1 Engenharia de prompts) | E | não | E — 5.1 — GI. Curso 5.1.4 e 5.1.6, P5: um prompt bem construído REDUZ, mas não ELIMINA alucinações; o curso 5.3.5 e o princípio 7 do curso 6.2 exigem conferir a saída antes de usá-la. "Elimina" e "dispensável a conferência humana" são generalização indevida. Difere do item 14 do Lote 4 porque aquele julga a definição de alucinação; este julga o alcance do prompt como medida contra ela. Fonte: curso 5.1.4 (conceito consistente com a definição de alucinação do F3). |
| 4 | L4-03 | Lote 4 — `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | P1-5.1 (5.1 Engenharia de prompts) | E | sim | E — [TS] — 5.1 — AT. A descrição é do chain-of-thought; prompt chaining é a sequência de vários prompts. Fontes: F3, F1, verificadas em 7/10/2026. |
| 5 | 4C-08 | Lote 4-C — `saida/gcb/GCB_Lote4C_v1_GCB-CPP.md` | P1-5.1 (5.1 Engenharia de prompts) | E | sim | E — [TS] — 5.1 — GI (restrição indevida do conceito; tentação: tratar a injeção de prompt como sinônimo do ataque direto do usuário). Curso 5.1.4: injeção de prompt = instruções maliciosas embutidas em textos que o modelo lê e que tentam sobrepor-se às instruções legítimas (conceito geral, sem fonte de fornecedor, como no curso). Lição O10: o item não depende de a literatura tratar o jailbreak como espécie de injeção ou como categoria distinta; basta que a injeção abranja as instruções embutidas em textos lidos, o que o curso afirma e o termo "restringe-se" nega. O item não usa o par injeção × jailbreak (C19) como critério. Fonte: curso 5.1.4. |
| 6 | 4C-07 | Lote 4-C — `saida/gcb/GCB_Lote4C_v1_GCB-CPP.md` | P1-5.1 (5.1 Engenharia de prompts) | C | não | C — 5.1 — sem armadilha (ancoragem). Curso 5.1.1: engenharia de prompts é a prática de projetar, testar e iterar prompts; curso 5.1.3: a iteração e avaliação pressupõem critérios de sucesso claros e testes empíricos (F1) e a medição do comportamento a cada mudança de prompt (F2). O item afirma só o conceito geral, sem recurso de produto. Fonte: F1 e F2, conforme o curso 5.1.3. |
| 7 | L4-01 | Lote 4 — `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | P1-5.1 (5.1 Engenharia de prompts) | C | sim | C — [TS] — 5.1 — TC (tentação: fine-tuning). Engenharia de prompts atua na entrada e não altera parâmetros; alterar parâmetros é fine-tuning. Fonte: F3, verificado em 7/10/2026. |
| 8 | L4-06 | Lote 4 — `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | P1-5.1 (5.1 Engenharia de prompts) | E | sim | E — [TS] — 5.1 — TC. RAG recupera documentos externos e os insere no prompt; retreinar o modelo é fine-tuning. Fontes: F2, F3, verificadas em 7/10/2026. |
| 9 | L4-08 | Lote 4 — `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | P1-5.2 (5.2 Aprendizado supervisionado, não supervisionado e por reforço) | E | sim | E — [TS] — 5.2 — TC. A descrição é da classificação (categorias definidas antes pelo humano); no clustering, o modelo encontra os grupos, e o humano pode nomeá-los com base em seu entendimento dos dados (F4: "You might then attempt to name those clusters"). Fonte: F4, verificado em 7/10/2026. (v3 — O12) |
| 10 | L4-07 | Lote 4 — `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | P1-5.2 (5.2 Aprendizado supervisionado, não supervisionado e por reforço) | C | não | C — 5.2 — sem armadilha (ancoragem). Supervisionado usa dados com a resposta correta; regressão prevê valor numérico; o F4 cita a chuva "in inches or millimeters". Fonte: F4, reverificado em 7/10/2026. |
| 11 | L4-09 | Lote 4 — `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | P1-5.2 (5.2 Aprendizado supervisionado, não supervisionado e por reforço) | E | não | E — 5.2 — GI. "Não supervisionado" significa ausência de rótulos nos dados; o humano escolhe os dados e os parâmetros e interpreta os resultados — e pode nomear os grupos encontrados (F4). Fonte: F4, verificado em 7/10/2026. (v3 — O12) |
| 12 | L4-10 | Lote 4 — `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | P1-5.2 (5.2 Aprendizado supervisionado, não supervisionado e por reforço) | C | sim | C — [TS] — 5.2 — TC. O reforço aprende por recompensas e penalidades de ações no ambiente, gerando uma política; não há rótulo da ação correta por entrada. Fonte: F4, verificado em 7/10/2026. |
| 13 | L4-14 | Lote 4 — `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | P1-5.3 (5.3 IA generativa: conceitos, exemplos e casos de uso) | C | não | C — 5.3 — sem armadilha (ancoragem). Definição literal: "the production of plausible-seeming but factually incorrect output by a generative AI model". Fonte: F3, verificado em 7/10/2026. |
| 14 | L4-12 | Lote 4 — `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | P1-5.3 (5.3 IA generativa: conceitos, exemplos e casos de uso) | C | sim | C — [TS] — v3 (O11) — 5.3 — TC (tentação: inverter os papéis). Discriminativo modela p(Y\|X) e "tries to draw boundaries in the data space"; generativo modela p(X,Y) ou p(X), a distribuição, e por isso gera instâncias novas. O item fala só de "um modelo discriminativo", sem exemplo de spam. Fonte: F5, verificado em 7/10/2026. |
| 15 | L4-13 | Lote 4 — `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | P1-5.3 (5.3 IA generativa: conceitos, exemplos e casos de uso) | E | não | E — 5.3 — GI. Modelo de fundação é "a very large pre-trained model trained on an enormous and diverse training set", não necessariamente texto; LLM é modelo de linguagem com muitíssimos parâmetros; o F3 define os termos separadamente (O1). Fonte: F3, verificado em 7/10/2026. |
| 16 | L4-16 | Lote 4 — `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | P1-5.3 (5.3 IA generativa: conceitos, exemplos e casos de uso) | E | sim | E — [TS] — 5.3 — TC. Fine-tuning altera parâmetros; RAG insere documentos na entrada; não são equivalentes nem diferem "apenas no custo". Fontes: F3, F2, verificadas em 7/10/2026. |
| 17 | L4-17 | Lote 4 — `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | P1-6 (6 Ética e responsabilidade digital no serviço público) | C | sim | C — [TS] — 6 — TC (tentação: ler a ressalva como erro). LGPD, art. 12, caput: dados anonimizados não são dados pessoais, salvo quando a anonimização for revertida ou puder sê-lo com esforços razoáveis; art. 5º, III, apenas define. Base: N1, art. 12, caput; art. 5º, III. Aprovado pela CQFP (art. 12, caput, conferido no Planalto em 07/10/2026). |
| 18 | L4-18 | Lote 4 — `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | P1-6 (6 Ética e responsabilidade digital no serviço público) | E | não | E — v3.1 — 6 — GI. O consentimento (art. 7º, I) é uma das bases; a execução de políticas públicas pela administração tem base própria no art. 7º, III, além da obrigação legal (art. 7º, II). Base: N1, art. 7º, I, II e III — conferido pela CQFP no Planalto em 08/10/2026. |
| 19 | L4-20 | Lote 4 — `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | P1-6 (6 Ética e responsabilidade digital no serviço público) | C | não | C — v3.1 — 6 — GI invertida. LAI, art. 3º, I: publicidade como preceito geral e sigilo como exceção; exceções legais incluem informações pessoais (art. 31, caput, e § 1º, I) e informações classificadas (art. 23, caput; art. 24, § 1º, I a III). Base: N2, arts. 3º, I; 23, caput; 24, § 1º, I a III; 31, caput, e § 1º, I — conferidos pela CQFP no Planalto em 08/10/2026. |
| 20 | L4-19 | Lote 4 — `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | P1-6 (6 Ética e responsabilidade digital no serviço público) | E | não | E — v3.1 — 6 — IC (responsabilidade deslocada para o instrumento). A ferramenta não é agente público; quem pratica o ato responde por ele; supervisão humana é o princípio aplicável (curso 6.1 e 6.2). Gabarito E aprovado pela CQFP sem dependência de norma; o item não se apoia em dispositivo legal. |
| 21 | A5-03 | Lote 5 — `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` | P1-7.1 (7.1 Conceitos, atributos, métricas, transformação de dados) | E | não | E — novo — 7.1 — GI (restrição indevida). Filtragem e criação de campos calculados são operações típicas de transformação, ao lado de junção, pivotagem e agregação. |
| 22 | A5-02 | Lote 5 — `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` | P1-7.1 (7.1 Conceitos, atributos, métricas, transformação de dados) | C | sim | C — [TS] — v3 (F3 b) — 7.1 — TC (tentação: "modifica valores, logo é transformação" → marcar E). Padronizar grafias divergentes corrige um problema de qualidade (formatos inconsistentes), o que é limpeza; agregação é somar ou contar registros. O ponto seguro do curso 7.1.4: limpeza corrige qualidade; agregar e derivar não é limpar. |
| 23 | A5-04 | Lote 5 — `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` | P1-7.1 (7.1 Conceitos, atributos, métricas, transformação de dados) | E | sim | E — [TS] — (A) — 7.1 — TC. Texto livre e áudio são dados não estruturados; estruturados seguem esquema fixo, como tabelas. |
| 24 | A5-01 | Lote 5 — `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` | P1-7.1 (7.1 Conceitos, atributos, métricas, transformação de dados) | C | não | C — (A) — 7.1. O partido qualifica o registro (atributo); a contagem mensal é valor quantitativo agregado (métrica). |
| 25 | A5-06 | Lote 5 — `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` | P1-8.1 (8.1 Princípios de visualização de dados) | E | sim | E — [TS] — (A) — 8.1 — TC (recomendada no lugar de desaconselhada). O comprimento da barra codifica o valor; truncar a base distorce a proporção; barras partem de zero. |
| 26 | A5-07 | Lote 5 — `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` | P1-8.1 (8.1 Princípios de visualização de dados) | E | sim | E — [TS] — (A) — 8.1 — TC (sequencial no lugar de qualitativa). Categorias sem ordem pedem paleta qualitativa; a sequencial sugere magnitude ordenada. |
| 27 | A5-05 | Lote 5 — `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` | P1-8.1 (8.1 Princípios de visualização de dados) | C | não | C — (A) — 8.1. Clareza e alta razão dados/tinta são princípios centrais de visualização. |
| 28 | A5-12 | Lote 5 — `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` | P1-8.2 (8.2 Tipos de gráficos (histograma, linha, barra, dispersão, box plot)) | E | não | E — novo — 8.2 — GI. O box plot resume por quartis e mediana e oculta a forma detalhada (bimodalidade); quem a mostra é o histograma. |
| 29 | 5C-03 | Lote 5-C — `saida/gcb/GCB_Lote5C_v1_GCB-CPP.md` | P1-8.2 (8.2 Tipos de gráficos (histograma, linha, barra, dispersão, box plot)) | E | sim | E — [TS] — 8.2 — TC (agrupado e empilhado trocados). Curso 8.2, gráfico de barras: agrupado = subcategorias lado a lado; empilhado = partes de um total; pegadinha do curso: empilhado quando se quer comparar as partes entre si. O item inverte os papéis (redação da v1.1, R-5C1: sem a expressão "lado a lado", que denunciava a troca). Difere do item A5-09 e do par C1 porque estes julgam barras × histograma; este julga as duas variantes do gráfico de barras. |
| 30 | 5C-04 | Lote 5-C — `saida/gcb/GCB_Lote5C_v1_GCB-CPP.md` | P1-8.2 (8.2 Tipos de gráficos (histograma, linha, barra, dispersão, box plot)) | C | não | C — 8.2 — sem armadilha (ancoragem). Curso 8.2, gráfico de barras: vertical (colunas) ou horizontal, esta melhor para rótulos longos. O item usa "preferível", equivalente ao "melhor" do curso, e não proíbe a vertical. |
| 31 | 5C-05 | Lote 5-C — `saida/gcb/GCB_Lote5C_v1_GCB-CPP.md` | P1-8.2 (8.2 Tipos de gráficos (histograma, linha, barra, dispersão, box plot)) | C | não | C — 8.2 — sem armadilha (ancoragem). Curso 8.2, gráfico de dispersão: o gráfico de bolhas acrescenta uma terceira variável no tamanho. Difere do item A5-11 porque aquele julga correlação × causalidade; este julga o que o gráfico de bolhas acrescenta. |
| 32 | A5-11 | Lote 5 — `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` | P1-8.2 (8.2 Tipos de gráficos (histograma, linha, barra, dispersão, box plot)) | C | sim | C — [TS] — convertido — 8.2 — IC (tentação: alinhamento quase perfeito → "prova causa" → marcar E). Dispersão mostra associação; correlação, por mais forte, não comprova causalidade. |
| 33 | A5-10 | Lote 5 — `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` | P1-8.2 (8.2 Tipos de gráficos (histograma, linha, barra, dispersão, box plot)) | E | não | E — novo — 8.2 — AT. Linha pressupõe eixo horizontal ordenado (tempo); ligar categorias sem ordem sugere continuidade inexistente; comparação entre categorias pede gráfico de barras. |
| 34 | A5-09 | Lote 5 — `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` | P1-8.2 (8.2 Tipos de gráficos (histograma, linha, barra, dispersão, box plot)) | C | sim | C — [TS] — v3 (F4) — 8.2 — TC (tentação: quem decorou "barras separadas" como regra marca E). As barras do histograma são contíguas porque as classes são intervalos adjacentes de uma escala numérica; no gráfico de barras, o espaçamento é convenção de desenho; o que distingue os dois é a natureza da variável (curso 8.2; par C1). |
| 35 | 5C-10 | Lote 5-C — `saida/gcb/GCB_Lote5C_v1_GCB-CPP.md` | P1-8.4 (8.4 Storytelling para visualização de dados) | E | não | E — 8.4 — IC (inversão da ordem: a mensagem vem antes da escolha dos gráficos). Curso 8.4, método: entender o contexto; definir a mensagem principal antes de escolher gráficos; depois, escolher a visualização adequada. O item inverte a ordem. Difere do item A5-19 porque aquele julga exploratória × explanatória; este julga a ordem do método. |
| 36 | A5-20 | Lote 5 — `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` | P1-8.4 (8.4 Storytelling para visualização de dados) | C | não | C — (A) — 8.4. Destaque e anotação guiam o olhar do público ao que sustenta a conclusão. |
| 37 | A5-18 | Lote 5 — `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` | P1-8.4 (8.4 Storytelling para visualização de dados) | C | não | C — (A) — 8.4. Definição essencial: dados, visual e narrativa a serviço de uma mensagem. |
| 38 | A5-19 | Lote 5 — `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` | P1-8.4 (8.4 Storytelling para visualização de dados) | E | sim | E — [TS] — (A) — 8.4 — TC (exploratória no lugar de explanatória). O perfil descrito é o da análise explanatória; na exploratória o analista ainda investiga. |
| 39 | 5C-09 | Lote 5-C — `saida/gcb/GCB_Lote5C_v1_GCB-CPP.md` | P1-8.4 (8.4 Storytelling para visualização de dados) | C | não | C — 8.4 — sem armadilha (ancoragem). Curso 8.4, estrutura narrativa: contexto (público e o que está em jogo), conflito ou problema (o que os dados revelam), resolução ou chamada à ação (o que fazer). Difere do item A5-18 porque aquele julga a tríade dados, visual e narrativa; este julga as etapas da estrutura narrativa. |
| 40 | 5C-07 | Lote 5-C — `saida/gcb/GCB_Lote5C_v1_GCB-CPP.md` | P1-8.4 (8.4 Storytelling para visualização de dados) | E | sim | E — [TS] — 8.4 — TC (storytelling e dashboard trocados). Curso 8.4: o storytelling tem uma mensagem central; o dashboard é exploração aberta, com muitos indicadores (par C14). O item inverte as duas caracterizações. Difere dos itens A5-18 e A5-19: A5-18 julga a definição do storytelling; A5-19 troca exploratória e explanatória; este troca storytelling e dashboard. |

## Verificação

- Total de itens: 40 (numeração contínua 1 a 40), todos AUTORAL, todos de P1 (TI e Dados, itens 5 a 8 do edital).
- Gabarito: 20 C e 20 E (50.0% C / 50.0% E). Itens com troca sutil [TS]: 19 de 40.
- Por lote: Lote 4 = 16; Lote 4-C = 4; Lote 5 = 14; Lote 5-C = 6.
- Por subitem do edital (itens, dos quais C):
  - 5.1 Engenharia de prompts: 8 itens (4 C, 4 E)
  - 5.2 Aprendizado supervisionado, não supervisionado e por reforço: 4 itens (2 C, 2 E)
  - 5.3 IA generativa: conceitos, exemplos e casos de uso: 4 itens (2 C, 2 E)
  - 6 Ética e responsabilidade digital no serviço público: 4 itens (2 C, 2 E)
  - 7.1 Conceitos, atributos, métricas, transformação de dados: 4 itens (2 C, 2 E)
  - 8.1 Princípios de visualização de dados: 3 itens (1 C, 2 E)
  - 8.2 Tipos de gráficos (histograma, linha, barra, dispersão, box plot): 7 itens (4 C, 3 E)
  - 8.4 Storytelling para visualização de dados: 6 itens (3 C, 3 E)
  - 8.3 Ferramentas de visualização de dados: 0 itens (os 4 itens do lote, A5-14 a A5-17, são VOLÁTIL; nenhum item apto a simulado final até a reverificação de janeiro/2027).
- Cobertura: 8 dos 9 subitens de P1 5–8 (5.1, 5.2, 5.3, 6, 7.1, 8.1, 8.2, 8.4). Não coberto: 8.3 (ver acima). Em 8.2 estão presentes os cinco gráficos do edital (histograma A5-09; linha A5-10; barra 5C-03 e 5C-04; dispersão A5-11 e 5C-05; box plot A5-12).
- Distribuição (lote × subitem): Lote 4 5.1 = 4; Lote 4 5.2 = 4; Lote 4 5.3 = 4; Lote 4 6 = 4; Lote 4-C 5.1 = 4; Lote 5 7.1 = 4; Lote 5 8.1 = 3; Lote 5 8.2 = 4; Lote 5 8.4 = 3; Lote 5-C 8.2 = 3; Lote 5-C 8.4 = 3.

### Sequência do gabarito (C/E por número)

CCEEECCEECECCCEECECEECECEECEECCCECECCECE — maior corrida de mesma resposta: 3 (embaralhamento por bloco, semente 0)

### Proporção e critérios de seleção

- Equilíbrio C/E: 20 C e 20 E, escolhidos por subitem (cada subitem com ±1 de diferença). Troca sutil: ver contagem acima; os itens de ancoragem (sem [TS]) foram mantidos para não superdimensionar a dificuldade.
- Proporção por subitem: tomaram-se todos os itens elegíveis dos subitens com poucos itens (5.2 sem L4-11: 4; 5.3: 4 de 4 elegíveis; 6: 4; 7.1: 4; 8.1: 3) e uma amostra dos subitens com muitos (5.1: 8 de 16 elegíveis; 8.2: 7 de 12; 8.4: 6 de 7). Resultado: IA (5.1–5.3) 16 itens, ética (6) 4, dados (7.1) 4, visualização (8.1, 8.2, 8.4) 16. Os subitens 5.1 e 8.2/8.4 receberam mais itens por terem mais itens elegíveis e, no caso de 8.2, por exigirem os cinco gráficos do edital.
- Itens de lotes distintos com o mesmo ponto de julgamento ou com pista cruzada não foram combinados (ver exclusões).

### Exclusões com motivo

Inelegíveis (5):

- A5-14 (8.3, gab C): inelegível: marcado VOLÁTIL no d-G do lote e no registro AUTORAL v2 (reverificação 4–8/1/2027; D-REVERIFICACAO-JAN).
- A5-15 (8.3, gab E): inelegível: marcado VOLÁTIL no d-G do lote e no registro AUTORAL v2 (reverificação 4–8/1/2027; D-REVERIFICACAO-JAN).
- A5-16 (8.3, gab C): inelegível: marcado VOLÁTIL no d-G do lote e no registro AUTORAL v2 (reverificação 4–8/1/2027; D-REVERIFICACAO-JAN).
- A5-17 (8.3, gab E): inelegível: marcado VOLÁTIL no d-G do lote e no registro AUTORAL v2 (reverificação 4–8/1/2027; D-REVERIFICACAO-JAN).
- L4-15 (5.3, gab E): inelegível: marcado VOLÁTIL no d-G do lote e no registro AUTORAL v2 (reverificação 4–8/1/2027; D-REVERIFICACAO-JAN).

Elegíveis não selecionados (15):

- 4C-01 (5.1, gab E): elegível, não selecionado: 5.1 já com 8 itens (proporção).
- 4C-03 (5.1, gab C): elegível, não selecionado: 5.1 já com 8 itens; temperatura já julgada em L4-04.
- 4C-04 (5.1, gab E): elegível, não selecionado: 5.1 já com 8 itens; temperatura já julgada em L4-04 (definição de temperatura entregaria L4-04).
- 4C-06 (5.1, gab C): elegível, não selecionado: 5.1 já com 8 itens.
- 4C-09 (5.1, gab C): elegível, não selecionado: pista cruzada com L4-06 (RAG × retreinamento).
- 4C-10 (5.1, gab E): elegível, não selecionado: 5.1 já com 8 itens.
- 5C-01 (8.2, gab C): elegível, não selecionado: 8.2 limitado a 7 itens (histograma já coberto por A5-09).
- 5C-02 (8.2, gab E): elegível, não selecionado: 8.2 limitado a 7 itens (gráfico de linha já coberto por A5-10).
- 5C-06 (8.2, gab C): elegível, não selecionado: 8.2 limitado a 7 itens (box plot já coberto por A5-12).
- 5C-08 (8.4, gab E): elegível, não selecionado: mesmo princípio de A5-20 (dirigir a atenção), conforme o parecer de QA do 5-C.
- A5-08 (8.2, gab E): elegível, não selecionado: 8.2 limitado a 7 itens (histograma já coberto por A5-09).
- A5-13 (8.2, gab C): elegível, não selecionado: 8.2 limitado a 7 itens (box plot já coberto por A5-12).
- L4-02 (5.1, gab E): elegível, não selecionado: define zero-shot no próprio enunciado (pista para 4C-02) e 5.1 já tem 8 itens.
- L4-05 (5.1, gab C): elegível, não selecionado por precaução: a justificativa do lote cita as fontes de fornecedor F1/F2 e a expressão "Sem marca VOLÁTIL" (a marca foi retirada na v3, R9); não há marca VOLÁTIL no item.
- L4-11 (5.2, gab C): elegível, não selecionado por escolha: R2 (L4-11 nunca com TRF6 item 81) não é violada por simulado só AUTORAL, mas o d-G do arquivo ainda traz "gabarito a confirmar contra o GAB_DEFINITIVO" (Despacho 9 / v3.4 pendente de aplicação no arquivo); evita-se copiar texto defasado.

### Regras e falta registrada

- D-QA-PENDENTE: nenhum item com "QA PENDENTE" (conferido nos quatro arquivos canônicos e nos pareceres: Lote 4-C v1.1 e Lote 5-C v1.1 CONFERIDOS; Lotes 4 v3 e 5 v3 CONFERIDOS pela CQFP em 8/10/2026; ratificados pela Presidência em 9/10/2026 conforme D-CANONICOS).
- Nenhum item reprovado: as substituições de 4C-06, 4C-09, 5C-03 e das versões v3 de A5-02 e A5-09 já estão aplicadas nos textos usados.
- VOLÁTIL / REVERIFICAR: nenhum item selecionado traz a marca no registro AUTORAL v2 nem no d-G (L4-15 e A5-14 a A5-17 excluídos).
- L4-11 × TRF6 item 81: L4-11 não entra neste simulado; o banco (TRF6) também não. Regra cumprida.
- FALTA REGISTRADA: o subitem 8.3 (ferramentas de visualização) não tem item apto a simulado final nestes lotes (4 de 4 VOLÁTIL); este simulado cobre 8 dos 9 subitens de P1 5–8. Há 40 itens elegíveis suficientes; a falta é de cobertura, não de quantidade. Reavaliar 8.3 após a reverificação de 4–8/1/2027 (D-REVERIFICACAO-JAN).
- Conferência por script (scratchpad t06/verify.py, rodado sobre os arquivos gravados): 40 enunciados e 40 justificativas idênticos, caractere a caractere, às linhas dos arquivos canônicos; gabarito do mapa = gabarito do d-G = registro AUTORAL v2; subitem do mapa = subitem do registro; numeração 1–40 contínua; 20 C e 20 E; nenhuma ocorrência de VOLÁTIL, REVERIFICAR, PENDENTE ou L4-11 no corpo do simulado; maior corrida de mesma resposta = 3.
- Ajuste T-31 (10/10/2026, gbq-csc): em `simulado_1.md` foram retirados a seção "Verificação (montagem)" (o conteúdo equivalente está na seção "Verificação" deste arquivo) e, do parágrafo de abertura, a frase de montagem; foi acrescentada a linha de aviso de que o simulado não traz itens do subitem 8.3. Nenhum item, ordem, numeração, comando, texto ou gabarito mudou (conferência por script em `saida/simulados/T31_2026-10-10.md`).
- Ressalva de arquivo: o Lote 4 canônico em saida/gcb ainda traz o cabeçalho v3.3; o Despacho 9 (v3.4, correções textuais de curso e do d-G do item 11, nenhum gabarito muda) está pendente de aplicação nesse arquivo. Nenhum item selecionado é afetado (o único d-G afetado é o de L4-11, não usado).
