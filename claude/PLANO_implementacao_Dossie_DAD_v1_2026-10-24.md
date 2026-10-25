# Plano de implementação do Dossiê Didático de Direito Administrativo na plataforma — v1 (24/10/2026)

Origem: Dossiê Didático DAD v1 (24/10/2026, documento vivo M7zTurNV3ArCRXHCnEMVJH; cópia e 20 relatórios por aula em DAD/ no Projeto). Plano preparado pela sessão Cowork a pedido do Fundador. Não decide matéria reservada; as decisões do Fundador estão na seção 6.

## 1. Premissa que governa tudo: o que do dossiê pode entrar

O dossiê analisou um curso de terceiro (Estratégia Concursos, curso 353871). A regra do Projeto para esse material é a D-ESTRATEGIA (20/10/2026): serve só para análise de forma, nunca como fonte de redação, conteúdo ou itens. A Parte VII do dossiê, lida ao pé da letra ("reconstruir aulas em unidades", "páginas-ouro a reaproveitar", "questões da bateria a migrar", "texto do curso, podado" como bloco 5), transformaria o curso em fonte da plataforma — o que a D-ESTRATEGIA veda e a Lei 9.610/1998 também alcança (reprodução de texto, tabelas e exemplos do autor).

Separação adotada neste plano:

| Entra (é conhecimento sobre como ensinar e sobre a banca) | Não entra (é conteúdo do curso) |
|---|---|
| Os 10 princípios didáticos (Parte III) e o padrão de 9 blocos (Parte IV) | Texto, parágrafos e caixas do curso |
| A lista de pares e confusões típicas por item do edital (seção 7 dos relatórios) — são fatos sobre o que a Cebraspe troca, não expressão do autor | Tabelas e esquemas do curso ("páginas-ouro"); refazemos os nossos a partir da lei |
| As lacunas do edital que o curso não cobre (2.2, 3.3, 4.1, 8, 9, 10.4–10.7) | Exemplos e casos do autor (ex.: "atraso de 1 h punido com 90 dias"); escrevemos casos próprios, de preferência a partir de itens reais |
| Os 12 erros que mudam resposta — como lista de pontos a conferir nos NOSSOS lotes | Questões inline e das baterias do curso — nenhuma migra; itens reais vêm só do CDN oficial (fila BANCO-DA) |
| As proporções literalidade × caso por tema (LAI ~90% literal; responsabilidade civil ~50% caso) | A "matriz" do ChatGPT como catálogo de páginas do curso |
| A ordem de prioridade por peso × defeito (ato, 8.112, 9.784 primeiro) | |
| A estimativa de carga (220 h) como teto que a nossa versão não pode repetir | |

Exceção de alto valor: o dossiê localizou no curso cerca de 15 questões rotuladas "Cebraspe – Câmara dos Deputados/2026" (A02, A07, A09, A10, A11, A15, A16, A18, A19). Se forem do ciclo cd_25_ns, são itens oficiais do órgão-alvo. O que entra não é o texto do curso, e sim o caderno e o gabarito definitivo em cdn.cebraspe.org.br, localizados a partir dessas pistas (mesmo tratamento "localizador → fonte oficial" da fila BANCO-DA).

## 2. O que muda na plataforma (formato ESPEC v1 → v2)

A ESPEC_curso_DA_formato_v1 (19/10) já tem DEFINIÇÃO / BASE LEGAL / EXEMPLO PARLAMENTAR / PEGADINHA PROVÁVEL, `emUmMinuto`, `resumo` e visuais (`compare`, `baseLegal`, `esquema`, `linha`, `fluxo`, `tabela`). O padrão de 9 blocos do dossiê encaixa nela com seis acréscimos:

| Bloco do dossiê | Onde cai na plataforma | Novo? |
|---|---|---|
| 1. Tarefas ("dado X, decidir Y", 3–6) | novo campo `topicos[id].tarefas[]`, exibido antes do curso | Sim |
| 2. Mapa de chegada | o visual de abertura já existente (`esquema`/`linha`/`compare`); repetido no fechamento | Parcial (repetição no fim) |
| 3. Glossário de pares | quadro novo `GLOSSÁRIO` no início do bloco do subitem; e `compare` para os pares centrais | Sim (quadro) |
| 4. Caso de abertura | quadro novo `CASO` antes da DEFINIÇÃO (pergunta sem resposta; a resposta vem depois da regra) | Sim |
| 5. Regra e critério | o curso atual (DEFINIÇÃO / BASE LEGAL / explicação), com a regra "uma representação por conceito" | Não (regra de produção) |
| 6. Pares que a banca troca | PEGADINHA PROVÁVEL já existe; passa a ter três colunas fixas (termo A × termo B × palavra que muda a resposta) — formato da D-PEGADINHA-UNICA | Parcial |
| 7. Itens intercalados | novo: marcador `ITEM <id>` no texto do curso, que a plataforma renderiza como item C/E respondível, com o comentário oculto até a resposta; 1 a cada subitem ou a cada ~3 quadros | Sim (plataforma + pacote) |
| 8. Fechamento | novo campo `topicos[id].fechamento` = 5 frases "o que levar" + lista "literalidade × caso"; `emUmMinuto` continua na abertura | Sim |
| 9. Verificação | já existe (questões por tópico); passa a exigir 10 por item-folha, metade literal e metade situação hipotética, com `comentario` em 3 linhas (palavra decisiva / regra / versão correta) | Parcial |

Regras de produção que entram no PADRAO_UNICO (v1.1) e no checa_pacote.py: nenhum termo antes da definição (verificação humana no QA didático; o script só confere a presença do GLOSSÁRIO); uma representação por conceito; classificações como perguntas; toda tabela cabe numa tela (limite já existente do `compare`/`tabela`); todo número com norma e data (já é regra do `baseLegal`); comentário em 3 linhas (script confere 3 segmentos); declaração de escopo por unidade ("o que fica para outra unidade"); itens só C/E com rótulo (já é regra). A lista de verificação do QA didático (Parte IV) vira o checklist do gcb-cqfp para DA.

Onde isso entra no cronograma da plataforma: a v17 (redesign funcional e visual, ordenada em 21/10 e não executada) é o veículo natural dos campos novos (`tarefas`, `fechamento`, `GLOSSÁRIO`, `CASO`, item intercalado respondível). Fazer uma v17.1 depois seria retrabalho de layout. Recomendação: incorporar à ordem da v17 antes de executá-la.

## 3. O que muda no conteúdo (Fábrica, lotes D1–D6 → v2)

Estado de partida: 6 lotes de DA, 410 itens AUTORAL, reforço em andamento; D6 (LAI e LGPD) e D1 canônicos; ORDEM_DA_FORMATO pendente de execução. O plano abaixo substitui a ORDEM_DA_FORMATO por uma ordem única em duas fases, para não formatar duas vezes.

