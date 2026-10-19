# T111_resumos_P2_A2_v1.md — T-111 parte A2 (P2-1.1, 1.2, 1.3, 1.5, 1.6, 1.7, 1.8) — produção gce-cpp — 2026-10-18

**Base.** Pacote v1.11 (`saida/pacote/pacote.json`). Fonte única: curso do próprio tópico, `lotes[].curso` de L1 segmentado por `## ` (1.1 = bloco 1, 1.2 = bloco 2, 1.3 = bloco 3, 1.5 = bloco 5, 1.6 = bloco 6, 1.7 = bloco 7, 1.8 = bloco 8; o 1.4 já está na A1). Regra de tamanho e forma: seção 2.1 da D1 da GCE (120 a 300 palavras e até 50% do curso; 3 a 6 parágrafos de 25 a 80 palavras; texto corrido; nenhum parágrafo começa por algarismo ou por maiúsculas seguidas de dois-pontos). Contagem por script (palavras separadas por espaço). Calibração pela A1 e pelo seu parecer: ressalvas do bloco mantidas, base legal só com o dispositivo do bloco, sem nota de processo de produção, um parágrafo por ideia, nada mais forte que o curso. Datas de verificação, URLs e identificadores de fonte do bloco foram omitidos por serem referência de produção. Nenhum fato fora do bloco.

## P2-1.1

**Contagens.** Curso 376 palavras; teto efetivo 188; resumo 188 palavras; 4 parágrafos (40, 40, 57, 51).

**Resumo.**

O ASR, reconhecimento automático de fala, converte áudio com fala em texto e só faz isso. Não decide quem falou, tarefa da diarização ou da identificação de locutor, nem o que o texto significa, tarefa da compreensão de linguagem natural.

O pipeline clássico é modular: pré-processamento, modelo acústico, léxico de pronúncia, modelo de linguagem e decodificador, que escolhe a hipótese de texto mais provável. Nos sistemas modernos uma rede única funde essas etapas, mas as funções continuam existindo por dentro.

A métrica central é o WER: substituições mais deleções mais inserções, divididas pelo número de palavras da referência humana; quanto menor, melhor. Como as inserções entram só no numerador, o WER pode ultrapassar 100%. No cálculo usual, sobre texto normalizado, não mede pontuação nem capitalização, e a atribuição de locutor fica fora do WER em qualquer convenção.

A banca tende a atribuir ao ASR funções de outros módulos, como identificar o orador, interpretar o sentido ou corrigir o conteúdo, quando ASR é transcrição literal. Também erra dizer que o WER varia só de 0% a 100%, ou que WER de 0% prova transcrição perfeita em todos os aspectos.

**Relatório por parágrafo (ideia | frase do bloco).**

1. ASR só converte fala em texto | "Faz apenas isso: fala → texto. Não decide quem falou ... nem o que o texto significa"
2. Pipeline clássico modular e fusão moderna | "Pipeline clássico (modular)"; "Nos sistemas modernos (item 1.2) essas etapas são fundidas em uma rede única, mas as funções continuam existindo 'por dentro'."
3. WER: fórmula, pode passar de 100%, limites | "Métrica central: WER (Word Error Rate) = (S + D + I) / N"; "o WER PODE ultrapassar 100%"; "a atribuição de locutor fica fora do WER em qualquer convenção"
4. Pegadinhas: funções de outros módulos e WER | "A banca tende a atribuir ao ASR funções que são de outros módulos"; "WER 'varia de 0% a 100%'. Errado"; "WER de 0% como prova de transcrição 'perfeita'"

## P2-1.2

**Contagens.** Curso 346 palavras; teto efetivo 173; resumo 172 palavras; 3 parágrafos (57, 54, 61).

**Resumo.**

Modelo end-to-end é aquele em que uma única rede neural é treinada para mapear diretamente o áudio ao texto, no lugar de modelo acústico, léxico e modelo de linguagem construídos separadamente. As famílias mais citadas são CTC, RNN-Transducer e codificador-decodificador com atenção; o Whisper, da OpenAI, é um codificador-decodificador Transformer treinado com supervisão fraca em larga escala.

