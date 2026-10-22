# estilo_DA_reforco_leva3.md — T-116 — 2026-10-22 — gerado por gbq-estilo

Auditoria de estilo Cebraspe da amostra da leva 3 do reforço de DA (D-REFORCO-2, regra 6; D-REFORCO-DA; ficha, seções 5, 7.4, 7.6, 8.3.8, 8.4.8 e 9.3). Ciclo s16c1. Destino: gcb-cqfp (os AJ abaixo seguem com os AJ do R1 para a v2 e são conferidos no R2) e gcb-gerencia (reconciliação da leva 3). Este agente audita e não produz. Nenhum outro arquivo foi alterado; regras/estilo_banca.md não foi tocado. Sem commit nem push.

**Resultado:** 4 itens auditados (13,3% de 30), sobre a **v1**, em paralelo ao R1 (ficha 9.3, item 6). Vereditos: 2 CONFORMES (D3-R33 e D3-R24), 2 AJUSTE (texto) (D3-R44 e D3-R50), 0 NÃO CONFORME. Nenhum AJ muda gabarito, ponto de julgamento, mecanismo, formato, moldura S/N ou aderência. Sem GATE pela regra 6.

**Rito:** cumprido como a ficha 9.3, item 6, manda. A auditoria correu sobre a v1, antes do R1 gravado (saida/gcb/QA_DA_reforco_leva3_R1_* ausente em disco na hora da leitura), então os textos da seção 5 são **AJ de v1**, não errata pós-R2 (seção 7.6 não se aplica). São 4 linhas de AJ, em 2 itens.

## 0. Objeto, entradas e método

| objeto | SHA-256 |
|---|---|
| saida/gcb/DA_reforco_leva3_v1.md (objeto; 30 itens; QA PENDENTE) | 7214e588c14f69b1acb72a8d3701efc77ab666824bfa487095c4389923fa91bb |
| saida/gcb/DA_reforco_ficha_2026-10-20.md (amostra: 8.4.8; rito: 5, 7.4, 7.6, 8.3.8, 9.3) | a09139bc3c05a68230f3aea5746490debb4418840d629574622927e1f2bc8493 |
| regras/estilo_banca.md (catálogo vigente em disco: **v1.1.3**; ver registro 2) | 9f9237f5f9828b77d5ab805849a7a14af13fb28fcc1c985fe462ec1027684caf |
| saida/banco/estilo_DA_reforco_leva2.md (modelo de forma e critérios) | ff94acfdc76ef000a13e18624dba6bbd4b2546b4cff2fb503718bf40033a0300 |
| saida/gcb/normativo_cache/Lei_4619_1965_2026-10-20.txt (D3-R24) | b91ef03df94717e00602b1b5195f73176c1c5cf5bebe6d80fba1cbaf37a9082f |
| saida/gcb/normativo_cache/Lei_10406_2002_CodigoCivil_compilada_2026-10-20.txt (D3-R33) | 97e0ffaa7e5b92d072622c9bde5ebdab9121cd32913c4292cb0c5f74a914a828 |
| saida/gcb/normativo_cache/Lei_13869_2019_2026-10-20.txt (D3-R44) | fb3b95c117e64fc0f26f0a915af3ae433d6ceb3aad2434fc5dcae72a64f04a33 |
| saida/gcb/normativo_cache/CF_1988_compilada_2026-10-20.txt (D3-R50) | d6580cb327147e1beb69ccd09cd930613c06f39e1791b235729930a01cacb51d |

**Script:** python3 -I, somente leitura, sobre o arquivo da leva (seções 1 e 2): enunciados, gabaritos, abertura × gabarito, fecho "é correto afirmar que" × gabarito, extensão e contagem de ocorrências dos trechos "antes" e "depois" da seção 5. As contagens de folha fechada e de DA acumulado não foram refeitas: vêm da seção 4 do arquivo da leva e são matéria do R1.

