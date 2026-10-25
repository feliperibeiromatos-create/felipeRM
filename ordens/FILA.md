# FILA da fábrica — leitura ordenada de TAREFAS.md (25/10/2026, noite)

Este arquivo não é um segundo estado: o estado de cada tarefa é o de TAREFAS.md; o "sim" do Fundador é uma linha NOVA em DECISOES.md. A secretaria reescreve esta tabela ao fim de cada ciclo. A sessão da fábrica executa as linhas AGORA/PENDENTE de cima para baixo (CICLO.md, passo 3).

| # | Tarefa | Ordem / objeto | Classe / estado | Depende de |
|---|---|---|---|---|
| 1 | T-128 | ORDEM_CD2026_LOCALIZAR — itens de DA do cd_25_ns no CDN, CEBRASPE_OFICIAL | AGORA / PENDENTE | — |
| 2 | T-130 | ORDEM_DA_V2_FASE1 — itens 2, 3.4, 4.4 em DA-v2 (ESPEC v2 + adendo v2.1) | AGORA / PENDENTE | — (erratas da QA12 via T-133) |
| 3 | T-129 | ORDEM_BANCO_DA_CDN_ONDA1 — 15 provas, ~415 candidatos; `mecanismo`; reclassificação cega de 100 | AGORA / PENDENTE | T-128 |
| 4 | T-133 | Errata reconciliada da QA12 (E1–E6, F1) na consolidação do próximo pacote | PRÓXIMO / PENDENTE | próximo pacote |
| 5 | T-131 | Build v17.1 com pacote DA-v2 real; gatilho A; publicação | AGORA / PENDENTE | T-130; D-V17-1-PUBLICAR |
| 6 | T-124 | Diagnóstico de entrada com 30 itens de DA | AGORA / PENDENTE | T-130, T-129 |
| 7 | — | ORDEM_BANCO_DA_CDN_ONDA2 (provas 16–40 da fila v2) — a redigir | a abrir | D-ONDAS |
| 8 | — | ORDEM_DA_V2_FASE2 (2.2, 3.3, 4.1, 8, 9, 10.4–10.7; LGPD 12 como unidade) — a redigir | a abrir | T-130; D-ONDAS |
| 9 | — | ORDEM_DA_V2_FASE3 (10, 3.1–3.2, 1.1, 6, 7) e FASE4 (11 e 12) — a redigir | a abrir | 8; D-ONDAS |
| 10 | — | ORDEM_BANCO_DA_CDN_ONDA3 (restante da fila v2) — a redigir | a abrir | 7; D-ONDAS |
| 11 | T-100, T-116 | Reforço DA até 20 por folha (piso 10 diretos) | AGORA / PENDENTE | GCB livre das fases DA-v2 |
| 12 | T-119 | Regra de simulado com DA | PRÓXIMO | 6 |
| 13 | T-120, T-11 | Reverificação de janeiro (4–8/1/2027): gerar lista a cada pacote; executar em janeiro | AGORA (lista) / janeiro (execução) | D-REDE-GOVBR |
| 14 | T-126 | Estudo login/senha por candidata (sem implementar) | PRÓXIMO | — |

Pausar uma linha: linha NOVA em DECISOES.md ("pausar T-xxx até <condição>"); a secretaria marca BLOQUEADA em TAREFAS.md com o motivo.