Há equívocos sobre o que end-to-end significa. Não significa ausência de dados rotulados, pois continua precisando de pares áudio-texto; nem de modelo de linguagem, cujo conhecimento fica implícito na rede; nem de pré-processamento, já que em geral o áudio vira espectrograma antes de entrar, embora haja modelos que recebem a forma de onda bruta.

As vantagens são simplicidade de treinamento, melhor desempenho com muitos dados e menos engenharia manual de pronúncia. Os custos são a exigência de grande volume de dados e a dificuldade de consertar pontualmente, pois não há dicionário para editar. Os erros podem ser fluentes porém falsos, de modo que afirmar que nunca alucinam ou sempre superam os modulares é generalização indevida.

**Relatório por parágrafo (ideia | frase do bloco).**

1. Definição e famílias; Whisper | "uma única rede neural é treinada para mapear diretamente o áudio ao texto"; "O Whisper, da OpenAI, é um codificador-decodificador Transformer treinado com supervisão fraca em larga escala"
2. O que end-to-end não significa | "O que 'end-to-end' NÃO significa:" (sem dados rotulados; sem modelo de linguagem; sem pré-processamento)
3. Vantagens, custos e generalizações indevidas | "Vantagens: simplicidade de treinamento..."; "erros podem ser fluentes porém falsos"; "afirmar que modelos end-to-end 'nunca alucinam' ou que 'sempre superam' os modulares"

## P2-1.3

**Contagens.** Curso 555 palavras; teto efetivo 277; resumo 265 palavras; 5 parágrafos (65, 46, 43, 51, 60).

**Resumo.**

Um LLM multimodal de áudio nativo recebe o áudio como entrada do próprio modelo, e em alguns casos produz áudio como saída, sem depender de um módulo ASR separado que converta a fala em texto antes. O contraste é a arquitetura em cascata, ASR, LLM sobre texto e síntese de voz, em que o LLM só vê texto e perde entonação, hesitação, sobreposição e risos.

A categoria existe comercialmente. A OpenAI distingue áudio em Chat Completions, a Realtime API para agentes fala-a-fala e endpoints dedicados de transcrição de arquivo e ao vivo. A documentação do Google descreve o áudio como entrada dos modelos Gemini para transcrição, sumarização e análise por timestamp.

ASR aprimorado por LLM é outra categoria. O LLM speech do Azure AI Speech transcreve ou traduz áudio pré-gravado, com qualidade e contexto reforçados por LLM, mas não é um LLM de áudio nativo conversacional. Usar LLM não é sinônimo de áudio nativo.

Na transcrição parlamentar, o modelo nativo pode transcrever, resumir e responder perguntas sobre o áudio na mesma passada, mas corre o risco de transcrição interpretativa: por gerar texto plausível, pode normalizar, completar ou omitir trechos. Para registro oficial, isso exige revisão humana, e o resultado continua sendo geração, não cópia fiel.

A banca pode dizer que a cascata preserva prosódia, quando o LLM da cascata só recebe texto, ou que o LLM nativo elimina a revisão humana. Pode confundir transcrição por LLM com ASR dedicado, pois a OpenAI recomenda endpoint dedicado para arquivos e LLM ou Realtime para conversação. Nomes e versões mudam em meses; cobra-se o conceito, não o produto.

**Relatório por parágrafo (ideia | frase do bloco).**

1. Definição e contraste com a cascata | "recebe o áudio como modalidade de ENTRADA do próprio modelo ... sem que o fluxo dependa de um módulo ASR separado"; "arquitetura EM CASCATA: ASR → LLM (texto) → TTS"
2. Categoria existe comercialmente (OpenAI, Google) | "Evidência de que a categoria existe comercialmente:" (OpenAI: Audio in Chat Completions, Realtime API, endpoints dedicados; Google: Audio understanding)
3. ASR aprimorado por LLM não é áudio nativo | "o 'LLM speech' do Azure AI Speech é um exemplo de outra categoria"; "'usa LLM' não é sinônimo de 'áudio nativo'"
4. Transcrição interpretativa e revisão humana | "O preço é o risco de 'transcrição interpretativa'"; "o resultado continua sendo uma GERAÇÃO, não uma cópia fiel"
5. Pegadinhas prováveis | "PEGADINHA PROVÁVEL (1) Dizer que a cascata 'preserva prosódia'"; (2), (3), (5) "a banca pode cobrar o CONCEITO, não o nome do produto"

