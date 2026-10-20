# fidelidade_v1_13_T118_gbq-cqe.md — T-118 (D1 da GBQ, passo 4.5) — 2026-10-20 — gerado por gbq-cqe

Fidelidade independente do fechamento do gatilho A do pacote v1.13 (ciclo s15c1). Base: `saida/pacote/T118_D1_v1_13_2026-10-20.md` (seções 4 e 5), contrato v1.2.10 (`regras/pacote_contrato.md`, SHA-256 2626a946…28c1, inalterado) e meu QA final (`QA_final_v1_13_v16_2026-10-20_gbq-cqe.md`, seções 8.3, 8.4 e 8.7). A gbq-cqe não produziu nem reconciliou nenhum objeto. Não alterei nenhum arquivo de produção e não fiz commit. Este relatório é o único arquivo que gravei no repositório.

Método: scripts próprios, rodados com `python3 -I` e só leitura do repositório, fora dele, em `/tmp/claude-0/-home-claude/72c49c1c-aa49-56a0-8236-2c7fd5868295/scratchpad/cqe_t118/`:
- `lib.py`: utilitários e diff JSON próprio, que também compara a ordem das chaves;
- `c1_fonte_remontagem.py`: fonte D6, remontagem, conferência A, plataforma por leitura e integridade;
- `c2_contagens_B.py`: conferência B, parse próprio dos canônicos, varredura, recontagem do passo 4.3.2, `nucleo_k1k4` e banco;
- `c3_adendo.py`: adendo 5;
- `c4_md.py`: edição .md;
- `c5_cobertura_manifesto.py`: cobertura e manifesto.

Os resultados brutos estão em `res_c1.json` a `res_c5.json`, `canon_parse.json` e `varredura_hits.json`. Rodei dois scripts de terceiros, como a D1 pede:
- `validar_da.py`, nos seis lotes;
- `montar_v1_13.py`, sem mudança, numa cópia mínima em `copia/` no scratchpad, nunca no repositório.

## 0. Veredito: APROVADO COM RESSALVAS

| Objeto | Veredito | Bloqueia o aceite canônico? |
|---|---|---|
| Errata do achado 10 (`D6_plataforma.json`, `D6_registro_formato.md`) | APROVADO | Não |
| `pacote.json` (82c4117c…f240) e `pacote_estudante.json` (04cbd593…0c40) | APROVADO | Não. Podem ser promovidos byte a byte. |
| `stats_v1_13_DA.json`, `conferencia_t118.json`, `cobertura_v1_13.md` | APROVADO | Não |
| Adendo 5 do registro GBQ | APROVADO COM RESSALVAS | **Sim, pelo achado 2.** É a condição (c) do gatilho A. A correção é mecânica, no `registro_adendo_v113.py`, e exige regerar as duas cópias. |
| Edição .md do estudante v1.13 (53 arquivos) | APROVADO COM RESSALVAS | **Sim, pelo achado 1**, só para promover `out/estudante/` a `saida/estudante/`. Basta uma errata v1.2.11 do contrato ou a regeração. Não é condição do gatilho A (ponto 11). |
| `MANIFESTO_v1_13.md` | APROVADO | Não (achado 6, INFO) |

O conteúdo está fiel em todos os objetos:
- 410 itens com id, enunciado e gabarito iguais aos canônicos aceitos;
- a v1.12 intacta;
- 0 marcas de produção;
- o `nucleo` igual ao recálculo k1–k4;
- a única diferença para a montagem anterior é o campo do achado 10.

As ressalvas que bloqueiam são de forma documental: um registro com faixa de ids errada e uma edição .md que diverge do texto do contrato vigente.

## 1. Objetos (SHA-256 dos bytes em disco)

