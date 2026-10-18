# QA_T96A_R2_2026-10-18_gce-cqfp.md — T-96 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L1_reforco_onda2_A_v2.md (gce-cpp), comparada com a v1 por diff integral. Rodada 2 de 2 (última; D-REFORCO-2). Critérios: os mesmos do parecer R1 (QA_T96A_R1_2026-10-18_gce-cqfp.md): D-REFORCO-1/2, D-T89-R1-ACEITE (critério de VOLÁTIL), T89 seção 3 (onda 2: [TS] ≥ metade + 2; nenhuma "definição" nova em 1.2), T93 O-1 a O-8, edital P2-1.2 ("Modelos de fala end-to-end").
A QA revisa; não reescreve.

## 1. Diff v1 → v2 (o que mudou, e só isso)
O diff tem 27 blocos, todos dentro do escopo do parecer: cabeçalho (linha 1 e bloco de resposta); mapa de R20, R40, R43, R44, R45; contagens de formato de 1.2; verificação de não repetição; tetos; Parte 2 de R20, R31, R40, R43, R44, R45, R46; Parte 3 de R31, R40, R43, R44, R45, R46; contagens, recontagem O-1, proveniência (só a coluna "itens") e dúvidas 1, 3 e 4. Nenhum dos outros 21 itens mudou (enunciado, gabarito, [TS], justificativa). CONFERE.

## 2. Ajustes A-1 a A-4 (texto exato)
| ajuste | Parte 2 | Parte 3 / mapa | veredito |
|---|---|---|---|
| A-1 (R20) | texto idêntico ao do parecer ("…e atribui o excesso de supressões, em regra, ao sinal de áudio fraco.") | Parte 3 intacta, como mandado; mapa conforme | APLICADO |
| A-2 (R31) | enunciado idêntico | trecho substituído e frase da "leitura par incorreto" apagada; gabarito C | APLICADO |
| A-3 (R45) | enunciado idêntico | "ou processamento em blocos (buffered chunked)" retirado; mapa conforme | APLICADO |
| A-4 (R46) | enunciado idêntico | trecho substituído; C e [TS] espelho mantidos | APLICADO |

## 3. Evidência — reaberta pela QA em 18/10/2026 (curl, HTTP 200)
| fonte | resultado | trecho literal |
|---|---|---|
| raw.githubusercontent.com/espnet/espnet/master/README.md | CONFERE | "Hybrid CTC/attention based end-to-end ASR — Fast/accurate training with CTC/attention multitask training — CTC/attention joint decoding to boost monotonic alignment decoding — Encoder: VGG-like CNN + BiRNN (LSTM/GRU), sub-sampling BiRNN (LSTM/GRU), Transformer, Conformer, Branchformer, or E-Branchformer — Decoder: RNN (LSTM/GRU), Transformer, or S4"; "comparable/superior to hybrid DNN/HMM and CTC"; "Restricted Self-Attention based on Longformer as an encoder for long sequences" (R40, R44, R45, R46) |
| raw.githubusercontent.com/facebookresearch/fairseq/main/examples/wav2vec/README.md | CONFERE | tabela de checkpoints do wav2vec 2.0: splits "10 minutes", "100 hours", "960 hours" (Base, Large, Large LV-60, LV-60 + Self Training); variantes conformer só 100 h e 960 h; robust: "960 hours Librispeech" e "300 hours Switchboard". Menor split listado = 10 minutos (R43) |
| raw.githubusercontent.com/NVIDIA/NeMo/main/docs/source/asr/intro.rst | CONFERE | "Long Audio — Inference on audio over 1 hour via local attention or buffered chunked processing." (R45 após A-3) |

## 4. Itens novos (folha 1.2, E, [TS])
- L1-R40 (TS, E). Gabarito E correto pelo README literal (Conformer está na linha Encoder; Decoder = RNN, Transformer ou S4; também no Transducer o Conformer é só do encoder). Escopo de 1.2: arquitetura codificador/decodificador de modelo end-to-end — DENTRO; o fato é conceitual e estável (o Conformer é, por construção, um codificador). Troca única: papel codificador → decodificador. Ponto único contra os 19 da folha e contra B, C, D (nenhuma ocorrência de Conformer em B_v2, C_v1, D_v2 nem no pacote v1.9). Sem "definição". Estilo: situação de uso + atribuição à fonte, 37 palavras. APROVADO.
- L1-R44 (PC, E). Gabarito E correto ("multitask training" + "joint decoding"). Escopo DENTRO (treinamento e decodificação de modelo end-to-end híbrido). Troca única: o treinamento, que é multitarefa CTC/atenção, passa a "somente atenção"; "apenas na decodificação" é a mesma troca enunciada pelo outro lado, não um segundo conceito. Distinto de R41 (finalidade da decodificação conjunta) e do item multitarefa do pacote (Whisper multilíngue/multitarefa, outro sentido). Ausente de B, C, D. APROVADO.
- L1-R43 (NP, E). Gabarito E correto pela tabela (10 minutos, não 10 horas). REPROVADO, por três motivos: (a) relevância e escopo: o ponto que decide o item é uma célula de tabela de checkpoints de um repositório ("Nessa lista, o menor conjunto…"), não um conceito de "Modelos de fala end-to-end"; é a mesma categoria que reprovou o R40 da v1 (fato de checkpoint específico), e manter um e reprovar o outro seria incoerente; (b) estabilidade e recurso: "10 horas" é também um split de ajuste fino do próprio experimento do wav2vec 2.0 (Libri-light 10 min / 1 h / 10 h / 100 h), ausente da tabela mas presente na literatura do modelo; a candidata que conhece o artigo e não o README fica exposta, e a lista do repositório pode mudar sem aviso — a troca "10 minutos × 10 horas" premia memorização de tabela, não domínio do tema; (c) o conceito subjacente (pouco áudio transcrito basta após pré-treinamento auto-supervisionado) não pode ser reaproveitado aqui sem colidir com R34 e L1-Q04. Sem ajuste possível na última rodada.