## P2-1.5

**Contagens.** Curso 297 palavras; teto efetivo 148; resumo 148 palavras; 4 parágrafos (32, 48, 25, 43).

**Resumo.**

A saída crua de muitos sistemas ASR é texto em minúsculas e sem pontuação, porque o modelo aprende sons, não sinais gráficos. Pontuação automática e capitalização restauram vírgulas, pontos, interrogações e maiúsculas.

Há duas formas de obtê-las. No pós-processamento, um modelo separado lê o texto cru, às vezes com pistas de pausa ou prosódia, e insere os sinais. Na geração direta, modelos end-to-end já emitem texto pontuado e capitalizado; no chirp_3 isso é gerado pelo modelo e pode ser desativado.

Pontuação falada é recurso diferente: o orador dita "vírgula" ou "ponto" e o sistema converte a palavra no sinal. Serve para ditado, não para sessões.

A pontuação automática é inferida da estrutura da frase e da entonação, não ouvida, e uma interrogação indevida muda o sentido, como em "Aprovado." e "Aprovado?"; por isso a revisão humana confere pontuação, não só palavras. A capitalização estima nomes próprios, sem certeza.

**Relatório por parágrafo (ideia | frase do bloco).**

1. Saída crua e função da camada | "A saída 'crua' de muitos sistemas ASR é texto em minúsculas e sem pontuação, porque o modelo aprende sons, não sinais gráficos."
2. Pós-processamento e geração direta | "Duas formas de obter isso: 1. Pós-processamento ... 2. Geração direta"; "No chirp_3, pontuação e capitalização automáticas são geradas pelo modelo e podem ser desativadas"
3. Pontuação falada é recurso diferente | "Recurso DIFERENTE: 'pontuação falada' (spoken punctuation)"; "Isso serve para ditado, não para sessões."
4. Inferência, revisão humana e capitalização | "A interrogação não foi 'ouvida': foi inferida da estrutura da frase e da entonação"; "capitalização automática ... ela estima"

## P2-1.6

**Contagens.** Curso 495 palavras; teto efetivo 247; resumo 220 palavras; 4 parágrafos (63, 61, 54, 42).

**Resumo.**

O ASR em português brasileiro enfrenta seis desafios: variação regional e social, com perda de acurácia nos padrões menos treinados; vocabulário técnico e parlamentar, em que palavras raras são trocadas por comuns de som parecido; condições acústicas do plenário; números, datas e abreviaturas, que exigem normalização; fala espontânea; e desequilíbrio de dados, pois há muito menos áudio transcrito em pt-BR que em inglês.

Cada fornecedor chama a mitigação de um modo. O Google usa speech adaptation, e o chirp_3 aceita até 1.000 frases, com recomendação de poucas entradas. A AWS tem custom vocabulary e custom language model, este treinado com texto do domínio e indisponível para pt-BR na tabela oficial. O Azure tem custom speech, e a OpenAI, os parâmetros prompt, keywords e languages.

A adaptação de vocabulário é viés de reconhecimento: empurra o decodificador para termos esperados, não é retreinamento acústico e não garante acerto em qualquer condição. Sotaque se trata com dados acústicos, não com lista de palavras. Carregar nomes de deputados e siglas reduz erros como PEC virar pec, mas não o erro de sotaque.

A banca pode igualar custom vocabulary a retreinamento, dizer que o CLM da AWS se treina com áudio, quando é com texto, afirmar que modelos multilíngues eliminam o problema do pt-BR ou que lista de termos garante reconhecimento em qualquer condição acústica.

**Relatório por parágrafo (ideia | frase do bloco).**

