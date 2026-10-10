# simulado_0_v0.2.md — R-04, T-15 — 2026-10-10 — gerado por gbq-csc

# Simulado 0 (misto, diagnóstico) — v0.2 — Câmara dos Deputados 2026, Cargo 11

Analista Legislativo, Especialidade Registro e Redação (Cebraspe, prova em 17/1/2027). Montado só com itens de `banco/banco.csv` (rótulo CEBRASPE_ANALOGA), aprovados no QA, **agrupados pelo comando original do caderno**. A v0.2 substitui a v0.1 (43 itens, comando genérico). Total: **60 itens** (Parte P1: 39; Parte P2: 21) em **34 comandos**. Gabarito e mapa em `saida/simulados/simulado_0_v0.2_gabarito.md`.

## Avisos de montagem

1. **Simulado diagnóstico, não final.** Contém 24 itens de aderência PARCIAL (D-ADERENCIA: parcial só em diagnóstico) e 4 itens VOLÁTEIS (inaptos a simulado final até a reverificação de 4–8/1/2027). Não use esta montagem como simulado final.
2. **Aderência PARCIAL (24 itens).** Cada um traz, logo abaixo do item, a marca `[ADERÊNCIA PARCIAL ...]` com o motivo; o mapa do gabarito repete a marca. Eles testam o tema vizinho, não o texto exato do subitem do edital da Câmara.
   - Dos 24, 17 estão em P2-4.1 (LGPD geral), 4 em P2-4.3 (segurança da informação geral), 2 em P1-8.3 (Grafana/Kibana) e 1 em P1-7.1 (KPIs). **Toda a cobertura de P2 neste simulado é PARCIAL.**
3. **Enquadramento em arbitragem (T-03), 6 itens.** BQ-0001, BQ-0009, BQ-0015, BQ-0016: o banco os trata como diretos, mas o QA de 09/10 os leu como INDIRETOS; marcados no corpo com `[ADERÊNCIA EM ARBITRAGEM — T-03]`. BQ-0014, BQ-0040: só o mapeamento do subitem está em discussão (o QA os leu como DIRETOS); sem marca no corpo, nota no mapa.
4. **Desequilíbrio C/E (contagem real).** Total: **33 C e 27 E** (55,0% C / 45,0% E). P1: 21 C e 18 E (53,8% C). P2: 12 C e 9 E (57,1% C). O banco aprovado e utilizável é assim; nenhum item aprovado foi removido para equilibrar. Quem marcasse C em todos os itens acertaria 55,0%; **não calibre o desempenho por esta proporção**.
5. **VOLÁTEIS (4 itens):** BQ-0064 (item 23; ChatGPT/DeepSeek, arquitetura transformer), BQ-0015 (item 18; objeto "thread" de API de assistentes de fornecedor), BQ-0017 (item 37; Grafana) e BQ-0035 (item 38; Kibana). Entram por ser diagnóstico; reverificação em 4–8/1/2027 (T-14 para BQ-0064; T-16 para BQ-0015, BQ-0017 e BQ-0035).
6. **LGPD e Lei 15.352/2026.** Os itens de LGPD reproduzem a prova original (anterior à Lei 15.352/2026, que alterou a LGPD; ANPD = Agência Nacional de Proteção de Dados). 16 desses itens aguardam a conferência do qa-normativo (T-13); o gabarito segue o definitivo do certame de origem.
7. **Fora desta montagem:** itens AUTORAL (o Simulado 0 é só banco) e os 6 itens anulados do banco (BQ-0029, 0030, 0031, 0060, 0062, 0063; D1 da GBQ: anulados não entram em nenhum simulado).
8. Textos e comandos copiados literalmente do banco e dos cadernos oficiais (cdn.cebraspe.org.br). Mantêm-se as grafias do original (por exemplo, "dashborad" e "ideal atender"). Itens do mesmo comando original que não foram aproveitados foram omitidos; a numeração é a deste simulado.

## Instruções

