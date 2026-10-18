# QA_T97C_R1_2026-10-18_gce-cqfp.md — T-97 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L2_reforco_onda3_C_v1.md (gce-cpp; 28 itens AUTORAL, L2-R75 a L2-R102; P2-2.5 e P2-2.6). Rodada R1. Revisora: gce-cqfp (opus; não produziu). Ciclo 2026-10-18 s12c4. Sem commit.
Entradas: linha T-97 (TAREFAS.md); D-REFORCO-1/2, D-FONTE-DATA-ANTERIOR, D-T89-R1-ACEITE, D-T96-ONDA2-ACEITE (II, critério de VOLÁTIL), D-ONDA3-FILA, D-ADERENCIA (DECISOES.md); T90_reconciliacao e QA_T90_R1 (reprovações de escopo de L2-R09/R10/R11 na onda 1: norma fora do edital; ferramenta de avaliação não é editor); T96_reconciliacao, seção 4 (ponto contra o pacote inteiro); QA_T96C_R1, ponto 1 (docstring do repositório oficial do Whisper aceito como documentação do fornecedor; código lido, não execução); saida/banco/estilo_onda_2.md (recomendações 1–7 à onda 3); edital/modulo_RF_IA_P2.md (2.5 "Normalização de texto: números, siglas, abreviações e termos técnicos"; 2.6 "Ferramentas de CAT (Computer Assisted Transcription) e editores de transcrição"); pacote.json v1.9; L2_reforco_onda1_v3.md; ondas 2 (A_v3, B_v2, C_v2, D_v3, saldo_v2) e 3 (A_v1, D_v1; B_v1 inexistente nesta data).

## 1. Evidência — todas as bases reabertas por esta coordenação em 18/10/2026

| fonte | resultado | trechos conferidos (literal) |
|---|---|---|
| learn.microsoft.com …/how-to-custom-speech-human-labeled-transcriptions | 200; "Last updated on 2025-12-29" | "Abbreviations that are pronounced as words shouldn't be edited (such as … "NATO")"; "Write out abbreviations that are pronounced as separate letters with each letter separated by a space"; "If you use audio, transcribe numbers as words that match the audio … "one oh one""; "Write out abbreviations in words"; tabela "Dr. Bruce Banner → Doctor Bruce Banner"; "The following normalization rules are automatically applied … Use lowercase letters … Remove all punctuation except apostrophes within words … Expand numbers into words/spoken form"; seção German: "Write decimal points as "," and not "."" — CONFERE (R75–R78, R88). Nota: as regras de R75, R76 e R78 estão na seção "Text normalization for US English". |
| learn.microsoft.com …/display-text-format | 200 | "Inverse Text Normalization (ITN) is a process that converts verbalized forms …"; "Some of the supported text formats include dates, times, decimals, currencies, addresses, emails, and phone numbers" — CONFERE (R86) |
| learn.microsoft.com …/how-to-custom-speech-display-text-format | 200 | "The philosophy of pattern-based custom ITN …"; "figures out how the words might be spoken"; exemplo JO:500 — CONFERE (R82) |
| learn.microsoft.com …/captioning-concepts | 200 | "hh:mm:ss,fff" (SRT); "hh:mm:ss.fff" (WebVTT); "One tick represents one hundred nanoseconds"; "associated with the first audio byte processed by the SDK"; "the offset begins when you start recognition"; exemplo "00:00:00,180 --> 00:00:03,230" — CONFERE (R89, R90, R92, R96) |
| learn.microsoft.com …/azure-video-indexer/customize-language-model-how-to | 200; sem aviso de aposentadoria na página | "From transcript edits"; "uses only the last version of the corrected line for updating the language model" — CONFERE (R100) |
| docs.aws.amazon.com …/custom-vocabulary-create-table.html | 200 | "Digits ( 0-9 ) are only supported in the DisplayAs column"; "you must spell them out"; "A.B.C."; "A.B.C.-s"; "Acronyms are not supported in all languages"; "supports symbols and special characters (for example, C++)" — CONFERE (R80, R81, R87) |
| docs.aws.amazon.com …/supported-languages.html (aberta por esta QA, não citada) | 200 | pt-BR: coluna "Acronyms" = "batch, streaming" — o R81 vale para o português do Brasil; VOLÁTIL (c) mantido pela ressalva da própria página |
| docs.aws.amazon.com …/subtitles.html | 200 | "default start index of 0 … differs from the more widely used value of 1"; "compatibility errors … be sure to verify which start index you require"; "This applies to both WebVTT and SubRip formats"; "a regular transcript file (containing additional information)" — CONFERE (R94, R95, R102) |
| docs.cloud.google.com …/reference/rest/v1/speech/recognize | 200; "Last updated 2025-10-23 UTC" | "Sequential list of transcription results corresponding to sequential portions of audio"; "A speech recognition result corresponding to a portion of the audio"; "May contain one or more recognition hypotheses" — CONFERE (R101) |
| raw.githubusercontent.com openai/whisper main: normalizers/basic.py, normalizers/english.py, normalizers/english.json, utils.py | 200; SHA-256 IGUAIS aos declarados (4742eaa0…, d31a5268…, 6607f948…, f46aa555…) | basic.py l. 61–62 (regex e comentários "remove words between brackets/parenthesis"), docstring de remove_symbols_and_diacritics, assinatura `remove_diacritics: bool = False`; english.py l. 454 (docstring "Applies British-American spelling mappings"), l. 539 (`re.sub(r"(\d),(\d)", r"\1\2", s)  # remove commas between digits`, antes de standardize_numbers); english.json l. 276 ("colour": "color"); utils.py WriteSRT `decimal_marker = ","`, WriteVTT `"."`, WriteTSV docstring (milissegundos inteiros; vírgula decimal), WriteTXT (só texto), WriteJSON/WriteJSONL; **iterate_result l. 196–228: o `replace("-->", "->")` só ocorre no ramo SEM marcas de tempo por palavra (else); no ramo com "words" o texto do trecho não é tocado** (ver R96) |
| raw.githubusercontent.com oTranscribe/oTranscribe master README.md | 200; SHA-256 igual (8089e136…) | "Pause (ESC), rewind (F1) and fast-forward (F2) without taking your hands off the keyboard"; localStorage "every second" — CONFERE (R98, R99) |

