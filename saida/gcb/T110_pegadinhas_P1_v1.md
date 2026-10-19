# T110_pegadinhas_P1_v1.md — T-110 (parte B): 72 pares de P1 convertidos em pegadinhas — 2026-10-18 — gerado por gcb-cpp

Tarefa: T-110 (ordens/ORDEM_V15_B_PARES.md; saida/gcb/V15_BAEF_D1_GCB_2026-10-18.md, seção 2; contrato em saida/pacote/V15_BAE_D1_GBQ_2026-10-18.md, 1.2, item 3).
Base: saida/pacote/pacote.json v1.11, lido em saida/pacote/gerador_v1_11/out/pacote.json, somente leitura (lotes 4, 5, 6a e 6b: campos pares, pegadinhas e curso; os lotes 4-C e 5-C não têm pares). Nenhum pacote, curso, par, pegadinha existente ou item foi alterado.
Produção: gcb-cpp. Esta parte não foi revisada; o parecer de QA é da gcb-cqfp.

## 0. Método e observações

- Cada par recebeu uma decisão: CONVERTIDO ou DESCARTADO. O itemEdital é o tópico cujo bloco de curso, no mesmo lote, ensina a distinção. Nos lotes 6a e 6b as pegadinhas existentes usam o itemEdital do tópico-pai do pacote (P1-1, P1-3, P1-2, P1-2.1, P1-4.1, P1-4.2, P1-4.3), e as novas seguem o mesmo uso.
- Texto: começa com "Não confunda A com B: ", traz o critério de A e o de B separados por ponto e vírgula e, só quando a troca está no curso ou numa pegadinha existente do mesmo tópico, uma frase final "Armadilha: …". Máximo de 320 caracteres (conferido por script: maior texto com 320).
- Sem fato novo: cada afirmação foi localizada no bloco de curso do itemEdital (a coluna de sustentação traz os trechos literais, conferidos por script contra o curso da v1.11). Do campo "como" dos pares só entrou o que o curso também diz.
- Pares de três termos (C1 do lote 4, C14 do lote 6a, C9 do lote 6b) viraram duas pegadinhas, uma por contraste, e contam como um par convertido. No CSV o par tem uma linha e os textos vêm separados por " || ".
- Fatos de ferramenta com data: só Data Studio (nome vigente desde abril de 2026; Looker Studio entre 11/10/2022 e abril de 2026; Looker como plataforma distinta), Power BI Desktop (download gratuito) e Meet (áudio ao apresentar), todos com a data de verificação que o curso já traz (08/10/2026). Nada sobre edição Pro, preço, versão, DAX, Report Server ou macOS. Nenhum par caiu em d4.
- LGPD e normas de ética (lote 4): nenhum texto convertido afirma dispositivo da LGPD. O único texto com norma de ética (C16) usa apenas o Decreto 1.171/1994, Seção I, inciso II, na redação e na data de conferência (08/10/2026, Planalto) que o curso traz; a gcb-gerencia deve submeter esse texto ao qa-normativo antes de qualquer promoção, porque este agente não reabriu a norma. Os pares de LGPD (C12 a C14) e o de direitos autorais (C20) foram descartados; o de ANPD (encarregado, C13) não tem critério de controlador e operador no curso (d3).
- Rótulo: pela regra 5 da D1 (rótulo de pegadinha existente do mesmo itemEdital que nomeia A ou B; senão o mais frequente do itemEdital no lote). Posição (apos): índice base 0 da última pegadinha existente do mesmo itemEdital no lote.

## 1. (a) Tabelas por lote

### Lote 4 (P1-5.1 a 5.3 e P1-6)

| Par | A | B | Decisão | itemEdital | Motivo | Bloco e trecho do curso que sustenta |
|---|---|---|---|---|---|---|
| C1 | Supervisionado | não supervisionado × por reforço | CONVERTIDO | P1-5.2 | — | L4#1 (5.2.2 a 5.2.4): "o modelo aprende a partir de dados ROTULADOS, isto é, exemplos que já trazem a resposta correta" / "o modelo recebe dados SEM rótulos e busca padrões ou estruturas significativas" / "significa SEM RÓTULOS, não" / "recebe RECOMPENSAS ou PENALIDADES" / "constrói uma POLÍTICA" / "não há rótulo com a "resposta certa" para cada entrada" |
| C2 | Modelo generativo | modelo discriminativo | DESCARTADO | P1-5.3 | d1 (duplicata da pegadinha existente de índice 14) | L4#2 (5.3.1, 5.3.2): "Modelo generativo modela a distribuição conjunta p(X, Y)" / "Modelo discriminativo modela a probabilidade condicional p(Y \| X)" |
| C3 | Zero-shot | one-shot × few-shot | CONVERTIDO | P1-5.1 | — | L4#0 (5.1.3): "Zero-shot: prompt sem nenhum exemplo de resposta esperada" / "One-shot: um único exemplo." / "a prompt that contains more than one (a 'few') example" |
| C4 | Chain-of-thought | prompt chaining | CONVERTIDO | P1-5.1 | — | L4#0 (5.1.3): "dividir uma tarefa complexa em vários prompts sequenciais, em que a saída de um alimenta o seguinte" / "no chaining há vários prompts; no chain-of-thought há um prompt que pede raciocínio explícito" |
| C5 | Engenharia de prompts | fine-tuning × RAG | CONVERTIDO | P1-5.1 | — | L4#0 (5.1.1, 5.1.3): "SEM alterar os parâmetros internos do modelo" / "engenharia de prompts atua na ENTRADA; fine-tuning atua nos PARÂMETROS" / "RAG injeta conhecimento NA ENTRADA; fine-tuning altera o MODELO" / "recuperar documentos relevantes" |
| C6 | Temperatura alta | baixa | CONVERTIDO | P1-5.1 | — | L4#0 (5.1.4): "a hyperparameter that controls the degree of randomness of a model's output" / "valores altos geram respostas mais variadas, valores baixos, mais previsíveis" / "Temperatura baixa não significa resposta "mais verdadeira": significa resposta mais determinística." |
| C7 | Regressão | classificação | CONVERTIDO | P1-5.2 | — | L4#1 (5.2.2): "Regressão: prevê um VALOR NUMÉRICO contínuo" / "Classificação: prevê uma CATEGORIA" / "Número → regressão. Categoria → classificação. Ambas supervisionadas" |
| C8 | Clustering | classificação | CONVERTIDO | P1-5.2 | — | L4#1 (5.2.3): "na classificação, as categorias são DEFINIDAS PREVIAMENTE pelo humano e o modelo atribui cada dado a uma delas" / "no clustering, os grupos NÃO são definidos previamente: o modelo os encontra, e o humano pode nomear os grupos" |
| C9 | Alucinação | viés | DESCARTADO | P1-5.3 | d3 (critério ausente do curso: o curso nomeia o viés algorítmico, mas não o define) | L4#2 (5.3.4) e L4#3 (6.2, item 3): "Riscos associados: alucinação (citar lei inexistente), viés" / "Não discriminação e equidade: vigilância contra viés algorítmico" |
| C10 | Modelo de fundação | LLM | CONVERTIDO | P1-5.3 | — | L4#2 (5.3.3): "a very large pre-trained model trained on an enormous and diverse training set" / "Pode ser multimodal." / "at a minimum, a language model having a very high number of parameters" / "nem todo modelo de fundação é LLM" |
| C11 | Conhecimento paramétrico | consulta em tempo real | CONVERTIDO | P1-5.3 | — | L4#2 (5.3.3): "Conhecimento paramétrico e data de corte" / "sem ferramentas ou RAG, o modelo responde com o que incorporou no treinamento; o modelo em si não consulta a internet ou bancos de dados" |
| C12 | Dado pessoal | dado sensível × dado anonimizado (LGPD 5º, I, II, III; 12, caput) | DESCARTADO | P1-6 | d1 (duplicata da pegadinha existente de índice 22) | L4#3 (6.3, LGPD art. 5º e art. 12): "Dados anonimizados (art. 12, caput): não são considerados dados pessoais para os fins da lei, SALVO quando o processo de anonimização for revertido" / "II dado pessoal sensível (origem racial ou étnica" |
| C13 | Controlador | operador × encarregado (LGPD 5º, VI, VII, VIII) | DESCARTADO | P1-6 | d3 (critério ausente do curso: o curso lista controlador e operador no art. 5º sem defini-los; só o encarregado tem definição, o que não dá critério dos dois lados) | L4#3 (6.3, LGPD art. 5º): "VI controlador; VII operador; VIII encarregado" / "encarregado: pessoa indicada pelo controlador e operador para atuar como canal de comunicação entre o controlador, os titulares dos dados e a Agência Nacional de Proteção de Dados (ANPD)" |
| C14 | Consentimento | demais bases legais (LGPD 7º) | DESCARTADO | P1-6 | d1 (duplicata da pegadinha existente de índice 26) | L4#3 (6.3, LGPD art. 7º): "Chave de prova: CONSENTIMENTO NÃO É A ÚNICA BASE, nem a principal para o Poder Público." |
| C15 | Publicidade | sigilo (LAI 3º, I) | DESCARTADO | P1-6 | d1 (duplicata da pegadinha existente de índice 25) | L4#3 (6.3, LAI art. 3º, I): "I publicidade como preceito geral e sigilo como exceção" |
| C16 | Legal | ético (Decreto 1.171, Seção I, II) | CONVERTIDO | P1-6 | — | L4#3 (6.1): "decidindo não apenas entre o legal e o ilegal, mas "principalmente entre o honesto e o desonesto" (conferido no Planalto em 08/10/2026)" / "A ética vai ALÉM da legalidade." |
| C17 | Supervisão humana | automação total | CONVERTIDO | P1-6 | — | L4#3 (6.1, 6.2): "Supervisão humana: decisões relevantes passam por pessoa responsável; a IA apoia, não decide sozinha." / "A ferramenta não responde; o agente público responde." |
| C18 | Usar IA | omitir tecnologia (Decreto 1.171, XV, "e") | DESCARTADO | P1-6 | d1 (duplicata da pegadinha existente de índice 27) | L4#3 (6.3, Decreto 1.171/1994, Seção III, XV, "e"): ""deixar de utilizar os avanços técnicos e científicos ao seu alcance ou do seu conhecimento para atendimento do seu mister"" |
| C19 | Injeção de prompt | jailbreak (conceitos gerais) | DESCARTADO | P1-5.1 | d3 (critério ausente do curso: o curso define a injeção de prompt, mas não traz jailbreak) | L4#0 (5.1.4): "Injeção de prompt (conceito geral, sem fonte de fornecedor no tópico 5.1 de TI e Dados): instruções maliciosas embutidas em textos que o modelo lê" |
| C20 | Texto oficial | obra protegida (Lei 9.610, 8º, IV × 7º) | DESCARTADO | P1-6 | d3 (critério ausente do curso: o art. 8º, IV, está no curso, mas o outro lado, obra protegida, não tem critério no curso; a pegadinha existente de índice 30 já cobre o lado do texto oficial) | L4#3 (6.3, Lei 9.610/1998): "art. 8º, IV — textos de tratados, leis, decretos, regulamentos, decisões judiciais e demais atos oficiais NÃO são objeto de proteção autoral" |

