# QA — Resumo visual de Direito Administrativo, leva 1 + plataforma v17.3 — R2 (28/10/2026)

QA Opus (qa-normativo-da, gcb-cqfp-didatico, QA-plataforma), com as mesmas regras da R1. Não editei nada em /home/claude/v17_3/; este relatório é o único arquivo criado lá. Os testes que reproduzem scripts da pasta foram rodados a partir do scratchpad, para não regravar `caps/`.

## Cabeçalho

**Hashes (sha256), conferidos com a mensagem da coordenação**
| Arquivo | sha256 |
|---|---|
| resumo_visual_leva1.py | ad32178b224f682d04d6affdf3e1907a263f46d5516c3cd0fca03963ca1ad348 |
| resumo_visual_leva1.json | f2f0adbf0ace5b1c92130e2dbb929756a064eaae0cd37bd39b609a846fb0e5ac |
| checa_resumo_visual.py (v1.1) | e72bedb2fea6a754168dcde865ab4cb6fd81e765953ba3d45c9b6905b31689f9 |
| patch_v17_3_resumo_visual.py | d3aa4700649e198633de8d6d022da3b7ac68c7ace9c096e2ae150a4d546254ad |
| plataforma_v17_3_template.html | 0f3ae578328c52aa0563f7955fa8e3c00de07e65150393a5a9a67dd9e4e63bed (patch reaplicado sobre o v17.2 89f07db1…: mesmo hash, 6 substituições) |
| pacote_previa_v114_rv1.json | 10f259502d2e0fbfac865333c26cc83c45103399e69f58459a96fb9df4349764 |
| plataforma_v17_3_previa.html | dbed1c90e593228100af75e2e6d0df3dcba84539ddf009ca657c665dc4c3be2b |
| extras_leva1_v114.json (canon, inalterado) | d5398fcd382ad3e2f289c35dac8de8e0654b9301982ff3f9e390ab4c1a98706d |
| ESPEC_resumo_visual_DA_v3 (emendada v3.1) | 015912531300f6871dddbe9aa44b022566be8898d0a9fc070b84ae746a2c4ed7 |

**Comandos executados**
- Diff do JSON R1 → R2 (dump legível): 323 linhas de diferença, todas lidas.
- `python3 -I checa_resumo_visual.py resumo_visual_leva1.json` → 0 bloqueios, 0 avisos; com `--pacote pacote_previa_v114_rv1.json` → 0/0; sobre o próprio pacote → 0/0.
- Mutação do checa v1.1: 18 casos (resultado em V5).
- `node regr_v17_3.js A B estado_antigo_v114.json` → telas 104 · 9 RV · 9 esperadas · **0 não esperadas** · 0 erros JS. Com `estado_antigo2_v114.json` → 110 · 9 · 9 · **0** · 0.
- `node t_janela20.js previa` → só a falha esperada `0.const` (v17.3); 0 erros JS.
- `node t_pir.js previa`, a partir do scratchpad → **0 falhas** em 320/390/1280 × claro/escuro (OL, role=group, rótulo "…, do topo à base", sem transbordo em `.nv` nem em `<b>`). Capturas próprias vistas: 390 e 1280, claro e escuro.
- Teste próprio com Playwright (o mesmo da R1) na prévia R2: 9 tópicos × {320 claro, 320 escuro, 390 escuro, 1280 claro} → contraste mínimo de texto 6,14 (claro) e 6,95 (escuro); ícones todos aria-hidden; sem rolagem horizontal; sem "30" ligado à nota; sem preto, azul, verde/vermelho ou emoji; "Resumo" abre a tela nova nos 9 tópicos e a antiga nos outros 70 (clique real em 2.1, 3.4 e 4.4); etiqueta "poucas questões deste item no corpus" em 1, 2.2, 3.2 e 3.3, e número com C/E nos demais.
- Fontes externas, consultadas em 28/10/2026:
  - **Câmara, Legin, Lei 13.848/2019, publicação original:** art. 42 dá ao art. 9º da Lei 9.986 os incisos I a III (renúncia; condenação judicial transitada em julgado ou condenação em PAD; descumprimento das vedações do art. 8º-B); o art. 52, VI, revoga o parágrafo único. Bate com o JSON.
  - **Câmara, Legin, Lei 15.371/2026, publicação original:** altera CLT, Lei 8.212, Lei 8.213 e Lei 11.770; sem menção a servidores nem à Lei 8.112; art. 11: 10/15/20 dias a partir de 1º/1/2027, 2028 e 2029 (a 3ª etapa condicionada à meta fiscal); vigência em 1º/1/2027.
  - **TJDFT, Boletim NUGEP n. 24/2019:** Tema 545 (RE 716.378), julgado em 07/08/2019. A tese diz que o regime público ou privado da fundação estatal depende do estatuto e das atividades, e que a estabilidade do art. 19 do ADCT não alcança as fundações de direito privado.
  - **ADI 191 e Decreto 10.835, art. 9º, §§ 2º e 3º:** não reconferi a ADI 191 no portal do STF (a citação é a corrente e eu a conheço com segurança: ADI 191/RS, rel. Cármen Lúcia, 2007/2008). Os §§ 2º e 3º do art. 9º do Decreto 10.835, aceitos pela conferência da produção na Câmara, não foram reconferidos por mim.
  - **Planalto:** continua inacessível daqui.

