# T111_resumos_P2_A4_v2.md — T-111 parte A4 (P2-3.1 a 3.4 e P2-4.1 a 4.3), rodada de correção R1 — produção gce-cpp — 2026-10-18

**Base.** Pacote v1.11 (`saida/pacote/pacote.json`), SHA-256 1b5657c726b5852885fe0e69e7835d6ec331e6d43dd19191cf451ff4ac069517. Fonte única: curso do próprio tópico. Parecer: `saida/gce/QA_T111_A4_R1_2026-10-18_gce-cqfp.md` (seção 4, texto exato da v2). Regra de tamanho e forma: seção 2.1 da D1 da GCE.

## Resposta ao relatório de QA (item a item)

| Item | Resposta |
|---|---|
| 3.1-A (ressalva 'norma interna, fora dos objetos de avaliação') | acatado: reposta no P5. |
| 3.1-B (alcance 'os sistemas aqui descritos') | acatado. |
| 3.1-cortes de tamanho (5 cortes) | acatado: aplicados; 268/268. |
| 3.2-A (um parágrafo por ideia) | acatado: P4 = nem busca semântica nem RAG verificam fatos; P5 = avaliação. |
| 3.2-B (definir precisão e revocação) | acatado. |
| 3.2-corte (cosseno) | acatado: 159/159. |
| 3.3-A (regime jurídico da ata) | acatado: sem nota de processo. |
| 3.3-B ('modelo de estrutura fixo') | acatado. |
| 3.4-A (volatilidade de nomes em parágrafo próprio) | acatado: 5 parágrafos. |
| 4.1-A (art. 7º, § 4º, 'tornado ... pelo titular') | acatado. |
| 4.1-B (art. 20, requisitos do caput) | acatado. |
| 4.1-C (art. 23, dever) | acatado. |
| 4.1-D (art. 13, § 4º; informação que o controlador guarda) | acatado. |
| 4.1-E ('É controverso') | acatado. |
| 4.1-F ('O operador que usa...') | acatado. |
| 4.1-cortes (voz e falas; base legal; supressão da frase sobre redação superada) | acatado: 298/300. |
| 4.2 (APROVADO) | mantido igual à v1; 4.2-R1 é ressalva de curso, destinada à Gerência, sem alteração do resumo. |
| 4.3-A (salvo conservação autorizada, arts. 15 e 16) | acatado. |
| 4.3-B (injeção de instruções completa) | acatado. |
| 4.3-C (art. 48, 'que possa acarretar') | acatado. |

Nenhum item não acatado. Texto da v2 idêntico ao dado no parecer; contagens recalculadas por script.

## Contagens por tópico

| Tópico | Curso (palavras) | Teto efetivo | Resumo (palavras) | Parágrafos | Palavras por parágrafo |
|---|--:|--:|--:|--:|---|
| P2-3.1 | 536 | 268 | 268 | 5 | 68, 59, 47, 41, 53 |
| P2-3.2 | 318 | 159 | 159 | 5 | 42, 25, 34, 32, 26 |
| P2-3.3 | 310 | 155 | 151 | 4 | 49, 34, 39, 29 |
| P2-3.4 | 376 | 188 | 187 | 5 | 42, 46, 41, 28, 30 |
| P2-4.1 | 1207 | 300 | 298 | 6 | 54, 52, 59, 48, 38, 47 |
| P2-4.2 | 709 | 300 | 269 | 6 | 52, 50, 32, 32, 71, 32 |
| P2-4.3 | 625 | 300 | 255 | 5 | 28, 69, 58, 47, 53 |

Conferência: os 7 resumos cumprem mínimo de 120, teto efetivo, 3 a 6 parágrafos de 25 a 80 palavras, sem início em algarismo ou em maiúsculas com dois-pontos, sem lista, markdown, título ou URL.

## P2-3.1

**Contagens.** Curso 536 palavras; teto efetivo 268; resumo 268 palavras; 5 parágrafos (68, 59, 47, 41, 53).

**Resumo.**

A IA em parlamentos se organiza em quatro famílias de aplicação sobre o acervo de sessões e reuniões. A transcrição converte fala em texto e é a base das demais. A sumarização condensa o conteúdo, de modo extrativo, que seleciona e copia trechos, ou abstrativo, que redige frases novas, caso dos LLMs. A indexação associa metadados, como tema, orador, proposição e órgão. A busca localiza documentos ou trechos.

