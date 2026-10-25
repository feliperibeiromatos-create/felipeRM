# T129_reconciliacao_2026-10-25.md — T-129 — 2026-10-25 — gerado por gbq-gerencia

Objeto: reconciliação e D1 da onda 1 de Direito Administrativo (ordens/ORDEM_BANCO_DA_CDN_ONDA1.md; Gerência titular GCB, GBQ em cópia; a GBQ governa banco/banco.csv). Ciclo 2026-10-25 s19c1. Sem commit. DECISOES.md não foi tocado.

Entregas reconciliadas:
- Produção gbq-cfp (sonnet): saida/banco/onda1/banco_onda1_staging.csv (261 itens, BQ-0212..BQ-0472; SHA-256 a2371420d1392c8a7f90cc234ee6f9f1650c36d9f461c0098c215c793582d208, não alterado); saida/banco/reserva_DA.csv (142 linhas na entrega); saida/banco/varredura_DA_onda1_2026-10-25.md.
- QA gbq-cqe (opus): saida/banco/QA_onda1_DA_2026-10-25.md: 0 reprovados (0%, sem gate), 4 CORRIGIR, 11 com duas leituras, 6 linhas da reserva com duas leituras. Texto, número, comando, base e gabarito conferidos com caderno e definitivo do CDN em 261/261, e a reserva em 142/142.
- Reclassificação cega de mecanismo (opus, sem ver os códigos): saida/banco/onda1/reclassificacao_cega_100_2026-10-25.csv.

## 1. D1 — correções da QA (4/4 aceitas)

| id | decisão |
|---|---|
| BQ-0315 (TCU CE 87) | ACEITA: VOLÁTIL-NORMATIVO e aderência direta → parcial. Base provável na IN SEGES/MPDG 5/2017, mesmo bloco do BQ-0316. Volta a direta sem VOLÁTIL se o qa-normativo-da achar a regra na Lei 14.133 ou em decreto vigente (T-144) |
| BQ-0376 (TRF6 C24 71) | ACEITA: parcial → direta (P1-DA-7). O comando é de improbidade, e a Lei 8.730/1993 não é necessária para julgar. Conferência da LIA na T-144 |
| BQ-0443 (PF CB2 38) | ACEITA: parcial → direta (P1-DA-7), pelo mesmo fundamento |
| BQ-0389 (TCE-RS CE1 65) | ACEITA: subitem 10.7 → 10.5 em observacoes. item_edital_camara continua P1-DA-10 |

## 2. D1 — duas leituras (11 itens)

Critério geral, o mesmo do BQ-0281 já na produção: o item é parcial quando o gabarito depende de decreto, instrução normativa ou regime de estatal (Lei 13.303), e não da lei do edital. O comando sozinho não decide. Decide o conhecimento exigido para julgar o item.

| id | decisão | fundamento |
|---|---|---|
| BQ-0472 (FUNPRESP CE1 58) | Leitura B: RETIRADO para a reserva. Id não reutilizado | O comando é "Em relação à Lei n.º 13.303/2016", tema FORA pela regra e)5. Assim fica coerente com as linhas da Embrapa Ana 57 e 58, que continuam na reserva. O item só seria parcial, ou seja, só diagnóstico. Como é o último id do staging, a fusão fica contígua (BQ-0212..BQ-0471) |
| BQ-0410 (Embrapa C18 63) | Leitura B: direta → parcial | O DFD vem do decreto do PCA, e a prova é de estatal |
| BQ-0413 (Embrapa C18 66) | Leitura B: direta → parcial | A revisão do PCA é regra do decreto do PCA, e a prova é de estatal |
| BQ-0412 (Embrapa C18 65) | Enquadramento P1-DA-11 → P1-DA-10 (10.5). Fica parcial | O conhecimento julgado é a publicidade do PCA, e não a LAI. Continua parcial pelo mesmo bloco de estatal e decreto do PCA |
| BQ-0288 (TRT10 C14 81) | Leitura A: parcial, mantida | Critérios dos órgãos de controle. Controle é tema FORA, e o 10.5 só tangencia |
| BQ-0366 (Embrapa CE065 68) | Leitura A: parcial, mantida | A prova é de estatal (regime da Lei 13.303 e RLCC). Fracionamento conceitual, sem a 14.133 como base certa |
| BQ-0278 (TRT10 C14 105) | Leitura B: parcial → direta (10.1) | A ordem das fases (propostas, julgamento, habilitação) é a da Lei 14.133. O comando cita o decreto, mas o gabarito não depende dele. Conferência na T-144 |
| BQ-0296 (TCU CE 115) | Leitura A: direta, mantida (2.1) | O conhecimento julgado é o efeito ex tunc da anulação ("nulidades"), e não o controle jurisdicional |
| BQ-0305 (TCU CE 110) | Leitura A: direta, mantida (2.1) | Autotutela, anulação e revogação: texto do 2.1 |
| BQ-0317 (TCU CE 89) | Leitura B por precaução: direta → parcial + VOLÁTIL-NORMATIVO | Mesmo bloco do BQ-0318 (VOL, IN 5/2017). Reverte se a T-144 achar a regra na Lei 14.133 |
| BQ-0265 (STM C8 105) | Leitura A: direta, sem VOL, mantida | O dever do fiscal de levar ao superior o que excede sua competência é, na leitura da GBQ, regra da própria Lei 14.133 [SEM FONTE — conferir na T-144]. Se a base for a IN 5/2017 ou o Decreto 11.246/2022, passa a parcial + VOL. Até lá fica fora de simulado final (seção 6) |

