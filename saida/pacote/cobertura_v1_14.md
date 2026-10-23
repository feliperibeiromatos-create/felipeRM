# cobertura_v1_14.md — T-95 — 2026-10-23 — gerado por secretaria

Ocorrência v1.14 de D-COBERTURA-AUTO e D-COBERTURA-AUTO-2 e regra de D-T97-META-FUNDADOR-RESP (formato da v1.13). Contagem por item-folha do edital (entrada sem subitens; títulos de seção não contam). Meta: 20 por folha, com piso de 10 diretos por folha (D-T97-META-FUNDADOR-RESP; T-107). Tarefa T-95 recorrente, ocorrência da v1.14 (T-123).

**Fontes.** P1, P2 e DA: saida/pacote/montagem_v1_14/out/pacote.json v1.14 (geradoEm 2026-10-23; 1433 itens; SHA-256 070bc237fcc7371a23365f6e66c9341cf5c0aee08ad9206a9f7be6c06150d495; campos itemEdital, rotulo, aderencia, volatil). Núcleo: saida/pacote/montagem_v1_14/out/pacote_estudante.json (SHA-256 6b56a7f8a1c7c42a01e145b0da35ab48691496fde82d2a9ee8fd4a6ff195b9ab; campo nucleo, por id; mesma lista de ids do pacote.json). Conferência: saida/pacote/montagem_v1_14/out/cobertura_v1_14.json (T-123). Folhas: 75 entradas do edital sem subitens (15 P1, 23 P2 e 37 DA); as 37 de DA conferidas contra edital/DA_itens_1_12_P1.md (D-COBERTURA-AUTO-2; conjuntos iguais). Script de contagem: rascunho em scratchpad t95/cobertura_v1_14.py (SHA-256 e280a9ace170249a3cce6eeb6171fb3e44aa0691b7652311d2576360f154d4f4).

**Definições.** Total = itens na folha (AUTORAL + CEBRASPE_ANALOGA). AUTORAL = rotulo AUTORAL. Reais = rotulo CEBRASPE_ANALOGA. Diretos e PARCIAIS = campo aderencia ("direta" e "parcial"). VOLÁTEIS = campo volatil verdadeiro. Núcleo = nucleo verdadeiro no pacote_estudante. Meta 20 cumprida: total >= 20. Piso 10 diretos cumprido: diretos >= 10.

**Totais de conferência.** 1433 itens no pacote; 1380 em folhas; 53 fora das folhas (ressalva (a)). Gabarito: 730 C e 703 E. AUTORAL nas folhas: 1276; Reais nas folhas: 104; Diretos: 1251; PARCIAIS: 129; VOLÁTEIS: 91; Núcleo: 724. Por matéria, em folhas: P1 172, P2 564, DA 644.

**Conferência contra cobertura_v1_14.json.** Sem divergências: todas as folhas, totais de gabarito, fora de folha e por matéria conferem.

**Ressalvas de cobertura.**
(a) Itens com itemEdital de título (não folha) ficam fora das folhas: 53 itens. P1 e P2 (39): 6B-01, BQ-0009, BQ-0011, BQ-0012, BQ-0038, BQ-0039, BQ-0069, BQ-0070, BQ-0071, BQ-0078, BQ-0079, BQ-0102, BQ-0111, BQ-0113, BQ-0114, BQ-0115, BQ-0116, BQ-0121, BQ-0122, BQ-0124, BQ-0125, BQ-0126, BQ-0127, BQ-0128, BQ-0129, BQ-0130, BQ-0132, BQ-0134, BQ-0135, BQ-0136, BQ-0137, BQ-0138, BQ-0139, BQ-0142, BQ-0145, BQ-0146, BQ-0148, BQ-0150, BQ-0152. DA (14): P1-DA-1 com 8 (D1-01, D1-02, D1-03, D1-04, D1-05, D1-06, D1-07, D1-08); P1-DA-8 com 6 (D4-74, D4-75, D4-76, D4-77, D4-78, D4-79).
(b) Reais de DA: a v1.14 tem itens CEBRASPE_ANALOGA de DA (10 nas folhas), vindos da D1 própria dos 38 itens de banco P1-DA (T-123). Na v1.13 esse valor era 0.
(c) O piso de 10 diretos é decidido para P2 1.x a 3.x (T-107). P1, P2 4.x e DA aparecem com o mesmo cálculo, só para conferência; nas listas, o rótulo "fora do escopo T-107" marca essas folhas.
(d) A coluna "Onda programada" de P1 foi reconstruída a partir de TAREFAS.md: as folhas P1 abaixo de 20 estão na T-99 (onda 5, D-REFORCO-2), que está PENDENTE. Na P1-5.2 (30 itens) há 7 itens L4-R no pacote; TAREFAS.md não os vincula a onda aberta, e a conferência cabe à gcb-gerencia. Para DA, a coluna segue a regra da v1.13 (T-116, D-REFORCO-DA).
(e) Mudanças de total, AUTORAL, reais, diretos, PARCIAIS, VOLÁTEIS ou núcleo de P1 e P2 desde a v1.13: nenhuma.
(f) Folhas P2 1.x a 4.x abaixo de 20: 0. Folhas P1 abaixo de 20: 14. Folhas de DA abaixo de 20: 12; com 20 ou mais: 25 (DA 2.1 = 22, DA 2.2 = 20, DA 3.1 = 20, DA 3.2 = 20, DA 3.3 = 20, DA 3.4 = 20, DA 4.1 = 20, DA 4.2 = 20, DA 4.3 = 20, DA 4.4 = 20, DA 5.1 = 20, DA 5.2 = 20, DA 6.1 = 20, DA 6.2 = 20, DA 6.3 = 20, DA 6.4 = 20, DA 6.5 = 20, DA 7 = 22, DA 8.1 = 20, DA 8.2 = 20, DA 8.3 = 20, DA 8.4 = 20, DA 9.1 = 20, DA 11 = 34, DA 12 = 24).

