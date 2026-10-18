# L3_reforco_onda4_C_v2.md — T-98 — 2026-10-18 — gerado por gce-cpp

## Resposta ao parecer QA_T98C_R1 (gce-cqfp) e à conferência QA_T98AC_normativo (qa-normativo), item a item

| ponto | resposta | o que foi feito |
|---|---|---|
| R80 (reprovado; gêmeo de L2-R36) | acatado | Item retirado e substituído por item novo, mesmo id, na 4.2: citação de passagens de obra (Lei 9.610/1998, art. 46, III), gabarito C, aplicação parlamentar, não VOLÁTIL. Ponto sem gêmeo no pacote (busca registrada abaixo). |
| R95 (reprovado; gêmeo de L2-R59) | acatado | Item retirado e substituído por item novo, mesmo id, na 4.3: dever de controlador e operador de manter registro das operações de tratamento (LGPD, art. 37), gabarito C, aplicação parlamentar, não VOLÁTIL. Ponto sem gêmeo no pacote. |
| R92 (ajustar) | acatado | Enunciado com o texto exato sugerido pelo parecer ("a autoridade nacional, e não o encarregado, poderá dispor sobre padrões técnicos mínimos para tornar aplicável o dever de os agentes de tratamento adotarem medidas de segurança..."); justificativa e Contagens ajustadas ("e não o encarregado"); [TS] espelho e C mantidos. |
| R76 (ajustar o (d-G)) | acatado | Citação literal corrigida: o art. 14 diz "não podendo opor-se a outra adaptação, arranjo, orquestração ou tradução, salvo se for cópia da sua". Enunciado e gabarito inalterados. |
| R73 (ressalva) | acatado | Registro no (d-G): "coletânea de estudos" pode ser lida como compilação (art. 7º, XIII) e não como obra coletiva (art. 5º, VIII, "h"); o E se sustenta nas duas leituras. Enunciado mantido (a troca "organizador" por "cada participante" vale em ambas). |
| R81 (ressalva) | acatado | Par com L1-R98 registrado (desempenho não uniforme entre grupos; fontes distintas: nota de transparência do Azure × model card do Whisper) e declaração de vizinhança corrigida na seção 1.3 e no (d-G). Recomendação à GBQ: os dois não figuram no mesmo simulado. |
| R89 (ressalva de registro) | acatado | Rodapé "Last updated 2026-10-15 UTC" registrado no (d-G) e na tabela de proveniência. |
| R90 (ressalva de estilo) | acatado, sem alteração | Registrado que "pode apenas recomendar... sem poder determiná-la" é restritivo duplo (estilo_onda_3, rec. 5). A ressalva era opcional; o enunciado fica, pois a troca única é "determinar" por "apenas recomendar". |
| R91 (ressalva de registro) | acatado | Rodapé "Last updated on 2026-08-26" registrado no (d-G) e na tabela de proveniência. VOLÁTIL (b), risco baixo, mantido. |
| R94 (hipótese) | acatado | Hipótese declarada trocada de (d) para (c) (aviso expresso da página; recurso periférico: programa de registro de dados), na tabela do mapa e no (d-G). VOLÁTIL baixo mantido. |
| Conferência normativa: 19 itens de lei federal (R68 a R79, R82, R83, R84, R86, R88, R90, R92) | acatado | Marca PENDENTE NORMATIVO retirada dos 19 (CONFERE). Observação: o R92 mudou de redação conforme o parecer da cqfp; o qa-normativo registrou que item com ponto de troca alterado volta a ele, e o dispositivo (art. 46, § 1º) é o mesmo. R80 e R95, novos e em lei federal, ficam PENDENTE NORMATIVO e QA PENDENTE. |

Busca de gêmeos dos itens novos (por PONTO, não só por frase literal):
- R80 (citação, art. 46, III): lidos todos os itens de P2-4.2 do pacote.json v1.10 (L3-Q22 a Q26 e L3-R09) e os 14 desta parte; busca por "citação", "passagens", "estudo, crítica", "polêmica", "pequenos trechos", "art. 46", "ideias" nos enunciados e justificativas dos 560 itens: nenhum item julga limitações ao direito de autor; "art. 46, III" e "estudo, crítica ou polêmica" só aparecem no texto de curso (GCE_Lote3_v2_CPP.md e campo "curso" do pacote), não em item. Folhas P2-1.x e 2.x (transcrição, degravação, revisão) não tratam de direito autoral. Vizinho declarado: L3-Q22 (art. 29: autorização prévia como regra; o R80 julga a exceção do art. 46, III). Partes A e B da onda 4 (folhas 3.x): sem ponto de direito autoral.
- R95 (registro das operações, art. 37): lidos os 26 itens de P2-4.1, os 6 de P2-4.3 e os itens P2-2.x e 1.x sobre registro, log, trilha e auditoria (L2-Q25, L2-Q26, L2-R106, L2-R112 tratam de auditoria de qualidade, não de registro de operações de tratamento de dados): nenhum julga o art. 37. Busca por "registro das operações", "art. 37", "rastreab", "operador" nos arquivos de reforço e nas partes A e B: sem ocorrência do ponto. Vizinhos declarados: L3-Q18 (quem decide as finalidades: controlador × operador), L3-Q29 (art. 48, caput) e BQ-0077 (relatório de impacto, outro instrumento).
- Script (python3 -I, somente leitura) sobre 1.042 enunciados (560 do pacote e os de reforço e Lotes D1/D6/4): R80 com Jaccard máximo 0,19 e maior sequência literal de 8 palavras; R95 com Jaccard máximo 0,28 (com L3-R11, que julga o término do tratamento, art. 47) e sequência literal de 9 palavras (fórmula de abertura "o tratamento dos dados pessoais"). Abaixo do limiar de 0,30 em ambos.

Lote após a v2: 14 C e 14 E (14/14 restaurado; 4.2 com 7 C e 7 E; 4.3 com 7 C e 7 E); [TS] 18; VOLÁTIL 2 (R91, R94; ambos baixos); aderência direta 28 de 28 (R95 mede o art. 37 como dever de rastreabilidade das operações de tratamento no pipeline de áudio contratado, no capítulo de agentes de tratamento e boas práticas; se a Gerência o julgar apenas parcial, a substituição é o art. 50, § 1º, ou o R95 sai do simulado final, D-ADERENCIA).

Reforço onda 4, parte C (D-REFORCO-2; D-T97-META-FUNDADOR-RESP), Lote 3, P2 itens 4.2 e 4.3. Vinte e oito itens AUTORAL novos, ids L3-R68 a L3-R95 (R68 a R81 na folha 4.2; R82 a R95 na folha 4.3). Nenhum item existente foi alterado. As folhas 3.1 a 3.4 são de outras produtoras (partes A e B da T-98) e não aparecem aqui.

Estado de QA: QA PENDENTE até a R2 da gce-cqfp (D-QA-PENDENTE; item sem QA não entra em simulado). A conferência normativa do qa-normativo (QA_T98AC_normativo_2026-10-18) deu CONFERE nos 19 itens de lei federal da v1 (R68 a R79, R82, R83, R84, R86, R88, R90 e R92); a marca PENDENTE NORMATIVO foi retirada deles. Os itens novos R80 e R95 (lei federal) ficam PENDENTE NORMATIVO.

Contagens de partida: pacote.json v1.10, filtro "P2-4.2" (6 itens: L3-Q22 a Q26 e L3-R09) e "P2-4.3" (6 itens: L3-Q27 a Q30, L3-R10 e L3-R11); todos os 12 estão marcados "direta" no pacote. Cada folha vai de 6 a 20; os diretos vão de 6 a 20 (piso de 10 cumprido com folga). Nomenclatura "Derep (antigo DETAQ)" (Ato da Mesa nº 251/2026): nenhum item a cita.

AVISOS À GERÊNCIA: (1) Todas as bases foram abertas em 18/10/2026 (HTTP 200): planalto.gov.br com User-Agent de navegador (Lei 9.610/1998 e LGPD, texto compilado), docs.aws.amazon.com, docs.cloud.google.com e learn.microsoft.com; nenhuma base usa data anterior (D-FONTE-DATA-ANTERIOR não é invocada). As leis federais dos itens foram lidas por mim; o qa-normativo conferiu os 19 itens da v1 e ainda não conferiu os novos R80 e R95 (abertos por mim em 18/10/2026 com trecho literal); por isso a marca QA PENDENTE. (2) Três páginas redirecionam e a URL citada é a final: cloud.google.com/speech-to-text/docs/data-logging → docs.cloud.google.com/speech-to-text/docs/v1/data-logging; cloud.google.com/vertex-ai/generative-ai/docs/learn/responsible-ai → docs.cloud.google.com/gemini-enterprise-agent-platform/models/responsible-ai; learn.microsoft.com/.../ai-foundry/responsible-ai/... → learn.microsoft.com/.../azure/foundry/responsible-ai/.... (3) Os 7 itens que citam documentação de fornecedor (R81, R85, R87, R89, R91, R93, R94) ficam na lista de conferência de base de 4–8/1/2027 (T-11, parte P2, gce-cqfp); 2 deles são VOLÁTEIS (R91, R94). (4) A pergunta sobre a natureza de conteúdo gerado por IA (titularidade, treinamento, responsabilidade por saídas, aplicação do art. 24, IV a resumo gerado) é controversa e não foi julgada em nenhum item (GCE_Lote3_v2_CPP.md, curso 4.2, "Controverso / não gabarito"); todos os itens de 4.2 julgam o texto da Lei 9.610/1998 ou orientação documentada de fornecedor (R81).

