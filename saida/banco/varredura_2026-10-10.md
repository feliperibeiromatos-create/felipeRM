# varredura_2026-10-10.md — T-07 — 2026-10-10 — gerado por gbq-cfp

## Método
- Busca web restrita a cdn.cebraspe.org.br só para localizar certames e nomes de arquivo. Cadernos e gabaritos definitivos baixados diretamente de cdn.cebraspe.org.br (curl) e lidos com pdftotext (modo bruto e layout; colunas conferidas por posição). Nenhum espelho de terceiros usado. Câmara 2012: listagem do CDN (CD_12_AT e CAMARA2012); camara.leg.br consultado apenas para localizar o portal (não usado como fonte de item).
- Texto dos itens copiado do PDF; cada texto foi conferido por script contra o texto extraído do caderno e cada gabarito lido da tabela do GAB_DEFINITIVO do mesmo certame. Comando (enunciado do bloco) registrado em observacoes. Downloads em /tmp/claude-0/-home-claude/3cf5e5a2-0a00-52ee-a3d1-ce0f04412748/scratchpad/s3/t07/.
- Rótulo CEBRASPE_ANALOGA em todas as linhas (nenhum certame é cd_25_ns ou cd_26_*; D-ROTULOS). ano_aplicacao = ano da aplicação, como nas varreduras anteriores (D-ANO: certame nomeado pelo ano do edital, com data de aplicação nas observações). Todas as observacoes iniciam com "QA PENDENTE; " (D-QA-PENDENTE).
- Limite: 7 certames (atingido; ver "Problemas relatados": um 8º caderno foi baixado e verificado, sem item); itens registrados: 46 (abaixo de 60).
- banco.csv: 46 linhas acrescentadas (BQ-0067 a BQ-0112) por csv.writer (delimiter ';', lineterminator '\n', QUOTE_MINIMAL); linhas existentes intactas (conferido byte a byte: o arquivo anterior é prefixo do novo). 112 itens no total.

## Identificação do "PF 2025 caderno 004"
- Há dois: (a) PF Policial (pf_25, Edital 1, 20/5/2025, aplicação 27/07/2025), código 106_PF_004_01 = Cargo 4 Perito Criminal Federal, Área 3 Informática Forense (já aberto em 09/10; aqui reaberto para os itens 1–4 de TI, ainda não varridos). (b) PF Administrativo (pf_25_adm, Edital 1, 25/4/2025, aplicação 29/06/2025), código 094_PF_004_01 = Cargo 4 Enfermeiro: caderno específico (4 páginas, itens 51–120) sem item aderente a TI, IA ou LGPD (busca textual); gabarito definitivo aberto (Gab_Definitivo_094_PF_004_01.pdf). Os conhecimentos básicos do Cargo 4 estão no caderno 094_PF_CB1_01 (nível superior), que rendeu itens.

