# estilo_DA_reforco_leva5.md — T-116 — 2026-10-22 — gerado por gbq-estilo

Auditoria de estilo Cebraspe da amostra da leva 5 do reforço de DA (D-REFORCO-2, regra 6; D-REFORCO-DA; ficha, seções 5, 7.4, 7.6, 9.3, 10.2, 11.2, 11.3 e 11.4.8). Ciclo s16c3. Destino: gcb-cqfp (o AJ abaixo segue com os AJ do R1 para a v2 e é conferido no R2) e gcb-gerencia (reconciliação da leva 5). Este agente audita e não produz. Nenhum outro arquivo foi alterado; regras/estilo_banca.md não foi tocado. Sem commit nem push.

**Resultado:** 4 itens auditados (13,3% de 30), sobre a **v1**, em paralelo ao R1 (ficha 9.3, item 6; 11.4.8). Vereditos: 3 CONFORMES (D2-R30, D2-R36 e D2-R47), 1 AJUSTE (texto) (D2-R32), 0 NÃO CONFORME. O AJ não muda gabarito, ponto de julgamento, mecanismo, formato, moldura S/N, aderência, abertura, campo Troca nem [TS]. Sem GATE pela regra 6.

**Rito:** cumprido como a ficha 9.3, item 6, e a 11.4.8 mandam. A auditoria correu sobre a v1, antes do R1 gravado (saida/gcb/QA_DA_reforco_leva5_R1_* ausente em disco na hora da leitura). O texto da seção 5 é, portanto, **AJ de v1**, e não errata pós-R2 (a seção 7.6 não se aplica). Se o R1 pedir o mesmo texto, ele é aplicado uma vez e registrado como um só ajuste, com as duas origens (ficha 11.3). É 1 linha de AJ, em 1 item.

**Registro do despacho:** o produtor mudou a troca do D2-R32 de "cinco" (coluna da ficha 11.4.4) para "dez dias" (bloco à GCB, dúvida (i); seção 6.2, item 1, do arquivo da leva). O estilo do item foi julgado como está na v1. Decidir o número cabe à gcb-cqfp e à GCB. A seção 2 registra a leitura de estilo sobre essa escolha.

**Classificação:** os vereditos, a atribuição de mecanismo, a leitura de pista e o juízo de risco de "mais de uma interpretação" são julgamento deste agente (gbq-estilo) e exigem revisão da GBQ (ver o AVISO no fim).

## 0. Objeto, entradas e método

| objeto | SHA-256 |
|---|---|
| saida/gcb/DA_reforco_leva5_v1.md (objeto; 30 itens; QA PENDENTE) | 3062f7cecdb62a7037234f30bae87f51b610ec0131c0b6a4eb3a39108254e591 (conferido em disco; igual ao do despacho) |
| saida/gcb/DA_reforco_ficha_2026-10-20.md (amostra: 11.4.8; rito: 5, 7.4, 7.6, 9.3, 10.2, 11.2, 11.3) | 2e676c62d45487ed5f267f40d8f70d9761e2e67534991aa9564a9550c88a4899 (conferido em disco) |
| regras/estilo_banca.md (catálogo em disco: **v1.1.3**, linha 2) | 9f9237f5f9828b77d5ab805849a7a14af13fb28fcc1c985fe462ec1027684caf |
| saida/banco/estilo_DA_reforco_leva4.md (modelo de forma e critérios) | lido; não alterado |
| saida/gcb/normativo_cache/Lei_8112_1990_compilada_2026-10-20.txt (D2-R32, linhas 481 a 485; D2-R36, linha 102) | 72f45d30…2efe (SHA-256 declarado no arquivo da leva; não refeito) |
| saida/gcb/normativo_cache/Lei_9784_1999_2026-10-20.txt (D2-R47, linha 31) | f9452916…ae19 (SHA-256 declarado no arquivo da leva; não refeito) |
| saida/gcb/D2_anexo_N_mapa_normativo.md (D2-R30, Lei 6.999, art. 4º, linha 1822; sem cópia em cache) | b0a54fff…340a (SHA-256 declarado na ficha 11.4.2; não refeito) |