Textos propostos (rótulo; apos; texto):

- C3 (Engenharia de prompts; apos 6; 231 caracteres): Não confunda zero-shot com one-shot e few-shot: o zero-shot traz só a instrução, sem nenhum exemplo; o one-shot traz um único exemplo; o few-shot traz mais de um. Armadilha: definir few-shot como um único exemplo, o que é one-shot.
- C4 (Engenharia de prompts; apos 6; 254 caracteres): Não confunda chain-of-thought com prompt chaining: o chain-of-thought é um único prompt que pede ao modelo que explique o raciocínio passo a passo; o prompt chaining divide a tarefa em vários prompts sequenciais, em que a saída de um alimenta o seguinte.
- C5 (Engenharia de prompts; apos 6; 244 caracteres): Não confunda engenharia de prompts com fine-tuning e RAG: a engenharia de prompts atua na entrada, sem alterar os parâmetros do modelo; o fine-tuning altera os parâmetros; o RAG recupera documentos e os insere no prompt, sem retreinar o modelo.
- C6 (Engenharia de prompts; apos 6; 268 caracteres): Não confunda temperatura alta com temperatura baixa: a temperatura controla o grau de aleatoriedade da saída; a alta gera respostas mais variadas, a baixa, mais previsíveis. Armadilha: temperatura baixa não torna a resposta mais verdadeira, apenas mais determinística.
- C1.1 (Aprendizado supervisionado, não supervisionado e por reforço; apos 13; 302 caracteres): Não confunda aprendizado supervisionado com não supervisionado: o supervisionado aprende com dados rotulados, que já trazem a resposta correta; o não supervisionado recebe dados sem rótulos e busca padrões ou estruturas. Armadilha: não supervisionado significa sem rótulos, não sem participação humana.
- C1.2 (Aprendizado supervisionado, não supervisionado e por reforço; apos 13; 307 caracteres): Não confunda aprendizado não supervisionado com aprendizado por reforço: o não supervisionado busca estrutura em dados sem rótulos; no reforço, o agente age em um ambiente, recebe recompensas ou penalidades e constrói uma política. Armadilha: no reforço não há rótulo com a resposta certa para cada entrada.
- C7 (Aprendizado supervisionado, não supervisionado e por reforço; apos 13; 274 caracteres): Não confunda regressão com classificação: a regressão prevê um valor numérico contínuo, como o preço futuro de uma casa; a classificação prevê uma categoria, como um e-mail ser spam ou não. Armadilha: atribuir à regressão a previsão de categorias; ambas são supervisionadas.
- C8 (Aprendizado supervisionado, não supervisionado e por reforço; apos 13; 253 caracteres): Não confunda clustering com classificação: na classificação, as categorias são definidas previamente pelo humano e o modelo atribui cada dado a uma delas; no clustering, o modelo encontra os grupos em dados sem rótulos, e o humano pode nomeá-los depois.
- C10 (IA generativa: conceitos, exemplos e casos de uso; apos 21; 284 caracteres): Não confunda modelo de fundação com LLM: o modelo de fundação é um modelo muito grande, pré-treinado em um conjunto enorme e diverso, que pode ser multimodal; o LLM é, no mínimo, um modelo de linguagem com número muito alto de parâmetros. Armadilha: nem todo modelo de fundação é LLM.
- C11 (IA generativa: conceitos, exemplos e casos de uso; apos 21; 241 caracteres): Não confunda conhecimento paramétrico com consulta em tempo real: o conhecimento paramétrico é o que o modelo incorporou no treinamento, até a data de corte; sem ferramentas ou RAG, o modelo em si não consulta a internet nem bancos de dados.
- C16 (Ética e responsabilidade digital no serviço público; apos 31; 309 caracteres): Não confunda o que é legal com o que é ético: o legal separa o legal do ilegal; o ético, segundo o Código de Ética do Servidor Público Civil Federal (Decreto 1.171/1994, Seção I, II, conferido no Planalto em 08/10/2026), separa principalmente o honesto do desonesto. Armadilha: a ética vai além da legalidade.
- C17 (Ética e responsabilidade digital no serviço público; apos 31; 280 caracteres): Não confunda supervisão humana com automação total: com supervisão humana, a IA apoia e a pessoa responsável decide e responde pelo ato; a IA não decide sozinha. Armadilha: a responsabilidade não se transfere ao sistema, pois a ferramenta não responde e o agente público responde.

### Lote 5 (P1-7.1 e P1-8.1 a 8.4)

