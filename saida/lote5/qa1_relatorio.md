# qa1_relatorio.md — Lote 5 — 2026-10-08 — gerado por gcb-cqfp

Objeto: `saida/lote5/v1_producao.md` (gerado por gcb-cpp), revisado contra `edital/itens_7_8_TI_e_Dados.md` e `lotes/lote5/DESPACHO.md`.
Revisor: GCB-CQFP. Rodada: QA 1. Data: 2026-10-08.
Papel: revisão. Nada foi reescrito no material; as correções abaixo são apontamentos para o produtor.

---

## 1. Cobertura

Veredito: PARCIAL (lacuna material em 8.3).

- 7.1 (conceitos, atributos, métricas, transformação): curso, resumo e 4 itens AUTORAL. Coberto.
- 8.1 (princípios): curso, resumo e 3 itens. Coberto.
- 8.2 (histograma, linha, barra, dispersão, box plot): os cinco tipos tratados um a um no curso e no resumo; itens para histograma (08, 09), linha (10), dispersão (11) e box plot (12, 13). Lacuna menor: nenhum item é dedicado ao gráfico de barras isoladamente (só aparece por contraste em A5-06 e A5-09). Aceitável, mas registrar.
- 8.3 (Power BI, Tableau e Data Studio): LACUNA. Sobre Power BI e Tableau não há nenhum conteúdo substantivo, porque as fontes oficiais estão bloqueadas na rede (confirmado por este QA, ver ponto 3). A conduta de marcar [SEM FONTE — não afirmar] está correta segundo CLAUDE.md, mas o resultado é que 2 das 3 ferramentas do edital ficam sem curso e sem item. Além disso, os 4 itens de 8.3 não sobrevivem a este QA (A5-14, A5-16 e A5-17 reprovados; A5-15 ajustar). Na prática, 8.3 está sem itens utilizáveis.
- 8.4 (storytelling): curso, resumo e 3 itens. Coberto.
- Formato do despacho: títulos (a) a (d) presentes. Os itens análogos citados no despacho (TRF6 2024, itens 63 e 81) não foram usados no material; não é exigência expressa, apenas registro.
- Cabeçalho (linha 3): "Cargo 11, P1" está impreciso. O edital diz que a P1 é comum aos 11 cargos; não se trata do "Cargo 11".

## 2. Correção conceitual

Veredito: CORRETO NO GERAL, com 4 imprecisões que a banca pode explorar.

2.1 Histograma (curso 8.2, linha 47): "a altura (ou área) representa a frequência". Simplificação. Rigor: com classes de mesma amplitude, a altura é proporcional à frequência; com amplitudes desiguais, é a ÁREA que é proporcional à frequência, e a altura representa a densidade de frequência. O "ou" deixa as duas coisas como equivalentes, o que não são. Explicitar a condição.

2.2 Box plot (curso 8.2, linha 67; resumo, linha 119; par 3): falta a regra que a banca cobra.
- Não aparece a regra usual de Tukey: limites em Q1 − 1,5·AIQ e Q3 + 1,5·AIQ (AIQ = Q3 − Q1). Os bigodes vão até o dado mais extremo dentro desses limites, e os pontos fora deles são marcados como outliers. O texto diz só "segundo a convenção adotada", o que é vago demais para a prova.
- Contradição latente: o curso apresenta "cinco números: mínimo, Q1, mediana, Q3, máximo" e, na mesma frase, admite outliers isolados. Quando há outliers, os bigodes NÃO terminam no mínimo e no máximo. O curso precisa dizer isso.
- Falta dizer expressamente que a caixa contém os 50% centrais dos dados. É o dado mais cobrado e só aparece de forma implícita em "intervalo interquartil".
- Tipo de variável: o box plot resume uma variável quantitativa; os "grupos" comparados são categorias de uma variável categórica. O texto diz "comparar grupos", mas não faz a distinção quantitativa × categórica. Explicitar.

