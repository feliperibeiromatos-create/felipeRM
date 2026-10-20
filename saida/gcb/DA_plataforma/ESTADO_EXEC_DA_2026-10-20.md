# ESTADO_EXEC_DA_2026-10-20.md — ordem do Fundador de 20/10/2026 (ORQUESTRADOR: LOTE, EXEC) — 2026-10-20 — gerado por orquestrador
Briefing de continuidade. A sessão parou a pedido do Fundador, depois de concluídas as tarefas em andamento. Branch local: exec-da-plataforma-2026-10-20. O último commit está na linha final do bundle.

## 1. Situação por lote
| Lote | Itens do edital | Estado | Arquivos |
|---|---|---|---|
| D6 | 11, 12 | Canônico (v2.1). Formato plataforma pronto; validador 0 FALHA; fidelidade 0 palavra acrescentada | DA_plataforma/D6_plataforma.json, D6_registro_formato.md |
| D1 | 1 a 2.2 | Canônico (v2). Formato plataforma pronto; validador 0 FALHA | DA_plataforma/D1_plataforma.json, D1_registro_formato.md |
| D5 | 10.1 a 10.7 | v2 pronta; R2 = APROVADO COM RESSALVAS, 0/70 reprovados. Falta: GCB fixar 4 ajustes de texto fora dos itens (parecer R2, seção 9), decidir o ponto 20 (moldura "Considere que um órgão do Poder Legislativo…"; QA indica opção i ou iii), reconciliar, formato plataforma | D5_v2.md, D5_parecer_R1/R2_gcb-cqfp.md, D5_leitura_critica.md |
| D2 | 3.1 a 4.4 | Anexo N (1.365 dispositivos, 0 NÃO CONFERIDO), ficha e v1 em duas partes (80 itens). QA PENDENTE | D2_anexo_N…, D2_ficha_lote.md, D2_v1_parteA/B.md |
| D3 | 5.1 a 7 | Anexo N (298 dispositivos), ficha e v1 em duas partes (80 itens; base doutrinária 26 ≤ teto 33 na parte A). QA PENDENTE | D3_anexo_N…, D3_ficha_lote.md, D3_v1_parteA/B.md |
| D4 | 8 a 9.4 | Anexo N (Decreto 9.203 + 49 dispositivos complementares + 31 trechos oficiais; 7 conceitos SEM FONTE), ficha e v1 em duas partes (79 itens: 73 de folha + 6 de caput). QA PENDENTE | D4_anexo_N…, D4_ficha_lote.md, D4_v1_parteA/B.md |

## 2. Próximos passos, na ordem
1. D2, D3, D4: juntar as partes A e B (script mecânico do orquestrador, seção a seção) → D<n>_v1.md; testar as costuras de gabarito (D4: 33/34 e 73/74).
2. Gerar D<n>_para_leitura_critica.md (cabeçalho neutro, sem itens, por script; a gcb-cqfp confere a neutralidade) e levar ao ChatGPT (autorização do Fundador de 20/10/2026) em paralelo com o R1 (gcb-cqfp).
3. v2 (gcb-cpp: resposta ao R1 + registro de acatamento) → R2 → reconciliação (gcb-gerencia) → formato plataforma (gcb-cpp + validar_da.py) → QA do formato.
4. D5: reconciliação (pontos acima) → formato plataforma.
5. Montagem do pacote (script): edital DA (46 entradas, edital_DA.json) + 6 lotes + itens + topicos; pacote só-DA e v1.13 = v1.12 + DA, com conferência de que a v1.12 fica byte a byte intacta; relatório por lote; parecer de QA final (gbq-cqe).
6. Subir à branch exec-da-plataforma-2026-10-20 do GitHub tudo o que ainda não subiu (na web só foram os 18 arquivos dos três primeiros commits: Anexos D2–D4, leitura e R1 do D5, D1/D6 plataforma, especificação, edital e scripts).

## 3. Pontos para o Fundador ratificar ou decidir
- Desvio declarado: o R1 corre em paralelo com a leitura externa, sem esperar as 48 h da D-DA-PRODUTOR (aplicado no D5; previsto para D2–D4).
- Desvio apontado pelas fichas: D2/D3/D4 abriram com o D5 ainda em QA (D-RITMO-MAX); base = ordem do Fundador de 20/10 (AGORA).
- Volume: 10 itens por folha nesta v1 (precedente D5); a meta de 20 por folha (D-REFORCO-2) fica para onda posterior. D4: 8.1 = 6 e 8.4 = 7 por falta de lastro oficial.
- D1 formatado: o exemplo de cada bloco ganhou a frase "O exemplo é hipotético." (o rótulo original dizia "hipotético"); o D6 não traz a frase. Uniformizar?
- Plataforma v15.4 (fora do escopo da fábrica; D-V15-PLATAFORMA): mapeia curso por prova + "-" + número, o que joga "## 1.1" do DA em P1-1.1 (TI), e conta itens P1-DA no módulo de TI; não lê o quadro BASE LEGAL nem os visuais compare/baseLegal. Precisa de adaptação antes de publicar.
- Alertas normativos: estágio probatório (Lei 8.112, art. 20: 24 meses × Decreto 12.374/2025: 36 meses × CF, art. 41: três anos); EC 140/2026 (16/10/2026) muda o art. 40 da CF depois do edital (fora da prova).
