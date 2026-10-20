# D2_parecer_R1_gcb-cqfp.md — T-75 — 2026-10-20 — gerado por gcb-cqfp
PARECER R1 — LOTE D2 v1 (saida/gcb/D2_v1.md, SHA-256 b357d93e386d00a9f52c1159cccf17c76f0fabe8ce517993bb15378249398b79, 310.515 bytes, LF, 2.056 linhas), junção mecânica pelo orquestrador das partes saida/gcb/D2_v1_parteA.md (SHA-256 4db081ed49fc72b31e4ec1c1580e3dc95ae81d96bad960e6a7a852c7551f88c8, 138.040 bytes, 949 linhas) e saida/gcb/D2_v1_parteB.md (SHA-256 04d82ec19376c2e639115fb5a5f1e2887fc88f06253474b20b79ae8ae9329480, 172.357 bytes, 1.073 linhas), produzidas por dois gcb-cpp em paralelo. Revisão de mérito. A gcb-cqfp revisa e não reescreve; os textos de ajuste abaixo são pontuais e fixados, como é costume; a redação final é da gcb-cpp na v2.

Referências: ficha saida/gcb/D2_ficha_lote.md (5c98fc685a5faddb6f46e53906104b8df04ff36840657798415763a1c6e561e6; seções 2 a 11 e Anexo R); Anexo N saida/gcb/D2_anexo_N_mapa_normativo.md (b0a54fff4ddcf21a693e01ba71032efccf72e0a6fdf912221ff05413cc0e340a, igual ao registrado na ficha), única base de texto legal; banco/banco.csv (b1c1588f8b4a80a233e7b8d485992d07e9adeb2570fb2343573ab7fde9a5721f) e banco/mapeamento_adicional.csv (c6f8a35586971080fdb0c0bd68428bdc7e04d547157f3f15f80eaa7708d302e5); saida/gcb/D1_v2.md (63bd27c34baec035dd39904ef565f6b5a662c0a30886a4a3d0b13b8b702e3d56; pontos bloqueados); CLAUDE.md; .claude/agents/gcb-cqfp.md; regras/PADRAO_UNICO_v1.md; regras/estilo_banca.md (v1.1.3); regras/proveniencia.md. Modelo: saida/gcb/D5_parecer_R1_gcb-cqfp.md. Não li saida/gcb/D2_leitura_critica.md (não existia em disco durante este R1; por instrução, não seria lido).

## 0. Resultado
- Itens: 80. APROVADO 71; APROVADO COM AJUSTE 9; REPROVADO 0.
- **Reprovação: 0/80 = 0,0%** (limite do gate: 30%). Não há gate.
- Por folha: nenhuma folha com reprovado. Ajustes: 3.1 (D2-07, obrigatório), 3.2 (D2-14), 3.3 (D2-23), 3.4 (D2-33, D2-34, D2-36, D2-39), 4.4 (D2-74, D2-80).
- Blocos: curso AJUSTE (pontual); resumo APROVADO; pares APROVADO; pegadinhas AJUSTE (pontual); proveniência APROVADO; contagens AJUSTE (o teste de ordem do LOTE falha na junção; seção 3, (a)); junção AJUSTE (forma; seção 3, (e)); leitura crítica: varredura de neutralidade sem ocorrência, mas sem o registro formal da ficha, seção 9 (seção 3, (g)).
- Veredito geral: **APROVADO COM AJUSTES** — a v2 responde aos 34 pontos da seção 5.

## 1. Evidência: conferência independente da base normativa (checklist 2 e 5)
1. Reabri em 20/10/2026, às 10:20 UTC, por curl com User-Agent de navegador (sem navegador), as 10 URLs da tabela de proveniência, que são as da seção 1 do Anexo N, sem parâmetro e sem sufixo. Arquivos em diretório próprio do scratchpad; extração por script (python3 -I), sem redigitação.

| Fonte (Anexo N) | URL | HTTP | Bytes (hoje × Anexo N) |
|---|---|---|---|
| 1 | https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm | 200 | 1.507.134 × 1.507.134 |
| 1-A | https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm | 200 | 1.847.715 × 1.847.715 |
| 2 | https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc138.htm | 200 | 21.932 × 21.932 |
| 3 | https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc140.htm | 200 | 49.669 × 49.669 |
| 4 | https://planalto.gov.br/ccivil_03/leis/l8112compilado.htm | 200 | 343.733 × 343.733 |
| 6 | https://www.planalto.gov.br/ccivil_03/leis/l9784.htm | 200 | 74.941 × 74.941 |
| 7 | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/decreto/d10835.htm | 200 | 71.902 × 71.902 |
| 8 | http://www.planalto.gov.br/ccivil_03/leis/l9007.htm | 200 | 12.549 × 12.549 |
| 9 | https://www.planalto.gov.br/ccivil_03/leis/l6999.htm | 200 | 8.785 × 8.785 |
| 10 | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12374.htm | 200 | 42.715 × 42.715 |

   Os textos de todas as 1.343 linhas de dispositivo da seção 4 do Anexo N que têm texto (excluídas rubricas, vetados e revogados sem texto) foram procurados nas páginas de hoje (comparação sem espaços em branco, ordinais "<sup>o</sup>" convertidos): 1.340/1.343 aparecem literalmente; as 3 restantes são a grafia "sic" do art. 93, §§ 5º a 7º, da Lei 8.112 (o "º" dentro de trecho tachado), já registrada no Anexo N, alerta 7. A redação do art. 40, § 4º, vigente em 2/10/2026 (EC 103/2019) foi encontrada na Fonte 1-A. Os SHA-256 do HTML de hoje diferem dos registrados no Anexo N com o mesmo tamanho (ex.: Fonte 1, f6fce3e7… × ae04e89b…; Fonte 4, be606b08… × 74a6719e…): só registro; o texto não mudou.
