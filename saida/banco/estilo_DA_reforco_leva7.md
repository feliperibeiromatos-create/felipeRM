# estilo_DA_reforco_leva7.md — T-116 — 2026-10-22 — gerado por gbq-estilo

Auditoria de estilo Cebraspe da amostra da leva 7 do reforço de DA (D-REFORCO-2, regra 6; D-REFORCO-DA; ficha, seções 5, 7.4, 7.6, 9.3, 10.2, 11.2, 11.3, 12.2, 13.2 e 13.4.8). Ciclo s16c5. Destino: gcb-cqfp (R1 da leva 7, em paralelo; nada a acrescentar aos AJ do R1) e gcb-gerencia (reconciliação da leva 7). Este agente audita e não produz. Nenhum outro arquivo foi alterado; regras/estilo_banca.md não foi tocado. Sem commit nem push.

**Resultado:** 5 itens auditados (16,7% de 30), sobre a **v1**, em paralelo ao R1 (ficha 9.3, item 6; 13.4.8). Vereditos: 5 CONFORMES (D3-R60, D3-R75, D3-R77, D3-R81 e D3-R85), 0 AJUSTE (texto), 0 NÃO CONFORME. Não há texto de AJ nesta leva. Sem GATE pela regra 6.

**Rito:** cumprido como a ficha 9.3, item 6, e a 13.4.8 mandam. A auditoria correu sobre a v1, antes do R1 gravado (saida/gcb/QA_DA_reforco_leva7_R1_* ausente em disco na hora da leitura). Como não há AJ de estilo, nada segue para a v2 por esta auditoria; a seção 7.6 (errata pós-R2) não se aplica, e a regra da 11.3 (mesmo texto pedido pelo R1 e pelo estilo, aplicado uma vez) fica sem objeto.

**Classificação:** os vereditos, a atribuição de mecanismo, a leitura de pista e o juízo de risco de "mais de uma interpretação" são julgamento deste agente (gbq-estilo) e exigem revisão da GBQ (ver o AVISO no fim).

## 0. Objeto, entradas e método

| objeto | SHA-256 |
|---|---|
| saida/gcb/DA_reforco_leva7_v1.md (objeto; 30 itens; QA PENDENTE) | fdafc3bd36127778727edb66d863c135f1fa08182757b6e58ec4c27ae736a0ed (conferido em disco; igual ao do despacho) |
| saida/gcb/DA_reforco_ficha_2026-10-20.md (amostra: 13.4.8; rito: 5, 7.4, 7.6, 9.3, 10.2, 11.2, 11.3, 12.2, 13.2) | 34fe46fc59e9215966b5568966c7a8a7d831c744760b12e08369a1eebf995391 (conferido em disco; igual ao do despacho) |
| regras/estilo_banca.md (catálogo em disco: **v1.1.3**, linha 2) | 9f9237f5f9828b77d5ab805849a7a14af13fb28fcc1c985fe462ec1027684caf |
| saida/banco/estilo_DA_reforco_leva6.md (modelo de forma e critérios) | 495750313bfc76d9c98d90b96610456bc2859d42d7a2c1dececa98793a4443b8 (lido; não alterado) |
| saida/gcb/normativo_cache/Lei_9784_1999_2026-10-20.txt (D3-R60: linhas 70, 72 e 75) | f9452916c03521a8435caae49c8feb690ae2b02086424b641204374f38f9ae19 |
| saida/gcb/normativo_cache/Lei_4619_1965_2026-10-20.txt (D3-R75: art. 6º; lei inteira lida para L7-1) | b91ef03df94717e00602b1b5195f73176c1c5cf5bebe6d80fba1cbaf37a9082f |
| saida/gcb/normativo_cache/Decreto_20910_1932_2026-10-20.txt (D3-R77: arts. 4º, caput e parágrafo único, e 5º; decreto inteiro lido) | a8a216f2cd510ace7eda954a9d0800939b6d0be19e5b10d9626d5d073aa2818a |
| saida/gcb/D3_anexo_N_mapa_normativo.md (D3-R81: Lei 8.429, art. 8º, caput, e art. 8º-A, linhas 211 a 213; D3-R85: art. 21, caput, I, II e §§ 1º a 5º, linhas 422 a 429; multa civil no art. 12, linhas 278 a 280) | 2ef58f9b50a23472fa733731db30fa998492698472ab873443d6a64d422ff1df |
| saida/gcb/D3_anexo_N_adendo_2026-10-22.md (Lei 4.619, art. 6º; Decreto 20.910, art. 4º) | 826e32b511ad448e66c760bda23e34c0940db847d04a54f87b97dcf19ef85c43 |
| saida/pacote/pacote.json v1.13 (só os enunciados de D3-24, D3-28, D3-74 e D3-75, para L3-3 e "Difere de") | 82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240 |

