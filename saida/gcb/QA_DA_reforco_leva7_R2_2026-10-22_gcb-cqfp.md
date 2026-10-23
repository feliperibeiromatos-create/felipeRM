# QA_DA_reforco_leva7_R2_2026-10-22_gcb-cqfp.md — T-116 — 2026-10-22 — gerado por gcb-cqfp

# PARECER QA R2 (ÚLTIMA RODADA) — REFORÇO DA, LEVA 7 (v2) — ciclo s16c5
A gcb-cqfp (opus) faz este QA de forma independente. Ela não produziu o texto revisado e não reescreve itens. Nenhum outro arquivo do repositório foi alterado; não houve commit nem push.

O exame segue:
- a ficha, seção 4.3: "o R2 confere cada AJ aplicado literalmente e examina só o que a v2 mudou além dos AJ";
- o R1, seção 8, item 1 (aplicar AJ-1 a AJ-8; qualquer outra mudança é examinada no R2);
- a ficha, seções 7.6, 9.3 (item 6), 10.3, 11.3 e 12.3 (o que é registro e o que é errata depois do R2);
- a auditoria de estilo (sem AJ; um registro sobre a justificativa, linha 2, do D3-R75).

Pontos examinados:
- os AJ-1 a AJ-8 (D3-R68), por substituição exata, inclusive o rótulo «**D3-R68.**» do AJ-1;
- o D3-R68 novo;
- os 29 itens não alterados;
- a Resposta à R1 (R.1 a R.6);
- a seção 4 refeita, contra o arquivo, inclusive o que a produção não recalculou (sequências, 4.1, 4.3, 4.4);
- toda mudança fora dos itens, contra a lista da R.4;
- a pendência declarada (dúvida (iv) do bloco 5 e item 1 da 6.4) e o registro do estilo sobre o D3-R75.

## 0. Objeto, entradas e método
| objeto | SHA-256 (em disco, 22/10/2026) |
|---|---|
| saida/gcb/DA_reforco_leva7_v2.md (objeto do R2; 30 itens; 159.681 bytes; 986 linhas LF; 0 CR) | c4f50b9ecabb3f0c99592d4bd997012b647a2b6b5b10ab5521eece385fe1f764 (= despacho) |
| saida/gcb/DA_reforco_leva7_v1.md (objeto do R1; base do diff; 922 linhas) | fdafc3bd36127778727edb66d863c135f1fa08182757b6e58ec4c27ae736a0ed (= despacho e R1) |
| saida/gcb/QA_DA_reforco_leva7_R1_2026-10-22_gcb-cqfp.md | f65132cf8fcda6081b059358d67ebe16c6603dcb44b06250003a449b4277a2ab (= despacho) |
| saida/banco/estilo_DA_reforco_leva7.md | fd59ea46407b10cf89a9a3b644449f4014f966f95a205f65df23ae13ca1098e1 (= despacho) |
| saida/gcb/DA_reforco_ficha_2026-10-20.md | 34fe46fc59e9215966b5568966c7a8a7d831c744760b12e08369a1eebf995391 (= despacho) |
| modelo de forma: saida/gcb/QA_DA_reforco_leva6_R2_2026-10-22_gcb-cqfp.md | d99c6d1936f457ac2a1149a8b225e03d7c751360939b67edadeef339f202b249 |

Lastro relido: adendo do D3 de 22/10/2026, seção 2 (A5.1-01, l. 59) e seção 4.1 (art. 84, II, l. 106); normativo_cache/CF_1988_compilada_2026-10-20.txt (l. 1017, 1036–1038, 1089–1091); normativo_cache/Lei_4619_1965_2026-10-20.txt (art. 6º); saida/pacote/pacote.json v1.13 (canônicos D3-01 a D3-10, campo enunciado). Também foram lidos: da ficha, as seções 1, 4, 7.3, 7.4, 7.6, 9.3, 10.2, 10.3, 11.2, 11.3, 11.6, 12.2, 12.3, 13.1 a 13.6; regras/ e CLAUDE.md.

