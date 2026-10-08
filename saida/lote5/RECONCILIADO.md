# RECONCILIADO.md — Lote 5 — 2026-10-08 — gerado por orquestrador (sessão principal)

Origem: v1_producao.md e v2_producao.md (gcb-cpp, modelo sonnet); qa1_relatorio.md e qa2_relatorio.md (gcb-cqfp, modelo opus).
Papel do orquestrador: rotear, verificar completude, reconciliar e gravar. Nenhum conteúdo pedagógico foi escrito ou corrigido aqui; o texto da seção (a) é transcrição da v2 (só os níveis de título foram rebaixados para caber neste documento) com notas de pendência marcadas como [NOTA DO ORQUESTRADOR].
Material para revisão humana. Nada deste arquivo vai à candidata.

Gates: QA1 reprovou 3/20 = 15%; QA2 reprovou 1/20 = 5%. Nenhum dos dois ultrapassou 30%.

---

# PARTE A — CONTEÚDO FINAL APROVADO

Critério: curso, resumo e pares confundíveis da v2 (QA2: correção conceitual CORRETO, com apontamentos menores N1–N3 sinalizados no texto) e os 17 itens com veredito APROVADO no QA2. Os itens A5-15, A5-16 e A5-17 estão fora desta parte; ver PARTE D.

## (a) CURSO

### NOTA DE EVIDÊNCIA
- URL aberta com sucesso em 2026-10-08 e que sustenta afirmação: https://cloud.google.com/blog/products/data-analytics/looker-studio-is-data-studio (Google Cloud Blog, fornecedor do produto).
- URLs tentadas e bloqueadas (EGRESS_BLOCKED) em 2026-10-08: https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview e https://www.tableau.com/why-tableau/what-is-tableau.
- Consequência: sobre Power BI e Tableau, recursos, versões, preços e limites ficam "[SEM FONTE — não afirmar]". Do edital sabe-se apenas que são ferramentas de visualização cobradas no item 8.3.

### 7.1 Conceitos, atributos, métricas, transformação de dados

Definição precisa
- Dado: registro bruto de um fato (ex.: "Projeto de Lei nº X, autor Y, apresentado em tal data"). Informação é o dado interpretado em contexto.
- Atributo: característica descritiva de uma entidade ou registro; a "coluna" que qualifica (partido, UF, tipo de proposição, data). Pode ser categórico (nominal ou ordinal) ou numérico.
- Métrica (medida): valor quantitativo mensurável, em geral resultado de agregação (contagem, soma, média), usado para avaliar volume ou desempenho (ex.: nº de proposições por mês).
- Dimensão × métrica: dimensões são atributos pelos quais se fatia a análise; métricas são o que se mede.
- Dados estruturados (tabelas com esquema fixo), semiestruturados (JSON, XML) e não estruturados (texto livre, áudio, vídeo).
- Transformação de dados: operações que alteram forma ou conteúdo para adequar os dados à análise: filtragem, junção, agregação, conversão de tipos, normalização de escala, campos calculados, pivoteamento.
- Limpeza de dados (data cleaning): correção de problemas de qualidade, como duplicatas, valores ausentes, erros de digitação e formatos inconsistentes. A literatura trata a limpeza de duas maneiras: como etapa de preparação própria, anterior à análise, ou como uma das operações da etapa de transformação (o "T" de ETL). Por isso, a afirmação "a transformação pode incluir a limpeza" tende a ser aceita como verdadeira; o erro típico é dizer que limpeza consiste em agregar ou derivar campos.

Exemplo aplicado
- Em base de proposições legislativas: "tipo de proposição" e "partido do autor" são atributos; "quantidade de proposições por mês" é métrica. Padronizar "PL", "P.L." e "Projeto de Lei" é limpeza; somar proposições por partido é transformação (agregação).

Pegadinha provável
- Trocar atributo por métrica (dizer que "UF do autor" é métrica); chamar de "limpeza" uma agregação ou derivação de campo; afirmar que dados estruturados são os "sem esquema".

### 8.1 Princípios de visualização de dados

