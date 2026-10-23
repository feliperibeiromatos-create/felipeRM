# Discursivas — padrões de resposta

## D1 — Questão

### Padrão de resposta

```text
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

Quesito 2.3 — Desafios do pt-BR em plenário e mitigação [valor máximo: 5,30]
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

Apresentação e estrutura textual: 0,70

Base normativa: não se aplica (questão sem dispositivo normativo).
Nota de correção (edital, 9.8.5.1, d): NQ = NC − 3 × NE ÷ TL, com NC
máximo de 15,00. Os valores máximos por quesito (5,00 / 4,00 / 5,30), mais 0,70 de apresentação são HIPÓTESE
deste material: os padrões oficiais publicam os conceitos, mas não o peso de
cada quesito.
```

### Aspectos (valor)

- (1) explique por que os dois produtos exigem modos de processamento diferentes (tempo real e lote), indicando um recurso que tende a estar disponível em um modo e não no outro; — valor: 5,00
- (2) diferencie diarização de falantes e identificação de locutor e indique qual delas é necessária para que a nota oficial exiba o nome do parlamentar que falou; — valor: 4,00
- (3) aponte dois desafios específicos do português brasileiro falado em plenário e, para cada um, o tipo de recurso técnico adequado para mitigá-lo, distinguindo adaptação de vocabulário de customização acústica. — valor: 5,30

### Quesitos

- **2.1** — Modos de processamento (tempo real × lote)
  - Conceito 0 — Não distinguiu os modos, ou os inverteu.
  - Conceito 1 — Abordou corretamente apenas um dos seguintes aspectos: (i) legenda ao vivo → tempo real, com processamento à medida que o áudio chega e prioridade de latência; (ii) resultados parciais revisáveis e finalização por endpointing, com contexto limitado; (iii) nota oficial → lote, com áudio completo, contexto integral e maior acurácia; (iv) integração do lote com a revisão humana antes da publicação; (v) indicação, com justificativa, de recurso disponível em um modo e não no outro. Respostas aceitas: diarização ou atribuição de locutor; resultados parciais; pós-processamento ou formatação mais completos em lote.
  - Conceito 2 — Abordou corretamente apenas dois ou três dos aspectos enumerados.
  - Conceito 3 — Abordou corretamente apenas quatro dos aspectos enumerados.
  - Conceito 4 — Abordou corretamente os cinco aspectos enumerados.
- **2.2** — Diarização × identificação de locutor
  - Conceito 0 — Confundiu os conceitos, ou definiu diarização como identificação ou verificação.
  - Conceito 1 — Abordou corretamente apenas um dos seguintes aspectos: (i) diarização como "quem falou quando", com rótulos genéricos e sem identidade; (ii) identificação como associação da voz a uma pessoa, por cadastro, amostras de referência ou atribuição humana; (iii) indicação de que a identificação é a necessária para exibir o nome, e de que a diarização sozinha não basta.
  - Conceito 2 — Abordou corretamente apenas dois dos aspectos enumerados.
  - Conceito 3 — Abordou corretamente os três aspectos enumerados.
- **2.3** — Desafios do pt-BR em plenário e mitigação
  - Conceito 0 — Não apontou desafio específico do pt-BR em plenário.
  - Conceito 1 — Abordou corretamente apenas um dos seguintes aspectos: (i) desafio lexical (siglas, expressões regimentais, nomes próprios); (ii) mitigação lexical por adaptação de vocabulário ou por modelo de linguagem com corpus de texto, sem retreino acústico; (iii) desafio acústico (sotaques, reverberação, ruído, sobreposição); (iv) mitigação acústica por customização com áudio do domínio e dos falantes; (v) distinção explícita entre adaptação de vocabulário e customização acústica.
  - Conceito 2 — Abordou corretamente apenas dois ou três dos aspectos enumerados.
  - Conceito 3 — Abordou corretamente apenas quatro dos aspectos enumerados.
  - Conceito 4 — Abordou corretamente os cinco aspectos enumerados.

## D2 — Questão

### Padrão de resposta

