# QA_DA_reforco_leva7_R1_2026-10-22_gcb-cqfp.md — T-116 — 2026-10-22 — gerado por gcb-cqfp

# PARECER QA R1 — REFORÇO DA, LEVA 7 (v1) — ciclo s16c5
Objeto: saida/gcb/DA_reforco_leva7_v1.md (30 itens, todos do lote D3: D3-R60 a D3-R69, folha 5.1; D3-R70 a D3-R79, folha 6.1; D3-R80 a D3-R89, folha 7, nesta ordem no arquivo).
Critérios: ficha saida/gcb/DA_reforco_ficha_2026-10-20.md, seção 4 (4.1 a 4.4), seções 13.4, 13.5 e 13.6, com as seções 1, 7, 8.2 (itens 4 e 7), 9.3, 10.2, 11.2, 11.6, 12.2 e 13.2. O adendo 13 prevalece onde divergir.
A gcb-cqfp não produziu este texto e não o reescreve. Todo ajuste vem em texto exato (ficha, seção 4.3). Esta leva não tem errata a conferir (ficha 13.3). Sem commit nem push. Nenhum outro arquivo do repositório foi alterado.

## 0. Resultado
- **APROVADO: 29. AJUSTAR (aprovado com ajuste): 1 (D3-R68). REPROVADO: 0.**
- **Taxa de reprovação: 0/30 = 0,0%** (limite 30%). Sem gate.
- Conferências de leva (ficha 4.4): **8 de 8 CONFEREM**. Nenhuma NÃO CONFERE. O teste de sequência e a integridade dos blocos também conferem.
- **Pertinência dos 8 parciais da 6.1** (ficha 13.4.10, item 4; 13.6): **8 aceitos, 0 recusados** (D3-R70, R72, R73, R75, R76, R77, R78 e R79). Motivos na seção 3. A 6.1 fecha em 20: 12 diretos e 8 parciais. O piso de 10 diretos está cumprido.
- **D3-R81 e D3-R82** (E5 sem [TS]): **aceitos como a ficha manda**. Esta QA **não pede [TS]**. Motivo na seção 2 (folha 7) e na seção 7. O teste de [TS] da folha 7 continua aprovado.
- **Dúvidas do bloco à GCB:** todas julgadas na seção 7. A única que gera ajuste é a (iv), D3-R68 (AJ-1 a AJ-8).
- Reabertura no planalto.gov.br (seção 1): as seis fontes da leva abriram com HTTP 200. Os bytes são iguais aos do Anexo N do D3 e do adendo de 22/10. Os 48 trechos da coluna Base estão nas páginas reabertas.

## 1. Entradas (SHA-256 em disco, 22/10/2026), método e rede
| objeto | SHA-256 |
|---|---|
| saida/gcb/DA_reforco_leva7_v1.md | fdafc3bd36127778727edb66d863c135f1fa08182757b6e58ec4c27ae736a0ed (= despacho; 147.822 bytes; 922 linhas LF; 0 CR) |
| saida/gcb/DA_reforco_ficha_2026-10-20.md | 34fe46fc59e9215966b5568966c7a8a7d831c744760b12e08369a1eebf995391 (= despacho; com a seção 13.6) |
| saida/gcb/D3_anexo_N_adendo_2026-10-22.md | 826e32b511ad448e66c760bda23e34c0940db847d04a54f87b97dcf19ef85c43 (= despacho e ficha 13.6) |
| saida/gcb/D3_anexo_N_mapa_normativo.md | 2ef58f9b50a23472fa733731db30fa998492698472ab873443d6a64d422ff1df (= ficha 13.4.2) |
| saida/gcb/D3_anexo_N_adendo_2026-10-20.md | bbfd3eed1a69edef189a1fb8f07fee901daaf5bb636d8192bb1442e53a3fa797 (= ficha 13.6) |
| saida/gcb/D2_anexo_N_mapa_normativo.md | b0a54fff4ddcf21a693e01ba71032efccf72e0a6fdf912221ff05413cc0e340a (seção 4.3: reserva cruzada da 5.1, não usada) |
| saida/gcb/D3_v2_1.md / D1_v2.md | 0f7a8b090fe6f2243ae55b36273dacdb719aaf04b19548dce70aad4867798930 / 63bd27c34baec035dd39904ef565f6b5a662c0a30886a4a3d0b13b8b702e3d56 |
| saida/gcb/DA_reforco_leva1_v2.md a leva6_v2.md | 2c431529…4f04 / 5baec20d…1bbe / e4c2a911…3237 / 57203ae3…38da / b531014b…81c4 / 0b8ccd4d07bf7d97cb9c1728c6bf4c18e3c5f7c9ac557e27f4537c068c96090b (= D-T116-LEVA1 a LEVA6-ACEITE) |
| normativo_cache/Lei_9784_1999_2026-10-20.txt | f9452916c03521a8435caae49c8feb690ae2b02086424b641204374f38f9ae19 |
| normativo_cache/CF_1988_compilada_2026-10-20.txt | d6580cb327147e1beb69ccd09cd930613c06f39e1791b235729930a01cacb51d |
| normativo_cache/Lei_10406_2002_CodigoCivil_compilada_2026-10-20.txt | 97e0ffaa7e5b92d072622c9bde5ebdab9121cd32913c4292cb0c5f74a914a828 |
| normativo_cache/Lei_4619_1965_2026-10-20.txt | b91ef03df94717e00602b1b5195f73176c1c5cf5bebe6d80fba1cbaf37a9082f |
| normativo_cache/Decreto_20910_1932_2026-10-20.txt | a8a216f2cd510ace7eda954a9d0800939b6d0be19e5b10d9626d5d073aa2818a |
| saida/pacote/pacote.json v1.13 | 82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240 |
| saida/banco/moldura_ce_itens_2026-10-20.csv | ed4b364dffbca7d9e8878591914783258fa7048c4f1837d98c3d62e34981daac (5.1: D3-07 E; 6.1: D3-28 C; 7: D3-74 C) |
| regras/estilo_banca.md | 9f9237f5f9828b77d5ab805849a7a14af13fb28fcc1c985fe462ec1027684caf |
| modelo de forma: QA_DA_reforco_leva6_R1_2026-10-22_gcb-cqfp.md | 12aefbd9e5c99986b85b284427a9c197ef68725c6d3b1c52c2111c9ed9733626 |

Lidos também: regras/ (PADRAO_UNICO_v1.md, proveniencia.md, estilo_banca.md, seções 3.1 a 3.12 e 5), CLAUDE.md e, em DECISOES.md, D-REFORCO-2, D-MOLDURA-CE, D-REFORCO-DA, D-T97-META-FUNDADOR-RESP e D-T116-LEVA1 a LEVA6-ACEITE.

