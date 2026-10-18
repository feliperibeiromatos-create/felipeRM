# L2_reforco_onda3_saldo_v1.md — T-105 — 2026-10-18 — gerado por gce-cpp

Tarefa T-105, saldo da onda 3 do reforço (D-REFORCO-2), ciclo s12c4. Escopo: 1 item AUTORAL, L2-R131, folha P2-2.4, em reposição ao L2-R67 (retirado na T97_reconciliacao, seção 1; o id L2-R67 não é reutilizado). Rótulo: AUTORAL. QA PENDENTE: o item não passou por QA (D-QA-PENDENTE) e não entra em simulado antes da R1 da gce-cqfp. Convenção de base: "verificado em 18/10/2026" significa página aberta e lida nesta data, nesta sessão (HTTP 200); nenhuma data anterior foi usada (D-FONTE-DATA-ANTERIOR não foi necessária). Nenhuma norma citada.

=====================================================================
PARTE 1/3 — MAPA
=====================================================================

## 1.1 Item novo

Formatos: D = definição; TS = troca de sujeito; SH = situação hipotética; NP = número ou prazo; PC = par confundível; AP = aplicação parlamentar.

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL |
|---|---|---|---|---|---|
| L2-R131 | P2-2.4 | Na identificação de canais do Amazon Transcribe (um orador por canal, rótulos ch_0 e ch_1), quando dois oradores falam ao mesmo tempo, os carimbos de tempo dos dois canais se sobrepõem: a fala simultânea é preservada por canal, e não intercalada em sequência | PC (sobreposição por canal × falas em sequência) | https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html (AWS, Amazon Transcribe Developer Guide, "Transcribing multi-channel audio", parágrafo da seção channel_labels) | n |

## 1.2 Atendimento dos requisitos da T-105

| requisito | atendimento |
|---|---|
| folha P2-2.4 | sim; entrada 2.4 do edital ("Formatação de transcrições parlamentares: identificação de oradores, marcação de pausa ruído, etc.") |
| gabarito E com [TS] de troca única | sim; um único termo muda: a negação "não" antes de "se sobrepõem" |
| aderência direta ao texto da 2.4 | sim; o ponto é a identificação do orador por rótulo de canal e a representação, na transcrição, da fala simultânea (evento que a formatação deve tratar). Nada de competência, prazo ou estrutura de órgão |
| sem regra de condução da sessão | sim; nenhuma norma regimental citada |
| sem metafato de escopo de página | sim; o ponto é o comportamento descrito do recurso (como as falas simultâneas aparecem na saída), e não o que a página declara cobrir |
| formato diferente de SH e AP, de preferência NP ou PC | sim; PC. Ressalva na seção "Dúvidas à Gerência", item 2 |
| ponto distinto dos 19 da folha | sim (seção 2) |
| sem gêmeo no pacote inteiro nem nas partes A, C, D da onda 3 | sim (seção 3) |
| base oficial aberta hoje, trecho literal, "verificado em 18/10/2026" | sim (Parte 3) |
| não VOLÁTIL | sim; o item não usa o limite de canais, nem versão, preço ou idioma; só o comportamento descrito em nota da página |

## 2 Verificação de não repetição na folha P2-2.4 (os 19 vigentes)

Conferidos: pacote.json v1.9 (L2-Q13, Q14, Q15, Q16, L2-R07, L2-R08), L2_reforco_onda1_v3.md e L2_reforco_onda3_B_v2.md (R61, R62, R63, R64, R65, R66, R68, R69, R70, R71, R72, R73, R74; R67 retirado).

