# DA_reforco_leva8_reconciliacao_2026-10-22.md — T-116 — 2026-10-22 — gerado por gcb-gerencia

# RECONCILIAÇÃO DA LEVA 8 DO REFORÇO DE DIREITO ADMINISTRATIVO (D-REFORCO-DA) — D1 da GCB, errata AJ-L7-E1 e gatilho A — ciclo s16c6
Titular: GCB (T-116). A GCB reconcilia e decide a D1. Não produz nem corrige item. Nenhum arquivo de produção ou de QA foi alterado. Além deste arquivo, só há três escritas: o acréscimo da seção 15 da ficha ("Adendo após a leva 8", com a ficha da leva 9), o item de gatilho em PARA_PRESIDENCIA.md e a linha T-116 de TAREFAS.md. Não houve commit nem push.

Decisões aplicadas:
- D-REFORCO-DA; D-REFORCO-2 (regras 1 a 6); D-MOLDURA-CE; D-T97-META-FUNDADOR-RESP;
- D-ADERENCIA; D-QA-PENDENTE; D-NUCLEO-CRITERIO; D-COMPLEMENTOS; D-FONTE-DATA-ANTERIOR; D-REVERIFICACAO-JAN;
- D-T116-LEVA1-ACEITE a D-T116-LEVA6-ACEITE;
- **D-T116-LEVA7-ACEITE** (DECISOES.md, linha 182): leva 8 aberta pelo adendo do D4; o D3-R75 ficou fora do aceite e voltou à GCB;
- **D-AJL7E1-RITO** (linha 183): a gcb-cqfp confere só a aplicação mecânica, e a proposição normativa nova vai ao qa-normativo-da;
- D-T120F-REDACAO (linha 180).

Precedentes:
- D-T89-R1-ACEITE: a reconciliação prevalece na consolidação;
- D-T116-LEVA1-ACEITE, parte (II), e D-T116-LEVA2-ACEITE: errata em rito próprio.

Gate do CLAUDE.md aplicado: afirmação sobre norma sem fonte datada depois do QA2 vai a "pendente" e nunca é aprovada. Nesta leva, nenhuma vai a "pendente" (seção 4.6, item 2).

## 0. Entradas (SHA-256 em disco, 22/10/2026)
| objeto | papel | SHA-256 |
|---|---|---|
| saida/gcb/DA_reforco_leva8_v2.md | **objeto final** (30 itens; 169.034 bytes; 1.011 linhas LF; 0 CR) | 1fdce9bde3393b445cabd75d50064fb2a2fdde103c03415dc82256c203bf6f2c |
| saida/gcb/DA_reforco_leva8_v1.md | objeto do R1 e do estilo (rastro) | 1b9903d5aa0c3f049a8aa361c2fda8c62b03b118272f6ef96df79907e50d8ecf |
| saida/gcb/QA_DA_reforco_leva8_R1_2026-10-22_gcb-cqfp.md | QA R1: 29 APROVADOS, 1 AJUSTAR, 0 REPROVADO; AJ-1 no D4-R47; 15 pontos do adendo aceitos; errata AJ-L7-E1 APLICÁVEL | 1d8a9e3e5e5e51d5778e8bbf87052126e67ef21dcecb31317afa17aa2f71fc42 |
| saida/gcb/QA_DA_reforco_leva8_R2_2026-10-22_gcb-cqfp.md | QA R2, última rodada: APROVADA 0/30; 1 NÃO CONFERE de registro; registros da seção 10 | 7db44624452c9d047b3ac54f438bf5722160a09fd7d1a655887df263b2827f5f |
| saida/banco/estilo_DA_reforco_leva8.md | estilo sobre a v1 (gbq-estilo): 3 CONFORMES, 2 AJUSTE (AJ-L8-E1 e AJ-L8-E2, aplicados), 0 NÃO CONFORME; S-L8-1, S-L8-2; L8-1 a L8-3 | e5c44b7720c2bbe14d7e8537e48838e083a303f25c2d6bcf5c8ab19a01e56087 |
| saida/gcb/D4_anexo_N_adendo_2026-10-22.md | adendo do qa-normativo-da (lastro da leva 8; seção 7: errata AJ-L7-E1, CONFERE) | 44ad15bdb0b34d05be734bd1a45277d4ad98af16864acbe483a8d91fe9cdb17f |
| saida/gcb/DA_reforco_ficha_2026-10-20.md | ficha antes deste adendo, com a seção 14 inteira (14.6 inclusive) | 539f22327fb4ec7914a3cae6f2ffe22cdc89c7f873f5ff9be6bb1ad242b0eac8 |
| saida/gcb/DA_reforco_ficha_2026-10-20.md | ficha com a seção 15 "Adendo após a leva 8" (esta reconciliação; só acréscimo antes da última linha; 363.999 bytes; 1.780 linhas; 0 CR) | db4b0279e76f1daea4e70bc7fd0889c27bb1d26284c8f65d94ad181eddf7f9c8 (sem a seção 15 dá de novo 539f2232…eac8, conferido por script) |
| saida/gcb/DA_reforco_leva7_v2.md | objeto da errata AJ-L7-E1 (D3-R75) | c4f50b9ecabb3f0c99592d4bd997012b647a2b6b5b10ab5521eece385fe1f764 |
| saida/gcb/DA_reforco_leva7_reconciliacao_2026-10-22.md / QA_DA_reforco_leva7_R2_2026-10-22_gcb-cqfp.md | origem do texto da errata (seção 4.1 / seção 10) | 17f3017f…ec9ee / b438acec…c705 |
| saida/gcb/normativo_cache/Lei_4619_1965_2026-10-20.txt | cópia da Lei 4.619 (errata) | b91ef03df94717e00602b1b5195f73176c1c5cf5bebe6d80fba1cbaf37a9082f |
| saida/gcb/D4_anexo_N_mapa_normativo.md; D4_anexo_N_adendo_2026-10-20.md | lastro da leva 8 e da ficha da leva 9 | 0d98c249…a05f; c32f58eb…16fb5 |
| saida/gcb/normativo_cache/CasaCivil_GuiaPoliticaGovernanca_2018_2026-10-20.txt | cópia integral do Guia F2 (20/10/2026) | d9b00721b29610adbcea7f4d7b0e05090c2daac0120a9b558a615bd0f0aae0b9 |
| saida/gcb/normativo_cache/CasaCivil_AvaliacaoExPost_v2_2018_2026-10-20.txt | cópia integral da Fonte F3 (ficha da leva 9) | 83fc8cb993bec6198a46e3d1bb14da44c18ab3cfc60e2e505b76c4abd7467b43 |
| saida/gcb/normativo_cache/TCU_ReferencialGovernancaOrganizacional_3ed_2020_TRECHOS_2026-10-20.txt | cópia dos trechos lidos da Fonte F1 (ficha da leva 9) | 08f5ed75b3c1fe29fc701959645baa4bd68031c1b85d975aa364dab5f2fc6be9 |
| saida/gcb/D4_v2_1.md; saida/gcb/D4_ficha_lote.md | canônicos do D4 (pontos, formatos, [TS]); lista fechada da seção 5.3 | c1a7a935…e5d9; cb0b0c30…c7a0 |
| saida/pacote/pacote.json v1.13 | partida (1.159 itens) | 82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240 |
| saida/banco/moldura_ce_itens_2026-10-20.csv | moldura oficial dos canônicos | ed4b364dffbca7d9e8878591914783258fa7048c4f1837d98c3d62e34981daac |
| DECISOES.md / TAREFAS.md (antes desta escrita) | decisões vigentes (última: D-AJL7E1-RITO, linha 183) / tarefas | 3f5dc70cac1c200be392b05660bed4bb41afe50cea145fb432d67717327c588a / 29de89e08daba4e139b52a5e643878e4a68ba9e61be310837c00338909bbb8c8 |