- Cada item está vinculado ao comando que imediatamente o antecede (instrução dos cadernos Cebraspe). De acordo com o comando a que cada item esteja vinculado, julgue-o CERTO (C) ou ERRADO (E) (edital nº 1/2026, subitem 8.2: itens agrupados por comandos, que devem ser respeitados).
- Para obter pontuação no item, marque um, e somente um, dos dois campos: `C` ou `E` (subitem 8.3). Marque no espaço `Resposta: [   ]` ao lado de cada item.
- Pontuação (subitem 8.11.2 do edital): **+1,00 ponto** se a marcação concordar com o gabarito; **−1,00 ponto** se discordar; **0,00 ponto** se não houver marcação ou houver marcação dupla (C e E). A nota da parte é a soma das notas dos itens (8.11.3).
- Total de itens: 60 (Parte P1: 39, itens 1 a 39; Parte P2: 21, itens 40 a 60). A numeração é contínua.
- As marcas entre colchetes abaixo de alguns itens são avisos de montagem do diagnóstico; não fazem parte do texto do item.

## Parte P1 — Conhecimentos Básicos (Tecnologia da Informação e Dados, itens 5 a 8 do edital)

Os itens abaixo tomam por base o item 14.2.3 do edital (TI e Dados, itens 5 a 8).

### Comando 1

> A respeito dos tipos de aprendizado de máquina, julgue os itens a seguir.

**1.** O agrupamento é um método de aprendizado não supervisionado que busca a similaridade entre os dados e, uma vez identificada tal similaridade, organiza os itens em clusters específicos.

Resposta: [   ]

### Comando 2

> Julgue os próximos itens, relativos a Naive Bayes e random forest.

**2.** Naive Bayes é um algoritmo de classificação baseado na aprendizagem por reforço, em que um agente realiza uma ação e recebe uma recompensa de acordo com o resultado dessa ação por meio da implementação do teorema de Bayes, com o objetivo de encontrar a probabilidade a posteriori.

Resposta: [   ]

### Comando 3

> A respeito de KNN (k-nearest neighbours), SVM (support vector machines), deep learning e técnicas de agrupamento, julgue os itens a seguir.

**3.** KNN é um algoritmo de aprendizado supervisionado não paramétrico que não pode ser utilizado em problemas de classificação, uma vez que seu objetivo é prever valores numéricos e não valores categóricos.

Resposta: [   ]

**4.** SVM é um algoritmo de aprendizado de máquina supervisionado que pode ser usado para desafios de classificação ou regressão.

Resposta: [   ]

### Comando 4

> A respeito de aprendizagem de máquina, julgue os itens que se seguem.

**5.** O modelo de aprendizado supervisionado ajusta uma função de mapeamento a partir de exemplos rotulados para generalizar dados ainda não vistos.

Resposta: [   ]

**6.** A aplicação de PCA (análise de componentes principais) em contexto não supervisionado independe de rótulos para extrair componentes de maior variância.

Resposta: [   ]

### Comando 5

> Em relação a tecnologias de IA e aprendizado de máquina, julgue os itens que se seguem.

**7.** A geração de linguagem natural é uma tecnologia capaz de criar texto similar ao texto escrito por seres humanos.

Resposta: [   ]

**8.** Técnicas de clustering são comuns em sistemas de recomendação para recomendar conteúdos aos usuários de forma individualizada.

Resposta: [   ]

### Comando 6

> Julgue os próximos itens, em relação a aprendizado supervisionado e não supervisionado.

**9.** Modelos de aprendizado não supervisionado são utilizados em três tarefas principais, entre as quais está a redução de dimensionalidade, que é uma técnica usada para se reduzir o número de entradas de dados a um tamanho gerenciável, não havendo, nesse caso, preservação da integridade do conjunto de dados.

Resposta: [   ]

**10.** No aprendizado supervisionado, os algoritmos de Naive Bayes e o de máquinas de vetores de suporte são utilizados tanto na classificação quanto na regressão.

Resposta: [   ]

### Comando 7

> Em relação à inteligência artificial e a suas técnicas, bem como aos sistemas de recomendação, julgue os itens subsequentes.

**11.** A classe de algoritmos denominada classificação é utilizada no grupo de aprendizado não supervisionado; esse modelo aprende a executar uma tarefa a partir de dados não rotulados (sem um resultado conhecido), apenas com base em suas características e padrões semelhantes.

