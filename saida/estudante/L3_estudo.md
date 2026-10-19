# Lote 3 — IA Aplicada no Contexto Parlamentar; Proteção e segurança da informação (P2 3.1–4.3)

Prova: P2

## Itens do edital

- P2-3.1 — Aplicações de IA em parlamentos: transcrição de sessões, sumarização, indexação e busca
- P2-3.2 — Sistemas de busca semântica em acervos parlamentares
- P2-3.3 — Geração automática de atas e resumos de sessões
- P2-3.4 — Modelos de IA multilíngues e especializados em português
- P2-4.1 — LGPD e proteção de dados em sistemas de transcrição e IA
- P2-4.2 — Direitos autorais e ética no uso de IA para conteúdo gerado
- P2-4.3 — Segurança da informação em pipelines de áudio e transcrição

## Resumo

```text
3.1 IA em parlamento: transcrição, SUMARIZAÇÃO (extrativa copia /
abstrativa redige), INDEXAÇÃO (metadados, temas, entidades), BUSCA. Erro
da transcrição se propaga. IA apoia; oficial = revisão humana.
3.2 Busca semântica: embeddings (vetores), similaridade, chunking,
índice vetorial, reranking. Lexical (termos exatos) ≠ semântica
(sentido). Híbrida combina. RAG reduz, não elimina, alucinação.
Precisão × revocação.
3.3 Ata (formal) ≠ resumo. Fluxo: transcrição verificada → segmentação
→ campos factuais → geração → revisão humana. Riscos: omissão, inversão,
atribuição, alucinação (sem sustentação na fonte). Fluência ≠ fidelidade.
ROUGE mede semelhança de texto.
3.4 Multilíngue: um modelo, vários idiomas, desempenho desigual,
tokenização pior em idioma sub-representado. Especializado em
português: treinado ou ajustado em pt, não exclusivo de idioma. Domínio:
ajuste fino, RAG, prompt. Nomes de modelos: voláteis.
4.1 LGPD: dado pessoal (art. 5º, I); controlador decide
× operador executa (5º, VI e VII; 39; 42, § 1º, I); encarregado = canal
(5º, VIII; 41); princípios (6º, I–X); consentimento não é a única base
(7º); acesso público não é livre (7º, § 3º); LGPD vale para o poder
público (Cap. IV); art. 20: a redação original exigia revisão "por pessoa natural", expressão suprimida (MP nº 869/2018, convertida na Lei 13.853/2019); o § 3º foi vetado; a Lei 15.352/2026 cria a ANPD, autarquia de natureza
especial vinculada ao MJSP (55-A), e transfere a ela os acervos;
anonimizado deixa de ser pessoal, salvo reversão por meios próprios ou
com esforço razoável (12); a definição de pseudonimização (13, § 4º) vale
"para os efeitos deste artigo".
4.2 Lei 9.610/1998: alocuções protegidas (7º, II); leis
e atos oficiais não (8º, IV); autor = pessoa física (11); direitos
morais inalienáveis (24; 27; 49, I); patrimoniais exigem autorização
(29); domínio público ≠ disponível na internet (41; 45); limitações (46).
Pontos controversos: autoria e proteção de conteúdo gerado por IA;
licitude do treinamento; enquadramento do pronunciamento parlamentar
(7º, II × 8º, IV), com o art. 46, I, "b", só como indício. Ética:
transparência, responsável humano, revisão, não atribuir palavras não
ditas.
4.3 Segurança: confidencialidade, integridade, disponibilidade;
cifragem (trânsito e repouso), acesso mínimo, logs, retenção e
eliminação, fornecedor e local de processamento; prompt injection;
embeddings não são anônimos por presunção. LGPD: arts. 6º VII-VIII, 46,
47, 48 (controlador comunica), 49, 50, 33; pseudonimizar ≠ anonimizar
(12).
```

## Curso

