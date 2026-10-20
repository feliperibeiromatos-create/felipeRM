# QA_D5_v2_1_conferencia_2026-10-20_gcb-cqfp.md — T-74 — 2026-10-20 — gerado por gcb-cqfp

Objeto: conferência dos 10 trechos da errata de forma (T74_reconciliacao_2026-10-20.md, seção 4) aplicada pelo orquestrador com saida/gcb/scripts_orq/aplicar_substituicoes.py sobre saida/gcb/D5_v2.md, que gerou saida/gcb/D5_v2_1.md. O escopo segue o R2, seção 9, fecho: a QA confere só os trechos (diff), sem nova rodada sobre os itens. Somente leitura do repositório; scripts próprios em python3 -I, no scratchpad; sem navegador; sem commit.

## 0. Veredito

**CONFERIDO.** O SHA-256 bate com o esperado pela GCB. O diff v2 → v2.1 fica só nas 10 linhas da tabela. Os trechos novos reproduzem byte a byte o texto exato do R2, seção 9, e estão corretos pela letra do Anexo N. A seção 5 (itens) está idêntica. Nada impede o gatilho A pelo lado da gcb-cqfp.

## 1. Hashes (em disco, 20/10/2026)

| Arquivo | SHA-256 | Bytes; linhas |
|---|---|---|
| saida/gcb/D5_v2_1.md | 44ddcc982642df66b246108cb7e3ef86031e8a99762aa2262a6c0bdde24e1333 (= esperado, T-74, seção 4) | 313.486; 1.747; LF, 0 CR; termina em "FIM DO LOTE D5\n" |
| saida/gcb/D5_v2.md (origem, não alterada) | 4c61c5cf0c28aae533f8dc1510493e4db633f4423daabdea1c34c0cc1ea7d409 | 313.079; 1.747 |
| saida/gcb/D5_parecer_R2_gcb-cqfp.md | d7a90354821428612626e3e89c548a5dd5284df9131012ed39607daa183becf4 | — |
| saida/gcb/D5_anexo_N_mapa_normativo.md | 497af8e63ecc78ba838927191235ebace582d69b4b482598130aa484508d76eb | — |

## 2. Diff v2 → v2.1

- `diff D5_v2.md D5_v2_1.md`: 10 hunks de uma linha (1c1 a 1743c1743), só nas linhas 1, 2, 40, 56, 171, 341, 426, 567, 1739 e 1743. Não há linha acrescentada nem removida.
- Reaplicação independente: o bloco CSV foi extraído com parser próprio (csv.reader; o arquivo tem um único bloco). Cada texto_antigo ocorre 1 vez na v2 e 1 vez na aplicação sequencial, e cada texto_novo ocorre 1 vez no resultado. O resultado é igual ao arquivo em disco, byte a byte (SHA-256 44ddcc98…1333).
- Seção 5 (itens, linhas 576 a 1583 da v2; 5.1 e 5.2): nenhuma linha alterada, **idêntica**. Da seção 6 até "FIM DO LOTE D5", mudam só as linhas 1739 e 1743 (seção 8). Nenhum item, gabarito, [TS], marca ou contagem foi tocado.

## 3. Trechos novos × texto exato do R2, seção 9

Teste: aplicar à v2 **somente os pares do R2, seção 9** (texto_antigo → texto_novo, como estão nas linhas 196 a 207 do R2) e as duas linhas de controle da ordem da T-74. O resultado é **idêntico à v2.1**, byte a byte (SHA-256 44ddcc98…1333). Logo, as substituições n. 3, 6, 8 e 9, que usam prefixo ou contexto final só para a unicidade, não alteram nada além do texto do R2.

| CSV n. | Linha | Origem no R2, seção 9 | Ocorrências do texto antigo na v2 → na v2.1; texto novo na v2.1 |
|---|---|---|---|
| 1, 2 | 1, 2 | — (ordem da T-74: linha de controle e "v2.1" no título) | 1 → 0; 1 |
| 3, 9 | 40, 1739 | n. 4 (2 ocorrências) | 2 → 0; 2 |
| 4 | 56 | n. 1 (seção 0.1, A7) | 1 → 0; 1 |
| 5 | 171 | n. 1 (C10.1-12) | 1 → 0; 1 |
| 6, 8 | 341, 567 | n. 2 (2 ocorrências) | 2 → 0; 2 |
| 7 | 426 | n. 5 (opcional) | 1 → 0; 1 |
| 10 | 1743 | n. 3 | 1 → 0; 1 |

