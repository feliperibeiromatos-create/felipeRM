# L1_reforco_onda2_C_v1.md — T-96 — 2026-10-18 — gerado por gce-cpp

Objeto: parte C da onda 2 do reforço (D-REFORCO-2; T-96, ciclo s12c3). 28 itens AUTORAL novos do Lote 1: P2-1.5 (L1-R75 a L1-R88, +14) e P2-1.6 (L1-R89 a L1-R102, +14). Cada folha passa de 6 para 20 itens. As folhas 1.1 a 1.4, 1.7 e 1.8 são das outras produtoras e não foram tocadas.
Rótulo de todos os itens: AUTORAL (produtor gce-cpp, lote L1-R, onda 2 do reforço, parte C). Nenhum item existente foi alterado. QA PENDENTE: nenhum item deste arquivo entra em simulado antes da QA da gce-cqfp (D-QA-PENDENTE).
Convenção: "verificado em 18/10/2026" = página aberta e lida nesta data, pelo gce-cpp, nesta produção. Nenhuma base de data anterior foi usada (D-FONTE-DATA-ANTERIOR não invocada). Nenhum item cita número de versão, preço ou limite numérico de produto; as contas dos itens R76, R82 e R102 são aritmética dos próprios enunciados.
Entradas lidas: CLAUDE.md; regras/proveniencia.md; regras/estilo_banca.md; edital/modulo_RF_IA_P2.md (itens 1.5 e 1.6); linha T-96 de TAREFAS.md; D-REFORCO-1, D-REFORCO-2, D-FONTE-DATA-ANTERIOR, D-T89-R1-ACEITE e D-ONDA2-FILA; saida/gce/T89_reconciliacao_2026-10-18.md; saida/banco/T93_reconciliacao_2026-10-18.md e estilo_onda_1.md; os 12 itens existentes das folhas (pacote v1.9 e canônicos).

=====================================================================
PARTE 1/3 — MAPA
=====================================================================

## 1. Itens novos (um ponto de julgamento por item, único na folha)

Formatos: D = definição; TS = troca de sujeito; SH = situação hipotética; NP = número ou prazo; PC = par confundível; AP = aplicação parlamentar. Nenhum item novo usa PC (diluição pedida na T89, seção 3).

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL |
|---|---|---|---|---|---|
| L1-R75 | P2-1.5 | Os sinais de pontuação são itens próprios da saída (tipo punctuation), com marcas de tempo e confiança, e não texto anexado à palavra anterior | D | https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works.html ; https://docs.aws.amazon.com/transcribe/latest/dg/streaming-partial-results.html | n |
| L1-R76 | P2-1.5 | Com a pontuação automática, a primeira letra após cada ponto final e cada ponto de interrogação é capitalizada (contagem: 9 + 4 = 13) | NP | https://docs.cloud.google.com/speech-to-text/docs/automatic-punctuation | n |
| L1-R77 | P2-1.5 | A capitalização automática abrange nomes próprios e a primeira palavra de cada frase; não se restringe ao início de frase | TS | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/display-text-format | n |
| L1-R78 | P2-1.5 | A capitalização automática só se aplica a idiomas cujo sistema de escrita distingue maiúsculas e minúsculas | D | https://docs.aws.amazon.com/transcribe/latest/dg/how-numbers.html | n |
| L1-R79 | P2-1.5 | Em resultados parciais, a pontuação também pode mudar até o fim do segmento; o item (palavra ou sinal) pode ser marcado como estável ou não | AP | https://docs.aws.amazon.com/transcribe/latest/dg/streaming-partial-results.html | n |
| L1-R80 | P2-1.5 | Com marcas de tempo por palavra, o Whisper mescla os sinais de fechamento (ponto, vírgula) à palavra anterior e os de abertura à seguinte | TS | https://raw.githubusercontent.com/openai/whisper/main/whisper/transcribe.py | n |
| L1-R81 | P2-1.5 | O TER (e não o WER) estende a avaliação ao formato final de exibição (pontuação, capitalização, ITN) | TS | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | n |
| L1-R82 | P2-1.5 | TER = (I + D + S) ÷ N, com N = tokens da referência (cálculo: 6 ÷ 80 = 7,5%) | NP | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | n |
| L1-R83 | P2-1.5 | Com a pontuação falada interpretada, a palavra "vírgula" citada como assunto pode virar sinal gráfico; o sistema não distingue a intenção | AP | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/display-text-format | n |
| L1-R84 | P2-1.5 | A forma de exibição de cada termo do vocabulário personalizado (grafia e maiúsculas de siglas e nomes) pode ser definida pelo usuário | AP | https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-table.html | n |
| L1-R85 | P2-1.5 | Para medir o TER, a transcrição de referência precisa ter a formatação de exibição (pontuação, capitalização, ITN) | SH | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | n |
| L1-R86 | P2-1.5 | A segmentação semântica devolve resultados finais ao detectar pontuação de fim de frase, e não apenas por silêncio | TS | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech | S (baixo/médio) |
| L1-R87 | P2-1.5 | No modo Automatic o decodificador cuida da pontuação; Dictated implica pontuação explícita (falada) | SH | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription-create | S (baixo/médio) |
| L1-R88 | P2-1.5 | A API de transcrição rápida produz apenas a forma de exibição (com pontuação e capitalização), diferentemente da transcrição em lote | SH | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/fast-transcription-create | S (baixo/médio) |
| L1-R89 | P2-1.6 | O idioma configurado deve corresponder ao efetivamente falado; local incompatível reduz a acurácia | SH | https://learn.microsoft.com/en-us/legal/cognitive-services/speech-service/speech-to-text/transparency-note | n |
| L1-R90 | P2-1.6 | Afastamento e proximidade excessivos do microfone degradam o áudio e a acurácia | D | https://learn.microsoft.com/en-us/legal/cognitive-services/speech-service/speech-to-text/transparency-note | n |
| L1-R91 | P2-1.6 | Fala simultânea (apartes) reduz a acurácia e pode ser tratada como ruído e ignorada; exige conferência | AP | https://learn.microsoft.com/en-us/legal/cognitive-services/speech-service/speech-to-text/transparency-note ; https://docs.cloud.google.com/speech-to-text/docs/best-practices | n |
| L1-R92 | P2-1.6 | Palavra ausente do vocabulário do modelo gera erro; jargão e nomes específicos da organização são os mais expostos | D | https://learn.microsoft.com/en-us/legal/cognitive-services/speech-service/speech-to-text/transparency-note | n |
| L1-R93 | P2-1.6 | Omissões se ligam a sinal de áudio fraco; substituições, a amostra insuficiente de termos do domínio | TS | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | n |
| L1-R94 | P2-1.6 | Lista de frases é personalização em tempo de execução, sem treino; custom speech é personalização prévia, com treino do modelo | TS | https://learn.microsoft.com/en-us/legal/cognitive-services/speech-service/speech-to-text/transparency-note ; https://learn.microsoft.com/en-us/azure/ai-services/speech-service/improve-accuracy-phrase-list | n |
| L1-R95 | P2-1.6 | Erros de inserção se ligam a gravação em ambiente ruidoso, com possível interferência entre falantes | SH | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | n |
| L1-R96 | P2-1.6 | Quando o vocabulário varia entre áreas do domínio, recomendam-se vários modelos customizados, desde que haja variedade de dados de treino | AP | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-speech-overview | n |
| L1-R97 | P2-1.6 | Valores altos de boost reduzem falsos negativos e podem aumentar falsos positivos (e não o inverso) | TS | https://docs.cloud.google.com/speech-to-text/docs/adaptation-model | n |
| L1-R98 | P2-1.6 | O desempenho do Whisper varia entre sotaques e dialetos de um mesmo idioma; avaliar um grupo não dispensa testar os demais | D | https://raw.githubusercontent.com/openai/whisper/main/model-card.md | n |
| L1-R99 | P2-1.6 | A necessidade de modelo customizado se verifica antes: compara-se o modelo base com a transcrição humana e calcula-se o WER | SH | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-speech-overview | n |
| L1-R100 | P2-1.6 | No Whisper de código aberto, um prompt inicial com vocabulário e nomes próprios torna mais provável a grafia correta, sem garanti-la | AP | https://raw.githubusercontent.com/openai/whisper/main/whisper/transcribe.py | n |
| L1-R101 | P2-1.6 | Os modelos Whisper com sufixo .en são apenas para inglês; os sem sufixo são os multilíngues | TS | https://raw.githubusercontent.com/openai/whisper/main/README.md | n |
| L1-R102 | P2-1.6 | O WER soma inserções, omissões e substituições sobre o número de palavras da referência (cálculo: 6 ÷ 40 = 15%) | NP | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | n |

