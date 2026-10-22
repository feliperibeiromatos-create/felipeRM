# estilo_DA_reforco_leva4.md — T-116 — 2026-10-22 — gerado por gbq-estilo

Auditoria de estilo Cebraspe da amostra da leva 4 do reforço de DA (D-REFORCO-2, regra 6; D-REFORCO-DA; ficha, seções 5, 7.4, 7.6, 9.3, 10.2 e 10.4.8). Ciclo s16c2. Destino: gcb-cqfp (os AJ abaixo seguem com os AJ do R1 para a v2 e são conferidos no R2) e gcb-gerencia (reconciliação da leva 4). Este agente audita e não produz. Nenhum outro arquivo foi alterado; regras/estilo_banca.md não foi tocado. Sem commit nem push.

**Resultado:** 4 itens auditados (14,3% de 28), sobre a **v1**, em paralelo ao R1 (ficha 9.3, item 6). Vereditos: 2 CONFORMES (D2-R14 e D3-R56), 2 AJUSTE (texto) (D2-R05 e D3-R54), 0 NÃO CONFORME. Nenhum AJ muda gabarito, ponto de julgamento, mecanismo, formato, moldura S/N, aderência, abertura, campo Troca ou [TS]. Sem GATE pela regra 6.

**Rito:** cumprido como a ficha 9.3, item 6, e a 10.4.8 mandam. A auditoria correu sobre a v1, antes do R1 gravado (saida/gcb/QA_DA_reforco_leva4_R1_* ausente em disco na hora da leitura). Os textos da seção 5 são, portanto, **AJ de v1**, e não errata pós-R2 (a seção 7.6 não se aplica). São 2 linhas de AJ, em 2 itens.

**Classificação:** os vereditos, a atribuição de mecanismo, a leitura de pista e o juízo de risco de "mais de uma interpretação" são julgamento deste agente (gbq-estilo) e exigem revisão da GBQ (ver o AVISO no fim).

## 0. Objeto, entradas e método

| objeto | SHA-256 |
|---|---|
| saida/gcb/DA_reforco_leva4_v1.md (objeto; 28 itens; QA PENDENTE) | 7b0c1dc7c38d1b92de08b3e4c21676df9591a5a13122b5de7670d65642e0f3d8 |
| saida/gcb/DA_reforco_ficha_2026-10-20.md (amostra: 10.4.8; rito: 5, 7.4, 7.6, 9.3, 10.2) | 777e6eb6a2d871f5d6afc26b22a479a9ccfcb9ede3285d68ab06e391c761a03a |
| regras/estilo_banca.md (catálogo em disco: **v1.1.3**, linha 2) | 9f9237f5f9828b77d5ab805849a7a14af13fb28fcc1c985fe462ec1027684caf |
| saida/banco/estilo_DA_reforco_leva3.md (modelo de forma e critérios) | f7d0181287455232317366ed63961e0521400b1b0f7dcfddb1ce2d0b569313e4 |
| saida/gcb/normativo_cache/CF_1988_compilada_2026-10-20.txt (D2-R05, linha 630; D2-R14, linha 649) | d6580cb3…cb51d (SHA-256 da ficha 10.4.2; não refeito) |
| saida/gcb/normativo_cache/Decreto_9830_2019_2026-10-20.txt (D3-R54, linha 109; art. 12, § 1º, linha 96) | ae022402…b232 (SHA-256 da ficha 10.4.2; não refeito) |
| saida/gcb/normativo_cache/Lei_10406_2002_CodigoCivil_compilada_2026-10-20.txt (D3-R56, linha 1835) | 97e0ffaa…a828 (SHA-256 da ficha 10.4.2; não refeito) |

**Script:** python3 -I, somente leitura, sobre o arquivo da leva (seções 1 e 2). Extrai enunciados e gabaritos e conta abertura × gabarito, fecho "é correto afirmar que" × gabarito, a fórmula "Nessa situação, nos termos d…", marcadores (absolutos, "mas não", ", e não", "mero", "por si só", "simples", "pois", "mesmo que", "prioritariamente"), extensão, e as ocorrências dos trechos "antes" e "depois" da seção 5. As contagens de folha fechada e de moldura acumulada não foram refeitas. Vêm da seção 4 do arquivo da leva e são matéria do R1.

