# varredura_2026-10-09.md — BANCO — 2026-10-08 — gerado por gbq-cfp

Nota de data: o nome do arquivo (2026-10-09) foi definido pelo usuário; a data real do sistema (`date -I`) é 2026-10-08, usada em data_verificacao e neste cabeçalho.

## Método
- Busca web (restrita a cdn.cebraspe.org.br) só para localizar certames/PDFs. Caderno e GAB_DEFINITIVO baixados diretamente de cdn.cebraspe.org.br (curl) e lidos com pdftotext (colunas separadas por recorte). Nenhum espelho usado como fonte.
- Alvo (a): padrão de diretório e código sondado direto no CDN (SEBRAE e ANM por código; Embrapa por varredura de GAB_DEFINITIVO 001–080 até localizar as opções de dados).
- Alvo (b): buscas por tema (LLM, embeddings, busca semântica, sumarização, transcrição, direitos autorais, conteúdo gerado por IA) em cadernos 2025–2026.
- Texto dos itens copiado do PDF, sem alteração (inclusive grafias do original: "dashborad", "ideal atender"). Itens que dependem de texto-base trazem o texto-base nas observações.
- Limite de 6 certames atingido (ver "PDFs que não abriram": 7 certames tocados na fase de localização; o 7º, Câmara PL 2026, não rendeu item). Itens registrados: 20 (abaixo de 60).

## Certames abertos (caderno + gabarito definitivo)
1. Embrapa 2024 (aplicação 23/3/2025), Analista, três opções de dados. Base: https://cdn.cebraspe.org.br/concursos/embrapa_24/arquivos/
   - Ciência de Dados (Opção 40002198): 042_EMBRAPA_ANALISTA_026_01.PDF / Gab_Definitivo_042_EMBRAPA_ANALISTA_026_01.PDF
   - Engenharia de Dados (Opção 40002220): 042_EMBRAPA_ANALISTA_034_01.PDF / Gab_Definitivo_042_EMBRAPA_ANALISTA_034_01.PDF
   - Análise de Dados (Opção 40001648): 042_EMBRAPA_ANALISTA_071_01.PDF / Gab_Definitivo_042_EMBRAPA_ANALISTA_071_01.PDF
   - Também aberto: 028 (Sistemas de Informação): sem item aderente (descartado abaixo).
2. ANM 2024 (aplicação 16/02/2025), Cargo 24 Especialista em Recursos Minerais, TI, Ciência de Dados.
   - https://cdn.cebraspe.org.br/concursos/anm_24/arquivos/038_ANM_024_01.PDF
   - https://cdn.cebraspe.org.br/concursos/anm_24/arquivos/Gab_Definitivo_038_ANM_024_01.PDF
3. SEBRAE 2024 (aplicação 08/09/2024), Perfil 14 Analista Técnico II, Cientista de Dados (004_SEBRAE_014_01). Itens de múltipla escolha A–D; nada registrado no banco (ver adiante).
   - https://cdn.cebraspe.org.br/concursos/sebrae_24/arquivos/004_SEBRAE_014_01.PDF
   - https://cdn.cebraspe.org.br/concursos/sebrae_24/arquivos/GAB_DEFINITIVO_004_SEBRAE_014_01.PDF
4. PF 2025 (Edital 1, 20/5/2025; aplicação 27/07/2025), Cargo 4 Perito Criminal Federal, Área 3 Informática Forense.
   - https://cdn.cebraspe.org.br/concursos/pf_25/arquivos/106_PF_004_01.pdf
   - https://cdn.cebraspe.org.br/concursos/pf_25/arquivos/C3612023C0E2243979FBA27DE2DD60A80FA5FCD9054B4D9664D9E51356E599EE.pdf (gabarito definitivo; nome hash, código interno 106_PF_004_01 impresso no PDF)

Caderno aberto sem gabarito definitivo (não rendem itens; ver descartados): 5. SEFAZ/SE 2025 Auditor TI (P3, itens 91–120); 6. TCE/RN 2025 (item 24, IA generativa); Câmara PL 2026 (item 90, IA generativa).

## Itens registrados (20): BQ-0047 a BQ-0066, todos CEBRASPE_ANALOGA
Embrapa 026 Ciência de Dados: BQ-0047 it.72 P1-8.2 C; BQ-0048 it.93 P1-8.3 E.
Embrapa 034 Engenharia de Dados: BQ-0049 it.91 P1-5.2 E; BQ-0050 it.92 P1-5.2 E; BQ-0051 it.93 P1-5.2 C.
Embrapa 071 Análise de Dados: BQ-0052 it.74 P1-8.2 E; BQ-0053 it.75 P1-8.2 E; BQ-0054 it.81 P1-7.1 C; BQ-0055 it.82 P1-7.1 C.
ANM Cargo 24: BQ-0056 it.55 P2-4.1 E; BQ-0057 it.56 P2-4.1 E; BQ-0058 it.90 P1-5.3 E; BQ-0059 it.91 P1-5.1 C; BQ-0060 it.92 P1-5.3 X (anulado); BQ-0061 it.93 P1-5.3 C; BQ-0062 it.95 P1-5.3 X (anulado); BQ-0063 it.96 P1-5.3 X (anulado); BQ-0064 it.97 P1-5.3 C.
PF Cargo 4: BQ-0065 it.104 P1-5.3 C; BQ-0066 it.105 P1-5.3 C.