## 5. Veredito por item (28)
| id | folha | gab. | [TS] | veredito R2 |
|---|---|---|---|---|
| L1-R19 | 1.1 | E | sim | APROVADO |
| L1-R20 | 1.1 | C | não | APROVADO (A-1 aplicado) |
| L1-R21 | 1.1 | E | não | APROVADO |
| L1-R22 | 1.1 | C | não | APROVADO |
| L1-R23 | 1.1 | E | sim | APROVADO |
| L1-R24 | 1.1 | E | sim | APROVADO (VOLÁTIL baixo) |
| L1-R25 | 1.1 | C | espelho | APROVADO |
| L1-R26 | 1.1 | C | não | APROVADO |
| L1-R27 | 1.1 | E | sim | APROVADO |
| L1-R28 | 1.1 | C | espelho | APROVADO |
| L1-R29 | 1.1 | E | sim | APROVADO (VOLÁTIL baixo) |
| L1-R30 | 1.1 | E | sim | APROVADO |
| L1-R31 | 1.1 | C | não | APROVADO (A-2 aplicado) |
| L1-R32 | 1.1 | C | não | APROVADO |
| L1-R33 | 1.2 | E | sim | APROVADO |
| L1-R34 | 1.2 | C | não | APROVADO |
| L1-R35 | 1.2 | E | sim | APROVADO |
| L1-R36 | 1.2 | C | não | APROVADO |
| L1-R37 | 1.2 | C | não | APROVADO |
| L1-R38 | 1.2 | E | não | APROVADO |
| L1-R39 | 1.2 | C | espelho | APROVADO |
| L1-R40 | 1.2 | E | sim | APROVADO (novo) |
| L1-R41 | 1.2 | E | sim | APROVADO |
| L1-R42 | 1.2 | C | não | APROVADO |
| L1-R43 | 1.2 | E | sim | REPROVADO (novo; seção 4) |
| L1-R44 | 1.2 | E | sim | APROVADO (novo) |
| L1-R45 | 1.2 | C | não | APROVADO (A-3 aplicado) |
| L1-R46 | 1.2 | C | espelho | APROVADO (A-4 aplicado) |
(Gabaritos e [TS] dos 21 itens inalterados conferidos contra a tabela do R1; estado dos itens 1.1 transcrito do R1, sem mudança no diff.)

## 6. Tetos com a reprovação
- Gabarito da parte: 14 C / 13 E (51,9% de C) — dentro de 40–60%. Folha 1.2: 7 C / 6 E.
- [TS]: 15/27. Mínimo T89 seção 3 (metade + 2) = 15,5 → 16: fica 1 abaixo; o substituto de R43 precisa ser E com [TS].
- Formato 1.2 (19): PC 5 (26%), maior formato dentro do teto; "definição" nova: 0. VOLÁTIL 1.2: 0. Folha 1.2 fica com 19/20.
- Estilo O-1 a O-8: novos itens conformes (comando "Julgue o item.", sem pista de extensão, atribuição à fonte). Normativo: nenhuma norma citada; sem PENDENTE NORMATIVO.

## 7. Taxa e veredito
Reprovados na R2: 1/28 = 3,6% (L1-R43), abaixo do gate de 30%. Aprovados: 27 (4 com ajuste aplicado, 2 novos).
Veredito geral: APROVADO COM RESSALVAS. Ressalvas à gce-gerencia (D1): (1) R43 não volta a esta parte (R2 é a última rodada); repor 1 item de 1.2, E com [TS], sem "definição", ponto conceitual e não tabelar, com QA própria, para devolver 1.2 a 20 e o [TS] da parte a 16; (2) registros do R1 mantidos (R34 × L1-Q04; R37 × L2-R04; R35 × L1-R119 da parte D na consolidação); (3) QA PENDENTE sai dos 27 aprovados só após a reconciliação da Gerência.