```text
Valores conforme o caderno oficial (questão: 15,00, com 0,70 de
apresentação; peça: 30,00, com 1,50 de apresentação). O peso de cada
quesito é HIPÓTESE deste material, alinhado à soma oficial.
Base normativa: não exigível. A menção correta à Portaria DG nº
77/2017 (Manual de Redação) é aceita, mas não exigida. Não se exige
convenção específica da Câmara.

PADRÃO DE RESPOSTA
A transcrição automática é a conversão do áudio em texto por software
de reconhecimento de fala, sem intervenção humana; o produto é um
rascunho. A degravação é a conversão da gravação em texto por pessoa
que a ouve, depois da gravação, com ou sem ferramentas. A revisão
humana confronta o texto com o áudio e com o contexto (pauta, lista de
oradores, glossário), corrige e responde pela versão publicada. No
fluxo human in the loop, nenhum texto automático é publicado sem essa
validação.
Critérios de fidelidade: preservar o que foi dito, sem acrescentar nem
omitir; e corrigir nomes, siglas, números e a atribuição das falas. O
erro que altera o sentido (omitir uma negação, trocar número, nome ou
orador) é mais grave que o erro de forma. Diante de trecho inaudível, o
revisor confere o áudio e, persistindo a dúvida, marca o trecho; não o
completa por conjectura.
A revisão em dupla submete o texto a um segundo revisor independente. A
auditoria de amostras reexamina parte do material para estimar a
qualidade do conjunto e realimentar o fluxo. O SLA fixa metas de prazo
e de qualidade e a forma de medi-las. A amostra estima, mas não garante
ausência de erro no que não foi examinado.

QUESITOS AVALIADOS
Quesito 2.1 — Transcrição automática, degravação, revisão e HITL
[valor: 5,00]
Aspectos:
 (i) transcrição automática: software, sem intervenção humana,
     rascunho;
 (ii) degravação: por pessoa, a posteriori;
 (iii) revisão humana: confronto com áudio e contexto e
       responsabilidade pela versão publicada;
 (iv) HITL: validação humana obrigatória antes da publicação; a saída
      automática não é registro oficial.
Conceito 0 — Não abordou ou abordou de forma totalmente equivocada.
Conceito 1 — Apenas um aspecto. Conceito 2 — Apenas dois. Conceito 3 —
Apenas três. Conceito 4 — Os quatro.
Anula o aspecto (iv): afirmar que a boa qualidade do ASR dispensa a
revisão.

Quesito 2.2 — Fidelidade, gravidade e inaudível [valor: 5,00]
Aspectos:
 (v) primeiro critério (exatidão ou preservação do sentido);
 (vi) segundo critério distinto. Lista fechada: completude e atribuição
      correta das falas; correção de nomes, siglas e números;
      consistência e uniformidade; conformidade com o manual ou guia da
      Casa;
 (vii) erro de sentido mais grave que erro de forma;
 (viii) inaudível: conferir e marcar, sem conjectura.
Conceito 0 a 4: por contagem, de "apenas um" a "os quatro".
Anulam o aspecto em que ocorrem: fidelidade como literalidade absoluta;
completar o inaudível sem marcação.

Quesito 2.3 — Controle de qualidade [valor: 4,30]
Aspectos:
 (ix) revisão em dupla com segundo revisor independente;
 (x) auditoria de amostras: estimar a qualidade e realimentar;
 (xi) SLA: metas de prazo e qualidade, com medição;
 (xii) limitação: a amostra estima e não garante (ou depende da
       representatividade).
Conceito 0 a 4: por contagem, de "apenas um" a "os quatro".
Anulam o aspecto em que ocorrem: a mesma pessoa relendo equivaler à
revisão em dupla; amostra sem erro provar lote sem erro.
```

### Aspectos (valor)

- (1) diferencie transcrição automática, degravação e revisão humana, indicando a função da revisão humana nesse fluxo (human in the loop); — valor: 5,00
- (2) apresente dois critérios de qualidade e fidelidade que a revisão deve observar, distinguindo o erro que altera o sentido do erro de forma, e indique como o revisor deve proceder diante de trecho inaudível; — valor: 5,00
- (3) explique como a revisão em dupla, a auditoria de amostras e o acordo de nível de serviço (SLA) contribuem para o controle de qualidade do fluxo, indicando uma limitação da auditoria por amostragem. — valor: 4,30

### Quesitos

