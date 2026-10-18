# Lote 2 — RF-DEGRAVACAO (degravação e pós-processamento, P2 2.1–2.8)

Prova: P2

## Itens do edital

- P2-2.1 — Diferença entre transcrição automática, degravação e revisão humana
- P2-2.2 — Fluxo de trabalho de degravação assistida por IA (Human in the loop)
- P2-2.3 — Revisão e edição de transcrições: critérios de qualidade e fidelidade
- P2-2.4 — Formatação de transcrições parlamentares: identificação de oradores, marcação de pausa ruído, etc.
- P2-2.5 — Normalização de texto: números, siglas, abreviações e termos técnicos
- P2-2.6 — Ferramentas de CAT (Computer Assisted Transcription) e editores de transcrição
- P2-2.7 — Controle de qualidade: revisão em dupla, auditorias de amostras, SLA
- P2-2.8 — Vocabulário técnico parlamentar e vocabulário adaptado (language model adaptation)

## Resumo

```text
2.1 AUTOMÁTICA = software, sem humano, rascunho. DEGRAVAÇÃO = pessoa
converte gravação em texto, a posteriori (≠ taquigrafia, simultânea).
REVISÃO = confronto com áudio e contexto, responsabilidade pelo texto.
2.2 HITL: validação humana obrigatória antes de publicar (≠ ON the
loop, supervisão; ≠ sem humano). Fluxo: preparo → ASR adaptado →
diarização e pós-proc. → identificação de oradores → revisão → QC →
publicação → retroalimentação. Confiança prioriza, não dispensa. Viés de
automação.
2.3 FIDELIDADE ≠ literalidade. Graus: literal / verbatim limpo / editado,
por decisão da instituição. Critérios: exatidão, completude, nomes-siglas-números, consistência, conformidade, rastreabilidade (inaudível se
marca, não se completa). Erro de sentido > erro de forma. Prática
oficial: revisão e redação final; notas sem e com redação final.
2.4 FORMATAÇÃO: orador padronizado e troca sinalizada; tipo de
intervenção (aparte, fala do Presidente, pela ordem, questão de ordem…
na lista do Banco de Discursos); pausa só se relevante;
eventos não falados em convenção ÚNICA e distinguível; sobreposição
registrada. Rótulo de diarização ≠ identificação. O aparteante tem
rótulo próprio. Forma de identificar o orador: observada nas notas oficiais de 2026. Convenção da Câmara para marcação de pausas e eventos não falados e para grafia: NÃO VERIFICADA.
2.5 NORMALIZAÇÃO = padronizar a FORMA. ITN (fala→escrita) é formatação
pós-ASR, não reconhecimento. Números, siglas, abreviações, termos:
regra única e glossário. Não corrige o conteúdo. Ambiguidade (ano ×
quantidade). Também usada para normalizar antes do WER. Manual de
Redação: obrigatório para documentos administrativos, recomendado para o
resto (Portaria DG nº 77/2017).
2.6 CAT do edital = TRANSCRIÇÃO assistida; na taquigrafia, traduz as notas estenotípicas em texto. "Tradução das notas" = decifrar os
sinais, não verter de idioma. Memória de tradução é recurso de tradução
entre idiomas, não da transcrição assistida. Editor: áudio sincronizado,
timecodes, rótulos, glossário, histórico, exportação. WebVTT: segmentos
com tempo e voice span para falante. Produto comercial:
NÃO VERIFICADO.
2.7 DUPLA REVISÃO = segundo revisor INDEPENDENTE. AUDITORIA = amostra
estima a qualidade; não prova ausência de erro no resto. SLA = metas de
prazo E qualidade. Indicadores: erros por gravidade, prazo, retrabalho.
2.8 Parlamentar: siglas, termos regimentais, nomes, proposições. LM
adaptado: probabilidade de sequências (contexto), interpolação,
reforço de termos, pronúncias. OOV = ausente do vocabulário. Risco:
sobre-reforço → falsos positivos; listas desatualizam. Avaliar em
dados separados, com WER geral e acerto de termos.
```

## Curso

