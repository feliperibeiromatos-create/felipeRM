# QA_DA_reforco_leva6_R1_2026-10-22_gcb-cqfp.md — T-116 — 2026-10-22 — gerado por gcb-cqfp

# PARECER QA R1 — REFORÇO DA, LEVA 6 (v1) — ciclo s16c4
Objeto: saida/gcb/DA_reforco_leva6_v1.md (30 itens: D2-R51 a D2-R60, folha 4.2; D2-R61 a D2-R70, folha 4.4; D2-R71 a D2-R80, folha 4.3, nesta ordem no arquivo). Critérios: ficha saida/gcb/DA_reforco_ficha_2026-10-20.md, seção 4 (4.1 a 4.4), seções 12.4 e 12.5, com as seções 1, 7, 8.2 (itens 4 e 7), 9.3, 10.2, 11.2, 11.6 e 12.2. O adendo 12 prevalece. A gcb-cqfp não produziu este texto e não o reescreve. Todo ajuste vem em texto exato (ficha, seção 4.3). Esta leva não tem errata a conferir (ficha 12.3). Sem commit nem push. Nenhum outro arquivo do repositório foi alterado.

## 0. Resultado
- **APROVADO: 30. AJUSTAR: 0. REPROVADO: 0.**
- **Taxa de reprovação: 0/30 = 0,0%** (limite 30%): sem gate. A leva segue para a v2, que pode ser idêntica à v1 (nenhum AJ).
- Conferências de leva (ficha 4.4): **8 de 8 CONFEREM**. Nenhuma NÃO CONFERE.
- Pontos pedidos pelo despacho, todos julgados na seção 2 e na seção 7:
  - D2-R59 (objeto trocado em relação à ficha): **aceito**. É desvio de redação, e não de sentido (ficha 12.3).
  - D2-R63 ("o qual terá efeito suspensivo"): **aceito**. A nota (br) é **comum, não obrigatória**.
  - D2-R72 (E sem [TS] e sem Troca): **aceito como a ficha manda**. A QA **não pede [TS]** (ficha 12.5, item 2); motivo na seção 2.
  - D2-R55 e D2-R67: **aceitos**.
  - D2-R52, R69 e R73 (trocas para menos, L6-1): **aceitos**. Os três E ficam nítidos.
  - D2-R62 e R75 (C3): **aceitos**.
  - D2-R54 e R65 (trocas para mais): **aceitos**.
  - D2-R77 (E sem o "só" da letra, L5-2): **aceito**.
- Reabertura no planalto.gov.br (seção 1): as Fontes 4 e 6 abriram com HTTP 200 e com o mesmo tamanho em bytes do Anexo N do D2. Os 41 trechos dos 30 itens ocorrem nas páginas de 22/10/2026.

## 1. Entradas (SHA-256 em disco, 22/10/2026), método e rede
| objeto | SHA-256 |
|---|---|
| saida/gcb/DA_reforco_leva6_v1.md | 8ba2bb6378f196a7811a43cd47927447b674c9f40a51421f94a97c073bd3bf87 (= despacho; 131.919 bytes; 873 linhas LF; 0 CR) |
| saida/gcb/DA_reforco_ficha_2026-10-20.md | 8a86e4bdb816824cc3e7e0c63991c5bd012021a2b02cbdf160416cce66c0eb6c (= despacho) |
| saida/gcb/D2_anexo_N_mapa_normativo.md | b0a54fff4ddcf21a693e01ba71032efccf72e0a6fdf912221ff05413cc0e340a (= ficha 12.4.2) |
| saida/gcb/D2_v2_1.md / D1_v2.md | 59cffaa689ea869cd11c13e6a833470b0b91d24b0f25ea2cc2e100ac9be8bd2c / 63bd27c34baec035dd39904ef565f6b5a662c0a30886a4a3d0b13b8b702e3d56 |
| saida/gcb/DA_reforco_leva1_v2.md a leva5_v2.md | 2c431529…4f04 / 5baec20d…1bbe / e4c2a911…3237 / 57203ae3…38da / b531014bcf2cf158890ffa4293062e796e505151a57dced14e8462875a8f81c4 (= D-T116-LEVA1 a LEVA5-ACEITE) |
| normativo_cache/Lei_8112_1990_compilada_2026-10-20.txt | 72f45d30dcf096207898d143ba551758e3ffac89e87d6dd2d42044fe65202efe |
| normativo_cache/Lei_9784_1999_2026-10-20.txt | f9452916c03521a8435caae49c8feb690ae2b02086424b641204374f38f9ae19 |
| saida/pacote/pacote.json v1.13 | 82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240 |
| saida/banco/moldura_ce_itens_2026-10-20.csv | ed4b364dffbca7d9e8878591914783258fa7048c4f1837d98c3d62e34981daac (4.2: D2-52 e D2-53 C; 4.3: D2-61 C; 4.4: D2-74 C) |
| regras/estilo_banca.md | 9f9237f5f9828b77d5ab805849a7a14af13fb28fcc1c985fe462ec1027684caf |
| modelo de forma: QA_DA_reforco_leva5_R1_2026-10-22_gcb-cqfp.md | f2374c2de64e561387a801012de198c21e9ee2ef3abcda5a60da300f02d3205a |

