# QA_T97C_R2_2026-10-18_gce-cqfp.md — T-97 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L2_reforco_onda3_C_v2.md (gce-cpp; 28 itens AUTORAL, L2-R75 a L2-R102; P2-2.5 e P2-2.6), contra a v1 e o parecer QA_T97C_R1_2026-10-18_gce-cqfp.md. Rodada R2 (última). Revisora: gce-cqfp (opus; não produziu). Sem commit nem push.
Entradas: R1 desta coordenação; v1 e v2; D-REFORCO-2 (regras 1 a 6), D-ADERENCIA, D-T96-ONDA2-ACEITE (II, critério de VOLÁTIL) em DECISOES.md; pacote.json v1.9; ondas 1 a 3 (A_v2, B_v1, que agora existe, e D_v1) para gêmeos.

## 1. Diff v1 → v2 (script próprio, python -I, por bloco de item)

- Parte 2 (enunciados) alterada só em: R76, R83, R85, R93, R98 (os 5 AJUSTAR de texto) e R88, R96 (substituídos). Nenhum outro enunciado mudou.
- Parte 3 (gabarito comentado) alterada só em: R76 (coerência com o novo enunciado), R79, R83, R84, R85 (execução retirada; aderência; R85 VOLÁTIL), R91, R94, R101, R102 (só "Aderência: direta" → "PARCIAL (D-ADERENCIA…)"), R88 e R96 (novos). R93 e R98 sem mudança na Parte 3 (a justificativa já cobria a moldura). Nenhum gabarito de item mantido mudou.
- Fora dos itens: cabeçalho de resposta (novo), convenção (frase sobre execução), siglas GRC e VIW, linhas do mapa de R79, R84, R85, R88, R91, R94, R96, R101, R102, contagens de VOLÁTIL de 2.5 (3 → 4), seção 3 (proximidades de R88 e R96; remoção da concentração HLT de R88 v1), lista de janeiro, proveniência (duas fontes novas) e dúvidas 1, 3 e 5. Todos coerentes com o parecer R1. Nada mais mudou.
- Conferência literal dos ajustes: R76 "audiência pública conduzida em inglês" e "one oh one" — CONFERE; R83 "transcrição de uma sessão de comissão, em português do Brasil" — CONFERE; R85 "Na avaliação da transcrição de reunião de comissão" — CONFERE; R93 "Em um editor de transcrição usado na revisão das sessões" — CONFERE; R98 "reuniões de comissão" — CONFERE.
- Execução local do Whisper: a palavra "execu" não aparece mais nos blocos de R79, R83, R84 e R85 da Parte 3 (aparecia nos quatro na v1). A execução ficou só como corroboração na convenção, nas contagens, na lista de janeiro e na proveniência, como pedido. Nota de registro: a lista de janeiro manda "repetir a execução de teste" em R83 a R85; é aceitável como corroboração, mas a reverificação se faz sobre o texto e o SHA-256, não sobre a execução.
- Marcas: aderência PARCIAL em R79, R84, R85, R91, R94, R101, R102 (7), no mapa e na Parte 3 — CONFERE. R85 VOLÁTIL (baixo), hipótese (c), no mapa, na Parte 3 ("inapto a simulado final até lá") e na lista de janeiro — CONFERE.
- Estrutura: 28 ids iguais nas Partes 2 e 3; Parte 2 sem gabarito, [TS], VOLÁTIL ou REVERIFICAR; FIM DA PARTE e FIM DO LOTE presentes; linha 1 no formato. CONFERE.

## 2. Evidência reaberta nesta rodada (18/10/2026)

| fonte | resultado | trecho conferido |
|---|---|---|
| docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig | 200; "Last updated 2025-10-23 UTC" | "Use transcription normalization to automatically replace parts of the transcript with phrases of your choosing."; Entry: "A single replacement configuration."; "caseSensitive boolean Whether the search is case sensitive." — CONFERE (R88). A página não condiciona o recurso (sem prévia, sem restrição de local) |
| learn.microsoft.com/en-us/azure/azure-video-indexer/edit-transcript-lines-portal | 200; título "View and update transcriptions in Azure AI Video Indexer website"; "Last updated on 2025-10-06"; "Applies to: Azure AI Video Indexer enabled by Azure Arc, Cloud-based Azure AI Video Indexer"; sem aviso de aposentadoria | "While in the edit mode, hover between two transcription lines. There's a gap between ending time of the transcript line and the beginning of the following transcript line. The add new transcription line option is visible."; "If there isn’t an option to add a new line, you can adjust the end/start time of the relevant transcript lines to fit a new line in your desired place." — CONFERE (R96) |
| raw.githubusercontent.com openai/whisper main normalizers/basic.py e english.py | 200; SHA-256 iguais aos declarados (4742eaa0…, d31a5268…) | basic.py l. 30 ("drop any diacritics"), l. 61 (`remove_diacritics: bool = False`), l. 69–70 (colchetes e parênteses); english.py l. 454 e l. 539 — CONFERE. Correção de registro da R1: as regex de colchetes e parênteses estão nas l. 69–70, não 61–62; e o `remove_diacritics` é parâmetro de `BasicTextNormalizer.__init__`, não da função remove_symbols_and_diacritics (a Parte 3 do R85 diz "assinatura" logo depois da função; imprecisão de registro, sem efeito no gabarito) |

