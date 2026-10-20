# QA_final_v1_13_v16_2026-10-20_gbq-cqe.md — ordem do Fundador 20/10/2026 — 2026-10-20 — gerado por gbq-cqe

QA independente do pacote v1.13 (v1.12 + Direito Administrativo, P1-DA) e da plataforma v16 final. A gbq-cqe não produziu nem reconciliou nenhum dos objetos. Os objetos não foram alterados e não há commit. Todas as conferências usaram scripts próprios, sem reaproveitar a lógica de `montar_v1_13.py`, `diag30_da.py` nem `build_plataforma_v16.py`. O único script de terceiros executado foi o validador `validar_da.py`, como a ordem pede.

## 0. Vereditos

| Objeto | Veredito | Bloqueia a publicação? |
|---|---|---|
| Pacote v1.13 (`pacote.json` e `pacote_estudante.json`) | **ACEITO COM RESSALVAS** | **Sim, até corrigir o achado 1** ("folha" e metatexto de produção no texto exibido de DA). Os achados 2 e 3 bloqueiam só o aceite canônico do `pacote_estudante.json` e do contrato, não a plataforma. |
| Plataforma v16 (`plataforma_v16_final.html` / `plataforma_v16_publicar.html`) | **ACEITO COM RESSALVAS** | O código passou em todos os testes. O arquivo atual embute o pacote com o achado 1, por isso precisa ser remontado com `build_plataforma_v16.py` depois da correção. Publicar continua reservado ao Fundador (D-V15-PLATAFORMA). |

## 1. Objetos conferidos (SHA-256 dos bytes em disco)

| Arquivo | Bytes | SHA-256 |
|---|---|---|
| saida/pacote/montagem_v1_13/out/pacote.json | 2.907.286 | 442741d85e19cdc3f104497ed4d3a9ca2d18ff2fd090292e477196404f160b5c |
| saida/pacote/montagem_v1_13/out/pacote_estudante.json | 2.645.784 | 01ebe3a8e5d09999c3aa085a147fd37679a4e3c3e881380a661c66a1a117f5a4 |
| saida/pacote/montagem_v1_13/out/diag30_DA.json | 988 | eb1ced6df3d624ae62b82337db6a4cfe29b86baa9494e96aed1b3defe61a6800 |
| saida/plataforma/plataforma_v16_final.html | 2.822.586 | b14fda941fbde16928101a205dbea21fa38e1ed59e31da26a7c0034d8e847cb3 |
| saida/plataforma/plataforma_v16_publicar.html | 2.822.040 | 053438e70d0980dd4747a487e33c5c7f458021d88854a8373247a8cc4fd99197 |
| saida/plataforma/plataforma_v16_final_template.html | 128.081 | c6de3f2a699597e124540eb4a59f451938ba44da9fa9c86d2a6e4b9d5fc0b46c |
| Referência: plataforma_v15_4_publicada_2026-10-19.html | 1.374.001 | 361e00efe1caee12a1ab8198ecec539861a11ed63bc79d01c2f8abee5f061873 |
| Referência: gerador_v1_12/out/pacote.json | — | 3476525319b027fe4427bf93598d516087ad6f18fb8dd5bbed4ad8c04be6024f |

Scripts da gbq-cqe, rodados com `python3 -I`, ficam fora do repositório, em `/tmp/claude-0/-home-claude/9f60db71-6d00-590f-a17d-a2a9f6b75e58/scratchpad/qa/`:
- `chkA.py`: conferência A;
- `chkB.py`: B e C, com parse próprio dos canônicos;
- `amostra.py`: resumos de tópico;
- `pw_v16.py`: conferência D, com Playwright e Chromium 1194 de `/opt/pw-browsers`, servidor `http.server` em 127.0.0.1:8766 e fontes do Google respondidas vazias;
- `dbg12.py` e `dbgpr.py`: verificações pontuais.

Os resultados brutos estão em `resA.json`, `resB.json` e `resD.json`, no mesmo diretório.

## 2. Conferência A: v1.12 intacta dentro da v1.13

Resultado: **OK nos dois arquivos.** A comparação é por objeto: cada objeto foi serializado com a ordem de chaves original, e os dois arquivos usam a mesma serialização (indent=1 + LF, conferida nos bytes). Com isso, o texto de cada objeto da v1.12 aparece igual, byte a byte, na v1.13.

| Bloco | pacote.json | pacote_estudante.json |
|---|---|---|
| Itens da v1.12 (mesma posição) | 749/749 idênticos | 749/749 idênticos |
| Lotes da v1.12 | 10/10 idênticos | 7/7 idênticos |
| Edital P1/P2 (ordem relativa mantida) | 47/47 idênticos | 47/47 idênticos |
| Simulados | 4 idênticos | 4 idênticos |
| Discursivas | 5 idênticas | 5 idênticas |
| Tópicos da v1.12 (ordem relativa mantida) | 40/40 idênticos | 40/40 idênticos |
| `versao` / ordem das chaves de topo | 1 / igual | 1 / igual |

Além disso:
- Os 410 itens, os 6 lotes e os 39 tópicos acrescentados são idênticos, byte a byte, aos de `D1..D6_plataforma.json`.
- O edital DA é igual a `edital_DA.json` e forma um bloco contíguo, logo depois do último P1 de TI (posições 20 a 65).
- `topicos` segue a ordem do edital e é o último campo.
- Só mudam `nome` e `geradoEm`. No `pacote_estudante.json`, o nome mudou de forma indevida (achado 2).

## 3. Conferência B: Direito Administrativo

### 3.1 Edital
O edital tem 46 entradas P1-DA. O id e o texto de cada uma são literais de `edital/DA_itens_1_12_P1.md`, conferidos por parse próprio da linha do edital: **0 diferenças**. Todas têm `prova` "P1" e os campos `id`, `prova` e `texto`.

