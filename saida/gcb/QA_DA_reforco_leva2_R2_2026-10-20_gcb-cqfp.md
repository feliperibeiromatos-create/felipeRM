# QA_DA_reforco_leva2_R2_2026-10-20_gcb-cqfp.md — T-116 — 2026-10-20 — gerado por gcb-cqfp

# PARECER QA R2 (ÚLTIMA RODADA) — LEVA 2 DO REFORÇO DE DA (D-REFORCO-DA) — ciclo s15c4
QA independente (gcb-cqfp, opus). Não produziu o texto revisado e não reescreve itens. Nenhum arquivo de produção foi alterado. Sem commit nem push. Sem leitura externa: bases conferidas no adendo e na cópia de saida/gcb/normativo_cache/. Escopo do R2 (R1, seção 8, item 5): cada AJ literalmente, o substituto D1-R13 por inteiro e só o que a v2 mudou além disso.

## 0. Objeto, entradas e método
| objeto | SHA-256 |
|---|---|
| saida/gcb/DA_reforco_leva2_v2.md (objeto do R2; 30 itens) | 5baec20d81eea47f50e79275375668284d58ff5649f85a06c37552cd0f161bbe |
| saida/gcb/DA_reforco_leva2_v1.md (objeto do R1) | 40f2288a99286e744f48b9bb9d9c6dda45ed96bdf336217955a6f3ffa83ee788 (= R1, seção 1) |
| saida/gcb/QA_DA_reforco_leva2_R1_2026-10-20_gcb-cqfp.md (parecer R1) | eae940796317397ccdfba05187eef039c31f483fdb478be0b329188d3fafea36 |
| saida/gcb/DA_reforco_ficha_2026-10-20.md | 77f2e60af942b004fde8443030ff42c251e45057451f8d03845628f4df6e5639 (= R1) |
| saida/gcb/D1_anexo_N_adendo_2026-10-20.md | cb4d02f9edbd0ec8f20b0bf8dec576868379f05fe1d7c1b6a54540a0177473f9 (= R1) |
| saida/gcb/D3_anexo_N_adendo_2026-10-20.md / D4_anexo_N_adendo_2026-10-20.md | bbfd3eed…a797 / c32f58eb…6fb5 (= R1) |
| saida/gcb/normativo_cache/Decreto_9830_2019_2026-10-20.txt | ae022402edcf1e5dfb951947d3f9c9f4323c957a2adeb7ac87f3601a213fb232 |
| saida/gcb/D1_v2.md (canônicos D1-53 a D1-60) | 63bd27c34baec035dd39904ef565f6b5a662c0a30886a4a3d0b13b8b702e3d56 |

Método (python3 -I, scratchpad da sessão, somente leitura): (a) os 11 AJ foram extraídos por regex do texto do R1 e aplicados por substituição exata à v1 (cada "substituir" com 1 ocorrência na v1 e o "por" com 0); (b) a v1 com os AJ aplicados foi comparada à v2 por id (enunciado da seção 1 e bloco da seção 2) e, nas seções 0 a 2, linha a linha; fora dos itens, diff v1 → v2 das seções 3 a 6 lido por inteiro; (c) o trecho do D1-R13 procurado como subcadeia (espaços normalizados) no adendo do D1 e na cópia do Decreto 9.830; canônicos D1-53 a D1-60 e leva 1 varridos por "9.830"; (d) contagens, formatos, moldura, aderência, abertura × gabarito, [TS] e teste de sequência (regra 6) refeitos do zero sobre os campos da v2.

## 1. Veredito geral
- **APROVADO.**
- Itens alterados na v2: 8 de 8 APROVADOS (7 com AJ + o substituto D1-R13).
- **Taxa de reprovação final: 0/30 = 0%** (v2). Acumulada no rito (R1 + R2): 1 reprovado (D1-R03, substituído) em 31 itens avaliados = 3,2%. Sem GATE.
- Itens APROVADOS no R1 mudados sem pedido: **nenhum** (22 de 22 idênticos, enunciado e bloco).
- Teto do Decreto 9.830 na 2.2 (6 × teto 5 da ficha, seção 8.2, item 5): pendência da GCB (v2, seção 6.4, item 1). **Não afeta a aprovação**: o teto é parâmetro de composição fixado pela GCB, não regra da seção 1 da ficha, e o próprio R1 indicou o A2.2-09 com esse custo. Se a GCB recusar o 6º item, o ponto que substituir o A2.2-09 é item novo e passa por QA próprio (fora desta rodada).

