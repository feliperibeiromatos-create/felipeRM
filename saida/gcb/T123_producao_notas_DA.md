# T123_producao_notas_DA.md — T-123, limpeza das marcas de produção nas justificativas do reforço de DA — 2026-10-23 — gerado por gcb-cpp

Insumos: `saida/gcb/T123_limpeza_D1_GCB_2026-10-23.md` (D1, seção 4); `saida/pacote/montagem_v1_14/T123_ocorrencias_DA.csv`; texto-base `saida/pacote/montagem_v1_14/out/reforco_bruto.json` (somente leitura). Saída irmã: `saida/gcb/T123_substituicoes_DA.csv` (91 edições; SHA-256 LF do arquivo: `01d5be77e40d74b1f4ae7be8faf05f4b222e4e1af39c61081c3b3fb13d152505`). Nenhum arquivo de leva, JSON, CSV de ocorrências, DECISOES, TAREFAS ou PARA_PRESIDENCIA foi tocado. Sem commit.

## (a) Tabela de fontes

Forma curta da seção 3.1 do `D4_registro_formato.md`, sem página e sem URL. Códigos distintos: 29 (27 códigos R com publicação por extenso, operação 6, mais G6 e G9, que saem pela operação 3 porque a frase já nomeia o Guia). NÃO IDENTIFICADO: nenhum. Nenhuma fonte nova. As datas de consulta são as registradas na linha "Base:" do item (ou, na falta, a do adendo).

