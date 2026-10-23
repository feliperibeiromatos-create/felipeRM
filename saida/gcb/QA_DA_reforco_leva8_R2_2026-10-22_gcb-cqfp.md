# QA_DA_reforco_leva8_R2_2026-10-22_gcb-cqfp.md — T-116 — 2026-10-22 — gerado por gcb-cqfp

# PARECER QA R2 (ÚLTIMA RODADA) — REFORÇO DA, LEVA 8 (v2) — ciclo s16c6
A gcb-cqfp (opus) faz este QA de forma independente. Ela não produziu o texto revisado e não reescreve itens. Nenhum outro arquivo do repositório foi alterado; não houve commit nem push.

O exame segue:
- a ficha, seção 4.3: "o R2 confere cada AJ aplicado literalmente e examina só o que a v2 mudou além dos AJ";
- a ficha, seção 9.3, item 6 (os AJ de estilo seguem com os do R1 para a v2 e são conferidos no R2), e a seção 14.2, itens 1 (L3-3 recontada quando o AJ muda a abertura) e 2 (justificativa sem afirmação sem fonte);
- o R1, seção 9, item 1 (aplicar o AJ-1; qualquer outra mudança é examinada no R2), e a auditoria de estilo, seção 5 (AJ-L8-E1 e AJ-L8-E2, com o efeito previsto sobre o prefixo);
- a ficha, seções 7.6, 10.3, 11.3, 12.3, 13.3 e 14.3 (o que é registro e o que é errata depois do R2).

Pontos examinados:
- os 3 AJ (AJ-1, D4-R47; AJ-L8-E1, D4-R35; AJ-L8-E2, D4-R48), por substituição exata;
- os 3 itens alterados, lidos inteiros, com o gabarito e a pista de forma depois da nova abertura;
- os 27 itens não alterados;
- a Resposta à R1 (R.1 a R.6);
- a seção 4 refeita, em especial a L3-3 recontada e a abertura × gabarito;
- toda mudança fora dos itens, contra a lista da R.4;
- a frase "49 verificações automáticas" do bloco 5 e o registro da produção sobre ela.

## 0. Objeto, entradas e método
| objeto | SHA-256 (em disco, 22/10/2026) |
|---|---|
| saida/gcb/DA_reforco_leva8_v2.md (objeto do R2; 30 itens; 169.034 bytes; 1.011 linhas LF; 0 CR) | 1fdce9bde3393b445cabd75d50064fb2a2fdde103c03415dc82256c203bf6f2c (= despacho) |
| saida/gcb/DA_reforco_leva8_v1.md (objeto do R1; base do diff; 935 linhas) | 1b9903d5aa0c3f049a8aa361c2fda8c62b03b118272f6ef96df79907e50d8ecf (= despacho e R1) |
| saida/gcb/QA_DA_reforco_leva8_R1_2026-10-22_gcb-cqfp.md | 1d8a9e3e5e5e51d5778e8bbf87052126e67ef21dcecb31317afa17aa2f71fc42 (= despacho) |
| saida/banco/estilo_DA_reforco_leva8.md | e5c44b7720c2bbe14d7e8537e48838e083a303f25c2d6bcf5c8ab19a01e56087 (= despacho) |
| saida/gcb/DA_reforco_ficha_2026-10-20.md | 539f22327fb4ec7914a3cae6f2ffe22cdc89c7f873f5ff9be6bb1ad242b0eac8 (= despacho) |
| saida/pacote/pacote.json v1.13 (canônicos das folhas 8.2, 8.3 e 9.1) | 82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240 |
| modelo de forma: saida/gcb/QA_DA_reforco_leva7_R2_2026-10-22_gcb-cqfp.md | b438aceca335fcd117ef5fcc88125695d055f230b06890e189cebaad0488c705 |

Lidos também: da ficha, as seções 4, 7.4, 7.6, 9.3, 10.2, 10.3, 11.2, 11.3, 12.2, 12.3, 13.2, 13.3, 14.1 a 14.6 (inclusive 14.4.4, 14.4.6 a 14.4.9); regras/ e CLAUDE.md; as levas 1 a 7 (v2), só para conferir que nenhuma tem item nas folhas 8.2, 8.3 e 9.1 (nenhuma tem) e para a moldura do D4 nas levas 1 e 2.