Lidos também: regras/ (PADRAO_UNICO_v1.md, estilo_banca.md, seções 3.1 a 3.12), CLAUDE.md e, em DECISOES.md, D-REFORCO-2 (l. 95), D-MOLDURA-CE (l. 171), D-REFORCO-DA (l. 173) e D-T116-LEVA1 a LEVA5-ACEITE (l. 175 a 179).

Método: li inteiras as seções 0 a 6 da v1 e confrontei cada item com a linha do Anexo N do D2 (seções 3, 4.3 e 4.4) e com a cópia em normativo_cache/.
- Os canônicos das três folhas foram relidos em duas fontes: no pacote.json v1.13 (ordem, gabarito e enunciado) e no D2_v2_1.md, seção 5.2 (formato, [TS] e ponto).
- Os scripts são próprios: python3 -I, somente leitura, no scratchpad da sessão (…/scratchpad/qa6/), fora do repositório.
- check.py confere os 30 blocos e os 13 campos. Também confere os trechos contra a seção do Anexo e contra a cópia (contagem e linha), a URL, a data e o número de palavras por trecho e por enunciado.
- counts.py reconstrói as folhas acumuladas a partir do pacote v1.13 mais a leva 6. Ele refaz o teste da regra 6 e conta formatos com os canônicos, moldura, abertura, fórmula, absolutos, termos do Legislativo e extensão.
- reab.py e reab2.py extraem o texto do HTML reaberto e buscam nele os trechos e as linhas de dispositivo da cópia.

**Rede — reabertura no planalto.gov.br (22/10/2026), como conferência e não como base (ficha 12.4.2, (c)).** Comando: `curl -sS -m 90 -A "Mozilla/5.0" -o <arquivo> -w "%{http_code} %{size_download}" <URL>`, com as URLs exatas do Anexo N do D2, seção 1. O HTML ficou só no scratchpad (…/scratchpad/qa6/html/) e não foi gravado em saida/.

| hora (UTC) | URL | HTTP | bytes (Anexo) | SHA-256 do HTML de 22/10 |
|---|---|---|---|---|
| 2026-10-22T22:51:47Z | https://planalto.gov.br/ccivil_03/leis/l8112compilado.htm (Fonte 4) | 200 | 343.733 (343.733) | fe7a23a781fa9c04b307fef4cb8a038e92db28f170c111407caca31056764092 |
| 2026-10-22T22:51:49Z | https://www.planalto.gov.br/ccivil_03/leis/l9784.htm (Fonte 6) | 200 | 74.941 (74.941) | 9af0e556445d869e064e27c9beae8d05b365b332635c41690f8bc1c07d83e1d9 |

O SHA-256 de hoje difere do Anexo (74a6719e…3c62; 08b38d0b…c6e8), da cópia (781e2936…e60c; 689bbb2d…a4f6) e da reabertura da produção (754f0620…0890; 3776b4aa…eb21), embora os bytes sejam os mesmos. Esse comportamento do Planalto já está registrado no R1 da leva 5. A comparação se fez sobre o texto.

A extração usou html.parser e cp1252, excluiu o tachado e converteu `<sup>o</sup>` em "º". A comparação normalizou espaços e ordinais. Resultados:
- 41 de 41 trechos da coluna Base estão nas páginas de hoje.
- Cópia × página de hoje, linhas de dispositivo: na Lei 8.112, 880 linhas, 1 não casada; na Lei 9.784, 220 linhas, 3 não casadas. As quatro são efeito da limpeza das notas entre parênteses, não diferença de texto, e todas estão fora da leva: art. 76-A da Lei 8.112; art. 56, § 3º, e arts. 64-A e 64-B da Lei 9.784, estes excluídos pela ficha 12.4.2.
- "2025" ocorre 1 vez na página da Lei 8.112, no "(Vide Decreto nº 12.374, de 2025)" do art. 20, que está fora da leva. "2026" não ocorre nas duas páginas.
- Nenhum dispositivo da leva mudou entre 20 e 22/10/2026. A T-120 continua como janela de janeiro (ficha 11.6).

## 2. Veredito por item
Legenda:
- G: gabarito pela letra.
- P: ponto único.
- T: troca legítima e única / [TS].
- F: sem pista de forma.
- Pe: pertinência à folha (Anexo, seção 3).
- Gê: não é gêmeo de canônico da folha, das levas 1 a 5 nem da própria leva.
- M: moldura.
- J: justificativa e proveniência.

Símbolos: ✓ confere. "Anexo l." = linha do Anexo N do D2. "l." = linha da cópia em normativo_cache/.

