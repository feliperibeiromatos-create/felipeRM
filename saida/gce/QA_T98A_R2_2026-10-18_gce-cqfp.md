# QA_T98A_R2_2026-10-18_gce-cqfp.md — T-98 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L3_reforco_onda4_A_v2.md (gce-cpp; 28 itens AUTORAL L3-R12 a L3-R39; P2-3.1 = R12–R25, P2-3.2 = R26–R39). Rodada R2, a última permitida. Revisora: gce-cqfp (opus; não produziu). O arquivo de produção não foi alterado e não houve commit.
Lidos: meu parecer QA_T98A_R1_2026-10-18_gce-cqfp.md; QA_T98AC_normativo_2026-10-18_qa-normativo.md; A_v1 e A_v2 (diff integral das Partes 1 a 3); edital/modulo_RF_IA_P2.md (1.8, 3.1, 3.3); DECISOES.md (D-REFORCO-2, D-T97-META-FUNDADOR-RESP, D-ADERENCIA, D-T96-ONDA2-ACEITE (II)); T97_reconciliacao (3.3, 3.4); QA_T105_R2 (precedente de aderência de item com base de fornecedor); pacote.json v1.10 (560 itens); L3_reforco_onda4_B_v2.md, C_v1.md e C_v2.md (só para gêmeos).

## 1. Diff v1 → v2

Rodei um diff integral das Partes 1 a 3. Só mudam: o L3-R12 (substituído, no mapa, no enunciado e na Parte 3); os rótulos de VOLÁTIL e de aderência de R13, R14 e R16; o "ela" → "ele" do R36; e as contagens e a proveniência que decorrem disso. Nenhum outro enunciado, gabarito, [TS] ou formato mudou. A Parte 2 não traz marca (sem gabarito, [TS], VOLÁTIL ou REVERIFICAR). Os 28 ids estão na mesma ordem nas Partes 2 e 3. "FIM DO LOTE" está presente.

## 2. Ajustes do R1: conferência

| item | pedido no R1 | aplicado na v2 | veredito |
|---|---|---|---|
| L3-R12 | REPROVADO: repor por 1 item direto da 3.1, de formato diferente de SH, de preferência E, sobre sumarização ou transcrição, sem gêmeo | Item novo em D, E [TS], sobre sumarização (Amazon Transcribe) | ver seção 3 |
| L3-R13 | VOLÁTIL baixo + aderência PARCIAL | Ambos aplicados, com REVERIFICAR em 4–8/1/2027 e "Inapto a simulado final" | **APROVADO** |
| L3-R14 | VOLÁTIL baixo + aderência PARCIAL | Ambos aplicados, nos mesmos termos | **APROVADO** |
| L3-R16 | VOLÁTIL baixo | Aplicado, com o motivo "padrão por fonte de dados" | **APROVADO** |
| L3-R36 | "ela pode usar" → "ele pode usar" | Aplicado (texto exato); nada mais mudou | **APROVADO** |
| L3-R23 | Ressalva (baixa discriminação; deixar fora do núcleo) | Mantido; a recomendação ficou na seção 1.4 | APROVADO COM RESSALVA (sem mudança) |
| Registros de formato, extensão e concentração de fonte | D1 da Gerência ou opcional | Formato e extensão ficaram registrados sem ação; quanto à fonte, o substituto usa base AWS | OK (registro) |
| Normativo (R12 da v1) | PENDENTE NORMATIVO | Encerrado: o item foi retirado e nenhum item desta parte cita norma | OK |

Reabri hoje (18/10/2026), com curl, HTTP 200 e sem redirecionamento, duas bases dos itens que mudaram de rótulo:
- "Como pesquisar" (www2.camara.leg.br, Banco de Discursos): encontrei literalmente "Resumo do discurso ou da reunião de comissão, com os principais assuntos tratados", "Íntegra do discurso de plenário ou da reunião de comissão" e "devem ser colocados entre aspas duplas". CONFERE (R13, R14).
- Indexer overview (learn.microsoft.com): encontrei literalmente "On subsequent runs, the indexer can usually detect and retrieve just the data that has changed" e "For blob data, change detection is automatic". CONFERE (R16).

## 3. L3-R12 (novo; P2-3.1; E [TS]; D; VOLÁTIL baixo)