Método. Li inteiras as seções 0 a 6 da v1. Confrontei cada item com a linha do Anexo N do D3 (seções 4.1, 4.4, 4.7 e 4.9), do adendo de 20/10 (4.8) ou do adendo de 22/10 (seção 4) e com a cópia em normativo_cache/. Os canônicos das três folhas foram relidos no pacote.json v1.13 (ordem, gabarito e enunciado) e no D3_v2_1.md (cabeçalho [TS] e campo Formato). Os scripts são próprios: python3 -I, somente leitura, no scratchpad (…/scratchpad/qa7/), fora do repositório.
- check.py e lines.py: os 48 trechos da coluna Base contra a seção citada do Anexo ou do adendo e contra a cópia (contagem e linha); URL, "consulta 20/10/2026" e palavras por item.
- counts.py: folhas acumuladas (pacote v1.13 + leva 7); teste da regra 6 no gabarito e no [TS]; formatos com os canônicos, C/E, moldura, abertura, fórmula, extensão e termos do Legislativo.
- reab.py e cf.py: texto das páginas reabertas (html.parser, cp1252, sem tachado nem script); busca dos 48 trechos e leitura dos dispositivos da Lei 8.429 com as notas.

**Rede — reabertura no planalto.gov.br, como conferência e não como base (ficha 13.4.10, item 4; 11.6).** Comando: `curl -sS -m 90 -A "Mozilla/5.0" -o <arquivo> -w "%{http_code} %{size_download}" <URL>`, com as URLs do Anexo N do D3 (Fontes 1, 4, 5 e 7) e do adendo de 22/10 (B3 e B4; a Lei 4.619 em https, como a ficha 13.6 fixou). O HTML ficou só no scratchpad (…/scratchpad/qa7/html/) e não foi gravado em saida/.

| hora (UTC) | URL | HTTP | bytes (Anexo/adendo) | SHA-256 do HTML |
|---|---|---|---|---|
| 2026-10-23T00:17:30Z | https://planalto.gov.br/ccivil_03/leis/l8429compilada.htm (Fonte 1) | 200 | 173.931 (173.931) | 7d37004f162299fc81a128d7a59c8391d185405e371a4d0e2ab6bd0c163e064c |
| 2026-10-23T00:17:31Z | https://www.planalto.gov.br/ccivil_03/leis/1950-1969/l4619.htm (B3) | 200 | 8.562 (8.562) | ad6b75e28c62dfa58281907cebbe5876c14658852da201c2423171d6b83d3292 |
| 2026-10-23T00:17:32Z | https://www.planalto.gov.br/ccivil_03/decreto/antigos/d20910.htm (B4) | 200 | 7.151 (7.151) | 868dfcc9188a0c408772aa5f655d5d530badab52849ba5f21437b94fb7ec5cb7 |
| 2026-10-23T00:17:33Z | https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm (Fonte 4; B1) | 200 | 1.507.134 (1.507.134) | 38403b1fdf585516ce5aa5c0ff7aaa8e3062bf91d414e0027ae01fbf805a3ba7 |
| 2026-10-23T00:17:35Z | https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm (Fonte 5; B2) | 200 | 923.899 (923.899) | b34de68fc27ebb1ec7fa28a4252b514191fa81000f7db31d7360571bdac0511d |
| 2026-10-23T00:17:37Z | https://www.planalto.gov.br/ccivil_03/leis/l9784.htm (Fonte 7) | 200 | 74.941 (74.941) | eaeba89ce9040ce02e2a14f781c0f690f850542a9ab37b27b8b097acd266250f |

As horas em UTC caem em 22/10/2026, 21h17 a 21h18 no horário de Brasília (data do despacho). O SHA-256 do HTML difere do Anexo, do adendo e da reabertura da produção, embora os bytes sejam iguais. É o script de medição do Planalto, já registrado no Anexo N do D3, seção 1. A comparação se fez sobre o texto. Resultados:
- 48 de 48 trechos da coluna Base estão nas páginas de hoje (normalização de espaços e ordinais; sem tachado).
- Lei 8.429: os 10 dispositivos da folha 7 (arts. 1º, § 2º; 2º, caput; 3º, § 2º; 7º, caput; 8º, caput; 12, § 9º; 13, § 3º; 20, § 2º; 21, caput e II; 23, § 1º) estão na página sem "(Vide ADI …)", sem "Revogado" e sem "vetado". As notas da página são iguais às do Anexo, 4.9.
- "2025" e "2026" não ocorrem nas páginas da Lei 8.429, da Lei 4.619, do Decreto 20.910, do Código Civil e da Lei 9.784. Na CF ocorrem em notas de outros dispositivos. Os arts. 5º, XXV, 84, 87 e 136 da página não têm nota de 2025 ou 2026.
- Nenhum dispositivo da leva mudou entre 20 e 22/10/2026. A T-120 continua como janela de janeiro (ficha 11.6).

## 2. Veredito por item
Legenda:
- G: gabarito pela letra.
- P: ponto único.
- T: troca legítima e única / [TS].
- F: sem pista de forma.
- Pe: pertinência à folha.
- Gê: não é gêmeo de canônico da folha, das levas 1 a 6 nem da própria leva.
- M: moldura.
- J: justificativa e proveniência.

Símbolos: ✓ confere. "Anexo l." = linha do Anexo N do D3. "ad22 l." / "ad20 l." = linha do adendo de 22/10 / de 20/10. "l." = linha da cópia em normativo_cache/.

