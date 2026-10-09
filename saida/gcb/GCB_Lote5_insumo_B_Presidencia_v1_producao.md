# Lote5_v1_producao.md — Lote 5 — 2026-10-08 — gerado por PRESIDÊNCIA (produtor substituto, opção "4, ciente" do Fundador)

Status: v1 — NÃO REVISADA. Destino obrigatório: GCB-CQFP (QA rodada 1). Nenhum trecho vai à candidata antes do QA.
Escopo: edital P1, TECNOLOGIA DA INFORMAÇÃO E DADOS, itens 7.1 e 8.1–8.4.
Fontes de ferramenta verificadas em 8/10/2026 (listadas na seção (e)). Referências doutrinárias (Tukey, Tufte, Cleveland e McGill, Knaflic, Dykes) são citadas por nome; a CQFP pode exigir obra e edição.

---

## (a) CURSO

### 7.1 Dados — conceitos, atributos, métricas, transformação

**7.1.1 Conceitos.**
- *Dado* é o registro bruto de um fato ("Deputado X falou 7 minutos em 3/9"). *Informação* é dado organizado com significado ("a média de fala por deputado foi 5 min"). *Conhecimento* é a informação aplicada a uma decisão ("ampliar o tempo de fala das comissões").
- Quanto à estrutura: *dado estruturado* (tabela com linhas e colunas — planilha de proposições), *semiestruturado* (XML/JSON com tags, como os dados abertos da Câmara), *não estruturado* (áudio de sessão, texto livre de notas taquigráficas).
- Quanto à natureza: *qualitativo* (categorias: partido, UF, tipo de proposição) ou *quantitativo* (números: tempo de fala, número de emendas). O quantitativo é *discreto* (contagem: nº de emendas) ou *contínuo* (medida: duração em segundos).
- Escalas de medida (Stevens): *nominal* (sem ordem: partido), *ordinal* (ordem sem distância: urgência baixa/média/alta), *intervalar* (distâncias iguais, zero arbitrário: temperatura °C), *de razão* (zero absoluto: duração, valor em reais).
- Exemplo aplicado: na base de proposições da Câmara, "tipo" (PL, PEC, MPV) é nominal; "regime de tramitação" pode ser tratado como ordinal; "número de pareceres" é discreto; "tempo até a aprovação" é contínuo.
- Pegadinha provável: item que calcule média de variável nominal ("partido médio") ou que trate escala ordinal como se as distâncias entre níveis fossem iguais. Também: chamar "informação" de "dado bruto".

**7.1.2 Atributos.**
- Em dado tabular, *atributo* = coluna = variável = campo; *registro* = linha = instância. Cada atributo tem *tipo* (texto, inteiro, decimal, data, booleano) e *domínio* (valores admitidos).
- *Chave* é atributo (ou conjunto) que identifica unicamente o registro (ex.: número + ano da proposição). *Atributo derivado* é calculado a partir de outros (idade a partir da data de nascimento).
- Exemplo aplicado: na tabela de deputados, "ideCadastro" é chave; "idade" é derivado de "dataNascimento"; "siglaPartido" é atributo nominal.
- Pegadinha provável: confundir atributo (a coluna "UF") com valor do atributo ("DF"); afirmar que todo atributo precisa ser único.

**7.1.3 Métricas.**
- *Métrica* é valor numérico agregado a partir dos dados: contagem, soma, média, mediana, moda, mínimo, máximo, desvio padrão, percentis, proporções/taxas. *Dimensão* é o atributo pelo qual a métrica é segmentada (métrica "nº de proposições" por dimensão "partido").
- *KPI* (indicador-chave) é métrica escolhida para monitorar um objetivo, com meta e período.
- Medidas de tendência central: *média* (sensível a valores extremos), *mediana* (valor do meio; robusta a extremos), *moda* (mais frequente; única medida aplicável a dado nominal). Dispersão: amplitude, variância, desvio padrão, intervalo interquartil (IQR = Q3 − Q1).
- Exemplo aplicado: tempo de tramitação de PLs: um PL de 20 anos puxa a média para cima; a mediana descreve melhor o "PL típico".
- Pegadinha provável: trocar média e mediana quanto à sensibilidade a outliers; chamar dimensão de métrica; afirmar que a média é a única medida válida para dados ordinais (é a mediana/moda).

