# QA_T96C_R2_2026-10-18_gce-cqfp.md — T-96 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L1_reforco_onda2_C_v2.md (gce-cpp; 28 itens AUTORAL, L1-R75 a L1-R102; P2-1.5 e P2-1.6; SHA-256 37043a8c1ea154a3bd02e559163d8e68d2606ae290802cffc41b8553a64cfce3). v1 de comparação: 09cc589c938e3c4507c3fa63b6e044875bcf673fadd9511e651a90cfbbd7cbb1 (= o declarado no R1). Rodada 2 de 2 (última).
Critérios: parecer R1 (QA_T96C_R1_2026-10-18_gce-cqfp.md); D-REFORCO-2 (regras 1 a 6); D-T89-R1-ACEITE (critério de VOLÁTIL); T89_reconciliacao, seção 3 ([TS] ≥ 16; diluição de PC em 1.5/1.6); T93_reconciliacao O-1 a O-8; D-T91-R3-ACEITE (formato segue a construção do ponto); edital 1.5 e 1.6; pacote.json v1.9; onda 1 (L1_reforco_onda1_v2.md); partes A, B e D v2 da onda 2 (L1-R43 da parte A, reprovado no R2 da parte A, não foi considerado).
A QA revisa; não reescreve.

## 1. Diff v1 → v2 (conferido por diff)

Mudaram só: linha 1; bloco de resposta (novas linhas 3–26); linhas de convenção/entradas (27–28); nota de formatos (36); linhas do mapa de R80, R87, R99, R101, R102; contagens de formato de 1.6; proximidades da seção 3 (R80, R87, R93/R95, R99, R101, R102, R43); seção 4 (estilo, substituição); Parte 2: R76, R80, R84, R87, R90, R92, R99, R101, R102; Parte 3: R80, R87 (com a linha VOLÁTIL), R99, R101, R102; tabela de conferência; atenção especial; tabela de proveniência (R80, R87, R99, R101, R102, SHA do transcribe.py; README do Whisper removido); fontes não abertas; dúvidas 1 e 2. Nada mais mudou: os 19 aprovados no R1 estão idênticos (enunciado, gabarito, [TS], justificativa, base). Justificativas de R76, R84, R90, R92 inalteradas, como mandava o R1.

## 2. A-1 a A-4 — texto exato

| ajuste | item | resultado |
|---|---|---|
| A-1 | L1-R76 | CONFERE: "essa regra resulta na capitalização de 13 palavras." (C mantido) |
| A-2 | L1-R84 | CONFERE: enunciado idêntico ao texto do R1, caractere a caractere (C; não VOLÁTIL) |
| A-3 | L1-R90 | CONFERE: "Segundo a nota de transparência do Azure Speech, na captação…" (E mantido) |
| A-4 | L1-R92 | CONFERE: "Segundo a nota de transparência do Azure Speech, quando uma palavra que não existe no modelo aparece no áudio, o resultado é um erro de transcrição; por isso," (C mantido) |

## 3. Evidência — reaberta pela QA hoje, 18/10/2026 (curl; 6/6 HTTP 200; trechos por script python -I)

| fonte | itens | resultado |
|---|---|---|
| docs.aws.amazon.com/transcribe/latest/dg/how-numbers.html | R80 | 3/3 CONFERE ("Amazon Transcribe automatically adds punctuation to all supported languages"; "For most languages, numbers are transcribed into their word forms."; "for languages with support for transcribing numbers…"). Nota: o exemplo "All other languages" da página omite os pontos de "a m", mas isso é formatação de abreviatura/número, não ausência de pontuação; a primeira frase literal decide o E |
| learn.microsoft.com/…/how-to-custom-speech-test-and-train | R87, R99 | 8/8 CONFERE. #ITN = "invert-text-normalization rules … numbers, addresses, and dates"; #rewrite = "rewrite pairs … capitalization and spelling correction"; exemplo "Capitalize "Contoso" (via #rewrite rule)"; remissão a "Language support". Na tabela de uso × tipo de dado, as linhas estão pareadas como no item: "nonstandard pronunciation, such as product names or acronyms" → "Pronunciation data or phonetic pronunciation in structured text"; "industry-specific vocabulary and grammar" → "Plain text or structured text data" |
| docs.aws.amazon.com/…/custom-vocabulary-create-list.html | R101 | CONFERE ("If an entry contains multiple words, you must hyphenate each word.") |
| docs.aws.amazon.com/…/custom-vocabulary-create-table.html | R101 | CONFERE ("Do not use spaces in this column. If your entry contains multiple words, separate each word with a hyphen (-).") |
| docs.cloud.google.com/speech-to-text/docs/adaptation-model | R102 | 2/2 CONFERE ("…boost is applied to the entire phrase and only the entire phrase."; "…add all bigrams (2-words, in order)…") |
| raw.githubusercontent.com/openai/whisper/main/whisper/transcribe.py | R100 | baixado hoje: 30.375 bytes, SHA-256 176f5ab30e961bec2a7872f5701a1f5bf3cbfc77946e50512f0f0cf00a1ceacf = o registrado na v2 |