### 3.2 Itens (410)
Os enunciados e gabaritos foram comparados com os canônicos D1_v2, D2_v2_1, D3_v2_1, D4_v2_1, D5_v2_1 e D6_v2_1. O parse é próprio: enunciado da seção 5.1 e gabarito da seção 5.2.

| Lote | Itens (esperado) | Enunciado ≠ canônico | Gabarito ≠ canônico | C/E | Voláteis |
|---|---|---|---|---|---|
| D1 | 60 (60) | 0 | 0 | 30/30 | 0 |
| D2 | 80 (80) | 0 | 0 | 40/40 | 2 (D2 com REVERIFICAR=sim) |
| D3 | 71 (71) | 0 | 0 | 31/40 | 0 |
| D4 | 79 (79) | 0 | 0 | 41/38 | 0 |
| D5 | 70 (70) | 0 | 0 | 35/35 | 0 |
| D6 | 50 (50) | 0 | 0 | 25/25 | 3 (D6-09, D6-32, D6-34; REVERIFICAR) |

Demais conferências dos itens:
- **Ids:** os 1.159 ids do pacote são únicos.
- **`itemEdital`:**
  - todos os valores existem no edital;
  - todos são iguais à folha ou ao subitem do cabeçalho do item no canônico (D6: LAI → 11, LGPD → 12);
  - 14 itens estão em caput com subitens (P1-DA-1: 8; P1-DA-8: 6), como o FORMATO admite.
- **`volatil`:** coincide com a marca VOLÁTIL/REVERIFICAR do canônico em 410/410.
- **Campos fixos:** `rotulo`, `aderencia`, `certame`, `ano`, `numero` e `url` (= arquivo canônico) estão corretos.
- **Ordem:** os itens seguem a ordem dos ids, como pede o FORMATO, seção 4. Em D3 e D5, a ordem de apresentação do canônico é outra (teste de sequência), o que não é achado.
- **Justificativas:** 307 são iguais à junção das linhas 1 e 2 do canônico. As outras 103 diferem só por operações registradas em `D<n>_registro_formato.md`:
  - D4, 39 itens: o código R1–R31 foi trocado pelo nome da publicação. Conferi a correspondência com a tabela do Anexo N do D4 (R1/R2 Bresser-Pereira, R4/R10/R13/R15/R23 Guia da Casa Civil, R12 Cavalcante, R16 CGU, R17 Martins, R18/R30/R31 guia ex post, R19–R24 TCU), e ela está correta;
  - D6, 34 itens: "[TS]" virou "a troca sutil", e as frases "Difere de BQ-…" foram deletadas;
  - D2 e D5: "elemento-isca" virou "elemento que parece trocado";
  - D1, D2, D3 e D5: "Não há troca:" virou "Não há troca;";
  - deleções de oração de processo em D1-09, D2-74, D4-36, D4-48, D4-67, D6-09 e D6-34.

### 3.3 Validador `validar_da.py`
Rodou nos seis lotes, com o canônico e o Anexo N de cada um: **0 FALHA e 0 AVISO** nos seis.

Quadros por lote (DEFINIÇÃO/BASE LEGAL):

| Lote | DEFINIÇÃO | BASE LEGAL |
|---|---|---|
| D1 | 26 | 22 |
| D2 | 109 | 109 |
| D3 | 63 | 49 |
| D4 | 62 | 62 |
| D5 | 58 | 58 |
| D6 | 47 | 47 |

Observação de método: o validador procura "R" só como R1/R2, não tem "folha" na lista e confere o enunciado por substring. Por isso a varredura abaixo usou uma lista própria, mais ampla.

### 3.4 Varredura de marcas de produção (seção 6 e lista da ordem)
Foram lidos 3.282 campos de texto exibido de DA:
- nome, resumo, curso, pares e pegadinhas dos lotes;
- comando, textoBase, enunciado e justificativa dos itens;
- emUmMinuto, resumo e todo texto de visual dos tópicos;
- texto do edital.