## P1 — TI (itens 1 a 8; 15 folhas)

| Folha | Total | AUTORAL | Reais | Diretos | PARCIAIS | VOLÁTEIS | Núcleo | Meta 20 | Faltam | Piso 10 diretos | Onda programada |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1-1 | 16 | 10 | 6 | 12 | 4 | 3 | 10 | não | 4 | sim | T-99 (onda 5, D-REFORCO-2; PENDENTE) |
| P1-2.1 | 6 | 4 | 2 | 6 | 0 | 2 | 6 | não | 14 | não (fora do escopo T-107) | T-99 (onda 5, D-REFORCO-2; PENDENTE) |
| P1-3 | 6 | 6 | 0 | 6 | 0 | 2 | 6 | não | 14 | não (fora do escopo T-107) | T-99 (onda 5, D-REFORCO-2; PENDENTE) |
| P1-4.1 | 11 | 4 | 7 | 10 | 1 | 0 | 10 | não | 9 | sim | T-99 (onda 5, D-REFORCO-2; PENDENTE) |
| P1-4.2 | 8 | 3 | 5 | 7 | 1 | 1 | 8 | não | 12 | não (fora do escopo T-107) | T-99 (onda 5, D-REFORCO-2; PENDENTE) |
| P1-4.3 | 6 | 5 | 1 | 6 | 0 | 1 | 6 | não | 14 | não (fora do escopo T-107) | T-99 (onda 5, D-REFORCO-2; PENDENTE) |
| P1-5.1 | 17 | 16 | 1 | 17 | 0 | 0 | 10 | não | 3 | sim | T-99 (onda 5, D-REFORCO-2; PENDENTE) |
| P1-5.2 | 30 | 12 | 18 | 29 | 1 | 0 | 10 | sim | 0 | sim | — |
| P1-5.3 | 15 | 5 | 10 | 14 | 1 | 3 | 10 | não | 5 | sim | T-99 (onda 5, D-REFORCO-2; PENDENTE) |
| P1-6 | 7 | 4 | 3 | 6 | 1 | 0 | 7 | não | 13 | não (fora do escopo T-107) | T-99 (onda 5, D-REFORCO-2; PENDENTE) |
| P1-7.1 | 9 | 4 | 5 | 7 | 2 | 0 | 9 | não | 11 | não (fora do escopo T-107) | T-99 (onda 5, D-REFORCO-2; PENDENTE) |
| P1-8.1 | 7 | 3 | 4 | 5 | 2 | 0 | 7 | não | 13 | não (fora do escopo T-107) | T-99 (onda 5, D-REFORCO-2; PENDENTE) |
| P1-8.2 | 19 | 12 | 7 | 16 | 3 | 0 | 10 | não | 1 | sim | T-99 (onda 5, D-REFORCO-2; PENDENTE) |
| P1-8.3 | 7 | 4 | 3 | 5 | 2 | 6 | 7 | não | 13 | não (fora do escopo T-107) | T-99 (onda 5, D-REFORCO-2; PENDENTE) |
| P1-8.4 | 8 | 7 | 1 | 8 | 0 | 0 | 8 | não | 12 | não (fora do escopo T-107) | T-99 (onda 5, D-REFORCO-2; PENDENTE) |
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