Fase A — antes de qualquer tela chegar à candidata (AGORA):
1. Conferência dirigida dos 6 lotes nos 12 pontos em que o curso de mercado errou (Parte VI do dossiê): função atípica "julgar" do Executivo; retorno do demitido por improbidade (art. 137 da 8.112); decisão coordenada da 9.784 ("três ou mais" E relevância E discordância); ressarcimento ao erário e Temas 897/899; dispensa × inexigibilidade (art. 74 × 75); prescrição intercorrente da LIA após a decisão do STF de 1/7/2026 (ADIs 7156 e 7236); regresso (dolo OU culpa, ação regressiva); linhas de defesa na Lei 14.133; requisitos cumulativos do empregado de estatal; regime de pessoal de autarquia após 2024; férias e Tema 1135 do STJ. É QA normativo sobre o nosso material, não sobre o curso; o que estiver certo, registra-se; o que estiver errado, errata.
2. Localizar no CDN as ~15 questões "Câmara dos Deputados/2026": se forem cd_25_ns, entram como CEBRASPE_OFICIAL do órgão-alvo e vão para o Estado Canônico; são os itens de maior valor preditivo que existem para este edital.
3. Produzir as unidades que não existem em lugar nenhum (nem no curso, nem nos nossos lotes, a confirmar no mapa de cobertura dos D1–D6): 2.2 parecer e responsabilidade do emissor; 3.3 requisição; 4.1 fontes e princípios do direito disciplinar; 10.4–10.7 gestor e fiscal do contrato, ETP e Termo de Referência; 8 e 9 modelos de gestão e governança (Decreto 9.203/2017). AUTORAL com QA Normativo; 20 itens por item-folha (D-REFORCO-2), 30 onde não houver item real análogo (D-LACUNAS).
4. Aplicar o formato v2 primeiro aos três tópicos de maior peso × defeito, na ordem do dossiê: item 2 (ato administrativo; quatro unidades), item 3.4 (provimento, vacância, deslocamento; a unidade-exemplo da Parte IV serve de modelo, reescrita com casos nossos), item 4.4 (Lei 9.784, incluindo arts. 11–17 e 53–55).

Fase B — PRÓXIMO:
5. Item 10 (licitações e contratos): matriz única de modalidades, quadro único de dispensas, régua de prazos, "vida do contrato" — como visuais `tabela`, `linha` e `fluxo` nossos, a partir da Lei 14.133; é o item com mais itens reais na fila BANCO-DA (271 C/E), então os itens intercalados podem ser quase todos reais.
6. Itens 3.1–3.2 (agentes, disposições constitucionais) com quadro de regime temporal; 1.1 (princípios) com as cinco tabelas de contraste que o dossiê lista como ausentes (legalidade × reserva legal × juridicidade; razoabilidade × proporcionalidade; supremacia × indisponibilidade; tutela × autotutela × hierarquia; publicidade × transparência); 6 (responsabilidade) com critério unificado da omissão; 7 (improbidade) com as pranchas de tipos, sanções, prescrição e competência.
7. Itens 11 e 12 (D6, já canônico): só acréscimos de formato — régua de números da LAI, tabela art. 7º × art. 11 da LGPD, mapa das bases legais na abertura; e correção da ordem didática que o dossiê aponta (bases legais antes de "consentimento").
8. Itens intercalados em todos os tópicos de DA a partir do banco real (depende da onda 1 da BANCO-DA); onde não houver real, AUTORAL marcado.

BACKLOG: revisão espaçada dos quadros de pares em 1, 7 e 30 dias (função da plataforma, candidata ao tutor v18); diagnóstico de 30 itens de DA no primeiro acesso ao módulo (regra já existente para as outras matérias); conversão das proporções literalidade × caso em meta de produção por item do edital.

DESCARTADO: usar o curso como fonte de texto, exemplos, tabelas ou questões (D-ESTRATEGIA); criar coordenação nova de reescrita (a Fábrica e a GCB já têm os agentes; ver seção 6, decisão 3); usar a aba Ajustes da matriz do ChatGPT.

## 4. Carga da candidata

O dossiê estima 220 h para o curso de mercado (135 h de teoria, 85 h de baterias). O calendário (D-CRONO v4: DA até 12/12, P1 e P2 a 20 por folha até ~15/11, reverificação 4–8/1, prova 17/1) não comporta isso ao lado das outras duas matérias. Teto proposto para o módulo de DA na plataforma: 37 itens-folha × (curso de 10–15 min + 20 itens) ≈ 45–55 h no total, o que exige que cada tópico caiba em uma unidade de 12–25 "telas" como o dossiê propõe. O número é estimativa desta sessão, para calibrar com a candidata (matéria reservada a PILOT_01: carga horária).

## 5. Ordens à Fábrica (formato FAB-AUTO; rodam só com o "sim" do Fundador)

