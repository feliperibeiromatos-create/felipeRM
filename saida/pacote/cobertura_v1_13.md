# cobertura_v1_13.md — T-95 — 2026-10-20 — gerado por secretaria

Ocorrência v1.13 de D-COBERTURA-AUTO e D-COBERTURA-AUTO-2 e regra de D-T97-META-FUNDADOR-RESP. Contagem por item-folha do edital (entrada sem subitens; títulos de seção não contam). Meta: 20 por folha, com piso de 10 diretos por folha (D-T97-META-FUNDADOR-RESP; T-107). Formato igual ao de cobertura_v1_12.md. Passo 4.4 da D1 da T-118 (saida/pacote/T118_D1_v1_13_2026-10-20.md).

**Fontes.** P1, P2 e DA: saida/pacote/montagem_v1_13/out/pacote.json v1.13 (geradoEm 2026-10-20; 1159 itens; SHA-256 82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240; campos itemEdital, rotulo, aderencia, volatil). Núcleo: saida/pacote/montagem_v1_13/out/pacote_estudante.json v1.13-E (SHA-256 04cbd593fdd30404ecb7f91f6b6722da6b2fc24e58d3c0eb68b10a4e792a0c40; campo nucleo, por id; mesma lista de ids do pacote.json). Observação: a errata do achado 10 da T-117 só muda um texto de par do D6 e não afeta contagens. Folhas: 75 entradas do edital do pacote sem subitens (15 P1, 23 P2 e 37 DA); as 37 de DA conferidas contra as entradas sem subitens de edital/DA_itens_1_12_P1.md (D-COBERTURA-AUTO-2; conjuntos iguais). Script: saida/pacote/montagem_v1_13/cobertura_v1_13.py (python3 -I, só leitura do repositório; SHA-256 72a89f86f001aebb6f4b5cf33b88c27b7f3eecbbfc75a3f0a6ccad3c8cf95312).

**Definições.** Total = itens na folha (AUTORAL + CEBRASPE_ANALOGA). AUTORAL = rotulo AUTORAL. Reais = rotulo CEBRASPE_ANALOGA. Diretos e PARCIAIS = campo aderencia ("direta" e "parcial"). VOLÁTEIS = campo volatil verdadeiro. Núcleo = nucleo verdadeiro no pacote_estudante. Formatos: o pacote não tem campo de formato por item; a coluna não existe no formato da cobertura_v1_12.md e não foi recontada (n/d). Meta 20 cumprida: total >= 20. Piso 10 diretos cumprido: diretos >= 10.

**Totais de conferência.** 1159 itens no pacote; 1132 em folhas; 27 fora das folhas (ressalva (a)). Gabarito: 582 C e 577 E (conferido no pacote). AUTORAL nas folhas: 1038; Reais nas folhas: 94; Diretos: 1038; PARCIAIS: 94; VOLÁTEIS: 91; Núcleo: 706. Por matéria, em folhas: P1 172, P2 564, DA 396.

**Critério de aceite da D1 (passo 4.4).** 75 folhas: 75 (confere). 1.159 itens: 1159 (confere). 1.132 em folha: 1132 (confere). 27 fora: 27 (confere). C/E 582/577: 582/577 (confere). DA 396 itens em folha: 396 (confere); 5 VOLÁTEIS: 5 no pacote, 5 em folha; núcleo 352 nas folhas: 352 (confere); 0 reais: 0 (confere). DA com 20 ou mais: 3 (confere); abaixo de 20: 34 (confere).

