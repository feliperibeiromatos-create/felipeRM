# QA_DA_reforco_leva5_R1_2026-10-22_gcb-cqfp.md — T-116 — 2026-10-22 — gerado por gcb-cqfp

# PARECER QA R1 — REFORÇO DA, LEVA 5 (v1) — ciclo s16c3
Objeto: saida/gcb/DA_reforco_leva5_v1.md (30 itens: D2-R21 a D2-R30, folha 3.3; D2-R31 a D2-R40, folha 3.4; D2-R41 a D2-R50, folha 4.1). Critérios: ficha saida/gcb/DA_reforco_ficha_2026-10-20.md, seção 4 (4.1 a 4.4), seções 11.4 e 11.6, com as seções 1, 7, 8.2 (itens 4 e 7), 9.3, 10.2 e 11.2; o adendo 11 prevalece. A gcb-cqfp não produziu este texto e não o reescreve. Todo ajuste vem em texto exato (ficha, seção 4.3). Esta leva não tem errata a conferir (ficha 11.3). Sem commit nem push. Nenhum outro arquivo do repositório foi alterado.

## 0. Resultado
- **APROVADO: 29. AJUSTAR: 1** (D2-R44: formato SUJ → DEF; AJ-1, com os reflexos AJ-2 a AJ-10 nas contagens). **REPROVADO: 0.**
- **Taxa de reprovação: 0/30 = 0,0%** (limite 30%): sem gate. A leva segue para a v2.
- Conferências de leva (ficha 4.4): **8 de 8 CONFEREM**; nenhuma NÃO CONFERE. A conferência (2) continua dentro do teto depois do AJ-1 (4.1 com DEF 6 de 20, no teto).
- Desvios do produtor julgados (seção 7): D2-R32 ("dez dias") e D2-R33 ("vinte por cento") **aceitos**; D2-R50 com cena distinta do D2-R47 **aceito**; dúvidas D2-R35, R44, R41, R28, R22, R26, R40 e R49 × D6-08 respondidas. Só a dúvida do D2-R44 gera ajuste.
- Reabertura no planalto.gov.br (seção 1): as 5 páginas abriram com HTTP 200, com o mesmo tamanho em bytes registrado no Anexo N do D2. Os 44 trechos dos 30 itens ocorrem nas páginas de 22/10/2026. As 118 linhas de dispositivo do Decreto 10.835 e as 18 da Lei 6.999 transcritas no Anexo (seções 4.5 e 4.7) também estão nas páginas de hoje, literalmente. A 3.3 não tem item "pendente".

## 1. Entradas (SHA-256 em disco, 22/10/2026), método e rede
| objeto | SHA-256 |
|---|---|
| saida/gcb/DA_reforco_leva5_v1.md | 3062f7cecdb62a7037234f30bae87f51b610ec0131c0b6a4eb3a39108254e591 (= despacho; 131.868 bytes; 866 linhas) |
| saida/gcb/DA_reforco_ficha_2026-10-20.md | 2e676c62d45487ed5f267f40d8f70d9761e2e67534991aa9564a9550c88a4899 (= despacho) |
| saida/gcb/D2_anexo_N_mapa_normativo.md | b0a54fff4ddcf21a693e01ba71032efccf72e0a6fdf912221ff05413cc0e340a (= ficha 11.4.2) |
| saida/gcb/D2_anexo_N_adendo_2026-10-22.md | abed6f934ca9d8881e9d2c6944de86a453018e90ee9e2a8ac139d876d1a8af61 (= despacho e ficha 11.6) |
| saida/gcb/D2_v2_1.md / D1_v2.md | 59cffaa689ea869cd11c13e6a833470b0b91d24b0f25ea2cc2e100ac9be8bd2c / 63bd27c34baec035dd39904ef565f6b5a662c0a30886a4a3d0b13b8b702e3d56 |
| saida/gcb/DA_reforco_leva1_v2.md a leva4_v2.md | 2c431529…4f04 / 5baec20d…1bbe / e4c2a911…3237 / 57203ae3a68042012989b549d19f2dbd5703623b5de3619275b3f05a2f8338da (= D-T116-LEVA1/2/3/4-ACEITE) |
| normativo_cache/CF_1988_compilada_2026-10-20.txt | d6580cb327147e1beb69ccd09cd930613c06f39e1791b235729930a01cacb51d |
| normativo_cache/Lei_8112_1990_compilada_2026-10-20.txt | 72f45d30dcf096207898d143ba551758e3ffac89e87d6dd2d42044fe65202efe |
| normativo_cache/Lei_9784_1999_2026-10-20.txt | f9452916c03521a8435caae49c8feb690ae2b02086424b641204374f38f9ae19 |
| saida/pacote/pacote.json v1.13 | 82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240 |
| saida/banco/moldura_ce_itens_2026-10-20.csv | ed4b364dffbca7d9e8878591914783258fa7048c4f1837d98c3d62e34981daac (DA 44 C / 9 E; D2 9/1; 3.4: D2-38 C; 4.1: D2-45 e D2-48 C; 3.3 sem moldura) |
| regras/estilo_banca.md | 9f9237f5f9828b77d5ab805849a7a14af13fb28fcc1c985fe462ec1027684caf |

Lidos também: regras/ (PADRAO_UNICO_v1.md, proveniencia.md, padrao_resposta_cebraspe.md, estilo_banca_semente.md, estilo_banca.md, seção 3), CLAUDE.md e, em DECISOES.md, D-REFORCO-DA (l. 173), D-REFORCO-2 (l. 95), D-MOLDURA-CE (l. 171) e D-T116-LEVA1/2/3/4-ACEITE (l. 175 a 178). Também saida/banco/moldura_ce_2026-10-20.md, seção 4 (cotas). Modelo de forma: saida/gcb/QA_DA_reforco_leva4_R1_2026-10-22_gcb-cqfp.md.