### Folha 5.1 — D3-R60 a D3-R69 (Anexo N do D3, 4.4 e 4.7; adendo de 22/10, 4.1; Fontes 4 e 7)
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D3-R60 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota ce) | N ✓ | ✓ | **APROVADO** | Lei 9.784, art. 13, caput e III (Anexo l. 157/160; l. 72/75). "Nessa situação, a Lei … estabelece" não é a fórmula "nos termos d…". O C fica fácil pelo cenário, mas é legítimo (C2). Item da amostra do estilo. |
| D3-R61 | E ✓ | ✓ | [TS] não podem → pode ✓ | ✓ | direta ✓ | ✓ (nota ce) | N ✓ | ✓ | **APROVADO** | Art. 13, caput e I (Anexo l. 157/158; l. 72/73). Dúvida (i): o E fica nítido sem "se não houver impedimento legal". A expressão o tornaria discutível, porque o próprio art. 13 é o impedimento. "Por parte de órgão administrativo ou de seu titular" é a letra do art. 12 e não acrescenta outro erro. |
| D3-R62 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota cf) | N ✓ | ✓ | **APROVADO** | Art. 14, caput, literal (Anexo l. 161; l. 76). O D1-41 julga o § 2º. |
| D3-R63 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota cf) | N ✓ | ✓ | **APROVADO** | Art. 14, § 1º (Anexo l. 162; l. 77). "Entre outros elementos" é verdadeiro (matérias, poderes e limites ficam fora). É ângulo novo do mesmo parágrafo do D3-02, que julga a ressalva de exercício (regra 2). Não é gêmeo. |
| D3-R64 | E ✓ | ✓ | [TS] menor → maior ✓ | ✓ | direta ✓ | ✓ (nota cg) | N ✓ | ✓ | **APROVADO** | Art. 17 (Anexo l. 167; l. 82). Dúvida (xii): "menor → maior" é inversão de polaridade (E2) mais do que conceito vizinho (E1). Fica como E3, que a produção declarou (ficha 13.3): o campo não vai ao pacote.json. Registro, sem AJ. |
| D3-R65 | E ✓ | ✓ | [TS] quando vagos → ocupados ✓ | ✓ | direta ✓ | ✓ (nota ch) | N ✓ | ✓ | **APROVADO** | CF, art. 84, VI, b (Anexo l. 135/137; l. 1042/1044). Dúvida (ii): o E está nítido pela letra da alínea b. Observação: o art. 84, XXV ("prover e extinguir os cargos públicos federais, na forma da lei"), poderia sugerir C a quem lê "pode dispor sobre essa extinção" sem âncora. O enunciado ancora a regra em "mediante decreto presidencial" e "nos termos do art. 84, VI, b"; as duas âncoras devem ficar. É a única fórmula da folha. |
| D3-R66 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota ci, obrigatória) | N ✓ | ✓ | **APROVADO** | CF, art. 84, parágrafo único (Anexo l. 138; l. 1067). C6 bem classificado: "algumas de suas atribuições" é parcial e verdadeiro. Não afirma qual parte do XXV é a "primeira parte" (B2). |
| D3-R67 | E ✓ | ✓ | [TS] incisos VI, XII e XXV → inclui o IV ✓ | ✓ | direta ✓ | ✓ (nota ci, obrigatória) | N ✓ | ✓ | **APROVADO** | Parágrafo único e inciso IV (Anexo l. 138/134; l. 1067/1040). Dúvida (iii): o E decorre da enumeração fechada que o próprio texto faz ("as atribuições mencionadas nos incisos VI, XII e XXV, primeira parte"), citada como tal ("passíveis de delegação"). Não é "E por ausência" (regra 8; L4-3). A nota (ci) obrigatória está bem posta: lido junto, o D3-R66 sinaliza o rol. |
| D3-R68 | E ✓ | ✓ | [TS] titular Presidente → Ministros ✓ | **ajuste** | direta ✓ | ✓ (nota cj) | N ✓ | ✓ | **APROVADO COM AJUSTE (AJ-1 a AJ-8)** | CF, art. 84, caput e II (ad22 l. 105/106; l. 1036/1038). Gabarito e ponto corretos. Dúvida (iv): duas pistas de forma facilitam o E. (a) A frase "com o auxílio do Presidente da República" põe o Presidente como auxiliar dos Ministros, o que é implausível de saída (ficha 10.2, item 6). (b) "Nos termos do art. 84, II" remete ao artigo que lista as competências privativas do Presidente. Por isso o item atribui "privativamente" ao Presidente o que diz ser dos Ministros. O AJ tira as duas pistas e mantém a troca de um só elemento (o titular da direção superior). Fica a tentação legítima do art. 87, parágrafo único, I (supervisão ministerial). O enunciado novo tem 19 palavras, dentro da faixa de E (L5-1). Gabarito, [TS], formato SUJ, moldura e posição não mudam. |
| D3-R69 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota cj) | N ✓ | ✓ | **APROVADO** | CF, art. 87, parágrafo único, caput e II (ad22 l. 109/111; l. 1089/1091). A cláusula "além de outras atribuições" é letra do caput do parágrafo único (A5.1-04) e não é ponto separado. |

### Folha 6.1 — D3-R70 a D3-R79 (Anexo N do D3, 4.1; adendo de 20/10, 4.8; adendo de 22/10, 4.2 a 4.5; Fontes 4, 5, B3 e B4)
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D3-R70 | C ✓ | ✓ | sem [TS] ✓ | ✓ | parcial ✓ (aceita, seção 3) | ✓ (nota ck) | N ✓ | ✓ | **APROVADO** | CC, art. 41, caput e IV (ad22 l. 125/129; l. 117/121). Item classificatório que não afirma responsabilidade (B4). A nota da Lei 11.107/2005 não é de 2025 ou 2026. |
| D3-R71 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota co) | N ✓ | ✓ | **APROVADO** | CF, art. 136, § 1º, caput e II (ad22 l. 118/119; l. 1621/1626). Julga só a letra, sem combinar com o art. 5º, XXV, nem com o art. 37, § 6º (B3). O item não nomeia o Congresso. |
| D3-R72 | E ✓ | ✓ | [TS] externo → interno ✓ | ✓ | parcial ✓ (aceita, seção 3) | ✓ (nota ck) | N ✓ | ✓ | **APROVADO** | CC, art. 42 (ad22 l. 132; l. 124). Dúvida (v): "e todas as pessoas regidas pelo direito internacional público" é letra do art. 42. O "todas" é absoluto literal e não é a troca (L6-2). O contraste é só pela letra, sem afirmar responsabilidade de Estado estrangeiro (B4). |
| D3-R73 | C ✓ | ✓ | sem [TS] ✓ | ✓ | parcial ✓ (aceita, seção 3) | ✓ (nota cm) | N ✓ | ✓ | **APROVADO** | Lei 4.619, art. 1º, caput (ad20 l. 229; l. 10; mapa A6.1-22). Ortografia atual no enunciado. A vírgula (sic) fica só na Base (B1). "Segundo a Lei nº 4.619/1965" basta para B6: o item não afirma quem hoje propõe a ação regressiva. |
| D3-R74 | E ✓ | ✓ | [TS] ulterior → prévia ✓ | ✓ | direta ✓ | ✓ (nota cl, obrigatória) | N ✓ | ✓ | **APROVADO** | CF, art. 5º, XXV (Anexo l. 114; l. 77). Dúvida (vi): a redação própria não repete a frase do D3-24. O D3-24 tem como ponto a condição "se houver dano" e o contraste com o art. 37, § 6º. O D3-R74 julga o momento, "ulterior". É ângulo novo do mesmo dispositivo (regra 2), com "Difere de" e a nota (cl) obrigatória, porque o D3-24 traz a palavra "ulterior" e entrega o E. "Prévia" é o termo do art. 5º, XXIV (E1). |
| D3-R75 | E ✓ | ✓ | [TS] uma quinta parte → um terço ✓ | ✓ | parcial ✓ (aceita, seção 3) | ✓ (nota cm) | N ✓ | ✓ | **APROVADO** | Lei 4.619, art. 6º (ad22 l. 140; l. 18). L6-1: a troca é para mais, contra o teto "não excederá", e assim contradiz a letra. L7-1: "terço" ocorre 0 vez na Lei 4.619 (cópia e página reaberta). Sujeito "funcionário estável" mantido. Item da amostra do estilo. |
| D3-R76 | C ✓ | ✓ | sem [TS] ✓ | ✓ | parcial ✓ (aceita, seção 3) | ✓ (nota cn) | N ✓ | ✓ | **APROVADO** | Decreto 20.910, art. 6º (ad22 l. 150; l. 17). A paráfrase é fiel ("contado da data do ato ou fato do qual a reclamação se originar"). |
| D3-R77 | E ✓ | ✓ | [TS] não corre → continua a correr ✓ | ✓ | parcial ✓ (aceita, seção 3) | ✓ (nota cn) | S ✓ (tipo da cota; fecho neutro) | ✓ | **APROVADO** | Decreto 20.910, art. 4º, caput (ad22 l. 147; l. 14). Dúvida (vii): "no estudo ou no pagamento" é subconjunto fiel das três hipóteses da letra. Omitir "ao reconhecimento" não altera o efeito, e "as repartições ou funcionários encarregados" está no plural. A consequência é trocada sem "sem" nem "não" (10.2, item 5), como no D2-R74 da leva 6. A moldura (órgão do Poder Legislativo da União como devedor) não decide o gabarito e não afirma prática da Câmara. Usa a fórmula; é o único E com moldura com a fórmula (L7-2). Item da amostra do estilo. |
| D3-R78 | C ✓ | ✓ | sem [TS] ✓ | ✓ | parcial ✓ (aceita, seção 3) | ✓ (nota cm) | N ✓ | ✓ | **APROVADO** | Lei 4.619, art. 4º, caput, literal (ad22 l. 137; l. 14), com "haja transitado" (B1). |
| D3-R79 | C ✓ | ✓ | sem [TS] ✓ | ✓ | parcial ✓ (aceita, seção 3) | ✓ (nota cn) | N ✓ | ✓ | **APROVADO** | Decreto 20.910, art. 8º, literal (ad22 l. 152; l. 19). O "somente" é literal em C (L7-3). |