```text
## 2.1 TRANSCRIÇÃO AUTOMÁTICA, DEGRAVAÇÃO E REVISÃO HUMANA

DEFINIÇÃO
Três conceitos que o edital manda diferenciar:
 - Transcrição automática: texto produzido por software de
   reconhecimento de fala (ASR, Lote 1) a partir do áudio, sem
   intervenção humana na produção. A saída é um RASCUNHO: não garante
   fidelidade em nomes, siglas, números, pontuação nem atribuição de
   falas.
 - Degravação: conversão de uma gravação (áudio ou vídeo) em texto
   escrito, tradicionalmente por uma pessoa que ouve e redige, com ou
   sem apoio de ferramentas. É feita DEPOIS, sobre a gravação. Contrasta
   com a taquigrafia, que registra a fala simultaneamente, ao vivo.
   [definição de uso corrente; sem fonte oficial verificada.]
 - Revisão humana: etapa em que pessoa qualificada confronta o texto
   (automático ou degravado) com o áudio e com o contexto (pauta, lista
   de oradores, glossário), corrige conteúdo e forma segundo critérios
   da instituição e responde pela versão publicada.
Em uma linha: automática = velocidade e escala, sem responsabilidade;
degravação = trabalho humano a partir da gravação; revisão = controle
de qualidade e responsabilidade pelo texto final.

Contexto institucional: o Banco de Discursos reúne notas taquigráficas
registradas pelo Derep (antigo DETAQ),
Departamento de Registro Oficial e Redação Parlamentar, por força do
Ato da Mesa nº 251/2026. A prática
oficial inclui a revisão e a redação final
dos pronunciamentos, com divulgação das notas sem redação final e,
depois, com redação final. Como curiosidade
histórica, a Ordem de Serviço nº 1/1970 tratava a primeira tradução das
notas como rascunho sujeito a correção e a suprimento de omissões, antes
da versão definitiva [norma de
caráter experimental, não cobrar o texto].

EXEMPLO PARLAMENTAR
Audiência pública em comissão. (1) O sistema gera, em minutos, uma
transcrição automática para consulta interna: é rascunho. (2) Uma
pessoa ouve a gravação e redige o texto: degravação. (3) Um revisor
confere o texto contra o áudio, corrige o nome de um convidado e uma
sigla e valida a versão a publicar: revisão humana. Os três podem
conviver no mesmo fluxo, em funções distintas.

PEGADINHA PROVÁVEL
(1) Trocar as definições (automática = humana; degravação = software).
(2) Dizer que a boa qualidade do ASR dispensa a revisão humana.
(3) Tratar degravação como sinônimo de taquigrafia (uma é posterior à
gravação; a outra é simultânea). (4) Dizer que revisão humana é
digitar tudo de novo. (5) Supor que o humano não erra: o controle da
qualidade humana é o tema do 2.7.

## 2.2 FLUXO DE DEGRAVAÇÃO ASSISTIDA POR IA (HUMAN IN THE LOOP)

DEFINIÇÃO
Degravação assistida por IA é o fluxo em que o sistema faz o trabalho
de volume e a pessoa valida o resultado. "Human in the loop" (HITL,
humano no circuito) significa que há um ponto de intervenção humana
obrigatório antes de o resultado produzir efeito (aqui, antes da
publicação). Distinguir, por uso corrente em governança de IA (sem fonte
normativa verificada):
 - human IN the loop: o humano intervém em cada ciclo e valida cada
   saída;
 - human ON the loop: o humano supervisiona e pode intervir, mas não
   valida cada saída;
 - sem humano: o sistema decide e publica sozinho.
Fluxo típico, em ordem:
 1. Preparo do áudio (qualidade, corte, canais).
 2. ASR com vocabulário adaptado (2.8).
 3. Diarização (1.4) e pós-processamento: pontuação, capitalização e
    normalização (1.5, 2.5).
 4. Identificação dos oradores: cadastro, lista de inscritos, ordem de
    falas (atribuição humana ou apoiada em dados).
 5. Revisão humana contra o áudio (2.3).
 6. Controle de qualidade: revisão em dupla e auditoria (2.7).
 7. Publicação.
 8. Retroalimentação: correções viram glossário e dados de ajuste.
Nota de confiança: muitos ASR devolvem pontuação de confiança por
palavra. Serve para PRIORIZAR a atenção do revisor, não para dispensar
a leitura: o sistema pode errar com alta confiança, e o modelo pode
gerar texto fluente e falso (Lote 1, itens 1.2 e 1.3). Risco humano
associado: viés de automação, a tendência de aceitar o texto da máquina
por parecer plausível.

EXEMPLO PARLAMENTAR
Reunião de comissão de 90 minutos: o ASR entrega o texto com rótulos
"Locutor 1…5"; o revisor associa os rótulos aos parlamentares pela lista
de inscritos, confere números e nomes contra o áudio, marca o trecho
inaudível e devolve o texto; o termo corrigido entra no glossário da
próxima reunião.

PEGADINHA PROVÁVEL
(1) HITL ≠ o revisor só olha trechos de baixa confiança. (2) HITL ≠
o humano transcreve do zero. (3) Revisão só de uma amostra no fim é
supervisão ou auditoria (ON the loop), não HITL. (4) "Assistida" ≠
automática com publicação direta. (5) Retroalimentar o sistema com
correções melhora o fluxo, mas não elimina a revisão seguinte.



## 2.3 REVISÃO E EDIÇÃO DE TRANSCRIÇÕES: QUALIDADE E FIDELIDADE

DEFINIÇÃO
Fidelidade é a preservação do que o orador disse: conteúdo, sentido e,
conforme o critério da instituição, o estilo. Fidelidade NÃO equivale
necessariamente a literalidade. Três graus de tratamento do texto:
 1. Literal (verbatim, ipsis verbis): registra tudo, inclusive
    hesitações, repetições, falsas partidas e vícios de linguagem.
 2. Verbatim limpo: retira disfluências sem conteúdo e mantém as
    palavras e a ordem com sentido.
 3. Texto editado: adapta à norma culta e ao estilo da instituição,
    preservando o sentido (e, em geral, o estilo do orador).
Qual grau vale é decisão editorial da instituição, explícita e aplicada
de modo uniforme.
Contexto oficial: a prática da Câmara inclui a revisão e a redação final
dos pronunciamentos e debates; as notas taquigráficas são divulgadas sem
redação final e, depois, com Redação Final. O
departamento responsável hoje se chama Departamento de Registro Oficial e
Redação Parlamentar. O curso NÃO afirma critério gramatical da
Câmara: mostra apenas que existe etapa de revisão e redação final.

Critérios de qualidade usuais na revisão:
 - Exatidão: o texto diz o que foi dito (nada acrescentado, omitido ou
   alterado em sentido).
 - Completude: todas as falas e intervenções constam, com o orador
   certo.
 - Correção de nomes, siglas e números (erro aqui é de alto risco).
 - Consistência: grafia e convenções uniformes (2.5).
 - Conformidade com o manual ou guia de estilo da Casa.
 - Rastreabilidade da dúvida: trecho inaudível ou incerto é MARCADO,
   não completado por conjectura.
Gravidade dos erros: erro que ALTERA O SENTIDO (omitir "não", trocar
número, nome ou orador) é mais grave que erro de forma que não impede a
compreensão (acento, grafia). Critérios de qualidade costumam graduar
a gravidade.

EXEMPLO PARLAMENTAR
O orador diz: "Não concordo com o destaque." O texto automático saiu
"Concordo com o destaque." É erro de sentido (crítico), mesmo com WER
baixo no trecho. Já "a nível de" corrigido para "em nível de", quando o
critério editorial da Casa prevê a correção, é ajuste de forma que não
altera o sentido.

PEGADINHA PROVÁVEL
(1) Fidelidade = literalidade absoluta. (2) Qualquer correção
gramatical é infidelidade (ou, no extremo oposto, o revisor pode
"melhorar" o conteúdo). (3) Completar o inaudível pelo contexto sem
marcar. (4) Tratar todos os erros como equivalentes. (5) Reduzir
qualidade a um número único de acerto de palavras (tema do Lote 1,
não repetido aqui).

## 2.4 FORMATAÇÃO DE TRANSCRIÇÕES PARLAMENTARES

DEFINIÇÃO
Formatar é organizar o texto para que o leitor saiba QUEM falou, EM QUE
TIPO DE INTERVENÇÃO e O QUE aconteceu além da fala. Elementos:
 - Identificação de oradores: rótulo padronizado por fala; troca de
   orador sempre sinalizada. A forma exata na Câmara (nome parlamentar,
   cargo, partido/UF) foi observada nas notas oficiais de 2026; o curso ensina o
   princípio: padronizado, uniforme, sem ambiguidade.
 - Tipo de intervenção: o Banco de Discursos da Câmara permite pesquisar
   por tipos como aparte, apresentação de proposição, declaração de
   voto, encaminhamento de votação, fala do Presidente (ou no exercício
   da Presidência), orientação de bancada, pela ordem, questão de ordem
   e registro de voto. Lição: aparte e fala do
   Presidente são categorias distintas do discurso principal. A lista pode mudar; nenhum item depende dela. Lista variável conforme a consulta à página (08/10/2026).
 - Marcação de pausa: depende do grau de fidelidade (2.3); numa
   transcrição editada, só pausa que tenha relevância para o registro.
 - Eventos não falados e ruído: palmas, risos, trecho inaudível, fala
   sobreposta. A convenção varia entre instituições; dentro de uma
   transcrição deve ser uma só, uniforme e DISTINGUÍVEL do texto falado
   (por exemplo, em marcação própria).
 - Marcas de tempo: úteis para conferência e para legendas (2.6).
 - Fala sobreposta: registrar a sobreposição, sem inventar quem disse o
   quê.
Ligação com o 1.4: diarização separa locutores com rótulos genéricos;
a identificação por NOME é cadastro ou atribuição humana. Adendo de
pegadinha do título do edital: ver o complemento do Lote 1 (adendo ao 1.4).

EXEMPLO PARLAMENTAR
O orador discursa; outro parlamentar pede um aparte; o Presidente interrompe para advertir sobre o tempo. Aparte: interrupção breve e oportuna do orador, por outro Deputado que obtém sua permissão (RICD, art. 176, caput e § 1º). O registro taquigráfico do aparte é a regra; o não apanhamento depende de determinação do Presidente (RICD, art. 17, I, 'h'). Texto bem formatado: três
orações com rótulos distintos, o aparte identificado como aparte, a fala
do Presidente identificada como tal e a sobreposição final sinalizada
por marca única.

PEGADINHA PROVÁVEL
(1) Confundir marcação (evento) com fala. (2) Afirmar que toda pausa
deve ser registrada. (3) Misturar fala do Presidente, aparte e discurso
numa só linha. (4) Dizer que a convenção de marcação é universal.
(5) Tratar rótulo de diarização ("Locutor 2") como identificação do
orador. (6) Atribuir a fala do aparteante ao orador que tem a palavra.

## 2.5 NORMALIZAÇÃO DE TEXTO: NÚMEROS, SIGLAS, ABREVIAÇÕES, TERMOS

DEFINIÇÃO
Normalização de texto é padronizar a FORMA de escrever, sem mudar o
conteúdo. Dois sentidos que a banca pode misturar:
 - Normalização (texto → fala): converte a forma escrita em forma
   falada ("25%" → "vinte e cinco por cento"); típica de síntese de
   voz e de preparo de texto para treinar modelos.
 - Normalização INVERSA (fala → texto escrito), ou ITN: converte a forma
   falada reconhecida em forma escrita convencional ("vinte e cinco por
   cento" → "25%"). É etapa de formatação posterior ao reconhecimento
   (1.5), não é reconhecimento acústico.
Domínios de decisão na transcrição parlamentar:
 - Números: algarismos ou extenso, separador de milhar, percentuais,
   moeda, datas, ordinais, numeração de dispositivos e proposições.
 - Siglas: forma escrita (PEC, MPV, CCJ), expansão na primeira
   ocorrência ou não, glossário. O ASR pode devolver as letras ou a
   pronúncia, não a sigla.
 - Abreviações: Sr., Sra., Dep.; uniformizar.
 - Termos técnicos: latinismos, estrangeirismos, expressões regimentais:
   grafia única, glossário.
 - Ambiguidades: "dois mil e vinte e seis" pode ser ano ou quantidade;
   a ITN decide por contexto e pode errar, logo o revisor confere.
Norma de referência: a Câmara tem Manual de Redação. A Portaria DG nº
77/2017 determina o uso das normas de padronização do Manual para os
documentos administrativos (art. 2º, caput) e as recomenda para as
demais modalidades de material escrito, respeitadas as características
de cada gênero textual (art. 2º, parágrafo único). O conteúdo do Manual sobre números e siglas NÃO foi
verificado. Ilustrativo apenas: "projeto de lei mil duzentos e
trinta e quatro de dois mil e vinte e seis" → "PL 1.234/2026" (a forma
exata dependeria do manual da Casa).
Normalização também aparece na AVALIAÇÃO: é prática comum normalizar
referência e hipótese (caixa, pontuação, grafia de números) antes de
calcular o WER, para não penalizar diferença só de formatação.

EXEMPLO PARLAMENTAR
No mesmo texto, "5%" na primeira página e "cinco por cento" na
terceira; "CCJ" e "Comissão de Constituição e Justiça" misturadas sem
critério. A padronização por regra institucional elimina a oscilação e
melhora a busca posterior.

PEGADINHA PROVÁVEL
(1) Normalização = corrigir o que o orador disse (errada: é padronizar
a forma, não corrigir a informação). (2) Siglas sempre por extenso, ou
números sempre em algarismos (generalização). (3) Confundir com
normalização de áudio (volume) ou de vetores. (4) Dizer que a ITN é
etapa do modelo acústico. (5) Achar que a máquina decide sem erro entre
ano e quantidade. (6) Tratar o Manual de Redação como obrigatório para
todo texto: a Portaria o torna obrigatório para documentos
administrativos e apenas recomenda para os demais.



## 2.6 FERRAMENTAS DE CAT E EDITORES DE TRANSCRIÇÃO

DEFINIÇÃO
O edital escreve "CAT (Computer Assisted Transcription)": transcrição
assistida por computador.
SENTIDO PRÓPRIO NA TAQUIGRAFIA: software que traduz as notas da máquina estenotípica em texto.
Em torno desse sentido estão os editores de transcrição de áudio, onde o
revisor trabalha o rascunho do ASR. ATENÇÃO À PALAVRA "tradução": no
jargão da taquigrafia, "tradução das notas" é decifrar os sinais
registrados e passá-los para texto, e NÃO verter o texto para outro
idioma [contexto histórico]. A
"memória de tradução", que reaproveita segmentos já traduzidos entre
idiomas, é recurso de ferramentas de tradução e não é o recurso central
da transcrição assistida.
Recursos típicos de editores de transcrição (categorias, sem citar
produto):
 - Reprodução sincronizada texto–áudio: clicar no trecho do texto toca
   o áudio correspondente.
 - Marcas de tempo (timecodes) por palavra, frase ou bloco.
 - Controle de velocidade, atalhos de teclado, pedal, retrocesso
   automático.
 - Rótulos de orador e tipos de intervenção.
 - Busca e substituição, glossário e lista de termos da Casa.
 - Destaque de trechos de baixa confiança do ASR.
 - Histórico de versões e controle de alterações; fluxo com mais de um
   usuário (revisor, auditor).
 - Exportação em formatos de texto, de documento e de legenda.
Formato de legenda como exemplo de padrão técnico: o WebVTT organiza o
texto em segmentos (cues) associados a intervalos de tempo e admite
indicar o falante de cada segmento por marcação própria (voice span). Serve para legendas e também
carrega informação de locutor.
Segurança: se o editor é local ou em nuvem decide onde o áudio fica
(custódia; Lote 1, item 1.8; Lote 3, item 4.3).

EXEMPLO PARLAMENTAR
O revisor abre a reunião no editor, clica na fala do relator, ouve o
trecho, corrige o número da emenda, aceita a marcação de orador e
exporta o texto e um arquivo de legenda com os rótulos de falante.

PEGADINHA PROVÁVEL
(1) Atribuir ao CAT da transcrição a memória de tradução, recurso de
ferramentas de tradução entre idiomas. (2) Confundir editor (onde o
humano trabalha) com ASR (que gera o rascunho). (3) Dizer que a
ferramenta dispensa a revisão. (4) Cobrar recurso de produto
específico: sem fonte datada, não é seguro (cobrar o CONCEITO). (5)
Achar que formato de legenda não pode levar identificação de falante.
(6) Jargão: ler "tradução das notas" como tradução para outro idioma;
em taquigrafia é decifrar os sinais e passar para texto.

## 2.7 CONTROLE DE QUALIDADE: REVISÃO EM DUPLA, AUDITORIA, SLA

DEFINIÇÃO
 - Revisão em dupla: um SEGUNDO revisor, independente do primeiro,
   examina o texto. Independência é o ponto: o mesmo revisor relendo
   não é revisão em dupla.
 - Auditoria de amostras: reexame de uma parte das transcrições já
   revisadas, para ESTIMAR a qualidade do conjunto e devolver feedback.
   Seleção: aleatória, estratificada (por tipo de reunião, revisor,
   duração) ou dirigida a risco. A amostra estima; não prova ausência
   de erro nas peças não examinadas.
 - SLA (Service Level Agreement, acordo de nível de serviço): acordo que
   fixa metas, em geral de prazo de entrega (turnaround) e de qualidade
   mínima (por exemplo, taxa máxima de erros por mil palavras ou de
   erros críticos), com forma de medição e consequências. Prazo
   cumprido sem a meta de qualidade não cumpre o acordo.
 - Indicadores comuns: taxa de erros (por tipo e gravidade), tempo de
   entrega, retrabalho, percentual auditado, concordância entre
   revisores.
 - Cuidado: meta só de prazo incentiva pressa; fadiga e viés de
   automação (2.2) também afetam o humano.

EXEMPLO PARLAMENTAR
Cada reunião de comissão é revisada por um revisor e conferida por
outro. Mensalmente, 10% das notas, sorteadas por tipo de reunião, são
auditadas; o SLA exige entrega em 24 horas e no máximo certa taxa de
erros críticos. A auditoria acha um erro de número recorrente: o termo
entra no glossário e o revisor recebe feedback.

PEGADINHA PROVÁVEL
(1) Revisão em dupla = o mesmo revisor lendo duas vezes. (2) Amostra
sem erro = lote sem erro. (3) SLA = apenas prazo (ou: SLA = sistema de
licenciamento). (4) Auditoria = revisão integral. (5) Dupla revisão
garante zero erros.

## 2.8 VOCABULÁRIO TÉCNICO PARLAMENTAR E MODELO DE LINGUAGEM ADAPTADO

NOTA DE ESCOPO (sobreposição com o 1.6)
O Lote 1 já cobre o que são adaptação de vocabulário (lista de termos),
modelo de linguagem customizado e customização acústica, e a regra de
que sotaque pede dados acústicos. Este item aprofunda o que é PRÓPRIO
do 2.8; não repete os julgamentos de Q12 a Q14 do Lote 1.

DEFINIÇÃO
 - Vocabulário técnico parlamentar (o que adaptar): siglas (PEC, MPV,
   CCJ), termos regimentais (questão de ordem, destaque, requerimento),
   nomes de parlamentares, municípios e órgãos, termos jurídicos,
   latinismos, designação de proposições.
 - Modelo de linguagem (LM): componente que estima a probabilidade de
   SEQUÊNCIAS de palavras ("questão de ordem" mais provável que
   "questão de morde"). Adaptar o LM com textos do domínio (pronunciamentos, atas, regimento) eleva a probabilidade de sequências
   típicas; ajuda a escolher entre palavras de som parecido pelo
   contexto, como sessão, seção e cessão, que são homófonas.
 - Técnicas gerais (nomes variam por fornecedor; produto não verificado):
   (i) interpolar um LM de domínio com o LM geral, com peso ajustável;
   (ii) reforço contextual de termos (biasing, lista de termos com
   peso); (iii) acrescentar pronúncias para termos novos; (iv) pós-correção por glossário ou por LLM (risco: o LLM pode alterar o
   conteúdo; ver 1.3).
 - OOV (out of vocabulary): palavra ausente do vocabulário do sistema.
   Nome novo de parlamentar é caso típico. Não é o mesmo que "baixa
   confiança".
 - Riscos: reforço excessivo faz o sistema inserir o termo reforçado
   onde ele não foi dito (falso positivo) e pode piorar outras palavras;
   listas ficam desatualizadas (nomes mudam a cada legislatura);
   adaptação não remove o ruído nem trata a causa acústica (sotaque pede
   dados acústicos), embora possa melhorar o reconhecimento dos termos
   esperados quando o áudio é ruidoso ou pouco claro.
 - Avaliação correta: separar os dados usados para adaptar dos dados de
   teste; medir o WER geral e também o acerto dos termos-alvo, antes e
   depois.
 - Dados de adaptação: textos de pronunciamentos e atas podem envolver
   direitos autorais e dados pessoais (Lote 3, itens 4.1 e 4.2).

EXEMPLO PARLAMENTAR
Em 2027 entram novos parlamentares: nomes que o modelo nunca viu viram
OOV. A equipe atualiza a lista com os nomes e suas pronúncias, ajusta o
LM com atas recentes e mede em reuniões novas (não nas usadas para
adaptar) se o acerto dos nomes subiu sem piorar o WER geral.

PEGADINHA PROVÁVEL
(1) OOV = baixa confiança (errado). (2) "Mais peso no reforço é sempre
melhor" (generalização). (3) Adaptação de LM = retreino acústico.
(4) Testar a adaptação nos mesmos dados usados para adaptar. (5) Pós-correção por LLM como garantia de fidelidade.
```

