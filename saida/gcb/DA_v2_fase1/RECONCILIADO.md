# RECONCILIADO.md — T-130 — 2026-10-25 — gerado por gcb-gerencia

ORDEM_DA_V2_FASE1 (ordens/ORDEM_DA_V2_FASE1.md), ciclo 2026-10-25 s19c1. Itens 2 (P1-DA-2.1, quatro unidades), 3.4 e 4.4 no formato DA-v2, com o adendo v2.1 adotado (D-ESPEC-DA-V2-1). Esta é a reconciliação da GCB: confere as entregas, decide D1 e emite gatilhos. A GCB não produziu nem revisou conteúdo. Não alterei produção nem pacote. Não fiz commit.

Rodadas: produção gcb-cpp (sonnet) v1 → R1 (qa-normativo-da: 1 ERRO em 60 itens; gcb-cqfp-didatico: 10 de 67 reprovados, 14,9%) → v2 (resposta_R1.md) → R2 (qa-normativo-da: APROVADO COM RESSALVAS, 0 de 60 com ERRO; gcb-cqfp-didatico: APROVADO COM RESSALVAS nos 3 lotes, 0 de 67 reprovados) → errata de forma v2.1 (registro_errata_forma_v2_1.md), sem nova rodada. Foram 2 rodadas, o máximo da ordem. Nenhum GATE: a reprovação final é de 0%, e a maior taxa foi 14,9%, na R1.

## 0. Conferência da v2.1 contra o registro (diff v2 × v2.1)

- **md** (v2_producao.md × v2_1_producao.md): 15 trechos alterados, mais a linha 1, que é só o nome do arquivo. São os 17 registrados: R2-1 (L843, L847), R2-2 (L1566, L1726, L2051, L2052), R2-3 (L847, L1273), R2-4 (L2051), O-R2-1 (retirada da linha "ITEM DV3-10" em L1525) e O-R2-2 (L713, L994, L1305, L1307, L1501, L1503, L1594). Não há alteração fora do registro.
- **JSON** (diff estrutural campo a campo, v2 b2c2aed6…84e9a8 → v2.1 d741bca3bb73d60f1ed416a68b047392d924c360252a4d5ebbe97c5c8738450f; o SHA-256 confere com o informado): só mudaram 4 campos de texto, `lotes[DV2].curso`, `lotes[DV3].curso`, `topicos[P1-DA-3.4].resumo` e `topicos[P1-DA-4.4].resumo`, cada um com as substituições do registro. Nenhum item mudou: 0 enunciados, 0 gabaritos e 0 comentários alterados, nenhum item novo ou removido.
- **Contra a base v1.14** (saida/pacote/pacote.json, 070bc237…d495): 1.433 → 1.493 itens (60 novos, 0 removidos) e 0 gabaritos alterados. Dos itens já existentes, só 7 mudaram, os reais intercalados BQ-0122, 0127, 0132, 0137, 0145, 0148 e 0150, e só nos campos `itemEdital`, `comentario`, `mecanismo` e `tipo`.
- **Conclusão:** a v2.1 só mudou o que o registro declara. O objeto do gatilho A é o pacote v2.1 com o SHA acima.

## 1. Reconciliação das condições da R2

| Condição | Origem | Situação na v2.1 | Conferido por mim |
|---|---|---|---|
| O-R2-1, verificação conforme ≥ 10 no DV3 | didático R2 | Cumprida pela via (i): DV3-10 devolvido à verificação | Contagem no JSON pela ESPEC §7 (por `itemEdital`, só itens com `comentario`, sem contar os intercalados): P1-DA-2.1 23 − 12 = **11**; P1-DA-3.4 21 − 9 = **12**; P1-DA-4.4 23 − 13 = **10** |
| O-R2-2, número sem artigo (7 pontos) | didático R2 | Cumprida nos 7 pontos | Pelo diff |
| R2-1 a R2-4, citação e data | normativo R2 | Aplicadas | Pelo diff. O texto vem da transcrição do qa_normativo_R2, §1 |
| R-R2-1 a R-R2-6 e demais R | didático R2 | Não aplicadas | D1 no §2 |

## 2. D1 da GCB nos pontos abertos

