# T102_reconciliacao_2026-10-18.md — T-102 — 2026-10-18 — gerado por gcb-gerencia

Objeto: reconciliação da T-102 (saldo do R4 da onda 1, P1-4.3; D-REFORCO-1). Base: TAREFAS.md (T-102); DECISOES.md (D-FONTE-DATA-ANTERIOR, D-T92-R4-PARCIAL, D-ONDA1-FILA); saida/gcb/T102_D1_2026-10-18.md; saida/gcb/L6B_reforco_onda1_saldo_v1.md (gcb-cpp; SHA-256 1399edfe2d8f5dbd36cff116ab75b1d5aa23143ab7851276703abd3790216e92); saida/gcb/QA_T102_R1_2026-10-18_gcb-cqfp.md (L6B-R01 APROVADO; L6B-R02 APROVADO COM AJUSTE A-1; reprovação 0/2 = 0%; O-1 não bloqueante). Precedente de método: T92_reconciliacao_2026-10-18.md, seções 2 e 8. A GCB não escreve em PARA_PRESIDENCIA.md nem em TAREFAS.md; os textos das seções 4 e 5 são para o orquestrador colar.

## 1. D1 (1) — A-1: APLICADO. Versão final = v2, com texto fixado pela QA
Motivo: o A-1 é de estilo (afirmação única, regra 1 da D-REFORCO-2: um ponto de julgamento por item). O superlativo "o golpe mais abrangente" abre uma segunda proposição, independente da inversão. O texto da QA mantém gabarito (E), [TS] (sim, mesma troca), formato (troca de sujeito), ponto, base, VOLÁTIL (não) e a justificativa da d-G, que já diz "faz do phishing a espécie e do pharming o gênero". A Gerência não reescreve: fixa o texto da QA, literal.

Arquivo de transcrição: saida/gcb/L6B_reforco_onda1_saldo_v2.md (gcb-cpp). É o v1 com SÓ as linhas abaixo trocadas (numeração do v1); todas as demais linhas idênticas.

1.1 Linha 1 →
# L6B_reforco_onda1_saldo_v2.md — T-102 — 2026-10-18 — gerado por gcb-cpp

1.2 Linha 9 (Parte 1, L6B-R01), última célula: "QA: PENDENTE (gcb-cqfp, R1)" → "QA: APROVADO (gcb-cqfp, R1, 18/10/2026)". Restante da linha idêntico.

1.3 Linha 10 (Parte 1, L6B-R02), última célula: "QA: PENDENTE (gcb-cqfp, R1)" → "QA: APROVADO COM AJUSTE (gcb-cqfp, R1, 18/10/2026); ajuste A-1 aplicado no v2". Restante da linha idêntico.

1.4 Linha 31 (Parte 2, enunciado do L6B-R02) → texto exato:
O phishing é um tipo específico de pharming, de modo que o pharming é o gênero e o phishing, uma de suas espécies.

1.5 Linha 40 (Parte 3, L6B-R01): só o trecho "QA: PENDENTE (gcb-cqfp, R1)." → "QA: APROVADO (gcb-cqfp, R1, 18/10/2026)."

1.6 Linha 48 (Parte 3, L6B-R02): só o trecho "QA: PENDENTE (gcb-cqfp, R1)." → "QA: APROVADO COM AJUSTE (gcb-cqfp, R1, 18/10/2026); ajuste A-1 aplicado no v2."

1.7 Conferência do v2 (orquestrador, por diff textual v1 → v2, ou gcb-gerencia): mudam só as linhas 1, 9, 10, 31, 40 e 48, com o texto das seções 1.1 a 1.6. Idêntico: sem R2 (o parecer R1 condiciona R2 a alteração além do texto do A-1) e vale a seção 4, estado final. Divergente: R2 pela gcb-cqfp, última rodada (D-REFORCO-1), restrita ao diff.

## 2. D1 (2) — correção registrada da D1 própria (O-1)
Na T102_D1_2026-10-18.md, seção 3, 1º marcador, a frase "Confronto literal com o PDF oficial na Rodada 2 do mesmo arquivo (R2.2/R2.3; ...; p. 27 para o trecho da seção 2.3.1)" está INEXATA. Leitura corrigida: a Rodada 2 do saida/gcb/lote6_conferencia.md (R2.3, l. 258) confrontou com o PDF só o fragmento "por meio de alterações no serviço de DNS (Domain Name System)" (p. 27). A oração gênero-espécie "Pharming é um tipo específico de phishing" consta, entre aspas, apenas da l. 154 (seção 2.3, amostragem de 5 fontes, leitura bruta da R1, verificado em 09/10/2026, método da l. 13: download direto e "As aspas abaixo são literais da página baixada").
Efeito: nenhum sobre o L6B-R02. A condição (1) da D-FONTE-DATA-ANTERIOR exige trecho literal registrado em proveniência de lote canônico, com URL oficial e data verdadeira; a l. 154 cumpre. A QA conferiu a condição (3) contra a l. 154 (CONFERE). A correção vai declarada no gatilho A. O arquivo da D1 não é reescrito; esta seção é o registro da correção.