**Conferência por script (leva 4, 28 itens):** "Considere que" 6 C / 5 E; declarativos 9 C / 8 E; fecho "é correto afirmar que" 0 C / 0 E; fórmula "Nessa situação, nos termos d…" 3 C / 1 E (D3-R53; D2-R03, D2-R08, D2-R19). Conferem com a seção 4.6 do arquivo e com a ficha 10.4.6. Único absoluto nos enunciados: "sempre que" (D2-R15, C, letra da fonte). Nenhum "mas não", ", e não", "mero", "por si só", "simples", "pois", "mesmo que" ou "prioritariamente".

**Critérios de estilo:** os mesmos das levas 1 a 3 (estilo da leva 3, seção 0):
- comando C/E;
- uma afirmação, com um só ponto de erro;
- troca real e única;
- nenhuma pista de forma;
- extensão dentro da faixa da base (estilo_banca v1.1.3, seção 4: C de 8 a 65 palavras; E de 19 a 62);
- registro formal;
- termo absoluto só quando for letra da fonte ou a própria troca;
- moldura que não decide o gabarito (R1 da T-122);
- risco de "mais de uma interpretação" (estilo_banca, seção 5.3, anulados da ANM);
- L3-1 a L3-5 (ficha 9.3), L4-1 a L4-4 e itens 5 e 6 da ficha 10.2.

Vereditos:
- **NÃO CONFORME:** dois pontos de erro, pista que entrega o gabarito, E decidido pela moldura, ou gabarito que só se sustenta com escolha da produção.
- **AJUSTE (texto):** defeito sanável por substituição exata, sem mudar gabarito, ponto, mecanismo nem a natureza da troca.

## 1. Amostra

Fixada pela ficha, seção 10.4.8, antes da produção. Sem sorteio.

| id | folha | lote | gab. | formato | moldura | aderência | o que cobre |
|---|---|---|---|---|---|---|---|
| D2-R05 | 3.1 | D2 | E [TS] | APL | S (órgão/servidor do Poder Legislativo da União) | direta | E com moldura; CF, art. 37, § 13 |
| D2-R14 | 3.2 | D2 | E [TS] | SUJ | N | direta | E com troca de instrumento (lei → edital), na folha com D2-16 e D2-20 |
| D3-R54 | 6.2 | D3 | E [TS] | DEF | N | direta | E sobre o Decreto 9.830, art. 14 (alerta C6) |
| D3-R56 | 6.2 | D3 | C | SIT | N | parcial | C com "Considere que" (L4-2); CC, art. 949 |

**Composição exigida (ficha, seção 5): CONFERE.**
- Tamanho: ⌈10% de 28⌉ = 3; foram designados 4.
- Ao menos 1 E com moldura: D2-R05.
- Os dois lotes da leva: D2 (D2-R05, D2-R14) e D3 (D3-R54, D3-R56).
- Ao menos 1 C: D3-R56.
- Ao menos 1 parcial: D3-R56.

## 2. Vereditos por item

Palavras: só o enunciado, sem o comando.