Registro do SHA (R100): ACEITO. github.com/api.github.com estão fora dos hosts liberados e o endereço raw não informa o commit; o SHA-256 do arquivo lido cumpre o objetivo da recomendação do R1 (permitir à conferência de janeiro detectar alteração), e a v2 manda comparar o SHA e reabrir o trecho em 4–8/1/2027. Está na tabela de proveniência e na "atenção especial". Nenhuma base de data anterior; nenhuma norma citada (sem PENDENTE NORMATIVO).

## 4. Os 5 substitutos, por inteiro

| id | folha | gab. | [TS] | formato | VOL | escopo no edital | ponto único (folha, onda 1, partes A/B/D) | veredito |
|---|---|---|---|---|---|---|---|---|
| L1-R80 | 1.5 | E | sim | TS | n | "pontuação automática" (literal) | distinto de R78 (condição da capitalização, mesma página) e de L1-R08 (C genérico, "pode variar"; sem conflito de gabarito); nada nas partes A/B/D nem no pacote sobre a abrangência por idioma | APROVADO |
| L1-R87 | 1.5 | E | sim | SH | S | "capitalização em transcrições" | distinto de Q30 (certeza), R77 (alcance), R84 (DisplayAs AWS), R09/R88 (formas lexical/exibição); sem #rewrite/#itn em nenhuma parte nem no pacote | APROVADO |
| L1-R99 | 1.6 | C | sim (O-6) | D declarado | n | "vocabulário técnico e parlamentar" | distinto de Q13/Q14 (adaptação × retreino; CV × CLM), de R94 e de L1-R128 (1.8, WER do modelo base, que agora fica só na parte D); sem conflito de gabarito com L1C-Q23 (1.2: "em regra" e restrito a sistemas end-to-end; a própria justificativa do Q23 registra os dados de pronúncia como recurso do custom speech) | APROVADO, ressalva de formato (seção 5) |
| L1-R101 | 1.6 | E | sim | SH | n | vocabulário parlamentar | distinto de R10 (conteúdo da lista) e R84 (forma de exibição, mesma tabela); L1-R117 (.en) não é mais tocado | APROVADO |
| L1-R102 | 1.6 | E | sim | TS | n | vocabulário parlamentar | distinto de R97 (FP × FN do boost, mesma página), de L1-R120 (phrase list) e de L1-R19/L2-R06 (WER); "boost" não aparece no pacote nem nas partes A/B/D com esse ponto | APROVADO |

