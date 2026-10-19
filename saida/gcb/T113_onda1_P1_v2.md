# T113_onda1_P1_v2.md — T-113 onda 1 (F1), P1-5.2, L4-R01 a L4-R07 — 2026-10-18 — gerado por gcb-cpp

Despacho: saida/gcb/T113_P1_D1_pos_R1_2026-10-18.md (D1 da GCB depois da R1), seção 2; parecer saida/gcb/QA_T113_P1_R1_2026-10-18_gcb-cqfp.md. Normas: D-REFORCO-2 (regras 1 a 6), D-FONTE-DATA-ANTERIOR, CLAUDE.md (EVIDÊNCIA), regras/proveniencia.md. Base de leitura: pacote v1.11, somente leitura. Nenhum item existente muda. Rótulo: AUTORAL em todos. Aderência: direta nos 7. VOLÁTEIS: 0.

## RESPOSTA AO QA (item a item, antes do texto corrigido)

| ponto do parecer / da D1 | resposta | onde |
|---|---|---|
| L4-R01, APROVADO; aplicar O-1 só no registro | ACATADO. Enunciado, textoBase, gabarito e justificativa idênticos ao v1 (comparação de string por script, python -I). O trecho registrado em proveniência passou a ser o do corpo: "Supervised learning models can make predictions after seeing lots of data with the correct answers and then discovering the connections between the elements in the data that produce the correct answers." Reaberto hoje: 1 ocorrência no corpo (seção "Types of ML Systems"), fora do "Page Summary". | Parte 3 |
| L4-R02, APROVADO | ACATADO. Idêntico ao v1 (string). Glossário reaberto hoje, HTTP 200, trecho literal presente. | Parte 4 |
| L4-R05, APROVADO; ajuste opcional de forma | ACATADO sem o ajuste opcional, conforme D1-6 da GCB. Idêntico ao v1 (string). | Parte 4 |
| 3.3 L4-R03, CORRIGIR (texto exato) | ACATADO. Enunciado e justificativa aplicados literalmente (seção 3.3 do parecer), sem nenhuma outra mudança. Gabarito E, [TS] sim, troca de sujeito. O textoBase continua vazio. | Parte 4 |
| 3.4 L4-R04, CORRIGIR (texto exato) | ACATADO. textoBase, enunciado e justificativa aplicados literalmente (seção 3.4 do parecer). Gabarito E, [TS] sim, situação hipotética. Base registrada: "Reinforcement learning is used to train robots to perform tasks, like walking around a room", no corpo da página, reaberta hoje (1 ocorrência). | Partes 3 e 4 |
| 3.6 L4-R06, REPROVADO (ponto h) | ACATADO. Ponto (h) retirado. O id L4-R06 é reutilizado com ponto novo (D1-3): consulta pública agrupada por semelhança = clustering, e não supervisionado. Gabarito E, [TS] sim, aplicação parlamentar. Texto do v1 descartado. | Partes 1 e 4 |
| 3.7 L4-R07, REPROVADO (ponto e) | ACATADO. Ponto (e) retirado. O id L4-R07 é reutilizado com ponto novo (D1-3): atributos × valor previsto na regressão do preço da casa. Gabarito C, par confundível. Sem a construção "X é classificado como tipo Y" e sem o RLHF, o que afasta o excesso de troca de sujeito, a cópia da pegadinha do curso e a colisão com o L4-R02. Texto do v1 descartado. | Partes 1 e 4 |
| Base obrigatória dos novos (D1, seção 2, item 4) | CUMPRIDA. Página aberta nesta produção, HTTP 200, trecho literal do corpo para os dois (Parte 3). Nenhum item "NÃO ENTREGUE". | Parte 3 |
| Barreiras de gêmeo (D1-3) | CONFERIDAS pela produção, sujeitas à gcb-cqfp. L4-R06 não julga "categorias definidas previamente" (L4-08), participação humana (L4-09), recomendação (BQ-0034) nem a definição de agrupamento (BQ-0013, BQ-0106); julga só o reconhecimento da tarefa no cenário, e a falsidade está só em "supervisionado". L4-R07 não julga "regressão prevê valor numérico" (L4-07, BQ-0104) nem algoritmo; julga qual elemento é atributo e qual é o previsto. Proximidade registrada com a pegadinha P2 do curso 5.2.7 ("clustering é supervisionado"): a pegadinha é a afirmação abstrata; o L4-R06 exige reconhecer a tarefa num cenário em que a palavra clustering não aparece no texto do estudante. | Parte 2.1 |
| Contas (D1-4) | REFEITAS na Parte 2: parte 4 C / 3 E (57% de C); folha de 30 com 16 C / 14 E; troca de sujeito 9/30 (30%, no teto); VOLÁTEIS 0. | Parte 2 |
| Observação | O campo "url" dos 7 itens do bloco json passou a apontar para este arquivo (v2), como manda a forma do item; não é texto do estudante. | Bloco json |