| id | gab. | mecanismo | trecho decisivo | palavras | veredito | motivo |
|---|---|---|---|---|---|---|
| D2-R05 | E [TS] | E3 (dispensa um dever existente: a manutenção da remuneração; declarado e confirmado) | "passando a perceber a remuneração desse cargo" | 67 | **AJUSTE (texto)** | Gabarito, ponto e troca corretos. A CF, art. 37, § 13, diz "mantida a remuneração do cargo de origem" (cópia, linha 630), e o item põe a do cargo de destino. É uma troca só, por contradição expressa, na mesma posição da letra. O E está na letra, e a moldura não decide: o cenário só põe o servidor em órgão do Poder Legislativo da União. A justificativa, linha 2, registra isso. Não há absoluto: "poderá" é letra da fonte. Não há fórmula "nos termos d…" ("Nessa situação, de acordo com a Constituição Federal"; seção 7.4.3). O cenário é distinto do D2-R03 e do D2-R10 (L3-3). **Defeito (extensão fora da faixa da base):** com 67 palavras, o item é o mais longo da leva e passa do teto de E da base (62; estilo_banca, seção 4). Os outros 27 itens estão entre 14 e 60. O excesso vem de duas condições verdadeiras e longas da letra antes da troca ("cujas atribuições e responsabilidades sejam compatíveis com a limitação" e "desde que possua a habilitação e o nível de escolaridade exigidos para o cargo de destino"). Isso alonga o E com moldura, a mesma assimetria de extensão que o estilo da leva 1 registrou (seção 4: moldura concentrada em E). O AJ-L4-E1 tira a segunda condição, que é acessória e não sustenta a troca, e nomeia o cargo no fecho ("a remuneração do cargo de destino"). O resultado tem 53 palavras. Omitir uma condição verdadeira num E não cria segundo ponto de erro (C6, "incompleto não é errado", estilo_banca 3.12). Com o AJ, o fecho fica literal ao campo Troca ("→ passando a perceber a remuneração do cargo de destino"), que hoje difere do enunciado ("desse cargo"). Ponto, gabarito, mecanismo, formato APL, moldura S (mesmo tipo), aderência e abertura CQ ficam iguais. A justificativa, linhas 1 e 2, continua verdadeira sem mudança. **Observação (moldura na leva):** os 3 itens com moldura da leva são E (D2-R03, D2-R05, D2-R10; 0 C / 3 E). É o plano da cota (ficha 10.4.6), e a 3.1 fechada fica com moldura 2 C / 3 E (40,0%; dado da ficha, não refeito). A nota (x) já leva os três ao teto de C com moldura por simulado. |
| D2-R14 | E [TS] | E3 (troca da condição da norma: o instrumento; declarado e confirmado) | "o edital do concurso pode estabelecer requisitos diferenciados de admissão" | 34 | **CONFORME** | Uma afirmação e uma troca ("a lei" → "o edital do concurso"), sobre texto que de resto é literal da CF, art. 39, § 3º ("podendo a lei estabelecer requisitos diferenciados de admissão quando a natureza do cargo o exigir"; cópia, linha 649). O E está na letra: o parágrafo atribui a possibilidade à lei. O item não diz que o edital "não pode" nada. Não traz "por si só" nem outro qualificador (L3-5). Não enumera os incisos do art. 7º. Não há absoluto (L3-2). O ator posto no lugar do sujeito da letra é plausível à primeira leitura, porque o edital é o lugar onde os requisitos aparecem na prática (ficha 10.2, item 6). É isso que dá discriminação ao item, e não é pista. **Pista de forma, conferida:** "edital" aparece na leva em 1 C (D2-R02, "prazo improrrogável previsto no edital") e 1 E (D2-R14). O par "lei" × outro instrumento na 3.2 fechada é 3 C / 3 E pela ficha (10.4.4; D2-11, D2-14, D2-R12 / D2-16, D2-20, D2-R14; não refeito). Não há série "instrumento trocado → E" que o item agrave, e a nota (am) já separa os três E no simulado. **Observação 1 (risco residual de interpretação, não reprova):** "estabelecer" pode ser lido como "fazer constar", e todo edital reproduz requisitos. Mas o item atribui ao edital o poder de estabelecer requisitos "diferenciados" quando a natureza do cargo o exigir, que é a competência que o parágrafo dá à lei. A leitura do E é a da letra, e o risco fica abaixo do dos anulados da ANM (estilo_banca 5.3). A nitidez é matéria do R1. **Observação 2 (redação):** "requisitos diferenciados de admissão de servidores ocupantes de cargo público" junta o sujeito da primeira oração do parágrafo ("Aplica-se aos servidores ocupantes de cargo público…") com o objeto da segunda. Fica um pouco pesado, mas a leitura é única. Sem AJ. Registro formal. |
| D3-R54 | E [TS] | E1 (troca de conceito vizinho: erro grosseiro → culpa; declarado e confirmado) | "depende de o agente público ter agido com dolo ou culpa em suas decisões ou opiniões técnicas" | 42 | **AJUSTE (texto)** | O ponto e a troca estão corretos. O Decreto 9.830, art. 14, diz que o regresso "somente será exercido na hipótese de o agente público ter agido com dolo ou erro grosseiro" (cópia, linha 109). O item nomeia o Decreto e o alcance ("no âmbito do Poder Executivo federal"), não tem moldura e não apresenta o artigo como regra do § 6º para todos os entes (C6). Também não usa "somente", "apenas" ou "só", como a ficha 10.4.4 manda. **Defeito (risco de "mais de uma interpretação", estilo_banca 5.3; é a dúvida (i) do bloco à GCB):** para cumprir a ficha, a produção trocou o "somente será exercido na hipótese de" da letra por "depende de". Mas "depende de X" diz que X é condição necessária. Lido assim, o item afirma que o regresso exige dolo ou culpa. O mesmo Decreto define o erro grosseiro como o "praticado com culpa grave" (art. 12, § 1º; cópia, linha 96). Então a exigência de dolo ou culpa é verdadeira como condição necessária: quem agiu com erro grosseiro agiu com culpa. Nessa leitura, um recurso pode sustentar C. O E só fica certo na leitura de condição suficiente ("basta a culpa"), que o verbo "depender" não exprime. Há um agravante: a leitura que leva ao C usa a relação entre "dolo ou erro grosseiro" e "dolo ou culpa", que o alerta C6 manda não afirmar ([SEM FONTE]). Assim, o gabarito do texto atual depende de matéria que a ficha deixou fora do item. **Correção:** o AJ-L4-E2 volta à moldura da letra sem o absoluto ("será exercido na hipótese de o agente público ter agido com dolo ou culpa"). O item passa a afirmar que a culpa, sem qualificação, abre o regresso, e o E fica na letra do art. 14 ("na hipótese de … dolo ou erro grosseiro"), com um só termo trocado, como no padrão E1 da base (estilo_banca 3.1). O resultado tem 45 palavras. Mecanismo (E1), ponto (A6.2-03), gabarito, Troca ("dolo ou erro grosseiro → dolo ou culpa"), formato DEF, moldura N, aderência e abertura DC ficam iguais. A justificativa, linhas 1 e 2, continua verdadeira sem mudança, e a nota da Base ("o enunciado não usa 'somente', 'apenas' nem 'só'") também. **Observação (par no art. 14):** com o AJ, o D3-R54 (E) e o D3-R51 (C, "é exercido com observância aos princípios … da proporcionalidade e da razoabilidade") têm a mesma abertura declarativa até o verbo. Um C e um E com a mesma forma não dão pista. A nota (ag) já os separa no simulado (L3-3 se aplica a cenário, e aqui não há cenário). **Se a gcb-cqfp recusar o AJ:** sem ele, o E fica discutível pela leitura de condição necessária. A decisão é do R1. |
| D3-R56 | C | C2 (reprodução próxima do texto normativo; declarado e confirmado) | "o ofensor indenizará o ofendido das despesas do tratamento e dos lucros cessantes até ao fim da convalescença, além de algum outro prejuízo que o ofendido prove haver sofrido" | 54 | **CONFORME** | O fecho é literal do CC, art. 949 (cópia, linha 1835), com a norma no fim do enunciado ("conforme o art. 949 do Código Civil"). Não usa a fórmula "Nessa situação, nos termos d…" (na 6.2, só o D3-R53 a usa; limite 1 de 2; seção 7.4.3). Abre com "Considere que" em C, como a L4-2 manda. Não há absoluto, contraste nem qualificador. Respeita o alerta C9: o sujeito é "o ofensor", e o item não diz que o Estado responde por esse artigo. O cenário não nomeia o Poder Legislativo. Registro formal ("até ao fim" é letra da fonte). A extensão está dentro da faixa de C (8 a 65). **Observação 1 (forma, a favor):** o cenário enuncia a hipótese ("lesão à saúde em decorrência de ofensa") e o fecho afirma a consequência da norma. É a forma em C da construção que a 7.4.5 e a 10.2, item 5, vedam em E. Ter essa forma em C ajuda a quebrar a leitura "cenário com a hipótese inteira → E". **Observação 2 (discriminação, não reprova):** é item de memória da letra, de pertinência parcial (C9, regime civil comum). A tentação declarada ("a indenização se limitaria às despesas de tratamento") é real, mas o item não discrimina compreensão do tema da folha. Cabe em simulado diagnóstico (nota (v)), não como âncora. **Observação 3 (cenário):** não há cenário gêmeo na folha (L3-3). "Considere que determinada pessoa…" aparece antes só no D3-R10 (6.3, "pessoa jurídica de direito público"), que diverge já na quarta palavra. |

