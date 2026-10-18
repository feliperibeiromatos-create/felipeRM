# QA_T98A_R1_2026-10-18_gce-cqfp.md — T-98 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L3_reforco_onda4_A_v1.md (gce-cpp; 28 itens AUTORAL L3-R12 a L3-R39; P2-3.1 = R12–R25, P2-3.2 = R26–R39). Rodada R1. Revisora: gce-cqfp (opus; não produziu). Ciclo 2026-10-18 s13c2. Nada foi reescrito no objeto; sem commit.
Entradas lidas: linha T-98 (TAREFAS.md; piso de 10 diretos por folha); D-REFORCO-1/2, D-FONTE-DATA-ANTERIOR, D-T89-R1-ACEITE, D-T96-ONDA2-ACEITE (II), D-T97-ONDA3-ACEITE (II), D-T97-META-FUNDADOR-RESP, D-ADERENCIA (DECISOES.md); T91_reconciliacao (seção 3: critério de formato; AP em 3.1 = LEGADO); T97_reconciliacao (seções 3.3, 3.4, 6); saida/banco/estilo_onda_3.md (seção 5); edital/modulo_RF_IA_P2.md (3.1, 3.2); pacote.json v1.10 (560 itens; P2-3.1 e P2-3.2 filtrados, e varredura por termo no pacote inteiro); L3_reforco_onda4_B_v1.md e C_v1.md (só para gêmeos); QA_T97B_R1 (precedente de rótulo da página "Como pesquisar").

## 1. Evidência — todas as 20 bases reabertas por esta coordenação em 18/10/2026

Método: curl com User-Agent de navegador, HTTP 200 em todas (sem redirecionamento além do declarado); HTML convertido a texto; os 38 trechos literais das justificativas buscados por script (python3 -I, scratchpad, somente leitura). Resultado: 38/38 CONFERE.

| fonte (URL) | HTTP | trechos conferidos | itens |
|---|---|---|---|
| Legin, Ato da Mesa nº 251/2026, publicação original (…/atodamesa-251-16-marco-2026-798819-publicacaooriginal-178493-cd-mesa.html) | 200 | art. 7º, caput e V: "Compete à Coordenação de Gestão do Discurso: […] V - sumarizar, indexar e tematizar os discursos […], vinculando os pronunciamentos às proposições legislativas" | R12 |
| www2.camara.leg.br …/pesquisa/como-pesquisar | 200 | "Assunto: Resumo do discurso ou da reunião de comissão, com os principais assuntos tratados"; "Íntegra do discurso de plenário ou da reunião de comissão"; "termos compostos (mais de 1 palavra) devem ser colocados entre aspas duplas. E os conectivos "and" ou "or" podem ser utilizados" | R13, R14 |
| learn.microsoft.com …/search-indexer-overview | 200 | "pulls data in without you having to write any code that adds data to an index"; "On an initial run, when the index is empty…"; "On subsequent runs, the indexer can usually detect and retrieve just the data that has changed. For blob data, change detection is automatic" | R15, R16 |
| …/cognitive-search-skill-keyphrases; …/cognitive-search-skill-entity-recognition-v3 | 200/200 | "main talking points in the record"; categorias Person, Location, Organization | R17 |
| …/cognitive-search-concept-intro | 200 | "mapping information for sending enriched content to target field"; "Output field mappings set the data path from enriched documents to an index"; "isn't searchable in its raw form"; "Optical character recognition (OCR) to recognize printed and handwritten text in binary files" | R18, R22 |
| …/search-lucene-query-architecture | 200 | "The unit of storage is an inverted index, one for each searchable field"; "Each term maps to the list of documents in which it occurs"; "Query execution has four stages" | R19, R23 |
| …/search-analyzers | 200 | "A general rule is to use the same analyzer for both indexing and querying, unless specific requirements dictate otherwise" | R20 |
| …/search-synonyms | 200 | "Explicit mapping only applies in the direction specified, and doesn't rewrite the query WA to Washington" | R21 |
| …/search-filters | 200 | "In contrast with keyword and vector search, a filter succeeds only if the match is exact"; "Security filters pass security identifiers as filter criteria, where a match in the index serves as a proxy for access rights" | R24, R38 |
| …/search-faceted-navigation | 200 | "Facets are dynamic because they're based on each specific query result set"; "The query executes first, and then facets are pulled from the current results" | R25 |
| …/vector-search-ranking | 200 | "Vector queries execute against an embedding space consisting of vectors generated from the same embedding model"; "For normalized vectors, this metric is identical to cosine similarity"; "exhaustive KNN can be used to build the ground truth set of nearest neighbors" | R26, R35, R36 |
| docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/task-types | 200 | "To get the best performance, you must use different task types to generate embeddings for your corpus and your queries"; RETRIEVAL_DOCUMENT / RETRIEVAL_QUERY. Nota: a página diz, logo depois, "you should use a task type that matches the user's intent" (há outros tipos de consulta); o item, que diz "um para documento e outro para consulta", continua correto | R27 |
| …/vector-search-how-to-chunk-documents | 200 | "beneficial if content is poorly represented as a single vector"; tabela Fixed-size × Variable-sized ("end-of-sentence punctuation marks, end-of-line markers") | R28, R29 |
| docs.aws.amazon.com …/kb-chunking.html | 200 | "the system initially retrieves child chunks, but replaces them with broader parent chunks" | R30 |
| …/hybrid-search-ranking | 200 | "take into account the position of the items in the original rankings"; "Each algorithm has its own range and magnitude" | R31 |
| …/semantic-search-overview | 200 | "it always adds secondary ranking over an initial result set that was scored using BM25 or Reciprocal Rank Fusion (RRF)"; "Extracts verbatim sentences and phrases from fields that best summarize the content" | R32, R33 |
| docs.aws.amazon.com …/opensearch-service/…/knn.html | 200 | "If you mix the knn query with other clauses, you might receive fewer than k results. In this example, the post_filter clause reduces the number of results from 2 to 1" | R34 |
| …/hybrid-search-overview | 200 | "Explicit sort orders override relevance-ranked results" | R37 |
| docs.aws.amazon.com …/kb-how-it-works.html | 200 | "Binary vectors, which use only 1 bit per dimension, aren't as costly on storage as floating-point (float32) vectors, which use 32 bits per dimension. However, binary vectors aren't as precise" | R39 |