Contagem por item do edital: P1-5.1 = 1; P1-5.2 = 3; P1-5.3 = 8 (3 anulados); P1-7.1 = 2; P1-8.2 = 3; P1-8.3 = 1; P2-4.1 = 2. Gabaritos: C 9, E 8, X 3.
Observação: 5.3 e 5.1 aqui também são aderentes a P2-3.x/1.3 apenas por analogia (LLM); marcação mantida em P1.

## Power BI / Tableau / Data Studio (P1-8.3), por certame do alvo (a)
- Embrapa 2024: SIM. Item 93 da opção 026 (Ciência de Dados) cita Tableau e Power BI (gabarito E): registrado como BQ-0048. Data Studio/Looker não aparece. Opções 034, 071 e 028: nenhuma menção às três ferramentas (busca textual no caderno).
- ANM 2024 Cargo 24: NÃO. Nenhum item cita Power BI, Tableau ou Data Studio (itens 106–108 tratam BI e modelagem em geral).
- SEBRAE 2024 Perfil 14: SIM para Power BI (e Qlik Sense), NÃO para Tableau e Data Studio. Itens (múltipla escolha, gabarito A–D no definitivo): Q39 DAX média móvel no Power BI (A); Q40 Power BI x Qlik Sense (C); Q41 visualizações personalizadas Power BI x Qlik (D); Q42 capacidades Power BI x Qlik (C); Q43 dashboard trimestral (B); Q46 dashboard em tempo real (D); Q47 Qlik Sense (A); Q49 Power BI com SQL (A). Também ggplot/matplotlib: Q44 (D), Q45 (X, anulada), Q50 (C). NÃO registrados: o schema fixa gabarito C|E|X e o formato A–D não cabe. DECISÃO HUMANA: estender o schema (nova coluna/valor) ou aceitar o descarte. Não converti itens para C/E (seria criar item).
- Tableau e Data Studio: o único item que cita Tableau em todo o material desta sessão é BQ-0048. Data Studio: nenhum.

## Sem resultado por item do edital (após esta sessão e a anterior)
Destaque obrigatório:
- P2-3.1 (IA em parlamentos: transcrição, sumarização, indexação e busca): nenhum item.
- P2-3.2 (busca semântica em acervos): nenhum item. Termo "embeddings"/"busca semântica" só apareceu em CONTEÚDO PROGRAMÁTICO de edital (TJPA 2025, retificação), não em item de prova.
- P2-3.3 (atas e resumos de sessões): nenhum item.
- P2-3.4 (modelos multilíngues/especializados em português): nenhum item. Itens sobre LLM genérico (BQ-0058, 0064, 0066) são o mais próximo; aderência por analogia.
- P2-4.2 (direitos autorais e ética no uso de IA): nenhum item. Buscas por "direitos autorais"/"conteúdo gerado por IA" não retornaram item de caderno 2025–2026 no CDN; só edital (Embrapa cita Lei 9.610 sem IA) e provas anteriores/vestibular.
- P1-8.3: coberto parcialmente: BQ-0048 (Tableau+Power BI), BQ-0017 e BQ-0035 (sessão anterior, Grafana/Kibana por tema); Power BI no SEBRAE só em formato A–D (não registrado). Data Studio: sem item.
Demais:
- P1-5.1: 1 item (BQ-0059, definição de prompt). Fraco.
- P1-5.2: 13 acumulados; P1-5.3: 14; P1-6: 2 (sem novos); P1-7.1: 5 acumulados (2 novos, métricas/KPIs); P1-8.1: 3 (sem novos); P1-8.2: 3 novos (box plot x2, barras empilhadas); histograma, linha, dispersão: só no SEBRAE (A–D, não registrado); P1-8.4 (storytelling): nenhum item.
- P2-1.x (ASR/transcrição), P2-2.x (degravação), P2-4.3 (pipelines de áudio): nenhum item nos cadernos desta sessão. P2-4.1: apenas LGPD geral (BQ-0056/0057, aderência ampla).
- Termos buscados sem item de prova encontrado: sumarização, busca semântica, embeddings, transcrição (como tema de IA), direitos autorais de IA.