Resposta: [   ]

### Comando 8

> Uma empresa recebe inúmeras solicitações de atendimento referentes à garantia de seus produtos. Cada solicitação descreve o defeito alegado pelo cliente, a data de compra do produto ou serviço e outros detalhes. A empresa deseja implantar um sistema que decida automaticamente se uma solicitação deve ser aprovada ou negada, com base em exemplos históricos de solicitações. A partir da situação hipotética precedente, julgue os itens a seguir, que versam sobre inteligência artificial e assuntos correlatos.

**12.** O algoritmo de regressão linear é indicado para resolver o problema em questão, pois estima valores contínuos, que podem ser usados para decidir pela aprovação ou pela negação.

Resposta: [   ]

**13.** O aprendizado de máquina não supervisionado é a escolha ideal atender às condições apresentadas, pois o sistema aprende a aprovar ou a negar sem dados rotulados.

Resposta: [   ]

**14.** A situação descrita representa um problema de classificação.

Resposta: [   ]

### Comando 9

> Julgue os itens seguintes, relativos a inteligência artificial (IA).

**15.** A análise preditiva é uma aplicação da IA em que são utilizadas técnicas de aprendizado de máquina para a previsão de resultados futuros com base em dados históricos.

Resposta: [   ]

[ADERÊNCIA EM ARBITRAGEM — T-03: banco: 5.3 (alt. 5.2); QA 09/10: INDIRETA em 5.3]  

**16.** A IA generativa consiste em técnicas de IA baseadas prioritariamente na utilização de aprendizado supervisionado para a criação de novas amostras de dados que se assemelham aos dados de treinamento.

Resposta: [   ]

### Comando 10

> Em relação aos grandes modelos de linguagem (LLM) e à inteligência artificial generativa, julgue os itens subsequentes.

**17.** O parâmetro temperature em LLM regula a amplitude da diversidade e criatividade nas previsões produzidas pelo modelo.

Resposta: [   ]

**18.** Uma thread representa uma entidade que pode ser configurada para responder às mensagens de um usuário a partir de vários parâmetros, como modelo, instruções e ferramentas.

Resposta: [   ]

[ADERÊNCIA EM ARBITRAGEM — T-03: QA 09/10: INDIRETA (conceito de API de fornecedor, não nomeado no edital)]  
[VOLÁTIL — dependência de produto; reverificação 4–8/1/2027 (T-16); inapto a simulado final]  

### Comando 11

> Acerca de inteligência artificial (IA), julgue os seguintes itens.

**19.** Nos modelos generativos baseados em difusão, como o stable diffusion, o processo de geração de imagens ocorre por meio da aplicação sequencial de ruído gaussiano em uma imagem inicial em branco, consoante o mesmo procedimento do treinamento, mas em escala reduzida, para otimizar o tempo de processamento.

Resposta: [   ]

### Comando 12

> No que se refere a inteligências artificiais (IAs) generativas e discriminativas, julgue os itens seguintes.

**20.** Para aplicações do mundo real, como geração de imagens, as distribuições são extremamente complexas, e o aprendizado profundo não conseguiu melhorar o desempenho dos modelos generativos, por isso se tem optado por investir em uma classe importante de modelos de linguagem de grande escala (LLMs — large language models) autorregressivos baseados em transformadores.

Resposta: [   ]

**21.** Um prompt é um conjunto de instruções que o modelo generativo utiliza para prever a resposta desejada.

Resposta: [   ]

**22.** Uma IA generativa cujo aprendizado é realizado a partir da distribuição de probabilidade conjunta p(x,y), em que x é o dado de entrada e y é o rótulo que se queira classificar, pode gerar mais amostras por si só artificialmente, com base em suposições a respeito da distribuição de dados.

Resposta: [   ]

**23.** O ChatGPT e o DeepSeek são plataformas de IA generativas baseadas em modelos de linguagem de grande escala (LLMs — large language models) e o princípio tecnológico dessas plataformas é a arquitetura transformer, que ajuda o modelo a aprender as relações entre palavras e frases em longos trechos de texto.