Os SHA-256 da v1, da v2, do R1, do R2, do estilo, do adendo e da ficha coincidem com os do despacho e com os declarados nos pareceres.

## 1. Objeto aceito
**saida/gcb/DA_reforco_leva8_v2.md, SHA-256 1fdce9bde3393b445cabd75d50064fb2a2fdde103c03415dc82256c203bf6f2c**, sem alteração, com os registros desta reconciliação prevalecendo na consolidação (seções 4 a 8). São 30 itens AUTORAL, todos aprovados no R1 e no R2, na ordem do arquivo:
- 8.2: D4-R29 a D4-R38 (10; a folha fecha em 20, com 20 diretos);
- 8.3: D4-R39 a D4-R48 (10; a folha fecha em 20, com 19 diretos e 1 parcial, o D4-R44);
- 9.1: D4-R49 a D4-R58 (10; a folha fecha em 20, com 20 diretos).

Nenhum id ficou vago. Os 30 seguem com "QA PENDENTE" até o aceite (D-QA-PENDENTE); a marca sai só na exportação da GBQ.

Nenhuma oração fica pendente nesta leva. Há duas erratas de estilo (AJ-L8-E3 no D4-R42 e AJ-L8-E4 no D4-R52), abertas em rito próprio (seção 4.2). Não condicionam o aceite: sem elas, os dois itens entram como aprovados no R2.

Parte separada: o **D3-R75** (leva 7), com a errata AJ-L7-E1, tem as duas conferências favoráveis (seção 4.7).

## 2. Conferência própria
Scripts em python3 -I, somente leitura, no scratchpad da sessão, fora do repositório: gcb_l8r/conf8.py, sl8.py, plan9.py, lines9.py, seq9.py, plan9b.py, cv.py.

| conferência | resultado |
|---|---|
| SHA-256 das entradas | = seção 0 |
| Linha 1 / última linha | "# DA_reforco_leva8_v2.md — T-116 — 2026-10-22 — gerado por gcb-cpp" / "FIM DA LEVA 08 — REFORÇO DA", com LF final; 169.034 bytes, 1.011 linhas, 0 CR — CONFERE |
| Ids | 30 únicos e contínuos (D4-R29 a D4-R58), na mesma ordem nas seções 1, 2 e 3.2. Nenhum está no pacote.json v1.13 (1.159 itens) nem nas levas 1 a 7 (208 ids; o último do D4 é o D4-R28) — CONFERE |
| Seção 1 (estudante) | sem "Gabarito", [TS], "TS=", VOLÁTIL, REVERIFICAR, URL, "QA PENDENTE", Fundador, Claude, opus ou sonnet — CONFERE |
| Campos (30 blocos) | 13 campos em 30/30. itemEdital = P1-DA-<folha>, AUTORAL e QA PENDENTE no cabeçalho em 30/30. [TS] do cabeçalho = "TS=sim" = campo Troca em 16/16; nenhum [TS] em C. VOLÁTIL 0; REVERIFICAR 0. Base com URL e "consulta" em 30/30. O D4-R55 traz a URL do Anexo N1 em http, idêntica à do Anexo (regra 3), com o registro da reabertura em https — CONFERE |
| Bases | 53 trechos entre aspas do campo "trecho:", todos subcadeia do Anexo N do D4, dos adendos de 20/10 e 22/10 ou da cópia do Guia (53/53). Os 18 trechos do Guia estão na cópia (18/18). Maior soma de trechos por item: 25 palavras (D4-R36; limite 25). Nenhum item do Guia cita 22/10/2026 como consulta — CONFERE |
| C/E da leva | **14 C / 16 E (46,7%)**; faixa de 12 a 18 em 30 (regra 6) — CONFERE |
| C/E por folha | leva: 8.2 4/6, 8.3 5/5, 9.1 5/5. Folhas fechadas (pacote v1.13 + leva): 8.2 10/10, 8.3 10/10, 9.1 10/10 |
| Formatos (DEF/SUJ/SIT/NUM/PAR/APL) | leva 8/3/6/1/8/4. Com os canônicos (D4_v2_1.md, campo Formato): 8.2 6/2/4/2/4/2; 8.3 5/1/5/1/4/4; 9.1 6/2/5/0/5/2. Maior formato: 6 de 20 (DEF na 8.2 e na 9.1; teto 6) — CONFERE |
| [TS] | 16, todos E; nenhum C-isca; nenhum E sem [TS] — CONFERE |
| Mecanismos | C1 1, C2 12, C3 1, E1 5, E2 8, E3 3 (= R1, seção 6, e v2, 4.2) |
| Aderência | 29 diretos / 1 parcial (D4-R44). Diretos por folha: 8.2 20, 8.3 19, 9.1 20; piso de 10 — CONFERE |
| Moldura | leva 0 C / 4 E (D4-R35, R42, R48, R52). DA = CSV 44/9 + levas 1 a 8 (6/35, recontados nos arquivos finais) = **50/44 (53,2%)**. Por folha com os canônicos: 8.2 1/1, 8.3 2/2, 9.1 1/1; no máximo 6 por folha — CONFERE |
| Abertura × gabarito (7.4.2; L3-1) | leva: "Considere que" 6 C / 4 E (60,0% de C); declarativos 8 C / 12 E (60,0% de E). Folhas fechadas: os mínimos de 40% são cumpridos (R1, conferência 5; R2, seção 5) — CONFERE |
| Abertura da moldura (L8-1) | forma da cota em D4-R35 e D4-R48; variante em D4-R42 e D4-R52 (0 C / 2 E) — = R2, seção 9 |
| L3-3 (prefixo comum ≥ 40, com itens da leva) | 8.2: D4-R35 × D4-14, 110. 8.3: D4-R48 × D4-19, 86, e D4-R48 × D4-26, 86. 9.1: nenhum (maior, 17). Abaixo de 40: 8.2 36 (D4-R34 × D4-09); 8.3 30 (D4-R41 × D4-R44) — = R2, seção 5 |
| Extensão (L5-1) | E de 26 a 58 palavras; C de 20 a 65 — CONFERE |
| Não regressão v1 → v2 | Aplicamos à v1 os três AJ (AJ-1 do R1; AJ-L8-E1 e AJ-L8-E2 do estilo), uma vez cada, por substituição exata: cada "antes" ocorre 1 vez e cada "depois" 0 vez na v1. O resultado reproduz byte a byte as seções 1, 2 e 3 da v2. Só diferem os enunciados do D4-R35 e do D4-R48 e o bloco do D4-R47 — = R2, seção 2 |
| Teste de sequência (regra 6; 7.3; 14.4.7) | leva ECEECCEEEC·CCEECECCEE·ECEECCECCE e [TS] TnTTnnTTTn·nnTTnTnnTT·TnTTnnTnnT. Folhas acumuladas: 8.2 ECCCEEECCC·ECEECCEEEC; 8.3 ECCEEECCEC·CCEECECCEE; 9.1 CEECCECCEE·ECEECCECCE. Passam no gabarito e no [TS] — CONFERE |
| Frase do bloco 5 (registro do R2) | "49 verificações automáticas" ocorre 1 vez na v1 e 1 vez na v2. A seção 4 da v2 tem 38 linhas com "CONFERE", 51 ocorrências da palavra e 0 "NÃO CONFERE" — = R2, seção 8 |
| SHA abreviado (registro do R2) | na l. 5 da v2, "1b9903d5…ecf" (3 caracteres finais); o valor é o da v1 — = R2, seção 10, item 2 |
| Errata AJ-L7-E1 (seção 4.7) | O "antes" ocorre 1 vez na v2 da leva 7, na l. 401, e o "depois" 0 vez. Aplicada em memória, muda só a l. 401 (mesmo número de linhas). Texto da errata idêntico na reconciliação da leva 7, no R2 da leva 7, na ficha 14.3, no R1 da leva 8 e no adendo, seção 7. Na cópia da Lei 4.619 e na página reaberta em 22/10/2026: "terço" 0, "têrço" 0, "desconto" 1, "quinta parte" 1, "limite" 0 — CONFERE |
| S-L8-1 e S-L8-2 (seção 4.2) | Cada "antes" ocorre 1 vez na v2 (l. 129 e l. 151, seção 1). O "depois" da S-L8-1 ocorre 0 vez; o da S-L8-2 ocorre 3 vezes, porque é o início do D4-R35 e de outros enunciados. Aplicadas em memória, mudam só os enunciados do D4-R42 e do D4-R52: 54 → 54 e 58 → 57 palavras. Prefixos: D4-R42 × D4-R48, 93; D4-R42 × D4-19 e × D4-26, 86; D4-R52 × D4-41, 98 — = R2, seção 9 |
| Ficha da leva 9 (seção 15.4) | Plano codificado item a item (30 itens, 15 C / 15 E). Formatos, moldura, abertura, K1 a K4, fecho neutro e sequência foram refeitos por script (seq9.py: 148 combinações de folhas passam; a adotada não tem trinca). Os trechos do Anexo N e do adendo de 20/10 ocorrem 1 vez, salvo o 8º-A, § 3º, o 12-A e o 15-A, IV, que repetem o texto dos dispositivos revogados (8º, § 3º; 12; 15, IV): registro na 15.4.2. Os 15 trechos novos que dependem do adendo ocorrem na cópia do Guia F2 ou da F3, com linha e página; o H3 aparece 2 vezes (4.1 e pergunta frequente) — seção 9 |

