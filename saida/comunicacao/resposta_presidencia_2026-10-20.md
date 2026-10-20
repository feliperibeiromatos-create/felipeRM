# resposta_presidencia_2026-10-20.md — resposta do chat da Presidência à atualização de 20/10/2026

REMETENTE:
PRESIDÊNCIA — Câmara 2026

DESTINATÁRIO:
FUNDADOR

PROMPT:


AUDITORIA DE 20/10: SIM. Mantenho tudo o que foi decidido por delegação. Nada é revertido.
Base: o seu relato e o Estado v61, que li nos pontos de entrega, pacote, gatilho, desvios e branch.
O resultado é forte: 410 itens de Direito Administrativo em seis lotes, com duas rodadas de QA. A pior reprovação foi de 12,5% (D3, na R1), e nenhum lote teve reprovação na R2. TI e Fala ficaram intactos byte a byte, e a v16 está publicada com o seu sim.

Mantenho, com cinco condições. Elas não revertem nada; fecham o que ficou aberto.

1. GATILHO A DA v1.13 (urgente)
A v16 foi publicada antes do fechamento formal do gatilho A da v1.13 (T-118 ainda aberta), com o pacote "aceito com ressalvas" pela gbq-cqe. O rito era o inverso: gatilho fechado primeiro, publicação depois. Ratifico porque havia a sua autorização. Duas regras daqui em diante:
- fechar a T-118 já, com as ressalvas listadas como pendências com responsável;
- nenhuma publicação seguinte antes do gatilho A fechado.

2. MOLDURA DO LEGISLATIVO (prioridade AGORA, e não só no simulado)
Se os itens com contexto da Câmara têm gabarito quase sempre C, a candidata aprende um atalho falso: "se fala da Câmara, é certo". Esse risco já está na plataforma publicada, e não só nos simulados futuros. Peço uma tarefa de conteúdo, não só a regra de montagem da T-119:
- contar, em todo o pacote, os itens com moldura e o C/E deles;
- equilibrar entre 40% e 60%. O caminho: novos itens E com moldura no reforço de DA, mais erratas pontuais com troca legítima, com QA;
- enquanto não equilibrar, aplicar a regra da T-119 no montador.

3. BRANCH E BACKUP (prioridade AGORA)
O trabalho do dia está na branch exec-da-plataforma-2026-10-20, e o Estado diz que ela pode nem estar no GitHub. Pela regra de sempre (toda sessão trabalha em main), as próximas sessões leem a main e não veriam nada disso. E já perdemos uma pasta uma vez. Ordem:
- enviar a branch ao GitHub;
- mesclar na main;
- só então abrir outra sessão.

4. REGRA DE COTA RESTABELECIDA
"Nenhum lote começa com QA do anterior aberto" volta a valer. O paralelismo de D2 a D4 fica ratificado como exceção desse dia, não como precedente.

5. DIAGNÓSTICO
Os 30 itens de DA ficam aceitos. Para não ter dois tamanhos, o diagnóstico da entrada passa a ter até 30 itens por matéria nas três.

DESIGN
A conferência que você pediu continua de pé, agora sobre a v16 publicada e não mais sobre uma versão de revisão. A CDJ recebe o link da v16 e faz a lista de ajustes das três matérias, com a nova estrutura de abas. O bloco à CDJ vai abaixo; mande junto o link da candidata.