## PARTE 1/4 — Mapa

| id | folha | ponto de julgamento | formato | gabarito | base | VOLÁTIL | QA |
|---|---|---|---|---|---|---|---|
| L4-R01 | P1-5.2 | indexação de proposições por tema, com a indexação histórica como rótulo, é classificação supervisionada | aplicação parlamentar | C | Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026 (aberta hoje, HTTP 200; trecho do corpo) | n | QA: APROVADO (gcb-cqfp, R1, 18/10/2026) |
| L4-R02 | P1-5.2 | avaliações humanas (aprovação/reprovação) usadas como feedback para ajustar respostas futuras = RLHF aplicado | aplicação parlamentar | C | Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 18/10/2026 (aberta hoje, HTTP 200) | n | QA: APROVADO (gcb-cqfp, R1, 18/10/2026) |
| L4-R03 | P1-5.2 | política (policy) no reforço = estratégia para acumular recompensas, e não a recompensa | troca de sujeito | E | Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026 (aberta hoje, HTTP 200) | n | QA: CORRIGIR (R1); texto exato aplicado no v2 |
| L4-R04 | P1-5.2 | exemplo canônico do reforço (robô que aprende a caminhar) reconhecido em cenário concreto | situação hipotética | E | Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026 (aberta hoje, HTTP 200) | n | QA: CORRIGIR (R1); texto exato aplicado no v2 |
| L4-R05 | P1-5.2 | classificação binária × multiclasse (critério: número de classes da saída) | par confundível | C | Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026 (aberta hoje, HTTP 200) | n | QA: APROVADO (gcb-cqfp, R1, 18/10/2026) |
| L4-R06 | P1-5.2 | agrupar por semelhança as contribuições de uma consulta pública, sem temas definidos antes, é clustering (não supervisionado); os grupos são descobertos pelo modelo e podem ser nomeados depois pelo servidor; o item afirma que é aprendizado supervisionado | aplicação parlamentar | E | Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026 (aberta hoje, HTTP 200; trecho do corpo) | n | QA PENDENTE (substituto, R2) |
| L4-R07 | P1-5.2 | atributos (features) × valor previsto na regressão do preço futuro de uma casa: metragem, CEP, quartos, banheiros e juros são atributos de entrada; o preço é o valor previsto | par confundível | C | Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026 (aberta hoje, HTTP 200; trecho do corpo) | n | QA PENDENTE (substituto, R2) |

Pontos: L4-R01 = (b); L4-R02 = (f), só a parte da avaliação acumulada como feedback; L4-R03 = (c); L4-R04 = (i); L4-R05 = (a); L4-R06 e L4-R07 = pontos novos da D1 da GCB pós-R1 (D1-3), no curso 5.2.3 e 5.2.6 (R06) e 5.2.1 e 5.2.2 (R07). Retirados: (h) e (e), por motivo da QA; (d) e (g), por falta de base na página.

Gabarito fixado: 4 C (L4-R01, L4-R02, L4-R05, L4-R07) e 3 E (L4-R03, L4-R04, L4-R06). [TS]: 3 (L4-R03, L4-R04, L4-R06). O L4-R07 tem gabarito C e não é [TS].

FIM DA PARTE 1/4

## PARTE 2/4 — Os 23 pontos ocupados, os 7 pontos e as contas da folha

### 2.1 Pontos dos 23 itens da folha (inalterados em relação ao v1)