Definição precisa
- Objetivo: traduzir dados em representações visuais que facilitem percepção, comparação e decisão.
- Princípios usuais: clareza e foco na mensagem; gráfico adequado ao tipo de dado e à pergunta; razão dados/tinta alta (eliminar ruído e decoração sem informação); integridade gráfica (escalas honestas; barras partem de zero; evitar distorção de proporções); uso funcional da cor (paleta qualitativa para categorias, sequencial para magnitude ordenada, divergente para desvios em torno de um ponto central; atenção ao daltonismo); rotulagem clara (título, eixos, unidades, fonte); hierarquia visual e consistência; acessibilidade.
- Atributos pré-atentivos (posição, comprimento, cor, tamanho) permitem leitura rápida; posição e comprimento são percebidos com mais precisão que área ou ângulo.

Exemplo aplicado
- Painel de execução orçamentária de um órgão legislativo: barras ordenadas por valor, eixo iniciando em zero, uma cor de destaque para a rubrica em foco e cinza para as demais.

Pegadinha provável
- Afirmar que truncar o eixo de barras é boa prática para realçar diferenças; dizer que mais cores e efeitos 3D aumentam a clareza; usar paleta sequencial para categorias sem ordem.

### 8.2 Tipos de gráficos

#### Histograma
- Definição: mostra a distribuição de frequência de uma variável quantitativa dividida em classes (intervalos) contíguas. Como o eixo horizontal é uma escala numérica contínua, as barras são adjacentes. Com classes de mesma amplitude, a altura da barra é proporcional à frequência. Com classes de amplitudes desiguais, a área da barra é que deve ser proporcional à frequência, e a altura passa a representar a densidade de frequência (frequência dividida pela amplitude da classe). Altura e área não são equivalentes em geral.
- Exemplo: distribuição do tempo de tramitação (em dias) de proposições.
- Pegadinha: tratá-lo como gráfico de barras de categorias; dizer que a ordem das classes é intercambiável; tratar altura e área como sempre equivalentes.

#### Gráfico de linha
- Definição: liga pontos sucessivos para mostrar a evolução de uma variável, tipicamente no tempo (eixo horizontal ordenado). Destaca tendência, sazonalidade e variações.
- Exemplo: número mensal de requerimentos de informação ao longo de uma legislatura.
- Pegadinha: confundir com dispersão; usar linha para categorias sem ordem.

#### Gráfico de barras
- Definição: compara valores entre categorias discretas; o comprimento da barra é proporcional ao valor e a base é em zero. Pode ser horizontal ou vertical, agrupado ou empilhado. O espaçamento entre barras é convenção de desenho que reforça tratar-se de categorias; o critério conceitual é a natureza da variável (categórica), não o espaço.
- Exemplo: quantidade de projetos por comissão.
- Pegadinha: confundir com histograma; aceitar eixo truncado; usar para distribuição de variável contínua agrupada em classes.

#### Gráfico de dispersão
- Definição: cada ponto é uma observação com coordenadas em duas variáveis quantitativas; revela relação, padrão, agrupamentos e outliers. Correlação visível não prova causalidade.
- Exemplo: gasto de gabinete versus número de proposições por parlamentar.
- Pegadinha: afirmar que mostra causa e efeito; confundir com linha; dizer que exige variável categórica.

#### Box plot (diagrama de caixa)
- Definição: resume a distribuição de uma variável quantitativa. A caixa vai do 1º quartil (Q1) ao 3º quartil (Q3), ou seja, contém os 50% centrais dos dados; a amplitude da caixa é o intervalo interquartil (AIQ = Q3 − Q1). A linha interna é a mediana (não a média).
- Bigodes e outliers (regra usual de Tukey, adotada como convenção por muitos programas, mas que pode variar): calculam-se limites em Q1 − 1,5·AIQ e Q3 + 1,5·AIQ; os bigodes vão até o dado mais extremo que ainda esteja dentro desses limites, e os pontos fora deles são marcados individualmente como outliers. Logo, quando há outliers, os bigodes não terminam no mínimo e no máximo da amostra; só terminam neles quando não há valores atípicos.
  - [NOTA DO ORQUESTRADOR — apontamento QA2 N1 em aberto: a regra dos bigodes vale para cada lado separadamente; ver PARTE B, D6. Texto não alterado pelo orquestrador.]