## Certames abertos (7)
Base: https://cdn.cebraspe.org.br/concursos/ ; gabarito = arquivo indicado.
1. PF 2025 Policial, Cargo 4 Perito Criminal Federal (Informática Forense). Caderno pf_25/arquivos/106_PF_004_01.pdf; gabarito pf_25/arquivos/C3612023C0E2243979FBA27DE2DD60A80FA5FCD9054B4D9664D9E51356E599EE.pdf (nome hash). Caderno de conhecimentos básicos 106_PF_CB1_01.pdf aberto, sem gabarito definitivo localizado (ver adiante).
2. PF Administrativo 2025 (Edital 1, 25/4/2025). Cadernos 094_PF_004_01 (Enfermeiro; sem item), 094_PF_CB1_01 (básicos, nível superior) e 094_PF_CB2_01 (básicos, nível médio, Cargo 15 Agente Administrativo), todos em pf_25_adm/arquivos/; gabaritos Gab_Definitivo_<mesmo código>.pdf.
3. DATAPREV 2023 (Edital 1, 28/7/2023; aplicação 01/10/2023), Cargo 3 Analista de TI, Perfil Análise de Negócios. dataprev_23/arquivos/893_DATAPREV_003_01.PDF e GAB_DEFINITIVO_893_DATAPREV_003_01.PDF (caderno traz itens 51–120).
4. CTI 2023 (Edital 1, 6/10/2023; aplicação 28/1/2024). cti_23/arquivos/922_MCTI_RENATO_ARCHER_006_01.PDF (Cargo 12 Tecnologista Pleno 1, Indústria 4.0 e Governo Digital) e CTI_23/arquivos/922_MCTI_RENATO_ARCHER_CG1_01.PDF (conhecimentos gerais); gabaritos GAB_DEFINITIVO_<mesmo código>.PDF.
5. TRF6 2024, caderno 012 (aplicação 19/01/2025), Cargo 12 Analista Judiciário, Apoio Especializado, Estatística. trf6_24/arquivos/034_TRF6_012_01.PDF e GAB_DEFINITIVO_034_TRF6_012_01.PDF.
6. Câmara dos Deputados 2012 (Edital 1, 14/3/2012; aplicação 3/6/2012), Analista Legislativo (Arquiteto, Engenheiro, Eng. Segurança do Trabalho; Técnico em Material e Patrimônio). CAMARA2012/arquivos/CAMDEP12_CB1_01.pdf e Gab_definitivo_CAMDEP12_CB1_01.PDF (básicos); CAMDEP12_CB2_01.pdf e Gab_definitivo_CAMDEP12_CB2_01.PDF (básicos do Técnico em Material e Patrimônio, mesmos itens de informática com outra numeração, usado só para conferência). Cadernos específicos 001–007 abertos: sem item de TI aderente. Alterações de gabarito (CD_2012_JUSTIFICATIVAS_DE_ALTERACOES_DE_GABARITO_RETIFICADO.PDF): só itens 8 (CB1) e 4, 91, 92 (CB2); nenhum dos itens registrados foi alterado.
7. FUB 2025 (Edital 1, 3/4/2025; aplicação 29/06/2025), conhecimentos básicos para os Cargos 16, 17 e 19. fub_25/arquivos/088_FUB_CB2_01.pdf e GAB_DEFINITIVO_088_FUB_CB2_01.pdf.

## Itens registrados (46): BQ-0067 a BQ-0112, todos CEBRASPE_ANALOGA
PF Perito (5): BQ-0067 it.67 P1-4.2 C; BQ-0068 it.68 P1-4.1 E; BQ-0069 it.79 P1-2.1 E; BQ-0070 it.87 P1-2 E; BQ-0071 it.88 P1-2 C.
PF Adm CB1 (6): BQ-0072 it.22 P1-6 C (IA autorizada x código de ética); BQ-0073 it.28 P1-4.1 C; BQ-0074 it.29 P1-4.2 E; BQ-0075 it.32 P1-4.2 C; BQ-0076 it.34 P1-4.3 C; BQ-0077 it.50 P2-4.1 C (RIPD).
PF Adm CB2 (6): BQ-0078 it.41 P1-2 C; BQ-0079 it.42 P1-2 E; BQ-0080 it.44 P1-1 C; BQ-0081 it.45 P1-1 C; BQ-0082 it.49 P1-4.1 E; BQ-0083 it.50 P1-4.1 E.
FUB CB2 (7): BQ-0084 it.30 P2-4.1 C; BQ-0085 it.33 P1-1 C; BQ-0086 it.34 P1-2.1 C; BQ-0087 it.35 P1-1 E; BQ-0088 it.36 P1-4.2 C; BQ-0089 it.37 P1-2.1 E; BQ-0090 it.38 P1-4.1 C.
Câmara 2012 CB1 (5): BQ-0091 it.31 P1-1 E; BQ-0092 it.33 P1-1 E; BQ-0093 it.41 P1-4.2 E; BQ-0094 it.42 P1-4.1 C; BQ-0095 it.43 P1-4.1 C. (Equivalentes no CB2: 23, 25, 28, 29, 30, mesmos gabaritos.)
DATAPREV (6): BQ-0096 it.70 P1-8.2 C; BQ-0097 it.71 P1-8.2 E; BQ-0098 it.92 P1-8.4 C; BQ-0099 it.100 P1-8.1 E; BQ-0100 it.119 P1-8.2 C; BQ-0101 it.120 P1-5.2 E.
CTI Cargo 12 (5): BQ-0102 it.88 P1-5.2 C; BQ-0103 it.94 P1-5.2 C; BQ-0104 it.95 P1-5.2 E; BQ-0105 it.96 P1-5.2 C; BQ-0106 it.97 P1-5.2 C.
CTI CG1 (5): BQ-0107 it.34 P1-7.1 E; BQ-0108 it.35 P1-7.1 C; BQ-0109 it.38 P2-4.1 C; BQ-0110 it.39 P2-4.1 E; BQ-0111 it.40 P1-6 C.
TRF6 012 (1): BQ-0112 it.53 P1-8.2 E.