## 3. Rito e QA
- **Adendo do qa-normativo-da** (saida/gcb/D4_anexo_N_adendo_2026-10-22.md, 44ad15bd…b17f; ficha 14.4.10, item 1; D-T116-LEVA7-ACEITE, condição (a)):
  - lastro da 8.2, da 8.3 e da 9.1: 22 linhas de lei e 11 trechos do Guia F2;
  - seção 7: conferência normativa da errata AJ-L7-E1 (CONFERE).
  - A GCB o conferiu na ficha 14.6: 15 de 15 trechos do plano; sentido confirmado nos quatro pontos de lei; aderência fixada pelo mapa (29 diretos / 1 parcial).
  - A leva foi despachada inteira, sem nova ficha nem novo gatilho (condição (d)).
- **Reabertura no planalto.gov.br**, com User-Agent de navegador. É conferência, não base (ficha 11.6; D-T120F-REDACAO):
  - adendo: 2026-10-23T01:04:11Z a 01:06:13Z (22/10, 22h04–22h06 em Brasília). Leis 9.637, 9.790, 13.019 (compilada e principal), 13.460 e 4.619: HTTP 200, bytes iguais aos do Anexo N;
  - R1: 01:57:46Z a 01:57:52Z. Seis fontes de lei (N1, N5, N6, N7, N8, N10): HTTP 200; 30 de 30 trechos de lei nas páginas do dia; "2025" só em notas tributárias da Lei 11.079 e "2026" só nos arts. 2º, parágrafo único, e 3º, XIV, da Lei 9.790, que nenhum item usa;
  - R2: 02:12:09Z a 02:12:12Z. N5, N10 e N1: HTTP 200, conferindo os três itens alterados.
  - Nenhum dispositivo da leva mudou entre 20 e 22/10/2026. A Base dos itens fica com as consultas registradas.
- **Guia F2 não reaberto, por recusa de política do www.gov.br.** O adendo fez duas tentativas reais (2026-10-23T01:04:16Z e 01:04:28Z), registradas literalmente: "curl: (56) CONNECT tunnel failed, response 403"; o estado do proxy registrou `connect_rejected` para www.gov.br:443. Pelo README do proxy, não houve terceira tentativa. O R1 e o R2 não tentaram, porque o despacho registrou a recusa. A base dos 11 itens com G/H é a cópia integral de 20/10/2026 (d9b00721…e0b9; PDF 900139b6…22fa8), admitida para este caso pela D-T116-LEVA7-ACEITE, condições (c) e (e). A página impressa foi fixada sobre a cópia por dois métodos, com controle de 5 de 5 (ficha 14.6). **A proposta do item (g) da T-120 já está escrita na ficha 14.6, item (ii), para a presidencia (competência D).** A GCB não altera TAREFAS.md nesse ponto; o pedido vai no item de gatilho.
- **R1** (gcb-cqfp, opus; não produziu nem reconcilia):
  - 29 APROVADOS, 1 AJUSTAR (D4-R47), 0 REPROVADO — **0/30 = 0,0%**, sem GATE;
  - conferências de leva: 8 de 8;
  - AJ-1 no D4-R47: o rótulo «a lei especial do usuário», sem fonte, dá lugar a «a Lei 13.460». É a regra da ficha 14.2, item 2, que o R1 conferiu na coluna J item a item;
  - pertinência dos 15 pontos do adendo: 15 aceitos (14 diretos e 1 parcial, o D4-R44), 0 recusados;
  - dúvidas (i) a (ix) do bloco à GCB julgadas, nenhuma com AJ;
  - registros: a 14.4.6, "nenhum E com absoluto inserido", é registro errado da ficha (D4-R58; L3-2 cumprida pelo D4-R50); D4-R36 fica SUJ; observações sem AJ no D4-R38 (linha 2), no D4-R43 (PAR) e no D4-R55 (ponto de vínculo mais fraco da 9.1);
  - **seção 8: errata AJ-L7-E1 APLICÁVEL** (itens (1) e (2) da ficha 14.3).
- **Estilo** (gbq-estilo; não produziu):
  - amostra designada pela ficha 14.4.8 antes da produção: 5/30 (16,7%; D4-R33, R35, R44, R48, R51), auditada **sobre a v1, em paralelo ao R1** (ficha 9.3, item 6);
  - **3 CONFORMES, 2 AJUSTE, 0 NÃO CONFORME**; sem GATE;
  - AJ-L8-E1 (D4-R35) e AJ-L8-E2 (D4-R48): a abertura da moldura passa à forma da cota, porque a variante só ocorria em E com moldura;
  - fora da amostra, sem veredito: S-L8-1 (D4-R42) e S-L8-2 (D4-R52);
  - recomendações L8-1 a L8-3 para a leva 9.
