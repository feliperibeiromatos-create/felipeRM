# Lote 1 — Reconhecimento de Fala e Transcrição de Áudio (P2 1.1–1.8)

Prova: P2

## Itens do edital

- P2-1.1 — Reconhecimento automático de fala (ASR – Automatic Speech Recognition)
- P2-1.2 — Modelos de fala end-to-end
- P2-1.3 — LLMs multimodais de áudio nativo
- P2-1.4 — Diarização de falantes: identificação e separação de múltiplos oradores
- P2-1.5 — Pontuação automática e capitalização em transcrições
- P2-1.6 — Desafios do ASR em Português Brasileiro: sotaques, vocabulário técnico e parlamentar
- P2-1.7 — Transcrição em tempo real
- P2-1.8 — Ferramentas e APIs: Whisper (Open AI), Google Speech-to-text, Azure Speech, AWS Transcribe

## Resumo

```text
ASR converte fala em texto; só isso. Métrica: WER = (S+D+I)/N, pode
passar de 100%; no cálculo usual, sobre texto normalizado, não mede pontuação nem capitalização; locutor fica fora do WER em qualquer convenção. Pipeline clássico:
features → modelo acústico → léxico → modelo de linguagem →
decodificador.
END-TO-END: uma rede única áudio→texto, treinada conjuntamente; famílias
CTC, RNN-T, encoder-decoder com atenção (Whisper, supervisão fraca em
larga escala). Ainda precisa de dados rotulados; não dispensa modelo de
linguagem (fica implícito); erros podem ser fluentes e falsos.
LLM DE ÁUDIO NATIVO: áudio entra direto no LLM (sem ASR separado);
oposto da CASCATA ASR→LLM→TTS, que perde prosódia. Faz transcrever +
resumir + responder, mas gera texto plausível: exige revisão humana.
Exemplos documentados: OpenAI (Audio in Chat Completions, Realtime,
GPT-Live), Google Gemini (audio understanding, 32 tokens/s). "ASR
aprimorado por LLM" (Azure LLM speech) é outra categoria.
DIARIZAÇÃO: "quem falou quando" com rótulos genéricos; ≠ identificação
(quem é, com cadastro) ≠ verificação (1:1). Etapas: VAD → segmentação →
embeddings → clustering. Métrica DER (≠ WER). Limites: sobreposição,
vozes parecidas; disponibilidade em streaming varia (não no chirp_3 nem
na Realtime da OpenAI; sim na AWS).
PONTUAÇÃO/CAPITALIZAÇÃO: inferidas (pós-processamento ou geradas pelo
modelo end-to-end); ≠ pontuação falada (ditada). Erro de pontuação muda
sentido em ata.
PT-BR: sotaques, siglas/nomes/regimento, acústica de plenário, números,
fala espontânea, menos dados. Mitigação: adaptação/custom vocabulary
(viés, não retreino), CLM (texto; indisponível para pt-BR na AWS), custom speech (acústico+linguagem+
pronúncia), prompt/keywords. Sotaque pede dados acústicos.
TEMPO REAL: blocos de áudio, parciais revisáveis, finais; endpointing
(rápido vs cortar orador); nem todo recurso existe em streaming e isso
varia por fornecedor; stream=true em arquivo não é tempo real.
FERRAMENTAS (07/10/2026): Whisper = modelo aberto (MIT), roda local, 98
idiomas; API OpenAI recomenda gpt-transcribe, whisper-1 para timestamps/
legendas/tradução p/ inglês, 25 MB. Google = chirp_3 (V2), 3 métodos,
pt-BR GA, sem diarização em streaming, adaptação ≤1.000 frases. Azure =
real-time, fast, batch, custom speech, diarização em tempo real e fast,
contêiner on-prem, LLM speech preview. AWS = batch + streaming, pt-BR,
custom vocabulary, CLM sem pt-BR, filtro, PII, diarização (inclusive
streaming), timestamps; language ID em streaming não combina com CLM/
redação.
```

## Curso

