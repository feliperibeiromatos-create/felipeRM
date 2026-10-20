# estilo_DA_reforco_leva1.md — T-116 (D-REFORCO-DA, leva 1, auditoria de estilo 10%) — 2026-10-20 — gerado por gbq-estilo

Auditoria de estilo Cebraspe da leva 1 do reforço de DA (ficha, seção 1, regra 15; D-REFORCO-DA: "gbq-estilo audita 10% por leva"). Ciclo s15c3. Destino: gcb-gerencia (reconciliação T116_L01). Este agente audita e não produz: nenhum arquivo de produção foi alterado; os textos abaixo são propostas de AJ no formato da ficha, seção 4.3. Sem commit nem push.

**Resultado:** 4 itens auditados (13,3% de 30), todos aprovados no R2: 3 CONFORMES (D4-R03, D3-R03, D4-R16) e 1 AJUSTE (texto) (D3-R13). NÃO CONFORME: 0. Sem GATE. Achados de leva: 2 AJ de texto exato (AJ-E1 e AJ-E2), 1 observação fora da amostra e 4 recomendações para a ficha da leva 2. **Risco de pista "moldura / 'Considere que' → E":** baixo no banco acumulado do D4 e do D3 e em cada folha; **moderado e localizado** dentro da leva 1, se ela for usada isolada, e no fecho neutro do D4, que hoje só aparece em E (0 C / 3 E). Detalhes na seção 4.

## 0. Objeto, entradas e método

| objeto | SHA-256 |
|---|---|
| saida/gcb/DA_reforco_leva1_v2.md (objeto; 30 itens; aprovado com ressalvas no R2) | 2c431529a5440d4a2bf2bb617bc75d496949dff28a824e0215322d00d79a4f04 |
| saida/gcb/QA_DA_reforco_leva1_R2_2026-10-20_gcb-cqfp.md | 7f77a3151b964aa3de01db1bdef26acf1f00137400f9ee4db5a99aaf93b0a509 |
| saida/gcb/DA_reforco_ficha_2026-10-20.md (amostra: seção 5) | acf8b57af3f42e0bcab9a6d92f6cfa3dd70deacf3f521fc285e5b3a1b0d95133 |
| saida/gcb/D4_v2_1.md (79 canônicos do D4) | c1a7a93598e9fd37b2009b9feaca3afd3898fa05f6f66e6de26dd40c2839e5d9 |
| saida/gcb/D3_v2_1.md (71 canônicos do D3) | 0f7a8b090fe6f2243ae55b36273dacdb719aaf04b19548dce70aad4867798930 |
| saida/banco/moldura_ce_itens_2026-10-20.csv (moldura oficial dos canônicos) | ed4b364dffbca7d9e8878591914783258fa7048c4f1837d98c3d62e34981daac |
| regras/estilo_banca.md v1.1.3 (tipologia E1–E6, C1–C6; marcadores; extensão da base: C média 31,6, de 8 a 65; E média 34,7, de 19 a 62) | 9f9237f5f9828b77d5ab805849a7a14af13fb28fcc1c985fe462ec1027684caf |

Método: script próprio (python3 -I, somente leitura, scratchpad da sessão; SHA-256 do script 691a4c74e934947729b9bbe92039b45770b6365e1a21c0a61d8b516d178ef2eb). O script extrai o enunciado da versão do estudante e o gabarito do bloco comentado de cada item; nos canônicos, confere o gabarito com o CSV de moldura (150 de 150 iguais) e usa a moldura do CSV; na leva, usa o campo "Moldura: S/N" do bloco. Abertura = início literal do enunciado; fecho = "a afirmação do expositor é correta" (acerto, expositor), "ele estará correto ao" (acerto, analista), "Nessa situação, é correto afirmar que" (neutro) ou outro. Associação medida por phi (sinal + = a abertura puxa para E) e teste exato de Fisher bicaudal. As contagens reproduzem as da produção e do R2: K1 13/6, K4 23/17, D3 com moldura 7/4.

