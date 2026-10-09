CONSOLIDAÇÃO GCE — LOTE 1 (RF-ASR, P2 1.1–1.8)
Data: 08/10/2026 | Base: GCE_Lote1_v2_CPP.md (LOTE 1 v2, versão canônica)
QA final: GCE-CQFP, rodada 2, APROVADO (verificado em 07/10/2026)

PARTE A — ERRATA OFICIAL (E1 a E6 da CQFP; aplicada pela GCE)
Onde houver conflito entre o v2 e esta errata, prevalece a errata.

E1 (d) Q07 — onde se lê "um sistema com diarização habilitada é
   suficiente", leia-se "um sistema com diarização habilitada, por si só,
   sem amostras de voz de referência, é suficiente".
E2 (d) Q08 — onde se lê "de modo que um sistema pode diarizar", leia-se
   "e um sistema pode diarizar".
E3 (d) Q11 — onde se lê "e de pistas prosódicas", leia-se "e,
   eventualmente, de pistas prosódicas".
E4 Item 1.1 — onde se lê "O WER mede só palavras: não mede pontuação,
   capitalização nem atribuição de locutor.", leia-se "No cálculo usual,
   sobre texto normalizado, o WER não mede pontuação nem capitalização;
   a atribuição de locutor fica fora do WER em qualquer convenção."
   Na pegadinha do 1.1, onde se lê "ele ignora pontuação e locutores",
   leia-se "no cálculo usual ele ignora pontuação, e em qualquer
   convenção ignora locutores".
   Coerência (d-G) Q01: onde se lê "WER mede apenas palavras; pontuação,
   capitalização e locutor estão fora da métrica", leia-se "no cálculo
   usual, pontuação e capitalização ficam fora do WER, e a atribuição de
   locutor fica fora em qualquer convenção". Gabarito E mantido.
E5 (b) Resumo, linha "PT-BR" — onde se lê "CLM (texto)", leia-se "CLM
   (texto; indisponível para pt-BR na AWS)".
E6 (d-G) Linha final — onde se lê "risco ALTO: Q16 (nome de parâmetro e
   fluxo de API); demais: risco baixo/médio", leia-se "nenhum de risco
   ALTO; Q16 e Q18: MÉDIO; Q14 e Q19: BAIXO (classificação final da
   CQFP, 07/10/2026)".

PARTE B — PADRÃO DE RESPOSTA DA DISCURSIVA (e) — formato D-RUBRICA
Rótulo: AUTORAL. Reconciliação da dupla cega CPP × CQFP (R1 a R4).

PADRÃO DE RESPOSTA
A legenda ao vivo exige transcrição em tempo real (streaming): o áudio é
processado à medida que chega, com prioridade para baixa latência,
resultados parciais sujeitos a revisão e finalização de cada trecho por
detecção de fim de fala (endpointing), com contexto limitado. A nota
taquigráfica oficial admite processamento em lote: o áudio completo
oferece contexto integral, maior acurácia e mais recursos de
pós-processamento, e o resultado passa por revisão humana antes da
publicação. Exemplo de recurso que tende a existir em um modo e não no
outro: a diarização, que em alguns serviços só existe no modo arquivo.
A diarização responde "quem falou quando": segmenta o áudio e atribui
rótulos genéricos (Locutor 1, Locutor 2), por semelhança de voz, sem
saber quem é cada pessoa. A identificação de locutor associa a voz a
uma pessoa determinada, com base em cadastro ou amostras de referência,
ou é feita por atribuição humana a partir da lista de oradores. Para que
a nota oficial exiba o nome do parlamentar, é necessária a
identificação; a diarização, sozinha, não basta.
No português brasileiro falado em plenário, o vocabulário técnico e
regimental (siglas como PEC e CCJ, expressões como "questão de ordem",
nomes de parlamentares e municípios) é mitigado por adaptação de
vocabulário, isto é, listas de termos que enviesam a decodificação, ou
por modelo de linguagem treinado com corpus de texto, sem retreino
acústico. Já os sotaques regionais e as condições acústicas do plenário
(reverberação, ruído, fala sobreposta) exigem customização acústica:
ajuste do modelo com áudio do domínio e dos falantes. Lista de termos
não corrige sotaque.

QUESITOS AVALIADOS
Quesito 2.1 — Modos de processamento (tempo real × lote) [valor
máximo: 5,00]
Conceito 0 — Não distinguiu os modos, ou os inverteu.
Conceito 1 — Abordou corretamente apenas um dos seguintes aspectos:
  (i) legenda ao vivo → tempo real, com processamento à medida que o
      áudio chega e prioridade de latência;
  (ii) resultados parciais revisáveis e finalização por endpointing,
       com contexto limitado;
  (iii) nota oficial → lote, com áudio completo, contexto integral e
        maior acurácia;
  (iv) integração do lote com a revisão humana antes da publicação;
  (v) indicação, com justificativa, de recurso disponível em um modo e
      não no outro. Respostas aceitas: diarização ou atribuição de
      locutor; resultados parciais; pós-processamento ou formatação
      mais completos em lote.
Conceito 2 — Abordou corretamente apenas dois ou três dos aspectos
  enumerados.
Conceito 3 — Abordou corretamente apenas quatro dos aspectos
  enumerados.
Conceito 4 — Abordou corretamente os cinco aspectos enumerados.

