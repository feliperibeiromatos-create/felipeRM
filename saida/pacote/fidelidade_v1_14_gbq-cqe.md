# fidelidade_v1_14_gbq-cqe.md — T-123 (fidelidade independente do pacote v1.14) — 2026-10-23 — gerado por gbq-cqe

Objeto: `saida/pacote/montagem_v1_14/out/` (commit 793225e, branch main). Base: D1 `saida/pacote/T123_D1_v1_14_2026-10-23.md`; relatório `saida/pacote/T123_FINAL_v1_14_2026-10-23.md`; contrato `regras/pacote_contrato.md` v1.2.12; aceites D-T116-LEVA1-ACEITE a LEVA8 (DECISOES.md, linhas 175 a 179, 181, 182, 184) e D-D3R75-AJL7E1-ACEITE (185); limpeza `saida/gcb/T123_limpeza_reconciliacao_GCB_2026-10-23.md` com `saida/gcb/DA_plataforma/DA_reforco_substituicoes.csv`.
Método: leitura e scripts próprios (`python -I`, só leitura do repositório, scratchpad da sessão `…/scratchpad/cqe/fid1.py` a `fid4.py`). Nenhum script da montagem foi usado para concluir. Os insumos de texto foram lidos com CRLF→LF (árvore com `core.autocrlf=true`). Não alterei nenhum arquivo do repositório, salvo este. Sem commit.

## Veredito: **ACEITO**

Nenhuma FALHA nos 7 pontos pedidos. Há 3 observações de registro (seção 8), e nenhuma muda dado, texto nem contagem.

## 1. v1.13 canônica contida sem alteração

| Critério | Resultado |
|---|---|
| Base v1.13: `montagem_v1_13/out/pacote.json` 82c4117c…, `pacote_estudante.json` 04cbd593…; iguais em LF aos canônicos promovidos `saida/pacote/pacote.json` e `pacote_estudante.json` | OK |
| Os 1.159 itens da v1.13 estão no `pacote.json` v1.14 iguais como objeto e com a mesma ordem de campos | OK (0 divergência) |
| Ordem relativa dos 1.159 preservada | OK |
| `edital`, `simulados`, `lotes`, `discursivas`, `topicos` iguais à v1.13 (pacote e estudante); chaves de topo na ordem da v1.13 | OK |
| Cabeçalho: `nome` "Câmara 2026 — pacote F4 (v1.14)" e "… do estudante (v1.14-E)"; `geradoEm` 2026-10-23 (> 2026-10-20) igual nos dois; `versao` 1 | OK |
| Estudante: os 1.159 itens da v1.13-E iguais, salvo `nucleo` | OK |
| `nucleo` que muda (admitido pela D1, seção 6): exatamente 12 itens, true→false: D1-07, D1-08, D3-79, D3-80, D6-07 a D6-10, D6-37 a D6-40 | OK |
| `montagem_v1_13/`, `saida/estudante/`, `saida/pacote/pacote*.json`, `saida/plataforma/`, `D<n>_plataforma.json` e as 8 levas sem modificação nem deleção no git desde a v1.13 canônica (3279398) e desde a leva 8 (4198906); `saida/plataforma/` só recebeu arquivos novos (v17, T-125) | OK |

## 2. Os 238 itens de reforço

Releitura própria das 8 levas: seção 1 (`**<id>.** <enunciado>`) e blocos da seção 2 (itemEdital, Aderência, Gabarito, Justificativa linhas 1 e 2, Marcas, cabeçalho [TS]).

