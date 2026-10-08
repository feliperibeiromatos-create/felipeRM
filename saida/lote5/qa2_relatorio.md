# qa2_relatorio.md — Lote 5 — 2026-10-08 — gerado por gcb-cqfp

Objeto: `saida/lote5/v2_producao.md` (gerado por gcb-cpp), revisado contra `saida/lote5/qa1_relatorio.md`, `edital/itens_7_8_TI_e_Dados.md`, `lotes/lote5/DESPACHO.md` e, para comparação, `saida/lote5/v1_producao.md`.
Revisor: GCB-CQFP. Rodada: QA 2. Data: 2026-10-08.
Papel: revisão. Nada foi reescrito no material; os pontos abaixo são apontamentos. As referências de linha são da v2.

---

## 1. Cobertura

Veredito: PARCIAL. Melhorou em relação à v1, mas a lacuna de 8.3 continua.

- 7.1: curso (l. 44-59), resumo (l. 139-142), pares 4 e 5, itens A5-01 a 04. Coberto.
- 8.1: curso (l. 61-72), resumo (l. 144-145), itens A5-05 a 07. Coberto.
- 8.2: os cinco tipos tratados um a um (l. 76-101), resumo (l. 147-152), pares 1 a 3, itens A5-08 a 13. Coberto. Continua sem item dedicado só ao gráfico de barras (só por contraste em A5-06 e A5-09). A v2 não acatou o ponto e justificou; a justificativa é aceita (o QA1 já o tratava como lacuna menor).
- 8.3: PARCIAL.
  - Data Studio: coberto com fonte (l. 109-114, 156, 191-195).
  - Power BI e Tableau: nenhum conteúdo substantivo (l. 107-108, 157). A conduta [SEM FONTE — não afirmar] está correta. O bloqueio foi reconfirmado por este QA (ponto 3).
  - Itens: dos 4 itens de 8.3, dois (A5-14 e A5-15) cobram o mesmo fato (Data Studio = ex-Looker Studio). A5-16 é reprovado neste QA, e A5-17 cobra um princípio de 8.1 com nomes de produto (ver ponto 4). Na prática, 8.3 tem um único conceito testado.
- 8.4: curso (l. 122-133), resumo (l. 159-160), itens A5-18 a 20. Coberto.
- Formato do despacho: títulos (a) a (d) presentes. A seção "RESPOSTA AO QA1" vem antes de (a), o que é aceitável. Os dois nomes do produto Google estão registrados, como o despacho pede (l. 109, 192-195).
- Cabeçalho: "P1, comum aos 11 cargos" (l. 3). Correto.

## 2. Correção conceitual

Veredito: CORRETO. Todas as correções do QA1 foram feitas. Restam uma imprecisão nova, de menor gravidade, e duas afirmações acessórias sem base.

Correções do QA1 conferidas:
- Histograma (l. 77, 148; A5-08): altura proporcional à frequência só com classes de mesma amplitude. Com amplitudes desiguais, a área é que é proporcional, e a altura passa a ser densidade. Correto e rigoroso.
- Box plot (l. 97-101, 152, 177-179):
  - caixa de Q1 a Q3 com os 50% centrais e AIQ = Q3 − Q1;
  - linha interna = mediana;
  - limites de Tukey em Q1 − 1,5·AIQ e Q3 + 1,5·AIQ, e o bigode vai até o dado mais extremo dentro do limite;
  - pontos fora dos limites são outliers;
  - variável quantitativa resumida, grupos dados por variável categórica;
  - o box plot não mostra bimodalidade.

  Correto. O texto declara corretamente que a regra é convenção e não lei.
- Limpeza × transformação (l. 53, 141, 186-189): as duas leituras da literatura estão registradas. A orientação "a transformação pode incluir limpeza" tende a C. Correto.
- Barras (l. 87, 168): o espaçamento aparece como convenção de desenho. O critério é a natureza da variável. Correto.

