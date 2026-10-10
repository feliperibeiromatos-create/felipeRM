# T15_T22_reconciliacao_2026-10-10.md — T-15 e T-22 — 2026-10-10 — gerado por gbq-gerencia

Entrada: `saida/simulados/T15_T22_relatorio_2026-10-10.md` (gbq-csc). Decisões aplicáveis: D-SIM0-V02, D-BANCO-TI-1-4, D-SIM0-P2, D-PACOTE-6 (APLICADA 10/10). A conferência foi feita por script, somente leitura: `git show HEAD:<arquivo>` comparado com a árvore de trabalho, CSV lido com `csv.reader(delimiter=';')`, e `git diff -U0`. A GBQ não editou banco, simulado nem gabarito.

## 1. Verificação por script

### banco/banco.csv
- Cabeçalho idêntico. 67 linhas antes e depois (cabeçalho + 66). Ids e ordem iguais.
- Comparação campo a campo de HEAD com a árvore de trabalho: só mudaram 11 campos em 7 linhas.
  - `observacoes` de BQ-0015, BQ-0017 e BQ-0035 (T-15). O prefixo `VOLÁTIL (dependência de produto: …; reverificação 4–8/1/2027, T-16; inapto a simulado final até lá); ` segue o formato de BQ-0064 e o resto do texto ficou preservado.
  - `item_edital_camara` de BQ-0011, BQ-0012, BQ-0038 e BQ-0039: `P2-4.3` → `P1-4` (T-22).
  - `observacoes` desses quatro: a nota PARCIAL/gatilho D foi trocada pela nota de remapeamento por D-BANCO-TI-1-4 (T-22).
- `gabarito`, `texto_integral`, `anulado`, `rotulo` e os demais campos não mudaram em nenhuma linha. Os gabaritos dos remapeados continuam E, C, C, E.
- `edital/TI_itens_1_4_P1.md` existe, com o texto literal fixado em D-BANCO-TI-1-4 e os ids P1-1 a P1-4.3. O orquestrador o criou na aplicação da decisão.

### saida/simulados/simulado_0_v0.2.md
- 468 → 471 linhas. Retiradas as 3 linhas de marca novas, o arquivo difere de HEAD só nas linhas 1 (cabeçalho), 9 (aviso 1) e 14 (aviso 5).
- As 3 marcas `[VOLÁTIL — dependência de produto; reverificação 4–8/1/2027 (T-16); inapto a simulado final]` estão logo abaixo dos itens 18 (BQ-0015), 37 (BQ-0017) e 38 (BQ-0035). A marca já existente do item 23 (BQ-0064) ficou como estava.
- Corpo dos itens, comandos, numeração (1–60), ordem e instruções: intactos.
- Aviso 1 (`1 item VOLÁTIL` → `4 itens VOLÁTEIS`) não constava da lista literal da T-15. A GBQ aceita a mudança como consequência necessária (o aviso conta VOLÁTEIS). D1.

### saida/simulados/simulado_0_v0.2_gabarito.md
- 240 linhas antes e depois. Diferem só as linhas 1, 41, 70, 89, 90, 122, 127, 216 e 239.
- Grades de gabarito (Parte P1 e Parte P2) e tabela de contagens: inalteradas. Total segue 33 C / 27 E.
- Mapa: 60 linhas. Nas colunas nº, Cmd, BQ-id, subitem, aderência e gab nada mudou. Na coluna VOLÁTIL, só os itens 18, 37 e 38 passaram de `não` para `sim`; as observações dessas três linhas ganharam a nota T-15.
- "Marcas de montagem": 4 VOLÁTEIS. Cobertura: P1-5.3 com 2 VOLÁTEIS (itens 18 e 23) e P1-8.3 com 2 VOLÁTEIS (itens 37 e 38).
- Errata: `retirar o item 56 (BQ-0025)` → `retirar o item 49 (BQ-0025)`. Conferido: o item 49 do mapa é BQ-0025 (P2-4.1, E).
- A nota informativa de "Conferências de montagem" (linha 239) foi atualizada por coerência. A GBQ aceita (D1).

### Conferência cruzada mapa × banco (estado atual)
- Os 60 gabaritos do mapa coincidem com o banco (60/60) e somam 33 C / 27 E.
- VOLÁTIL é o mesmo conjunto no banco, no mapa e no corpo: itens {18, 23, 37, 38}.
- O subitem do edital diverge do banco em 5 itens, todos previstos e fora do objeto da T-15:
  - item 15 (BQ-0009): mapa P1-5.3, banco P1-5. Pendência da T-20.
  - itens 57–60 (BQ-0011, 0012, 0038, 0039): mapa P2-4.3/PARCIAL, banco P1-4/DIRETA. Efeito da T-22.

## 2. Vereditos