Resposta: [   ]

[VOLÁTIL — dependência de produto; reverificação 4–8/1/2027 (T-14); inapto a simulado final]  

### Comando 13

> Julgue os itens a seguir, relativos à inteligência artificial (IA).

**24.** Deepfakes são vídeos gerados por IA para produzir conteúdo altamente realista e podem ser criados por meio de rede adversária generativa (GAN), a qual corresponde a uma arquitetura de aprendizado profundo que treina duas redes neurais para competirem entre si.

Resposta: [   ]

**25.** LLM (Large Language Models) são modelos de aprendizado profundo pré-treinados em grandes quantidades de dados que podem ser utilizados para gerar texto e outros conteúdos, além de executar outras tarefas de processamento de linguagem natural.

Resposta: [   ]

### Comando 14

> Em relação à privacidade em governança e ética de inteligência artificial, julgue o item seguinte.

**26.** De acordo com os princípios de governança e ética relativos à inteligência artificial, a opacidade sobre os algoritmos é encorajada como prática padrão para garantir a eficácia dos sistemas.

Resposta: [   ]

[ADERÊNCIA EM ARBITRAGEM — T-03: QA 09/10: INDIRETA em P1-6 (ética de IA em geral, não de serviço público); alt. P2-4.2]  

### Comando 15

> De acordo com as Resoluções n.º 468/2022, n.º 396/2021, n.º 335/2020 e n.º 332/2020 da Presidência do CNJ, julgue os itens a seguir.

**27.** A impossibilidade de eliminação do viés discriminatório de um modelo de inteligência artificial não enseja a imediata descontinuidade de sua utilização, devendo-se adotar medidas corretivas e efetuar o registro de seu projeto.

Resposta: [   ]

### Comando 16

> Acerca do processo ETL (extrair, transformar, carregar) e da manipulação, do tratamento e da visualização de dados, julgue os itens que se seguem.

**28.** A limpeza de dados consiste no processo de reorganização dos dados para a garantia de sua qualidade e consistência.

Resposta: [   ]

### Comando 17

> A respeito de indicadores, medidas, métricas, metas e KPIs, julgue os seguintes itens.

**29.** Uma medida representa um dado bruto coletado diretamente de um processo, sem qualquer interpretação, como, por exemplo, a quantidade de sacas de café colhidas em um dia. Por sua vez, uma métrica é uma medida analisada em um contexto específico e pode envolver cálculos e comparações, como é o caso, por exemplo, da produtividade média de uma lavoura por hectare ao longo de uma safra.

Resposta: [   ]

**30.** Os indicadores-chave de desempenho (KPIs) possuem características distintas, incluindo-se faixas de desempenho codificadas, que podem ser representadas visualmente, prazos para o atingimento das metas e benchmarks que servem como referência para a avaliação do desempenho.

Resposta: [   ]

[ADERÊNCIA PARCIAL — KPIs: faixas de desempenho, prazos de meta e benchmarks (gestão de desempenho) vão além de "conceitos, atributos, métricas" do 7.1]  

### Comando 18

> A respeito de técnicas de visualização de dados, julgue o item subsequente.

**31.** Na visualização de um conjunto complexo de dados, o uso de gráficos permite a exibição de plotagens e diagramas, organizados ao longo de dois eixos.

Resposta: [   ]

[ADERÊNCIA EM ARBITRAGEM — T-03: banco: 8.1 (alt. 8.2); QA 09/10: INDIRETA nos dois]  

### Comando 19

> A respeito de visualização, análise exploratória de dados e geoprocessamento, julgue os seguintes itens.

**32.** A definição de seções implícitas pode ser realizada pela utilização de formas coloridas e pela sobreposição de elementos visuais alinhados, o que confere uma clara distinção entre diferentes áreas do layout dos dashboards.

Resposta: [   ]

**33.** No contexto de um layout de relatório, o equilíbrio assimétrico consiste na distribuição do peso uniforme dos objetos em ambas as metades da página, independentemente do tamanho dos objetos.

Resposta: [   ]

### Comando 20

> Acerca de técnicas e métodos estatísticos para a análise de dados agrícolas, julgue os itens que se seguem.

