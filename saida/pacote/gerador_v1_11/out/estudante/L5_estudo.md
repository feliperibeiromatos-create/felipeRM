# Lote 5 — TID-DADOS-VIZ (P1 7.1 e 8.1–8.4)

Prova: P1

## Itens do edital

- P1-7.1 — Conceitos, atributos, métricas, transformação de dados
- P1-8.1 — Princípios de visualização de dados
- P1-8.2 — Tipos de gráficos (histograma, linha, barra, dispersão, box plot)
- P1-8.3 — Ferramentas de visualização de dados (Power BI, Tableau e Data Studio)
- P1-8.4 — Storytelling para visualização de dados

## Resumo

```text
NOTA DO EDITAL (8.11.2): na prova objetiva, cada item vale +1,00 ponto se a marcação concordar com o gabarito oficial definitivo, −1,00 ponto se discordar e 0,00 se não houver marcação ou houver marcação dupla (C e E) (Edital nº 1/2026, subitem 8.11.2).

7.1 DADOS. Dado (bruto) → informação (organizado) → conhecimento (aplicado). Estruturado (esquema fixo) / semiestruturado (XML, JSON) / não estruturado (texto livre, áudio, vídeo). Qualitativo (nominal, ordinal) × quantitativo (discreto, contínuo; escalas intervalar e de razão). Atributo = coluna/variável; registro = linha; chave identifica; derivado é calculado; não confundir atributo com seu valor. Métrica = agregado numérico (contagem, soma, média, mediana, moda, desvio padrão, percentil); dimensão = atributo de segmentação; KPI = métrica com meta. Média sensível a extremos; mediana robusta; moda vale para nominal. Transformação: agregar, filtrar, juntar, pivotar, discretizar, codificar, normalizar (reescala) e padronizar (média 0, desvio 1), derivar, anonimizar. Limpeza = corrigir qualidade (duplicatas, nulos, erros, formatos); sua classificação (etapa própria ou parte do "T" de ETL) diverge na literatura; o ponto seguro: limpeza corrige qualidade; agregar e derivar não é limpar. ETL transforma antes da carga; ELT, depois.

8.1 PRINCÍPIOS. Pergunta antes do gráfico. Integridade: barras desde zero; evitar lie factor, chartjunk e 3D; maximizar dados/tinta. Percepção: posição > comprimento > ângulo > área > cor. Paleta qualitativa (categorias sem ordem), sequencial (magnitude), divergente (desvio de um centro); daltonismo. Título afirmativo, eixos com unidade, poucos elementos, escalas consistentes, acessibilidade.

8.2 GRÁFICOS. Histograma: variável quantitativa em classes adjacentes de escala numérica → barras contíguas e ordem fixa; mesma amplitude → altura ∝ frequência; amplitudes desiguais → área ∝ frequência (altura = densidade). Linha: evolução em eixo ordenado (tempo), tendência. Barras: comparação entre categorias; base em zero; agrupado/empilhado; espaçamento entre barras é convenção de desenho. Dispersão: relação entre duas quantitativas; correlação ≠ causalidade; bolhas = 3ª variável. Box plot: caixa Q1–Q3 (50% centrais, AIQ); linha = mediana; bigodes, por lado, até o dado mais extremo dentro de Q1 − 1,5·AIQ e Q3 + 1,5·AIQ; além, outliers; compara grupos; não mostra média nem forma detalhada.

8.3 FERRAMENTAS (informação sujeita a mudança; verificado em 8/10/2026). Power BI: Desktop (Windows, criação de relatórios, download gratuito, Power Query Editor) → publica no serviço (organizar, gerenciar, distribuir; permite criar dashboards); Mobile = consumo. Tableau: Desktop (criação; dashboards), Cloud (hospedado pela Tableau), Server (auto-hospedado; vários sites), Prep (preparação), Mobile (interage com Server/Cloud), Public (gratuito e público). Data Studio: nome vigente; foi Looker Studio de 11/10/2022 a abril de 2026; datastudio.google.com; edição Data Studio sem custo e edição paga Pro; Looker ≠ Data Studio. A ferramenta pode sugerir ou gerar visuais; a adequação do gráfico é do analista. Não verificados, sem afirmação: DAX, Report Server, versões, licenças, preços, limites, macOS.

8.4 STORYTELLING. Dados + visual + narrativa; uma mensagem central e chamada à ação; contexto → conflito → resolução; público primeiro; eliminar ruído; dirigir a atenção (cor, anotação, título afirmativo); explanatória (conduz) × exploratória (descobre); não é dashboard, não é decoração.
```