Nenhuma base deixou de ser reaberta. Nenhuma base de data anterior (D-FONTE-DATA-ANTERIOR não invocada; correto). Nenhuma norma citada (checklist 6: nada PENDENTE NORMATIVO).

**Itens do Whisper "executados" (R79, R83, R84, R85).** A base declarada é texto do repositório oficial (docstring, comentário de código, assinatura, arquivo de mapeamento), não a execução. Conferido por leitura, sem executar: R79 sai do docstring de EnglishSpellingNormalizer + english.json; R83 sai do comentário e da regex da l. 539 ("3,5" → "35" é leitura direta da regex, aplicada antes do normalizador de números, que não altera "35"); R84 sai dos comentários e regex da l. 61–62; R85 sai do docstring ("drop any diacritics") + assinatura (opção, padrão False). **Nenhum gabarito depende da execução local**; a execução da produtora é só corroboração e não deve constar como base (ver AJUSTAR de registro, seção 3). Comentário de código é base mais fraca que docstring (precedente QA_T96C_R1 trata de docstring); aceito aqui porque o comentário vem colado à linha de código que o confirma, com SHA registrado para janeiro.

## 2. Ponto único, gêmeos e escopo

- Ponto único na folha: 14 + 14 pontos distintos entre si e dos 6 existentes de cada folha (L2-Q17–Q20, R09, R10 em 2.5; L2-Q21–Q23, R11–R13 em 2.6). CONFERE.
- Contra o pacote inteiro (T96_reconciliacao, seção 4): busca própria no pacote.json v1.9 (NATO, DisplayAs, tick, SRT/SubRip/WebVTT, localStorage, Video Indexer, índice, travessão, diacrítico, colchete, vírgula, ITN, abreviação, sigla, JSON, TSV, TXT, alemão, teclado, porções, alternativas, extenso) e nas ondas 1–3: **nenhum gêmeo**. Vizinhanças declaradas pela produtora conferidas e corretas (R80/R81/R87 × L1-R84/L1-R101; R82 × L1-R87; R86 × L2-Q17; R101 × L2-R11; R89 × L2-Q23; R84 × L2-Q15). R26 da parte A usa a mesma página HLT com ponto distinto (definição de transcrição rotulada).
- Escopo/aderência (D-ADERENCIA). Critério desta QA: em 2.5, direta quando o ponto é normalização de números, siglas, abreviações ou termos técnicos; em 2.6, direta quando o ponto é função do editor ou propriedade do formato que o editor usa para sincronizar texto, tempo e falante (precedente canônico L2-Q23); PARCIAL quando o ponto é detalhe de saída de serviço ou de implementação, com o editor só como moldura. Resultado:
  - 2.5 direta: R75, R76, R77, R78, R80, R81, R82, R83, R86, R87. **PARCIAL: R79** (grafia britânica × americana, só em inglês; não é número, sigla, abreviação nem termo técnico), **R84** (remoção de marcações de eventos: matéria de 2.4 vista pelo normalizador de comparação), **R85** (diacríticos: fora da enumeração de 2.5). **R88: fora** (ver REPROVADO).
  - 2.6 direta: R89, R90, R92, R93, R95, R97, R98, R99, R100. **PARCIAL: R91** (JSON × JSON Lines do escritor do Whisper), **R94** (índice inicial padrão do Amazon Transcribe), **R101** (estrutura da resposta da API do Google), **R102** (arquivo de transcrição regular gerado com as legendas). **R96: fora** (ver REPROVADO).
  - Registro para a Gerência (D1): em 2.6 só R98, R99 e R100 julgam função de editor propriamente dita; 11 de 14 julgam formato ou saída de serviço. Não é vício de item, mas a folha fica deslocada do seu objeto; o substituto de R96 deve julgar função de editor.