**D1-1. Pegadinha da prioridade (DV3, última mini-lição), ligada a itens C (DV3-20 AP; BQ-0127 LIT).** Aceita nesta fase como exceção declarada. A pegadinha cumpre a regra do estilo §6.5: é SUP, observada no art. 69-A, § 1º, com A/B/MUDA, `par` e `texto` coerentes, conferidos pelo normativo R2 (N10) e pelo didático R2 (A3). O defeito está só no agrupamento de erros da plataforma, porque quem erra o DV3-20 cai em AP. Não há gabarito em disputa. A troca do gabarito do DV3-19 fica DESCARTADA. O remédio é o DV3-21, um E SUP de prioridade como item de verificação do P1-DA-4.4, aberto como T-145 (PRÓXIMO), com produção gcb-cpp e as duas QAs. Não bloqueia o gatilho A.

**D1-2. Cotas de mecanismo fora da faixa (DV2 E/CON = 5; DV3 E/SUP = 4 e E/GEN = 0).** Para esta fase, os três desvios estão de acordo com a ordem. A ordem (e) manda "rodar checa_estilo_DA.py … e justificar cada aviso no relatório do lote". O script só emite avisos, as cotas são aproximadas ("≈", ±3 pontos sobre o corpus), os três avisos foram justificados (resposta_R1.md §6, item 2) e o didático R2 os julgou ressalva R (§5(b)). O desvio é de 1 item por código, e o total de E (11 no DV2, 10 no DV3) está dentro da faixa de 8–12. Uma regra geral de que "o §6.5 prevalece sobre a cota de mecanismo, com desvio de ±1 por código aceito com justificativa", que valeria para as fases 2–4 e as ondas, seria uma interpretação permanente de regra adotada pelo Fundador (regras/estilo_banca_DA_v1.md §6.1 e §6.5; D-ESPEC-DA-V2-1). Não é do meu nível. Vai como gatilho E. O didático mostrou que o conflito só é estrutural no DV3. Por isso, o reequilíbrio (uma pegadinha SUP do DV3 recodificada como CON; uma CON do DV2 como AUT; um 11º E GEN no DV3) entra na T-148 (PRÓXIMO), junto com a troca por itens reais da onda 1.

**D1-3. Contagem da verificação.** A meta da ESPEC §7 ("mínimo de 10 por item-folha além dos intercalados … todas com comentario") está atingida nos três tópicos: 11, 12 e 10. Não há desvio de regra do Fundador e, portanto, não há gatilho. Os avisos "meta 10" do checa_pacote_v2.py (DV1 8, DV3 7) são erro de conta do script, que subtrai dos 20 itens DV os intercalados reais, embora estes não estejam entre os 20. Também não são válidas as contas que incluem itens D1/D2 sem `comentario` (33 e 29). A correção do script vai para a T-150 (GBQ, BACKLOG).

**D1-4. Decisões do produtor, ratificadas.** (i) As quatro unidades do item 2 viram quatro blocos `##` do lote DV1, todos sob P1-DA-2.1, e o P1-DA-2 (caput) fica sem bloco e sem item. O caput não tinha tópico no pacote v1.14 e passa de 3 itens para 0 com a reclassificação dos 3 reais, objeto do gatilho D. (ii) O DV3 é uma unidade que cobre a Lei 9.784 inteira (arts. 1º a 70). (iii) O desfazimento dos `resumo` e `pares` de D1/D2 sobrepostos (A6) fica aceito. As duas QAs aceitaram as três decisões.

**D1-5. Avisos do checa_pacote_v2 (0 bloqueios, 13 avisos).** Aceitos os seguintes. DIAG30, prefixos e lotes novos e marcas de produção (0 → 7, linhas `ITEM BQ-nnnn`) ficam para a GBQ no build (T-131). ITEM/quadros (6 avisos) é decisão de formato, ressalva R (linha 6). "Meta 10" está no D1-3. O aviso "2 parágrafos com mais de 4 frases" (DV2 3.4) vem do contador, que trata "art." como fim de frase, e não há frase nova.

