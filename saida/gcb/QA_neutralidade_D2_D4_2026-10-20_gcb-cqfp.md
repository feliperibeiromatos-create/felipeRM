# QA_neutralidade_D2_D4_2026-10-20_gcb-cqfp.md — T-75/T-76/T-77 — 2026-10-20 — gerado por gcb-cqfp

Conferência de neutralidade (D-CABECALHO-NEUTRO, DECISOES.md l. 109: "Toda versão destinada a comparação ou a produtor externo leva cabeçalho sem autoria, sem modelo e sem serviço, desde a linha 1. A gcb-cqfp confere isso antes de qualquer entrega para fora da fábrica.") dos três arquivos que vão ao leitor externo. Somente leitura: nenhum arquivo do lote foi alterado. Precedente: saida/gcb/D5_para_leitura_critica.md (NEUTRO CONFERIDO no R1 do D5).

## 0. Vereditos

| Arquivo | SHA-256 conferido | Veredito |
|---|---|---|
| saida/gcb/D2_para_leitura_critica.md (704 linhas, 189218 bytes) | 558a24d43ce96a6691ddc19bee2f2bc6f8caec2156ad748a99f8a3ba5fc8b2e9 | **NÃO NEUTRO** — 6 ajustes obrigatórios (seção 2) |
| saida/gcb/D3_para_leitura_critica.md (528 linhas, 116938 bytes) | ad2934375836119a2fd0cb13c7f811b12f3b945f7c777cfd562bc1c60b911804 | **NÃO NEUTRO** — 10 ajustes obrigatórios (seção 3) |
| saida/gcb/D4_para_leitura_critica.md (536 linhas, 112382 bytes) | c0b7c181a705d38b3209091f57f99e0dd8b4b826ce30e9aa70c064b86b62bc14 | **NÃO NEUTRO** — 14 ajustes obrigatórios (seção 4) |

Nenhum dos três tem nome de fornecedor, modelo, agente, unidade, "fábrica", Fundador, orquestrador, código de tarefa ou decisão, id BQ, item C/E ou a expressão "leitura crítica"; o cabeçalho está correto. O que reprova são **resíduos das substituições do script**: o script troca o *nome* da ficha ou do Anexo N, mas deixa o *conteúdo* que remete a eles (mínimos e obrigatórios da ficha, "Parte A/B" da produção dividida, "alerta N" e "seção 4/5" do Anexo N, "D6", "fonte N9", "nunca item"). Em três pontos a troca também muda o sentido (critério 4). Nada disso aparece no precedente D5.

## 1. O que passou nos três arquivos

| Critério | Resultado | Como foi conferido |
|---|---|---|
| (1) cabeçalho | OK nos três | Linha 1 "LOTE D<n> — <título> — curso, resumo, pares e pegadinhas — 20/10/2026" e linha 3 "Instrução ao leitor…", no mesmo formato do D5. Sem autoria, modelo ou serviço. |
| (1) termos proibidos | OK na varredura literal | grep -i em fábrica, GCB/GBQ/GCE/gc*, cqfp, Claude, ChatGPT, GPT, OpenAI, Anthropic, Gemini, sonnet, opus, Fundador, presidência da fábrica, orquestrador, ficha, Anexo, QA, BQ-, T-nn, D-XXX, D<n>-nn, "leitura crítica", acatamento, [TS], SEM FONTE, REVERIFICAR e QA PENDENTE: 0 ocorrências. O PROIB do script também dá 0. "presidencial" (D3 l. 46) e "Presidência da República" (D2 l. 492) são matéria. **Os resíduos indiretos estão nas seções 2 a 4.** |
| (2) sem itens C/E | OK nos três | O corpo vai de "## 1." até a linha anterior a "## 5. (e) ITENS INÉDITOS C/E" do v1. Não há enunciado, gabarito, justificativa de item nem id D<n>-nn. As seções 5 a 8 do v1 (itens, proveniência, contagens e bloco à GCB) não foram exportadas. |
| (3) idêntico ao v1, salvo as substituições | OK nos três | O script, rodado em cópia no scratchpad (python3 -I, sem tocar o repo), regenerou os três arquivos **byte a byte idênticos** aos do disco. O diff linha a linha do v1 (l. 26–725 do D2, l. 26–548 do D3, mesmo recorte no D4) contra a saída dá o mesmo número de linhas, menos só as 9 linhas "### Parte A/B" de cada lote. Toda linha alterada corresponde a uma regra de SUBS: não há texto acrescentado nem removido fora das SUBS. |
| (4) sentido normativo | OK em geral; 3 exceções | "[SEM FONTE — não afirmar]" → "(não afirmado neste material)", "Anexo N, seção 5 (SEM FONTE …)" → "texto legal compilado (sem fonte oficial localizada)" e as supressões de BQ-0126, BQ-0150, BQ-0151 e BQ-0152 (só o parêntese de rastreio) preservam o sentido. **Exceções**: "REVERIFICAR" → "Nota de vigência:" vazio (D2), porque o aviso de vigência pendente se perde; "Mínimo da ficha" → "Mínimo deste material" (D2, D3 e D4); "Anexo N" → "texto legal compilado" onde o Anexo N trazia o referencial doutrinário ou institucional (D4), porque doutrina passa a parecer texto legal. |
| (5) edital literal | OK nos três | Cada linha "> …" é substring exata da linha 5 de edital/DA_itens_1_12_P1.md (que se declara "Texto literal abaixo, sem alteração"). Os itens estão completos e cortados na fronteira certa: o item 4 termina antes de " 5 Poderes…", o 7 antes de " 8 Evolução…" e o 9 antes de " 10 Noções…". Itens: D2 = 3 e 4; D3 = 5, 6 e 7; D4 = 8 e 9. |

