# D5_parecer_R1_gcb-cqfp.md — T-74 — 2026-10-20 — gerado por gcb-cqfp
PARECER R1 — LOTE D5 v1 (saida/gcb/D5_v1.md, SHA-256 efcf3aba443006b0bf98f204d5c1bf2cd975c43a361a8c377cdc12218d764d2b, 191.740 bytes, LF, 1.405 linhas, produzido pela gcb-cpp). Revisão de mérito. A gcb-cqfp revisa e não reescreve. Os textos de ajuste abaixo são pontuais e fixados, como é costume; a redação final e a substituição do item reprovado são da gcb-cpp na v2.

Referências: ficha saida/gcb/D5_ficha_lote.md (50260772…4a95; seções 2, 3, 5, 6, 7, 9 e 10); despacho lotes/loteD5/DESPACHO.md; regras/PADRAO_UNICO_v1.md; regras/estilo_banca.md; regras/proveniencia.md; Anexo N saida/gcb/D5_anexo_N_mapa_normativo.md (497af8e6…76eb), única base de texto legal; banco/banco.csv (b1c1588f…721f) e banco/mapeamento_adicional.csv (c6f8a355…02e5); DECISOES.md, linhas D-DA-LOTES, D-DA-BANCO, D-DA-INSUMOS, D-DA-PRODUTOR, D-REFORCO-2, D-CABECALHO-NEUTRO, D-LOTED1-CANONICO e D-LOTED6-CANONICO. Modelo: saida/gcb/D1_parecer_R1_gcb-cqfp.md.

## 0. Resultado
- Itens: 70. APROVADO 61; APROVADO COM AJUSTE 8; REPROVADO 1.
- **Reprovação: 1/70 = 1,4%** (limite do gate: 30%). Não há gate.
- Por folha: 10.1, 10.2, 10.3, 10.4, 10.5 e 10.7 sem reprovado; 10.6 com 1 reprovado (D5-54, 10% da folha).
- Blocos: curso AJUSTE; resumo AJUSTE; pares AJUSTE; pegadinhas AJUSTE; proveniência APROVADO; contagens APROVADO (com duas observações, seção 3); arquivo de leitura crítica NEUTRO CONFERIDO; script de limpeza APROVADO.
- Veredito geral: **APROVADO COM AJUSTES** — a v2 responde aos 24 pontos da seção 5.

## 1. Evidência: conferência independente da base normativa (checklist 2 e 5)
1. Reabri em 20/10/2026, às 08:41 UTC, por curl com User-Agent de navegador, as quatro URLs da tabela de proveniência (seção 6 do D5 v1), que são as do Anexo N, sem parâmetro e sem sufixo. Arquivos em diretório próprio do scratchpad; extração por script (python3 -I), sem redigitação.

| URL | HTTP | Bytes (hoje × Anexo N) | Resultado |
|---|---|---|---|
| https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm | 200 | 649.705 × 649.705 | Os 1.435 dispositivos da seção 4 do Anexo N (vigentes e vetados; fora as linhas tachadas) aparecem literalmente na página de hoje (comparação sem espaços em branco): 1.435/1.435, nenhuma divergência. O SHA-256 do HTML de hoje (553c842b…a7f2) difere do registrado (c8c14fdb…5f6f) com o mesmo tamanho: só registro; o texto não mudou. |
| https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15471.htm | 200 | 72.507 × 72.507 | Abre. Só fundamenta o art. 75, XVI (REVERIFICAR), usado apenas no curso. |
| https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15266.htm | 200 | 22.251 × 22.251 | Abre. Nenhum dispositivo alterado por ela é usado no lote. |
| https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15210.htm | 200 | 14.239 × 14.239 | Abre. Art. 44-A não usado. |