**Script:** python3 -I, somente leitura, no scratchpad da sessão, sobre o arquivo da leva (seções 1 e 2). Ele extrai enunciados e gabaritos e conta:
- abertura × gabarito;
- a fórmula "Nessa situação, nos termos d…";
- absolutos por gabarito (sempre, somente, apenas, só, exclusivamente, qualquer, todo/toda, nenhum/nenhuma, ninguém, vedado/vedada);
- números no enunciado;
- extensão;
- ocorrências do "antes" e do "depois" da seção 5.

As contagens de folha fechada e de moldura acumulada não foram refeitas. Vêm da seção 4 do arquivo da leva e são matéria do R1.

**Conferência por script (leva 5, 30 itens):**
- "Considere que": 7 C / 7 E; declarativos: 9 C / 7 E.
- Fórmula "Nessa situação, nos termos d…": 3 C / 4 E, em 7 dos 14 CQ (no limite da orientação, ficha 11.4.6).
- Fecho "é correto afirmar que": 0 nos enunciados.
- Absolutos nos enunciados: C 5 (D2-R25 "somente", D2-R31 "qualquer", D2-R34 "nenhum", D2-R36 "somente", D2-R49 "ninguém"); E 1 (D2-R47 "vedada", inserido pela troca).
- Extensão: C de 15 a 53 palavras (média 32,5); E de 26 a 56 (média 35,9).

Conferem com a seção 4.6 do arquivo e com a ficha 11.4.6.

**Critérios de estilo:** os mesmos das levas 1 a 4 (estilo da leva 4, seção 0):
- comando C/E;
- uma afirmação, com um só ponto de erro;
- troca real e única;
- nenhuma pista de forma;
- extensão dentro da faixa da base (estilo_banca v1.1.3, seção 4: C de 8 a 65 palavras; E de 19 a 62);
- registro formal;
- termo absoluto só quando for letra da fonte ou a própria troca;
- moldura que não decide o gabarito (R1 da T-122);
- risco de "mais de uma interpretação" (estilo_banca, seção 5.3);
- L3-1 a L3-5 (ficha 9.3), L4-1 a L4-4 e itens 5 e 6 da ficha 10.2, L5-1 e L5-2 (ficha 11.2).

Vereditos:
- **NÃO CONFORME:** dois pontos de erro, pista que entrega o gabarito, E decidido pela moldura, ou gabarito que só se sustenta com escolha da produção.
- **AJUSTE (texto):** defeito sanável por substituição exata, sem mudar gabarito, ponto, mecanismo nem a natureza da troca.

## 1. Amostra

Fixada pela ficha, seção 11.4.8, antes da produção. Sem sorteio.

| id | folha | lote | gab. | formato | moldura | aderência | o que cobre |
|---|---|---|---|---|---|---|---|
| D2-R32 | 3.4 | D2 | E [TS] | APL | S (órgão/servidor do Poder Legislativo da União) | direta | E com moldura; troca de número; Lei 8.112, art. 97, III, a |
| D2-R47 | 4.1 | D2 | E [TS] | APL | S (idem) | direta | E com moldura; absoluto inserido "vedada"; Lei 9.784, art. 2º, parágrafo único, XII |
| D2-R36 | 3.4 | D2 | C | DEF | N | direta | C da exigência (b); absoluto literal "somente"; Lei 8.112, art. 20, § 4º |
| D2-R30 | 3.3 | D2 | E [TS] | PAR | N | direta | E da folha sem cópia em cache; Lei 6.999, art. 4º |

**Composição exigida (ficha, seção 5): CONFERE.**
- Tamanho: ⌈10% de 30⌉ = 3; foram designados 4.
- Ao menos 1 E com moldura: D2-R32 e D2-R47, nas duas folhas com cota (3.4 e 4.1).
- Todos os lotes da leva: só há o D2, e os 4 itens são dele.
- Ao menos 1 C: D2-R36.
- Parcial: a leva tem 0 parciais (30 diretos), e a exigência não se aplica.

## 2. Vereditos por item

Palavras: só o enunciado, sem o comando.

