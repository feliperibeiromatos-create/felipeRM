# L2_reforco_onda3_saldo_v2.md — T-105 — 2026-10-18 — gerado por gce-cpp

Tarefa T-105, segunda versão (D-GATE-T105, Fundador: reprovação comum da v1; v2 com ponto novo e QA normal, R2). Escopo: 1 item AUTORAL, L2-R131 (mesmo id), folha P2-2.4, em reposição ao L2-R67 (retirado; id L2-R67 não reutilizado). Rótulo: AUTORAL. QA PENDENTE: o item não passou por QA (D-QA-PENDENTE) e não entra em simulado antes da R2 da gce-cqfp. "Verificado em 18/10/2026" = página aberta e lida nesta data, nesta sessão (HTTP 200). Nenhuma norma citada.

=====================================================================
PARTE 1/3 — RESPOSTA AO PARECER, MAPA E BUSCA DE UNICIDADE
=====================================================================

## 1.0 Resposta ao parecer (QA_T105_R1_2026-10-18_gce-cqfp.md)

| ponto do parecer | resposta |
|---|---|
| Veredito: L2-R131 v1 REPROVADO, gêmeo do L1-R64 (mesmo ponto, mesma frase-base da página channel-id da AWS) | acatado. O ponto da v1 (sobreposição de carimbos por canal) foi abandonado por inteiro. A v2 não usa a página channel-id, nem a de diarização da AWS, nem a de diarização do Google ou do Azure |
| Declaração errada da v1 (busca por palavra-chave no L1 onda 2 B não achou o R64) | acatado. A v2 varre por script a frase-base literal e as palavras-chave contra 35 arquivos (seção 1.3), em vez de busca manual |
| Vizinhos L1-R69 (canais mesclados, Azure) e L1-R91 (fala simultânea como ruído) não declarados | acatado como registro; a v2 não trata de canais, mesclagem nem fala simultânea |
| Orientação: ponto novo; frase-base ≥ 45 caracteres varrida por script contra finais das ondas 1 a 3 e pacote.json v1.9 | acatado; seção 1.3 |
| Formato: o item da v1 era TS, não PC | acatado. Na v2 o formato é PC (par items × audio_segments, e fala contínua × pausa), declarado com a troca de um único termo |
| Nota: B_v2 citado onde a versão final é B_v3 | acatado; a v2 varre os finais (B_v3 etc.) e também as versões anteriores |
| Requisitos mantidos (E com [TS] de troca única, aderência direta à 2.4, formato ≠ SH e AP, não VOLÁTIL, base reaberta hoje) | mantidos; seção 1.2 |

## 1.1 Item novo

Formatos: D = definição; TS = troca de sujeito; SH = situação hipotética; NP = número ou prazo; PC = par confundível; AP = aplicação parlamentar.

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL |
|---|---|---|---|---|---|
| L2-R131 | P2-2.4 | Na saída em lote do Amazon Transcribe, o elemento audio_segments registra, com início e fim, trechos de fala contínua (pausas mínimas); a pausa fica fora do segmento, e não é ela que o segmento delimita | PC (fala contínua × pausa; items × audio_segments) | https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html (AWS, Amazon Transcribe Developer Guide, "Data input and output", seção de exemplo de saída) | n |

## 1.2 Atendimento dos requisitos da T-105

| requisito | atendimento |
|---|---|
| folha P2-2.4 | sim; edital 2.4: "identificação de oradores, marcação de pausa ruído, etc." O ponto é a marcação de pausa na estrutura da transcrição (o que o segmento de fala delimita e o que fica fora dele) |
| gabarito E com [TS] de troca única | sim; um único termo muda: o objeto do registro, "trechos de fala contínua" → "as pausas existentes entre as falas". A oração sobre o elemento items é verdadeira e neutra |
| aderência direta à 2.4 | sim (marcação de pausa na transcrição). Ressalva em "Dúvidas", item 3 |
| sem regra de condução da sessão | sim; nenhuma norma regimental |
| sem metafato de página | sim; o ponto é o conteúdo do campo da saída (o que o segmento representa), não o que a página declara cobrir |
| formato ≠ SH e AP | sim; PC |
| ponto distinto dos 19 da folha e sem gêmeo no pacote | sim (1.3 e 1.4) |
| base oficial aberta hoje, trecho literal | sim (Parte 3) |
| não VOLÁTIL | sim; o enunciado não usa limite, versão, preço, idioma nem parâmetro de requisição |