| código | nome por extenso (como vai ao texto) | onde está identificado | data de consulta registrada | itens que usam |
|---|---|---|---|---|
| G6 | o Guia da Política de Governança Pública (Casa Civil, 2018) | Base (a do D4-R52, não a do D4-R51): saida/gcb/DA_reforco_leva8_v2.md:543; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-22.md:175 (seção 5) | 20/10/2026 | D4-R51 |
| G9 | o Guia da Política de Governança Pública (Casa Civil, 2018) | Base: saida/gcb/DA_reforco_leva8_v2.md:322; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-22.md:178 (seção 5) | 20/10/2026 | D4-R38 |
| R37 | o artigo de Bouckaert (ENAP, 2024) | Base: saida/gcb/DA_reforco_leva1_v2.md:124; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:153 (seção 5) | 20/10/2026 | D4-R01 |
| R39 | o artigo de Bouckaert (ENAP, 2024) | Base: saida/gcb/DA_reforco_leva1_v2.md:139 e saida/gcb/DA_reforco_leva1_v2.md:185 (D4-R05); adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:155 (seção 5) | 20/10/2026 | D4-R02, D4-R05 |
| R40 | o artigo de Bouckaert (ENAP, 2024) | Base: saida/gcb/DA_reforco_leva1_v2.md:200; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:156 (seção 5) | 20/10/2026 | D4-R06 |
| R43 | o texto de Silvestre (ENAP, 2019) | Base: saida/gcb/DA_reforco_leva1_v2.md:170; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:159 (seção 5) | 20/10/2026 | D4-R04 |
| R44 | o texto de Silvestre (ENAP, 2019) | Base: saida/gcb/DA_reforco_leva1_v2.md:325; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:160 (seção 5) | 20/10/2026 | D4-R14 |
| R45 | o texto de Silvestre (ENAP, 2019) | Base: saida/gcb/DA_reforco_leva1_v2.md:231; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:161 (seção 5) | 20/10/2026 | D4-R08 |
| R46 | o texto de Silvestre (ENAP, 2019) | Base: saida/gcb/DA_reforco_leva1_v2.md:216 e saida/gcb/DA_reforco_leva1_v2.md:279 (D4-R11); adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:162 (seção 5) | 20/10/2026 | D4-R07, D4-R11 |
| R53 | o texto de Cavalcante (Ipea, 2018) | Base: saida/gcb/DA_reforco_leva1_v2.md:247; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:169 (seção 5) | 20/10/2026 | D4-R09 |
| R54 | o texto de Cavalcante (Ipea, 2018) | Base: saida/gcb/DA_reforco_leva1_v2.md:294; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:170 (seção 5) | 20/10/2026 | D4-R18 |
| R55 | o texto de Cavalcante (Ipea, 2018) | Base: saida/gcb/DA_reforco_leva1_v2.md:154; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:171 (seção 5) | 20/10/2026 | D4-R03 |
| R57 | o texto de Cavalcante (Ipea, 2018) | Base: saida/gcb/DA_reforco_leva1_v2.md:263; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:173 (seção 5) | 20/10/2026 | D4-R10 |
| R60 | o Referencial Básico de Governança Organizacional (TCU, 2020) | Base: saida/gcb/DA_reforco_leva2_v2.md:179; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:176 (seção 5) | 20/10/2026 | D4-R20 |
| R62 | o Referencial Básico de Governança Organizacional (TCU, 2020) | Base: saida/gcb/DA_reforco_leva2_v2.md:240; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:178 (seção 5) | 20/10/2026 | D4-R24 |
| R63 | o Referencial Básico de Governança Organizacional (TCU, 2020) | Base: saida/gcb/DA_reforco_leva1_v2.md:546; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:179 (seção 5) | 20/10/2026 | D4-R15 |
| R64 | o Referencial Básico de Governança Organizacional (TCU, 2020) | Base: saida/gcb/DA_reforco_leva1_v2.md:562; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:180 (seção 5) | 20/10/2026 | D4-R16 |
| R65 | o documento didático da CGU | Base: saida/gcb/DA_reforco_leva2_v2.md:210; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:181 (seção 5) | 20/10/2026 | D4-R22 |
| R66 | o documento didático da CGU | Base: saida/gcb/DA_reforco_leva2_v2.md:194; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:182 (seção 5) | 20/10/2026 | D4-R21 |
| R67 | o documento didático da CGU | Base: saida/gcb/DA_reforco_leva2_v2.md:272; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:183 (seção 5) | 20/10/2026 | D4-R26 |
| R72 | o texto de Martins (Ipea, 2018) | Base: saida/gcb/DA_reforco_leva1_v2.md:578; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:188 (seção 5) | 20/10/2026 | D4-R17 |
| R74 | o guia prático de análise ex post (Casa Civil, 2018) | Base: saida/gcb/DA_reforco_leva2_v2.md:303; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:190 (seção 5) | 20/10/2026 | D4-R28 |
| R76 | o guia prático de análise ex post (Casa Civil, 2018) | Base: saida/gcb/DA_reforco_leva2_v2.md:256; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:192 (seção 5) | 20/10/2026 | D4-R25 |
| R77 | o guia prático de análise ex post (Casa Civil, 2018) | Base: saida/gcb/DA_reforco_leva2_v2.md:164; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:193 (seção 5) | 20/10/2026 | D4-R19 |
| R78 | o guia prático de análise ex post (Casa Civil, 2018) | Base: saida/gcb/DA_reforco_leva2_v2.md:164; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:194 (seção 5) | 20/10/2026 | D4-R19 |
| R79 | o guia prático de análise ex post (Casa Civil, 2018) | Base: saida/gcb/DA_reforco_leva2_v2.md:287; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:195 (seção 5) | 20/10/2026 | D4-R27 |
| R80 | o guia prático de análise ex post (Casa Civil, 2018) | Base: saida/gcb/DA_reforco_leva2_v2.md:287; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:196 (seção 5) | 20/10/2026 | D4-R27 |
| R81 | o guia prático de análise ex post (Casa Civil, 2018) | Base: saida/gcb/DA_reforco_leva2_v2.md:225; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:197 (seção 5) | 20/10/2026 | D4-R23 |
| R83 | o texto de Cavalcante (Ipea, 2018) | Base: saida/gcb/DA_reforco_leva1_v2.md:309; adendo: saida/gcb/D4_anexo_N_adendo_2026-10-20.md:199 (seção 5) | 20/10/2026 | D4-R13 |

Pontos para o QA nesta tabela:
- R65, R66 e R67 (Controladoria-Geral da União, documento didático "Cadeia de valor da CGU", sem data impressa): a forma é "o documento didático da CGU", a mesma já usada no `D4_registro_formato.md` (3.1, C8.4-03); sem ano, porque a Base registra "sem data impressa".
- R63 e R64 usam o ano 2020 (3. ed., 2020 na Base), como no `D4_registro_formato.md` ("Referencial Básico de Governança Organizacional (TCU, 2020)").
- R46 e R43/R44/R45: a Base diz "Enap" e o adendo "ENAP"; usei "ENAP", forma do exemplo da seção 3 do D1 e do registro de formato.
- D4-R20 e D4-R24: depois da troca, a frase repete "Referencial" ("O Referencial Básico de Governança Organizacional (TCU, 2020) lista, entre as diretrizes para a boa governança do Referencial do TCU, ..."; "... registra, no Referencial do TCU, ..."). Mantive porque a regra manda o nome por extenso e proíbe palavra nova; a repetição é do texto original ("do Referencial do TCU"). Se o QA ou a GCB preferirem, a correção é de redação e exige decisão da GCB.

