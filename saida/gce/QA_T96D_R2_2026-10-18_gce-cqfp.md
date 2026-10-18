# QA_T96D_R2_2026-10-18_gce-cqfp.md — T-96 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L1_reforco_onda2_D_v2.md (gce-cpp; SHA-256 2762f17b5ca6188841c97e1807bd4a24d300e2196d7024231b6818833d77a5fb), 28 itens AUTORAL L1-R103 a L1-R130. Rodada 2 de 2 (última). Base: parecer R1 (QA_T96D_R1_2026-10-18_gce-cqfp.md); diff v1 → v2; D-REFORCO-2; D-T89-R1-ACEITE. A gce-cqfp revisa e aponta; não reescreve.

## 1. Diff v1 → v2 (nada além do declarado)

`diff` integral conferido. Mudaram só: linha 1; bloco de resposta inserido no topo (l. 3–17); mapa (R103, R104, R114, R124, R129); proximidades (R124 × R12 trocado por R124 × R126/R122/R106); tabela de formatos da 1.8 (SH 6, AP 3) e linha de conclusão; enunciados de R103, R104, R114, R124 e R129; justificativas de R103, R104, R114, R123, R124 e R129; base do R124; tabelas de contagem e estilo (C/E por folha, formato máximo, extensões, O-1, O-4, O-7); proveniência (saiu a linha AWS custom-language-models; R124 acrescido à do model card). Os 22 itens APROVADOS na R1 e o enunciado do R123 estão byte a byte iguais à v1. R119 sem mudança, como pedido.

## 2. Evidência — reabertura hoje (18/10/2026, curl, HTTP 200)

| URL | trecho conferido | resultado |
|---|---|---|
| raw.githubusercontent.com/openai/whisper/main/model-card.md | seção "Model Use" › "Evaluated Use", 3º parágrafo (l. 46 do arquivo baixado): "In particular, we caution against using Whisper models to transcribe recordings of individuals taken without their consent or purporting to use these models for any kind of subjective classification." | CONFERE (R124). A v2 (seção 1.3, proximidades) diz "segundo parágrafo"; é o terceiro da seção (o 2º é o da diarização, base do R126). Erro de localização na v2, sem efeito: o trecho está literal e na seção citada |
| raw.githubusercontent.com/openai/whisper/main/README.md | l. 62: "The relative speeds below are measured by transcribing English speech on a A100, and the real-world speed may vary significantly depending on many factors including the language, the speaking speed, and the available hardware." | CONFERE (R129) |
| docs.aws.amazon.com/transcribe/latest/dg/streaming.html | "When your audio stream contains no speech, encode and send the same amount of silence. For example, silence for PCM is a stream of zero bytes."; "This error occurs when a stream exceeds the maximum allowed session duration. … This is a hard limit that cannot be increased. To continue transcribing, start a new streaming session." | CONFERE (R104, R114) |
| docs.aws.amazon.com/transcribe/latest/dg/streaming-partial-results.html | "Low stability provides the highest accuracy. High stability transcribes faster, but with slightly lower accuracy." | CONFERE (R103) |

Nenhuma norma citada (sem PENDENTE NORMATIVO). D-FONTE-DATA-ANTERIOR não incide.

## 3. Ajustes da R1

