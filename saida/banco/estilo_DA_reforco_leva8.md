# estilo_DA_reforco_leva8.md — T-116 — 2026-10-22 — gerado por gbq-estilo

Auditoria de estilo Cebraspe da amostra da leva 8 do reforço de DA (D-REFORCO-2, regra 6; D-REFORCO-DA; ficha, seções 5, 7.4, 7.6, 9.3, 10.2, 11.2, 11.3, 12.2, 13.2, 14.2 e 14.4.8). Ciclo s16c6. Destino: gcb-cqfp (R1 da leva 8, em paralelo; os AJ de estilo seguem com os AJ do R1 para a v2) e gcb-gerencia (reconciliação da leva 8). Este agente audita e não produz. Nenhum outro arquivo foi alterado; regras/estilo_banca.md não foi tocado. Sem commit nem push.

**Resultado:** 5 itens auditados (16,7% de 30), sobre a **v1**, em paralelo ao R1 (ficha 9.3, item 6; 14.4.8). Vereditos: 3 CONFORMES (D4-R33, D4-R44 e D4-R51), 2 AJUSTE (texto) (D4-R35 e D4-R48), 0 NÃO CONFORME. Dois textos de AJ: AJ-L8-E1 (D4-R35) e AJ-L8-E2 (D4-R48), os dois na abertura da moldura. Sem GATE pela regra 6.

**Rito:** cumprido como a ficha 9.3, item 6, e a 14.4.8 mandam. A auditoria correu sobre a v1, antes do R1 gravado (saida/gcb/QA_DA_reforco_leva8_R1_* ausente em disco na hora da leitura). Os AJ-L8-E1 e AJ-L8-E2 seguem com os AJ do R1 para a v2 e são conferidos no R2. Se o R1 pedir o mesmo texto, ele é aplicado uma vez e registrado como um só ajuste, com as duas origens (11.3). A seção 7.6 (errata pós-R2) não se aplica. Os dois AJ mudam o início do enunciado, e por isso a seção 5 declara o efeito sobre o prefixo comum (14.2, item 1).

**Classificação:** os vereditos, a atribuição de mecanismo, a leitura de pista e o juízo de risco de "mais de uma interpretação" são julgamento deste agente (gbq-estilo) e exigem revisão da GBQ (ver o AVISO no fim).

## 0. Objeto, entradas e método

| objeto | SHA-256 |
|---|---|
| saida/gcb/DA_reforco_leva8_v1.md (objeto; 30 itens; QA PENDENTE) | 1b9903d5aa0c3f049a8aa361c2fda8c62b03b118272f6ef96df79907e50d8ecf (conferido em disco; igual ao do despacho) |
| saida/gcb/DA_reforco_ficha_2026-10-20.md (amostra: 14.4.8; rito: 5, 7.4, 7.6, 9.3, 10.2, 11.2, 11.3, 12.2, 13.2, 14.2; plano: 14.4.4 a 14.4.7; conferência do adendo: 14.6) | 539f22327fb4ec7914a3cae6f2ffe22cdc89c7f873f5ff9be6bb1ad242b0eac8 (conferido em disco; igual ao do despacho) |
| regras/estilo_banca.md (catálogo em disco: **v1.1.3**, linha 2) | 9f9237f5f9828b77d5ab805849a7a14af13fb28fcc1c985fe462ec1027684caf |
| saida/banco/estilo_DA_reforco_leva7.md (modelo de forma e critérios) | fd59ea46407b10cf89a9a3b644449f4014f966f95a205f65df23ae13ca1098e1 (lido; não alterado) |
| saida/gcb/D4_anexo_N_mapa_normativo.md (D4-R33: Lei 13.019, art. 2º, I, a, seção 4.3; D4-R35: Lei 11.079, art. 2º, caput, §§ 1º a 4º, seção 4.2) | 0d98c24969788d2baeb150535b6a7cd538ea856fb64d3d707bc53ede24e5a05f |
| saida/gcb/D4_anexo_N_adendo_2026-10-22.md (D4-R44: Lei 13.460, art. 23, caput e §§ 1º e 2º; D4-R48: art. 21; seção 4.4) | 44ad15bdb0b34d05be734bd1a45277d4ad98af16864acbe483a8d91fe9cdb17f |
| saida/gcb/normativo_cache/CasaCivil_GuiaPoliticaGovernanca_2018_2026-10-20.txt (D4-R51: G5, linhas 525 a 529; contexto nas linhas 515 a 561) | d9b00721b29610adbcea7f4d7b0e05090c2daac0120a9b558a615bd0f0aae0b9 |
| saida/pacote/pacote.json v1.13 (só enunciado e gabarito dos 79 canônicos do D4, para prefixo, abertura e moldura) | 82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240 |
| saida/gcb/DA_reforco_leva1_v2.md e DA_reforco_leva2_v2.md (só seções 1 e 2, itens do D4, para abertura e moldura no acumulado) | 2c431529a5440d4a2bf2bb617bc75d496949dff28a824e0215322d00d79a4f04; 5baec20d81eea47f50e79275375668284d58ff5649f85a06c37552cd0f161bbe |

A Lei 13.460 não tem cópia em normativo_cache/. Os trechos do D4-R44 e do D4-R48 foram lidos no adendo de 22/10/2026, seção 4.4. A contagem de "dois anos" na lei inteira (L7-1) vem da v1, seção 4.6, e da ficha 14.6 (página reaberta pela produção e pela GCB) e não foi refeita aqui. É limitação de método, sem bloqueio.

