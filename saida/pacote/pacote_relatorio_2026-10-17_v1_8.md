# pacote_relatorio_2026-10-17_v1_8.md — T-81 — 2026-10-17 — gerado por gbq-csc

REMETENTE: gbq-csc (produção, sonnet), executando a D1 da GBQ (`saida/pacote/T81_D1_escopo_v1_8_2026-10-17.md`; D-T12-V13; D-T81-RESPOSTA, Fundador, opção A).
DESTINATÁRIO: gbq-cqe (fidelidade, com leitura própria); depois gbq-gerencia (reconciliação e gatilho A). Cópia: orquestrador. Sem commit (do orquestrador).

## 1. Arquivos de saída: SHA-256 e bytes (conteúdo LF)

| Arquivo | Bytes | SHA-256 | Esperado pela D1 | Confere |
|---|---|---|---|---|
| `pacote.json` v1.8 (`out/`) | 621907 | `09d4a457612781275659a3f7fbfd3a182f20fd9d4003e5ba38007d0c26c7a9c0` | 621907 bytes, `09d4a457612781275659a3f7fbfd3a182f20fd9d4003e5ba38007d0c26c7a9c0` (seção 1.3 e 8) | sim |
| `pacote_estudante.json` v1.8-E (`out/`) | 602815 | `851e2370a9f5e9c8e5db725ff84777f70c12f81044983d339434ac7504e04c3e` | (sem valor fixado na D1) | — |
| `regras/pacote_contrato.md` v1.2.5 | 35460 | `10eac696dbb83049ba12ee793ff4991a1884094b7b88cdaf39f10a3fcc33660e` | 35460 bytes, 154 linhas, `10eac696dbb83049ba12ee793ff4991a1884094b7b88cdaf39f10a3fcc33660e` (seção 8, CONTRATO-V125) | sim |
| manifesto ordenado da edição v1.8 (SHA-256 das linhas "<sha256>  <nome>"; 34 arquivos) | — | `0b7391fa0178488924de8e6ed420c6108dd5fdad0e10fd1c5ccc40d9cd4bae6c` | v1.7: `67d2bdf85925a232…` (43 arquivos) | — |

No disco do Windows os arquivos do repositório têm CRLF (core.autocrlf); todo SHA-256 deste relatório é do conteúdo LF, como manda a D1 (P1).

## 2. Diff `pacote.json` v1.7 (git `62ab128`, `f20216c2…`) → v1.8 (D1, 1.3)

| Caminho | Antes (v1.7) | Depois (v1.8) |
|---|---|---|
| `.geradoEm` | `2026-10-14` | `2026-10-17` |
| `.nome` | `Câmara 2026 — pacote F4 (v1.7)` | `Câmara 2026 — pacote F4 (v1.8)` |

Exatamente 2 caminhos, `$.nome` e `$.geradoEm`; nenhuma chave entra, sai ou muda de lugar. O arquivo de dados completo mantém os 10 lotes, inclusive L1C, L4C e L5C (D1, 3.5). E13 e T-54 já aplicadas (F4 e F5 da T81_exequibilidade): não se mexe nelas (a E13 está no comando da D1 e da D2; o curso do L3 traz "que se possa afirmar").

## 3. `pacote_estudante.json`: deleções por regra e por campo (D1, 2.2)

Total: **709 remoções** em 36 regras; 1265 campos comparados (cada um é subsequência da origem, salvo as exceções fechadas CAIXA, REALINHA e a fusão do L1); CAIXA 8/8 e REALINHA 2/2, exatamente 1 cada.

Por campo (categoria de campo; escopo das regras = nome de arquivo de origem da v1.7):

| Campo | Campos alterados | Remoções |
|---|---|---|
| `lotes[].resumo` | 6 | 35 |
| `lotes[].curso` | 8 | 341 |
| `lotes[].pares[].a` | 0 | 0 |
| `lotes[].pares[].b` | 0 | 0 |
| `lotes[].pares[].como` | 3 | 3 |
| `lotes[].pegadinhas[].rotulo` | 0 | 0 |
| `lotes[].pegadinhas[].texto` | 32 | 32 |
| `itens[].nota` | 1 | 1 |
| `itens[].justificativa (AUTORAL)` | 75 | 105 |
| `itens[].url (AUTORAL)` | 180 | 180 |
| `simulados[SIM-0].avisos[0]` | 1 | 1 |
| `discursivas[].comando` | 0 | 0 |
| `discursivas[].padrao` | 3 | 11 |
| `discursivas[].aspectos[].texto` | 0 | 0 |
| `discursivas[].quesitos[].nome` | 0 | 0 |
| `discursivas[].quesitos[].conceitos[]` | 0 | 0 |

