# v1_producao.md — Lote 5 — 2026-10-08 — gerado por gcb-cpp

Escopo: itens 7.1 e 8.1 a 8.4 do edital (Cargo 11, P1). Rótulo de todos os itens C/E: AUTORAL.

NOTA DE EVIDÊNCIA (leia primeiro)
- URL aberta com sucesso e que sustenta afirmação: https://cloud.google.com/blog/products/data-analytics/looker-studio-is-data-studio (verificado em 2026-10-08).
- URLs não acessíveis em 2026-10-08 (bloqueio de rede): learn.microsoft.com (Power BI), powerbi.microsoft.com, www.tableau.com, help.tableau.com, support.google.com, lookerstudio.google.com, docs.cloud.google.com.
- Consequência: sobre Power BI e Tableau, recursos, versões, preços e limites estão como [SEM FONTE — não afirmar]. Só se afirma que ambos constam do edital como ferramentas de visualização.

---

# (a) CURSO

## 7.1 Conceitos, atributos, métricas, transformação de dados

Definição precisa
- Dado: registro bruto de um fato (ex.: "Projeto de Lei nº X, autor Y, apresentado em tal data"). Informação é o dado interpretado em contexto.
- Atributo: característica descritiva de uma entidade/registro; é a "coluna" que qualifica (partido, UF, tipo de proposição, data). Pode ser categórico (nominal/ordinal) ou numérico.
- Métrica (medida): valor quantitativo mensurável, em geral resultado de agregação (contagem, soma, média) sobre atributos, usado para avaliar desempenho ou volume (ex.: nº de proposições por mês).
- Dimensão x métrica: dimensões são atributos pelos quais se fatia a análise; métricas são o que se mede.
- Dados estruturados (tabelas com esquema fixo), semiestruturados (JSON, XML) e não estruturados (textos livres, áudio, vídeo).
- Transformação de dados: operações que alteram forma ou conteúdo para adequar os dados à análise: filtragem, junção, agregação, conversão de tipos, normalização de escala, criação de campos calculados, pivoteamento.
- Limpeza de dados (data cleaning): correção de problemas de qualidade, como duplicatas, valores ausentes, erros de digitação e inconsistências de formato. É etapa de preparação, conceitualmente distinta da transformação.

Exemplo aplicado
- Em base de proposições legislativas: "tipo de proposição" e "partido do autor" são atributos; "quantidade de proposições por mês" é métrica. Padronizar "PL", "P.L." e "Projeto de Lei" para um só valor é limpeza; somar proposições por partido é transformação (agregação).

Pegadinha provável
- Trocar atributo por métrica (dizer que "UF do autor" é métrica), ou chamar de "limpeza" uma agregação/derivação de campo. Também: afirmar que dados estruturados são os "sem esquema".

## 8.1 Princípios de visualização de dados

Definição precisa
- Objetivo: traduzir dados em representações visuais que facilitem percepção, comparação e decisão.
- Princípios usuais: clareza e foco na mensagem; escolha do gráfico adequado ao tipo de dado e à pergunta; razão dados/tinta alta (eliminar ruído e decoração sem informação); integridade gráfica (escalas honestas; barras partem de zero; evitar distorção de proporções); uso funcional da cor (paleta qualitativa para categorias, sequencial para magnitude ordenada, divergente para desvios em torno de um ponto central; atenção a daltonismo); rotulagem clara (títulos, eixos, unidades, fonte); hierarquia visual e consistência; acessibilidade.
- Atributos pré-atentivos (posição, comprimento, cor, tamanho) permitem leitura rápida; posição e comprimento são percebidos com mais precisão que área ou ângulo.

Exemplo aplicado
- Painel de execução orçamentária de um órgão legislativo: gráfico de barras ordenadas por valor, eixo iniciando em zero, uma cor de destaque para a rubrica em foco e cinza para as demais.

Pegadinha provável
- Afirmar que truncar o eixo de barras é "boa prática" para realçar diferenças; dizer que mais cores e efeitos 3D aumentam a clareza; usar paleta sequencial para categorias sem ordem.

## 8.2 Tipos de gráficos

### Histograma
- Definição: mostra a distribuição de frequência de uma variável quantitativa (contínua ou discreta agrupada) dividida em classes (intervalos). Barras adjacentes, pois o eixo horizontal é contínuo; a altura (ou área) representa a frequência.
- Exemplo: distribuição do tempo de tramitação (em dias) de proposições.
- Pegadinha: tratá-lo como gráfico de barras de categorias; afirmar que as barras são separadas; dizer que a ordem das classes é intercambiável.