- **R2** (última rodada):
  - os três AJ foram aplicados literalmente, uma vez cada; D4-R35, D4-R47 e D4-R48 APROVADOS; os 27 restantes idênticos;
  - **0/30 = 0,0% — APROVADA**; acumulado no rito: 0/30;
  - **NÃO CONFERE: 1, de registro** (frase "49 verificações automáticas" do bloco 5; seção 4.1);
  - registros: abertura variante residual no D4-R42 e no D4-R52 (errata da 7.6 possível, decisão da GCB; seção 4.2); SHA abreviado (seção 4.3); os três pares de prefixo não pedem nota (seção 4.4).
- L3-1 a L7-3, o item 4 da 13.2 e os itens 1 e 2 da 14.2 foram conferidos no R1, no R2, no estilo e aqui (seção 2): **cumpridos**. A L3-3 foi recontada na v2 depois dos AJ que mudaram a abertura (14.2, item 1).
- Nenhum gabarito está em disputa. O aceite pedido é do objeto, não "com ressalva". Os registros estão fechados pelas decisões da seção 4. As erratas AJ-L8-E3 e AJ-L8-E4 não condicionam o aceite.

## 4. Decisões da GCB (D1)

### 4.1 NÃO CONFERE de registro do R2 ("49 verificações automáticas", bloco 5, l. 976 da v2): registro, sem errata
**Decisão: vale o texto do R2, registrado aqui, sem errata:** «na v2, o número de verificações da seção 4 não é declarado; vale "0 com resultado NÃO CONFERE", conferido pelo R2».

Fundamentos:
- (a) o número 49 não se reproduz da seção 4, nem na v1 nem na v2 (38 linhas, 45 ou 51 ocorrências, conforme a contagem; seção 2);
- (b) o que importa continua verdadeiro: a seção 4 da v2 não tem nenhum NÃO CONFERE, e o R2 a refez inteira;
- (c) o bloco 5 não vai ao pacote.json e não há v3 (ficha 4.3; regra 15);
- (d) é o mesmo tipo do NÃO CONFERE de registro da leva 7, também fechado por registro (reconciliação da leva 7, 4.3; fichas 11.3, 12.3 e 14.3).

Regra para as levas seguintes (ficha 15.2, item 5): número de verificações no bloco 5 só com a contagem que o produziu; linha que deixou de valer é marcada na Resposta à R1.

### 4.2 Abertura variante residual no D4-R42 e no D4-R52 (S-L8-1 e S-L8-2): errata AJ-L8-E3 e AJ-L8-E4, em rito próprio
**Decisão: a GCB abre as erratas da seção 7.6 com o texto do estilo.** As erratas não condicionam o aceite dos dois itens: sem elas, entram como aprovados no R2 (defeito só de forma, como o D3-R18 sem a AJ-L2-E1).

Textos (substituição exata no enunciado, seção 1 da v2; cada "antes" ocorre 1 vez no arquivo):
- **AJ-L8-E3 | D4-R42** (l. 129): antes «Considere que um expositor, em audiência pública de comissão da Câmara dos Deputados, trate da participação social.» → depois «Considere que, em audiência pública de comissão da Câmara dos Deputados, um expositor trate da participação social.»
- **AJ-L8-E4 | D4-R52** (l. 151): antes «Considere que um expositor, ouvido em audiência pública de comissão da Câmara dos Deputados, afirme que,» → depois «Considere que, em audiência pública de comissão da Câmara dos Deputados, um expositor afirme que,»

Fundamentos:
- (a) A pista é sistemática e sanável por texto. Com os AJ-L8-E1 e AJ-L8-E2, a variante de abertura ficou em 0 C / 2 E no D4 com moldura. Em cada folha fechada (8.3 e 9.1), o único item com variante é E, e os C com moldura usam a forma da cota (R2, seção 9; estilo, seção 4, item 4). O estilo julgou essa pista digna de AJUSTE nos dois itens da amostra, e os dois restantes têm a mesma forma.
- (b) O texto é do gbq-estilo, e não da gcb-cqfp. Por isso a conferência de conteúdo pode ficar com a gcb-cqfp sem ferir a separação (D-AJL7E1-RITO: o critério só desloca o juízo quando a própria QA redigiu o texto).
- (c) A errata não muda ponto, gabarito, Troca, mecanismo, formato, moldura, tipo, fecho nem aderência. Só reordena a cena da moldura e tira «ouvido». A GCB a lê como texto de forma, e não de "construção" no sentido da 7.6 (o exemplo da 7.6, AJ-E3, mudava a troca). Mesmo assim, ela só entra com QA própria.
- (d) Efeito sobre o prefixo, conferido por script: D4-R42 × D4-R48, 93 caracteres; D4-R42 × D4-19 e × D4-26, 86; D4-R52 × D4-41, 98. As cenas são distintas até o fecho, e nenhuma nota é exigida, pelo mesmo raciocínio do R2, seção 5. É o efeito buscado pela L8-1 (seção 4.5).
- (e) Não é complemento sem ordem (D-COMPLEMENTOS): o texto vai ao pacote.json (enunciado) e corrige pista apontada pelo estilo e pelo R2 dentro do rito da leva. O rito é o da 7.6, lida pela D-T116-LEVA1-ACEITE, parte (II).
- (f) A alternativa (registro sem errata) deixaria a pista em dois itens canônicos, sem saída posterior, já que não há v3.

**Conferência (ficha 15.3):**
- a **gcb-cqfp**, em seção própria do R1 da leva 9 ("Erratas AJ-L8-E3 e AJ-L8-E4 (leva 8)"), separada do veredito da leva 9, confere:
  - (1) cada "antes" ocorre exatamente 1 vez na v2 (1fdce9bd…f6f2c), na seção 1, e o "depois" da E3 0 vez (o da E4 ocorre 3 vezes como início de outros enunciados; a substituição é única pelo "antes");
  - (2) gabarito, ponto, Troca, mecanismo, formato APL, moldura S (tipo e fecho), aderência, abertura CQ e bloco da seção 2 ficam inalterados;
  - (3) o enunciado resultante, lido inteiro, não muda o sentido, não cria pista e fica na faixa de extensão (54 e 57 palavras);
  - (4) os prefixos acima, com cena distinta até o fecho.
- Veredito: CONFERIDO / NÃO CONFERIDO.
- Não é terceira rodada da leva 8, não altera o arquivo da leva 8 e não é QA aberto que impeça a leva 9.

**Destino:**
- o gatilho A desta leva pergunta só o tratamento (parte (III));
- o texto é perguntado no gatilho A da leva 9, depois da conferência;
- aceito, a GBQ aplica na consolidação (T-123, se o aceite vier antes da geração final da v1.14, ou na seguinte), por substituição exata na seção 1 do arquivo da leva 8, com aborto se o "antes" não ocorrer exatamente 1 vez, registro por id e conferência da gbq-cqe;
- sem aceite, o D4-R42 e o D4-R52 ficam como aprovados no R2.

### 4.3 SHA abreviado com 3 caracteres (v2, l. 5, "1b9903d5…ecf"): registro, sem errata
**Decisão: registro.** O valor é o da v1. As outras entradas usam 4 caracteres ("…8ecf"). O cabeçalho de entradas não vai ao pacote.json. Errata só de registro seria complemento sem ordem (D-COMPLEMENTOS). É o mesmo critério das fichas 11.3 e 13.3. Regra: ficha 15.2, item 5.

### 4.4 Pares de prefixo da L3-3 (D4-R35 × D4-14, 110; D4-R48 × D4-19 e × D4-26, 86): sem nota
**Decisão: nenhuma nota obrigatória e nenhuma nota comum nova.**