| id | gab | ponto de julgamento ocupado | formato |
|---|---|---|---|
| BQ-0013 | C | agrupamento como método não supervisionado que organiza por similaridade em clusters | definição |
| BQ-0018 | E | Naive Bayes atribuído ao aprendizado por reforço (algoritmo de classificação, não reforço) | troca de sujeito |
| BQ-0019 | E | KNN supervisionado negado para classificação (prevê só valores numéricos) | troca de sujeito |
| BQ-0020 | C | SVM como algoritmo supervisionado para classificação ou regressão | definição |
| BQ-0026 | C | supervisionado ajusta função de mapeamento a partir de exemplos rotulados para generalizar | definição |
| BQ-0027 | C | PCA em contexto não supervisionado dispensa rótulos e extrai componentes de maior variância | definição |
| BQ-0034 | C | clustering em sistemas de recomendação de conteúdo | definição |
| BQ-0041 | E | redução de dimensionalidade como tarefa não supervisionada (negada a preservação da integridade dos dados) | troca de sujeito |
| BQ-0042 | E | Naive Bayes e SVM atribuídos tanto à classificação quanto à regressão | troca de sujeito |
| BQ-0043 | E | classificação situada no grupo não supervisionado | troca de sujeito |
| BQ-0049 | E | regressão linear como algoritmo indicado para decisão de aprovar ou negar (problema de classificação) | situação hipotética |
| BQ-0050 | E | não supervisionado como escolha para aprovar ou negar sem dados rotulados | situação hipotética |
| BQ-0051 | C | identificação do caso de aprovar ou negar como problema de classificação | situação hipotética |
| BQ-0101 | E | sistema "não supervisionado" treinado com dados classificados manualmente | troca de sujeito |
| BQ-0103 | C | supervisionado usa conjunto de treinamento para ensinar a saída desejada | definição |
| BQ-0104 | E | regressão como tipo de aprendizado não supervisionado | troca de sujeito |
| BQ-0105 | C | Naive Bayes como algoritmo supervisionado de classificação (independência condicional, teorema de Bayes) | definição |
| BQ-0106 | C | clustering agrupa dados não rotulados; tipos de algoritmo de cluster | definição |
| L4-07 | C | regressão = valor numérico (exemplo da chuva em milímetros) | definição |
| L4-08 | E | clustering com categorias definidas previamente (descrição da classificação) | par confundível |
| L4-09 | E | não supervisionado ≠ sem participação humana | troca de sujeito |
| L4-10 | C | reforço: recompensas e penalidades, sem rótulo da ação correta por entrada | definição |
| L4-11 | C | IA generativa: pré-treino sem rótulos e ajuste supervisionado ou por reforço | definição |

Pontos que não podem voltar (D1): regressão = valor numérico; clustering sem categorias prévias; não supervisionado ≠ sem humano; reforço sem rótulo por entrada; pré-treino generativo sem rótulos + ajuste; classificação não é não supervisionada; Naive Bayes, SVM, KNN, PCA e regressão linear como algoritmos. Nenhum dos 7 cai nesses pontos.

Notas de deduplicação (só aqui, nunca nas justificativas): L4-R01 não repete BQ-0051 nem BQ-0034. L4-R03 e L4-R04 não repetem L4-10 (o L4-10 julga a ausência de rótulo por entrada; o L4-R03 julga o conceito de política; o L4-R04 julga o reconhecimento de um cenário, e a falsidade está em trocar reforço por não supervisionado, sem a ideia de resposta correta por movimento). L4-R05 não repete nenhum dos 23. L4-R06 não repete L4-08, L4-09, BQ-0034, BQ-0013 nem BQ-0106: julga reconhecer a tarefa num cenário. L4-R07 não repete L4-07, BQ-0104 nem os algoritmos: julga qual elemento é entrada e qual é a saída prevista. O RLHF fica só no L4-R02, que não tem mais par na parte.

### 2.2 Tabela de pontos (os 23 + os 7 = 30)

Os 23 estão na tabela 2.1. Os 7 desta parte:

| id | gab | ponto de julgamento | formato |
|---|---|---|---|
| L4-R01 | C | indexação de proposições por tema, com a indexação histórica como rótulo, é classificação supervisionada | aplicação parlamentar |
| L4-R02 | C | avaliações humanas usadas como feedback para ajustar respostas futuras = RLHF aplicado | aplicação parlamentar |
| L4-R03 | E | política no reforço = estratégia, e não a recompensa | troca de sujeito |
| L4-R04 | E | robô que aprende a caminhar = exemplo de reforço reconhecido em cenário | situação hipotética |
| L4-R05 | C | binária × multiclasse (número de classes da saída) | par confundível |
| L4-R06 | E | consulta pública agrupada por semelhança sem temas prévios = clustering, não supervisionado | aplicação parlamentar |
| L4-R07 | C | atributos de entrada × valor previsto na regressão do preço da casa | par confundível |

