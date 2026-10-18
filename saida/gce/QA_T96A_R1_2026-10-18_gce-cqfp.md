# QA_T96A_R1_2026-10-18_gce-cqfp.md — T-96 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L1_reforco_onda2_A_v1.md (gce-cpp; 28 itens AUTORAL, L1-R19 a L1-R46; folhas P2-1.1 e P2-1.2). Rodada 1 de no máximo 2 (D-REFORCO-1/2).
Critérios: D-REFORCO-1 e 2 (regras 1 a 6), D-FONTE-DATA-ANTERIOR, D-T89-R1-ACEITE (critério de VOLÁTIL da seção 1 da T89_reconciliacao), D-ONDA2-FILA, T89_reconciliacao seção 3 (onda 2: [TS] ≥ metade + 2; nenhuma "definição" nova em 1.2), T93_reconciliacao O-1 a O-8, edital/modulo_RF_IA_P2.md (transcrição literal), pacote.json v1.9 (existentes de 1.1 e 1.2) e canônicos do Lote 1.
A QA revisa; não reescreve. Os textos de ajuste abaixo são o texto exato a aplicar; nada mais muda.

## 1. Evidência — URLs reabertas pela QA em 18/10/2026 (curl, todas HTTP 200)

| fonte | resultado | trechos conferidos (literal) |
|---|---|---|
| learn.microsoft.com …/how-to-custom-speech-evaluate-data ("Last updated on 2025-12-29") | CONFERE | "divides the sum by the total number of words provided in the human-labeled transcript (N)"; definições de Insertion/Deletion; "select an acoustic dataset that's different from the one you used with your model… more realistic sense"; "many deletion errors, it's usually because of weak audio signal strength"; "Substitution errors often occur when an insufficient sample of domain-specific terms…" (R19, R20, R22, R27) |
| raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm (v. 1.5) | CONFERE, com ressalva em R31 | "global minimization of a Levenshtein distance function… 0, 3, 3 and 4"; "precision of generated statistics is directly correlated…"; transcrições de referência alternativas ("what are"/"what're"); "treating word errors with equal weight"; "Weighted-Word-Scoring" como "variation"; "Percent of sentence errors = # incorrect ref and hyp pairs / # ref and hyp pairs". A página NÃO define "par incorreto" (R31) |
| cloud.google.com/speech-to-text/docs/best-practices ("Last updated 2026-10-13") | CONFERE | "16,000 Hz or higher… avoid re-sampling… telephony the native rate is commonly 8000 Hz"; "Use a lossless codec… Using mp3… may reduce accuracy"; "Multiple people talking at the same time… may be interpreted as background noise and ignored"; "applying noise-reduction signal processing… typically reduces recognition accuracy" (R23, R24, R25, R29) |
| docs.aws.amazon.com/transcribe/latest/dg/how-input.html | CONFERE | "lossless formats are recommended for both"; "telephone recordings, typically use 8,000 Hz" (R23, R25) |
| docs.aws.amazon.com/transcribe/latest/dg/alternatives.html | CONFERE | "creates different versions of the same transcript and assigns a confidence score… you only get the version with the highest confidence score" (R32) |
| raw.githubusercontent.com/openai/whisper/main/README.md | CONFERE | l. 125: "sliding 30-second window, performing autoregressive sequence-to-sequence predictions on each window" (R33) |
| raw.githubusercontent.com/openai/whisper/main/model-card.md | CONFERE | 680,000 h; 65% inglês/inglês; 18%; 17%; "directly correlated with the amount of training data"; "strongly recommend… robust evaluations… context and domain"; "prone to generating repetitive texts… mitigated to some degree… but not perfectly"; "disparate performance on different accents and dialects"; "cannot be used for real-time transcription out of the box" (R35–R38, R43, R44) |
| raw.githubusercontent.com/facebookresearch/fairseq/main/examples/wav2vec/README.md | CONFERE | "learns speech representations on unlabeled data"; "We combined speech data from multiple domains in [Robust wav2vec 2.0: Analyzing Domain Shift…]"; tabela XLSR-53 (Languages = 53); MLS e CommonVoice com Portuguese (R34, R40, R42) |
| raw.githubusercontent.com/NVIDIA/NeMo/main/docs/source/asr/intro.rst | CONFERE | "n-gram LM fusion (NGPU-LM) for CTC, RNN-T, TDT, and AED models improves transcription accuracy without retraining"; "Long Audio — … via local attention or buffered chunked processing" (R39, R45) |
| raw.githubusercontent.com/espnet/espnet/master/README.md | CONFERE | l. 298 "State-of-the-art performance in several ASR benchmarks (comparable/superior to hybrid DNN/HMM and CTC)"; l. 301 "CTC/attention joint decoding to boost monotonic alignment decoding"; l. 305 "…trained only with text data"; l. 339 "Restricted Self-Attention based on Longformer… for long sequences" (R39, R41, R45, R46) |