A Lei 8.429 não tem cópia em normativo_cache/ (ficha 13.4.2 e 13.5, item 3): os trechos do D3-R81 e do D3-R85 foram lidos no Anexo N do D3, seção 4.9 (limitação de método, sem bloqueio).

**Script:** python3 -I, somente leitura, no scratchpad da sessão, sobre as seções 1 e 2 do arquivo da leva. Ele extrai enunciados e gabaritos e conta abertura × gabarito, a fórmula "Nessa situação, nos termos d…", "Nessa situação," em geral, marcadores por gabarito (sempre, somente, apenas, só, exclusivamente, qualquer, todo/toda/todas, nenhum, única, "pois", "não", "sem", "também", "impede", "continua"), extensão (palavras separadas por espaço, só o enunciado) e prefixos comuns de cena (L3-3). As contagens de folha fechada, de moldura acumulada e de moldura × fórmula no D3 não foram refeitas: vêm da seção 4 do arquivo da leva e são matéria do R1.

**Conferência por script (leva 7, 30 itens; 15 C / 15 E):**
- "Considere que": 6 C / 4 E; declarativos: 9 C / 11 E.
- Fórmula "Nessa situação, nos termos d…": 1 C / 2 E, em 3 dos 10 CQ (D3-R65, D3-R77, D3-R86; 1 por folha). Outras aberturas do fecho com "Nessa situação," (sem a fórmula): 5 C / 2 E.
- Fecho "é correto afirmar que": 0.
- Absolutos nos enunciados: "somente" 1 C (D3-R79) / 1 E (D3-R82, letra, fora da troca); "uma única vez" 1 C (D3-R88); "qualquer" e "todo" 0 C / 1 E (D3-R80, letra); "todas" 0 C / 1 E (D3-R72, letra). Nenhum E com absoluto inserido pela troca.
- "pois": 0 C / 0 E.
- Negação "não" nos enunciados: 4 C (D3-R60, R76, R83, R89) / 1 E (D3-R75, letra "não excederá"); "sem": 0 C / 1 E (D3-R84, letra "sem prejuízo").
- Extensão: C de 13 a 47 palavras (média 34,7); E de 25 a 53 (média 37,5).

Conferem com as seções 0 e 4.6 do arquivo e com a ficha 13.4.6.

**Critérios de estilo:** os mesmos das levas 1 a 6 (estilo da leva 6, seção 0):
- comando C/E;
- uma afirmação, com um só ponto de erro;
- troca real e única;
- nenhuma pista de forma;
- extensão dentro da faixa da base (estilo_banca v1.1.3, seção 4: C de 8 a 65 palavras; E de 19 a 62);
- registro formal;
- termo absoluto só quando for letra da fonte ou a própria troca;
- moldura que não decide o gabarito (R1 da T-122);
- risco de "mais de uma interpretação" (estilo_banca, seção 5.3);
- 7.4 (itens 2 a 5), L3-1 a L3-5 (ficha 9.3), L4-1 a L4-4 e itens 5 e 6 da ficha 10.2, L5-1 e L5-2 (11.2), L6-1 e L6-2 (12.2), L7-1 a L7-3 e a regra "E sem [TS] só em E3 por contraste, E5 ou E6" (13.2, itens 1 a 4).