Método: scripts próprios em python3 -I, somente leitura, no scratchpad da sessão (…/scratchpad/qa7r2/), fora do repositório.
- (a) `diff` v1 × v2, lido linha a linha: 13 blocos de diferença (l. 1; 3; 5; 8–71 inseridas; 106; 285; 291; 295; 796; 897; 899; 944; 948). Linhas 3, 5, 944 e 948 comparadas também por caractere (SequenceMatcher).
- (b) aj.py: os 8 AJ, copiados do R1 (seção 5) por expressão regular, aplicados em memória à v1 por `str.replace(antes, depois, 1)`; resultado comparado com a v2 por id (seções 1 e 2) e linha a linha fora da "Resposta à R1".
- (c) s4.py: refeitos sobre a v2 e sobre a v1 gabarito, [TS], Troca ⇔ [TS] ⇔ "TS=sim", formatos, moldura, aderência, mecanismos, abertura × gabarito, fórmula, extensão (por espaços, como a produção) e o teste de sequência da regra 6 (corrida de 4, alternância de 5, bloco de período 2 a 8 por max(8, 2p)), na leva, nas folhas da leva e nas folhas acumuladas com os canônicos da ficha 13.4.7. Prefixo comum (L3-3) do D3-R68 novo com os 29 itens da leva e com os canônicos da 5.1 (pacote.json v1.13).

**Rede — reabertura no planalto.gov.br (checklist, item 3; ficha 11.6).** Comando: `curl -sS -m 120 -A "Mozilla/5.0" -o <arquivo> -w "%{http_code} %{size_download}" <URL>`. HTML só no scratchpad. Texto extraído por html.parser (cp1252, sem script/style, sem tachado), espaços normalizados.

| hora (UTC) | URL | HTTP | bytes (= Anexo/adendo e R1) | SHA-256 do HTML |
|---|---|---|---|---|
| 2026-10-23T00:29:17Z | https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm (Fonte 4; B1) | 200 | 1.507.134 | e1a7a9c5ec2f07d4062330d520b96ca9042a2662f0e29e09ca3db4b74c2271e4 |
| 2026-10-23T00:29:21Z | https://www.planalto.gov.br/ccivil_03/leis/1950-1969/l4619.htm (B3; https, ficha 13.6) | 200 | 8.562 | fee3ba61bf686d740847c0ca61957a65e315cdba8828c6478cd1f18bbc2e70d2 |
| 2026-10-23T00:29:21Z | https://www.planalto.gov.br/ccivil_03/decreto/antigos/d20910.htm (B4) | 200 | 7.151 | c9635ba6e5bc959f04daac5c91542da69d0831b8b29a4fe3bef33cb5e8423979 |
| 2026-10-23T00:29:22Z | https://planalto.gov.br/ccivil_03/leis/l8429compilada.htm (Fonte 1) | 200 | 173.931 | 9ac89736f30a7686f6c0ca21e9f914ae00d5a54b75ef858741c14e7dbbb2da4f |

As horas em UTC caem em 22/10/2026, 21h29 no horário de Brasília. O SHA do HTML muda a cada download (Anexo N do D3, seção 1); a comparação é sobre o texto.
- **CF:** «Compete privativamente ao Presidente da República:» e «II - exercer, com o auxílio dos Ministros de Estado, a direção superior da administração federal;» ocorrem 1 vez cada. A expressão «direção superior» ocorre **1 vez** na página (e 1 vez na cópia, l. 1038). O art. 87, parágrafo único, I («exercer a orientação, coordenação e supervisão dos órgãos e entidades da administração federal na área de sua competência»), ocorre 1 vez.
- **Lei 4.619:** «não excederá de uma quinta parte, da importância de seu vencimento ou remuneração» ocorre 1 vez; «terço» 0 vez; «desconto» 1 vez (só no art. 6º).
- **Decreto 20.910:** «A prescrição somente poderá ser interrompida uma vez.» 1 vez. **Lei 8.429:** página aberta, bytes iguais.

A reabertura é conferência, não base. A Base dos itens continua a consulta de 20/10/2026 (ficha 11.6).

## 1. Veredito geral
- **Leva: APROVADA.**
- O item alterado: **D3-R68 APROVADO** (AJ-1 a AJ-8 aplicados; E firme pela letra do art. 84, caput e II, da CF).
- Os 29 itens não alterados ficam APROVADOS, como no R1. São idênticos aos da v1 no enunciado e no bloco.
- **Reprovação final: 0/30 = 0,0%** (limite 30%). No acumulado do rito (R1 + R2), também 0/30. Sem GATE.
- Itens aprovados no R1 e mudados sem pedido: **nenhum**.
- Conferências do despacho:
  - (1) AJ-1 a AJ-8 por substituição exata, sem efeito colateral no texto (rótulo do AJ-1 incluído): **CONFERE**.
  - (2) 29 itens idênticos aos da v1: **CONFERE**.
  - (3) Resposta à R1: **CONFERE**, com 1 ressalva (R.5, "demais contagens"; ver (4)).
  - (4) seção 4 refeita contra o arquivo: **NÃO CONFERE em 1 linha** — 4.6, L3-3 (l. 891), afirma «prefixo comum de 40 ou mais caracteres entre enunciados: nenhum»; com o AJ-1, D3-R68 × D3-R69 têm prefixo comum de 46 caracteres. Sem efeito em item, gabarito, contagem de aprovação ou na regra L3-3 (seção 5). As sequências, 4.1, 4.3 e 4.4 **conferem**.
  - (5) toda mudança fora dos itens declarada na R.4: **CONFERE**.