```text
## 1.1 RECONHECIMENTO AUTOMÁTICO DE FALA (ASR)

DEFINIÇÃO
ASR (Automatic Speech Recognition) é a tarefa computacional de converter
um sinal de áudio contendo fala em uma sequência de texto. Faz apenas
isso: fala → texto. Não decide quem falou (isso é diarização/identificação de locutor) nem o que o texto significa (isso é compreensão de
linguagem natural).

Pipeline clássico (modular), útil para entender o vocabulário da área:
 1. Pré-processamento: o áudio é dividido em janelas curtas e convertido
    em representações acústicas (espectrogramas, coeficientes como MFCC).
 2. Modelo acústico: associa trechos de áudio a unidades sonoras
    (fonemas ou subpalavras).
 3. Léxico (dicionário de pronúncia): liga sequências de fonemas a
    palavras.
 4. Modelo de linguagem: estima quais sequências de palavras são
    prováveis ("questão de ordem" é mais provável que "questão de
    morde").
 5. Decodificador: combina tudo e escolhe a hipótese de texto mais
    provável.
Nos sistemas modernos (item 1.2) essas etapas são fundidas em uma rede
única, mas as funções continuam existindo "por dentro".

Métrica central: WER (Word Error Rate) = (S + D + I) / N, onde S =
substituições, D = deleções, I = inserções e N = número de palavras da
transcrição de referência (feita por humano). Quanto menor, melhor.
Como I entra no numerador e não no denominador, o WER PODE ultrapassar
100%. No cálculo usual, sobre texto normalizado, o WER não mede pontuação nem capitalização; a atribuição de locutor fica fora do WER em qualquer convenção.

EXEMPLO PARLAMENTAR
Na sessão deliberativa, o deputado diz: "Sr. Presidente, peço a palavra
pela ordem." O ASR produz: "senhor presidente peço a palavra pela
ordem". O reconhecimento acertou as palavras (WER baixo), mas a saída
está sem pontuação, sem maiúsculas e sem a abreviatura padrão. Essas
camadas são tratadas nos itens 1.5 e 2.x, não pelo ASR "puro".

PEGADINHA PROVÁVEL
A banca tende a atribuir ao ASR funções que são de outros módulos:
"o ASR identifica o orador", "o ASR interpreta o sentido da fala",
"o ASR corrige o conteúdo". Todas erradas. ASR = transcrição literal.
Outra: afirmar que WER "varia de 0% a 100%". Errado: inserções permitem
WER > 100%. Outra: tratar WER de 0% como prova de transcrição "perfeita"
em todos os aspectos — no cálculo usual ele ignora pontuação, e em qualquer convenção ignora locutores.

## 1.2 MODELOS DE FALA END-TO-END

DEFINIÇÃO
Modelo end-to-end ("ponta a ponta") é aquele em que uma única rede
neural é treinada para mapear diretamente o áudio ao texto, substituindo
a construção separada de modelo acústico + léxico + modelo de linguagem.
Toda a rede é otimizada conjuntamente para o objetivo final (texto
correto). Famílias arquiteturais mais citadas: CTC (Connectionist
Temporal Classification), RNN-Transducer e codificador-decodificador com
atenção (Transformers). O Whisper, da OpenAI, é um codificador-decodificador Transformer treinado com supervisão fraca em larga escala
(artigo do Whisper, "Robust Speech Recognition via Large-Scale Weak Supervision", 06/12/2022; repositório openai/whisper no GitHub, verificado em 07/10/2026).

O que "end-to-end" NÃO significa:
 - não significa "sem dados rotulados": continua precisando de pares
   áudio-texto para treinar (a "supervisão fraca" do Whisper usa
   transcrições existentes na internet, não ausência de transcrição);
 - não significa "sem modelo de linguagem": o conhecimento linguístico
   fica implícito na rede e, em muitos sistemas, ainda se pode acoplar
   um modelo de linguagem externo na decodificação;
 - não significa "sem pré-processamento": em geral (por exemplo, no Whisper) o áudio é convertido em espectrograma antes de entrar na rede; há modelos que recebem a forma de onda bruta (por exemplo, wav2vec 2.0, arXiv 2006.11477, seção 2, verificado em 08/10/2026).

Vantagens: simplicidade de treinamento, melhor desempenho com muitos
dados, menos engenharia manual de pronúncia. Custos: exige grande volume
de dados, é mais difícil de "consertar" pontualmente (não há dicionário
para editar), e erros podem ser fluentes porém falsos (o modelo "inventa"
uma frase plausível onde o áudio é ruim) — modelos end-to-end não são
imunes a esse tipo de erro.

EXEMPLO PARLAMENTAR
Um modelo modular erra o nome de um deputado porque o léxico não contém
a pronúncia; a correção é adicionar a entrada ao dicionário. Um modelo
end-to-end erra o mesmo nome; a correção passa por adaptação de vocabulário (item 1.6) ou por mais dados — não há dicionário para editar.

PEGADINHA PROVÁVEL
Trocar "end-to-end" por "não supervisionado" ou "sem modelo de linguagem". Também: afirmar que modelos end-to-end "nunca alucinam" ou que
"sempre superam" os modulares em qualquer condição — generalizações
indevidas.

## 1.3 LLMs MULTIMODAIS DE ÁUDIO NATIVO

DEFINIÇÃO
Um LLM multimodal de áudio nativo é um modelo de linguagem de grande
porte que recebe o áudio como modalidade de ENTRADA do próprio modelo
(e, em alguns casos, produz áudio como SAÍDA), sem que o fluxo dependa
de um módulo ASR separado que converta fala em texto antes do processamento. O contraste é com a arquitetura EM CASCATA: ASR → LLM (texto) →
TTS (síntese de voz), em que o LLM só vê texto e perde o que não está
nas palavras (entonação, hesitação, sobreposição, risos).

Evidência de que a categoria existe comercialmente:
 - OpenAI: o guia oficial distingue (i) "Audio in Chat Completions"
   (entrada/saída de áudio em requisições multimodais), (ii) a Realtime
   API e o GPT-Live (agentes fala-a-fala) e (iii) os endpoints dedicados
   de transcrição de arquivo e transcrição ao vivo (documentação da OpenAI sobre áudio, verificado em 07/10/2026).
 - Google: a documentação "Audio understanding" descreve o uso de áudio
   como entrada dos modelos Gemini para transcrição, sumarização e
   análise de trechos por timestamp; a mesma documentação informa que
   cada segundo de áudio é representado por 32 tokens (documentação do Google sobre áudio e transcrição na API Gemini, verificado em 07/10/2026). Há também um modelo dedicado de transcrição (gemini-3.5-transcribe) com diarização, timestamps por palavra e dicas de vocabulário
   (custom_vocabulary); as dicas de vocabulário não se combinam com
   diarização nem com timestamps por palavra (documentação do Google sobre áudio e transcrição na API Gemini, página /transcribe, verificado em 07/10/2026).

Contraste: ASR aprimorado por LLM. O "LLM speech" do Azure AI Speech é
um exemplo de outra categoria — um serviço de ASR aprimorado por LLM,
que transcreve ou traduz áudio PRÉ-GRAVADO (documentação da Microsoft sobre o Azure AI Speech, verificado em 07/10/2026). Não é
um LLM de áudio nativo conversacional: é reconhecimento de fala com
qualidade e contexto reforçados por LLM. A distinção importa para a
prova: "usa LLM" não é sinônimo de "áudio nativo".

Por que isso importa para transcrição parlamentar: o modelo nativo pode,
na mesma passada, transcrever, resumir, identificar temas e responder
perguntas sobre o áudio. O preço é o risco de "transcrição interpretativa": como o modelo foi treinado para gerar texto plausível, ele
pode normalizar, completar ou omitir trechos. Para registro oficial,
isso exige revisão humana (item 2.2) e critérios de fidelidade (2.3).

EXEMPLO PARLAMENTAR
Áudio de uma comissão com três oradores se interrompendo. Em cascata, o
ASR produz um bloco de texto e o LLM resume a partir dele, sem saber
quem interrompeu quem. Um LLM de áudio nativo recebe o áudio diretamente
e pode ser instruído a "transcrever marcando interrupções e indicando
timestamps" — porém o resultado continua sendo uma GERAÇÃO, não uma
cópia fiel, e deve ser conferido.

PEGADINHA PROVÁVEL
(1) Dizer que a cascata "preserva prosódia" — não preserva; o LLM da
cascata só recebe texto. (2) Dizer que o LLM nativo "elimina a necessidade de revisão humana" — contraria o próprio edital (2.2, human in the
loop). (3) Confundir "transcrição por LLM" com "ASR dedicado": o próprio
fornecedor recomenda endpoint dedicado para transcrição de arquivos e
LLM/Realtime para conversação (documentação da OpenAI sobre áudio, verificado em 07/10/2026). (4) Confundir "ASR
aprimorado por LLM" com "LLM de áudio nativo". (5) Nomes e versões de
modelos mudam em meses: a banca pode cobrar o CONCEITO, não o nome do
produto.



## 1.4 DIARIZAÇÃO DE FALANTES

DEFINIÇÃO
Diarização (speaker diarization) responde a "quem falou quando": segmenta o áudio em trechos e atribui a cada trecho um rótulo de locutor
genérico (Locutor 1, Locutor 2...). Etapas típicas: detecção de atividade de voz (VAD) → segmentação → extração de "embeddings" de voz por
segmento → agrupamento (clustering) dos segmentos por semelhança de voz
→ rotulagem. Métrica usual: DER (Diarization Error Rate), que soma erro
de falante, fala perdida e falso alarme — distinta do WER, que mede
erros de palavras.

Três conceitos que a banca adora misturar:
 - Diarização: separa os locutores, SEM dizer quem são.
 - Identificação de locutor: diz QUEM é, comparando a voz com um banco
   de vozes cadastradas (precisa de cadastro prévio).
 - Verificação de locutor: confirma se a voz é de UMA pessoa específica
   alegada (1 para 1), como em autenticação.
A diarização pode ser ligada à identificação quando se fornecem amostras de referência: a API da OpenAI permite até quatro referências
curtas (2 a 10 s) com nomes de locutores conhecidos para mapear os
segmentos (documentação da OpenAI sobre fala para texto, verificado em 07/10/2026).

Limitações recorrentes: fala sobreposta (apartes), locutores com vozes
parecidas, mudança rápida de orador, áudio de canal único com ruído de
plenário. A disponibilidade por modo varia entre fornecedores: no
Google Speech-to-Text V2, não há diarização em StreamingRecognize no
modelo chirp_3 (documentação do Google Cloud sobre o modelo Chirp 3, verificado em 07/10/2026); na OpenAI, a rotulagem de locutores
está no endpoint de transcrição de arquivo e não é suportada em sessões
Realtime de transcrição (documentação da OpenAI sobre fala para texto, verificado em 07/10/2026); em contrapartida, o Amazon
Transcribe oferece diarização em streaming (parâmetro ShowSpeakerLabel)
(referência da API StartStreamTranscription, da AWS, verificado em 07/10/2026). A lição para a prova: "diarização em streaming"
não é regra geral nem impossibilidade geral — depende do serviço.

EXEMPLO PARLAMENTAR
Na transcrição de uma audiência pública com cinco convidados, a diarização entrega "Locutor 1 ... Locutor 5". Para que o texto saia como
"O SR. FULANO (Relator)", é preciso identificação — por amostra de voz
cadastrada ou, na prática do registro, pela revisão humana com a lista
de inscritos e a ordem de falas. Diarização habilitada, sozinha, não
produz nomes.

PEGADINHA PROVÁVEL
Definir diarização como "identificação" ou "verificação". Afirmar que
diarização está disponível "em qualquer modo" de qualquer serviço — ou
que nunca existe em streaming. Afirmar que a diarização resolve sozinha
a fala sobreposta.

## 1.5 PONTUAÇÃO AUTOMÁTICA E CAPITALIZAÇÃO

DEFINIÇÃO
A saída "crua" de muitos sistemas ASR é texto em minúsculas e sem pontuação, porque o modelo aprende sons, não sinais gráficos. Pontuação
automática e capitalização são a camada que restaura vírgulas, pontos,
interrogações e maiúsculas. Duas formas de obter isso:
 1. Pós-processamento: um modelo separado (geralmente de rotulagem de
    sequência) lê o texto cru — às vezes com pistas de pausa/prosódia —
    e insere os sinais.
 2. Geração direta: modelos end-to-end modernos aprendem a emitir texto
    já pontuado e capitalizado, como parte da própria saída. No chirp_3,
    pontuação e capitalização automáticas são geradas pelo modelo e
    podem ser desativadas (documentação do Google Cloud sobre o modelo Chirp 3, verificado em 07/10/2026). No Amazon Transcribe, o
    serviço adiciona pontuação e formatação de números (visão geral da documentação do Amazon Transcribe, verificado em 07/10/2026).
Recurso DIFERENTE: "pontuação falada" (spoken punctuation), em que o
orador dita "vírgula", "ponto", e o sistema converte a palavra no sinal.
O Google documenta esse recurso separadamente da pontuação automática
(documentação do Google Cloud sobre o modelo Chirp 3, menu de recursos, verificado em 07/10/2026). Isso serve para ditado, não para
sessões.

EXEMPLO PARLAMENTAR
Áudio: "o senhor me permite um aparte deputado" → cru: "o senhor me
permite um aparte deputado" → pontuado: "O senhor me permite um aparte,
Deputado?" A interrogação não foi "ouvida": foi inferida da estrutura
da frase e da entonação. Em registro oficial, uma interrogação indevida
muda o sentido ("Aprovado." vs "Aprovado?"), por isso a revisão humana
(2.3) confere pontuação, não só palavras.

PEGADINHA PROVÁVEL
Dizer que a pontuação automática "detecta os sinais pronunciados" (isso
é pontuação falada). Dizer que capitalização automática identifica
nomes próprios "com certeza" — ela estima; "Câmara" (instituição) vs
"câmara" (sala) é decisão de contexto que o modelo pode errar.

## 1.6 DESAFIOS DO ASR EM PORTUGUÊS BRASILEIRO

DEFINIÇÃO / MAPA DOS DESAFIOS
 1. Variação regional e social: sotaques, redução de sílabas, "s"
    chiado, vogais abertas/fechadas — o modelo treinado majoritariamente
    com um padrão perde acurácia nos demais.
 2. Vocabulário técnico e parlamentar: siglas (PEC, MPV, CCJ, PL),
    expressões regimentais ("pela ordem", "questão de ordem", "obstrução", "destaque", "requerimento de urgência"), nomes próprios de
    parlamentares, de municípios e de órgãos, termos jurídicos e latinismos. Palavras raras ou ausentes do treinamento são substituídas
    por palavras comuns de som parecido.
 3. Condições acústicas do plenário: microfones distintos, reverberação, burburinho, apartes e sobreposição.
 4. Números, datas, dinheiro e abreviaturas: "artigo quinze, parágrafo
    segundo" → "art. 15, § 2º" exige normalização (item 2.5).
 5. Fala espontânea: hesitações, reformulações, frases incompletas.
 6. Desequilíbrio de dados: há muito menos áudio transcrito em pt-BR
    que em inglês; modelos multilíngues cobrem pt-BR, mas a acurácia
    varia por idioma (a própria OpenAI avisa que, no Whisper, a acurácia
    varia entre os idiomas suportados) (documentação da OpenAI sobre fala para texto, verificado em 07/10/2026).

FERRAMENTAS DE MITIGAÇÃO (o que cada fornecedor chama de quê):
 - Google: "speech adaptation"/model adaptation — lista de palavras e
   frases que elevam a probabilidade de reconhecimento; o chirp_3 aceita
   até 1.000 frases, e a própria documentação recomenda poucas entradas
   para não degradar o resto (documentação do Google Cloud sobre o modelo Chirp 3, verificado em 07/10/2026).
 - AWS: "custom vocabulary" (acrescenta termos ao vocabulário base) (visão geral da documentação do Amazon Transcribe, verificado em 07/10/2026) e "custom language model" (CLM), treinado com dados
   de TEXTO do domínio fornecidos pelo usuário, recurso distinto do
   custom vocabulary (documentação do Amazon Transcribe sobre modelos de linguagem personalizados, verificado em 07/10/2026). CLM indisponível para pt-BR
   na tabela oficial (documentação do Amazon Transcribe sobre idiomas suportados, verificado em 07/10/2026); para pt-BR, o recurso de
   mitigação lexical documentado é o custom vocabulary.
 - Azure: "custom speech" — modelos personalizados treinados com dados
   acústicos, de linguagem e de pronúncia (documentação da Microsoft sobre o Azure AI Speech, verificado em 07/10/2026).
 - OpenAI: parâmetros prompt, keywords e languages no modelo de transcrição recomendado; no whisper-1, prompt limitado a 224 tokens (documentação da OpenAI sobre fala para texto, verificado em 07/10/2026).
Distinção decisiva: adaptação de vocabulário é VIÉS de reconhecimento
(empurra o decodificador para termos esperados); não é retreinamento
acústico e não garante acerto em qualquer condição. Sotaque se trata
com dados acústicos (modelo customizado ou mais dados), não com lista
de palavras.

EXEMPLO PARLAMENTAR
Antes de transcrever a sessão, a equipe carrega uma lista com nomes dos
513 deputados, siglas das comissões e expressões regimentais. O erro
"PEC" → "pec" ou "pet" cai; o erro de sotaque de um orador nordestino
não muda, porque a lista não altera o modelo acústico.

PEGADINHA PROVÁVEL
Igualar custom vocabulary a retreinamento; dizer que CLM se treina com
áudio (no AWS é com texto); dizer que "modelos multilíngues eliminam o
problema do pt-BR"; dizer que lista de termos garante reconhecimento
"em qualquer condição acústica".



## 1.7 TRANSCRIÇÃO EM TEMPO REAL

DEFINIÇÃO
Transcrição em tempo real (streaming) processa o áudio ENQUANTO ele
chega, em pequenos blocos, devolvendo texto com atraso de segundos. Em
oposição: transcrição em lote (batch/arquivo), em que o áudio completo
já existe e é processado inteiro. Características do streaming:
 - resultados PARCIAIS/intermediários (podem mudar) e resultados FINAIS
   (em geral consolidados quando o sistema detecta fim de enunciado);
 - "endpointing": decisão de que o orador terminou uma frase, geralmente
   por silêncio; sensibilidade maior = resposta mais rápida, mas risco
   de cortar o orador — o Google documenta três níveis de sensibilidade
   e avisa exatamente esse risco (documentação do Google Cloud sobre o modelo Chirp 3, verificado em 07/10/2026);
 - estabilização de resultados parciais: recurso para reduzir "idas e
   vindas" do texto exibido (documentado pela AWS como partial-result
   stabilization) (referência da API StartStreamTranscription, da AWS, verificado em 07/10/2026);
 - recursos que podem não existir em streaming — e isso varia por
   fornecedor: diarização ausente em StreamingRecognize do chirp_3 (documentação do Google Cloud sobre o modelo Chirp 3, verificado em 07/10/2026) e nas sessões Realtime da OpenAI (documentação da OpenAI sobre fala para texto, verificado em 07/10/2026), mas disponível em streaming no Amazon Transcribe (referência da API StartStreamTranscription, da AWS, verificado em 07/10/2026); na AWS, a identificação automática de idioma em streaming não
   pode ser combinada com CLM nem com redação de PII (referência da API StartStreamTranscription, da AWS, verificado em 07/10/2026).
Cuidado conceitual: "streaming de SAÍDA" ≠ "tempo real". Na OpenAI, o
endpoint de transcrição de arquivo aceita stream=true para devolver o
texto aos poucos enquanto processa um ARQUIVO COMPLETO; áudio ao vivo
de microfone usa a Realtime/Live transcription, outro fluxo (documentação da OpenAI sobre fala para texto, verificado em 07/10/2026).

EXEMPLO PARLAMENTAR
Legenda ao vivo da sessão na TV Câmara: streaming com baixa latência;
tolera-se correção de texto parcial. Notas taquigráficas oficiais:
melhor fazer em lote, com diarização e revisão. São dois produtos, dois
fluxos, duas tolerâncias a erro.

PEGADINHA PROVÁVEL
"Streaming é sempre mais preciso" (não; batch vê contexto completo).
"Streaming oferece os mesmos recursos que batch" (não necessariamente;
ver diarização). "stream=true em arquivo = tempo real" (não).

## 1.8 FERRAMENTAS E APIs

Regra de leitura: tudo abaixo é retrato de 07/10/2026. Nomes de modelo
e limites mudam. O que a prova tende a cobrar é a CATEGORIA de recurso
(batch/streaming, diarização, vocabulário, idioma, execução local).

WHISPER (OpenAI)
Observação: o edital grafa "Whisper (Open AI)"; a grafia oficial do
fornecedor é "OpenAI". A diferença não afeta o julgamento de itens.
 - Modelo de código aberto, com código e pesos publicados no GitHub
   (openai/whisper) sob licença MIT; pode ser executado localmente, sem
   enviar áudio a terceiros — relevante para dados sensíveis (repositório openai/whisper no GitHub, verificado em 07/10/2026).
 - A documentação da API informa que o Whisper suporta 98 idiomas, com
   acurácia variável por idioma (documentação da OpenAI sobre fala para texto, verificado em 07/10/2026).
 - Na API: whisper-1 é indicado quando se precisa de timestamps por
   palavra/segmento, formatos de legenda ou tradução para o inglês
   (endpoint /audio/translations, só para inglês). Para transcrição
   geral, a OpenAI recomenda hoje o modelo gpt-transcribe; para rótulos
   de locutor, gpt-4o-transcribe-diarize; para áudio ao vivo, a transcrição Realtime (gpt-live-transcribe) (documentação da OpenAI sobre fala para texto, verificado em 07/10/2026).
 - Limite de arquivo: 25 MB (dividir arquivos maiores sem cortar frases)
   (documentação da OpenAI sobre fala para texto, verificado em 07/10/2026).
 - Prompt do whisper-1 limitado a 224 tokens; o modelo não segue
   instruções como um LLM, só usa o prompt como contexto de vocabulário
   (documentação da OpenAI sobre fala para texto, verificado em 07/10/2026).

GOOGLE CLOUD SPEECH-TO-TEXT (documentação do Google Cloud sobre o modelo Chirp 3, verificado em 07/10/2026)
 - Modelo atual: chirp_3, exclusivo da API V2.
 - Três métodos: StreamingRecognize (tempo real), Recognize (áudio
   curto, < 1 min) e BatchRecognize (longo).
 - pt-BR em disponibilidade geral (GA) para transcrição.
 - Diarização: não há diarização em StreamingRecognize; pt-BR suportado.
 - Pontuação e capitalização automáticas; transcrição "agnóstica de
   idioma" (language_codes=["auto"]); adaptação com até 1.000 frases;
   prompt de formatação (preview); redutor de ruído (não remove vozes
   humanas de fundo); sensibilidade de endpointing.

AZURE AI SPEECH (Microsoft) (documentação da Microsoft sobre o Azure AI Speech; documentação da Microsoft sobre diarização no Azure AI Speech, verificado em 07/10/2026)
 - Modos: transcrição em tempo real (streaming), "fast transcription"
   (arquivo) e transcrição em lote (grandes volumes, assíncrona).
 - Custom speech: modelos personalizados com dados acústicos, de linguagem e de pronúncia, para ruído e jargão de domínio.
 - Diarização documentada em tempo real e na fast transcription (documentação da Microsoft sobre diarização no Azure AI Speech);
   lote e limites por idioma: não verificados.
 - Identificação de idioma; "LLM speech (preview)" para transcribe e
   translate de áudio pré-gravado; execução em nuvem OU em contêineres
   on-premises; acesso por SDK, CLI e REST.

AMAZON TRANSCRIBE (AWS) (documentação do Amazon Transcribe sobre idiomas suportados; visão geral da documentação do Amazon Transcribe; referência da API StartStreamTranscription, da AWS; documentação do Amazon Transcribe sobre modelos de linguagem personalizados, verificado em 07/10/2026)
 - Modos batch (arquivo no S3) e streaming.
 - pt-BR suportado em batch e streaming (documentação do Amazon Transcribe sobre idiomas suportados).
 - Custom vocabulary (termos adicionados ao vocabulário base) (visão geral da documentação do Amazon Transcribe);
   custom language model, treinado com dados de texto, distinto do
   custom vocabulary (documentação do Amazon Transcribe sobre modelos de linguagem personalizados); CLM indisponível para pt-BR na tabela
   oficial (documentação do Amazon Transcribe sobre idiomas suportados).
 - Filtro de vocabulário (remover termos indesejados); redação de PII;
   particionamento de locutores (diarização), inclusive em streaming
   (ShowSpeakerLabel) (referência da API StartStreamTranscription, da AWS); timestamp por palavra; identificação
   automática de idioma; pontuação e formatação de números (visão geral da documentação do Amazon Transcribe).
 - Restrição documentada: identificação de idioma em streaming não se
   combina com CLM nem com redação (referência da API StartStreamTranscription, da AWS).

QUADRO-SÍNTESE (categorias, não versões)
 Recurso            | OpenAI        | Google chirp_3 | Azure          | AWS
 Streaming          | sim (Realt.)  | sim            | sim            | sim
 Batch/arquivo      | sim           | sim            | sim            | sim
 Diarização         | sim (arquivo) | sim (não em    | sim (tempo real| sim (batch e
                    |               | streaming)     | e fast) (documentação da Microsoft sobre diarização no Azure AI Speech)* | streaming)
 Vocab./adaptação   | prompt/keyw.  | ≤1.000 frases  | custom speech  | CV (CLM sem pt-BR)
 Execução local     | Whisper OSS   | não verificado | contêiner      | não verificado
                    | (repositório openai/whisper no GitHub)         |                |                |
 Tradução p/ inglês | sim (whisper-1)| não verificado| sim (speech    | não verificado
                    |               |                | translation)   |
* Azure: lote e limites por idioma não verificados.

EXEMPLO PARLAMENTAR
Escolha de ferramenta para o departamento de registro da Câmara (Derep (antigo DETAQ); Ato da Mesa nº 251/2026): se a exigência
for "áudio não sai do prédio", entre as opções verificadas estão o
Whisper local (repositório openai/whisper no GitHub) e o contêiner Azure (documentação da Microsoft sobre o Azure AI Speech); se for "diarização em
pt-BR em lote", o Google documenta (documentação do Google Cloud sobre o modelo Chirp 3); se for "legenda ao vivo",
qualquer um dos quatro em modo streaming — sem diarização no caso do
chirp_3 (documentação do Google Cloud sobre o modelo Chirp 3), e sem rótulos de locutor também na transcrição Realtime
da OpenAI (documentação da OpenAI sobre fala para texto).

PEGADINHA PROVÁVEL
Trocar o modo em que um recurso existe (diarização em streaming vs
batch); atribuir "código aberto" à API (o aberto é o modelo Whisper, não
os serviços); afirmar limites numéricos ou preços sem data; dizer que a
tradução do whisper-1 é "para qualquer idioma" (é só para inglês);
tratar modelo local e serviço em nuvem como equivalentes quanto à
custódia do áudio.

## Complemento

O edital intitula o 1.4 "Diarização de falantes: identificação e
separação de múltiplos oradores". A banca pode usar "identificar" em
dois sentidos, e o julgamento do item depende de qual deles o enunciado
adota.

SENTIDO AMPLO — "identificar" = DISTINGUIR
Perceber que há oradores diferentes e separar as falas de cada um:
"Locutor 1", "Locutor 2". É o que a diarização faz. Não implica saber
quem é cada pessoa. Frases típicas: "a diarização identifica os
diferentes oradores"; "identificação e separação de múltiplos
oradores".

SENTIDO PRÓPRIO — "identificar" = DIZER QUEM É
Associar a voz a uma pessoa determinada: por amostras de voz cadastradas
(identificação de locutor) ou por atribuição humana, com a lista de
inscritos e a ordem das falas. Frases típicas: "exibir o nome do
orador"; "informar a identidade"; "indicar qual parlamentar falou".

REGRA DE DECISÃO PARA A PROVA
 1. Se o item fala em IDENTIDADE, NOME, CADASTRO, "qual parlamentar" ou
    "quem é": é identificação propriamente dita. Diarização sozinha, sem
    amostras de referência, não basta.
 2. Se o item fala em DISTINGUIR, SEPARAR, "quantos oradores" ou rótulos
    genéricos: é diarização, mesmo que use o verbo "identificar".
 3. Se o item usa "identificar" sem mais contexto, não o julgue pelo
    verbo: procure o OBJETO da frase. "Identifica que há três oradores"
    = distinguir. "Identifica os oradores pelo nome" = identificação.
 4. Verificação de locutor continua sendo outra coisa: 1 para 1,
    contra uma identidade alegada (item 1.4).
Ligação com a prática da Casa: na nota taquigráfica, o nome do
parlamentar vem de cadastro ou da atribuição humana; o rótulo da
diarização é só ponto de partida (exemplo parlamentar do 1.4).
Ponte que confunde: diarização ligada à identificação por amostras de
referência (a API da OpenAI aceita até quatro amostras com nomes; documentação da OpenAI sobre fala para texto, verificado em 07/10/2026) mapeia rótulos para nomes. Aí o nome existe
por causa das amostras, não da diarização em si.

PEGADINHAS ADICIONAIS
(1) Ler "identificação" do título como "o sistema sabe os nomes".
(2) Ler "identificar" no item como identificação de locutor sem checar
o objeto. (3) Dizer que diarização que distingue oradores também
verifica identidade. (4) Dizer que, por existirem amostras de
referência, a diarização "sempre" entrega nomes: depende de as
amostras terem sido fornecidas.
```