Bases não reabertas: nenhuma. D-FONTE-DATA-ANTERIOR não invocada (correto). Planalto não usado (nenhuma lei federal).

## 2. Veredito por item

Legenda: G = gabarito conferido; Base = literal; Ponto = ponto único e frase-base sem gêmeo (pacote v1.10 inteiro, *reforco*, partes B e C); Adr. = aderência por esta QA; VOL = rótulo por esta QA.

| id | folha | G | Base | Ponto | formato | [TS] | VOL | Adr. | veredito |
|---|---|---|---|---|---|---|---|---|---|
| L3-R12 | 3.1 | E ok | CONFERE | ok (L2-R39 usa o art. 7º, I; outro inciso) | D | ok (objeto da vinculação) | n | PARCIAL | **REPROVADO (escopo/aderência)** — PENDENTE NORMATIVO |
| L3-R13 | 3.1 | C ok | CONFERE | ok (L2-R07/R25/R61/R66, outros campos) | PC | ok (espelho) | **VOLÁTIL baixo** | PARCIAL | **AJUSTAR (rótulo + aderência)** |
| L3-R14 | 3.1 | C ok | CONFERE | ok | SH | — | **VOLÁTIL baixo** | PARCIAL | **AJUSTAR (rótulo + aderência)** |
| L3-R15 | 3.1 | E ok | CONFERE | ok | TSj | ok (serviço × aplicativo) | n | direta | APROVADO |
| L3-R16 | 3.1 | C ok | CONFERE | ok | SH | — | **VOLÁTIL baixo** | direta | **AJUSTAR (rótulo)** |
| L3-R17 | 3.1 | E ok | CONFERE | ok (× L3-Q01, distinto) | PC | ok (inversão das funções) | n | direta | APROVADO |
| L3-R18 | 3.1 | C ok | CONFERE | ok | D | — | n | direta | APROVADO |
| L3-R19 | 3.1 | E ok | CONFERE | ok | D | ok (direção termo→doc) | n | direta | APROVADO |
| L3-R20 | 3.1 | E ok | CONFERE | ok | SH (registro) | ok (mesmo × diferentes) | n | direta | APROVADO |
| L3-R21 | 3.1 | E ok | CONFERE | ok | PC | ok (sentido) | n | direta | APROVADO |
| L3-R22 | 3.1 | C ok | CONFERE | ok | D (registro) | — | n | direta | APROVADO |
| L3-R23 | 3.1 | C ok | CONFERE | ok | NP | — | n | direta | APROVADO COM RESSALVA (baixa discriminação) |
| L3-R24 | 3.1 | C ok | CONFERE | ok | PC | ok (espelho) | n | direta | APROVADO |
| L3-R25 | 3.1 | E ok | CONFERE | ok | SH | ok (dinâmicas × estáticas) | n | direta | APROVADO |
| L3-R26 | 3.2 | E ok | CONFERE | ok (× Q05, R08 distintos) | SH | ok (modelo × dimensão) | n | direta | APROVADO |
| L3-R27 | 3.2 | C ok | CONFERE | ok (× L3-R65 da parte B, distinto) | PC | — | VOLÁTIL baixo (ok) | direta | APROVADO |
| L3-R28 | 3.2 | C ok | CONFERE | ok | SH | — | n | direta | APROVADO |
| L3-R29 | 3.2 | E ok | CONFERE | ok | PC | ok (inversão das descrições) | n | direta | APROVADO |
| L3-R30 | 3.2 | C ok | CONFERE | ok (BQ-0106 é clustering, distinto) | AP | ok (espelho) | n | direta | APROVADO |
| L3-R31 | 3.2 | E ok | CONFERE | ok | D | ok (posição × pontuação) | n | direta | APROVADO |
| L3-R32 | 3.2 | E ok | CONFERE | ok | D | ok (2ª × 1ª etapa) | n | direta | APROVADO |
| L3-R33 | 3.2 | E ok | CONFERE | ok | PC | ok (literal × abstrativo) | n | direta | APROVADO |
| L3-R34 | 3.2 | C ok | CONFERE | ok | SH | — | n | direta | APROVADO |
| L3-R35 | 3.2 | E ok | CONFERE | ok (× R04, distinto) | PC | ok (normalizados × não) | n | direta | APROVADO |
| L3-R36 | 3.2 | C ok | CONFERE | ok (× R03, distinto) | AP | — | n | direta | **AJUSTAR (texto)** |
| L3-R37 | 3.2 | E ok | CONFERE | ok | SH | ok (sobrepõe × mantém) | n | direta | APROVADO |
| L3-R38 | 3.2 | C ok | CONFERE | ok | AP | — | n | direta | APROVADO |
| L3-R39 | 3.2 | C ok | CONFERE | ok | NP | ok (espelho) | n | direta | APROVADO |