**Taxas:**
- NÃO CONFORME: 0/4.
- AJUSTE (texto): 2/4 (D2-R05, D3-R54), sem mudança de gabarito.
- Itens decididos pela moldura: 0. O D2-R05 é o único com moldura, e o E está na letra do § 13.

## 3. Conferência de L3-1 a L3-5 (ficha 9.3), L4-1 a L4-4 e itens 5 e 6 (ficha 10.2) nos 4 itens

| regra | D2-R05 (E) | D2-R14 (E) | D3-R54 (E) | D3-R56 (C) |
|---|---|---|---|---|
| L3-1 (abertura por folha fechada) | CQ E na 3.1. A 3.1 fechada fica com CQ 4 C / 4 E (seção 4.6 do arquivo): CONFERE | DC E na 3.2. A 3.2 fechada fica com DC 6 C / 7 E, 53,8% de E: CONFERE | DC E na 6.2. A 6.2 fechada fica com DC 7 C / 7 E: CONFERE | CQ C na 6.2. A 6.2 fechada fica com CQ 3 C / 3 E: CONFERE |
| L3-2 (absoluto inserido pela troca) | sem absoluto ("poderá" é letra da fonte): não se aplica | sem absoluto: não se aplica | sem absoluto (o "somente" da letra foi tirado por ordem da ficha): não se aplica | sem absoluto: não se aplica |
| L3-3 (cenário gêmeo) | cenário distinto do D2-R03 e do D2-R10; os três só compartilham a expressão da cota: CONFERE | declarativo: não se aplica | declarativo; a abertura é igual à do D3-R51 (C), com a nota (ag): CONFERE | cenário único na folha: CONFERE |
| L3-4 ("mas não" / ", e não") | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE |
| L3-5 (qualificador minimizador) | ausente: CONFERE | ausente ("por si" só aparece na justificativa): CONFERE | ausente: CONFERE | ausente: CONFERE |
| L4-1 (fecho "é correto afirmar que" fora do D4) | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE | ausente: CONFERE. Na leva, 0/0 (script) |
| L4-2 (abertura da 6.2) | não se aplica | não se aplica | DC, como no plano: CONFERE | CQ com gabarito C, como no plano: CONFERE |
| L4-3 (referente de rol, E6) | não é E6: não se aplica | não é E6: não se aplica | não é E6: não se aplica | C: não se aplica |
| L4-4 (condição inventada sobre hipótese autônoma) | E3 de efeito, não de condição: não se aplica | E3 de instrumento: não se aplica | E1: não se aplica. O princípio vizinho, de nomear pelo elemento e não por verbo ou rótulo de sentido amplo, está no AJ-L4-E2 | C: não se aplica |
| 10.2, item 5 (hipótese inteira negada no fecho) | o cenário traz a limitação, e o fecho troca o efeito sem negar: CONFERE | não se aplica | não se aplica | é C; ver obs. 1: CONFERE |
| 10.2, item 6 (SUJ E com ator plausível) | não é SUJ | o edital é plausível e a fonte o pressupõe: CONFERE | não é SUJ | não é SUJ |

