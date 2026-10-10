# PROMPT DE PARTIDA — CICLO CONTÍNUO (D-PRES-FABRICA)
Trabalhe na branch main. Repita o laço abaixo até uma condição de parada, sem pedir confirmação entre etapas:
1. Execute um CICLO conforme orquestradores/CICLO.md (passos 1 a 5), sem a parada do passo 6.
2. Se PARA_PRESIDENCIA.md tiver itens, delegue ao agente presidencia a decisão de todos eles. Ele grava em DECISOES.md, LOG_PRESIDENCIA.md e, quando couber, PARA_FUNDADOR.md.
3. Commit em main com a mensagem "Ciclo <data-hora>: <n> tarefas, <n> decisões" e push para origin (D-BACKUP). Se o push falhar: imprima "GATE: backup não enviado — decisão humana" e PARE.
4. Condições de PARADA (verificar nesta ordem):
   a) PARA_FUNDADOR.md tem algum item novo neste ciclo;
   b) qualquer GATE foi impresso;
   c) TAREFAS.md não tem tarefa AGORA em estado PENDENTE e o ciclo não gerou decisões novas;
   d) 6 ciclos completos nesta sessão (teto de consumo);
   e) erro de ferramenta, rede ou cota.
   Se nenhuma condição: volte ao passo 1.
5. Ao parar: imprima um resumo (ciclos rodados, tarefas concluídas, decisões tomadas pela presidencia, itens em PARA_FUNDADOR.md, motivo da parada) e "FÁBRICA PARADA — ver PARA_FUNDADOR.md".