- **NÃO CONFERE: 1** (a linha L3-3 da 4.6; registro sem errata, seção 8, item 1). Há outros registros sem efeito (seção 8).

## 2. Conferência (1) — AJ-1 a AJ-8 aplicados por substituição exata, sem efeito colateral
Textos dos AJ: R1, seção 5 (l. 137–144).

| AJ | campo | "substituir" na v1 | "por" na v1 | "substituir" na v2 | "por" na v2 | veredito |
|---|---|---|---|---|---|---|
| AJ-1 | enunciado (seção 1) | 1 | 0 | 0 | 1 (l. 106) | **APLICADO** |
| AJ-2 | Ponto de julgamento | 1 | 0 | 0 | 1 (l. 285) | **APLICADO** |
| AJ-3 | Justificativa (linha 2) | 1 | 0 | 0 | 1 (l. 291) | **APLICADO** |
| AJ-4 | Troca | 1 | 0 | 0 | 1 (l. 295) | **APLICADO** |
| AJ-5 | 4.5, tabela de pontos | 1 | 0 | 0 | 1 (l. 796) | **APLICADO** |
| AJ-6 | 4.6, palavras por item | 1 | 0 | 1, só na R.2 (l. 20), como citação | 2: l. 899 e R.2 (l. 20) | **APLICADO** |
| AJ-7 | 4.6, L5-1 | 1 | 0 | 1, só na R.2 (l. 21) | 2: l. 897 e R.2 (l. 21) | **APLICADO** |
| AJ-8 | bloco 5, item (9) | 1 | 0 | 2, só na R.2 (l. 22) e na R.4 (l. 66), como citação | 3: l. 948, R.2 e R.4 | **APLICADO** |

- Aplicados os 8 AJ em memória à v1, os 30 enunciados e os 30 blocos ficam iguais aos da v2 (30/30 e 30/30). Fora da "Resposta à R1", o texto em memória difere da v2 só nas l. 1, 3, 5 e 944, todas declaradas na R.4 (seção 6).
- **Rótulo «**D3-R68.**» (AJ-1; R.2):** o "antes" e o "por" do AJ-1 começam pelo mesmo rótulo, e a substituição literal o conserva uma vez. Na v2, «**D3-R68.**» ocorre 2 vezes: no item (l. 106) e na citação da R.2 (l. 15). «**D3-R68.** **D3-R68.**» ocorre 0 vez. O tratamento declarado é o que a substituição exata produz: **CONFERE**. O mesmo vale para o rótulo "- Troca: " do AJ-4 (nos dois lados) e para o AJ-3 (sem rótulo nos dois lados; a substituição é só do texto depois de "- Justificativa (linha 2): ").
- Efeito colateral no texto: **nenhum**. No bloco do D3-R68 (l. 283–297) mudam só Ponto, Justificativa (linha 2) e Troca. Ficam iguais: itemEdital, Formato SUJ, Moldura N, Aderência direta, Gabarito E, Justificativa (linha 1), Tipo de base, Base, Mecanismo E3, Difere de, Marcas (TS=sim) e o cabeçalho com [TS].
- Efeito do AJ-1 em medida da seção 4 que o R1 não previu: o prefixo comum com o D3-R69 (seção 5, linha L3-3). É falha de previsão do R1, não da aplicação.
- Origem única: o estilo não tem AJ. A regra de texto igual (ficha 11.3) não se aplica.

## 3. Veredito do D3-R68
| id | folha | gab. | [TS] | enunciado da v2 (lido inteiro) | base (adendo; cópia; página de 22/10) | veredito |
|---|---|---|---|---|---|---|
| D3-R68 | 5.1 | E | sim | «De acordo com a Constituição Federal, compete privativamente aos Ministros de Estado exercer a direção superior da administração federal.» | CF, art. 84, caput e II (adendo de 22/10, 4.1, l. 106; cópia l. 1036 e 1038): «Compete privativamente ao Presidente da República:» […] «II - exercer, com o auxílio dos Ministros de Estado, a direção superior da administração federal;»; 1 ocorrência na página de 22/10 | **APROVADO** |

