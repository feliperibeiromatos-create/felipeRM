# T93_reconciliacao_2026-10-18.md — T-93 — 2026-10-18 — gerado por gbq-gerencia

REMETENTE: gbq-gerencia (reconciliação e D1; não produz nem revisa item).
DESTINATÁRIO: orquestrador (estado da T-93 em TAREFAS.md; a D-ONDA1-FILA (2) libera a T-94). Cópia: gbq-estilo; gce-gerencia e gcb-gerencia (registros para a onda 2, T-96).
Base: `saida/banco/estilo_onda_1.md` (gbq-estilo, ciclo 2026-10-18 s12c2); D-REFORCO-2 (regras 5 e 6); D-T89-R1-ACEITE, D-T90-R2-ACEITE, D-T91-R3-ACEITE, D-T92-R4-PARCIAL; D-ONDA1-FILA; `regras/estilo_banca.md` v1.1.3.

## 0. Conferência própria da GBQ (python3 -I, somente leitura)

| Ponto | Relato do gbq-estilo | Conferência da GBQ | Confere |
|---|---|---|---|
| Universo | 48 itens aceitos (L1 18, L2 18, L3 11, L6A 1); L6B-R01/R02 fora (SUSPENSOS) | 48 ids lidos dos 4 arquivos finais, com os SHA-256 das decisões de aceite (gerador_v1_9/reforco.py) | sim |
| Tamanho da amostra | 10% de 48 = 4,8 → 5 (mínimo da T-93), com ao menos 1 de cada lote R1–R4 | 5 itens, um de cada lote e um quinto de L1–L3 | sim |
| Sorteio | `random.Random(20261018).choice`, L1, L2, L3 e depois os 44 restantes; L6A-R01 por obrigação | reproduzido: L1-R07, L2-R11, L3-R02 e L2-R14 (44 restantes) | sim |
| Vereditos | 5/5 APROVADOS; 0% de reprovação; sem GATE | li os 5 enunciados e gabaritos nos arquivos finais: comando, ponto único, mecanismo e [TS] coerentes com o relato; nenhum motivo de reprovação | sim |
| Faixa de C (regra 5) | 23 C / 25 E = 47,9% | 23 C / 25 E pela Parte 3 dos 4 arquivos (L1 9/9, L2 8/10, L3 6/5, L6A 0/1); [TS] 23 (7, 10, 5, 1) | sim |
| Faixa com a T-102 | 46,0% a 50,0% com os 2 itens de L6B, qualquer gabarito | 23/50, 24/50, 25/50 | sim |

## 1. D1 — aceite

**D-RT93-01 — ACEITE do relatório, sem GATE.** A auditoria cumpre a regra 6 da D-REFORCO-2 (10% da onda, mínimo de 5, ao menos 1 de cada lote R1 a R4), com sorteio reproduzível. A reprovação é 0/5 (0%), abaixo do gate de 30%. A faixa de C da onda (regra 5) está cumprida: 47,9%. Nenhum item aceito muda, e nenhuma observação toca gabarito, [TS], VOLÁTIL ou aderência. A T-93 fica CONCLUÍDA, e pela D-ONDA1-FILA (2) a T-94 passa a AGORA. A faixa é reconferida no gatilho A da T-102, como manda a D-T92-R4-PARCIAL.

**D-RT93-02 — Natureza das observações.** As observações das seções 2 e 4 do relatório são de estilo, valem para a produção das ondas seguintes e não são ressalva sobre o objeto aceito. Os mecanismos atribuídos pelo gbq-estilo (C3, E3, E4, E5) são julgamento do auditor e ficam registrados como tais; a GBQ não os usa para reclassificar formato (o formato de cada item é o do mapa canônico, D-T91-R3-ACEITE, critério 3.1).

## 2. Registros para a onda 2 (T-96) e seguintes

Valem para gce-cpp e gcb-cpp na produção e para gce-cqfp e gcb-cqfp na QA, como critério de estilo. Não são regra nova de reprovação: um item que não os siga não é reprovado só por isso.