## Pares

- **Transcrição automática** vs **degravação**: software sem humano / pessoa a partir da gravação.
- **Degravação** vs **taquigrafia**: depois, sobre a gravação / ao vivo.
- **Transcrição automática** vs **revisão humana**: rascunho / controle e responsabilidade.
- **Human IN the loop** vs **human ON the loop**: valida cada saída / supervisiona e intervém.
- **Confiança do ASR** vs **correção**: prioriza a atenção / não garante acerto.
- **Fidelidade** vs **literalidade**: preservar sentido e estilo / registrar tudo.
- **Erro de sentido** vs **erro de forma**: altera o que foi dito / não impede a compreensão.
- **Inaudível marcado** vs **inaudível completado**: rastreável / conjectura.
- **Aparte** vs **fala do Presidente vs discurso principal**: tipos de intervenção distintos.
- **Marcação de evento** vs **fala**: evento não é fala; convenção única.
- **Rótulo de diarização** vs **identificação do orador**: genérico / nome.
- **Normalização (texto→fala)** vs **normalização inversa, ITN (fala→texto escrito)**.
- **Normalização de texto** vs **correção de conteúdo**: forma / informação.
- **Normalização de texto** vs **normalização de áudio (volume)**.
- **CAT, transcrição assistida (traduz as notas estenotípicas em texto)** vs **memória de tradução (reaproveita segmentos já traduzidos entre idiomas); e "tradução das notas" (decifrar sinais e passar para texto) vs tradução de idioma**.
- **Editor de transcrição** vs **ASR**: onde o humano trabalha / gerador do rascunho.
- **Revisão em dupla (2º revisor independente)** vs **releitura pelo mesmo revisor**.
- **Auditoria de amostras (estima)** vs **revisão integral (examina tudo)**.
- **SLA (prazo e qualidade)** vs **apenas prazo**.
- **OOV (ausente do vocabulário)** vs **baixa confiança**.
- **Adaptação de modelo de linguagem (sequências, contexto)** vs **reforço de termos (palavras isoladas, com peso)**.
- **Reforço moderado** vs **sobre-reforço (falsos positivos)**.

