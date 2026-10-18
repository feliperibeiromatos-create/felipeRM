# L2_reforco_onda3_C_v2.md — T-97 — 2026-10-18 — gerado por gce-cpp

## RESPOSTA AO RELATÓRIO DE QA (QA_T97C_R1_2026-10-18_gce-cqfp.md; rodada de correção v2)

Veredito da QA: APROVADO COM RESSALVAS, 2/28 reprovados (7,1%; gate de 30% não acionado). Resposta item a item (aplicado o texto exato do parecer; nenhum gabarito mudou nos itens mantidos):

| id | pedido da QA | resposta | o que mudou na v2 |
|---|---|---|---|
| L2-R76 | AJUSTAR (texto) | acatado | Enunciado: "audiência pública conduzida em inglês" e o orador diz "one oh one" (exemplo da própria página, como no R78); gabarito C mantido. |
| L2-R79 | AJUSTAR (registro) | acatado | Retirado "executado em 18/10/2026" da justificativa (a base é o docstring e o english.json); aderência PARCIAL (só simulado diagnóstico). A nota sobre o docstring de números saiu do bloco do item e consta da dúvida 3. |
| L2-R83 | AJUSTAR (texto + registro) | acatado | Moldura "transcrição de uma sessão de comissão" (formato AP mantido; contagem de formatos inalterada); execução retirada da justificativa (base: comentário e expressão regular do código). |
| L2-R84 | AJUSTAR (registro) | acatado | Execução retirada da justificativa; aderência PARCIAL. |
| L2-R85 | AJUSTAR (texto + registro) | acatado | Moldura "transcrição de reunião de comissão"; VOLÁTIL (baixo), hipótese (c); aderência PARCIAL; execução retirada. Com isso, 2.5 fica em 4 de 20 VOLÁTEIS (20%, no teto), e o substituto do R88 não é VOLÁTIL. |
| L2-R88 | REPROVADO | acatado | Substituído por item novo (mesmo id), de 2.5, E [TS], NP, não VOLÁTIL, aplicável ao português (sigla TCU; Speech-to-Text do Google, normalização de transcrição). Ver Partes 2 e 3. |
| L2-R91 | AJUSTAR (registro) | acatado | Aderência PARCIAL. |
| L2-R93 | AJUSTAR (texto) | acatado | Moldura "editor de transcrição usado na revisão das sessões"; gabarito E e [TS] mantidos; formato AP mantido. |
| L2-R94 | AJUSTAR (registro) | acatado | Aderência PARCIAL; VOLÁTIL (baixo/médio) mantido. |
| L2-R96 | REPROVADO | acatado | Substituído por item novo (mesmo id), de 2.6, E [TS], função de editor de transcrição (ajuste de linhas no editor do Azure AI Video Indexer), não VOLÁTIL. Ver Partes 2 e 3. |
| L2-R98 | AJUSTAR (texto) | acatado | "reuniões de comissão"; C mantido. |
| L2-R101 | AJUSTAR (registro) | acatado | Aderência PARCIAL. |
| L2-R102 | AJUSTAR (registro) | acatado | Aderência PARCIAL. |

Itens APROVADOS sem ajuste (acatado; texto, gabarito e registro inalterados): L2-R75, R77, R78, R80, R81, R82, R86, R87, R89, R90, R92, R95, R97, R99, R100.
Pontos gerais da QA: (1) retirar a execução local do Whisper das justificativas de R79, R83, R84 e R85: acatado (a execução permanece só como corroboração de registro, na proveniência e na lista de janeiro; nenhum gabarito depende dela); (2) aderência PARCIAL em R79, R84, R85, R91, R94, R101 e R102: acatado (7 itens; só simulado diagnóstico, D-ADERENCIA); (3) ressalvas de estilo sobre R90 e R98 (discriminação baixa): acatado como registro, sem efeito, como a própria QA indica; (4) registro para a Gerência (D1) de que a folha 2.6 fica deslocada do seu objeto: acatado e registrado na dúvida 1 (com o substituto do R96, 4 de 14 itens julgam função de editor: R96, R98, R99, R100). Não acatado: nenhum.
Contagens depois da v2: 28 itens; 14 C / 14 E (50%); por folha 7 C / 7 E; [TS] 18 de 28 (9 em cada folha); VOLÁTEIS: 2.5 com 4 de 20 (20%) e 2.6 com 3 de 20 (15%), risco alto 0; formatos das duas folhas de 20 inalterados (2.5: D 2, SH 5, AP 5, PC 4, TS 3, NP 1; 2.6: D 2, PC 4, SH 4, TS 4, AP 4, NP 2); aderência 21 direta e 7 PARCIAL. Todos continuam QA PENDENTE até a R2 e a reconciliação da gce-gerencia (D-QA-PENDENTE).

=====================================================================
LOTE CORRIGIDO (mesma estrutura do v1)
=====================================================================

Tarefa T-97, onda 3 do reforço, parte C (ciclo s12c4), v2 (rodada de correção: responde ao QA_T97C_R1 e substitui o v1; substituídos L2-R88 e L2-R96). Escopo: P2 folhas 2.5 (normalização de texto: números, siglas, abreviações e termos técnicos) e 2.6 (ferramentas de CAT e editores de transcrição), 28 itens AUTORAL novos: L2-R75 a L2-R88 (+14) na folha 2.5 e L2-R89 a L2-R102 (+14) na folha 2.6. Cada folha passa de 6 para 20 itens. As folhas 2.1 a 2.4, 2.7 e 2.8 são das outras produtoras da onda 3 e não foram tocadas.
Rótulo de todos os itens: AUTORAL (produtor gce-cpp, lote L2-R, onda 3 do reforço, parte C). Nenhum item existente foi alterado. QA PENDENTE: nenhum item deste arquivo entra em simulado antes da QA da gce-cqfp (D-QA-PENDENTE).
Convenção: "verificado em 18/10/2026" = página ou arquivo aberto e lido nesta data, pelo gce-cpp, nesta produção. Nenhuma base de data anterior foi usada (D-FONTE-DATA-ANTERIOR não invocada). Nenhum item cita versão, preço ou limite numérico de produto; as contas de R90 (ticks) são aritmética do próprio enunciado. Nomenclatura: nenhum item menciona o departamento; onde a Casa aparece, é como "Casa" ou "comissão". Nenhuma norma foi citada (sem PENDENTE NORMATIVO). A execução local do código do Whisper, feita pela produtora, é só corroboração de registro: nenhum gabarito nem justificativa depende dela.
Entradas lidas: CLAUDE.md; regras/proveniencia.md; regras/estilo_banca.md; edital/modulo_RF_IA_P2.md (itens 2.5 e 2.6, escopo literal); linha T-97 de TAREFAS.md; D-REFORCO-1, D-REFORCO-2, D-FONTE-DATA-ANTERIOR, D-T89-R1-ACEITE, D-T96-ONDA2-ACEITE (critério de VOLÁTIL, seção II) e D-ONDA3-FILA em DECISOES.md; saida/gce/T90_reconciliacao_2026-10-18.md (legado de "definição" em 2.5 e 2.6, seção 4) e QA_T90_R1_2026-10-18_gce-cqfp.md (motivos das reprovações de escopo de R09, R10 e R11 da onda 1); saida/gce/T96_reconciliacao_2026-10-18.md (seção 4: ponto conferido contra o pacote inteiro); saida/banco/estilo_onda_2.md (O-1 a O-8 e recomendações à onda 3) e T93_reconciliacao_2026-10-18.md; saida/pacote/pacote.json v1.9 (334 itens, todos conferidos), GCE_Lote2_v2_CPP.md, GCE_Lote2_padroes_GCE.md, GCE_Lote2_consolidacao_GCE.md, L2_reforco_onda1_v3.md, as partes A a D e o saldo da onda 2 (L1-R19 a L1-R131) e as partes A e D da onda 3 (L2-R19 a L2-R46 e L2-R103 a L2-R130; a parte B, folhas 2.3 e 2.4, não existia no momento da conferência). Para a v2: QA_T97C_R1_2026-10-18_gce-cqfp.md (parecer), D-ADERENCIA, e, para as bases dos dois itens novos, as páginas abertas em 18/10/2026 (Google Cloud, RecognitionConfig; Microsoft Learn, "View and update transcriptions in Azure AI Video Indexer website"); a parte B continua inexistente nesta data.
Escopo literal (lição da onda 1): nenhum item toca LC 95/1998 nem regra de redação legislativa; nenhum item toca tela de avaliação de modelo (teste de acurácia, WER como métrica de produto). Em 2.5, todos os itens julgam como números, siglas, abreviações, grafias e termos técnicos são padronizados (ou não) no texto transcrito ou no texto de treinamento e de comparação. Em 2.6, todos os itens ancoram-se em editor de transcrição, revisor ou arquivo que o editor importa.

=====================================================================
PARTE 1/3 — MAPA
=====================================================================

## 1. Itens novos (um ponto de julgamento por item, único na folha e sem gêmeo no pacote)

