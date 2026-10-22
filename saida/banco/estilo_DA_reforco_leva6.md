# estilo_DA_reforco_leva6.md — T-116 — 2026-10-22 — gerado por gbq-estilo

Auditoria de estilo Cebraspe da amostra da leva 6 do reforço de DA (D-REFORCO-2, regra 6; D-REFORCO-DA; ficha, seções 5, 7.4, 7.6, 9.3, 10.2, 11.2, 11.3, 12.2 e 12.4.8). Ciclo s16c4. Destino: gcb-cqfp (o AJ abaixo segue com os AJ do R1 para a v2 e é conferido no R2) e gcb-gerencia (reconciliação da leva 6). Este agente audita e não produz. Nenhum outro arquivo foi alterado; regras/estilo_banca.md não foi tocado. Sem commit nem push.

**Resultado:** 5 itens auditados (16,7% de 30), sobre a **v1**, em paralelo ao R1 (ficha 9.3, item 6; 12.4.8). Vereditos: 4 CONFORMES (D2-R51, D2-R54, D2-R65 e D2-R72), 1 AJUSTE (texto) (D2-R73), 0 NÃO CONFORME. O AJ não muda gabarito, ponto de julgamento, mecanismo, formato, moldura S/N, aderência, abertura, campo Troca nem [TS]. Sem GATE pela regra 6.

**Rito:** cumprido como a ficha 9.3, item 6, e a 12.4.8 mandam. A auditoria correu sobre a v1, antes do R1 gravado (saida/gcb/QA_DA_reforco_leva6_R1_* ausente em disco na hora da leitura). O texto da seção 5 é, portanto, **AJ de v1**, e não errata pós-R2 (a seção 7.6 não se aplica). Se o R1 pedir o mesmo texto, ele é aplicado uma vez e registrado como um só ajuste, com as duas origens (ficha 11.3). É 1 linha de AJ, em 1 item.

**Classificação:** os vereditos, a atribuição de mecanismo, a leitura de pista e o juízo de risco de "mais de uma interpretação" são julgamento deste agente (gbq-estilo) e exigem revisão da GBQ (ver o AVISO no fim).

## 0. Objeto, entradas e método

| objeto | SHA-256 |
|---|---|
| saida/gcb/DA_reforco_leva6_v1.md (objeto; 30 itens; QA PENDENTE) | 8ba2bb6378f196a7811a43cd47927447b674c9f40a51421f94a97c073bd3bf87 (conferido em disco; igual ao do despacho) |
| saida/gcb/DA_reforco_ficha_2026-10-20.md (amostra: 12.4.8; rito: 5, 7.4, 7.6, 9.3, 10.2, 11.2, 11.3, 12.2) | 8a86e4bdb816824cc3e7e0c63991c5bd012021a2b02cbdf160416cce66c0eb6c (conferido em disco; igual ao do despacho) |
| regras/estilo_banca.md (catálogo em disco: **v1.1.3**, linha 2) | 9f9237f5f9828b77d5ab805849a7a14af13fb28fcc1c985fe462ec1027684caf |
| saida/banco/estilo_DA_reforco_leva5.md (modelo de forma e critérios) | lido; não alterado |
| saida/gcb/normativo_cache/Lei_8112_1990_compilada_2026-10-20.txt (D2-R51, linha 662; D2-R54, linhas 630 e seguintes e 699; D2-R72, linhas 777, 790 e 791; D2-R73, linhas 649 a 660, 715 a 727 e 741 a 745) | 72f45d30dcf096207898d143ba551758e3ffac89e87d6dd2d42044fe65202efe (refeito em disco) |
| saida/gcb/normativo_cache/Lei_9784_1999_2026-10-20.txt (D2-R65, linhas 13, 144 e 148) | f9452916c03521a8435caae49c8feb690ae2b02086424b641204374f38f9ae19 (refeito em disco) |
| saida/gcb/DA_reforco_leva4_v2.md e DA_reforco_leva5_v2.md (só para as contagens acumuladas do D2 na seção 4) | lidos; não alterados |