2. Citações: um script (python3 -I) extraiu as 806 citações "art./arts." de todo o D5 v1 (curso, resumo, pares, pegadinhas, pontos de julgamento, justificativas, bases, proveniência) e conferiu artigo, parágrafo, inciso e alínea contra as linhas **vigentes** do Anexo N (excluídas as tachadas e as vetadas). Resultado: 806/806 existem e são vigentes. O teste foi validado com citações falsas plantadas (§ inexistente, inciso inexistente, "art. 79, parágrafo único"), todas apanhadas.
3. Por leitura, conferi contra o texto do Anexo N o texto, a numeração, os prazos, os percentuais e os números de todos os 70 itens e das 70 justificativas, das 16 linhas da tabela do resumo, dos 16 pares e das 44 pegadinhas. Números do resumo: todos literais (art. 8º, § 2º; art. 32, § 1º, I, VIII e XI; art. 75, III e VIII; art. 94, I e II; arts. 98, 99, 106, 107, 110, 114, 123, 125; art. 135, § 3º; art. 137, § 2º, II a IV; art. 148, § 2º; art. 156, §§ 3º a 5º; art. 7º, III; art. 140, § 6º). Os desvios de redação estão na seção 3 (resumo, seguro-garantia; par P-16; curso C10.7-05).
4. "Redação dada por": nenhum item se apoia em dispositivo com redação de 2025/2026 (REVERIFICAR = 0 nos itens, correto). O art. 75, XVI aparece só no curso, C10.1-08, na redação da Lei 15.471/2026, igual à do Anexo N, com a marca REVERIFICAR e a redação anterior dada como superada. Vetos superados, art. 79 e arts. 191/193 não são usados. A ADI 6890 aparece só na proveniência, sem afirmar efeito.
5. Nenhum item afirma valor em reais (varredura "R$" e "reais" nos 70 enunciados: 0). Os valores do art. 75, I e II, e do art. 95, § 2º, aparecem só no curso, com "a Lei 14.133 fixa" e a nota de atualização (art. 182) NÃO CONFERIDA, como manda a ficha (6.6). Nenhum "[SEM FONTE]" em item. VOLÁTIL = 0, correto.
6. Itens reais do item 10: banco/banco.csv tem exatamente 4 itens P1-DA-10 (BQ-0113, BQ-0134, BQ-0135, BQ-0142), os do Anexo R; banco/mapeamento_adicional.csv não tem nenhum mapeamento a P1-DA-10. Conferência de ponto de julgamento na seção 2 (coluna Motivo) e na resposta 3 da seção 4.

## 2. Veredito por item (checklist 3)
Legenda: AP = APROVADO; AJ = APROVADO COM AJUSTE (texto exato na seção 2.1); REP = REPROVADO.