Formatos: D = definição; TS = troca de sujeito; SH = situação hipotética; NP = número ou prazo; PC = par confundível; AP = aplicação parlamentar. Critério de classificação (T91_reconciliacao, seção 3.1): o formato é o da construção do ponto de julgamento, e não o do gabarito; o item C tem o formato da sua contraparte E. Nenhum item novo usa D (diluição do legado, T90_reconciliacao, seção 4). Siglas das bases: HLT = Microsoft Learn, "How to create human-labeled transcriptions"; DTF = Microsoft Learn, "Display text formatting with speech to text"; CDF = Microsoft Learn, "How to prepare display text format training data for custom speech"; CAP = Microsoft Learn, "Captioning with speech to text"; AWS-CV = Amazon Transcribe, "Creating a custom vocabulary using a table"; AWS-SUB = Amazon Transcribe, "Generating subtitle files"; W-BAS, W-ING, W-JSON, W-UT = arquivos do repositório oficial openai/whisper (whisper/normalizers/basic.py, english.py, english.json; whisper/utils.py), lidos em raw.githubusercontent.com; GRC = Google Cloud, Speech-to-Text, "RecognitionConfig" (REST v1); VIW = Microsoft Learn, "View and update transcriptions in Azure AI Video Indexer website".

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL | aderência |
|---|---|---|---|---|---|---|
| L2-R75 | P2-2.5 | A abreviação pronunciada como palavra (NATO) não se edita; a pronunciada letra a letra é escrita com as letras separadas por espaço | PC | HLT, "Text normalization for US English": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-human-labeled-transcriptions | n | direta |
| L2-R76 | P2-2.5 | Em transcrição de treinamento feita a partir do áudio, o número é escrito por extenso na forma em que foi pronunciada | SH | HLT (mesma URL) | n | direta |
| L2-R77 | P2-2.5 | Entre as regras automáticas de normalização das transcrições de treinamento está expandir números em palavras (não convertê-los em algarismos) | PC | HLT (mesma URL) | S (baixo/médio): regra automática = comportamento padrão do serviço | direta |
| L2-R78 | P2-2.5 | A orientação é escrever por extenso as abreviações ("Dr." como "Doctor") | AP | HLT (mesma URL) | n | direta |
| L2-R79 | P2-2.5 | O normalizador de grafia do Whisper para o inglês mapeia grafias britânicas para americanas ("colour" para "color"), de modo que as duas formas contam como a mesma palavra | SH | W-ING, docstring de EnglishSpellingNormalizer, e W-JSON: https://raw.githubusercontent.com/openai/whisper/main/whisper/normalizers/english.py ; https://raw.githubusercontent.com/openai/whisper/main/whisper/normalizers/english.json | n | PARCIAL (D-ADERENCIA: só simulado diagnóstico) |
| L2-R80 | P2-2.5 | No vocabulário em tabela do Amazon Transcribe, algarismos só na coluna DisplayAs; na Phrase, números por extenso | PC | AWS-CV: https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-table.html | n | direta |
| L2-R81 | P2-2.5 | Sigla pronunciada letra a letra entra com as letras separadas por pontos, e o s do plural liga-se por hífen (C.P.I.-s) | SH | AWS-CV (mesma URL) | S (baixo/médio): a página ressalva que siglas não são suportadas em todos os idiomas | direta |
| L2-R82 | P2-2.5 | Na ITN personalizada, informa-se o formato escrito desejado, e o serviço deduz as formas faladas | SH | CDF, "Custom ITN": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-display-text-format | S (baixo/médio): recurso de custom speech condicionado a locais com suporte | direta |
| L2-R83 | P2-2.5 | O normalizador do Whisper para o inglês remove vírgulas entre algarismos; sem adaptação, converteria "3,5" em "35" em texto em português | AP | W-ING, comentário "# remove commas between digits" (mesma URL de R79) | n | direta |
| L2-R84 | P2-2.5 | O normalizador básico do Whisper remove o texto entre colchetes e parênteses (marcações como [aplausos]); não o mantém | AP | W-BAS, comentários do método de chamada: https://raw.githubusercontent.com/openai/whisper/main/whisper/normalizers/basic.py | n | PARCIAL (D-ADERENCIA: só simulado diagnóstico) |
| L2-R85 | P2-2.5 | Com a opção de descartar diacríticos, "sessão" e "sessao" tornam-se a mesma palavra | AP | W-BAS (mesma URL de R84) | S (baixo): opção configurável (padrão desligada) de módulo periférico do Whisper, hipótese (c) | PARCIAL (D-ADERENCIA: só simulado diagnóstico) |
| L2-R86 | P2-2.5 | A ITN do Azure Speech abrange datas, horas, decimais, moedas, endereços, e-mails e telefones; não se restringe a números | TS | DTF, "Inverse Text Normalization": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/display-text-format | n | direta |
| L2-R87 | P2-2.5 | Na tabela do Amazon Transcribe, símbolos e caracteres especiais ("C++") são admitidos na coluna DisplayAs | TS | AWS-CV (mesma URL de R80) | n | direta |
| L2-R88 | P2-2.5 | Na normalização de transcrição por substituições, a entrada que distingue maiúsculas de minúsculas na busca só alcança a grafia exata: de três ocorrências (duas "TCU", uma "Tcu"), troca duas | NP | GRC, campo transcriptNormalization e objeto Entry: https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig | n | direta |
| L2-R89 | P2-2.6 | Intervalo de tempo: SRT usa vírgula (hh:mm:ss,fff) e WebVTT usa ponto (hh:mm:ss.fff) | PC | CAP, "Caption output format": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/captioning-concepts ; W-UT: https://raw.githubusercontent.com/openai/whisper/main/whisper/utils.py | n | direta |
| L2-R90 | P2-2.6 | Um tick equivale a cem nanossegundos; 12.500.000 ticks de deslocamento = 1,25 segundo | NP | CAP, "Caption and speech synchronization" (mesma URL de R89) | n | direta |
| L2-R91 | P2-2.6 | O JSON grava o resultado completo em um documento; o JSON Lines grava um objeto por trecho, uma linha cada | PC | W-UT, classes WriteJSON e WriteJSONL (mesma URL de R89) | n | PARCIAL (D-ADERENCIA: só simulado diagnóstico) |
| L2-R92 | P2-2.6 | O deslocamento zero é o primeiro byte processado, e não o início da transmissão; o editor deve compensar o atraso de início | SH | CAP, "Caption and speech synchronization" (mesma URL de R89) | n | direta |
| L2-R93 | P2-2.6 | O TSV do Whisper grava início e fim em milissegundos inteiros, para evitar que o ambiente troque o ponto decimal por vírgula | AP | W-UT, docstring de WriteTSV (mesma URL de R89) | n | direta |
| L2-R94 | P2-2.6 | Nas legendas, o Amazon Transcribe usa por padrão o índice inicial 0, e não o 1, mais usado; índice inadequado pode gerar erro de compatibilidade | NP | AWS-SUB: https://docs.aws.amazon.com/transcribe/latest/dg/subtitles.html | S (baixo/médio): padrão do produto | PARCIAL (D-ADERENCIA: só simulado diagnóstico) |
| L2-R95 | P2-2.6 | Com identificação de falantes, travessões distinguem os falantes de um mesmo trecho de legenda nos dois formatos (WebVTT e SubRip) | TS | AWS-SUB (mesma URL de R94) | n | direta |
| L2-R96 | P2-2.6 | No editor de transcrição, quando não há opção de adicionar nova linha entre duas linhas, ajustam-se os horários de início e de término das linhas vizinhas (e não o texto delas) | SH | VIW, seção de inserção e remoção de linhas: https://learn.microsoft.com/en-us/azure/azure-video-indexer/edit-transcript-lines-portal | n | direta |
| L2-R97 | P2-2.6 | O formato TXT do Whisper grava só o texto de cada trecho, sem marcas de tempo | TS | W-UT, classe WriteTXT (mesma URL de R89) | n | direta |
| L2-R98 | P2-2.6 | Há editores que permitem pausar, retroceder e avançar o áudio por teclas, sem tirar as mãos do teclado | AP | README do oTranscribe: https://raw.githubusercontent.com/oTranscribe/oTranscribe/master/README.md | n | direta |
| L2-R99 | P2-2.6 | Editor que grava o texto no armazenamento local do navegador guarda o rascunho no equipamento do revisor, e não em servidor da instituição | SH | README do oTranscribe (mesma URL de R98) | S (baixo): recurso de ferramenta específica, periférico | direta |
| L2-R100 | P2-2.6 | No editor do Azure AI Video Indexer, se a mesma linha é editada várias vezes, só a última versão é usada no retreinamento do modelo de linguagem | TS | Microsoft Learn, "Customize a language model with Azure AI Video Indexer", "Customize language models by correcting transcripts": https://learn.microsoft.com/en-us/azure/azure-video-indexer/customize-language-model-how-to | S (baixo/médio): comportamento de produto | direta |
| L2-R101 | P2-2.6 | Na resposta do Speech-to-Text do Google, resultados sequenciais são porções consecutivas do áudio; as hipóteses alternativas ficam dentro de cada resultado | PC | Google Cloud, speech.recognize (REST v1), RecognizeResponse e SpeechRecognitionResult: https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/recognize | n | PARCIAL (D-ADERENCIA: só simulado diagnóstico) |
| L2-R102 | P2-2.6 | Ao gerar legendas, o Amazon Transcribe produz também o arquivo de transcrição regular, com informações adicionais às da legenda | AP | AWS-SUB (mesma URL de R94) | n | PARCIAL (D-ADERENCIA: só simulado diagnóstico) |

