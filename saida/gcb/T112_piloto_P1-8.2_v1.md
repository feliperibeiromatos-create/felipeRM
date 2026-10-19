# T112_piloto_P1-8.2_v1.md — T-112 (E), piloto visual do tópico P1-8.2 — 2026-10-18 — gerado por gcb-cpp

Normas: V15_BAEF_D1_GCB_2026-10-18.md (seção 4, regra 0.7), ordens/ORDEM_V15_E_PILOTO_VISUAL.md, contrato v1.2.9 (V15_BAE_D1_GBQ_2026-10-18.md, seção 1.2). Base: pacote v1.11, curso L5#2, somente leitura. O resumo não está aqui (está em T111_resumos_P1_parte1_v1.md).

## (a) Em 1 minuto e visuais

Em 1 minuto (3 pontos):
1. Histograma: variável quantitativa em classes adjacentes; barras: categorias. A diferença está na variável.
2. Linha mostra evolução em eixo ordenado; dispersão mostra relação entre duas quantitativas, sem provar causa.
3. Box plot: caixa do Q1 ao Q3, linha na mediana, bigodes pelos limites de 1,5·AIQ (regra usual de Tukey).

Visual 1, tabela "Qual gráfico para qual pergunta" (4 colunas, 5 linhas, legenda). Visual 2, esquema "Como ler um box plot" (centro "Box plot", 6 ramos). Texto completo no bloco json.

Excluídos: barras (o curso não traz dado numérico com fonte oficial e data), linha (o curso não tem cronologia), fluxo (o curso não tem procedimento em passos).

## (b) Rastreio ao curso L5#2

| Elemento | Trecho do curso que sustenta |
|---|---|
| Ponto 1 | Histograma, Definição: "variável quantitativa ... classes (intervalos) adjacentes"; Gráfico de barras, Definição: "o que o distingue conceitualmente do histograma é a natureza da variável: categórica aqui, quantitativa em classes adjacentes ... no histograma". |
| Ponto 2 | Gráfico de linha: "evolução de uma variável ao longo de um eixo horizontal ordenado"; Gráfico de dispersão: "coordenadas em duas variáveis quantitativas ... Correlação visível não prova causalidade." |
| Ponto 3 | Box plot: "A caixa vai do 1º quartil (Q1) ao 3º quartil (Q3)"; "A linha interna é a mediana"; "limites Q1 − 1,5·AIQ e Q3 + 1,5·AIQ" e "regra usual de Tukey". |
| Tabela, Histograma / Quantitativa, em classes adjacentes | Definição do histograma (variável quantitativa, classes adjacentes). |
| Tabela, Histograma / Distribuição: forma, centro, dispersão, modas | "Permite ver forma (simétrica, assimétrica), centro, dispersão, modas e outliers". |
| Tabela, Histograma / Tratá-lo como barras de categorias | Pegadinha: "tratá-lo como gráfico de barras de categorias". |
| Tabela, Linha / eixo ordenado, como o tempo | "eixo horizontal ordenado, tipicamente o tempo". |
| Tabela, Linha / tendência, sazonalidade, variações | "Destaca tendência, sazonalidade e variações". |
| Tabela, Linha / Usar para categorias sem ordem | Pegadinha: "usar linha para categorias sem ordem (partidos, comissões)". |
| Tabela, Barras / Categorias discretas e seus valores; comparação | "compara valores entre categorias discretas". |
| Tabela, Barras / Confundir com histograma; eixo truncado | Pegadinha: "confundir com histograma; aceitar eixo truncado". |
| Tabela, Dispersão / Duas variáveis quantitativas | "coordenadas em duas variáveis quantitativas". |
| Tabela, Dispersão / Relação, agrupamentos e outliers | "revela relação (direção, força, forma), agrupamentos e outliers". |
| Tabela, Dispersão / Afirmar causa e efeito | Pegadinha: "afirmar que mostra causa e efeito". |
| Tabela, Box plot / Quantitativa; uma caixa por grupo | "a variável resumida é quantitativa; os grupos são categorias ... (uma caixa por comissão)". |
| Tabela, Box plot / Resumo: Q1, mediana, Q3 | "resume a distribuição de uma variável quantitativa"; caixa de Q1 a Q3; linha interna é a mediana. |
| Tabela, Box plot / linha central não é a média | Pegadinha: "dizer que a linha central é a média". |
| Legenda | "regra usual de Tukey ... mas que pode variar". |
| Ramo 1 | "contém os 50% centrais dos dados". |
| Ramo 2 | "a amplitude da caixa é o intervalo interquartil (AIQ = Q3 − Q1)". |
| Ramo 3 | "A linha interna é a mediana (não a média ...)". |
| Ramo 4 | "calculam-se os limites Q1 − 1,5·AIQ e Q3 + 1,5·AIQ"; "regra usual de Tukey". |
| Ramo 5 | "cada bigode vai até o dado mais extremo DO SEU LADO que ainda esteja dentro do limite respectivo". |
| Ramo 6 | "os pontos além dos limites são marcados individualmente como outliers". |

