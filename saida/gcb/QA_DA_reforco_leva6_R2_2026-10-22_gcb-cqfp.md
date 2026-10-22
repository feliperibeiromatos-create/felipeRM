# QA_DA_reforco_leva6_R2_2026-10-22_gcb-cqfp.md — T-116 — 2026-10-22 — gerado por gcb-cqfp

# PARECER QA R2 (ÚLTIMA RODADA) — REFORÇO DA, LEVA 6 (v2) — ciclo s16c4
A gcb-cqfp (opus) faz este QA de forma independente. Ela não produziu o texto revisado e não reescreve itens. Nenhum outro arquivo do repositório foi alterado; não houve commit nem push.

O exame segue:
- a ficha, seção 4.3: "o R2 confere cada AJ aplicado literalmente e examina só o que a v2 mudou além dos AJ";
- o R1, seção 8, item 1 (nenhum AJ; qualquer outra mudança é examinada no R2);
- a ficha, seção 9.3, item 6: o AJ da auditoria de estilo vai para a v2 e é conferido aqui;
- a auditoria de estilo, seção 5, "O que o R2 confere", itens 1 a 3.

Pontos examinados:
- o AJ-L6-E1 do estilo (D2-R73), único ajuste da rodada;
- os 29 itens não alterados;
- a Resposta à R1 (R.1 a R.6);
- a seção 4 refeita, contra o arquivo;
- toda mudança fora dos itens, contra a lista da R.4.

## 0. Objeto, entradas e método
| objeto | SHA-256 (em disco, 22/10/2026) |
|---|---|
| saida/gcb/DA_reforco_leva6_v2.md (objeto do R2; 30 itens; 141.300 bytes; 927 linhas) | 0b8ccd4d07bf7d97cb9c1728c6bf4c18e3c5f7c9ac557e27f4537c068c96090b (= despacho) |
| saida/gcb/DA_reforco_leva6_v1.md (objeto do R1; base do diff; 873 linhas) | 8ba2bb6378f196a7811a43cd47927447b674c9f40a51421f94a97c073bd3bf87 (= despacho e R1) |
| saida/gcb/QA_DA_reforco_leva6_R1_2026-10-22_gcb-cqfp.md | 12aefbd9e5c99986b85b284427a9c197ef68725c6d3b1c52c2111c9ed9733626 (= despacho) |
| saida/banco/estilo_DA_reforco_leva6.md | 495750313bfc76d9c98d90b96610456bc2859d42d7a2c1dececa98793a4443b8 (= despacho) |
| saida/gcb/DA_reforco_ficha_2026-10-20.md | 8a86e4bdb816824cc3e7e0c63991c5bd012021a2b02cbdf160416cce66c0eb6c (= despacho) |
| saida/gcb/D2_anexo_N_mapa_normativo.md (qa-normativo-da, T-75) | b0a54fff4ddcf21a693e01ba71032efccf72e0a6fdf912221ff05413cc0e340a (= R1) |
| normativo_cache/Lei_8112_1990_compilada_2026-10-20.txt | 72f45d30dcf096207898d143ba551758e3ffac89e87d6dd2d42044fe65202efe (= R1) |
| normativo_cache/Lei_9784_1999_2026-10-20.txt | f9452916c03521a8435caae49c8feb690ae2b02086424b641204374f38f9ae19 (= R1) |
| saida/pacote/pacote.json v1.13 | 82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240 (= R1) |

Também foram lidos:
- da ficha, as seções 4 (4.1 a 4.4), 9.3, 10.2, 11.2, 11.3, 12.2, 12.3 e 12.5;
- regras/ e CLAUDE.md.

Modelo de forma: saida/gcb/QA_DA_reforco_leva5_R2_2026-10-22_gcb-cqfp.md.

Método: scripts próprios em python3 -I, somente leitura, no scratchpad da sessão, fora do repositório.
- (a) `diff` v1 × v2, lido linha a linha: 7 blocos de diferença (l. 1; l. 3; l. 5 → 5–59; l. 72 → 126; l. 791 → 845; l. 839 → 893; l. 843 → 897).
- (b) O AJ-L6-E1, copiado da auditoria (seção 5, l. 153), foi aplicado em memória à v1 por `str.replace(antes, depois, 1)` e o resultado comparado com a v2 por id.
- (c) Os 30 enunciados (seção 1) e os 30 blocos (seção 2) da v1 e da v2 foram comparados por id.
- (d) Refeitos sobre a v2: gabarito e sequência; [TS] e Troca ⇔ [TS]; formatos por folha e na leva; mecanismos; moldura S; abertura × gabarito; fórmula; absolutos por marcador; negação frontal; contrastes; extensão (por espaços, como a v1); prefixo comum do D2-R73 com a leva e com o pacote.json (L3-3); linha 1 e última linha.

