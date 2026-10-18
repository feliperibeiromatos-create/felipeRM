# L1_reforco_onda2_C_v2.md — T-96 — 2026-10-18 — gerado por gce-cpp

## RESPOSTA AO PARECER QA_T96C_R1_2026-10-18_gce-cqfp.md (rodada 2 de no máximo 2)

Resultado: 5 reprovados substituídos (mesmos ids e folhas), 4 ajustes aplicados com o texto exato, 19 itens aprovados mantidos sem alteração de texto; nada mais foi mudado (diff v1 para v2 limitado às linhas dos 9 itens, às linhas de contagem e de base que dependem deles e a este bloco).

| item do parecer | veredito da QA | resposta |
|---|---|---|
| L1-R76 | AJUSTAR (A-1) | acatado. Aplicado o texto exato: "isso resulta em 13 palavras iniciadas por maiúscula." passou a "essa regra resulta na capitalização de 13 palavras." Gabarito C e justificativa mantidos. |
| L1-R84 | AJUSTAR (A-2) | acatado. Enunciado substituído pelo texto exato do parecer ("Há serviços de ASR em que o vocabulário personalizado permite associar a cada termo a forma como ele deve aparecer na saída, o que possibilita fazer constar da transcrição siglas e nomes próprios da Casa com a grafia e as maiúsculas desejadas."). Gabarito C, não VOLÁTIL. |
| L1-R90 | AJUSTAR (A-3) | acatado. Inserido no início "Segundo a nota de transparência do Azure Speech, " e "Na captação" passou a "na captação". Gabarito E mantido. |
| L1-R92 | AJUSTAR (A-4) | acatado. Abertura substituída pelo texto exato: "Segundo a nota de transparência do Azure Speech, quando uma palavra que não existe no modelo aparece no áudio, o resultado é um erro de transcrição; por isso," Gabarito C mantido. |
| L1-R80 | REPROVADO (fora do edital; depende de valores padrão do ramo main) | acatado. Substituído, mesmo id, folha 1.5, por item novo E [TS], formato troca de sujeito: a pontuação automática do Amazon Transcribe vale para todos os idiomas suportados, e a condição de suporte à transcrição de números não a restringe (o item atribui à pontuação a condição dos números). Está no texto do edital da folha ("pontuação automática"). Base aberta hoje com trecho literal; não VOLÁTIL; nenhum valor de repositório. |
| L1-R87 | REPROVADO (duplicata de L1-Q11) | acatado. Substituído, mesmo id, folha 1.5, por item novo E [TS], situação hipotética: no arquivo de formato de exibição personalizado do custom speech, a regra que fixa capitalização e grafia fica em #rewrite, e não em #itn. Ponto de capitalização controlada, sem relação com pontuação falada × automática (Q11). Base aberta hoje, trecho literal; VOLÁTIL baixo/médio (recurso de serviço gerenciado; a folha 1.5 fica em 3 de 20, como na v1). |
| L1-R99 | REPROVADO (duplicata de L1-R128, parte D) | acatado. Substituído, mesmo id, folha 1.6, por item novo C [TS] (falsa pegadinha, par costumeiramente invertido), formato definição: para termos de pronúncia não padrão (siglas), o Azure Speech indica dados de pronúncia; texto simples fica com vocabulário e gramática do setor. Vocabulário técnico, como a QA recomendou. Sem WER e sem comparação de modelo base (R128 fica só na parte D). Não VOLÁTIL. |
| L1-R101 | REPROVADO (duplicata de L1-R117, parte D; ponto de 1.8) | acatado. Substituído, mesmo id, folha 1.6, por item novo E [TS], situação hipotética: no vocabulário personalizado do Amazon Transcribe, a entrada de várias palavras liga as palavras por hífen, e não por espaço (nome de comissão). Vocabulário parlamentar; sem catálogo de modelos nem Whisper. Não VOLÁTIL. |
| L1-R102 | REPROVADO (fórmula do WER é de 1.1; coberto por L2-R06) | acatado. Substituído, mesmo id, folha 1.6, por item novo E [TS], troca de sujeito: o boost atribuído a frase de várias palavras incide sobre a frase inteira e somente sobre ela, e não sobre cada trecho (nome completo de órgão da Casa). Vocabulário parlamentar; sem WER. Não VOLÁTIL. |
| Aprovados: R75, R77, R78, R79, R81, R82, R83, R85, R86, R88, R89, R91, R93, R94, R95, R96, R97, R98, R100 | APROVADO | mantidos sem alteração de texto, gabarito, [TS] ou justificativa. |
| Dúvida 1 da produtora (docstring como documentação do fornecedor) | SIM, vale | acatado. Recomendação de registrar o SHA do commit: acatada em parte. Os hosts liberados (raw.githubusercontent.com, entre outros) não incluem github.com nem api.github.com, e o endereço raw do ramo main não informa o commit; registrado, em seu lugar, o SHA-256 do arquivo lido hoje (whisper/transcribe.py, 30.375 bytes: 176f5ab30e961bec2a7872f5701a1f5bf3cbfc77946e50512f0f0cf00a1ceacf), para a conferência de janeiro detectar qualquer alteração. R100 é o único item desta parte que ainda se apoia nesse arquivo (R80 saiu). |
| Dúvidas 2 a 5 (VOLÁTIL; R83; R90; TER) | respondidas | acatado. VOLÁTIL: R86, R87 (novo) e R88 (1.5 em 3 de 20; teto de 4). R83: o ponto do mapa fica registrado como "a palavra pode ser convertida mesmo quando citada como assunto" (item e gabarito inalterados). R90: fechado pelo A-3. TER em 1.5: R81, R82 e R85 mantidos (3 de 20, 15%); R85 é o de troca se a Gerência quiser diluir. |
| Registros para a D1: R79 (formato AP e [TS] fraco), R93 × L1-R20, R94 × L1-R120 | registro | acatado. Nenhum texto mudado; os três constam na seção 3 da Parte 1. R79 permanece AP (a reclassificação para D é facultativa e não estoura o teto). |
| Bloqueio: não transferir L1-R43 (parte A) para 1.6 enquanto R98 estiver mantido | registro | acatado e sem objeto: a parte A v2 substituiu o L1-R43 por ponto do wav2vec 2.0 (10 minutos de ajuste fino, folha 1.2); R98 permanece. |
| Cobertura: substituições de 1.6 em sotaques ou vocabulário parlamentar | recomendação | acatado. As três de 1.6 tratam de vocabulário técnico e parlamentar (dados de pronúncia de siglas; entrada de nome composto; peso de frase composta). |