- **2.1** — Transcrição automática, degravação, revisão e HITL
  - Conceito 0 — Não abordou ou abordou de forma totalmente equivocada.
  - Conceito 1 — Apenas um aspecto.
  - Conceito 2 — Apenas dois.
  - Conceito 3 — Apenas três.
  - Conceito 4 — Os quatro.
- **2.2** — Fidelidade, gravidade e inaudível
  - Conceito 0 a 4: por contagem, de "apenas um" a "os quatro".
- **2.3** — Controle de qualidade
  - Conceito 0 a 4: por contagem, de "apenas um" a "os quatro".

## D3 — Peça técnica

### Padrão de resposta

```text
Valores conforme o caderno oficial (questão: 15,00, com 0,70 de
apresentação; peça: 30,00, com 1,50 de apresentação). O peso de cada
quesito é HIPÓTESE deste material, alinhado à soma oficial.
Base normativa: não exigível. A menção correta à Portaria DG nº
77/2017 (Manual de Redação) é aceita, mas não exigida. Não se exige
convenção específica da Câmara.

PADRÃO DE RESPOSTA (síntese)
O parecer identifica a consulta (padronização do texto de transcrição
automática com revisão humana em reuniões de comissões) e relata os
três problemas.
Na formatação: rótulo padronizado de orador; sinalização de toda troca;
aparte e fala do Presidente como intervenções distintas; eventos não
falados e inaudível em convenção única e distinguível. O rótulo da
diarização não identifica o orador.
Na normalização: regra institucional única e glossário. A normalização
padroniza a forma e não o conteúdo dito, e a normalização inversa
automática exige conferência das ambiguidades.
No vocabulário: os erros vêm de termos raros ou fora do vocabulário
(OOV). Mitigam-se com lista de termos e com adaptação do modelo de
linguagem com textos do domínio. Há riscos, a atualização é periódica
e a avaliação se faz em dados separados.
Conclui com recomendações articuladas aos problemas, mantém a revisão
humana e indica medida de controle de qualidade com verificação do
resultado. A conclusão é em forma de opinião técnica fundamentada.

QUESITOS AVALIADOS
Quesito 2.1 — Objeto e relato [valor: 2,00]
Aspectos:
 (i) objeto da consulta;
 (ii) relato sintético dos três problemas.
Conceito 0 — Não abordou. Conceito 1 — Apenas (i) ou apenas (ii).
Conceito 2 — (i) e (ii).

Quesito 2.2 — Formatação [valor: 8,00]
Aspectos:
 (iii) identificação padronizada do orador;
 (iv) sinalização de toda troca de orador;
 (v) aparte e fala do Presidente distintos do discurso principal;
 (vi) eventos não falados em convenção única e distinguível. Lista
      fechada: palmas, risos, trecho inaudível, sobreposição de vozes,
      manifestações do plenário;
 (vii) o rótulo da diarização não identifica o orador; a identificação
       vem de cadastro, lista de inscritos ou revisão humana.
Conceito 0 — Não abordou ou abordou de forma totalmente equivocada.
Conceito 1 — Um aspecto. Conceito 2 — Dois. Conceito 3 — Três ou
quatro. Conceito 4 — Os cinco.
Anula o aspecto (vii): tratar o rótulo da diarização como identificação.

Quesito 2.3 — Normalização [valor: 6,00]
Aspectos:
 (viii) regra institucional única (manual ou guia);
 (ix) a normalização padroniza a forma, não o conteúdo;
 (x) normalização inversa automática com conferência humana das
     ambiguidades;
 (xi) glossário de siglas e termos, para consistência e busca.
Conceito 0 a 4: por contagem, de "apenas um" a "os quatro".
Conceito 0 também quando o candidato trata a normalização como
correção do conteúdo.

Quesito 2.4 — Vocabulário, adaptação e risco [valor: 7,00]
Aspectos:
 (xii) causa: termos raros ou OOV trocados por palavras de som
       parecido;
 (xiii) lista ou reforço de termos (nomes, siglas, expressões
        regimentais);
 (xiv) adaptação do modelo de linguagem com textos do domínio, atuando
       sobre sequências e contexto;
 (xv) risco, em lista fechada: sobre-reforço com inserção de termo não
      dito; listas desatualizadas (a cada legislatura); a adaptação não
      trata a causa acústica (ruído, sotaque), que pede dados acústicos;
 (xvi) atualização periódica e avaliação em dados distintos dos usados
       para adaptar.
Conceito 0 — Não abordou, ou equiparou adaptação a retreino acústico.
Conceito 1 — Um aspecto. Conceito 2 — Dois. Conceito 3 — Três ou
quatro. Conceito 4 — Os cinco.
Nota de correção: sem trava "obrigatoriamente", conforme o modelo
oficial. O risco (xv) é aspecto próprio, e sem ele não se chega ao
conceito máximo.

Quesito 2.5 — Conclusão e recomendações [valor: 5,50]
Aspectos:
 (xvii) recomendações articuladas aos três problemas;
 (xviii) manutenção da revisão humana antes da publicação;
 (xix) medida de controle de qualidade com verificação do resultado,
       em lista fechada: revisão em dupla; auditoria por amostragem;
       indicadores ou SLA com medição antes e depois;
 (xx) conclusão em forma de opinião técnica fundamentada.
Conceito 0 — Não concluiu nem recomendou. Conceito 1 — Um aspecto.
Conceito 2 — Dois ou três. Conceito 3 — Os quatro.

Nota (edital, 9.8.5.2, d): NPT = NC − 6 × NE ÷ TL.
Gênero da peça: HIPÓTESE por analogia para o Cargo 11. Se o
gênero real for outro, os quesitos 2.2 a 2.4 valem como conteúdo.
```

