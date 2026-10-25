ORQUESTRADOR: BANCO
REMETENTE: Fundador (decisão de 24/10/2026), registrada pela sessão Cowork
DESTINATÁRIO: EXEC (Fábrica)
PROMPT:
a) Objeto: localizar em cdn.cebraspe.org.br os itens de Direito Administrativo aplicados pela Cebraspe para a Câmara dos Deputados no ciclo cd_25_ns (provas de 8/3/2026), em todos os cargos, e incorporá-los ao banco como CEBRASPE_OFICIAL (órgão-alvo).
b) Gerência titular: GCB; GBQ em cópia (banco e simulados). Executor gbq-cfp (Sonnet); QA independente (Opus) confere 100% dos itens incorporados.
c) Escopo: cadernos de conhecimentos básicos de todos os cargos do cd_25_ns e seus gabaritos definitivos; itens cujo conteúdo caia nos 12 itens do edital de DA do Cargo 11. Pistas a confirmar ao fim (só para checar que a busca não deixou nada de fora; nenhum texto delas entra no banco): cerca de 15 questões rotuladas "Cebraspe – Câmara dos Deputados/2026" no curso de mercado analisado pelo dossiê (temas: organização administrativa; licitações; contratos; controle; responsabilidade civil; regime disciplinar; Lei 9.784 — sete itens; LAI; LGPD — três itens).
d) Arquivos-base: banco/banco.csv (schema D-SCHEMA-02); edital/DA_itens_1_12_P1.md; estado/Estado_Canonico_Camara_2026.md (ativos do cd_25_ns já conhecidos: cadernos P3 e padrões definitivos, com a pasta do concurso no CDN).
e) Regras: texto do caderno oficial, número do item, gabarito definitivo, anulados com X e fora de simulado; item_edital_camara pelo conhecimento exigido, no subitem literal mais específico; rótulo CEBRASPE_OFICIAL só se o certame for a Câmara dos Deputados; itens de outras disciplinas do cd_25_ns NÃO entram (escopo D-ESCOPO-3). Se a listagem do CDN exigir JavaScript, usar os nomes de arquivo já conhecidos e padrões de nome do concurso; registrar cada URL aberta.
f) Saída: banco/banco.csv atualizado (ids BQ sequenciais); saida/banco/cd25ns_DA_<data>.md com cadernos e gabaritos abertos (URL), itens localizados por item do edital, pistas confirmadas/não confirmadas; parecer de QA; linha para o Estado Canônico.
g) Classificação: AGORA