### Folha 7 — D3-R80 a D3-R89 (Anexo N do D3, 4.9; Fonte 1; sem cópia em cache: trecho × linha do Anexo e × página reaberta)
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D3-R80 | E ✓ | ✓ | [TS] ainda que … sem remuneração → desde que mediante remuneração ✓ | ✓ | direta ✓ | ✓ (nota cs) | N ✓ | ✓ | **APROVADO** | Art. 2º, caput (Anexo l. 201). Dúvida (viii): a troca é de um só elemento, a exigência de remuneração. Retirar "transitoriamente" do enunciado não cria segundo erro, porque o item não afirma nada sobre o exercício transitório. "Todo aquele" e "qualquer" são literais e não são a troca (L6-2). O SUJ E usa elemento da própria fonte (10.2, item 6). |
| D3-R81 | E ✓ | ✓ | sem [TS] (E5) ✓ | ✓ | direta ✓ | ✓ (nota cp) | N ✓ | ✓ | **APROVADO** | Art. 8º, caput (Anexo l. 211). A moldura (reparação até o limite da herança) é verdadeira por si. O segmento acrescido ("sujeitando-se também à multa civil") contradiz o "apenas" da letra: E por contradição expressa (regra 8), não "E por ausência". Sem "só", "apenas" ou verbo de condição necessária (L5-2). **A QA não pede [TS]**: nenhum elemento da letra é substituído; o item soma um segmento acessório (estilo_banca 3.5 e 5.1: [TS] obrigatório só em E1 e E2). O art. 8º-A, parágrafo único (sucessão empresarial, com exceção para simulação ou fraude), não alcança o herdeiro do cenário. Item da amostra do estilo. |
| D3-R82 | E ✓ | ✓ | sem [TS] (E5) ✓ | ✓ | direta ✓ | ✓ (nota cq) | N ✓ | ✓ | **APROVADO** | Art. 12, § 9º (Anexo l. 291). Dúvida (ix): "ressalvada a multa civil, que pode ser executada desde a prolação da sentença" é exceção falsa em moldura verdadeira, o caso típico de E5 (estilo_banca 3.5, "excetuando-se"). Não há contradição interna, e "somente" é literal e não é a troca (L6-2; L7-3). **A QA não pede [TS]**, pelo mesmo motivo do D3-R81. O § 9º não tem "(Vide ADI)" na página. |
| D3-R83 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota cr) | N ✓ | ✓ | **APROVADO** | Art. 1º, § 2º, literal (Anexo l. 194). |
| D3-R84 | E ✓ | ✓ | [TS] demissão → suspensão ✓ | ✓ | direta ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 13, § 3º (Anexo l. 297). O "sem prejuízo de outras sanções cabíveis" é letra e não nega a hipótese (10.2, item 5). Nenhum canônico usa o art. 13. |
| D3-R85 | E ✓ | ✓ | [TS] independe → a aprovação impede ✓ | ✓ | direta ✓ | ✓ (nota ct) | S ✓ (tipo da cota; fecho neutro) | ✓ | **APROVADO** | Art. 21, caput e II (Anexo l. 422/424). Dúvida (x): usa "conforme" e não a fórmula (L7-2). "Tribunal de Contas" é elemento do inciso II. Os §§ 1º e 2º do art. 21 (atos e decisões de controle "considerados" pelo juiz) não tornam verdadeiro o "impede", porque não condicionam a aplicação. O § 4º ("Vide ADI 7236/7156") não é usado. A moldura não decide. O cenário é distinto do D3-74 (L3-3). Item da amostra do estilo. |
| D3-R86 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota cu) | N ✓ | ✓ | **APROVADO** | Art. 7º, caput, literal (Anexo l. 209). É a única fórmula da folha. |
| D3-R87 | E ✓ | ✓ | [TS] suspende → interrompe ✓ | ✓ | direta ✓ | ✓ (nota cv) | N ✓ | ✓ | **APROVADO** | Art. 23, § 1º (Anexo l. 437). E1 nítido. O "180 dias" é letra e não é a troca. |
| D3-R88 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota cw) | N ✓ | ✓ | **APROVADO** | Art. 20, § 2º, com o § 1º como sujeito do afastamento (Anexo l. 421/420). "Uma única vez" é absoluto literal em C (L3-2). |
| D3-R89 | C ✓ | ✓ | sem [TS] ✓ | ✓ | direta ✓ | ✓ (nota cs) | N ✓ | ✓ | **APROVADO** | Art. 3º, § 2º (Anexo l. 205). Sem "(Vide ADI)": a nota 7156 é do § 1º, que não é usado. C3 bem classificado (negativa "não se aplicarão"). |