## 3. Veredito por item

**L2-R75 — APROVADO.** E [TS] PC; inverte os dois tratamentos (palavra × letra a letra); uma troca. Base literal.
**L2-R76 — AJUSTAR (texto).** C correto pela base, mas a regra está na seção "US English" e o enunciado põe um orador de audiência pública dizendo "um zero um" (português), o que abre recurso: a orientação para o inglês não rege áudio em português. Ajuste: "audiência pública conduzida em inglês" e o exemplo da própria página ("one oh one"), como já faz o R78.
**L2-R77 — APROVADO.** E [TS] PC; minúsculas e pontuação corretas, troca única no sentido da conversão. VOLÁTIL (b) baixo/médio correto.
**L2-R78 — APROVADO.** C AP; literal ("Write out abbreviations in words"; "Doctor Bruce Banner"). Ambientação verossímil (audiência com convidado estrangeiro).
**L2-R79 — AJUSTAR (registro).** C SH; base textual (docstring + english.json), sem dependência de execução. Aderência PARCIAL (seção 2): só simulado diagnóstico. Retirar da justificativa o "executado em 18/10/2026" como apoio do gabarito (manter só na proveniência, como corroboração).
**L2-R80 — APROVADO.** E [TS] PC; troca das colunas; literal.
**L2-R81 — APROVADO.** C [TS] espelho SH; literal; pt-BR com suporte a siglas (supported-languages, aberta por esta QA). VOLÁTIL (c) correto.
**L2-R82 — APROVADO.** C SH; literal; VOLÁTIL (c) coerente com L1-R87.
**L2-R83 — AJUSTAR (texto + registro).** C [TS] espelho; base = comentário + regex (l. 539), gabarito lido no código. Formato AP sem aplicação parlamentar (só "português do Brasil"): incluir a moldura ("transcrição de uma sessão de comissão") ou reclassificar, conferindo o teto de 30%. Retirar a execução da justificativa como apoio.
**L2-R84 — AJUSTAR (registro).** E [TS] AP; base = comentários + regex (l. 61–62); troca única. Aderência PARCIAL. Retirar a execução da justificativa como apoio.
**L2-R85 — AJUSTAR (texto + registro).** E [TS]; base = docstring + assinatura. (1) Formato AP sem nenhuma ambientação parlamentar: incluir a moldura (ex.: "transcrição de reunião de comissão") ou reclassificar. (2) VOLÁTIL: o gabarito depende de opção configurável (padrão False) de módulo periférico do Whisper (normalizador de avaliação), hipótese (c) da D-T96-ONDA2-ACEITE; marcar VOLÁTIL (baixo). Com isso 2.5 fica com 4 VOLÁTEIS — 20% só com 20 itens, logo o substituto de R88 não pode ser VOLÁTIL. (3) Aderência PARCIAL. (4) Retirar a execução da justificativa.
**L2-R86 — APROVADO.** E [TS] TS; restringe a ITN a números; lista exemplificativa sustenta o E.
**L2-R87 — APROVADO.** C TS; literal.
**L2-R88 — REPROVADO.** Extrapolação do edital: cobra a convenção decimal da orientação do Azure para o **alemão**; o candidato só acerta sabendo ortografia alemã ou a página, e o ponto declarado ("a convenção muda com o idioma") não é o que o enunciado julga. Não há aplicação a transcrição em português nem a contexto parlamentar. A própria produtora o indicou como o mais distante (dúvida 5). Substituir por item de 2.5 sobre número, sigla ou abreviação aplicável a pt-BR, não VOLÁTIL, formato diferente de SH e AP (que estão em 5/20), preferencialmente NP (2.5 fica sem NP).
**L2-R89 — APROVADO.** E [TS] PC; doc do Azure literal + código do Whisper; aderência direta (precedente L2-Q23).
**L2-R90 — APROVADO.** C NP; conta correta (12.500.000 × 100 ns = 1,25 s). Ressalva de estilo: o enunciado dá a definição do tick, e o item vira aritmética de baixa discriminação (estilo_onda_2, recomendação 7); sem efeito.
**L2-R91 — AJUSTAR (registro).** C PC; código (json.dump × laço com json.dumps por trecho), gabarito lido no texto. Aderência PARCIAL.
**L2-R92 — APROVADO.** C [TS] espelho SH; literal; consequência aritmética legítima; "independentemente" em C, compensado pelo R85 (O-2).
**L2-R93 — AJUSTAR (texto).** E [TS]; docstring de WriteTSV literal; troca única. Formato AP sem aplicação parlamentar (só configuração regional pt-BR): incluir moldura ("editor usado na revisão das sessões") ou reclassificar.
**L2-R94 — AJUSTAR (registro).** C NP; literal; VOLÁTIL (b) correto. Aderência PARCIAL (padrão de saída do serviço; o editor é moldura).
**L2-R95 — APROVADO.** E [TS] TS; "This applies to both WebVTT and SubRip" literal; troca única.
**L2-R96 — REPROVADO.** (1) Gabarito condicional: em utils.py (SHA f46aa555…, l. 196–228) o `replace("-->", "->")` só se aplica no ramo sem marcas de tempo por palavra; com word timestamps, o texto do trecho é gravado sem essa substituição. O enunciado não fixa a opção, e "grava o texto sem nenhuma modificação" (E) pode ser verdadeiro em configuração válida — ambiguidade que a banca anularia. (2) Base é corpo de código, sem docstring nem comentário. (3) Extrapolação: detalhe interno da implementação de referência, fora do objeto de 2.6. Substituir por item de 2.6 que julgue função de editor de transcrição, não VOLÁTIL, preferencialmente E (2.6 fica 7 C / 6 E).
**L2-R97 — APROVADO.** E [TS] TS; WriteTXT só imprime o texto em todos os ramos; relevante para sincronização no editor.
**L2-R98 — AJUSTAR (texto).** C AP; README literal. Formato AP com "reuniões" genéricas: dar a moldura parlamentar ("reuniões de comissão"). Ressalva de estilo: C existencial ("há editores…") de baixa discriminação (estilo_onda_2, recomendação 7).
**L2-R99 — APROVADO.** C SH; literal; VOLÁTIL (c) conservador, admitido.
**L2-R100 — APROVADO.** E [TS] TS; literal; VOLÁTIL (b) conservador, admitido.
**L2-R101 — AJUSTAR (registro).** E [TS] PC; literal; troca única. Aderência PARCIAL (estrutura da resposta da API).
**L2-R102 — AJUSTAR (registro).** C [TS] espelho AP; literal. Aderência PARCIAL.

