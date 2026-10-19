# T113_onda1_P1_v1.md — T-113 onda 1 (F1), P1-5.2, L4-R01 a L4-R07 — 2026-10-18 — gerado por gcb-cpp

Despacho: saida/gcb/V15_BAEF_D1_GCB_2026-10-18.md, seção 5, e saida/pacote/V15_BAE_D1_GBQ_2026-10-18.md, seção 4. Base de leitura: pacote v1.11 (saida/pacote/gerador_v1_11/out/pacote.json), somente leitura; sem duplicata do enunciado de nenhum dos 560 itens (busca por termos-chave: multiclasse, binária, política, AlphaGo, robô, RLHF, feedback, indexação, quatro categorias; as ocorrências de "política" e "indexa" são de outros tópicos). Nenhum item existente muda. Rótulo de todos os itens: AUTORAL. Aderência: direta nos 7. VOLÁTEIS: 0.

## PARTE 1/4 — Mapa

| id | folha | ponto de julgamento | formato | gabarito | base | VOLÁTIL | QA |
|---|---|---|---|---|---|---|---|
| L4-R01 | P1-5.2 | indexação de proposições por tema, com a indexação histórica como rótulo, é classificação supervisionada | aplicação parlamentar | C | Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026 (aberta hoje, HTTP 200, trecho literal presente) | n | QA PENDENTE |
| L4-R02 | P1-5.2 | avaliações humanas (aprovação/reprovação) usadas como feedback para ajustar respostas futuras = RLHF aplicado | aplicação parlamentar | C | Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 18/10/2026 (aberta hoje, HTTP 200, trecho literal presente) | n | QA PENDENTE |
| L4-R03 | P1-5.2 | política (policy) no reforço = estratégia para acumular recompensas, e não a recompensa | troca de sujeito | E | Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026 (aberta hoje, HTTP 200, trecho literal presente) | n | QA PENDENTE |
| L4-R04 | P1-5.2 | exemplo canônico do reforço (robô que aprende a caminhar) reconhecido em cenário concreto | situação hipotética | E | Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026 (aberta hoje, HTTP 200, trecho literal presente) | n | QA PENDENTE |
| L4-R05 | P1-5.2 | classificação binária × multiclasse (critério: número de classes da saída) | par confundível | C | Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026 (aberta hoje, HTTP 200, trecho literal presente) | n | QA PENDENTE |
| L4-R06 | P1-5.2 | classificação do Google dos sistemas de ML por forma de aprender: quatro categorias, com a IA generativa | número ou prazo | E | Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026 (aberta hoje, HTTP 200, trecho literal presente) | n | QA PENDENTE |
| L4-R07 | P1-5.2 | enquadramento do RLHF: reforço com feedback humano, e não não supervisionado | par confundível | E | Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 18/10/2026 (aberta hoje, HTTP 200, trecho literal presente) | n | QA PENDENTE |

Pontos escolhidos no cardápio da D1: L4-R01 = (b); L4-R02 = (f), só na parte da avaliação acumulada como feedback para ajuste (a parte "sem aprendizado em tempo real a cada clique" não é julgada: a página do glossário não a diz e a base do item é a página); L4-R03 = (c); L4-R04 = (i); L4-R05 = (a); L4-R06 = (h); L4-R07 = (e). Nenhum ponto fora do cardápio. Não usados: (d), recompensa atrasada (a ideia não consta da página aberta, só do curso, o que não serve de base) e (g), padrões em vez de regras programadas (a página não o diz nesses termos).

Distinção entre L4-R02 e L4-R07 (ambos citam o RLHF): L4-R02 julga a aplicação (feedback de revisores usado para ajustar respostas futuras); L4-R07 julga o enquadramento (reforço, e não não supervisionado). Se a gcb-cqfp os considerar gêmeos, um deles sai, e o saldo fica para a onda seguinte com o mesmo id.

Gabarito fixado: 3 C (L4-R01, L4-R02, L4-R05) e 4 E (L4-R03, L4-R04, L4-R06, L4-R07). Com os 12 C e 11 E da folha atual, P1-5.2 fecha em 15 C / 15 E. [TS]: 4 (L4-R03, L4-R04, L4-R06, L4-R07).

FIM DA PARTE 1/4

## PARTE 2/4 — Os 23 pontos ocupados e as contas da folha

### 2.1 Pontos dos 23 itens da folha (um por id; formato classificado pela gcb-cpp)

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

Pontos que não podem voltar (D1): regressão = valor numérico; clustering sem categorias prévias; não supervisionado ≠ sem humano; reforço sem rótulo por entrada; pré-treino generativo sem rótulos + ajuste; classificação não é não supervisionada; Naive Bayes, SVM, KNN, PCA e regressão linear como algoritmos. Nenhum dos 7 novos cai nesses pontos.