**Rede — reabertura no planalto.gov.br (22/10/2026).** Comando: `curl -sS -L -A "Mozilla/5.0"`, com as URLs exatas da coluna Base. O HTML ficou só no scratchpad. O objeto cita **2 URLs distintas** (Fonte 4: 42 + 2 ocorrências; Fonte 6: 22 ocorrências); as duas foram reabertas. Não há terceira URL citada a abrir.

| hora (UTC) | URL | HTTP | bytes | SHA-256 do HTML |
|---|---|---|---|---|
| 2026-10-22T23:00:55Z | https://planalto.gov.br/ccivil_03/leis/l8112compilado.htm (Fonte 4; D2-R73) | 200 | 343.733 (= R1 e Anexo) | 68fa0902368b0fd1c4134660f671a97e6e925d3b85389b47185f1eb58adc9a32 |
| 2026-10-22T23:00:56Z | https://www.planalto.gov.br/ccivil_03/leis/l9784.htm (Fonte 6) | 200 | 74.941 (= R1 e Anexo) | c74088e98a762027ce1434f8c391c384f032086ee607ac7e3fd7a7d0a7acab0e |

O SHA do HTML muda a cada download (R1, seção 1); a comparação é sobre o texto (tags retiradas, entidades resolvidas, espaços normalizados).
- **Lei 8.112:** ocorrem na página: «O indiciado será citado por mandado expedido pelo presidente da comissão para apresentar defesa escrita, no prazo de 10 (dez) dias, assegurando-se-lhe vista do processo na repartição» (art. 161, § 1º; cópia l. 742; Anexo l. 1030); «para, no prazo de cinco dias, apresentar defesa escrita, assegurando-se-lhe vista do processo na repartição» (art. 133, § 2º; cópia l. 654; Anexo l. 942); «II - inquérito administrativo, que compreende instrução, defesa e relatório» (art. 151, II; cópia l. 717; Anexo l. 1005); «II - instrução sumária, que compreende indiciação, defesa e relatório» (art. 133, II; cópia l. 651).
- **Lei 9.784:** art. 1º e art. 42 presentes, iguais à cópia (página em cp1252).

A reabertura é conferência, não base. A Base dos itens continua a consulta de 20/10/2026 (ficha 11.6).

## 1. Veredito geral
- **Leva: APROVADA.**
- O item alterado: **D2-R73 APROVADO** (AJ-L6-E1 aplicado; E firme pela letra do art. 161, § 1º).
- Os 29 itens não alterados ficam APROVADOS, como no R1. São idênticos aos da v1 no enunciado e no bloco.
- **Reprovação final: 0/30 = 0,0%** (limite 30%). No acumulado do rito (R1 + R2), também 0/30. Sem GATE.
- Itens aprovados no R1 e mudados sem pedido: **nenhum**. O D2-R73 mudou só pelo AJ-L6-E1, pedido pelo estilo e conferido aqui (ficha 9.3, item 6).
- Conferências do despacho:
  - (1) AJ-L6-E1 por substituição exata, sem efeito colateral: CONFERE.
  - (2) 29 itens idênticos aos da v1: CONFERE.
  - (3) Resposta à R1: CONFERE.
  - (4) seção 4 refeita contra o arquivo: CONFERE.
  - (5) toda mudança fora dos itens declarada na R.4; seções 0, 3 e 6 idênticas: CONFERE.
- **NÃO CONFERE: nenhuma.** Há 3 registros sem efeito em item, gabarito, contagem ou aprovação (seção 8).

## 2. Conferência (1) — AJ-L6-E1 aplicado por substituição exata, sem efeito colateral
Texto do AJ (estilo, seção 5, l. 153): `AJ-L6-E1 | D2-R73 | enunciado (seção 1) | substituir: «Segundo a Lei nº 8.112/1990, o indiciado, citado por mandado» | por: «Segundo a Lei nº 8.112/1990, na fase de inquérito administrativo do processo disciplinar, o indiciado, citado por mandado»`

