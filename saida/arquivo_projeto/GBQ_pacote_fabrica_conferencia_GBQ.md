# GBQ — PRÉ-CONFERÊNCIA DO PACOTE DA FÁBRICA (v1.1, T-27) — 13/10/2026
GBQ (Opus 5.5). A GBQ não produziu o pacote: a produção é da fábrica (gbq-csc/T-27). Conferência por script, somente leitura.

## Objeto
- GBQ/pacote_v1_fabrica.json: "Câmara 2026 — pacote F4 (v1.1)", geradoEm 2026-10-10, 541.533 bytes no espelho lido.
- Conteúdo: 240 itens, 10 lotes, 5 discursivas, 2 simulados e edital com 47 entradas.

Referências:
- claude/GBQ_Registro_AUTORAL_v3.md (rev. 13/10);
- GBQ/pacote_v1_auto.json (EXEC, conferência cruzada);
- GBQ/banco.csv (112 linhas);
- linhas T-25 e T-31 do TAREFAS.md (transportadas pelo Fundador).

Esta é uma pré-conferência da GBQ. Não é o gatilho A, que sai depois da Tarefa B da GBQ-CSC-S (D-PACOTE-BASE).

## 1. Itens AUTORAL (180)
- IDs 1:1 com o Registro v3: 0 a mais, 0 a menos.
- Gabarito e subitem (com prefixo): 180/180, 0 divergência. Totais: 89 C / 91 E.
- volatil=true: exatamente os 15 inaptos da v3 (14 VOLÁTIL + L3-Q21, codificado como volatil=true e com nota "REVERIFICAR … não VOLÁTIL" na justificativa). É conservador e aceito.
- [TS]: não exportado (não há campo). Metadado interno; não bloqueia.
- Lotes 6a/6b: 30/30 com a v3 (gabarito e subitem). A A-6b-1 e a T-17 são textuais e não alteraram gabarito (R6 fechada).

## 2. Comparação com o pacote da EXEC (150 AUTORAL comuns)
- Enunciados: 149/150 idênticos. Única diferença em L1-Q04: o pacote da fábrica tem "áudio– texto", com espaço espúrio depois do travessão; a EXEC tem "áudio–texto". Defeito de forma.
- Comandos: 150/150 iguais ao comando ORIGINAL. A fábrica não normalizou os comandos com faixa de IDs, o que respeita o edital 8.2.
- Justificativas: 143/150 iguais. As 7 diferenças:
  - L4-11: atualizada para "definitivo E" (correta);
  - L3-Q21: nota REVERIFICAR;
  - L1C-Q24: a fábrica retirou a marca de verificação;
  - L1C-Q26: aspas;
  - L4-08, L4-09 e L4-13: a fábrica acrescentou marcas internas "(v3 — O12)" e "(O1)".

## 3. Itens do banco (60)
- 60 = BQ-0001 a BQ-0066, menos os 6 anulados (29, 30, 31, 60, 62, 63). Nenhum anulado no pacote. BQ-0067 a BQ-0112 (terceira varredura) ficam fora da v1.1.
- Gabarito, subitem e número: conferem com GBQ/banco.csv.
- Aderência: 37 DIRETA / 23 PARCIAL. As 23 parciais são 17 de P2-4.1, 2 de P1-8.3, 1 de P1-5.3, 1 de P1-6, 1 de P1-7.1 e 1 de P1-8.1, igual à T-25.
- VOLÁTEIS do banco: BQ-0015, 0017, 0035 e 0064.
- TRF6 70–76 = BQ-0002 a BQ-0008; 96 e 98 = BQ-0011 e BQ-0012 (P1-4, DIRETA); 63 = BQ-0001; 80 = BQ-0009; 81 = BQ-0010. Nenhum item real aparece duas vezes (R3 cumprida).
- textoBase: "nenhum" (string) em 237 itens. Forma: o esperado é campo vazio.