## 3. D1 — reserva (6 linhas com duas leituras): todas na leitura A (ficam na reserva)

- Linhas 102–103 (Embrapa Ana 57/58): ficam. É coerente com a retirada do BQ-0472.
- Linha 53 (TRT10 101, IN 65/2021): fica. O prazo do parâmetro depende da IN.
- Linha 60 (TCU 109, controle administrativo): fica, porque controle é FORA. A autotutela já está coberta pelo BQ-0305.
- Linha 122 (TCE-RS OCE 63, requisição de bens): fica. O 3.3 "Requisição" está sob "Agentes públicos", ou seja, é requisição de pessoal.
- Linha 0 (FUB 92, fontes do DA): fica. O 4.1 trata das fontes do direito disciplinar. Reabrir como parcial em 4.1 é possível numa onda futura, com staging e QA próprios.
- Reserva depois: 143 linhas (142 + BQ-0472, com motivo e a nota de id retirado). SHA-256 ddc5b02188e6536fed90cb7cd2fc315ae7e0e83b654bed58be46ca1352ffdfe7.

## 4. Mecanismo — concordância e D1 dos 13 discordantes

- Concordância cega 87/100 no código principal e 91/100 com o alternativo. Está acima do piso de 80% (ordem e.8; ESTILO §7). A tabela de mecanismos não volta à Presidência.
- O D1 seguiu as definições da seção 4 de regras/estilo_banca_DA_v1.md:
  - Adotado o código cego em 9: BQ-0223 AP→LIT (paráfrase do CF art. 41, § 2º, sem narrativa); BQ-0250 AP→CON (afastamento no lugar de aproveitamento); BQ-0270 SUP→NEG (inverte a tese do STF); BQ-0281 PRA→CON (fase trocada); BQ-0304 GEN→NEG ("não alcança", sem absolutizador); BQ-0327 GEN→SUP ("independentemente de dolo" suprime requisito); BQ-0404 AP→LIT (tese em paráfrase); BQ-0407 SUP→TEM (marco de eficácia); BQ-0439 PRA→LIT (item C com prazo correto é paráfrase fiel).
  - Mantido o da produção em 4: BQ-0332 SUP ("sem formular juízo" suprime a proposta de decisão; o alternativo cego é SUP); BQ-0388 NEG ("vedado" no lugar de "admitido"; o alternativo cego é NEG); BQ-0421 AUT (destinatário do recurso trocado); BQ-0427 GEN ("um único índice"; o alternativo cego é GEN).
  - Registro em observacoes: "mecanismo=<adotado> (D1 GBQ T-129: …; produção <X>)" ou "D1 GBQ T-129: mecanismo da produção mantido". Os 161 fora da amostra ficam como a produção.
- Distribuição final (260): LIT 109, CON 33, SUP 25, NEG 25, AP 22, GEN 14, PRA 12, AMB 8, AUT 7, TEM 5.

## 5. Fusão em banco/banco.csv

- Antes: SHA-256 da9b0f14941478d553c7c2221a0f1b9cc37e431ba992a223202f9537cb07cc8f (250.537 bytes; 212 linhas = cabeçalho + BQ-0001..BQ-0211, incluídas as BQ-0153..0211 da T-128, ainda sem aceite).
- Depois: SHA-256 a539452cf978147829a4c11dd820fee029c0047a0ab69cf2c4e06a63947bb206 (581.127 bytes; 472 linhas = cabeçalho + BQ-0001..BQ-0471).
- Provas (script python -I, scratchpad t129/aplica.py):
  - o arquivo novo começa byte a byte com o arquivo anterior. `git diff --numstat` dá 319 inserções e 0 remoções (59 da T-128 + 260 da T-129);
  - cabeçalho de 18 campos inalterado, CRLF, UTF-8;
  - ida e volta csv do staging idêntica em 261/261 antes da edição;
  - ids contíguos BQ-0212..BQ-0471.
- "QA PENDENTE" → "QA APROVADO gbq-cqe 2026-10-25 (T-129)" em 260/260. O único "QA PENDENTE" que resta no banco é o do BQ-0141 (T-79, anterior, não tocado).
- Onda fundida: 260 itens, 126 C / 134 E, 0 X; aderência 235 direta / 25 parcial; 18 VOLÁTIL-NORMATIVO. Por nível: P1-DA-10 115, P1-DA-4 34, P1-DA-3 29, P1-DA-7 22, P1-DA-6 15, P1-DA-1 14, P1-DA-2 12, P1-DA-11 10, P1-DA-5 9.

