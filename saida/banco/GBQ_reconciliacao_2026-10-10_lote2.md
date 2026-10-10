# GBQ_reconciliacao_2026-10-10_lote2.md — T-07 e T-10 — 2026-10-10 — gerado por gbq-gerencia

Papel: gbq-gerencia, nível D1.

Regras aplicadas:
- CLAUDE.md;
- DECISOES.md: D-ADERENCIA, D-QA-PENDENTE, D-ROTULOS, D-MC, D-BANCO-TI-1-4, D-LEI-15352, D-SIM1-CANONICO (critério de aceite de simulado final) e D-FUNDADOR-AGORA-1;
- regras/pacote_contrato.md v1.1, com a leitura D1 da regra 2 dada na reconciliação lote1;
- registro AUTORAL v3, regras R1 a R4;
- orquestradores/BANCO.md.

Escritas feitas nesta reconciliação:
- banco/banco.csv, só nas linhas BQ-0067 a BQ-0112 (seção 1.4);
- append de errata em saida/banco/varredura_2026-10-10.md;
- append único em TAREFAS.md (T-40 a T-42);
- append único em PARA_PRESIDENCIA.md (gatilho A do Simulado 2).

O git só foi lido. Os simulados não foram editados.

## 1. T-07 — terceira varredura (gbq-cfp → gbq-cqe)

### 1.1 Conferência

- O QA, saida/banco/qualidade_2026-10-10_T07.md, traz 46 APROVADOS, 0 CORRIGIR, 0 REPROVADOS e 0 NÃO VERIFICÁVEIS (0%). Os 46 aprovados são BQ-0067 a BQ-0112, com 27 C e 19 E.
- Os downloads da gbq-cqe são independentes dos da produtora. A conferência de texto e de gabarito é literal (46/46). A proveniência e o D-ROTULOS conferem (todos CEBRASPE_ANALOGA), e não há múltipla escolha.
- A gerência conferiu por script:
  - o banco tem 112 linhas;
  - as 46 linhas novas tinham o prefixo "QA PENDENTE; ";
  - C/E = 27/19 confere;
  - todas as observacoes trazem o segmento "comando:";
  - as linhas BQ-0001 a 0066 não mudaram desde a reconciliação lote1 (SHA-256 4ebee3510c9bf0a4…).

Veredito: CONCLUÍDA. A varredura fica reconciliada com as decisões D1 abaixo.

### 1.2 Arbitragem de aderência e mapa

O critério é o do R03 e da T-03: DIRETA quando o item cobra o que o subitem nomeia; PARCIAL quando cobra tema vizinho ou genérico, versão não nomeada ou nível acima de noções. A base é D-ADERENCIA.