Quesito 2.2 — Diarização × identificação de locutor [valor máximo:
4,00]
Conceito 0 — Confundiu os conceitos, ou definiu diarização como
  identificação ou verificação.
Conceito 1 — Abordou corretamente apenas um dos seguintes aspectos:
  (i) diarização como "quem falou quando", com rótulos genéricos e sem
      identidade;
  (ii) identificação como associação da voz a uma pessoa, por cadastro,
       amostras de referência ou atribuição humana;
  (iii) indicação de que a identificação é a necessária para exibir o
        nome, e de que a diarização sozinha não basta.
Conceito 2 — Abordou corretamente apenas dois dos aspectos enumerados.
Conceito 3 — Abordou corretamente os três aspectos enumerados.
(A menção correta à verificação de locutor, 1:1, não altera o
conceito.)

Quesito 2.3 — Desafios do pt-BR em plenário e mitigação [valor máximo:
6,00]
Conceito 0 — Não apontou desafio específico do pt-BR em plenário.
Conceito 1 — Abordou corretamente apenas um dos seguintes aspectos:
  (i) desafio lexical (siglas, expressões regimentais, nomes próprios);
  (ii) mitigação lexical por adaptação de vocabulário ou por modelo de
       linguagem com corpus de texto, sem retreino acústico;
  (iii) desafio acústico (sotaques, reverberação, ruído, sobreposição);
  (iv) mitigação acústica por customização com áudio do domínio e dos
       falantes;
  (v) distinção explícita entre adaptação de vocabulário e
      customização acústica.
Conceito 2 — Abordou corretamente apenas dois ou três dos aspectos
  enumerados.
Conceito 3 — Abordou corretamente apenas quatro dos aspectos
  enumerados.
Conceito 4 — Abordou corretamente os cinco aspectos enumerados.
Anulam o aspecto em que ocorrem:
- afirmar que lista de termos corrige sotaque;
- afirmar que adaptação de vocabulário retreina o modelo acústico;
- afirmar que modelo multilíngue elimina o problema.
Normalização de números e abreviaturas é aceita como desafio adicional,
mas não substitui os aspectos (ii), (iv) e (v).

Base normativa: não se aplica (questão sem dispositivo normativo).
Nota de correção (edital, 9.8.5.1, d): NQ = NC − 3 × NE ÷ TL, com NC
máximo de 15,00. Os valores máximos por quesito (5 / 4 / 6) são HIPÓTESE
do Projeto: os padrões oficiais publicam os conceitos, mas não o peso de
cada quesito.

FIM DA CONSOLIDAÇÃO GCE — LOTE 1

ADENDO GCE — 08/10/2026 — CORREÇÃO DE VALORES (alinhamento ao caderno
oficial)
Motivo: o caderno oficial da Câmara (4536C347…pdf) atribui a cada
questão até 15,00 pontos, dos quais até 0,70 à apresentação e estrutura
textual. Os tópicos de conteúdo somam 14,30 (6,00 + 7,00 + 1,30). Os
valores da Parte B somavam 15,00 só em conteúdo e estão corrigidos.

E7 Parte B, Quesito 2.3: onde se lê "[valor máximo: 6,00]", leia-se
   "[valor máximo: 5,30]". Fica acrescida a linha: "Apresentação e
   estrutura textual: 0,70".
   Na nota de correção, onde se lê "Os valores máximos por quesito
   (5 / 4 / 6)", leia-se "(5,00 / 4,00 / 5,30), mais 0,70 de
   apresentação".
E8 Enunciado (e) do LOTE 1 v2 (GCE_Lote1_v2_CPP.md): acrescentar
   "[valor: 5,00 pontos]" ao fim da alínea a, "[valor: 4,00 pontos]" ao
   fim da alínea b e "[valor: 5,30 pontos]" ao fim da alínea c.
   Antes do enunciado, acrescentar: "Ao domínio do conteúdo serão
   atribuídos até 15,00 pontos, dos quais até 0,70 ponto à apresentação
   e estrutura textual."
FIM DO ADENDO

ADENDO 2 GCE — 08/10/2026 — decorrente do QA do Lote 1-C
E9 Curso do LOTE 1 v2, item 1.2, terceiro tópico de "O que end-to-end
   NÃO significa": onde se lê "o áudio continua sendo convertido em
   espectrograma antes de entrar na rede", leia-se "em geral (por
   exemplo, no Whisper) o áudio é convertido em espectrograma antes de
   entrar na rede; há modelos que recebem a forma de onda bruta (por
   exemplo, wav2vec 2.0, arXiv 2006.11477, seção 2 [V 08/10/2026])".
   O mesmo ajuste vale para a linha "END-TO-END" do resumo (b), se
   houver a mesma generalização.
R-J (reverificação de 04 a 08/01/2027, a cargo da GCE-CQFP): incluir o
   fato de produto do curso 1.4 "até quatro referências de 2 a 10 s com
   nomes de locutores [F1]", além dos itens Q14, Q16, Q18 e Q19.
FIM DO ADENDO 2

ADENDO 3 GCE — 08/10/2026 — nome do departamento
E10 Curso do LOTE 1 v2, item 1.8, "EXEMPLO PARLAMENTAR": onde se lê
    "Escolha de ferramenta para o Departamento de Taquigrafia", leia-se
    "Escolha de ferramenta para o departamento de registro da Câmara
    (Derep, antigo DETAQ; Ato da Mesa nº 251/2026)".
FIM DO ADENDO 3