**Fonte, aberta por esta coordenação.** https://docs.aws.amazon.com/transcribe/latest/dg/tca-output-batch.html, aberta em 18/10/2026 com curl e UA de navegador: HTTP 200, sem redirecionamento, 38.200 bytes, sem data de atualização na página. Trecho literal encontrado na seção "Generative call summarization":
> "The analytics job will complete without summary generation in the following cases: Insufficient conversation content: The conversation must include at least one turn from both the agent and the customer. [...] Safety guardrails: The conversation must meet safety guardrails in place to ensure appropriate summary is generated. When these guardrails are not met, the service will return the error code FAILED_SAFETY_GUIDELINES. The error code can be found in Skipped section within AnalyticsJobDetails in the output."

O exemplo de saída mostra `"JobStatus": "COMPLETED"` e `"Skipped": [{"Feature": "GENERATIVE_SUMMARIZATION", ...}]`. As duas citações da justificativa CONFEREM.

**Gabarito E: correto.** O trabalho termina (COMPLETED); só o resumo é pulado. Por isso, "interrompido com falha, sem produzir a transcrição nem as demais análises" é falso. Não vejo leitura razoável que dê C.
Risco residual de recurso, baixo: a página fala em "error code FAILED_SAFETY_GUIDELINES". O item, porém, afirma a interrupção do trabalho e a falta da transcrição, e ambas são desmentidas pelo JobStatus COMPLETED.

**[TS] de troca única: OK.** Só muda o desfecho do trabalho: conclui sem o resumo → é interrompido com falha. A oração "sem produzir a transcrição nem as demais análises" é consequência da mesma troca, e não um segundo conceito. No teste de reversão ("conclui, sem gerar o resumo"), o enunciado fica verdadeiro.

**Formato D: OK.** Mantém D 5/20 na 3.1; o maior formato fica em 25%. Não é SH, como pedia o R1.

**VOLÁTIL baixo: CONCORDO.** É comportamento documentado de recurso de fornecedor, hipótese (b). Está inapto a simulado final até a reverificação de 4–8/1/2027.

**Gêmeo por ponto, inclusive paráfrase: NENHUM.** Fiz busca própria, sem diferenciar maiúsculas, nos 560 itens do pacote.json v1.10 (registro inteiro).
- Combinei Transcribe com resum, sumari, summar, guardrail, salvaguard e analític, e resumo ou sumarização com falha, sem resumo, interromp, salvaguard e seguran. Zero acertos.
- O L3-Q02 (sumarização ≠ transcrição reduzida) e o Q04 (propagação de erros) são pontos distintos.
- Parte B v2: R40–R47 tratam da sumarização do Azure Language (saídas, aspectos, escopo) e R54–R56 da identificação de idioma do Transcribe. Pontos distintos.
- Partes C v1/v2: R85, R87, R93 e R95 tratam do Transcribe em segurança, LGPD e PII. Pontos distintos.
- "Call Analytics" em saida/ só aparece em notas de fonte (L2 saldo_v2, l. 101; L1 onda 2 B, base de diarização), sem item com esse ponto.

**Aderência: APROVADO COM RESSALVA (D1 da Gerência).** Esta QA não confirma a marca "direta" sem reserva. A fonte é de produto de central de atendimento: o próprio trecho exige "at least one turn from both the agent and the customer". O ponto é a semântica de status do trabalho na API (COMPLETED com Skipped). Pelo critério da QA_T105_R2 ("o item não pede conhecer a ferramenta como produto (API, preço, idioma, parâmetro)"), isso puxa o tema para a 1.8 (AWS Transcribe). O precedente da casa já afastou o Call Analytics como "aderência de call center, fora do contexto" (L2_reforco_onda3_saldo_v2, l. 101).

Mesmo assim, não reprovo, por três razões:
- o objeto é sumarização por IA, que a 3.1 nomeia;
- o item não traz moldura institucional nem afirma uso parlamentar;
- pela D-T97-META-FUNDADOR-RESP, um PARCIAL conta para a meta de 20, e a folha continua acima do piso.

Leitura desta QA: PARCIAL (tema de 1.8; produto de atendimento). Se a Gerência adotar essa leitura, a 3.1 fica com 15/20 diretas (piso de 10 cumprido). Gabarito, [TS], formato e VOLÁTIL não mudam. A instrução 3.4 da T97_reconciliacao ("item novo de folha com menos de 12 diretas é direto") deixa então de ser cumprida neste item, como já ocorre em R13 e R14. A escolha é D1 da Gerência; não há mais rodada.