Apontamentos novos:
- N1. Bigodes por lado (l. 98): "quando há outliers, os bigodes não terminam no mínimo e no máximo da amostra; só terminam neles quando não há valores atípicos". A regra vale para cada lado separadamente. Se só há outlier superior, o bigode inferior termina no mínimo. A frase global permite uma leitura errada ("um outlier qualquer faz os dois bigodes deixarem os extremos"). É imprecisão que a banca pode explorar. Precisar "do lado em que há outlier". A formulação da l. 179 ("nem sempre vão ao mínimo e ao máximo") está correta.
- N2. Linha 120: "misturar com Excel/Office (itens 1 a 6, fora do escopo)". O arquivo de edital do repositório transcreve só os itens 7 e 8, e o conteúdo dos itens 1 a 6 não está documentado no material. Retirar ou indicar a fonte.
- N3. Linha 120: "a prova pode usar qualquer dos nomes" é especulação sobre a banca. É inócua, mas não tem base. A l. 195 ("em prova, aceitar os dois nomes como o mesmo produto") resolve melhor.
- N4. Histograma (l. 77; A5-08): "variável quantitativa" sem distinguir contínua e discreta. O material fala em "escala numérica contínua". O histograma também se aplica a variável discreta agrupada em classes. Não é erro, e o A5-08 não depende disso. Só registro.

Itens conferidos sem ressalva: dado × informação; atributo categórico/numérico; dimensão × métrica; identificador numérico não é métrica; estruturado/semiestruturado/não estruturado; razão dados/tinta; integridade gráfica; paletas; precisão perceptiva; linha × dispersão; correlação ≠ causalidade; storytelling; exploratória × explanatória.

## 3. Evidência

Veredito: APROVADO COM RESSALVA. As afirmações sobre o Data Studio estão datadas, têm URL oficial e foram conferidas por este QA. A ressalva é o A5-16, que afirma recursos de Power BI e Tableau sem fonte (ver "AFIRMAÇÕES SOBRE FERRAMENTAS").

Verificações feitas por este QA em 2026-10-08 (WebFetch):

3.1 https://cloud.google.com/blog/products/data-analytics/looker-studio-is-data-studio — ABERTA.
- Título da aba: "Looker Studio is Data Studio | Google Cloud Blog". Confere com l. 109.
- H1: "Data Studio returns as new home for Data Cloud assets". Confere.
- Data: "April 10, 2026". Confere.
- Trechos literais da l. 110 ("reintroducing a beloved and familiar name, Data Studio (formerly Looker Studio)"), da l. 111 ("We believe the new Data Studio is the ideal choice for personal data exploration — ...") e da l. 112 ("As part of this reintroduction, with Looker as our enterprise business intelligence platform, we are evolving Data Studio to complement the Looker platform, independently."): CONFEREM.
- A página também contém, e a v2 NÃO cita: "Data Studio continues to offer powerful, no-cost individual analysis and visualization, serving as the on-ramp for creating and sharing ad-hoc reports, transforming data to an interactive dashboard in minutes." e "All existing reports, data sources, assets and users will be transitioned to the new experience with no action on your part." Esses trechos dariam fonte à parte "Data Studio" do A5-16 e à segunda oração do A5-15. Não foram usados, e o QA não os incorpora (não reescreve).

3.2 https://cloud.google.com/looker-studio — ABERTA, com conteúdo truncado. Título literal: "Data Studio: Business Insights Visualizations | Google Cloud". Não foi possível ler o H1 nem o corpo. Corrobora o nome vigente "Data Studio".

3.3 https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview — BLOQUEADA. Erro literal: EGRESS_BLOCKED, "Access to learn.microsoft.com is blocked by the network egress proxy."

3.4 https://www.tableau.com/why-tableau/what-is-tableau — BLOQUEADA. Erro literal: EGRESS_BLOCKED, "Access to www.tableau.com is blocked by the network egress proxy."

