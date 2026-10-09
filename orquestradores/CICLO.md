# PROMPT DE PARTIDA — CICLO (uma sessão por ciclo; colar como primeira mensagem)
Trabalhe na branch main. Execute um CICLO conforme CLAUDE.md, sem pedir confirmação entre etapas:
1. Leia DECISOES.md (aplique toda linha marcada NOVA; depois marque-a APLICADA com a data), TAREFAS.md e estado/ESTADO_CANONICO.md.
2. Mova historico/ o PARA_PRESIDENCIA.md anterior (renomeando com a data) e comece um novo, vazio.
3. Para cada tarefa AGORA em estado PENDENTE, na ordem da fila: marque EM CURSO; execute com os agentes indicados (produção sonnet → QA opus, no máximo 2 rodadas; ou verificação/conferência conforme o objeto); entregue o resultado ao agente da Gerência titular (gce-gerencia, gcb-gerencia ou gbq-gerencia), que reconcilia e decide D1; grave as saídas na pasta indicada; marque CONCLUÍDA ou BLOQUEADA (com motivo). Limite por ciclo: 4 tarefas ou o primeiro GATE.
4. Cada Gerência escreve em PARA_PRESIDENCIA.md apenas gatilhos A–E, no formato do agente, e em TAREFAS.md as tarefas novas (classe PRÓXIMO por padrão).
5. Delegue à secretaria a atualização de estado/ESTADO_CANONICO.md e do log do ciclo.
6. Imprima resumo de 10 linhas e "CICLO ENCERRADO — PARA_PRESIDENCIA.md tem N itens". Pare.
