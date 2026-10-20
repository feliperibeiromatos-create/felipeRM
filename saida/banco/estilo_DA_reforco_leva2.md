# estilo_DA_reforco_leva2.md — T-116 (D-REFORCO-DA, leva 2, auditoria de estilo 10%) — 2026-10-20 — gerado por gbq-estilo

Auditoria de estilo Cebraspe da leva 2 do reforço de DA (ficha, seções 5, 7.6 e 8.3.8; D-REFORCO-DA: "gbq-estilo audita 10% por leva"). Ciclo s15c4. Destino: gcb-gerencia (reconciliação da leva 2) e gcb-cqfp (conferência das erratas). Este agente audita e não produz. Nenhum arquivo de produção foi alterado. Sem commit nem push.

**Resultado:** 3 itens auditados (10,0% de 30), todos aprovados no R2. Vereditos: 2 CONFORMES (D4-R20 e D1-R04), 1 AJUSTE (texto) (D3-R18), 0 NÃO CONFORME. Sem GATE.

**Rito (D-T116-LEVA1-ACEITE; ficha 7.6 e 8.3.8):** a ficha previa a auditoria sobre a v1, em paralelo ao R1. Ela não aconteceu: o R2, seção 6, item 3, registra o arquivo como ausente. Por isso a auditoria correu sobre a v2 aprovada, e todo texto exato abaixo vale como **"errata para conferência"** da gcb-cqfp, ou então como **"recomendação para as próximas levas"**, sem efeito sobre os 30 itens. São 2 erratas para conferência e 6 recomendações.

**Pista "moldura / 'Considere que'" (por script, seção 4):**
- **Leva 2 isolada:** sem sinal (CQ phi +0,05; moldura phi +0,15; ambos não significativos). A leva corrigiu a inversão da leva 1.
- **DA acumulado (470 itens):** resta um viés para **C**, herdado dos canônicos. Moldura: 48 C / 21 E (69,6%; phi −0,16; p < 0,001). CQ: 60,4% C (p = 0,004). O viés de CQ desaparece sem a moldura (phi −0,05; p = 0,35) e diminui a cada leva.
- **Recorte só do reforço do D3:** moldura → E (2 C / 6 E; Fisher p = 0,018; regra ingênua 81%). O risco fica contido pela nota (w), segundo a qual o reforço não forma simulado isolado.

## 0. Objeto, entradas e método

| objeto | SHA-256 |
|---|---|
| saida/gcb/DA_reforco_leva2_v2.md (objeto; 30 itens; APROVADO no R2) | 5baec20d81eea47f50e79275375668284d58ff5649f85a06c37552cd0f161bbe |
| saida/gcb/QA_DA_reforco_leva2_R2_2026-10-20_gcb-cqfp.md | cfce8e25aec338c898e662bd59e826a7e755de70e822e4573f0ec9c0f500549b |
| saida/gcb/QA_DA_reforco_leva2_R1_2026-10-20_gcb-cqfp.md | eae940796317397ccdfba05187eef039c31f483fdb478be0b329188d3fafea36 |
| saida/gcb/DA_reforco_ficha_2026-10-20.md (amostra: seção 8.3.8) | 77f2e60af942b004fde8443030ff42c251e45057451f8d03845628f4df6e5639 |
| saida/gcb/DA_reforco_leva1_v2.md (30 itens aceitos; D-T116-LEVA1-ACEITE) | 2c431529a5440d4a2bf2bb617bc75d496949dff28a824e0215322d00d79a4f04 |
| saida/pacote/pacote.json v1.13 (410 canônicos de DA, D1 a D6: enunciado e gabarito) | 82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240 |
| saida/banco/moldura_ce_itens_2026-10-20.csv (moldura oficial dos canônicos) | ed4b364dffbca7d9e8878591914783258fa7048c4f1837d98c3d62e34981daac |
| regras/estilo_banca.md v1.1.3 (tipologia, marcadores; extensão da base: C média 31,6, de 8 a 65; E média 34,7, de 19 a 62) | 9f9237f5f9828b77d5ab805849a7a14af13fb28fcc1c985fe462ec1027684caf |
| saida/banco/estilo_DA_reforco_leva1.md (critérios e partida) | 2d50c4cb210943105fabaeb35459a3137ed78b2393b6b15981cbbe8894728878 |
| DECISOES.md (D-T116-LEVA1-ACEITE, D-MOLDURA-CE, D-REFORCO-DA) | b4683df5ec6925c9bd88fa3f7c772fa7454dd324cb25586c97d27da737471641 |