| Critério | Resultado |
|---|---|
| SHA-256 LF de cada leva contido na linha de aceite (175, 176, 177, 178, 179, 181, 182; leva 7 também na 185; 184) | OK 8/8 |
| Ids da seção 1 = ids da seção 2, na mesma ordem, em cada leva | OK 8/8 |
| 238 ids únicos; D1-R03 e D4-R12 ausentes da leitura e do pacote | OK |
| Erratas: o "antes" ocorre 1 vez na seção indicada e 1 vez no arquivo, o "depois" 0 vez (AJ-E1, D3-R13; AJ-L2-E1, D3-R18; AJ-L7-E1, D3-R75) | OK 3/3 |
| Linha 2 do D3-R75 igual, por igualdade, ao texto da D1, seção 2.2 | OK |
| D4-R42 e D4-R52: enunciado igual ao da seção 1 da leva 8, sem as erratas AJ-L8-E3/E4, que não têm aceite | OK |
| CSV da GCB: SHA-256 LF df9f53bd…b501; registro de formato a511fd8d…820e; 91 linhas, campo sempre `justificativa`; 85 ids alterados | OK |
| Cada `antes` ocorre 1 vez na justificativa bruta (j1 + " " + j2, depois das erratas) e 1 vez na aplicação sequencial | OK 91/91 |
| Operações: 6 = 29, 3 = 39, processo = 23. Nas 62 de operação 3 e processo, o `depois` é subsequência do `antes` (só deleção) | OK |
| Operação 6: o autor e o ano do `depois` constam do campo "Base" do próprio item na leva (29/29). Os 3 "alargados" (D4-R15, R20, R24) só reaproveitam palavras do `antes`; "a mesma publicação" (D4-R19, D4-R27) remete à publicação nomeada antes, na mesma justificativa | OK |
| Campo a campo, nos 238: `id`, `rotulo` AUTORAL, `certame`, `cargo`, `ano` 2026, `numero` = nn, `comando` "Julgue o item a seguir.", `textoBase` "", `enunciado` (com erratas), `gabarito`, `justificativa` (j1 + " " + j2, erratas e as 91 edições aplicadas literalmente), `itemEdital`, `aderencia`, `url` = arquivo da leva; ordem de campos = a dos itens DA da v1.13; sem `volatil` | OK 238/238 |
| Estudante: o mesmo objeto, com `url` "" e `nucleo` booleano como último campo | OK 238/238 |
| `out/reforco_bruto.json` igual à minha releitura (enunciado e justificativa bruta) | OK |
| Ordem: os 238 são os últimos de `itens`, na ordem das levas e da seção 1; D3-R75 logo depois do D3-R74 | OK |
| Por leva (n; C/E; [TS]; parciais): 30;15/15;16;8 · 30;17/13;13;2 · 30;16/14;14;11 · 28;15/13;13;5 · 30;16/14;14;0 · 30;14/16;15;0 · 30;15/15;13;8 · 30;14/16;16;1 | OK, igual à D1, seção 2.1 |
| "Marcas: … VOLÁTIL=não" em 238/238 | OK |

Amostra textual: não houve amostra. A igualdade foi conferida nos 238/238, contra a fonte e contra a tabela da GCB.

## 3. Os 36 itens de banco P1-DA

| Critério | Resultado |
|---|---|
| `banco/banco.csv` LF b1c1588f…721f; 40 linhas P1-DA (BQ-0113 a BQ-0152) | OK |
| Entram 36: BQ-0113 a 0130, 0132, 0134 a 0140, 0142 a 0150 e 0152. Os 13 campos são iguais à coluna de origem (rotulo, certame, cargo, ano_aplicacao int, numero_item int, texto_comando literal, texto_base, texto_integral, gabarito, justificativa "", item_edital_camara, aderencia, url_caderno) e não há campo a mais (`nota`, `volatil` ou `interno`) | OK 36/36 |
| Estudante: o mesmo objeto com `nucleo`; URL oficial mantida | OK 36/36 |
| Fora: BQ-0131 e BQ-0133 (anulado = "sim"); BQ-0141 ("QA PENDENTE" em `observacoes`, a única linha do banco com essa marca); BQ-0151 ("DIVERGE do texto vigente do Decreto 9.203/2017") | OK |
| C/E 26/10; CEBRASPE_ANALOGA e "direta" em 36/36; por entrada: DA-1 4, 2 3, 3 5, 4 4, 5 3, 6 1, 7 2, 8 1, 9 1, 10 4, 11 4, 12 4 | OK (= D1, 2.3) |
| Bloco do banco: os 142 primeiros de `itens` (106 + 36), em ordem de id. Ordem global = banco, os 1.053 não-banco da v1.13, os 238 | OK |
| Mapeamento dos 106 de banco da v1.13: os 13 campos iguais às colunas em 106/106. Dez têm campo opcional a mais, já na v1.13 (`volatil`: BQ-0015, 0017, 0035, 0064, 0075, 0076, 0086, 0089; `nota`: BQ-0040; `nota` e `interno`: BQ-0003) | OK |

## 4. Detector próprio das 10 categorias da ORDEM C (C01 a C10)

Regras próprias, mais largas que a C-MARCAS da D1:
- C01 "lote(s)";
- C02 códigos de item (L/4C/5C/A5/6A/6B, `BQ-nnnn`, `D<n>-R?nn`), "Difere de", "espelho da troca", "gêmeo";
- C03 "par Cn", "(Cn)", "(En)", "Pn", "alerta", "Bn", "A8.1-nn", "Kn";
- C04 qualquer `[…]`;
- C05 `R/F/G/H/N/U + número`, GG/TB, "Anexo";
- C06 TC/IC/GI/AT, "sem armadilha", "Mecanismo:";
- C07 QA/CQFP/CQE/CPP/GCE/GCB/GBQ/CSC, nomes de agente, "conferido por script", "parecer", "R1/R2";
- C08 errata, produção, produtor(a), fábrica, moldura, cota, ficha, "leva n", rodada, folha, núcleo, `D-XXX`, `T-nnn`, AUTORAL, CEBRASPE_, "TS=", deduplica;
- C09 vN, "versão N";
- C10 "Só o fato e a fonte", "sem item", "não gabarito", controverso, "não cobr…", PENDENTE, reverificar, VOLÁTI, "sem fonte", "não afirmar", URL, `**`.