2. Citações: um script próprio (python3 -I) extraiu todas as citações "art./arts." do D2 v1 (curso, resumo, pares, pegadinhas, pontos de julgamento, justificativas, bases, proveniência, contagens), deduziu a norma pelo contexto e conferiu artigo, parágrafo, inciso e alínea contra os rótulos da seção 4 do Anexo N, com a situação (vigente, revogado, vetado, vigência encerrada). Resultado: 1.147 caminhos conferidos e existentes; nenhum item, justificativa ou base aponta dispositivo inexistente, revogado, vetado ou de vigência encerrada. Os 33 avisos residuais do script foram conferidos à mão e são artefatos de leitura (enumerações "I a III", "a a e", "I e XVII, e a"; norma deduzida errada pelo script; "Decreto 10.835, art. 36, I"; CF, art. 5º, LIV e LV, que o lote cita só como "[SEM FONTE — não afirmar]"). O art. 1º do Decreto 12.374 é citado só como "lido e não transcrito", como no Anexo N.
3. Por leitura, conferi contra o texto do Anexo N o texto, a numeração, os prazos, os números e o "redação dada por" de todos os 80 itens e das 160 linhas de justificativa, das 38 linhas das tabelas do resumo, dos 23 pares, das 88 pegadinhas e dos 89 blocos de curso (35 + caput C3.0-01 na parte A; 53 na parte B). Desvios: só os da seção 3 (curso e pegadinhas, todos fora de item).
4. Alertas do Anexo N (ficha, seção 3.3): EC 140/2026 — nenhum item no art. 40 (nem § 4º nem § 5º-A); nota de registro no curso C3.1-05, com a redação da EC 103/2019, conforme a ficha. CF, art. 37, XVI, b (EC 138/2025) — um item (D2-01), com REVERIFICAR, na redação vigente; a anterior serve de troca. Decreto 12.374/2025 — um item (D2-28, art. 21, § 1º), com REVERIFICAR; o art. 2º só no curso C3.4-03, no resumo (com referencial e REVERIFICAR) e no par P-06. REVERIFICAR ≤ 2 por folha (3.1: 1; 3.3: 1). Decreto 9.144 nunca citado como vigente (C3.3-07 e G-22 registram a revogação pelo Decreto 10.835, art. 36, I). Art. 143, §§ 1º e 2º, e art. 8º, III e IV, da Lei 8.112: só como revogados, sem conteúdo. Art. 60-D, §§ 3º e 4º: não usados. Dispositivos com "Vide ADI/ADPF" (CF, art. 39, caput, e art. 40, § 18; Lei 8.112, arts. 127, IV, 134 e 137): só no curso, pela letra, com a nota da ficha; nenhum item tem ponto neles nem depende deles; fora das tabelas do resumo.
5. Estágio probatório (ficha, seção 3.4): cumprido. Itens cujo ponto é número do tema: 2 (D2-06, CF, art. 41, caput, com "Segundo a Constituição Federal"; D2-31, Lei 8.112, art. 20, caput, com "Nos termos da Lei nº 8.112/1990"); nenhum sobre o art. 21 da Lei 8.112; nenhum item afirma revogação, derrogação, alteração da lei pelo Decreto, igualdade de prazos ou aplicação do Decreto à Câmara. Os três textos aparecem lado a lado em C3.4-03 e em P-06, com a frase literal da ficha, seção 3.4, (d).
6. Itens reais: banco/banco.csv tem exatamente 9 itens mapeados a P1-DA-3 e P1-DA-4 (BQ-0114, 0125, 0126, 0127, 0128, 0132, 0145, 0146, 0150), os do Anexo R; banco/mapeamento_adicional.csv não tem nenhum mapeamento a P1-DA-3 nem a P1-DA-4. Nenhum outro item do banco (varredura por "8.112", "9.784", "servidor", "requisi", "sindicância", "estágio") repete ponto do lote. Pontos do D1 conferidos no D1_v2 (texto dos itens D1-09 a D1-60): só o D2-07 colide (com o D1-18; ver item 2.1, n. 1).
7. Base doutrinária = 0 nos itens; nenhum "[SEM FONTE" em item (5.1 e 5.2); nenhuma referência a ADI, ADPF, STF, TCU ou doutrinador em enunciado; VOLÁTIL = 0, correto.

## 2. Veredito por item (checklist 3)
Legenda: AP = APROVADO; AJ = APROVADO COM AJUSTE (texto exato na seção 2.1); REP = REPROVADO. "Gab." é o da v1, conferido pela letra do Anexo N.