Nenhuma base de data anterior; nenhuma norma citada (nada PENDENTE NORMATIVO).

## 3. Itens novos

**L2-R88 (2.5) — APROVADO, com ressalva de registro (formato).**
- Gabarito E correto: com a busca sensível à caixa, "Tcu" não corresponde a "TCU"; trocam-se 2 das 3 ocorrências, e não as 3. A conclusão vale com ou sem correspondência por substring.
- [TS] com troca única ("duas" → "três", isto é, a sensibilidade à caixa ignorada).
- Aderência direta: substituição de sigla por forma expandida no texto transcrito, núcleo de 2.5, e aplicável a pt-BR.
- Ponto único: na folha e no pacote. Contra L2-R10, mesma página, o ponto é distinto (R10 julga a ordem das entradas; R88, a caixa). Contra L1-R78, L1-R84 e L1-R87 também é distinto (capitalização como saída, não busca). Busca própria (TCU, Tcu, caseSensitive, transcriptNormalization, maiúsculas, sensível) no pacote v1.9 e nas ondas 1 a 3, inclusive B_v1: nenhum gêmeo.
- Não VOLÁTIL: correto. A caixa é premissa do enunciado, que não nomeia campo, limite nem padrão, e a página não condiciona o recurso. Mesmo rótulo do L2-R10.
- Formato: a classificação NP não se sustenta pelo critério da T91_reconciliacao, 3.1 (o formato segue a construção do ponto). O número "duas de três" é contagem criada pelo cenário, não número ou prazo documentado, e o ponto é o mecanismo da busca sensível à caixa, aplicado a uma situação hipotética. O registro correto é SH. Com isso, 2.5 fica com SH 6/20 (30%, no teto, sem folga) e NP 0; a regra 3 ("no máximo 30%") continua cumprida. Não muda texto nem gabarito: a Gerência fixa o rótulo SH na reconciliação (D1).
- Estilo: sem absolutos nem cauda falsa; moldura "reunião de comissão". Ressalva de baixa discriminação, porque o gabarito se deduz da premissa fixada no enunciado (estilo_onda_2, recomendação 7, como em R90); sem efeito.

**L2-R96 (2.6) — APROVADO.**
- Gabarito E correto: a documentação manda ajustar os horários de início e de término das linhas vizinhas, e não o texto delas. A troca é única (horário → texto). O "pode" do enunciado espelha o "you can" da página, e o E não fica ambíguo: editar o texto não abre intervalo na linha do tempo.
- Aderência direta: função de editor de transcrição (inserir linha, ajustar marcas de tempo), como pedido na R1. 2.6 passa a ter 4/14 itens de função de editor (R96, R98, R99, R100).
- Ponto único: distinto de Q22 e R12 (quem gera e para que serve a marca de tempo) e de R100 (outra página; retreinamento). Sem gêmeo no pacote nem nas ondas 1 a 3 (nova linha, linhas vizinhas, Video Indexer).
- Formato SH: 2.6 fica com SH 4/20.
- VOLÁTIL: a marcação "não" é admitida. O ponto é procedimento documentado do editor, sem versão, limite, padrão nem parâmetro nomeado, e a página não traz condição nem aviso de aposentadoria. Marcar VOLÁTIL por conservadorismo, como em R100, também seria admitido, e 2.6 iria a 4/20. Fica a critério da Gerência (D1), sem efeito na aprovação.
- Moldura "audiência pública". Estilo conforme.

## 4. Conformidade da parte (v2)

- Gabarito: 14 C / 14 E (50%); 7 C / 7 E por folha. Faixa da regra 5 cumprida.
- [TS]: 18/28, exigência de 16 cumprida, 9 por folha; cada E [TS] troca um só conceito; 4 C espelho (R81, R83, R92, R102).
- VOLÁTIL: 7 (R77, R81, R82, R85; R94, R99, R100). 2.5 com 4/20 = 20%, no teto, conferido; 2.6 com 3/20 = 15%; 0 de risco alto.
- Formato (folha de 20), com o R88 registrado como SH: 2.5 com D 2, SH 6, AP 5, PC 4, TS 3, NP 0; 2.6 com D 2, PC 4, SH 4, TS 4, AP 4, NP 2. Máximo de 30%, cumprido.
- Aderência: 21 direta e 7 PARCIAL (só simulado diagnóstico, D-ADERENCIA).
- Normativo: nada citado. Nomenclatura: correta.