**Script:** python3 -I, somente leitura, no scratchpad da sessão (est8/), sobre as seções 1 e 2 do arquivo da leva, os canônicos do D4 no pacote.json e as seções 1 e 2 das levas 1 e 2. Ele conta:
- abertura × gabarito;
- fecho de acerto, fecho neutro e a fórmula "Nessa situação, nos termos d…";
- marcadores por gabarito: sempre, somente, apenas, só, exclusivamente, qualquer, único, "pois", "mesmo que", "prioritariamente", "não", "sem";
- aberturas de atribuição ("Nos termos d…", "Segundo …", "De acordo com …", "Conforme …");
- abertura dos itens com moldura, no D4 acumulado;
- fecho neutro × moldura, no D4 acumulado;
- extensão (palavras separadas por espaço, só o enunciado);
- prefixo comum entre enunciados, na leva e com os canônicos da folha (L3-3), antes e depois dos AJ.

As contagens de folha fechada, de K1 a K4, de sequência e de moldura acumulada de DA não foram refeitas: vêm da seção 4 do arquivo da leva e da ficha 14.4.6 e 14.6, e são matéria do R1.

**Conferência por script (leva 8, 30 itens; 14 C / 16 E):**
- "Considere que": 6 C / 4 E; declarativos: 8 C / 12 E.
- Fórmula "Nessa situação, nos termos d…": 1 C (D4-R40) / 0 E. Fecho neutro "Nessa situação, é correto afirmar que": 2 C (D4-R38, R56) / 2 E (D4-R42, R48). Fecho de acerto: 0 C / 2 E (D4-R35, R52).
- Itens com moldura: 0 C / 4 E (D4-R35, R42, R48, R52).
- Marcadores: "pois" 1 C (D4-R53) / 0 E; "sempre", "somente", "apenas", "prioritariamente" e "mesmo que": 0 / 0; "só" 0 C / 1 E (D4-R42, letra); "qualquer" 0 C / 1 E (D4-R44, letra); "único" 0 C / 1 E (D4-R35, letra); "exclusivamente" 0 C / 1 E (D4-R36, letra).
- Negação "não": 2 C (D4-R33, R54) / 2 E (D4-R29, R41); "sem": 2 C (D4-R33, R40) / 0 E.
- Extensão: C de 20 a 65 palavras (média 42,3); E de 26 a 58 (média 39,5).

Conferem com as seções 0, 4.2 e 4.6 do arquivo e com a ficha 14.4.6 e 14.6. Há uma exceção, de registro (seção 4 abaixo, item 1).

**Critérios de estilo:** os mesmos das levas 1 a 7 (estilo da leva 7, seção 0):
- comando C/E;
- uma afirmação, com um só ponto de erro;
- troca real e única;
- nenhuma pista de forma;
- extensão dentro da faixa da base (estilo_banca v1.1.3, seção 4: C de 8 a 65 palavras; E de 19 a 62);
- registro formal;
- termo absoluto só quando for letra da fonte ou a própria troca;
- moldura que não decide o gabarito (R1 da T-122);
- risco de "mais de uma interpretação" (estilo_banca, seção 5.3);
- as regras de forma da ficha: 7.4 (itens 1 a 5), L3-1 a L3-5 (9.3), L4-1 a L4-4 e os itens 5 e 6 da 10.2, L5-1 e L5-2 (11.2), L6-1 e L6-2 (12.2), L7-1 a L7-3 e o item 4 da 13.2, e os itens 1 e 2 da 14.2 (AJ de abertura e justificativa sem afirmação sem fonte).

Vereditos:
- **NÃO CONFORME:** dois pontos de erro, pista que entrega o gabarito, E decidido pela moldura, ou gabarito que só se sustenta com escolha da produção.
- **AJUSTE (texto):** defeito sanável por substituição exata, sem mudar gabarito, ponto, mecanismo nem a natureza da troca.

## 1. Amostra

Fixada pela ficha, seção 14.4.8, antes da produção. Sem sorteio.

| id | folha | lote | gab. | formato | moldura | aderência | o que cobre |
|---|---|---|---|---|---|---|---|
| D4-R33 | 8.2 | D4 | C | SIT | N | direta | C com "Considere que"; Lei 13.019, art. 2º, I, a |
| D4-R35 | 8.2 | D4 | E [TS] | APL | S (audiência pública de comissão da Câmara dos Deputados, expositor; fecho de acerto) | direta | E com moldura e fecho de acerto (K2); Lei 11.079, art. 2º, § 4º, III |
| D4-R44 | 8.3 | D4 | E [TS] | NUM | N | **parcial** (ficha 14.6) | única troca de número da leva (L6-1, L7-1); Lei 13.460, art. 23, § 1º |
| D4-R48 | 8.3 | D4 | E [TS] | APL | S (idem; fecho neutro) | direta | E com moldura e fecho neutro (7.4, item 1); Lei 13.460, art. 21 |
| D4-R51 | 9.1 | D4 | E [TS] | SUJ | N | direta | SUJ com organização citada pela fonte (10.2, item 6); Guia F2, G5 |

**Composição exigida (ficha, seção 5): CONFERE.**
- Tamanho: ⌈10% de 30⌉ = 3; foram designados 5.
- Ao menos 1 E com moldura: D4-R35 (8.2) e D4-R48 (8.3), 2 dos 4 da leva.
- Todos os lotes da leva: só há o D4, e os 5 itens são dele. As três folhas estão cobertas.
- Ao menos 1 C: D4-R33.
- Ao menos 1 parcial: D4-R44. A amostra foi designada na 14.4.8, quando o plano dava a leva inteira como direta. A ficha 14.6 fixou depois o D4-R44 como parcial (A8.3-07, indireta no mapa do adendo), e com isso a exigência fica coberta. A pertinência é da gcb-cqfp.