## 2. Ajustes do R1 — conferência literal
| AJ | item / campo | "substituir" na v2 | "por" na v2 | item = v1 + AJ (enunciado e bloco) | veredito |
|---|---|---|---|---|---|
| AJ-1 | D1-R01 / enunciado | 0 | 1 no item (l. 108); 2ª ocorrência só na tabela "Resposta à R1" (l. 13) | idêntico | APLICADO |
| AJ-2 | D1-R04 / enunciado | 0 | 1 (l. 114) | idêntico | APLICADO |
| AJ-3 | D1-R05 / enunciado | 0 | 1 (l. 116) | idêntico (com AJ-4) | APLICADO |
| AJ-4 | D1-R05 / Troca | 0 | 1 no bloco (l. 384); 2ª na "Resposta à R1" (l. 16) | idêntico (com AJ-3) | APLICADO |
| AJ-5 | D1-R09 / enunciado | 0 | 1 (l. 124) | idêntico | APLICADO |
| AJ-6 | D3-R15 / enunciado | 0 | 1 no item (l. 136); 2ª na "Resposta à R1" (l. 18) | idêntico (com AJ-7) | APLICADO |
| AJ-7 | D3-R15 / Justificativa (linha 2) | 0 | 1 (l. 521) | idêntico (com AJ-6) | APLICADO |
| AJ-8 | D3-R19 / enunciado | 0 | 1 (l. 144) | idêntico (com AJ-9) | APLICADO |
| AJ-9 | D3-R19 / Troca | 0 | 1 (l. 587) | idêntico (com AJ-8) | APLICADO |
| AJ-10 | D3-R20 / enunciado | 0 | 1 (l. 146) | idêntico (com AJ-11) | APLICADO |
| AJ-11 | D3-R20 / Justificativa (linha 2) | 0 | 1 no bloco (l. 599); 2ª na "Resposta à R1" (l. 23) | idêntico (com AJ-10) | APLICADO |

Nenhum dos 7 itens com AJ mudou fora do texto do AJ (comparação por id após aplicação simulada: diferença zero). Gabarito, [TS], formato, moldura (S/N e tipo), aderência e abertura dos 7 itens: iguais à v1.

Registros sem AJ (não reprovam; harmonizar na consolidação, T-123, se a GCB quiser): (i) D1-R05, linha "Ponto de julgamento" (resumo) ainda diz "o processo não terá seguimento até a apresentação" — fora do alcance do AJ-3/AJ-4, declarado pela produção (v2, seção 6.2, item 4); a Troca e o enunciado estão corretos; (ii) D1-R01, "Ponto de julgamento" e Justificativa (linha 2) continuam descrevendo a dispensa do § 2º: descrição correta do dispositivo, não do enunciado; não cria pista (fora da versão do estudante).