### 2.3 Contas de formato (folha de 30 itens; teto de 30% sobre a folha final = 9)

| formato | já na folha (23) | novos | total (30) | teto 9 |
|---|--:|--:|--:|---|
| definição | 11 | 0 | 11 | excesso legado, não imputado; nenhum item novo entra |
| troca de sujeito | 8 | 1 (L4-R03) | 9 | no teto (30,0%) |
| situação hipotética | 3 | 1 (L4-R04) | 4 | ok |
| par confundível | 1 | 2 (L4-R05, L4-R07) | 3 | ok |
| aplicação parlamentar | 0 | 3 (L4-R01, L4-R02, L4-R06) | 3 | ok |
| número ou prazo | 0 | 0 | 0 | ok |
| soma | 23 | 7 | 30 | |

Se um substituto não passar na R2, vale a D1-5 da GCB. L4-R07 sozinho: difere-se também o L4-R03; parte com 5 itens (3 C / 2 E), folha de 28 com troca de sujeito 8/28 (28,6%), situação hipotética 4, par confundível 2, aplicação parlamentar 3, definição 11. L4-R06 falhando: a escolha vai à GBQ por gatilho D.

### 2.4 Gabarito da folha

Atual: 12 C (BQ-0013, 0020, 0026, 0027, 0034, 0051, 0103, 0105, 0106, L4-07, L4-10, L4-11) e 11 E. Novos: 4 C e 3 E (57% de C na parte, dentro de 40% a 60%). Folha: 16 C / 14 E. VOLÁTEIS: 0. [TS] da parte: 3 (L4-R03, L4-R04, L4-R06).

FIM DA PARTE 2/4

## PARTE 3/4 — Verificação de rede (18/10/2026)

Comando (por página): `curl -sL -m 40 -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36" -o <arquivo> -w "%{http_code} %{size_download}" <URL>`; busca textual no HTML sem scripts e estilos, entidades decodificadas (python -I).

| página | URL | HTTP | bytes | "Last updated" | resultado |
|---|---|--:|--:|---|---|
| Google for Developers, "Introduction to ML: What is Machine Learning?" | https://developers.google.com/machine-learning/intro-to-ml/what-is-ml | 200 | 106.621 | 2026-01-27 UTC | aberta em 18/10/2026 nesta produção; trechos literais do corpo presentes (abaixo), cada um com 1 ocorrência |
| Google for Developers, "Machine Learning Glossary: Generative AI" | https://developers.google.com/machine-learning/glossary/generative | 200 | 164.810 | 2026-04-13 UTC | aberta em 18/10/2026; trecho literal do RLHF presente |

Trecho literal por item (corpo da página, nenhum do quadro "Page Summary"; verificado em 18/10/2026):

- L4-R01 (O-1 aplicado): "Supervised learning models can make predictions after seeing lots of data with the correct answers and then discovering the connections between the elements in the data that produce the correct answers."
- L4-R02: "Using feedback from human raters to improve the quality of a model's responses." e "The system can then adjust its future responses based on that feedback." (glossário).
- L4-R03: "A reinforcement learning system generates a policy that defines the best strategy for getting the most rewards." (e "Reinforcement learning models make predictions by getting rewards or penalties based on actions performed within an environment.")
- L4-R04: "Reinforcement learning is used to train robots to perform tasks, like walking around a room"
- L4-R05: "Binary classification models output a value from a class that contains only two values, for example, a model that outputs either rain or no rain. Multiclass classification models output a value from a class that contains more than two values"
- L4-R06: "Clustering differs from classification because the categories aren't defined by you." e "You might then attempt to name those clusters based on your understanding of the dataset." (seção "Unsupervised learning", que abre com "An unsupervised learning model aims to identify meaningful patterns in a dataset.")
- L4-R07: linha da tabela de modelos de regressão: "Future house price | Square footage, zip code, number of bedrooms and bathrooms, lot size, mortgage interest rate, property tax rate, construction costs, and number of homes for sale in the area. | The price of the home." (colunas "Possible input data" e "Numeric prediction"). Os cinco elementos do item estão na coluna de dados de entrada; o preço está na coluna da previsão. Tabela no corpo, seção "Regression".