## 2. Vereditos por item

Palavras: só o enunciado, sem o comando.

| id | gab. | mecanismo | trecho decisivo | palavras | veredito | motivo |
|---|---|---|---|---|---|---|
| D4-R33 | C | C2 (reprodução próxima do texto normativo; declarado e confirmado), com traço de C6 (lista abreviada) | "não distribua, entre os seus sócios ou associados, […] resultados, sobras ou excedentes […], e os aplique integralmente na consecução do respectivo objeto social" | 63 | **CONFORME** | **Reprodução da letra.** A Lei 13.019, art. 2º, I, a, diz "entidade privada sem fins lucrativos que não distribua entre os seus sócios ou associados, conselheiros, diretores, empregados, doadores ou terceiros eventuais resultados, sobras, excedentes operacionais, brutos ou líquidos, dividendos, isenções de qualquer natureza, participações ou parcelas do seu patrimônio, auferidos mediante o exercício de suas atividades, e que os aplique integralmente na consecução do respectivo objeto social, de forma imediata ou por meio da constituição de fundo patrimonial ou fundo de reserva" (Anexo N do D4, 4.3). A cena reproduz o sujeito, o rol de destinatários e o dever de aplicação integral. O fecho conclui pelo enquadramento. Não há troca, e há um só ponto.<br><br>**Lista abreviada: sem segunda leitura que derrube o C.** A cena põe "excedentes" no lugar de "excedentes operacionais, brutos ou líquidos". Isso é um superconjunto: quem não distribui excedentes não distribui os operacionais. A cena omite "dividendos, isenções de qualquer natureza, participações ou parcelas do seu patrimônio" e a forma de aplicação ("de forma imediata ou por meio da constituição de fundo …"). Pela estilo_banca 3.12 (C6), "incompleto não é errado": o item não diz que esses são os únicos requisitos e não põe na cena nada que os contrarie, e "sem fins lucrativos" cobre o núcleo do que falta. O risco de recurso pela tese do "cenário incompleto" existe, mas é baixo. A justificativa, linha 2, nomeia essa tentação. A escolha entre a lista abreviada e a lista inteira é da gcb-cqfp (v1, bloco 5, dúvida (i)). A lista inteira levaria o item a cerca de 85 palavras, acima do teto de C (L5-1).<br><br>**Forma a favor do equilíbrio.** É um C com "Considere que", com "não" e com "sem" ("sem fins lucrativos"). Na leva, "não" fica em 2 C / 2 E e "sem" em 2 C / 0 E: o item ajuda a que a negação não vire marca de E (estilo_banca 3.13 e 4). O fecho "Nessa situação, essa entidade se enquadra, nos termos da Lei …" não é a fórmula "Nessa situação, nos termos d…" nem o fecho neutro. Extensão de 63 palavras, dentro da faixa de C (teto 65). Registro formal.<br><br>**Observação (discriminação):** a cena enumera os elementos da alínea e pergunta só pelo enquadramento, como o D3-R60 da leva 7. O item discrimina pouco entre candidatas preparadas, mas não tem defeito. O par com o D4-R36 (nota (de)) não lê um ao outro: o D4-R33 não fala de organização religiosa. |
| D4-R35 | E [TS] | E2 (inversão de polaridade: "É vedada" → "é admitida"; declarado e confirmado) | "é admitida a celebração de contrato de parceria público-privada que tenha como objeto único a execução de obra pública" | 48 | **AJUSTE (texto)** | **Uma troca, na letra.** A Lei 11.079, art. 2º, § 4º, diz "É vedada a celebração de contrato de parceria público-privada: […] III – que tenha como objeto único o fornecimento de mão-de-obra, o fornecimento e instalação de equipamentos ou a execução de obra pública" (Anexo N do D4, 4.2). A afirmação do expositor inverte a vedação, e o fecho de acerto a dá por correta. É um só ponto de erro.<br><br>**Uma só leitura.** O § 2º ("ainda que envolva execução de obra") e o § 1º ("concessão de serviços públicos ou de obras públicas") admitem obra como parte da PPP, e não como **objeto único**. O item mantém "objeto único", e o gabarito se sustenta pela letra do inciso III. "único" é letra da fonte e não é a troca (L6-2). A linha 2 da justificativa cita o § 1º com o seu lastro (14.2, item 2).<br><br>**A moldura não decide.** O expositor em audiência pública de comissão da Câmara dos Deputados só situa a afirmação. Não há norma interna, regimento nem prática real da Câmara. K2 passa de 7/7 a 7/9 (43,8%; pela detecção larga da GCB, 12/9, 57,1%), dentro da faixa da regra 11.<br><br>**Defeito (pista de forma na abertura da moldura).** Os 12 canônicos do D4 com moldura (todos C) e os 8 itens com moldura das levas 1 e 2 (2 C / 6 E) abrem com a forma da cota: "Considere que, em audiência pública de comissão da Câmara dos Deputados, um expositor …" (14 C / 6 E). Os 4 itens com moldura da leva 8, todos E, abrem com variantes: "Considere que um expositor, em audiência …" (D4-R35, R42), "Considere que um expositor, ouvido em audiência …" (D4-R52) e "Considere que, durante audiência …" (D4-R48). Com isso, a variante fica em 0 C / 4 E. Em cada folha fechada, o C com moldura usa a forma da cota (8.2: D4-14; 8.3: D4-19 e D4-26; 9.1: D4-41), e o E com moldura usa a variante. Como a leva entra em simulado misturada por folha com os canônicos (nota (w)), a forma da abertura separa C de E nas três folhas. O n é pequeno (4), e a variante não entrega o gabarito do item isolado, porque a troca está na letra. Mas é pista de forma sistemática e sanável por texto, sem mudar ponto, gabarito, mecanismo, troca, moldura nem fecho. Por isso o veredito é AJUSTE, e não NÃO CONFORME.<br><br>**Correção (AJ-L8-E1):** a abertura passa à forma da cota, com o verbo da regra 10 ("um expositor afirme"). "sustente" ocorre só neste item da leva. Ficam iguais: ponto, gabarito, mecanismo E2, formato APL, moldura S, fecho de acerto, aderência, abertura CQ, campo Troca, [TS] e as duas linhas da justificativa. O enunciado continua com 48 palavras. O efeito sobre o prefixo está na seção 5. |
| D4-R44 | E [TS] | E3 (altera o comando: troca de número na periodicidade; declarado e confirmado) | "por pesquisa de satisfação feita a cada dois anos" | 40 | **CONFORME** | **Uma troca, de número.** A Lei 13.460, art. 23, § 1º, diz "A avaliação será realizada por pesquisa de satisfação feita, no mínimo, a cada um ano, ou por qualquer outro meio que garanta significância estatística aos resultados" (adendo de 22/10/2026, 4.4). O item põe "a cada dois anos". O sujeito ("os órgãos e entidades públicos abrangidos pela lei") é o do caput do art. 23. É uma troca só.<br><br>**Sentido da troca (L6-1), a favor.** A letra é um piso de frequência ("no mínimo, a cada um ano"). Se o item mantivesse "no mínimo", uma leitura de "intervalo mínimo de um ano" deixaria "dois anos" compatível com a letra. O item tira o "no mínimo" e afirma o intervalo como valor da regra, e assim a troca contradiz a letra nas duas leituras. A leitura natural (pelo menos uma vez por ano) tem apoio no próprio adendo: o § 2º remete à "periodicidade a que se refere o § 1º".<br><br>**L7-1 cumprida (dado da v1 e da ficha 14.6, não refeito).** "dois anos" ocorre 0 vez na Lei 13.460. As outras periodicidades da lei (art. 3º, "periodicidade mínima anual", do quadro geral dos serviços; art. 14, II, "anualmente", do relatório das ouvidorias) são anuais e não dão o valor posto a outra figura.<br><br>**A alternativa não torna o E certo.** "ou por qualquer outro meio que garanta significância estatística aos resultados" é letra e não é a troca ("qualquer": absoluto literal mantido, L6-2). Uma tese de recurso diria que uma pesquisa bienal com significância estatística cabe no "outro meio". Mas o item afirma qual é a regra da pesquisa de satisfação, e a regra da lei é anual. O gabarito se sustenta pela letra. Risco baixo; registro, sem AJ.<br><br>Declarativo, sem moldura. A abertura "Segundo a Lei …" é a de 3 dos 4 declarativos com essa abertura na leva, todos E (seção 4, item 2). Isso é dado de lote, e não defeito deste item. Sem "mas não" e sem qualificador. Extensão dentro da faixa de E. Registro formal. A justificativa, linha 2, descreve a tentação pelo próprio item (14.2, item 2). Aderência parcial pela ficha 14.6: só vai a simulado diagnóstico (D-ADERENCIA). |
| D4-R48 | E [TS] | E2 (inversão de polaridade: "sem remuneração" → "remunerado"; declarado e confirmado) | "a participação do usuário no conselho é considerada serviço relevante e remunerado" | 44 | **AJUSTE (texto)** | **Uma troca, na letra.** A Lei 13.460, art. 21, diz "A participação do usuário no conselho será considerada serviço relevante e sem remuneração" (adendo de 22/10/2026, 4.4). O item mantém "serviço relevante" e inverte "sem remuneração". É um só ponto de erro, sem segunda leitura: o adendo não traz outro dispositivo sobre remuneração do conselheiro.<br><br>**Fecho neutro (7.4, item 1): CONFERE.** O D4 chega à leva com o fecho neutro em 2 C / 3 E (40,0%). O piso da regra estava atingido, e o E pode usar o fecho. Ao fim da leva, o fecho neutro fica em 4/5 (44,4%), dentro da faixa.<br><br>**A moldura não decide.** O expositor "trate dos conselhos de usuários"; a afirmação julgada é a do item ("é correto afirmar que, segundo a Lei …"), e não a do expositor. Não há norma interna nem prática real da Câmara. O par com o D4-R40 (nota (dj)) não lê um ao outro: o D4-R40 não fala de remuneração.<br><br>**Defeito (pista de forma na abertura da moldura):** o mesmo do D4-R35. "Considere que, durante audiência pública …" é variante que só ocorre em E com moldura no D4. Na 8.3 fechada, os dois C com moldura (D4-19, D4-26) usam a forma da cota, e os dois E (D4-R42, D4-R48) usam variantes. Sanável por texto, sem mudar ponto, gabarito, mecanismo, troca, moldura nem fecho: AJUSTE, e não NÃO CONFORME.<br><br>**Correção (AJ-L8-E2):** "durante audiência" passa a "em audiência", a forma da cota. Ficam iguais: ponto, gabarito, mecanismo E2, formato APL, moldura S, fecho neutro, aderência, abertura CQ, campo Troca, [TS] e as duas linhas da justificativa. O enunciado continua com 44 palavras. O efeito sobre o prefixo está na seção 5.<br><br>Sem absoluto, sem "mas não", sem qualificador e sem negação no fecho (10.2, item 5). Sem a fórmula "nos termos d…" (L7-2). Extensão dentro da faixa de E. Registro formal. A justificativa, linha 2, descreve a tentação pelo próprio item (14.2, item 2). |
| D4-R51 | E [TS] | E1 (troca de conceito vizinho: Banco Mundial → OCDE; declarado e confirmado) | "atribui à OCDE a descrição da governança como processo" | 30 | **CONFORME** | **Uma troca, de organização, na atribuição.** O Guia diz "O Banco Mundial, em seu Relatório de Desenvolvimento Mundial 2017: Governança e a Lei, descreve governança como sendo um 'processo por meio do qual atores estatais e não-estatais interagem para formular e implementar políticas dentro de um conjunto predefinido de regras formais e informais que moldam e são moldadas pelo poder' (Banco Mundial, 2017, tradução nossa)" (cópia, linhas 525 a 529). O item atribui a descrição à OCDE. O recorte da citação ("… para formular e implementar políticas") é subconjunto, sem mudar o sentido. É uma troca só.<br><br>**SUJ com ator plausível (10.2, item 6; 7.4, item 4): CONFERE.** A OCDE é citada pelo próprio Guia no mesmo capítulo (linha 558) e seria plausível à primeira leitura. O nome não nega a função.<br><br>**Uma só leitura, com uma observação.** O Guia aproxima as duas organizações: "as abordagens que o Banco Mundial e a OCDE têm sobre o tema" (linha 517); "A OCDE, na mesma linha, afirma que a boa governança é um meio para atingir um fim" (linha 558); o conceito "está alinhado aos entendimentos dessas duas organizações" (linhas 561 e 562). Uma tese de recurso diria que o Guia põe as duas na "mesma linha". Mas a descrição julgada vai entre aspas, com a referência "(Banco Mundial, 2017, tradução nossa)", e o que o Guia atribui à OCDE é outra frase (meio × fim). O gabarito se sustenta pela letra. Risco baixo; registro, sem AJ.<br><br>**Atribuição admitida.** Banco Mundial e OCDE são organizações citadas pelo Guia, nomeáveis como a ficha permite (14.4.2; seção 0.2, item 4). O item não nomeia autor de capítulo. "não-estatais", com hífen, segue a letra da fonte, como a ficha 14.6 manda. Em texto próprio, a ortografia atual seria "não estatais". Registro, sem AJ, porque a grafia foi fixada pela ficha.<br><br>Declarativo, sem moldura, sem absoluto, sem "mas não" e sem qualificador. "não" de "não-estatais" é letra e não é negação. Nenhum prefixo comum de 25 caracteres ou mais com outro item da leva ou com canônico da 9.1. Vizinho do D4-R52 no arquivo (posições 23 e 24; nota (dp)). O D4-R52 associa a OCDE à frase "meio × fim" e pode ajudar a descartar a OCDE no D4-R51; a nota (dp) já separa os dois em simulado. Extensão dentro da faixa de E. Registro formal. A justificativa, linha 2, cita G6 com o seu lastro (14.2, item 2). |