Fundamentos (R2, seção 5):
- (a) a L3-3 trata de cenário literal idêntico até o fecho, e os três pares divergem antes da norma citada;
- (b) nenhum item entrega o gabarito do outro, que é o critério das notas obrigatórias, como (db), (ci) e (cl);
- (c) o prefixo comum é o efeito buscado pelo AJ: os E com moldura passam à forma de abertura dos C da folha. Separá-los em simulado recriaria a separação por forma que o AJ desfez.

O par D4-R48 × D4-26 já está na nota comum (dj). A mesma leitura vale para os prefixos das AJ-L8-E3 e AJ-L8-E4, se aceitas. A regra L8-1 (seção 4.5) a fixa para as levas seguintes.

### 4.5 Recomendações L8-1 a L8-3 do estilo: aceitas, com uma faixa e uma regra da GCB (ficha 15.2)
1. **L8-1 (abertura da moldura): aceita no texto do estilo.** Nos itens com moldura de expositor (folhas 8.x e 9.x), a abertura segue a forma da cota, qualquer que seja o gabarito. Variante só entra se o lote tiver C com moldura com a mesma variante. Prefixo comum de 40 ou mais caracteres com canônico da folha é registrado na seção 4 e não impede o item quando a cena diverge antes do fecho. A seção 4 da leva conta abertura da moldura × gabarito no lote acumulado.
2. **L8-2 (abertura de atribuição nos declarativos): aceita, com faixa.** O D4 acumulado (136 itens) tem "Nos termos d…" 5 C / 12 E e "Segundo …" 8 C / 18 E. Por isso, entre os declarativos novos do D4 que abrem com uma dessas expressões, a leva tem **de 50% a 75% de C**. O teto evita criar na folha fechada a pista inversa. A seção 4 conta abertura de atribuição × gabarito por folha fechada e no D4 acumulado. "De acordo com …" (8 C / 3 E) e "Conforme …" (2 C / 0 E) ficam de preferência com E novos.
3. **L8-3 (fecho neutro × moldura): aceita.** Hoje, com moldura, 1 C / 4 E; sem moldura, 3 C / 1 E. Na leva 9, nenhum E com moldura usa o fecho neutro. O fecho neutro novo vai a C sem moldura.
4. **L8-4 (regra da GCB, decorrente da L8-3 e de K2): fecho dos E com moldura no D4.** O K2 estrito («a afirmação do expositor é correta») está em 7 C / 9 E (43,8%), e um só E a mais o leva abaixo de 40%. Por isso, os E novos com moldura usam os fechos que hoje só ocorrem em C: «a afirmação do expositor está correta» (5 C / 0 E) e «a afirmação do expositor corresponde ao que o decreto prevê» (2 C / 0 E). Com isso, K2 estrito fica em 7/9, e K2 pela detecção larga da GCB vai a 12/14 (46,2%). A seção 4 conta fecho × moldura × gabarito no D4 acumulado.

Nenhuma das quatro tem efeito sobre os 30 itens da leva 8, salvo o que a seção 4.2 decide para o D4-R42 e o D4-R52.

### 4.6 Outros registros (D1)
1. **AJ-1, AJ-L8-E1 e AJ-L8-E2:** aceitos. Foram aplicados na v2 e conferidos no R2 por substituição exata. Não mudam gabarito, [TS], formato, moldura, aderência, abertura CQ/DC, fecho ou sequência. Extensões: 48 (D4-R35) e 44 (D4-R48). O efeito na L3-3 foi previsto pelo estilo e recontado na v2 (14.2, item 1).
2. **Justificativas (14.2, item 2):** a coluna J foi conferida no R1 item a item. O único rótulo sem fonte (D4-R47) saiu pelo AJ-1. Nenhuma oração fica pendente; o gate do CLAUDE.md não tem objeto nesta leva.
3. **Pertinência dos 15 pontos do adendo:** aceita pela gcb-cqfp (R1, seção 3). O **D4-R44 fica "Aderência: parcial"**: conta para a meta de 20 e vai só a simulado diagnóstico (D-ADERENCIA). Nenhuma folha fica abaixo de 20 nem abaixo do piso de 10 diretos.
4. **Ficha 14.4.6, "nenhum E com absoluto inserido":** é registro errado da ficha, e não regra (R1, dúvida (vi)). A regra aplicável é a L3-2, cumprida pelo D4-R50 ("tudo", literal de G1) na 9.1. Corrigido na ficha 15.3, sem efeito no item. O R1 sugeriu pesar o D4-R58 na amostra da leva 9. O plano da leva 9 não tem E com absoluto inserido, e a amostra cobre a regra pela contagem de absolutos da seção 4 (registro).
5. **D4-R36 fica SUJ** (R1, dúvida (ii)): a troca recorta o sujeito ("distintas das" → "inclusive as"). Como DEF, a 8.2 iria a 7 em 20, acima do teto.
6. **Observações do R1 sem AJ:**
   - D4-R38: a linha 2 da justificativa explica mal a tentação, mas não afirma nada fora da Base;
   - D4-R43: PAR defensável;
   - D4-R55: ponto de vínculo mais fraco da 9.1 (o Anexo dá o art. 4º, II, como "núcleo 9.4; compl. 9.1"). A ficha 14.4.4 o fixou como direto, e a GCB mantém "direta". A diretriz é das que o Anexo marca para a 9.1, e o item não julga o alcance do decreto.
7. **Mecanismos:** C1 1, C2 12, C3 1, E1 5, E2 8, E3 3. O campo não vai ao pacote.json.
8. **Núcleo** (ficha 14.1; D-NUCLEO-CRITERIO): os 30 são false (a 8.2, a 8.3 e a 9.1 têm 10 canônicos cada).
9. **Ordem na folha e ids** (fichas 7.3 e 14.1): canônicos na ordem do pacote v1.13; depois, a leva 8 na ordem do arquivo (8.2 = R29–R38; 8.3 = R39–R48; 9.1 = R49–R58). A consolidação é por itemEdital. O reforço do D4 chega a D4-R58; a leva 9 segue em D4-R59.
10. **Rede:** o planalto.gov.br respondeu HTTP 200 em todas as reaberturas do adendo, do R1 e do R2, com User-Agent de navegador. O SHA do HTML muda a cada pedido (bloco `f5_cspm`; adendo, seção 1); a comparação foi sobre o texto. O www.gov.br foi recusado pela política do ambiente (seção 3). Registro, sem medida.
11. **Notas de simulado:** (db) a (ds), (w) e (x) com os ids finais, iguais aos da ficha 14.4.9. A (db) é obrigatória. A produção não fez acréscimo (seção 7).

### 4.7 ERRATA AJ-L7-E1 (D3-R75, leva 7) — CONFERE (qa-normativo-da) e APLICÁVEL (gcb-cqfp): reconciliada; D3-R75 apto ao aceite com a errata
**Decisão: os dois vereditos exigidos pela D-T116-LEVA7-ACEITE, parte (II), e pela D-AJL7E1-RITO são favoráveis e se completam.** A GCB leva ao gatilho A, como parte separada, o aceite do **D3-R75 com a errata aplicada** (item e texto final da linha 2 juntos), na forma da D-T116-LEVA7-ACEITE (II).