Observação sobre o termo "atributos": a página usa "input data" (dados de entrada); "atributos ou features" é vocabulário do curso (5.2.1). A justificativa do L4-R07 usa "dados de entrada" e "valor previsto", que a página sustenta.

FIM DA PARTE 3/4

## PARTE 4/4 — Os 7 itens (texto do estudante e gabarito comentado)

### L4-R01 (P1-5.2). AUTORAL. Julgue o item.
Uma unidade da Câmara pretende treinar um modelo para indexar automaticamente proposições por tema, usando como exemplos de treinamento a indexação já feita por servidores em anos anteriores.
Nessa situação, o modelo será treinado por aprendizado supervisionado, em tarefa de classificação, porque a indexação anterior funciona como o rótulo de cada proposição.

Gabarito: C
Justificativa (duas linhas): Os exemplos já indexados trazem a resposta correta (o tema) para cada proposição, e prever uma categoria é classificação, tarefa do aprendizado supervisionado. Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026.
[TS]: não. VOLÁTIL: não. Aderência: direta. Ponto de julgamento: indexação de proposições por tema, com a indexação histórica como rótulo, é classificação supervisionada. Formato: aplicação parlamentar. QA: PENDENTE.
Proveniência: Google for Developers, "Introduction to ML: What is Machine Learning?", https://developers.google.com/machine-learning/intro-to-ml/what-is-ml, verificado em 18/10/2026 (aberta hoje, HTTP 200).

### L4-R02 (P1-5.2). AUTORAL. Julgue o item.
Revisores do Derep (antigo DETAQ) avaliam, com aprovação ou reprovação, as minutas geradas por um assistente de redação baseado em IA generativa.
Se a equipe técnica usar essas avaliações como feedback humano para ajustar as respostas futuras do modelo, a técnica empregada corresponde ao aprendizado por reforço com feedback humano (RLHF).

Gabarito: C
Justificativa (duas linhas): O glossário define o RLHF como o uso de feedback de avaliadores humanos para melhorar as respostas do modelo, que passa a ajustar suas respostas futuras com base nesse retorno. O item descreve esse uso. Fonte: Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 18/10/2026.
[TS]: não. VOLÁTIL: não. Aderência: direta. Ponto de julgamento: avaliações humanas (aprovação/reprovação) usadas como feedback para ajustar respostas futuras = RLHF aplicado. Formato: aplicação parlamentar. QA: PENDENTE.
Proveniência: Google for Developers, "Machine Learning Glossary: Generative AI", https://developers.google.com/machine-learning/glossary/generative, verificado em 18/10/2026 (aberta hoje, HTTP 200).

### L4-R03 (P1-5.2). AUTORAL. Julgue o item.
No aprendizado por reforço, denomina-se política a recompensa que o agente recebe em razão das ações que executa no ambiente.

Gabarito: E
Justificativa (duas linhas): Armadilha: troca de conceito. A recompensa é o sinal que o agente recebe pelas ações que executa; a política é a estratégia que o sistema gera para obter o máximo de recompensas. Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026.
[TS]: sim. VOLÁTIL: não. Aderência: direta. Ponto de julgamento: política (policy) no reforço = estratégia para acumular recompensas, e não a recompensa. Formato: troca de sujeito. QA: CORRIGIR (R1); texto exato aplicado no v2.
Proveniência: Google for Developers, "Introduction to ML: What is Machine Learning?", https://developers.google.com/machine-learning/intro-to-ml/what-is-ml, verificado em 18/10/2026 (aberta hoje, HTTP 200; "Last updated 2026-01-27 UTC").

### L4-R04 (P1-5.2). AUTORAL. Julgue o item.
Um laboratório treina um robô para aprender a caminhar por uma sala, por tentativa e erro, em interação com o ambiente.
Nessa situação, o treinamento descrito constitui exemplo de aprendizado não supervisionado.