```text
## 3.1 APLICAÇÕES DE IA EM PARLAMENTOS: TRANSCRIÇÃO, SUMARIZAÇÃO, INDEXAÇÃO E BUSCA

DEFINIÇÃO
Quatro famílias de aplicação sobre o acervo de sessões e reuniões:
 - Transcrição: fala → texto (itens 1.1 a 1.8 e 2.1 a 2.8). É a base das demais.
 - Sumarização: condensar o conteúdo. Pode ser EXTRATIVA (seleciona e
   copia trechos do original) ou ABSTRATIVA (redige frases novas a
   partir do original; é o caso dos LLMs).
 - Indexação: associar a cada documento metadados e termos que permitam
   recuperá-lo depois: tema, orador, proposição, órgão. A IA ajuda a
   extrair temas e entidades (nomes de pessoas, órgãos, números de
   proposições) e a classificar.
 - Busca: localizar documentos ou trechos; por palavras-chave, por
   semelhança de sentido (3.2) ou perguntas respondidas com base em
   trechos recuperados do acervo.
Encadeamento: a saída de uma etapa é a entrada da seguinte. Erro na
transcrição (nome trocado, "não" omitido) se propaga para resumo, índice
e busca, e o produto final parece mais confiável do que é.
Benefícios usuais: rapidez, acessibilidade (legendas), memória
institucional, ganho de escala. Riscos usuais: erro e texto fluente
porém falso, viés, perda de fidelidade, exposição de dados pessoais
(4.1), segurança do pipeline (4.3), opacidade, dependência de
fornecedor. Princípio de uso: a IA APOIA; o que vira registro oficial
passa por revisão humana (item 2.2).

EXEMPLO PARLAMENTAR
Sessão de comissão: o sistema transcreve; gera um resumo por pauta;
indexa por proposição e por parlamentar; um assessor pergunta "o que se
discutiu sobre determinado tema?" e recebe trechos com a indicação da
sessão. Se a transcrição trocou o número da proposição, o índice
associa a fala à proposição errada.

PEGADINHA PROVÁVEL
(1) Tratar sumarização como "transcrição menor" (resumo condensa e
reformula; transcrição reproduz). (2) Dizer que acervo público dispensa
supervisão e avaliação. (3) Ignorar a propagação de erros entre
etapas. (4) Chamar de "indexação" o que é busca, e vice-versa. (5) Dizer
que a IA "decide" o que é relevante sem critério humano: critérios,
tesauro e avaliação são definidos pela instituição.

Ato da Mesa nº 225, de 15/12/2025 (Câmara dos Deputados; DCD, Ed. Extra A,
18/12/2025, p. 9; Boletim Administrativo, 19/12/2025, p. 22; vigência na
publicação, art. 6º): estabelece diretrizes gerais para a política de
governança de inteligência artificial no âmbito da Câmara e determina sua
implementação pela Diretoria-Geral. Em paráfrase: o art. 3º fixa diretrizes
mínimas, entre elas uso de IA guiado por princípios éticos (transparência,
proteção de dados, não discriminação, supervisão humana: I); observância
da LGPD (III); regras para IA generativa, com requisitos para prompts,
agentes autônomos ou semiautônomos e revisão humana (V); informação ao
usuário que interage com agente de IA (VIII); supervisão contínua, inclusive
de falhas, vieses e alucinações (IX); o art. 4º, IV, atribui à
Diretoria-Geral criar e manter o comitê de ética de uso da IA.
Como contexto
deste item: reforça, na própria Casa, o princípio "a IA apoia; o registro
oficial passa por revisão humana". O texto lido NÃO trata de transcrição,
taquigrafia, reconhecimento de fala nem registro de sessões: por isso, não se pode afirmar que
o Ato regula os sistemas descritos nos itens 3.1 a 3.3. Norma interna, fora dos objetos de avaliação (Ato da Mesa nº 225/2025 da Câmara, no Legin, paráfrase, sem transcrição literal, verificado em 10/10/2026).

## 3.2 BUSCA SEMÂNTICA EM ACERVOS PARLAMENTARES

DEFINIÇÃO
Busca por palavras-chave (lexical): recupera documentos que contêm os
termos da consulta (ou variações tratadas por regras), ranqueados por
critérios como frequência. Falha quando a palavra do usuário não é a do
documento ("ocupação irregular" × "invasão").
Busca semântica: consulta e trechos do acervo são convertidos em
vetores numéricos (EMBEDDINGS) por um modelo; textos de sentido próximo
ficam próximos no espaço vetorial; a busca devolve os trechos mais
próximos da consulta (medida de similaridade, como o cosseno). Passos
típicos: dividir os documentos em trechos (chunking) → gerar embeddings
→ guardar em índice vetorial → embutir a consulta → recuperar os mais
próximos → opcionalmente reordenar (reranking).
Busca híbrida: combina as duas, porque termos exatos (número de
proposição, nome próprio, sigla) e semelhança de sentido atendem a
necessidades diferentes.
Perguntas e respostas sobre o acervo (RAG, geração com recuperação):
recupera trechos e pede a um LLM que responda com base neles, citando a
origem. Reduz, mas NÃO elimina, resposta inventada.
Limites: ambiguidade de siglas; nuances jurídicas; dependência da
qualidade do modelo de embeddings e da transcrição; vigência de normas
(o acervo traz versões antigas); permissões de acesso (documento
sigiloso não pode aparecer); resultado por proximidade, não prova de
que o texto "afirma" algo. Avaliação: precisão (quanto do recuperado é
relevante) e revocação (quanto do relevante foi recuperado).

EXEMPLO PARLAMENTAR
Consulta "gastos com viagens de parlamentares". A busca lexical perde
um pronunciamento que fala em "deslocamentos custeados pela Casa"; a
semântica o encontra. Já a consulta "PEC 45" é melhor atendida pela
busca lexical, porque o número exato importa mais que o sentido.

PEGADINHA PROVÁVEL
(1) Semântica = dicionário de sinônimos (é similaridade aprendida por
modelo). (2) Semântica sempre mais precisa que a lexical (para nome e
número exato, não é). (3) Dizer que a busca semântica "entende" ou
"verifica" fatos. (4) Dizer que RAG elimina a alucinação. (5) Confundir
precisão com revocação.



## 3.3 GERAÇÃO AUTOMÁTICA DE ATAS E RESUMOS DE SESSÕES

DEFINIÇÃO
Ata: documento formal que registra o ocorrido numa reunião (data, local,
presenças, pauta, deliberações, votações, encaminhamentos). Resumo:
condensação do conteúdo, de caráter informativo. O regime jurídico da ata
na Câmara (Regimento Interno e atos próprios) NÃO foi verificado; o curso trata só do princípio: documento que pode produzir efeitos exige
conferência e responsável humano.
Fluxo típico de geração automática:
 1. Transcrição verificada (a qualidade do que entra limita a do que
    sai).
 2. Segmentação por item de pauta.
 3. Extração de campos estruturados: presenças, proposições, resultado
    de votação, encaminhamentos.
 4. Geração do texto (em geral abstrativa), com modelo de estrutura
    fixo (template).
 5. Revisão humana obrigatória.
Riscos específicos:
 - Omissão e inversão: "aprovado" × "rejeitado", falta de "não".
 - Atribuição errada de fala ou voto.
 - Números e nomes trocados.
 - Alucinação: conteúdo NÃO SUSTENTADO pela fonte. O problema não é a
   frase ser nova (na abstração, é) mas ter informação que a transcrição
   não contém.
 - Fluência enganosa: texto bem escrito não prova fidelidade.
Mitigação: gerar a partir de transcrição verificada; separar campos
factuais (extração) de narrativa (geração); exigir citação do trecho-fonte para cada afirmação; lista de checagem (quórum, votação, nomes);
revisão humana e responsável identificado. Métricas automáticas de
resumo, como as baseadas em sobreposição de palavras (ex.: ROUGE),
medem semelhança de texto, não fidelidade factual.

EXEMPLO PARLAMENTAR
Ata gerada de uma reunião deliberativa: o modelo escreve "o requerimento
foi aprovado", mas a transcrição registra que foi retirado de pauta. O
campo de votação extraído da transcrição sinaliza o conflito, e o
revisor corrige antes de publicar.

PEGADINHA PROVÁVEL
(1) Trocar extrativa por abstrativa (extrativa copia; abstrativa
redige). (2) Texto fluente = texto fiel. (3) Resumo automático como
substituto da ata sem validação. (4) Achar que "frase nova" já é erro.
(5) Achar que métrica de sobreposição mede verdade.

## 3.4 MODELOS DE IA MULTILÍNGUES E ESPECIALIZADOS EM PORTUGUÊS

DEFINIÇÃO
 - Modelo multilíngue: um único modelo treinado com dados de vários
   idiomas, capaz de atender a todos. Características: o desempenho
   varia por idioma, em geral melhor nos de mais dados; a capacidade do
   modelo é compartilhada entre idiomas; o tokenizador pode fragmentar
   mais as palavras de idiomas sub-representados, o que aumenta tokens,
   custo e latência.
 - Modelo especializado em português: treinado ou ajustado com
   corpora em português, para captar vocabulário, variedades do
   português do Brasil (pt-BR) e, às vezes, um domínio (jurídico,
   legislativo). "Especializado" pode significar treinado do zero em
   português OU adaptado de um modelo multilíngue; não implica
   exclusividade de idioma. Ganhos possíveis: melhor compreensão de
   expressões locais e termos regimentais. Limites: pode perder
   generalidade e depender do volume de dados disponível.
 - Modelo de domínio (legislativo): obtém-se por ajuste fino com textos
   do domínio, por recuperação de documentos oficiais (RAG, 3.2) ou por
   instruções (prompts); não exige treinar do zero.
 - Fala e texto: o ASR multilíngue (itens 1.1 a 1.8) e o LLM multilíngue são
   componentes distintos; ser multilíngue num não garante no outro.
 - Particularidades do contexto: estrangeirismos, latinismos, siglas,
   mistura de idiomas na mesma fala e variação regional.
 - Avaliação: testar em tarefas e dados em português do domínio de uso,
   não só em resultados gerais.
 - Vigência: modelo treinado em data passada não conhece normas novas;
   por isso a recuperação de fontes oficiais atualizadas é prática
   comum (3.2).
 - Nomes e versões de modelos mudam em meses e NÃO foram verificados. A banca pode cobrar o CONCEITO, e não o nome do produto.

EXEMPLO PARLAMENTAR
Um modelo geral multilíngue resume bem um discurso em linguagem comum,
mas erra o sentido de um termo regimental; a equipe o complementa com a
recuperação do texto do Regimento e com um glossário, e mede o acerto em
pronunciamentos em português.

PEGADINHA PROVÁVEL
(1) Multilíngue = desempenho igual em todos os idiomas. (2) Especializado
= treinado exclusivamente em um idioma. (3) Especializar exige treinar do
zero. (4) Dizer que um modelo especializado "conhece" normas novas sem
atualização. (5) Cobrar nome de modelo (volátil e não verificado).


Todos os dispositivos abaixo estão em paráfrase. Fontes: LGPD compilada (Planalto) e Lei 9.610/1998 (Planalto), lidas em 08/10/2026.

## 4.1 LGPD E PROTEÇÃO DE DADOS EM SISTEMAS DE TRANSCRIÇÃO E IA

DEFINIÇÕES (LGPD)
 - Dado pessoal: informação relacionada a pessoa natural identificada ou
   identificável (art. 5º, I). A gravação da voz e as falas
   transcritas de pessoa identificada são dado pessoal.
 - Dado pessoal sensível: o art. 5º, II, enumera origem
   racial ou étnica, convicção religiosa, opinião política, filiação a
   sindicato ou a organização de caráter religioso, filosófico ou
   político, dado referente à saúde ou à vida sexual, dado genético e
   dado biométrico quando vinculado a pessoa natural.
   O caráter taxativo dessa enumeração é debate doutrinário.
   O ponto é controverso: a lei não define "dado biométrico"; se
   toda gravação de voz, ou se uma fala parlamentar, é dado sensível
   depende de interpretação. Já a impressão vocal usada para identificar
   o locutor tende a ser tratada como biométrica, mas isso não deve ser tomado como certo.
 - Titular (art. 5º, V), controlador (VI: a quem competem as DECISÕES
   sobre o tratamento), operador (VII: realiza o tratamento EM NOME do
   controlador), encarregado (VIII: canal de comunicação entre
   controlador, titulares e ANPD), agentes de tratamento (IX: controlador
   e operador).
 - Tratamento (art. 5º, X): qualquer operação com dados pessoais; inclui
   coleta, armazenamento, processamento, compartilhamento e eliminação.
   Transcrever e sumarizar são tratamento.
 - Anonimização e pseudonimização: dado anonimizado é o
   que não pode ser associado a um titular por meios técnicos razoáveis
   e disponíveis (art. 5º, III); anonimização é a utilização desses
   meios para que o dado perca a possibilidade de associação, direta ou
   indireta, a um indivíduo (art. 5º, XI). O dado anonimizado não é
   dado pessoal (art. 12, caput), SALVO se o processo for revertido
   utilizando exclusivamente meios próprios ou se a reversão for possível
   com esforços razoáveis (art. 12, caput; fatores como custo e tempo, §
   1º). A pseudonimização é definida no art. 13, § 4º, "para os efeitos
   deste artigo", que trata de estudos em saúde pública: o dado perde a
   associação a um indivíduo, senão pelo uso de informação adicional
   mantida separadamente pelo controlador em ambiente controlado e
   seguro. Essa definição tem alcance restrito ao art. 13. A distinção
   geral se apoia no art. 12: se o próprio controlador consegue reverter
   com a tabela que guarda, o dado continua pessoal. Pseudonimizar NÃO é,
   por si, anonimizar.
 - Princípios (art. 6º, I a X): finalidade, adequação, necessidade (o
   mínimo necessário), livre acesso, qualidade dos dados (exatidão,
   clareza, relevância e atualização), transparência, segurança,
   prevenção, não discriminação e responsabilização e prestação de
   contas.
 - Hipóteses de tratamento (art. 7º): entre outras, consentimento (I),
   obrigação legal (II), pela administração pública para políticas
   públicas (III), legítimo interesse (IX). O consentimento NÃO é a
   única base. Dados de acesso público: o tratamento deve considerar a
   finalidade, a boa-fé e o interesse público que justificaram a
   disponibilização (art. 7º, § 3º); a dispensa de consentimento para
   dados manifestamente públicos pelo titular não afasta os direitos
   do titular nem os princípios (art. 7º, § 4º); o uso para novas
   finalidades exige propósito legítimo e específico (art. 7º, § 7º).
 - Poder público (Capítulo IV): tratamento para a finalidade pública, com
   informação clara das hipóteses e indicação de encarregado (art. 23, I
   e III); o uso compartilhado atende a finalidades específicas (art. 26).
   A LGPD SE APLICA ao poder público.
 - Decisões automatizadas (art. 20): o titular pode solicitar a revisão
   de decisões tomadas unicamente com base em tratamento automatizado
   que afetem seus interesses, e o controlador deve informar os critérios
   e procedimentos, observados os segredos comercial e industrial. O texto
   vigente NÃO diz que a revisão seja feita por pessoa natural: a redação
   original do caput exigia revisão "por pessoa natural", e a MP nº 869/2018, convertida na Lei 13.853/2019, suprimiu a expressão (na
   página compilada, o caput traz a anotação "Redação dada pela Lei nº
   13.853, de 2019"). O § 3º, incluído pela Lei 13.853/2019, consta como vetado na página compilada, com remissão à VEP nº 288/2019; o conteúdo do veto não foi conferido. Cuidado com a
   redação superada.
 - Governança: registro das operações (art. 37); relatório de impacto à
   proteção de dados (RIPD, art. 5º, XVII) que a autoridade nacional
   pode determinar (art. 38) e pedir ao poder público (art. 32);
   operador segue as instruções do controlador (art. 39); encarregado
   indicado pelo controlador (art. 41).
 - Responsabilidade: o operador responde solidariamente quando descumpre
   a legislação ou as instruções lícitas do controlador (art. 42, § 1º,
   I).
 - Autoridade nacional e ANPD: a "autoridade nacional" é a entidade da
   administração pública responsável por zelar, implementar e fiscalizar o
   cumprimento da Lei em todo o território nacional (art. 5º, XIX, redação
   da Lei 15.352/2026). A Lei 15.352/2026 CRIA a Agência Nacional de
   Proteção de Dados (ANPD), autarquia de natureza especial vinculada ao
   Ministério da Justiça e Segurança Pública (nova redação do art. 55-A),
   e TRANSFERE a ela os acervos (art. 15 da Lei 15.352/2026). A autoridade nacional não "é" a Agência por definição; passou a
   ser exercida por ela. A redação anterior (órgão da Presidência da
   República) está SUPERADA.
 - Sanções (art. 52, § 3º): algumas sanções administrativas podem ser
   aplicadas a entes e órgãos públicos (incisos I, IV, V, VI, X, XI e
   XII do caput); a multa (incisos II e III) não consta dessa lista.

APLICAÇÃO A TRANSCRIÇÃO E IA
Fala, voz e transcrição de pessoas identificadas são dados pessoais. Ao
contratar um serviço de terceiro, a Casa tende a ser controladora e o
fornecedor, operadora (conforme o desenho do contrato). Finalidade pública
específica, minimização e segurança orientam o desenho; qualidade dos
dados (art. 6º, V) conecta-se à exatidão da transcrição.

EXEMPLO PARLAMENTAR
O órgão contrata um serviço de transcrição de audiências. Ele decide as
finalidades e as instruções; o fornecedor processa o áudio em seu nome.
Se o fornecedor usar o áudio para finalidade própria, extrapola as
instruções e responde solidariamente (art. 42, § 1º, I).

PEGADINHA PROVÁVEL
(1) Consentimento como única base legal. (2) Dado público = livre para
qualquer fim (art. 7º, § 3º). (3) LGPD não se aplica ao poder público.
(4) Trocar controlador e operador (quem decide × quem executa).
(5) Revisão de decisão automatizada "por pessoa natural" (redação
superada). (6) ANPD como órgão da Presidência (redação superada), ou
"a autoridade nacional é a Agência" sem a criação pela Lei 15.352/2026.
(7) Pseudonimização = anonimização (a definição do art. 13, § 4º, tem
alcance restrito; a distinção geral vem do art. 12). (8) Encarregado como
quem decide as finalidades (é canal de comunicação). (9) Citar a página
multivigente da LGPD, que mistura redações.

Contexto institucional — Ato da Mesa nº 225, de 15/12/2025 (DCD, Ed.
Extra A, 18/12/2025): estabelece diretrizes gerais para a política de
governança de inteligência artificial no âmbito da Câmara dos Deputados
e determina sua implementação pela Diretoria-Geral. Em síntese, o art.
3º orienta a política para: princípios éticos, entre eles transparência,
proteção de dados, não discriminação e supervisão humana (I);
conformidade com a LGPD (III); disciplina do uso de IA generativa, com
requisitos para prompts, para agentes autônomos ou semiautônomos e para
revisão humana (V); informação ao usuário quando interage com agentes de
IA (VIII); supervisão que inclui o monitoramento de vieses e alucinações
(IX). O art. 4º, IV, prevê comitê de ética de uso da IA. Norma interna; referência de contexto.

## 4.2 DIREITOS AUTORAIS E ÉTICA NO USO DE IA PARA CONTEÚDO GERADO

DEFINIÇÕES (Lei 9.610/1998, texto do Planalto)
 - Obras protegidas (art. 7º): criações do espírito fixadas em qualquer
   suporte; entre elas, as conferências, alocuções, sermões e outras da
   mesma natureza (II); adaptações e traduções apresentadas como criação
   nova (XI); coletâneas e bases de dados que, pela seleção ou
   organização, sejam criação intelectual (XIII). A proteção da base de
   dados não abarca os dados em si (art. 7º, § 2º).
 - Não protegidos (art. 8º): ideias e métodos como tais (I); textos de
   tratados, leis, decretos, regulamentos, decisões judiciais e demais
   atos oficiais (IV); informações de uso comum (V); nomes e títulos
   isolados (VI). Texto de lei não é obra protegida.
 - Autor: a pessoa física criadora da obra (art. 11). A proteção
   independe de registro (art. 18).
 - Direitos morais (art. 24): entre eles, reivindicar a autoria (I), ter
   o nome indicado na utilização da obra (II) e assegurar a integridade,
   opondo-se a modificações que possam prejudicá-la ou atingi-lo em sua
   reputação ou honra (IV). São inalienáveis e irrenunciáveis (art. 27);
   a cessão total não os compreende (art. 49, I).
 - Direitos patrimoniais (arts. 28 e 29): dependem de autorização
   prévia e expressa do autor a reprodução (I), a adaptação e outras
   transformações (III) e a inclusão em base de dados e o armazenamento
   em computador (IX), entre outras modalidades. "Reprodução" inclui o
   armazenamento permanente ou temporário por meios eletrônicos (art.
   5º, VI). A cessão se interpreta restritivamente (art. 4º).
 - Domínio público: setenta anos contados de 1º de janeiro do ano
   seguinte ao falecimento (art. 41) e as demais hipóteses do art. 45.
   Estar disponível na internet NÃO é estar em domínio público.
 - Limitações (art. 46), entre outras: reprodução, em diários ou
   periódicos, de discursos pronunciados em reuniões públicas de
   qualquer natureza (I, b); citação para estudo, crítica ou polêmica,
   na medida justificada e com indicação do autor e da origem (III);
   uso para produzir prova judiciária ou administrativa (VII); pequenos
   trechos, sem prejuízo da exploração normal da obra nem dos
   interesses legítimos dos autores (VIII). Paráfrases e paródias que
   não sejam verdadeiras reproduções nem impliquem descrédito são livres
   (art. 47).
Pontos controversos (não há texto legal expresso nem
jurisprudência firmada que se possa afirmar):
 (a) se conteúdo gerado por IA é obra protegida e quem seria o titular;
 (b) se o treinamento de modelos com obras protegidas configura
     reprodução ilícita ou se se enquadra em alguma limitação;
 (c) a responsabilidade por saídas que reproduzam trechos protegidos;
 (d) a aplicação do art. 46, VIII ao treinamento;
 (e) a aplicação do direito de integridade (art. 24, IV) a um resumo de
     discurso gerado por IA (inferência de aplicação, que não se pode afirmar como certa);
 (f) o ENQUADRAMENTO do pronunciamento parlamentar em sessão: alocução
     protegida (art. 7º, II) ou ato oficial (art. 8º, IV). NÃO está
     firmado. INDÍCIO legal, e não enquadramento definitivo: o art. 46, I,
     "b", ao permitir reproduzir na imprensa discursos de reuniões
     públicas, trata discursos como matéria de direito autoral, sujeita a
     limitação.
Itens C/E só sobre o texto da Lei 9.610/1998 ou conceitos estáveis.
ÉTICA (conceitos estáveis, sem norma específica verificada):
transparência sobre o uso de IA; responsabilidade humana pelo texto
publicado; revisão humana; não atribuir a ninguém palavras que não disse;
rastreabilidade das fontes; não discriminação (princípio do art. 6º, IX,
da LGPD); proteção de dados (4.1).

EXEMPLO PARLAMENTAR
O serviço publica um resumo automático de um discurso sem indicar que
foi gerado por IA e atribuindo ao orador frases que ele não disse. Sem
sustentar tese autoral controversa, o caso mostra o problema ético:
falta transparência e responsável humano, e o texto atribuído ao orador
não corresponde ao que foi dito.

PEGADINHA PROVÁVEL
(1) Textos de lei são protegidos (art. 8º, IV: não são). (2) "Disponível
na internet" = domínio público. (3) Direitos morais se cedem com os
patrimoniais (art. 27; art. 49, I). (4) Afirmar como certo se a IA gera
obra protegida ou se o treinamento é lícito (controverso). (5) Esquecer
que a proteção independe de registro (art. 18). (6) Confundir citação
(art. 46, III) com reprodução integral livre. (7) Afirmar como certo que o
pronunciamento parlamentar é obra protegida ou, ao contrário, ato oficial
(enquadramento não firmado).



## 4.3 SEGURANÇA DA INFORMAÇÃO EM PIPELINES DE ÁUDIO E TRANSCRIÇÃO

DEFINIÇÃO
Segurança da informação protege três propriedades: confidencialidade
(só quem pode acessa), integridade (o dado não é alterado sem
autorização) e disponibilidade (está acessível quando necessário).
Pipeline típico, e onde agir:
 1. Captação do áudio: autenticidade da fonte; risco de áudio sintético
    ou adulterado (deepfake de voz).
 2. Transmissão: criptografia em trânsito.
 3. Armazenamento (áudio bruto, transcrições, embeddings, registros de
    acesso, backups): criptografia em repouso, gestão de chaves,
    segregação de ambientes.
 4. Processamento (ASR, LLM, busca): local ou em nuvem; quem é o
    fornecedor, onde processa, se há subcontratados, se usa os dados do
    cliente para outro fim (verificar no contrato; não presumir).
 5. Revisão e publicação: controle de acesso por perfil e privilégio
    mínimo; autenticação forte; registro (log) e trilha de auditoria.
 6. Retenção e eliminação: prazo definido; eliminar o áudio bruto quando
    cessar a finalidade, salvo conservação autorizada (LGPD, arts. 15 e
    16).
 7. Resposta a incidentes e comunicação.
Riscos específicos de IA:
 - Envio do áudio a serviço externo (perda de custódia; item 1.8).
 - Injeção de instruções (prompt injection): texto transcrito ou
   recuperado, que contém comandos maliciosos, manipula o LLM que o
   processa; tratar conteúdo transcrito como dado, não como instrução.
 - Embeddings e vetores: não presumir que sejam anônimos; podem conter
   informação sobre o texto original.
 - Integridade: sem controle (por exemplo, impressão digital criptográfica
   do arquivo), a transcrição pode ser alterada sem rastro.
Dispositivos da LGPD (paráfrase):
 - Segurança e prevenção como princípios (art. 6º, VII e VIII).
 - Dever de adotar medidas de segurança técnicas e administrativas aptas
   a proteger os dados de acessos não autorizados e de situações
   acidentais ou ilícitas de destruição, perda, alteração, comunicação ou
   tratamento inadequado (art. 46, caput), observadas desde a concepção
   do produto ou serviço até a sua execução (art. 46, § 2º); a autoridade
   pode fixar padrões mínimos (art. 46, § 1º).
 - O dever de segurança persiste mesmo após o término do tratamento (art.
   47); os sistemas devem ser estruturados para atender aos requisitos
   de segurança e boas práticas (art. 49).
 - Incidente que possa acarretar risco ou dano relevante: o controlador
   comunica a autoridade nacional e o titular, em prazo razoável
   definido pela autoridade, com conteúdo mínimo (natureza dos dados,
   titulares envolvidos, medidas de proteção usadas, riscos, motivos da
   demora, medidas adotadas) (art. 48, caput e § 1º).
 - Boas práticas e governança, com programa de governança em privacidade
   (art. 50).
 - Transferência internacional: transferência de dados pessoais para país
   estrangeiro ou organismo internacional (art. 5º, XV), permitida só nos
   casos do art. 33 (entre eles, país com grau de proteção adequado, art.
   33, I; garantias oferecidas pelo controlador, art. 33, II; e execução
   de política pública, com publicidade, art. 33, VII). Enviar áudio de
   pessoas identificadas a serviço com servidores no exterior pode
   configurar transferência internacional.

EXEMPLO PARLAMENTAR
O áudio de uma reunião reservada é enviado a um serviço de transcrição
em nuvem. O desenho correto prevê: cifragem em trânsito e em repouso,
acesso restrito e registrado, prazo de retenção, cláusula sobre local de
processamento e subcontratados, e plano de comunicação de incidentes.

PEGADINHA PROVÁVEL
(1) Cifrar o áudio resolve toda a segurança (e acesso, registro, retenção?
não dispensa). (2) Pseudonimizar = anonimizar: a definição do art. 13, §
4º, vale "para os efeitos deste artigo"; a distinção geral vem do art.
12 (se a reversão é possível por meios próprios, o dado segue pessoal).
(3) Quem comunica o incidente: o controlador, não o operador (art. 48).
(4) Segurança só no armazenamento, e não na transmissão e no
processamento. (5) Achar que nuvem no exterior nunca é possível ou que
sempre é livre: depende do art. 33. (6) Esquecer o dever de segurança
após o fim do tratamento.
```