VOLÁTEIS novos: 3 (L1-R86, L1-R87, L1-R88), todos de risco baixo/médio; risco alto novo: 0. Critério aplicado: o da D-T89-R1-ACEITE (VOLÁTIL = gabarito dependente de fato mutável até 4–8/1/2027: versão, limite, preço, disponibilidade, modelo padrão, nome ou existência de recurso). Os demais itens que nomeiam produto afirmam propriedade fixa de artefato publicado, fórmula de métrica ou orientação estrutural da documentação, e entram só na conferência de base de janeiro, sem efeito de VOLÁTIL.

## 2. Itens já existentes por folha e contagem da folha de 20

### P2-1.5 (6 existentes + 14 novos = 20)
| id | ponto | formato | VOL |
|---|---|---|---|
| L1-Q10 | End-to-end pode emitir texto pontuado; arquiteturas clássicas restauram pontuação depois | D | n |
| L1-Q11 | Pontuação falada × pontuação automática | PC | n |
| L1C-Q29 | Pontuação automática pode mudar o sentido; a revisão confere a pontuação | AP | n |
| L1C-Q30 | Capitalização estima e erra (Câmara × câmara) | PC | n |
| L1-R08 | Disponibilidade de pontuação/capitalização varia com idioma e modo; confere-se na documentação | SH | n |
| L1-R09 | Forma lexical (sem caixa e pontuação) × forma de exibição (com) | TS | n |
| L1-R75 a L1-R88 | ver tabela da seção 1 | 14 novos | 3 S |

Contagem de formatos da folha de 20 (existentes + novos): D 3 (15%); TS 5 (25%); SH 4 (20%); NP 2 (10%); PC 2 (10%); AP 4 (20%). Teto de 30% (6 de 20) cumprido em todos os formatos; maior ocupação: TS 5.
VOLÁTEIS da folha de 20: 0 existente(s) + 3 novo(s) = 3 de 20 (15%); teto de 20% (4 de 20) cumprido. Risco alto: 0.

### P2-1.6 (6 existentes + 14 novos = 20)
| id | ponto | formato | VOL |
|---|---|---|---|
| L1-Q12 | Lista de termos não garante acerto em qualquer condição nem corrige sotaque | D | n |
| L1-Q13 | Adaptação de vocabulário não é retreino acústico; sotaque pede dados acústicos | PC | n |
| L1-Q14 | Amazon Transcribe: custom vocabulary × custom language model | PC | S (baixo/médio) |
| L1-R10 | Vocabulário personalizado: termos úteis (inclusive nomes próprios); sem dados confidenciais ou pessoais que nada acrescentam | AP | n |
| L1-R11 | Desempenho de modelo multilíngue varia entre idiomas; WER em inglês não se transfere ao pt-BR | SH | n |
| L1-R12 | Homófonas resolvidas pelo modelo de linguagem, não pelo acústico | TS | n |
| L1-R89 a L1-R102 | ver tabela da seção 1 | 14 novos | 0 S |

Contagem de formatos da folha de 20 (existentes + novos): D 4 (20%); TS 5 (25%); SH 4 (20%); NP 1 (5%); PC 2 (10%); AP 4 (20%). Teto de 30% (6 de 20) cumprido em todos os formatos; maior ocupação: TS 5.
VOLÁTEIS da folha de 20: 1 existente(s) + 0 novo(s) = 1 de 20 (5%); teto de 20% (4 de 20) cumprido. Risco alto: 0.

## 3. Verificação de não repetição e proximidades registradas