As etapas são encadeadas: a saída de uma é a entrada da seguinte. Um erro de transcrição, como nome trocado ou "não" omitido, se propaga para o resumo, o índice e a busca, e o produto final parece mais confiável do que é. Se a transcrição trocar o número da proposição, o índice associa a fala à proposição errada.

Os benefícios usuais são rapidez, acessibilidade, memória institucional e ganho de escala. Os riscos são erro e texto fluente porém falso, viés, perda de fidelidade, exposição de dados pessoais, opacidade e dependência de fornecedor. A IA apoia, e o que vira registro oficial passa por revisão humana.

Sumarização não é transcrição menor, pois o resumo condensa e reformula e a transcrição reproduz. A IA também não decide sozinha o que é relevante: critérios, tesauro e avaliação são definidos pela instituição, e acervo público não dispensa supervisão e avaliação.

O Ato da Mesa nº 225/2025, norma interna fora dos objetos de avaliação, fixa diretrizes de governança de IA na Câmara, como supervisão humana (art. 3º, I) e conformidade com a LGPD (III). Não trata de transcrição, taquigrafia nem registro de sessões, e não se pode afirmar que regule os sistemas aqui descritos.

**Relatório por parágrafo (ideia | frase do bloco).**

1. Quatro famílias de aplicação | "Quatro famílias de aplicação sobre o acervo de sessões e reuniões"; "EXTRATIVA (seleciona e copia trechos...)" / "ABSTRATIVA (redige frases novas...)"
2. Encadeamento e propagação de erros | "Encadeamento: a saída de uma etapa é a entrada da seguinte."; "Se a transcrição trocou o número da proposição, o índice associa a fala à proposição errada."
3. Benefícios, riscos e princípio de uso | "Benefícios usuais: rapidez, acessibilidade (legendas), memória institucional, ganho de escala."; "a IA APOIA; o que vira registro oficial passa por revisão humana"
4. Sumarização não é transcrição; critérios humanos | "Tratar sumarização como 'transcrição menor' (resumo condensa e reformula; transcrição reproduz)."; "critérios, tesauro e avaliação são definidos pela instituição"
5. Ato da Mesa 225/2025 e seu limite | "Norma interna, fora dos objetos de avaliação"; "o art. 3º fixa diretrizes mínimas ... supervisão humana: I ... observância da LGPD (III)"; "O texto lido NÃO trata de transcrição, taquigrafia, reconhecimento de fala nem registro de sessões" (alcance: os sistemas descritos no tópico)

## P2-3.2

**Contagens.** Curso 318 palavras; teto efetivo 159; resumo 159 palavras; 5 parágrafos (42, 25, 34, 32, 26).

**Resumo.**

A busca lexical recupera documentos que contêm os termos da consulta e falha quando a palavra do usuário não é a do documento. A busca semântica converte consulta e trechos em embeddings, vetores numéricos, e devolve os trechos de sentido mais próximo.

Os passos típicos são dividir os documentos em trechos, gerar embeddings, guardar em índice vetorial, embutir a consulta, recuperar os mais próximos e, opcionalmente, reordenar.

A busca híbrida combina as duas, porque termos exatos, como o número de uma proposição, pedem a busca lexical, e a semelhança de sentido atende outra necessidade. A semântica nem sempre é mais precisa.

Nem a busca semântica nem o RAG, geração com recuperação, verificam fatos. O RAG pede ao LLM que responda com base nos trechos recuperados e reduz, mas não elimina, a resposta inventada.

A avaliação da busca usa duas medidas: a precisão, que mede quanto do recuperado é relevante, e a revocação, que mede quanto do relevante foi recuperado.

**Relatório por parágrafo (ideia | frase do bloco).**

1. Busca lexical x busca semântica | "Busca por palavras-chave (lexical): recupera documentos que contêm os termos da consulta"; "(EMBEDDINGS) ..."
2. Passos típicos da busca semântica | "Passos típicos: dividir os documentos em trechos (chunking) → ... → opcionalmente reordenar (reranking)."
3. Busca híbrida e número exato | "Busca híbrida: combina as duas ..."; "Semântica sempre mais precisa que a lexical (para nome e número exato, não é)."
4. Nem a busca semântica nem o RAG verificam fatos | "Reduz, mas NÃO elimina, resposta inventada."; "resultado por proximidade, não prova de que o texto 'afirma' algo"
5. Avaliação: precisão e revocação | "Avaliação: precisão ... e revocação" (definições das duas, como no bloco)