### Gráfico de linha
- Definição: liga pontos sucessivos para mostrar evolução de uma variável, tipicamente ao longo do tempo (eixo horizontal ordenado). Destaca tendência, sazonalidade e variações.
- Exemplo: número mensal de requerimentos de informação ao longo de uma legislatura.
- Pegadinha: confundir com dispersão (relação entre duas variáveis quantitativas sem ordem temporal); usar linha para categorias sem ordem.

### Gráfico de barras
- Definição: compara valores entre categorias discretas; comprimento da barra proporcional ao valor; barras separadas; base em zero. Pode ser horizontal ou vertical, agrupado ou empilhado.
- Exemplo: quantidade de projetos por comissão.
- Pegadinha: confundir com histograma; aceitar eixo truncado; usar para distribuição de variável contínua.

### Gráfico de dispersão
- Definição: cada ponto representa uma observação com coordenadas em duas variáveis quantitativas; revela relação, padrão, agrupamentos e outliers. Correlação visível não prova causalidade.
- Exemplo: gasto de gabinete versus número de proposições por parlamentar.
- Pegadinha: afirmar que mostra causa e efeito; confundir com linha; dizer que exige variável categórica.

### Box plot (diagrama de caixa)
- Definição: resume a distribuição por cinco números: mínimo, 1º quartil (Q1), mediana, 3º quartil (Q3) e máximo; a caixa vai de Q1 a Q3 (intervalo interquartil) e a linha interna marca a mediana; "bigodes" indicam a extensão dos dados e pontos isolados indicam valores atípicos (outliers), segundo a convenção adotada. Útil para comparar distribuições entre grupos.
- Exemplo: comparar a distribuição de prazos de análise entre comissões.
- Pegadinha: dizer que a linha central é a média; que mostra a forma detalhada da distribuição (como o histograma); que a caixa contém todos os dados.

## 8.3 Ferramentas de visualização de dados (Power BI, Tableau e Data Studio)

Definição precisa (somente o que tem fonte)
- Power BI, Tableau e Data Studio constam do edital (item 8.3) como ferramentas de visualização de dados, isto é, software para conectar fontes, construir visuais e painéis (dashboards) e compartilhar análises.
- Power BI: recursos, componentes, versões, licenças e limites: [SEM FONTE — não afirmar]. URL oficial tentada e não acessível em 2026-10-08: https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview.
- Tableau: recursos, produtos, versões e preços: [SEM FONTE — não afirmar]. URLs oficiais tentadas e não acessíveis em 2026-10-08: https://www.tableau.com/why-tableau/what-is-tableau e https://help.tableau.com/current/pro/desktop/en-us/what_is_tableau.htm.
- Data Studio (Google): ver nome vigente abaixo e em (c).
  - Verificado em 2026-10-08, Google Cloud Blog, post "Looker Studio is Data Studio", datado nesse post de "April 10, 2026": o Google Cloud informa que está "reintroducing a beloved and familiar name, Data Studio (formerly Looker Studio)". Fonte: https://cloud.google.com/blog/products/data-analytics/looker-studio-is-data-studio
  - O mesmo post descreve o Data Studio como adequado a "personal data exploration" (relatórios ad hoc) e ligado a fontes Google como BigQuery, Google Sheets e Ads.
  - Resumo: o produto nasceu como Data Studio, foi chamado Looker Studio e, segundo o post acima, voltou a se chamar Data Studio. O histórico da primeira renomeação (2022) vem apenas de fontes secundárias nesta rodada: [SEM FONTE oficial aberta — não afirmar datas de 2022].
  - Recursos, versões "Pro", preços e limites: [SEM FONTE — não afirmar].

Exemplo aplicado
- Uma consultoria legislativa poderia publicar um painel de proposições por tema; a escolha entre ferramentas é decisão de contexto. Nenhuma afirmação de capacidade específica de produto é feita aqui.

Pegadinha provável
- Atribuir a uma ferramenta recurso de outra; tratar "Looker Studio" e "Data Studio" como produtos diferentes (a prova pode usar qualquer dos nomes); misturar com Excel/Office (fora do escopo; itens 1 a 6).

## 8.4 Storytelling para visualização de dados

