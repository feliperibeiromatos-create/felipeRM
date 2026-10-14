# T58_reconciliacao_2026-10-13.md — T-58 — 2026-10-13 — gerado por gce-gerencia

Objeto: reconciliação (D1) da T-58, errata de forma do curso do Lote 3 (D1-T54-b, `saida/gce/T54_item5_decisao_2026-10-13.md`, seção 3.1). Produção: `saida/gce/lote3_errata3_2026-10-13.md` (gce-cpp). QA: `saida/gce/QA_T58_2026-10-13_gce-cqfp.md` (gce-cqfp, APROVADO, 0 itens reprovados, observações O-1 a O-4). Também conferida aqui, só para fechar a D1 da GCE, a parte (a) do item 5 da T-54 (D1-T54-a), que a GBQ aplicou na T-57 (pacote v1.4). Leitura somente, com script próprio no scratchpad (`t58rec/chk.py`, Python `-I`). Nenhum arquivo de lote, da GBQ ou de interface foi alterado; só este arquivo foi gravado.

## 1. Conferência da GCE (somente leitura)

| # | Ponto | Resultado |
|---|---|---|
| 1 | `saida/gce/GCE_Lote3_v2_CPP.md` atual | SHA-256 `58b0dbedb35897d2c7244394576f0d0b53b4074ff7af2920ba9a8083f75ef438`, 57200 bytes = o "depois" da produção e do QA. OK |
| 2 | `saida/gce/GCE_Lote3_padroes_GCE.md` | SHA-256 `cc17ec964b53…`, igual à base da D1-T54. Não foi tocado. OK |
| 3 | Pacote v1.4 (`saida/pacote/pacote.json`) | SHA-256 `f8c0c131f16dab52b1646b3d302670a3afc498b23ac03a7b34a8ff97520ffa54`, 621744 bytes. Comparação com a v1.3 (`git show 9622604`, SHA-256 `fdcb7afdb4fb…`): no nível de cima, só mudam `nome`, `lotes` e `discursivas`. OK |
| 4 | D1–D4 (`discursivas[0..3].padrao`) | Idênticas às da v1.3. A D4 termina no anexo `Notas de correção (GCE, R2–R4)` mais as linhas 14–23 literais do arquivo de padrões. OK, como a D1 previu |
| 5 | D5 (`discursivas[4].padrao`) | Só o `padrao` difere da v1.3. O diff tem exatamente 2 operações: no rótulo, "2" → "3" (`R2–R4` → `R3–R4`), e a remoção do trecho literal das linhas 14–20 (R2, 7 linhas). A D5 termina em `\n\nNotas de correção (GCE, R3–R4)\n` mais as linhas 21–23 literais. Na D5: 0 "R2. Alínea c". OK, como a D1 previu |
| 6 | Curso do L3 (`lotes[3].curso`) | Diff v1.3 → v1.4 só "eu" → "se" (difflib: insere `s`, apaga `u`). No pacote inteiro: "que eu possa afirmar" 0; "que se possa afirmar" 1, no curso do L3. OK |
| 7 | Edição do estudante | `DISCURSIVAS_padrao.md`: o anexo da D5 (linha 506 em diante) traz só as notas R3 e R4. O anexo da D4 (linha 406 em diante) fica com R2–R4. `L3_estudo.md` 422: `jurisprudência firmada que se possa afirmar):`. OK |
| 8 | Projeto do claude.ai | `GCE_Lote3_v2_CPP.md` foi lido por `project_read`. O arquivo tem a entrada T-44 na Tabela de Correções, não tem a entrada T-54, e o curso 4.2 ainda diz "que eu possa afirmar". É, portanto, a versão anterior à T-58 (a da D-TRANSPORTE-B-L3, `a9c3fba5…`); conferi o conteúdo, não calculei o hash. A versão do Projeto diverge da fábrica, como previsto (O-4) |

