# QA_v2_1_D2_D4_conferencia_2026-10-20_gcb-cqfp.md — T-75/T-76/T-77 — 2026-10-20 — gerado por gcb-cqfp

Objeto: conferência das versões finais v2.1 dos Lotes D2, D3 e D4. O orquestrador as gerou com saida/gcb/scripts_orq/aplicar_substituicoes.py (SHA-256 b803f3a5…464e, o mesmo registrado na T-75, seção 1.1) a partir do bloco CSV de cada reconciliação: T75_reconciliacao_2026-10-20.md (seção 4), T76_reconciliacao_2026-10-20.md (seção 3) e T77_reconciliacao_2026-10-20.md (seção 4). O escopo segue o fecho de cada R2: a QA confere só os trechos (diff), sem nova rodada sobre os itens. Somente leitura do repositório. Scripts próprios em python3 -I, no scratchpad (qa21: conf.py, conf2.py, pts.py). Sem navegador e sem commit.

## 0. Veredito

| Lote | Veredito | SHA-256 da v2.1 (= esperado) | Substituições | Linhas alteradas |
|---|---|---|---|---|
| D2 | **CONFERIDO** | 59cffaa689ea869cd11c13e6a833470b0b91d24b0f25ea2cc2e100ac9be8bd2c | 29 | 28 |
| D3 | **CONFERIDO** | 0f7a8b090fe6f2243ae55b36273dacdb719aaf04b19548dce70aad4867798930 | 8 | 8 |
| D4 | **CONFERIDO** | c1a7a93598e9fd37b2009b9feaca3afd3898fa05f6f66e6de26dd40c2839e5d9 | 3 | 3 |

Nos três lotes, o diff v2 → v2.1 fica só nas linhas da tabela. Os trechos novos reproduzem byte a byte o texto exato fixado nos R2. O que a GCB acrescentou (linhas 1 e 2) está correto. Nenhum gabarito, [TS], marca, posição ou contagem mudou. Pelo lado da gcb-cqfp, nada impede o gatilho A dos três lotes. Não há texto a corrigir.

## 1. Hashes (em disco, 20/10/2026)

| Arquivo | SHA-256 | Bytes; linhas |
|---|---|---|
| D2_v2_1.md | 59cffaa689ea869cd11c13e6a833470b0b91d24b0f25ea2cc2e100ac9be8bd2c (= T-75, seção 4) | 468.448; 2.386; LF, 0 CR; última linha "FIM DO LOTE D2" |
| D2_v2.md (origem, não alterada) | 50c213af26ac25cc217bc768a45cfa75f1d65778aadca155022a94e6d279cde7 | 467.513; 2.386 |
| D3_v2_1.md | 0f7a8b090fe6f2243ae55b36273dacdb719aaf04b19548dce70aad4867798930 (= T-76, seção 3) | 307.970; 1.959; LF, 0 CR; última linha "FIM DO LOTE D3" |
| D3_v2.md (origem, não alterada) | 9248c4a052aa3961d39aa910aa0de7a5a12d072946114a2ea2f4873e014a6bc5 | 307.578; 1.959 |
| D4_v2_1.md | c1a7a93598e9fd37b2009b9feaca3afd3898fa05f6f66e6de26dd40c2839e5d9 (= T-77, seção 4) | 313.968; 2.120; LF, 0 CR; última linha "FIM DO LOTE D4" |
| D4_v2.md (origem, não alterada) | 71c55229fdf1fbcc5b188d1364fc99276cc9bd2a4ed07fb83ba476a698bd3eed | 313.793; 2.120 |
| T75 / T76 / T77_reconciliacao_2026-10-20.md | 08f80318…6ad3 / 160995d6…0e36 / 1396b5bf…1fdb | — |
| D2 / D3 / D4_parecer_R2_gcb-cqfp.md | e0306fe0…ddb8 / 3c0adae8…f572 / aa455795…32cc | — |
| D2 / D3 / D4_anexo_N_mapa_normativo.md | b0a54fff…340a / 2ef58f9b…f1df / 0d98c249…a05f | — |

Os tamanhos e as contagens de linhas são os que as reconciliações previram.

## 2. Método (igual para os três lotes)

1. **Reaplicação independente.** Extraí o bloco CSV com parser próprio (csv.reader; cada arquivo tem um único bloco) e o reapliquei à v2. Cada texto_antigo ocorre 1 vez na v2 e 1 vez na aplicação sequencial. O resultado é igual ao arquivo em disco, byte a byte, nos três lotes.
2. **Diff por linha** (difflib, sem autojunk). Só hunks de substituição; nenhuma linha acrescentada ou removida.
3. **Teste contra o R2.** Apliquei à v2 **só os pares do R2** (trecho atual → texto novo, extraídos do próprio parecer) e as linhas de controle 1 e 2 tomadas da v2.1. O resultado é idêntico à v2.1 nos três lotes. Assim, nenhuma substituição muda algo além do texto do R2 e das linhas de controle. Cada par do R2 coincide exatamente, nos dois campos, com uma linha do CSV.
4. **Itens.** Fiz o parse das seções 5.1 e 5.2 da v2 e da v2.1 e comparei campo a campo: enunciado, cabeçalho (com [TS] e marcas), Folha, Ponto, Formato, Gabarito, Justificativas, Base, Mecanismo, Troca, Alteração e Marcas. Comparei também a ordem de apresentação e as sequências de gabarito e de [TS].