| Arquivo | Bytes | SHA-256 |
|---|---|---|
| saida/gcb/DA_plataforma/D6_plataforma.json | 184.191 | f8691dd5a3fd968922bf8bac8e26b4dd4f1475183afc9d6a0e84418d08b17122 (HEAD: 8b8e5a42…754a, 184.195) |
| saida/gcb/DA_plataforma/D6_registro_formato.md | — | 7998cc7be19676125ba13bdcc7f52537012488371ec8e1f9e01aa916b09890ca (HEAD: 4448eec4…ec27) |
| saida/pacote/montagem_v1_13/out/pacote.json | 2.906.558 | 82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240 (HEAD: 007787e3…c192) |
| saida/pacote/montagem_v1_13/out/pacote_estudante.json | 2.644.822 | 04cbd593fdd30404ecb7f91f6b6722da6b2fc24e58d3c0eb68b10a4e792a0c40 (HEAD: 8b5489b9…b8dd) |
| saida/pacote/montagem_v1_13/out/stats_v1_13_DA.json | 2.145 | f077cb33900b3f765b8c3259c1768b0dc3699ff2872fdfe24cf028b997dc7320 (HEAD: f48878ba…) |
| saida/pacote/montagem_v1_13/out/conferencia_t118.json | 2.100.552 | 6c5250c90f99af57cb28c907789923403c2e8a6b404dc65369608f9e2b99844f |
| saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo5_2026-10-20.md (= out/registro_adendo5.md) | 10.245 | 7224db40670608bff726f67b6b4769a509b225953146b80013b05d9c57f55918 |
| saida/pacote/montagem_v1_13/MANIFESTO_v1_13.md | 16.970 | (68 linhas, todas iguais ao disco) |
| saida/pacote/cobertura_v1_13.md | — | conferido por conteúdo (seção 6) |
| saida/plataforma/plataforma_v16_publicar.html | 2.821.316 | 4d19eb05f3da3b8eebd466ec62fb91b01791397a692e8dfd0c4ddff229a065fb (= HEAD = D-PLATAFORMA-V16-PUBLICACAO) |
| saida/plataforma/plataforma_v16_final_template.html | 128.081 | c6de3f2a699597e124540eb4a59f451938ba44da9fa9c86d2a6e4b9d5fc0b46c (inalterado) |

## 2. Fonte D6: errata do achado 10 (D1, 5.1). OK

| # | Conferência | Resultado |
|---|---|---|
| F3 | Diff JSON recursivo, D6 disco × HEAD | Só `/lote/pares/0/como`. Nenhuma chave nova, removida ou reordenada. |
| F4 | Natureza da mudança | `**` passou de 4 caracteres para 0, e `antigo.replace('**','') == novo`. |
| F5 | `lote.resumo` | Idêntico ao HEAD, com o negrito `**temporária**` mantido. |
| F6 | Edição por texto | O old_str da D1 ocorre 1 vez no HEAD. O HEAD com a troca é igual ao disco byte a byte. O arquivo é igual a `json.dumps(indent=1)+"\n"`. |
| F7 | `**` em `pares` e `pegadinhas` dos seis lotes, de D1 a D6 | 0 em todos |
| F8 | D1–D5 `_plataforma.json`, `edital_DA.json`, registros D1–D5 e `validar_da.py` | Iguais ao HEAD |
| F9 | Registro de formato | O blob HEAD é prefixo do arquivo, e a seção nova está só no fim. Ela traz: título; origem (QA 8.7, achado 10; v1.2.10, ponto 4); item `[par 0 (L-P1), campo como] deleção de marca (negrito)`; antes ⊂ `como` do HEAD e depois ⊂ `como` do disco; motivo; a frase "Só forma: … (campo markdown)" literal; "Total: 1 mudança no D6 (`pares`)"; e bytes, SHA-256 e caminho iguais aos obtidos. |
| F10–F11 | `validar_da.py` | "RESULTADO: 0 FALHA, 0 AVISO" nos seis lotes |

O parecer da gcb-cqfp (CONFERIDO) bate com tudo isso.

## 3. Remontagem, conferência A e plataforma (D1, 5.2)

**Remontagem.**
- A reconstrução própria a partir de `gerador_v1_12/out` (34765253…/23224c96…), `edital_DA.json` e D1–D6 (bloco do edital antes do primeiro P2, `url` "" e `nucleo` no estudante, tópicos com as chaves em ordem) deu **byte a byte** 82c4117c… (2.906.558 bytes) e 04cbd593… (2.644.822 bytes).
- O `montar_v1_13.py` (723370f5…, igual ao HEAD), rodado numa cópia, deu "RESULTADO: 0 FALHA", os mesmos dois SHA-256 e o mesmo `stats_v1_13_DA.json`.