| id | antes | decisão D1 | motivo |
|---|---|---|---|
| BQ-0072 | P1-6 DIRETA | P1-6 DIRETA (leitura 1) | O uso de IA institucional é julgado pelo código de ética do servidor. É "ética e responsabilidade digital no serviço público" no sentido literal. Vai ao qa-normativo (T-40). |
| BQ-0111 | P1-6 PARCIAL | P1-4 DIRETA (leitura 2) | Princípios e diretrizes do Governo Digital (Lei 14.129/2021, art. 3º) são "conceitos gerais de governança digital" (item 4 do edital, D-BANCO-TI-1-4). É o primeiro análogo real de governança digital: interessa à T-19 (R-5, BACKLOG). Vai ao qa-normativo (T-40). |
| BQ-0069 | P1-2.1 PARCIAL | P1-2 DIRETA (leitura 2) | As camadas do modelo TCP/IP são o núcleo de "Redes de computadores", em nível de noções. |
| BQ-0070, 0071 | P1-2 PARCIAL | P1-2 DIRETA (leitura 2) | O item 2 do edital é genérico, e a função do NAT e do DHCP é conteúdo básico de rede. Dependem do texto do comando (T-42). |
| BQ-0080, 0081 | P1-1 PARCIAL | P1-1 PARCIAL (leitura 1) | A versão nomeada no item (Excel 2019) não é a do edital (MSOffice 365). |
| BQ-0085, 0087 | P1-1 PARCIAL | P1-1 DIRETA (leitura 2) | O edital nomeia Excel e Word, e o item não fixa versão. Não se afirma igualdade de comportamento no 365 ([SEM FONTE — não afirmar]). O que decide é o critério de nomeação. |
| BQ-0089 | P1-2.1 PARCIAL | P1-2.1 DIRETA (leitura 2) e VOLÁTIL | Motor de busca é ferramenta e procedimento de Internet. O gabarito depende do comportamento atual do Google (aspas, pontuação e capitalização), por isso é VOLÁTIL (T-41). |
| BQ-0099 | P1-8.1 PARCIAL | P1-8.1 PARCIAL (leitura 1) | O item cobra a utilidade gerencial do dashboard, não um princípio de visualização. |
| BQ-0102 | P1-5.2 PARCIAL | P1-5 DIRETA (leitura 2) | A definição de aprendizado de máquina é conceito básico de IA (item 5). É o mesmo tratamento dado a BQ-0009 na T-03. |
| BQ-0106 | P1-5.2 DIRETA | P1-5.2 DIRETA (leitura 1) | O objeto é agrupamento de dados não rotulados, o não supervisionado do 5.2. A tipologia dos algoritmos é detalhe do mesmo tema. |
| BQ-0076 | P1-4.3 DIRETA | P1-4.3 DIRETA (leitura 1), correlato P1-4.2 | O phishing está nomeado no 4.3. A marca VOLÁTIL é mantida (T-41). |
| BQ-0092 | P1-1 PARCIAL | P1-1 PARCIAL, fora de simulado (leitura 2) | O gabarito E oficial é contraintuitivo e não tem justificativa publicada, e o produto é o Office 2010. Fica só para estudo, com o gabarito oficial. A regra decorre da montagem de simulados, que é governada pela GBQ. |
| BQ-0077, 0084, 0109, 0110 | P2-4.1 "aderência ampla" | P2-4.1 PARCIAL | É LGPD geral, não LGPD em sistemas de transcrição e IA, coerente com BQ-0056 e 0057 (R03). |

A redação "aderência ampla" foi corrigida porque a expressão não consta da regra 2 do contrato v1.1. Sem a correção, os 4 itens sairiam como "direta" no pacote.

Os demais itens ficam como estão no banco, sem divergência no QA.

### 1.3 VOLÁTIL, qa-normativo e pendências

- VOLÁTIL: BQ-0075, 0076 e 0086 (marca da produtora, confirmada pelo QA) e BQ-0089 (D1). O prefixo segue o formato de BQ-0064 e BQ-0015, e todos vão à reverificação de janeiro (T-41). BQ-0080, 0081, 0085 e 0087 descrevem funções estáveis e não recebem a marca, como o QA registrou.
- Vão ao qa-normativo (T-40), pela regra de fonte normativa do Projeto, por artigo e inciso: BQ-0072 (Decreto 1.171/1994), BQ-0077, 0084, 0109 e 0110 (LGPD frente à Lei 15.352/2026) e BQ-0111 (Lei 14.129/2021).
  - A conferência do QA de banco localizou os dispositivos, mas não substitui o qa-normativo.
  - Até a T-40 concluir, os 6 itens ficam fora de qualquer simulado. A marca é "aguarda qa-normativo (T-40)", que não confunde com "QA PENDENTE".
  - Em BQ-0110, a nota "conferir contra a LGPD compilada" deu lugar ao resultado do QA de banco (art. 4º sem alteração pela Lei 15.352/2026, verificado em 2026-10-10).
- Recomendação do QA sobre preliminar × definitivo: aceita. A observacoes de cada linha registra o estado do gabarito preliminar:
  - "gabarito preliminar localizado, igual ao definitivo" em DATAPREV, CTI, TRF6 e Câmara 2012;
  - "preliminar e justificativas não localizados no CDN" no PF Administrativo (12 itens);
  - "preliminar não localizado; item ausente do PDF de justificativas" no PF Policial e na FUB.
- Pacote: os 46 itens não entram na T-27. Pela regra 3 do contrato v1.1 e pela linha T-29, item de banco fora de simulado espera as colunas de comando. A T-42 estende a T-29 a essas linhas. Até lá, só os 60 itens C/E de BQ-0001 a 0066 vão ao pacote, como a T-27 já prevê.

### 1.4 banco/banco.csv — alteração aplicada

