# T47_reconciliacao_2026-10-13.md — T-47 — 2026-10-13 — gerado por gcb-gerencia

Objeto: reconciliação da T-47, errata de forma D-ERRATA-L5-TUKEY (Fundador, 13/10/2026) no curso do Lote 5. A cadeia foi gcb-cpp → gcb-cqfp → gcb-gerencia.
Entradas:
- produção: saida/gcb/lote5_errata_tukey_2026-10-13.md (gcb-cpp, commit 82bea20; versão anterior 91c82af);
- QA: saida/gcb/QA_T47_2026-10-13_gcb-cqfp.md (APROVADO COM RESSALVAS, 0/20 itens reprovados);
- objeto: saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md.

## 1. Veredito
**T-47 CONCLUÍDA e reconciliada** (D1 GCB). A frase do Fundador está aplicada literalmente ao fim da linha "Bigodes e outliers" (curso 8.2, bloco do box plot). Itens, gabaritos, [TS], VOLÁTIL, resumo (b) e pares não mudaram. A GCB aplicou só erratas de registro (R4 e o rótulo de versão v3.2; seção 3). Nada volta à gcb-cpp. O espelho fica pronto para a T-48, que exporta o curso do Lote 5 com a errata.

## 2. Decisão sobre as ressalvas da CQFP
| Ressalva | Classe proposta pela CQFP | Decisão da GCB (D1) | Motivo |
|---|---|---|---|
| R1. O parêntese "regra usual de Tukey… pode variar" é redundante com a frase do Fundador | BACKLOG | **DESCARTADO** | Não há erro nem contradição. A frase nova traz um elemento próprio: a prova cobra esta regra. Enxugar o parêntese mexeria no texto de curso além do que o Fundador decidiu. A Gerência não produz texto de curso. Além disso, o ajuste abriria nova rodada gcb-cpp → gcb-cqfp no caminho crítico da T-48, só por ganho de estilo. Um BACKLOG sem condição de reativação ficaria sem dono, por isso não foi mantido. |
| R2. A forma "fator 1,5·AIQ" seria mais rigorosa como "fator 1,5" | DESCARTADO | **DESCARTADO** (de acordo com a CQFP) | O texto é literal do Fundador e o contexto da mesma linha tira a ambiguidade. |
| R3. Na contagem de marcas por grep, a linha de registro conta como falso positivo | PRÓXIMO | **PRÓXIMO, como orientação de método para a T-48, sem tarefa nova** | O arquivo não precisa mudar. Na T-48 e nas conferências futuras do Lote 5, [TS] e VOLÁTIL se contam só na Parte 3 (itens e d-G), ou no arquivo inteiro excluindo o cabeçalho e a Tabela de Correções. A linha de base está na seção 4. O orquestrador deve repassar esta orientação ao prompt da T-48 (gbq-csc e gcb-cqfp). |
| R4. O status da linha de registro ainda dizia "conferência CQFP pendente" | AGORA | **AGORA — aplicada pela GCB** | É errata de registro e já tem o parecer de QA. Segue o mesmo rito do ajuste NOTA 8.11.2, que foi aplicado mediante registro e sem nova conferência. |
| Observação de evidência: "a prova costuma cobrar esta" não tem fonte datada | sem classe | **Registrada; vedado converter a frase em item ou em justificativa de gabarito** | A frase é literal do Fundador e não afirma nada sobre ferramenta ou norma. Hoje o único lastro interno é o BQ-0053 (CEBRASPE_ANALOGA, Embrapa 2024). |

## 3. Erratas aplicadas pela GCB (somente em saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md)
1. **R4, Tabela de Correções** (linha 27, que era a 26):
   - antes: "| aplicada (13/10/2026); conferência CQFP pendente |"
   - depois: "| aplicada (v3.2, 13/10/2026); conferida (CQFP, 13/10/2026) |"
2. **Rótulo de versão no cabeçalho** (linha 8 nova, depois da "v3.1 — …"), seguindo o padrão das linhas anteriores do cabeçalho e da v3.4 do Lote 4:
   - "v3.2 — errata de forma T-47 (D-ERRATA-L5-TUKEY, Fundador, 13/10/2026) no curso 8.2, bloco do box plot; conferida pela CQFP em 13/10/2026; registro na Tabela de Correções"
   - Motivo: dar à Secretaria e à T-48 um nome de versão. D-CANONICOS e o Estado Canônico nomeiam a v3.1.
   - A linha não contém "[TS]", "VOLÁTIL" nem a frase do Fundador, então não altera nenhuma contagem.

Linhas 1 a 41 (cabeçalho e Tabela) e Partes 1/3, 2/3 e 3/3: as Partes ficaram idênticas à produção conferida pela CQFP.

## 4. Conferência por script
O script fica em scratchpad t47g/aplica_confere.py e roda somente leitura sobre as linhas de base. Bases usadas:
- 91c82af: antes da T-47;
- 82bea20: produção conferida pela CQFP;
- arquivo gravado: depois das erratas da GCB.