| Item | Folha | Gab. | [TS] | Veredito | Motivo curto |
|---|---|---|---|---|---|
| D2-01 | 3.1 | E | sim | AP | CF, art. 37, XVI, b (EC 138/2025): "de qualquer natureza" → "apenas técnico ou científico"; troca única; REVERIFICAR correto. |
| D2-02 | 3.1 | C | não | AP | Art. 37, III, literal. |
| D2-03 | 3.1 | E | sim | AP | Art. 38, III; supressão da condição de compatibilidade de horários. |
| D2-04 | 3.1 | C | sim (isca) | AP | Art. 41, § 1º, III, literal; isca "lei complementar" literal. |
| D2-05 | 3.1 | C | não | AP | Art. 41, § 3º, literal; moldura APL hipotética. |
| D2-06 | 3.1 | E | sim | AP | Art. 41, caput; referencial dito ("Segundo a Constituição Federal"); três anos → dois anos (ficha 3.4, (c)). |
| D2-07 | 3.1 | E | não | AJ | Art. 37, § 2º. O segmento falso ("a nulidade só se produz depois de declarada judicialmente") só se julga pela autotutela sem prévia decisão judicial, que é o ponto do D1-18 (e da Lei 9.784, art. 53, D1-18/D1-48); o próprio § 2º não diz nada sobre declaração judicial. Ajuste obrigatório; sem ele, o item é reprovado. |
| D2-08 | 3.1 | C | não | AP | Art. 37, XVI, a e c, com o caput; duas hipóteses verdadeiras. |
| D2-09 | 3.1 | E | sim | AP | Art. 37, X; "observada a iniciativa privativa em cada caso" → "do chefe do Poder Executivo em todos os casos". Mecanismo cabe melhor em E3 (nota, sem efeito). |
| D2-10 | 3.1 | C | não | AP | Art. 41, § 4º, literal; moldura APL. |
| D2-11 | 3.2 | C | não | AP | CF, art. 37, I, literal (mecanismo é C2, e não C3; nota, sem efeito). |
| D2-12 | 3.2 | C | não | AP | Lei 8.112, art. 2º, literal; SIT genérico. |
| D2-13 | 3.2 | E | sim | AP | Art. 37, V; exclusividade das funções de confiança transferida aos cargos em comissão. |
| D2-14 | 3.2 | C | sim (isca) | AJ | Art. 37, V. O enunciado traz, inteira, a proposição julgada no D2-13 ("funções de confiança são exercidas exclusivamente por servidores ocupantes de cargo efetivo"): quem lê um responde o outro (ficha 6.1). Separar o ponto (percentuais mínimos). |
| D2-15 | 3.2 | E | não | AP | Art. 9º, II e parágrafo único; E5 demonstrável pelo parágrafo único. |
| D2-16 | 3.2 | E | sim | AP | Art. 3º, parágrafo único; "criados por lei" → "por ato do dirigente máximo". |
| D2-17 | 3.2 | C | não | AP | Art. 5º, V, literal; sem pretensão de rol exaustivo. |
| D2-18 | 3.2 | C | não | AP | Art. 3º, caput, literal; "difere de BQ-0114" pertinente. |
| D2-19 | 3.2 | E | sim | AP | Art. 37, II; ressalva do cargo em comissão → função de confiança. |
| D2-20 | 3.2 | E | sim | AP | Art. 37, IX; "a lei" → "ato normativo do Poder contratante"; sem conteúdo da Lei 8.745. |
| D2-21 | 3.3 | E | sim | AP | Decreto 10.835, art. 9º, caput (irrecusável) × art. 3º, § 2º, III; "difere de BQ-0128" pertinente. |
| D2-22 | 3.3 | C | não | AP | Art. 9º, § 1º; não indica órgão com prerrogativa. |
| D2-23 | 3.3 | E | não | AJ | Lei 9.007, art. 2º e parágrafo único. O segmento acessório tem dois erros somados (perda de direitos e vantagens; período que não conta como efetivo exercício); a ficha 6.1 e o estilo 5.1 pedem um erro só. |
| D2-24 | 3.3 | E | sim | AP | Art. 9º, §§ 2º e 3º; exceção do § 3º suprimida. |
| D2-25 | 3.3 | C | não | AP | Art. 11, caput, com a ressalva. |
| D2-26 | 3.3 | E | sim | AP | Art. 11, parágrafo único × art. 8º; regra da cessão aplicada à requisição. |
| D2-27 | 3.3 | C | sim (isca) | AP | Lei 6.999, art. 2º, § 1º, literal; isca "um ano, prorrogável" literal. |
| D2-28 | 3.3 | C | não | AP | Decreto 12.374, art. 21, § 1º, literal; referencial dito; REVERIFICAR correto. |
| D2-29 | 3.3 | E | sim | AP | CF, art. 5º, XXV; "ulterior" → "prévia". |
| D2-30 | 3.3 | E | não | AP | Lei 8.112, art. 18, caput e § 2º; E5 demonstrável pelo § 2º. |
| D2-31 | 3.4 | C | não | AP | Art. 20, caput, literal; referencial dito; "difere de BQ-0125" pertinente. |
| D2-32 | 3.4 | E | sim | AP | Arts. 36 e 37; definição de remoção atribuída à redistribuição. |
| D2-33 | 3.4 | E | sim | AJ | Art. 8º × art. 33, I. Gabarito seguro, mas o campo "troca" registra três elementos por um ("o aproveitamento, a reintegração e a recondução → a exoneração"), como se houvesse troca múltipla; a omissão não é erro (C6), o erro é a inclusão da exoneração. |
| D2-34 | 3.4 | C | não | AJ | Art. 25, caput e I, literal. Tópico "readaptação, reversão, reintegração, recondução e aproveitamento", que a ficha 5.2 manda tratar com ângulo diferente do BQ-0150: falta o "difere de BQ-0150". |
| D2-35 | 3.4 | C | sim (isca) | AP | Art. 13, § 1º, literal; isca "trinta dias" literal. |
| D2-36 | 3.4 | E | sim | AJ | Art. 20, § 3º; troca única e correta. Mesmo artigo do BQ-0125 (art. 20, I a V) e tópico "estágio probatório … ângulo diferente do BQ-0125" (ficha 5.2): falta o "difere de BQ-0125". |
| D2-37 | 3.4 | C | não | AP | Art. 28, caput, literal; "difere de BQ-0150" pertinente. |
| D2-38 | 3.4 | C | não | AP | Art. 35, I e II, literal; moldura APL. |
| D2-39 | 3.4 | E | sim | AJ | Art. 91, caput (e art. 20, § 4º); troca única. Tópico "licenças e afastamentos … ângulo diferente do BQ-0126" (ficha 5.2): falta o "difere de BQ-0126". Gabarito de junção (E) cumprido. |
| D2-40 | 3.4 | E | não | AP | Arts. 106 e 107, I; E5 demonstrável pelo art. 107, I. Gabarito de junção (E) cumprido. |
| D2-41 | 4.1 | C | sim (isca) | AP | Lei 9.784, art. 2º, parágrafo único, XI, literal; "difere de BQ-0145/D1" pertinente. Gabarito de junção (C) cumprido. |
| D2-42 | 4.1 | C | não | AP | Lei 8.112, art. 126, literal na hipótese "nega a existência do fato". Gabarito de junção (C) cumprido. |
| D2-43 | 4.1 | E | sim | AP | Art. 128, parágrafo único; causa dispensada. |
| D2-44 | 4.1 | C | não | AP | Lei 9.784, art. 2º, parágrafo único, VI. |
| D2-45 | 4.1 | C | não | AP | Art. 129, só a proposição da fonte (norma interna); norma interna dita hipotética; dono 4.1 correto. Sem duplicata com o D2-55 (ver seção 4, B-3). |
| D2-46 | 4.1 | E | não | AP | Art. 143, caput ("assegurada ao acusado ampla defesa"); a dispensa contradiz o caput. |
| D2-47 | 4.1 | E | sim | AP | Art. 125; "independentes" → "dependentes". |
| D2-48 | 4.1 | C | não | AP | Art. 128, caput, literal; moldura APL. |
| D2-49 | 4.1 | E | sim | AP | Lei 9.784, art. 2º, parágrafo único, X; supressão das situações de litígio com "apenas". |
| D2-50 | 4.1 | E | sim | AP | Lei 9.784, art. 69; relação subsidiária invertida. |
| D2-51 | 4.2 | E | sim | AP | Art. 132, VII; ressalva da legítima defesa suprimida. |
| D2-52 | 4.2 | C | não | AP | Art. 116, IV, literal; moldura APL. |
| D2-53 | 4.2 | C | não | AP | Art. 141, I; moldura APL; não afirma prática da Casa. |
| D2-54 | 4.2 | C | não | AP | Art. 142, I a III, literal. |
| D2-55 | 4.2 | E | sim | AP | Art. 129 (penalidade) × art. 132, XIII; incisos I a VIII e XIX → IX a XVI. |
| D2-56 | 4.2 | E | sim | AP | Art. 117, VIII; segundo → terceiro grau. |
| D2-57 | 4.2 | C | não | AP | Art. 142, § 3º, literal; proposição diferente do D2-54. |
| D2-58 | 4.2 | E | sim | AP | Art. 131; correspondência 3/5 invertida (uma troca: a correspondência). |
| D2-59 | 4.2 | C | sim (isca) | AP | Art. 126-A, literal (vírgula acrescida após "apuração", sem efeito); isca literal. |
| D2-60 | 4.2 | C | não | AP | Art. 130, § 2º, literal; "difere de BQ-0146" pertinente. |
| D2-61 | 4.3 | C | não | AP | Art. 147, caput, literal; moldura APL. |
| D2-62 | 4.3 | E | sim | AP | Art. 149, caput; três → dois. |
| D2-63 | 4.3 | E | sim | AP | Art. 145, II; 30 → 90 dias. |
| D2-64 | 4.3 | C | sim (isca) | AP | Art. 168, parágrafo único, literal; isca "agravar" literal. |
| D2-65 | 4.3 | C | não | AP | Art. 161, § 2º, literal. |
| D2-66 | 4.3 | E | sim | AP | Art. 175; ônus do requerente → da autoridade. |
| D2-67 | 4.3 | C | não | AP | Arts. 140 e 133, literal. |
| D2-68 | 4.3 | C | não | AP | Art. 152, caput, literal. |
| D2-69 | 4.3 | E | sim | AP | Art. 169, § 1º; consequência invertida. |
| D2-70 | 4.3 | E | não | AP | Art. 146 ("sempre … será obrigatória"); a dispensa por confissão contradiz o caput. |
| D2-71 | 4.4 | E | sim | AP | Lei 9.784, art. 65, parágrafo único × art. 64, parágrafo único; regra do recurso transposta. |
| D2-72 | 4.4 | C | sim (isca) | AP | Art. 54, § 1º, literal; "difere de D1-50" pertinente (o D1-50 é o caput). |
| D2-73 | 4.4 | C | não | AP | Art. 64, parágrafo único; "difere de BQ-0132" pertinente. |
| D2-74 | 4.4 | C | não | AJ | Art. 61, caput; gabarito C se sustenta pela ressalva. Mas a moldura "servidor … recurso … em processo de seu interesse" convida a aplicar a lei própria do servidor (Lei 8.112, arts. 104 a 115, em especial art. 109), com a Lei 9.784 só subsidiária (art. 69): risco de impugnação por duas leituras (estilo 5.3). Trocar o sujeito por "interessado". |
| D2-75 | 4.4 | E | sim | AP | Art. 19, parágrafo único; grave → leve. |
| D2-76 | 4.4 | C | não | AP | Art. 49, literal. |
| D2-77 | 4.4 | C | não | AP | Art. 24, caput, literal. |
| D2-78 | 4.4 | E | sim | AP | Art. 49-A, § 6º, II; dentro da folha 4.4 (Lei 9.784), e não do item 5 do edital. |
| D2-79 | 4.4 | E | sim | AP | Art. 59, caput; dez → cinco dias; "difere de BQ-0132" pertinente. |
| D2-80 | 4.4 | E | não | AJ | Art. 38, § 2º. Gabarito E correto, mas a justificativa, linha 2, apoia a falsidade só na ausência ("que a norma não prevê"); a falsidade decorre do art. 56, caput (das decisões cabe recurso), que deve constar da justificativa e da base. Falta também o "difere de BQ-0132" (tópico recurso). |

