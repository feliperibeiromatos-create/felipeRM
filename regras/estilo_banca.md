# estilo_banca.md — T-03 — 2026-10-09 — gerado por gbq-estilo
v1.1

## 1. Cabeçalho

- Versão: v1.1. Substitui a v1.0 de 2026-10-08, que se baseava em 42 itens de BQ-0001 a 0046.
- Data: 2026-10-09
- Banco: 66 itens (BQ-0001 a BQ-0066), todos CEBRASPE_ANALOGA, de 9 certames Cebraspe:
  - TRF6 2024: Cargo 2, Análise de Dados; aplicação 19/01/2025.
  - BCB 2024: Analista, TI; aplicação 4/8/2024.
  - ANATEL 2024: Cargo 2, Ciências de Dados; aplicação 15/09/2024.
  - SUSEP 2025: Cargo 4, TI e Ciência de Dados; aplicação 08/06/2025.
  - CNJ 2024: Cargo 2, Análise de Sistemas; aplicação 30/6/2024.
  - ANTT 2023: Cargo 1; aplicação 14/4/2024.
  - Embrapa 2024: Analista, 3 cadernos (026 Ciência de Dados, 034 Engenharia de Dados, 071 Análise de Dados); aplicação 23/3/2025.
  - ANM 2024: Cargo 24, TI e Ciência de Dados; aplicação 16/02/2025.
  - PF 2025: Cargo 4, Perito Criminal Federal, Área 3; aplicação 27/07/2025.
- Anulados: 6, todos com gabarito X (BQ-0029, 0030, 0031, 0060, 0062, 0063). Não entram na proporção C/E, na tipologia nem nos marcadores, porque sem gabarito não há mecanismo C/E para observar. Os três anulados da ANM têm justificativa oficial, usada só nas recomendações (seção 5.3).
- Base efetiva: 60 itens com gabarito C ou E, sendo C = 33 e E = 27. Confere com a contagem da gbq-gerencia em saida/banco/R03_reconciliacao_2026-10-09.md.
- Status de QA da base:
  - BQ-0001 a 0046: saida/banco/qualidade_2026-10-09.md (45 APROVADAS e 1 CORRIGIR).
    - BQ-0025 entra a partir desta versão. O único apontamento contra ela (a falta, em observacoes, da alteração C→E entre preliminar e definitivo) foi sanado por D-RECUPERACAO (c). A linha agora registra "gabarito preliminar C alterado para E no definitivo". O gabarito E já tinha sido conferido como correto. A GBQ deve confirmar essa inclusão (seção 6).
  - BQ-0047 a 0066: saida/banco/qualidade_2026-10-09_R03.md (20 APROVADOS), reconciliados em R03_reconciliacao_2026-10-09.md. Nenhuma linha tem mais "QA PENDENTE".
- Fontes lidas, todas em modo somente leitura:
  - banco/banco.csv, com leitor CSV que respeita as aspas (separador ";").
  - Os dois relatórios de qualidade e a reconciliação R-03.
  - regras/estilo_banca_semente.md, só como referência.
  - A v1.0 deste guia.
  - edital/TI_itens_5_8_P1.md, só para os nomes dos subitens.
- Fora do escopo desta coordenação, e não alterado:
  - A arbitragem de aderência (DIRETA/PARCIAL) das divergências do QA de 09/10, que a gbq-gerencia faz em paralelo (T-03).
  - O banco, que não foi alterado.
- Limitações de dados:
  - O CSV não tem coluna de comando. A proporção por tipo de comando não foi calculada; usa-se a proporção por subitem do edital (item_edital_camara).

## 2. Proporção C/E observada

Total sobre a base de 60 itens: C = 33 (55,0%); E = 27 (45,0%). Na v1.0 era C 57,1% / E 42,9%, sobre 42 itens.

Por certame:

| Certame | itens no banco | anulados (X) | base C+E | C | E | %C / %E |
|---|---|---|---|---|---|---|
| TRF6 2024 | 12 | 0 | 12 | 7 | 5 | 58,3 / 41,7 |
| BCB 2024 | 5 | 0 | 5 | 3 | 2 | 60,0 / 40,0 |
| ANATEL 2024 | 8 | 0 | 8 | 3 | 5 | 37,5 / 62,5 |
| SUSEP 2025 | 7 | 3 | 4 | 3 | 1 | 75,0 / 25,0 |
| CNJ 2024 | 8 | 0 | 8 | 6 | 2 | 75,0 / 25,0 |
| ANTT 2023 | 6 | 0 | 6 | 2 | 4 | 33,3 / 66,7 |
| Embrapa 2024 (026: 1C/1E; 034: 1C/2E; 071: 2C/2E) | 9 | 0 | 9 | 4 | 5 | 44,4 / 55,6 |
| ANM 2024 | 9 | 3 | 6 | 3 | 3 | 50,0 / 50,0 |
| PF 2025 | 2 | 0 | 2 | 2 | 0 | 100 / 0 |
| Total | 66 | 6 | 60 | 33 | 27 | 55,0 / 45,0 |

Por subitem do edital. O mapeamento é o do banco. As notas de aderência são as já registradas, e esta coordenação não decide aderência.

| Subitem | C | E | X | v1.0 (C/E/X) | Observação |
|---|---|---|---|---|---|
| P1-5.1 | 1 | 0 | 0 | 0/0/0 | BQ-0059; DIRETA (D1 R-03). É o único item do subitem. |
| P1-5.2 | 6 | 7 | 0 | 5/5/0 | +BQ-0049 (DIRETA, D1 R-03), 0050, 0051 |
| P1-5.3 | 7 | 4 | 3 | 3/3/0 | +BQ-0058, 0061, 0064 (VOLÁTIL), 0065, 0066; X: 0060, 0062, 0063 |
| P1-6 | 0 | 2 | 0 | 0/2/0 | sem mudança |
| P1-7.1 | 2 | 1 | 2 | 0/1/2 | +BQ-0054, 0055 (PARCIAL, D1 R-03) |
| P1-8.1 | 2 | 1 | 0 | 2/1/0 | sem mudança |
| P1-8.2 | 1 | 2 | 0 | ausente | BQ-0047, 0052, 0053; DIRETA (QA R-03 e D1 R-03) |
| P1-8.3 | 2 | 1 | 0 | 2/0/0 | +BQ-0048 (Tableau e Power BI, nomeados no edital) |
| P2-4.1 | 10 | 7 | 1 | 10/4/1 | +BQ-0025, 0056, 0057, todas PARCIAIS (LGPD geral) |
| P2-4.3 | 2 | 2 | 0 | 2/2/0 | sem mudança |
| P1 (soma) | 21 | 18 | 5 | 12/12/2 | |
| P2 (soma) | 12 | 9 | 1 | 12/6/1 | |