**7.1.4 Transformação de dados.**
- Transformar é alterar forma, escala ou estrutura dos dados para análise. Operações típicas: *agregação* (somar por mês), *filtragem*, *junção* (join de tabelas por chave), *pivotagem* (linhas ↔ colunas), *discretização/binning* (contínuo → faixas), *codificação* (categoria → número, ex.: one-hot), *normalização* (reescalar para intervalo, ex.: 0–1) e *padronização* (média 0, desvio 1), *derivação* de atributos, *anonimização/pseudonimização*.
- *Limpeza* (tratar duplicatas, nulos, inconsistências, erros de digitação) é etapa distinta, embora frequentemente agrupada no mesmo processo. No fluxo *ETL* (extrair, transformar, carregar) a transformação precede a carga; no *ELT* ela ocorre após a carga, no destino.
- Exemplo aplicado: para comparar tempo de fala entre comissões de tamanhos diferentes, calcula-se o tempo por membro (derivação) e agrega-se por mês (agregação).
- Pegadinha provável: definir normalização como "remoção de duplicatas" (é limpeza); inverter ETL e ELT; afirmar que transformação altera o dado de origem (atua sobre cópias/camadas analíticas).

### 8.1 Princípios de visualização de dados

- *Propósito antes da forma*: a visualização responde a uma pergunta; o tipo de gráfico decorre da natureza do dado (categórico × quantitativo; um momento × série temporal; distribuição × relação).
- *Integridade*: a representação visual deve ser proporcional ao valor. Em gráficos de barras, o eixo de valores começa em zero; truncá-lo exagera diferenças. Tufte chama de *lie factor* a razão entre o efeito visual e o efeito nos dados, e recomenda alta *razão dado-tinta* (data-ink ratio) e eliminação de *chartjunk* (3D, sombras, decoração).
- *Percepção*: Cleveland e McGill ordenaram a precisão com que lemos codificações visuais — posição em escala comum (mais precisa) > comprimento > ângulo/inclinação > área > volume/cor (menos precisa). Daí barras serem lidas com mais exatidão que pizzas.
- *Cor*: paleta *categórica* para categorias sem ordem; *sequencial* para intensidade de uma grandeza; *divergente* para valores que se afastam de um centro (positivo/negativo). Considerar daltonismo (evitar depender só de vermelho × verde).
- *Clareza*: título que afirma a mensagem, eixos rotulados com unidade, legenda próxima aos dados, poucos elementos por gráfico, consistência de escalas ao comparar painéis.
- *Gestalt*: proximidade, similaridade e fechamento guiam agrupamentos visuais; usar a favor da leitura.
- Exemplo aplicado: para mostrar "proposições aprovadas por comissão", barras horizontais ordenadas por valor; para "evolução mensal de sessões", linha; evitar pizza com 20 comissões.
- Pegadinha provável: afirmar que área/cor comparam com mais precisão que posição; que o eixo de barras pode começar em qualquer valor sem prejuízo; que pizza é adequada para muitas categorias ou para evolução no tempo; que 3D melhora a leitura.

### 8.2 Tipos de gráficos

**Histograma.** Mostra a *distribuição de frequências de uma variável quantitativa contínua* (ou discreta com muitos valores), dividida em intervalos (classes/bins). As barras são *contíguas* (sem espaços) porque os intervalos são adjacentes; com classes de mesma largura, a altura indica a frequência (em geral, a área é proporcional à frequência). Permite ver forma (simétrica, assimétrica), centro, dispersão, modas e outliers. A escolha do número de classes altera a aparência.
- Exemplo: distribuição da duração dos discursos em plenário em faixas de 2 minutos.
- Pegadinha: chamar de gráfico de barras; afirmar que as barras devem ter espaço entre si; usar histograma para categorias nominais.

