# GBQ-CSC-S — PROTOCOLO DE CALIBRAÇÃO DE SIMULADOS — v1.1 (12/10/2026)

Substitui a v1 (GBQ/CSC-S_Protocolo_Calibracao_v1.md, histórico). Aprovado pela GBQ em 12/10/2026 com emendas (R0, C1 ampliado, C13, referências da v3, respostas às 4 perguntas), incorporadas aqui. Emitido pela GBQ-CSC-S (Sonnet 5.5, Alto).
Não monta simulado, não revisa conteúdo nem gabarito de item. Não recomenda nada sobre aplicação à candidata (PILOT_01), carga horária ou prioridades de estudo (matérias reservadas).

## 0. Base e verificações

Registro vigente: claude/GBQ_Registro_AUTORAL_v3.md (180 AUTORAL; substitui a v2 como referência de C1, C6, C8 e C12).
Recontagem pela CSC-S em 12/10/2026 (script sobre a transcrição das linhas da v2, já conferidas 150/150 contra o pacote da EXEC, mais as 30 linhas dos Lotes 6a e 6b): 180 IDs únicos; 89 C e 91 E; 91 [TS]; 37 [TS] com gabarito C; 15 VOLÁTIL ou REVERIF.; 165 aptos. Por prova: P1 90 itens (44 C, 46 E, 46 [TS], 18 [TS] com C, 10 inaptos, 80 aptos); P2 90 itens (45 C, 45 E, 45 [TS], 19 [TS] com C, 5 inaptos, 85 aptos). Lotes 6a e 6b: 15 itens cada; 6a = 7 C, 8 E, 8 [TS] (2 com C), 5 VOLÁTEIS; 6b = 7 C, 8 E, 8 [TS] (3 com C), 0 VOLÁTIL. Cobertura P1-1 7/10, P1-2 1/1, P1-2.1 4/4, P1-3 3/5, P1-4.1 4/4, P1-4.2 3/3, P1-4.3 3/3. Tudo igual ao declarado na v3. Limite da recontagem: as 150 linhas da v3 não foram retranscritas; conferi que a v3 = v2 conferida + Lotes 6.

Edital (PDF do Projeto, conferido em 12/10/2026): 7.1 (P1 = 90; P2 = 90); 7.2 (5 h); 8.1 (180,00 pontos); 8.2 (julgamento vinculado ao comando); 8.3 (uma, e somente uma, marcação); 8.11.2 (+1,00; −1,00; 0,00 sem marcação ou marcação dupla); 8.11.3; 8.11.4 (NFPO = P1 + P2); 8.11.5 (eliminação se P1 < 18,00, P2 < 27,00 ou NFPO < 54,00).

Derivados (da CSC-S; não constam do edital):
- 5 h ÷ 180 itens = 100 s (1 min 40 s) por item; simulado de N itens: N × 100 s.
- Limiar proporcional de referência (CONFIRMADO pela GBQ): 20% (P1) e 30% (P2) do máximo possível do bloco (N), proporcional a 18/90 e 27/90. Limiar_ref = 0,20 × N (P1) ou 0,30 × N (P2); simulado misto: por prova e total (0,30 × N total).
- Ressalva fixa: "referência proporcional, não previsão de aprovação". Os simulados cobrem só o escopo deste Projeto (P1 itens 1 a 8 de TI e Dados; P2 itens 1.1 a 4.3), não as 90 questões de cada prova.

## 1. Entrada (resultados)

Resultados chegam pelo Fundador. Formato mínimo para diagnóstico por subitem: uma marca por ID, em {C, E, B}, com B = sem marcação ou marcação dupla (ambos 0,00). Só o total: registra-se o total e o subitem fica "não calculável". Registrar também data, simulado (arquivo e versão), prova, tipo (diagnóstico ou final), tempo gasto e condição de aplicação, se informados. A candidata é identificada só como PILOT_01.

## 2. Checklist de conferência (todo simulado)

Cada linha termina em CONFORME, VIOLAÇÃO (ID + regra) ou NÃO CONFERÍVEL (motivo). Violação: devolve-se à GBQ com o item e a regra, sem corrigir.