## 4. Simulados (pré-condição T-25/T-31: CONCLUÍDAS e reconciliadas, conforme TAREFAS.md)
SIM-0, "Simulado 0 — diagnóstico (v0.2)":
- 60 itens, todos do banco; 33 C / 27 E.
- Por prova: P1 43 / P2 17, igual à T-25.
- Itens VOLÁTEIS e PARCIAIS presentes, o que é permitido em diagnóstico.
- R2 não se aplica (L4-11 ausente).
SIM-1, "Simulado 1 — P1 final (TI e Dados, itens 5 a 8)":
- 40 itens AUTORAL; 20 C / 20 E.
- 0 VOLÁTIL, 0 PARCIAL, 0 de P1-8.3 (D-83-SIMULADO), R2 cumprida.
- Subitens: 5.1 = 8, 5.2 = 4, 5.3 = 4, 6 = 4, 7.1 = 4, 8.1 = 3, 8.2 = 7, 8.4 = 6.
- CONFORME às regras de simulado final.

## 5. Lotes e discursivas
- 10 lotes. L1C, L4C e L5C sem curso ou resumo, como no pacote da EXEC.
- L6B com a A-6b-1: "cópias" sem "[sic]", 0 "usuario", 0 "pendente (BACKLOG)".
- 5 discursivas, com quesitos (3, 3, 5, 3 e 5).
- Pegadinhas: a fábrica as AGRUPA por subitem e perde o rótulo do objeto. Exemplo, L5/P1-8.2: "tratá-lo como gráfico de barras…" sem dizer que é o histograma. A EXEC mantém uma pegadinha por linha, com rótulo. O conteúdo é o mesmo, mas a leitura isolada fica ambígua.
- Grafia: resta 1 "Derep, antigo DETAQ" no L1 (D-DEREP: "Derep (antigo DETAQ)").

## 6. Edição do estudante (não bloqueia a integridade dos dados; bloqueia a entrega à candidata)
17 justificativas têm marcas internas: CQFP, "(v3 — O12)", "(O1)", "Lição O10", "R-4C1", "Risco MÉDIO". Ocorrem em L2-Q23, L4-08, 09, 13, 15, 17, 18, 19 e 20, 4C-06, 08 e 09, entre outras.
Pela D-PILOT-MATERIAL e pela D-GPAI revista (T-12), o material vai à candidata só na edição do estudante, com a conferência de fidelidade do gbq-cqe.

## 7. Juízo da GBQ (provisório, até a Tarefa B da GBQ-CSC-S)
- Integridade de itens, banco e simulados: CONFORME. Nenhuma divergência de gabarito, subitem, volátil, aderência ou elegibilidade.
- Defeitos de FORMA, que não bloqueiam o gatilho A dos dados (classe PRÓXIMO, para a v1.2 ou a T-12):
  - F1: L1-Q04 "áudio– texto";
  - F2: textoBase "nenhum" em vez de vazio;
  - F3: pegadinhas agrupadas sem rótulo;
  - F4: 17 justificativas com marca interna;
  - F5: 1 "Derep, antigo DETAQ" no L1.
- Restrição: o pacote v1.1 não é edição do estudante.

## 8. Pontos de atenção da Presidência (D-PACOTE-QA, 12/10), conferidos pela GBQ em 13/10
1. QA PENDENTE / QA REPROVADO:
   - Nenhum item do pacote traz essas marcas. As justificativas e observações exportadas têm 0 ocorrências.
   - Nenhuma linha do GBQ/banco.csv traz "QA PENDENTE" ou "QA REPROVADO".
   - As 6 linhas com "aguarda qa-normativo (T-40); fora de simulado até a conclusão" (BQ-0072, 0077, 0084, 0109, 0110 e 0111) estão FORA do pacote, que vai só até BQ-0066.
   - Sem objeção.
2. Lote 4, "a confirmar" na O6: 0 ocorrências no pacote (lotes e itens). A L4-11 já diz "definitivo E". Nada a registrar contra a D-LOTE4-FONTE.
3. Lote 3, metadado "CONTEXTO NORMATIVO INTERNO (ERRATA T-08, 10/10/2026; SEM ITEM)" no curso: presente, 1 ocorrência. Registrado; previsto na T-44; não é objeção.
