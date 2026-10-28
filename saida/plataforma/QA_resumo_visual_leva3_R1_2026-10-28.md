# QA — Resumo visual de Direito Administrativo, leva 3 (P1-DA-7, 8, 8.1–8.4, 9.1–9.4) — R1 (28/10/2026)

QA Opus (qa-normativo-da + gcb-cqfp-didatico + QA-plataforma), com as regras das levas 1 e 2. Não editei nada em /home/claude/v17_3/; este relatório é o único arquivo criado lá. Classificação: BLOQUEIA / CORRIGIR / SUGESTÃO; N (normativo), D (didático), I (interface/script), P (processo).

## Cabeçalho

**Hashes (sha256), todos conferidos com a mensagem da coordenação**
| Arquivo | sha256 |
|---|---|
| resumo_visual_leva3.json | 0a3bae617e5dcbd18cb72494812422d2e7f68a2918956685c9027f2cb6304b75 |
| resumo_visual_leva3.py | bd9af7abefca77ed563fa9f29205c34acad69904e11e9de85e00809c3fc11ef7 |
| extras_leva3_v114.json | 3e677386d09a471cf6391532657abb9a22eb4e57f6993bfb12db9c83bff9b823 |
| canon_leva3_dump.txt | b9dbb605ce23c9f22847c145e2014d95bc5e03c7df7b1374e1626c3353cdc893 |
| evidencia_Lei8429_Camara_2026-10-28.txt | 829d3cd03efc2f50423c8f7c41a4b8a35d53eb8c474ac82e679d306d00b3ed3a |
| pacote_previa_v114_rv3.json | 50d15caaa58d096bdf9856b2e11faf15d17045ca9dacf9ed99d270341154a015 |
| plataforma_v17_3_previa_leva3.html | d16fbb1f2352bd76cc9ebe76ef7669406b37ccb1324fe960c0b7461127feb842 |
| checa_resumo_visual.py | 43ed8198… (v1.2, inalterado) |
| TRIAGEM leva 3 | 32ec817ce4b27ff4b5d4265f06849026a4705f0c7c089d9cf2e8b42189f07373 |
| template v17.3 | 11b99a41… (inalterado) |

**Integridade da prévia**
- A prévia é exatamente o template com o pacote rv3 embutido e a meta "…levas 1 a 3 (prévia, QA R1)".
- No pacote rv3, os RV das levas 1 e 2 estão intactos e os 10 da leva 3 são iguais ao JSON.
- Sem a leva 3, o pacote rv3 é igual ao rv2 aprovado.
- `extras_leva3_v114.json` é igual ao canon do pacote.

**Comandos executados e fontes lidas (verificado em 28/10/2026)**
1. Leitura integral do JSON (dump de 1.105 linhas), do canon (106 linhas) e da triagem.
2. **Lei 8.429/1992:** texto atualizado baixado por mim da Câmara dos Deputados, Legislação Informatizada (`www2.camara.leg.br/legin/fed/lei/1992/lei-8429-2-junho-1992-357452-normaatualizada-pl.html`). Conferi todos os artigos citados no item 7.
3. **Decreto 9.203/2017:** texto atualizado e publicação original da Câmara (`…/legin/fed/decret/2017/decreto-9203-22-novembro-2017-785782-normaatualizada-pe.html` e `…-publicacaooriginal-154277-pe.html`). Conferi os arts. 1º a 6º, 7º/7º-A, 8º-A, 8º-B (§§ 1º e 2º), 9º-A, 10-B, 12-A, 13-A, 15-A, 17, 19, 20 e 20-A, e os arts. 7º a 15 originais.
4. **Notícias oficiais do STF** (noticias.stf.jus.br e portal.stf.jus.br):
   - 31/08/2022, ADIs 7.042 e 7.043 (`portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=493313`);
   - 24/09/2025, cautelar na ADI 7.236 (prescrição intercorrente);
   - 28/05/2026, 24/06/2026, 25/06/2026 e **01/07/2026**, julgamento conjunto das **ADIs 7.156 e 7.236**, concluído em 1º/7/2026.