**Conferência por script (leva 3, 30 itens):** "Considere que" 6 C / 6 E; declarativos 10 C / 8 E; fecho "é correto afirmar que" 0 C / 1 E (só o D3-R44). Conferem com a seção 4.6 do arquivo.

**Critérios de estilo:** os mesmos das levas 1 e 2 (estilo da leva 2, seção 0): comando C/E; uma afirmação com um só ponto de erro; troca real e única; nenhuma pista de forma; extensão dentro da faixa da base (estilo_banca v1.1.3, seção 4: C de 8 a 65 palavras; E de 19 a 62); registro formal; termo absoluto só quando for letra da fonte ou a própria troca; moldura que não decide o gabarito (R1 da T-122); risco de "mais de uma interpretação" (estilo_banca, seção 5.3, anulados da ANM); L3-1 a L3-5 (ficha 9.3).
- **NÃO CONFORME:** dois pontos de erro, pista que entrega o gabarito, E decidido pela moldura, ou gabarito que só se sustenta com escolha da produção.
- **AJUSTE (texto):** defeito sanável por substituição exata, sem mudar gabarito, ponto, mecanismo nem a natureza da troca.

## 1. Amostra

Fixada pela ficha, seção 8.4.8, antes da produção. Sem sorteio.

| id | folha | lote | gab. | formato | moldura | aderência | o que cobre |
|---|---|---|---|---|---|---|---|
| D3-R33 | 6.5 | D3 | C | APL | S (órgão/servidor do Poder Legislativo da União) | direta | C com moldura, par R3; absolutos literais (L3-2) |
| D3-R44 | 5.2 | D3 | E [TS] | APL | S (comissão/sessão da Câmara dos Deputados; cota da 5.2) | parcial | E com moldura; absoluto inserido pela troca (L3-2) |
| D3-R50 | 6.2 | D3 | E [TS] | SIT | N | direta | E com "Considere que", sem moldura; CF, art. 5º, LXXV |
| D3-R24 | 6.4 | D3 | E [TS] | NUM | N | parcial | E declarativo, troca de número; Lei 4.619 |

**Composição exigida (ficha, seção 5): CONFERE.** Tem ao menos 1 E com moldura (D3-R44), o único lote da leva (D3), 1 C (D3-R33) e itens parciais (D3-R44, D3-R24).

## 2. Vereditos por item

Palavras: só o enunciado, sem o comando.

