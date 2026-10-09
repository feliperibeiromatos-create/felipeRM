# TAREFAS — fila da fábrica (v2 — RECONSTRUÇÃO, 9/10/2026). Formato: id; unidade; objeto; classe; estado; agentes; saída
R-01; GBQ; BANCO (reconstrução): varredura TRF6 2024 (034_TRF6_002_01: itens 63, 70–76, 80, 81, 96, 98; anulados 58/105/117), BCB 2024, ANATEL 2024, SUSEP 2025, CNJ 2024, ANTT 2023 (aplicação 14/04/2024) — os 6 certames da primeira varredura; registrar texto_comando e texto_base desde já; ids BQ-0001 em diante; AGORA; PENDENTE; gbq-cfp → gbq-gerencia; banco/banco.csv + saida/banco/varredura_<data>.md
R-02; GBQ; BANCO (reconstrução, 2ª varredura): Embrapa 2025, ANM 2024, SEBRAE 2024 (só C/E; múltipla escolha registrada e excluída, D-MC) + busca por tema para P2 3.x e 4.2; AGORA; PENDENTE; gbq-cfp → gbq-gerencia; banco + varredura
R-03; GBQ; QUALIDADE de todo o banco reconstruído (R-01 e R-02) e guia regras/estilo_banca.md v1.0; AGORA; PENDENTE; gbq-cqe → gbq-estilo → gbq-gerencia; saida/banco/qualidade_<data>.md; regras/estilo_banca.md
R-04; GBQ; SIMULADO 0 v0.2 (diagnóstico, só itens do banco aprovados, agrupados por comando original, avisos de aderência parcial e desequilíbrio C/E); AGORA; PENDENTE; gbq-csc → gbq-gerencia; saida/simulados/simulado_0_v0.2.md + gabarito

## Fila regular (após a reconstrução; T-01 e T-02 ficam absorvidas por R-03 e R-04)
T-03; GBQ; Arbitragem das 7 aderências (após R-03, pelos novos ids) e revisão da tipologia do guia v1.0 → v1.1; AGORA; PENDENTE; gbq-gerencia (com gbq-estilo); regras/estilo_banca.md v1.1
T-04; GCB; Conferência de aplicação e amostragem dos Lotes 6a e 6b (produzidos pela EXEC); gatilho A; AGORA; PENDENTE; gcb-cqfp → gcb-gerencia; saida/gcb/lote6_conferencia.md; PARA_PRESIDENCIA
T-05; GBQ; EXPORTAR — pacote.json v1 com todos os lotes canônicos (regras/pacote_contrato.md); AGORA; PENDENTE; gbq-csc → gbq-gerencia; saida/pacote/pacote.json + relatório
T-06; GBQ; SIMULADO 1 — P1 com itens inéditos dos Lotes 4, 4-C, 5, 5-C (40 itens, sem VOLÁTIL); PRÓXIMO (AGORA após T-05); PENDENTE; gbq-csc → gbq-gerencia; saida/simulados/simulado_1.md + gabarito
T-07; GBQ; Terceira varredura: PF 2025 caderno 004 (identificar cargo), DATAPREV 2023 caderno 003, CTI 2023, TRF6 2024 caderno 012, Câmara 2012 (só com gabarito definitivo no CDN), temas engenharia de prompts e LGPD aplicada a IA; PRÓXIMO; PENDENTE; gbq-cfp → gbq-cqe → gbq-gerencia; banco + varredura
T-08; GCE; Errata: Ato da Mesa nº 225/2025 como contexto (sem item) no curso do Lote 3; PRÓXIMO; PENDENTE; gce-cpp → gce-cqfp → gce-gerencia; saida/gce/lote3_errata_<data>.md
T-09; GCE; Base regimental do aparte (pendência P1 do Lote 2) — Regimento Interno da Câmara, fonte camara.leg.br; PRÓXIMO; PENDENTE; qa-normativo → gce-gerencia; saida/gce/lote2_aparte.md
T-10; GBQ; SIMULADO 2 — P2 com itens inéditos dos Lotes 1, 1-C, 2, 3 (40) + 7 ANALOGA do Lote 3; PRÓXIMO; PENDENTE; gbq-csc → gbq-gerencia; saida/simulados/simulado_2.md + gabarito
T-11; GCE/GCB; Reverificação de janeiro (4–8/1/2027): 15 VOLÁTEIS, fato do curso 1.4, nome Data Studio, ANPD; PRÓXIMO (datado); PENDENTE; gce-cqfp e gcb-cqfp → Gerências; saida/reverificacao_jan2027.md
T-12; TODAS; Atualização do pacote.json a cada gatilho A novo — recorrente; PRÓXIMO; PENDENTE; gbq-csc → gbq-gerencia; saida/pacote/pacote.json