| id | gab. | mecanismo | trecho decisivo | palavras | veredito | motivo |
|---|---|---|---|---|---|---|
| D2-R32 | E [TS] | E3 (inventa prazo: troca de número; declarado e confirmado) | "por dez dias consecutivos em razão do casamento" | 36 | **AJUSTE (texto)** | **Gabarito, ponto e troca corretos.** A Lei 8.112, art. 97, III, a, diz "por 8 (oito) dias consecutivos em razão de: a) casamento" (cópia, linhas 481 a 485), e o item põe dez. É uma troca só, de um número, na posição da letra.<br><br>**A moldura não decide.** O cenário só põe o servidor em órgão do Poder Legislativo da União, e o fecho cita a Lei 8.112. Não há fecho de acerto nem norma interna.<br><br>**Escolha de "dez" no lugar de "cinco", a favor no estilo.** Com "poderá ausentar-se … por cinco dias", o item ficaria verdadeiro como afirmação parcial: quem tem direito a oito dias pode ausentar-se por cinco. Isso é o C6 da base ("incompleto não é errado", estilo_banca 3.12), e o E ficaria discutível. "Dez" contradiz a letra sem essa leitura, e o número verdadeiro vem do artigo verificado (regra 4 do E3, estilo_banca 5.2, lida como no estilo da leva 3, D3-R24). "Dez dias" não coincide com prazo de outro item da 3.4 (0 nos enunciados de D2-31 a D2-40 e na leva; o "dez … trinta dias" do D2-30 é da 3.3). Decidir o número cabe ao R1 e à GCB (dúvida (i)).<br><br>Fórmula "Nessa situação, nos termos d…": é um dos 7 de 14 CQ, dentro do limite. Sem cenário gêmeo (L3-3), sem contraste e sem qualificador.<br><br>**Defeito (absoluto da letra cortado, com efeito de marcador):** a letra é "Sem qualquer prejuízo, poderá o servidor ausentar-se do serviço" (cópia, linha 481), e o item escreve "sem prejuízo". O corte deixa "sem prejuízo" sem complemento, uma elipse que a letra não tem. Também tira da leva o único E em que um absoluto literal não seria o erro. Na leva, hoje, todo absoluto literal está em C (5 de 5: D2-R25, R31, R34, R36, R49), e o único absoluto em E é o inserido pela troca (D2-R47). A regra ingênua "absoluto que soa a letra → C" acerta 5 de 5, o oposto do que estilo_banca 5.1 pede ("Não deixe o marcador coincidir sempre com o mesmo gabarito"). Na base, há E com absoluto que não é o erro (BQ-0003, BQ-0043; estilo_banca 3.13).<br><br>**Correção:** o AJ-L5-E1 repõe "qualquer", que é letra. Com ele, "qualquer" fica 1 C / 1 E na 3.4 (D2-R31 C; D2-R32 E). O resultado tem 37 palavras. Ficam iguais: ponto, gabarito, mecanismo, formato APL, moldura S (mesmo tipo), aderência, abertura CQ, campo Troca ("8 (oito) dias consecutivos → dez dias consecutivos") e [TS]. A justificativa, linha 1, já traz "sem qualquer prejuízo" e fica literal ao enunciado. A linha 2 continua verdadeira.<br><br>**Observação (sentido da troca de número na leva):** ver a seção 4. |
| D2-R47 | E [TS] | E3 (cria vedação inexistente no lugar da ressalva "sem prejuízo"; declarado e confirmado; fronteira com E2, inversão de polaridade) | "vedada a atuação dos interessados" | 43 | **CONFORME** | **Uma troca** ("sem prejuízo da atuação dos interessados" → "vedada a atuação dos interessados") sobre texto que, de resto, é a letra da Lei 9.784, art. 2º, parágrafo único, XII ("impulsão, de ofício, do processo administrativo, sem prejuízo da atuação dos interessados"; cópia, linha 31). O E está na letra: o inciso ressalva a atuação dos interessados, e o item a veda.<br><br>**A moldura não decide.** O cenário diz "no desempenho de função administrativa", que é a condição do art. 1º, § 1º, para a lei alcançar o órgão do Legislativo da União. A dúvida sobre a aplicação da lei não surge, e a leitura "Legislativo → a lei não se aplica → E" fica bloqueada. Não há norma interna, regimento nem prática real da Câmara.<br><br>**L3-2 cumprida:** o absoluto "vedada" é inserido pela troca, e a 4.1 tem C com absoluto literal (D2-R49, "ninguém"). Não havia troca E1 limpa no inciso XII: "condicionada à provocação dos interessados" contradiria "de ofício" dentro da própria frase, e isso seria pista. A troca "vedada" é a do plano (ficha 11.4.4).<br><br>Sem "mas não", ", e não" ou qualificador. O cenário é distinto do D2-R41 e do D2-R50 (L3-3; o arquivo registra 0 prefixos comuns de 40 ou mais caracteres). Registro formal. "do processo" encurta "do processo administrativo" sem mudar o sentido, porque o cenário já nomeia o processo administrativo.<br><br>**Observação 1 (tentação, não pista):** "instaurado processo administrativo de ofício", no cenário, aproxima a instauração de ofício (outra regra) da impulsão de ofício do fecho. Isso puxa para o C quem acha que processo aberto de ofício dispensa os interessados. É a tentação declarada na justificativa, linha 2, e não entrega o gabarito.<br><br>**Observação 2 (discriminação):** quem conhece o contraditório (D2-49, inciso X, na mesma folha) recusa "vedada" com facilidade. O item discrimina pouco entre candidatas preparadas, mas não tem defeito. A nota (be) limita a 2 por simulado os itens do mesmo parágrafo único. |
| D2-R36 | C | C3 (C com traço de E: o restritivo "somente"; declarado). Também é C2 (reprodução quase literal) | "somente poderão ser concedidas as licenças e os afastamentos previstos nos arts. 81, incisos I a IV, 94, 95 e 96" | 53 | **CONFORME** | **Reprodução da Lei 8.112, art. 20, § 4º** (cópia, linha 102). A única diferença é "bem como o afastamento" no lugar de "bem assim afastamento", que é equivalente e está registrada pela produção (seção 6.2, item 8).<br><br>**Absoluto literal em C,** como estilo_banca 5.1 recomenda ("escreva C … com termo absoluto, quando a restrição for a própria definição") e a exigência (b) da ficha pede. O item tem um só ponto. Não traz número do estágio probatório (alerta 3 do Anexo), nem o caput, o § 5º ou o Decreto 12.374. A extensão está na faixa de C (8 a 65). Registro formal.<br><br>Classificar como C3 é defensável: na base, o absoluto é traço de E (3.13), e o item pune quem marca E por reflexo diante do "somente". Pela forma, o mecanismo primário é C2. A diferença não muda nada no item.<br><br>**Pista conferida:** na leva, o absoluto literal está em C 5 vezes. Com o AJ-L5-E1, uma ocorrência passa a E (seção 2, D2-R32), e o D2-R36 deixa de reforçar a série "absoluto literal → C".<br><br>**Observação 1 (risco residual de interpretação, não reprova):** a mesma lei concede "ao servidor", sem ressalva de estágio, a licença para tratamento de saúde (art. 202; cópia, linha 872) e a licença à gestante (art. 207; cópia, linha 890), que estão fora do rol do § 4º. Uma leitura sistemática pode alegar que o "somente" do § 4º não esgota as licenças possíveis no estágio e sustentar E em recurso. A leitura do C é a da letra ("Segundo a Lei nº 8.112/1990" + texto literal do parágrafo), e o risco fica abaixo do dos anulados da ANM (estilo_banca 5.3). Os arts. 202 e 207 são citados aqui só como razão da observação, e não como base de item. A nitidez é matéria do R1.<br><br>**Observação 2 (discriminação):** o item cobra memória de remissão numérica (arts. 81, I a IV, 94, 95 e 96). O par com o D2-39 (E, licença para trato de assuntos particulares no estágio) dá o uso do dispositivo, e a nota (ay) separa os dois no simulado. |
| D2-R30 | E [TS] | E1 (troca de conceito vizinho: prazo certo → prazo indeterminado, a regra geral do Decreto 10.835, art. 11; declarado e confirmado) | "são feitas por prazo indeterminado" | 28 | **CONFORME** | **Uma troca** sobre a Lei 6.999, art. 4º, caput ("Exceto no caso de nomeação para cargo em comissão, as requisições para as Secretarias dos Tribunais Eleitorais, serão feitas por prazo certo, não excedente de 1 (um) ano"; Anexo N do D2, linha 1822; sem cópia em cache, limitação de método da ficha 11.4.2, (c)). O E está na letra.<br><br>**O conceito vizinho tem lastro e dá discriminação:** o prazo indeterminado é a regra geral do Decreto 10.835, art. 11, "salvo disposição legal em contrário", e a Lei 6.999 é essa disposição. A nota (au) separa o item do D2-25.<br><br>**A ressalva sem "exceto"** (ficha 11.4.4; 4.1, item 4) vira oração restritiva ("que não se destinem à nomeação para cargo em comissão"). O "não" é a ressalva da lei, e não negação frontal (7.4.5; 10.2, item 5). A oração gramaticalmente poderia se ligar a "Tribunais Eleitorais", mas o sentido só admite "requisições". A leitura é única.<br><br>Declarativo, sem moldura, com a norma na abertura. A 3.3 fechada fica com declarativos 6 C / 9 E (60,0% de E; dado do arquivo, não refeito; L3-1). Não há absoluto: o E não usa "sempre" nem "sem limite", e a troca é de conceito, como L3-2 prefere. Extensão dentro da faixa de E. Registro formal.<br><br>**Observação (renovação):** a Lei 6.999 prevê renovação anual das requisições "atualmente" existentes nas Secretarias (art. 5º; Anexo N, linha 1824). Isso não torna o prazo indeterminado nem cria segunda leitura: é regra transitória, e o item fala da regra do art. 4º. |