Critérios de estilo (os das ondas 1 a 4 e F1): comando C/E ("Julgue cada item como Certo ou Errado", presente na seção 1); enunciado assertivo, uma afirmação e um só ponto de erro; troca real e única, com mecanismo da tipologia; nenhuma pista de forma que entregue o gabarito; extensão dentro da faixa da base; registro formal e impessoal; termo absoluto só quando for a letra da fonte ou o próprio ponto da troca; cenário que pese no juízo ou, se for só moldura de cota, que não decida o gabarito (R1 da T-122). NÃO CONFORME: dois pontos de erro, pista que entrega o gabarito ou E decidido pela moldura. AJUSTE (texto): defeito sanável por substituição exata, sem mudar o gabarito nem o ponto.

## 1. Amostra

A ficha fixa a amostra (seção 5, "Leva 1 (4 itens, 13%)"), designada por ponto antes da produção; não houve sorteio e a semente 20261020 não foi usada. Ids finais da v2 pela correspondência ponto → id da seção 4.5 do arquivo da leva (confirmada no bloco à GCB, linha "Amostra da gbq-estilo"):

| ficha (ponto) | id na v2 | folha | lote | gab. | formato | moldura | aderência | o que a amostra cobre |
|---|---|---|---|---|---|---|---|---|
| 8.1 item 13 (A8.1-27, alínea i) | D4-R03 | 8.1 | D4 | E [TS] | SIT | N (analista; fecho de acerto) | direta | "Considere que", "pós-NPM", K2, K3, K4 |
| 6.3 item 4 (A6.3-07) | D3-R03 | 6.3 | D3 | C | APL | S (órgão do Poder Legislativo da União) | direta | C com moldura (par da R3) |
| 6.3 item 11 (A6.3-12) | D3-R13 | 6.3 | D3 | C | SUJ | N | parcial | C declarativo, aderência parcial |
| 8.4 item 2 (A8.4-08) | D4-R16 | 8.4 | D4 | E [TS] | APL | S (expositor; fecho de acerto) | direta | E com moldura, troca de sujeito |

Composição exigida pela ficha: ao menos 1 E com moldura (D4-R16), 1 item de cada lote (D4 e D3), 1 C (D3-R03, D3-R13) e 1 parcial (D3-R13) — CONFERE. Os dois itens que o R1 pediu para "acompanhar" (D3-R02 e D4-R14) foram lidos fora da amostra e não entram na taxa (seção 3).

## 2. Vereditos por item

Palavras: só o enunciado, sem o comando.

