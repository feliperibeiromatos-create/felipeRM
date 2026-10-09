# simulado_0_v0.2_reconciliacao.md — R-04 — 2026-10-09 — gerado por gbq-gerencia

- Entrada: saida/simulados/simulado_0_v0.2.md e saida/simulados/simulado_0_v0.2_gabarito.md (gbq-csc, R-04).
- Conferido contra: banco/banco.csv (66 linhas, leitura CSV com aspas, separador ";"), saida/banco/R03_reconciliacao_2026-10-09.md, saida/banco/qualidade_2026-10-09.md, DECISOES.md, CLAUDE.md, .claude/agents/gbq-gerencia.md (c).
- Regras aplicadas: D-QA-PENDENTE, D-ADERENCIA, D-ROTULOS, D-ANO, D-RECUPERACAO, regra (c) da GBQ, pontuação +1/−1/0 (edital 8.11.2).
- Nenhum arquivo do simulado ou do banco foi editado nesta reconciliação.

## Verificação das regras de montagem (item c da GBQ)
Conferência automatizada dos 60 itens do mapa contra o banco: id, rótulo, subitem, gabarito (mapa e tabela), texto_integral (corpo do simulado, espaços normalizados), anulado, "QA PENDENTE" e VOLÁTIL. Resultado: 0 divergências.

| regra | resultado | evidência |
|---|---|---|
| Sem "QA PENDENTE" | CUMPRIDA | 0 de 60 itens com o prefixo; 0 de 66 linhas do banco com o prefixo. |
| Anulados fora | CUMPRIDA | BQ-0029, 0030, 0031, 0060, 0062, 0063 ausentes. Os 60 itens com gabarito válido do banco estão todos no simulado (nenhum aprovado ficou de fora). |
| Só banco (sem AUTORAL) | CONFIRMADA | 60 de 60 são BQ-*, todos CEBRASPE_ANALOGA. Nenhum id A<lote>-NN ou <lote>-NN no corpo. |
| L4-11 × TRF6 item 81 | CUMPRIDA | BQ-0010 (TRF6 it. 81) é o item 16. L4-11 não aparece no corpo do simulado (0 ocorrências). As 3 menções a L4-11 no gabarito citam só a regra. |
| VOLÁTIL | CUMPRIDA para diagnóstico | Item 23 (BQ-0064) está sinalizado no corpo e no mapa. Simulado diagnóstico; a regra "nunca VOLÁTIL" vale para simulado final. Ver decisão (ii): passam a 4 itens após a T-15. |
| Aderência parcial | CUMPRIDA (D-ADERENCIA) | 24 PARCIAIS marcados no corpo e no mapa. 30 DIRETA, 4 DIRETA* e 2 DIRETA†. Se a T-03 rebaixar algum DIRETA* a PARCIAL, o diagnóstico não muda. |
| Equilíbrio C/E | ACEITO com aviso (D1) | 33 C e 27 E, ou seja 55,0% C. P1: 21 C e 18 E. P2: 12 C e 9 E. É a proporção do banco válido inteiro. Retirar itens aprovados para equilibrar reduziria a cobertura. O aviso 4 do simulado basta. |
| Cobertura do edital | REGISTRADA como limitação | P1: 8 de 9 subitens, todos com item DIRETO; falta 8.4. P2: 2 de 23 subitens (4.1 e 4.3), os dois só PARCIAIS. Para P2, o v0.2 não diagnostica RF/transcrição (1.1–3.4) nem 4.2. Isso cabe ao Simulado 2 (T-10, AUTORAL). |
| Pontuação +1/−1/0 | CONFERIDA | Instruções e gabarito citam o edital 8.11.2, além de 8.2, 8.3 e 8.11.3. |
| Formato | CONFERIDO | 60 itens (P1 39, P2 21), numeração contínua, 34 comandos literais, gabarito em arquivo separado, mapa item → BQ-id → fonte → subitem, D-ANO no mapa. |

