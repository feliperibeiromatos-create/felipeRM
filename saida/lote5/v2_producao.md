# v2_producao.md — Lote 5 — 2026-10-08 — gerado por gcb-cpp

Escopo: itens 7.1 e 8.1 a 8.4 do edital (P1, comum aos 11 cargos). Rótulo de todos os itens C/E: AUTORAL.

# RESPOSTA AO QA1

Checklist do relatório (seções 1 a 6)

- 1. Cobertura, 8.3 sem conteúdo sobre Power BI e Tableau: acatado em parte. Reconheço a lacuna; as fontes oficiais seguem bloqueadas (reabertas em 2026-10-08: learn.microsoft.com e www.tableau.com retornaram EGRESS_BLOCKED). Mantido "[SEM FONTE — não afirmar]". Em 8.3 o curso passa a tratar a categoria "ferramenta de visualização" (conceito que independe de produto) e o Data Studio (com fonte). Cobertura parcial declarada.
- 1. Lacuna menor: nenhum item dedicado só ao gráfico de barras: não acatado. O próprio QA a considera aceitável; o gráfico de barras é cobrado por contraste em A5-06 e A5-09, e o limite de 6 itens em 8.2 está distribuído nos outros quatro tipos mais o par histograma × barras. Registrado.
- 1. Itens análogos TRF6 2024 não usados: acatado como registro. Não foram usados porque não tenho o texto oficial dos itens aberto nesta rodada; não afirmo conteúdo de prova sem fonte.
- 1. Cabeçalho "Cargo 11, P1" impreciso: acatado. Corrigido para "P1, comum aos 11 cargos".
- 2.1 Histograma, altura × área: acatado. Curso e item ajustados (classes de mesma amplitude: altura proporcional à frequência; amplitudes desiguais: a área é proporcional, e a altura representa a densidade de frequência).
- 2.2 Box plot, regra de Tukey, bigodes × mínimo/máximo, 50% centrais, quantitativa × categórica: acatado integralmente. Observo que 1,5·AIQ é convenção usual (Tukey) adotada por muitos softwares, não lei; o texto diz isso. Sem fonte de fornecedor, nada é afirmado sobre ferramenta específica.
- 2.3 Limpeza × transformação: acatado. Curso e par 5 reescritos: limpeza é tratada ora como etapa de preparação própria, ora como parte da transformação (o "T" de ETL); o candidato deve julgar pelo enunciado. A5-02 permanece correto.
- 2.4 "Barras separadas" como convenção de desenho: acatado. Texto do curso e do par 1 passa a dizer que é convenção visual; o critério conceitual é variável contínua em classes (histograma) × categorias (barras). Atenção: A5-09 foi reformulado para não depender só do espaçamento.
- 3. E1 título × manchete do post: acatado. Cito as duas: aba/URL "Looker Studio is Data Studio"; manchete "Data Studio returns as new home for Data Cloud assets". Reabri a URL em 2026-10-08 e a manchete e a data (April 10, 2026) conferem.
- 3. E2 trecho literal sobre o Looker: acatado. Substituí a paráfrase pelo trecho literal, confirmado na reabertura.
- 3. E3 "nasceu como Data Studio": acatado. Retirado; o post diz apenas "beloved and familiar name".
- 3. E4 Power BI e Tableau / encaminhar à Presidência: acatado. Pendência registrada ao final do texto (precisa de acesso oficial por outra via).
- 3. E5: sem ação; acatado.
- 5. Repetição de "Julgue o item." em cada item: acatado. Comando dado uma vez; itens só com a afirmação.
- 6. Condições 1 a 5: acatadas e atendidas conforme abaixo.

Itens AJUSTAR e REPROVADO

