# simulado_1_QA_2026-10-10.md — T-34 — 2026-10-10 — gerado por gbq-cqe

# QA independente do Simulado 1 (P1 final, TI e Dados itens 5–8) como objeto

Agente: gbq-cqe (QA, opus). Não produziu, não montou e não reconciliou o Simulado 1 (T-06 e T-31 foram gbq-csc → gbq-gerencia). Condição exigida por D-SIM1-DEVOLVIDO (presidencia, 10/10/2026). Somente leitura: nenhum item, ordem, numeração, comando, texto ou gabarito foi alterado; divergências registradas, sem correção.

## Objeto e bases

- Objeto: `saida/simulados/simulado_1.md` (folha) e `saida/simulados/simulado_1_gabarito.md` (grade, mapa, justificativas, verificação).
- Bases canônicas (D-CANONICOS), seções (d) e (d-G): `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` (cabeçalho v3.3), `saida/gcb/GCB_Lote4C_v1_GCB-CPP.md` (v1.1 com 6-A), `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` (v3.1), `saida/gcb/GCB_Lote5C_v1_GCB-CPP.md` (v1.1).
- Registro: `saida/gbq/claude_GBQ_Registro_AUTORAL_v2.md` (gabarito, subitem, TS e marca dos 60 ids L4/4C/A5/5C).
- Edital: `edital/TI_itens_5_8_P1.md` (nomes dos subitens, transcrição literal).
- Regras localizadas: R1, R1-N, R2 e R4 estão definidas no registro AUTORAL v2, seção "Regras de elegibilidade (GBQ, D1)": R1 = VOLÁTIL inapto a simulado final até 4–8/1/2027; R1-N = REVERIFICAR (normativo), mesmo tratamento do R1; R2 = L4-11 nunca no mesmo simulado que o item real TRF6 2024, Cargo 2, nº 81; R4 = AUTORAL é aderência direta por construção. Não há definição delas em `regras/` (os cinco arquivos de `regras/` não as contêm); a definição usada é a do registro. D-QA-PENDENTE e D-ADERENCIA: DECISOES.md e CLAUDE.md.

## Método

Script próprio, escrito do zero nesta tarefa (não reutiliza t06/verify.py nem scripts da GBQ): `/tmp/claude-0/-home-claude/3cf5e5a2-0a00-52ee-a3d1-ce0f04412748/scratchpad/t34/qa_t34.py` (saída: `result.json` na mesma pasta). Ele lê os arquivos em modo leitura e:
1. extrai, de cada arquivo canônico, o bloco entre "(d) VERSÃO DO ESTUDANTE" e "(d-G) GABARITO COMENTADO" (enunciados e linha de comando de cada item) e o bloco (d-G) até "Nota de produção"/"REGISTRO DE ACATAMENTO"/"FIM" (60 entradas);
2. extrai da folha os 8 blocos "Comando N" e os 40 itens `**n.**`, e do gabarito a grade 8×5 e as 40 linhas do mapa (desescapando `\|` das células Markdown);
3. compara, por item, com igualdade exata de cadeia: enunciado da folha = (d); gabarito da grade = mapa = 1º caractere da entrada d-G = registro; [TS] do mapa = presença de "[TS]" no d-G = coluna TS do registro; justificativa do mapa = entrada d-G sem o identificador inicial; arquivo de origem do mapa = arquivo onde o id foi achado; subitem do mapa = registro e nome do subitem = edital; comando do bloco da folha = linha de comando canônica do próprio item com "julgue os itens [de] X a Y." substituído por "julgue os itens a seguir.";
4. regras: marca VOLÁTIL (d-G ou registro) → R1; marca "REVERIFICAR" → R1-N; id L4-11 ou marca R2 → R2; "PENDENTE" no d-G ou no registro → D-QA-PENDENTE; "a confirmar" no d-G → registro; id fora do registro AUTORAL → D-ADERENCIA/rótulo;
5. folha sem pistas: busca em todas as linhas de `simulado_1.md` por id de lote ou de banco (L*, 4C, 5C, A5, BQ, 6A, 6B), "Lote", VOLÁTIL, REVERIFICAR, PENDENTE, L4-11, TRF6, [TS]/"troca sutil", contagem C/E (número seguido de C/E, "certos/errados", "C/E", %), rótulos (AUTORAL, CEBRASPE_, ANALOGA) e "QA"; e confere que as 40 linhas "Resposta: [   ]" estão vazias;
6. globais: numeração 1–40 contínua na folha, na grade e no mapa; ids únicos; contagens declaradas na seção "Verificação" recalculadas.