**Script:** python3 -I, somente leitura, no scratchpad da sessão, sobre o arquivo da leva (seções 1 e 2). Ele extrai enunciados, gabaritos e moldura e conta:
- abertura × gabarito;
- a fórmula "Nessa situação, nos termos d…";
- o fecho "é correto afirmar que";
- absolutos por gabarito (sempre, somente, apenas, só, exclusivamente, qualquer, todo/toda, nenhum/nenhuma, ninguém, vedado/vedada);
- "pois";
- moldura × fórmula × gabarito (leva 6 e, no D2, levas 4 e 5);
- extensão;
- ocorrências do "antes" e do "depois" da seção 5.

As contagens de folha fechada e de moldura acumulada não foram refeitas. Vêm da seção 4 do arquivo da leva e são matéria do R1.

**Conferência por script (leva 6, 30 itens; 14 C / 16 E):**
- "Considere que": 7 C / 5 E; declarativos: 7 C / 11 E.
- Fórmula "Nessa situação, nos termos d…": 2 C / 4 E, em 6 dos 12 CQ (D2-R54, R60, R62, R65, R74, R77; 2 por folha), no limite da ficha 12.2, item 3.
- Fecho "é correto afirmar que": 0 nos enunciados.
- Absolutos nos enunciados: C 3 (D2-R64 "somente", D2-R70 "sempre", D2-R71 "sempre"); E 2 (D2-R69 "qualquer", D2-R72 "qualquer"; os dois literais e fora da troca). Nenhum E com absoluto inserido.
- "pois": 1 C (D2-R78) / 0 E.
- Moldura: 0 C / 4 E (D2-R54, R58, R65, R77); 3 dos 4 com a fórmula.
- Extensão: C de 23 a 42 palavras (média 33,1); E de 21 a 52 (média 34,2).

Conferem com as seções 0 e 4.6 do arquivo e com a ficha 12.4.6.

**Critérios de estilo:** os mesmos das levas 1 a 5 (estilo da leva 5, seção 0):
- comando C/E;
- uma afirmação, com um só ponto de erro;
- troca real e única;
- nenhuma pista de forma;
- extensão dentro da faixa da base (estilo_banca v1.1.3, seção 4: C de 8 a 65 palavras; E de 19 a 62);
- registro formal;
- termo absoluto só quando for letra da fonte ou a própria troca;
- moldura que não decide o gabarito (R1 da T-122);
- risco de "mais de uma interpretação" (estilo_banca, seção 5.3);
- L3-1 a L3-5 (ficha 9.3), L4-1 a L4-4 e itens 5 e 6 da ficha 10.2, L5-1 e L5-2 (ficha 11.2), L6-1 e L6-2 (ficha 12.2).

Vereditos:
- **NÃO CONFORME:** dois pontos de erro, pista que entrega o gabarito, E decidido pela moldura, ou gabarito que só se sustenta com escolha da produção.
- **AJUSTE (texto):** defeito sanável por substituição exata, sem mudar gabarito, ponto, mecanismo nem a natureza da troca.

## 1. Amostra

Fixada pela ficha, seção 12.4.8, antes da produção. Sem sorteio.

| id | folha | lote | gab. | formato | moldura | aderência | o que cobre |
|---|---|---|---|---|---|---|---|
| D2-R51 | 4.2 | D2 | C | DEF | N | direta | C da exigência (b); Lei 8.112, art. 135 |
| D2-R54 | 4.2 | D2 | E [TS] | APL | S (órgão/servidor do Poder Legislativo da União) | direta | E com moldura; troca de número para mais (teto); Lei 8.112, art. 130, § 1º |
| D2-R65 | 4.4 | D2 | E [TS] | APL | S (idem; cena "função administrativa") | direta | E com moldura na 4.4; troca de número para mais (prazo máximo); Lei 9.784, art. 44 |
| D2-R72 | 4.3 | D2 | E | DEF | N | direta | único E sem [TS]; erro por contraste com a Lei 8.112, art. 182, parágrafo único; absoluto literal fora da troca (L6-2) |
| D2-R73 | 4.3 | D2 | E [TS] | NUM | N | direta | troca de número para menos, afirmada como valor da regra (L6-1); Lei 8.112, art. 161, § 1º |

**Composição exigida (ficha, seção 5): CONFERE.**
- Tamanho: ⌈10% de 30⌉ = 3; foram designados 5.
- Ao menos 1 E com moldura: D2-R54 (4.2) e D2-R65 (4.4).
- Todos os lotes da leva: só há o D2, e os 5 itens são dele. As três folhas estão cobertas.
- Ao menos 1 C: D2-R51.
- Parcial: a leva tem 0 parciais (30 diretos), e a exigência não se aplica.