## 2. D2 — NÃO NEUTRO: ajustes obrigatórios

Os números de linha referem-se ao arquivo atual, antes de qualquer supressão.

| # | Linha | Texto atual (exato) | Substituir por (exato) | Motivo |
|---|---|---|---|---|
| D2-a | 561 | `Mínimo deste material: 8, com os 6 obrigatórios (P-01 a P-06). Entregues: 12 (os 6 obrigatórios e os 6 recomendados da parte A).` | suprimir a linha 561 e a linha em branco 562 | Conteúdo da ficha (mínimo, obrigatórios e recomendados) com o nome trocado e a divisão da produção ("parte A"). Muda o sentido, porque o mínimo é da ficha e não "deste material". (1)(4) |
| D2-b | 583 | `Mínimo deste material: 8, com os 6 obrigatórios (P-51 a P-56). Entregues: 11.` | suprimir a linha 583 e a linha em branco 584 | idem |
| D2-c | 175 | `(parte B deste lote)` | `(item 4 deste material)` | Divisão da produção. (1) |
| D2-d | 29 | `Nota Nota de vigência: a alínea b` | `Nota (vigência a reconfirmar): a alínea b` | "REVERIFICAR" marca ponto na fila de reverificação; "Nota de vigência:" vazio apaga o aviso, e a palavra sai duplicada. (4) |
| D2-e | 138 | `(Nota de vigência:; norma de 2025, vigente)` | `(vigência a reconfirmar; norma de 2025, vigente)` | idem (4) |
| D2-f | 160, 490, 505, 570 (4 ocorrências) | `Nota de vigência:)` | `vigência a reconfirmar)` | idem (4). Resultado: "(vigência a reconfirmar)" nas linhas 160 e 570; "(EC 138/2025; vigência a reconfirmar)" na 490; "(…no referencial do Decreto; vigência a reconfirmar)" na 505. |

Ajuste de forma (opcional): linhas 14 e 207, `((não afirmado neste material))` → `(não afirmado neste material)`.

## 3. D3 — NÃO NEUTRO: ajustes obrigatórios