**Taxas:**
- NÃO CONFORME: 0/4.
- AJUSTE (texto): 1/4 (D2-R32), sem mudança de gabarito.
- Itens decididos pela moldura: 0. Nos dois itens com moldura (D2-R32 e D2-R47), o E está na letra.

## 3. Conferência de L3-1 a L3-5 (ficha 9.3), L4-1 a L4-4, itens 5 e 6 (ficha 10.2), L5-1 e L5-2 (ficha 11.2) nos 4 itens

| regra | D2-R32 (E) | D2-R47 (E) | D2-R36 (C) | D2-R30 (E) |
|---|---|---|---|---|
| L3-1 (abertura por folha fechada) | CQ E na 3.4; a 3.4 fechada fica com CQ 4 C / 5 E (44,4% de C): CONFERE | CQ E na 4.1; a 4.1 fechada fica com CQ 6 C / 4 E: CONFERE | DC C na 3.4; a 3.4 fechada fica com DC 6 C / 5 E (45,5% de E): CONFERE | DC E na 3.3; a 3.3 fechada fica com DC 6 C / 9 E: CONFERE |
| L3-2 (absoluto inserido pela troca) | sem absoluto inserido. Com o AJ, "qualquer" é letra e não é a troca: não se aplica | "vedada" inserido; C literal na mesma folha (D2-R49): CONFERE | C, absoluto literal: não se aplica | sem absoluto: não se aplica |
| L3-3 (cenário gêmeo) | cenário distinto do D2-R35, D2-R37 e D2-R39: CONFERE | cenário distinto do D2-R41 e do D2-R50: CONFERE | declarativo: não se aplica | declarativo: não se aplica |
| L3-4 ("mas não" / ", e não") | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE |
| L3-5 (qualificador minimizador) | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE |
| L4-1 (fecho "é correto afirmar que" fora do D4) | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE. Na leva, 0 (script) |
| L4-2 (abertura da 6.2) | não se aplica | não se aplica | não se aplica | não se aplica |
| L4-3 (referente de rol, E6) | não é E6 | não é E6 | C: não se aplica | não é E6 |
| L4-4 (condição inventada sobre hipótese autônoma) | E3 de número: não se aplica | E3 de ressalva: não se aplica | C: não se aplica | E1: não se aplica |
| 10.2, item 5 (hipótese inteira negada no fecho) | o fecho troca o número sem negar: CONFERE | o fecho troca a ressalva sem negar a impulsão: CONFERE | C: não se aplica | o "não" é a ressalva da lei: CONFERE |
| 10.2, item 6 (SUJ E com ator plausível) | não é SUJ | não é SUJ | não é SUJ | não é SUJ |
| L5-1 (extensão) | 36 palavras (37 com o AJ), dentro de 19 a 62: CONFERE | 43: CONFERE | 53, dentro de 8 a 65 (C): CONFERE | 28: CONFERE |
| L5-2 (absoluto da letra retirado de E com outra troca) | o "qualquer" da letra foi retirado sem ordem da ficha, e o AJ o repõe. Não há verbo de condição necessária: CONFERE com o AJ | não se aplica | C: não se aplica | não se aplica |