## 2. Vereditos por item

Palavras: só o enunciado, sem o comando.

| id | gab. | mecanismo | trecho decisivo | palavras | veredito | motivo |
|---|---|---|---|---|---|---|
| D2-R51 | C | C2 (reprodução próxima do texto normativo; declarado e confirmado) | "a destituição de cargo em comissão exercido por não ocupante de cargo efetivo será aplicada nos casos de infração sujeita às penalidades de suspensão e de demissão" | 32 | **CONFORME** | **Reprodução literal da Lei 8.112, art. 135, caput** (cópia, linha 662), com a abertura "Segundo a Lei nº 8.112/1990". O elemento "exercido por não ocupante de cargo efetivo" fica no enunciado, como a exigência (b) pede.<br><br>Um só ponto. Não traz o parágrafo único (exoneração convertida em destituição), que é o par do D2-R76 (nota (bk)). Sem absoluto, sem "mas não" e sem qualificador. Declarativo, sem moldura. Extensão dentro da faixa de C. Registro formal.<br><br>**Discriminação:** a tentação real é achar que a destituição cabe só nos casos de demissão, e não também nos de suspensão. Quem conhece a letra marca C. A justificativa, linha 2, fala em outra tentação (estender a destituição a quem ocupa cargo efetivo), que o enunciado não chega a testar, porque traz o elemento. A linha continua verdadeira, e a escolha é da gcb-cqfp. |
| D2-R54 | E [TS] | E3 (altera o prazo: troca de número; declarado e confirmado) | "ele será punido com suspensão de até trinta dias" | 52 | **CONFORME** | **Uma troca, de número, na posição da letra.** A Lei 8.112, art. 130, § 1º, diz "Será punido com suspensão de até 15 (quinze) dias o servidor que, injustificadamente, recusar-se a ser submetido a inspeção médica determinada pela autoridade competente, cessando os efeitos da penalidade uma vez cumprida a determinação", e o item põe trinta. O resto do enunciado é a letra.<br><br>**Sentido da troca (L6-1), a favor.** A letra é um teto ("até"), e a troca para cima dá à Administração poder de punir que a lei não dá: uma suspensão de vinte dias caberia no item e não cabe na lei. A troca para menos ("até dez dias") ficaria compatível com a leitura de permissão. O número trinta não é o teto de outra conduta do art. 130. Fica entre o teto do § 1º (15) e o do caput (90), e isso pega quem só conhece o caput. É a tentação declarada na justificativa, linha 2, e dá discriminação sem entregar o gabarito.<br><br>**Vizinho com lastro, sem segunda leitura:** "suspensão de até 30 (trinta) dias" é também a letra do art. 145, II (cópia, linha 699). Lá, porém, é o limite do que a sindicância pode aplicar, e não a pena da recusa à inspeção. É outra figura: a pena da conduta é a do § 1º, em qualquer rito. Funciona como o vizinho do D2-R65, e a nota (bn) já separa o item do D2-63 (art. 145, II).<br><br>**A moldura não decide.** O cenário só põe o servidor em órgão do Poder Legislativo da União, e o fecho cita a Lei 8.112. Não há fecho de acerto nem norma interna. A conduta inteira fica no cenário, e o fecho troca o número sem negar a consequência (10.2, item 5).<br><br>Fórmula "Nessa situação, nos termos d…": é uma das 2 da 4.2, dentro do limite (ver a seção 4 sobre moldura × fórmula). Cena distinta da do D2-R58 (L3-3; prefixo comum abaixo de 40 caracteres, dado do arquivo). Extensão dentro da faixa de E. Registro formal. |
| D2-R65 | E [TS] | E3 (altera o prazo: troca de número; declarado e confirmado) | "o interessado terá o direito de manifestar-se no prazo máximo de quinze dias" | 51 | **CONFORME** | **Uma troca, de número.** A Lei 9.784, art. 44, diz "Encerrada a instrução, o interessado terá o direito de manifestar-se no prazo máximo de dez dias, salvo se outro prazo for legalmente fixado" (cópia, linha 148), e o item põe quinze. A ressalva "salvo se outro prazo for legalmente fixado" é letra e não salva o item, porque o item afirma quinze como regra geral.<br><br>**Sentido da troca (L6-1), a favor.** O número é afirmado como direito com prazo máximo. Um prazo maior dá ao interessado mais do que a lei dá e contradiz a letra. Um prazo menor ficaria dentro do direito.<br><br>**Conceito vizinho com lastro:** "prazo máximo de quinze dias" é a letra do art. 42 da mesma lei, sobre o parecer de órgão consultivo (cópia, linha 144). É outra figura (outro ato, outro sujeito), e por isso não cria segunda leitura. Dá discriminação, como o vizinho do D2-R30 na leva 5. A justificativa, linha 2, aponta como tentação o prazo de trinta dias para decidir (art. 49). A confusão mais provável é com o art. 42, que a produção já registrou na nota de simulado D2-R65 × D1-54 (bloco 5). A linha continua verdadeira, e a escolha é da gcb-cqfp.<br><br>**A moldura não decide.** "no desempenho de função administrativa" é a condição do art. 1º, § 1º (cópia, linha 13), e bloqueia a leitura "Legislativo → a lei não se aplica → E". Não há norma interna, regimento nem prática real da Câmara.<br><br>Fórmula: é uma das 2 da 4.4, dentro do limite. Cena distinta da do D2-74, do D2-R47 e do D2-R50 (L3-3; prefixos de 13 e 14 caracteres, dado do arquivo). Extensão dentro da faixa de E. Registro formal.<br><br>**Observação (cena-tipo):** no D2, a cena "órgão do Poder Legislativo da União no desempenho de função administrativa" fica com 1 C (D2-74) e 3 E (D2-R47, D2-R50, D2-R65). A nota (bt) já separa os quatro no simulado. |
| D2-R72 | E | E3 (troca a hipótese da revisão: "a inocência do punido ou a inadequação da penalidade" → "o agravamento da penalidade"; declarado; fronteira com E2, inversão de polaridade) | "suscetíveis de justificar o agravamento da penalidade aplicada" | 35 | **CONFORME** | **O E está na letra.** A Lei 8.112, art. 174, caput, admite a revisão quando houver fatos novos ou circunstâncias "suscetíveis de justificar a inocência do punido ou a inadequação da penalidade aplicada" (cópia, linha 777). O art. 182, parágrafo único, diz "Da revisão do processo não poderá resultar agravamento de penalidade" (cópia, linha 791). O item põe o agravamento como fundamento da revisão.<br><br>**Uma só leitura.** Seria possível alegar que "inadequação da penalidade" inclui a pena branda demais. O item não usa "inadequação", e o art. 182, parágrafo único, fecha essa leitura com letra expressa. O gabarito não depende de escolha da produção.<br><br>**Sem [TS], defensável no estilo.** A troca não é sutil: "agravamento" diz o oposto do sentido protetivo do caput, e o erro fica visível para quem conhece o art. 182, parágrafo único. Pela forma, o mecanismo fica na fronteira E3/E2. estilo_banca 5.1 manda marcar [TS] "em E1 e E2 sempre", mas o mecanismo declarado é E3, e a classificação E3 (troca da condição da norma, 3.3) é defensável. Se a gcb-cqfp reclassificar para E2 e pedir [TS], o teste de [TS] da 4.3 reprova (ficha 12.5, item 2), e a decisão é dela e da GCB.<br><br>**L6-2 cumprida:** "a qualquer tempo" é letra e não é a troca, e o "qualquer" fica num E. "a pedido ou de ofício" também é letra. Sem "mas não", ", e não" ou qualificador. Declarativo, sem moldura. Extensão dentro da faixa de E. Registro formal.<br><br>**Observação (discriminação):** a vedação de agravamento é conhecida (também está na Lei 9.784, art. 65, parágrafo único, do D2-71). O item discrimina pouco entre candidatas preparadas, mas não tem defeito. A nota (bv) separa o D2-R72 do D2-R76, do D2-66 e do D2-71. |
| D2-R73 | E [TS] | E3 (altera o prazo: troca de número; declarado e confirmado) | "tem prazo de cinco dias para apresentar defesa escrita" | 30 | **AJUSTE (texto)** | **Gabarito, ponto e troca corretos.** A Lei 8.112, art. 161, § 1º, diz "O indiciado será citado por mandado expedido pelo presidente da comissão para apresentar defesa escrita, no prazo de 10 (dez) dias, assegurando-se-lhe vista do processo na repartição" (cópia, linha 742), e o item põe cinco. É uma troca só.<br><br>**L6-1 cumprida.** O número é afirmado como valor da regra ("tem prazo de cinco dias"), e a troca para menos contradiz a letra.<br><br>**Defeito (risco de "mais de uma interpretação", estilo_banca 5.3):** a mesma lei dá prazo de **cinco dias** para a defesa escrita do indiciado no procedimento sumário: "promoverá a citação pessoal do servidor indiciado, ou por intermédio de sua chefia imediata, para, no prazo de cinco dias, apresentar defesa escrita, assegurando-se-lhe vista do processo na repartição" (art. 133, § 2º; cópia, linha 654). O art. 140 manda usar esse rito no abandono de cargo e na inassiduidade habitual, que são matéria da própria leva (D2-R52, D2-R56). A segunda metade do item ("cinco dias para apresentar defesa escrita, assegurando-se-lhe vista do processo na repartição") é, palavra por palavra, a letra do art. 133, § 2º.<br><br>O que ancora o item no art. 161 é só "citado por mandado expedido pelo presidente da comissão". No sumário, a citação é "pessoal … ou por intermédio de sua chefia imediata", mas o art. 133, § 8º, manda aplicar ao sumário, de forma subsidiária, o Título V, onde está o art. 161. A âncora reduz o risco, mas não o fecha. Um recurso pode sustentar C ("segundo a Lei 8.112, o indiciado tem cinco dias para a defesa escrita"). O gabarito se sustenta pela letra do art. 161, § 1º, e o defeito é sanável por texto. Por isso o veredito é AJUSTE, e não NÃO CONFORME.<br><br>**Correção:** o AJ-L6-E1 nomeia a fase pelo nome que só o rito ordinário tem: "inquérito administrativo" (art. 151, II; seção "Do Inquérito", onde está o art. 161). No sumário, a fase equivalente é a "instrução sumária" (art. 133, II). O acréscimo não diz qual é o prazo, não cita o sumário e não cria contraste ("e não …"). Por isso não entrega o gabarito, e o "cinco" continua sendo um vizinho que discrimina, como no D2-R65. O resultado tem 38 palavras. Ficam iguais: ponto, gabarito, mecanismo, formato NUM, moldura N, aderência, abertura DC, campo Troca ("no prazo de 10 (dez) dias → tem prazo de cinco dias") e [TS]. As linhas 1 e 2 da justificativa continuam verdadeiras. |

