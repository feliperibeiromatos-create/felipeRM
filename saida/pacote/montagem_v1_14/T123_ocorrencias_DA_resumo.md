# T123_ocorrencias_DA_resumo.md — T-123 fase 1 — 2026-10-23 — gerado por gbq-csc

Extracao por script (`python -I extrair_reforco_da.py`), leitura CRLF->LF, SHA-256 LF das 8 levas e de banco/banco.csv conferidos. Insumo da limpeza da GCB (D1, secao 3). Nada foi corrigido.

Campos lidos: enunciado e justificativa (j1 + " " + j2) dos 238 de reforco; enunciado, comando e textoBase dos 36 de banco P1-DA. Regras: C-MARCAS (D1 8.1) + inventario T-108 (categorias C01-C10 da ORDEM C) + lista R de marcas_processo.py. Sobrepostos na mesma categoria sao fundidos. Classe: MARCA (limpar), VERIFICAR (decisao da GCB), FP (falso positivo).

## Totais

- Ocorrencias: 109 (FP 2, MARCA 103, VERIFICAR 4).
- Itens de reforco com ao menos 1 MARCA: 85 de 238 (a D1 estimou 85 com padrao mais largo). Em enunciado: 0.
- Itens de banco com MARCA: 0 de 36.

## MARCA por categoria

| Categoria | Descricao | Ocorrencias | Reforco | Banco |
|---|---|--:|--:|--:|
| C01 | lote/leva de producao | 0 | 0 | 0 |
| C02 | codigo de item / ponto | 8 | 8 | 0 |
| C03 | codigo de par, pegadinha, alerta | 33 | 33 | 0 |
| C04 | etiqueta entre colchetes | 0 | 0 | 0 |
| C05 | codigo de fonte, Anexo, url | 41 | 41 | 0 |
| C06 | mecanismo TC/IC/GI/AT, (C|E)n | 0 | 0 | 0 |
| C07 | QA, unidade, agente | 0 | 0 | 0 |
| C08 | producao, errata, fabrica, id de decisao | 0 | 0 | 0 |
| C09 | versao de producao | 0 | 0 | 0 |
| C10 | instrucao interna (moldura, cota, ficha, [TS], folha, PENDENTE, **...) | 21 | 21 | 0 |

## MARCA por lote e por leva (reforco)

| Lote | D1 | D2 | D3 | D4 |
|---|--:|--:|--:|--:|
| ocorrencias | 1 | 22 | 42 | 38 |

| Leva | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| ocorrencias | 25 | 16 | 22 | 13 | 12 | 5 | 4 | 6 |

## Subtipos de MARCA (reforco e banco)

| Categoria | Subtipo | n |
|---|---|--:|
| C02 | id de item | 8 |
| C03 | alerta | 33 |
| C05 | Anexo N | 4 |
| C05 | codigo de fonte R/F/G/H | 37 |
| C10 | cota | 1 |
| C10 | folha | 2 |
| C10 | moldura | 18 |

## Ids de reforco com MARCA (85)

D4-R01, D4-R02, D4-R03, D4-R04, D4-R05, D4-R06, D4-R07, D4-R08, D4-R09, D4-R10, D4-R11, D4-R18, D4-R13, D4-R14, D3-R01, D3-R02, D3-R04, D3-R09, D3-R12, D4-R15, D4-R16, D4-R17, D4-R19, D4-R20, D4-R21, D4-R22, D4-R23, D4-R24, D4-R25, D4-R26, D4-R27, D4-R28, D1-R02, D3-R15, D3-R17, D3-R20, D3-R25, D3-R26, D3-R31, D3-R32, D3-R33, D3-R36, D3-R37, D3-R43, D3-R44, D3-R46, D3-R49, D3-R50, D3-R51, D3-R52, D3-R53, D3-R54, D3-R55, D3-R56, D3-R57, D3-R58, D3-R59, D2-R02, D2-R03, D2-R05, D2-R07, D2-R10, D2-R25, D2-R32, D2-R35, D2-R37, D2-R39, D2-R41, D2-R45, D2-R47, D2-R48, D2-R50, D2-R54, D2-R58, D2-R65, D2-R77, D3-R74, D3-R77, D3-R85, D4-R31, D4-R34, D4-R35, D4-R38, D4-R43, D4-R51

## Conferencias

- 238 ids unicos; C/E [122, 116]; parciais 35; erratas AJ-E1, AJ-L2-E1, AJ-L7-E1 com antes 1x / depois 0x antes de aplicar.
- Colunas do CSV (";" UTF-8 LF): id_ocorrencia, item, origem, lote, leva, campo, parte, posicao, categoria, subtipo, regras, classe, motivo, trecho_antes, ocorrencias_do_trecho_no_campo, antes_unico, arquivo_linha. `antes_unico` = menor trecho em torno da ocorrencia que ocorre 1 vez no campo (para a coluna `antes` das substituicoes).