## PARTE 1/3 — Mapa

Convenção de verificação: todas as páginas abaixo foram abertas em 18/10/2026 e o trecho citado foi lido. "L9610" = https://www.planalto.gov.br/ccivil_03/leis/l9610.htm (texto compilado). "LGPD" = https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm (texto compilado). Siglas de fornecedor: AWS-DP = https://docs.aws.amazon.com/transcribe/latest/dg/data-protection.html; AWS-PII = https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html; GCP-RAI = https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/responsible-ai; GCP-LOG = https://docs.cloud.google.com/speech-to-text/docs/v1/data-logging; MS-TN = https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note; MS-DPS = https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/data-privacy-security.

### 1.1 Itens novos

| id | folha | ponto de julgamento | formato | base (verificado em 18/10/2026) | VOLÁTIL | aderência |
|---|---|---|---|---|---|---|
| L3-R68 | P2-4.2 | Autor é a pessoa física criadora da obra; a proteção ao autor só alcança pessoa jurídica nos casos previstos em lei. | definição | L9610, art. 11, caput e parágrafo único | n | direta |
| L3-R69 | P2-4.2 | Para a lei, "reprodução" inclui o armazenamento temporário por meios eletrônicos, e não só o permanente. | definição | L9610, art. 5º, VI | n | direta |
| L3-R70 | P2-4.2 | Obra anônima ou pseudônima: setenta anos contados da primeira publicação (termo inicial diverso do falecimento). | número ou prazo | L9610, art. 43, caput | n | direta |
| L3-R71 | P2-4.2 | Sem estipulação contratual escrita, o prazo máximo da transmissão de direitos de autor é de cinco anos. | número ou prazo | L9610, art. 49, III | n | direta |
| L3-R72 | P2-4.2 | A defesa da integridade e da autoria da obra em domínio público compete ao Estado (não aos sucessores). | troca de sujeito | L9610, art. 24, § 2º | n | direta |
| L3-R73 | P2-4.2 | Em obra coletiva, a titularidade dos direitos patrimoniais sobre o conjunto cabe ao organizador (não a cada participante), que mantém a proteção da participação individual. | troca de sujeito | L9610, art. 17, caput e § 2º; art. 5º, VIII, "h" | n | direta |
| L3-R74 | P2-4.2 | A proteção dos direitos de autor independe de registro da obra (o registro é facultativo). | situação hipotética | L9610, art. 18; art. 19 | n | direta |
| L3-R75 | P2-4.2 | Adquirir exemplar da obra não transfere ao adquirente os direitos patrimoniais do autor (digitalizar e divulgar continua a depender de autorização). | situação hipotética | L9610, art. 37 | n | direta |
| L3-R76 | P2-4.2 | Quem traduz obra em domínio público é titular de direitos sobre a sua tradução, mas não pode opor-se a outra tradução da mesma obra. | troca de sujeito | L9610, art. 14 | n | direta |
| L3-R77 | P2-4.2 | A cessão de direitos só se opera para as modalidades de utilização já existentes à data do contrato. | situação hipotética | L9610, art. 49, V | n | direta |
| L3-R78 | P2-4.2 | A proteção da base de dados como criação intelectual recai sobre a seleção, a organização ou a disposição do conteúdo, e não abrange os dados ou materiais em si. | par confundível (estrutura × conteúdo) | L9610, art. 7º, XIII e § 2º | n | direta |
| L3-R79 | P2-4.2 | Paráfrases e paródias são livres, desde que não sejam verdadeiras reproduções da obra originária nem lhe impliquem descrédito. | par confundível (paráfrase × reprodução) | L9610, art. 47 | n | direta |
| L3-R80 | P2-4.2 | A citação de passagens de qualquer obra, para fins de estudo, crítica ou polêmica, na medida justificada e com indicação do nome do autor e da origem da obra, não constitui ofensa aos direitos autorais. | aplicação parlamentar | L9610, art. 46, III | n | direta |
| L3-R81 | P2-4.2 | Sem esforço consciente, o desempenho de um sistema de IA pode variar entre grupos de pessoas (região, gênero, idade etc.); avaliar por grupos não é dispensável. | aplicação parlamentar | MS-TN, seção "Fairness considerations" | n (conceito documentado; conferência de base em 4–8/1/2027) | direta |
| L3-R82 | P2-4.3 | Tratamento irregular por falta da segurança esperada: as técnicas disponíveis são as da época em que o tratamento foi realizado (não as da apuração do dano). | definição | LGPD, art. 44, caput e III | n | direta |
| L3-R83 | P2-4.3 | Responde pelos danos da violação da segurança o controlador ou o operador que deixou de adotar as medidas do art. 46 e deu causa ao dano. | troca de sujeito | LGPD, art. 44, parágrafo único | n | direta |
| L3-R84 | P2-4.3 | Os sistemas de tratamento devem ser estruturados para atender aos requisitos de segurança, às boas práticas e à governança e aos princípios gerais da lei. | definição | LGPD, art. 49 | n | direta |
| L3-R85 | P2-4.3 | Responsabilidade compartilhada em nuvem: o fornecedor protege a infraestrutura global; o cliente responde pela configuração e pelo gerenciamento de segurança dos serviços que usa. | troca de sujeito | AWS-DP, parágrafo inicial ("shared responsibility model") | n (conceito documentado; conferência de base em 4–8/1/2027) | direta |
| L3-R86 | P2-4.3 | Medida técnica que torna os dados ininteligíveis para terceiros é avaliada no juízo de gravidade do incidente. | situação hipotética | LGPD, art. 48, § 3º | n | direta |
| L3-R87 | P2-4.3 | Não colocar informação confidencial ou sensível em tags e campos de texto livre (como o nome do trabalho), que podem ir a registros de cobrança e de diagnóstico. | aplicação parlamentar | AWS-DP, parágrafo sobre campos de texto livre ("We strongly recommend that you never put confidential or sensitive information...") | n (boa prática documentada; conferência de base em 4–8/1/2027) | direta |
| L3-R88 | P2-4.3 | O programa de governança em privacidade, com planos de resposta a incidentes e remediação, é faculdade ("poderá") do controlador, não dever. | par confundível (faculdade × dever) | LGPD, art. 50, § 2º, I, "g" | n | direta |
| L3-R89 | P2-4.3 | A renderização automática da saída do modelo (Markdown ou HTML) expõe a injeção indireta de prompt e à exfiltração de dados; recomenda-se sanitizar a saída. | situação hipotética | GCP-RAI, seção "Recommended practices" ("Mitigate risks from rendered model output") | n (boa prática documentada; conferência de base em 4–8/1/2027) | direta |
| L3-R90 | P2-4.3 | A autoridade nacional pode determinar (não apenas recomendar) ao controlador providências como a ampla divulgação do incidente. | situação hipotética | LGPD, art. 48, § 2º, I | n | direta |
| L3-R91 | P2-4.3 | Reconhecimento de fala: em tempo real, o áudio é processado só na memória do servidor, sem armazenamento em repouso; em lote, o cliente define o armazenamento e a retenção. | par confundível (tempo real × lote) | MS-DPS, seções "Real-time speech to text" e "Batch transcription" | s (risco baixo; hipótese (b), comportamento de produto) | direta |
| L3-R92 | P2-4.3 | Cabe à autoridade nacional (não ao encarregado) dispor sobre padrões técnicos mínimos para tornar aplicável o dever de segurança. | troca de sujeito | LGPD, art. 46, § 1º | n | direta |
| L3-R93 | P2-4.3 | Menor privilégio: usuários individuais, cada um com só as permissões necessárias às suas funções. | definição | AWS-DP, parágrafo sobre contas e usuários ("set up individual users... only the permissions necessary") | n (boa prática documentada; conferência de base em 4–8/1/2027) | direta |
| L3-R94 | P2-4.3 | No programa de registro de dados do Cloud Speech-to-Text, a exclusão do projeto não exclui os dados registrados (exige pedido de exclusão). | aplicação parlamentar | GCP-LOG, "Data privacy and security" ("Caution: Your logged data is not deleted when you delete your project") | s (risco baixo; hipótese (c), recurso periférico) | direta |
| L3-R95 | P2-4.3 | Controlador e operador devem manter registro das operações de tratamento de dados pessoais que realizarem (rastreabilidade no serviço de transcrição contratado). | aplicação parlamentar | LGPD, art. 37 | n | direta |

### 1.2 Itens existentes por folha (pontos e formatos) e verificação dos tetos

Classificação dos existentes: a da T91_reconciliacao_2026-10-18.md, seção 3.3 (formato definido pela construção do ponto) e a de L3_reforco_onda1_v3.md, seção 1.2. Textos conferidos em saida/pacote/pacote.json v1.10.

