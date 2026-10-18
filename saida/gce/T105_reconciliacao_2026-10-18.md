# T105_reconciliacao_2026-10-18.md — T-105 — 2026-10-18 — gerado por gce-gerencia

Objeto: reconciliação da T-105 (saldo da onda 3, D-REFORCO-2; 1 item AUTORAL L2-R131 em P2-2.4, em reposição ao L2-R67 retirado, id não reutilizado), ciclo 2026-10-18 s13c1. Lidos: TAREFAS.md (T-105, T-104, T-98, T-107); DECISOES.md (D-GATE-T105, D-T97-META-FUNDADOR-RESP, D-T97-ONDA3-ACEITE, D-ONDA4-FILA); saida/gce/T97_reconciliacao_2026-10-18.md (seções 1, 3, 6, 7 e 8); saldo_v1 e saldo_v2; QA_T105_R1 e QA_T105_R2 (gce-cqfp).

## 1. Histórico das rodadas
- v1 (SHA-256 0dac94cd…9845): REPROVADO na R1 (1/1). O item era gêmeo do L1-R64 (mesma frase-base da página channel-id da AWS). O GATE de 30% foi afastado pelo Fundador (D-GATE-T105): a reprovação é comum, e a v2 sai com ponto novo e QA normal.
- v2 (SHA-256 22e4c1e2fe47fdcf02c215447a00b79026131678ff9db8991c7b25c1fcaf0888): APROVADO na R2 (0/1, 0%), sem ajuste de texto. Ponto: o elemento audio_segments da saída em lote do Amazon Transcribe registra trechos de fala contínua, e não as pausas. Formato PC; E [TS] de troca única; aderência DIRETA; não VOLÁTIL. A base (how-input.html, SHA-256 79c5144d…1eeb) foi reaberta pela QA em 18/10/2026. A busca de gêmeos foi feita por script pela produção e repetida pela QA: 0 acertos.

## 2. D1: versão final = v2, sem v3
- O final é saida/gce/L2_reforco_onda3_saldo_v2.md. Enunciado, gabarito, [TS], formato e aderência não mudam. As correções abaixo valem só para a Parte 1 (registro) e prevalecem sobre ela na consolidação (precedente D-T89-R1-ACEITE, como na T97_reconciliacao). Por isso não se faz v3 de transcrição.
- Tabela de Correções (registro, sem efeito no item):

| # | local na v2 | está | correto | origem |
|---|---|---|---|---|
| 1 | Parte 1, linha de estilo após 1.5 | "item de 58 palavras" | enunciado de 50 palavras | QA_T105_R2, registro 1 |
| 2 | Parte 1, 1.5, linha de formatos de P2-2.4 | SH 5, TS 5, AP 4, PC 4, D 1, NP 1 | SH 5, TS 4, AP 4, PC 4, D 2, NP 1 (maior 25%, SH) | conferência da Gerência: a v2 partiu da recontagem da R1, que já incluía o R131 v1 como TS, e somou outra vez. A base é a T97_reconciliacao, seção 7 (19 itens: SH5 TS4 AP4 PC3 D2 NP1), mais o R131 em PC |
| 3 | Parte 3, "Dúvidas", item 2 | "TS 6/20 (30%)" na leitura alternativa | TS 5/20 (25%) | decorre do #2. A dúvida fica sem objeto, porque a QA leu PC |

## 3. Contagens finais
- P2-2.4: de 19 para 20 itens (meta de 20 cumprida). Gabarito 10 C / 10 E. Formatos SH5 TS4 AP4 PC4 D2 NP1, com o maior em 25% (teto de 30% cumprido). VOLÁTIL 3/20 (15%; R07, R61, R66). Diretas 11/20 e PARCIAIS 9/20: o piso de 10 diretas da D-T97-META-FUNDADOR-RESP fica cumprido.
- Onda 3 (T-97 + T-105): 112 itens (L2-R19 a L2-R131, sem L2-R67). Gabarito 56 C / 56 E (50,0%, dentro da faixa de 40% a 60%). [TS] 70/112 (62,5%; meta de 58). VOLÁTEIS novos: 18, sem mudança. PARCIAIS novos: 43, sem mudança.
- Folhas 2.x: 160 itens (todas com 20); diretas 114/160.
- Pacote v1.10: 557 + 1 = 558 itens, se a Presidência aceitar antes da geração final da T-104. Do contrário, o item vai à v1.11 sem reabrir a v1.10 (linha da T-105; D-ONDA4-FILA).

