# T74_reconciliacao_2026-10-18.md — T-74 — 2026-10-18 — gerado por gcb-gerencia

Objeto: reconciliação do Lote D5 (Licitações e contratos, Lei 14.133/2021; P1-DA, item 10). Ciclo 2026-10-18 s12c1. Rito normal (ficha, seção 9; despacho): Anexo N → D1 pré-R1 → v1 → R1 → v2 → R2 → reconciliação. A D-CEGO-2 não se aplica. Lição do D1 cumprida (ficha, critério 9): **a GCB não editou a v2 revisada no R2**; esta reconciliação não aplica errata nenhuma e não grava em nenhum arquivo do lote.

## 1. Conferência própria (script da GCB, python -I, somente leitura)
SHA-256 em disco (bruto; entre parênteses, sem CR quando o arquivo tem CR):
| Arquivo | Bytes | SHA-256 | Agente |
|---|---|---|---|
| saida/gcb/D5_anexo_N_mapa_normativo.md | 506736 (com CR) | 3eee8743c061e1401edf186e4f08a0ab908532c7322413d6b22d8795bcba27d8 (sem CR: 2cf23922…9201) | qa-normativo-da |
| saida/gcb/D5_ficha_lote.md | 20840 | 2a6af5eed8358de59ea9da4150b54c862714debe99b31b1140a3c53dbce39136 | gcb-gerencia |
| saida/gcb/D5_despacho_GCB-CPP.md | 7342 | 548d37a91c9e7ef86c03e4b4c6e6583f956f9e28bd5f3d289b0b714fcd6f7114 | gcb-gerencia |
| saida/gcb/D5_D1_pre_R1_2026-10-18.md | 3643 | b56973ff2c55ab7675ab5bc8190bf3850791d08edbbca539c7ecd00026c07bad | gcb-gerencia |
| saida/gcb/D5_v1.md | 92103 | 2c1cbd3b3d9b9ec75de826e750c018c03b6a8cab0a4337044372eaf7bec59dae | gcb-cpp (sonnet) |
| saida/gcb/D5_parecer_R1_gcb-cqfp.md | 18346 | e127374d2a3dded607764e3dd0ecd50a4a897797ae43401750c615ddab9c9aec | gcb-cqfp (opus) |
| **saida/gcb/D5_v2.md (versão final = revisada no R2)** | **99086 (LF, sem CR)** | **86b11efbb9f525be7d33537086b603a79617a3591a3f2cd4c983ea6a9625b518** | gcb-cpp (sonnet) |
| saida/gcb/D5_parecer_R2_gcb-cqfp.md | 14289 | 993ac67e967d9d33989d50263a235053927a85f7056018d02b8e073dea4a1bd7 | gcb-cqfp (opus) |
- O SHA da v2 em disco é idêntico ao registrado no R2 (86b11efb…b518). O Anexo N em disco é o citado no R1 e no R2 (3eee8743…27d8). A v1 em disco é a citada no R1 e no R2.

Contagens (parser próprio sobre 5.1 e 5.2 da v2; marcas lidas da linha "Marcas:" e conferidas com o cabeçalho de cada bloco — coerentes nos 30):
| Subitem | Itens | C | E | [TS] | Base doutrinária (teto) | REVERIFICAR | VOLÁTIL |
|---|---|---|---|---|---|---|---|
| 10.1 | 6 | 3 | 3 | 3 | 0 (1) | 0 | 0 |
| 10.2 | 5 | 3 | 2 | 3 | 0 (1) | 0 | 0 |
| 10.3 | 4 | 2 | 2 | 2 | 2 (2) | 0 | 0 |
| 10.4 | 5 | 2 | 3 | 2 | 0 (0) | 0 | 0 |
| 10.5 | 4 | 2 | 2 | 2 | 0 (0) | 0 | 0 |
| 10.6 | 3 | 2 | 1 | 1 | 0 (0) | 0 | 0 |
| 10.7 | 3 | 2 | 1 | 2 | 0 (0) | 0 | 0 |
| Total (P1-DA-10) | 30 | 16 (53%) | 14 | 15 | 2 (4) — D5-14, D5-15 | 0 | 0 |
- D5-01 a D5-30 contínuos na versão do estudante (5.1) e no gabarito comentado (5.2), nas duas versões; 30 "AUTORAL — QA PENDENTE". Pares confundíveis: 12 (os 8 obrigatórios presentes). Pegadinhas: 30. Nenhum "R$" em enunciado; nenhum "[SEM FONTE]" em item.
- Primeira linha no formato do CLAUDE.md ("# D5_v2.md — T-74 — 2026-10-18 — gerado por gcb-cpp"); última linha "FIM DO LOTE D5".
- Batem com a seção 7 da v2 e com o R2, seção 5. Critérios 2 e 3 da ficha cumpridos (6/5/4/5/4/3/3, ±0; [TS] 15; C 16 na faixa 12–18; ≥1 C e ≥1 E nos subitens com 4 ou mais; VOLÁTIL 0; REVERIFICAR 0, coerente com o Anexo N).
- Não regressão v1 → v2 (script próprio): enunciado mudou só em D5-18, D5-20, D5-30; bloco do gabarito comentado mudou só em D5-12 (linha "Mecanismo") e D5-30 (justificativa, linha 2); 26 itens idênticos; **nenhum gabarito mudou**. Fora da seção 5, o diff linha a linha só toca o cabeçalho, a seção 0, o curso (10.1.5, 10.2.4, 10.3.4, 10.4.2, 10.4.5), dois pares e a nota à GBQ, a nota de pares relacionados de 5.2, a proveniência e o bloco à GCB — tudo declarado na tabela da seção 0 da v2. Confere com o R2, seção 1.
- Reprovação: R1 0/30 = 0% (3 APROVADO COM AJUSTE); R2 0/30 = 0%, APROVADO 30/30, todos os blocos APROVADO, sem pedido de v2.1. Sem gate. Nenhum item reprovado remanescente (critério 7).
- Separação produção × QA (critério 11): gcb-cpp (sonnet) × gcb-cqfp (opus); normativo prévio pelo qa-normativo-da; a GCB só decidiu (D1 pré-R1) e reconcilia.

