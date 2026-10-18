# QA_T97A_R2_2026-10-18_gce-cqfp.md — T-97 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L2_reforco_onda3_A_v2.md (gce-cpp; 28 itens AUTORAL L2-R19 a L2-R46; P2-2.1 = R19–R32, P2-2.2 = R33–R46). Rodada R2 (última). Revisão; nada foi reescrito no objeto.
Lido: QA_T97A_R1_2026-10-18_gce-cqfp.md; QA_T97A_normativo_2026-10-18_qa-normativo.md (14/14 CONFERE, 0 DIVERGE); L2_reforco_onda3_A_v1.md e v2 (diff integral); DECISOES.md (D-REFORCO-2, D-ADERENCIA, D-T96-ONDA2-ACEITE (II)); edital/modulo_RF_IA_P2.md (2.1, 2.2); pacote.json v1.9, finais da onda 2 (L1_reforco_onda2_A_v3, B_v2, C_v2, D_v3, saldo_v2), L2_reforco_onda1_v3 e as partes B_v1 (agora existente), C_v2 e D_v1 da onda 3 (varredura de gêmeos por script, python -I).

## 1. Diff v1 → v2 (o que mudou e se era devido)

Conferido por diff integral. Mudanças: (a) bloco de resposta ao QA no topo (linhas 3–54; item a item, todos "acatado"); (b) R20, R33, R35, R36, R37, R43, R44: enunciados = texto exato da R1 (comparação literal por script: 7/7 idênticos); (c) R23, R24, R40: enunciado, ponto, base e gabarito novos (substituições); (d) R31: gabarito "L2-R31. C." sem [TS], justificativa sem "espelho"; R35: justificativa sem "A recomendação de nova tentativa está correta." (a frase só subsiste na citação do bloco de resposta); (e) aderência PARCIAL nos 13 itens da R1 e marca PENDENTE NORMATIVO nos 14 itens normativos (mapa e d-G); (f) contagens, tabelas, registros O-1 a O-8, proveniência (Rol de 2009 retirado; R23, R40 acrescidos à linha da nota de transparência; R24 à do A2I) e dúvidas à Gerência, em decorrência. Nenhuma outra alteração: nenhum enunciado, gabarito ou [TS] fora da lista acima mudou. Rol do DETAQ: 0 ocorrências como base. Parte 2 sem gabarito, [TS], VOLÁTIL, REVERIFICAR, PENDENTE ou PARCIAL; 28 ids na Parte 2 e 28 gabaritos na Parte 3; FIM DO LOTE presente.

## 2. Evidência — bases reabertas por esta coordenação hoje (18/10/2026; curl com User-Agent de navegador; HTTP 200 em todas)

| fonte (URL final) | trecho conferido | itens |
|---|---|---|
| learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note (ms.date 2026-03-31; "Last updated on 2026-03-31") | "Because of these acoustic and linguistic variations, you should expect a certain level of inaccuracy in the output text when you design an application." CONFERE. Item Human-in-the-loop: "…ensuring constant human oversight… and maintaining the role of humans in decision making. Ensure that you can have real-time human intervention in the solution to prevent harm. This enables you to manage situations when the AI model does not perform as required." CONFERE | R23, R40 (e R33) |
| docs.aws.amazon.com/sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.html | "Use Amazon A2I with Amazon Transcribe – Have humans review Amazon Transcribe transcriptions of video or audio files." CONFERE; "low-confidence predictions or random prediction samples" CONFERE; aviso "no longer open to new customers. Existing customers can continue to use the service as normal." presente | R24, R37 |
| www2.camara.leg.br/legin/int/atomes/2026/atodamesa-251-16-marco-2026-798819-publicacaooriginal-178493-cd-mesa.html | art. 2º, VI, literal CONFERE | R20 |
| docs.cloud.google.com/speech-to-text/docs/best-practices | "Listen to some sample audio. It should sound clear, without distortion or unexpected noise." CONFERE | R44 |

Normativo: o registro do qa-normativo (14/14 CONFERE; Ato 251 vigente, "Não consta revogação expressa"; RICD arts. 97, 98 e 255 sem nota de alteração) cobre R19, R20, R21, R22, R28, R29, R31, R32, R38, R39, R41, R42, R45 e R46, inclusive o texto do ajuste do R20. **A marca PENDENTE NORMATIVO pode sair dos 14 itens** (mapa, d-G, contagens e legenda) na reconciliação/v3.

## 3. Os três substitutos, por inteiro