**Diff contra a montagem anterior.**
- O HEAD de `out/` é 007787e3… e 8b5489b9…. O diff JSON dá só `/lotes/15/pares/0/como` no `pacote.json` e só `/lotes/12/pares/0/como` no `pacote_estudante.json`.
- Trocar só esse campo no HEAD e reserializar reproduz os arquivos atuais byte a byte.

**Por que `stats_v1_13_DA.json` mudou.** O `montar_v1_13.py` grava em `lotes.D<n>.sha_json` o SHA-256 de cada `D<n>_plataforma.json`. O diff contra o HEAD tem só `/lotes/D6/sha_json`, que passou de 8b8e5a42… para f8691dd5…, o SHA do D6 corrigido. Contagens, C/E, pares (43), pegadinhas (63) e itens por folha não mudaram.

`diag30_DA.json` não mudou (eb1ced6d…, igual ao HEAD).

**Conferência A (v1.12 intacta): OK nos dois arquivos.**
- Os 749 itens são idênticos byte a byte, na mesma posição.
- Também são idênticos os lotes da v1.12 (10 no `pacote.json` e 7 no estudante), as 47 entradas de edital P1/P2, os simulados, as discursivas e os 40 tópicos, na ordem relativa.
- O topo e `versao` não mudaram. Só mudam `nome` e `geradoEm`.
- O edital DA é igual a `edital_DA.json`, num bloco contíguo nas posições 20 a 65.
- Os 410 itens e os 6 lotes DA são iguais às fontes byte a byte. No estudante, os itens diferem só por `url` "" e `nucleo` como último campo.
- Os 39 tópicos DA são iguais às fontes como objeto, com as chaves `resumo`, `emUmMinuto` e `visuais`, nesta ordem.
- Edital, lotes DA e `topicos` do estudante são idênticos aos do `pacote.json`.

**Plataforma v16 (no lugar da conferência D, por leitura).**
- O template final (c6de3f2a…) tem 0 "pares", 0 ".como" e 0 "como" como chave.
- Os campos que o template lê do lote são `id`, `nome` (via `loteObj`), `prova`, `itensEdital`, `resumo`, `curso` e `pegadinhas`. `pares` não é lido.
- `plataforma_v16_publicar.html` tem o SHA-256 4d19eb05…, igual ao HEAD e ao publicado.
- O pacote embutido (`PUB_INLINE`, com `<\/` desfeito) é igual, como objeto, ao `out/pacote.json` anterior (007787e3).
- A diferença para o canônico 82c4117c é só `/lotes/15/pares/0/como`, que não é exibido.
- O arquivo publicado é um trecho contíguo de build(template final, 007787e3), pela regra própria (JSON compacto e `</` escapado).

A divergência entre a v16 publicada e o canônico está registrada na D1, seção 2, e vai à T-123.

**Integridade (D1, 5.6).** `git status` não tem nenhuma mudança em `saida/plataforma/`, `saida/simulados/`, `saida/estudante/`, `saida/pacote/pacote*.json`, `saida/pacote/gerador_v1_12/` nem `regras/`. D1–D5 e `edital_DA.json` não mudaram (F8), e `diag30_DA.json` também não (R5).

## 4. Conferência B e contagens (D1, 5.2 e 5.3)

**Canônicos.** O SHA-256 de D1_v2 (63bd27c3), de D2 a D5 v2.1 (59cffaa6, 0f7a8b09, c1a7a935, 44ddcc98) e de D6_v2_1 (a9831058) está na linha do próprio ato de aceite em DECISOES.md:
- D-LOTED1-CANONICO, linha 93;
- D-LOTED6-CANONICO, linha 117;
- D-LOTED5-CANONICO, linha 162;
- D-LOTED2-CANONICO, linha 163;
- D-LOTED3-CANONICO, linha 164;
- D-LOTED4-CANONICO, linha 165.

As linhas são iguais em HEAD.

**410 itens (parse próprio das seções 5.1 e 5.2 de cada canônico).**