## Pares

- **ASR** vs **diarização vs identificação de locutor**: texto / quem-quando / quem-é.
- **Diarização** vs **verificação de locutor**: muitos rótulos / 1 pessoa confirmada.
- **End-to-end** vs **modular**: rede única / módulos separados — ambos supervisionados.
- **End-to-end** vs **não supervisionado**: arquitetura / regime de dados.
- **LLM de áudio nativo** vs **cascata ASR→LLM→TTS**: áudio no modelo / texto no modelo.
- **Transcrição por LLM** vs **ASR dedicado**: geração interpretativa / reconhecimento literal.
- **Pontuação automática** vs **pontuação falada**: inferida / ditada.
- **Custom vocabulary (adaptação)** vs **custom language model**: lista de termos que enviesa / modelo treinado com corpus de texto.
- **Adaptação de vocabulário** vs **modelo acústico customizado**: termos / sotaque e ruído.
- **Streaming (tempo real)** vs **batch (arquivo)**: parciais e latência / contexto completo e mais recursos.
- **stream=true em arquivo** vs **Realtime**: saída incremental de arquivo pronto / áudio ao vivo.
- **Endpointing sensível** vs **preciso**: rápido e corta / lento e completo.
- **WER** vs **DER**: erro de palavras / erro de atribuição de locutor.
- **Whisper (modelo aberto)** vs **API OpenAI (serviço)**: local / nuvem.
- **Tradução (whisper-1, só para inglês)** vs **transcrição (idioma original)**.
- **Timestamps por palavra** vs **por enunciado**: granularidade fina (cada palavra com início e fim) / granularidade grossa (cada frase ou trecho).
- **LLM de áudio nativo** vs **ASR aprimorado por LLM**: áudio como entrada do LLM / reconhecimento de fala reforçado por LLM.