### 2.1 Textos exatos dos ajustes (APROVADO COM AJUSTE)
1. **D2-07** (obrigatório) — Enunciado: "Segundo a Constituição Federal, a não observância da exigência de concurso público implica a nulidade do ato e a punição da autoridade responsável, nos termos da lei, mas a não observância do prazo de validade do concurso acarreta apenas a punição da autoridade, sem nulidade do ato." Ponto de julgamento: "CF, art. 37, § 2º — a nulidade do ato alcança também a inobservância do prazo de validade (inciso III), e não só a da exigência de concurso (inciso II)". Justificativa, linha 2: "O segmento final é falso: o § 2º comina a nulidade e a punição tanto à inobservância do inciso II quanto à do inciso III." Gabarito E; mecanismo E5; sem [TS] (contagens da folha mantidas).
2. **D2-14** — Enunciado: "Considere que se pretenda disciplinar, por lei, o preenchimento de cargos em comissão em órgão da administração pública federal. Nessa situação, segundo a Constituição Federal, os cargos em comissão devem ser preenchidos por servidores de carreira nos casos, condições e percentuais mínimos previstos em lei." Ponto de julgamento: "CF, art. 37, V — os cargos em comissão são preenchidos por servidores de carreira nos casos, condições e percentuais mínimos previstos em lei". Formato: SIT (3.2 passa a DEF 3, SUJ 3, SIT 2, NUM 1, PAR 0, APL 1). Gabarito C; [TS] com "elemento-isca: percentuais mínimos (literal no art. 37, V)" mantido. Justificativa, linha 2: "Não há troca: a candidata tende a achar que 'mínimos' estaria trocado por 'máximos', mas é o que o inciso diz."
3. **D2-23** — Enunciado: "As requisições de servidores de qualquer órgão ou entidade da Administração Pública Federal para a Presidência da República são irrecusáveis, mas o período da requisição não é considerado efetivo exercício no cargo ou emprego de origem." Ponto de julgamento: "Lei 9.007/1995, art. 2º, parágrafo único — o período de requisição para a Presidência da República é considerado, para todos os efeitos da vida funcional, efetivo exercício no cargo ou emprego de origem". Justificativa, linha 2: "O segmento final é falso: o parágrafo único considera o período de requisição, para todos os efeitos da vida funcional, como efetivo exercício no cargo ou emprego de origem." Gabarito E; E5; sem [TS].
4. **D2-33** — Campo "troca": "rol do art. 8º (formas de provimento) → inclusão da exoneração, que é forma de vacância (art. 33, I); a omissão do aproveitamento, da reintegração e da recondução não é o erro (incompleto não é errado)". Enunciado, gabarito E e [TS] mantidos.
5. **D2-34** — Acrescentar o campo: "Difere de BQ-0150 porque julga a definição de reversão e a sua hipótese por invalidez (art. 25, caput e I), e não a recondução e as suas duas causas (art. 29, I e II)."
6. **D2-36** — Acrescentar o campo: "Difere de BQ-0125 porque julga o limite da cessão do servidor em estágio probatório (art. 20, § 3º), e não os fatores de avaliação do estágio (art. 20, I a V)."
7. **D2-39** — Acrescentar o campo: "Difere de BQ-0126 porque julga a vedação da licença para o trato de assuntos particulares ao servidor em estágio probatório (art. 91, caput), e não a vedação de atividade remunerada na licença por motivo de doença em pessoa da família (art. 81, I, e § 3º)."
8. **D2-74** — Enunciado: "Considere que interessado interponha recurso administrativo contra decisão proferida em processo administrativo conduzido por órgão do Poder Legislativo da União no desempenho de função administrativa. Nessa situação, salvo disposição legal em contrário, o recurso não tem efeito suspensivo, conforme a Lei nº 9.784/1999." Justificativa, linha 2: "Não há troca; a moldura do Legislativo (art. 1º, § 1º, ponto do D1-16) é só contexto hipotético, e o item julga apenas a regra do art. 61, caput." Gabarito C, APL e "difere de BQ-0132" mantidos.
9. **D2-80** — Justificativa, linha 2: "O segmento final é falso: das decisões administrativas cabe recurso (art. 56, caput), e a recusa fundamentada de provas não suprime esse direito." Base: "Lei 9.784/1999, art. 38, § 2º; art. 56, caput, como contraste (Anexo N, seção 4.4)". Acrescentar o campo: "Difere de BQ-0132 porque julga a recusa de provas (art. 38, § 2º), e não a retratação da autoridade que proferiu a decisão (art. 56, § 1º)." Enunciado e gabarito E mantidos.

