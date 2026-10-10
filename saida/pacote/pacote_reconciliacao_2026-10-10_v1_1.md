# pacote_reconciliacao_2026-10-10_v1_1.md — T-27 — 2026-10-10 — gerado por gbq-gerencia

Papel: gbq-gerencia, nível D1.

Entrada:
- `saida/pacote/pacote.json` v1.1 (541533 bytes; SHA-256 d318382639ee24ec…);
- `saida/pacote/pacote_relatorio_2026-10-10.md` (gbq-csc).

Regras:
- `regras/pacote_contrato.md` v1.1, com a leitura D1 da regra 2 (sem distinção de caixa; reconciliação lote1, seção 5);
- linha T-27 e D-PACOTE-6;
- D-SIM0-V02 e D-SIM1-CANONICO;
- D-ADERENCIA e D-QA-PENDENTE;
- registro AUTORAL v3 (T-30).

Conferência por script próprio, só de leitura (scratchpad s3/gbq_rec/t27chk.py), sem reuso do gerador da produtora. Nenhum arquivo do pacote foi alterado.

## 1. Conferência (item (e) da GBQ) — 0 falhas

- Estrutura:
  - JSON relido sem erro;
  - 8 chaves de topo, na ordem do contrato, com `versao` 1;
  - só campos do contrato, e `volatil` nunca é `false`;
  - 47 entradas de edital, e todo `itemEdital` e `pegadinhas.itemEdital` existe no edital.
- Itens:
  - 240 ids, 0 duplicados;
  - todos têm id, enunciado e gabarito C/E;
  - 122 C / 118 E.
- Banco × AUTORAL:
  - Banco: 60 itens, exatamente BQ-0001 a 0066 com gabarito C/E. BQ-0067 a 0112 ficam fora até a T-42.
    - Gabarito, enunciado (= texto_integral), itemEdital, rótulo e justificativa vazia batem em 60/60.
    - Aderência pela regra 2, sem distinção de caixa, recalculada do banco atual (já com as notas da T-13/T-21): 60/60, com 23 parcial e 37 direta. O resultado mostra que as notas da reconciliação lote1 não alteraram a exportação.
    - Contagem: 33 C / 27 E.
  - AUTORAL: 180 ids, iguais aos do registro v3.
    - O gabarito bate em 180/180. Todos têm justificativa e todos são "direta". Contagem: 89 C / 91 E.
    - Por lote: L1 20, L1C 10, L2 30, L3 30, L4 20, L4C 10, L5 20, L5C 10, L6A 15, L6B 15.
    - Subitem: os 165 itens fora do 6A batem com o registro. Os 15 do 6A saem no item do edital (P1-1 e P1-3), porque o edital não tem os subitens 1.1–1.4 e 3.1–3.3 do lote. É o mesmo mapeamento da v1.
- `volatil`: 19 itens.
  - Banco, 4: BQ-0015, 0017, 0035 e 0064, iguais às marcas do banco.
  - AUTORAL, 15: iguais a VOLÁTIL + REVERIFICAR do registro v3, com L3-Q21 incluído (item 2 da T-27).
- Lotes 6: não há "Observação para a GCB-CQFP" nem "Derep, antigo DETAQ" nos lotes nem nos itens 6A/6B (item 1 da T-27, T-17).
- Discursivas: 5 (D1 a D5), como na v1.
- Simulados, contra os arquivos:
  - SIM-0 = mapa de `simulado_0_v0.2_gabarito.md`, na ordem: 60 ids, tipo diagnóstico, 33 C / 27 E.
  - SIM-1 = mapa de `simulado_1_gabarito.md`, na ordem: 40 ids, tipo final, 20 C / 20 E, 0 `volatil`, sem L4-11.
  - Os ids dos dois existem em `itens`.
  - O Simulado 2 fica fora porque o gatilho A está pendente, e o 0-P2 fica fora porque está em produção. As duas exclusões estão corretas pela regra 5.