## (b) Contagens

Edições: 91, cobrindo as 103 ocorrências MARCA do CSV (uma vez cada) mais 1 EXTRA (GCB-EXTRA-01), no total de 104 ids de ocorrência. Itens editados: 85. Itens sem MARCA tocados: 0.

| por categoria da edição | edições | ocorrências MARCA cobertas |
|---|---|---|
| C02 | 6 | 18 |
| C03 | 33 | 33 |
| C05 | 35 | 35 |
| C10 | 17 | 17 |

(Categoria da edição = a da marca principal; edições que absorvem ocorrências de outra categoria, como o D3-R33 e as C02 com sufixo C05, contam as ocorrências na categoria da edição.)

| por operação | edições |
|---|---|
| 3 | 39 |
| processo | 23 |
| 6 | 29 |

| por ação | edições |
|---|---|
| DELETAR | 45 |
| SUBSTITUIR | 46 |

| por modo | edições |
|---|---|
| TEMPLATE | 91 |
| LIVRE | 0 |

## (c) Linhas alargadas, EXTRA e marcas achadas em itens sem MARCA

Linhas alargadas, fundidas ou com contração (a `nota` da linha explica): 50 de 91. Todas as demais têm `antes` igual ao `antes_unico` do CSV: GCB-T123-0001, GCB-T123-0003, GCB-T123-0004, GCB-T123-0005, GCB-T123-0006, GCB-T123-0008, GCB-T123-0010, GCB-T123-0011, GCB-T123-0012, GCB-T123-0014, GCB-T123-0015, GCB-T123-0016, GCB-T123-0025, GCB-T123-0026, GCB-T123-0027, GCB-T123-0028, GCB-T123-0029, GCB-T123-0030, GCB-T123-0031, GCB-T123-0032, GCB-T123-0033, GCB-T123-0034, GCB-T123-0035, GCB-T123-0036, GCB-T123-0037, GCB-T123-0064, GCB-T123-0065, GCB-T123-0067, GCB-T123-0069, GCB-T123-0070, GCB-T123-0071, GCB-T123-0072, GCB-T123-0073, GCB-T123-0075, GCB-T123-0077, GCB-T123-0078, GCB-T123-0079, GCB-T123-0080, GCB-T123-0082, GCB-T123-0084, GCB-T123-0085.