P2-4.2 (existentes: 6; novos: 14; folha final: 20)
- L3-Q22: conferências e alocuções são obras protegidas; reprodução e inclusão em base de dados dependem de autorização (arts. 7º, II; 29). Formato: definição.
- L3-Q23: leis, decretos e decisões judiciais não são objeto de proteção (art. 8º, IV). Formato: troca de sujeito.
- L3-Q24: disponível na internet não é domínio público. Formato: situação hipotética.
- L3-Q25: direitos morais inalienáveis; não se transmitem na cessão total (arts. 24, II; 27; 49, I). Formato: par confundível.
- L3-Q26: transparência e revisão humana no uso de IA generativa. Formato: aplicação parlamentar.
- L3-R09: setenta anos do falecimento (art. 41). Formato: número ou prazo.
- Novos: R68 (definição), R69 (definição), R70 (número ou prazo), R71 (número ou prazo), R72 (troca de sujeito), R73 (troca de sujeito), R74 (situação hipotética), R75 (situação hipotética), R76 (troca de sujeito), R77 (situação hipotética), R78 (par confundível), R79 (par confundível), R80 (aplicação parlamentar), R81 (aplicação parlamentar).
- Distribuição final (20): definição 3 (Q22, R68, R69), troca de sujeito 4 (Q23, R72, R73, R76), situação hipotética 4 (Q24, R74, R75, R77), par confundível 3 (Q25, R78, R79), aplicação parlamentar 3 (Q26, R80, R81), número ou prazo 3 (R09, R70, R71). Maior formato: 4/20 = 20%. Teto de 30%: cumprido.
- Gabarito dos novos: 7 C (R68, R71, R74, R76, R77, R79, R80) e 7 E (R69, R70, R72, R73, R75, R78, R81).
- VOLÁTIL: 0/20 (0%). Aderência: 20 diretos de 20 (6 existentes + 14 novos).
- Pontos: nenhum dos 14 repete um dos 6 existentes nem outro dos novos. Os 14 pontos são: art. 11; art. 5º, VI; art. 43; art. 49, III; art. 24, § 2º; art. 17, § 2º; art. 18; art. 37; art. 14; art. 49, V; art. 7º, XIII e § 2º; art. 47; citação de passagens (art. 46, III); equidade entre grupos (MS-TN).

P2-4.3 (existentes: 6; novos: 14; folha final: 20)
- L3-Q27: medidas de segurança técnicas e administrativas, desde a concepção (art. 46, caput e § 2º). Formato: definição.
- L3-Q28: pseudonimização com tabela em poder do órgão não é anonimização. Formato: par confundível.
- L3-Q29: o dever de comunicar incidente é do controlador (art. 48, caput). Formato: troca de sujeito.
- L3-Q30: envio de áudio a servidor no exterior pode ser transferência internacional (art. 33). Formato: aplicação parlamentar.
- L3-R10: prazo da comunicação de incidente definido pela autoridade (art. 48, § 1º). Formato: número ou prazo.
- L3-R11: o dever de segurança persiste após o término do tratamento (art. 47). Formato: situação hipotética.
- Novos: R82 (definição), R83 (troca de sujeito), R84 (definição), R85 (troca de sujeito), R86 (situação hipotética), R87 (aplicação parlamentar), R88 (par confundível), R89 (situação hipotética), R90 (situação hipotética), R91 (par confundível), R92 (troca de sujeito), R93 (definição), R94 (aplicação parlamentar), R95 (aplicação parlamentar).
- Distribuição final (20): definição 4 (Q27, R82, R84, R93), par confundível 3 (Q28, R88, R91), troca de sujeito 4 (Q29, R83, R85, R92), aplicação parlamentar 4 (Q30, R87, R94, R95), número ou prazo 1 (R10), situação hipotética 4 (R11, R86, R89, R90). Maior formato: 4/20 = 20%. Teto de 30%: cumprido.
- Gabarito dos novos: 7 C (R84, R86, R87, R89, R92, R93, R95) e 7 E (R82, R83, R85, R88, R90, R91, R94).
- VOLÁTIL: 2/20 (10%): R91, R94; nenhum de risco alto. Teto de 20%: cumprido.
- Aderência: 20 diretos de 20 (6 existentes + 14 novos).
- Pontos: nenhum dos 14 repete um dos 6 existentes nem outro dos novos. Os 14 pontos são: art. 44, caput e III; art. 44, parágrafo único; art. 49; responsabilidade compartilhada (AWS-DP); art. 48, § 3º; campos de texto livre (AWS-DP); art. 50, § 2º, I, "g"; renderização da saída do modelo (GCP-RAI); art. 48, § 2º; retenção em tempo real × lote (MS-DPS); art. 46, § 1º; menor privilégio (AWS-DP); exclusão do projeto e dados registrados (GCP-LOG); registro das operações de tratamento (art. 37).

### 1.3 Totais, conferências e vizinhanças