Definição precisa
- Storytelling com dados: combinação de dados, visuais e narrativa para comunicar uma mensagem e conduzir o público a uma conclusão ou ação.
- Estrutura narrativa clássica: contexto (quem é o público e o que está em jogo), conflito/problema (o que os dados revelam), resolução/chamada à ação (o que fazer).
- Práticas: conhecer o público; definir a mensagem principal ("big idea") antes de escolher gráficos; usar destaque (cor, anotação, título que afirma a conclusão) para guiar a atenção; remover ruído; ordenar a sequência para que cada visual sustente o ponto seguinte; diferenciar análise exploratória (o analista descobre) de explanatória (o público é conduzido).

Exemplo aplicado
- Apresentação à Mesa Diretora sobre atraso na tramitação: título "Prazo médio de análise dobrou em dois anos", gráfico de linha com o ponto de inflexão anotado e uma recomendação final.

Pegadinha provável
- Dizer que storytelling é apenas "enfeitar" o gráfico ou que dispensa mensagem explícita; inverter exploratória e explanatória; sugerir que se devem mostrar todos os dados disponíveis em vez de selecionar o que sustenta a mensagem.

---

# (b) RESUMO (uma página)

7.1
- Atributo = característica descritiva (coluna qualificadora). Métrica = valor quantitativo agregado. Dimensão fatia; métrica mede.
- Limpeza = corrigir qualidade (duplicatas, ausentes, formatos). Transformação = remodelar/agregar/derivar (filtro, junção, agregação, campo calculado).
- Estruturado = esquema fixo; não estruturado = texto livre, áudio, vídeo.

8.1
- Mensagem clara, gráfico adequado, pouco ruído, escalas honestas (barras desde zero), cor com função (qualitativa para categorias, sequencial para magnitude, divergente para desvio), rótulos e acessibilidade.

8.2
- Histograma: distribuição de variável quantitativa em classes; barras coladas.
- Linha: evolução (tempo) e tendência.
- Barras: comparação entre categorias; barras separadas; base zero.
- Dispersão: relação entre duas quantitativas; correlação não é causalidade.
- Box plot: mediana, Q1, Q3, extremos e outliers; compara grupos.

8.3
- Power BI, Tableau e Data Studio: ferramentas de visualização do edital.
- Data Studio é o nome que o Google Cloud, em post datado de 10/4/2026 (verificado em 2026-10-08), reintroduziu para o produto antes chamado Looker Studio.
- Recursos, versões, preços e limites de qualquer ferramenta: [SEM FONTE — não afirmar].

8.4
- Dados + visual + narrativa; público primeiro; mensagem principal; contexto, conflito, resolução; destaque e anotações; explanatória (conduz) x exploratória (descobre).

---

# (c) PARES CONFUNDÍVEIS

1. Histograma x gráfico de barras
- Histograma: variável quantitativa agrupada em classes contínuas; barras adjacentes; ordem das classes fixa; mostra distribuição.
- Barras: categorias discretas; barras separadas; ordem pode variar; compara valores.
- Teste rápido: o eixo horizontal é uma escala numérica contínua? Histograma.

2. Linha x dispersão
- Linha: pontos ligados em sequência (em geral tempo); mostra evolução e tendência de uma série.
- Dispersão: pontos soltos, duas variáveis quantitativas; mostra relação, agrupamentos e outliers; não há ordem sequencial.
- Teste rápido: um eixo é tempo? Linha. Dois números por observação sem sequência? Dispersão.

3. Box plot x histograma
- Box plot: resumo em cinco números; evidencia mediana, dispersão e outliers; ótimo para comparar muitos grupos; não mostra a forma detalhada (ex.: bimodalidade).
- Histograma: mostra a forma da distribuição por frequências em classes; não evidencia diretamente quartis e mediana.
- Linha dentro da caixa = mediana, não média.

4. Atributo x métrica
- Atributo: característica descritiva do registro (partido, UF, tipo).
- Métrica: valor quantitativo agregado (contagem de proposições, média de dias).
- Uma coluna numérica não é automaticamente métrica (ex.: número do projeto é identificador/atributo).

5. Transformação x limpeza de dados
- Limpeza: corrige defeitos de qualidade (duplicatas, nulos, erros, formatos inconsistentes).
- Transformação: muda estrutura/conteúdo para análise (agregar, juntar, filtrar, derivar campo, normalizar).
- Padronizar grafias divergentes = limpeza; somar por mês = transformação. Na prática as etapas se misturam; a prova tende a usar o exemplo canônico.