| Lote | n | Ids = canônico | Ordem numérica | C/E | Gabarito ≠ | Enunciado ≠ | [TS] |
|---|---|---|---|---|---|---|---|
| lote D1 | 60 | sim | sim | 30/30 | 0 | 0 | 30 |
| lote D2 | 80 | sim | sim | 40/40 | 0 | 0 | 40 |
| lote D3 | 71 | sim | sim | 31/40 | 0 | 0 | 40 |
| lote D4 | 79 | sim | sim | 41/38 | 0 | 0 | 39 |
| lote D5 | 70 | sim | sim | 35/35 | 0 | 0 | 35 |
| lote D6 | 50 | sim | sim | 25/25 | 0 | 0 | 25 |

Outras conferências dos itens:
- `itemEdital` é igual à folha ou ao subitem do cabeçalho do canônico.
- `volatil` (D2-01, D2-28, D6-09, D6-32, D6-34) é igual à marca REVERIFICAR/VOLÁTIL do canônico e ao preâmbulo.
- Os campos fixos estão corretos em 410/410: AUTORAL, "Projeto Câmara 2026", cargo, 2026, "direta", `numero` e `url`.
- Os 1.159 ids são únicos.
- Os ids vagos D3-19, 31, 39, 42, 48, 50, 57, 60, 65 e 69 e D5-54 estão ausentes e não foram reutilizados.

**Varredura de marcas.** Li 4.201 campos de texto exibido de DA no `pacote.json`: nome, resumo e curso do lote; a, b e como dos pares; rótulo e texto das pegadinhas; comando, textoBase, enunciado e justificativa dos itens; resumo, emUmMinuto e toda string de visual dos tópicos; texto do edital. Usei a lista da seção 8.4 do QA, mais "folha", R/F com 1 ou 2 dígitos e url.

Resultado: **0 em todas as marcas.** Ficam os falsos positivos conhecidos:
- 53 "Presidência", todas "Presidência da República", que é conteúdo;
- "mecanismo:" em D4-46, que é conteúdo;
- os 197 "Como a banca troca:" prescritos.

Também há **0 `**` cru** nos campos que não são markdown e 0 `**` em número ímpar nos campos markdown. O validador deu 0 FALHA nos seis lotes (F10–F11).

**Recontagem do passo 4.3.2: tudo igual a `conferencia_t118.json`** (100 critérios, 0 FALHA). Os números:
- 46 entradas P1-DA, iguais a `edital_DA.json` e ao literal de `edital/DA_itens_1_12_P1.md` (parse próprio), todas com `prova` "P1";
- 16 lotes no `pacote.json` e 13 no estudante, com os 6 lotes DA no fim;
- 39 tópicos DA (79 no total), que são as 37 folhas mais P1-DA-1 e P1-DA-8;
- 37 folhas, com 396 itens em folha e 14 fora (P1-DA-1: 8; P1-DA-8: 6);
- 3 folhas com 20 ou mais (2.1 = 22, 11 = 30, 12 = 20) e 34 abaixo;
- no pacote inteiro, 27 itens fora de folha (13 + 14) e C/E 582/577;
- `nucleo` DA 366 true e 44 false. Os false estão em 1.1 (1), 1.2 (1), 2.1 (12), 11 (20) e 12 (10). O total do estudante é 733 (367 + 366).

**`nucleo_k1k4` (letra (e)).** Recalculei com:
- k1 = data do APLICADA da linha do ato, que dá 2026-10-18 para D1 e D6 e 2026-10-20 para D2 a D5, como na tabela da D1;
- k2 = linha do ato, pela minha própria regex de primeira ocorrência APLICADA;
- k3 = aderência;
- k4 = posição no `pacote.json`.

O resultado é **igual ao `nucleo` do estudante em 410/410**. Não há item não-DA em P1-DA nem folha com mais de um lote.

**Banco.** Há 40 linhas P1-DA, de BQ-0113 a BQ-0152. BQ-0131 e BQ-0133 estão anuladas, e as 38 restantes são vigentes. Nenhuma está nos dois pacotes.

## 5. Adendo 5 (D1, 5.4)

