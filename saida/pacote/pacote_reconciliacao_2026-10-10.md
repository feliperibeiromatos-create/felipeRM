# pacote_reconciliacao_2026-10-10.md — T-05 — 2026-10-10 — gerado por gbq-gerencia

REMETENTE: GBQ — Gerência de Banco de Questões e Simulados
DESTINATÁRIO: orquestrador (roteamento e estado da T-05); GCB e GCE (tarefas de suas unidades, para conhecimento); Presidência: nenhum gatilho neste ciclo
Entrada: `saida/pacote/pacote.json` e `saida/pacote/pacote_relatorio.md` (T-05, gbq-csc, 10/10/2026). Regras aplicadas: CLAUDE.md (com o Adendo v2.1), DECISOES.md (D-CANONICOS, D-LOTE6A-CANONICO, D-LOTE6B-CANONICO, D-SIM0-V02, D-PACOTE-6, D-BANCO-TI-1-4, D-QA-PENDENTE, D-ADERENCIA, D-DEREP), `regras/pacote_contrato.md`, TAREFAS.md (T-05, T-12, T-17, T-25), `saida/gcb/lote6_reconciliacao.md` e `saida/simulados/T15_T22_reconciliacao_2026-10-10.md`. Papéis: gbq-gerencia e gce-gerencia.

A conferência foi feita por script, somente leitura. O script carregou o JSON e o comparou com `banco/banco.csv` (csv, `;`), com o registro `saida/gbq/claude_GBQ_Registro_AUTORAL_v2.md` (150 linhas de item) e com as linhas d-G dos arquivos `saida/gcb/GCB_Lote6a_v2_producao_auto.md` e `GCB_Lote6b_v2_producao_auto.md`. A GBQ não editou o pacote nem outros arquivos.

## 1. Conferência das contagens

| Objeto | Pacote | Fonte canônica | Resultado |
|---|---|---|---|
| itens (total) | 240; 122 C / 118 E; 0 ids duplicados | 60 banco + 180 AUTORAL | confere |
| banco | 60; 33 C / 27 E; todos CEBRASPE_ANALOGA | banco.csv: 66 linhas (33 C, 27 E, 6 X). Os 6 anulados (BQ-0029, 0030, 0031, 0060, 0062, 0063) ficaram fora | confere. Mesmo conjunto de ids; gabarito, subitem e texto 60/60 |
| AUTORAL L1 / L1-C / L2 / L3 | 20 (10/10) / 10 (4/6) / 30 (15/15) / 30 (16/14) | registro v2 | confere |
| AUTORAL L4 / L4-C / L5 / L5-C | 20 (10/10) / 10 (5/5) / 20 (10/10) / 10 (5/5) | registro v2 | confere. Os 150 do registro estão todos no pacote: gabarito 150/150, subitem 150/150 |
| AUTORAL L6a / L6b | 15 (7/8) / 15 (7/8) | d-G do 6a e do 6b; D-LOTE6A/6B-CANONICO | confere 15/15 cada |
| AUTORAL (total) | 180; 89 C / 91 E; aderência "direta" 180/180 | — | confere |
| VOLÁTIL (`"volatil": true`) | 18. Banco 4: BQ-0015, 0017, 0035, 0064. AUTORAL 14: L1-Q14, Q16, Q18, Q19; L4-15; A5-14 a 17; 6A-01, 09, 10, 14, 15 | banco (prefixo VOLÁTIL) 4; registro v2 9; 6a 5; 6b 0 | confere. Falta L3-Q21: ver ponto (e) |
| aderência do banco | 37 direta / 23 parcial. Parciais: 17 P2-4.1, 2 P1-8.3, 1 P1-5.3, 1 P1-6, 1 P1-7.1, 1 P1-8.1 | contagens-alvo da GBQ na T-25 (T15_T22_reconciliacao, D1 3) | confere exatamente |
| QA PENDENTE | 0 no banco e 0 no JSON | D-QA-PENDENTE | confere |
| edital | 47 entradas (P1 20, P2 27), sem duplicata; todo `itemEdital` existe | edital/ (3 arquivos) | confere |
| simulados | 1 (SIM-0, diagnóstico): 60 ids do banco, 33 C / 27 E, 4 VOLÁTEIS, 23 parciais | simulado_0_v0.2 + gabarito | confere com o banco. O documento do simulado ainda diverge do banco em 5 itens (T-25) |
| comando dos itens de banco | 60/60 não vazios e literais do simulado; 34 comandos distintos = 34 blocos "Comando" | simulado_0_v0.2.md | confere. textoBase só em BQ-0049, 0050 e 0051 |
| lotes | 10. Curso, resumo, pares e pegadinhas conforme o relatório; L4C e L5C vazios | — | confere |
| discursivas | 5 (D1, D2, D4 questão: 14,30 + 0,70; D3, D5 peça: 28,50 + 1,50) | padrões GCE | confere |