### 2.2 Item reprovado
Nenhum. O D2-07 só se mantém com o ajuste 1 (seção 2.1); sem ele, é reprovado por repetir o ponto do D1-18 (ficha, seção 7).

## 3. Blocos
- **(a) Contagens e sequência (checklist 4; ficha 5.1, 6.2 a 6.4)**: refeitas por script próprio sobre o D2_v1.md (o arquivo seqtest.py do scratchpad compartilhado não foi usado). 80 itens, D2-01 a D2-80 contínuos na 5.1 e na 5.2, 10 por folha, todos com os campos fixos, "AUTORAL" e "QA PENDENTE=sim"; linha de folha antes do primeiro item de cada folha nas duas formas; marca [TS] coerente nos três lugares (cabeçalho, "Marcas" e campo "troca"). Por folha: C = 5/5/4/5 (parte A, 19) e 5/6/5/5 (parte B, 21); lote 40 C/40 E (50%). [TS] = 5 em cada folha (4 E e 1 C com elemento-isca literal), 20 por parte, 40 no lote. Formatos dentro do teto de 3 por folha; APL ≤ 2 por folha contada a moldura (3.1: 2; 3.2: 1; 3.3: 0; 3.4: 1; 4.1: 2; 4.2: 2; 4.3: 1; 4.4: 1); nenhum SIT com moldura do Legislativo. REVERIFICAR 2; VOLÁTIL 0. As tabelas de contagem das duas partes conferem com o arquivo. Teste de ordem da ficha 6.4: APROVADO em cada uma das 8 folhas e em cada parte, para os gabaritos e para a sequência de [TS]; gabaritos de junção cumpridos (D2-39 = E; D2-40 = E; D2-41 = C; D2-42 = C). **No lote, dois testes falham, ambos na junção** (as produtoras testaram cada parte só com os 2 gabaritos de junção da outra, e o script de junção não acrescentou a "Contagens do lote", seção (e)):
  - gabaritos: bloco repetido de período 4 por 8 itens, D2-36 a D2-43 ("ECCE" + "ECCE"); limite da ficha: menos de 8;
  - [TS]: alternância estrita por 7 itens, D2-38 a D2-44 ("n T n T n T n"); limite: 4.
  Trocar posições entre itens de mesmo gabarito, o remédio previsto na ficha 2.4, não altera a sequência de gabaritos; o período 4 só se quebra com a troca de posição de um C com um E. Simulei por script todas as permutações das seis primeiras posições da folha 4.1 (mantidos D2-41 = C e D2-42 = C) e a de menor deslocamento que aprova folha, parte e lote, nos gabaritos e no [TS], é: **novo D2-41 = atual D2-44; novo D2-42 = atual D2-42; novo D2-43 = atual D2-41; novo D2-44 = atual D2-43**; D2-45 a D2-50 sem mudança. A folha 4.1 fica 5 C/5 E e 5 [TS]; lote: maior corrida 3, maior alternância 4, períodos 2/3/4 = 4/7/7, 5/6 = 8/11 (gabaritos) e corrida 3, alternância 4 (ver ponto 10 para o [TS]). Registro, fora do critério formal (períodos 2 a 6): no v1, o período 7 chega a 18 itens (D2-31 a D2-48) e o período 8 a 13 (D2-13 a D2-25); após a troca proposta, período 7 = 14.