## Pares

- **Transcrição** vs **sumarização**: reproduz / condensa e reformula.
- **Sumarização extrativa** vs **abstrativa**: copia trechos / redige frases novas.
- **Indexação** vs **busca**: organizar para recuperar / recuperar.
- **Busca lexical** vs **busca semântica**: termos exatos / sentido.
- **Busca semântica** vs **busca híbrida**: só vetores / vetores + termos.
- **Busca semântica** vs **RAG**: recupera trechos / recupera e gera resposta.
- **Precisão** vs **revocação**: relevante entre o recuperado / recuperado entre o relevante.
- **Ata** vs **resumo**: registro formal / condensação informativa.
- **Alucinação** vs **reformulação**: informação sem sustentação na fonte / frase nova com sentido fiel.
- **Fluência** vs **fidelidade do texto gerado**.
- **Modelo multilíngue** vs **especializado em português**.
- **Especializado (treinado/ajustado em pt)** vs **exclusivo (só pt)**.
- **Ajuste fino** vs **RAG**: altera o modelo / fornece documentos na consulta.
- **Controlador (decide)** vs **operador (executa em nome)**.
- **Controlador** vs **encarregado**: decide / canal de comunicação.
- **Dado pessoal** vs **dado pessoal sensível (enumeração do art. 5º, II)**.
- **Anonimização (art. 12: dado deixa de ser pessoal, salvo reversão por meios próprios ou com esforço razoável)** vs **pseudonimização (art. 13, § 4º, definida "para os efeitos deste artigo", com informação adicional guardada separadamente)**.
- **Consentimento** vs **outras hipóteses do art. 7º**.
- **Dado de acesso público** vs **dado livre para qualquer uso**.
- **Revisão de decisão automatizada (art. 20)** vs **revisão por pessoa natural (redação original, suprimida pela MP nº 869/2018, convertida na Lei 13.853/2019)**.
- **Autoridade nacional (art. 5º, XIX)** vs **ANPD criada pela Lei 15.352/2026 (autarquia vinculada ao MJSP); órgão da Presidência (redação superada)**.
- **Obra protegida** vs **ato oficial não protegido (art. 8º, IV)**.
- **Domínio público** vs **disponível na internet**.
- **Direitos morais** vs **patrimoniais**.
- **Citação (art. 46, III)** vs **reprodução integral**.
- **Confidencialidade, integridade, disponibilidade**.
- **Criptografia em trânsito** vs **em repouso**.
- **Incidente de segurança (comunica o controlador)** vs **vazamento interno sem risco relevante**.