Texto (ficha 14.3; reconciliação da leva 7, 4.1; R2 da leva 7, seção 10), substituição exata na seção 2 de saida/gcb/DA_reforco_leva7_v2.md (c4f50b9e…f764), l. 401:
- antes «; a tentação é lembrar de outro limite de desconto fora desta lei (o valor “terço” não ocorre na Lei 4.619).»
- depois «; o valor “terço” não ocorre na Lei 4.619, cujo único limite de desconto é o do art. 6º.»
- Linha 2 resultante: «O item troca “uma quinta parte” por “um terço”, teto maior, o que contradiz o limite da letra; o valor “terço” não ocorre na Lei 4.619, cujo único limite de desconto é o do art. 6º.»

As duas conferências:
1. **Conferência normativa — qa-normativo-da (opus; não redigiu o texto nem o item), adendo, seção 7: CONFERE (CONFERIDO).**
   - Página reaberta: https://www.planalto.gov.br/ccivil_03/leis/1950-1969/l4619.htm, 2026-10-23T01:04:15Z, HTTP 200, 8.562 bytes, SHA-256 do HTML 2d8e883c…e4f2, User-Agent de navegador, comando registrado. Cópia de 20/10/2026: b91ef03d…082f.
   - "terço", "têrço", "um terço", "1/3" e "terça": 0 vez nas duas.
   - "desconto": 1 vez, só no art. 6º («não excederá de uma quinta parte»). "quinta parte": 1. "limite": 0, porque o "limite" do texto é leitura fiel de «não excederá de».
   - Nenhuma nota de alteração.
   - A proposição fala só da Lei 4.619 e não afirma nada sobre outra norma.
   - Esse veredito cobre o item (3) e o que restava do item (4) da ficha 14.3, na divisão da D-AJL7E1-RITO, item (2).
2. **Aplicação mecânica — gcb-cqfp, R1 da leva 8, seção 8: APLICÁVEL (= CONFERIDO nos itens (1) e (2) da ficha 14.3).**
   - (1) o "antes" ocorre 1 vez na v2 da leva 7, na l. 401 ("Justificativa (linha 2)" do bloco do D3-R75), e o "depois" 0 vez;
   - (2) aplicada em memória, só essa linha muda. Cabeçalho, itemEdital, ponto, formato NUM, moldura N, aderência parcial, gabarito E, linha 1, tipo de base, Base, mecanismo E3, Troca («não excederá de uma quinta parte (art. 6º) → não excederá um terço»), "Difere de", Marcas e o enunciado da seção 1 ficam iguais.
   - A gcb-cqfp não julgou o conteúdo do texto que ela mesma redigiu no R2 da leva 7, como manda a D-AJL7E1-RITO.

Reconciliação da GCB:
- (a) a conferência própria (seção 2) confirma as contagens: o "antes" 1 vez e o "depois" 0 vez; diff de uma linha; o texto é idêntico nas cinco fontes que o transcrevem; na cópia e na página, "terço" 0, "desconto" 1, "quinta parte" 1 e "limite" 0;
- (b) a linha 2 resultante descreve a troca do item e só afirma o que a Base e a lei dizem. A oração sem fonte («outro limite de desconto fora desta lei») sai inteira;
- (c) com os dois vereditos favoráveis, o motivo da exclusão do D3-R75 na D-T116-LEVA7-ACEITE (a oração PENDENTE no texto do item) deixa de existir, desde que a errata seja aceita junto com o item;
- (d) a errata não muda Troca, gabarito, ponto nem construção;
- (e) não é terceira rodada da leva 7 e não altera o arquivo da leva 7.

**Destino (parte (II) do gatilho):** aceito, a GBQ aplica a errata na consolidação da v1.14 (T-123), por substituição exata na seção 2 do arquivo da leva 7, com aborto se o "antes" não ocorrer exatamente 1 vez, registro por id (D3-R75) e conferência da gbq-cqe na fidelidade. Efeitos:
- a **6.1 passa a 20** (11 C / 9 E; 12 diretos e 8 parciais, com o D3-R75 parcial);
- a nota (y-7) volta a 8 itens, e a (z-7) se extingue;
- a moldura não muda (o D3-R75 é Moldura N).

Recusado, o D3-R75 fica fora da v1.14, e a GCB decide por D1 se a 6.1 fecha em 19 com registro ou se recebe item da reserva numa leva seguinte, com QA normal (D-T116-LEVA7-ACEITE (II)).

## 5. Aderência
| folha | canônicos (pacote v1.13) | leva 8 | folha fechada | piso de 10 diretos |
|---|---|---|---|---|
| 8.2 | 10 diretos | 10 diretos | 20 diretos | cumprido |
| 8.3 | 10 diretos | 9 diretos / 1 parcial (D4-R44) | 19 / 1 | cumprido |
| 9.1 | 10 diretos | 10 diretos | 20 diretos | cumprido |
| leva | — | **29 / 1** | — | — |

A pertinência do D4-R44 é parcial: a periodicidade da pesquisa de satisfação é avaliação continuada pelo usuário, apoio à participação cidadã, e não a participação mesma (R1, seção 3; ficha 14.6). O item só vai a simulado diagnóstico. Os pontos "compl." do Anexo ficam diretos quando a ficha os fixou assim e a gcb-cqfp não recusou (D4-R43, D4-R55).

## 6. Moldura acumulada (D-MOLDURA-CE) — conferida
Conferência por script nos arquivos finais das levas 1 a 8 (campo "Moldura") e no CSV oficial dos canônicos:

| conjunto | C / E com moldura | %C | faixa de 40% a 60% |
|---|---|---|---|
| DA, partida (CSV, pacote v1.13) | 44 / 9 | 83,0% | acima |
| DA depois da leva 7 (29 aceitos; o D3-R75 é N) | 50 / 40 | 55,6% | dentro |
| leva 8 | +0 / +4 | — | — |
| **DA depois da leva 8** | **50 / 44** | **53,2%** | **dentro — meta mantida (= DA 50/44 esperado, ficha 14.4.6)** |
| D4 (K1) depois da leva 8 | 14 / 10 | 58,3% | dentro |
| D3 / D2 (sem item novo) | 9 / 13 / 10 / 14 | 40,9% / 41,7% | dentro |
| **DA esperado depois da leva 9 (ficha 15.4.6)** | **50 / 49** | **50,5%** | dentro |
| D4 (K1) esperado depois da leva 9 | 14 / 15 | 48,3% | dentro |

- A leva 8 cumpriu as cotas da T-122 (8.2 1 E; 8.3 2 E; 9.1 1 E), sem C com moldura (R3 sem par a exigir). Há 35 E novos com moldura nas levas 1 a 8 (≥ 21 da meta da T-122), e 2 × 50 = 100 ≤ 3 × 44 = 132.
- Conjuntos do D4 depois da leva 8:
  - K2 7/9 (43,8%; pela detecção larga, 12/9 = 57,1%);
  - K3 5/4;
  - K4 31/22 (58,5%);
  - fecho neutro 4/5 (44,4%);
  - ", e não" 2/2.
- Condições (as da D-T116-LEVA7-ACEITE):
  - (a) o 50/44 conta os 4 E desta leva e vale com o aceite do gatilho A (sem ele, DA fica em 50/40, 55,6%);
  - (b) a contagem é da GCB sobre o pacote v1.13 + levas; a recontagem oficial é da GBQ, pelo script reaplicado à v1.14 (T-123);
  - (c) a regra (c) da D-MOLDURA-CE (T-119: C ≤ E com moldura em cada simulado) continua até a recontagem oficial, com fim por D1 da GBQ;
  - (d) as levas 9 a 12 seguem só com as cotas da T-122 (leva 9: 0 C / 5 E).