### Folha 4.2 — D2-R51 a D2-R60 (Anexo N do D2, seção 4.3; Fonte 4; núcleo 4.2 = arts. 121 a 126-A e 127 a 142)
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D2-R51 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota bk) | N ✓ | ✓ | **APROVADO** | Art. 135, caput, literal (Anexo l. 950; l. 662). Cumpre a exigência (b): art. 135 como primeiro ponto da 4.2, com "exercido por não ocupante de cargo efetivo" no enunciado. Nenhum canônico julga o art. 135. |
| D2-R52 | E ✓ | ✓ | [TS] trinta → vinte ✓ | ✓ | direta ✓ | ✓ (nota bl) | N ✓ | ✓ | **APROVADO** | Art. 138 (Anexo l. 955; l. 667). L6-1: o item define o abandono pelo limiar ("configura abandono … por mais de vinte dias"). Por isso, ausências de 21 a 30 dias passariam a configurá-lo, o que contradiz a letra. O E está nítido. |
| D2-R53 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota bm) | N ✓ | ✓ | **APROVADO** | Art. 142, § 2º, literal (Anexo l. 972; l. 684). É um ângulo novo do art. 142; D2-54 e D2-57 julgam os incisos I a III e o § 3º. |
| D2-R54 | E ✓ | ✓ | [TS] 15 → trinta ✓ | ✓ | direta ✓ | ✓ (nota bn) | S ✓ (tipo da cota; fecho neutro) | ✓ | **APROVADO** | Art. 130, § 1º (Anexo l. 919; l. 631). A troca é para mais e contradiz o teto "até 15". O "suspensão de até 30 dias" do art. 141, III, é tentação legítima da própria folha. A moldura não decide o gabarito. |
| D2-R55 | E ✓ | ✓ | [TS] autoridade que fez a nomeação → chefe da repartição e outras autoridades (inciso III) ✓ | ✓ | direta ✓ | ✓ (nota bo) | N ✓ | ✓ | **APROVADO** | Art. 141, III e IV (Anexo l. 965/966; l. 677/678). Dúvida (iv): o trecho "na forma dos respectivos regimentos ou regulamentos" é a letra do inciso III. Ele dá plausibilidade ao ator trocado (10.2, item 6) e não cria ambiguidade, porque o inciso IV dá à destituição uma autoridade própria. O item não nomeia órgão do Legislativo nem afirma norma interna. A troca é única: o bloco de ator do inciso III. |
| D2-R56 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota bl) | N ✓ | ✓ | **APROVADO** | Art. 139, literal (Anexo l. 956; l. 668). |
| D2-R57 | E ✓ | ✓ | [TS] se tornou conhecido → foi praticado ✓ | ✓ | direta ✓ | ✓ (nota bm) | N ✓ | ✓ | **APROVADO** | Art. 142, § 1º (Anexo l. 971; l. 683). E1 nítido. |
| D2-R58 | E ✓ | ✓ | [TS] demissão → suspensão ✓ | ✓ | direta ✓ | ✓ (nota bp) | S ✓ (tipo da cota; fecho neutro) | ✓ | **APROVADO** | Art. 132, caput e V (Anexo l. 923/928; l. 635/640). O cenário é distinto do D2-52 e do D2-R54 (L3-3). Não há negação frontal. |
| D2-R59 | E ✓ | ✓ | [TS] os crimes e contravenções → as infrações disciplinares ✓ | ✓ | direta ✓ | ✓ (nota bq) | N ✓ | ✓ | **APROVADO** | Art. 123 (Anexo l. 901; l. 613). Desvio da coluna da ficha ("inclui" → substitui): ver a seção 7, (i). A substituição é a forma legítima da troca (regra 8). Acrescentar as infrações ao rol, sem retirar os crimes e as contravenções, deixaria o item como "E por ausência", porque o art. 123 não diz "somente". Com a substituição, o item atribui à responsabilidade penal o objeto da administrativa (E1). Observação, sem AJ: o D2-R53, da mesma folha, aplica à infração disciplinar também capitulada como crime o prazo da lei penal. Isso pode inclinar quem o vê junto a marcar C no D2-R59. O gabarito não fica discutível, porque o item fala das infrações disciplinares como categoria. Nova nota sugerida (by) na seção 8. |
| D2-R60 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota bp) | N ✓ | ✓ | **APROVADO** | Art. 136 com o art. 132, XI (Anexo l. 952/934; l. 664/646). O item usa só o inciso XI (dúvida (xii)), e o recorte é verdadeiro. |

