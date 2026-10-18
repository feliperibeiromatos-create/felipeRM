# QA_T98B_R1_2026-10-18_gce-cqfp.md — T-98 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L3_reforco_onda4_B_v1.md (gce-cpp; 28 itens AUTORAL, L3-R40 a R53 em P2-3.3 e L3-R54 a R67 em P2-3.4). R1 da parte B da T-98, ciclo 2026-10-18 s13c2. Revisão: aponto onde e por quê; não reescrevo, salvo o texto exato de supressão pedido no ajuste do R62. Sem commit e sem push.

Lido: CLAUDE.md; regras/ (proveniencia, estilo_banca, padrao_resposta_cebraspe); TAREFAS.md (T-98, piso de 10 diretos por folha; T-107); DECISOES.md (D-REFORCO-1, D-REFORCO-2, D-FONTE-DATA-ANTERIOR, D-T89-R1-ACEITE, D-T96-ONDA2-ACEITE (II), D-T97-ONDA3-ACEITE (II), D-T97-META-FUNDADOR-RESP, D-ADERENCIA); T91_reconciliacao (seções 2 e 3: Legin, critério de formato, nenhum AP em 3.4); T97_reconciliacao (seções 1, 3.3, 3.4, 4 e 6); saida/banco/estilo_onda_3.md (seções 4 e 5); edital/modulo_RF_IA_P2.md (3.3 "Geração automática de atas e resumos de sessões"; 3.4 "Modelos de IA multilíngues e especializados em português"); saida/pacote/pacote.json v1.10 (560 itens; 3.3 = Q09–Q12, R05 parcial, R06 → 5 diretos + 1 parcial; 3.4 = Q13–Q16, R07, R08 → 6 diretos; confere com a partida declarada); L3_reforco_onda1_v3.md; finais das ondas 1–3 em saida/gce/*reforco*. Outras partes da onda 4 (L3_reforco_onda4_A/C/D_v1.md): não existem em disco nesta data; gêmeo dentro da onda 4 conferido só dentro da parte B.

## 0. Resultado

- REPROVADO: 1 (L3-R50 — gêmeo do L1-R54).
- AJUSTAR: 2 (L3-R59 — rótulo VOLÁTIL; L3-R62 — supressão de oração que extrapola a base).
- APROVADO: 25 (vários com ressalva de registro, seção 3).
- Taxa de reprovação: 1/28 = 3,6% (não aprovados, REPROVADO + AJUSTAR: 3/28 = 10,7%). Gate de 30% não acionado.
- Nenhum gabarito errado. 
- PENDENTE NORMATIVO: L3-R51, R52, R53 (RICD, art. 97, §§ 2º, 3º e 1º). O literal do Legin foi reaberto e confere (seção 2), mas a marca fica até o parecer do qa-normativo, que corre em paralelo.
- Veredito geral da parte B: APROVADO COM RESSALVAS. A folha P2-3.3 cai para 19 itens com a saída do R50. A reposição é D1 da gce-gerencia (precedente T-97, seção 1).

## 1. Estrutura e contagens (script próprio, python3 -I, somente leitura)

- Parte 2: 28 ids e Parte 3: 28 gabaritos, nos mesmos ids e na mesma ordem. A Parte 2 não traz gabarito, [TS], VOLÁTIL nem REVERIFICAR. Todos os enunciados abrem com "Julgue o item.". A última linha é "FIM DO LOTE", e as partes estão numeradas (D-REFORCO-1). Confere.
- Gabarito: 14 C / 14 E = 50,0% (regra 5). Confere. Sem o R50: 13 C / 14 E = 48,1%, ainda na faixa de 40% a 60%.
- [TS]: 24 de 28. São 14 de 14 em E, todos de troca única: R41, R43, R47, R49, R51, R53, R55, R57, R59, R63, R66 e R67 trocam um conceito; R44 e R64 invertem um único par, como admitido no precedente. Os outros 10 [TS] estão em C, pela convenção espelho (O-6, aceita nas ondas 2 e 3): R40, R42, R45, R52, R54, R56, R58, R61, R62 e R65. Cada um declara na justificativa a troca do espelho, e cada troca é de um conceito só. Confere. Avaliação: a convenção é admissível, e a proporção (10 de 14 C) fica acima da onda 3 (15 de 56 C). Registro para a Gerência: o espelho não é troca presente no texto do item. Na contagem da meta de [TS], só os E (14 de 28 = 50%) já bastam.
- Extensão: de 23 a 61 palavras. Nenhum C passa de 65 (O-1).
- Formatos (teto de 30% = 6 por folha de 20): 3.3 tem no máximo 5 (D) e 3.4 tem no máximo 5 (D e SH). Não há AP novo na 3.4, como manda a T91_reconciliacao, seção 3.3: o legado Q15 e Q16 dá 2/20. Confere. Sem o R50, o D da 3.3 fica em 4/19.
- VOLÁTIL (regra 4, máximo de 20%): na 3.3, R50 dá 1/20; sai com a reprovação, e a folha fica com 0/19. Na 3.4, R56 e R65 dão 2/20, que vão a 3/20 = 15% com o R59 (seção 3). Dentro do teto.
- Aderência e piso de 10 diretos (D-T97-META-FUNDADOR-RESP):
  - 3.3: 19/20 declarados. Sem o R50, ficam 18/19, ou 17/19 se o R53 passar a PARCIAL.
  - 3.4: 20/20 declarados, ou 19/20 se o R64 passar a PARCIAL.
  - O piso é cumprido com folga em qualquer leitura.
  - A instrução da T97_reconciliacao, seção 3.4 (item novo de folha com menos de 12 diretos deve ser direto), também é cumprida.

## 2. Evidência: URLs reabertas por esta QA em 18/10/2026

Abri as 12 URLs da tabela de proveniência (curl -L, User-Agent de navegador). Todas deram HTTP 200, na mesma URL final declarada. Conferi por script 47 trechos literais contra o texto extraído: 46 batem byte a byte. O 47º é o trecho do R62 no README: lá, "BrWaC (Brazilian Web as Corpus)" está dentro de marcação de link markdown. O texto renderizado é idêntico ao citado, e isso é registro, sem efeito.

| # | URL | data exibida na página (conferida) | trechos conferidos |
|---|---|---|---|
| 1 | learn.microsoft.com/.../language-service/summarization/overview | 2026-06-30 | Positional information; original sentences; contextual input range; Rank score; tabela recap / chapterTitle / narrative ("Summarizes a conversation into one paragraph \| recap"; "Segments … summary for each segment … \| narrative"; "Segments … title for each segment … \| chapterTitle"); "as-is, with no added customization"; aviso "Summarization retires from Azure Language on March 31, 2029" |
| 2 | learn.microsoft.com/.../summarization/how-to/summarize | 2026-06-30 | speech transcripts with speakers; Word/PDF/PowerPoint; "any number of parties"; issues and resolutions "between two parties"; follow-up tasks; "The service provides the AI models" |
| 3 | learn.microsoft.com/en-us/azure/foundry/responsible-ai/language-service/transparency-note-extractive-summarization (título "Use cases for summarization") | 2026-04-01 | "Segment a long conversation with a short title"; "avoid scenarios in which the AI system could affect an individual's legal status or legal rights" |
| 4 | learn.microsoft.com/.../language-service/transparency-note | 2026-04-01 | "Lack of standard punctuation or casing…"; "select the option to include punctuation" |
| 5 | docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/audio-understanding | 2026-10-15 UTC | "enable the audioTimestamp parameter" |
| 6 | www2.camara.leg.br/legin/... Resolução 17/1989, norma atualizada | — | art. 97, caput e §§ 1º a 3º, literais conferidos (sequência no texto: caput, § 1º Anais, § 2º lista nominal, § 3º última sessão; art. 98 a seguir) |
| 7 | docs.aws.amazon.com/transcribe/latest/dg/lang-id.html | sem data | lote (dominante ou todos); "without you having to specify a language code"; "optionally provide a list of two or more"; "Streaming requests must have a minimum of two additional language options"; "faster language identification" |
| 8 | learn.microsoft.com/.../speech-service/language-identification | 2026-03-04 | candidatos (fr-FR/en-US × alemão); at-start × contínua; "doesn't support changing languages within the same sentence"; latência inicial; "one locale per base language" |
| 9 | raw.githubusercontent.com/neuralmind-ai/portuguese-bert/master/README.md | sem data | BrWaC; "Pearson's correlation for STS and F1-score for RTE and NER"; tabela (Base 0.836/89.2/83.1/77.6 × mBERT 0.809/86.8/79.2/73.1) |
| 10 | docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/get-text-embeddings | 2026-10-15 UTC | "Specialized in English and code tasks" (text-embedding-005); "Specialized in multilingual tasks" (text-multilingual-embedding-002) |
| 11 | docs.aws.amazon.com/translate/latest/dg/how-custom-terminology.html | sem data | "doesn't guarantee that it will use the target term for every translation"; "uses the translation from the terminology file" |
| 12 | docs.aws.amazon.com/translate/latest/dg/what-is.html | sem data | "text translation service"; "such as meeting minutes" |

Base NÃO reaberta: o artigo do BERTimbau (arXiv 1909.10649 / Springer 2020) e o model card do Hugging Face. Os dois hosts recusam a conexão (proxy 403). Só importam para o ajuste do R62 (seção 3).
D-FONTE-DATA-ANTERIOR: não foi invocada. Todas as bases foram abertas na data da produção, e esta QA confirma isso.

## 3. Veredito por item

Legenda de formato da produção: D, TSj, SH, NP, PC, AP. "Gêmeo" = o mesmo ponto em qualquer folha do pacote v1.10 ou de saida/gce/*reforco*.

| id | folha | gab. | formato | veredito | motivo (onde e por quê) |
|---|---|---|---|---|---|
| L3-R40 | 3.3 | C [TS] esp. | D | APROVADO | Fiel a "Positional information…" e "original sentences". Ponto distinto do L3-Q10 (definição extrativa × abstrativa): aqui se julga o atributo da saída. Sem gêmeo. |
| L3-R41 | 3.3 | E [TS] | PC | APROVADO | Troca única (contextual input range → rank score). A página mostra o rank score só na seção da extrativa. Vizinho declarado do R40. |
| L3-R42 | 3.3 | C [TS] esp. | SH | APROVADO (ressalva de registro) | Gabarito e base certos. O cenário é decorativo: a 1ª frase não pesa no juízo, que é um par confundível de entradas (estilo_onda_3, rec. 4). Pela construção do ponto (T91, 3.1(a)), o formato real é PC. Com a reclassificação, o PC da 3.3 fica em 5/19, dentro do teto. D1 de registro. |
| L3-R43 | 3.3 | E [TS] | TSj | APROVADO | Troca única: o alcance "qualquer número de partes" é atribuído a issues and resolutions, quando a página diz "between two parties". O cenário pesa no juízo ("dezenas de oradores"; "agiu corretamente"). |
| L3-R44 | 3.3 | E [TS] | PC | APROVADO | A inversão de um único par (recap × narrative) confere com a tabela da página 1. Vizinho de R46, que trata do título por segmento, ponto distinto. |
| L3-R45 | 3.3 | C [TS] esp. | AP | APROVADO | Fiel a "Follow-up tasks summarizes action items and tasks that arise during a meeting". A AP da 3.3 fica em 3/20, abaixo do teto. |
| L3-R46 | 3.3 | C | D | APROVADO | Fiel às páginas 1 e 3. C sem [TS], com discriminação baixa (rec. 7 da onda 3), sem efeito. |
| L3-R47 | 3.3 | E [TS] | D | APROVADO (ressalva de estilo) | O E está certo ("as-is, with no added customization"). Ressalva: a concessiva "Ainda que o serviço forneça os modelos…" não opõe nada à oração principal, e a leitura fica truncada. Não há ambiguidade de gabarito. Fica para o gbq-estilo, junto com R59 e R60. |
| L3-R48 | 3.3 | C | SH | APROVADO | Fiel à seção "Limitations" da página 4. Sem gêmeo no 1.5 (L1-Q10, Q11, C-Q29, R08, R75–R88 tratam de outros pontos) nem no L3-Q04 (propagação de erro). |
| L3-R49 | 3.3 | E [TS] | SH | APROVADO | A troca única ("evitar" → "adequado") confere com a nota de transparência de sumarização. O cenário (sanção a parlamentar com base em resumo automático) é verossímil no Conselho de Ética e pesa no juízo. |
| L3-R50 | 3.3 | C | D | **REPROVADO** | (1) Gêmeo: o L1-R54 (P2-1.3, E, já canônico na onda 2; L1_reforco_onda2_B_v2.md, l. 244–245) julga o mesmo ponto, ou seja, que em arquivo só de áudio o Gemini exige configurar o parâmetro de timestamp na configuração de geração e que pedir no prompt não basta. O R50 é a versão C desse item. Viola a regra 1 da D-REFORCO-2 e a T96_reconciliacao, seção 4 (ponto contra o pacote inteiro). A seção 1.3 da entrega declarou vizinhança só com L2-Q22 e L1-R02 e não viu o L1-R54, que escreve "carimbos de tempo" e "audio_timestamp". (2) O ponto é de P2-1.3 (LLMs multimodais de áudio nativo), não de geração de atas. (3) Rótulo incoerente com o gêmeo: VOLÁTIL baixo aqui, médio no L1-R54 ("mesmo trecho, mesmo rótulo", D-T96 II). Ajuste não cabe. Sai, e a 3.3 precisa de reposição (seção 4). |
| L3-R51 | 3.3 | E [TS] | AP | APROVADO — PENDENTE NORMATIVO | O literal do art. 97, § 2º, confere no Legin. Troca única ("de presença e de ausência" → "apenas de presença"). Aderência DIRETA confirmada: segue o precedente L3-R06 (art. 97, caput, marcado "direta" no pacote v1.10), e o ponto é o conteúdo da própria ata (T97, 3.4). |
| L3-R52 | 3.3 | C [TS] esp. | NP | APROVADO — PENDENTE NORMATIVO | O literal do art. 97, § 3º, confere. O NP se justifica pelo quórum ("qualquer número"), e o espelho troca o quórum. Aderência DIRETA confirmada: ata "redigida em resumo" é o objeto da folha. |
| L3-R53 | 3.3 | E [TS] | PC | APROVADO (ressalva de aderência) — PENDENTE NORMATIVO | O literal do art. 97, § 1º, confere, com troca única (cronológica → temática). A aderência DIRETA não se confirma: a encadernação dos Anais e o recolhimento ao Arquivo dizem respeito à guarda das atas já feitas, não à geração da ata nem ao seu registro, revisão ou publicação (T97, 3.4). O precedente L3-R06 cobre o padrão de redação da ata (caput), não o § 1º. Recomendo PARCIAL (D1 da gce-gerencia), o que não fere o piso (17/19). Registro: "impressas ou datilografadas" é texto vigente do RICD e se mantém. |
| L3-R54 | 3.4 | C [TS] esp. | SH | APROVADO | Literal do lote AWS conferido. O cenário (português e espanhol) pesa no juízo. Sem gêmeo: o L1-R89 trata de idioma configurado errado. |
| L3-R55 | 3.4 | E [TS] | D | APROVADO | Troca única (lista opcional → exigência prévia). Mesma página que R54 e R56, pontos distintos. |
| L3-R56 | 3.4 | C [TS] esp. | NP | APROVADO | Literal conferido ("minimum of two additional language options"; "faster"). VOLÁTIL baixo (a) confirmado (limite numérico). |
| L3-R57 | 3.4 | E [TS] | SH | APROVADO | Troca única. O exemplo da própria página (fr-FR e en-US × alemão) sustenta o E sem margem. Não é VOLÁTIL: mecanismo documentado do recurso central de candidatos. |
| L3-R58 | 3.4 | C [TS] esp. | PC | APROVADO | At-start × contínua conferidos literalmente. |
| L3-R59 | 3.4 | E [TS] | SH | **AJUSTAR (rótulo)** | O gabarito E está certo ("doesn't support changing languages within the same sentence… doesn't detect the language change per word"). Mas o E depende da INEXISTÊNCIA de um recurso, a detecção de troca de idioma dentro da frase (code-switching). Essa é a hipótese (c) da D-T96-ONDA2-ACEITE (II), existência de recurso, e não mecanismo do recurso central: se o fornecedor passar a suportar, o gabarito se inverte. "Marcação a menos não" é admitida. Ajuste: marcar VOLÁTIL (baixo), hipótese (c), no mapa e no (d-G); a 3.4 fica com 3/20 = 15%. Ressalva de estilo: "Ainda que um orador fale principalmente em português, ele insere…" é concessiva sem oposição real (v. R47). Texto opcional para a gce-cpp, sem efeito no gabarito. |
| L3-R60 | 3.4 | C | D | APROVADO (ressalva de estilo) | Literal conferido. Ressalva: "ainda que se trate de recurso opcional" não se opõe a "latência maior" e é a 3ª concessiva sem contraste da parte (R47, R59, R60). Fica para o gbq-estilo. Não é VOLÁTIL: boa prática documentada, sem número. |
| L3-R61 | 3.4 | C [TS] esp. | PC | APROVADO | Literal conferido ("one locale per base language"; en-US e en-GB). |
| L3-R62 | 3.4 | C [TS] esp. | D | **AJUSTAR (texto)** | O README sustenta "treinados no BrWaC…, um grande corpus de língua portuguesa", mas não diz nada sobre "e não em um corpus multilíngue". A oração final extrapola a base e cria um ponto de recurso. A inicialização dos pesos a partir de checkpoint multilíngue ou inglês está [SEM FONTE — não afirmar], porque não pude abrir o artigo nem o model card, mas é um questionamento plausível. A oração também tensiona com o L3-Q14 da mesma folha, cuja justificativa diz que o modelo especializado "pode ser adaptado de modelo multilíngue". Texto exato do ajuste: suprimir ", e não em um corpus multilíngue", e o enunciado termina em "…um grande corpus de língua portuguesa.". Gabarito C e [TS] espelho mantidos. A base passa a citar o trecho renderizado (registro). |
| L3-R63 | 3.4 | E [TS] | TSj | APROVADO | A tabela confere (Base > mBERT em STS, RTE e nas duas NER). Troca única no sujeito que supera. Não é VOLÁTIL: o README é estático e tem conferência de base. |
| L3-R64 | 3.4 | E [TS] | NP | APROVADO (ressalva de registro) | O gabarito confere com "Pearson's correlation for STS and F1-score for RTE and NER", com troca de um único par. Formato: o nome de uma métrica não é "valor, prazo ou expressão numérica" (T91, 3.1(c)), então o formato é PC (a 3.4 iria a PC 5/20 e NP 1/20). Aderência: o ponto é a métrica de avaliação de NLP, não o modelo multilíngue ou especializado em si. Recomendo PARCIAL (D1); a 3.4 fica com 19/20 diretos. |
| L3-R65 | 3.4 | C [TS] esp. | SH | APROVADO (ressalva de registro) | Literais conferidos. VOLÁTIL médio (catálogo com ids versionados -005/-002) confirmado. Como depende de versão, é inapto a simulado final até 4–8/1/2027, e o rótulo cobre isso. Registro: a página recomenda hoje o gemini-embedding-001, que "surpasses" os dois; o item não afirma preferência e, por isso, não é afetado. O cenário é decorativo, e o formato real é PC (3.4: PC 5/20 ou 6/20 com o R64, no teto). Se a Gerência reclassificar R64 e R65, fica PC 6/20 = 30%, exatamente no teto, e a folha não admite mais PC. |
| L3-R66 | 3.4 | E [TS] | PC | APROVADO | Literal "doesn't guarantee" conferido, troca única. Sem gêmeo: a terminologia do L1 onda 2 C (l. 347) é a pronúncia do custom speech. |
| L3-R67 | 3.4 | E [TS] | D | APROVADO | Literais conferidos ("text translation service"; "meeting minutes"). Ponto simples e sem ambiguidade. |

## 4. Para a gce-gerencia (D1; nada decidido aqui)

1. R50 REPROVADO por gêmeo. A P2-3.3 fica com 19. Precedente da T-97, seção 1: repor com produção nova, id novo e QA própria. Requisitos sugeridos para a reposição:
   - ponto de geração de atas ou resumos sem gêmeo no pacote v1.10 nem nas ondas 1 a 4;
   - aderência direta;
   - formato diferente de D, que tem folga;
   - preferência por E, para a folha voltar a 10/10;
   - não VOLÁTIL.
   Atenção à numeração das outras partes da onda 4 (L3-R68+ pode colidir).
2. R59 com VOLÁTIL baixo (c), e R62 com a supressão exata da seção 3. Os dois passam pela R2.
3. Registros de rótulo, D1 sem R2 de mérito:
   - aderência PARCIAL recomendada em R53 e R64;
   - formato PC recomendado em R42, R64 e R65 (cenário decorativo e métrica não numérica). Com isso, PC chega a 6/20 na 3.4, no teto;
   - com R53 e R64 PARCIAIS, a 3.3 fica com 17/19 diretos e a 3.4 com 19/20; o piso de 10 continua cumprido.
4. Concentração, registro de cobertura sem regra violada:
   - 3.3: 9 dos 13 novos remanescentes vêm de um só conjunto de páginas (Azure Language summarization), e a página anuncia a aposentadoria do recurso em 31/3/2029, depois da prova. Não é VOLÁTIL, mas as 9 bases entram em bloco na conferência de janeiro;
   - 3.4: 8 dos 14 novos tratam de identificação de idioma em dois fornecedores (vizinhança com a 1.8). Na reposição, convém evitar os dois focos.
5. Estilo, para o gbq-estilo na amostra da onda 4: há 3 concessivas sem oposição (R47, R59, R60), e 3 SH com cenário decorativo (R42, R65; R54 pesa).
6. PENDENTE NORMATIVO em R51, R52 e R53 até o parecer do qa-normativo. O literal no Legin já foi conferido por esta QA.
7. Conferência de base de 4–8/1/2027 (T-11, P2): os 27 remanescentes. VOLÁTEIS: R56, R59 e R65.

## 5. Tabela final (28 itens)

| id | veredito | | id | veredito |
|---|---|---|---|---|
| L3-R40 | APROVADO | | L3-R54 | APROVADO |
| L3-R41 | APROVADO | | L3-R55 | APROVADO |
| L3-R42 | APROVADO (registro: formato PC) | | L3-R56 | APROVADO |
| L3-R43 | APROVADO | | L3-R57 | APROVADO |
| L3-R44 | APROVADO | | L3-R58 | APROVADO |
| L3-R45 | APROVADO | | L3-R59 | AJUSTAR (VOLÁTIL baixo, c) |
| L3-R46 | APROVADO | | L3-R60 | APROVADO (estilo) |
| L3-R47 | APROVADO (estilo) | | L3-R61 | APROVADO |
| L3-R48 | APROVADO | | L3-R62 | AJUSTAR (suprimir oração final) |
| L3-R49 | APROVADO | | L3-R63 | APROVADO |
| L3-R50 | REPROVADO (gêmeo L1-R54) | | L3-R64 | APROVADO (registro: PC; PARCIAL) |
| L3-R51 | APROVADO — PENDENTE NORMATIVO | | L3-R65 | APROVADO (registro: PC) |
| L3-R52 | APROVADO — PENDENTE NORMATIVO | | L3-R66 | APROVADO |
| L3-R53 | APROVADO (registro: PARCIAL) — PENDENTE NORMATIVO | | L3-R67 | APROVADO |

Reprovados: 1/28 = 3,6%. Não aprovados (REPROVADO + AJUSTAR): 3/28 = 10,7%. Gate de 30% não acionado. Veredito geral: APROVADO COM RESSALVAS.

AVISO: vereditos de aderência, formato e VOLÁTIL são julgamento desta QA e dependem de D1 da gce-gerencia. As contagens e a conferência de literais vêm de script próprio (python3 -I, somente leitura; páginas baixadas no scratchpad da sessão em 18/10/2026).