### Aspectos (valor)

- (1) objeto da consulta e relato sintético dos problemas observados; — valor: 2,00
- (2) formatação da transcrição: identificação de oradores, sinalização da troca de orador, aparte e fala do Presidente, eventos não falados; — valor: 8,00
- (3) normalização de números, datas, siglas e abreviações; — valor: 6,00
- (4) vocabulário técnico parlamentar e adaptação do sistema, com indicação de um risco dessa adaptação; — valor: 7,00
- (5) conclusão com recomendações objetivas, incluindo ao menos uma medida de controle de qualidade para verificar o resultado. — valor: 5,50

### Quesitos

- **2.1** — Objeto e relato
  - Conceito 0 — Não abordou.
  - Conceito 1 — Apenas (i) ou apenas (ii).
  - Conceito 2 — (i) e (ii).
- **2.2** — Formatação
  - Conceito 0 — Não abordou ou abordou de forma totalmente equivocada.
  - Conceito 1 — Um aspecto.
  - Conceito 2 — Dois.
  - Conceito 3 — Três ou quatro.
  - Conceito 4 — Os cinco.
- **2.3** — Normalização
  - Conceito 0 a 4: por contagem, de "apenas um" a "os quatro".
  - Conceito 0 também quando o candidato trata a normalização como correção do conteúdo.
- **2.4** — Vocabulário, adaptação e risco
  - Conceito 0 — Não abordou, ou equiparou adaptação a retreino acústico.
  - Conceito 1 — Um aspecto.
  - Conceito 2 — Dois.
  - Conceito 3 — Três ou quatro.
  - Conceito 4 — Os cinco.
- **2.5** — Conclusão e recomendações
  - Conceito 0 — Não concluiu nem recomendou.
  - Conceito 1 — Um aspecto.
  - Conceito 2 — Dois ou três.
  - Conceito 3 — Os quatro.

## D4 — Questão

### Padrão de resposta