**Script:** python3 -I, somente leitura, no scratchpad da sessão (estilo_l2/corr.py, SHA-256 351ba1c10cd40dbaaed8a5943fe1cb250719d61f10be01ad3b7f5c0c0baf4d91).

**Fontes de dados:**
- Canônicos: enunciado e gabarito vêm do pacote.json e a moldura vem do CSV. O gabarito do pacote foi conferido com o do CSV: 410 de 410 iguais. Nenhum item de DA tem textoBase.
- Levas 1 e 2: o enunciado vem da seção 1 de cada arquivo. Gabarito, moldura (S/N) e [TS] vêm do bloco comentado.

**Definições:**
- Abertura: CQ = o enunciado começa por "Considere que".
- Fecho de acerto: "a afirmação do expositor é correta" ou "estará correto ao".
- Fecho neutro: "Nessa situação, é correto afirmar que".
- Fórmula: "Nessa situação, nos termos d…".
- Associação: phi (sinal + = o traço puxa para E) e teste exato de Fisher bicaudal.
- Regra ingênua: "traço → E; sem o traço → C".

**Conferência das contagens:** as do arquivo da leva e as do R2 se reproduzem (DA 48/21; D3 8/7; K1 14/6; K4 25/18; fecho neutro 2/3; ", e não" 1/2; CQ da leva 7/6 e DC 10/7).

**Critérios de estilo:** os mesmos da auditoria da leva 1, seção 0: comando C/E; uma afirmação com um só ponto de erro; troca real e única; nenhuma pista de forma; extensão dentro da faixa da base; registro formal; termo absoluto só quando for a letra da fonte ou a própria troca; moldura que não decide o gabarito (R1 da T-122).
- **NÃO CONFORME:** dois pontos de erro, pista que entrega o gabarito ou E decidido pela moldura.
- **AJUSTE (texto):** defeito sanável por substituição exata, sem mudar gabarito, ponto, Troca nem mecanismo.

## 1. Amostra

A ficha, seção 8.3.8, fixou a amostra antes da produção. Não houve sorteio e a semente 20261020 não foi usada.

| id | folha | lote | gab. | formato | moldura | aderência | o que cobre |
|---|---|---|---|---|---|---|---|
| D4-R20 | 8.4 | D4 | C | APL | S (expositor; fecho neutro) | direta | C com moldura; pistas K1, K4 e fecho neutro |
| D1-R04 | 2.2 | D1 | E [TS] | SIT | N | direta | E com CQ sem moldura; Decreto 9.830; texto do AJ-2 (R1) |
| D3-R18 | 6.4 | D3 | E [TS] | APL | S (servidor de órgão do Poder Legislativo da União) | parcial | E com moldura; parcial; Lei 8.112 |

**Composição exigida (ficha, seção 5): CONFERE.** Inclui ao menos 1 E com moldura (D3-R18), os três lotes da leva, 1 C (D4-R20) e 1 parcial (D3-R18).

## 2. Vereditos por item

Palavras: só o enunciado, sem o comando.