Leitura:
- A proporção continua perto de metade/metade, com leve viés para C (55%).
- O viés da v1.0, concentrado na LGPD (P2-4.1 com 10 C e 4 E), diminuiu: agora são 10 C e 7 E, ou 58,8% de C. P1 tem 53,8% de C e P2, 57,1%.
- A variação entre certames continua grande (de 33% a 100% de C), e cada certame tem só de 2 a 12 itens. Não force proporção por lote. A faixa de 45% a 60% de C por lote se mantém, e a base (55%) fica no meio dela.

## 3. Tipologia de padrões

Regras de classificação:
- Cada um dos 60 itens tem um mecanismo primário e entra em exatamente um padrão. As somas fecham em 27 E e 33 C.
- Um padrão exige pelo menos 3 itens reais, citados por BQ-id. Com menos que isso, é INDÍCIO.
- "% base" é calculado sobre 60 itens. "% do grupo" é calculado sobre 27 E ou sobre 33 C.
- Os trechos entre aspas são literais do texto_integral do banco, inclusive as grafias originais.

Regra de desempate entre E4, E5 e E6, para itens com moldura verdadeira e um segmento falso:
- Se o segmento falso nega ou estende o que um método ou uma ferramenta faz, o item é E4.
- Se o segmento falso é um quantificador absoluto ou uma prescrição universal, o item é E6.
- Nos demais casos (exceção, consequência ou premissa causal), o item é E5.

Os traços transversais podem coexistir com o padrão primário e estão em 3.13.

### 3.1 [E1] Troca de conceito vizinho

- Definição: o enunciado atribui ao termo X a definição, a família ou a propriedade de um conceito vizinho Y da mesma área. O restante da frase é verdadeiro.
- Mecanismo: E. O erro está no núcleo, mas a frase soa técnica e coerente. Quem não domina o par X/Y aceita.
- Itens:
  - BQ-0010 (E): "baseadas prioritariamente na utilização de aprendizado supervisionado"
  - BQ-0015 (E): "Uma thread representa uma entidade que pode ser configurada para responder às mensagens de um usuário a partir de vários parâmetros, como modelo, instruções e ferramentas." Atribui a "thread" a definição de outro objeto da API.
  - BQ-0018 (E): "Naive Bayes é um algoritmo de classificação baseado na aprendizagem por reforço"
  - BQ-0039 (E): "Autenticidade é um princípio que visa garantir que o autor não negue ter criado e assinado determinada informação". Atribui à autenticidade a definição de não repúdio.
  - BQ-0043 (E): "A classe de algoritmos denominada classificação é utilizada no grupo de aprendizado não supervisionado"
  - BQ-0044 (E): "A limpeza de dados consiste no processo de reorganização dos dados"
- Frequência: n = 6; 10,0% da base; 22,2% dos E. Continua sendo o padrão E mais frequente.
- Subitens: P1-5.2 (BQ-0018, 0043), P1-5.3 (BQ-0010, 0015), P1-7.1 (BQ-0044), P2-4.3 (BQ-0039).
- Fronteira: BQ-0050 também envolve o par supervisionado/não supervisionado, mas cobra a adequação do paradigma ao cenário do texto-base. Por isso foi classificada em E4.

### 3.2 [E2] Inversão de definição, de polaridade ou de relação

- Definição: o conceito recebe o seu oposto. Pode ser um princípio descrito pela sua violação, um processo descrito no sentido contrário, um par simétrico/assimétrico trocado, ou os dois polos de uma relação ("A em nome de B") trocados entre si.
- Mecanismo: E. A frase mantém o vocabulário do conceito e diz o contrário.
- Itens:
  - BQ-0011 (E): "garante que um dado ou uma informação tenham sido alterados sem o registro da ação correspondente"
  - BQ-0016 (E): "a opacidade sobre os algoritmos é encorajada como prática padrão"
  - BQ-0022 (E): "o equilíbrio assimétrico consiste na distribuição do peso uniforme dos objetos em ambas as metades da página"
  - BQ-0028 (E): "o processo de geração de imagens ocorre por meio da aplicação sequencial de ruído gaussiano em uma imagem inicial em branco". Descreve a geração no sentido do treinamento.
  - BQ-0056 (E, novo): "realiza o tratamento de dados pessoais em nome do operador é denominada de controlador". Os papéis de controlador e operador estão trocados. O texto vigente da definição na LGPD fica com o qa-normativo (T-13).
- Frequência: n = 5; 8,3% da base; 18,5% dos E.
- Subitens: P2-4.3 (BQ-0011), P1-6 (BQ-0016), P1-8.1 (BQ-0022), P1-5.3 (BQ-0028), P2-4.1 (BQ-0056).
- Mudança: a definição foi ampliada para incluir a inversão de relação, por causa de BQ-0056. A correção da v1.0 sobre BQ-0011 continua valendo: o item define integridade pelo seu oposto, e não "como disponibilidade", como diz a semente.

### 3.3 [E3] Alteração do comando normativo

- Definição: em item sobre norma, a frase faz uma destas alterações:
  - cria um dever inexistente;
  - dispensa um dever existente;
  - inventa prazo ou condição;
  - nega a consequência prevista;
  - troca a condição da norma pela remissão a outra norma.
- Mecanismo: E. A frase mantém o tom da lei ("deve", "não será necessário", "não enseja", "desde que") e muda o efeito jurídico.
- Itens:
  - BQ-0003 (E): "deve ser comunicada previamente pois a ela compete zelar pela proteção dos dados pessoais". Cria um dever e o reforça com uma justificativa verdadeira.
  - BQ-0004 (E): "não será necessário novo consentimento do titular"
  - BQ-0023 (E): "devem ser retidos por um período de cinco anos, mesmo após a conclusão do seu processamento"
  - BQ-0040 (E): "não enseja a imediata descontinuidade de sua utilização, devendo-se adotar medidas corretivas"
  - BQ-0057 (E, novo): "pode ser realizado, desde que siga o recomendado no Estatuto da Criança e do Adolescente". Substitui a condição da LGPD por uma remissão a outra lei.