## 3. Pertinência dos 8 parciais da 6.1 (ficha 13.4.10, item 4; 13.6)
Critério: a 6.1 é a folha geral ("Responsabilidade civil do Estado no direito brasileiro"). Pertinência parcial (indireta) é admitida quando o dispositivo integra o regime brasileiro da responsabilidade do Estado por aplicação ou contraste. Integram esse regime o sujeito do art. 43 do CC, o regresso contra o agente culpado (CF, art. 37, § 6º, parte final) e a prescrição das pretensões contra a Fazenda. O item tem de nomear a norma e o sujeito dela (adendo de 22/10, seção 3) e não pode afirmar o que é SEM FONTE (B2 a B6).
| id | dispositivo (mapa) | juízo | motivo |
|---|---|---|---|
| D3-R70 | CC, art. 41, caput e IV (A6.1-04) | **aceito** | Define o sujeito do art. 43 ("pessoas jurídicas de direito público interno"), núcleo da 6.1. É aplicação direta da letra, com o item só classificatório (B4). |
| D3-R72 | CC, art. 42 (A6.1-06) | **aceito** (o mais distante dos 8) | Julga o qualificador "interno" × "externo" que recorta o sujeito do art. 43. O vínculo é de contraste, e o item não o estende à responsabilidade de Estado estrangeiro, que é SEM FONTE (B4). Fica parcial, só para simulado diagnóstico (D-ADERENCIA), com a nota (ck). Informação, não motivo: recusá-lo poria o C de D3-30 junto do D3-R70, D3-R71 e D3-R73 (corrida de 4 C) e quebraria o teste da 6.1 acumulada, no gabarito e no [TS] (counts.py). |
| D3-R73 | Lei 4.619, art. 1º, caput (A6.1-22) | **aceito** | O dever de propor a ação regressiva executa o regresso do art. 37, § 6º, parte final. É o mesmo regime dos D3-R23, R24 e R36, aceitos em outras folhas. |
| D3-R75 | Lei 4.619, art. 6º (A6.1-10) | **aceito** | Liquidação do que o funcionário deve à Fazenda, fase final do regresso. |
| D3-R76 | Decreto 20.910, art. 6º (A6.1-16) | **aceito** | Prescrição de pretensão contra a Fazenda pela via administrativa, no mesmo decreto do art. 1º (D3-R22), que fixa o prazo das pretensões indenizatórias contra o Estado. O vínculo é o mais fraco do decreto, mas existe. |
| D3-R77 | Decreto 20.910, art. 4º, caput (A6.1-13) | **aceito** | Curso da prescrição da dívida passiva líquida da Fazenda, incluída a indenizatória. |
| D3-R78 | Lei 4.619, art. 4º, caput (A6.1-07) | **aceito** | Competência para a ação regressiva (regresso). |
| D3-R79 | Decreto 20.910, art. 8º (A6.1-18) | **aceito** | Interrupção da prescrição contra a Fazenda. |

Resultado: **8 aceitos, 0 recusados**. A 6.1 fecha em 20: 12 diretos (10 canônicos, D3-R71 e D3-R74) e 8 parciais. Os parciais contam para a meta e só vão a simulado diagnóstico (D-ADERENCIA; D-T97-META-FUNDADOR-RESP). A reconciliação não tem folha menor a registrar.

## 4. Reprovação e substituto
Nenhum item reprovado e nenhum id vago. As reservas das três folhas ficam intactas: 5.1 com 5 pontos, 6.1 com 6 e 7 com 7.

## 5. Ajustes em texto exato (ficha, seção 4.3)
Todos são do D3-R68 (dúvida (iv); ficha 10.2, item 6). Cada trecho atual ocorre 1 vez na v1 (conferido por script, aj.py). A gcb-cpp aplica por substituição exata, sem outra mudança.
- AJ-1 | D3-R68 | enunciado (seção 1) | substituir: «**D3-R68.** Nos termos do art. 84, II, da Constituição Federal, compete privativamente aos Ministros de Estado exercer, com o auxílio do Presidente da República, a direção superior da administração federal.» | por: «**D3-R68.** De acordo com a Constituição Federal, compete privativamente aos Ministros de Estado exercer a direção superior da administração federal.»
- AJ-2 | D3-R68 | Ponto de julgamento | substituir: «- Ponto de julgamento: A5.1-01 — CF, art. 84, caput e II (adendo de 22/10/2026, 4.1) — compete privativamente ao Presidente da República exercer, com o auxílio dos Ministros de Estado, a direção superior da administração federal (item troca os papéis)» | por: «- Ponto de julgamento: A5.1-01 — CF, art. 84, caput e II (adendo de 22/10/2026, 4.1) — compete privativamente ao Presidente da República exercer, com o auxílio dos Ministros de Estado, a direção superior da administração federal (item atribui a direção superior aos Ministros de Estado)»
- AJ-3 | D3-R68 | Justificativa (linha 2) | substituir: «O item inverte os papéis: põe os Ministros de Estado como titulares e o Presidente como auxiliar; a tentação é ler “com o auxílio dos Ministros” como partilha da titularidade da direção superior.» | por: «O item atribui aos Ministros de Estado a direção superior que a letra dá privativamente ao Presidente da República; a tentação é confundir o auxílio dos Ministros com a titularidade da direção superior.»
- AJ-4 | D3-R68 | Troca | substituir: «- Troca: compete privativamente ao Presidente da República … com o auxílio dos Ministros de Estado (art. 84, caput e II) → compete privativamente aos Ministros de Estado … com o auxílio do Presidente da República» | por: «- Troca: compete privativamente ao Presidente da República exercer, com o auxílio dos Ministros de Estado, a direção superior (art. 84, caput e II) → compete privativamente aos Ministros de Estado exercer a direção superior»
- AJ-5 | D3-R68 | seção 4.5 (tabela de pontos) | substituir: «| A5.1-01 — CF, art. 84, caput e II (adendo de 22/10/2026, 4.1) — compete privativamente ao Presidente da República exercer, com o auxílio dos Ministros de Estado, a direção superior da administração federal (item troca os papéis) |» | por: «| A5.1-01 — CF, art. 84, caput e II (adendo de 22/10/2026, 4.1) — compete privativamente ao Presidente da República exercer, com o auxílio dos Ministros de Estado, a direção superior da administração federal (item atribui a direção superior aos Ministros de Estado) |»
- AJ-6 | D3-R68 | seção 4.6 (palavras por item) | substituir: «D3-R68 29;» | por: «D3-R68 19;»
- AJ-7 | D3-R68 | seção 4.6 (L5-1) | substituir: «E da leva de 25 a 53 palavras» | por: «E da leva de 19 a 53 palavras»
- AJ-8 | D3-R68 | seção 5 (bloco à GCB, item (9)) | substituir: «E de 25 a 53 palavras» | por: «E de 19 a 53 palavras»