| Par | A | B | Decisão | itemEdital | Motivo | Bloco e trecho do curso que sustenta |
|---|---|---|---|---|---|---|
| C1 | Histograma | gráfico de barras | CONVERTIDO | P1-8.2 | — | L5#2 (histograma; barras): "mostra a distribuição de frequência de uma variável quantitativa" / "adjacentes de uma escala numérica. Por isso as barras são contíguas e a ordem das classes é fixa" / "compara valores entre categorias discretas" / "o espaçamento entre as barras é convenção de desenho" |
| C2 | Linha | dispersão | CONVERTIDO | P1-8.2 | — | L5#2 (linha; dispersão): "liga pontos sucessivos para mostrar a evolução de uma variável ao longo de um eixo horizontal ordenado, tipicamente o tempo" / "cada ponto é uma observação com coordenadas em duas variáveis quantitativas; revela relação (direção, força, forma), agrupamentos e outliers" / "Correlação visível não prova causalidade." |
| C3 | Box plot | histograma | CONVERTIDO | P1-8.2 | — | L5#2 (box plot; histograma): "A caixa vai do 1º quartil (Q1) ao 3º quartil (Q3)" / "A linha interna é a mediana" / "Não mostra a forma detalhada da distribuição (bimodalidade), que o histograma mostra." / "mostra a distribuição de frequência de uma variável quantitativa" |
| C4 | Média | mediana | CONVERTIDO | P1-7.1 | — | L5#0 (7.1.3): "média (sensível a valores extremos); mediana (valor do meio; robusta a extremos)" / "um PL de 20 anos puxa a média para cima; a mediana descreve melhor o "PL típico"" / "afirmar que a média é a medida válida para dado ordinal (são a mediana e a moda)" |
| C5 | Atributo | métrica (dimensão × medida) | CONVERTIDO | P1-7.1 | — | L5#0 (7.1.2, 7.1.3): "dimensões são os atributos pelos quais se fatia a análise; métricas são o que se mede" / "Métrica (medida) é valor quantitativo mensurável, em geral resultado de agregação" / "o número do projeto é identificador" |
| C6 | Transformação | limpeza | CONVERTIDO | P1-7.1 | — | L5#0 (7.1.4): "Transformar é alterar forma, escala, conteúdo ou estrutura dos dados" / "Limpeza de dados: correção de problemas de qualidade — duplicatas, valores ausentes, erros de digitação, formatos inconsistentes" / "limpeza corrige qualidade; agregar e derivar não é limpar" |
| C7 | Normalização | padronização | CONVERTIDO | P1-7.1 | — | L5#0 (7.1.4): "normalização (reescalar para um intervalo, ex.: 0–1) e padronização (média 0, desvio 1)" / "usar normalização e padronização como sinônimos em item que exige a distinção" |
| C8 | ETL | ELT | CONVERTIDO | P1-7.1 | — | L5#0 (7.1.4): "no fluxo ETL (extrair, transformar, carregar), a transformação precede a carga; no ELT, ocorre após a carga, no destino" |
| C9 | Paleta sequencial | divergente × categórica | CONVERTIDO | P1-8.1 | — | L5#1 (8.1): "paleta qualitativa/categórica para categorias, sequencial para magnitude ordenada, divergente para desvios em torno de um ponto central" / "usar paleta sequencial ou divergente para categorias sem ordem" |
| C10 | Posição | área/cor | CONVERTIDO | P1-8.1 | — | L5#1 (8.1, percepção): "a precisão de leitura segue a ordem posição em escala comum > comprimento > ângulo/inclinação > área > volume/cor; daí barras serem lidas com mais exatidão que pizzas" |
| C11 | Data Studio | Looker Studio × Looker | CONVERTIDO | P1-8.3 | — | L5#3 (8.3, Data Studio): "Nome vigente: Data Studio" / "em 11/10/2022 passou a chamar-se Looker Studio" / "em abril de 2026 voltou a chamar-se Data Studio" / "Looker as our enterprise business intelligence platform" / "Produto distinto do Data Studio/Looker Studio." |
| C12 | Tableau Cloud | Tableau Server | DESCARTADO | P1-8.3 | d1 (duplicata da pegadinha existente de índice 36) | L5#3 (8.3, Tableau): "Tableau Cloud — "A fully hosted cloud-based enterprise-grade analytics platform"" / "Tableau Server — "A self-hosted platform, either on-premises or in a public cloud"" |
| C13 | Power BI Desktop | serviço do Power BI | CONVERTIDO | P1-8.3 | — | L5#3 (8.3, Power BI): "the development tool available to data analysts and other report creators" / "available to download for free" / "allows you to organize, manage, and distribute your reports and other Power BI items" / "also allows you to create high-level dashboards that drill down to reports" |
| C14 | Storytelling | dashboard | CONVERTIDO | P1-8.4 | — | L5#4 (8.4): "combinação de três elementos — dados, elementos visuais e narrativa" / "Difere do dashboard (exploração aberta, muitos indicadores)" / "o storytelling tem uma mensagem central" |
| C15 | Explanatória | exploratória | CONVERTIDO | P1-8.4 | — | L5#4 (8.4): "Diferenciar análise exploratória (o analista investiga para descobrir) de explanatória (o público é conduzido a uma mensagem já definida)." |

Textos propostos (rótulo; apos; texto):

- C4 (MÉTRICAS; apos 14; 258 caracteres): Não confunda média com mediana: a média é sensível a valores extremos; a mediana, valor do meio, é robusta a extremos, e por isso descreve melhor o caso típico quando há um valor muito alto. Armadilha: para dado ordinal valem a mediana e a moda, não a média.
- C5 (ATRIBUTOS; apos 14; 317 caracteres): Não confunda atributo com métrica: o atributo (dimensão) é a coluna pela qual se fatia a análise, como o partido; a métrica é o valor quantitativo mensurável, em geral resultado de agregação, como o número de proposições. Armadilha: coluna numérica não é automaticamente métrica (o número do projeto é identificador).
- C6 (TRANSFORMAÇÃO DE DADOS; apos 14; 303 caracteres): Não confunda transformação com limpeza: a transformação altera forma, escala, conteúdo ou estrutura dos dados, como agregar, derivar e normalizar; a limpeza corrige problemas de qualidade, como duplicatas, valores ausentes e erros de digitação. Armadilha: tratar agregar ou derivar como se fosse limpar.
- C7 (TRANSFORMAÇÃO DE DADOS; apos 14; 228 caracteres): Não confunda normalização com padronização: a normalização reescala os dados para um intervalo, como de 0 a 1; a padronização leva os dados a média 0 e desvio 1. Armadilha: tratá-las como sinônimos em item que exige a distinção.
- C8 (TRANSFORMAÇÃO DE DADOS; apos 14; 159 caracteres): Não confunda ETL com ELT: no ETL (extrair, transformar, carregar), a transformação precede a carga; no ELT, a transformação ocorre depois da carga, no destino.
- C9 (Princípios de visualização de dados; apos 19; 256 caracteres): Não confunda paleta sequencial com divergente e categórica: a sequencial representa magnitude ordenada; a divergente, desvios em torno de um ponto central; a categórica, categorias. Armadilha: usar paleta sequencial ou divergente para categorias sem ordem.
- C10 (Princípios de visualização de dados; apos 19; 312 caracteres): Não confunda posição com área ou cor na leitura de um gráfico: segundo Cleveland e McGill, a precisão decresce de posição em escala comum a comprimento, ângulo, área e, por fim, volume ou cor; por isso barras são lidas com mais exatidão que pizzas. Armadilha: afirmar que área ou cor comparam melhor que posição.
- C1 (Histograma; apos 32; 298 caracteres): Não confunda histograma com gráfico de barras: o histograma mostra a distribuição de uma variável quantitativa em classes adjacentes de escala numérica, com barras contíguas; o de barras compara valores entre categorias discretas. Armadilha: o espaçamento entre as barras é só convenção de desenho.
- C2 (Gráfico de linha; apos 32; 320 caracteres): Não confunda gráfico de linha com gráfico de dispersão: a linha liga pontos sucessivos e mostra a evolução de uma variável em eixo ordenado, em geral o tempo; a dispersão tem observações com coordenadas em duas variáveis quantitativas e revela relação e agrupamentos. Armadilha: correlação visível não prova causalidade.
- C3 (Box plot (diagrama de caixa); apos 32; 291 caracteres): Não confunda box plot com histograma: o box plot resume a distribuição pelos quartis, com a mediana na linha interna, bigodes e outliers, e permite comparar grupos; o histograma mostra a frequência por classe e, assim, a forma da distribuição, como a bimodalidade, que o box plot não mostra.
- C11 (Data Studio (Google); apos 42; 280 caracteres): Não confunda Data Studio com Looker Studio e Looker: Data Studio é o nome vigente desde abril de 2026; o mesmo produto se chamou Looker Studio entre 11/10/2022 e abril de 2026; o Looker é uma plataforma de BI corporativa, produto distinto (Google Cloud, verificado em 08/10/2026).
- C13 (Power BI (Microsoft); apos 42; 318 caracteres): Não confunda Power BI Desktop com serviço do Power BI: o Desktop é a ferramenta de desenvolvimento, de download gratuito, em que se conecta aos dados e se cria o relatório; o serviço, plataforma on-line, organiza, gerencia e distribui os relatórios e também cria dashboards (Microsoft Learn, verificado em 08/10/2026).
- C14 (Storytelling para visualização de dados; apos 47; 250 caracteres): Não confunda storytelling com dashboard: o storytelling com dados combina dados, elementos visuais e narrativa em torno de uma mensagem central, para conduzir o público a uma conclusão ou ação; o dashboard é exploração aberta, com muitos indicadores.
- C15 (Storytelling para visualização de dados; apos 47; 186 caracteres): Não confunda análise exploratória com explanatória: na exploratória, o analista investiga os dados para descobrir algo; na explanatória, o público é conduzido a uma mensagem já definida.

### Lote 6a (P1-1 e P1-3)