2.3 Limpeza × transformação (curso 7.1, linha 23; par 5): "conceitualmente distinta da transformação" é afirmação forte demais. Em boa parte da literatura de ETL e de preparação de dados, a limpeza (cleansing) é tratada como uma das operações da etapa de transformação (o "T" de ETL). Um item do tipo "a transformação de dados pode incluir a limpeza" seria provavelmente C. O par 5 já diz que "as etapas se misturam", mas o curso e o resumo vendem a separação como regra. Ajustar o curso para não induzir o candidato a marcar E nesse item. O A5-02 continua correto (ver ponto 4), porque "limpeza consiste em agregar e derivar" é errado em qualquer leitura.

2.4 Gráfico de barras (linha 57): "barras separadas" é convenção de desenho, não requisito conceitual. Não é erro, mas não deve virar critério de gabarito isolado. "Base em zero" está correto.

Itens conferidos sem ressalva: dado × informação; atributo categórico/numérico; dimensão × métrica; coluna numérica não é automaticamente métrica; estruturado/semiestruturado/não estruturado; razão dados/tinta; integridade gráfica; paletas qualitativa/sequencial/divergente; precisão perceptiva de posição/comprimento sobre área/ângulo (Cleveland e McGill); linha × dispersão; dispersão com duas quantitativas e correlação ≠ causalidade; box plot não mostra bimodalidade; mediana (não média) na caixa; storytelling, exploratória × explanatória.

## 3. Evidência

Veredito: APROVADO COM CORREÇÕES. A afirmação central (o nome voltou a ser Data Studio) está CONFIRMADA na fonte. Há duas imprecisões de citação e uma lacuna que já pode ser fechada.

Verificações feitas por este QA em 2026-10-08 (WebFetch):

3.1 https://cloud.google.com/blog/products/data-analytics/looker-studio-is-data-studio — ABERTA.
- Título da aba (HTML title): "Looker Studio is Data Studio | Google Cloud Blog".
- Manchete do post (H1): "Data Studio returns as new home for Data Cloud assets".
- Data: "April 10, 2026". Autores: Sean Zinsmeister (Director of Product Management, Data Cloud) e Jennifer Skene (Product Manager).
- Trecho literal confirmado: "reintroducing a beloved and familiar name, Data Studio (formerly Looker Studio)".
- Trecho literal confirmado: "We believe the new Data Studio is the ideal choice for personal data exploration — a place to craft ad-hoc reports, and quickly visualize data across Google's ecosystem, from BigQuery to Google Sheets and Ads."
- Trecho literal sobre o Looker (resolve o [SEM FONTE] da linha 161): "As part of this reintroduction, with Looker as our enterprise business intelligence platform, we are evolving Data Studio to complement the Looker platform, independently."
- A página NÃO informa data efetiva de transição nem novo domínio. Diz: "All existing reports, data sources, assets and users will be transitioned to the new experience with no action on your part." O link "Data Studio" do post aponta para https://cloud.google.com/looker-studio.
- Conclusão: a afirmação do v1 de que o produto voltou a se chamar Data Studio em 2026 (antes Looker Studio) está correta e tem fonte oficial datada.

3.2 https://cloud.google.com/looker-studio (link oficial do produto citado no post; não consta do v1) — ABERTA.
- Título literal: "Data Studio: Business Insights Visualizations | Google Cloud". O conteúdo retornado estava truncado e não foi possível ler o H1. Corrobora o nome vigente "Data Studio" em 2026-10-08.
- Observação: o resumo automático da ferramenta acrescentou, por conta própria, que o Google teria renomeado o produto para Looker Studio em 2022. Isso NÃO está na página e NÃO foi usado como evidência. O histórico de 2022 continua [SEM FONTE oficial aberta].

3.3 https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview — BLOQUEADA. Erro literal: EGRESS_BLOCKED, "Access to learn.microsoft.com is blocked by the network egress proxy."

3.4 https://www.tableau.com/why-tableau/what-is-tableau — BLOQUEADA. Erro literal: EGRESS_BLOCKED, "Access to www.tableau.com is blocked by the network egress proxy."

3.5 https://help.tableau.com/current/pro/desktop/en-us/what_is_tableau.htm — BLOQUEADA. Erro literal: EGRESS_BLOCKED, "Access to help.tableau.com is blocked by the network egress proxy."

Conclusão: o registro de bloqueio que o v1 faz para Microsoft e Tableau está confirmado. O conteúdo dessas páginas não é presumido aqui.