- Comparação entre grupos: a variável resumida é quantitativa; os grupos são categorias de uma variável categórica (ex.: uma caixa por comissão). Não mostra a forma detalhada da distribuição (como bimodalidade), que o histograma mostra.
- Exemplo: comparar a distribuição de prazos de análise entre comissões.
- Pegadinha: dizer que a linha central é a média; que a caixa vai do mínimo ao máximo; que a caixa contém todos os dados; que mostra a forma detalhada como o histograma.

### 8.3 Ferramentas de visualização de dados (Power BI, Tableau e Data Studio)

Definição precisa
- Categoria: ferramenta de visualização de dados é software para conectar fontes de dados, construir visuais, reuni-los em painéis (dashboards) e compartilhar análises. Este é o conceito geral de categoria, não uma afirmação de recurso de produto específico. A ferramenta é meio: os princípios de 8.1 e a escolha do gráfico de 8.2 continuam sendo responsabilidade do analista.
- Power BI: recursos, componentes, versões, licenças e limites: [SEM FONTE — não afirmar]. URL oficial tentada e bloqueada em 2026-10-08: https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview.
- Tableau: recursos, produtos, versões e preços: [SEM FONTE — não afirmar]. URL oficial tentada e bloqueada em 2026-10-08: https://www.tableau.com/why-tableau/what-is-tableau.
- Data Studio (Google): verificado em 2026-10-08 no Google Cloud Blog. Fonte: https://cloud.google.com/blog/products/data-analytics/looker-studio-is-data-studio. O título da aba e o slug são "Looker Studio is Data Studio"; a manchete do post é "Data Studio returns as new home for Data Cloud assets"; data do post: April 10, 2026.
  - Trecho literal: "reintroducing a beloved and familiar name, Data Studio (formerly Looker Studio)."
  - Trecho literal: "We believe the new Data Studio is the ideal choice for personal data exploration — a place to craft ad-hoc reports, and quickly visualize data across Google's ecosystem, from BigQuery to Google Sheets and Ads."
  - Trecho literal sobre o Looker: "As part of this reintroduction, with Looker as our enterprise business intelligence platform, we are evolving Data Studio to complement the Looker platform, independently."
  - Conclusão sustentada pela fonte: Data Studio é o nome vigente em 2026-10-08 do produto antes chamado Looker Studio; Looker é a plataforma corporativa de BI, tratada no post como distinta.
  - O que a fonte não informa e não se afirma: data efetiva de transição, novo domínio, recursos, preços, limites. O histórico de renomeações anteriores (2022) não foi aberto em fonte oficial: [SEM FONTE — não afirmar].

Exemplo aplicado
- Uma consultoria legislativa poderia reunir em um painel os visuais de proposições por tema, tipo e mês. Nenhuma capacidade de produto específico é afirmada.

Pegadinha provável
- Atribuir a uma ferramenta recurso de outra; tratar "Looker Studio" e "Data Studio" como produtos diferentes (a prova pode usar qualquer dos nomes); confundir Data Studio com Looker (plataforma corporativa); supor que a ferramenta escolhe o gráfico certo no lugar do analista; misturar com Excel/Office (itens 1 a 6, fora do escopo).
  - [NOTA DO ORQUESTRADOR — apontamentos QA2 N2 e N3 em aberto: "itens 1 a 6" e "a prova pode usar qualquer dos nomes" estão sem fonte; ver PARTE B, D7–D8 e PENDENTE NORMATIVO/TÉCNICO. Texto não alterado pelo orquestrador.]

### 8.4 Storytelling para visualização de dados

Definição precisa
- Storytelling com dados: combinação de dados, visuais e narrativa para comunicar uma mensagem e conduzir o público a uma conclusão ou ação.
- Estrutura narrativa clássica: contexto (público e o que está em jogo), conflito ou problema (o que os dados revelam), resolução ou chamada à ação (o que fazer).
- Práticas: conhecer o público; definir a mensagem principal ("big idea") antes de escolher gráficos; usar destaque (cor, anotação, título que afirma a conclusão) para guiar a atenção; remover ruído; ordenar a sequência para que cada visual sustente o ponto seguinte; diferenciar análise exploratória (o analista descobre) de explanatória (o público é conduzido a uma mensagem já definida).