- Frequência: n = 5; 8,3% da base; 18,5% dos E.
- Subitens: P2-4.1 (BQ-0003, 0004, 0023, 0057), P1-6 (BQ-0040).
- Vigência não verificada. Todos os itens de LGPD vão para o qa-normativo (T-13, 17 itens), e BQ-0040 (Resolução CNJ) também está pendente. O mecanismo vale como estilo, não como conteúdo vigente.

### 3.4 [E4] Erro de adequação ou de escopo: método, paradigma ou ferramenta × tarefa

- Definição: o item faz uma destas três coisas:
  - nega uma tarefa ou capacidade que o método ou a ferramenta admite;
  - estende a um método uma tarefa que ele não admite;
  - indica, para o problema descrito, um método ou paradigma de outra natureza.
- Mecanismo: E. Ocorre de três formas:
  - Enumeração ("tanto... quanto"): um elemento verdadeiro empresta credibilidade ao falso.
  - Negação: vem com causa falsa ("uma vez que") ou ao lado de uma afirmação verdadeira sobre o mesmo objeto.
  - Cenário: o juízo de adequação ("é indicado", "é a escolha ideal") vem com justificativa ("pois").
- Itens:
  - BQ-0019 (E): "não pode ser utilizado em problemas de classificação, uma vez que seu objetivo é prever valores numéricos"
  - BQ-0042 (E): "os algoritmos de Naive Bayes e o de máquinas de vetores de suporte são utilizados tanto na classificação quanto na regressão"
  - BQ-0048 (E, novo): "e não possuem funcionalidades para análise de dados ou integração com bancos de dados"
  - BQ-0049 (E, novo): "O algoritmo de regressão linear é indicado para resolver o problema em questão". O texto-base pede uma decisão de aprovar ou negar a partir de exemplos históricos.
  - BQ-0050 (E, novo): "O aprendizado de máquina não supervisionado é a escolha ideal atender às condições apresentadas, pois o sistema aprende a aprovar ou a negar sem dados rotulados."
- Contraste C, com o mesmo terreno e sem o erro:
  - BQ-0020: "pode ser usado para desafios de classificação ou regressão"
  - BQ-0051: "A situação descrita representa um problema de classificação." Mesmo texto-base de BQ-0049 e 0050.
- Frequência: n = 5; 8,3% da base; 18,5% dos E.
- Subitens: P1-5.2 (BQ-0019, 0042, 0049, 0050), P1-8.3 (BQ-0048).
- Mudança: E4 era indício na v1.0 (n = 2) e passa a padrão. A definição foi ampliada de "algoritmo × tarefa" para "método, paradigma ou ferramenta × tarefa".

### 3.5 [E5] Segmento acessório falso em moldura verdadeira

- Definição: a oração principal, ou moldura, é verdadeira. Um segmento acessório é falso: uma exceção ("excetuando-se..."), uma consequência ("não havendo...") ou uma premissa causal ("..., por isso..."). O segmento pode estar no fim da frase (cauda) ou no meio dela.
- Mecanismo: E. Quem lê confirma a moldura e relaxa, e o erro passa no segmento acessório.
- Itens:
  - BQ-0002 (E): "excetuando-se, por questões de segurança, a identificação do controlador"
  - BQ-0041 (E): "não havendo, nesse caso, preservação da integridade do conjunto de dados"
  - BQ-0058 (E, novo): "e o aprendizado profundo não conseguiu melhorar o desempenho dos modelos generativos, por isso se tem optado por investir em". A premissa é falsa e a conclusão sobre LLMs autorregressivos, plausível. É a primeira ocorrência na base da forma pura do tipo 3 da semente (verdadeira com causa falsa).
- Frequência: n = 3; 5,0% da base; 11,1% dos E.
- Subitens: P2-4.1 (BQ-0002), P1-5.2 (BQ-0041), P1-5.3 (BQ-0058).
- Mudança: E5 era indício na v1.0 (n = 2, só "cauda falsa") e passa a padrão. A definição foi ampliada de "parte final" para "segmento acessório" com a entrada de BQ-0058. Essa ampliação é julgamento desta coordenação. Se a GBQ preferir o recorte da v1.0, E5 volta a INDÍCIO (n = 2), e BQ-0058 fica como indício isolado de "causa falsa".

### 3.6 [E6] Regra relativa convertida em absoluta (generalização indevida) — NOVO

- Definição: o item toma algo que vale em alguns casos ou como opção (uma base legal entre outras, um gráfico adequado a certos fins, uma convenção de sinalização) e o enuncia como única possibilidade, como regra sem exceção ou como obrigação universal. Os veículos são "só", "sempre" e "deve... antes de qualquer".
- Mecanismo: E. Sem o quantificador ou a prescrição, a frase seria aceitável. O erro está na generalização.
- Itens:
  - BQ-0025 (E): "só podem ser tratados com o consentimento específico e destacado do titular ou de seu representante legal"
  - BQ-0052 (E): "será sempre a melhor escolha"
  - BQ-0053 (E): "deve ser tratado como um outlier e removido da base de dados antes de qualquer análise adicional"
- Contraste C (sem generalização, no mesmo tema de BQ-0025):
  - BQ-0032: "pode ser realizado sem o consentimento do titular"
  - BQ-0045: "poderá ocorrer sem fornecimento de consentimento do titular"
- Contraexemplos (termo absoluto em item C, onde a restrição faz parte da própria definição):
  - BQ-0006: "apenas os dados pertinentes"
  - BQ-0054: "sem qualquer interpretação"
- Frequência: n = 3; 5,0% da base; 11,1% dos E.
- Subitens: P2-4.1 (BQ-0025), P1-8.2 (BQ-0052, 0053).
- Fronteiras:
  - BQ-0004 ("de forma absoluta") tem um termo absoluto que concorre com a dispensa de dever. Fica em E3, como na v1.0.
  - BQ-0053 também tem estrutura de cauda (E5). Pela regra de desempate, a prescrição universal prevalece.
- Origem: recupera o tipo 4 da semente (generalização indevida), que a v1.0 havia rebaixado a INDÍCIO porque só 1 item tinha termo absoluto como fonte de erro.

### 3.7 [C1] Definição ou descrição canônica correta

- Definição: o item descreve um conceito, uma técnica, uma ferramenta ou a classificação de um cenário como a literatura ou a documentação o fazem, sem marcador de armadilha e sem simplificação que pareça lacuna.
- Mecanismo: C por correção direta. Esses itens são a âncora do caderno.

