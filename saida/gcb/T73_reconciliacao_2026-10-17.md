# T73_reconciliacao_2026-10-17.md — T-73 — 2026-10-17 — gerado por gcb-gerencia

Objeto: reconciliação do Lote D1 (Estado, Administração Pública e ato administrativo; P1-DA, itens 1–2). Ciclo 2026-10-17 s11c4. Rito normal (ficha, seção 9; despacho, seção 2): Anexo N → v1 → R1 → v2 → R2 → reconciliação. A D-CEGO-2 não se aplica.

## 1. Conferência própria (script da GCB, Python, somente leitura salvo a errata da seção 3)
SHA-256 em disco, conferidos com os informados:
| Arquivo | SHA-256 | Agente |
|---|---|---|
| saida/gcb/D1_despacho_GCB-CPP.md | 062957c4936126fee56ccf3af77228308e90105c4ab346006b08f977bf8123ed | gcb-gerencia |
| saida/gcb/D1_ficha_lote.md | 61ebd5009ba68ae581f5f32e3526d5c3246bc53704f143bd134f7c9e9ba1489c | gcb-gerencia |
| saida/gcb/D1_anexo_N_mapa_normativo.md | 71aea65fe76ff4deb3cbf709933e1136b03e473cb3e2cacf9a5ce1db75b9a194 | qa-normativo-da |
| saida/gcb/D1_v1.md | 6e3635cdf7cfeeabe9b8932b005b254c4571b98fdf689bdb35e93618851c98fe | gcb-cpp (sonnet) |
| saida/gcb/D1_parecer_R1_gcb-cqfp.md | 945cf683939b495a540b434c9746b0a62de780dd995760026d95ece52d51bb36 | gcb-cqfp (opus) |
| saida/gcb/D1_v2.md, como revisada no R2 | 59ed8767fd23608af056678624114c00f948c85cdab1ca1d8b05cc6608107774 | gcb-cpp |
| saida/gcb/D1_parecer_R2_gcb-cqfp.md | bf781aae18601be783ffd3356706e087088b794bb13d2a85a784d39ae00b5708 | gcb-cqfp |
| **saida/gcb/D1_v2.md, após a errata da seção 3 (versão final)** | **63bd27c34baec035dd39904ef565f6b5a662c0a30886a4a3d0b13b8b702e3d56** | gcb-cpp; errata de forma gcb-gerencia |

Contagens (parser próprio sobre 5.1 e 5.2 da v2 final; marcas lidas da linha "Marcas:" e conferidas com o cabeçalho de cada bloco — coerentes nos 60):
| Escopo | Itens | C | E | [TS] | REVERIFICAR | VOLÁTIL | Base doutrinária (teto) |
|---|---|---|---|---|---|---|---|
| 1.0 | 8 | 4 | 4 | 4 | 0 | 0 | 3 (4) |
| 1.1 | 11 | 5 | 6 | 6 | 0 | 0 | 3 (3) |
| 1.2 | 11 | 6 | 5 | 5 | 0 | 0 | 3 (3) |
| 2.1 | 22 | 11 | 11 | 11 | 0 | 0 | 5 (5) |
| 2.2 | 8 | 4 | 4 | 4 | 0 | 0 | 0 (0) |
| Item 1 (P1-DA-1) | 30 | 15 (50%) | 15 | 15 | 0 | 0 | 9 |
| Item 2 (P1-DA-2) | 30 | 15 (50%) | 15 | 15 | 0 | 0 | 5 |
| Total | 60 | 30 | 30 | 30 | 0 | 0 | 14 (15) |
- D1-01 a D1-60 contínuos na versão do estudante e no gabarito comentado; todos "AUTORAL — QA PENDENTE". Primeira linha no formato do CLAUDE.md; última linha "FIM DO LOTE D1".
- Batem com a seção 7 da v2 e com o R2, seção 4. Critérios 2 e 3 da ficha cumpridos (8/11/11/22/8, ±0; [TS] 15/15; C 15/15; VOLÁTIL 0; REVERIFICAR 0, coerente com o Anexo N).
- Não regressão v1 → v2 (script próprio): enunciado mudou em D1-11, 13, 18, 21, 29, 30, 35, 52; comentário mudou em D1-05, 09, 11, 18, 24, 29, 30, 35, 39, 49, 52; 47 itens idênticos; gabarito mudou só no D1-52 (C → E, declarado no ponto 12). Confere com o R2, seção 1.
- Reprovação: R1 2/60 = 3,3%; R2 0/60 = 0%. Sem gate. Nenhum item reprovado remanescente (critério 7).
- Separação produção × QA (critério 9): gcb-cpp (sonnet) × gcb-cqfp (opus); normativo pelo qa-normativo-da.

