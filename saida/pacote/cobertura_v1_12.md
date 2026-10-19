# cobertura_v1_12.md — T-95 — 2026-10-19 — gerado por secretaria

Ocorrência v1.12 de D-COBERTURA-AUTO e regra de D-T97-META-FUNDADOR-RESP. Contagem por item-folha do edital (entrada sem subitens; títulos de seção não contam). Meta: 20 por folha, com piso de 10 diretos por folha (D-T97-META-FUNDADOR-RESP; T-107). Formato igual ao de cobertura_v1_11.md.

**Fontes.** P1 e P2: saida/pacote/pacote.json v1.12 (geradoEm 2026-10-18; 749 itens; SHA-256 3476525319b027fe4427bf93598d516087ad6f18fb8dd5bbed4ad8c04be6024f; campos itemEdital, rotulo, aderencia, volatil). Núcleo: saida/pacote/pacote_estudante.json v1.12-E (SHA-256 23224c96b4189097012f139f52a9b995c29d930c6ac72801659720d6db612abd; campo nucleo, por id). Folhas: 38 entradas do edital do pacote sem subitens (15 P1 e 23 P2). DA: o pacote.json v1.12 não contém itens de DA. Contagem feita por script em modo isolado (python -I, só leitura), no scratchpad da Secretaria.

**Definições.** Total = itens na folha (AUTORAL + CEBRASPE_ANALOGA). AUTORAL = rotulo AUTORAL. Reais = rotulo CEBRASPE_ANALOGA. Diretos e PARCIAIS = campo aderencia ("direta" e "parcial"). VOLÁTEIS = campo volatil verdadeiro. Núcleo = nucleo verdadeiro no pacote_estudante. Meta 20 cumprida: total >= 20. Piso 10 diretos cumprido: diretos >= 10.

**Totais de conferência.** 749 itens no pacote; 736 em folhas; 13 fora das folhas (ressalva (a)). Gabarito: 380 C e 369 E (conferido no pacote). AUTORAL nas folhas: 642; Reais nas folhas: 94; Diretos: 642; PARCIAIS: 94; VOLÁTEIS: 86; Núcleo: 354.

**Ressalvas de cobertura.**
(a) Itens com itemEdital de título (não folha) ficam fora das folhas: 13 itens: 6B-01, BQ-0009, BQ-0011, BQ-0012, BQ-0038, BQ-0039, BQ-0069, BQ-0070, BQ-0071, BQ-0078, BQ-0079, BQ-0102, BQ-0111.
(b) DA não recontada: o pacote.json v1.12 não contém itens de DA. Os valores de DA são os de cobertura_v1_11.md (seção DA), sem nova contagem nesta ocorrência.
(c) O piso de 10 diretos é decidido para P2 1.x a 3.x (T-107). P1, P2 4.x aparecem com o mesmo cálculo, só para conferência; nas listas, o rótulo "fora do escopo T-107" marca essas folhas.
(d) A coluna "Onda programada" não foi reconstruída nesta ocorrência (n/r); a programação das ondas está em TAREFAS.md.
(e) Mudanças de total desde a v1.11 (total v1.11 → v1.12): P1-5.2 de 23 para 30; P2-1.1 de 20 para 29; P2-1.2 a P2-1.8 de 20 para 30; P2-2.1 de 20 para 27; P2-2.2 de 20 para 21; P2-2.8 de 19 para 20; P2-3.1 de 7 para 27; P2-3.2, P2-3.3 e P2-3.4 de 6 para 20; P2-4.1 de 26 para 30; P2-4.2 e P2-4.3 de 6 para 20. As demais folhas mantêm o total da v1.11.
(f) Folhas P2 1.x a 4.x: nenhuma abaixo de 20. As folhas P1 abaixo de 20 são 14 (lista (a)).

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

## DA — Noções de Direito Administrativo

Não recontado nesta ocorrência: o pacote.json v1.12 não contém itens de DA. Valores de DA: cobertura_v1_11.md, seção DA (ressalva (b)).

## Listas para o orquestrador (T-95, T-107)

(a) Folhas P1 abaixo de 20 (14; a programação de onda não foi reconstruída, ressalva (d)): P1-1 (16; faltam 4), P1-2.1 (6; faltam 14), P1-3 (6; faltam 14), P1-4.1 (11; faltam 9), P1-4.2 (8; faltam 12), P1-4.3 (6; faltam 14), P1-5.1 (17; faltam 3), P1-5.3 (15; faltam 5), P1-6 (7; faltam 13), P1-7.1 (9; faltam 11), P1-8.1 (7; faltam 13), P1-8.2 (19; faltam 1), P1-8.3 (7; faltam 13), P1-8.4 (8; faltam 12).
(a2) Folhas P2 1.x a 4.x abaixo de 20: nenhuma.
(a3) Folhas que atingiram 30 itens (9): P1-5.2 (30); P2-1.2 a P2-1.8 (30 cada); P2-4.1 (30).
(b) Folhas com menos de 10 diretos (todas fora do escopo T-107): P1-2.1 (6), P1-3 (6), P1-4.2 (7), P1-4.3 (6), P1-6 (6), P1-7.1 (7), P1-8.1 (5), P1-8.3 (5), P1-8.4 (8), P2-4.1 (9). Nas folhas P2 1.x a 3.x, nenhuma.
(b2) DA: ver cobertura_v1_11.md (não recontado).

FIM — cobertura_v1_12.md