Ressalva: a T-57 ainda não tem QA da gbq-cqe (não há `QA_T57_*` em `saida/pacote/`). As linhas 3 a 7 acima são uma conferência da GCE para fechar a sua D1 e não substituem o QA da T-57.

## 2. Decisões (D1 da GCE)

| # | Observação ou ponto | Decisão | Classe |
|---|---|---|---|
| D1-T58-1 | Veredito da gce-cqfp | APROVADO aceito. Saem exatamente as 2 operações da seção 3.1 da D1-T54 (E-1 e E-2), com texto literal. Contagens de controle iguais: [TS] 19, VOLÁTIL 4, NORMATIVO — QA 36, [V 2. De "(c) PARES" até o fim, o texto é idêntico. Nenhum item, gabarito, fonte, [TS], VOLÁTIL ou marca [V] mudou. A errata fica incorporada ao espelho da fábrica | AGORA (encerrada) |
| D1-T58-2 | O-1: com as quebras de linha unidas, "que eu possa afirmar" aparece 2 vezes no arquivo (linha 76, N4, e a citação do "onde se lê" no registro T-54, linhas 38–39) | Sem ação. As duas ocorrências são intencionais: a N4 é registro de processo em primeira pessoa (D1-T54-b), e a Tabela de Correções precisa citar o texto antigo. Nenhuma das duas é exportada (0 no pacote v1.4, linha 6 da conferência). O critério da D1, contagem por linha, foi cumprido | DESCARTADO |
| D1-T58-3 | O-2: `gerador_v1_3/relatorio_v1_3.py` 440 registra "que eu possa afirmar" como mantido | Resolvida pela T-57. O relatório da v1.4 (`pacote_relatorio_2026-10-13_v1_4.md`, linha 639) lista a expressão em "Saíram desta lista na v1.4 … (T-58)", e a varredura da edição dá 0 (linha 637). O `gerador_v1_3/` fica intacto por desenho, como histórico. Sem tarefa | DESCARTADO |
| D1-T58-4 | O-3: a produção conta 1029/1033 linhas (`split('\n')`) e o QA conta 1028/1032 quebras | Sem ação nesta tarefa: é o mesmo arquivo e os hashes conferem. Daqui em diante, toda instrução de conferência da GCE declara o critério de contagem de linhas e usa o número de quebras (`wc -l`) como padrão. Isso é regra de forma das próximas D1 da GCE e não gera tarefa | BACKLOG (forma) |
| D1-T58-5 | O-4: o SHA-256 novo diverge do arquivo transportado ao Projeto por D-TRANSPORTE-B-L3 | O transporte é matéria do Fundador e vai como GATILHO E (seção 4). O transporte não depende do QA nem do gatilho A da T-57: o arquivo da GCE está fechado | AGORA (gatilho E) |
| D1-T58-6 | D5 do pacote v1.4 (parte (a) do item 5, aplicada pela GBQ) | Ficou como a D1-T54-a previu (linhas 4–7 da conferência): R2 fora da D5, R3–R4 literais (linhas 21–23), D4 sem mudança, comando, aspectos, quesitos e conceitos da D5 iguais. Nada a corrigir do lado da GCE | AGORA (encerrada) |
| D1-T58-7 | Rótulo do anexo da D5, "Notas de correção (GCE, R3–R4)" | ACEITO. Ele descreve exatamente o conteúdo (R3 e R4, decisões da GCE), é simétrico ao rótulo da D4 ("GCE, R2–R4") e coincide com a sugestão da própria D1-T54-a. Na edição do estudante, " (GCE, R3–R4)" é apagado como identificador interno e sobra só "Notas de correção", como nas demais. A escolha do rótulo cabe à GBQ (exportação); a GCE concorda | AGORA (encerrada) |
| D1-T58-8 | Participação da gce-cqfp na T-57 ("+ gce-cqfp para eventual errata da GCE", linha da T-57) | Atendida pela QA da T-58: a única errata da GCE no ciclo é a E-1/E-2, já APROVADA. A D5 é exportação da GBQ, e o QA dela é da gbq-cqe. A GCE dispensa outra rodada da gce-cqfp na T-57. Sugestão à gbq-cqe, sem caráter de tarefa: conferir (i) D5 = `padrao` da v1.3 menos as linhas 14–20, com o rótulo trocado; (ii) curso do L3 com só "eu" → "se"; (iii) D4 idêntica | AGORA (encerrada) |

## 3. Estado proposto da T-58 (para o orquestrador aplicar em TAREFAS.md)

```
CONCLUÍDA (ciclo 2026-10-13 s6c1; QA gce-cqfp APROVADO, 0 itens reprovados, observações O-1 a O-4 decididas; reconciliada pela GCE em saida/gce/T58_reconciliacao_2026-10-13.md; GCE_Lote3_v2_CPP.md SHA-256 58b0dbed…; transporte ao Projeto pedido por GATILHO E)
```

Nota para a linha da T-54 (titular GBQ; registro só informativo): o item (5) está cumprido do lado da GCE. A parte (b) foi feita na T-58 (CONCLUÍDA). A parte (a) foi aplicada na T-57 (pacote v1.4) e a GCE a conferiu conforme a sua D1; falta só o QA da gbq-cqe na própria T-57.

## 4. BLOCO PARA_PRESIDENCIA

```
GATILHO E | GCE | Transporte ao Projeto do claude.ai do GCE_Lote3_v2_CPP.md com a errata T-58 (D1-T54-b: curso 4.2, "que eu possa afirmar" → "que se possa afirmar", + registro T-54 na Tabela de Correções), substituindo a versão transportada por D-TRANSPORTE-B-L3 | saida/gce/GCE_Lote3_v2_CPP.md (SHA-256 58b0dbedb35897d2c7244394576f0d0b53b4074ff7af2920ba9a8083f75ef438, 57200 bytes) → Projeto GCE_Lote3_v2_CPP.md (hoje a versão a9c3fba59aafd21e…, 56929 bytes; conferido por project_read: sem a entrada T-54); saida/gce/lote3_errata3_2026-10-13.md; saida/gce/QA_T58_2026-10-13_gce-cqfp.md; saida/gce/T58_reconciliacao_2026-10-13.md | 2 operações (4 linhas inseridas na Tabela de Correções + 1 linha trocada, só "eu" → "se"), +271 bytes, +4 linhas; [TS] 19→19, VOLÁTIL 4→4, NORMATIVO — QA 36→36, [V 2→2; de "(c) PARES" ao fim idêntico (SHA-256 4c2d7ab83bc53e0d…); 0 item, 0 gabarito, 0 fonte alterados; QA gce-cqfp APROVADO, 0 reprovados; versão anterior preservada no git (2c681b9) e o "onde se lê" citado na Tabela de Correções, portanto sem exclusão de ativo canônico; sem gasto e sem entrega à candidata (a edição v1.4 segue reservada, D-ENTREGA-V13-ESPERA); independe do QA e do gatilho A da T-57 | Transportar agora saida/gce/GCE_Lote3_v2_CPP.md (58b0dbed…) para GCE_Lote3_v2_CPP.md no Projeto, substituindo a versão a9c3fba5…, no passo 7 do orquestrador, com a Secretaria registrando a versão (T-58) no Estado Canônico — SIM ou NÃO? (Se a presidencia entender cabível a delegação D-FUNDADOR-DELEGA-1, precedentes D-TRANSPORTE-L1-AD5 e D-TRANSPORTE-L5-V32.)
```

## 5. BLOCO TAREFAS

nenhuma.

(O registro da versão pela Secretaria depois do transporte segue o rito da T-52, por proposta da presidencia; não é tarefa da GCE.)

REMETENTE: gce-gerencia
DESTINATÁRIO: orquestrador (TAREFAS.md e PARA_PRESIDENCIA.md); cópia gce-cpp, gce-cqfp, gbq-gerencia (D1-T58-6 a D1-T58-8)
