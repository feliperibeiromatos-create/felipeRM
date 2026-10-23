# RELATÓRIO — pacote.json v1 (ordem EXEC-01)

EXEC — Executora Automatizada, 12/10/2026. Gerência titular: GBQ (o gatilho A cabe à GBQ-CSC). Arquivo: GBQ/pacote_v1_auto.json.

## 1. Contrato e método

- O contrato EXPORTAR_pacote.md, anexado pelo Fundador, NÃO chegou à EXEC: não estava na sessão nem no Projeto.
- O pacote segue o carregador do consumidor real, o Protótipo 0 (artefato privado do Fundador, D-PLATAFORMA-0), lido em 12/10/2026, e os campos exigidos pela ordem (item e).
- Campos de item: id, lote, numero, comando, comandoOriginal (quando normalizado), textoBase, enunciado, gabarito, itemEdital, aderencia, rotulo, ts, volatil, justificativa, observacao, fonte; nos itens reais, também certame, cargo, ano, aplicacao e url.
- Campos de lote: id, nome, itensEdital, resumo, curso, pares{a,b,como}, pegadinhas{itemEdital,texto}, observacao, arquivos.
- Campos de discursiva: id, lote, tipo, genero, itensEdital, comando, linhas, aspectosValorados, apresentacao, padrao, quesitos, baseNormativa, observacao.
- Pipeline:
  - extração fiel por lote (5 produtores Sonnet), com as erratas das consolidações aplicadas;
  - QA independente por lote (5 pareceres Opus, rodada 1);
  - correções aplicadas;
  - montagem e validação por script;
  - conferência final pelo QA (Opus): CONFERIDO, sem pendências.

## 2. Validação

- JSON parse: OK (390403 bytes).
- IDs: 157, todos únicos.
- Todo item tem id, enunciado e gabarito C ou E, além de itemEdital do edital, rotulo e aderencia.
- Gabarito, subitem e [TS]: 150/150 AUTORAL conferem com claude/GBQ_Registro_AUTORAL_v2.md (por script, QA Opus).
- Amostra de 10 enunciados (seed 20261012) idêntica à fonte. Todos os enunciados foram conferidos na rodada 1.

## 3. Contagens por lote

| Lote/rótulo | Itens | C | E | [TS] | VOLÁTIL |
|---|---|---|---|---|---|
| L1/AUTORAL | 20 | 10 | 10 | 10 | 4 |
| L1C/AUTORAL | 10 | 4 | 6 | 5 | 0 |
| L2/AUTORAL | 30 | 15 | 15 | 15 | 0 |
| L3/AUTORAL | 30 | 16 | 14 | 15 | 0 |
| L3/CEBRASPE_ANALOGA | 7 | 4 | 3 | 0 | 0 |
| L4/AUTORAL | 20 | 10 | 10 | 10 | 1 |
| L4C/AUTORAL | 10 | 5 | 5 | 5 | 0 |
| L5/AUTORAL | 20 | 10 | 10 | 10 | 4 |
| L5C/AUTORAL | 10 | 5 | 5 | 5 | 0 |

Totais:
- P2: 90 AUTORAL + 7 CEBRASPE_ANALOGA (TRF6 2024, itens 70–76; aderência parcial).
- P1: 60 AUTORAL.
- VOLÁTEIS (9): L1-Q14, Q16, Q18, Q19; L4-15; A5-14 a A5-17.
- REVERIFICAR normativo (1): L3-Q21.
- Todos os 10 estão marcados em observacao.

| Lote | curso (caracteres) | resumo | pares | pegadinhas |
|---|---|---|---|---|
| L1 | 23272 | 2488 | 17 | 31 |
| L1C | 2438 | 0 | 0 | 4 |
| L2 | 20101 | 2688 | 22 | 42 |
| L3 | 28008 | 2717 | 28 | 42 |
| L4 | 36901 | 4282 | 20 | 32 |
| L4C | 0 | 0 | 0 | 0 |
| L5 | 20562 | 3537 | 15 | 52 |
| L5C | 0 | 0 | 0 | 0 |

Discursivas (5):
- DISC-L1-Q (questao): itensEdital P2-1.4, P2-1.6, P2-1.7 (inferido; ver seção 6)
- DISC-L2-Q (questao): itensEdital P2-2.1, P2-2.2, P2-2.3, P2-2.7 (inferido; ver seção 6)
- DISC-L2-P (peca): itensEdital P2-2.4, P2-2.5, P2-2.7, P2-2.8 (inferido; ver seção 6)
- DISC-L3-Q (questao): itensEdital P2-3.2, P2-3.3, P2-4.1, P2-4.2 (inferido; ver seção 6)
- DISC-L3-P (peca): itensEdital P2-4.1, P2-4.3 (inferido; ver seção 6)

## 4. Contagem por item do edital

