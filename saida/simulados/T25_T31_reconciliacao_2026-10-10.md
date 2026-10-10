# T25_T31_reconciliacao_2026-10-10.md — T-25 e T-31 — 2026-10-10 — gerado por gbq-gerencia

REMETENTE: GBQ — Gerência de Banco de Questões e Simulados
DESTINATÁRIO: orquestrador (estado de T-25 e T-31); Presidência (gatilho A do Simulado 1 em PARA_PRESIDENCIA.md)

Entradas (gbq-csc): `saida/simulados/T25_2026-10-10.md` e `saida/simulados/T31_2026-10-10.md`, com os arquivos `simulado_0_v0.2.md`, `simulado_0_v0.2_gabarito.md`, `simulado_1.md` e `simulado_1_gabarito.md`. Regras: CLAUDE.md (Adendo v2.1), D-SIM0-V02, D-BANCO-TI-1-4, D-ADERENCIA, D-PACOTE-6, D-BACKUP-2; reconciliações anteriores da GBQ (`simulado_1_reconciliacao.md`, `T15_T22_reconciliacao_2026-10-10.md`). Papéis: gbq-gerencia e gce-gerencia.

Conferência por script, somente leitura (scratchpad `t25t31/verify.py`): `git show HEAD:<arquivo>` × árvore de trabalho, `git diff -U0`, CSV com `csv.DictReader(delimiter=';')`. Resultado: 38/38 verificações OK (a contagem de "Resposta: [   ]" da folha do Simulado 1 dá 41 porque a instrução cita o campo uma vez; as linhas próprias de resposta são 40, igual ao HEAD). `banco/` e `edital/` sem diferença em relação ao HEAD. Os arquivos canônicos usados pelo Simulado 1 (`saida/gcb/`, `saida/gbq/`) não mudaram desde a T-06. A GBQ não editou simulado, gabarito, banco nem lote.

## 1. T-31 — folha do Simulado 1

| Verificação | Resultado |
|---|---|
| Linha de base da T-06 reproduzida no HEAD ("## Instruções" até antes de "## Verificação (montagem)") | 9408 caracteres, sha256 `427ad5d06ec47341…` |
| Trecho "## Instruções" → fim do item 40 na folha nova | igual à linha de base após `rstrip` (9407 caracteres; só falta a linha em branco final que precedia a seção retirada) |
| 40 enunciados, numeração 1–40, 8 comandos, 40 linhas de resposta | idênticos ao HEAD |
| Seção "## Verificação (montagem)" | retirada; a folha termina no "Resposta: [   ]" do item 40 |
| Frase de montagem da abertura | retirada |
| Aviso do 8.3 | presente 1 vez, antes de "## Instruções", com o texto fixado na T-31 |
| Pistas na folha: ids (L4-, 4C-, A5-, 5C-, BQ-), [TS], VOLÁTIL, REVERIFICAR, PENDENTE, TRF6, AUTORAL, "Lote", "saida/", "Verificação", contagens "n C"/"n E", "C/E", "%", "Gabarito:" | 0 ocorrência |
| `simulado_1_gabarito.md` | HEAD = linha de base `4c19e45a98fa08db…`; diff = linha 1 + 1 linha nova "Ajuste T-31", dentro de "Regras e falta registrada"; grade, mapa e verificação intactos |

- O hash do trecho mudou em 1 caractere (linha em branco final). O conteúdo é idêntico. **Aceito (D1)**: o critério da T-31 é a identidade do conteúdo do corpo, e a linha em branco pertencia à separação da seção retirada.
- **Veredito T-31: CONCLUÍDA** e reconciliada. A condição 3(d) da reconciliação da T-06 está cumprida.

## 2. T-25 — Simulado 0 v0.2