Vereditos:
- **NÃO CONFORME:** dois pontos de erro, pista que entrega o gabarito, E decidido pela moldura, ou gabarito que só se sustenta com escolha da produção.
- **AJUSTE (texto):** defeito sanável por substituição exata, sem mudar gabarito, ponto, mecanismo nem a natureza da troca.

## 1. Amostra

Fixada pela ficha, seção 13.4.8, antes da produção. Sem sorteio.

| id | folha | lote | gab. | formato | moldura | aderência | o que cobre |
|---|---|---|---|---|---|---|---|
| D3-R60 | 5.1 | D3 | C | SIT | N | direta | C da 5.1 com "Considere que"; Lei 9.784, art. 13, caput e III |
| D3-R75 | 6.1 | D3 | E [TS] | NUM | N | parcial | única troca de número da leva (L6-1, L7-1); Lei 4.619, art. 6º |
| D3-R77 | 6.1 | D3 | E [TS] | APL | S (órgão/servidor do Poder Legislativo da União) | parcial | E com moldura e com a fórmula (L7-2); Decreto 20.910, art. 4º, caput |
| D3-R81 | 7 | D3 | E | SIT | N | direta | E sem [TS], E5 (13.2, item 4); Lei 8.429, art. 8º, caput |
| D3-R85 | 7 | D3 | E [TS] | APL | S (idem) | direta | E com moldura sem a fórmula (L7-2); Lei 8.429, art. 21, caput e II |

**Composição exigida (ficha, seção 5): CONFERE.**
- Tamanho: ⌈10% de 30⌉ = 3; foram designados 5.
- Ao menos 1 E com moldura: D3-R77 (6.1) e D3-R85 (7), os dois da leva.
- Todos os lotes da leva: só há o D3, e os 5 itens são dele. As três folhas estão cobertas.
- Ao menos 1 C: D3-R60.
- Ao menos 1 parcial: D3-R75 e D3-R77 (aderência fixada pelo mapa do adendo de 22/10/2026; ficha 13.6). A pertinência é da gcb-cqfp.

## 2. Vereditos por item

Palavras: só o enunciado, sem o comando.