Exemplo aplicado
- Apresentação à Mesa Diretora sobre atraso na tramitação: título "Prazo médio de análise dobrou em dois anos", gráfico de linha com o ponto de inflexão anotado e recomendação final.

Pegadinha provável
- Dizer que storytelling é apenas enfeitar o gráfico ou dispensa mensagem explícita; inverter exploratória e explanatória; sugerir mostrar todos os dados em vez de selecionar o que sustenta a mensagem.

---

## (b) RESUMO (uma página)

7.1
- Atributo = característica descritiva (coluna qualificadora). Métrica = valor quantitativo agregado. Dimensão fatia; métrica mede.
- Limpeza = corrigir qualidade (duplicatas, ausentes, formatos); pode ser vista como etapa própria ou como parte da transformação. Transformação = remodelar, agregar, derivar (filtro, junção, agregação, campo calculado). Agregar não é limpar.
- Estruturado = esquema fixo; não estruturado = texto livre, áudio, vídeo.

8.1
- Mensagem clara, gráfico adequado, pouco ruído, escalas honestas (barras desde zero), cor com função (qualitativa para categorias, sequencial para magnitude, divergente para desvio), rótulos e acessibilidade.

8.2
- Histograma: variável quantitativa em classes contíguas; mesma amplitude: altura proporcional à frequência; amplitudes desiguais: área proporcional (altura = densidade).
- Linha: evolução (tempo) e tendência.
- Barras: comparação entre categorias; base em zero.
- Dispersão: relação entre duas quantitativas; correlação não é causalidade.
- Box plot: caixa Q1 a Q3 (50% centrais); linha = mediana; bigodes até o dado mais extremo dentro de Q1 − 1,5·AIQ e Q3 + 1,5·AIQ; fora disso, outliers; compara grupos (categóricos) de uma variável quantitativa.

8.3
- Ferramenta de visualização = conecta fontes, constrói visuais e painéis; não substitui o critério do analista.
- Data Studio é o nome vigente (verificado em 2026-10-08, Google Cloud Blog, post de April 10, 2026) do produto antes chamado Looker Studio; Looker é a plataforma corporativa de BI.
- Power BI e Tableau: recursos, versões, preços e limites: [SEM FONTE — não afirmar].

8.4
- Dados + visual + narrativa; público primeiro; mensagem principal; contexto, conflito, resolução; destaque e anotações; explanatória (conduz) × exploratória (descobre).

---

## (c) PARES CONFUNDÍVEIS

1. Histograma × gráfico de barras
- Histograma: variável quantitativa agrupada em classes contíguas; barras adjacentes porque o eixo é contínuo; ordem das classes fixa; mostra distribuição.
- Barras: categorias discretas; a ordem pode variar; compara valores; o espaço entre barras é convenção visual.
- Teste rápido: o eixo horizontal é uma escala numérica contínua dividida em intervalos? Histograma.

2. Linha × dispersão
- Linha: pontos ligados em sequência (em geral tempo); evolução e tendência.
- Dispersão: pontos soltos, duas variáveis quantitativas; relação, agrupamentos e outliers; sem ordem sequencial.
- Teste rápido: um eixo é tempo? Linha. Dois números por observação, sem sequência? Dispersão.

3. Box plot × histograma
- Box plot: caixa Q1–Q3 com 50% centrais, mediana, bigodes e outliers (regra usual de 1,5·AIQ); bom para comparar muitos grupos; não mostra a forma detalhada (ex.: bimodalidade).
- Histograma: mostra a forma da distribuição por frequências em classes; não evidencia quartis e mediana diretamente.
- Linha dentro da caixa = mediana, não média. Bigodes nem sempre vão ao mínimo e ao máximo.

4. Atributo × métrica
- Atributo: característica descritiva do registro (partido, UF, tipo).
- Métrica: valor quantitativo agregado (contagem de proposições, média de dias).
- Coluna numérica não é automaticamente métrica (ex.: número do projeto é identificador).

5. Transformação × limpeza de dados
- Limpeza: corrige defeitos de qualidade (duplicatas, nulos, erros, formatos inconsistentes).
- Transformação: muda estrutura ou conteúdo para análise (agregar, juntar, filtrar, derivar campo, normalizar).
- Padronizar grafias divergentes = limpeza; somar por mês = transformação. Em ETL, a limpeza costuma ser tratada como parte do "T"; assim "a transformação pode incluir limpeza" é, em geral, verdadeira, e "limpeza consiste em agregar" é falsa.