| # | Linha | Texto atual (exato) | Substituir por (exato) | Motivo |
|---|---|---|---|---|
| D3-a | 45 | `(texto legal compilado, alerta 6)` | `(texto legal compilado)` | "alerta N" é a numeração interna do Anexo N, que sobra depois da troca do nome. O texto legal compilado não tem "alertas", e o leitor não consegue resolver a remissão. (1)(4) |
| D3-b | 72 | `(texto legal compilado, alerta 4)` | `(texto legal compilado)` | idem |
| D3-c | 109 | `(texto legal compilado, alerta 1)` | `(texto legal compilado)` | idem |
| D3-d | 114 | `(texto legal compilado, alerta 2)` | `(texto legal compilado)` | idem |
| D3-e | 158 | `(texto legal compilado e alerta 3)` | `(texto legal compilado)` | idem |
| D3-f | 284 | `(texto legal compilado, alerta 8)` | `(texto legal compilado)` | idem |
| D3-g | 349 | `(texto legal compilado, alerta 15)` | `(texto legal compilado)` | idem |
| D3-h | 412 | `Mínimo deste material para a Parte A: 10, com os 7 obrigatórios (P-01 a P-07). Entregues: 13.` | suprimir a linha 412 e a linha em branco 413 | Conteúdo da ficha e divisão da produção. (1)(4) |
| D3-i | 435 | `Mínimo deste material para a Parte B: 8, com os 6 obrigatórios (P-51 a P-56). Entregues: 10.` | suprimir a linha 435 e a linha em branco 436 | idem |
| D3-j | 455 | `código G-NN (faixa G-01 a G-50 da Parte A).` | `código G-NN.` | Divisão da produção. (1) |

Ajustes de forma (opcionais):
- linhas 15 e 40: `((não afirmado neste material))` → `(não afirmado neste material)`;
- linha 349: `no texto legal compilado A LC 219` → `no texto legal compilado. A LC 219` (o ponto foi consumido pela regex de "seção 2.1.");
- linhas 361, 364 (2 ocorrências), 369, 371 e 372: `(Base doutrinária:)` → `(base doutrinária)`;
- linhas 423 e 425 a 428: `(Base doutrinária:,` → `(base doutrinária,`.

## 4. D4 — NÃO NEUTRO: ajustes obrigatórios

| # | Linha | Texto atual (exato) | Substituir por (exato) | Motivo |
|---|---|---|---|---|
| D4-a | 14 e 191 (2 ocorrências) | `(R-id da seção 5 do texto legal compilado, com as palavras-chave literais)` | `(R-id, com as palavras-chave literais)` | A seção 5 do Anexo N, renomeada, reapresenta o referencial (TCU, ENAP, Ipea, autores) como se fosse "texto legal compilado". (1)(4) |
| D4-b | 14 | `Temas da Parte B (governança,` | `Temas do item 9 (governança,` | Divisão da produção. (1) |
| D4-c | 144 | `(LAI, art. 10, caput; exceção deste material)**` | `(LAI, art. 10, caput)**` | "exceção da ficha" com o nome trocado. (1)(4) |
| D4-d | 145 | `- Definição: Lado passivo do par, pela exceção única deste material (curso e par; nunca item), com o texto do texto legal compilado do D6, seção 4, consulta de 17/10/2026 (mesma URL da fonte N9): ` | `- Definição: Lado passivo do par, com o texto legal compilado (consulta de 17/10/2026): ` | Remete a outro lote ("D6"), à seção 4 do Anexo N, ao id de fonte do Anexo N ("fonte N9"), à exceção da ficha e à existência de itens ("nunca item"). (1) |
| D4-e | 191 | `do Decreto 9.203/2017, texto integral compilado (texto legal compilado), ou` | `do Decreto 9.203/2017, texto integral compilado, ou` | Era "(Anexo N, seção 4.1)"; virou redundância que mantém o rastro. (1) |
| D4-f | 191 | `exemplo hipotético no contexto da seção 4 deste material;` | `exemplo hipotético no contexto do Legislativo;` | Era "seção 4 da ficha" (contexto de uso: Câmara dos Deputados). Hoje aponta para a seção 4 do próprio arquivo, que é a de Pegadinhas: remissão errada. (1)(4) |
| D4-g | 206 | `na mesma página, segundo o texto legal compilado, o referencial diz que` | `na mesma página, o referencial diz que` | Era "segundo o Anexo N" (a nota de quem leu a fonte). Agora atribui a uma "lei" o relato sobre o referencial do TCU. (4) |
| D4-h | 336 | `Fontes: texto legal compilado (normas, seção 4; referencial R1 a R18, seção 5).` | `Fontes: normas (texto legal compilado) e referencial (R1 a R18).` | Seções 4 e 5 do Anexo N; o referencial aparece como parte do texto legal. (1)(4) |
| D4-i | 374 | `por qualquer interessado (só curso e par) \| Lei 12.527/2011, art. 10, caput (texto legal compilado do D6) \|` | `por qualquer interessado \| Lei 12.527/2011, art. 10, caput \|` | "D6" (outro lote) e "só curso e par" (existência de itens). (1) |
| D4-j | 435 | `(LAI, art. 10, caput; só curso e par)` | `(LAI, art. 10, caput)` | idem (1) |
| D4-k | 435 | `(texto legal compilado do D6, seção 4, consulta de 17/10/2026)` | `(texto legal compilado, consulta de 17/10/2026)` | "D6" e seção do Anexo N. (1) |
| D4-l | 425 | `Mínimo deste material: 8 na Parte A (14 obrigatórios no lote, 7 na Parte A: P-01 a P-07). Entregues: 11 (P-01 a P-11). Cada lado` | `Cada lado` | Conteúdo da ficha e divisão da produção. Fica só a regra de método ("Cada lado tem dispositivo ou R-id; lado sem lastro não entra."). (1)(4) |
| D4-m | 444 | `Mínimo deste material para a Parte B: 8, com os 7 obrigatórios (P-51 a P-57). Entregues: 12 (os 7 obrigatórios e 5 sugeridos com lastro nos dois lados).` | suprimir a linha 444 e a linha em branco 445 | idem |
| D4-n | 504 | `Códigos G-51 em diante (G-01 a G-50 são da Parte A).` | `Códigos G-51 em diante.` | Divisão da produção. (1) |