## 4. Contagens (script próprio, python3 -I, sobre a Parte 3 da v2)

| folha | itens | C/E novos | C/E folha | [TS] novos | VOLÁTIL folha | formatos novos | maior formato (folha) | diretas folha |
|---|---|---|---|---|---|---|---|---|
| P2-3.1 | 6 + 14 = 20 | 7/7 | 10/10 | 9/14 | 4/20 = 20% (R12, R13, R14, R16; todos baixo) | D4 PC4 SH4 TSj1 NP1 | 5/20 = 25% | 16/20 declarado; 15/20 se R12 for PARCIAL |
| P2-3.2 | 6 + 14 = 20 | 7/7 | 10/10 | 9/14 | 1/20 = 5% (R27) | D2 PC4 SH4 NP1 AP3 | 5/20 = 25% | 20/20 |
| Parte A | 28 | 14/14 (50%) | — | 18/28 (≥ 16 = metade + 2) | 5 no lote, risco alto 0 | — | — | — |

- Todas as contagens declaradas na v2 conferem.
- C está em 50% (faixa de 40–60%). VOLÁTIL na 3.1 está em 20%, no teto da regra (≤ 20%). O maior formato fica em ≤ 30% nas duas folhas.
- O enunciado do R12 tem 49 palavras, como declarado; a diferença de extensão C × E (4,7 palavras) não muda.

## 5. Veredito

**Itens alterados nesta rodada (6): L3-R12 APROVADO COM RESSALVA (aderência, D1); L3-R13, R14, R16 e R36 APROVADOS. L3-R23 continua APROVADO COM RESSALVA.** Os outros 22 itens não mudaram desde a v1 e seguem aprovados no R1. Nenhum gabarito errado.

**Taxa de reprovação da parte na R2: 0/28 (0%).** Não há GATE. Veredito geral da parte A: **APROVADO COM RESSALVAS** (ressalvas só de registro e D1). PENDENTE NORMATIVO: nenhum.

## 6. Registros residuais para a gce-gerencia (D1)

1. **L3-R12, aderência.** É D1 da Gerência: manter "direta" ou passar a PARCIAL, como esta QA lê (motivo na seção 3). Se passar a PARCIAL, a 3.1 fica com 15/20 diretas e 5 PARCIAIS (R01, R02, R12, R13, R14). O piso de 10 continua cumprido, e não há reposição pela D-T97-META-FUNDADOR-RESP.
2. **L3-R13 e R14.** Continua a D1 já registrada no R1: PARCIAL contado para a meta (regra do Fundador) × instrução 3.4 da T97_reconciliacao. A Gerência deve registrar qual das duas prevalece na 3.1 da onda 4.
3. **VOLÁTIL da 3.1 no teto (4/20 = 20%).** Não sobra margem. Se a Gerência marcar outro item da folha como VOLÁTIL na reconciliação ou na reverificação de janeiro, a folha passa do teto.
4. **Recurso, baixo risco (R12).** A página usa a expressão "error code" para um trabalho que termina COMPLETED. A justificativa já cita "will complete without summary generation". Fica como nota para a GBQ, se o item for usado em simulado diagnóstico.
5. **Proximidades para a GBQ (D2 de montagem), sem gêmeo.**
   - L3-R12 × L3-R43 (parte B): a sumarização voltada a conversas de duas partes, de atendimento.
   - L3-R12 × L3-R54–R56 (parte B) e × C-R85/R87/R93/R95: o mesmo produto, Amazon Transcribe.
   - Recomendo que não fiquem no mesmo caderno.
6. **Ressalvas mantidas do R1, sem efeito de aceite.**
   - L3-R23 fica fora do núcleo.
   - A diferença de extensão C × E (4,7 palavras) não recebeu ação, e a produção justificou.
   - A classificação de formato de R20, R22 (D × SH) e de R30, R36, R38 (AP × SH) segue mantida. Se R22 for lido como SH, a 3.1 fica com SH 6/20 = 30%, ainda no teto.
7. **Reverificação de 4–8/1/2027 (T-11, P2, gce-cqfp).**
   - REVERIFICAR: R12, R13, R14, R16, R27.
   - CONFERÊNCIA DE BASE: os outros 23.
   - A página do R12 não tem data de atualização; convém registrar o SHA-256 na reverificação.
