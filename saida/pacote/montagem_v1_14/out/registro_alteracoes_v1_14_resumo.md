# registro_alteracoes_v1_14_resumo.md — T-123 — 2026-10-23 — gerado por gbq-csc (registro_alteracoes_v114.py)

Registro de alterações por id da v1.14 (D1 da T-123, seção 5). Arquivo: `out/registro_alteracoes_v1_14.csv` (UTF-8, LF, separador ";"; colunas `id;tipo;campo;antes;depois;origem;ocorrencias`). Linhas: 380.

## Por tipo

| Tipo | Linhas |
|---|--:|
| entrada_reforco | 238 |
| entrada_banco | 36 |
| errata | 3 |
| formato | 91 |
| nucleo_estudante | 12 |
| **Total** | **380** |

## Notas

- `entrada_reforco`: os 238 itens D<n>-R<nn>; a origem é o arquivo da leva e o ato de aceite (linha de DECISOES.md e data).
- `entrada_banco`: os 36 itens de banco P1-DA (BQ-0113 a BQ-0152, fora BQ-0131, BQ-0133, BQ-0141 e BQ-0151).
- `errata`: D3-R13 (AJ-E1), D3-R18 (AJ-L2-E1) e D3-R75 (AJ-L7-E1), aplicadas na leitura das levas (o arquivo da leva não muda); a AJ-L8-E3 (D4-R42) e a AJ-L8-E4 (D4-R52) não têm aceite e não constam.
- `formato`: as 91 substituições da limpeza da GCB (operações: 3 39, 6 29, processo 23); 85 itens de reforço têm a justificativa alterada. Enunciado, gabarito, itemEdital e aderência não mudam.
- `nucleo_estudante`: 12 itens da v1.13 passam de true para false no pacote do estudante: D1-07, D1-08, D3-79, D3-80, D6-07, D6-08, D6-09, D6-10, D6-37, D6-38, D6-39, D6-40.
- Nenhum item da v1.13 muda no `pacote.json`.