## 1.3 Busca de unicidade por script (python -I)

Arquivos varridos: 35 = pacote.json e pacote_estudante.json (v1.9); L1_reforco_onda1_v1/v2; L2_reforco_onda1_v1/v2/v3; L3_reforco_onda1_v1/v2/v3; L1_reforco_onda2_A/B/C/D (v1 a v3 onde existem) e saldo_v1/v2; L2_reforco_onda3_A/B/C/D (v1 a v3) e saldo_v1 (inclui todos os finais indicados).

Frase-base (45 caracteres ou mais) buscada, sem diferenciar maiúsculas: "uninterrupted spoken language, with minimal pauses or breaks". Palavras-chave do ponto buscadas: "minimal pauses"; "audio_segments"; "audio segment"; "pausas mínimas"; "fala ininterrupta"; "fala contínua"; "segmento de áudio"; "segmentos de áudio"; "trecho de fala"; "natural flow of speech"; "interrupted spoken"; "uninterrupted".
Resultado: 0 acertos em todos os 35 arquivos, para todas as chaves. (Nota de método: as 13 chaves foram buscadas por varredura de subcadeia no texto inteiro de cada arquivo.)

Varreduras anteriores que levaram ao descarte de pontos, mesma data: página channel-id e diarization da AWS (L1-R64, L1-R74); Google "Detect different speakers" ("labels by number", "running aggregate": L1-R66, L2-R70); Azure quickstart de diarização em tempo real ("Unknown", "Guest-1", DiarizeIntermediateResults: L1-R65, L1-Q07); página de legendas da AWS ("dashes are used to distinguish each speaker": L2-R95/C-R95; "natural pause": L2-R69); Azure "Segmentation silence timeout" (já em itens); Azure legendagem (R67 retirado).

## 1.4 Vizinhos conferidos (nenhum é gêmeo)

| vizinho | ponto do vizinho | por que R131 é distinto |
|---|---|---|
| L2-R69 (2.4) | a legenda do Transcribe permanece visível até uma pausa natural ou o fim da fala | R69 julga regra de exibição da legenda (página de legendas); R131 julga o conteúdo do campo audio_segments na saída em lote (página de entrada e saída). Páginas e frases diferentes |
| L2-Q16 (2.4) | nem toda pausa precisa ser registrada | Q16 é critério editorial de formatação; R131 é a estrutura da saída automática |
| L2-R68 (2.4) | duração do reconhecimento no Azure não inclui silêncio | outro fornecedor, outro campo (duração × segmento) |
| L1-R23, L1-R25 (1.1) | formato e taxa de amostragem do áudio (mesma página how-input) | outras seções da página; nada de estrutura de saída |
| L2-Q15 (2.4) | convenção para eventos não falados | R131 não trata de eventos |
| L2-R62 (2.4) | marcas de falante e sons suprimidas pelo Whisper | outro fornecedor e outro ponto |

## 1.5 Contagens

| quesito | valor |
|---|---|
| item novo | 1 (L2-R131) |
| gabarito | E (1 E, 0 C) |
| [TS] | 1; onda 3 com o saldo: 70 |
| VOLÁTIL | 0 |
| P2-2.4 depois do saldo | 20 itens (19 + 1); gabarito 10 C / 10 E |
| formatos de P2-2.4 (de 20), conforme recontagem do parecer R1 (TS 5, PC 3, SH 5) mais o R131 em PC | SH 5, TS 5, AP 4, PC 4, D 1, NP 1 (maior: SH 25%, TS 25%); teto de 30% cumprido |
| aderência de P2-2.4 | R131 direta: 11 diretas em 20; PARCIAIS: 9 |
| CONFERÊNCIA DE BASE (jan/2027) | R131 (reabrir a URL e conferir o trecho da Parte 3 e o SHA-256) |