## Decisões D1
| ponto | decisão | motivo |
|---|---|---|
| (i) BQ-0025 (item 49) | MANTIDO. O CORRIGIR do QA de 09/10 fica reconciliado como APROVADO, sem nova passagem pela gbq-cqe. Vale para este e para os próximos simulados (como PARCIAL, só diagnóstico). | O QA marcou CORRIGIR só no campo observacoes e conferiu no CDN o texto literal, o gabarito E (definitivo) e a proveniência. A correção foi determinada pela Presidência com texto literal (D-RECUPERACAO c). Conferi que observacoes agora traz "gabarito preliminar C alterado para E no definitivo". Conferir a aplicação de uma correção mecânica é reconciliação, não revisão de conteúdo. Uma nova passagem da gbq-cqe revisaria o que ela mesma já verificou. A pendência normativa segue na T-13, como nos demais itens LGPD. |
| (i-a) Errata interna do gabarito | A seção "Item mantido sob condição" diz "retirar o item 56 (BQ-0025)". O correto é item 49. Vai para a T-15 (mecânico). | O item 56 é BQ-0057. É uma referência interna do gabarito, sem efeito em item ou gabarito. |
| (ii) BQ-0014 (item 17, temperature) | NÃO VOLÁTIL | O item cobra um conceito genérico de amostragem em LLM e não nomeia produto. Nenhuma mudança de produto inverte o gabarito C. Mesmo critério da R-03. |
| (ii) BQ-0015 (item 18, "thread") | VOLÁTIL (dependência de produto) | O gabarito E depende do modelo de objetos de uma API de assistentes de fornecedor (o "thread" × a entidade configurável com modelo, instruções e ferramentas), que o item nem nomeia. O QA de 09/10 registrou que nada disso foi verificado em fonte do fornecedor. Um vocabulário de API pode mudar e inverter a leitura. A arbitragem de aderência segue na T-03, sem efeito sobre esta marca. |
| (ii) BQ-0017 (item 37, Grafana) e BQ-0035 (item 38, Kibana: mapas, Lens, Canvas) | VOLÁTIL (dependência de produto) | São afirmações positivas sobre capacidades e recursos nomeados de produtos comerciais, sem verificação em fonte do fornecedor. É o mesmo critério que marcou BQ-0064 na R-03. Os dois já são PARCIAIS, então a marca não muda a elegibilidade atual; ela os leva à reverificação de janeiro. |
| (ii) BQ-0048 (item 39, Tableau/Power BI) | NÃO VOLÁTIL (mantida a D1 da R-03) | O gabarito E se apoia numa negativa absoluta que é falsa pela definição da categoria BI. Nenhuma mudança de versão a inverte. |
| (ii) Aplicação | As marcas no banco (observacoes, no formato de BQ-0064) e no simulado (corpo, mapa, aviso 5 e coluna de cobertura) vão para a T-15. A reverificação de janeiro dos 3 itens vai para a T-16 (complementa a T-14, que não foi alterada). | A GBQ não edita o banco nem o simulado neste ciclo. Escritas paralelas: só appends. |
| Simulado pronto? | PRONTO como diagnóstico, com ajuste mecânico T-15 antes de qualquer uso | O ajuste só acrescenta marcas e corrige uma referência interna. Não muda item, ordem, numeração, comando nem gabarito. Nenhum item sai. |
| Entrega à candidata | Fora do nível D1 (matéria do Fundador: o que é compartilhado com a PILOT_01 e quando). Recomendação da GBQ: só depois da T-15 aplicada e da T-13 concluída sem gatilho D. | 16 itens LGPD (itens 40–50 e 52–56, ou seja BQ-0002 a 0008, 0023, 0024, 0025, 0032, 0037, 0045, 0046, 0056 e 0057) reproduzem provas anteriores à Lei 15.352/2026. BQ-0036 (item 51, Marco Civil) segue na T-03. |

## Contagens finais (após a T-15, que não altera itens nem gabarito)
- Itens: 60 (P1 39: itens 1–39; P2 21: itens 40–60), em 34 comandos. Todos BQ-*, CEBRASPE_ANALOGA, anulado=nao.
- Gabarito: 33 C e 27 E (55,0% C). P1: 21 C e 18 E. P2: 12 C e 9 E.
- Aderência: DIRETA 30; DIRETA* 4 em arbitragem T-03 (BQ-0001, 0009, 0015, 0016); DIRETA† 2, com mapeamento em arbitragem T-03 (BQ-0014, 0040); PARCIAL 24.
- VOLÁTIL: hoje 1 (BQ-0064, item 23); após a T-15, 4 (mais BQ-0015, item 18; BQ-0017, item 37; BQ-0035, item 38). Cobertura: P1-5.3 com 2 VOLÁTEIS, P1-8.3 com 2.
- Excluídos: 6 anulados. Itens aprovados fora: 0.
- Pendências que afetam itens do simulado, sem bloquear o diagnóstico: T-03 (6 itens), T-13 (16 itens), T-14 e T-16 (4 VOLÁTEIS, janeiro).

## Tarefas novas (append em TAREFAS.md)
- T-15 (AGORA): ajuste mecânico pós-R-04 nas marcas VOLÁTIL do banco e do Simulado 0 v0.2, mais a errata interna "item 56" → "item 49". É AGORA, e não PRÓXIMO, porque o gatilho A depende dela.
- T-16 (PRÓXIMO, datado): reverificação de janeiro de BQ-0015, 0017 e 0035.

## Estado da R-04
CONCLUÍDA e reconciliada em 2026-10-09. O Simulado 0 v0.2 está apto como diagnóstico, condicionado ao ajuste mecânico T-15, que não muda conteúdo.
Gatilho A emitido em PARA_PRESIDENCIA.md: aceite do Simulado 0 v0.2 como diagnóstico. A entrega à PILOT_01 depende de decisão do Fundador.
Outros gatilhos (B a E): nenhum. As decisões (i) e (ii) são D1 do domínio da GBQ: nenhuma muda gabarito, rótulo ou escopo, e não há conflito.