## 2. D1 da GCB sobre o que resta
(a) **Limites de cobertura da D1 pré-R1 (art. 29, art. 137, art. 122, art. 115 sem item): MANTIDOS** como registrados em saida/gcb/D5_D1_pre_R1_2026-10-18.md, seção 1. O R2 confirmou que a seção 0 e a seção 8 da v2 estão harmonizadas com ela. Os quatro tópicos ficam no curso; o critério 4 da ficha está cumprido com essas leituras ((a) e (b): tópico cumprido por outro artigo do mesmo tópico, D5-04 e D5-11; (c) e (d): não são cobertura mínima). Não são condição sobre o objeto.
(b) **D5-16 e D5-20: MANTIDOS** (D1 pré-R1, pontos 2 e 3; R1, seção 2, condição D5-20 × D5-27 cumprida sem repetição). Art. 75, VIII (ADI 6890): não usado em item; o curso traz a nota de efeito não conferido — cumpre o ponto 4. Nada vai ao BACKLOG sem ordem.
(c) **Duas observações de forma do R2 (seção 4): SEM ERRATA.** (i) Dois parênteses seguidos no curso 10.4.5 ("(art. 117, caput e § 1º) (Anexo N, seção 4)") — não afeta sentido nem item; (ii) a observação (iii) da seção 8 mantém "o R1 deve confirmar que são pontos pacíficos" — é registro histórico do bloco à GCB, já respondido pelo R1 (D5-14 e D5-15 aprovados) e pelo R2. Não há motivo forte: nenhuma das duas chega à candidata como erro de conteúdo, e o bloco à GCB e a seção 0 são material interno. Corrigi-las exigiria v2.1 e R2.1 (ficha, critério 9) sem ganho. Por isso também **não abro tarefa** à gcb-cpp.
(d) **Pares que não vão ao mesmo simulado** (nota da gcb-cqfp, R1, seção 4; transcrita na v2 após a tabela de pares e ao fim de 5.2): D5-21/D5-22; D5-13/D5-15; por cautela, D5-12/D5-13 e D5-09/D5-15. Não há par espelhado em sentido estrito. Encaminhado à GBQ no gatilho A.

## 3. Veredito e encaminhamento
- **Lote D5 RECONCILIADO e PRONTO para o gatilho A**, sem errata: versão final saida/gcb/D5_v2.md, **SHA-256 86b11efbb9f525be7d33537086b603a79617a3591a3f2cd4c983ea6a9625b518** (LF, 99086 bytes), idêntica à revisada no R2. Até o aceite, todo item segue "QA PENDENTE" (D-QA-PENDENTE); nada vai à plataforma nem à candidata antes da exportação da GBQ.
- Notas à GBQ (para depois do aceite): os quatro pares da seção 2 (d) não vão ao mesmo simulado; VOLÁTIL 0, nada entra na fila de janeiro por este lote; módulo m-da; Anexo R (BQ-0113, 0134, 0135, 0142) só calibragem — os itens D5 têm "difere de" onde há análogo.
- Espelho no Projeto (GCB/D5_*): a sincronizar, fora da fábrica.
- Tarefas novas: nenhuma (D-COMPLEMENTOS; observações de forma sem errata). A próxima da ordem dos lotes D é o D2 (T-75), que esta Gerência não promove.
- T-74: pode ser registrada CONCLUÍDA pelo orquestrador após o gatilho A (esta Gerência não altera a linha da T-74).

FIM DA RECONCILIAÇÃO T-74