| Verificação | Resultado |
|---|---|
| Produção vs 91c82af (conferência independente da produção) | 2 operações: insert da linha 26 (registro) e replace da linha 117→118. A linha 118 é igual a "linha 117 da base + espaço + frase literal" (assert True) |
| Gravado vs produção (git diff contra 82bea20) | 2 operações: insert da linha 8 (v3.2) e replace da linha 26→27, só o status. `git diff --stat`: 2 inserções, 1 remoção |
| Parte 1/3 | idêntica à produção; 1 linha diferente da base 91c82af (a do box plot); 128 linhas |
| Parte 2/3 | idêntica à produção e à base; 36 linhas |
| Parte 3/3 (itens e d-G) | idêntica à produção e à base; 75 linhas |
| d-G | 20 itens, 10 C e 10 E; sequência de gabaritos igual à base |
| Frase do Fundador | 2 ocorrências: linha 119 (curso) e linha 27 (citação no registro) |
| [TS], ocorrências | na Parte 3: 13, igual à base. No arquivo inteiro: 16 contra 15 da base; o +1 é a linha de registro (R3). Fora da Tabela: 15, igual à base |
| VOLÁTIL, ocorrências | na Parte 3: 7, igual à base. No arquivo inteiro: 13 contra 12 da base; o +1 é a linha de registro (R3). Fora da Tabela: 12, igual à base |
| Forma | 44078 bytes; sem CRLF; sem espaço no fim de linha; ponto médio U+00B7 (conferido pela CQFP e não tocado pela GCB) |

Os números de ocorrência acima diferem dos da CQFP (14→15 e 12→13), que contou linhas. O método é outro; a conclusão é a mesma: só a linha de registro acrescenta marca.

## 5. Sincronização com o Projeto
O canônico do Projeto no claude.ai, GCB/Lote5_v3_canonica_GCB-CPP.md (gravado em 8/10/2026), está em v3.1, sem a errata. O espelho saida/gcb passa a estar à frente dele em 3 linhas:
- a frase do box plot;
- a linha da Tabela;
- o rótulo v3.2.

Nenhum item, gabarito, [TS] ou VOLÁTIL diverge entre os dois. O transporte é ato do Fundador e por isso vai como gatilho E, como no precedente T-32 (Lote 4 v3.4) e na D-TRANSPORTE-FUNDADOR. O transporte não condiciona a T-48: o pacote lê o espelho.

## 6. Classificação
- T-47: CONCLUÍDA.
- R4 e rótulo v3.2: AGORA, aplicados.
- R3: PRÓXIMO, orientação de método para a T-48.
- R1 e R2: DESCARTADO.
- Transporte do Lote 5 v3.2 ao Projeto: AGORA, matéria do Fundador (gatilho E).

## Estado final proposto da T-47
T-47; GCB; (objeto inalterado); AGORA; **CONCLUÍDA** — reconciliada pela GCB em 13/10/2026 (saida/gcb/T47_reconciliacao_2026-10-13.md):
- QA gcb-cqfp: APROVADO COM RESSALVAS, 0/20 itens;
- R4 e rótulo v3.2 aplicados pela GCB; R1 e R2 descartados; R3 vira orientação de contagem na T-48;
- d-G 20/20 inalterado (10 C/10 E); Partes 2 e 3 idênticas à base;
- liberada como condição da T-48.

Saída: saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md (v3.2) + saida/gcb/lote5_errata_tukey_2026-10-13.md + saida/gcb/QA_T47_2026-10-13_gcb-cqfp.md + saida/gcb/T47_reconciliacao_2026-10-13.md

## BLOCO PARA_PRESIDENCIA
GATILHO E | GCB | Transporte ao Projeto do Lote 5 v3.2. É a v3.1 canônica com a errata T-47 (D-ERRATA-L5-TUKEY, frase literal do Fundador na legenda do box plot, curso 8.2), conferida pela gcb-cqfp (APROVADO COM RESSALVAS, 0/20) e reconciliada pela GCB. O espelho da fábrica está à frente do canônico do Projeto (GCB/Lote5_v3_canonica_GCB-CPP.md, v3.1) só em texto de curso e registro; o transporte não condiciona a T-48 | saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md; saida/gcb/lote5_errata_tukey_2026-10-13.md; saida/gcb/QA_T47_2026-10-13_gcb-cqfp.md; saida/gcb/T47_reconciliacao_2026-10-13.md | 3 linhas diferentes do Projeto: frase do box plot, linha da Tabela de Correções e rótulo v3.2. 20 itens AUTORAL inalterados (10 C/10 E); Parte 3 com 13 [TS] e 7 VOLÁTIL em ocorrências, iguais à base; Partes 2 e 3 idênticas à base 91c82af | O Fundador (ou a Presidência, por D-FUNDADOR-DELEGA-1) autoriza transportar saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md (v3.2) para GCB/Lote5_v3_canonica_GCB-CPP.md no Projeto, com registro da v3.2 pela Secretaria no Estado Canônico (D-CANONICOS nomeia a v3.1)? SIM/NÃO

## BLOCO TAREFAS
nenhuma