As conferências de folha fechada vêm da seção 4.6 do arquivo da leva (linha 788) e não foram refeitas aqui. As de leva foram refeitas (seção 0).

## 4. Leitura fora da amostra (sem veredito, fora da taxa)

- **Extensão na leva (script):** C média 35,9 (de 17 a 60); E média 39,0 (de 14 a 67). Dois itens ficam fora da faixa de E da base (19 a 62):
  - D2-R05 (67), da amostra, com o AJ-L4-E1;
  - **D2-R11 (14), fora da amostra.** O texto é "Segundo a Lei nº 8.112/1990, a investidura em cargo público ocorrerá com a nomeação.". É mais curto que o menor E da base. Um E curto e seco, com a troca no último termo, é a forma mais fácil de reconhecer. É matéria do R1, ou de registro na reconciliação. Aqui não há veredito nem texto.
- **Moldura na leva:** 0 C / 3 E (D2-R03, D2-R05, D2-R10), como no plano (ficha 10.4.6). Pela regra ingênua "moldura → E", a leva acerta 3 de 3. O equilíbrio é o do DA acumulado e da 3.1 fechada (2 C / 3 E, dado da ficha), não o da leva. Sem efeito nos AJ.
- **Fórmula "Nessa situação, nos termos d…":** 4 dos 11 CQ (3 C / 1 E). Na 6.2, 1 de 2; no D2, 3 de 9, dentro da orientação de no máximo 4.