| # | Registro | Origem |
|---|---|---|
| O-1 | **Extensão.** Na onda 1, os itens C são mais longos que os E (média de 49,6 contra 40,4 palavras), o inverso da base (31,6 contra 34,7). Na onda 2, encurtar os C e escrever alguns E longos, para que a extensão não vire pista. Item C acima de 65 palavras (o máximo de C da base) só em situação hipotética com duas frases. Na onda 1, isso aconteceu em L2-R10 (76) e L2-R11 (68). | relatório, 2 e 4 |
| O-2 | **"independe".** Na onda 1, aparece só em E (3 casos: L1-R01, L1-R11, L2-R05). Escrever ao menos um C com "independe" ou "independentemente". | relatório, 4 |
| O-3 | **Possibilidade afirmativa.** "pode/podem/poderá" aparece em 8 C e 3 E, viés parecido com o da base. Seguir a seção 5.1 do guia e usar "pode" também em E. | relatório, 4 |
| O-4 | **Remissão à norma.** Depois de "Segundo o RICD" (ou de outra norma), não pôr na mesma oração um vínculo que a norma não traz. No L3-R02, a oração sobre inteligência artificial ficou dentro da remissão. Pôr esse vínculo fora do escopo da remissão, em frase própria ou no texto-base. | relatório, 2 (L3-R02) |
| O-5 | **Cauda que se denuncia.** Evitar cauda falsa cuja redação seja quase autocontraditória, como "exercer, em lugar do fiscal, as atribuições próprias e exclusivas". O mecanismo E5 continua válido; prefira a paráfrase que não entregue o erro, desde que o sentido da lei fique intacto. | relatório, 2 (L2-R14) |
| O-6 | **[TS] em item C.** A convenção "espelho" da GCE (falsa pegadinha marcada [TS]) continua admitida, como na onda 1 (L1-R07, L2-R02). Ela não é exigida nem proibida pelo guia (seção 5.1). | relatório, 2 e 4 |
| O-7 | **Restritivos e causais.** Manter a distribuição da onda 1: restritivos também em C ("apenas", "somente") e causa não presa a E. | relatório, 4 |
| O-8 | **Concessiva.** "ainda que" aparece só em C (n pequeno). Admitir concessiva em E na onda 2. | relatório, 4 |

Pela regra 6 da D-REFORCO-2, o gbq-estilo audita a onda 2 com estes registros entre os critérios. Uma atualização de `regras/estilo_banca.md` (v1.1.4) que os incorpore fica como opção da GBQ numa tarefa própria. Ela não é aberta por esta reconciliação.

## 3. Estado da T-93 (texto para TAREFAS.md)

T-93; GBQ; ESTILO — auditoria da onda 1 do reforço (D-REFORCO-2, regra 6): o gbq-estilo audita 10% dos itens de reforço da onda 1 aceitos (no mínimo 5 dos 50, com ao menos 1 de cada um dos lotes R1, R2, R3 e R4), confere a faixa de 40% a 60% de C da onda (regra 5) e grava saida/banco/estilo_onda_1.md; reprovação acima de 30% = GATE; depois das reconciliações das T-89 a T-92 e antes da consolidação da v1.9; AGORA (D-REFORCO-2); CONCLUÍDA (ciclo 2026-10-18 s12c2; amostra 5/48 sorteada com semente 20261018 e reproduzida pela GBQ; 5 APROVADOS, 0% de reprovação, sem GATE; onda 23 C / 25 E = 47,9%, na faixa; reconciliada pela GBQ, D-RT93-01 e 02, com os registros O-1 a O-8 para a onda 2 (T-96); a faixa é reconferida no gatilho A da T-102; a T-94 passa a AGORA, D-ONDA1-FILA (2)); gbq-estilo → gbq-gerencia; saida/banco/estilo_onda_1.md, saida/banco/T93_reconciliacao_2026-10-18.md

## 4. Gatilhos

Nenhum. A T-93 não tem gatilho próprio. A média real de itens por ciclo da onda 1 (D-REFORCO-2) vai no gatilho A da T-94, como manda a D-ONDA1-FILA (5).