Bases não reabertas: nenhuma (10/10 reabertas). O artigo do arXiv citado no README do fairseq (Hsu et al., 2021; base implícita de R42) não abre na rede (arxiv.org fechado) e não é citado no item; registrado. Nenhuma base de data anterior (D-FONTE-DATA-ANTERIOR não aplicável). Nenhuma norma citada: sem PENDENTE NORMATIVO.

## 2. Pontos de julgamento levantados pela produtora (Dúvidas 1 a 4)

1. Escopo de fairseq, NeMo e ESPnet (R34, R39–R42, R45, R46). O texto do edital em 1.2 é conceitual ("Modelos de fala end-to-end") e não restringe a base às ferramentas do 1.8; a documentação oficial dos projetos é "documento oficial" na regra 2 da D-REFORCO-2. Itens cujo ponto é conceito de modelo end-to-end (pré-treinamento auto-supervisionado, CTC/atenção, fusão de LM, atenção restrita, comparação com híbridos) estão DENTRO de 1.2: R34, R39, R41, R42, R45, R46. R40 está FORA: o ponto é a lista de idiomas de um checkpoint específico (XLSR-53), não previsto no edital; o tema (modelo multilíngue que cobre o português) pertence a 3.4. A decisão sobre a natureza da base é D1 da gce-gerencia; o parecer da QA é pela admissibilidade.
2. VOLÁTIL. Concordo com R24 e R29 VOLÁTEIS (risco baixo): descrevem comportamento do reconhecedor vigente (robustez a ruído, vozes sobrepostas), que muda com o modelo. R23 e R25 NÃO VOLÁTEIS: princípio de engenharia de áudio (codec sem perda; não reamostrar), coincidente em dois fornecedores, não dependente de versão, limite, preço ou modelo padrão (critério da T89, seção 1); ficam na conferência de base de 4–8/1/2027. Mesmo reclassificados, 1.1 ficaria em 4/20 (20%), no teto.
3. R43 (sotaques) e R44 (tempo real). O ponto decisivo de cada um é literalmente o tema de outra folha ("sotaques", 1.6; "Transcrição em tempo real", 1.7), em produção paralela, onde a QA não consegue conferir a unicidade do ponto. REPROVADOS na folha 1.2 (ver seção 3); a Gerência pode transferi-los a 1.6/1.7 depois de conferir duplicata com a produção paralela, sem nova QA de texto.
4. R31. A página do NIST traz a fórmula, não a definição de "par incorreto". Ajuste de texto abaixo (mantém o gabarito C e o "independentemente" pedido pelo O-2).

## 3. Veredito por item

