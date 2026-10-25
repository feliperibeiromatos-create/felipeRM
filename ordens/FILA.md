# FILA da fábrica — leitura ordenada de TAREFAS.md (25/10/2026, s19c1)

Este arquivo não é um segundo estado: o estado de cada tarefa é o de TAREFAS.md; o "sim" do Fundador é uma linha NOVA em DECISOES.md. A secretaria reescreve esta tabela ao fim de cada ciclo. A sessão da fábrica executa as linhas AGORA/PENDENTE de cima para baixo (CICLO.md, passo 3).

| # | Tarefa | Ordem / objeto | Classe / estado | Depende de |
|---|---|---|---|---|
| 1 | T-144 | Conferência de vigência da onda 1 de DA no banco (objeto ampliado, D-T129-ONDA1-DEVOLVIDO) — GBQ, qa-normativo-da | AGORA / PENDENTE | — (primeira tarefa da GBQ) |
| 2 | T-136 | ORDEM_DA_V2_FASE2 — lacunas 2.2, 3.3, 4.1, 8, 9, 10.4–10.7 e LGPD 12 (GCB) | AGORA / PENDENTE | T-130 aceita (cumprida em s19c1) |
| 3 | T-131 | Build v17.1 com pacote DA-v2 real (consolidação GBQ dos 60 DV e 7 reais); gatilho A; publicação | AGORA / PENDENTE | T-130 aceita (cumprida); decisão da T-134 |
| 4 | T-134 | PUBLICAR v17.1 + v1.14 — BLOQUEADA: versão publicada 1792774306-636e com mudanças de 23/10 fora da fábrica; item RESERVADA em PARA_FUNDADOR.md | AGORA / BLOQUEADA (Fundador) | decisão do Fundador |
| 5 | T-137 | ORDEM_DA_V2_FASE3 — itens 10, 3.1–3.2, 1.1, 6 e 7 (GCB) | AGORA / PENDENTE | T-136 |
| 6 | T-138 | ORDEM_DA_V2_FASE4 — acréscimos em 11 e 12 (GCB) | AGORA / PENDENTE | T-137 |
| 7 | T-143 | Omitidos de T-128 no cd_25_ns: CG 72, CG 73, E2 95; CG 68 condicional (GBQ) | PRÓXIMO / PENDENTE | — (não depende da devolução da T-129) |
| 8 | T-133 | Errata reconciliada da QA12 (E1–E6, F1) na consolidação do próximo pacote (GCB → GBQ) | PRÓXIMO / PENDENTE | próximo pacote |
| 9 | T-145 | DV3-21: item E de mecanismo SUP, prioridade na tramitação (GCB) | PRÓXIMO / PENDENTE | aceite da T-130 (cumprido em s19c1); pode ir junto com a T-136 |
| 10 | T-146 | Mini-lição do DV1 (P1-DA-2.1) sobre formas de extinção do ato (GCB) | PRÓXIMO / PENDENTE | aceite da T-130 (cumprido em s19c1); entra na T-136 |
| 11 | T-147 | Errata de forma da fase 1 DA-v2 (R-R2-1 a R-R2-6; par art. 57 × prazo; pegadinha ato × fato) (GCB) | PRÓXIMO / PENDENTE | T-131 (consolidação seguinte) |
| 12 | T-149 | A16: comentario, mecanismo e tipo nos itens antigos de D1/D2 de 2.1, 3.4 e 4.4 (GCB) | PRÓXIMO / PENDENTE | aceite da T-130 (cumprido em s19c1) |
| 13 | T-148 | Fase 1 DA-v2 × onda 1 do banco: (a) trocar AUTORAL por itens reais, após novo aceite da T-129 e da T-144; (b) NÃO CORRE até a resposta ao gatilho E (D-COTA-MECANISMO-FUNDADOR) | PRÓXIMO / PENDENTE | (a) T-129 aceita e T-144; (b) resposta do Fundador |
| 14 | T-135 | ORDEM_BANCO_DA_CDN_ONDA2 — provas 16–40 da fila v2 (GBQ) | AGORA / PENDENTE | novo aceite da T-129 |
| 15 | T-139 | ORDEM_BANCO_DA_CDN_ONDA3 — restante da fila v2 (GBQ) | AGORA / PENDENTE | T-135 e novo aceite da T-129 |
| 16 | T-129 | ORDEM_BANCO_DA_CDN_ONDA1 — DEVOLVIDA (D-T129-ONDA1-DEVOLVIDO); reemissão após a T-144 | AGORA / BLOQUEADA | T-144 |
| 17 | T-124 | Diagnóstico de entrada com 30 itens de DA (GBQ) | AGORA / PENDENTE | T-130 (cumprida); T-129 aceita (pendente) |
| 18 | T-100, T-116 | Reforço DA até 20 por folha (piso 10 diretos) | AGORA / PENDENTE | GCB livre das fases DA-v2 (T-136 a T-138) |
| 19 | T-119 | Regra de simulado com DA | PRÓXIMO | T-124 |
| 20 | T-120, T-11 | Reverificação de janeiro (4–8/1/2027): gerar lista a cada pacote; executar em janeiro | AGORA (lista) / janeiro (execução) | D-REDE-GOVBR |
| 21 | T-140 | v17.2 — refazer item intercalado do curso (PLATAFORMA) | PRÓXIMO / PENDENTE | D-INLINE-REFAZER |
| 22 | T-126 | Estudo login/senha por candidata (sem implementar) | PRÓXIMO | — |
| 23 | T-150 | Ferramentas e insumo da fase 1 DA-v2 (GBQ e GCB) | BACKLOG / PENDENTE | — |
| 24 | T-141 | Diagnóstico por tópico (D18) e por mecanismo (D30) (GBQ) | BACKLOG / PENDENTE | D18 após T-136; D30 com ≥ 60 itens com mecanismo por matéria |
| 25 | T-142 | Multi-IA: candidata simulada e júri de controvérsias, fora da fábrica (Fundador) | BACKLOG / PENDENTE | Fundador |

Concluídas em s19c1 (fora da fila): T-128 (D-T128-CD25NS-ACEITE); T-130 (D-T130-DAV2-FASE1-ACEITE).

Pausar uma linha: linha NOVA em DECISOES.md ("pausar T-xxx até <condição>"); a secretaria marca BLOQUEADA em TAREFAS.md com o motivo.