Controle negativo: cópia temporária com 1 acento retirado no item 2, 1 gabarito trocado na grade (item 7) e 1 justificativa truncada; o script acusou os três (e nada além das divergências reais). Cópia apagada.

## (1) Literalidade — 40/40

- Enunciado folha = (d) canônico: 40/40.
- Gabarito grade = mapa = d-G = registro AUTORAL v2: 40/40.
- [TS] mapa = d-G = registro: 40/40 (19 sim).
- Justificativa do mapa = entrada integral do d-G sem o identificador: 40/40. Observação (não é divergência): no item 14 (L4-12), a célula traz `p(Y\|X)`, escape exigido pela tabela Markdown; o texto renderizado é idêntico ao d-G `p(Y|X)`.
- Arquivo de origem e subitem do mapa = registro; nome do subitem = edital literal: 40/40.

## (2) Comandos — 37/40

| Comando | itens (ids) | comando da folha | canônico(s) sem a faixa | resultado |
|---|---|---|---|---|
| 1 | 1–8 (4C-02, L4-04, 4C-05, L4-03, 4C-08, 4C-07, L4-01, L4-06) | Acerca da engenharia de prompts, julgue os itens a seguir. | Lote 4 e Lote 4-C: idêntico | ok |
| 2 | 9–12 (L4-08, L4-07, L4-09, L4-10) | A respeito dos tipos de aprendizado de máquina, julgue os itens a seguir. | Lote 4: idêntico | ok |
| 3 | 13–16 (L4-14, L4-12, L4-13, L4-16) | Acerca da IA generativa, julgue os itens a seguir. | Lote 4: idêntico | ok |
| 4 | 17–20 (L4-17, L4-18, L4-20, L4-19) | No que se refere à ética e à responsabilidade digital no serviço público, julgue os itens a seguir. | Lote 4: idêntico | ok |
| 5 | 21–24 (A5-03, A5-02, A5-04, A5-01) | Acerca de dados, atributos, métricas e transformação de dados, julgue os itens a seguir. | Lote 5: idêntico | ok |
| 6 | 25–27 (A5-06, A5-07, A5-05) | A respeito dos princípios de visualização de dados, julgue os itens a seguir. | Lote 5: idêntico | ok |
| 7 | 28–34 (A5-12, 5C-03, 5C-04, 5C-05, A5-11, A5-10, A5-09) | Acerca dos tipos de gráficos, julgue os itens a seguir. | Lote 5 e Lote 5-C: idêntico | ok |
| 8 | 35–40 (5C-10, A5-20, A5-18, A5-19, 5C-09, 5C-07) | No que se refere ao storytelling para visualização de dados, julgue os itens a seguir. | Lote 5 (A5-18 a A5-20): idêntico. Lote 5-C (5C-07, 5C-09, 5C-10): "Acerca do storytelling para visualização de dados, julgue os itens a seguir." | **DIVERGE para 35, 39, 40** |

DIVERGÊNCIA D-1 (registrada, não corrigida): o Comando 8 reúne itens de dois lotes cujos comandos canônicos têm redação diferente ("No que se refere ao…" no Lote 5; "Acerca do…" no Lote 5-C). A folha adotou a do Lote 5. Para os itens 35 (5C-10), 39 (5C-09) e 40 (5C-07), o comando da folha não é o comando canônico do próprio item sem a faixa.
- Leitura A (estrita, adotada neste veredito, por ser a letra de T-34 e de D-SIM1-DEVOLVIDO, que não admite aceite "com ressalva"): o critério (2) é por item; 35, 39 e 40 REPROVADOS no critério (2). Texto, gabarito, [TS] e justificativa desses itens conferem.
- Leitura B (por bloco): cada bloco de comando da folha é, literalmente, um comando canônico sem a faixa (8/8: o Comando 8 = comando do Lote 5); os dois comandos têm o mesmo escopo (8.4, storytelling) e diferem só na fórmula de abertura. Nessa leitura, 40/40 APROVADO.
- Nota para a reconciliação: a leitura A não se satisfaz com uma única redação no Comando 8 (qualquer das duas falha para os itens do outro lote); cumpri-la exige separar o bloco 8 em dois comandos, o que mexe em ordem e numeração. A arbitragem entre A e B é da gbq-gerencia (D1), não deste QA.

## (3) Regras