| Verificação | Resultado |
|---|---|
| Itens (nº, comando, texto) e 34 comandos | idênticos ao HEAD 60/60 |
| Grade do gabarito | idêntica ao HEAD 60/60 |
| Mapa: nº, Cmd, BQ-id, gab | idênticos ao HEAD; linhas alteradas exatamente {15, 17, 18, 26, 27, 31, 51, 57–60} |
| Mapa × banco | subitem 60/60, gabarito 60/60, texto do corpo = `texto_integral` 60/60, `anulado=nao` e sem "QA PENDENTE" 60/60; aderência e VOLÁTIL = observacoes do banco 60/60 |
| Marcas do corpo × mapa | 23 PARCIAIS = 23 marcas `[ADERÊNCIA PARCIAL …]`, com motivo contido na observação do mapa; VOLÁTIL {18, 23, 37, 38} nos dois; 0 marca de arbitragem; legenda DIRETA*/DIRETA† retirada |
| Contagens | 37 DIRETA / 23 PARCIAL (17 P2-4.1, 2 P1-8.3, 1 P1-5.3, 1 P1-6, 1 P1-7.1, 1 P1-8.1) / 0 em arbitragem; 4 VOLÁTEIS; 33 C / 27 E; Parte P1 39 (21 C), Parte P2 21 (12 C); módulo P1 43 (23 C), módulo P2 17 (10 C) |
| Cobertura (41 linhas P1 + P2) | recomputada a partir do mapa e igual à tabela (P1-4: 4 itens, 2 C / 2 E, 4 DIRETOS; P1-5: 1 C DIRETO; P1-5.3: 10, 6 C / 4 E, 9 D / 1 P, 2 VOLÁTEIS; P2-4.3 SEM ITEM) |
| Diff do corpo | só linha 1, introdução, avisos 1–4, linha de total das instruções, marcas dos itens 15, 18, 26, 31, 51 e 57–60 e a nota antes do Comando 33 |

- Item 51: motivo "Marco Civil da Internet, Lei 12.965/2014, não LGPD"; referência T-21 no mapa. Conforme a T-25.
- A redação "Caput sem linha própria…" da cobertura é nota explicativa coerente com as linhas P1-1 a P1-5. **Aceita (D1)**, sem ajuste.
- **Veredito T-25: CONCLUÍDA** e reconciliada. O Simulado 0 v0.2 está alinhado ao banco, que é a fonte. A condição (4) da T-27 sobre a T-25 está cumprida.

## 3. Decisões D1

1. **D-SIM0-V02 — nenhuma matéria nova.** A parte "aplicar T-15 e regerar o gabarito" já estava cumprida (T15_T22_reconciliacao, seção 2), e a T-25 regerou o gabarito outra vez. Os números aceitos pela Presidência (60 itens; Parte P1 39, Parte P2 21; 33 C / 27 E) não mudaram. A contagem por módulo deriva de D-BANCO-TI-1-4 (D1 anterior). Falta só a T-13 sem gatilho D, e a entrega segue reservada ao Fundador. Sem gatilho.
2. **Escopo da T-13 conferido.** Os 16 itens LGPD do Simulado 0 v0.2 (P2-4.1, exceto BQ-0036) estão todos na T-13. A T-13 inclui também BQ-0031, que é anulado e está fora do simulado; isso não tem efeito.
3. **Itens 27 (BQ-0040) e 51 (BQ-0036) e a T-21.** D-SIM0-V02 condiciona o uso só à T-13. Esses dois itens do simulado têm a atualidade do gabarito sob a T-21. No domínio da GBQ (pacote), a GBQ só confere a inclusão do Simulado 0 v0.2 em "simulados" na T-27 com a T-21 também CONCLUÍDA sem gatilho D. É o mesmo critério da T-13, aplicado na conferência por script da gbq-gerencia antes do gatilho A do pacote. A linha da T-27 não é reescrita. Não amplia a condição de uso fixada pela Presidência, por isso não há gatilho. Classe: PRÓXIMO (sem tarefa nova; T-21 já na fila).
4. **Simulado 1 no pacote.** Depois do aceite, a inclusão segue a T-12 (recorrente "a cada gatilho A novo") e o contrato v1.1 (T-26, ponto 5). Não há tarefa nova. O gatilho não pede liberação à plataforma.

## 4. Tarefas novas
Nenhuma.

## 5. Gatilhos
Simulado 1 pronto para aceite como simulado final (condição da T-06: T-31 reconciliada). Emitido em PARA_PRESIDENCIA.md:

`GATILHO A | GBQ | Simulado 1 (P1 — final, TI e Dados itens 5–8), T-06 e T-31 reconciliadas, pronto para aceite como simulado final | saida/simulados/simulado_1.md; saida/simulados/simulado_1_gabarito.md; saida/simulados/simulado_1_reconciliacao.md; saida/simulados/T25_T31_reconciliacao_2026-10-10.md | 40 itens AUTORAL canônicos (L4 16, 4-C 4, L5 14, 5-C 6); 20 C/20 E; 19 [TS]; 0 VOLÁTIL, 0 QA PENDENTE, 0 PARCIAL; cobertura 8 de 9 subitens de P1 5–8 (8.3 sem item: falta registrada, avisada na folha, T-33); folha sem contagem C/E nem ids (script 38/38 OK) | A Presidência aceita o Simulado 1 como simulado final de P1 (TI e Dados, itens 5–8), com a falta do 8.3 registrada? (SIM/NÃO; a entrega à candidata segue reservada ao Fundador)`

Simulado 0 v0.2: nenhum gatilho (ver 3.1).