Método: scripts próprios em python3 -I, somente leitura, no scratchpad da sessão (…/scratchpad/qa8r2/), fora do repositório.
- (a) `diff` v1 × v2, lido linha a linha: 12 blocos (l. 1; 3; 5; 8–82 inseridas; 113; 141; 460; 909; 911; 972; 977; 982). Os enunciados do D4-R35 e do D4-R48 foram comparados também por caractere (SequenceMatcher).
- (b) aj.py: os 3 AJ, copiados por expressão regular do R1 (seção 5) e do estilo (seção 5), aplicados em memória à v1 por `str.replace(antes, depois, 1)`; resultado comparado com a v2 por id (seções 1 e 2), por seção (3 a 6) e linha a linha fora da "Resposta à R1".
- (c) pref.py e fecho.py: sobre a v1 e a v2, com os 30 canônicos das três folhas (pacote.json v1.13), prefixo comum (L3-3) de todos os pares com item da leva, abertura × gabarito na leva e nas folhas fechadas, forma de abertura e verbo da moldura e fecho × gabarito nos 24 itens com moldura do D4 (12 canônicos, 8 das levas 1 e 2, 4 da leva 8), extensão e sequência de gabarito.
- (d) sl8.py: aplicação simulada, só para registro, das sugestões S-L8-1 e S-L8-2 do estilo sobre a v2 (seção 9).

**Rede — reabertura no planalto.gov.br (checklist, item 3; ficha 11.6).** Comando: `curl -sS -m 120 -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36" -o <arquivo> -w "%{http_code} %{size_download}" <URL>`. HTML só no scratchpad. Texto extraído por html.parser (sem script, style nem tachado), espaços normalizados. O www.gov.br não foi pedido (recusado pela política de rede; despacho); nenhum dos 3 itens alterados depende do Guia.

| hora (UTC) | URL | HTTP | bytes (= R1, seção 1) | SHA-256 do HTML |
|---|---|---|---|---|
| 2026-10-23T02:12:09Z | https://planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l11079compilado.htm (N5; D4-R35) | 200 | 74.422 | 1acdcf07e3978a10bf9f3ab0121749dfdb1ef6bd165a63a3996479028a7e3fa6 |
| 2026-10-23T02:12:10Z | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13460.htm (N10; D4-R47, D4-R48) | 200 | 69.906 | a4f0eef97eddf57c5846e69fb4e188e1f6ba52f0ca6cdea37a5112df2bf8838d |
| 2026-10-23T02:12:12Z | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/decreto/d9203.htm (N1; canônicos D4-14 e D4-19 dos pares de prefixo) | 200 | 86.892 | 60345f2e074f0ce72f3d912a6e63c717f61564ba4c03ba581aaabaeaa814de40 |

As horas em UTC caem em 22/10/2026, 23h12 no horário de Brasília. O SHA do HTML muda a cada download (adendo do D4 de 22/10, seção 1); a comparação é sobre o texto.
- **Lei 11.079:** «É vedada a celebração de contrato de parceria público-privada» 1 vez; «que tenha como objeto único» 1; «a execução de obra pública» 1; «admitida» 0. O § 4º, III, lido no contexto: «III – que tenha como objeto único o fornecimento de mão-de-obra, o fornecimento e instalação de equipamentos ou a execução de obra pública».
- **Lei 13.460:** «A participação do usuário no conselho será considerada serviço relevante e sem remuneração» 1 vez; «remunera» 2 vezes (essa e «sem remuneração» na definição de agente público, art. 2º, IV; nenhuma dá remuneração ao conselheiro). «A aplicação desta Lei não afasta a necessidade de cumprimento do disposto» 1; «na Lei nº 8.078» 1; «quando caracterizada relação de consumo» 1.
- **Decreto 9.203:** «IV - articular instituições» 1; «VIII - manter processo decisório orientado pelas evidências» 1 (os pontos do D4-14 e do D4-19, citados na L3-3 da v2).

A reabertura é conferência, não base. A Base dos itens continua a consulta registrada (ficha 11.6).

## 1. Veredito geral
- **Leva: APROVADA.**
- Os 3 itens alterados: **D4-R35 APROVADO**, **D4-R47 APROVADO**, **D4-R48 APROVADO** (seção 3).
- Os 27 itens não alterados ficam APROVADOS, como no R1. São idênticos aos da v1 no enunciado e no bloco.
- **Reprovação final: 0/30 = 0,0%** (limite 30%). No acumulado do rito (R1 + R2), também 0/30. Sem GATE.
- Itens aprovados no R1 e mudados sem pedido: **nenhum**.
- Conferências do despacho:
  - (1) os 3 AJ por substituição exata, sem efeito colateral: **CONFERE**.
  - (2) os 3 itens alterados (gabarito firme; nenhuma pista nova com a abertura nova): **CONFERE**.
  - (3) 27 itens idênticos aos da v1: **CONFERE**.
  - (4) Resposta à R1: **CONFERE**, com 2 ressalvas de registro (seção 7).
  - (5) seção 4 refeita, inclusive a L3-3 recontada e a abertura × gabarito: **CONFERE** (seção 5).
  - (6) toda mudança fora dos itens declarada na R.4: **CONFERE** (seção 6).
  - (7) frase "49 verificações automáticas" do bloco 5 e o registro da produção: **NÃO CONFERE (de registro)** (seção 8). Sem efeito em item, gabarito, contagem ou aprovação.