## Tabela das 7 verificações

| # | Verificação | Resultado | Evidência |
|---|---|---|---|
| 1 | Normativo | **DEFEITO** (1 ALTA, 1 MÉDIA) | Os defeitos normativos da R1 foram tratados e conferidos: D1, D2, D3, D4, D5, D6, D8, D9, D10, D11, D12, D14 (a lei confere com a Câmara) e D15 no mapa. **Novo:** N1 (legenda de 1.1 B10, razoabilidade "expressa" em contradição com a própria definição de implícito) e N2 (subtetos de 3.1 sem o do Legislativo estadual). |
| 2 | Fidelidade ao canon | **CONFERIDO com pendência** | Nada no JSON contradiz o `extras_leva1_v114.json`, salvo onde o canon errava (D2 "só", D33 anotação do art. 21), que o RV corrige. O despacho ao canon ainda **não** foi aplicado: o pacote v1.14 continua com "o estável só perde o cargo nas hipóteses do art. 41, § 1º" (N14). |
| 3 | Triagem | **CONFERIDO** | Nenhum erro listado na triagem no JSON; os três que tinham escapado na R1 (foro de autarquia, pirâmide da remuneração, "Povo") foram corrigidos. |
| 4 | Didático | **DEFEITO** (MÉDIA) | O Relâmpago de 1.2 ainda não tem centralização, embora a coordenação diga que tem (N3). Os encurtamentos para ≤ 140 caracteres tiveram perdas pequenas (N6, N7). Uma referência de produção ficou visível (N5). Tabelas ≤ 4 colunas; classificações com a pergunta que distingue (2.1 B9 agora separa "planos do ato" e "exequibilidade"). |
| 5 | Script | **DEFEITO** (MÉDIA) | v1.1 cobre os itens (i) a (x) da R1, mas o cruzamento com o baseLegal compara só `ref`: um `lei` com o texto adulterado ("dez anos" no art. 54) passa com `--pacote` (N4). |
| 6 | Interface | **CONFERIDO** | Pirâmide sem corte (t_pir 0/6 e capturas legíveis nos dois temas); a11y da pirâmide corrigida (role=group, `<ol>`); ícone da barra de seção no escuro agora em --on-strong (15,3:1); etiqueta conforme a ESPEC §4 (N9 BAIXA). Regressão 0/0; t_janela20 só com a falha esperada. |
| 7 | Estética × decisão (a) | **CONFERIDO** | Sem preto puro, azul fora do foco, verde/vermelho fora de C/E ou emoji. A família MapasPro continua reconhecível. No celular a pirâmide vira faixas de mesma largura (corte de 6%), o que perde um pouco a forma, mas é aceitável para manter a leitura. |

### Pontos pedidos pela coordenação
- **D2 (art. 169, § 4º): CONFERIDO.** O marco "Perda" cita o art. 41, § 1º, e o art. 169, §§ 4º e 5º (ato normativo motivado; indenização de um mês de remuneração por ano de serviço, § 5º); relâmpago [4] e pegadinha nova corretos. Pendência no canon: N14.
- **D3: CONFERIDO.** Título "O que o servidor pode receber (art. 49)"; indenizações "não integram a remuneração nem se incorporam (art. 49, § 1º)"; gratificações e adicionais "incorporam-se nos casos e condições da lei (art. 49, § 2º)"; legenda e relâmpago com "vantagens pecuniárias permanentes (art. 41)".
- **D5: CONFERIDO** na Câmara, na publicação original da Lei 13.848 (arts. 42 e 52, VI).
- **D9: CONFERIDO** (Tema 545 / RE 716.378, pelo boletim oficial do TJDFT; ADI 191 pela citação corrente, sem reconferência no portal do STF). O texto respeita o DL 200, art. 5º, IV (direito privado), e a pegadinha nova está correta.
- **D14: CONFERIDO.** A Lei 15.371/2026 não altera a Lei 8.112. Ressalva BAIXA: o JSON diz que ela altera "a CLT e a Lei 8.213"; altera também a Lei 8.212 e a Lei 11.770 (N8).
- **Pirâmide: CONFERIDO** (ver V6).
- **Etiqueta de cobrança: CONFERIDO** (ver V6). Ressalva: o 2.2 tem 0 questões e a etiqueta diz "poucas" (N9).
- **Frases novas e encurtadas:** lidas todas. Defeitos em N1, N2, N3, N5, N6, N7, N10 e N15.