- R1 (VOLÁTIL): 0/40 com marca VOLÁTIL no d-G ou no registro. Os 5 VOLÁTEIS de P1 5–8 no registro (L4-15, A5-14, A5-15, A5-16, A5-17) estão fora do simulado. Cumprida.
- R1-N (REVERIFICAR normativo): 0/40 com a marca REVERIFICAR (no registro, só L3-Q21, P2, fora do objeto). O item 10 (L4-07) traz no d-G "reverificado em 7/10/2026", registro de verificação passada, não a marca. Cumprida.
- R2: L4-11 ausente; nenhum item real (TRF6 2024, Cargo 2, nº 81, nem outro item de banco) no simulado: os 40 são AUTORAL do registro v2. Cumprida.
- D-QA-PENDENTE: 0/40 com "QA PENDENTE" ou "PENDENTE" no d-G, no registro ou nos arquivos canônicos (busca nos quatro arquivos: nenhuma ocorrência de "QA PENDENTE"). Situação de QA dos lotes de origem: Lote 4 v3 e Lote 5 v3 CONFERIDOS (GCB_Conferencia_v3_Lotes4e5_CQFP.md, 08/10/2026); Lote 4-C v1.1 com 6-A CONFERIDO e Lote 5-C v1.1 CONFERIDO (pareceres R1 da CQFP, conferências de aplicação de 08/10/2026), canônicos por D-CANONICOS. Nenhum d-G selecionado contém "a confirmar". Cumprida.
- D-ADERENCIA: 40/40 AUTORAL do registro v2, aderência direta por construção (R4); os 40 subitens do mapa estão no edital P1 5–8 com o nome literal. Nenhum item real de aderência parcial. Cumprida.
- Observações sem efeito no veredito: (a) L4-17, L4-18 e L4-20 têm marca "normativo" no registro (não é REVERIFICAR); os d-G registram conferência da CQFP no Planalto (07 e 08/10/2026) e os dispositivos citados (LGPD art. 5º, III; art. 7º, I a III; art. 12, caput; LAI arts. 3º, I; 23; 24, § 1º; 31) não estão entre os alterados pela Lei 15.352/2026 segundo D-LEI15352-PROV (art. 5º, VIII e XIX; Capítulo IX; arts. 55-A e 55-C). (b) O Lote 4 em `saida/gcb` está na v3.3; o Despacho 9 (v3.4) altera, entre (d) e (d-G), só o d-G do item 11 (L4-11), fora do simulado: nenhum item selecionado é afetado.

## (4) Folha sem pistas

Busca em todas as linhas de `simulado_1.md`: 0 ocorrência de id de lote ou de banco, "Lote", VOLÁTIL, REVERIFICAR, PENDENTE, L4-11, TRF6, [TS]/"troca sutil", contagem C/E, rótulo de fonte ou "QA". As 40 linhas "Resposta: [   ]" estão vazias; numeração 1–40 contínua. A folha remete o gabarito a arquivo separado e avisa a ausência do 8.3, sem pista de resposta. Cumprida.

## Globais (recalculados)

40 itens; ids únicos; 20 C / 20 E; 19 [TS]; Lote 4 = 16, 4-C = 4, Lote 5 = 14, 5-C = 6; por subitem (itens, C): 5.1 (8, 4), 5.2 (4, 2), 5.3 (4, 2), 6 (4, 2), 7.1 (4, 2), 8.1 (3, 1), 8.2 (7, 4), 8.4 (6, 3); sequência CCEEECCEECECCCEECECEECECEECEECCCECECCECE = a declarada; maior corrida = 3. Tudo confere com a seção "Verificação" do gabarito.

## Veredito por item

