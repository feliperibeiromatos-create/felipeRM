# L1_reforco_onda2_saldo_v2.md — T-103 — 2026-10-18 — gerado por gce-cpp

## Resposta ao parecer QA_T103_R1_2026-10-18_gce-cqfp.md (R1)

| ponto do parecer | resposta |
|---|---|
| Veredito AJUSTAR: [TS] de troca única violado pela oração "o que impede combiná-los com proveito" (E4) | acatado. Oração suprimida; o enunciado do L1-R131 termina em "...e o autotreinamento (self-training) são técnicas excludentes." Com "complementares" no lugar de "excludentes" o item fica C (troca única). A linha [TS] e a justificativa seguem coerentes com o novo fim: a justificativa já falava só da troca de "complementares" por "excludentes". Item de 40 palavras (eram 46). |
| Gabarito comentado: acrescentar "Complementary" consta do próprio README | acatado. Frase acrescentada ao fim da primeira linha do gabarito. |
| Seções 2 e 3: A_v2 e D_v2 por A_v3 e D_v3 | acatado. Referências trocadas. |
| Ressalvas (ponto conceitual; escopo 1.2) | sem alteração pedida; mantidas. |

Nada mais mudou em relação à v1. QA PENDENTE até a R2 (conferência do diff) da gce-cqfp.


Tarefa T-103, saldo da onda 2 do reforço (D-REFORCO-2), ciclo s12c3. Escopo: 1 item AUTORAL, L1-R131, folha P2-1.2, em reposição ao L1-R43 (retirado na T96_reconciliacao, seção 1; o id L1-R43 não é reutilizado). Rótulo: AUTORAL. QA PENDENTE: o item não passou por QA (D-QA-PENDENTE) e não entra em simulado antes da R1 da gce-cqfp. Convenção de base: "verificado em 18/10/2026" significa página aberta e lida nesta data, nesta sessão (HTTP 200); nenhuma data anterior foi usada (D-FONTE-DATA-ANTERIOR não foi necessária). Nenhuma norma citada.

=====================================================================
PARTE 1/3 — MAPA
=====================================================================

## 1.1 Item novo

Formatos: D = definição; TS = troca de sujeito; SH = situação hipotética; NP = número ou prazo; PC = par confundível; AP = aplicação parlamentar.

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL |
|---|---|---|---|---|---|
| L1-R131 | P2-1.2 | Pré-treinamento auto-supervisionado (aprende de áudio sem rótulos) e autotreinamento (self-training) são técnicas complementares no modelo end-to-end wav2vec 2.0, e não excludentes: a combinação de ambas é tratada como proveitosa | SH | https://raw.githubusercontent.com/facebookresearch/fairseq/main/examples/wav2vec/README.md (repositório oficial facebookresearch/fairseq, parágrafos iniciais) | n |

## 1.2 Atendimento dos requisitos da T-103

| requisito | atendimento |
|---|---|
| folha P2-1.2 | sim; entrada 1.2 do edital ("Modelos de fala end-to-end") |
| gabarito E com [TS] de troca única | sim; troca única de "complementares" por "excludentes" |
| formato diferente de definição e de par confundível | sim; formato SH (situação hipotética). Troca de sujeito era preferência, não exigência: o ponto escolhido (relação entre duas técnicas) não admite troca de sujeito sem segunda troca ou sem afirmação que o README não sustenta literalmente; o [TS] é de predicado (um único termo) |
| ponto conceitual de modelo end-to-end, e não fato de tabela, checkpoint ou lista de repositório | sim; a relação entre aprendizado auto-supervisionado e autotreinamento é conceito de treinamento, e o trecho-base é prosa do README (parágrafos iniciais), e não a tabela "Pre-trained models" |
| ponto distinto dos 19 da folha | sim (seção 2) |
| sem gêmeo em outra folha | sim (seção 3) |
| base oficial aberta hoje, trecho literal, "verificado em 18/10/2026" | sim (Parte 3) |
| não VOLÁTIL | sim; relação entre técnicas de treinamento descrita no README de um projeto, sem versão, preço, limite ou recurso de produto |

## 2 Verificação de não repetição na folha P2-1.2 (os 19 vigentes)

Conferidos: pacote.json v1.9 (L1-Q03, L1-Q04, L1C-Q23, L1C-Q24, L1-R03, L1-R04), L1_reforco_onda1_v2.md e L1_reforco_onda2_A_v3.md/T96_reconciliacao (R33 a R42, R44 a R46).

| vizinho | ponto do vizinho | por que R131 é distinto |
|---|---|---|
| L1-R34 | wav2vec 2.0 aprende de dados não rotulados (pré-treinamento) | R34 julga o uso de áudio sem transcrição no pré-treinamento; R131 julga a relação do pré-treinamento com o autotreinamento (complementares ou excludentes) |
| L1-R42 | dados de múltiplos domínios no pré-treinamento, para a mudança de domínio | R42 julga a estratégia de domínio; R131 não trata de domínio |
| L1-Q04 | pares áudio-texto continuam necessários (supervisão fraca) | Q04 julga a necessidade de pares; R131 não julga necessidade de rótulos |
| L1-R33, R03, R04, R38, R39, R40, R41, R44, R45, R46, Q03, Q23, Q24, R35, R36, R37 | outros pontos (autorregressão, tokens de tarefa, janelas, repetição, LM externo, Conformer, CTC, atenção local, desempenho frente a DNN/HMM, alucinação, dicionário, espectrograma, dados do Whisper, avaliação no domínio) | nenhum trata de autotreinamento nem de sua relação com o pré-treinamento |
| L1-R43 (retirado) | menor conjunto de ajuste fino do wav2vec 2.0 | id não reutilizado; o ponto de R131 não é o do R43 (tabela de checkpoints) |