- **NÃO CONFERE: 1** (o item (7), registro sem errata). Os outros registros estão na seção 10.

## 2. Conferência (1) — os 3 AJ aplicados por substituição exata, sem efeito colateral
Textos dos AJ: R1, seção 5 (l. 143), e estilo, seção 5 (l. 155 e 157). O R1 e o estilo não pedem o mesmo texto; a regra de texto igual (ficha 11.3) não se aplica.

| AJ | origem | id | campo | "substituir" na v1 | "por" na v1 | "substituir" na v2 | "por" na v2 | veredito |
|---|---|---|---|---|---|---|---|---|
| AJ-1 | R1 | D4-R47 | Justificativa (linha 2) | 1 | 0 | 1, só na R.2 (l. 15), como citação | 2: l. 460 (item) e R.2 (l. 15) | **APLICADO** |
| AJ-L8-E1 | estilo | D4-R35 | enunciado (seção 1) | 1 | 0 | 1, só na R.2 (l. 16), como citação | 3: l. 113 (item), R.2 (l. 16) e 4.6, L3-3 (l. 909, dentro do prefixo citado de 110 caracteres) | **APLICADO** |
| AJ-L8-E2 | estilo | D4-R48 | enunciado (seção 1) | 1 | 0 | 1, só na R.2 (l. 17), como citação | 2: l. 141 (item) e R.2 (l. 17) | **APLICADO** |

- Aplicados os 3 AJ em memória à v1, os 30 enunciados e os 30 blocos ficam iguais aos da v2 (30/30 e 30/30). Fora da "Resposta à R1", o texto em memória difere da v2 só nas l. 1, 3, 5, 909, 911, 972, 977 e na linha nova 982, todas declaradas na R.4 (seção 6).
- Comparação por caractere:
  - D4-R35: sai « um expositor» depois de "Considere que"; «sustente» passa a «um expositor afirme». O resto do enunciado, do «que, nos termos da Lei nº 11.079/2004» ao fecho «Nessa situação, a afirmação do expositor é correta.», fica igual. 48 palavras antes e depois.
  - D4-R48: «durante» passa a «em». Nada mais muda. 44 palavras antes e depois.
  - D4-R47: no bloco, só a linha «- Justificativa (linha 2):» muda («a lei especial do usuário» → «a Lei 13.460»).
- Efeito colateral no texto: **nenhum**. Os blocos da seção 2 do D4-R35 e do D4-R48 são idênticos aos da v1 (o bloco não repete o enunciado). No bloco do D4-R47 ficam iguais: cabeçalho com [TS], itemEdital, Ponto, Formato PAR, Moldura N, Aderência direta, Gabarito E, Justificativa (linha 1), Tipo de base, Base, Mecanismo E2, Troca, Difere de e Marcas (TS=sim).
- Efeito previsto e verificado: só o da L3-3, que o estilo previu (seção 5 do estilo) e a v2 recontou (seção 5 abaixo).

## 3. Veredito dos 3 itens alterados
| id | folha | gab. | [TS] | enunciado da v2 (lido inteiro) | base (Anexo/adendo; página de 22/10) | veredito |
|---|---|---|---|---|---|---|
| D4-R35 | 8.2 | E | sim | «Considere que, em audiência pública de comissão da Câmara dos Deputados, um expositor afirme que, nos termos da Lei nº 11.079/2004, é admitida a celebração de contrato de parceria público-privada que tenha como objeto único a execução de obra pública. Nessa situação, a afirmação do expositor é correta.» | Lei 11.079, art. 2º, § 4º, caput e III (Anexo N do D4, 4.2): «É vedada a celebração de contrato de parceria público-privada: […] III – que tenha como objeto único […] a execução de obra pública»; 1 ocorrência de cada trecho na página de 22/10 | **APROVADO** |
| D4-R47 | 8.3 | E | sim | «Nos termos da Lei nº 13.460/2017, a aplicação da lei afasta a necessidade de cumprimento do disposto na Lei nº 8.078/1990 quando caracterizada relação de consumo.» (igual à v1) | Lei 13.460, art. 1º, § 2º, caput e II (Anexo N do D4, 4.7): «A aplicação desta Lei não afasta a necessidade de cumprimento do disposto: […] II - na Lei nº 8.078, […] quando caracterizada relação de consumo.»; 1 ocorrência na página de 22/10 | **APROVADO** |
| D4-R48 | 8.3 | E | sim | «Considere que, em audiência pública de comissão da Câmara dos Deputados, um expositor trate dos conselhos de usuários de serviços públicos. Nessa situação, é correto afirmar que, segundo a Lei nº 13.460/2017, a participação do usuário no conselho é considerada serviço relevante e remunerado.» | Lei 13.460, art. 21 (adendo de 22/10, 4.4): «A participação do usuário no conselho será considerada serviço relevante e sem remuneração.»; 1 ocorrência na página de 22/10 | **APROVADO** |