```text
ASPECTOS
 (i)    Busca por palavras-chave: recupera documentos pela coincidência dos termos da consulta.
 (ii)   Busca semântica: consulta e trechos são representados por vetores (embeddings); recupera por proximidade de sentido, mesmo sem palavras em comum.
 (iii)  Um risco do resumo automático. Lista fechada: omissão; inversão de sentido; atribuição errada de fala ou voto; troca de números e nomes; alucinação (informação sem sustentação na fonte); fluência enganosa.
 (iv)   Uma mitigação. Lista fechada: revisão humana antes da publicação; gerar o resumo a partir de transcrição verificada; exigir o trecho-fonte de cada afirmação; lista de checagem.
 (v)    A Câmara é a controladora, porque a ela competem as decisões sobre o tratamento (LGPD, art. 5º, VI).
 (vi)   A empresa contratada é a operadora: trata os dados em nome do controlador e segundo suas instruções (LGPD, art. 5º, VII, e art. 39). Aceita-se a ressalva "conforme o contrato".
 (vii)  Primeiro princípio, explicado.
 (viii) Segundo princípio, explicado.
        Lista fechada (LGPD, art. 6º): finalidade (I); adequação (II); necessidade (III); livre acesso (IV); qualidade dos dados (V); transparência (VI); segurança (VII); prevenção (VIII); não discriminação (IX); responsabilização e prestação de contas (X).
 (ix)   Uma razão para cuidado à luz da Lei 9.610/1998. Lista fechada:
        - conferências e alocuções são obras protegidas (art. 7º, II), e reproduzi-las ou incluí-las em base de dados depende de autorização (art. 29, I e IX), ressalvadas as limitações (art. 46, I, "b", e III);
        - direitos morais: indicação do nome do autor e integridade da obra (art. 24, II e IV), inalienáveis e irrenunciáveis (art. 27);
        - a citação exige indicação do autor e da origem (art. 46, III).
 (x)    Um cuidado ético com conteúdo gerado por IA. Lista fechada: transparência sobre o uso de IA; revisão humana com responsável identificado; não atribuir ao orador palavras que ele não disse; rastreabilidade das fontes.

QUESITOS
Quesito 2.1 — Busca semântica × lexical; risco e mitigação do resumo [valor: 5,00]
 - Conceito 0: não abordou.
 - Conceito 1: um dos aspectos (i) a (iv).
 - Conceito 2: dois.
 - Conceito 3: três.
 - Conceito 4: os quatro.

Quesito 2.2 — Controlador, operador e princípios [valor: 5,00]
 - Conceito 0: não abordou ou inverteu os papéis.
 - Conceito 1: um dos aspectos (v) a (viii).
 - Conceito 2: dois.
 - Conceito 3: três.
 - Conceito 4: os quatro.
 Um princípio só nomeado, sem explicação, não conta.

Quesito 2.3 — Direitos autorais e ética [valor: 4,30]
 - Conceito 0: não abordou ou afirmou como certo tema controverso (por exemplo, que o conteúdo gerado por IA é ou não é obra protegida).
 - Conceito 1: abordou apenas (ix) ou apenas (x).
 - Conceito 2: abordou (ix) e (x), mas sem indicar dispositivo correto em (ix).
 - Conceito 3: abordou (ix) e (x), com o dispositivo correto em (ix).

Os aspectos enumerados valem como padrão de resposta, com as bases normativas indicadas em cada um. Nota: questão: NQ = NC − 3 × NE ÷ TL (9.8.5.1, d); peça: NPT = NC − 6 × NE ÷ TL (9.8.5.2, d). O peso de cada quesito é HIPÓTESE deste material, alinhada à soma oficial.

Notas de correção
1. Alínea c da discursiva: NÃO se exige enquadrar o
    pronunciamento parlamentar como obra protegida (Lei 9.610/1998, art.
    7º, II) nem como ato oficial (art. 8º, IV). Não há texto legal nem
    jurisprudência firmada sobre isso. Fica descartada a afirmação
    categórica, segundo a qual os pronunciamentos "são
    obras intelectuais protegidas". Basta uma razão da lista (ix), com
    o dispositivo correto.
2. Voz como dado sensível (biométrico): nem exigido nem penalizado.
3. Base legal do tratamento pelo poder público: aceitam-se o art. 23 e
    o art. 7º, II ou III.
```

### Aspectos (valor)

- (1) diferencie busca semântica de busca por palavras-chave e aponte um risco da geração automática de resumos para o registro parlamentar e uma medida para mitigá-lo; — valor: 5,00
- (2) identifique, à luz da LGPD, quem seria o controlador e quem seria o operador nessa contratação e explique dois princípios que devem orientar o tratamento dos dados pessoais envolvidos; — valor: 5,00
- (3) indique, à luz da Lei 9.610/1998, uma razão pela qual os pronunciamentos exigem cuidado no seu uso e, quanto ao conteúdo gerado por IA, um cuidado ético a ser observado. — valor: 4,30