As conferências de folha fechada vêm da seção 4.6 do arquivo da leva e não foram refeitas aqui. As de leva foram refeitas (seção 0).

## 4. Leitura fora da amostra (sem veredito, fora da taxa)

- **Sentido da troca de número (indício; n = 4).** Na leva, todas as trocas de número em E vão para cima:
  - D2-R23: seis meses → um ano;
  - D2-R32: oito → dez dias;
  - D2-R33: dez → vinte por cento;
  - D2-R37: três → seis meses.

  Na leva 3, o D3-R24 também foi para cima (sessenta → noventa dias; estilo da leva 3). O motivo é real e foi registrado pela produção (dúvida (i)). Quando a letra é duração, teto ou piso afirmado como permissão ("poderá … por", "por até", "não pode ser inferior a"), um número menor fica compatível com a letra (C6), e só o maior dá E nítido. A série cria um atalho: "prazo ou percentual mais generoso que o esperado → E". Com 4 itens na leva, é indício, e não padrão. Não há efeito sobre o AJ. O texto da recomendação está na seção 6, L6-1.
- **Absolutos na leva (script):** 5 C / 1 E, e o único E é aquele em que o absoluto é a troca. Com o AJ-L5-E1, ficam 5 C / 2 E, e um dos E tem absoluto literal que não é o erro. A recomendação está na seção 6, L6-2.
- **Fórmula "Nessa situação, nos termos d…":** 7 dos 14 CQ (3 C / 4 E), no limite da orientação da ficha (no máximo 7). Na leva 6, qualquer CQ a mais com a fórmula passa do limite.
- **Moldura na leva:** 1 C / 6 E (D2-R35 C; D2-R32, R37, R39, R41, R47, R50 E), como no plano (ficha 11.4.6). O equilíbrio é o do DA acumulado e das folhas fechadas (3.4 e 4.1: 2 C / 3 E cada, dado da ficha), e não o da leva. A nota (x) já leva os sete ao teto de C com moldura por simulado.