Por regra:

| Regra | Ocorrências |
|---|---|
| url AUTORAL (valor inteiro apagado) | 180 |
| F (parêntese) | 83 |
| V | 55 |
| F (prosa: referência a fonte) | 51 |
| F (fim de parêntese) | 48 |
| código de fonte do L5 (U/GG/TB) | 33 |
| F (frase "Fonte(s): …") | 30 |
| F (parêntese com verificação) | 26 |
| F (colchete) | 25 |
| agente/unidade interna (CQFP, QA, GCB, GCE, CPP) | 25 |
| NORMATIVO — QA | 18 |
| código N do L2/L3 | 14 |
| F (fim de parêntese, após vírgula) | 13 |
| F (início de parêntese) | 13 |
| NORMATIVO — QA (prefixo da base legal) | 13 |
| F ("Conforme a Fn (leitura …):") | 11 |
| id interno (R-xx, E-xx, O-xx, D-xx) | 10 |
| F (frase de fonte) | 9 |
| carimbo de leitura "aberta(s) hoje" | 9 |
| caixa (minúscula → maiúscula na inicial deixada por deleção) | 8 |
| carimbo datado de verificação/leitura (ligado a F-ref) | 7 |
| F (parêntese com seção/verificação) | 5 |
| carimbo "Verificado em 8/10/2026" (L5) | 4 |
| classificação interna de VOLÁTIL na justificativa | 3 |
| F (fim de parêntese, "com Fn") | 2 |
| V (parcial: mantém a orientação ao estudante) | 2 |
| id interno / versão do lote (v2) | 2 |
| marca de processo de produção do lote ("Nesta produção" / "a especificação previa") | 2 |
| D-ADERENCIA no aviso do SIM-0 (deleção literal única) | 1 |
| F (fim de parêntese, após travessão) | 1 |
| F (início de parêntese, antes de aspas) | 1 |
| F (parêntese com leitura) | 1 |
| NORMATIVO — QA (frase de marca e fontes) | 1 |
| NORMATIVO — QA (parcial: mantém a orientação ao estudante) | 1 |
| id de decisão na nota (D-LEI-15352) | 1 |
| marca de processo ("neste chat") | 1 |

## 4. Varredura R (D1, 2.3 e 2.4): conteúdo (X), dúvida (Y) e termos fora da lista

Lista X (exceções de CONTEÚDO, fechada; caminhos com índice base 0; a gbq-csc não acrescenta entrada):

| # | Campo | Contexto literal | Casamento | Esperado | Real |
|---|---|---|---|---|---|
| X1 | `itens[BQ-0040].comando` | `da Presidência do CNJ` | ampliada | 1 | 1 |
| X2 | `itens[BQ-0064].enunciado` | `O ChatGPT e o DeepSeek` | modelo | 1 | 1 |
| X3 | `lotes[L2].curso` | `da Presidência), orientação de bancada` | ampliada | 1 | 1 |
| X4 | `lotes[L3].curso` | `(órgão da Presidência da` | ampliada | 1 | 1 |
| X5 | `lotes[L3].curso` | `ANPD como órgão da Presidência (redação superada)` | ampliada | 1 | 1 |
| X6 | `lotes[L3].pares[20].b` | `órgão da Presidência (redação superada)` | ampliada | 1 | 1 |
| X7 | `lotes[L3].pegadinhas[25].texto` | `ANPD como órgão da Presidência (redação superada)` | ampliada | 1 | 1 |
| X8 | `lotes[L6A].curso` | `A tecla F4, com a referência` | Fn | 1 | 1 |

Y1, **DÚVIDA** (não tocada):