**34.** Boxplots são úteis para comparar a variabilidade da qualidade das culturas entre diferentes tratamentos agrícolas, pois destacam a mediana, a dispersão dos dados e os possíveis valores atípicos.

Resposta: [   ]

### Comando 21

> Julgue os itens a seguir, a respeito da análise exploratória de dados.

**35.** Em um dashborad interativo desenvolvido com a finalidade de monitorar a produtividade agrícola de diferentes culturas ao longo dos meses, um gráfico de barras empilhado será sempre a melhor escolha para se comparar a variação da produção entre as culturas ao longo do tempo, pois permite visualizar tanto os totais combinados quanto às contribuições individuais de cada cultura, sem perda de informação.

Resposta: [   ]

**36.** Em um box-plot, se um valor for menor que o primeiro quartil menos 1,5 vezes o intervalo interquartil, esse valor deve ser tratado como um outlier e removido da base de dados antes de qualquer análise adicional.

Resposta: [   ]

### Comando 22

> Acerca de monitoramento e observabilidade de sistemas de TI, julgue os itens subsequentes.

**37.** O Grafana é capaz de fazer queries em diferentes tipos de data source, transformar os dados obtidos e gerar a visualização em forma de dashboard.

Resposta: [   ]

[ADERÊNCIA PARCIAL — ferramenta fora da lista do 8.3 (Power BI, Tableau, Data Studio)]  
[VOLÁTIL — dependência de produto; reverificação 4–8/1/2027 (T-16); inapto a simulado final]  

### Comando 23

> Julgue os itens a seguir, a respeito de sistema gerenciador de banco de dados relacional e NoSQL.

**38.** Kibana é uma ferramenta que permite visualizar os dados armazenados no Elasticsearch, com possibilidade de gerar gráficos convencionais ou widgets integrados, como mapas, lens e canvas.

Resposta: [   ]

[ADERÊNCIA PARCIAL — ferramenta fora da lista do 8.3 (Power BI, Tableau, Data Studio)]  
[VOLÁTIL — dependência de produto; reverificação 4–8/1/2027 (T-16); inapto a simulado final]  

### Comando 24

> Julgue os próximos itens, a respeito de computação e de programação.

**39.** As ferramentas de business intelligence, como o Tableau e o Power BI, são utilizadas para criação de dashboards e não possuem funcionalidades para análise de dados ou integração com bancos de dados.

Resposta: [   ]

## Parte P2 — Conhecimentos Específicos (Reconhecimento de Fala, Transcrição e IA, itens 1 a 4 do edital)

Os itens abaixo tomam por base o item 14.2.4 do edital (Cargo 11, itens 1.1 a 4.3).

### Comando 25

> Julgue os próximos itens, com base no disposto na Lei Geral de Proteção de Dados Pessoais (LGPD).

**40.** O titular tem direito ao acesso facilitado às informações sobre o tratamento de seus dados, que deverão ser disponibilizadas de forma clara e adequada, excetuando-se, por questões de segurança, a identificação do controlador.

Resposta: [   ]

[ADERÊNCIA PARCIAL — LGPD/privacidade geral; o 4.1 trata de LGPD em sistemas de transcrição e IA]  

**41.** Quando houver tratamento para fins exclusivos de segurança pública ou defesa nacional, a Autoridade Nacional de Proteção de Dados (ANPD) deve ser comunicada previamente pois a ela compete zelar pela proteção dos dados pessoais.

Resposta: [   ]

[ADERÊNCIA PARCIAL — LGPD/privacidade geral; o 4.1 trata de LGPD em sistemas de transcrição e IA]  

**42.** Considere que determinado tribunal de justiça seja controlador dos dados de certo titular e tenha deste obtido consentimento para o tratamento de seus dados pessoais. Nessa situação, caso haja necessidade de o referido tribunal compartilhar os dados do referido titular com o CNJ de forma absoluta, não será necessário novo consentimento do titular.

Resposta: [   ]

[ADERÊNCIA PARCIAL — LGPD/privacidade geral; o 4.1 trata de LGPD em sistemas de transcrição e IA]  

