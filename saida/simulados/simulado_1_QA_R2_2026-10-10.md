# simulado_1_QA_R2_2026-10-10.md — T-34 R2 — 2026-10-10 — gerado por gbq-cqe

# QA independente do Simulado 1 — rodada 2 (final)

Agente: gbq-cqe (QA, opus). Não produziu, não montou, não reconciliou e não corrigiu o Simulado 1. Somente leitura: nenhum arquivo além deste foi editado e o git foi usado só para ler (`git diff`, `git show`, `git status`).

## Entradas

- Rodada 1: `saida/simulados/simulado_1_QA_2026-10-10.md` — REPROVADO, 3/40 (7,5%), itens 35 (5C-10), 39 (5C-09) e 40 (5C-07), critério (2), divergência D-1 do Comando 8.
- Arbitragem: `saida/simulados/T34_reconciliacao_2026-10-10.md` (gbq-gerencia, D1) — adotada a leitura A (por item); correção mecânica T-35.
- Correção: `saida/simulados/T35_2026-10-10.md` (gbq-csc). O Comando 8 foi dividido: Comando 8 com 35–37 = A5-20, A5-18, A5-19; novo Comando 9, "Acerca do storytelling para visualização de dados, julgue os itens a seguir.", com 38–40 = 5C-10, 5C-09, 5C-07. Gabarito, mapa e sequência acompanham a mudança.
- Objeto atual: `saida/simulados/simulado_1.md` e `saida/simulados/simulado_1_gabarito.md`. Bases sem alteração: os quatro arquivos canônicos (`saida/gcb/…`), o registro AUTORAL v2 e `edital/TI_itens_5_8_P1.md` não têm modificação no `git status`.

## Método

- Mesmo script próprio da rodada 1, sem mudança de método: `/tmp/claude-0/-home-claude/3cf5e5a2-0a00-52ee-a3d1-ce0f04412748/scratchpad/t34/qa_t34.py`.
  - Ele já lia qualquer número de blocos "### Comando N"; não foi preciso ajustá-lo para 9 blocos.
  - Saídas: `result_R1.json` (rodada 1) e `result_R2.json` (esta rodada), na mesma pasta.
- Controle de identidade do objeto: o script rodou sobre as versões de HEAD dos dois arquivos (`git show HEAD:…`, cópia temporária já apagada). O resultado é idêntico ao `result_R1.json`, com as mesmas 3 falhas. Portanto o objeto anterior à T-35 é o que a rodada 1 conferiu, e o diff abaixo é a mudança completa.
- O relatório da T-35 diz que a gbq-csc reutilizou "o script de QA da T-34" (base_qa.py). Esta rodada não usa nada daquele arquivo: a conferência abaixo vem só de `qa_t34.py`, que está no scratchpad desta tarefa.

## Diff conferido (git diff HEAD, somente leitura)

`simulado_1.md` (+9 −5 linhas):
- Linha 1 (cabeçalho): acréscimo de "T-35".
- Itens 35–37: passam a ser os textos que antes eram 36, 37 e 38 (A5-20, A5-18, A5-19) e continuam sob o Comando 8, cuja linha de comando não mudou.
- Novo bloco "### Comando 9" / "> Acerca do storytelling para visualização de dados, julgue os itens a seguir." antes do item 38.
- Item 38: passa a ser o texto que antes era 35 (5C-10). Os itens 39 e 40 não mudaram.
- Nenhuma outra linha mudou. Os itens 1–34 e os Comandos 1–7 estão intactos.

`simulado_1_gabarito.md` (+9 −8 linhas):
- Linha 1 (cabeçalho).
- Grade: célula 35 E→C e célula 37 C→E. As células 36 (C) e 38 (E) já coincidiam com o novo item.
- Mapa: linhas 35–38 = A5-20, A5-18, A5-19, 5C-10. Só a coluna nº mudou; as demais colunas são idênticas às linhas anteriores.
- Sequência: nova sequência e nota "itens 35–38 reordenados na T-35".
- Uma linha "Ajuste T-35" acrescentada ao fim de "Regras e falta registrada", antes de "Ressalva de arquivo".
- Nada mais mudou. Não restou ocorrência da sequência antiga no arquivo.

O diff corresponde exatamente à especificação da seção 2 de `T34_reconciliacao_2026-10-10.md`. Não houve alteração de texto, gabarito por item, [TS], justificativa ou seleção.

## (1) Literalidade — 40/40