**D1-6. Achados R não aplicados.** R-R2-1 (L876, art. 25, II), R-R2-2 (Sipec/SIPEC; "requisição" e "exercício provisório"), R-R2-3 (comando do DV2-18 entrega o MUDA), R-R2-4 (passo "Retorno" do mapa do DV2), R-R2-5 (MUDA de L1740 como CON) e R-R2-6 (resumo de D1, "estão nos lotes DV1 e DV3; este lote mantém", e o mesmo em D2) não mudam gabarito, base legal nem contagem. Ficam como errata de forma na T-147 (PRÓXIMO), aplicada na consolidação do pacote seguinte e não antes, para não alterar o SHA do objeto do gatilho A. O R-R2-6 é texto que a candidata lê e tem custo mínimo. Por isso a T-147 vem antes da fase 2 na fila da GCB. A15 (DV1: outras formas de extinção e espécies) e A16 (`comentario`, `mecanismo` e `tipo` nos itens D1/D2 dos três tópicos) seguem PRÓXIMO, na T-146 e na T-149.

**D1-7. Status pós-QA dos 60 AUTORAL.** Os 60 itens DV1-01..DV3-20 trazem hoje, no pacote, `interno: "QA PENDENTE (T-130, DA-v2 fase 1)"`. As duas QAs da R2 aprovaram os 60. A GCB fixa o status final como "QA APROVADO qa-normativo-da R2 + gcb-cqfp-didatico R2 2026-10-25 (T-130)". A GBQ grava esse status no campo `interno` na consolidação da T-131, depois do aceite do gatilho A, sem nenhuma outra mudança nos 60 itens. Até essa gravação vale a D-QA-PENDENTE: os itens não entram em simulado.

**D1-8. Itens reais intercalados.** Os 7 reais (CEBRASPE_ANALOGA, proveniência APROVADA na T-79, todos de aderência direta) conferem nas duas QAs, com gabaritos inalterados. No pacote, o `itemEdital` deles passou da folha-mãe para a folha (P1-DA-2 → 2.1: BQ-0122, 0137, 0148; P1-DA-3 → 3.4: BQ-0150; P1-DA-4 → 4.4: BQ-0127, 0132, 0145). Em banco/banco.csv eles continuam na folha-mãe. Mapeamento de item ao edital é D2, e o banco é da GBQ. Por isso emito o gatilho D, com a GBQ em cópia. O DIAG30 do template v17.1 não contém nenhum dos 7 nem id DV (conferência da produção, resposta_R1.md §7).

**D1-9. Erratas da QA12.** E1–E6 (D5 e D3) não alcançam os tópicos reescritos e seguem na T-133. A F1 (título C4.4-13 do D2) foi absorvida no pacote pela substituição do bloco 4.4 pelo DV3 (registro_alteracoes_v2.md). Na T-133 ela fica só para o arquivo-fonte do D2.

**D1-10. Lista de pares DAD.** Continua ausente do repositório (anexo do Fundador, ordem (d)). Os pares foram produzidos dos nossos lotes, dos mapas e do banco, e o didático R2 confirmou que não há material de terceiro (D-ESTRATEGIA). A conferência contra a lista fica BACKLOG até o anexo chegar (T-150, parte (d)).

**D1-11. Pontos de troca por item real.** A onda 1 da BANCO-DA (T-129) já tem 260 linhas no banco, com aceite pendente. A troca dos AUTORAL listados nos "pontos de troca" do relatorio_topicos_v1.md por itens reais vai para a T-148 (PRÓXIMO), depois do aceite da T-129 e da T-144 para os ids que ela cobre.

## 3. (a) Conteúdo final aprovado

Objeto: saida/gcb/DA_v2_fase1/pacote_v1_15_DAv2_fase1_v2_1.json (SHA-256 d741bca3bb73d60f1ed416a68b047392d924c360252a4d5ebbe97c5c8738450f) e o arquivo-fonte saida/gcb/DA_v2_fase1/v2_1_producao.md.