### Folha 4.4 — D2-R61 a D2-R70 (Anexo N do D2, seção 4.4; Fonte 6; núcleo 4.4 = Lei 9.784 integral)
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D2-R61 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota bs) | N ✓ | ✓ | **APROVADO** | Art. 20 e art. 18, caput (Anexo l. 1440/1434; l. 91/85). Litígio com o interessado é impedimento (art. 18, III), e inimizade notória é suspeição: o par fica nítido. O C usa o contraste ", e não" (L3-4: 2 C, 0 E na leva). |
| D2-R62 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 45 (Anexo l. 1498; l. 149). O C3 está bem classificado: "antes de ouvir o interessado" é traço de dispensa (estilo_banca 3.9). A paráfrase de "sem a prévia manifestação" é fiel. |
| D2-R63 | E ✓ | ✓ | [TS] sem efeito suspensivo → o qual terá efeito suspensivo ✓ | ✓ | direta ✓ | ✓ (nota br) | N ✓ | ✓ | **APROVADO** | Art. 21 (Anexo l. 1441; l. 92). Dúvida (ii): "o qual terá efeito suspensivo" contradiz frontalmente a regra específica ("sem efeito suspensivo"). O art. 61, parágrafo único, só permite à autoridade dar efeito suspensivo, caso a caso, e não torna verdadeira a afirmação de efeito automático. O relativo "o qual" retoma "recurso" sem ambiguidade. |
| D2-R64 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 51, § 1º (Anexo l. 1554; l. 206). O "somente" é literal (L3-2 e L6-2). |
| D2-R65 | E ✓ | ✓ | [TS] dez → quinze ✓ | ✓ | direta ✓ | ✓ (nota bt) | S ✓ (função administrativa; art. 1º, § 1º, só como cenário) | ✓ | **APROVADO** | Art. 44 (Anexo l. 1497/1362; l. 148/13). A troca é para mais e contradiz o "máximo de dez". A ressalva "salvo se outro prazo for legalmente fixado" é da letra e fala de lei, não de norma interna: a moldura não decide. Os prefixos com D2-74, D2-R47 e D2-R50 ficam abaixo de 40 caracteres (L3-3). |
| D2-R66 | E ✓ | ✓ | [TS] dirigido à autoridade que proferiu a decisão → dirigido diretamente à autoridade superior ✓ | ✓ | direta ✓ | ✓ (nota bu) | N ✓ | ✓ | **APROVADO** | Art. 56, § 1º (Anexo l. 1567; l. 219). O ator trocado é mencionado pela fonte e plausível (10.2, item 6). "A quem cabe apreciá-lo" não acrescenta outro erro. |
| D2-R67 | E ✓ | ✓ | [TS] de modo contínuo → em dias úteis ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 66, caput e § 2º (Anexo l. 1600/1598; l. 252/250). Dúvida (v): a parte final (dia do começo e dia do vencimento) é verdadeira e vem depois da troca. Não dilui o E e não soma exigência que decida sozinha (regra 9). "Dias úteis" está na lei (arts. 23, 26, § 2º, 41 e 62): tentação legítima, E1. O item tem 29 palavras (L5-1) e não usa "apenas". |
| D2-R68 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 26, § 4º, literal (Anexo l. 1466; l. 117). |
| D2-R69 | E ✓ | ✓ | [TS] 60 (sessenta) → cinquenta e cinco ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 69-A, caput e I (Anexo l. 1609/1610; l. 261/262). L6-1: o item afirma a idade como critério da regra, e por isso uma idade menor contradiz a letra. Os incisos II a IV (deficiência, doença grave) não tornam o item verdadeiro, porque o item põe a idade como critério. O "em qualquer órgão ou instância" é literal e não é a troca (L6-2). A redação é de 2009: não leva REVERIFICAR. |
| D2-R70 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 68, literal (Anexo l. 1605; l. 257). O "sempre" é literal. |