## P2-3.3

**Contagens.** Curso 310 palavras; teto efetivo 155; resumo 151 palavras; 4 parágrafos (49, 34, 39, 29).

**Resumo.**

Ata é o documento formal que registra o ocorrido na reunião, com presenças, pauta, deliberações, votações e encaminhamentos. Resumo é a condensação informativa do conteúdo. O regime jurídico da ata na Câmara não é tratado aqui; fica o princípio: documento que pode produzir efeitos exige conferência e responsável humano.

O fluxo típico parte de transcrição verificada, segmenta por item de pauta, extrai campos estruturados, gera o texto em geral de forma abstrativa com modelo de estrutura fixo e termina em revisão humana obrigatória.

Os riscos específicos são omissão e inversão, como "aprovado" por "rejeitado", atribuição errada de fala ou voto, números e nomes trocados e fluência enganosa. Alucinação é conteúdo não sustentado pela fonte; a frase ser nova não é o problema.

A mitigação separa campos factuais, extraídos, da narrativa gerada, exige citação do trecho-fonte e mantém revisão humana. Métricas de sobreposição, como ROUGE, medem semelhança de texto, não fidelidade factual.

**Relatório por parágrafo (ideia | frase do bloco).**

1. Ata, resumo e princípio humano | "Ata: documento formal que registra o ocorrido numa reunião"; "o curso trata só do princípio: documento que pode produzir efeitos exige conferência e responsável humano"
2. Fluxo da geração automática | "Fluxo típico de geração automática: 1. Transcrição verificada ... 5. Revisão humana obrigatória."; modelo de estrutura fixo (template)
3. Riscos específicos e alucinação | "Omissão e inversão: 'aprovado' × 'rejeitado'"; "Alucinação: conteúdo NÃO SUSTENTADO pela fonte."
4. Mitigação e métricas | "separar campos factuais (extração) de narrativa (geração); exigir citação do trecho-fonte"; "ROUGE ... medem semelhança de texto, não fidelidade factual"

## P2-3.4

**Contagens.** Curso 376 palavras; teto efetivo 188; resumo 187 palavras; 5 parágrafos (42, 46, 41, 28, 30).

**Resumo.**

O modelo multilíngue é um único modelo treinado com dados de vários idiomas. Seu desempenho varia por idioma, em geral melhor nos de mais dados. O tokenizador pode fragmentar mais as palavras de idiomas sub-representados, o que aumenta tokens, custo e latência.

O modelo especializado em português é treinado ou ajustado com corpora em português, para captar vocabulário e variedades do pt-BR. Pode ser treinado do zero ou adaptado de um multilíngue, sem exclusividade de idioma. Pode ganhar em expressões locais e termos regimentais, mas pode perder generalidade.

Um modelo de domínio legislativo se obtém por ajuste fino, por recuperação de documentos oficiais (RAG) ou por instruções, sem treinar do zero. Como o modelo não conhece normas posteriores ao treino, a recuperação de fontes oficiais atualizadas é prática comum.

O ASR multilíngue e o LLM multilíngue são componentes distintos: ser multilíngue num não garante no outro. A avaliação deve usar dados em português do domínio de uso.

Nomes e versões de modelos mudam em meses e são voláteis, e a banca pode cobrar o conceito, como multilíngue, especializado ou de domínio, e não o nome do produto.

**Relatório por parágrafo (ideia | frase do bloco).**

1. Modelo multilíngue e tokenização | "Modelo multilíngue: um único modelo treinado com dados de vários idiomas"; "o tokenizador pode fragmentar mais as palavras de idiomas sub-representados"
2. Modelo especializado em português | "'Especializado' pode significar treinado do zero em português OU adaptado de um modelo multilíngue; não implica exclusividade de idioma."
3. Modelo de domínio e vigência | "Modelo de domínio (legislativo): obtém-se por ajuste fino ..., por recuperação de documentos oficiais (RAG, 3.2) ou por instruções (prompts)"
4. ASR x LLM e avaliação em português | "o ASR multilíngue ... e o LLM multilíngue são componentes distintos"; "testar em tarefas e dados em português do domínio de uso"
5. Volatilidade de nomes de modelos | "A banca pode cobrar o CONCEITO, e não o nome do produto." (multilíngue, especializado, de domínio)