5. `checa_resumo_visual.py` → leva 3 com `--pacote`: 0/0; pacote rv3 inteiro (30 tópicos): 0/0. A mutação não foi refeita: o checador é o mesmo aprovado na R3 da leva 2.
6. `regr_v17_3.js` (A = prévia leva 2; B = prévia leva 3), estados antigo e antigo2 → 104 e 110 telas · 30 RV · 10 esperadas · **0 não esperadas** · 0 erros JS. `t_janela20.js` → 0 falhas, 0 erros JS.
7. Teste próprio com Playwright, 10 tópicos × 4 cenários:
   - contraste mínimo de texto 6,14:1 (claro) e 6,95:1 (escuro);
   - nenhum ícone sem aria-hidden, sem rolagem horizontal, sem "30" ligado à nota, sem preto, azul, verde/vermelho ou emoji;
   - o RV abre só nos 10 tópicos; os outros 49 tópicos com resumo abrem a tela antiga (clique real em 7, 9.2 e 10.1).

## Achado central (P1-DA-7)
A Lei 8.429 que o visual ensina é a da **letra** do texto atualizado da Câmara. Mas o STF concluiu em **1º/7/2026** o julgamento das **ADIs 7.156 e 7.236** e declarou inconstitucionais, ou reinterpretou, vários dispositivos que o visual ensina como vigentes.

O texto da Câmara não anota essas ADIs: anota só "Vide ADIs 7.042 e 7.043". A triagem viu a "ATUALIZAÇÃO 2024-2025 — ADI 7.236" no PDF MapasPro e a deixou "fora", como "não conferida". O resultado é que a candidata aprenderia regras que o STF afastou.

As decisões abaixo estão nas notícias oficiais do STF de 28/05, 24/06, 25/06 e 01/07/2026. O acórdão ainda não foi lido aqui, e o enquadramento por parágrafo deve ser confirmado na ata e no acórdão. Mas a substância é inequívoca, e as notícias bastam para bloquear.

## Achados

### BLOQUEIA (todos em P1-DA-7)

**N1 — `linhaTempo` "Prescrição da ação (art. 23)", marcos [3] "Metade do prazo" e [4] "Prescrição intercorrente"; `relampago` [5].**
- **Texto atual:** "o prazo recomeça do dia da interrupção, pela metade: 4 anos (§ 5º)"; "se entre os marcos do § 4º transcorrer o prazo do § 5º, o juiz a reconhece de ofício (§ 8º)"; "interrompida, recomeça pela metade (art. 23)".
- **O que decidiu o STF:** "Por maioria, o Plenário declarou a inconstitucionalidade de dispositivo que reduzia pela metade o prazo prescricional … foi afastada a regra segundo a qual, após a interrupção da prescrição, o prazo voltaria a correr pela metade, passando de oito para quatro anos." As hipóteses de interrupção foram mantidas por unanimidade, e o Tribunal fixou "o prazo máximo de 20 anos de prescrição". Fonte: notícia oficial do STF de 01/07/2026, ADIs 7.156 e 7.236, verificado em 28/10/2026. O § 5º já estava suspenso por cautelar na ADI 7.236 (notícia de 24/09/2025).
- **Redação proposta:** marco [3] "Interrompida, a prescrição recomeça; a regra que reduzia o prazo à metade (§ 5º) foi declarada inconstitucional pelo STF (ADIs 7.156 e 7.236, 1º/7/2026), que fixou o prazo máximo de 20 anos"; retirar o marco [4] até a leitura do acórdão (o § 8º remete ao § 5º); relâmpago [5]: "Prescrição: 8 anos do fato; suspensão até 180 dias (art. 23); a 'metade' do § 5º caiu no STF; teto de 20 anos."

**N2 — `fluxo` "Da notícia do fato à sentença", passo [4].**
- **Texto atual:** "Decisão que fixa um único tipo por ato, sem mudar o fato nem a capitulação (art. 17, §§ 10-C e 10-D)".
- **O que decidiu o STF:** derrubou "dispositivos que restringiam a atuação do juiz … A lei determinava que o magistrado ficasse vinculado ao enquadramento jurídico indicado na petição inicial … a definição jurídica desses fatos é atribuição do Judiciário" (notícia oficial de 24/06/2026).
- **Redação proposta:** "O autor narra os fatos; o enquadramento jurídico é do juiz, que não fica vinculado à capitulação da inicial (STF, ADIs 7.156 e 7.236)".

**N3 — `fluxo`, passo [2].**
- **Texto atual:** "indisponibilidade de bens, se houver perigo de dano (art. 16)".
- **O que decidiu o STF:** declarou inconstitucionais "trechos que condicionavam o bloqueio de bens à demonstração concreta de risco imediato", afastou em parte a vedação de presumir a urgência e admitiu o bloqueio "quando houver indícios especialmente fortes de irregularidade, mesmo sem demonstração de urgência", alcançando também o enriquecimento ilícito (notícia de 24/06/2026).
- **Redação proposta:** "indisponibilidade de bens para recompor o erário ou o acréscimo ilícito (art. 16); o STF admitiu o bloqueio sem demonstração de urgência quando houver indícios especialmente fortes (ADIs 7.156 e 7.236)".