## Pegadinhas

- [P2-1.1] **Reconhecimento automático de fala (ASR – Automatic Speech Recognition)** — A banca tende a atribuir ao ASR funções que são de outros módulos: "o ASR identifica o orador", "o ASR interpreta o sentido da fala", "o ASR corrige o conteúdo". Todas erradas. ASR = transcrição literal. Outra: afirmar que WER "varia de 0% a 100%". Errado: inserções permitem WER > 100%. Outra: tratar WER de 0% como prova de transcrição "perfeita" em todos os aspectos — no cálculo usual ele ignora pontuação, e em qualquer convenção ignora locutores.
- [P2-1.1] **Reconhecimento automático de fala (ASR – Automatic Speech Recognition)** — Não confunda ASR com diarização nem com identificação de locutor: o ASR só converte fala em texto; a diarização responde a quem falou e quando; a identificação de locutor diz quem é a pessoa. Decidir quem falou não é função do ASR.
- [P2-1.2] **Modelos de fala end-to-end** — Trocar "end-to-end" por "não supervisionado" ou "sem modelo de linguagem". Também: afirmar que modelos end-to-end "nunca alucinam" ou que "sempre superam" os modulares em qualquer condição — generalizações indevidas.
- [P2-1.2] **Modelos de fala end-to-end** — Não confunda modelo end-to-end com modelo modular: no end-to-end, uma única rede neural é treinada para mapear diretamente o áudio ao texto; no modular, modelo acústico, léxico e modelo de linguagem são componentes separados. Os dois são supervisionados.
- [P2-1.3] **LLMs multimodais de áudio nativo** — Dizer que a cascata "preserva prosódia" — não preserva; o LLM da cascata só recebe texto.
- [P2-1.3] **LLMs multimodais de áudio nativo** — Dizer que o LLM nativo "elimina a necessidade de revisão humana" — contraria o próprio edital (2.2, human in the loop).
- [P2-1.3] **LLMs multimodais de áudio nativo** — Confundir "transcrição por LLM" com "ASR dedicado": o próprio fornecedor recomenda endpoint dedicado para transcrição de arquivos e LLM/Realtime para conversação (documentação da OpenAI sobre áudio, verificado em 07/10/2026).
- [P2-1.3] **LLMs multimodais de áudio nativo** — Confundir "ASR aprimorado por LLM" com "LLM de áudio nativo".
- [P2-1.3] **LLMs multimodais de áudio nativo** — Nomes e versões de modelos mudam em meses: a banca pode cobrar o CONCEITO, não o nome do produto.
- [P2-1.3] **LLMs multimodais de áudio nativo** — Não confunda LLM de áudio nativo com cascata ASR → LLM → TTS: no modelo nativo, o áudio entra no próprio LLM, sem módulo ASR separado; na cascata, o LLM só vê texto e perde o que não está nas palavras, como entonação, hesitação, sobreposição e risos.
- [P2-1.4] **Diarização de falantes: identificação e separação de múltiplos oradores** — Definir diarização como "identificação" ou "verificação". Afirmar que diarização está disponível "em qualquer modo" de qualquer serviço — ou que nunca existe em streaming. Afirmar que a diarização resolve sozinha a fala sobreposta.
- [P2-1.4] **Diarização de falantes: identificação e separação de múltiplos oradores** — Não confunda WER (Word Error Rate) com DER (Diarization Error Rate): o WER mede erros de palavras; o DER soma erro de falante, fala perdida e falso alarme.
- [P2-1.5] **Pontuação automática e capitalização em transcrições** — Dizer que a pontuação automática "detecta os sinais pronunciados" (isso é pontuação falada). Dizer que capitalização automática identifica nomes próprios "com certeza" — ela estima; "Câmara" (instituição) vs "câmara" (sala) é decisão de contexto que o modelo pode errar.
- [P2-1.6] **Desafios do ASR em Português Brasileiro: sotaques, vocabulário técnico e parlamentar** — Igualar custom vocabulary a retreinamento
- [P2-1.6] **Desafios do ASR em Português Brasileiro: sotaques, vocabulário técnico e parlamentar** — dizer que CLM se treina com áudio (no AWS é com texto)
- [P2-1.6] **Desafios do ASR em Português Brasileiro: sotaques, vocabulário técnico e parlamentar** — dizer que "modelos multilíngues eliminam o problema do pt-BR"
- [P2-1.6] **Desafios do ASR em Português Brasileiro: sotaques, vocabulário técnico e parlamentar** — dizer que lista de termos garante reconhecimento "em qualquer condição acústica".
- [P2-1.6] **Desafios do ASR em Português Brasileiro: sotaques, vocabulário técnico e parlamentar** — Não confunda custom vocabulary com custom language model (CLM): o custom vocabulary acrescenta termos ao vocabulário base e age como viés de reconhecimento; o CLM, no Amazon Transcribe, é treinado com dados de texto do domínio, e não com áudio.
- [P2-1.6] **Desafios do ASR em Português Brasileiro: sotaques, vocabulário técnico e parlamentar** — Não confunda adaptação de vocabulário com modelo acústico customizado: a adaptação de vocabulário é viés de reconhecimento, que empurra o decodificador para termos esperados, e não altera o modelo acústico; sotaque e ruído se tratam com dados acústicos, em modelo customizado ou com mais dados.
- [P2-1.7] **Transcrição em tempo real** — "Streaming é sempre mais preciso" (não; batch vê contexto completo). "Streaming oferece os mesmos recursos que batch" (não necessariamente; ver diarização). "stream=true em arquivo = tempo real" (não).
- [P2-1.7] **Transcrição em tempo real** — Não confunda endpointing sensível com endpointing preciso: o endpointing decide que o orador terminou a frase, em geral por silêncio. O sensível responde mais rápido, mas corre o risco de cortar o orador; o preciso é mais lento, porém corre menos risco de cortá-lo.
- [P2-1.8] **Ferramentas e APIs: Whisper (Open AI), Google Speech-to-text, Azure Speech, AWS Transcribe** — Trocar o modo em que um recurso existe (diarização em streaming vs batch)
- [P2-1.8] **Ferramentas e APIs: Whisper (Open AI), Google Speech-to-text, Azure Speech, AWS Transcribe** — atribuir "código aberto" à API (o aberto é o modelo Whisper, não os serviços)
- [P2-1.8] **Ferramentas e APIs: Whisper (Open AI), Google Speech-to-text, Azure Speech, AWS Transcribe** — afirmar limites numéricos ou preços sem data
- [P2-1.8] **Ferramentas e APIs: Whisper (Open AI), Google Speech-to-text, Azure Speech, AWS Transcribe** — dizer que a tradução do whisper-1 é "para qualquer idioma" (é só para inglês)
- [P2-1.8] **Ferramentas e APIs: Whisper (Open AI), Google Speech-to-text, Azure Speech, AWS Transcribe** — tratar modelo local e serviço em nuvem como equivalentes quanto à custódia do áudio.
- [P2-1.8] **Ferramentas e APIs: Whisper (Open AI), Google Speech-to-text, Azure Speech, AWS Transcribe** — Não confunda tradução com transcrição no whisper-1: a tradução, pelo endpoint /audio/translations, devolve o texto em inglês, e só para o inglês; a transcrição mantém o idioma original do áudio.
- [P2-1.8] **Ferramentas e APIs: Whisper (Open AI), Google Speech-to-text, Azure Speech, AWS Transcribe** — Não confunda timestamps por palavra com timestamps por segmento: os primeiros marcam início e fim de cada palavra, em granularidade fina; os segundos marcam cada frase ou trecho, em granularidade grossa. O whisper-1 é indicado quando se precisa de timestamps por palavra ou por segmento.
- [P2-1.4] **Diarização de falantes: identificação e separação de múltiplos oradores** — Ler "identificação" do título como "o sistema sabe os nomes".
- [P2-1.4] **Diarização de falantes: identificação e separação de múltiplos oradores** — Ler "identificar" no item como identificação de locutor sem checar o objeto.
- [P2-1.4] **Diarização de falantes: identificação e separação de múltiplos oradores** — Dizer que diarização que distingue oradores também verifica identidade.
- [P2-1.4] **Diarização de falantes: identificação e separação de múltiplos oradores** — Dizer que, por existirem amostras de referência, a diarização "sempre" entrega nomes: depende de as amostras terem sido fornecidas.

