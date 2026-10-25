# CICLO CONTÍNUO v2 — proposta reconciliada com o estado da fábrica em 25/10/2026 (noite)

Pedido do Fundador: "fazer um ciclo contínuo até terminar tudo". Esta versão substitui a proposta da manhã (que ainda não estava no repositório) e foi conferida contra TAREFAS.md, DECISOES.md e PARA_FUNDADOR.md da sessão s18 (25/10). Não altera orquestradores/CICLO_CONTINUO.md nem CICLO.md: propõe uma variante (seção 3) que o Fundador adota ou não (D-CICLO-V2).

## 0. O que já está feito (não precisa de decisão)
- T-127 ORDEM_DA_QA12: CONCLUÍDA em s18c1 (matriz 12 × 6; 0 gabarito afetado; erratas E1–E6 e F1 aceitas pela GCB, aplicação na T-133).
- D-ESPEC-DA-V2-1 (Fundador, 25/10): adendo v2.1 ADOTADO — caso em 5–10%, `mecanismo` obrigatório, cotas por lote, checa_estilo_DA.py antes da entrega. Isso resolve as antigas D-ADENDO-2.1 e D-CASO da proposta da manhã.
- D-V17-1-ESTILO (Fundador, 25/10): card "Como a Cebraspe constrói o item" em forma discreta; ressalva (a) da QA R5 resolvida.
- D-V17-1-INLINE, D-DOSSIE-DAD, D-ESPEC-DA-V2, D-DA-ORDEM, D-BANCO-LOCALIZADOR: APLICADAS em s18c1.
- Kit DA-v2 (ESPEC v2, adendo v2.1, PADRAO adendo, checa_pacote_v2.py, checa_estilo_DA.py, gcb-cqfp-didatico, 4 ordens, fila v2 de 1.321 candidatos): já no repositório, com as alterações da s18.
- Plataforma v17.1: template, patch, prévia, 67 testes e QA R3–R5 em saida/plataforma/ (T-131, PENDENTE só do build real e do sim de publicação).

## 1. Critério de parada ("terminar tudo")
O ciclo termina quando as seis linhas estiverem SIM, verificadas por script no pacote vigente e registradas no Estado Canônico:
1. Banco real: itens cd_25_ns da Câmara incorporados (T-128); ≥ 30 itens CEBRASPE_OFICIAL/ANALOGA verificados no CDN nos itens de DA onde a fila permite (10.1, 10.2, 7, 11, 1.2, 2.1, 4.4, 3.4, 10.4, 10.5); ≥ 1 em cada item-folha com candidato.
2. Conteúdo: 20 itens por item-folha nas três matérias (30 onde não há real análogo; piso de 10 diretos, D-T97-META-FUNDADOR-RESP), C/E 40–60%, cotas de mecanismo do adendo v2.1 em DA, zero marcas de produção, zero bloqueios em checa_pacote_v2.py, avisos de checa_estilo_DA.py justificados.
3. Formato: todos os tópicos de DA em DA-v2 (fases 1–4); TI e Fala no formato vigente, sem regressão (R1–R9).
4. Lacunas do edital: 2.2, 3.3, 4.1, 8, 9, 10.4–10.7 cobertas e LGPD (12) com unidade própria.
5. Plataforma: v17.1 ou posterior publicada à candidata com o pacote que cumpre 1–4; diagnóstico de entrada com 30 itens de DA (T-124); regressão verde; QA de interface por modelo distinto aprovada.
6. Reverificação de janeiro (4–8/1/2027, T-120 e T-11) com a lista de VOLÁTEIS/REVERIFICAR gerada pelo pacote; a liberação de www.gov.br na rede da fábrica (pedido de 22/10 em PARA_FUNDADOR) decidida antes.
Data-alvo: 12/12/2026 para 1–4 (D-CRONO v4); 5 logo depois; 6 em janeiro.

