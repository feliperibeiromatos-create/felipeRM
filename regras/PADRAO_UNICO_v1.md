# PADRÃO ÚNICO DE PRODUÇÃO DE CONTEÚDO — v1 (14/10/2026)
Documento canônico do método. Vale para toda linha de conteúdo: Câmara 2026, LGPD, Direito Administrativo e o que vier. Escrito uma vez; cada fábrica aponta para ele. Quem muda este documento é o Fundador; a Presidência propõe.

Origem: consolida as regras validadas no Projeto Câmara 2026 entre 7 e 14/10/2026, que produziram 210 itens inéditos canônicos, banco de 112 itens reais verificados e plataforma publicada.

---

## 1. UNIDADE DE PRODUÇÃO: O LOTE
Toda matéria é dividida em lotes. Um lote = um bloco de itens contíguos do edital ou do índice do curso. Entrega padrão de um lote:

(a) CURSO, item a item: definição precisa; exemplo aplicado ao contexto de uso; "pegadinha provável".
(b) RESUMO de uma página.
(c) PARES CONFUNDÍVEIS: mínimo 8, com a coluna "como a banca troca".
(d) ITENS INÉDITOS C/E: 20 por lote; 30 quando o subitem não tiver item real análogo. Numerados `<lote>-NN`. Cada um com enunciado, gabarito, justificativa de duas linhas. Metade com troca sutil de um único conceito, marcada [TS].
(e) DISCURSIVA, quando a prova tiver: comando com aspectos valorados + padrão de resposta no formato da banca.
(f) TABELA DE PROVENIÊNCIA: toda afirmação sobre ferramenta, produto ou norma, com URL oficial e data.

Marcas obrigatórias por item: [TS] (troca sutil), VOLÁTIL (depende de produto/versão; inapto a simulado final até reverificação datada), REVERIFICAR (norma que pode mudar).

## 2. EVIDÊNCIA E PROVENIÊNCIA
- Afirmação sobre ferramenta, API, produto ou modelo: "verificado em [data]" + URL oficial do fornecedor. Sem fonte: escrever "[SEM FONTE — não afirmar]". Nunca versão, preço ou limite sem fonte datada.
- Norma: citação por artigo, inciso e parágrafo, do texto compilado no site oficial (no Brasil, planalto.gov.br), com data da cópia. Registrar alterações recentes.
- Rótulos de questão: OFICIAL (prova do certame-alvo ou do seu ciclo), ANALOGA (outro certame da mesma banca), OUTRA_OFICIAL (outra banca), AUTORAL (inédita). Rótulo "estilo" é proibido.
- Item real só entra no banco depois de conferido contra o gabarito definitivo oficial. "X" no definitivo = anulado, fora do banco. Espelhos de terceiros (sites de questões, cursinhos) são vedados, mesmo quando reproduzem o PDF oficial.
- Convenção de ano: "ano do edital (aplicação dd/mm/aaaa)".
- Item de múltipla escolha não entra em banco de prova C/E; registra-se a existência como evidência de que o tema é cobrado.
- Item sem QA leva a marca "QA PENDENTE" e nunca entra em simulado.

## 3. SEPARAÇÃO PRODUÇÃO × QA (a regra que mais evitou erro)
- Quem produz não revisa. Nunca, em nenhuma hipótese, o mesmo agente ou chat faz as duas coisas sobre o mesmo texto.
- Produção e QA em modelos distintos. Se os dois lados forem do mesmo fornecedor, usar modelos diferentes; se houver dois fornecedores, melhor ainda.
- Ciclo: v1 → QA rodada 1 → v2 (com resposta item a item: acatado / não acatado + motivo) → QA rodada 2 → reconciliação pela gerência → aceite humano.
- Gate: QA reprovando mais de 30% dos itens interrompe o ciclo e exige decisão humana.
- Discursiva: correção em dupla cega, dois corretores que não veem o trabalho um do outro, reconciliada pela gerência.

## 4. QA NORMATIVO
Conteúdo que depende de lei passa por verificação do texto vigente antes da produção, não depois. O verificador abre a URL oficial, transcreve o dispositivo e registra data. Se não conseguir abrir, declara "não aberta" — nunca substitui por memória nem por fonte secundária.

## 5. PADRÃO DE RESPOSTA DE DISCURSIVA (formato Cebraspe; adaptável a outras bancas)
1. Comando: situação hipotética + ordem ("redija parecer técnico com base em [norma]") + aspectos numerados com valor em pontos.
2. Padrão: texto corrido com os aspectos enumerados (i), (ii), (iii)…, cada um com qualificação do fato, consequência e base normativa por artigo.
3. Quesitos avaliados: cada quesito com conceitos de 0 a N; conceito k = "abordou corretamente k dos aspectos enumerados".
4. Regra de ouro: a nota vem da cobertura de aspectos, não da qualidade argumentativa. A apresentação vale uma fração pequena. Erros gramaticais descontam por fórmula do edital.