Alcance:
- (a) `comando`, `textoBase`, `enunciado` e `justificativa` dos 274 itens novos, no `pacote_estudante.json`; o texto é idêntico no `pacote.json` (conferido);
- (b) as linhas novas dos 12 arquivos .md que mudam (diff contra a v1.13-E), com máscara só dos títulos de item.

| Medida | Resultado |
|---|---|
| Sensibilidade (controle): sobre a justificativa bruta, sem a limpeza, o detector acusa 90 ids (C03 37, C05 41, C08 25, C07 9, C02 7); cobre os 85 limpos | detector funcional |
| (a) Texto dos 274 depois da limpeza: 22 casamentos, todos conteúdo (FP): "parecer" obrigatório/jurídico (D1-R01, R05, R06, R07, R12; 15); "núcleo de governo" (D4-R18; 3); "produção" no sentido do conteúdo (D4-R24; 1); "produtor" na letra da lei (BQ-0113; 1); "desconto em folha (de pagamento)" (D3-R75; 2) | **0 marca**; 22 FP de conteúdo; 0 MANTER necessário |
| "Presidência da República" no D2-R21 e no D2-R24 (lista X da GBQ) | Conteúdo (remissão à Lei 9.007). Meu detector não o acusa. Confirmo a classificação |
| (b) Linhas novas da .md: além dos mesmos FP de conteúdo, só casamentos de forma: títulos `**<id>** —` e `### <id> — Gabarito`, linha "Item do edital: P1-DA-…", "URL oficial: https://cdn.cebraspe.org.br/…" dos 36 de banco, listas de ids em NUCLEO.md, "v1.14-E" e "lote D<n>" no README.md. A forma é a mesma dos itens da v1.13-E (conferida no D1-01 × D1-R01) | **0 marca** no texto de item |
| `**` dentro do texto de enunciado ou justificativa na seção "## Itens de reforço" dos 8 arquivos DA_D1 a D4 | 0 |

## 5. Contagens (recontagem própria)

| Medida | Esperado | Obtido |
|---|---|---|
| Itens; C/E | 1.433; 730/703 | 1.433; 730/703 |
| DA (itemEdital P1-DA); C/E | 684; 350/334 | 684; 350/334 |
| Reforço; C/E | 238; 122/116 | 238; 122/116 |
| Lote pelo prefixo do id | D1 72, D2 160, D3 160, D4 136, D5 70, D6 50 | igual |
| Parciais de DA | 35 (lista da D1, seção 2.1) | 35, a mesma lista (todos de reforço) |
| VOLÁTEIS de DA | 5 (D2-01, D2-28, D6-09, D6-32 e D6-34) | 5; o conjunto total de `volatil` é igual ao da v1.13 |
| `nucleo` true | 775 (367 fora de DA + 408 de DA); DA 408/276 | 775; 367 + 408; 408/276 |
| `nucleo` do reforço | 18 ids da D1, seção 6 | os mesmos 18 |
| `nucleo` do banco P1-DA | 36/36 | 36/36 |
| `nucleo` fora de DA | igual à v1.13 por id | igual |
| Itens novos em `simulados` | 0 | 0 |

Recontagem própria do `nucleo` de DA:
- critério inteiro do ponto 3 da v1.2.7: k1 data, k2 linha do ato, k3 direta antes de parcial, k4 posição; 10 primeiros por `itemEdital`;
- tabela da D1, seção 6; banco pela `data_verificacao` do banco.csv;
- linhas 93, 117, 162 a 165, 175 a 179, 181, 182, 184 e 185 de DECISOES.md conferidas pelo nome do ato.

Resultado: 684/684 iguais ao `pacote_estudante.json`.

## 6. Coerência: pacote_estudante.json, edição .md, adendo 6, contrato