### Quesitos

- **2.1** — Busca semântica × lexical; risco e mitigação do resumo
  - Conceito 0: não abordou.
  - Conceito 1: um dos aspectos (i) a (iv).
  - Conceito 2: dois.
  - Conceito 3: três.
  - Conceito 4: os quatro.
- **2.2** — Controlador, operador e princípios
  - Conceito 0: não abordou ou inverteu os papéis.
  - Conceito 1: um dos aspectos (v) a (viii).
  - Conceito 2: dois.
  - Conceito 3: três.
  - Conceito 4: os quatro. Um princípio só nomeado, sem explicação, não conta.
- **2.3** — Direitos autorais e ética
  - Conceito 0: não abordou ou afirmou como certo tema controverso (por exemplo, que o conteúdo gerado por IA é ou não é obra protegida).
  - Conceito 1: abordou apenas (ix) ou apenas (x).
  - Conceito 2: abordou (ix) e (x), mas sem indicar dispositivo correto em (ix).
  - Conceito 3: abordou (ix) e (x), com o dispositivo correto em (ix).

## D5 — Peça técnica

### Padrão de resposta

```text
ASPECTOS
 (i)     Objeto: contratação de serviço em nuvem para transcrever e sumarizar o áudio das reuniões de comissões; análise de conformidade com a LGPD e de segurança.
 (ii)    Relato da situação: processamento possivelmente fora do Brasil e armazenamento por prazo indefinido.
 (iii)   O áudio da voz e as transcrições de pessoas identificadas são dados pessoais (art. 5º, I), e transcrever e sumarizar são operações de tratamento (art. 5º, X).
 (iv)    A Câmara é a controladora (art. 5º, VI).
 (v)     O fornecedor é o operador e segue as instruções do controlador (art. 5º, VII, e art. 39).
 (vi)    O operador responde solidariamente se descumprir a lei ou as instruções lícitas (art. 42, § 1º, I). Também aceito como aspecto: menção a dado sensível, por exemplo opinião política (art. 5º, II), desde que tratada como risco e não como afirmação categórica.
 (vii)   Tratamento pelo poder público para atender à finalidade pública e às competências legais (art. 23, caput), com informação das hipóteses e indicação de encarregado (art. 23, I e III). Também aceita a base legal do art. 7º, II ou III.
 (viii)  Pelo menos dois princípios aplicados ao caso (art. 6º). Lista fechada: finalidade (I); necessidade (III), contra o prazo indefinido; transparência (VI); segurança (VII); prevenção (VIII).
 (ix)    Medidas de segurança técnicas e administrativas (art. 46, caput), desde a concepção até a execução (art. 46, § 2º). Lista fechada de exemplos: cifragem em trânsito e em repouso; controle de acesso por perfil; registro de acessos; segregação de ambientes.
 (x)     O dever de segurança persiste após o término do tratamento (art. 47), ou os sistemas devem ser estruturados para atender aos requisitos de segurança (art. 49).
 (xi)    Retenção: o término do tratamento ocorre quando a finalidade é alcançada (art. 15, I), com eliminação depois do término, ressalvada a conservação autorizada (art. 16). O prazo indefinido é incompatível com o princípio da necessidade (art. 6º, III).
 (xii)   Incidente: o controlador comunica à ANPD e ao titular (art. 48, caput), com o conteúdo mínimo do art. 48, § 1º. O contrato deve obrigar o operador a avisar o controlador.
 (xiii)  O processamento no exterior pode configurar transferência internacional (art. 5º, XV).
 (xiv)   A transferência só é permitida nos casos do art. 33. Lista fechada de exemplos: grau de proteção adequado (I); garantias do controlador, como cláusulas-padrão (II, "b"); execução de política pública com publicidade (VII).
 (xv)    Recomendação contratual: finalidade e instruções definidas e vedação de uso dos dados para fins próprios do fornecedor (arts. 39 e 42, § 1º, I).
 (xvi)   Recomendação: prazo de retenção definido e eliminação ao término (arts. 15 e 16).
 (xvii)  Recomendação: cláusula sobre local de processamento e subcontratados, com transferência só nos casos do art. 33.
 (xviii) Recomendação: requisitos de segurança e plano de resposta a incidentes (arts. 46 e 48). Também aceito: relatório de impacto à proteção de dados (art. 5º, XVII, e arts. 32 ou 38).
 (xix)   Conclusão técnica fundamentada, com os dispositivos indicados.

QUESITOS
Quesito 2.1 — Objeto e situação [valor: 2,00]
 - Conceito 0: não abordou.
 - Conceito 1: abordou (i) ou (ii).
 - Conceito 2: abordou (i) e (ii).

Quesito 2.2 — Natureza dos dados e papéis [valor: 6,00]
 - Conceito 0: não abordou ou inverteu controlador e operador.
 - Conceito 1: um dos aspectos (iii) a (vi).
 - Conceito 2: dois.
 - Conceito 3: três.
 - Conceito 4: os quatro.

Quesito 2.3 — Finalidade pública, princípios e segurança [valor: 7,00]
 - Conceito 0: não abordou.
 - Conceito 1: um dos aspectos (vii) a (x).
 - Conceito 2: dois.
 - Conceito 3: três.
 - Conceito 4: os quatro.

Quesito 2.4 — Ciclo de vida, incidentes e transferência internacional [valor: 8,00]
 - Conceito 0: não abordou, ou atribuiu ao operador o dever de comunicar o incidente à ANPD.
 - Conceito 1: um dos aspectos (xi) a (xiv).
 - Conceito 2: dois.
 - Conceito 3: três.
 - Conceito 4: os quatro.

Quesito 2.5 — Recomendações e conclusão com dispositivos [valor: 5,50]
 - Conceito 0: não apresentou recomendações.
 - Conceito 1: um dos aspectos (xv) a (xix).
 - Conceito 2: dois ou três.
 - Conceito 3: quatro ou cinco.

Os aspectos enumerados valem como padrão de resposta, com as bases normativas indicadas em cada um. Nota: questão: NQ = NC − 3 × NE ÷ TL (9.8.5.1, d); peça: NPT = NC − 6 × NE ÷ TL (9.8.5.2, d). O peso de cada quesito é HIPÓTESE deste material, alinhada à soma oficial.

Notas de correção
1. Voz como dado sensível (biométrico): nem exigido nem penalizado.
2. Base legal do tratamento pelo poder público: aceitam-se o art. 23 e
    o art. 7º, II ou III.
```