Achados que corrigem o relatório da produtora (não alteram contagem):
- **DETAQ.** Há 10 ocorrências no JSON. Uma só está fora da forma de D-DEREP, no curso do L2 ("…pelo Departamento de Taquigrafia, Revisão e Redação (DETAQ) […], hoje Departamento de Registro Oficial e Redação Parlamentar, por força do Ato da Mesa nº 251/2026"). O relatório fala em 2. A grafia "Derep, antigo DETAQ" aparece uma vez no L1 (texto da E10), uma no L6A e uma no L6B. Ao contrário do que diz o relatório (seção 5, item 3), os Lotes 6 ainda não trazem só a forma "Derep (antigo DETAQ)": OB-6a-2/OB-6b-2, objeto da T-17(b), continuam no texto exportado.
- **OB-6b-1 está no JSON.** O curso 4.0.2 do L6B traz uma ocorrência de "Observação para a GCB-CQFP: a Lei 14.129/2021 … não fundamenta item".

## 2. Reconciliação ponto a ponto (D1 GBQ)

### (a) Erratas T-17 dos Lotes 6 não aplicadas: BLOQUEIO
- A produtora agiu certo ao exportar o texto literal sem corrigir.
- OB-6b-1 é bloqueante da exportação do 6b, como a GCB declarou em lote6_reconciliacao.md (seção 3). A nota interna à GCB-CQFP está no curso exportado do L6B. Por isso o pacote v1 **não é liberável**.
- OB-6a-2/OB-6b-2 (grafia do Derep) não bloqueiam, mas são corrigidos na mesma errata. OB-6b-3, a linha CQFP-1 e TRF6 96/98 não chegam ao JSON.
- **Decisão:** o pacote não será refeito por recorte. A GBQ não retira o L6B nem edita o texto do curso, que é da GCB. A liberação espera a T-17 concluída e reconciliada pela GCB, seguida da regeração (T-27).
- A T-17 é tarefa da GCB, classe PRÓXIMO, e agora está no caminho crítico do pacote. A GBQ registra isso para o orquestrador e a GCB. Reclassificar a T-17 cabe à GCB ou à Presidência.
- **Classe: AGORA (bloqueio registrado). Resolve: T-17 → T-27.**

### (b) Regra de aderência estendida: ACEITA
- A regra literal do prompt EXPORTAR ("observacoes contendo 'parcial'") é só um atalho de mapeamento. O critério de mérito é D-ADERENCIA aplicado pela arbitragem da GBQ (T-03, T-22).
- O resultado da regra estendida coincide item a item com as contagens-alvo da GBQ na T-25: 23 parciais, distribuídos como 17 P2-4.1, 2 P1-8.3, 1 P1-5.3, 1 P1-6, 1 P1-7.1 e 1 P1-8.1.
- A regra literal marcaria só 5 parciais e liberaria 18 itens a simulado final contra D-ADERENCIA. Seria o erro.
- **Decisão D1:** "aderência temática ampla" e "aderência apenas por tema" valem como parcial. O mapeamento vai para o contrato (T-26).
- **Classe: DESCARTADO como pendência** (o pacote está correto). O registro no contrato fica PRÓXIMO (T-26).

