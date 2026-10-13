# QA_schema02_2026-10-13_gbq-cqe.md — D-SCHEMA-02-EXEC (T-29 + T-42), conferência por amostragem — 2026-10-13 — gerado por gbq-cqe

Objeto: colunas texto_comando e texto_base acrescentadas a banco/banco.csv (112 linhas) e banco/SCHEMA.md, produzidos pela gbq-csc (commit 82bea20; base 91c82af). Relatório de produção: saida/banco/schema02_2026-10-13.md. A gbq-cqe não produziu o objeto. Somente leitura do repositório; único arquivo gravado: este parecer.

## 1. Veredito

**APROVADO COM RESSALVAS.**

- banco/banco.csv: **APROVADO** sem correção. As 15 colunas antigas estão idênticas em 112/112, o formato do arquivo foi preservado e, na amostra de 32 linhas (19/19 cadernos), texto_comando e texto_base conferem com o caderno oficial. Fora da amostra, a conferência por script independente deu texto_comando literal em 112/112. A varredura de texto-base nos 19 cadernos não encontrou nenhum texto-base omitido.
- banco/SCHEMA.md: **ressalva de forma (R-1)**. A frase "(o pacote exporta o vazio como "nenhum")" vale para a v1.1 e ficou desatualizada diante da F2 da v1.2 (D-T12-V12). Correção exata na seção 6.
- Convenção de BQ-0070, 0071 e 0112: é fiel ao caderno. Recomendo à GBQ **manter**, com uma cautela para a T-48 (seção 5).

## 2. (a) Conferência por script: colunas antigas e formato

Script próprio (scratchpad s4/qa_t29/scripts/a.py), csv com delimiter=';', comparado com `git show 91c82af:banco/banco.csv` (sha256 969c0bfd…, igual ao "antes" da produção). O arquivo atual (sha256 6ce6d5ec…) é idêntico ao do commit 82bea20.

| Verificação | Resultado |
|---|---|
| Linhas (cabeçalho + itens) antes/depois | 113 / 113 |
| Colunas antes/depois | 15 em todas as linhas / 17 em todas as linhas |
| Cabeçalho | 15 nomes antigos idênticos, na mesma ordem, mais `texto_comando`, `texto_base` ao final |
| 15 colunas antigas idênticas, linha a linha | **112/112** (0 diferenças) |
| ids e ordem | 112 ids únicos, BQ-0001…BQ-0112, mesma ordem |
| Linha física nova = linha antiga + `;texto_comando;texto_base` | 114/114 linhas físicas (prefixo byte a byte) |
| Terminador de linha | LF nos dois arquivos, 0 CR, termina em `\n`, sem BOM |
| Quoting | QUOTE_MINIMAL nos dois. Releitura e regravação com csv.writer(';', lineterminator='\n', QUOTE_MINIMAL) devolvem os dois arquivos **byte a byte idênticos**. Nenhum campo novo exige aspas (0 com `;`, `"` ou quebra de linha) |

Resultado: formato coerente com o anterior e nenhum leitor existente deslocado.

## 3. (b) Amostra e conferência contra os cadernos oficiais

**Método.** Baixei com curl os 19 cadernos distintos de url_caderno, todos de cdn.cebraspe.org.br (HTTP 200 nos 19), para o scratchpad s4/qa_t29/pdfs/. O tamanho e o prefixo de sha256 dos 19 PDFs conferem com a tabela da seção 3 do relatório de produção. A extração usou pdftotext e um extrator próprio com pdfplumber, que separa as duas colunas e registra o recuo de cada linha. No caderno ANATEL 002 o pdftotext embaralha colunas, por isso valeu a extração por coluna.

Em cada linha conferi:
1. o item pelo numero_item: linha na margem com o número seguido do início do texto_integral, ocorrência única no caderno;
2. o comando: o parágrafo na margem que antecede o grupo do item, sem outro comando entre ele e o item;
3. o que vem imediatamente antes do comando, para ver se existe texto, situação, quadro ou código que o comando chame de "precedente".

**Além da amostra.**
- O script de reconstrução literal do comando a partir do PDF (scripts/c.py, independente do da produção) rodou nas 112 linhas. Deu igualdade exata, caractere a caractere, em 105/112.
- As 7 restantes conferi à mão e estão corretas:
  - BQ-0049, 0050 e 0051: o script juntou texto-base e comando porque o primeiro parágrafo é recuado. Separados, o texto_base confere exato, 373 caracteres, e o texto_comando também.
  - BQ-0103 a 0106: falso positivo do meu script, que mudou de coluna na p. 2. No caderno, os itens 86 a 97 estão todos sob "Julgue os próximos itens, relativos a aprendizado de máquina.", sem comando intermediário, e o comando seguinte, "Julgue os próximos itens, relativos a extração e representação de conhecimento…", só vem antes do item 98.