## Pegadinhas

- [P2-3.1] **Aplicações de IA em parlamentos: transcrição de sessões, sumarização, indexação e busca** — Tratar sumarização como "transcrição menor" (resumo condensa e reformula; transcrição reproduz).
- [P2-3.1] **Aplicações de IA em parlamentos: transcrição de sessões, sumarização, indexação e busca** — Dizer que acervo público dispensa supervisão e avaliação.
- [P2-3.1] **Aplicações de IA em parlamentos: transcrição de sessões, sumarização, indexação e busca** — Ignorar a propagação de erros entre etapas.
- [P2-3.1] **Aplicações de IA em parlamentos: transcrição de sessões, sumarização, indexação e busca** — Chamar de "indexação" o que é busca, e vice-versa.
- [P2-3.1] **Aplicações de IA em parlamentos: transcrição de sessões, sumarização, indexação e busca** — Dizer que a IA "decide" o que é relevante sem critério humano: critérios, tesauro e avaliação são definidos pela instituição.
- [P2-3.1] **Aplicações de IA em parlamentos: transcrição de sessões, sumarização, indexação e busca** — Não confunda sumarização extrativa com sumarização abstrativa: a extrativa seleciona e copia trechos do original; a abstrativa redige frases novas a partir do original, caso dos LLMs.
- [P2-3.2] **Sistemas de busca semântica em acervos parlamentares** — Semântica = dicionário de sinônimos (é similaridade aprendida por modelo).
- [P2-3.2] **Sistemas de busca semântica em acervos parlamentares** — Semântica sempre mais precisa que a lexical (para nome e número exato, não é).
- [P2-3.2] **Sistemas de busca semântica em acervos parlamentares** — Dizer que a busca semântica "entende" ou "verifica" fatos.
- [P2-3.2] **Sistemas de busca semântica em acervos parlamentares** — Dizer que RAG elimina a alucinação.
- [P2-3.2] **Sistemas de busca semântica em acervos parlamentares** — Confundir precisão com revocação.
- [P2-3.2] **Sistemas de busca semântica em acervos parlamentares** — Não confunda busca semântica com busca híbrida: a semântica converte consulta e trechos em vetores (embeddings) e devolve os mais próximos; a híbrida combina busca lexical e semântica, porque termos exatos, como número de proposição, nome próprio e sigla, e semelhança de sentido atendem a necessidades diferentes.
- [P2-3.2] **Sistemas de busca semântica em acervos parlamentares** — Não confunda busca semântica com RAG (geração com recuperação): a busca semântica devolve os trechos mais próximos da consulta; o RAG recupera trechos e pede a um LLM que responda com base neles, citando a origem.
- [P2-3.3] **Geração automática de atas e resumos de sessões** — Trocar extrativa por abstrativa (extrativa copia; abstrativa redige).
- [P2-3.3] **Geração automática de atas e resumos de sessões** — Texto fluente = texto fiel.
- [P2-3.3] **Geração automática de atas e resumos de sessões** — Resumo automático como substituto da ata sem validação.
- [P2-3.3] **Geração automática de atas e resumos de sessões** — Achar que "frase nova" já é erro.
- [P2-3.3] **Geração automática de atas e resumos de sessões** — Achar que métrica de sobreposição mede verdade.
- [P2-3.3] **Geração automática de atas e resumos de sessões** — Não confunda ata com resumo: a ata é o documento formal que registra o ocorrido numa reunião, com data, local, presenças, pauta, deliberações, votações e encaminhamentos; o resumo é a condensação do conteúdo, de caráter informativo.
- [P2-3.3] **Geração automática de atas e resumos de sessões** — Não confunda alucinação com reformulação: alucinação é conteúdo não sustentado pela fonte, isto é, informação que a transcrição não contém; a reformulação é frase nova com sentido fiel, própria da sumarização abstrativa. Frase nova, por si, não é erro.
- [P2-3.4] **Modelos de IA multilíngues e especializados em português** — Multilíngue = desempenho igual em todos os idiomas.
- [P2-3.4] **Modelos de IA multilíngues e especializados em português** — Especializado = treinado exclusivamente em um idioma.
- [P2-3.4] **Modelos de IA multilíngues e especializados em português** — Especializar exige treinar do zero.
- [P2-3.4] **Modelos de IA multilíngues e especializados em português** — Dizer que um modelo especializado "conhece" normas novas sem atualização.
- [P2-3.4] **Modelos de IA multilíngues e especializados em português** — Cobrar nome de modelo (volátil e não verificado).
- [P2-3.4] **Modelos de IA multilíngues e especializados em português** — Não confunda modelo multilíngue com modelo especializado em português: o multilíngue é um único modelo treinado com dados de vários idiomas, com desempenho que varia por idioma; o especializado é treinado ou ajustado com corpora em português, para captar vocabulário e variedades do pt-BR.
- [P2-3.4] **Modelos de IA multilíngues e especializados em português** — Não confunda ajuste fino com recuperação de documentos oficiais (RAG): o ajuste fino com textos do domínio altera o modelo; o RAG fornece documentos na consulta, por recuperação. Nenhum dos dois exige treinar do zero.
- [P2-4.1] **LGPD e proteção de dados em sistemas de transcrição e IA** — Consentimento como única base legal.
- [P2-4.1] **LGPD e proteção de dados em sistemas de transcrição e IA** — Dado público = livre para qualquer fim (art. 7º, § 3º).
- [P2-4.1] **LGPD e proteção de dados em sistemas de transcrição e IA** — LGPD não se aplica ao poder público.
- [P2-4.1] **LGPD e proteção de dados em sistemas de transcrição e IA** — Trocar controlador e operador (quem decide × quem executa).
- [P2-4.1] **LGPD e proteção de dados em sistemas de transcrição e IA** — Revisão de decisão automatizada "por pessoa natural" (redação superada).
- [P2-4.1] **LGPD e proteção de dados em sistemas de transcrição e IA** — ANPD como órgão da Presidência (redação superada), ou "a autoridade nacional é a Agência" sem a criação pela Lei 15.352/2026.
- [P2-4.1] **LGPD e proteção de dados em sistemas de transcrição e IA** — Pseudonimização = anonimização (a definição do art. 13, § 4º, tem alcance restrito; a distinção geral vem do art. 12).
- [P2-4.1] **LGPD e proteção de dados em sistemas de transcrição e IA** — Encarregado como quem decide as finalidades (é canal de comunicação).
- [P2-4.1] **LGPD e proteção de dados em sistemas de transcrição e IA** — Citar a página multivigente da LGPD, que mistura redações.
- [P2-4.1] **LGPD e proteção de dados em sistemas de transcrição e IA** — Não confunda dado pessoal com dado pessoal sensível: dado pessoal é a informação relacionada a pessoa natural identificada ou identificável (art. 5º, I); sensível é o que o art. 5º, II, enumera, como origem racial ou étnica, opinião política, dado referente à saúde e dado genético.
- [P2-4.2] **Direitos autorais e ética no uso de IA para conteúdo gerado** — Textos de lei são protegidos (art. 8º, IV: não são).
- [P2-4.2] **Direitos autorais e ética no uso de IA para conteúdo gerado** — "Disponível na internet" = domínio público.
- [P2-4.2] **Direitos autorais e ética no uso de IA para conteúdo gerado** — Direitos morais se cedem com os patrimoniais (art. 27; art. 49, I).
- [P2-4.2] **Direitos autorais e ética no uso de IA para conteúdo gerado** — Afirmar como certo se a IA gera obra protegida ou se o treinamento é lícito (controverso).
- [P2-4.2] **Direitos autorais e ética no uso de IA para conteúdo gerado** — Esquecer que a proteção independe de registro (art. 18).
- [P2-4.2] **Direitos autorais e ética no uso de IA para conteúdo gerado** — Confundir citação (art. 46, III) com reprodução integral livre.
- [P2-4.2] **Direitos autorais e ética no uso de IA para conteúdo gerado** — Afirmar como certo que o pronunciamento parlamentar é obra protegida ou, ao contrário, ato oficial (enquadramento não firmado).
- [P2-4.3] **Segurança da informação em pipelines de áudio e transcrição** — Cifrar o áudio resolve toda a segurança (e acesso, registro, retenção? não dispensa).
- [P2-4.3] **Segurança da informação em pipelines de áudio e transcrição** — Pseudonimizar = anonimizar: a definição do art. 13, § 4º, vale "para os efeitos deste artigo"; a distinção geral vem do art. 12 (se a reversão é possível por meios próprios, o dado segue pessoal).
- [P2-4.3] **Segurança da informação em pipelines de áudio e transcrição** — Quem comunica o incidente: o controlador, não o operador (art. 48).
- [P2-4.3] **Segurança da informação em pipelines de áudio e transcrição** — Segurança só no armazenamento, e não na transmissão e no processamento.
- [P2-4.3] **Segurança da informação em pipelines de áudio e transcrição** — Achar que nuvem no exterior nunca é possível ou que sempre é livre: depende do art. 33.
- [P2-4.3] **Segurança da informação em pipelines de áudio e transcrição** — Esquecer o dever de segurança após o fim do tratamento.
- [P2-4.3] **Segurança da informação em pipelines de áudio e transcrição** — Não confunda criptografia em trânsito com criptografia em repouso: a primeira protege os dados durante a transmissão; a segunda protege os dados armazenados, como áudio bruto, transcrições, embeddings, registros de acesso e backups, e se acompanha de gestão de chaves.