| id | gab. | mecanismo | marcadores | palavras | veredito | motivo |
|---|---|---|---|---|---|---|
| D4-R03 | E [TS] | E2 (fortalecimento → enfraquecimento, R55, alínea i) | "Considere que um analista", "ele estará correto ao incluir entre elas" | 31 | CONFORME | Uma afirmação, uma troca, literal da alínea. Extensão igual à média de E da base. Registro adequado. Não há termo absoluto. A moldura de analista é decorativa, mas é a forma canônica do lote (D4-03, D4-08) e não decide o gabarito. Sem ela, o item viraria DEF, e a 8.1 está no teto de DEF (6 de 20; ficha, seção 3.5). **Achado (pista cruzada, não do item isolado):** D4-R03 (E) e D4-R18 (C) abrem com a mesma frase e julgam alíneas da mesma lista. O D4-R18 afirma, como C, o "fortalecimento das capacidades de coordenação e monitoramento… pelo núcleo de governo", o que sinaliza à candidata que o pós-NPM não "enfraquece" o Estado e ajuda a resolver o D4-R03 sem conhecer a alínea i. Correção: nota de simulado (AJ-E2). |
| D3-R03 | C | C6 (afirmação parcial verdadeira; omite "solidariamente/subsidiariamente" sem marcador de exclusividade) | "Considere que órgão do Poder Legislativo da União", "Nessa situação, nos termos da Lei" | 54 | CONFORME | Fiel ao art. 121, § 2º (hipótese, condição e encargos). "resultantes da execução do contrato" vem do caput do mesmo artigo e não altera o sentido. O ponto de julgamento (a condição "se comprovada falha") é claro. A moldura é a da cota e não decide nada. É o C com moldura que, na leva, quebra a série moldura → E (D3: 1 C / 3 E com moldura). A extensão está no alto dos C (54; teto da base 65), mas aceitável para cenário. Registro de leva: abre com a mesma fórmula "Nessa situação, nos termos d…" que os outros 5 itens com "Considere que" do D3 (seção 4.3, rec. L2-3). |
| D3-R13 | C | C2 (reprodução do art. 22, caput, do CDC) | "Nos termos do", "qualquer" (literal da norma, em C) | 41 | AJUSTE (texto) | Gabarito e ponto corretos. O termo amplo "sob qualquer outra forma de empreendimento" é a letra do artigo, num C, como a seção 5.1 do estilo_banca recomenda. **Defeito de clareza:** a ordem inversa ("são obrigados a fornecer serviços adequados, eficientes, seguros e, quanto aos essenciais, contínuos os órgãos públicos, …") empurra o sujeito para depois de um predicativo de 11 palavras. A sequência "contínuos os órgãos públicos" admite uma leitura de passagem errada ("contínuos" como atributo de "órgãos"), e a inversão não faz parte do estilo da banca para reprodução de dispositivo. A ordem direta é a própria letra do art. 22, caput: o item fica literal, com o mesmo número de palavras e o mesmo gabarito (AJ-E1). Discriminação baixa, como todo C2 de memória, sem defeito de estilo. Em pertinência (o item não toca a omissão), a QA já aceitou a aderência parcial; não é matéria de estilo. |
| D4-R16 | E [TS] | E1 (liderança → unidades de apoio, R64; troca de sujeito) | "Considere que, em audiência pública de comissão da Câmara dos Deputados, um expositor afirme que, de acordo com o Referencial…", "a afirmação do expositor é correta" | 52 | CONFORME | Uma afirmação, uma troca, literal de R64, atribuída ao TCU (B2). Registro formal. Não há termo absoluto. O E está na letra da base, e não na moldura (R1 da T-122). **Observação de discriminação (não reprova):** a troca vai para um ator cujo nome ("unidades de apoio") já sugere que ele não cria valor para a sociedade. A candidata pode acertar por senso comum, numa versão fraca do critério do L1-R140 (onda F1). Trocar o sujeito por um ator mais plausível exigiria um novo lastro no adendo e uma nova QA; é escolha da produção, não texto exato, e por isso não há AJ (ficha, seção 4.3). **Achado de co-ocorrência:** D4-R15 e D4-R16 têm a mesma abertura, a mesma fonte (TCU, unidades de apoio), o mesmo fecho e o mesmo gabarito (E). Juntos num simulado, formam a série "expositor + TCU = E". Correção: nota de simulado (AJ-E2). |

Taxa de NÃO CONFORME: 0/4. AJUSTE (texto): 1/4 (D3-R13), sem mudança de gabarito. Itens decididos pela moldura: 0 (os 2 E com moldura lidos, D4-R16 e, fora da amostra, D3-R02 e D4-R14, têm troca literal declarada).

## 3. Fora da amostra (lidos a pedido do R1, seção 7, item 4; sem veredito, fora da taxa)

- **D3-R02 (E, APL, 46 palavras).** O cenário lista um a um os elementos do art. 186 ("voluntariamente", "deixe de adotar providência", "viole direito", "cause dano"), e a conclusão nega frontalmente: "a omissão voluntária não configura ato ilícito". O cenário foi montado para caber na definição, e a negação operativa aparece no fecho. As duas coisas inclinam para E: é uma pista de forma moderada. A versão original da ficha ("só ação") pediria "somente" e ", e não" num E, dois marcadores que a leva já concentra em E (seção 4.4). Texto opcional, que tira a negação frontal e mantém o ponto (A6.3-01), o gabarito E e o mecanismo E3:
  `AJ-E3 (opcional) | D3-R02 | enunciado | substituir: «Nessa situação, nos termos do art. 186 do Código Civil, a omissão voluntária não configura ato ilícito.» | por: «Nessa situação, nos termos do art. 186 do Código Civil, a configuração de ato ilícito exigiria que o dano decorresse de ação do servidor.»`
  O AJ-E3 muda o campo Troca e por isso volta à gcb-cqfp, se a GCB o aceitar: `substituir: «Troca: ação ou omissão voluntária → a omissão voluntária não configura ato ilícito (CC, art. 186)» | por: «Troca: ação ou omissão voluntária → exigiria ação (CC, art. 186)»`. Sem ele, o item fica como está, com este registro.
- **D4-R14 (E, APL, 41 palavras).** "integralmente" é literal de R44, e a troca é a polaridade (não irá → irá). O absoluto é o próprio ponto, e não um acessório. Na leva, os absolutos ficam em 1 C (D3-R13, "qualquer") e 2 E (D4-R14, "integralmente"; D4-R15, "quase sempre", que é a letra da fonte e não a troca). Sem desequilíbrio que configure pista. Sem achado.