Fundamentação:
1. **D4-R35 — gabarito E firme.** A afirmação julgada é a do expositor, e o fecho de acerto («a afirmação do expositor é correta») a dá por correta. A letra do § 4º, III, veda a PPP de objeto único de execução de obra pública; o expositor a diz admitida. É inversão de polaridade (E2), um elemento, por contradição expressa. «admitida» ocorre 0 vez na lei. Os §§ 1º e 2º admitem obra como parte da concessão, não como objeto único, e o item mantém «objeto único» (letra; não é a troca). A abertura nova só mexe na moldura: «afirme» substitui «sustente» como verbo do expositor, sem mudar o que ele afirma. O gabarito não depende da moldura.
2. **D4-R48 — gabarito E firme.** O fecho neutro põe a afirmação julgada fora da fala do expositor («é correto afirmar que, segundo a Lei nº 13.460/2017, …»). A letra do art. 21 diz «sem remuneração»; o item diz «remunerado». É uma troca, por contradição expressa. A Lei 13.460 não tem outro dispositivo que remunere o conselheiro: «remunera» ocorre 2 vezes na página, ambas como «sem remuneração». «durante» → «em» não toca a proposição.
3. **D4-R47 — gabarito E firme e justificativa sem afirmação sem fonte (ficha 14.2, item 2).** O enunciado é o da v1, aprovado no R1. A linha 1 reproduz a letra do § 2º, II. A linha 2 nova («O item troca “não afasta” por “afasta”; a tentação é supor que a Lei 13.460 exclua a Lei 8.078/1990 quando há relação de consumo.») descreve a troca pelo próprio item e só nomeia as duas leis do trecho da Base. Não afirma fato, valor ou norma fora da Base. O rótulo sem fonte («lei especial do usuário») saiu. A regra da 14.2, item 2, está cumprida.
4. **Nenhuma pista nova com a abertura nova (D4-R35 e D4-R48).** Contagem por script nos 24 itens com moldura do D4 (12 canônicos, 8 das levas 1 e 2, 4 da leva 8):
   - Forma da cota («Considere que, em audiência pública de comissão da Câmara dos Deputados, um expositor …»): v1 14 C / 6 E → v2 **14 C / 8 E** (63,6% de C). Variantes: v1 0 C / 4 E → v2 **0 C / 2 E** (D4-R42, D4-R52). A pista que o estilo apontou (variante só em E) **sai** dos dois itens alterados.
   - Verbo da moldura, na forma da cota: «afirme» 13 C / 5 E (D4-R35 e os E da leva 1); «trate» 1 C / 3 E (D4-R20 C; D4-R08, R17, R48 E). Com as variantes, «afirme» fica em 13 C / 6 E (D4-R52) e «trate» em 1 C / 4 E (D4-R42). O AJ-L8-E2 não muda o verbo: só troca «durante» por «em». «sustente», que só ocorria no D4-R35, saiu.
   - Fecho: o do D4-R35 («a afirmação do expositor é correta») ocorre 4 C / 6 E no D4 com moldura; não marca gabarito. O fecho neutro do D4-R48 é o da ficha 14.4.4 (registro L8-3 do estilo, para a leva 9). Nenhum dos dois fechos mudou.
   - Nas folhas fechadas, o D4-R35 abre como o D4-14 (C), e o D4-R48 como o D4-19 e o D4-26 (C). Abrir como os C da folha é o que desfaz a pista; o prefixo comum que isso cria é tratado na seção 5.
5. **Forma.** Os três continuam declarativos ou CQ como antes (D4-R35 e D4-R48 CQ; D4-R47 declarativo). Sem negação frontal, sem contraste novo, sem absoluto inserido. Formato, moldura, aderência e mecanismo iguais aos do bloco. Extensão: 48, 26 e 44 palavras (faixa de E de 19 a 62).
6. **Estilo Cebraspe:** "Julgue o item" cabe ao caderno; cada um é afirmação única, julgável pela letra, sem generalização injustificada. Nenhuma norma interna, regimento ou prática real da Câmara (ficha 4.1, item 5): a audiência só situa a cena.

## 4. Conferência (3) — os 27 itens não alterados
**CONFERE.** Na comparação por id, 28 enunciados (seção 1) e 29 blocos (seção 2) são idênticos aos da v1. Só o D4-R35 e o D4-R48 diferem no enunciado, e só o D4-R47 no bloco, e só pelo texto dos AJ. Os 27 itens restantes são idênticos nos dois campos. A seção 3 (proveniência) e a seção 6 são idênticas às da v1. Os 27 ficam APROVADOS, como no R1, seção 2.