| Par | A | B | Decisão | itemEdital | Motivo | Bloco e trecho do curso que sustenta |
|---|---|---|---|---|---|---|
| C1 | Referência relativa | absoluta × mista (Excel) | CONVERTIDO | P1-1 | — | L6A#2 (1.2.2): "Por padrão, uma referência de célula é RELATIVA: muda de posição conforme a fórmula é copiada" / "por exemplo $B$2" / "fixando só a coluna ($B2) ou só a linha (B$2)" / "O $ TRAVA o que vem imediatamente depois dele." |
| C2 | Mesclar | dividir células (Word) | DESCARTADO | P1-1 | d1 (duplicata da pegadinha existente de índice 2) | L6A#1 (1.1.3): "MESCLAR = muitas células viram uma; DIVIDIR = uma célula vira várias." |
| C3 | Ocultar | resolver alterações controladas (Word) | CONVERTIDO | P1-1 | — | L6A#1 (1.1.2, 1.1.5): "o modo "Sem Marcação" só oculta as alterações temporariamente, e elas voltam a aparecer quando o documento é reaberto" / "Ocultar muda só a exibição; aceitar/rejeitar decide o conteúdo." / "só trocar o modo para "Sem Marcação" NÃO limpa o arquivo" |
| C4 | Aceitar | rejeitar alteração (Word) | CONVERTIDO | P1-1 | — | L6A#1 (1.1.2): "ACEITAR (incorpora a alteração ao texto) × REJEITAR (descarta a alteração, restabelecendo o texto original)" / "apenas navegam, sem decidir" |
| C5 | Sumário automático | digitado à mão | CONVERTIDO | P1-1 | — | L6A#1 (1.1.4): "Os sumários no Word se baseiam nos títulos do documento." / "clica-se com o botão direito no sumário e escolhe-se "Atualizar Campo"" / "digitar manualmente "Capítulo 1 ...... 3" não cria estrutura que o Word reconheça" / "o sumário automático é GERADO a partir dos estilos de título" |
| C6 | SE: verdadeiro | falso | DESCARTADO | P1-1 | d1 (duplicata da pegadinha existente de índice 10; a de índice 11 completa com o terceiro argumento opcional) | L6A#2 (1.2.3): "O primeiro resultado vale se a comparação for Verdadeira; o segundo, se for Falsa." / "O colchete na sintaxe indica o argumento opcional (valor_se_falso)." |
| C7 | PROCV exata | aproximada | CONVERTIDO | P1-1 | — | L6A#2 (1.2.4): "com FALSO, devolve correspondência EXATA; com VERDADEIRO, ou deixando o argumento em branco, devolve correspondência APROXIMADA (o valor mais próximo que não ultrapasse o procurado)" / "Omitir o quarto argumento NÃO equivale a FALSO." |
| C8 | PROCV | ÍNDICE/CORRESP (direção da pesquisa) | CONVERTIDO | P1-1 | — | L6A#2 (1.2.4): "só pode pesquisar um valor da esquerda para a direita" / "caso contrário, recomenda ÍNDICE e CORRESP" |
| C9 | Animação | transição (PowerPoint) | DESCARTADO | P1-1 | d1 (duplicata da pegadinha existente de índice 12; a de índice 14 completa com uma transição por slide) | L6A#3 (1.3.3): "ANIMAÇÃO = efeito num OBJETO dentro do slide; TRANSIÇÃO = efeito na MUDANÇA DE SLIDE." |
| C10 | Slide mestre | alteração em slide isolado | DESCARTADO | P1-1 | d1 (duplicata da pegadinha existente de índice 13) | L6A#3 (1.3.2): "Quando você edita o slide mestre, todos os slides baseados nele conterão essas alterações." / "alterar um slide individual muda só aquele" |
| C11 | Compartilhar com exibição | com edição (OneDrive) | CONVERTIDO | P1-1 | — | L6A#4 (1.4.2): "EXIBIR = ler; EDITAR = ler e alterar. Compartilhar não transfere a propriedade do arquivo" |
| C12 | Restaurar versão | descartar a atual (OneDrive) | DESCARTADO | P1-1 | d1 (duplicata da pegadinha existente de índice 16) | L6A#4 (1.4.3): "A versão restaurada torna-se a versão atual, e a versão que era a atual passa a aparecer na lista como versão anterior." |
| C13 | Webmail | cliente de e-mail | DESCARTADO | P1-3 | d1 (duplicata da pegadinha existente de índice 21; a de índice 22 completa o lado do cliente) | L6A#6 (3.1.1): "WEBMAIL: acesso à caixa postal por navegador, sem necessidade de aplicativo específico instalado no dispositivo." / "CLIENTE DE E-MAIL: programa de correio próprio, em regra instalado no computador ou no celular" |
| C14 | SMTP | POP3 × IMAP4 | CONVERTIDO | P1-3 | — | L6A#6 (3.1.2): "SMTP: transferência de mensagens" / "permite à estação de trabalho acessar a caixa postal no servidor" / "depende do SMTP para ENVIAR" / "por padrão os clientes POP3 removem as mensagens baixadas do servidor" / "baixam para uma única pasta e não sincronizam várias pastas" / "por padrão os clientes IMAP4 NÃO removem as mensagens baixadas do servidor" / "dão suporte a várias pastas" |
| C15 | Para/Cc | Cco | CONVERTIDO | P1-3 | — | L6A#6 (3.1.3): "Para: destinatários principais. Cc (com cópia): destinatários de ciência; os endereços aparecem para todos" / "Cco RECEBE a mensagem, mas fica OCULTO para os demais." |
| C16 | Equipe | canal (Teams) | CONVERTIDO | P1-3 | — | L6A#7 (3.2.2): "coleções de pessoas, conteúdo e ferramentas que envolvem diferentes projetos e resultados dentro de uma organização" / "Canais são seções dedicadas dentro de uma equipe para manter as conversas organizadas por tópicos, projetos etc." |
| C17 | Canal padrão | privado × compartilhado (Teams) | DESCARTADO | P1-3 | d1 (duplicata das pegadinhas existentes de índice 28, que cobre canal padrão e privado, e de índice 29, que cobre o canal compartilhado) | L6A#7 (3.2.2): "abertos a todos os membros da equipe (canais padrão), a membros selecionados da equipe (canais privados) ou a pessoas selecionadas dentro e fora da equipe (canais compartilhados)" |
| C18 | Apresentar guia | janela × tela inteira (Meet) | CONVERTIDO | P1-3 | — | L6A#8 (3.3.3): "Ao apresentar uma guia do Chrome, o áudio é compartilhado por padrão; em janela ou tela inteira, o áudio do sistema só é compartilhado se a opção "Compartilhar também o áudio do sistema" for ativada." / "(leitura de 08/10/2026)" |
| C19 | Teams | Meet | DESCARTADO | P1-3 | d1 (duplicata da pegadinha existente de índice 32) | L6A#8 (3.3.1): "É produto DISTINTO do Teams: Teams é da Microsoft; Meet é do Google." |

Textos propostos (rótulo; apos; texto):

- C1 (EXCEL; apos 20; 275 caracteres): Não confunda referência relativa com absoluta e mista: a relativa, que é o padrão, muda de posição quando a fórmula é copiada; a absoluta ($B$2) fixa coluna e linha; a mista fixa só a coluna ($B2) ou só a linha (B$2). Armadilha: o $ trava o que vem imediatamente depois dele.
- C3 (WORD; apos 20; 280 caracteres): Não confunda ocultar alterações com resolvê-las no Word: o modo Sem Marcação só oculta as alterações, temporariamente, e elas voltam ao reabrir o documento; aceitar ou rejeitar decide o conteúdo e é o que as remove de fato. Armadilha: trocar para Sem Marcação não limpa o arquivo.
- C4 (WORD; apos 20; 225 caracteres): Não confunda aceitar com rejeitar uma alteração controlada: aceitar incorpora a alteração ao texto; rejeitar a descarta, restabelecendo o texto original. Armadilha: Avançar e Anterior apenas navegam, sem aceitar nem rejeitar.
- C5 (WORD; apos 20; 296 caracteres): Não confunda sumário automático com sumário digitado à mão: o automático é gerado a partir dos títulos com estilo de título e é atualizado com Atualizar Campo; o digitado à mão não cria estrutura que o Word reconheça. Armadilha: dizer que o sumário automático independe da formatação dos títulos.
- C7 (EXCEL; apos 20; 296 caracteres): Não confunda correspondência exata com aproximada no PROCV: com FALSO no quarto argumento, a correspondência é exata; com VERDADEIRO ou com o argumento em branco, é aproximada, isto é, o valor mais próximo que não ultrapasse o procurado. Armadilha: omitir o quarto argumento não equivale a FALSO.
- C8 (EXCEL; apos 20; 242 caracteres): Não confunda PROCV com ÍNDICE e CORRESP quanto à direção da pesquisa: o PROCV só pesquisa da esquerda para a direita, e a coluna do valor procurado precisa estar à esquerda da coluna de retorno; se não estiver, recomendam-se ÍNDICE e CORRESP.
- C11 (ONEDRIVE; apos 20; 213 caracteres): Não confunda compartilhar com exibição e com edição no OneDrive: com exibição, quem recebe o link apenas lê; com edição, lê e altera o arquivo. Armadilha: achar que compartilhar transfere a propriedade do arquivo.
- C14.1 (CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL); apos 34; 238 caracteres): Não confunda SMTP com POP3: o SMTP transfere e envia as mensagens; o POP3 permite à estação acessar a caixa postal no servidor, em geral baixando as mensagens. Armadilha: o POP3 não envia; o programa de e-mail depende do SMTP para enviar.
- C14.2 (CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL); apos 34; 289 caracteres): Não confunda POP3 com IMAP4: por padrão, os clientes POP3 removem as mensagens baixadas do servidor, baixam para uma única pasta e não sincronizam várias pastas; os clientes IMAP4 não as removem por padrão e dão suporte a várias pastas (Microsoft Learn, "POP3 e IMAP4 em Exchange Online").
- C15 (CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL); apos 34; 263 caracteres): Não confunda Para e Cc com Cco: em Para (destinatários principais) e em Cc (ciência), os endereços aparecem para todos; quem está em Cco recebe a cópia, mas seu endereço fica oculto para os demais. Armadilha: dizer que o destinatário em Cco não recebe a mensagem.
- C16 (CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL); apos 34; 239 caracteres): Não confunda equipe com canal no Teams: a equipe é a coleção de pessoas, conteúdo e ferramentas dos projetos e resultados de uma organização; o canal é uma seção dedicada dentro da equipe, que organiza as conversas por tópicos ou projetos.
- C18 (CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL); apos 34; 287 caracteres): Não confunda apresentar uma guia com apresentar uma janela ou a tela inteira no Meet: a guia é uma aba do Chrome, com áudio compartilhado por padrão; na janela ou na tela inteira, o áudio do sistema só é compartilhado se a opção for ativada (Ajuda do Google Meet, leitura de 08/10/2026).