## 7. Notas de simulado — "não pôr no mesmo simulado" e restrições de uso da leva 8
Destino: T-119 (regra de montagem) e T-123 (campos de montagem). Continuam (a) a (da) das levas 1 a 7.

| # | itens | motivo | origem |
|---|---|---|---|
| (db) **OBRIGATÓRIA** (par indicado) | D4-R29 × D4-R34 (obrigatória); D4-R29 × D4-09 e D4-12 (comum) | o C do D4-R34 («modalidade patrocinada ou administrativa») entrega o E do D4-R29 (concessão comum) | ficha 14.4.9; R1, 2 e 9 |
| (dc) | D4-R31 × D4-11 e D4-07 | instrumentos da Lei 13.019 (art. 2º, III, VII, VIII e VIII-A) | ficha 14.4.9 |
| (dd) | D4-R32 × D4-16 | qualificação de OSCIP (Lei 9.790, art. 1º) | idem |
| (de) | D4-R33 × D4-R36 | OSC (Lei 13.019, art. 2º, I, a e c) | idem |
| (df) | D4-R35 × D4-13 | vedações de PPP (Lei 11.079, art. 2º, § 4º) | idem |
| (dg) | D4-R37 × D4-15 | organização social (Lei 9.637, arts. 1º e 5º) | idem |
| (dh) | D4-R30, D4-R38 e D4-10 | Guia F2, silos e redes: no máximo 2 por simulado | idem |
| (di) | D4-R39, D4-R41, D4-R47 e D4-21 | Lei 13.460, art. 1º: no máximo 2 por simulado | idem |
| (dj) | D4-R40 × D4-R48 × D4-26 | participação do usuário (conselhos de usuários; art. 6º, I) | idem |
| (dk) | D4-R43 × D4-17 e D4-67 | transparência: princípio (art. 3º, VI) × diretriz (art. 4º, XI) | idem |
| (dl) | D4-R45 × D4-24 | divulgação de informações (Lei 13.460, art. 6º, VI × LAI, art. 8º) | idem |
| (dm) | D4-R42 × D4-18 e D4-20 | participação social (Guia F2; R12; R13) | idem |
| (dn) | D4-R46 × D4-17 e D4-23 | transparência ativa (Guia F2; R14; R15) | idem |
| (do) | D4-R49, D4-R50, D4-R56, D4-R58, D4-35, D4-36 e D4-43 | conceito de governança (Guia F2, Cap. I; Decreto, art. 2º, I; R20; R23): no máximo 2 por simulado | idem |
| (dp) | D4-R51 × D4-R52 | Banco Mundial × OCDE (Guia F2, Cap. I) | idem; R1, (ix) |
| (dq) | D4-R53, D4-R57 e D4-40 | alinhamento (R22; Guia F2): no máximo 2 por simulado | idem |
| (dr) | D4-R54, D4-38 e D4-39 | governança × governabilidade (R21): no máximo 2 por simulado | idem |
| (ds) | D4-R55 × D4-68 | diretrizes do art. 4º (II × VI) | idem |
| (w) | a leva 8 inteira (ou só itens de reforço) | não forma simulado isolado; entra misturada por folha com os canônicos | ficha 14.4.9 |
| (x) | os 4 itens com moldura (D4-R35, D4-R42, D4-R48, D4-R52) | contam para o teto de 50% de C com moldura por simulado | D-MOLDURA-CE (c) |
| (y-8) | D4-R44 (parcial) | só simulado diagnóstico | D-ADERENCIA; R1, 3 |
| (y-7) e (z-7), atualização | D3-R75 | com o aceite da parte (II) do gatilho, a (z-7) se extingue, e a (y-7) volta a 8 itens (D3-R70, R72, R73, R75, R76, R77, R78, R79). Sem o aceite, ficam como na D-T116-LEVA7-ACEITE | seção 4.7 |

As reservas das três folhas não foram usadas (R1, seção 4). Os 30 itens só vão a simulado depois do gatilho A aceito e da consolidação (D-QA-PENDENTE); nenhum é VOLÁTIL. As notas da leva 9 começam em (dt) (ficha 15.4.9).

## 8. Para a GBQ (T-123, consolidação v1.14)
1. Fonte: saida/gcb/DA_reforco_leva8_v2.md (1fdce9bd…f6f2c; 169.034 bytes), com esta reconciliação prevalecendo (precedente D-T89-R1-ACEITE).
2. Ato de aceite desta leva para os 30 ids no gerador. Núcleo false nos 30 (seção 4.6, item 8); ordem pela seção 4.6, item 9; aderência: 29 diretas e 1 parcial (D4-R44).
3. Nenhum texto de item muda além do que a v2 traz (enunciados do D4-R35 e do D4-R48 com AJ-L8-E1 e AJ-L8-E2; justificativa, linha 2, do D4-R47 com AJ-1).
   - **AJ-L8-E3 e AJ-L8-E4** (D4-R42, D4-R52): não aplicar até o aceite do texto no gatilho A da leva 9. Aceitas, aplicar por substituição exata na seção 1, com aborto se o "antes" não ocorrer exatamente 1 vez, registro por id e conferência da gbq-cqe. O "depois" da E4 já ocorre 3 vezes no arquivo, e a unicidade é pelo "antes".
4. **D3-R75 (leva 7), se a parte (II) for aceita:** aplicar a AJ-L7-E1 por substituição exata na seção 2 de saida/gcb/DA_reforco_leva7_v2.md (c4f50b9e…f764), l. 401, com aborto se o "antes" não ocorrer exatamente 1 vez, registro por id e conferência da gbq-cqe. O D3-R75 entra na 6.1 depois do D3-R74, na ordem do arquivo da leva 7, núcleo false, "Aderência: parcial". Sem o aceite, o D3-R75 fica fora da v1.14.
5. Notas da seção 7 nos campos de montagem, com a (db) obrigatória no escopo indicado.
6. Recontagem da moldura na v1.14: DA 50/44 (53,2%) depois da leva 8 (o D3-R75 não muda a conta); D4 K1 14/10. A meta da D-MOLDURA-CE fica mantida na contagem da GCB. A recontagem oficial é da GBQ, e o fim da regra (c) da T-119 depende da D1 da GBQ sobre ela.
7. Com a leva 8, as folhas 8.2, 8.3 e 9.1 fecham em 20. O reforço do D4 vai a D4-R58.