- Enunciado da folha = (d) canônico: 40/40.
- Gabarito: grade = mapa = d-G = registro, 40/40.
- [TS]: mapa = d-G = registro, 40/40 (19 sim).
- Justificativa do mapa = entrada integral do d-G sem o identificador: 40/40.
- Arquivo de origem, subitem e nome do subitem (= edital): 40/40.
- Observação mantida da rodada 1, sem efeito: no item 14 (L4-12), `\|` é escape da tabela Markdown.

## (2) Comandos canônicos por item — 40/40

| Comando | itens (ids) | comando da folha | resultado |
|---|---|---|---|
| 1 | 1–8 (4C-02, L4-04, 4C-05, L4-03, 4C-08, 4C-07, L4-01, L4-06) | Acerca da engenharia de prompts, julgue os itens a seguir. | ok (Lote 4 e 4-C) |
| 2 | 9–12 (L4-08, L4-07, L4-09, L4-10) | A respeito dos tipos de aprendizado de máquina, julgue os itens a seguir. | ok |
| 3 | 13–16 (L4-14, L4-12, L4-13, L4-16) | Acerca da IA generativa, julgue os itens a seguir. | ok |
| 4 | 17–20 (L4-17, L4-18, L4-20, L4-19) | No que se refere à ética e à responsabilidade digital no serviço público, julgue os itens a seguir. | ok |
| 5 | 21–24 (A5-03, A5-02, A5-04, A5-01) | Acerca de dados, atributos, métricas e transformação de dados, julgue os itens a seguir. | ok |
| 6 | 25–27 (A5-06, A5-07, A5-05) | A respeito dos princípios de visualização de dados, julgue os itens a seguir. | ok |
| 7 | 28–34 (A5-12, 5C-03, 5C-04, 5C-05, A5-11, A5-10, A5-09) | Acerca dos tipos de gráficos, julgue os itens a seguir. | ok (Lote 5 e 5-C) |
| 8 | 35–37 (A5-20, A5-18, A5-19) | No que se refere ao storytelling para visualização de dados, julgue os itens a seguir. | ok (Lote 5) |
| 9 | 38–40 (5C-10, 5C-09, 5C-07) | Acerca do storytelling para visualização de dados, julgue os itens a seguir. | ok (Lote 5-C) |

A leitura por item e a leitura por bloco coincidem nos 9 blocos. A divergência D-1 está SANADA.

## (3) Regras — 40/40

- R1: nenhum item VOLÁTIL. Os VOLÁTEIS L4-15 e A5-14 a A5-17 continuam fora.
- R1-N: nenhum item com a marca REVERIFICAR.
- R2: L4-11 ausente; nenhum item real (TRF6) no simulado.
- D-QA-PENDENTE: nenhum "PENDENTE" ou "a confirmar" nos d-G selecionados ou no registro. Os quatro lotes de origem estão CONFERIDOS pela CQFP e são canônicos (D-CANONICOS).
- D-ADERENCIA: 40 AUTORAL, todos com aderência direta por construção (R4). Subitens de P1 5–8 conforme o edital.
- As definições das regras R1, R1-N, R2 e R4 estão no registro AUTORAL v2, não em `regras/` (como registrado na rodada 1).

## (4) Folha sem pistas — cumprida

Nenhuma ocorrência de: id de lote ou de banco, "Lote", VOLÁTIL, REVERIFICAR, PENDENTE, L4-11, TRF6, [TS] ou "troca sutil", contagem C/E, rótulo de fonte ou "QA". As 40 linhas "Resposta: [   ]" estão vazias. O novo bloco não acrescentou nota, id ou contagem; a folha termina no "Resposta: [   ]" do item 40.

## Globais (recalculados)

- 40 itens, numeração 1–40 contínua na folha, na grade e no mapa; ids únicos.
- 20 C / 20 E; 19 [TS].
- Por lote: 4 = 16, 4-C = 4, 5 = 14, 5-C = 6.
- Por subitem (itens, C): 5.1 (8, 4) · 5.2 (4, 2) · 5.3 (4, 2) · 6 (4, 2) · 7.1 (4, 2) · 8.1 (3, 1) · 8.2 (7, 4) · 8.4 (6, 3).
- Sequência CCEEECCEECECCCEECECEECECEECEECCCECCCEECE = a declarada no gabarito; maior corrida = 3.
- Tudo confere com a seção "Verificação" do gabarito, que não precisou mudar.

## Veredito por item