| id | gab. | mecanismo | trecho decisivo | palavras | veredito | motivo |
|---|---|---|---|---|---|---|
| D3-R33 | C | C2 (declarado e confirmado) | "o ato será legítimo somente quando as circunstâncias o tornarem absolutamente necessário, não excedendo os limites do indispensável para a remoção do perigo" | 53 | **CONFORME** | Uma afirmação, literal do art. 188, parágrafo único, do CC (conferida na cópia, linha 465). "somente" e "absolutamente" são letra da fonte, e o item é o C com absoluto literal que equilibra o E com "só" inserido do D3-R35 (L3-2). A moldura é decorativa: o cenário só põe o servidor a deteriorar coisa alheia para remover perigo, e o fecho enuncia a regra condicional da norma, sem julgar o caso. A moldura não decide, e o C não depende dela. Usa a fórmula "Nessa situação, nos termos d…" (3 de 12 CQ na leva; limite 5). Registro formal. **Observação 1 (discriminação):** com dois advérbios absolutos literais, o item pune quem marca E por reflexo diante de "somente" (traço de C3, estilo_banca 3.9 e 5.1). É o uso pedido pelo catálogo, não defeito. **Observação 2 (cena):** a cena de remoção de perigo repete-se no D3-R35 (E) e no D3-R29 (C). Os cenários não são literais até o fecho (L3-3 cumprida), e a nota (r) já veda os três no mesmo simulado. **Observação 3 (rótulo):** o bloco declara "fecho: neutro" sem a fórmula "é correto afirmar que" (como no registro 3 do estilo da leva 2). Sem efeito nas contagens. |
| D3-R44 | E [TS] | E6 (rol aberto → exaustivo; declarado e confirmado) | "esse rol, no qual se incluem os membros do Poder Legislativo, é exaustivo" | 47 | **AJUSTE (texto)** | Gabarito, ponto e troca corretos. A Lei 13.869, art. 2º, enumera os sujeitos ativos "compreendendo, mas não se limitando a" (cópia, linha 22). O absoluto "exaustivo" é a própria troca, e a 5.2 tem C com absoluto literal (D3-R45, D3-R47; L3-2 cumprida). A moldura não decide: o E está na letra do caput, e a moldura de sessão de comissão é decorativa ("seja debatido o rol"). **Defeito 1 (referente ambíguo, risco de "mais de uma interpretação", estilo_banca 5.3):** "esse rol" retoma "o rol de sujeitos ativos do crime". O caput define o sujeito ativo por categoria fechada ("qualquer agente público, servidor ou não"), e só a enumeração dos incisos é aberta. Um recurso pode sustentar que o conjunto dos sujeitos ativos é delimitado (só agente público), e o E fica discutível. O AJ-L3-E1 amarra o referente à enumeração dos agentes públicos, que é o que a lei declara não exaustivo. **Defeito 2 (pista de forma nova no D3):** o fecho "é correto afirmar que" é o fecho neutro do D4. No D3 ele só aparece neste item: 0 C / 1 E no lote (seção 4.6 do arquivo; canônicos 0/0). Com n = 1 é indício e não padrão, mas a forma nasce só em E. É a mesma assimetria que levou à regra 7.4.1 no D4 (0 C / 3 E na leva 1). O AJ-L3-E1 tira a fórmula no mesmo texto: o D3 volta a 0/0, e o rótulo "fecho: neutro" do bloco passa a ser coerente com os demais itens do D3. O AJ-L3-E2 harmoniza o campo Troca. O resultado tem 51 palavras, dentro da faixa de E (19 a 62). |
| D3-R50 | E [TS] | E3 (condição inventada; declarado e confirmado) | "a indenização pelo Estado depende da configuração de erro judiciário" | 33 | **AJUSTE (texto)** | Uma troca: a CF, art. 5º, LXXV, põe a prisão além do tempo fixado na sentença como hipótese autônoma ("assim como"; cópia, linha 149), e o item a condiciona ao erro judiciário. A abertura "Considere que" sem moldura em E está dentro da 7.4.2 (leva: CQ 6/6). Não há negação frontal (7.4.5): o cenário traz a hipótese, mas o fecho acrescenta condição que a norma não cria, e não nega a conclusão. **Defeito (risco de "mais de uma interpretação", estilo_banca 5.3):** "configuração de erro judiciário" não diz erro em quê. Quem ler a prisão além do tempo como erro judiciário em sentido amplo (a própria justificativa, linha 2, nomeia essa leitura como a tentação) pode sustentar que, no cenário, o erro "se configura" pela própria prisão excessiva, e então o item seria C. O AJ-L3-E3 amarra a condição inventada à condenação ("depende de que a condenação tenha decorrido de erro judiciário"), que é a primeira hipótese do inciso, distinta da segunda pela letra. O E fica nítido sem depender de doutrina. O mecanismo (E3), o ponto (A6.2-06), o gabarito e a natureza da troca (hipótese autônoma → condicionada ao erro judiciário) ficam iguais. O AJ-L3-E4 harmoniza o campo Troca. O resultado tem 37 palavras. A justificativa, linha 2, continua verdadeira sem mudança. |
| D3-R24 | E [TS] | E3 (prazo trocado; declarado e confirmado) | "o prazo para ajuizamento da ação regressiva será de noventa dias" | 30 | **CONFORME** | Uma troca, de um só número ("sessenta" → "noventa"), sobre texto que de resto é literal do art. 2º da Lei 4.619 (cópia, linha 12). O termo inicial ("a partir da data em que transitar em julgado a condenação imposta à Fazenda") está mantido. Não há absoluto, contraste nem qualificador (L3-2, L3-4 e L3-5 não se aplicam). O item é declarativo, sem moldura, com a norma na abertura. A forma E3 "inventa prazo" tem análogo na base (BQ-0023, "cinco anos"; estilo_banca 3.3). O "cinco anos" vedado pela ficha (8.4.4) não aparece, e não há confusão com o prazo do Decreto 20.910 (D3-R22). Registro formal. **Observação 1 (discriminação, não reprova):** é item de memória pura de número, numa lei de 1965 de pertinência parcial. A tentação declarada ("prazo redondo e plausível") é real, mas o item não discrimina compreensão. Cabe em simulado diagnóstico (nota (v)), não como âncora. **Observação 2 (leitura do catálogo):** a regra 4 do E3 em estilo_banca 5.2 ("Não use números ou prazos ausentes do artigo verificado") é lida aqui como exigência de que o número verdadeiro venha do artigo verificado, o que está cumprido. A troca de número em E necessariamente usa número ausente da fonte. Fica a ressalva de que "noventa dias" não deve coincidir com prazo de outro dispositivo da mesma folha ("noventa" tem 0 ocorrências em D3_v2_1.md, DA_reforco_leva1_v2.md e DA_reforco_leva2_v2.md, por grep, e na leva 3 só aparece no D3-R24 e nos campos dele). |