## 5. Veredito geral

**APROVADO COM RESSALVAS — 0/28 reprovados (0%).** Gate de 30% não acionado. As ressalvas são só de registro, para a reconciliação da gce-gerencia, e nenhuma muda texto ou gabarito:
1. R88 com formato SH, não NP: 2.5 fica com SH 6/20, no teto.
2. R96 não VOLÁTIL, admitido; a marcação conservadora fica a critério da Gerência.
3. Linhas do basic.py corrigidas para l. 69–70, e a "assinatura" do R85 é de `BasicTextNormalizer.__init__`.
4. Na lista de janeiro, a reverificação se faz pelo texto e pelo SHA-256; a execução é só corroboração.

Os 28 itens seguem QA PENDENTE até a reconciliação e o aceite (D-QA-PENDENTE). R79, R84, R85, R91, R94, R101 e R102 vão só a simulado diagnóstico. Os 7 VOLÁTEIS ficam inaptos a simulado final até 4–8/1/2027.

| id | folha | gab. | [TS] | formato | VOLÁTIL | aderência | R1 | R2 |
|---|---|---|---|---|---|---|---|---|
| L2-R75 | 2.5 | E | sim | PC | n | direta | APROVADO | APROVADO |
| L2-R76 | 2.5 | C | — | SH | n | direta | AJUSTAR (texto) | APROVADO |
| L2-R77 | 2.5 | E | sim | PC | S | direta | APROVADO | APROVADO |
| L2-R78 | 2.5 | C | — | AP | n | direta | APROVADO | APROVADO |
| L2-R79 | 2.5 | C | — | SH | n | PARCIAL | AJUSTAR (registro) | APROVADO |
| L2-R80 | 2.5 | E | sim | PC | n | direta | APROVADO | APROVADO |
| L2-R81 | 2.5 | C | espelho | SH | S | direta | APROVADO | APROVADO |
| L2-R82 | 2.5 | C | — | SH | S | direta | APROVADO | APROVADO |
| L2-R83 | 2.5 | C | espelho | AP | n | direta | AJUSTAR (texto) | APROVADO |
| L2-R84 | 2.5 | E | sim | AP | n | PARCIAL | AJUSTAR (registro) | APROVADO |
| L2-R85 | 2.5 | E | sim | AP | S (baixo) | PARCIAL | AJUSTAR (texto) | APROVADO (registro: assinatura = __init__) |
| L2-R86 | 2.5 | E | sim | TS | n | direta | APROVADO | APROVADO |
| L2-R87 | 2.5 | C | — | TS | n | direta | APROVADO | APROVADO |
| L2-R88 (novo) | 2.5 | E | sim | SH (declarado NP) | n | direta | REPROVADO (v1) | APROVADO (registro: SH) |
| L2-R89 | 2.6 | E | sim | PC | n | direta | APROVADO | APROVADO |
| L2-R90 | 2.6 | C | — | NP | n | direta | APROVADO | APROVADO |
| L2-R91 | 2.6 | C | — | PC | n | PARCIAL | AJUSTAR (registro) | APROVADO |
| L2-R92 | 2.6 | C | espelho | SH | n | direta | APROVADO | APROVADO |
| L2-R93 | 2.6 | E | sim | AP | n | direta | AJUSTAR (texto) | APROVADO |
| L2-R94 | 2.6 | C | — | NP | S | PARCIAL | AJUSTAR (registro) | APROVADO |
| L2-R95 | 2.6 | E | sim | TS | n | direta | APROVADO | APROVADO |
| L2-R96 (novo) | 2.6 | E | sim | SH | n | direta | REPROVADO (v1) | APROVADO |
| L2-R97 | 2.6 | E | sim | TS | n | direta | APROVADO | APROVADO |
| L2-R98 | 2.6 | C | — | AP | n | direta | AJUSTAR (texto) | APROVADO |
| L2-R99 | 2.6 | C | — | SH | S | direta | APROVADO | APROVADO |
| L2-R100 | 2.6 | E | sim | TS | S | direta | APROVADO | APROVADO |
| L2-R101 | 2.6 | E | sim | PC | n | PARCIAL | AJUSTAR (registro) | APROVADO |
| L2-R102 | 2.6 | C | espelho | AP | n | PARCIAL | AJUSTAR (registro) | APROVADO |