| Critério | Resultado |
|---|---|
| Estudante = pacote, salvo `url` "" nos AUTORAL e `nucleo` como último campo (nos 1.433) | OK |
| .md: 53 arquivos; 41 iguais byte a byte à v1.13-E de `montagem_v1_13/out/estudante/`, que é igual em LF a `saida/estudante/` (v1.13-E promovida); mudam exatamente os 12 da D1, seção 10 | OK |
| Cada um dos 274 ids novos tem 1 título no `_itens` certo e 1 no `_gabarito` certo, e 2 no total da edição (fora NUCLEO.md). Enunciado, comando (banco), "Gabarito: X" e justificativa iguais ao estudante. Os de reforço ficam depois de "## Itens de reforço" | OK 274/274 |
| Ordem dos ids nos arquivos `_itens` de DA e de BANCO = ordem do pacote | OK |
| NUCLEO.md: por `itemEdital`, "k de n" e ids iguais ao `nucleo` do estudante (todas as entradas); soma 775 | OK |
| README.md: v1.14-E, 2026-10-23, "684 itens, sendo 36 de provas anteriores" | OK |
| Digest R2-D da .md (minha reconstrução) f9c1c065…916b = FINAL | OK |
| Adendo 6: SHA-256 LF das 8 levas; os 35 parciais; os 18 do núcleo; vagos D1-R03 e D4-R12; AJ-E1, AJ-L2-E1, AJ-L7-E1 e AJ-L8-E3/E4 (sem aceite); sem enunciado; 0 "D<n>" isolado | OK |
| Registro de alterações: 238 entrada_reforco, 36 entrada_banco, 3 errata, 91 formato, 12 nucleo_estudante (os 12 ids da seção 1) | OK (380 linhas) |
| Contrato: v1.2.11 do git (3279398) LF 85b30fcc…616b. Atual LF 3916ad99…8df, igual ao blob em HEAD. Reconstruí a v1.2.12 a partir da v1.2.11 e da D1, seção 7 (C-1 título; C-2 frase ao fim da linha 3; C-3 linha em branco e bloco de 13 linhas depois da âncora única "5. **Aplicação.** A partir da edição .md v1.13-E"), e o resultado é igual ao arquivo linha a linha. Nenhuma outra linha difere | OK |

## 7. Clone limpo descartável

| Clone (`git clone --no-local` de 793225e, no scratchpad) | Resultado |
|---|---|
| autocrlf do sistema (`true`, `C:/Program Files/Git/etc/gitconfig`) | Os 83 arquivos da pasta (fora o próprio manifesto) têm bytes e SHA-256 iguais ao MANIFESTO_v1_14.md, seção 4. `out/` é igual byte a byte à árvore de trabalho. MANIFESTO igual. 0 CR em `out/` e nos scripts |
| `--config core.autocrlf=false` (persistido no clone; também `-c core.autocrlf=false` transitório) | Idem: 83/83 iguais ao MANIFESTO; 0 CR |
| SHA-256 nos dois clones | `pacote.json` 070bc237…d495; `pacote_estudante.json` 6b56a7f8…b9ab; `registro_adendo6.md` 74855f03…970b. Os mesmos do FINAL e do MANIFESTO |
| Pasta real × MANIFESTO (árvore de trabalho) | 83 = 83, 0 divergência |

## 8. Achados (numerados)

1. **Sem divergência de dado.** Os pontos (1) a (7) dão 0 FALHA na conferência própria. As únicas mudanças em objetos da v1.13 são as admitidas pela D1 e pelo ponto 9 da v1.2.12: `nome`, `geradoEm`, posição dos itens depois do bloco do banco e 12 `nucleo` no estudante.
2. **Observação de registro (sem efeito em dado).** O `contrato_v1_2_12_2026-10-23.md` informa "325 → 339" linhas (contagem de `\n`) na tabela e "340 − 326 = 14" (contagem de linhas por split) no texto. As duas contagens estão certas, mas sob convenções diferentes. O difflib alinha a linha em branco inserida depois do bloco (insert 320–334), e não antes dele. O resultado é idêntico ao texto mandado pela D1, conferido por reconstrução.
3. **Observação (FP de conteúdo, sem MANTER).** O texto que a candidata lê tem 22 casamentos de palavras homônimas das categorias C07 e C08 ("parecer", "núcleo de governo", "produção", "produtor", "desconto em folha"). Todos são conteúdo jurídico ou administrativo. Nenhum pede MANTER do Fundador. A lista X ("Presidência da República", D2-R21 e D2-R24) é conteúdo.
4. **Observação de rito.** Duas trocas de operação 6 usam "a mesma publicação" (D4-R19, D4-R27). Cada uma remete à publicação nomeada antes, na mesma justificativa, e as duas foram conferidas no R2 da gcb-cqfp. Não há palavra nova fora disso: os 3 "alargados" (D4-R15, R20, R24) só reaproveitam palavras do `antes`.

Condição (d) do gatilho A da D1, seção 13: **fidelidade da gbq-cqe ACEITA**.