## Tópico P2-3.1 — Aplicações de IA em parlamentos: transcrição de sessões, sumarização, indexação e busca

### Resumo do tópico

A IA em parlamentos se organiza em quatro famílias de aplicação sobre o acervo de sessões e reuniões. A transcrição converte fala em texto e é a base das demais. A sumarização condensa o conteúdo, de modo extrativo, que seleciona e copia trechos, ou abstrativo, que redige frases novas, caso dos LLMs. A indexação associa metadados, como tema, orador, proposição e órgão. A busca localiza documentos ou trechos.

As etapas são encadeadas: a saída de uma é a entrada da seguinte. Um erro de transcrição, como nome trocado ou "não" omitido, se propaga para o resumo, o índice e a busca, e o produto final parece mais confiável do que é. Se a transcrição trocar o número da proposição, o índice associa a fala à proposição errada.

Os benefícios usuais são rapidez, acessibilidade, memória institucional e ganho de escala. Os riscos são erro e texto fluente porém falso, viés, perda de fidelidade, exposição de dados pessoais, opacidade e dependência de fornecedor. A IA apoia, e o que vira registro oficial passa por revisão humana.

Sumarização não é transcrição menor, pois o resumo condensa e reformula e a transcrição reproduz. A IA também não decide sozinha o que é relevante: critérios, tesauro e avaliação são definidos pela instituição, e acervo público não dispensa supervisão e avaliação.