## P2-4.1

**Contagens.** Curso 1207 palavras; teto efetivo 300; resumo 298 palavras; 6 parágrafos (54, 52, 59, 48, 38, 47).

**Resumo.**

Dado pessoal é a informação relacionada a pessoa natural identificada ou identificável (art. 5º, I), inclusive voz e falas transcritas de pessoa identificada. O dado sensível, do art. 5º, II, inclui o dado biométrico vinculado a pessoa natural. É controverso se toda gravação de voz é sensível, pois a lei não define dado biométrico.

O controlador decide sobre o tratamento (art. 5º, VI), o operador trata em nome dele (VII) e o encarregado é canal de comunicação (VIII), sem decidir finalidades. Transcrever e sumarizar são tratamento. O operador que usa o áudio para finalidade própria extrapola as instruções e responde solidariamente (art. 42, § 1º, I).

O dado anonimizado não é dado pessoal (art. 12, caput), salvo se o processo for revertido exclusivamente com meios próprios ou for reversível com esforços razoáveis. Pseudonimizar não é, por si, anonimizar: a definição do art. 13, § 4º, vale só para esse artigo, e, se o próprio controlador reverte com a informação que guarda, o dado continua pessoal.

O consentimento não é a única base legal (art. 7º). A dispensa para dado tornado manifestamente público pelo titular não afasta os direitos do titular nem os princípios (art. 7º, § 4º). A LGPD se aplica ao poder público, cujo tratamento deve atender à finalidade pública (art. 23).

O titular pode solicitar revisão de decisão tomada unicamente com base em tratamento automatizado que afete seus interesses (art. 20). O texto vigente não exige revisão por pessoa natural; a Lei 13.853/2019 suprimiu essa exigência da redação original.

A Lei 15.352/2026 criou a ANPD, autarquia vinculada ao Ministério da Justiça e Segurança Pública, e a autoridade nacional passou a ser exercida por ela; a redação de órgão da Presidência está superada. A multa não consta das sanções aplicáveis a órgãos públicos (art. 52, § 3º).

**Relatório por parágrafo (ideia | frase do bloco).**

1. Dado pessoal e dado sensível | "Dado pessoal: informação relacionada a pessoa natural identificada ou identificável (art. 5º, I)."; "a lei não define 'dado biométrico'; se toda gravação de voz ... depende de interpretação" (ponto controverso)
2. Controlador, operador, encarregado | "controlador (VI) ... operador (VII) ... encarregado (VIII: canal de comunicação ...)"; art. 42, § 1º, I (conforme o desenho do contrato: operador que usa o áudio)
3. Anonimização e pseudonimização | "O dado anonimizado não é dado pessoal (art. 12, caput), SALVO ..."; art. 13, § 4º ("para os efeitos deste artigo"); reversão com a informação adicional que o controlador guarda
4. Bases de tratamento e poder público | art. 7º, § 4º (dado tornado manifestamente público pelo titular); art. 23 ("deverá ser realizado para o atendimento de sua finalidade pública")
5. Decisões automatizadas e redação superada | art. 20, caput ("unicamente com base em tratamento automatizado ... que afetem seus interesses"); "O texto vigente NÃO diz que a revisão seja feita por pessoa natural"
6. ANPD, Lei 15.352/2026 e sanções | "A Lei 15.352/2026 CRIA a Agência Nacional de Proteção de Dados (ANPD) ..."; "a multa (incisos II e III) não consta dessa lista"

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

Inalterado em relação à v1 (ver `T111_resumos_P2_A4_v1.md`, relatório do P2-4.2).

## P2-4.3

**Contagens.** Curso 625 palavras; teto efetivo 300; resumo 255 palavras; 5 parágrafos (28, 69, 58, 47, 53).

**Resumo.**

A segurança da informação protege a confidencialidade, a integridade e a disponibilidade: só quem pode acessa, o dado não é alterado sem autorização e está acessível quando necessário.