**OK:**
- O adendo em `saida/gbq/` é igual byte a byte a `out/registro_adendo5.md`, em LF.
- Os ids da seção 9 são exatamente os 410 do pacote, sem repetição, por folha igual ao `itemEdital`, com o n declarado correto e na ordem do edital.
- Na seção 1, canônico, n, SHA-256 do canônico (igual ao DECISOES.md, na linha do ato citada), ato e arquivo de plataforma com SHA-256 batem com o disco. O D6 aparece com o novo f8691dd5….
- Na seção 2, n, C, E, [TS], VOLÁTEIS, PARCIAIS e aptos são iguais à recontagem no pacote e no canônico, lote a lote, e o total é 410, 202, 208, 209, 5, 0 e 405.
- Na seção 3, os formatos de D2 a D5 são iguais à minha contagem do campo "Formato" de cada canônico, por código.
- Na seção 4, os vagos estão certos.
- Na seção 5, R1 tem os 5 voláteis; REVERIFICAR traz D2-01 e D2-28 (T-120) e D6-09, D6-32 e D6-34; R4-b tem 0; R6 tem 405.
- Na seção 6, as remissões (T75 5.5, T76 4.5, T77 5.5, D1 da T-74, T73 e T101) apontam para arquivos que existem.
- Também estão presentes as seções 7 (qualificação "lote D<n>") e 8 (D<n>-R<nn> reservados à T-116).
- Nenhum enunciado aparece no adendo.

**Contra o adendo 4.** A linha 1 segue o mesmo padrão (`# arquivo — T-nnn — data — gerado por gbq-csc (script)`), assim como a linha 2 e o parágrafo de base. As seções são paralelas: Fontes, Totais, Formatos, Ids vagos, Regras, Restrições e Itens por folha, com as mesmas colunas de totais. A seção 7 do adendo 4 ("Erratas e URL") não tem equivalente (achado 4).

**Falhas:**
- a coluna "Ids" da seção 1 está errada para lote D3 e lote D5 (achado 2);
- há ids de lote sem qualificação (achado 3).

## 6. Edição .md do estudante (D1, 5.5) e contrato

**Critérios do passo 4.3.4: todos OK.**
- São 53 arquivos: os 35 da base mais os 18 de DA.
- Os 35 da base têm o SHA-256 citado na promoção da v1.12. Desses, 33 são iguais byte a byte e só NUCLEO.md e README.md mudaram.
- No README.md, só saíram as linhas de versão e data e entraram v1.13-E, 2026-10-20 e 7 linhas de DA. A frase "dois visuais em todos os tópicos de DA" é verdadeira: são 78 visuais em 39 tópicos.
- Cada um dos 410 ids aparece 1 vez nos `_itens` e 1 vez nos `_gabarito`, no arquivo do próprio lote. Enunciado, gabarito, item do edital e justificativa são iguais aos do `pacote_estudante` **nos 410**, o que é mais que a amostra exigida.
- A amostra explícita de 41 ids (de 6 a 7 por lote, semente 20261020) foi lida bloco a bloco e confere: D1-50, D1-30, D1-48, D1-42, D1-53, D1-21, D1-14, D2-62, D2-08, D2-64, D2-11, D2-19, D2-05, D2-42, D3-76, D3-28, D3-09, D3-34, D3-63, D3-12, D3-30, D4-68, D4-28, D4-20, D4-07, D4-05, D4-21, D4-15, D5-35, D5-61, D5-53, D5-36, D5-27, D5-58, D5-12, D6-21, D6-14, D6-06, D6-46, D6-38, D6-47.
- A linha 1 de cada `DA_D<n>_estudo.md` é "# " + `lotes[D<n>].nome`.
- Resumo e curso são literais, em bloco de texto, como nos L<n>.
- Pares e pegadinhas são iguais ao JSON e não têm nenhum `**`.
- Os 39 tópicos têm cabeçalho, "Resumo do tópico" e "Em 1 minuto" literais.
- Os 78 visuais em texto conferem com o JSON:
  - 23 `compare`, como tabela "Aspecto | a | b" com a legenda;
  - 29 `baseLegal`, com a norma e "ref — texto (conferido AAAA-MM-DD)";
  - tabela, esquema, fluxo e linha, com todo o texto presente.
- Os 105 dispositivos aparecem literais.
- Nos 18 arquivos DA há **0** ocorrências de "folha", R/F, "QA PENDENTE", url, `D[1-6]` solto sem "lote ", "Lote", REVERIFICAR, VOLÁTIL, [TS], "Anexo N", T-nn, D-XXX e BQ-.
- NUCLEO.md tem 733 ids. As 39 linhas de DA são iguais ao `nucleo` true por `itemEdital`, no formato "(n de total)", e as linhas anteriores ficaram na mesma ordem.
- O relatório `estudante_md_v1_13.json` tem 53 arquivos e 0 FALHA.