- Total: **texto_comando literal em 112/112** e item localizado pelo numero_item em 112/112.

**Escolha da amostra (32 linhas).**
- Os 19 cadernos estão cobertos.
- Entram as obrigatórias BQ-0049/0050/0051 e BQ-0070/0071/0112.
- Entram 4 anuladas: BQ-0029, 0031, 0060 e 0062.
- Entram 13 linhas de BQ-0067..0112.
- Entram casos de início de página ou coluna, onde um texto-base no fim da coluna anterior poderia ter escapado.

| id | caderno (url_caderno) | item | comando OK? | texto_base OK? | observação |
|---|---|---|---|---|---|
| BQ-0001 | TRF6_24 034_TRF6_002 | 63 | OK | OK (vazio) | comando no topo da p1 col2; antes, item 62 |
| BQ-0006 | TRF6_24 034_TRF6_002 | 74 | OK | OK (vazio) | comando no topo da p2 col1; antes, item 73 |
| BQ-0012 | TRF6_24 034_TRF6_002 | 98 | OK | OK (vazio) | grupo de 96; topo da p3 col1; antes, item 95 |
| BQ-0016 | bcb_24 959_BCB_002 | 64 | OK | OK (vazio) | antes, item 63 (MLOps) |
| BQ-0018 | anatel_24 961_ANATEL_002 | 87 | OK | OK (vazio) | topo da p2 col2; antes, item 85 |
| BQ-0025 | anatel_24 961_ANATEL_002 | 84 | OK | OK (vazio) | antes, item 83 |
| BQ-0029 | susep_25 065_SUSEP_004 | 62 | OK | OK (vazio) | ANULADA; grupo de 61; antes, item 60 |
| BQ-0031 | susep_25 065_SUSEP_004 | 79 | OK | OK (vazio) | ANULADA; grupo de 76, sob o título "SEGURANÇA DA INFORMAÇÃO"; antes, item 75 |
| BQ-0036 | cnj_24 979_CNJ_002 | 97 | OK | OK (vazio) | antes, item 96 |
| BQ-0040 | cnj_24 979_CNJ_002 | 113 | OK | OK (vazio) | topo da p4 col1; antes, item 112 (o grupo do firewall, 111–112, é outro) |
| BQ-0041 | ANTT_23 951_ANTT_001 | 1 | OK | OK (vazio) | antes, só a caixa de instruções e o título da prova, que não são texto-base |
| BQ-0044 | ANTT_23 951_ANTT_001 | 10 | OK | OK (vazio) | antes, item 9 |
| BQ-0048 | embrapa_24 042_EMBRAPA_ANALISTA_026 | 93 | OK | OK (vazio) | grupo de 88; antes, item 87. O "quadro precedente" deste caderno rege o item 96, que não está no banco |
| BQ-0049 | embrapa_24 042_EMBRAPA_ANALISTA_034 | 91 | OK | OK (373 caracteres, exato) | divisão texto_base/comando correta: o comando remete à "situação hipotética precedente" |
| BQ-0050 | embrapa_24 042_EMBRAPA_ANALISTA_034 | 92 | OK | OK (idem) | mesmo grupo |
| BQ-0051 | embrapa_24 042_EMBRAPA_ANALISTA_034 | 93 | OK | OK (idem) | mesmo grupo |
| BQ-0054 | embrapa_24 042_EMBRAPA_ANALISTA_071 | 81 | OK | OK (vazio) | antes, item 80 |
| BQ-0060 | anm_24 038_ANM_024 | 92 | OK | OK (vazio) | ANULADA; grupo de 90; antes, item 89 |
| BQ-0062 | anm_24 038_ANM_024 | 95 | OK | OK (vazio) | ANULADA; mesmo grupo, sem comando intermediário |
| BQ-0065 | pf_25 106_PF_004 | 104 | OK | OK (vazio) | topo da p4 col1; antes, item 103 |
| BQ-0070 | pf_25 106_PF_004 | 87 | OK | OK (vazio) | situação hipotética dentro da frase do comando; antes, item 86. Ver seção 5 |
| BQ-0071 | pf_25 106_PF_004 | 88 | OK | OK (vazio) | idem |
| BQ-0072 | pf_25_adm 094_PF_CB1 | 22 | OK | OK (vazio) | "―" (U+2015) conforme o caderno; a situação ("Suponha que…") está no próprio item; antes, item 19, de outro grupo com texto-base |
| BQ-0075 | pf_25_adm 094_PF_CB1 | 32 | OK | OK (vazio) | grupo de 28; topo da p3 col1, depois de "Espaço livre" |
| BQ-0082 | pf_25_adm 094_PF_CB2 | 49 | OK | OK (vazio) | grupo de 46; antes, item 45 |
| BQ-0084 | fub_25 088_FUB_CB2 | 30 | OK | OK (vazio) | grupo de 26; antes, item 25 |
| BQ-0088 | fub_25 088_FUB_CB2 | 36 | OK | OK (vazio) | antes, item 35 |
| BQ-0093 | CAMARA2012 CAMDEP12_CB1 | 41 | OK | OK (vazio) | topo da p5 col2; antes, item 40 |
| BQ-0098 | dataprev_23 893_DATAPREV_003 | 92 | OK | OK (vazio) | grupo de 91; antes, item 90 |
| BQ-0106 | cti_23 922_MCTI_RENATO_ARCHER_006 | 97 | OK | OK (vazio) | grupo de 86, cruzando a coluna; o comando seguinte começa no 98 |
| BQ-0109 | CTI_23 922_MCTI_RENATO_ARCHER_CG1 | 38 | OK | OK (vazio) | grupo de 36; antes, item 35 |
| BQ-0112 | trf6_24 034_TRF6_012 | 53 | OK | OK (vazio) | situação dentro da frase do comando, logo depois do título da prova. Ver seção 5 |