- Foram alteradas 46 linhas, todas entre BQ-0067 e BQ-0112:
  - observacoes nas 46;
  - item_edital_camara em 3 (BQ-0069 → P1-2; BQ-0102 → P1-5; BQ-0111 → P1-4).
- As 66 primeiras linhas e o cabeçalho ficaram intactos byte a byte. Os gabaritos e o texto_integral não mudaram.
- Formato: csv.reader/csv.writer, delimiter ';', lineterminator '\n', QUOTE_MINIMAL.
- Antes de gravar, o arquivo foi conferido contra a leitura inicial.
- SHA-256: 4ebee3510c9bf0a4… antes e 969c0bfd7ff03c10… depois. A cópia de antes está em scratchpad s3/gbq_rec/banco_antes_lote2.csv.
- Conferência depois de gravar:
  - 0 "QA PENDENTE" no intervalo;
  - aderência pela regra 2 (sem distinção de maiúsculas e minúsculas): 30 DIRETA e 16 PARCIAL, cada uma coerente com a palavra declarada em observacoes;
  - 4 VOLÁTEIS;
  - 6 itens aguardando a T-40;
  - 7 itens fora de simulado (os 6 da T-40 e BQ-0092);
  - 24 itens aptos a simulado final (DIRETOS, não VOLÁTEIS e fora da T-40).
- Por subitem, DIRETA/PARCIAL:
  - P1-1: 2/4
  - P1-2: 5/0
  - P1-2.1: 2/0
  - P1-4: 1/0
  - P1-4.1: 6/1
  - P1-4.2: 4/1
  - P1-4.3: 1/0
  - P1-5: 1/0
  - P1-5.2: 4/1
  - P1-6: 1/0
  - P1-7.1: 1/1
  - P1-8.1: 0/1
  - P1-8.2: 1/3
  - P1-8.4: 1/0
  - P2-4.1: 0/4

### 1.5 Desvio de processo: limite de certames

- orquestradores/BANCO.md fixa "6 certames ou 60 itens". A sessão abriu 8 cadernos-certame (7 com itens e o STM 2025 sem item) e registrou 46 itens. O "limite de 7" da varredura não tem fonte no repositório.
- Decisão D1: os itens são aceitos, porque o limite protege o custo da sessão e não a qualidade do item. A qualidade foi conferida pelo QA (46/46).
  - A FUB 2025 e o PF Administrativo entraram pela busca dos itens 1 a 4 de TI, que D-BANCO-TI-1-4 mandou incluir na T-07.
  - Não há gasto novo a decidir nem matéria do Fundador.
  - Daqui em diante, a varredura declara o limite de BANCO.md e a fonte de qualquer outro limite.
- A excedência fica registrada na errata E3 da varredura.

### 1.6 Errata textual do relatório de varredura (D1, append)

- Aplicada por append em saida/banco/varredura_2026-10-10.md, sem reescrever o texto da produtora:
  - E1: nome do PDF de justificativas da Câmara 2012;
  - E2: alterações no CB2 de 2012 (altera o item 4 e anula 91, 92, 93, 94 e 96);
  - E3: limite.
- E1 e E2 vêm da evidência da gbq-cqe. A GBQ não baixou de novo o PDF do Grupo 1 de 2012. A cópia da produtora no scratchpad (cam12_just) é a do Grupo 2.
- Nenhum item registrado foi afetado.

### 1.7 Classificação

- AGORA: aplicadas as decisões de 1.2 a 1.6.
- PRÓXIMO: T-40 (qa-normativo) e T-42 (colunas de comando).
- PRÓXIMO datado: T-41 (VOLÁTEIS em janeiro).
- BACKLOG: nada novo. BQ-0111 apenas informa a T-19.

## 2. T-10 — Simulado 2 (P2, final; gbq-csc)

### 2.1 Conferência independente (script próprio da GBQ, sem reuso dos scripts da produtora e do QA)