```
ORQUESTRADOR: LOTE
REMETENTE: Fundador (decisão de 24/10/2026), registrada pela sessão Cowork
DESTINATÁRIO: EXEC (Fábrica)
PROMPT:
a) Objeto: ORDEM_DA_QA12 — conferir os lotes D1 a D6 nos 12 pontos da Parte VI do Dossiê Didático DAD v1 (lista na seção 3, item 1, do plano anexo); emitir errata onde o nosso material divergir da norma vigente; registrar "conferido, sem divergência" onde não divergir.
b) Gerência titular: GCB; executor qa-normativo-da (modelo distinto da produção dos lotes).
c) Escopo: curso, resumo, pares, pegadinhas e justificativas dos 6 lotes de DA; só os 12 pontos.
d) Arquivos-base: lotes D1–D6; mapas normativos dos lotes; DAD/Dossie_Didatico_DAD_v1_2026-10-24.md (Parte VI) — usado só como lista de pontos, nunca como fonte de redação (D-ESTRATEGIA).
e) Regras: toda conferência em texto oficial (Planalto; STF/STJ para teses, com número e data); afirmação sem fonte datada = "[SEM FONTE — não afirmar]"; nenhum trecho do curso de mercado é copiado para o relatório.
f) Saída: saida/qa/QA12_DA_<data>.md com os 12 pontos × 6 lotes, status e erratas; pacote só muda via errata reconciliada.
g) Classificação: AGORA
```

```
ORQUESTRADOR: BANCO
REMETENTE: Fundador (decisão de 24/10/2026), registrada pela sessão Cowork
DESTINATÁRIO: EXEC (Fábrica)
PROMPT:
a) Objeto: ORDEM_CD2026_LOCALIZAR — localizar em cdn.cebraspe.org.br os itens de Direito Administrativo aplicados pela Cebraspe para a Câmara dos Deputados no ciclo cd_25_ns (provas de 8/3/2026), em todos os cargos, e incorporá-los ao banco como CEBRASPE_OFICIAL (órgão-alvo).
b) Gerência titular: GCB; GBQ em cópia.
c) Escopo: cadernos de conhecimentos básicos de todos os cargos do cd_25_ns; itens cujo conteúdo caia nos 12 itens do edital de DA do Cargo 11. As ~15 pistas do dossiê (A02 q. 2–3; A07 q. 1; A09 q. 1; A10 q. 6; A11 q. 1; A15 p. 85; A16 sete itens; A18 q. 1; A19 q. 11, 17, 18) servem só para confirmar que a busca não deixou nada de fora; nenhum texto do curso entra no banco.
d) Arquivos-base: banco/banco.csv; edital/DA_itens_1_12_P1.md; Estado Canônico (ativos do cd_25_ns já anexados: cadernos P3 e padrões definitivos).
e) Regras: texto do caderno oficial, número do item, gabarito definitivo, anulados com X; item_edital pelo conhecimento exigido; rótulo CEBRASPE_OFICIAL só se o certame for a Câmara dos Deputados.
f) Saída: banco atualizado; saida/banco/cd25ns_DA_<data>.md com cadernos abertos, itens localizados por item do edital e lista das pistas do dossiê confirmadas ou não; registro para o Estado Canônico.
g) Classificação: AGORA
```