| vizinho | ponto do vizinho | por que R131 é distinto |
|---|---|---|
| L2-Q13 | cada fala atribuída a um orador identificado de forma padronizada, com a troca de orador sinalizada | Q13 julga o princípio de atribuição e sinalização; R131 julga como a fala simultânea de dois canais aparece nos carimbos de tempo de um serviço |
| L2-Q15 | convenção uniforme para eventos não falados | Q15 trata de eventos não falados (palmas, risos, inaudível); R131 trata de falas, não de eventos |
| L2-Q16 | nem toda pausa precisa ser registrada | R131 não trata de pausa |
| L2-Q14 | aparte registrado sob o rótulo do orador com a palavra | Q14 é critério de rotulagem do aparte; R131 não trata de aparte |
| L2-R62 | marcas de falante e anotações de sons: supressão pelo Whisper | R62 julga o que se suprime na geração; R131 julga a sobreposição de carimbos por canal |
| L2-R70, R72 | diarização do Google e do Azure (resultados agregados; informação de falante por frase) | R70 e R72 julgam a saída da diarização; R131 julga a identificação de canais (um orador por canal), que é outro recurso |
| L2-R68, R69 | duração sem silêncio (Azure); exibição da legenda (Transcribe) | pontos de sincronia e exibição; R131 não trata de legenda nem de duração |
| L2-R07, R08, R61, R63, R64, R65, R66, R71, R73, R74, L2-R08 | Banco de Discursos, registro taquigráfico, ata, aparte, discurso escrito, sessão secreta, referência humana, aviso de legenda automática | nenhum trata de canais nem de fala simultânea |

## 3 Verificação de gêmeos em outras folhas e vizinhanças declaradas

Conferido contra: pacote.json v1.9 inteiro (busca por "ao mesmo tempo", "simult", "sobrepos", "overlap", "ch_0", "channel_labels", "speaker_labels", "spk_"; acertos só em itens alheios: seções de dashboard, clustering, endpointing e "transição simultânea" do Office); L1_reforco_onda1_v2, L1_reforco_onda2_A_v3 a D_v3 e saldo_v2; L2_reforco_onda1_v3; L2_reforco_onda3_A_v3 (v2/v3), C_v2 e D_v2 (busca textual: nenhum acerto sobre canais ou falas simultâneas).

Vizinhanças declaradas, conferidas e distintas (nenhum é gêmeo):

| vizinho | folha | ponto do vizinho | por que R131 é distinto |
|---|---|---|---|
| L1-R07 | 1.4 | com um microfone em canal próprio por parlamentar, a atribuição pode apoiar-se na separação por canais, abordagem distinta da diarização | R07 julga a distinção canais × diarização como abordagem de atribuição; R131 julga o efeito da identificação de canais sobre os carimbos de tempo na fala simultânea. Os dois itens não devem figurar no mesmo simulado (registro para a GBQ) |
| L1-R29 | 1.1 | vozes simultâneas em canal único podem ser tratadas como ruído de fundo e ignoradas (Google) | R29 julga canal único e fornecedor Google; R131 julga canais separados e Amazon Transcribe. Mesma família de problema, ponto contrário (canal único × um canal por orador) |
| curso 1.4 (pacote), pegadinha "a diarização resolve sozinha a fala sobreposta" | 1.4 | afirmação de curso, não item | R131 não julga diarização |

## 4 Contagens

| quesito | valor |
|---|---|
| item novo | 1 (L2-R131) |
| gabarito | E (1 E, 0 C) |
| [TS] | 1 (R131); onda 3 com o saldo: 70 |
| VOLÁTIL | 0 |
| P2-2.4 depois do saldo | 20 itens (19 + 1); gabarito 10 C / 10 E |
| formatos de P2-2.4 (de 20) | SH 5, TS 4, AP 4, PC 4, D 2, NP 1 (maior: SH, 25%); teto de 30% cumprido; definição nova: 0 |
| aderência de P2-2.4 | 11 diretas em 20 (10 + R131); PARCIAIS: 9 |
| VOLÁTEIS em P2-2.4 | 3/20 (R07, R61, R66); R131 não acrescenta |
| CONFERÊNCIA DE BASE (jan/2027) | R131 (reabrir a URL e conferir os dois trechos da Parte 3) |

Estilo (regras/estilo_banca.md): E por supressão de um único termo (a negação), sem marcador absoluto ("sempre", "só", "apenas", "qualquer", "nunca") no enunciado; item de 65 palavras, com moldura de situação.

FIM DA PARTE 1/3

=====================================================================
PARTE 2/3 — (d) ITEM DO ESTUDANTE
=====================================================================