Gabarito: E
Justificativa (duas linhas): Armadilha: troca de tipo de aprendizado. Treinar robôs para caminhar por uma sala, por tentativa e erro em interação com o ambiente, é exemplo de aprendizado por reforço, e não de aprendizado não supervisionado, que busca padrões em dados sem rótulos. Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026.
[TS]: sim. VOLÁTIL: não. Aderência: direta. Ponto de julgamento: exemplo canônico do reforço (robô que aprende a caminhar) reconhecido em cenário concreto. Formato: situação hipotética. QA: CORRIGIR (R1); texto exato aplicado no v2.
Proveniência: Google for Developers, "Introduction to ML: What is Machine Learning?", https://developers.google.com/machine-learning/intro-to-ml/what-is-ml, verificado em 18/10/2026 (aberta hoje, HTTP 200; "Last updated 2026-01-27 UTC").

### L4-R05 (P1-5.2). AUTORAL. Julgue o item.
Um modelo de classificação cuja saída é apenas uma entre duas classes, como "chuva" ou "sem chuva", é denominado de classificação binária; se admitir mais de duas classes, é de classificação multiclasse.

Gabarito: C
Justificativa (duas linhas): O critério é o número de classes na saída: duas, binária; mais de duas, multiclasse. Os dois tipos são classificação, tarefa supervisionada. Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026.
[TS]: não. VOLÁTIL: não. Aderência: direta. Ponto de julgamento: classificação binária × multiclasse (critério: número de classes da saída). Formato: par confundível. QA: PENDENTE.
Proveniência: Google for Developers, "Introduction to ML: What is Machine Learning?", https://developers.google.com/machine-learning/intro-to-ml/what-is-ml, verificado em 18/10/2026 (aberta hoje, HTTP 200).

### L4-R06 (P1-5.2). AUTORAL. Julgue o item.
Um órgão da Câmara recebeu cerca de 40 mil contribuições escritas em uma consulta pública e pretende agrupá-las por semelhança de conteúdo, sem temas definidos antes, para descobrir os assuntos mais citados.
Nessa situação, a tarefa descrita configura aprendizado supervisionado.

Gabarito: E
Justificativa (duas linhas): Armadilha: troca de tipo de aprendizado. Agrupar por semelhança dados sem resposta correta é clustering, técnica do aprendizado não supervisionado: os grupos são descobertos pelo modelo, e o servidor pode nomeá-los depois. Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026.
[TS]: sim. VOLÁTIL: não. Aderência: direta. Ponto de julgamento: agrupar por semelhança as contribuições de uma consulta pública, sem temas definidos antes, é clustering (não supervisionado); o item afirma que é aprendizado supervisionado. Formato: aplicação parlamentar. QA: PENDENTE (substituto, R2).
Proveniência: Google for Developers, "Introduction to ML: What is Machine Learning?", https://developers.google.com/machine-learning/intro-to-ml/what-is-ml, verificado em 18/10/2026 (aberta hoje, HTTP 200; "Last updated 2026-01-27 UTC").

### L4-R07 (P1-5.2). AUTORAL. Julgue o item.
Uma equipe constrói um modelo de regressão para estimar o preço futuro de uma casa.
Nesse modelo, a metragem, o CEP, o número de quartos e de banheiros e a taxa de juros do financiamento são atributos de entrada, e o preço da casa é o valor previsto.

Gabarito: C
Justificativa (duas linhas): Os atributos são os dados de entrada do modelo (metragem, CEP, quartos, banheiros e juros); o preço da casa é o resultado que o modelo devolve, isto é, o valor previsto. Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026.
[TS]: não. VOLÁTIL: não. Aderência: direta. Ponto de julgamento: atributos (features) × valor previsto na regressão do preço futuro de uma casa. Formato: par confundível. QA: PENDENTE (substituto, R2).
Proveniência: Google for Developers, "Introduction to ML: What is Machine Learning?", https://developers.google.com/machine-learning/intro-to-ml/what-is-ml, verificado em 18/10/2026 (aberta hoje, HTTP 200; "Last updated 2026-01-27 UTC").