## 5. Textos exatos (AJ de v1; seguem com os AJ do R1 para a v2 e são conferidos no R2)

Formato da ficha, seção 4.3. Cada "antes" ocorre exatamente 1 vez em saida/gcb/DA_reforco_leva4_v1.md, e cada "depois" 0 vez, conferido por script.

`AJ-L4-E1 | D2-R05 | enunciado (seção 1) | substituir: «ele poderá ser readaptado para cargo cujas atribuições e responsabilidades sejam compatíveis com a limitação, desde que possua a habilitação e o nível de escolaridade exigidos para o cargo de destino, passando a perceber a remuneração desse cargo.» | por: «ele poderá ser readaptado para cargo cujas atribuições e responsabilidades sejam compatíveis com a limitação, passando a perceber a remuneração do cargo de destino.»`

`AJ-L4-E2 | D3-R54 | enunciado (seção 1) | substituir: «depende de o agente público ter agido com dolo ou culpa em suas decisões ou opiniões técnicas.» | por: «será exercido na hipótese de o agente público ter agido com dolo ou culpa em suas decisões ou opiniões técnicas.»`

**Efeito dos dois AJ:**
- Ficam inalterados: gabarito (E; E), ponto (CF, art. 37, § 13; A6.2-03), mecanismo (E3; E1), formato (APL; DEF), moldura (S, mesmo tipo; N), aderência (direta; direta), abertura (CQ; DC), campo Troca e [TS].
- O D2-R05 vai de 67 para 53 palavras, e o D3-R54 de 42 para 45.
- Nenhum campo da seção 2 precisa de harmonização. A Troca do D2-R05 passa a coincidir literalmente com o fecho, e a do D3-R54 não muda.

**Contagens a refazer na v2 (por script, seção 4 do arquivo):** só a extensão. Abertura, fecho, fórmula, moldura (o D2-R05 mantém "órgão do Poder Legislativo da União") e absolutos ficam iguais. Nenhum dos dois textos novos tem "somente", "apenas" ou "só".

**O que o R2 confere:**
1. Cada "antes" com 1 ocorrência na v1 e cada "depois" aplicado literalmente na v2.
2. Nenhum outro campo dos dois blocos muda.
3. Lidos inteiros, os enunciados resultantes mantêm o E pela letra e não criam pista:
   - CF, art. 37, § 13: "mantida a remuneração do cargo de origem";
   - Decreto 9.830, art. 14: "somente será exercido na hipótese de o agente público ter agido com dolo ou erro grosseiro".

**Se a gcb-cqfp recusar algum AJ:** o item segue para o R1 como está na v1.
- AJ-L4-E1: o defeito é só de extensão.
- AJ-L4-E2: o defeito é de risco de recurso sobre o gabarito (seção 2), e a decisão é do R1.