```
ORQUESTRADOR: LOTE
REMETENTE: Fundador (decisão de 24/10/2026), registrada pela sessão Cowork
DESTINATÁRIO: EXEC (Fábrica)
PROMPT:
a) Objeto: ORDEM_DA_V2 — substituir a ORDEM_DA_FORMATO (19/10) por esta: aplicar o formato ESPEC v2 (seção 2 do plano anexo) aos lotes de DA e produzir as unidades faltantes do edital (2.2, 3.3, 4.1, 8, 9, 10.4–10.7).
b) Gerência titular: GCB; produção Sonnet, QA gcb-cqfp (Opus) com o checklist do QA didático (Parte IV do dossiê) e qa-normativo-da para toda citação.
c) Escopo e ordem: fase 1 = itens 2, 3.4 e 4.4 (maior peso × defeito); fase 2 = unidades novas das lacunas; fase 3 = itens 10, 3.1–3.2, 1.1, 6, 7; fase 4 = acréscimos em 11 e 12 (já canônicos). Cada fase fecha com gatilho A antes da seguinte.
d) Arquivos-base: ESPEC v2 (a ser gravada pela sessão de design a partir da seção 2 do plano); PADRAO_UNICO v1.1; edital (46 entradas P1-DA-); mapas normativos; banco/banco.csv (itens intercalados reais, quando houver); lista de pares e confusões por item do edital extraída da seção 7 dos relatórios DAD/Relatorios_aulas (só os pares, como conhecimento sobre a banca).
e) Regras: D-ESTRATEGIA — nenhum texto, exemplo, tabela ou questão do curso de mercado; casos e exemplos são próprios, de preferência derivados de itens reais do banco; tarefas no formato "dado X, decidir Y"; glossário antes do primeiro uso; uma representação por conceito; pares em três colunas; item intercalado C/E com rótulo e comentário em 3 linhas; fechamento com "o que levar" e "literalidade × caso"; declaração de escopo; 20 itens por item-folha (30 sem real análogo); todo número com norma e data; checa_pacote.py com as regras novas antes da entrega.
f) Saída por fase: pacote novo (número da Fábrica), relatório por lote (tópicos, tarefas, pares, itens intercalados reais × autorais, dispositivos conferidos), parecer de QA didático e normativo, relatório do checa_pacote.py.
g) Classificação: fase 1 AGORA (depois da ORDEM_DA_QA12); fases 2–4 PRÓXIMO; gasto por fase é decisão do Fundador.
```

## 6. Decisões do Fundador (matérias reservadas)

1. Confirmar que a D-ESTRATEGIA se aplica ao dossiê como descrito na seção 1 (método entra; texto, exemplos, tabelas e questões do curso não). Recomendação: SIM — é a regra que você mesmo fixou, e a plataforma vira produto; conteúdo de terceiro dentro dela é risco jurídico e de marca.
2. Incorporar os campos novos (tarefas, glossário, caso, item intercalado, fechamento) à ordem da v17 antes de executá-la, em vez de uma v17.1 depois. Recomendação: SIM; é gasto, mas evita refazer layout.
3. Coordenação nova de reescrita (proposta do dossiê, GDA-CRD) ou Fábrica + GCB com as ordens acima. Recomendação: Fábrica + GCB; os agentes de produção, QA normativo e QA didático já existem, e um chat novo teria de transportar lote por lote pelas suas mãos.
4. Gasto: ORDEM_DA_QA12 e ORDEM_CD2026_LOCALIZAR são pequenas (uma sessão cada); ORDEM_DA_V2 fase 1 é uma rodada de produção completa (três tópicos); fases 2–4 em ondas.
5. Nada vai à candidata antes do gatilho A de cada fase e do seu "sim" (D-AUDITORIA-20OUT).

## 7. Registro para a Secretaria de Estado Canônico (quando o Fundador decidir)

Linhas propostas: D-DOSSIE-DAD (24/10): o Dossiê Didático DAD v1 é insumo de método e de lista de verificação; o curso analisado permanece sob a D-ESTRATEGIA. D-ESPEC-DA-V2 (data da decisão): formato v2 com tarefas, glossário, caso, item intercalado, fechamento e comentário em 3 linhas. D-DA-ORDEM (data): ORDEM_DA_FORMATO substituída pela ORDEM_DA_V2. Pendências: ORDEM_DA_QA12; ORDEM_CD2026_LOCALIZAR; unidades novas 2.2, 3.3, 4.1, 8, 9, 10.4–10.7.