### Lote 6b (P1-2, P1-2.1 e P1-4.1 a 4.3)

| Par | A | B | Decisão | itemEdital | Motivo | Bloco e trecho do curso que sustenta |
|---|---|---|---|---|---|---|
| C1 | LAN | WAN | DESCARTADO | P1-2 | d1 (duplicata da pegadinha existente de índice 0) | L6B#0 (2.0.2): "LAN (rede local): área geográfica restrita" / "WAN (rede de longa distância): interliga redes ou equipamentos em áreas geograficamente distantes" |
| C2 | Internet | Web | CONVERTIDO | P1-2.1 | — | L6B#1 (2.1.1): "rede mundial de computadores formada pela interligação de redes de todo o planeta, que usa o conjunto de protocolos TCP/IP. É a INFRAESTRUTURA." / "serviço que funciona SOBRE a Internet: conjunto de páginas e recursos interligados por hiperlinks, acessados por meio do protocolo HTTP/HTTPS e identificados por URLs" / "Internet e Web NÃO são sinônimos." |
| C3 | Internet | intranet × extranet | CONVERTIDO | P1-2.1 | — | L6B#1 (2.1.1): "\| Internet \| aberto, mundial \| TCP/IP \| sites públicos \|" / "rede PRIVADA de uma organização, que usa as mesmas tecnologias e protocolos da Internet" / "com ACESSO RESTRITO ao público autorizado" / "extensão CONTROLADA da intranet para um público externo autorizado (parceiros, fornecedores, clientes)" |
| C4 | Switch | roteador | DESCARTADO | P1-2 | d1 (duplicata da pegadinha existente de índice 1) | L6B#0 (2.0.4): "Switch (comutador): interliga equipamentos de uma LAN" / "Roteador: interliga REDES DIFERENTES e escolhe o caminho dos pacotes entre elas" |
| C5 | DNS | DHCP | DESCARTADO | P1-2 | d1 (duplicata da pegadinha existente de índice 4; a de índice 10, do tópico 2.1, repete o contraste) | L6B#0 (2.0.5, 2.0.6): "DHCP: serviço que atribui automaticamente endereço IP" / "DNS: traduz nomes de domínio em endereços IP" |
| C6 | TCP | UDP | CONVERTIDO | P1-2 | — | L6B#0 (2.0.6): "TCP entrega os dados de forma confiável, ordenada e com controle de erros; UDP entrega sem essas garantias, com menor atraso (usado em voz e vídeo ao vivo)" |
| C7 | Navegador | mecanismo de busca | CONVERTIDO | P1-2.1 | — | L6B#1 (2.1.3): "Navegador (browser): programa CLIENTE que solicita páginas aos servidores web e as exibe." / "serviço (site) que indexa páginas e as localiza por palavras-chave. O navegador é o programa; a busca é um serviço acessado por meio dele." |
| C8 | Confidencialidade | integridade × disponibilidade | CONVERTIDO | P1-4.1 | — | L6B#3 (4.1.1): "seja acessível SOMENTE a quem está autorizado" / "NÃO seja alterada, apagada ou corrompida de modo não autorizado ou acidental" / "esteja ACESSÍVEL e utilizável por quem está autorizado SEMPRE QUE necessário" |
| C9 | Backup completo | incremental × diferencial | CONVERTIDO | P1-4.1 | — | L6B#3 (4.1.2): "COMPLETO (full): copia TODOS os dados selecionados, independentemente de terem mudado." / "INCREMENTAL: copia SOMENTE o que mudou desde o último backup completo ou incremental e marca os arquivos como copiados" / "a restauração exige o último completo MAIS todos os incrementais até o ponto desejado, na ordem" / "DIFERENCIAL: NÃO marca os arquivos como copiados; por isso, numa rotina de completo + diferenciais, cada diferencial acumula tudo o que mudou desde o último completo" / "A restauração exige o último completo MAIS o último diferencial." |
| C10 | Backup | sincronização | CONVERTIDO | P1-4.1 | — | L6B#3 (4.1.2): "Backup guarda um ponto no tempo; sincronização espelha o estado atual." / "uma exclusão ou uma criptografia por ransomware pode ser replicada; só funciona como backup se houver HISTÓRICO de versões e retenção" |
| C11 | Vírus | worm | CONVERTIDO | P1-4.1 | — | L6B#3 (4.1.4): "insere cópias de si em programas e arquivos (hospedeiros); só age quando o hospedeiro é executado" / "programa independente que se replica e se propaga automaticamente pelas redes, explorando vulnerabilidades ou falhas de configuração" / "NÃO precisa de hospedeiro nem de ação do usuário" |
| C12 | Vírus | trojan | CONVERTIDO | P1-4.1 | — | L6B#3 (4.1.3, 4.1.4): "se propaga inserindo cópias de si mesmo" / "parece um programa legítimo (jogo, planilha, "atualização"), mas executa também funções maliciosas" / "NÃO se replica; depende de o usuário instalá-lo e executá-lo" |
| C13 | Spyware | ransomware | CONVERTIDO | P1-4.1 | — | L6B#3 (4.1.4): "monitora as atividades do usuário e envia as informações a terceiros" / "atinge a confidencialidade" / "torna inacessíveis os dados do equipamento (em geral, por criptografia) e exige resgate para restabelecer o acesso" / "atinge a disponibilidade" / "pagar o resgate não garante a devolução dos dados" |
| C14 | Antivírus | firewall | DESCARTADO | P1-4.2 | d1 (duplicata da pegadinha existente de índice 24) | L6B#4 (4.2.2, 4.2.5): "ANTIVÍRUS = olha ARQUIVOS e PROGRAMAS (detecta e remove malware). FIREWALL = olha TRÁFEGO (permite ou bloqueia conexões por regras)." |
| C15 | Firewall | antispyware | CONVERTIDO | P1-4.2 | — | L6B#4 (4.2.2, 4.2.3): "Mecanismo que CONTROLA o tráfego de rede entre redes ou entre o equipamento e a rede, permitindo ou bloqueando conexões segundo REGRAS" / "Programa voltado a detectar e remover SPYWARE, o código que monitora as atividades do usuário e envia as informações a terceiros" / "a distinção conceitual permanece: a função de cada mecanismo é distinta, ainda que venham juntos" |
| C16 | Phishing | pharming | DESCARTADO | P1-4.3 | d1 (duplicata da pegadinha existente de índice 31; a de índice 32 repete o contraste) | L6B#5 (4.3.2): "PHISHING = engodo ("isca") para a vítima agir" / "PHARMING = redirecionamento da navegação por adulteração da resolução de nomes" |
| C17 | HTTPS | legitimidade do site | CONVERTIDO | P1-4.3 | — | L6B#5 (4.3.4): "o navegador autentica o servidor como responsável pelo DOMÍNIO acessado, e a comunicação ganha confidencialidade e integridade" / "O que o HTTPS NÃO garante: que o domínio seja o da instituição que o usuário pretendia acessar, nem que o titular do site aja de boa-fé." / ""o HTTPS não oferece autenticação alguma" também é erro" |
| C18 | Quarentena | exclusão | DESCARTADO | P1-4.2 | d1 (duplicata da pegadinha existente de índice 30) | L6B#4 (4.2.1): "quarentena (isola o arquivo suspeito)" |

Textos propostos (rótulo; apos; texto):

