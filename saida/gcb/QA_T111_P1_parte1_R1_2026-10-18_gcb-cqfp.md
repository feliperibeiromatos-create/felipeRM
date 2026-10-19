# QA_T111_P1_parte1_R1_2026-10-18_gcb-cqfp.md — T-111 (A1), QA R1 do resumo do tópico P1-8.2 — 2026-10-18 — gerado por gcb-cqfp

Objeto: saida/gcb/T111_resumos_P1_parte1_v1.md (gcb-cpp). Normas: saida/gcb/V15_BAEF_D1_GCB_2026-10-18.md (seção 0, regras 1, 2 e 7; seção 3, regra de tamanho, forma e QA da A); ordens/ORDEM_V15_A_RESUMOS.md (e). Base: saida/pacote/pacote.json v1.11, lote L5, bloco "ITEM 8.2 — TIPOS DE GRÁFICOS" (L5#2), lido por script próprio (`python -I`); o arquivo é idêntico byte a byte a saida/pacote/gerador_v1_11/out/pacote.json (cmp). Somente leitura; nada alterado fora deste arquivo.

## 1. Veredito

**P1-8.2: CORRIGIR** (um único ajuste de forma, regra "um parágrafo por ideia"; texto exato na seção 4). Conteúdo, fidelidade, tamanho, cobertura e varredura aprovados. Reprovados: 0 de 1 tópico (0%). R2 só neste ajuste.

## 2. Conferência por critério (leitura própria)

| Critério | Resultado | Observação |
|---|---|---|
| Sem fato novo (rastreio frase a frase, 11 frases) | APROVADO | Cada frase localizada no curso L5#2; conferi as 11 linhas da tabela de rastreio contra o texto do curso. Nenhuma afirmação fora do bloco; nenhum exemplo novo. |
| Sentido fiel / correção conceitual | APROVADO | Histograma: classes adjacentes, barras contíguas, ordem fixa, área proporcional à frequência com amplitudes desiguais e altura como densidade (curso: "densidade de frequência") — correto. Barras × histograma pela natureza da variável, espaçamento como convenção — fiel. Dispersão: correlação não prova causalidade — fiel. Box plot: caixa Q1–Q3, 50% centrais, AIQ = Q3 − Q1, mediana e não média, limites Q1 − 1,5·AIQ e Q3 + 1,5·AIQ, bigode até o dado mais extremo do seu lado dentro do limite, pontos além = outliers — correto e fiel. "Que pode variar entre programas" condensa "adotada como convenção por muitos programas, mas que pode variar"; aceitável, sem distorção. |
| Cobertura e pegadinha central | APROVADO | Pegadinha central (histograma tratado como barras de categorias) nos §1–2; ordem das classes, altura × área, linha central = média, caixa mínimo–máximo e bigodes por lado também cobertos; "eixo truncado" coberto por "base em zero". |
| Tamanho | APROVADO | Recontado: 217 palavras (80–220); curso sem título 694 palavras → 31,3% (≤ 40%); 5 parágrafos com 52, 45, 38, 36, 46 palavras (≤ 60). Após o ajuste: 6 parágrafos (≤ 6) com 52, 45, 17, 21, 36, 46; total inalterado. |
| Forma | APROVADO | Prosa corrida; sem lista, tabela, negrito; nenhuma linha inicia por número de item ou rótulo em maiúsculas com dois-pontos; sem fonte ou data (o resumo não repete fato datado). |
| Um parágrafo por ideia | CORRIGIR | O §3 junta duas ideias distintas (gráfico de linha; gráfico de dispersão), sem frase de contraste entre elas, enquanto o box plot foi corretamente dividido em dois parágrafos (caixa; bigodes). Ver seção 4. |
| Sem referência de produção (varredura 0.7) | APROVADO | Repeti a regex das 10 categorias da ordem C sobre o texto do bloco json: zero ocorrências. Nenhuma exceção da regra 3 aplicável. |
| Forma do arquivo (D1, 0.8) | APROVADO | Cabeçalho, seções pedidas e um único bloco json `{"P1-8.2":{"resumo":"…"}}`, sem outro campo. |
| Checklist da coordenação: URLs, normativo, itens AUTORAL, estilo Cebraspe | NÃO SE APLICA | O resumo não cita URL nem fonte datada, nem lei; a parte não tem itens. |

## 3. Tabela de pareceres

| Tópico | Bloco | Palavras | % do curso | Parágrafos | Parecer |
|---|---|---|---|---|---|
| P1-8.2 | L5#2 | 217 | 31,3% | 5 (6 após ajuste) | CORRIGIR |

Percentual de reprovados: 0% (0/1). Percentual com ajuste: 100% (1/1).

## 4. Correção exigida (texto exato, para o _v2)

Substituir o 3º parágrafo

> O gráfico de linha mostra a evolução de uma variável em um eixo ordenado, tipicamente o tempo. O gráfico de dispersão mostra a relação entre duas variáveis quantitativas, cada ponto sendo uma observação; correlação visível não prova causalidade.

por dois parágrafos, separados por linha em branco (no json, `\n\n` entre eles), sem alterar nenhuma palavra:

> O gráfico de linha mostra a evolução de uma variável em um eixo ordenado, tipicamente o tempo.
>
> O gráfico de dispersão mostra a relação entre duas variáveis quantitativas, cada ponto sendo uma observação; correlação visível não prova causalidade.

No json, o trecho passa a ser: `…convenção de desenho.\n\nO gráfico de linha mostra a evolução de uma variável em um eixo ordenado, tipicamente o tempo.\n\nO gráfico de dispersão mostra a relação entre duas variáveis quantitativas, cada ponto sendo uma observação; correlação visível não prova causalidade.\n\nNo box plot, …`. Atualizar a seção 3 do arquivo (6 parágrafos; 52, 45, 17, 21, 36, 46 palavras) e a numeração do rastreio (3.1 → §3; 3.2–3.3 → §4; seguintes renumerados). Nenhuma outra mudança.

## 5. Encaminhamento

gcb-cpp grava saida/gcb/T111_resumos_P1_parte1_v2.md só com o ajuste da seção 4; a R2 (saida/gcb/QA_T111_P1_parte1_R2_2026-10-18_gcb-cqfp.md) confere apenas esse ajuste e as contagens. A frente E pode seguir sobre o texto do v1: o conteúdo do resumo não muda.