- Enunciado da folha = (d) canônico dos Lotes 1, 1-C, 2 e 3: 40/40. Nos itens 17 e 22, foi preciso unir as quebras de linha depois de travessão ou hífen.
- Gabarito da grade = d-G = registro AUTORAL v3: 40/40. Mapa (id) = item da folha: 40/40.
- 40 ids únicos; 20 C/20 E.
- Por bloco: 1 = 13, 2 = 14, 3 = 7, 4 = 6, o que dá 23/23 subitens.
- Um só comando, igual ao comando canônico dos quatro lotes.
- Marcas dos 40 no registro: nenhuma VOLÁTIL ou REVERIFICAR. São 6 "normativo" e 1 "discriminação baixa (NB5)".
- Nenhum enunciado se repete nos Simulados 0, 0 v0.2 e 1.
- As seções (d) e (d-G) atuais são as que o QA conferiu. As erratas T-08 e T-28, já reconciliadas pela GCE, não tocam (d) nem (d-G).
- QA independente da gbq-cqe (simulado_2_QA_2026-10-10.md): APROVADO/CONFERIDO 40/40, 0 REPROVADO.

### 2.2 Decisões D1

- Falta dos 7 CEBRASPE_ANALOGA do Lote 3 (BQ-0002 a 0008): vale a leitura A.
  - Os 7 são PARCIAIS no banco ("aderência temática ampla"). D-ADERENCIA, decisão da Presidência, restringe item parcial a simulado diagnóstico.
  - A expressão "+ 7 ANALOGA do Lote 3" da linha T-10 é anterior e foi escrita pela própria GBQ. Diante da regra superior, essa parte da tarefa fica DESCARTADA para o simulado final.
  - Não cabe reclassificar: os 7 são LGPD geral, e a T-13 manteve o gabarito, não a aderência.
  - Os 7 continuam no Simulado 0 v0.2 (diagnóstico), e incluí-los repetiria itens.
  - Não há decisão acima de D1, porque a GBQ aplica a regra superior e não pede exceção. Por isso não se emite gatilho C nem D. O gatilho A abaixo deixa a exclusão explícita, e a Presidência pode decidir de outro modo no aceite.
- O-1, pista cruzada fraca do item 9 com os itens 16 e 13: o item é MANTIDO. A pista só funciona para quem já sabe que o 13 é C, que é o próprio conhecimento cobrado. O 16 é E no todo. Sobreposição temática desse grau é usual na prova Cebraspe. Trocar o item exigiria nova montagem e nova rodada de QA sem ganho proporcional.
- O-2, sobre o item 33 e o item 20: MANTIDO. O 33 não decide o 20.
- O-3, discriminação baixa do item 6: MANTIDO. A marca não é regra de exclusão.
- O-4 e O-5: sem efeito.
- O-6, referência ao "item 14.2.4": conferida contra os documentos de escopo da GCE (GCE_Despachos_pendentes_GCE.md, "ESCOPO (edital, item 14.2.4, Cargo 11)"; GCE_BIP_retorno_v2.md, "subitens literais do Edital (14.2.3 e 14.2.4), lidos no PDF do Projeto"). Está correta e a folha não muda.
- T-24 (Simulado 0-P2, diagnóstico): para não repetir itens, a montagem tira os 25 dos 45 itens AUTORAL elegíveis de P2 que ficaram fora do Simulado 2. O universo é 90, menos 40 selecionados, menos 5 inelegíveis.

Veredito: CONCLUÍDA. As condições de aceite de simulado final, conforme o precedente D-SIM1-CANONICO, estão cumpridas:
- QA independente APROVADO/CONFERIDO;
- Gerência reconciliou;
- as contagens batem;
- nenhum gabarito está em disputa;
- não há VOLÁTIL nem REVERIFICAR.

Emite-se o GATILHO A. A entrega à candidata (PILOT_01) continua reservada ao Fundador.

## 3. Tarefas novas (append único em TAREFAS.md)

- T-40 (PRÓXIMO): qa-normativo de BQ-0072, 0077, 0084, 0109, 0110 e 0111.
- T-41 (PRÓXIMO, datado): reverificação de janeiro de BQ-0075, 0076, 0086 e 0089.
- T-42 (PRÓXIMO): complemento da T-29, colunas de comando para BQ-0067 a BQ-0112.

## 4. Gatilhos (append único em PARA_PRESIDENCIA.md)

- GATILHO A, Simulado 2: pronto para aceite como simulado final de P2.
- Nenhum outro. A T-07 não exige aceite, porque os itens de banco chegam à Presidência pelo gatilho A do pacote (T-12/T-27, depois da T-42).

## 5. T-24 — Simulado 0-P2 (P2, diagnóstico; gbq-csc → gbq-cqe)

