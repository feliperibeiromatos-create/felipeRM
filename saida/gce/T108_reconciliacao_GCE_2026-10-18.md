# T-108 — Reconciliação da GCE (lotes 1, 1-C, 2, 3 e discursivas D1–D5) — 2026-10-18 — gerado por GCE (gce-gerencia, ciclo s14)

Base: saida/gce/QA_T108_R1_2026-10-18_gce-cqfp.md; saida/gce/QA_T108_R2_2026-10-18_gce-cqfp.md (R2: 12/12 APROVADO, ressalva O1); saida/gce/T108_D1_GCE_2026-10-18.md; saida/gce/T108_D1_pos_R1_GCE_2026-10-18.md; saida/gce/T108_substituicoes_GCE_v2.csv (SHA-256 c4a29f1bf21721a1d2ec52517462f56c4fae8fca8cbf2c517875200c87f07fe7); saida/pacote/T108_ocorrencias.csv; pacote.json v1.10 (SHA-256 LF d43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed; bruto 58e73632091fad60bcea796dab96c9512c86cf8bfbe752b7ac5f209fc2ffff0c); D-V15-ENCOMENDA; D-V15-C-M2.

Natureza: D1. Nada aqui muda enunciado, gabarito, itemEdital, aderência, gênero de peça ou rótulo. A ressalva O1 entra como errata de forma idêntica às já aprovadas GCE-0265 a 0267, sem nova rodada de QA (limite de 2 rodadas atingido; precedente D1 pós-R2 da T-78): a conferência é por script da GCE (seção 3).

## 1. Decisão D1 pós-R2 sobre a ressalva O1

"HIPÓTESE do Projeto" em discursivas[D1].padrao e [D2].padrao entra como errata, forma fixa da D1 pós-R1 §4 ("do Projeto" → "deste material"; rótulo HIPÓTESE mantido). Conferido por script (somente leitura, python -I) sobre o pacote.json v1.10: "do Projeto" ocorre uma única vez em cada campo; nenhuma das 269 linhas da v2 toca esses dois campos (sem sobreposição); no pacote inteiro, depois de aplicadas as 271 linhas, não resta "do Projeto" (as demais ocorrências, em D3, D4 e D5, já estão cobertas pela v2).

Linhas novas da v3 (entram no fim, nessa ordem; `⏎` é quebra de linha LF real dentro do campo e não se escreve; `fonte_origem` vazia):

| id_edicao | ids_ocorrencia | caminho | lote | categoria | antes | depois | acao | regra | nota |
|---|---|---|---|---|---|---|---|---|---|
| GCE-0270 | NAO_INVENTARIADA-12 | discursivas[D1].padrao | DISCURSIVA | C07 | `são HIPÓTESE⏎do Projeto:` | `são HIPÓTESE⏎deste material:` | SUBSTITUIR | 5 | `D1 pós-R2 (O1 do QA R2); forma de GCE-0265 a 0267; rótulo HIPÓTESE mantido` |
| GCE-0271 | NAO_INVENTARIADA-13 | discursivas[D2].padrao | DISCURSIVA | C07 | `é HIPÓTESE do Projeto,` | `é HIPÓTESE deste material,` | SUBSTITUIR | 5 | `D1 pós-R2 (O1 do QA R2); forma de GCE-0265 a 0267; rótulo HIPÓTESE mantido` |

Frases resultantes: D1 "…mais 0,70 de apresentação são HIPÓTESE⏎deste material: os padrões oficiais publicam os conceitos…"; D2 "O peso de cada⏎quesito é HIPÓTESE deste material, alinhado à soma oficial." Concordância igual à aprovada em D3.

## 2. Arquivo final da tabela

- Arquivo final: saida/gce/T108_substituicoes_GCE_v3.csv (a produzir pela gce-cpp, T-108-GCE-P3): 271 registros = 269 da v2 byte a byte + GCE-0270 e GCE-0271.
- SHA-256 esperado (v3 simulada pela GCE com o mesmo escritor da v1/v2: UTF-8, vírgula, aspas mínimas, fim de registro CRLF, LF dentro do campo): 77ad3ac331ec120c6fb086c0b3f7c05cb77776c1e06b3dcaa6df2ab1d52fc599.
- Base aprovada no QA: v2, SHA-256 c4a29f1bf21721a1d2ec52517462f56c4fae8fca8cbf2c517875200c87f07fe7.
- Aceite: a v3 vale só se o script da seção 3 passar sem falha e o SHA-256 do arquivo entregue for igual ao esperado. Se falhar, vale a v2 e GCE-0270/0271 passam a pendência da GCE para a GBQ aplicar na consolidação (sem mudança no gatilho A além do arquivo).