## Tópico P2-1.1 — Reconhecimento automático de fala (ASR – Automatic Speech Recognition)

### Resumo do tópico

O ASR, reconhecimento automático de fala, converte áudio com fala em texto e só faz isso. Não decide quem falou, tarefa da diarização ou da identificação de locutor, nem o que o texto significa, tarefa da compreensão de linguagem natural.

O pipeline clássico é modular: pré-processamento, modelo acústico, léxico de pronúncia, modelo de linguagem e decodificador, que escolhe a hipótese de texto mais provável. Nos sistemas modernos uma rede única funde essas etapas, mas as funções continuam existindo por dentro.

A métrica central é o WER: substituições mais deleções mais inserções, divididas pelo número de palavras da referência humana; quanto menor, melhor. Como as inserções entram só no numerador, o WER pode ultrapassar 100%. No cálculo usual, sobre texto normalizado, não mede pontuação nem capitalização, e a atribuição de locutor fica fora do WER em qualquer convenção.

A banca tende a atribuir ao ASR funções de outros módulos, como identificar o orador, interpretar o sentido ou corrigir o conteúdo, quando ASR é transcrição literal. Também é errado dizer que o WER varia de 0% a 100%, ou que WER de 0% prova transcrição perfeita em todos os aspectos.

## Tópico P2-1.2 — Modelos de fala end-to-end