Nenhum gabarito errado. Nenhuma ambiguidade de gabarito. Nenhum gêmeo no pacote v1.10 nem nas partes B e C (varredura por termo: pull/push, frases-chave, índice invertido, analisador, sinônimo, OCR, faceta, tipo de tarefa, chunk, hierárquic, RRF, ranqueador, legenda, k-NN, produto escalar, exaustivo, ground truth, ordenação, binário, segurança, tematiz, Coordenação de Gestão do Discurso, art. 7º; os acertos são de pontos distintos, já declarados em 1.3 da entrega ou triviais, como BQ-0019 KNN-classificador e BQ-0106 clustering).

### 2.1 Motivos

**L3-R12 — REPROVADO (escopo/aderência).** Literal e gabarito corretos, mas: (a) o ponto é competência de coordenação do Derep (a quem cabe indexar e a que se vinculam os pronunciamentos), sem conteúdo de IA, numa folha de "Aplicações de IA em parlamentos"; (b) a instrução da Gerência para a onda 4 (T97_reconciliacao, 3.4) diz que norma de estrutura ou competência de órgão (Ato 251) "entra só quando o ponto é o próprio registro, a revisão ou a publicação do texto" — indexação/tematização não é nenhum dos três; (c) precedente de mesma natureza: L2-R39 (Ato 251, art. 7º, I, Coordenação de Gestão do Discurso) foi canonizado como PARCIAL; (d) a 3.1 parte de 4 diretas (< 12), e a mesma 3.4 manda que item novo dessa folha seja direto. A D1 é da Gerência; esta QA não vê leitura que o mantenha como direto. Repor por 1 item de saldo direto (de preferência sumarização ou transcrição de sessões, hoje sem item novo na folha; formato diferente de SH, ver seção 3). PENDENTE NORMATIVO (Ato da Mesa no Legin) enquanto existir.