A linha 1 mantém o formato do CLAUDE.md ("# D5_v2_1.md — T-74 — 2026-10-20 — gerado por …"). O acréscimo "; errata de forma da gcb-gerencia (T74_…)" registra a autoria da errata. O arquivo é interno, e a D-CABECALHO-NEUTRO não se aplica (T-74, seção 3).

## 4. Correção pela letra do Anexo N

- **Art. 79 (n. 4 e 5; Anexo N, l. 941–960).** O caput e os incisos I a III têm a redação original. O inciso IV foi "Incluído pela Lei nº 15.266, de 2025". O § 1º (caput) tem "Redação dada pela Lei nº 15.266, de 2025", e os seus incisos I a VI, a redação original. O § 1º, VII, e as alíneas a a f foram "Incluído[s] pela Lei nº 15.266, de 2025". O § 2º foi "Incluído pela Lei nº 15.266, de 2025". Todos esses dispositivos de 2025 estão marcados **REVERIFICAR**. O texto novo de C10.1-12 diz exatamente isso: "inciso IV, o § 1º (caput e inciso VII, com as alíneas) e o § 2º com redação dada ou incluída pela Lei 15.266/2025". A forma curta da linha A7 ("inciso IV e §§ 1º e 2º com redação de 2025") é o resumo fixado no R2. A forma precisa está em C10.1-12, e o artigo não é usado em item. Correto.
- **Art. 24 (n. 6 e 8; Anexo N, l. 383–386).** O caput diz "Desde que justificado, o orçamento estimado da contratação poderá ter caráter sigiloso". O inciso I diz "o sigilo não prevalecerá para os órgãos de controle interno e externo". O parágrafo único diz que, "na hipótese de licitação em que for adotado o critério de julgamento por maior desconto, o preço estimado ou o máximo aceitável constará do edital". Cada uma das três condutas da pegadinha nova ("Dar caráter sigiloso … sem justificativa", "opor o sigilo aos órgãos de controle interno e externo", "deixar fora do edital, na licitação por maior desconto, o preço estimado ou o máximo aceitável") contraria um desses três dispositivos, citados em "Desfeita por"/"Dispositivo", que não mudam. A frase não reproduz a sugestão B9 do leitor. Correto.
- **Art. 6º sem marca "Edital:" (n. 3 e 9).** Na coluna Observação do Anexo N, os incisos XIII (l. 116), XIV (l. 117), XV (l. 118), XVII (l. 123) e XLIII (l. 193) estão vazios, sem "Edital:". A lista nova acrescenta exatamente esses dispositivos, e as remissões conferem na v2.1: C10.1-10 tem o título "(art. 6º, XIII e XIV; arts. 33 e 34)"; C10.1-12 tem "art. 6º, XLIII"; P-17 cita art. 6º, XIII e XIV; P-22 cita art. 6º, XLIII; P-23 cita art. 6º, XV e XVII. Correto.
- **Fronteira do art. 117 e art. 7º (n. 10).** Na v2.1, o D5-58 (l. 708) é a prerrogativa de fiscalizar (art. 104, III), renumerado por troca de posição (l. 1458). O D5-60 (l. 712) é a segregação de funções (art. 7º). O art. 7º tem "Edital: núcleo 10.4; núcleo 10.6" no Anexo N. "(requisitos e segregação, D5-51, D5-52, D5-59, D5-60)" está correto.
- **Resumo 10.6 (n. 7).** O art. 117, § 2º, tem "Edital: … núcleo 10.6" no Anexo N. Na v2.1, ele está no par P-27 (l. 489) e na pegadinha G-71 (l. 570, "Dispositivo: … art. 117, § 2º"), sem item. Correto.

## 5. Observações (sem efeito)

Nenhuma ressalva nova. As pendências documentais da v2 que a T-74 resolveu (ponto 20, pela opção (i); pontos 18, 23 e 24) ficam como histórico no arquivo, como decidido na T-74, seção 2, "Efeito documental".

FIM DA CONFERÊNCIA — D5 v2.1 CONFERIDO