## 2. D1 da GCB sobre os pendentes (a)–(d)
(a) **Outorga × delegação (1.2): cobertura parcial ACEITA.** A ficha, seção 6, proíbe ponto controverso; a extensão da titularidade transferida na outorga e as definições de delegação variam entre autores (curso 1.2.5 e R1, seção 3, concordam). O tópico "descentralização" tem item de letra de lei (D1-27, DL 200, art. 10, § 1º, b e c, inclusive o plano "órbita privada, mediante contratos ou concessões") e o curso registra que o lote não cobra a dicotomia. Não se abre vaga: o teto de 1.2 está em 3/3 e não há ângulo pacífico que justifique revê-lo. Fica dispensada, para este lote, a parte "(por outorga e por delegação)" da cobertura mínima de 1.2.
(b) **Espécies de extinção (2.1): cobertura atual ACEITA** (anulação e revogação: D1-18, 48, 49, 51; convalidação como contraponto: art. 55). Cassação, caducidade e contraposição ficam sem item: caducidade e contraposição têm terminologia instável (R1, resposta 7); a cassação é estável, mas a vaga doutrinária de 2.1 foi usada, por recomendação da QA, para motivo × motivação (par obrigatório que não tinha item), e isso tem precedência. A cassação também NÃO está no curso: a frase "cassação no curso" da seção 0 da v2 era inexata e foi corrigida por errata (seção 3). Não abro nova rodada para incluí-la no curso: o tema não é exigido em item, o curso não afirma nada errado por omissão e a D-COMPLEMENTOS veda complemento sem ordem.
(c) **D1-24 (definição legal de SEM): CONFIRMADO.** A condição da ficha, seção 3.2, está cumprida: o Anexo N transcreve as duas redações (seções 4, 6.7 e 6.8). O gabarito E se apoia em "sob a forma de sociedade anônima", comum ao DL 200, art. 5º, III, e à Lei 13.303, art. 4º; a justificativa atribui a liberdade de forma só à EP do DL 200, art. 5º, II, e não decide qual redação prevalece. A gcb-cqfp não se opõe (R2, seção 5, c).
(d) **Motivos determinantes sem item: lacuna ACEITA; teto 5/5 de 2.1 MANTIDO.** Fundamentos: (i) o ponto pacífico do tema (validade condicionada à existência e veracidade dos motivos indicados) é o próprio ponto de julgamento do BQ-0137, que está no Anexo R, apto, com gabarito definitivo, e que a candidata treina pelo banco; um item AUTORAL com ângulo "realmente novo" exigiria desdobramento doutrinário menos pacífico, o que a seção 6 da ficha veda; (ii) a v1 tentou e foi reprovada justamente por isso (R1, D1-52); (iii) a vaga foi para motivo × motivação, par obrigatório da ficha, seção 2, que não tinha item; (iv) o curso 2.1.6 e o resumo do item 2 trazem a teoria como contexto. A cobertura mínima de 2.1 fica cumprida, para este lote, por "motivação (D1-52 e itens do art. 50) + motivos determinantes pelo BQ-0137 e pelo curso". Rever o teto exigiria v3 e R3, sem ganho que compense, contra a meta de 25/10/2026.
Critério 4 da ficha: cumprido com as dispensas (a) e (d) desta D1; pares 11 + 11 com os 12 obrigatórios; pegadinhas 26 consolidadas com base (R2).

## 3. Errata documental (R2, seção 3) — aplicada pela GCB na seção 0 da v2; só forma
- Ponto 17 (linha 27): a frase "Registrei também, em seção própria, que o R1 achou tamanhos de página diferentes…" foi substituída por nota "[ERRATA GCB, T-73, 17/10/2026: …]" que diz não haver seção própria e remete a esta reconciliação. Registro: o R1 (seção 1) achou o tamanho da página da LINDB compilada em 47.412 bytes (Anexo N: 48.971) e o da Lei 4.717 em 35.908 bytes (Anexo N: 34.349), com o texto dos dispositivos usados idêntico ao do Anexo N; o Anexo N não foi alterado e a diferença não afeta item.
- Ponto 19 (ii) (linha 29): "cassação no curso, sem item" → "cassação sem item e fora do curso [ERRATA GCB, T-73, 17/10/2026: …]". O pendente (b) da linha 34 não continha a palavra "cassação" e ficou como estava.
- Prova de que é só forma: diff entre a v2 revisada no R2 (59ed8767…) e a final (63bd27c3…) = 2 linhas alteradas (27 e 29), ambas na seção 0; linhas 38 até o fim (seções 1 a 8 e "FIM DO LOTE D1") com SHA-256 idêntico antes e depois (98ee9da3…1298); o script de itens dá 60/60 enunciados e comentários idênticos e nenhum gabarito alterado. Não há nova rodada.

## 4. Veredito e encaminhamento
- **Lote D1 RECONCILIADO e PRONTO para o gatilho A** (versão final saida/gcb/D1_v2.md, SHA-256 63bd27c3…3d56). Até o aceite, todo item segue "QA PENDENTE" (D-QA-PENDENTE); nada vai à plataforma nem à candidata antes da exportação da GBQ.
- Notas à GBQ (para depois do aceite): não pôr no mesmo simulado os pares espelhados D1-55/D1-56 e D1-57/D1-58 (v2, ponto 20); VOLÁTIL 0, nada entra na fila de janeiro por este lote; módulo m-da.
- Espelho no Projeto (GCB/D1_*): a sincronizar, fora da fábrica.
- Tarefas novas: nenhuma (as dispensas (a), (b) e (d) não geram complemento; D-COMPLEMENTOS).
- T-73: pode ser registrada CONCLUÍDA pelo orquestrador após o gatilho A (esta Gerência não altera a linha da T-73).

FIM DA RECONCILIAÇÃO T-73