Ajuste de forma (opcional): linha 387, `((não afirmado neste material))` → `(não afirmado neste material)`.

## 5. Recomendações (não bloqueiam; não constam do precedente D5)

Menções à existência de itens, que não dão o conteúdo de nenhum deles: D2 l. 16 "(não é folha; sem itens)", l. 19 e 96 "nenhum item a julga.", l. 44 "Nenhum item deste lote julga o art. 40, § 4º, ou o § 5º-A."; D4 l. 43 "(R5): só curso**", l. 44 "e nenhum item do lote versa sobre o conteúdo do PDRAE", l. 213 e 509 "e nenhum item os mistura". Sugestão: suprimir os trechos. Também se recomenda que o D4 traga uma chave de R-ids e F-ids (R1–R21, F4–F9), porque o leitor externo não consegue resolver as siglas. Isso exige acréscimo de conteúdo pela produção, e não pela gcb-cqfp.

## 6. Verificação dos ajustes e como aplicá-los

- Os 30 ajustes obrigatórios e os opcionais foram aplicados **em cópias no scratchpad** (o repo não foi tocado). Cada texto atual ocorre exatamente o número de vezes indicado. Depois dos ajustes, a varredura ampliada (a de 1 mais "Parte A/B", "alerta N", "seção N do texto legal/deste material", "fonte Nn", "D<n>" isolado, "Nota de vigência:", "mínimo deste", "exceção deste material", "nunca item") dá 0 resíduo no D2 e no D3. No D4 sobra só "só curso" da l. 43, que é recomendação (seção 5).
- Como os arquivos são gerados, o caminho preferível é levar os ajustes às SUBS de saida/gcb/scripts_orq/leitura_critica_gen.py e regenerar. Uma edição manual seria desfeita na próxima execução. Equivalentes sugeridos, nesta ordem e **antes** das regras atuais de "Anexo N", "ficha" e "REVERIFICAR":
  - `r'^Mínimo da ficha[^\n]*\n\n'` → `''` (com re.M), com o caso especial do D4 l. 445 do v1, que mantém "Cada lado tem dispositivo ou R-id; lado sem lastro não entra.";
  - `r',? (?:e )?alerta \d+'` logo depois de "Anexo N" → `''`;
  - `r'\bREVERIFICAR\b:?'` → `'vigência a reconfirmar'`, tratando antes "Nota REVERIFICAR:";
  - substituições literais para as linhas do D4 (D4-a a D4-k, D4-n) e para "Parte A/B" (D2-c, D3-j);
  - acrescentar ao PROIB: `(?i:\bparte [ab]\b|alerta \d|nunca item|só curso|fonte N\d|\bD[1-9]\b(?!-)|mínimo d)`.
- Depois de aplicar, a gcb-cqfp reconfere: SHA-256 novo, diff contra a versão atual restrito às linhas desta lista e varredura com 0 resíduo. Só então cada arquivo pode receber NEUTRO CONFERIDO e sair para o leitor externo.

## 7. Reconferência (2026-10-20)