| Item | Folha | Gab. | Veredito | Motivo curto |
|---|---|---|---|---|
| D5-01 | 10.1 | C | AP | Art. 1º, I, literal; função administrativa do Legislativo. |
| D5-02 | 10.1 | E | AP | Art. 5º; [TS] por negação da presença no rol (polaridade), troca única. |
| D5-03 | 10.1 | E | AJ | [TS] legítimo (segurança jurídica → finalidade). Justificativa, linha 2, afirma "constar de outros diplomas" sem lastro no Anexo N. |
| D5-04 | 10.1 | C | AP | Arts. 5º e 11, IV. O inciso fala em "incentivar … o desenvolvimento nacional sustentável"; a paráfrase "objetivo" é aceitável (C1/C3). |
| D5-05 | 10.1 | C | AP | Art. 17, § 1º, literal, com os dois requisitos. |
| D5-06 | 10.1 | E | AP | Art. 6º, XLI, e art. 29; obrigatória → facultativa. |
| D5-07 | 10.1 | C | AP | Art. 6º, XXXIX e XL; omissão do prêmio não torna errado (C6). |
| D5-08 | 10.1 | E | AJ | Art. 72, VI; E5 correto. Mesma hipótese de fato do BQ-0113 (exclusividade, instrução da contratação direta): falta o "difere de BQ-0113". |
| D5-09 | 10.1 | E | AP | Art. 74, III; "publicidade e divulgação institucional" está dentro da vedação. "Difere de BQ-0113" pertinente. |
| D5-10 | 10.1 | C | AP | Art. 75, VIII, literal na parte reproduzida; elemento-isca literal; sem ADI. |
| D5-11 | 10.2 | C | AP | Art. 89, caput, literal. |
| D5-12 | 10.2 | E | AP | Art. 92, IX; "quando for o caso" → "em qualquer hipótese". O mecanismo cabe melhor em E6 (generalização) do que em E3; não muda o veredito. |
| D5-13 | 10.2 | C | AP | Art. 96, § 1º, literal. |
| D5-14 | 10.2 | E | AP | Art. 148, caput; E5 (retroatividade não dispensa a análise prévia). |
| D5-15 | 10.2 | E | AP | Art. 98; autorizada → vedada a majoração. |
| D5-16 | 10.2 | C | AP | Art. 103, § 4º, literal. |
| D5-17 | 10.2 | E | AP | Art. 103, § 2º; contratado → Administração. |
| D5-18 | 10.2 | C | AP | Art. 152, literal; isca "sempre" literal. |
| D5-19 | 10.2 | C | AP | Art. 156, § 3º, literal (0,5% e 30%). |
| D5-20 | 10.2 | E | AP | Art. 156, § 2º; inexecução parcial (art. 155, I) → total (III). |
| D5-21 | 10.3 | E | AP | Art. 6º, LVIII, e art. 92, § 3º; dois segmentos falsos, por isso sem [TS] (correto). |
| D5-22 | 10.3 | C | AJ | Art. 92, § 4º, II, e art. 135: a lei manda ("será por repactuação"; "serão repactuados"); o item diz "pode se dar". Gabarito C se sustenta, mas a ficha 6.5 pede o verbo do Anexo N. |
| D5-23 | 10.3 | E | AP | Art. 104, II; supressão de "nos casos especificados nesta Lei". |
| D5-24 | 10.3 | C | AP | Art. 107, literal, com previsão em edital e atestado. |
| D5-25 | 10.3 | C | AP | Art. 138, II, literal; isca literal. |
| D5-26 | 10.3 | E | AP | Art. 106, caput: "celebrar … até 5 anos"; a âncora "diretrizes do art. 106" afasta a leitura pela vigência decenal do art. 107 e pelo art. 108. |
| D5-27 | 10.3 | E | AP | Art. 125; 25% → 50% (recorte "nas compras" não é segunda troca). |
| D5-28 | 10.3 | C | AP | Art. 124, II, d, literal na ressalva. |
| D5-29 | 10.3 | E | AP | Art. 126; vedação → permissão condicionada. |
| D5-30 | 10.3 | C | AJ | Art. 137, § 2º, II, e § 3º, I: o "salvo" traz só parte da ressalva (falta "ato ou fato que o contratado tenha praticado…"); a justificativa diz "ressalva literal", o que não é exato. |
| D5-31 | 10.4 | C | AP | Art. 91, caput, literal. |
| D5-32 | 10.4 | E | AP | Art. 94, I e II; 10 → 20 dias úteis na contratação direta. |
| D5-33 | 10.4 | E | AP | Art. 7º, caput; autoridade máxima → agente de contratação. |
| D5-34 | 10.4 | C | AP | Art. 91, § 4º, alcança a prorrogação. |
| D5-35 | 10.4 | E | AP | Art. 95, § 2º; inversão regra × exceção; sem valor em reais. |
| D5-36 | 10.4 | C | AP | Art. 115, § 5º, literal; isca literal. |
| D5-37 | 10.4 | C | AP | Art. 121, § 1º, com a ressalva do § 2º expressa. |
| D5-38 | 10.4 | E | AP | Art. 120; E5. |
| D5-39 | 10.4 | C | AP | Art. 140, II, b, literal. Espelho parcial do D5-57 (nota à GBQ, ponto 22). |
| D5-40 | 10.4 | E | AP | Art. 117, caput; dever → faculdade. "Difere de BQ-0135" pertinente. Único item do caput na 10.4, como manda a fronteira da ficha. |
| D5-41 | 10.5 | E | AP | Art. 11, parágrafo único; alta administração → agente de contratação. |
| D5-42 | 10.5 | C | AP | Art. 12, VII, literal; isca "poderão" literal. |
| D5-43 | 10.5 | C | AJ | Art. 18, caput. Repete, em parte, a proposição do D5-49 ("fase preparatória caracterizada pelo planejamento"); separar os pontos (ficha 6.1). |
| D5-44 | 10.5 | E | AP | Art. 18, VI; obrigatoriamente → facultativamente. |
| D5-45 | 10.5 | C | AP | Art. 40, caput e II, literal. |
| D5-46 | 10.5 | C | AP | Art. 6º, XXIII, f, literal; peça do planejamento. |
| D5-47 | 10.5 | E | AP | Art. 169, caput; E5 (linhas de defesa não substituem o controle social). |
| D5-48 | 10.5 | E | AP | Art. 169, II e III; segunda → terceira linha. |
| D5-49 | 10.5 | C | AP | Arts. 5º e 18, caput. |
| D5-50 | 10.5 | E | AP | Art. 12, § 1º; "será observado" → "não vincula". |
| D5-51 | 10.6 | E | AJ | Art. 7º, III. "Não pode … ter vínculo … até o segundo grau" é verdadeiro como subconjunto da vedação até o terceiro grau; o gabarito E fica impugnável. Tornar o limite explícito. |
| D5-52 | 10.6 | C | AP | Art. 7º, I, e art. 117, caput; isca "preferencialmente" literal. |
| D5-53 | 10.6 | C | AP | Art. 117, § 1º (registro). "Difere de BQ-0134" pertinente. |
| D5-54 | 10.6 | E | **REP** | Duplicata de ponto com o D5-53 (ficha 6.1): o segmento falso só se julga pelo dever de anotar todas as ocorrências em registro próprio, que é o ponto do D5-53. Quem acerta um acerta o outro. |
| D5-55 | 10.6 | C | AP | Art. 117, § 4º, II, literal; ângulo distinto do BQ-0135 (§ 4º, I, titularidade). |
| D5-56 | 10.6 | E | AP | Art. 117, § 3º; órgãos de assessoramento → agente de contratação e equipe de apoio. |
| D5-57 | 10.6 | E | AP | Art. 140, II, a; responsável pela fiscalização → servidor ou comissão. |
| D5-58 | 10.6 | C | AP | Art. 7º, § 1º, literal, inclusive a finalidade. |
| D5-59 | 10.6 | C | AJ | Art. 7º, § 2º: o enunciado não fala do fiscal; a aderência à folha 10.6 ("papel do fiscalizador") fica fraca. Ancorar no fiscal. |
| D5-60 | 10.6 | E | AP | Art. 104, III; Administração → contratado. |
| D5-61 | 10.7 | C | AP | Art. 6º, XX, literal. Espelho com D5-62 e D5-70 (nota à GBQ, ponto 22). |
| D5-62 | 10.7 | E | AP | Art. 6º, XX e XXIII; ETP → TR (par obrigatório P-06). |
| D5-63 | 10.7 | E | AP | Art. 6º, XXIII, b; estudos técnicos preliminares → projeto básico. |
| D5-64 | 10.7 | C | AP | Art. 6º, XXIII, c, literal. |
| D5-65 | 10.7 | C | AJ | Art. 18, § 2º. "Deverá conter ao menos [XIII] e [VI], devendo apresentar justificativas quando não contemplar os demais" diz que os incisos I, IV e VIII (também obrigatórios) admitem justificativa: como está, o gabarito C não se sustenta. Ajuste obrigatório; sem ele, o item é reprovado. |
| D5-66 | 10.7 | E | AP | Art. 18, § 1º, XII, e § 2º; justificável → obrigatório sem justificativa. |
| D5-67 | 10.7 | C | AP | Art. 18, § 1º, V, literal, com a válvula do § 2º. |
| D5-68 | 10.7 | C | AP | Art. 40, § 1º, I, literal; isca literal. |
| D5-69 | 10.7 | E | AP | Art. 6º, XXVI e XXIV; projeto executivo → anteprojeto. |
| D5-70 | 10.7 | E | AP | Art. 6º, XX, e art. 18, II; E5. |

