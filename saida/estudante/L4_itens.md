# Lote 4 — Conceitos básicos de inteligência artificial; Ética e responsabilidade digital no serviço público (P1 5.1–5.3 e 6) — itens

Itens para julgar (C = certo, E = errado). Gabarito e justificativas no arquivo L4_gabarito.md.

**Comando.** Acerca da engenharia de prompts, julgue os itens a seguir.

**L4-01** — A engenharia de prompts consiste em projetar e refinar as instruções fornecidas a um modelo de linguagem para obter a saída desejada, sem alteração dos parâmetros internos do modelo.

**L4-02** — Na técnica denominada few-shot, o prompt contém um único exemplo da resposta esperada, o que a distingue da técnica zero-shot, em que nenhum exemplo é fornecido.

**L4-03** — O encadeamento de prompts (prompt chaining) é a técnica em que se solicita ao modelo, em um único prompt, que explicite seu raciocínio passo a passo antes de apresentar a resposta final.

**L4-04** — A redução da temperatura de um modelo de linguagem torna suas respostas mais previsíveis, mas não assegura que o conteúdo gerado seja factualmente correto.

**L4-05** — Delimitar as partes de um prompt com marcadores como tags XML ou seções em Markdown contribui para que o modelo distinga instruções de dados de referência.

**L4-06** — A geração aumentada por recuperação (RAG) consiste em retreinar o modelo com os documentos da organização, de modo que esse conhecimento passe a integrar os parâmetros do modelo.

**Comando.** A respeito dos tipos de aprendizado de máquina, julgue os itens a seguir.

**L4-07** — No aprendizado supervisionado, o modelo é treinado com exemplos que já contêm a resposta correta, e a tarefa de prever um valor numérico, como a quantidade de chuva em milímetros, é denominada regressão.

**L4-08** — No agrupamento (clustering), técnica de aprendizado não supervisionado, as categorias são definidas previamente pelo analista, cabendo ao modelo atribuir cada dado a uma delas.

**L4-09** — Diz-se que o aprendizado é não supervisionado quando o processo dispensa qualquer participação humana, inclusive na interpretação dos padrões encontrados.

**L4-10** — No aprendizado por reforço, o agente aprende por meio de recompensas e penalidades decorrentes de suas ações em um ambiente, sem que lhe seja fornecido, para cada entrada, o rótulo da ação correta.

**L4-11** — Os modelos de IA generativa são, em regra, pré-treinados com grandes volumes de dados sem rótulos atribuídos manualmente e, em etapa posterior, podem ser ajustados por aprendizado supervisionado ou por reforço para tarefas específicas.

**Comando.** Acerca da IA generativa, julgue os itens a seguir.

**L4-12** — Um modelo discriminativo aprende a fronteira entre categorias, ao passo que um modelo generativo aprende a distribuição dos dados, o que lhe permite produzir novas instâncias.

**L4-13** — Todo modelo de fundação é um grande modelo de linguagem (LLM), uma vez que ambos os termos designam modelos pré-treinados exclusivamente em grandes volumes de texto.

**L4-14** — Denomina-se alucinação a produção, por um modelo de IA generativa, de conteúdo plausível, porém factualmente incorreto.

**L4-15** — Um grande modelo de linguagem, por si só, consulta bases de dados e a internet em tempo real antes de responder, razão pela qual suas respostas refletem sempre a informação mais atual disponível.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

**L4-16** — O ajuste fino (fine-tuning) e a geração aumentada por recuperação (RAG) são formas equivalentes de incorporar conhecimento a um modelo, diferindo apenas no custo computacional.

**Comando.** No que se refere à ética e à responsabilidade digital no serviço público, julgue os itens a seguir.

**L4-17** — Segundo a LGPD, os dados anonimizados não são considerados dados pessoais, salvo quando o processo de anonimização puder ser revertido com esforços razoáveis.

**L4-18** — Para a administração pública, o consentimento do titular é a única hipótese legal que autoriza o tratamento de dados pessoais necessários à execução de políticas públicas.

**L4-19** — Quando um servidor público utiliza sistema de inteligência artificial para elaborar documento oficial, a responsabilidade pelo conteúdo do documento transfere-se ao fornecedor do sistema.