| id | gab. | mecanismo | trecho decisivo | palavras | veredito | motivo |
|---|---|---|---|---|---|---|
| D3-R60 | C | C2 (reprodução próxima do texto normativo; declarado e confirmado) | "a matéria de competência exclusiva da autoridade não pode ser objeto de delegação" | 40 | **CONFORME** | **Reprodução da letra.** A Lei 9.784, art. 13, diz "Não podem ser objeto de delegação: […] III - as matérias de competência exclusiva do órgão ou autoridade" (cópia, linhas 72 e 75). O item cita a lei e reproduz o inciso III, com "da autoridade" no lugar de "do órgão ou autoridade" (subconjunto, sem mudar o sentido). Um só ponto.<br><br>**Cena sem segunda leitura.** "pretenda delegar a outro órgão" é a delegação do art. 12 (cópia, linha 70: "a outros órgãos ou titulares"), e a cena não traz a ressalva "se não houver impedimento legal" nem outro elemento que abra discussão. Sem absoluto, sem "mas não" e sem qualificador. "Nessa situação, a Lei nº 9.784/1999 estabelece que" não é a fórmula "nos termos d…" (a da 5.1 é o D3-R65, a única da folha). Extensão dentro da faixa de C. Registro formal.<br><br>**Forma a favor do equilíbrio.** É um C com "Considere que" e com negação operativa ("não pode"): na leva, "não" fica em 4 C / 1 E, e o CQ da leva em 6 C / 4 E. É o C com negação que a estilo_banca 3.13 e 4 pedem para que "não" não vire marca de E.<br><br>**Observação (discriminação):** a cena repete no fecho o atributo que decide ("competência exclusiva"), e o adjetivo "exclusiva" já sugere, pelo senso comum, a indelegabilidade. O item discrimina pouco entre candidatas preparadas, mas não tem defeito: é letra, e a justificativa, linha 2, aponta a tentação real (a conveniência do art. 12, caput). O par com o D3-R61 (nota (ce)) não lê um ao outro: o D3-R60 não menciona atos normativos. |
| D3-R75 | E [TS] | E3 (altera o comando: troca de número no teto; declarado e confirmado) | "o qual não excederá um terço da importância de seu vencimento ou remuneração" | 39 | **CONFORME** | **Uma troca, de número.** A Lei 4.619, art. 6º, diz "A liquidação do que fôr devido pelo funcionário estável à Fazenda Nacional poderá ser feita mediante desconto em fôlha de pagamento, o qual não excederá de uma quinta parte, da importância de seu vencimento ou remuneração" (cópia; adendo de 22/10/2026), e o item põe um terço. O resto é a letra em ortografia atual (alerta B7, grafias só na Base). Sujeito "funcionário estável" mantido (ficha 13.6).<br><br>**Sentido da troca (L6-1), a favor.** A letra é um teto ("não excederá"). A troca para mais afirma um teto que a lei não dá: um desconto de um quarto caberia no item e não cabe na lei. A troca para menos ficaria compatível com a leitura de limite.<br><br>**L7-1 cumprida.** "terço" ocorre 0 vez na Lei 4.619 (conferido na cópia inteira; a lei tem 7 artigos), e o art. 6º é o único dispositivo da lei sobre desconto. O valor posto não é o de outra figura nem de outro rito da mesma norma, e não há segunda leitura.<br><br>A permissão "poderá ser feita" é letra e não é a troca. Sem absoluto inserido, sem "mas não" e sem qualificador. Declarativo, sem moldura. Extensão dentro da faixa de E. Registro formal.<br><br>**Observação (justificativa, linha 2):** "a tentação é lembrar de outro limite de desconto fora desta lei" não nomeia o limite nem tem base no Anexo ou no adendo. A frase não afirma um valor, mas fica perto do que a ficha 4.2 chama de "afirmação fora da base". A escolha é da gcb-cqfp; o enunciado não muda. |
| D3-R77 | E [TS] | E3 (nega a consequência: "não corre" → "continua a correr"; declarado; fronteira com E2, inversão de polaridade) | "a prescrição continua a correr durante essa demora" | 53 | **CONFORME** | **Uma troca, de polaridade, na letra.** O Decreto 20.910, art. 4º, caput, diz "Não corre a prescrição durante a demora que, no estudo, ao reconhecimento ou no pagamento da dívida, considerada líquida, tiverem as repartições ou funcionários encarregados de estudar e apurá-la" (cópia, linha 14). A cena usa a letra ("dívida considerada líquida", "as repartições ou funcionários encarregados de estudar e apurar", no plural, como a ficha 13.6 exige), e o fecho afirma que a prescrição corre. É uma troca só. O "requerido" da cena atende o parágrafo único (entrada do requerimento; cópia, linha 15).<br><br>**Uma só leitura.** O art. 5º (cópia, linha 16) tira o efeito suspensivo da demora **do titular** do direito; a cena põe a demora nas repartições, e o art. 5º não entra. A omissão de "ao reconhecimento" reduz a hipótese a um subconjunto, sem mudar o efeito. O gabarito não depende de escolha da produção. Mecanismo: E3 ("nega a consequência prevista", 3.3) é defensável; pela forma, é também inversão de polaridade (E2). Com o [TS] declarado, a fronteira não tem efeito (estilo_banca 5.1; ficha 13.3, primeiro registro).<br><br>**Negação frontal (7.4.5; 10.2, item 5): não se configura como pista.** A cena traz os elementos do art. 4º, e o fecho afirma o oposto da consequência. Isso lembra o D3-R02 da leva 1. Há duas diferenças. Primeira: o fecho é afirmativo ("continua a correr"); o "não" da letra sai do E, e a 10.2, item 5, mira a negação com "sem" ou "não". Segunda: a estrutura "cena montada com a hipótese da letra + consequência no fecho" aparece na leva em 4 C (D3-R60, R71, R73, R89) e neste E, e por isso não inclina para E. A troca "não corre → corre" é a do plano (ficha 13.4.4).<br><br>**A moldura não decide.** O órgão do Poder Legislativo da União é só o destinatário do requerimento de pagamento de dívida da União (Decreto 20.910, art. 1º: "dívidas passivas da União"). Não há norma interna, regimento nem prática real da Câmara. A leitura "Legislativo → o decreto não se aplica" não tem apoio na letra e não é o caminho da justificativa.<br><br>**L7-2 cumprida.** É o único E com moldura da leva que usa a fórmula (1 de 2), e a única fórmula da 6.1. Cena distinta da do D3-28 (servidor que causa dano) e da do D3-R85 (L3-3; nenhum prefixo comum de 25 caracteres ou mais com outro item da leva, dado do script). Extensão: 53 palavras, a maior da leva, dentro da faixa de E (L5-1). Registro formal. |
| D3-R81 | E | E5 (segmento acessório falso em moldura verdadeira; declarado; fronteira com E3, "cria um dever inexistente") | "sujeitando-se também à multa civil" | 42 | **CONFORME** | **A moldura é verdadeira, e o segmento é falso.** A Lei 8.429, art. 8º, caput, diz "O sucessor ou o herdeiro daquele que causar dano ao erário ou que se enriquecer ilicitamente estão sujeitos apenas à obrigação de repará-lo até o limite do valor da herança ou do patrimônio transferido" (Anexo N do D3, 4.9, linha 211). "o herdeiro está sujeito à obrigação de reparar o dano até o limite do valor da herança" é a letra. A cauda "sujeitando-se também à multa civil" contradiz o "apenas". É um só ponto de erro.<br><br>**E5 sem [TS], defensável (13.2, item 4).** Pela regra de desempate da estilo_banca 3 (moldura verdadeira + segmento falso), o segmento é uma consequência, e não um quantificador nem uma capacidade de método: E5. Não há troca de um elemento da letra, e sim acréscimo; sem troca real, sem marca (ficha, regra 7). Pela substância, o item também "cria um dever inexistente" (E3). Se a gcb-cqfp reclassificar para E3 e pedir [TS], o teste de [TS] da folha 7 reprova (ficha 13.4.7 e 13.5, item 2), e a decisão é dela e da GCB.<br><br>**O "apenas" da letra sai, e isso é coerente.** O "apenas" é o elemento que o segmento falso contradiz. Mantê-lo ao lado de "também à multa civil" daria um item contraditório em si. A L6-2 (absoluto literal que não é a troca) não se aplica, e a L5-2 é cumprida (sem "só" nem verbo de condição necessária).<br><br>**Uma só leitura, com uma observação.** O art. 8º-A, parágrafo único (linha 213), trata da sucessora de pessoa jurídica, e não do herdeiro; não cria segunda leitura. A cena não diz se houve condenação antes do óbito. A leitura natural é a de dano ainda não julgado, e o gabarito se sustenta pela letra ("apenas"), sem jurisprudência. O risco de recurso pela tese da multa já imposta é baixo e fica fora da letra; registro, sem AJ.<br><br>Sem absoluto inserido, sem "mas não" e sem qualificador. "também" fica em 1 C (D3-R89) / 1 E na leva. Cena distinta da do D3-R89 (prefixo comum "Considere que determinada pessoa ", 33 caracteres; L3-3) e da do D3-R18 (6.4; nota (cp)). Extensão dentro da faixa de E. Registro formal. |
| D3-R85 | E [TS] | E3 (cria consequência inexistente: "independe" → "impede"; declarado e confirmado) | "a aprovação das contas impede a aplicação ao gestor das sanções por ato de improbidade administrativa" | 46 | **CONFORME** | **Uma troca, na letra.** A Lei 8.429, art. 21, diz "A aplicação das sanções previstas nesta lei independe: […] II - da aprovação ou rejeição das contas pelo órgão de controle interno ou pelo Tribunal ou Conselho de Contas" (Anexo N do D3, 4.9, linhas 422 e 424; redação original). O item afirma que a aprovação impede. É uma troca só.<br><br>**Uma só leitura.** Os §§ 1º e 2º do art. 21 (linhas 425 e 426) mandam o juiz **considerar** os atos e as decisões dos órgãos de controle; não dão à aprovação efeito de impedir a sanção. O § 4º usa "impede" para a absolvição criminal confirmada por colegiado e tem nota "(Vide ADI 7236)" e "(Vide ADI 7156)"; o item não toca nele, e a cena não fala em ação penal. O gabarito se sustenta pela letra do inciso II.<br><br>**A moldura não decide.** O órgão do Poder Legislativo da União só situa o gestor cujas contas o Tribunal de Contas aprovou. O art. 1º, § 5º, da Lei 8.429 nomeia o Poder Legislativo (Anexo N do D3, 4.9, linha 197), e a cena não sugere o contrário. Não há norma interna nem prática real da Câmara.<br><br>**L7-2 cumprida.** Sem a fórmula "nos termos d…": cita a lei com "Nessa situação, conforme a Lei nº 8.429/1992", forma que a L7-2 admite. "Nessa situação," sem a fórmula fica em 5 C / 2 E na leva, e não é atalho. Cena distinta da do D3-74 (nomeação do cônjuge) e da do D3-R77 (L3-3). O "Tribunal de Contas" da cena é elemento do inciso II. "impede" não é absoluto inserido do tipo da L3-2. Sem "mas não", sem qualificador e sem negação no fecho (10.2, item 5). Extensão dentro da faixa de E. Registro formal. |