## 5. Texto exato (AJ de v1; segue com os AJ do R1 para a v2 e é conferido no R2)

Formato da ficha, seção 4.3. O "antes" ocorre exatamente 1 vez em saida/gcb/DA_reforco_leva5_v1.md, e o "depois", 0 vez, conferido por script. A forma curta «sem qualquer prejuízo,» já aparece na justificativa, linha 1, do D2-R32. Por isso o "antes" e o "depois" incluem "por dez dias".

`AJ-L5-E1 | D2-R32 | enunciado (seção 1) | substituir: «ausentar-se do serviço, sem prejuízo, por dez dias» | por: «ausentar-se do serviço, sem qualquer prejuízo, por dez dias»`

**Efeito:**
- Ficam inalterados: gabarito (E), ponto (Lei 8.112, art. 97, III, a), mecanismo (E3), formato (APL), moldura (S, mesmo tipo; fecho neutro), aderência (direta), abertura (CQ), campo Troca, [TS], fórmula "Nessa situação, nos termos d…" e justificativa (linhas 1 e 2).
- O item vai de 36 para 37 palavras.
- Nenhum outro campo do bloco precisa de harmonização.

**Contagens a refazer na v2 (por script, seção 4.6 do arquivo):**
- absolutos por gabarito: "qualquer" fica 1 C / 1 E; "E com absoluto literal que não é a troca" vai de 0 para 1; "E com absoluto inserido" continua só o D2-R47;
- extensão do D2-R32.

Abertura, fecho, fórmula, moldura e L3-2 ficam iguais.

**Interação com o R1:** se o R1 mudar o número do D2-R32, o "antes" deixa de ocorrer. Nesse caso, vale o texto do R1, e a gcb-cpp repõe "qualquer" pelo mesmo princípio, só se o R1 o tiver acolhido. Se não tiver, a GCB registra na reconciliação. Se o R1 pedir este mesmo texto, é um só ajuste, com as duas origens (ficha 11.3).

**O que o R2 confere:**
1. O "antes" com 1 ocorrência na v1 e o "depois" aplicado literalmente na v2.
2. Nenhum outro campo do bloco muda.
3. Lido inteiro, o enunciado resultante mantém o E pela letra ("Sem qualquer prejuízo, poderá o servidor ausentar-se do serviço: … III - por 8 (oito) dias consecutivos em razão de: a) casamento"; cópia, linhas 481 a 485) e não cria pista.

**Se a gcb-cqfp recusar o AJ:** o item segue como está na v1. O defeito é de marcador e de fidelidade à letra, não de gabarito.

## 6. Recomendações para as próximas levas