- C6 (Redes de computadores; apos 4; 198 caracteres): Não confunda TCP com UDP: o TCP entrega os dados de forma confiável, ordenada e com controle de erros; o UDP entrega sem essas garantias, com menor atraso, e por isso é usado em voz e vídeo ao vivo.
- C2 (Conceitos básicos, ferramentas, aplicativos e procedimentos de Internet e intranet; apos 12; 308 caracteres): Não confunda Internet com Web: a Internet é a rede mundial de computadores formada pela interligação de redes, a infraestrutura que usa TCP/IP; a Web é um serviço sobre a Internet, de páginas interligadas por hiperlinks, acessadas por HTTP/HTTPS e identificadas por URLs. Armadilha: tratá-las como sinônimos.
- C3 (Conceitos básicos, ferramentas, aplicativos e procedimentos de Internet e intranet; apos 12; 315 caracteres): Não confunda Internet com intranet e extranet: a Internet é aberta e mundial; a intranet é rede privada de uma organização, de acesso restrito ao público autorizado, com as mesmas tecnologias da Internet; a extranet é a extensão controlada da intranet a um público externo autorizado, como parceiros e fornecedores.
- C7 (Conceitos básicos, ferramentas, aplicativos e procedimentos de Internet e intranet; apos 12; 250 caracteres): Não confunda navegador com mecanismo de busca: o navegador é o programa cliente que solicita páginas aos servidores web e as exibe; o mecanismo de busca é um serviço que indexa páginas e as localiza por palavras-chave, acessado por meio do navegador.
- C8 (Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais; apos 23; 309 caracteres): Não confunda confidencialidade com integridade e disponibilidade: confidencialidade é só quem está autorizado ter acesso; integridade é a informação não ser alterada, apagada ou corrompida de modo não autorizado ou acidental; disponibilidade é ela estar acessível a quem está autorizado sempre que necessário.
- C9.1 (Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais; apos 23; 280 caracteres): Não confunda backup completo com incremental e diferencial: o completo copia todos os dados selecionados, tenham mudado ou não, e a restauração usa o último completo; o incremental e o diferencial copiam apenas o que mudou, e a restauração exige o completo mais cópias adicionais.
- C9.2 (Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais; apos 23; 316 caracteres): Não confunda backup incremental com diferencial: o incremental copia o que mudou desde o último completo ou incremental, marca os arquivos e, na restauração, exige o completo e todos os incrementais; o diferencial não marca os arquivos, acumula o que mudou desde o completo e exige o completo e o último diferencial.
- C10 (Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais; apos 23; 276 caracteres): Não confunda backup com sincronização: o backup guarda um ponto no tempo; a sincronização espelha o estado atual, de modo que uma exclusão ou uma criptografia por ransomware pode ser replicada. Armadilha: a sincronização só funciona como backup se houver histórico e retenção.
- C11 (Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais; apos 23; 287 caracteres): Não confunda vírus com worm: o vírus insere cópias de si em programas e arquivos hospedeiros e só age quando o hospedeiro é executado; o worm é programa independente que se replica e se propaga automaticamente pelas redes, explorando vulnerabilidades, sem hospedeiro nem ação do usuário.
- C12 (Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais; apos 23; 255 caracteres): Não confunda vírus com trojan: o vírus propaga-se inserindo cópias de si em programas e arquivos; o trojan (cavalo de Troia) parece um programa legítimo, mas executa também funções maliciosas, não se replica e depende de o usuário instalá-lo e executá-lo.
- C13 (Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais; apos 23; 302 caracteres): Não confunda spyware com ransomware: o spyware monitora as atividades do usuário e envia as informações a terceiros (confidencialidade); o ransomware torna os dados inacessíveis, em geral por criptografia, e exige resgate (disponibilidade). Armadilha: pagar o resgate não garante a devolução dos dados.
- C15 (Programas de proteção (antivírus, firewall, antispyware); apos 30; 303 caracteres): Não confunda firewall com antispyware: o firewall controla o tráfego de rede, permitindo ou bloqueando conexões segundo regras; o antispyware detecta e remove spyware, que monitora o usuário e envia informações a terceiros. Armadilha: pacotes de segurança que reúnem as funções não eliminam a distinção.
- C17 (Ameaças digitais (phishing, pharming); apos 38; 307 caracteres): Não confunda HTTPS com legitimidade do site: o HTTPS, com certificado digital, autentica o servidor para o domínio acessado e protege a comunicação; ele não garante que o domínio seja o da instituição pretendida nem que o titular aja de boa-fé. Armadilha: dizer que o HTTPS não autentica nada também é erro.

## 2. (b) Contagem

| Lote | Pares | Convertidos | Textos novos | Descartados | d1 | d2 | d3 | d4 | d5 |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| L4 | 20 | 11 | 12 | 9 | 5 | 0 | 4 | 0 | 0 |
| L5 | 15 | 14 | 14 | 1 | 1 | 0 | 0 | 0 | 0 |
| L6A | 19 | 11 | 12 | 8 | 8 | 0 | 0 | 0 | 0 |
| L6B | 18 | 12 | 13 | 6 | 6 | 0 | 0 | 0 | 0 |
| Total | 72 | 48 | 51 | 24 | 20 | 0 | 4 | 0 | 0 |

Soma: 48 convertidos + 24 descartados = 72 pares (esperado 72). Os 48 convertidos geram 51 pegadinhas novas (L4 12, L5 14, L6a 12, L6b 13).
Nenhum descarte por d2 (nenhum par de outro lote de P1 daria o mesmo texto), d4 ou d5; nenhum motivo fora dos cinco fechados.

## 3. (c) Varredura (regra 0.7 da D1)

Regex das categorias da ordem C sobre os 51 textos novos e seus rótulos. Texto da candidata. Contagem de ocorrências:

| Categoria | Ocorrências |
|---|--:|
| 1 Lote N | 0 |
| 2 neste/do lote | 0 |
| 3 códigos de item | 0 |
| 4 códigos de par | 0 |
| 5 etiquetas [V.. / NORMATIVO / F..] | 0 |
| 6 códigos de fonte F/N | 0 |
| 7 prefixos TC/IC/GI/AT | 0 |
| 8 QA/produção/errata/versão | 0 |
| 9 instruções internas | 0 |
| 10 Difere do item | 0 |

Ocorrências da tecla F4: 0. Ocorrências do termo técnico "lote": 0. Meta: zero em todas as linhas; resultado atingido.

## 4. (d) Bloco para a v1.12

