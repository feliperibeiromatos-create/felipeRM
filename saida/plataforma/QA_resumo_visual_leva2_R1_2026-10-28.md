# QA — Resumo visual de Direito Administrativo, leva 2 (itens 4.1–4.4, 5.1, 5.2, 6.1–6.5) — R1 (28/10/2026)

QA Opus (qa-normativo-da + gcb-cqfp-didatico + QA-plataforma). Não produzi nada do que reviso e não editei nada em /home/claude/v17_3/; este relatório é o único arquivo criado lá. Os testes que gravam saída rodaram com saída no scratchpad. Classificação: **BLOQUEIA / CORRIGIR / SUGESTÃO**; numeração N (normativo), D (didático), I (interface/script), P (processo).

## Cabeçalho

**Hashes (sha256), todos conferidos com a mensagem da coordenação**
| Arquivo | sha256 |
|---|---|
| resumo_visual_leva2.json | b8b4e96c6ee7f8fdf1d4c71d8b0512deec5958f4593076c2c667e54c354f617b |
| resumo_visual_leva2.py | ca5a064b2ab626628d624610477dc69e157c36e70070c64c3dd96f0dfb562846 |
| extras_leva2_v114.json | 5471832c4dc597adc2903472d77f6814a8fdd30cd7c923f353f7885e58fb3828 |
| canon_leva2_dump.txt | 130315f6aa95ecac58071919323115b1eaf2604ea24bc1b101c6a36436999285 |
| pacote_previa_v114_rv2.json | 67c1b677e8e7f041a74fc1e15a6fa5b264e403ba73ea2b974b59233cf0c62dca |
| plataforma_v17_3_previa_leva2.html | 20e0c21b18c40d91b7f5406343368d75108fc85242840778fac3f65d17c191a0 |
| checa_resumo_visual.py | 9a339ee2273c2772f880bb87ff727881a5cbcb47c437ef6f235471e9cf64e133 |
| TRIAGEM_resumos_MapasPro_DA_leva2 | d04aef3431c460c05802cb03ac5fa033ffffe4e0936b799a80a1880dd37bba1f |
| Conferencia_Dirigida_DAD_Leva2 (ChatGPT, insumo) | 4a397db047f9961c5eee87131ca486d8cbed9b65c3158b38c87485cbb175f2b0 |
| DESPACHO_conferencia_leva2 | 47396e54d21c2d54d53e99d5c2e1b617bfcb54d82cc3140c21b821b7f49d3915 |
| template v17.3 | 11b99a41… (inalterado) |
| t_janela20.js | 36959052… |

**Integridade da prévia**
- A prévia é exatamente o template 11b99a41… com o pacote rv2 embutido e a meta trocada.
- O pacote rv2 tem os 11 `resumoVisual` iguais ao JSON e os 9 da leva 1 intactos (f618895c…).
- Sem os 11 novos, o pacote rv2 é idêntico ao pacote rv1 aprovado.

**Comandos executados**
1. Leitura integral do JSON (dump de 1.361 linhas), do canon (canon_leva2_dump.txt), da triagem, do despacho e dos trechos pertinentes do parecer do ChatGPT.
2. **Fontes oficiais lidas hoje (verificado em 28/10/2026):**
   - Câmara dos Deputados, Legislação Informatizada, Lei 9.784/1999 e Lei 8.112/1990, **texto atualizado completo** em HTML. Obtive o texto inteiro, não truncado, por download direto (curl com user-agent de navegador). Tirei de lá os artigos citados abaixo.
   - Portal do STF, páginas de repercussão geral (numeração e tese literal dos Temas 532 e 592).
   - STF, Informativo 996 (RE 633.782).
   - STJ (scon): **bloqueado** ("Request Rejected").
