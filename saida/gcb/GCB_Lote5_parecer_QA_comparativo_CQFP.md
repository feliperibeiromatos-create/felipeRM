# Lote 5 — PARECER DE QA COMPARATIVO — GCB-CQFP → GCB — 08/10/2026
Salvo nos arquivos do Projeto pela GCB em 08/10/2026. Transcrição condensada pela GCB (trechos de fonte, vereditos e números mantidos literalmente; apenas a formatação foi enxugada); o texto integral está no chat da GCB-CQFP. Para leitura pela GCB-CPP na produção da v2 única. Insumos: (A) GCB/Lote5_insumo_A_RECONCILIADO_piloto_ClaudeCode.md; (B) GCB/Lote5_insumo_B_Presidencia_v1_producao.md.

## 1. TAREFA 1 — fontes (todas verificadas em 08/10/2026)
[U1] https://learn.microsoft.com/en-gb/training/modules/get-started-with-power-bi/2-using-power-bi
[U2] https://learn.microsoft.com/en-us/training/modules/create-data-set/2-install
[U3] https://help.tableau.com/current/tableau/en-us/tableau_product_overview.htm
[U4] https://docs.cloud.google.com/data-studio/welcome
[U5] https://docs.cloud.google.com/data-studio/release-notes
[U6] https://cloud.google.com/blog/products/data-analytics/looker-studio-is-data-studio

- P1 Power BI (U1, U2): "three primary components to Power BI"; Desktop = "the development tool available to data analysts and other report creators"; serviço "allows you to organize, manage, and distribute your reports"; "The Power BI service also allows you to create high-level dashboards"; "you start with Power BI Desktop to connect to data and create the report. Then you publish the report to the Power BI service"; "available to download for free either through the Windows store or as a direct installer"; "a Microsoft Windows desktop application called Power BI Desktop"; "Transform data with Power Query Editor (comes with Power BI Desktop)". FECHADA para componentes, Windows, gratuito, fluxo Desktop→serviço, dashboards no serviço, Power Query Editor. PENDENTES: DAX, Report Server, licenças, limites, macOS (silêncio da fonte não é base para item).
- P2 Tableau (U3): Cloud "A fully hosted cloud-based enterprise-grade analytics platform"; Server "A self-hosted platform, either on-premises or in a public cloud"; "Tableau Server can have multiple sites"; Prep "combining, shaping, and cleaning data"; Mobile "interacts with visualizations on your Tableau Server or Tableau Cloud site"; Public "A free platform to explore, create, and publicly share data visualizations online". FECHADA (6 produtos). Versões e preços: PENDENTE.
- P3 A5-16 de (A): Power BI e Data Studio confirmados ("turns your data into informative, shareable, and fully customizable dashboards and reports"); Tableau "access, visualize, and analyze" confirmado, "dashboards" NÃO localizado. Reprovação mantida.
- P4 A5-17 de (A): nenhuma fonte. PENDENTE permanente; descartar item.
- P5 Renomeação de 2022: U4 "In April 2026, the Looker Studio product name returned to its original name: Data Studio". Mês/ano da renomeação para Looker Studio não localizados. PENDENTE quanto à data; afeta "out/2022" em (B) (curso, resumo, par, A5-15).
- P6 Transição 2026: U6 post de April 10, 2026, "Data Studio (formerly Looker Studio)"; U5 entrada de April 16, 2026, "We've rebranded Looker Studio as Data Studio"; U4 "https://datastudio.google.com/" e "lookerstudio.google.com will automatically redirect". FECHADA.
- P7: edital 14.2.3, TI: item 1 = MSOffice 365; itens 5 e 6 = IA e ética. "Itens 1 a 6" ERRADO → "item 1 (MSOffice 365)". "A prova pode usar qualquer dos nomes" é especulação → retirar.
- Data Studio Pro (U4 seção "Upgrade to Data Studio Pro"; U6 "Data Studio Pro is designed for scaling teams"): existência FECHADA; preço PENDENTE.
- A5-15 de (A): gabarito E se sustenta, mas redundante com A5-14. Substituir.
- Nome vigente: Data Studio (U4, U5, U6); o edital usa o nome vigente.
- Chat "QA de Ferramentas e Versões" revogado pela CQFP (DESCARTADO).