**Taxas:**
- NÃO CONFORME: 0/4.
- AJUSTE (texto): 2/4 (D3-R44, D3-R50), sem mudança de gabarito.
- Itens decididos pela moldura: 0 (D3-R33 e D3-R44 têm a moldura como cena decorativa; o E do D3-R44 está na letra do caput).

## 3. Conferência de L3-1 a L3-5 (ficha 9.3) nos 4 itens

| regra | D3-R33 (C) | D3-R44 (E) | D3-R50 (E) | D3-R24 (E) |
|---|---|---|---|---|
| L3-1 (abertura por folha fechada) | CQ C na 6.5; 6.5 fechada CQ 5 C / 4 E (seção 4.6 do arquivo) — CONFERE | CQ E na 5.2; 5.2 fechada CQ 5 C / 2 E e declarativos 5 C / 8 E (61,5% de E) — CONFERE (o excesso de C em CQ é legado: D3-15, D3-16 e D3-18) | CQ E na 6.2 (folha aberta; 6.2 com CQ 1 C / 3 E, a leva 4 fecha) — não se aplica ainda; ver rec. L4-2 | DC E na 6.4; 6.4 fechada declarativos 6 C / 5 E (45,5% de E) — CONFERE |
| L3-2 (absoluto inserido pela troca) | C com absoluto literal ("somente", "absolutamente"), equilibra o D3-R35 — CONFERE | E com "exaustivo" inserido; C literal na 5.2: D3-R45, D3-R47 — CONFERE | sem absoluto — não se aplica | sem absoluto — não se aplica |
| L3-3 (cenário gêmeo) | cena de perigo com D3-R35 e D3-R29, sem cenário literal idêntico; nota (r) — CONFERE | cenário único na leva — CONFERE | cenário único; o A6.2-05 da leva 4 fica fora do mesmo simulado (bloco à GCB) — CONFERE | declarativo — não se aplica |
| L3-4 ("mas não" / ", e não") | ausente — CONFERE | ausente no enunciado (o "mas não se limitando a" da fonte não foi transcrito) — CONFERE | ausente — CONFERE | ausente — CONFERE |
| L3-5 (qualificador minimizador) | ausente — CONFERE | ausente — CONFERE | ausente — CONFERE | ausente — CONFERE |

As conferências de folha fechada de L3-1 vêm da seção 4.6 do arquivo da leva e não foram refeitas aqui. As de leva foram refeitas (seção 0).

## 4. Leitura fora da amostra (sem veredito, fora da taxa)