Resultado: **0 ocorrências** de todas as marcas, salvo "folha":
- "Lote" e "lote D";
- ids D1–D6-NN, BQ-, L…/A5/6A/4C/5C;
- códigos C…-NN, L7., G12., G-07, P-03 e PARTE n;
- F1–F22 e [F…, [V …, "NORMATIVO — QA", "QA PENDENTE", "trecho importado";
- REVERIFICAR, VOLÁTIL, [TS] e "elemento-isca";
- BASE DOUTRINÁRIA, "Anexo N", "mapa normativo", "ficha" e "seção n";
- **R1–R31**, v1/v2 e "acatado";
- unidades, agentes e ferramentas de IA, "SEM FONTE", T-nn e D-XXX.

As 197 ocorrências de "troca:" são todas da forma prescrita "Como a banca troca:" dos pares. "Mecanismo:" aparece 1 vez como conteúdo ("o objetivo do mecanismo: reduzir"), o que é falso positivo. "**folha" aparece 23 vezes** (achado 1).

### 3.5 baseLegal
São 105 dispositivos em 29 visuais, todos `literal: true`:
- **105/105** têm o texto letra a letra no Anexo N do lote. A comparação só normaliza espaços, sem retirar aspas, negrito nem pontuação, ao contrário do validador.
- **105/105** têm o `conferido` igual à data de consulta do mapa para aquele trecho (17/10, 18/10 ou 20/10/2026, conforme o lote).
- O artigo do `ref` é o da linha do mapa em 105/105.
- O artigo é citado no bloco `##` do curso do próprio tópico em 105/105.

### 3.6 Amostra de 15 resumos de tópico contra o curso
Tópicos da amostra: 1, 2.1, 3.1, 3.4, 4.3, 5.2, 6.3, 7, 8, 8.4, 9.4, 10.1, 10.6, 11 e 12, com 195 a 249 palavras. O método foi automático, com leitura das frases marcadas: todo número do resumo está no bloco do curso, e as frases com menos de 75% de palavras de conteúdo presentes no bloco foram lidas uma a uma, contra o curso.

Resultado: **14/15 sem fato novo**. As frases marcadas em 3.1, 9.4, 10.1 e 10.6 estão no curso (art. 41, § 1º; art. 8º-B, trimestral; art. 28, § 2º; art. 7º, § 2º). A exceção é o 8.4 (achado 6).

## 4. Conferência C: diagnóstico DA (`diag30_DA.json`)
**OK em todos os critérios:**
- 30 ids distintos, todos existentes, todos de DA e todos em folha do edital;
- nenhum volátil, todos de aderência direta e nenhum em simulado;
- pelo menos 1 por item do edital 1 a 12: {1: 2, 2: 2, 3: 3, 4: 3, 5: 2, 6: 4, 7: 1, 8: 3, 9: 3, 10: 5, 11: 1, 12: 1};
- C/E 15/15, igual ao declarado, e folhas declaradas iguais ao `itemEdital` dos itens;
- a lista `DIAG30.DA` do template final é idêntica a `diag30_DA.json`, e as listas P1 e P2 são as da v15.4.

## 5. Conferência D: plataforma v16 (Playwright, 390×844 e 1280×900, claro e escuro)

### 5.1 Montagem e arquivo de publicação
- `plataforma_v16_final.html` é **byte a byte** igual a `build(plataforma_v16_final_template.html, pacote.json v1.13)`, refeito por script próprio com a mesma regra de serialização.
- O template final difere do `plataforma_v16_template.html` só na meta `mapaspro:versao` e na lista `DIAG30.DA`.
- `plataforma_v16_publicar.html` é **exatamente o corpo** de `plataforma_v16_final.html`: é o final sem a primeira linha (o esqueleto `<!doctype…><body>`, idêntico ao da v15.4 publicada) e sem o `\n</body></html>` final. A primeira linha e o fim do arquivo têm a mesma forma da cópia publicada da v15.4.

### 5.2 TI e Fala: v16 final × v15.4 publicada — iguais

| | v15.4 | v16 final |
|---|---|---|
| TI: tópicos com curso / itens | 17 / 185 | 17 / 185 |
| Fala: tópicos com curso / itens | 23 / 564 | 23 / 564 |
| Itens por tópico e numeração | — | iguais |

- **Render dos 5 tópicos de cada módulo** (HTML de `#app`):
  - TI P1-1, P1-2, P1-2.1, P1-3 e P1-4: hashes iguais (ex.: P1-1 5509003f4e5c = 5509003f4e5c);
  - Fala P2-1.1 a P2-1.5: hashes iguais (ex.: P2-1.4 f1d54896709b = f1d54896709b).
- **Além da amostra:** os 40 cursos, os 40 resumos de tópico e as telas da matéria TI, da matéria Fala e de Erros estão idênticos.
- **Painel, Prática e Disciplinas** diferem só pelos acréscimos de DA:
  - "0 de 80 tópicos" no lugar de "0 de 41";
  - cartão "39 tópicos";
  - diagnóstico DA na lista e no botão.

### 5.3 Direito Administrativo
- **Tópicos e itens:** 39 tópicos com curso e 410 itens no módulo. A numeração exibida vai de 1 a 12, sem "DA-". TI continua com 185 itens e Fala com 564.
- **Matéria:** 9 grupos (1 a 6, 8, 9 e 10). Os itens 7, 11 e 12 aparecem como tópicos, porque não têm subitens.
- **Os 39 tópicos com curso foram abertos** nos 4 cenários (156 aberturas), com estes resultados:
  - 0 erros e 0 avisos de console, em todo o teste, inclusive nas páginas da v15.4;
  - quadros DEFINIÇÃO, BASE LEGAL, EXEMPLO e PEGADINHA renderizados em número igual ao de rótulos do bloco `##`, em 39/39;
  - "Em 1 minuto" com 3 itens, em 39/39;
  - visuais desenhados no tipo e na ordem do JSON, em 39/39, com 0 figuras vazias. São 29 baseLegal (número de dispositivos igual ao do JSON), 23 compare, 13 tabela, 9 esquema, 3 fluxo e 1 linha. O detector marcou 4.2 e 7 como "compare", mas é falso positivo: são tabelas com a primeira coluna "Aspecto" e saem como tabela;
  - nenhum `###` em maiúsculas, nenhum rótulo solto e nenhum "DA-" no texto;
  - um único markdown cru: o "**e**" de uma pegadinha do 12 (achado 5).
- **Prática em blocos de 10 questões:**

  | Tópico | Cenário | Correções | Nota (= esperada) |
  |---|---|---|---|
  | 3.4 | 390 claro | 10 | 4 |
  | 7 | 390 claro | 10 | 4 |
  | 10.1 | 390 claro | 10 | 4 |
  | 9.4 | 1280 escuro | 10 | 4 |

  Em todos, os itens são distintos e todos do tópico, há 7 acertos e 3 erros, e o rótulo da correção é "tópico N".
- **Diagnóstico DA (390 claro e 1280 escuro):**
  - o botão "Fazer diagnóstico · 30 itens" abre o `D30-DA` com 30 itens, na ordem de `diag30_DA.json`;
  - a correção sai certa: 19 acertos, 10 erros e 1 em branco, igual ao esperado, com nota 9;
  - há 30 correções e 30 tópicos no resultado.
- **Rolagem horizontal a 390 px:** nenhuma, nos dois temas. Telas conferidas:
  - matéria DA e os 39 cursos;
  - resumo, resumo do tópico 10.6 e painel;
  - questão, resultado, diagnóstico, erros e recomendações.

  A 1280 px também não houve rolagem.

### 5.4 Tempo de carga
Medido em servidor local, de `goto` até o app pronto, em 3 medições por caso:

| Arquivo | Tamanho | 390 px | 1280 px | DOMContentLoaded |
|---|---|---|---|---|
| v16 final | 2,82 MB | 258 / 881 / 268 ms | 303 / 257 / 254 ms | cerca de 230 ms |
| v15.4 | 1,37 MB | 190 / 165 / 204 ms | 164 / 157 / 164 ms | cerca de 130–160 ms |

O tempo é razoável: cerca de 100 ms a mais que a v15.4, com um caso isolado de 881 ms. O tempo de rede para baixar 2,8 MB no aparelho da candidata não foi medido, porque o servidor é local.

### 5.5 Screenshots
São 28 arquivos em `saida/plataforma/testes_v16_final/`:
- 01: disciplinas;
- 02: matéria;
- 03: cursos 3.1, 10.1, 4.3, 12, 8 e 9.4, nos 4 cenários;
- 04: visuais baseLegal, compare, tabela, esquema, linha e fluxo;
- 05: quadros;
- 06: resumo de tópico;
- 07: painel;
- 08 e 09: questão e resultados;
- 10 e 11: diagnóstico;
- 12: recomendações.

## 6. Achados

| N.º | Gravidade | Objeto | Achado | Bloqueia publicação? |
|---|---|---|---|---|
| 1 | **ALTA** | Pacote (texto de DA) e, por embutir, plataforma | A palavra de produção **"folha" aparece 23 vezes** no texto exibido à candidata. Ela está na lista proibida desta ordem. Também há metatexto de produção. Detalhe abaixo. | **Sim.** A correção é mecânica, na fábrica (GCB), registrada, sem tocar enunciado nem gabarito. Depois, remontar `pacote.json` e `pacote_estudante.json` (`montar_v1_13.py`) e a plataforma (`build_plataforma_v16.py`), e repetir A, B e D. A alternativa é o Fundador manter as remissões como MANTER registrado (contrato v1.2.8, ponto 4). |
| 2 | MÉDIA | `pacote_estudante.json` | Contrato v1.2.5 e v1.2.7 descumprido nos itens DA. Detalhe abaixo. | Não para a plataforma, que embute `pacote.json`. Bloqueia o aceite canônico do arquivo do estudante. |
| 3 | MÉDIA | Contrato | A v1.13 está sem errata do contrato, que segue na v1.2.9. Detalhe abaixo. | Não para a plataforma, que já lê os dois tipos e descarta tipo desconhecido. É pendência formal do gatilho A da v1.13 (errata v1.2.10, D1 da GBQ). |
| 4 | BAIXA | Pacote | Os ids de lote D1 a D5 coincidem com os ids das discursivas D1 a D5. Na plataforma, os espaços de nomes são separados (`P.lotes` × `P.discursivas`/`S.disc`) e não há efeito. Há risco de ambiguidade em relatórios, registros e importação de erros. | Não. |
| 5 | BAIXA | Pacote D6 / plataforma | Uma pegadinha de P1-DA-12 (art. 48) traz `**e**`. A lista final "Pegadinhas prováveis" da plataforma não interpreta negrito e mostra os asteriscos. | Não. Corrigir junto com o achado 1, retirando os `**` da pegadinha. |
| 6 | BAIXA | Pacote D4 (`topicos`) | O resumo de P1-DA-8.4 traz conteúdo que está no curso de 9.3, e não no de 8.4 ("respostas efetivas e úteis às necessidades ou às demandas de interesse público"), além das remissões "é tratado em 9.3/8.2". O FORMATO, seção 5, pede só o curso daquele id. | Não. |
| 7 | BAIXA | Pacote D4 (justificativas) | A troca registrada de R-códigos por nome da publicação deixou redação repetitiva em D4-62, D4-75 e D4-78 (ex.: "O artigo de Bresser-Pereira (ENAP, 2022) diz… e o artigo de Bresser-Pereira (ENAP, 2022) a chama…") e parênteses duplos em D4-38. Não há erro de conteúdo. | Não. |
| 8 | BAIXA | Pacote (texto de DA) | Há notas editoriais que não estão na lista proibida e não foram tratadas como achado de bloqueio. Exemplos: "o curso não afirma…" (D1, D3, D4), "[REVOGADO]" (D4), "No texto próprio do curso" (D4) e "Item C com elemento que parece trocado" (D2, D5). Revisar no estilo. | Não. |
| 9 | INFO | Plataforma | A meta `mapaspro:versao` já diz "publicada em 20/10/2026", antes do "sim" do Fundador. | Não. Ajustar a data na remontagem, se a publicação for em outro dia. |

Detalhe do achado 1 ("folha" e metatexto de produção):

| Onde | Ocorrências | Situação no registro de formato |
|---|---|---|
| D2.curso | 5 | MANTER registrado pelo produtor |
| D3.curso | 2 | MANTER registrado pelo produtor |
| D5.curso | 3 | MANTER registrado pelo produtor |
| D4.curso | 5 | sem registro de MANTER |
| D4.resumo | 1 | sem registro de MANTER |
| Justificativas D4-14, D4-27, D4-30, D4-49, D4-52 e D4-63 | 6 | sem registro de MANTER |
| Resumo do tópico P1-DA-8.2 | 1 | sem registro de MANTER |

Exemplos:
- "O caput 3 não é folha. Todo conteúdo cobrável está nas folhas 3.1 a 3.4." Está no `### Caput 3`, que abre o tópico 3.1.
- "Os detalhes do fiscal estão na folha 10.6."
- "Distribuição por folha: ver 8.x (IV, VIII, IX, XI)…"
- "…é ponto da folha 8.2." Essa frase está em justificativa e também fere a seção 7, que manda deixar fora as frases que só falam do processo.

Detalhe do achado 2 (`pacote_estudante.json` nos itens DA):
- `nome` = "Câmara 2026 — pacote F4 (v1.13)". Deveria ser o nome próprio com sufixo "-E", como na v1.12: "Câmara 2026 — pacote do estudante (v1.12-E)".
- Os 410 itens DA têm `url` não vazia ("saida/gcb/D…"). Deveria ser "" nos AUTORAL.
- Os 410 itens DA não têm o campo `nucleo`, que o contrato exige em todo item (v1.2.7, ponto 3). Os 749 itens da v1.12 têm.
- Causa: `montar_v1_13.py` acrescenta os mesmos objetos DA aos dois arquivos.

Detalhe do achado 3 (contrato sem errata):
- Os tipos de visual `compare` e `baseLegal` estão fora da lista fechada do ponto 1 da v1.2.9 ("e nenhum outro").
- Os lotes D1 a D6 e os seus arquivos-fonte não estão na tabela de fonte.
- O `rotulo` das pegadinhas de DA segue o FORMATO (texto do edital), e não a regra (d) da v1.2.

## 7. O que bloqueia a publicação
1. **Achado 1.** Retirar ou trocar "folha" e o metatexto de produção nas 23 ocorrências, ou obter do Fundador o MANTER registrado. Depois, remontar o pacote e a plataforma e repetir as conferências A, B (varredura e validador) e D (cursos DA), pelos scripts acima.
2. Publicar continua reservado ao Fundador (D-V15-PLATAFORMA). O arquivo a publicar é `plataforma_v16_publicar.html` remontado, que precisa continuar sendo exatamente o corpo do `_final`.

Os achados 2 e 3 não impedem a publicação da plataforma. Eles impedem o aceite canônico do `pacote_estudante.json` v1.13 e precisam de errata do contrato (v1.2.10) antes do gatilho A. Os achados 4 a 9 são ressalvas.

## 8. Reconferência pós-errata (20/10/2026)

Esta seção cobre o estado do repositório no commit e53e146, com a árvore limpa. Nesse commit já estão três mudanças feitas depois do QA acima:
- a errata de forma da gcb-cpp nos `D<n>_plataforma.json`, para os achados 1, 5, 6 e 7;
- o contrato v1.2.10 da gbq-gerencia, para os achados 2, 3 e 4;
- a remontagem do pacote e da plataforma pelo orquestrador.

A gbq-cqe não alterou nenhum objeto e não fez commit. As conferências usaram scripts próprios, rodados com `python3 -I`, em `/tmp/claude-0/-home-claude/9f60db71-6d00-590f-a17d-a2a9f6b75e58/scratchpad/qa2/`:
- `jdiff.py`: diff estrutural contra 684ae5c;
- `chkA2.py`: conferência A e edição do estudante;
- `chkB2.py`: conferências B e C, com a varredura ampliada;
- `artcurso.py`: baseLegal × curso;
- `chkContrato.py`: pontos 3 a 7 da v1.2.10;
- `chkBuild.py`: montagem e arquivo de publicação;
- `pw_v16b.py`: conferência D.

Os resultados brutos estão em `resA2.json`, `resB2.json` e `resD2.json`. Os 28 screenshots novos estão em `saida/plataforma/testes_v16_final/pos_errata_2026-10-20/`. Esse é o único acréscimo ao repositório além desta seção.

### 8.0 Vereditos finais

| Objeto | Veredito | Bloqueia a publicação? |
|---|---|---|
| Pacote v1.13 (`pacote.json` e `pacote_estudante.json`) | **ACEITO COM RESSALVAS** | **Não, pelo QA.** O achado 1 está resolvido. A ressalva nova (achado 10, um `**` num par do D6) não aparece na plataforma. |
| Plataforma v16 (`plataforma_v16_final.html` / `plataforma_v16_publicar.html`) | **ACEITO** | **Não, pelo QA.** Publicar continua reservado ao Fundador (D-V15-PLATAFORMA). Também depende do gatilho A da v1.13, cujas condições (b) a (d) estão fora deste QA (ver 8.9). |

### 8.1 Objetos conferidos (SHA-256 dos bytes em disco)

| Arquivo | Bytes | SHA-256 |
|---|---|---|
| saida/pacote/montagem_v1_13/out/pacote.json | 2.906.562 | 007787e3ed13b87bdcbbf384a40a41182b78e2f977fb4cc090bc4b84c931c192 |
| saida/pacote/montagem_v1_13/out/pacote_estudante.json | 2.644.826 | 8b5489b9828a9b3cde25fb27546cc155987b320cd63fd31381cad9cb0442b8dd |
| saida/pacote/montagem_v1_13/out/diag30_DA.json | 988 | eb1ced6df3d624ae62b82337db6a4cfe29b86baa9494e96aed1b3defe61a6800 (inalterado) |
| saida/plataforma/plataforma_v16_final.html | 2.821.862 | 19c44ac5cfd4745b418cae70b7ccd3a8262dbd59f9bd33c063a4c7c82e227bed |
| saida/plataforma/plataforma_v16_publicar.html | 2.821.316 | 4d19eb05f3da3b8eebd466ec62fb91b01791397a692e8dfd0c4ddff229a065fb |
| saida/plataforma/plataforma_v16_final_template.html | 128.081 | c6de3f2a699597e124540eb4a59f451938ba44da9fa9c86d2a6e4b9d5fc0b46c (inalterado) |
| saida/gcb/DA_plataforma/D1_plataforma.json | 128.443 | 5d953b134307f40e3f51485c5550d6eadbda3a96a64ea3dfb3a3ae845439fbe9 (inalterado) |
| saida/gcb/DA_plataforma/D2_plataforma.json | 413.272 | cba2e2769ba680ee028edf0f0a5e52a5bf55671c894f5c920edaf84f3cf139bf |
| saida/gcb/DA_plataforma/D3_plataforma.json | 236.815 | 917827abb6a2c5d01af386eaa0bf7678cbd0e02b8896e9cb9262216eb4c8f9c1 |
| saida/gcb/DA_plataforma/D4_plataforma.json | 251.380 | e44b66e785a8d4ce55449b2574153d7670a603cb8f457975248aede323c22806 |
| saida/gcb/DA_plataforma/D5_plataforma.json | 287.310 | 5ebec2854beb00ac0fb2581c028095d4dc306fec61118080cd37666c47e3a0c2 |
| saida/gcb/DA_plataforma/D6_plataforma.json | 184.195 | 8b8e5a42e3a8f5e9f500fa0fec8450f06e1932409ca6cae303a8b1ee0fa9754a |
| regras/pacote_contrato.md (v1.2.10) | 68.699 | 2626a946e9e295692244a50643113571fb380b3eca5bfb2fe5db06a0242928c1 |
| saida/pacote/montagem_v1_13/montar_v1_13.py | 7.056 | 723370f56fe830cace0d46056b681ce6c3e0b87f4497cbd1da84101ad6391ebe |
| saida/gcb/DA_plataforma/scripts/validar_da.py | 10.647 | eb944d324f3143ff26fb01a0f54507f5d3a9dcc43d22e6e3a7e9274686f445a4 |

### 8.2 Diff dos `D<n>_plataforma.json` contra 684ae5c

Resultado: **nenhum `id`, `enunciado`, `gabarito` ou `itemEdital` mudou.** Também não mudaram `comando`, `textoBase`, `volatil`, `url`, `numero`, `rotulo`, `aderencia`, a ordem dos itens, o `id` nem os `itensEdital` dos lotes, nem as chaves de `topicos`. O diff, feito campo a campo sobre o JSON, achou só os caminhos abaixo.

| Lote | Caminhos alterados | Registro "Errata de forma — QA final 20/10/2026" |
|---|---|---|
| D1 | nenhum (arquivo idêntico) | — |
| D2 | `lote.curso` | 4 entradas: 2 deleções de frase de processo e 2 trocas "folha" → "subitem". Conferem com o diff. |
| D3 | `lote.curso` | 2 entradas: 1 deleção e 1 troca. Conferem. |
| D4 | `lote.curso` e `lote.resumo`; justificativas de D4-14, 27, 30, 38, 49, 52, 62, 63, 75 e 78; resumos dos tópicos 8.2 e 8.4 | 19 entradas: 16 de curso, resumo e justificativas, mais 3 de tópicos. Conferem, inclusive a nota de formato do C9.4-03 (a lista de 3 itens virou parágrafo depois da deleção). |
| D5 | `lote.curso` | 3 trocas. Conferem. |
| D6 | `lote.pegadinhas[51].texto` (`**e**` → `e`) | 1 entrada. Confere. |

### 8.3 Conferência A (v1.12 intacta): OK

`chkA2.py` deu 0 FALHA nos dois arquivos. Os pontos conferidos:
- **v1.12 dentro da v1.13:** 749/749 itens idênticos byte a byte, na mesma posição, nos dois arquivos. Também são idênticos os lotes da v1.12 (10 no `pacote.json`, 7 no `pacote_estudante.json`), as 47 entradas de edital P1/P2, os 4 simulados, as 5 discursivas e os 40 tópicos, na mesma ordem relativa.
- **Topo do arquivo:** a ordem das chaves de topo e `versao` 1 não mudaram. A serialização continua indent=1 + LF.
- **Edital DA:** é igual a `edital_DA.json` e forma um bloco contíguo nas posições 20 a 65, entre `P1-8.4` e `P2-1`.
- **Itens e lotes DA:** os 410 itens e os 6 lotes DA são idênticos, byte a byte, aos `D<n>_plataforma.json` atuais. No estudante, os itens diferem só por `url` "" e `nucleo`, que calculei por conta própria.
- **Tópicos DA:** os 39 são iguais aos das fontes como objeto. Saem com as chaves `resumo`, `emUmMinuto`, `visuais`, nesta ordem (v1.2.10, ponto 7), e são idênticos byte a byte à fonte com as chaves reordenadas. Nenhum valor mudou.
- **`topicos`:** continua o último campo e segue a ordem do edital (79 no total).

### 8.4 Conferência B (Direito Administrativo): OK, com a ressalva do achado 10

**Edital e itens (parse próprio dos canônicos).** Não houve nenhuma diferença:
- 46 entradas de edital, todas literais;
- 410 itens (D1 60, D2 80, D3 71, D4 79, D5 70, D6 50);
- enunciado e gabarito iguais aos dos canônicos, com 0 diferença em cada lote;
- `itemEdital` igual à folha/subitem do canônico;
- `volatil` igual à marca do canônico em 410/410;
- ids únicos (1.159);
- campos fixos e `url` corretos.

A ordem de apresentação do canônico de D3 e D5 continua diferente da ordem dos ids, como na seção 3.2. Isso não é achado.

**Justificativas.** São 108 diferentes da junção das linhas 1 e 2 do canônico, contra 103 no QA. As 5 novas (D4-14, 27, 30, 49 e 52) e as alterações em D4-38, 62, 63, 75 e 78 são todas entradas do registro de formato do D4. Nenhuma diferença ficou sem registro.

**Validador `validar_da.py` (versão ampliada).** Rodou nos seis lotes, com o canônico e o Anexo N de cada um: **0 FALHA e 0 AVISO** nos seis. A contagem de quadros é a mesma da seção 3.3. O validador normaliza `**` antes de comparar e não procura `**` em pares, por isso o achado 10 não aparece nele.

**Varredura ampliada.** Foram lidos 3.282 campos de texto exibido de DA, agora tirados do próprio `pacote.json`. A lista é a da seção 3.4, com três mudanças:
- "folha" e "Folha" (singular e plural) entram na busca;
- o código R passou a `R\d{1,2}` e o código F a `F\d{1,2}`;
- "**" cru passou a ser procurado nos campos que não são markdown: pares, pegadinhas, enunciados, justificativas, "Em 1 minuto", visuais e edital. Nos campos markdown (curso e resumos), a busca é por `**` em número ímpar.

Resultado:
- **"folha": 0** (eram 23);
- **R/F: 0**;
- todas as outras marcas: 0;
- `**` em número ímpar nos campos markdown: 0;
- **`**` cru: 1 campo**, D6, par 0 ("restrição **temporária**"). É o achado 10.
- Ficam os falsos positivos já conhecidos: os 197 "Como a banca troca:" prescritos e "mecanismo:" como conteúdo (D4-46).

**baseLegal.** Os 105 dispositivos, em 29 visuais, passaram em quatro conferências, todas 105/105:
- `literal: true`;
- texto letra a letra no Anexo N;
- `conferido` igual à data de consulta do mapa;
- artigo citado no bloco `##` do curso do tópico (`artcurso.py`, que aceita "art. 2º", "arts. 2º e 3º" e intervalos).

**Resumos de tópico.** Os 39 têm de 150 a 250 palavras. Os dois alterados:
- 8.4: 198 palavras, sem número ausente do curso, sem conteúdo do 9.3 e sem remissão;
- 8.2: 242 palavras, sem número ausente do curso. Restou a remissão "é do subitem 8.4", que também está no curso de 8.2 e por isso é admitida.

**Contrato v1.2.10 (`chkContrato.py`).** Conferi os pontos 3 a 7 e só um item falhou:

| Ponto | O que foi conferido | Resultado |
|---|---|---|
| 3 | Campos dos itens DA na ordem dos demais; `cargo`, comando fixo e `textoBase` "" | OK |
| 4 | Lotes D1 a D6 com campos na ordem do ponto, `prova` "P1", nomes no padrão "Direito Administrativo — … (itens x e y do edital)", sem "Lote" | OK |
| 4 | Pares `{a, b, como}` com " Como a banca troca: " | OK |
| 4 | Pares e pegadinhas sem `**` | **FALHA, só no D6, par 0** (achado 10) |
| 5 | Rótulo das 405 pegadinhas igual ao texto do edital do `itemEdital`; nenhuma "Não confunda" | OK |
| 6 | `compare` e `baseLegal` com os campos na ordem do ponto | OK |
| 7 | 1 ou 2 visuais e 3 frases no "Em 1 minuto" | OK |

Tipos de visual: 29 baseLegal, 23 compare, 13 tabela, 9 esquema, 3 fluxo e 1 linha.

**Texto do contrato.** `regras/pacote_contrato.md` tem o SHA-256 declarado na D1 (2626a946…). A seção "Errata de forma da v1.2.10" está no arquivo literalmente igual à seção 3 da D1. O título passou a v1.2.10, e o arquivo não tem CR.

### 8.5 Conferência C (diagnóstico): OK

`diag30_DA.json` não mudou (SHA-256 igual). Todos os critérios da seção 4 foram repetidos sobre o pacote novo e deram OK:
- 30 ids distintos, todos existentes e todos de DA;
- nenhum volátil, todos de aderência "direta" e nenhum em simulado;
- pelo menos 1 por item do edital 1 a 12, todos em folha;
- C/E 15/15, e folhas declaradas iguais ao `itemEdital` dos itens.

No template final, `DIAG30.DA` é igual a `diag30_DA.json`, e as listas P1 e P2 são iguais às da v15.4.

### 8.6 Conferência D (plataforma, Playwright/Chromium, 390×844 e 1280×900, claro e escuro): OK

**Montagem e arquivo de publicação.**
- `plataforma_v16_final.html` é **byte a byte** igual ao template final com o `pacote.json` v1.13 atual embutido, pela regra própria (JSON compacto e `</` escapado). O pacote embutido, decodificado, é igual ao `pacote.json`.
- `plataforma_v16_publicar.html` é **exatamente o corpo** do final: sem a primeira linha, que é idêntica à da v15.4 publicada, e sem o `\n</body></html>` final.
- O template final não mudou e difere do `plataforma_v16_template.html` só na meta `mapaspro:versao` e em `DIAG30`.

**TI e Fala × v15.4: iguais.**
- TI: 17 tópicos com curso e 185 itens. Fala: 23 tópicos com curso e 564 itens.
- Itens por tópico e numeração são iguais.
- A amostra de 5+5 tópicos tem os mesmos hashes de render (ex.: P1-1 5509003f4e5c).
- Os 40 cursos, os 40 resumos de tópico e as telas da matéria TI, da matéria Fala e de Erros são idênticos.
- Prática, Painel e Disciplinas diferem só pelos acréscimos de DA, os mesmos da seção 5.2.

**Direito Administrativo.**
- **Estrutura:** 39 tópicos com curso, 410 itens, numeração de 1 a 12 sem "DA-", 9 grupos na matéria e o botão de diagnóstico presente.
- **Os 39 tópicos foram abertos nos 4 cenários** (156 aberturas), com **0 erros e 0 avisos de console** em todo o teste. Em 39/39, nos quatro cenários:
  - os quadros DEFINIÇÃO, BASE LEGAL, EXEMPLO e PEGADINHA saem em número igual ao do bloco `##`;
  - o "Em 1 minuto" tem 3 itens;
  - os baseLegal têm o número de dispositivos do JSON;
  - não há figura vazia, `###` em maiúsculas, rótulo solto nem "DA-".
- **Markdown cru:** o detector não achou nada em nenhum tópico. O `**e**` do tópico 12 (achado 5) sumiu.
- **Visuais:** saem no tipo e na ordem do JSON em 37/39. Os outros dois, 4.2 e 7, são o mesmo falso positivo da seção 5.3 (tabela com a primeira coluna "Aspecto").
- **Prática em blocos de 10 questões:** foram feitos blocos em 3.4, 7 e 10.1 (390 claro) e em 9.4 (1280 escuro). Em todos:
  - 10 itens distintos, todos do tópico;
  - 7 acertos e 3 erros, com nota 4, igual à esperada;
  - 10 correções, com o rótulo "tópico N".
- **Diagnóstico DA (390 claro e 1280 escuro):**
  - abre o `D30-DA`, com 30 itens na ordem de `diag30_DA.json`;
  - 19 acertos, 10 erros e 1 em branco, igual ao esperado, com nota 9;
  - 30 correções e 30 tópicos no resultado.
- **Rolagem horizontal:** nenhuma, nas 17 telas conferidas a 390 px (dois temas) e a 1280 px. As telas são as da seção 5.3: matéria, os 39 cursos, resumo, resumo do 10.6, painel, questão, resultado, diagnóstico, erros e recomendações.

**Tempo de carga.** Medido de `goto` até o app pronto:

| Arquivo | 390 px | 1280 px |
|---|---|---|
| v16 final | 259 / 263 / 285 ms | 256 / 229 / 236 ms |
| v15.4 | 189 / 171 / 169 ms | 168 / 172 / 177 ms |

### 8.7 Situação dos achados 1 a 9 e achado novo

| N.º | Situação | Evidência |
|---|---|---|
| 1 | **RESOLVIDO** | A varredura dá 0 "folha" e 0 R/F, contra 23. As frases de processo foram deletadas e as remissões úteis viraram "subitem", tudo registrado (8.2). O validador ampliado também dá 0. Pacote e plataforma foram remontados. |
| 2 | **RESOLVIDO** | `nome` "Câmara 2026 — pacote do estudante (v1.13-E)". Os itens DA têm `url` "" e `nucleo` como último campo, 366 true e 44 false, igual ao meu cálculo. Detalhe em 8.8. |
| 3 | **RESOLVIDO** | Contrato v1.2.10 (SHA-256 2626a946…): `compare` e `baseLegal` na lista fechada (ponto 6), tabela de fonte dos lotes D1 a D6 (ponto 2) e rótulo das pegadinhas pela regra (d) (ponto 5). |
| 4 | **REGISTRADO** (mantido) | Ponto 9 da v1.2.10: os ids são únicos por lista, as 5 colisões ficam fechadas e o id vai qualificado fora da plataforma. Conferi que as colisões continuam só D1 a D5 e que a plataforma não é afetada. |
| 5 | **RESOLVIDO** na pegadinha | A pegadinha 52 do D6 ficou sem `**`, e não há markdown cru no tópico 12. Ver o achado 10 para o par que restou. |
| 6 | **RESOLVIDO** | O resumo do 8.4 tem 198 palavras, só do curso de 8.4, sem remissão. |
| 7 | **RESOLVIDO** | Em D4-62, D4-75 e D4-78, a segunda menção virou "o mesmo guia" e "o mesmo artigo". Em D4-38, o parêntese duplo virou aposto. |
| 8 | Ressalva mantida (BAIXA) | Notas editoriais como "o curso não afirma…" e "O documento da CGU é documento interno do órgão…" (resumo do 8.4) continuam. Não estavam no escopo da errata. |
| 9 | Ressalva mantida (INFO) | A meta `mapaspro:versao` diz "publicada em 20/10/2026". Ajustar só se a publicação for em outro dia. |
| **10 (novo)** | **BAIXA** | Detalhe abaixo. |

Detalhe do achado 10:
- **Onde:** `lotes[D6].pares[0].como` ("Sigilosa: restrição **temporária** por imprescindibilidade…").
- **Regra:** o ponto 4 da v1.2.10 diz que "os textos de `pares` e de `pegadinhas` não levam marcas de markdown (`**`)". A própria D1, seção 2.3, já tinha listado este par junto com a pegadinha, mas a errata da GCB corrigiu só a pegadinha.
- **Efeito:** a plataforma v16 não lê `lote.pares`, porque o template não tem nenhuma referência a pares. A candidata não vê o problema, e por isso ele não bloqueia a publicação.
- **Pendência:** é uma não conformidade do pacote ao contrato. Deve ser corrigida na fonte (gcb-cpp, D6, com registro de formato e remontagem) ou registrada como exceção, antes do aceite canônico do pacote ou na próxima errata, o que vier antes. Também precisa ser corrigida antes de gerar a edição .md, que exibiria os pares.

### 8.8 Edição do estudante × v1.2.10, ponto 8: CUMPRE

| Exigência | Resultado |
|---|---|
| `nome` | "Câmara 2026 — pacote do estudante (v1.13-E)" |
| `versao` e `geradoEm` | 1 e 2026-10-20, iguais aos do `pacote.json` |
| Edital, lotes DA e `topicos` | Idênticos aos do `pacote.json` |
| Itens DA | Texto e campos iguais aos do `pacote.json`, na mesma ordem de campos, salvo `url` "" e `nucleo` (bool) como último campo |
| `nucleo` DA | 366 true e 44 false. Os false estão em P1-DA-1.1 (1), 1.2 (1), 2.1 (12), 11 (20) e 12 (10). É igual ao cálculo próprio (posição ≤ 10 na folha, na ordem do `pacote.json`) e igual ao da D1. |
| Condições (i) a (iii) | Verificadas: cada `itemEdital` DA tem itens de um só lote; todos os itens são "direta"; nenhum item fora de D1 a D6 está em P1-DA. |
| Itens DA em ordem numérica de id em cada lote | Verificado |
| Itens da v1.12 | Com `nucleo`, inalterados |
| `pacote.json` | Sem `nucleo`, com `url` do canônico nos itens DA |

### 8.9 O que bloqueia a publicação

**Pelo QA, nada.** O achado 1, que era o único bloqueante, está resolvido. Os achados 2 e 3 estão resolvidos e o 4 está registrado. O achado 10 e os achados 8 e 9 são ressalvas que a candidata não vê na plataforma.

O arquivo a publicar é `plataforma_v16_publicar.html` (SHA-256 4d19eb05…), que é exatamente o corpo de `plataforma_v16_final.html` (19c44ac5…).

Fora do QA, publicar continua dependendo de dois pontos:
- **o "sim" do Fundador** (D-V15-PLATAFORMA);
- **o gatilho A da v1.13** (v1.2.10, ponto 11). A condição (a) está cumprida por esta reconferência. As outras três estão em aberto:
  - (b) o aceite canônico de D2 a D5 em DECISOES.md: não há linha de aceite desses lotes em DECISOES.md em 20/10/2026, só D-LOTED1-CANONICO e D-LOTED6-CANONICO;
  - (c) o adendo 5 do registro GBQ;
  - (d) a conferência de contagens da gbq-csc.