## 4. D1: registros para a GBQ e para a onda 4
- Proximidade L2-R131 × L2-R68: relação fala × silêncio na saída do ASR, com fornecedores e campos distintos. Não são gêmeos. Na montagem, os dois não ficam no mesmo simulado nem no mesmo caderno. Passa a ser a 12ª proximidade da lista da T97_reconciliacao, seção 6.
- CONFERÊNCIA DE BASE (4–8/1/2027): reabrir how-input.html, conferir os três trechos literais da Parte 3 e comparar o SHA-256. O item não é VOLÁTIL.
- Estilo: o L2-R131 entra na amostra do gbq-estilo da onda 4 (T-98, saida/banco/estilo_onda_4.md) como item fixo, fora do sorteio, sem contar nele e não condicionante, com o registro "L2-R131 — saldo da onda 3". Precedente: L1-R131 na onda 3 (T97_reconciliacao, seção 8).
- T-107: a folha 2.4 sai da condição de "no piso" (10/19) e passa a 11/20.

## 5. Estado da T-105 (texto para TAREFAS.md)
CONCLUÍDA (18/10/2026, s13c1): L2-R131 v2 em P2-2.4 (E [TS], PC, DIRETA, não VOLÁTIL; base AWS how-input, verificada em 18/10/2026); v1 REPROVADO na R1 (gêmeo do L1-R64; D-GATE-T105); v2 APROVADO na R2 (0%); final saldo_v2 (SHA-256 22e4c1e2…0888), sem v3, com a Tabela de Correções de registro da T105_reconciliacao; 2.4 de 19 para 20 (10 C / 10 E; 11 diretas); onda 3 com 112 itens, 56 C / 56 E e [TS] 70; gatilho A emitido; estilo: item fixo na onda 4 (T-98); gce-cpp → gce-cqfp → gce-gerencia; saida/gce/L2_reforco_onda3_saldo_v2.md; saida/gce/T105_reconciliacao_2026-10-18.md

## 6. Gatilho (texto para PARA_PRESIDENCIA.md)
GATILHO A | GCE | T-105 — saldo da onda 3 (D-REFORCO-2; D-GATE-T105): 1 item AUTORAL L2-R131 em P2-2.4, que repõe o L2-R67 retirado | saida/gce/L2_reforco_onda3_saldo_v2.md (final; SHA-256 22e4c1e2fe47fdcf02c215447a00b79026131678ff9db8991c7b25c1fcaf0888); saida/gce/QA_T105_R1_2026-10-18_gce-cqfp.md; saida/gce/QA_T105_R2_2026-10-18_gce-cqfp.md; saida/gce/T105_reconciliacao_2026-10-18.md | L2-R131: E [TS], PC, DIRETA, não VOLÁTIL. QA: R1 1/1 reprovado (v1, gêmeo do L1-R64); R2 0/1 (v2, sem ajuste de texto). Gêmeos: 0. Proximidade com o L2-R68 registrada para a GBQ. Folha 2.4: de 19 para 20 itens, 10 C / 10 E, 11 diretas, VOLÁTIL 3/20, maior formato 25%. Onda 3: 112 itens, 56 C / 56 E (50,0%), [TS] 70. Correções de registro (palavras, formatos) só na reconciliação, sem v3. | Pergunta fechada: aceitar o L2-R131 como canônico, para consolidação no pacote v1.10 (T-104), se o aceite vier antes da geração final; senão, na v1.11 — SIM ou NÃO?

## 7. Efeito na T-104 (v1.10)
O gerador_v1_10 está em preparação, e a geração final espera os aceites deste ciclo. Com SIM antes da geração, a T-104 inclui o L2-R131 a partir do saldo_v2, com a Tabela de Correções desta reconciliação prevalecendo sobre a Parte 1. O total fica em 558, com a 2.4 em 20. Campo "nucleo": o R131 não entra entre os 10 primeiros da folha. Com NÃO, ou com aceite depois da geração, o item vai à v1.11 e a 2.4 fica com 19 na v1.10.
