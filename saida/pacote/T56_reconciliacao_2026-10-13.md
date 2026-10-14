# T56_reconciliacao_2026-10-13.md — T-56 (EXPORTAR v1.3; D-V13-AGORA) — 2026-10-13 — gerado por gbq-gerencia

REMETENTE: gbq-gerencia (opus; não produziu nem revisou o objeto)
DESTINATÁRIO: orquestrador (transcrição em TAREFAS.md e PARA_PRESIDENCIA.md), com cópia à Secretaria de Estado Canônico

## 0. Objeto, base e conferência da gerência

- **Produção** (gbq-csc, sonnet; commit 9622604):
  - `saida/pacote/pacote.json` v1.3: SHA-256 `fdcb7afdb4fb449229c6d530e877d839f8d334cd9667731e1b7222c9c7fb0eca`, 620956 bytes. Conferido com `sha256sum` em 13/10/2026: disco = commit = relatório = QA.
  - `saida/estudante/`: 43 arquivos; manifesto ordenado `6a60f28116d9ec35`.
  - `saida/pacote/pacote_relatorio_2026-10-13_v1_3.md`: `e70a1fdaec50`.
  - `saida/pacote/gerador_v1_3/`: `MANIFESTO.md` `5be4eba80547`.
- **QA:** gbq-cqe (opus; não produziu nem reconciliou). Parecer `saida/pacote/QA_T56_2026-10-13_gbq-cqe.md` (`5a50907f449d`), com veredito **APROVADO**:
  - 0 AGORA e 0 CORRIGIR;
  - O-1 e O-2 classificados BACKLOG; O-3, O-4 e O-5 DESCARTADO;
  - DÚVIDAS 14 a 16 vêm com recomendação.
- **Base de comparação:** v1.2, commit 2684ab1, SHA-256 `f46ed9f8…7304fe`, aceita pela D-PACOTE-V12 e entregue pela D-ENTREGA-V12-A.
- **Escopo:** D-V13-AGORA. Abrange `T48_reconciliacao_R2_2026-10-13.md`, seção 4, itens 1 a 5, e `T55_conferencia_2026-10-13.md`, seção 4. A T-54 fica fora (BACKLOG).
- **Conferência própria da gerência** (por script, somente leitura, sem usar o gerador da produção):
  - **Diff contra a v1.2:** fora de `nome`, `legendaMecanismo` e `avisos`, o pacote v1.3 é idêntico à v1.2 (JSON estrito).
  - **Itens:** 286, com 286 ids únicos.
    - Banco: 106 (60 C/46 E). AUTORAL: 180 (89 C/91 E). C/E total: 149/137.
    - Aderência: 247 direta, 39 parcial.
    - `volatil` 23 (banco 8, AUTORAL 15); `nota` 2; `comandoOriginal` 90.
    - 0 "QA PENDENTE".
  - **Lotes:** 10, dos quais 6 têm legenda (L4, L4C, L5, L5C, L6A, L6B). Pegadinhas: 262.
  - **Outros blocos:** 5 discursivas; 47 entradas de edital.
  - **Simulados:**
    - SIM-0: diagnóstico, 60 itens (33 C/27 E), 4 voláteis, 23 parciais, 3 avisos.
    - SIM-1 e SIM-2: finais, 40 itens cada (20/20), 0 volátil, 0 parcial.
    - SIM-0-P2: diagnóstico, 25 itens (13/12).
    - L4-11 não está em nenhum simulado.
  - **Edição:** 43 arquivos; o manifesto ordenado `6a60f28116d9ec35` confere com o do QA. Resultados das varreduras:
    - 0 "Nesta produção" e 0 "especificação previa";
    - 0 "Avisos de montagem" e 0 "D-ADERENCIA";
    - 0 fragmento dos 3 avisos;
    - "Mecanismo(s):" 1× em cada um dos 6 `L<lote>_gabarito.md` com o campo e 0 nos demais arquivos. As outras ocorrências de "Mecanismo" são conteúdo dos lotes, já presente na v1.2.
    - `git diff 2684ab1 9622604 -- saida/estudante` mostra 8 arquivos alterados.
  - **Gerador:** `gerador_v1_3/MANIFESTO.md` confere em 93/93 (SHA-256 e bytes). `gerador_v1_2` está intacto: `git diff 276dc28 9622604` vazio.
  - **Resultado:** tudo confere com o QA e com o relatório.