**Taxas:**
- NÃO CONFORME: 0/5.
- AJUSTE (texto): 2/5 (D4-R35, D4-R48).
- Itens decididos pela moldura: 0. Nos dois itens com moldura (D4-R35 e D4-R48), o E está na letra. O AJ trata só da forma da abertura.

## 3. Conferência das regras de forma da ficha nos 5 itens

Fonte das regras: ficha 7.4; L3-1 a L3-5 (9.3); L4-1 a L4-4 e itens 5 e 6 (10.2); L5-1 e L5-2 (11.2); L6-1 e L6-2 (12.2); L7-1 a L7-3 e item 4 (13.2); itens 1 e 2 (14.2).

| regra | D4-R33 (C) | D4-R35 (E) | D4-R44 (E) | D4-R48 (E) | D4-R51 (E) |
|---|---|---|---|---|---|
| 7.4.1 (fecho neutro do D4) | não usa | fecho de acerto: não se aplica | declarativo: não se aplica | E com fecho neutro, partida 2/3 (40%): CONFERE | não se aplica |
| 7.4.2 e L3-1 (abertura por leva e por folha fechada) | CQ C; leva CQ 6 C / 4 E; 8.2 fechada CQ 5 C / 1 E: CONFERE | CQ E; idem: CONFERE | DC E; leva DC 8 C / 12 E; 8.3 fechada DC 5 C / 6 E: CONFERE | CQ E; 8.3 fechada CQ 5 C / 4 E: CONFERE | DC E; 9.1 fechada DC 5 C / 8 E: CONFERE |
| 7.4.3 e 12.2, item 3 (fórmula) | sem a fórmula | sem a fórmula | sem a fórmula | sem a fórmula | sem a fórmula |
| 7.4.4 e 10.2, item 6 (SUJ) | não é SUJ | não é SUJ | não é SUJ | não é SUJ | OCDE citada pela fonte, plausível: CONFERE |
| 7.4.5 e 10.2, item 5 (negação frontal) | C: não se aplica | cena = afirmação do expositor, sem negação: CONFERE | sem cena: não se aplica | fecho sem "sem" nem "não": CONFERE | sem cena: não se aplica |
| regra 11 (K1, K2, K4) | K4 31/22 (58,5%): CONFERE | K1 14/10; K2 7/9: CONFERE | não se aplica | K1 14/10: CONFERE | não se aplica |
| pista de forma (critério de estilo) | sem pista | **abertura variante só em E com moldura: AJ-L8-E1** | sem pista própria (abertura "Segundo": dado de lote, seção 4) | **idem: AJ-L8-E2** | sem pista |
| L3-2 (absoluto inserido pela troca) | não se aplica | sem absoluto inserido | sem absoluto inserido | sem absoluto | sem absoluto |
| L3-3 (cenário gêmeo; prefixo ≥ 40 na folha) | maior prefixo 14 (D4-15): CONFERE | v1: 17 (D4-08); depois do AJ: 110 com D4-14, cena distinta: CONFERE (seção 5) | 30 com D4-R41: CONFERE | v1: 15; depois do AJ: 86 com D4-19 e D4-26, cena distinta: CONFERE (seção 5) | 0: CONFERE |
| L3-4 ("mas não" / ", e não") | ausente | ausente | ausente | ausente | ausente |
| L3-5 (qualificador minimizador) | ausente | ausente | ausente | ausente | ausente |
| L4-1 a L4-4 | não se aplicam (D4; sem E6; sem condição inventada) | idem | idem | idem | idem |
| L5-1 (extensão) | 63, dentro de 8 a 65: CONFERE | 48, dentro de 19 a 62: CONFERE | 40: CONFERE | 44: CONFERE | 30: CONFERE |
| L5-2 | não se aplica | não se aplica | não se aplica | não se aplica | não se aplica |
| L6-1 (sentido da troca de número) | não se aplica | não é número | número como valor da regra, sem "no mínimo": CONFERE | não é número | não é número |
| L6-2 (absoluto literal que não é a troca) | não se aplica | "único" mantido: CONFERE | "qualquer" mantido: CONFERE | não se aplica | não se aplica |
| L7-1 (valor posto igual ao de outra figura) | não se aplica | não se aplica | "dois anos" 0 vez na Lei 13.460 (v1; ficha 14.6): CONFERE | não se aplica | não se aplica |
| L7-2 (moldura e fórmula) | sem moldura | E com moldura sem a fórmula: CONFERE | sem moldura | E com moldura sem a fórmula: CONFERE | sem moldura |
| L7-3 (restritivo literal por marcador) | no D4, "somente" 0/0 e "sempre" 0 C / 1 E: sem gatilho | idem | idem | idem | idem |
| 13.2, item 4 (E sem [TS]) | C | com [TS] | com [TS] | com [TS] | com [TS] |
| 14.2, item 1 (AJ que muda a abertura) | sem AJ | efeito declarado na seção 5 | sem AJ | efeito declarado na seção 5 | sem AJ |
| 14.2, item 2 (justificativa sem afirmação sem fonte) | CONFERE | CONFERE (§ 1º citado com lastro) | CONFERE | CONFERE | CONFERE (G6 citado com lastro) |