**Ressalvas de cobertura.**
(a) Itens com itemEdital de título (não folha) ficam fora das folhas: 27 itens. P1 e P2 (13, os mesmos da v1.12): 6B-01, BQ-0009, BQ-0011, BQ-0012, BQ-0038, BQ-0039, BQ-0069, BQ-0070, BQ-0071, BQ-0078, BQ-0079, BQ-0102, BQ-0111. DA (14): P1-DA-1 com 8 (D1-01, D1-02, D1-03, D1-04, D1-05, D1-06, D1-07, D1-08); P1-DA-8 com 6 (D4-74, D4-75, D4-76, D4-77, D4-78, D4-79) (P1-DA-1 é o caput do título 1 e P1-DA-8 é o caput do título 8; D1-a).
(b) Reais de DA: o pacote v1.13 não tem item CEBRASPE_ANALOGA de DA (0); os 38 itens de banco com itemEdital P1-DA ficam fora da v1.13 e dependem de D1 própria (T-118, (d); T-78 e T-79; T-123), por isso a coluna Reais de DA é 0 e as folhas DA 7, 11 e 12 não somam os reais do banco que cobertura_v1_11.md listava.
(c) O piso de 10 diretos é decidido para P2 1.x a 3.x (T-107). P1, P2 4.x e DA aparecem com o mesmo cálculo, só para conferência; nas listas, o rótulo "fora do escopo T-107" marca essas folhas.
(d) A coluna "Onda programada" de P1 não foi reconstruída nesta ocorrência (n/r); a programação das ondas está em TAREFAS.md. Para DA, as folhas abaixo de 20 estão na onda da T-116 (D-REFORCO-DA; reforço até 20 por folha, das mais ralas às mais cheias), por isso nada se escreve em PARA_PRESIDENCIA.md por DA.
(e) Mudanças de total, AUTORAL, reais, diretos, PARCIAIS, VOLÁTEIS ou núcleo de P1 e P2 desde a v1.12: nenhuma (as 38 folhas são idênticas às de cobertura_v1_12.md). A v1.13 acrescenta 410 itens de DA (D1 60, D2 80, D3 71, D4 79, D5 70, D6 50), todos AUTORAL e diretos.
(f) Folhas P2 1.x a 4.x: nenhuma abaixo de 20. As folhas P1 abaixo de 20 são 14. As folhas de DA abaixo de 20 são 34; com 20 ou mais, 3 (DA 2.1 = 22, DA 11 = 30, DA 12 = 20).

## P1 — TI (itens 1 a 8; 15 folhas)

| Folha | Total | AUTORAL | Reais | Diretos | PARCIAIS | VOLÁTEIS | Núcleo | Meta 20 | Faltam | Piso 10 diretos | Onda programada |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1-1 | 16 | 10 | 6 | 12 | 4 | 3 | 10 | não | 4 | sim | n/r |
| P1-2.1 | 6 | 4 | 2 | 6 | 0 | 2 | 6 | não | 14 | não (fora do escopo T-107) | n/r |
| P1-3 | 6 | 6 | 0 | 6 | 0 | 2 | 6 | não | 14 | não (fora do escopo T-107) | n/r |
| P1-4.1 | 11 | 4 | 7 | 10 | 1 | 0 | 10 | não | 9 | sim | n/r |
| P1-4.2 | 8 | 3 | 5 | 7 | 1 | 1 | 8 | não | 12 | não (fora do escopo T-107) | n/r |
| P1-4.3 | 6 | 5 | 1 | 6 | 0 | 1 | 6 | não | 14 | não (fora do escopo T-107) | n/r |
| P1-5.1 | 17 | 16 | 1 | 17 | 0 | 0 | 10 | não | 3 | sim | n/r |
| P1-5.2 | 30 | 12 | 18 | 29 | 1 | 0 | 10 | sim | 0 | sim | — |
| P1-5.3 | 15 | 5 | 10 | 14 | 1 | 3 | 10 | não | 5 | sim | n/r |
| P1-6 | 7 | 4 | 3 | 6 | 1 | 0 | 7 | não | 13 | não (fora do escopo T-107) | n/r |
| P1-7.1 | 9 | 4 | 5 | 7 | 2 | 0 | 9 | não | 11 | não (fora do escopo T-107) | n/r |
| P1-8.1 | 7 | 3 | 4 | 5 | 2 | 0 | 7 | não | 13 | não (fora do escopo T-107) | n/r |
| P1-8.2 | 19 | 12 | 7 | 16 | 3 | 0 | 10 | não | 1 | sim | n/r |
| P1-8.3 | 7 | 4 | 3 | 5 | 2 | 6 | 7 | não | 13 | não (fora do escopo T-107) | n/r |
| P1-8.4 | 8 | 7 | 1 | 8 | 0 | 0 | 8 | não | 12 | não (fora do escopo T-107) | n/r |
| **Soma** | 172 | 99 | 73 | 154 | 18 | 18 | 124 | | | | |

## P2 — RF/IA (itens 1.1 a 4.3; 23 folhas)