**L4-20** — Nos termos da LAI, a publicidade é o preceito geral e o sigilo, a exceção, o que não impede a restrição legal de acesso a informações pessoais e a informações classificadas como sigilosas.

**Comando.** Acerca da engenharia de prompts, julgue os itens a seguir.

**4C-01** — No prompt, o contexto é o conjunto de demonstrações de entrada e saída que ilustram a resposta esperada, ao passo que os exemplos são o texto de referência sobre o qual o modelo deve trabalhar.

**4C-02** — O emprego de vários exemplos no prompt (few-shot) costuma produzir resultados melhores que o zero-shot e o one-shot, ao custo de um prompt mais longo.

**4C-03** — O resultado produzido por um modelo de linguagem a partir de um prompt depende não apenas do texto do prompt, mas também de outros fatores, como os dados de treinamento do modelo e a temperatura adotada.

**4C-04** — A janela de contexto designa o grau de aleatoriedade das respostas de um modelo de linguagem, ao passo que a temperatura corresponde ao limite de tokens que o modelo processa por requisição.

**4C-05** — Um prompt que reúna papel, formato de saída e restrições bem definidos elimina o risco de alucinação, tornando dispensável a conferência humana da resposta.

**4C-06** — Um prompt composto apenas por uma instrução detalhada, que descreve inclusive o formato desejado da resposta, mas que não traz nenhuma demonstração de entrada e saída, caracteriza a técnica zero-shot, ainda que a instrução seja extensa.

**4C-07** — Na engenharia de prompts, a definição de critérios de sucesso claros e a realização de testes a cada alteração do prompt permitem avaliar se a modificação melhorou o resultado obtido.

**4C-08** — A injeção de prompt restringe-se à digitação, pelo próprio usuário, de instruções destinadas a burlar as restrições do modelo, não abrangendo instruções maliciosas embutidas em textos que o modelo lê.

**4C-09** — Para que um modelo de linguagem, sem acesso a ferramentas externas (como a busca) ou a RAG e sem retreinamento, resuma um relatório interno elaborado depois do seu treinamento, o texto do relatório deve ser incluído no prompt, como contexto.

**4C-10** — A determinação, no prompt, de que o modelo não atribua a um orador fala que ele não tenha feito constitui especificação do formato de saída, e não restrição ao comportamento do modelo.

## Itens de reforço

**Texto-base.** Uma unidade da Câmara pretende treinar um modelo para indexar automaticamente proposições por tema, usando como exemplos de treinamento a indexação já feita por servidores em anos anteriores.

**L4-R01** — Nessa situação, o modelo será treinado por aprendizado supervisionado, em tarefa de classificação, porque a indexação anterior funciona como o rótulo de cada proposição.

**Texto-base.** Revisores do Derep (antigo DETAQ) avaliam, com aprovação ou reprovação, as minutas geradas por um assistente de redação baseado em IA generativa.

**L4-R02** — Se a equipe técnica usar essas avaliações como feedback humano para ajustar as respostas futuras do modelo, a técnica empregada corresponde ao aprendizado por reforço com feedback humano (RLHF).

**L4-R03** — No aprendizado por reforço, denomina-se política a recompensa que o agente recebe em razão das ações que executa no ambiente.

**Texto-base.** Um laboratório treina um robô para aprender a caminhar por uma sala, por tentativa e erro, em interação com o ambiente.

**L4-R04** — Nessa situação, o treinamento descrito constitui exemplo de aprendizado não supervisionado.

**L4-R05** — Um modelo de classificação cuja saída é apenas uma entre duas classes, como "chuva" ou "sem chuva", é denominado de classificação binária; se admitir mais de duas classes, é de classificação multiclasse.

**Texto-base.** Um órgão da Câmara recebeu cerca de 40 mil contribuições escritas em uma consulta pública e pretende agrupá-las por semelhança de conteúdo, sem temas definidos antes, para descobrir os assuntos mais citados.

**L4-R06** — Nessa situação, a tarefa descrita configura aprendizado supervisionado.

**Texto-base.** Uma equipe constrói um modelo de regressão para estimar o preço futuro de uma casa.

**L4-R07** — Nesse modelo, a metragem, o CEP, o número de quartos e de banheiros e a taxa de juros do financiamento são atributos de entrada, e o preço da casa é o valor previsto.