| id | folha | gab. | [TS] | formato | VOL | veredito | motivo |
|---|---|---|---|---|---|---|---|
| L1-R19 | 1.1 | E | sim | NP | n | APROVADO | conta 3+1+2 = 6; hipótese 51; 6/51 ≈ 11,8% aritmeticamente certo, troca única = denominador; base MS/NIST literal; distinto de L1C-Q22 (limite > 100%) |
| L1-R20 | 1.1 | C | não | AP | n | APROVADO COM AJUSTE A-1 | a página vai de "muitas supressões" para "sinal fraco", e não de "sinal fraco" para "sobretudo supressões"; inverter a direção da segunda oração deixa o C exposto a recurso |
| L1-R21 | 1.1 | E | não | SH | n | APROVADO | base literal ("precision… directly correlated…"); a restrição "só… exatamente o mesmo erro" é a falsidade; cauda não se denuncia (O-5) |
| L1-R22 | 1.1 | C | não | SH | n | APROVADO | nota literal da página MS |
| L1-R23 | 1.1 | E | sim | AP | n | APROVADO | Google e AWS recomendam sem perda; troca única perda↔sem perda; não VOLÁTIL (seção 2) |
| L1-R24 | 1.1 | E | sim | PC | S baixo | APROVADO | trecho literal "typically reduces"; VOLÁTIL correto; REVERIFICAR |
| L1-R25 | 1.1 | C | espelho | NP | n | APROVADO | literal Google (16.000 Hz ou mais; telefonia 8.000 Hz; sem reamostrar); não VOLÁTIL |
| L1-R26 | 1.1 | C | não | D | n | APROVADO | literal NIST; D em 1.1 = 3/20 |
| L1-R27 | 1.1 | E | sim | TS | n | APROVADO | troca de papéis inserção/supressão (um conceito); literal MS |
| L1-R28 | 1.1 | C | espelho | AP | n | APROVADO | literal NIST (referências alternativas); "para"/"pra" é aplicação legítima |
| L1-R29 | 1.1 | E | sim | AP | S baixo | APROVADO | literal Google; VOLÁTIL correto; REVERIFICAR |
| L1-R30 | 1.1 | E | sim | PC | n | APROVADO | inverte padrão (peso igual) e variação (ponderada); literal NIST |
| L1-R31 | 1.1 | C | não | PC | n | APROVADO COM AJUSTE A-2 | "um único erro de palavra torna o par incorreto" não está na página (só a fórmula); retirar a leitura não literal |
| L1-R32 | 1.1 | C | não | D | n | APROVADO | literal AWS; "pode" e "em geral" seguram a generalização; distinto de L1-R02 |
| L1-R33 | 1.2 | E | sim | PC | n | APROVADO | literal README l. 125; distinto de L1-R04 (janela de 30 s) e de L1-R03 (tokens de tarefa) |
| L1-R34 | 1.2 | C | não | AP | n | APROVADO | literal fairseq; conceito de 1.2. Registro: convive com L1-Q04 (C, pares áudio–texto continuam necessários) sem contradição, porque o item fala só do pré-treinamento; a justificativa do estudante deve manter a menção ao ajuste fino com áudio transcrito |
| L1-R35 | 1.2 | E | sim | NP | n | APROVADO | 65% inglês/inglês, literal; propriedade do artefato (não VOLÁTIL). Registro: tema de Whisper também cabe em 1.8 (produção paralela); a Gerência confere duplicata ao consolidar |
| L1-R36 | 1.2 | C | não | SH | n | APROVADO | literal model card ("directly correlated"; "lower accuracy… less training data"); distinto de L1-R11 (1.6) |
| L1-R37 | 1.2 | C | não | AP | n | APROVADO | literal model card. Registro: mesmo trecho-base de L2-R04 (2.2, "compete à instituição avaliar…"); folhas diferentes, regra 1 não violada; item de baixa dificuldade |
| L1-R38 | 1.2 | E | não | AP | n | APROVADO | "but not perfectly", literal; "pode" em E (O-3) |
| L1-R39 | 1.2 | C | espelho | SH | n | APROVADO | NeMo ("without retraining") e ESPnet ("trained only with text data") literais; ponto distinto de L1C-Q23 e de L2-Q28 (2.8) |
| L1-R40 | 1.2 | E | sim | NP | n | REPROVADO | escopo: o ponto é fato de checkpoint específico (idiomas do XLSR-53), não previsto no edital; o tema (modelo multilíngue que cobre o português) é de 3.4 (onda 4), não de 1.2; extrapolação punível em recurso |
| L1-R41 | 1.2 | E | sim | PC | n | APROVADO | literal ESPnet l. 301 (alinhamento monotônico); troca única |
| L1-R42 | 1.2 | C | não | AP | n | APROVADO | literal fairseq ("combined speech data from multiple domains" em estudo intitulado "Robust wav2vec 2.0: Analyzing Domain Shift…"); "estratégia documentada para tratar a mudança de domínio" é leitura do título, aceitável sem afirmar ganho; arXiv não aberto (registro); CONFERÊNCIA DE BASE |
| L1-R43 | 1.2 | E | sim | AP | n | REPROVADO | escopo da folha: o ponto (desempenho desigual entre sotaques) é o texto literal do 1.6 ("sotaques"), folha em produção paralela; unicidade do ponto não conferível; transferível a 1.6 por D1 da Gerência após conferência de duplicata |
| L1-R44 | 1.2 | E | sim | SH | n | REPROVADO | escopo da folha: o ponto (uso em tempo real) é o título do 1.7, folha em produção paralela; mesma solução do R43 (transferência a 1.7 ou 1.8 após conferência) |
| L1-R45 | 1.2 | C | não | SH | n | APROVADO COM AJUSTE A-3 | "processamento do áudio em blocos sequenciais" repete, no essencial, o ponto de L1-R04 (janelas sucessivas de 30 s, mesma folha); o ponto próprio é a atenção local/restrita |
| L1-R46 | 1.2 | C | espelho | PC | n | APROVADO COM AJUSTE A-4 | o README afirma o desempenho dos modelos do próprio toolkit (lista de recursos do ESPnet), não da "abordagem end-to-end" em geral; atribuir a afirmação ao que a fonte diz |