- **(b) Ponto de julgamento e duplicatas (ficha 6.1 e 7)**: 80 pontos declarados, distintos por texto. Duplicata semântica dentro do lote: D2-13 × D2-14 (ajuste 2). Entre as partes: nenhuma (art. 129: D2-45 julga a fonte do dever, D2-55 o rol de proibições que leva à advertência; ver seção 4, B-3). Com o D1: D2-07 × D1-18 (ajuste 1). Com o Anexo R: nenhuma repetição; "difere de" pertinente nos 12 que o trazem; faltam D2-34, D2-36, D2-39 e D2-80 (ajustes 5 a 7 e 9). Pares que não devem ir ao mesmo simulado (sem efeito no veredito): ponto 20.
- **(c) Cobertura (checklist 1; ficha 5.2)**: cumprida em 3.1 (III: D2-02; § 2º: D2-07; XVI: D2-01, 08; art. 38: D2-03; remuneração: D2-09; estabilidade e avaliação: D2-06, 10; perda: D2-04; §§ 2º e 3º: D2-05), 3.2 (I: D2-11; II: D2-19; V: D2-13, 14; IX: D2-20; arts. 2º e 3º: D2-12, 16, 18; art. 5º: D2-17; art. 9º: D2-15), 3.3 (art. 9º, caput: D2-21; § 1º: D2-22; §§ 2º e 3º: D2-24; art. 11: D2-25, 26; Lei 9.007: D2-23; Lei 6.999: D2-27; Decreto 12.374: D2-28; art. 18: D2-30; art. 5º, XXV: D2-29), 3.4 (art. 8º: D2-33; posse: D2-35; estágio ≤ 2: D2-31, 36; provimentos derivados: D2-34, 37; vacância: D2-38; remoção × redistribuição: D2-32; licenças: D2-39; petição: D2-40), 4.1 (art. 143: D2-46; art. 128: D2-48, 43; art. 125: D2-47; art. 126: D2-42; critérios IV a XI: D2-41, 44, 49; art. 69: D2-50; fonte do art. 129: D2-45), 4.3 (sindicância: D2-63; art. 146: D2-70; art. 147: D2-61; comissão: D2-62; prazo: D2-68; indiciação: D2-65; julgamento: D2-64; nulidade: D2-69; revisão: D2-66; rito sumário: D2-67) e 4.4 (impedimento: D2-75; prazos: D2-77; instrução e decisão: D2-76, 80; decisão coordenada: D2-78; decadência: D2-72; recurso: D2-73, 74, 79; revisão: D2-71). **Folha 4.2: falta o tópico "destituição de cargo em comissão e conversão da exoneração (art. 135 e parágrafo único), 1"**, declarado pela produtora. A ficha soma 11 itens mínimos para 10 posições na 4.2 (dez tópicos, sendo a prescrição "ao menos 2"): é limite da ficha, e não erro da produção (ponto 11). Pares obrigatórios: os 12 presentes (P-01 a P-06; P-51 a P-56), todos com dispositivo do Anexo N de cada lado; 23 pares no total (12 + 11), acima do mínimo de 16.
- **(d) Curso, resumo, pares e pegadinhas**: conteúdo fiel ao Anexo N; exemplos ditos hipotéticos; nenhuma afirmação sobre norma interna, estrutura ou prática real da Câmara; Decretos 10.835 e 12.374 sem aplicação afirmada à Câmara ("[SEM FONTE — não afirmar]"); requisição pela Câmara não afirmada. Curso de caput (C3.0-01) curto e sem item, par ou pegadinha. Resumo: uma página por item, tabelas com números literais, sem art. 21 e sem dispositivos com remissão a ADI/ADPF; estágio sempre com referencial. Ajustes pontuais, fora de item (pontos 14 a 17): C3.3-06 parafraseia "na forma estabelecias por esta Lei" como "na forma da lei"; C4.1-06 diz que o inciso XII é "cobrado em outro lote" (é ponto do BQ-0145); C4.3-07/G-80 falam em "parente colateral" sem o limite do terceiro grau; o exemplo de C3.2-03 qualifica "função de direção" como função de confiança sem dizer que foi designação para função de confiança.
- **(e) Junção mecânica (ficha 2.4; critério 6)**: o texto das duas partes está integralmente preservado: script próprio confirmou que toda linha das partes está no D2_v1.md e que as únicas linhas novas são as de cabeçalho, as subdivisões "### Parte A/B" e a linha final; bloco de convenções idêntico nas duas partes; SHA-256 das partes registrados na linha 4 do D2_v1.md e iguais aos de hoje. Desvios de forma em relação à ficha 2.4: (i) linha 1 "… — junção mecânica pelo orquestrador das partes A e B (gcb-cpp); nenhum texto alterado", e não "… — gerado por gcb-cpp" (formato do CLAUDE.md); linha 2 também difere da ficha; (ii) seção "## 0. CABEÇALHOS DAS PARTES" acrescida (nono título "##") e bloco de convenções repetido duas vezes, em vez de uma (o da parte A); (iii) faltam "### Contagens do lote (script de junção)" na ## 7 (o que deixou passar as falhas da seção (a)) e "### Junção" na ## 8; (iv) o script saida/gcb/D2_juntar_partes.py não está no repositório, o que impede reproduzir a junção. Ver ponto 12.
- **(f) Proveniência (checklist 5)**: APROVADO. Dez URLs, idênticas às da seção 1 do Anexo N (inclusive "http://" na Lei 9.007 e o "planalto.gov.br" sem "www" na Lei 8.112), com "verificado em 20/10/2026 (Anexo N, fonte N)"; reabertas pela QA (seção 1). Itens reais citados com fontes em banco/banco.csv (cdn.cebraspe.org.br). Pontos sem fonte declarados, nenhum em item. Na parte A, a coluna "Data e fonte" repete "Anexo N, fonte N" duas vezes (forma, sem efeito).
- **(g) Leitura crítica (ficha, seção 9; critério 8)**: o arquivo saida/gcb/D2_para_leitura_critica.md existe (558a24d43ce96a6691ddc19bee2f2bc6f8caec2156ad748a99f8a3ba5fc8b2e9, 704 linhas; gravado às 07:12, um minuto depois do D2_v1.md). Linha 1 neutra no texto da ficha; instrução literal ao leitor; texto literal dos itens 3 e 4 do edital. Varredura desta QA contra a lista proibida da ficha (fornecedor, modelo, serviço, agentes e unidades da fábrica, "fábrica", Fundador, Presidência, T-, D-, "QA PENDENTE", Anexo N/R, "ficha", "banco", BQ-, D1-, D2-, gabarito, [TS], REVERIFICAR, VOLÁTIL, "[SEM FONTE", Derep/DETAQ, parâmetro de URL): 0 ocorrência. **Não constam do repositório o script gerador saida/gcb/D2_para_leitura_critica_gen.py nem o registro saida/gcb/D2_neutralidade_gcb-cqfp.md**, que a ficha exige antes de qualquer saída e antes do início do R1. Este R1 não grava o registro (instrução da T-75: gravar só o parecer); a varredura acima fica como subsídio (ponto 13). A resposta externa (D2_leitura_critica.md) não foi lida.
- **(h) Estilo Cebraspe (checklist 3)**: APROVADO no conjunto. "Julgue cada item como Certo ou Errado." na 5.1; afirmação única; nenhum "exceto" em enunciado; termos absolutos literais da norma ou como o próprio erro. Três padrões lexicais que a v2 deve olhar (estilo_banca 5.1 e 5.3; pontos 18 e 19): (i) **moldura do Legislativo × gabarito**: 9 dos 10 itens APL são C (só o D2-19 é E); (ii) "razão pela qual" aparece em 5 itens, todos E (D2-07, 15, 23, 30, 40; após os ajustes 1 e 3, em 3, todos E); (iii) termos absolutos ("apenas", "somente", "exclusivamente", "nunca", "sempre", "qualquer", "todos") aparecem em 16 enunciados, 15 deles E (só o D2-14 é C).
- **(i) Fronteiras (ficha 5.4; critério 6)**: respeitadas. Nenhum código da faixa da outra parte; dono de cada dispositivo conforme a ficha 5.4 (art. 129, fonte → 4.1; penalidade → 4.2; Lei 9.784, arts. 2º e 69 → 4.1; art. 18 da Lei 8.112 → 3.3; arts. 2º a 5º e 9º → 3.2). Citações cruzadas só como contraste, sem item.
- **(j) Primeira e última linha**: partes corretas ("# D2_v1_parteA.md — T-75 — 2026-10-20 — gerado por gcb-cpp"; "FIM DA PARTE A — LOTE D2"; idem B). Juntado: última linha "FIM DO LOTE D2" correta; linha 1 fora do formato (seção (e)). Produção (gcb-cpp) e QA (gcb-cqfp) em agentes distintos.