| id | gab. | mecanismo | marcadores | palavras | veredito | motivo |
|---|---|---|---|---|---|---|
| D4-R20 | C | C2 (declarado). A rigor, C6: a alínea f continua com "e lidar com as limitações de recursos…" e o item a corta, sem marcador de exclusividade. | "Considere que, em audiência pública de comissão da Câmara dos Deputados, um expositor trate…"; "Nessa situação, é correto afirmar que" | 49 | **CONFORME** | Afirmação única, literal da alínea f de R60, atribuída ao TCU. Registro formal; não há termo absoluto. A moldura é decorativa: o expositor só "trate das diretrizes" e não afirma nada. O juízo é do examinador, pelo fecho neutro, e por isso a moldura não decide o gabarito. Cumpre a L2-1/7.4.1 (fecho neutro em C) e é o par R3 do D4-R16. **Observação de discriminação (não reprova):** a diretriz tem redação "virtuosa" (inovação, valor público) e a candidata tende a marcar C por plausibilidade. A tentação declarada na justificativa ("duvidar de que a inovação conste") é fraca. É um C2 de memória típico. **Indício (n = 4, não é padrão):** na 8.4, os itens que citam o Referencial do TCU somam 1 C / 3 E (D4-R15 E, D4-R16 E, D4-R20 C, D4-R24 E). As notas (h) e (u) já separam os pares mais próximos. |
| D1-R04 | E [TS] | E2 (polaridade do art. 12, § 3º) | "Considere que determinado agente público, ao emitir opinião técnica, tenha dado causa a dano"; "Nessa situação, segundo o Decreto nº 9.830/2019"; "o mero nexo … implica" | 40 | **CONFORME** | Uma troca, literal ("não implica" → "implica"). O cenário estabelece o nexo ("tenha dado causa"), não enumera a exceção (dolo ou erro grosseiro), não monta negação frontal (7.4.5) e não tem moldura (P3). **Observação 1 (marcador):** "mero" é letra da norma e qualifica o nexo como insuficiente; afirmar que o "mero" nexo "implica" a responsabilização inclina levemente para E. Tirar o "mero" deixaria o item discutível ("o nexo implica" pode ser lido como pressuposto e não como causa suficiente), então o "mero" fica. Na folha, o qualificador está equilibrado: "por si só" no D1-R09 (C) e "mero" no D1-R04 (E). No DA acumulado, "mero / por si só / simples" somam 5 C / 3 E. Não há pista agregada. **Observação 2 (pista cruzada):** depois do AJ-2 e do AJ-5, o D1-R04 (E) e o D1-R09 (C) têm o mesmo cenário literal até "tenha dado causa a dano" e o mesmo fecho "Nessa situação, segundo o Decreto nº 9.830/2019". No mesmo simulado, o C do D1-R09 ("o montante do dano, por si só, não pode ser elemento para caracterizar…") ensina que o Decreto exige algo além do dano e do nexo, e isso ajuda a resolver o D1-R04 sem conhecer o § 3º. Hoje só existe a nota (s2), D1-R13 × D1-R04. Correção: nota de simulado (AJ-L2-E2). |
| D3-R18 | E [TS] | E3 (até o limite da herança → sem limite) | "Considere que servidor público civil da União lotado em órgão do Poder Legislativo da União"; "sem limite de valor"; "conforme a Lei nº 8.112/1990" | 47 | **AJUSTE (texto)** | Gabarito, ponto e troca corretos. O absoluto "sem limite de valor" é a própria troca (estilo_banca, seção 5.1). Na leva, os absolutos estão equilibrados (C: D3-R14 "todos", D3-R15 "exclusivamente", D3-R17 "independentemente", todos letra da norma; E: D4-R25 "exclusivamente", D3-R18 "sem limite"). A moldura não decide: o E está na letra do § 3º. A norma vem no fim do enunciado, cumprindo a 7.4.3. **Defeito de clareza:** "tenha causado dano ao erário e falecido" elide o auxiliar e encosta "falecido" em "erário"; a leitura de passagem ("dano ao erário e [ao] falecido") é possível. A ordem dos fatos (dano, depois morte) sustenta o juízo sobre os sucessores, e a fórmula da banca para cenário sequencial é explícita. Correção: AJ-L2-E1, que só acrescenta "posteriormente" e o auxiliar, com mesmo gabarito, ponto, Troca, mecanismo e moldura (49 palavras). **Observação de discriminação (não reprova):** a troca por absoluto explícito é a forma mais reconhecível de E; ver a rec. L3-2. |

**Taxas:**
- NÃO CONFORME: 0/3.
- AJUSTE (texto): 1/3 (D3-R18), sem mudança de gabarito.
- Itens decididos pela moldura: 0. Os E com moldura da leva (D3-R16, D3-R18, D3-R19) têm troca literal declarada no campo Troca.

## 3. Leitura fora da amostra (sem veredito, fora da taxa)