3.5 https://powerbi.microsoft.com/ (domínio citado na pendência da l. 326) — BLOQUEADA. Erro literal: EGRESS_BLOCKED, "Access to powerbi.microsoft.com is blocked by the network egress proxy."

Conclusão: a declaração da v2 (l. 9, 41) de que as fontes da Microsoft e do Tableau seguem bloqueadas está CONFIRMADA. O conteúdo dessas páginas não é presumido aqui.

## 4. Itens AUTORAL

Rótulos: todos AUTORAL (l. 3, 201). Nenhum CEBRASPE_ESTILO. OK.

- A5-01 — APROVADO. Sem alteração de mérito.
- A5-02 — APROVADO. "Consiste em agregar e derivar" é E em qualquer leitura de limpeza.
- A5-03 — APROVADO.
- A5-04 — APROVADO.
- A5-05 — APROVADO.
- A5-06 — APROVADO.
- A5-07 — APROVADO.
- A5-08 — APROVADO. A nova redação condiciona a proporcionalidade à mesma amplitude, e o C fica seguro.
- A5-09 — APROVADO. Foi reformulado (a resposta da l. 33 omite isso, mas a l. 16 o declara). Agora a inversão é entre a natureza das variáveis, e não só entre o espaçamento: é troca de conceito, e o E é seguro.
- A5-10 — APROVADO.
- A5-11 — APROVADO.
- A5-12 — APROVADO. Inclui os 50% centrais e a variável quantitativa. O C é seguro.
- A5-13 — APROVADO. Tem uma única troca (média por mediana), e a caixa Q1–Q3 está correta. O E é seguro.
- A5-14 — APROVADO, com ressalva. A âncora de data e autoria foi retirada, e o C tem fonte verificada. Ressalvas: "atualmente" torna o item datado (vale na data da verificação), e o item cobre o mesmo fato do A5-15 (ver A5-15).
- A5-15 — AJUSTAR. A troca (produtos distintos × mesmo produto renomeado) é válida, e o E é correto e tem fonte. Problemas:
  - a segunda oração, "de modo que um relatório criado em um deles não pode ser identificado com o outro", é vaga ("identificado com"?) e não é redação de banca;
  - o item repete o fato do A5-14, de modo que dois dos quatro itens de 8.3 testam a mesma informação.
- A5-16 — REPROVADO. O enunciado atribui expressamente a Power BI e Tableau as capacidades de "conectar fontes de dados, construir visuais e reuni-los em painéis (dashboards) para compartilhamento". A justificativa diz que isso é feito "sem afirmar recurso de produto específico", mas o enunciado nomeia os produtos e o gabarito C depende dessa afirmação. O item contradiz o próprio material, que marca recursos de Power BI e Tableau como [SEM FONTE — não afirmar] (l. 107-108, 157). Pela regra de evidência, é afirmação sobre ferramenta sem fonte e fica REPROVADA. Para o Data Studio havia fonte disponível (3.1), que não foi citada.
- A5-17 — AJUSTAR. O gabarito E é seguro, e o item não é metaitem. Mas a "troca" não é sutil: "deixa de ser necessário observar o tipo de dado... pois a ferramenta assume essa decisão" é um absurdo evidente, não um conceito vizinho trocado. Além disso, o conteúdo medido é de 8.1/8.2; os nomes de produto são só cenário, e o item não mede conhecimento de ferramenta. Ele também traz afirmação implícita sobre os três produtos (nenhum decide pelo analista) sem fonte de fornecedor.
- A5-18 — APROVADO.
- A5-19 — APROVADO. Tem uma única troca (exploratória no lugar de explanatória), e os demais elementos são verdadeiros. O E é seguro.
- A5-20 — APROVADO.

Conferência das "10 trocas sutis de conceito único" declaradas (l. 324: 02, 04, 06, 07, 09, 11, 13, 15, 17, 19): NÃO CONFIRMADO integralmente.
- Válidas e sutis: 8 (A5-02, 04, 06, 07, 09, 11, 13, 19).
- Válida, mas o item precisa de ajuste de redação: 1 (A5-15).
- Troca não sutil (absurdo evidente): 1 (A5-17).