Notas de deduplicação (só aqui, nunca nas justificativas): L4-R01 não repete BQ-0051 (aquele identifica a tarefa de aprovar ou negar como classificação; este julga a indexação histórica como rótulo, isto é, o caráter supervisionado) nem BQ-0034 (clustering em recomendação). L4-R03 e L4-R04 não repetem L4-10: o L4-10 julga a ausência de rótulo por entrada; o L4-R03 julga o conceito de política e o L4-R04 julga o reconhecimento de um cenário. L4-R05 não repete nenhum dos 23 (binária × multiclasse não aparece em nenhum). L4-R06 e L4-R07 não têm gêmeo na folha.

### 2.2 Contas de formato (folha com 30 itens)

| formato | já na folha (23) | novos | total (30) | teto 9 |
|---|--:|--:|--:|---|
| definição | 11 | 0 | 11 | excesso legado, não imputado; nenhum item novo entra |
| troca de sujeito | 8 | 1 (L4-R03) | 9 | no teto |
| situação hipotética | 3 | 1 (L4-R04) | 4 | ok |
| par confundível | 1 | 2 (L4-R05, L4-R07) | 3 | ok |
| aplicação parlamentar | 0 | 2 (L4-R01, L4-R02) | 2 | ok |
| número ou prazo | 0 | 1 (L4-R06) | 1 | ok |
| soma | 23 | 7 | 30 | |

A distribuição sugerida (2 aplicação parlamentar, 1 situação hipotética, 2 troca de sujeito, 1 definição, 1 par confundível) foi ajustada: definição já está em 11 e troca de sujeito em 8, de modo que só 1 troca de sujeito cabe sem passar de 9 e nenhuma definição entra; as vagas foram para par confundível (+2 no total), situação hipotética (+1) e número ou prazo (+1). Atenção da gcb-cqfp e da Gerência: com a classificação acima, definição fica em 11 de 30, acima de 9, mas é excesso legado (regra 6 da D1, não imputado). Se a Gerência reclassificar algum dos 11 (por exemplo, BQ-0034 como aplicação), a conta se resolve sem mudar os 7.

### 2.3 Gabarito da folha

Atual: 12 C (BQ-0013, 0020, 0026, 0027, 0034, 0051, 0103, 0105, 0106, L4-07, L4-10, L4-11) e 11 E. Novos: 3 C e 4 E (43% C na parte, dentro de 40% a 60%). Folha: 15 C / 15 E.

FIM DA PARTE 2/4

## PARTE 3/4 — Verificação de rede (18/10/2026)

Comando (por página): `curl -sL -m 40 -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36" -o <arquivo> -w "%{http_code} %{size_download}" <URL>`; busca textual no HTML sem scripts e estilos, entidades decodificadas.

| página | URL | HTTP | bytes | resultado |
|---|---|--:|--:|---|
| Google for Developers, "Introduction to ML: What is Machine Learning?" | https://developers.google.com/machine-learning/intro-to-ml/what-is-ml | 200 | 106.617 | aberta em 18/10/2026; trechos literais presentes (abaixo) |
| Google for Developers, "Machine Learning Glossary: Generative AI" | https://developers.google.com/machine-learning/glossary/generative | 200 | 164.806 | aberta em 18/10/2026; trecho literal do RLHF presente (abaixo) |

Trecho literal por item (todos confirmados na página aberta hoje; data de verificação: 18/10/2026):

- L4-R01: "Supervised learning uses labeled data to make predictions, often for regression (predicting numerical values) or classification (categorizing data)."
- L4-R02: "Using feedback from human raters to improve the quality of a model's responses. For example, an RLHF mechanism can ask users to rate the quality of a model's response with a 👍 or 👎 emoji. The system can then adjust its future responses based on that feedback."
- L4-R03: "A reinforcement learning system generates a policy that defines the best strategy for getting the most rewards."
- L4-R04: "Reinforcement learning is used to train robots to perform tasks, like walking around a room, and software programs like AlphaGo to play the game of Go."
- L4-R05: "Binary classification models output a value from a class that contains only two values, for example, a model that outputs either rain or no rain. Multiclass classification models output a value from a class that contains more than two values"
- L4-R06: "ML systems can be categorized as supervised, unsupervised, reinforcement, or generative AI, each learning differently."
- L4-R07: "Reinforcement Learning from Human Feedback (RLHF) ... Using feedback from human raters to improve the quality of a model's responses."

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
No aprendizado por reforço, denomina-se política a recompensa que o agente recebe após cada ação executada no ambiente.