**Taxas:**
- NÃO CONFORME: 0/5.
- AJUSTE (texto): 1/5 (D2-R73), sem mudança de gabarito.
- Itens decididos pela moldura: 0. Nos dois itens com moldura (D2-R54 e D2-R65), o E está na letra.

## 3. Conferência de L3-1 a L3-5 (ficha 9.3), L4-1 a L4-4, itens 5 e 6 (ficha 10.2), L5-1 e L5-2 (ficha 11.2), L6-1 e L6-2 (ficha 12.2) nos 5 itens

| regra | D2-R51 (C) | D2-R54 (E) | D2-R65 (E) | D2-R72 (E) | D2-R73 (E) |
|---|---|---|---|---|---|
| L3-1 (abertura por folha fechada) | DC C na 4.2; a 4.2 fechada fica com DC 5 C / 7 E: CONFERE | CQ E na 4.2; a 4.2 fechada fica com CQ 5 C / 3 E: CONFERE | CQ E na 4.4; a 4.4 fechada fica com CQ 5 C / 2 E: CONFERE | DC E na 4.3; a 4.3 fechada fica com DC 6 C / 7 E: CONFERE | DC E na 4.3: idem: CONFERE |
| L3-2 (absoluto inserido pela troca) | não se aplica | sem absoluto: não se aplica | sem absoluto: não se aplica | "qualquer" é letra, não troca: não se aplica | sem absoluto: não se aplica |
| L3-3 (cenário gêmeo) | declarativo: não se aplica | cena distinta da do D2-R58 e da do D2-R53 e do D2-R60: CONFERE | cena distinta da do D2-74, do D2-R47 e do D2-R50: CONFERE | declarativo: não se aplica | declarativo: não se aplica |
| L3-4 ("mas não" / ", e não") | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE; o AJ não acrescenta contraste |
| L3-5 (qualificador minimizador) | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE |
| L4-1 (fecho "é correto afirmar que" fora do D4) | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE. Na leva, 0 (script) |
| L4-2 (abertura da 6.2) | não se aplica | não se aplica | não se aplica | não se aplica | não se aplica |
| L4-3 (referente de rol, E6) | C: não se aplica | não é E6 | não é E6 | não é E6 | não é E6 |
| L4-4 (condição inventada sobre hipótese autônoma) | C: não se aplica | E3 de número: não se aplica | E3 de número: não se aplica | troca a hipótese da revisão por outra, sem condicionar uma hipótese autônoma a outra: não se aplica | E3 de número: não se aplica |
| 10.2, item 5 (hipótese inteira negada no fecho) | C: não se aplica | o fecho troca o número sem negar: CONFERE | o fecho troca o número sem negar: CONFERE | sem "sem" nem "não": CONFERE | sem "sem" nem "não": CONFERE |
| 10.2, item 6 (SUJ E com ator plausível) | não é SUJ | não é SUJ | não é SUJ | não é SUJ | não é SUJ |
| L5-1 (extensão) | 32, dentro de 8 a 65 (C): CONFERE | 52, dentro de 19 a 62: CONFERE | 51: CONFERE | 35: CONFERE | 30 (38 com o AJ): CONFERE |
| L5-2 (absoluto da letra retirado de E) | não se aplica | a letra não tem absoluto: não se aplica | não se aplica | não se aplica | não se aplica |
| L6-1 (sentido da troca de número) | não se aplica | para mais, teto: CONFERE | para mais, prazo máximo: CONFERE | não é troca de número | para menos, afirmado como valor da regra: CONFERE (ver o defeito na seção 2) |
| L6-2 (absoluto literal que não é a troca) | não se aplica | não se aplica | não se aplica | "a qualquer tempo" fica: CONFERE | não se aplica |