| AJ | item / campo | "substituir" na v1 | "por" na v1 | "substituir" na v2 | "por" na v2 | veredito |
|---|---|---|---|---|---|---|
| AJ-L6-E1 (estilo) | D2-R73 / enunciado | 1 | 0 | 1, só na R.2 (l. 13), como citação do "antes" | 2: no item (l. 126) e na R.2 (l. 13) | **APLICADO** |

- "inquérito administrativo": 0 na v1; 3 na v2 (item, l. 126; R.2, duas vezes, como citação). Confere com a R.2.
- Aplicado o AJ em memória à v1, os 30 enunciados e os 30 blocos ficam iguais aos da v2 (30/30).
- Efeito colateral: **nenhum**. O bloco da seção 2 do D2-R73 (l. 491–505) é idêntico ao da v1: Ponto (art. 161, § 1º), Formato NUM, Moldura N, Aderência direta, Gabarito E, Justificativa (linhas 1 e 2), Base, Mecanismo E3, Troca («no prazo de 10 (dez) dias (art. 161, § 1º) → tem prazo de cinco dias»), Difere de e Marcas (TS=sim).
- Origem única: o R1 não pediu ajuste do D2-R73 (R1, seção 4: nenhum AJ). A regra de texto igual (ficha 11.3) não se aplica, como a R.2 diz.
- Extensão (script, por espaços): 30 → 38 palavras, igual à R.2 e ao estilo (seção 5).

## 3. Conferência (2) — os 29 itens não alterados
**CONFERE.** Na comparação por id, 29 enunciados e 30 blocos são idênticos aos da v1; só difere o enunciado do D2-R73, e só pelo texto do AJ. A seção 3 (proveniência, l. 615–669) é idêntica à da v1 (fora do diff).

## 4. Conferência (3) — Resposta à R1
**CONFERE.** As 6 partes batem com o R1 e com o estilo:
- **R.1:** os números do R1 (30/0/0; 0,0%; 8 de 8; nenhum AJ) e do estilo (5 itens, 16,7%; 4 CONFORMES; 1 AJUSTE, D2-R73; 0 NÃO CONFORME) estão corretos. L7-1 a L7-3 não aplicadas, por serem dirigidas às levas seguintes (estilo, seção 6): correto.
- **R.2:** o texto do AJ é cópia literal da auditoria, seção 5; "antes" 1 e "depois" 0 na v1 confere (seção 2). A leitura do enunciado resultante confere com a seção 7 deste parecer.
- **R.3:** (1) a nota (by) fica registrada e não foi inserida no bloco 5 nem na 6.4. O R1 (seção 8, item 2) a dirigiu "à GCB, sem decisão desta QA": a escolha é coerente com o R1. (2) D2-R72 mantido com Mecanismo E3; contagens C2 12, C3 2, E1 4, E3 12 recontadas: confere. (3) demais registros aceitos sem mudança: conferem com o R1, seção 7.
- **Tabela item a item (30 linhas):** os 29 "mantido" não mudaram de fato; o D2-R73 está descrito como "alterado só no enunciado". As remissões ao R1 (dúvidas aceitas, L6-1, CONFORMES da amostra) conferem.
- **R.4:** conferida contra o diff (seção 6).
- **R.5 e R.6:** conferidas por recontagem (seção 5).