Resultado da amostra: 32/32 com comando OK e 32/32 com texto_base OK.

**Varredura de texto-base omitido (atenção especial).**
- Despejei, para cada um dos 50 grupos de comando do banco, as 14 linhas anteriores ao comando no PDF (s4/qa_t29/ctx.txt). Isso cobre as 112 linhas, não só a amostra.
- Em 47 grupos, o que precede o comando é o último item do grupo anterior, um título de seção, o cabeçalho de página, "Espaço livre" ou a caixa de instruções (ANTT). Nenhum desses é texto-base.
- O único grupo com texto, situação ou quadro antes do comando é o de BQ-0049..0051, já preenchido.
- Procurei também, nos 19 cadernos, os marcadores "precedente", "Com base nessas informações", "texto precedente", "quadro" e "Texto CB…". Todos os blocos encontrados regem itens que não estão no banco:
  - TRF6 002, itens 51 e seguintes (probabilidades I–III) e 110 e seguintes (tabela TABCIDADES);
  - ANATEL, itens 51–65 (distribuições e estimadores);
  - SUSEP, itens 73–75 (esquema SINISTRO/APOLICE) e o grupo de .gitlab-ci.yml;
  - CNJ, itens 55–56 (código PHP) e 111–112 (firewall);
  - Embrapa 026, item 96 e seguintes (quadro de talhões);
  - PF 004, itens 65–66 (situação do firmware);
  - PF CB1, os grupos do texto e do email (Língua Portuguesa e Redação Oficial), item 15 e seguintes (proposição P) e 18 e seguintes (levantamento prisional).
- Não há "Texto CB1A1" nem quadro que reja item do banco.
- **Ids afetados por omissão de texto-base: nenhum.** O vazio em 109/112 está correto.

## 4. Achados

| # | Gravidade | Objeto | Achado | Evidência | Correção proposta |
|---|---|---|---|---|---|
| R-1 | forma (não bloqueia) | banco/SCHEMA.md, parágrafo de texto_base | "(o pacote exporta o vazio como "nenhum")" descreve só a v1.1. A F2 da v1.2 (D-T12-V12; regras/pacote_contrato.md, Regras da v1.2, (b)) manda exportar `""`. Lida sem data, a frase pode induzir a T-48 a emitir "nenhum" | SCHEMA.md: "Vazio quando o item não tem texto-base próprio (o pacote exporta o vazio como "nenhum")."; pacote_contrato.md: "Quando o item não tem texto-base, `textoBase` é `""` (string vazia), não `"nenhum"` (F2)." | Texto exato na seção 6 |
| O-1 | observação de método (sem correção) | relatório de produção, (d) | Para BQ-0067..0112 a conferência por script da produção comparou o comando com o segmento "comando:" de observacoes, que é uma fonte interna. A conferência contra o caderno ficou só na extração da própria produção | relatório, seção 4 (d) | Nenhuma. Esta conferência independente contra o PDF supre a lacuna: 46/46 OK, incluindo 0070, 0071 e 0112 |

