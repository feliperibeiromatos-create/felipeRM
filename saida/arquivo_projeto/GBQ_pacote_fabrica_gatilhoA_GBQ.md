# GBQ — GATILHO A do pacote.json v1.1 da fábrica (D-PACOTE-BASE, D-PACOTE-QA) — 13/10/2026
GBQ (Opus 5.5).

## Objeto
GBQ/pacote_v1_fabrica.json: "Câmara 2026 — pacote F4 (v1.1)", T-27, geradoEm 2026-10-10, 541.533 bytes no espelho lido em 13/10.
Conteúdo: 240 itens (180 AUTORAL + 60 CEBRASPE_ANALOGA), 10 lotes, 5 discursivas, SIM-0 (diagnóstico) e SIM-1 (final, P1 5–8).
Qualquer alteração no arquivo depois deste gatilho exige nova conferência.

## Base
1. Pré-conferência da GBQ (Opus): GBQ/pacote_fabrica_conferencia_GBQ.md.
2. QA independente, Tarefa B da GBQ-CSC-S (Sonnet): GBQ/CSC-S_Conferencia_pacote_fabrica_v1.md. Parecer: SEM OBJEÇÃO.
3. As duas conferências coincidem. Não há divergência de ID, gabarito, subitem, volátil, aderência ou composição.

## Resultado
- AUTORAL × Registro v3: 180/180 em ID, gabarito e subitem; 89 C / 91 E; volatil=true nos 15 inaptos.
- Lotes 6a/6b: 30/30.
- Banco: 60 itens = BQ-0001 a BQ-0066 sem os 6 anulados.
  - Contra o banco.csv: 0 divergência, inclusive no enunciado.
  - Contra o gabarito definitivo oficial (CSC-S, independente do banco.csv): 66/66.
  - Aderência: 37 DIRETA / 23 PARCIAL.
  - Nenhum item com "QA PENDENTE" ou "QA REPROVADO". R3 cumprida.
- SIM-0: CONFORME (diagnóstico; 33 C / 27 E; P1 43 / P2 17).
- SIM-1: CONFORME às regras de simulado final (0 VOLÁTIL, 0 PARCIAL, 0 P1-8.3, R2; 20 C / 20 E).
- Pontos da Presidência:
  - Lote 4 sem "a confirmar";
  - Lote 3 com o metadado ERRATA T-08 (registrado; previsto na T-44);
  - nenhum item QA PENDENTE ou REPROVADO.

## Decisões da GBQ (D1)
- D1-a: TRF6 96 e 98 (BQ-0011 e BQ-0012) = DIRETA ao P1-4 (Registro v3, rev. 13/10). A redação "parciais" da CIÊNCIA da GBQ de 12/10 fica SUPERADA.
- D1-b: no banco, a ausência de declaração de aderência vale DIRETA (26 itens). PRÓXIMO: a fábrica torna a aderência explícita em todas as linhas do banco.csv.
- D1-c: os comandos com faixa de numeração ("julgue os itens de 1 a 6") devem ser normalizados para "julgue os itens a seguir.", com o original em campo próprio (comandoOriginal), como a EXEC fez. A fábrica não adotou essa forma na v1.1, embora a D-PACOTE-BASE o previsse.
  - No SIM-1, 26 itens estão em grupos parciais.
  - CONDIÇÃO: o SIM-1 não é aplicado pela plataforma antes dessa normalização. A folha simulado_1.md (T-31) tem numeração própria.
  - Classe: PRÓXIMO, com a v1.2.

## Restrições do gatilho
- O gatilho certifica a integridade dos DADOS (itens, gabaritos, banco, composição dos simulados). Não certifica a fidelidade textual de curso, pegadinhas e discursivas contra os arquivos canônicos, que fica com a edição do estudante (T-12, gbq-cqe).
- O pacote NÃO é edição do estudante: há marcas internas em 17 justificativas. A entrega à candidata é matéria do Fundador (D-PILOT-MATERIAL, D-PILOT-PROTOTIPO0) e depende da T-12.

## Pendências classificadas
- PRÓXIMO (fábrica, v1.2 ou T-12):
  - F1: L1-Q04 "áudio– texto";
  - F2: textoBase "nenhum" em vez de vazio;
  - F3: pegadinhas agrupadas sem rótulo do objeto;
  - F4: 17 justificativas com marcas internas;
  - F5: "Derep, antigo DETAQ" no L1;
  - D1-b;
  - D1-c;
  - simulados com N e versão declarados no JSON.
- BACKLOG:
  - texto do enunciado × caderno oficial dos 60 itens do banco;
  - campo [TS] no JSON;
  - GBQ-CSC-BQ restrito a texto.
- PRÓXIMO: GBQ-CSC-RES, com o mesmo gatilho.