- **T-15: CONCLUÍDA.** Fez só o descrito, sem mudar item, ordem, numeração, comando, texto ou gabarito. O gabarito foi regerado e cumpre a parte "aplicar T-15 e regerar o gabarito" de D-SIM0-V02. O uso pela candidata continua condicionado à T-13 sem gatilho D e à entrega pelo Fundador.
- **T-22: CONCLUÍDA.** O remapeamento seguiu D-BANCO-TI-1-4 sem mudar gabarito. edital/TI_itens_1_4_P1.md já existia.

## 3. Decisões D1

1. **T-20 ampliada → T-25 (AGORA).** A T-20 fica substituída por uma tarefa nova, a T-25, acrescentada ao final de TAREFAS.md. A linha da T-20 não foi reescrita. Cabe ao orquestrador marcá-la "substituída por T-25" no seu controle de estados.
   - A T-25 faz numa única passagem mecânica a T-20 original e a atualização dos itens 57–60 decorrente da T-22, e no fim regera o gabarito.
   - **Classe AGORA**, e não a PRÓXIMO padrão, por três motivos:
     - o simulado e o gabarito divergem hoje do banco, que é a fonte, em 5 itens;
     - D-PACOTE-6 manda incluir o Simulado 0 v0.2 na T-12 "quando estiver pronto", e ele não está pronto enquanto diverge do banco;
     - o ajuste é mecânico e barato.
   - Ordem: a T-25 vem antes de qualquer inclusão do Simulado 0 v0.2 no pacote (T-12) e de qualquer entrega.
2. **Estrutura em Partes.** Os itens 57–60 ficam na posição atual, sob o cabeçalho "Parte P2". A regra do ajuste mecânico proíbe mudar ordem e numeração, e o simulado é agrupado por comando original (comandos 33 e 34). A divergência entre a Parte por posição e o módulo do edital fica declarada:
   - uma nota antes do Comando 33;
   - a contagem por módulo do edital nos avisos e no gabarito: P1 43 itens (23 C / 20 E); P2 17 itens (10 C / 7 E);
   - a contagem por Parte mantida: P1 39 (21/18); P2 21 (12/9).
   - Esta decisão não muda o que a Presidência aceitou em D-SIM0-V02 (60 itens, 33 C / 27 E). A leitura por módulo apenas deriva de D-BANCO-TI-1-4. Não é D2 e não gera gatilho.
3. **Contagens-alvo da T-25** (calculadas por script sobre o mapa atual com as trocas da T-20 e da T-22):
   - Aderência: 37 DIRETA / 23 PARCIAL / 0 em arbitragem.
   - Distribuição dos 23 PARCIAIS:
     - P2-4.1: 17
     - P1-8.3: 2 (37, 38)
     - P1-5.3: 1 (18)
     - P1-6: 1 (26)
     - P1-7.1: 1 (30)
     - P1-8.1: 1 (31)
   - Cobertura alterada:
     - P1-4: 4 itens (2 C / 2 E), todos DIRETOS, 0 VOLÁTIL (itens 57–60)
     - P1-5: 1 item (C), DIRETO (item 15)
     - P1-5.3: 10 itens (6 C / 4 E), 9 DIRETOS, 1 PARCIAL, 2 VOLÁTEIS
     - P1-6: 2 itens, 1 DIRETO, 1 PARCIAL
     - P1-8.1: 3 itens, 2 DIRETOS, 1 PARCIAL
     - P2-4.3: SEM ITEM
     - P2: 1 de 23 subitens com item (4.1, só PARCIAL)
   - TI 1–4: só P1-4 tem item. P1-1, P1-2, P1-2.1, P1-3, P1-4.1, P1-4.2 e P1-4.3 ficam SEM ITEM.
   - VOLÁTEIS e gabaritos inalterados: 4 VOLÁTEIS; 33 C / 27 E.
4. **Critério de aceite da T-25** (a GBQ confere por script):
   - mapa = banco em subitem para 60/60;
   - texto, BQ-id e gabarito 60/60;
   - as marcas do corpo coincidem com o mapa (PARCIAL e VOLÁTIL);
   - o diff fica restrito às linhas listadas na tarefa.
5. **D-SIM0-P2 / T-24.** Sem efeito desta reconciliação. A T-24 segue PRÓXIMO e usa só AUTORAL dos Lotes 1, 1-C, 2 e 3, nenhum dos quais é afetado pela T-22.
6. **T-16** segue PRÓXIMO (datada). O prefixo VOLÁTIL do banco já a referencia.

## 4. Tarefas novas
- T-25 (AGORA), num único append a TAREFAS.md. Substitui a T-20.

## 5. Gatilhos
- Nenhum. Não há pacote para aceite, matéria fora do domínio, conflito acima de D1, decisão D2 nem matéria do Fundador.