## 1. Decisões (D1 da GBQ)

| # | Ponto | Decisão | Classe | Destino |
|---|---|---|---|---|
| D-T56-01 | Veredito do QA (APROVADO) | Acolhido. Os itens 1 a 5 da lista da R2 (seção 4) e os pontos §4.1 a §4.5 da T-55 estão cumpridos e conferidos. A T-56 está apta, e emite-se o GATILHO A da v1.3 (seção 4). | — | seção 4 |
| D-T56-02 | DÚVIDA 14: forma de exibição da `legendaMecanismo` (linha própria, literal, sem título) | Aceita como está, porque cumpre o ponto 4 da v1.2.1 e a D-T53-01. Não se acrescenta título "Legenda" (seria texto não canônico). A extensão aos `SIM-*_gabarito.md` continua BACKLOG (D-T53-01) e passa a ser o item (7) da T-54 (seção 2). | DESCARTADO | — |
| D-T56-03 | DÚVIDA 15: aviso 1 com "D-ADERENCIA"; aviso 2 remete à marca `[ADERÊNCIA PARCIAL ...]`, que não aparece na edição | Sem ação na v1.3. No campo `avisos`, o literal fica como está (D-T53-03 e D-T53-07). Os avisos continuam não exibidos na edição até decisão do Fundador. Se o Fundador decidir exibi-los, a GBQ toma numa só D1, antes da ocorrência da T-12 que os exibir, as duas decisões abaixo. | BACKLOG (condicionado ao Fundador) | — |
| D-T56-04 | DÚVIDA 16: o padrão `D-[A-Z]{2,}` aparece sem `\b` no parecer R2 | DESCARTADO, com a errata de registro da seção 3. A varredura de fato usou `\bD-[A-Z]{2,}` e dá 0 na v1.2 e na v1.3. As 14 ocorrências sem `\b` não são id de decisão: D-DADOS ×6, D-IA ×6 e D-TO ×2 (TID-DADOS-VIZ, TID-IA, END-TO-END). | DESCARTADO | seção 3 |
| D-T56-05 | O-1: scripts "histórico" de `gerador_v1_3` (`relatorio_R1.py`, `report.py`, `report2.py`, `diff.py`, `diff2.py`) não rodam no estado da v1.3 (rc 1, sem gravar nada) | Acolhido. Na próxima ocorrência da T-12, o manifesto marca cada um como "não executável; registro da R0/R1" ou o move para `historico/`, à escolha da produção, sem alterar os scripts ativos. Não afeta o objeto. | BACKLOG → lista da próxima T-12 | seção 2, item 1 |
| D-T56-06 | O-2: os `out/*_stdout.txt` vêm de redirecionamento não descrito, e `fidelidade_stdout.txt` traz caminho absoluto | Acolhido. Na próxima T-12, a "Ordem de execução" do manifesto passa a descrever o redirecionamento de cada `*_stdout.txt`. As 2 linhas de caminho absoluto saem do conteúdo comparado por SHA-256: ou são relativizadas no script, ou o arquivo é declarado "não reprodutível byte a byte". Não afeta o objeto. | BACKLOG → lista da próxima T-12 | seção 2, item 2 |
| D-T56-07 | O-3 (rótulo da seção 11), O-4 (C-16(c) feita como regra própria nº 50) e O-5 (`⟦ ⟧` deslocados no Apêndice A; "Nada foi commitado") | DESCARTADO, confirmado como no QA. Nenhum deles afeta número, dado ou resultado da edição. | DESCARTADO | — |