No pipeline, a captação exige autenticidade da fonte, por causa do áudio sintético; a transmissão, criptografia em trânsito; o armazenamento, criptografia em repouso e gestão de chaves; a revisão e publicação, privilégio mínimo, registro e trilha de auditoria; e a retenção, prazo definido e eliminação do áudio bruto quando cessar a finalidade, salvo conservação autorizada (arts. 15 e 16). Cifrar o áudio não dispensa acesso restrito, registro e retenção.

No processamento, é preciso verificar no contrato, sem presumir, quem é o fornecedor, onde processa, se há subcontratados e se usa os dados do cliente para outro fim. Enviar áudio a serviço externo implica perda de custódia, e enviar áudio de pessoas identificadas a servidores no exterior pode configurar transferência internacional, permitida só nos casos do art. 33.

Há riscos próprios de IA. Na injeção de instruções, o texto transcrito ou recuperado traz comandos maliciosos que manipulam o LLM, e por isso o conteúdo transcrito é dado, não instrução. Embeddings não se presumem anônimos. Sem controle de integridade, a transcrição pode ser alterada sem rastro.

A LGPD impõe medidas de segurança técnicas e administrativas desde a concepção do serviço (art. 46, caput e § 2º), e o dever persiste após o término do tratamento (art. 47). Em incidente que possa acarretar risco ou dano relevante, quem comunica a autoridade nacional e o titular é o controlador (art. 48).

**Relatório por parágrafo (ideia | frase do bloco).**

1. Três propriedades | "confidencialidade (só quem pode acessa), integridade ... e disponibilidade ..."
2. Pontos de ação no pipeline | "Pipeline típico, e onde agir:"; retenção "salvo conservação autorizada (LGPD, arts. 15 e 16)"
3. Processamento por terceiros e transferência | "quem é o fornecedor, onde processa, se há subcontratados, se usa os dados do cliente para outro fim (verificar no contrato; não presumir)"
4. Riscos específicos de IA | texto transcrito ou recuperado com comandos maliciosos manipula o LLM que o processa; "tratar conteúdo transcrito como dado, não como instrução"
5. Dispositivos da LGPD sobre segurança | arts. 46, caput e § 2º, 47 e 48 ("que possa acarretar risco ou dano relevante")

## Bloco JSON