## 4. Ajustes (texto exato)

A-1 (L1-R20, Parte 2). Substituir
"A documentação da Microsoft costuma associar esse padrão de erro à amostra insuficiente de termos do domínio, e relaciona o sinal de áudio fraco, sobretudo, às supressões."
por
"A documentação da Microsoft costuma associar esse padrão de erro à amostra insuficiente de termos do domínio, e atribui o excesso de supressões, em regra, ao sinal de áudio fraco."
Parte 3: na justificativa, nada muda (já diz "associa muitas supressões a sinal de áudio fraco"). Mapa: ponto passa a "…e o excesso de supressões associa-se ao sinal fraco".

A-2 (L1-R31, Parte 2). Substituir o enunciado inteiro por
"Na taxa de erro de sentença, calculada em ferramentas de pontuação como o sclite, do NIST, divide-se o número de pares de referência e hipótese incorretos pelo total de pares, independentemente do número de palavras de cada par."
Parte 3: substituir "de modo que um único erro de palavra torna o par incorreto, sejam quantas forem as palavras certas do par" por "e não o número de palavras erradas pelo total de palavras"; apagar a frase "A leitura "par incorreto = par com ao menos um erro de palavra" é a do cálculo; a página não a escreve literalmente." Gabarito C mantido.

A-3 (L1-R45, Parte 2). Substituir o enunciado inteiro por
"Na transcrição de uma sessão do Plenário com várias horas de duração, modelos end-to-end podem recorrer a mecanismos de atenção local ou restrita no codificador, documentados em toolkits abertos, para processar sequências longas de áudio."
Parte 3: substituir "O NeMo documenta inferência em áudio com mais de uma hora por atenção local ou processamento em blocos (buffered chunked), e o ESPnet lista" por "O NeMo documenta inferência em áudio com mais de uma hora por atenção local, e o ESPnet lista". Mapa: ponto passa a "Para áudio longo, modelos end-to-end recorrem a atenção local ou restrita no codificador". Gabarito C mantido.