### Tabela de proveniência
| fonte | URL oficial | data de verificação | itens |
|---|---|---|---|
| Google for Developers, "Introduction to ML: What is Machine Learning?" | https://developers.google.com/machine-learning/intro-to-ml/what-is-ml | 18/10/2026 (HTTP 200; "Last updated 2026-01-27 UTC") | L4-R01, L4-R03, L4-R04, L4-R05, L4-R06, L4-R07 |
| Google for Developers, "Machine Learning Glossary: Generative AI" | https://developers.google.com/machine-learning/glossary/generative | 18/10/2026 (HTTP 200; "Last updated 2026-04-13 UTC") | L4-R02 |

### Contagem
Itens: 7. Gabarito: C 4 / E 3. [TS]: 3. VOLÁTEIS: 0. Folha P1-5.2: 23 + 7 = 30 (16 C / 14 E).

### Varredura (regra 0.7)
Regex das categorias da ordem C (marca de lote, ids de item, códigos de par e de fonte, etiquetas [V…]/[NORMATIVO…], prefixos TC/IC/GI/AT, "Difere do item", QA, produção, errata, versão, instruções internas) sobre textoBase, enunciado e justificativa dos 7 itens: zero ocorrências (script próprio, python -I). Comparação de string: L4-R01, L4-R02 e L4-R05 idênticos ao v1 em textoBase, enunciado, gabarito e justificativa. As páginas aparecem por extenso, com "verificado em 18/10/2026".

FIM DA PARTE 4/4