**Sem gabarito em itens e folhas.** Os 6 `DA_D<n>_itens.md`, os demais `_itens.md` e as `_folha.md` dos simulados não têm nenhum "Gabarito:" nem "Justificativa".

**Contrato, regras da .md:**
- v1.2.5, ponto 4: o aviso VOLÁTIL fixo aparece exatamente nos 5 voláteis, nos itens e no gabarito. OK.
- v1.2.1, ponto 1 (texto-base antes do comando): não se aplica, porque os itens DA têm 0 `textoBase`.
- `nota`: não se aplica, porque os itens DA não têm o campo.
- v1.2.7, ponto 6 (NUCLEO.md): OK.
- v1.2.9, ponto 6 (resumo, Em 1 minuto e visuais em texto, com tabela em tabela e fluxo, linha e esquema em lista): OK.
- **v1.2.10, ponto 8: diverge** (achado 1).

**Cobertura (secretaria).** As 75 folhas (P1 15, P2 23, DA 37) foram recontadas no pacote, com total, AUTORAL, reais, diretos, PARCIAIS, VOLÁTEIS e núcleo, e são iguais linha a linha. Os totais também batem: 1.159 itens, 1.132 em folha, 27 fora, C/E 582/577, núcleo DA em folha 352 e 3 folhas DA com 20 ou mais. Não há nada para PARA_PRESIDENCIA.md, porque as folhas abaixo de 20 estão na T-116.

## 7. Achados

| N.º | Gravidade | Objeto | Achado | Bloqueia? |
|---|---|---|---|---|
| 1 | **MÉDIA** | Edição .md × contrato | O ponto 8 da v1.2.10 diz que a edição .md "não é gerada na v1.13" e que, quando for, "os pares de DA seguem a forma GCB do ponto 2 da v1.2.2, sem id: `- **a** × **b** \| como`". A D1 da T-118 (passo 4.3.4) manda gerar a .md com "0 `**` nas seções de pares e pegadinhas". O gerador cumpriu a D1: os 197 pares saem como `- a × b \| como` (0 de 197 na forma do contrato). Nenhuma errata do contrato registra a mudança, e o MANIFESTO (divergência 6) registra a escolha sem citar o ponto 8. É conflito entre dois textos da GBQ, sem erro de conteúdo. | **Sim**, para o aceite canônico e a promoção da edição .md. Não bloqueia o JSON nem o gatilho A (ponto 11). A gbq-gerencia escolhe um destes caminhos: (a) errata v1.2.11 do ponto 8 (.md gerada na v1.13; pares DA sem marcas), que é o caminho de menor custo e mantém os 53 arquivos; ou (b) regerar os pares de DA na forma do contrato e mudar o critério da D1. |
| 2 | **MÉDIA** | Adendo 5, seção 1 | Na coluna "Ids", lote D3 está como "D3-01 a D3-71 (sem os vagos da seção 4)" e lote D5 como "D5-01 a D5-70 (sem os vagos da seção 4)". Os ids reais vão de D3-01 a D3-81 (D3-71 a D3-80 na folha 7 e D3-81 na 6.2) e de D5-01 a D5-71 (D5-71 na 10.6). A faixa deixa fora do registro 10 ids do lote D3 (D3-72 a D3-81, nenhum deles vago) e 1 id do lote D5 (D5-71), e contradiz a seção 4 do próprio adendo ("D3-01 a D3-81, com 10 vagos"; "D5-01 a D5-71, com 1 vago"). A causa é que o n foi usado como último número. As seções 2 e 9 estão certas. | **Sim**, para o aceite do adendo 5 (condição (c) do gatilho A). A correção cabe à gbq-csc: trocar por "D3-01 a D3-81 (sem os vagos da seção 4)" e "D5-01 a D5-71 (sem o vago da seção 4)" no `registro_adendo_v113.py`, regerar `out/registro_adendo5.md` e a cópia de `saida/gbq/`, e atualizar o manifesto. |
| 3 | BAIXA | Adendo 5 | Ids de lote aparecem sem qualificação ("- D2: DEF 24…", "D1 e D6: o canônico…", "(D2)", "(D6)", "- D1: saida/gcb/T73…", "D3: D3-01…"), nas linhas 26, 29–33, 38 e 47–52. Isso contraria o ponto 9 da v1.2.10 ("em relatório, registro e diagnóstico da fábrica, o id vem sempre qualificado") e a seção 7 do próprio adendo. As colunas "Lote" das tabelas já qualificam. | Não. Corrigir junto com o achado 2 ("lote D2: …"). |
| 4 | BAIXA | Adendo 5 × adendo 4 | O adendo 4 tem a seção 7 "Erratas e URL", que remete ao registro de alterações por id. O adendo 5 não remete aos `D<n>_registro_formato.md`, que fazem esse papel para DA (v1.2.10, ponto 2), entre eles a errata do achado 10. A D1 não pediu essa remissão. | Não. Recomendo acrescentar uma linha na regeração do achado 2. |
| 5 | BAIXA (processo) | Promoção | `saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo5_2026-10-20.md` já está no repositório (14:11, antes da última geração de `out/`, que é igual), mas a D1, seção 4.6, manda promover só depois do aceite e em ato separado do orquestrador. O `registro_adendo_v113.py` grava só em `out/`. O MANIFESTO diz que "nada é promovido", mas lista o arquivo. | Não. Esta cópia não vale como canônica até o aceite, e depois do achado 2 será substituída. |
| 6 | INFO | MANIFESTO_v1_13.md | As 68 linhas batem com o disco. `cobertura_v1_13.py` (secretaria, 14:12) e este relatório foram gravados em `montagem_v1_13/` depois do manifesto e não estão nele. | Não. Atualizar o manifesto na regeração do achado 2 ou na promoção. |
| 7 | INFO | Árvore de trabalho | DECISOES.md, TAREFAS.md e PARA_PRESIDENCIA.md mudaram às 13:54, antes da D1 (14:00), na abertura do ciclo s15c1: marcas APLICADA e as tarefas T-122 a T-124. Essas mudanças estão fora da T-118. As linhas dos atos (93, 117, 162–165) são iguais em HEAD, por isso o `nucleo_k1k4` não muda. | Não. |
| 8 | INFO | Plataforma v16 | A v16 publicada embute 007787e3, a versão anterior à errata. A diferença para o canônico 82c4117c é só `lotes[D6].pares[0].como`, que o template não lê. Isso está registrado na D1, seção 2, e vai à T-123. | Não. |