## 3. Substituto D1-R13 — conferência completa
| verificação | resultado |
|---|---|
| Enunciado | «Segundo o Decreto nº 9.830/2019, configura-se dolo ou erro grosseiro do agente público ainda que não reste comprovada, nos autos do processo de responsabilização, situação ou circunstância fática capaz de caracterizá-los.» |
| Base literal | trecho de 24 palavras («Não será configurado dolo … situação ou circunstância fática»): subcadeia exata do adendo do D1 (seção 4.3, linha do art. 12, § 2º; ponto A2.2-09 na tabela 3.1, "direta (P3)") e da cópia saida/gcb/normativo_cache/Decreto_9830_2019_2026-10-20.txt (1 ocorrência). A parte final do enunciado ("capaz de caracterizá-los") é a da letra ("capaz de caracterizar o dolo ou o erro grosseiro"), na forma da própria linha A2.2-09 do adendo. URL (d9830.htm) e "consulta 20/10/2026" idênticas às do adendo. ≤ 25 palavras. |
| Gabarito | **E confere**: o § 2º diz que não se configura dolo ou erro grosseiro sem a comprovação nos autos; o item afirma que se configura ainda que ela falte. Inversão única de polaridade (E2), literal; sem leitura alternativa que o torne C. |
| Ponto único | sim: um elemento (exigência de comprovação nos autos), um dispositivo (art. 12, § 2º). |
| Pista de forma | nenhuma: sem "Considere que", sem absoluto, sem "pode"; o "não" é conteúdo do dispositivo dentro da concessiva, não negação frontal de cenário (7.4.5). "Segundo o Decreto nº 9.830/2019" na 2.2: 2 C (D1-R02, R08) / 2 E (D1-R10, R13). Concessiva "configura-se … ainda que" na leva: D3-R15 (C, 6.4) e D1-R13 (E, 2.2), 1/1 — sem pista; registro à gbq-estilo (construção repetida em folhas distintas). |
| Pertinência à 2.2 | direta: A2.2-09 é ponto direto do adendo para a 2.2; item declarativo do art. 12 do Decreto (regime de responsabilização por decisões ou opiniões técnicas), mesmo enquadramento do D1-R02 (§ 1º), aprovado no R1. O motivo dos AJ-2/AJ-5 (cena de "conduta" ou "ato" genérico) não se aplica: não há cena. Alerta P3 cumprido: sem moldura, sem afirmar alcance do Decreto ao Legislativo. |
| Não gêmeo | ok: nenhum canônico D1-53 a D1-60 cita o Decreto 9.830 (varredura: 0; D1-57 e D1-58 julgam a LINDB, art. 28, outro dispositivo e outro elemento); leva 1: 0 ocorrências de "9.830"; na leva, D1-R04 (§ 3º, nexo), D1-R09 (§ 5º, montante), D1-R02 (§ 1º), D1-R08 (§ 6º), D1-R10 (art. 17) julgam elementos distintos, e nenhum enunciado deles afirma ou nega a exigência do § 2º (nenhum entrega o gabarito). "Difere de: D1-R04" e nota "não pôr no mesmo simulado" D1-R13 × D1-R04 presentes (bloco e seção 5, nota (s2)), como pedido no R1. |
| Campos da regra 14 | completos: itemEdital P1-DA-2.2; ponto A2.2-09; Formato DEF; Moldura N; Aderência direta; Gabarito E; justificativa em duas linhas; Tipo de base DISPOSITIVO; Base com fonte, URL, data, trecho e nota; Mecanismo E2; Troca; Difere de; Marcas TS=sim (cabeçalho com [TS]), REVERIFICAR=não, VOLÁTIL=não, QA PENDENTE=sim. |
| Posição | 3ª da 2.2 nas seções 1, 2, 3.2 e 4.5 (entre D1-R02 e D1-R04), como o R1 pediu; id D1-R03 não reutilizado. |
| Efeito nas faixas | D1-R03 (E, [TS], declarativo) → D1-R13 (E, [TS], declarativo): sequências de gabarito e [TS] da 2.2 idênticas (CCEEECECCEEC / nnTTTnTnnTTn); abertura × gabarito inalterada; formato SUJ → DEF (2.2 final 6/2/5/1/6/0: DEF 6 e PAR 6 no teto de 6). |
| **Veredito** | **APROVADO** |

## 4. Diff v1 → v2 fora dos itens (todas as mudanças são derivadas e pedidas)
- Seção "Resposta à R1" (nova): item a item; nenhum ponto do R1 não acatado.
- Seção 0: formatos da 2.2 (1/3/5/0/3/0 → 2/2/5/0/3/0) e da leva (6/5/8/0/6/5 → 7/4/8/0/6/5) e nota de mudança; demais colunas iguais.
- 3.2 e 4.5: linha do D1-R03 trocada pela do D1-R13, mesma posição.
- 4.1 e 4.7: 2.2 final 5/3/5/1/6/0 → 6/2/5/1/6/0, "DEF 6 e PAR 6".
- 4.6: conferência com a ficha 29/30 (divergência única: D1-R13, decidida no R1); SUJ, negação frontal, itens do Decreto e trechos atualizados com o D1-R13.
- 4.8 (nova): concentração por norma na 2.2 — Decreto 9.830 6 (teto 5), Lei 14.133 4 (teto 4), Lei 9.784 2.
- 5 e 6: ids, reserva usada (A2.2-09), nota (s) sem "D1-R03 × D1-55", nota (s2) nova, desvio 6.1 único (D1-R13), desvios 6.2 atualizados (D3-R15 eliminado; mecanismos E2 5, E3 2), pendências 6.4 (itens 1 a 9).
- 4.3 (sequência) e 4.4 (moldura e conjuntos): sem mudança, como esperado.
- Linha 1 e última linha: «# DA_reforco_leva2_v2.md — T-116 — 2026-10-20 — gerado por gcb-cpp»; «FIM DA LEVA 02 — REFORÇO DA».