3. `python3 -I checa_resumo_visual.py resumo_visual_leva2.json --pacote pacote_previa_v114_rv2.json` → 0/0; sobre o pacote rv2 inteiro (20 tópicos) → 0/0.
4. Mutação: 22 casos injetados no JSON da leva 2 (detalhe em I1).
5. `frases()` (ABREV): comparei a contagem antiga com a nova nos textos das duas levas (detalhe em I4).
6. `regr_v17_3.js` (A = prévia leva 1 final, 67ee1325…; B = prévia leva 2), estados antigo e antigo2 → 104 e 110 telas · 20 RV em B · 11 mudanças esperadas · **0 não esperadas** · 0 erros JS.
7. `t_janela20.js` na prévia leva 2 → 0 falhas, 0 erros JS.
8. Teste próprio com Playwright, 11 tópicos × {320 claro, 320 escuro, 390 escuro, 1280 claro}:
   - contraste mínimo de texto 6,14:1 (claro) e 6,95:1 (escuro);
   - sem ícone sem aria-hidden, rolagem horizontal, "30" ligado à nota, preto, azul, verde/vermelho ou emoji;
   - o botão "Resumo" abre o RV nos 11 tópicos e a tela antiga nos outros 59 (clique real em 4.4, 6.5 e 7);
   - 0 erros JS.
9. Varredura estrutural do JSON: nenhum mapa com mais de 8 ramos, nenhuma tabela com mais de 4 colunas, nenhum marco sem "quando", nenhum box sem rótulo, nenhuma frase de relâmpago acima de 140 caracteres, nenhuma "pegadinha provável".
10. Capturas `caps_l2` vistas por amostragem: 4.2 em celular e desktop (mapa, tabela de 4 colunas empilhada no celular). Sem estouro de texto.

## Achados

### BLOQUEIA
**N1 — P1-DA-4.4 · `linhaTempo` "Do pedido à decisão do recurso", marco [1] "Instrução", e `pegadinhas` [1].**
- **Texto atual:** "…consulta pública a critério da autoridade (art. 32)" e "Certo: O art. 32 trata da **consulta pública**; as alegações finais (dez dias) estão no art. 44."
- **Erro de dispositivo:** a consulta pública é o **art. 31**; o **art. 32** é a **audiência pública** ("Antes da tomada de decisão, a juízo da autoridade, diante da relevância da questão, poderá ser realizada audiência pública para debates sobre a matéria do processo"). Verificado em 28/10/2026 na Câmara dos Deputados, Legislação Informatizada, Lei 9.784/1999, texto atualizado.
- **Gravidade:** a pegadinha ensina o erro no campo "Certo", o pior lugar possível. A mesma afirmação está no parecer do ChatGPT (N13.1) e no despacho, que a dá como "conferida na Câmara" (ver P1).
- **Redação proposta:**
  - marco [1]: "de ofício ou a pedido (art. 29); provas obtidas por meios ilícitos são inadmissíveis (art. 30); consulta pública, por despacho motivado, em matéria de interesse geral (art. 31); audiência pública, a juízo da autoridade (art. 32)";
  - pegadinha [1], certo: "O art. 32 trata da **audiência pública** (a consulta pública é o art. 31); as alegações finais (dez dias) estão no **art. 44**."
  - Corrigir também a menção em `fontes` do 4.4.

### CORRIGIR (obrigatório antes da R2)

**N2 — P1-DA-6.3 · `box` regra "Tema 592 do STF (RE 841.526)".**
- A tese entre aspas não é literal. O texto do portal do STF (verificado em 28/10/2026, aba Tese do Tema 592) é: "Em caso de inobservância **do** seu dever específico de proteção previsto no **art. 5º, inciso XLIX**, da Constituição Federal, o Estado é responsável pela morte de detento." O JSON traz "**de** seu" e "**artigo** 5º".
- A numeração (Tema 592 ↔ RE 841.526, rel. Min. Luiz Fux, trânsito em 07/09/2016) confere.
- **Redação:** a tese literal acima. Em `fontes`, trocar "conforme a notícia oficial … a reconferir" por "tese conferida no portal do STF em 28/10/2026".