- **D3-R16 (E):** "… mas não por dano à imagem". O contraste "mas não" soma 0 C / 2 E no DA acumulado (D3-R16 e 1 canônico). É indício (n = 2), não padrão. A troca é a exclusão do rol, então não é negação frontal de cenário (7.4.5). Ver a rec. L3-4.
- **D3-R15 (C) e D1-R13 (E):** a mesma construção "configura-se … ainda que …", em folhas distintas, com 1 C / 1 E. Não há pista. Fica o registro pedido pelo R2, seção 3.
- **Extensão na leva:** C média 39,8 (de 23 a 59); E média 40,3 (de 30 a 56). A diferença era de +8,3 para E na leva 1 e caiu para +0,5. Nenhum item sai da faixa da base.
- **Marcadores na leva 2 (C/E):**

| marcador | C | E |
|---|---|---|
| "não" | 4 | 4 |
| "ainda que" | 1 | 1 |
| "exclusiv-" | 1 | 1 |
| ", e não" | 1 | 0 |
| "pode" | 1 | 0 |
| "todos" | 1 | 0 |
| "independentemente" | 1 | 0 |
| "sem limite" | 0 | 1 |
| "mero" | 0 | 1 |
| "afasta" | 0 | 1 |
| "implica" | 0 | 1 |

  Não aparecem "somente", "apenas", "sempre", "nunca" nem "qualquer". Nenhum desequilíbrio configura pista.

## 4. Correlação abertura / moldura × gabarito (por script; C/E)

### 4.1 Escopos

| escopo | n | C/E | CQ C/E (%C) | sem CQ C/E (%C) | phi CQ→E | p | moldura S C/E (%C) | moldura N C/E (%C) | phi mold.→E | p | regra ingênua CQ→E / mold.→E | classe majoritária |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DA canônicos (D1 a D6) | 410 | 202/208 | 69/35 (66,3%) | 133/173 (43,5%) | −0,20 | <0,001 | 44/9 (83,0%) | 158/199 (44,3%) | −0,26 | <0,001 | 41,0% / 40,7% | 50,7% |
| DA leva 1 | 30 | 15/15 | 5/12 (29,4%) | 10/3 (76,9%) | +0,47 | 0,025 | 2/9 (18,2%) | 13/6 (68,4%) | +0,48 | 0,021 | 73,3% / 73,3% | 50,0% |
| **DA leva 2** | 30 | 17/13 | **7/6 (53,8%)** | **10/7 (58,8%)** | **+0,05** | **1,000** | **2/3 (40,0%)** | 15/10 (60,0%) | **+0,15** | **0,628** | **53,3% / 60,0%** | 56,7% |
| DA levas 1 + 2 (só reforço) | 60 | 32/28 | 12/18 (40,0%) | 20/10 (66,7%) | +0,27 | 0,069 | 4/12 (25,0%) | 28/16 (63,6%) | +0,34 | 0,010 | 63,3% / 66,7% | 53,3% |
| **DA acumulado** | 470 | 234/236 | **81/53 (60,4%)** | 153/183 (45,5%) | **−0,13** | **0,004** | **48/21 (69,6%)** | 186/215 (46,4%) | **−0,16** | **<0,001** | 43,8% / 44,0% | 50,2% |
| DA acumulado, só moldura N | 401 | 186/215 | 35/32 (52,2%) | 151/183 (45,2%) | −0,05 | 0,348 | — | — | — | — | — | — |
| D1 acumulado | 72 | 36/36 | 3/2 | 33/34 | −0,05 | 1,000 | 1/0 | 35/36 | −0,12 | 1,000 | 48,6% / 48,6% | 50,0% |
| D3 leva 2 | 8 | 5/3 | 2/3 | 3/0 | +0,60 | 0,196 | 1/3 | 4/0 | +0,77 | 0,143 | 75,0% / 87,5% | 62,5% |
| D3 levas 1 + 2 | 21 | 13/8 | 5/6 (45,5%) | 8/2 (80,0%) | +0,36 | 0,183 | **2/6 (25,0%)** | **11/2 (84,6%)** | **+0,60** | **0,018** | 66,7% / **81,0%** | 61,9% |
| D3 acumulado | 92 | 44/48 | 20/16 (55,6%) | 24/32 (42,9%) | −0,12 | 0,287 | 8/7 (53,3%) | 36/41 (46,8%) | −0,05 | 0,779 | 43,5% / 46,7% | 52,2% |
| D4 leva 2 | 10 | 6/4 | 2/1 | 4/3 | −0,09 | 1,000 | 1/0 | 5/4 | −0,27 | 1,000 | 50,0% / 50,0% | 60,0% |
| D4 acumulado | 106 | 54/52 | 25/18 (58,1%) | 29/34 (46,0%) | −0,12 | 0,241 | 14/6 (70,0%) | 40/46 (46,5%) | −0,18 | 0,082 | 44,3% / 43,4% | 50,9% |
| D2 (sem reforço ainda) | 80 | 40/40 | 18/8 (69,2%) | 22/32 (40,7%) | −0,27 | 0,031 | 9/1 (90,0%) | 31/39 (44,3%) | −0,30 | 0,014 | 37,5% / 40,0% | 50,0% |
| D5 (sem reforço ainda) | 70 | 35/35 | 15/9 (62,5%) | 20/26 (43,5%) | −0,18 | 0,208 | 15/7 (68,2%) | 20/28 (41,7%) | −0,25 | 0,070 | 41,4% / 38,6% | 50,0% |
| Folha 8.4 (fechada, 20) | 20 | 10/10 | 4/5 (44,4%) | 6/5 (54,5%) | +0,10 | 1,000 | 2/3 | 8/7 | +0,12 | 1,000 | 55,0% / 55,0% | 50,0% |
| Folha 2.2 (fechada, 20) | 20 | 10/10 | 3/2 | 7/8 | −0,12 | 1,000 | 0/0 | 10/10 | 0,00 | 1,000 | 45,0% / 50,0% | 50,0% |
| Folha 6.4 (16 de 20) | 16 | 8/8 | 3/5 (37,5%) | 5/3 (62,5%) | +0,25 | 0,619 | 2/3 | 6/5 | +0,13 | 1,000 | 62,5% / 56,2% | 50,0% |