| ID | trecho decisivo (literal) | subitem |
|---|---|---|
| BQ-0008 | "a obrigação legal decorre de uma norma de conduta, isto é, uma regra que disciplina um comportamento" | P2-4.1 |
| BQ-0009 | "são utilizadas técnicas de aprendizado de máquina para a previsão de resultados futuros com base em dados históricos" | P1-5.3 |
| BQ-0013 | "O agrupamento é um método de aprendizado não supervisionado que busca a similaridade entre os dados" | P1-5.2 |
| BQ-0014 | "O parâmetro temperature em LLM regula a amplitude da diversidade e criatividade nas previsões" | P1-5.3 |
| BQ-0017 | "O Grafana é capaz de fazer queries em diferentes tipos de data source" | P1-8.3 |
| BQ-0020 | "pode ser usado para desafios de classificação ou regressão" | P1-5.2 |
| BQ-0026 | "ajusta uma função de mapeamento a partir de exemplos rotulados para generalizar dados ainda não vistos" | P1-5.2 |
| BQ-0033 | "uma tecnologia capaz de criar texto similar ao texto escrito por seres humanos" | P1-5.3 |
| BQ-0035 | "Kibana é uma ferramenta que permite visualizar os dados armazenados no Elasticsearch" | P1-8.3 |
| BQ-0038 | "seja capaz de verificar que os dados não foram modificados indevidamente" | P2-4.3 |
| BQ-0047 (novo) | "pois destacam a mediana, a dispersão dos dados e os possíveis valores atípicos" | P1-8.2 |
| BQ-0051 (novo) | "A situação descrita representa um problema de classificação." | P1-5.2 |
| BQ-0054 (novo) | "uma métrica é uma medida analisada em um contexto específico e pode envolver cálculos e comparações" | P1-7.1 |
| BQ-0055 (novo) | "incluindo-se faixas de desempenho codificadas, que podem ser representadas visualmente, prazos para o atingimento das metas e benchmarks" | P1-7.1 |
| BQ-0061 (novo) | "aprendizado é realizado a partir da distribuição de probabilidade conjunta p(x,y)" | P1-5.3 |
| BQ-0064 (novo; VOLÁTIL) | "o princípio tecnológico dessas plataformas é a arquitetura transformer" | P1-5.3 |
| BQ-0066 (novo) | "são modelos de aprendizado profundo pré-treinados em grandes quantidades de dados" | P1-5.3 |

- Frequência: n = 17; 28,3% da base; 51,5% dos C.
- Mudanças:
  - BQ-0001 saiu de C1 e foi para C6.
  - Entraram 7 itens novos.
- Notas:
  - BQ-0047 é C com "pois". A justificativa causal verdadeira também ocorre em C, e não só em E (ver 4).
  - BQ-0055 é uma enumeração de atributos inteiramente verdadeira. Contrasta com a enumeração mista de BQ-0042 (E4).

### 3.8 [C2] Reprodução próxima do texto normativo

- Definição: a frase reproduz, de forma literal ou quase literal, um princípio ou dispositivo de lei.
- Mecanismo: C. Quem conhece o texto da lei reconhece. Quem desconfia de frases longas e "bonitas" erra.
- Itens:
  - BQ-0006 (C): "deve abranger apenas os dados pertinentes, proporcionais e não excessivos em relação às suas finalidades"
  - BQ-0024 (C): "deve demonstrar a adoção de medidas eficazes e capazes de comprovar a observância e o cumprimento das normas"
  - BQ-0036 (C): "a proteção da privacidade e a proteção dos dados pessoais, na forma da lei". Marco Civil da Internet.
  - BQ-0037 (C): "os dados deverão ser mantidos em formato interoperável e estruturado para uso compartilhado"
- Frequência: n = 4; 6,7% da base; 12,1% dos C. Nenhum item novo.
- Subitem: P2-4.1.
- A proximidade com o texto vigente não foi conferida por artigo e fica com o qa-normativo (T-13).

### 3.9 [C3] Item C redigido para parecer E

- Definição: o item é verdadeiro, mas carrega traço de superfície típico de item E: exceção ou dispensa, negação, "sem consentimento", concessiva ("mesmo que") ou "independe".
- Mecanismo: C. Pune quem marca E por reflexo diante de exceção ou negação.
- Itens:
  - BQ-0005 (C): "ficando dispensada tal exigência para os dados tornados manifestamente públicos pelo titular"
  - BQ-0007 (C): "o consentimento do titular não constitui a base legal mais apropriada"
  - BQ-0012 (C): "mesmo que o sistema ou a infraestrutura esteja sob pressão"
  - BQ-0027 (C): "independe de rótulos para extrair componentes de maior variância"
  - BQ-0032 (C): "pode ser realizado sem o consentimento do titular"
  - BQ-0045 (C): "poderá ocorrer sem fornecimento de consentimento do titular"
- Frequência: n = 6; 10,0% da base; 18,2% dos C. Nenhum item novo.
- Subitens: P2-4.1 (BQ-0005, 0007, 0032, 0045), P2-4.3 (BQ-0012), P1-5.2 (BQ-0027).
- Nota: BQ-0054 ("sem qualquer interpretação") tem traço de superfície de E, mas seu mecanismo primário é a definição do par medida × métrica. Foi classificada em C1.

### 3.10 [C4] Item C com aparente estranheza semântica (INDÍCIO)

- Definição: o item é verdadeiro, mas combina ideias que parecem colidir.
- Itens:
  - BQ-0021 (C): "pela sobreposição de elementos visuais alinhados"
  - BQ-0034 (C): "para recomendar conteúdos aos usuários de forma individualizada"
- Frequência: n = 2; 3,3% da base; 6,1% dos C. Continua INDÍCIO, sem item novo.
- Subitens: P1-8.1 (BQ-0021), P1-5.2 (BQ-0034).

### 3.11 [C5] Paráfrase não literal de norma aceita como C (INDÍCIO; não usar como modelo)

- Item: BQ-0046 (C): "permitida a países ou organismos internacionais que tenham legislação equivalente à LGPD". O QA anota que a expressão difere da redação do art. 33, I.
- Frequência: n = 1; 1,7% da base; 3,0% dos C. Continua INDÍCIO.
- Subitem: P2-4.1.
- Está pendente de qa-normativo (T-13). Não reproduza no AUTORAL: o gabarito depende de tolerância da banca, que não se pode prever.

### 3.12 [C6] Afirmação parcial verdadeira, sem marcador de exclusividade ("incompleto não é errado") — NOVO