## 6. Recomendações para as próximas levas

Texto exato para a gcb-gerencia incluir na ficha da leva 5 ou nas seguintes, se aceitar. Nenhuma tem efeito sobre os 28 itens da leva 4 além dos AJ da seção 5.

- **L5-1 (extensão do E com moldura):** "Item E não passa de 62 palavras no enunciado (teto de E da base, estilo_banca, seção 4). Quando a letra traz mais de uma condição verdadeira antes do elemento trocado, o item mantém só a que dá contexto à troca. A seção 4 do arquivo da leva lista por script todo item fora da faixa da base (C de 8 a 65; E de 19 a 62)."
- **L5-2 (absoluto da letra retirado de E com outra troca):** "Quando a ficha manda tirar do E o absoluto da letra ('somente será exercido na hipótese de'), o item mantém a moldura do dispositivo sem o absoluto ('será exercido na hipótese de'), e não um verbo de condição necessária ('depende de', 'exige', 'pressupõe'). Isso vale sempre que o termo posto pela troca puder abranger o da letra (culpa × erro grosseiro; D3-R54, AJ-L4-E2)."
- **À GBQ (montagem, T-119 e T-123):** o D3-R56 e os demais parciais da 6.2 ficam só em simulado diagnóstico (nota (v)), como a ficha já prevê. Os três E com moldura da 3.1 contam para a nota (x). Sem texto novo.

## 7. Registros

1. **Rito:** auditoria sobre a v1, em paralelo ao R1, como a ficha 9.3, item 6, e a 10.4.8 determinam. Os AJ seguem para a v2 com os do R1 e são conferidos no R2. Nenhuma errata pós-R2 (seção 7.6) é proposta.
2. **Versão do catálogo:** o despacho cita "regras/estilo_banca.md (versão em disco)". O arquivo em disco é a **v1.1.3** (linha 2; SHA-256 na seção 0), a mesma das auditorias das levas 1 a 3. Os mecanismos citados (C2, C6, E1, E3) e as seções 3.1, 3.3, 3.8, 3.12, 4 e 5.3 são os da v1.1.3. Nada foi alterado no catálogo.
3. **Nome do arquivo:** o da ficha 10.4.8 e 7.5 (saida/banco/estilo_DA_reforco_leva4.md).
4. **Fidelidade às bases:** só se leram as linhas das cópias em saida/gcb/normativo_cache/ correspondentes aos 4 itens, para confirmar o trecho decisivo:
   - CF, art. 37, § 13, e art. 39, § 3º;
   - Decreto 9.830, arts. 12 e 14;
   - CC, art. 949.

   O art. 12, § 1º, do Decreto 9.830 (cópia, linha 96) não está no Adendo 2 do adendo do D3 (A2.4.6 só transcreve o art. 14). Ele é citado aqui só como razão do risco de interpretação do D3-R54, e não como base de item. A conferência das bases é matéria da gcb-cqfp e do qa-normativo-da.
5. **Escopo:** nada vai à plataforma nem à candidata. Nenhuma tarefa nova (D-COMPLEMENTOS). Nenhum gatilho em PARA_PRESIDENCIA.md. Nenhum NÃO CONFORME, e por isso nenhum GATE pela regra 6.

AVISO: os vereditos, a atribuição de mecanismo, a leitura de pista e o juízo de risco de "mais de uma interpretação" são julgamento deste agente (gbq-estilo) e exigem revisão da GBQ. As contagens de abertura, de fecho, de fórmula, de marcadores, de extensão e de ocorrência dos trechos de AJ vêm de script sobre o arquivo gravado (python3 -I, somente leitura), com revisão manual dos 4 itens. As contagens de folha fechada, de moldura acumulada e do par "lei" na 3.2 foram tomadas da seção 4 do arquivo da leva e da ficha, sem refazer. Com n pequeno (amostra de 4; recortes de 1 a 28 itens), nenhuma associação é regra. A tabela serve para corrigir vieses de redação, nunca para prever gabarito.

FIM DA AUDITORIA DE ESTILO — LEVA 04 — REFORÇO DA