**L2-R23 (2.1; C; SH; não VOLÁTIL; direta).** Gabarito C correto: o enunciado reproduz a recomendação literal (expectativa de imprecisão ao projetar a aplicação, por variações acústicas e linguísticas), sem condição acrescida. Aderência direta a 2.1: julga uma característica da transcrição automática que a diferencia do texto revisado. Ponto único na folha e no pacote (nenhum item com "inaccuracy"/"certo nível de imprecisão"/"variações acústicas" no pacote v1.9, onda 2, L2/L3 onda 1 e partes B, C, D). Proximidade R23 × L2-Q03 declarada e aceita: Q03 julga que o bom desempenho em áudio bom não dispensa revisão humana; R23 julga a expectativa de projeto. Formato SH, não AP (cumpre "sem AP em 2.1"). Estilo: curto, sem absoluto, fonte nomeada. **APROVADO.**

**L2-R24 (2.1; E [TS]; PC; VOLÁTIL baixo, REVERIFICAR; direta).** Gabarito E correto: a página diz "Have humans review Amazon Transcribe transcriptions"; o item afirma que as pessoas transcrevem o áudio do zero, e não revisam. [TS] de troca única (revisar a saída automática → transcrever do zero). Aderência direta: é a diferença entre revisão humana e degravação (2.1). VOLÁTIL baixo pela hipótese (c) da D-T96-ONDA2-ACEITE (serviço que a própria página declara fechado a novos clientes); coerente com R37, mesma página, mesmo rótulo; o item não afirma disponibilidade. Ponto único (nenhum A2I no pacote nem nas outras partes; R37 julga outra frase da página). Formato PC (sem AP). Registro de estilo (sem ajuste): "revisão humana consiste em transcrever do zero" carrega certa tensão semântica, mas é o próprio conceito cobrado pela folha. **APROVADO.**

**L2-R40 (2.2; E [TS]; SH; não VOLÁTIL; direta).** Gabarito E correto: a nota manda assegurar "real-time human intervention in the solution to prevent harm"; o item diz "posterior ao processamento do áudio, e não a intervenção em tempo real". [TS] de troca única (em tempo real → posterior). Aderência direta a 2.2 (human in the loop). Formato SH, não D (cumpre "sem definição em 2.2"). Proximidade R40 × L2-R33 declarada e aceita: mesmo item Human-in-the-loop, frases distintas (papel humano na decisão × intervenção em tempo real); R40 × L2-Q07 (revisão só ao final) também distinta. Registro de estilo (sem ajuste): "Uma equipe da Casa" é usual na banca; "da Câmara dos Deputados" seria mais explícito. **APROVADO.**

Recomendação à Gerência/GBQ (D2 de montagem, sem efeito no aceite): R23 × L2-Q03 e R40 × L2-R33 não figurarem no mesmo simulado ou caderno, como os gêmeos entre folhas da D-T96-ONDA2-ACEITE.

## 4. Veredito por item

| id | fl. | gab. | [TS] | formato | VOL | aderência | veredito R2 |
|---|---|---|---|---|---|---|---|
| L2-R19 | 2.1 | E | sim | SH | n | PARCIAL | APROVADO |
| L2-R20 | 2.1 | E | sim | TS | n | direta | APROVADO (texto exato aplicado) |
| L2-R21 | 2.1 | E | sim | TS | n | PARCIAL | APROVADO |
| L2-R22 | 2.1 | C | — | D | n | PARCIAL | APROVADO (registro: motivo da PARCIAL) |
| L2-R23 | 2.1 | C | — | SH | n | direta | APROVADO (novo) |
| L2-R24 | 2.1 | E | sim | PC | S baixo | direta | APROVADO (novo) |
| L2-R25 | 2.1 | E | sim | TS | S baixo | PARCIAL | APROVADO |
| L2-R26 | 2.1 | C | esp. | D | n | direta | APROVADO |
| L2-R27 | 2.1 | C | — | SH | n | PARCIAL | APROVADO |
| L2-R28 | 2.1 | E | sim | PC | n | PARCIAL | APROVADO |
| L2-R29 | 2.1 | E | sim | TS | n | PARCIAL | APROVADO |
| L2-R30 | 2.1 | C | — | PC | n | direta | APROVADO |
| L2-R31 | 2.1 | C | — (retirado) | D | n | PARCIAL | APROVADO (ajuste aplicado) |
| L2-R32 | 2.1 | C | — | SH | n | PARCIAL | APROVADO |
| L2-R33 | 2.2 | E | sim | TS | n | direta | APROVADO (texto exato aplicado) |
| L2-R34 | 2.2 | C | — | SH | n | direta | APROVADO |
| L2-R35 | 2.2 | E | sim | PC | n | PARCIAL | APROVADO (texto e justificativa aplicados) |
| L2-R36 | 2.2 | C | — | AP | n | direta | APROVADO (texto exato aplicado) |
| L2-R37 | 2.2 | C | esp. | SH | S baixo | direta | APROVADO (texto exato aplicado) |
| L2-R38 | 2.2 | E | sim | TS | n | PARCIAL | APROVADO |
| L2-R39 | 2.2 | C | esp. | PC | n | PARCIAL | APROVADO |
| L2-R40 | 2.2 | E | sim | SH | n | direta | APROVADO (novo) |
| L2-R41 | 2.2 | E | sim | TS | n | PARCIAL | APROVADO |
| L2-R42 | 2.2 | E | sim | PC | n | PARCIAL | APROVADO |
| L2-R43 | 2.2 | C | — | AP | n | direta | APROVADO (texto exato aplicado) |
| L2-R44 | 2.2 | C | — | AP | n | direta | APROVADO (texto exato aplicado) |
| L2-R45 | 2.2 | C | esp. | SH | n | PARCIAL | APROVADO |
| L2-R46 | 2.2 | E | sim | NP | n | PARCIAL | APROVADO |

