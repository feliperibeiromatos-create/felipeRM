# QA_T96B_R2_2026-10-18_gce-cqfp.md — T-96 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L1_reforco_onda2_B_v2.md (gce-cpp; SHA-256 201a3172c97792474627b22d7c749f7a21389a4984d2926c8b4e0364afc7b23e; 28 itens AUTORAL, L1-R47 a L1-R74; folhas P2-1.3 e P2-1.4). Comparado com a v1 (SHA-256 22100f046d269bdb491ede1a31d83e9566caef83ded7a7db4b92765b34cbe2f9) por diff. Rodada 2, a última de no máximo 2 (D-REFORCO-2).
Critérios: os mesmos da R1 (QA_T96B_R1_2026-10-18_gce-cqfp.md): D-REFORCO-2 (regras 1 a 6), D-T89-R1-ACEITE (critério de VOLÁTIL), D-FONTE-DATA-ANTERIOR, T89_reconciliacao seção 3, T93_reconciliacao O-1 a O-8, pacote.json v1.9 (334 itens), partes A (v1), C (v1) e D (v2) da onda 2.
A QA revisa; não reescreve.

## 1. Diff v1 → v2 (conferido por diff e script)

Linhas alteradas: 1 (cabeçalho), bloco novo de resposta ao parecer (linhas 3 a 18), mapa de R48, R54 e R58, proximidades da 1.3 (l. 108), Parte 2 de R48, R54, R58, R60, R62, R70 e R73, Parte 3 de R48, R54, R58 e R60, linha "Extensão", três linhas da tabela de proveniência, mais uma nota da R2. Nenhuma outra linha mudou. Os demais 20 enunciados, gabaritos, [TS], VOLÁTEIS e bases estão idênticos aos da v1. CONFERE.

## 2. Ajustes A-1 a A-6 (texto exato)

Cada trecho entre aspas da seção 4 da R1 foi buscado na v2: os textos novos aparecem 1 vez cada, e os textos substituídos aparecem 0 vezes.

| ajuste | item | Parte 2 | Parte 3 | mapa | resultado |
|---|---|---|---|---|---|
| A-1 | R48 | enunciado literal | as 2 substituições literais ("Receber o áudio como entrada não determina…"; "Google Cloud (Gemini Enterprise Agent Platform, Audio understanding)") | ponto literal | CONFERE; E, [TS], PC mantidos |
| A-2 | R54 | enunciado literal | abertura literal | ponto literal | CONFERE; E, [TS], VOLÁTIL médio, concessiva (O-8) mantidos |
| A-3 | R60 | última frase literal | justificativa literal (16 × 8 = 128) | sem mudança | CONFERE; E, [TS] mantidos |
| A-4 | R62 | enunciado literal | sem mudança | sem mudança | CONFERE |
| A-5 | R70 | enunciado literal (reunião de comissão) | sem mudança | sem mudança | CONFERE; AP mantido |
| A-6 | R73 | enunciado literal | sem mudança | sem mudança | CONFERE |

Correção de registro da extensão: conferida por script próprio sobre a Parte 2 da v2. C 40,5 (30 a 52; maior R49) e E 39,4 (26 a 46; maior R54). CONFERE com a linha da v2.

## 3. URLs finais e evidência (reabertas pela QA em 18/10/2026, curl -L)

| URL citada | resultado |
|---|---|
| https://docs.aws.amazon.com/nova/latest/userguide/speech.html | HTTP 200, sem redirecionamento. Trecho do novo R58 conferido literalmente na página baixada: "Bidirectional event streaming : Amazon Nova Sonic uses a persistent bidirectional connection that allows simultaneous event streaming in both directions. Unlike traditional request-response patterns, this approach permits the following: Continuous audio streaming from the user to the model Concurrent speech processing and generation Real-time model responses without waiting for complete utterances". CONFERE |
| docs.cloud.google.com/vertex-ai/…/multimodal/audio-understanding | HTTP 200; a URL final é https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/audio-understanding, igual à registrada na v2. CONFERE |
| docs.cloud.google.com/vertex-ai/…/live-api | HTTP 200; a URL final é https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/live-api, igual à registrada. CONFERE |
| learn.microsoft.com/…/openai/how-to/audio-real-time | HTTP 200; a URL final é https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/realtime-audio, igual à registrada. CONFERE |