Equilíbrio de gabarito: 10 C (01, 03, 05, 08, 10, 12, 14, 16, 18, 20) e 10 E, conferido. Sem o A5-16, ficam 9 C e 10 E.

## 5. Estilo Cebraspe

Veredito: ADEQUADO.

- O comando "Julgue os itens a seguir." aparece uma vez (l. 201). A repetição "Julgue o item." foi removida dos 20 itens, conforme o diff com a v1.
- Cada item é afirmação única e julgável.
- Absolutos ("sempre", "nunca", "apenas", "somente", "exclusivamente"): nenhuma ocorrência nos 20 itens (busca feita no arquivo). Dois termos fortes estão justificados porque são o próprio conceito trocado: "sem relação entre si" (A5-15) e "deixa de ser necessário" (A5-17). "Comprova" (A5-11) também é o conceito trocado.
- Fora dos itens, "sempre" aparece na l. 79 ("tratar altura e área como sempre equivalentes") e na l. 179 ("nem sempre vão ao mínimo e ao máximo"). Os dois usos estão corretos.
- Redação fora do padrão de banca: segunda oração do A5-15 (ver ponto 4).

## 6. Veredito geral

APROVADO COM RESSALVAS.

7.1, 8.1, 8.2 e 8.4 estão sólidos, e todas as correções conceituais do QA1 foram feitas. Os problemas remanescentes se concentram em 8.3:
1. A5-16 afirma recursos de Power BI e Tableau sem fonte (REPROVADO).
2. A5-15 (redação e redundância com A5-14) e A5-17 (troca não sutil; não mede ferramenta): AJUSTAR.
3. Cobertura de Power BI e Tableau: continua parcial por bloqueio de rede, reconfirmado. A pendência está corretamente encaminhada à Presidência (l. 326).
4. Ajustes menores: N1 (bigodes por lado, l. 98), N2 (itens 1 a 6 do edital sem fonte, l. 120), N3 (especulação sobre a banca, l. 120).

Contagem: APROVADO 17; AJUSTAR 2 (A5-15, A5-17); REPROVADO 1 (A5-16).

PERCENTUAL_REPROVADOS: 1/20 = 5%

---

## CONFRONTO COM QA1