Texto exato para a gcb-gerencia incluir na ficha da leva 6 ou nas seguintes, se aceitar. Nenhuma tem efeito sobre os 30 itens da leva 5 além do AJ da seção 5.

- **L6-1 (sentido da troca de número):** "Em item E cuja troca é um número (prazo, percentual, período ou quantidade), a leva não põe todas as trocas no mesmo sentido. Quando a letra afirma o número como permissão, teto ou piso ('poderá … por', 'por até', 'não pode ser inferior a') e a troca para menor ficaria compatível com a letra, o item afirma o número como valor da regra ('o período de ausência … é de cinco dias', 'o percentual mínimo de cada parcela é de cinco por cento'). Assim, a troca para menor também contradiz a letra. A seção 4 do arquivo da leva lista, por script, o sentido de cada troca de número (para mais ou para menos) e a contagem por leva."
- **L6-2 (absoluto literal que não é a troca):** "Absoluto que é letra da fonte e não é o elemento trocado fica no enunciado também em item E ('sem qualquer prejuízo', Lei 8.112, art. 97; D2-R32, AJ-L5-E1). A seção 4 do arquivo da leva conta por gabarito o absoluto literal que não é a troca, ao lado do absoluto inserido (L3-2)."
- **À GCB (fórmula):** a fórmula "Nessa situação, nos termos d…" chegou ao limite na leva 5 (7 de 14 CQ). Não há texto novo. A orientação da ficha 7.4.3 já cobre o caso.

## 7. Registros

1. **Rito:** auditoria sobre a v1, em paralelo ao R1, como a ficha 9.3, item 6, e a 11.4.8 determinam. O AJ segue para a v2 com os do R1 e é conferido no R2. Nenhuma errata pós-R2 (seção 7.6) é proposta.
2. **Versão do catálogo:** o despacho cita "regras/estilo_banca.md (versão em disco)". O arquivo em disco é a **v1.1.3** (linha 2; SHA-256 na seção 0), a mesma das auditorias das levas 1 a 4. Os mecanismos citados (C2, C3, C6, E1, E2, E3, E6) e as seções 3.3, 3.8, 3.9, 3.12, 3.13, 4, 5.1, 5.2 e 5.3 são os da v1.1.3. Nada foi alterado no catálogo.
3. **Nome do arquivo:** o da ficha 11.4.8 e 7.5 (saida/banco/estilo_DA_reforco_leva5.md).
4. **Fidelidade às bases:** só se leram as linhas das bases dos 4 itens, para confirmar o trecho decisivo:
   - Lei 8.112, arts. 20, § 4º (e § 5º, como contexto), 81, 97, 202 e 207;
   - Lei 9.784, art. 2º, parágrafo único, XII;
   - Lei 6.999, arts. 4º e 5º, no Anexo N do D2.

   Os arts. 202 e 207 da Lei 8.112 e o art. 5º da Lei 6.999 são citados só como razão de observação de risco, e não como base de item. A conferência das bases é matéria da gcb-cqfp.
5. **Troca do D2-R32:** julgada como está na v1 ("dez dias"), conforme o despacho. A mudança em relação à ficha ("cinco") é desvio declarado pela produção (seção 6.2, item 1, e bloco à GCB, dúvida (i)), e decidi-la não cabe a este agente.
6. **Escopo:** nada vai à plataforma nem à candidata. Nenhuma tarefa nova (D-COMPLEMENTOS). Nenhum gatilho em PARA_PRESIDENCIA.md. Nenhum NÃO CONFORME, e por isso nenhum GATE pela regra 6.

AVISO: os vereditos, a atribuição de mecanismo, a leitura de pista e o juízo de risco de "mais de uma interpretação" são julgamento deste agente (gbq-estilo) e exigem revisão da GBQ. As contagens de abertura, de fórmula, de fecho, de absolutos, de números, de extensão e de ocorrência dos trechos de AJ vêm de script sobre o arquivo gravado (python3 -I, somente leitura), com revisão manual dos 4 itens. As contagens de folha fechada e de moldura acumulada foram tomadas da seção 4 do arquivo da leva e da ficha, sem refazer. Com n pequeno (amostra de 4; recortes de 1 a 30 itens), nenhuma associação é regra, e nenhum marcador decide o gabarito. A tabela serve para corrigir vieses de redação, nunca para prever gabarito.

FIM DA AUDITORIA DE ESTILO — LEVA 05 — REFORÇO DA