| Lote | Tópico | Itens AUTORAL | C / E | Caso | Mecanismos E | ITEM intercalados (reais) | Verificação conforme | QA normativo R2 | QA didático R2 |
|---|---|---|---|---|---|---|---|---|---|
| DV1 | P1-DA-2.1 (4 blocos) | 20 | 10 / 10 (LIT 8, AP 2) | 2 (10%) | CON 4, SUP 3, GEN 1, NEG 1, AUT 1 | 12 (BQ-0137, 0122, 0148) | 11 | CONFERE / doutrina declarada | APROVADO COM RESSALVAS, 0/23 |
| DV2 | P1-DA-3.4 | 20 | 9 / 11 (LIT 7, AP 2) | 2 (10%) | CON 5, SUP 3, GEN 1, NEG 1, AMB 1 | 9 (BQ-0150) | 12 | CONFERE (DV2-05 REVERIFICAR) | APROVADO COM RESSALVAS, 0/21 |
| DV3 | P1-DA-4.4 | 20 | 10 / 10 (LIT 8, AP 2) | 2 (10%) | CON 3, SUP 4, AUT 2, NEG 1 | 13 (BQ-0145, 0132, 0127) | 10 | CONFERE | APROVADO COM RESSALVAS, 0/23 |
| Total | 3 tópicos | 60 | 29 / 31 | 6 | — | 34 (7 reais) | — | 0/60 ERRO | 0/67 reprovados |

Totais por tópico no pacote (todas as origens): P1-DA-2.1 45, P1-DA-3.4 41, P1-DA-4.4 43, todos acima da meta de 20 (D-REFORCO-2). Verificadores: checa_pacote_v2_v2_1.md com 0 bloqueios e 13 avisos (D1-5); checa_estilo_v2_1.txt com 3 avisos de cota (D1-2). Itens entre 21 e 35 palavras: 100% nos três lotes. Comandos com 2–3 temas: 60 de 60 (didático R2, A5). Um VOLÁTIL: DV2-05.

## 4. (b) Divergências remanescentes

| # | Divergência | Classe | Destino |
|---|---|---|---|
| 1 | Pegadinha SUP da prioridade sem item E próprio | R (exceção D1-1) | T-145, PRÓXIMO |
| 2 | Cotas: DV2 E/CON 5; DV3 E/SUP 4, E/GEN 0 | R para esta fase (D1-2); regra geral | gatilho E; reequilíbrio na T-148 |
| 3 | 7 reais com `itemEdital` na folha no pacote e na folha-mãe no banco | D2 | gatilho D; GBQ alinha na T-131 se aceito |
| 4 | Status `interno` "QA PENDENTE" nos 60 | mecânico | GBQ na T-131, depois do gatilho A (D1-7) |
| 5 | R-R2-1 a R-R2-6 (forma) | R | T-147, PRÓXIMO |
| 6 | A15 (extinção e espécies) | R | T-146, PRÓXIMO (fase 2) |
| 7 | A16 (D1/D2 sem `comentario`, `mecanismo`, `tipo`) | R | T-149, PRÓXIMO |
| 8 | Linha 6 (ITEM a cada 2–3 quadros), aviso nos 3 lotes | formato | aceito como aviso |
| 9 | Par art. 57 × prazo do recurso; pegadinha ato × fato | R | T-147 |
| 10 | Script conta mal a verificação; contador de frases; heurística "comando entrega o par" | ferramenta | T-150, BACKLOG (GBQ) |
| 11 | Lista DAD de pares ausente | insumo do Fundador | T-150, parte (d), BACKLOG |
| 12 | DV1-01, 02, 08, 09, 10, 11 NÃO CONFERIDO pelo normativo (doutrina declarada, sem artigo) | informativo | sem ação: o QA não aponta erro; regra marcada como doutrina |

Nenhuma divergência envolve gabarito.

## 5. (c) Proveniência de normas (texto compilado do Planalto)

