# cobertura_v1_10.md — T-95 — 2026-10-18 — gerado por secretaria

Ocorrência v1.10 de D-COBERTURA-AUTO (D-COBERTURA-AUTO-2 para DA) e regra de D-T97-META-FUNDADOR-RESP. Contagem por item-folha do edital (entrada sem subitens; títulos de seção não contam). Meta: 20 por folha, com piso de 10 diretos por folha (D-T97-META-FUNDADOR-RESP; T-107).

**Fontes.** P1 e P2: saida/pacote/pacote.json v1.10 (campos itemEdital, rotulo, aderencia, volatil; pacote.json com mtime 16:19 de 18/10/2026; geração T-104 (fidelidade gbq-cqe ainda pendente) no momento da leitura). Núcleo: saida/pacote/pacote_estudante.json (campo nucleo). DA: D1 canônico saida/gcb/D1_v2.md (60 itens; subitem por item; caput 1.0 fora das folhas); D6 canônico v2.1 saida/gcb/D6_v2_1.md (D-LOTED6-CANONICO; LAI D6-01 a D6-30 em folha 11; LGPD D6-31 a D6-50 em folha 12); banco/banco.csv (delimitador ";", coluna item_edital_camara, anulado, aderencia) e banco/mapeamento_adicional.csv (D-DA-BANCO, 20 linhas em P1-DA-12). Folhas P1 e P2: 15 e 23 entradas sem subitens do edital do pacote. Folhas DA: 37 entradas sem subitens de edital/DA_itens_1_12_P1.md, conferidas em saida/gcb/T95_conferencia_DA_2026-10-18.md (seção 1). Script de contagem: scratchpad (python -I, só leitura).

**Definições.** Total = itens na folha (P1/P2: AUTORAL + reais; DA: AUTORAL + reais válidos, ver D1-b). AUTORAL = rotulo AUTORAL. Reais = rotulo CEBRASPE_ANALOGA (P1/P2) ou banco válido (DA, anuladas excluídas). Diretos e PARCIAIS = campo aderencia dos itens da folha (P1/P2: todos os itens têm o campo; DA: o banco tem o campo, mas os lotes D1 e D6 não declaram aderência, então diretos e PARCIAIS dos itens AUTORAL de DA são n/d). VOLÁTEIS = campo volatil verdadeiro (P1/P2); DA: 0 nos lotes D1 e D6 (VOLÁTIL=não) e nenhuma marca de volatilidade nas observações do banco. Núcleo = nucleo verdadeiro no pacote_estudante (P1/P2); DA: n/d (DA não está no pacote v1.10). Meta 20 cumprida: total >= 20. Piso 10 diretos cumprido: diretos >= 10 (n/d onde a aderência não existe).

**Ressalvas de cobertura.**
(a) Itens com itemEdital de título (não folha) ficam fora das folhas: 13 itens (P1-2: 6, P1-4: 5, P1-5: 2). Itens: BQ-0009, BQ-0011, BQ-0012, BQ-0038, BQ-0039, BQ-0069, BQ-0070, BQ-0071, BQ-0078, BQ-0079, BQ-0102, BQ-0111, 6B-01.
(b) DA: o banco indexa DA por seção (P1-DA-1 a P1-DA-12). Nas seções com uma só folha (7, 11, 12) os reais entram na folha; nas seções com mais de uma folha (1 a 6, 8 a 10) os reais ficam n/d por folha (regra D1-b iii) e o total da folha é só o AUTORAL, com o limite superior somando todo o banco válido da seção. Os 20 itens de mapeamento_adicional entram em DA 12 como parcela adicional (D1-b ii); são linhas do banco indexadas a P2-4.1 e seguem contadas em P2-4.1 (contagem por disciplina, sem soma cruzada).
(c) DA: os 8 itens D1-01 a D1-08 (subitem 1.0, caput do título 1) não são folha; ficam fora das 37 (D1-a) e fora da meta.
(d) O piso de 10 diretos é decidido para P2 1.x a 3.x (T-107). P1, P2 4.x e DA aparecem com o mesmo cálculo, só para conferência; nas listas, o rótulo "fora do escopo T-107" marca essas folhas.
(e) "QA PENDENTE" aparece no texto dos itens de D1_v2.md e D6_v2_1.md; a contagem não usa essa marca e não a altera.

## P1 — TI (itens 1 a 8; 15 folhas)

