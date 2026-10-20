# fidelidade_v1_13_T118_R2_gbq-cqe.md — T-118 (R2 da fidelidade; D1 dos achados, seção 3) — 2026-10-20 — gerado por gbq-cqe

Reconferência R2 da fidelidade da v1.13, ciclo s15c1. Cobre só o que mudou depois da R1 (`saida/pacote/montagem_v1_13/fidelidade_v1_13_T118_gbq-cqe.md`, SHA-256 6c5f71f0…4ba4, inalterada). Base: `saida/pacote/T118_D1_achados_fidelidade_2026-10-20.md` (03bbe6b6…257b), seção 3, critérios R2-1 a R2-7. A gbq-cqe não produziu, corrigiu nem reconciliou nenhum objeto. Não alterei nenhum arquivo de produção e não fiz commit. Este relatório é o único arquivo que gravei no repositório, e ele fica fora de `montagem_v1_13/`, como pede a D1.

Método: script próprio `r2.py` (d2c3bd85…6198), rodado com `python3 -I`, só com leitura do repositório. Fica fora dele, em `/tmp/claude-0/-home-claude/72c49c1c-aa49-56a0-8236-2c7fd5868295/scratchpad/cqe_t118_r2/`. Os resultados brutos estão em `saida_r2.txt` e `res_r2.json`: 112 verificações OK e 0 FALHA. Extraí os anexos A a D da D1 e conferi o SHA-256 de cada um (e82a2e9b, 1ae66134, 9d0db657 e 6560b93a: os quatro OK). Usei o anexo A só como contraprova, porque a minha regra é mais estrita. O anexo B também deu 6/6 OK.

## 0. Veredito: ACEITO

| Critério | Objeto | Veredito |
|---|---|---|
| R2-1 | Contrato v1.2.11 (achado 1) | ACEITO |
| R2-2 | Edição .md × v1.2.11 | ACEITO |
| R2-3 | Adendo 5 regerado (achados 2, 3 e 4) | ACEITO. Ressalva no texto do critério (achado R2-B); o objeto está certo. |
| R2-4 | Scripts alterados | ACEITO |
| R2-5 | Achado 5 | ACEITO |
| R2-6 | MANIFESTO (achados 3 e 6) | ACEITO. **70 é o número correto**, e o 71 da D1 é erro do critério (achado R2-A). |
| R2-7 | Integridade | ACEITO |

Os achados 1 a 6 da R1 estão resolvidos. Os achados 7 e 8 eram INFO, sem ação. Nada mais bloqueia a reconciliação e o gatilho A (D1 da T-118, passo 4.6). A promoção é byte a byte e cabe ao orquestrador: `out/registro_adendo5.md` (a1ca1681…7437), os dois pacotes e `out/estudante/`.

## 1. R2-1: contrato v1.2.11. ACEITO

- `regras/pacote_contrato.md`: SHA-256 85b30fcc…616b, 72.183 bytes, 325 linhas LF e 0 CR.
- O blob de HEAD é 2626a946…28c1, com 68.699 bytes e 311 linhas. Os opcodes (`SequenceMatcher`, `autojunk=False`) são exatamente `replace 0–1`, `replace 2–3` e `insert 306–306 → 306–320`.
- A linha 1 só troca "(v1.2.10, 2026-10-20)" por "(v1.2.11, 2026-10-20)".
- A linha 3 é a linha 3 de HEAD, mais um espaço, mais a frase citada na seção 4 do registro (`contrato_v1_2_11_2026-10-20.md`, fa5f5f69…2e86).
- As 14 linhas inseridas são iguais ao texto entre as marcas da seção 4 do registro. Depois delas vêm a linha em branco e o `---`.
- O registro declara os valores de antes e de depois certos e cita literalmente o subitem que a errata substitui.

**Coerência com o ponto 4 da v1.2.10.** O último subitem do ponto 4 diz que os textos de `pares` e `pegadinhas` não levam `**`. Ele está intacto, e a errata o invoca como base do seu ponto 2. Não há contradição: o mesmo texto sai sem marcas no pacote, na plataforma e na .md.