| Folha | Total | AUTORAL | Reais | Diretos | PARCIAIS | VOLÁTEIS | Núcleo | Meta 20 | Faltam | Piso 10 diretos | Onda programada |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P2-1.1 | 29 | 29 | 0 | 29 | 0 | 1 | 10 | sim | 0 | sim | — |
| P2-1.2 | 30 | 30 | 0 | 30 | 0 | 0 | 10 | sim | 0 | sim | — |
| P2-1.3 | 30 | 30 | 0 | 30 | 0 | 6 | 10 | sim | 0 | sim | — |
| P2-1.4 | 30 | 30 | 0 | 30 | 0 | 6 | 10 | sim | 0 | sim | — |
| P2-1.5 | 30 | 30 | 0 | 30 | 0 | 6 | 10 | sim | 0 | sim | — |
| P2-1.6 | 30 | 30 | 0 | 30 | 0 | 6 | 10 | sim | 0 | sim | — |
| P2-1.7 | 30 | 30 | 0 | 30 | 0 | 6 | 10 | sim | 0 | sim | — |
| P2-1.8 | 30 | 30 | 0 | 30 | 0 | 2 | 10 | sim | 0 | sim | — |
| P2-2.1 | 27 | 27 | 0 | 17 | 10 | 5 | 10 | sim | 0 | sim | — |
| P2-2.2 | 21 | 21 | 0 | 14 | 7 | 1 | 10 | sim | 0 | sim | — |
| P2-2.3 | 20 | 20 | 0 | 10 | 10 | 3 | 10 | sim | 0 | sim | — |
| P2-2.4 | 20 | 20 | 0 | 11 | 9 | 3 | 10 | sim | 0 | sim | — |
| P2-2.5 | 20 | 20 | 0 | 17 | 3 | 4 | 10 | sim | 0 | sim | — |
| P2-2.6 | 20 | 20 | 0 | 16 | 4 | 3 | 10 | sim | 0 | sim | — |
| P2-2.7 | 20 | 20 | 0 | 18 | 2 | 0 | 10 | sim | 0 | sim | — |
| P2-2.8 | 20 | 20 | 0 | 19 | 1 | 4 | 10 | sim | 0 | sim | — |
| P2-3.1 | 27 | 27 | 0 | 22 | 5 | 5 | 10 | sim | 0 | sim | — |
| P2-3.2 | 20 | 20 | 0 | 20 | 0 | 1 | 10 | sim | 0 | sim | — |
| P2-3.3 | 20 | 20 | 0 | 18 | 2 | 0 | 10 | sim | 0 | sim | — |
| P2-3.4 | 20 | 20 | 0 | 19 | 1 | 3 | 10 | sim | 0 | sim | — |
| P2-4.1 | 30 | 9 | 21 | 9 | 21 | 1 | 10 | sim | 0 | não (fora do escopo T-107) | — |
| P2-4.2 | 20 | 20 | 0 | 20 | 0 | 0 | 10 | sim | 0 | sim | — |
| P2-4.3 | 20 | 20 | 0 | 19 | 1 | 2 | 10 | sim | 0 | sim | — |
| **Soma** | 564 | 543 | 21 | 488 | 76 | 68 | 230 | | | | |

## DA — Noções de Direito Administrativo (37 folhas de edital/DA_itens_1_12_P1.md)

Ordem do edital. Reais = 0 em todas as folhas (ressalva (b)). Todos os itens de DA são AUTORAL e diretos (PARCIAIS = 0).