As conferências de folha fechada vêm da seção 4.6 do arquivo da leva e não foram refeitas aqui. As de leva foram refeitas (seção 0).

## 4. Leitura fora da amostra (sem veredito, fora da taxa)

- **Valor da troca de número igual ao da mesma figura em outro rito (indício; n = 1).** É o defeito do D2-R73 (seção 2). Nas outras quatro trocas de número da leva, o valor posto não é o da mesma figura em outra regra da lei:
  - D2-R52: vinte dias. Na Lei 8.112, é, entre outros, o prazo comum de defesa com dois ou mais indiciados (art. 161, § 2º), outra figura.
  - D2-R54: trinta dias. Na Lei 8.112, é, entre outros, o teto da suspensão que a sindicância pode aplicar (art. 145, II) e o prazo de conclusão do sumário (art. 133, § 7º). São outras figuras (seção 2).
  - D2-R65: quinze dias. É o prazo do parecer (Lei 9.784, art. 42), outra figura.
  - D2-R69: cinquenta e cinco anos. Não ocorre na Lei 9.784.

  A troca para menos, pedida pela L6-1, aumenta esse risco nas normas de processo, onde os ritos abreviados têm prazos menores. O texto da recomendação está na seção 6, L7-1.
- **Moldura e fórmula (indício; n = 8, só no D2).** No D2, nas levas 4 a 6, os itens com moldura e a fórmula "Nessa situação, nos termos d…" ficam com 0 C / 8 E:
  - leva 4: D2-R03;
  - leva 5: D2-R32, R39, R41, R47;
  - leva 6: D2-R54, R65, R77.

  A fórmula sem moldura fica com 7 C / 1 E:
  - leva 4: D2-R08, R19;
  - leva 5: D2-R24, R31, R42;
  - leva 6: D2-R60, R62 C e D2-R74 E.

  A fórmula, sozinha, está equilibrada (8 C / 9 E nas três levas). A combinação reproduz o desenho da cota, em que o item com moldura é de preferência E (ficha, regra 10), e não decide o gabarito. Ainda assim, cria um atalho ("órgão do Legislativo + 'Nessa situação, nos termos d…' → E") que acertaria 8 de 8 no reforço do D2. O D2 fecha na leva 6, e a leitura vale para os lotes seguintes com moldura (D3 na leva 7; D4 nas levas 8 e 9; D5 nas levas 10 e 11). O texto está na seção 6, L7-2.