1. Seis desafios do pt-BR | "DEFINIÇÃO / MAPA DOS DESAFIOS" itens 1 a 6 (variação regional, vocabulário técnico, condições acústicas, números, fala espontânea, desequilíbrio de dados)
2. Mitigação por fornecedor | "FERRAMENTAS DE MITIGAÇÃO (o que cada fornecedor chama de quê)": Google, AWS (CLM indisponível para pt-BR), Azure, OpenAI
3. Adaptação é viés, não retreinamento | "Distinção decisiva: adaptação de vocabulário é VIÉS de reconhecimento"; "Sotaque se trata com dados acústicos ... não com lista de palavras"; exemplo parlamentar
4. Pegadinhas prováveis | "Igualar custom vocabulary a retreinamento; dizer que CLM se treina com áudio (no AWS é com texto)..."

## P2-1.7

**Contagens.** Curso 355 palavras; teto efetivo 177; resumo 176 palavras; 4 parágrafos (34, 53, 48, 41).

**Resumo.**

Transcrição em tempo real, ou streaming, processa o áudio enquanto ele chega, em pequenos blocos, devolvendo texto com atraso de segundos. Na transcrição em lote, o áudio completo já existe e é processado inteiro.

No streaming há resultados parciais, que podem mudar, e finais, em geral consolidados quando se detecta fim de enunciado. O endpointing decide, geralmente por silêncio, que o orador terminou a frase: sensibilidade maior responde mais rápido, mas arrisca cortar o orador. A estabilização de parciais reduz as idas e vindas do texto exibido.

Recursos podem faltar em streaming, e isso varia por fornecedor: não há diarização em StreamingRecognize do chirp_3 nem nas sessões Realtime da OpenAI, mas há no Amazon Transcribe. Streaming de saída não é tempo real: na OpenAI, stream=true devolve o texto aos poucos, mas de um arquivo completo.

A legenda ao vivo da TV Câmara tolera correção de texto parcial; notas taquigráficas oficiais convêm melhor em lote, com diarização e revisão. Streaming não é sempre mais preciso, pois o lote vê contexto completo, nem oferece necessariamente os mesmos recursos.

**Relatório por parágrafo (ideia | frase do bloco).**

1. Streaming x lote | "processa o áudio ENQUANTO ele chega"; "Em oposição: transcrição em lote (batch/arquivo)"
2. Parciais, finais, endpointing, estabilização | "resultados PARCIAIS/intermediários ... e resultados FINAIS"; "endpointing"; "estabilização de resultados parciais"
3. Recursos que variam e streaming de saída | "recursos que podem não existir em streaming — e isso varia por fornecedor"; "'streaming de SAÍDA' ≠ 'tempo real'"
4. Legenda ao vivo x notas e pegadinhas | "Legenda ao vivo da sessão na TV Câmara: streaming com baixa latência"; "'Streaming é sempre mais preciso' (não; batch vê contexto completo)"

## P2-1.8

**Contagens.** Curso 920 palavras; teto efetivo 300; resumo 277 palavras; 5 parágrafos (55, 60, 46, 54, 62).

**Resumo.**

O conteúdo sobre ferramentas é retrato de um momento: nomes de modelo e limites mudam, e a prova tende a cobrar a categoria de recurso, como batch ou streaming, diarização, vocabulário, idioma e execução local. O edital grafa Whisper (Open AI), mas a grafia oficial do fornecedor é OpenAI, o que não afeta o julgamento.

O Whisper tem código e pesos publicados no GitHub sob licença MIT e pode rodar localmente, sem enviar áudio a terceiros, o que importa para dados sensíveis. Na API, o whisper-1 serve para timestamps, formatos de legenda e tradução apenas para o inglês, e a OpenAI recomenda hoje outros modelos para transcrição geral, rótulos de locutor e áudio ao vivo.

O Google Cloud Speech-to-Text usa o modelo chirp_3, exclusivo da API V2, com três métodos: StreamingRecognize para tempo real, Recognize para áudio curto e BatchRecognize para longo. Há pt-BR em disponibilidade geral, diarização com pt-BR suportado mas não em StreamingRecognize, e adaptação com até 1.000 frases.