```json
{
 "topicos": {
  "P2-3.1": {
   "resumo": "A IA em parlamentos se organiza em quatro famílias de aplicação sobre o acervo de sessões e reuniões. A transcrição converte fala em texto e é a base das demais. A sumarização condensa o conteúdo, de modo extrativo, que seleciona e copia trechos, ou abstrativo, que redige frases novas, caso dos LLMs. A indexação associa metadados, como tema, orador, proposição e órgão. A busca localiza documentos ou trechos.\n\nAs etapas são encadeadas: a saída de uma é a entrada da seguinte. Um erro de transcrição, como nome trocado ou \"não\" omitido, se propaga para o resumo, o índice e a busca, e o produto final parece mais confiável do que é. Se a transcrição trocar o número da proposição, o índice associa a fala à proposição errada.\n\nOs benefícios usuais são rapidez, acessibilidade, memória institucional e ganho de escala. Os riscos são erro e texto fluente porém falso, viés, perda de fidelidade, exposição de dados pessoais, opacidade e dependência de fornecedor. A IA apoia, e o que vira registro oficial passa por revisão humana.\n\nSumarização não é transcrição menor, pois o resumo condensa e reformula e a transcrição reproduz. A IA também não decide sozinha o que é relevante: critérios, tesauro e avaliação são definidos pela instituição, e acervo público não dispensa supervisão e avaliação.\n\nO Ato da Mesa nº 225/2025, norma interna fora dos objetos de avaliação, fixa diretrizes de governança de IA na Câmara, como supervisão humana (art. 3º, I) e conformidade com a LGPD (III). Não trata de transcrição, taquigrafia nem registro de sessões, e não se pode afirmar que regule os sistemas aqui descritos."
  },
  "P2-3.2": {
   "resumo": "A busca lexical recupera documentos que contêm os termos da consulta e falha quando a palavra do usuário não é a do documento. A busca semântica converte consulta e trechos em embeddings, vetores numéricos, e devolve os trechos de sentido mais próximo.\n\nOs passos típicos são dividir os documentos em trechos, gerar embeddings, guardar em índice vetorial, embutir a consulta, recuperar os mais próximos e, opcionalmente, reordenar.\n\nA busca híbrida combina as duas, porque termos exatos, como o número de uma proposição, pedem a busca lexical, e a semelhança de sentido atende outra necessidade. A semântica nem sempre é mais precisa.\n\nNem a busca semântica nem o RAG, geração com recuperação, verificam fatos. O RAG pede ao LLM que responda com base nos trechos recuperados e reduz, mas não elimina, a resposta inventada.\n\nA avaliação da busca usa duas medidas: a precisão, que mede quanto do recuperado é relevante, e a revocação, que mede quanto do relevante foi recuperado."
  },
  "P2-3.3": {
   "resumo": "Ata é o documento formal que registra o ocorrido na reunião, com presenças, pauta, deliberações, votações e encaminhamentos. Resumo é a condensação informativa do conteúdo. O regime jurídico da ata na Câmara não é tratado aqui; fica o princípio: documento que pode produzir efeitos exige conferência e responsável humano.\n\nO fluxo típico parte de transcrição verificada, segmenta por item de pauta, extrai campos estruturados, gera o texto em geral de forma abstrativa com modelo de estrutura fixo e termina em revisão humana obrigatória.\n\nOs riscos específicos são omissão e inversão, como \"aprovado\" por \"rejeitado\", atribuição errada de fala ou voto, números e nomes trocados e fluência enganosa. Alucinação é conteúdo não sustentado pela fonte; a frase ser nova não é o problema.\n\nA mitigação separa campos factuais, extraídos, da narrativa gerada, exige citação do trecho-fonte e mantém revisão humana. Métricas de sobreposição, como ROUGE, medem semelhança de texto, não fidelidade factual."
  },
  "P2-3.4": {
   "resumo": "O modelo multilíngue é um único modelo treinado com dados de vários idiomas. Seu desempenho varia por idioma, em geral melhor nos de mais dados. O tokenizador pode fragmentar mais as palavras de idiomas sub-representados, o que aumenta tokens, custo e latência.\n\nO modelo especializado em português é treinado ou ajustado com corpora em português, para captar vocabulário e variedades do pt-BR. Pode ser treinado do zero ou adaptado de um multilíngue, sem exclusividade de idioma. Pode ganhar em expressões locais e termos regimentais, mas pode perder generalidade.\n\nUm modelo de domínio legislativo se obtém por ajuste fino, por recuperação de documentos oficiais (RAG) ou por instruções, sem treinar do zero. Como o modelo não conhece normas posteriores ao treino, a recuperação de fontes oficiais atualizadas é prática comum.\n\nO ASR multilíngue e o LLM multilíngue são componentes distintos: ser multilíngue num não garante no outro. A avaliação deve usar dados em português do domínio de uso.\n\nNomes e versões de modelos mudam em meses e são voláteis, e a banca pode cobrar o conceito, como multilíngue, especializado ou de domínio, e não o nome do produto."
  },
  "P2-4.1": {
   "resumo": "Dado pessoal é a informação relacionada a pessoa natural identificada ou identificável (art. 5º, I), inclusive voz e falas transcritas de pessoa identificada. O dado sensível, do art. 5º, II, inclui o dado biométrico vinculado a pessoa natural. É controverso se toda gravação de voz é sensível, pois a lei não define dado biométrico.\n\nO controlador decide sobre o tratamento (art. 5º, VI), o operador trata em nome dele (VII) e o encarregado é canal de comunicação (VIII), sem decidir finalidades. Transcrever e sumarizar são tratamento. O operador que usa o áudio para finalidade própria extrapola as instruções e responde solidariamente (art. 42, § 1º, I).\n\nO dado anonimizado não é dado pessoal (art. 12, caput), salvo se o processo for revertido exclusivamente com meios próprios ou for reversível com esforços razoáveis. Pseudonimizar não é, por si, anonimizar: a definição do art. 13, § 4º, vale só para esse artigo, e, se o próprio controlador reverte com a informação que guarda, o dado continua pessoal.\n\nO consentimento não é a única base legal (art. 7º). A dispensa para dado tornado manifestamente público pelo titular não afasta os direitos do titular nem os princípios (art. 7º, § 4º). A LGPD se aplica ao poder público, cujo tratamento deve atender à finalidade pública (art. 23).\n\nO titular pode solicitar revisão de decisão tomada unicamente com base em tratamento automatizado que afete seus interesses (art. 20). O texto vigente não exige revisão por pessoa natural; a Lei 13.853/2019 suprimiu essa exigência da redação original.\n\nA Lei 15.352/2026 criou a ANPD, autarquia vinculada ao Ministério da Justiça e Segurança Pública, e a autoridade nacional passou a ser exercida por ela; a redação de órgão da Presidência está superada. A multa não consta das sanções aplicáveis a órgãos públicos (art. 52, § 3º)."
  },
  "P2-4.2": {
   "resumo": "São protegidas as criações do espírito fixadas em qualquer suporte, entre elas conferências e alocuções (art. 7º, II), e a proteção independe de registro (art. 18). Não são protegidos ideias e métodos como tais, textos de leis e demais atos oficiais, informações de uso comum e nomes ou títulos isolados (art. 8º).\n\nOs direitos morais, como reivindicar a autoria e assegurar a integridade (art. 24), são inalienáveis e irrenunciáveis (art. 27), e a cessão total não os compreende (art. 49, I). Os patrimoniais dependem de autorização prévia e expressa para reprodução, adaptação e inclusão em base de dados (arts. 28 e 29).\n\nEstar disponível na internet não é estar em domínio público, que ocorre setenta anos contados de 1º de janeiro do ano seguinte ao falecimento (art. 41), além das hipóteses do art. 45.\n\nEntre as limitações do art. 46 estão a citação para estudo, crítica ou polêmica, na medida justificada e com indicação do autor e da origem (III); citação não é reprodução integral livre.\n\nHá pontos controversos, sem texto legal expresso nem jurisprudência firmada, e nenhum se afirma como certo: se o conteúdo gerado por IA é obra protegida, se o treinamento com obras protegidas é reprodução ilícita ou se cabe em limitação, e se o pronunciamento parlamentar é alocução protegida (art. 7º, II) ou ato oficial (art. 8º, IV). O art. 46, I, b, é só indício legal de que discursos são matéria autoral.\n\nNo campo ético, os conceitos estáveis são transparência sobre o uso de IA, responsabilidade humana pelo texto publicado, revisão humana, rastreabilidade das fontes e não atribuir a ninguém palavras que não disse."
  },
  "P2-4.3": {
   "resumo": "A segurança da informação protege a confidencialidade, a integridade e a disponibilidade: só quem pode acessa, o dado não é alterado sem autorização e está acessível quando necessário.\n\nNo pipeline, a captação exige autenticidade da fonte, por causa do áudio sintético; a transmissão, criptografia em trânsito; o armazenamento, criptografia em repouso e gestão de chaves; a revisão e publicação, privilégio mínimo, registro e trilha de auditoria; e a retenção, prazo definido e eliminação do áudio bruto quando cessar a finalidade, salvo conservação autorizada (arts. 15 e 16). Cifrar o áudio não dispensa acesso restrito, registro e retenção.\n\nNo processamento, é preciso verificar no contrato, sem presumir, quem é o fornecedor, onde processa, se há subcontratados e se usa os dados do cliente para outro fim. Enviar áudio a serviço externo implica perda de custódia, e enviar áudio de pessoas identificadas a servidores no exterior pode configurar transferência internacional, permitida só nos casos do art. 33.\n\nHá riscos próprios de IA. Na injeção de instruções, o texto transcrito ou recuperado traz comandos maliciosos que manipulam o LLM, e por isso o conteúdo transcrito é dado, não instrução. Embeddings não se presumem anônimos. Sem controle de integridade, a transcrição pode ser alterada sem rastro.\n\nA LGPD impõe medidas de segurança técnicas e administrativas desde a concepção do serviço (art. 46, caput e § 2º), e o dever persiste após o término do tratamento (art. 47). Em incidente que possa acarretar risco ou dano relevante, quem comunica a autoridade nacional e o titular é o controlador (art. 48)."
  }
 }
}
```

FIM DO ARQUIVO
