# lote5_errata_tukey_2026-10-13 — T-47 — 2026-10-13 — gerado por gcb-cpp

Errata de forma D-ERRATA-L5-TUKEY (Fundador, 13/10/2026) em saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md. Cópia anterior: scratchpad s4/t47/antes.md. Aplicação no pacote: T-48.

## Linha do box plot (curso 8.2, bloco "Box plot (diagrama de caixa)"; linha 117 antes, 118 depois)

ANTES:

- Bigodes e outliers (regra usual de Tukey, adotada como convenção por muitos programas, mas que pode variar): calculam-se os limites Q1 − 1,5·AIQ e Q3 + 1,5·AIQ; cada bigode vai até o dado mais extremo DO SEU LADO que ainda esteja dentro do limite respectivo, e os pontos além dos limites são marcados individualmente como outliers. A regra vale por lado: um outlier superior não impede que o bigode inferior termine no mínimo da amostra. Logo, os bigodes só coincidem com o mínimo e o máximo quando não há outliers daquele lado.

DEPOIS:

- Bigodes e outliers (regra usual de Tukey, adotada como convenção por muitos programas, mas que pode variar): calculam-se os limites Q1 − 1,5·AIQ e Q3 + 1,5·AIQ; cada bigode vai até o dado mais extremo DO SEU LADO que ainda esteja dentro do limite respectivo, e os pontos além dos limites são marcados individualmente como outliers. A regra vale por lado: um outlier superior não impede que o bigode inferior termine no mínimo da amostra. Logo, os bigodes só coincidem com o mínimo e o máximo quando não há outliers daquele lado. O fator 1,5·AIQ é a convenção usual (Tukey); outras convenções existem e a prova costuma cobrar esta.

## Registro no cabeçalho (Tabela de Correções, linha 26, após "NOTA 8.11.2 (ajuste)")

| Errata T-47 (D-ERRATA-L5-TUKEY, 13/10/2026) | 8.2, bloco "Box plot (diagrama de caixa)", linha "Bigodes e outliers" | Acrescentada ao fim da linha a frase: "O fator 1,5·AIQ é a convenção usual (Tukey); outras convenções existem e a prova costuma cobrar esta." (errata de forma; gabaritos, itens, [TS], VOLÁTIL, contagens e resumo (b) inalterados; aplicação no pacote pela T-48) | Decisão do Fundador (D-ERRATA-L5-TUKEY) | aplicada (13/10/2026); conferência CQFP pendente |

## Saída do script (Python difflib, SequenceMatcher sobre linhas)

```
('insert', 25, 25, 25, 26)
('replace', 116, 117, 117, 118)
['insert', 'replace']
OK: so linha do box plot e registro mudam; demais linhas identicas: 283 linhas preservadas
```

Operações não-equal: exatamente 2 (replace 1 linha: box plot; insert 1 linha: registro). Demais 283 linhas idênticas byte a byte.

## Bytes

- antes: 43302
- depois: 43896
- diferença: +594 = 108 (espaço + frase na linha do box plot) + 486 (linha do registro + quebra de linha)