## Curso

```text
## ITEM 7.1 — DADOS: CONCEITOS, ATRIBUTOS, MÉTRICAS, TRANSFORMAÇÃO

### 7.1.1 CONCEITOS
- Dado é o registro bruto de um fato ("Projeto de Lei nº X, autor Y, apresentado em tal data"; "Deputado X falou 7 minutos em 3/9"). Informação é o dado organizado e interpretado em contexto ("a média de fala por deputado foi 5 min"). Conhecimento é a informação aplicada a uma decisão.
- Quanto à estrutura: dado estruturado (tabela com esquema fixo, linhas e colunas — planilha de proposições); semiestruturado (XML/JSON com marcação, como os dados abertos da Câmara); não estruturado (texto livre de notas taquigráficas, áudio e vídeo de sessões).
- Quanto à natureza: qualitativo (categorias: partido, UF, tipo de proposição) ou quantitativo (números: tempo de fala, número de emendas). O quantitativo é discreto (contagem: nº de emendas) ou contínuo (medida: duração em segundos).
- Escalas de medida: nominal (sem ordem: partido); ordinal (ordem sem distância definida: urgência baixa/média/alta); intervalar (distâncias iguais, zero arbitrário: temperatura em °C); de razão (zero absoluto: duração, valor em reais).
- Exemplo aplicado: na base de proposições, "tipo" (PL, PEC, MPV) é nominal; "regime de tramitação" pode ser tratado como ordinal; "número de pareceres" é discreto; "tempo até a aprovação" é contínuo.
- Pegadinha provável: calcular média de variável nominal ("partido médio"); tratar escala ordinal como se as distâncias entre níveis fossem iguais; chamar "informação" de "dado bruto"; afirmar que dados estruturados são os "sem esquema".

### 7.1.2 ATRIBUTOS
- Em dado tabular, atributo = coluna = variável = campo; registro = linha = instância. Cada atributo tem tipo (texto, inteiro, decimal, data, booleano) e domínio (valores admitidos). Pode ser categórico (nominal ou ordinal) ou numérico.
- Chave é o atributo (ou conjunto de atributos) que identifica unicamente o registro (número + ano da proposição). Atributo derivado é calculado a partir de outros (idade a partir da data de nascimento).
- Dimensão × métrica: dimensões são os atributos pelos quais se fatia a análise; métricas são o que se mede.
- Exemplo aplicado: na tabela de deputados, o identificador de cadastro é chave; "idade" deriva de "data de nascimento"; "sigla do partido" é atributo nominal.
- Pegadinha provável: confundir o atributo (a coluna "UF") com o valor do atributo ("DF"); afirmar que todo atributo precisa ser único; trocar atributo por métrica (dizer que "UF do autor" é métrica).

### 7.1.3 MÉTRICAS
- Métrica (medida) é valor quantitativo mensurável, em geral resultado de agregação: contagem, soma, média, mediana, moda, mínimo, máximo, desvio padrão, percentis, proporções e taxas. Dimensão é o atributo pelo qual a métrica é segmentada (métrica "nº de proposições" por dimensão "partido"). KPI é a métrica escolhida para monitorar um objetivo, com meta e período.
- Tendência central: média (sensível a valores extremos); mediana (valor do meio; robusta a extremos); moda (valor mais frequente; única aplicável a dado nominal). Dispersão: amplitude, variância, desvio padrão, intervalo interquartil (AIQ = Q3 − Q1).
- Exemplo aplicado: tempo de tramitação de PLs: um PL de 20 anos puxa a média para cima; a mediana descreve melhor o "PL típico". "Quantidade de proposições por mês" é métrica; "partido do autor" é atributo/dimensão.
- Pegadinha provável: inverter média e mediana quanto à sensibilidade a extremos; chamar dimensão de métrica; dizer que coluna numérica é automaticamente métrica (o número do projeto é identificador); afirmar que a média é a medida válida para dado ordinal (são a mediana e a moda).

### 7.1.4 TRANSFORMAÇÃO DE DADOS
- Transformar é alterar forma, escala, conteúdo ou estrutura dos dados para adequá-los à análise. Operações típicas: agregação (somar por mês), filtragem, junção (join por chave), pivotagem (linhas ↔ colunas), discretização/binning (contínuo → faixas), codificação (categoria → número, ex.: one-hot), normalização (reescalar para um intervalo, ex.: 0–1) e padronização (média 0, desvio 1), conversão de tipos, campos calculados/derivação, anonimização/pseudonimização.
- Limpeza de dados: correção de problemas de qualidade — duplicatas, valores ausentes, erros de digitação, formatos inconsistentes. A classificação da limpeza diverge na literatura: alguns a tratam como etapa de preparação própria, anterior à análise; outros, como uma das operações da etapa de transformação (o "T" de ETL). O ponto seguro é: limpeza corrige qualidade; agregar e derivar não é limpar.
- ETL × ELT: no fluxo ETL (extrair, transformar, carregar), a transformação precede a carga; no ELT, ocorre após a carga, no destino.
- Exemplo aplicado: padronizar "PL", "P.L." e "Projeto de Lei" é limpeza; somar proposições por partido é transformação (agregação); para comparar tempo de fala entre comissões de tamanhos diferentes, calcula-se o tempo por membro (derivação) e agrega-se por mês (agregação).
- Pegadinha provável: definir normalização como "remoção de duplicatas" (é limpeza); chamar de "limpeza" uma agregação; inverter ETL e ELT; usar normalização e padronização como sinônimos em item que exige a distinção.

## ITEM 8.1 — PRINCÍPIOS DE VISUALIZAÇÃO DE DADOS

Definição precisa
- Objetivo: traduzir dados em representações visuais que facilitem percepção, comparação e decisão. A visualização responde a uma pergunta; o tipo de gráfico decorre da natureza do dado (categórico × quantitativo; um momento × série temporal; distribuição × relação).
- Princípios usuais: clareza e foco na mensagem; gráfico adequado ao tipo de dado e à pergunta; razão dados/tinta alta (eliminar ruído, decoração e "chartjunk" — 3D, sombras — termos associados a Tufte); integridade gráfica (escalas honestas; barras partem de zero; evitar distorção de proporções — o "lie factor" de Tufte é a razão entre o efeito visual e o efeito nos dados); uso funcional da cor (paleta qualitativa/categórica para categorias, sequencial para magnitude ordenada, divergente para desvios em torno de um ponto central; atenção ao daltonismo); rotulagem clara (título, eixos, unidades, fonte); hierarquia visual e consistência de escalas entre painéis; acessibilidade.
- Percepção: atributos pré-atentivos (posição, comprimento, cor, tamanho) permitem leitura rápida. Segundo os estudos de percepção visual (Cleveland e McGill), a precisão de leitura segue a ordem posição em escala comum > comprimento > ângulo/inclinação > área > volume/cor; daí barras serem lidas com mais exatidão que pizzas. Princípios de Gestalt (proximidade, similaridade, fechamento) guiam os agrupamentos visuais.

Exemplo aplicado
- Painel de execução orçamentária de um órgão legislativo: barras ordenadas por valor, eixo iniciando em zero, uma cor de destaque para a rubrica em foco e cinza para as demais; para "evolução mensal de sessões", linha; evitar pizza com 20 comissões.

Pegadinha provável
- Afirmar que truncar o eixo de barras é boa prática para realçar diferenças; dizer que mais cores e efeitos 3D aumentam a clareza; usar paleta sequencial ou divergente para categorias sem ordem; afirmar que área ou cor comparam com mais precisão que posição; dizer que pizza é adequada para muitas categorias ou para evolução no tempo.

## ITEM 8.2 — TIPOS DE GRÁFICOS

Histograma
- Definição: mostra a distribuição de frequência de uma variável quantitativa (contínua, ou discreta com muitos valores) dividida em classes (intervalos) adjacentes de uma escala numérica. Por isso as barras são contíguas e a ordem das classes é fixa. Com classes de mesma amplitude, a altura da barra é proporcional à frequência. Com classes de amplitudes desiguais, a ÁREA da barra é que deve ser proporcional à frequência, e a altura passa a representar a densidade de frequência (frequência dividida pela amplitude da classe). Altura e área não são equivalentes em geral. Permite ver forma (simétrica, assimétrica), centro, dispersão, modas e outliers; o número de classes altera a aparência.
- Exemplo: distribuição do tempo de tramitação (em dias) de proposições; duração dos discursos em faixas de 2 minutos.
- Pegadinha: tratá-lo como gráfico de barras de categorias; dizer que a ordem das classes é intercambiável; tratar altura e área como sempre equivalentes; usar histograma para categorias nominais.

Gráfico de linha
- Definição: liga pontos sucessivos para mostrar a evolução de uma variável ao longo de um eixo horizontal ordenado, tipicamente o tempo. Destaca tendência, sazonalidade e variações; várias séries podem ser comparadas, com cuidado com o número de linhas.
- Exemplo: número mensal de requerimentos de informação ao longo de uma legislatura.
- Pegadinha: confundir com dispersão; usar linha para categorias sem ordem (partidos, comissões), o que sugere continuidade inexistente.

Gráfico de barras (colunas)
- Definição: compara valores entre categorias discretas; o comprimento da barra é proporcional ao valor e a base é em zero. Vertical (colunas) ou horizontal (melhor para rótulos longos); agrupado (subcategorias lado a lado) ou empilhado (partes de um total). No gráfico de barras, o espaçamento entre as barras é convenção de desenho; o que o distingue conceitualmente do histograma é a natureza da variável: categórica aqui, quantitativa em classes adjacentes de uma escala numérica no histograma (daí as barras contíguas deste). Ordenar por valor facilita a leitura quando não há ordem natural.
- Exemplo: quantidade de projetos por comissão; proposições por partido.
- Pegadinha: confundir com histograma; aceitar eixo truncado; usar para distribuição de variável contínua agrupada em classes; empilhado quando se quer comparar as partes entre si.

Gráfico de dispersão
- Definição: cada ponto é uma observação com coordenadas em duas variáveis quantitativas; revela relação (direção, força, forma), agrupamentos e outliers. Pode receber linha de tendência; o gráfico de bolhas acrescenta uma terceira variável no tamanho. Correlação visível não prova causalidade.
- Exemplo: gasto de gabinete versus número de proposições por parlamentar.
- Pegadinha: afirmar que mostra causa e efeito; confundir com linha; dizer que exige variável categórica em um dos eixos.

Box plot (diagrama de caixa)
- Definição: resume a distribuição de uma variável quantitativa. A caixa vai do 1º quartil (Q1) ao 3º quartil (Q3), ou seja, contém os 50% centrais dos dados; a amplitude da caixa é o intervalo interquartil (AIQ = Q3 − Q1). A linha interna é a mediana (não a média; a média só aparece com marcação extra).
- Bigodes e outliers (regra usual de Tukey, adotada como convenção por muitos programas, mas que pode variar): calculam-se os limites Q1 − 1,5·AIQ e Q3 + 1,5·AIQ; cada bigode vai até o dado mais extremo DO SEU LADO que ainda esteja dentro do limite respectivo, e os pontos além dos limites são marcados individualmente como outliers. A regra vale por lado: um outlier superior não impede que o bigode inferior termine no mínimo da amostra. Logo, os bigodes só coincidem com o mínimo e o máximo quando não há outliers daquele lado. O fator 1,5·AIQ é a convenção usual (Tukey); outras convenções existem e a prova costuma cobrar esta.
- Comparação entre grupos: a variável resumida é quantitativa; os grupos são categorias de uma variável categórica (uma caixa por comissão). Não mostra a forma detalhada da distribuição (bimodalidade), que o histograma mostra.
- Exemplo: comparar a distribuição de prazos de análise entre comissões.
- Pegadinha: dizer que a linha central é a média; que a caixa vai do mínimo ao máximo ou contém todos os dados; que os bigodes vão até 1,5 desvio padrão; que mostra frequência por intervalo (isso é histograma).

## ITEM 8.3 — FERRAMENTAS DE VISUALIZAÇÃO DE DADOS (POWER BI, TABLEAU E DATA STUDIO) — informação sujeita a mudança

Definição precisa (categoria)
- Ferramenta de visualização de dados é software para conectar fontes de dados, construir visuais, reuni-los em painéis (dashboards) e compartilhar análises. A ferramenta pode sugerir ou gerar visuais, mas a adequação do gráfico ao dado e à pergunta é responsabilidade do analista (princípios de 8.1 e escolha de 8.2). Menção sujeita a mudança: o Data Studio Pro oferece, em Preview, o recurso Code Interpreter, que "translates natural language questions into Python code to provide advanced analysis and visualizations" (CI, verificado em 8/10/2026) — exemplo de ferramenta que gera visualizações; o recurso não é objeto de item.

Power BI (Microsoft) — fonte principal Microsoft Learn, "Using Power BI" (versão en-us); Microsoft Learn, módulo Dynamics 365 Business Central, página de instalação do Power BI Desktop, só para a natureza Windows do Desktop (verificado em 8/10/2026)
- Três componentes ("There are three primary components to Power BI"): Power BI Desktop (aplicativo de desktop), serviço do Power BI (plataforma on-line) e Power BI Mobile (aplicativo móvel multiplataforma) (Microsoft Learn, "Using Power BI").
- Power BI Desktop: "the development tool available to data analysts and other report creators" (Microsoft Learn, "Using Power BI"); "a Microsoft Windows desktop application called Power BI Desktop" (Microsoft Learn, módulo Dynamics 365 Business Central, página de instalação do Power BI Desktop); "available to download for free either through the Windows store or as a direct installer" (Microsoft Learn, "Using Power BI"); "Transform data with Power Query Editor (comes with Power BI Desktop)" (Microsoft Learn, "Using Power BI").
- Serviço do Power BI: "allows you to organize, manage, and distribute your reports and other Power BI items"; "also allows you to create high-level dashboards that drill down to reports" (Microsoft Learn, "Using Power BI").
- Fluxo típico: "First, you start with Power BI Desktop to connect to data and create the report. Then you publish the report to the Power BI service and distribute to consumers" (Microsoft Learn, "Using Power BI"). O fluxo documentado encerra no serviço; o Mobile é consumo.
- Não verificados, sem afirmação: DAX, Report Server, versões, licenças, preços, limites, execução em macOS (o silêncio da fonte não é base para item).
- Pegadinha: inverter o fluxo (criar no serviço, publicar no Desktop); dizer que o Desktop é pago; dizer que o serviço não permite criar dashboards.

Tableau (Salesforce) — Tableau Help, "Tableau product overview"; dashboards por Trailhead (Salesforce), "Data Presentation and Publication in Tableau Desktop" / "Build a Dashboard" (verificado em 8/10/2026)
- Família de produtos (Tableau Help, "Tableau product overview"): Tableau Desktop (criação e análise); Tableau Cloud — "A fully hosted cloud-based enterprise-grade analytics platform"; Tableau Server — "A self-hosted platform, either on-premises or in a public cloud", e "Tableau Server can have multiple sites"; Tableau Prep — "combining, shaping, and cleaning data"; Tableau Mobile — "interacts with visualizations on your Tableau Server or Tableau Cloud site"; Tableau Public — "A free platform to explore, create, and publicly share data visualizations online".
- Dashboards: no Tableau Desktop, "By combining your views into an interactive dashboard, your stakeholders can compare a variety of data simultaneously" (Trailhead (Salesforce), módulo "Data Presentation and Publication in Tableau Desktop").
- Não verificados, sem afirmação: versões e preços.
- Pegadinha: trocar Cloud (hospedado pela Tableau) por Server (hospedado pelo cliente); dizer que o Tableau Public é privado ou pago.

Data Studio (Google) — Google Cloud, Data Studio, página "Welcome"; Google Cloud, notas de versão do Data Studio (16/04/2026); Google Cloud Blog, 10/04/2026 ("Data Studio (formerly Looker Studio)"); Google Cloud Blog, 11/10/2022 ("And starting today, Data Studio is now Looker Studio.") (verificado em 8/10/2026)
- Nome vigente: Data Studio (Google Cloud, Data Studio, página "Welcome"; Google Cloud, notas de versão do Data Studio (16/04/2026); Google Cloud Blog, 10/04/2026 ("Data Studio (formerly Looker Studio)")). Histórico: lançado como Data Studio; em 11/10/2022 passou a chamar-se Looker Studio — Google Cloud Blog, 11/10/2022 ("And starting today, Data Studio is now Looker Studio."); em abril de 2026 voltou a chamar-se Data Studio — anúncio do Google Cloud Blog, 10/04/2026 ("Data Studio (formerly Looker Studio)"); Google Cloud, notas de versão do Data Studio (16/04/2026), "We've rebranded Looker Studio as Data Studio"; Google Cloud, Data Studio, página "Welcome": "In April 2026, the Looker Studio product name returned to its original name: Data Studio". Não se afirma dia exato da mudança de 2026. Endereço: https://datastudio.google.com/ ; lookerstudio.google.com redireciona (Google Cloud, Data Studio, página "Welcome").
- O que é: "turns your data into informative, shareable, and fully customizable dashboards and reports" (Google Cloud, Data Studio, página "Welcome"); "personal data exploration", "ad-hoc reports", dados do ecossistema Google "from BigQuery to Google Sheets and Ads" (Google Cloud Blog, 10/04/2026 ("Data Studio (formerly Looker Studio)")).
- Edições: a edição Data Studio é sem custo ("no-cost", Google Cloud, Data Studio, página "Welcome"); existe a edição paga Data Studio Pro (Google Cloud, Data Studio, página "Welcome", seção "Upgrade to Data Studio Pro"; Google Cloud Blog, 10/04/2026 ("Data Studio (formerly Looker Studio)"): "Data Studio Pro is designed for scaling teams"; anunciada como Looker Studio Pro em 11/10/2022, segundo o Google Cloud Blog). Preço da Pro: não verificado. Não se deve dizer apenas "o Data Studio é gratuito".
- Looker (plataforma): "Looker as our enterprise business intelligence platform"; o Data Studio evolui "to complement the Looker platform, independently" (Google Cloud Blog, 10/04/2026 ("Data Studio (formerly Looker Studio)")). Produto distinto do Data Studio/Looker Studio.
- Pegadinha: afirmar que "o Data Studio foi descontinuado e substituído pelo Looker Studio" (foi renomeado, e o nome voltou em abril de 2026); confundir Data Studio com Looker; tratar Looker Studio e Data Studio como produtos diferentes; atribuir à ferramenta a responsabilidade pela adequação do gráfico (a ferramenta pode sugerir ou gerar visuais, mas a adequação ao dado e à pergunta é do analista); misturar com Excel/Office (item 1 do edital, MSOffice 365, fora do escopo dos itens 7 e 8 de TI e Dados).

Exemplo aplicado
- Uma consultoria legislativa reúne em um painel os visuais de proposições por tema, tipo e mês. No Power BI, o fluxo documentado é criar o relatório no Power BI Desktop e publicá-lo no serviço, de onde é distribuído aos consumidores (Microsoft Learn, "Using Power BI"). No Tableau e no Data Studio, o painel é construído e compartilhado com os produtos de cada família, sem que o curso do tópico 8.3 de TI e Dados afirme um fluxo específico. Em qualquer ferramenta, a escolha de barras para "por tema" e de linha para "por mês" é responsabilidade do analista, ainda que a ferramenta sugira ou gere visuais.

## ITEM 8.4 — STORYTELLING PARA VISUALIZAÇÃO DE DADOS

Definição precisa
- Storytelling com dados: combinação de três elementos — dados, elementos visuais e narrativa (tríade associada a Dykes) — para comunicar uma mensagem e conduzir o público a uma conclusão ou ação. Difere do dashboard (exploração aberta, muitos indicadores) e de "muitos gráficos": o storytelling tem uma mensagem central.
- Estrutura narrativa: contexto (público e o que está em jogo), conflito ou problema (o que os dados revelam), resolução ou chamada à ação (o que fazer).
- Método (associado a Knaflic): entender o contexto (quem é o público, o que precisa saber, o que deve fazer); definir a mensagem principal antes de escolher gráficos; escolher a visualização adequada; eliminar o desnecessário (ruído); dirigir a atenção (cor, contraste, tamanho, posição, anotações; título que afirma a conclusão); pensar como designer (hierarquia, alinhamento); ordenar a sequência para que cada visual sustente o ponto seguinte. Diferenciar análise exploratória (o analista investiga para descobrir) de explanatória (o público é conduzido a uma mensagem já definida).

Exemplo aplicado
- Apresentação à Mesa Diretora sobre atraso na tramitação: título "Prazo médio de análise dobrou em dois anos", gráfico de linha com o ponto de inflexão anotado, série relevante em cor forte e as demais em cinza, recomendação final.

Pegadinha provável
- Dizer que storytelling é apenas enfeitar o gráfico ou dispensa mensagem explícita; inverter exploratória e explanatória; sugerir mostrar o máximo de métricas para o público concluir sozinho; dizer que narrativa dispensa dados; usar dashboard e storytelling como sinônimos.
```