Método: li inteiras as seções 0 a 6 da v1 e confrontei cada item com a linha do Anexo N do D2 (seções 3, 4.1, 4.3, 4.4, 4.5 e 4.7) ou do adendo (seção 2) e com a cópia em saida/gcb/normativo_cache/. Os canônicos das três folhas foram relidos no pacote.json v1.13 (ordem do pacote, gabarito, enunciado) e no D2_v2_1.md (formato, [TS] e ponto). Os scripts são próprios: python3 -I, somente leitura, no scratchpad da sessão, fora do repositório.
- check.py: 30 blocos, 13 campos; trechos × seção do Anexo ou do adendo × cópia; URL, data, palavras por trecho e por enunciado.
- seq.py: folhas acumuladas reconstruídas do pacote v1.13 + leva 5; teste da regra 6, com autoteste nas sequências da leva 4.
- counts.py: C/E, formatos por folha com os canônicos, moldura (CSV + campo), abertura, fórmula, absolutos, termos do Legislativo e unicidade dos AJ.
- reab.py e reab2.py: extração do HTML reaberto e busca dos trechos e das linhas do Anexo.

**Rede — reabertura no www.planalto.gov.br (22/10/2026).** Comando: `curl -sS -m 60 -A "Mozilla/5.0" -o <arquivo> -w "%{http_code} %{size_download}" <URL>`, URL a URL, com as URLs exatas do Anexo N do D2, seção 1. O HTML ficou só no scratchpad (…/scratchpad/html/) e não foi gravado em saida/.
| hora (UTC) | URL | HTTP | bytes (Anexo) | SHA-256 do HTML de 22/10 |
|---|---|---|---|---|
| 2026-10-22T21:34:23Z | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/decreto/d10835.htm (Fonte 7) | 200 | 71.902 (71.902) | 34512b9a0ccb98e6e8d774a465abdc42196c44c0e48f4d0dfa00ca8a0f033abe |
| 2026-10-22T21:34:24Z | https://www.planalto.gov.br/ccivil_03/leis/l6999.htm (Fonte 9) | 200 | 8.785 (8.785) | f4fd924ff5023af001bf6508775ad2e4833d654b331081ed7a80604408310ce9 |
| 2026-10-22T21:34:25Z | https://planalto.gov.br/ccivil_03/leis/l8112compilado.htm (Fonte 4) | 200 | 343.733 (343.733) | 8852a932b6975a65b9cfb81529947a4cbe7123371f1301e71bf03b720dfaec80 |
| 2026-10-22T21:34:26Z | https://www.planalto.gov.br/ccivil_03/leis/l9784.htm (Fonte 6) | 200 | 74.941 (74.941) | efd567f7461ab8d712718349fec8a9cc23e0bbb2662e8a74b031f141e4242e36 |
| 2026-10-22T21:34:27Z | https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm (Fonte 1) | 200 | 1.507.134 (1.507.134) | fbaa90ea886e44280eb0beb77ec0dc3306086875fb90955f46123c9aa2dc36b8 |

Os SHA-256 de hoje diferem dos do Anexo (Fonte 7 a9a30220…1ce7; Fonte 9 2e000266…d2ad2), embora o tamanho seja o mesmo. É o comportamento já registrado no adendo do D3, seção 1, e no adendo de 22/10, alerta 2: o Planalto troca um script de medição a cada download. A comparação se fez sobre o texto.

Extração: html.parser, cp1252, tachado excluído, `<sup>o</sup>` → "º"; 0 U+FFFD nas cinco páginas; comparação com espaços normalizados. Resultados:
- **Decreto 10.835**: as 118 linhas com texto da seção 4.5 do Anexo (rubricas e o art. 5º tachado fora) estão na página de 22/10, 118/118.
- **Lei 6.999**: as 18 linhas da seção 4.7 estão na página, 18/18.
- Nenhuma das duas páginas cita 2023, 2024, 2025 ou 2026: não há alteração nova.
- Os 44 trechos da coluna Base dos 30 itens ocorrem nas páginas de 22/10, todos 1 vez, com três exceções que se resolvem pelo trecho vizinho: o fragmento "casamento" do D2-R32 ocorre 6 vezes, a alínea a vem logo depois do trecho do inciso III, e o trecho do inciso III ocorre 1 vez; o fragmento "em virtude de sentença judicial transitada em julgado" do D2-R41 ocorre 3 vezes na CF (arts. 41, 95 e 128), e o trecho do caput do § 1º ocorre 1 vez.

A reabertura é conferência, não base. A base dos itens continua a do Anexo N do D2, consulta de 20/10/2026, e a da cópia em cache, como a ficha 11.4.2 e a 11.6 mandam. Nada foi suprido por memória.

Fato de rede confirmado: o www.planalto.gov.br responde com User-Agent de navegador. O registro do R1 da leva 4 ("Empty reply", código 000, sem User-Agent) fica explicado pelo fato registrado na ficha 11.6.

Grafia do host da Fonte 4: o Anexo grafa https://planalto.gov.br/… (sem "www") e a linha 1 da cópia grafa https://www.planalto.gov.br/…. Os 10 itens da Lei 8.112 usam a URL do Anexo (ficha 11.4.2), e a página sem "www" abriu hoje com o mesmo tamanho. Registro, não desvio.

## 2. Veredito por item
Legenda:
- G: gabarito pela letra.
- P: ponto único.
- T: troca legítima e única / [TS].
- F: sem pista de forma.
- Pe: pertinência à folha.
- Gê: não gêmeo (canônico da folha, levas 1 a 4, própria leva).
- M: moldura.
- J: justificativa e proveniência.

Símbolos: ✓ confere; ~ confere com ajuste. "Anexo l." = linha do Anexo N do D2; "l." = linha da cópia em normativo_cache/; "adendo s. 2" = seção 2 do adendo de 22/10/2026.