VOLÁTEIS novos: 7 (P2-2.5: R77, R81, R82, R85; P2-2.6: R94, R99, R100), todos de risco baixo ou baixo/médio; risco alto novo: 0. Critério aplicado: o da D-T96-ONDA2-ACEITE (II): VOLÁTIL = gabarito que depende de (a) versão, limite, preço ou modelo padrão; (b) comportamento PADRÃO de produto ou parâmetro NOMEADO; (c) existência ou disponibilidade de recurso que a documentação condiciona ou que é periférico; (d) comportamento ilustrado só em saída de exemplo. R77 (b), R81 (c, ressalva de idiomas), R82 (c, locais com suporte; mesmo tipo de base e mesmo rótulo do L1-R87), R85 (c, opção configurável de módulo periférico do Whisper, por indicação da QA R1), R94 (b), R99 (c, periférico), R100 (b). Os demais itens que nomeiam produto julgam mecanismo, sintaxe ou estrutura documentada de recurso central, ou o comportamento do código publicado, e entram só na conferência de base de janeiro, sem efeito de VOLÁTIL.

## 2. Itens já existentes por folha e contagem da folha de 20

### P2-2.5 (6 existentes + 14 novos = 20)
| id | ponto | formato | VOL |
|---|---|---|---|
| L2-Q17 | Normalização inversa converte fala em forma escrita, depois do reconhecimento | D | n |
| L2-Q18 | Normalização padroniza a forma; não corrige o conteúdo dito | D | n |
| L2-Q19 | Sem regra, a mesma sigla ou número aparece grafado de formas diferentes | SH | n |
| L2-Q20 | Expandir ou não a sigla é convenção; "sempre" e "única forma" erram | AP | n |
| L2-R09 | Mesma normalização aplicada à referência e à hipótese antes de calcular a WER | TS | n |
| L2-R10 | Regra específica antes da geral em substituições aplicadas na ordem listada | PC | n |
| L2-R75 a L2-R88 | ver tabela da seção 1 | 14 novos | 4 S |

Contagem de formatos da folha de 20 (existentes + novos): D 2 (10%); SH 5 (25%); AP 5 (25%); PC 4 (20%); TS 3 (15%); NP 1 (5%). Soma 20. Teto de 30% (6 de 20) cumprido em todos os formatos; maior ocupação: SH 5 e AP 5. D fica em 2 de 20 = 10% (legado de 33,3% diluído; nenhum D novo).
VOLÁTEIS da folha de 20: 0 existente(s) + 4 novo(s) = 4 de 20 (20%); teto de 20% (4 de 20) cumprido, sem folga. Risco alto: 0.

### P2-2.6 (6 existentes + 14 novos = 20)
| id | ponto | formato | VOL |
|---|---|---|---|
| L2-Q21 | CAT do edital é transcrição assistida, não memória de tradução | PC | n |
| L2-Q22 | Editores sincronizam texto e áudio por marcas de tempo | D | n |
| L2-Q23 | WebVTT organiza segmentos com tempo e pode indicar o falante | D | n |
| L2-R11 | Versões alternativas do trecho: o revisor escolhe a que corresponde ao áudio | SH | n |
| L2-R12 | Marcas de tempo por palavra vêm do serviço, não do revisor | TS | n |
| L2-R13 | Confiança por palavra pode orientar a conferência no editor | AP | n |
| L2-R89 a L2-R102 | ver tabela da seção 1 | 14 novos | 3 S |

Contagem de formatos da folha de 20 (existentes + novos): D 2 (10%); PC 4 (20%); SH 4 (20%); TS 4 (20%); AP 4 (20%); NP 2 (10%). Soma 20. Teto de 30% (6 de 20) cumprido em todos os formatos; maior ocupação: 4 (20%). D fica em 2 de 20 = 10% (nenhum D novo).
VOLÁTEIS da folha de 20: 0 existente(s) + 3 novo(s) = 3 de 20 (15%); teto de 20% (4 de 20) cumprido. Risco alto: 0.

## 3. Verificação de não repetição e proximidades registradas