## 2. TAREFA 2 — arbitragem D1–D10
D1 RESOLVIDO: Power BI e Tableau cobertos por U1–U3. D2 8.3 de (A) não atendia; usar 8.3 de (B) ajustado. D3 A5-16 (A) REPROVADO mantido; substituir por A5-16 (B). D4 A5-15 (A) redundante; substituir por A5-15 (B) sem "em 2022". D5 A5-17 (A) DESCARTAR; substituir por A5-17 (B). D6 regra de Tukey vale por lado: corrigir curso de (A); (B) erra ao juntar "cinco números (mín…máx)" com bigodes de Tukey: corrigir também. D7 "itens 1 a 6" → "item 1". D8 retirar frase. D9 eram 8 [TS] válidas; tarefa 3 leva a 10. D10 registro sem efeito de mérito. Nenhuma divergência PENDENTE.

## 3. TAREFA 3 — conjunto de itens proposto
(A) A5-01 a A5-13 e A5-18 a A5-20 (16 itens) + (B) A5-14, A5-15, A5-16, A5-17 (4 itens). 20 itens; 10 C / 10 E; 10 [TS]; 7.1 = 4; 8.1 = 3; 8.2 = 6; 8.3 = 4; 8.4 = 3; VOLÁTIL = 4 (teto). A5-14 de (A) sai (levaria a 5 VOLÁTIL). Condição: retirar "em 2022" do A5-15 de (B).
ALERTA: em ambos os insumos, todas as [TS] têm gabarito E. Recomendação: converter 3 a 5 [TS] em itens C cuja tentação leve a marcar E (modelo: itens 1, 4, 10, 12 e 17 do Lote 4).

## 4. TAREFA 4 — veredito comparativo
| Dimensão | (A) piloto Claude Code (Sonnet + Opus, 2 rodadas) | (B) Presidência v1 (não revisada) |
|---|---|---|
| Cobertura | 7.1 enxuto (sem escalas nem tendência central); 8.3 com 1 de 4; Power BI e Tableau sem conteúdo | 7.1 amplo (escalas, média/mediana, ETL/ELT, normalização); 8.3 cobre as 3 ferramentas; 20 itens distribuídos |
| Correção | Alta após 2 rodadas; restam D6 e "itens 1 a 6" | Boa nos itens; curso com 4 falhas: cinco números × Tukey; "limpeza é etapa distinta" (absoluto); "transformação não altera a origem" (generalização); "out/2022" e "macOS" sem fonte |
| Evidência | Disciplinada mas pobre: 1 URL; 7 pendências por bloqueio de rede | 5 URLs oficiais corretas; excedeu a fonte em 3 pontos (2022, macOS, fluxo "→ Mobile") |
| Estilo | Itens limpos; A5-17 absurdo; [TS] 100% E | Itens de conceito único; [TS] 100% E; A5-15 com ano sem fonte |
Síntese: (A) ganha em precisão conceitual; (B) em cobertura e evidência de ferramentas; nenhum aprovável sozinho. v2 única: partir do curso de (A) e incorporar de (B) 7.1.1–7.1.4 (menos as 2 frases absolutas), o 8.3 (menos 2022 e macOS) e os itens da tarefa 3.

## 5. OBSERVAÇÕES PARA A v2 ÚNICA
a) (f)2 de (B): adotar a redação de (A) — classes desiguais: área ∝ frequência; altura = densidade.
b) (f)1 de (B): autores (Tukey, Tufte, Cleveland e McGill, Knaflic, Dykes) podem ficar no curso sem obra/edição; nenhum item atribui afirmação específica a autor ("segundo os estudos de percepção visual" é adequado).
c) Retirar da tabela (e) de (B) o "fluxo Desktop → serviço → Mobile": U1 encerra o fluxo no serviço; Mobile é consumo.

## 6. Classificação (CQFP)
Tarefas 1–4 concluídas; FV DESCARTADO; alerta [TS] e item 5 AGORA; P4 e P5 BACKLOG (fora de item); VOLÁTEIS aprovados: reverificar entre 04 e 08/01/2027.


## 7. ADENDO DA CQFP — 08/10/2026 (onde houver diferença, PREVALECE este adendo)
Transcrição condensada pela GCB; trechos de fonte literais.

### 7.1 FV
Chat GCB-CQFP-FV foi instalado antes da revogação e entregou a tarefa 1; entrega aceita e consolidada pela CQFP. FV passa a INATIVO (reativação proposta para reverificação dos VOLÁTEIS entre 04 e 08/01/2027 — PRÓXIMO). A revogação de 08/10 fica sem efeito.