### Folha 3.3 — D2-R21 a D2-R30 (Anexo N do D2, seções 4.5 e 4.7; sem cópia em cache; página reaberta em 22/10)
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D2-R21 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota av, ax) | N ✓ | ✓ | **APROVADO** | Decreto 10.835, art. 9º, § 4º, literal (Anexo l. 1673; página 22/10: 1). Ponto distinto dos D2-21, 22 e 24 (caput, § 1º, §§ 2º e 3º). |
| D2-R22 | E ✓ | ✓ | [TS] entidade a que pertencer o agente → órgão ou entidade requisitante ✓ | ✓ | direta ✓ | ✓ (nota aw) | N ✓ | ✓ | **APROVADO** | Art. 29, caput (Anexo l. 1767; página: 1). Dúvida (ii): a ressalva omitida (Lei 8.112, art. 93, § 4º) não torna verdadeira a competência do requisitante; o E sai da letra. O ator trocado é mencionado pela fonte (art. 9º, caput) e é plausível (10.2, item 6). Observação, sem AJ: o "Ministro de Estado" fica sem complemento e pode ser lido como o do requisitante; nas duas leituras o item atribui a competência ao lado do requisitante e o E fica nítido. |
| D2-R23 | E ✓ | ✓ | [TS] 6 meses → um ano ✓ | ✓ | direta ✓ | ✓ (nota at) | N ✓ | ✓ | **APROVADO** | Lei 6.999, art. 3º, caput (Anexo l. 1818; página: 1). Troca para um número maior que a letra; o "um ano" é o prazo do art. 2º, § 1º (D2-27), tentação legítima. |
| D2-R24 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota av) | N ✓ | ✓ | **APROVADO** | Art. 9º, literal (Anexo l. 1828). Cenário sem órgão do Legislativo. Usa a fórmula "Nessa situação, nos termos d…" (1 de 7). |
| D2-R25 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota at) | N ✓ | ✓ | **APROVADO** | Art. 3º, § 3º, literal (Anexo l. 1821). "somente" literal (C com absoluto da letra; L3-2). Não fica vizinho do D2-R23 (posições 3 e 5). |
| D2-R26 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 30-A, caput e III (Anexo l. 1775 e 1778; Decreto 11.306/2022, anterior a 2/10/2026). Dúvida (xi): "novo ato de requisição" é subconjunto verdadeiro de "novo ato de cessão ou de requisição"; nada afirma do parágrafo único (comunicação prévia). |
| D2-R27 | E ✓ | ✓ | [TS] quando encerrada a requisição → de imediato ✓ | ✓ | direta ✓ | ✓ (nota ax) | N ✓ | ✓ | **APROVADO** | Art. 9º, § 5º, II, e § 6º (Anexo l. 1676 e 1677). A participação no concurso fica no cenário como hipótese, e o fecho troca o momento por conceito vizinho, sem negar a consequência (10.2, item 5). 46 palavras. |
| D2-R28 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 10 (Anexo l. 1679). Dúvida (iii): sem o "somente", a parte afirmada é verdadeira por si (C6, "incompleto não é errado"); não há marcador de exclusividade que a contradiga. Omitir "direta e indireta" e a remissão ao art. 22 não muda o sentido. Reserva art. 22 nunca no mesmo simulado. |
| D2-R29 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 1º, caput, e § 1º, III (Anexo l. 1627, 1628 e 1631). O enunciado não afirma rol aberto nem fechado. |
| D2-R30 | E ✓ | ✓ | [TS] prazo certo, até 1 ano → prazo indeterminado ✓ | ✓ | direta ✓ | ✓ (nota au) | N ✓ | ✓ | **APROVADO** | Art. 4º, caput (Anexo l. 1822). A ressalva reescrita como oração restritiva ("que não se destinem à nomeação…") é fiel e evita o "exceto" (regra 9). O "comissão" é de "cargo em comissão". Amostra da gbq-estilo. |

### Folha 3.4 — D2-R31 a D2-R40 (Anexo N do D2, seção 4.3; Fonte 4; exigência (b))
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D2-R31 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota ba) | N ✓ | ✓ | **APROVADO** | Lei 8.112, art. 49, § 1º, literal (l. 238; Anexo l. 531). Exigência (b): "para qualquer efeito". |
| D2-R32 | E ✓ | ✓ | [TS] 8 → dez dias ✓ | ✓ | direta ✓ | ✓ | S, órgão/servidor ✓ | ✓ | **APROVADO** | Art. 97, caput e III, a (l. 481, 484 e 485; Anexo l. 769, 772 e 773). **Desvio aceito** (seção 7): com "cinco", o E seria discutível; com "dez", o item contradiz a letra. A moldura não decide. Amostra da gbq-estilo. |
| D2-R33 | E ✓ | ✓ | [TS] dez → vinte por cento ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 46, § 1º (l. 226; Anexo l. 519; MP 2.225-45/2001). **Desvio aceito** (seção 7): "não inferior a cinco por cento" seria implicado pela letra; "não inferior a vinte por cento" nega parcelas de 10% a 19%, que a letra admite. |
| D2-R34 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 41, § 5º, literal (l. 214; Anexo l. 507; Lei 11.784/2008). Exigência (b): "Nenhum servidor". 15 palavras (faixa de C: 8 a 65). |
| D2-R35 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | S, órgão/servidor ✓ | ✓ | **APROVADO** | Art. 76, literal (l. 344; Anexo l. 635). Dúvida (vii), R3 cumprida: a cota da T-122 para a 3.4 é 1 E (moldura_ce_2026-10-20.md, seção 4, linha 12); a leva traz 3 E com moldura (D2-R32, R37, R39), 2 além da cota, e o C faz par 1:1 com um deles. A folha fica com 2 C / 3 E com moldura (40,0%) e 5 itens com moldura (≤ 6). Registro de redação: a ficha 11.4.6 fala em "cotas da T-122 na 3.4 (3 E)"; os 3 E são a antecipação da ficha 2.2 (cota 1 + 2), e não a cota da T-122. |
| D2-R36 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota ay, **obrigatória**) | N ✓ | ✓ | **APROVADO** | Art. 20, § 4º (l. 102; Anexo l. 396; Lei 9.527/1997). "bem como o afastamento" no lugar de "bem assim afastamento" é equivalente. Exigência (b): "somente". Nenhum número do estágio probatório. Não é gêmeo do D2-39 (ponto: art. 91, caput): o dispositivo e o elemento são outros (regra 2). Mas o D2-39 cita o art. 20, § 4º, como base acessória, e o rol fechado afirmado aqui (que não inclui o art. 91) entrega o E do D2-39. Por isso a nota (ay) é obrigatória para o par D2-R36 × D2-39. Amostra da gbq-estilo. |
| D2-R37 | E ✓ | ✓ | [TS] três → seis meses ✓ | ✓ | direta ✓ | ✓ | S, órgão/servidor ✓ | ✓ | **APROVADO** | Art. 87, caput (l. 419; Anexo l. 708). "por até seis meses" excede a letra ("por até três meses"): é E pela letra, e não E por um número menor contido no permitido. 56 palavras (≤ 62). |
| D2-R38 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota az) | N ✓ | ✓ | **APROVADO** | Art. 30, literal (l. 148; Anexo l. 441). |
| D2-R39 | E ✓ | ✓ | [TS] necessidade do serviço → a pedido do servidor ✓ | ✓ | direta ✓ | ✓ | S, órgão/servidor ✓ | ✓ | **APROVADO** | Art. 77, caput (l. 364; Anexo l. 654; Lei 9.525/1997). Troca da condição, sem E por ausência. O § 3º (parcelamento "requeridas pelo servidor", l. 367), citado na justificativa, confere. |
| D2-R40 | E ✓ | ✓ | [TS] ajuda de custo → diárias ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 53, caput (l. 251; Anexo l. 544); contraste com o art. 58, caput (l. 262), literal na nota. Dúvida (vi): a troca de parcela indenizatória é nítida (E1); o enunciado nada afirma das diárias além da finalidade trocada. |