- QA1-1 (8.3 sem Power BI e Tableau). Resposta da v2: "acatado em parte". Status: NÃO RESOLVIDO. A conduta é aceita, mas a lacuna persiste por causa do bloqueio externo, reconfirmado em 3.3 a 3.5. Pendência na l. 326.
- QA1-1 (sem item dedicado a barras). Resposta da v2: "não acatado". Status: RESOLVIDO. A recusa é aceita: o QA1 já classificara o ponto como aceitável.
- QA1-1 (itens TRF6 2024 não usados). Resposta da v2: "acatado como registro". Status: RESOLVIDO. Não era exigência, e o motivo dado (sem texto oficial aberto) é coerente com a regra de evidência.
- QA1-1 (cabeçalho "Cargo 11"). Resposta: "acatado". Status: RESOLVIDO (l. 3).
- QA1-2.1 (histograma, altura × área). Resposta: "acatado". Status: RESOLVIDO (l. 77, 148; A5-08).
- QA1-2.2 (box plot: Tukey, bigodes, 50%, quantitativa × categórica). Resposta: "acatado integralmente". Status: RESOLVIDO (l. 97-101, 152, 177-179). Nova imprecisão menor na l. 98 (N1, bigodes por lado).
- QA1-2.3 (limpeza × transformação). Resposta: "acatado". Status: RESOLVIDO (l. 53, 141, 189).
- QA1-2.4 (barras separadas). Resposta: "acatado". Status: RESOLVIDO (l. 87, 168).
- QA1-E1 (manchete × título da aba). Resposta: "acatado". Status: RESOLVIDO (l. 109, 192). Confere com a página (3.1).
- QA1-E2 (trecho literal do Looker). Resposta: "acatado". Status: RESOLVIDO (l. 112, 194). O trecho é literal e foi conferido.
- QA1-E3 ("nasceu como Data Studio"). Resposta: "acatado". Status: RESOLVIDO. A expressão só aparece na seção de resposta (l. 19), não no curso.
- QA1-E4 (encaminhar à Presidência). Resposta: "acatado". Status: RESOLVIDO quanto ao encaminhamento (l. 326). A cobertura segue pendente (ver QA1-1).
- QA1-E5. Resposta: sem ação. Status: RESOLVIDO.
- QA1-5 ("Julgue o item." repetido). Resposta: "acatado". Status: RESOLVIDO. O diff com a v1 confirma a remoção nos 20 itens.
- QA1-A5-13 (troca dupla). Resposta: "acatado". Status: RESOLVIDO.
- QA1-A5-14 (data de post de blog). Resposta: "acatado". Status: RESOLVIDO. A âncora foi retirada. Ressalva: redundância com A5-15.
- QA1-A5-15 (âncora de data). Resposta: "acatado". Status: RESOLVIDO quanto à âncora. A nova redação gerou um novo apontamento (AJUSTAR: segunda oração vaga; redundância).
- QA1-A5-16 (metaitem sobre o edital). Resposta: "acatado"; segundo a v2, o novo item seria "conceitual... sem afirmar recurso de produto". Status: RESPOSTA NÃO ACEITA. O metaitem foi eliminado, mas o novo enunciado afirma recursos de Power BI e Tableau nomeados, sem fonte, contra o [SEM FONTE — não afirmar] do próprio material.
- QA1-A5-17 (pegadinha de leitura do edital). Resposta: "acatado". Status: RESOLVIDO quanto ao vício apontado. O novo item gerou um novo apontamento (AJUSTAR: troca não sutil; não mede ferramenta).
- QA1-A5-19 (troca dupla). Resposta: "acatado". Status: RESOLVIDO.
- QA1-6 condição 1 (refazer itens de 8.3). Resposta: "atendida". Status: NÃO RESOLVIDO. Dos 4 itens, 1 está reprovado e 2 precisam de ajuste.
- QA1-6 condições 2 a 5. Resposta: "atendidas". Status: RESOLVIDO. A condição 5 é atendida como encaminhamento.
- Declaração da v2, l. 33 ("demais 14 itens sem alteração de mérito; A5-08 e A5-12 ajustados"). Status: inexata. A5-09 também foi reescrito (declarado só na l. 16). Conferido: o novo A5-09 está correto.

---

## AFIRMAÇÕES SOBRE FERRAMENTAS