## 5. Conferência (4) — seção 4 refeita, conferida contra o arquivo (script próprio sobre a v2)
| verificação | refeito pela QA | v2 | resultado |
|---|---|---|---|
| gabarito da leva | 14 C / 16 E (46,7%; faixa 12–18); folhas 4/6, 5/5, 5/5 | 14/16 | CONFERE |
| sequência | CECEECEEEC·CCECEEECEC·CEEECCECCE | igual à v1, à 4.3 e à ficha 12.4.7 | CONFERE (nenhum gabarito mudou; os testes da regra 6 ficam como no R1) |
| [TS] | 15, todos E; Troca ⇔ [TS]; 0 C-isca; único E sem [TS]: D2-R72 | 15 | CONFERE |
| formatos da leva | DEF/SUJ/SIT/NUM/PAR/APL 6/3/8/4/5/4; 4.2 2/1/2/2/1/2; 4.4 2/1/3/1/2/1; 4.3 2/1/3/1/2/1 | iguais (R.6, 4.7) | CONFERE |
| mecanismos | C2 12, C3 2, E1 4, E3 12 | iguais | CONFERE |
| moldura S | 0 C / 4 E (D2-R54, R58, R65, R77) | igual | CONFERE; DA 50/38 e D2 10/14 como no R1 |
| abertura × gabarito | "Considere que" 7 C / 5 E; declarativos 7 C / 11 E (o D2-R73 continua DC, "Segundo a Lei…") | iguais | CONFERE |
| fórmula "Nessa situação, nos termos d…" | 6 dos 12 CQ (D2-R54, R60, R62, R65, R74, R77) | igual | CONFERE |
| absolutos (L3-2, L6-2) | C literal: R64 somente, R70 sempre, R71 sempre; E literal não trocado: R69 qualquer, R72 qualquer; nenhum E inserido; o acréscimo do D2-R73 não traz absoluto | iguais | CONFERE |
| negação frontal / contrastes | E com "não", "nem" ou "sem": nenhum; ", e não" só em C (R61, R79) | iguais | CONFERE |
| extensão | 30 contagens declaradas = recontadas (30/30); D2-R73 38; E 21–52 (soma 556, média 34,75); C 23–42 (soma 463, média 33,07) | iguais (4.6; R.5) | CONFERE (L5-1); v1: soma E 548, média 34,25, como a R.5 diz |
| L6-1 | 5 trocas de número; 3 para menos (R52, R69, R73), 2 para mais (R54, R65); a citação "o indiciado … tem prazo de cinco dias" da 4.6 (l. 850) continua subcadeia válida, com a elipse | igual | CONFERE |
| L3-3 (prefixo) | maior prefixo comum do D2-R73 novo: 29–30 caracteres ("Segundo a Lei nº 8.112/1990, "), com D2-R76, R79, R80 e com os canônicos D2-59, D2-44, D2-47, D2-54; nenhum cenário idêntico até o fecho | — | CONFERE |
| linha 1 / última linha | "# DA_reforco_leva6_v2.md — T-116 — 2026-10-22 — gerado por gcb-cpp" / "FIM DA LEVA 06 — REFORÇO DA" com LF | — | CONFERE |

Soma e média de palavras dos E não aparecem na seção 4 nem na seção 0 (grep: 0 ocorrência de 548/34,25 na v1). Por isso a única linha da seção 4 que o AJ obriga a mudar é a "Palavras por item", como a auditoria previu (seção 5) e a R.5 confirma.