## 4. Risco de padrão "moldura do Legislativo / 'Considere que' → E" (por script)

### 4.1 "Considere que" (CQ) e moldura × gabarito

| escopo | n | C/E | CQ C/E (%C) | sem CQ C/E (%C) | phi CQ→E | Fisher p | moldura S C/E (%C) | moldura N C/E (%C) | phi moldura→E | Fisher p |
|---|---|---|---|---|---|---|---|---|---|---|
| D4 canônicos | 79 | 41/38 | 21/8 (72,4%) | 20/30 (40,0%) | −0,31 | 0,010 | 12/0 (100%) | 29/38 (43,3%) | −0,41 | <0,001 |
| D4 leva 1 | 17 | 7/10 | 2/9 (18,2%) | 5/1 (83,3%) | +0,63 | 0,035 | 1/6 (14,3%) | 6/4 (60,0%) | +0,46 | 0,134 |
| **D4 acumulado** | 96 | 48/48 | **23/17 (57,5%)** | 25/31 (44,6%) | **−0,13** | **0,301** | **13/6 (68,4%)** | 35/42 (45,5%) | −0,18 | 0,123 |
| D3 canônicos | 71 | 31/40 | 15/10 (60,0%) | 16/30 (34,8%) | −0,24 | 0,049 | 6/1 (85,7%) | 25/39 (39,1%) | −0,28 | 0,038 |
| D3 leva 1 | 13 | 8/5 | 3/3 (50,0%) | 5/2 (71,4%) | +0,22 | 0,592 | 1/3 (25,0%) | 7/2 (77,8%) | +0,50 | 0,217 |
| **D3 acumulado** | 84 | 39/45 | **18/13 (58,1%)** | 21/32 (39,6%) | **−0,18** | **0,118** | **7/4 (63,6%)** | 32/41 (43,8%) | −0,13 | 0,332 |
| Folha 8.1 acumulada | 20 | 10/10 | 4/6 (40,0%) | 6/4 (60,0%) | +0,20 | 0,656 | 2/3 | 8/7 | +0,12 | 1,000 |
| Folha 6.3 acumulada | 20 | 10/10 | 5/5 (50,0%) | 5/5 (50,0%) | 0,00 | 1,000 | 2/3 | 8/7 | +0,12 | 1,000 |
| Folha 8.4 acumulada (parcial; fecha na leva 2) | 10 | 4/6 | 2/4 (33,3%) | 2/2 (50,0%) | +0,17 | 1,000 | 1/3 | 3/3 | +0,25 | 0,571 |
| **Leva 1 inteira** | 30 | 15/15 | **5/12 (29,4%)** | **10/3 (76,9%)** | **+0,47** | **0,025** | **2/9 (18,2%)** | 13/6 (68,4%) | **+0,48** | **0,021** |

Regra ingênua "CQ → E; sem CQ → C": acerta 42/96 = 43,8% no D4 acumulado e 34/84 = 40,5% no D3 acumulado, abaixo da classe majoritária (50,0% e 53,6%). Na folha 8.1, acerta 60%; na 6.3, 50%. **Na leva 1 isolada acerta 22/30 = 73,3%**, e a regra "moldura → E" também acerta 73,3%, contra 50% da classe majoritária.

Leitura:
1. No banco acumulado não há pista para E. A leva diluiu o viés antigo da abertura para C (D4: phi de −0,31 para −0,13; D3: de −0,24 para −0,18; nenhum dos dois significativo) sem invertê-lo, e as folhas completas ficam equilibradas. É o efeito pretendido pela D-MOLDURA-CE e pela regra 11 da ficha.
2. **Dentro da leva 1, a correlação inverteu e é significativa**: CQ dá 12 E em 17, e o declarativo dá 10 C em 13. Isso decorre do plano de antecipação (9 dos 11 itens com moldura são E por desenho; ficha, seção 2.2), e não de defeito de item. O risco existe só se a leva 1, ou um recorte só do reforço, for usada isolada num simulado. Montado por folha, com os canônicos, o simulado não carrega o sinal.

### 4.2 Abertura detalhada × gabarito (canônico | leva 1 | acumulado)