**N3 — P1-DA-5.1 · `box` regra "Delegação do poder de polícia — Tema 532", `mapa` "Poder de polícia" (ramo "Ciclo de polícia") e `pegadinhas` [2].**
- A tese literal **confere** com o portal do STF (verificado em 28/10/2026; Tema 532 ↔ RE 633.782, rel. Min. Luiz Fux, trânsito em 03/02/2021).
- Falta o limite que o próprio STF fixou e que a banca cobra: a **ordem de polícia** (a função legislativa) é "a única fase do ciclo de polícia que, por sua natureza, é absolutamente indelegável". Consentimento, fiscalização e sanção podem ser delegados (STF, Informativo 996, verificado em 28/10/2026).
- Sem isso, a pegadinha [2] ("a tese não limita a delegação a essas fases") leva a candidata a supor que todas as fases são delegáveis.
- **Redação:**
  - box: acrescentar "A ordem de polícia (função legislativa) continua indelegável; consentimento, fiscalização e sanção podem ser delegados nas condições da tese (Informativo STF 996)";
  - pegadinha [2], certo: "O STF admite delegar consentimento, fiscalização e **sanção** (o caso era de multa); só a **ordem de polícia** é indelegável (Tema 532; Inf. 996)".

**N4 — P1-DA-4.2 · `box` regra "Destituição de cargo em comissão (art. 135)".**
- A leitura "2 anos se a infração era punível com suspensão, 5 se com demissão (EDcl no MS 18.327/DF, DJe 20/2/2013)" **não pôde ser conferida**: o scon do STJ recusa este ambiente, e a única fonte é o parecer consultivo do ChatGPT, que é insumo e não fonte.
- Ela também diverge da letra do art. 142, I ("5 anos … destituição de cargo em comissão", verificado em 28/10/2026 na Câmara), que o próprio tópico repete no mapa (ramo "Prescrição") e na legenda da tabela. Num item literal da banca, a regra é a de 5 anos.
- **Redação:** retirar a frase do STJ do box e deixar: "A destituição de cargo em comissão exercido por não ocupante de cargo efetivo é aplicada nos casos de infração sujeita às penalidades de suspensão e de demissão (art. 135); a ação disciplinar prescreve em 5 anos (art. 142, I)". Se a GCB confirmar o acórdão no STJ, ele volta como `atencao` rotulada "jurisprudência do STJ (conferida em [data])".

**N5 — P1-DA-4.2 · `escala` "Do mais leve ao mais grave", ponto "Destituição".**
- **Texto atual:** "de cargo em comissão ou de função comissionada: infração sujeita a suspensão ou demissão (art. 135)".
- O art. 135 trata só da destituição de **cargo em comissão** exercido por **não ocupante de cargo efetivo** (verificado em 28/10/2026, Câmara). A destituição de função comissionada é penalidade do art. 127, VI, sem regra no art. 135. A leva 1 (3.4) já registra "a lei não fixa prazo próprio no art. 142".
- **Redação:** "de cargo em comissão exercido por não ocupante de cargo efetivo: infração sujeita a suspensão ou demissão (art. 135); a de função comissionada é penalidade do art. 127, VI".

**N6 — P1-DA-4.3 · `dois` "Rito ordinário × rito sumário", lado b, item [3].**
- **Texto atual:** "Na acumulação ilegal, o servidor pode optar por um dos cargos até o último dia da defesa, e o processo é arquivado".
- A lei não fala em arquivamento. O art. 133, § 5º, diz: "A opção pelo servidor até o último dia de prazo para defesa configurará sua boa-fé, hipótese em que se converterá automaticamente em pedido de exoneração do outro cargo" (verificado em 28/10/2026, Câmara).
- **Redação:** "Na acumulação ilegal, a opção até o último dia da defesa configura boa-fé e converte-se em pedido de exoneração do outro cargo (art. 133, § 5º)".

