# T79_reconciliacao_2026-10-17.md — T-79 (varredura P1-DA, BQ-0113 a BQ-0152: reconciliação e D1) — 2026-10-17 — gerado por gbq-gerencia

Bases lidas:
- a linha T-79 de TAREFAS.md;
- saida/banco/varredura_2026-10-17.md (gbq-cfp, produção);
- saida/banco/QA_T79_2026-10-17_gbq-cqe.md (proveniência e aderência);
- saida/banco/QA_T79_normativo_2026-10-17_qa-normativo-da.md (texto vigente);
- banco/SCHEMA.md e edital/DA_itens_1_12_P1.md;
- em DECISOES.md: D-ADERENCIA, D-QA-PENDENTE, D-MC, D-ESCOPO-3, D-DA-BANCO e D-FUNDADOR-AGORA-2;
- os precedentes R-03 (saida/banco/R03_reconciliacao_2026-10-09.md) e T-40 (saida/banco/GBQ_reconciliacao_2026-10-13.md, seção 5).

A gbq-gerencia não produz nem revisa. Aqui ela decide o D1 e aplica só alterações mecânicas em observacoes, mais a coluna aderencia de uma linha (BQ-0114), como manda o SCHEMA.

## 1. Situação dos QAs
- **gbq-cqe:** 40 de 40 verificadas, 0% reprovado (abaixo do gate de 30%). Foram 37 APROVADAS e 3 AJUSTES mecânicos não bloqueantes (BQ-0131, 0133 e 0145), sem nenhuma CORREÇÃO. Os gabaritos ficaram em 27 C, 11 E e 2 X, e 40 de 40 conferem visualmente com o GAB_DEFINITIVO_. Todos os 40 itens são CEBRASPE_ANALOGA: nenhum vem de cd_25_ns ou cd_26_*, o que está de acordo com a D-ROTULOS. Não há duplicidade.
- **qa-normativo-da:** dos 29 itens normativos, 27 CONFEREM. BQ-0151 diverge e BQ-0141 fica para reverificação. Outros 11 itens ficam fora do QA normativo: 9 de doutrina ou jurisprudência e 2 anulados.

## 2. D1 — aderência da BQ-0114 (D-ADERENCIA)
**Decisão: DIRETA, P1-DA-3.** A coluna aderencia passa de "parcial" para "direta", e o motivo fica registrado em observacoes, como exige o SCHEMA. Fundamentos:
- O item 3 do edital tem como título "Agentes públicos". O subitem 3.2, "Cargo, emprego e função pública", cobre justamente quem exerce função pública sem ocupar cargo nem emprego, que é o caso do jurado como agente honorífico ou particular em colaboração.
- A classificação dos agentes públicos é o núcleo do título 3 e não depende de o subitem enumerar as espécies.
- Há precedente de aderência direta pelo caput: BQ-0072 e BQ-0111 (D1 da T-40) e os itens P1-DA-7 desta varredura, mapeados ao caput.
- A leitura parcial da produtora fica registrada e não é acolhida.

Com isso, a aderência fica em 40 de 40 diretas.

Tipologia do guia: nenhuma alteração do regras/estilo_banca.md decorre desta varredura. Nenhum padrão novo foi proposto, então a regra "menos de 3 itens = removido ou indício" não se aplica aqui.

## 3. D1 — ajustes mecânicos (só em observacoes; nenhum gabarito, texto, comando ou mapeamento muda)
- **A1 (BQ-0131 e BQ-0133): ACEITO**, com o texto sugerido pela gbq-cqe acrescentado ao fim de observacoes, como no precedente R03 (BQ-0060, 0062 e 0063).
  - BQ-0131: gabarito preliminar C anulado, mais a justificativa Cebraspe ("princípios implícitos da administração", sem indicação do dispositivo legal).
  - BQ-0133: gabarito preliminar E anulado, mais a justificativa Cebraspe (generalização da redação).
- **A2 (BQ-0145): ACEITO.** Foi acrescentado: "grafia '9.784/1992' literal do caderno [sic]; a norma é a Lei 9.784/1999". O texto_comando continua literal.
- **Cosmético (URL TRF6_24 × trf6_24):** sem ação.

## 4. D1 — retirada de "QA PENDENTE" (D-QA-PENDENTE; precedentes R-03 e T-40)
Em cada linha, o trecho "QA PENDENTE (…)" foi substituído no mesmo lugar. O resto de observacoes não muda.
- **27 normativos com CONFERE** (BQ-0113, 0115, 0117 a 0120, 0122 a 0129, 0132, 0134, 0135, 0140, 0142 a 0147, 0149, 0150 e 0152) recebem: "QA T-79 concluído: proveniência APROVADA (gbq-cqe, 17/10/2026); qa-normativo-da T-79: <norma, dispositivo>, sustenta <C|E> (verificado em 17/10/2026, planalto.gov.br)". As ressalvas do qa-normativo-da que não invertem o gabarito vão entre parênteses: BQ-0120, 0122, 0124, 0125, 0128 e 0142.
- **9 de doutrina ou jurisprudência** (BQ-0114, 0116, 0121, 0130, 0136, 0137, 0138, 0139 e 0148) recebem: "QA T-79 concluído: proveniência APROVADA (gbq-cqe, 17/10/2026); fora do QA normativo (doutrina/jurisprudência; qa-normativo-da T-79)". A BQ-0139 também registra que o art. 37, § 6º, da CF foi conferido e é compatível com o item.
- **2 anulados** (BQ-0131 e BQ-0133) recebem: "QA T-79 concluído: proveniência APROVADA (gbq-cqe, 17/10/2026); anulado, fora do QA normativo (qa-normativo-da T-79)", mais o A1. Continuam excluídos de simulado porque o gabarito é X.
- **Mantidos com "QA PENDENTE"**, e com o motivo reescrito no parêntese:
  - BQ-0151 (DIVERGE): o art. 14 do Decreto 9.203/2017 foi revogado pelo Decreto 9.901/2019, e o decreto fala em "programa", e não em "políticas", de integridade.
  - BQ-0141 (REVERIFICAR): o art. 12, § 1º, da Lei 8.429/1992 está com a eficácia suspensa na ADI 7236, e o julgamento de 24/6/2026 não tem resultado final com fonte.

  As duas linhas ficam fora de qualquer simulado, e cada uma tem um GATILHO D próprio em PARA_PRESIDENCIA.md.
