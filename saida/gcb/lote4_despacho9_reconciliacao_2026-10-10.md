# lote4_despacho9_reconciliacao_2026-10-10.md — T-32 — 2026-10-10 — gerado por gcb-gerencia

Objeto: reconciliação da T-32 (Despacho 9, Lote 4 v3.3 → v3.4; O6 e D-DEREP), cadeia gcb-cpp → gcb-gerencia, sem QA (rito do próprio despacho: "correção textual de curso e de d-G, sem rodada de QA e sem nova conferência; nenhum gabarito muda").
Entradas: saida/gcb/lote4_despacho9_2026-10-10.md (relatório da gcb-cpp); saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md; saida/gcb/GCB_Despachos_pendentes_GCB-CPP.md (texto do Despacho 9 lido na versão HEAD).

## 1. Veredito
**T-32 CONCLUÍDA** (D1 GCB). Espelho do Lote 4 em v3.4, com exatamente as substituições do Despacho 9; gabaritos, [TS] e VOLÁTIL intactos. Nada a devolver à gcb-cpp.

## 2. Conferência por script (somente leitura; git show HEAD e git diff; scratchpad t32/verify.py)
Método independente do relatório da produtora: as substituições foram tiradas do texto do Despacho 9 (arquivo de Despachos no HEAD), aplicadas à cópia HEAD do Lote 4 e o resultado comparado byte a byte com o arquivo gravado.

| Verificação | Resultado |
|---|---|
| Cada trecho "antes" do despacho ocorre 1 vez no HEAD (10 trechos + linha nova da Tabela) | 1/1 em todos |
| HEAD + 11 substituições do despacho == arquivo gravado | True (só mudaram os trechos do despacho) |
| git diff --numstat do Lote 4 | 11 inserções / 9 remoções = 9 linhas alteradas (Conteúdo, O6, fontes normativas, 5.1.5, 5.2.5, 5.2.6, 5.3.6 P2, 6.4, d-G 11) + 2 linhas novas (cabeçalho v3.4; linha da Tabela); Despachos 1/1 |
| Despachos: HEAD + troca da linha "Pendente" == arquivo gravado | True (só a linha 2 mudou) |
| d-G: itens / C / E | 20 / 10 / 10 (HEAD idem); sequência de gabaritos idêntica |
| [TS] no d-G | 10 (HEAD idem); total do arquivo 12 = HEAD |
| VOLÁTIL no d-G | 1, item 15 (HEAD idem); total do arquivo 13 = HEAD |
| Parte 3 (d), enunciados | idêntica ao HEAD |
| "unidade de taquigrafia" / "Derep (antigo DETAQ)" / "N11 —" | 0 / 3 / 1 |
| L4-11: (d) e d-G sem "a confirmar" | sim; d-G 11 traz "gabarito definitivo E, conferido no GAB_DEFINITIVO_034_TRF6_002_01" |

Observações de forma, sem efeito:
- A linha nova da Tabela de Correções foi gravada com as barras de abertura e fechamento da tabela markdown; o conteúdo das cinco colunas é o literal do despacho.
- As ocorrências remanescentes de "a confirmar" (cabeçalho v3.2; linhas O2, O4, O6 — coluna de descrição —, O9, ITENS 18–20, Conferência A CONFIRMAR; nota de fontes; nota de produção) são registro histórico de correções, não ressalva de item. O despacho mandou trocar só o status da linha O6.
- A produtora não abriu o GAB_DEFINITIVO, corretamente: o despacho dá o gabarito definitivo E do item 81 como decisão da Presidência, "sem nova conferência". A marca "conferido no GAB_DEFINITIVO_034_TRF6_002_01" tem lastro registrado: conferência da GBQ-CFP em 7/10 (estado/ESTADO_CANONICO.md, log de 8/10) e decisão da Presidência de 07–09/10. A Gerência não reabre a conferência.

## 3. L4-11
No espelho do repositório, L4-11 (5.2, gabarito C) fica sem ressalva de texto e apto a simulado final, sempre sem BQ-0010 (TRF6 2024, item 81; regra R2 da GBQ). Enunciado e gabarito não mudaram. A ressalva de arquivo registrada em saida/simulados/simulado_1_gabarito.md (Despacho 9 pendente) fica superada para o espelho; a GBQ monta a partir de saida/gcb (v3.4).

## 4. Pendência de sincronização do canônico do Projeto
O canônico do Projeto no claude.ai, GCB/Lote4_v3_canonica_GCB-CPP.md, continua em v3.3 (linha O6 sem v3.4), e GCB/Despachos_pendentes_GCB-CPP.md continua com "Pendente: Despacho 9". O espelho saida/gcb está à frente do canônico. Sincronizar o Projeto é transporte do Fundador (a fábrica não escreve no Projeto). Até a sincronização, Projeto e espelho divergem só nos 11 trechos do Despacho 9 (texto de curso, d-G 11, Tabela de Correções e fontes normativas); nenhum gabarito, item, [TS] ou VOLÁTIL diverge.
Encaminhamento: GATILHO E em PARA_PRESIDENCIA.md (matéria do Fundador: transporte dos dois arquivos para o Projeto). Depois da sincronização, a entrega do despacho ("Despacho 9 aplicado; Lote 4 v3.4 atualizado no Projeto") fica cumprida, e a Secretaria registra Lote 4 v3.4 no Estado Canônico (D-CANONICOS e ativo GCB/Lote4 nomeiam v3.3).

## 5. Tarefas novas
Nenhuma. A sincronização não é tarefa de unidade da fábrica; vai pelo gatilho E.

## 6. Classificação
- T-32: CONCLUÍDA.
- Sincronização do Projeto (Lote 4 v3.4 + Despachos): AGORA, matéria do Fundador (gatilho E).