| id | pedido R1 | conferência R2 | veredito |
|---|---|---|---|
| R103 | ancorar no Amazon Transcribe | "No Amazon Transcribe em streaming, que permite estabilizar…" — ancorado; E, [TS] (papéis alto × baixo), PC e ponto mantidos; justificativa ancorada | APROVADO |
| R104 | (a) tirar a cauda; (b) fornecedor; parlamentar no sujeito | cauda retirada; "ao Amazon Transcribe em streaming"; "de uma reunião de comissão" no sujeito; "independentemente" em C mantido; justificativa sem o "próximo do tempo real", que não estava no trecho | APROVADO |
| R114 | ancorar | "…do Amazon Transcribe … solicitar à AWS"; E [TS]; VOLÁTIL médio mantido (limite de serviço) | APROVADO (VOLÁTIL médio) |
| R119 | manter âncora | sem mudança | APROVADO |
| R123 | justificativa sem "fast transcription" | frase retirada, e também o contêiner (não estava no trecho literal); só o "retrieve … asynchronously" ficou como base; enunciado e E intactos | APROVADO |
| R129 | predicado avaliativo | "e agiu corretamente ao ressalvar que…" — o juízo é a conduta, C unívoco; reclassificado SH (correto: situação com conduta julgada). 43 palavras, C mais longo, abaixo do E mais longo (48), O-1 cumprido | APROVADO COM AJUSTE DE FORMA (justificativa) |

Defeito no R129, só na justificativa (l. 288), sem efeito no gabarito: a oração ficou sem regência — "porque as velocidades relativas foram medidas … e que a velocidade real pode variar…". O "e que" depois de "porque" não tem verbo de que dependa. Correção mínima que a QA aceita sem R3 (a redação é da produção/Gerência): suprimir o "que" ("… em uma A100 e a velocidade real pode variar …"). Aplicada literalmente na reconciliação, não exige nova rodada.

## 4. Novo R124 (inteiro)

Enunciado (l. 179, 38 palavras): "Ao planejar a degravação de reuniões reservadas das comissões com o Whisper, a equipe deve levar em conta que o model card adverte contra o uso dos modelos para transcrever gravações de pessoas feitas sem o consentimento delas."

- Gabarito C: correto. A advertência está literal no model card (seção 2). O item reproduz só a primeira das duas condutas do trecho (gravação sem consentimento) e não a classificação subjetiva: recorte fiel, sem vínculo novo (O-4).
- Ponto único: conferido por busca de "consent"/"consentimento" nas partes A, B e C (saida/gce/L1_reforco_onda2_A_v1.md, B_v1.md, C_v1.md): zero ocorrências. No pacote.json v1.9 "consentimento" só aparece em itens de LGPD (BQ-0004, 0005, 0007, 0025, 0032, 0045, 0084, L4-18), de outra folha e outro ponto (hipótese legal de tratamento × advertência de uso do fornecedor). Na 1.8, nenhum canônico (Q18–Q20, R16–R18) nem novo usa o ponto. Proximidades com R126 (diarização não avaliada, 2º parágrafo da mesma seção), R122 (alucinação) e R106 (tempo real fora da caixa): pontos distintos; aceitas.
- Formato AP: correto, com o elemento parlamentar no sujeito. A 1.8 fica com AP 3/20 = 15%.
- Estilo: C sem restritivo, sem "pode"; uma afirmação; extensão dentro da faixa (C 30–43).
- VOLÁTIL: não. É propriedade do artefato publicado (model card, ramo main), sem número, versão, preço, disponibilidade ou recurso de serviço gerenciado: critério da D-T89-R1-ACEITE. REVERIFICAR declarado.
- [TS]: não (C não espelho): correto.
- Ressalva de registro, sem efeito no gabarito: o contexto "reuniões reservadas das comissões" pode sugerir ao leitor que essas gravações são feitas sem consentimento. O item não afirma isso — o C só exige que a advertência exista e deva ser considerada no planejamento —, e por isso não cabe recurso. Mas o elemento parlamentar fica perto de vínculo implícito. Não bloqueia; registro para a Gerência e para a auditoria de estilo (gbq-estilo).
- Edital: 1.8 nomeia o Whisper; condição de uso declarada pelo fornecedor está no escopo. Nenhuma extrapolação; sem dependência de lei.
- Cobertura registrada sem efeito: com a saída da base AWS, a 1.8 nova tem Whisper 6, Google 4, Azure 3, AWS 1 (R127). As quatro ferramentas do edital seguem cobertas (AWS também no canônico R17).