**Taxas:**
- NÃO CONFORME: 0/5.
- AJUSTE (texto): 0/5.
- Itens decididos pela moldura: 0. Nos dois itens com moldura (D3-R77 e D3-R85), o E está na letra.

## 3. Conferência de 7.4, L3-1 a L3-5 (ficha 9.3), L4-1 a L4-4, itens 5 e 6 (10.2), L5-1 e L5-2 (11.2), L6-1 e L6-2 (12.2), L7-1 a L7-3 e item 4 (13.2) nos 5 itens

| regra | D3-R60 (C) | D3-R75 (E) | D3-R77 (E) | D3-R81 (E) | D3-R85 (E) |
|---|---|---|---|---|---|
| 7.4.2 e L3-1 (abertura por leva e por folha fechada) | CQ C; leva CQ 6 C / 4 E; 5.1 fechada CQ 3 C / 3 E: CONFERE | DC E; leva DC 9 C / 11 E; 6.1 fechada DC 6 C / 8 E: CONFERE | CQ E; 6.1 fechada CQ 5 C / 1 E: CONFERE | CQ E; 7 fechada CQ 4 C / 3 E: CONFERE | CQ E; idem: CONFERE |
| 7.4.3 e 12.2, item 3 (fórmula) | sem a fórmula: CONFERE | declarativo: não se aplica | a única da 6.1: CONFERE | sem a fórmula: CONFERE | sem a fórmula: CONFERE |
| 7.4.5 e 10.2, item 5 (negação frontal) | C: não se aplica | sem cena: não se aplica | fecho afirmativo; estrutura igual à de 4 C da leva: CONFERE (ver seção 2) | acréscimo, sem negar a consequência: CONFERE | cena parcial, fecho sem "sem" nem "não": CONFERE |
| L3-2 (absoluto inserido pela troca) | não se aplica | sem absoluto: não se aplica | sem absoluto: não se aplica | sem absoluto: não se aplica | "impede" não é absoluto do tipo: não se aplica |
| L3-3 (cenário gêmeo) | prefixo de 52 caracteres com o D3-R86, depois cena distinta: CONFERE | declarativo: não se aplica | cena distinta da do D3-28 e da do D3-R85: CONFERE | cena distinta da do D3-R89: CONFERE | cena distinta da do D3-74: CONFERE |
| L3-4 ("mas não" / ", e não") | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE |
| L3-5 (qualificador minimizador) | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE |
| L4-1 (fecho "é correto afirmar que" fora do D4) | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE. Na leva, 0 (script) |
| L4-2 (abertura da 6.2) | não se aplica | não se aplica | não se aplica | não se aplica | não se aplica |
| L4-3 (referente de rol, E6) | C: não se aplica | não é E6 | não é E6 | não é E6 | não é E6 |
| L4-4 (condição inventada sobre hipótese autônoma) | C: não se aplica | E3 de número: não se aplica | não condiciona hipótese a outra: não se aplica | não se aplica | não se aplica |
| 10.2, item 6 (SUJ E com ator plausível) | não é SUJ | não é SUJ | não é SUJ | não é SUJ | não é SUJ |
| L5-1 (extensão) | 40, dentro de 8 a 65 (C): CONFERE | 39, dentro de 19 a 62: CONFERE | 53: CONFERE | 42: CONFERE | 46: CONFERE |
| L5-2 (absoluto da letra retirado de E) | não se aplica | não se aplica | não se aplica | sem "só" nem verbo de condição necessária: CONFERE | não se aplica |
| L6-1 (sentido da troca de número) | não se aplica | para mais, teto: CONFERE | não é troca de número | não é troca de número | não é troca de número |
| L6-2 (absoluto literal que não é a troca) | não se aplica | não se aplica | não se aplica | o "apenas" é o elemento contradito: não se aplica (seção 2) | não se aplica |
| L7-1 (valor da troca igual ao de outra figura da mesma norma) | não se aplica | "terço" 0 vez na Lei 4.619: CONFERE | não se aplica | não se aplica | não se aplica |
| L7-2 (moldura e fórmula) | sem moldura | sem moldura | com a fórmula, 1 dos 2 E com moldura: CONFERE | sem moldura | sem a fórmula: CONFERE |
| L7-3 (restritivo literal por marcador) | não se aplica ao item; na leva, "somente" 1 C (D3-R79) / 1 E (D3-R82): CONFERE | idem | idem | idem | idem |
| 13.2, item 4 (E sem [TS]) | C | com [TS] | com [TS] | E5, declarado na ficha 13.4.4: CONFERE | com [TS] |