Em cada folha, o ponto de cada item novo foi comparado, item a item, com os 6 existentes e com os outros 13 novos; nenhum se repete. Proximidades que a Gerência pode querer ver (todas com ponto distinto):
- R77 (1.5) × L1C-Q30: ambos tratam de capitalização. Q30 julga a certeza do recurso (Câmara × câmara); R77 julga o alcance (nomes próprios e início de frase).
- R87 (1.5) × L1-Q11: ambos tocam pontuação falada × automática. Q11 contrasta os dois recursos; R87 julga qual valor do parâmetro de API deixa o decodificador decidir (VOLÁTIL).
- R88 (1.5) × L1-R09: ambos tocam forma lexical × exibição. R09 define as duas formas; R88 julga qual API só produz a forma de exibição (VOLÁTIL).
- R81, R82 e R85 (1.5) usam o mesmo par de métricas (TER × WER) e a mesma página, mas julgam coisas distintas: qual medida cobre o formato de exibição; o cálculo do TER; o requisito de formatação na referência. Três itens de 20 (15%) em torno de uma métrica; se a Gerência julgar concentração, o R85 é o de menor custo de troca.
- R94 (1.6) × L1-Q13: Q13 julga adaptação × retreino acústico; R94 julga personalização em tempo de execução (lista de frases) × prévia (custom speech).
- R98 (1.6) × L1-Q12 e Q13: sotaque aparece nos três. Q12 e Q13 julgam o que a lista de termos e a adaptação não resolvem; R98 julga a variação de desempenho do Whisper entre sotaques e dialetos.
- R100 (1.6) × L1-R10: R10 julga o conteúdo da lista de termos; R100 julga o prompt inicial do Whisper como forma de orientar a grafia.
- R93, R95 e R102 (1.6) usam a mesma documentação de avaliação da Azure (páginas de erros e de WER), com pontos distintos: causa de omissões e substituições; causa de inserções; fórmula do WER.
- R101 (1.6): a escolha do modelo Whisper aproxima o item da folha 1.8, mas o ponto é a adequação de modelos .en ao português, desafio de pt-BR da folha 1.6.

## 4. Conformidade com as restrições da onda 2

- [TS] (T89, seção 3): exigência = metade dos itens da parte + 2 = 14 + 2 = 16; produzidos: 16 de 28 (13 em itens E, 3 em itens C, estes como "falsa pegadinha", convenção admitida em T93/O-6).
- Formato (T89, seção 3; D-REFORCO-2, regra 3): nenhum "par confundível" novo em 1.5 e 1.6 (PC fica em 2 de 20 = 10% em cada folha, diluído do legado de 33,3%); nenhum formato acima de 30%.
- VOLÁTIL (D-REFORCO-2, regra 4; D-T89-R1-ACEITE): ver seção 2; 3 novos, todos em 1.5, nenhum de risco alto.
- Gabarito da parte (D-REFORCO-2, regra 5): 14 C / 14 E em 28 (50% de C; faixa de 11 a 17 C cumprida); por folha, 7 C / 7 E.
- Estilo (T93, O-1 a O-8): O-1: médias de palavras do enunciado C 43,8 e E 43,4 (na onda 1: 49,6 e 40,4), nenhum C acima de 65 palavras; O-2: "independentemente" em item C (R83); O-3: "pode" também em item E (R98); O-4: nenhum item usa remissão a norma; O-5: nenhuma cauda falsa autocontraditória; O-6: [TS] em 3 itens C, como falsa pegadinha (R79, R95, R99); O-7: restritivo "somente" também em item C (R78); O-8: concessiva "ainda que" em item E (R85).
- Base por item: 28 de 28 com documento oficial ou documentação oficial do fornecedor, URL e "verificado em 18/10/2026" (páginas abertas hoje); as citações literais foram conferidas por script contra o texto das páginas baixadas. Nenhuma norma foi citada (sem PENDENTE NORMATIVO).

FIM DA PARTE 1/3

=====================================================================
PARTE 2/3 — (d) ITENS DO ESTUDANTE
=====================================================================

L1-R75. Julgue o item.
Nos resultados do Amazon Transcribe, os sinais de pontuação inseridos na transcrição não constam como itens próprios da saída: cada sinal é anexado ao texto da palavra anterior, e somente as palavras recebem marcas de tempo e medida de confiança.

L1-R76. Julgue o item.
O Speech-to-Text do Google, com a pontuação automática habilitada, capitaliza a primeira letra após cada ponto final e cada ponto de interrogação inseridos. Em um trecho com 9 pontos finais e 4 pontos de interrogação, cada um seguido de outra palavra, isso resulta em 13 palavras iniciadas por maiúscula.

L1-R77. Julgue o item.
Na formatação do texto de exibição do Azure Speech, a capitalização automática restringe-se à primeira palavra de cada frase, de modo que nomes próprios, como o de um parlamentar citado da tribuna, não são capitalizados por esse recurso.

L1-R78. Julgue o item.
Em um serviço de ASR multilíngue, a capitalização automática de palavras somente se aplica aos idiomas cujo sistema de escrita distingue letras maiúsculas e minúsculas.

L1-R79. Julgue o item.
Em legenda ao vivo, os resultados parciais do segmento em andamento podem ser revistos, inclusive quanto à pontuação: há serviços que indicam, para cada palavra ou sinal, se o item já é estável, e a legenda pode exibir de forma distinta os ainda instáveis.

L1-R80. Julgue o item.
Na implementação de referência do Whisper, quando se solicitam marcas de tempo por palavra, os sinais de pontuação de fechamento, como o ponto final e a vírgula, são mesclados com a palavra seguinte, ao passo que os de abertura, como o parêntese de abertura, são mesclados com a palavra anterior.

L1-R81. Julgue o item.
No Azure Speech, o WER é a medida estendida que avalia o texto final de exibição, com pontuação, capitalização e normalização de números, enquanto o TER, por sua vez, limita-se às palavras do formato lexical.

L1-R82. Julgue o item.
Em um teste do Azure Speech, a referência feita por revisores tinha 80 tokens, e o texto reconhecido teve 1 token inserido, 2 omitidos e 3 substituídos. Nessa situação, o TER, calculado pela soma dos erros dividida pelo número de tokens da referência, é de 7,5%.

L1-R83. Julgue o item.
Em sistema de ASR que interpreta a pontuação falada, a palavra "vírgula", dita por um parlamentar ao se referir ao texto de um dispositivo, pode ser convertida no sinal gráfico, independentemente de ter sido citada como assunto, o que exige atenção do revisor.

L1-R84. Julgue o item.
Em serviços de ASR que permitem associar, a cada termo de um vocabulário personalizado, a forma como ele deve aparecer na saída, a equipe pode fazer constar da transcrição siglas e nomes próprios da Casa com a grafia e as maiúsculas desejadas.

L1-R85. Julgue o item.
Uma equipe pretende medir o TER do ASR da Casa, no Azure Speech, usando como referência transcrições de sessões revisadas apenas quanto às palavras, sem pontuação nem letras maiúsculas. Nessa situação, a referência é adequada, ainda que não tenha esses elementos, pois o TER avalia o texto reconhecido contra as palavras da referência.