- A5-13 (AJUSTAR): acatado. Passa a ter uma só troca (média no lugar de mediana); a caixa delimita Q1 a Q3 corretamente no enunciado.
- A5-14 (REPROVADO): acatado. Novo A5-14 sem data de post nem autoria; cobra apenas que Data Studio é o nome do produto antes chamado Looker Studio. A fonte fica na justificativa.
- A5-15 (AJUSTAR): acatado. Âncora "abril de 2026" retirada; troca única mantida (produto distinto × mesmo produto).
- A5-16 (REPROVADO): acatado. Metaitem sobre o edital eliminado; novo item é conceitual sobre a categoria de ferramenta (painel que reúne visuais de fontes conectadas), sem afirmar recurso de produto.
- A5-17 (REPROVADO): acatado. Novo item de 8.3 com troca única de conceito: a ferramenta não dispensa o critério de escolha do gráfico.
- A5-19 (AJUSTAR): acatado. Reescrito com uma só troca (exploratória × explanatória) e demais elementos verdadeiros.
- Os demais 14 itens (APROVADO): sem alteração de mérito; A5-08 e A5-12 receberam ajuste de redação pelos pontos 2.1 e 2.2; "Julgue o item." removido.

---

# (a) CURSO

## NOTA DE EVIDÊNCIA
- URL aberta com sucesso em 2026-10-08 e que sustenta afirmação: https://cloud.google.com/blog/products/data-analytics/looker-studio-is-data-studio (Google Cloud Blog, fornecedor do produto).
- URLs tentadas e bloqueadas (EGRESS_BLOCKED) em 2026-10-08: https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview e https://www.tableau.com/why-tableau/what-is-tableau.
- Consequência: sobre Power BI e Tableau, recursos, versões, preços e limites ficam "[SEM FONTE — não afirmar]". Do edital sabe-se apenas que são ferramentas de visualização cobradas no item 8.3.

## 7.1 Conceitos, atributos, métricas, transformação de dados

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

## 8.1 Princípios de visualização de dados

Definição precisa
- Objetivo: traduzir dados em representações visuais que facilitem percepção, comparação e decisão.
- Princípios usuais: clareza e foco na mensagem; gráfico adequado ao tipo de dado e à pergunta; razão dados/tinta alta (eliminar ruído e decoração sem informação); integridade gráfica (escalas honestas; barras partem de zero; evitar distorção de proporções); uso funcional da cor (paleta qualitativa para categorias, sequencial para magnitude ordenada, divergente para desvios em torno de um ponto central; atenção ao daltonismo); rotulagem clara (título, eixos, unidades, fonte); hierarquia visual e consistência; acessibilidade.
- Atributos pré-atentivos (posição, comprimento, cor, tamanho) permitem leitura rápida; posição e comprimento são percebidos com mais precisão que área ou ângulo.

Exemplo aplicado
- Painel de execução orçamentária de um órgão legislativo: barras ordenadas por valor, eixo iniciando em zero, uma cor de destaque para a rubrica em foco e cinza para as demais.

Pegadinha provável
- Afirmar que truncar o eixo de barras é boa prática para realçar diferenças; dizer que mais cores e efeitos 3D aumentam a clareza; usar paleta sequencial para categorias sem ordem.

## 8.2 Tipos de gráficos

### Histograma
- Definição: mostra a distribuição de frequência de uma variável quantitativa dividida em classes (intervalos) contíguas. Como o eixo horizontal é uma escala numérica contínua, as barras são adjacentes. Com classes de mesma amplitude, a altura da barra é proporcional à frequência. Com classes de amplitudes desiguais, a área da barra é que deve ser proporcional à frequência, e a altura passa a representar a densidade de frequência (frequência dividida pela amplitude da classe). Altura e área não são equivalentes em geral.
- Exemplo: distribuição do tempo de tramitação (em dias) de proposições.
- Pegadinha: tratá-lo como gráfico de barras de categorias; dizer que a ordem das classes é intercambiável; tratar altura e área como sempre equivalentes.

### Gráfico de linha
- Definição: liga pontos sucessivos para mostrar a evolução de uma variável, tipicamente no tempo (eixo horizontal ordenado). Destaca tendência, sazonalidade e variações.
- Exemplo: número mensal de requerimentos de informação ao longo de uma legislatura.
- Pegadinha: confundir com dispersão; usar linha para categorias sem ordem.

### Gráfico de barras
- Definição: compara valores entre categorias discretas; o comprimento da barra é proporcional ao valor e a base é em zero. Pode ser horizontal ou vertical, agrupado ou empilhado. O espaçamento entre barras é convenção de desenho que reforça tratar-se de categorias; o critério conceitual é a natureza da variável (categórica), não o espaço.
- Exemplo: quantidade de projetos por comissão.
- Pegadinha: confundir com histograma; aceitar eixo truncado; usar para distribuição de variável contínua agrupada em classes.