6. Data Studio x Looker Studio
- Nome vigente: Data Studio. Verificado em 2026-10-08 no Google Cloud Blog (post "Looker Studio is Data Studio", datado "April 10, 2026"): "reintroducing a beloved and familiar name, Data Studio (formerly Looker Studio)". Fonte: https://cloud.google.com/blog/products/data-analytics/looker-studio-is-data-studio
- Looker Studio: nome anterior do mesmo produto, segundo o mesmo post ("formerly Looker Studio").
- Não confundir com "Looker" sozinho: o post descreve o Looker como plataforma de BI corporativa distinta ("Looker remains the enterprise BI platform" é paráfrase do conteúdo resumido; a frase literal não foi extraída com certeza: tratar como [SEM FONTE — não afirmar] até QA conferir).
- Páginas de suporte e documentação do Google não foram acessíveis em 2026-10-08; data efetiva de transição e novo domínio: [SEM FONTE — não afirmar].
- Em prova, aceitar os dois nomes como o mesmo produto; o edital usa "Data Studio".

---

# (d) 20 ITENS C/E AUTORAL

Julgue os itens a seguir. Rótulo de todos: AUTORAL.

A5-01 (7.1)
Julgue o item. Em uma base de dados de proposições legislativas, "partido do autor" é exemplo de atributo, enquanto "número de proposições apresentadas por mês" é exemplo de métrica.
Gabarito: C.
Justificativa: O partido qualifica o registro (atributo); a contagem mensal é valor quantitativo agregado (métrica).
Troca sutil: não.

A5-02 (7.1)
Julgue o item. A limpeza de dados consiste em agregar e derivar novos campos a partir dos dados existentes, como somar proposições por partido, com o objetivo de adequar a base à análise.
Gabarito: E.
Justificativa: Agregar e derivar campos é transformação de dados; limpeza corrige problemas de qualidade (duplicatas, ausentes, formatos).
Troca sutil: sim (limpeza no lugar de transformação).

A5-03 (7.1)
Julgue o item. A transformação de dados pode envolver operações como filtragem, junção de tabelas, agregação e criação de campos calculados.
Gabarito: C.
Justificativa: São operações típicas de transformação, que remodelam os dados para a análise.
Troca sutil: não.

A5-04 (7.1)
Julgue o item. Dados estruturados são aqueles que não seguem esquema predefinido, como textos livres de discursos parlamentares e arquivos de áudio de sessões.
Gabarito: E.
Justificativa: Texto livre e áudio são dados não estruturados; dados estruturados seguem esquema fixo, como tabelas.
Troca sutil: sim (estruturados no lugar de não estruturados).

A5-05 (8.1)
Julgue o item. Na visualização de dados, é recomendável destacar a mensagem principal e eliminar elementos decorativos que não carreguem informação, de modo a reduzir o ruído visual.
Gabarito: C.
Justificativa: Clareza e alta razão dados/tinta são princípios centrais de visualização.
Troca sutil: não.

A5-06 (8.1)
Julgue o item. Em gráfico de barras, iniciar o eixo vertical em valor diferente de zero é prática recomendada, pois amplia as diferenças entre as categorias sem comprometer a integridade da leitura.
Gabarito: E.
Justificativa: Como o comprimento da barra codifica o valor, truncar a base distorce a proporção; barras devem partir de zero.
Troca sutil: sim (recomendada no lugar de desaconselhada).

A5-07 (8.1)
Julgue o item. Para representar categorias sem ordem natural, como as unidades da Federação, recomenda-se paleta de cores sequencial, que sugere progressão de menor para maior valor.
Gabarito: E.
Justificativa: Categorias sem ordem pedem paleta qualitativa; a sequencial sugere magnitude ordenada.
Troca sutil: sim (sequencial no lugar de qualitativa).

A5-08 (8.2)
Julgue o item. O histograma representa a distribuição de frequências de uma variável quantitativa agrupada em classes, com barras adjacentes.
Gabarito: C.
Justificativa: O eixo horizontal é contínuo, por isso as barras se tocam e a altura indica a frequência da classe.
Troca sutil: não.

A5-09 (8.2)
Julgue o item. No histograma, as barras são separadas por espaços para indicar que as classes são categorias independentes, ao contrário do gráfico de barras, em que as barras são contíguas.
Gabarito: E.
Justificativa: A situação é inversa: histograma tem barras contíguas; gráfico de barras tem barras separadas.
Troca sutil: sim (inversão contíguas/separadas entre os dois gráficos).

A5-10 (8.2)
Julgue o item. O gráfico de linha é adequado para representar a evolução de uma variável ao longo do tempo, pois evidencia tendências e variações entre períodos sucessivos.
Gabarito: C.
Justificativa: A ligação entre pontos ordenados no tempo é a função típica do gráfico de linha.
Troca sutil: não.