**N4 — `box` regra "Perda da função e direitos políticos: só com o trânsito em julgado", última frase.**
- **Texto atual:** "A perda da função atinge apenas o vínculo de mesma qualidade e natureza da época da infração, salvo extensão excepcional no art. 9º (art. 12, § 1º)."
- **O que decidiu o STF:** acolheu a proposta de Dias Toffoli: "perda de todas as funções públicas do agente condenado por improbidade, mas, excepcionalmente e fundamentadamente, o juiz poderá deixar de aplicar a perda a uma ou outra função pública específica" (notícia de 24/06/2026).
- **Redação proposta:** "A perda alcança todas as funções públicas do condenado; excepcionalmente e de forma fundamentada, o juiz pode deixar de aplicá-la a uma função específica (STF, ADIs 7.156 e 7.236, afastando a restrição do art. 12, § 1º)."

**N5 — `dois` "Acordo de não persecução civil (art. 17-B)", lado "Exige", item [3].**
- **Texto atual:** "Oitiva do Tribunal de Contas sobre o valor do dano, em 90 dias (§ 3º)".
- **O que decidiu o STF:** "declarou inconstitucional o dispositivo que obrigava a consulta prévia ao tribunal de contas para apuração do valor do dano … em prazo de até 90 dias" (notícia de 24/06/2026).
- **Redação proposta:** retirar o item; querendo, acrescentar ao pé: "A oitiva obrigatória do Tribunal de Contas (§ 3º) foi declarada inconstitucional (ADIs 7.156 e 7.236)".

**N6 — `box` regra "Independência das instâncias (art. 21)", segunda frase.**
- **Texto atual:** "A absolvição criminal pelos mesmos fatos, confirmada por decisão colegiada, impede o trâmite da ação de improbidade (§ 4º)".
- **O que decidiu o STF:** "a absolvição na esfera criminal não encerra automaticamente a ação de improbidade". O encerramento automático só ocorre quando a Justiça criminal reconhece, com trânsito em julgado, que o fato não existiu ou que o acusado não foi o autor, ou a legítima defesa, o estrito cumprimento do dever legal ou o exercício regular do direito, ou quando a denúncia é arquivada ou rejeitada por esses três últimos fundamentos (notícia de 25/06/2026).
- **Redação proposta:** "A absolvição criminal não encerra automaticamente a ação de improbidade; só a encerra, com trânsito em julgado, quando reconhece a inexistência do fato, a negativa de autoria, a legítima defesa, o estrito cumprimento do dever legal ou o exercício regular do direito (STF, ADIs 7.156 e 7.236, afastando a regra do § 4º)". A primeira frase (art. 21, I e II) fica.

**N7 — `pegadinhas` [7].**
- **Texto atual:** "Errado: O terceiro que concorre para o ato responde solidariamente com o agente. Certo: … no limite da participação e dos benefícios diretos, **vedada qualquer solidariedade** (art. 17-C, § 2º)".
- **O que decidiu o STF:** declarou o trecho "parcialmente inconstitucional": as sanções são individualizadas, mas "a recomposição dos prejuízos causados aos cofres públicos pode ser exigida de forma solidária dos responsáveis pelo dano" (notícia de 24/06/2026). O "Certo" atual ensina a regra afastada, e o "Errado" ficou parcialmente certo.
- **Redação proposta:** "Errado: Na improbidade praticada por vários réus, é vedada qualquer solidariedade, inclusive no ressarcimento. Certo: As sanções são individualizadas, mas o **ressarcimento** ao erário pode ser exigido **solidariamente** dos responsáveis pelo dano (STF, ADIs 7.156 e 7.236)."

**N8 — `mapa` "Quem responde pela Lei 8.429", ramo [2] "Terceiro (art. 3º)".**
- **Texto atual:** "sócios e diretores só com participação e benefícios diretos (§ 1º)".
- **O que decidiu o STF:** formou-se maioria "para considerar inconstitucional a exigência de comprovação de 'benefícios diretos'"; basta a participação ativa e dolosa (notícia de 28/05/2026, consolidada em 01/07/2026).
- **Redação proposta:** "quem, mesmo não sendo agente público, induza ou concorra dolosamente para o ato; sócios, cotistas e diretores respondem se comprovada a participação dolosa (o STF afastou a exigência de 'benefícios diretos' do § 1º)".