## Pares

- C1. **Histograma** × **gráfico de barras** | variável quantitativa em classes adjacentes de escala numérica; barras contíguas; ordem fixa; mostra distribuição | categorias discretas; ordem livre; compara valores; espaçamento entre barras é convenção de desenho | chama histograma de "barras"; pede histograma para partidos. Teste: o eixo horizontal é escala numérica dividida em intervalos? Histograma.
- C2. **Linha** × **dispersão** | pontos ligados em eixo ordenado (tempo); evolução | pontos soltos de duas quantitativas; relação, agrupamentos, outliers | linha para categorias; dispersão "para ver evolução".
- C3. **Box plot** × **histograma** | quartis, mediana, bigodes, outliers; compara grupos; esconde forma detalhada | frequência por classe; mostra forma e modas; não evidencia quartis | diz que box plot mostra frequência por faixa; que a linha é a média; que os bigodes vão sempre ao mínimo e ao máximo.
- C4. **Média** × **mediana** | sensível a extremos | robusta; valor central | inverte a sensibilidade.
- C5. **Atributo** × **métrica (dimensão × medida)** | coluna que descreve/segmenta (partido) | número agregado (total de PLs) | chama "partido" de métrica; toma coluna numérica (número do projeto) por métrica.
- C6. **Transformação** × **limpeza** | muda forma/escala/estrutura (agregar, normalizar, derivar) | corrige erros, nulos, duplicatas, formatos | define normalização como remoção de duplicatas; "limpeza é agregar". A classificação da limpeza diverge na literatura; o ponto seguro: limpeza corrige qualidade; agregar e derivar não é limpar.
- C7. **Normalização** × **padronização** | reescala para intervalo (0–1) | média 0 e desvio 1 (z-score) | usa como sinônimos em item que exige distinção.
- C8. **ETL** × **ELT** | transforma antes da carga | transforma depois, no destino | inverte a ordem.
- C9. **Paleta sequencial** × **divergente × categórica** | intensidade crescente | afastamento de um centro | categorias sem ordem | divergente ou sequencial para partidos.
- C10. **Posição** × **área/cor** | leitura mais precisa | leitura menos precisa | afirma que área ou cor compara melhor.
- C11. **Data Studio** × **Looker Studio × Looker** | nome vigente desde abril de 2026 (edição Data Studio, sem custo; existe a edição paga Pro) | nome do mesmo produto entre 11/10/2022 e abril de 2026 | plataforma de BI corporativa, produto distinto | "Data Studio foi descontinuado/substituído"; Looker = Data Studio.
- C12. **Tableau Cloud** × **Tableau Server** | hospedado pela Tableau | hospedado pelo cliente (on-premises ou nuvem pública) | inverte quem hospeda.
- C13. **Power BI Desktop** × **serviço do Power BI** | cria o relatório (aplicativo Windows, download gratuito) | publica, organiza, distribui; permite criar dashboards | diz que se cria no serviço e publica no Desktop; que o Desktop é pago.
- C14. **Storytelling** × **dashboard** | mensagem única, narrativa, ação | exploração aberta, muitos indicadores | usa como sinônimos.
- C15. **Explanatória** × **exploratória** | mensagem definida; conduz o público | analista investiga para descobrir | inverte os termos.