Decisões que a D-T56-03 reserva, caso o Fundador mande exibir os avisos:

- (a) deleção mínima de "D-ADERENCIA: " no aviso 1 (D-T53-07);
- (b) tratamento da remissão do aviso 2. As opções são exibir a marca de aderência nos itens do `SIM-0_gabarito.md`, nunca na folha, ou fazer uma deleção literal da frase de remissão. A GBQ fixa a forma.

Decisão de fluxo: T-56 reconciliada; o GATILHO A da v1.3 é emitido. O aceite é do objeto como dado canônico e não decide entrega. A entrega à candidata (PILOT_01) da v1.3, seja na plataforma, seja na edição do estudante, continua reservada ao Fundador. A D-ENTREGA-V12-A cobriu só a v1.2. O push pelo PC do Fundador (D-V13-AGORA) é matéria dele e não depende desta reconciliação.

## 2. PARA A PRÓXIMA T-12 (próxima ocorrência; a partir de 18/10, D-MODO-TREINO)

**Base:** gerador `saida/pacote/gerador_v1_3/`, contrato v1.2.1 com as D1 da R2 (seção 2) e desta reconciliação. Produção gbq-csc; QA gbq-cqe; reconciliação GBQ.

1. **O-1 (D-T56-05):** no manifesto do gerador, marcar os scripts históricos não executáveis ou movê-los para `historico/`.
2. **O-2 (D-T56-06):** descrever o redirecionamento dos `*_stdout.txt` na "Ordem de execução" e tratar o caminho absoluto de `fidelidade_stdout.txt`.
3. **Canônico novo:** incorporar o que a ocorrência trouxer com gatilho aceito, como correções do caderno de erros, erratas, lotes ou simulados. `nome`: "Câmara 2026 — pacote F4 (v1.4)"; `versao` 1.
4. **Não regressão:** refazer as varreduras da seção 3.5 do QA R2, com `\bD-[A-Z]{2,}` (seção 3), as exceções fechadas da R1 e as conferências do QA da T-56. O diff v1.3 → v1.4 fica restrito ao item 3.
5. **Avisos do SIM-0:** só entram se o Fundador tiver decidido exibi-los. Nesse caso, a D1 da D-T56-03 vem antes do despacho.

## 3. Errata de registro (DÚVIDA 16)

No parecer `saida/pacote/QA_T48_R2_2026-10-13_gbq-cqe.md`, seção 3.5, l. 158 ("Varreduras extras"), leia-se `\bD-[A-Z]{2,}` onde está `D-[A-Z]{2,}`. O script executado (`s4/qa48_r2/r2_edicao.py`) usou o padrão com `\b`, e o resultado 0 está correto. A errata fica só neste registro: o parecer não é alterado, porque é peça de QA e o QA não é revisado pela gerência.

## 4. Estado final proposto

- **T-56: CONCLUÍDA**
  - Ciclo 2026-10-13 s5c1.
  - Produção gbq-csc (commit 9622604). QA gbq-cqe APROVADO (`QA_T56_2026-10-13_gbq-cqe.md`).
  - Reconciliada pela GBQ em `saida/pacote/T56_reconciliacao_2026-10-13.md`. GATILHO A da v1.3 emitido.
  - O-1 e O-2 vão à lista da próxima T-12.
- **T-12 (recorrente): PENDENTE.** Texto de estado proposto: "ocorrência v1.3 concluída pela T-56 (D-V13-AGORA; gatilho A 13/10/2026); próxima ocorrência (v1.4) a partir de 18/10, na cadência semanal (D-MODO-TREINO), com gerador base saida/pacote/gerador_v1_3/ e a lista PARA A PRÓXIMA T-12 de saida/pacote/T56_reconciliacao_2026-10-13.md, seção 2 (O-1, O-2, canônico novo com gatilho aceito, não regressão; avisos do SIM-0 só após decisão do Fundador)". Classe PRÓXIMO (recorrente), agentes e saída mantidos.
- **T-54 (BACKLOG): aditamento.** Acrescentar o item "(7) legendaMecanismo nos `SIM-*_gabarito.md` (legenda literal de cada lote de origem; D-T53-01, D-T56-02)". Classe e estado mantidos.