- **Fecho "é correto afirmar que" no D3:** só o D3-R44 usa a fórmula (0 C / 1 E). Com o AJ-L3-E1 aplicado, o D3 fica 0/0. Sem o AJ, a GCB deve registrar o indício na reconciliação (ver rec. L4-1).
- **D3-R35 (E, fora da amostra):** a dúvida (i) do bloco à GCB, sobre se o E pela condição inventada ("só terá direito … se provar a culpa do servidor") é nítido, é matéria do R1. Pelo estilo, o par D3-R33 (C, "somente" literal) × D3-R35 (E, "só" inserido) está equilibrado no marcador.
- **Extensão dos 4 itens:** de 30 a 53 palavras (37 e 51 depois dos AJ), dentro da faixa da base.

## 5. Textos exatos (AJ de v1; seguem com os AJ do R1 para a v2 e são conferidos no R2)

Formato da ficha, seção 4.3. Cada "antes" ocorre exatamente 1 vez em saida/gcb/DA_reforco_leva3_v1.md e cada "depois" 0 vez, conferido por script.

`AJ-L3-E1 | D3-R44 | enunciado (seção 1) | substituir: «Nessa situação, é correto afirmar que, segundo a Lei nº 13.869/2019, esse rol, no qual se incluem os membros do Poder Legislativo, é exaustivo.» | por: «Nessa situação, segundo a Lei nº 13.869/2019, a enumeração dos agentes públicos considerados sujeitos ativos desse crime, na qual se incluem os membros do Poder Legislativo, é exaustiva.»`

`AJ-L3-E2 | D3-R44 | Troca (seção 2) | substituir: «- Troca: compreendendo, mas não se limitando a → rol exaustivo (art. 2º, caput)» | por: «- Troca: compreendendo, mas não se limitando a → enumeração exaustiva (art. 2º, caput)»`

`AJ-L3-E3 | D3-R50 | enunciado (seção 1) | substituir: «a indenização pelo Estado depende da configuração de erro judiciário.» | por: «a indenização pelo Estado depende de que a condenação tenha decorrido de erro judiciário.»`

`AJ-L3-E4 | D3-R50 | Troca (seção 2) | substituir: «→ a indenização pelo Estado depende da configuração de erro judiciário (art. 5º, LXXV)» | por: «→ a indenização pelo Estado depende de que a condenação tenha decorrido de erro judiciário (art. 5º, LXXV)»`

- **Efeito dos quatro:** gabarito (E), ponto (A5.2-18; A6.2-06), mecanismo (E6; E3), formato (APL; SIT), moldura (S, mesmo tipo; N), aderência (parcial; direta), abertura CQ e [TS] inalterados. D3-R44 vai de 47 para 51 palavras; D3-R50, de 33 para 37.
- **Contagens a refazer na v2 (por script, seção 4 do arquivo):** com o AJ-L3-E1, o fecho "é correto afirmar que" do D3 vai de 0 C / 1 E para 0/0 (tabela "Lote D3", seção 4.6), e a dúvida (vi) do bloco à GCB perde o objeto. O classificador de moldura continua a marcar S no D3-R44 ("sessão de comissão da Câmara dos Deputados" permanece). Nenhuma outra contagem muda.
- **O que o R2 confere:** (1) cada "antes" com 1 ocorrência na v1 e cada "depois" aplicado literalmente na v2; (2) nenhum outro campo dos dois blocos muda; (3) os enunciados resultantes, lidos inteiros, mantêm o E pela letra (Lei 13.869, art. 2º, caput: "compreendendo, mas não se limitando a"; CF, art. 5º, LXXV: "assim como o que ficar preso além do tempo fixado na sentença") e não criam pista.
- **Se a gcb-cqfp recusar algum AJ:** o item segue para o R1 como está na v1. Os defeitos são de clareza e de risco de recurso, não de gabarito.

## 6. Recomendações para as próximas levas

Texto exato para a gcb-gerencia incluir na ficha da leva 4 ou nas seguintes, se aceitar. Nenhuma tem efeito sobre os 30 itens da leva 3 além dos AJ da seção 5.