### CORRIGIR

**N9 — P1-DA-7 · `texto` B1, última frase.**
- **Texto atual:** "…assim como a divergência interpretativa baseada em jurisprudência, ainda que não pacificada (§ 8º)".
- O STF manteve o § 8º "com ajustes": a interpretação precisa estar fundada em entendimentos, ainda que não pacificados, do próprio STF, dos tribunais superiores ou, na falta deles, em decisões colegiadas de tribunais de segunda instância (notícia de 28/05/2026).
- **Redação proposta:** "…assim como a divergência interpretativa fundada em entendimento, ainda que não pacificado, do STF, dos tribunais superiores ou, na falta deles, de decisões colegiadas de segunda instância (§ 8º, com a leitura do STF nas ADIs 7.156 e 7.236)".

**N10 — P1-DA-7 · `fontes` e `fluxo`/`box` em geral.**
- Acrescentar a fonte "STF, ADIs 7.156 e 7.236 (julgamento concluído em 1º/7/2026): notícias oficiais de 28/5, 24/6, 25/6 e 1º/7/2026", e a nota de que o acórdão está pendente de leitura.
- Pontos do mesmo julgamento que a banca cobrará e que podem entrar como SUGESTÃO, depois de conferidos:
  - a proibição de contratar alcança os três níveis da federação: o STF invalidou a limitação ao ente lesado do art. 12, § 4º;
  - a ação de improbidade tem natureza civil (art. 17-D, interpretação conforme);
  - a lei dos partidos políticos não exclui a Lei de Improbidade.

**I1 — Etiquetas de cobrança (ponto 4 do pedido).**
- O renderizador e a ESPEC §4 fazem assim: com 0 questões, "nenhuma questão enquadrada neste item no corpus"; com 1 a 3, "poucas questões deste item no corpus", e o número exato só na nota ao toque.
- Medido na prévia:
  - 8, 8.1, 8.4, 9.3 e 9.4 → "nenhuma questão enquadrada";
  - **8.3 (3), 9.1 (1) e 9.2 (2) → "poucas questões deste item no corpus"**, sem o número na etiqueta;
  - 7 → "95 questões … (75 C/E)"; 8.2 → "38 … (28 C/E)".
- O comportamento está certo. A triagem (seção 0) diz que 8.3, 9.1 e 9.2 "ficam com o número"; corrigir a frase da triagem.

### SUGESTÃO

**D1 — P1-DA-8 · `box` "Sem datas e sem autor fundador".**
- "A banca costuma pedir a ordem…" é afirmação de frequência sem lastro: o item tem 0 questões no corpus de 2025.
- **Redação:** "Pergunte a ordem (patrimonialista, burocrática, gerencial) e a fonte inspiradora de cada um (hierarquia; mercado)."

**D2 — P1-DA-8.1 · `pegadinhas` [2].**
- O "Certo" ("O curso não afirma substituição, data nem autor de origem") não corrige o "Errado" no plano do conteúdo: é uma nota de curso.
- **Redação:** "Certo: A NPG tem as redes como princípio orientador (Bouckaert); as fontes do curso não datam sua origem nem afirmam que tenha substituído a NPM."

**N11 — P1-DA-8.3 · `mapa` ramo "Decreto 9.203, art. 4º, VIII e IX" e `pegadinhas` [2].**
- O inciso IX trata de "editar e revisar atos normativos … realizando consultas públicas sempre que conveniente". O contexto (atos normativos) não aparece, e a banca pode explorá-lo.
- **Redação:** "na edição e revisão de atos normativos, consultas públicas sempre que conveniente (IX)".

**N12 — P1-DA-9.4 · `mapa` CIG, ramo "Quórum".**
- Citar o dispositivo: "(art. 8º-B, §§ 1º e 2º)". Texto conferido: "quórum de reunião … maioria simples … quórum de aprovação … maioria absoluta"; "voto de qualidade em caso de empate".

**N13 — P1-DA-9.4 · `linhaTempo` "Artigos com letra".**
- Confere com o texto oficial: arts. 7º a 15 originais sobre o CIG (7º a 12), os órgãos (13) e os comitês internos (14 e 15); revogação pelo **Decreto 9.901/2019**; art. 20-A acrescido em 2019 e revogado pelo **Decreto 10.756/2021**.
- Sugestão: nomear os dois decretos nos marcos.