Gabarito: E
Justificativa (duas linhas): Armadilha: troca de conceito. A recompensa é o sinal recebido após a ação; a política é a estratégia que o sistema gera para obter o máximo de recompensas. Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026.
[TS]: sim. VOLÁTIL: não. Aderência: direta. Ponto de julgamento: política (policy) no reforço = estratégia para acumular recompensas, e não a recompensa. Formato: troca de sujeito. QA: PENDENTE.
Proveniência: Google for Developers, "Introduction to ML: What is Machine Learning?", https://developers.google.com/machine-learning/intro-to-ml/what-is-ml, verificado em 18/10/2026 (aberta hoje, HTTP 200).

### L4-R04 (P1-5.2). AUTORAL. Julgue o item.
Um laboratório treina um robô para caminhar por uma sala por tentativa e erro: o robô executa movimentos, recebe recompensas quando avança e penalidades quando cai.
Nessa situação, o treinamento caracteriza aprendizado supervisionado, pois o robô aprende a partir de exemplos que trazem a resposta correta para cada movimento.

Gabarito: E
Justificativa (duas linhas): Armadilha: troca de tipo de aprendizado. Treinar robôs para caminhar por uma sala é exemplo de aprendizado por reforço, que usa recompensas e penalidades por ações no ambiente, e não exemplos com resposta correta. Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026.
[TS]: sim. VOLÁTIL: não. Aderência: direta. Ponto de julgamento: exemplo canônico do reforço (robô que aprende a caminhar) reconhecido em cenário concreto. Formato: situação hipotética. QA: PENDENTE.
Proveniência: Google for Developers, "Introduction to ML: What is Machine Learning?", https://developers.google.com/machine-learning/intro-to-ml/what-is-ml, verificado em 18/10/2026 (aberta hoje, HTTP 200).

### L4-R05 (P1-5.2). AUTORAL. Julgue o item.
Um modelo de classificação cuja saída é apenas uma entre duas classes, como "chuva" ou "sem chuva", é denominado de classificação binária; se admitir mais de duas classes, é de classificação multiclasse.

Gabarito: C
Justificativa (duas linhas): O critério é o número de classes na saída: duas, binária; mais de duas, multiclasse. Os dois tipos são classificação, tarefa supervisionada. Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026.
[TS]: não. VOLÁTIL: não. Aderência: direta. Ponto de julgamento: classificação binária × multiclasse (critério: número de classes da saída). Formato: par confundível. QA: PENDENTE.
Proveniência: Google for Developers, "Introduction to ML: What is Machine Learning?", https://developers.google.com/machine-learning/intro-to-ml/what-is-ml, verificado em 18/10/2026 (aberta hoje, HTTP 200).

### L4-R06 (P1-5.2). AUTORAL. Julgue o item.
Segundo a página do Google for Developers sobre aprendizado de máquina, os sistemas de ML são classificados, quanto à forma como aprendem, em três categorias (supervisionado, não supervisionado e por reforço), não se incluindo a IA generativa nessa classificação.

Gabarito: E
Justificativa (duas linhas): Armadilha: número de categorias. A página classifica os sistemas em quatro categorias quanto à forma de aprender: supervisionado, não supervisionado, por reforço e IA generativa. Fonte: Google for Developers, "Introduction to ML: What is Machine Learning?", verificado em 18/10/2026.
[TS]: sim. VOLÁTIL: não. Aderência: direta. Ponto de julgamento: classificação do Google dos sistemas de ML por forma de aprender: quatro categorias, com a IA generativa. Formato: número ou prazo. QA: PENDENTE.
Proveniência: Google for Developers, "Introduction to ML: What is Machine Learning?", https://developers.google.com/machine-learning/intro-to-ml/what-is-ml, verificado em 18/10/2026 (aberta hoje, HTTP 200).

### L4-R07 (P1-5.2). AUTORAL. Julgue o item.
Por utilizar avaliações feitas por pessoas, o RLHF é classificado como técnica de aprendizado não supervisionado.

Gabarito: E
Justificativa (duas linhas): Armadilha: troca de categoria. O RLHF é aprendizado por reforço com feedback humano (reinforcement learning from human feedback); a presença de avaliadores humanos não o torna não supervisionado. Fonte: Google for Developers, "Machine Learning Glossary: Generative AI", verificado em 18/10/2026.
[TS]: sim. VOLÁTIL: não. Aderência: direta. Ponto de julgamento: enquadramento do RLHF: reforço com feedback humano, e não não supervisionado. Formato: par confundível. QA: PENDENTE.
Proveniência: Google for Developers, "Machine Learning Glossary: Generative AI", https://developers.google.com/machine-learning/glossary/generative, verificado em 18/10/2026 (aberta hoje, HTTP 200).

### Tabela de proveniência
| fonte | URL oficial | data de verificação | itens |
|---|---|---|---|
| Google for Developers, "Introduction to ML: What is Machine Learning?" | https://developers.google.com/machine-learning/intro-to-ml/what-is-ml | 18/10/2026 (HTTP 200) | L4-R01, L4-R03, L4-R04, L4-R05, L4-R06 |
| Google for Developers, "Machine Learning Glossary: Generative AI" | https://developers.google.com/machine-learning/glossary/generative | 18/10/2026 (HTTP 200) | L4-R02, L4-R07 |