### Resumo do tópico

Modelo end-to-end é aquele em que uma única rede neural é treinada para mapear diretamente o áudio ao texto, no lugar de modelo acústico, léxico e modelo de linguagem construídos separadamente. As famílias mais citadas são CTC, RNN-Transducer e codificador-decodificador com atenção; o Whisper, da OpenAI, é um codificador-decodificador Transformer treinado com supervisão fraca em larga escala.

Há equívocos sobre o que end-to-end significa. Não significa ausência de dados rotulados, pois continua precisando de pares áudio-texto; nem de modelo de linguagem, cujo conhecimento fica implícito na rede; nem de pré-processamento, já que em geral o áudio vira espectrograma antes de entrar, embora haja modelos que recebem a forma de onda bruta.

As vantagens são simplicidade de treinamento, melhor desempenho com muitos dados e menos engenharia manual de pronúncia. Os custos são a exigência de grande volume de dados e a dificuldade de consertar pontualmente, pois não há dicionário para editar. Os erros podem ser fluentes porém falsos, de modo que afirmar que nunca alucinam ou sempre superam os modulares é generalização indevida.

## Tópico P2-1.3 — LLMs multimodais de áudio nativo

### Resumo do tópico

Um LLM multimodal de áudio nativo recebe o áudio como entrada do próprio modelo, e em alguns casos produz áudio como saída, sem depender de um módulo ASR separado que converta a fala em texto antes. O contraste é a arquitetura em cascata, ASR, LLM sobre texto e síntese de voz, em que o LLM só vê texto e perde entonação, hesitação, sobreposição e risos.