Fundamentação:
1. **Gabarito E firme pela letra do art. 84, caput e II.** A letra dá a direção superior da administração federal, privativamente, ao Presidente da República; os Ministros só auxiliam. O item a atribui, privativamente, aos Ministros. É contradição expressa (regra 8), não "E por ausência". «Direção superior» ocorre uma só vez na CF (cópia e página), e só para o Presidente: não há outro dispositivo que torne o item verdadeiro.
2. **Uma troca, de um elemento.** A troca é o titular (Presidente → Ministros de Estado), um SUJ. A omissão de "com o auxílio dos Ministros de Estado" retira condição verdadeira e não abre segundo ponto de erro (L5-1, complemento: manter só o que dá contexto). A Troca do bloco (AJ-4) descreve exatamente o que o enunciado faz.
3. **As duas pistas do R1 saíram.** O Presidente não é mais posto como auxiliar dos Ministros (ficha 10.2, item 6), e o enunciado não remete ao art. 84, II. A abertura "De acordo com a Constituição Federal" é a mesma do D3-R69 (C) e de outros itens: não marca gabarito.
4. **Tentação legítima.** Os Ministros são atores da fonte (art. 84, II; art. 76, cópia l. 1017: «auxiliado pelos Ministros de Estado») e exercem «orientação, coordenação e supervisão» na área de sua competência (art. 87, parágrafo único, I; cópia l. 1090). Quem confunde supervisão ministerial com direção superior marca C. O item mede esse conhecimento.
5. **Forma.** 19 palavras (por espaços), no piso da faixa de E da base (19 a 62; L5-1): "Itens E abaixo de 19 palavras: nenhum" continua verdadeiro. Declarativo, sem moldura, sem absoluto inserido ("privativamente" é letra do caput), sem negação, sem contraste, sem fórmula. Formato SUJ mantido (a ficha 13.4.4 dá SUJ). A coluna "o que se julga" da ficha 13.4.4 trazia "com o auxílio do Presidente"; a coluna é sentido, não redação (ficha 12.3): sem errata da ficha.
6. **Justificativa (linhas 1 e 2) e Ponto:** verdadeiros e com lastro no adendo. **Base:** a nota «os atores do item (Presidente da República e Ministros de Estado) são os da fonte» ficou imprecisa depois do AJ-1 (o item só nomeia os Ministros); a regra que ela invoca (10.2, item 6) continua cumprida. Registro (seção 8, item 3).
7. **Sequência e notas:** gabarito e [TS] não mudam; a nota (cj) (D3-R68 × D3-R69 × D3-R66) continua pertinente e cobre o par de prefixo comum da seção 5.
8. **Estilo Cebraspe:** afirmação única, julgável, sem generalização injustificada.

## 4. Conferência (2) — os 29 itens não alterados
**CONFERE.** Na comparação por id, 29 enunciados (seção 1) e 29 blocos (seção 2) são idênticos aos da v1; só o D3-R68 difere, e só pelo texto dos AJ-1 a AJ-4. A seção 3 (proveniência, l. 627–690) é idêntica à da v1 (fora do diff). Os 29 ficam APROVADOS, como no R1, seção 2.