## 3. Conferência por script da GCE (sem R3)

Script: saida/gce/T108_conferir_v3_GCE.py (somente leitura, python -I). Uso: `python -I saida/gce/T108_conferir_v3_GCE.py saida/gce/T108_substituicoes_GCE_v2.csv saida/gce/T108_substituicoes_GCE_v3.csv saida/pacote/pacote.json`. Verifica: SHA da v2 e do pacote (LF); (a) 272 registros brutos (cabeçalho + 271); (b) os 270 primeiros registros (cabeçalho + 269) iguais byte a byte à v2; (c) GCE-0270/0271 no fim, com os 11 campos exatos da seção 1; sem CR em `antes`/`depois`; `antes` das duas com 1 ocorrência no campo; (d) sobreposição 0 nas 271; (e) aplicação sequencial sem falha e resíduo 0 ("do Projeto", "não afirmar", "Inapto a simulado", "costuma(m) ser cobrad") nos campos tocados; HIPÓTESE intacto em D1/D2; imprime o SHA da v3.

Ensaio sobre a v3 simulada (2026-10-18): todas as verificações OK; 123 campos tocados; 0 falhas; 0 resíduos; SHA 77ad3ac3…c599. Resultado sobre o arquivo entregue (2026-10-18, saida/gce/T108_substituicoes_GCE_v3.csv): SHA v2 OK; (a) 272 registros brutos OK; (b) 270 primeiros iguais à v2 byte a byte OK; (c) GCE-0270/0271 no fim com campos exatos OK; sem CR OK; SHA pacote LF OK; (d) sobreposição 0 OK; (e) aplicação sem falhas OK; resíduo 0 OK; HIPÓTESE intacto em D1 e D2 OK; 123 campos tocados; 0 falhas. SHA-256 da v3 entregue: 77ad3ac331ec120c6fb086c0b3f7c05cb77776c1e06b3dcaa6df2ab1d52fc599, igual ao esperado. CONFERIDA: a v3 é o arquivo final aceito pela GCE; a alternativa v2 da seção 2 fica sem efeito.

## 4. Contagens finais

### 4.1 Inventário da GBQ (saida/pacote/T108_ocorrencias.csv, pacote.json, gerência GCE): 323 ocorrências

| lote | PROCESSO | VERIFICAR | FP-R1 | FP-CONTEUDO | total | cobertas pela tabela | resíduo PROCESSO+VERIFICAR |
|---|---|---|---|---|---|---|---|
| 1 | 90 | 0 | 12 | 0 | 102 | 90 | 0 |
| 1-C | 7 | 0 | 0 | 0 | 7 | 7 | 0 |
| 2 | 117 | 7 | 3 | 3 | 130 | 124 | 0 |
| 3 | 67 | 0 | 0 | 0 | 67 | 67 | 0 |
| DISCURSIVA | 5 | 0 | 12 | 0 | 17 | 5 | 0 |
| total | 286 | 7 | 27 | 3 | 323 | 293 | 0 |

Cobertas por categoria (293): C01 14; C02 16; C04 115; C05 18; C07 7; C08 4; C09 2; C10 117. Cobertas por lote × categoria: L1 C04 59, C10 31; L1-C C04 4, C08 1, C09 2; L2 C01 10, C02 15, C04 18, C05 9, C07 1, C08 2, C10 69; L3 C01 4, C02 1, C04 34, C05 9, C07 2, C10 17; DISCURSIVA C07 4, C08 1.

Fora da tabela (30), todos falsos positivos do inventário: 27 FP-R1 (regra 1, "lote" técnico; 15 no escopo da ordem, 12 em campos extras: 12 em D1/D2, 12 no L1, 3 no L2) e 3 FP-CONTEUDO no L2 (D-C08-093f788f lotes[L2].curso e D-C08-1809cbcc itens[L2-R43].justificativa, "produção" no sentido técnico do conteúdo; D-C08-01f0b795 itens[L2-R19].justificativa, "Errata" como seção de documento oficial). Os 3 FP-CONTEUDO não são marca de processo (classificação do próprio inventário) e ficam como estão. Meta cumprida: zero marca de processo remanescente, salvo falsos positivos.