L1-R86. Julgue o item.
Na transcrição ao vivo de uma sessão com o Azure Speech, a segmentação semântica do reconhecimento contínuo devolve resultados finais apenas quando detecta silêncio prolongado, sem levar em conta a pontuação de fim de frase, que é irrelevante para o fechamento do segmento.

L1-R87. Julgue o item.
Na transcrição em lote de sessões em que os oradores não ditam sinais de pontuação, a equipe deseja que o decodificador decida a pontuação do texto. Nessa situação, no Azure Speech, deve-se configurar o modo de pontuação Dictated, que atribui ao decodificador a tarefa de inserir os sinais.

L1-R88. Julgue o item.
Considere que uma equipe precise da forma lexical do texto reconhecido, sem pontuação e sem capitalização. Nessa situação, a API de transcrição rápida do Azure Speech não atende à necessidade, porque produz apenas a forma de exibição, ao contrário da API de transcrição em lote.

L1-R89. Julgue o item.
Uma equipe configura o reconhecimento de uma audiência pública para o português do Brasil, mas um convidado estrangeiro passa a falar em espanhol. Nessa situação, a acurácia da transcrição tende a diminuir no trecho em espanhol, pois o idioma configurado deve corresponder ao efetivamente falado no áudio.

L1-R90. Julgue o item.
Na captação do áudio do Plenário para o ASR, o microfone muito afastado do orador reduz a acurácia do reconhecimento, ao passo que o microfone muito próximo da boca a melhora, por captar a voz com mais nitidez.

L1-R91. Julgue o item.
Nos apartes, em que dois parlamentares falam ao mesmo tempo, a acurácia do ASR tende a cair, e há orientação de fornecedor segundo a qual pessoas que falam simultaneamente podem ser interpretadas como ruído de fundo e ignoradas, o que recomenda a conferência desses trechos pelo revisor.

L1-R92. Julgue o item.
Quando uma palavra ausente do vocabulário do modelo aparece no áudio, o resultado é um erro de transcrição, razão pela qual siglas, jargões e nomes próprios específicos da Casa estão entre os termos mais sujeitos a erro e justificam o uso de listas de termos.

L1-R93. Julgue o item.
Na análise dos erros de um teste de ASR com termos da Casa, quando predominam as omissões de palavras, a causa mais provável é a amostra insuficiente de termos do domínio nos dados de treino, ao passo que as substituições costumam decorrer de sinal de áudio fraco.

L1-R94. Julgue o item.
No Azure Speech, a lista de frases (phrase list) exige o treinamento prévio de um modelo com dados da Casa, ao passo que o custom speech é aplicado em tempo de execução, imediatamente antes do reconhecimento, sem necessidade de treinar modelo.

L1-R95. Julgue o item.
Considere que, em teste do ASR com gravações de comissão feitas com ruído de fundo e falas cruzadas, o texto reconhecido tenha apresentado muitas palavras inseridas que ninguém disse. Nessa situação, o resultado é compatível com a orientação de que erros de inserção indicam gravação em ambiente ruidoso.

L1-R96. Julgue o item.
Quando o vocabulário usado em áreas de atuação distintas da Casa difere de modo significativo, pode ser vantajoso treinar modelos customizados separados para cada área, em vez de um modelo único, desde que haja dados de treinamento com variedade suficiente em cada uma.

L1-R97. Julgue o item.
Nas ferramentas de adaptação de vocabulário que permitem atribuir peso (boost) às frases, elevar muito o valor do boost para o nome de um parlamentar reduz os falsos positivos, isto é, os casos em que o nome aparece na transcrição sem ter sido dito, mas aumenta os falsos negativos.

L1-R98. Julgue o item.
Em razão de ter sido treinado com grande volume de dados diversos, o Whisper apresenta desempenho uniforme entre sotaques e dialetos de um mesmo idioma, de modo que a avaliação do modelo com um grupo de falantes pode dispensar testes com os demais grupos regionais.

L1-R99. Julgue o item.
Antes de decidir treinar um modelo customizado, a equipe transcreve uma amostra de áudio das comissões com o modelo base, compara o resultado com a transcrição humana e calcula o WER. Se o WER for elevado, recomenda-se treinar o modelo para as palavras incorretamente identificadas.

L1-R100. Julgue o item.
Uma forma de orientar o Whisper de código aberto a grafar corretamente nomes próprios e termos específicos da Casa é fornecer, como prompt inicial da primeira janela, um texto com esse vocabulário, o que torna mais provável a grafia correta, mas não a garante.

L1-R101. Julgue o item.
Para transcrever as sessões em português com o Whisper de código aberto, a equipe deve escolher um dos modelos com sufixo .en, que são os multilíngues, e não os modelos sem sufixo, que são restritos ao inglês.

L1-R102. Julgue o item.
Em um teste do Azure Speech, a transcrição de referência, feita por revisores, tinha 40 palavras, e o texto reconhecido apresentou 1 palavra inserida, 2 omitidas e 3 substituídas. Nessa situação, o WER é de 12,5%, pois as inserções não entram no cálculo.

FIM DA PARTE 2/3

=====================================================================
PARTE 3/3 — (d-G) GABARITO COMENTADO
=====================================================================
Legenda: [TS] = troca sutil de um único conceito (em item C, "falsa pegadinha": o item descreve corretamente o par que costuma ser invertido). VOLÁTIL = gabarito dependente de fato de produto que pode mudar até a reverificação de 4–8/1/2027. REVERIFICAR = reabrir a URL e conferir o trecho na janela de janeiro (T-11, gce-cqfp); nos itens não VOLÁTEIS a conferência é de base, sem efeito de VOLÁTIL (D-T89-R1-ACEITE). Todas as páginas foram abertas em 18/10/2026.