**L3-R13 e L3-R14 — AJUSTAR (rótulo e aderência).** (1) VOLÁTIL: a mesma página "Como pesquisar" sustentou L2-R07, L2-R25, L2-R61 e L2-R66, todos VOLÁTIL baixo e assim canonizados (D-T97-ONDA3-ACEITE, lista dos 18; QA_T97B_R1, l. 43 e 48). Papel de campo e sintaxe de busca de um portal não são "recurso central de serviço" de fornecedor no sentido da D-T96-ONDA2-ACEITE (II); são redação de interface que pode mudar sem aviso. "Marcação a menos não" → marcar VOLÁTIL baixo (REVERIFICAR em 4–8/1/2027), ou a Gerência registra por D1 por que a mesma página muda de rótulo. (2) Aderência: o ponto é o uso de campo (R13) e a sintaxe booleana (R14) de um portal de pesquisa sem IA; pelo critério que fez L3-R01/R02 PARCIAIS (ponto institucional em folha de IA) e L2-R61/R66 PARCIAIS, são PARCIAIS. Efeito: pela regra do Fundador (D-T97-META-FUNDADOR-RESP) contam para a meta de 20 e a 3.1 continua acima do piso de 10 diretas; pela instrução 3.4 da T97_reconciliacao (item novo de folha com menos de 12 diretas é direto), seriam substituídos. Escolha = D1 da Gerência; não reprovo porque gabarito, base e ponto estão corretos.

**L3-R16 — AJUSTAR (rótulo).** O gabarito depende de "For blob data, change detection is automatic": comportamento padrão de produto que a página diferencia por fonte de dados ("For other data sources like Azure SQL or Azure Cosmos DB…"). É a hipótese (b) da D-T96-ONDA2-ACEITE (II). Marcar VOLÁTIL baixo. A 3.1 fica, com R13, R14 e R16, em 3/20 = 15% (≤ 20%).

**L3-R36 — AJUSTAR (texto, concordância).** "Um órgão legislativo […] deseja avaliar […]. Segundo a documentação do Azure AI Search, **ela** pode usar o KNN exaustivo" — o referente é masculino. Texto exato: trocar "ela pode usar" por "ele pode usar". Sem efeito de gabarito.

**L3-R23 — APROVADO COM RESSALVA.** Correto e com base literal, mas é o C de menor discriminação da parte (enumeração reproduzida; recomendação 7 do estilo_onda_3), já declarado pela produção. Não reprovo; recomendo que fique fora do núcleo (campo "nucleo") e que a Gerência avalie trocá-lo se houver saldo da 3.1.

## 3. Formato, teto de 30% e AP em 3.1

- Contagens declaradas conferidas (3.1: D 5, PC 5, SH 5, TSj 2, NP 1, AP 2; 3.2: D 3, PC 5, SH 5, TSj 1, NP 2, AP 4). Nenhum AP novo em 3.1 (legado da T91, 3.3, respeitado; a folha de 20 tem AP 2/20 = 10%, de volta ao teto, e o bloqueio de AP em 3.1 pode ser encerrado pela Gerência).
- Registro de classificação (sem reprovação): R22 abre com "Considere que…" (construção de SH) e está como D; R20 está como SH sem cenário que pese no juízo (é regra geral, construção de D). Se a Gerência reclassificar R22 como SH, a 3.1 fica com SH 6/20 = 30% (no teto) — e, sem o R12, 6/19 = 31,6% até o saldo; logo, o saldo da 3.1 não pode ser SH.
- 3.2: R30, R36 e R38 (AP) têm moldura parlamentar explícita (comissão, órgão legislativo, assembleia), conforme o precedente da QA_T97C_R1 (AP exige aplicação parlamentar); a fronteira AP × SH é tênue, mas, mesmo lidos como SH, a Gerência deve conferir: SH passaria a 8/20 = 40% (acima do teto). Mantida a classificação declarada; D1 da Gerência.

## 4. VOLÁTIL

- R27: VOLÁTIL baixo, hipótese (b) — CONCORDO (parâmetro nomeado de API; a página foi atualizada em 2026-10-15 e mudou de endereço, o que reforça a marcação). Inapto a simulado final até a reverificação.
- Acrescentar VOLÁTIL baixo: R13, R14 (precedente da mesma página), R16 (padrão por fonte de dados). Por folha: 3.1 3/20 (15%), 3.2 1/20 (5%). Nenhum de risco alto.
- Demais (R15, R17–R26, R28–R39): NÃO VOLÁTIL confirmado (mecanismo de recurso central, sem número, versão, preço, padrão ou disponibilidade condicionada; os números de R23 e R39 são estruturais). R39: a página condiciona o uso de vetores binários ao modelo ("some models support"), mas o item julga só a relação 1 × 32 bits e custo × precisão, não a disponibilidade — não VOLÁTIL. Todos com conferência de base em 4–8/1/2027 (T-11, P2, gce-cqfp).