D6 (50 canônicos) não tem CQ e tem 1 item com moldura (C).

### 4.2 Fechos e fórmula (C/E)

| conjunto | fecho neutro | fecho de acerto | "Nessa situação, nos termos d…" | ", e não" | "Considere que servidor/órgão do Poder Legislativo da União" (D3) |
|---|---|---|---|---|---|
| D4 canônicos | 0/0 | 5/0 | 3/0 | 0/0 | — |
| D4 leva 1 | 0/3 | 2/6 | 0/0 | 0/2 | — |
| D4 leva 2 | 2/0 | 0/1 | 0/0 | 1/0 | — |
| **D4 acumulado** | **2/3 (40%)** | 7/7 | 3/0 | 1/2 | — |
| D3 acumulado | 0/0 | 0/0 | 4/4 | 3/1 | canônicos 5/0; leva 1 1/3; leva 2 1/3 → **7/6** |
| D1 acumulado | 0/0 | 0/0 | 1/1 | 0/1 | — |

### 4.3 Leitura

1. **Leva 2: sem pista.** As regras da ficha 7.4 funcionaram:
   - L2-1/7.4.1: o fecho neutro do D4 passou de 0/3 para 2/3, no piso de 40%.
   - L2-2/7.4.2: CQ com 53,8% de C e declarativos com 41,2% de E.
   - L2-3/7.4.3: a fórmula aparece em 2 de 5 itens na 6.4.
   - L2-4/7.4.4: o contraste ganhou 1 C.
   - Resultado: a regra ingênua "CQ → E" acerta 53,3%, abaixo da classe majoritária (56,7%). Na leva 1 acertava 73,3%.