- Definição: o item descreve o objeto por uma parte ou por uma simplificação (um suporte, um uso típico, um componente) e não diz que essa parte é a única. Uma leitura rigorosa vê lacuna, mas não há falsidade.
- Mecanismo: C. Quem trata incompletude como erro marca E. É o espelho de E6: quando a banca quer o E, acrescenta "só", "sempre" ou "qualquer"; sem esse marcador, a parte verdadeira fica C.
- Itens:
  - BQ-0001 (C, reclassificada de C1): "o uso de gráficos permite a exibição de plotagens e diagramas, organizados ao longo de dois eixos". Nem todo gráfico tem dois eixos, mas o item usa "permite" e não diz "todo".
  - BQ-0059 (C, novo): "Um prompt é um conjunto de instruções que o modelo generativo utiliza para prever a resposta desejada." Um prompt pode conter também contexto, exemplos ou perguntas.
  - BQ-0065 (C, novo): "Deepfakes são vídeos gerados por IA". Deepfakes não se limitam a vídeo, e o restante do item ("treina duas redes neurais para competirem entre si") é canônico.
- Frequência: n = 3; 5,0% da base; 9,1% dos C.
- Subitens: P1-8.1 (BQ-0001), P1-5.1 (BQ-0059), P1-5.3 (BQ-0065).
- Diferença para C5: em C6, a parte afirmada é verdadeira sem depender de tolerância. Em C5, a paráfrase troca o critério da norma.
- A leitura de que esses itens são "incompletos" é julgamento desta coordenação. Os três poderiam ser lidos como C1 por um revisor menos rigoroso. Se a GBQ os reclassificar, C6 deixa de existir (n = 0) e C1 volta a 20.

### 3.13 Traços transversais (pontos da semente reavaliados)

Contagem nos 60 itens da base. Um item pode ter mais de um traço.

| Traço | Itens | Em quantos é a fonte do erro | Veredito v1.1 (v1.0) |
|---|---|---|---|
| Termo absoluto ou universal ("sempre", "só", "apenas", "qualquer", "exclusivos", "de forma absoluta") | C: BQ-0006, 0054; E: BQ-0003, 0004, 0025, 0043, 0052, 0053 | 3 (BQ-0025, 0052, 0053), mais 1 concorrente com E3 (BQ-0004) | PADRÃO E6 (era INDÍCIO, com 1). Não decide: 2 C e 2 E têm o termo sem que ele seja o erro. |
| "prioritariamente" deslocando o núcleo | BQ-0010 (E) | 1 | INDÍCIO (sem mudança) |
| Verdadeira com causa falsa (forma pura do tipo 3 da semente) | BQ-0058 (E) | 1 | INDÍCIO, dentro de E5 (era 0) |
| Verdadeira com consequência falsa | BQ-0041 (E) | 1 | dentro de E5 (sem mudança) |
| Exceção ou ressalva indevida | BQ-0002 (E) | 1 | dentro de E5 (sem mudança) |
| Exceção ou dispensa verdadeira | BQ-0005 (C) | — | dentro de C3 |
| Nexo causal ou de finalidade como reforço | ver detalhe | — | traço, não padrão |
| Juízo de adequação forte ("é indicado", "escolha ideal", "melhor escolha") | E: BQ-0049, 0050, 0052 | 3, mas como veículo de E4 ou E6 | traço novo; em C só aparecem formas fracas ou negadas (BQ-0047 "úteis"; BQ-0007 "não constitui a base legal mais apropriada") |
| Condicional "desde que" | E: BQ-0023, 0057 | 1 (BQ-0057, a condição trocada) | INDÍCIO novo (2 E, 0 C) |
| Item situacional ("Considere que..."; texto-base comum a vários itens) | BQ-0004 (E); bloco BQ-0049 (E), 0050 (E), 0051 (C) | — | forma; 2 ocorrências (era 1) |

Detalhe:
- Termo absoluto. "nunca", "somente", "exclusivamente", "todo(s)" e "em qualquer hipótese" continuam com 0 ocorrências.
  - "por si só" (BQ-0061, C) não é restritivo e não foi contado.
  - Em BQ-0003, "exclusivos" vem da própria norma. Em BQ-0043, o erro é a troca de conceito (E1).
- Nexo causal ou de finalidade:
  - Conectores causais: E em BQ-0003 ("pois"; a causa é verdadeira e a principal, falsa), 0019 ("uma vez que"), 0049, 0050, 0052 ("pois") e 0058 ("por isso"). C em BQ-0006 ("logo") e BQ-0047 ("pois", com justificativa verdadeira).
  - Finalidade explícita: E em BQ-0016, 0018, 0028, 0039 e 0052.
- Bloco com texto-base (Embrapa 034, it.91–93): 3 itens sobre o mesmo cenário, com gabaritos mistos (2 E, 1 C). É a primeira ocorrência na base de um item que só faz sentido com o texto-base (BQ-0051).

## 4. Marcadores lexicais

Contagem por expressão regular no campo texto_integral dos 60 itens com gabarito, seguida de revisão manual dos falsos positivos. A taxa de base é de 55,0% C / 45,0% E.

AVISO: correlação não é regra. Os n são pequenos, e quase todo marcador aparece nos dois gabaritos. Nenhum marcador decide o gabarito. Use a tabela para diagnosticar vieses de redação, nunca para "adivinhar" o gabarito nem para fabricar itens com gabarito previsível.

Marcadores pedidos pelo papel:

| Marcador | C | E | Itens |
|---|---|---|---|
| "prioritariamente" | 0 | 1 | E: BQ-0010 |
| "sempre" | 0 | 1 | E: BQ-0052 |
| "apenas" | 1 | 1 | C: BQ-0006; E: BQ-0043 |
| "só" restritivo ("só podem") | 0 | 1 | E: BQ-0025 |
| "qualquer" | 1 | 1 | C: BQ-0054; E: BQ-0053 |
| outros absolutos ("exclusivos", "de forma absoluta") | 0 | 2 | E: BQ-0003, 0004 |
| subtotal termo absoluto ou universal | 2 | 6 | ver 3.13 |
| "pois" | 1 | 4 | C: BQ-0047; E: BQ-0003, 0049, 0050, 0052 |
| outros conectores causais ("uma vez que", "logo", "por isso") | 1 | 2 | C: BQ-0006; E: BQ-0019, 0058 |
| "mesmo que" | 1 | 0 | C: BQ-0012 |
| "mesmo sob", "mesmo após" | 0 | 2 | E: BQ-0011, 0023 |

Demais marcadores:

| Marcador | C | E | Itens |
|---|---|---|---|
| "consiste" (definição formal) | 0 | 3 | E: BQ-0010, 0022, 0044 |
| possibilidade afirmativa ("pode", "podem", "poderá", "permite", "permitida", "capaz de"), excluídos "não pode" e "só podem" | 15 | 5 | C: BQ-0001, 0017, 0020, 0021, 0032, 0033, 0035, 0038, 0045, 0046, 0054, 0055, 0061, 0065, 0066; E: BQ-0015, 0039, 0049, 0052, 0057 |
| possibilidade negada ("não pode") | 0 | 1 | E: BQ-0019 |
| dever ("deve", "devem", "deverão", "devendo-se") | 4 | 5 | C: BQ-0005, 0006, 0024, 0037; E: BQ-0002, 0003, 0023, 0040, 0053 |
| negação operativa ("não"), excluídos termos técnicos ("não supervisionado", "não paramétrico", "não rotulados", "não vistos") | 3 | 7 | C: BQ-0006, 0007, 0038; E: BQ-0004, 0019, 0039, 0040, 0041, 0048, 0058 |
| "sem" | 3 | 4 | C: BQ-0032, 0045, 0054; E: BQ-0011, 0043, 0050, 0052 |
| exceção ou dispensa explícita ("excetuando-se", "dispensada") | 1 | 1 | C: BQ-0005; E: BQ-0002 |
| "independe", "independentemente" | 1 | 1 | C: BQ-0027; E: BQ-0022 |
| "desde que" | 0 | 2 | E: BQ-0023, 0057 |
| finalidade explícita ("para garantir", "para otimizar", "com o objetivo de", "visa", "com a finalidade de") | 0 | 5 | E: BQ-0016, 0018, 0028, 0039, 0052 |
| raiz "garant-" | 2 | 4 | C: BQ-0012, 0045; E: BQ-0011, 0016, 0039, 0044 |
| abertura por remissão à fonte ("Conforme", "De acordo com", "Segundo") | 5 | 3 | C: BQ-0006, 0032, 0036, 0037, 0045; E: BQ-0016, 0023, 0025 |
| enumeração "tanto... quanto" | 0 | 2 | E: BQ-0042, 0052 |
| juízo de adequação forte ("indicado", "ideal", "melhor escolha") | 0 | 3 | E: BQ-0049, 0050, 0052 |
| abertura "Considere que" | 0 | 1 | E: BQ-0004 |

Extensão dos itens, em palavras:
- C: média 31,6; mediana 28 (de 8 a 65).
- E: média 34,7; mediana 32 (de 19 a 62).
- A diferença é pequena e não discrimina.

Leituras que a tabela permite, todas com n pequeno:
- A possibilidade afirmativa continua concentrada em C (15 C, 5 E; 75% de C contra 55% na base), mas menos do que a v1.0 sugeria (ver Mudanças). Em E, o "pode" aparece em oração acessória ou na justificativa (BQ-0049, 0052), ou vem com condição falsa (BQ-0057).
- Só aparecem em E: "consiste", finalidade explícita, "tanto... quanto", "desde que" e juízo de adequação forte. Todos têm n de 2 a 5.
- "pois" aparece mais em E (4) do que em C (1). Em BQ-0003, porém, a causa é verdadeira e o erro está na oração principal. Em BQ-0047 (C), a causa é verdadeira e o item, também. "pois" não sinaliza E.
- Os termos absolutos se dividem em 2 C e 6 E, e só em 3 dos 6 E eles são o erro. A semente acertou o mecanismo (E6), mas o marcador sozinho não decide.
- Negação, "sem", "deve", exceção e concessiva aparecem nos dois lados. C3 existe para punir quem acha que esses marcadores discriminam.

## 5. Recomendações às CPPs (redação AUTORAL e [TS])

### 5.1 Regras gerais (valem para todos os padrões)

- Não copie nem parafraseie de perto itens da banca.
  - Não reutilize o par de conceitos de um item-exemplo: integridade/alteração, Naive Bayes/reforço, KNN/classificação, assimétrico/simétrico, controlador/operador, classificação/regressão sobre o cenário de garantia, barras empilhadas/"sempre".
  - Não reutilize a mesma moldura sintática com troca de uma palavra.
  - O que se reaproveita é o mecanismo, não o texto.
- Escreva primeiro a versão C, verdadeira e verificada com fonte. Só depois aplique o mecanismo para obter a versão E. Cada item tem um erro, e um só.
- Marque [TS] quando houver troca sutil: em E1 e E2 sempre; em E4, quando a troca for de um único termo.
- Equilíbrio de cada lote:
  - entre 45% e 60% de C;
  - itens C3 e C6, para não treinar a candidata a marcar E diante de negação, exceção ou definição incompleta.
- Não deixe o marcador coincidir sempre com o mesmo gabarito:
  - escreva E com "pode" e C com "consiste";
  - escreva C com "pois" e com termo absoluto, quando a restrição for a própria definição (como em BQ-0006 e 0054).
- Norma: só a partir de texto do planalto.gov.br verificado pelo qa-normativo, com data. Ferramenta: só com fonte datada do fornecedor, e com a marca VOLÁTIL quando a afirmação depender de produto. Sem fonte, o item fica pendente.
- Os exemplos abaixo são esqueletos ilustrativos, não itens aprovados. Todos passam por QA antes de qualquer uso.

### 5.2 Por padrão

E1 — Troca de conceito vizinho (sem mudança)
1. Escolha um par de conceitos que a candidata pode confundir (precisão × revocação, histograma × gráfico de barras, few-shot × ajuste fino, WER × CER).
2. Atribua a definição de um ao nome do outro e mantenha o restante verdadeiro.

Exemplo: "A revocação de um classificador indica a fração das previsões positivas que de fato pertencem à classe positiva." (E; descreve a precisão) [TS]

E2 — Inversão de definição, de polaridade ou de relação
1. Tome uma definição com direção clara (treino × teste, entrada × saída, "A em nome de B").
2. Inverta a direção e conserve o vocabulário.

Exemplo: "Diz-se que há sobreajuste quando o modelo erra muito nos dados de treino, mas acerta bem em dados novos." (E; a relação está invertida) [TS]

E3 — Alteração do comando normativo
1. Parta do artigo verificado (texto vigente, com a data da consulta).
2. Altere uma só peça do comando: o sujeito, o verbo deôntico, a condição, o prazo, a consequência ou a norma de remissão (esta última é nova, por BQ-0057).
3. Se quiser, acrescente uma justificativa verdadeira com "pois".
4. Não use números ou prazos ausentes do artigo verificado. Sem o qa-normativo, o item não sai.