## 4. Respostas às dúvidas das produtoras (seção 8 de cada parte)
Parte A:
- A-1 (a) Previdência (CF, art. 40) sem item: correto; o tópico é teto ("no máximo 1"), e os §§ 4º, 5º-A e 18 estão vedados. (b) Art. 37, IV, e art. 4º da Lei 8.112 sem item: correto (tetos). (c) CF, art. 39, caput, e Lei 8.112, arts. 127, IV, 134 e 137 sem item: correto (ficha 3.2). (d) Folha 3.3 sem APL: correto (ficha, seção 4).
- A-2 Estágio probatório: tratamento conforme a ficha 3.4 (seção 1, n. 5).
- A-3 Itens para atenção: D2-01 e D2-28 corretos (REVERIFICAR). Iscas D2-04, D2-27 e D2-35: troca real e única, item certo; D2-14: ajuste 2 (duplicata com D2-13). E5 D2-07: ajuste 1 (colisão com D1-18); D2-23: ajuste 3 (dois erros); D2-15, D2-30 e D2-40: segmento falso demonstrável pelo Anexo N. Trocas de sujeito D2-13, D2-16, D2-20 e D2-39: corretas. "Difere de" D2-18, 21, 31 e 37: pertinentes. D2-06 e D2-31: corretos.
- A-4 Linha final "FIM DA PARTE A — LOTE D2": correta (ficha 2.2).
- A-5 Ocorrência de processo (seqtest.py sobrescrito no scratchpad compartilhado): registrada; os testes deste R1 foram refeitos por script próprio e confirmam os da parte A no escopo da parte (seção 3, (a)).
Parte B:
- B-1 Art. 135 sem item na 4.2: limite da ficha (11 mínimos para 10 posições); decisão da GCB (ponto 11).
- B-2 Arts. 127, IV, 134 e 137; art. 143, §§ 1º e 2º; pontos sem fonte: tratamento correto.
- B-3 Art. 129 em dois itens (D2-45 e D2-55): sem duplicata semântica; proposições diferentes, cada uma na folha que a ficha 5.4, (d), lhe atribui.
- B-4 Art. 69 × processo disciplinar: o item (D2-50) fica na letra do art. 69; a ligação com a Lei 8.112 só no curso: correto.
- B-5 Linha final "FIM DA PARTE B — LOTE D2": correta.
- B-6 (dúvida 1) Folha 4.2 com 6 C: dentro da faixa (4 a 6).
- B-7 (dúvida 2) D2-78: mantido; o dispositivo é da Lei 9.784 (folha 4.4) e o item não trata do poder disciplinar como poder (item 5 do edital).
- B-8 (dúvida 3) D2-45: norma interna dita hipotética, sem ato real da Câmara: correto.
- B-9 (dúvida 4) D2-70, "cassação de aposentadoria": literal do art. 146; o item não depende do art. 127, IV, nem do art. 134.
- B-10 (dúvida 5) Numeração do D1: conferida no D1_v2 por esta QA; os "difere de D1-NN" dos D2-41, 44, 49 e 72 são corretos. A lista do bloco 8 que inclui D2-60, 73, 74 e 79 entre os "difere de D1" é inexata: esses trazem "difere de BQ-NNNN" (ponto 21).
- B-11 (dúvida 6) Período 6 do [TS] = 11: passa na parte; no lote, a alternância do [TS] falha na junção (seção 3, (a); ponto 10).
- B-12 (dúvida 7) E sem [TS] (D2-46, D2-70, D2-80): correto; D2-80 recebe o ajuste 9 (ancoragem da falsidade).
- B-13 Itens para atenção: iscas D2-41, 59, 64 e 72 literais e sem troca; D2-53 só a letra do art. 141, I; D2-71 correto; D2-60 e D2-79 com ponto distinto do BQ-0146 e do BQ-0132.