Ordem do edital. Reais e diretos conforme o pacote v1.14 (ressalva (b)).

| Folha | Total | AUTORAL | Reais | Diretos | PARCIAIS | VOLÁTEIS | Núcleo | Meta 20 | Faltam | Piso 10 diretos | Onda programada |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DA 1.1 | 11 | 11 | 0 | 11 | 0 | 0 | 10 | não | 9 | sim | T-116 (D-REFORCO-DA) |
| DA 1.2 | 11 | 11 | 0 | 11 | 0 | 0 | 10 | não | 9 | sim | T-116 (D-REFORCO-DA) |
| DA 2.1 | 22 | 22 | 0 | 22 | 0 | 0 | 10 | sim | 0 | sim | — |
| DA 2.2 | 20 | 20 | 0 | 20 | 0 | 0 | 10 | sim | 0 | sim | — |
| DA 3.1 | 20 | 20 | 0 | 20 | 0 | 1 | 10 | sim | 0 | sim | — |
| DA 3.2 | 20 | 20 | 0 | 20 | 0 | 0 | 10 | sim | 0 | sim | — |
| DA 3.3 | 20 | 20 | 0 | 20 | 0 | 1 | 10 | sim | 0 | sim | — |
| DA 3.4 | 20 | 20 | 0 | 20 | 0 | 0 | 10 | sim | 0 | sim | — |
| DA 4.1 | 20 | 20 | 0 | 20 | 0 | 0 | 10 | sim | 0 | sim | — |
| DA 4.2 | 20 | 20 | 0 | 20 | 0 | 0 | 10 | sim | 0 | sim | — |
| DA 4.3 | 20 | 20 | 0 | 20 | 0 | 0 | 10 | sim | 0 | sim | — |
| DA 4.4 | 20 | 20 | 0 | 20 | 0 | 0 | 10 | sim | 0 | sim | — |
| DA 5.1 | 20 | 20 | 0 | 20 | 0 | 0 | 10 | sim | 0 | sim | — |
| DA 5.2 | 20 | 20 | 0 | 16 | 4 | 0 | 10 | sim | 0 | sim | — |
| DA 6.1 | 20 | 20 | 0 | 12 | 8 | 0 | 10 | sim | 0 | sim | — |
| DA 6.2 | 20 | 20 | 0 | 15 | 5 | 0 | 10 | sim | 0 | sim | — |
| DA 6.3 | 20 | 20 | 0 | 12 | 8 | 0 | 10 | sim | 0 | sim | — |
| DA 6.4 | 20 | 20 | 0 | 14 | 6 | 0 | 10 | sim | 0 | sim | — |
| DA 6.5 | 20 | 20 | 0 | 17 | 3 | 0 | 10 | sim | 0 | sim | — |
| DA 7 | 22 | 20 | 2 | 22 | 0 | 0 | 10 | sim | 0 | sim | — |
| DA 8.1 | 20 | 20 | 0 | 20 | 0 | 0 | 10 | sim | 0 | sim | — |
| DA 8.2 | 20 | 20 | 0 | 20 | 0 | 0 | 10 | sim | 0 | sim | — |
| DA 8.3 | 20 | 20 | 0 | 19 | 1 | 0 | 10 | sim | 0 | sim | — |
| DA 8.4 | 20 | 20 | 0 | 20 | 0 | 0 | 10 | sim | 0 | sim | — |
| DA 9.1 | 20 | 20 | 0 | 20 | 0 | 0 | 10 | sim | 0 | sim | — |
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
| DA 11 | 34 | 30 | 4 | 34 | 0 | 1 | 10 | sim | 0 | sim | — |
| DA 12 | 24 | 20 | 4 | 24 | 0 | 2 | 10 | sim | 0 | sim | — |
| **Soma** | 644 | 634 | 10 | 609 | 35 | 5 | 370 | | | | |

### DA — da folha mais rala para a mais cheia (ordem da D-REFORCO-DA)

Empate de total: ordem do edital. "Faltam para 20" = 20 menos o total, mínimo 0.