O Ato da Mesa nº 225/2025, norma interna fora dos objetos de avaliação, fixa diretrizes de governança de IA na Câmara, como supervisão humana (art. 3º, I) e conformidade com a LGPD (III). Não trata de transcrição, taquigrafia nem registro de sessões, e não se pode afirmar que regule os sistemas aqui descritos.

## Tópico P2-3.2 — Sistemas de busca semântica em acervos parlamentares

### Resumo do tópico

A busca lexical recupera documentos que contêm os termos da consulta e falha quando a palavra do usuário não é a do documento. A busca semântica converte consulta e trechos em embeddings, vetores numéricos, e devolve os trechos de sentido mais próximo.

Os passos típicos são dividir os documentos em trechos, gerar embeddings, guardar em índice vetorial, embutir a consulta, recuperar os mais próximos e, opcionalmente, reordenar.

A busca híbrida combina as duas, porque termos exatos, como o número de uma proposição, pedem a busca lexical, e a semelhança de sentido atende outra necessidade. A semântica nem sempre é mais precisa.

Nem a busca semântica nem o RAG, geração com recuperação, verificam fatos. O RAG pede ao LLM que responda com base nos trechos recuperados e reduz, mas não elimina, a resposta inventada.

A avaliação da busca usa duas medidas: a precisão, que mede quanto do recuperado é relevante, e a revocação, que mede quanto do relevante foi recuperado.