| # | Conferência | Fonte |
|---|---|---|
| C0 / R0 | Identificação: arquivo, versão, tipo (diagnóstico/final), prova, N total, N por bloco. Subitem SEMPRE com prefixo P1- ou P2- (os números colidem: P1-4.1 = backup e malware; P2-4.1 = LGPD em transcrição e IA). Subitem sem prefixo = VIOLAÇÃO. A v0.1 do Simulado 0 não é aplicável. | Registro v3 R0; D-SIM0-V01 |
| C1 | R1/R1-N: nenhum item VOLÁTIL ou REVERIFICAR em simulado final. IDs vedados (15): L1-Q14, L1-Q16, L1-Q18, L1-Q19, L4-15, A5-14, A5-15, A5-16, A5-17, 6A-01, 6A-09, 6A-10, 6A-14, 6A-15 (VOLÁTIL) e L3-Q21 (REVERIFICAR). Em diagnóstico são permitidos. | Registro v3 |
| C2 | R2: L4-11 e o item real TRF6 2024, Cargo 2, nº 81 (caderno 034_TRF6_002_01) nunca no mesmo simulado. | Registro v3 |
| C3 | R3: itens reais não entram no registro e não se contam duas vezes; fonte canônica = banco (D-DEDUP-P9). Vale para TRF6 70 a 76 e 96 e 98. Verificação por ID e por chave (certame, caderno, nº): cada um aparece uma só vez, no bloco de reais. | Registro v3 |
| C4 | D-ADERENCIA / R4: item real de aderência parcial só em simulado diagnóstico. TRF6 70 a 76 = PARCIAL (decisão de mérito da GBQ, 12/10; também parcial o uso no P1-6); TRF6 96 e 98 = parciais. Os AUTORAL são de aderência direta por construção. | Registro v3 R4 |
| C5 | Itens reais em bloco de calibração separado, com nota própria. | Ato de criação |
| C6 | Gabarito de cada item: AUTORAL contra o registro v3 (ID, gabarito, subitem com prefixo, [TS]); reais contra os campos do pacote da fábrica e contra o gabarito definitivo oficial (PDF do Projeto ou cdn.cebraspe.org.br); anulados (X) fora de simulado. Anulados TRF6 2024, Cargo 2: 58, 105 e 117. | D-BANCO-01 |
| C7 | Comando e texto-base: comando original (texto_comando) e texto-base presentes; comando com faixa de IDs exige o original preservado ou normalização declarada. | D-SIM0-V01; D-SCHEMA-02 |
| C8 | Escopo: todo item mapeado a subitem do edital do Cargo 11 (P1 1 a 8.4; P2 1.1 a 4.3). Itens 6A/6B passam a ser conferíveis pela v3. Item fora da v3 e sem rótulo de banco = NÃO CONFERÍVEL. | Registro v3 |
| C9 | D-83-SIMULADO: simulado final antes de 08/01/2027 sai sem item de P1-8.3, com registro da ausência. Alertas: P2-1.8 só L1-Q20 apto; P1-2 só 6B-01; P1-4 (governança digital) 0 itens; P1-3 3 aptos de 5. | Registro v3 |
| C10 | Duplicidade: nenhum ID repetido; nenhum enunciado repetido; nenhum item em dois blocos. | — |
| C11 | Contagens: N declarado = N de itens; N por prova; tempo declarado = N × 100 s (derivado). | Edital 7.1, 7.2 |
| C12 | Distribuição C/E e [TS] observada × registro (seção 5). | Registro v3 |
| C13 (R5) | TRF6 96 e 98 fora de QUALQUER simulado (diagnóstico ou final) até a conferência visual humana do PDF. Presença = VIOLAÇÃO. | Registro v3 R5 |

Simulado 0 v0.2 e Simulado 1: o checklist C0–C13 só roda depois das tarefas T-25/T-31 da fábrica (a GBQ confirmará). Até lá: NÃO CONFERÍVEL — pré-condição T-25/T-31 não confirmada.

## 3. Planilha por simulado

Um bloco AUTORAL e um bloco de reais, separados. Por bloco: N; A (acertos); E (erros); B (sem marcação ou marcação dupla); Conferência A + E + B = N (senão ERRO e não se calcula o resto); Líquido = A − E (edital 8.11.2 e 8.11.3); % = Líquido ÷ N; Limiar_ref = 0,20 × N (P1) ou 0,30 × N (P2); Situação "≥ referência" ou "< referência", sempre com a ressalva fixa. Simulado misto: uma linha por prova e uma de total. Com N pequeno, mostrar também a fração.

## 4. Planilha por subitem

Uma linha por subitem presente (com prefixo de prova), por bloco, separadamente: n; A; E; B; Líquido (A − E); Taxa de erro (E ÷ n); Taxa de abstenção (B ÷ n); Precisão nas marcadas (auxiliar, descritiva: A ÷ (A + E), quando A + E > 0); Leitura ("tendência" se n ≤ 2; com n ≥ 3, "indicação"; nunca "medida"). Com n ≤ 2, mostrar frações, nunca porcentagem isolada. Ressalva fixa: "com 1 ou 2 itens por subitem, o diagnóstico indica tendência, não medida".

## 5. Distribuição C/E e [TS]: observada × registro

