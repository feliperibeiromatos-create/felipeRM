# GBQ-CSC-S — PROTOCOLO DE CALIBRAÇÃO DE SIMULADOS — v1 (12/10/2026)

Emitido pela GBQ-CSC-S (Sonnet 5.5, Alto) à GBQ, para aprovação. Tarefa A do ato de criação (9/10/2026).
Não monta simulado, não revisa conteúdo nem gabarito de item. Não recomenda nada sobre aplicação à candidata (PILOT_01), carga horária ou prioridades de estudo (matérias reservadas).

## 0. Base e verificações

Fontes lidas em 12/10/2026: claude/GBQ_Registro_AUTORAL_v2.md (150 itens); Edital - Camara 2026.pdf (Projeto); GBQ/pacote_v1_auto.json; Estado_Canonico_Camara_2026.md (v29).

Registro v2, recontado por script na transcrição integral das 150 linhas: 150 IDs únicos; 75 C e 75 E; 75 [TS]; 10 VOLÁTIL ou REVERIFICAR; 140 aptos a final. Por lote (itens / C / E / [TS] / [TS] com gabarito C / VOLÁTIL ou REVERIF. / aptos): L1 20/10/10/10/4/4/16; L1C 10/4/6/5/2/0/10; L2 30/15/15/15/7/0/30; L3 30/16/14/15/6/1/29; L4 20/10/10/10/5/1/19; L4C 10/5/5/5/2/0/10; A5 20/10/10/10/4/4/16; L5C 10/5/5/5/2/0/10. Todos os totais e a cobertura por subitem do registro conferem. Divergência: nenhuma.

Edital, conferido no PDF do Projeto em 12/10/2026: 7.1 (P1 = 90 itens; P2 = 90 itens); 7.2 (5 horas para as provas objetivas); 8.1 (180,00 pontos); 8.2 (julgamento do item vinculado ao comando); 8.3 (só pontua o item com uma, e somente uma, marcação); 8.11.2 (+1,00 concordância; −1,00 discordância; 0,00 sem marcação ou marcação dupla); 8.11.3 (nota da prova = soma das notas dos itens); 8.11.4 (NFPO = P1 + P2); 8.11.5 (eliminação se P1 < 18,00, P2 < 27,00 ou NFPO < 54,00). Os textos de instalação conferem.

Derivados (da GBQ-CSC-S, declarados como tais, não constam do edital):
- 5 h ÷ 180 itens = 1 min 40 s (100 s) por item. Para um simulado de N itens: N × 100 s.
- Limiar proporcional de referência: 18/90 = 20% (P1) e 27/90 = 30% (P2); 54/180 = 30% (NFPO).
- Fórmula adotada: limiar_ref = 0,20 × N para bloco ou simulado de P1; 0,30 × N para P2. Em simulado misto, calcula-se por prova e para o total (0,30 × N total). Ver pergunta 1 (seção 9).
- Ressalva fixa: "referência proporcional, não previsão de aprovação". Além disso, os simulados cobrem só o escopo deste Projeto (P1 itens 5 a 8 de TI e Dados; P2 itens 1.1 a 4.3), não as 90 questões de cada prova; o limiar é proporcional por construção, e não o limiar do edital.

## 1. Entrada (resultados)

Resultados chegam pelo Fundador. Formato mínimo para diagnóstico por subitem: uma marca por ID do simulado, em {C, E, B}, com B = sem marcação ou marcação dupla (ambos valem 0,00). Se vier só o total, registra-se o total e o diagnóstico por subitem fica "não calculável". Registrar também: data, simulado (arquivo e versão), prova (P1/P2/misto), tipo (diagnóstico ou final), tempo gasto e condição de aplicação, se informados. A candidata é identificada só como PILOT_01. A CSC-S registra e diagnostica; não recomenda.

## 2. Checklist de conferência (todo simulado, antes de aceitar a calibração)

Cada linha termina em CONFORME, VIOLAÇÃO (ID + regra) ou NÃO CONFERÍVEL (motivo). Violação: devolve-se à GBQ com o item e a regra, sem corrigir.