| id_edicao | item | antes | depois |
|---|---|---|---|
| GCB-T123-0002 | D4-R01 | ` (alerta B9)` | `` |
| GCB-T123-0007 | D4-R05 | ` (alerta B9)` | `` |
| GCB-T123-0009 | D4-R07 | `de R46` | `do texto de Silvestre (ENAP, 2019)` |
| GCB-T123-0013 | D4-R11 | `de R46` | `do texto de Silvestre (ENAP, 2019)` |
| GCB-T123-0017 | D4-R14 | `(alerta B4: ` | `(` |
| GCB-T123-0018 | D3-R01 | ` (alerta A2)` | `` |
| GCB-T123-0019 | D3-R02 | ` (alerta A11)` | `` |
| GCB-T123-0020 | D3-R04 | ` (alerta A7)` | `` |
| GCB-T123-0021 | D3-R09 | ` (alerta A1)` | `` |
| GCB-T123-0022 | D3-R12 | ` (alerta A1)` | `` |
| GCB-T123-0023 | D4-R15 | `R63 (TCU, que cita Kaplan e Norton)` | `O Referencial Básico de Governança Organizacional (TCU, 2020), que cita Kaplan e Norton,` |
| GCB-T123-0024 | D4-R16 | `R64 (TCU)` | `O Referencial Básico de Governança Organizacional (TCU, 2020)` |
| GCB-T123-0038 | D1-R02 | ` (alerta P4)` | `` |
| GCB-T123-0039 | D3-R15 | `(alerta A2: ` | `(` |
| GCB-T123-0040 | D3-R17 | ` (alertas A2 e A11)` | `` |
| GCB-T123-0041 | D3-R20 | ` (alerta A1)` | `` |
| GCB-T123-0042 | D3-R25 | `(pertinência parcial: regime de consumo, alerta A7)` | `(regime de consumo)` |
| GCB-T123-0043 | D3-R26 | ` (alerta A3)` | `` |
| GCB-T123-0044 | D3-R31 | `; alerta A5)` | `)` |
| GCB-T123-0045 | D3-R32 | ` (alerta A6)` | `` |
| GCB-T123-0046 | D3-R33 | ` (C com moldura em par com o E com moldura além da cota da folha: D3-R27, D3-R31 e D3-R35)` | `` |
| GCB-T123-0047 | D3-R36 | `(alerta A8: ` | `(` |
| GCB-T123-0048 | D3-R37 | `(alertas A7 e A11: ` | `(` |
| GCB-T123-0049 | D3-R43 | `: alerta C2)` | `)` |
| GCB-T123-0050 | D3-R44 | `(alertas C1 e C4: ` | `(` |
| GCB-T123-0051 | D3-R46 | ` (alerta C1)` | `` |
| GCB-T123-0052 | D3-R49 | `: alerta C8)` | `)` |
| GCB-T123-0053 | D3-R50 | `(alerta C7: ` | `(` |
| GCB-T123-0054 | D3-R51 | `(alerta C6: ` | `(` |
| GCB-T123-0055 | D3-R52 | `(alerta C9: ` | `(` |
| GCB-T123-0056 | D3-R53 | ` (alerta C9)` | `` |
| GCB-T123-0057 | D3-R54 | `(alerta C6: ` | `(` |
| GCB-T123-0058 | D3-R55 | `: alerta C8)` | `)` |
| GCB-T123-0059 | D3-R56 | ` (alerta C9)` | `` |
| GCB-T123-0060 | D3-R57 | `(alerta C11: ` | `(` |
| GCB-T123-0061 | D3-R58 | `(alerta C9: ` | `(` |
| GCB-T123-0062 | D3-R59 | `(alerta C7: ` | `(` |
| GCB-T123-0063 | D2-R02 | `, tema de outro ponto da folha` | `` |
| GCB-T123-0066 | D2-R07 | ` (alerta 1)` | `` |
| GCB-T123-0068 | D2-R25 | `, objeto do D2-R23` | `` |
| GCB-T123-0074 | D2-R45 | ` (objeto do D2-41)` | `` |
| GCB-T123-0076 | D2-R48 | `, objeto do D2-R50` | `` |
| GCB-T123-0081 | D2-R77 | ` (L5-2)` | `` |
| GCB-T123-0083 | D3-R74 | `, base do D3-R53` | `` |
| GCB-T123-0086 | D4-R31 | `; Anexo N do D4, seção 4.3` | `` |
| GCB-T123-0087 | D4-R34 | ` (Anexo N do D4, seção 4.2)` | `` |
| GCB-T123-0088 | D4-R35 | `; Anexo N do D4, seção 4.2` | `` |
| GCB-T123-0089 | D4-R38 | ` (G9, ii e iii)` | `` |
| GCB-T123-0090 | D4-R43 | ` (Anexo N do D4, seção 4.1)` | `` |
| GCB-T123-0091 | D4-R51 | ` (G6)` | `` |

EXTRA: GCB-EXTRA-01, "pertinência parcial:" no D3-R25, absorvida na edição GCB-T123-0042 (mesmo parêntese do "alerta A7"), como prevê o D1. Nenhuma outra EXTRA.

Marcas em itens sem MARCA (não editadas): nenhuma. Varredura com os padrões da C-MARCAS (seção 8.1 do D1 da GBQ) e "pertinência parcial", sobre enunciado e justificativa dos 153 itens sem MARCA, no texto-base.

Outras observações: nenhum "moldura", "folha" ou "cota" em sentido de conteúdo foi achado (além do "desconto em folha" do D3-R75, FP, intacto). Os 4 VERIFICAR e os 2 FP ficaram sem edição (D4-R24 "produção", D2-R21 e D2-R24 "Presidência", D3-R75 "folha"; BQ-0113 está no banco, fora do reforço). O D4-R24 tem uma edição, a do código R62, que não toca "produção".

## (d) Autoconferência (python -I, só leitura; script e cópia em scratchpad `gcb_t123/`)

- (1) antes literal, único, sem sobreposição: **PASSA**. erros=[]
- (2) 103 MARCA cobertas 1 vez: **PASSA**. MARCA=103, nao cobertas/duplicadas=[], VERIFICAR/FP cobertos=[], EXTRA=['GCB-EXTRA-01']
- (3) DELETAR com depois vazio; op 6 com fonte_origem: **PASSA**. violacoes=[]
- (4) C-MARCAS e "pertinência parcial" = 0 nos 238 (exceção: desconto em folha, D3-R75): **PASSA**. restantes=[]
- (5) PROCESSO (marcas_processo.py) = 0, salvo os 2 casamentos "Presidência" (VERIFICAR/conteúdo, D2-R21 e D2-R24, iguais antes e depois): **PASSA**. antes=2 depois=2; restantes=[]
- (6) enunciado/gabarito/itemEdital/aderência idênticos; justificativas dos itens sem MARCA byte a byte: **PASSA**. itens sem MARCA=153; campos alterados=[]; sem-MARCA alterados=[]; itens editados=85
- (7) 4 VERIFICAR e 2 FP intactos: **PASSA**. VERIFICAR=['D4-R24', 'D2-R21', 'D2-R24', 'BQ-0113'] FP=['D3-R75', 'D3-R75']; BQ-0113 fora do reforço (nao tocado); violacoes=[]