## 3 Verificação de gêmeos em outras folhas

Conferido contra: pacote.json v1.9 inteiro (busca por "autotreinamento", "self-training", "pseudo-rótulo", "wav2vec"; única ocorrência de wav2vec em outra parte do pacote: L1C-Q24, da própria 1.2); L1_reforco_onda1_v2.md; L1_reforco_onda2_A_v3.md; B_v2, C_v2 e D_v3 (único registro de wav2vec fora da A: nota de substituição do L1-R43 na C_v2, sem item); lista de gêmeos da T96_reconciliacao, seção 4 (8 pares; R131 não figura em nenhum). Resultado: nenhum item de outra folha julga autotreinamento ou a relação com o pré-treinamento. Sem gêmeo.

## 4 Contagens

| quesito | valor |
|---|---|
| item novo | 1 (L1-R131) |
| gabarito | E (1 E, 0 C) |
| [TS] | 1 (R131) |
| VOLÁTIL | 0 |
| P2-1.2 depois do saldo | 20 itens (19 + 1) |
| formatos de P2-1.2 (de 20) | D 2, PC 5, TS 2, NP 2, SH 5, AP 4 (maior: PC, 25%; SH 25%); teto de 30% cumprido; definição nova: 0 |
| VOLÁTEIS em P2-1.2 | 0/20 |
| onda 2 com o saldo | 56 C / 56 E de 112 = 50,0% de C (regra 5: faixa de 40% a 60%) |
| [TS] da onda 2 com o saldo | 66 de 112 (58,9%) |
| CONFERÊNCIA DE BASE (jan/2027) | R131 (reabrir a URL e conferir os dois trechos da Parte 3) |

Estilo (regras/estilo_banca.md): E por troca de um único termo (E4), sem marcador absoluto ("sempre", "só", "apenas", "qualquer") no enunciado; item de 40 palavras.

FIM DA PARTE 1/3

=====================================================================
PARTE 2/3 — (d) ITEM DO ESTUDANTE
=====================================================================

L1-R131. Julgue o item.
Uma equipe da Câmara dispõe de extenso acervo de áudio de sessões sem transcrição e de poucas horas de áudio transcrito. Nessa situação, segundo o README oficial do wav2vec 2.0, o pré-treinamento auto-supervisionado e o autotreinamento (self-training) são técnicas excludentes.

FIM DA PARTE 2/3

=====================================================================
PARTE 3/3 — (d-G) GABARITO COMENTADO
=====================================================================

L1-R131. E [TS]. O README do wav2vec 2.0 trata o pré-treinamento auto-supervisionado (aprendizado de representações a partir de áudio sem rótulos) e o autotreinamento como técnicas complementares, tanto que registra a combinação das duas. O item troca "complementares" por "excludentes". "Complementary" consta do próprio README, no texto do link da linha 7.
Base: facebookresearch/fairseq, README do wav2vec 2.0 (https://raw.githubusercontent.com/facebookresearch/fairseq/main/examples/wav2vec/README.md), arquivo aberto e lido em 18/10/2026 (HTTP 200; verificado em 18/10/2026). Trechos literais: "wav2vec 2.0 learns speech representations on unlabeled data as described in [wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations (Baevski et al., 2020)]"; "We also combined wav2vec 2.0 with self-training in [Self-training and Pre-training are Complementary for Speech Recognition (Xu et al., 2020)]". O item não afirma ganho numérico. Autotreinamento como uso de rótulos gerados por um modelo sobre áudio sem transcrição é conceito geral, sem fonte de fornecedor, e não é necessário para decidir o item. Não VOLÁTIL. CONFERÊNCIA DE BASE (4–8/1/2027).

## Tabela de proveniência (página aberta e lida em 18/10/2026)
| fonte | URL oficial | data da página / verificação | usada em |
|---|---|---|---|
| Meta, repositório oficial facebookresearch/fairseq, README do wav2vec 2.0 (ramo main) | https://raw.githubusercontent.com/facebookresearch/fairseq/main/examples/wav2vec/README.md | arquivo sem data de página; aberto e lido em 18/10/2026 (HTTP 200); verificado em 18/10/2026 | R131 |

Fontes abertas na busca do ponto e não usadas (nenhum item depende delas): raw.githubusercontent.com openai/whisper (README, model-card), espnet/espnet (README), NVIDIA/NeMo (intro.rst, asr_language_modeling_and_customization.rst); cloud.google.com Chirp 3; learn.microsoft.com (nota de transparência do Speech); docs.aws.amazon.com (what-is, how-it-works). Pontos descartados por gêmeo ou escopo: pontuação embutida no modelo (já no pacote, outra folha), CTC não autorregressivo (vizinho próximo do R33), tabela de decodificadores do NeMo (fato de tabela), tradução do Whisper para o inglês (L1-R16, 1.8), modelos .en (L1-R117, 1.8), detecção de atividade de voz e diarização (1.4 e R126).

## Dúvidas à Gerência (D1 da gce-gerencia)
1. Natureza da base: o README do fairseq é documentação oficial do projeto, não ferramenta nomeada no edital (1.8); admissibilidade já aceita para os itens R34, R42 e demais da parte A (mesma dúvida 1 da A_v3). Se a Gerência preferir, a QA confere o trecho do texto-âncora do link sobre autotreinamento como texto literal do README.
2. Formato: troca de sujeito não foi viável sem segunda troca ou afirmação não literal; o item é SH. A 1.2 fica em SH 5/20 (25%).

FIM DA PARTE 3/3
FIM DO LOTE