**Gráfico de linha.** Liga pontos ordenados no eixo x — tipicamente *tempo* — para mostrar *tendência, sazonalidade e variação*. Exige variável de x ordenada e contínua ou sequencial; várias séries podem ser comparadas, com cuidado para o número de linhas.
- Exemplo: número de sessões deliberativas por mês ao longo da legislatura.
- Pegadinha: usar linha para categorias sem ordem (partidos), o que sugere continuidade inexistente; ligar pontos de categorias.

**Gráfico de barras (colunas).** Compara *valores entre categorias*. Barras *separadas* por espaços; vertical (colunas) ou horizontal (melhor para rótulos longos); *agrupado* (subcategorias lado a lado) ou *empilhado* (partes de um total). O eixo de valores começa em zero. Ordenar por valor facilita a leitura quando não há ordem natural.
- Exemplo: proposições apresentadas por partido na sessão legislativa.
- Pegadinha: confundir com histograma; eixo truncado; empilhado quando se quer comparar as partes entre si (difícil ler bases desalinhadas).

**Gráfico de dispersão.** Cada ponto é um par (x, y) de *duas variáveis quantitativas*; revela *relação* (direção, força, forma), agrupamentos e outliers. Pode receber linha de tendência; o *gráfico de bolhas* acrescenta uma terceira variável no tamanho. *Correlação não implica causalidade*.
- Exemplo: tempo de mandato (x) versus número de proposições apresentadas (y) por deputado.
- Pegadinha: afirmar que correlação forte prova causa; usar dispersão com variável categórica em um dos eixos; confundir com linha.

**Box plot (diagrama de caixa).** Resume a distribuição por *cinco números*: mínimo, primeiro quartil (Q1), mediana (Q2), terceiro quartil (Q3), máximo. A *caixa* vai de Q1 a Q3 (intervalo interquartil, IQR), a linha interna é a *mediana*; os *bigodes* (critério de Tukey) estendem-se até o último dado dentro de 1,5 × IQR a partir da caixa, e os pontos além são *outliers*. Ótimo para *comparar distribuições* entre grupos lado a lado. Não mostra a média (salvo marcação extra) nem a forma detalhada (bimodalidade fica oculta).
- Exemplo: tempo de tramitação de PLs por comissão de origem, uma caixa por comissão.
- Pegadinha: dizer que a linha da caixa é a média; que os bigodes vão até 1,5 desvio padrão; que a caixa cobre 100% dos dados (cobre os 50% centrais); que o box plot mostra frequência por intervalo (isso é histograma).

### 8.3 Ferramentas de visualização de dados

