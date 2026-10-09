ENTREGA DE LOTE — GCE-CPP → GCE
Data: 07/10/2026
LOTE 1 v2 — RF-ASR (P2, Cargo 11, "Reconhecimento de Fala, Transcrição
e Inteligência Artificial", itens 1.1 a 1.8) — VERSÃO CANÔNICA
PARTE 1/4: cabeçalho, tabela de correções, fontes, itens 1.1 a 1.3
Rodada 2 de 2. Todas as correções C1–C20, S1–S5, reestruturação 4a–4f,
R3 e P6 aplicadas. Todos os itens C/E são AUTORAL.

TABELA DE CORREÇÕES — código → localização no v2
C1  → 1.2, parágrafo "Whisper" (fontes F9, F10)
C2  → 1.3, lista de evidências (bullet Microsoft removido) + parágrafo
      "Contraste: ASR aprimorado por LLM"
C3  → 1.4, parágrafo "Limitações recorrentes" (chirp_3)
C4  → 1.6, "Ferramentas de mitigação", bullet AWS (fonte F11)
C5  → 1.6, "Ferramentas de mitigação", bullet AWS (CLM sem pt-BR)
C6  → (c), par confundível 16
C7  → (d)/(d-G), Q10
C8  → (d)/(d-G), Q15
C9  → (d-G), Q18 (fonte F10)
C10 → (d) versão do estudante, sem [TS]
C11 → 1.7, lista de características, primeiro bullet
C12 → 1.8, Whisper, primeiro bullet (fonte F10)
C13 → 1.8, Whisper, terceiro bullet ("formatos de legenda")
C14 → 1.8, Google, bullet "Diarização"
C15 → 1.8, Azure, bullet "Modos"
C16 → 1.8, AWS, bullets custom vocabulary / CLM
C17 → 1.8, quadro-síntese, coluna "Execução local"
C18 → 1.8, quadro-síntese, Azure/diarização + nota (fonte F12)
C19 → 1.8, "Exemplo parlamentar", itens (a), (b), (c)
C20 → (b) resumo, linhas "LLM DE ÁUDIO NATIVO", "FERRAMENTAS"
S1  → 1.3, bullet Google
S2  → (d-G), Q05 (cita só F8)
S3  → 1.4, parágrafo "Limitações recorrentes" (contraexemplo AWS)
S5  → 1.7, bullet "recursos que podem não existir em streaming"
Q09 → (d)/(d-G), Q09 convertido em item conceitual (1.4, DER × WER)
Q20 → (d)/(d-G), Q20 substituído por item conceitual (1.8, custódia de
      dados: modelo local × serviço em nuvem)
TS  → (d-G): 4 itens [TS] convertidos em gabarito C (Q04, Q08, Q11,
      Q17); 4 itens sem troca convertidos em gabarito E (Q01, Q03, Q07,
      Q12); 10 C / 10 E; 10 [TS]; voláteis: só Q14, Q16, Q18, Q19
R3  → (e), alínea b ("necessária")
P6  → 1.8, Whisper, observação após o título

CONVENÇÃO DE EVIDÊNCIA
[V 07/10/2026 — Fn] = verificado em 07/10/2026 na fonte oficial Fn.
Fontes F9 a F12 foram abertas e confirmadas pela CQFP na rodada 1 e
incorporadas por decisão da GCE; a CPP não as reabriu.
 F1  OpenAI — developers.openai.com/api/docs/guides/speech-to-text
 F2  OpenAI — developers.openai.com/api/docs/guides/audio
 F3  Google Cloud — docs.cloud.google.com/speech-to-text/docs/models/chirp-3
 F4  Microsoft — learn.microsoft.com/azure/ai-services/speech-service/overview
 F5  AWS — docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html
 F6  AWS — aws.amazon.com/documentation-overview/transcribe/
 F7  AWS — referência StartStreamTranscription (docs.aws.amazon.com)
 F8  Google — ai.google.dev/gemini-api/docs/audio e
     ai.google.dev/gemini-api/docs/transcribe
 F9  OpenAI — arxiv.org/abs/2212.04356 (artigo do Whisper, 06/12/2022)
 F10 OpenAI — github.com/openai/whisper (código e pesos, licença MIT)
 F11 AWS — docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html
 F12 Microsoft — learn.microsoft.com/azure/ai-services/speech-service/
     get-started-stt-diarization

=====================================================================
(a) CURSO DIDÁTICO — ITEM A ITEM
=====================================================================

--- 1.1 RECONHECIMENTO AUTOMÁTICO DE FALA (ASR) ---

DEFINIÇÃO
ASR (Automatic Speech Recognition) é a tarefa computacional de converter
um sinal de áudio contendo fala em uma sequência de texto. Faz apenas
isso: fala → texto. Não decide quem falou (isso é diarização/identifi-
cação de locutor) nem o que o texto significa (isso é compreensão de
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
100%. O WER mede só palavras: não mede pontuação, capitalização nem
atribuição de locutor.

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
em todos os aspectos — ele ignora pontuação e locutores.

--- 1.2 MODELOS DE FALA END-TO-END ---

DEFINIÇÃO
Modelo end-to-end ("ponta a ponta") é aquele em que uma única rede
neural é treinada para mapear diretamente o áudio ao texto, substituindo
a construção separada de modelo acústico + léxico + modelo de linguagem.
Toda a rede é otimizada conjuntamente para o objetivo final (texto
correto). Famílias arquiteturais mais citadas: CTC (Connectionist
Temporal Classification), RNN-Transducer e codificador-decodificador com
atenção (Transformers). O Whisper, da OpenAI, é um codificador-decodi-
ficador Transformer treinado com supervisão fraca em larga escala
[V 07/10/2026 — F9, artigo "Robust Speech Recognition via Large-Scale
Weak Supervision", 06/12/2022; F10, repositório openai/whisper].

O que "end-to-end" NÃO significa:
 - não significa "sem dados rotulados": continua precisando de pares
   áudio-texto para treinar (a "supervisão fraca" do Whisper usa
   transcrições existentes na internet, não ausência de transcrição);
 - não significa "sem modelo de linguagem": o conhecimento linguístico
   fica implícito na rede e, em muitos sistemas, ainda se pode acoplar
   um modelo de linguagem externo na decodificação;
 - não significa "sem pré-processamento": o áudio continua sendo
   convertido em espectrograma antes de entrar na rede.

Vantagens: simplicidade de treinamento, melhor desempenho com muitos
dados, menos engenharia manual de pronúncia. Custos: exige grande volume
de dados, é mais difícil de "consertar" pontualmente (não há dicionário
para editar), e erros podem ser fluentes porém falsos (o modelo "inventa"
uma frase plausível onde o áudio é ruim) — modelos end-to-end não são
imunes a esse tipo de erro.

EXEMPLO PARLAMENTAR
Um modelo modular erra o nome de um deputado porque o léxico não contém
a pronúncia; a correção é adicionar a entrada ao dicionário. Um modelo
end-to-end erra o mesmo nome; a correção passa por adaptação de vocabu-
lário (item 1.6) ou por mais dados — não há dicionário para editar.

PEGADINHA PROVÁVEL
Trocar "end-to-end" por "não supervisionado" ou "sem modelo de lingua-
gem". Também: afirmar que modelos end-to-end "nunca alucinam" ou que
"sempre superam" os modulares em qualquer condição — generalizações
indevidas.

--- 1.3 LLMs MULTIMODAIS DE ÁUDIO NATIVO ---

DEFINIÇÃO
Um LLM multimodal de áudio nativo é um modelo de linguagem de grande
porte que recebe o áudio como modalidade de ENTRADA do próprio modelo
(e, em alguns casos, produz áudio como SAÍDA), sem que o fluxo dependa
de um módulo ASR separado que converta fala em texto antes do processa-
mento. O contraste é com a arquitetura EM CASCATA: ASR → LLM (texto) →
TTS (síntese de voz), em que o LLM só vê texto e perde o que não está
nas palavras (entonação, hesitação, sobreposição, risos).

Evidência de que a categoria existe comercialmente:
 - OpenAI: o guia oficial distingue (i) "Audio in Chat Completions"
   (entrada/saída de áudio em requisições multimodais), (ii) a Realtime
   API e o GPT-Live (agentes fala-a-fala) e (iii) os endpoints dedicados
   de transcrição de arquivo e transcrição ao vivo [V 07/10/2026 — F2].
 - Google: a documentação "Audio understanding" descreve o uso de áudio
   como entrada dos modelos Gemini para transcrição, sumarização e
   análise de trechos por timestamp; a mesma documentação informa que
   cada segundo de áudio é representado por 32 tokens [V 07/10/2026 —
   F8]. Há também um modelo dedicado de transcrição (gemini-3.5-trans-
   cribe) com diarização, timestamps por palavra e dicas de vocabulário
   (custom_vocabulary); as dicas de vocabulário não se combinam com
   diarização nem com timestamps por palavra [V 07/10/2026 — F8,
   /transcribe].

Contraste: ASR aprimorado por LLM. O "LLM speech" do Azure AI Speech é
um exemplo de outra categoria — um serviço de ASR aprimorado por LLM,
que transcreve ou traduz áudio PRÉ-GRAVADO [V 07/10/2026 — F4]. Não é
um LLM de áudio nativo conversacional: é reconhecimento de fala com
qualidade e contexto reforçados por LLM. A distinção importa para a
prova: "usa LLM" não é sinônimo de "áudio nativo".

Por que isso importa para transcrição parlamentar: o modelo nativo pode,
na mesma passada, transcrever, resumir, identificar temas e responder
perguntas sobre o áudio. O preço é o risco de "transcrição interpre-
tativa": como o modelo foi treinado para gerar texto plausível, ele
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
cascata só recebe texto. (2) Dizer que o LLM nativo "elimina a necessi-
dade de revisão humana" — contraria o próprio edital (2.2, human in the
loop). (3) Confundir "transcrição por LLM" com "ASR dedicado": o próprio
fornecedor recomenda endpoint dedicado para transcrição de arquivos e
LLM/Realtime para conversação [V 07/10/2026 — F2]. (4) Confundir "ASR
aprimorado por LLM" com "LLM de áudio nativo". (5) Nomes e versões de
modelos mudam em meses: a banca pode cobrar o CONCEITO, não o nome do
produto.

FIM DA PARTE 1/4

ENTREGA DE LOTE — GCE-CPP → GCE
Data: 07/10/2026
LOTE 1 v2 — RF-ASR — PARTE 2/4: itens 1.4 a 1.6

--- 1.4 DIARIZAÇÃO DE FALANTES ---

DEFINIÇÃO
Diarização (speaker diarization) responde a "quem falou quando": segmen-
ta o áudio em trechos e atribui a cada trecho um rótulo de locutor
genérico (Locutor 1, Locutor 2...). Etapas típicas: detecção de ativi-
dade de voz (VAD) → segmentação → extração de "embeddings" de voz por
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
A diarização pode ser ligada à identificação quando se fornecem amos-
tras de referência: a API da OpenAI permite até quatro referências
curtas (2 a 10 s) com nomes de locutores conhecidos para mapear os
segmentos [V 07/10/2026 — F1].

Limitações recorrentes: fala sobreposta (apartes), locutores com vozes
parecidas, mudança rápida de orador, áudio de canal único com ruído de
plenário. A disponibilidade por modo varia entre fornecedores: no
Google Speech-to-Text V2, não há diarização em StreamingRecognize no
modelo chirp_3 [V 07/10/2026 — F3]; na OpenAI, a rotulagem de locutores
está no endpoint de transcrição de arquivo e não é suportada em sessões
Realtime de transcrição [V 07/10/2026 — F1]; em contrapartida, o Amazon
Transcribe oferece diarização em streaming (parâmetro ShowSpeakerLabel)
[V 07/10/2026 — F7]. A lição para a prova: "diarização em streaming"
não é regra geral nem impossibilidade geral — depende do serviço.

EXEMPLO PARLAMENTAR
Na transcrição de uma audiência pública com cinco convidados, a diari-
zação entrega "Locutor 1 ... Locutor 5". Para que o texto saia como
"O SR. FULANO (Relator)", é preciso identificação — por amostra de voz
cadastrada ou, na prática do registro, pela revisão humana com a lista
de inscritos e a ordem de falas. Diarização habilitada, sozinha, não
produz nomes.

PEGADINHA PROVÁVEL
Definir diarização como "identificação" ou "verificação". Afirmar que
diarização está disponível "em qualquer modo" de qualquer serviço — ou
que nunca existe em streaming. Afirmar que a diarização resolve sozinha
a fala sobreposta.

--- 1.5 PONTUAÇÃO AUTOMÁTICA E CAPITALIZAÇÃO ---

DEFINIÇÃO
A saída "crua" de muitos sistemas ASR é texto em minúsculas e sem pon-
tuação, porque o modelo aprende sons, não sinais gráficos. Pontuação
automática e capitalização são a camada que restaura vírgulas, pontos,
interrogações e maiúsculas. Duas formas de obter isso:
 1. Pós-processamento: um modelo separado (geralmente de rotulagem de
    sequência) lê o texto cru — às vezes com pistas de pausa/prosódia —
    e insere os sinais.
 2. Geração direta: modelos end-to-end modernos aprendem a emitir texto
    já pontuado e capitalizado, como parte da própria saída. No chirp_3,
    pontuação e capitalização automáticas são geradas pelo modelo e
    podem ser desativadas [V 07/10/2026 — F3]. No Amazon Transcribe, o
    serviço adiciona pontuação e formatação de números [V 07/10/2026 —
    F6].
Recurso DIFERENTE: "pontuação falada" (spoken punctuation), em que o
orador dita "vírgula", "ponto", e o sistema converte a palavra no sinal.
O Google documenta esse recurso separadamente da pontuação automática
[V 07/10/2026 — F3, menu de recursos]. Isso serve para ditado, não para
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

--- 1.6 DESAFIOS DO ASR EM PORTUGUÊS BRASILEIRO ---

DEFINIÇÃO / MAPA DOS DESAFIOS
 1. Variação regional e social: sotaques, redução de sílabas, "s"
    chiado, vogais abertas/fechadas — o modelo treinado majoritariamente
    com um padrão perde acurácia nos demais.
 2. Vocabulário técnico e parlamentar: siglas (PEC, MPV, CCJ, PL),
    expressões regimentais ("pela ordem", "questão de ordem", "obstru-
    ção", "destaque", "requerimento de urgência"), nomes próprios de
    parlamentares, de municípios e de órgãos, termos jurídicos e lati-
    nismos. Palavras raras ou ausentes do treinamento são substituídas
    por palavras comuns de som parecido.
 3. Condições acústicas do plenário: microfones distintos, reverbe-
    ração, burburinho, apartes e sobreposição.
 4. Números, datas, dinheiro e abreviaturas: "artigo quinze, parágrafo
    segundo" → "art. 15, § 2º" exige normalização (item 2.5).
 5. Fala espontânea: hesitações, reformulações, frases incompletas.
 6. Desequilíbrio de dados: há muito menos áudio transcrito em pt-BR
    que em inglês; modelos multilíngues cobrem pt-BR, mas a acurácia
    varia por idioma (a própria OpenAI avisa que, no Whisper, a acurácia
    varia entre os idiomas suportados) [V 07/10/2026 — F1].

FERRAMENTAS DE MITIGAÇÃO (o que cada fornecedor chama de quê):
 - Google: "speech adaptation"/model adaptation — lista de palavras e
   frases que elevam a probabilidade de reconhecimento; o chirp_3 aceita
   até 1.000 frases, e a própria documentação recomenda poucas entradas
   para não degradar o resto [V 07/10/2026 — F3].
 - AWS: "custom vocabulary" (acrescenta termos ao vocabulário base) [V
   07/10/2026 — F6] e "custom language model" (CLM), treinado com dados
   de TEXTO do domínio fornecidos pelo usuário, recurso distinto do
   custom vocabulary [V 07/10/2026 — F11]. CLM indisponível para pt-BR
   na tabela oficial [V 07/10/2026 — F5]; para pt-BR, o recurso de
   mitigação lexical documentado é o custom vocabulary.
 - Azure: "custom speech" — modelos personalizados treinados com dados
   acústicos, de linguagem e de pronúncia [V 07/10/2026 — F4].
 - OpenAI: parâmetros prompt, keywords e languages no modelo de trans-
   crição recomendado; no whisper-1, prompt limitado a 224 tokens [V
   07/10/2026 — F1].
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

FIM DA PARTE 2/4

ENTREGA DE LOTE — GCE-CPP → GCE
Data: 07/10/2026
LOTE 1 v2 — RF-ASR — PARTE 3/4: itens 1.7, 1.8 e (b) resumo

--- 1.7 TRANSCRIÇÃO EM TEMPO REAL ---

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
   e avisa exatamente esse risco [V 07/10/2026 — F3];
 - estabilização de resultados parciais: recurso para reduzir "idas e
   vindas" do texto exibido (documentado pela AWS como partial-result
   stabilization) [V 07/10/2026 — F7];
 - recursos que podem não existir em streaming — e isso varia por
   fornecedor: diarização ausente em StreamingRecognize do chirp_3 [V
   07/10/2026 — F3] e nas sessões Realtime da OpenAI [V 07/10/2026 —
   F1], mas disponível em streaming no Amazon Transcribe [V 07/10/2026
   — F7]; na AWS, a identificação automática de idioma em streaming não
   pode ser combinada com CLM nem com redação de PII [V 07/10/2026 —
   F7].
Cuidado conceitual: "streaming de SAÍDA" ≠ "tempo real". Na OpenAI, o
endpoint de transcrição de arquivo aceita stream=true para devolver o
texto aos poucos enquanto processa um ARQUIVO COMPLETO; áudio ao vivo
de microfone usa a Realtime/Live transcription, outro fluxo [V
07/10/2026 — F1].

EXEMPLO PARLAMENTAR
Legenda ao vivo da sessão na TV Câmara: streaming com baixa latência;
tolera-se correção de texto parcial. Notas taquigráficas oficiais:
melhor fazer em lote, com diarização e revisão. São dois produtos, dois
fluxos, duas tolerâncias a erro.

PEGADINHA PROVÁVEL
"Streaming é sempre mais preciso" (não; batch vê contexto completo).
"Streaming oferece os mesmos recursos que batch" (não necessariamente;
ver diarização). "stream=true em arquivo = tempo real" (não).

--- 1.8 FERRAMENTAS E APIs ---

Regra de leitura: tudo abaixo é retrato de 07/10/2026. Nomes de modelo
e limites mudam. O que a prova tende a cobrar é a CATEGORIA de recurso
(batch/streaming, diarização, vocabulário, idioma, execução local).

WHISPER (OpenAI)
Observação: o edital grafa "Whisper (Open AI)"; a grafia oficial do
fornecedor é "OpenAI". A diferença não afeta o julgamento de itens.
 - Modelo de código aberto, com código e pesos publicados no GitHub
   (openai/whisper) sob licença MIT; pode ser executado localmente, sem
   enviar áudio a terceiros — relevante para dados sensíveis [V
   07/10/2026 — F10].
 - A documentação da API informa que o Whisper suporta 98 idiomas, com
   acurácia variável por idioma [V 07/10/2026 — F1].
 - Na API: whisper-1 é indicado quando se precisa de timestamps por
   palavra/segmento, formatos de legenda ou tradução para o inglês
   (endpoint /audio/translations, só para inglês). Para transcrição
   geral, a OpenAI recomenda hoje o modelo gpt-transcribe; para rótulos
   de locutor, gpt-4o-transcribe-diarize; para áudio ao vivo, a trans-
   crição Realtime (gpt-live-transcribe) [V 07/10/2026 — F1].
 - Limite de arquivo: 25 MB (dividir arquivos maiores sem cortar frases)
   [V 07/10/2026 — F1].
 - Prompt do whisper-1 limitado a 224 tokens; o modelo não segue
   instruções como um LLM, só usa o prompt como contexto de vocabulário
   [V 07/10/2026 — F1].

GOOGLE CLOUD SPEECH-TO-TEXT [V 07/10/2026 — F3]
 - Modelo atual: chirp_3, exclusivo da API V2.
 - Três métodos: StreamingRecognize (tempo real), Recognize (áudio
   curto, < 1 min) e BatchRecognize (longo).
 - pt-BR em disponibilidade geral (GA) para transcrição.
 - Diarização: não há diarização em StreamingRecognize; pt-BR suportado.
 - Pontuação e capitalização automáticas; transcrição "agnóstica de
   idioma" (language_codes=["auto"]); adaptação com até 1.000 frases;
   prompt de formatação (preview); redutor de ruído (não remove vozes
   humanas de fundo); sensibilidade de endpointing.

AZURE AI SPEECH (Microsoft) [V 07/10/2026 — F4, F12]
 - Modos: transcrição em tempo real (streaming), "fast transcription"
   (arquivo) e transcrição em lote (grandes volumes, assíncrona).
 - Custom speech: modelos personalizados com dados acústicos, de lin-
   guagem e de pronúncia, para ruído e jargão de domínio.
 - Diarização documentada em tempo real e na fast transcription [F12];
   lote e limites por idioma: não verificados.
 - Identificação de idioma; "LLM speech (preview)" para transcribe e
   translate de áudio pré-gravado; execução em nuvem OU em contêineres
   on-premises; acesso por SDK, CLI e REST.

AMAZON TRANSCRIBE (AWS) [V 07/10/2026 — F5, F6, F7, F11]
 - Modos batch (arquivo no S3) e streaming.
 - pt-BR suportado em batch e streaming [F5].
 - Custom vocabulary (termos adicionados ao vocabulário base) [F6];
   custom language model, treinado com dados de texto, distinto do
   custom vocabulary [F11]; CLM indisponível para pt-BR na tabela
   oficial [F5].
 - Filtro de vocabulário (remover termos indesejados); redação de PII;
   particionamento de locutores (diarização), inclusive em streaming
   (ShowSpeakerLabel) [F7]; timestamp por palavra; identificação
   automática de idioma; pontuação e formatação de números [F6].
 - Restrição documentada: identificação de idioma em streaming não se
   combina com CLM nem com redação [F7].

QUADRO-SÍNTESE (categorias, não versões)
 Recurso            | OpenAI        | Google chirp_3 | Azure          | AWS
 Streaming          | sim (Realt.)  | sim            | sim            | sim
 Batch/arquivo      | sim           | sim            | sim            | sim
 Diarização         | sim (arquivo) | sim (não em    | sim (tempo real| sim (batch e
                    |               | streaming)     | e fast) [F12]* | streaming)
 Vocab./adaptação   | prompt/keyw.  | ≤1.000 frases  | custom speech  | CV (CLM sem pt-BR)
 Execução local     | Whisper OSS   | não verificado | contêiner      | não verificado
                    | [F10]         |                |                |
 Tradução p/ inglês | sim (whisper-1)| não verificado| sim (speech    | não verificado
                    |               |                | translation)   |
* Azure: lote e limites por idioma não verificados.

EXEMPLO PARLAMENTAR
Escolha de ferramenta para o Departamento de Taquigrafia: se a exigência
for "áudio não sai do prédio", entre as opções verificadas estão o
Whisper local [F10] e o contêiner Azure [F4]; se for "diarização em
pt-BR em lote", o Google documenta [F3]; se for "legenda ao vivo",
qualquer um dos quatro em modo streaming — sem diarização no caso do
chirp_3 [F3], e sem rótulos de locutor também na transcrição Realtime
da OpenAI [F1].

PEGADINHA PROVÁVEL
Trocar o modo em que um recurso existe (diarização em streaming vs
batch); atribuir "código aberto" à API (o aberto é o modelo Whisper, não
os serviços); afirmar limites numéricos ou preços sem data; dizer que a
tradução do whisper-1 é "para qualquer idioma" (é só para inglês);
tratar modelo local e serviço em nuvem como equivalentes quanto à
custódia do áudio.

=====================================================================
(b) RESUMO DE UMA PÁGINA — LOTE 1 v2
=====================================================================
ASR converte fala em texto; só isso. Métrica: WER = (S+D+I)/N, pode
passar de 100%; não mede pontuação nem locutor. Pipeline clássico:
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
(viés, não retreino), CLM (texto), custom speech (acústico+linguagem+
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

FIM DA PARTE 3/4

ENTREGA DE LOTE — GCE-CPP → GCE
Data: 07/10/2026
LOTE 1 v2 — RF-ASR — PARTE 4/4: (c), (d), (d-G) e (e)

=====================================================================
(c) PARES CONFUNDÍVEIS
=====================================================================
 1. ASR vs diarização vs identificação de locutor: texto / quem-quando /
    quem-é.
 2. Diarização vs verificação de locutor: muitos rótulos / 1 pessoa
    confirmada.
 3. End-to-end vs modular: rede única / módulos separados — ambos
    supervisionados.
 4. End-to-end vs não supervisionado: arquitetura / regime de dados.
 5. LLM de áudio nativo vs cascata ASR→LLM→TTS: áudio no modelo / texto
    no modelo.
 6. Transcrição por LLM vs ASR dedicado: geração interpretativa /
    reconhecimento literal.
 7. Pontuação automática vs pontuação falada: inferida / ditada.
 8. Custom vocabulary (adaptação) vs custom language model: lista de
    termos que enviesa / modelo treinado com corpus de texto.
 9. Adaptação de vocabulário vs modelo acústico customizado: termos /
    sotaque e ruído.
10. Streaming (tempo real) vs batch (arquivo): parciais e latência /
    contexto completo e mais recursos.
11. stream=true em arquivo vs Realtime: saída incremental de arquivo
    pronto / áudio ao vivo.
12. Endpointing sensível vs preciso: rápido e corta / lento e completo.
13. WER vs DER: erro de palavras / erro de atribuição de locutor.
14. Whisper (modelo aberto) vs API OpenAI (serviço): local / nuvem.
15. Tradução (whisper-1, só para inglês) vs transcrição (idioma
    original).
16. Timestamps por palavra vs por enunciado: granularidade fina (cada
    palavra com início e fim) / granularidade grossa (cada frase ou
    trecho).
17. LLM de áudio nativo vs ASR aprimorado por LLM: áudio como entrada
    do LLM / reconhecimento de fala reforçado por LLM.

=====================================================================
(d) VERSÃO DO ESTUDANTE — 20 ITENS C/E (AUTORAL)
=====================================================================
Julgue os itens a seguir (C = certo, E = errado).

Q01. Como o WER é a razão entre erros e palavras de referência, uma
transcrição com WER igual a 0% é necessariamente fiel ao áudio também
em pontuação, capitalização e atribuição de locutor.

Q02. Um sistema ASR, ao converter em texto o áudio de uma sessão,
identifica necessariamente qual parlamentar proferiu cada fala, por ser
essa uma etapa intrínseca do reconhecimento de fala.

Q03. Por integrarem acústica e linguagem em uma rede única, os modelos
de fala end-to-end são imunes a erros de "alucinação", pois só
transcrevem o que foi efetivamente pronunciado.

Q04. Modelos de fala end-to-end continuam dependendo de pares áudio–
texto para treinamento, ainda que a supervisão possa ser "fraca", isto
é, obtida de transcrições preexistentes não produzidas para esse fim.

Q05. LLMs multimodais de áudio nativo recebem o áudio como modalidade de
entrada do próprio modelo, sem que o fluxo dependa de um módulo ASR
separado para converter a fala em texto antes do processamento.

Q06. Na arquitetura em cascata (ASR → LLM → TTS), o LLM processa
diretamente as características acústicas da fala, razão pela qual
preserva informação prosódica como entonação e hesitação.

Q07. Como a diarização atribui a cada falante um rótulo próprio, um
sistema com diarização habilitada é suficiente para que a transcrição
de uma audiência pública exiba o nome de cada convidado que falou.

Q08. A verificação de locutor difere da diarização por operar em
comparação um-para-um contra uma identidade alegada, de modo que um
sistema pode diarizar uma sessão inteira sem verificar nem identificar
ninguém.

Q09. A métrica DER (diarization error rate) agrega erros de atribuição
de falante, fala não detectada e falsos alarmes, sendo distinta do WER,
que mede erros de palavras.

Q10. Modelos end-to-end modernos podem gerar pontuação e capitalização
como parte da própria saída de texto, ao passo que arquiteturas
tradicionais de ASR em geral recorrem a etapa posterior de restauração
de pontuação.

Q11. Pontuação falada e pontuação automática são recursos distintos: na
primeira, o orador dita o sinal de pontuação; na segunda, o sistema
infere o sinal a partir da estrutura da frase e de pistas prosódicas.

Q12. Uma vez carregada uma lista de termos parlamentares por adaptação
de vocabulário, o sistema ASR passa a reconhecer corretamente esses
termos em qualquer condição acústica, independentemente do sotaque do
orador.

Q13. A adaptação de vocabulário (speech adaptation ou custom vocabulary)
consiste no retreinamento do modelo acústico com gravações do domínio,
sendo, por isso, a técnica indicada para corrigir erros causados por
sotaques regionais.

Q14. No Amazon Transcribe, o custom vocabulary amplia o vocabulário base
com termos do domínio, enquanto o custom language model é construído a
partir de dados de texto fornecidos pelo usuário.

Q15. Na transcrição em tempo real (streaming), o sistema pode emitir
resultados parciais sujeitos a revisão, e o resultado final de um trecho
em geral é consolidado após a detecção do fim do enunciado
(endpointing).

Q16. Na API de transcrição de arquivos da OpenAI, o parâmetro
stream=true transforma a requisição em transcrição em tempo real de
áudio ao vivo, equivalendo ao uso de uma sessão da Realtime API.

Q17. Elevar a sensibilidade de endpointing no reconhecimento em
streaming reduz a latência de finalização dos resultados, mas pode
fragmentar enunciados quando o orador faz pausas, de modo que latência
e acurácia não melhoram simultaneamente.

Q18. O Whisper, da OpenAI, foi disponibilizado como modelo de código
aberto executável localmente, enquanto a API da OpenAI oferece, além do
whisper-1, modelos de transcrição mais recentes recomendados para
transcrição geral de arquivos.

Q19. O Azure AI Speech oferece transcrição em tempo real e em lote, mas,
por tratar-se de serviço exclusivamente em nuvem, não permite execução
em contêineres on-premises.

Q20. Modelo de ASR de código aberto executado localmente e serviço de
ASR em nuvem são equivalentes quanto à custódia do áudio, pois em ambos
os casos a instituição mantém controle exclusivo sobre os dados
processados.

=====================================================================
(d-G) GABARITO COMENTADO
=====================================================================
Legenda: [TS] = troca sutil de conceito; VOLÁTIL = depende de fato de
produto verificado em 07/10/2026; "convertido" = item do v1 alterado
nesta rodada; "novo" = item criado nesta rodada.

Q01. E — convertido (era C). WER mede apenas palavras; pontuação,
capitalização e locutor estão fora da métrica, então WER 0% não garante
fidelidade nesses aspectos. Erro por extrapolação.

Q02. E [TS]. ASR produz texto; atribuir falas a locutores é diarização
(rótulos) ou identificação (nomes), módulos distintos.

Q03. E — convertido (era C). Modelos end-to-end podem produzir trechos
fluentes porém falsos onde o áudio é ruim; a arquitetura não imuniza
contra alucinação. Erro por generalização.

Q04. C [TS] — convertido (era E). Falsa pegadinha: "supervisão fraca"
parece sugerir ausência de rótulos, mas significa transcrições
preexistentes; pares áudio–texto continuam necessários.

Q05. C. É o que distingue o modelo nativo da arquitetura em cascata:
áudio como entrada do próprio LLM [V 07/10/2026 — F8].

Q06. E [TS]. Na cascata o LLM recebe apenas o texto do ASR; prosódia se
perde — justamente a limitação que o áudio nativo pretende superar.

Q07. E — convertido (era C). Diarização entrega rótulos genéricos
(Locutor 1, 2...); exibir nomes exige identificação (amostra cadastrada
ou revisão humana). Erro por extrapolação.

Q08. C [TS] — convertido (era E). Falsa pegadinha: a frase soa invertida
mas está correta — verificação é 1:1 contra identidade alegada; diarizar
não exige verificar nem identificar.

Q09. C — convertido (era item de produto). DER soma erro de falante,
fala perdida e falso alarme; WER soma substituições, deleções e
inserções de palavras. Métricas distintas para tarefas distintas.

Q10. C. Modelos end-to-end podem emitir texto já pontuado e
capitalizado; pipelines clássicos em geral restauram pontuação em etapa
posterior.

Q11. C [TS] — convertido (era E). Falsa pegadinha: o item parece
confundir os dois recursos, mas os distingue corretamente — ditado do
sinal versus inferência do sinal.

Q12. E — convertido (era C). Adaptação de vocabulário enviesa o
reconhecimento para termos esperados; não garante acerto em qualquer
condição acústica nem corrige sotaque. Erro por generalização.

Q13. E [TS]. Adaptação é lista de termos que enviesa o reconhecimento,
não retreino acústico; sotaque pede dados acústicos/modelo customizado.

Q14. C — VOLÁTIL (verificado em 07/10/2026). Distinção documentada pela
AWS: custom vocabulary amplia o vocabulário base [F6]; custom language
model é treinado com dados de texto [F11].

Q15. C. Funcionamento padrão do streaming: parciais revisáveis e final
em geral consolidado após o fim do enunciado.

Q16. E [TS] — VOLÁTIL (verificado em 07/10/2026). stream=true devolve
texto incremental de um arquivo já completo; áudio ao vivo usa a
transcrição Realtime, fluxo distinto [F1].

Q17. C [TS] — convertido (era E). Falsa pegadinha: o item parece
afirmar ganho duplo, mas afirma o trade-off correto — menor latência,
risco de fragmentar enunciados.

Q18. C — VOLÁTIL (verificado em 07/10/2026). Código e pesos abertos no
repositório openai/whisper, licença MIT [F10]; a API recomenda
gpt-transcribe para transcrição geral e reserva whisper-1 a timestamps,
legendas e tradução [F1].

Q19. E [TS] — VOLÁTIL (verificado em 07/10/2026). A documentação oficial
prevê implantação em nuvem ou on-premises via contêineres [F4].

Q20. E [TS] — novo (substitui item de produto). Em serviço em nuvem o
áudio é enviado a infraestrutura de terceiro; só a execução local
mantém o áudio sob controle exclusivo da instituição. Equivalência de
custódia é falsa.

Distribuição: 10 C (Q04, Q05, Q08, Q09, Q10, Q11, Q14, Q15, Q17, Q18) e
10 E (Q01, Q02, Q03, Q06, Q07, Q12, Q13, Q16, Q19, Q20).
Itens [TS]: 10 (Q02, Q04, Q06, Q08, Q11, Q13, Q16, Q17, Q19, Q20), dos
quais 4 com gabarito C e 6 com gabarito E.
Itens sem troca com gabarito E (extrapolação/generalização): 4 (Q01,
Q03, Q07, Q12).
Dependentes de produto (VOLÁTIL): 4 — Q14, Q16, Q18, Q19; risco ALTO:
Q16 (nome de parâmetro e fluxo de API); demais: risco baixo/médio.
Cobertura: 1.1 (Q01–Q02), 1.2 (Q03–Q04), 1.3 (Q05–Q06), 1.4 (Q07–Q09),
1.5 (Q10–Q11), 1.6 (Q12–Q14), 1.7 (Q15–Q17), 1.8 (Q18–Q20).

=====================================================================
(e) HIPÓTESE DE QUESTÃO DISCURSIVA — ENUNCIADO (até 20 linhas)
=====================================================================
Rótulo: AUTORAL. Roteiro de resposta já consolidado pela GCE (não
reemitido).

A Câmara dos Deputados estuda adotar transcrição automática do áudio das
sessões plenárias como insumo para o registro taquigráfico, com dois
produtos distintos: legendas exibidas ao vivo na TV Câmara e notas
taquigráficas oficiais, publicadas após revisão. Considerando os
fundamentos do reconhecimento automático de fala e das tecnologias
associadas, redija texto dissertativo em que você:
 a) explique por que os dois produtos exigem modos de processamento
    diferentes (tempo real e lote), indicando um recurso que tende a
    estar disponível em um modo e não no outro;
 b) diferencie diarização de falantes e identificação de locutor e
    indique qual delas é necessária para que a nota oficial exiba o nome
    do parlamentar que falou;
 c) aponte dois desafios específicos do português brasileiro falado em
    plenário e, para cada um, o tipo de recurso técnico adequado para
    mitigá-lo, distinguindo adaptação de vocabulário de customização
    acústica.

FIM DA PARTE 4/4
FIM DO LOTE 1 v2