**43.** O tratamento de dados pessoais deve ser realizado mediante o consentimento do titular, ficando dispensada tal exigência para os dados tornados manifestamente públicos pelo titular.

Resposta: [   ]

[ADERÊNCIA PARCIAL — LGPD/privacidade geral; o 4.1 trata de LGPD em sistemas de transcrição e IA]  

### Comando 26

> Julgue os próximos itens, relativos ao tratamento de dados pessoais no poder público, conforme orientação da ANPD.

**44.** Segundo o princípio da necessidade, o tratamento de dados deve ser limitado ao mínimo necessário para a realização de suas finalidades, logo deve abranger apenas os dados pertinentes, proporcionais e não excessivos em relação às suas finalidades.

Resposta: [   ]

[ADERÊNCIA PARCIAL — LGPD/privacidade geral; o 4.1 trata de LGPD em sistemas de transcrição e IA]  

**45.** Quando o tratamento de dados pessoais for necessário para o cumprimento de obrigações e atribuições legais, caso em que o cidadão não possui condições efetivas de se manifestar livremente sobre o uso de seus dados pessoais, o consentimento do titular não constitui a base legal mais apropriada para o tratamento de dados pessoais pelo poder público.

Resposta: [   ]

[ADERÊNCIA PARCIAL — LGPD/privacidade geral; o 4.1 trata de LGPD em sistemas de transcrição e IA]  

**46.** Na hipótese de o tratamento de dados pessoais pelo poder público ser realizado para o cumprimento de obrigação legal ou regulatória pelo controlador, a obrigação legal decorre de uma norma de conduta, isto é, uma regra que disciplina um comportamento, em geral estabelecendo um fato ou uma hipótese legal, com uma possível consequência jurídica em caso de descumprimento.

Resposta: [   ]

[ADERÊNCIA PARCIAL — LGPD/privacidade geral; o 4.1 trata de LGPD em sistemas de transcrição e IA]  

### Comando 27

> Em relação ao tratamento e à qualidade dos dados no sistema de gerenciamento de informações, julgue os itens subsequentes.

**47.** De acordo com a Lei Geral de Proteção de Dados Pessoais (LGPD), os dados pessoais devem ser retidos por um período de cinco anos, mesmo após a conclusão do seu processamento, desde que sejam cumpridos os limites técnicos das atividades em questão.

Resposta: [   ]

[ADERÊNCIA PARCIAL — LGPD/privacidade geral; o 4.1 trata de LGPD em sistemas de transcrição e IA]  

**48.** O agente de tratamento deve demonstrar a adoção de medidas eficazes e capazes de comprovar a observância e o cumprimento das normas de proteção de dados pessoais, bem como demonstrar a eficácia dessas medidas.

Resposta: [   ]

[ADERÊNCIA PARCIAL — LGPD/privacidade geral; o 4.1 trata de LGPD em sistemas de transcrição e IA]  

### Comando 28

> No que se refere à governança de dados, julgue os próximos itens.

**49.** De acordo com a LGPD, dados pessoais relacionados a convicção religiosa são considerados sensíveis e só podem ser tratados com o consentimento específico e destacado do titular ou de seu representante legal.

Resposta: [   ]

[ADERÊNCIA PARCIAL — LGPD/privacidade geral; o 4.1 trata de LGPD em sistemas de transcrição e IA]  

### Comando 29

> Julgue os itens subsequentes, relativos a CIS controls, assinatura e certificação digital, segurança em nuvens e ao que dispõe a Lei Geral de Proteção de Dados Pessoais (LGPD).

**50.** De acordo com a LGPD, o tratamento de dados pessoais sensíveis pode ser realizado sem o consentimento do titular, quando o tratamento for necessário para o cumprimento de obrigação legal ou regulatória pelo controlador.

Resposta: [   ]

[ADERÊNCIA PARCIAL — LGPD/privacidade geral; o 4.1 trata de LGPD em sistemas de transcrição e IA]  

### Comando 30

> Com base na Lei Geral de Proteção de Dados Pessoais (LGPD) e no Marco Civil da Internet, julgue os itens a seguir.