A5-11 (8.2)
Julgue o item. O gráfico de dispersão exibe a relação entre duas variáveis quantitativas e, quando os pontos formam padrão linear, comprova que a variação de uma variável causa a variação da outra.
Gabarito: E.
Justificativa: O padrão indica correlação, que não comprova causalidade.
Troca sutil: sim (comprova causa no lugar de sugere correlação).

A5-12 (8.2)
Julgue o item. O box plot resume a distribuição de uma variável por meio de mediana, primeiro e terceiro quartis e extremos, permitindo ainda identificar valores atípicos e comparar grupos.
Gabarito: C.
Justificativa: A caixa vai de Q1 a Q3, a linha interna é a mediana e pontos isolados indicam outliers.
Troca sutil: não.

A5-13 (8.2)
Julgue o item. No box plot, a linha traçada no interior da caixa representa a média aritmética dos dados, e a caixa delimita o intervalo entre o mínimo e o máximo da variável.
Gabarito: E.
Justificativa: A linha interna é a mediana, e a caixa delimita Q1 a Q3, não mínimo e máximo.
Troca sutil: sim (média no lugar de mediana; a caixa como intervalo mínimo-máximo).

A5-14 (8.3)
Julgue o item. Segundo comunicado do Google Cloud datado de 10 de abril de 2026, o nome Data Studio foi reintroduzido para o produto antes denominado Looker Studio.
Gabarito: C.
Justificativa: O post "Looker Studio is Data Studio" fala em reintroduzir o nome Data Studio (formerly Looker Studio). Verificado em 2026-10-08 em https://cloud.google.com/blog/products/data-analytics/looker-studio-is-data-studio.
Troca sutil: não.

A5-15 (8.3)
Julgue o item. O nome Data Studio, reintroduzido pelo Google Cloud em abril de 2026, designa um produto distinto e sem relação com o anteriormente chamado Looker Studio.
Gabarito: E.
Justificativa: O próprio comunicado descreve Data Studio como "formerly Looker Studio", isto é, o mesmo produto com outro nome. Fonte verificada em 2026-10-08 (URL do A5-14).
Troca sutil: sim (produto distinto no lugar de mesmo produto renomeado).

A5-16 (8.3)
Julgue o item. Power BI, Tableau e Data Studio são ferramentas de visualização de dados listadas no edital para o tema de visualização de dados.
Gabarito: C.
Justificativa: O item 8.3 do edital cita exatamente essas três ferramentas.
Troca sutil: não.

A5-17 (8.3)
Julgue o item. O item 8.3 do edital trata de ferramentas de visualização de dados e cita Power BI, Tableau e Excel.
Gabarito: E.
Justificativa: A terceira ferramenta citada é o Data Studio, não o Excel.
Troca sutil: sim (Excel no lugar de Data Studio).

A5-18 (8.4)
Julgue o item. O storytelling para visualização de dados combina dados, elementos visuais e narrativa para comunicar uma mensagem e conduzir o público a uma conclusão ou ação.
Gabarito: C.
Justificativa: Essa é a definição essencial: dados, visual e narrativa a serviço de uma mensagem.
Troca sutil: não.

A5-19 (8.4)
Julgue o item. Na abordagem de storytelling, deve-se apresentar ao público todos os dados disponíveis e deixar que ele descubra por conta própria a mensagem principal, o que caracteriza a análise explanatória.
Gabarito: E.
Justificativa: Deixar o público descobrir é característica exploratória; a explanatória seleciona dados e explicita a mensagem.
Troca sutil: sim (explanatória no lugar de exploratória; mensagem não explicitada).

A5-20 (8.4)
Julgue o item. Em uma apresentação com storytelling, o uso de cor de destaque e de anotações para direcionar a atenção ao ponto-chave do gráfico contribui para a clareza da mensagem.
Gabarito: C.
Justificativa: Destaque e anotação guiam o olhar do público ao que sustenta a conclusão.
Troca sutil: não.

Contagem por subitem: 7.1 = 4 (A5-01 a 04); 8.1 = 3 (05 a 07); 8.2 = 6 (08 a 13); 8.3 = 4 (14 a 17); 8.4 = 3 (18 a 20).
Troca sutil: 10 itens (A5-02, 04, 06, 07, 09, 11, 13, 15, 17, 19). Gabaritos: 10 C e 10 E.