Objeto: parte C da onda 2 do reforço (D-REFORCO-2; T-96, ciclo s12c3). 28 itens AUTORAL novos do Lote 1: P2-1.5 (L1-R75 a L1-R88, +14) e P2-1.6 (L1-R89 a L1-R102, +14). Cada folha passa de 6 para 20 itens. As folhas 1.1 a 1.4, 1.7 e 1.8 são das outras produtoras e não foram tocadas.
Rótulo de todos os itens: AUTORAL (produtor gce-cpp, lote L1-R, onda 2 do reforço, parte C). Nenhum item existente foi alterado. QA PENDENTE: nenhum item deste arquivo entra em simulado antes da QA da gce-cqfp (D-QA-PENDENTE).
Convenção: "verificado em 18/10/2026" = página aberta e lida nesta data, pelo gce-cpp, nesta produção. Nenhuma base de data anterior foi usada (D-FONTE-DATA-ANTERIOR não invocada). Nenhum item cita número de versão, preço ou limite numérico de produto; as contas dos itens R76 e R82 são aritmética dos próprios enunciados.
Entradas lidas (v2, além das da v1): QA_T96C_R1_2026-10-18_gce-cqfp.md; D-REFORCO-2 e D-T89-R1-ACEITE em DECISOES.md; partes A, B e D v2 da onda (para não repetir ponto). Entradas lidas na v1: CLAUDE.md; regras/proveniencia.md; regras/estilo_banca.md; edital/modulo_RF_IA_P2.md (itens 1.5 e 1.6); linha T-96 de TAREFAS.md; D-REFORCO-1, D-REFORCO-2, D-FONTE-DATA-ANTERIOR, D-T89-R1-ACEITE e D-ONDA2-FILA; saida/gce/T89_reconciliacao_2026-10-18.md; saida/banco/T93_reconciliacao_2026-10-18.md e estilo_onda_1.md; os 12 itens existentes das folhas (pacote v1.9 e canônicos).

=====================================================================
PARTE 1/3 — MAPA
=====================================================================

## 1. Itens novos (um ponto de julgamento por item, único na folha)