Objeto: os três arquivos depois dos ajustes obrigatórios e opcionais das seções 2 a 4. O orquestrador os aplicou por substituição literal com saida/gcb/scripts_orq/neutralidade_ajustes.py, e não pelas SUBS do gerador (seção 6). Somente leitura do repositório. A versão anterior foi regenerada numa cópia mínima em /tmp/gcbcqfp_copia_repo (edital/DA_itens_1_12_P1.md, saida/gcb/scripts_orq/ e saida/gcb/D2_v1.md a D4_v1.md), com python3 -I. Scripts próprios ficaram no scratchpad. Sem navegador; sem commit.

### 7.0 Vereditos

| Arquivo | SHA-256 atual | Bytes; linhas | Veredito |
|---|---|---|---|
| saida/gcb/D2_para_leitura_critica.md | 96cd914017d1d43e39a725397f21cafa9e05542824181c411e1b4f3ec7cd282b | 189.036; 700 | **NEUTRO CONFERIDO** |
| saida/gcb/D3_para_leitura_critica.md | 5aee518924c297d4607aef62e2c9ba61a3b3f76cec21649323237f142e890365 | 116.628; 524 | **NÃO NEUTRO**: 1 ajuste obrigatório (7.4) |
| saida/gcb/D4_para_leitura_critica.md | 505c573405b8a55d2f206c4e6d70809f5550302ed125ba55b1d4de4db2d909c3 | 111.685; 534 | **NEUTRO CONFERIDO** |

### 7.1 Versão anterior regenerada

Na cópia, `python3 -I leitura_critica_gen.py` foi rodado com os argumentos D2 "Agentes públicos e direito administrativo disciplinar" 3,4; D3 "Poderes administrativos, responsabilidade civil do Estado e improbidade" 5,6,7; e D4 "Gestão pública e governança" 8,9. Os títulos são os da linha 1 dos arquivos atuais. O resultado deu 558a24d4…b2e9 (189.218 bytes; 704 linhas), ad293437…1804 (116.938; 528) e c0b7c181…bc14 (112.382; 536), iguais aos SHA-256 da seção 0, com 0 achado do PROIB do gerador. O script do orquestrador, rodado sobre essa cópia, reproduz os três arquivos em disco byte a byte.

### 7.2 Diff anterior → atual: só as linhas da lista

- Aplicação independente. As seções 2 a 4 deste relatório foram transcritas para um script próprio que trabalha **por número de linha**: confere que o texto atual está na linha indicada e que o total de ocorrências no arquivo é o da lista. Depois, troca o texto ou suprime a linha e a branca seguinte. O resultado é igual ao arquivo em disco nos três lotes, byte a byte. Não há mudança fora da lista nem item da lista sem aplicação.
- Hunks do `diff`:
  - D2: 14, 29, 138, 160, 175, 207, 490, 505, 561–562 (supressão), 570 e 582–583 (supressão). Este último é a forma do diff para a supressão da l. 583 e da branca 584, que estão entre duas brancas; o resultado é o mesmo.
  - D3: 15, 40, 45, 72, 109, 114, 158, 284, 349, 361, 364, 369, 371–372, 412–413 (supressão), 423, 425–428, 435–436 (supressão) e 455.
  - D4: 14, 144–145, 191, 206, 336, 374, 387, 425, 435, 444–445 (supressão) e 504.
  
  Todos correspondem, um a um, a D2-a a D2-f, D3-a a D3-j, D4-a a D4-n e aos opcionais.
- Linhas: 704 → 700, 528 → 524 e 536 → 534, com LF, 0 CR e final "---\nFIM\n" inalterados. As 8 ocorrências de linha em branco dupla de cada arquivo já estavam na versão anterior (supressão de "### Parte A/B" pelo gerador). Nenhuma foi criada pelos ajustes.

### 7.3 Varredura ampliada nos arquivos atuais