**N7 — P1-DA-4.3 · `dois` (pé) "O que muda é a comissão e o prazo; a ampla defesa é a mesma", e o lado b.**
- No rito sumário também mudam o **prazo de defesa** (cinco dias, art. 133, § 2º) e o **prazo de julgamento** (cinco dias, art. 133, § 4º). O lado a lista "defesa em 10 ou 20 dias" e "julgamento em 20 dias", e o lado b não traz os equivalentes, o que leva a inferir que são iguais.
- **Redação:** acrescentar ao lado b "Defesa escrita em 5 dias (art. 133, § 2º)" e "Julgamento em 5 dias (art. 133, § 4º)"; pé: "Mudam a comissão e os prazos; a ampla defesa continua assegurada".
- Opcional no relâmpago [7]: "…dois estáveis; 30 + 15 dias; defesa e julgamento em 5 (art. 133)".

**N8 — P1-DA-4.3 · `mapa` "A comissão do PAD", ramo "Instrução", e `pegadinhas` [3].**
- "a lei não fixa número máximo de testemunhas (art. 156)" está correto, mas o art. 156, § 1º, permite ao presidente "denegar pedidos considerados impertinentes, meramente protelatórios, ou de nenhum interesse para o esclarecimento dos fatos" (verificado em 28/10/2026, Câmara). Sem isso, a candidata pode marcar Certo em "o acusado pode arrolar testemunhas sem limite e o pedido não pode ser negado".
- **Redação** (pegadinha [3], certo): "A lei **não fixa** número máximo (art. 156); o presidente pode denegar pedidos impertinentes ou protelatórios (§ 1º)". O mesmo acréscimo vai no ramo do mapa.

**N9 — P1-DA-4.4 · `box` atenção "Recurso: o que a lei diz de fato" e `relampago` [4].**
- "tramita por, no máximo, três instâncias (art. 57)" omite a ressalva do artigo: "salvo disposição legal diversa" (verificado em 28/10/2026, Câmara). É a parte que a banca troca.
- **Redação:** "…no máximo três instâncias, salvo disposição legal diversa (art. 57)".

**D1 — P1-DA-5.2 · `compare` "Excesso × desvio", linha "Consequência", e coerência com a leva 1 (2.1).**
- O 5.2 diz que o excesso (incompetência) gera "nulidade do ato lesivo ao patrimônio" (Lei 4.717, art. 2º, letra correta).
- Mas o 2.1, aprovado na leva 1, ensina que, pela doutrina majoritária, o vício de competência é sanável, salvo competência exclusiva ou em razão da matéria. Lado a lado, a candidata pode concluir que o excesso nunca se convalida.
- **Redação:** na linha "Consequência", coluna excesso: "Nulidade do ato lesivo ao patrimônio (Lei 4.717, art. 2º); pela doutrina majoritária, o vício de competência admite convalidação, salvo competência exclusiva ou em razão da matéria (ver 2.1)".

**D2 — Coerência triagem × JSON: "Omissão abusiva" (P1-DA-5.2 · `mapa`, ramo [2]; `relampago` [4]; `pegadinhas` [2]).**
- A triagem diz "NÃO ENTRA: 'Omissão abusiva' como terceira espécie de abuso (doutrina minoritária)", mas o JSON a inclui em três blocos.
- O conteúdo do JSON é defensável e vem rotulado como doutrina: a forma omissiva do abuso é lição corrente (Hely), e o JSON não a trata como "terceira espécie".
- **Correção:** decidir e registrar. Recomendo manter no JSON e corrigir a triagem: "entra como forma omissiva do abuso (doutrina), não como terceira espécie".

**D3 — P1-DA-4.2 · `escala` "Do mais leve ao mais grave".**
- A ordem põe cassação e destituição à direita da demissão, isto é, "mais graves". A destituição cabe também para infração punível com **suspensão** (art. 135), e a cassação equivale à demissão para o inativo (art. 134).
- A escala sugere uma gradação que a lei não faz.
- **Correção:** encerrar a escala na demissão (advertência → suspensão → demissão) e levar cassação e destituição para um box "Penas equivalentes fora da escala" (arts. 134 e 135, com o texto de N5); ou retitular para "As seis penalidades do art. 127".