**51.** Conforme prescreve o Marco Civil da Internet, configuram-se como princípios que disciplinam o uso da Internet no Brasil a proteção da privacidade e a proteção dos dados pessoais, na forma da lei.

Resposta: [   ]

[ADERÊNCIA PARCIAL — LGPD/privacidade geral; o 4.1 trata de LGPD em sistemas de transcrição e IA]  

**52.** Conforme a LGPD, no âmbito do tratamento de dados pessoais pelo poder público, consideradas a execução de políticas públicas e a prestação de serviços públicos, os dados deverão ser mantidos em formato interoperável e estruturado para uso compartilhado.

Resposta: [   ]

[ADERÊNCIA PARCIAL — LGPD/privacidade geral; o 4.1 trata de LGPD em sistemas de transcrição e IA]  

### Comando 31

> Com base no previsto na Lei n.º 12.527/2011, Lei de Acesso à Informação (LAI), e na Lei n.º 13.709/2018, Lei Geral de Proteção de Dados Pessoais (LGPD), julgue os próximos itens.

**53.** Conforme a LGPD, o tratamento de dados pessoais sensíveis poderá ocorrer sem fornecimento de consentimento do titular, nas hipóteses em que for indispensável para a garantia da prevenção à fraude e à segurança do titular, nos processos de identificação e autenticação de cadastro em sistemas eletrônicos.

Resposta: [   ]

[ADERÊNCIA PARCIAL — LGPD/privacidade geral; o 4.1 trata de LGPD em sistemas de transcrição e IA]  

**54.** A transferência internacional de dados pessoais é permitida a países ou organismos internacionais que tenham legislação equivalente à LGPD.

Resposta: [   ]

[ADERÊNCIA PARCIAL — LGPD/privacidade geral; o 4.1 trata de LGPD em sistemas de transcrição e IA]  

### Comando 32

> Com base na Lei nº 13.709/2018 (LGPD), julgue os próximos itens.

**55.** Pessoa natural ou jurídica que realiza o tratamento de dados pessoais em nome do operador é denominada de controlador.

Resposta: [   ]

[ADERÊNCIA PARCIAL — LGPD/privacidade geral; o 4.1 trata de LGPD em sistemas de transcrição e IA]  

**56.** O tratamento de dados pessoais de crianças pode ser realizado, desde que siga o recomendado no Estatuto da Criança e do Adolescente.

Resposta: [   ]

[ADERÊNCIA PARCIAL — LGPD/privacidade geral; o 4.1 trata de LGPD em sistemas de transcrição e IA]  

### Comando 33

> Julgue os itens a seguir, a respeito da segurança da informação e dos vários tipos de ataques e suas características.

**57.** A integridade é um princípio de segurança da informação que garante que um dado ou uma informação tenham sido alterados sem o registro da ação correspondente, mesmo sob necessidade de auditoria.

Resposta: [   ]

[ADERÊNCIA PARCIAL — princípio geral de segurança da informação; o 4.3 trata de pipelines de áudio e transcrição]  

**58.** Em segurança da informação, a disponibilidade é um princípio que garante, aos usuários, a capacidade de acessar sistemas e(ou) informações quando necessário, mesmo que o sistema ou a infraestrutura esteja sob pressão.

Resposta: [   ]

[ADERÊNCIA PARCIAL — princípio geral de segurança da informação; o 4.3 trata de pipelines de áudio e transcrição]  

### Comando 34

> Acerca de segurança da informação, julgue os itens a seguir.

**59.** Um dos objetivos da integridade é permitir que o destinatário de uma mensagem ou informação seja capaz de verificar que os dados não foram modificados indevidamente.

Resposta: [   ]

[ADERÊNCIA PARCIAL — princípio geral de segurança da informação; o 4.3 trata de pipelines de áudio e transcrição]  

**60.** Autenticidade é um princípio que visa garantir que o autor não negue ter criado e assinado determinada informação, a qual pode estar materializada em uma mensagem ou em um documento.

Resposta: [   ]

[ADERÊNCIA PARCIAL — princípio geral de segurança da informação; o 4.3 trata de pipelines de áudio e transcrição]