- **L4-1 (fecho "é correto afirmar que" fora do D4):** "Nos lotes D1, D2, D3 e D5, o fecho 'Nessa situação, é correto afirmar que' só entra se a mesma leva tiver ao menos um C com o mesmo fecho no mesmo lote. A seção 4.6 do arquivo da leva informa o conjunto por gabarito em cada lote, e não só no D4."
- **L4-2 (abertura da 6.2 na leva 4):** "A 6.2 chega à leva 4 com 'Considere que' 1 C / 3 E (25,0% de C; seção 4.6 da leva 3). Dos 8 itens da leva 4 na folha (5 C / 3 E pelo plano), os que abrirem com 'Considere que' são preferencialmente C, até a 6.2 fechada ficar com CQ de ao menos 40% de C (regra 7.4.2, L3-1)."
- **L4-3 (referente de rol ou conjunto):** "Item E que troca rol aberto por fechado (E6) nomeia a enumeração que a fonte declara aberta ('os incisos', 'a enumeração', 'a lista de …'), e não um 'rol' que possa ser lido como a categoria-gênero que a própria fonte fecha (D3-R44, AJ-L3-E1)."
- **L4-4 (condição inventada sobre hipótese autônoma):** "Item E que condiciona uma hipótese autônoma a outra (E3) nomeia a outra hipótese pelos elementos que a lei lhe dá ('que a condenação tenha decorrido de erro judiciário'), e não por rótulo que admita sentido amplo ('configuração de erro judiciário') (D3-R50, AJ-L3-E3)."
- **À GBQ (montagem, T-119 e T-123):** o D3-R24 (memória de número, parcial) e os demais parciais ficam só em simulado diagnóstico (nota (v)), como a ficha já prevê. Sem texto novo.

## 7. Registros

1. **Rito:** auditoria sobre a v1, em paralelo ao R1, como a ficha 9.3, item 6, e a 8.4.8 determinam. Os AJ seguem para a v2 com os do R1 e são conferidos no R2. Nenhuma errata pós-R2 (seção 7.6) é proposta.
2. **Versão do catálogo:** o despacho cita "regras/estilo_banca.md (catálogo v1.0 vigente)". O arquivo em disco é a **v1.1.3** (linha 2; SHA-256 na seção 0), que é a versão usada nesta auditoria e na da leva 2. Os mecanismos citados (C2, C3, E3, E6) e as seções 3.3, 3.9, 5.1, 5.2 e 5.3 são os da v1.1.3. A divergência de rótulo fica registrada para a GBQ; nada foi alterado no catálogo.
3. **Nome do arquivo:** o da ficha 8.4.8 e 7.5 (saida/banco/estilo_DA_reforco_leva3.md).
4. **Fidelidade às bases:** só se leram as linhas das cópias em saida/gcb/normativo_cache/ correspondentes aos 4 itens (Lei 4.619, art. 2º; CC, art. 188, parágrafo único; Lei 13.869, art. 2º; CF, art. 5º, LXXV), para confirmar o trecho decisivo. A conferência das bases é matéria da gcb-cqfp e do qa-normativo-da.
5. **Escopo:** nada vai à plataforma nem à candidata. Nenhuma tarefa nova (D-COMPLEMENTOS). Nenhum gatilho em PARA_PRESIDENCIA.md. Nenhum NÃO CONFORME, e por isso nenhum GATE pela regra 6.

AVISO: os vereditos, a atribuição de mecanismo, a leitura de pista e o juízo de risco de "mais de uma interpretação" são julgamento deste agente (gbq-estilo) e exigem revisão da GBQ. As contagens de abertura, de fecho, de extensão e de ocorrência dos trechos de AJ vêm de script sobre o arquivo gravado (python3 -I, somente leitura), com revisão manual dos 4 itens. As contagens de folha fechada e de lote foram tomadas da seção 4 do arquivo da leva, sem refazer. Com n pequeno (amostra de 4; recortes de 1 a 30 itens), nenhuma associação é regra. A tabela serve para corrigir vieses de redação, nunca para prever gabarito.

FIM DA AUDITORIA DE ESTILO — LEVA 03 — REFORÇO DA