6. Data Studio × Looker Studio (e × Looker)
- Nome vigente: Data Studio. Verificado em 2026-10-08 no Google Cloud Blog (aba/URL "Looker Studio is Data Studio"; manchete "Data Studio returns as new home for Data Cloud assets"; data April 10, 2026): "reintroducing a beloved and familiar name, Data Studio (formerly Looker Studio)". Fonte: https://cloud.google.com/blog/products/data-analytics/looker-studio-is-data-studio
- Looker Studio: nome anterior do mesmo produto ("formerly Looker Studio").
- Looker: no mesmo post, "Looker as our enterprise business intelligence platform"; Data Studio evolui "to complement the Looker platform, independently". Não confundir Looker com Looker Studio/Data Studio.
- Data efetiva de transição e novo domínio: [SEM FONTE — não afirmar]. Em prova, aceitar os dois nomes como o mesmo produto; o edital usa "Data Studio".


## (d) ITENS C/E AUTORAL APROVADOS NO QA2 (17)

Julgue os itens a seguir. Rótulo de todos: AUTORAL.

A5-01 (7.1)
Em uma base de dados de proposições legislativas, "partido do autor" é exemplo de atributo, enquanto "número de proposições apresentadas por mês" é exemplo de métrica.
Gabarito: C.
Justificativa: O partido qualifica o registro (atributo). A contagem mensal é valor quantitativo agregado (métrica).
Troca sutil: não.

A5-02 (7.1)
A limpeza de dados consiste em agregar e derivar novos campos a partir dos dados existentes, como somar proposições por partido, com o objetivo de adequar a base à análise.
Gabarito: E.
Justificativa: Agregar e derivar campos é transformação de dados. Limpeza corrige problemas de qualidade (duplicatas, ausentes, formatos).
Troca sutil: sim (limpeza no lugar de transformação).

A5-03 (7.1)
A transformação de dados pode envolver operações como filtragem, junção de tabelas, agregação e criação de campos calculados.
Gabarito: C.
Justificativa: São operações típicas de transformação, que remodelam os dados para a análise.
Troca sutil: não.

A5-04 (7.1)
Dados estruturados são aqueles que não seguem esquema predefinido, como textos livres de discursos parlamentares e arquivos de áudio de sessões.
Gabarito: E.
Justificativa: Texto livre e áudio são dados não estruturados. Dados estruturados seguem esquema fixo, como tabelas.
Troca sutil: sim (estruturados no lugar de não estruturados).

A5-05 (8.1)
Na visualização de dados, é recomendável destacar a mensagem principal e eliminar elementos decorativos que não carreguem informação, de modo a reduzir o ruído visual.
Gabarito: C.
Justificativa: Clareza e alta razão dados/tinta são princípios centrais de visualização.
Troca sutil: não.

A5-06 (8.1)
Em gráfico de barras, iniciar o eixo vertical em valor diferente de zero é prática recomendada, pois amplia as diferenças entre as categorias sem comprometer a integridade da leitura.
Gabarito: E.
Justificativa: O comprimento da barra codifica o valor, então truncar a base distorce a proporção. Barras devem partir de zero.
Troca sutil: sim (recomendada no lugar de desaconselhada).

A5-07 (8.1)
Para representar categorias sem ordem natural, como as unidades da Federação, recomenda-se paleta de cores sequencial, que sugere progressão de menor para maior valor.
Gabarito: E.
Justificativa: Categorias sem ordem pedem paleta qualitativa. A sequencial sugere magnitude ordenada.
Troca sutil: sim (sequencial no lugar de qualitativa).

A5-08 (8.2)
No histograma, as classes são intervalos contíguos de uma variável quantitativa e, quando todas têm a mesma amplitude, a altura de cada barra é proporcional à frequência da classe.
Gabarito: C.
Justificativa: O eixo é contínuo, por isso as barras se tocam. Com amplitudes iguais, altura e frequência são proporcionais.
Troca sutil: não.