As 3 URLs finais estão registradas na tabela de proveniência, e a nota da R2 as leva à conferência de base de 4–8/1/2027. A linha do Google audio-understanding deixou de listar R58, e a linha da AWS speech.html passou a listá-lo. CONFERE.
Registro, sem efeito: a coluna "base" do mapa (Parte 1) de R47, R48, R52 e R54 continua com a URL citada. A URL final está só na proveniência, o que basta.
Nenhuma norma citada: não há PENDENTE NORMATIVO. Nenhuma base de data anterior.

## 4. Novo L1-R58, exame integral

Enunciado (51 palavras): "Em um LLM de áudio nativo conversacional, a conexão bidirecional em fluxo contínuo permite que o áudio do usuário seja enviado ao modelo enquanto este processa a fala e gera a resposta, diferentemente do padrão de requisição e resposta, em que o modelo só responde depois de receber o conteúdo completo."

- Gabarito C: correto. As três orações ("enviado… enquanto", "processa a fala e gera a resposta", "requisição e resposta… depois do conteúdo completo") correspondem, nesta ordem, a "Continuous audio streaming from the user to the model", "Concurrent speech processing and generation" e "Unlike traditional request-response patterns… without waiting for complete utterances". A última oração é inferência direta do contraste da base, não extrapolação. O verbo "permite" evita generalizar a todo produto. Não há leitura plausível em E.
- Escopo: dentro de 1.3 ("LLMs multimodais de áudio nativo"). A base é de modelo fala-para-fala (Nova Sonic), e o enunciado é específico de áudio conversacional, não um parâmetro genérico de LLM. O motivo do REPROVADO da R1 está superado. O item não tem dependência de versão: VOLÁTIL "não" está correto pelo critério da T-89 (conceito de arquitetura), e o REVERIFICAR sem efeito de VOLÁTIL é adequado.
- Ponto único na folha: o item não repete os 6 existentes (Q05, Q06, L1C-Q25, L1C-Q26, R05, R06; nenhum item do pacote v1.9 tem "bidirecional", "requisição e resposta", "fluxo contínuo", "fala-para-fala" ou "Nova Sonic") nem os 13 novos. Proximidades na folha, todas distintas: R56 julga o streaming da SAÍDA e a percepção de latência (E); R57, a interrupção com manutenção do contexto; R60, o limite e a renovação da conexão; R47, as modalidades de entrada. A proximidade com R56 é a mais forte, mas os pontos são diferentes (envio simultâneo da entrada × efeito do streaming da resposta), e os gabaritos são opostos.
- Partes A, C e D: a parte A não tem proximidade (R44, 1.2, trata do Whisper em tempo real). A parte C também não (R79, 1.5, trata de pontuação em resultados parciais). Na parte D, proximidade registrada para a D1, que não viola a regra 1, porque as folhas são diferentes: L1-R107 (1.7, E) julga que o reconhecimento síncrono do Google responde só depois de processar todo o áudio, enquanto o streaming entrega resultados intermediários. A oração final do R58 ("padrão de requisição e resposta, em que o modelo só responde depois de receber o conteúdo completo") toca a mesma oposição. O ponto que decide o R58 é a conexão bidirecional com processamento e geração concomitantes num modelo de áudio nativo, que é próprio da 1.3. Também ficam registradas, mais longe, as proximidades com L1-R112 (1.7), R15 (1.7) e R17 (1.8), que tratam de streaming × lote no ASR.
- Formato e teto: o formato declarado é definição. Na folha de 20, D = 3 (Q05, R47, R58) = 15%, abaixo do teto de 30% (6). Registro, sem efeito: pelo critério da D2 da T-91 (o formato segue a construção do ponto), a construção "X permite…, diferentemente de Z" também pode ser lida como par confundível. Nessa leitura, PC = 4/20 = 20% e D = 2/20, também dentro do teto. Na 1.3 não vale a vedação de definição da onda 2 (essa vedação é só da 1.4).
- Estilo: afirmação única com contraste; a frase é longa, mas não é ambígua; não usa "sempre", "nunca" ou "apenas" absolutos. Com 51 palavras, é o segundo C mais longo. A média de C passou de 39,4 para 40,5 e ficou 1,1 palavra acima da média de E (39,4), uma pequena inversão do que o O-1 recomenda (a base tem C 31,6 contra E 34,7). Não há C acima de 65 palavras, e a diferença é muito menor que a da onda 1 (9,2). Fica como registro de estilo para a Gerência e para a auditoria do gbq-estilo (regra 6), sem efeito de veredito.
- Veredito: APROVADO.