## 5. Contagens e faixas (refeitas do zero sobre a v2)
| conferência | resultado |
|---|---|
| C/E leva | 17 C / 13 E (56,7%) — faixa 12–18: CONFERE |
| C/E por folha | 8.4 leva 6/4, folha 10/10; 2.2 leva 6/6, folha 10/10; 6.4 leva 5/3, folha 8/8 (de 16) — CONFERE |
| Formatos (DEF/SUJ/SIT/NUM/PAR/APL) | leva 7/4/8/0/6/5; 8.4 3/1/2/0/3/1; 2.2 2/2/5/0/3/0 (folha 6/2/5/1/6/0); 6.4 2/1/1/0/0/4 — teto 6 por formato na folha de 20 respeitado (2.2 com DEF e PAR no teto) — CONFERE |
| [TS] | 13 (todos E; 0 C-isca); cabeçalho [TS] × marca TS: 30/30 coerentes — CONFERE |
| Moldura S | leva 2 C / 3 E (D4-R20, D3-R20 / D3-R16, R18, R19); 2.2 0; conjuntos (DA 48/21; D4 K1–K4; D3 8/7) iguais ao R1 — CONFERE |
| Aderência | 28 diretas / 2 parciais (D3-R18, D3-R20); piso de 10 diretos: 8.4 20, 2.2 20, 6.4 14 — CONFERE |
| Abertura × gabarito | "Considere que" 7 C / 6 E; declarativos 10 C / 7 E (iguais ao R1) — CONFERE |
| VOLÁTIL / REVERIFICAR / QA PENDENTE | 0 / 0 / 30 — CONFERE |
| Pontos | 30 códigos distintos; A2.2-01 fora; A2.2-09 não usado em canônico nem na leva 1 — CONFERE |
| Teste de sequência (regra 6) | folhas da leva e leva inteira: gabarito e [TS] passam (corrida máx. 3; alternância máx. 4; nenhum bloco periódico no limite); acumuladas: só os legados registrados no R1 (2.2 alternância 6, posições 1–6; 6.4 gabarito p3 8; 8.4 [TS] p3 9), nenhum com item novo — CONFERE |

## 6. Pendências da GCB (comentário só no que toca a aprovação)
1. Teto do Decreto 9.830 (6 × 5) — não afeta a aprovação (seção 1).
2. Ficha 8.5/8.3.5/8.3.6, faixas de ids do D1 (D1-R14–R22 na 1.1; D1-R23–R31 na 1.2), reserva da 2.2 (sem A2.2-01; A2.2-05 a retirar, sugestão do R1) — não afetam a aprovação.
3. Auditoria de estilo da amostra (saida/banco/estilo_DA_reforco_leva2.md): ausente em disco em 20/10/2026. O D1-R04 está aprovado com o AJ-2; AJ de estilo que vier depois segue o rito da ficha (8.3.8 ou errata, 7.6), decisão da GCB, e não reabre este R2.
4. Errata AJ-E1 (D3-R13, leva 1): CONFERIDA no R1 (seção 6); a v2 não a toca; segue ao gatilho A como item separado.

## 7. Tabela de vereditos (itens alterados na v2)
| id | alteração | veredito R2 |
|---|---|---|
| D1-R01 | AJ-1 (enunciado) | APROVADO |
| D1-R13 | substituto do D1-R03 (A2.2-09; E; [TS]; DEF; posição 3) | APROVADO |
| D1-R04 | AJ-2 (enunciado) | APROVADO |
| D1-R05 | AJ-3 (enunciado), AJ-4 (Troca) | APROVADO (registro i) |
| D1-R09 | AJ-5 (enunciado) | APROVADO |
| D3-R15 | AJ-6 (enunciado), AJ-7 (Justificativa 2) | APROVADO |
| D3-R19 | AJ-8 (enunciado), AJ-9 (Troca) | APROVADO |
| D3-R20 | AJ-10 (enunciado), AJ-11 (Justificativa 2) | APROVADO |
| D1-R03 | retirado (reprovado no R1; id não volta) | — |
| demais 22 | sem alteração | APROVADO (mantido do R1) |

Resultado da leva para a reconciliação: 30 itens aprovados (10 da 8.4, 12 da 2.2, 8 da 6.4). Próximo passo do rito: auditoria de estilo (gbq-estilo) e reconciliação da GCB, com decisão sobre o teto do Decreto 9.830.

FIM DO PARECER QA R2 — LEVA 02 — REFORÇO DA