## 6. VOLÁTIL e conferência normativa (T-144, PRÓXIMO, qa-normativo-da)

- 18 VOLÁTIL-NORMATIVO mantidos ou acrescentados: os 16 da produção + BQ-0315 + BQ-0317. Ficam inaptos a simulado final até 4–8/1/2027.
- A conferência normativa que o QA não fez (o planalto não respondeu) foi aberta em TAREFAS.md como T-144, com 80 ids em seis listas (a–f): IN 5/2017, PCA/fases/fiscal, LIA, Lei 8.112, 14.133 com valor ou prazo, STF. Nenhum item da onda depende da LGPD.
- D1 de montagem: até a T-144 concluir, nenhum dos 80 entra em simulado final.
- Aptos a simulado final hoje: 176 diretas não VOL fora das listas (84 C / 92 E). Diagnóstico: 25 parciais.

## 7. Metas ≥ 30 reais por item do edital (reais = CEBRASPE_OFICIAL + ANALOGA, sem X; "antes" inclui a T-128 pendente de aceite; entre parênteses, só direta)

| Grupo | antes | + onda 1 | depois | depois (direta) | meta 30 |
|---|---|---|---|---|---|
| 1.1 | 2 (2) | 4 | 6 | 6 | faltam 24 |
| 1.2 | 9 (9) | 10 | 19 | 18 | faltam 11 (12 diretas) |
| 2 | 6 (6) | 12 | 18 | 18 | faltam 12 |
| 3 sem 3.4 | 5 (3) | 18 | 23 | 21 | faltam 7 (9) |
| 3.4 | 6 (6) | 11 | 17 | 17 | faltam 13 |
| 4.1–4.3 | 1 (1) | 9 | 10 | 10 | (3.4 + 4.1–4.3 = 27: faltam 3) |
| 4.4 | 6 (6) | 25 | 31 | 31 | ATINGIDA |
| 5 | 3 (3) | 9 | 12 | 12 | faltam 18 |
| 6 | 2 (2) | 15 | 17 | 17 | faltam 13 |
| 7 | 5 (5) | 22 | 27 | 27 | faltam 3 |
| 8 / 9 / 12 | 8 / 6 / 7 | 0 | 8 / 6 / 7 | 6 / 5 / 7 | sem meta nesta ordem |
| 10 | 24 (24) | 115 | 139 | 115 | ATINGIDA |
| 11 | 6 (6) | 10 | 16 | 16 | sem meta nesta ordem |

Diferenças em relação à varredura da produção: 1.2 −1 (BQ-0472 retirado); 7 direta 25 → 27 (BQ-0376 e BQ-0443); 10 +1 e 11 −1 (BQ-0412). A direta do 10 fica em 115, com 18 VOL todos em 10. Metas da ordem: 10 e 4.4 atingidas. Ficam abaixo 7 (−3), 3.4/4 (−3 na leitura conjunta), 1.2 (−11) e, entre os "quanto falta", 1.1 (24), 2 (12), 3 (7), 5 (18) e 6 (13).

## 8. Ondas 2+ (ordens já em ordens/)

- ONDA2 (T-135, ordens/ORDEM_BANCO_DA_CDN_ONDA2.md): provas 16–40, cerca de 365 candidatos C/E em 25 provas.
- ONDA3 (T-139, ordens/ORDEM_BANCO_DA_CDN_ONDA3.md): provas 41–110, cerca de 339 candidatos C/E em 70 provas (17 a reconferir).
- Estimativa da GBQ: pela taxa da onda 1 sem as provas de regulamento interno (cerca de 70% incorporados), algo como 230–260 itens na onda 2 e 210–240 na onda 3. É estimativa, não contagem.
- Prioridade de cobertura: 1.1, 5, 2, 6, 3.4 e 1.2.
- O gasto das ondas 2+ é PRÓXIMO e depende de novo "sim" do Fundador (ordem, alínea g). As ordens não são executadas por esta reconciliação.

## 9. T-143 (omitidos do cd_25_ns)

Ids a partir de BQ-0473. A onda 1 foi gravada até BQ-0471, e o BQ-0472 está retirado e não pode ser reutilizado. A T-143 está desbloqueada em TAREFAS.md (PRÓXIMO, PENDENTE).

## 10. Gatilho

GATILHO A da GBQ acrescentado em PARA_PRESIDENCIA.md, depois dos gatilhos da T-128 e da T-134. A onda 1 não depende do aceite da T-128: os ids e os itens são independentes. Nada vai ao pacote nem à plataforma sem gatilho A próprio e o "sim" do Fundador (ordem, e.9).