## Bloco json (7 itens)
```json
[
 {
  "id": "L4-R01",
  "rotulo": "AUTORAL",
  "certame": "Projeto Câmara 2026",
  "cargo": "Lote 4",
  "ano": 2026,
  "numero": 1,
  "comando": "Julgue o item.",
  "textoBase": "Uma unidade da Câmara pretende treinar um modelo para indexar automaticamente proposições por tema, usando como exemplos de treinamento a indexação já feita por servidores em anos anteriores.",
  "enunciado": "Nessa situação, o modelo será treinado por aprendizado supervisionado, em tarefa de classificação, porque a indexação anterior funciona como o rótulo de cada proposição.",
  "gabarito": "C",
  "justificativa": "Os exemplos já indexados trazem a resposta correta (o tema) para cada proposição, e prever uma categoria é classificação, tarefa do aprendizado supervisionado. Fonte: Google for Developers, \"Introduction to ML: What is Machine Learning?\", verificado em 18/10/2026.",
  "itemEdital": "P1-5.2",
  "aderencia": "direta",
  "url": "saida/gcb/T113_onda1_P1_v2.md"
 },
 {
  "id": "L4-R02",
  "rotulo": "AUTORAL",
  "certame": "Projeto Câmara 2026",
  "cargo": "Lote 4",
  "ano": 2026,
  "numero": 2,
  "comando": "Julgue o item.",
  "textoBase": "Revisores do Derep (antigo DETAQ) avaliam, com aprovação ou reprovação, as minutas geradas por um assistente de redação baseado em IA generativa.",
  "enunciado": "Se a equipe técnica usar essas avaliações como feedback humano para ajustar as respostas futuras do modelo, a técnica empregada corresponde ao aprendizado por reforço com feedback humano (RLHF).",
  "gabarito": "C",
  "justificativa": "O glossário define o RLHF como o uso de feedback de avaliadores humanos para melhorar as respostas do modelo, que passa a ajustar suas respostas futuras com base nesse retorno. O item descreve esse uso. Fonte: Google for Developers, \"Machine Learning Glossary: Generative AI\", verificado em 18/10/2026.",
  "itemEdital": "P1-5.2",
  "aderencia": "direta",
  "url": "saida/gcb/T113_onda1_P1_v2.md"
 },
 {
  "id": "L4-R03",
  "rotulo": "AUTORAL",
  "certame": "Projeto Câmara 2026",
  "cargo": "Lote 4",
  "ano": 2026,
  "numero": 3,
  "comando": "Julgue o item.",
  "textoBase": "",
  "enunciado": "No aprendizado por reforço, denomina-se política a recompensa que o agente recebe em razão das ações que executa no ambiente.",
  "gabarito": "E",
  "justificativa": "Armadilha: troca de conceito. A recompensa é o sinal que o agente recebe pelas ações que executa; a política é a estratégia que o sistema gera para obter o máximo de recompensas. Fonte: Google for Developers, \"Introduction to ML: What is Machine Learning?\", verificado em 18/10/2026.",
  "itemEdital": "P1-5.2",
  "aderencia": "direta",
  "url": "saida/gcb/T113_onda1_P1_v2.md"
 },
 {
  "id": "L4-R04",
  "rotulo": "AUTORAL",
  "certame": "Projeto Câmara 2026",
  "cargo": "Lote 4",
  "ano": 2026,
  "numero": 4,
  "comando": "Julgue o item.",
  "textoBase": "Um laboratório treina um robô para aprender a caminhar por uma sala, por tentativa e erro, em interação com o ambiente.",
  "enunciado": "Nessa situação, o treinamento descrito constitui exemplo de aprendizado não supervisionado.",
  "gabarito": "E",
  "justificativa": "Armadilha: troca de tipo de aprendizado. Treinar robôs para caminhar por uma sala, por tentativa e erro em interação com o ambiente, é exemplo de aprendizado por reforço, e não de aprendizado não supervisionado, que busca padrões em dados sem rótulos. Fonte: Google for Developers, \"Introduction to ML: What is Machine Learning?\", verificado em 18/10/2026.",
  "itemEdital": "P1-5.2",
  "aderencia": "direta",
  "url": "saida/gcb/T113_onda1_P1_v2.md"
 },
 {
  "id": "L4-R05",
  "rotulo": "AUTORAL",
  "certame": "Projeto Câmara 2026",
  "cargo": "Lote 4",
  "ano": 2026,
  "numero": 5,
  "comando": "Julgue o item.",
  "textoBase": "",
  "enunciado": "Um modelo de classificação cuja saída é apenas uma entre duas classes, como \"chuva\" ou \"sem chuva\", é denominado de classificação binária; se admitir mais de duas classes, é de classificação multiclasse.",
  "gabarito": "C",
  "justificativa": "O critério é o número de classes na saída: duas, binária; mais de duas, multiclasse. Os dois tipos são classificação, tarefa supervisionada. Fonte: Google for Developers, \"Introduction to ML: What is Machine Learning?\", verificado em 18/10/2026.",
  "itemEdital": "P1-5.2",
  "aderencia": "direta",
  "url": "saida/gcb/T113_onda1_P1_v2.md"
 },
 {
  "id": "L4-R06",
  "rotulo": "AUTORAL",
  "certame": "Projeto Câmara 2026",
  "cargo": "Lote 4",
  "ano": 2026,
  "numero": 6,
  "comando": "Julgue o item.",
  "textoBase": "Um órgão da Câmara recebeu cerca de 40 mil contribuições escritas em uma consulta pública e pretende agrupá-las por semelhança de conteúdo, sem temas definidos antes, para descobrir os assuntos mais citados.",
  "enunciado": "Nessa situação, a tarefa descrita configura aprendizado supervisionado.",
  "gabarito": "E",
  "justificativa": "Armadilha: troca de tipo de aprendizado. Agrupar por semelhança dados sem resposta correta é clustering, técnica do aprendizado não supervisionado: os grupos são descobertos pelo modelo, e o servidor pode nomeá-los depois. Fonte: Google for Developers, \"Introduction to ML: What is Machine Learning?\", verificado em 18/10/2026.",
  "itemEdital": "P1-5.2",
  "aderencia": "direta",
  "url": "saida/gcb/T113_onda1_P1_v2.md"
 },
 {
  "id": "L4-R07",
  "rotulo": "AUTORAL",
  "certame": "Projeto Câmara 2026",
  "cargo": "Lote 4",
  "ano": 2026,
  "numero": 7,
  "comando": "Julgue o item.",
  "textoBase": "Uma equipe constrói um modelo de regressão para estimar o preço futuro de uma casa.",
  "enunciado": "Nesse modelo, a metragem, o CEP, o número de quartos e de banheiros e a taxa de juros do financiamento são atributos de entrada, e o preço da casa é o valor previsto.",
  "gabarito": "C",
  "justificativa": "Os atributos são os dados de entrada do modelo (metragem, CEP, quartos, banheiros e juros); o preço da casa é o resultado que o modelo devolve, isto é, o valor previsto. Fonte: Google for Developers, \"Introduction to ML: What is Machine Learning?\", verificado em 18/10/2026.",
  "itemEdital": "P1-5.2",
  "aderencia": "direta",
  "url": "saida/gcb/T113_onda1_P1_v2.md"
 }
]
```
FIM DO LOTE