As conferências de folha fechada vêm da seção 4 do arquivo da leva e da ficha 13.4.6 e não foram refeitas aqui. As de leva foram refeitas (seção 0).

## 4. Leitura fora da amostra (sem veredito, fora da taxa)

- **Moldura e fórmula no D3 (indício; dado do arquivo, seção 4.6).** No acumulado do D3 (160 itens), moldura com fórmula fica em 2 C / 6 E, e moldura sem fórmula em 7 C / 7 E. O atalho "Legislativo + 'Nessa situação, nos termos d…' → E" acertaria 6 de 8 no D3, contra 8 de 8 no D2. A leva 7 cumpre a L7-2 (1 de 2). O D3 fecha o reforço em D3-R89, e a leitura vale para os lotes que ainda terão moldura (D4 nas levas 8 e 9; D5 nas levas 10 e 11), já cobertos pela L7-2.
- **Inversão da letra nos E com moldura (indício; n = 2).** Os dois E com moldura da leva invertem a letra: "não corre" → "continua a correr" (D3-R77) e "independe" → "impede" (D3-R85). Os dois fechos são afirmativos e não trazem marca lexical comum. Sem efeito de pista nesta leva.
- **"pois": 0 C / 0 E.** A estilo_banca 5.1 recomenda "escreva C com 'pois'", e a ficha não exige isso por leva. Registro.
- **Negação "não" em C (dado do script).** 4 C / 1 E (o E é letra, D3-R75). A leva corrige, no D3, a concentração de negação em E que a estilo_banca 4 registra na base (3 C / 7 E).

