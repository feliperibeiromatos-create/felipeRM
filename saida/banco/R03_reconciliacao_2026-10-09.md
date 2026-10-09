# R03_reconciliacao_2026-10-09.md — R-03 — 2026-10-09 — gerado por gbq-gerencia

- Entrada: saida/banco/qualidade_2026-10-09_R03.md (gbq-cqe): BQ-0047 a BQ-0066, 20 APROVADOS, 0 CORRIGIR, 0 REPROVADOS, 0 não verificáveis (0% reprovados, abaixo do gate de 30%).
- Regras aplicadas: D-RECUPERACAO, D-QA-PENDENTE, D-ADERENCIA, D-ROTULOS, regras/proveniencia.md, banco/SCHEMA.md.
- Nenhum gabarito, rótulo, texto_integral, item_edital_camara ou URL foi alterado. Só a coluna observacoes mudou, em 20 linhas.
- Critério de aderência (o mesmo do QA): DIRETA = o item cobra o que o subitem do edital nomeia; PARCIAL = tema vizinho ou genérico, ou ferramenta/norma não nomeada. PARCIAL = só simulado diagnóstico (D-ADERENCIA).

## Decisões D1
| item | decisão | motivo |
|---|---|---|
| BQ-0047 a BQ-0066 | Reconciliados como APROVADOS; prefixo "QA PENDENTE; " retirado | Veredito APROVADO da gbq-cqe nos 20, com texto literal e gabarito definitivo conferidos no CDN Cebraspe. |
| BQ-0049 | DIRETA, P1-5.2 (sem mudança de subitem). "aderência moderada" passa a "aderência DIRETA" | Escolher entre classificação e regressão diante de exemplos históricos rotulados é o núcleo do aprendizado supervisionado que o 5.2 nomeia. Coerente com BQ-0050 e 0051, do mesmo comando. |
| BQ-0052 | DIRETA, P1-8.2 (sem mudança de subitem). Fica resolvida a nota "8.1/8.2" | "Barra" está nomeado no 8.2. Julgar a adequação de um tipo de gráfico à finalidade é a forma típica de cobrar tipos de gráficos. A leitura 8.1 fica registrada. |
| BQ-0053 | DIRETA, P1-8.2 (sem mudança de subitem) | A regra 1,5×IQR é a convenção de outlier do box plot, que o 8.2 nomeia. O tratamento de outlier (7.1) é secundário e fica registrado como leitura alternativa. |
| BQ-0055 | PARCIAL, P1-7.1 (sem mudança de subitem). "aderência moderada" passa a "aderência PARCIAL". Só diagnóstico | O item cobra atributos de gestão de desempenho (faixas codificadas, prazos de meta, benchmarks), que ficam além de "conceitos, atributos, métricas" de dados. BQ-0054 (medida × métrica) segue DIRETA. |
| BQ-0059 | DIRETA, P1-5.1 (sem mudança de subitem) | O prompt é o objeto que o subitem "engenharia de prompts" nomeia. A definição de prompt é o item elementar desse subitem. Este é o único item do banco em P1-5.1. |
| BQ-0056, BQ-0057 | PARCIAL, P2-4.1 (sem mudança; o banco já diz "aderência temática ampla") | Sem divergência: é LGPD geral, não LGPD em sistemas de transcrição e IA. É coerente com BQ-0002 a 0008. |
| BQ-0060, BQ-0062, BQ-0063 | Acolhida a sugestão da gbq-cqe: o gabarito preliminar e a justificativa de anulação vão para observacoes | O precedente é BQ-0025 (preliminar registrado em observacoes). A fonte oficial está localizada (ANM_24_Justificativas_de_alterações_de_gabarito.pdf, CDN Cebraspe, Cargo 24). anulado e gabarito X não mudam. |
| Anulados (BQ-0029, 0030, 0031, 0060, 0062, 0063) | Não entram em nenhum simulado, nem no diagnóstico. Ficam no banco como registro de proveniência | Sem gabarito válido, o item não se pontua em +1/−1/0 (edital 8.11.2). A decisão vale para a R-04 e seguintes. |
| BQ-0064 | Recebe a marca VOLÁTIL. Fica inapto a simulado final até a reverificação de 4–8/1/2027 (T-14). Pode ir ao diagnóstico | A afirmação positiva sobre a arquitetura de duas plataformas comerciais nomeadas (ChatGPT, DeepSeek) depende de produto e não foi verificada em fonte do fornecedor. |
| BQ-0048 | Não recebe a marca VOLÁTIL | O gabarito E depende de uma negativa absoluta ("não possuem funcionalidades para análise de dados ou integração com bancos de dados"). Ela é falsa enquanto Tableau e Power BI forem ferramentas de BI, pois essas funções definem a categoria. Nenhuma mudança de versão pode inverter o gabarito. |
| BQ-0056, BQ-0057 → qa-normativo | Vira a tarefa T-13 (não executada agora). Por D1, a T-13 inclui os demais itens LGPD que o QA de 09/10 já levou ao qa-normativo: BQ-0002 a 0008, 0023, 0024, 0025, 0031, 0032, 0037, 0045, 0046 (17 itens no total) | A Lei 15.352/2026 alterou a LGPD (regras/proveniencia.md). Uma tarefa única, com a mesma norma e o mesmo revisor, evita duplicar. BQ-0036 (Marco Civil) fica para a T-03. Não há bloqueio adicional: todos são PARCIAIS e, por isso, já ficam fora de simulado final. |