## 3. Contagens finais (v2)
- Itens: 2 — L6B-R01 (C; aplicação parlamentar; [TS] não; VOLÁTIL não) e L6B-R02 (E; troca de sujeito; [TS] sim; VOLÁTIL não). C 1 / E 1; [TS] 1; VOLÁTIL 0 (risco alto 0).
- P1-4.3: 4 → 6 (pacote.json v1.8: BQ-0076, 6B-13, 6B-14, 6B-15; meta 6 por folha cumprida). Formatos novos: aplicação parlamentar 1/6, troca de sujeito 1/6; "definição" novo 0 (legado 3/6 não imputado, T92_D1, 2.4). VOLÁTIL na folha 0/6.
- R4 (D-REFORCO-1 = 3): completo — L6A-R01 E (aceito, D-T92-R4-PARCIAL), L6B-R01 C, L6B-R02 E = 1 C / 2 E.
- Onda 1: 50 itens = 48 aceitos + 2 = 24 C / 26 E (48% de C), dentro da faixa de 40% a 60% (D-REFORCO-2, regra 5); contagem da D1 (seção 4), a reconferir pela presidencia no aceite.
- Bases: L6B-R01 aberta em 18/10/2026 (support.microsoft.com, reaberta também pela gcb-cpp e pela QA; trecho literal CONFERE). L6B-R02 por D-FONTE-DATA-ANTERIOR (verificado em 09/10/2026; registro canônico lote6_conferencia.md, l. 154; não reaberta em 18/10/2026 por restrição de rede, confirmada pela QA: código 000). Os dois entram na conferência de base de 4–8/1/2027 (T-11, P1, gcb-cqfp); o L6B-R02 com reabertura obrigatória da URL (condição 4).

## 4. D1 (3) — estado da T-102 (texto para o orquestrador)
Provisório (até a conferência do v2):
EM CURSO (ciclo 2026-10-18 s12c2; QA R1 = 0% — L6B-R01 APROVADO, L6B-R02 APROVADO COM AJUSTE A-1 de estilo; versão final fixada em saida/gcb/T102_reconciliacao_2026-10-18.md, seção 1; aguarda transcrição literal no v2 pela gcb-cpp e conferência por diff; correção O-1 da D1 registrada na seção 2)
Final (v2 conferido como idêntico):
CONCLUÍDA (18/10/2026, s12c2): 2 de 2 itens — L6B-R01 (P1-4.3, C, aplicação parlamentar, não VOLÁTIL) e L6B-R02 (P1-4.3, E, troca de sujeito, [TS], não VOLÁTIL; base D-FONTE-DATA-ANTERIOR, verificado em 09/10/2026); final em saida/gcb/L6B_reforco_onda1_saldo_v2.md; QA R1 0%, A-1 aplicado sem R2; P1-4.3 4 → 6; R4 completo (1 C / 2 E); gatilho A emitido; reconciliação em saida/gcb/T102_reconciliacao_2026-10-18.md
Se o diff divergir: EM CURSO (R2 gcb-cqfp, última rodada, restrita ao diff).

## 5. Gatilho A (para o orquestrador colar em PARA_PRESIDENCIA.md só depois do v2 conferido como idêntico; acrescentar o SHA-256 do v2)
GATILHO A | GCB | T-102 — saldo do R4 da onda 1 (D-REFORCO-1): L6B-R01 e L6B-R02 (P1-4.3; AUTORAL) | final saida/gcb/L6B_reforco_onda1_saldo_v2.md (SHA-256 <a preencher na conferência>); D1 saida/gcb/T102_D1_2026-10-18.md; QA saida/gcb/QA_T102_R1_2026-10-18_gcb-cqfp.md; reconciliação saida/gcb/T102_reconciliacao_2026-10-18.md (diff v1 → v2 só nas linhas 1, 9, 10, 31, 40 e 48) | 2 itens: L6B-R01 C (aplicação parlamentar; [TS] não; base support.microsoft.com, verificado em 18/10/2026, trecho literal) e L6B-R02 E (troca de sujeito; [TS] sim; base D-FONTE-DATA-ANTERIOR: verificado em 09/10/2026, registro canônico lote6_conferencia.md, l. 154, F4; não reaberta em 18/10/2026 por restrição de rede); VOLÁTIL 0; QA independente gcb-cqfp (opus) R1 0/2 reprovados, A-1 de estilo aplicado com o texto exato da QA, sem R2; P1-4.3 4 → 6 (pacote.json v1.8); R4 completo 3 itens = 1 C / 2 E (com o L6A-R01); onda 1 = 50 itens, 24 C / 26 E (48%, regra 5 cumprida); REVERIFICAR dos 2 itens à T-11 (P1, gcb-cqfp), L6B-R02 com reabertura obrigatória da URL. Correções declaradas para auditoria: (i) O-1 — a T102_D1, seção 3, afirmou que a R2 do lote6_conferencia.md confrontou no PDF o trecho da seção 2.3.1; a R2.3 (l. 258) conferiu só o fragmento do DNS; a oração gênero-espécie consta apenas da l. 154 (R1, 09/10/2026), o que basta à condição (1); (ii) a T102_D1, seção 3, corrigiu a T92_D1, 1.2(b): o trecho gênero-espécie é literal no registro de conferência do lote canônico, não só paráfrase nas FONTES; se a Presidência entender que só valem as FONTES do arquivo de produção, o L6B-R02 sai sem outro efeito e o R4 fica em 2 (1 C / 1 E) | Pergunta fechada: a Presidência ACEITA (SIM/NÃO) L6B-R01 e L6B-R02 como canônicos e, como a T-94 já gera a v1.9 sem eles (D-T92-R4-PARCIAL: aceite depois do início da geração → consolidação seguinte), confirma a entrada na v1.10 (SIM), em vez de reabrir a v1.9 (NÃO)?

## 6. Registros
- Nenhum item existente muda. Nenhum GATE (0% < 30%). Sem conflito entre Gerências.
- D-COMPLEMENTOS: nada aberto além do saldo devido. BACKLOG de ferramentas: inalterado.
- Nada vai à plataforma nem à candidata sem gatilho A aceito e exportação pela GBQ.