| nº | id | enunciado (d) | gab (grade = mapa = d-G = registro) | [TS] (mapa = d-G = registro) | justificativa = d-G | comando = canônico sem faixa | R1 / R1-N / R2 / D-QA-PENDENTE / D-ADERENCIA | veredito |
|---|---|---|---|---|---|---|---|---|
| 1 | 4C-02 | ok | ok | ok | ok | ok | ok | APROVADO |
| 2 | L4-04 | ok | ok | ok | ok | ok | ok | APROVADO |
| 3 | 4C-05 | ok | ok | ok | ok | ok | ok | APROVADO |
| 4 | L4-03 | ok | ok | ok | ok | ok | ok | APROVADO |
| 5 | 4C-08 | ok | ok | ok | ok | ok | ok | APROVADO |
| 6 | 4C-07 | ok | ok | ok | ok | ok | ok | APROVADO |
| 7 | L4-01 | ok | ok | ok | ok | ok | ok | APROVADO |
| 8 | L4-06 | ok | ok | ok | ok | ok | ok | APROVADO |
| 9 | L4-08 | ok | ok | ok | ok | ok | ok | APROVADO |
| 10 | L4-07 | ok | ok | ok | ok | ok | ok | APROVADO |
| 11 | L4-09 | ok | ok | ok | ok | ok | ok | APROVADO |
| 12 | L4-10 | ok | ok | ok | ok | ok | ok | APROVADO |
| 13 | L4-14 | ok | ok | ok | ok | ok | ok | APROVADO |
| 14 | L4-12 | ok | ok | ok | ok | ok | ok | APROVADO |
| 15 | L4-13 | ok | ok | ok | ok | ok | ok | APROVADO |
| 16 | L4-16 | ok | ok | ok | ok | ok | ok | APROVADO |
| 17 | L4-17 | ok | ok | ok | ok | ok | ok | APROVADO |
| 18 | L4-18 | ok | ok | ok | ok | ok | ok | APROVADO |
| 19 | L4-20 | ok | ok | ok | ok | ok | ok | APROVADO |
| 20 | L4-19 | ok | ok | ok | ok | ok | ok | APROVADO |
| 21 | A5-03 | ok | ok | ok | ok | ok | ok | APROVADO |
| 22 | A5-02 | ok | ok | ok | ok | ok | ok | APROVADO |
| 23 | A5-04 | ok | ok | ok | ok | ok | ok | APROVADO |
| 24 | A5-01 | ok | ok | ok | ok | ok | ok | APROVADO |
| 25 | A5-06 | ok | ok | ok | ok | ok | ok | APROVADO |
| 26 | A5-07 | ok | ok | ok | ok | ok | ok | APROVADO |
| 27 | A5-05 | ok | ok | ok | ok | ok | ok | APROVADO |
| 28 | A5-12 | ok | ok | ok | ok | ok | ok | APROVADO |
| 29 | 5C-03 | ok | ok | ok | ok | ok | ok | APROVADO |
| 30 | 5C-04 | ok | ok | ok | ok | ok | ok | APROVADO |
| 31 | 5C-05 | ok | ok | ok | ok | ok | ok | APROVADO |
| 32 | A5-11 | ok | ok | ok | ok | ok | ok | APROVADO |
| 33 | A5-10 | ok | ok | ok | ok | ok | ok | APROVADO |
| 34 | A5-09 | ok | ok | ok | ok | ok | ok | APROVADO |
| 35 | 5C-10 | ok | ok | ok | ok | **DIVERGE** | ok | REPROVADO — critério (2): comando da folha (Comando 8, "No que se refere ao storytelling…") ≠ comando canônico do Lote 5-C sem a faixa ("Acerca do storytelling para visualização de dados, julgue os itens a seguir.") |
| 36 | A5-20 | ok | ok | ok | ok | ok | ok | APROVADO |
| 37 | A5-18 | ok | ok | ok | ok | ok | ok | APROVADO |
| 38 | A5-19 | ok | ok | ok | ok | ok | ok | APROVADO |
| 39 | 5C-09 | ok | ok | ok | ok | **DIVERGE** | ok | REPROVADO — critério (2): comando da folha (Comando 8, "No que se refere ao storytelling…") ≠ comando canônico do Lote 5-C sem a faixa ("Acerca do storytelling para visualização de dados, julgue os itens a seguir.") |
| 40 | 5C-07 | ok | ok | ok | ok | **DIVERGE** | ok | REPROVADO — critério (2): comando da folha (Comando 8, "No que se refere ao storytelling…") ≠ comando canônico do Lote 5-C sem a faixa ("Acerca do storytelling para visualização de dados, julgue os itens a seguir.") |

## Veredito geral

- APROVADOS: 37/40. REPROVADOS: 3/40 (itens 35, 39 e 40; 5C-10, 5C-09, 5C-07), todos pelo critério (2), divergência D-1 do Comando 8. Percentual de reprovados: 7,5%. Critérios (1), (3) e (4): 40/40 sem divergência.
- VEREDITO GERAL: REPROVADO (7,5% de reprovados), na leitura A (estrita). Na leitura B (por bloco), registrada acima, o resultado seria APROVADO/CONFERIDO 40/40. Este QA não arbitra: a gbq-gerencia decide em D1 entre A e B (ou ordena a separação do Comando 8) e, conforme a decisão, reconcilia e reemite o gatilho A.
- Abaixo de 30%: sem gate.
- Classificação: D-1 AGORA (condição do gatilho A do Simulado 1).