Formatos: D = definição; TS = troca de sujeito; SH = situação hipotética; NP = número ou prazo; PC = par confundível; AP = aplicação parlamentar. Nenhum item novo usa PC (diluição pedida na T89, seção 3). Na v2, os 5 substitutos têm [TS] (troca de um único conceito), nenhum repete ponto das folhas, da onda 1 ou das partes A, B e D, e nenhum usa valor padrão de ramo de repositório.

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL |
|---|---|---|---|---|---|
| L1-R75 | P2-1.5 | Os sinais de pontuação são itens próprios da saída (tipo punctuation), com marcas de tempo e confiança, e não texto anexado à palavra anterior | D | https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works.html ; https://docs.aws.amazon.com/transcribe/latest/dg/streaming-partial-results.html | n |
| L1-R76 | P2-1.5 | Com a pontuação automática, a primeira letra após cada ponto final e cada ponto de interrogação é capitalizada (contagem: 9 + 4 = 13) | NP | https://docs.cloud.google.com/speech-to-text/docs/automatic-punctuation | n |
| L1-R77 | P2-1.5 | A capitalização automática abrange nomes próprios e a primeira palavra de cada frase; não se restringe ao início de frase | TS | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/display-text-format | n |
| L1-R78 | P2-1.5 | A capitalização automática só se aplica a idiomas cujo sistema de escrita distingue maiúsculas e minúsculas | D | https://docs.aws.amazon.com/transcribe/latest/dg/how-numbers.html | n |
| L1-R79 | P2-1.5 | Em resultados parciais, a pontuação também pode mudar até o fim do segmento; o item (palavra ou sinal) pode ser marcado como estável ou não | AP | https://docs.aws.amazon.com/transcribe/latest/dg/streaming-partial-results.html | n |
| L1-R80 | P2-1.5 | A pontuação automática vale para todos os idiomas suportados; a condição de haver suporte à transcrição de números refere-se ao formato dos números (algarismos), e não à pontuação | TS | https://docs.aws.amazon.com/transcribe/latest/dg/how-numbers.html | n |
| L1-R81 | P2-1.5 | O TER (e não o WER) estende a avaliação ao formato final de exibição (pontuação, capitalização, ITN) | TS | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | n |
| L1-R82 | P2-1.5 | TER = (I + D + S) ÷ N, com N = tokens da referência (cálculo: 6 ÷ 80 = 7,5%) | NP | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | n |
| L1-R83 | P2-1.5 | Com a pontuação falada interpretada, a palavra "vírgula" citada como assunto pode virar sinal gráfico; o sistema não distingue a intenção | AP | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/display-text-format | n |
| L1-R84 | P2-1.5 | A forma de exibição de cada termo do vocabulário personalizado (grafia e maiúsculas de siglas e nomes) pode ser definida pelo usuário | AP | https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-table.html | n |
| L1-R85 | P2-1.5 | Para medir o TER, a transcrição de referência precisa ter a formatação de exibição (pontuação, capitalização, ITN) | SH | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | n |
| L1-R86 | P2-1.5 | A segmentação semântica devolve resultados finais ao detectar pontuação de fim de frase, e não apenas por silêncio | TS | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech | S (baixo/médio) |
| L1-R87 | P2-1.5 | No arquivo de formato de exibição personalizado do custom speech, a seção #rewrite (e não a #itn) reúne os pares de reescrita para capitalização e correção de grafia | SH | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-test-and-train (seção "Custom display text formatting data for training") | S (baixo/médio) |
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
| L1-R99 | P2-1.6 | Para termos de pronúncia não padrão (siglas), o dado indicado é o de pronúncia (forma fonética e de exibição); o texto simples fica com vocabulário e gramática do setor | D | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-test-and-train (tabela de uso e tipo de dado) | n |
| L1-R100 | P2-1.6 | No Whisper de código aberto, um prompt inicial com vocabulário e nomes próprios torna mais provável a grafia correta, sem garanti-la | AP | https://raw.githubusercontent.com/openai/whisper/main/whisper/transcribe.py | n |
| L1-R101 | P2-1.6 | No vocabulário personalizado do Amazon Transcribe, a entrada de várias palavras liga as palavras por hífen, e não por espaço | SH | https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-list.html ; https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-table.html | n |
| L1-R102 | P2-1.6 | O boost atribuído a frase de várias palavras incide sobre a frase inteira e somente sobre ela; favorecer trechos exige entradas adicionais (bigramas), cada uma com seu boost | TS | https://docs.cloud.google.com/speech-to-text/docs/adaptation-model | n |

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

Contagem de formatos da folha de 20 (existentes + novos): D 5 (25%); TS 5 (25%); SH 4 (20%); NP 0 (0%); PC 2 (10%); AP 4 (20%). Teto de 30% (6 de 20) cumprido em todos os formatos; maior ocupação: D 5 e TS 5.
VOLÁTEIS da folha de 20: 1 existente(s) + 0 novo(s) = 1 de 20 (5%); teto de 20% (4 de 20) cumprido. Risco alto: 0.

## 3. Verificação de não repetição e proximidades registradas

