# lote6_reconciliacao.md — T-04 — 2026-10-09 — gerado por gcb-gerencia

REMETENTE: GCB — Gerência de Conhecimentos Básicos (P1, TI e Dados)
DESTINATÁRIO: orquestrador (roteamento); gcb-cqfp (conferência restrita do 6b); Presidência (gatilho A do 6a em PARA_PRESIDENCIA.md)
Entrada: saida/gcb/lote6_conferencia.md (T-04, gcb-cqfp, 09/10/2026). Regras aplicadas: CLAUDE.md, DECISOES.md (D-ESCOPO / D-ESCOPO-2, D-CANONICOS, D-ADERENCIA, D-DEREP, D-REVERIFICACAO-JAN, D-COMPLEMENTOS), saida/gcb/GCB_Lotes6_especificacao_PRES-S.md, papel gcb-gerencia/gce-gerencia.

## 1. Estado de cada lote

| Lote | Arquivo | Itens | Contagens | Situação após a reconciliação |
|---|---|---|---|---|
| 6a — TI-FERRAMENTAS (itens 1 e 3) | saida/gcb/GCB_Lote6a_v2_producao_auto.md | 15 AUTORAL (6A-01 a 6A-15) | 7 C / 8 E; 8 [TS] (2 C, 6 E); 5 VOLÁTEIS (6A-01, 09, 10, 14, 15); Word 3, Excel 3, PowerPoint 2, OneDrive 2; item 3 = 5 | CONFERIDO (gcb-cqfp) e RECONCILIADO sem correção. Apontamentos R1 11/11 atendidos; fontes 5/5; itens com problema 0/15. GATILHO A emitido em PARA_PRESIDENCIA.md. Não canônico até o aceite da Presidência. |
| 6b — TI-REDES-SEGURANCA (itens 2 e 4) | saida/gcb/GCB_Lote6b_v2_producao_auto.md | 15 AUTORAL (6B-01 a 6B-15) + 2 itens reais CEBRASPE_ANALOGA fora dos 15 (TRF6 96 E, 98 C) | 7 C / 8 E; 8 [TS] (3 C, 5 E); 0 VOLÁTIL; 2 = 1, 2.1 = 4, 4.1 = 4, 4.2 = 3, 4.3 = 3 (inalteradas) | A-6b-1 APLICADO pela GCB (errata textual, seção 2). ESTADO FINAL (09/10/2026): CONFERIDO pela gcb-cqfp na Rodada 2 (lote6_conferencia.md, R2.1 a R2.4). O diff confirma exatamente as linhas 30, 205, 279, 322 e 395. Os 6 trechos conferem literalmente com o PDF oficial da F4 (pp. 25 e 40), e não restou "[sic]", "usuario" nem "copias". Gabarito, [TS] e contagem estão inalterados; itens com problema: 0/15. RECONCILIADO. GATILHO A emitido em PARA_PRESIDENCIA.md. OB-6b-1 a OB-6b-3 seguem PRÓXIMO (T-17) e R-5 segue BACKLOG (T-19). Não canônico até o aceite da Presidência. Pela GCB, T-04 está concluída. |

Gate de 30%: não se aplica (6a 0%; 6b 6,7%, já sanado na forma).

## 2. Tabela de Correções — Lote 6b (A-6b-1, errata textual de citação; sem mudança de gabarito, [TS], VOLÁTIL, contagem ou ponto de julgamento)

Base: PDF oficial da Cartilha (F4), lido pela gcb-cqfp em 09/10/2026, traz "usuário" (seção 2.3) e "cópias" (seção 4.1). O "[sic]" atribuía à fonte um erro que é da extração do PDF.

| nº | linha (arquivo 6b) | parte | antes | depois |
|---|---|---|---|---|
| CQFP-1.1 | 30 | FONTES, F4 (seção 2.3) | "...dados pessoais e financeiros de um usuario [sic]" | "...dados pessoais e financeiros de um usuário" |
| CQFP-1.2 | 30 | FONTES, F4 (seção 4.1) | "...que se propaga inserindo copias de si mesmo" | "...que se propaga inserindo cópias de si mesmo" |
| CQFP-1.3 | 205 | curso 4.1.3 | "...que se propaga inserindo copias de si mesmo [sic]" | "...que se propaga inserindo cópias de si mesmo" |
| CQFP-1.4 | 279 | curso 4.3.1 | "...dados pessoais e financeiros de um usuario [sic]" | "...dados pessoais e financeiros de um usuário" |
| CQFP-1.5 | 322 | resumo 4.1 | "(F4: \"se propaga inserindo copias de si mesmo\")" | "(F4: \"se propaga inserindo cópias de si mesmo\")" |
| CQFP-1.6 | 395 | d-G 6B-09 | "(vírus, seção 4.1: \"se propaga inserindo copias de si mesmo\")" | "(vírus, seção 4.1: \"se propaga inserindo cópias de si mesmo\")" |

Verificação após a aplicação (09/10/2026):
- diff contra a cópia anterior: exatamente 5 linhas alteradas (30, 205, 279, 322, 395); o arquivo segue com 407 linhas; nenhuma outra linha tocada.
- grep -i "usuario|copias|\[sic\]" no arquivo do 6b: 0 ocorrências.
- O trecho "a extração do PDF corrompe os acentos" (l. 30) foi mantido, por estar fora da ordem; continua verdadeiro como nota de método.
- A Tabela de Correções interna do lote NÃO recebeu a linha CQFP-1 nesta rodada, para não deslocar as 5 linhas a conferir; o registro fica aqui e vai ao lote na errata de forma (T-nova, seção 4).
- Espelho no Projeto (GCB/Lote6b_v2_producao_auto.md) ainda está na versão anterior: sincronizar só depois do "CONFERIDO" da gcb-cqfp (fora do alcance desta Gerência).