| # | Folha | Total | Faltam para 20 | Diretos | VOLÁTEIS | Núcleo |
|---|---|---|---|---|---|---|
| 1 | DA 9.2 | 10 | 10 | 10 | 0 | 10 |
| 2 | DA 9.3 | 10 | 10 | 10 | 0 | 10 |
| 3 | DA 9.4 | 10 | 10 | 10 | 0 | 10 |
| 4 | DA 10.1 | 10 | 10 | 10 | 0 | 10 |
| 5 | DA 10.2 | 10 | 10 | 10 | 0 | 10 |
| 6 | DA 10.3 | 10 | 10 | 10 | 0 | 10 |
| 7 | DA 10.4 | 10 | 10 | 10 | 0 | 10 |
| 8 | DA 10.5 | 10 | 10 | 10 | 0 | 10 |
| 9 | DA 10.6 | 10 | 10 | 10 | 0 | 10 |
| 10 | DA 10.7 | 10 | 10 | 10 | 0 | 10 |
| 11 | DA 1.1 | 11 | 9 | 11 | 0 | 10 |
| 12 | DA 1.2 | 11 | 9 | 11 | 0 | 10 |
| 13 | DA 2.2 | 20 | 0 | 20 | 0 | 10 |
| 14 | DA 3.1 | 20 | 0 | 20 | 1 | 10 |
| 15 | DA 3.2 | 20 | 0 | 20 | 0 | 10 |
| 16 | DA 3.3 | 20 | 0 | 20 | 1 | 10 |
| 17 | DA 3.4 | 20 | 0 | 20 | 0 | 10 |
| 18 | DA 4.1 | 20 | 0 | 20 | 0 | 10 |
| 19 | DA 4.2 | 20 | 0 | 20 | 0 | 10 |
| 20 | DA 4.3 | 20 | 0 | 20 | 0 | 10 |
| 21 | DA 4.4 | 20 | 0 | 20 | 0 | 10 |
| 22 | DA 5.1 | 20 | 0 | 20 | 0 | 10 |
| 23 | DA 5.2 | 20 | 0 | 16 | 0 | 10 |
| 24 | DA 6.1 | 20 | 0 | 12 | 0 | 10 |
| 25 | DA 6.2 | 20 | 0 | 15 | 0 | 10 |
| 26 | DA 6.3 | 20 | 0 | 12 | 0 | 10 |
| 27 | DA 6.4 | 20 | 0 | 14 | 0 | 10 |
| 28 | DA 6.5 | 20 | 0 | 17 | 0 | 10 |
| 29 | DA 8.1 | 20 | 0 | 20 | 0 | 10 |
| 30 | DA 8.2 | 20 | 0 | 20 | 0 | 10 |
| 31 | DA 8.3 | 20 | 0 | 19 | 0 | 10 |
| 32 | DA 8.4 | 20 | 0 | 20 | 0 | 10 |
| 33 | DA 9.1 | 20 | 0 | 20 | 0 | 10 |
| 34 | DA 2.1 | 22 | 0 | 22 | 0 | 10 |
| 35 | DA 7 | 22 | 0 | 22 | 0 | 10 |
| 36 | DA 12 | 24 | 0 | 24 | 2 | 10 |
| 37 | DA 11 | 34 | 0 | 34 | 1 | 10 |
| | **Soma (37 folhas)** | 644 | 118 | 609 | 5 | 370 |

## Listas para o orquestrador (T-95, T-107)

(a) Folhas P1 abaixo de 20 (14): P1-1 (16; faltam 4), P1-2.1 (6; faltam 14), P1-3 (6; faltam 14), P1-4.1 (11; faltam 9), P1-4.2 (8; faltam 12), P1-4.3 (6; faltam 14), P1-5.1 (17; faltam 3), P1-5.3 (15; faltam 5), P1-6 (7; faltam 13), P1-7.1 (9; faltam 11), P1-8.1 (7; faltam 13), P1-8.2 (19; faltam 1), P1-8.3 (7; faltam 13), P1-8.4 (8; faltam 12).
(a2) Folhas P2 1.x a 4.x abaixo de 20: nenhuma.
(a4) Folhas de DA abaixo de 20 (12): DA 9.2 (10; faltam 10), DA 9.3 (10; faltam 10), DA 9.4 (10; faltam 10), DA 10.1 (10; faltam 10), DA 10.2 (10; faltam 10), DA 10.3 (10; faltam 10), DA 10.4 (10; faltam 10), DA 10.5 (10; faltam 10), DA 10.6 (10; faltam 10), DA 10.7 (10; faltam 10), DA 1.1 (11; faltam 9), DA 1.2 (11; faltam 9).
(b) Folhas P1 e P2 com menos de 10 diretos: P1-2.1 (6), P1-3 (6), P1-4.2 (7), P1-4.3 (6), P1-6 (6), P1-7.1 (7), P1-8.1 (5), P1-8.3 (5), P1-8.4 (8), P2-4.1 (9).
(b2) Folhas de DA com menos de 10 diretos (fora do escopo T-107): nenhuma.

FIM — cobertura_v1_14.md