L1-R75. E [TS]. Na documentação, a saída traz confiança e marcas de tempo para cada palavra ou sinal de pontuação, e o exemplo de resultado mostra o ponto como item de tipo "punctuation". O item troca o item próprio pelo sinal anexado à palavra.
Base: AWS, Amazon Transcribe, How Amazon Transcribe works (https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works.html), verificado em 18/10/2026: “In addition to the transcribed text, transcripts contains data about the transcribed content, including confidence scores and timestamps for each word or punctuation mark.” | AWS, Amazon Transcribe, Streaming and partial results (https://docs.aws.amazon.com/transcribe/latest/dg/streaming-partial-results.html), verificado em 18/10/2026: “"Type": "punctuation"”.
Formato: D (definição).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R76. C. Segundo a documentação, ao habilitar a pontuação automática o serviço capitaliza a primeira letra após cada ponto final e cada ponto de interrogação; 9 + 4 = 13. A contagem inclui os dois sinais, e não apenas o ponto final.
Base: Google Cloud, Speech-to-Text, Enable automatic punctuation (https://docs.cloud.google.com/speech-to-text/docs/automatic-punctuation), verificado em 18/10/2026: “When you enable automatic punctuation Speech-to-Text will also automatically capitalize the first letter after each period and question mark.”.
Formato: NP (número ou prazo).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R77. E [TS]. Segundo a documentação, o serviço capitaliza automaticamente nomes próprios e palavras no início de frase. O item troca o alcance do recurso, reduzindo-o ao início de frase.
Base: Microsoft, Azure Speech, Display text formatting with speech to text (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/display-text-format), verificado em 18/10/2026: “the Speech service automatically capitalizes proper nouns and words at the beginning of a sentence.”.
Formato: TS (troca de sujeito).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R78. C. A documentação do Amazon Transcribe informa que as palavras são capitalizadas nos idiomas que usam distinção de caixa em seus sistemas de escrita. Em escritas sem essa distinção, não há o que capitalizar.
Base: AWS, Amazon Transcribe, Transcribing numbers and punctuation (https://docs.aws.amazon.com/transcribe/latest/dg/how-numbers.html), verificado em 18/10/2026: “capitalizes words appropriately for languages that use case distinction in their writing systems.”.
Formato: D (definição).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R79. C [TS]. No Amazon Transcribe, com a estabilização de resultados parciais, cada item, palavra ou sinal de pontuação, recebe o campo Stable, e os itens não estáveis têm mais chance de mudar. A legenda pode exibi-los em formato diferente, como itálico.
Base: AWS, Amazon Transcribe, Streaming and partial results (https://docs.aws.amazon.com/transcribe/latest/dg/streaming-partial-results.html), verificado em 18/10/2026: “Stable field to indicate whether an item is stable, where 'item' refers to a transcribed word or punctuation mark.”; “Items flagged as false (not stable) are more likely to change as your segment is transcribed.”; “You can also choose to display non-stable words in a different format, such as italics”.
Formato: AP (aplicação parlamentar).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R80. E [TS]. No código de transcribe(), os símbolos de append_punctuations (entre eles o ponto e a vírgula) são mesclados com a palavra anterior, e os de prepend_punctuations (como o parêntese de abertura), com a seguinte. O item inverte o sentido da mesclagem.
Base: OpenAI, repositório oficial openai/whisper, whisper/transcribe.py (ramo main) (https://raw.githubusercontent.com/openai/whisper/main/whisper/transcribe.py), verificado em 18/10/2026: “If word_timestamps is True, merge these punctuation symbols with the next word”; “If word_timestamps is True, merge these punctuation symbols with the previous word”.
Nota de base: Valores padrão conferidos na assinatura de transcribe() (linhas 51 e 52 do arquivo aberto): prepend_punctuations inclui o parêntese de abertura; append_punctuations inclui o ponto e a vírgula.
Formato: TS (troca de sujeito).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R81. E [TS]. A documentação define o WER sobre as palavras e o TER como a medida estendida para o formato final de exibição, com pontuação, capitalização e ITN. O item inverte as atribuições.
Base: Microsoft, Azure Speech, Test accuracy of a custom speech model (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data), verificado em 18/10/2026: “Besides word error rate, you can also use the extended measurement of Token Error Rate (TER) to evaluate quality on the final end-to-end display format.”; “TER takes into account the display format aspects such as punctuation, capitalization, and ITN.”.
Formato: TS (troca de sujeito).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R82. C. A documentação define TER = (I + D + S) ÷ N sobre os tokens da transcrição de referência: (1 + 2 + 3) ÷ 80 = 0,075, ou 7,5%. O denominador é o total de tokens da referência.
Base: Microsoft, Azure Speech, Test accuracy of a custom speech model (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data), verificado em 18/10/2026: “TER counts the number of incorrect tokens identified during recognition, and divides the sum by the total number of tokens provided in the human-labeled transcript (N).”.
Formato: NP (número ou prazo).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R83. C. No modo de ditado do Azure Speech, descrições verbais de pontuação, como "question mark", viram o sinal correspondente. Como a conversão não depende da intenção do orador, a revisão deve conferir os trechos em que a palavra é citada como assunto.
Base: Microsoft, Azure Speech, Display text formatting with speech to text (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/display-text-format), verificado em 18/10/2026: “This mode causes the speech configuration instance to interpret word descriptions of sentence structures such as punctuation.”; “are you sure question mark”.
Nota de base: A parte "independentemente da intenção" é consequência lógica da definição do modo (interpretação de palavras como sinais); a documentação não a enuncia literalmente.
Formato: AP (aplicação parlamentar).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R84. C. No Amazon Transcribe, a coluna DisplayAs da tabela do vocabulário personalizado define como a entrada aparece na saída, como em "DynamoDB" e "ABCs". Assim, grafia e caixa do termo podem ser fixadas pela equipe.
Base: AWS, Amazon Transcribe, Creating a custom vocabulary using a table (https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-table.html), verificado em 18/10/2026: “Defines the how you want your entry to look in your transcription output.”; “Dynamo-D.B.[TAB][TAB][TAB]DynamoDB”.
Formato: AP (aplicação parlamentar).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R85. E [TS]. Para medir o TER, a documentação exige que os dados de teste incluam transcrições com formatação de exibição, como pontuação, capitalização e ITN. Sem esses elementos na referência, a medida deixa de refletir o formato final, que é o seu objeto.
Base: Microsoft, Azure Speech, Test accuracy of a custom speech model (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data), verificado em 18/10/2026: “To measure TER, make sure the audio + transcript testing data includes transcripts with display formatting such as punctuation, capitalization, and ITN.”.
Formato: SH (situação hipotética).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R86. E [TS]. Segundo a documentação, em vez de depender somente de limites de silêncio, a segmentação semântica devolve resultados finais, na maioria dos casos, ao detectar pontuação de fim de frase, como "." ou "?". O item atribui a ela o critério da segmentação por silêncio.
Base: Microsoft, Azure Speech, How to recognize speech (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech), verificado em 18/10/2026: “Instead of only relying on silence timeouts, semantic segmentation mostly segments and returns final results when it detects sentence-ending punctuation (such as '.' or '?').”.
Formato: TS (troca de sujeito).
VOLÁTIL (baixo/médio): existência e condições de um recurso de produto (a documentação cita exigência de versão mínima do SDK e indisponibilidade para alguns idiomas); o item não afirma versão nem idioma. REVERIFICAR em 4–8/1/2027; inapto a simulado final até lá.

L1-R87. E [TS]. Na API de transcrição em lote, o modo Automatic deixa o decodificador tratar a pontuação, e o Dictated implica pontuação explícita, falada. O item troca os dois modos.
Base: Microsoft, Azure Speech, Create a batch transcription (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription-create), verificado em 18/10/2026: “Accepted values are None to disable punctuation, Dictated to imply explicit (spoken) punctuation, Automatic to let the decoder deal with punctuation, or DictatedAndAutomatic to use dictated and automatic punctuation.”.
Formato: SH (situação hipotética).
VOLÁTIL (baixo/médio): nome e valores de uma propriedade de API de serviço gerenciado (existência de recurso). REVERIFICAR em 4–8/1/2027; inapto a simulado final até lá.

L1-R88. C. A documentação informa que a transcrição rápida, diferentemente da transcrição em lote, produz apenas a forma de exibição, que inclui pontuação e capitalização, e não a forma lexical.
Base: Microsoft, Azure Speech, Use the fast transcription API (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/fast-transcription-create), verificado em 18/10/2026: “Unlike the batch transcription API, fast transcription API only produces transcriptions in the display (not lexical) form. The display form is a more human-readable form of the transcription that includes punctuation and capitalization.”.
Formato: SH (situação hipotética).
VOLÁTIL (baixo/médio): capacidade de uma API de serviço gerenciado (existência de recurso). REVERIFICAR em 4–8/1/2027; inapto a simulado final até lá.

L1-R89. C. A nota de transparência do Azure Speech lista o local incompatível entre os fatores que reduzem a acurácia e exige que o idioma especificado corresponda ao falado. O espanhol falado sob configuração pt-BR é o caso.
Base: Microsoft, Azure Speech, Transparency note for speech to text (https://learn.microsoft.com/en-us/legal/cognitive-services/speech-service/speech-to-text/transparency-note), verificado em 18/10/2026: “Mismatched locales: Users might not speak the languages that you expect.”; “The language or locale must match the actual language that's spoken in an input voice.”.
Formato: SH (situação hipotética).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R90. E [TS]. A nota de transparência do Azure Speech indica que tanto o orador muito distante quanto o muito próximo do microfone podem prejudicar a qualidade do áudio e a acurácia. O item troca o efeito da proximidade excessiva.
Base: Microsoft, Azure Speech, Transparency note for speech to text (https://learn.microsoft.com/en-us/legal/cognitive-services/speech-service/speech-to-text/transparency-note), verificado em 18/10/2026: “A speaker who is too close to the microphone could also cause audio quality deterioration. Both cases can adversely affect the accuracy of speech to text.”.
Formato: D (definição).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R91. C. A nota de transparência da Microsoft cita a fala sobreposta entre os fatores de perda de acurácia, e a documentação do Google informa que pessoas falando ao mesmo tempo podem ser tratadas como ruído de fundo e ignoradas. Convém revisar os apartes.
Base: Microsoft, Azure Speech, Transparency note for speech to text (https://learn.microsoft.com/en-us/legal/cognitive-services/speech-service/speech-to-text/transparency-note), verificado em 18/10/2026: “Overlapped speech: There might be multiple speakers within range of an audio input device, and they might speak at the same time.” | Google Cloud, Speech-to-Text, Best practices (https://docs.cloud.google.com/speech-to-text/docs/best-practices), verificado em 18/10/2026: “Multiple people talking at the same time, or at different volumes may be interpreted as background noise and ignored.”.
Formato: AP (aplicação parlamentar).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R92. C. A nota de transparência do Azure Speech afirma que termos e jargões de uma organização podem não constar do vocabulário padrão e que palavra inexistente no modelo gera erro de transcrição. Recomenda, então, adicionar vocabulário personalizado.
Base: Microsoft, Azure Speech, Transparency note for speech to text (https://learn.microsoft.com/en-us/legal/cognitive-services/speech-service/speech-to-text/transparency-note), verificado em 18/10/2026: “If a word that doesn't exist in a model appears in the audio, the result is an error in transcription.”; “users might speak organization-specific terms and jargon that aren't in a standard vocabulary.”.
Formato: D (definição).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R93. E [TS]. Segundo a documentação do Azure Speech, muitas omissões costumam vir de sinal de áudio fraco, e as substituições, de amostra insuficiente de termos do domínio nas transcrições ou no texto relacionado. O item troca as causas.
Base: Microsoft, Azure Speech, Test accuracy of a custom speech model (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data), verificado em 18/10/2026: “When you encounter many deletion errors, it's usually because of weak audio signal strength.”; “Substitution errors often occur when an insufficient sample of domain-specific terms is provided as either human-labeled transcriptions or related text.”.
Formato: TS (troca de sujeito).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R94. E [TS]. A documentação descreve a lista de frases como personalização em tempo de execução, aplicada antes de iniciar o reconhecimento e sem treinamento, e o custom speech como personalização prévia, com treino do modelo. O item inverte os dois.
Base: Microsoft, Azure Speech, Transparency note for speech to text (https://learn.microsoft.com/en-us/legal/cognitive-services/speech-service/speech-to-text/transparency-note), verificado em 18/10/2026: “At runtime through the use of the phrase list feature”; “Ahead of time through the use of custom speech” | Microsoft, Azure Speech, Improve recognition accuracy with phrase list (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/improve-accuracy-phrase-list), verificado em 18/10/2026: “You apply the phrase list at runtime and it doesn't require model training.”.
Formato: TS (troca de sujeito).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R95. C [TS]. A documentação do Azure Speech relaciona os erros de inserção a áudio gravado em ambiente ruidoso, possivelmente com diafonia (crosstalk). A associação está correta: as omissões é que se ligam a sinal fraco.
Base: Microsoft, Azure Speech, Test accuracy of a custom speech model (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data), verificado em 18/10/2026: “Insertion errors mean that the audio was recorded in a noisy environment and crosstalk might be present, causing recognition problems.”.
Formato: SH (situação hipotética).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R96. C. A documentação do Azure Speech recomenda múltiplos modelos quando o vocabulário varia entre as áreas do domínio, pois o modelo não precisa filtrar dados de assuntos alheios, mas lembra que o treino exige variedade de dados.
Base: Microsoft, Azure Speech, What is custom speech? (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-speech-overview), verificado em 18/10/2026: “Multiple models are recommended if the vocabulary varies across the domain areas.”; “Regardless, training still requires a decent variety of training data.”.
Formato: AP (aplicação parlamentar).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R97. E [TS]. A documentação do Google informa que valores de boost mais altos tendem a reduzir os falsos negativos, mas podem aumentar os falsos positivos, isto é, a palavra aparecer sem ter sido dita. O item troca os dois efeitos.
Base: Google Cloud, Speech-to-Text, Improve transcription results with model adaptation (https://docs.cloud.google.com/speech-to-text/docs/adaptation-model), verificado em 18/10/2026: “Higher boost values can result in fewer false negatives”; “boost can also increase the likelihood of false positives; that is, cases where the word or phrase appears in the transcription even though it didn't occur in the audio.”.
Formato: TS (troca de sujeito).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R98. E. O cartão do modelo Whisper informa que o desempenho é desigual entre sotaques e dialetos de um mesmo idioma e recomenda avaliações robustas no contexto e no domínio de uso. Logo, não há uniformidade que dispense testes por grupo.
Base: OpenAI, repositório oficial openai/whisper, model-card.md (ramo main) (https://raw.githubusercontent.com/openai/whisper/main/model-card.md), verificado em 18/10/2026: “The models also exhibit disparate performance on different accents and dialects of particular languages”; “We strongly recommend that users perform robust evaluations of the models in a particular context and domain before deploying them.”.
Formato: D (definição).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R99. C [TS]. O Azure Speech recomenda verificar se o modelo base basta comparando sua transcrição com a humana e obtendo o WER; só com WER alto se recomenda treinar para as palavras erradas. A ordem correta é medir antes de customizar.
Base: Microsoft, Azure Speech, What is custom speech? (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-speech-overview), verificado em 18/10/2026: “One recommended way to see if the base model suffices is to analyze the transcription produced from the base model and compare it with a human-generated transcript for the same audio.”; “If the WER score is high, training a custom model to recognize the incorrectly identified words is recommended.”.
Formato: SH (situação hipotética).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R100. C. A documentação de transcribe() descreve initial_prompt como texto de contexto para a primeira janela, como vocabulários personalizados ou nomes próprios, para tornar mais provável a grafia correta. "Mais provável" não equivale a garantia.
Base: OpenAI, repositório oficial openai/whisper, whisper/transcribe.py (ramo main) (https://raw.githubusercontent.com/openai/whisper/main/whisper/transcribe.py), verificado em 18/10/2026: “Optional text to provide as a prompt for the first window.”; “to make it more likely to predict those word correctly.”.
Formato: AP (aplicação parlamentar).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R101. E [TS]. No README do Whisper, as versões .en são modelos apenas para inglês, e os modelos sem o sufixo são os multilíngues. O item troca as duas categorias.
Base: OpenAI, repositório oficial openai/whisper, README.md (ramo main) (https://raw.githubusercontent.com/openai/whisper/main/README.md), verificado em 18/10/2026: “| tiny | 39 M | `tiny.en` | `tiny` |”; “The `.en` models for English-only applications tend to perform better”.
Nota de base: Os nomes dos modelos e a coluna "English-only model" × "Multilingual model" constam da tabela "Available models and languages" do README.
Formato: TS (troca de sujeito).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R102. E [TS]. O WER soma inserções, omissões e substituições e divide o total pelo número de palavras da referência: (1 + 2 + 3) ÷ 40 = 15%. Os 12,5% resultam de excluir as inserções, que a fórmula inclui.
Base: Microsoft, Azure Speech, Test accuracy of a custom speech model (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data), verificado em 18/10/2026: “WER counts the number of incorrect words identified during recognition, and divides the sum by the total number of words provided in the human-labeled transcript (N).”; “Insertion (I): Words that are incorrectly added in the hypothesis transcript”.
Formato: NP (número ou prazo).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

## Contagens
| quesito | valor |
|---|---|
| total | 28 (P2-1.5: 14, de L1-R75 a L1-R88; P2-1.6: 14, de L1-R89 a L1-R102) |
| P2-1.5 | 7 C (R76, R78, R79, R82, R83, R84, R88) / 7 E (R75, R77, R80, R81, R85, R86, R87) |
| P2-1.6 | 7 C (R89, R91, R92, R95, R96, R99, R100) / 7 E (R90, R93, R94, R97, R98, R101, R102) |
| C / E da parte | 14 C / 14 E (50% de C; faixa 11 a 17 C cumprida) |
| [TS] | 16 de 28 (exigência: 16): 13 em itens E (R75, R77, R80, R81, R85, R86, R87, R90, R93, R94, R97, R101, R102) e 3 em itens C (R79, R95, R99) |
| [TS] por folha | P2-1.5: 8 de 14; P2-1.6: 8 de 14 |
| VOLÁTIL novos | 3 (R86, R87, R88); risco alto: 0 |
| VOLÁTEIS da folha de 20 | P2-1.5: 3 de 20 (15%); P2-1.6: 1 de 20 (5%; L1-Q14, existente) |
| formatos de P2-1.5 (20) | D 3; TS 5; SH 4; NP 2; PC 2; AP 4 |
| formatos de P2-1.6 (20) | D 4; TS 5; SH 4; NP 1; PC 2; AP 4 |
| formatos dos 28 novos | D 5; TS 8; SH 6; NP 3; PC 0; AP 6 |
| extensão (palavras do enunciado) | C: média 43,8, mediana 45, de 25 a 49; E: média 43,4, mediana 43, de 35 a 53 |
| aritmética conferida por script | R76: 9 + 4 = 13; R82: (1 + 2 + 3) ÷ 80 = 7,5%; R102: (1 + 2 + 3) ÷ 40 = 15% (o item afirma 12,5% = 5 ÷ 40, sem as inserções) |

## Lista de REVERIFICAR de janeiro (4–8/1/2027; T-11, parte P2, gce-cqfp)
- VOLÁTEIS: L1-R86, L1-R87, L1-R88.
- Conferência de base sem efeito de VOLÁTIL: L1-R75, L1-R76, L1-R77, L1-R78, L1-R79, L1-R80, L1-R81, L1-R82, L1-R83, L1-R84, L1-R85, L1-R89, L1-R90, L1-R91, L1-R92, L1-R93, L1-R94, L1-R95, L1-R96, L1-R97, L1-R98, L1-R99, L1-R100, L1-R101, L1-R102.
- Atenção especial: R80 e R100 têm base em arquivo de código do ramo main (whisper/transcribe.py: docstring e valores padrão da assinatura), que muda mais que o README; R98 e R101 têm base em model-card.md e README do mesmo repositório; R90 depende de trecho da nota de transparência da Microsoft (data da página: 31/03/2026).

## Tabela de proveniência (todas as páginas abertas e lidas em 18/10/2026)
| fonte | URL oficial | data da página / verificação | usada em |
|---|---|---|---|
| AWS, Amazon Transcribe, How Amazon Transcribe works | https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works.html | sem data na página; verificado em 18/10/2026 | R75 |
| AWS, Amazon Transcribe, Transcribing numbers and punctuation | https://docs.aws.amazon.com/transcribe/latest/dg/how-numbers.html | sem data na página; verificado em 18/10/2026 | R78 |
| AWS, Amazon Transcribe, Streaming and partial results | https://docs.aws.amazon.com/transcribe/latest/dg/streaming-partial-results.html | sem data na página; verificado em 18/10/2026 | R75, R79 |
| AWS, Amazon Transcribe, Creating a custom vocabulary using a table | https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-table.html | sem data na página; verificado em 18/10/2026 | R84 |
| Google Cloud, Speech-to-Text, Enable automatic punctuation | https://docs.cloud.google.com/speech-to-text/docs/automatic-punctuation | Last updated 2026-10-13 UTC; verificado em 18/10/2026 | R76 |
| Google Cloud, Speech-to-Text, Improve transcription results with model adaptation | https://docs.cloud.google.com/speech-to-text/docs/adaptation-model | Last updated 2026-10-13 UTC; verificado em 18/10/2026 | R97 |
| Google Cloud, Speech-to-Text, Best practices | https://docs.cloud.google.com/speech-to-text/docs/best-practices | Last updated 2026-10-13 UTC; verificado em 18/10/2026 | R91 |
| Microsoft, Azure Speech, Display text formatting with speech to text | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/display-text-format | Last updated on 2025-12-29; verificado em 18/10/2026 | R77, R83 |
| Microsoft, Azure Speech, Test accuracy of a custom speech model | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | Last updated on 2025-12-29; verificado em 18/10/2026 | R81, R82, R85, R93, R95, R102 |
| Microsoft, Azure Speech, What is custom speech? | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-speech-overview | Last updated on 2026-02-25; verificado em 18/10/2026 | R96, R99 |
| Microsoft, Azure Speech, Improve recognition accuracy with phrase list | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/improve-accuracy-phrase-list | Last updated on 2026-06-29; verificado em 18/10/2026 | R94 |
| Microsoft, Azure Speech, Transparency note for speech to text | https://learn.microsoft.com/en-us/legal/cognitive-services/speech-service/speech-to-text/transparency-note | Last updated on 2026-03-31; verificado em 18/10/2026 | R89, R90, R91, R92, R94 |
| Microsoft, Azure Speech, Create a batch transcription | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription-create | Last updated on 2026-04-03; verificado em 18/10/2026 | R87 |
| Microsoft, Azure Speech, Use the fast transcription API | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/fast-transcription-create | Last updated on 2026-04-08; verificado em 18/10/2026 | R88 |
| Microsoft, Azure Speech, How to recognize speech | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech | Last updated on 2026-06-05; verificado em 18/10/2026 | R86 |
| OpenAI, repositório oficial openai/whisper, README.md (ramo main) | https://raw.githubusercontent.com/openai/whisper/main/README.md | arquivo aberto e lido em 18/10/2026 (HTTP 200); verificado em 18/10/2026 | R101 |
| OpenAI, repositório oficial openai/whisper, model-card.md (ramo main) | https://raw.githubusercontent.com/openai/whisper/main/model-card.md | arquivo aberto e lido em 18/10/2026 (HTTP 200); verificado em 18/10/2026 | R98 |
| OpenAI, repositório oficial openai/whisper, whisper/transcribe.py (ramo main) | https://raw.githubusercontent.com/openai/whisper/main/whisper/transcribe.py | arquivo aberto e lido em 18/10/2026 (HTTP 200); verificado em 18/10/2026 | R80, R100 |

Fontes não abertas: nenhuma fonte necessária deixou de abrir. Não foram tentados, por estarem fora dos hosts liberados, github.com (a página), openai.com, arxiv.org (artigo do Whisper citado no README), w3.org e huggingface.co; nenhum item depende deles. Duas URLs de cartão de IA responsável da AWS retornaram 404 e não foram usadas. planalto.gov.br, Legin e camara.leg.br não foram consultados (nenhuma norma citada).

Dúvidas para a Gerência titular e a QA:
1. VOLÁTIL de R86, R87 e R88: classificados S (baixo/médio) por dependerem de existência e condições de recurso de produto (segmentação semântica; valores do parâmetro de pontuação da transcrição em lote; capacidade da API de transcrição rápida). Se a Gerência os tratar como não VOLÁTEIS, nada muda no teto; se tratar outros como VOLÁTEIS, 1.5 tem folga até 4 de 20.
2. R80 e R100 usam como base o docstring e a assinatura de transcribe() no repositório oficial do Whisper (código, não documentação em prosa). O README sustenta R101; o model-card sustenta R98. Se a Gerência entender que código-fonte não é "documentação do fornecedor", R80 e R100 caem e podem ser substituídos por outros dois pontos de 1.5 e 1.6.
3. R83: a oração "independentemente de ter sido citada como assunto" é consequência lógica do modo de ditado (a palavra é interpretada como sinal), não frase literal da documentação; a base literal sustenta a interpretação de descrições verbais de pontuação.
4. R90: a documentação do Google recomenda o microfone o mais próximo possível do falante; o item se apoia na nota da Microsoft ("too close" também prejudica) e fala de microfone "muito próximo da boca". A QA pode conferir se a redação evita conflito entre as duas orientações.
5. TER em 1.5: três itens (R81, R82, R85); ver seção 3 da Parte 1.

FIM DA PARTE 3/3
FIM DO LOTE