### Gráfico de dispersão
- Definição: cada ponto é uma observação com coordenadas em duas variáveis quantitativas; revela relação, padrão, agrupamentos e outliers. Correlação visível não prova causalidade.
- Exemplo: gasto de gabinete versus número de proposições por parlamentar.
- Pegadinha: afirmar que mostra causa e efeito; confundir com linha; dizer que exige variável categórica.

### Box plot (diagrama de caixa)
- Definição: resume a distribuição de uma variável quantitativa. A caixa vai do 1º quartil (Q1) ao 3º quartil (Q3), ou seja, contém os 50% centrais dos dados; a amplitude da caixa é o intervalo interquartil (AIQ = Q3 − Q1). A linha interna é a mediana (não a média).
- Bigodes e outliers (regra usual de Tukey, adotada como convenção por muitos programas, mas que pode variar): calculam-se limites em Q1 − 1,5·AIQ e Q3 + 1,5·AIQ; os bigodes vão até o dado mais extremo que ainda esteja dentro desses limites, e os pontos fora deles são marcados individualmente como outliers. Logo, quando há outliers, os bigodes não terminam no mínimo e no máximo da amostra; só terminam neles quando não há valores atípicos.
- Comparação entre grupos: a variável resumida é quantitativa; os grupos são categorias de uma variável categórica (ex.: uma caixa por comissão). Não mostra a forma detalhada da distribuição (como bimodalidade), que o histograma mostra.
- Exemplo: comparar a distribuição de prazos de análise entre comissões.
- Pegadinha: dizer que a linha central é a média; que a caixa vai do mínimo ao máximo; que a caixa contém todos os dados; que mostra a forma detalhada como o histograma.

## 8.3 Ferramentas de visualização de dados (Power BI, Tableau e Data Studio)

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

## 8.4 Storytelling para visualização de dados

Definição precisa
- Storytelling com dados: combinação de dados, visuais e narrativa para comunicar uma mensagem e conduzir o público a uma conclusão ou ação.
- Estrutura narrativa clássica: contexto (público e o que está em jogo), conflito ou problema (o que os dados revelam), resolução ou chamada à ação (o que fazer).
- Práticas: conhecer o público; definir a mensagem principal ("big idea") antes de escolher gráficos; usar destaque (cor, anotação, título que afirma a conclusão) para guiar a atenção; remover ruído; ordenar a sequência para que cada visual sustente o ponto seguinte; diferenciar análise exploratória (o analista descobre) de explanatória (o público é conduzido a uma mensagem já definida).

Exemplo aplicado
- Apresentação à Mesa Diretora sobre atraso na tramitação: título "Prazo médio de análise dobrou em dois anos", gráfico de linha com o ponto de inflexão anotado e recomendação final.

Pegadinha provável
- Dizer que storytelling é apenas enfeitar o gráfico ou dispensa mensagem explícita; inverter exploratória e explanatória; sugerir mostrar todos os dados em vez de selecionar o que sustenta a mensagem.

---

# (b) RESUMO (uma página)

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

# (c) PARES CONFUNDÍVEIS

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

---

# (d) 20 ITENS C/E AUTORAL

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

Contagem por subitem: 7.1 = 4 (A5-01 a 04); 8.1 = 3 (05 a 07); 8.2 = 6 (08 a 13); 8.3 = 4 (14 a 17); 8.4 = 3 (18 a 20).
Troca sutil de conceito único: 10 itens (A5-02, 04, 06, 07, 09, 11, 13, 15, 17, 19). Gabaritos: 10 C (01, 03, 05, 08, 10, 12, 14, 16, 18, 20) e 10 E.

PENDÊNCIA PARA A PRESIDÊNCIA: a cobertura de Power BI e Tableau em 8.3 só fecha com fonte oficial acessível (liberação de rede para learn.microsoft.com, powerbi.microsoft.com, tableau.com e help.tableau.com, ou material oficial anexado ao repositório). Até lá, cobertura parcial declarada.