- **VOLÁTIL:** nenhuma das 40 linhas depende de produto, então nenhuma é marcada.

## 5. Contagens finais e aptidão
- banco.csv tem 152 registros mais o cabeçalho, com 18 colunas em todas as linhas e ids únicos.
- O CSV foi conferido por script:
  - o cabeçalho e as linhas 1–112 são idênticos ao estado anterior e ao git HEAD, com fim de linha normalizado;
  - só as linhas BQ-0113 a 0152 foram alteradas, e nelas só as colunas observacoes (40) e aderencia (1, BQ-0114);
  - o CRLF continua uniforme.
- **Linhas da T-79:**
  - 38 saíram de "QA PENDENTE" e 2 continuam com ele (BQ-0141 e BQ-0151).
  - Em todo o banco, só essas 2 linhas têm "QA PENDENTE".
- **Aptas a simulado (C/E, sem QA PENDENTE, sem VOLÁTIL): 36, todas de aderência direta.**
  - São 26 C e 10 E. O desequilíbrio C/E deve ser compensado na montagem.
  - Por item do edital:

    | Item | DA-1 | DA-2 | DA-3 | DA-4 | DA-5 | DA-6 | DA-7 | DA-8 | DA-9 | DA-10 | DA-11 | DA-12 |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|
    | Aptas | 4 | 3 | 5 | 4 | 3 | 1 | 2 | 1 | 1 | 4 | 4 | 4 |
- **Lacunas** (confirmadas a partir da varredura): 3.1, 4.1, 4.3, 6.1 a 6.3, 8.1 a 8.4, 9.1 a 9.3 e 10.2 a 10.5. Também há reforço necessário de itens E e de DA-6 a DA-9. Esses pontos foram para a T-86.
- **Deduplicação P9 × BQ:** não houve. O cruzamento da gbq-cqe com BQ-0001 a 0112 não encontrou duplicidade. A BQ-0146, que aparece no caderno FUB CB3 #25 e de novo no CB4 #17, está registrada uma única vez. O banco é a fonte.
- **Pacote:** sem gatilho A agora. As 38 linhas aptas entram no pacote na próxima T-12, com a gbq-csc conferindo as contagens contra os arquivos canônicos.

## 6. Tarefas novas (TAREFAS.md, PRÓXIMO)
- **T-86:** varredura P1-DA das lacunas.
- **T-87:** reverificação da BQ-0141 (resultado das ADIs 7156/7236) e cumprimento das decisões dos dois gatilhos D. O prazo máximo é a janela de 4–8/1/2027.
- **T-88:** inclusão dos 27 normativos da T-79 na reverificação de janeiro. Complementa a T-51 sem alterá-la.

## 7. Gatilhos gravados (PARA_PRESIDENCIA.md, acrescentados ao fim)
- GATILHO D | GBQ | BQ-0151 (DIVERGE). A recomendação é SIM: manter o gabarito oficial C e excluir o item de vez de qualquer simulado.
- GATILHO D | GBQ | BQ-0141 (REVERIFICAR). A recomendação é SIM: manter "QA PENDENTE" e o item fora de simulado até haver fonte oficial do STF, pela T-87.

Estado da T-79: reconciliada pela GBQ. A linha da T-79 em TAREFAS.md não foi alterada por esta Gerência.

## Adendo — ciclo 2026-10-17 s11c4 (gbq-gerencia)
- **D-BQ0151-DIVERGE cumprida.** Em banco/banco.csv, linha BQ-0151, coluna observacoes, o trecho "QA PENDENTE (qa-normativo-da T-79: DIVERGE; … ciclo s11c3)" foi substituído no mesmo lugar por "DIVERGE do texto vigente do Decreto 9.203/2017 (art. 14 revogado pelo Decreto 9.901/2019); inapto a qualquer simulado". O resto da célula foi mantido. Gabarito C, texto, comando, rótulo, mapeamento e aderência ficaram inalterados.
- **Conferência por script:** comparação com o git HEAD, ignorando CR. Só uma célula mudou (BQ-0151/observacoes). O CSV continua válido: 18 colunas em todas as linhas, 152 registros e CRLF preservado.
- **Regra para a próxima T-12 (pacote):** BQ-0151 (D-BQ0151-DIVERGE, item 4) e BQ-0141 (D-BQ0141-REVERIFICAR, QA PENDENTE) ficam fora de pacote.json, de pacote_estudante.json e da edição do estudante. A BQ-0151 só volta a ser considerada por decisão D1 da GBQ sobre a forma de exibição, com QA da gbq-cqe. A BQ-0141 só volta depois da T-87. Nenhuma das duas entra em simulado. A BQ-0151 está inapta em caráter permanente, a qualquer simulado.