| Padrão | D2 | D3 | D4 |
|---|---|---|---|
| Lista da seção 1: fábrica, GCB/GBQ/GCE, cqfp, cpp, Claude, ChatGPT, GPT, OpenAI, Anthropic, Gemini, sonnet, opus, Fundador, orquestrador, ficha, Anexo, QA, BQ-, T-nn, D-XXX, D<n>-nn, "leitura crítica", acatamento, [TS], SEM FONTE, REVERIFICAR e QA PENDENTE | 0 | 0 | 0 |
| Seção 6: "Parte A/B", "alerta N", "nunca item", "fonte Nn", "D<n>" isolado, "Nota de vigência", "mínimo deste", "exceção deste material", "seção N do texto legal/deste material", "do texto legal compilado do", "Entregues:", "obrigatórios (P-", "((" | 0 | 0 | 0 |
| "(Base doutrinária:)" e "(Base doutrinária:," | 0 | 0 | 0 |
| Termos de processo: R1/R2 como rodada, v1/v2, produção/produtor, parecer, rodada, revisor, pendente, "a confirmar", "confirmado pelo", acréscimo, inédito, troca sutil, script, .md/.py, agente/unidade/gerência como órgão da fábrica | 0 | **1** (7.4) | 0 |
| "só curso" | 0 | 0 | 1 (l. 43): recomendação da seção 5 |

- Falsos positivos, sem resíduo:
  - "mínimo da/das" no D4 (l. 149 "Conteúdo mínimo da divulgação", LAI; l. 244 "conteúdo mínimo das práticas") e "no mínimo dez" no D2 (Lei 8.112, art. 15, § 1º) são matéria. São os 4 "resíduos" que o PROIB do script do orquestrador imprime.
  - R1 a R31 no D4 são ids do referencial (TCU, Casa Civil, Ipea, ENAP).
  - "banca" ("Como a banca troca") e "folha a folha" são do formato que o precedente D5 também usa.
  - "Presidência da República", "Secretaria Especial…", "produção de provas", "revisão" (geral anual; disciplinar) e "agente público" são matéria.
  - "Base doutrinária: (ponto pacífico)", no D3, é a troca do rótulo do v1 pelo gerador. Tem o sentido preservado e não remete à produção.
- Ficam como estavam (seção 5, não bloqueiam): no D2, "(não é folha; sem itens)" (l. 16), "nenhum item a julga" (l. 19 e 96) e "Nenhum item deste lote julga…" (l. 44); no D4, l. 43 "só curso" e l. 44, 213 e 507 "nenhum item…"; a chave de R-ids do D4, que deve cobrir R1 a R31 e não só R1 a R21, como dito na seção 5.

### 7.4 D3 — NÃO NEUTRO: ajuste obrigatório (resíduo novo, fora da lista da seção 3)

| # | Linha | Texto atual (exato) | Substituir por (exato) | Motivo |
|---|---|---|---|---|
| D3-k | 146 (C6.2-03, definição; mesma linha na versão anterior) | `(ponto pacífico, a ser confirmado pelo R1)` | `(ponto pacífico)` | "R1" é a rodada de QA da fábrica, e no D3 não há R-id de referencial. O trecho revela o processo de revisão e que a matéria passou por QA, contra o critério (1). Ocorre 1 vez. O texto novo segue o D3_parecer_R1_gcb-cqfp.md, ponto 20 ("C6.2-03: tirar 'a ser confirmado pelo R1'; pacificidade confirmada"), e iguala a forma às demais "Base doutrinária: (ponto pacífico):". (1) |

- O resíduo já estava na versão de 558a…/ad29…/c0b7… e escapou da varredura da seção 1 deste relatório, que não procurava "R\d" de rodada. **A falha é desta QA, não da aplicação.** A varredura de processo da 7.3 passa a fazer parte da conferência de neutralidade.
- Resultado esperado depois do ajuste (simulado em cópia): SHA-256 f40bac9216eda245a091362a5517f290e96b94365ad11dcaa65065bb38200d07, 116.602 bytes, 524 linhas. Se for aplicado por substituição literal (por exemplo, como uma linha a mais da lista 'D3' do neutralidade_ajustes.py, com contagem 1), a gcb-cqfp reconfere só o hash e esse trecho.
- Para regerações futuras: acrescentar ao PROIB `\bR\d\b` (salvo nos lotes com R-id de referencial, como o D4) e `(?i:a ser confirmado|confirmado pel)`. Melhor ainda: tirar a menção no D3_v1.md, ou no seu sucessor da v2, pela produção, como manda o ponto 20 do R1.

### 7.5 Saída para o leitor externo

D2 (96cd9140…282b) e D4 (505c5734…d909c3) podem sair. O D3 só sai depois do D3-k, com o hash f40bac92…0d07 conferido.