### 2.1 Textos exatos dos ajustes (APROVADO COM AJUSTE)
1. **D5-03** — Justificativa, linha 2: substituir por "O item substitui 'segurança jurídica' por 'finalidade', princípio que o art. 5º não enumera." (Sem afirmação sobre outros diplomas, que não estão no Anexo N.)
2. **D5-08** — Acrescentar o campo: "Difere de BQ-0113 porque julga a razão da escolha do contratado na instrução da contratação direta (art. 72, VI), e não o documento idôneo que comprova a exclusividade nem a vedação de preferência por marca (art. 74, I e § 1º)."
3. **D5-22** — Enunciado: trocar "pode se dar por repactuação" por "dar-se-á por repactuação". Base: acrescentar "art. 92, § 4º, II". Gabarito C mantido.
4. **D5-30** — Enunciado: depois de "de guerra", acrescentar ", ou quando a suspensão decorrer de ato ou fato que o contratado tenha praticado, do qual tenha participado ou para o qual tenha contribuído". Justificativa, linha 1: "… e o § 3º, I, exclui essa hipótese em calamidade pública, grave perturbação da ordem interna ou guerra, ou quando decorrer de ato ou fato do contratado." Gabarito C mantido.
5. **D5-43** — Enunciado: suprimir ", caracterizada pelo planejamento,", ficando "Nessa situação, a fase preparatória deve compatibilizar-se com o plano de contratações anual, sempre que elaborado, e com as leis orçamentárias." Ponto de julgamento: "art. 18, caput — a fase preparatória compatibiliza-se com o plano de contratações anual, sempre que elaborado, e com as leis orçamentárias". Gabarito C mantido; o D5-49 fica com "caracterizada pelo planejamento".
6. **D5-51** — Enunciado: "Para ser designado fiscal de contrato, o agente público não pode ser cônjuge ou companheiro de contratados habituais da Administração, e o impedimento decorrente de vínculo de parentesco com eles, colateral ou por afinidade, alcança somente até o segundo grau." Troca: "até o terceiro grau → somente até o segundo grau". Gabarito E e [TS] mantidos.
7. **D5-59** — Enunciado: "Os requisitos e a segregação de funções que se observam na designação do fiscal do contrato aplicam-se também aos órgãos de assessoramento jurídico e de controle interno da Administração." Base: art. 7º, caput, § 1º e § 2º; art. 117, caput. Gabarito C mantido. (Não mencionar o auxílio do § 3º, para não entregar o gabarito do D5-56.)
8. **D5-65** — Enunciado: "Entre os elementos que o estudo técnico preliminar deverá conter obrigatoriamente estão o posicionamento conclusivo sobre a adequação da contratação para o atendimento da necessidade a que se destina e a estimativa do valor da contratação." Justificativa, linha 2: "O item cita dois dos cinco elementos mínimos (I, IV, VI, VIII e XIII), sem a pretensão de esgotá-los; incompleto não é errado." Gabarito C mantido; "difere de BQ-0142" mantido.