- Ocorrências em texto exportado:
  - "QA PENDENTE": 0. "[TS]": 0. "A CONFIRMAR"/"a confirmar": 0.
  - "REVERIFICAR": 2, na justificativa do L3-Q21 e no curso do L3. São as marcas normativas do lote canônico, coerentes com `volatil`.
  - "ERRATA T-08" e "registro da GCB-CQFP": 1 cada, no curso do L3 (ponto b).

## 2. Pontos levantados

(a) L4 v3.4 (T-32): aceito.
- A mudança está na justificativa do L4-11 e na pegadinha P2 do L4. O texto trocado ("a confirmar contra o GAB_DEFINITIVO" → "gabarito definitivo E") fala do item 81 do TRF6, não do L4-11.
- O gabarito do L4-11 continua C, igual ao registro v3. Nenhum item, gabarito, [TS] ou VOLÁTIL mudou.
- É o Despacho 9, decisão da Presidência de 09/10/2026, aplicado e reconciliado pela GCB.
- O pacote lê o arquivo da tabela de fonte (regra 4).
- O canônico do Projeto no claude.ai ainda está na v3.3. O transporte já está pedido no gatilho E da GCB (T-32), e a divergência é só esse texto.
- O L4-11 não está em nenhum simulado do pacote.

(b) Rótulo interno no curso do L3: deve sair, mas não bloqueia.
- O título "CONTEXTO NORMATIVO INTERNO (ERRATA T-08, 10/10/2026; SEM ITEM)" e a nota "(registro da GCB-CQFP, 08/10/2026)" são metadado de processo num texto que vai à candidata.
- O arquivo é da GCE, então a errata é matéria fora do domínio da GBQ: vai à Presidência como GATILHO B. Pede-se a errata de forma, sem mudar conteúdo, e a reexportação na próxima regeração (T-12).
- O pacote v1.1 reproduz fielmente o canônico, como manda o contrato. Marcas de evidência no curso ([NORMATIVO — QA …], [V …]) existem desde a v1 por construção. O defeito é de forma e não viola o contrato.
- Fica em BACKLOG, sem tarefa, a hipótese de a plataforma filtrar marcas de processo. Só se a Presidência ou o Fundador quiserem.

(c) T-36 (notas de vigência do SIM-0): não bloqueia o aceite do pacote, mas condiciona a liberação.
- O pacote lista só os ids do SIM-0. O comando exportado de BQ-0040 é o literal do caderno e cita a Res. CNJ 332/2020, revogada pela 615/2025 (T-21). O contrato v1.1 não tem campo para nota.
- Decisão D1: a T-43 cria o campo opcional `nota`, retrocompatível como o `volatil`, para BQ-0040 e BQ-0003. Ela sai junto com a T-38 e a T-36, na próxima regeração.
- Liberar o SIM-0 e esses dois itens à plataforma pressupõe a T-36 e a T-43. A liberação em si é matéria do Fundador.
- O SIM-1 e os demais itens não dependem disso.

## 3. Decisão

T-27 CONCLUÍDA e reconciliada. As condições estão cumpridas:
- T-17 reconciliada pela GCB;
- T-25 reconciliada;
- T-26 e T-30 concluídas;
- T-28 incorporada;
- itens (1) a (6) da T-27 conferidos;
- contagens conferidas contra o registro v3 (180) e o banco (60).

Emite-se o GATILHO A do pacote v1.1 (aceite do pacote). Liberar o pacote à plataforma da candidata é decisão do Fundador e não faz parte do aceite.

## 4. Tarefas e gatilhos

- Tarefa nova (append único): T-43 (PRÓXIMO), campo opcional `nota` no contrato e no pacote.
- Gatilhos (append único em PARA_PRESIDENCIA.md):
  - A: pacote v1.1;
  - B: errata de forma do curso do L3 (GCE).