- Totais da parte C: 28 itens (14 em 4.2; 14 em 4.3); 14 C e 14 E (50,0%, dentro de 40–60%; 7/7 em cada folha); [TS] 18 (4.2: R69, R70, R72, R73, R75, R78, R81 em E e R76, R77 em C espelho = 9; 4.3: R82, R83, R85, R88, R90, R91, R94 em E e R84, R92 em C espelho = 9); VOLÁTIL 2 (ambos em 4.3); aderência direta 28 de 28.
- Conferência de pontos contra o pacote (script, python3 -I, somente leitura): a frase-base de cada um dos 28 enunciados foi comparada a todos os enunciados de saida/pacote/pacote.json v1.10 (560 itens) e aos 12 arquivos saida/gce/*reforco*.md; resultado na seção "Contagens" da Parte 3. Na v2, a comparação dos itens novos R80 e R95 foi feita também por PONTO (leitura dos itens das folhas P2-1.x, 2.x e 4.x e Jaccard); busca registrada na resposta ao parecer, no topo.
- Pontos de LGPD contra a P2-4.1 (26 itens), o Lote 4 e o D6 (saida/gcb/D6_v2_1.md): a 4.1 não usa os arts. 44, 46, § 1º, 48, §§ 2º e 3º, 49 nem 50; o D6 usa o art. 48, caput (D6-48), o art. 6º, VII e VIII (D6-36) e o art. 41, § 2º, mas nenhum dos pontos de R82 a R92; o Lote 4 só tem L4-17 (anonimização) e L4-19 (responsabilidade pelo conteúdo, ética), sem relação com os pontos novos.
- Vizinhanças declaradas (pontos distintos, mesmo artigo ou tema; sem gêmeo): R70 × L3-R09 (art. 43 × art. 41: termo inicial diverso); R72 × L3-Q24 (defesa da integridade × equivalência com a internet); R75 × L3-Q22 (aquisição de exemplar × autorização para reprodução); R77 × L3-Q25 (art. 49, V × art. 49, I); R78 × L3-Q22 (art. 7º, XIII × art. 29, IX); R80 × L3-Q22 (art. 46, III: citação como limitação × art. 29: autorização prévia como regra); R81 × L2-R35, L2-R40 e L2-R43 (mesma nota de transparência do Azure Speech, outras seções); R81 × L1-R98 (P2-1.6): par declarado, com o mesmo juízo de fundo (desempenho não uniforme entre grupos), fontes distintas (nota de transparência do Azure × model card do Whisper, sotaques) e ângulo de equidade próprio da 4.2; recomenda-se à GBQ que não figurem no mesmo simulado; R82 e R84 × L3-Q27 (art. 44 e art. 49 × art. 46); R86 e R90 × L3-R10, L3-Q29 e D6-48 (art. 48, §§ 3º e 2º × § 1º e caput); R89 × 4C-08 (saída renderizada × definição de injeção de prompt); R91 × L1-Q19 e L1-Q20 (retenção por modo × execução local e custódia); R92 × L3-Q27 (art. 46, § 1º × caput e § 2º); R93 × itens de segurança da P1 (menor privilégio não tem item na P1); R95 × L3-Q18 (finalidades: controlador × operador; o R95 julga o registro das operações), L3-Q29 (art. 48, caput) e BQ-0077 (relatório de impacto, outro instrumento).
- Instruções das reconciliações cumpridas: T96, seção 4 (conferência contra o pacote inteiro, gêmeos só declarados); T97, seção 3.4 (item novo de folha com menos de 12 diretos é direto); T91, seção 3.3 (teto medido com os canônicos); estilo_onda_3, seção 5 (equilibrar ", e não", "independentemente" e "Segundo"; concessiva também em E; um restritivo por item; cenário que pesa no juízo; "da Câmara dos Deputados" no lugar de "da Casa").
- Fora do escopo desta parte: as folhas 3.1 a 3.4 (outras produtoras).

FIM DA PARTE 1/3

## PARTE 2/3 — (d) Itens do estudante

Julgue o item.

**L3-R68** (P2-4.2)
A Lei n.º 9.610/1998 considera autor a pessoa física criadora de obra literária, artística ou científica, ainda que a proteção concedida ao autor possa aplicar-se a pessoas jurídicas nos casos previstos na própria lei.

**L3-R69** (P2-4.2)
Segundo a Lei n.º 9.610/1998, a reprodução da obra consiste na cópia de exemplares em qualquer forma tangível e compreende o armazenamento permanente, mas não o armazenamento temporário por meios eletrônicos.

**L3-R70** (P2-4.2)
Segundo a Lei n.º 9.610/1998, o prazo de proteção aos direitos patrimoniais sobre as obras anônimas ou pseudônimas é de setenta anos, a contar do falecimento do autor.

**L3-R71** (P2-4.2)
Segundo a Lei n.º 9.610/1998, quando a transferência dos direitos de autor a terceiros não for objeto de estipulação contratual escrita, o prazo máximo da transmissão será de cinco anos.

**L3-R72** (P2-4.2)
De acordo com a Lei n.º 9.610/1998, a defesa da integridade e da autoria da obra caída em domínio público compete aos sucessores do autor, e não ao Estado.

**L3-R73** (P2-4.2)
Considere que a Câmara dos Deputados publique, sob a sua marca, uma coletânea de estudos com a participação de diversos autores. Nessa situação, segundo a Lei n.º 9.610/1998, a titularidade dos direitos patrimoniais sobre o conjunto da obra cabe a cada participante, a quem é assegurada, ainda, a proteção de sua participação individual.

**L3-R74** (P2-4.2)
Um professor universitário escreveu artigo inédito sobre o uso de inteligência artificial na transcrição de sessões legislativas e não o registrou em órgão público. Nessa situação, segundo a Lei n.º 9.610/1998, a proteção aos direitos de autor sobre o artigo existe independentemente de registro.

**L3-R75** (P2-4.2)
A Câmara dos Deputados adquiriu, para a sua biblioteca, exemplares de um livro de autor vivo e pretende digitalizá-los e disponibilizá-los em seu portal. Nessa situação, de acordo com a Lei n.º 9.610/1998, a aquisição dos exemplares conferiu à Câmara os direitos patrimoniais sobre a obra, o que torna desnecessária a autorização do autor para a digitalização e a divulgação.

**L3-R76** (P2-4.2)
Segundo a Lei n.º 9.610/1998, quem traduz obra caída em domínio público é titular de direitos de autor sobre a sua tradução, mas não pode opor-se a que outra pessoa faça nova tradução da mesma obra.

**L3-R77** (P2-4.2)
Em 1999, um autor cedeu a um editor, por contrato escrito, os direitos de utilização de sua obra, sem mencionar formas de utilização que ainda não existiam. Nessa situação, segundo a Lei n.º 9.610/1998, a cessão somente se operou para as modalidades de utilização já existentes à data do contrato.

**L3-R78** (P2-4.2)
Uma base de dados cuja seleção e organização do conteúdo constituam criação intelectual é obra protegida pela Lei n.º 9.610/1998, e essa proteção abrange os dados ou materiais nela contidos, considerados em si mesmos.

**L3-R79** (P2-4.2)
A Lei n.º 9.610/1998 distingue a paráfrase da reprodução: são livres as paráfrases e as paródias que não forem verdadeiras reproduções da obra originária nem lhe implicarem descrédito.

**L3-R80** (P2-4.2)
Uma unidade da Câmara dos Deputados elabora estudo técnico sobre o uso de inteligência artificial na transcrição de sessões e pretende citar passagens de artigos de terceiros. Nessa situação, segundo a Lei n.º 9.610/1998, a citação dessas passagens não constitui ofensa aos direitos autorais se for feita para fins de estudo, crítica ou polêmica, na medida justificada para o fim a atingir, com a indicação do nome do autor e da origem da obra.

**L3-R81** (P2-4.2)
Conforme a nota de transparência do Azure Speech, o desempenho de um sistema de IA como o de reconhecimento de fala é uniforme entre grupos de pessoas, ainda que não haja esforço consciente voltado a melhorá-lo para todos os grupos, razão pela qual a avaliação do sistema usado nas sessões da Câmara dos Deputados dispensa a verificação por grupos de oradores.

**L3-R82** (P2-4.3)
Segundo a Lei Geral de Proteção de Dados Pessoais, o tratamento de dados pessoais é irregular quando não fornece a segurança que o titular dele pode esperar, consideradas circunstâncias como o modo pelo qual é realizado, o resultado e os riscos que razoavelmente dele se esperam e as técnicas de tratamento disponíveis à época em que o dano foi apurado.

**L3-R83** (P2-4.3)
Segundo a Lei Geral de Proteção de Dados Pessoais, responde pelos danos decorrentes da violação da segurança dos dados apenas o controlador que deixe de adotar as medidas de segurança previstas na lei, ainda que o operador, ao não as adotar, tenha dado causa ao dano.

**L3-R84** (P2-4.3)
Segundo a Lei Geral de Proteção de Dados Pessoais, os sistemas utilizados para o tratamento de dados pessoais, como os de transcrição de sessões, devem ser estruturados de forma a atender não apenas aos requisitos de segurança, mas também aos padrões de boas práticas e de governança e aos princípios gerais previstos na lei.

**L3-R85** (P2-4.3)
Segundo a documentação do Amazon Transcribe, pelo modelo de responsabilidade compartilhada, a AWS protege a infraestrutura global que executa a nuvem e também responde pelas tarefas de configuração e de gerenciamento de segurança dos serviços que o cliente utiliza.

**L3-R86** (P2-4.3)
Terceiros não autorizados acessaram arquivos de áudio de reuniões de comissão armazenados por um órgão, mas o controlador comprova que os arquivos estavam cifrados, de modo que os dados pessoais se tornaram ininteligíveis para quem os acessou. Nessa situação, segundo a Lei Geral de Proteção de Dados Pessoais, essa comprovação será avaliada no juízo de gravidade do incidente.

**L3-R87** (P2-4.3)
Uma unidade da Câmara dos Deputados cria trabalhos de transcrição no Amazon Transcribe. Segundo a documentação do serviço, recomenda-se que informações confidenciais ou sensíveis, como dados pessoais de participantes de uma audiência, não sejam inseridas em tags nem em campos de texto livre, como o campo de nome, porque esses campos podem ser usados em registros de cobrança ou de diagnóstico.

**L3-R88** (P2-4.3)
Segundo a Lei Geral de Proteção de Dados Pessoais, o controlador é obrigado a implementar programa de governança em privacidade que contenha, entre outros requisitos, planos de resposta a incidentes e remediação.

**L3-R89** (P2-4.3)
Um painel da Câmara dos Deputados exibe automaticamente, em formato Markdown ou HTML, resumos de sessões gerados por modelo de linguagem. Nessa situação, segundo as orientações de IA responsável do Google Cloud, a renderização automática da saída do modelo pode expor o painel a injeção indireta de prompt e à exfiltração de dados, e recomenda-se sanitizar a saída antes de exibi-la.

**L3-R90** (P2-4.3)
Verificada a gravidade de incidente de segurança que lhe foi comunicado, a autoridade nacional pode apenas recomendar ao controlador a ampla divulgação do fato em meios de comunicação, sem poder determiná-la, segundo a Lei Geral de Proteção de Dados Pessoais.

**L3-R91** (P2-4.3)
Segundo a documentação da Microsoft sobre dados e privacidade do reconhecimento de fala, na transcrição em lote o áudio é processado apenas na memória do servidor do Azure, sem armazenamento em repouso, enquanto na transcrição em tempo real o cliente indica o local de armazenamento do áudio e do texto gerado e controla a sua retenção.

**L3-R92** (P2-4.3)
Segundo a Lei Geral de Proteção de Dados Pessoais, a autoridade nacional, e não o encarregado, poderá dispor sobre padrões técnicos mínimos para tornar aplicável o dever de os agentes de tratamento adotarem medidas de segurança, considerados a natureza das informações tratadas, as características específicas do tratamento e o estado atual da tecnologia.

**L3-R93** (P2-4.3)
Segundo a documentação do Amazon Transcribe, recomenda-se configurar usuários individuais para acessar o serviço, de modo que cada um receba apenas as permissões necessárias ao cumprimento de suas funções.

**L3-R94** (P2-4.3)
Uma unidade da Câmara dos Deputados aderiu, em um projeto do Google Cloud Speech-to-Text, ao programa de registro de dados e, ao final de um teste com áudios de reuniões, excluiu o projeto. Nessa situação, segundo a documentação do serviço, a exclusão do projeto bastou para que os dados registrados também fossem excluídos, sem necessidade de pedido específico de exclusão ao Google.

**L3-R95** (P2-4.3)
Uma unidade da Câmara dos Deputados contratou empresa para transcrever, em serviço de nuvem, os áudios de reuniões de comissão, e a contratada realiza o tratamento dos dados pessoais em nome da Câmara. Nessa situação, segundo a Lei Geral de Proteção de Dados Pessoais, tanto o controlador quanto o operador devem manter registro das operações de tratamento de dados pessoais que realizarem.

FIM DA PARTE 2/3

## PARTE 3/3 — (d-G) Gabarito comentado

**L3-R68** (P2-4.2) Gabarito: C.
Justificativa: Lei 9.610/1998, art. 11: "Autor é a pessoa física criadora de obra literária, artística ou científica"; parágrafo único: a proteção ao autor "poderá aplicar-se às pessoas jurídicas nos casos previstos nesta Lei". O item reproduz a regra e a exceção.
Base: Lei 9.610/1998, art. 11, planalto.gov.br (https://www.planalto.gov.br/ccivil_03/leis/l9610.htm), texto compilado, verificado em 18/10/2026. Sem [TS]. Não VOLÁTIL.
Aderência: direta.

**L3-R69** (P2-4.2) Gabarito: E. [TS]
Justificativa: art. 5º, VI: reprodução é a cópia "de qualquer forma tangível, incluindo qualquer armazenamento permanente ou temporário por meios eletrônicos". O item exclui o armazenamento temporário.
Base: Lei 9.610/1998, art. 5º, VI, planalto.gov.br (mesma URL), verificado em 18/10/2026. Não VOLÁTIL.
Aderência: direta.

**L3-R70** (P2-4.2) Gabarito: E. [TS]
Justificativa: art. 43: nas obras anônimas ou pseudônimas, setenta anos "contado de 1° de janeiro do ano imediatamente posterior ao da primeira publicação". O item troca a primeira publicação pelo falecimento do autor (termo do art. 41).
Base: Lei 9.610/1998, art. 43, caput, planalto.gov.br (mesma URL), verificado em 18/10/2026. Vizinho de L3-R09 (art. 41), com termo inicial diverso. Não VOLÁTIL.
Aderência: direta.

**L3-R71** (P2-4.2) Gabarito: C.
Justificativa: art. 49, III: "na hipótese de não haver estipulação contratual escrita, o prazo máximo será de cinco anos". O item reproduz a regra.
Base: Lei 9.610/1998, art. 49, III, planalto.gov.br (mesma URL), verificado em 18/10/2026. Sem [TS]. Não VOLÁTIL.
Aderência: direta.

**L3-R72** (P2-4.2) Gabarito: E. [TS]
Justificativa: art. 24, § 2º: "Compete ao Estado a defesa da integridade e autoria da obra caída em domínio público". O item troca o Estado pelos sucessores do autor.
Base: Lei 9.610/1998, art. 24, § 2º, planalto.gov.br (mesma URL), verificado em 18/10/2026. Não VOLÁTIL.
Aderência: direta.

**L3-R73** (P2-4.2) Gabarito: E. [TS]
Justificativa: art. 17, § 2º: "Cabe ao organizador a titularidade dos direitos patrimoniais sobre o conjunto da obra coletiva"; o caput assegura a proteção das participações individuais. O item troca o organizador por cada participante, e só a segunda oração é correta.
Base: Lei 9.610/1998, art. 17, caput e § 2º, e art. 5º, VIII, "h" (obra coletiva), planalto.gov.br (mesma URL), verificado em 18/10/2026. Não VOLÁTIL. Registro (parecer R1): "coletânea de estudos" pode ser lida como compilação (art. 7º, XIII) e não como obra coletiva (art. 5º, VIII, "h", que exige a fusão das contribuições); o E se sustenta nas duas leituras, porque a titularidade do conjunto não cabe a cada participante em nenhuma delas.
Aderência: direta.

**L3-R74** (P2-4.2) Gabarito: C.
Justificativa: art. 18: "A proteção aos direitos de que trata esta Lei independe de registro"; o art. 19 apenas faculta ao autor registrar a obra. A ausência de registro não afasta a proteção.
Base: Lei 9.610/1998, arts. 18 e 19, planalto.gov.br (mesma URL), verificado em 18/10/2026. Sem [TS]. Não VOLÁTIL.
Aderência: direta.

**L3-R75** (P2-4.2) Gabarito: E. [TS]
Justificativa: art. 37: a aquisição do original ou de exemplar "não confere ao adquirente qualquer dos direitos patrimoniais do autor, salvo convenção em contrário entre as partes e os casos previstos nesta Lei". O item afirma que a aquisição transferiu os direitos e dispensa a autorização do autor.
Base: Lei 9.610/1998, art. 37, planalto.gov.br (mesma URL), verificado em 18/10/2026. Vizinho de L3-Q22 (autorização para reprodução). Não VOLÁTIL.
Aderência: direta.

**L3-R76** (P2-4.2) Gabarito: C. [TS] (espelho)
Justificativa: art. 14: é titular de direitos de autor quem traduz obra caída no domínio público, "não podendo opor-se a outra adaptação, arranjo, orquestração ou tradução, salvo se for cópia da sua". O item reproduz as duas metades ("mas não pode opor-se"); a ressalva da cópia não é julgada.
Base: Lei 9.610/1998, art. 14, planalto.gov.br (mesma URL), verificado em 18/10/2026. Não VOLÁTIL.
Aderência: direta.

**L3-R77** (P2-4.2) Gabarito: C. [TS] (espelho)
Justificativa: art. 49, V: "a cessão só se operará para modalidades de utilização já existentes à data do contrato". O item aplica a regra; "somente" traduz o "só" da lei, sem exceder o texto.
Base: Lei 9.610/1998, art. 49, V, planalto.gov.br (mesma URL), verificado em 18/10/2026. Vizinho de L3-Q25 (art. 49, I). Não VOLÁTIL. O item não afirma nada sobre IA.
Aderência: direta.

**L3-R78** (P2-4.2) Gabarito: E. [TS]
Justificativa: art. 7º, XIII: a base de dados é obra protegida quando, "por sua seleção, organização ou disposição de seu conteúdo", constitui criação intelectual; § 2º: a proteção "não abarca os dados ou materiais em si mesmos". O item estende a proteção aos dados.
Base: Lei 9.610/1998, art. 7º, XIII e § 2º, planalto.gov.br (mesma URL), verificado em 18/10/2026. Vizinho de L3-Q22 (art. 29, IX). Não VOLÁTIL.
Aderência: direta.

**L3-R79** (P2-4.2) Gabarito: C.
Justificativa: art. 47: "São livres as paráfrases e paródias que não forem verdadeiras reproduções da obra originária nem lhe implicarem descrédito". O item reproduz o limite da liberdade (reprodução e descrédito).
Base: Lei 9.610/1998, art. 47, planalto.gov.br (mesma URL), verificado em 18/10/2026. Sem [TS]. Não VOLÁTIL.
Aderência: direta.

**L3-R80** (P2-4.2) Gabarito: C.
Justificativa: art. 46, III: não constitui ofensa aos direitos autorais "a citação em livros, jornais, revistas ou qualquer outro meio de comunicação, de passagens de qualquer obra, para fins de estudo, crítica ou polêmica, na medida justificada para o fim a atingir, indicando-se o nome do autor e a origem da obra". O item reproduz as condições da citação (finalidade, medida justificada, indicação de autor e origem).
Base: Lei 9.610/1998, art. 46, III, planalto.gov.br (https://www.planalto.gov.br/ccivil_03/leis/l9610.htm), texto compilado, verificado em 18/10/2026 (HTTP 200; User-Agent de navegador; trecho literal conferido no texto baixado hoje). Sem [TS]. Não VOLÁTIL. Vizinho de L3-Q22 (art. 29: autorização prévia como regra; o R80 julga a limitação do art. 46, III). Sem gêmeo no pacote (busca por ponto registrada no topo). O item não afirma nada sobre conteúdo gerado por IA nem sobre treinamento de modelos.
Aderência: direta. QA PENDENTE; PENDENTE NORMATIVO.

**L3-R81** (P2-4.2)
Conforme a nota de transparência do Azure Speech, o desempenho de um sistema de IA como o de reconhecimento de fala é uniforme entre grupos de pessoas, ainda que não haja esforço consciente voltado a melhorá-lo para todos os grupos, razão pela qual a avaliação do sistema usado nas sessões da Câmara dos Deputados dispensa a verificação por grupos de oradores.

**L3-R82** (P2-4.3)
Segundo a Lei Geral de Proteção de Dados Pessoais, o tratamento de dados pessoais é irregular quando não fornece a segurança que o titular dele pode esperar, consideradas circunstâncias como o modo pelo qual é realizado, o resultado e os riscos que razoavelmente dele se esperam e as técnicas de tratamento disponíveis à época em que o dano foi apurado.

**L3-R83** (P2-4.3)
Segundo a Lei Geral de Proteção de Dados Pessoais, responde pelos danos decorrentes da violação da segurança dos dados apenas o controlador que deixe de adotar as medidas de segurança previstas na lei, ainda que o operador, ao não as adotar, tenha dado causa ao dano.

**L3-R84** (P2-4.3)
Segundo a Lei Geral de Proteção de Dados Pessoais, os sistemas utilizados para o tratamento de dados pessoais, como os de transcrição de sessões, devem ser estruturados de forma a atender não apenas aos requisitos de segurança, mas também aos padrões de boas práticas e de governança e aos princípios gerais previstos na lei.

**L3-R85** (P2-4.3)
Segundo a documentação do Amazon Transcribe, pelo modelo de responsabilidade compartilhada, a AWS protege a infraestrutura global que executa a nuvem e também responde pelas tarefas de configuração e de gerenciamento de segurança dos serviços que o cliente utiliza.

**L3-R86** (P2-4.3)
Terceiros não autorizados acessaram arquivos de áudio de reuniões de comissão armazenados por um órgão, mas o controlador comprova que os arquivos estavam cifrados, de modo que os dados pessoais se tornaram ininteligíveis para quem os acessou. Nessa situação, segundo a Lei Geral de Proteção de Dados Pessoais, essa comprovação será avaliada no juízo de gravidade do incidente.

**L3-R87** (P2-4.3)
Uma unidade da Câmara dos Deputados cria trabalhos de transcrição no Amazon Transcribe. Segundo a documentação do serviço, recomenda-se que informações confidenciais ou sensíveis, como dados pessoais de participantes de uma audiência, não sejam inseridas em tags nem em campos de texto livre, como o campo de nome, porque esses campos podem ser usados em registros de cobrança ou de diagnóstico.

**L3-R88** (P2-4.3)
Segundo a Lei Geral de Proteção de Dados Pessoais, o controlador é obrigado a implementar programa de governança em privacidade que contenha, entre outros requisitos, planos de resposta a incidentes e remediação.

**L3-R89** (P2-4.3)
Um painel da Câmara dos Deputados exibe automaticamente, em formato Markdown ou HTML, resumos de sessões gerados por modelo de linguagem. Nessa situação, segundo as orientações de IA responsável do Google Cloud, a renderização automática da saída do modelo pode expor o painel a injeção indireta de prompt e à exfiltração de dados, e recomenda-se sanitizar a saída antes de exibi-la.

**L3-R90** (P2-4.3)
Verificada a gravidade de incidente de segurança que lhe foi comunicado, a autoridade nacional pode apenas recomendar ao controlador a ampla divulgação do fato em meios de comunicação, sem poder determiná-la, segundo a Lei Geral de Proteção de Dados Pessoais.

**L3-R91** (P2-4.3)
Segundo a documentação da Microsoft sobre dados e privacidade do reconhecimento de fala, na transcrição em lote o áudio é processado apenas na memória do servidor do Azure, sem armazenamento em repouso, enquanto na transcrição em tempo real o cliente indica o local de armazenamento do áudio e do texto gerado e controla a sua retenção.

**L3-R92** (P2-4.3)
Segundo a Lei Geral de Proteção de Dados Pessoais, a autoridade nacional, e não o encarregado, poderá dispor sobre padrões técnicos mínimos para tornar aplicável o dever de os agentes de tratamento adotarem medidas de segurança, considerados a natureza das informações tratadas, as características específicas do tratamento e o estado atual da tecnologia.

**L3-R93** (P2-4.3)
Segundo a documentação do Amazon Transcribe, recomenda-se configurar usuários individuais para acessar o serviço, de modo que cada um receba apenas as permissões necessárias ao cumprimento de suas funções.

**L3-R94** (P2-4.3)
Uma unidade da Câmara dos Deputados aderiu, em um projeto do Google Cloud Speech-to-Text, ao programa de registro de dados e, ao final de um teste com áudios de reuniões, excluiu o projeto. Nessa situação, segundo a documentação do serviço, a exclusão do projeto bastou para que os dados registrados também fossem excluídos, sem necessidade de pedido específico de exclusão ao Google.

**L3-R95** (P2-4.3)
Uma unidade da Câmara dos Deputados contratou empresa para transcrever, em serviço de nuvem, os áudios de reuniões de comissão, e a contratada realiza o tratamento dos dados pessoais em nome da Câmara. Nessa situação, segundo a Lei Geral de Proteção de Dados Pessoais, tanto o controlador quanto o operador devem manter registro das operações de tratamento de dados pessoais que realizarem.

FIM DA PARTE 2/3

## PARTE 3/3 — (d-G) Gabarito comentado

**L3-R68** (P2-4.2) Gabarito: C.
Justificativa: Lei 9.610/1998, art. 11: "Autor é a pessoa física criadora de obra literária, artística ou científica"; parágrafo único: a proteção ao autor "poderá aplicar-se às pessoas jurídicas nos casos previstos nesta Lei". O item reproduz a regra e a exceção.
Base: Lei 9.610/1998, art. 11, planalto.gov.br (https://www.planalto.gov.br/ccivil_03/leis/l9610.htm), texto compilado, verificado em 18/10/2026. Sem [TS]. Não VOLÁTIL.
Aderência: direta.

**L3-R69** (P2-4.2) Gabarito: E. [TS]
Justificativa: art. 5º, VI: reprodução é a cópia "de qualquer forma tangível, incluindo qualquer armazenamento permanente ou temporário por meios eletrônicos". O item exclui o armazenamento temporário.
Base: Lei 9.610/1998, art. 5º, VI, planalto.gov.br (mesma URL), verificado em 18/10/2026. Não VOLÁTIL.
Aderência: direta.

**L3-R70** (P2-4.2) Gabarito: E. [TS]
Justificativa: art. 43: nas obras anônimas ou pseudônimas, setenta anos "contado de 1° de janeiro do ano imediatamente posterior ao da primeira publicação". O item troca a primeira publicação pelo falecimento do autor (termo do art. 41).
Base: Lei 9.610/1998, art. 43, caput, planalto.gov.br (mesma URL), verificado em 18/10/2026. Vizinho de L3-R09 (art. 41), com termo inicial diverso. Não VOLÁTIL.
Aderência: direta.

**L3-R71** (P2-4.2) Gabarito: C.
Justificativa: art. 49, III: "na hipótese de não haver estipulação contratual escrita, o prazo máximo será de cinco anos". O item reproduz a regra.
Base: Lei 9.610/1998, art. 49, III, planalto.gov.br (mesma URL), verificado em 18/10/2026. Sem [TS]. Não VOLÁTIL.
Aderência: direta.

**L3-R72** (P2-4.2) Gabarito: E. [TS]
Justificativa: art. 24, § 2º: "Compete ao Estado a defesa da integridade e autoria da obra caída em domínio público". O item troca o Estado pelos sucessores do autor.
Base: Lei 9.610/1998, art. 24, § 2º, planalto.gov.br (mesma URL), verificado em 18/10/2026. Não VOLÁTIL.
Aderência: direta.

**L3-R73** (P2-4.2) Gabarito: E. [TS]
Justificativa: art. 17, § 2º: "Cabe ao organizador a titularidade dos direitos patrimoniais sobre o conjunto da obra coletiva"; o caput assegura a proteção das participações individuais. O item troca o organizador por cada participante, e só a segunda oração é correta.
Base: Lei 9.610/1998, art. 17, caput e § 2º, e art. 5º, VIII, "h" (obra coletiva), planalto.gov.br (mesma URL), verificado em 18/10/2026. Não VOLÁTIL. Registro (parecer R1): "coletânea de estudos" pode ser lida como compilação (art. 7º, XIII) e não como obra coletiva (art. 5º, VIII, "h", que exige a fusão das contribuições); o E se sustenta nas duas leituras, porque a titularidade do conjunto não cabe a cada participante em nenhuma delas.
Aderência: direta.

**L3-R74** (P2-4.2) Gabarito: C.
Justificativa: art. 18: "A proteção aos direitos de que trata esta Lei independe de registro"; o art. 19 apenas faculta ao autor registrar a obra. A ausência de registro não afasta a proteção.
Base: Lei 9.610/1998, arts. 18 e 19, planalto.gov.br (mesma URL), verificado em 18/10/2026. Sem [TS]. Não VOLÁTIL.
Aderência: direta.

**L3-R75** (P2-4.2) Gabarito: E. [TS]
Justificativa: art. 37: a aquisição do original ou de exemplar "não confere ao adquirente qualquer dos direitos patrimoniais do autor, salvo convenção em contrário entre as partes e os casos previstos nesta Lei". O item afirma que a aquisição transferiu os direitos e dispensa a autorização do autor.
Base: Lei 9.610/1998, art. 37, planalto.gov.br (mesma URL), verificado em 18/10/2026. Vizinho de L3-Q22 (autorização para reprodução). Não VOLÁTIL.
Aderência: direta.

**L3-R76** (P2-4.2) Gabarito: C. [TS] (espelho)
Justificativa: art. 14: é titular de direitos de autor quem traduz obra caída no domínio público, "não podendo opor-se a outra adaptação, arranjo, orquestração ou tradução, salvo se for cópia da sua". O item reproduz as duas metades ("mas não pode opor-se"); a ressalva da cópia não é julgada.
Base: Lei 9.610/1998, art. 14, planalto.gov.br (mesma URL), verificado em 18/10/2026. Não VOLÁTIL.
Aderência: direta.

**L3-R77** (P2-4.2) Gabarito: C. [TS] (espelho)
Justificativa: art. 49, V: "a cessão só se operará para modalidades de utilização já existentes à data do contrato". O item aplica a regra; "somente" traduz o "só" da lei, sem exceder o texto.
Base: Lei 9.610/1998, art. 49, V, planalto.gov.br (mesma URL), verificado em 18/10/2026. Vizinho de L3-Q25 (art. 49, I). Não VOLÁTIL. O item não afirma nada sobre IA.
Aderência: direta.

**L3-R78** (P2-4.2) Gabarito: E. [TS]
Justificativa: art. 7º, XIII: a base de dados é obra protegida quando, "por sua seleção, organização ou disposição de seu conteúdo", constitui criação intelectual; § 2º: a proteção "não abarca os dados ou materiais em si mesmos". O item estende a proteção aos dados.
Base: Lei 9.610/1998, art. 7º, XIII e § 2º, planalto.gov.br (mesma URL), verificado em 18/10/2026. Vizinho de L3-Q22 (art. 29, IX). Não VOLÁTIL.
Aderência: direta.

**L3-R79** (P2-4.2) Gabarito: C.
Justificativa: art. 47: "São livres as paráfrases e paródias que não forem verdadeiras reproduções da obra originária nem lhe implicarem descrédito". O item reproduz o limite da liberdade (reprodução e descrédito).
Base: Lei 9.610/1998, art. 47, planalto.gov.br (mesma URL), verificado em 18/10/2026. Sem [TS]. Não VOLÁTIL.
Aderência: direta.

**L3-R80** (P2-4.2) Gabarito: C.
Justificativa: a nota de transparência recomenda "Customer feedback loop: Provide a feedback channel that allows users and individuals to report issues with the service once it's been deployed", com "ongoing monitoring and improvement". O item reproduz a recomendação, sem torná-la obrigação legal.
Base: Microsoft Learn, Transparency Note for Azure Speech speech to text, seção "Guidance for integration and responsible use with speech to text" (https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note), verificado em 18/10/2026 (página atualizada em 31/03/2026 segundo o rodapé). Sem [TS]. Não VOLÁTIL (boa prática documentada, sem número nem versão); conferência de base em 4–8/1/2027.
Aderência: direta.

**L3-R81** (P2-4.2) Gabarito: E. [TS]
Justificativa: a nota informa que, "without conscious effort focused on improving performance for all groups, it is often possible for the performance of an AI system to vary across groups based on factors such as race, ethnicity, region, gender, and age". O item afirma uniformidade e dispensa a verificação por grupos.
Base: Microsoft Learn, mesma nota, seção "Fairness considerations" (mesma URL), verificado em 18/10/2026 (rodapé "Last updated on 2026-03-31"). Não VOLÁTIL (conceito documentado); conferência de base em 4–8/1/2027. Par registrado com L1-R98 (P2-1.6): mesmo juízo de fundo (desempenho não uniforme entre grupos), fontes distintas (nota de transparência do Azure × model card do Whisper) e ângulo de equidade próprio da 4.2; não devem figurar no mesmo simulado.
Aderência: direta.

**L3-R82** (P2-4.3) Gabarito: E. [TS]
Justificativa: LGPD, art. 44, caput: o tratamento é irregular quando não fornece a segurança esperada, considerando-se, no inciso III, "as técnicas de tratamento de dados pessoais disponíveis à época em que foi realizado". O item desloca o momento para a apuração do dano.
Base: LGPD, art. 44, caput e III, planalto.gov.br, texto compilado (https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm), verificado em 18/10/2026. Vizinho de L3-Q27 (art. 46). Não VOLÁTIL.
Aderência: direta.

**L3-R83** (P2-4.3) Gabarito: E. [TS]
Justificativa: art. 44, parágrafo único: responde pelos danos "o controlador ou o operador que, ao deixar de adotar as medidas de segurança previstas no art. 46 desta Lei, der causa ao dano". O item restringe a responsabilidade ao controlador.
Base: LGPD, art. 44, parágrafo único, planalto.gov.br (mesma URL), verificado em 18/10/2026. Não VOLÁTIL.
Aderência: direta.

**L3-R84** (P2-4.3) Gabarito: C. [TS] (espelho)
Justificativa: art. 49: os sistemas "devem ser estruturados de forma a atender aos requisitos de segurança, aos padrões de boas práticas e de governança e aos princípios gerais previstos nesta Lei e às demais normas regulamentares". O item reproduz o rol, com o contraste "não apenas... mas também".
Base: LGPD, art. 49, planalto.gov.br (mesma URL), verificado em 18/10/2026. Vizinho de L3-Q27 (art. 46). Não VOLÁTIL.
Aderência: direta.

**L3-R85** (P2-4.3) Gabarito: E. [TS]
Justificativa: na documentação, a AWS "is responsible for protecting the global infrastructure that runs all of the AWS Cloud" e o cliente é "responsible for the security configuration and management tasks for the AWS services that you use". O item atribui essas tarefas à AWS.
Base: Amazon Transcribe Developer Guide, "Data protection in Amazon Transcribe" (https://docs.aws.amazon.com/transcribe/latest/dg/data-protection.html), verificado em 18/10/2026. Não VOLÁTIL (conceito documentado); conferência de base em 4–8/1/2027.
Aderência: direta.

**L3-R86** (P2-4.3) Gabarito: C.
Justificativa: art. 48, § 3º: "No juízo de gravidade do incidente, será avaliada eventual comprovação de que foram adotadas medidas técnicas adequadas que tornem os dados pessoais afetados ininteligíveis, no âmbito e nos limites técnicos de seus serviços, para terceiros não autorizados a acessá-los". O item não afirma dispensa da comunicação.
Base: LGPD, art. 48, § 3º, planalto.gov.br (mesma URL), verificado em 18/10/2026. Sem [TS]. Vizinho de L3-R10, L3-Q29 e D6-48. Não VOLÁTIL.
Aderência: direta.

**L3-R87** (P2-4.3) Gabarito: C.
Justificativa: a documentação recomenda "strongly... that you never put confidential or sensitive information... into tags or free-form text fields such as a Name field", pois esses dados "may be used for billing or diagnostic logs". O item aplica a recomendação a dados pessoais de participantes.
Base: Amazon Transcribe Developer Guide, "Data protection in Amazon Transcribe" (mesma URL), verificado em 18/10/2026. Sem [TS]. Não VOLÁTIL (boa prática documentada); conferência de base em 4–8/1/2027.
Aderência: direta.

**L3-R88** (P2-4.3) Gabarito: E. [TS]
Justificativa: art. 50, § 2º: o controlador "poderá" implementar programa de governança em privacidade que, entre outros requisitos, "conte com planos de resposta a incidentes e remediação" (I, "g"). O item troca a faculdade por obrigação.
Base: LGPD, art. 50, § 2º, I, "g", planalto.gov.br (mesma URL), verificado em 18/10/2026. Não VOLÁTIL.
Aderência: direta.

**L3-R89** (P2-4.3) Gabarito: C.
Justificativa: a página afirma que, se a aplicação renderiza automaticamente a saída do modelo, como Markdown ou HTML, "you may be vulnerable to indirect prompt injection and data exfiltration", e recomenda "Sanitize output". O item reproduz o risco e a mitigação.
Base: Google Cloud, Responsible AI (https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/responsible-ai), seção "Recommended practices", verificado em 18/10/2026 (rodapé "Last updated 2026-10-15 UTC"; a URL antiga cloud.google.com/vertex-ai/... redireciona para esta). Sem [TS]. Não VOLÁTIL (boa prática documentada, sem produto nem versão no enunciado); conferência de base em 4–8/1/2027. Vizinho de 4C-08 (definição de injeção de prompt, P1-5.1).
Aderência: direta.

**L3-R90** (P2-4.3) Gabarito: E. [TS]
Justificativa: art. 48, § 2º: a autoridade nacional "poderá... determinar ao controlador a adoção de providências, tais como: I - ampla divulgação do fato em meios de comunicação". O item troca "determinar" por "apenas recomendar".
Base: LGPD, art. 48, § 2º, I, planalto.gov.br (mesma URL), verificado em 18/10/2026. Vizinho de L3-R10, L3-Q29 e D6-48. Não VOLÁTIL. Registro (parecer R1): "pode apenas recomendar... sem poder determiná-la" é restritivo duplo (estilo_onda_3, rec. 5); mantido, pois a única troca é "determinar" por "apenas recomendar".
Aderência: direta.

**L3-R91** (P2-4.3) Gabarito: E. [TS]
Justificativa: na documentação, em tempo real "audio input is processed only on the Azure's server memory, and no data is stored at rest"; em lote, o cliente especifica o armazenamento do áudio e da saída e "controls the storage of this data, including the retention". O item inverte os dois modos.
Base: Microsoft Learn, Data, privacy, and security for Speech to text (https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/data-privacy-security), verificado em 18/10/2026 (rodapé "Last updated on 2026-08-26"). VOLÁTIL (hipótese (b), comportamento de produto; risco baixo). REVERIFICAR em 4–8/1/2027.
Aderência: direta.

**L3-R92** (P2-4.3) Gabarito: C. [TS] (espelho)
Justificativa: art. 46, § 1º: "A autoridade nacional poderá dispor sobre padrões técnicos mínimos para tornar aplicável o disposto no caput deste artigo, considerados a natureza das informações tratadas, as características específicas do tratamento e o estado atual da tecnologia". O item atribui a faculdade à autoridade nacional, com o contraste "e não o encarregado" (o encarregado, art. 41, não tem essa competência), o que evita a contestação pelo art. 50, caput, que permite a controladores e operadores formular regras de boas práticas, inclusive de padrões técnicos.
Base: LGPD, art. 46, § 1º, planalto.gov.br (mesma URL), verificado em 18/10/2026. Vizinho de L3-Q27 (art. 46, caput e § 2º). Não VOLÁTIL.
Aderência: direta.

**L3-R93** (P2-4.3) Gabarito: C.
Justificativa: a documentação recomenda "set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties". O item reproduz o princípio do menor privilégio.
Base: Amazon Transcribe Developer Guide, "Data protection in Amazon Transcribe" (mesma URL), verificado em 18/10/2026. Sem [TS]. Não VOLÁTIL (boa prática documentada, sem número nem versão); conferência de base em 4–8/1/2027.
Aderência: direta.

**L3-R94** (P2-4.3) Gabarito: E. [TS]
Justificativa: na página sobre registro de dados, o aviso "Caution: Your logged data is not deleted when you delete your project" remete a um formulário de pedido de exclusão. O item afirma que a exclusão do projeto basta.
Base: Google Cloud, Cloud Speech-to-Text, Data logging (https://docs.cloud.google.com/speech-to-text/docs/v1/data-logging), seção "Data privacy and security", verificado em 18/10/2026 (página atualizada em 13/10/2026 segundo o rodapé; a URL antiga cloud.google.com/speech-to-text/docs/data-logging redireciona para esta). VOLÁTIL (hipótese (c), recurso periférico: programa de registro de dados; risco baixo). REVERIFICAR em 4–8/1/2027.
Aderência: direta.

**L3-R95** (P2-4.3) Gabarito: C.
Justificativa: LGPD, art. 37: "O controlador e o operador devem manter registro das operações de tratamento de dados pessoais que realizarem, especialmente quando baseado no legítimo interesse". O item aplica o dever aos dois agentes no serviço de transcrição contratado; o legítimo interesse não é julgado.
Base: LGPD, art. 37, planalto.gov.br, texto compilado (https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm), verificado em 18/10/2026 (HTTP 200; User-Agent de navegador; trecho literal conferido no texto baixado hoje). Sem [TS]. Não VOLÁTIL. Vizinho de L3-Q18 (finalidades: controlador × operador), L3-Q29 (art. 48, caput) e BQ-0077 (relatório de impacto). Sem gêmeo no pacote (busca por ponto registrada no topo).
Aderência: direta (dever de rastreabilidade das operações de tratamento no pipeline de áudio contratado). QA PENDENTE; PENDENTE NORMATIVO.

### Contagens

- Total: 28 itens AUTORAL novos (L3-R68 a L3-R95). C = 14 (R68, R71, R74, R76, R77, R79, R80, R84, R86, R87, R89, R92, R93, R95); E = 14 (R69, R70, R72, R73, R75, R78, R81, R82, R83, R85, R88, R90, R91, R94). Gabarito C da parte: 50,0% (faixa de 40–60%). Por folha: 4.2 com 7 C e 7 E (sequência C E E C E E C E C C E C C E; no máximo duas iguais seguidas); 4.3 com 7 C e 7 E (sequência E E C E C C E C E E C C E C).
- [TS]: 18 (64,3%; mínimo de 16). Em E (troca única), 14: R69, R70, R72, R73, R75, R78, R81, R82, R83, R85, R88, R90, R91, R94. Em C (espelho: restritivo ou contraste verdadeiro), 4: R76 ("mas não pode opor-se"), R77 ("somente"), R84 ("não apenas... mas também"), R92 ("e não o encarregado"). Sem [TS]: R68, R71, R74, R79, R80, R86, R87, R89, R93, R95.
- Formato dos novos: definição 5 (R68, R69, R82, R84, R93); número ou prazo 2 (R70, R71); troca de sujeito 6 (R72, R73, R76, R83, R85, R92); situação hipotética 6 (R74, R75, R77, R86, R89, R90); par confundível 4 (R78, R79, R88, R91); aplicação parlamentar 5 (R80, R81, R87, R94, R95). Folhas de 20 (com os 6 existentes): 4.2 = definição 3, troca de sujeito 4, situação hipotética 4, par confundível 3, aplicação parlamentar 3, número ou prazo 3 (máximo 4/20 = 20%); 4.3 = definição 4, par confundível 3, troca de sujeito 4, aplicação parlamentar 4, número ou prazo 1, situação hipotética 4 (máximo 4/20 = 20%). Teto de 30%: cumprido nas duas folhas.
- VOLÁTIL: 2 no lote (R91, R94), ambos em 4.3 (2/20 = 10%; 4.2 com 0/20); risco alto: 0; teto de 20% por folha cumprido. Critério: D-T96-ONDA2-ACEITE (II), hipóteses (b) para o R91 e (c) para o R94; R81, R85, R87, R89 e R93 não são VOLÁTEIS (boa prática ou conceito documentado, sem número, versão, padrão nem disponibilidade condicionada) e têm conferência de base em 4–8/1/2027; R80 e R95 são lei federal. REVERIFICAR: R91, R94.
- Aderência: direta nos 28; parcial: nenhum. Por folha: 4.2 com 20 diretos de 20 (6 existentes + 14 novos); 4.3 com 20 diretos de 20. Piso de 10 diretos por folha cumprido; nenhum item de aderência parcial foi produzido.
- Bases: 13 itens em Lei 9.610/1998 (R68 a R80) e 8 em LGPD (R82, R83, R84, R86, R88, R90, R92, R95), ambas no planalto.gov.br (texto compilado), abertas em 18/10/2026; 7 em documentação de fornecedor (R81, R85, R87, R89, R91, R93, R94), abertas em 18/10/2026. Nenhum item usa o Legin; nenhum usa base de data anterior.
- Itens por folha: 4.2 = 14 novos (R68 a R81); 4.3 = 14 novos (R82 a R95). Folhas após o reforço: 4.2 = 20 (6 + 14); 4.3 = 20 (6 + 14).
- Conferência por script (python3 -I, somente leitura, sobre este arquivo e o pacote.json v1.10; na v2, repetida com os itens novos R80 e R95 e acrescida de Jaccard, ver resposta no topo): 28 ids na Parte 2 e 28 gabaritos na Parte 3, na mesma ordem; Parte 2 sem gabarito, [TS], VOLÁTIL nem REVERIFICAR; todos os enunciados com "Julgue o item." no comando da parte. Frase-base: o maior trecho de palavras que cada enunciado compartilha com qualquer dos 560 enunciados do pacote e dos 12 arquivos de reforço e do GCE_Lote3_v2_CPP.md é de 4 a 9 palavras, e todos esses trechos são fórmulas de abertura ("Segundo a Lei n.º 9.610/1998", "Segundo a Lei Geral de Proteção de Dados Pessoais, o", "Segundo a documentação do Amazon Transcribe", "Nessa situação, segundo a documentação do serviço") ou expressões literais da lei; nenhum trecho com conteúdo de julgamento repete frase de item existente (o trecho de 12 palavras entre R90 e L3-R10, que repetia a definição legal de incidente, foi reescrito e caiu para 9).
- Extensão (estilo): média de 44,6 palavras nos C e 45,1 nos E (de 28 a 62), sem diferença que sirva de pista (O-1). Marcadores: "independentemente" 1 C / 0 E; "ainda que" 1 C / 2 E; abertura "Segundo" 6 C / 7 E; ", e não" 1 C / 1 E; "apenas" 2 C / 3 E; "somente" 1 C / 0 E; "pode" 5 C / 2 E.
- Estado de QA: QA PENDENTE até a R2 da gce-cqfp. Conferência normativa: CONFERE nos 19 itens de lei federal da v1 (marca retirada); R80 e R95 PENDENTE NORMATIVO. Rótulo: AUTORAL em todos.

### Tabela de proveniência

| fonte | URL | data de verificação | usada em |
|---|---|---|---|
| Lei 9.610/1998, texto compilado (arts. 5º, VI; 7º, XIII e § 2º; 11; 14; 17; 18; 19; 24, § 2º; 37; 43; 46, III; 47; 49, III e V) | https://www.planalto.gov.br/ccivil_03/leis/l9610.htm | 18/10/2026 (HTTP 200; User-Agent de navegador) | R68 a R80 |
| Lei 13.709/2018 (LGPD), texto compilado (arts. 37; 44; 46, § 1º; 48, §§ 2º e 3º; 49; 50, § 2º) | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm | 18/10/2026 (HTTP 200) | R82, R83, R84, R86, R88, R90, R92, R95 |
| Microsoft Learn, Transparency Note for Azure Speech speech to text (seção "Fairness considerations"); rodapé "Last updated on 2026-03-31" | https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note | 18/10/2026 | R81 |
| Microsoft Learn, Data, privacy, and security for Speech to text (seções "Real-time speech to text" e "Batch transcription"); rodapé "Last updated on 2026-08-26" | https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/data-privacy-security | 18/10/2026 | R91 |
| Amazon Transcribe Developer Guide, Data protection in Amazon Transcribe | https://docs.aws.amazon.com/transcribe/latest/dg/data-protection.html | 18/10/2026 | R85, R87, R93 |
| Google Cloud, Responsible AI (seção "Recommended practices"); rodapé "Last updated 2026-10-15 UTC" | https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/responsible-ai | 18/10/2026 | R89 |
| Google Cloud, Cloud Speech-to-Text, Data logging; rodapé "Last updated 2026-10-13 UTC" | https://docs.cloud.google.com/speech-to-text/docs/v1/data-logging | 18/10/2026 | R94 |

Afirmações não feitas por falta de fonte: prazo regulamentar da autoridade nacional para comunicar incidente — [SEM FONTE — não afirmar]; titularidade de conteúdo gerado por IA e licitude do treinamento com obras protegidas — controvérsia sem texto legal expresso (curso 4.2 do Lote 3), não julgada; nenhuma versão, preço ou limite numérico de ferramenta foi afirmado.

FIM DA PARTE 3/3

FIM DO LOTE