1. Item a item (exata): para cada item AUTORAL, gabarito, subitem e [TS] iguais aos do registro v3; diferença = VIOLAÇÃO (C6).
2. Agregada (descritiva, sem limiar fixo; a GBQ decide se o desvio importa):

| Referência (Registro v3) | Itens | C | E | [TS] | [TS] com gabarito C |
|---|---|---|---|---|---|
| Total | 180 | 89 | 91 | 91 | 37 |
| P1 | 90 | 44 | 46 | 46 | 18 |
| P2 | 90 | 45 | 45 | 45 | 19 |

Para reais: observado × distribuição do banco (referência NÃO CONFERÍVEL até o banco.csv estar no Projeto). [TS] é marcador binário do registro da GBQ; a CSC-S não o reinterpreta.

## 6. Relatório de calibração (formato)

1. Cabeçalho: simulado, versão, tipo, prova, data, origem do resultado (Fundador), PILOT_01.
2. Checklist C0 a C13: CONFORME, VIOLAÇÃO ou NÃO CONFERÍVEL, com IDs.
3. Nota do bloco AUTORAL e nota do bloco de reais, separadas (seção 3).
4. Comparação AUTORAL × reais: líquido ÷ N de cada bloco lado a lado, em porcentagem, e diferença em pontos percentuais, sem causa atribuída. Sem os dois blocos (por exemplo, simulado só com itens do banco): "comparação não aplicável".
5. Subitens (seção 4), na ordem do edital, com a ressalva fixa.
6. Distribuição observada × registro (seção 5).
7. Diagnóstico: onde líquido, taxa de erro ou abstenção se concentram, por subitem e por bloco; só o que a contagem sustenta; sem recomendação de estudo, carga horária ou aplicação.
8. Ressalvas fixas: (a) "com 1 ou 2 itens por subitem, o diagnóstico indica tendência, não medida"; (b) "referência proporcional, não previsão de aprovação"; (c) o simulado cobre só o escopo deste Projeto; (d) matérias reservadas à PILOT_01 e ao Fundador não são tratadas.
9. Pendências e classificação AGORA / PRÓXIMO / BACKLOG / DESCARTADO.

## 7. Registro acumulado

Resultados por item (ID | marca | gabarito | acerto) e log por simulado (data, tipo, líquido, % e limiar). O acumulado por subitem só soma simulados da mesma versão de item; item retirado ou alterado por errata encerra a série daquele ID. GBQ-CSC-RES (PRÓXIMO; gatilho: primeiro simulado calibrado e aplicado) herda este registro.

## 8. Tarefa B refeita: conferência do pacote da FÁBRICA (D-PACOTE-BASE)

Pré-condição: o Fundador publica o pacote da fábrica no Projeto (sugestão: GBQ/pacote_v1_fabrica.json). Até lá, nada a executar além do preparo (registro v3 já transcrito e totais conferidos).
(a) 180 AUTORAL × Registro v3: IDs 1:1; gabarito, subitem com prefixo, [TS], volátil e REVERIFICAR.
(b) Lote 6b: qualquer diferença de gabarito, subitem ou [TS] nos itens 6B entre o pacote e a v3 (errata T-17 / A-6b-1) é reportada, sem corrigir (R6).
(c) 60 itens do banco: rótulo (CEBRASPE_ANALOGA; OFICIAL só no ciclo da Câmara); gabarito definitivo; nenhum anulado (X); nenhum "QA PENDENTE"; aderência conforme a arbitragem T-03 (33 DIRETA / 27 PARCIAL no Simulado 0 v0.2, segundo a Presidência); TRF6 70–76, 96 e 98 contados uma só vez (R3) e, quanto a 96 e 98, ausentes de simulado (C13).
(d) Comparação com o pacote da EXEC nos 150 AUTORAL comuns: gabarito, subitem, [TS], volátil e igualdade de enunciado (por diff).
(e) Decisões de forma da EXEC (comandoOriginal; justificativas sem prefixo): registrar presença ou ausência; ausência não é divergência.
Retorno: um bloco à GBQ com (a) a (e), divergências por ID e parecer "sem objeção" ou "com objeção" ao gatilho A (um só, emitido pela GBQ).

## 9. Paralelização (sugestão GBQ-CSC-BQ)

RECUSADA por ora, com este motivo: a parte (c) pede o gabarito definitivo oficial de poucos certames (um PDF por certame e cargo), que a CSC-S abre em sequência. Classificação: DESCARTADO. Reavalio (BACKLOG) se o pacote não trouxer certame, caderno, número e url suficientes para a conferência, ou se forem necessários mais de 10 PDFs.

FIM DO PROTOCOLO v1.1