### Folha 4.3 — D2-R71 a D2-R80 (Anexo N do D2, seção 4.3; Fonte 4; núcleo 4.3 = arts. 143 a 182, 133 e 140)
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D2-R71 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 165, § 1º, literal (Anexo l. 1041; l. 753). Não é gêmeo do D2-64: lá se julga o poder do julgador; aqui, o relatório. |
| D2-R72 | E ✓ | ✓ | sem [TS] e sem Troca, por ordem da ficha ✓ | ✓ | direta ✓ | ✓ (nota bv) | N ✓ | ✓ | **APROVADO** | Art. 174, caput, e art. 182, parágrafo único (Anexo l. 1065/1079; l. 777/791). O item substitui, de fato, um elemento do art. 174: "a inocência do punido ou a inadequação da penalidade aplicada" → "o agravamento da penalidade aplicada". Essa substituição inverte a finalidade da revisão e não troca um conceito vizinho. O gabarito decorre da vedação expressa do art. 182, parágrafo único, e não de uma omissão do art. 174: E por contradição expressa (regra 8), como nos D2-70 e D2-80. O critério da ficha (12.4.4) é sustentável, e esta QA **não pede [TS]** (12.5, item 2). Assim, o teste de [TS] da 4.3 continua aprovado e não há desvio a registrar. Observação, sem AJ: o Mecanismo E3 se descreveria melhor como E2 (inversão de polaridade ou finalidade). O campo não está na lista da ficha 4.2, e a troca mudaria as contagens da seção 4 sem efeito no item. O "a qualquer tempo" é literal (L6-2). |
| D2-R73 | E ✓ | ✓ | [TS] 10 (dez) → cinco ✓ | ✓ | direta ✓ | ✓ (nota bw) | N ✓ | ✓ | **APROVADO** | Art. 161, § 1º (Anexo l. 1030; l. 742). L6-1: "tem prazo de cinco dias" afirma o valor da regra, e não um teto. O E está nítido. As partes verdadeiras (mandado do presidente da comissão; vista na repartição) dão contexto, e só uma vem antes da troca (L5-1). |
| D2-R74 | E ✓ | ✓ | [TS] cessarão os seus efeitos → continua a produzir efeitos até a conclusão ✓ | ✓ | direta ✓ | ✓ (nota bx) | N ✓ | ✓ | **APROVADO** | Art. 147, parágrafo único (Anexo l. 994; l. 706). A consequência é trocada sem "sem" nem "não" (10.2, item 5). |
| D2-R75 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 154, parágrafo único (Anexo l. 1014; l. 726). O C3 está bem classificado: "independentemente" é o traço "independe" de estilo_banca 3.9. |
| D2-R76 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (notas bk, bv) | N ✓ | ✓ | **APROVADO** | Art. 182, caput (Anexo l. 1078; l. 790). O par destituição convertida × demais declaradas sem efeito é fiel à letra, sem "exceto" nem "mas não". |
| D2-R77 | E ✓ | ✓ | [TS] após → antes ✓ | ✓ | direta ✓ | ✓ | S ✓ (tipo da cota; fecho neutro) | ✓ | **APROVADO** | Art. 172, caput (Anexo l. 1058; l. 770). Dúvida (x): sem o "só", o item afirma permissão ("poderá ser concedida antes"), o que contradiz frontalmente "só poderá … após". O E está nítido e cumpre a L5-2: sem "só" e sem verbo de condição necessária. O parágrafo único (exoneração de ofício convertida em demissão) não alcança a exoneração a pedido. A moldura não decide. |
| D2-R78 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 158, caput, literal (Anexo l. 1021; l. 733). |
| D2-R79 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 167, § 2º, literal (Anexo l. 1048; l. 760). Usa o contraste ", e não" em C (L3-4). |
| D2-R80 | E ✓ | ✓ | [TS] autoridade instauradora → presidente da comissão ✓ | ✓ | direta ✓ | ✓ (nota bw) | N ✓ | ✓ | **APROVADO** | Art. 164, § 2º (Anexo l. 1039; l. 751). A redação é da Lei 9.527/1997: não leva REVERIFICAR. O presidente da comissão aparece na fonte (arts. 156, § 1º, e 161, § 1º) e é plausível (10.2, item 6). |

## 3. Reprovação e substituto
Nenhum item reprovado. Nenhum id vago. Os pontos de reserva das três folhas ficam intactos.

## 4. Ajustes em texto exato (ficha, seção 4.3)
Nenhum AJ. A v2 pode repetir a v1 byte a byte, ou acrescentar só a "Resposta à R1". Se a v2 mudar qualquer coisa além disso, o R2 examina a mudança (ficha 4.3).