As ressalvas 8 (notas editoriais, BAIXA) e 9 (meta `mapaspro:versao`, INFO) do QA final continuam como estavam. A D1 já as encaminhou, na seção 3 (T-117 e T-123).

## 8. Critérios de aceite da D1, um a um

| Passo | Critério | Resultado |
|---|---|---|
| 4.1 | D6 com 184.191 bytes e SHA-256 f8691dd5… | OK (F2) |
| 4.1 | Diff JSON contra 8b8e5a42 só em `/lote/pares[0]/como` | OK (F3) |
| 4.1 | 0 `**` em pares e pegadinhas dos seis lotes | OK (F7) |
| 4.1 | D1–D5 e `edital_DA.json` inalterados | OK (F8) |
| 4.2 | `como` muda só pela retirada de dois pares de `**` | OK (F4) |
| 4.2 | `lote.resumo` intacto, com negrito | OK (F5) |
| 4.2 | Registro de formato corresponde ao diff | OK (F9, F9b) |
| 4.2 | `validar_da.py` no D6 com 0 FALHA | OK (F10) |
| 4.2 | Parecer gcb-cqfp CONFERIDO | OK |
| 4.3.1 | `montar_v1_13.py` sem mudança e "RESULTADO: 0 FALHA" | OK (R6; cópia) |
| 4.3.1 | `pacote.json` com 2.906.558 bytes e SHA 82c4117c… | OK (R1) |
| 4.3.1 | `pacote_estudante.json` com 2.644.822 bytes e SHA 04cbd593… | OK (R1) |
| 4.3.1 | Diff contra 007787e3 e 8b5489b9 só no campo | OK (R2, R3) |
| 4.3.1 | `diag30_DA.json` intocado | OK (R5) |
| 4.3.2 | 410 itens, ids e gabaritos iguais ao canônico, SHA conferido, C/E por lote | OK (B0–B4) |
| 4.3.2 | 46 entradas P1-DA iguais a `edital_DA.json` e ao .md do edital, contíguas em 20–65 | OK (A2, K6) |
| 4.3.2 | 6 lotes DA (16 no total) | OK (K5) |
| 4.3.2 | 39 tópicos DA iguais às fontes como objeto (79 no total) | OK (A5, K3) |
| 4.3.2 | `nucleo` 366/44 com a distribuição do preâmbulo | OK (K7) |
| 4.3.2 | `volatil` igual ao preâmbulo | OK (B5) |
| 4.3.2 | 749 itens da v1.12 byte a byte | OK (A) |
| 4.3.2 | 37 folhas, 396 em folha e 14 fora | OK (K1) |
| 4.3.2 | Os 38 do banco ausentes | OK (K11) |
| 4.3.2 (e) | `nucleo_k1k4` igual em 410/410 com os atos e as linhas da tabela | OK (K8, K9) |
| 4.3.3 | Ids do adendo iguais aos 410 do pacote | OK (D1) |
| 4.3.3 | SHA-256 igual ao de DECISOES.md | OK (D2) |
| 4.3.3 | Soma por lote igual a 410 | OK (D4) |
| 4.3.3 | Nenhum enunciado | OK (D8) |
| 4.3.3 | Conteúdo: fontes, totais, formatos, vagos, R1/REVERIFICAR, R6, restrições, "lote D<n>", D<n>-R<nn>, itens por folha | OK, **salvo a coluna Ids das fontes (achado 2)** e a qualificação (achado 3) |
| 4.3.4 | 53 arquivos; 33 iguais à base | OK (M1, M3) |
| 4.3.4 | Cada um dos 410: 1× em `_itens` e 1× em `_gabarito`, com texto igual | OK (M6, M7) |
| 4.3.4 | Linha 1 do `_estudo` igual a "# " + nome | OK (M11) |
| 4.3.4 | 105 dispositivos literais | OK (M14) |
| 4.3.4 | 0 de folha, R/F, "QA PENDENTE", url e D<n> solto | OK (M15) |
| 4.3.4 | 0 `**` em pares e pegadinhas | OK (M11), mas diverge do contrato v1.2.10, ponto 8 (achado 1) |
| 4.3.4 | NUCLEO.md com 733 ids | OK (M5) |
| 4.3.5 | Manifesto com bytes e SHA-256; nada promovido | OK nos valores; promoção antecipada do adendo (achado 5) e manifesto incompleto (achado 6) |
| 4.4 | Cobertura: 75 folhas, 1.159, 1.132/27, 582/577, DA 396 / 5 VOLÁTEIS / núcleo 352 / 0 reais, 3 ≥20 e 34 <20, nada em PARA_PRESIDENCIA | OK (V1, V2) |
| 5.6 | Integridade de `saida/plataforma/`, simulados, `diag30`, D1–D5 e `edital_DA` | OK (I1, F8, R5) |