Apontamentos de evidência:
- E1. Título do post: o v1 chama a fonte de post "Looker Studio is Data Studio". Esse é o título da aba e o slug da URL; a manchete do post é "Data Studio returns as new home for Data Cloud assets". Citar a manchete, ou as duas, e indicar qual é qual (linhas 78, 159, 252).
- E2. Linha 161: o [SEM FONTE] sobre o Looker pode ser substituído pelo trecho literal do item 3.1. A paráfrase "Looker remains the enterprise BI platform" NÃO é literal e não deve ser usada entre aspas.
- E3. Linha 80: "o produto nasceu como Data Studio" é inferência. O post diz "beloved and familiar name", o que indica uso anterior do nome, mas não afirma que foi o nome original. Marcar como inferência ou retirar.
- E4. Power BI e Tableau: a conduta [SEM FONTE — não afirmar] está correta. A cobertura de 8.3 só fecha com fonte oficial acessível por outra via (liberação de rede, conector autorizado ou material oficial anexado ao repositório). Encaminhar à Presidência.
- E5. A regra do checklist ("toda afirmação sobre ferramenta tem verificado em [data] e URL oficial") está cumprida nas afirmações sobre Data Studio. As afirmações sobre Power BI e Tableau se limitam ao texto do edital, que é a fonte primária adequada.

## 4. Itens AUTORAL

Rótulos: todos AUTORAL. Nenhum CEBRASPE_ESTILO. OK.

- A5-01 — APROVADO. Atributo × métrica correto; gabarito C seguro.
- A5-02 — APROVADO. Troca limpeza/transformação; "consiste em agregar e derivar" é E em qualquer leitura. Ver 2.3 para o curso.
- A5-03 — APROVADO. C seguro.
- A5-04 — APROVADO. Troca estruturado/não estruturado; E seguro.
- A5-05 — APROVADO. C seguro.
- A5-06 — APROVADO. Troca recomendada/desaconselhada; E seguro.
- A5-07 — APROVADO. Troca qualitativa/sequencial; E seguro.
- A5-08 — APROVADO. C seguro. Ver 2.1 para o curso.
- A5-09 — APROVADO. Inversão contíguas/separadas; é troca de conceito, não de leitura.
- A5-10 — APROVADO. C seguro.
- A5-11 — APROVADO. Correlação × causalidade; E seguro.
- A5-12 — APROVADO. C defensável. "Extremos" é aceitável porque o item menciona os outliers à parte; o curso deve explicar a regra de 1,5·AIQ (ver 2.2).
- A5-13 — AJUSTAR. Duas trocas no mesmo item (média por mediana e caixa como mínimo–máximo). Foge do padrão do despacho ("um único conceito trocado"); o candidato acerta por qualquer das duas. Manter uma troca só.
- A5-14 — REPROVADO. Enunciado que a banca não escreveria: cobra a data e a autoria de um post de blog ("comunicado do Google Cloud datado de 10 de abril de 2026"). Isso é memorização de notícia e extrapola o "ferramentas de visualização" do edital. O conteúdo (Data Studio = ex-Looker Studio) é válido, mas sem a âncora de data e fonte.
- A5-15 — AJUSTAR. A troca (produto distinto × mesmo produto renomeado) é válida e o gabarito E está correto. Retirar a âncora "reintroduzido pelo Google Cloud em abril de 2026", pelo mesmo motivo do A5-14.
- A5-16 — REPROVADO. Metaitem sobre o conteúdo do próprio edital ("listadas no edital"). A banca não escreve item sobre o edital; não mede conhecimento de ferramenta.
- A5-17 — REPROVADO. Metaitem sobre o edital e pegadinha de leitura e memorização (qual nome aparece no item 8.3), não troca de conceito. Além disso, a frase "Excel não é ferramenta de visualização" seria discutível se o item fosse reformulado sem a referência ao edital.
- A5-18 — APROVADO. C seguro.
- A5-19 — AJUSTAR. Duas trocas sobrepostas ("apresentar todos os dados" e "explanatória" no lugar de "exploratória"). Mesmo problema do A5-13. Manter uma só.
- A5-20 — APROVADO. C seguro.