## 3. D2 (T-75; 29 substituições)

- **Diff.** 23 hunks em 28 linhas: 1, 2, 32, 116, 117, 122, 140, 222, 245, 317, 393, 410, 415, 418 (n. 14 e 15), 452, 724, 730, 911, 917, 918, 976, 977, 979, 980, 982, 986, 1.318 e 2.266. É exatamente a lista da T-75, seção 4.
- **Trechos novos × R2 ("Ajustes residuais (texto exato)").** Os 27 pares do R2 estão no CSV sem alteração: ajuste 1 → n. 17; 2 → 10; 3 → 11; 4 → 14; 5 → 8; 6 → 9; 7 → 16; 8a–8l → 13, 21, 12, 20, 19, 22, 23, 24, 25, 26, 18 e 27; 9a/9b → 7 e 15; 10a–10c → 4, 5 e 6; 11 → 3; 12a/12b → 28 e 29. Na v2.1, cada texto antigo ocorre 0 vez e cada texto novo ocorre 1 vez. As exceções são previstas: os textos novos de 8c e 8d são iguais (n. 12 e 20) e ocorrem 2 vezes, como o R2 anunciou.
- **Acréscimo da GCB (n. 1 e 2).** A linha 1 passou a "# D2_v2_1.md — T-75 — 2026-10-20 — gerado por gcb-cpp; errata de forma da gcb-gerencia (T75_reconciliacao_2026-10-20.md)", no formato do CLAUDE.md e no mesmo padrão do D5 v2.1 (T-74). A linha 2 passou a "… — v2.1 — 2026-10-20". O "\n" no texto antigo do n. 1 serve só para unicidade: a citação da linha 1 da v2 na seção 0 (linha 25, ponto 12) continua intacta. Correto. Não há conteúdo normativo acrescentado pela GCB.
- **Letra do Anexo N (os textos são da QA; conferi de novo na v2.1).** As fontes, por linha do Anexo N:
  - Lei 9.784: art. 49-A, caput, "No âmbito da Administração Pública federal" (l. 1507), e § 6º, III, "autoridades de Poderes distintos" (l. 1518); art. 63, § 1º, "sendo-lhe devolvido o prazo para recurso" (l. 1588).
  - Decreto 10.835: art. 19 (l. 1712).
  - Lei 8.112: art. 76-A, I a IV (l. 640–643: "regularmente instituído…", "quando tais atividades não estiverem incluídas entre as suas atribuições permanentes", "ou supervisionar essas atividades"); art. 207, caput, "120 (cento e vinte) dias consecutivos" e "Vide Decreto nº 6.690, de 2008" (l. 1178); art. 98, §§ 1º a 3º (l. 776–778); art. 111 (l. 834); art. 136 (l. 952, casos dos incisos IV, VIII, X e XI do art. 132); art. 142, § 2º (l. 972); art. 150, parágrafo único, e art. 156, caput (l. 1002 e 1016); art. 156, § 2º (l. 1018); art. 167, § 2º, "pena mais grave" (l. 1048).
  - CF: art. 39, § 3º, enumeração "IV, VII, … XXII e XXX" (l. 243).
  - Lei 6.999: art. 8º (l. 1827).

  Todos os textos novos conferem com a letra, e o "Dispositivo" de cada pegadinha não mudou.
- **Itens.** 80 ids, a mesma ordem em 5.1 e 5.2, idêntica à da v2. O único campo de item alterado é o "Ponto de julgamento" do D2-13 (ajuste opcional 12a, linha 1.318). O cabeçalho continua "AUTORAL — QA PENDENTE [TS]", e enunciado, gabarito (E), [TS], Formato, Justificativas e Marcas não mudaram. A lista da seção 7 (linha 2.266, 12b) é igual ao campo da 5.2 nos 80 itens, e os 80 pontos continuam distintos (o do D2-13 difere do do D2-14).
- **Sequências.** Gabaritos ECECCEECECCCECEECCEEECEECECCEECEECCECCEECCCECEECEEECCCEECECCCEECCECCEEECCCECCEEE (40 C / 40 E). [TS] TnTTnTnnTnnnTTnTnnTTTnnTnTTnTnnTTnTTnnTnnnTTnnTnTTTnnnTTnTTnnTTTnTnnTnTTnnTnnTTn (40). As duas são iguais às da v2 e da T-75, seção 1.2.

