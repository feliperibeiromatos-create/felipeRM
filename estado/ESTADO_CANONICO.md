# ESTADO CANÔNICO — FÁBRICA — Versão F3 — 8/10/2026 — gerado por secretaria
Sincronizar manualmente com o Estado_Canonico_Camara_2026.md do Projeto no claude.ai (Fundador) a cada gatilho A.
## 1. Organograma (agentes)
gce-cpp (sonnet), gce-cqfp (opus), gcb-cpp (sonnet), gcb-cqfp (opus), qa-normativo (opus), gbq-cfp (sonnet, web), gbq-csc (sonnet), gbq-cqe (opus), gbq-estilo (opus), corretor-a (sonnet), corretor-b (opus), secretaria (haiku). Presidência: chat no claude.ai (Fable 5.1).
## 2. Plano de lotes
| Lote | Itens | Status |
|---|---|---|
| 1 RF-ASR | P2 1.1–1.8 | em produção manual (GCE claude.ai); não rodar aqui sem ordem |
| 2 RF-DEGRAVACAO | P2 2.1–2.8 | não iniciado |
| 3 RF-IA-PARLAMENTAR + RF-PROTECAO | P2 3.1–4.3 | não iniciado |
| 4 TID-IA | P1 5.1–5.3, 6 | em produção manual (GCB claude.ai); não rodar aqui sem ordem |
| 5 TID-DADOS-VIZ | P1 7.1, 8.1–8.4 | concluído no piloto; QA comparativo em curso |
## 3. Decisões vigentes
Ver Estado Canônico do Projeto (claude.ai). Aqui só o que a fábrica registrar por gate.
- 8/10/2026 — Tarefa BANCO executada na mesma sessão do piloto Lote 5 e da instalação da Fábrica v1, por ordem expressa do Fundador (exceção à regra "uma tarefa por sessão").
- 8/10/2026 — Tarefa QUALIDADE-ESTILO executada por ordem expressa do Fundador (não consta de orquestradores/; sem prompt de partida próprio). Anulações: "X" no gabarito definitivo basta como prova; PDF de justificativas é complemento.
## 4. Ativos
edital/, regras/, lotes/, banco/banco.csv (46 itens, BQ-0001 a BQ-0046, todos CEBRASPE_ANALOGA, gabaritos conferidos com os PDFs definitivos), saida/banco/varredura_2026-10-08.md.
- saida/banco/qualidade_2026-10-09.md (QA do banco: 46 verificadas, 45 APROVADAS, 1 CORRIGIR, 0 NÃO VERIFICÁVEIS).
- regras/estilo_banca.md v1.0 (base 42 itens efetivos de 6 certames: 45 aprovados menos 3 anulados; 24 C / 18 E).
- regras/estilo_banca_semente.md (semente anterior, renomeada de regras/estilo_banca.md, só referência).
## 5. Pendências abertas
- Liberar domínios de rede; www.planalto.gov.br ainda bloqueado (necessário ao qa-normativo).
- QA comparativo do Lote 5.
- Autorização para rodar Lotes 1–4 aqui.
- Próxima varredura de banco: Embrapa 2025 (Ciência/Engenharia de Dados), ANM 2024 Cargo 24, SEBRAE 2024 (004_SEBRAE_014_01, indicado com itens de Power BI, não aberto).
- Varredura dirigida a P2-3.1 a 3.4 e P2-4.2 (sem resultado na varredura de 8/10/2026).
- lotes/lote1..4/DESPACHO.md ausentes.
- BQ-0025 (ANATEL it.84): campo observacoes não registra alteração de gabarito C (preliminar) → E (definitivo); correção cabe à GBQ (banco não foi alterado).
- Justificativas de anulação não localizadas (BQ-0029, 0030, 0031; e BQ-0025 alteração): nomes testados no CDN deram 404; apis.cebraspe.org.br bloqueado pelo proxy.
- SUSEP: gabarito preliminar não localizado; alterações das 7 linhas SUSEP não conferidas.
- 7 divergências de aderência registradas sem decisão (BQ-0001, 0009, 0014, 0015, 0016, 0036, 0040).
- Vigência das normas nos itens (LGPD, Marco Civil, Resolução CNJ) e afirmações sobre ferramentas não verificadas → qa-normativo (planalto.gov.br ainda bloqueado). O gbq-cqe mencionou alteração da LGPD por uma "Lei 15.352/2026" — afirmação NÃO verificada pelo orquestrador.
- Classificação dos itens por padrão em estilo_banca.md é julgamento do gbq-estilo; revisão humana.
- CLAUDE.md não lista gbq-cqe, gbq-estilo nem a tarefa QUALIDADE-ESTILO.
## 6. Log
| Data | Tarefa | Evento |
|---|---|---|
| 8/10/2026 | — | Fábrica v1 instalada |
| 8/10/2026 | BANCO | 6 certames, 46 itens registrados; GATILHO A. |
| 8/10/2026 | QUALIDADE-ESTILO | QA banco 45/46 aprovadas; estilo_banca v1.0; GATILHO A. |