## 2. A fila (ordens/FILA.md) — espelho de TAREFAS.md, não um segundo estado
A fábrica já tem estado por tarefa em TAREFAS.md (AGORA/PRÓXIMO; PENDENTE/EM CURSO/CONCLUÍDA/BLOQUEADA). A proposta da manhã de uma linha `ESTADO:` dentro de cada ordem fica DESCARTADA: criaria dois estados para a mesma coisa. ordens/FILA.md passa a ser só a leitura ordenada da fila (o que roda a seguir, o que depende de quê, o que espera decisão), atualizada pela secretaria ao fim de cada ciclo. O "sim" do Fundador continua onde sempre esteve: uma linha NOVA em DECISOES.md (o arquivo DECISOES_linhas_novas_2026-10-25.md na raiz traz as linhas prontas, para ele só trocar [SIM/NÃO]).

Fila em 25/10 (ordem de execução):
1. T-128 ORDEM_CD2026_LOCALIZAR — AGORA, PENDENTE.
2. T-130 ORDEM_DA_V2_FASE1 (itens 2, 3.4, 4.4) — AGORA, PENDENTE (não depende mais da T-127; erratas via T-133).
3. T-129 ORDEM_BANCO_DA_CDN_ONDA1 (15 provas, ~415 candidatos) — AGORA, PENDENTE (após T-128).
4. T-133 errata QA12 na consolidação do próximo pacote — PRÓXIMO.
5. T-131 build v17.1 com o pacote DA-v2 real + gatilho A — AGORA, após T-130; publicar depende de D-V17-1-PUBLICAR.
6. T-124 diagnóstico de entrada com 30 de DA — após 2 e 3.
7. ORDEM_BANCO_DA_CDN_ONDA2 (provas 16–40 da fila v2) — a criar; espera D-ONDAS.
8. ORDEM_DA_V2_FASE2 (lacunas 2.2, 3.3, 4.1, 8, 9, 10.4–10.7; LGPD 12 como unidade) — a criar; espera D-ONDAS.
9. ORDEM_DA_V2_FASE3 (10, 3.1–3.2, 1.1, 6, 7) e FASE4 (acréscimos em 11 e 12) — a criar; espera D-ONDAS.
10. ORDEM_BANCO_DA_CDN_ONDA3 (restante) — espera D-ONDAS.
11. T-100/T-116 REFORÇO DA e reforço TI/Fala até 20 por folha — já abertas; entram quando as fases DA-v2 liberarem a GCB.
12. T-120/T-11 reverificação de janeiro — gerar a lista ao fim de cada pacote; executar 4–8/1/2027.
Como as ordens 7–10 ainda não existem como arquivo, a primeira sessão depois de D-ONDAS = SIM as redige (orquestrador + gbq-gerencia/gcb-gerencia), no modelo das ordens de 24/10, e as abre como tarefas PRÓXIMO → AGORA.

## 3. O que muda no laço (D-CICLO-V2, a adotar)
O prompt orquestradores/CICLO_CONTINUO.md já faz o laço (CICLO → presidencia → commit/push → parar por a–e). Três ajustes, só com o sim do Fundador:
a) Parada (a) "PARA_FUNDADOR.md tem item novo" passa a valer só para itens RESERVADA, GATE e AUDITORIA. Itens INFORMATIVO (como os três de s18c1) não param o laço — hoje parariam.
b) Teto de 6 ciclos por sessão continua; o Fundador abre a sessão seguinte com o mesmo prompt. Teto semanal: 5 sessões (D-ONDAS). Relatório semanal em PARA_FUNDADOR.md: as seis linhas da seção 1 com SIM/NÃO e o que falta.
c) Antes de cada entrega de pacote: `python3 -I claude/kit_pacote/checa_pacote_v2.py` (zero bloqueios) e `python3 -I claude/kit_pacote/checa_estilo_DA.py <pacote> --so-v2` (avisos justificados no relatório). Build da prévia: `build_plataforma_v17.py --template saida/plataforma/plataforma_v17_1_template.html --pacote <novo>` + regressao_pacote.py. Publicação à candidata só por D-V17-1-PUBLICAR (seção 4).
Texto do prompt v2 (colar como primeira mensagem da sessão da fábrica, depois de D-CICLO-V2 = SIM):