Estilo (regras/estilo_banca.md): E por troca de um único conceito; sem marcador absoluto ("sempre", "só", "apenas", "qualquer", "nunca"); item de 58 palavras, com moldura de situação.

FIM DA PARTE 1/3

=====================================================================
PARTE 2/3 — (d) ITEM DO ESTUDANTE
=====================================================================

L2-R131. Julgue o item.
Na transcrição em lote de uma reunião de comissão pelo Amazon Transcribe, o arquivo de saída traz o elemento items, com dados de cada palavra e de cada sinal de pontuação, e o elemento audio_segments, que registra, com horário de início e de fim, as pausas existentes entre as falas.

FIM DA PARTE 2/3

=====================================================================
PARTE 3/3 — (d-G) GABARITO COMENTADO
=====================================================================

L2-R131. E [TS]. Segundo a documentação do Amazon Transcribe, um segmento de áudio é um trecho da gravação com fala ininterrupta e pausas mínimas, registrado em audio_segments com horário de início e de fim; a pausa não é o que o segmento registra. O item troca "trechos de fala contínua" por "as pausas existentes entre as falas" (única troca); a oração sobre o elemento items é verdadeira.
Base: AWS, Amazon Transcribe Developer Guide, "Data input and output" (https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html), página aberta e lida em 18/10/2026 (HTTP 200; verificado em 18/10/2026; SHA-256 do HTML baixado: 79c5144dbc6cecc36e920b9e5a615c52cc37986f99a3589d2ade5bf1b92b1eeb, para a conferência de janeiro). Trechos literais: "items : Contains information on each word and punctuation mark from the transcripts section."; "audio_segments : An audio segment is a specific portion of an audio recording that contains uninterrupted spoken language, with minimal pauses or breaks. This segment captures a natural flow of speech and is captured in audio_segments with a start time and end time."; "This includes start time, end time, a confidence score, and a type ( pronunciation or punctuation )." Não VOLÁTIL: o item não usa limite, versão, preço, idioma nem parâmetro; depende só da definição de campo da saída. CONFERÊNCIA DE BASE (4–8/1/2027). Aderência: DIRETA (marcação de pausa na transcrição).

## Tabela de proveniência (página aberta e lida em 18/10/2026)
| fonte | URL oficial | data da página / verificação | usada em |
|---|---|---|---|
| AWS, Amazon Transcribe Developer Guide, "Data input and output" | https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html | página sem data de publicação; aberta e lida em 18/10/2026 (HTTP 200); verificado em 18/10/2026 | R131 |

Fontes abertas na busca do ponto e não usadas: AWS channel-id e diarization; Google "Detect different speakers"; Microsoft quickstart de diarização em tempo real e "How to recognize speech" (silêncio); AWS "Creating video subtitles"; AWS Call Analytics (non-talk time: aderência de call center, fora do contexto); Whisper transcribe.py (hallucination_silence_threshold: tema de 1.8); Portal da Câmara, "Entenda como é feito o registro do discurso parlamentar" e rol do DETAQ de 2009 (documento antigo, sem regra de formatação atual, nomenclatura anterior ao Derep); w3.org (WCAG, WebVTT): host inacessível nesta sessão.

## Dúvidas à Gerência (D1 da gce-gerencia)
1. Natureza da base: documentação de fornecedor de ferramenta nomeada no edital (1.8), mesma categoria de L2-R69 e L2-R70.
2. Formato: PC pela oposição entre trecho de fala contínua e pausa e entre items e audio_segments; se a QA o ler TS, a 2.4 fica com TS 6/20 (30%), no teto.
3. Aderência: classificada direta (marcação de pausa na estrutura da transcrição). Se a QA a ler PARCIAL (tema de 1.8/ferramenta), a 2.4 fica com 10/20 diretas, ainda no piso da seção 3.3 da T97_reconciliacao.
4. Nota de limite: o nome do campo (audio_segments) é da estrutura atual da saída; por isso a conferência de janeiro compara o SHA-256 da página.

FIM DA PARTE 3/3
FIM DO LOTE