### Contagem
Itens: 7. Gabarito: C 3 / E 4. [TS]: 4. VOLÁTEIS: 0. Folha P1-5.2: 23 + 7 = 30 (15 C / 15 E).

### Varredura (regra 0.7)
Regex das categorias da ordem C (marca de lote, ids de item, códigos de par e de fonte, etiquetas [V…]/[NORMATIVO…], prefixos TC/IC/GI/AT, "Difere do item", QA, produção, errata, versão) sobre textoBase, enunciado e justificativa dos 7 itens: zero ocorrências. As notas de deduplicação ficam só nas Partes 1 e 2. As páginas aparecem por extenso, com "verificado em 18/10/2026".

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
  "url": "saida/gcb/T113_onda1_P1_v1.md"
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
  "url": "saida/gcb/T113_onda1_P1_v1.md"
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
  "enunciado": "No aprendizado por reforço, denomina-se política a recompensa que o agente recebe após cada ação executada no ambiente.",
  "gabarito": "E",
  "justificativa": "Armadilha: troca de conceito. A recompensa é o sinal recebido após a ação; a política é a estratégia que o sistema gera para obter o máximo de recompensas. Fonte: Google for Developers, \"Introduction to ML: What is Machine Learning?\", verificado em 18/10/2026.",
  "itemEdital": "P1-5.2",
  "aderencia": "direta",
  "url": "saida/gcb/T113_onda1_P1_v1.md"
 },
 {
  "id": "L4-R04",
  "rotulo": "AUTORAL",
  "certame": "Projeto Câmara 2026",
  "cargo": "Lote 4",
  "ano": 2026,
  "numero": 4,
  "comando": "Julgue o item.",
  "textoBase": "Um laboratório treina um robô para caminhar por uma sala por tentativa e erro: o robô executa movimentos, recebe recompensas quando avança e penalidades quando cai.",
  "enunciado": "Nessa situação, o treinamento caracteriza aprendizado supervisionado, pois o robô aprende a partir de exemplos que trazem a resposta correta para cada movimento.",
  "gabarito": "E",
  "justificativa": "Armadilha: troca de tipo de aprendizado. Treinar robôs para caminhar por uma sala é exemplo de aprendizado por reforço, que usa recompensas e penalidades por ações no ambiente, e não exemplos com resposta correta. Fonte: Google for Developers, \"Introduction to ML: What is Machine Learning?\", verificado em 18/10/2026.",
  "itemEdital": "P1-5.2",
  "aderencia": "direta",
  "url": "saida/gcb/T113_onda1_P1_v1.md"
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
  "url": "saida/gcb/T113_onda1_P1_v1.md"
 },
 {
  "id": "L4-R06",
  "rotulo": "AUTORAL",
  "certame": "Projeto Câmara 2026",
  "cargo": "Lote 4",
  "ano": 2026,
  "numero": 6,
  "comando": "Julgue o item.",
  "textoBase": "",
  "enunciado": "Segundo a página do Google for Developers sobre aprendizado de máquina, os sistemas de ML são classificados, quanto à forma como aprendem, em três categorias (supervisionado, não supervisionado e por reforço), não se incluindo a IA generativa nessa classificação.",
  "gabarito": "E",
  "justificativa": "Armadilha: número de categorias. A página classifica os sistemas em quatro categorias quanto à forma de aprender: supervisionado, não supervisionado, por reforço e IA generativa. Fonte: Google for Developers, \"Introduction to ML: What is Machine Learning?\", verificado em 18/10/2026.",
  "itemEdital": "P1-5.2",
  "aderencia": "direta",
  "url": "saida/gcb/T113_onda1_P1_v1.md"
 },
 {
  "id": "L4-R07",
  "rotulo": "AUTORAL",
  "certame": "Projeto Câmara 2026",
  "cargo": "Lote 4",
  "ano": 2026,
  "numero": 7,
  "comando": "Julgue o item.",
  "textoBase": "",
  "enunciado": "Por utilizar avaliações feitas por pessoas, o RLHF é classificado como técnica de aprendizado não supervisionado.",
  "gabarito": "E",
  "justificativa": "Armadilha: troca de categoria. O RLHF é aprendizado por reforço com feedback humano (reinforcement learning from human feedback); a presença de avaliadores humanos não o torna não supervisionado. Fonte: Google for Developers, \"Machine Learning Glossary: Generative AI\", verificado em 18/10/2026.",
  "itemEdital": "P1-5.2",
  "aderencia": "direta",
  "url": "saida/gcb/T113_onda1_P1_v1.md"
 }
]
```
FIM DO LOTE