| # | Campo | Contexto literal | Casamento | Esperado | Real | Motivo |
|---|---|---|---|---|---|---|
| Y1 | `itens[L4-11].justificativa` | `O F4 afirma que` | Fn | 1 | 1 | Remover a referência de fonte exige reescrever a frase (D-T81-05). Fica literal e vai a este relatório como DÚVIDA, para errata da GCB se ela quiser. |

Casamentos de R no `pacote_estudante.json` (caminho, rótulo, casamento, destino): 9; de processo: 0.

- `itens[BQ-0040].comando` | ampliada | `Presidência` | **X1** | …21, n.º 335/2020 e n.º 332/2020 da Presidência do CNJ, julgue os itens a seguir.…
- `itens[BQ-0064].enunciado` | modelo | `ChatGPT` | **X2** | …O ChatGPT e o DeepSeek são plataformas de IA…
- `itens[L4-11].justificativa` | Fn | `F4` | **Y1** | …ioritariamente supervisionado"). O F4 afirma que "generative models are …
- `lotes[L2].curso` | ampliada | `Presidência` | **X3** | … Presidente (ou no exercício↵   da Presidência), orientação de bancada, pela orde…
- `lotes[L3].curso` | ampliada | `Presidência` | **X4** | … ela. A redação anterior (órgão da Presidência da↵   República) está SUPERADA.↵ -…
- `lotes[L3].curso` | ampliada | `Presidência` | **X5** | …↵superada). (6) ANPD como órgão da Presidência (redação superada), ou↵"a autorida…
- `lotes[L3].pares[20].b` | ampliada | `Presidência` | **X6** | …rquia vinculada ao MJSP); órgão da Presidência (redação superada)…
- `lotes[L3].pegadinhas[25].texto` | ampliada | `Presidência` | **X7** | …ANPD como órgão da Presidência (redação superada), ou "a autorida…
- `lotes[L6A].curso` | Fn | `F4` | **X8** | …B2) ou só a linha (B$2).↵- A tecla F4, com a referência selecionada na b…

Termos fora da lista (ficam como estão; só contagem, sem ação): "Presidente" 15, "Projeto" 188, "OpenAI" 31, "Anthropic" 6, "Gemini" 3, "GPT" 5, "Whisper" 21, "insumo" 2.

Na edição v1.8 (`out/estudante/`) a mesma varredura deve dar exatamente 11 casamentos (X1 2, X2 2, X3, X4 a X7 no `L3_estudo.md`, X8, Y1): ver a conferência (7) abaixo.

## 5. Fusão 1-C/4-C/5-C (D1, 3): contagem de itens por lote

| Lote | antes (v1.7) | depois (v1.8-E) | esperado pela D1 (3.4) |
|---|---|---|---|
| L1 | 20 (+ L1C 10) | 30 | 20 (+ L1C 10) → 30 |
| L4 | 20 (+ L4C 10) | 30 | 20 (+ L4C 10) → 30 |
| L5 | 20 (+ L5C 10) | 30 | 20 (+ L5C 10) → 30 |
| L2 | 30 | 30 | 30 → 30 |
| L3 | 30 | 30 | 30 → 30 |
| L6A | 15 | 15 | 15 → 15 |
| L6B | 15 | 15 | 15 → 15 |
| Total AUTORAL / banco | 180 / 106 | 180 / 106 | 180 / 106 |

Fusão no JSON: `lotes` = L1, L2, L3, L4, L5, L6A, L6B; `L1.curso` = curso do L1 + `\n\n## Complemento\n\n` + curso do 1-C; `L1.pegadinhas` = as 19 do L1 + as 4 do 1-C; L4C e L5C têm curso, resumo, pares e pegadinhas vazios (nada a fundir); associação do item ao lote pelo prefixo (`L1C-` → L1, `4C-` → L4, `5C-` → L5) registrada no contrato v1.2.5, ponto 3. Edição: 34 arquivos (43 na v1.7), com 9 retirados e 8 alterados.

**Nota (consequência registrada, não DÚVIDA — D1, 3.1):** a `legendaMecanismo` do L5C ("Mecanismo: troca de conceito (TC), generalização indevida (G…") não tem lugar no L5, que já tem a sua ("Mecanismos: TC troca de conceito; GI generalização indevida;…"). Os códigos são os mesmos (TC, GI, AT, IC) nas duas redações. A legenda do L4C é igual à do L4 (sim) e a do L5C também. Os `*_gabarito.md` da edição passam a trazer só a legenda do próprio lote; os `SIM-*_gabarito.md` não mudam.