```json
{
 "L4": [
  {
   "apos": 6,
   "itemEdital": "P1-5.1",
   "rotulo": "Engenharia de prompts",
   "texto": "Não confunda zero-shot com one-shot e few-shot: o zero-shot traz só a instrução, sem nenhum exemplo; o one-shot traz um único exemplo; o few-shot traz mais de um. Armadilha: definir few-shot como um único exemplo, o que é one-shot."
  },
  {
   "apos": 6,
   "itemEdital": "P1-5.1",
   "rotulo": "Engenharia de prompts",
   "texto": "Não confunda chain-of-thought com prompt chaining: o chain-of-thought é um único prompt que pede ao modelo que explique o raciocínio passo a passo; o prompt chaining divide a tarefa em vários prompts sequenciais, em que a saída de um alimenta o seguinte."
  },
  {
   "apos": 6,
   "itemEdital": "P1-5.1",
   "rotulo": "Engenharia de prompts",
   "texto": "Não confunda engenharia de prompts com fine-tuning e RAG: a engenharia de prompts atua na entrada, sem alterar os parâmetros do modelo; o fine-tuning altera os parâmetros; o RAG recupera documentos e os insere no prompt, sem retreinar o modelo."
  },
  {
   "apos": 6,
   "itemEdital": "P1-5.1",
   "rotulo": "Engenharia de prompts",
   "texto": "Não confunda temperatura alta com temperatura baixa: a temperatura controla o grau de aleatoriedade da saída; a alta gera respostas mais variadas, a baixa, mais previsíveis. Armadilha: temperatura baixa não torna a resposta mais verdadeira, apenas mais determinística."
  },
  {
   "apos": 13,
   "itemEdital": "P1-5.2",
   "rotulo": "Aprendizado supervisionado, não supervisionado e por reforço",
   "texto": "Não confunda aprendizado supervisionado com não supervisionado: o supervisionado aprende com dados rotulados, que já trazem a resposta correta; o não supervisionado recebe dados sem rótulos e busca padrões ou estruturas. Armadilha: não supervisionado significa sem rótulos, não sem participação humana."
  },
  {
   "apos": 13,
   "itemEdital": "P1-5.2",
   "rotulo": "Aprendizado supervisionado, não supervisionado e por reforço",
   "texto": "Não confunda aprendizado não supervisionado com aprendizado por reforço: o não supervisionado busca estrutura em dados sem rótulos; no reforço, o agente age em um ambiente, recebe recompensas ou penalidades e constrói uma política. Armadilha: no reforço não há rótulo com a resposta certa para cada entrada."
  },
  {
   "apos": 13,
   "itemEdital": "P1-5.2",
   "rotulo": "Aprendizado supervisionado, não supervisionado e por reforço",
   "texto": "Não confunda regressão com classificação: a regressão prevê um valor numérico contínuo, como o preço futuro de uma casa; a classificação prevê uma categoria, como um e-mail ser spam ou não. Armadilha: atribuir à regressão a previsão de categorias; ambas são supervisionadas."
  },
  {
   "apos": 13,
   "itemEdital": "P1-5.2",
   "rotulo": "Aprendizado supervisionado, não supervisionado e por reforço",
   "texto": "Não confunda clustering com classificação: na classificação, as categorias são definidas previamente pelo humano e o modelo atribui cada dado a uma delas; no clustering, o modelo encontra os grupos em dados sem rótulos, e o humano pode nomeá-los depois."
  },
  {
   "apos": 21,
   "itemEdital": "P1-5.3",
   "rotulo": "IA generativa: conceitos, exemplos e casos de uso",
   "texto": "Não confunda modelo de fundação com LLM: o modelo de fundação é um modelo muito grande, pré-treinado em um conjunto enorme e diverso, que pode ser multimodal; o LLM é, no mínimo, um modelo de linguagem com número muito alto de parâmetros. Armadilha: nem todo modelo de fundação é LLM."
  },
  {
   "apos": 21,
   "itemEdital": "P1-5.3",
   "rotulo": "IA generativa: conceitos, exemplos e casos de uso",
   "texto": "Não confunda conhecimento paramétrico com consulta em tempo real: o conhecimento paramétrico é o que o modelo incorporou no treinamento, até a data de corte; sem ferramentas ou RAG, o modelo em si não consulta a internet nem bancos de dados."
  },
  {
   "apos": 31,
   "itemEdital": "P1-6",
   "rotulo": "Ética e responsabilidade digital no serviço público",
   "texto": "Não confunda o que é legal com o que é ético: o legal separa o legal do ilegal; o ético, segundo o Código de Ética do Servidor Público Civil Federal (Decreto 1.171/1994, Seção I, II, conferido no Planalto em 08/10/2026), separa principalmente o honesto do desonesto. Armadilha: a ética vai além da legalidade."
  },
  {
   "apos": 31,
   "itemEdital": "P1-6",
   "rotulo": "Ética e responsabilidade digital no serviço público",
   "texto": "Não confunda supervisão humana com automação total: com supervisão humana, a IA apoia e a pessoa responsável decide e responde pelo ato; a IA não decide sozinha. Armadilha: a responsabilidade não se transfere ao sistema, pois a ferramenta não responde e o agente público responde."
  }
 ],
 "L5": [
  {
   "apos": 14,
   "itemEdital": "P1-7.1",
   "rotulo": "MÉTRICAS",
   "texto": "Não confunda média com mediana: a média é sensível a valores extremos; a mediana, valor do meio, é robusta a extremos, e por isso descreve melhor o caso típico quando há um valor muito alto. Armadilha: para dado ordinal valem a mediana e a moda, não a média."
  },
  {
   "apos": 14,
   "itemEdital": "P1-7.1",
   "rotulo": "ATRIBUTOS",
   "texto": "Não confunda atributo com métrica: o atributo (dimensão) é a coluna pela qual se fatia a análise, como o partido; a métrica é o valor quantitativo mensurável, em geral resultado de agregação, como o número de proposições. Armadilha: coluna numérica não é automaticamente métrica (o número do projeto é identificador)."
  },
  {
   "apos": 14,
   "itemEdital": "P1-7.1",
   "rotulo": "TRANSFORMAÇÃO DE DADOS",
   "texto": "Não confunda transformação com limpeza: a transformação altera forma, escala, conteúdo ou estrutura dos dados, como agregar, derivar e normalizar; a limpeza corrige problemas de qualidade, como duplicatas, valores ausentes e erros de digitação. Armadilha: tratar agregar ou derivar como se fosse limpar."
  },
  {
   "apos": 14,
   "itemEdital": "P1-7.1",
   "rotulo": "TRANSFORMAÇÃO DE DADOS",
   "texto": "Não confunda normalização com padronização: a normalização reescala os dados para um intervalo, como de 0 a 1; a padronização leva os dados a média 0 e desvio 1. Armadilha: tratá-las como sinônimos em item que exige a distinção."
  },
  {
   "apos": 14,
   "itemEdital": "P1-7.1",
   "rotulo": "TRANSFORMAÇÃO DE DADOS",
   "texto": "Não confunda ETL com ELT: no ETL (extrair, transformar, carregar), a transformação precede a carga; no ELT, a transformação ocorre depois da carga, no destino."
  },
  {
   "apos": 19,
   "itemEdital": "P1-8.1",
   "rotulo": "Princípios de visualização de dados",
   "texto": "Não confunda paleta sequencial com divergente e categórica: a sequencial representa magnitude ordenada; a divergente, desvios em torno de um ponto central; a categórica, categorias. Armadilha: usar paleta sequencial ou divergente para categorias sem ordem."
  },
  {
   "apos": 19,
   "itemEdital": "P1-8.1",
   "rotulo": "Princípios de visualização de dados",
   "texto": "Não confunda posição com área ou cor na leitura de um gráfico: segundo Cleveland e McGill, a precisão decresce de posição em escala comum a comprimento, ângulo, área e, por fim, volume ou cor; por isso barras são lidas com mais exatidão que pizzas. Armadilha: afirmar que área ou cor comparam melhor que posição."
  },
  {
   "apos": 32,
   "itemEdital": "P1-8.2",
   "rotulo": "Histograma",
   "texto": "Não confunda histograma com gráfico de barras: o histograma mostra a distribuição de uma variável quantitativa em classes adjacentes de escala numérica, com barras contíguas; o de barras compara valores entre categorias discretas. Armadilha: o espaçamento entre as barras é só convenção de desenho."
  },
  {
   "apos": 32,
   "itemEdital": "P1-8.2",
   "rotulo": "Gráfico de linha",
   "texto": "Não confunda gráfico de linha com gráfico de dispersão: a linha liga pontos sucessivos e mostra a evolução de uma variável em eixo ordenado, em geral o tempo; a dispersão tem observações com coordenadas em duas variáveis quantitativas e revela relação e agrupamentos. Armadilha: correlação visível não prova causalidade."
  },
  {
   "apos": 32,
   "itemEdital": "P1-8.2",
   "rotulo": "Box plot (diagrama de caixa)",
   "texto": "Não confunda box plot com histograma: o box plot resume a distribuição pelos quartis, com a mediana na linha interna, bigodes e outliers, e permite comparar grupos; o histograma mostra a frequência por classe e, assim, a forma da distribuição, como a bimodalidade, que o box plot não mostra."
  },
  {
   "apos": 42,
   "itemEdital": "P1-8.3",
   "rotulo": "Data Studio (Google)",
   "texto": "Não confunda Data Studio com Looker Studio e Looker: Data Studio é o nome vigente desde abril de 2026; o mesmo produto se chamou Looker Studio entre 11/10/2022 e abril de 2026; o Looker é uma plataforma de BI corporativa, produto distinto (Google Cloud, verificado em 08/10/2026)."
  },
  {
   "apos": 42,
   "itemEdital": "P1-8.3",
   "rotulo": "Power BI (Microsoft)",
   "texto": "Não confunda Power BI Desktop com serviço do Power BI: o Desktop é a ferramenta de desenvolvimento, de download gratuito, em que se conecta aos dados e se cria o relatório; o serviço, plataforma on-line, organiza, gerencia e distribui os relatórios e também cria dashboards (Microsoft Learn, verificado em 08/10/2026)."
  },
  {
   "apos": 47,
   "itemEdital": "P1-8.4",
   "rotulo": "Storytelling para visualização de dados",
   "texto": "Não confunda storytelling com dashboard: o storytelling com dados combina dados, elementos visuais e narrativa em torno de uma mensagem central, para conduzir o público a uma conclusão ou ação; o dashboard é exploração aberta, com muitos indicadores."
  },
  {
   "apos": 47,
   "itemEdital": "P1-8.4",
   "rotulo": "Storytelling para visualização de dados",
   "texto": "Não confunda análise exploratória com explanatória: na exploratória, o analista investiga os dados para descobrir algo; na explanatória, o público é conduzido a uma mensagem já definida."
  }
 ],
 "L6A": [
  {
   "apos": 20,
   "itemEdital": "P1-1",
   "rotulo": "EXCEL",
   "texto": "Não confunda referência relativa com absoluta e mista: a relativa, que é o padrão, muda de posição quando a fórmula é copiada; a absoluta ($B$2) fixa coluna e linha; a mista fixa só a coluna ($B2) ou só a linha (B$2). Armadilha: o $ trava o que vem imediatamente depois dele."
  },
  {
   "apos": 20,
   "itemEdital": "P1-1",
   "rotulo": "WORD",
   "texto": "Não confunda ocultar alterações com resolvê-las no Word: o modo Sem Marcação só oculta as alterações, temporariamente, e elas voltam ao reabrir o documento; aceitar ou rejeitar decide o conteúdo e é o que as remove de fato. Armadilha: trocar para Sem Marcação não limpa o arquivo."
  },
  {
   "apos": 20,
   "itemEdital": "P1-1",
   "rotulo": "WORD",
   "texto": "Não confunda aceitar com rejeitar uma alteração controlada: aceitar incorpora a alteração ao texto; rejeitar a descarta, restabelecendo o texto original. Armadilha: Avançar e Anterior apenas navegam, sem aceitar nem rejeitar."
  },
  {
   "apos": 20,
   "itemEdital": "P1-1",
   "rotulo": "WORD",
   "texto": "Não confunda sumário automático com sumário digitado à mão: o automático é gerado a partir dos títulos com estilo de título e é atualizado com Atualizar Campo; o digitado à mão não cria estrutura que o Word reconheça. Armadilha: dizer que o sumário automático independe da formatação dos títulos."
  },
  {
   "apos": 20,
   "itemEdital": "P1-1",
   "rotulo": "EXCEL",
   "texto": "Não confunda correspondência exata com aproximada no PROCV: com FALSO no quarto argumento, a correspondência é exata; com VERDADEIRO ou com o argumento em branco, é aproximada, isto é, o valor mais próximo que não ultrapasse o procurado. Armadilha: omitir o quarto argumento não equivale a FALSO."
  },
  {
   "apos": 20,
   "itemEdital": "P1-1",
   "rotulo": "EXCEL",
   "texto": "Não confunda PROCV com ÍNDICE e CORRESP quanto à direção da pesquisa: o PROCV só pesquisa da esquerda para a direita, e a coluna do valor procurado precisa estar à esquerda da coluna de retorno; se não estiver, recomendam-se ÍNDICE e CORRESP."
  },
  {
   "apos": 20,
   "itemEdital": "P1-1",
   "rotulo": "ONEDRIVE",
   "texto": "Não confunda compartilhar com exibição e com edição no OneDrive: com exibição, quem recebe o link apenas lê; com edição, lê e altera o arquivo. Armadilha: achar que compartilhar transfere a propriedade do arquivo."
  },
  {
   "apos": 34,
   "itemEdital": "P1-3",
   "rotulo": "CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL)",
   "texto": "Não confunda SMTP com POP3: o SMTP transfere e envia as mensagens; o POP3 permite à estação acessar a caixa postal no servidor, em geral baixando as mensagens. Armadilha: o POP3 não envia; o programa de e-mail depende do SMTP para enviar."
  },
  {
   "apos": 34,
   "itemEdital": "P1-3",
   "rotulo": "CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL)",
   "texto": "Não confunda POP3 com IMAP4: por padrão, os clientes POP3 removem as mensagens baixadas do servidor, baixam para uma única pasta e não sincronizam várias pastas; os clientes IMAP4 não as removem por padrão e dão suporte a várias pastas (Microsoft Learn, \"POP3 e IMAP4 em Exchange Online\")."
  },
  {
   "apos": 34,
   "itemEdital": "P1-3",
   "rotulo": "CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL)",
   "texto": "Não confunda Para e Cc com Cco: em Para (destinatários principais) e em Cc (ciência), os endereços aparecem para todos; quem está em Cco recebe a cópia, mas seu endereço fica oculto para os demais. Armadilha: dizer que o destinatário em Cco não recebe a mensagem."
  },
  {
   "apos": 34,
   "itemEdital": "P1-3",
   "rotulo": "CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL)",
   "texto": "Não confunda equipe com canal no Teams: a equipe é a coleção de pessoas, conteúdo e ferramentas dos projetos e resultados de uma organização; o canal é uma seção dedicada dentro da equipe, que organiza as conversas por tópicos ou projetos."
  },
  {
   "apos": 34,
   "itemEdital": "P1-3",
   "rotulo": "CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL)",
   "texto": "Não confunda apresentar uma guia com apresentar uma janela ou a tela inteira no Meet: a guia é uma aba do Chrome, com áudio compartilhado por padrão; na janela ou na tela inteira, o áudio do sistema só é compartilhado se a opção for ativada (Ajuda do Google Meet, leitura de 08/10/2026)."
  }
 ],
 "L6B": [
  {
   "apos": 4,
   "itemEdital": "P1-2",
   "rotulo": "Redes de computadores",
   "texto": "Não confunda TCP com UDP: o TCP entrega os dados de forma confiável, ordenada e com controle de erros; o UDP entrega sem essas garantias, com menor atraso, e por isso é usado em voz e vídeo ao vivo."
  },
  {
   "apos": 12,
   "itemEdital": "P1-2.1",
   "rotulo": "Conceitos básicos, ferramentas, aplicativos e procedimentos de Internet e intranet",
   "texto": "Não confunda Internet com Web: a Internet é a rede mundial de computadores formada pela interligação de redes, a infraestrutura que usa TCP/IP; a Web é um serviço sobre a Internet, de páginas interligadas por hiperlinks, acessadas por HTTP/HTTPS e identificadas por URLs. Armadilha: tratá-las como sinônimos."
  },
  {
   "apos": 12,
   "itemEdital": "P1-2.1",
   "rotulo": "Conceitos básicos, ferramentas, aplicativos e procedimentos de Internet e intranet",
   "texto": "Não confunda Internet com intranet e extranet: a Internet é aberta e mundial; a intranet é rede privada de uma organização, de acesso restrito ao público autorizado, com as mesmas tecnologias da Internet; a extranet é a extensão controlada da intranet a um público externo autorizado, como parceiros e fornecedores."
  },
  {
   "apos": 12,
   "itemEdital": "P1-2.1",
   "rotulo": "Conceitos básicos, ferramentas, aplicativos e procedimentos de Internet e intranet",
   "texto": "Não confunda navegador com mecanismo de busca: o navegador é o programa cliente que solicita páginas aos servidores web e as exibe; o mecanismo de busca é um serviço que indexa páginas e as localiza por palavras-chave, acessado por meio do navegador."
  },
  {
   "apos": 23,
   "itemEdital": "P1-4.1",
   "rotulo": "Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais",
   "texto": "Não confunda confidencialidade com integridade e disponibilidade: confidencialidade é só quem está autorizado ter acesso; integridade é a informação não ser alterada, apagada ou corrompida de modo não autorizado ou acidental; disponibilidade é ela estar acessível a quem está autorizado sempre que necessário."
  },
  {
   "apos": 23,
   "itemEdital": "P1-4.1",
   "rotulo": "Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais",
   "texto": "Não confunda backup completo com incremental e diferencial: o completo copia todos os dados selecionados, tenham mudado ou não, e a restauração usa o último completo; o incremental e o diferencial copiam apenas o que mudou, e a restauração exige o completo mais cópias adicionais."
  },
  {
   "apos": 23,
   "itemEdital": "P1-4.1",
   "rotulo": "Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais",
   "texto": "Não confunda backup incremental com diferencial: o incremental copia o que mudou desde o último completo ou incremental, marca os arquivos e, na restauração, exige o completo e todos os incrementais; o diferencial não marca os arquivos, acumula o que mudou desde o completo e exige o completo e o último diferencial."
  },
  {
   "apos": 23,
   "itemEdital": "P1-4.1",
   "rotulo": "Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais",
   "texto": "Não confunda backup com sincronização: o backup guarda um ponto no tempo; a sincronização espelha o estado atual, de modo que uma exclusão ou uma criptografia por ransomware pode ser replicada. Armadilha: a sincronização só funciona como backup se houver histórico e retenção."
  },
  {
   "apos": 23,
   "itemEdital": "P1-4.1",
   "rotulo": "Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais",
   "texto": "Não confunda vírus com worm: o vírus insere cópias de si em programas e arquivos hospedeiros e só age quando o hospedeiro é executado; o worm é programa independente que se replica e se propaga automaticamente pelas redes, explorando vulnerabilidades, sem hospedeiro nem ação do usuário."
  },
  {
   "apos": 23,
   "itemEdital": "P1-4.1",
   "rotulo": "Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais",
   "texto": "Não confunda vírus com trojan: o vírus propaga-se inserindo cópias de si em programas e arquivos; o trojan (cavalo de Troia) parece um programa legítimo, mas executa também funções maliciosas, não se replica e depende de o usuário instalá-lo e executá-lo."
  },
  {
   "apos": 23,
   "itemEdital": "P1-4.1",
   "rotulo": "Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais",
   "texto": "Não confunda spyware com ransomware: o spyware monitora as atividades do usuário e envia as informações a terceiros (confidencialidade); o ransomware torna os dados inacessíveis, em geral por criptografia, e exige resgate (disponibilidade). Armadilha: pagar o resgate não garante a devolução dos dados."
  },
  {
   "apos": 30,
   "itemEdital": "P1-4.2",
   "rotulo": "Programas de proteção (antivírus, firewall, antispyware)",
   "texto": "Não confunda firewall com antispyware: o firewall controla o tráfego de rede, permitindo ou bloqueando conexões segundo regras; o antispyware detecta e remove spyware, que monitora o usuário e envia informações a terceiros. Armadilha: pacotes de segurança que reúnem as funções não eliminam a distinção."
  },
  {
   "apos": 38,
   "itemEdital": "P1-4.3",
   "rotulo": "Ameaças digitais (phishing, pharming)",
   "texto": "Não confunda HTTPS com legitimidade do site: o HTTPS, com certificado digital, autentica o servidor para o domínio acessado e protege a comunicação; ele não garante que o domínio seja o da instituição pretendida nem que o titular aja de boa-fé. Armadilha: dizer que o HTTPS não autentica nada também é erro."
  }
 ]
}
```