A5-09 (8.2)
O histograma representa categorias discretas e independentes, cuja ordem pode ser alterada sem prejuízo da leitura, enquanto o gráfico de barras representa a distribuição de uma variável quantitativa contínua dividida em classes.
Gabarito: E.
Justificativa: A situação é inversa: o histograma trata de variável quantitativa em classes ordenadas e o gráfico de barras compara categorias discretas.
Troca sutil: sim (inversão entre histograma e gráfico de barras).

A5-10 (8.2)
O gráfico de linha é adequado para representar a evolução de uma variável ao longo do tempo, pois evidencia tendências e variações entre períodos sucessivos.
Gabarito: C.
Justificativa: Ligar pontos ordenados no tempo é a função típica do gráfico de linha.
Troca sutil: não.

A5-11 (8.2)
O gráfico de dispersão exibe a relação entre duas variáveis quantitativas e, quando os pontos formam padrão linear, comprova que a variação de uma variável causa a variação da outra.
Gabarito: E.
Justificativa: O padrão indica correlação, que não comprova causalidade.
Troca sutil: sim (comprova causa no lugar de sugere correlação).

A5-12 (8.2)
O box plot resume a distribuição de uma variável quantitativa por meio da mediana e dos quartis, em uma caixa que contém os 50% centrais dos dados, e permite sinalizar valores atípicos e comparar grupos.
Gabarito: C.
Justificativa: A caixa vai de Q1 a Q3 (50% centrais), a linha interna é a mediana e pontos isolados indicam outliers. Grupos diferentes podem ser comparados lado a lado.
Troca sutil: não.

A5-13 (8.2)
No box plot, a linha traçada no interior da caixa representa a média aritmética dos dados, e a caixa delimita o intervalo entre o primeiro e o terceiro quartis.
Gabarito: E.
Justificativa: A linha interna é a mediana, não a média. A delimitação da caixa entre Q1 e Q3 está correta.
Troca sutil: sim (média no lugar de mediana; única troca).

A5-14 (8.3)
Data Studio é o nome atualmente adotado pelo Google para o produto de visualização de dados anteriormente denominado Looker Studio.
Gabarito: C.
Justificativa: O Google Cloud descreve "Data Studio (formerly Looker Studio)". Verificado em 2026-10-08 em https://cloud.google.com/blog/products/data-analytics/looker-studio-is-data-studio.
Troca sutil: não.

A5-18 (8.4)
O storytelling para visualização de dados combina dados, elementos visuais e narrativa para comunicar uma mensagem e conduzir o público a uma conclusão ou ação.
Gabarito: C.
Justificativa: É a definição essencial: dados, visual e narrativa a serviço de uma mensagem.
Troca sutil: não.

A5-19 (8.4)
A análise exploratória é aquela em que o analista, já conhecendo a mensagem principal, seleciona os dados que a sustentam para conduzir o público a uma conclusão.
Gabarito: E.
Justificativa: Esse é o perfil da análise explanatória. Na exploratória o analista ainda investiga os dados para descobrir padrões.
Troca sutil: sim (exploratória no lugar de explanatória; única troca).

A5-20 (8.4)
Em uma apresentação com storytelling, o uso de cor de destaque e de anotações para direcionar a atenção ao ponto-chave do gráfico contribui para a clareza da mensagem.
Gabarito: C.
Justificativa: Destaque e anotação guiam o olhar do público ao que sustenta a conclusão.
Troca sutil: não.

Observação do QA2 sobre A5-14 (aprovado com ressalva): o advérbio "atualmente" torna o item datado (vale na data da verificação, 2026-10-08), e o item cobre o mesmo fato do A5-15.

Efeito na distribuição exigida pelo despacho: 8.3 fica com 1 item aprovado de 4 exigidos. Trocas sutis válidas entre os aprovados: 8 (A5-02, 04, 06, 07, 09, 11, 13, 19) de 10 exigidas. Gabaritos entre os aprovados: 9 C e 8 E.

---

# PARTE B — DIVERGÊNCIAS REMANESCENTES ENTRE CPP E CQFP (sem decisão de mérito)

Formato: posição da CPP (v2) | posição da CQFP (QA2). O orquestrador não decide.