## Alterações feitas em banco/banco.csv (campo observacoes; antes → depois)
Formato preservado: separador ";", aspas mínimas, LF, 15 colunas, 67 linhas. Colunas 1–14 conferidas como idênticas por comparação.
| ID | campo | antes → depois |
|---|---|---|
| BQ-0047, 0048, 0050, 0051, 0054, 0056, 0057, 0058, 0061, 0065, 0066 | observacoes | "QA PENDENTE; …" → "…" (só a retirada do prefixo) |
| BQ-0049 | observacoes | "QA PENDENTE; aderência moderada (supervisionado: classificação x regressão); …" → "aderência DIRETA P1-5.2, D1 GBQ R-03 (supervisionado: classificação x regressão); …" |
| BQ-0052 | observacoes | "QA PENDENTE; gráfico de barras empilhado em dashboard (8.1/8.2); …" → "gráfico de barras empilhado em dashboard; aderência DIRETA P1-8.2, D1 GBQ R-03 (leitura alternativa 8.1 registrada); …" |
| BQ-0053 | observacoes | "QA PENDENTE; box plot; …" → "box plot; aderência DIRETA P1-8.2, D1 GBQ R-03 (leitura alternativa P1-7.1 registrada); …" |
| BQ-0055 | observacoes | "QA PENDENTE; KPIs/métricas; aderência moderada; …" → "KPIs/métricas; aderência PARCIAL, D1 GBQ R-03 (só simulado diagnóstico, D-ADERENCIA); …" |
| BQ-0059 | observacoes | "QA PENDENTE; engenharia de prompts (definição de prompt); …" → "engenharia de prompts (definição de prompt); aderência DIRETA P1-5.1, D1 GBQ R-03; …" |
| BQ-0060 | observacoes | prefixo retirado e acréscimo ao final: "; gabarito preliminar C anulado no definitivo; justificativa Cebraspe: o item possibilita mais de uma interpretação (ANM_24_Justificativas_de_alterações_de_gabarito.pdf)" |
| BQ-0062 | observacoes | prefixo retirado e acréscimo ao final: "; gabarito preliminar E anulado no definitivo; justificativa Cebraspe: o item possibilita mais de uma interpretação (ANM_24_Justificativas_de_alterações_de_gabarito.pdf)" |
| BQ-0063 | observacoes | prefixo retirado e acréscimo ao final: "; gabarito preliminar C anulado no definitivo; justificativa Cebraspe: o item possibilita mais de uma interpretação (ANM_24_Justificativas_de_alterações_de_gabarito.pdf)" |
| BQ-0064 | observacoes | "QA PENDENTE; IA generativa/LLM/transformer; …" → "VOLÁTIL (dependência de produto: ChatGPT/DeepSeek; reverificação 4–8/1/2027, T-14; inapto a simulado final até lá); IA generativa/LLM/transformer; …" |

## Contagem final do banco (após a R-03)
- Total: 66 itens (BQ-0001 a BQ-0066), todos CEBRASPE_ANALOGA. P1: 44; P2: 22.
- Sem "QA PENDENTE": 66 de 66.
- Anulados (gabarito X): 6 (BQ-0029, 0030, 0031, 0060, 0062, 0063).
- Gabarito válido: 60, sendo C = 33 e E = 27.
- VOLÁTIL: 1 (BQ-0064).
- Pendências fora da R-03: T-03 (arbitragem das 7 aderências do QA de 09/10 e tipologia v1.1); T-13 (qa-normativo LGPD, 17 itens); T-14 (reverificação de BQ-0064 em janeiro).

## Estado da R-03
CONCLUÍDA e reconciliada em 2026-10-09. A R-04 (Simulado 0 v0.2, diagnóstico) está desbloqueada quanto ao QA: 66 itens sem QA PENDENTE, menos os 6 anulados, que ficam excluídos.
Gatilhos para a Presidência: nenhum. A R-03 é QA interno do banco, sem mudança de gabarito, rótulo ou escopo, sem matéria do Fundador e sem conflito.