```
Trabalhe na branch main. Repita o laço abaixo até uma condição de parada, sem pedir confirmação entre etapas:
1. Execute um CICLO conforme orquestradores/CICLO.md (passos 1 a 5), sem a parada do passo 6. Ordem das tarefas AGORA: a de ordens/FILA.md; ao fim, a secretaria atualiza ordens/FILA.md.
2. Se PARA_PRESIDENCIA.md tiver itens, delegue ao agente presidencia a decisão de todos eles.
3. Antes de qualquer entrega de pacote: checa_pacote_v2.py (zero bloqueios) e checa_estilo_DA.py --so-v2 (avisos justificados). Publicação à candidata só se DECISOES.md tiver D-V17-1-PUBLICAR = SIM e as condições dela estiverem cumpridas; senão, só prévia.
4. Commit em main "Ciclo <data-hora>: <n> tarefas, <n> decisões" e push (D-BACKUP). Push falhou: imprima "GATE: backup não enviado — decisão humana" e PARE.
5. PARADA (nesta ordem): a) PARA_FUNDADOR.md ganhou item RESERVADA, GATE ou AUDITORIA neste ciclo (INFORMATIVO não para); b) qualquer GATE; c) nenhuma tarefa AGORA PENDENTE e nenhuma decisão nova; d) 6 ciclos nesta sessão; e) erro de ferramenta, rede ou cota. Senão, volte ao passo 1.
6. Ao parar: resumo (ciclos, tarefas, decisões, itens em PARA_FUNDADOR.md, motivo) e "FÁBRICA PARADA — ver PARA_FUNDADOR.md".
```

## 4. Decisões que ainda faltam (o resto já foi decidido — seção 0)
Linhas prontas em DECISOES_linhas_novas_2026-10-25.md; recomendação desta sessão entre colchetes.
- D-CICLO-V2: adotar a seção 3. [SIM]
- D-V17-1-PUBLICAR: (i) publicar agora a v17.1 com o pacote v1.14 (QA R5 aprovou; ressalva (a) resolvida pela D-V17-1-ESTILO; roteiro de entrada checa → painel → regressão → prévia → sim); (ii) daí em diante, publicar cada pacote ao fim do ciclo quando houver gatilho A, zero bloqueios, R1–R9 verde e QA-plataforma aprovada, sem novo sim por pacote. [SIM a (i) e (ii) — é a única forma de o ciclo não parar a cada pacote; o Fundador mantém o veto por uma linha NOVA. Ressalva: muda a leitura da D-AUDITORIA-20OUT, que exige "sim" por publicação; por isso é dele.]
- D-ONDAS: autorizar de uma vez as ondas 2 e 3 do banco e as fases 2–4 do DA-v2, com teto de 5 sessões por semana e relatório semanal. [SIM — gasto é matéria reservada, por isso vai com teto e pode ser pausada por linha NOVA.]
- D-INLINE-REFAZER: item intercalado respondido pode ser refeito (sem registro, já que não conta nota); implementação na v17.2. [SIM]
- D18/D30: diagnóstico por tópico (D18) e por mecanismo (D30). [BACKLOG até a fase 2; D30 só com ≥ 60 itens com `mecanismo` por matéria.]
- D-MULTI-IA: ChatGPT/DeepSeek como candidata simulada e júri de controvérsias; teste cego de produção na fase 3; reclassificação cega de mecanismos já prevista na ONDA1 (e.8) fica em agente Claude de modelo distinto. Nenhum dado da candidata sai para outro fornecedor. [SIM para candidata simulada e júri; o resto BACKLOG. Adoção de nova IA é matéria reservada.]
- D-CEGO-2 × D6: o qa-normativo-da ainda está proibido de ler o D6 (pendência (1) da s18). [Liberar: o D6 é canônico desde 18/10; o teste cego já aconteceu.]
- D-REDE-GOVBR: liberar www.gov.br:443 na rede da fábrica antes de 4–8/1/2027 (pedido de 22/10). [SIM]

## 5. Classificação
AGORA: seção 3 (D-CICLO-V2), D-V17-1-PUBLICAR, D-ONDAS, ordens/FILA.md. PRÓXIMO: redigir ORDEM_BANCO_DA_CDN_ONDA2 e ORDEM_DA_V2_FASE2–4 (primeira sessão após D-ONDAS); D-INLINE-REFAZER (v17.2). BACKLOG: D18/D30; teste cego multi-IA. DESCARTADO: linha `ESTADO:` dentro das ordens (duplicaria o estado de TAREFAS.md).