As conferências de folha fechada e de K1 a K4 vêm da seção 4 do arquivo da leva e da ficha 14.4.6 e 14.6, e não foram refeitas aqui. As de leva foram refeitas (seção 0).

## 4. Leitura fora da amostra (sem veredito, fora da taxa)

1. **Registro inexato na v1, seção 4.6 (L3-3), à gcb-cqfp.** A v1 diz que os quatro itens com moldura não compartilham 40 caracteres de prefixo "nem entre si". O D4-R35 (8.2) e o D4-R42 (8.3) compartilham 86 caracteres ("Considere que um expositor, em audiência pública de comissão da Câmara dos Deputados, "). Os dois estão em folhas distintas, e a L3-3 é por folha: sem efeito em item. A linha da seção 4.6 da v2 sai recontada de qualquer modo (14.2, item 1), por causa dos AJ da seção 5.
2. **Abertura de atribuição nos declarativos do D4 (indício; script).**

   | abertura | canônicos (79) | levas 1 e 2 (27) | leva 8 (30) | D4 acumulado (136) |
   |---|---|---|---|---|
   | "Nos termos d…" | 4 C / 7 E | 0 / 0 | 1 C / 5 E | 5 C / 12 E |
   | "Segundo …" | 6 C / 13 E | 1 C / 2 E | 1 C / 3 E | 8 C / 18 E |
   | "De acordo com …" | 3 C / 0 E | 3 C / 1 E | 2 C / 2 E | 8 C / 3 E |
   | "Conforme …" | 0 / 0 | 0 / 0 | 2 C / 0 E | 2 C / 0 E |

   A regra ingênua "'Nos termos d…' ou 'Segundo …' no início → E" acertaria 30 de 43 no D4 acumulado (69,8%). Na leva 8, acertaria 8 de 10. A leva agrava o desvio que já estava nos canônicos. Nenhum marcador decide o gabarito, e a tendência é de lote, e não de item. Por isso nenhum AJ é pedido nesta leva. Vai como proposta para a leva 9 (seção 6).