- **Restritivos literais por marcador (indício).** No D2, levas 4 a 6 (script):
  - "sempre": 3 C / 0 E (D2-R15, R70, R71);
  - "somente": 3 C / 0 E (D2-R25, R36, R64);
  - "qualquer": 1 C / 3 E (D2-R31 C; D2-R32, R69, R72 E).

  A L6-2 foi cumprida pelo "qualquer". A regra ingênua "'sempre' ou 'somente' de letra → C", porém, acerta 6 de 6, e a base tem E com "sempre" (BQ-0052; estilo_banca 4). O texto está na seção 6, L7-3.
- **Sentido das trocas de número:** 3 para menos (D2-R52, R69, R73) e 2 para mais (D2-R54, R65), como a ficha 12.2, item 1, planejou (dado do arquivo; conferido nos três itens da amostra). O atalho "número mais generoso → E", registrado na leva 5, não se repete na leva 6.
- **"pois":** 1 C (D2-R78) / 0 E, como estilo_banca 5.1 recomenda ("escreva C com 'pois'").

## 5. Texto exato (AJ de v1; segue com os AJ do R1 para a v2 e é conferido no R2)

Formato da ficha, seção 4.3. O "antes" ocorre exatamente 1 vez em saida/gcb/DA_reforco_leva6_v1.md, e o "depois", 0 vez, conferido por script. A expressão "inquérito administrativo" ocorre 0 vez no arquivo.