| # | Conferência | Fonte |
|---|---|---|
| C0 | Identificação: arquivo, versão, tipo (diagnóstico/final), prova, N total, N por bloco (AUTORAL / reais). A v0.1 do Simulado 0 não é aplicável. | D-SIM0-V01 |
| C1 | R1/R1-N: nenhum item VOLÁTIL ou REVERIFICAR em simulado final. IDs vedados: L1-Q14, L1-Q16, L1-Q18, L1-Q19, L4-15, A5-14, A5-15, A5-16, A5-17 (VOLÁTIL) e L3-Q21 (REVERIFICAR). Em diagnóstico são permitidos. | Registro v2 |
| C2 | R2: L4-11 e o item real TRF6 2024, Cargo 2, nº 81 (caderno 034_TRF6_002_01) nunca no mesmo simulado. | Registro v2; GBQ D1 de 8/10 |
| C3 | R3: os itens 70 a 76 do TRF6 (Parte D do Lote 3) são itens do banco; nunca contados duas vezes. Verificação por ID e por chave (certame, caderno, nº): cada um aparece uma só vez, no bloco de reais, e não entra no total do bloco AUTORAL. | Registro v2 |
| C4 | D-ADERENCIA / R4: item real de aderência parcial só em simulado diagnóstico. Os AUTORAL são de aderência direta por construção. | D-ADERENCIA |
| C5 | Itens reais em bloco de calibração separado, com nota própria. | Ato de criação |
| C6 | Gabarito de cada item conferido: AUTORAL contra o registro v2 (ID existe, gabarito, subitem, [TS]); reais contra o banco (gabarito definitivo, não preliminar; item não anulado). Anulados (X) ficam fora de simulado. Anulados do TRF6 2024, Cargo 2: 58, 105 e 117 (conferido no GAB definitivo do Projeto em 12/10/2026). | D-BANCO-01 |
| C7 | Comando e texto-base: cada item traz o comando original (texto_comando) e o texto-base, quando houver, porque o edital 8.2 vincula o julgamento ao comando. Comando com faixa de IDs de lote ("itens de 1 a 6") exige o original preservado ou a normalização declarada. | D-SIM0-V01; D-SCHEMA-02 |
| C8 | Escopo: todo item mapeado a subitem do edital do Cargo 11 (P1 5.1 a 8.4; P2 1.1 a 4.3). Item de P1 itens 1 a 4 (Lotes 6a/6b) é NÃO CONFERÍVEL até o Registro AUTORAL v3, porque o registro v2 não os contém. | Registro v2; Estado v29 |
| C9 | D-83-SIMULADO: simulado final antes de 08/01/2027 sai sem item de 8.3, com registro da ausência. Alerta de cobertura: P2 1.8 tem 1 só item apto (L1-Q20). | Estado v29; Registro v2 |
| C10 | Duplicidade: nenhum ID repetido; nenhuma repetição de enunciado; nenhum item contado em dois blocos. | — |
| C11 | Contagens: N declarado = N de itens; N por prova; tempo declarado = N × 100 s (derivado). | Edital 7.1, 7.2 |
| C12 | Distribuição C/E e [TS] observada × registro (seção 5). | Registro v2 |

## 3. Planilha por simulado

Um bloco AUTORAL e um bloco de reais, separados. Colunas por bloco:

| Campo | Definição |
|---|---|
| N | itens do bloco |
| A | acertos (marca = gabarito) |
| E | erros (marca ≠ gabarito) |
| B | sem marcação ou marcação dupla |
| Conferência | A + E + B = N; senão ERRO e não se calcula o resto |
| Líquido | A − E (edital 8.11.2 e 8.11.3) |
| % | Líquido ÷ N |
| Limiar_ref | 0,20 × N (P1) ou 0,30 × N (P2) |
| Situação | "≥ referência" ou "< referência" |
| Ressalva | "referência proporcional, não previsão de aprovação" |

Em simulado misto: uma linha por prova e uma de total (NFPO proporcional = 0,30 × N total). Em bloco com N pequeno, mostrar também a fração (por exemplo, líquido 3 de 10).

## 4. Planilha por subitem

Uma linha por subitem do edital presente no simulado, para cada bloco (AUTORAL e reais) separadamente:

| Campo | Definição |
|---|---|
| Subitem | por exemplo P2-1.4 |
| n | itens do subitem no bloco |
| A, E, B | contagens |
| Líquido | A − E |
| Taxa de erro | E ÷ n |
| Taxa de abstenção | B ÷ n |
| Precisão nas marcadas (auxiliar, descritiva) | A ÷ (A + E), quando A + E > 0 |
| Leitura | "tendência" se n ≤ 2; com n ≥ 3, "indicação", sempre sem a palavra "medida" |

Com n ≤ 2, mostrar frações (1 de 2), nunca porcentagem isolada. Ressalva fixa em todo relatório: "com 1 ou 2 itens por subitem, o diagnóstico indica tendência, não medida".

## 5. Distribuição C/E e [TS]: observada × registro

Duas verificações:

1. Item a item (exata): para cada item AUTORAL do simulado, gabarito e marca [TS] iguais aos do registro v2. Qualquer diferença é VIOLAÇÃO (C6).
2. Agregada (descritiva, sem limiar fixo; a GBQ decide se desvio importa): observado no simulado × referência do registro.

| Referência do registro v2 | Itens | C | E | [TS] | [TS] com gabarito C |
|---|---|---|---|---|---|
| Todos | 150 | 75 | 75 | 75 | 32 |
| P1 (5.1 a 8.4) | 60 | 30 | 30 | 30 | 13 |
| P2 (1.1 a 4.3) | 90 | 45 | 45 | 45 | 19 |

Para reais: observado × distribuição do banco (24 C, 19 E e 3 X em 46 itens no relatório de 8/10; banco.csv não está no Projeto, então a referência fica NÃO CONFERÍVEL até a GBQ publicá-lo). A definição de [TS] é a do registro da GBQ; a CSC-S o trata como marcador binário e não o reinterpreta.

## 6. Relatório de calibração (formato)

1. Cabeçalho: simulado, versão, tipo, prova, data, origem do resultado (Fundador), PILOT_01.
2. Checklist C0 a C12: CONFORME, VIOLAÇÃO ou NÃO CONFERÍVEL, com IDs.
3. Nota do bloco AUTORAL (seção 3) e nota do bloco de reais (seção 3), separadas.
4. Comparação AUTORAL × reais: líquido ÷ N de cada bloco lado a lado, como porcentagem, porque o N difere; diferença em pontos percentuais; sem causa atribuída. Se o simulado não tiver os dois blocos (por exemplo o Simulado 0, só com itens do banco), registrar "comparação não aplicável".
5. Subitens (seção 4), em ordem do edital, com a ressalva fixa.
6. Distribuição observada × registro (seção 5).
7. Diagnóstico: descrição de onde o líquido, a taxa de erro ou a abstenção se concentram, em termos de subitem e de bloco; só o que a contagem sustenta. Sem recomendação de estudo, carga horária ou aplicação.
8. Ressalvas fixas: (a) "com 1 ou 2 itens por subitem, o diagnóstico indica tendência, não medida"; (b) "referência proporcional, não previsão de aprovação"; (c) o simulado cobre só o escopo deste Projeto; (d) matérias reservadas à PILOT_01 e ao Fundador não são tratadas.
9. Pendências e classificação AGORA / PRÓXIMO / BACKLOG / DESCARTADO.

## 7. Registro acumulado

Cada resultado reportado entra numa tabela de resultados por item (ID | marca | gabarito | acerto), mais um log por simulado (data, tipo, líquido, % e limiar). O acumulado por subitem só soma simulados de mesma versão de item; item retirado ou alterado por errata encerra a série daquele ID. GBQ-CSC-RES (PRÓXIMO; gatilho: primeiro simulado calibrado e aplicado) herda este registro.

## 8. Paralelização (decisão sobre a sugestão do ato de criação)

RECUSADA, motivo: a conferência do pacote (157 itens) já foi feita por script nesta sessão e a de cada simulado é uma checagem curta do mesmo script, de modo que um chat novo só somaria transporte do Fundador, que é o gargalo. Classificação: DESCARTADO. Reavaliar (BACKLOG) se houver mais de três simulados em conferência ao mesmo tempo.

## 9. Perguntas à GBQ (a CSC-S segue com o provisório indicado até a resposta)

1. Limiar: "20% do líquido em simulado de P1 e 30% em simulado de P2" foi lido como 20% e 30% do máximo possível (N pontos), que é o que o edital implica (18/90 e 27/90). Confirmar.
2. Os itens 70 a 76 do TRF6 saem no pacote v1 com aderência "parcial" (decisão da EXEC, baseada no GCE_BIP_retorno_v2.md; o QA da própria EXEC observou que a Parte D e o P9 não os qualificam assim). Pelo D-ADERENCIA, "parcial" os exclui de simulado final. Confirmar se são "parcial" ou "direta". Até lá, a CSC-S os trata como parcial (só diagnóstico).
3. Itens dos Lotes 6a/6b: fora do registro v2; a CSC-S só os conferirá com o Registro AUTORAL v3. O Estado v29 lista como VOLÁTEIS do 6a: 6A-01, 6A-09, 6A-10, 6A-14 e 6A-15.
4. Banco: o banco.csv não está no Projeto. Sem ele, as conferências C6 (reais) e C3 por chave (certame, caderno, nº) ficam NÃO CONFERÍVEL, e a dedup P9 × BQ (D-DEDUP-P9) continua com a GBQ.

FIM DO PROTOCOLO
