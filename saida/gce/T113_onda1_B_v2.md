# T113_onda1_B_v2.md — T-113 onda 1 (F1), parte B (P2-1.4, P2-1.5, P2-1.6), rodada de correção R1 — 2026-10-18 — gerado por gce-cpp

## RESPOSTA AO RELATÓRIO DE QA (saida/gce/QA_T113_B_R1_2026-10-18_gce-cqfp.md), item a item

Convenção: "acatado" = aplicado nesta v2; "não acatado + motivo" = não aplicado. Nenhum ponto do relatório foi não acatado. Os 21 itens APROVADOS (R163, R164, R165, R166, R167, R168, R170, R171, R172, R175, R176, R178, R179, R180, R182, R183, R184, R185, R188, R189, R190) seguem com enunciado, gabarito e justificativa idênticos aos da v1; a única mudança neles é de proveniência sem efeito no item (datas ms.date, etiqueta v20250625 em R182 e R189), tratada em "Proveniência" abaixo.

### Achados da seção 1

| nº | achado | resposta | ação na v2 |
|---|---|---|---|
| 1 | R162 gêmeo de L1-R74 | acatado | R162 reprovado; substituto com o mesmo id, de ponto distinto (fala sobreposta na DER) |
| 2 | R186 gêmeo de L2-R124 | acatado | R186 reprovado; substituto com o mesmo id, de ponto distinto (robustez do Whisper a sotaques, ruído e linguagem técnica) |
| 3 | R191 contradiz a documentação vigente e repete L1-R89 | acatado | R191 reprovado; substituto com o mesmo id, de ponto distinto (conjunto de caracteres do português no vocabulário personalizado) |
| 4 | R169 com marca VOLÁTIL errada e folha acima do teto | acatado | R169 reprovado; substituto com o mesmo id, não VOLÁTIL, de modo que a P2-1.4 fica com 3 existentes + 3 novos = 6 de 30 (20,0%); a alternativa D1 da GCE (manter o R169 como VOLÁTIL e retirar outro) não foi usada |
| 5 | R177 extrapola o edital | acatado | R177 reprovado; substituto com o mesmo id, que incide em pontuação e capitalização em transcrições (prompt) |

### Critério de não VOLÁTIL (seção 2)

| nº | ponto | resposta | ação na v2 |
|---|---|---|---|
| 2.1 | NeMo r1.23.0 mantido como não VOLÁTIL, com ressalva de registro; reposição sem NeMo | acatado | observação "modelo ausente do ramo main em 18/10/2026; documentação das versões 1.23 a 2.4" na tabela de proveniência; nenhum dos 5 substitutos usa o NeMo (o do R177 usa o guia da API da OpenAI) |
| 2.2 | Whisper (R181, R182, R189) mantido como não VOLÁTIL; fixar a etiqueta v20250625 | acatado | URL na etiqueta v20250625 em R181 (corrigido), R182 e R189 (só proveniência, texto idêntico); a etiqueta e os trechos de R182 e R189 foram reconferidos nesse endereço; o substituto do R186 também cita o Whisper (cartão do modelo) e está fixado na mesma etiqueta |
| 2.3 | pyannote.metrics (R163 a R166) mantido como não VOLÁTIL | acatado | sem mudança; o substituto do R162 usa a mesma página, em ponto distinto |
| 2.4 | R169 é VOLÁTIL (achado 4); R187 deve ser VOLÁTIL baixo; R190 e R162 corretos | acatado | R169 substituído (achado 4); R187 passa a VOLÁTIL baixo (5.4); R190 inalterado |

### Proximidades (seção 3)

| par | resposta | ação na v2 |
|---|---|---|
| R181 × L1-R81 / R85; R188 × R98; R187 × R97 / R102; R190 × R97 / R102; R167 × R09 / R61 / Q09; R168 / R170 × R69 | acatado (QA: DISTINTO) | sem mudança |
| R182 × L1-R89; R171 × L1-Q07 | acatado (QA: não reprovam) | sem mudança |
| R162 × L1-R74; R186 × L2-R124 | acatado (QA: REPROVAM) | itens substituídos |
| L2-R84 / R85 (P2-2.5) sobre o normalizador do Whisper | acatado (registro) | o R181 corrigido não toca colchetes nem diacríticos, que são os pontos daqueles itens |

### Parecer por item (seção 4)

| id | parecer do QA | resposta | ação na v2 |
|---|---|---|---|
| L1-R162 | REPROVADO | acatado | substituído (SH, C, não VOLÁTIL) |
| L1-R163, R164, R165, R166, R167, R168 | APROVADO | acatado | idênticos à v1 |
| L1-R169 | REPROVADO | acatado | substituído (SH, C, não VOLÁTIL) |
| L1-R170, R171, R172 | APROVADO | acatado | idênticos à v1 |
| L1-R173 | CORRIGIR (registro, 5.1) | acatado | formato AP passa a D no mapa, na Parte 3 e nas tabelas |
| L1-R174 | CORRIGIR (texto, 5.2) | acatado | enunciado, justificativa e ponto do mapa com o texto exato da 5.2 |
| L1-R175, R176 | APROVADO | acatado | idênticos à v1 |
| L1-R177 | REPROVADO | acatado | substituído (SH, E, [TS], VOLÁTIL baixo) |
| L1-R178, R179, R180 | APROVADO | acatado | idênticos à v1 |
| L1-R181 | CORRIGIR (texto, 5.3) | acatado | enunciado e justificativa com o texto exato da 5.3; URL na etiqueta v20250625 |
| L1-R182, R183, R184, R185 | APROVADO | acatado | idênticos à v1 (R182 com a URL na etiqueta v20250625) |
| L1-R186 | REPROVADO | acatado | substituído (D, E, [TS], não VOLÁTIL) |
| L1-R187 | CORRIGIR (VOLÁTIL, 5.4) | acatado | "Base" com VOLÁTIL baixo, REVERIFICAR com o texto da 5.4, coluna VOLÁTIL do mapa em `VOLÁTIL baixo`; enunciado e gabarito idênticos |
| L1-R188, R189, R190 | APROVADO | acatado | idênticos à v1 (R189 com a URL na etiqueta v20250625) |
| L1-R191 | REPROVADO | acatado | substituído (AP, C, VOLÁTIL baixo) |

### Correções com texto exato (seção 5)

| nº | resposta | ação na v2 |
|---|---|---|
| 5.1 R173 | acatado | mapa: coluna formato `D`; Parte 3: "Formato: D."; tabela P2-1.5: linha D `3 / 5 / 8 / 26,7%` e linha AP `4 / 0 / 4 / 13,3%` (conferir a tabela abaixo) |
| 5.2 R174 | acatado | texto literal da 5.2 na Parte 2 e na Parte 3; [TS] mantido (a v2 tem uma única troca: descartar por privilegiar); formato SH; não VOLÁTIL; ponto do mapa conforme a 5.2 |
| 5.3 R181 | acatado | texto literal da 5.3 na Parte 2 e na Parte 3; gabarito C; formato PC; não VOLÁTIL; URL na etiqueta v20250625; o código foi reaberto na etiqueta e os trechos "s = s.lower()" e "Replace any other markers, symbols, punctuations with a space" conferem; os dois trechos do exemplo coincidem depois do normalizador |
| 5.4 R187 | acatado | itens 1, 2 e 3 da 5.4 aplicados literalmente |
| 5.5 (1) datas do Microsoft Learn | acatado | ms.date na tabela e nos mapas: transparency note 2026-03-31; batch-transcription-create 2026-03-30; captioning-concepts 2026-02-25 (conferidas no metadado ms.date das páginas abertas hoje) |
| 5.5 (2) observação do NeMo | acatado | incluída na tabela de proveniência |