| nº | id | comando | enunciado (d) | gab (grade = mapa = d-G = registro) | [TS] | justificativa = d-G | comando = canônico do item sem faixa | R1 / R1-N / R2 / D-QA-PENDENTE / D-ADERENCIA | veredito |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 4C-02 | 1 | ok | ok | ok | ok | ok | ok | APROVADO |
| 2 | L4-04 | 1 | ok | ok | ok | ok | ok | ok | APROVADO |
| 3 | 4C-05 | 1 | ok | ok | ok | ok | ok | ok | APROVADO |
| 4 | L4-03 | 1 | ok | ok | ok | ok | ok | ok | APROVADO |
| 5 | 4C-08 | 1 | ok | ok | ok | ok | ok | ok | APROVADO |
| 6 | 4C-07 | 1 | ok | ok | ok | ok | ok | ok | APROVADO |
| 7 | L4-01 | 1 | ok | ok | ok | ok | ok | ok | APROVADO |
| 8 | L4-06 | 1 | ok | ok | ok | ok | ok | ok | APROVADO |
| 9 | L4-08 | 2 | ok | ok | ok | ok | ok | ok | APROVADO |
| 10 | L4-07 | 2 | ok | ok | ok | ok | ok | ok | APROVADO |
| 11 | L4-09 | 2 | ok | ok | ok | ok | ok | ok | APROVADO |
| 12 | L4-10 | 2 | ok | ok | ok | ok | ok | ok | APROVADO |
| 13 | L4-14 | 3 | ok | ok | ok | ok | ok | ok | APROVADO |
| 14 | L4-12 | 3 | ok | ok | ok | ok | ok | ok | APROVADO |
| 15 | L4-13 | 3 | ok | ok | ok | ok | ok | ok | APROVADO |
| 16 | L4-16 | 3 | ok | ok | ok | ok | ok | ok | APROVADO |
| 17 | L4-17 | 4 | ok | ok | ok | ok | ok | ok | APROVADO |
| 18 | L4-18 | 4 | ok | ok | ok | ok | ok | ok | APROVADO |
| 19 | L4-20 | 4 | ok | ok | ok | ok | ok | ok | APROVADO |
| 20 | L4-19 | 4 | ok | ok | ok | ok | ok | ok | APROVADO |
| 21 | A5-03 | 5 | ok | ok | ok | ok | ok | ok | APROVADO |
| 22 | A5-02 | 5 | ok | ok | ok | ok | ok | ok | APROVADO |
| 23 | A5-04 | 5 | ok | ok | ok | ok | ok | ok | APROVADO |
| 24 | A5-01 | 5 | ok | ok | ok | ok | ok | ok | APROVADO |
| 25 | A5-06 | 6 | ok | ok | ok | ok | ok | ok | APROVADO |
| 26 | A5-07 | 6 | ok | ok | ok | ok | ok | ok | APROVADO |
| 27 | A5-05 | 6 | ok | ok | ok | ok | ok | ok | APROVADO |
| 28 | A5-12 | 7 | ok | ok | ok | ok | ok | ok | APROVADO |
| 29 | 5C-03 | 7 | ok | ok | ok | ok | ok | ok | APROVADO |
| 30 | 5C-04 | 7 | ok | ok | ok | ok | ok | ok | APROVADO |
| 31 | 5C-05 | 7 | ok | ok | ok | ok | ok | ok | APROVADO |
| 32 | A5-11 | 7 | ok | ok | ok | ok | ok | ok | APROVADO |
| 33 | A5-10 | 7 | ok | ok | ok | ok | ok | ok | APROVADO |
| 34 | A5-09 | 7 | ok | ok | ok | ok | ok | ok | APROVADO |
| 35 | A5-20 | 8 | ok | ok | ok | ok | ok | ok | APROVADO |
| 36 | A5-18 | 8 | ok | ok | ok | ok | ok | ok | APROVADO |
| 37 | A5-19 | 8 | ok | ok | ok | ok | ok | ok | APROVADO |
| 38 | 5C-10 | 9 | ok | ok | ok | ok | ok | ok | APROVADO |
| 39 | 5C-09 | 9 | ok | ok | ok | ok | ok | ok | APROVADO |
| 40 | 5C-07 | 9 | ok | ok | ok | ok | ok | ok | APROVADO |

## Veredito geral

- APROVADOS: 40/40. REPROVADOS: 0/40 (0%). Critérios (1), (2), (3) e (4): 40/40.
- Divergência D-1 da rodada 1 (Comando 8): SANADA pela T-35, conforme a D1 da gbq-gerencia (leitura A).
- VEREDITO GERAL: APROVADO/CONFERIDO. Está cumprida a condição de D-SIM1-DEVOLVIDO: QA independente concluído, APROVADO/CONFERIDO, sobre o simulado como objeto.
- Encaminhamento: gbq-cqe → gbq-gerencia, para reconciliar e reemitir o gatilho A. Falta do 8.3 (aviso na folha) e T-33 mantidas. A entrega à candidata (PILOT_01) continua reservada ao Fundador.
- Classificação: AGORA (condição do gatilho A).