## 5. Conferência (5) — seção 4 refeita contra o arquivo (script próprio sobre a v2 e a v1)
| verificação | refeito pela QA (v2) | declarado na v2 | resultado |
|---|---|---|---|
| gabarito da leva | 14 C / 16 E (46,7%); folhas 4/6, 5/5, 5/5 | igual (seção 0; R.6) | CONFERE |
| sequência de gabarito | ECEECCEEEC·CCEECECCEE·ECEECCECCE | igual à v1, à 4.3 e à ficha 14.4.7 | CONFERE |
| [TS], Troca, formatos, mecanismos, moldura, aderência, K1 a K4, absolutos, sequências | os campos de que dependem são idênticos nos 30 blocos da v1 e da v2 (seção 2); valores conferidos no R1, seção 6 | iguais à v1 (fora do diff; R.5 "não mudam") | CONFERE |
| abertura × gabarito | leva: CQ 6 C / 4 E; declarativos 8 C / 12 E. Folhas fechadas: 8.2 CQ 5/1, DC 5/9; 8.3 CQ 5/4, DC 5/6; 9.1 CQ 5/2, DC 5/8. Os dois AJ mantêm «Considere que» | iguais (R.5; 4.6 fora do diff) | CONFERE |
| extensão | D4-R35 48, D4-R48 44; E 26–58; C 20–65 | iguais (l. 919; R.5) | CONFERE |
| **L3-3 (prefixo comum ≥ 40)** | v1: nenhum (maior 36, D4-09 × D4-R34). v2: **3 pares** — 8.2 D4-R35 × D4-14, **110**; 8.3 D4-R48 × D4-19, **86**, e D4-R48 × D4-26, **86**. Prefixos citados na l. 909 conferem letra a letra («…um expositor afirme que, nos termos d»; «…um expositor »). Abaixo de 40: 8.2 36, 34, 34, 34, iguais aos da v1. D4-R42 e D4-R52: máximo 17 (D4-R42 × D4-R45, empatado com D4-R42 × D4-25; D4-R52 × D4-R56, empatado com D4-R52 × D4-37) | l. 909 e 911; R.5 | **CONFERE** |
| moldura da 4.6 (l. 911) | D4-R35 e D4-R48 na forma da cota; D4-R42 e D4-R52 em variante; cenários distintos até o fecho; pontos dos canônicos (Decreto 9.203, art. 4º, IV e VIII; Lei 13.460, art. 6º, I) conferidos na página reaberta | l. 911 | CONFERE |
| linha 1 / última linha | "# DA_reforco_leva8_v2.md — T-116 — 2026-10-22 — gerado por gcb-cpp" / "FIM DA LEVA 08 — REFORÇO DA" com LF | — | CONFERE |

**Leitura dos 3 pares de prefixo (despacho: se cabe nota de simulado obrigatória). Não cabe nota obrigatória, nem nota comum nova.**
- **A L3-3 não é violada.** Ela trata de cenário literal idêntico até o fecho (ficha 9.3, item 3). Nos três pares, o texto comum é só a moldura da cota. Os itens divergem antes da norma citada e muito antes do fecho:
  - D4-R35 × D4-14: «a Lei nº 11.079/2004, é admitida …» × «o Decreto nº 9.203/2017, constitui diretriz …». Os fechos também diferem: «é correta» × «corresponde ao que o decreto prevê».
  - D4-R48 × D4-19 e × D4-26: «trate dos conselhos de usuários …» × «afirme que, nos termos …».
- **Nenhum item entrega o gabarito do outro.** Esse é o critério das notas obrigatórias, como (db), (ci) e (cl).
  - O D4-14 (diretriz de articular instituições) nada diz sobre PPP.
  - O D4-19 (processo decisório orientado por evidências) nada diz sobre conselho de usuários.
  - O D4-26 (direito à participação na avaliação dos serviços) nada diz sobre remuneração do conselheiro. O par D4-R48 × D4-26 já está na nota comum (dj).
- **O prefixo comum é o efeito buscado pelo AJ.** Ele põe os E com moldura na mesma forma de abertura dos C da folha. Separá-los em simulado por nota recriaria, na montagem, a separação por forma que o AJ desfez.
- A declaração da v2 («sem nota nova de simulado (as notas (df) … e (dj) … continuam)») confere. A (df) é D4-R35 × D4-13, e não cobre o D4-14; a (dj) cobre só o D4-R48 × D4-26. Os outros dois pares ficam sem nota, e nenhuma é exigida. O "Difere de" do D4-R35 já registra o D4-14 («moldura de expositor em outra cena»).