## Pegadinhas

- [P2-2.1] **Diferença entre transcrição automática, degravação e revisão humana** — Trocar as definições (automática = humana; degravação = software).
- [P2-2.1] **Diferença entre transcrição automática, degravação e revisão humana** — Dizer que a boa qualidade do ASR dispensa a revisão humana.
- [P2-2.1] **Diferença entre transcrição automática, degravação e revisão humana** — Tratar degravação como sinônimo de taquigrafia (uma é posterior à gravação; a outra é simultânea).
- [P2-2.1] **Diferença entre transcrição automática, degravação e revisão humana** — Dizer que revisão humana é digitar tudo de novo.
- [P2-2.1] **Diferença entre transcrição automática, degravação e revisão humana** — Supor que o humano não erra: o controle da qualidade humana é o tema do 2.7.
- [P2-2.2] **Fluxo de trabalho de degravação assistida por IA (Human in the loop)** — HITL ≠ o revisor só olha trechos de baixa confiança.
- [P2-2.2] **Fluxo de trabalho de degravação assistida por IA (Human in the loop)** — HITL ≠ o humano transcreve do zero.
- [P2-2.2] **Fluxo de trabalho de degravação assistida por IA (Human in the loop)** — Revisão só de uma amostra no fim é supervisão ou auditoria (ON the loop), não HITL.
- [P2-2.2] **Fluxo de trabalho de degravação assistida por IA (Human in the loop)** — "Assistida" ≠ automática com publicação direta.
- [P2-2.2] **Fluxo de trabalho de degravação assistida por IA (Human in the loop)** — Retroalimentar o sistema com correções melhora o fluxo, mas não elimina a revisão seguinte.
- [P2-2.3] **Revisão e edição de transcrições: critérios de qualidade e fidelidade** — Fidelidade = literalidade absoluta.
- [P2-2.3] **Revisão e edição de transcrições: critérios de qualidade e fidelidade** — Qualquer correção gramatical é infidelidade (ou, no extremo oposto, o revisor pode "melhorar" o conteúdo).
- [P2-2.3] **Revisão e edição de transcrições: critérios de qualidade e fidelidade** — Completar o inaudível pelo contexto sem marcar.
- [P2-2.3] **Revisão e edição de transcrições: critérios de qualidade e fidelidade** — Tratar todos os erros como equivalentes.
- [P2-2.3] **Revisão e edição de transcrições: critérios de qualidade e fidelidade** — Reduzir qualidade a um número único de acerto de palavras (tema do Lote 1, não repetido aqui).
- [P2-2.4] **Formatação de transcrições parlamentares: identificação de oradores, marcação de pausa ruído, etc.** — Confundir marcação (evento) com fala.
- [P2-2.4] **Formatação de transcrições parlamentares: identificação de oradores, marcação de pausa ruído, etc.** — Afirmar que toda pausa deve ser registrada.
- [P2-2.4] **Formatação de transcrições parlamentares: identificação de oradores, marcação de pausa ruído, etc.** — Misturar fala do Presidente, aparte e discurso numa só linha.
- [P2-2.4] **Formatação de transcrições parlamentares: identificação de oradores, marcação de pausa ruído, etc.** — Dizer que a convenção de marcação é universal.
- [P2-2.4] **Formatação de transcrições parlamentares: identificação de oradores, marcação de pausa ruído, etc.** — Tratar rótulo de diarização ("Locutor 2") como identificação do orador.
- [P2-2.4] **Formatação de transcrições parlamentares: identificação de oradores, marcação de pausa ruído, etc.** — Atribuir a fala do aparteante ao orador que tem a palavra.
- [P2-2.5] **Normalização de texto: números, siglas, abreviações e termos técnicos** — Normalização = corrigir o que o orador disse (errada: é padronizar a forma, não corrigir a informação).
- [P2-2.5] **Normalização de texto: números, siglas, abreviações e termos técnicos** — Siglas sempre por extenso, ou números sempre em algarismos (generalização).
- [P2-2.5] **Normalização de texto: números, siglas, abreviações e termos técnicos** — Confundir com normalização de áudio (volume) ou de vetores.
- [P2-2.5] **Normalização de texto: números, siglas, abreviações e termos técnicos** — Dizer que a ITN é etapa do modelo acústico.
- [P2-2.5] **Normalização de texto: números, siglas, abreviações e termos técnicos** — Achar que a máquina decide sem erro entre ano e quantidade.
- [P2-2.5] **Normalização de texto: números, siglas, abreviações e termos técnicos** — Tratar o Manual de Redação como obrigatório para todo texto: a Portaria o torna obrigatório para documentos administrativos e apenas recomenda para os demais.
- [P2-2.6] **Ferramentas de CAT (Computer Assisted Transcription) e editores de transcrição** — Atribuir ao CAT da transcrição a memória de tradução, recurso de ferramentas de tradução entre idiomas.
- [P2-2.6] **Ferramentas de CAT (Computer Assisted Transcription) e editores de transcrição** — Confundir editor (onde o humano trabalha) com ASR (que gera o rascunho).
- [P2-2.6] **Ferramentas de CAT (Computer Assisted Transcription) e editores de transcrição** — Dizer que a ferramenta dispensa a revisão.
- [P2-2.6] **Ferramentas de CAT (Computer Assisted Transcription) e editores de transcrição** — Cobrar recurso de produto específico: sem fonte datada, não é seguro (cobrar o CONCEITO).
- [P2-2.6] **Ferramentas de CAT (Computer Assisted Transcription) e editores de transcrição** — Achar que formato de legenda não pode levar identificação de falante.
- [P2-2.6] **Ferramentas de CAT (Computer Assisted Transcription) e editores de transcrição** — Jargão: ler "tradução das notas" como tradução para outro idioma; em taquigrafia é decifrar os sinais e passar para texto.
- [P2-2.7] **Controle de qualidade: revisão em dupla, auditorias de amostras, SLA** — Revisão em dupla = o mesmo revisor lendo duas vezes.
- [P2-2.7] **Controle de qualidade: revisão em dupla, auditorias de amostras, SLA** — Amostra sem erro = lote sem erro.
- [P2-2.7] **Controle de qualidade: revisão em dupla, auditorias de amostras, SLA** — SLA = apenas prazo (ou: SLA = sistema de licenciamento).
- [P2-2.7] **Controle de qualidade: revisão em dupla, auditorias de amostras, SLA** — Auditoria = revisão integral.
- [P2-2.7] **Controle de qualidade: revisão em dupla, auditorias de amostras, SLA** — Dupla revisão garante zero erros.
- [P2-2.8] **Vocabulário técnico parlamentar e vocabulário adaptado (language model adaptation)** — OOV = baixa confiança (errado).
- [P2-2.8] **Vocabulário técnico parlamentar e vocabulário adaptado (language model adaptation)** — "Mais peso no reforço é sempre melhor" (generalização).
- [P2-2.8] **Vocabulário técnico parlamentar e vocabulário adaptado (language model adaptation)** — Adaptação de LM = retreino acústico.
- [P2-2.8] **Vocabulário técnico parlamentar e vocabulário adaptado (language model adaptation)** — Testar a adaptação nos mesmos dados usados para adaptar.
- [P2-2.8] **Vocabulário técnico parlamentar e vocabulário adaptado (language model adaptation)** — Pós-correção por LLM como garantia de fidelidade.