## 4. Conformidade da parte (depois desta R1)

- Taxa: **REPROVADOS 2/28 = 7,1%** (R88, R96); AJUSTAR texto 5 (R76, R83, R85, R93, R98); AJUSTAR só de registro 6 (R79, R84, R91, R94, R101, R102); APROVADOS 15. Gate de 30%: não acionado. Nenhum ajuste muda gabarito.
- Gabarito: v1 14 C / 14 E (50%). Sem R88 e R96 (ambos E): 14 C / 12 E em 26 (53,8%); faixa 40–60% cumprida; com os dois substitutos fica entre 50% e 57%.
- [TS]: 18/28 conferidos; cada E [TS] troca exatamente um conceito (R75, R77, R80, R84, R85, R86, R89, R93, R95, R97, R100, R101; R88 e R96 também, mas reprovados); 4 C espelho (R81, R83, R92, R102; convenção O-6). Depois das reprovações, 16/26 (exigência metade + 2 = 15 para 26; 16 para 28).
- VOLÁTIL: 6 declarados, todos baixo ou baixo/médio, critério da D-T96-ONDA2-ACEITE aplicado corretamente; +R85 recomendado (c). 2.5: 4/20 (20%, no teto, com substituto não VOLÁTIL); 2.6: 3/20 (15%). Risco alto: 0.
- Formato (≤ 30%): 2.5 sem R88 = D 2, SH 5, AP 5, PC 4, TS 3, NP 0 (19); 2.6 sem R96 = D 2, PC 4, SH 3, TS 4, AP 4, NP 2 (19). Nenhum D novo (correto). Os rótulos AP de R83, R85, R93 e R98 só se sustentam com a moldura pedida; se a Gerência preferir reclassificar, refazer a contagem (SH já está em 5/20 em 2.5).
- Estilo (estilo_onda_2, 1–7): "independentemente" em C (R92) e E (R85); concessiva "ainda que" em C (R76) e E (R84); "Segundo a…" variado; fonte nomeada; sem absolutos empilhados; ambientação fora da remissão. Ressalvas de discriminação baixa em R90 e R98 (sem efeito).
- Estrutura: PARTE 1/3–3/3, FIM DA PARTE, FIM DO LOTE presentes; Parte 2 sem gabarito, [TS], VOLÁTIL ou REVERIFICAR; Parte 3 com os mesmos 28 ids; linha 1 no formato. CONFERE.
- Normativo: nenhuma norma citada; nada PENDENTE NORMATIVO. Nomenclatura: "Casa"/"comissão", sem o departamento; correto.