## 6. ESTILO DE ITEM (ampliado pelo banco de cada linha)
Forma: "Julgue o item"; afirmação única; sem "exceto", sem alternativas.
Mecanismos que levam a ERRADO: troca sutil de um conceito em frase no restante verdadeira; inversão de definição; afirmação verdadeira com causa falsa; generalização indevida ("sempre", "apenas", "exclusivamente").
Mecanismos que levam a CERTO: definição correta e literal da norma ou da documentação oficial; item que parece errado por soar simples demais.
Proporção observada: perto de metade C, metade E; não forçar.
Nunca: item que dependa de versão de software, preço ou número não verificado.
Regra de catálogo: padrão sustentado por menos de 3 itens reais é "indício", não padrão.

## 7. CONTRATO DE DADOS: pacote.json
Arquivo único que liga qualquer fábrica à plataforma. Campos:
`versao`, `geradoEm`, `nome`; `edital` (id, prova, texto); `itens` (id, rotulo, certame, cargo, ano, numero, comando, comandoOriginal, textoBase, enunciado, gabarito C|E, justificativa, itemEdital, aderencia direta|parcial, volatil, url); `simulados` (id, nome, tipo diagnostico|final, itens[]); `lotes` (id, nome, prova, itensEdital[], resumo, curso, pares[], pegadinhas[]); `discursivas` (id, tipo, comando, aspectos[], padrao, quesitos[]).
Duas saídas por geração: o pacote completo (com justificativas internas) e a "edição do estudante" (sem notas internas de QA).
Matéria nova entra como módulo no mesmo contrato. A plataforma não muda.

## 8. PLATAFORMA
Uma só, alimentada por pacote.json: trilha de lotes, teste de lote, simulado no formato da prova, caderno de erros com revisão espaçada (sai após dois acertos seguidos), painel de cobertura, folha de discursiva, véspera. Progresso no aparelho do aluno.
Desempenho em pílula com o número dentro: abaixo de 60% de nota líquida vermelho; 60% a 80% inclusive amarelo; acima de 80% verde. Nota líquida = (acertos − erros) ÷ itens apresentados.
Sistema visual: papel #FBFBF8, tinta #1B2A41, cinza #4F5B6B, marcador #F2C94C, acerto #2E7D5B, erro #9C2E2E; fonte Atkinson Hyperlegible; traço 2 px; alvo mínimo 44 px, primário 56 px; uma instrução e uma ação primária por tela. Proibido: emoji, fotos de banco, gradientes decorativos, sombras, informação que dependa só de cor, texto abaixo de 13 px, amarelo como cor de texto.

## 9. GOVERNANÇA MÍNIMA
- Uma fábrica por linha de conteúdo, mesma estrutura de pastas e agentes, apontando para este padrão.
- Fila única por fábrica (TAREFAS.md), decisões por arquivo (DECISOES.md), saída para o humano só em gatilho (PARA_PRESIDENCIA.md / PARA_FUNDADOR.md).
- Gatilhos de retorno ao humano: pacote concluído e reconciliado; necessidade fora do domínio; conflito que a regra não resolve; decisão de mérito; matéria reservada ao Fundador.
- Matérias reservadas ao Fundador: gasto; o que chega ao aluno e quando; escopo; adoção de ferramenta; exclusão de ativo; pausa de linha.
- Backup ao fim de todo ciclo. Perder a pasta uma vez já bastou.
- Um único editor por arquivo canônico. Duas estruturas editando o mesmo arquivo geram versões divergentes.

## 10. MULTIFORNECEDOR (Claude + ChatGPT)
Princípio: fornecedor diferente é a melhor separação de QA que existe, porque os erros não são correlacionados.
- O Claude mantém o padrão, a arbitragem e a plataforma.
- O ChatGPT produz as linhas em que for melhor; a fábrica do Claude revisa. O inverso também vale: o Claude produz, o ChatGPT revisa.
- Nenhum dos dois revisa a própria produção, nem opera como segunda presidência.
- Entrega do produtor externo no formato da seção 1, para entrar no ciclo sem adaptação.
- Teste cego, sempre que houver dúvida sobre quem é melhor em uma matéria: a mesma unidade produzida pelos dois, QA independente comparando as duas versões sem saber a origem, veredito por cobertura, correção, evidência e estilo. Precedente: no Lote 5 do Câmara 2026, nenhuma das duas versões era aprovável sozinha e a fusão foi melhor que as duas.