**I1 — Script `checa_resumo_visual.py`: mutação revela furos dos termos vedados da leva 2.**
- Resultado: dos 22 casos injetados, 15 foram barrados corretamente e 7 passaram.
- **Barrados:** data inválida, literal falso, texto do art. 49 adulterado, ref ausente do baseLegal, relâmpago com 141 caracteres, "pegadinha provável", quádruplo, emoji, página de PDF, mapa com 9 ramos, ícone inválido, cobrança ausente, dois com 8 itens, "ALTÍSSIMA". O controle passou, como esperado.
- **Passaram:**
  - "mais de sessenta dias";
  - "até dez testemunhas";
  - "apenas consentimento e fiscalização (Sistema S)";
  - "art. 2º, XXI";
  - tese do Tema 532 adulterada;
  - marco sem "quando";
  - box sem rótulo.
- **Correção:**
  - acrescentar aos VEDADOS: `mais de sessenta dias`, `até (dez|10) testemunhas`, `apenas (o )?consentimento e (a )?fiscaliza`, `art\. ?2º, XXI`, `art\. ?32.{0,40}consulta`, `Sistema S.{0,60}deleg`, `art\. ?150.{0,40}impediment`;
  - criar uma lista `TESES` (Tema 532, Tema 592, SV 5) com o texto literal conferido, bloqueando qualquer "Tese: "…"" que não coincida;
  - marco sem "quando" e box sem rótulo como aviso (o renderizador tem fallback).

### SUGESTÃO
- **N10 — 4.2, tabela "Prazos que a banca cobra":** incluir o art. 142, § 3º ("A abertura de sindicância ou a instauração de processo disciplinar interrompe a prescrição, até a decisão final proferida por autoridade competente") e o § 4º. Verificado em 28/10/2026, Câmara. Tema muito cobrado e ausente.
- **N11 — 6.1 e 6.2:** a banca cobra a vítima acionar diretamente o agente (Tema 940 do STF, tese da dupla garantia) e a prestadora responder perante não usuário (Tema 130). O canon não tem nenhum dos dois. Lacuna para a GCB (PRÓXIMO), não erro desta leva; só entra no visual depois de conferido no portal do STF.
- **N12 — 4.4, `linhaTempo` marco [6]:** "pela autoridade superior (art. 59, § 1º)". O § 1º fala em "órgão competente"; o encaminhamento à autoridade superior é o art. 56, § 1º. Trocar para "(arts. 56, § 1º, e 59, § 1º)".
- **N13 — 5.1, `dois` delegação, item [0]:** acrescentar "se não houver impedimento legal" e as razões de índole técnica, social, econômica, jurídica ou territorial do art. 12 (texto conferido).
- **D4 — 6.5, `escala`:** o título "Da exclusão à atenuação" e o extremo direito "Não afeta" não casam. Trocar o título para "Da exclusão ao 'não afeta'" ou o extremo para "Atenua / não afeta".
- **D5 — 6.5, `box` "Excludente só quando exclusiva":** o exemplo "enchente previsível sem drenagem" é caso doutrinário sem fonte, e a triagem diz que "o visual não usa casos inventados". Manter só o exemplo do Tema 592, ou rotular "(exemplo doutrinário)".
- **I2 — Etiquetas de cobrança:** a triagem (seção 0) e o pedido dizem "poucas questões" em 5.2, 6.3, 6.4 e 6.5, mas pela ESPEC §4 (até 3 questões) a etiqueta mostra os números (7, 4, 5, 5). O comportamento segue a ESPEC e está correto; corrigir a frase da triagem. A 4.1 mostra "nenhuma questão enquadrada neste item no corpus", correto.
- **I3 — Capturas:** a barra de navegação fixa aparece sobreposta no meio das capturas de página inteira (artefato do screenshot, já existente na leva 1). No celular, a linha zebrada da tabela empilhada tem fundo interno deslocado (cosmético, também da leva 1).
- **I4 — `frases()` (ABREV):** não afrouxou bloqueios, porque a função só alimenta o aviso "texto com mais de 4 frases". Nos 6 textos da leva 2 em que a contagem antiga dava 5 a 7 frases (falsos positivos em "art.", "8.112", siglas), a nova dá 2 a 3, que é o real. Ressalva: com `re.I`, o padrão de sigla `(\b[A-Z])\.` também casa uma letra minúscula isolada ("alínea e. O ato"), juntando duas frases. Usar o padrão de sigla sem `re.I`.