A categoria existe comercialmente. A OpenAI distingue áudio em Chat Completions, a Realtime API para agentes fala-a-fala e endpoints dedicados de transcrição de arquivo e ao vivo. A documentação do Google descreve o áudio como entrada dos modelos Gemini para transcrição, sumarização e análise por timestamp.

ASR aprimorado por LLM é outra categoria. O LLM speech do Azure AI Speech transcreve ou traduz áudio pré-gravado, com qualidade e contexto reforçados por LLM, mas não é um LLM de áudio nativo conversacional. Usar LLM não é sinônimo de áudio nativo.

Na transcrição parlamentar, o modelo nativo pode transcrever, resumir e responder perguntas sobre o áudio na mesma passada, mas corre o risco de transcrição interpretativa: por gerar texto plausível, pode normalizar, completar ou omitir trechos. Para registro oficial, isso exige revisão humana, e o resultado continua sendo geração, não cópia fiel.

A banca pode dizer que a cascata preserva prosódia, quando o LLM da cascata só recebe texto, ou que o LLM nativo elimina a revisão humana. Pode confundir transcrição por LLM com ASR dedicado, pois a OpenAI recomenda endpoint dedicado para arquivos e LLM ou Realtime para conversação. Nomes e versões mudam em meses; cobra-se o conceito, não o produto.

## Tópico P2-1.4 — Diarização de falantes: identificação e separação de múltiplos oradores

### Resumo do tópico

Diarização responde a "quem falou quando": segmenta o áudio em trechos e atribui a cada um um rótulo genérico de locutor, como Locutor 1 e Locutor 2. As etapas vão da detecção de atividade de voz à rotulagem, passando por embeddings e agrupamento por semelhança. A métrica usual é o DER, distinta do WER, que mede erros de palavras.

Três conceitos se misturam. A diarização separa os locutores sem dizer quem são. A identificação de locutor diz quem é, comparando a voz com um banco de vozes cadastradas. A verificação de locutor confirma se a voz é de uma pessoa específica alegada, de um para um, como na autenticação.

O verbo "identificar" também é armadilha. Se o item trata de identidade, nome, cadastro ou "qual parlamentar", exige identificação propriamente dita. Se trata de distinguir, separar ou contar oradores, é diarização, ainda que use o verbo. Sem contexto, julga-se pelo objeto: identificar que há três oradores é distinguir; identificar os oradores pelo nome é identificação.

A diarização pode ser ligada à identificação quando se fornecem amostras de referência: a API da OpenAI permite até quatro referências curtas com nomes de locutores conhecidos para mapear os segmentos. O nome existe por causa das amostras, não da diarização em si. Num texto com nomes, como "O SR. FULANO (Relator)", há amostra cadastrada ou revisão humana com a lista de inscritos.

A diarização tem limites técnicos e de oferta: sofre com fala sobreposta, vozes parecidas e ruído de plenário em canal único. A disponibilidade varia por serviço e modo: o Google Speech-to-Text V2 não tem diarização em StreamingRecognize no modelo chirp_3, a OpenAI não a suporta em sessões Realtime e o Amazon Transcribe a oferece em streaming. Logo, diarização em streaming não é regra geral nem impossibilidade geral.