### 2.2 Item reprovado
- **D5-54** — Substituir por item de ponto novo da folha 10.6, sem tocar o § 1º (D5-53), o § 2º (BQ-0134) nem o § 4º, I, na parte da atribuição exclusiva (BQ-0135). Sugestões com lastro no Anexo N: (a) art. 117, § 4º, I, na parte "responsabilidade civil objetiva pela veracidade e pela precisão das informações" ou "termo de compromisso de confidencialidade" do terceiro contratado, com "difere de BQ-0135"; ou (b) art. 137, II (desatendimento das determinações regulares da autoridade designada para acompanhar e fiscalizar a execução como motivo de extinção), já no curso C10.6-06. Para manter as contagens da folha (5 C/5 E; 5 [TS]; 1 E sem [TS]), o substituto deve ser E sem [TS] (E5), ou a gcb-cpp declara a nova contagem. Se usar a moldura do Legislativo, observar o ponto 20.

## 3. Blocos
- **Contagens (checklist 4; ficha 5.1, 6.2 a 6.4)**: refeitas por script sobre o arquivo. 70 itens D5-01 a D5-70 contínuos nas duas formas, todos com os campos fixos e "QA PENDENTE". Por folha: 10 itens; 5 C/5 E; 5 [TS] (4 E e 1 C com elemento-isca literal); [TS] sem campo "troca" = 0; formatos dentro do teto de 3 (10.3 com 3 de número ou prazo; 10.7 com 3 de par confundível); APL rotulado ≤ 2; REVERIFICAR 0; VOLÁTIL 0. Lote: 35 C/35 E (50%); 35 [TS]. Teste de ordem da ficha 6.4: APROVADO por folha e no lote (maior corrida de iguais 2; maior alternância estrita 4; nenhum bloco de período 2 a 4 com 8 ou mais). Sequência de [TS]: maior corrida 3, alternância 4, nenhum período 2 a 4. Pontos de julgamento declarados: 70 distintos (mas ver D5-54 e D5-43). Duas observações:
  (a) **Padrão de período 6 no gabarito.** De D5-13 a D5-38 (26 itens, folhas 10.2 a 10.4), o gabarito repete "CEECEC" (CEECECCEECECCEECECCEECECCE). A ficha só testa períodos 2 a 4, por isso o critério formal passa; mas o checklist pede ausência de padrão previsível. Também a marca [TS] repete período 6 em D5-55 a D5-70 (16 itens) e período 8 em D5-08 a D5-26 (19 itens); como a marca não aparece na versão do estudante, isso é só registro. Ver ponto 19.
  (b) **Moldura do Legislativo.** 23 dos 70 enunciados abrem com "Considere que um órgão do Poder Legislativo da União": 13 rotulados APL e 10 rotulados SIT (D5-08, 09, 14, 28, 37, 40, 47, 54, 68, 70). Pela convenção do próprio D5 v1 ("APL = aplicação parlamentar, contexto da seção 4 da ficha"), esses 10 também têm o contexto da seção 4, e o teto de 2 APL por folha (ficha 6.3) seria ultrapassado em 10.1, 10.3, 10.4, 10.5, 10.6 e 10.7 (4, 3, 4, 3, 3 e 4). Ver ponto 20 (decisão da GCB sobre o critério da sua ficha).
