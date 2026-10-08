# ESTADO CANÔNICO — FÁBRICA — Versão F3 — 8/10/2026 — gerado por secretaria
Sincronizar manualmente com o Estado_Canonico_Camara_2026.md do Projeto no claude.ai (Fundador) a cada gatilho A.
## 1. Organograma (agentes)
gce-cpp (sonnet), gce-cqfp (opus), gcb-cpp (sonnet), gcb-cqfp (opus), qa-normativo (opus), gbq-cfp (sonnet, web), gbq-csc (sonnet), corretor-a (sonnet), corretor-b (opus), secretaria (haiku). Presidência: chat no claude.ai (Fable 5.1).
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
- 8/10/2026 — Tarefa BANCO executada em sessão própria, só esta tarefa (agente gbq-cfp).
- 8/10/2026 — BANCO: limite de 6 certames ultrapassado em 1 na fase de localização (Câmara PL 2026), sem item registrado.
## 4. Ativos
edital/, regras/, lotes/, banco/banco.csv (66 itens, BQ-0001 a BQ-0066, todos CEBRASPE_ANALOGA; BQ-0047 a BQ-0066 da varredura de 8/10/2026 com gabarito definitivo do certame), saida/banco/varredura_2026-10-08.md, saida/banco/varredura_2026-10-09.md.
## 5. Pendências abertas
- Liberar domínios de rede; www.planalto.gov.br ainda bloqueado (necessário ao qa-normativo).
- QA comparativo do Lote 5.
- Autorização para rodar Lotes 1–4 aqui.
- Embrapa, ANM e SEBRAE varridos em 8/10/2026. Power BI/Tableau: só BQ-0048 (Embrapa 026 it. 93). Data Studio: sem item.
- DECISÃO HUMANA: SEBRAE 2024 Perfil 14 tem itens de múltipla escolha A–D sobre Power BI/Qlik/dashboards/ggplot (Q39–Q47, Q49, Q50; Q45 anulada) não registrados porque o schema só aceita gabarito C|E|X. Estender o schema ou aceitar descarte.
- Varredura dirigida de 8/10/2026 (termos sumarização, busca semântica, embeddings, LLM, transcrição, direitos autorais, conteúdo gerado por IA, cadernos 2025–2026) a P2-3.1 a 3.4 e P2-4.2: sem item em prova; termos aparecem só em conteúdo programático de edital (TJPA 2025). Sem resultado também: P1-8.4, P2-1.x, P2-2.x.
- Gabaritos definitivos de TCE/RN 2025 e Câmara PL 2026 não localizados (itens sobre IA generativa: TCE/RN item 24; Câmara PL item 90) — revarrer quando disponíveis. Cadernos sem gabarito definitivo localizado: SEFAZ/SE 2025 Auditor TI, TCE/RN 2025, Câmara PL 2026.
- lotes/lote1..4/DESPACHO.md ausentes.
## 6. Log
| Data | Tarefa | Evento |
|---|---|---|
| 8/10/2026 | — | Fábrica v1 instalada |
| 8/10/2026 | BANCO | 6 certames, 46 itens registrados; GATILHO A. |
| 8/10/2026 | BANCO | 4 certames com gabarito definitivo (+3 cadernos sem gabarito), 20 itens (BQ-0047–0066); GATILHO A. |