- D1. Cobertura de Power BI e Tableau em 8.3. CPP: "acatado em parte"; mantém [SEM FONTE] por bloqueio de rede. CQFP: conduta aceita, mas NÃO RESOLVIDO; bloqueio reconfirmado (EGRESS_BLOCKED em learn.microsoft.com, www.tableau.com, powerbi.microsoft.com).
- D2. Refazer os itens de 8.3 (condição 1 do QA1). CPP: "atendida". CQFP: NÃO RESOLVIDO; dos 4 itens, 1 reprovado e 2 a ajustar.
- D3. A5-16. CPP: item conceitual de categoria, "sem afirmar recurso de produto específico". CQFP: RESPOSTA NÃO ACEITA; o enunciado nomeia Power BI e Tableau e afirma capacidades sem fonte. REPROVADO.
- D4. A5-15. CPP: âncora de data retirada; troca sutil válida. CQFP: âncora resolvida, mas a segunda oração ("não pode ser identificado com o outro") é vaga e o item repete o fato do A5-14. AJUSTAR.
- D5. A5-17. CPP: troca sutil (responsabilidade do analista × ferramenta). CQFP: troca não sutil (absurdo evidente), mede 8.1 e não ferramenta, e contém afirmação implícita sem fonte sobre os três produtos. AJUSTAR.
- D6. Box plot, bigodes (v2, curso 8.2). CPP: "quando há outliers, os bigodes não terminam no mínimo e no máximo". CQFP (N1, apontamento novo): a regra vale por lado; um outlier superior não impede o bigode inferior de terminar no mínimo. Sem resposta da CPP (surgiu na rodada 2).
- D7. Menção a "Excel/Office (itens 1 a 6)" na pegadinha de 8.3. CQFP (N2, novo): sem fonte; o edital no repositório só transcreve os itens 7 e 8. Sem resposta da CPP.
- D8. "A prova pode usar qualquer dos nomes" (pegadinha de 8.3). CQFP (N3, novo): especulação sobre a banca, sem base. Sem resposta da CPP.
- D9. Contagem de trocas sutis. CPP: 10. CQFP: 8 válidas, 1 a ajustar (A5-15), 1 não sutil (A5-17).
- D10. Declaração da v2 sobre itens alterados. CPP: "demais 14 itens sem alteração de mérito; A5-08 e A5-12 ajustados". CQFP: inexata, A5-09 também foi reescrito (o novo A5-09 está correto). Divergência só de registro.
- Registro (não é divergência): N4 do QA2 (histograma também se aplica a variável discreta agrupada) foi anotado pela CQFP apenas como observação, sem exigência.
- Resolvidas e sem divergência: histograma altura × área; box plot (Tukey, 50% centrais, quantitativa × categórica); limpeza × transformação; barras separadas; citações E1–E3; cabeçalho "P1, comum aos 11 cargos"; "Julgue o item" repetido; A5-13; A5-19; A5-14 (âncora); recusa de item exclusivo de barras (aceita pela CQFP); itens TRF6 não usados (aceito).

---

# PARTE C — AFIRMAÇÕES SOBRE FERRAMENTAS (com data e fonte)

Com fonte oficial verificada (aberta por CPP e conferida por CQFP em 2026-10-08):
- Fonte: https://cloud.google.com/blog/products/data-analytics/looker-studio-is-data-studio (Google Cloud Blog; título da aba "Looker Studio is Data Studio"; manchete "Data Studio returns as new home for Data Cloud assets"; post datado de April 10, 2026).
  - "Data Studio (formerly Looker Studio)": Data Studio é o nome vigente, em 2026-10-08, do produto antes chamado Looker Studio. Usado no curso 8.3, resumo, par 6 e itens A5-14 e A5-15.
  - Data Studio como "personal data exploration", "ad-hoc reports", dados do ecossistema Google "from BigQuery to Google Sheets and Ads".
  - Looker como "enterprise business intelligence platform", com o Data Studio evoluindo "to complement the Looker platform, independently".
- Fonte complementar aberta pela CQFP em 2026-10-08: https://cloud.google.com/looker-studio — só o título foi lido ("Data Studio: Business Insights Visualizations | Google Cloud"); corrobora o nome vigente.
- Trechos da mesma página do blog que a CQFP encontrou e que a v2 não cita (registro, sem incorporação): "serving as the on-ramp for creating and sharing ad-hoc reports, transforming data to an interactive dashboard in minutes" e "All existing reports, data sources, assets and users will be transitioned to the new experience with no action on your part."