Esclarecimento do ponto (5): o inventário PROCESSO de `marcas_processo.py` dá 2 casamentos nos 238 itens, antes e depois das edições, ambos "Presidência" em "Presidência da República" (D2-R21 e D2-R24, VERIFICAR/conteúdo, D1 seção 1.4, que manda não editar). Os casamentos fora esses dois: 0. Como o inventário na D1 da GBQ é lido com a lista X de conteúdo, o resíduo esperado é só esse par.

Pendências: nenhuma código NÃO IDENTIFICADO; nenhuma marca achada em item sem MARCA; os pontos de redação para o QA estão no fim da seção (a).

## Rodada 2 (resposta ao QA_T123_limpeza_R1_2026-10-23_gcb-cqfp.md)

- **Veredito R1.** DEVOLVIDO (89 APROVADO, 2 CORRIGIR, 0 REPROVADO). Aceito sem objeção.
- **Linha GCB-T123-0028 (D4-R20): acatado.** `antes` alargado para `R60 lista, entre as diretrizes para a boa governança do Referencial do TCU,`; `depois` = `O Referencial Básico de Governança Organizacional (TCU, 2020) lista, entre as diretrizes para a boa governança,`; `nota` = "alargado (sem repetir)". Texto exato do parecer, sem palavra nova.
- **Linha GCB-T123-0032 (D4-R24): acatado.** `antes` = `R62 registra, no Referencial do TCU,`; `depois` = `O Referencial Básico de Governança Organizacional (TCU, 2020) registra`; `nota` = "alargado (sem repetir)". O VERIFICAR "produção" do D4-R24 segue intacto.
- **Demais 89 linhas: sem alteração.** `T123_substituicoes_DA_v2.csv` difere da v1 só nas linhas 0028 e 0032 (colunas antes, depois, nota), conferido por script (ver abaixo). Com essas duas, as linhas alargadas passam de 50 para 52 de 91; a lista da seção (c) fica desatualizada nesses dois ids e vale esta rodada.
- **P2, G6: acatado.** A Base citada na tabela de fontes (l. 543 da leva 8) é a do D4-R52, e não a do D4-R51 (l. 527 é G5). A linha de G6 foi corrigida para dizer isso; o G6 no D4-R51 está na justificativa e no campo "Troca", identificado no adendo de 22/10, seção 5, l. 175. A deleção do D4-R51 (0091) não muda.
- **P2, R39 e R46: acatado.** Acrescentadas as Bases do D4-R05 (leva 1, l. 185, código R39) e do D4-R11 (leva 1, l. 279, código R46) às linhas de R39 e R46.
- **P1 (GBQ):** não é desta unidade; registrado. Os dois casamentos "Presidência da República" (D2-R21, D2-R24) seguem como conteúdo (VERIFICAR) e ficam intactos.
- **Autoconferência da rodada (python -I, só leitura):** resultado abaixo.
  - Diff v1 x v2 (bytes): 93 linhas físicas em cada (cabeçalho + 91 + final vazio); diferem só as linhas 29 e 33 do arquivo (GCB-T123-0028 e GCB-T123-0032); cabeçalho igual; sem CR; 91 registros. **PASSA.**
  - `antes` das duas linhas: ocorre 1 vez na justificativa do item (D4-R20 e D4-R24) e contém o `antes_unico` (R60 / R62). **PASSA.**
  - Texto resultante: sem "Referencial do TCU" residual; as frases ficam "O Referencial Básico de Governança Organizacional (TCU, 2020) lista, entre as diretrizes para a boa governança, a de apoiar..." e "... (TCU, 2020) registra a classificação das atividades...". **PASSA.**
  - Demais critérios da mecânica (a, c, d, e, f do parecer, seção 1) dependem só de `antes`/`depois`/`acao`/`operacao`/`fonte_origem`, que não mudam nas outras 89 linhas; as linhas 0028 e 0032 continuam SUBSTITUIR, operação 6, com `fonte_origem` preenchida.