Efeito dos AJ: nenhum em gabarito, [TS], formato, moldura, aderência, abertura, fórmula ou sequência. A coluna Base fica com a letra do art. 84, caput e II, como está. O D3-R68 passa a 19 palavras, no piso da faixa de E (L5-1), e a fórmula da 5.1 continua só no D3-R65.

## 6. Conferências de leva (ficha, seção 4.4)
| # | conferência | resultado |
|---|---|---|
| 1 | C/E da leva | **CONFERE**. A leva tem 15 C / 15 E (50,0%; faixa de 12 a 18 em 30), na sequência CECCEECEEC·CCECEECECC·EEECEECECC, igual à da ficha 13.4.7. Com os canônicos, as folhas fecham em 5.1 10/10, 6.1 11/9 e 7 9/11 (faixa de 8 a 12 C). |
| 2 | tetos por folha | **CONFERE**. Os formatos da leva são os da ficha 13.4.4 (5.1 3/2/3/0/2/0; 6.1 1/1/2/3/2/1; 7 2/1/3/1/2/1, em DEF/SUJ/SIT/NUM/PAR/APL). Com os canônicos (D3_v2_1.md, campo Formato): 5.1 6/3/5/0/5/1, 6.1 4/2/4/3/5/2 e 7 5/2/5/3/3/2. O maior formato é DEF 6 de 20 na 5.1, no teto (ficha 13.4.5). VOLÁTIL 0 e REVERIFICAR 0: as redações são originais, da Lei 14.230/2021, da EC 32/2001 ou da Lei 11.107/2005. Moldura por folha com os canônicos: 5.1 1, 6.1 2, 7 2 (≤ 6). Diretos: 5.1 20, 6.1 12 (piso 10, seção 3), 7 20. |
| 3 | moldura acumulada e conjuntos | **CONFERE**. CSV: DA 44/9; D3 6/1 (5.1: D3-07 E; 6.1: D3-28 C; 7: D3-74 C). Levas 1 a 6 nos arquivos finais: 6/29, dos quais o D3 tem 3/10. A leva 7 tem 0 C / 2 E (D3-R77 e D3-R85), ambos do tipo "órgão/servidor do Poder Legislativo da União". DA vai a **50/40 (55,6%)** e D3 a **9/13 (40,9%)**, como na ficha 13.4.6 e 2.2. Meta da D-MOLDURA-CE: 31 E novos (≥ 21); 2 × 50 = 100 ≤ 120. As cotas da T-122 (6.1 1 E; 7 1 E) estão cumpridas. Não há C com moldura (R3 sem par a exigir). K1 a K4, D2, D1, D4 e D5 não têm item novo. Termos do Legislativo (Legislativo, Câmara, Congresso, Senado, deputado, parlamentar, plenário) só nos 2 itens S. |
| 4 | pontos sem duplicata | **CONFERE**. Os 30 pontos são distintos. Nenhum coincide com os pontos já usados da ficha 13.4.3 (canônicos das três folhas e de outras folhas), nem com os pontos das levas 1 a 6 (grep do campo Ponto: Lei 4.619, arts. 1º, caput, 4º e 6º; Decreto 20.910, arts. 2º a 10; CF, arts. 5º, XXV, 84, 87 e 136; CC, arts. 41 e 42; Lei 9.784, arts. 13 a 17; Lei 8.429 — nenhum uso). Mesmo dispositivo com outro elemento, com "Difere de" e nota: R63 × D3-02 e R74 × D3-24. Nenhum ponto da lista "Fora da leva 7" (13.4.2) foi usado. |
| 5 | exigências da leva | **CONFERE**. Exigência (d): o D3 chega a D3-R89 (89 itens; seção 2.1), com piso de 10 diretos nas três folhas. Exigência (a): os 2 itens novos com moldura são E. L4-1: nenhum fecho "é correto afirmar que". Abertura (7.4.2; L3-1): na leva, CQ 6 C / 4 E (60,0% de C) e declarativos 9 C / 11 E (55,0% de E). Nas folhas fechadas: 5.1 CQ 3/3 e DC 7/7; 6.1 CQ 5/1 e DC 6/8; 7 CQ 4/3 e DC 5/8. Fórmula (7.4.3; L7-2): 3 dos 10 CQ (D3-R65, R77, R86), 1 por folha; com moldura só no D3-R77 (1 de 2 E com moldura); nunca no D3-R85. L3-2, L6-2 e L7-3: C com absoluto literal D3-R79 ("somente") e D3-R88 ("uma única vez"); E com absoluto literal que não é a troca D3-R72, R80 e R82; nenhum E com absoluto inserido. L3-3: nenhum cenário idêntico até o fecho. L3-4 e L3-5: nenhum "mas não", ", e não", "mero", "por si só" ou "simples". L4-3 e L4-4: nenhum E6 e nenhum E3 que condicione hipótese autônoma. 10.2, itens 5 e 6: nenhuma negação frontal; o SUJ D3-R68 depende do AJ (seção 5). L5-1: E entre 25 e 53 palavras na v1 (19 a 53 com o AJ-1); C entre 13 e 47. L5-2: o D3-R81 não usa "só", "apenas" nem verbo de condição necessária. L6-1 e L7-1: 1 troca de número (D3-R75, para mais), e o valor posto ocorre 0 vez na Lei 4.619. 13.2, item 4: os únicos E sem [TS] são D3-R81 e R82, ambos E5. |
| 6 | primeiro e último id por lote | **CONFERE**. D3-R60 a D3-R89 são contínuos, com as faixas por folha da ficha 13.1 (5.1 R60–R69; 6.1 R70–R79; 7 R80–R89) e as folhas na ordem 5.1, 6.1, 7. Nenhum desses ids está no pacote.json v1.13 nem nas levas 1 a 6 (último D3 anterior: D3-R59). O núcleo é false nos 30 (ficha 13.1). |
| 7 | linha 1 e última linha | **CONFERE**. Linha 1: "# DA_reforco_leva7_v1.md — T-116 — 2026-10-22 — gerado por gcb-cpp". Última linha: "FIM DA LEVA 07 — REFORÇO DA", com LF final. |
| 8 | bases no cache (amostra de 5 ou mais) | **CONFERE**. Os 48 trechos dos 30 itens são subcadeia da seção citada do Anexo (4.1, 4.4, 4.7, 4.9), do adendo de 20/10 (4.8) ou do adendo de 22/10 (seção 4), 1 vez cada (48/48). Os 34 trechos de normas com cópia são subcadeia da cópia, 1 vez cada (34/34). Amostra com linha da cópia: Lei 9.784 l. 72/73 (R61), 82 (R64); CF l. 1044 (R65), 1067 (R66/R67), 1038 (R68), 1626 (R71), 77 (R74); CC l. 124 (R72); Lei 4.619 l. 10 (R73), 18 (R75), 14 (R78); Decreto 20.910 l. 14 (R77), 19 (R79). Folha 7: trecho × linha do Anexo 4.9 e × página reaberta (10/10). A maior soma de trecho por item é 25 palavras (R69; limite 25). "Consulta 20/10/2026" aparece em 30/30. A URL é a do Anexo ou do adendo em 30/30; a Lei 4.619 vai em https (ficha 13.6) e a Lei 8.429 sem "www", como a Fonte 1. |
| — | teste de sequência (regra 6; 7.3; 13.4.7) | **CONFERE** (counts.py; canônicos na ordem do pacote v1.13; nenhuma das levas 1 a 6 tem item nestas folhas). Passam, no gabarito e no [TS], a leva, as folhas da leva, as folhas acumuladas e o legado. Os valores são iguais aos da v1, seção 4.3. Com D3-R81 e R82 sem [TS], a folha 7 acumulada passa (TTnnnTTTnn·TnnnTTnTnn). |
| — | integridade dos blocos | **CONFERE**. Os 30 blocos têm os campos da regra 14. Troca ⇔ [TS] ⇔ "TS=sim" vale nos 13 itens com [TS], todos E; não há C-isca. itemEdital P1-DA-<folha>, AUTORAL e QA PENDENTE em 30/30. A seção 1 não traz gabarito, [TS], URL nem marcas. Nenhum "exceto", "R$", "NGP", "Vide" ou "STF" em enunciado. Nenhum autor nomeado. Mecanismos: C2 13, C3 1, C6 1, E1 4, E3 9, E5 2. |