**P1 — Processo (D-CONFERIDO-LITERAL não basta para leis sob controle concentrado).**
- A evidência literal prova o **texto**, não a **validade**. Regra proposta: para toda lei com ADIs pendentes ou julgadas sobre os dispositivos citados ("Vide ADI…" no texto da Câmara ou ADI conhecida), a produção confere no portal do STF a situação de cada dispositivo antes de gravar `conferido`, e registra o resultado na evidência.
- Na Lei 8.429, isso vale também para o canon (pacote v1.14, P1-DA-7) e para o **banco de questões** do item 7.
- Itens cujo gabarito dependa do art. 23, § 5º; do art. 17, §§ 10-C, 10-D e 10-F; do art. 16, §§ 3º e 4º; do art. 12, §§ 1º e 4º; do art. 17-B, § 3º; do art. 17-C, § 2º; do art. 21, § 4º; ou do art. 3º, § 1º, precisam de revisão (GBQ/GCB, AGORA, porque a prova é em 17/1/2027).

## Itens 8 e 9: conferência contra o canon e o decreto (ponto 2 do pedido)
- **8 (`linha`, `compare`, `mapa`, `box`):** nada além do canon. A única marca temporal é "anos 80, nos países centrais" (Bresser-Pereira), mais "monarquias absolutas". Ver D1.
- **8.1 (`esquema`, `compare`, `dois`, `escala`):** a escala "hierarquia → mercado → redes" está rotulada "Sequência de inspiração (Cavalcante, Ipea, 2018), sem datas" e "não cronologia", como o canon. A convenção de siglas e o "o que não se afirma" coincidem com o canon. Ver D2.
- **8.2:** PPP (Lei 11.079, art. 2º, caput e §§ 1º a 3º, bloco `lei` igual ao baseLegal) e vedações (valor inferior a R$ 10 milhões; prazo inferior a 5 anos; objeto único de mão de obra, equipamentos ou obra), como no canon. Termos de colaboração e de fomento e acordo de cooperação (Lei 13.019) e OS/OSCIP (3 anos, ato vinculado), como no canon.
- **8.3:** coprodução (Lui et al.), transparência ativa × passiva (rótulos do TCU e do Guia), Decreto art. 4º, VIII, IX e XI. Confere; ver N11.
- **8.4:** valor público (art. 2º, II, parte inicial) × cadeia de valor (CGU, Martins, Casa Civil). Confere.
- **9.1:** conceito do art. 2º, I, em quatro blocos; governança × gestão e governabilidade × governança (TCU), como no canon. O título do compare perdeu a página do TCU, o que é correto pelo checador.
- **9.2:** "competência e motivação não são princípios": confere, porque o art. 5º, I, a a d, lista integridade, competência, responsabilidade e motivação como condições da liderança, e o art. 3º, I a VI, não traz competência nem motivação. Rol fechado de três mecanismos; art. 6º e parágrafo único; comitês internos (art. 15-A). Confere.
- **9.3:** definição inteira do art. 2º, II; art. 4º, I, III e VII ("sempre que possível", "prioritárias"); art. 6º, parágrafo único, I. Confere.
- **9.4:**
  - âmbito federal direto, autárquico e fundacional (art. 1º); seis princípios, onze diretrizes e três mecanismos;
  - CIG: art. 7º-A, reuniões trimestrais (art. 8º-B), quórum (§§ 1º e 2º), grupos de trabalho (art. 10-B, II a IV), participação não remunerada (art. 12-A);
  - arts. 13-A e 15-A; art. 17 (quatro princípios) e art. 19 (quatro eixos);
  - revogações de 2019 e 2021.
  - **Tudo confere com o texto oficial lido hoje** (ponto 3 do pedido). Ver N12 e N13.
- Pegadinhas de 8 e 9: o "certo" de todas é sustentado pelo canon ou pelo decreto, salvo a forma de D2.

## Item 7: o que confere (fora de N1–N9)
- Sujeitos: arts. 1º (caput e §§ 1º a 3º e 5º a 8º) e 2º com parágrafo único; art. 3º, caput e § 2º (Lei 12.846).
- Sucessão: arts. 8º e 8º-A.
- Tipos:
  - art. 9º ("e notadamente");
  - art. 10, caput ("efetiva e comprovadamente"), §§ 1º e 2º e inciso XXII, com o XXI e o art. 10-A revogados;
  - art. 11: rol fechado, incisos I, II, IX e X revogados, §§ 1º, 4º e 5º. O STF validou o dolo e o rol taxativo.