**Coerência com o ponto 8 da v1.2.10.** O último subitem do ponto 8 ("não é gerada na v1.13 … `- **a** × **b** | como`") continua no texto, como nas erratas anteriores, que acrescentam e não reescrevem. A errata declara que o substitui (ponto 1) e que prevalece só para os lotes D1 a D6. A linha 3 remete à seção nova. Os demais subitens do ponto 8 (nome, `versao`, `geradoEm`, edital, lotes, tópicos, itens e `nucleo` do `pacote_estudante.json`) não são tocados.

**Mérito, por leitura.**
- A errata só trata da .md de DA.
- Não muda campo, `versao`, `versaoFormato` nem os pacotes (82c4117c… e 04cbd593…, conferidos no R2-7).
- Não contradiz o ponto 2 da v1.2.10 (registro de formato como conferência pacote × canônico).
- Não contradiz o ponto 9 (qualificação).
- Mantém o ponto 2 da v1.2.2 para os lotes L1 a L6B.

Há uma imprecisão de remissão, sem efeito: achado R2-C.

## 2. R2-2: edição .md × v1.2.11. ACEITO

- `out/estudante/` tem 53 arquivos. O digest das linhas "caminho TAB sha256", ordenadas pelo caminho relativo a `out/`, unidas por `\n` e com `\n` final, é c6ecc6e5…29a9, como na D1. Sem o `\n` final, o digest seria ea14bef6…7fe6, e a D1 não diz qual das duas formas usa.
- Fiz a implementação própria do ponto 2 da v1.2.11: seções delimitadas pelo próximo `## ` ou `# `, linhas não vazias, prefixo "- " e o resto igual à concatenação literal dos campos do `pacote_estudante.json`, na ordem do JSON. O resultado:

| Lote | Pares | Pegadinhas | `**` |
|---|---|---|---|
| lote D1 | 22/22 | 26/26 | 0 |
| lote D2 | 46/46 | 114/114 | 0 |
| lote D3 | 31/31 | 67/67 | 0 |
| lote D4 | 24/24 | 62/62 | 0 |
| lote D5 | 31/31 | 73/73 | 0 |
| lote D6 | 43/43 | 63/63 | 0 |
| Total | 197 | 405 | 0 |

A .md gerada cumpre a v1.2.11 sem regeração.

## 3. R2-3: adendo 5 regerado. ACEITO

- `out/registro_adendo5.md`: a1ca1681…7437, 11.582 bytes, 111 linhas LF e 0 CR.
- No diff linha a linha contra `historico/registro_adendo5_R1_7224db40.md`, as linhas trocadas são exatamente 10, 12, 26, 29–33, 38, 42 e 47–52, e as inseridas são 103–111. O resto é igual.
- As trocas, lidas uma a uma:
  - 10 e 12 corrigem a faixa;
  - 26, 29–33, 42 e 47–52 só acrescentam "lote "/"lotes " (a 26 e a 42 conferi por substituição exata);
  - 38 reescreve a frase com "nos lotes"/"No lote", e números e faixas não mudam.
- A seção 9 é igual byte a byte. Na seção 2, o título e a tabela (linhas 15–24) são iguais, e a linha 26 difere só pela qualificação "(lote D2)" e "(lote D6)" (achado R2-B).

**Seção 1.** Calculei a faixa pelo menor e pelo maior id numérico de cada lote no `out/pacote.json`. Também conferi que o intervalo menos os vagos da seção 4 dá exatamente os ids do pacote e que o n bate:

| Lote | Faixa no adendo | n | Vagos |
|---|---|---|---|
| lote D1 | D1-01 a D1-60 | 60 | 0 |
| lote D2 | D2-01 a D2-80 | 80 | 0 |
| lote D3 | D3-01 a D3-81 (sem os vagos da seção 4) | 71 | 10 |
| lote D4 | D4-01 a D4-79 | 79 | 0 |
| lote D5 | D5-01 a D5-71 (sem o vago da seção 4) | 70 | 1 |
| lote D6 | D6-01 a D6-50 | 50 | 0 |

O lote D5 traz o singular "sem o vago".

**Qualificação.** Usei uma regra própria, mais estrita que a do anexo A: a "D1" de decisão só fica isenta se vier seguida de " da GBQ", " da T-<n>" ou " própria". Ela dá 0 ids soltos no adendo. O anexo A também dá "NAO_QUALIFICADOS 0".