L2-R131. Julgue o item.
Em uma reunião de comissão, dois oradores foram gravados, cada um em seu próprio canal de áudio, e a gravação foi transcrita no Amazon Transcribe com a identificação de canais. Nessa situação, as falas de cada canal recebem o rótulo do respectivo canal e, nos trechos em que os dois oradores falam ao mesmo tempo, os carimbos de tempo dos dois canais não se sobrepõem.

FIM DA PARTE 2/3

=====================================================================
PARTE 3/3 — (d-G) GABARITO COMENTADO
=====================================================================

L2-R131. E [TS]. Segundo a documentação do Amazon Transcribe, as falas de cada canal recebem o rótulo do canal (ch_0 e ch_1), e, se uma pessoa em um canal fala ao mesmo tempo que outra em canal distinto, os carimbos de tempo de cada canal se sobrepõem enquanto elas falam uma sobre a outra. O item troca "se sobrepõem" por "não se sobrepõem" (única troca).
Base: AWS, Amazon Transcribe Developer Guide, "Transcribing multi-channel audio" (https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html), página aberta e lida em 18/10/2026 (HTTP 200; verificado em 18/10/2026; SHA-256 do HTML baixado: 13d557e8f86168fbbab5c548984f9cc30dfd4ee4b2a2b3dcfc734695a29fa094, para a conferência de janeiro). Trechos literais: "In your transcript, channels are assigned the labels ch_0 and ch_1."; "Note that if a person on one channel speaks at the same time as a person on a separate channel, timestamps for each channel overlap while the individuals are speaking over each other." O item não usa o limite de canais da página (que traz o advérbio "currently") nem exemplo de código. Não VOLÁTIL. CONFERÊNCIA DE BASE (4–8/1/2027).

## Tabela de proveniência (página aberta e lida em 18/10/2026)
| fonte | URL oficial | data da página / verificação | usada em |
|---|---|---|---|
| AWS, Amazon Transcribe Developer Guide, "Transcribing multi-channel audio" | https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html | página sem data de publicação; aberta e lida em 18/10/2026 (HTTP 200); verificado em 18/10/2026 | R131 |
| AWS, Amazon Transcribe Developer Guide, "Partitioning speakers (diarization)" | https://docs.aws.amazon.com/transcribe/latest/dg/diarization.html | aberta e lida em 18/10/2026 (HTTP 200); só para separar recursos; nenhum item depende dela | nenhum (descartada) |

Fontes abertas na busca do ponto e não usadas: learn.microsoft.com (diarização em tempo real do Azure Speech: "Speaker ID" é identificador genérico, ponto vizinho de L1-Q07 e L1C-Q27 da 1.4); cloud.google.com (Speech-to-Text, áudio multicanal: rótulo channel_tag, ponto vizinho de L1-R07); raw.githubusercontent.com openai/whisper (transcribe.py, parâmetro no_speech_threshold: processamento de silêncio, aderência marginal à 2.4). RICD, art. 17, I, "h" (não-apanhamento de discurso ou aparte pela taquigrafia): descartado por ser vizinho do L2-R08 (art. 73, VII e VIII) e por depender de regra de condução. Pontos descartados por VOLÁTIL provável: limite de 30 falantes e de dois canais (a página usa "currently" no segundo).

## Dúvidas à Gerência (D1 da gce-gerencia)
1. Natureza da base: a documentação da AWS é fonte oficial de fornecedor de ferramenta nomeada no edital (1.8), mesma categoria de L2-R69 e L2-R70.
2. Formato: o item é PC pela oposição entre a sobreposição preservada por canal e a intercalação em sequência (o item é o contrário da documentação). Se a gce-cqfp ou a Gerência o classificarem de outro modo (por exemplo, TS), a 2.4 fica com TS 5/20 (25%) e PC 3/20 (15%), dentro do teto; o item não é SH nem AP.
3. Aderência: classificada direta (identificação do orador por canal e representação da fala simultânea). Se a QA a ler PARCIAL (tema de 1.4), a 2.4 fica com 10/20 diretas, ainda no piso da seção 3.3 da T97_reconciliacao.

FIM DA PARTE 3/3
FIM DO LOTE