## 5. Pontos para a v2 (a gcb-cpp responde item a item: acatado / não acatado + motivo)
1. D2-07 (obrigatório): enunciado, ponto de julgamento e justificativa, linha 2 (texto 2.1, n. 1).
2. D2-14: enunciado em SIT, ponto de julgamento e justificativa, linha 2 (texto 2.1, n. 2); refazer a contagem de formatos da 3.2.
3. D2-23: enunciado com um só erro, ponto de julgamento e justificativa, linha 2 (texto 2.1, n. 3).
4. D2-33: campo "troca" (texto 2.1, n. 4).
5. D2-34: "difere de BQ-0150" (texto 2.1, n. 5).
6. D2-36: "difere de BQ-0125" (texto 2.1, n. 6).
7. D2-39: "difere de BQ-0126" (texto 2.1, n. 7).
8. D2-74: sujeito "interessado" e justificativa, linha 2 (texto 2.1, n. 8).
9. D2-80: justificativa, linha 2, base com o art. 56, caput, e "difere de BQ-0132" (texto 2.1, n. 9).
10. Sequência do lote (seção 3, (a)) — **decisão da GCB**: a falha de período 4 dos gabaritos (D2-36 a D2-43) não se corrige com troca entre itens de mesmo gabarito (remédio da ficha 2.4). Proposta conferida por script: na folha 4.1, novo D2-41 = atual D2-44; novo D2-42 = atual D2-42; novo D2-43 = atual D2-41; novo D2-44 = atual D2-43; D2-45 a D2-50 inalterados. Corrige também a alternância do [TS] (D2-38 a D2-44). Se a GCB autorizar, a produtora da parte B renumera, registra a correspondência no bloco 8 e refaz o teste da ficha 6.4 na folha, na parte e no lote (gabaritos e [TS]), informando também os períodos 5 a 8. Se a GCB preferir corrigir pela parte A (folha 3.4), a troca também terá de ser de um C com um E.
11. Cobertura da 4.2 (art. 135) — **decisão da GCB**: (i) aceitar a lacuna na v1 (a ficha soma 11 mínimos para 10 posições), com registro, e fazer do art. 135 e parágrafo único o primeiro ponto do reforço D2-R da 4.2; ou (ii) mandar substituir um item da 4.2 por um item do art. 135 (por exemplo, "Constatada infração sujeita a suspensão ou demissão, a exoneração de cargo em comissão efetuada a juízo da autoridade é convertida em destituição de cargo em comissão" — C, art. 135, parágrafo único), redistribuindo os tópicos da folha e refazendo contagens e sequência. A QA recomenda (i), porque nenhum item da 4.2 tem tópico em duplicidade fora da prescrição, que a ficha exige em dobro.
12. Junção da v2 (ficha 2.4; seção 3, (e)): linha 1 no formato da ficha ("# D2_v2.md — T-75 — [data] — gerado por gcb-cpp") e linha 2 da ficha; bloco de convenções uma vez (o da parte A), sem "## 0"; "### Contagens do lote (script de junção)" com os testes da ficha 6.4 sobre D2-01 a D2-80 (gabaritos e [TS]); "### Junção" com os SHA-256 das partes e a data; script gravado em saida/gcb/D2_juntar_partes.py e executado com python3 -I.
13. Leitura crítica (seção 3, (g)) — à GCB e ao orquestrador: gravar no repositório o script saida/gcb/D2_para_leitura_critica_gen.py e emitir, em tarefa própria da gcb-cqfp, o registro saida/gcb/D2_neutralidade_gcb-cqfp.md ("NEUTRO CONFERIDO", SHA-256 558a24d4…b2e9, hora UTC). Se o arquivo já saiu para o leitor externo sem o registro, registrar o desvio de rito para a ratificação do Fundador, junto com os desvios já anotados na ficha, seção 9. A resposta externa vai para a v2 com registro de acatamento (saida/gcb/D2_acatamento_leitura_critica.md, seções A e B) e é conferida no R2.
14. Curso C3.3-06: trocar "dar-se-á na forma da lei (grafia do compilado: 'estabelecias')" por "dar-se-á na forma estabelecida por esta Lei (grafia do compilado: 'estabelecias')".
15. Curso C4.1-06: trocar "Os incisos I, II, III, V, XII e XIII são cobrados em outro lote" por "Os incisos I, II, III, V e XIII são pontos do D1, e o inciso XII é ponto do item real BQ-0145; nenhum deles é ponto de item desta folha".
16. Curso C4.3-07 (pegadinha) e G-80: trocar "admitir nela parente colateral do acusado" por "admitir nela cônjuge, companheiro ou parente do acusado, consanguíneo ou afim, em linha reta ou colateral, até o terceiro grau".
17. Curso C3.2-03, exemplo: trocar "seja designado para função de direção: trata-se de função de confiança" por "seja designado para função de confiança de direção: a função é reservada a quem tem cargo efetivo".
18. Moldura do Legislativo × gabarito (seção 3, (h), i) — **decisão da GCB**: 9 dos 10 APL são C. Ou (i) aceitar com registro; ou (ii) mandar converter ao menos 3 itens E em APL (ou neutralizar a moldura de ao menos 3 APL C), sem passar de 2 APL por folha e sem afirmar norma interna. A QA recomenda (ii).
19. Marcadores lexicais (seção 3, (h), ii e iii; estilo 5.1 e 5.3): variar o conector dos E5 restantes da parte A (D2-15, 30, 40), ou incluir um item C com "razão pela qual" verdadeiro; considerar um C com termo absoluto definicional além do D2-14. Não altera veredito; a produtora acata ou registra o não acatamento com motivo.
20. Notas à GBQ, para simulado (sem efeito no veredito): não pôr no mesmo simulado D2-13 com D2-14 (art. 37, V, mesmo após o ajuste) nem com D2-19; D2-63 com D2-70 (limite de 30 dias da sindicância × obrigatoriedade do processo acima de 30 dias); D2-71 com D2-73 (agravamento na revisão × gravame no recurso); D2-25 com D2-27 (prazo indeterminado × prazo da Lei 6.999); D2-42 com D2-47 (arts. 125 e 126); D2-45 com D2-55 (art. 129); D2-21 com D2-26 (requisição × cessão); D2-06 com D2-31 (números do estágio e da estabilidade).
21. Bloco 8 da parte B: corrigir a lista de itens com "difere de D1-NN" (são D2-41, 44, 49 e 72; D2-60, 73, 74 e 79 trazem "difere de BQ-NNNN").
22. Normalizar o campo "Formato" (a parte B acrescenta a descrição do código; a parte A, só o código). Forma; opcional.
23. Contagens das duas partes e do lote refeitas depois dos pontos 1 a 11 e 18, com a lista dos 80 pontos de julgamento declarada sem duplicata (ficha 6.1).
24. Dúvida A-1 (previdência, art. 37, IV, art. 4º, ADI, 3.3 sem APL): resolvida; sem ação.
25. Dúvida A-2 (estágio probatório): resolvida; sem ação.
26. Dúvida A-3 (itens para atenção da parte A): resolvida pelos pontos 1 a 3; demais sem ação.
27. Dúvida A-4 (linha final da parte A): resolvida; sem ação.
28. Dúvida A-5 (seqtest.py sobrescrito): registrada; à GCB, recomendação de scripts de teste com nome por parte e por tarefa no scratchpad; sem ação de conteúdo.
29. Dúvida B-1 (art. 135): ponto 11.
30. Dúvidas B-2 a B-5 (STF, art. 129 em duas folhas, art. 69, linha final): resolvidas; sem ação.
31. Dúvida B-6 (60% de C na 4.2): resolvida; sem ação.
32. Dúvidas B-7 a B-9 (D2-78, D2-45, D2-70): resolvidas; itens mantidos.
33. Dúvida B-10 (numeração do D1 não conferida pela produtora): conferida por esta QA; ponto 21.
34. Dúvidas B-11 e B-12 (período 6 do [TS]; E sem [TS]): pontos 10 e 9.

Todo item continua "QA PENDENTE" até o R2 e a reconciliação da GCB (D-QA-PENDENTE). Nada vai à plataforma nem à candidata.

FIM DO PARECER R1 — LOTE D2