## 5. Conferências de leva (ficha, seção 4.4)
| # | conferência | resultado |
|---|---|---|
| 1 | C/E da leva | **CONFERE**. A leva tem 14 C / 16 E (46,7%; faixa 12–18 em 30), na sequência CECEECEEEC·CCECEEECEC·CEEECCECCE, igual à ficha 12.4.7. As folhas fechadas 4.2, 4.4 e 4.3 ficam com 10 C / 10 E cada (faixa 8–12 C). |
| 2 | tetos por folha | **CONFERE**. Formatos da leva por folha iguais à ficha 12.4.4: 4.2 2/1/2/2/1/2; 4.4 2/1/3/1/2/1; 4.3 2/1/3/1/2/1 (DEF/SUJ/SIT/NUM/PAR/APL). Com os canônicos (D2_v2_1.md, campo Formato): 4.2 5/1/4/5/1/4; 4.4 5/1/5/4/3/2; 4.3 5/1/5/4/3/2. O maior formato é 5 de 20 (teto 6). VOLÁTIL 0 e REVERIFICAR 0: as redações são originais, da Lei 9.527/1997 (art. 164, § 2º) ou da Lei 12.008/2009 (art. 69-A). Moldura por folha, contando os canônicos: 4.2 4, 4.4 2, 4.3 2 (≤ 6). Piso de 10 diretos: 20 diretos em cada folha. |
| 3 | moldura acumulada e conjuntos | **CONFERE**. CSV: DA 44/9; D2 9/1 (4.2: D2-52 e D2-53 C; 4.3: D2-61 C; 4.4: D2-74 C). Levas 1 a 5: 6/25 (partida da leva 6: 50/34). A leva 6 tem 0 C / 4 E (D2-R54, R58, R65, R77), todos do tipo "órgão/servidor do Poder Legislativo da União". DA vai a **50/38 (56,8%)** e D2 a **10/14 (41,7%)**, iguais à ficha 12.4.6. Meta da D-MOLDURA-CE: 29 E novos (≥ 21); 100 ≤ 114. As cotas da T-122 (4.2 2 E; 4.3 1 E; 4.4 1 E) estão cumpridas. Não há C com moldura (R3 sem par a exigir). D3, D4 (K1 a K4, fecho neutro, ", e não") e D1 não têm item novo. Termos do Legislativo (Legislativo, Câmara, Congresso, Senado, deputado, parlamentar, plenário, Casa) aparecem só nos 4 itens S. |
| 4 | pontos sem duplicata | **CONFERE**. Os 30 pontos são distintos. Nenhum dispositivo coincide com os pontos já usados da ficha 12.4.3 (canônicos das três folhas e outras folhas e levas) nem com os D2-R01 a R50. Mesmo artigo com outro elemento, todos com "Difere de" e nota: R53 e R57 × D2-54/57; R54 × D2-60; R55 × D2-53; R58 × D2-51; R73 × D2-65; R74 × D2-61; R59 × D3-R06 (art. 124) e D2-47/D3-R31 (art. 125); dentro da leva, R53 × R57 (art. 142, § 2º × § 1º). Nenhum ponto da lista "Fora da leva 6" (12.4.2) foi usado. O art. 1º, § 1º, aparece só como cenário do D2-R65, e o art. 141, III, só como contraste do D2-R55. |
| 5 | exigências da leva | **CONFERE**. Exigência (b): o D2-R51 é o primeiro da 4.2, do art. 135, C, sem [TS]. L4-1: nenhum fecho "é correto afirmar que". Abertura (7.4.2; L3-1): na leva, CQ 7 C / 5 E (58,3% de C) e declarativos 7 C / 11 E (61,1% de E). Nas folhas fechadas: 4.2 CQ 5/3 e DC 5/7; 4.4 CQ 5/2 e DC 5/8; 4.3 CQ 4/3 e DC 6/7, recontadas sobre pacote mais leva. Fórmula (12.2, item 3): 6 dos 12 CQ, 2 por folha (D2-R54, R60, R62, R65, R74, R77). L3-2 e L6-2: C com absoluto literal R64, R70, R71; E com absoluto literal que não é a troca R69, R72; nenhum E com absoluto inserido. L3-3: nenhum cenário idêntico até o fecho. L3-4: ", e não" só em C (R61, R79). L3-5: nenhum "mero", "por si só" ou "simples". L4-3 e L4-4: nenhum E6 e nenhum E3 que condicione hipótese autônoma. 10.2, item 5: nenhuma negação frontal. 10.2, item 6: os SUJ E (R55, R66, R80) usam ator mencionado pela fonte. L5-1: E entre 21 e 52 palavras, C entre 23 e 42, iguais à v1. L5-2: o D2-R77 não usa "só" nem verbo de condição necessária. L6-1: 5 trocas de número, 3 para menos (R52, R69, R73), todas afirmadas como valor ou critério da regra, e 2 para mais (R54, R65). |
| 6 | primeiro e último id por lote | **CONFERE**. D2-R51 a D2-R80 são contínuos, com as faixas por folha da ficha 12.1 (4.2 R51–R60; 4.4 R61–R70; 4.3 R71–R80) e as folhas na ordem 4.2, 4.4, 4.3. Nenhum desses ids está no pacote.json v1.13 nem nas levas 1 a 5 (último anterior: D2-R50). O núcleo é false nos 30 (ficha 12.1). |
| 7 | linha 1 e última linha | **CONFERE**. Linha 1: "# DA_reforco_leva6_v1.md — T-116 — 2026-10-22 — gerado por gcb-cpp". Última linha: "FIM DA LEVA 06 — REFORÇO DA", com LF final. |
| 8 | bases no cache (amostra de 5 ou mais) | **CONFERE**. Os 41 trechos dos 30 itens são subcadeia da seção citada do Anexo (4.3 ou 4.4) e da cópia em cache, 1 vez cada (41/41). Amostra reaberta, com linha da cópia: Lei 8.112 l. 613 (R59), 631 (R54), 677/678 (R55), 770 (R77), 777/791 (R72), 742 (R73); Lei 9.784 l. 92 (R63), 252/250 (R67), 262 (R69), 148/13 (R65). A maior soma de trecho por item é 24 palavras (R54; limite 25). "consulta 20/10/2026" aparece em 30/30. A URL é igual à do Anexo em 30/30; a Fonte 4 vai sem "www", como no Anexo e nas levas 4 e 5. Reaberto o planalto em 22/10 (seção 1), os 41 trechos estão nas páginas. |
| — | teste de sequência (regra 6; 7.3; 12.4.7) | **CONFERE** (counts.py; canônicos na ordem do pacote v1.13; nenhuma das levas 1 a 5 tem item nestas folhas). Passam, no gabarito e no [TS], a leva, as folhas da leva, as folhas acumuladas e o legado. Os valores são iguais aos da v1, seção 4.3. Os mais perto do limite: p5 9/10 no gabarito da leva inteira e da 4.4 acumulada; p6 11/12 no [TS] da 4.2 acumulada; p8 14/16 no [TS] da 4.3 acumulada e da leva. |
| — | integridade dos blocos | **CONFERE**. Os 30 blocos têm os 13 campos. Troca ⇔ [TS] ⇔ "TS=sim" vale nos 15 itens com [TS], todos E; não há C-isca. O único E sem [TS] é o D2-R72, por ordem da ficha. itemEdital P1-DA-<folha>, AUTORAL e QA PENDENTE em 30/30. A seção 1 não traz gabarito, [TS], URL nem marcas. Nenhum "exceto", "R$", "NGP", "Vide" ou "STF" em enunciado. Nenhum autor nomeado. |