Para a gcb-cqfp: conferir só as 5 linhas acima contra o PDF oficial; com CONFERIDO, a GCB emite o gatilho A do 6b.

## 3. Decisões D1

| Objeto | Decisão | Classe |
|---|---|---|
| A-6b-1 (citação não literal da F4) | Aplicado pela GCB como errata textual (seção 2), nos termos do papel ("aplica erratas sem mudar gabarito"); dispensa ordem à EXEC. | AGORA — cumprido; falta só a conferência restrita |
| OB-6b-1 (nota interna à GCB-CQFP dentro do curso 4.0.2, l. 171, citando a Lei 14.129/2021 sem artigo) | Retirar a nota do curso e levá-la à Nota de produção; a lei só fica no curso com artigo conferido pelo qa-normativo. Não bloqueia o gatilho A (não fundamenta item), mas BLOQUEIA a exportação do 6b à plataforma até ser aplicada, porque o curso vai à candidata. | PRÓXIMO (antes de T-12 para o 6b) |
| OB-6a-2 e OB-6b-2 (grafia "Derep, antigo DETAQ" no 6a l. 111 e no 6b l. 98) | Uniformizar para "Derep (antigo DETAQ)" (D-DEREP). Sentido idêntico; não bloqueia. | PRÓXIMO (mesma errata de forma) |
| OB-6b-3 (Nota de produção (i), l. 403, sem o trojan) | Incluir o trojan na lista, alinhando com o F4 (AJ-1). Texto interno; não bloqueia. | PRÓXIMO (mesma errata de forma) |
| OB-6a-1 (os 4 itens com "pode" — 6A-03, 09, 14, 15 — são todos C) | Não reabrir itens que acabam de ser conferidos (exigiria nova rodada de QA). Fica registrado para a próxima edição do 6a ou para a montagem de simulado que use 3 ou mais desses itens (equilibrar com item E de possibilidade afirmativa de outro lote). | BACKLOG |
| OB-6a-3 (URL da F9 do 6a redireciona) | Incluir os 5 VOLÁTEIS do 6a e a URL final da F9 no roteiro FV de janeiro; condicionado ao aceite do gatilho A do 6a. | PRÓXIMO (datado: emissão em 04/01/2027) |
| TRF6 2024 itens 96 (E) e 98 (C) — "conferência visual humana do PDF" em BACKLOG | DADA POR CUMPRIDA. O risco que a motivava era a leitura mediada por ferramenta (WebFetch com paráfrase). Em 09/10 a gcb-cqfp leu o caderno oficial no CDN do Cebraspe por extração direta e literal (pdftotext -raw), com comando do bloco, ponto de julgamento e gabarito definitivo oficial (96 = E; 98 = C; anulados 58, 105, 117). Há corroboração independente: o banco da GBQ registra o texto integral dos mesmos itens (BQ-0011 e BQ-0012, gbq-cfp, 08/10/2026, mesmas URLs oficiais, mesmos gabaritos). Duas leituras literais independentes da fonte oficial cumprem a finalidade; a leitura humana não acrescenta garantia proporcional. Permanece a restrição de D-ADERENCIA: aderência parcial, só simulado diagnóstico. A menção "pendente (BACKLOG)" no texto do 6b (seção ITENS REAIS, Nota de produção (v), linha R-6 da Tabela) será atualizada na errata de forma. | DESCARTADO (pendência encerrada por cumprimento) |
| R-5 do 6b (governança digital sem item) | Mantido. Nenhum item novo sem ancoragem normativa pelo qa-normativo e sem ordem (D-COMPLEMENTOS). | BACKLOG |
| Divergência do checklist do papel gcb-cqfp ("10 [TS]", "20 itens") × especificação PRES-S (15 itens, 7–8 [TS]) | Prevalece a especificação, como fez a gcb-cqfp. Sem ação. | DESCARTADO |

Observação fora do domínio (para o orquestrador rotear à GBQ; não é gatilho): BQ-0011 e BQ-0012 estão mapeados no banco como P2-4.3 ("aderência temática ampla"); com a D-ESCOPO-2, o encaixe mais próximo passou a ser P1, TI item 4/4.1 (como no 6b). Remapeamento é decisão da GBQ.

## 4. Pendências e tarefas

- 6b: conferência restrita das 5 linhas pela gcb-cqfp CUMPRIDA (Rodada 2, CONFERIDO). Gatilho A do 6b emitido em PARA_PRESIDENCIA.md (append único).
- Sincronizar o espelho do Projeto (GCB/Lote6b_v2_producao_auto.md) com a versão de saida/gcb: liberado, porque o 6b está CONFERIDO. Cabe ao orquestrador ou ao Fundador.
- Tarefas novas acrescentadas a TAREFAS.md: T-17 (PRÓXIMO) errata de forma dos Lotes 6 (OB-6b-1, OB-6a-2, OB-6b-2, OB-6b-3, linha CQFP-1 na Tabela interna, atualização da menção ao BACKLOG 96/98); T-18 (PRÓXIMO, datado) inclusão dos VOLÁTEIS do 6a e da URL da F9 no roteiro FV de janeiro; T-19 (BACKLOG) R-5, governança digital.
- Gatilho A do 6a: escrito em PARA_PRESIDENCIA.md (append único).