### Folha 4.1 — D2-R41 a D2-R50 (Anexo N do D2, seções 4.1 e 4.4; adendo de 22/10/2026, seção 2)
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D2-R41 | E ✓ | ✓ | [TS] transitada em julgado → ainda sujeita a recurso ✓ | ✓ | direta ✓ | ✓ (nota bb) | S, órgão/servidor ✓ | ✓ | **APROVADO** | CF, art. 41, § 1º, caput e I (l. 697 e 698; Anexo l. 292 e 293; EC 19/1998). Dúvida (iv): o E é nítido sem o "só". O item afirma que a sentença recorrível produz a perda, e isso contradiz o inciso I; não depende de condição necessária (L5-2 cumprida). A pertinência direta ("compl. 4.1", Anexo seção 3) é aceita. |
| D2-R42 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota bc) | N ✓ | ✓ | **APROVADO** | CF, art. 5º, LV (adendo s. 2; l. 125). Conferência da 11.6 / D-T116-LEVA4-ACEITE (c): a letra "o contraditório e ampla defesa" ocorre 1 vez no enunciado; "a ampla defesa", 0 vez. Inciso inteiro, ordem e vírgulas da letra. A Base traz as duas datas verdadeiras (cópia de 20/10; página reaberta em 22/10). |
| D2-R43 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota be) | N ✓ | ✓ | **APROVADO** | Lei 9.784, art. 2º, parágrafo único, IV (l. 19 e 23; Anexo l. 1368 e 1372). |
| D2-R44 | E ✓ | ✓ | [TS] na Constituição → em regulamento do órgão ✓ | ✓ | direta ✓ | ✓ (nota be) | N ✓ | ✓ | **AJUSTAR** (AJ-1; AJ-2 a AJ-10) | Inciso V (l. 24; Anexo l. 1373). Gabarito E pela letra. Dúvida (v): o formato SUJ está **mal declarado**. A troca é do instrumento que prevê o sigilo (Constituição → regulamento do órgão), da mesma família do D2-R04 da leva 4 (lei específica → lei complementar, DEF, aceito). Como SUJ, o item também não cumpre a 7.4.4 e a 10.2, item 6 ("ator que a própria fonte menciona"): a Lei 9.784 não menciona "regulamento" (busca na cópia: 0). Passa a DEF, sem mudar ponto, enunciado, gabarito, Troca nem mecanismo. Efeito: 4.1 com DEF 6 de 20 (no teto de 6) e SUJ 1; leva com DEF 6 e SUJ 4. |
| D2-R45 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota be) | N ✓ | ✓ | **APROVADO** | Inciso VII, literal (l. 26; Anexo l. 1375). |
| D2-R46 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota bb) | N ✓ | ✓ | **APROVADO** | CF, art. 41, § 1º, caput e II (l. 697 e 699; Anexo l. 292 e 294). Sem "só" (L5-2). Pertinência direta aceita. |
| D2-R47 | E ✓ | ✓ | [TS] sem prejuízo da atuação → vedada a atuação dos interessados ✓ | ✓ | direta ✓ | ✓ | S, órgão/servidor ✓ | ✓ | **APROVADO** | Inciso XII (l. 31; Anexo l. 1380); cenário pelo art. 1º, § 1º (l. 13; Anexo l. 1362), sem afirmar norma interna. Absoluto "vedada" inserido pela troca, com C de absoluto literal na mesma folha (D2-R49; L3-2). Amostra da gbq-estilo. |
| D2-R48 | E ✓ | ✓ | [TS] formas simples → formas solenes ✓ | ✓ | direta ✓ | ✓ (nota bd) | N ✓ | ✓ | **APROVADO** | Inciso IX (l. 28; Anexo l. 1377). O enunciado não contém "simples" (L3-5 não se aplica). |
| D2-R49 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | CF, art. 5º, LIV, literal (adendo s. 2; l. 124). Dúvida (ix): o C é nítido ("ninguém" literal; C3). Não é gêmeo do D6-08 (folha 11, lote D6): o ponto do D6-08 é o art. 32 da LAI, e o devido processo legal aparece ali só como condição de contexto. A regra 2 não se aplica; a nota proposta pela produção (D2-R49 × D6-08) é facultativa, por cautela. |
| D2-R50 | E ✓ | ✓ | [TS] direitos dos administrados → interesse da Administração ✓ | ✓ | direta ✓ | ✓ (nota bd) | S, órgão/servidor ✓ | ✓ | **APROVADO** | Inciso VIII (l. 27; Anexo l. 1376). Desvio de cena aceito (seção 7): a cena é distinta da do D2-R47 (L3-3 cumprida). Registro: os dois E com moldura da 4.1 sobre a Lei 9.784 têm a mesma cena-tipo ("função administrativa" em órgão do Legislativo) e o mesmo esqueleto de fecho ("deve ser observado o critério de …"). Nota nova sugerida (bf), seção 8. |

## 3. Reprovação e substituto
Nenhum item reprovado. Não há reposição de E com moldura (ficha 11.5, item 2): os 6 E com moldura ficam, e a meta da D-MOLDURA-CE se cumpre na leva (DA 50/34, 59,5%).