### 5.1 Conferência independente (script próprio da GBQ, s3/gbq_rec/s0p2chk.py; só leitura)

- Enunciado da folha = (d) canônico atual dos Lotes 1, 1-C, 2 e 3: 25/25. As seções (d) e (d-G) dos Lotes 2 e 3 não foram tocadas pelas erratas T-08 e T-28.
- Gabarito da grade = d-G = registro AUTORAL v3: 25/25. Mapa (id) = item: 25/25. 25 ids únicos. 13 C/12 E.
- Um só comando, igual ao canônico.
- Marcas: 0 VOLÁTIL e 0 REVERIFICAR; 4 "normativo", que não excluem. Nenhum item tocado por errata de consolidação (L1-Q01, Q07, Q08, Q11; L1C-Q23, Q26; L2-Q14, Q21; L3-Q20).
- Repetição: nenhum enunciado aparece nos Simulados 0, 0 v0.2, 1 e 2.
- Blocos: 1 = 7, 2 = 9, 3 = 5, 4 = 4. Subitens cobertos: 21/23, e faltam 1.2 e 1.8.
- Contagem por lote: L1 = 4 (Q02, Q06, Q12, Q15), L1-C = 3 (Q25, Q27, Q29), L2 = 9, L3 = 9.
  - O gabarito declara exatamente isso (linhas 53 e 84) e está correto.
  - A inversão "L1 3, L1C 4" estava só no resumo da ordem recebida, não no arquivo. Não há tarefa mecânica a abrir.
- QA independente da gbq-cqe (simulado_0_P2_QA_2026-10-10.md): APROVADO/CONFERIDO 25/25, 0 REPROVADO.

### 5.2 Decisões D1

- Cobertura: vale a leitura A. A D-SIM0-P2 pede os 4 blocos cobertos "em proporção ao edital", e está cumprida no limite do conjunto elegível.
  - Por script: o bloco 1 tem exatamente 7 itens elegíveis fora do Simulado 2 (L1-Q02, Q06, Q12, Q15; L1C-Q25, Q27, Q29), sem VOLÁTIL e sem errata. Os 7 foram usados.
  - O desvio é de 7/9/5/4 contra 9/9/4/3. As faltas de 1.2 e 1.8 estão registradas e motivadas.
  - A D-ADERENCIA não é afetada: são 25 itens AUTORAL, de aderência direta por construção (R4).
- Leitura B: rejeitada, nas duas variantes.
  - Repetir itens do Simulado 2 contaminaria o simulado final. O diagnóstico é feito antes, e a regra é não repetir.
  - Admitir itens com errata de consolidação exigiria texto emendado fora da literalidade do (d) canônico. Foi o mesmo critério do Simulado 2.
  - Fica em BACKLOG, sem tarefa: se a Presidência quiser ampliar o universo elegível de P2, os 9 itens com errata podem ser regravados com a errata aplicada pela GCE. O universo hoje é 90 − 5 inelegíveis − 40 do Simulado 2 − 25 do 0-P2 = 20 elegíveis, todos dos blocos 2 a 4.
- O-1, pista L1-Q06 (item 24) × L1C-Q25 (item 7), a 17 posições: MANTIDO. Retirar um dos itens reduziria o bloco 1 a 6 itens, e o simulado é diagnóstico.
- O-2, L2-Q23 (marca [V] de fonte, NÃO VOLÁTIL): MANTIDO. O único substituto no 2.6 tem errata.
- O-3: o QA do Simulado 2 continua válido sobre os arquivos atuais. Isso confirma a seção 2.1.
- Ordem de uso (informação ao Fundador, sem decisão da GBQ): por natureza, o diagnóstico 0-P2 precede o Simulado 2, que é final. Os dois não têm item em comum.

Veredito: CONCLUÍDA. As condições de aceite estão cumpridas:
- QA independente APROVADO/CONFERIDO;
- Gerência reconciliou;
- as contagens batem;
- não há VOLÁTIL;
- não há repetição.

Emite-se o GATILHO A do Simulado 0-P2 como simulado diagnóstico de P2. A entrega à candidata é reservada ao Fundador.

### 5.3 Tarefas e gatilhos

- Tarefas novas: nenhuma.
- Gatilho A do Simulado 0-P2: append único em PARA_PRESIDENCIA.md.