## 9. Pendências com destino
| pendência | destino | condição |
|---|---|---|
| **D3-R75 com a errata AJ-L7-E1** | gatilho A desta leva, parte (II); aplicação pela GBQ na T-123 | conferências favoráveis (seção 4.7); sem aceite, fica fora da v1.14 |
| **Erratas AJ-L8-E3 e AJ-L8-E4** (D4-R42, D4-R52) | tratamento: gatilho A desta leva, parte (III). Conferência: gcb-cqfp, seção própria do R1 da leva 9. Texto: gatilho A da leva 9 | sem aceite ou sem CONFERIDO, os dois ficam como aprovados no R2 |
| **Item (g) da T-120** (Guia F2, PDF não reaberto em 22/10/2026) | proposta para a presidencia (competência D), texto na ficha 14.6, item (ii), repetido no item de gatilho | a GCB não altera TAREFAS.md nesse ponto |
| Notas (db) a (ds), (w), (x), (y-8); atualização de (y-7) e (z-7) | T-119 e T-123 | antes do primeiro simulado com DA |
| Regras da ficha 15.2 (L8-1 a L8-4; bloco 5) | produção e QA da leva 9 em diante; conferência na reconciliação | toda leva |
| Frase "49 verificações", SHA abreviado, pares de prefixo, 14.4.6 (absolutos), D4-R36 SUJ, observações do R1 | fechados (seções 4.1, 4.3, 4.4 e 4.6): sem errata e sem medida no item | sem ação |
| Meta da D-MOLDURA-CE | mantida na contagem da GCB (50/44); recontagem oficial da GBQ na v1.14 (T-123); fim da regra (c) da T-119 por D1 da GBQ | com o aceite desta leva |
| **Leva 9 — (a) despachável?** | **NÃO é despachável já.** A 9.4 tem lastro exato no Anexo (Decreto 9.203 integral) e fecha em 20 sem adendo. A 9.2 tem 9 pontos firmes do Anexo e do adendo de 20/10 para 10 itens. A **9.3 tem 3 pontos firmes** (art. 6º, parágrafo único, I; art. 3º, I; R59) para 10 itens. A leva sai inteira (ficha 14.4.2 (a); precedentes das levas 5, 7 e 8). Esta é a última etapa da sessão s16: a leva 9 fica para a próxima sessão | depois do adendo e da conferência da GCB (ficha 15.4.10, itens 1 e 2; seção 15.6, a acrescentar) |
| **Leva 9 — (b) adendo do qa-normativo-da** | **precisa**, com escopo fechado (ficha 15.4.2 (b)), em arquivo novo saida/gcb/D4_anexo_N_adendo_<data ISO>.md:<br>– **9.3**: Guia F2 (Fonte F2), três trechos — H3, seção 4.1, capacidade de resposta (l. 1407–1409; p. 40); H4, quatro resultados desejáveis segundo o Banco Mundial (l. 908–910; p. 29); H5, três fontes de legitimidade (l. 608–612; p. 21). Guia prático de análise ex post (Casa Civil, 2018; Fonte F3 do Anexo N), quatro trechos — F3a, percepção da população atendida (l. 1497–1498; p. 32 impressa); F3b, critérios dos indicadores (l. 1491–1494; p. 32); F3c, grupo contrafactual (l. 1533–1535; p. 33); F3d, Boxe 1, quando executar a avaliação de impacto (l. 600–602; p. 15);<br>– **9.2**: Guia F2, um trecho — G10, seção 6.1, alta administração (l. 2799–2801; p. 68);<br>– **reserva**: G11 (l. 1552–1553; p. 42), G12 (Tabela 7, l. 3145–3147; p. 74) e F3e (l. 1528–1529; p. 33);<br>– nada de lei (a 9.4 e os dispositivos da 9.2 e da 9.3 estão no Anexo, seção 4.1).<br>**URLs** (as do Anexo N do D4, Fontes F2 e F3): https://www.gov.br/casacivil/pt-br/assuntos/governanca/comite-interministerial-de-governanca/arquivos/guia-da-politica-de-governanca-publica_versao-defeso.pdf; https://www.gov.br/casacivil/pt-br/assuntos/governanca/comite-interministerial-de-governanca/arquivos/avaliacao-de-politicas-publicas-guia-pratico-de-analise-ex-post.pdf.<br>**Rede**: o planalto.gov.br responde com User-Agent de navegador, mas o adendo não precisa dele; o **www.gov.br está recusado pela política** do ambiente (403 no CONNECT, em 22/10/2026). Cada PDF tem uma tentativa real, registrada literalmente, sem desvio e sem repetir a recusa (README do proxy). A base fica nas cópias de 20/10/2026 (Guia d9b00721…e0b9; F3 83fc8cb9…7b43, cópia integral por pdftotext do PDF 829ef2a0…a8c0), com a página impressa fixada sobre a cópia (F2: desvio 0; F3: −4, conforme o Anexo N, seção 1) | despacho do orquestrador na próxima sessão, depois do gatilho A desta leva (a sessão para aqui; CLAUDE.md). Faz parte do primeiro passo da T-116 e da regra do lastro "A CONFIRMAR" (ficha 2.1), sem tarefa nova (D-COMPLEMENTOS). O uso das duas cópias para trechos novos depende da mesma leitura da D-T116-LEVA7-ACEITE, (c) e (e) (ficha 15.4.2 (b), último item) |
| **Leva 9 — (c) folha abaixo de 20** | **Com o adendo, nenhuma** (9.2 20, com 3 pontos de reserva; 9.3 20, com 3; 9.4 20, com 6). **Sem o adendo, a 9.3 fica abaixo de 20:** chegaria a 13 ou 14, e a leva precisaria de nova ficha. A 9.2 fecharia em 20 só com a reserva do Anexo (Decreto 9.203, art. 17, caput, quase gêmeo do D4-73 da 9.4), com registro. A 9.4 fecha em 20 sem adendo. Se a gcb-cqfp recusar pertinência de ponto do adendo, a folha fecha menor, com registro (ficha 2.1). Nenhuma folha fica abaixo do piso de 10 diretos (os 10 canônicos de cada folha são diretos) | reconciliação da leva 9 |
| T-120 | se o adendo da leva 9 usar as cópias do Guia F2 e da F3 sem reabrir os PDFs, a GCB registra na conferência (seção 15.6, a acrescentar) e propõe à presidencia o item correspondente da T-120 (F3; e, no Guia, os ids novos que a (g) não lista). Nada a acrescentar por esta reconciliação além da (g) | conferência do adendo da leva 9 |
| Ordem das folhas 8.2, 8.3 e 9.1 e faixas (ficha 14.1) | T-123 | consolidação por itemEdital |

## 10. Gatilho
Tudo em condição:
- adendo do qa-normativo-da conferido (ficha 14.6);
- QA independente concluído em 2 rodadas: 0/30 no R1 e no R2, APROVADA; 1 NÃO CONFERE só de registro, fechado na seção 4.1;
- estilo sobre a v1 sem NÃO CONFORME, com os dois AJ aplicados;
- SHA-256, contagens, C/E, formatos, moldura (meta mantida), aderência (1 parcial aceito), pontos, bases (53/53 no lastro; 18/18 na cópia do Guia), abertura, L3-1 a L7-3, 14.2 e sequência conferidos por script;
- não regressão: v1 + AJ-1, AJ-L8-E1 e AJ-L8-E2 = v2;
- errata AJ-L7-E1 com CONFERE do qa-normativo-da e APLICÁVEL da gcb-cqfp, reconciliada na seção 4.7;
- erratas AJ-L8-E3 e AJ-L8-E4 abertas em rito próprio (seção 4.2), sem condicionar o aceite.

O gatilho A está escrito em PARA_PRESIDENCIA.md, num item com pergunta fechada em três partes:
- (I) os 30 itens D4-R29 a D4-R58;
- (II) o D3-R75 com a errata AJ-L7-E1 aplicada;
- (III) o tratamento das erratas AJ-L8-E3 e AJ-L8-E4.

O item leva também o pedido de acréscimo do item (g) à T-120, como proposta para a competência D. Nada vai à plataforma nem à candidata sem o sim do Fundador.

FIM DA RECONCILIAÇÃO — LEVA 08 — REFORÇO DA