**Power BI (Microsoft).** Três componentes: *Power BI Desktop* (aplicativo para Windows, ferramenta de criação de relatórios, disponível gratuitamente para download), *serviço do Power BI* (plataforma on-line/SaaS para publicar, organizar, compartilhar relatórios e criar dashboards) e *Power BI Mobile* (apps para consumo em dispositivos móveis). Fluxo típico: conectar e modelar dados e criar o relatório no Desktop → publicar no serviço → distribuir e consumir no serviço e no Mobile. [verificado em 8/10/2026 — Microsoft Learn: https://learn.microsoft.com/en-gb/training/modules/get-started-with-power-bi/2-using-power-bi e https://learn.microsoft.com/en-us/training/modules/create-data-set/2-install]
- Nomes de linguagens e recursos internos (Power Query, DAX, Report Server) não foram verificados nesta rodada: [SEM FONTE DATADA — não afirmar até a CQFP confirmar].
- Pegadinha: inverter o fluxo (criar no serviço, publicar no Desktop); dizer que o Desktop é pago ou que roda nativamente em macOS; dizer que dashboards são criados no Desktop (o material oficial situa dashboards no serviço).

**Tableau (Salesforce).** Família de produtos: *Tableau Desktop* (criação e análise), *Tableau Cloud* (plataforma totalmente hospedada em nuvem), *Tableau Server* (plataforma auto-hospedada, on-premises ou em nuvem pública; pode ter vários sites), *Tableau Prep* (preparação: combinar, moldar, limpar dados), *Tableau Mobile* (app que interage com Server/Cloud) e *Tableau Public* (plataforma gratuita para criar e compartilhar publicamente visualizações). [verificado em 8/10/2026 — Tableau Help: https://help.tableau.com/current/tableau/en-us/tableau_product_overview.htm]
- Pegadinha: trocar Cloud (hospedado pela Tableau) por Server (hospedado pelo cliente); dizer que Tableau Public é privado ou pago; atribuir ao Prep a função de visualização.

**Data Studio (Google).** Ferramenta *sem custo* ("no-cost") para transformar dados em painéis e relatórios compartilháveis. Histórico de nome: lançada como Data Studio; em outubro de 2022 passou a chamar-se *Looker Studio*; **em abril de 2026 o nome voltou a ser Data Studio**, com URL https://datastudio.google.com/ (o endereço lookerstudio.google.com redireciona). [verificado em 8/10/2026 — Google Cloud: https://docs.cloud.google.com/data-studio/welcome e notas de versão de 16/4/2026: https://docs.cloud.google.com/data-studio/release-notes]
- Logo, o nome usado no edital ("Data Studio") é o nome vigente. Versão paga "Data Studio Pro" (antes Looker Studio Pro): citada em fontes secundárias; [SEM FONTE OFICIAL DATADA NESTA RODADA — a CQFP confirma antes de usar em item].
- Pegadinha: item afirmando que "Data Studio foi descontinuado e substituído pelo Looker Studio" (errado desde abril de 2026); confundir Data Studio com *Looker* (plataforma de BI corporativa, produto distinto).

### 8.4 Storytelling para visualização de dados

- *Conceito*: contar uma história com dados é combinar três elementos — *dados*, *narrativa* e *elementos visuais* (Dykes) — para levar o público a uma conclusão e a uma ação. Difere de dashboard (exploração aberta) e de "muitos gráficos": o storytelling tem *uma mensagem central*.
- *Método* (Knaflic): entender o contexto (quem é o público, o que precisa saber, o que deve fazer); escolher a visualização adequada; *eliminar o desnecessário* (ruído); *dirigir a atenção* (cor, contraste, tamanho, posição, anotações); pensar como designer (hierarquia visual, alinhamento); construir a *narrativa* com início (contexto), meio (tensão/achado) e fim (resolução/chamada à ação).
- *Técnicas*: título em forma de afirmação ("Sessões caíram 30% no 2º semestre"), destaque de uma única série em cor forte com as demais em cinza, anotações no gráfico, sequência de gráficos que revela a história passo a passo, escolha de uma métrica por slide.
- Exemplo aplicado: relatório à Mesa sobre atrasos de pauta: contexto (nº de sessões), tensão (aumento de sessões sem quórum), achado (concentração nas sextas), ação (redistribuir a pauta).
- Pegadinha: afirmar que storytelling é "enfeitar" gráficos; que se deve apresentar o máximo de métricas para o público concluir sozinho; que narrativa dispensa dados; que dashboard e storytelling são sinônimos.

---

## (b) RESUMO (uma página)

**7.1 Dados.** Dado (bruto) → informação (organizado) → conhecimento (aplicado). Estruturado / semiestruturado / não estruturado. Qualitativo (nominal, ordinal) × quantitativo (discreto, contínuo; escalas intervalar e de razão). Atributo = coluna/variável; registro = linha; chave identifica; derivado é calculado. Métrica = agregado numérico (contagem, soma, média, mediana, moda, desvio padrão, percentil); dimensão = atributo de segmentação; KPI = métrica com meta. Média é sensível a extremos; mediana é robusta; moda vale para nominal. Transformação: agregar, filtrar, juntar, pivotar, discretizar, codificar, normalizar (reescala) e padronizar (média 0, desvio 1), derivar, anonimizar. Limpeza (duplicatas, nulos, erros) é etapa distinta. ETL transforma antes de carregar; ELT, depois.

**8.1 Princípios.** Pergunta antes do gráfico. Integridade: barras começam em zero; evitar lie factor, chartjunk e 3D; maximizar dado-tinta (Tufte). Percepção (Cleveland e McGill): posição > comprimento > ângulo > área > cor. Paleta categórica (sem ordem), sequencial (intensidade), divergente (em torno de um centro). Título afirmativo, eixos com unidade, poucos elementos, escalas consistentes.

**8.2 Gráficos.** Histograma: distribuição de variável contínua, barras contíguas, classes. Linha: tendência no tempo, x ordenado. Barras: comparação entre categorias, barras separadas, eixo em zero, agrupado/empilhado. Dispersão: relação entre duas quantitativas; correlação ≠ causalidade; bolhas = 3ª variável. Box plot: mín, Q1, mediana, Q3, máx; caixa = IQR (50% centrais); bigodes até 1,5 × IQR (Tukey); pontos além = outliers; não mostra média por padrão.

**8.3 Ferramentas (verificado em 8/10/2026).** Power BI (Microsoft): Desktop (Windows, criação, gratuito) → serviço (nuvem: publicar, compartilhar, dashboards) → Mobile. Tableau (Salesforce): Desktop, Cloud (hospedado), Server (auto-hospedado), Prep (preparação), Mobile, Public (gratuito e público). Data Studio (Google): sem custo; foi Looker Studio de out/2022 a abr/2026 e voltou a chamar-se Data Studio em abril de 2026 (datastudio.google.com). Looker ≠ Data Studio.

**8.4 Storytelling.** Dados + narrativa + visual, com uma mensagem central e chamada à ação. Contexto → visual adequado → eliminar ruído → dirigir atenção (cor, anotação) → design → narrativa (início, meio, fim). Não é dashboard, não é decoração.

---

## (c) PARES CONFUNDÍVEIS

| Par | Um | Outro | Como a banca troca |
|---|---|---|---|
| Histograma × barras | distribuição de variável contínua; barras contíguas; eixo x = intervalos | comparação entre categorias; barras separadas; eixo x = categorias | chama histograma de "barras" ou pede histograma para partidos |
| Linha × dispersão | pontos ligados em x ordenado (tempo); tendência | pontos soltos de duas quantitativas; relação | linha para categorias; dispersão "para ver evolução" |
| Box plot × histograma | cinco números, quartis, outliers; compara grupos | frequência por classe; mostra forma e modas | diz que box plot mostra frequência por faixa |
| Média × mediana | sensível a extremos | robusta a extremos; valor central | inverte a sensibilidade |
| Atributo × métrica (dimensão × medida) | coluna que descreve/segmenta (partido) | número agregado (total de PLs) | chama "partido" de métrica |
| Transformação × limpeza | muda forma/escala/estrutura (agregar, normalizar) | corrige erros, nulos, duplicatas | define normalização como remoção de duplicatas |
| Normalização × padronização | reescala para intervalo (0–1) | média 0 e desvio 1 (z-score) | usa os termos como sinônimos em item que exige distinção |
| ETL × ELT | transforma antes da carga | transforma depois, no destino | inverte a ordem |
| Paleta sequencial × divergente × categórica | intensidade crescente | afastamento de um centro | categorias sem ordem | divergente para partidos; categórica para intensidade |
| Posição × área/cor | leitura mais precisa | leitura menos precisa | afirma que área compara melhor |
| Data Studio × Looker Studio × Looker | nome vigente desde abr/2026 (gratuito) | nome usado entre out/2022 e abr/2026 (mesmo produto) | plataforma de BI corporativa, produto distinto | "Data Studio foi substituído"; Looker = Data Studio |
| Tableau Cloud × Tableau Server | hospedado pela Tableau | hospedado pelo cliente | inverte quem hospeda |
| Power BI Desktop × serviço | cria o relatório (Windows) | publica, compartilha, dashboards | diz que se cria no serviço e publica no Desktop |
| Storytelling × dashboard | mensagem única, narrativa, ação | exploração aberta, muitos indicadores | usa como sinônimos |

---

## (d) 20 ITENS C/E — rótulo AUTORAL — Lote 5
Formato Cebraspe: "Julgue o item". [TS] marca os 10 itens com troca sutil de um único conceito em frase no restante verdadeira. Distribuição: 7.1 (A5-01 a 04), 8.1 (05 a 07), 8.2 (08 a 13), 8.3 (14 a 17), 8.4 (18 a 20).

**A5-01 (7.1).** Em uma base de dados tabular, cada coluna corresponde a um atributo (variável) e cada linha, a um registro.
Gabarito: C. Justificativa: é a definição básica de dado estruturado; atributo = coluna, registro/instância = linha.

**A5-02 (7.1) [TS].** A mediana é a medida de tendência central mais sensível à presença de valores extremos, razão pela qual se recomenda a média para descrever distribuições assimétricas.
Gabarito: E. Justificativa: inversão — a média é sensível a extremos; a mediana é robusta e é a recomendada em distribuições assimétricas.

**A5-03 (7.1) [TS].** A normalização de dados consiste em remover registros duplicados e corrigir valores inválidos antes da análise.
Gabarito: E. Justificativa: a descrição é de limpeza de dados; normalização é reescalar valores para um intervalo comum.

**A5-04 (7.1).** Em uma análise sobre a produção legislativa, o número médio de proposições apresentadas por deputado é uma métrica, e o partido pelo qual essa métrica é segmentada é uma dimensão.
Gabarito: C. Justificativa: métrica é valor numérico agregado; dimensão é o atributo que segmenta a métrica.

**A5-05 (8.1) [TS].** Segundo os estudos de percepção visual, a codificação de valores por área e por intensidade de cor permite comparações mais precisas do que a codificação por posição em uma escala comum.
Gabarito: E. Justificativa: a ordem de precisão (Cleveland e McGill) é posição > comprimento > ângulo > área > cor; área e cor são as menos precisas.

**A5-06 (8.1).** Em gráficos de barras, iniciar o eixo de valores em ponto diferente de zero distorce a comparação entre as categorias, pois o comprimento das barras deixa de ser proporcional aos valores representados.
Gabarito: C. Justificativa: a barra codifica o valor pelo comprimento; eixo truncado quebra a proporcionalidade (princípio da integridade).

**A5-07 (8.1) [TS].** Uma paleta de cores divergente é a escolha adequada para distinguir categorias sem ordem natural, como os partidos políticos em um gráfico de barras.
Gabarito: E. Justificativa: categorias sem ordem pedem paleta categórica; a divergente serve a valores que se afastam de um centro.

**A5-08 (8.2).** No histograma, as barras são contíguas porque representam intervalos adjacentes de uma variável contínua, e, com classes de mesma largura, a altura de cada barra indica a frequência de observações no intervalo.
Gabarito: C. Justificativa: definição do histograma; contiguidade decorre da adjacência das classes.

**A5-09 (8.2) [TS].** O gráfico de barras é o tipo indicado para representar a distribuição de frequências de uma variável quantitativa contínua, como a duração dos discursos em plenário.
Gabarito: E. Justificativa: distribuição de variável contínua é representada por histograma; barras comparam categorias.

**A5-10 (8.2).** Em um box plot, a caixa delimita o intervalo entre o primeiro e o terceiro quartis, e a linha no interior da caixa indica a mediana da distribuição.
Gabarito: C. Justificativa: caixa = IQR (Q1 a Q3); linha interna = mediana (Q2).

**A5-11 (8.2) [TS].** Em um box plot construído pelo critério de Tukey, os bigodes se estendem até 1,5 vez o desvio padrão a partir da caixa, e os pontos além desse limite são tratados como outliers.
Gabarito: E. Justificativa: o limite de Tukey é 1,5 × intervalo interquartil (IQR), não desvio padrão.

**A5-12 (8.2).** O gráfico de dispersão permite examinar a relação entre duas variáveis quantitativas, mas uma correlação forte observada nele não autoriza, por si só, afirmar relação de causa e efeito.
Gabarito: C. Justificativa: dispersão mostra associação; causalidade exige desenho de pesquisa ou controle de variáveis.

**A5-13 (8.2) [TS].** O gráfico de linhas é o mais indicado para comparar valores entre categorias sem ordem natural, como o número de projetos aprovados por comissão temática.
Gabarito: E. Justificativa: linhas pressupõem x ordenado (tempo); comparação entre categorias pede gráfico de barras.

**A5-14 (8.3).** O Power BI é composto pelo Power BI Desktop, aplicativo para Windows no qual os relatórios são criados; pelo serviço do Power BI, plataforma on-line para publicação e compartilhamento; e por aplicativos móveis para consumo.
Gabarito: C. Justificativa: três componentes e fluxo descritos no material oficial da Microsoft (verificado em 8/10/2026).

**A5-15 (8.3) [TS].** A ferramenta Data Studio, do Google, foi descontinuada em 2022 e substituída pelo Looker Studio, de modo que a denominação Data Studio não corresponde a produto vigente.
Gabarito: E. Justificativa: o produto foi renomeado (não descontinuado) para Looker Studio em 2022 e voltou a chamar-se Data Studio em abril de 2026 (fonte Google, verificado em 8/10/2026).

**A5-16 (8.3).** O Tableau Public é uma plataforma gratuita para criar e compartilhar publicamente visualizações, enquanto o Tableau Server é a versão auto-hospedada da plataforma e o Tableau Cloud, a versão totalmente hospedada em nuvem.
Gabarito: C. Justificativa: descrição conforme a visão geral de produtos da Tableau (verificado em 8/10/2026).

**A5-17 (8.3) [TS].** No fluxo de trabalho típico do Power BI, o relatório é criado no serviço on-line e, em seguida, publicado no Power BI Desktop para consumo pelos usuários.
Gabarito: E. Justificativa: inversão do fluxo — cria-se no Desktop e publica-se no serviço.

**A5-18 (8.4).** O storytelling com dados combina dados, narrativa e elementos visuais para conduzir o público a uma conclusão, e não se confunde com a simples exibição de muitos gráficos em um painel.
Gabarito: C. Justificativa: os três elementos (Dykes) e a mensagem central distinguem storytelling de dashboard.

**A5-19 (8.4) [TS].** Na narrativa com dados, recomenda-se apresentar o maior número possível de métricas em cada gráfico, de modo que o público extraia suas próprias conclusões sem a interferência do autor.
Gabarito: E. Justificativa: o storytelling elimina o desnecessário e dirige a atenção a uma mensagem; o excesso de métricas é o oposto da técnica.

**A5-20 (8.4).** O uso de contraste de cor para destacar a série relevante e a inclusão de anotações diretamente no gráfico são técnicas de storytelling, pois dirigem a atenção do público à mensagem central.
Gabarito: C. Justificativa: "dirigir a atenção" por cor, tamanho, posição e anotação é etapa reconhecida do método (Knaflic).

---

## (e) AFIRMAÇÕES SOBRE FERRAMENTAS — proveniência (para a CQFP)
| Afirmação | Fonte oficial | Verificado em |
|---|---|---|
| Power BI = Desktop (Windows, criação, gratuito) + serviço (on-line, publicar/compartilhar, dashboards) + Mobile; fluxo Desktop → serviço → Mobile | https://learn.microsoft.com/en-gb/training/modules/get-started-with-power-bi/2-using-power-bi ; https://learn.microsoft.com/en-us/training/modules/create-data-set/2-install | 8/10/2026 |
| Tableau: Desktop, Cloud (hospedado), Server (auto-hospedado, vários sites), Prep (preparação), Mobile, Public (gratuito, público) | https://help.tableau.com/current/tableau/en-us/tableau_product_overview.htm | 8/10/2026 |
| Data Studio (Google): sem custo; Looker Studio renomeado para Data Studio em abril de 2026; URL datastudio.google.com; lookerstudio.google.com redireciona | https://docs.cloud.google.com/data-studio/welcome ; https://docs.cloud.google.com/data-studio/release-notes (16/4/2026) | 8/10/2026 |
| Data Studio Pro (paga) | só fontes secundárias | PENDENTE — não usar em item |
| Power Query, DAX, Report Server | não verificados | PENDENTE — não usar em item |

## (f) PENDÊNCIAS DO PRODUTOR (declaradas)
1. Referências doutrinárias citadas por autor, sem edição/página: Tukey (box plot, 1,5 × IQR), Tufte (lie factor, data-ink, chartjunk), Cleveland e McGill (hierarquia perceptual), Knaflic (storytelling), Dykes (dados + narrativa + visual). A CQFP decide se exige obra.
2. "Com classes de mesma largura, a altura indica a frequência" — formulação cautelosa; a CQFP confirma a redação para classes desiguais (área ∝ frequência).