### (c) comando e textoBase extraídos do simulado e de observações: ACEITOS para v1
- banco.csv não tem as colunas texto_comando e texto_base (SCHEMA.md), apesar da instrução da R-01.
- Os 60 itens exportados estão no Simulado 0 v0.2, que copia os comandos dos cadernos oficiais. Conferido: 60/60 literais e 34/34 blocos.
- Para BQ-0049 a 0051, a separação entre textoBase e comando segue a nota "texto-base do comando (copiado do PDF)" das observações. É mapeamento, sem texto novo.
- O atalho não serve para item do banco que não esteja num simulado, como os da T-07. Daí a T-29: colunas próprias no banco antes de itens novos entrarem no pacote.
- **Classe: DESCARTADO para v1; PRÓXIMO (T-29).**

### (d) SIM-0 v0.2 incluído com o simulado divergente do banco: NÃO LIBERÁVEL no estado atual
- Na reconciliação T15_T22, a GBQ (D1 1) decidiu que a T-25 vem "antes de qualquer inclusão do Simulado 0 v0.2 no pacote (T-12)". D-PACOTE-6 pede o simulado "quando estiver pronto".
- D-SIM0-V02 condiciona o uso pela candidata à T-13 concluída sem gatilho D. A plataforma não tem campo para conter o uso: o que entra no pacote liberado fica disponível.
- O SIM-0 do JSON é só uma lista de ids, e as aderências vêm do banco, que está certo. Por isso não há erro de dado no v1. Mesmo assim, o simulado não está "pronto" no sentido da decisão.
- **Decisão D1:** o SIM-0 só entra num pacote liberável depois de duas condições: a T-25 concluída e reconciliada pela GBQ (mapa = banco 60/60) e a T-13 concluída sem gatilho D. Na regeração (T-27), se faltar qualquer uma, `simulados` sai vazio e o relatório registra o motivo. Liberar o simulado à candidata continua reservado ao Fundador.
- **Classe: AGORA (T-25, já na fila); condição registrada na T-27.**

### (e) Demais pontos
| Ponto | Decisão D1 | Classe |
|---|---|---|
| L4C e L5C sem curso, resumo e pares | São complementos só com itens, por construção; o curso está nos Lotes 4 e 5 e o nome do lote já diz "complemento". Ficam em `lotes` porque os itens precisam de lote para o teste de lote (D-ONBOARDING). Sem ação. | DESCARTADO |
| [TS] não exportado | O contrato não tem campo e a candidata não precisa da marca para estudar. Fica disponível no registro e nos arquivos canônicos. Extensão só se a plataforma pedir. | BACKLOG |
| Bloco R1–R5 do Lote 3 fora do `padrao` de D4/D5 (domínio GCE; a GBQ decide só a exportação) | R1 e R5 são processo interno: não vão. R2, R3 e R4 são critérios de aceitação e tolerância que mudam a autocorreção: R2 (alínea c sem exigir enquadramento como obra ou ato oficial), R3 (voz como dado sensível nem exigida nem penalizada) e R4 (art. 23 ou art. 7º, II ou III). O script confirmou que o `padrao` de D4 não cita o art. 23. Decisão: anexar R2–R4, literais, como "Notas de correção (GCE, R2–R4)" ao `padrao` de D4 e D5 na regeração. É cópia do texto reconciliado da GCE, sem texto novo. | PRÓXIMO (T-27) |
| "DETAQ" literal no curso do L2 (D-DEREP; errata E4 da consolidação do L2) | É 1 ocorrência no JSON. O fato está certo, porque o trecho já informa o nome atual e o Ato da Mesa 251/2026, mas a forma de D-DEREP não está aplicada. A E4 fixa a regra de leitura, não um texto de substituição, por isso a produtora não podia aplicá-la. Vai para errata de forma da GCE, sem mudar gabarito. Não bloqueia o pacote. A forma "(Derep, antigo DETAQ; Ato…)" do L1, vinda da E10, fica aceita, porque o parêntese já existe e o sentido é idêntico. | PRÓXIMO (T-28) |
| L3-Q21 (REVERIFICAR normativo) sem marca | Pela regra R1-N do registro GBQ v2, REVERIFICAR normativo tem o mesmo tratamento do VOLÁTIL: inapto a simulado final até 4–8/1/2027. A plataforma só conhece `volatil`, e sem a marca poderia usar o L3-Q21 em simulado final. Decisão: na regeração, L3-Q21 sai com `"volatil": true` (total 19: banco 4, AUTORAL 15). O contrato passa a dizer que `volatil` cobre também o REVERIFICAR normativo. | PRÓXIMO (T-27 e T-26) |
| Campo `volatil` fora do contrato | É aceito como extensão opcional e retrocompatível, presente só quando verdadeiro. O contrato diz que nada além dos campos listados é necessário, e um campo opcional a mais não quebra a leitura. O campo é necessário para cumprir CLAUDE.md ("VOLÁTIL: inapto a simulado final") na plataforma. Não muda gabarito, escopo, gênero nem rótulo, então não é D2. Será formalizado no contrato. | PRÓXIMO (T-26) |
| Itens do banco à espera de QA normativo (T-13: 16 de LGPD exportados; T-21: BQ-0036 e BQ-0040) | Ficam em `itens`. Passaram pelo QA de 09/10, não têm QA PENDENTE e o gabarito é o definitivo do certame. Se a T-13 ou a T-21 der gatilho D, o pacote é regerado. | PRÓXIMO (T-13, T-21 existentes) |
| Registro AUTORAL v2 sem os Lotes 6a e 6b | O registro diz que eles "entram na v3, após o gatilho A da GCB". Os dois já são canônicos (D-LOTE6A/6B-CANONICO), mas a produtora teve de conferir o 6a e o 6b direto nos arquivos de lote. Emitir o registro v3 com 180 itens (89 C / 91 E) antes da regeração, para que a conferência da T-27 cubra os 180 contra uma só fonte. | PRÓXIMO (T-30) |
| Fonte "saida/lote*/RECONCILIADO.md" inexistente | O prompt EXPORTAR cita arquivos que não existem. A produtora usou a tabela de arquivos canônicos (relatório, seção 1), conferida aqui. O contrato passa a citar essa tabela. | PRÓXIMO (T-26) |