3. **Fecho neutro × moldura no D4 (indício; script).** Fecho neutro com moldura: 1 C (D4-R20) / 4 E (D4-R08, R17, R42, R48). Fecho neutro sem moldura: 3 C (D4-R23, R38, R56) / 1 E (D4-R13). O conjunto inteiro está na faixa (4/5), mas a combinação "moldura + fecho neutro" inclina para E, como "moldura + fórmula" no D2 (L7-2). A leva 9 tem pouca margem: K1 está em 58,3% e K2 em 43,8%. Vai como proposta de medida (seção 6).
4. **Abertura variante nos E com moldura fora da amostra (D4-R42 e D4-R52).** Os AJ-L8-E1 e AJ-L8-E2 só desfazem a pista por completo se os outros dois E com moldura da leva também passarem à forma da cota. Os textos abaixo são **sugestão, sem veredito**; a adoção é da gcb-cqfp no R1. Cada "antes" ocorre exatamente 1 vez em saida/gcb/DA_reforco_leva8_v1.md (conferido por script), e nada muda além da abertura.
   - `S-L8-1 | D4-R42 | enunciado (seção 1) | substituir: «Considere que um expositor, em audiência pública de comissão da Câmara dos Deputados, trate da participação social.» | por: «Considere que, em audiência pública de comissão da Câmara dos Deputados, um expositor trate da participação social.»` Efeito: prefixo de 86 caracteres com o D4-19 e o D4-26 e, com o AJ-L8-E2, de 93 com o D4-R48 («… um expositor trate d»), na 8.3; cenas distintas até o fecho; 54 palavras.
   - `S-L8-2 | D4-R52 | enunciado (seção 1) | substituir: «Considere que um expositor, ouvido em audiência pública de comissão da Câmara dos Deputados, afirme que,» | por: «Considere que, em audiência pública de comissão da Câmara dos Deputados, um expositor afirme que,»` Efeito: prefixo de 98 caracteres com o D4-41, na 9.1, com cena distinta até o fecho. O enunciado passa de 58 a 57 palavras.