## 4. D3 (T-76; 8 substituições)

- **Diff.** 7 hunks em 8 linhas: 1, 2, 478, 649, 727, 1.287, 1.864 e 1.952. É exatamente a lista da T-76, seção 3.
- **Trechos novos × R2, seção 9.** n. 1 → CSV 5 (D3-81, enunciado); n. 2 → 6 (D3-37, justificativa, linha 2); n. 3 → 4 (G-76); n. 4 → 8 (seção 8, notas à GBQ); n. 5 → 7 (seção 7.5); n. 7 → 3 (C7-23, opcional). Em todos, os dois campos são idênticos aos do R2. O enunciado do D3-81 na v2.1 (linha 727) é, byte a byte, o "Enunciado resultante" do R2. Duas ocorrências residuais são previstas. O texto antigo do n. 8 ocorre 1 vez porque é o fecho literal do texto novo, como registra a T-76. O texto novo do n. 2 já era substring do antigo.
- **Acréscimo da GCB (n. 1 e 2).** A linha 1 está no mesmo formato do D2. A linha 2 é o texto do R2, n. 6 ("… improbidade (P1-DA, itens 5 a 7) — …"), com uma única diferença: "v2" passou a "v2.1", por ordem da T-76. A forma "(P1-DA, itens 5 a 7)" é a da ficha do lote (linha 2 e linha 48) e a da D1 da GCB, seção 5, item 1 (linha 168). A condição do n. 6 do R2 (a GCB manter a D1, seção 5, item 1) foi cumprida. Correto.
- **Letra do Anexo N.** CC, art. 43, "ressalvado direito regressivo contra os causadores do dano, se houver, por parte destes, culpa ou dolo" (l. 143): o enunciado do D3-81 continua C. Lei 8.429, art. 12, § 2º, "A multa pode ser aumentada até o dobro, se o juiz considerar…" (l. 284): o G-76 novo contraria o dispositivo, que não mudou. Art. 11, XII, "com recursos do erário … inequívoco enaltecimento do agente público" (l. 270): a pegadinha nova do C7-23 se apoia na letra. As notas de montagem do n. 8 repetem o R1, ponto 33. Correto.
- **Itens.** 71 ids, mesma ordem nas versões e em 5.1 = 5.2. Mudam só o enunciado do D3-81 e a justificativa, linha 2, do D3-37. Cabeçalhos (QA PENDENTE (R2), BASE DOUTRINÁRIA), gabaritos, pontos, [TS] e marcas não mudaram. Gabaritos ECCEECEECCECEECCECEECECCEECECCEEECCEECEEECCEECEECCEEECEECCEEECECCECEECE (31 C / 40 E). [TS] TTnnTnTTnnTnTTnTnnTTTnnnTTnTnnTTTnTTnnTTTnnTTnTTTnnTTnTTnnTTTnTnnnTTTnT (40). As duas são iguais às da v2 e da T-76, seção 1.

## 5. D4 (T-77; 3 substituições)

- **Diff.** 2 hunks em 3 linhas: 1, 2 e 43. É exatamente a lista da T-77, seção 4. Da seção 1 até "FIM DO LOTE D4", nada mudou.
- **Trecho novo × R2 ("Ajustes residuais (texto exato)", n. 1) → CSV 3.** Idêntico nos dois campos. Na v2.1, o texto antigo ocorre 0 vez e o novo, 1 vez. É texto documental da seção 0.1, sem conteúdo normativo.
- **Acréscimo da GCB (n. 1 e 2).** A linha 1 está no mesmo formato e a linha 2 diz "v2.1". O "\n" no texto antigo do n. 1 serve só para unicidade: a citação da linha 1 da v2 na linha 22 (seção 0, ponto 9) continua intacta. Correto.
- **Itens.** 79 ids, mesma ordem e nenhum campo alterado. Gabaritos ECCEECECCCEEECCCECCEEECCECCEECECCCEECCECCEEECEECCECCEEECEECCECCCEECEECCECCEEECC (41 C / 38 E). [TS] com 39 marcações, mesma sequência da T-77, seção 1.

## 6. Observações (sem efeito)

Nenhuma ressalva nova. Algumas ocorrências antigas ficam como histórico, conforme decidido nas reconciliações: no D2, o motivo do art. 217 na seção 8 (T-75, 5.3, n. 5) e as citações da linha 1 da v2; no D3, a declaração da produção sobre o D3-81 (T-76, 4.3, n. 3); no D4, a citação da linha 1 da v2 na linha 22.

FIM DA CONFERÊNCIA — D2 v2.1 CONFERIDO; D3 v2.1 CONFERIDO; D4 v2.1 CONFERIDO