| Folha | Total | AUTORAL | Reais | Diretos | PARCIAIS | VOLÁTEIS | Núcleo | Meta 20 | Faltam | Piso 10 diretos | Onda programada |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1-1 | 16 | 10 | 6 | 12 | 4 | 3 | 10 | não | 4 | sim | T-99 |
| P1-2.1 | 6 | 4 | 2 | 6 | 0 | 2 | 6 | não | 14 | não | T-99 |
| P1-3 | 6 | 6 | 0 | 6 | 0 | 2 | 6 | não | 14 | não | T-99 |
| P1-4.1 | 11 | 4 | 7 | 10 | 1 | 0 | 10 | não | 9 | sim | T-99 |
| P1-4.2 | 8 | 3 | 5 | 7 | 1 | 1 | 8 | não | 12 | não | T-99 |
| P1-4.3 | 6 | 5 | 1 | 6 | 0 | 1 | 6 | não | 14 | não | T-99 |
| P1-5.1 | 17 | 16 | 1 | 17 | 0 | 0 | 10 | não | 3 | sim | T-99 |
| P1-5.2 | 23 | 5 | 18 | 22 | 1 | 0 | 10 | sim | 0 | sim | — |
| P1-5.3 | 15 | 5 | 10 | 14 | 1 | 3 | 10 | não | 5 | sim | T-99 |
| P1-6 | 7 | 4 | 3 | 6 | 1 | 0 | 7 | não | 13 | não | T-99 |
| P1-7.1 | 9 | 4 | 5 | 7 | 2 | 0 | 9 | não | 11 | não | T-99 |
| P1-8.1 | 7 | 3 | 4 | 5 | 2 | 0 | 7 | não | 13 | não | T-99 |
| P1-8.2 | 19 | 12 | 7 | 16 | 3 | 0 | 10 | não | 1 | sim | T-99 |
| P1-8.3 | 7 | 4 | 3 | 5 | 2 | 6 | 7 | não | 13 | não | T-99 |
| P1-8.4 | 8 | 7 | 1 | 8 | 0 | 0 | 8 | não | 12 | não | T-99 |
| **Soma** | 165 | 92 | 73 | 147 | 18 | 18 | 124 | | | | |

## P2 — RF/IA (itens 1.1 a 4.3; 23 folhas)

| Folha | Total | AUTORAL | Reais | Diretos | PARCIAIS | VOLÁTEIS | Núcleo | Meta 20 | Faltam | Piso 10 diretos | Onda programada |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P2-1.1 | 20 | 20 | 0 | 20 | 0 | 0 | 10 | sim | 0 | sim | — |
| P2-1.2 | 20 | 20 | 0 | 20 | 0 | 0 | 10 | sim | 0 | sim | — |
| P2-1.3 | 20 | 20 | 0 | 20 | 0 | 3 | 10 | sim | 0 | sim | — |
| P2-1.4 | 20 | 20 | 0 | 20 | 0 | 3 | 10 | sim | 0 | sim | — |
| P2-1.5 | 20 | 20 | 0 | 20 | 0 | 3 | 10 | sim | 0 | sim | — |
| P2-1.6 | 20 | 20 | 0 | 20 | 0 | 1 | 10 | sim | 0 | sim | — |
| P2-1.7 | 20 | 20 | 0 | 20 | 0 | 3 | 10 | sim | 0 | sim | — |
| P2-1.8 | 20 | 20 | 0 | 20 | 0 | 2 | 10 | sim | 0 | sim | — |
| P2-2.1 | 20 | 20 | 0 | 10 | 10 | 2 | 10 | sim | 0 | sim | — |
| P2-2.2 | 20 | 20 | 0 | 13 | 7 | 1 | 10 | sim | 0 | sim | — |
| P2-2.3 | 20 | 20 | 0 | 10 | 10 | 3 | 10 | sim | 0 | sim | — |
| P2-2.4 | 20 | 20 | 0 | 11 | 9 | 3 | 10 | sim | 0 | sim | — |
| P2-2.5 | 20 | 20 | 0 | 17 | 3 | 4 | 10 | sim | 0 | sim | — |
| P2-2.6 | 20 | 20 | 0 | 16 | 4 | 3 | 10 | sim | 0 | sim | — |
| P2-2.7 | 20 | 20 | 0 | 18 | 2 | 0 | 10 | sim | 0 | sim | — |
| P2-2.8 | 20 | 20 | 0 | 19 | 1 | 4 | 10 | sim | 0 | sim | — |
| P2-3.1 | 6 | 6 | 0 | 4 | 2 | 0 | 6 | não | 14 | não | T-98 |
| P2-3.2 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | não | 14 | não | T-98 |
| P2-3.3 | 6 | 6 | 0 | 5 | 1 | 0 | 6 | não | 14 | não | T-98 |
| P2-3.4 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | não | 14 | não | T-98 |
| P2-4.1 | 26 | 5 | 21 | 5 | 21 | 1 | 10 | sim | 0 | não | — |
| P2-4.2 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | não | 14 | não | T-98 |
| P2-4.3 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | não | 14 | não | T-98 |
| **Soma** | 382 | 361 | 21 | 312 | 70 | 36 | 206 | | | | |