## Tópico P2-3.3 — Geração automática de atas e resumos de sessões

### Resumo do tópico

Ata é o documento formal que registra o ocorrido na reunião, com presenças, pauta, deliberações, votações e encaminhamentos. Resumo é a condensação informativa do conteúdo. O regime jurídico da ata na Câmara não é tratado aqui; fica o princípio: documento que pode produzir efeitos exige conferência e responsável humano.

O fluxo típico parte de transcrição verificada, segmenta por item de pauta, extrai campos estruturados, gera o texto em geral de forma abstrativa com modelo de estrutura fixo e termina em revisão humana obrigatória.

Os riscos específicos são omissão e inversão, como "aprovado" por "rejeitado", atribuição errada de fala ou voto, números e nomes trocados e fluência enganosa. Alucinação é conteúdo não sustentado pela fonte; a frase ser nova não é o problema.

A mitigação separa campos factuais, extraídos, da narrativa gerada, exige citação do trecho-fonte e mantém revisão humana. Métricas de sobreposição, como ROUGE, medem semelhança de texto, não fidelidade factual.

## Tópico P2-3.4 — Modelos de IA multilíngues e especializados em português

### Resumo do tópico

O modelo multilíngue é um único modelo treinado com dados de vários idiomas. Seu desempenho varia por idioma, em geral melhor nos de mais dados. O tokenizador pode fragmentar mais as palavras de idiomas sub-representados, o que aumenta tokens, custo e latência.