**Seção 10.**
- Os seis SHA-256 batem com o disco: 66c65194, a05e0def, 8e49aaa0, 8f7cc099, 77bb5787 e 7998cc7b. O do lote D6 é igual ao conferido pela gcb-cqfp (7998cc7b…90ca).
- As 7 remissões apontam para arquivos que existem, e a seção "## Errata de forma — T-118 (achado 10), 20/10/2026" existe no registro do lote D6 (linha 204).
- Não há nenhum enunciado: 0 prefixos de 60 caracteres dos 410 enunciados aparecem no adendo.
- As remissões da seção 6 continuam válidas (7).

## 4. R2-4: scripts alterados. ACEITO

Desfiz as trocas dos anexos em ordem inversa, com cada âncora nova ocorrendo uma única vez:
- anexo C (13 trocas): `registro_adendo_v113.py`, hoje 42b7025b…fa70, volta a dd7d9a0d…2b22;
- anexo D (10 trocas): `manifesto_v1_13.py`, hoje e06115ee…9f53, volta a 5f92b713…2ac0.

Só mudaram as trocas listadas.

## 5. R2-5: achado 5. ACEITO

- O adendo não existe mais em `saida/gbq/`. `git status --ignored --untracked-files=all` dá vazio em `saida/gbq/`, `saida/estudante/` e `saida/plataforma/`: a pasta `saida/gbq/` está igual a HEAD, e a cópia antecipada, que não estava versionada, não deixou rastro.
- `historico/registro_adendo5_R1_7224db40.md` tem 7224db40…5918 e 10.245 bytes. `historico/` contém só esse arquivo.
- Nada foi promovido: `saida/pacote/pacote.json` e `pacote_estudante.json` estão iguais a HEAD, e `saida/estudante/` e `saida/gbq/` não têm arquivo novo.

## 6. R2-6: MANIFESTO. ACEITO

O `MANIFESTO_v1_13.md` tem d56cb806…0403 e 19.501 bytes.

**Seção 3.** Lista 70 arquivos, iguais um a um, em bytes e SHA-256, ao conteúdo recursivo de `montagem_v1_13/`, sem o próprio manifesto e sem `__pycache__` (que não existe). Nada fica fora da pasta. A linha "Total" traz "70 arquivos … (dos quais 53 em out/estudante/). Nenhum arquivo fora desta pasta: …". Nenhum arquivo da pasta é mais novo que o manifesto.

**Por que 70, e não 71.** A contagem no disco dá 53 arquivos em `out/estudante/` e mais 17 arquivos:
- `QA_final_v1_13_v16_2026-10-20_gbq-cqe.md`, `cobertura_v1_13.py`, `conferir_t118.py`, `diag30_da.py`, `estudante_md_v113.py`, `fidelidade_v1_13_T118_gbq-cqe.md`, `manifesto_v1_13.py`, `montar_v1_13.py` e `registro_adendo_v113.py`;
- `historico/registro_adendo5_R1_7224db40.md`;
- `out/conferencia_t118.json`, `out/diag30_DA.json`, `out/estudante_md_v1_13.json`, `out/pacote.json`, `out/pacote_estudante.json`, `out/registro_adendo5.md` e `out/stats_v1_13_DA.json`.

O "71" da D1 vem do ensaio da gbq-gerencia (`scratchpad/ger_t118/sim2/MANIFESTO_v1_13.md`). O diff dele contra o manifesto real tem só duas diferenças:
- a linha `| saida/pacote/montagem_v1_13/run_manif.py | 11416 | 22460058… |`, um auxiliar do próprio ensaio que estava na cópia e que não existe no repositório;
- a linha "Total" (71 contra 70).

O erro é do critério, não do MANIFESTO (achado R2-A). O valor de referência de 19.621 bytes, que a D1 já dizia não ser critério, difere do real pelo mesmo motivo.

**Seção 1.** Tem 14 linhas, todas OK, entre elas as três novas, com o esperado igual ao obtido: adendo a1ca1681…, R1 7224db40… e contrato 85b30fcc….

**Seção 4.** Traz os seis `D<n>_registro_formato.md` e `regras/pacote_contrato.md`, com o SHA-256 igual ao disco. As demais entradas também batem, e o SHA-256 de DECISOES.md é igual ao do disco (3fd7bed9).

