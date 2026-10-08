# PROMPT DE PARTIDA — LOTE (colar como primeira mensagem; substituir N pelo número do lote)
Execute a tarefa LOTE para o Lote N, conforme CLAUDE.md, sem pedir confirmação entre etapas.
1. Leia estado/ESTADO_CANONICO.md e lotes/loteN/DESPACHO.md. Se o lote exigir texto normativo (indicado no despacho), delegue primeiro ao agente qa-normativo e grave em saida/loteN/normativo_*.md.
2. PRODUÇÃO v1 — agente de produção indicado no despacho (gce-cpp para P2; gcb-cpp para P1) → saida/loteN/v1_producao.md.
3. QA1 — agente de QA correspondente (gce-cqfp / gcb-cqfp) → saida/loteN/qa1_relatorio.md. Gate >30%.
4. PRODUÇÃO v2 — mesmo produtor, corrigindo v1 conforme qa1, respondendo item a item → saida/loteN/v2_producao.md.
5. QA2 — mesmo revisor, v2 contra qa1 → saida/loteN/qa2_relatorio.md. Gate >30%.
6. RECONCILIADO — você: (a) conteúdo final aprovado; (b) divergências remanescentes CPP × CQFP, sem decidir mérito; (c) tabela de proveniência de ferramentas e normas; (d) itens AUTORAL aprovados / reprovados / pendentes; (e) hipóteses de discursiva/peça com padrão de resposta (P2) → saida/loteN/RECONCILIADO.md.
7. Delegue à secretaria a atualização do estado. Imprima resumo de 10 linhas e "GATILHO A — aguardando decisão humana". Pare.