## 5. Conferência (4) — seção 4 refeita contra o arquivo (script próprio sobre a v2 e a v1)
| verificação | refeito pela QA (v2) | declarado na v2 | resultado |
|---|---|---|---|
| gabarito da leva | 15 C / 15 E (50,0%; faixa 12–18); folhas 5/5, 6/4, 4/6 | igual (seção 0; R.6) | CONFERE |
| sequência de gabarito | CECCEECEEC·CCECEECECC·EEECEECECC | igual à v1, à 4.3 e à ficha 13.4.7 | CONFERE |
| sequência de [TS] | nTnnTTnTTn·nnTnTTnTnn·TnnnTTnTnn | igual | CONFERE |
| teste da regra 6 (não refeito pela produção; refeito aqui) | passa na leva, nas 3 folhas da leva e nas 3 folhas acumuladas com os canônicos da 13.4.7 (5.1 ECCEECEECC / TTnnTnTTnn; 6.1 ECECCEECEC / TTnnnTTnTn; 7 EECCECEECC / TTnnnTTTnn), no gabarito e no [TS] | 4.3 idêntica à v1 | CONFERE |
| 4.1 e 4.4 (não refeitas pela produção) | os campos de que dependem (gabarito, [TS], formato, moldura, aderência) são idênticos nos 30 blocos da v1 e da v2; valores conferidos no R1, seção 6, (1) a (3) | idênticas à v1 (fora do diff) | CONFERE |
| [TS] / Troca | 13, todos E; Troca ⇔ [TS] ⇔ "TS=sim" em 30/30; 0 C-isca; E sem [TS]: D3-R81 e R82 (E5) | igual | CONFERE |
| formatos | leva DEF/SUJ/SIT/NUM/PAR/APL 6/4/8/4/6/2 | igual (R.6) | CONFERE |
| mecanismos | C2 13, C3 1, C6 1, E1 4, E3 9, E5 2 | igual (R.3) | CONFERE |
| moldura / aderência | 0 C / 2 E (D3-R77, R85); 22 diretos / 8 parciais | igual | CONFERE |
| abertura × gabarito | CQ 6 C / 4 E; declarativos 9 C / 11 E (D3-R68 continua DC) | igual | CONFERE |
| fórmula | 3 dos 10 CQ (D3-R65, R77, R86) | igual | CONFERE |
| extensão | 30 contagens = linha "Palavras por item" (cadeia exata presente); D3-R68 19; E 19–53 (soma 552, média 36,80); C 13–47 (soma 521, média 34,73); v1: E 25–53, soma 562, média 37,47 | iguais (l. 897, 899; R.5) | CONFERE |
| **L3-3 (prefixo comum)** | D3-R68 × D3-R69: **46 caracteres** («De acordo com a Constituição Federal, compete »). Na v1, o maior par da 5.1 (canônicos + leva) era D3-R62 × D3-R64, 35. Na v2, D3-R68 × D3-R69 passa a ser o maior | l. 891: «Pares da mesma folha (canônicos + leva 7) com prefixo comum de 40 ou mais caracteres entre enunciados: nenhum.» | **NÃO CONFERE** |
| linha 1 / última linha | "# DA_reforco_leva7_v2.md — T-116 — 2026-10-22 — gerado por gcb-cpp" / "FIM DA LEVA 07 — REFORÇO DA" com LF | — | CONFERE |

Leitura da linha que não confere:
- A afirmação da l. 891 era verdadeira na v1 e ficou falsa com o AJ-1. A produção não a refez: a lista do que o script recalculou (R.5) não inclui o prefixo da L3-3, mas a R.5 diz que "demais contagens" não mudam. Essa frase da R.5 fica inexata nesse ponto.
- **A regra L3-3 não é violada.** Ela trata de cenário literal idêntico até o fecho (ficha 9.3, item 3). O prefixo comum é só a fórmula de abertura e o verbo; os itens divergem logo depois ("privativamente aos Ministros … direção superior" × "ao Ministro de Estado, além de outras atribuições … expedir instruções"). E o par já tem a nota (cj) de não pôr no mesmo simulado. O C do D3-R69 não entrega o E do D3-R68, nem o contrário.
- Efeito: nenhum em item, gabarito, [TS], contagem ou aprovação. A seção 4 não vai ao pacote.json. Depois do R2 não há v3 (ficha 1, regra 15); vale o valor certo registrado na reconciliação (precedentes das fichas 11.3 e 12.3). Sem errata.