A-4 (L1-R46, Parte 2). Substituir o enunciado inteiro por
"Segundo a documentação do ESPnet, os modelos end-to-end desse toolkit alcançam, em vários benchmarks de reconhecimento de fala, desempenho comparável ou superior ao de sistemas híbridos DNN/HMM, o que não implica superioridade em qualquer condição de uso."
Parte 3: substituir "O item parece subestimar o end-to-end, mas reproduz a documentação" por "O item parece subestimar o end-to-end, mas reproduz o que a documentação afirma sobre os modelos do toolkit". Gabarito C e [TS] espelho mantidos.

## 5. Tetos, gabarito, [TS] e estrutura

- Estrutura: PARTE 1/3 a 3/3, FIM DA PARTE e FIM DO LOTE presentes; Parte 2 com 28 ids e sem gabarito, [TS], VOLÁTIL ou REVERIFICAR (0 ocorrências); Parte 3 com 28 gabaritos. Cabeçalho na forma do CLAUDE.md. Rótulo AUTORAL e QA PENDENTE declarados. CONFERE.
- Gabarito: 14 C / 14 E (50%) como entregue. Sem os 3 reprovados (todos E): 14 C / 11 E (56%), ainda na faixa de 40–60%; as 3 substituições em 1.2 devem ser preferencialmente E para voltar a 50% na parte.
- [TS]: 16/28 como entregue, conferidos um a um: os 12 em E trocam exatamente um conceito (R19 denominador; R23 perda/sem perda; R24 reduz/eleva; R27 papéis; R29 ignorado/transcrito; R30 padrão/variação; R33 autorregressivo; R35 grupo majoritário; R40 inclusão do português; R41 monotônico; R43 uniformidade; R44 tempo real); os 4 C espelho (R25, R28, R39, R46) seguem o O-6. Sem os reprovados: 13/25 — abaixo do mínimo da T89 seção 3 para a parte (metade + 2); as substituições precisam de [TS] (as 3) para voltar a 16/28.
- Formato 1.1 (20): D 3, PC 4, TS 2, NP 3, SH 3, AP 5 → máx. 25%. CONFERE. VOLÁTIL 1.1: 2/20 (10%). CONFERE.
- Formato 1.2: sem os reprovados, 17 itens (D 2, PC 4, TS 1, NP 2, SH 4, AP 4). As 3 substituições: nenhuma "definição" (T89 seção 3); recomenda-se troca de sujeito (só 1 TS na folha), com no máximo 6 por formato. VOLÁTIL 1.2: 0/20. Sem "definição" nova na entrega: CONFERE.
- Estilo Cebraspe (O-1 a O-8): comando "Julgue o item."; extensão equilibrada (C 43,3 × E 41,2 palavras, conferido por amostragem); O-2 cumprido (R31, mantido no A-2); O-3, O-7, O-8 cumpridos; O-5 conferido em R21 e R38. CONFERE.
- Normativo: nenhuma lei citada. Sem PENDENTE NORMATIVO.

## 6. Taxa e veredito

Reprovados: 3/28 = 10,7% (R40, R43, R44), abaixo do gate de 30%. Aprovados com ajuste: 4 (R20, R31, R45, R46). Aprovados: 21.
Veredito geral: APROVADO COM RESSALVAS. Para a R2: aplicar A-1 a A-4 literalmente; substituir R40, R43 e R44 por 3 itens novos de 1.2 (E, com [TS], sem "definição", ponto único contra os 17 restantes e os 6 existentes) ou, por D1 da Gerência, transferir R43/R44 a 1.6/1.7 após conferência de duplicata com a produção paralela e repor 1.2. Registros para a Gerência: R34 × L1-Q04; R37 × L2-R04 (mesmo trecho-base, folhas distintas); R35/R36 × produção paralela de 1.8.