5. **"Considere que" por folha fechada (dado da v1, 4.6).** Na 8.2, CQ fica em 5 C / 1 E (83,3% de C) e, na 9.1, em 5 C / 2 E (71,4%). A 7.4.2 só fixa o mínimo de 40% de C, e as duas folhas cumprem. O excesso inverte a pista antiga ("Considere que → E") em "Considere que → C" nessas folhas. K4 do D4 está em 31/22 (58,5%), perto do teto de 60%. Na leva 9, o CQ novo do D4 é E de preferência.
6. **D4-R58 (absoluto inserido pela troca; v1, bloco 5, dúvida (vi)).** "definição exaustiva e definitiva" põe dois absolutos que não estão na fonte. A ficha 14.4.6 dizia "nenhum E com absoluto inserido". A L3-2 fica satisfeita pelos C com absoluto literal do lote (dado da v1). A estilo_banca 5.1 e a L3-2 preferem, quando a fonte permite, a troca por conceito vizinho (E1) à troca por absoluto. A decisão é da gcb-cqfp; registro, sem texto deste agente.
7. **"pois": 1 C (D4-R53) / 0 E.** A leva cumpre a estilo_banca 5.1 ("escreva C com 'pois'"). Registro.

## 5. Texto exato (AJ de v1; segue com os AJ do R1 para a v2 e é conferido no R2)

`AJ-L8-E1 | D4-R35 | enunciado (seção 1) | substituir: «Considere que um expositor, em audiência pública de comissão da Câmara dos Deputados, sustente que,» | por: «Considere que, em audiência pública de comissão da Câmara dos Deputados, um expositor afirme que,»`

`AJ-L8-E2 | D4-R48 | enunciado (seção 1) | substituir: «Considere que, durante audiência pública de comissão da Câmara dos Deputados, um expositor trate dos conselhos» | por: «Considere que, em audiência pública de comissão da Câmara dos Deputados, um expositor trate dos conselhos»`

Conferência por script sobre saida/gcb/DA_reforco_leva8_v1.md:
- cada "antes" ocorre 1 vez; cada "por" ocorre 0 vez;
- o enunciado só aparece na seção 1, porque o bloco da seção 2 não repete o enunciado;
- extensão: D4-R35 fica em 48 palavras e D4-R48 em 44 (L5-1).

Ficam iguais nos dois: ponto, gabarito, mecanismo, formato APL, Moldura (S, tipo e fecho), aderência, abertura CQ, campo Troca, [TS], Base e as duas linhas da justificativa.

**Efeito sobre o prefixo comum (14.2, item 1).** A v2 recalcula a linha de L3-3 da seção 4.6 e não a dá como "não muda". O previsto, por script:
- **D4-R35 (8.2):** prefixo de 110 caracteres com o D4-14 («Considere que, em audiência pública de comissão da Câmara dos Deputados, um expositor afirme que, nos termos d»). Depois, D4-14 «o Decreto nº 9.203/2017, constitui diretriz…» × D4-R35 «a Lei nº 11.079/2004, é admitida…». A cena é distinta até o fecho, e não há cenário gêmeo (9.3, item 3); a nota (df) e a ordem não mudam.
- **D4-R48 (8.3):** prefixo de 86 caracteres com o D4-19 e com o D4-26 («Considere que, em audiência pública de comissão da Câmara dos Deputados, um expositor »). Depois, «afirme que, nos termos…» × «trate dos conselhos…». Cena distinta.
- **Com a S-L8-1 adotada:** o D4-R48 e o D4-R42 passam a compartilhar 93 caracteres («… um expositor trate d»). Depois, «os conselhos de usuários…» × «a participação social.». Cena distinta.
- **Moldura:** o classificador da T-122 continua a dar S nos dois itens, porque o tipo da cota fica literal: «audiência pública de comissão da Câmara dos Deputados» e «expositor». A gcb-cpp reconfere por script na v2.