## 7. Desvios e dúvidas declarados pela produção (seções 5 e 6 da v1) e pontos do despacho
| # | desvio ou dúvida | avaliação |
|---|---|---|
| (i) / 6.2.1 | D3-R61 sem "se não houver impedimento legal" | **Aceito.** A coluna da ficha é sentido, não redação. Com a expressão, o E ficaria discutível. |
| (ii) / 6.2.3 | D3-R65: "ocupados" no cenário, sem "ainda que" | **Aceito.** O E está nítido pela letra da alínea b. As âncoras "mediante decreto presidencial" e "nos termos do art. 84, VI, b" afastam a leitura pelo art. 84, XXV, e devem ficar. |
| (iii) / 6.2.5 | D3-R67: rol fechado | **Aceito.** O E decorre da enumeração do texto, citada como tal (regra 8; L4-3). |
| (iv) | D3-R68: troca dos dois atores | **Ajuste** (AJ-1 a AJ-8): o Presidente posto como auxiliar dos Ministros é implausível de saída (10.2, item 6), e "art. 84, II" denuncia o titular. A troca passa a ser só do titular. |
| (v) / 6.2.6 | D3-R72: "e todas as pessoas regidas pelo direito internacional público" | **Aceito.** É letra do art. 42, e "todas" é absoluto literal que não é a troca (L6-2). |
| (vi) / 6.2.7 | D3-R74: redação própria | **Aceito.** A nota (cl) é **obrigatória**, como na ficha 13.4.9. |
| (vii) / 6.2.8 | D3-R77: "demorem no estudo ou no pagamento"; "continua a correr" | **Aceito.** É subconjunto fiel das hipóteses da letra. "Continua a correr" tem o mesmo sentido de "corre normalmente", da coluna da ficha. |
| (viii) / 6.2.9 | D3-R80 sem "transitoriamente" | **Aceito.** A troca é de um só elemento (remuneração). |
| (ix) / 6.2.10 | D3-R82: "ressalvada a multa civil" | **Aceito.** É E5 nítido, sem contradição interna. |
| (x) / 6.2.11 | D3-R85: "conforme", "Tribunal de Contas" | **Aceito** (L7-2). |
| (xi) | D3-R73 e R75: ortografia atual no enunciado | **Aceito.** A grafia da época e a vírgula (sic) ficam na Base (B1, B7). |
| (xii) | D3-R64: E3 ou E1 | **Registro, sem AJ.** O mecanismo se descreve melhor como E2 (inversão de polaridade). Fica o declarado (ficha 13.3). |
| (xiii) | pertinência dos 8 parciais | **Julgada na seção 3:** 8 aceitos. |
| (xiv) | contagem de "somente" (D3-R01 a R59) | **Conferido.** Por marcador exato, o resultado é 2 C / 2 E (D3-R33 C, R38 E, R43 E, R47 C). A ficha 13.2, item 3, diz 2 C / 3 E porque contou o "só" do D3-R35 (E); o "apenas" do D3-R23 (E) é outro marcador. É registro, sem errata da ficha e sem efeito: não há gatilho no D3 em nenhuma das contagens, e a leva traz "somente" em C (R79) e em E fora da troca (R82). |
| (xv) | linha da leva 4 na 4.6 | **Aceito.** O D3 tem itens na leva 4 (D3-R52 a R59, folha 6.2), e a ficha 13.4.10, item 3, pede o D3 "levas 1 a 3, leva 7, acumulado". Omitir a leva 4 deixaria o acumulado errado. A linha própria é correta, e o acumulado de 160 itens confere. |
| 6.2.12 | absolutos literais em D3-R72 e R80, além do R82 da ficha 13.4.6 | **Aceito** (L6-2). São letra da fonte e não são a troca, e não há E com absoluto inserido. A lista da ficha 13.4.6 era previsão; a seção 4 da v1 é a contagem. |
| 6.2.2, 6.2.4, 6.2.13 a 6.2.15 | "entre outros elementos" (R63); "algumas" (R66); mecanismos; formatos; trechos com "[…]" | **Aceitos.** Os trechos com "[…]" são subcadeias contínuas do lastro e da cópia, com soma ≤ 25 palavras. |
| 6.1 | 30 linhas iguais à ficha 13.4.4 | **Conferido:** formato, moldura, gabarito, [TS], aderência (13.6) e abertura, 30 de 30. |
| despacho | D3-R81 e D3-R82 sem [TS] | **Aceitos.** A QA não pede [TS] (seção 2, folha 7). Não há desvio a registrar pela 13.5, item 2. |