## 4. Ajustes em texto exato (ficha, seção 4.3)
Conferido por script sobre a v1: cada "substituir" ocorre 1 vez no arquivo e cada "por" 0 vez. "\n" indica quebra de linha (LF), como no AJ-5 do R1 da leva 1. O AJ-1 é o ajuste do item. Os AJ-2 a AJ-10 são só reflexo dele nas seções 0, 4 e 6 (contagens e registros); não mudam item nenhum.

`AJ-1 | D2-R44 | Formato | substituir: «previstas na Constituição (item troca por em regulamento do órgão)\n- Formato: SUJ» | por: «previstas na Constituição (item troca por em regulamento do órgão)\n- Formato: DEF»`

`AJ-2 | arquivo (seção 0) | linha da 4.1 | substituir: «| 4.1 (lote D2) | 10 | 5 | 5 | 50,0% | 5 / 0 | 0 / 3 | 2/2/2/0/1/3 |» | por: «| 4.1 (lote D2) | 10 | 5 | 5 | 50,0% | 5 / 0 | 0 / 3 | 3/1/2/0/1/3 |»`

`AJ-3 | arquivo (seção 0) | linha da leva | substituir: «| 14 / 0 | 1 / 6 | 5/5/7/3/3/7 |» | por: «| 14 / 0 | 1 / 6 | 6/4/7/3/3/7 |»`

`AJ-4 | arquivo (seção 4.1) | linha da 4.1 | substituir: «| 5/2/5/0/3/5 | DEF 5 (25,0% de 20) |» | por: «| 6/1/5/0/3/5 | DEF 6 (30,0% de 20) |»`

`AJ-5 | arquivo (seção 4.6) | SUJ | substituir: «D2-R22 (E), D2-R29 (C), D2-R34 (C), D2-R44 (E), D2-R49 (C); SUJ com gabarito E: D2-R22, D2-R44 — o ator posto no lugar do sujeito da letra é mencionado pela fonte e plausível à primeira leitura (D2-R22: o órgão ou a entidade requisitante, art. 9º, caput; D2-R44: o regulamento do órgão, ator plausível na função de ressalvar sigilo, que o inciso V atribui à Constituição);» | por: «D2-R22 (E), D2-R29 (C), D2-R34 (C), D2-R49 (C); SUJ com gabarito E: D2-R22 — o ator posto no lugar do sujeito da letra é mencionado pela fonte e plausível à primeira leitura (D2-R22: o órgão ou a entidade requisitante, art. 9º, caput); o D2-R44 passa a DEF pelo AJ-1 do R1 (a troca é do instrumento que prevê o sigilo, e a Lei 9.784 não menciona regulamento);»`

`AJ-6 | arquivo (seção 4.7) | linha da 4.1 | substituir: «| 4.1 (sobre 20 itens) | 5 (25,0%) | 2 (10,0%) | 5 (25,0%) | 0 (0,0%) | 3 (15,0%) | 5 (25,0%) | DEF 5 (25,0%) |» | por: «| 4.1 (sobre 20 itens) | 6 (30,0%) | 1 (5,0%) | 5 (25,0%) | 0 (0,0%) | 3 (15,0%) | 5 (25,0%) | DEF 6 (30,0%; no teto) |»`

`AJ-7 | arquivo (seção 4.7) | formatos da leva | substituir: «4.1 2/2/2/0/1/3. Formatos da leva: DEF 5, SUJ 5, SIT 7, NUM 3, PAR 3, APL 7 (ficha, 11.4.5: DEF 5, SUJ 5, SIT 7, NUM 3, PAR 3, APL 7 — CONFERE).» | por: «4.1 3/1/2/0/1/3. Formatos da leva: DEF 6, SUJ 4, SIT 7, NUM 3, PAR 3, APL 7 (ficha, 11.4.5: DEF 5, SUJ 5, SIT 7, NUM 3, PAR 3, APL 7; diferença só do D2-R44, SUJ → DEF, pelo AJ-1 do R1).»`

`AJ-8 | arquivo (seção 4.7) | formatos finais | substituir: «4.1 = 5/2/5/0/3/5 — CONFERE.» | por: «4.1 = 5/2/5/0/3/5 (arquivo: 6/1/5/0/3/5, pelo AJ-1 do R1; DEF 6 no teto de 6); 3.3 e 3.4 — CONFERE.»`

`AJ-9 | arquivo (seção 4.8) | comparação com a ficha | substituir: «30 linhas lidas; diferenças: nenhuma — 30 de 30 linhas iguais.» | por: «30 linhas lidas; diferença: 1 (D2-R44, formato SUJ na ficha → DEF, pelo AJ-1 do R1) — 29 de 30 linhas iguais.»`

`AJ-10 | arquivo (seção 6.2, item 10) | registro de desvio | substituir: «O D2-R29, o D2-R34, o D2-R44 e o D2-R49 são SUJ pela ficha; só o D2-R22 e o D2-R44 trocam o sujeito ou a fonte da regra por outro ator.» | por: «O D2-R29, o D2-R34 e o D2-R49 são SUJ pela ficha, e o D2-R22 é o único SUJ que troca o sujeito por outro ator; o D2-R44, SUJ na ficha, passa a DEF pelo AJ-1 do R1 (desvio de formato registrado também na seção 4.8).»`

Efeito do AJ-1, conferido por simulação em script:
- Muda só a linha do campo Formato do D2-R44 (seção 2). O enunciado, o ponto, o gabarito E, o [TS], a Troca (previstas na Constituição → previstas em regulamento do órgão), o mecanismo E3, a moldura N, a abertura declarativa, a Base e a Justificativa ficam.
- Teto de formato: 4.1 final DEF 6 / SUJ 1 / SIT 5 / NUM 0 / PAR 3 / APL 5, maior formato 30% (no teto, regra 4); leva DEF 6, SUJ 4, SIT 7, NUM 3, PAR 3, APL 7.
- Nenhuma outra contagem muda: C/E, [TS], sequência, moldura, abertura, fórmula, absolutos e extensão ficam como estão.
- A seção 6.1, frase "nenhum desvio", fica coberta pelo AJ-9, que registra o desvio na seção 4.8, e pelo AJ-10. Se a v2 preferir, regrava por script a frase da 6.1 com o mesmo conteúdo, e o R2 confere.