2. **DA acumulado: viés residual para C, herdado e em queda.** Moldura → C: phi de −0,26 nos canônicos para −0,16 no acumulado; 69,6% de C contra a meta de 40% a 60% da D-MOLDURA-CE, prevista para a leva 5. O viés de CQ → C só existe porque a moldura se concentra em CQ: sem moldura, phi −0,05 (p = 0,35). A regra inversa "CQ → C" acerta 56,2% contra a majoritária de 50,2%, a mesma pista da T-122 em escala menor. Os maiores focos estão em folhas ainda sem reforço: D2 (moldura 9 C / 1 E; p = 0,014) e D5 (15/7). Não é defeito da leva 2.
3. **Reforço do D3 isolado: moldura → E (2 C / 6 E; p = 0,018; regra ingênua 81%).** O sinal vem da cota de E com moldura, por desenho (ficha 2.2). Nas levas 1 e 2 juntas, os 10 itens declarativos do D3 dão 8 C / 2 E. A leva 3, pelo plano (8.4.6), acrescenta 1 C / 4 E com moldura, e o reforço do D3 vai a cerca de 3/10 com moldura. No D3 acumulado não há pista (8/7; phi −0,05; depois da leva 3, 9/11 pelo plano). O risco existe só em simulado montado com o reforço isolado, que a nota (w) da ficha 8.5 já veda. A cena "Considere que servidor/órgão do Poder Legislativo da União" está em 7/6 no D3 acumulado (canônicos 5/0, reforço 2/6).
4. **Folha 6.4:** com 16 de 20 itens, CQ está em 3 C / 5 E (37,5% de C; não significativo). A leva 3 acrescenta 4 itens declarativos (2 C / 2 E). A folha fecharia com CQ em 37,5% de C, abaixo do piso de 40% que a 7.4.2 fixa só por leva. Ver a rec. L3-1.

## 5. Textos exatos

Cada trecho "antes" ocorre 1 vez no arquivo da leva, conferido por grep. Classificação conforme a D-T116-LEVA1-ACEITE: texto do estilo sobre item já aprovado no R2 só entra em aceite com conferência da gcb-cqfp.

**AJ-L2-E1 — ERRATA PARA CONFERÊNCIA (gcb-cqfp)**

`AJ-L2-E1 | D3-R18 | enunciado (seção 1) | substituir: «tenha causado dano ao erário e falecido.» | por: «tenha causado dano ao erário e, posteriormente, tenha falecido.»`

- Efeito: só clareza e ordem dos fatos. Gabarito E, ponto A6.4-13, Troca, mecanismo E3, formato APL, moldura S (mesmo tipo), aderência parcial e abertura CQ ficam inalterados. O enunciado vai de 47 para 49 palavras.
- O que a gcb-cqfp confere: (1) "antes" com 1 ocorrência na seção 1 e "depois" com 0; (2) nenhum outro campo muda; (3) o enunciado resultante, lido inteiro, não muda o sentido nem cria pista.
- Se não for aceita até a geração da v1.14, o D3-R18 entra como aprovado no R2 (o defeito é só de clareza).

**AJ-L2-E2 — ERRATA PARA CONFERÊNCIA (nota de simulado, no bloco à GCB; não altera texto de item)**

`AJ-L2-E2 | bloco à GCB (seção 5), notas "não pôr no mesmo simulado" | substituir: «(s2) NOVA: D1-R13 e D1-R04 (Decreto 9.830, art. 12, §§ 2º e 3º: prova do dolo ou do erro grosseiro).» | por: «(s2) NOVA: D1-R13 e D1-R04 (Decreto 9.830, art. 12, §§ 2º e 3º: prova do dolo ou do erro grosseiro); (s3) D1-R04 e D1-R09 (mesmo cenário literal "determinado agente público, ao emitir opinião técnica, tenha dado causa a dano" e mesmo fecho "Nessa situação, segundo o Decreto nº 9.830/2019"; o C do D1-R09, § 5º, sinaliza o erro do D1-R04, § 3º; gbq-estilo, auditoria da leva 2).»`

- Na ficha 8.5, a GCB acrescenta a linha (s3) na mesma forma, com destino à T-119 e à T-123.

## 6. Recomendações para as próximas levas

Texto exato para a gcb-gerencia incluir na ficha da leva 3 ou nas seguintes. Nenhuma tem efeito sobre os 30 itens da leva 2.