| Norma / dispositivos | URL | Verificado em | Situação |
|---|---|---|---|
| Lei 9.784/1999, arts. 1º a 70 (incl. 11–17, 24, 26, 30, 38, 49, 49-A a 49-G, 50, 51, 53–55, 57–63, 69, 69-A) | https://www.planalto.gov.br/ccivil_03/leis/l9784.htm | 2026-10-17 e 2026-10-20 (mapas D1/D2); reconferido em 2026-10-25 (R1, R2) | CONFERIDO; última alteração Lei 14.210/2021 |
| Lei 8.112/1990, arts. 6º–9º, 13–15, 18, 20, 21, 24–25, 27–37, 93 | https://www.planalto.gov.br/ccivil_03/leis/l8112compilado.htm | 2026-10-20; reconferido em 2026-10-25 | CONFERIDO; remissão ao Decreto 12.374 no art. 20 |
| CF, art. 5º, XII e LVI; art. 41, caput e § 4º | https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm | 2026-10-20; art. 5º reconferido em 2026-10-25 (R2) | CONFERIDO |
| Lei 4.717/1965, art. 2º | https://www.planalto.gov.br/ccivil_03/leis/l4717.htm | 2026-10-17; reconferido em 2026-10-25 (R1) | CONFERIDO |
| LINDB (DL 4.657/1942), arts. 20 e 21 | https://www.planalto.gov.br/ccivil_03/decreto-lei/del4657compilado.htm | 2026-10-17; reconferido em 2026-10-25 | CONFERIDO (Lei 13.655/2018) |
| Decreto 12.374/2025, arts. 1º, 2º e 24 | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12374.htm | arts. 2º e 24 em 2026-10-20 e 2026-10-25; art. 1º em 2026-10-25 (R2) | CONFERIDO; **REVERIFICAR 4–8/1/2027** |
| Decreto 12.967/2026, arts. 1º e 2º | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/decreto/d12967.htm | 2026-10-25 (R1, R2) | CONFERIDO; só altera o art. 9º, §§ 6º e 8º, do Decreto 12.374; **REVERIFICAR** |

Sem fonte: a gravação feita por um dos interlocutores está marcada "[SEM FONTE — não afirmar]", e a sanabilidade do vício de forma e o controle judicial do art. 53 estão marcados como doutrina com [SEM FONTE]. Nenhum espelho de terceiro foi usado. Os 7 reais têm proveniência CDN, APROVADA na T-79. O DV2-05 (Decreto 12.374) vai para a fila de janeiro (T-11) e fica inapto a simulado final até a reverificação.

## 6. (d) Itens AUTORAL

- **Aprovados (60):** DV1-01 a DV1-20, DV2-01 a DV2-20 e DV3-01 a DV3-20. Os 60 passaram pelo qa-normativo-da R2 (0 ERRO; 54 CONFERE, 6 NÃO CONFERIDO por serem doutrina declarada: DV1-01, 02, 08, 09, 10, 11) e pelo gcb-cqfp-didatico R2 (0 reprovados). VOLÁTIL: DV2-05, aprovado, mas fora de simulado final até 4–8/1/2027. Status a gravar: D1-7.
- **Reprovados:** nenhum. Na R1 foram 10 de 67, todos corrigidos na v2 e aprovados na R2, com ids e gabaritos mantidos.
- **Pendentes:** nenhum dos 60. O DV3-21 não existe ainda (T-145).
- **Intercalados:** 27 AUTORAL e 7 reais. Nenhum se repete na verificação do mesmo tópico (checa_pacote_v2 sem bloqueio).

## 7. Linha proposta para o Estado Canônico

DA-v2 fase 1 (T-130, ORDEM_DA_V2_FASE1), GCB, 25/10/2026: lotes DV1 (P1-DA-2.1, 4 blocos), DV2 (P1-DA-3.4) e DV3 (P1-DA-4.4, Lei 9.784 inteira) no formato DA-v2 com adendo v2.1. 60 AUTORAL novos (29 C / 31 E; 6 caso; DV2-05 VOLÁTIL) e 7 reais intercalados. Pacote pacote_v1_15_DAv2_fase1_v2_1.json, SHA-256 d741bca3…450f (1.493 itens sobre a v1.14 070bc237…d495). QA normativo R2: 0/60 ERRO. QA didático R2: 0/67 reprovados. checa_pacote_v2: 0 bloqueios. Reconciliado pela GCB em saida/gcb/DA_v2_fase1/RECONCILIADO.md. Gatilho A emitido, aceite pendente. Gatilho D (itemEdital dos 7 reais) e gatilho E (cota × §6.5) emitidos. Build na T-131.