## 6. Conferência (5) — toda mudança fora dos itens está declarada na R.4
| local (v2) | mudança (diff) | declarada na R.4? |
|---|---|---|
| l. 1 | v1 → v2 no nome do arquivo | sim, (1) |
| l. 3 | «Esta é a v1 (gcb-cpp, primeira produção da leva; despacho de origem» → «Esta é a v2 (gcb-cpp, rodada de correção: R1 com AJ-1 a AJ-8 (D3-R68) e auditoria de estilo sem AJ, conforme a seção “Resposta à R1”; despacho de origem»; o resto do parágrafo é igual (comparação por caractere) | sim, (2), com o texto exato |
| l. 5 | linha de entradas: acrescidos no fim v1 (fdafc3bd…a0ed), R1 (f65132cf…a2ab) e estilo (fd59ea46…98e1); valores corretos | sim, (3) |
| l. 8–71 | seção "Resposta à R1", antes da seção 0 (l. 72) | sim, (4) |
| l. 106, 285, 291, 295 | enunciado, Ponto, Justificativa (linha 2) e Troca do D3-R68 | são os AJ-1 a AJ-4 |
| l. 796 (4.5) | linha do D3-R68 | sim, (5) (AJ-5) |
| l. 897, 899 (4.6) | "E da leva de 19 a 53"; "D3-R68 19;" | sim, (6) (AJ-7, AJ-6); nenhuma outra frase nova na seção 4: confere |
| l. 944 (bloco 5, Arquivo) | v1 → v2 no nome | sim, (7) |
| l. 948 (bloco 5, item (9)) | "E de 25 a 53" → "E de 19 a 53" | sim, (8) (AJ-8) |

- Nenhuma mudança fora da lista. O diff tem exatamente os 13 blocos da seção 0, (a).
- Seções 0, 3, 4.1 a 4.4, 4.7, 4.8 e 6, o resto do bloco 5 (inclusive a dúvida (iv)) e a última linha não mudam, como a R.4 diz: CONFERE.
- Sem mudança não declarada, também não há mudança que devia ter sido feita e foi declarada como feita. A linha L3-3 da 4.6 é o caso inverso (não mudou e devia ter mudado), tratado na seção 5.

## 7. Conferência (3) — Resposta à R1
**CONFERE**, com a ressalva da seção 5.
- **R.1:** os números do R1 (29 / 1 / 0; 0,0%; 8 de 8; 8 parciais aceitos) e do estilo (5 itens, 5 CONFORMES, 0 AJUSTE, 0 NÃO CONFORME) estão corretos.
- **R.2:** os 8 AJ estão transcritos com o texto do R1. Antes 1 e depois 0 na v1, nos 8: confere (seção 2). O tratamento dos rótulos (AJ-1, AJ-3, AJ-4) confere. A remissão "seção 8 e lista de AJ" do R1 é imprecisa: os textos estão na seção 5 do R1, e a seção 8, item 1, só manda aplicá-los. Sem efeito. A leitura do enunciado resultante confere com a seção 3 deste parecer, inclusive a tentação do art. 87, parágrafo único, I, que a R.2 deixou para o R2.
- **R.3:** (1) D3-R64 mantido com E3, como o R1 disse ("fica o declarado"): confere. (2) dúvida (iv) e 6.4: ver a seção 9 deste parecer. (3) registro do estilo sobre o D3-R75 transcrito fielmente: ver a seção 10. (4) demais registros: conferem com o R1, seções 7 e 8.
- **Tabela item a item (30 linhas):** os 29 "mantido" não mudaram de fato; o D3-R68 está descrito como alterado pelos AJ-1 a AJ-5, com AJ-6 a AJ-8 nas seções 4.6 e 5. As remissões ao R1 conferem.
- **R.4:** conferida contra o diff (seção 6).
- **R.5:** soma e média de E (562 → 552; 37,47 → 36,80) e faixa e média de C (13–47; 34,73) conferem por recontagem. Ressalva: a frase "Não mudam: … sequências, seção 0 e demais contagens" fica inexata para o prefixo da L3-3 (seção 5). As sequências não mudaram de fato (seção 5).
- **R.6:** conferida por recontagem.

## 8. Registros (sem veredito e sem efeito; à reconciliação)
1. **4.6, L3-3 (l. 891):** o valor certo, depois do AJ-1, é: na 5.1 (canônicos + leva 7), um par com prefixo comum de 40 ou mais caracteres, D3-R68 × D3-R69 (46; «De acordo com a Constituição Federal, compete »), sem cenário idêntico até o fecho e coberto pela nota (cj). Falha de previsão do R1 (AJ-1, seção 5: "nenhum [efeito] em … abertura"), não da produção na aplicação. Sem errata (fichas 11.3 e 12.3).
2. **Remissão da R.2** ("seção 8 e lista de AJ" do R1): os textos estão na seção 5 do R1. Campo que não vai ao pacote.json.
3. **Nota da Base do D3-R68 (l. 293):** «os atores do item (Presidente da República e Ministros de Estado) são os da fonte (ficha, 10.2, item 6)». Depois do AJ-1 o item só nomeia os Ministros. A nota continua verdadeira no que importa (o ator posto no item é mencionado pela fonte), mas a lista dos "atores do item" ficou maior que o item. O R1 não a incluiu nos AJ. Se a GCB quiser harmonizar na consolidação, por errata com substituição exata (ficha 7.6; não muda Troca, gabarito nem construção): substituir «os atores do item (Presidente da República e Ministros de Estado) são os da fonte» (1 ocorrência na v2) por «o ator posto no item (Ministros de Estado) é mencionado pela fonte». Sem efeito no veredito.
4. **Coluna da ficha 13.4.4 do D3-R68** ("com o auxílio do Presidente"): o enunciado final não traz essa parte. A coluna é sentido, não redação (ficha 12.3). Sem errata da ficha.
5. **Rede (checklist, item 3):** quatro URLs citadas reabertas (seção 0), todas HTTP 200, com bytes iguais aos do Anexo/adendo.

## 9. Pendência declarada pela produção — dúvida (iv) do bloco 5 e item 1 da 6.4
**Leitura: é só registro. Não pede AJ, errata nem v3.**
- O que está no texto: a dúvida (iv) (l. 952) diz «o E troca os dois atores da letra (Presidente × Ministros de Estado) … “Ministros … com o auxílio do Presidente” pode ser lido como implausível à primeira leitura … a gcb-cqfp julga». O item 1 da 6.4 (l. 980) só lista «(iv) D3-R68» entre as dúvidas pendentes; ele não descreve o item. Quem descreve a versão da v1 é só a dúvida (iv).
- Por que é só registro:
  - (a) A dúvida foi feita sobre a v1 e é uma pergunta à QA. O R1 a respondeu (seção 7: ajuste) e a v2 aplicou os AJ. O texto da pergunta continua verdadeiro como registro do que se perguntou, e a R.3, item 2, diz que se deve ler assim.
  - (b) O bloco à GCB e a 6.4 não vão ao pacote.json, e rótulos e textos desses campos não são harmonizados depois do R2 (ficha 10.3, segundo registro).
  - (c) O R1 não pediu a mudança (o AJ-8 tocou só o item (9)), e a produção não podia mudar além dos AJ sem declarar (ficha 4.3). Não mudar foi o correto.
- O que a reconciliação deve fazer: dar a dúvida (iv) e o item 1 da 6.4, no que toca o D3-R68, como **resolvidos** pelo R1 (AJ-1 a AJ-8) e por este R2 (seção 3: APROVADO). O D3-R68 final já não tem o Presidente como auxiliar.

## 10. Registro do estilo sobre a justificativa, linha 2, do D3-R75
Texto (v2, l. 401): «O item troca “uma quinta parte” por “um terço”, teto maior, o que contradiz o limite da letra; a tentação é lembrar de outro limite de desconto fora desta lei (o valor “terço” não ocorre na Lei 4.619).»

**Leitura da gcb-cqfp: o estilo tem razão. A oração «a tentação é lembrar de outro limite de desconto fora desta lei» afirma, sem fonte, que existe outro limite de desconto em outra norma.** O R1 marcou a coluna J do D3-R75 como ✓ e não viu isso; a falha é do R1.
- **O item continua APROVADO.** O enunciado, o gabarito (E pela letra do art. 6º: «não excederá de uma quinta parte»; página de 22/10: 1 ocorrência), a Troca, a Base e a linha 1 da justificativa estão certos. A parte final da linha 2 («o valor “terço” não ocorre na Lei 4.619») tem lastro: 0 ocorrência na cópia e na página. A oração sem fonte não decide o gabarito nem entra no enunciado.
- **Pela ficha 4.2, seria ajuste, e não reprovação** ("justificativa … com afirmação fora da base"). Este R2 não abre AJ novo sobre item não alterado (ficha 4.3: o R2 examina só os AJ e o que a v2 mudou; regra 15: no máximo 2 rodadas). Não há v3.
- **Pela gate do CLAUDE.md** (afirmação sobre norma sem fonte datada depois do QA2 vai para "pendente" no RECONCILIADO, nunca aprovada), a oração **não pode ser dada como texto aprovado**. A reconciliação a registra como **pendente**, e não o item. Isso não conta como reprovação.
- Saída que cabe na ficha 7.6 (errata depois do R2, por substituição exata na consolidação; não muda Troca, gabarito nem construção): substituir «; a tentação é lembrar de outro limite de desconto fora desta lei (o valor “terço” não ocorre na Lei 4.619).» (1 ocorrência na v2) por «; o valor “terço” não ocorre na Lei 4.619, cujo único limite de desconto é o do art. 6º.». O texto novo só diz o que a cópia e a página mostram («desconto» ocorre 1 vez na lei, no art. 6º; «terço» 0 vez). A decisão é da GCB. Se ela não adotar a errata, a oração fica pendente e não entra no pacote.

## 11. Tabela-resumo dos 30 itens (v2)
| id | folha | ponto | gab. | [TS] | formato | moldura | aderência | R1 | R2 |
|---|---|---|---|---|---|---|---|---|---|
| D3-R60 | 5.1 | Lei 9.784, art. 13, caput e III | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico à v1) |
| D3-R61 | 5.1 | Lei 9.784, art. 13, caput e I | E | sim | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R62 | 5.1 | Lei 9.784, art. 14, caput | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R63 | 5.1 | Lei 9.784, art. 14, § 1º | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R64 | 5.1 | Lei 9.784, art. 17 | E | sim | PAR | N | direta | APROVADO | APROVADO (idêntico; E2 × E3 registrado) |
| D3-R65 | 5.1 | CF, art. 84, VI, b | E | sim | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R66 | 5.1 | CF, art. 84, parágrafo único | C | não | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R67 | 5.1 | CF, art. 84, parágrafo único (IV como contraste) | E | sim | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R68 | 5.1 | CF, art. 84, caput e II | E | sim | SUJ | N | direta | APROVADO COM AJUSTE (AJ-1 a AJ-8) | **APROVADO** (AJ-1 a AJ-8 aplicados; registros 1 e 3 da seção 8) |
| D3-R69 | 5.1 | CF, art. 87, parágrafo único, II | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R70 | 6.1 | CC, art. 41, caput e IV | C | não | DEF | N | parcial | APROVADO | APROVADO (idêntico) |
| D3-R71 | 6.1 | CF, art. 136, § 1º, caput e II | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R72 | 6.1 | CC, art. 42 (art. 41 como contraste) | E | sim | PAR | N | parcial | APROVADO | APROVADO (idêntico) |
| D3-R73 | 6.1 | Lei 4.619, art. 1º, caput | C | não | SIT | N | parcial | APROVADO | APROVADO (idêntico) |
| D3-R74 | 6.1 | CF, art. 5º, XXV | E | sim | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R75 | 6.1 | Lei 4.619, art. 6º | E | sim | NUM | N | parcial | APROVADO | APROVADO (idêntico; oração da justificativa, linha 2, pendente na reconciliação, com errata proposta: seção 10) |
| D3-R76 | 6.1 | Decreto 20.910, art. 6º | C | não | NUM | N | parcial | APROVADO | APROVADO (idêntico) |
| D3-R77 | 6.1 | Decreto 20.910, art. 4º, caput | E | sim | APL | S | parcial | APROVADO | APROVADO (idêntico) |
| D3-R78 | 6.1 | Lei 4.619, art. 4º, caput | C | não | SUJ | N | parcial | APROVADO | APROVADO (idêntico) |
| D3-R79 | 6.1 | Decreto 20.910, art. 8º | C | não | NUM | N | parcial | APROVADO | APROVADO (idêntico) |
| D3-R80 | 7 | Lei 8.429, art. 2º, caput | E | sim | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R81 | 7 | Lei 8.429, art. 8º, caput | E | não (E5) | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R82 | 7 | Lei 8.429, art. 12, § 9º | E | não (E5) | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R83 | 7 | Lei 8.429, art. 1º, § 2º | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R84 | 7 | Lei 8.429, art. 13, § 3º | E | sim | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R85 | 7 | Lei 8.429, art. 21, caput e II | E | sim | APL | S | direta | APROVADO | APROVADO (idêntico) |
| D3-R86 | 7 | Lei 8.429, art. 7º, caput | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R87 | 7 | Lei 8.429, art. 23, § 1º | E | sim | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R88 | 7 | Lei 8.429, art. 20, § 2º | C | não | NUM | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R89 | 7 | Lei 8.429, art. 3º, § 2º | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |

Percentual de reprovados: **0/30 = 0,0%**. APROVADO: 30 (100%). REPROVADO: 0.

## 12. Notas à GCB (sem decisão desta QA)
1. A leva segue para a reconciliação e o gatilho A. Há 8 ajustes na rodada (AJ-1 a AJ-8, todos do D3-R68, do R1); o estilo não teve AJ.
2. Para a reconciliação:
   - a linha L3-3 da 4.6 que não confere (seção 5; registro 1);
   - a pendência (iv)/6.4, a dar como resolvida (seção 9);
   - a oração da justificativa, linha 2, do D3-R75, como pendente, com errata proposta (seção 10);
   - a nota da Base do D3-R68, com errata opcional (registro 3).
3. Continuam os registros do R1, seção 8, item 3: 8 parciais da 6.1 aceitos; D3-R81 e R82 sem [TS]; E2 no D3-R64; contagem de "somente"; reabertura como conferência e T-120 em janeiro.
4. Notas de simulado: como no R1, seção 8, item 2; (ci) e (cl) obrigatórias; (cj) cobre também o par de prefixo D3-R68 × D3-R69.
5. Núcleo (ficha 13.1): os 30 itens ficam false, como na v1.

FIM DO PARECER QA R2 — LEVA 7 — REFORÇO DA