## 5. Texto exato (AJ)

Nenhum. Nenhum dos 5 itens tem defeito sanável por substituição exata, e nenhum texto segue para a v2 por esta auditoria. As observações da seção 2 (D3-R60: discriminação; D3-R75: justificativa, linha 2; D3-R81: multa já imposta antes do óbito) não são AJ. A escolha sobre a justificativa do D3-R75 é da gcb-cqfp no R1.

## 6. Recomendações para as próximas levas

Nenhuma regra nova. As leituras da seção 4 estão cobertas pela L7-2 e pela estilo_banca 5.1. Este agente não propõe texto de ficha nesta leva.

## 7. Registros

1. **Rito:** auditoria sobre a v1, em paralelo ao R1, como a ficha 9.3, item 6, e a 13.4.8 determinam. Sem AJ, nada segue para a v2 por esta auditoria. Nenhuma errata pós-R2 (seção 7.6) é proposta.
2. **Versão do catálogo:** o despacho cita "regras/estilo_banca.md (versão em disco)". O arquivo em disco é a **v1.1.3** (linha 2; SHA-256 na seção 0), a mesma das auditorias das levas 1 a 6. Os mecanismos citados (C2, E2, E3, E5) e as seções 3, 3.2, 3.3, 3.5, 3.13, 4, 5.1 e 5.3 são os da v1.1.3. Nada foi alterado no catálogo.
3. **Nome do arquivo:** o da ficha 13.4.8 e 7.5 (saida/banco/estilo_DA_reforco_leva7.md).
4. **Fidelidade às bases:** só se leram as linhas das bases dos 5 itens, para confirmar o trecho decisivo:
   - Lei 9.784, arts. 12 e 13 (cópia);
   - Lei 4.619, inteira (7 artigos; cópia), para a L7-1;
   - Decreto 20.910, inteiro (cópia), com foco nos arts. 1º, 4º e 5º;
   - Lei 8.429, arts. 1º, § 5º, 8º, 8º-A, 12, I a III (multa civil), e 21 (Anexo N do D3, 4.9).

   O art. 5º do Decreto 20.910 e os arts. 1º, § 5º, 8º-A e 21, §§ 1º, 2º e 4º, da Lei 8.429 são citados só como razão de veredito, e não como base de item. A conferência das bases é matéria da gcb-cqfp.