## 5. Conferências de leva (ficha, seção 4.4)
| # | conferência | resultado |
|---|---|---|
| 1 | C/E da leva | **CONFERE**: 16 C / 14 E (53,3%; faixa 12–18 em 30). Sequência CEECCCECCE·CEECCCECEE·ECCECCEECE, igual à ficha 11.4.7. Folhas fechadas: 3.3, 3.4 e 4.1 com 10 C / 10 E cada (faixa 8–12 C). |
| 2 | tetos por folha | **CONFERE**. Formatos da leva por folha iguais à ficha 11.4.4: 3.3 2/2/3/2/1/0; 3.4 1/1/2/1/1/4; 4.1 2/2/2/0/1/3 na v1, 3/1/2/0/1/3 depois do AJ-1. Com os canônicos (D2_v2_1.md, campo Formato): 3.3 5/3/5/4/3/0; 3.4 4/1/4/3/3/5; 4.1 5/2/5/0/3/5 na v1, 6/1/5/0/3/5 com o AJ-1 (DEF 6 no teto de 6). VOLÁTIL 0; REVERIFICAR 0: não há redação de 2025/2026; Decreto 11.306/2022, Leis 9.525/1997, 9.527/1997 e 11.784/2008, MP 2.225-45/2001 e EC 19/1998 são anteriores a 2/10/2026, e o Decreto 12.374/2025 fica fora. Moldura por folha: 3.3 0; 3.4 5; 4.1 5 (≤ 6). Piso de 10 diretos: 20 diretos em cada folha. |
| 3 | moldura acumulada e conjuntos | **CONFERE**. CSV: DA 44/9; D2 9/1 (3.4 D2-38 C; 4.1 D2-45 e D2-48 C). Levas 1 a 4: 2/9 + 2/3 + 1/4 + 0/3 = 5/19. Leva 5: 1 C / 6 E (D2-R35 / D2-R32, R37, R39, R41, R47, R50; tipo "órgão/servidor do Poder Legislativo da União"). DA 49/28 → **50/34 (59,5%)**, igual às fichas 2.2 e 11.4.6: **meta da D-MOLDURA-CE cumprida** (25 E novos ≥ 21; 100 ≤ 102). D2 9/4 → **10/10 (50,0%)**. D3, D4 (K1 a K4, fecho neutro, ", e não") e D1 sem item novo. Termos do Legislativo só nos 7 itens S; o "comissão" do D2-R30 é "cargo em comissão". R3 cumprida (cota da 3.4 = 1 E; seção 2, D2-R35). |
| 4 | pontos sem duplicata | **CONFERE**: 30 pontos distintos. Nenhum dispositivo coincide com os pontos dos canônicos das três folhas (ficha 11.4.3) nem com os D2-R01 a R20. Mesmo artigo com outro elemento, todos com "Difere de" e nota: R21 × D2-21/22/24; R36 × D2-31/36 e D2-39; R41 e R46 × D2-04; R43 a R50 × D2-41/43/49. O D2-R36 × D2-39 tem nota obrigatória (seção 2). Excluídos da 11.4.2 respeitados: Decreto 12.374; Decreto 10.835, arts. 5º, 12, 16, 23 e 31 a 33; Lei 8.112, art. 20, caput, e números do estágio probatório, art. 135 e art. 143, §§ 1º e 2º; arts. 116 a 182; CF, art. 37, XVI, b, e art. 40, §§ 4º e 5º-A; Lei 9.784, art. 2º, parágrafo único, I (reservado à 1.1); "fontes" do direito disciplinar como conceito. Nenhum órgão requisitante além da Presidência da República e da Justiça Eleitoral. |
| 5 | exigências da leva | **CONFERE**. Exigência (b): três C com o absoluto da letra, diretos e sem [TS] (D2-R31, R34, R36), com "Difere de" para o art. 20. L4-1: 0 fecho "é correto afirmar que". Abertura (7.4.2; L3-1): leva com CQ 7 C / 7 E (50,0% de C) e declarativos 9 C / 7 E (43,8% de E); folhas fechadas 3.3 CQ 4/1 e DC 6/9, 3.4 CQ 4/5 e DC 6/5, 4.1 CQ 6/4 e DC 4/6, recontadas sobre o pacote + leva. Fórmula: 7 dos 14 CQ (D2-R24, R31, R32, R39, R41, R42, R47; orientação ≤ 7). L3-2: C com absoluto literal R25, R31, R34, R36, R49; E com absoluto inserido só o R47, com C literal na mesma folha. L3-3: nenhum cenário idêntico até o fecho na mesma folha. L3-4 e L3-5: 0. L4-3 e L4-4: nenhum E6 e nenhum E3 que condicione hipótese autônoma. 10.2, item 5: nenhum E nega no fecho a hipótese inteira do cenário. 10.2, item 6: o D2-R22 cumpre; o D2-R44 não cumpria como SUJ, e o AJ-1 resolve. L5-1: E entre 26 e 56 palavras, C entre 15 e 53, recontadas, iguais à v1. L5-2: D2-R41 e D2-R46 sem "só" nem verbo de condição necessária. |
| 6 | primeiro e último id por lote | **CONFERE**: D2-R21 a D2-R50, contínuos, como na ficha 11.1 e 11.4.1; nenhum no pacote.json v1.13 (1.159 itens) nem nas levas 1 a 4. Núcleo false nos 30 (ficha 11.1). |
| 7 | linha 1 e última linha | **CONFERE**: "# DA_reforco_leva5_v1.md — T-116 — 2026-10-22 — gerado por gcb-cpp"; "FIM DA LEVA 05 — REFORÇO DA" (com LF final). |
| 8 | bases reabertas no cache (amostra de 5 da 3.4 e da 4.1, ficha 11.4.2) e 3.3 trecho × linha do Anexo | **CONFERE**. 3.4 e 4.1: os 28 trechos dos 20 itens são subcadeia da seção citada do Anexo (4.1, 4.3, 4.4) ou do adendo (s. 2) e da cópia em cache (28/28). Amostra reaberta com linha: Lei 8.112 l. 484 (R32), 226 (R33), 102 (R36), 364 (R39); CF l. 125 (R42), 124 (R49), 698 (R41); Lei 9.784 l. 24 (R44), 31 (R47). 3.3 (ficha 11.4.2 e 11.4.10, item 2): os 16 trechos dos 10 itens ocorrem 1 vez na seção 4.5 ou 4.7 do Anexo, nas linhas 1628/1631 (R29), 1673 (R21), 1676/1677 (R27), 1679 (R28), 1767 (R22), 1775/1778 (R26), 1818 (R23), 1821 (R25), 1822 (R30) e 1828 (R24). Coincidem com as 10 linhas da ficha 11.4.2, mais as de contexto 1628, 1676 e 1775. Reaberto o planalto em 22/10 (seção 1), as linhas do Anexo e os trechos estão nas páginas. Maior soma de trecho por item: 25 palavras (R21, R36, R42; limite 25). "consulta 20/10/2026" em 30/30. URL igual à do Anexo/adendo em 30/30. |
| — | teste de sequência (regra 6; 7.3) | **CONFERE** (seq.py; canônicos na ordem do pacote v1.13, sem itens das levas 1 a 4 nestas folhas). Leva, folhas da leva, folhas acumuladas e legado passam, no gabarito e no [TS]. Valores iguais aos da v1, seção 4.3; o mais perto do limite é p7 13/14 na leva inteira e no [TS] da 4.1 acumulada. Autoteste: 6.2 acumulada da leva 4 reprova só por p4 8/8 (legado registrado). O AJ-1 não muda gabarito nem [TS]. |
| — | integridade dos blocos | 30 blocos com os 13 campos. Troca ⇔ [TS] ⇔ "TS=sim" ⇔ E (14/14; 0 C-isca). itemEdital P1-DA-<folha>, AUTORAL e QA PENDENTE em 30/30. Seção 1 sem gabarito, [TS], URL ou marcas. 0 "exceto", "R$", "NGP", "Vide" ou "STF" em enunciado. Nenhum autor nomeado. |

