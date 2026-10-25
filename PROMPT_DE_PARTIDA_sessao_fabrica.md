# Prompt de partida da sessão da Fábrica (colar no Claude Code, na raiz do repositório felipeRM, depois do commit do kit)

Leia, nesta ordem: CLAUDE.md; estado/Estado_Canonico_Camara_2026.md; orquestradores/CICLO_CONTINUO.md; DECISOES.md (linhas D-DOSSIE-DAD, D-ESPEC-DA-V2, D-DA-ORDEM e D-BANCO-LOCALIZADOR, de 24/10/2026); claude/ESPEC_curso_DA_formato_v2_2026-10-24.md; claude/PADRAO_UNICO_v1_1_adendo_DA-v2.md.

Há quatro ordens novas em ordens/: ORDEM_DA_QA12, ORDEM_CD2026_LOCALIZAR, ORDEM_BANCO_DA_CDN_ONDA1 e ORDEM_DA_V2_FASE1. Execute UMA ordem por sessão, nesta ordem: QA12 → CD2026_LOCALIZAR → BANCO_DA_CDN_ONDA1 → DA_V2_FASE1. Respeite a trava SESSAO_EM_CURSO.lock (sessões consecutivas, nunca simultâneas, D-RITMO-MAX).

Para cada ordem: use o orquestrador indicado na primeira linha; produção e QA em subagentes de modelos distintos (quem produz não revisa); máximo de 2 rodadas de QA; ao fim, gatilho A (ou devolução) registrado em TAREFAS.md e no Estado Canônico local pelo subagente secretaria; commit; RESUMO com a sentinela "FIM DA EXECUÇÃO". Matéria reservada (gasto além da ordem, publicação, exclusão de ativo, adoção de ferramenta) vai para PARA_FUNDADOR.md e para; não decida.

Antes de entregar qualquer pacote da ORDEM_DA_V2_FASE1, rode `python3 -I claude/kit_pacote/checa_pacote_v2.py <pacote vigente> <pacote novo> --registro <registro> --saida saida/conferencia_<data>.md` e exija zero bloqueios. Nenhum trecho, exemplo, tabela ou questão de curso de terceiro entra em nenhum arquivo (D-ESTRATEGIA); referência explícita é bloqueio do script.

Ao terminar a sessão, escreva em PARA_FUNDADOR.md: ordem executada, resultado em três linhas, próximo passo e o que depende de "sim" (gasto da onda 2 do banco; fases 2–4 da DA_V2; publicação).