Veredito: APROVADO.

## 5. Contagens (conferidas por script/leitura)

- C/E da parte D: 14 C / 14 E = 50,0% (faixa 40–60%). Por folha: 1.7 6 C / 8 E; 1.8 8 C / 6 E. A faixa da regra 5 é da onda e se confere com A–C.
- [TS]: 17/28 (inalterado), cada E com uma única troca.
- Formatos da 1.8: SH 6/20 = 30% (R16, R117, R121, R125, R128, R129), no teto sem folga; AP 3/20. A 1.7 segue com máximo de 20%. Qualquer mudança futura de formato na 1.8 que acrescente SH fere a regra 3.
- VOLÁTIL: 1.7 3/20 = 15% (Q16, R110, R114); 1.8 2/20 = 10% (Q18, Q19), 0 novos, se mantida a posição da seção 6.
- Estrutura: Parte 2 sem gabarito, [TS], VOLÁTIL ou REVERIFICAR; FIM DO LOTE presente; linha 1 no formato.

## 6. Posição da QA sobre R120 e R128 (para a Gerência)

NÃO VOLÁTEIS, com REVERIFICAR e conferência de base obrigatória em 4–8/1/2027 (T-11, parte P2, gce-cqfp). Motivo: o ponto de cada um é o mecanismo documentado de recurso central — phrase list aplicada em tempo de execução, sem treino (R120); WER contra transcrição humana como critério para treinar custom speech (R128) —, sem número, versão, preço, limite ou disponibilidade regional. O risco de o recurso deixar de existir até janeiro é baixo, e a mudança afetaria o nome do recurso, não o mecanismo. Nos dois casos o mesmo tratamento já valeu para R17 (D-T89-R1-ACEITE). Como a letra ratificada lista "existência de recurso", a Gerência deve registrar expressamente, na reconciliação, que funcionamento documentado de recurso central não se enquadra nessa hipótese. Sem esse registro, os dois seriam VOLÁTEIS novos na 1.8 (4/20 = 20%, no teto, mas contra a T89_reconciliacao, seção 3) e teriam de ser substituídos, o que não cabe mais nesta rodada. Com o R124 substituído, o terceiro caso da R1 deixou de existir.

## 7. Veredito geral

APROVADO COM RESSALVAS — R2: 0/28 reprovados (0,0%), sem GATE. Ressalvas: (1) justificativa do R129 com a correção mínima da seção 3, aplicada literalmente na reconciliação; (2) registro D2 da gce-gerencia sobre R120 e R128 (seção 6); (3) registro do R124 (contexto de reunião reservada) e da localização "2º parágrafo" (é o 3º), sem efeito.

| id | veredito | id | veredito |
|---|---|---|---|
| L1-R103 | APROVADO | L1-R117 | APROVADO |
| L1-R104 | APROVADO | L1-R118 | APROVADO |
| L1-R105 | APROVADO | L1-R119 | APROVADO |
| L1-R106 | APROVADO | L1-R120 | APROVADO (registro D2) |
| L1-R107 | APROVADO | L1-R121 | APROVADO |
| L1-R108 | APROVADO | L1-R122 | APROVADO |
| L1-R109 | APROVADO | L1-R123 | APROVADO |
| L1-R110 | APROVADO (VOLÁTIL médio) | L1-R124 | APROVADO (novo) |
| L1-R111 | APROVADO | L1-R125 | APROVADO |
| L1-R112 | APROVADO | L1-R126 | APROVADO |
| L1-R113 | APROVADO | L1-R127 | APROVADO |
| L1-R114 | APROVADO (VOLÁTIL médio) | L1-R128 | APROVADO (registro D2) |
| L1-R115 | APROVADO | L1-R129 | APROVADO COM AJUSTE DE FORMA (justificativa) |
| L1-R116 | APROVADO | L1-R130 | APROVADO |