## Pegadinhas

- [P1-7.1] **CONCEITOS** — calcular média de variável nominal ("partido médio")
- [P1-7.1] **CONCEITOS** — tratar escala ordinal como se as distâncias entre níveis fossem iguais
- [P1-7.1] **CONCEITOS** — chamar "informação" de "dado bruto"
- [P1-7.1] **CONCEITOS** — afirmar que dados estruturados são os "sem esquema".
- [P1-7.1] **ATRIBUTOS** — confundir o atributo (a coluna "UF") com o valor do atributo ("DF")
- [P1-7.1] **ATRIBUTOS** — afirmar que todo atributo precisa ser único
- [P1-7.1] **ATRIBUTOS** — trocar atributo por métrica (dizer que "UF do autor" é métrica).
- [P1-7.1] **MÉTRICAS** — inverter média e mediana quanto à sensibilidade a extremos
- [P1-7.1] **MÉTRICAS** — chamar dimensão de métrica
- [P1-7.1] **MÉTRICAS** — dizer que coluna numérica é automaticamente métrica (o número do projeto é identificador)
- [P1-7.1] **MÉTRICAS** — afirmar que a média é a medida válida para dado ordinal (são a mediana e a moda).
- [P1-7.1] **TRANSFORMAÇÃO DE DADOS** — definir normalização como "remoção de duplicatas" (é limpeza)
- [P1-7.1] **TRANSFORMAÇÃO DE DADOS** — chamar de "limpeza" uma agregação
- [P1-7.1] **TRANSFORMAÇÃO DE DADOS** — inverter ETL e ELT
- [P1-7.1] **TRANSFORMAÇÃO DE DADOS** — usar normalização e padronização como sinônimos em item que exige a distinção.
- [P1-8.1] **Princípios de visualização de dados** — Afirmar que truncar o eixo de barras é boa prática para realçar diferenças
- [P1-8.1] **Princípios de visualização de dados** — dizer que mais cores e efeitos 3D aumentam a clareza
- [P1-8.1] **Princípios de visualização de dados** — usar paleta sequencial ou divergente para categorias sem ordem
- [P1-8.1] **Princípios de visualização de dados** — afirmar que área ou cor comparam com mais precisão que posição
- [P1-8.1] **Princípios de visualização de dados** — dizer que pizza é adequada para muitas categorias ou para evolução no tempo.
- [P1-8.2] **Histograma** — tratá-lo como gráfico de barras de categorias
- [P1-8.2] **Histograma** — dizer que a ordem das classes é intercambiável
- [P1-8.2] **Histograma** — tratar altura e área como sempre equivalentes
- [P1-8.2] **Histograma** — usar histograma para categorias nominais.
- [P1-8.2] **Gráfico de linha** — confundir com dispersão
- [P1-8.2] **Gráfico de linha** — usar linha para categorias sem ordem (partidos, comissões), o que sugere continuidade inexistente.
- [P1-8.2] **Gráfico de barras (colunas)** — confundir com histograma
- [P1-8.2] **Gráfico de barras (colunas)** — aceitar eixo truncado
- [P1-8.2] **Gráfico de barras (colunas)** — usar para distribuição de variável contínua agrupada em classes; empilhado quando se quer comparar as partes entre si.
- [P1-8.2] **Gráfico de dispersão** — afirmar que mostra causa e efeito
- [P1-8.2] **Gráfico de dispersão** — confundir com linha
- [P1-8.2] **Gráfico de dispersão** — dizer que exige variável categórica em um dos eixos.
- [P1-8.2] **Box plot (diagrama de caixa)** — dizer que a linha central é a média; que a caixa vai do mínimo ao máximo ou contém todos os dados; que os bigodes vão até 1,5 desvio padrão; que mostra frequência por intervalo (isso é histograma).
- [P1-8.3] **Power BI (Microsoft)** — inverter o fluxo (criar no serviço, publicar no Desktop)
- [P1-8.3] **Power BI (Microsoft)** — dizer que o Desktop é pago
- [P1-8.3] **Power BI (Microsoft)** — dizer que o serviço não permite criar dashboards.
- [P1-8.3] **Tableau (Salesforce)** — trocar Cloud (hospedado pela Tableau) por Server (hospedado pelo cliente)
- [P1-8.3] **Tableau (Salesforce)** — dizer que o Tableau Public é privado ou pago.
- [P1-8.3] **Data Studio (Google)** — afirmar que "o Data Studio foi descontinuado e substituído pelo Looker Studio" (foi renomeado, e o nome voltou em abril de 2026)
- [P1-8.3] **Data Studio (Google)** — confundir Data Studio com Looker
- [P1-8.3] **Data Studio (Google)** — tratar Looker Studio e Data Studio como produtos diferentes
- [P1-8.3] **Data Studio (Google)** — atribuir à ferramenta a responsabilidade pela adequação do gráfico (a ferramenta pode sugerir ou gerar visuais, mas a adequação ao dado e à pergunta é do analista)
- [P1-8.3] **Data Studio (Google)** — misturar com Excel/Office (item 1 do edital, MSOffice 365, fora do escopo dos itens 7 e 8 de TI e Dados).
- [P1-8.4] **Storytelling para visualização de dados** — Dizer que storytelling é apenas enfeitar o gráfico ou dispensa mensagem explícita
- [P1-8.4] **Storytelling para visualização de dados** — inverter exploratória e explanatória
- [P1-8.4] **Storytelling para visualização de dados** — sugerir mostrar o máximo de métricas para o público concluir sozinho
- [P1-8.4] **Storytelling para visualização de dados** — dizer que narrativa dispensa dados
- [P1-8.4] **Storytelling para visualização de dados** — usar dashboard e storytelling como sinônimos.