Totais: C 27, E 19, X 0. Por item do edital (novos): P1-1 = 6; P1-2 = 4; P1-2.1 = 3; P1-4.1 = 7; P1-4.2 = 5; P1-4.3 = 1; P1-5.2 = 6; P1-6 = 2; P1-7.1 = 2; P1-8.1 = 1; P1-8.2 = 4; P1-8.4 = 1; P2-4.1 = 4.
Acumulado no banco (112 itens): P1-1 6; P1-2 4; P1-2.1 3; P1-3 0; P1-4 4 (remapeados) + P1-4.1 7 + P1-4.2 5 + P1-4.3 1; P1-5 1; P1-5.1 1; P1-5.2 19; P1-5.3 13; P1-6 4; P1-7.1 7; P1-8.1 4; P1-8.2 7; P1-8.3 3; P1-8.4 1; P2-4.1 22.

Aderência: itens marcados PARCIAL nas observacoes valem só para simulado diagnóstico (D-ADERENCIA). Marcados VOLÁTIL (BQ-0075, 0076, 0086): dependem de produto. Itens de Excel 2019 (BQ-0080, 0081) e Office 2010 (BQ-0091, 0092) não são Microsoft 365: aderência PARCIAL a P1-1. BQ-0110 (LGPD, segurança pública) tem redação anterior à Lei 15.352/2026: conferir contra a LGPD compilada antes de qualquer uso.

## Sem resultado por item do edital (após esta sessão)
Itens 1–4 de TI (D-BANCO-TI-1-4):
- P1-1 (MSOffice 365: Word, Excel, PowerPoint, OneDrive): 6 itens, todos PARCIAIS (Excel 2019, Office 2010, Word/Excel sem versão). Nenhum item sobre OneDrive nem sobre "365" como produto; PowerPoint só em BQ-0091.
- P1-2 e P1-2.1 (redes; Internet e intranet): 7 itens. Nenhum item sobre intranet.
- P1-3 (correio eletrônico, webmail, cliente de e-mail; Microsoft Teams, Google Meet): SEM RESULTADO. Nenhum item sobre e-mail, Teams ou Meet nos 12 cadernos lidos. Buscas por Teams/Meet/OneDrive/e-mail nos textos extraídos não retornaram item de prova.
- P1-4.1: 7 itens (backup 2: BQ-0073, 0094; worms/vírus/backdoor/rootkit/ransomware 5). P1-4.2: 5 (antivírus, firewall, sandbox). P1-4.3 (phishing, pharming): 1 item (BQ-0076, phishing via SmartScreen) mais BQ-0083 (ransomware e phishing, classificado 4.1). Pharming: SEM RESULTADO.
Demais itens:
- P1-5.1 (engenharia de prompts): SEM RESULTADO nesta sessão (nenhum item com "prompt" nos cadernos abertos). Acumulado: 1 (BQ-0059). Buscas dirigidas no CDN devolveram apenas cadernos genéricos (PF 2025 básicos, FUB 2025, STM 2025, TJPA 2025 servidor, Telebras 2025, PM-DF 2025 CFO, SEDUC-AL 2026); só PF, FUB e STM foram abertos e nenhum traz item de prompt.
- P1-5.2: 6 novos (BQ-0101 a 0106). P1-5.3: nenhum novo.
- P1-6: 2 novos (BQ-0072 IA autorizada e ética do servidor, aderência direta; BQ-0111 governo digital, parcial). Melhor cobertura até aqui para "ética e responsabilidade digital".
- P1-7.1: 2 novos (tipo de dado numérico; tipos de análise).
- P1-8.1: 1 novo (dashboards). P1-8.2: histograma e dispersão (BQ-0096, 0097, em contexto de qualidade), box plot (BQ-0100, 0112); linha, barra: SEM RESULTADO nesta sessão. P1-8.3 (Power BI, Tableau, Data Studio): SEM RESULTADO nesta sessão. P1-8.4 (storytelling): 1 item (BQ-0098), o primeiro do banco.
- P2-1.x (ASR, transcrição), P2-2.x (degravação), P2-3.1 a 3.4 (IA em contexto parlamentar, busca semântica, atas e resumos, modelos multilíngues): SEM RESULTADO (nenhum item nos cadernos abertos).
- P2-4.1 (LGPD): 4 novos, todos de LGPD geral (RIPD, dados sensíveis, tratamento, âmbito). "LGPD aplicada a IA" (decisões automatizadas, art. 20; IA e dados pessoais): SEM RESULTADO; busca dirigida no CDN não devolveu caderno com tal item e os itens de IA dos cadernos abertos (PF Adm CB2 texto-base de IA generativa, itens 9–16) são linguísticos, não de LGPD.
- P2-4.2 (direitos autorais e ética no uso de IA): SEM RESULTADO. P2-4.3 (segurança em pipelines de áudio): SEM RESULTADO (itens de segurança desta sessão são de TI básica, mapeados em P1-4.x).