## 6. Errata
Nenhuma errata a conferir nesta leva (ficha 12.3).

## 7. Desvios e dúvidas declarados pela produção (seções 5 e 6 da v1)
| # | desvio ou dúvida | avaliação |
|---|---|---|
| (i) / 6.2.1 | D2-R59: "inclui" da coluna da ficha → substituição do objeto | **Aceito.** A coluna "o que se julga" é sentido, não redação (ficha 12.3), e o sentido foi mantido: a responsabilidade penal passa a abranger as infrações disciplinares. A substituição evita o "E por ausência" (regra 8; o art. 123 não fecha o rol com "somente"). Formato, gabarito, [TS], moldura, aderência e posição seguem a ficha. A reconciliação registra o desvio, sem errata da ficha. Sugere-se a nota (by) (seção 8). |
| (ii) / 6.2.2 | D2-R63: "o qual terá efeito suspensivo" | **Aceito** (seção 2). A nota (br) é **comum, não obrigatória**. O D2-74 afirma a regra geral com a ressalva "salvo disposição legal em contrário". Por isso não decide o D2-R63, e o D2-R63 não decide o D2-74. Os dois só se reforçam. |
| (iii) | D2-R72 sem [TS] e sem Troca | **Aceito** (seção 2). A QA não pede [TS], e o teste de [TS] da 4.3 fica aprovado. Não há desvio a registrar pela 12.5, item 2. |
| (iv) / 6.2.3 | D2-R55: "na forma dos respectivos regimentos ou regulamentos" | **Aceito**: é a letra do inciso III, sem ambiguidade e sem afirmar norma interna. |
| (v) | D2-R67: parte verdadeira depois da troca | **Aceito**: não dilui o E. |
| (vi) | D2-R52, R69 e R73: trocas para menos | **Aceito**: os três afirmam o número como valor ou critério da regra (L6-1), e o E fica nítido. |
| (vii) | D2-R54 e R65: trocas para mais | **Aceito**: teto e prazo máximo; o sentido vem da ficha. |
| (viii) | D2-R62 e R75: C3 | **Aceito**: os traços de dispensa e de "independe" estão de acordo com estilo_banca 3.9. |
| (ix) | D2-R61: C com ", e não" | **Aceito**. L3-4 cumprida. |
| (x) | D2-R77: E sem "só" | **Aceito**: E nítido; L5-2 cumprida. |
| (xi) / 6.2.6 | D2-R65: cena "função administrativa" | **Aceito**: a cena é distinta da do D2-74, do D2-R47 e do D2-R50. Fica a nota (bt). |
| (xii) | D2-R60: só o inciso XI | **Aceito**. |
| (xiii) | grafia do host da Fonte 4 | **Registrada** (seção 1). |
| 6.2.4, 6.2.5, 6.2.7 a 6.2.10 | grafia "argüida" fora do enunciado (R61); paráfrase "antes de ouvir" (R62); "diretamente … a quem cabe apreciá-lo" (R66); mecanismos; trechos com "[…]" | **Aceitos**. Os trechos com "[…]" são subcadeias contínuas do lastro e da cópia, e a soma fica ≤ 25 palavras. Mecanismos sem reclassificação (C2 12, C3 2, E1 4, E3 12). A observação do E2 no D2-R72 é registro, sem AJ. |
| 6.1 | 30 linhas iguais à ficha 12.4.4 | **Conferido**: formato, moldura, gabarito, [TS], aderência e abertura, 30 de 30. |

## 8. Lista para a v2 (gcb-cpp) e notas à GCB
1. Não há AJ a aplicar. A v2 pode ser cópia da v1, com a "Resposta à R1" se o rito a pedir. Qualquer outra mudança é examinada no R2 (ficha 4.3). Os AJ de estilo da amostra (D2-R51, R54, R65, R72, R73; ficha 12.4.8), se houver, vão para a v2 e são conferidos no R2 (ficha 9.3, item 6). Texto igual pedido pelo R1 e pelo estilo é aplicado uma vez (ficha 11.3).
2. Notas de simulado, à GCB, sem decisão desta QA:
   - aceitas com os ids finais: (bk) a (bx), (w) e (x), e os acréscimos da produção D2-R65 × D1-54, D2-R61 × D2-R63, D2-R71 × D2-64, D2-R75 × D2-63 e D2-R79 × D2-53, todos comuns;
   - (br) D2-R63 × D2-74: **comum, não obrigatória** (seção 7, (ii));
   - (bq) com o acréscimo do D3-R06 (art. 124), que a produção fez: aceito;
   - nova (by), sugerida e comum: D2-R59 × D2-R53, da mesma folha. O C do art. 142, § 2º (prazo penal para a infração também capitulada como crime) pode inclinar a marcar C no E do art. 123.