## 8. Lista para a v2 (gcb-cpp) e notas à GCB
1. Aplicar AJ-1 a AJ-8 (D3-R68), por substituição exata. Qualquer outra mudança é examinada no R2 (ficha 4.3). Os AJ de estilo da amostra (D3-R60, R75, R77, R81, R85; ficha 13.4.8), se houver, vão para a v2 e são conferidos no R2 (ficha 9.3, item 6). Nenhum deles toca o D3-R68. Texto igual pedido pelo R1 e pelo estilo é aplicado uma vez (ficha 11.3).
2. Notas de simulado, à GCB, sem decisão desta QA:
   - aceitas com os ids finais: (ce) a (cw), (w) e (x). As notas (ci) e (cl) são **obrigatórias**, como na ficha 13.4.9;
   - acréscimos da produção (D3-R63 × D3-02; D3-R69 × D3-06; D3-R82 × D3-R88 × D3-76; D3-R77 × D3-28; D3-R85 × D3-74): aceitos, todos comuns;
   - com o AJ-1, a nota (cj) (D3-R68 × D3-R69 × D3-R66) continua pertinente. Nenhuma nota nova.
3. Registros à reconciliação, sem errata da ficha:
   - pertinência dos 8 parciais da 6.1 aceita (seção 3); a 6.1 fecha em 20 (12 diretos / 8 parciais);
   - D3-R81 e R82 sem [TS], aceitos, sem desvio pela 13.5, item 2;
   - observação do mecanismo E2 no D3-R64, sem AJ;
   - contagem de "somente" do D3 (dúvida (xiv)), sem errata;
   - reabertura das seis fontes em 22/10 (seção 1), só como conferência. A Base dos itens fica com a consulta de 20/10, e a T-120 continua como janela de janeiro (ficha 11.6).
4. Núcleo: os 30 ficam false (ficha 13.1), o que confere com a v1.
5. Para a leva 8, só registro: DA fica com moldura 50 C / 40 E (55,6%) e D3 com 9/13 (40,9%). O reforço do D3 fecha em D3-R89.

## 9. Tabela-resumo dos 30 itens
| id | folha | ponto | gab. | [TS] | formato | moldura | aderência | veredito |
|---|---|---|---|---|---|---|---|---|
| D3-R60 | 5.1 | Lei 9.784, art. 13, caput e III | C | não | SIT | N | direta | APROVADO |
| D3-R61 | 5.1 | Lei 9.784, art. 13, caput e I | E | sim | DEF | N | direta | APROVADO |
| D3-R62 | 5.1 | Lei 9.784, art. 14, caput | C | não | DEF | N | direta | APROVADO |
| D3-R63 | 5.1 | Lei 9.784, art. 14, § 1º | C | não | SIT | N | direta | APROVADO |
| D3-R64 | 5.1 | Lei 9.784, art. 17 | E | sim | PAR | N | direta | APROVADO |
| D3-R65 | 5.1 | CF, art. 84, VI, b | E | sim | SIT | N | direta | APROVADO |
| D3-R66 | 5.1 | CF, art. 84, parágrafo único | C | não | SUJ | N | direta | APROVADO |
| D3-R67 | 5.1 | CF, art. 84, parágrafo único (IV como contraste) | E | sim | PAR | N | direta | APROVADO |
| D3-R68 | 5.1 | CF, art. 84, caput e II | E | sim | SUJ | N | direta | APROVADO COM AJUSTE (AJ-1 a AJ-8) |
| D3-R69 | 5.1 | CF, art. 87, parágrafo único, II | C | não | DEF | N | direta | APROVADO |
| D3-R70 | 6.1 | CC, art. 41, caput e IV | C | não | DEF | N | parcial | APROVADO |
| D3-R71 | 6.1 | CF, art. 136, § 1º, caput e II | C | não | SIT | N | direta | APROVADO |
| D3-R72 | 6.1 | CC, art. 42 (art. 41 como contraste) | E | sim | PAR | N | parcial | APROVADO |
| D3-R73 | 6.1 | Lei 4.619, art. 1º, caput | C | não | SIT | N | parcial | APROVADO |
| D3-R74 | 6.1 | CF, art. 5º, XXV | E | sim | PAR | N | direta | APROVADO |
| D3-R75 | 6.1 | Lei 4.619, art. 6º | E | sim | NUM | N | parcial | APROVADO |
| D3-R76 | 6.1 | Decreto 20.910, art. 6º | C | não | NUM | N | parcial | APROVADO |
| D3-R77 | 6.1 | Decreto 20.910, art. 4º, caput | E | sim | APL | S | parcial | APROVADO |
| D3-R78 | 6.1 | Lei 4.619, art. 4º, caput | C | não | SUJ | N | parcial | APROVADO |
| D3-R79 | 6.1 | Decreto 20.910, art. 8º | C | não | NUM | N | parcial | APROVADO |
| D3-R80 | 7 | Lei 8.429, art. 2º, caput | E | sim | SUJ | N | direta | APROVADO |
| D3-R81 | 7 | Lei 8.429, art. 8º, caput | E | não (E5) | SIT | N | direta | APROVADO |
| D3-R82 | 7 | Lei 8.429, art. 12, § 9º | E | não (E5) | DEF | N | direta | APROVADO |
| D3-R83 | 7 | Lei 8.429, art. 1º, § 2º | C | não | DEF | N | direta | APROVADO |
| D3-R84 | 7 | Lei 8.429, art. 13, § 3º | E | sim | PAR | N | direta | APROVADO |
| D3-R85 | 7 | Lei 8.429, art. 21, caput e II | E | sim | APL | S | direta | APROVADO |
| D3-R86 | 7 | Lei 8.429, art. 7º, caput | C | não | SIT | N | direta | APROVADO |
| D3-R87 | 7 | Lei 8.429, art. 23, § 1º | E | sim | PAR | N | direta | APROVADO |
| D3-R88 | 7 | Lei 8.429, art. 20, § 2º | C | não | NUM | N | direta | APROVADO |
| D3-R89 | 7 | Lei 8.429, art. 3º, § 2º | C | não | SIT | N | direta | APROVADO |

Percentual de reprovados: **0/30 = 0,0%**. APROVADO 29 (96,7%); AJUSTAR 1 (3,3%; D3-R68); REPROVADO 0.

FIM DO PARECER QA R1 — LEVA 7 — REFORÇO DA