`AJ-L6-E1 | D2-R73 | enunciado (seção 1) | substituir: «Segundo a Lei nº 8.112/1990, o indiciado, citado por mandado» | por: «Segundo a Lei nº 8.112/1990, na fase de inquérito administrativo do processo disciplinar, o indiciado, citado por mandado»`

**Efeito:**
- Ficam inalterados: gabarito (E), ponto (Lei 8.112, art. 161, § 1º), mecanismo (E3), formato (NUM), moldura (N), aderência (direta), abertura (DC), campo Troca, [TS] e justificativa (linhas 1 e 2).
- O item vai de 30 para 38 palavras.
- Nenhum outro campo do bloco precisa de harmonização. A Base pode ficar como está, porque o trecho citado é o do art. 161, § 1º.

**Contagens a refazer na v2 (por script, seção 4.6 do arquivo):** só a extensão do D2-R73 (lista de palavras por item; E da leva continua de 21 a 52 palavras). Abertura, fecho, fórmula, absolutos, moldura, L3-2, L6-1 e L6-2 ficam iguais.

**Interação com o R1:** se o R1 mudar o número do D2-R73 para um valor que não é o de outro rito, o defeito some, e vale o texto do R1. Se o R1 mudar a abertura do item, o "antes" deixa de ocorrer. Nesse caso, a gcb-cpp aplica o mesmo acréscimo, depois de "Segundo a Lei nº 8.112/1990,", só se o R1 o tiver acolhido. Se não tiver, a GCB registra na reconciliação. Se o R1 pedir este mesmo texto, é um só ajuste, com as duas origens (ficha 11.3).

**O que o R2 confere:**
1. O "antes" com 1 ocorrência na v1 e o "depois" aplicado literalmente na v2.
2. Nenhum outro campo do bloco muda.
3. Lido inteiro, o enunciado resultante mantém o E pela letra do art. 161, § 1º ("no prazo de 10 (dez) dias"; cópia, linha 742), fica fora da hipótese do art. 133, § 2º (fase de "instrução sumária", art. 133, II), e não cria pista.

**Se a gcb-cqfp recusar o AJ:** o item segue como está na v1, e a GCB registra o risco de recurso na reconciliação. O defeito é de nitidez, não de gabarito.

## 6. Recomendações para as próximas levas

Texto exato para a gcb-gerencia incluir na ficha da leva 7 ou nas seguintes, se aceitar. Nenhuma tem efeito sobre os 30 itens da leva 6 além do AJ da seção 5.