## 9. O que bloqueia o aceite canônico

1. **Achado 2 (adendo 5, faixa de ids de lote D3 e lote D5).** Bloqueia o aceite do adendo 5, que é a condição (c) do gatilho A da v1.13. O caminho é: corrigir no `registro_adendo_v113.py` (com os achados 3 e 4, opcionais), regerar `out/registro_adendo5.md`, substituir a cópia em `saida/gbq/` só no ato de promoção e atualizar o manifesto. Basta uma reconferência curta da gbq-cqe nas seções 1 e 2 do adendo novo e no diff contra este (7224db40…).
2. **Achado 1 (edição .md × contrato v1.2.10, ponto 8).** Bloqueia o aceite canônico e a promoção de `out/estudante/` a `saida/estudante/` até a gbq-gerencia registrar a errata v1.2.11 do ponto 8 ou mandar regerar. Não bloqueia o gatilho A nem o JSON.

`pacote.json` e `pacote_estudante.json` (82c4117c… e 04cbd593…), a errata do achado 10, `conferencia_t118.json` e `cobertura_v1_13.md` estão aptos ao aceite. A promoção é byte a byte, pelo orquestrador. Publicar continua reservado ao Fundador (D-V15-PLATAFORMA), e a próxima plataforma (T-123) embute o canônico.