## DEFEITOS (numeração própria da R2: N1…)

### ALTA
**N1 — P1-DA-1.1 · B10 (mapa "Princípios que a banca cobra além do LIMPE"), legenda e ramos [3] e [4].** A legenda diz: "Implícito é o que a CF não escreve; contraditório e razoabilidade são expressos (CF, art. 5º, LV; Lei 9.784, art. 2º)." Os ramos dizem "Razoabilidade e proporcionalidade (Lei 9.784, art. 2º)" e "Segurança jurídica (Lei 9.784, art. 2º)". Pela definição da própria legenda (implícito = o que a CF não escreve), a razoabilidade, a proporcionalidade e a segurança jurídica são **implícitas na CF**. São expressas só na Lei 9.784. A frase leva a marcar Errado num item clássico da Cebraspe ("razoabilidade e proporcionalidade são princípios implícitos na Constituição": Certo). É defeito introduzido pela correção de D15. **Correção:** "Implícito na CF = não escrito na CF. Contraditório e ampla defesa são expressos na CF (art. 5º, LV). Razoabilidade, proporcionalidade e segurança jurídica são implícitos na CF, mas expressos na Lei 9.784/1999 (art. 2º). Prerrogativa é poder; sujeição é limite." Nos ramos [3] e [4]: "(implícito na CF; expresso na Lei 9.784, art. 2º)".

### MÉDIA
**N2 — P1-DA-3.1 · B7 (texto) e B11 [7].** "há subtetos nos Estados, no DF e nos Municípios (subsídio do Governador, do Prefeito, dos Desembargadores, conforme o Poder)". O art. 37, XI, tem quatro subtetos: Prefeito (Municípios); Governador (Executivo estadual e distrital); **Deputados Estaduais e Distritais (Legislativo)**; Desembargadores do TJ, limitado a 90,25% do subsídio dos Ministros do STF (Judiciário, aplicável ao MP, aos Procuradores e aos Defensores). A enumeração "conforme o Poder" omite o Legislativo. **Correção:** listar os quatro, com o limite de 90,25%, ou dizer só "há subtetos por ente e por Poder (art. 37, XI)". A faculdade do § 12 é opcional.

**N3 — P1-DA-1.2 · B15 (relâmpago).** A coordenação informa que o relâmpago "agora tem" concentração e centralização, mas a frase [1] tem só "Concentração: menos órgãos". **Centralização** continua ausente do Relâmpago, e ela está no texto do item do edital (resíduo de D18). **Correção (≤ 140 caracteres):** por exemplo, "Centralização: o ente presta por seus órgãos; concentração: menos órgãos (oposto da desconcentração)." numa frase própria (há espaço: 10 frases é o máximo, e [2] pode ser fundida com [3]).

**N4 — Script, cruzamento com o baseLegal (ESPEC §5.7).** `checa_resumo_visual.py --pacote` compara só a `ref` do dispositivo. Mutação: art. 54 com "dez anos" no lugar de "cinco anos" → **0 bloqueios**. Um bloco `lei` com texto adulterado passa. **Correção:** comparar também `texto` (igualdade após normalizar espaços) e `literal`; divergência = bloqueio.