- Sanções: art. 12, I a III, §§ 2º, 5º e 9º.
- Representação e indisponibilidade: art. 14; art. 16 só no que não é N3.
- Processo: art. 17, caput (com ADIs 7.042/7.043), §§ 6º, 7º, 10-A, 14 e 19 (I, II e IV).
- Acordo e sentença: art. 17-B, caput, § 1º (I a III), §§ 4º, 6º e 7º; art. 17-C, caput, I, § 1º e § 3º.
- Trânsito em julgado e afastamento: art. 20, caput e §§ 1º e 2º.
- Independência: art. 21, I e II (ver N6 para o § 4º).
- Prescrição: art. 23, caput e §§ 1º a 4º, 6º e 7º.
- Todas as citações literais curtas entre aspas coincidem com o texto da Câmara e com a evidência da produção.
- **Legitimidade (ponto 1):** o box e as pegadinhas estão dentro do que a notícia oficial de 31/08/2022 sustenta: legitimidade ativa concorrente do MP e dos entes públicos lesados, que também podem celebrar o acordo de não persecução civil. "A pessoa jurídica interessada pode intervir (art. 17, § 14)" é texto da lei, não da notícia; está correto. O cidadão pode representar (art. 14), e a lei não lhe dá a ação.

## Interface e didática (pontos 4 e 5)
- **Interface:** sem defeito. Contraste, aria, 320 px, tema escuro, roteamento do botão, regressão e `t_janela20.js` estão em ordem. Etiquetas: ver I1.
- **Didática:**
  - registro, ícones e estrutura iguais aos das levas 1 e 2;
  - relâmpagos com 6 a 9 frases de até 140 caracteres (checa); tabelas com até 4 colunas;
  - pegadinhas sem rótulo de probabilidade;
  - fora D1 e D2, sem defeito.
  - Os blocos novos de 8 e 9 (`mapa`, `dois`, `escala`, `linhaTempo`) só reorganizam o canon, salvo a precisão de N13, que está correta no texto oficial.

## Contagem
BLOQUEIA 8 (N1–N8, todos em P1-DA-7) · CORRIGIR 3 (N9, N10, I1) · SUGESTÃO 6 (D1, D2, N11, N12, N13, P1).

## Veredito
**REPROVADO** por causa do P1-DA-7: oito blocos ensinam regras que o STF declarou inconstitucionais ou reinterpretou nas ADIs 7.156 e 7.236 (julgamento concluído em 1º/7/2026).

Os itens 8 e 9 (nove tópicos) estão **aprovados no conteúdo** e só têm sugestões. Se a Presidência quiser, podem seguir separados do item 7.

O item 7 precisa de R2 com:
- os oito blocos reescritos;
- as fontes do STF;
- leitura da ata ou do acórdão das ADIs 7.156 e 7.236 para o enquadramento por parágrafo, ou, na falta, as notícias oficiais citadas, com a ressalva "acórdão pendente".

## O que a produção deve mudar antes da R2
1. **N1:** art. 23, § 5º ("metade") fora como regra vigente; teto de 20 anos; marco do § 8º retirado até o acórdão; relâmpago [5] reescrito.
2. **N2:** fluxo [4] sem os §§ 10-C e 10-D; o enquadramento jurídico é do juiz.
3. **N3:** fluxo [2] sem o requisito de "perigo de dano"; bloqueio com indícios fortes, sem urgência.
4. **N4:** box do trânsito em julgado: perda de todas as funções, salvo exceção fundamentada.
5. **N5:** acordo de não persecução civil sem a oitiva obrigatória do Tribunal de Contas.
6. **N6:** box do art. 21: a absolvição criminal não encerra automaticamente; listar as hipóteses excepcionais.
7. **N7:** pegadinha [7] reescrita (ressarcimento solidário).
8. **N8:** mapa, ramo do terceiro: sem a exigência de "benefícios diretos".
9. **N9:** texto B1, art. 1º, § 8º com o ajuste do STF.
10. **N10:** fontes com as ADIs 7.156 e 7.236 e a ressalva "acórdão pendente".
11. **I1:** frase da triagem sobre as etiquetas de 8.3, 9.1 e 9.2.
12. **P1:** aplicar a regra de validade em controle concentrado à evidência da Lei 8.429 e despachar à GCB/GBQ a revisão do canon e do banco do item 7 (AGORA).
13. **Sugestões D1, D2, N11, N12, N13:** a critério da produção.