- **L7-1 (valor da troca de número igual ao da mesma figura em outro rito):** "Em item E cuja troca é um número, o valor posto pelo item não é o valor que a mesma norma dá à mesma figura (mesmo ato, mesmo sujeito) em outro rito ou regime. Exemplo: o prazo de defesa escrita do indiciado é de dez dias no inquérito (Lei 8.112, art. 161, § 1º) e de cinco no procedimento sumário (art. 133, § 2º). Se a troca usar esse valor, o enunciado nomeia o rito da letra por um elemento que só ele tem ('na fase de inquérito administrativo'; D2-R73, AJ-L6-E1). Valor igual ao de outra figura da mesma lei é admitido como conceito vizinho (D2-R65: quinze dias, art. 42). A seção 4 do arquivo da leva lista, por script, para cada troca de número, as outras ocorrências do valor posto na cópia da norma e a figura a que cada uma se refere."
- **L7-2 (moldura e fórmula):** "Nos lotes em que o item com moldura é de preferência E, a fórmula 'Nessa situação, nos termos d…' não fica concentrada nos itens com moldura. Em cada leva, no máximo metade dos E com moldura usa a fórmula, e os demais citam a norma no cenário ou de outro modo ('segundo …', 'conforme …', 'a Lei … prevê'). A seção 4 do arquivo da leva conta moldura × fórmula × gabarito, por lote e no acumulado (D2, levas 4 a 6: moldura com fórmula 0 C / 8 E; fórmula sem moldura 7 C / 1 E)."
- **L7-3 (restritivo literal em E, por marcador):** "A contagem de absolutos da seção 4 do arquivo da leva sai por marcador, e não só por classe. Quando um restritivo literal ('somente', 'sempre') aparecer só em C no lote acumulado, a leva traz, se a fonte permitir, ao menos um E em que esse restritivo é letra da fonte e não é o elemento trocado (L6-2). D2, levas 4 a 6: 'sempre' 3 C / 0 E; 'somente' 3 C / 0 E; 'qualquer' 1 C / 3 E."

## 7. Registros

1. **Rito:** auditoria sobre a v1, em paralelo ao R1, como a ficha 9.3, item 6, e a 12.4.8 determinam. O AJ segue para a v2 com os do R1 e é conferido no R2. Nenhuma errata pós-R2 (seção 7.6) é proposta.
2. **Versão do catálogo:** o despacho cita "regras/estilo_banca.md (versão em disco)". O arquivo em disco é a **v1.1.3** (linha 2; SHA-256 na seção 0), a mesma das auditorias das levas 1 a 5. Os mecanismos citados (C2, E1, E2, E3, E6) e as seções 3.2, 3.3, 3.8, 3.13, 4, 5.1 e 5.3 são os da v1.1.3. Nada foi alterado no catálogo.
3. **Nome do arquivo:** o da ficha 12.4.8 e 7.5 (saida/banco/estilo_DA_reforco_leva6.md).
4. **Fidelidade às bases:** só se leram as linhas das bases dos 5 itens, para confirmar o trecho decisivo:
   - Lei 8.112, arts. 130, 133 (caput, incisos e §§ 2º, 7º e 8º), 135, 140, 145, 151, 155, 161, 174 e 182;
   - Lei 9.784, arts. 1º, § 1º, 42 e 44.

   Os arts. 133, 140, 145, 151 e 155 da Lei 8.112 e o art. 42 da Lei 9.784 são citados só como razão de veredito, de observação ou do texto do AJ, e não como base de item. Nenhum deles está na lista "Fora da leva 6" da ficha 12.4.2. A conferência das bases é matéria da gcb-cqfp.
5. **D2-R72 sem [TS]:** julgado como a ficha 12.4.4 o fixa. A fronteira E3/E2 está registrada, e a decisão sobre [TS] cabe à gcb-cqfp e à GCB (ficha 12.5, item 2).
6. **Escopo:** nada vai à plataforma nem à candidata. Nenhuma tarefa nova (D-COMPLEMENTOS). Nenhum gatilho em PARA_PRESIDENCIA.md. Nenhum NÃO CONFORME, e por isso nenhum GATE pela regra 6.

AVISO: os vereditos, a atribuição de mecanismo, a leitura de pista e o juízo de risco de "mais de uma interpretação" são julgamento deste agente (gbq-estilo) e exigem revisão da GBQ. As contagens de abertura, de fórmula, de fecho, de absolutos, de "pois", de moldura × fórmula, de extensão e de ocorrência dos trechos de AJ vêm de script sobre os arquivos gravados (python3 -I, somente leitura), com revisão manual dos 5 itens. As contagens de folha fechada e de moldura acumulada foram tomadas da seção 4 do arquivo da leva e da ficha, sem refazer. Com n pequeno (amostra de 5; recortes de 1 a 30 itens), nenhuma associação é regra, e nenhum marcador decide o gabarito. A tabela serve para corrigir vieses de redação, nunca para prever gabarito.

FIM DA AUDITORIA DE ESTILO — LEVA 06 — REFORÇO DA