| lote | abertura | canônico | leva 1 | acumulado |
|---|---|---|---|---|
| D4 | "Considere que, em audiência pública de comissão da Câmara dos Deputados, um expositor…" | 12/0 | 1/6 | 13/6 |
| D4 | "Considere que um analista…" | 2/0 | 1/3 | 3/3 |
| D4 | "Considere que…" sem moldura (outros) | 7/8 | 0/0 | 7/8 |
| D4 | declarativo direto | 7/10 | 5/1 | 12/11 |
| D4 | declarativo com remissão ("Nos termos", "Segundo"…) | 13/20 | 0/0 | 13/20 |
| D3 | "Considere que órgão/servidor do Poder Legislativo da União…" ou sessão da Câmara | 6/1 | 1/3 | 7/4 |
| D3 | "Considere que…" sem moldura | 9/9 | 2/0 | 11/9 |
| D3 | declarativo direto | 11/19 | 0/0 | 11/19 |
| D3 | declarativo com remissão | 5/11 | 5/2 | 10/13 |

### 4.3 Fecho × gabarito (D4)

| fecho | canônico | leva 1 | acumulado |
|---|---|---|---|
| "a afirmação do expositor é correta" (K2) | 3/0 | 1/4 | 4/4 |
| "ele estará correto ao…" (K2) | 2/0 | 1/2 | 3/2 |
| **"Nessa situação, é correto afirmar que…" (neutro)** | 0/0 | **0/3** | **0/3** |
| outro "Nessa situação…" | 14/7 | 0/0 | 14/7 |
| sem fecho | 22/31 | 5/1 | 27/32 |

**Achado (indício, n = 3):** o fecho neutro foi criado pela leva 1 (D4-R08, D4-R13, D4-R17) e só existe em E. Se a leva 2 repetir o uso, ele vira o primeiro marcador de E do D4 com 100% de acerto. A produção já registrou o problema (Pendências, item 3). Correção: rec. L2-1.

No D3, todos os 6 itens com "Considere que" da leva fecham com "Nessa situação, nos termos d…" (3 C / 3 E). Não há pista, mas a fórmula repete o defeito que a onda F1 apontou na rec. 2 ("Nessa situação, segundo a Lei…"). Correção: rec. L2-3.

### 4.4 Outros marcadores na leva (30 enunciados; nenhum decide o gabarito — estilo_banca, seção 4)

| marcador | C | E | itens |
|---|---|---|---|
| negação operativa "não" | 0 | 3 | E: D4-R10, D4-R13, D3-R02 |
| contraste ", e não …" | 0 | 2 | E: D4-R10, D4-R13 (no D4 acumulado: 0 C / 2 E; nos canônicos, 0/0) |
| "qualquer" | 1 | 0 | C: D3-R13 (letra da norma) |
| "integralmente" | 0 | 1 | E: D4-R14 (é a troca) |
| "sempre" (em "quase sempre") | 0 | 1 | E: D4-R15 (letra da fonte; a troca é internos → externos) |
| "depende" | 0 | 1 | E: D3-R08 (é a troca) |
| "somente", "apenas", "só", "nunca", "todo", "exclusiv-" (fora de "dedicação exclusiva"), "independentemente" | 0 | 0 | — |

Extensão na leva: C média 35,0 (mediana 35, de 19 a 56); E média 43,3 (mediana 44, de 28 a 58). A diferença (+8,3 para E) vai no mesmo sentido da base (+3,1 para E), mas é maior, porque a moldura se concentra em E. Não há item fora da faixa. Registro, sem efeito.

Termos absolutos: nenhum C com absoluto falso, nenhum E com absoluto acessório. A seção 5.1 do estilo_banca é cumprida.

## 5. Textos exatos (formato da ficha, seção 4.3; cada trecho atual ocorre 1 vez no arquivo da leva, conferido por grep)

`AJ-E1 | D3-R13 | enunciado (seção 1) | substituir: «são obrigados a fornecer serviços adequados, eficientes, seguros e, quanto aos essenciais, contínuos os órgãos públicos, por si ou suas empresas, concessionárias, permissionárias ou sob qualquer outra forma de empreendimento.» | por: «os órgãos públicos, por si ou suas empresas, concessionárias, permissionárias ou sob qualquer outra forma de empreendimento, são obrigados a fornecer serviços adequados, eficientes, seguros e, quanto aos essenciais, contínuos.»`
(Efeito: ordem direta, igual à letra do art. 22, caput; mesmo gabarito C, mesmo ponto, mesmo mecanismo C2, 41 palavras; nenhum outro campo muda.)