Além do inventário: NAO_INVENTARIADA-01 a -13 e o E3 (dentro de GCE-0098), todos cobertos.

### 4.2 Tabela v3: 271 linhas

| lote | linhas |
|---|---|
| 1 | 88 |
| 1-C | 7 |
| 2 | 107 |
| 3 | 56 |
| DISCURSIVA | 13 |

Por ação: SUBSTITUIR 186; DELETAR 85. Por categoria da linha: C04 111; C10 93; C07 15; C02 13; C05 12; C01 12; C08 3; C09 2; C04;C05 3; C05;C10 3; C01;C02 1; C08;C10 1; C02;C10 1; C04;C10 1.

## 5. Tabela de Correções (T-108, GCE)

| rodada | linhas | resultado | destino |
|---|---|---|---|
| R1 | 263 | 260 APROVADO, 3 CORRIGIR, 1 faltante | GCE-0094, 0105, 0154 corrigidas; GCE-0264 nova (D1 pós-R1 §1) |
| D1 pós-R1 | recomendações R1–R5 | aceitas (R3 em redação própria) | GCE-0205, 0218, 0235 corrigidas; GCE-0265 a 0269 novas |
| R2 | 12 | 12 APROVADO, ressalva O1 | v2 aceita (SHA c4a29f1b…7fe7) |
| D1 pós-R2 | O1 | errata de forma idêntica | GCE-0270, 0271 (v3, conferência por script, sem R3) |

Pendências da GCE na T-108: nenhuma, salvo a entrega e a conferência da v3 (seção 3).

## 6. Para a GBQ (D1 dela; a GCE só informa)

1. Acrescentar ao inventário os ids sem registro no T108_ocorrencias.csv, todos cobertos pela tabela:

| id | caminho | categoria | linha GCE |
|---|---|---|---|
| NAO_INVENTARIADA-01 | lotes[L2].curso | C05 | GCE-0110 |
| NAO_INVENTARIADA-02 | lotes[L3].curso | C01 | GCE-0238 |
| NAO_INVENTARIADA-03 | discursivas[D4].padrao | C07 | GCE-0260 |
| NAO_INVENTARIADA-04 | discursivas[D4].padrao | C07 | GCE-0261 |
| NAO_INVENTARIADA-05 | discursivas[D5].padrao | C07 | GCE-0263 |
| NAO_INVENTARIADA-06 | itens[L2-R18].justificativa | C10 | GCE-0264 |
| NAO_INVENTARIADA-07 | discursivas[D3].padrao | C07 | GCE-0265 |
| NAO_INVENTARIADA-08 | discursivas[D4].padrao | C07 | GCE-0266 |
| NAO_INVENTARIADA-09 | discursivas[D5].padrao | C07 | GCE-0267 |
| NAO_INVENTARIADA-10 | lotes[L3].curso | C10 | GCE-0268 |
| NAO_INVENTARIADA-11 | lotes[L3].curso | C10 | GCE-0269 |
| NAO_INVENTARIADA-12 | discursivas[D1].padrao | C07 | GCE-0270 (v3) |
| NAO_INVENTARIADA-13 | discursivas[D2].padrao | C07 | GCE-0271 (v3) |
| E3 (sem id próprio) | lotes[L2].resumo | C05 | GCE-0098 (dentro de D-C05-43ed5a69) |

2. Acrescentar à varredura os padrões "do Projeto", "não afirmar", "Inapto a simulado" e "costuma(m) ser cobrad".
3. Restrição de simulado do L2-R18: "inapto a simulado final até a reverificação de 4–8/1/2027; se a página mudar o número antes de janeiro, reescrever o item sem o limite" sai do texto da candidata por GCE-0264, mas, pela D-V15-C-M2, vai ao campo interno do item e continua valendo para o gbq-csc. O campo `volatil` fica como está.
4. A tabela cobre o pacote.json. A GCE não verificou o pacote_estudante.json (fora do objeto). Se ele não for derivado do pacote.json limpo, a GBQ confere nele as mesmas 271 linhas.
5. Os 30 falsos positivos (seção 4.1) ficam no texto. Os 3 FP-CONTEUDO não pedem edição.