### Em 1 minuto

- Diarização responde a quem falou quando: segmenta o áudio em trechos e dá a cada um um rótulo genérico de locutor, sem dizer quem são.
- Identificação de locutor compara a voz com um banco de vozes cadastradas; verificação confirma se a voz é de uma pessoa específica alegada, de um para um.
- Diarização em streaming não é regra geral nem impossibilidade geral, pois depende do serviço; fala sobreposta e vozes parecidas seguem como limitações.

#### Etapas típicas da diarização

1. Detecção de atividade de voz (VAD)
2. Segmentação do áudio em trechos
3. Extração de embeddings de voz por segmento
4. Agrupamento (clustering) por semelhança de voz
5. Rotulagem (Locutor 1, Locutor 2...)

#### Diarização, identificação e verificação de locutor

| Conceito | Pergunta que responde | Como funciona |
|---|---|---|
| Diarização | Quem falou quando? | Separa os locutores, sem dizer quem são |
| Identificação de locutor | Quem é? | Compara a voz com banco de vozes cadastradas (cadastro prévio) |
| Verificação de locutor | É a pessoa alegada? | Confirma se a voz é da pessoa alegada (1 para 1), como em autenticação |

*A diarização pode ser ligada à identificação quando há amostras de referência.*

#### Limitações recorrentes da diarização

- **Diarização de falantes**
  - Fala sobreposta (apartes)
  - Locutores com vozes parecidas
  - Mudança rápida de orador
  - Áudio de canal único com ruído de plenário

## Tópico P2-1.5 — Pontuação automática e capitalização em transcrições

### Resumo do tópico

A saída crua de muitos sistemas ASR é texto em minúsculas e sem pontuação, porque o modelo aprende sons, não sinais gráficos. Pontuação automática e capitalização restauram vírgulas, pontos, interrogações e maiúsculas.

Há duas formas de obtê-las. No pós-processamento, um modelo separado lê o texto cru, às vezes com pistas de pausa ou prosódia, e insere os sinais. Na geração direta, modelos end-to-end já emitem texto pontuado e capitalizado; no chirp_3 isso é gerado pelo modelo e pode ser desativado.

Pontuação falada é recurso diferente: o orador dita "vírgula" ou "ponto" e o sistema converte a palavra no sinal. Serve para ditado, não para sessões.

Pontuação e capitalização automáticas são estimativas; a interrogação é inferida da estrutura da frase e da entonação, não ouvida, e a capitalização estima nomes próprios. Uma interrogação indevida muda o sentido ("Aprovado." e "Aprovado?"); por isso, a revisão confere pontuação, não só palavras.

## Tópico P2-1.6 — Desafios do ASR em Português Brasileiro: sotaques, vocabulário técnico e parlamentar

### Resumo do tópico

O ASR em português brasileiro enfrenta seis desafios: variação regional e social, com perda de acurácia nos padrões menos treinados; vocabulário técnico e parlamentar, em que palavras raras são trocadas por comuns de som parecido; condições acústicas do plenário; números, datas e abreviaturas, que exigem normalização; fala espontânea; e desequilíbrio de dados, pois há muito menos áudio transcrito em pt-BR que em inglês.

Cada fornecedor chama a mitigação de um modo. O Google usa speech adaptation, e o chirp_3 aceita até 1.000 frases, com recomendação de poucas entradas. A AWS tem custom vocabulary e custom language model, este treinado com texto do domínio e indisponível para pt-BR na tabela oficial. O Azure tem custom speech, e a OpenAI, os parâmetros prompt, keywords e languages.

A adaptação de vocabulário é viés de reconhecimento: empurra o decodificador para termos esperados, não é retreinamento acústico e não garante acerto em qualquer condição. Sotaque se trata com dados acústicos, não com lista de palavras. Carregar nomes de deputados e siglas reduz erros como PEC virar pec, mas não o erro de sotaque.

A banca pode igualar custom vocabulary a retreinamento, dizer que o CLM da AWS se treina com áudio, quando é com texto, afirmar que modelos multilíngues eliminam o problema do pt-BR ou que lista de termos garante reconhecimento em qualquer condição acústica.

## Tópico P2-1.7 — Transcrição em tempo real

### Resumo do tópico

Transcrição em tempo real, ou streaming, processa o áudio enquanto ele chega, em pequenos blocos, devolvendo texto com atraso de segundos. Na transcrição em lote, o áudio completo já existe e é processado inteiro.

No streaming há resultados parciais, que podem mudar, e finais, em geral consolidados quando se detecta fim de enunciado. O endpointing decide, geralmente por silêncio, que o orador terminou a frase: sensibilidade maior responde mais rápido, mas arrisca cortar o orador. A estabilização de parciais reduz as idas e vindas do texto exibido.

Recursos podem faltar em streaming, e isso varia por fornecedor: não há diarização em StreamingRecognize do chirp_3 nem nas sessões Realtime da OpenAI, mas há no Amazon Transcribe. Streaming de saída não é tempo real: na OpenAI, stream=true devolve o texto aos poucos, mas de um arquivo completo.

A legenda ao vivo da TV Câmara tolera correção de texto parcial; notas taquigráficas oficiais convêm melhor em lote, com diarização e revisão. Streaming não é sempre mais preciso, pois o lote vê contexto completo, nem oferece necessariamente os mesmos recursos.

## Tópico P2-1.8 — Ferramentas e APIs: Whisper (Open AI), Google Speech-to-text, Azure Speech, AWS Transcribe

### Resumo do tópico

O conteúdo sobre ferramentas é retrato de 07/10/2026: nomes de modelo e limites mudam, e a prova tende a cobrar a categoria de recurso, como batch ou streaming, diarização, vocabulário, idioma e execução local. O edital grafa Whisper (Open AI), mas a grafia oficial do fornecedor é OpenAI, o que não afeta o julgamento.

O Whisper tem código e pesos publicados no GitHub sob licença MIT e pode rodar localmente, sem enviar áudio a terceiros, o que importa para dados sensíveis. Na API, o whisper-1 serve para timestamps, formatos de legenda e tradução apenas para o inglês, e a OpenAI recomenda hoje outros modelos para transcrição geral, rótulos de locutor e áudio ao vivo.

O Google Cloud Speech-to-Text usa o modelo chirp_3, exclusivo da API V2, com três métodos: StreamingRecognize para tempo real, Recognize para áudio curto e BatchRecognize para longo. Há pt-BR em disponibilidade geral, diarização com pt-BR suportado mas não em StreamingRecognize, e adaptação com até 1.000 frases.

O Azure AI Speech oferece transcrição em tempo real, fast transcription para arquivo e transcrição em lote, custom speech, diarização documentada em tempo real e na fast transcription, e execução em nuvem ou em contêineres on-premises. O Amazon Transcribe oferece batch e streaming, com pt-BR em ambos, custom vocabulary e diarização inclusive em streaming.

A banca tende a trocar o modo em que um recurso existe, como diarização em streaming ou em lote; atribuir código aberto à API, quando o aberto é o modelo Whisper; afirmar limites ou preços sem data; dizer que a tradução do whisper-1 é para qualquer idioma; e tratar modelo local e serviço em nuvem como equivalentes quanto à custódia do áudio.