## 6. Errata
Nenhuma errata a conferir nesta leva (ficha 11.3).

## 7. Desvios e dúvidas declarados pela produção (seções 5 e 6 da v1)
| # | desvio ou dúvida | avaliação |
|---|---|---|
| (i) / 6.2.1 | D2-R32: "oito → dez dias" em vez de "oito → cinco" | **Aceito.** Com "cinco", o item afirmaria uma ausência menor que a garantida, e o E ficaria discutível (ficha 4.1, item 2): quem pode ausentar-se por oito dias consecutivos pode ausentar-se por cinco. "Dez" contradiz a letra (art. 97, III, a) e não coincide com outro prazo do art. 97. O plano da ficha 11.4.4 dá o sentido da troca, não a redação. O desvio é de redação, motivado e declarado, e não exige errata da ficha; a reconciliação registra. |
| (i) / 6.2.1 | D2-R33: "dez → vinte por cento" em vez de "dez → cinco" | **Aceito**, pelo mesmo motivo. "Não inferior a cinco por cento" é implicado pelo piso de dez, e seria C pela letra. "Não inferior a vinte por cento" nega parcelas de 10% a 19% que a letra admite: E pela letra. A alternativa citada pela produção ("por apenas cinco dias"; "não inferior a cinco por cento") **não** é recomendada: o primeiro insere absoluto (L3-2) e o segundo continua implicado. |
| (ii) | D2-R22: ator trocado e ressalva omitida | **Aceito** (seção 2). |
| (iii) | D2-R28: C6 sem "somente" | **Aceito**: C nítido. |
| (iv) | D2-R41: E sem "só" | **Aceito**: E nítido; L5-2 cumprida. |
| (v) / 6.2.10 | D2-R44: SUJ × DEF | **Não aceito como está** → AJ-1 (DEF), com os reflexos AJ-2 a AJ-10. |
| (vi) | D2-R40: PAR ajuda de custo × diárias | **Aceito**: troca nítida (E1). |
| (vii) | D2-R35: C com moldura | **Aceito**: R3 cumprida (cota 1 + 2 E além dela na 3.4). |
| (viii) / 6.2.2 | D2-R42: letra do adendo | **Conferido**: "o contraditório e ampla defesa", 1 vez; "a ampla defesa", 0 vez (D-T116-LEVA4-ACEITE (c)). |
| (ix) | D2-R49 × D6-08 | **Aceito**: C nítido; não é gêmeo. A nota é facultativa. |
| (x) / 6.2.3 | D2-R50 com cena distinta do D2-R47 | **Aceito.** A ficha 11.4.4 pede "cena como no D2-R47" (mesma cena-tipo, função administrativa) e, no parágrafo da moldura da 4.1, "cenas distintas até o fecho (L3-3)". A produção cumpriu as duas leituras: mesma cena-tipo, texto distinto. Fica a nota (bf) sugerida na seção 8. |
| (xi) / 6.2.4 | D2-R26: subconjunto do caput | **Aceito**. |
| (xii) | grafia do host da Fonte 4 | **Registrada** (seção 1). |
| (xiii) | 3.3 sem cópia em cache | Página reaberta em 22/10 (seção 1): as 10 bases conferem. **Nenhum item vai a "pendente"** (ficha 11.5, item 1). |
| 6.2.5 a 6.2.9, 6.2.11 | redação do D2-R30, R43/R45, R29, R36; mecanismos; trechos com "[…]" | **Aceitos**. Os trechos com "[…]" são subcadeias contínuas do lastro e da cópia, e a soma fica ≤ 25 palavras. Mecanismos sem reclassificação (C2 10, C3 5, C6 1, E1 4, E3 10). |
| 6.1 | 30 linhas iguais à ficha 11.4.4 | **Conferido** na v1; depois do AJ-1, 29 de 30 (formato do D2-R44). |