O Azure AI Speech oferece transcrição em tempo real, fast transcription para arquivo e transcrição em lote, custom speech, diarização documentada em tempo real e na fast transcription, e execução em nuvem ou em contêineres on-premises. O Amazon Transcribe oferece batch e streaming, com pt-BR em ambos, custom vocabulary e diarização inclusive em streaming.

A banca tende a trocar o modo em que um recurso existe, como diarização em streaming ou em lote; atribuir código aberto à API, quando o aberto é o modelo Whisper; afirmar limites ou preços sem data; dizer que a tradução do whisper-1 é para qualquer idioma; e tratar modelo local e serviço em nuvem como equivalentes quanto à custódia do áudio.

**Relatório por parágrafo (ideia | frase do bloco).**

1. Regra de leitura e grafia do edital | "tudo abaixo é retrato de 07/10/2026 ... O que a prova tende a cobrar é a CATEGORIA de recurso"; "o edital grafa 'Whisper (Open AI)'"
2. Whisper: aberto, local, whisper-1 | "Modelo de código aberto ... sob licença MIT; pode ser executado localmente"; "whisper-1 é indicado quando se precisa de timestamps ... tradução para o inglês"
3. Google Cloud Speech-to-Text | "Modelo atual: chirp_3, exclusivo da API V2"; "Três métodos"; "Diarização: não há diarização em StreamingRecognize; pt-BR suportado"
4. Azure AI Speech e Amazon Transcribe | "Modos: transcrição em tempo real ..., 'fast transcription' ... e transcrição em lote"; "Modos batch ... e streaming"; "diarização, inclusive em streaming (ShowSpeakerLabel)"
5. Pegadinhas prováveis | "Trocar o modo em que um recurso existe"; "atribuir 'código aberto' à API"; "tratar modelo local e serviço em nuvem como equivalentes quanto à custódia do áudio"

## Contagens da parte

| Tópico | Curso | Teto efetivo | Resumo | Parágrafos |
|---|--:|--:|--:|--:|
| P2-1.1 | 376 | 188 | 188 | 4 |
| P2-1.2 | 346 | 173 | 172 | 3 |
| P2-1.3 | 555 | 277 | 265 | 5 |
| P2-1.5 | 297 | 148 | 148 | 4 |
| P2-1.6 | 495 | 247 | 220 | 4 |
| P2-1.7 | 355 | 177 | 176 | 4 |
| P2-1.8 | 920 | 300 | 277 | 5 |

7 tópicos; todos dentro de 120 a 300 palavras, do teto de 50% do curso e de 3 a 6 parágrafos de 25 a 80 palavras.

## Bloco JSON