5. **D3-R77 e D3-R81, fronteiras de mecanismo:** E3/E2 no D3-R77 (sem efeito, porque há [TS]) e E5/E3 no D3-R81 (com efeito sobre o [TS], ficha 13.5, item 2). Ficam como declaradas, como a ficha 13.3 (primeiro registro) admite quando a QA não pede [TS]; a decisão é da gcb-cqfp e da GCB.
6. **Escopo:** nada vai à plataforma nem à candidata. Nenhuma tarefa nova (D-COMPLEMENTOS). Nenhum gatilho em PARA_PRESIDENCIA.md. Nenhum NÃO CONFORME, e por isso nenhum GATE pela regra 6.

AVISO: os vereditos, a atribuição de mecanismo, a leitura de pista e o juízo de risco de "mais de uma interpretação" são julgamento deste agente (gbq-estilo) e exigem revisão da GBQ. As contagens de abertura, de fórmula, de fecho, de absolutos e marcadores, de "pois", de extensão e de prefixo de cena vêm de script sobre o arquivo gravado (python3 -I, somente leitura), com revisão manual dos 5 itens. As contagens de folha fechada, de moldura acumulada e de moldura × fórmula no D3 foram tomadas da seção 4 do arquivo da leva e da ficha, sem refazer. Com n pequeno (amostra de 5; recortes de 1 a 30 itens), nenhuma associação é regra, e nenhum marcador decide o gabarito. A tabela serve para corrigir vieses de redação, nunca para prever gabarito.

FIM DA AUDITORIA DE ESTILO — LEVA 07 — REFORÇO DA