### BAIXA
- **N5 — P1-DA-2.1 · B5, legenda:** "(o pacote traz os três primeiros; a tipicidade é acréscimo de Di Pietro)". "O pacote" é referência interna, sem sentido para a candidata (mesma família do D13). Trocar por "três atributos são consenso; a tipicidade é acréscimo de Di Pietro".
- **N6 — P1-DA-3.4 · B13 [2]:** o relâmpago perdeu o aviso "reverificar (T-120)". O decreto (norma infralegal) e a lei divergem, e a questão está aberta no Projeto; a linha do tempo mantém o aviso, o relâmpago não. Acrescentar "— T-120: reverificar".
- **N7 — P1-DA-2.1 · B16:** o relâmpago perdeu a decadência de cinco anos (art. 54), parte de "nulidades". A frase [9] de extinção omite "desaparecimento do sujeito ou do objeto", que está na tabela B13.
- **N8 — P1-DA-3.4 · B7 e `fontes`:** "a Lei 15.371/2026 … altera a CLT e a Lei 8.213". Altera também a Lei 8.212 e a Lei 11.770 (Câmara, publicação original). A conclusão ("não a Lei 8.112") está correta.
- **N9 — Etiqueta do P1-DA-2.2:** com 0 questões, a etiqueta diz "poucas questões deste item no corpus". O número exato está na nota ("0 questões enquadradas"), conforme a ESPEC §4, mas "poucas" para zero é impreciso. Sugestão: "nenhuma ou poucas questões".
- **N10 — P1-DA-3.1 · B10.a [1]:** "Norma de eficácia plena: não depende de lei" (sindicalização, art. 37, VI). É a posição majoritária, mas sem rótulo de doutrina. Acrescentar "(doutrina)".
- **N11 — Script, outros casos que passam:** `conferido` "2026-13-45" (regex só de forma); "Exemplos de SEM: Petrobras, Vale." (o termo vedado exige "economia mista" a até 40 caracteres); "Tema quente: cai em toda prova"; número sem norma no mesmo bloco ("O prazo é de 45 dias."), regra da ESPEC §3 que fica só para o QA.
- **N12 — ESPEC v3.1, processo:** os limites foram afrouxados pela produção depois do QA (mapa: ramo de "até 90" para título ≤ 60 e texto ≤ 180; dois: 2–6 para 2–7), de modo a caber o conteúdo existente. A justificativa do 2–7 (arts. 8º e 33) é boa, mas a emenda deve ir com ciência à Gerência (quem produz não aprova a própria régua).
- **N13 — Rastreabilidade:** a ADI 191 e o Decreto 10.835, art. 9º, §§ 2º e 3º, não foram reconferidos em fonte oficial nesta rodada (o portal do STF não foi aberto; os parágrafos do decreto foram aceitos pela conferência da produção). Registrar no `fontes` a data e o local da conferência da ADI 191 quando houver.
- **N14 — Canon (fora do objeto, pendência):** o pacote v1.14 (P1-DA-3.1, resumo e emUmMinuto[2]) ainda diz "o estável só perde o cargo nas hipóteses do art. 41, § 1º", e a anotação "(prazo 3 anos - vide EMC nº 19)" continua no baseLegal do art. 21 (3.4). O despacho à Secretaria de Estado Canônico precisa ser executado antes da próxima publicação do pacote; o curso e o resumo em prosa continuam mostrando o texto antigo.
- **N15 — P1-DA-3.1 · B5 (mapa, alínea c):** "Dois cargos ou empregos de profissionais de saúde — privativos de profissões regulamentadas" deslocou o "privativos". O texto constitucional é "dois cargos ou empregos privativos de profissionais de saúde, com profissões regulamentadas". Usar a redação literal (a banca cobra a letra).

## Situação dos defeitos da R1
- **Corrigidos e conferidos:** D1, D2 (no RV), D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D16, D17, D19 (i–x), D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30, D31, D32, D33 (no RV), D34 e D35.
- **Corrigidos com resíduo:** D15 (a legenda nova gerou N1); D18 (falta a centralização: N3); D19 (cruzamento só por ref: N4); D2 e D33 no canon (N14).

## Contagem
BLOQUEIA 0 · ALTA 1 · MÉDIA 3 · BAIXA 11 (total 15).

## Veredito
**APROVADO COM RESSALVAS.** A publicação fica condicionada à correção de N1, uma legenda e dois títulos de ramo, com verificação pontual pela QA e sem nova rodada completa. N2, N3 e N4 devem entrar no mesmo ciclo. As BAIXA podem ir para a leva 2. A plataforma (renderizador, pirâmide, etiqueta, regressão) está aprovada sem ressalva de interface.

Fontes externas desta rodada (28/10/2026): Câmara dos Deputados, Legislação Informatizada, Lei 13.848/2019, publicação original (www2.camara.leg.br/legin/fed/lei/2019/lei-13848-25-junho-2019-788523-publicacaooriginal-158408-pl.html); Câmara, Lei 15.371/2026, publicação original (www2.camara.leg.br/legin/fed/lei/2026/lei-15371-31-marco-2026-798908-publicacaooriginal-178711-pl.html); TJDFT, Boletim Informativo NUGEP n. 24, 09/08/2019 (Tema 545).