[TS]: cada um dos 4 E troca exatamente um conceito — R80 (condição dos números atribuída à pontuação; a oração "nos demais, sem pontuação" é consequência da troca, não segundo erro), R87 (#itn no lugar de #rewrite, mantida a descrição do #rewrite), R101 (espaço no lugar de hífen), R102 (peso estendido aos trechos; a cauda "dispensa cadastrar…" é consequência, sem O-5). Gabaritos conferidos contra os trechos reabertos; nenhum ambíguo; nenhum depende de valor padrão de ramo de repositório.
Divergência com a instrução recebida: a instrução diz "R99 é C sem [TS]", mas a v2 marca "L1-R99. C [TS]" (falsa pegadinha, O-6), e a conta de 16/28 depende disso. A marcação é legítima pelo O-6 (o par correto é o costumeiramente invertido); sem ela, [TS] cairia para 15/28, abaixo da meta da T89, seção 3.
VOLÁTIL (R87): correto pelo critério da D-T89-R1-ACEITE (nome de seção e condições de recurso de serviço gerenciado; a página remete à lista de modelos/locais); REVERIFICAR em 4–8/1/2027; 1.5 = 3/20 (15%), teto cumprido, risco alto 0.

## 5. Ressalvas (registro e D1 da Gerência; nenhuma muda gabarito)

1. **R99 — formato.** O item afirma "X para A, e não Y, que se destina a B", em C, com os dois lados corretamente atribuídos: pelo critério ratificado na D-T91-R3-ACEITE (o formato segue a construção do ponto), é construção de par confundível, como Q11 e Q14, e não "definição". Reclassificado, 1.6 fica PC 3/20 (15%) e D 4/20, dentro do teto de 30%; a regra de diluição da T89, seção 3, vale "até a folha voltar a ≤ 30%", o que a folha de 20 já atende. Não há texto a mudar; cabe à Gerência registrar o formato real (PC) ou fixar outro na D1. A declaração da v2 "nenhum par confundível novo" fica inexata em um item.
2. **R101 × R87 — rótulo VOLÁTIL.** R87 (nome de seção de arquivo de recurso) está como VOLÁTIL; R101 (regra de sintaxe de entrada do mesmo tipo de recurso) e R84 (mesma tabela), não. A distinção é defensável (R87 apoia-se também na remissão a locais com suporte), mas fica para a Gerência uniformizar (D2 de rótulo, D-T89-R1-ACEITE); se R101 virar VOLÁTIL, 1.6 vai a 2/20, dentro do teto.
3. **Conferência de base em janeiro (sem efeito de VOLÁTIL):** R80, R99, R101, R102 entram na lista da T-11, parte P2 (gce-cqfp); R100 com comparação do SHA-256.
4. **Estilo:** 5 itens da parte abrem com "Segundo a…" (R80, R90, R92, R99, R102), 3 deles introduzidos na v2; sem erro, mas repetição de abertura a ser vista pelo gbq-estilo na amostra da onda. Extensões dos novos (35, 63, 57, 43, 50 palavras) dentro do O-1 (nenhum C acima de 65).
5. Registros do R1 mantidos para a D1 (R83, R79, R93 × L1-R20, R94 × L1-R120, concentração TER em 1.5): constam da v2 sem mudança de texto, como pedido. Bloqueio de L1-R43: sem objeto (substituído na parte A e, além disso, reprovado no R2 da parte A).

## 6. Conjunto (script)

28 ids na Parte 2 e 28 gabaritos na Parte 3; 14 C / 14 E (50%); por folha 1.5 7 C / 7 E e 1.6 7 C / 7 E; [TS] 16/28 (13 E + 3 C: R79, R95, R99); VOLÁTIL 3 novos (R86, R87, R88; todos em 1.5); Parte 2 sem gabarito, [TS], VOLÁTIL ou REVERIFICAR (0 ocorrências); PARTE 1/3–3/3 e FIM DO LOTE presentes; rótulo AUTORAL; QA PENDENTE declarado. Formatos declarados: 1.5 D 3, TS 5, SH 4, NP 2, PC 2, AP 4; 1.6 D 5, TS 5, SH 4, NP 0, PC 2, AP 4 (com a ressalva 1: D 4, PC 3). Nenhum formato acima de 30%.

## 7. Veredito por item

| id | folha | gab. | [TS] | veredito R2 |
|---|---|---|---|---|
| L1-R75 | 1.5 | E | sim | APROVADO (R1) |
| L1-R76 | 1.5 | C | não | APROVADO (A-1 conferido) |
| L1-R77 | 1.5 | E | sim | APROVADO (R1) |
| L1-R78 | 1.5 | C | não | APROVADO (R1) |
| L1-R79 | 1.5 | C | sim | APROVADO (R1) |
| L1-R80 | 1.5 | E | sim | APROVADO (novo) |
| L1-R81 | 1.5 | E | sim | APROVADO (R1) |
| L1-R82 | 1.5 | C | não | APROVADO (R1) |
| L1-R83 | 1.5 | C | não | APROVADO (R1) |
| L1-R84 | 1.5 | C | não | APROVADO (A-2 conferido) |
| L1-R85 | 1.5 | E | sim | APROVADO (R1) |
| L1-R86 | 1.5 | E | sim | APROVADO (R1; VOLÁTIL) |
| L1-R87 | 1.5 | E | sim | APROVADO (novo; VOLÁTIL) |
| L1-R88 | 1.5 | C | não | APROVADO (R1; VOLÁTIL) |
| L1-R89 | 1.6 | C | não | APROVADO (R1) |
| L1-R90 | 1.6 | E | sim | APROVADO (A-3 conferido) |
| L1-R91 | 1.6 | C | não | APROVADO (R1) |
| L1-R92 | 1.6 | C | não | APROVADO (A-4 conferido) |
| L1-R93 | 1.6 | E | sim | APROVADO (R1) |
| L1-R94 | 1.6 | E | sim | APROVADO (R1) |
| L1-R95 | 1.6 | C | sim | APROVADO (R1) |
| L1-R96 | 1.6 | C | não | APROVADO (R1) |
| L1-R97 | 1.6 | E | sim | APROVADO (R1) |
| L1-R98 | 1.6 | E | não | APROVADO (R1) |
| L1-R99 | 1.6 | C | sim | APROVADO (novo; ressalva de formato, seção 5.1) |
| L1-R100 | 1.6 | C | não | APROVADO (R1; SHA-256 registrado e conferido) |
| L1-R101 | 1.6 | E | sim | APROVADO (novo; ressalva de rótulo, seção 5.2) |
| L1-R102 | 1.6 | E | sim | APROVADO (novo) |

## 8. Taxa e veredito

Reprovados: 0/28 = 0% (gate de 30% não acionado). AJUSTAR: 0. APROVADOS: 28.
Veredito geral: **APROVADO COM RESSALVAS** — ressalvas só de registro e D1/D2 da Gerência (formato do R99; uniformização de VOLÁTIL R87 × R101/R84; lista de conferência de janeiro; repetição de abertura "Segundo a…"), nenhuma com efeito sobre texto ou gabarito. Não há rodada 3: a parte C segue para a reconciliação da gce-gerencia.