3. Registros à reconciliação, sem errata da ficha:
   - desvio de redação do D2-R59 ("inclui" → substituição; seção 7, (i));
   - D2-R72 sem [TS], aceito pela QA, sem desvio pela 12.5, item 2;
   - observação do mecanismo E2 no D2-R72, sem AJ;
   - reabertura das Fontes 4 e 6 em 22/10 (seção 1), só como conferência. A Base dos itens fica com a consulta de 20/10, e a T-120 continua como janela de janeiro (ficha 11.6).
4. Núcleo: os 30 ficam false (ficha 12.1), o que confere com a v1.
5. Para a leva 7, só registro: DA fica com moldura 50 C / 38 E (56,8%) e D2 com 10/14 (41,7%). A leva 7 é D3-R60 a D3-R89 (ficha 12.1).

## 9. Tabela-resumo dos 30 itens
| id | folha | ponto | gab. | [TS] | formato | moldura | aderência | veredito |
|---|---|---|---|---|---|---|---|---|
| D2-R51 | 4.2 | Lei 8.112, art. 135, caput | C | não | DEF | N | direta | APROVADO |
| D2-R52 | 4.2 | Lei 8.112, art. 138 | E | sim | NUM | N | direta | APROVADO |
| D2-R53 | 4.2 | Lei 8.112, art. 142, § 2º | C | não | SIT | N | direta | APROVADO |
| D2-R54 | 4.2 | Lei 8.112, art. 130, § 1º | E | sim | APL | S | direta | APROVADO |
| D2-R55 | 4.2 | Lei 8.112, art. 141, IV (III como contraste) | E | sim | SUJ | N | direta | APROVADO |
| D2-R56 | 4.2 | Lei 8.112, art. 139 | C | não | NUM | N | direta | APROVADO |
| D2-R57 | 4.2 | Lei 8.112, art. 142, § 1º | E | sim | PAR | N | direta | APROVADO |
| D2-R58 | 4.2 | Lei 8.112, art. 132, caput e V | E | sim | APL | S | direta | APROVADO |
| D2-R59 | 4.2 | Lei 8.112, art. 123 | E | sim | DEF | N | direta | APROVADO |
| D2-R60 | 4.2 | Lei 8.112, art. 136 (art. 132, XI) | C | não | SIT | N | direta | APROVADO |
| D2-R61 | 4.4 | Lei 9.784, art. 20 (art. 18 como contraste) | C | não | PAR | N | direta | APROVADO |
| D2-R62 | 4.4 | Lei 9.784, art. 45 | C | não | SIT | N | direta | APROVADO |
| D2-R63 | 4.4 | Lei 9.784, art. 21 | E | sim | DEF | N | direta | APROVADO |
| D2-R64 | 4.4 | Lei 9.784, art. 51, § 1º | C | não | SIT | N | direta | APROVADO |
| D2-R65 | 4.4 | Lei 9.784, art. 44 | E | sim | APL | S | direta | APROVADO |
| D2-R66 | 4.4 | Lei 9.784, art. 56, § 1º | E | sim | SUJ | N | direta | APROVADO |
| D2-R67 | 4.4 | Lei 9.784, art. 66, § 2º | E | sim | PAR | N | direta | APROVADO |
| D2-R68 | 4.4 | Lei 9.784, art. 26, § 4º | C | não | SIT | N | direta | APROVADO |
| D2-R69 | 4.4 | Lei 9.784, art. 69-A, caput e I | E | sim | NUM | N | direta | APROVADO |
| D2-R70 | 4.4 | Lei 9.784, art. 68 | C | não | DEF | N | direta | APROVADO |
| D2-R71 | 4.3 | Lei 8.112, art. 165, § 1º | C | não | DEF | N | direta | APROVADO |
| D2-R72 | 4.3 | Lei 8.112, art. 174, caput (art. 182, par. ún.) | E | não | DEF | N | direta | APROVADO |
| D2-R73 | 4.3 | Lei 8.112, art. 161, § 1º | E | sim | NUM | N | direta | APROVADO |
| D2-R74 | 4.3 | Lei 8.112, art. 147, par. ún. | E | sim | SIT | N | direta | APROVADO |
| D2-R75 | 4.3 | Lei 8.112, art. 154, par. ún. | C | não | SIT | N | direta | APROVADO |
| D2-R76 | 4.3 | Lei 8.112, art. 182, caput | C | não | PAR | N | direta | APROVADO |
| D2-R77 | 4.3 | Lei 8.112, art. 172, caput | E | sim | APL | S | direta | APROVADO |
| D2-R78 | 4.3 | Lei 8.112, art. 158, caput | C | não | SIT | N | direta | APROVADO |
| D2-R79 | 4.3 | Lei 8.112, art. 167, § 2º | C | não | PAR | N | direta | APROVADO |
| D2-R80 | 4.3 | Lei 8.112, art. 164, § 2º | E | sim | SUJ | N | direta | APROVADO |

Percentual de reprovados: **0/30 = 0,0%**. APROVADO 30 (100,0%); AJUSTAR 0; REPROVADO 0.

FIM DO PARECER QA R1 — LEVA 6 — REFORÇO DA