## 5. Tetos e contagens da v2 (script próprio)

- Estrutura: Partes 1/3 a 3/3, os FIM DA PARTE e o FIM DO LOTE estão presentes. A Parte 2 tem 28 ids com "Julgue o item." e 0 ocorrências de gabarito, [TS], VOLÁTIL ou REVERIFICAR. A Parte 3 tem 28 gabaritos. CONFERE.
- Gabarito: 14 C / 14 E (50%); 1.3 com 7 C / 7 E e 1.4 com 7 C / 7 E. A faixa de 40% a 60% está cumprida.
- [TS]: 17/28 (meta de 16) cumprida. O R58 não tem [TS].
- Formato: 1.3 (20): D 3, TS 3, SH 4, NP 3, PC 3, AP 4, com máximo de 20%. 1.4 (20): TS 5, AP 5, SH 4, NP 2, D 2, PC 2, com máximo de 25% e nenhum D ou PC novo. CONFERE.
- VOLÁTIL: 3/20 em cada folha (15%), nenhum de risco alto. CONFERE.

## 6. Veredito por item

| id | veredito R2 | id | veredito R2 |
|---|---|---|---|
| L1-R47 | APROVADO | L1-R61 | APROVADO |
| L1-R48 | APROVADO (A-1 aplicado) | L1-R62 | APROVADO (A-4 aplicado) |
| L1-R49 | APROVADO | L1-R63 | APROVADO |
| L1-R50 | APROVADO | L1-R64 | APROVADO |
| L1-R51 | APROVADO | L1-R65 | APROVADO |
| L1-R52 | APROVADO | L1-R66 | APROVADO |
| L1-R53 | APROVADO | L1-R67 | APROVADO |
| L1-R54 | APROVADO (A-2 aplicado) | L1-R68 | APROVADO |
| L1-R55 | APROVADO | L1-R69 | APROVADO |
| L1-R56 | APROVADO | L1-R70 | APROVADO (A-5 aplicado) |
| L1-R57 | APROVADO | L1-R71 | APROVADO |
| L1-R58 | APROVADO (item novo) | L1-R72 | APROVADO |
| L1-R59 | APROVADO | L1-R73 | APROVADO (A-6 aplicado) |
| L1-R60 | APROVADO (A-3 aplicado) | L1-R74 | APROVADO |

## 7. Taxa e veredito geral

Reprovados: 0/28 = 0%. AJUSTAR: 0. Não há GATE.
Veredito geral: APROVADO COM RESSALVAS. As ressalvas são só de registro e D1 da Gerência e não exigem texto novo:
(a) proximidade R58 (1.3) × L1-R107 (1.7, parte D), na oposição streaming × requisição completa;
(b) leitura alternativa do formato do R58 como par confundível, sem efeito no teto;
(c) O-1: C 40,5 × E 39,4 depois do novo R58, a ser observado pelo gbq-estilo;
(d) os registros da R1 que continuam abertos para a D1: coerência de VOLÁTIL entre R65 e R71, R57 conservador, R62 × L1-Q20/Q18, concentração das bases no README do pyannote (ramo develop), R49 com base de console, R68 com baixa discriminação e estilo opcional em R63;
(e) a conferência de base de 4–8/1/2027 inclui as 3 URLs redirecionadas e o R58 (speech.html).