**Seção 5.**
- A obs. 6 cita a v1.2.11 e o registro `contrato_v1_2_11_2026-10-20.md`.
- A obs. 10 descreve as correções dos achados 2 a 6, com o `historico/`, `cobertura_v1_13.py` e `fidelidade_v1_13_T118_gbq-cqe.md`.
- Qualificação: o anexo A dá "NAO_QUALIFICADOS 0" a partir da linha 133. A minha regra estrita marca cinco "D1" nas linhas 134, 135, 137, 138 e 141 ("pela D1", "a D1", "A D1", "(D1, seção 2)"). Li uma a uma: todas são a decisão de Gerência, e nenhuma é id de lote. OK.

## 7. R2-7: integridade. ACEITO

| Arquivo | SHA-256 (igual à R1) |
|---|---|
| out/pacote.json | 82c4117c…f240 |
| out/pacote_estudante.json | 04cbd593…0c40 |
| out/stats_v1_13_DA.json | f077cb33…7320 |
| out/conferencia_t118.json | 6c5250c9…844f |
| out/diag30_DA.json | eb1ced6d…6800 |
| out/estudante_md_v1_13.json | ad7374dd…f5fa |
| montar_v1_13.py | 723370f5…1ebe |
| conferir_t118.py | 3fa09b7d…0768 |
| estudante_md_v113.py | 54faa3bf…c976 |
| cobertura_v1_13.py | 72a89f86…5312 |

Também conferi:
- os `D<n>_plataforma.json` e os `D<n>_registro_formato.md` dos lotes D1 a D5 são iguais a HEAD;
- `D6_plataforma.json` = f8691dd5… e `D6_registro_formato.md` = 7998cc7b…, os valores da R1;
- `edital_DA.json` é igual a HEAD;
- `saida/plataforma/` tem 4d19eb05… e c6de3f2a…;
- `git status` fora de `montagem_v1_13/` mostra só o que já estava na R1 (abertura do ciclo, errata do achado 10, montagem) e os três arquivos da gbq-gerencia (a D1 dos achados, o registro v1.2.11 e `regras/pacote_contrato.md`).

## 8. Achados da R2

| N.º | Gravidade | Objeto | Achado | Bloqueia? |
|---|---|---|---|---|
| R2-A | INFO | D1 dos achados, passo 6 e seção 1 (achado 6) | O critério "71 arquivos listados" está errado: contou `run_manif.py`, um auxiliar do ensaio no scratchpad `ger_t118/sim2/`. O número certo é 70, e o MANIFESTO e a devolução da gbq-csc estão corretos. | Não. A gbq-gerencia registra o 70 na reconciliação. |
| R2-B | INFO | D1 dos achados, preâmbulo e R2-3 | "As seções 2 e 9 são iguais byte a byte" contradiz a própria lista de linhas do diff: a linha 26 está na seção 2 e foi trocada pelo achado 3 ("(lote D2)", "(lote D6)"). Pela leitura certa, a tabela da seção 2 e a seção 9 são iguais, e a linha 26 muda só pela qualificação. É isso que está no disco. | Não. |
| R2-C | INFO | Errata v1.2.11, ponto 4 | A frase "Resumo, curso, tópicos, itens, gabaritos e `NUCLEO.md` continuam no ponto 6 da v1.2.9 e no ponto 8 da v1.2.10" remete mal. A regra do `NUCLEO.md` está no ponto 6 da v1.2.7 (linha 193). O ponto 8 da v1.2.10 não tem regra de .md além do subitem que a errata substitui. As regras dos itens e gabaritos .md estão em erratas anteriores, entre elas a v1.2.1 (ponto 1) e a v1.2.5 (ponto 4). O efeito ("nada mais muda") está certo, e a .md cumpre todas essas regras (R1, seção 6). | Não. Corrigir a remissão na próxima errata, se houver. |
| R2-D | INFO | D1 dos achados, R2-2 | O digest c6ecc6e5…29a9 pressupõe `\n` final após a última linha, e a D1 não fixa isso. Para os próximos critérios, convém fixar a forma. | Não. |

Nenhum achado bloqueia. **Veredito R2: ACEITO** (R2-1 a R2-7 OK).