LINHAS PARA O DECISOES.md DA FÁBRICA (na main, depois da mesclagem)
NOVA | D-AUDITORIA-20OUT | Presidência, 20/10/2026: ratificadas todas as decisões e desvios por delegação da execução de 20/10 (DA D1 a D6, pacote v1.13, plataforma v16). Condições: (1) a T-118 (gatilho A da v1.13) é fechada antes de qualquer outra tarefa, com as ressalvas da gbq-cqe registradas como pendências com responsável; nenhuma publicação futura antes do gatilho A fechado; (2) volta a valer "nenhum lote novo com QA do anterior aberto"; o paralelismo de D2 a D4 foi exceção; (3) o diagnóstico da entrada tem até 30 itens por matéria nas três matérias.
NOVA | D-MOLDURA-CE | Tarefa AGORA (titular GBQ, execução gcb e gce): contar em todo o pacote v1.13 os itens com moldura do Legislativo (situação na Câmara, no Congresso ou com parlamentar) e o C/E deles, por matéria. Se C passar de 60%: (a) o reforço de DA e as ondas seguintes produzem itens com moldura com gabarito E até a proporção entrar em 40–60%, com troca legítima e QA; (b) erratas pontuais em itens canônicos só com troca legítima, gate de QA e registro de acatamento; (c) até equilibrar, o montador de simulados (T-119) limita os itens com moldura a 50% de C em cada simulado. Relatório saida/banco/moldura_ce_<data>.md.
NOVA | D-BRANCH-MERGE-20OUT | Antes de qualquer sessão nova: enviar a branch exec-da-plataforma-2026-10-20 ao origin e mesclar em main, preservando a v1.13, a v16 e o Estado v61; verificar que a main contém saida/pacote/montagem_v1_13 e saida/plataforma/plataforma_v16_publicar.html; se houver conflito, parar e avisar.

REMETENTE:
PRESIDÊNCIA — Câmara 2026

DESTINATÁRIO:
CDJ — Coordenação de Design e Jornada da Candidata

PROMPT:


Ajuste da tarefa de conferência (Presidência, 20/10). Não haverá uma "versão de revisão": a plataforma v16, com as três matérias e conteúdo real, já está publicada no link da candidata, com o sim do Fundador. O link chega com o Fundador.

Faça a conferência sobre a v16:
- a mesma lista de verificação da reativação;
- a mudança de estrutura (Recomendações, Painel, Simulado leve, Erros);
- Pegadinhas como seção única.

Atenção a duas coisas que a v16 traz e a lista anterior não previa:
(a) Direito Administrativo tem tópicos com resumo, "Em 1 minuto" e visuais (compare e baseLegal). Confira a leitura desses blocos no celular.
(b) O diagnóstico de DA tem 30 itens.

A saída continua a mesma: tabela de achados com prioridade, variações no painel só onde a solução não for óbvia, e pedido de decisão ao Fundador. Você não altera a plataforma.

REMETENTE:
PRESIDÊNCIA — Câmara 2026

DESTINATÁRIO:
Secretaria de Estado Canônico

PROMPT:


Registrar no Estado (v62):

- D-AUDITORIA-20OUT (Presidência, 20/10/2026). A Presidência ratifica a execução de 20/10: Direito Administrativo D1 a D6 com 410 itens, pacote v1.13 com 1.159 itens, plataforma v16 publicada com o sim do Fundador, e os quatro desvios declarados. Condições:
- a T-118 (gatilho A da v1.13) é fechada antes de qualquer outra tarefa, e nenhuma publicação futura acontece antes do gatilho A;
- volta a valer a regra de não abrir lote novo com o QA do anterior aberto; o paralelismo de D2 a D4 fica registrado como exceção;
- o diagnóstico da entrada passa a ter até 30 itens por matéria. Isso altera a D-SIMULADOS-P1P2, que dizia "até 25".
- D-MOLDURA-CE (AGORA, titular GBQ): contar e equilibrar o C/E dos itens com moldura do Legislativo no pacote inteiro. O equilíbrio vem do reforço e de erratas com QA. A regra do montador (T-119) é a medida provisória até lá.
- D-BRANCH-MERGE-20OUT (AGORA): enviar a branch exec-da-plataforma-2026-10-20 ao GitHub e mesclá-la na main antes de qualquer sessão nova.
- A conferência de design da CDJ passa a ser feita sobre a v16 publicada. Deixa de existir a "versão de revisão".

Seção 5:
- abrir "D-MOLDURA-CE — GBQ";
- abrir "mesclagem da branch de 20/10 — Fundador/orquestrador";
- reclassificar a T-118 como primeira da fila;
- fechar "versão de revisão da plataforma — Presidência" (superada pela v16).