Em cada folha, o ponto de cada item novo foi comparado, item a item, com os 6 existentes e com os outros 13 novos; nenhum se repete. Proximidades que a Gerência pode querer ver (todas com ponto distinto):
- R77 (1.5) × L1C-Q30: ambos tratam de capitalização. Q30 julga a certeza do recurso (Câmara × câmara); R77 julga o alcance (nomes próprios e início de frase).
- R80 (1.5, substituto) × L1-R78: mesma página da AWS ("Transcribing numbers and punctuation"). R78 julga a condição da capitalização (idiomas com distinção de caixa); R80 julga a abrangência da pontuação (todos os idiomas suportados) e a condição de suporte a números, que não é dela. R80 × L1-R08: R08 manda conferir a disponibilidade por idioma e modo, sem conflito, pois a AWS fala em "all supported languages".
- R87 (1.5, substituto) × L1C-Q30 e R77: os três tocam a capitalização. Q30 julga a certeza do recurso; R77, o alcance da capitalização automática; R87 julga em qual seção das regras de exibição personalizadas se fixa a capitalização de um termo (#rewrite × #itn). Ponto distinto, de recurso de custom speech, e VOLÁTIL.
- R88 (1.5) × L1-R09: ambos tocam forma lexical × exibição. R09 define as duas formas; R88 julga qual API só produz a forma de exibição (VOLÁTIL).
- R81, R82 e R85 (1.5) usam o mesmo par de métricas (TER × WER) e a mesma página, mas julgam coisas distintas: qual medida cobre o formato de exibição; o cálculo do TER; o requisito de formatação na referência. Três itens de 20 (15%) em torno de uma métrica; se a Gerência julgar concentração, o R85 é o de menor custo de troca.
- R94 (1.6) × L1-Q13: Q13 julga adaptação × retreino acústico; R94 julga personalização em tempo de execução (lista de frases) × prévia (custom speech).
- R98 (1.6) × L1-Q12 e Q13: sotaque aparece nos três. Q12 e Q13 julgam o que a lista de termos e a adaptação não resolvem; R98 julga a variação de desempenho do Whisper entre sotaques e dialetos.
- R100 (1.6) × L1-R10: R10 julga o conteúdo da lista de termos; R100 julga o prompt inicial do Whisper como forma de orientar a grafia.
- R93 e R95 (1.6) usam a mesma documentação de avaliação da Azure (página de erros), com pontos distintos: causa de omissões e substituições; causa de inserções. R93 × L1-R20 (parte A) e R94 × L1-R120 (parte D) seguem registrados para a D1, como pediu a QA.
- R99 (1.6, substituto) × L1-Q12 e Q13: Q13 julga adaptação de vocabulário × retreino acústico (sotaque); R99 mapeia o tipo de dado do custom speech ao uso (pronúncia de siglas × texto simples). R99 × L1C-Q23 (1.2, canônico): Q23 diz que, em sistemas end-to-end, em regra não há dicionário de pronúncias separado a editar; R99 afirma só o que a documentação do Azure indica (dados de pronúncia no custom speech), sem generalizar para sistemas end-to-end. R99 não repete o R128 (1.8, parte D, comparação do modelo base por WER).
- R101 (1.6, substituto) × L1-R10 (1.6) e L1-R84 (1.5): R10 julga o conteúdo da lista (termos úteis, sem dados pessoais); R84 julga a forma de exibição (DisplayAs, mesma tabela da AWS); R101 julga a forma de grafar a entrada de várias palavras (hífen). Pontos distintos. R101 não repete o R117 (1.8, parte D, modelos .en).
- R102 (1.6, substituto) × L1-R97 (1.6): mesma página do Google (adaptação de modelo). R97 julga os efeitos de valores altos de boost (falsos negativos × positivos); R102 julga o alcance do peso sobre frase de várias palavras. R102 não toca a fórmula do WER (L1-R19, 1.1) nem L2-R06.
- Bloqueio da QA sobre L1-R43: sem objeto (a parte A v2 substituiu o L1-R43 por ponto do wav2vec 2.0, folha 1.2).

## 4. Conformidade com as restrições da onda 2

- [TS] (T89, seção 3): exigência = metade dos itens da parte + 2 = 14 + 2 = 16; produzidos: 16 de 28 (13 em itens E, 3 em itens C, estes como "falsa pegadinha", convenção admitida em T93/O-6).
- Formato (T89, seção 3; D-REFORCO-2, regra 3): nenhum "par confundível" novo em 1.5 e 1.6 (PC fica em 2 de 20 = 10% em cada folha, diluído do legado de 33,3%); nenhum formato acima de 30%.
- VOLÁTIL (D-REFORCO-2, regra 4; D-T89-R1-ACEITE): ver seção 2; 3 novos, todos em 1.5, nenhum de risco alto.
- Gabarito da parte (D-REFORCO-2, regra 5): 14 C / 14 E em 28 (50% de C; faixa de 11 a 17 C cumprida); por folha, 7 C / 7 E.
- Estilo (T93, O-1 a O-8): O-1: médias de palavras do enunciado C 45,1 e E 44,9 (na onda 1: 49,6 e 40,4), nenhum C acima de 65 palavras (maior C: 57); O-2: "independentemente" em item C (R83); O-3: "pode" também em item E (R98); O-4: nenhum item usa remissão a norma; O-5: nenhuma cauda falsa autocontraditória; O-6: [TS] em 3 itens C, como falsa pegadinha (R79, R95, R99), todos com par correto e costumeiramente invertido; os 5 substitutos da v2 têm [TS] de troca única; O-7: restritivo "somente" também em item C (R78); O-8: concessiva "ainda que" em item E (R85).
- Substituição (v2): os 5 itens novos têm [TS] de troca única, nenhum "par confundível", pontos distintos dos demais da folha, da onda 1 e das partes A, B e D (conferido contra os mapas de A_v2, B_v2 e D_v2 e contra o pacote v1.9), tetos de formato e de VOLÁTIL cumpridos; 14 C / 14 E mantidos (7 / 7 por folha).
- Base por item: 28 de 28 com documento oficial ou documentação oficial do fornecedor, URL e "verificado em 18/10/2026" (páginas abertas hoje); as citações literais foram conferidas por script contra o texto das páginas baixadas. Nenhuma norma foi citada (sem PENDENTE NORMATIVO).

FIM DA PARTE 1/3

=====================================================================
PARTE 2/3 — (d) ITENS DO ESTUDANTE
=====================================================================

L1-R75. Julgue o item.
Nos resultados do Amazon Transcribe, os sinais de pontuação inseridos na transcrição não constam como itens próprios da saída: cada sinal é anexado ao texto da palavra anterior, e somente as palavras recebem marcas de tempo e medida de confiança.

L1-R76. Julgue o item.
O Speech-to-Text do Google, com a pontuação automática habilitada, capitaliza a primeira letra após cada ponto final e cada ponto de interrogação inseridos. Em um trecho com 9 pontos finais e 4 pontos de interrogação, cada um seguido de outra palavra, essa regra resulta na capitalização de 13 palavras.

L1-R77. Julgue o item.
Na formatação do texto de exibição do Azure Speech, a capitalização automática restringe-se à primeira palavra de cada frase, de modo que nomes próprios, como o de um parlamentar citado da tribuna, não são capitalizados por esse recurso.

L1-R78. Julgue o item.
Em um serviço de ASR multilíngue, a capitalização automática de palavras somente se aplica aos idiomas cujo sistema de escrita distingue letras maiúsculas e minúsculas.

L1-R79. Julgue o item.
Em legenda ao vivo, os resultados parciais do segmento em andamento podem ser revistos, inclusive quanto à pontuação: há serviços que indicam, para cada palavra ou sinal, se o item já é estável, e a legenda pode exibir de forma distinta os ainda instáveis.

L1-R80. Julgue o item.
Segundo a documentação do Amazon Transcribe, a pontuação automática é inserida somente nos idiomas que contam com suporte à transcrição de números em algarismos; nos demais, a saída da transcrição vem sem sinais de pontuação.

L1-R81. Julgue o item.
No Azure Speech, o WER é a medida estendida que avalia o texto final de exibição, com pontuação, capitalização e normalização de números, enquanto o TER, por sua vez, limita-se às palavras do formato lexical.

L1-R82. Julgue o item.
Em um teste do Azure Speech, a referência feita por revisores tinha 80 tokens, e o texto reconhecido teve 1 token inserido, 2 omitidos e 3 substituídos. Nessa situação, o TER, calculado pela soma dos erros dividida pelo número de tokens da referência, é de 7,5%.

L1-R83. Julgue o item.
Em sistema de ASR que interpreta a pontuação falada, a palavra "vírgula", dita por um parlamentar ao se referir ao texto de um dispositivo, pode ser convertida no sinal gráfico, independentemente de ter sido citada como assunto, o que exige atenção do revisor.

L1-R84. Julgue o item.
Há serviços de ASR em que o vocabulário personalizado permite associar a cada termo a forma como ele deve aparecer na saída, o que possibilita fazer constar da transcrição siglas e nomes próprios da Casa com a grafia e as maiúsculas desejadas.

L1-R85. Julgue o item.
Uma equipe pretende medir o TER do ASR da Casa, no Azure Speech, usando como referência transcrições de sessões revisadas apenas quanto às palavras, sem pontuação nem letras maiúsculas. Nessa situação, a referência é adequada, ainda que não tenha esses elementos, pois o TER avalia o texto reconhecido contra as palavras da referência.

L1-R86. Julgue o item.
Na transcrição ao vivo de uma sessão com o Azure Speech, a segmentação semântica do reconhecimento contínuo devolve resultados finais apenas quando detecta silêncio prolongado, sem levar em conta a pontuação de fim de frase, que é irrelevante para o fechamento do segmento.

L1-R87. Julgue o item.
Considere que uma equipe pretenda fazer o Azure Speech escrever com iniciais maiúsculas o nome de um órgão, como Câmara dos Deputados, quando o texto reconhecido o apresentar em minúsculas. Nessa situação, deve cadastrar a regra no arquivo de formato de exibição personalizado do custom speech, na seção #itn, que se destina a trocar palavras por motivos como capitalização e correção de grafia.

L1-R88. Julgue o item.
Considere que uma equipe precise da forma lexical do texto reconhecido, sem pontuação e sem capitalização. Nessa situação, a API de transcrição rápida do Azure Speech não atende à necessidade, porque produz apenas a forma de exibição, ao contrário da API de transcrição em lote.

L1-R89. Julgue o item.
Uma equipe configura o reconhecimento de uma audiência pública para o português do Brasil, mas um convidado estrangeiro passa a falar em espanhol. Nessa situação, a acurácia da transcrição tende a diminuir no trecho em espanhol, pois o idioma configurado deve corresponder ao efetivamente falado no áudio.

L1-R90. Julgue o item.
Segundo a nota de transparência do Azure Speech, na captação do áudio do Plenário para o ASR, o microfone muito afastado do orador reduz a acurácia do reconhecimento, ao passo que o microfone muito próximo da boca a melhora, por captar a voz com mais nitidez.

L1-R91. Julgue o item.
Nos apartes, em que dois parlamentares falam ao mesmo tempo, a acurácia do ASR tende a cair, e há orientação de fornecedor segundo a qual pessoas que falam simultaneamente podem ser interpretadas como ruído de fundo e ignoradas, o que recomenda a conferência desses trechos pelo revisor.

L1-R92. Julgue o item.
Segundo a nota de transparência do Azure Speech, quando uma palavra que não existe no modelo aparece no áudio, o resultado é um erro de transcrição; por isso, siglas, jargões e nomes próprios específicos da Casa estão entre os termos mais sujeitos a erro e justificam o uso de listas de termos.

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
Segundo a documentação do Azure Speech, para siglas e outros termos da Casa cuja pronúncia não é a padrão, a personalização indicada é a de dados de pronúncia, que definem a forma fonética e a forma de exibição do termo, e não a de texto simples, que se destina ao vocabulário e à gramática específicos do setor.

L1-R100. Julgue o item.
Uma forma de orientar o Whisper de código aberto a grafar corretamente nomes próprios e termos específicos da Casa é fornecer, como prompt inicial da primeira janela, um texto com esse vocabulário, o que torna mais provável a grafia correta, mas não a garante.

L1-R101. Julgue o item.
Considere que a equipe monte o vocabulário personalizado do Amazon Transcribe para as audiências públicas e queira incluir, como uma única entrada, o nome Comissão de Constituição e Justiça. Nessa situação, deve separar as palavras da entrada por espaços, e não por hífen.

L1-R102. Julgue o item.
Segundo a documentação do Speech-to-Text do Google, ao atribuir valor de boost a uma frase de várias palavras, como o nome completo de um órgão da Casa, o peso incide também sobre cada trecho do nome, o que dispensa cadastrar como entradas adicionais as combinações de palavras que o compõem.

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

L1-R80. E [TS]. Na documentação, o Amazon Transcribe adiciona pontuação automaticamente em todos os idiomas suportados; a condição de haver suporte à transcrição de números diz respeito ao formato dos números (algarismos, e não palavras). O item atribui à pontuação a condição que vale para os números.
Base: AWS, Amazon Transcribe, Transcribing numbers and punctuation (https://docs.aws.amazon.com/transcribe/latest/dg/how-numbers.html), verificado em 18/10/2026: “Amazon Transcribe automatically adds punctuation to all supported languages”; “For most languages, numbers are transcribed into their word forms.”; “for languages with support for transcribing numbers, Amazon Transcribe treats numbers differently depending on the context in which they're used.”.
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

L1-R87. E [TS]. Na documentação do custom speech, a seção #rewrite do arquivo de formato de exibição reúne pares de reescrita para trocar palavras por motivos como capitalização e correção de grafia; a seção #itn traz padrões de exibição como números, endereços e datas. O item troca a seção.
Base: Microsoft, Azure Speech, Training and testing datasets (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-test-and-train), verificado em 18/10/2026: “A list of rewrite pairs to replace certain words for reasons such as capitalization and spelling correction.”; “A list of invert-text-normalization rules to define certain display patterns such as numbers, addresses, and dates.”; “Capitalize "Contoso" (via #rewrite rule)”.
Formato: SH (situação hipotética).
VOLÁTIL (baixo/médio): nome de seção de arquivo e condições de um recurso de serviço gerenciado (a própria página remete a lista de modelos base e locais com suporte: “For a list of supported base models and locales for training with structured text, see Language support.”); o item não afirma modelo nem idioma. REVERIFICAR em 4–8/1/2027; inapto a simulado final até lá.

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

L1-R99. C [TS]. A tabela de uso e tipo de dado do custom speech indica dados de pronúncia (ou pronúncia fonética em texto estruturado) para definir a forma fonética e a de exibição de termo de pronúncia não padrão, como siglas, e texto simples ou estruturado para vocabulário e gramática do setor. O item descreve corretamente o par que costuma ser invertido (falsa pegadinha).
Base: Microsoft, Azure Speech, Training and testing datasets (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-test-and-train), verificado em 18/10/2026: “Define the phonetic and displayed form of a word or term that has nonstandard pronunciation, such as product names or acronyms.”; “Pronunciation data or phonetic pronunciation in structured text”; “Improve recognition accuracy on industry-specific vocabulary and grammar, such as medical terminology or IT jargon.”; “Plain text or structured text data”.
Formato: D (definição).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R100. C. A documentação de transcribe() descreve initial_prompt como texto de contexto para a primeira janela, como vocabulários personalizados ou nomes próprios, para tornar mais provável a grafia correta. "Mais provável" não equivale a garantia.
Base: OpenAI, repositório oficial openai/whisper, whisper/transcribe.py (ramo main) (https://raw.githubusercontent.com/openai/whisper/main/whisper/transcribe.py), verificado em 18/10/2026: “Optional text to provide as a prompt for the first window.”; “to make it more likely to predict those word correctly.”.
Formato: AP (aplicação parlamentar).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R101. E [TS]. Na documentação do Amazon Transcribe, a entrada de várias palavras do vocabulário personalizado tem as palavras ligadas por hífen (como em Los-Angeles), e a coluna da tabela não admite espaços. O item troca o hífen pelo espaço.
Base: AWS, Amazon Transcribe, Creating a custom vocabulary using a list (https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-list.html), verificado em 18/10/2026: “If an entry contains multiple words, you must hyphenate each word.” | AWS, Amazon Transcribe, Creating a custom vocabulary using a table (https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-table.html), verificado em 18/10/2026: “Do not use spaces in this column. If your entry contains multiple words, separate each word with a hyphen (-).”.
Formato: SH (situação hipotética).
REVERIFICAR: conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL.

L1-R102. E [TS]. Segundo a documentação do Google, o boost atribuído a uma frase de várias palavras se aplica à frase inteira e somente a ela; para favorecer trechos, sugere-se acrescentar como entradas adicionais, cada uma com seu boost, os bigramas que a compõem. O item estende o peso aos trechos.
Base: Google Cloud, Speech-to-Text, Improve transcription results with model adaptation (https://docs.cloud.google.com/speech-to-text/docs/adaptation-model), verificado em 18/10/2026: “If you assign a boost value to a multi-word phrase, boost is applied to the entire phrase and only the entire phrase.”; “we suggest that you add all bigrams (2-words, in order) that make up the phrase as additional phrase items and assign boost values to each.”.
Formato: TS (troca de sujeito).
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
| formatos de P2-1.6 (20) | D 5; TS 5; SH 4; NP 0; PC 2; AP 4 |
| formatos dos 28 novos | D 6; TS 8; SH 6; NP 2; PC 0; AP 6 |
| extensão (palavras do enunciado) | C: média 45,1, mediana 45,5, de 25 a 57; E: média 44,9, mediana 44, de 35 a 63 |
| aritmética conferida por script | R76: 9 + 4 = 13; R82: (1 + 2 + 3) ÷ 80 = 7,5% |

## Lista de REVERIFICAR de janeiro (4–8/1/2027; T-11, parte P2, gce-cqfp)
- VOLÁTEIS: L1-R86, L1-R87, L1-R88.
- Conferência de base sem efeito de VOLÁTIL: L1-R75, L1-R76, L1-R77, L1-R78, L1-R79, L1-R80, L1-R81, L1-R82, L1-R83, L1-R84, L1-R85, L1-R89, L1-R90, L1-R91, L1-R92, L1-R93, L1-R94, L1-R95, L1-R96, L1-R97, L1-R98, L1-R99, L1-R100, L1-R101, L1-R102.
- Atenção especial: R100 tem base em arquivo de código do ramo main (whisper/transcribe.py, só o docstring de initial_prompt; SHA-256 do arquivo lido em 18/10/2026: 176f5ab30e961bec2a7872f5701a1f5bf3cbfc77946e50512f0f0cf00a1ceacf, 30.375 bytes), que muda mais que o README; na conferência de janeiro, comparar o SHA-256 e reabrir o trecho. R98 tem base em model-card.md do mesmo repositório. R87 (novo) é VOLÁTIL e depende da página de dados de treino do custom speech (data da página: 19/12/2025). R90 e R92 dependem de trechos da nota de transparência da Microsoft (data da página: 31/03/2026).

## Tabela de proveniência (todas as páginas abertas e lidas em 18/10/2026)
| fonte | URL oficial | data da página / verificação | usada em |
|---|---|---|---|
| AWS, Amazon Transcribe, How Amazon Transcribe works | https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works.html | sem data na página; verificado em 18/10/2026 | R75 |
| AWS, Amazon Transcribe, Transcribing numbers and punctuation | https://docs.aws.amazon.com/transcribe/latest/dg/how-numbers.html | sem data na página; verificado em 18/10/2026 | R78, R80 |
| AWS, Amazon Transcribe, Streaming and partial results | https://docs.aws.amazon.com/transcribe/latest/dg/streaming-partial-results.html | sem data na página; verificado em 18/10/2026 | R75, R79 |
| AWS, Amazon Transcribe, Creating a custom vocabulary using a table | https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-table.html | sem data na página; verificado em 18/10/2026 | R84, R101 |
| AWS, Amazon Transcribe, Creating a custom vocabulary using a list | https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary-create-list.html | sem data na página; verificado em 18/10/2026 | R101 |
| Google Cloud, Speech-to-Text, Enable automatic punctuation | https://docs.cloud.google.com/speech-to-text/docs/automatic-punctuation | Last updated 2026-10-13 UTC; verificado em 18/10/2026 | R76 |
| Google Cloud, Speech-to-Text, Improve transcription results with model adaptation | https://docs.cloud.google.com/speech-to-text/docs/adaptation-model | Last updated 2026-10-13 UTC; verificado em 18/10/2026 | R97, R102 |
| Google Cloud, Speech-to-Text, Best practices | https://docs.cloud.google.com/speech-to-text/docs/best-practices | Last updated 2026-10-13 UTC; verificado em 18/10/2026 | R91 |
| Microsoft, Azure Speech, Display text formatting with speech to text | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/display-text-format | Last updated on 2025-12-29; verificado em 18/10/2026 | R77, R83 |
| Microsoft, Azure Speech, Test accuracy of a custom speech model | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | Last updated on 2025-12-29; verificado em 18/10/2026 | R81, R82, R85, R93, R95, R102 |
| Microsoft, Azure Speech, What is custom speech? | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-speech-overview | Last updated on 2026-02-25; verificado em 18/10/2026 | R96 |
| Microsoft, Azure Speech, Training and testing datasets | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-test-and-train | Last updated on 2025-12-19; verificado em 18/10/2026 | R87, R99 |
| Microsoft, Azure Speech, Improve recognition accuracy with phrase list | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/improve-accuracy-phrase-list | Last updated on 2026-06-29; verificado em 18/10/2026 | R94 |
| Microsoft, Azure Speech, Transparency note for speech to text | https://learn.microsoft.com/en-us/legal/cognitive-services/speech-service/speech-to-text/transparency-note | Last updated on 2026-03-31; verificado em 18/10/2026 | R89, R90, R91, R92, R94 |
| Microsoft, Azure Speech, Create a batch transcription | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription-create | Last updated on 2026-04-03; verificado em 18/10/2026 | R87 |
| Microsoft, Azure Speech, Use the fast transcription API | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/fast-transcription-create | Last updated on 2026-04-08; verificado em 18/10/2026 | R88 |
| Microsoft, Azure Speech, How to recognize speech | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech | Last updated on 2026-06-05; verificado em 18/10/2026 | R86 |
| OpenAI, repositório oficial openai/whisper, model-card.md (ramo main) | https://raw.githubusercontent.com/openai/whisper/main/model-card.md | arquivo aberto e lido em 18/10/2026 (HTTP 200); verificado em 18/10/2026 | R98 |
| OpenAI, repositório oficial openai/whisper, whisper/transcribe.py (ramo main) | https://raw.githubusercontent.com/openai/whisper/main/whisper/transcribe.py | arquivo aberto e lido em 18/10/2026 (HTTP 200); SHA-256 do arquivo lido: 176f5ab30e961bec2a7872f5701a1f5bf3cbfc77946e50512f0f0cf00a1ceacf; verificado em 18/10/2026 | R100 |

Fontes não abertas: nenhuma fonte necessária deixou de abrir. Não foram tentados, por estarem fora dos hosts liberados, github.com (a página e a API, motivo de o commit do transcribe.py não ter sido registrado: ver SHA-256 na tabela), openai.com, arxiv.org, w3.org e huggingface.co; nenhum item depende deles. O README do Whisper, base do R101 da v1, deixou de ser base desta parte. Duas URLs de cartão de IA responsável da AWS retornaram 404 e não foram usadas. planalto.gov.br, Legin e camara.leg.br não foram consultados (nenhuma norma citada).

Dúvidas para a Gerência titular e a QA:
1. VOLÁTIL de R86, R87 e R88: classificados S (baixo/médio) por dependerem de existência e condições de recurso de produto (segmentação semântica; seção #rewrite × #itn do formato de exibição personalizado, no R87 substituto; capacidade da API de transcrição rápida). Se a Gerência os tratar como não VOLÁTEIS, nada muda no teto; se tratar outros como VOLÁTEIS, 1.5 tem folga até 4 de 20.
2. R100 usa como base o docstring de transcribe() no repositório oficial do Whisper (código, não documentação em prosa; a QA já aceitou como documentação do fornecedor). O model-card sustenta R98. Se a Gerência entender o contrário, só o R100 cai. Nenhum item desta parte depende mais de valores padrão da assinatura do código.
3. R83: a oração "independentemente de ter sido citada como assunto" é consequência lógica do modo de ditado (a palavra é interpretada como sinal), não frase literal da documentação; a base literal sustenta a interpretação de descrições verbais de pontuação.
4. R90: a documentação do Google recomenda o microfone o mais próximo possível do falante; o item se apoia na nota da Microsoft ("too close" também prejudica) e fala de microfone "muito próximo da boca". A QA pode conferir se a redação evita conflito entre as duas orientações.
5. TER em 1.5: três itens (R81, R82, R85); ver seção 3 da Parte 1.

FIM DA PARTE 3/3
FIM DO LOTE