Nenhum achado em banco/banco.csv. **Valor a gravar no banco: nenhum.**

## 5. (c) Convenção de BQ-0070, 0071 e 0112 (situação hipotética dentro do comando)

**Fidelidade: fiel ao caderno.**
- PF 004, antes do item 87: é um único parágrafo na margem, uma só frase, sem texto separado: "Considerando que, em uma rede local interna, um computador use o IP 192.168.1.10 e que a rede local acessa a Internet usando o IP 203.0.113.12 público, julgue os itens subsecutivos."
- TRF6 012, antes do item 51: também uma só frase, logo depois do título da prova: "Julgue os itens a seguir, considerando que, em certo tribunal regional, a duração de 1.000 processos encerrados nos últimos dois anos variou entre dois e sessenta meses, com quartis, para os dados levantados, iguais a 12, 18 e 24 meses."
- O texto_comando gravado é literal nas três linhas.
- Não existe, no caderno, um bloco de texto-base distinto que pudesse ir para texto_base. Bem diferente é o caso de BQ-0049..0051, em que a situação vem em parágrafo próprio e o comando remete a ela ("A partir da situação hipotética precedente").

**Recomendação à GBQ (sem decidir): MANTER.** Motivos:
1. Pôr a situação em texto_base obrigaria a cortar uma frase do caderno no meio. Sobraria um comando truncado ("…, julgue os itens subsecutivos.") ou seria preciso redigir um texto novo, contra a regra de literalidade e o "Nada de texto novo" da regra 3 do contrato.
2. A regra do SCHEMA já é objetiva: texto_base é o bloco que precede o comando e ao qual ele remete. A cláusula do SCHEMA para a situação dentro da frase cobre exatamente esses três casos.
3. A mesma regra serve a itens futuros como o do CNJ 111–112 ("Considerando que uma rede local tenha um firewall…"), se entrarem.

**Cautela para a T-48 (D1-c, comandos normalizados com campo comandoOriginal).**
- Nessas três linhas a premissa de que o item depende está no comando: a média dos quartis 12/18/24 e os IPs 192.168.1.10 e 203.0.113.12.
- A normalização não pode reduzi-las a "Julgue os itens a seguir." Isso tornaria os itens 87, 88 e 53 injulgáveis.
- Sugestão: a gbq-cqe conferir na T-48 que, em BQ-0070, 0071 e 0112, o comando exibido ao estudante preserva a situação inteira, ou que a plataforma mostra o comandoOriginal.

## 6. (d) banco/SCHEMA.md

- A lista de colunas, com 17 nomes na ordem do arquivo, confere com o cabeçalho real.
- A descrição de texto_comando confere com o conteúdo: literal, hifenização de quebra de linha desfeita, espaços normalizados, situação dentro da frase mantida e obrigatória inclusive nas anuladas (6/6 preenchidas).
- A descrição de texto_base confere: preenchido em 3/112 (BQ-0049..0051) e vazio quando não há texto-base próprio. A convenção "[tabela: ...]" ainda não foi exercida, o que está correto: nenhum item do banco depende de quadro.
- Única divergência: R-1.

**Correção exata proposta para R-1** (substituir só o parêntese, sem tocar o resto da linha):

- de: `Vazio quando o item não tem texto-base próprio (o pacote exporta o vazio como "nenhum").`
- para: `Vazio quando o item não tem texto-base próprio (o pacote v1.1/v1.1.1 exporta o vazio como "nenhum"; a partir da v1.2, como "" — F2, D-T12-V12).`

## 7. Rastreabilidade

- Cadernos: 19 PDFs baixados em 2026-10-13 de cdn.cebraspe.org.br (URLs = url_caderno do banco; lista em s4/qa_t29/urls.txt), em scratchpad s4/qa_t29/pdfs/. O tamanho e o sha256 conferem com o relatório de produção.
- Scripts: s4/qa_t29/scripts/a.py (colunas e formato), ext.py (extração por coluna com recuo), ctx.py (contexto anterior a cada um dos 50 comandos), c.py (reconstrução literal do comando, 112 linhas).
- Saídas intermediárias: s4/qa_t29/ctx.txt e c_res.json.
- Nenhum espelho de terceiros foi consultado. Não houve commit nem alteração de outro arquivo do repositório.