Conferência das "10 trocas sutis" declaradas (02, 04, 06, 07, 09, 11, 13, 15, 17, 19): NÃO CONFIRMADO.
- Válidas como estão: 6 (A5-02, 04, 06, 07, 09, 11).
- Precisam de ajuste: 3 (A5-13 e A5-19 por troca dupla; A5-15 pela âncora de data).
- Inválida: 1 (A5-17, pegadinha de leitura do edital).

Equilíbrio de gabarito: 10 C e 10 E declarados, conferido. Após o QA, restam 17 itens aproveitáveis (com ajuste): 8 C e 9 E.

## 5. Estilo Cebraspe

Veredito: ADEQUADO, com ressalvas.

- Cada item é afirmação única e julgável. OK.
- O material repete "Julgue o item." dentro de cada item, além do comando geral "Julgue os itens a seguir". A Cebraspe usa o comando uma vez, antes do bloco, e depois só a afirmação. Retirar a repetição (forma, não mérito).
- Absolutos ("sempre", "nunca", "apenas"): nenhuma ocorrência nos 20 itens. "Comprova" (A5-11) é termo forte, mas é justamente o conceito trocado; justificado.
- Fora dos itens, o curso traz absolutos aceitáveis ("barras devem partir de zero"). Ressalva: "conceitualmente distinta" (7.1) e "barras separadas" (barras) estão fortes demais; ver 2.3 e 2.4.
- A5-14, A5-16 e A5-17 não têm estilo de banca (data de blog; referência ao edital).

## 6. Veredito geral

APROVADO COM RESSALVAS.

Condições para a rodada 2:
1. Refazer os itens de 8.3: substituir A5-14, A5-16 e A5-17 e ajustar A5-15, sem âncora de data de blog e sem referência ao edital.
2. Ajustar A5-13 e A5-19 para uma única troca de conceito cada.
3. Corrigir o curso: histograma (altura × área, 2.1); box plot (regra de 1,5·AIQ, bigodes × mínimo/máximo, 50% centrais, quantitativa × categórica, 2.2); limpeza × transformação (2.3).
4. Corrigir as citações: manchete × título da aba do post (E1); trecho literal do Looker (E2); inferência "nasceu como Data Studio" (E3); "Cargo 11" no cabeçalho.
5. Power BI e Tableau: encaminhar à Presidência a necessidade de acesso a fonte oficial. Sem isso, 8.3 permanece com cobertura parcial declarada.

Os subitens 7.1, 8.1, 8.2 e 8.4 estão sólidos. O problema está concentrado em 8.3 e em duas trocas duplas.

PERCENTUAL_REPROVADOS: 3/20 = 15%

Contagem: APROVADO 14; AJUSTAR 3; REPROVADO 3.

---

## Tabela final dos 20 itens

| Nº | Veredito | Motivo |
|---|---|---|
| A5-01 | APROVADO | Atributo × métrica correto |
| A5-02 | APROVADO | Troca limpeza/transformação válida |
| A5-03 | APROVADO | Operações de transformação corretas |
| A5-04 | APROVADO | Troca estruturado/não estruturado válida |
| A5-05 | APROVADO | Princípio de clareza correto |
| A5-06 | APROVADO | Eixo truncado em barras; troca válida |
| A5-07 | APROVADO | Paleta sequencial × qualitativa; troca válida |
| A5-08 | APROVADO | Definição de histograma correta |
| A5-09 | APROVADO | Inversão contíguas/separadas válida |
| A5-10 | APROVADO | Gráfico de linha correto |
| A5-11 | APROVADO | Correlação ≠ causalidade |
| A5-12 | APROVADO | Box plot correto; curso deve ter 1,5·AIQ |
| A5-13 | AJUSTAR | Duas trocas no mesmo item |
| A5-14 | REPROVADO | Cobra data de post de blog; não é Cebraspe |
| A5-15 | AJUSTAR | Troca válida; retirar âncora de data |
| A5-16 | REPROVADO | Metaitem sobre o edital |
| A5-17 | REPROVADO | Pegadinha de leitura do edital |
| A5-18 | APROVADO | Definição de storytelling correta |
| A5-19 | AJUSTAR | Duas trocas sobrepostas |
| A5-20 | APROVADO | Destaque e anotação corretos |