- **Curso**: AJUSTE. 44 blocos (9/7/5/5/6/6/6), cada um com definição por artigo, exemplo hipotético dito como tal e pegadinha com dispositivo. Nenhuma afirmação sobre norma interna ou prática real da Câmara. Ajustes: (a) **C10.7-05** afirma "o projeto básico, para obras e serviços de engenharia", e o exemplo diz que a reforma de auditório "exige projeto básico, e não apenas TR". Isso contradiz o art. 18, § 3º, que o próprio curso transcreve em C10.7-02 (obras e serviços comuns de engenharia: especificação "apenas em termo de referência ou em projeto básico", demonstrada a inexistência de prejuízo), e o art. 6º, XXV, não restringe o projeto básico à engenharia ("a obra ou o serviço"). Ver ponto 14. (b) **C10.2-02**, pegadinha: "garantias" estão em "quando exigidas" (art. 92, XII), não em "quando for o caso". Ver ponto 16.
- **Resumo**: AJUSTE. Uma página, conteúdo fiel ao curso; tabela com números literais. Corrigir a linha "1 mês antes da assinatura (seguro-garantia)": o art. 96, § 3º, fixa **prazo mínimo de 1 mês, contado da homologação e anterior à assinatura**. A redação atual sugere um prazo contado para trás a partir da assinatura. Ver ponto 15.
- **Pares**: AJUSTE. 16 (mínimo 14); os 12 obrigatórios estão presentes (P-01 a P-12), todos com "como a banca troca". Ajustes: **P-07** (TR × projeto básico): tirar "Usa o TR para obra" de "como a banca troca" e a restrição "obra ou serviço de engenharia" da diferença (art. 18, § 3º; art. 6º, XXV), como no ponto 14; **P-16**: "com competência de autoridade de nível equivalente ao das do § 6º, I" vale só para os Poderes Legislativo e Judiciário, o MP e a Defensoria (art. 156, § 6º, II). No Executivo, a competência é das próprias autoridades do inciso I. Ver ponto 17.
- **Pegadinhas**: AJUSTE. 44, uma por bloco, sem repetição, cada uma com dispositivo. Ajustar G-43 (tirar "usar TR para obra") e G-11 (garantias "quando exigidas"), junto com os pontos 14 e 16.
- **Proveniência (checklist 5)**: APROVADO. 4 normas, URLs idênticas às do Anexo N, sem parâmetro, com "verificado em 18/10/2026"; reabertas pela QA em 20/10/2026 (seção 1). Os itens reais citados têm as fontes em banco/banco.csv (cdn.cebraspe.org.br). Os pontos sem fonte estão declarados ("[SEM FONTE — não afirmar]": valores atualizados, atribuições do gestor, promulgação dos vetos, ADI 6890), nenhum em item.
- **Cobertura (checklist 1; ficha 5.2)**: cumprida nas 7 folhas, no curso e nos itens. 10.1: âmbito D5-01; princípios D5-02, 03, 04; objetivos D5-04; fases D5-05; modalidades D5-06, 07; contratação direta D5-08; inexigibilidade D5-09 (ângulo diferente do BQ-0113); dispensa D5-10; dispensada × dispensável sem item (teto "no máximo 1"; está no curso C10.1-09 e no par P-02). 10.2: regime D5-11; cláusulas D5-12; garantias D5-13, 15; riscos D5-16, 17; nulidade D5-14; meios alternativos D5-18; sanções D5-19, 20 (teto 2). 10.3: prerrogativas D5-23; duração D5-24, 26; alteração D5-27, 28, 29; equilíbrio D5-21, 22, 28; extinção D5-25, 30. 10.4: formalização D5-31, 32, 34, 35; designação D5-33; execução D5-36, 37, 38; recebimento D5-39; caput do art. 117 só em D5-40. 10.5: princípio e governança D5-41, 49; PCA D5-42, 50; fase preparatória D5-43, 44; compras D5-45; modelo de gestão D5-46; riscos e linhas D5-47, 48. 10.6: requisitos e segregação D5-51, 52, 58; registro D5-53; § 3º D5-56; § 4º, II D5-55; recebimento provisório D5-57; prerrogativa D5-60 (o substituto do D5-54 não pode desfazer nenhuma destas). 10.7: ETP D5-61; alíneas do TR D5-63, 64; § 1º e § 2º D5-65, 66, 67; TR × anteprojeto × projetos D5-69 (teto 1); art. 40, § 1º D5-68. Fronteira do art. 117 respeitada.
- **Estilo Cebraspe**: APROVADO no conjunto. "Julgue cada item como Certo ou Errado." na versão do estudante; afirmação única; nenhum "exceto"; nenhuma referência a ADI, STF, TCU ou doutrinador em item; termos absolutos ("somente", "sempre", "exclusivamente", "todas", "todo") ou são literais da lei (D5-10, 18, 20, 53, 64) ou são o próprio erro (D5-12, 50). Exceções tratadas na seção 2: D5-22 (verbo), D5-30 (ressalva parcial), D5-51 (limite numérico ambíguo), D5-65 (ao menos/demais).
- **Leitura crítica (critério 7; D-CABECALHO-NEUTRO; D-DA-PRODUTOR)**: **NEUTRO CONFERIDO.** saida/gcb/D5_para_leitura_critica.md (83915866133d6909af626a8355333f6f403681033edb1b0d669d59fcb9439da1, igual ao registrado em TAREFAS.md, 354 linhas). Linha 1 = texto da ficha, seção 9 ("LOTE D5 — Licitações e contratos (Lei 14.133/2021) — curso, resumo, pares e pegadinhas — 18/10/2026"); a instrução ao leitor é a literal da D-DA-PRODUTOR. Varredura: 0 ocorrência de fornecedor, modelo, serviço, agente da fábrica, unidade, fábrica, Fundador, Presidência, id de tarefa ou de decisão, "QA PENDENTE", Anexo N/R, BQ-, "ficha", "banco", "D5-", gabarito, [TS], REVERIFICAR, VOLÁTIL, "[SEM FONTE", URL ou parâmetro de URL. As ocorrências de "agente", "produtor", "fabricante", "unidades" e "lotes" são termos da lei. O arquivo não traz itens, gabaritos, justificativas, contagens nem bloco à GCB. **Script saida/gcb/D5_para_leitura_critica_gen.py** (f862cd26…17c8): extrai exatamente as seções 1 a 4 do D5 v1 (de "## 1. (a) CURSO" até antes de "## 5. (e) ITENS"), aplica 19 substituições de neutralização, cada uma com aborto se não encontrar o texto, e põe o cabeçalho neutro, a instrução e o item 10 literal do edital. Rodei uma cópia no scratchpad com os caminhos deste repositório (python3 -I): a saída é **byte a byte igual** ao arquivo gravado (mesmo SHA-256), o que também confirma que o D5 v1 não mudou desde a geração. Registro: o script tem caminhos absolutos de outra máquina (/home/user/felipeRM/…) e não roda aqui sem edição (ponto 23). Quando o R1 começou (20/10/2026, 08:41 UTC, dentro do prazo de 48 horas, que vence em 20/10/2026, 16:11:47 UTC), não havia resposta externa nem registro de acatamento. O arquivo saida/gcb/D5_leitura_critica.md apareceu em disco durante o R1 (gravado às 08:45 UTC). Por instrução do despacho, esta QA não o leu nem o comenta. O registro de acatamento (saida/gcb/D5_acatamento_leitura_critica.md) não existe. Pela ficha, seção 9, resposta que chega depois de iniciado o R1 vai para a v2, com registro de acatamento item a item, e o R2 confere (ponto 24).
- **Primeira e última linha (critério 9)**: corretas ("# D5_v1.md — T-74 — 2026-10-18 — gerado por gcb-cpp"; "FIM DO LOTE D5"). Produção gcb-cpp e QA gcb-cqfp em agentes distintos.