- L. 42: "Do edital sabe-se apenas que são ferramentas de visualização cobradas no item 8.3". Fonte: edital (fonte primária); data: n/a. Status: COM FONTE VERIFICADA (conferido no arquivo do edital).
- L. 106 e 155: categoria genérica "ferramenta de visualização conecta fontes, constrói visuais, painéis". Fonte: nenhuma (conceito geral, sem produto). Status: conceitual, aceitável enquanto não nomeia produto.
- L. 107: Power BI, recursos etc. "[SEM FONTE — não afirmar]". URL tentada: learn.microsoft.com/.../power-bi-overview, 2026-10-08. Status: SEM FONTE, declarado e não afirmado. Correto; bloqueio reconfirmado.
- L. 108: Tableau, idem. URL tentada: www.tableau.com/why-tableau/what-is-tableau, 2026-10-08. Status: SEM FONTE, declarado e não afirmado. Correto; bloqueio reconfirmado.
- L. 109: título da aba, manchete e data do post. Fonte: Google Cloud Blog, verificado em 2026-10-08. Status: COM FONTE VERIFICADA.
- L. 110: "Data Studio (formerly Looker Studio)". Mesma fonte e data. Status: COM FONTE VERIFICADA.
- L. 111: "personal data exploration... ad-hoc reports... BigQuery to Google Sheets and Ads". Mesma fonte e data. Status: COM FONTE VERIFICADA.
- L. 112-113: Looker é a plataforma corporativa de BI, e o Data Studio é distinto ("independently"). Mesma fonte e data. Status: COM FONTE VERIFICADA.
- L. 114: histórico de renomeação de 2022. Status: SEM FONTE, declarado e não afirmado. Correto.
- L. 120: "a prova pode usar qualquer dos nomes"; "Excel/Office (itens 1 a 6)". Sem fonte nem data. Status: SEM FONTE (N2, N3).
- L. 156: resumo, Data Studio é o nome vigente e Looker é BI corporativo. Fonte: Google Cloud Blog, 2026-10-08. Status: COM FONTE VERIFICADA.
- L. 157: Power BI e Tableau "[SEM FONTE — não afirmar]". Status: SEM FONTE, declarado. Correto.
- L. 192-194: par 6, trechos literais. Fonte: Google Cloud Blog, 2026-10-08. Status: COM FONTE VERIFICADA.
- L. 195: data de transição e domínio "[SEM FONTE]". Status: SEM FONTE, declarado. Correto (a página de fato não informa).
- A5-14: Data Studio é o nome atual do ex-Looker Studio. Fonte: Google Cloud Blog, 2026-10-08. Status: COM FONTE VERIFICADA.
- A5-15: mesmo produto renomeado. Fonte: Google Cloud Blog, 2026-10-08. Status: COM FONTE VERIFICADA quanto à identidade do produto. A oração sobre relatórios não tem trecho citado; a página tem um trecho que a sustentaria ("All existing reports... transitioned"), mas ele não está no material.
- A5-16: Power BI e Tableau "permitem conectar fontes, construir visuais, painéis, compartilhamento". Sem fonte nem data. Status: SEM FONTE. REPROVADA.
- A5-16: Data Studio, mesma capacidade. Fonte disponível em 3.1 ("creating and sharing ad-hoc reports, transforming data to an interactive dashboard"), mas não citada. Status: SEM FONTE no material.
- A5-17: implicitamente, nenhuma das três ferramentas "assume a decisão" de escolha do gráfico. Sem fonte nem data. Status: SEM FONTE (afirmação implícita). O gabarito se sustenta pelo princípio de 8.1, não pelo produto.

---

## Tabela final dos 20 itens

| Nº | Veredito | Motivo |
|---|---|---|
| A5-01 | APROVADO | Atributo × métrica correto |
| A5-02 | APROVADO | Troca limpeza/transformação válida |
| A5-03 | APROVADO | Operações de transformação corretas |
| A5-04 | APROVADO | Troca estruturado/não estruturado |
| A5-05 | APROVADO | Princípio de clareza correto |
| A5-06 | APROVADO | Eixo truncado; troca válida |
| A5-07 | APROVADO | Paleta sequencial × qualitativa |
| A5-08 | APROVADO | Condição de amplitude igual incluída |
| A5-09 | APROVADO | Inversão de natureza das variáveis |
| A5-10 | APROVADO | Gráfico de linha correto |
| A5-11 | APROVADO | Correlação ≠ causalidade |
| A5-12 | APROVADO | 50% centrais e quantitativa |
| A5-13 | APROVADO | Troca única média/mediana |
| A5-14 | APROVADO | Fonte verificada; redundante com 15 |
| A5-15 | AJUSTAR | Oração final vaga; repete A5-14 |
| A5-16 | REPROVADO | Recursos de PBI/Tableau sem fonte |
| A5-17 | AJUSTAR | Troca não sutil; não mede ferramenta |
| A5-18 | APROVADO | Definição de storytelling |
| A5-19 | APROVADO | Troca única exploratória/explanatória |
| A5-20 | APROVADO | Destaque e anotação corretos |