**Reprovados: 0/28 = 0%.** Gate de 30%: não acionado. Todos os E com exatamente um conceito trocado (os 11 da R1 mais R24 e R40).

## 5. Contagens conferidas (por script sobre a v2)

- Gabarito: 14 C / 14 E (50,0%); 2.1 7/7; 2.2 7/7 (regra 5 cumprida).
- [TS]: 18 (14 E + 4 espelhos: R26, R37, R39, R45); R31 sem [TS].
- VOLÁTIL: 3 novos, todos baixo (R24, R25, R37); 2.1 2/20 = 10%; 2.2 1/20 = 5%; 0 alto (regra 4).
- Formatos (folha de 20): 2.1 SH 5, TS 5, PC 4, D 4, AP 2 (0 AP novo), NP 0; 2.2 SH 5, TS 4, PC 4, AP 4, D 2 (0 D nova), NP 1; maior 25% (regra 3). TS da 2.1 = 5/20, abaixo do limite de 6/20 da R1.
- **Aderência agregada: 2.1 = 10 diretas em 20** (Q01–Q04, R01, R20, R23, R24, R26, R30) **CONFERE**; 2.2 = 13 em 20 (Q05–Q08, R03, R04, R33, R34, R36, R37, R40, R43, R44) CONFERE; parte: 12 diretas, 16 PARCIAIS.
- Ponto único: nenhum duplicado na folha nem contra o pacote v1.9, a onda 2, os L2/L3 da onda 1 e as partes B_v1, C_v2, D_v1 da onda 3. Parte B (ressalva 3 da R1, agora conferível): não usa o Ato 251; seus itens da página "Como pesquisar" (R61 Tipo Fala; R66 Fase) e do RICD art. 98 (caput, §§ 3º, 6º, 7º) são pontos distintos de R25, R19 e R28.

## 6. Ressalvas (registro; nenhuma toca gabarito)

1. Retirar a marca PENDENTE NORMATIVO dos 14 itens (registro do qa-normativo, 14/14 CONFERE).
2. Linha de cabeçalho "QA PENDENTE: nenhum item deste arquivo passou por QA" fica desatualizada após esta R2 e a reconciliação.
3. L2-R22: o motivo da PARCIAL ("competência entre órgãos e coordenações") não descreve o art. 1º (transformação do órgão); ler-se "contexto institucional", como R45/R46. Erro de agrupamento da própria R1, corrigível na reconciliação.
4. Montagem: R23 × L2-Q03 e R40 × L2-R33 fora do mesmo caderno (seção 3).
5. Estilo: recomendação 2 do estilo_onda_2 (concessiva em E) segue não cumprida nesta parte — registro, já anotado na R1.

## 7. Veredito geral

**APROVADO — 0/28 reprovados (0%)**, com as ressalvas de registro da seção 6, a fechar pela gce-gerencia na reconciliação. Ajustes da R1 aplicados com o texto exato; substitutos R23, R24 e R40 aprovados; diff limpo; aderência da 2.1 em 10 diretas em 20. Itens permanecem QA PENDENTE até a reconciliação (D-QA-PENDENTE); 16 PARCIAIS só em simulado diagnóstico (D-ADERENCIA); R24, R25 e R37 VOLÁTEIS, inaptos a simulado final até 4–8/1/2027.