## 4. Respostas às dúvidas da produtora (bloco à GCB do D5 v1)
1. **E5 sem [TS] (D5-08, 14, 21, 38, 47, 54, 70)**: nenhum deles ganha [TS]. D5-21 tem dois segmentos falsos (índice "único e nacional" e "vedada"); nos demais, o erro está no nexo causal ou consequente, não na troca de um elemento do dispositivo. O total de [TS] fica em 35. O D5-54 sai por outro motivo (seção 2.2).
2. **Itens marcados para atenção**: D5-26, gabarito E seguro (seção 2). D5-09, correto ("divulgação institucional" está dentro de "publicidade e divulgação"). D5-30, AJUSTE (ressalva completa). D5-37, correto (ressalva do § 2º expressa). D5-65, AJUSTE obrigatório (o "demais" inclui incisos obrigatórios). D5-60, correto (inversão do titular, troca única).
3. **Anexo R**: nenhum item repete ponto de julgamento de item real. D5-09 × BQ-0113, D5-40 e D5-55 × BQ-0135, D5-53 e D5-56 × BQ-0134, D5-65, 66 e 67 × BQ-0142: ângulos distintos, "difere de" pertinente. Falta o "difere de BQ-0113" no D5-08 (ajuste 2). O "difere de BQ-0134" do D5-54 está correto, mas o item reprova por duplicata interna.
4. **Gestor do contrato**: a abordagem do curso e do par P-08 (a lei só nomeia o gestor, art. 8º, § 3º; atribuições "[SEM FONTE — não afirmar]") está correta e não gera item.
5. **Conceito e finalidade (10.1)**: apoio nos arts. 11 e 17, sem item doutrinário: correto (Anexo N, seção 7, item 11).