## 8. Lista para a v2 (gcb-cpp) e notas à GCB
1. Aplicar os AJ-1 a AJ-10 por substituição exata, sem outra mudança. Recontar por script as seções 0 e 4: nenhuma contagem além das de formato deve mudar.
2. O R2 confere os AJ aplicados literalmente e examina só o que a v2 mudar além deles. Os AJ de estilo da amostra (D2-R32, R47, R36, R30; ficha 11.4.8), se houver, vão com estes para a v2 (ficha 9.3, item 6). Texto igual pedido pelo R1 e pelo estilo é aplicado uma vez (ficha 11.3).
3. Notas de simulado, à GCB e sem decisão desta QA:
   - aceitas com os ids finais: (at) a (be), (w) e (x), e os acréscimos da produção D2-R35 × D2-R39, D2-R31 × D2-R40 e D2-R42/R46/R49 (no máximo 2 por simulado); D2-R49 × D6-08, facultativa;
   - (ay) **obrigatória** para o par D2-R36 × D2-39: o rol fechado do art. 20, § 4º, afirmado no C, entrega o E do D2-39;
   - nova (bf), sugerida: D2-R47 × D2-R50. Os dois são E com moldura da mesma cena-tipo ("função administrativa" em órgão do Poder Legislativo da União) e com o mesmo esqueleto de fecho ("deve ser observado o critério de …"). Juntos, um sinaliza o outro, e a (be) sozinha não os separa.
4. Registros à reconciliação (sem errata da ficha):
   - desvios de número dos D2-R32 e R33 (seção 7);
   - formato do D2-R44 (AJ-1);
   - "cotas da T-122 na 3.4 (3 E)" da ficha 11.4.6: a cota da T-122 é 1 E, e os 3 E são a antecipação da 2.2;
   - reabertura de 22/10 das Fontes 1, 4, 6, 7 e 9 (seção 1), só conferência; a Base dos itens fica com a consulta de 20/10, e a T-120 continua como janela de janeiro (ficha 11.6).
5. Núcleo: os 30 ficam false (ficha 11.1). Confere com a v1.
6. Para a leva 6, só registro: a moldura de DA fica em 50 C / 34 E (59,5%) e a do D2 em 10/10 (50,0%), meta da D-MOLDURA-CE cumprida na leva 5. Na leva 6 a folha 4.2 abre com o D2-R51 (Lei 8.112, art. 135; exigência (b)). Pedido ao qa-normativo-da usa User-Agent de navegador (ficha 11.6).

## 9. Tabela-resumo dos 30 itens
| id | folha | ponto | gab. | [TS] | formato | moldura | aderência | veredito |
|---|---|---|---|---|---|---|---|---|
| D2-R21 | 3.3 | Decreto 10.835, art. 9º, § 4º | C | não | DEF | N | direta | APROVADO |
| D2-R22 | 3.3 | Decreto 10.835, art. 29, caput | E | sim | SUJ | N | direta | APROVADO |
| D2-R23 | 3.3 | Lei 6.999, art. 3º, caput | E | sim | NUM | N | direta | APROVADO |
| D2-R24 | 3.3 | Lei 6.999, art. 9º | C | não | SIT | N | direta | APROVADO |
| D2-R25 | 3.3 | Lei 6.999, art. 3º, § 3º | C | não | NUM | N | direta | APROVADO |
| D2-R26 | 3.3 | Decreto 10.835, art. 30-A, III | C | não | SIT | N | direta | APROVADO |
| D2-R27 | 3.3 | Decreto 10.835, art. 9º, § 5º, II, e § 6º | E | sim | SIT | N | direta | APROVADO |
| D2-R28 | 3.3 | Decreto 10.835, art. 10 | C | não | DEF | N | direta | APROVADO |
| D2-R29 | 3.3 | Decreto 10.835, art. 1º, § 1º, III | C | não | SUJ | N | direta | APROVADO |
| D2-R30 | 3.3 | Lei 6.999, art. 4º, caput | E | sim | PAR | N | direta | APROVADO |
| D2-R31 | 3.4 | Lei 8.112, art. 49, § 1º | C | não | SIT | N | direta | APROVADO |
| D2-R32 | 3.4 | Lei 8.112, art. 97, III, a | E | sim | APL | S | direta | APROVADO |
| D2-R33 | 3.4 | Lei 8.112, art. 46, § 1º | E | sim | NUM | N | direta | APROVADO |
| D2-R34 | 3.4 | Lei 8.112, art. 41, § 5º | C | não | SUJ | N | direta | APROVADO |
| D2-R35 | 3.4 | Lei 8.112, art. 76 | C | não | APL | S | direta | APROVADO |
| D2-R36 | 3.4 | Lei 8.112, art. 20, § 4º | C | não | DEF | N | direta | APROVADO |
| D2-R37 | 3.4 | Lei 8.112, art. 87, caput | E | sim | APL | S | direta | APROVADO |
| D2-R38 | 3.4 | Lei 8.112, art. 30 | C | não | SIT | N | direta | APROVADO |
| D2-R39 | 3.4 | Lei 8.112, art. 77, caput | E | sim | APL | S | direta | APROVADO |
| D2-R40 | 3.4 | Lei 8.112, art. 53, caput | E | sim | PAR | N | direta | APROVADO |
| D2-R41 | 4.1 | CF, art. 41, § 1º, I | E | sim | APL | S | direta | APROVADO |
| D2-R42 | 4.1 | CF, art. 5º, LV (adendo) | C | não | SIT | N | direta | APROVADO |
| D2-R43 | 4.1 | Lei 9.784, art. 2º, par. ún., IV | C | não | DEF | N | direta | APROVADO |
| D2-R44 | 4.1 | Lei 9.784, art. 2º, par. ún., V | E | sim | SUJ → DEF (AJ-1) | N | direta | AJUSTAR (AJ-1 a AJ-10) |
| D2-R45 | 4.1 | Lei 9.784, art. 2º, par. ún., VII | C | não | DEF | N | direta | APROVADO |
| D2-R46 | 4.1 | CF, art. 41, § 1º, II | C | não | SIT | N | direta | APROVADO |
| D2-R47 | 4.1 | Lei 9.784, art. 2º, par. ún., XII | E | sim | APL | S | direta | APROVADO |
| D2-R48 | 4.1 | Lei 9.784, art. 2º, par. ún., IX | E | sim | PAR | N | direta | APROVADO |
| D2-R49 | 4.1 | CF, art. 5º, LIV (adendo) | C | não | SUJ | N | direta | APROVADO |
| D2-R50 | 4.1 | Lei 9.784, art. 2º, par. ún., VIII | E | sim | APL | S | direta | APROVADO |

Percentual de reprovados: **0/30 = 0,0%**. APROVADO 29 (96,7%); AJUSTAR 1 (3,3%); REPROVADO 0.

FIM DO PARECER QA R1 — LEVA 5 — REFORÇO DA
