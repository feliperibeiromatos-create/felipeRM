# T113_onda1_D_v2.md — T-113 onda 1, parte D, rodada de correção R1 (P2-2.2, 2.8, 3.1, 4.1; 15 itens AUTORAL) — 2026-10-18 — gerado por gce-cpp

Reforço da ordem F (D-REFORCO-2), parte D da D1 da GCE (V15_BAEF_D1_GCE_2026-10-18.md, seções 0 e 4) e da D1 da GBQ (V15_BAE_D1_GBQ_2026-10-18.md, 4.2). Quinze itens AUTORAL novos: L2-R143 (P2-2.2, +1), L2-R132 (P2-2.8, reposição, direta e não VOLÁTIL), L3-R96 a L3-R104 (P2-3.1, +9) e L3-R105 a L3-R108 (P2-4.1, +4). Nenhum item existente foi alterado. Esta v2 aplica o parecer R1: R101 e R108 substituídos, R102 e R104 com troca de rótulo, demais itens iguais à v1. Rótulo AUTORAL e QA PENDENTE (D-QA-PENDENTE) em todos. Aderência DIRETA em todos.


## RESPOSTA AO RELATÓRIO DE QA (QA_T113_D_R1_2026-10-18_gce-cqfp.md), item a item

| Ponto do QA | Resposta |
|---|---|
| L3-R101 REPROVADO (aderência) | **Acatado.** Item substituído, mesmo id. Novo ponto: a supervisão humana é sempre necessária no uso de IA para transcrição e análise (Manual de Comunicação da Câmara dos Deputados, "Uso da inteligência artificial"). Aderência direta a P2-3.1 (aplicações de IA em parlamentos); gabarito E, [TS] único; não VOLÁTIL (diretriz, não capacidade de produto nem estado da ferramenta); fonte oficial fora da UIP. O Akoma Ntoso sai da parte. |
| L3-R102 CORRIGIR (rótulo) | **Acatado.** Texto do item e justificativa inalterados. Mapa: VOLÁTIL passa a "n (definição de recurso; conferência de base em 4–8/1/2027)". Parte 3: a linha de VOLÁTIL baixo e a linha REVERIFICAR foram trocadas pelos textos exatos do parecer. |
| L3-R104 CORRIGIR (rótulo) | **Acatado.** Texto do item e justificativa inalterados. Mapa: VOLÁTIL passa a "VOLÁTIL baixo". Parte 3: "Não VOLÁTIL (conceito de arquitetura)." trocada por "VOLÁTIL baixo (capacidade documentada de produto; hipótese (b))." e acrescentada a linha REVERIFICAR antes de "Formato: D.", nos termos do parecer. |
| L3-R108 REPROVADO (duplicata D6-49) | **Acatado.** Item substituído, mesmo id; o par bloqueio × eliminação (art. 5º, XIII e XIV) sai da parte. Novo ponto: LGPD, art. 6º, IX (princípio da não discriminação) aplicado a sistema de IA que trata falas de audiências; gabarito E, [TS] por troca única do nome do princípio (não discriminação → prevenção). Conferido contra o pacote.json v1.11 (560 itens) e contra saida/gce/*.md, saida/gcb/*.md (D6 v2.1 inclusive): o art. 6º, IX só aparece em texto de curso (D6 v2.1, linha dos princípios; GCE_Lote3_v1/v2), em nenhum item; "fins discriminatórios" não consta de enunciado ou justificativa de item algum. Fora da lista de evitados do QA. PENDENTE NORMATIVO (ao qa-normativo). |
| Demais itens (L2-R143, L2-R132, L3-R96 a R100, R103, R105 a R107) | Sem alteração; iguais à v1. R105 a R107 seguem PENDENTE NORMATIVO. |
| Contas na parte (QA, seção 2) | Gabarito mantido em 7 C / 8 E (R101 e R108 continuam E); 3.1 em 4 C / 5 E; 4.1 em 2 C / 2 E. VOLÁTIL na 3.1: R100 e R104 (2 novos) mais 4 da onda 4, total 6/30 = 20% (no teto). Fornecedor na 3.1: UIP 4, Microsoft 2, Google 1, Câmara dos Deputados 2 (R100 Dados Abertos, R101 Manual de Comunicação), total 9; teto de 4 cumprido. Formato 3.1: D 9 (R100, R101, R104), SH 9, PC 6 (teto 9 de 30). Formato 4.1: R108 passa de PC a SH (SH novos 3; PC novos 0). |

Verificação das fontes novas em 18/10/2026: (i) Manual de Comunicação da Câmara, https://infograficos.camara.leg.br/manual-de-comunicacao/uso-da-inteligencia-artificial/ , lido por ferramenta de leitura de página (a página carrega por script e a requisição direta devolve corpo vazio); trecho literal "A supervisão humana é sempre necessária."; a página não exibe data de publicação ou atualização. (ii) LGPD, art. 6º, IX, texto compilado do Planalto, aberto em 18/10/2026: "não discriminação: impossibilidade de realização do tratamento para fins discriminatórios ilícitos ou abusivos".

## 0. Leituras, bases e verificações

**Lido antes:** CLAUDE.md; regras/proveniencia.md, padrao_resposta_cebraspe.md e estilo_banca.md; edital/modulo_RF_IA_P2.md (2.2 "Fluxo de trabalho de degravação assistida por IA (Human in the loop)"; 2.8 "Vocabulário técnico parlamentar e vocabulário adaptado (language model adaptation)"; 3.1 "Aplicações de IA em parlamentos: transcrição de sessões, sumarização, indexação e busca"; 4.1 "LGPD e proteção de dados em sistemas de transcrição e IA"); D-REFORCO-2 (DECISOES.md); ordens/ORDEM_V15_F_BANCO40.md; as seções 0 e 4 da D1 da GCE e a 4.2 da D1 da GBQ; T91_reconciliacao, seção 3.1 (critério de formato); formato de saida/gce/L3_reforco_onda4_A_v3.md; saida/pacote/pacote.json v1.11 (filtro P2-2.2, 2.8, 3.1, 4.1 e busca no pacote inteiro) e os 14 itens da onda 4 em 3.1 (L3_reforco_onda4_A_v3.md); cursos 2.2, 2.8, 3.1 e 4.1 de `lotes[].curso`.

**Bases.** Todas as páginas foram abertas em 18/10/2026 (HTTP 200) e baixadas nesse dia; os trechos literais da Parte 3 foram extraídos do texto baixado. Nenhuma data de verificação anterior foi usada. Nenhum item afirma sobre Whisper, Google Speech-to-Text, Azure Speech ou preço, versão, limite e região de produto. Os casos de uso da União Interparlamentar (UIP/IPU) são, nas palavras da própria página, descrição de "como um sistema deve funcionar", e não estudo de caso de implantação; por isso os enunciados falam em "caso de uso publicado" e não em "o parlamento faz".

**Concentração por fonte na 3.1 (9 novos; teto de 4 por fornecedor).** UIP 4 (R96, R97, R98, R99); Microsoft Learn 2 (R103, R104); Google Cloud 1 (R102); Câmara dos Deputados 2 (R100, Dados Abertos; R101, Manual de Comunicação). A UIP é organização interparlamentar, não fornecedor, e cada caso de uso tem autor distinto (Câmara dos Deputados da Itália, Senado da Itália, Parlamento da Estônia, Conselho de Representantes do Bahrein). A 3.1 com a onda 4 tinha 10 de 14 novos da Microsoft; aqui a Microsoft é 2 de 9.

**Verificação de não repetição.**
1. Busca por termo, sem distinção de maiúsculas, em `saida/pacote/pacote.json` (560 itens), `saida/gce/*.md`, `saida/gcb/*.md` e `banco/banco.csv` (exceto este arquivo), com os termos: Riigikogu, HANS, Akoma (ponto retirado na v2), knowledge store, Text Split, Bahrein, Canadá, Itália, Finlândia, proposicoesTemas, área temática, bloqueio (como definição), encarregado, "qualidade dos dados", UIP e IPU. Resultado: nenhum item do pacote nem da onda 4 traz os casos de uso da UIP, o Akoma Ntoso, o knowledge store, a habilidade Text Split, a classificação temática de proposições ou a classificação de conteúdo do Google. "UIP/IPU" aparece em arquivos anteriores só como fonte de outros pontos (diretrizes e glossário), e o 4.2 da onda 4 não usa os casos de uso de transcrição.
2. LGPD: pontos já usados e evitados. Art. 48, caput (L3-Q29, L3-R10); art. 46, caput e § 1º (L3-Q27, onda 4 parte C); art. 5º, I e II, art. 6º, III, art. 7º, § 3º, art. 11, II (a, b, e, g), art. 12, art. 20, art. 55-A, art. 37, § 2º, art. 42, § 1º, I. Os pontos novos (art. 6º, V; art. 9º, § 1º; art. 41, § 1º; art. 6º, IX) não constam em nenhum item do pacote nem da onda 4; o art. 5º, XIII e XIV saiu da parte (duplicata do D6-49). Vizinhanças declaradas, de pontos distintos: R105 × L3-Q13 (qualidade dos dados em modelo multilíngue, assunto diverso, sem relação com a LGPD); R106 × BQ-0002 (art. 9º, caput, direito de acesso à informação × art. 9º, § 1º, nulidade do consentimento); R107 × L3-Q18 (art. 5º, VI e VII) e o art. 41, § 2º, usado no curso e no D6; R108 × D6-36 e BQ-0024 (segurança, art. 6º, VII, e a prevenção que o D6 contrasta com ela): pontos distintos, não gêmeos (art. 6º, IX, não discriminação).
3. Ponto por folha: cada item tem um ponto declarado no mapa; nenhum repete nem é gêmeo de item da folha (v1.11 e, na 3.1, os 14 da onda 4) nem de outro da parte. Vizinhanças: R96 × L3-Q02 (resumo × transcrição, outro ponto: divisão por assunto com marcadores); R97 × L3-Q03 (revisão humana de IA em registro público, sem o fluxo documentalista/rascunho); R98 × L2-Q05 (HITL como definição geral × ordem revisão/publicação no caso HANS); R100 × L3-Q01 (indexação como conceito × estrutura do arquivo de classificação temática); R143 × L2-R24 e L2-Q05 (2.1 e 2.2: revisão do texto automático em vez de transcrição do zero e rascunho a validar × contingência de transcrição manual quando o sistema falha, outro ponto).
4. A conferência por script de sequências de seis palavras entre os enunciados e justificativas novos e os 560 itens do pacote e os arquivos `saida/gce/*reforco*.md` foi feita sobre este arquivo e não achou coincidência além de fórmulas de remissão ("segundo a Lei Geral de Proteção de Dados Pessoais", "nessa situação").

**Fontes e proveniência.** As afirmações sobre Amazon Transcribe, Whisper, Google Speech-to-Text e Azure Speech: nenhuma. Sobre produtos: Cloud Natural Language API (Google Cloud) e Azure AI Search (Microsoft Learn), nos termos literais das páginas da Parte 3. Normas: LGPD, texto compilado do Planalto, aberto em 18/10/2026; os itens R105 a R108 da 4.1 vão ao qa-normativo. Fonte nova da v2: Manual de Comunicação da Câmara dos Deputados (R101).

## Contagens

| Folha | Itens novos | C | E | [TS] | VOLÁTIL novos | VOLÁTIL na folha final |
|---|--:|--:|--:|--:|--:|---|
| P2-2.2 | 1 (L2-R143) | 1 | 0 | 0 | 0 | 1/21 (existente) |
| P2-2.8 | 1 (L2-R132) | 0 | 1 | 1 | 0 | 4/20 (existentes) |
| P2-3.1 | 9 (L3-R96 a R104) | 4 | 5 | 6 | 2 (R100, R104) | 6/30 = 20% (4 da onda 4 + 2) |
| P2-4.1 | 4 (L3-R105 a R108) | 2 | 2 | 2 | 0 | 1/30 (existente) |
| **Parte** | **15** | **7** | **8** | **9** | **2** | |

- Gabarito da parte: 7 C e 8 E (46,7%; faixa de 6 a 9 C cumprida). 3.1: 4 C e 5 E (faixa de 3 a 6). 4.1: 2 C e 2 E.
- [TS]: 9 de 15. Em E (troca única): R132, R96, R98, R100, R101, R104, R106, R108. Em C (espelho): R97.
- VOLÁTIL: 2 (R100 e R104), ambos baixo e na 3.1 (teto 2 da D1); 3.1 chega a 6 de 30 (20%, no teto).
- Aderência: 15 DIRETA, 0 PARCIAL.
- Ids: L2-R143, L2-R132, L3-R96 a L3-R108; nenhum id repetido.

### Formato × existentes × novos × total (legenda D, TSj, SH, NP, PC, AP; critério da T91_reconciliacao, 3.1; classificação dos existentes pela produção)

| Formato | 2.2 exist. | 2.2 novos | 2.2 total (teto 6 de 21) | 2.8 exist. | 2.8 novos | 2.8 total (teto 6 de 20) | 3.1 exist. | 3.1 novos | 3.1 total (teto 9 de 30) | 4.1 exist. | 4.1 novos | 4.1 total (teto 9 de 30) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| D | 5 | 0 | 5 | 7 | 0 | 7 (LEGADO) | 6 | 3 | 9 | 22 | 0 | 22 (LEGADO) |
| TSj | 7 | 0 | 7 (LEGADO) | 2 | 0 | 2 | 2 | 1 | 3 | 2 | 0 | 2 |
| SH | 7 | 0 | 7 (LEGADO) | 4 | 0 | 4 | 5 | 4 | 9 | 1 | 3 | 4 |
| NP | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1 |
| PC | 0 | 0 | 0 | 1 | 0 | 1 | 5 | 1 | 6 | 0 | 0 | 0 |
| AP | 0 | 1 | 1 | 4 | 1 | 5 | 2 | 0 | 2 | 0 | 1 | 1 |
| **Total** | 20 | 1 | 21 | 19 | 1 | 20 | 21 | 9 | 30 | 26 | 4 | 30 |

Existentes classificados: 2.2: D Q05, Q06, Q07, Q08, R03; TSj R04, R33, R35, R38, R39, R41, R42; SH R34, R36, R37, R40, R43, R44, R45; NP R46. 2.8: D Q28, Q29, Q30, R117, R118, R119, R126; TSj R17, R123; SH R120, R121, R122, R125; NP R18; PC R124; AP R127, R128, R129, R130. 3.1: D Q01, L2-R16, R12, R18, R19, R22; TSj L3-R02, R15; SH L3-R01, R14, R16, R20, R25; NP R23; PC Q02, R13, R17, R21, R24; AP Q03, Q04. 4.1: D BQ-0002, 0003, 0005, 0006, 0007, 0008, 0024, 0025, 0032, 0036, 0037, 0045, 0046, 0057, 0077, 0084, 0109, 0110 e L3-Q17, Q19, Q20, Q21 (22); TSj BQ-0056, L3-Q18; SH BQ-0004; NP BQ-0023.

Nenhum item novo usa formato que já excedesse o teto. Os excessos de D (2.8 e 4.1), TSj e SH (2.2) são LEGADO, não imputados à onda e não tocados. Na 3.1, D, SH e PC ficam no teto de 9 (30%); os novos de D (R100, R101, R104) e SH (R96, R98, R99, R103) fecham exatamente em 9 de 30. Na 3.1 não há novo item de AP (legado 2 de 21, T91, 3.3).

Fonte por item e classificação de formato divergente, se houver, ficam para a D1 da Gerência (R107: SH, e não TSj, por ter cenário; R105: AP por aplicar o princípio à transcrição de pronunciamentos; R108: SH, por ter cenário).

=====================================================================
PARTE 1/3 — MAPA
=====================================================================

| id | folha | ponto de julgamento | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL | aderência |
|---|---|---|---|---|---|---|
| L2-R143 | P2-2.2 | Quando o reconhecimento automático de fala está indisponível ou sua integração com o sistema de informação parlamentar é interrompida, o transcritor transcreve manualmente o segmento a partir do áudio e dos metadados (fluxo alternativo) | AP | UIP, "Automated speech recognition to support the transcription of parliamentary proceedings", caso de uso 066, Câmara dos Comuns do Canadá (https://www.ipu.org/ai-use-cases/automated-speech-recognition-support-transcription-parliamentary-proceedings; verificado em 18/10/2026) | n | direta |
| L2-R132 | P2-2.8 | O modelo de linguagem de fala para texto precisa de palavras novas de tempos em tempos e de treinamento adicional (o vocabulário não é estático) | AP | UIP, "AI-powered verbatim records system (HANS)", caso de uso 016, Parlamento da Estônia, "Potential challenges" (https://www.ipu.org/ai-use-cases/ai-powered-verbatim-records-system-hans; verificado em 18/10/2026) | n (conceito estável; reposição direta) | direta |
| L3-R96 | P2-3.1 | A sumarização do relatório taquigráfico divide o relatório em seções por assunto e gera marcadores e resumo breve para cada seção (e não para o relatório inteiro) | SH | UIP, "Tags and summaries of parliamentary reports", caso de uso 012, Câmara dos Deputados da Itália (https://www.ipu.org/ai-use-cases/tags-and-summaries-parliamentary-reports; verificado em 18/10/2026) | n | direta |
| L3-R97 | P2-3.1 | No resumo gerado por IA a partir da transcrição, o sistema produz o rascunho e o documentalista o revisa e finaliza quanto a exatidão e completude | TSj | UIP, "Creation of draft summary reports based on transcripts of parliamentary sessions", caso de uso 032, Senado da Itália (https://www.ipu.org/ai-use-cases/creation-draft-summary-reports-based-transcripts-parliamentary-sessions; verificado em 18/10/2026) | n | direta |
| L3-R98 | P2-3.1 | Na ata literal preparada pelo sistema, a revisão dos editores precede a publicação no sítio do parlamento | SH | UIP, "AI-powered verbatim records system (HANS)", caso de uso 016, Parlamento da Estônia, "Scenario" (https://www.ipu.org/ai-use-cases/ai-powered-verbatim-records-system-hans; verificado em 18/10/2026) | n | direta |
| L3-R99 | P2-3.1 | Com áudio ruim ou falas simultâneas, o sistema sinaliza os trechos da transcrição para revisão manual | SH | UIP, "Automated Hansard report system: Converting parliamentary audio to text using AI", caso de uso 062, Conselho de Representantes do Bahrein, "Alternate flows" (https://www.ipu.org/ai-use-cases/automated-hansard-report-system-converting-parliamentary-audio-text-using-ai; verificado em 18/10/2026) | n | direta |
| L3-R100 | P2-3.1 | Na classificação temática de proposições dos Dados Abertos da Câmara, cada registro corresponde a uma área temática, e a proposição com mais de um tema ocupa várias linhas | D | Câmara dos Deputados, Dados Abertos, "Classificação temática das proposições" (https://dadosabertos.camara.leg.br/swagger/api.html; verificado em 18/10/2026; a página não exibe data de atualização) | VOLÁTIL baixo | direta |
| L3-R101 | P2-3.1 | A supervisão humana é sempre necessária no uso de IA para transcrição e análise de conteúdo, inclusive com a checagem do conteúdo produzido | D | Câmara dos Deputados, Manual de Comunicação, "Uso da inteligência artificial" (https://infograficos.camara.leg.br/manual-de-comunicacao/uso-da-inteligencia-artificial/; verificado em 18/10/2026; a página não exibe data de publicação ou atualização) | n (diretriz; não depende de versão, preço, limite ou do estado da ferramenta) | direta |
| L3-R102 | P2-3.1 | Análise de entidades (nomes próprios) × classificação de conteúdo (categorias aplicáveis ao texto) | PC | Google Cloud, "Analyzing Entities" e "Classifying Content", Cloud Natural Language API ("Last updated 2026-10-13 UTC") (https://cloud.google.com/natural-language/docs/analyzing-entities; https://cloud.google.com/natural-language/docs/classifying-text; verificado em 18/10/2026) | n (definição de recurso; conferência de base em 4–8/1/2027) | direta |
| L3-R103 | P2-3.1 | A habilidade Text Split divide o texto em frases ou em páginas de determinado comprimento, o que serve a limites de tamanho de texto de habilidades posteriores, como as de embeddings | SH | Microsoft Learn, "Text Split skill - Azure AI Search" ("Last updated on 2026-09-17") (https://learn.microsoft.com/en-us/azure/search/cognitive-search-skill-textsplit; verificado em 18/10/2026) | n | direta |
| L3-R104 | P2-3.1 | O conteúdo do knowledge store não é recuperado por consulta do Azure AI Search, ao contrário do conteúdo do índice | D | Microsoft Learn, "Knowledge store in Azure AI Search" ("Last updated on 2026-03-18") (https://learn.microsoft.com/en-us/azure/search/knowledge-store-concept-intro; verificado em 18/10/2026) | VOLÁTIL baixo | direta |
| L3-R105 | P2-4.1 | A exigência de exatidão, clareza, relevância e atualização do dado, conforme a necessidade e a finalidade, é o princípio da qualidade dos dados | AP | LGPD, art. 6º, V (https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm; texto compilado, verificado em 18/10/2026) | n | direta |
| L3-R106 | P2-4.1 | O consentimento é nulo se as informações fornecidas ao titular tiverem conteúdo enganoso ou abusivo ou não tiverem sido apresentadas previamente com transparência | SH | LGPD, art. 9º, § 1º (mesma URL; verificado em 18/10/2026) | n | direta |
| L3-R107 | P2-4.1 | A identidade e as informações de contato do encarregado são divulgadas publicamente, de forma clara e objetiva, preferencialmente no sítio eletrônico do controlador | SH | LGPD, art. 41, § 1º (mesma URL; verificado em 18/10/2026) | n | direta |
| L3-R108 | P2-4.1 | Princípio da não discriminação: impossibilidade de realização do tratamento para fins discriminatórios ilícitos ou abusivos (não se confunde com a prevenção) | SH | LGPD, art. 6º, IX (mesma URL; verificado em 18/10/2026) | n | direta |

=====================================================================
PARTE 2/3 — (d) ITENS DO ESTUDANTE
=====================================================================

Julgue o item.

**L2-R143** (P2-2.2)
No caso de uso da Câmara dos Comuns do Canadá publicado pela União Interparlamentar, quando a tecnologia de reconhecimento automático de fala estiver indisponível ou sua integração com o sistema de informação parlamentar for interrompida, o transcritor transcreve manualmente o segmento de áudio, a partir do áudio e dos metadados, antes de concluir sua tarefa.

**L2-R132** (P2-2.8)
Segundo o caso de uso do sistema de atas literais HANS, do Parlamento da Estônia, publicado pela União Interparlamentar, o modelo de linguagem do sistema de conversão de fala em texto, depois de treinado com material suficiente, não demanda a inclusão de palavras novas nem treinamento adicional.

**L3-R96** (P2-3.1)
Um usuário do sistema de relatórios taquigráficos da Câmara dos Deputados da Itália seleciona o relatório de uma sessão e executa o algoritmo de inteligência artificial descrito em caso de uso publicado pela União Interparlamentar. Nessa situação, o algoritmo gera marcadores (tags) e um resumo breve para o relatório como um todo, sem dividi-lo em seções por assunto.

**L3-R97** (P2-3.1)
No caso de uso do Senado da Itália publicado pela União Interparlamentar, o serviço de inteligência artificial generativa produz o rascunho do relatório-resumo a partir da transcrição de uma sessão do plenário ou de comissão, e cabe ao documentalista, e não ao sistema, revisá-lo e finalizá-lo quanto à exatidão e à completude.

**L3-R98** (P2-3.1)
Considere que um parlamento adote, para as sessões plenárias, o fluxo descrito no caso de uso do sistema HANS, do Parlamento da Estônia, publicado pela União Interparlamentar. Nessa situação, o texto preparado automaticamente pelo sistema é publicado no sítio do parlamento antes da revisão pelos editores, que o corrigem depois de publicado.

**L3-R99** (P2-3.1)
Considere um sistema de relatórios taquigráficos apoiado em inteligência artificial, como o descrito em caso de uso do Conselho de Representantes do Bahrein publicado pela União Interparlamentar, e uma sessão em que a qualidade do áudio seja ruim ou várias pessoas falem ao mesmo tempo. Nessa situação, o sistema sinaliza os trechos da transcrição para revisão manual.

**L3-R100** (P2-3.1)
Nos arquivos de classificação temática das proposições disponibilizados pelo portal Dados Abertos da Câmara dos Deputados, a proposição relacionada a mais de uma área temática aparece em um único registro, que reúne todos os temas a ela associados.

**L3-R101** (P2-3.1)
De acordo com o Manual de Comunicação da Câmara dos Deputados, no uso de inteligência artificial para transcrição e análise de conteúdo, a supervisão humana é dispensável quando a ferramenta apresenta alta precisão.

**L3-R102** (P2-3.1)
Segundo a documentação da Cloud Natural Language API, do Google Cloud, a análise de entidades examina o texto em busca de entidades conhecidas, como nomes próprios de personalidades públicas e de locais, ao passo que a classificação de conteúdo analisa o documento e retorna a lista de categorias que se aplicam ao texto nele encontrado.

**L3-R103** (P2-3.1)
Uma equipe pretende enviar as transcrições de sessões, que são longas, a um modelo de embeddings que impõe tamanho máximo de texto. Nessa situação, de acordo com a documentação do Azure AI Search, a habilidade Text Split pode dividir o texto em frases ou em páginas de determinado comprimento, o que atende a exigências de tamanho máximo de texto de habilidades posteriores, como as que repassam trechos a modelos de embeddings.

**L3-R104** (P2-3.1)
De acordo com a documentação do Azure AI Search, o conteúdo enriquecido por inteligência artificial gravado em um knowledge store, armazenamento secundário no Azure Storage, pode ser recuperado por meio de consultas do próprio Azure AI Search, tal como ocorre com o conteúdo do índice de busca.

**L3-R105** (P2-4.1)
Na transcrição dos pronunciamentos de parlamentares, a exigência de que os dados tratados sejam exatos, claros, relevantes e atualizados, de acordo com a necessidade e para o cumprimento da finalidade do tratamento, decorre do princípio da qualidade dos dados, previsto na Lei Geral de Proteção de Dados Pessoais.

**L3-R106** (P2-4.1)
Um órgão público colhe o consentimento dos participantes de uma audiência para o tratamento de suas falas gravadas, mas as informações previamente fornecidas aos titulares tinham conteúdo enganoso. Nessa situação, segundo a Lei Geral de Proteção de Dados Pessoais, o consentimento é considerado válido enquanto não for revogado pelo titular.

**L3-R107** (P2-4.1)
Um órgão público que contrata serviço de transcrição de audiências indica o encarregado pelo tratamento de dados pessoais. Nessa situação, segundo a Lei Geral de Proteção de Dados Pessoais, a identidade e as informações de contato do encarregado devem ser divulgadas publicamente, de forma clara e objetiva, preferencialmente no sítio eletrônico do controlador.

**L3-R108** (P2-4.1)
Um órgão público utiliza sistema de inteligência artificial para classificar as falas de audiências públicas. Nessa situação, segundo a Lei Geral de Proteção de Dados Pessoais, a impossibilidade de realização do tratamento para fins discriminatórios ilícitos ou abusivos corresponde ao princípio da prevenção.

=====================================================================
PARTE 3/3 — (d-G) GABARITO COMENTADO
=====================================================================

**L2-R143** (P2-2.2) Gabarito: C.
Justificativa: Nos fluxos alternativos, o caso de uso registra: "When automated speech recognition technology is unavailable or its integration with the parliamentary information management system is interrupted, the transcriber/transeditor uses the relevant audio and metadata to manually transcribe the audio segment before completing their task." O item reproduz o fluxo alternativo, sem troca.
Base: UIP, "Automated speech recognition to support the transcription of parliamentary proceedings" (caso de uso 066; autor: Câmara dos Comuns do Canadá; data do caso de uso: 12/07/2024) (https://www.ipu.org/ai-use-cases/automated-speech-recognition-support-transcription-parliamentary-proceedings), verificado em 18/10/2026. Não VOLÁTIL. Formato: AP.
Aderência: DIRETA (contingência humana no fluxo de degravação assistida, 2.2).

**L2-R132** (P2-2.8) Gabarito: E. [TS]
Justificativa: O caso de uso do HANS registra como desafio que "the speech-to-text language model needs to be expanded with new words from time to time, and needs additional training". O item troca a necessidade periódica de novas palavras e de treinamento adicional por dispensa depois do treinamento inicial.
Base: UIP, "AI-powered verbatim records system (HANS)" (caso de uso 016; autor: Riigikogu, Parlamento da Estônia; data do caso de uso: 05/06/2024) (https://www.ipu.org/ai-use-cases/ai-powered-verbatim-records-system-hans), verificado em 18/10/2026. Não VOLÁTIL (conceito de manutenção do vocabulário, estável; reposição direta). Formato: AP.
Aderência: DIRETA (atualização do vocabulário do modelo de linguagem, 2.8).

**L3-R96** (P2-3.1) Gabarito: E. [TS]
Justificativa: O caso de uso descreve que o algoritmo "divides the report into sections based on subjects" e "provides tags and a brief summary for each section". O item troca o tratamento por seção pelo do relatório como um todo.
Base: UIP, "Tags and summaries of parliamentary reports" (caso de uso 012; autor: Departamento de TI da Câmara dos Deputados da Itália; data do caso de uso: 22/05/2024) (https://www.ipu.org/ai-use-cases/tags-and-summaries-parliamentary-reports), verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
Aderência: DIRETA (sumarização e indexação por marcadores de relatório de sessão, 3.1).

**L3-R97** (P2-3.1) Gabarito: C. [TS]
Justificativa: O caso de uso registra: "The AI system generates a draft summary report based on the transcript. The documentalist reviews and finalizes the summary report for accuracy and completeness." O item reproduz o contraste "e não ao sistema" sem trocar os papéis (C espelho: versão verdadeira de uma troca sutil, com o contraste à vista).
Base: UIP, "Creation of draft summary reports based on transcripts of parliamentary sessions" (caso de uso 032; autor: Senado da Itália; data do caso de uso: 12/06/2024) (https://www.ipu.org/ai-use-cases/creation-draft-summary-reports-based-transcripts-parliamentary-sessions), verificado em 18/10/2026. Não VOLÁTIL. Formato: TSj.
Aderência: DIRETA (sumarização de sessões com revisão humana, 3.1).

**L3-R98** (P2-3.1) Gabarito: E. [TS]
Justificativa: Segundo o caso de uso: "Editors review the text prepared by the system and make the necessary corrections; the transcript is then automatically published". A revisão precede a publicação; o item inverte a ordem.
Base: UIP, "AI-powered verbatim records system (HANS)" (caso de uso 016; Riigikogu, Parlamento da Estônia; 05/06/2024) (https://www.ipu.org/ai-use-cases/ai-powered-verbatim-records-system-hans), verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
Aderência: DIRETA (transcrição de sessões plenárias em parlamento, 3.1).

**L3-R99** (P2-3.1) Gabarito: C.
Justificativa: Segundo o caso de uso: "If the audio quality is poor or multiple people are speaking at once, the system flags sections of the transcript for manual review." O item reproduz o fluxo alternativo.
Base: UIP, "Automated Hansard report system: Converting parliamentary audio to text using AI" (caso de uso 062; autor: Conselho de Representantes do Bahrein; data do caso de uso: 06/10/2024) (https://www.ipu.org/ai-use-cases/automated-hansard-report-system-converting-parliamentary-audio-text-using-ai), verificado em 18/10/2026. Não VOLÁTIL. Formato: SH.
Aderência: DIRETA (transcrição de sessões com sinalização de trechos para revisão, 3.1).

**L3-R100** (P2-3.1) Gabarito: E. [TS]
Justificativa: A página dos Dados Abertos descreve a "Classificação temática das proposições": "cada registro corresponde a uma área temática" e, quando a proposição se relaciona a mais de um tema, "os arquivos trazem múltiplas linhas/entradas com os mesmos identificadores da proposição, uma para cada área temática associada à proposição". O item troca as várias linhas por um único registro.
Base: Câmara dos Deputados, Dados Abertos, seção de arquivos "Classificação temática das proposições" (https://dadosabertos.camara.leg.br/swagger/api.html), verificado em 18/10/2026 (a página não exibe data de atualização; os arquivos trazem "Atualização diária"). VOLÁTIL baixo (estrutura de arquivo de portal).
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir a descrição do arquivo de classificação temática (um registro por área temática e múltiplas linhas por proposição). VOLÁTIL baixo, hipótese (b) da D-T96-ONDA2-ACEITE (II). Inapto a simulado final até a reverificação.
Formato: D. Aderência: DIRETA (indexação temática de proposições, 3.1).

**L3-R101** (P2-3.1) Gabarito: E. [TS]
Justificativa: O Manual de Comunicação da Câmara, ao tratar do uso de IA para transcrição e análise, registra: "A supervisão humana é sempre necessária." e inclui a checagem do conteúdo produzido entre os cuidados para evitar informações incorretas. O item troca "sempre necessária" por dispensável diante de alta precisão.
Base: Câmara dos Deputados, Manual de Comunicação, "Uso da inteligência artificial" (https://infograficos.camara.leg.br/manual-de-comunicacao/uso-da-inteligencia-artificial/), verificado em 18/10/2026 (a página não exibe data de publicação ou atualização; lida por ferramenta de leitura de página, pois a requisição direta devolve corpo vazio). Não VOLÁTIL (diretriz de supervisão; o item não afirma nada sobre a ferramenta de transcrição e sumarização em desenvolvimento nem sobre versão, preço ou limite). Formato: D.
Aderência: DIRETA (aplicação de IA em parlamento: transcrição e análise de conteúdo com supervisão humana, 3.1).

**L3-R102** (P2-3.1) Gabarito: C.
Justificativa: "Entity Analysis inspects the given text for known entities (proper nouns such as public figures, landmarks, etc.), and returns information about those entities" e "Content Classification analyzes a document and returns a list of content categories that apply to the text found in the document". O item reproduz o contraste sem trocar os recursos.
Base: Google Cloud, "Analyzing Entities" (https://cloud.google.com/natural-language/docs/analyzing-entities) e "Classifying Content" (https://cloud.google.com/natural-language/docs/classifying-text), Cloud Natural Language API, "Last updated 2026-10-13 UTC", verificado em 18/10/2026. Não VOLÁTIL (definição dos recursos; sem versão, preço ou limite). Formato: PC.
Conferência de base em 4–8/1/2027: reabrir as duas páginas e conferir as definições de análise de entidades e de classificação de conteúdo.
Aderência: DIRETA (extração de entidades e classificação para indexação, 3.1).

**L3-R103** (P2-3.1) Gabarito: C.
Justificativa: "The Text Split skill breaks text into chunks of text. You can specify whether you want to break the text into sentences or into pages of a particular length" e "This skill is useful if there are maximum text length requirements in other skills downstream, such as embedding skills". O item reproduz a função da habilidade.
Base: Microsoft Learn, "Text Split skill - Azure AI Search" ("Last updated on 2026-09-17") (https://learn.microsoft.com/en-us/azure/search/cognitive-search-skill-textsplit), verificado em 18/10/2026. Não VOLÁTIL (conceito de divisão em trechos; sem versão, preço ou limite). Formato: SH.
Aderência: DIRETA (preparação de transcrições para indexação e busca, 3.1).

**L3-R104** (P2-3.1) Gabarito: E. [TS]
Justificativa: "There's no query support in Azure AI Search for retrieving content from a knowledge store." O knowledge store é armazenamento secundário no Azure Storage, ao passo que o índice de busca é consultado pelo serviço. O item afirma o contrário.
Base: Microsoft Learn, "Knowledge store in Azure AI Search" ("Last updated on 2026-03-18") (https://learn.microsoft.com/en-us/azure/search/knowledge-store-concept-intro), verificado em 18/10/2026. VOLÁTIL baixo (capacidade documentada de produto; hipótese (b)).
REVERIFICAR em 4–8/1/2027: reabrir a página e conferir a ausência de suporte a consulta ao knowledge store no Azure AI Search. Inapto a simulado final até a reverificação.
Formato: D.
Aderência: DIRETA (índice de busca × armazenamento do conteúdo enriquecido, 3.1).

**L3-R105** (P2-4.1) Gabarito: C.
Justificativa: LGPD, art. 6º, V: "qualidade dos dados: garantia, aos titulares, de exatidão, clareza, relevância e atualização dos dados, de acordo com a necessidade e para o cumprimento da finalidade de seu tratamento". O item reproduz o princípio e o aplica à transcrição.
Base: Lei nº 13.709/2018, texto compilado do Planalto (https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm), verificado em 18/10/2026. Não VOLÁTIL. Formato: AP. PENDENTE NORMATIVO: ao qa-normativo.
Aderência: DIRETA.

**L3-R106** (P2-4.1) Gabarito: E. [TS]
Justificativa: LGPD, art. 9º, § 1º: "Na hipótese em que o consentimento é requerido, esse será considerado nulo caso as informações fornecidas ao titular tenham conteúdo enganoso ou abusivo ou não tenham sido apresentadas previamente com transparência, de forma clara e inequívoca". O item troca "nulo" por "válido enquanto não revogado".
Base: Lei nº 13.709/2018, texto compilado do Planalto (mesma URL), verificado em 18/10/2026. Não VOLÁTIL. Formato: SH. PENDENTE NORMATIVO: ao qa-normativo.
Aderência: DIRETA.

**L3-R107** (P2-4.1) Gabarito: C.
Justificativa: LGPD, art. 41, § 1º: "A identidade e as informações de contato do encarregado deverão ser divulgadas publicamente, de forma clara e objetiva, preferencialmente no sítio eletrônico do controlador". O item reproduz a regra, sem troca.
Base: Lei nº 13.709/2018, texto compilado do Planalto (mesma URL), verificado em 18/10/2026. Não VOLÁTIL. Formato: SH. PENDENTE NORMATIVO: ao qa-normativo.
Aderência: DIRETA.

**L3-R108** (P2-4.1) Gabarito: E. [TS]
Justificativa: LGPD, art. 6º, IX: "não discriminação: impossibilidade de realização do tratamento para fins discriminatórios ilícitos ou abusivos"; a prevenção é outro princípio (art. 6º, VIII). O item atribui à prevenção o conceito da não discriminação.
Base: Lei nº 13.709/2018, texto compilado do Planalto (https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm), art. 6º, IX, verificado em 18/10/2026. Não VOLÁTIL. Formato: SH. PENDENTE NORMATIVO: ao qa-normativo.
Aderência: DIRETA.

Observações de proveniência: (1) cada página foi baixada em 18/10/2026 (HTTP 200, curl com agente de navegador) e os trechos entre aspas foram conferidos contra o texto baixado; (2) as páginas da UIP não exibem data de atualização, e a data entre parênteses é a do caso de uso; (3) nenhuma afirmação sobre Whisper, Google Speech-to-Text, Azure Speech ou AWS Transcribe; as afirmações sobre Cloud Natural Language API e Azure AI Search são as literais das páginas citadas, sem versão, preço, limite ou região; (4) a LGPD foi lida no texto compilado do Planalto; as redações superadas (art. 20, Lei 15.352/2026) não são usadas; (5) os itens R105 a R108 da 4.1 estão marcados PENDENTE NORMATIVO até o parecer do qa-normativo (QA_T113_normativo_2026-10-18_qa-normativo.md); (6) a v2 inclui o Manual de Comunicação da Câmara (R101), sem data de página; a UIP não é norma nem documento de unidade extinta; os casos de uso são descrição de como um sistema deve funcionar, o que o enunciado de cada item reflete.

FIM DA PARTE 3/3

FIM DO LOTE