`AJ-E2 | bloco à GCB (seção 5), notas "não pôr no mesmo simulado" | substituir: «(f) D3-R05 e D3-R02 (CC, art. 186; elementos distintos do mesmo artigo; nota preventiva).» | por: «(f) D3-R05 e D3-R02 (CC, art. 186; elementos distintos do mesmo artigo; nota preventiva); (g) D4-R03 e D4-R18 (mesma abertura e mesma lista de tendências do pós-NPM; o "fortalecimento" afirmado no D4-R18, C, sinaliza o erro do D4-R03, E; gbq-estilo, auditoria da leva 1); (h) D4-R15 e D4-R16 (mesma abertura, mesma fonte do TCU sobre unidades de apoio, mesmo fecho e mesmo gabarito E; gbq-estilo, auditoria da leva 1).»`

AJ-E3 (opcional, fora da amostra): seção 3.

## 6. Recomendações à ficha da leva 2 (texto exato para a gcb-gerencia incluir na seção 3 da ficha da leva 2; sem efeito sobre os 30 itens da leva 1)

- **L2-1 (fecho neutro do D4):** "Na folha 8.4 (leva 2), ao menos 2 itens C usam o fecho neutro 'Nessa situação, é correto afirmar que …'. Nenhum item E novo do D4 usa esse fecho até o D4 acumulado com ele chegar a 40% de C (partida: 0 C / 3 E, D4-R08, D4-R13 e D4-R17)."
- **L2-2 (abertura na leva):** "Na leva 2, os itens com 'Considere que' ficam com ao menos 40% de C, e os declarativos (sem 'Considere que'), com ao menos 40% de E (leva 1: 'Considere que' 5 C / 12 E; declarativos 10 C / 3 E; regra ingênua 'Considere que → E' com 73,3% de acerto na leva isolada). A cota de E com moldura da seção 2.2 prevalece; o equilíbrio vem dos itens sem moldura."
- **L2-3 (fórmula do D3):** "Nas folhas do D3 (6.4), no máximo metade dos itens com 'Considere que' usa a fórmula 'Nessa situação, nos termos d…'. Os demais usam 'Nessa situação, …' com a norma citada no cenário ou no fim do enunciado (leva 1: 6 de 6)."
- **L2-4 (contraste e troca de sujeito):** "No D4, ao menos 1 item C novo usa o contraste ', e não …' (acumulado: 0 C / 2 E). Em item SUJ, o sujeito trocado é um ator que a própria fonte menciona e que seria plausível na função, não um ator cujo nome já negue a função (D4-R16, 'unidades de apoio')."
- **À GBQ (montagem de simulado):** a leva 1 não forma simulado isolado; seus itens entram misturados por folha, com os canônicos (seção 4.1, leitura 2). Valem as notas (a) a (h) do bloco à GCB.

## 7. Registros

1. Nome do arquivo: este relatório segue o nome da ordem recebida (saida/banco/estilo_DA_reforco_leva1.md). A ficha, seção 1, regra 15, prevê saida/banco/estilo_onda_DA_L01.md. A GCB renomeia na reconciliação, se quiser.
2. A amostra foi fixada pela ficha (seção 5). O sorteio de reserva (semente 20261020) não foi aplicado.
3. A fidelidade às bases foi lida nos trechos literais transcritos nos blocos comentados e no parecer R2. Nenhuma página foi reaberta: isso é matéria da gcb-cqfp e do qa-normativo-da.
4. Nada vai à plataforma nem à candidata. Nenhuma tarefa nova (D-COMPLEMENTOS). Nenhum gatilho em PARA_PRESIDENCIA.md.

AVISO: os vereditos, a atribuição de mecanismo e a leitura de pista são julgamento deste agente (gbq-estilo) e exigem revisão da GBQ. As contagens de C/E, aberturas, fechos, moldura, marcadores e extensão vêm de script sobre os arquivos gravados (python3 -I, somente leitura), com revisão manual dos itens citados. Com n pequeno (leva de 30; fecho neutro n = 3), nenhuma associação é regra: a tabela serve para corrigir vieses de redação, nunca para prever gabarito.

FIM DA AUDITORIA DE ESTILO — LEVA 01 — REFORÇO DA