## 3. Veredito da T-05

**T-05: CONCLUÍDA.** O pacote v1 foi gerado e conferido pela Gerência, com todas as contagens iguais às fontes canônicas: 240 itens, 0 duplicatas, 180/180 AUTORAL e 60/60 banco. **Ainda não é liberável à plataforma.**
- Bloqueios e as tarefas que os resolvem:
  - OB-6b-1 no curso do L6B: T-17 (GCB).
  - SIM-0 sem a T-25 e sem a T-13: T-25 e T-13; até lá, o SIM-0 sai do pacote liberável.
  - L3-Q21 sem a marca e D4/D5 sem R2–R4: T-27.
- A regeração (T-27, execução da T-12 por D-PACOTE-6) produz o pacote candidato a aceite. Depois dela, a GBQ confere por script e emite o gatilho A.
- **Gatilho A: não emitido**, porque o pacote está bloqueado.
- Nenhum outro gatilho (B a E) se configura: não há matéria fora do domínio, conflito acima de D1, decisão D2 nem matéria do Fundador pendente agora. A liberação à plataforma e o que vai à candidata seguem reservados ao Fundador e serão perguntados no gatilho A do pacote regerado.
- O orquestrador marca a T-05 como CONCLUÍDA no seu controle de estados. A GBQ não reescreve linhas de TAREFAS.md.

## 4. Tarefas novas (append único a TAREFAS.md)
- T-26 (PRÓXIMO): errata de forma do contrato `regras/pacote_contrato.md` para a v1.1.
- T-27 (PRÓXIMO, condicionada): regeração do pacote.json, v1.1, pela T-12.
- T-28 (PRÓXIMO): errata de forma da GCE, D-DEREP, no curso do L2.
- T-29 (PRÓXIMO): colunas texto_comando e texto_base no banco.
- T-30 (PRÓXIMO): Registro AUTORAL v3 com os Lotes 6a e 6b.

## 5. Gatilhos
Nenhum.