### Conferências da parte (seção 6)

| nº | ponto | resposta |
|---|---|---|
| 6.1 a 6.3 | estrutura, normativo, gabarito na v1 | acatado, sem mudança de fato |
| 6.4 | reposições: 1.4 duas, ambas C e não VOLÁTEIS; 1.5 uma, não D, sem NeMo, até 1 VOLÁTIL; 1.6 duas, ao menos 1 C, até 1 VOLÁTIL | acatado: 1.4 R162 e R169, C, não VOLÁTEIS, formato SH; 1.5 R177, E, formato SH, 1 VOLÁTIL baixo, sem NeMo; 1.6 R186 (E, formato D, não VOLÁTIL) e R191 (C, formato AP, 1 VOLÁTIL baixo) |
| 6.5 | teto de 9/30 por formato | acatado: 1.4 máximo 8 (SH); 1.5 máximo 8 (D); 1.6 máximo 8 (D e SH) |
| 6.6 | VOLÁTIL por folha | acatado: 1.4 6/30; 1.5 6/30; 1.6 6/30 (cada uma em 20,0%, no teto) |

FIM DA RESPOSTA AO QA

---

Reforço onda 1 da ordem F (T-113; D-REFORCO-2; D-V15-F-AJUSTE; D1 da GCE V15_BAEF, seção 4), parte B, Lote 1, P2 itens 1.4, 1.5 e 1.6, versão 2 (rodada de correção R1). Trinta itens AUTORAL novos: L1-R162 a L1-R171 (P2-1.4), L1-R172 a L1-R181 (P2-1.5) e L1-R182 a L1-R191 (P2-1.6). Nenhum item existente foi alterado. Rótulo AUTORAL em todos, aderência DIRETA em todos, QA PENDENTE em todos (D-QA-PENDENTE). Partida: pacote v1.11 (cada folha com 20 itens, todos diretos), mais a onda 4 (que não toca as folhas 1.4 a 1.6) e as demais partes da onda 1. Mudanças da v2 em relação à v1: 4 itens corrigidos (R173, R174, R181, R187) e 5 substitutos com os mesmos ids (R162, R169, R177, R186, R191); os outros 21 itens são idênticos aos da v1.

**Contagens da parte.** Gabarito: 13 C / 17 E (43,3% de C; faixa da parte, 12 a 18 C; faixa da regra 5 da D-REFORCO-2, 40% a 60%). Por folha: 1.4 com 4 C, 1.5 com 5 C, 1.6 com 4 C (faixa de 4 a 6). [TS]: 16 de 30. VOLÁTIL novo: 11.

| folha | itens novos | C | E | [TS] | VOLÁTIL novos (teto) | VOLÁTEIS existentes | VOLÁTIL na folha final | aderência |
|---|--:|--:|--:|--:|--|--:|--|---|
| P2-1.4 | 10 | 4 | 6 | 5 | 3 (3) | 3 | 6 de 30 (20,0%) | 10 diretos de 10 |
| P2-1.5 | 10 | 5 | 5 | 5 | 3 (3) | 3 | 6 de 30 (20,0%) | 10 diretos de 10 |
| P2-1.6 | 10 | 4 | 6 | 6 | 5 (5) | 1 | 6 de 30 (20,0%) | 10 diretos de 10 |

**VOLÁTIL novos por folha.** 1.4: R168, R170, R171. 1.5: R177, R178, R180. 1.6: R183, R184, R185, R187, R191.