| Folha | Total | AUTORAL | Reais | Diretos | PARCIAIS | VOLÁTEIS | Núcleo | Meta 20 | Faltam | Piso 10 diretos | Onda programada |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DA 1.1 | 11 | 11 | 0 | 11 | 0 | 0 | 10 | não | 9 | sim | T-116 (D-REFORCO-DA) |
| DA 1.2 | 11 | 11 | 0 | 11 | 0 | 0 | 10 | não | 9 | sim | T-116 (D-REFORCO-DA) |
| DA 2.1 | 22 | 22 | 0 | 22 | 0 | 0 | 10 | sim | 0 | sim | — |
| DA 2.2 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | não | 12 | não (fora do escopo T-107) | T-116 (D-REFORCO-DA) |
| DA 3.1 | 10 | 10 | 0 | 10 | 0 | 1 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 3.2 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 3.3 | 10 | 10 | 0 | 10 | 0 | 1 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 3.4 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 4.1 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 4.2 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 4.3 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 4.4 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 5.1 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 5.2 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | não | 11 | não (fora do escopo T-107) | T-116 (D-REFORCO-DA) |
| DA 6.1 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 6.2 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | não | 11 | não (fora do escopo T-107) | T-116 (D-REFORCO-DA) |
| DA 6.3 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | não | 13 | não (fora do escopo T-107) | T-116 (D-REFORCO-DA) |
| DA 6.4 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | não | 12 | não (fora do escopo T-107) | T-116 (D-REFORCO-DA) |
| DA 6.5 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | não | 12 | não (fora do escopo T-107) | T-116 (D-REFORCO-DA) |
| DA 7 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 8.1 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | não | 14 | não (fora do escopo T-107) | T-116 (D-REFORCO-DA) |
| DA 8.2 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 8.3 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 8.4 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | não | 13 | não (fora do escopo T-107) | T-116 (D-REFORCO-DA) |
| DA 9.1 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 9.2 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 9.3 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 9.4 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 10.1 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 10.2 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 10.3 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 10.4 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 10.5 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 10.6 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 10.7 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | não | 10 | sim | T-116 (D-REFORCO-DA) |
| DA 11 | 30 | 30 | 0 | 30 | 0 | 1 | 10 | sim | 0 | sim | — |
| DA 12 | 20 | 20 | 0 | 20 | 0 | 2 | 10 | sim | 0 | sim | — |
| **Soma** | 396 | 396 | 0 | 396 | 0 | 5 | 352 | | | | |

### DA — da folha mais rala para a mais cheia (ordem da D-REFORCO-DA)

Empate de total: ordem do edital. "Faltam para 20" = 20 menos o total, mínimo 0.

| # | Folha | Total | Faltam para 20 | Diretos | VOLÁTEIS | Núcleo |
|---|---|---|---|---|---|---|
| 1 | DA 8.1 | 6 | 14 | 6 | 0 | 6 |
| 2 | DA 6.3 | 7 | 13 | 7 | 0 | 7 |
| 3 | DA 8.4 | 7 | 13 | 7 | 0 | 7 |
| 4 | DA 2.2 | 8 | 12 | 8 | 0 | 8 |
| 5 | DA 6.4 | 8 | 12 | 8 | 0 | 8 |
| 6 | DA 6.5 | 8 | 12 | 8 | 0 | 8 |
| 7 | DA 5.2 | 9 | 11 | 9 | 0 | 9 |
| 8 | DA 6.2 | 9 | 11 | 9 | 0 | 9 |
| 9 | DA 3.1 | 10 | 10 | 10 | 1 | 10 |
| 10 | DA 3.2 | 10 | 10 | 10 | 0 | 10 |
| 11 | DA 3.3 | 10 | 10 | 10 | 1 | 10 |
| 12 | DA 3.4 | 10 | 10 | 10 | 0 | 10 |
| 13 | DA 4.1 | 10 | 10 | 10 | 0 | 10 |
| 14 | DA 4.2 | 10 | 10 | 10 | 0 | 10 |
| 15 | DA 4.3 | 10 | 10 | 10 | 0 | 10 |
| 16 | DA 4.4 | 10 | 10 | 10 | 0 | 10 |
| 17 | DA 5.1 | 10 | 10 | 10 | 0 | 10 |
| 18 | DA 6.1 | 10 | 10 | 10 | 0 | 10 |
| 19 | DA 7 | 10 | 10 | 10 | 0 | 10 |
| 20 | DA 8.2 | 10 | 10 | 10 | 0 | 10 |
| 21 | DA 8.3 | 10 | 10 | 10 | 0 | 10 |
| 22 | DA 9.1 | 10 | 10 | 10 | 0 | 10 |
| 23 | DA 9.2 | 10 | 10 | 10 | 0 | 10 |
| 24 | DA 9.3 | 10 | 10 | 10 | 0 | 10 |
| 25 | DA 9.4 | 10 | 10 | 10 | 0 | 10 |
| 26 | DA 10.1 | 10 | 10 | 10 | 0 | 10 |
| 27 | DA 10.2 | 10 | 10 | 10 | 0 | 10 |
| 28 | DA 10.3 | 10 | 10 | 10 | 0 | 10 |
| 29 | DA 10.4 | 10 | 10 | 10 | 0 | 10 |
| 30 | DA 10.5 | 10 | 10 | 10 | 0 | 10 |
| 31 | DA 10.6 | 10 | 10 | 10 | 0 | 10 |
| 32 | DA 10.7 | 10 | 10 | 10 | 0 | 10 |
| 33 | DA 1.1 | 11 | 9 | 11 | 0 | 10 |
| 34 | DA 1.2 | 11 | 9 | 11 | 0 | 10 |
| 35 | DA 12 | 20 | 0 | 20 | 2 | 10 |
| 36 | DA 2.1 | 22 | 0 | 22 | 0 | 10 |
| 37 | DA 11 | 30 | 0 | 30 | 1 | 10 |
| | **Soma (37 folhas)** | 396 | 356 | 396 | 5 | 352 |