## 5. Veredito geral

**APROVADO COM RESSALVAS — 2/28 reprovados (7,1%).** Para a v2: substituir R88 (2.5; não VOLÁTIL; preferencialmente NP) e R96 (2.6; função de editor; preferencialmente E); aplicar os 5 ajustes de texto; registrar aderência PARCIAL em R79, R84, R85, R91, R94, R101, R102 (só simulado diagnóstico, D-ADERENCIA); marcar R85 VOLÁTIL (baixo); tirar a execução local da justificativa de R79, R83, R84 e R85 (base = texto do repositório). Todos continuam QA PENDENTE até a R2 e a reconciliação da gce-gerencia.

| id | folha | gab. | [TS] | formato | VOLÁTIL | aderência | veredito |
|---|---|---|---|---|---|---|---|
| L2-R75 | 2.5 | E | sim | PC | n | direta | APROVADO |
| L2-R76 | 2.5 | C | — | SH | n | direta | AJUSTAR (texto) |
| L2-R77 | 2.5 | E | sim | PC | S | direta | APROVADO |
| L2-R78 | 2.5 | C | — | AP | n | direta | APROVADO |
| L2-R79 | 2.5 | C | — | SH | n | PARCIAL | AJUSTAR (registro) |
| L2-R80 | 2.5 | E | sim | PC | n | direta | APROVADO |
| L2-R81 | 2.5 | C | espelho | SH | S | direta | APROVADO |
| L2-R82 | 2.5 | C | — | SH | S | direta | APROVADO |
| L2-R83 | 2.5 | C | espelho | AP | n | direta | AJUSTAR (texto) |
| L2-R84 | 2.5 | E | sim | AP | n | PARCIAL | AJUSTAR (registro) |
| L2-R85 | 2.5 | E | sim | AP | S (recomendado) | PARCIAL | AJUSTAR (texto) |
| L2-R86 | 2.5 | E | sim | TS | n | direta | APROVADO |
| L2-R87 | 2.5 | C | — | TS | n | direta | APROVADO |
| L2-R88 | 2.5 | E | sim | NP | n | fora | REPROVADO |
| L2-R89 | 2.6 | E | sim | PC | n | direta | APROVADO |
| L2-R90 | 2.6 | C | — | NP | n | direta | APROVADO |
| L2-R91 | 2.6 | C | — | PC | n | PARCIAL | AJUSTAR (registro) |
| L2-R92 | 2.6 | C | espelho | SH | n | direta | APROVADO |
| L2-R93 | 2.6 | E | sim | AP | n | direta | AJUSTAR (texto) |
| L2-R94 | 2.6 | C | — | NP | S | PARCIAL | AJUSTAR (registro) |
| L2-R95 | 2.6 | E | sim | TS | n | direta | APROVADO |
| L2-R96 | 2.6 | E | sim | SH | n | fora | REPROVADO |
| L2-R97 | 2.6 | E | sim | TS | n | direta | APROVADO |
| L2-R98 | 2.6 | C | — | AP | n | direta | AJUSTAR (texto) |
| L2-R99 | 2.6 | C | — | SH | S | direta | APROVADO |
| L2-R100 | 2.6 | E | sim | TS | S | direta | APROVADO |
| L2-R101 | 2.6 | E | sim | PC | n | PARCIAL | AJUSTAR (registro) |
| L2-R102 | 2.6 | C | espelho | AP | n | PARCIAL | AJUSTAR (registro) |