Cada ponto foi comparado, item a item, com os 6 existentes da folha e com os outros 13 novos (nenhuma duplicata) e, pela instrução da T96_reconciliacao (seção 4), com o pacote.json v1.9 inteiro (334 itens), com os 112 itens da onda 2 (L1-R19 a L1-R131) e com as partes A e D da onda 3 (L2-R19 a L2-R46 e L2-R103 a L2-R130; a parte B não existia no momento da conferência), por busca de palavras-chave (NATO, minúsculas, abreviação, grafia, DisplayAs, sigla, ITN, vírgula, colchetes, acento, alemão, SRT, WebVTT, legenda, tick, TSV, JSON, índice, travessão, navegador, teclado, Video Indexer, resultados consecutivos, ASCII; e, para os dois itens da v2, caixa, TCU, nova linha, linhas vizinhas, lacuna, Video Indexer) e leitura dos itens achados. Nenhum gêmeo (mesmo ponto em outra folha) foi encontrado. Proximidades que a Gerência pode querer ver (todas com ponto distinto):
- 2.5, mesma página de HLT: R75, R76, R77 e R78 (4 de 14; o R88 da v1, também de HLT, foi substituído). Julgam, respectivamente, o critério de pronúncia para abreviações, o número conforme o áudio, a direção da conversão automática e a abreviação por extenso.
- R75 e R78 × L2-Q20 (2.5): Q20 julga a convenção parlamentar de expandir ou não a sigla ("sempre", "única forma"); R75 julga o critério de pronúncia (palavra × letra a letra) das diretrizes do Azure Speech; R78 julga a orientação de escrever por extenso a abreviação ("Dr."), que é abreviação e não sigla.
- R77 e R86 × L2-Q17 (2.5): Q17 julga que "vinte e cinco por cento" em "25%" é normalização inversa, depois do reconhecimento. R77 julga a direção contrária, aplicada ao texto de treinamento (números em palavras). R86 julga a abrangência da ITN (datas, horas, moedas), não a direção.
- R77 × L2-Q18 (2.5): Q18 julga que normalização padroniza a forma e não corrige o conteúdo; R77 julga quais regras o serviço aplica por conta própria.
- R80, R81 e R87 × L1-R84 (1.5) e L1-R101 (1.6): mesma página do Amazon Transcribe (tabela de vocabulário). R84 julga que DisplayAs define a forma de saída; R101 julga o hífen em entrada de várias palavras; R80 julga algarismos × extenso por coluna; R81 julga a sintaxe da sigla e do plural; R87 julga símbolos e caracteres especiais na DisplayAs. Cinco itens do pacote usam a mesma página (L1-R84, L1-R101 e, agora, R80, R81 e R87), com pontos distintos; R80, R81 e R87 são 3 de 14 em 2.5.
- R82 × L1-R87 (1.5): R87 julga em qual seção do arquivo de formato de exibição se fixa a capitalização (#rewrite × #itn); R82 julga a lógica da ITN personalizada (informa-se o formato escrito; o serviço deduz as formas faladas). Ambos VOLÁTEIS, mesma natureza de base.
- R79, R83, R84 e R85 (2.5) vêm do mesmo módulo de normalizadores do Whisper (4 de 14, 29%): R79 julga o mapeamento de grafias britânicas e americanas; R83, a remoção de vírgulas entre algarismos; R84, a remoção do texto entre colchetes e parênteses; R85, o descarte de diacríticos. São quatro comportamentos distintos. R84 e R85 são o par de menor custo de troca se a Gerência julgar concentração.
- R83, R84 e R85 × L2-R09 (2.5): R09 julga que a mesma normalização vale para referência e hipótese; R83 a R85 julgam o que cada normalizador faz com o texto. R84 × L2-Q15 (2.4): Q15 julga a uniformidade da convenção de marcar eventos não falados; R84 julga o que o normalizador de comparação faz com essas marcações.
- 2.6: R89 × L2-Q23 (WebVTT): Q23 julga que o WebVTT transporta intervalo e falante; R89 julga o separador decimal do intervalo (SRT × WebVTT).
- R90, R92, R93 × L2-R12 e L2-Q22 (2.6): R12 julga quem gera a marca de tempo (o serviço); Q22 julga a função (sincronizar); R90 julga a unidade do deslocamento; R92 julga a origem do deslocamento; R93 julga a razão de o TSV usar milissegundos inteiros. R90 e R92 vêm do mesmo parágrafo da página CAP, com pontos distintos (unidade × origem).
- R94, R95 e R102 (2.6) vêm da mesma página do Amazon Transcribe (legendas): índice inicial, travessões para falantes e arquivo de transcrição regular. Três de 14; pontos distintos.
- R97 × R91 (2.6): R97 julga que o TXT não traz marcas de tempo; R91 julga a estrutura de JSON × JSON Lines.
- R88 × L2-R10 (2.5), mesma página do Google (RecognitionConfig): R10 julga a ordem de aplicação das substituições (específica antes da geral); R88 julga a sensibilidade à caixa da busca (grafia exata). Pontos distintos. R88 × R81 (2.5): R81 julga a sintaxe da sigla no vocabulário do Amazon Transcribe; R88 julga a substituição da sigla por forma expandida na saída.
- R96 × L2-Q22 e L2-R12 (2.6): Q22 julga a função de sincronizar texto e áudio por marcas de tempo; R12 julga que as marcas por palavra vêm do serviço; R96 julga o que o revisor faz no editor quando falta espaço para uma nova linha (ajustar os horários das linhas vizinhas). R96 × R100 (2.6): páginas distintas do Azure AI Video Indexer (edição de linhas × retreinamento do modelo de linguagem); pontos distintos.
- R100 × L2-Q08 (2.2): Q08 julga que alimentar o sistema com as correções melhora o fluxo sem eliminar a revisão; R100 julga que, em edições repetidas da mesma linha, só a última versão alimenta o retreinamento. Gêmeo? Não: pontos distintos e folhas diferentes; registrado por vizinhança.
- R101 × L2-R11 (2.6), mesma página do Google: R11 julga a decisão do revisor entre versões alternativas; R101 julga o que são "resultados" (porções consecutivas) em oposição às alternativas (hipóteses do mesmo trecho). R101 × L2-R13: R13 julga a confiança por palavra, tema distinto.
- R118 (2.8, parte D) × R86 (2.5): R118 julga as classes de adaptação de modelo do Google para valores monetários e datas; R86 julga a abrangência da ITN na formatação do texto de saída do Azure Speech. R125 (2.8, parte D) × R80, R81 e R87 (2.5): R125 julga a região do vocabulário personalizado do Amazon Transcribe; R80, R81 e R87 julgam a sintaxe da tabela. R121 e R122 (2.8) não tocam 2.5 nem 2.6.
- R98 e R99 (2.6) vêm do README do oTranscribe (2 de 14). R99 × L3-Q27 e L3-Q30 (4.3): Q27 julga medidas de segurança e Q30 julga a transferência internacional; R99 julga apenas onde o rascunho fica guardado em um editor. Sem sobreposição.

## 4. Conformidade com as restrições da onda 3

- [TS] (T89, seção 3): exigência = metade dos itens da parte + 2 = 14 + 2 = 16; produzidos: 18 de 28 (14 em itens E, todos com troca de um único conceito, e 4 em itens C, estes como espelho de troca sutil, convenção admitida em T93/O-6: R81, R83, R92, R102). Por folha: 2.5, 9 de 14; 2.6, 9 de 14.
- Formato (D-REFORCO-2, regra 3): nenhum formato acima de 30% em nenhuma das duas folhas de 20 (ver seção 2); nenhum item novo usa D.
- VOLÁTIL (D-REFORCO-2, regra 4): 2.5 com 4 de 20 (20%, no teto, com o R85 marcado conforme a QA R1); 2.6 com 3 de 20 (15%); 7 novos na parte; nenhum de risco alto.
- Aderência (D-ADERENCIA): 21 direta e 7 PARCIAL (R79, R84, R85, R91, R94, R101, R102), estes só para simulado diagnóstico.
- Gabarito da parte (D-REFORCO-2, regra 5): 14 C / 14 E em 28 (50% de C; faixa de 40% a 60%, isto é, de 11 a 17 C, cumprida); por folha, 7 C / 7 E.
- Estilo (T93, O-1 a O-8; estilo_onda_2, recomendações): O-1, extensão: C com média de 50,1 palavras e E com 48,6 (E de 42 a 62, com cinco acima de 50), nenhum C acima de 65 (maior: 62); O-2, "independentemente" em C (R92) e em E (R85); O-3, "pode" também em E (R85); O-4, nenhum item cita norma, e a ambientação parlamentar fica fora do escopo de "Segundo a documentação…"; O-5, nenhuma cauda falsa autocontraditória nem absolutos empilhados num E; O-6, [TS] em 4 itens C como espelho; O-7, restritivos e causais distribuídos em C e E; O-8, "ainda que" em C (R76) e em E (R84); abertura "Segundo a…" em número reduzido e variada; fonte nomeada sempre que o item usa "a orientação" ou "a documentação".
- Base por item: 28 de 28 com documentação oficial do fornecedor ou arquivo do repositório oficial do fornecedor, URL e "verificado em 18/10/2026" (abertos hoje). As citações literais foram conferidas por script contra o texto das páginas e dos arquivos baixados hoje; os gabaritos dos normalizadores do Whisper (R79, R83, R84, R85) decorrem do texto do repositório (docstring, comentário, expressão regular, assinatura; SHA-256 na tabela de proveniência); a execução de teste feita hoje é corroboração de registro, e não base.

FIM DA PARTE 1/3

=====================================================================
PARTE 2/3 — (d) ITENS DO ESTUDANTE
=====================================================================

L2-R75. Julgue o item.
Segundo a documentação do Azure Speech sobre transcrições rotuladas por pessoas (orientação para o inglês dos Estados Unidos), a abreviação pronunciada como uma palavra, a exemplo de NATO, deve ser escrita com as letras separadas por espaço, ao passo que a abreviação pronunciada letra a letra deve ser mantida como está.

L2-R76. Julgue o item.
Uma equipe prepara, para treinar um modelo no Azure Speech, transcrições rotuladas por pessoas do áudio de uma audiência pública conduzida em inglês. Um orador diz “one oh one” ao citar o número 101. Segundo a documentação para o inglês dos Estados Unidos, o número deve ser transcrito por extenso como foi pronunciado, ainda que o revisor considere mais usual outra leitura.

L2-R77. Julgue o item.
Entre as regras de normalização que o Azure Speech aplica automaticamente às transcrições rotuladas enviadas para treinamento, segundo a documentação, estão a conversão das letras para minúsculas, a remoção da pontuação, exceto apóstrofos no interior de palavras, e a conversão dos números escritos por extenso em algarismos.

L2-R78. Julgue o item.
Uma equipe da Casa prepara, para treinar um modelo no Azure Speech, transcrições rotuladas por pessoas de uma audiência pública conduzida em inglês. Pela orientação da Microsoft para o inglês dos Estados Unidos, a abreviação “Dr.” deve ser escrita por extenso, de modo que “Dr. Bruce Banner” conste como “Doctor Bruce Banner”.

L2-R79. Julgue o item.
Uma equipe vai comparar duas transcrições em inglês que diferem apenas por grafias como “colour” e “color”. Nessa situação, o normalizador de grafia que o Whisper oferece para o inglês, por aplicar mapeamentos entre grafias britânicas e americanas, permite tratar as duas formas como a mesma palavra.

L2-R80. Julgue o item.
Na tabela de vocabulário personalizado do Amazon Transcribe, os números podem ser escritos em algarismos na coluna Phrase, na qual se registra a entrada, ao passo que a coluna DisplayAs, que define a forma exibida na saída, exige que os números sejam escritos por extenso.

L2-R81. Julgue o item.
Uma equipe pretende cadastrar no vocabulário personalizado do Amazon Transcribe a sigla CPI, pronunciada letra a letra, e também o seu plural. Segundo a documentação do serviço, a entrada do plural na coluna Phrase deve ser escrita C.P.I.-s, com as letras separadas por pontos e o s ligado à sigla por hífen.

L2-R82. Julgue o item.
Uma equipe quer que o Azure Speech escreva sempre em um mesmo formato um código alfanumérico, como “JO:500”, usado como exemplo na documentação. Nessa situação, na regra de ITN personalizada, a equipe informa o formato escrito desejado, e o serviço deduz as maneiras pelas quais o código pode ser falado.

L2-R83. Julgue o item.
Uma equipe compara a transcrição de uma sessão de comissão, em português do Brasil, com a de referência, aplicando sem adaptação o normalizador de texto do Whisper para o inglês, que remove as vírgulas entre algarismos. Como no Brasil a vírgula separa a parte decimal, “3,5” seria convertido em “35”, o que distorceria a comparação de valores.

L2-R84. Julgue o item.
Ao preparar a comparação entre a transcrição automática e a de referência de uma sessão, o normalizador básico de texto do Whisper mantém no texto as marcações entre colchetes ou parênteses, ainda que se refiram a eventos não falados, como [aplausos] e (risos).

L2-R85. Julgue o item.
Na avaliação da transcrição de reunião de comissão, o normalizador básico de texto do Whisper pode ser configurado para descartar os diacríticos antes da comparação com a transcrição de referência. Com essa configuração, independentemente de a diferença entre os textos estar apenas no acento, “sessão” e “sessao” continuam a ser tratadas como palavras distintas.

L2-R86. Julgue o item.
A normalização inversa de texto (ITN) do Azure Speech, que converte formas verbalizadas em suas formas escritas simbólicas, restringe-se, segundo a documentação sobre a formatação do texto de exibição, à conversão de números ditos por extenso em algarismos, sem alcançar datas, horas, valores monetários ou endereços.

L2-R87. Julgue o item.
Segundo a documentação do Amazon Transcribe, na tabela de vocabulário personalizado, os símbolos e caracteres especiais de um termo técnico, como o “++” de “C++”, são admitidos na coluna DisplayAs, que define a forma pela qual a entrada aparece na saída da transcrição.

L2-R88. Julgue o item.
Uma equipe configura, no Speech-to-Text do Google, uma entrada de normalização de transcrição que troca a sigla TCU por Tribunal de Contas da União, com a busca sensível a maiúsculas e minúsculas. Em uma transcrição de reunião de comissão na qual o reconhecedor grafou o termo duas vezes como “TCU” e uma vez como “Tcu”, a entrada é aplicada às três ocorrências.

L2-R89. Julgue o item.
Um revisor importa em um editor de transcrição arquivos de legenda gerados pelo Azure Speech. Segundo a documentação do serviço, o intervalo de tempo do formato SRT usa ponto entre os segundos e os milésimos (hh:mm:ss.fff), ao passo que o do formato WebVTT usa vírgula (hh:mm:ss,fff).

L2-R90. Julgue o item.
Um editor de transcrição recebe do Azure Speech o deslocamento (offset) de um trecho reconhecido, medido em ticks, em que um tick equivale a cem nanossegundos. Nessa situação, o deslocamento de 12.500.000 ticks indica que o trecho começa 1,25 segundo depois do início do áudio processado.

L2-R91. Julgue o item.
Ao exportar do Whisper a transcrição de uma sessão para ser aberta em um editor de transcrição, o formato JSON grava o resultado completo em um único documento, ao passo que o formato JSON Lines grava cada trecho como um objeto JSON em uma linha própria.

L2-R92. Julgue o item.
Considere que o reconhecimento em tempo real de uma sessão de comissão pelo Azure Speech tenha começado dez minutos depois do início da transmissão. Segundo a documentação do serviço, o deslocamento zero corresponde ao primeiro byte de áudio processado, independentemente do início da transmissão; assim, para alinhar o texto ao vídeo integral, o editor de transcrição deve considerar esses dez minutos.

L2-R93. Julgue o item.
Em um editor de transcrição usado na revisão das sessões, cuja configuração regional do português do Brasil adota a vírgula como separador decimal, o formato tabular (TSV) de saída do Whisper, por registrar o início e o fim de cada trecho em segundos com casas decimais, fica sujeito a erro de leitura.

L2-R94. Julgue o item.
Ao gerar legendas para um editor de transcrição, o Amazon Transcribe usa, por padrão, o índice inicial 0 na numeração dos trechos, e não o 1, mais utilizado; segundo a documentação, índice inadequado pode causar erros de compatibilidade, e por isso a equipe deve verificar o índice exigido antes de criar os arquivos.

L2-R95. Julgue o item.
Ao gerar legendas com a identificação de falantes habilitada, o Amazon Transcribe distingue por travessões os falantes que aparecem em um mesmo trecho de legenda, o que vale somente para o formato SubRip, e não para o WebVTT, também gerado pelo serviço.

L2-R96. Julgue o item.
Considere que um revisor trabalhe, no modo de edição do editor de transcrição do Azure AI Video Indexer, em uma audiência pública e não encontre a opção de adicionar uma nova linha entre duas linhas consecutivas. Segundo a documentação do serviço, ele pode abrir espaço para a nova linha ajustando o texto das linhas vizinhas.

L2-R97. Julgue o item.
O formato de texto simples (TXT) gravado pelo Whisper conserva, para cada trecho transcrito, as marcas de tempo de início e fim, o que permite ao revisor sincronizar o texto com o áudio em um editor de transcrição, tal como ocorre com os formatos de legenda e o tabular.

L2-R98. Julgue o item.
Para agilizar a revisão de transcrições de reuniões de comissão, há editores de transcrição que permitem pausar, retroceder e avançar a reprodução do áudio por teclas, de modo que o revisor não precisa tirar as mãos do teclado para controlar o áudio.

L2-R99. Julgue o item.
Um revisor trabalha em um editor de transcrição que grava o texto automaticamente no armazenamento local do navegador (localStorage). Nessa situação, o rascunho fica guardado no navegador do equipamento utilizado, e não, por meio desse recurso, em servidor da instituição.

L2-R100. Julgue o item.
No editor de transcrição do Azure AI Video Indexer, as linhas corrigidas pelos revisores são reunidas em um arquivo usado para retreinar o modelo de linguagem. Se o revisor edita várias vezes a mesma linha, todas as versões sucessivas dessa linha são usadas no retreinamento.

L2-R101. Julgue o item.
A lista de resultados sequenciais que um editor de transcrição recebe do Speech-to-Text do Google, ao final do reconhecimento de um arquivo de áudio, corresponde, segundo a documentação do serviço, a hipóteses alternativas para o áudio inteiro, e não a porções consecutivas do áudio.

L2-R102. Julgue o item.
Para revisar a transcrição de uma sessão gravada em vídeo, a equipe solicita ao Amazon Transcribe a geração de legendas nos formatos SRT e WebVTT. Nessa situação, o serviço produz também o arquivo de transcrição regular, que contém informações adicionais às dos arquivos de legenda, às quais o revisor pode recorrer.

FIM DA PARTE 2/3

=====================================================================
PARTE 3/3 — (d-G) GABARITO COMENTADO
=====================================================================
Legenda: [TS] = troca sutil de um único conceito (nos itens C, "espelho": item construído como a negação de uma troca sutil). VOLÁTIL = depende de produto, versão ou comportamento padrão (critério da D-T96-ONDA2-ACEITE, II). REVERIFICAR = reabrir a fonte na reverificação de 4–8/1/2027 (T-11, parte P2). Páginas e arquivos abertos em 18/10/2026. "SHA-256" = hash do arquivo do repositório lido hoje, para a conferência de janeiro detectar qualquer alteração.

L2-R75. E [TS]. A documentação manda não editar a abreviação pronunciada como palavra (NATO, RAM) e escrever com as letras separadas por espaço a pronunciada letra a letra; o item inverte os dois tratamentos. O critério é o modo de pronúncia no áudio, e não o fato de a forma ser uma abreviação.
Base: Microsoft, Azure Speech, How to create human-labeled transcriptions, seção "Text normalization for US English" (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-human-labeled-transcriptions), verificado em 18/10/2026: “Abbreviations that are pronounced as words shouldn't be edited”; “Write out abbreviations that are pronounced as separate letters with each letter separated by a space.”.
Formato: PC (par confundível). Aderência: direta.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R76. C. Para o conjunto de treinamento, o número registrado deve corresponder ao áudio: 101 pode ser dito de mais de uma forma, e a transcrição segue a forma dita. O enunciado usa o exemplo da própria documentação ("one oh one"), em audiência conduzida em inglês, escopo em que vale a orientação para o inglês dos Estados Unidos.
Base: Microsoft, Azure Speech, How to create human-labeled transcriptions, seção "Text normalization for US English" (mesma URL de R75), verificado em 18/10/2026: “If you use audio, transcribe numbers as words that match the audio”; exemplo: “"101" could be pronounced as "one oh one" or "one hundred and one"”.
Formato: SH (situação hipotética). Aderência: direta.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R77. E [TS]. VOLÁTIL (baixo/médio). A documentação lista, entre as regras automáticas, expandir números em palavras (forma falada), e não convertê-los em algarismos; o item troca o sentido da conversão (normalização × normalização inversa). Regra automática do serviço = comportamento padrão de produto (hipótese (b) da D-T96-ONDA2-ACEITE).
Base: Microsoft, Azure Speech, How to create human-labeled transcriptions (mesma URL de R75), verificado em 18/10/2026: “The following normalization rules are automatically applied to transcriptions:”; “Use lowercase letters.”; “Remove all punctuation except apostrophes within words.”; “Expand numbers into words/spoken form, such as dollar amounts.”.
Formato: PC (par confundível). Aderência: direta.
REVERIFICAR: VOLÁTIL (baixo/médio); conferência de base em 4–8/1/2027 (inapto a simulado final até lá).

L2-R78. C. A documentação recomenda escrever as abreviações por extenso, e o exemplo da tabela é "Dr. Bruce Banner" que passa a "Doctor Bruce Banner". A recomendação vale para a preparação de transcrições de treinamento em inglês dos Estados Unidos, escopo que o item declara.
Base: Microsoft, Azure Speech, How to create human-labeled transcriptions (mesma URL de R75), verificado em 18/10/2026: “Write out abbreviations in words.”; tabela de exemplos: “Dr. Bruce Banner” → “Doctor Bruce Banner”.
Formato: AP (aplicação parlamentar). Aderência: direta.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R79. C. O normalizador de grafia do Whisper para o inglês aplica mapeamentos entre grafias britânicas e americanas; no arquivo de mapeamento, "colour" corresponde a "color". Assim, duas transcrições que diferem só por essa variante passam a ser tratadas como iguais.
Base: OpenAI, repositório oficial openai/whisper, whisper/normalizers/english.py (https://raw.githubusercontent.com/openai/whisper/main/whisper/normalizers/english.py; SHA-256 d31a52685b5b42628ea4e3343c3a7925ce5b2f317e6c0ec4575677dd5c8b5d2c), docstring de EnglishSpellingNormalizer: “Applies British-American spelling mappings as listed in [1].”; whisper/normalizers/english.json (SHA-256 6607f948be9824d2e1b2fa2223cd94c06c45afa4e05ea0e3d5e1f2bdffde2465): “"colour": "color"”. Verificado em 18/10/2026. Nota de registro: este item não usa o docstring de EnglishNumberNormalizer como base (ver dúvida 3).
Formato: SH (situação hipotética). Aderência: PARCIAL (D-ADERENCIA: só simulado diagnóstico).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R80. E [TS]. Na tabela de vocabulário, a coluna Phrase não admite algarismos (os números devem ser escritos por extenso), e os algarismos só são admitidos na coluna DisplayAs; o item inverte as colunas. O exemplo da documentação é "VX02Q", que na Phrase é V.X.-zero-two-Q. e na DisplayAs, VX02Q.
Base: AWS, Amazon Transcribe, Creating a custom vocabulary using a table (https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-table.html), verificado em 18/10/2026: “Digits ( 0-9 ) are only supported in the DisplayAs column.”; “If you want to include numbers in the Phrase column, you must spell them out.”.
Formato: PC (par confundível). Aderência: direta.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R81. C [TS]. VOLÁTIL (baixo/médio). A documentação manda separar por pontos as letras pronunciadas da sigla (A.B.C.) e ligar por hífen o s do plural (A.B.C.-s); o item é o espelho da troca sutil "C.P.I.s" ou "CPI-s", que seria incorreta. VOLÁTIL pela hipótese (c): a própria página ressalva que siglas não são suportadas em todos os idiomas; o item não afirma suporte a nenhum idioma.
Base: AWS, Amazon Transcribe, Creating a custom vocabulary using a table (mesma URL de R80), verificado em 18/10/2026: “Enter acronyms, or other words whose letters should be pronounced individually, as single letters separated by periods ( A.B.C. ).”; “To enter the plural form of an acronym, such as 'ABCs', separate the 's' from the acronym with a hyphen ( A.B.C.-s )”; “Acronyms are not supported in all languages”.
Formato: SH (situação hipotética). Aderência: direta.
REVERIFICAR: VOLÁTIL (baixo/médio); conferência de base em 4–8/1/2027 (inapto a simulado final até lá).

L2-R82. C. VOLÁTIL (baixo/médio). Na ITN personalizada o usuário especifica a saída que deseja ver, e o serviço deduz como as palavras podem ser faladas (o código JO:500 pode ser dito "J O" ou "joe", "five hundred" ou "five oh oh"). VOLÁTIL pela hipótese (c): recurso de custom speech que a página condiciona a locais com suporte (pt-BR consta da lista da página), mesma natureza de base do L1-R87.
Base: Microsoft, Azure Speech, How to prepare display text format training data for custom speech, seção "Custom ITN" (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-display-text-format), verificado em 18/10/2026: “The philosophy of pattern-based custom ITN is that you can specify the final output that you want to see. The Speech service figures out how the words might be spoken and map the predicted spoken expressions to the specified output format.”.
Formato: SH (situação hipotética). Aderência: direta.
REVERIFICAR: VOLÁTIL (baixo/médio); conferência de base em 4–8/1/2027 (inapto a simulado final até lá).

L2-R83. C [TS]. O normalizador de texto do Whisper para o inglês remove vírgulas entre algarismos (comentário e expressão regular do código); aplicado a "3,5" sem adaptação, o resultado é "35", porque a remoção ocorre antes da padronização dos números. O item não afirma que o Whisper é inadequado ao português, e sim que esse normalizador, sem adaptação, distorce valores decimais escritos com vírgula; é o espelho da troca "o normalizador do inglês serve ao português sem adaptação".
Base: OpenAI, repositório oficial openai/whisper, whisper/normalizers/english.py (mesma URL e SHA-256 de R79), classe EnglishTextNormalizer, comentário do código: “# remove commas between digits”, verificado em 18/10/2026.
Formato: AP (aplicação parlamentar; moldura: transcrição de uma sessão de comissão). Aderência: direta.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R84. E [TS]. O normalizador básico remove o texto entre colchetes e entre parênteses (comentários e expressão regular do código), como em "[aplausos]" e "(risos)". O item troca "remove" por "mantém".
Base: OpenAI, repositório oficial openai/whisper, whisper/normalizers/basic.py (https://raw.githubusercontent.com/openai/whisper/main/whisper/normalizers/basic.py; SHA-256 4742eaa040e0657fa1247a1361e0d856c62317a43326ea59a40c2e9edd8d2c38), classe BasicTextNormalizer, comentários do código: “# remove words between brackets”; “# remove words between parenthesis”, verificado em 18/10/2026.
Formato: AP (aplicação parlamentar). Aderência: PARCIAL (D-ADERENCIA: só simulado diagnóstico).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R85. E [TS]. VOLÁTIL (baixo). Com a opção de descartar diacríticos, a docstring prevê que os diacríticos são descartados, de modo que "sessão" e "sessao" ficam idênticas; sem a opção (padrão desligado), mantêm-se distintas. O item afirma que continuam distintas com o descarte. VOLÁTIL pela hipótese (c) da D-T96-ONDA2-ACEITE: o gabarito depende de opção configurável de módulo periférico do Whisper (normalizador de avaliação).
Base: OpenAI, repositório oficial openai/whisper, whisper/normalizers/basic.py (mesma URL e SHA-256 de R84), função remove_symbols_and_diacritics, docstring: “Replace any other markers, symbols, and punctuations with a space, and drop any diacritics (category 'Mn' and some manual mappings)”; assinatura: “remove_diacritics: bool = False”, verificado em 18/10/2026.
Formato: AP (aplicação parlamentar; moldura: transcrição de reunião de comissão). Aderência: PARCIAL (D-ADERENCIA: só simulado diagnóstico).
REVERIFICAR: VOLÁTIL (baixo); conferência de base em 4–8/1/2027 (inapto a simulado final até lá).

L2-R86. E [TS]. A documentação define a ITN como a conversão de formas verbalizadas em formas escritas simbólicas e lista, entre os formatos suportados, datas, horas, decimais, moedas, endereços, e-mails e telefones; o item restringe a ITN a números. A lista é exemplificativa ("Some of the supported text formats include"), o que sustenta o gabarito E.
Base: Microsoft, Azure Speech, Display text formatting with speech to text, seção "Inverse Text Normalization" (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/display-text-format), verificado em 18/10/2026: “Inverse Text Normalization (ITN) is a process that converts verbalized forms into their corresponding symbolic written forms.”; “Some of the supported text formats include dates, times, decimals, currencies, addresses, emails, and phone numbers.”.
Formato: TS (troca de sujeito). Aderência: direta.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R87. C. A documentação informa que a coluna DisplayAs admite símbolos e caracteres especiais (exemplo: C++), enquanto as demais colunas seguem o conjunto de caracteres do idioma. O E correspondente restringiria os símbolos à coluna Phrase.
Base: AWS, Amazon Transcribe, Creating a custom vocabulary using a table (mesma URL de R80), verificado em 18/10/2026: “The DisplayAs column supports symbols and special characters (for example, C++).”.
Formato: TS (troca de sujeito). Aderência: direta.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R88. E [TS]. A normalização de transcrição do Google troca trechos do texto por frases escolhidas pelo usuário, e cada entrada informa se a busca distingue maiúsculas de minúsculas. Com a busca sensível à caixa, "Tcu" não corresponde a "TCU": só as duas ocorrências com a grafia exata são trocadas, e não as três. O item troca "duas" por "três", isto é, ignora a sensibilidade à caixa que o próprio enunciado fixa. Não VOLÁTIL: a sensibilidade à caixa é premissa declarada no enunciado, que não nomeia campo, limite nem padrão (mesmo tipo de base do L2-R10, aceito como não VOLÁTIL).
Base: Google Cloud, Speech-to-Text, RecognitionConfig (REST v1), campo transcriptNormalization e objeto Entry (https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig; página com "Last updated 2025-10-23 UTC"), verificado em 18/10/2026: “Use transcription normalization to automatically replace parts of the transcript with phrases of your choosing.”; “A single replacement configuration.”; “Whether the search is case sensitive.”.
Formato: NP (número ou prazo): o julgamento decide por contagem de ocorrências (2 de 3). Aderência: direta (2.5: substituição de sigla por forma expandida no texto transcrito).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R89. E [TS]. O intervalo de tempo do SRT é hh:mm:ss,fff (vírgula), e o do WebVTT é hh:mm:ss.fff (ponto); o item troca os separadores. O código do Whisper confirma: marcador decimal "," no escritor de SRT e "." no de WebVTT.
Base: Microsoft, Azure Speech, Captioning with speech to text, seção "Caption output format" (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/captioning-concepts), verificado em 18/10/2026: “The SRT (SubRip Text) timespan output format is hh:mm:ss,fff”; “The WebVTT (Web Video Text Tracks) timespan output format is hh:mm:ss.fff”; OpenAI, repositório oficial openai/whisper, whisper/utils.py (https://raw.githubusercontent.com/openai/whisper/main/whisper/utils.py; SHA-256 f46aa555363ab42a455cd7c7f8c108dc2f69c5a94c6354c73ae96d671d9b1c37): classe WriteSRT, “decimal_marker: str = ","”, e classe WriteVTT, “decimal_marker: str = "."”.
Formato: PC (par confundível). Aderência: direta.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R90. C. Um tick equivale a 100 nanossegundos, isto é, a um décimo de milionésimo de segundo; 12.500.000 ticks ÷ 10.000.000 ticks por segundo = 1,25 s (conta conferida por script). O deslocamento é contado a partir do primeiro byte de áudio processado.
Base: Microsoft, Azure Speech, Captioning with speech to text, seção "Caption and speech synchronization" (mesma URL de R89), verificado em 18/10/2026: “One tick represents one hundred nanoseconds or one ten-millionth of a second.”; “starting from 0 (zero) tick, associated with the first audio byte processed by the SDK”.
Formato: NP (número ou prazo). Aderência: direta.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R91. C. No Whisper, o escritor JSON grava o resultado inteiro de uma só vez (json.dump), e o escritor JSON Lines grava um objeto JSON por trecho, cada um em uma linha. Um editor pode, assim, ler o segundo formato trecho a trecho.
Base: OpenAI, repositório oficial openai/whisper, whisper/utils.py (mesma URL e SHA-256 de R89), classes WriteJSON (“json.dump(result, file)”) e WriteJSONL (“print(json.dumps(segment), file=file, flush=True)”, dentro do laço “for segment in result["segments"]:”), verificado em 18/10/2026.
Formato: PC (par confundível). Aderência: PARCIAL (D-ADERENCIA: só simulado diagnóstico).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R92. C [TS]. O deslocamento começa em zero no primeiro byte processado, isto é, quando o reconhecimento começa; com início dez minutos depois da transmissão, a marca zero não coincide com o início do vídeo, e a soma dos dez minutos é consequência aritmética. O item é o espelho da troca "o deslocamento é contado desde o início da transmissão".
Base: Microsoft, Azure Speech, Captioning with speech to text, seção "Caption and speech synchronization" (mesma URL de R89), verificado em 18/10/2026: “the offset begins when you start recognition, since that's when the SDK starts processing the audio stream”.
Formato: SH (situação hipotética). Aderência: direta.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R93. E [TS]. O TSV do Whisper registra início e fim em milissegundos inteiros, justamente para evitar que a configuração do ambiente troque o ponto decimal por vírgula; o item afirma que usa segundos com casas decimais. A referência ao português do Brasil é aplicação (a vírgula é o separador decimal no Brasil), e não frase da documentação.
Base: OpenAI, repositório oficial openai/whisper, whisper/utils.py (mesma URL e SHA-256 de R89), docstring de WriteTSV, verificado em 18/10/2026: “<start time in integer milliseconds>”; “Using integer milliseconds as start and end times means there's no chance of interference from an environment setting a language encoding that causes the decimal in a floating point number to appear as a comma”.
Formato: AP (aplicação parlamentar). Aderência: direta.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R94. C. VOLÁTIL (baixo/médio). A documentação informa o índice inicial padrão 0 do serviço, diferente do 1, mais usado, e adverte para erros de compatibilidade; recomenda verificar o índice exigido antes de criar as legendas. VOLÁTIL pela hipótese (b): padrão do produto; o item não nomeia o parâmetro que altera o índice.
Base: AWS, Amazon Transcribe, Generating subtitle files (https://docs.aws.amazon.com/transcribe/latest/dg/subtitles.html), verificado em 18/10/2026: “Amazon Transcribe uses a default start index of 0 for subtitle output, which differs from the more widely used value of 1”; “Using the incorrect start index can result in compatibility errors with other services”.
Formato: NP (número ou prazo). Aderência: PARCIAL (D-ADERENCIA: só simulado diagnóstico).
REVERIFICAR: VOLÁTIL (baixo/médio); conferência de base em 4–8/1/2027 (inapto a simulado final até lá).

L2-R95. E [TS]. Com a identificação de falantes, os travessões distinguem os falantes de um mesmo trecho de legenda nos dois formatos (WebVTT e SubRip); o item restringe a regra ao SubRip.
Base: AWS, Amazon Transcribe, Generating subtitle files (mesma URL de R94), verificado em 18/10/2026: “If there are multiple speakers in a given subtitle segment, dashes are used to distinguish each speaker. This applies to both WebVTT and SubRip formats”.
Formato: TS (troca de sujeito). Aderência: direta.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R96. E [TS]. A documentação manda, quando falta a opção de adicionar nova linha entre duas linhas (porque não há intervalo entre o fim de uma e o início da seguinte), ajustar os horários de início e de término das linhas vizinhas para que a nova linha caiba onde se deseja; o item troca horário por texto. O espaço de uma nova linha é um intervalo de tempo na linha do tempo do editor. Não VOLÁTIL: mecanismo documentado de função do editor, sem versão, limite, padrão ou parâmetro nomeado.
Base: Microsoft, Azure AI Video Indexer, View and update transcriptions in Azure AI Video Indexer website, seção "Insert or remove transcript lines in the Azure AI Video Indexer website" (https://learn.microsoft.com/en-us/azure/azure-video-indexer/edit-transcript-lines-portal; "Last updated on 2025-10-06"), verificado em 18/10/2026: “While in the edit mode, hover between two transcription lines. There's a gap between ending time of the transcript line and the beginning of the following transcript line. The add new transcription line option is visible.”; “If there isn’t an option to add a new line, you can adjust the end/start time of the relevant transcript lines to fit a new line in your desired place.”.
Formato: SH (situação hipotética). Aderência: direta (função de editor de transcrição: inserir linha e ajustar horários).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R97. E [TS]. O escritor TXT do Whisper imprime apenas o texto de cada trecho, sem marcas de tempo; as marcas de tempo constam dos formatos SRT, WebVTT, TSV e JSON. O item atribui ao TXT o que é dos outros formatos.
Base: OpenAI, repositório oficial openai/whisper, whisper/utils.py (mesma URL e SHA-256 de R89), classe WriteTXT: “print(segment["text"].strip(), file=file, flush=True)”, verificado em 18/10/2026.
Formato: TS (troca de sujeito). Aderência: direta.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R98. C. O README de um editor de transcrição de código aberto lista pausar, retroceder e avançar o áudio por teclas, sem tirar as mãos do teclado. O item generaliza em forma existencial ("há editores") e não nomeia produto.
Base: oTranscribe, repositório oficial oTranscribe/oTranscribe, README.md (https://raw.githubusercontent.com/oTranscribe/oTranscribe/master/README.md; SHA-256 8089e13664b683c5b4b397e08cc6a8da6d67a2da2fb22c24995d9fb639954125), verificado em 18/10/2026: “Pause (ESC), rewind (F1) and fast-forward (F2) without taking your hands off the keyboard”.
Formato: AP (aplicação parlamentar). Aderência: direta.
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R99. C. VOLÁTIL (baixo). O README informa que o texto é salvo automaticamente no localStorage do navegador, que é armazenamento do navegador do equipamento e não de servidor; a segunda parte do enunciado é consequência desse armazenamento. VOLÁTIL pela hipótese (c): recurso de uma ferramenta específica, periférico ao tema.
Base: oTranscribe, README.md (mesma URL e SHA-256 de R98), verificado em 18/10/2026: “Your transcript is automatically saved to the browser's `localStorage` every second”.
Formato: SH (situação hipotética). Aderência: direta.
REVERIFICAR: VOLÁTIL (baixo); conferência de base em 4–8/1/2027 (inapto a simulado final até lá).

L2-R100. E [TS]. VOLÁTIL (baixo/médio). A documentação diz que, nas várias edições da mesma linha, só a última versão é usada para atualizar o modelo de linguagem; o item afirma que todas as versões sucessivas são usadas. VOLÁTIL pela hipótese (b): comportamento de produto, em página compartilhada por duas ofertas do serviço.
Base: Microsoft, Azure AI Video Indexer, Customize a language model with Azure AI Video Indexer, seção "Customize language models by correcting transcripts" (https://learn.microsoft.com/en-us/azure/azure-video-indexer/customize-language-model-how-to), verificado em 18/10/2026: “It captures all lines that you corrected in the transcription of your video and adds them to a text file called From transcript edits.”; “If you make multiple edits to the same line, Azure AI Video Indexer uses only the last version of the corrected line for updating the language model.”.
Formato: TS (troca de sujeito). Aderência: direta.
REVERIFICAR: VOLÁTIL (baixo/médio); conferência de base em 4–8/1/2027 (inapto a simulado final até lá).

L2-R101. E [TS]. Segundo a referência da API, a lista de resultados é sequencial e corresponde a porções sequenciais do áudio; as hipóteses alternativas ficam no campo de alternativas de cada resultado. O item troca resultados por hipóteses alternativas do áudio inteiro.
Base: Google Cloud, Speech-to-Text, speech.recognize (REST v1) (https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/recognize; "Last updated 2025-10-23 UTC"), verificado em 18/10/2026: “Sequential list of transcription results corresponding to sequential portions of audio.”; “A speech recognition result corresponding to a portion of the audio.”; “May contain one or more recognition hypotheses”.
Formato: PC (par confundível). Aderência: PARCIAL (D-ADERENCIA: só simulado diagnóstico).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L2-R102. C [TS]. Com legendas, o serviço produz também o arquivo de transcrição regular, que contém informações adicionais; o revisor pode recorrer a ele quando a legenda não bastar. O item é o espelho da troca "a legenda contém todas as informações e o serviço não gera outro arquivo".
Base: AWS, Amazon Transcribe, Generating subtitle files (mesma URL de R94), verificado em 18/10/2026: “When using the subtitle feature, your selected subtitle file(s) and a regular transcript file (containing additional information) are produced.”.
Formato: AP (aplicação parlamentar). Aderência: PARCIAL (D-ADERENCIA: só simulado diagnóstico).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

## Contagens
| quesito | valor |
|---|---|
| total | 28 (P2-2.5: 14, de L2-R75 a L2-R88; P2-2.6: 14, de L2-R89 a L2-R102) |
| P2-2.5 | 7 C (R76, R78, R79, R81, R82, R83, R87) / 7 E (R75, R77, R80, R84, R85, R86, R88) |
| P2-2.6 | 7 C (R90, R91, R92, R94, R98, R99, R102) / 7 E (R89, R93, R95, R96, R97, R100, R101) |
| C / E da parte | 14 C / 14 E (50% de C; faixa 11 a 17 C cumprida) |
| [TS] | 18 de 28 (exigência: 16): 14 em itens E (R75, R77, R80, R84, R85, R86, R88, R89, R93, R95, R96, R97, R100, R101) e 4 em itens C, como espelho (R81, R83, R92, R102) |
| [TS] por folha | P2-2.5: 9 de 14; P2-2.6: 9 de 14 |
| VOLÁTIL novos | 7 (R77, R81, R82, R85 em 2.5; R94, R99, R100 em 2.6); risco alto: 0 |
| VOLÁTEIS da folha de 20 | P2-2.5: 4 de 20 (20%, no teto); P2-2.6: 3 de 20 (15%) |
| formatos de P2-2.5 (20) | D 2; SH 5; AP 5; PC 4; TS 3; NP 1 |
| formatos de P2-2.6 (20) | D 2; PC 4; SH 4; TS 4; AP 4; NP 2 |
| formatos dos 28 novos | PC 6; SH 7; AP 7; TS 5; NP 3; D 0 |
| extensão (palavras do enunciado) | C: média 50,1, mediana 50,5, de 40 a 62; E: média 48,6, mediana 46,5, de 42 a 62 (diferença de 1,5 palavra; na onda 1 era de 9,2 e na onda 2, de 0,1); nenhum C acima de 65 palavras |
| aritmética conferida por script | R90: 12.500.000 ÷ 10.000.000 = 1,25 s. Corroboração de registro, não base: a execução do código do Whisper em 18/10/2026 coincidiu com a leitura do texto do repositório em R79, R83, R84 e R85 |
| aderência | 21 direta; 7 PARCIAL (R79, R84, R85, R91, R94, R101, R102: só simulado diagnóstico); ver dúvida 1 |

## Lista de REVERIFICAR de janeiro (4–8/1/2027; T-11, parte P2, gce-cqfp)
- VOLÁTEIS (inaptos a simulado final até a reverificação): R77, R81, R82, R85, R94, R99, R100.
- Conferência de base, sem efeito de VOLÁTIL: R75, R76, R78, R79, R80, R83, R84, R86, R87, R88, R89, R90, R91, R92, R93, R95, R96, R97, R98, R101, R102 (em R88 e R96, reabrir as URLs do Google, RecognitionConfig, e do Azure AI Video Indexer, "View and update transcriptions"). Para os itens apoiados em arquivos do repositório do Whisper (R79, R83, R84, R85, R89, R91, R93, R97) e do oTranscribe (R98, R99): comparar o SHA-256 registrado e, se mudou, reabrir o trecho; em R83 a R85, repetir a execução de teste.

## Tabela de proveniência (todas as páginas e arquivos abertos e lidos em 18/10/2026)
| fonte | URL oficial | data da página / verificação | usada em |
|---|---|---|---|
| Microsoft, Azure Speech, How to create human-labeled transcriptions | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-human-labeled-transcriptions | Last updated on 2025-12-29; verificado em 18/10/2026 | R75, R76, R77, R78 |
| Microsoft, Azure Speech, Display text formatting with speech to text | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/display-text-format | Last updated on 2025-12-29; verificado em 18/10/2026 | R86 |
| Microsoft, Azure Speech, How to prepare display text format training data for custom speech | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-display-text-format | Last updated on 2026-01-30; verificado em 18/10/2026 | R82 |
| Microsoft, Azure Speech, Captioning with speech to text | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/captioning-concepts | Last updated on 2026-02-25; verificado em 18/10/2026 | R89, R90, R92 |
| Microsoft, Azure AI Video Indexer, View and update transcriptions in Azure AI Video Indexer website | https://learn.microsoft.com/en-us/azure/azure-video-indexer/edit-transcript-lines-portal | Last updated on 2025-10-06; verificado em 18/10/2026 | R96 |
| Google Cloud, Speech-to-Text, RecognitionConfig (REST v1) | https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig | Last updated 2025-10-23 UTC; verificado em 18/10/2026 | R88 |
| Microsoft, Azure AI Video Indexer, Customize a language model with Azure AI Video Indexer | https://learn.microsoft.com/en-us/azure/azure-video-indexer/customize-language-model-how-to | Last updated on 2026-07-14; verificado em 18/10/2026 | R100 |
| AWS, Amazon Transcribe, Creating a custom vocabulary using a table | https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-table.html | sem data na página; verificado em 18/10/2026 | R80, R81, R87 |
| AWS, Amazon Transcribe, Generating subtitle files | https://docs.aws.amazon.com/transcribe/latest/dg/subtitles.html | sem data na página; verificado em 18/10/2026 | R94, R95, R102 |
| Google Cloud, Speech-to-Text, speech.recognize (REST v1) | https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/recognize | Last updated 2025-10-23 UTC; verificado em 18/10/2026 | R101 |
| OpenAI, repositório oficial openai/whisper, whisper/normalizers/basic.py (ramo main) | https://raw.githubusercontent.com/openai/whisper/main/whisper/normalizers/basic.py | arquivo aberto e lido em 18/10/2026 (HTTP 200); SHA-256 4742eaa040e0657fa1247a1361e0d856c62317a43326ea59a40c2e9edd8d2c38 (2.064 bytes); verificado em 18/10/2026 | R84, R85 |
| OpenAI, repositório oficial openai/whisper, whisper/normalizers/english.py (ramo main) | https://raw.githubusercontent.com/openai/whisper/main/whisper/normalizers/english.py | arquivo aberto e lido em 18/10/2026 (HTTP 200); SHA-256 d31a52685b5b42628ea4e3343c3a7925ce5b2f317e6c0ec4575677dd5c8b5d2c (21.001 bytes); verificado em 18/10/2026 | R79, R83 |
| OpenAI, repositório oficial openai/whisper, whisper/normalizers/english.json (ramo main) | https://raw.githubusercontent.com/openai/whisper/main/whisper/normalizers/english.json | arquivo aberto e lido em 18/10/2026 (HTTP 200); SHA-256 6607f948be9824d2e1b2fa2223cd94c06c45afa4e05ea0e3d5e1f2bdffde2465 (56.128 bytes); verificado em 18/10/2026 | R79 |
| OpenAI, repositório oficial openai/whisper, whisper/utils.py (ramo main) | https://raw.githubusercontent.com/openai/whisper/main/whisper/utils.py | arquivo aberto e lido em 18/10/2026 (HTTP 200); SHA-256 f46aa555363ab42a455cd7c7f8c108dc2f69c5a94c6354c73ae96d671d9b1c37 (11.839 bytes); verificado em 18/10/2026 | R89, R91, R93, R97 |
| oTranscribe, repositório oficial oTranscribe/oTranscribe, README.md (ramo master) | https://raw.githubusercontent.com/oTranscribe/oTranscribe/master/README.md | arquivo aberto e lido em 18/10/2026 (HTTP 200); SHA-256 8089e13664b683c5b4b397e08cc6a8da6d67a2da2fb22c24995d9fb639954125 (4.861 bytes); verificado em 18/10/2026 | R98, R99 |

Fontes não abertas: nenhuma fonte necessária deixou de abrir. A página do Microsoft Word sobre transcrição de gravações (support.microsoft.com) devolveu 404 no endereço tentado e não foi usada. Não foram tentados, por estarem fora dos hosts liberados, github.com (a página), openai.com, arxiv.org, w3.org (a especificação do WebVTT; o formato foi sustentado pela documentação do Azure e pelo código do Whisper) e gov.br. planalto.gov.br, Legin e camara.leg.br não foram consultados (nenhuma norma citada). O módulo `regex` e o pacote `more_itertools`, de que o código do Whisper depende, não estavam instalados; a execução de teste (corroboração de registro, e não base de gabarito) usou substitutos mínimos desses dois módulos, sem efeito sobre as funções testadas (R79, R83, R84, R85). Na v2, as páginas do Google (RecognitionConfig) e do Azure AI Video Indexer ("View and update transcriptions") foram abertas em 18/10/2026 (HTTP 200) e os trechos literais citados foram conferidos por script contra o texto das páginas.

Dúvidas para a Gerência titular e a QA:
1. Aderência (D-ADERENCIA): decidida pela QA R1 (R79, R84, R85, R91, R94, R101 e R102 PARCIAIS). Registro para a Gerência: em 2.6, só R96 (novo), R98, R99 e R100 julgam função de editor propriamente dita; 10 de 14 julgam formato ou saída de serviço (precedente L2-Q23). Não é vício de item, mas a folha fica deslocada do seu objeto.
2. Base em código do repositório oficial do fornecedor (R79, R83, R84, R85, R89, R91, R93, R97): comentários, docstrings e código-fonte, com SHA-256 do arquivo lido (a execução de teste feita hoje é só corroboração). Precedente aceito pela QA: o docstring de transcribe() no L1-R100. Se a Gerência entender o contrário, caem R79, R83, R84, R85, R91, R93 e R97, e R89 mantém a base da documentação do Azure.
3. R79: o docstring de EnglishNumberNormalizer ("$20 million" resulta em "20000000 dollars") difere do comportamento executado hoje ("$20000000"); por isso o item usa a docstring de EnglishSpellingNormalizer e o arquivo de mapeamento, e não a de números. O registro serve à conferência de janeiro.
4. Concentração de fonte: em 2.5, HLT tem 4 de 14 (R75, R76, R77, R78) e os normalizadores do Whisper têm 4 de 14 (R79, R83, R84, R85); em 2.6, o código do Whisper (utils.py) sustenta 4 de 14 (R89 com a documentação do Azure, R91, R93, R97). Cada ponto é distinto. R97 (2.6) é o de menor custo de troca.
5. R88 e R96 da v1 foram reprovados pela QA R1 e substituídos na v2 por itens de aderência direta: R88 (2.5; sigla TCU e substituição de transcrição com busca sensível à caixa; NP por contagem de ocorrências, formato que a QA preferia) e R96 (2.6; ajuste de linhas no editor do Azure AI Video Indexer). Se a Gerência entender que a contagem 2 de 3 do R88 é situação hipotética e não número, a reclassificação para SH leva 2.5 a SH 6 (30%, no teto), sem estourar.
6. R98 e R99 usam o README do oTranscribe, ferramenta de terceiros, mas é a documentação oficial no repositório do próprio projeto; os enunciados não nomeiam o produto (R99 cita o armazenamento local do navegador). R99 foi marcado VOLÁTIL (baixo) por conservadorismo (hipótese (c), recurso periférico).
7. VOLÁTIL: 2.5 em 4 de 20 (20%, no teto, com R85 marcado conforme a QA R1); 2.6 em 3 de 20 (15%, folga de 1). Qualquer novo VOLÁTIL em 2.5 estoura o teto.

FIM DA PARTE 3/3
FIM DO LOTE