## 6. E13, T-54 e T-69

- E13 e T-54: **já aplicadas** (F4 e F5 da `T81_exequibilidade_2026-10-17.md`); a v1.8 não mexe nelas. Conferido no pacote v1.8: o comando da D1 e o da D2 trazem "de até 20 linhas" (2 ocorrências), 0 do texto antigo; o curso do L3 traz "que se possa afirmar" (0 "que eu possa afirmar").
- T-69 (4): **feita**. `validate.py` termina com `sys.exit(1 if fails else 0)` depois do `json.dump`; continuam 118 verificações (nenhuma nova, nenhuma retirada). Teste negativo em `conferencias_v18.py`: sobre uma cópia do pacote com 1 gabarito trocado, o código de saída é 1.
- T-69 (2): **NÃO admitida; continua BACKLOG** (D1, 5). O item é do validador mantido `saida/treino/ferramentas/validar_erros.py` (`220dd559…`), que fica fora do gerador.

## 7. Divergências entre o escopo de lote e o escopo de simulado de uma mesma justificativa (6.2 (5); só registro)

Resultado

Contagem na edição v1.7 aceita: ver o texto da conferência: "0". Lista: (nenhuma). O JSON segue o escopo de lote, como manda a D1.

## 8. Registro P8: plataforma v1.7 × `pacote_estudante.json` (D1, 0 e 7; fora do escopo desta tarefa)

A plataforma v1.7 (`saida/plataforma/plataforma_v1_7.html`; **não tocada**) lê `pacote.json`. A associação item→lote vem de uma tabela fixa no HTML (`LOTE_INFO`: presente; prefixos `L1C-`: presente, `4C-`: presente, `5C-`: presente) e os lotes de cada módulo estão fixos (`lotes:["L6A","L6B","L4","L4C","L5","L5C"]`: presente; `["L1","L1C","L2","L3"]`: presente). Se ela ler o `pacote_estudante.json` sem adaptação, os itens dos complementos ficam fora dos testes de lote. Fica como registro para o rito do Fundador (D1, seção 7); nenhuma alteração de `saida/plataforma/` foi feita, nenhum artefato foi republicado, nada foi entregue à candidata.

## 8b. Adendo 1 da D1 (seção 9) e adaptações da produtora

- **Adendo 1 (D1 complementar da GBQ, 17/10/2026, seção 9):** o commit 73e9d49 (T-78, D-DA-BANCO) acrescentou o sufixo literal `; mapeamento adicional: ver banco/mapeamento_adicional.csv (D-DA-BANCO)` à `observacoes` de 20 linhas do banco; dos itens com `nota`, só o BQ-0003 o recebeu, e `banco.nota_de` (do rótulo "nota de vigência:" ao fim da célula) o levava à `nota`. Decisão: o sufixo é nota de PROCESSO e não entra em `nota` (regra 4 da v1.1.1; SCHEMA.md linha 7). Correção só no gerador: `banco.py` (`SUF_MAPA` e `nota_de`, com assert), `validate.py` (verificação da `nota` sobre `observacoes` sem o sufixo; continuam 118) e a conferência de não regressão do banco em `conferencias_v18.py`. `banco/` não foi alterado.
- **Defeito latente da v1_7 (registro, sem ação na v1_7):** o `gerador_v1_7`, intacto, rodado sobre o banco atual exportaria na nota do BQ-0003 o sufixo (a `nota_de` da v1_7 devolveria 327 caracteres terminando em "co/mapeamento_adicional.csv (D-DA-BANCO)", e a v1_7 não tem o tratamento do sufixo). A v1.8 não tem esse efeito: a nota do BQ-0003 no pacote v1.8 é igual a a da v1.7.
- **X5, X6 e X7 contados juntos na edição (aceito, 9.5 (a)):** nos campos do JSON os caminhos são distintos e as contagens são individuais; na edição o contexto de X6 é substring do de X5 e do de X7 e os três caem em `L3_estudo.md`; vale o grupo {X5, X6, X7} = 3, com a localização conferida (1 no bloco do curso, 1 em "## Pares", 1 em "## Pegadinhas"; X4 1 no curso; total 11). Linhas da edição com o grupo:
  - `L3_estudo.md:338`: …a por ela. A redação anterior (órgão da Presidência da…
  - `L3_estudo.md:363`: …superada). (6) ANPD como órgão da Presidência (redação superada), ou…
  - `L3_estudo.md:559`: …(autarquia vinculada ao MJSP); órgão da Presidência (redação superada)**.…
  - `L3_estudo.md:595`: …transcrição e IA** — ANPD como órgão da Presidência (redação superada), ou "a autoridade nacional é …
