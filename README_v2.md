# FÁBRICA v2 — como instalar e operar

INSTALAR (sessão fechada, branch main): descompactar esta pasta POR CIMA da fábrica v1. Substitui CLAUDE.md; acrescenta 3 agentes de Gerência, orquestradores/CICLO.md, TAREFAS.md, DECISOES.md, PARA_PRESIDENCIA.md, historico/. Nada é removido. Antes do primeiro ciclo: copiar do Projeto para saida/gce/ e saida/gcb/ os arquivos canônicos GCE_* e GCB/* (os agentes de Gerência precisam deles); copiar o Estado Canônico mais recente para estado/.

OPERAR (um ciclo = uma sessão):
1. Se houver decisões novas da Presidência, cole-as em DECISOES.md como "NOVA | D-XXX | enunciado".
2. Abra o Claude Code na pasta e cole o conteúdo de orquestradores/CICLO.md.
3. Ao final, abra PARA_PRESIDENCIA.md. Se tiver itens, cole-o no chat da Presidência; se estiver vazio, não há nada a decidir — rode o próximo ciclo quando quiser.
4. Leve o estado/ESTADO_CANONICO.md atualizado à Secretaria de chat (ela prevalece) quando houver gatilho A aceito.
Transporte por ciclo: dois (PARA_PRESIDENCIA para cá; DECISOES para lá).

O QUE NÃO ESTÁ AUTOMATIZADO, POR DESENHO: aceitar lotes e decidir matéria reservada (Presidência/Fundador); entregar à candidata (Fundador, pela plataforma); liberar rede do ambiente (Fundador). Os chats do claude.ai (GCE, GCB, GBQ, Secretaria) continuam sob demanda e para janeiro; a fábrica não os substitui como registro canônico.

MÉTRICA POR CICLO: tarefas concluídas, gates disparados, itens em PARA_PRESIDENCIA, tempo seu.