Faltam 356 itens para as 34 folhas de DA abaixo de 20 chegarem a 20 (sem contar os itens fora de folha de P1-DA-1 e P1-DA-8, caput). Folhas de DA com menos de 10 itens: DA 8.1 = 6, DA 6.3 = 7, DA 8.4 = 7, DA 2.2 = 8, DA 6.4 = 8, DA 6.5 = 8, DA 5.2 = 9, DA 6.2 = 9.

## Listas para o orquestrador (T-95, T-107)

(a) Folhas P1 abaixo de 20 (14; a programação de onda não foi reconstruída, ressalva (d)): P1-1 (16; faltam 4), P1-2.1 (6; faltam 14), P1-3 (6; faltam 14), P1-4.1 (11; faltam 9), P1-4.2 (8; faltam 12), P1-4.3 (6; faltam 14), P1-5.1 (17; faltam 3), P1-5.3 (15; faltam 5), P1-6 (7; faltam 13), P1-7.1 (9; faltam 11), P1-8.1 (7; faltam 13), P1-8.2 (19; faltam 1), P1-8.3 (7; faltam 13), P1-8.4 (8; faltam 12).
(a2) Folhas P2 1.x a 4.x abaixo de 20: nenhuma.
(a3) Folhas que atingiram 30 itens (9): P1-5.2, P2-1.2, P2-1.3, P2-1.4, P2-1.5, P2-1.6, P2-1.7, P2-1.8, P2-4.1.
(a4) Folhas de DA abaixo de 20 (34; todas na onda da T-116): DA 8.1 (6; faltam 14), DA 6.3 (7; faltam 13), DA 8.4 (7; faltam 13), DA 2.2 (8; faltam 12), DA 6.4 (8; faltam 12), DA 6.5 (8; faltam 12), DA 5.2 (9; faltam 11), DA 6.2 (9; faltam 11), DA 3.1 (10; faltam 10), DA 3.2 (10; faltam 10), DA 3.3 (10; faltam 10), DA 3.4 (10; faltam 10), DA 4.1 (10; faltam 10), DA 4.2 (10; faltam 10), DA 4.3 (10; faltam 10), DA 4.4 (10; faltam 10), DA 5.1 (10; faltam 10), DA 6.1 (10; faltam 10), DA 7 (10; faltam 10), DA 8.2 (10; faltam 10), DA 8.3 (10; faltam 10), DA 9.1 (10; faltam 10), DA 9.2 (10; faltam 10), DA 9.3 (10; faltam 10), DA 9.4 (10; faltam 10), DA 10.1 (10; faltam 10), DA 10.2 (10; faltam 10), DA 10.3 (10; faltam 10), DA 10.4 (10; faltam 10), DA 10.5 (10; faltam 10), DA 10.6 (10; faltam 10), DA 10.7 (10; faltam 10), DA 1.1 (11; faltam 9), DA 1.2 (11; faltam 9).
(b) Folhas com menos de 10 diretos (P1 e P2): P1-2.1 (6), P1-3 (6), P1-4.2 (7), P1-4.3 (6), P1-6 (6), P1-7.1 (7), P1-8.1 (5), P1-8.3 (5), P1-8.4 (8), P2-4.1 (9). Nas folhas P2 1.x a 3.x, nenhuma.
(b2) Folhas de DA com menos de 10 diretos (fora do escopo T-107): DA 2.2 (8), DA 5.2 (9), DA 6.2 (9), DA 6.3 (7), DA 6.4 (8), DA 6.5 (8), DA 8.1 (6), DA 8.4 (7).

FIM — cobertura_v1_13.md
