# Lote 4-C — TID-IA, complemento (P1 5.1) — gabarito e justificativas

Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada de técnica (AT), inversão de causa e efeito (IC)

### 4C-01 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: TC (elementos do prompt trocados). Curso 5.1.2: o CONTEXTO (ou material de referência) é o texto sobre o qual o modelo deve trabalhar; os EXEMPLOS são demonstrações de entrada e saída. O item troca as definições. Difere do item 2 do Lote 4 porque aquele julga o número de exemplos que define o few-shot; este julga o que é "contexto" e o que é "exemplo" na anatomia do prompt. Fonte: curso 5.1.2 (itens 3 e 4).

### 4C-02 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: sem armadilha (ancoragem). Curso 5.1.3: o few-shot costuma produzir resultados melhores que o zero-shot e o one-shot, ao custo de um prompt mais longo. O item usa "costuma", como o curso, e não afirma ganho garantido. Difere do item 2 do Lote 4 porque aquele julga a definição de few-shot pelo número de exemplos; este julga o efeito relatado e o custo.

### 4C-03 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: GI invertida (tentação: "engenharia de prompts controla a saída; logo o prompt é o único fator" → marcar E). Curso 5.1.1: o resultado depende, entre outros fatores, dos dados de treinamento e da temperatura. O item diz que o prompt não é o único fator, sem afirmar que o texto do prompt é irrelevante. Difere do item 4 do Lote 4 porque aquele julga a relação entre temperatura baixa e veracidade; este julga a pluralidade de fatores que determinam a saída.

### 4C-04 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: TC (definições trocadas). Curso 5.1.4: temperatura é o hiperparâmetro que controla o grau de aleatoriedade da saída; janela de contexto é o limite de tokens que o modelo processa por requisição. O item inverte as duas definições. Difere do item 4 do Lote 4 porque aquele julga se temperatura baixa assegura veracidade; este julga a definição de temperatura e a de janela de contexto. Fonte: curso 5.1.4 (janela de contexto, conceito geral).

### 4C-05 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: GI. Curso 5.1.4 e 5.1.6, P5: um prompt bem construído REDUZ, mas não ELIMINA alucinações; o curso 5.3.5 e o princípio 7 do curso 6.2 exigem conferir a saída antes de usá-la. "Elimina" e "dispensável a conferência humana" são generalização indevida. Difere do item 14 do Lote 4 porque aquele julga a definição de alucinação; este julga o alcance do prompt como medida contra ela. Fonte: curso 5.1.4 (conceito consistente com a definição de alucinação).

### 4C-06 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: AT (tentação: tomar a instrução longa ou a descrição do formato desejado por "exemplo" e concluir que o prompt é one-shot → marcar E). Curso 5.1.2 (itens 4 e 5): exemplos são demonstrações de entrada e saída; o formato de saída é a forma da resposta (tabela, JSON, número de linhas) e, descrito em palavras, não é demonstração. Curso 5.1.3: zero-shot = prompt sem nenhum exemplo de resposta esperada, só a instrução. A extensão da instrução e a descrição do formato não a transformam em exemplo. Difere do item 2 do Lote 4 porque aquele julga o few-shot pelo número de exemplos (um único exemplo é one-shot); este julga o zero-shot pela ausência de qualquer demonstração, ainda que a instrução seja longa e detalhada. Fonte: curso 5.1.2 e 5.1.3.

### 4C-07 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: sem armadilha (ancoragem). Curso 5.1.1: engenharia de prompts é a prática de projetar, testar e iterar prompts; curso 5.1.3: a iteração e avaliação pressupõem critérios de sucesso claros e testes empíricos e a medição do comportamento a cada mudança de prompt. O item afirma só o conceito geral, sem recurso de produto.

### 4C-08 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: GI (restrição indevida do conceito; tentação: tratar a injeção de prompt como sinônimo do ataque direto do usuário). Curso 5.1.4: injeção de prompt = instruções maliciosas embutidas em textos que o modelo lê e que tentam sobrepor-se às instruções legítimas (conceito geral, sem fonte de fornecedor, como no curso). O item não depende de a literatura tratar o jailbreak como espécie de injeção ou como categoria distinta; basta que a injeção abranja as instruções embutidas em textos lidos, o que o curso afirma e o termo "restringe-se" nega. O item não usa o par injeção × jailbreak (C19) como critério. Fonte: curso 5.1.4.

### 4C-09 — Gabarito: C

- Item do edital: P1-5.1
- Justificativa: sem armadilha (ancoragem). Curso 5.1.2 (item 3): o contexto é o texto sobre o qual o modelo deve trabalhar; curso 5.1.3: o RAG recupera documentos e os insere no prompt; curso 5.3.3: sem ferramentas ou RAG, o modelo responde com o que incorporou no treinamento (conhecimento paramétrico). Um relatório elaborado depois do treinamento não integra esse conhecimento; sem ferramentas externas (como a busca), sem RAG e sem retreinamento, o caminho é incluí-lo no prompt, como contexto. O acréscimo "e sem retreinamento" existe porque o curso (5.1.1; 5.3.3) prevê o fine-tuning como outra forma de incorporar conhecimento: sem a ressalva, o "deve" ficaria vulnerável a recurso. Difere do item 15 do Lote 4 porque aquele julga se o modelo consulta fontes externas por si só; este julga a aplicação (o material entra como contexto do prompt). Difere do item 6 do Lote 4 porque aquele julga RAG × retreinamento. Fonte: curso 5.1.2, 5.1.3 e 5.3.3.

### 4C-10 — Gabarito: E

- Item do edital: P1-5.1
- Justificativa: TC (formato × restrição; não sutil). Curso 5.1.2 (item 6): restrições e critérios indicam o que o modelo NÃO deve fazer ("não invente nomes"); curso 5.1.5: no exemplo, "não atribua a um orador fala que ele não tenha feito" é restrição, e não formato. Formato de saída (item 5 do curso 5.1.2) é a forma da resposta (tabela, JSON, número de linhas). O item julga apenas a natureza da determinação negativa, sem depender da fronteira entre formato e restrição em instruções mistas. Fonte: curso 5.1.2 e 5.1.5.
