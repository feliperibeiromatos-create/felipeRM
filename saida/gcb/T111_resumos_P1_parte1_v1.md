# T111_resumos_P1_parte1_v1.md — T-111 (A1), resumo do tópico P1-8.2 — 2026-10-18 — gerado por gcb-cpp

Normas: V15_BAEF_D1_GCB_2026-10-18.md (seção 3, regra de tamanho e forma; regra 0.7), ordens/ORDEM_V15_A_RESUMOS.md. Base: pacote v1.11 (saida/pacote/gerador_v1_11/out/pacote.json), somente leitura.

## 1. Tópico e blocos de curso usados

P1-8.2 (Tipos de gráficos): bloco L5#2, inteiro (histograma, linha, barras, dispersão, box plot). Nenhum outro bloco.

## 2. Resumo

O histograma mostra a distribuição de frequência de uma variável quantitativa dividida em classes adjacentes de uma escala numérica; por isso as barras são contíguas e a ordem das classes é fixa. Com amplitudes desiguais, a área da barra é que deve ser proporcional à frequência, e a altura representa a densidade.

O gráfico de barras compara valores entre categorias discretas, com a base em zero. O que o distingue do histograma é a natureza da variável, categórica nele e quantitativa em classes no histograma, e não o espaçamento entre as barras, que é convenção de desenho.

O gráfico de linha mostra a evolução de uma variável em um eixo ordenado, tipicamente o tempo. O gráfico de dispersão mostra a relação entre duas variáveis quantitativas, cada ponto sendo uma observação; correlação visível não prova causalidade.

No box plot, a caixa vai do primeiro ao terceiro quartil e contém os 50% centrais dos dados; sua amplitude é o intervalo interquartil, Q3 menos Q1. A linha interna é a mediana, não a média.

Na regra usual de Tukey, que pode variar entre programas, os limites são Q1 menos 1,5 vezes o intervalo interquartil e Q3 mais 1,5 vezes esse intervalo. Cada bigode vai até o dado mais extremo do seu lado dentro do limite; pontos além dele são outliers.

## 3. Contagens (regra de tamanho)

- Parágrafos: 5 (limite 3 a 6); palavras por parágrafo: 52, 45, 38, 36, 46 (limite 60 cada).
- Palavras do resumo: 217 (limite 80 a 220). Palavras do curso do tópico (sem o título): 694. Percentual: 31.3% (limite 40%).
- Forma: prosa corrida, sem lista, sem tabela, sem negrito; nenhuma linha começa com número de item nem com rótulo em maiúsculas seguido de dois-pontos; sem exemplo novo; sem fato datado (nenhuma fonte ou data a citar).
- Cobertura: pegadinha central do curso (histograma tratado como gráfico de barras de categorias) está no 1º e 2º parágrafos; demais ideias centrais: linha × dispersão, causalidade, caixa/mediana, regra de Tukey por lado.

## 4. Rastreio frase a frase

| Frase | Resumo | Trecho do curso que sustenta |
|---|---|---|
| 1.1 | O histograma mostra a distribuição de frequência ... escala numérica; por isso as barras são contíguas e a ordem das classes é fixa. | Histograma, Definição: "distribuição de frequência de uma variável quantitativa ... dividida em classes (intervalos) adjacentes de uma escala numérica. Por isso as barras são contíguas e a ordem das classes é fixa." |
| 1.2 | Com amplitudes desiguais, a área da barra ... a altura representa a densidade. | Histograma, Definição: "Com classes de amplitudes desiguais, a ÁREA da barra é que deve ser proporcional à frequência, e a altura passa a representar a densidade de frequência." |
| 2.1 | O gráfico de barras compara valores entre categorias discretas, com a base em zero. | Gráfico de barras, Definição: "compara valores entre categorias discretas; ... a base é em zero." |
| 2.2 | O que o distingue do histograma é a natureza da variável ... convenção de desenho. | Gráfico de barras, Definição: "o espaçamento entre as barras é convenção de desenho; o que o distingue conceitualmente do histograma é a natureza da variável: categórica aqui, quantitativa em classes adjacentes ... no histograma." Pegadinha: "confundir com histograma". |
| 3.1 | O gráfico de linha mostra a evolução ... tipicamente o tempo. | Gráfico de linha, Definição: "evolução de uma variável ao longo de um eixo horizontal ordenado, tipicamente o tempo." |
| 3.2 | O gráfico de dispersão mostra a relação entre duas variáveis quantitativas, cada ponto sendo uma observação; | Gráfico de dispersão, Definição: "cada ponto é uma observação com coordenadas em duas variáveis quantitativas; revela relação". |
| 3.3 | correlação visível não prova causalidade. | Gráfico de dispersão, Definição: "Correlação visível não prova causalidade." |
| 4.1 | No box plot, a caixa vai do primeiro ao terceiro quartil e contém os 50% centrais; amplitude = intervalo interquartil, Q3 menos Q1. | Box plot, Definição: "A caixa vai do 1º quartil (Q1) ao 3º quartil (Q3), ou seja, contém os 50% centrais dos dados; ... (AIQ = Q3 − Q1)." |
| 4.2 | A linha interna é a mediana, não a média. | Box plot, Definição: "A linha interna é a mediana (não a média ...)." |
| 5.1 | Na regra usual de Tukey, que pode variar entre programas, os limites são Q1 menos 1,5 vezes ... e Q3 mais 1,5 vezes ... | Box plot, Bigodes e outliers: "regra usual de Tukey ... pode variar: ... limites Q1 − 1,5·AIQ e Q3 + 1,5·AIQ". |
| 5.2 | Cada bigode vai até o dado mais extremo do seu lado dentro do limite; pontos além dele são outliers. | Box plot, Bigodes e outliers: "cada bigode vai até o dado mais extremo DO SEU LADO que ainda esteja dentro do limite respectivo, e os pontos além dos limites são marcados individualmente como outliers." |

## 5. Varredura (regra 0.7)

Regex das 10 categorias da ordem C sobre o texto do resumo (referências de lote, ids de item, códigos de par e de fonte, etiquetas, prefixos TC/IC/GI/AT, "Difere do item", QA, errata, versão, marcas de lista e negrito): zero ocorrências. Exceções da regra 0.3: nenhuma neste tópico.

## Pendências

Nenhuma.

```json
{
  "P1-8.2": {
    "resumo": "O histograma mostra a distribuição de frequência de uma variável quantitativa dividida em classes adjacentes de uma escala numérica; por isso as barras são contíguas e a ordem das classes é fixa. Com amplitudes desiguais, a área da barra é que deve ser proporcional à frequência, e a altura representa a densidade.\n\nO gráfico de barras compara valores entre categorias discretas, com a base em zero. O que o distingue do histograma é a natureza da variável, categórica nele e quantitativa em classes no histograma, e não o espaçamento entre as barras, que é convenção de desenho.\n\nO gráfico de linha mostra a evolução de uma variável em um eixo ordenado, tipicamente o tempo. O gráfico de dispersão mostra a relação entre duas variáveis quantitativas, cada ponto sendo uma observação; correlação visível não prova causalidade.\n\nNo box plot, a caixa vai do primeiro ao terceiro quartil e contém os 50% centrais dos dados; sua amplitude é o intervalo interquartil, Q3 menos Q1. A linha interna é a mediana, não a média.\n\nNa regra usual de Tukey, que pode variar entre programas, os limites são Q1 menos 1,5 vezes o intervalo interquartil e Q3 mais 1,5 vezes esse intervalo. Cada bigode vai até o dado mais extremo do seu lado dentro do limite; pontos além dele são outliers."
  }
}
```