## 5. BLOCO PARA_PRESIDENCIA

GATILHO A | GBQ | Aceite do pacote.json v1.3 e da edição do estudante v1.3 como dados canônicos da v1.3, substituindo a v1.2 (D-PACOTE-V12). Objeto: T-56, ocorrência antecipada da T-12 (D-V13-AGORA). Condições: produção gbq-csc (sonnet), com conferência das contagens contra os arquivos canônicos (validate 107/0; conferências 91/0; mutação 5/5); QA independente opus que não produziu nem reconciliou (gbq-cqe, APROVADO; 0 AGORA, 0 CORRIGIR; o gerador regera pacote, edição e relatório byte a byte num clone fora do repositório); reconciliação GBQ (conferência própria por script: tudo confere). Diff v1.2 → v1.3 restrito a `nome`, `legendaMecanismo` em 6 lotes (literais canônicos) e `avisos` no SIM-0 (avisos 1, 2 e 4, literais); na edição, 8 de 43 arquivos mudaram (N-1 por deleção pura em L6B_estudo.md, legenda no topo de 6 gabaritos de lote, README). Restrições: (i) a entrega à candidata (PILOT_01) da v1.3, na plataforma e/ou na edição do estudante, é do Fundador e NÃO é decidida por este gatilho; (ii) os avisos do SIM-0 ficam no pacote como dado e NÃO são exibidos na edição até decisão do Fundador. Ressalvas: nenhuma; O-1/O-2 (forma do manifesto do gerador) vão à próxima T-12. Cópia: Secretaria de Estado Canônico | saida/pacote/pacote.json (SHA-256 fdcb7afdb4fb449229c6d530e877d839f8d334cd9667731e1b7222c9c7fb0eca, conferido com sha256sum em 13/10/2026); saida/estudante/ (43 arquivos; manifesto 6a60f28116d9ec35); saida/pacote/pacote_relatorio_2026-10-13_v1_3.md (e70a1fdaec50); saida/pacote/gerador_v1_3/ (MANIFESTO 5be4eba80547; 93/93); saida/pacote/QA_T56_2026-10-13_gbq-cqe.md; saida/pacote/T56_reconciliacao_2026-10-13.md; regras/pacote_contrato.md v1.2.1 (47e3c290646f) | itens 286 = 106 banco (60 C/46 E) + 180 AUTORAL (89 C/91 E); C/E 149/137; aderência direta 247 / parcial 39; volatil 23 (banco 8, AUTORAL 15); nota 2; comandoOriginal 90; 0 QA PENDENTE; pegadinhas 262; lotes 10 (6 com legendaMecanismo: L4, L4C, L5, L5C, L6A, L6B); simulados 4, n 60/40/40/25 (SIM-0 v0.2 diagnóstico 33 C/27 E, 23 parciais, 4 voláteis, 3 avisos; SIM-1 e SIM-2 finais 20/20, 0 volátil, 0 parcial; SIM-0-P2 diagnóstico 13/12); L4-11 fora de simulado; discursivas 5; edital 47; 620956 bytes; reprovação 0/286 | A Presidência aceita o pacote.json v1.3 (SHA-256 fdcb7afd…) e a edição do estudante v1.3 (43 arquivos; manifesto 6a60f28116d9ec35) como dados canônicos da v1.3, substituindo a v1.2, ficando a entrega à candidata (PILOT_01) — o que vai à plataforma e/ou a edição do estudante, e quando — e a exibição dos avisos do SIM-0 reservadas ao Fundador e NÃO decididas por este gatilho? SIM/NÃO

## 6. BLOCO TAREFAS

nenhuma. Os resíduos O-1 e O-2 vão à lista da próxima ocorrência da T-12 (seção 2), e a extensão da legenda entra como aditamento da T-54 (seção 4).