| Item | Itens | Escopo |
|---|---|---|
| P1-1 | 0 | futuro |
| P1-2 | 0 | futuro |
| P1-2.1 | 0 | futuro |
| P1-3 | 0 | futuro |
| P1-4 | 0 | futuro |
| P1-4.1 | 0 | futuro |
| P1-4.2 | 0 | futuro |
| P1-4.3 | 0 | futuro |
| P1-5.1 | 16 | atual |
| P1-5.2 | 5 | atual |
| P1-5.3 | 5 | atual |
| P1-6 | 4 | atual |
| P1-7.1 | 4 | atual |
| P1-8.1 | 3 | atual |
| P1-8.2 | 12 | atual |
| P1-8.3 | 4 | atual |
| P1-8.4 | 7 | atual |
| P2-1.1 | 4 | atual |
| P2-1.2 | 4 | atual |
| P2-1.3 | 4 | atual |
| P2-1.4 | 5 | atual |
| P2-1.5 | 4 | atual |
| P2-1.6 | 3 | atual |
| P2-1.7 | 3 | atual |
| P2-1.8 | 3 | atual |
| P2-2.1 | 4 | atual |
| P2-2.2 | 4 | atual |
| P2-2.3 | 4 | atual |
| P2-2.4 | 4 | atual |
| P2-2.5 | 4 | atual |
| P2-2.6 | 3 | atual |
| P2-2.7 | 4 | atual |
| P2-2.8 | 3 | atual |
| P2-3.1 | 4 | atual |
| P2-3.2 | 4 | atual |
| P2-3.3 | 4 | atual |
| P2-3.4 | 4 | atual |
| P2-4.1 | 12 | atual |
| P2-4.2 | 5 | atual |
| P2-4.3 | 4 | atual |

Itens 1–4 de TI (P1-1 a P1-4.3): incluídos no edital como "futuro", sem itens (Lotes 6a e 6b excluídos).

## 5. Exclusões

- banco/banco.csv: arquivo não recebido pela EXEC (não anexado à sessão nem ao Projeto).
- Simulado 0 (saida/simulados/simulado_0.md e gabarito): arquivos não recebidos pela EXEC.
- Lotes 6a e 6b: sem gatilho A da GCB (ordem EXEC-01, item c).
- "simulados" vai vazio ([]) porque o Simulado 0 não foi recebido. O Protótipo 0 aceita lista vazia e mostra "Nenhum simulado".

## 6. Decisões de FORMA da EXEC (sem mérito)

1. Justificativa = comentário do d-G sem o prefixo de metadados (gabarito, [TS], VOLÁTIL, subitem, "convertido"), já que esses dados estão em campos próprios. As referências internas do d-G ("Lição O10", "R-4C1", "Risco BAIXO", [NORMATIVO — QA]) foram mantidas; retirá-las é PRÓXIMO, na edição do estudante (GPAI).
2. Comandos com faixa de IDs (60 itens, Lotes 4, 4-C, 5 e 5-C) foram normalizados para "julgue os itens a seguir.", para funcionar em simulado embaralhado. O texto original fica em "comandoOriginal".
3. itensEdital das discursivas: a fonte não mapeia, então foi inferido a partir das alíneas e dos quesitos, com observacao. A confirmação cabe à GCE.
4. Aderência "parcial" dos itens 70–76, conforme GCE_BIP_retorno_v2.md, seção 2.
5. Lotes complementares (1-C, 4-C, 5-C) entram como lotes próprios. A fonte não tem curso nem resumo, então esses campos vão vazios (o 1-C traz o adendo do 1.4 como curso).

## 7. Pendências classificadas

AGORA:
- GBQ: emitir o gatilho A.
- Fundador: carregar o pacote no Protótipo 0 (aba Dados) para teste.
- Fundador: enviar à EXEC o banco.csv, o Simulado 0 e o EXPORTAR_pacote.md, se a GBQ quiser a v1.1 completa.

PRÓXIMO:
- v1.1 com o banco (apenas linhas sem "QA PENDENTE") e o Simulado 0.
- Conferir o pacote contra o contrato EXPORTAR_pacote.md.
- O montador de simulados deve excluir de simulado final os itens com volatil=true E os itens com "REVERIFICAR" em observacao (L3-Q21).
- Itens 70–76: deduplicar contra o banco (R3 do registro GBQ e D-DEDUP-P9) quando o banco entrar.
- Edição do estudante: limpar referências internas.

Questões de MÉRITO para as Gerências (pela Presidência; não alteradas):
- GCE, Lote 2: o resumo 2.4 diz "Convenção exata da Câmara: NÃO VERIFICADA", mas o curso 2.4, depois da E3, diz "observada nas notas oficiais de 2026". A contradição é parcial. Está registrada em observacao do lote.
- GCE, Lote 3: o par 20 diz "suprimida pela Lei 13.853/2019", e o curso 4.1 (E1/E3) diz "MP nº 869/2018, convertida na Lei 13.853/2019". Harmonizar exige errata.
- GCE, Lote 1: o motivo do Adendo E7/E8 cita as parcelas "6,00 + 7,00 + 1,30", mas os valores aplicados são 5,00 + 4,00 + 5,30. A soma está correta.
- GCB, Lote 4: o curso e a justificativa do L4-11 ainda dizem que o item 81 do TRF6 está "a confirmar". O gabarito definitivo E já foi conferido (GCE_ItensReais_P9_GCE.md). Está anotado em observacao do L4-11.

BACKLOG: nenhum.

## 8. Rastro

- Pareceres de QA por lote: rodada 1 e conferência final, consolidados em GBQ/pacote_v1_QA_auto.md.
- Fragmentos e scripts ficam na sessão da EXEC (exec01/frag, exec01/scripts).

FIM DO RELATÓRIO