E4 — Adequação ou escopo: método, paradigma ou ferramenta × tarefa (agora padrão)
1. Liste os métodos e as tarefas que cada um admite, ou monte um texto-base com um problema bem definido.
2. Faça uma destas três coisas:
   - indique para o problema um método de outra natureza;
   - negue uma tarefa que o método admite;
   - enumere dois métodos em que só um admite a tarefa.
3. Ferramentas: negue ou atribua capacidades só no nível da categoria, cuja negação é falsa por definição, como em BQ-0048. Nunca dependa de recurso ou versão de um produto.

Exemplo em bloco com texto-base, com gabaritos mistos. Texto-base: "Um setor deseja medir a qualidade de transcrições automáticas de sessões comparando-as com transcrições de referência revisadas."
- "Nessa situação, o coeficiente de silhueta é a métrica indicada, pois compara a transcrição produzida com a de referência." (E; a silhueta avalia agrupamentos) [TS]
- "Nessa situação, a taxa de erro de palavras (WER) é uma métrica adequada." (C)

E5 — Segmento acessório falso em moldura verdadeira (agora padrão)
1. Escreva uma frase verdadeira completa.
2. Acrescente um segmento falso, no fim ou no meio: uma exceção ("excetuando-se"), uma consequência ("razão pela qual", "não havendo") ou uma premissa causal ("..., por isso").
3. A moldura precisa continuar verdadeira por si.

Exemplo: "A normalização min-max reescala cada atributo para o intervalo [0, 1], razão pela qual a ordem relativa dos valores do atributo deixa de ser preservada." (E; a transformação é monotônica e preserva a ordem)

E6 — Regra relativa convertida em absoluta (novo)
1. Parta de uma afirmação verdadeira do tipo "pode", "é uma das formas" ou "em geral".
2. Converta-a em regra universal com "sempre", "só", "deve... em qualquer caso" ou "antes de qualquer".
3. Faça par, no mesmo lote, com um item C6 ou C3 sobre o mesmo conteúdo sem o quantificador.
4. Inclua também um item C com termo absoluto definicional, para que o marcador não vire atalho.

Exemplos:
- "Registros com valores ausentes devem ser sempre removidos do conjunto antes do treinamento de um modelo de aprendizado de máquina." (E; a imputação é alternativa)
- Par: "A remoção de registros com valores ausentes é uma das formas de tratar dados faltantes." (C)

C1 — Definição canônica correta
1. Escreva a definição de referência com suas palavras, sem palavra-armadilha, a partir de fonte verificada.
2. Também vale classificar corretamente um cenário de texto-base (como BQ-0051).

Exemplo: "Na validação cruzada k-fold, cada observação é usada para validação exatamente uma vez." (C)

C2 — Reprodução próxima do texto normativo
1. Use o texto vigente, verificado pelo qa-normativo, e cite o artigo na justificativa.
2. Prefira dispositivos ligados ao edital (LGPD em sistemas de transcrição e IA).
3. Não faça paráfrase solta, para não cair em C5.

C3 — Item C que parece E
1. Escolha uma regra verdadeira com exceção, negação ou concessiva.
2. Exponha esse traço na frase.

Exemplos:
- "Mesmo sem dispor de rótulos, é possível avaliar um agrupamento por métricas internas, como o coeficiente de silhueta." (C)
- "Instruções explícitas de formato no prompt não garantem, por si sós, que o modelo produza a saída no formato pedido." (C)

C6 — Afirmação parcial verdadeira (novo)
1. Descreva o objeto por um uso típico ou um componente verdadeiro, sem "só", "apenas", "todo" ou "sempre".
2. Confira que a parte afirmada é verdadeira por si, sem depender de tolerância da banca. Se depender, o item vira C5 e não sai.

Exemplo: "Sistemas de reconhecimento automático de fala convertem o sinal de áudio em texto." (C)

C4 — Estranheza aparente (INDÍCIO; usar com parcimônia)

Exemplo: "Um box plot pode ocultar que a distribuição dos dados é bimodal." (C)

Indícios (usar com parcimônia, nunca como fórmula):
- "prioritariamente" deslocando o núcleo. Exemplo: "No few-shot prompting, o modelo se adapta à tarefa prioritariamente pelo ajuste de seus pesos a partir dos exemplos incluídos no prompt." (E) [TS]
- "desde que" com condição trocada (2 E). Use só dentro de E3, com artigo verificado.

### 5.3 O que evitar

- Ambiguidade que leva à anulação. Os três anulados da ANM (BQ-0060, 0062, 0063) têm a mesma justificativa oficial: "o item possibilita mais de uma interpretação". As causas prováveis abaixo são leitura desta coordenação, e a banca não as detalha:
  - notação que admite duas leituras (BQ-0060: "probabilidade condicional p(x|y)" para IA discriminativa);
  - taxonomia de "principais grupos" sem fonte canônica única (BQ-0062);
  - descrição de procedimento que varia conforme a variante do método (BQ-0063, sobre GAN).
  - Os anulados da SUSEP (BQ-0029, 0030, 0031) não têm justificativa localizada.
- Itens cujo gabarito depende de produto (BQ-0064, VOLÁTIL), de versão, de preço ou de número não verificado.
- Paráfrase de norma cujo C depende de tolerância (C5).
- Fazer todo item E carregar um absoluto, um "pois" ou um "consiste", ou todo item C carregar "pode".

## 6. Ressalvas

1. A CLASSIFICAÇÃO É JULGAMENTO DESTE AGENTE (gbq-estilo) E EXIGE REVISÃO DA GBQ. A atribuição de mecanismo primário, as ampliações de definição (E2, E4, E5), os padrões novos (E6, C6) e a reclassificação de BQ-0001 são leituras, não fatos. Pontos mais sensíveis:
   - E5 ampliado: se não for aceito, E5 volta a indício (n = 2).
   - C6: se não for aceito, os três itens voltam a C1.
   - Fronteiras: BQ-0050 (E1 ou E4), BQ-0053 (E5 ou E6), BQ-0004 (E3 ou E6), BQ-0048 (E4 ou E5) e BQ-0054 (C1 ou C3).
2. Os padrões com menos de 3 ocorrências são INDÍCIO, não regra:
   - na tipologia: C4 (n = 2) e C5 (n = 1);
   - nos traços: "prioritariamente" (1), "causa falsa" pura (1) e "desde que" (2).