- **Substituição da reconstrução acumulada (aceito, 9.5 (b); altera a 6.2 (1)):** a reconstrução da edição v1.3 → v1.8 e os testes T54-x foram substituídos pela conferência v1.7 → v1.8 (diff fechado da 3.3 com reconstrução). Fundamento: transitividade; a v1.7 é canônica (D-PACOTE-V17, com aquela reconstrução e aqueles testes aprovados pela gbq-cqe na T-71) e a v1.8 é a v1.7 com 2 trocas conferidas byte a byte (pacote) e o diff fechado da 3.3 (edição). A conferência (0) confere a base: `git show 62ab128:saida/pacote/pacote.json` = `f20216c2…` e a edição desse commit com manifesto ordenado `67d2bdf85925a232…`. O diff acumulado do pacote v1.3 → v1.8 e o histórico do pacote foram mantidos.
- Registro do contrafactual (banco de `62ab128` sobreposto ao HEAD, feito antes do Adendo, só diagnóstico): `pacote_estudante.json` `851e2370…` (602815 bytes) e manifesto da edição `0b7391fa01784889…`; com a correção da 9.3 a regeração sobre o banco atual deve reproduzi-los (conferido: sim).

## 9. Resultados das seções 6.1 a 6.4 da D1

**6.1 `estudante_json.py`** (asserções (a) a (f)): 0 falhas.

**6.2 `conferencias_v18.py`:** 214 conferências; 0 falhas.

| Grupo | OK | FALHA |
|---|---|---|
| BASE | 6 | 0 |
| (1) T-64 | 2 | 0 |
| (0) DIFF v1.7->v1.8 | 7 | 0 |
| (1) HIST v1.6->v1.7 | 5 | 0 |
| (1) HIST E13 | 1 | 0 |
| (1) HIST v1.5->v1.6 | 7 | 0 |
| (1) DIFF | 11 | 0 |
| (2) CONTRATO v1.2.5 | 8 | 0 |
| (3) EDIÇÃO v1.7->v1.8 | 17 | 0 |
| (4) IDENT json | 13 | 0 |
| (5) JSON×ED v1.7 | 7 | 0 |
| (6) JSON×ED v1.8 | 5 | 0 |
| (7) VARREDURA R json | 1 | 0 |
| (7) VARREDURA R edição | 3 | 0 |
| (7) CONTAGEM | 1 | 0 |
| (4) VARR 3.5 | 15 | 0 |
| (4) VARR 3.5 extra | 19 | 0 |
| (4) QA T-56 | 6 | 0 |
| (4) CAIXA C-05 | 2 | 0 |
| (4) CAIXA C-15 | 9 | 0 |
| (4) REUNIÃO C-06 | 1 | 0 |
| (4) REUNIÃO C-07 | 1 | 0 |
| (4) REUNIÃO C-08 | 1 | 0 |
| (4) REUNIÃO | 2 | 0 |
| (4) C-13 | 1 | 0 |
| (4) C-18 | 1 | 0 |
| (4) C-10 | 1 | 0 |
| (4) C-11 | 1 | 0 |
| (4) T57 s3-6 | 1 | 0 |
| (5) CONT | 20 | 0 |
| (6) T-59 | 9 | 0 |
| (6) T-66 | 5 | 0 |
| (7) E13 | 3 | 0 |
| (8) GERADOR | 6 | 0 |
| (8) BANCO Adendo 1 | 2 | 0 |
| (8) T-69 (4) | 2 | 0 |
| (8) ESTUDANTE_JSON | 2 | 0 |
| (9) MUTAÇÕES | 10 | 0 |