Coerência com o resumo do P1-8.2: mesmos fatos, sem cópia à letra (os pontos são mais curtos e reformulados).

## (c) Contagem de caracteres

- emUmMinuto: 106, 108, 103 (limite 140).
- Tabela, por linha (Gráfico, Variáveis, O que mostra, Armadilha): histograma 10/35/45/34; linha 16/43/44/30; barras 17/35/38/39; dispersão 20/28/32/22; box plot 8/33/39/35 (limite 80).
- Ramos: 44, 36, 35, 59, 65, 50 (limite 70).

## (d) Varredura (regra 0.7)

Regex das 10 categorias da ordem C sobre o texto novo: zero marcas de produção. Falsos positivos do regex, conferidos um a um: "P1-8" (chave do tópico, exigida pelo contrato) e "diferença" (palavra comum, no ponto 1); nenhum é "Difere do item". Exceções da regra 0.3: nenhuma.

## Pendências

Nenhuma.

## (e) json

```json
{
  "P1-8.2": {
    "emUmMinuto": [
      "Histograma: variável quantitativa em classes adjacentes; barras: categorias. A diferença está na variável.",
      "Linha mostra evolução em eixo ordenado; dispersão mostra relação entre duas quantitativas, sem provar causa.",
      "Box plot: caixa do Q1 ao Q3, linha na mediana, bigodes pelos limites de 1,5·AIQ (regra usual de Tukey)."
    ],
    "visuais": [
      {
        "tipo": "tabela",
        "titulo": "Qual gráfico para qual pergunta",
        "colunas": [
          "Gráfico",
          "Variáveis",
          "O que mostra",
          "Armadilha"
        ],
        "linhas": [
          [
            "Histograma",
            "Quantitativa, em classes adjacentes",
            "Distribuição: forma, centro, dispersão, modas",
            "Tratá-lo como barras de categorias"
          ],
          [
            "Gráfico de linha",
            "Uma variável em eixo ordenado, como o tempo",
            "Evolução: tendência, sazonalidade, variações",
            "Usar para categorias sem ordem"
          ],
          [
            "Gráfico de barras",
            "Categorias discretas e seus valores",
            "Comparação de valores entre categorias",
            "Confundir com histograma; eixo truncado"
          ],
          [
            "Gráfico de dispersão",
            "Duas variáveis quantitativas",
            "Relação, agrupamentos e outliers",
            "Afirmar causa e efeito"
          ],
          [
            "Box plot",
            "Quantitativa; uma caixa por grupo",
            "Resumo da distribuição: Q1, mediana, Q3",
            "Dizer que a linha central é a média"
          ]
        ],
        "legenda": "Box plot: regra usual de Tukey, que pode variar entre programas"
      },
      {
        "tipo": "esquema",
        "titulo": "Como ler um box plot",
        "centro": "Box plot",
        "ramos": [
          "Caixa do Q1 ao Q3: os 50% centrais dos dados",
          "AIQ = Q3 − Q1 é a amplitude da caixa",
          "Linha interna: mediana, não a média",
          "Limites: Q1 − 1,5·AIQ e Q3 + 1,5·AIQ (regra usual de Tukey)",
          "Cada bigode vai ao dado mais extremo do seu lado dentro do limite",
          "Pontos além dos limites são marcados como outliers"
        ]
      }
    ]
  }
}
```