### P — Processo
- **P1 — Falsa conferência.** O despacho e o `fontes` do 4.4 dão o art. 32 da Lei 9.784 como "conferido na Câmara dos Deputados em 28/10/2026 (consulta pública)", e o texto oficial diz o contrário (N1). O erro veio do parecer do ChatGPT e passou como conferido. Pedido à produção: a marca "conferido em [data]" só se grava com o trecho literal copiado da fonte para um arquivo de evidência (ou citado no relatório de produção), dispositivo a dispositivo.
- **P2 — Lei 8.112 já pode ser aberta.** O texto atualizado completo da Lei 8.112 está acessível na Câmara por download direto (`www2.camara.leg.br/legin/fed/lei/1990/lei-8112-11-dezembro-1990-322161-normaatualizada-pl.html`, com user-agent de navegador). O mesmo vale para a Lei 9.784 (`…/lei-9784-29-janeiro-1999-322239-normaatualizada-pl.html`). A "a conferir" da triagem para os arts. 131, 133, 135, 136, 140, 145–156, 161, 164, 165, 167, 171, 174, 175 e 182 pode ser fechada pela produção com a data de hoje: conferi todos e os valores do JSON batem, salvo N5–N8.

## Conferência normativa — o que bate (verificado em 28/10/2026)
- **Lei 9.784/1999 (Câmara, texto atualizado):** art. 1º e §§ 1º e 2º; art. 2º, caput (onze princípios) e parágrafo único (I a XIII; XII impulsão de ofício; XIII interpretação); arts. 3º, 4º, 5º, 6º, 9º, 10, 11, 12 (ver N13), 13, 14 (inclusive § 3º, "editadas pelo delegado"), 15, 18 a 21, 24 e parágrafo único, 26, § 2º, 29, 30, 44, 47, 48, 49, 50 (I a VIII e § 1º), 53, 54, 56, § 1º, 57 (ver N9), 58, 59 e §§ 1º e 2º, 61 e parágrafo único, 63 (I a IV e § 2º), 66 (caput e § 2º), 69. Divergência: **art. 32 (N1)**.
- **Lei 8.112/1990 (Câmara, texto atualizado):**
  - art. 116 (doze incisos); art. 117 (dezenove incisos; VIII, IX, X, XII, XIV, XV como citados);
  - arts. 125 e 126; art. 128 e parágrafo único; art. 129; art. 130, caput e §§ 1º e 2º; art. 131 e parágrafo único; art. 132, I a XIII; art. 133, caput, I a III e §§ 2º a 8º; arts. 134 a 136; arts. 138 e 139; art. 140, I, a e b, e II; art. 141, I a IV; art. 142, I a III e §§ 1º e 2º;
  - arts. 143, 145 (I a III e parágrafo único), 146 e 148; art. 149, caput e § 2º; arts. 150, 151 e 152; art. 154 e parágrafo único; art. 156; art. 161, §§ 1º e 2º; art. 164, §§ 1º e 2º; art. 165, §§ 1º e 2º; art. 167; art. 171; arts. 174 e 175; art. 182 e parágrafo único.
  - Divergências de alcance: N5, N6, N7 e N8.
- **STF (portal, repercussão geral):** Tema 532 ↔ RE 633.782, tese literal **igual** à do JSON; Tema 592 ↔ RE 841.526, tese com duas diferenças de redação (N2). Informativo 996: ordem de polícia indelegável (N3).
- **Constituição, CTN, Código Civil, Lei 4.717, Lei 6.830 e SV 5** (do canon conferido em 20/10/2026 e do meu conhecimento seguro do texto; Planalto inacessível daqui): CF arts. 5º, XXV, LIV, LV e LXIX, 21, XXIII, d, 37, § 6º, 41, § 1º, II, 49, V, 84, IV, VI, a e b, e parágrafo único; CTN art. 78 e parágrafo único; CC art. 43; Lei 4.717, art. 2º, a e e, e parágrafo único, a e e; Lei 6.830/1980, art. 1º (execução fiscal da dívida ativa, que inclui a não tributária); SV 5.
- **STJ, EDcl no MS 18.327/DF:** NÃO CONFERIDO (scon bloqueado); ver N4.

