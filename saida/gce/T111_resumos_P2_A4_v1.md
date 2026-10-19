# T111_resumos_P2_A4_v1.md — T-111 parte A4 (P2-3.1 a 3.4 e P2-4.1 a 4.3) — produção gce-cpp — 2026-10-18

**Base.** Pacote v1.11 (`saida/pacote/pacote.json`). Fonte única: curso do próprio tópico, `lotes[].curso` do L3 segmentado por `## ` (L3#0 a L3#6, tópicos 3.1 a 4.3). Regra de tamanho e forma: seção 2.1 da D1 da GCE (120 a 300 palavras e até 50% do curso; 3 a 6 parágrafos de 25 a 80 palavras; texto corrido, sem lista, markdown, título nem URL; nenhum parágrafo começa por algarismo ou por maiúsculas seguidas de dois-pontos). Contagem por script (palavras separadas por espaço). Nenhum fato fora do bloco: as datas de verificação e as URLs do bloco foram omitidas por serem referência de produção; as ressalvas do bloco (pontos controversos, redação superada, limite do Ato da Mesa) foram mantidas.

## Contagens por tópico

| Tópico | Curso (palavras) | Teto efetivo | Resumo (palavras) | Parágrafos | Palavras por parágrafo |
|---|--:|--:|--:|--:|---|
| P2-3.1 | 536 | 268 | 266 | 5 | 69, 59, 48, 41, 49 |
| P2-3.2 | 318 | 159 | 149 | 4 | 48, 25, 34, 42 |
| P2-3.3 | 310 | 155 | 147 | 4 | 47, 32, 39, 29 |
| P2-3.4 | 376 | 188 | 173 | 4 | 42, 46, 41, 44 |
| P2-4.1 | 1207 | 300 | 298 | 6 | 62, 53, 54, 45, 37, 47 |
| P2-4.2 | 709 | 300 | 269 | 6 | 52, 50, 32, 32, 71, 32 |
| P2-4.3 | 625 | 300 | 240 | 5 | 28, 62, 58, 41, 51 |

Conferência: os 7 resumos cumprem mínimo de 120, teto efetivo, 3 a 6 parágrafos de 25 a 80 palavras, sem início em algarismo ou em maiúsculas com dois-pontos, sem lista, markdown, título ou URL.

## P2-3.1

**Contagens.** Curso 536 palavras; teto efetivo 268; resumo 266 palavras; 5 parágrafos (69, 59, 48, 41, 49).

**Resumo.**

A IA em parlamentos se organiza em quatro famílias de aplicação sobre o acervo de sessões e reuniões. A transcrição converte fala em texto e é a base das demais. A sumarização condensa o conteúdo, de modo extrativo, que seleciona e copia trechos, ou abstrativo, que redige frases novas, como fazem os LLMs. A indexação associa metadados, como tema, orador, proposição e órgão. A busca localiza documentos ou trechos.

As etapas são encadeadas: a saída de uma é a entrada da seguinte. Um erro de transcrição, como nome trocado ou "não" omitido, se propaga para o resumo, o índice e a busca, e o produto final parece mais confiável do que é. Se a transcrição trocar o número da proposição, o índice associa a fala à proposição errada.

Os benefícios usuais são rapidez, acessibilidade, memória institucional e ganho de escala. Os riscos usuais são erro e texto fluente porém falso, viés, perda de fidelidade, exposição de dados pessoais, opacidade e dependência de fornecedor. A IA apoia, e o que vira registro oficial passa por revisão humana.

Sumarização não é transcrição menor, pois o resumo condensa e reformula e a transcrição reproduz. A IA também não decide sozinha o que é relevante: critérios, tesauro e avaliação são definidos pela instituição, e acervo público não dispensa supervisão e avaliação.

O Ato da Mesa nº 225/2025 fixa diretrizes gerais de governança de IA na Câmara, como supervisão humana (art. 3º, I) e conformidade com a LGPD (art. 3º, III). Seu texto não trata de transcrição, taquigrafia nem registro de sessões, e não se pode afirmar que regule esses sistemas.

**Relatório por parágrafo (ideia | frase do bloco).**

1. Quatro famílias de aplicação | "Quatro famílias de aplicação sobre o acervo de sessões e reuniões"; "EXTRATIVA (seleciona e copia trechos...)" / "ABSTRATIVA (redige frases novas...)"
2. Encadeamento e propagação de erros | "Encadeamento: a saída de uma etapa é a entrada da seguinte."; "Se a transcrição trocou o número da proposição, o índice associa a fala à proposição errada."
3. Benefícios, riscos e princípio de uso | "Benefícios usuais: rapidez, acessibilidade (legendas), memória institucional, ganho de escala."; "a IA APOIA; o que vira registro oficial passa por revisão humana"
4. Sumarização não é transcrição; critérios humanos | "Tratar sumarização como 'transcrição menor' (resumo condensa e reformula; transcrição reproduz)."; "critérios, tesauro e avaliação são definidos pela instituição"
5. Ato da Mesa 225/2025 e seu limite | "o art. 3º fixa diretrizes mínimas, entre elas ... supervisão humana: I ... observância da LGPD (III)"; "O texto lido NÃO trata de transcrição, taquigrafia, reconhecimento de fala nem registro de sessões"

## P2-3.2

**Contagens.** Curso 318 palavras; teto efetivo 159; resumo 149 palavras; 4 parágrafos (48, 25, 34, 42).

**Resumo.**

A busca lexical recupera documentos que contêm os termos da consulta e falha quando a palavra do usuário não é a do documento. A busca semântica converte consulta e trechos em embeddings, vetores numéricos, e devolve os trechos de sentido mais próximo, medido por similaridade como o cosseno.

Os passos típicos são dividir os documentos em trechos, gerar embeddings, guardar em índice vetorial, embutir a consulta, recuperar os mais próximos e, opcionalmente, reordenar.

A busca híbrida combina as duas, porque termos exatos, como o número de uma proposição, pedem a busca lexical, e a semelhança de sentido atende outra necessidade. A semântica nem sempre é mais precisa.

A geração com recuperação (RAG) tem limites: pede a um LLM que responda com base nos trechos recuperados, mas só reduz, não elimina, a resposta inventada, e a proximidade não prova que o texto afirma algo. A avaliação usa precisão e revocação.

**Relatório por parágrafo (ideia | frase do bloco).**

1. Busca lexical x busca semântica | "Busca por palavras-chave (lexical): recupera documentos que contêm os termos da consulta"; "(EMBEDDINGS) ... medida de similaridade, como o cosseno"
2. Passos típicos da busca semântica | "Passos típicos: dividir os documentos em trechos (chunking) → gerar embeddings → guardar em índice vetorial → embutir a consulta → recuperar os mais próximos → opcionalmente reordenar (reranking)."
3. Busca híbrida e número exato | "Busca híbrida: combina as duas, porque termos exatos (número de proposição, nome próprio, sigla) e semelhança de sentido atendem a necessidades diferentes."; "Semântica sempre mais precisa que a lexical (para nome e número exato, não é)."
4. RAG, limites e avaliação | "Reduz, mas NÃO elimina, resposta inventada."; "resultado por proximidade, não prova de que o texto 'afirma' algo"; "Avaliação: precisão ... e revocação"

## P2-3.3

**Contagens.** Curso 310 palavras; teto efetivo 155; resumo 147 palavras; 4 parágrafos (47, 32, 39, 29).

**Resumo.**

Ata é o documento formal que registra o ocorrido na reunião, com presenças, pauta, deliberações, votações e encaminhamentos. Resumo é a condensação informativa do conteúdo. Sobre o regime jurídico da ata na Câmara, vale só o princípio: documento que pode produzir efeitos exige conferência e responsável humano.

O fluxo típico parte de transcrição verificada, segmenta por item de pauta, extrai campos estruturados, gera o texto em geral de forma abstrativa com modelo fixo e termina em revisão humana obrigatória.

Os riscos específicos são omissão e inversão, como "aprovado" por "rejeitado", atribuição errada de fala ou voto, números e nomes trocados e fluência enganosa. Alucinação é conteúdo não sustentado pela fonte; a frase ser nova não é o problema.

A mitigação separa campos factuais, extraídos, da narrativa gerada, exige citação do trecho-fonte e mantém revisão humana. Métricas de sobreposição, como ROUGE, medem semelhança de texto, não fidelidade factual.

**Relatório por parágrafo (ideia | frase do bloco).**

1. Ata, resumo e princípio humano | "Ata: documento formal que registra o ocorrido numa reunião"; "o curso trata só do princípio: documento que pode produzir efeitos exige conferência e responsável humano"
2. Fluxo da geração automática | "Fluxo típico de geração automática: 1. Transcrição verificada ... 5. Revisão humana obrigatória."
3. Riscos específicos e alucinação | "Omissão e inversão: 'aprovado' × 'rejeitado'"; "Alucinação: conteúdo NÃO SUSTENTADO pela fonte. O problema não é a frase ser nova ... mas ter informação que a transcrição não contém."
4. Mitigação e métricas | "separar campos factuais (extração) de narrativa (geração); exigir citação do trecho-fonte"; "ROUGE ... medem semelhança de texto, não fidelidade factual"

## P2-3.4

**Contagens.** Curso 376 palavras; teto efetivo 188; resumo 173 palavras; 4 parágrafos (42, 46, 41, 44).

**Resumo.**

O modelo multilíngue é um único modelo treinado com dados de vários idiomas. Seu desempenho varia por idioma, em geral melhor nos de mais dados. O tokenizador pode fragmentar mais as palavras de idiomas sub-representados, o que aumenta tokens, custo e latência.

O modelo especializado em português é treinado ou ajustado com corpora em português, para captar vocabulário e variedades do pt-BR. Pode ser treinado do zero ou adaptado de um multilíngue, sem exclusividade de idioma. Pode ganhar em expressões locais e termos regimentais, mas pode perder generalidade.

Um modelo de domínio legislativo se obtém por ajuste fino, por recuperação de documentos oficiais (RAG) ou por instruções, sem treinar do zero. Como o modelo não conhece normas posteriores ao treino, a recuperação de fontes oficiais atualizadas é prática comum.

O ASR multilíngue e o LLM multilíngue são componentes distintos: ser multilíngue num não garante no outro. A avaliação deve usar dados em português do domínio de uso. Nomes de modelos mudam em meses, e a banca pode cobrar o conceito, não o produto.

**Relatório por parágrafo (ideia | frase do bloco).**

1. Modelo multilíngue e tokenização | "Modelo multilíngue: um único modelo treinado com dados de vários idiomas"; "o tokenizador pode fragmentar mais as palavras de idiomas sub-representados, o que aumenta tokens, custo e latência"
2. Modelo especializado em português | "'Especializado' pode significar treinado do zero em português OU adaptado de um modelo multilíngue; não implica exclusividade de idioma."; "Limites: pode perder generalidade"
3. Modelo de domínio e vigência | "Modelo de domínio (legislativo): obtém-se por ajuste fino ..., por recuperação de documentos oficiais (RAG, 3.2) ou por instruções (prompts); não exige treinar do zero."; "modelo treinado em data passada não conhece normas novas"
4. ASR x LLM, avaliação e nomes | "o ASR multilíngue ... e o LLM multilíngue são componentes distintos"; "testar em tarefas e dados em português do domínio de uso"; "A banca pode cobrar o CONCEITO, e não o nome do produto."

## P2-4.1

**Contagens.** Curso 1207 palavras; teto efetivo 300; resumo 298 palavras; 6 parágrafos (62, 53, 54, 45, 37, 47).

**Resumo.**

Dado pessoal é a informação relacionada a pessoa natural identificada ou identificável (art. 5º, I), inclusive a gravação da voz e as falas transcritas de pessoa identificada. O dado sensível é o do art. 5º, II, que inclui o dado biométrico vinculado a pessoa natural. Se toda gravação de voz é sensível depende de interpretação, pois a lei não define dado biométrico.

O controlador decide sobre o tratamento (art. 5º, VI), o operador trata em nome dele (VII) e o encarregado é o canal de comunicação, sem decidir finalidades (VIII). Transcrever e sumarizar são tratamento. Se o fornecedor usa o áudio para finalidade própria, extrapola as instruções e responde solidariamente (art. 42, § 1º, I).

O dado anonimizado não é dado pessoal (art. 12, caput), salvo se o processo for revertido exclusivamente com meios próprios ou for reversível com esforços razoáveis. Pseudonimizar não é, por si, anonimizar: a definição do art. 13, § 4º, tem alcance restrito, e, se o controlador reverte com a tabela, o dado continua pessoal.

O consentimento não é a única base de tratamento (art. 7º). A dispensa para dado manifestamente público não afasta os direitos do titular nem os princípios (art. 7º, § 4º). A LGPD se aplica ao poder público, que trata dados para finalidade pública (art. 23).

Na decisão automatizada, o titular pode solicitar revisão (art. 20). O texto vigente não diz que a revisão seja feita por pessoa natural, exigência da redação original suprimida pela Lei 13.853/2019; citar a redação superada é erro.

A Lei 15.352/2026 criou a ANPD, autarquia vinculada ao Ministério da Justiça e Segurança Pública, e a autoridade nacional passou a ser exercida por ela; a redação de órgão da Presidência está superada. A multa não consta das sanções aplicáveis a órgãos públicos (art. 52, § 3º).

**Relatório por parágrafo (ideia | frase do bloco).**

1. Dado pessoal e dado sensível | "Dado pessoal: informação relacionada a pessoa natural identificada ou identificável (art. 5º, I)."; "a lei não define 'dado biométrico'; se toda gravação de voz ... é dado sensível depende de interpretação"
2. Controlador, operador, encarregado | "controlador (VI: a quem competem as DECISÕES sobre o tratamento), operador (VII: realiza o tratamento EM NOME do controlador), encarregado (VIII: canal de comunicação ...)"; "Transcrever e sumarizar são tratamento."; art. 42, § 1º, I
3. Anonimização e pseudonimização | "O dado anonimizado não é dado pessoal (art. 12, caput), SALVO se o processo for revertido utilizando exclusivamente meios próprios ou se a reversão for possível com esforços razoáveis"; "Pseudonimizar NÃO é, por si, anonimizar."
4. Bases de tratamento e poder público | "O consentimento NÃO é a única base."; "a dispensa de consentimento para dados manifestamente públicos pelo titular não afasta os direitos do titular nem os princípios (art. 7º, § 4º)"; "A LGPD SE APLICA ao poder público."
5. Decisões automatizadas e redação superada | "O texto vigente NÃO diz que a revisão seja feita por pessoa natural"; "Cuidado com a redação superada."
6. ANPD, Lei 15.352/2026 e sanções | "A Lei 15.352/2026 CRIA a Agência Nacional de Proteção de Dados (ANPD), autarquia ... vinculada ao Ministério da Justiça e Segurança Pública"; "A autoridade nacional não 'é' a Agência por definição; passou a ser exercida por ela."; "a multa (incisos II e III) não consta dessa lista"

## P2-4.2

**Contagens.** Curso 709 palavras; teto efetivo 300; resumo 269 palavras; 6 parágrafos (52, 50, 32, 32, 71, 32).

**Resumo.**

São protegidas as criações do espírito fixadas em qualquer suporte, entre elas conferências e alocuções (art. 7º, II), e a proteção independe de registro (art. 18). Não são protegidos ideias e métodos como tais, textos de leis e demais atos oficiais, informações de uso comum e nomes ou títulos isolados (art. 8º).

Os direitos morais, como reivindicar a autoria e assegurar a integridade (art. 24), são inalienáveis e irrenunciáveis (art. 27), e a cessão total não os compreende (art. 49, I). Os patrimoniais dependem de autorização prévia e expressa para reprodução, adaptação e inclusão em base de dados (arts. 28 e 29).

Estar disponível na internet não é estar em domínio público, que ocorre setenta anos contados de 1º de janeiro do ano seguinte ao falecimento (art. 41), além das hipóteses do art. 45.

Entre as limitações do art. 46 estão a citação para estudo, crítica ou polêmica, na medida justificada e com indicação do autor e da origem (III); citação não é reprodução integral livre.

Há pontos controversos, sem texto legal expresso nem jurisprudência firmada, e nenhum se afirma como certo: se o conteúdo gerado por IA é obra protegida, se o treinamento com obras protegidas é reprodução ilícita ou se cabe em limitação, e se o pronunciamento parlamentar é alocução protegida (art. 7º, II) ou ato oficial (art. 8º, IV). O art. 46, I, b, é só indício legal de que discursos são matéria autoral.

No campo ético, os conceitos estáveis são transparência sobre o uso de IA, responsabilidade humana pelo texto publicado, revisão humana, rastreabilidade das fontes e não atribuir a ninguém palavras que não disse.

**Relatório por parágrafo (ideia | frase do bloco).**

1. Obras protegidas e não protegidas | "Obras protegidas (art. 7º): ... as conferências, alocuções, sermões"; "A proteção independe de registro (art. 18)."; "Não protegidos (art. 8º): ideias e métodos como tais (I); textos de tratados, leis ... e demais atos oficiais (IV)"
2. Direitos morais e patrimoniais | "São inalienáveis e irrenunciáveis (art. 27); a cessão total não os compreende (art. 49, I)."; "dependem de autorização prévia e expressa do autor a reprodução (I), a adaptação ... (III) e a inclusão em base de dados ... (IX)"
3. Domínio público | "Domínio público: setenta anos contados de 1º de janeiro do ano seguinte ao falecimento (art. 41) e as demais hipóteses do art. 45. Estar disponível na internet NÃO é estar em domínio público."
4. Limitação da citação (art. 46, III) | "citação para estudo, crítica ou polêmica, na medida justificada e com indicação do autor e da origem (III)"; "Confundir citação (art. 46, III) com reprodução integral livre."
5. Pontos controversos | "Pontos controversos (não há texto legal expresso nem jurisprudência firmada que se possa afirmar)" (a, b, f); "INDÍCIO legal, e não enquadramento definitivo"
6. Ética: conceitos estáveis | "ÉTICA (conceitos estáveis, sem norma específica verificada): transparência sobre o uso de IA; responsabilidade humana pelo texto publicado; revisão humana; não atribuir a ninguém palavras que não disse; rastreabilidade das fontes"

## P2-4.3

**Contagens.** Curso 625 palavras; teto efetivo 300; resumo 240 palavras; 5 parágrafos (28, 62, 58, 41, 51).

**Resumo.**

A segurança da informação protege a confidencialidade, a integridade e a disponibilidade: só quem pode acessa, o dado não é alterado sem autorização e está acessível quando necessário.

No pipeline, a captação exige autenticidade da fonte, por causa do áudio sintético; a transmissão, criptografia em trânsito; o armazenamento, criptografia em repouso e gestão de chaves; a revisão e publicação, privilégio mínimo, registro e trilha de auditoria; e a retenção, prazo definido e eliminação do áudio bruto quando cessar a finalidade. Cifrar o áudio não dispensa acesso restrito, registro e retenção.

No processamento, é preciso verificar no contrato, sem presumir, quem é o fornecedor, onde processa, se há subcontratados e se usa os dados do cliente para outro fim. Enviar áudio a serviço externo implica perda de custódia, e enviar áudio de pessoas identificadas a servidores no exterior pode configurar transferência internacional, permitida só nos casos do art. 33.

Há riscos próprios de IA. Na injeção de instruções, o texto transcrito traz comandos maliciosos, e por isso o conteúdo transcrito é dado, não instrução. Embeddings não se presumem anônimos. Sem controle de integridade, a transcrição pode ser alterada sem rastro.

A LGPD impõe medidas de segurança técnicas e administrativas desde a concepção do serviço (art. 46, caput e § 2º), e o dever persiste após o término do tratamento (art. 47). Em incidente com risco ou dano relevante, quem comunica a autoridade nacional e o titular é o controlador (art. 48).

**Relatório por parágrafo (ideia | frase do bloco).**

1. Três propriedades | "confidencialidade (só quem pode acessa), integridade (o dado não é alterado sem autorização) e disponibilidade (está acessível quando necessário)"
2. Pontos de ação no pipeline | "Pipeline típico, e onde agir:" itens 1, 2, 3, 5 e 6; "Cifrar o áudio resolve toda a segurança (e acesso, registro, retenção? não dispensa)"
3. Processamento por terceiros e transferência | "quem é o fornecedor, onde processa, se há subcontratados, se usa os dados do cliente para outro fim (verificar no contrato; não presumir)"; "Enviar áudio de pessoas identificadas a serviço com servidores no exterior pode configurar transferência internacional."
4. Riscos específicos de IA | "tratar conteúdo transcrito como dado, não como instrução"; "Embeddings e vetores: não presumir que sejam anônimos"; "a transcrição pode ser alterada sem rastro"
5. Dispositivos da LGPD sobre segurança | "Dever de adotar medidas de segurança técnicas e administrativas ... (art. 46, caput), observadas desde a concepção ... (art. 46, § 2º)"; "O dever de segurança persiste mesmo após o término do tratamento (art. 47)"; "o controlador comunica a autoridade nacional e o titular ... (art. 48)"

## Bloco JSON

```json
{
 "topicos": {
  "P2-3.1": {
   "resumo": "A IA em parlamentos se organiza em quatro famílias de aplicação sobre o acervo de sessões e reuniões. A transcrição converte fala em texto e é a base das demais. A sumarização condensa o conteúdo, de modo extrativo, que seleciona e copia trechos, ou abstrativo, que redige frases novas, como fazem os LLMs. A indexação associa metadados, como tema, orador, proposição e órgão. A busca localiza documentos ou trechos.\n\nAs etapas são encadeadas: a saída de uma é a entrada da seguinte. Um erro de transcrição, como nome trocado ou \"não\" omitido, se propaga para o resumo, o índice e a busca, e o produto final parece mais confiável do que é. Se a transcrição trocar o número da proposição, o índice associa a fala à proposição errada.\n\nOs benefícios usuais são rapidez, acessibilidade, memória institucional e ganho de escala. Os riscos usuais são erro e texto fluente porém falso, viés, perda de fidelidade, exposição de dados pessoais, opacidade e dependência de fornecedor. A IA apoia, e o que vira registro oficial passa por revisão humana.\n\nSumarização não é transcrição menor, pois o resumo condensa e reformula e a transcrição reproduz. A IA também não decide sozinha o que é relevante: critérios, tesauro e avaliação são definidos pela instituição, e acervo público não dispensa supervisão e avaliação.\n\nO Ato da Mesa nº 225/2025 fixa diretrizes gerais de governança de IA na Câmara, como supervisão humana (art. 3º, I) e conformidade com a LGPD (art. 3º, III). Seu texto não trata de transcrição, taquigrafia nem registro de sessões, e não se pode afirmar que regule esses sistemas."
  },
  "P2-3.2": {
   "resumo": "A busca lexical recupera documentos que contêm os termos da consulta e falha quando a palavra do usuário não é a do documento. A busca semântica converte consulta e trechos em embeddings, vetores numéricos, e devolve os trechos de sentido mais próximo, medido por similaridade como o cosseno.\n\nOs passos típicos são dividir os documentos em trechos, gerar embeddings, guardar em índice vetorial, embutir a consulta, recuperar os mais próximos e, opcionalmente, reordenar.\n\nA busca híbrida combina as duas, porque termos exatos, como o número de uma proposição, pedem a busca lexical, e a semelhança de sentido atende outra necessidade. A semântica nem sempre é mais precisa.\n\nA geração com recuperação (RAG) tem limites: pede a um LLM que responda com base nos trechos recuperados, mas só reduz, não elimina, a resposta inventada, e a proximidade não prova que o texto afirma algo. A avaliação usa precisão e revocação."
  },
  "P2-3.3": {
   "resumo": "Ata é o documento formal que registra o ocorrido na reunião, com presenças, pauta, deliberações, votações e encaminhamentos. Resumo é a condensação informativa do conteúdo. Sobre o regime jurídico da ata na Câmara, vale só o princípio: documento que pode produzir efeitos exige conferência e responsável humano.\n\nO fluxo típico parte de transcrição verificada, segmenta por item de pauta, extrai campos estruturados, gera o texto em geral de forma abstrativa com modelo fixo e termina em revisão humana obrigatória.\n\nOs riscos específicos são omissão e inversão, como \"aprovado\" por \"rejeitado\", atribuição errada de fala ou voto, números e nomes trocados e fluência enganosa. Alucinação é conteúdo não sustentado pela fonte; a frase ser nova não é o problema.\n\nA mitigação separa campos factuais, extraídos, da narrativa gerada, exige citação do trecho-fonte e mantém revisão humana. Métricas de sobreposição, como ROUGE, medem semelhança de texto, não fidelidade factual."
  },
  "P2-3.4": {
   "resumo": "O modelo multilíngue é um único modelo treinado com dados de vários idiomas. Seu desempenho varia por idioma, em geral melhor nos de mais dados. O tokenizador pode fragmentar mais as palavras de idiomas sub-representados, o que aumenta tokens, custo e latência.\n\nO modelo especializado em português é treinado ou ajustado com corpora em português, para captar vocabulário e variedades do pt-BR. Pode ser treinado do zero ou adaptado de um multilíngue, sem exclusividade de idioma. Pode ganhar em expressões locais e termos regimentais, mas pode perder generalidade.\n\nUm modelo de domínio legislativo se obtém por ajuste fino, por recuperação de documentos oficiais (RAG) ou por instruções, sem treinar do zero. Como o modelo não conhece normas posteriores ao treino, a recuperação de fontes oficiais atualizadas é prática comum.\n\nO ASR multilíngue e o LLM multilíngue são componentes distintos: ser multilíngue num não garante no outro. A avaliação deve usar dados em português do domínio de uso. Nomes de modelos mudam em meses, e a banca pode cobrar o conceito, não o produto."
  },
  "P2-4.1": {
   "resumo": "Dado pessoal é a informação relacionada a pessoa natural identificada ou identificável (art. 5º, I), inclusive a gravação da voz e as falas transcritas de pessoa identificada. O dado sensível é o do art. 5º, II, que inclui o dado biométrico vinculado a pessoa natural. Se toda gravação de voz é sensível depende de interpretação, pois a lei não define dado biométrico.\n\nO controlador decide sobre o tratamento (art. 5º, VI), o operador trata em nome dele (VII) e o encarregado é o canal de comunicação, sem decidir finalidades (VIII). Transcrever e sumarizar são tratamento. Se o fornecedor usa o áudio para finalidade própria, extrapola as instruções e responde solidariamente (art. 42, § 1º, I).\n\nO dado anonimizado não é dado pessoal (art. 12, caput), salvo se o processo for revertido exclusivamente com meios próprios ou for reversível com esforços razoáveis. Pseudonimizar não é, por si, anonimizar: a definição do art. 13, § 4º, tem alcance restrito, e, se o controlador reverte com a tabela, o dado continua pessoal.\n\nO consentimento não é a única base de tratamento (art. 7º). A dispensa para dado manifestamente público não afasta os direitos do titular nem os princípios (art. 7º, § 4º). A LGPD se aplica ao poder público, que trata dados para finalidade pública (art. 23).\n\nNa decisão automatizada, o titular pode solicitar revisão (art. 20). O texto vigente não diz que a revisão seja feita por pessoa natural, exigência da redação original suprimida pela Lei 13.853/2019; citar a redação superada é erro.\n\nA Lei 15.352/2026 criou a ANPD, autarquia vinculada ao Ministério da Justiça e Segurança Pública, e a autoridade nacional passou a ser exercida por ela; a redação de órgão da Presidência está superada. A multa não consta das sanções aplicáveis a órgãos públicos (art. 52, § 3º)."
  },
  "P2-4.2": {
   "resumo": "São protegidas as criações do espírito fixadas em qualquer suporte, entre elas conferências e alocuções (art. 7º, II), e a proteção independe de registro (art. 18). Não são protegidos ideias e métodos como tais, textos de leis e demais atos oficiais, informações de uso comum e nomes ou títulos isolados (art. 8º).\n\nOs direitos morais, como reivindicar a autoria e assegurar a integridade (art. 24), são inalienáveis e irrenunciáveis (art. 27), e a cessão total não os compreende (art. 49, I). Os patrimoniais dependem de autorização prévia e expressa para reprodução, adaptação e inclusão em base de dados (arts. 28 e 29).\n\nEstar disponível na internet não é estar em domínio público, que ocorre setenta anos contados de 1º de janeiro do ano seguinte ao falecimento (art. 41), além das hipóteses do art. 45.\n\nEntre as limitações do art. 46 estão a citação para estudo, crítica ou polêmica, na medida justificada e com indicação do autor e da origem (III); citação não é reprodução integral livre.\n\nHá pontos controversos, sem texto legal expresso nem jurisprudência firmada, e nenhum se afirma como certo: se o conteúdo gerado por IA é obra protegida, se o treinamento com obras protegidas é reprodução ilícita ou se cabe em limitação, e se o pronunciamento parlamentar é alocução protegida (art. 7º, II) ou ato oficial (art. 8º, IV). O art. 46, I, b, é só indício legal de que discursos são matéria autoral.\n\nNo campo ético, os conceitos estáveis são transparência sobre o uso de IA, responsabilidade humana pelo texto publicado, revisão humana, rastreabilidade das fontes e não atribuir a ninguém palavras que não disse."
  },
  "P2-4.3": {
   "resumo": "A segurança da informação protege a confidencialidade, a integridade e a disponibilidade: só quem pode acessa, o dado não é alterado sem autorização e está acessível quando necessário.\n\nNo pipeline, a captação exige autenticidade da fonte, por causa do áudio sintético; a transmissão, criptografia em trânsito; o armazenamento, criptografia em repouso e gestão de chaves; a revisão e publicação, privilégio mínimo, registro e trilha de auditoria; e a retenção, prazo definido e eliminação do áudio bruto quando cessar a finalidade. Cifrar o áudio não dispensa acesso restrito, registro e retenção.\n\nNo processamento, é preciso verificar no contrato, sem presumir, quem é o fornecedor, onde processa, se há subcontratados e se usa os dados do cliente para outro fim. Enviar áudio a serviço externo implica perda de custódia, e enviar áudio de pessoas identificadas a servidores no exterior pode configurar transferência internacional, permitida só nos casos do art. 33.\n\nHá riscos próprios de IA. Na injeção de instruções, o texto transcrito traz comandos maliciosos, e por isso o conteúdo transcrito é dado, não instrução. Embeddings não se presumem anônimos. Sem controle de integridade, a transcrição pode ser alterada sem rastro.\n\nA LGPD impõe medidas de segurança técnicas e administrativas desde a concepção do serviço (art. 46, caput e § 2º), e o dever persiste após o término do tratamento (art. 47). Em incidente com risco ou dano relevante, quem comunica a autoridade nacional e o titular é o controlador (art. 48)."
  }
 }
}
```

FIM DO ARQUIVO