## 5. Estilo, gabarito e estrutura

- Gabarito: 14 C / 14 E (50%); por folha 7/7 e 7/7; folhas de 20 com 10/10. Sem o R12: 14 C / 13 E (51,9%), 3.1 com 10 C / 9 E — o saldo da 3.1 deve ser E para manter 10/10 (ou C, ficando 11/9, dentro da regra 5, que é por onda).
- [TS]: 18/28 conferidos por script; cada um com troca única (R17 e R29 são inversão de um par, mecanismo único, aceito nas ondas 2 e 3). Sem o R12: 17/27.
- Extensão (script próprio, só enunciado): C 52,4 × E 47,7 palavras (diferença 4,7; na onda 3 foi 1,0). Não é regra de reprovação (O-1 é critério), mas é pista de extensão no sentido da base: recomendo ao gbq-estilo pôr na amostra da onda 4 os C mais longos (R38 62, R16 59, R27 56, R28 55) e à Gerência, como D1 opcional, aparar 1 ou 2 deles na v2 sem mexer no ponto.
- Recomendações 1–6 e 8 do estilo_onda_3 cumpridas como declarado (conferi ", e não" 2C/2E; "Segundo/De acordo com" 4C/4E; concessiva em E nas duas folhas). Recomendação 7: R23 (ver 2.1).
- Concentração de fonte (registro): 21 dos 28 itens vêm do Microsoft Learn (Azure AI Search), 11 dos 14 novos da 3.1. Correto quanto à base, mas a banca tende a cobrar o conceito, não o produto; para o saldo da 3.1, preferir base não Microsoft e ponto conceitual (sumarização ou transcrição de sessões, hoje só nos canônicos Q02 e Q04).
- Estrutura: linha 1 no formato; Parte 2 sem gabarito, [TS], VOLÁTIL ou REVERIFICAR; Parte 3 com os mesmos 28 ids na mesma ordem; "FIM DO LOTE" presente; QA PENDENTE declarado em todos (D-QA-PENDENTE). Cobertura do edital: 3.1 cobre indexação e busca; sumarização e transcrição de sessões sem item novo (registro). 3.2 cobre busca semântica de forma ampla (embeddings, chunking, híbrida, RRF, ranqueador, métricas, ANN/KNN, filtros).

## 6. Aderência e piso de 10 diretas (T-98; D-T97-META-FUNDADOR-RESP)

| folha | itens | diretas (declarado) | diretas (esta QA) | piso 10 |
|---|---|---|---|---|
| P2-3.1 | 20 (19 sem R12) | 18 | 15 de 19 (Q01–Q04 + R15–R25), com R12 fora e R13/R14 PARCIAIS; 16 de 20 com saldo direto | CUMPRIDO |
| P2-3.2 | 20 | 20 | 20 | CUMPRIDO |

L3-R12: o art. 7º, V, do Ato da Mesa nº 251/2026 foi conferido literalmente no Legin (publicação original), mas a declaração de aderência "direta" NÃO se sustenta (seção 2.1).

## 7. Veredito geral

**APROVADO COM RESSALVAS — 1/28 reprovado (3,6%)**, sem GATE (limiar de 30%). REPROVADO: L3-R12 (escopo/aderência; PENDENTE NORMATIVO). AJUSTAR: L3-R13 e L3-R14 (VOLÁTIL baixo; aderência PARCIAL, com D1 da Gerência sobre a instrução 3.4 da T97), L3-R16 (VOLÁTIL baixo), L3-R36 ("ela" → "ele"). Ressalva: L3-R23 (baixa discriminação). Registros de formato (R20, R22; AP × SH na 3.2), de extensão (4,7 palavras) e de concentração de fonte. Nenhum gabarito errado; 20/20 bases reabertas e 38/38 literais CONFERE. Para a v2: aplicar os ajustes e repor o R12 por 1 item de saldo direto na 3.1 (não SH; preferencialmente E; ponto de sumarização ou transcrição de sessões; sem gêmeo com o pacote e com as partes B e C). Todos continuam QA PENDENTE até a R2 e a reconciliação.