3. A base é pequena: 60 itens com gabarito, de 2 a 12 por certame. Todos os percentuais têm margem larga. PF 2025 (2 itens, 100% de C) não indica tendência.
4. Inclusão de BQ-0025. A linha estava em CORRIGIR no QA de 09/10 só por causa de observacoes. Foi sanada por D-RECUPERACAO (c), mas não houve nova rodada formal da gbq-cqe. A gbq-gerencia a conta na base válida (R03_reconciliacao). A GBQ deve confirmar. Sem ela, a base seria de 59 itens (33 C / 26 E) e E6 cairia a indício (n = 2).
5. Subitens sem análogo real na base, onde o guia é extrapolação:
   - P1-8.4, P2-1.x, P2-2.x, P2-3.x e P2-4.2. Para P2-4.2 há apenas as leituras alternativas de BQ-0016 e BQ-0040.
   - P1-5.1 e P1-8.2 deixam de ser lacuna: BQ-0059, BQ-0047, 0052 e 0053, todos DIRETOS (D1 R-03).
   - P1-8.3 passa a ter um análogo com ferramenta do edital (BQ-0048).
6. Aderência. Esta coordenação não arbitra. Registram-se:
   - as decisões D1 da R-03: BQ-0049, 0052, 0053 e 0059 DIRETAS; BQ-0055, 0056 e 0057 PARCIAIS;
   - as 7 divergências do QA de 09/10 (BQ-0001, 0009, 0014, 0015, 0016, 0036, 0040), em arbitragem paralela pela gbq-gerencia (T-03).
7. Vigência e fonte não verificadas:
   - Itens de LGPD (17, entre eles BQ-0025, 0056 e 0057): T-13 no qa-normativo, por causa da Lei 15.352/2026.
   - Também pendentes: BQ-0036 (Marco Civil) e BQ-0040 (Resolução CNJ).
   - Ferramentas sem fonte do fornecedor: BQ-0014, 0015, 0017, 0028, 0035, 0048 e 0064. BQ-0064 é VOLÁTIL (T-14).
   - Os mecanismos descritos valem como estilo, não como conteúdo vigente.
8. Não há coluna de comando no CSV, por isso a proporção por tipo de comando não foi calculada.
9. Pontos da semente:
   - Confirmados com n ≥ 3:
     - troca sutil (E1);
     - inversão de definição (E2);
     - item correto e literal da norma (C2);
     - item C que parece E (C3);
     - generalização indevida (tipo 4), agora E6, com a ressalva de que o marcador sozinho não decide;
     - proporção perto de metade.
   - Afirmação verdadeira com causa ou consequência falsa (tipo 3): absorvida por E5. A forma pura tem 1 item (BQ-0058).
   - "prioritariamente": continua INDÍCIO.
   - "Afirmação única por item": há exceções de forma (BQ-0004 com "Considere que"; bloco com texto-base BQ-0049 a 0051).
   - "Nunca: item que depende de versão de software": continua válida.

## 7. Mudanças v1.0 → v1.1

Base:
- Itens com gabarito: 42 → 60.
- Certames: 6 → 9 (+Embrapa 2024, ANM 2024, PF 2025).
- C: 24 → 33. E: 18 → 27. %C: 57,1 → 55,0.
- Anulados fora: 3 → 6.
- BQ-0025 incluída.

| Padrão | v1.0 | v1.1 | Situação | Itens que entraram ou saíram |
|---|---|---|---|---|
| E1 Troca de conceito vizinho | 6 (padrão) | 6 (padrão) | mantido | — |
| E2 Inversão de definição, de polaridade ou de relação | 4 (padrão) | 5 (padrão) | reforçado; definição ampliada (inversão de relação) | +BQ-0056 |
| E3 Alteração do comando normativo | 4 (padrão) | 5 (padrão) | reforçado; inclui troca da norma de remissão | +BQ-0057 |
| E4 Adequação ou escopo × tarefa | 2 (indício) | 5 (padrão) | promovido de indício a padrão; ampliado de "algoritmo" para "método, paradigma ou ferramenta" | +BQ-0048, 0049, 0050 |
| E5 Segmento acessório falso (ex-"cauda falsa") | 2 (indício) | 3 (padrão) | promovido de indício a padrão; ampliado de "cauda" para "segmento acessório" (sujeito à revisão da GBQ) | +BQ-0058 |
| E6 Regra relativa convertida em absoluta | — | 3 (padrão) | novo; recupera o tipo 4 da semente | +BQ-0025, 0052, 0053 |
| C1 Definição canônica | 11 (padrão) | 17 (padrão) | reforçado | −BQ-0001 (para C6); +BQ-0047, 0051, 0054, 0055, 0061, 0064, 0066 |
| C2 Reprodução próxima da norma | 4 (padrão) | 4 (padrão) | mantido | — |
| C3 C redigido para parecer E | 6 (padrão) | 6 (padrão) | mantido | — |
| C4 Estranheza aparente | 2 (indício) | 2 (indício) | mantido como indício | — |
| C5 Paráfrase normativa aceita | 1 (indício) | 1 (indício) | mantido como indício | — |
| C6 Afirmação parcial verdadeira | — | 3 (padrão) | novo | BQ-0001 (de C1), +BQ-0059, 0065 |
| Removidos | — | — | nenhum | — |

Totais:
- Padrões: 6 → 10.
- Indícios de tipologia: 4 → 2.
- Nenhum padrão foi rebaixado a indício.

Traços e marcadores:
- "Termo absoluto como fonte de erro": de 1 (indício) para 3 + 1 concorrente, e virou o padrão E6.
- "Causa falsa" pura: de 0 para 1 (indício, dentro de E5).
- Traços novos: "desde que" (indício, 2 E) e "juízo de adequação forte" (3 E).
- Forma situacional: de 1 para 2 ocorrências (bloco com texto-base).
- Recontagem da possibilidade afirmativa:
  - A v1.0 informou 8 C / 1 E. Com a regra explícita desta versão, a base antiga dá 10 C / 2 E: a v1.0 omitiu BQ-0038 e 0046 (C) e BQ-0039 (E).
  - Na base atual, 15 C / 5 E.
- Marcadores acrescentados à tabela: "sempre", "só", "qualquer", "pois" (separado dos demais causais), "desde que" e juízo de adequação.
- Os demais marcadores foram recontados sobre 60 itens.

Recomendações:
- Novas seções para E4, E6 e C6, com a técnica do bloco com texto-base de gabaritos mistos.
- Pareamento E6 × C6.
- Seção "O que evitar", com a lição dos anulados da ANM.

AVISO: a classificação é julgamento do agente gbq-estilo e exige revisão da GBQ antes de orientar produção.