- **L3-1 (abertura por folha fechada):** "A regra 7.4.2 (CQ com ao menos 40% de C; declarativos com ao menos 40% de E) também é conferida na folha fechada (canônicos + reforço). Na 6.4, que fecharia com CQ 3 C / 5 E, um dos 2 C da leva 3 (D3-R22 ou D3-R25) passa a abrir com 'Considere que', sem moldura. A 6.4 fica com CQ 4 C / 5 E (44,4%); a leva 3 com CQ 6/6 e declarativos 10/8. Se o formato passar de SUJ ou NUM a SIT, o teto é respeitado (SIT 4 em 20). O teste de sequência não muda, porque gabarito e [TS] ficam iguais."
- **L3-2 (absoluto inserido pela troca):** "Em item E cuja troca insere absoluto que não está na fonte ('sem limite', 'exclusivamente', 'qualquer'), a leva traz ao menos um C com absoluto literal da fonte na mesma folha ou no mesmo lote. A seção 4 do arquivo da leva informa a contagem de absolutos por gabarito. Prefira, quando a fonte permitir, a troca por conceito vizinho (E1) à troca por absoluto (leva 2: D3-R18 e D4-R25, equilibrados por D3-R14, D3-R15 e D3-R17)."
- **L3-3 (cenário gêmeo):** "Dois itens da mesma folha com cenário literal idêntico até o fecho só entram com a nota 'não pôr no mesmo simulado' declarada pela gcb-cpp no próprio arquivo da leva (leva 2: D1-R04 × D1-R09, sem nota; D3-R18 × D3-R20, com a nota (m))."
- **L3-4 (contraste 'mas não'):** "Contraste 'mas não' / ', e não' em E só se a leva ou o lote tiver C com o mesmo contraste literal ('mas não': DA acumulado 0 C / 2 E; ', e não': 6 C / 5 E, equilibrado)."
- **L3-5 (qualificador minimizador):** "Em item E de inversão de polaridade de dispositivo com 'mero', 'por si só' ou 'simples', a folha traz um C com qualificador equivalente (na 2.2: D1-R09 C equilibra D1-R04 E). Na dúvida, o qualificador fica, se tirá-lo tornar o gabarito discutível."
- **À GBQ (montagem, T-119 e T-123):** valem as notas (k) a (x) da ficha 8.5, com a (s3). A nota (w) ("as levas não formam simulado isolado") passa a ter lastro numérico: no reforço do D3, moldura → E tem 81% de acerto ingênuo (p = 0,018). No DA acumulado o sinal é o oposto (moldura → C, 69,6%), e o teto de 50% de C com moldura por simulado (D-MOLDURA-CE (c)) segue indispensável até a leva 5. Nas levas que abrirem as folhas do D2 (moldura 9 C / 1 E) e do D5 (15/7), a cota de E com moldura da ficha 2.2 é o que reduz o viés; não há texto novo a propor.

## 7. Registros

1. **Rito:** a ficha 8.3.8 previa a auditoria sobre a v1, em paralelo ao R1. Isso não aconteceu: o arquivo estava ausente no R1 e no R2 (R2, seção 6, item 3; v2, pendência 6.4, item 6). A auditoria correu sobre a v2 aprovada, e os dois textos da seção 5 são errata para conferência (ficha 7.6, lida conforme a D-T116-LEVA1-ACEITE). Nenhum dos dois muda Troca, gabarito ou construção. Para a leva 3, a ficha 8.4.8 mantém o mesmo rito; recomenda-se cumprir a auditoria sobre a v1, para evitar errata pós-R2.
2. **Nome do arquivo:** o da ordem e da ficha 7.5 (saida/banco/estilo_DA_reforco_leva2.md).
3. **Rótulo de fecho nos blocos do D3:** os blocos do D3-R16, R18, R19 e R20 declaram "fecho: neutro", mas o enunciado não usa a fórmula "Nessa situação, é correto afirmar que" (o fecho neutro é conjunto do D4). Sem efeito nas contagens, que vêm do enunciado. A GCB pode harmonizar o rótulo na consolidação.
4. **Fidelidade às bases:** lida nos trechos literais dos blocos e no R2. Nenhuma página foi reaberta: isso é matéria da gcb-cqfp e do qa-normativo-da.
5. **Escopo:** nada vai à plataforma nem à candidata. Nenhuma tarefa nova (D-COMPLEMENTOS). Nenhum gatilho em PARA_PRESIDENCIA.md.

AVISO: os vereditos, a atribuição de mecanismo e a leitura de pista são julgamento deste agente (gbq-estilo) e exigem revisão da GBQ. As contagens de C/E, aberturas, fechos, moldura, marcadores e extensão vêm de script sobre os arquivos gravados (python3 -I, somente leitura), com revisão manual dos itens citados. Com n pequeno (leva de 30; recortes de 8 a 21 itens), nenhuma associação é regra. A tabela serve para corrigir vieses de redação, nunca para prever gabarito.

FIM DA AUDITORIA DE ESTILO — LEVA 02 — REFORÇO DA