## 6. Conferência (5) — toda mudança fora dos itens está declarada na R.4
| local (v2) | mudança (diff) | declarada na R.4? |
|---|---|---|
| l. 1 | v1 → v2 no nome do arquivo | sim, (1) |
| l. 3 | «Esta é a v1 (gcb-cpp; despacho do orquestrador» → «Esta é a v2 (gcb-cpp, rodada de correção: … ; despacho de origem do orquestrador»; o resto do parágrafo é igual | sim, (2), com o texto exato |
| l. 5 | linha de entradas: acrescidos no fim v1, R1 e estilo (início…fim) | sim, (3) |
| l. 6–59 | seção "Resposta à R1", antes da seção 0 (l. 61) | sim, (4) |
| l. 126 | enunciado do D2-R73 | é o AJ (seção 2) |
| l. 845 (4.6) | "Palavras por item": só D2-R73 30 → 38 | sim, (5); nenhuma frase nova na seção 4 |
| l. 893 (bloco 5, Arquivo) | v1 → v2 no nome | sim, (6) |
| l. 897 (bloco 5, amostra) | «Auditoria sobre esta v1» → «Auditoria sobre a v1» | sim, (7) |

- **Seções 0, 3 e 6 idênticas:** CONFERE (nenhum bloco do diff cai nas l. 61–71, 615–669 ou 903–925 da v2). Também ficam iguais 4.1 a 4.5, 4.7, 4.8, o restante do bloco 5 e a última linha, como a R.4 diz.
- Nenhuma mudança fora da lista. O diff tem exatamente os 7 blocos da seção 0, (a).
- A mudança (7) é harmonização de rótulo no bloco à GCB **antes** do R2 e declarada; a vedação da ficha 10.3 vale depois do R2. Corrige o registro "esta v1" que o R2 da leva 5 (seção 6) apontou na leva anterior. Sem efeito.

## 7. Veredito do D2-R73
| id | folha | gab. | [TS] | enunciado da v2 (lido inteiro) | base (Anexo; cópia; página de 22/10) | veredito |
|---|---|---|---|---|---|---|
| D2-R73 | 4.3 | E | sim | «Segundo a Lei nº 8.112/1990, na fase de inquérito administrativo do processo disciplinar, o indiciado, citado por mandado expedido pelo presidente da comissão, tem prazo de cinco dias para apresentar defesa escrita, assegurando-se-lhe vista do processo na repartição.» | Lei 8.112, art. 161, § 1º (Anexo l. 1030; cópia l. 742): «O indiciado será citado por mandado expedido pelo presidente da comissão para apresentar defesa escrita, no prazo de 10 (dez) dias, assegurando-se-lhe vista do processo na repartição»; 1 ocorrência na página de 22/10 | **APROVADO** |

Fundamentação:
1. **Gabarito E firme pela letra do art. 161, § 1º.** O item afirma "tem prazo de cinco dias"; a letra dá "10 (dez) dias". Uma só troca, de número, afirmada como valor da regra (L6-1): troca para menos que contradiz a letra.
2. **O acréscimo é verdadeiro e tem lastro no Anexo N.** O processo disciplinar tem a fase "II - inquérito administrativo, que compreende instrução, defesa e relatório" (art. 151, II; Anexo l. 1005; cópia l. 717). O art. 161 está sob a rubrica "Do Inquérito" (Anexo l. 1011; cópia l. 723). A citação para defesa é ato dessa fase. O acréscimo não abre segundo ponto de erro.
3. **Fica fora da hipótese do art. 133, § 2º.** O prazo de cinco dias da defesa escrita é do procedimento sumário (cópia l. 654), cuja fase equivalente é a "instrução sumária" (art. 133, II; cópia l. 651). O sumário não tem fase chamada "inquérito administrativo". O art. 133, § 8º, manda aplicar o Título V ao sumário só subsidiariamente: não transforma a instrução sumária em inquérito nem importa para o inquérito o prazo de cinco dias. O risco de "mais de uma interpretação" (estilo_banca 5.3) que a auditoria apontou fica fechado.
4. **Não cria pista.** O acréscimo não diz o prazo, não cita o sumário nem usa contraste ("e não …"). Quem sabe que o inquérito dá 10 dias e o sumário 5 acerta pelo conhecimento que o item mede: o "cinco" continua sendo vizinho que discrimina.
5. **Forma.** Abertura declarativa, sem absoluto, sem negação, 38 palavras (faixa E 19–62). Nenhum termo do Legislativo. Moldura N mantida. A justificativa (linhas 1 e 2) continua verdadeira e literal. A Base fica no art. 161, § 1º: o acréscimo é contexto, com lastro no Anexo (ver o registro 2 da seção 8).
6. **Estilo Cebraspe:** afirmação única, julgável, sem generalização injustificada.

## 8. Registros (sem veredito e sem efeito; à reconciliação)
1. **SHA abreviado da v1 na linha de entradas (l. 5):** «8ba2bb63…3bf87», com 5 caracteres no fim, contra 4 nas demais entradas e no despacho («…bf87»). O valor é correto (o SHA termina em …bd3bf87); a R.2 traz o valor completo. Campo que não vai ao pacote.json; sem errata (ficha 11.3).
2. **Base do D2-R73:** cita só o art. 161, § 1º. O acréscimo do AJ ("na fase de inquérito administrativo do processo disciplinar") se apoia no art. 151, II, e na rubrica "Do Inquérito", que estão no Anexo N (l. 1005 e 1011), mas não no campo Base. A auditoria (seção 5) aceitou a Base como está, e esta QA concorda: o ponto de julgamento é o prazo do § 1º. Sem AJ.
3. **Nota (bw) D2-R73 × D2-65 e D2-R80:** a justificativa do canônico D2-65 (pacote v1.13) diz «a tentação é confundir com o prazo de 10 dias do indiciado único (§ 1º)», o que entrega o E do D2-R73 se vierem juntos. A nota (bw) já impede o mesmo simulado. Fica registrado o motivo, sem mudança.
4. **Rede (checklist, item 3):** o objeto cita só 2 URLs distintas; as duas foram reabertas (seção 0). Não havia terceira URL a abrir.

## 9. Tabela-resumo dos 30 itens (v2)
| id | folha | ponto | gab. | [TS] | formato | moldura | aderência | R1 | R2 |
|---|---|---|---|---|---|---|---|---|---|
| D2-R51 | 4.2 | Lei 8.112, art. 135, caput | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico à v1) |
| D2-R52 | 4.2 | Lei 8.112, art. 138 | E | sim | NUM | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R53 | 4.2 | Lei 8.112, art. 142, § 2º | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R54 | 4.2 | Lei 8.112, art. 130, § 1º | E | sim | APL | S | direta | APROVADO | APROVADO (idêntico) |
| D2-R55 | 4.2 | Lei 8.112, art. 141, IV (III como contraste) | E | sim | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R56 | 4.2 | Lei 8.112, art. 139 | C | não | NUM | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R57 | 4.2 | Lei 8.112, art. 142, § 1º | E | sim | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R58 | 4.2 | Lei 8.112, art. 132, caput e V | E | sim | APL | S | direta | APROVADO | APROVADO (idêntico) |
| D2-R59 | 4.2 | Lei 8.112, art. 123 | E | sim | DEF | N | direta | APROVADO | APROVADO (idêntico; nota (by) sugerida, à GCB) |
| D2-R60 | 4.2 | Lei 8.112, art. 136 (art. 132, XI) | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R61 | 4.4 | Lei 9.784, art. 20 (art. 18 como contraste) | C | não | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R62 | 4.4 | Lei 9.784, art. 45 | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R63 | 4.4 | Lei 9.784, art. 21 | E | sim | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R64 | 4.4 | Lei 9.784, art. 51, § 1º | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R65 | 4.4 | Lei 9.784, art. 44 | E | sim | APL | S | direta | APROVADO | APROVADO (idêntico) |
| D2-R66 | 4.4 | Lei 9.784, art. 56, § 1º | E | sim | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R67 | 4.4 | Lei 9.784, art. 66, § 2º | E | sim | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R68 | 4.4 | Lei 9.784, art. 26, § 4º | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R69 | 4.4 | Lei 9.784, art. 69-A, caput e I | E | sim | NUM | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R70 | 4.4 | Lei 9.784, art. 68 | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R71 | 4.3 | Lei 8.112, art. 165, § 1º | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R72 | 4.3 | Lei 8.112, art. 174, caput (art. 182, par. ún.) | E | não | DEF | N | direta | APROVADO | APROVADO (idêntico; E2 × E3 à GCB) |
| D2-R73 | 4.3 | Lei 8.112, art. 161, § 1º | E | sim | NUM | N | direta | APROVADO | **APROVADO** (AJ-L6-E1 aplicado) |
| D2-R74 | 4.3 | Lei 8.112, art. 147, par. ún. | E | sim | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R75 | 4.3 | Lei 8.112, art. 154, par. ún. | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R76 | 4.3 | Lei 8.112, art. 182, caput | C | não | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R77 | 4.3 | Lei 8.112, art. 172, caput | E | sim | APL | S | direta | APROVADO | APROVADO (idêntico) |
| D2-R78 | 4.3 | Lei 8.112, art. 158, caput | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R79 | 4.3 | Lei 8.112, art. 167, § 2º | C | não | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D2-R80 | 4.3 | Lei 8.112, art. 164, § 2º | E | sim | SUJ | N | direta | APROVADO | APROVADO (idêntico) |

Percentual de reprovados: **0/30 = 0,0%**. APROVADO: 30 (100%). REPROVADO: 0.

## 10. Notas à GCB (sem decisão desta QA)
1. A leva segue para a reconciliação e o gatilho A. Há 1 ajuste na rodada (AJ-L6-E1, do estilo); o R1 não teve AJ.
2. Registros para a reconciliação: os 4 da seção 8. Nenhum pede errata.
3. Continuam os registros do R1, seção 8, itens 2 e 3: nota (by) sugerida (D2-R59 × D2-R53); desvio de redação do D2-R59; D2-R72 sem [TS] e a observação E2 × E3; reabertura de 22/10 como conferência.
4. As recomendações L7-1 a L7-3 do estilo (seção 6) vão para a ficha da leva 7, se a GCB aceitar. Não têm efeito sobre esta leva.
5. Núcleo (ficha 12.1): os 30 itens ficam false, como na v1.

FIM DO PARECER QA R2 — LEVA 6 — REFORÇO DA