Se o R1 pedir o mesmo texto, ele é aplicado uma vez, com as duas origens (11.3). Se o R1 pedir outro texto para a abertura desses itens, prevalece o do R1, desde que a abertura dos E com moldura deixe de diferir da dos C com moldura da mesma folha. A reconciliação registra.

## 6. Recomendações para as próximas levas

Propostas à GCB (texto da gbq-estilo; a aceitação é da GCB na reconciliação ou na ficha da leva 9):

- **L8-1 — abertura da moldura (texto da gbq-estilo).** "Nos itens com moldura de expositor (folhas 8.x e 9.x), a abertura segue a forma da cota ('Considere que, em audiência pública de comissão da Câmara dos Deputados, um expositor …'), qualquer que seja o gabarito. Variante de abertura só entra se o lote tiver C com moldura com a mesma variante. Prefixo comum de 40 ou mais caracteres com canônico da folha é registrado na seção 4 (L3-3; 14.2, item 1) e não impede o item quando a cena diverge antes do fecho. A seção 4 do arquivo da leva conta, por script, abertura da moldura × gabarito no lote acumulado." (D4 acumulado: forma da cota 14 C / 6 E; variantes 0 C / 4 E.)
- **L8-2 — abertura de atribuição nos declarativos (texto da gbq-estilo).** "Nos declarativos do D4, as aberturas 'Nos termos d…' e 'Segundo …' não ficam concentradas em E. Na leva 9, os itens novos com essas aberturas têm ao menos 50% de C, e a seção 4 conta abertura de atribuição × gabarito no lote acumulado." (D4 acumulado: "Nos termos d…" 5 C / 12 E; "Segundo …" 8 C / 18 E; "De acordo com …" 8 C / 3 E.)
- **L8-3 — fecho neutro × moldura (medida).** "A seção 4 do arquivo da leva conta fecho neutro × moldura × gabarito no D4 acumulado (hoje: com moldura 1 C / 4 E; sem moldura 3 C / 1 E). Na leva 9, nenhum E com moldura usa o fecho neutro se houver alternativa dentro das faixas de K1 e K2; se não houver, a ficha registra o desvio."

## 7. Registros

1. **Rito:** auditoria sobre a v1, em paralelo ao R1, como a ficha 9.3, item 6, e a 14.4.8 determinam. Os AJ-L8-E1 e AJ-L8-E2 seguem com os AJ do R1 para a v2 e são conferidos no R2. Nenhuma errata pós-R2 (seção 7.6) é proposta. As sugestões S-L8-1 e S-L8-2 (seção 4, item 4) não são AJ desta auditoria, porque os itens estão fora da amostra.
2. **Versão do catálogo:** o despacho cita "regras/estilo_banca.md (versão em disco)". O arquivo em disco é a **v1.1.3** (linha 2; SHA-256 na seção 0), a mesma das auditorias das levas 1 a 7. Os mecanismos citados (C2, C6, E1, E2, E3) e as seções 3.1, 3.2, 3.3, 3.8, 3.12, 3.13, 4, 5.1 e 5.3 são os da v1.1.3. Nada foi alterado no catálogo.
3. **Nome do arquivo:** o do despacho e da ficha 14.4.8 e 7.5 (saida/banco/estilo_DA_reforco_leva8.md).
4. **Fidelidade às bases:** só se leram, para confirmar o trecho decisivo dos 5 itens:
   - Lei 11.079, art. 2º, caput e §§ 1º a 4º (Anexo N do D4, 4.2);
   - Lei 13.019, art. 2º, I, a a c, III, VII, VIII e VIII-A (Anexo N do D4, 4.3);
   - Lei 13.460, arts. 18, 19, 21 e 23, caput e §§ 1º e 2º (adendo de 22/10/2026, 4.4);
   - Guia F2, cópia, linhas 515 a 562.

   Os §§ 1º e 2º da Lei 11.079 e as linhas 517, 558 e 561 do Guia são citados só como razão de veredito, e não como base de item. A conferência das bases e da pertinência é matéria da gcb-cqfp.
5. **D4-R44, aderência parcial:** fixada pela ficha 14.6 depois da designação da amostra. A pertinência é da gcb-cqfp. O item conta para a composição da seção 5 enquanto a parcialidade valer.
6. **Escopo:** nada vai à plataforma nem à candidata. Nenhuma tarefa nova (D-COMPLEMENTOS). Nenhum gatilho em PARA_PRESIDENCIA.md. Nenhum NÃO CONFORME, e por isso nenhum GATE pela regra 6.

AVISO: os vereditos, a atribuição de mecanismo, a leitura de pista e o juízo de risco de "mais de uma interpretação" são julgamento deste agente (gbq-estilo) e exigem revisão da GBQ. Vêm de script sobre os arquivos gravados (python3 -I, somente leitura), com revisão manual dos 5 itens, as contagens de:
- abertura, fecho, fórmula, moldura × abertura e fecho neutro × moldura;
- absolutos e marcadores, "pois", "não" e "sem";
- extensão e prefixo de cena.

As contagens de folha fechada, de K1 a K4, de sequência e de moldura acumulada de DA, e a contagem de "dois anos" na Lei 13.460, foram tomadas da seção 4 do arquivo da leva e da ficha, sem refazer. Com n pequeno (amostra de 5; recortes de 4 a 136 itens), nenhuma associação é regra, e nenhum marcador decide o gabarito. A tabela serve para corrigir vieses de redação, nunca para prever gabarito.

FIM DA AUDITORIA DE ESTILO — LEVA 08 — REFORÇO DA