**Leituras.** CLAUDE.md; ordens/ORDEM_V15_F_BANCO40.md; regras/proveniencia.md; regras/estilo_banca.md; edital/modulo_RF_IA_P2.md (1.4 "Diarização de falantes: identificação e separação de múltiplos oradores"; 1.5 "Pontuação automática e capitalização em transcrições"; 1.6 "Desafios do ASR em Português Brasileiro: sotaques, vocabulário técnico e parlamentar"); D-REFORCO-2 (regras 1 a 6), D-FONTE-DATA-ANTERIOR, D-ADERENCIA; o parecer saida/gce/QA_T113_B_R1_2026-10-18_gce-cqfp.md (inteiro); a v1 desta parte; saida/pacote/pacote.json v1.11 (560 itens, em especial os 20 de cada uma das três folhas); todos os saida/gce/*.md e saida/gcb/*.md que não são pareceres de QA (inclusive a onda 4 e as partes A, C e D da T-113).

**Bases.** Todas as páginas e arquivos abaixo foram abertos em 18/10/2026 (HTTP 200) e baixados com curl; cada trecho literal citado nas justificativas dos 7 itens com texto novo nesta rodada (5 substitutos, R174 e R181) foi conferido por script próprio (python -I, HTML sem tags, espaços normalizados) contra o texto baixado nesse dia. Os trechos dos demais itens são os da v1, já conferidos pela produção e pela QA (45 de 45 CONFEREM no relatório do QA). Nenhuma data de verificação anterior foi usada (D-FONTE-DATA-ANTERIOR não é invocada). Nenhum item cita dispositivo legal nem norma da Câmara: a parte não vai ao qa-normativo. As páginas do Google trazem a data "Last updated"; as do Microsoft Learn trazem o metadado ms.date (2026-03-31, 2026-03-30 e 2026-02-25, conforme a tabela); as da AWS, o guia da OpenAI, a documentação do pyannote.metrics e os arquivos do repositório não exibem data de atualização. O código e o cartão do modelo do Whisper estão fixados na etiqueta v20250625.

**Verificação de não repetição dos 5 substitutos.** Busca por conceito e sinônimos (grep por termos em português e em inglês) nos 560 itens do pacote.json v1.11 (enunciado e justificativa) e em todos os saida/gce/*.md e saida/gcb/*.md que não são pareceres de QA, inclusive a onda 4 e as partes A, C e D da T-113. Termos buscados: fala sobreposta, sobreposição, overlapping speech, skip_overlap, detecção perdida; mesmo ambiente, ambiente acústico, microfone comum; prompt com pontuação, capitalização e preservar; robustez, robustness, linguagem técnica, technical language; conjunto de caracteres, character set, acentuadas, cedilha. Resultado: nenhum item existente nem rascunho julga os mesmos pontos. Proximidades registradas, com o ponto distinto:
- L1-R162 (a DER leva em conta a fala sobreposta e a ausência de módulo de detecção pode elevar a detecção perdida) × L1-R64 (sobreposição de intervalos entre canais), × L1-R91 (queda de acurácia do ASR nos apartes) e × L1-R164 e L1-R165 (denominador e mapeamento da DER): outro ponto da mesma métrica, sem repetir o juízo.
- L1-R169 (desempenho do Azure Speech melhor com todos os falantes no mesmo ambiente acústico) × L1-R90 (microfone afastado ou próximo demais) e × L1-R168 (diarização em canal único): R90 trata da distância ao microfone; R168, do número de canais; R169, do ambiente comum dos falantes.
- L1-R177 (o prompt da API da OpenAI e a preservação de pontuação e capitalização) × L1-R100 (prompt inicial do Whisper de código aberto para grafar nomes e termos) e × L1-Q11 (pontuação falada × automática): R100 trata do vocabulário; Q11, de dois recursos conceituais; R177, de um uso do parâmetro prompt.
- L1-R186 (robustez melhorada a sotaques, ruído e linguagem técnica, segundo o cartão do Whisper) × L1-R98 (desempenho desigual entre sotaques) e × L1-R36 e L1-R37 (cartão do modelo): R98 julga a uniformidade entre sotaques; R186 julga o alcance da robustez comparada a outros sistemas, e o item do substituto reconhece a desigualdade entre sotaques apenas na justificativa.
- L1-R191 (conjunto de caracteres do português no campo Phrase) × L2-R80 (algarismos na coluna Phrase) × L2-R87 (símbolos na coluna DisplayAs) × L1-R101 (hifens em termos de várias palavras): cada um julga um caractere ou uma coluna distinta; R191 julga as letras acentuadas e o cedilha do português.

Legenda dos formatos: D = definição; TSj = troca de sujeito; SH = situação hipotética; NP = número ou prazo; PC = par confundível; AP = aplicação parlamentar. Critério de classificação: o da T91_reconciliacao, seção 3.1 (o formato segue a construção do ponto, e não o gabarito; o formato de um item C é o da sua contraparte E). Legenda do [TS]: troca sutil de um único conceito; em item C, a convenção "espelho" (a versão verdadeira de uma troca sutil, com o contraste à vista), declarada na justificativa. Os 20 itens existentes de cada folha foram classificados pelo mesmo critério (ver a v1).

**Tabela formato × existentes × novos × total (teto de 9 por formato na folha de 30), recalculada depois das correções 5.1 e das cinco substituições.**

P2-1.4

| formato | existentes | novos | total | % da folha |
|---|--:|--:|--:|--:|
| D | 4 | 0 | 4 | 13,3% |
| TSj | 4 | 2 | 6 | 20,0% |
| SH | 4 | 4 | 8 | 26,7% |
| NP | 2 | 2 | 4 | 13,3% |
| PC | 2 | 1 | 3 | 10,0% |
| AP | 4 | 1 | 5 | 16,7% |
| total | 20 | 10 | 30 | 100% |

P2-1.5

| formato | existentes | novos | total | % da folha |
|---|--:|--:|--:|--:|
| D | 3 | 5 | 8 | 26,7% |
| TSj | 5 | 0 | 5 | 16,7% |
| SH | 4 | 3 | 7 | 23,3% |
| NP | 2 | 0 | 2 | 6,7% |
| PC | 2 | 2 | 4 | 13,3% |
| AP | 4 | 0 | 4 | 13,3% |
| total | 20 | 10 | 30 | 100% |

P2-1.6

| formato | existentes | novos | total | % da folha |
|---|--:|--:|--:|--:|
| D | 6 | 2 | 8 | 26,7% |
| TSj | 5 | 2 | 7 | 23,3% |
| SH | 4 | 4 | 8 | 26,7% |
| NP | 0 | 0 | 0 | 0,0% |
| PC | 1 | 1 | 2 | 6,7% |
| AP | 4 | 1 | 5 | 16,7% |
| total | 20 | 10 | 30 | 100% |

Legado registrado: nenhuma folha passa de 8 itens de um mesmo formato (26,7%); o teto de 30% (9 de 30) é cumprido nas três, também depois de 5.1.

=====================================================================
PARTE 1/3 — MAPA
=====================================================================

| id | folha | ponto de julgamento | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL | aderência |
|---|---|---|---|---|---|---|
| L1-R162 | P2-1.4 | Na DER em sua configuração padrão (skip_overlap em False), a fala sobreposta entra na avaliação; sem módulo de detecção de fala sobreposta, o sistema pode acumular mais detecção perdida | SH | pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) (https://pyannote.github.io/pyannote-metrics/reference.html; verificado em 18/10/2026) | n | direta |
| L1-R163 | P2-1.4 | Motivo da remoção de um colar em torno das fronteiras de turno na avaliação: a imprecisão das anotações manuais, e não a dos sistemas | TSj | pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) (https://pyannote.github.io/pyannote-metrics/reference.html; verificado em 18/10/2026) | n | direta |
| L1-R164 | P2-1.4 | Denominador da DER: soma, sobre todos os falantes, da duração da fala de referência, e não a duração do arquivo | NP | pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) (https://pyannote.github.io/pyannote-metrics/reference.html; verificado em 18/10/2026) | n | direta |
| L1-R165 | P2-1.4 | Os nomes dos rótulos do sistema não precisam coincidir com os da referência: a DER usa mapeamento um a um entre falantes, na versão ótima pelo algoritmo húngaro | SH | pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) (https://pyannote.github.io/pyannote-metrics/reference.html; verificado em 18/10/2026) | n | direta |
| L1-R166 | P2-1.4 | Segmentação excessiva dá alta pureza e baixa cobertura; subsegmentação (dois falantes fundidos) dá baixa pureza e cobertura maior | PC | pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) (https://pyannote.github.io/pyannote-metrics/reference.html; verificado em 18/10/2026) | n | direta |
| L1-R167 | P2-1.4 | Métrica de qualidade da diarização no Azure Speech: WDER (taxa de erro de diarização por palavra), e não o WER | TSj | Microsoft Learn, Azure Speech, "Transparency note: speech to text" (ms.date 2026-03-31) (https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note; verificado em 18/10/2026) | n | direta |
| L1-R168 | P2-1.4 | Na transcrição em lote do Azure Speech, a diarização espera gravação em canal único (mono) e não está disponível em gravações estéreo | SH | Microsoft Learn, Azure Speech, "Create a batch transcription" (ms.date 2026-03-30) (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription-create; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R169 | P2-1.4 | Na transcrição de conversa gravada com identificação de falantes, o Azure Speech tende a ter melhor desempenho quando todos os falantes estão no mesmo ambiente acústico (sala, microfone comum) | SH | Microsoft Learn, Azure Speech, "Transparency note: speech to text" (ms.date 2026-03-31) (https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note; verificado em 18/10/2026) | n | direta |
| L1-R170 | P2-1.4 | A identificação de canais do Amazon Transcribe não admite áudio com mais de dois canais | NP | AWS, Amazon Transcribe Developer Guide, "Transcribing multi-channel audio" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R171 | P2-1.4 | Modelo de diarização que aceita trechos de áudio de referência de falantes conhecidos, com nomes, para associar os segmentos a esses falantes | AP | OpenAI, Speech to text (guia da API), seção "Speaker diarization" (sem data de atualização na página) (https://developers.openai.com/api/docs/guides/speech-to-text; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R172 | P2-1.5 | Para cada palavra, o modelo de pontuação e capitalização prevê a marca que se segue à palavra e se ela deve ser capitalizada | D | NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst; verificado em 18/10/2026) | n | direta |
| L1-R173 | P2-1.5 | Por padrão, o modelo considera só vírgulas, pontos e interrogações; outros sinais exigem novos rótulos | D | NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst; verificado em 18/10/2026) | n | direta |
| L1-R174 | P2-1.5 | Na inferência por segmentos, as previsões junto às bordas, onde o desempenho é pior, são descartadas (margin), e não privilegiadas | SH | NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst; verificado em 18/10/2026) | n | direta |
| L1-R175 | P2-1.5 | O modelo é composto de dois classificadores de token treinados em conjunto sobre um modelo de linguagem pré-treinado e opera sobre texto | D | NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst; verificado em 18/10/2026) | n | direta |
| L1-R176 | P2-1.5 | A avaliação do modelo gera dois relatórios de classificação (capitalização e pontuação) com precisão, revocação e F1, e não um relatório de WER | PC | NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst; verificado em 18/10/2026) | n | direta |
| L1-R177 | P2-1.5 | O prompt da API de transcrição da OpenAI serve também para preservar pontuação e capitalização, e não só vocabulário | SH | OpenAI, Speech to text (guia da API), seção "Prompting" (sem data de atualização na página) (https://developers.openai.com/api/docs/guides/speech-to-text; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R178 | P2-1.5 | Por padrão o Google Speech-to-Text não inclui pontuação nos resultados; a pontuação automática precisa ser solicitada | D | Google Cloud, "Enable automatic punctuation" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/automatic-punctuation; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R179 | P2-1.5 | Para treinar o modelo de pontuação e capitalização, recomenda-se balancear os dados, sobretudo para a tarefa de pontuação | D | NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst; verificado em 18/10/2026) | n | direta |
| L1-R180 | P2-1.5 | Na legenda ao vivo com o Azure Speech, a pontuação dos resultados parciais não está disponível | SH | Microsoft Learn, Azure Speech, "Captioning with speech to text" (ms.date 2026-02-25) (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/captioning-concepts; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R181 | P2-1.5 | O normalizador básico de texto do Whisper converte para minúsculas e troca símbolos e pontuação por espaço, de modo que o texto normalizado não distingue pontuação nem caixa | PC | OpenAI, repositório oficial openai/whisper, whisper/normalizers/basic.py (etiqueta v20250625) (https://raw.githubusercontent.com/openai/whisper/v20250625/whisper/normalizers/basic.py; verificado em 18/10/2026) | n | direta |
| L1-R182 | P2-1.6 | O Whisper detecta o idioma uma vez, com base em até os primeiros 30 s, quando o idioma não é informado | SH | OpenAI, repositório oficial openai/whisper, whisper/transcribe.py (etiqueta v20250625) (https://raw.githubusercontent.com/openai/whisper/v20250625/whisper/transcribe.py; verificado em 18/10/2026) | n | direta |
| L1-R183 | P2-1.6 | Na tabela de vocabulário personalizado do Amazon Transcribe, SoundsLike e IPA não são mais suportados | TSj | AWS, Amazon Transcribe Developer Guide, "Creating custom vocabulary tables" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-table.html; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R184 | P2-1.6 | Com modelo de linguagem personalizado ativo na mesma requisição, o DisplayAs do vocabulário personalizado não é aplicado | SH | AWS, Amazon Transcribe Developer Guide, "Improving transcription accuracy with custom vocabularies and custom language models" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/improving-accuracy.html; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R185 | P2-1.6 | Ao incluir um modelo de linguagem personalizado na requisição, não se pode habilitar a identificação de idioma | SH | AWS, Amazon Transcribe Developer Guide, "Custom language models" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R186 | P2-1.6 | Segundo o cartão do modelo Whisper, a robustez melhorada em relação a muitos sistemas existentes alcança sotaques, ruído de fundo e linguagem técnica | D | OpenAI, repositório oficial openai/whisper, model-card.md (etiqueta v20250625) (https://raw.githubusercontent.com/openai/whisper/v20250625/model-card.md; verificado em 18/10/2026) | n | direta |
| L1-R187 | P2-1.6 | Por padrão, a adaptação de modelo do Google tem efeito relativamente pequeno, sobretudo em frases de uma palavra | TSj | Google Cloud, "Improve transcription results with model adaptation" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/adaptation-model; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L1-R188 | P2-1.6 | Os modelos de fala são treinados com dados que incluem diversos estilos de fala, sotaques, dialetos e entonações e variações acústicas de dispositivos de gravação | D | Microsoft Learn, Azure Speech, "Transparency note: speech to text" (ms.date 2026-03-31) (https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note; verificado em 18/10/2026) | n | direta |
| L1-R189 | P2-1.6 | A lista de idiomas do Whisper de código aberto traz um único código para o português (pt), sem variante brasileira | PC | OpenAI, repositório oficial openai/whisper, whisper/tokenizer.py (etiqueta v20250625) (https://raw.githubusercontent.com/openai/whisper/v20250625/whisper/tokenizer.py; verificado em 18/10/2026) | n | direta |
| L1-R190 | P2-1.6 | Sem boost, as palavras da frase de adaptação são reconhecidas com igual probabilidade | SH | Google Cloud, "Improve transcription results with model adaptation" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/adaptation-model; verificado em 18/10/2026) | n | direta |
| L1-R191 | P2-1.6 | O conjunto de caracteres do português no vocabulário personalizado do Amazon Transcribe admite letras acentuadas e o cedilha no campo Phrase | AP | AWS, Amazon Transcribe Developer Guide, "Custom vocabularies" e "Character sets for custom vocabularies and vocabulary filters" (as páginas não exibem data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html; https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html; verificado em 18/10/2026) | VOLÁTIL baixo | direta |

=====================================================================
PARTE 2/3 — (d) ITENS DO ESTUDANTE
=====================================================================

Julgue o item.

**L1-R162** (P2-1.4)
Uma equipe avalia, com a taxa de erro de diarização (DER) do pyannote.metrics em sua configuração padrão, um sistema de diarização que não inclui módulo de detecção de fala sobreposta, usando gravações de comissão com muitos apartes. Nessa situação, segundo a documentação, a métrica leva em conta a fala sobreposta, o que pode aumentar a detecção perdida atribuída ao sistema.

**L1-R163** (P2-1.4)
Na avaliação de sistemas de diarização, é comum remover da avaliação uma faixa (colar) em torno de cada fronteira de turno de fala, porque os sistemas automáticos não conseguem determinar essas fronteiras com precisão no nível da amostra de áudio.

**L1-R164** (P2-1.4)
Considere um arquivo de 100 s em que a fala de referência soma 80 s. Um sistema de diarização apresentou 4 s de falso alarme, 2 s de fala perdida e 6 s de confusão de falantes. Nessa situação, segundo a definição de DER da documentação do pyannote.metrics, a DER é de 12%, resultado de 12 s de erro divididos pelos 100 s de duração do arquivo.

**L1-R165** (P2-1.4)
Na avaliação de um sistema de diarização, o sistema rotulou como spk_0 o orador que a anotação de referência chama de Presidente. Nessa situação, a diferença entre os nomes dos rótulos não constitui, por si só, erro de confusão, pois a DER se apoia em um mapeamento um a um entre os falantes da referência e os do sistema, que, na versão ótima, é calculado pelo algoritmo húngaro de modo a minimizar a confusão.

**L1-R166** (P2-1.4)
Segundo a documentação do pyannote.metrics, resultados com segmentação excessiva (muitos agrupamentos de falantes) tendem a produzir alta cobertura e baixa pureza, ao passo que resultados com subsegmentação (dois falantes fundidos em um grande agrupamento) levam a alta pureza e cobertura menor.

**L1-R167** (P2-1.4)
Segundo a nota de transparência do Azure Speech, a qualidade da diarização é medida pela taxa de erro de palavras (WER), de modo que o serviço não adota métrica específica para a atribuição das palavras aos falantes.

**L1-R168** (P2-1.4)
Uma equipe envia à transcrição em lote do Azure Speech, com a diarização habilitada, um arquivo estéreo que traz dois oradores. Nessa situação, segundo a documentação, a diarização é aplicada normalmente, pois o recurso foi concebido para gravações com mais de um canal.

**L1-R169** (P2-1.4)
Uma comissão grava a reunião em um único arquivo, com todos os parlamentares falando para um microfone comum na mesma sala, e envia a gravação ao Azure Speech para obter a transcrição com a indicação de quem falou. Nessa situação, segundo a nota de transparência, estar todos os falantes no mesmo ambiente acústico, como o de uma sala em que falam para um microfone comum, é a condição em que o sistema tende a ter melhor desempenho.

**L1-R170** (P2-1.4)
O sistema de som de um comitê grava o áudio, com um microfone por canal, em um arquivo de quatro canais. Nessa situação, segundo a documentação do Amazon Transcribe, a identificação de canais pode ser usada para transcrever separadamente cada um dos quatro canais.

**L1-R171** (P2-1.4)
Para que a transcrição de uma audiência exiba o nome do presidente da sessão, a API de transcrição da OpenAI, no modelo especializado em diarização, aceita o envio de trechos curtos de áudio de referência de falantes conhecidos, acompanhados dos respectivos nomes, para associar os segmentos de fala a esses falantes.

**L1-R172** (P2-1.5)
No modelo de pontuação e capitalização documentado pelo NeMo, para cada palavra do texto de entrada o modelo prevê a marca de pontuação que deve preceder a palavra e se ela deve ser grafada com inicial maiúscula.

**L1-R173** (P2-1.5)
Segundo a documentação do NeMo, por padrão o modelo de pontuação e capitalização considera vírgulas, pontos finais e pontos de interrogação, tendo os demais sinais sido removidos dos dados; para que sinais como o ponto e vírgula e os dois-pontos fossem restaurados em transcrições, seria preciso introduzir novos rótulos.

**L1-R174** (P2-1.5)
Uma equipe usa o script de inferência de pontuação e capitalização do NeMo em um texto de transcrição muito longo, que é dividido em segmentos. Nessa situação, segundo a documentação, como o desempenho do modelo é pior junto às bordas dos segmentos, as previsões feitas para os tokens próximos dessas bordas são privilegiadas no cálculo das previsões finais.

**L1-R175** (P2-1.5)
O modelo de pontuação e capitalização do NeMo é composto de dois classificadores no nível de token, um para a pontuação e outro para a capitalização, treinados em conjunto sobre um modelo de linguagem pré-treinado, e opera sobre texto, e não sobre o sinal de áudio.

**L1-R176** (P2-1.5)
A avaliação do modelo de pontuação e capitalização do NeMo gera um único relatório de taxa de erro de palavras (WER), que cobre ao mesmo tempo a pontuação e a capitalização.

**L1-R177** (P2-1.5)
Uma equipe percebe que a transcrição de audiências, feita com um modelo de transcrição da API da OpenAI que aceita prompt, vem sem a pontuação e as iniciais maiúsculas adotadas na Casa. Nessa situação, segundo o guia da API, o prompt não é recurso adequado para isso, pois serve apenas para melhorar o reconhecimento de nomes, siglas e vocabulário específico da gravação, e não para preservar pontuação nem capitalização.

**L1-R178** (P2-1.5)
Segundo a documentação do Google Cloud Speech-to-Text, por padrão o serviço já insere pontuação nos resultados do reconhecimento, de modo que a pontuação automática precisa ser desabilitada quando não for desejada.

**L1-R179** (P2-1.5)
Segundo a documentação do NeMo, no treinamento do modelo de pontuação e capitalização recomenda-se balancear os dados, especialmente para a tarefa de pontuação.

**L1-R180** (P2-1.5)
Em legenda ao vivo de uma sessão produzida com o Azure Speech, a equipe percebe que os resultados parciais (evento Recognizing) chegam sem pontuação. Segundo a documentação do serviço, isso é esperado, pois a pontuação dos resultados parciais não está disponível.

**L1-R181** (P2-1.5)
O normalizador de texto básico do repositório oficial do Whisper, usado para uniformizar textos antes de compará-los, converte o texto em minúsculas e substitui por espaço símbolos e sinais de pontuação; por isso, depois dessa normalização, os trechos "Senhor Presidente, a sessão" e "senhor presidente a sessão" tornam-se idênticos, e a comparação não registra a diferença de vírgula nem de maiúsculas entre eles.

**L1-R182** (P2-1.6)
Uma sessão do Plenário começa em português e, em certo momento, um convidado passa a falar em espanhol. Se o idioma não for informado ao Whisper de código aberto, segundo o código de referência, o modelo detecta o idioma a cada janela de 30 segundos, o que faz o trecho em espanhol ser transcrito como espanhol.

**L1-R183** (P2-1.6)
Para melhorar o reconhecimento de siglas da Casa, a equipe pode preencher, na tabela de vocabulário personalizado do Amazon Transcribe, as colunas SoundsLike e IPA, que o serviço usa para orientar a pronúncia dos termos.

**L1-R184** (P2-1.6)
Uma equipe do Amazon Transcribe envia, na mesma requisição, um modelo de linguagem personalizado e um vocabulário personalizado com formas de exibição (DisplayAs) para siglas da Casa. Nessa situação, segundo a documentação, as formas de exibição do vocabulário não são aplicadas à saída enquanto o modelo de linguagem personalizado estiver ativo.

**L1-R185** (P2-1.6)
Uma equipe pretende usar, na transcrição de audiências, um modelo de linguagem personalizado do Amazon Transcribe e, ao mesmo tempo, a identificação automática de idioma. Nessa situação, segundo a documentação, ao se incluir um modelo de linguagem personalizado na requisição não é possível habilitar a identificação de idioma, sendo preciso especificar o código do idioma.

**L1-R186** (P2-1.6)
Segundo o cartão do modelo Whisper, os estudos indicam que, em comparação com muitos sistemas de ASR existentes, os modelos exibem robustez melhorada a sotaques e a ruído de fundo, mas essa melhora não alcança a linguagem técnica.

**L1-R187** (P2-1.6)
Segundo a documentação do Google Cloud Speech-to-Text, a adaptação de modelo tem, por padrão, efeito forte sobre o reconhecimento, sobretudo para frases de uma só palavra.

**L1-R188** (P2-1.6)
Segundo a nota de transparência do Azure Speech, os modelos de fala são treinados com dados de voz que incluem diversos estilos de fala, idiomas, sotaques, dialetos e entonações, além de variações acústicas geradas por diferentes tipos de dispositivos de gravação.

**L1-R189** (P2-1.6)
A lista de idiomas do Whisper de código aberto traz códigos de idioma distintos para o português do Brasil e para o português de Portugal, o que permite informar ao modelo a variante regional da fala a ser transcrita.

**L1-R190** (P2-1.6)
Uma equipe do Google Cloud Speech-to-Text inclui sessão e seção em um conjunto de frases de adaptação, sem atribuir valores de boost. Nessa situação, segundo a documentação, o modelo passa a reconhecer sessão com probabilidade maior que seção.

**L1-R191** (P2-1.6)
Ao cadastrar, no vocabulário personalizado do Amazon Transcribe para o português, termos da Casa como Constituição e proposições, a equipe verifica que, segundo a documentação, só podem ser usados os caracteres do conjunto do idioma e que o conjunto do português para o campo Phrase inclui, além das letras de A a Z, o apóstrofo, o hífen e o ponto, letras acentuadas e o cedilha.

=====================================================================
PARTE 3/3 — (d-G) GABARITO COMENTADO
=====================================================================

**L1-R162** (P2-1.4) Gabarito: C.
Justificativa: A documentação da DER registra: "this metric does take overlapping speech into account, potentially leading to increased missed detection in case the speaker diarization system does not include an overlapping speech detection module"; a opção skip_overlap vem em False por padrão ("keep overlap regions"). O item aplica a regra a gravações com apartes (C espelho).
Base: pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) (https://pyannote.github.io/pyannote-metrics/reference.html), seção/ponto: seção "Diarization" e parâmetro skip_overlap; verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R163** (P2-1.4) Gabarito: E. [TS]
Justificativa: Segundo a documentação, "Because manual annotations cannot be precise at the audio sample level", é comum remover da avaliação um colar em torno de cada fronteira de turno de fala. O item troca a causa (anotações manuais, que servem de referência) pela imprecisão dos sistemas automáticos.
Base: pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) (https://pyannote.github.io/pyannote-metrics/reference.html), seção/ponto: seção sobre colar (collar); verificado em 18/10/2026. Não VOLÁTIL. Formato: TSj.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R164** (P2-1.4) Gabarito: E. [TS]
Justificativa: Na definição da documentação, a DER é a soma de falso alarme, detecção perdida e confusão dividida por "total", que é "the sum over all speakers of their reference speech duration"; logo, 12 s divididos por 80 s resultam em 15%. O item troca o denominador (fala de referência) pela duração do arquivo, o que daria 12%.
Base: pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) (https://pyannote.github.io/pyannote-metrics/reference.html), seção/ponto: seção "Diarization error rate"; verificado em 18/10/2026. Não VOLÁTIL. Formato: NP.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R165** (P2-1.4) Gabarito: C.
Justificativa: A documentação informa que a DER depende de um "one-to-one mapping between reference and hypothesized speakers" e que a versão ótima "uses the Hungarian algorithm to compute the mapping that minimize the confusion term". O item aplica a regra ao caso de rótulos com nomes diferentes (C espelho).
Base: pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) (https://pyannote.github.io/pyannote-metrics/reference.html), seção/ponto: seção "Optimal vs. greedy"; verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R166** (P2-1.4) Gabarito: E. [TS]
Justificativa: Segundo a documentação, a segmentação excessiva tende a "high purity and low coverage", e a subsegmentação, a "low purity and higher coverage". O item inverte, nos dois casos, o efeito sobre a pureza e a cobertura.
Base: pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) (https://pyannote.github.io/pyannote-metrics/reference.html), seção/ponto: seção sobre pureza e cobertura (purity e coverage); verificado em 18/10/2026. Não VOLÁTIL. Formato: PC.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R167** (P2-1.4) Gabarito: E. [TS]
Justificativa: A nota de transparência afirma: "For diarization, we measure the quality by using word diarization error rate (WDER)", e que, quanto menor o WDER, melhor a diarização. O item troca a métrica específica (WDER) pelo WER.
Base: Microsoft Learn, Azure Speech, "Transparency note: speech to text" (ms.date 2026-03-31) (https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note), seção/ponto: seção "System performance"; verificado em 18/10/2026. Não VOLÁTIL. Formato: TSj.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R168** (P2-1.4) Gabarito: E.
Justificativa: Segundo a documentação da propriedade diarization, a entrada é "expected to be a mono channel that contains multiple voices" e "The feature isn't available with stereo recordings". O item afirma que o recurso se aplica a gravações com mais de um canal.
Base: Microsoft Learn, Azure Speech, "Create a batch transcription" (ms.date 2026-03-30) (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription-create), seção/ponto: propriedade diarization; verificado em 18/10/2026. VOLÁTIL baixo. Formato: SH.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R169** (P2-1.4) Gabarito: C.
Justificativa: A nota de transparência registra, para a transcrição de conversa em eventos gravados: "The system will perform better if all speakers are in the same acoustic environment (for example, the conversation takes place in a room in which people speak into a common microphone)". O item aplica a regra à comissão que fala para um microfone comum na mesma sala (C espelho).
Base: Microsoft Learn, Azure Speech, "Transparency note: speech to text" (ms.date 2026-03-31) (https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note), seção/ponto: "Considerations when choosing other use cases", item "Conversation transcription on prerecorded events"; verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R170** (P2-1.4) Gabarito: E. [TS]
Justificativa: A documentação informa que, com dois canais, é possível transcrever a fala de cada canal separadamente, e que o "Amazon Transcribe doesn't currently support audio with more than two channels". O item troca o limite de dois canais por quatro.
Base: AWS, Amazon Transcribe Developer Guide, "Transcribing multi-channel audio" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html), seção/ponto: abertura da página; verificado em 18/10/2026. VOLÁTIL baixo. Formato: NP.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R171** (P2-1.4) Gabarito: C.
Justificativa: A documentação informa: "You can optionally supply up to four short audio references with known_speaker_names[] and known_speaker_references[] to map segments onto known speakers". O item aplica o recurso ao caso do nome do presidente da sessão (C espelho).
Base: OpenAI, Speech to text (guia da API), seção "Speaker diarization" (sem data de atualização na página) (https://developers.openai.com/api/docs/guides/speech-to-text), seção/ponto: seção "Speaker diarization"; verificado em 18/10/2026. VOLÁTIL baixo. Formato: AP.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R172** (P2-1.5) Gabarito: E. [TS]
Justificativa: Segundo a documentação, para cada palavra o modelo "predicts a punctuation mark that should follow the word (if any)" e "predicts if the word should be capitalized or not". O item troca a marca que se segue à palavra pela que a precede.
Base: NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst), seção/ponto: seção "Model Description"; verificado em 18/10/2026. Não VOLÁTIL. Formato: D.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R173** (P2-1.5) Gabarito: C.
Justificativa: A documentação informa que "By default, the following punctuation marks are considered: commas, periods, and question marks", e que "This can be changed by introducing new labels". O item aplica a regra ao ponto e vírgula e aos dois-pontos (C espelho).
Base: NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst), seção/ponto: seção "Raw Data Format"; verificado em 18/10/2026. Não VOLÁTIL. Formato: D.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R174** (P2-1.5) Gabarito: E. [TS]
Justificativa: A documentação afirma que a divisão em segmentos leva a desempenho pior "near edges of segments" e que o parâmetro margin serve para descartar ("discard") as probabilidades previstas para os tokens "near segment edges". O item troca o descarte dessas previsões por sua preferência.
Base: NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst), seção/ponto: seção "Inference"; verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R175** (P2-1.5) Gabarito: C.
Justificativa: A documentação descreve "two token-level classifiers on top of a pre-trained" modelo de linguagem, treinados em conjunto, e informa que o modelo "can work with any text dataset". O item reúne as duas características documentadas (C espelho).
Base: NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst), seção/ponto: seção "Model Description"; verificado em 18/10/2026. Não VOLÁTIL. Formato: D.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R176** (P2-1.5) Gabarito: E. [TS]
Justificativa: Segundo a documentação, a avaliação gera "two classification reports: one for capitalization task and another one for punctuation task", com as métricas Precision, Recall e F1. O item troca os dois relatórios de classificação por um único relatório de WER.
Base: NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst), seção/ponto: seção "Model Evaluation"; verificado em 18/10/2026. Não VOLÁTIL. Formato: PC.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R177** (P2-1.5) Gabarito: E. [TS]
Justificativa: O guia da API diz que o prompt serve para melhorar o reconhecimento de "names, acronyms, formatting, or recording-specific vocabulary" e lista, entre os cenários úteis de prompt, "Preserving punctuation, capitalization, and filler words". O item restringe a finalidade ao vocabulário e exclui a pontuação e a capitalização.
Base: OpenAI, Speech to text (guia da API), seção "Prompting" (sem data de atualização na página) (https://developers.openai.com/api/docs/guides/speech-to-text), seção/ponto: seção "Prompting"; verificado em 18/10/2026. VOLÁTIL baixo. Formato: SH.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R178** (P2-1.5) Gabarito: E. [TS]
Justificativa: A documentação afirma que "By default, Speech-to-Text does not include punctuation marks in the results from speech recognition", sendo necessário solicitar a inserção automática. O item troca o padrão (sem pontuação) pelo oposto.
Base: Google Cloud, "Enable automatic punctuation" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/automatic-punctuation), seção/ponto: abertura da página; verificado em 18/10/2026. VOLÁTIL baixo. Formato: D.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R179** (P2-1.5) Gabarito: C.
Justificativa: A documentação informa que o modelo "can work with any text dataset, although it is recommended to balance the data, especially for the punctuation task". O item reproduz a recomendação documentada (C espelho).
Base: NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial) (https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst), seção/ponto: seção "Raw Data Format"; verificado em 18/10/2026. Não VOLÁTIL. Formato: D.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R180** (P2-1.5) Gabarito: C.
Justificativa: A documentação sobre legendas registra a nota: "Punctuation of partial results isn't available." O item aplica a nota ao caso da legenda ao vivo (C espelho).
Base: Microsoft Learn, Azure Speech, "Captioning with speech to text" (ms.date 2026-02-25) (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/captioning-concepts), seção/ponto: seção "Get partial results"; verificado em 18/10/2026. VOLÁTIL baixo. Formato: SH.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R181** (P2-1.5) Gabarito: C.
Justificativa: No código do normalizador, "s = s.lower()", a função de limpeza "Replace any other markers, symbols, punctuations with a space" e, em seguida, os espaços sucessivos são reduzidos a um só; a vírgula vira espaço e as maiúsculas viram minúsculas, de modo que os dois trechos coincidem. O item aplica o código ao exemplo (C espelho).
Base: OpenAI, repositório oficial openai/whisper, whisper/normalizers/basic.py (etiqueta v20250625) (https://raw.githubusercontent.com/openai/whisper/v20250625/whisper/normalizers/basic.py), seção/ponto: classe BasicTextNormalizer; verificado em 18/10/2026. Não VOLÁTIL. Formato: PC.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R182** (P2-1.6) Gabarito: E. [TS]
Justificativa: O código de referência registra: "Detecting language using up to the first 30 seconds. Use `--language` to specify the language". O item troca a detecção única, com base nos primeiros 30 segundos, pela detecção a cada janela.
Base: OpenAI, repositório oficial openai/whisper, whisper/transcribe.py (etiqueta v20250625) (https://raw.githubusercontent.com/openai/whisper/v20250625/whisper/transcribe.py), seção/ponto: função transcribe(); verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R183** (P2-1.6) Gabarito: E. [TS]
Justificativa: A documentação informa: "SoundsLike is no longer supported for Custom Vocabulary" e "IPA is no longer supported for Custom Vocabulary", devendo as colunas ficar vazias. O item afirma que o serviço usa as duas colunas, o que a documentação nega.
Base: AWS, Amazon Transcribe Developer Guide, "Creating custom vocabulary tables" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-table.html), seção/ponto: seção sobre as colunas da tabela; verificado em 18/10/2026. VOLÁTIL baixo. Formato: TSj.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R184** (P2-1.6) Gabarito: C.
Justificativa: A documentação alerta: "Custom vocabulary features (such as the DisplayAs field) are not applied to transcription output when a custom language model is active in the same request". O item aplica o alerta ao caso das siglas da Casa (C espelho).
Base: AWS, Amazon Transcribe Developer Guide, "Improving transcription accuracy with custom vocabularies and custom language models" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/improving-accuracy.html), seção/ponto: nota "Important"; verificado em 18/10/2026. VOLÁTIL baixo. Formato: SH.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R185** (P2-1.6) Gabarito: C.
Justificativa: A documentação alerta: "if you include a custom language model in your request, you can't enable language identification (you must specify a language code)". O item aplica o alerta ao caso de uso simultâneo dos dois recursos (C espelho).
Base: AWS, Amazon Transcribe Developer Guide, "Custom language models" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html), seção/ponto: abertura da página; verificado em 18/10/2026. VOLÁTIL baixo. Formato: SH.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R186** (P2-1.6) Gabarito: E. [TS]
Justificativa: O cartão do modelo afirma que, "over many existing ASR systems, the models exhibit improved robustness to accents, background noise, and technical language". O item retira a linguagem técnica do alcance dessa melhora (troca única do alcance); não equivale a desempenho uniforme entre sotaques, que o próprio cartão nega.
Base: OpenAI, repositório oficial openai/whisper, model-card.md (etiqueta v20250625) (https://raw.githubusercontent.com/openai/whisper/v20250625/model-card.md), seção/ponto: seção "Performance and Limitations"; verificado em 18/10/2026. Não VOLÁTIL. Formato: D.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R187** (P2-1.6) Gabarito: E. [TS]
Justificativa: A documentação afirma: "By default model adaptation provides a relatively small effect, especially for one-word phrases". O item troca o efeito relativamente pequeno por efeito forte.
Base: Google Cloud, "Improve transcription results with model adaptation" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/adaptation-model), seção/ponto: seção "Fine-tune transcription results using boost"; verificado em 18/10/2026. VOLÁTIL baixo. Formato: TSj.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R188** (P2-1.6) Gabarito: C.
Justificativa: A nota de transparência afirma: "Speech models are trained on voice data that includes various speech styles, languages, accents, dialects, and intonations, and on acoustic variations that are generated by using different types of recording devices". O item reproduz a descrição dos dados de treinamento (C espelho).
Base: Microsoft Learn, Azure Speech, "Transparency note: speech to text" (ms.date 2026-03-31) (https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note), seção/ponto: glossário (speech model); verificado em 18/10/2026. Não VOLÁTIL. Formato: D.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R189** (P2-1.6) Gabarito: E. [TS]
Justificativa: No arquivo de idiomas do repositório, o português consta com um único código: "pt": "portuguese". O item afirma haver códigos distintos para as variantes do Brasil e de Portugal.
Base: OpenAI, repositório oficial openai/whisper, whisper/tokenizer.py (etiqueta v20250625) (https://raw.githubusercontent.com/openai/whisper/v20250625/whisper/tokenizer.py), seção/ponto: dicionário LANGUAGES; verificado em 18/10/2026. Não VOLÁTIL. Formato: PC.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R190** (P2-1.6) Gabarito: E. [TS]
Justificativa: No exemplo de "fair" e "fare" da documentação: "Without boost values, the recognition model will recognize" as duas palavras "with equal probability". O item troca a igualdade de probabilidade por probabilidade maior para uma das palavras.
Base: Google Cloud, "Improve transcription results with model adaptation" (Last updated 2026-10-13 UTC) (https://docs.cloud.google.com/speech-to-text/docs/adaptation-model), seção/ponto: seção "Fine-tune transcription results using boost"; verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

**L1-R191** (P2-1.6) Gabarito: C.
Justificativa: A página de vocabulários personalizados diz que "only the characters listed in your language's character set can be used in a custom vocabulary", e a página dos conjuntos de caracteres lista, para o português, no campo Phrase, A–Z, apóstrofo, hífen e ponto, além de caracteres Unicode como Ç/ç, Ã/ã e Õ/õ. O item aplica a regra aos termos Constituição e proposições (C espelho).
Base: AWS, Amazon Transcribe Developer Guide, "Custom vocabularies" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html) e "Character sets for custom vocabularies and vocabulary filters" (a página não exibe data de atualização) (https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html), seção/ponto: abertura da primeira página e seção "Portuguese character set" da segunda; verificado em 18/10/2026. VOLÁTIL baixo. Formato: AP.
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir o trecho citado; VOLÁTIL baixo (dependência de recurso, limite ou padrão de produto). Inapto a simulado final até a reverificação.
Aderência: DIRETA (incide sobre o texto literal do edital da folha).

### Tabela de proveniência

| fonte | URL | data de verificação | usada em |
|---|---|---|---|
| pyannote.metrics, Reference (documentação oficial da biblioteca; sem data de atualização na página) | https://pyannote.github.io/pyannote-metrics/reference.html | 18/10/2026 | R162, R163, R164, R165, R166 |
| Microsoft Learn, Azure Speech, "Transparency note: speech to text" (ms.date 2026-03-31) | https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note | 18/10/2026 | R167, R169, R188 |
| Microsoft Learn, Azure Speech, "Create a batch transcription" (ms.date 2026-03-30) | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription-create | 18/10/2026 | R168 |
| AWS, Amazon Transcribe Developer Guide, "Transcribing multi-channel audio" (a página não exibe data de atualização) | https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html | 18/10/2026 | R170 |
| OpenAI, Speech to text (guia da API), seções "Speaker diarization" e "Prompting" (sem data de atualização na página) | https://developers.openai.com/api/docs/guides/speech-to-text | 18/10/2026 | R171, R177 |
| NVIDIA NeMo, "Punctuation and Capitalization Model" (documentação da versão r1.23.0 do repositório oficial; modelo ausente do ramo main em 18/10/2026, HTTP 404 na URL equivalente; documentação das versões 1.23 a 2.4) | https://raw.githubusercontent.com/NVIDIA/NeMo/r1.23.0/docs/source/nlp/punctuation_and_capitalization.rst | 18/10/2026 | R172, R173, R174, R175, R176, R179 |
| Google Cloud, "Enable automatic punctuation" (Last updated 2026-10-13 UTC) | https://docs.cloud.google.com/speech-to-text/docs/automatic-punctuation | 18/10/2026 | R178 |
| Microsoft Learn, Azure Speech, "Captioning with speech to text" (ms.date 2026-02-25) | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/captioning-concepts | 18/10/2026 | R180 |
| OpenAI, repositório oficial openai/whisper, whisper/normalizers/basic.py (etiqueta v20250625) | https://raw.githubusercontent.com/openai/whisper/v20250625/whisper/normalizers/basic.py | 18/10/2026 | R181 |
| OpenAI, repositório oficial openai/whisper, whisper/transcribe.py (etiqueta v20250625) | https://raw.githubusercontent.com/openai/whisper/v20250625/whisper/transcribe.py | 18/10/2026 | R182 |
| AWS, Amazon Transcribe Developer Guide, "Creating custom vocabulary tables" (a página não exibe data de atualização) | https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-table.html | 18/10/2026 | R183 |
| AWS, Amazon Transcribe Developer Guide, "Improving transcription accuracy with custom vocabularies and custom language models" (a página não exibe data de atualização) | https://docs.aws.amazon.com/transcribe/latest/dg/improving-accuracy.html | 18/10/2026 | R184 |
| AWS, Amazon Transcribe Developer Guide, "Custom language models" (a página não exibe data de atualização) | https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html | 18/10/2026 | R185 |
| OpenAI, repositório oficial openai/whisper, model-card.md (etiqueta v20250625) | https://raw.githubusercontent.com/openai/whisper/v20250625/model-card.md | 18/10/2026 | R186 |
| Google Cloud, "Improve transcription results with model adaptation" (Last updated 2026-10-13 UTC) | https://docs.cloud.google.com/speech-to-text/docs/adaptation-model | 18/10/2026 | R187, R190 |
| OpenAI, repositório oficial openai/whisper, whisper/tokenizer.py (etiqueta v20250625) | https://raw.githubusercontent.com/openai/whisper/v20250625/whisper/tokenizer.py | 18/10/2026 | R189 |
| AWS, Amazon Transcribe Developer Guide, "Custom vocabularies" (a página não exibe data de atualização) | https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html | 18/10/2026 | R191 |
| AWS, Amazon Transcribe Developer Guide, "Character sets for custom vocabularies and vocabulary filters" (a página não exibe data de atualização) | https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html | 18/10/2026 | R191 |

Observações de proveniência: (1) o texto de cada página foi baixado em 18/10/2026 (HTTP 200, exceto a URL do NeMo no ramo main, que devolve 404 e por isso o item usa a etiqueta r1.23.0) e os trechos entre aspas foram conferidos por script contra esse texto; (2) as afirmações sobre Whisper (L1-R181, R182, R186, R189), Google Speech-to-Text (L1-R178, R187, R190), Azure Speech (L1-R167, R168, R169, R180, R188), AWS Transcribe (L1-R170, R183 a R185, R191) e sobre a API da OpenAI (L1-R171, R177) têm cada uma a URL oficial e a data acima; as afirmações sobre pyannote.metrics (R162 a R166) e NVIDIA NeMo (R172 a R176, R179) vêm da documentação oficial das próprias ferramentas; (3) nenhuma versão de modelo, preço ou limite numérico foi afirmada sem a fonte datada; os limites e o escopo de recurso citados (dois canais, quatro referências de áudio, prompt, conjunto de caracteres, padrão da adaptação) estão em itens marcados VOLÁTIL baixo; (4) a documentação do NeMo é a da versão r1.23.0 do repositório oficial (URL fixada na etiqueta), de modo que os itens R172 a R176 e R179 não dependem de página mutável, mas entram na lista de conferência de base de janeiro; (5) o código e o cartão do Whisper citados estão fixados na etiqueta v20250625 do repositório oficial (aberta com HTTP 200 em 18/10/2026), e os itens R181, R182, R186 e R189 entram na conferência de base de janeiro; (6) as datas do Microsoft Learn são o metadado ms.date da página (transparency note 2026-03-31; batch-transcription-create 2026-03-30; captioning-concepts 2026-02-25); (7) nenhum item cita lei, ato ou regimento.

FIM DO LOTE