## Didático (resumo)
- **Coerência com a leva 1:** mesmos tipos, ícones da lista, registro e estrutura (seção → visuais → lei → relâmpago → pegadinhas).
- **Limites:** relâmpagos com 6 a 9 frases, todas com até 140 caracteres; pegadinhas em pares Errado/Certo, sem "pegadinha provável" (a legenda de 6.5 diz "típica").
- **Etiquetas:** conforme a ESPEC (I2).
- **Canon:** nada contradiz o canon dos 11 tópicos. O RV acrescenta o Tema 532, o Tema 592 e a leitura do STJ (N4), lacunas já despachadas à GCB.

## Veredito
**REPROVADO**: há um BLOQUEIA (N1, art. 32 da Lei 9.784 apresentado como consulta pública, inclusive no "Certo" de uma pegadinha). A correção é textual. Com N1 e os CORRIGIR feitos, a **R2 pode ser pontual**, sobre os blocos alterados, com o diff do JSON e a nova rodada de mutação. O resto da leva está sólido: conferi todos os prazos do PAD e da Lei 9.784 no texto oficial, as teses do STF estão certas na substância e a interface passou em todos os testes.

## O que a produção deve mudar antes da R2
1. **N1** (BLOQUEIA): 4.4, marco "Instrução" e pegadinha [1]: art. 31 = consulta pública; art. 32 = audiência pública; corrigir também `fontes`.
2. **N2:** 6.3, tese do Tema 592 com a redação literal do portal.
3. **N3:** 5.1, ordem de polícia indelegável no box do Tema 532, no mapa e na pegadinha [2].
4. **N4:** 4.2, retirar do box a leitura do STJ (MS 18.327) até a conferência; manter o art. 142, I.
5. **N5 + D3:** 4.2, escala sem a função comissionada no art. 135; cassação e destituição fora da gradação.
6. **N6:** 4.3, art. 133, § 5º (boa-fé, conversão em pedido de exoneração), sem "arquivado".
7. **N7:** 4.3, defesa e julgamento em 5 dias no rito sumário (art. 133, §§ 2º e 4º).
8. **N8:** 4.3, art. 156, § 1º, no ramo da instrução e na pegadinha das testemunhas.
9. **N9:** 4.4, "salvo disposição legal diversa" no art. 57 (box e relâmpago).
10. **D1:** 5.2, consequência do excesso coerente com o 2.1 (convalidação, doutrina majoritária).
11. **D2:** triagem coerente com o JSON quanto à "omissão abusiva".
12. **I1:** checa com os VEDADOS da leva 2 e a lista `TESES`; nova rodada de mutação.
13. **P1/P2:** registrar a evidência literal de cada `conferido`; fechar a pendência "a conferir" da Lei 8.112 com a data de 28/10/2026.
14. **SUGESTÕES** (N10–N13, D4, D5, I2–I4): a critério da produção, nesta rodada ou na leva 3.

Fontes oficiais desta rodada (lidas em 28/10/2026):
- Câmara, Lei 9.784/1999, texto atualizado: www2.camara.leg.br/legin/fed/lei/1999/lei-9784-29-janeiro-1999-322239-normaatualizada-pl.html
- Câmara, Lei 8.112/1990, texto atualizado: www2.camara.leg.br/legin/fed/lei/1990/lei-8112-11-dezembro-1990-322161-normaatualizada-pl.html
- STF, Tema 532: portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?incidente=4005451&numeroProcesso=633782&classeProcesso=RE&numeroTema=532
- STF, Tema 592: portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?incidente=4645403&numeroProcesso=841526&classeProcesso=RE&numeroTema=592
- STF, Informativo 996: www.stf.jus.br/arquivo/informativo/documento/informativo996.htm