## PDFs/URLs que não abriram ou sem gabarito definitivo
- Câmara PL 2026 (Técnico Legislativo, Policial Legislativo Federal): caderno aberto (.../cd_26_pl/arquivos/6BA6C911910A9996895927100E426BD4733C0601F6E27F998FD96D420A356EDC.pdf; item 90 IA generativa/tokens). Gabarito definitivo NÃO localizado: a busca só retornou um gabarito preliminar (.../cd_26_pl/arquivos/032F32AC416AFC720AD3B303851BB3F8E7984D73E11CFC9A38CE1478A1193DC9.pdf) e esse URL deu HTTP 404 no curl. Item não entra.
- TCE/RN 2025: caderno aberto (.../tce_rn_25/arquivos/ED8518BD51BAD9A2B1B81E90E0F8A6D26AD846B7FD2B3B3BCC0D4DEB6DF415DE.pdf; item 24 modelos de IA generativa fechados); gabarito definitivo não localizado (a busca devolveu só o preliminar; o URL .../C350154870F4D6E9B5DE6053132C307BCB58AE31BAD8DFBC5E0FDC23425CE655.pdf deu 404 no curl). Item não entra. Também não consegui identificar a que cargo o caderno corresponde.
- SEFAZ/SE 2025 Auditor TI: caderno P3 aberto (.../sefaz_se_25_auditor/arquivos/F2DF078E18C57C4C205666B52B19C8FA823D2A4ACC43B1A0E31C0C05D6C7F3D0.pdf, itens 91–120): sem item de IA/LLM/RAG (busca textual), apesar de o edital listar RAG e LLM. Gabarito definitivo (A629E1FF...) não aberto por não haver item.
- Sondagens 404 (nomes errados, sem uso): .../concursos/sebrae_24_ps|SEBRAE_24_PSE_1|... ; .../anm_24|ANM_25|embrapa_25/arquivos/ED_n_..._ABERTURA.PDF ; PF: GAB_DEFINITIVO_106_PF_004_01.PDF/.pdf (o nome real é hash).
- Nenhum PDF registrado veio corrompido. Extração com símbolos matemáticos ilegível em Embrapa 026 (itens 89, 96–100), não registrados (fora do escopo).

## Fontes recusadas
- Nenhuma fonte de terceiros foi usada. Resultados da busca web de agregadores (pciconcursos.com.br, direcaoconcursos.com.br) apareceram só para localizar a existência de cargos (Embrapa Ciência/Engenharia de Dados; ANM Cargo 24; edital ANM em cdn.direcaoconcursos) e foram descartados como proveniência: o código e os cadernos foram confirmados diretamente no CDN do Cebraspe.
- Busca por direitos autorais/IA sugeriu qconcursos/Estratégia como caminho; recusado conforme regras/proveniencia.md.

## Itens descartados e por quê
- SEBRAE 2024 (todos os itens acima): formato múltipla escolha A–D incompatível com o schema; aguardam decisão humana.
- Embrapa 026: itens 71–95 restantes (ANOVA, SIG, ML aplicado a agro, Big Data) fora do escopo; 91/92/94 (APIs, Maple/R) fora.
- Embrapa 034: 94 (CRISP-DM), 96–100 (estatística inferencial) fora de P1-5–8; 71–90 (programação, BPMN, Scrum, DER) fora.
- Embrapa 071: 84 (anonimização de dados agrícolas, C) de aderência fraca a P2-4.1 (sem LGPD explícita); 79/80 (BI e modelos preditivos), 83, 85 (pipelines batch/streaming), 93 (text mining), 94 (análise prescritiva), 98 (machine learning) fora de 5.1–5.3/7.1/8.x ou genéricos demais; 76 e 91 anulados fora de escopo.
- Embrapa 028 (Sistemas de Informação): itens 91–100 de IA/IoT em agricultura (CNN em doenças de plantas, previsão de colheita) específicos de agro; segurança (81–84) genérica.
- ANM 24: 51–54 (ITIL), 57–62, 63–74 (licitações), 75–86 (segurança da informação genérica, incluindo MFA, hash, ICP-Brasil), 87–89 (redes neurais), 94 (Naive Bayes, anulado), 98–114 (nuvem, SQL, CRISP-DM, ETL), 115–117 (data mining, overfitting): fora de escopo ou genéricos. 106 (informação x conhecimento em BI) fora.
- PF Cargo 4: 106 em diante (forense, criptografia) segurança genérica; outros itens de computação fora do escopo.
- Câmara PL 90, TCE/RN 24: sem gabarito definitivo aberto (acima).

## Problemas relatados
- Divergência de data (nome do arquivo 09/10 x sistema 08/10).
- O limite de 6 certames foi ultrapassado em 1 na fase de localização (Câmara PL 2026 aberto antes de saber que não tinha gabarito definitivo); nenhum item dele registrado.
- Rede/CDN funcionou; 404 apenas em URLs sondadas ou índices de busca desatualizados.