```json
{
 "topicos": {
  "P2-1.1": {
   "resumo": "O ASR, reconhecimento automático de fala, converte áudio com fala em texto e só faz isso. Não decide quem falou, tarefa da diarização ou da identificação de locutor, nem o que o texto significa, tarefa da compreensão de linguagem natural.\n\nO pipeline clássico é modular: pré-processamento, modelo acústico, léxico de pronúncia, modelo de linguagem e decodificador, que escolhe a hipótese de texto mais provável. Nos sistemas modernos uma rede única funde essas etapas, mas as funções continuam existindo por dentro.\n\nA métrica central é o WER: substituições mais deleções mais inserções, divididas pelo número de palavras da referência humana; quanto menor, melhor. Como as inserções entram só no numerador, o WER pode ultrapassar 100%. No cálculo usual, sobre texto normalizado, não mede pontuação nem capitalização, e a atribuição de locutor fica fora do WER em qualquer convenção.\n\nA banca tende a atribuir ao ASR funções de outros módulos, como identificar o orador, interpretar o sentido ou corrigir o conteúdo, quando ASR é transcrição literal. Também erra dizer que o WER varia só de 0% a 100%, ou que WER de 0% prova transcrição perfeita em todos os aspectos."
  },
  "P2-1.2": {
   "resumo": "Modelo end-to-end é aquele em que uma única rede neural é treinada para mapear diretamente o áudio ao texto, no lugar de modelo acústico, léxico e modelo de linguagem construídos separadamente. As famílias mais citadas são CTC, RNN-Transducer e codificador-decodificador com atenção; o Whisper, da OpenAI, é um codificador-decodificador Transformer treinado com supervisão fraca em larga escala.\n\nHá equívocos sobre o que end-to-end significa. Não significa ausência de dados rotulados, pois continua precisando de pares áudio-texto; nem de modelo de linguagem, cujo conhecimento fica implícito na rede; nem de pré-processamento, já que em geral o áudio vira espectrograma antes de entrar, embora haja modelos que recebem a forma de onda bruta.\n\nAs vantagens são simplicidade de treinamento, melhor desempenho com muitos dados e menos engenharia manual de pronúncia. Os custos são a exigência de grande volume de dados e a dificuldade de consertar pontualmente, pois não há dicionário para editar. Os erros podem ser fluentes porém falsos, de modo que afirmar que nunca alucinam ou sempre superam os modulares é generalização indevida."
  },
  "P2-1.3": {
   "resumo": "Um LLM multimodal de áudio nativo recebe o áudio como entrada do próprio modelo, e em alguns casos produz áudio como saída, sem depender de um módulo ASR separado que converta a fala em texto antes. O contraste é a arquitetura em cascata, ASR, LLM sobre texto e síntese de voz, em que o LLM só vê texto e perde entonação, hesitação, sobreposição e risos.\n\nA categoria existe comercialmente. A OpenAI distingue áudio em Chat Completions, a Realtime API para agentes fala-a-fala e endpoints dedicados de transcrição de arquivo e ao vivo. A documentação do Google descreve o áudio como entrada dos modelos Gemini para transcrição, sumarização e análise por timestamp.\n\nASR aprimorado por LLM é outra categoria. O LLM speech do Azure AI Speech transcreve ou traduz áudio pré-gravado, com qualidade e contexto reforçados por LLM, mas não é um LLM de áudio nativo conversacional. Usar LLM não é sinônimo de áudio nativo.\n\nNa transcrição parlamentar, o modelo nativo pode transcrever, resumir e responder perguntas sobre o áudio na mesma passada, mas corre o risco de transcrição interpretativa: por gerar texto plausível, pode normalizar, completar ou omitir trechos. Para registro oficial, isso exige revisão humana, e o resultado continua sendo geração, não cópia fiel.\n\nA banca pode dizer que a cascata preserva prosódia, quando o LLM da cascata só recebe texto, ou que o LLM nativo elimina a revisão humana. Pode confundir transcrição por LLM com ASR dedicado, pois a OpenAI recomenda endpoint dedicado para arquivos e LLM ou Realtime para conversação. Nomes e versões mudam em meses; cobra-se o conceito, não o produto."
  },
  "P2-1.5": {
   "resumo": "A saída crua de muitos sistemas ASR é texto em minúsculas e sem pontuação, porque o modelo aprende sons, não sinais gráficos. Pontuação automática e capitalização restauram vírgulas, pontos, interrogações e maiúsculas.\n\nHá duas formas de obtê-las. No pós-processamento, um modelo separado lê o texto cru, às vezes com pistas de pausa ou prosódia, e insere os sinais. Na geração direta, modelos end-to-end já emitem texto pontuado e capitalizado; no chirp_3 isso é gerado pelo modelo e pode ser desativado.\n\nPontuação falada é recurso diferente: o orador dita \"vírgula\" ou \"ponto\" e o sistema converte a palavra no sinal. Serve para ditado, não para sessões.\n\nA pontuação automática é inferida da estrutura da frase e da entonação, não ouvida, e uma interrogação indevida muda o sentido, como em \"Aprovado.\" e \"Aprovado?\"; por isso a revisão humana confere pontuação, não só palavras. A capitalização estima nomes próprios, sem certeza."
  },
  "P2-1.6": {
   "resumo": "O ASR em português brasileiro enfrenta seis desafios: variação regional e social, com perda de acurácia nos padrões menos treinados; vocabulário técnico e parlamentar, em que palavras raras são trocadas por comuns de som parecido; condições acústicas do plenário; números, datas e abreviaturas, que exigem normalização; fala espontânea; e desequilíbrio de dados, pois há muito menos áudio transcrito em pt-BR que em inglês.\n\nCada fornecedor chama a mitigação de um modo. O Google usa speech adaptation, e o chirp_3 aceita até 1.000 frases, com recomendação de poucas entradas. A AWS tem custom vocabulary e custom language model, este treinado com texto do domínio e indisponível para pt-BR na tabela oficial. O Azure tem custom speech, e a OpenAI, os parâmetros prompt, keywords e languages.\n\nA adaptação de vocabulário é viés de reconhecimento: empurra o decodificador para termos esperados, não é retreinamento acústico e não garante acerto em qualquer condição. Sotaque se trata com dados acústicos, não com lista de palavras. Carregar nomes de deputados e siglas reduz erros como PEC virar pec, mas não o erro de sotaque.\n\nA banca pode igualar custom vocabulary a retreinamento, dizer que o CLM da AWS se treina com áudio, quando é com texto, afirmar que modelos multilíngues eliminam o problema do pt-BR ou que lista de termos garante reconhecimento em qualquer condição acústica."
  },
  "P2-1.7": {
   "resumo": "Transcrição em tempo real, ou streaming, processa o áudio enquanto ele chega, em pequenos blocos, devolvendo texto com atraso de segundos. Na transcrição em lote, o áudio completo já existe e é processado inteiro.\n\nNo streaming há resultados parciais, que podem mudar, e finais, em geral consolidados quando se detecta fim de enunciado. O endpointing decide, geralmente por silêncio, que o orador terminou a frase: sensibilidade maior responde mais rápido, mas arrisca cortar o orador. A estabilização de parciais reduz as idas e vindas do texto exibido.\n\nRecursos podem faltar em streaming, e isso varia por fornecedor: não há diarização em StreamingRecognize do chirp_3 nem nas sessões Realtime da OpenAI, mas há no Amazon Transcribe. Streaming de saída não é tempo real: na OpenAI, stream=true devolve o texto aos poucos, mas de um arquivo completo.\n\nA legenda ao vivo da TV Câmara tolera correção de texto parcial; notas taquigráficas oficiais convêm melhor em lote, com diarização e revisão. Streaming não é sempre mais preciso, pois o lote vê contexto completo, nem oferece necessariamente os mesmos recursos."
  },
  "P2-1.8": {
   "resumo": "O conteúdo sobre ferramentas é retrato de um momento: nomes de modelo e limites mudam, e a prova tende a cobrar a categoria de recurso, como batch ou streaming, diarização, vocabulário, idioma e execução local. O edital grafa Whisper (Open AI), mas a grafia oficial do fornecedor é OpenAI, o que não afeta o julgamento.\n\nO Whisper tem código e pesos publicados no GitHub sob licença MIT e pode rodar localmente, sem enviar áudio a terceiros, o que importa para dados sensíveis. Na API, o whisper-1 serve para timestamps, formatos de legenda e tradução apenas para o inglês, e a OpenAI recomenda hoje outros modelos para transcrição geral, rótulos de locutor e áudio ao vivo.\n\nO Google Cloud Speech-to-Text usa o modelo chirp_3, exclusivo da API V2, com três métodos: StreamingRecognize para tempo real, Recognize para áudio curto e BatchRecognize para longo. Há pt-BR em disponibilidade geral, diarização com pt-BR suportado mas não em StreamingRecognize, e adaptação com até 1.000 frases.\n\nO Azure AI Speech oferece transcrição em tempo real, fast transcription para arquivo e transcrição em lote, custom speech, diarização documentada em tempo real e na fast transcription, e execução em nuvem ou em contêineres on-premises. O Amazon Transcribe oferece batch e streaming, com pt-BR em ambos, custom vocabulary e diarização inclusive em streaming.\n\nA banca tende a trocar o modo em que um recurso existe, como diarização em streaming ou em lote; atribuir código aberto à API, quando o aberto é o modelo Whisper; afirmar limites ou preços sem data; dizer que a tradução do whisper-1 é para qualquer idioma; e tratar modelo local e serviço em nuvem como equivalentes quanto à custódia do áudio."
  }
 }
}
```

FIM DO ARQUIVO
