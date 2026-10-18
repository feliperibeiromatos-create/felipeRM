# T95_conferencia_DA_2026-10-18.md — T-95 — 2026-10-18 — gerado por gcb-gerencia

Conferência da cobertura de DA em saida/pacote/cobertura_v1_9.md (secretaria), por D-COBERTURA-AUTO-2. Ciclo s12c2. Só leitura dos arquivos de origem; conferência por script próprio (python -I).

Fontes conferidas: edital/DA_itens_1_12_P1.md (texto literal, D-ESCOPO-3); saida/gcb/D1_v2.md (canônico, D-LOTED1-CANONICO; contagem pelo rótulo "(subitem x.y)" do gabarito comentado, seção 5.2); banco/banco.csv (delimitador ";", coluna item_edital_camara, coluna anulado); banco/mapeamento_adicional.csv (D-DA-BANCO).

## 1. Lista das 37 folhas — CONFERE

Entradas sem subitens no edital: 1.1, 1.2 (2); 2.1, 2.2 (2); 3.1–3.4 (4); 4.1–4.4 (4); 5.1, 5.2 (2); 6.1–6.5 (5); 7 (1); 8.1–8.4 (4); 9.1–9.4 (4); 10.1–10.7 (7); 11, 12 (2) = 37. Títulos com subitens (1, 2, 3, 4, 5, 6, 8, 9, 10) não são folhas, inclusive os que têm texto próprio no caput (1, 8, 10). A lista de cobertura_v1_9.md, linhas 65–101, é igual, na mesma ordem.

## 2. Contagem do D1 canônico por folha — CONFERE

D1_v2.md: 1.0 = 8 (D1-01 a D1-08); 1.1 = 11 (D1-09 a D1-19); 1.2 = 11 (D1-20 a D1-30); 2.1 = 22 (D1-31 a D1-52); 2.2 = 8 (D1-53 a D1-60); total 60, todos AUTORAL, VOLÁTIL=não nos 60 (linha Marcas). Igual à conferência da presidencia em D-LOTED1-CANONICO.

| Folha | D1 (cobertura_v1_9) | D1 (conferência) | Resultado |
|---|---|---|---|
| DA 1.1 | 11 | 11 | CONFERE |
| DA 1.2 | 11 | 11 | CONFERE |
| DA 2.1 | 22 | 22 | CONFERE |
| DA 2.2 | 8 | 8 | CONFERE |
| DA 3.1 a DA 12 (33 folhas) | 0 | 0 | CONFERE |
| Soma 37 folhas | 52 | 52 | CONFERE |
| VOLÁTEIS (todas) | 0 | 0 | CONFERE |

Coluna "Faltam" (20 − D1): CONFERE nas 37 linhas para o D1. Tabela do banco por seção (linhas 108–121; 40 linhas, 2 anuladas, 38 válidas, todas CEBRASPE_ANALOGA): CONFERE seção a seção.

## 3. Reais por folha — DIVERGE em DA 7, DA 11 e DA 12

Os títulos 7, 11 e 12 não têm subitens: a seção do banco é a própria folha, e o "n/d" não se aplica.

| Folha | Reais (cobertura_v1_9) | Reais (conferência) | Faltam correto | Resultado |
|---|---|---|---|---|
| DA 7 | n/d | 3 válidas (4 linhas; 1 anulada, BQ-0133) | 17 | DIVERGE |
| DA 11 | n/d | 4 | 16 | DIVERGE |
| DA 12 | n/d | 24 = 4 (coluna do banco) + 20 (mapeamento_adicional, D-DA-BANCO, aderência direta, ids distintos, nenhum anulado) | 0 | DIVERGE |
| demais 34 folhas | n/d | n/d (seção com mais de uma folha) | como está | CONFERE |

## 4. D1 da GCB

D1-a (itens D1-01 a D1-08, subitem 1.0). Não contam para nenhuma folha. Tratam do caput do título 1 (Estado, governo, poderes, organização do Estado: CF, arts. 1º, 2º e 18), que não é folha (D-COBERTURA-AUTO: títulos de seção não contam); não se realocam a 1.1 (princípios) nem a 1.2 (organização administrativa), porque o ponto de julgamento é outro, e realocar inflaria essas folhas. Mesmo tratamento de P1 TI (ressalva (a): itens de título fora das folhas). Registro: uma linha própria "DA 1 (caput; não é folha) = 8", fora da soma das 37 e fora da meta de 20; os 8 seguem no total do lote (60). O mesmo vale, nos lotes futuros, para itens dos caputs com texto dos títulos 8 e 10.

D1-b (itens reais do banco sem nível de folha). (i) Seção com uma só folha (7, 11, 12): contar na folha, só itens válidos (anulado=nao), anuladas entre parênteses, e somar ao total da folha para o "Faltam" (critério da tabela P1: Total = AUTORAL + reais). (ii) Mapeamento adicional da D-DA-BANCO (aderência direta): conta na folha mapeada, em parcela separada ("4 + 20 adicional"), sem alterar o banco; o mesmo item continua contado em P2-4.1 no seu módulo (contagens por disciplina, sem soma cruzada). (iii) Seção com mais de uma folha (1–6, 8–10): não ratear nem classificar por inferência (a classificação por folha é mérito, não registro); os reais ficam só na tabela por seção, a célula de folha segue "n/d" e o "Faltam" da folha conta só o AUTORAL. Classificação por folha desses 30 itens fica para quando houver ordem; não abro tarefa (D-COMPLEMENTOS).

## 5. Correções que a secretaria deve fazer em saida/pacote/cobertura_v1_9.md

1. Linha 84 (DA 7): Reais "3 (+1 anulada)"; Faltam 17.
2. Linha 100 (DA 11): Reais 4; Faltam 16.
3. Linha 101 (DA 12): Reais "24 (4 + 20 adicional D-DA-BANCO)"; Faltam 0.
4. Linha 102 (Soma): Reais "31 nas folhas 7, 11, 12; demais n/d".
5. Linha 9, ressalva (b): restringir o n/d às seções com mais de uma folha e citar D1-b deste arquivo; ressalva (c): citar D1-a.
6. Linha 104: acrescentar a linha "DA 1 (caput; não é folha) = 8, fora das 37" (D1-a).
7. Linha 124: trocar "não somadas" por "somadas em DA 12 como parcela adicional (D1-b, T-95)".
Folhas abaixo de 20 fora de onda programada (linhas 126–130): continua "nenhuma" (T-100 cobre todas as folhas de DA).

FIM — T95_conferencia_DA_2026-10-18.md