## 5. Pontos para a v2 (a gcb-cpp responde item a item: acatado / não acatado + motivo)
1. D5-03: justificativa, linha 2, sem "outros diplomas" (texto 2.1, n. 1).
2. D5-08: acrescentar "difere de BQ-0113" (texto 2.1, n. 2).
3. D5-22: "dar-se-á por repactuação"; base com o art. 92, § 4º, II (texto 2.1, n. 3).
4. D5-30: ressalva completa do art. 137, § 3º, I, no enunciado e na justificativa (texto 2.1, n. 4).
5. D5-43: tirar "caracterizada pelo planejamento" e reescrever o ponto de julgamento (texto 2.1, n. 5).
6. D5-51: limite explícito "alcança somente até o segundo grau" (texto 2.1, n. 6).
7. D5-59: ancorar no fiscal do contrato, sem citar o § 3º do art. 117 (texto 2.1, n. 7).
8. D5-65: retirar o segmento "devendo apresentar justificativas quando não contemplar os demais"; justificativa, linha 2, com os cinco incisos (texto 2.1, n. 8).
9. D5-54 (REPROVADO): substituir por item de ponto novo da 10.6 (seção 2.2), com ponto de julgamento, base, mecanismo e, se houver, "difere de".
10. Contagens da 10.6 e do lote refeitas após o ponto 9 (meta: 5 C/5 E e 5 [TS] na folha; 35/35 e 35 [TS] no lote), com o teste da ficha 6.4 refeito.
11. Pontos de julgamento: declarar na v2 a lista dos 70 pontos depois dos pontos 5 e 9, sem duplicata (ficha 6.1).
12. Nota de mecanismo (sem efeito no gabarito): D5-12 em E6 (generalização "em qualquer hipótese"), se a produtora concordar.
13. Notas à GBQ registradas no bloco à GCB da v2 (ver ponto 22).
14. Curso C10.7-05, par P-07 e pegadinha G-43: retirar "o projeto básico, para obras e serviços de engenharia" e "usar TR para obra"; trocar o exemplo da reforma de auditório pela letra do art. 6º, XXV (o projeto básico define e dimensiona a obra ou o serviço) e do art. 18, § 3º (em obras e serviços comuns de engenharia, demonstrada a inexistência de prejuízo, a especificação pode ser feita apenas em TR ou em projeto básico).
15. Resumo, tabela: "prazo mínimo de 1 mês, contado da homologação e anterior à assinatura (seguro-garantia)", art. 96, § 3º.
16. Curso C10.2-02 e G-11: "garantias, quando exigidas" (art. 92, XII), separadas das cláusulas "quando for o caso".
17. Par P-16: competência para a inidoneidade conforme o art. 156, § 6º, I (Executivo: ministro de Estado, secretário estadual ou municipal; autarquia ou fundação: autoridade máxima) e II (Legislativo, Judiciário, MP e Defensoria: autoridade de nível hierárquico equivalente, na forma de regulamento).
18. Arquivo de leitura crítica: se a v2 mudar curso, resumo, pares ou pegadinhas (pontos 14 a 17), a GCB decide se regera o D5_para_leitura_critica.md. Não é condição do R2, porque o arquivo já foi entregue ao leitor externo.
19. Sequência de gabaritos: quebrar o bloco de período 6 de D5-13 a D5-38. Trocar posições entre itens de mesmo gabarito não muda a sequência; é preciso trocar de posição, dentro de ao menos uma das folhas 10.2 a 10.4, um item C com um item E (a folha continua com 5 C e 5 E) e renumerar, com a correspondência no bloco à GCB. Refazer o teste da ficha 6.4 e informar também os períodos 5 a 8. Se a GCB entender que o critério formal (períodos 2 a 4) basta, registra o não acatamento com motivo.
20. Moldura do Legislativo (seção 3, observação b) — **decisão da GCB** sobre o critério da sua ficha: (i) aceitar que SIT com moldura legislativa não conta como APL; ou (ii) mandar neutralizar a moldura em parte dos 10 itens SIT ("Considere que, em contrato regido pela Lei nº 14.133/2021, …"), para que cada folha tenha no máximo 2 itens com o contexto da seção 4. A produtora executa o que a GCB decidir.
21. Contagem de formatos refeita depois dos pontos 9 e 20.
22. Notas à GBQ, para simulado (sem efeito no veredito): não pôr no mesmo simulado D5-61 com D5-62 ou D5-70 (mesma definição do art. 6º, XX); D5-39 com D5-57 (agentes dos recebimentos em compras); D5-24 com D5-26 (prazos dos arts. 106 e 107); D5-66 com D5-67 (válvula do art. 18, § 2º); D5-43 com D5-49 (art. 18, caput), mesmo depois do ajuste.
23. Script D5_para_leitura_critica_gen.py: parametrizar os caminhos (relativos à raiz do repositório) para que rode em qualquer máquina. Não muda o arquivo gerado.
24. Leitura crítica externa: saida/gcb/D5_leitura_critica.md chegou durante o R1 e não foi lida por esta QA. A gcb-cpp grava saida/gcb/D5_acatamento_leitura_critica.md (acatada / não acatada + motivo, só com artigo vigente do Anexo N e sem repetir ponto coberto, nem os pontos de julgamento já usados) e leva à v2, com "QA PENDENTE", o que acatar; o R2 confere o registro e tudo o que ele mudar (critério 7).

Todo item continua "QA PENDENTE" até o R2 e a reconciliação da GCB (D-QA-PENDENTE). Nada vai à plataforma nem à candidata.

FIM DO PARECER R1 — LOTE D5