### 7.2 Mudanças no parecer (verificado em 08/10/2026)
- P5 — FECHADA. Fonte GG4: https://cloud.google.com/blog/products/data-analytics/looker-next-evolution-business-intelligence-data-studio — post de October 11, 2022: "And starting today, Data Studio is now Looker Studio." Efeitos: RETIRADA a condição de excluir "em 2022" do A5-15 de (B) (item fica como está, gabarito E: o erro está em "descontinuada" e em "não corresponde a produto vigente"); o "out/2022" do curso, resumo e pares de (B) passa a ter fonte. Histórico: Data Studio → Looker Studio (11/10/2022) → Data Studio (abril de 2026; anúncio em 10/04, nota de versão em 16/04). Não afirmar dia exato para 2026.
- P3 — FECHADA. Fonte TB2 (Trailhead, Salesforce, aceita como fonte oficial do fornecedor): https://trailhead.salesforce.com/content/learn/modules/data-presentation-and-publication-in-tableau-desktop/build-a-dashboard — "By combining your views into an interactive dashboard…" (módulo de Tableau Desktop). Substituição do A5-16 de (A) pelo A5-16 de (B) continua recomendada (mais específico). Conjunto da tarefa 3 não muda.
- P4 — veredito inalterado: DESCARTAR A5-17 de (A).

### 7.3 Novas correções para a v2 única (AGORA)
d) Retirar do curso de (B) as pegadinhas que tomam inferência como fato (lição O12): Power BI — "dizer que o Desktop roda em macOS" e "dizer que dashboards são criados no Desktop"; Tableau — "atribuir ao Prep a função de visualização". As fontes dizem que o serviço "allows" criar dashboards e descrevem o Prep como preparação; nada indica exclusividade.
e) "Sem custo" vale para a edição Data Studio, não para a Data Studio Pro (GG1, GG3). Na tabela de pares de (B), trocar "(gratuito)" por "(edição Data Studio, sem custo; existe a edição paga Pro)". Item que diga só "o Data Studio é gratuito" é ambíguo e não pode ser usado.
f) Power BI: fonte principal = versão en-us do U1 (canônica). O U2 é de módulo do Dynamics 365 Business Central: usá-lo só para "Microsoft Windows desktop application".

### 7.4 Totais consolidados da tarefa 1
FECHADAS: P1 (parcial), P2, P3, P5, P6, P7 (com correção), 8.3, Data Studio Pro (existência). PENDENTES: P1 residual (DAX, Report Server, versão, licença, preço, limite); P4; P7 a) ("a prova pode usar qualquer dos nomes": retirar). VOLÁTIL: os 4 itens de 8.3 do conjunto — teto atingido. Nome vigente: Data Studio.

### 7.5 O que não muda
Tarefas 2, 3 e 4 como no parecer (20 itens; 10 C / 10 E; 10 [TS]; mínimos por subitem; alerta de [TS] 100% E; veredito comparativo).


## 8. ADENDO 2 DA CQFP — 08/10/2026 (prevalece sobre as seções anteriores onde houver diferença)
Transcrição condensada pela GCB; trechos de fonte literais.
- P4 — FECHADA, com achado contrário à premissa do A5-17 de (A). Fonte (verificado em 08/10/2026): https://docs.cloud.google.com/data-studio/conversational-analytics-code-interpreter — título "Enable and use the Code Interpreter | Data Studio"; o Code Interpreter "translates natural language questions into Python code to provide advanced analysis and visualizations". Recurso da assinatura Data Studio Pro, em Preview (pré-GA).
- Efeito a): descarte do A5-17 de (A) mantido, com fundamento adicional (risco de recurso contra o gabarito E).
- Efeito b) — correção 5g (AGORA): no 8.3 do curso de (A), reescrever a pegadinha "supor que a ferramenta escolhe o gráfico certo no lugar do analista" como responsabilidade, não como incapacidade da ferramenta. Exemplo: "a ferramenta pode sugerir ou gerar visuais, mas a adequação do gráfico ao dado e à pergunta continua sendo responsabilidade do analista". Nenhum item pode afirmar que as ferramentas não geram ou não sugerem visualizações.
- Efeito c): o recurso (Preview, só edição Pro) não vira conteúdo de item — seria VOLÁTIL e o teto de 4 está atingido.
- Pendentes após o adendo 2: P1 residual (DAX, Report Server, versão, licença, preço, limite); P7 a) (retirar a frase).
FIM DO PARECER (com adendos 1 e 2)