## DA — Noções de Direito Administrativo (37 folhas de edital/DA_itens_1_12_P1.md)

| Folha | Total | AUTORAL (lote) | Reais (banco válido) | Diretos | PARCIAIS | VOLÁTEIS | Núcleo | Meta 20 | Faltam | Piso 10 diretos | Onda programada |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DA 1.1 | 11 (mín.; máx. 15) | 11 | n/d (seção P1-DA-1: 4 válidas) | n/d | n/d | 0 | n/d | não | 9 | n/d | T-100 (DA) |
| DA 1.2 | 11 (mín.; máx. 15) | 11 | n/d (seção P1-DA-1: 4 válidas) | n/d | n/d | 0 | n/d | não | 9 | n/d | T-100 (DA) |
| DA 2.1 | 22 (mín.; máx. 25) | 22 | n/d (seção P1-DA-2: 3 válidas) | n/d | n/d | 0 | n/d | sim | 0 | n/d | — |
| DA 2.2 | 8 (mín.; máx. 11) | 8 | n/d (seção P1-DA-2: 3 válidas) | n/d | n/d | 0 | n/d | não | 12 | n/d | T-100 (DA) |
| DA 3.1 | 0 (mín.; máx. 5) | 0 | n/d (seção P1-DA-3: 5 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-75 (D2) |
| DA 3.2 | 0 (mín.; máx. 5) | 0 | n/d (seção P1-DA-3: 5 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-75 (D2) |
| DA 3.3 | 0 (mín.; máx. 5) | 0 | n/d (seção P1-DA-3: 5 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-75 (D2) |
| DA 3.4 | 0 (mín.; máx. 5) | 0 | n/d (seção P1-DA-3: 5 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-75 (D2) |
| DA 4.1 | 0 (mín.; máx. 4) | 0 | n/d (seção P1-DA-4: 4 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-75 (D2) |
| DA 4.2 | 0 (mín.; máx. 4) | 0 | n/d (seção P1-DA-4: 4 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-75 (D2) |
| DA 4.3 | 0 (mín.; máx. 4) | 0 | n/d (seção P1-DA-4: 4 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-75 (D2) |
| DA 4.4 | 0 (mín.; máx. 4) | 0 | n/d (seção P1-DA-4: 4 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-75 (D2) |
| DA 5.1 | 0 (mín.; máx. 3) | 0 | n/d (seção P1-DA-5: 3 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-76 (D3) |
| DA 5.2 | 0 (mín.; máx. 3) | 0 | n/d (seção P1-DA-5: 3 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-76 (D3) |
| DA 6.1 | 0 (mín.; máx. 1) | 0 | n/d (seção P1-DA-6: 1 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-76 (D3) |
| DA 6.2 | 0 (mín.; máx. 1) | 0 | n/d (seção P1-DA-6: 1 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-76 (D3) |
| DA 6.3 | 0 (mín.; máx. 1) | 0 | n/d (seção P1-DA-6: 1 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-76 (D3) |
| DA 6.4 | 0 (mín.; máx. 1) | 0 | n/d (seção P1-DA-6: 1 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-76 (D3) |
| DA 6.5 | 0 (mín.; máx. 1) | 0 | n/d (seção P1-DA-6: 1 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-76 (D3) |
| DA 7 | 3 | 0 | 3 (+1 anulada) | 3 | 0 | 0 | n/d | não | 17 | não | T-76 (D3) |
| DA 8.1 | 0 (mín.; máx. 1) | 0 | n/d (seção P1-DA-8: 1 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-77 (D4) |
| DA 8.2 | 0 (mín.; máx. 1) | 0 | n/d (seção P1-DA-8: 1 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-77 (D4) |
| DA 8.3 | 0 (mín.; máx. 1) | 0 | n/d (seção P1-DA-8: 1 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-77 (D4) |
| DA 8.4 | 0 (mín.; máx. 1) | 0 | n/d (seção P1-DA-8: 1 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-77 (D4) |
| DA 9.1 | 0 (mín.; máx. 2) | 0 | n/d (seção P1-DA-9: 2 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-77 (D4) |
| DA 9.2 | 0 (mín.; máx. 2) | 0 | n/d (seção P1-DA-9: 2 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-77 (D4) |
| DA 9.3 | 0 (mín.; máx. 2) | 0 | n/d (seção P1-DA-9: 2 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-77 (D4) |
| DA 9.4 | 0 (mín.; máx. 2) | 0 | n/d (seção P1-DA-9: 2 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-77 (D4) |
| DA 10.1 | 0 (mín.; máx. 4) | 0 | n/d (seção P1-DA-10: 4 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-74 (D5) |
| DA 10.2 | 0 (mín.; máx. 4) | 0 | n/d (seção P1-DA-10: 4 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-74 (D5) |
| DA 10.3 | 0 (mín.; máx. 4) | 0 | n/d (seção P1-DA-10: 4 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-74 (D5) |
| DA 10.4 | 0 (mín.; máx. 4) | 0 | n/d (seção P1-DA-10: 4 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-74 (D5) |
| DA 10.5 | 0 (mín.; máx. 4) | 0 | n/d (seção P1-DA-10: 4 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-74 (D5) |
| DA 10.6 | 0 (mín.; máx. 4) | 0 | n/d (seção P1-DA-10: 4 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-74 (D5) |
| DA 10.7 | 0 (mín.; máx. 4) | 0 | n/d (seção P1-DA-10: 4 válidas) | n/d | n/d | 0 | n/d | não | 20 | n/d | T-74 (D5) |
| DA 11 | 34 | 30 | 4 | n/d (banco: 4) | n/d (banco: 0) | 0 | n/d | sim | 0 | n/d | — |
| DA 12 | 44 | 20 | 24 (4 banco + 20 adicional D-DA-BANCO) | n/d (banco: 24) | n/d (banco: 0) | 0 | n/d | sim | 0 | n/d | — |
| **Soma (37 folhas)** | | 102 | 31 nas folhas 7, 11, 12 (demais n/d) | | | 0 | n/d | | | | |

DA 1 (caput; não é folha) = 8 (D1-01 a D1-08), fora das 37 e da meta (D1-a).

Adicional de DA 12 (mapeamento_adicional.csv, D-DA-BANCO): 20 direta(s), 0 parcial(is); ids distintos dos do banco; nenhum anulado.

## Listas para o orquestrador (T-95, T-107)

(a) Folhas abaixo de 20 fora de onda programada (lista do orquestrador): nenhuma.
(a2) Folhas P2 1.x e 2.x abaixo de 20 de T-96/T-97 (concluídas; fora da lista do orquestrador): nenhuma.
(a3) DA: folhas abaixo de 20 todas cobertas por T-100 (BACKLOG) e, para 3 a 10, por T-74 a T-77: 34 folhas abaixo de 20, nenhuma fora de onda.
(b) Folhas com menos de 10 diretos, P1 e P2 (diretos conhecidos): P1-2.1 (6; fora do escopo T-107), P1-3 (6; fora do escopo T-107), P1-4.2 (7; fora do escopo T-107), P1-4.3 (6; fora do escopo T-107), P1-6 (6; fora do escopo T-107), P1-7.1 (7; fora do escopo T-107), P1-8.1 (5; fora do escopo T-107), P1-8.3 (5; fora do escopo T-107), P1-8.4 (8; fora do escopo T-107), P2-3.1 (4), P2-3.2 (6), P2-3.3 (5), P2-3.4 (6), P2-4.1 (5; fora do escopo T-107), P2-4.2 (6; fora do escopo T-107), P2-4.3 (6; fora do escopo T-107).
(b2) DA com diretos conhecidos (folhas só com banco): DA 7 (banco 3 direta(s)).
(b3) DA com AUTORAL e sem aderência declarada (diretos n/d): 6 folhas; com piso não verificável. Folhas multi-seção (n/d): DA 2.2, DA 3.1, DA 3.2, DA 3.3, DA 3.4, DA 4.1, DA 4.2, DA 4.3, DA 4.4, DA 5.1, DA 5.2, DA 6.1, DA 6.2, DA 6.3, DA 6.4, DA 6.5, DA 8.1, DA 8.2, DA 8.3, DA 8.4, DA 9.1, DA 9.2, DA 9.3, DA 9.4, DA 10.1, DA 10.2, DA 10.3, DA 10.4, DA 10.5, DA 10.6, DA 10.7.

Ondas (T-98 P2 3.1–3.4, 4.2, 4.3; T-99 P1 abaixo de 20; T-100 DA; T-74 D5; T-75 a T-77 D2, D3, D4) conforme TAREFAS.md. Esta contagem não escreve em PARA_PRESIDENCIA.md.

FIM — cobertura_v1_10.md