## 6. Conferência (6) — toda mudança fora dos itens está declarada na R.4
| local (v2) | mudança (diff) | declarada na R.4? |
|---|---|---|
| l. 1 | v1 → v2 no nome do arquivo | sim, (1) |
| l. 3 | «Esta é a v1 (gcb-cpp, primeira produção da leva; despacho de origem» → «Esta é a v2 (gcb-cpp, rodada de correção: R1 com AJ-1 (D4-R47) e auditoria de estilo com AJ-L8-E1 (D4-R35) e AJ-L8-E2 (D4-R48), conforme a seção “Resposta à R1”; despacho de origem»; o resto do parágrafo é igual | sim, (2), com o texto exato |
| l. 5 | entradas: acrescidos no fim v1 (1b9903d5…ecf), R1 (1d8a9e3e…fc42) e estilo (e5c44b77…6087); valores corretos | sim, (3) (registro: o da v1 com 3 caracteres finais, seção 10, item 2) |
| l. 8–82 | seção "Resposta à R1", antes da seção 0 (l. 83) | sim, (4) |
| l. 113, 141, 460 | enunciados do D4-R35 e do D4-R48; justificativa, linha 2, do D4-R47 | são os AJ-L8-E1, AJ-L8-E2 e AJ-1 |
| l. 909 (4.6, L3-3, 1º marcador) | de "nenhum" para os 3 pares, com os prefixos citados | sim, (5)(a) |
| l. 911 (4.6, L3-3, 3º marcador) | moldura dos 4 itens reescrita; "vale para a v1" → "vale para a v2" | sim, (5)(b) |
| l. 972 (bloco 5, Arquivo) | v1 → v2 no nome | sim, (6) |
| l. 977 (bloco 5, Pistas de forma, item (7)) | "nenhum par" → "3 pares …" | sim, (7) |
| l. 982 (bloco 5, nova) | marcador "Registros do estilo da leva 8 (v2)" | sim, (8) |

- Nenhuma mudança fora da lista. O diff tem exatamente os 12 blocos da seção 0, (a). Nenhuma outra linha da seção 4 mudou, e as seções 0, 3 e 6 não mudaram: confere com a R.4 e a R.5.
- A frase "49 verificações automáticas" (l. 976) e a frase «Esta v1 não toca saida/gcb/DA_reforco_leva7_v2.md» (l. 983) não mudaram. Por isso não estão na R.4, o que está correto. A segunda é tratada na R.3, item 4. A primeira não é tratada em parte alguma do arquivo (seção 8).

## 7. Conferência (4) — Resposta à R1
**CONFERE**, com 2 ressalvas de registro.
- **R.1:** os números do R1 (29 / 1 / 0; 0,0%; 8 de 8; 15 pontos aceitos, 14 diretos e 1 parcial) e do estilo (5 itens; 3 CONFORMES; 2 AJUSTE; 0 NÃO CONFORME) estão corretos.
- **R.2:** os 3 AJ estão transcritos com o texto exato do R1 e do estilo. "Antes" 1 e "por" 0 na v1, nos 3: confere (seção 2). As extensões (48 e 44) e os campos que "ficam iguais" conferem. O efeito na L3-3 está declarado e recontado (seção 5).
- **R.3:** (1) S-L8-1 e S-L8-2 não aplicadas: correto (ver adiante e seção 9). (2) L8-1 a L8-3 ficam para a leva 9: correto. (3) As observações do R1 sobre D4-R38, R43, R55 e R58 estão fielmente transcritas; nenhuma pedia AJ. (4) As dúvidas aceitas pelo R1 e os textos da v1 sobre a 6.3 (b) e o bloco 5 estão lidos como registro. Este R2 os lê assim. (5) A errata AJ-L7-E1 fica fora da produção: correto. (6) As notas de simulado conferem com o R1, seção 9, item 2.
- **Tabela item a item (30 linhas):** os 27 "mantido" não mudaram de fato. Os 3 "alterado" estão descritos com o AJ certo.
- **R.4:** conferida contra o diff (seção 6).
- **R.5:** conferida por recontagem (seção 5). A frase "a comparação da seção 4 da v1 com a desta v2 … mostra diferença só nos dois marcadores da L3-3" confere.
- **R.6:** conferida.
- **Ressalva 1 (R.3, item 1, "a escolha é da gcb-cqfp (R2)"):** este R2 não abre AJ sobre item não alterado (ficha 4.3: o R2 examina só os AJ e o que a v2 mudou; no máximo 2 rodadas). A escolha sobre S-L8-1 e S-L8-2 fica com a GCB (seção 9).
- **Ressalva 2:** a Resposta não registra que a frase "49 verificações automáticas" do bloco 5 ficou sem lastro na v2 (seção 8).

## 8. Conferência (7) — a frase "49 verificações automáticas" do bloco 5 e o registro da produção
**NÃO CONFERE (de registro; sem errata).**
- **O texto (l. 976, idêntico à l. 901 da v1):** «Resultado dos scripts da seção 4: 49 verificações automáticas registradas, 0 com resultado NÃO CONFERE ou equivalente.»
- **O número 49 não se reproduz a partir da seção 4, na v1 nem na v2.** A seção 4 tem, nas duas versões:
  - 38 linhas com "CONFERE";
  - 45 ocorrências de "— CONFERE" ou ": CONFERE";
  - 51 ocorrências da palavra "CONFERE";
  - 0 ocorrências de "NÃO CONFERE";
  - 2 linhas "passa" no teste de sequência.

  Nenhuma dessas contagens dá 49. A R.5 descreve o script da v2 sem número ("todas as verificações conferem (0 falha)") e diz que ele passou a recalcular a L3-3 com os pares novos. O número de verificações da v2 não é declarado em parte alguma.
- **O que continua verdadeiro:** "0 com resultado NÃO CONFERE". A seção 4 da v2 não tem nenhum NÃO CONFERE, e este R2 confere a seção 4 inteira (seção 5).
- **O registro da produção** (segundo o despacho, a frase "ficou desatualizada") procede: na v2, o número não é sustentado pelo arquivo. Mas o registro **não está no arquivo**. Nem a R.3, nem a R.4, nem a R.5, nem o bloco 5 o mencionam. A busca por "desatualiz" dá 0 ocorrências. É o caso inverso do que a R.4 cobre: uma linha que não mudou e que devia ter sido marcada. Mesmo tipo do registro do R2 da leva 7 (L3-3 da 4.6).
- **Efeito: nenhum** em item, gabarito, [TS], contagem ou aprovação. O bloco 5 não vai ao pacote.json. Depois do R2 não há v3. Vale o registro na reconciliação, sem errata (fichas 11.3, 12.3 e 14.3, precedente da L3-3 da leva 7). Texto proposto para a reconciliação, que não altera o arquivo: «na v2, o número de verificações da seção 4 não é declarado; vale "0 com resultado NÃO CONFERE", conferido pelo R2».

## 9. Abertura variante residual — D4-R42 e D4-R52 (S-L8-1 e S-L8-2 não aplicadas)
**Leitura: é só registro neste R2. Não pede AJ nem v3.**
- Situação na v2: no D4 com moldura, a variante de abertura fica em **0 C / 2 E** (D4-R42 na 8.3; D4-R52 na 9.1). Em cada uma dessas folhas fechadas, o único item com variante é E, e os C com moldura usam a forma da cota. A pista que o estilo descreveu (estilo, seção 2, D4-R35) continua, menor, nesses dois itens. Pelo próprio estilo, o n é pequeno e a variante não entrega o gabarito do item isolado, porque a troca está na letra.
- Por que não é AJ aqui:
  - (a) os dois itens foram aprovados no R1 sem AJ e não mudaram na v2;
  - (b) o R2 examina só os AJ e o que a v2 mudou (ficha 4.3), e a QA tem no máximo 2 rodadas;
  - (c) as sugestões são da gbq-estilo, fora da amostra e sem veredito (estilo, seção 4, item 4). A produção as deixou de lado por ordem do orquestrador, e a R.3 o declara.
- Saída que a ficha prevê, se a GCB quiser desfazer a pista: errata pós-R2 da seção 7.6 (texto do estilo sobre item aprovado), registrada na reconciliação e aplicada na consolidação por substituição exata com aborto, se o aceite da leva a incluir.
  - Conferência mecânica, só para registro (sl8.py, sobre a v2): o "antes" da S-L8-1 ocorre 1 vez (l. 129) e o da S-L8-2 1 vez (l. 151). O "por" da S-L8-2 já ocorre 3 vezes, porque é o mesmo início do D4-R35. Isso não impede a substituição, que é única pelo "antes".
  - Efeito simulado: D4-R42 × D4-19 e × D4-26, 86 caracteres; D4-R42 × D4-R48, 93; D4-R52 × D4-41, 98. Os cenários continuam distintos até o fecho, e nenhuma nota é exigida, pelo mesmo raciocínio da seção 5. Extensão: D4-R42 54 → 54 palavras; D4-R52 58 → 57.
  - A seção 7.6 exclui texto que mude "construção" sem QA própria. Se uma abertura de moldura conta como construção, a decisão é da GCB. Este R2 não redige nem adota o texto.

## 10. Registros (sem veredito e sem efeito; à reconciliação)
1. **Frase "49 verificações automáticas" (bloco 5, l. 976):** seção 8.
2. **SHA abreviado da v1 na l. 5 ("1b9903d5…ecf"):** 3 caracteres finais, onde as outras entradas usam 4 ("…8ecf"). O valor está correto. É registro, sem errata (fichas 11.3 e 13.3).
3. **Abertura variante residual (D4-R42, D4-R52):** seção 9; decisão da GCB.
4. **Pares de prefixo da L3-3 (D4-R35 × D4-14; D4-R48 × D4-19; D4-R48 × D4-26):** conferem; nenhuma nota obrigatória e nenhuma comum nova (seção 5).
5. **Rede (checklist, item 3):** três URLs citadas foram reabertas (seção 0). Todas deram HTTP 200, com bytes iguais aos do R1 e do adendo. O www.gov.br não foi pedido.
6. Continuam os registros do R1, seção 9, item 3, inclusive a errata AJ-L7-E1, julgada APLICÁVEL no R1, seção 8, que este R2 não reexamina.

## 11. Tabela-resumo dos 30 itens (v2)
| id | folha | ponto | gab. | [TS] | formato | moldura | aderência | R1 | R2 |
|---|---|---|---|---|---|---|---|---|---|
| D4-R29 | 8.2 | Lei 11.079, art. 2º, § 3º | E | sim | PAR | N | direta | APROVADO | APROVADO (idêntico à v1) |
| D4-R30 | 8.2 | Guia F2, G8 | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R31 | 8.2 | Lei 13.019, art. 2º, VIII-A | E | sim | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R32 | 8.2 | Lei 9.790, art. 1º, § 2º | E | sim | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R33 | 8.2 | Lei 13.019, art. 2º, I, a | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R34 | 8.2 | Lei 11.079, art. 2º, caput | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R35 | 8.2 | Lei 11.079, art. 2º, § 4º, III | E | sim | APL | S | direta | APROVADO (estilo: AJUSTE, AJ-L8-E1) | **APROVADO** (AJ-L8-E1 aplicado; prefixo de 110 com D4-14, sem nota) |
| D4-R36 | 8.2 | Lei 13.019, art. 2º, I, c | E | sim | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R37 | 8.2 | Lei 9.637, art. 5º (Lei 9.790, art. 9º como contraste) | E | sim | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R38 | 8.2 | Guia F2, G9 (i) | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R39 | 8.3 | Lei 13.460, art. 1º, caput | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R40 | 8.3 | Lei 13.460, art. 18, caput | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R41 | 8.3 | Lei 13.460, art. 1º, § 1º | E | sim | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R42 | 8.3 | Guia F2, H1 (boxe da CGU) | E | sim | APL | S | direta | APROVADO | APROVADO (idêntico; abertura variante: registro, seção 9) |
| D4-R43 | 8.3 | Decreto 9.203, art. 3º, VI, com R84 | C | não | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R44 | 8.3 | Lei 13.460, art. 23, § 1º | E | sim | NUM | N | parcial | APROVADO | APROVADO (idêntico) |
| D4-R45 | 8.3 | Lei 13.460, art. 6º, VI | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R46 | 8.3 | Guia F2, H2 | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R47 | 8.3 | Lei 13.460, art. 1º, § 2º, II | E | sim | PAR | N | direta | APROVADO COM AJUSTE (AJ-1) | **APROVADO** (AJ-1 aplicado; justificativa sem afirmação sem fonte) |
| D4-R48 | 8.3 | Lei 13.460, art. 21 | E | sim | APL | S | direta | APROVADO (estilo: AJUSTE, AJ-L8-E2) | **APROVADO** (AJ-L8-E2 aplicado; prefixo de 86 com D4-19 e D4-26, sem nota nova) |
| D4-R49 | 9.1 | Guia F2, G4 (nota 2) | E | sim | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R50 | 9.1 | Guia F2, G1 | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R51 | 9.1 | Guia F2, G5 | E | sim | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R52 | 9.1 | Guia F2, G6 | E | sim | APL | S | direta | APROVADO | APROVADO (idêntico; abertura variante: registro, seção 9) |
| D4-R53 | 9.1 | R22, segundo elemento | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R54 | 9.1 | R21, terceiro elemento | C | não | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R55 | 9.1 | Decreto 9.203, art. 4º, II | E | sim | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R56 | 9.1 | Guia F2, G3 | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R57 | 9.1 | Guia F2, G7 | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D4-R58 | 9.1 | Guia F2, G2 | E | sim | PAR | N | direta | APROVADO | APROVADO (idêntico) |

Percentual de reprovados: **0/30 = 0,0%**. APROVADO: 30 (100%). REPROVADO: 0.

## 12. Notas à GCB (sem decisão desta QA)
1. A leva segue para a reconciliação e o gatilho A. Há 3 ajustes na rodada: AJ-1 (R1), AJ-L8-E1 e AJ-L8-E2 (estilo). Todos foram aplicados por substituição exata.
2. Para a reconciliação:
   - a frase "49 verificações automáticas" do bloco 5, que não confere (seção 8; registro sem errata);
   - a abertura variante residual do D4-R42 e do D4-R52, para decisão (seção 9);
   - o SHA abreviado da l. 5 (seção 10, item 2).
3. Notas de simulado: como no R1, seção 9, item 2. A (db) é obrigatória. Os 3 pares de prefixo da L3-3 não pedem nota (seção 5).
4. Errata AJ-L7-E1 (D3-R75): APLICÁVEL no R1, seção 8. Vai ao gatilho A como parte separada (ficha 14.3).
5. Núcleo (ficha 14.1): os 30 itens ficam false, como na v1.

FIM DO PARECER QA R2 — LEVA 8 — REFORÇO DA