O modelo especializado em português é treinado ou ajustado com corpora em português, para captar vocabulário e variedades do pt-BR. Pode ser treinado do zero ou adaptado de um multilíngue, sem exclusividade de idioma. Pode ganhar em expressões locais e termos regimentais, mas pode perder generalidade.

Um modelo de domínio legislativo se obtém por ajuste fino, por recuperação de documentos oficiais (RAG) ou por instruções, sem treinar do zero. Como o modelo não conhece normas posteriores ao treino, a recuperação de fontes oficiais atualizadas é prática comum.

O ASR multilíngue e o LLM multilíngue são componentes distintos: ser multilíngue num não garante no outro. A avaliação deve usar dados em português do domínio de uso.

Nomes e versões de modelos mudam em meses e são voláteis, e a banca pode cobrar o conceito, como multilíngue, especializado ou de domínio, e não o nome do produto.

## Tópico P2-4.1 — LGPD e proteção de dados em sistemas de transcrição e IA

### Resumo do tópico

Dado pessoal é a informação relacionada a pessoa natural identificada ou identificável (art. 5º, I), inclusive voz e falas transcritas de pessoa identificada. O dado sensível, do art. 5º, II, inclui o dado biométrico vinculado a pessoa natural. É controverso se toda gravação de voz é sensível, pois a lei não define dado biométrico.

O controlador decide sobre o tratamento (art. 5º, VI), o operador trata em nome dele (VII) e o encarregado é canal de comunicação (VIII), sem decidir finalidades. Transcrever e sumarizar são tratamento. O operador que usa o áudio para finalidade própria extrapola as instruções e responde solidariamente (art. 42, § 1º, I).

O dado anonimizado não é dado pessoal (art. 12, caput), salvo se o processo for revertido exclusivamente com meios próprios ou for reversível com esforços razoáveis. Pseudonimizar não é, por si, anonimizar: a definição do art. 13, § 4º, vale só para esse artigo, e, se o próprio controlador reverte com a informação que guarda, o dado continua pessoal.

O consentimento não é a única base legal (art. 7º). A dispensa para dado tornado manifestamente público pelo titular não afasta os direitos do titular nem os princípios (art. 7º, § 4º). A LGPD se aplica ao poder público, cujo tratamento deve atender à finalidade pública (art. 23).

O titular pode solicitar revisão de decisão tomada unicamente com base em tratamento automatizado que afete seus interesses (art. 20). O texto vigente não exige revisão por pessoa natural; a Lei 13.853/2019 suprimiu essa exigência da redação original.

A Lei 15.352/2026 criou a ANPD, autarquia vinculada ao Ministério da Justiça e Segurança Pública, e a autoridade nacional passou a ser exercida por ela; a redação de órgão da Presidência está superada. A multa não consta das sanções aplicáveis a órgãos públicos (art. 52, § 3º).

## Tópico P2-4.2 — Direitos autorais e ética no uso de IA para conteúdo gerado

### Resumo do tópico

São protegidas as criações do espírito fixadas em qualquer suporte, entre elas conferências e alocuções (art. 7º, II), e a proteção independe de registro (art. 18). Não são protegidos ideias e métodos como tais, textos de leis e demais atos oficiais, informações de uso comum e nomes ou títulos isolados (art. 8º).

Os direitos morais, como reivindicar a autoria e assegurar a integridade (art. 24), são inalienáveis e irrenunciáveis (art. 27), e a cessão total não os compreende (art. 49, I). Os patrimoniais dependem de autorização prévia e expressa para reprodução, adaptação e inclusão em base de dados (arts. 28 e 29).

Estar disponível na internet não é estar em domínio público, que ocorre setenta anos contados de 1º de janeiro do ano seguinte ao falecimento (art. 41), além das hipóteses do art. 45.

Entre as limitações do art. 46 estão a citação para estudo, crítica ou polêmica, na medida justificada e com indicação do autor e da origem (III); citação não é reprodução integral livre.

Há pontos controversos, sem texto legal expresso nem jurisprudência firmada, e nenhum se afirma como certo: se o conteúdo gerado por IA é obra protegida, se o treinamento com obras protegidas é reprodução ilícita ou se cabe em limitação, e se o pronunciamento parlamentar é alocução protegida (art. 7º, II) ou ato oficial (art. 8º, IV). O art. 46, I, b, é só indício legal de que discursos são matéria autoral.

No campo ético, os conceitos estáveis são transparência sobre o uso de IA, responsabilidade humana pelo texto publicado, revisão humana, rastreabilidade das fontes e não atribuir a ninguém palavras que não disse.

## Tópico P2-4.3 — Segurança da informação em pipelines de áudio e transcrição

### Resumo do tópico

A segurança da informação protege a confidencialidade, a integridade e a disponibilidade: só quem pode acessa, o dado não é alterado sem autorização e está acessível quando necessário.

No pipeline, a captação exige autenticidade da fonte, por causa do áudio sintético; a transmissão, criptografia em trânsito; o armazenamento, criptografia em repouso e gestão de chaves; a revisão e publicação, privilégio mínimo, registro e trilha de auditoria; e a retenção, prazo definido e eliminação do áudio bruto quando cessar a finalidade, salvo conservação autorizada (arts. 15 e 16). Cifrar o áudio não dispensa acesso restrito, registro e retenção.

No processamento, é preciso verificar no contrato, sem presumir, quem é o fornecedor, onde processa, se há subcontratados e se usa os dados do cliente para outro fim. Enviar áudio a serviço externo implica perda de custódia, e enviar áudio de pessoas identificadas a servidores no exterior pode configurar transferência internacional, permitida só nos casos do art. 33.

Há riscos próprios de IA. Na injeção de instruções, o texto transcrito ou recuperado traz comandos maliciosos que manipulam o LLM, e por isso o conteúdo transcrito é dado, não instrução. Embeddings não se presumem anônimos. Sem controle de integridade, a transcrição pode ser alterada sem rastro.

A LGPD impõe medidas de segurança técnicas e administrativas desde a concepção do serviço (art. 46, caput e § 2º), e o dever persiste após o término do tratamento (art. 47). Em incidente que possa acarretar risco ou dano relevante, quem comunica a autoridade nacional e o titular é o controlador (art. 48).