Sem fonte datada após a rodada 2: movidas para PENDENTE NORMATIVO/TÉCNICO (abaixo), nunca aprovadas.

## PENDENTE NORMATIVO/TÉCNICO

- P1. Power BI: qualquer recurso, componente, versão, licença ou limite. URLs oficiais tentadas em 2026-10-08 e bloqueadas pela rede do ambiente: learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview; powerbi.microsoft.com.
- P2. Tableau: qualquer recurso, produto, versão ou preço. URLs tentadas em 2026-10-08 e bloqueadas: www.tableau.com/why-tableau/what-is-tableau; help.tableau.com.
- P3. A5-16: afirmação de que Power BI, Tableau e Data Studio "permitem conectar fontes de dados, construir visuais e reuni-los em painéis (dashboards) para compartilhamento" — sem fonte para Power BI e Tableau; para Data Studio havia trecho disponível não citado.
- P4. A5-17: afirmação implícita de que nenhuma das três ferramentas "assume a decisão" de escolha do gráfico — sem fonte de fornecedor.
- P5. Histórico de renomeação de 2022 (Data Studio → Looker Studio): não aberto em fonte oficial.
- P6. Data efetiva da transição de 2026 e eventual novo domínio: a fonte aberta não informa.
- P7. "A prova pode usar qualquer dos nomes" e menção a "Excel/Office (itens 1 a 6)": sem fonte (afirmações acessórias em 8.3; não são sobre recurso de ferramenta, mas foram listadas aqui por estarem sem fonte).

Para fechar P1 e P2: liberar na política de rede do ambiente os domínios oficiais da Microsoft e do Tableau, ou anexar ao repositório material oficial datado.

---

# PARTE D — SITUAÇÃO DOS ITENS AUTORAL (veredito do QA2)

Aprovados (17): A5-01, A5-02, A5-03, A5-04, A5-05, A5-06, A5-07, A5-08, A5-09, A5-10, A5-11, A5-12, A5-13, A5-14, A5-18, A5-19, A5-20.

Reprovados (1):
- A5-16 (8.3) — recursos de Power BI e Tableau afirmados sem fonte.

Pendentes — AJUSTAR (2):
- A5-15 (8.3) — segunda oração vaga; repete o fato do A5-14.
- A5-17 (8.3) — troca não sutil; não mede conhecimento de ferramenta.

Texto integral dos itens não aprovados (transcrição da v2, para a decisão humana):

A5-15 (8.3)
Looker Studio e Data Studio são produtos distintos e sem relação entre si, de modo que um relatório criado em um deles não pode ser identificado com o outro.
Gabarito: E.
Justificativa: Segundo o Google Cloud, Data Studio é o nome do produto antes chamado Looker Studio: trata-se do mesmo produto. Fonte verificada em 2026-10-08 (URL do A5-14).
Troca sutil: sim (produto distinto no lugar de mesmo produto renomeado).

A5-16 (8.3)
Ferramentas de visualização de dados, como Power BI, Tableau e Data Studio, permitem conectar fontes de dados, construir visuais e reuni-los em painéis (dashboards) para compartilhamento de análises.
Gabarito: C.
Justificativa: Descreve a categoria de ferramenta de visualização, sem afirmar recurso de produto específico. Detalhes de cada produto: [SEM FONTE — não afirmar].
Troca sutil: não.

A5-17 (8.3)
Ao se utilizar uma ferramenta de visualização como Power BI, Tableau ou Data Studio, deixa de ser necessário observar o tipo de dado e a pergunta analítica na escolha do gráfico, pois a ferramenta assume essa decisão pelo analista.
Gabarito: E.
Justificativa: A ferramenta é meio: a escolha do gráfico adequado ao dado e à pergunta continua sendo critério do analista (princípios de 8.1 e 8.2).
Troca sutil: sim (responsabilidade do analista no lugar de transferida à ferramenta).

Resultado contra o despacho: 17 de 20 itens aprovados; 8.3 com 1 de 4; 8 de 10 trocas sutis válidas. O lote não cumpre integralmente o padrão de entrega em 8.3 enquanto P1 e P2 estiverem pendentes.