### Aspectos (valor)

- (1) objeto da consulta e relato sintético da situação; — valor: 2,00
- (2) natureza dos dados e papéis de controlador e de operador; — valor: 6,00
- (3) finalidade pública, princípios aplicáveis e medidas de segurança; — valor: 7,00
- (4) ciclo de vida dos dados (retenção e eliminação), comunicação de incidentes e possível transferência internacional; — valor: 8,00
- (5) conclusão com recomendações objetivas e os dispositivos da LGPD que as embasam. — valor: 5,50

### Quesitos

- **2.1** — Objeto e situação
  - Conceito 0: não abordou.
  - Conceito 1: abordou (i) ou (ii).
  - Conceito 2: abordou (i) e (ii).
- **2.2** — Natureza dos dados e papéis
  - Conceito 0: não abordou ou inverteu controlador e operador.
  - Conceito 1: um dos aspectos (iii) a (vi).
  - Conceito 2: dois.
  - Conceito 3: três.
  - Conceito 4: os quatro.
- **2.3** — Finalidade pública, princípios e segurança
  - Conceito 0: não abordou.
  - Conceito 1: um dos aspectos (vii) a (x).
  - Conceito 2: dois.
  - Conceito 3: três.
  - Conceito 4: os quatro.
- **2.4** — Ciclo de vida, incidentes e transferência internacional
  - Conceito 0: não abordou, ou atribuiu ao operador o dever de comunicar o incidente à ANPD.
  - Conceito 1: um dos aspectos (xi) a (xiv).
  - Conceito 2: dois.
  - Conceito 3: três.
  - Conceito 4: os quatro.
- **2.5** — Recomendações e conclusão com dispositivos
  - Conceito 0: não apresentou recomendações.
  - Conceito 1: um dos aspectos (xv) a (xix).
  - Conceito 2: dois ou três.
  - Conceito 3: quatro ou cinco.