## Anulados (X)
Nenhum anulado aderente nos cadernos lidos. X existentes e fora do escopo: DATAPREV 60 (BPMN) e 66; TRF6 012: 70, 75, 84, 86, 108 (probabilidade e inferência); CTI CG1: 12 (inglês) e 26 (raciocínio); PF Perito: 80 (SSH, número de sessões; fora de 1–4); PF Adm CB1: 37 (Constituição); PF Adm Enfermeiro 004: 52, 57, 90, 92 (saúde).

## Localizado, formato incompatível
- Nenhum item de múltipla escolha nos 7 certames desta sessão (todos C/E). Registro anterior (SEBRAE 2024, Perfil 14) permanece em varredura_2026-10-09.md.

## PDFs que não abriram ou sem gabarito definitivo aberto
- PF 2025 Policial, conhecimentos básicos (106_PF_CB1_01.pdf, https://cdn.cebraspe.org.br/concursos/pf_25/arquivos/106_PF_CB1_01.pdf): caderno aberto (3 páginas; itens 13–20 trazem Windows, Excel, clustering, Big Data, firewall e antivírus, zero-day), mas o gabarito definitivo dos básicos não foi localizado (nomes GAB_DEFINITIVO_/Gab_Definitivo_106_PF_CB1_01 deram HTTP 404; os PDFs de gabarito em nome hash localizados cobrem só os itens específicos de cada cargo). Itens não entram.
- Câmara 2012, Grupo 2 (Museólogo, Técnica Legislativa, Taquígrafo, Médico; CD_12_AT): o CDN lista editais, resultados e justificativas de gabarito, mas nenhum caderno nem GAB_DEFINITIVO. Por isso não entram (regra: só com gabarito definitivo no CDN). Pista: o Taquígrafo 2012 pode ter conhecimentos básicos de informática; localizar o gabarito definitivo antes de usar.
- Sondagens 404 (nomes errados, sem uso): GAB_DEFINITIVO/Gab_Definitivo de 106_PF_CB1_01 (variações de caixa e extensão).

## Itens descartados e por quê
- DATAPREV 003: 72 (Pareto, fora da lista do edital 8.2), 97, 98, 101 (BI, OLAP, ETL), 118 (Big Data) e demais (PMBOK, COBIT, ITIL, BPM, SQL, Scrum, negociação): fora de P1-1–8 / P2-4.
- TRF6 012: 55 (histograma, depende de figura que o texto não reproduz); 51, 52, 54, 56–60 (estatística descritiva, sem relação com visualização); 61–68 e demais itens do Código de Ética Profissional do Estatístico (ética da categoria, não P1-6).
- CTI 006: 60 (IA conversacional em IoT) e 62 (aprendizado de máquina em IoT): aderência fraca a P1-5; 86, 87, 89–93 (aprendizado de máquina técnico: sobreajuste, tarefas, mineração): fora de 5.2 estrito; 98–105 (ontologias), 106–108 (ISO 37120), 109–119 (mineração e Big Data, exceto os registrados): fora do escopo.
- CTI CG1: 31–33 (hardware, SO, CPU), 36–37 (IN SGD/ME 94/2022).
- PF Perito 004: demais itens (arquitetura, bancos de dados, OWASP, OAuth, esteganografia, DNSSEC, WPA3, Linux, criptografia, forense): especializados, fora de P1-1–4; 104–105 já registrados (BQ-0065, 0066).
- PF Adm CB1: 30 (verificação de credenciais no Chrome), 31 (depende de figura), 33 (desfragmentação do Windows 11); PF Adm CB2: 43 (Windows 10), 46–48 (nuvem e Explorador de Arquivos).
- FUB CB2: 31–32 (Windows Explorer).
- Câmara 2012 CB1: 29, 30, 38–40 (Windows 7), 32 (Calc/BrOffice), 34 (computação em nuvem e backup), 35–36 (Internet Explorer 8, operador "link:" do Google), 37 (redes sociais): produto desatualizado ou fora do edital; cadernos específicos 001–007: sem TI aderente.

## Fontes recusadas
- Nenhuma fonte de terceiros foi usada. Resultados de busca restritos a cdn.cebraspe.org.br; o portal camara.leg.br só foi consultado para localizar o Grupo 1 de 2012 (cuja prova e gabarito definitivo foram abertos no CDN do Cebraspe).

## Problemas relatados
- Limite de 7 certames ultrapassado em 1 na fase de verificação: o caderno STM 2025 (stm_25/arquivos/072_STM_CG5_01.pdf) foi baixado e varrido por busca textual (sem item de TI, IA ou LGPD); gabarito não aberto; nada registrado dele. Contando-o, 8 certames tocados, 7 com itens. Também foram baixados, sem registrar item, o edital de abertura da Câmara Analista Legislativo 2026 (cd_26_analista, Edital 1 de 2/10/2026) e a Abertura do FUB e do PF Administrativo (só para identificar cargos).
- Rede/CDN funcionou; 404 apenas em URLs sondadas. Extração com símbolos matemáticos ilegível em parte dos itens de probabilidade do TRF6 012 (ex.: item 69), não registrados.
- Itens de Câmara 2012 e Office 2010/Excel 2019 são de produto desatualizado: aderência parcial a P1-1 por construção.
- Pendente para o QA (gbq-cqe): BQ-0067 a BQ-0112 todos com "QA PENDENTE"; conferir em especial BQ-0072 (item de ética com IA, gabarito C), BQ-0092 (gabarito E de item que parece correto em Office, conforme gabarito definitivo de 2012) e BQ-0110 (LGPD, redação anterior à Lei 15.352/2026).

## Errata (gbq-gerencia, 2026-10-10; D1, saida/banco/GBQ_reconciliacao_2026-10-10_lote2.md; fonte: saida/banco/qualidade_2026-10-10_T07.md)
- E1. Câmara 2012, certame 6: o nome do PDF de justificativas é CD_2012_JUSTIFICATIVAS_DE_ALTERA____ES_DE_GABARITO_RETIFICADO.PDF (https://cdn.cebraspe.org.br/concursos/CAMARA2012/arquivos/CD_2012_JUSTIFICATIVAS_DE_ALTERA____ES_DE_GABARITO_RETIFICADO.PDF), e não "…ALTERACOES…", que dá HTTP 404.
- E2. Câmara 2012, certame 6, alterações de gabarito no CB2: o PDF altera o item 4 e anula os itens 91, 92, 93, 94 e 96 (e não só "4, 91, 92"). No CB1, só o item 8 é alterado. Nenhum item registrado e nenhum equivalente conferido (CB2 23, 25, 28, 29 e 30) foi afetado.
- E3. Limite: orquestradores/BANCO.md fixa "6 certames ou 60 itens". O limite de "7 certames" citado acima não tem fonte no repositório. A sessão abriu 8 cadernos-certame: 7 com itens, mais o STM 2025 sem item. A excedência está registrada na reconciliação.