**Verificações (`validate.py`, 118):** 118 verificações; 0 falhas.

**Fidelidade (`estudante_fidelidade.py`, com a fusão):** 5765 comparações; 0 diferenças; 2 marcas residuais (as 2 esperadas: L4_gabarito.md:58 = Y1 e L6A_estudo.md:83 = X8).

**Mutações da fidelidade (`fidelidade_mutacao.py`):** 14 mutações, 259 diferenças detectadas, todas detectadas: True.

**6.3 pipeline** (`rodar_tudo.sh`, 11 passos, `set -e`, determinismo: `geradoEm` literal, nenhuma leitura de data, hora ou HEAD): saídas-padrão em `out/*_stdout.txt`.
- `out/gen_stdout.txt`: 1 F (parêntese com leitura)
- `out/estudante_json_stdout.txt`: 0 falhas
- `out/fidelidade_stdout.txt`:    ('L6A_estudo.md', 83, 'F4', '- A tecla F4, com a referência selecionada na barra ')
- `out/sync_stdout.txt`: RESULTADO: TUDO OK
- `out/validate_stdout.txt`: 118 verificações; 0 falhas
- `out/conferencias_stdout.txt`: 214 conferências; 0 falhas
- `out/mutacao_stdout.txt`: {"mutacoes": 14, "arquivos_mutados": ["BANCO_gabarito.md", "DISCURSIVAS.md", "DISCURSIVAS_padrao.md", "L1_estudo.md", "L1_itens.md", "L2_estudo.md", "L2_gabarito.md", "L3_estudo.md", "L4_estudo.md", "
- `out/validar_erros_stdout.txt`: 12 conferências; 0 falhas

**6.4 conferência (f)** (regeração em 2 cópias limpas):

| Cópia | cwd | PYTHONHASHSEED | arquivos em `out/` (original / cópia) | idênticos | diferenças de nome |
|---|---|---|---|---|---|
| cópia 1 | `raiz da cópia 1 (scratchpad/cf/cA)` | 7 | 65 / 65 | 65 | nenhuma |
| cópia 2 | `/tmp` | 4242 | 65 / 65 | 65 | nenhuma |

Resultado: **65 de 65 arquivos de `out/` idênticos byte a byte nas duas cópias** (inclui `pacote.json`, `pacote_estudante.json`, `estudante/` com 34 arquivos e o relatório); nenhuma diferença de nome; o `MANIFESTO.md` regerado pelo passo 11 em cada cópia é igual, byte a byte, ao desta pasta na primeira passagem (com o registro provisório); em ambas, 214 conferências, 118 verificações, 14 mutações da fidelidade detectadas, 8 mutações do JSON detectadas e 12 conferências do teste do registro, 0 falhas. As cópias são clones limpos do HEAD (com o `banco/banco.csv` do HEAD, T-78) e foram rodadas com `PYTHONHASHSEED` e pastas diferentes das do original. Depois de gravado este registro definitivo, o pipeline rodou de novo no original (segunda passagem: `out/` igual ao da primeira, exceto o relatório e `relatorio_stdout.txt`, que citam este registro) e numa terceira cópia limpa (`PYTHONHASHSEED` 99, a partir de /tmp), com `out/` (65/65) e `MANIFESTO.md` iguais, byte a byte, aos do original. Os scripts temporários da ocorrência não são necessários para regenerar: só `gerador_v1_8/` e o que já está no git. No Windows, a execução usou um shim de ambiente (LF na escrita de texto e UTF-8 nos filhos), fora do repositório.

## 10. DÚVIDAS e divergências frente à especificação

DÚVIDA 1 (D1, 2.4, Y1): `itens[L4-11].justificativa` contém "O F4 afirma que"; remover a referência de fonte exige reescrever a frase (D-T81-05). Fica literal no JSON e na edição (`L4_gabarito.md:58`). Para errata da GCB, se ela quiser; não é falha.

Nenhuma divergência: todos os valores esperados da D1 conferem (pacote.json `09d4a457…`, 621907 bytes; contrato `10eac696…`; 9 casamentos de R no JSON e 11 na edição, 0 de processo; 8/8 mutações detectadas).

