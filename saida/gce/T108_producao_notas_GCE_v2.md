# T-108 — notas de produção da GCE, v2 (T-108-GCE-P2) — 2026-10-18 — gerado por gce-cpp

Objeto: saida/gce/T108_substituicoes_GCE_v2.csv (269 registros). Base: saida/gce/T108_substituicoes_GCE.csv (v1, 263 linhas) e saida/gce/T108_D1_pos_R1_GCE_2026-10-18.md, seção 6. Gerado por script (python -I) que serializa os registros com o mesmo escritor CSV da v1 (UTF-8, vírgula, aspas mínimas, fim de registro CRLF, quebras LF dentro dos campos), depois de confirmar que ele reproduz a v1 byte a byte.

Contagens: 269 = 257 inalteradas + 6 corrigidas (GCE-0094, 0105, 0154, 0205, 0218, 0235; só mudam `depois` e `nota`) + 6 novas (GCE-0264 a 0269, no fim, nessa ordem).

Saída da autoconferência (somente leitura, python -I):

```
(a) registros v2: 269 (esperado 269); cabecalho igual: True
(b) iguais byte a byte a v1: 257 (esperado 257); ordem preservada: True ; novas no fim, em ordem: True
    corrigida GCE-0094 colunas alteradas: ['depois', 'nota']
    corrigida GCE-0105 colunas alteradas: ['depois', 'nota']
    corrigida GCE-0154 colunas alteradas: ['depois', 'nota']
    corrigida GCE-0205 colunas alteradas: ['depois', 'nota']
    corrigida GCE-0218 colunas alteradas: ['depois', 'nota']
    corrigida GCE-0235 colunas alteradas: ['depois', 'nota']
pacote SHA bruto 58e73632091fad60bcea796dab96c9512c86cf8bfbe752b7ac5f209fc2ffff0c | LF d43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed | confere D1: True
(c) antes das 12 ocorre 1x no campo do pacote v1.10: True
(d) pares sobrepostos nas 269: 0
    antes unico no campo em todas as 269: True []
(e) campos tocados: 121 | residuos (termos + padroes da secao 5): 0
    (os 11 textos novos ou corrigidos conferidos presentes nos campos apos aplicar: True)
(f) SHA-256 v1: 5732a193f49f753e7becd1ec5783682f7a6609b4ecccb175dc09435b3fe42024 | confere: True
    SHA-256 v2: c4a29f1bf21721a1d2ec52517462f56c4fae8fca8cbf2c517875200c87f07fe7
FALHAS: []
```

Em (e), os termos varridos foram "costuma ser cobrad", "costumam ser cobrad", "do Projeto", "não afirmar", "Inapto a simulado" e os padrões da seção 5 da D1 inicial (códigos F/N, de item, de par, [V, NORMATIVO, REVERIFICAR, QA, CPP, GCE, CQFP, Lote(s), VOLÁTIL, errata, vN, D-…, não cobrar, SEM ITEM, NÃO GABARITO, Difere, Qnn, par Cn, CONTROVERSO, R2–R9, En, espelho da troca, hipótese (a–c)).
