# T128_reconciliacao_2026-10-25.md — T-128 — 2026-10-25 — gerado por gbq-gerencia

Objeto: reconciliação e D1 da GBQ sobre a T-128 (ordens/ORDEM_CD2026_LOCALIZAR.md; Gerência titular pela ordem: GCB, GBQ em cópia; em TAREFAS.md a unidade é GBQ). Ciclo s19c1.
Entradas: produção gbq-cfp (banco/banco.csv BQ-0153..BQ-0211; saida/banco/cd25ns_DA_2026-10-25.md); QA gbq-cqe, Opus (saida/banco/QA_cd25ns_DA_2026-10-25.md). Produção (sonnet) e QA (opus) em modelos distintos; a GBQ não produziu nem revisou item.
Regras aplicadas: D-ROTULOS, D-ANO, D-ADERENCIA, D-QA-PENDENTE, D-MC, D-ESCOPO-3, D-BANCO-LOCALIZADOR, D-ESPEC-DA-V2-1 (`mecanismo`), regras/estilo_banca_DA_v1.md §4.

## 1. Reconciliação produção × QA

- Cobertura da QA: 59/59 (100%). Reprovados 0 (0%; sem GATE). Corrigir 3 (só o código de mecanismo em observacoes). Texto, número, comando, texto-base, gabarito (30 C / 28 E / 1 X, = definitivos), anulado (só BQ-0190, E2 98, X conferido com as justificativas de 15/04/2026), rótulo CEBRASPE_OFICIAL (cd_25_ns = certame-alvo), URLs, datas e item_edital: sem divergência.
- Fontes: 7 PDFs oficiais em cdn.cebraspe.org.br/concursos/cd_25_ns/arquivos/, abertos pela produção e de novo pela QA (HTTP 200; SHA-256 na seção 1 do relatório da QA). Nenhuma fonte de terceiro usada para texto ou gabarito.
- Ressalva de método aceita: a concordância de mecanismo (54/58 = 93,1%) não foi totalmente cega. A GBQ não pede reclassificação agora: o mecanismo não altera texto nem gabarito, só alimenta o diagnóstico D30, que está em BACKLOG (D-D18-D30, ≥ 60 itens com `mecanismo` por matéria). Fica registrado para a T-141.

## 2. D1 da GBQ

### 2.1 Mecanismo (tipologia do guia; competência GBQ)

| id | item | produção | QA | D1 | motivo |
|---|---|---|---|---|---|
| BQ-0189 | E2 97 | SUP | NEG | **NEG** | CF, art. 38, IV: o tempo "será contado para todos os efeitos legais"; o item diz "não podendo ser computado". Direção invertida (§4: NEG). |
| BQ-0192 | E2 126 | CON | NEG | **NEG** | STF: a contratada emergencial "não está impedida"; o item diz "estará impedida". Direção invertida, sem conceito vizinho trocado. |
| BQ-0208 | E2 142 | SUP | CON | **CON** | Lei 14.133, art. 121, § 2º: solidária (previdenciários) × subsidiária (trabalhistas); o requisito "falha na fiscalização" está no item. Troca de conceito vizinho. |
| BQ-0204 | E2 138 | TEM | NEG (sem proposta) | **NEG** | Lei 14.133, art. 131: a extinção "não configurará óbice"; o item diz "prejudica". O erro está na polaridade, não no marco temporal; mesmo critério dos três acima. Leitura TEM registrada em observacoes. |

Em cada linha, observacoes passou a "mecanismo=<D1> (D1 gbq-gerencia T-128; leitura da produção: <anterior>)".

### 2.2 Aderência (D-ADERENCIA; competência GBQ)

| id | item | registrada | D1 | motivo |
|---|---|---|---|---|
| BQ-0174 | CG 69 | parcial | **parcial (mantida)** | Metade do juízo é sobre o Estado do bem-estar (universalização de direitos), que não está no item 8 do edital; só as disfunções da burocracia são P1-DA-8. Fica só para simulado diagnóstico. |
| BQ-0176 | CG 71 | parcial | **direta** | Controle social na execução orçamentária = participação cidadã (P1-DA-8.3, literal); o erro do item está justamente no alcance da participação. |
| BQ-0183 | CG 85 | parcial | **direta** | Conferências, conselhos e orçamento participativo são as instâncias de participação cidadã (P1-DA-8.3). |
| BQ-0184 | CG 88 | parcial | **direta** | Conselhos de políticas públicas institucionalizam a participação da sociedade civil (P1-DA-8.3). |

Mantidas como parciais (QA: justificáveis; GBQ concorda): BQ-0175 (accountability, 8.3 só por tema), BQ-0182 (9.1 por tema), BQ-0187 e BQ-0188 (STF sobre membros do MP/Judiciário; 3.1 por extensão). BQ-0165: mapeamento adicional P1-DA-10.4 só registrado; item_edital segue P1-DA-6.
Resultado nas 59: 54 direta / 5 parcial (antes 51 / 8).

### 2.3 Omitidos e discutíveis (decisão; a GBQ não cria nem grava item)

| caderno / item | gab. def. (QA) | D1 | mapa provisório | aderência provisória |
|---|---|---|---|---|
| CG 72 | E | **INCLUIR** | P1-DA-8 (reforma gerencial / NPM, literal no caput do item 8) | direta |
| CG 73 | C | **INCLUIR** | P1-DA-8 (gestão por resultados como traço da NPM) | direta, a confirmar pela QA |
| E2 95 | C | **INCLUIR** | P1-DA-3.1 (CF, art. 37, VII, com a jurisprudência do STF) | direta, a confirmar pela QA (trata de servidor público, não de membro de Poder, diferente de E1 107/110) |
| CG 68 | C | **INCLUIR SE** a gbq-cfp, lendo o caderno, confirmar que o item gira em torno da sustação de ato normativo que exorbita do poder regulamentar (CF, art. 49, V) → P1-DA-5.1/5.2, parcial; se for só controle legislativo externo, **FORA** | P1-DA-5.1 | parcial |
| E1 123 | C | **FORA** | — | Controle externo (registro de aposentadoria pelo TCU) não está nos 12 itens de DA; a leitura por 2.1 (ato complexo) ou 3.1 é extensão. Leitura da QA registrada. |
| E1 139 | C | **FORA** | — | Apetite ao risco é do bloco de governança corporativa (E1 139–143); o item 9 do edital é governança pública (Decreto 9.203). |

Critério: o relatório da produção excluiu CG 72–73 como "outras disciplinas", mas o item 8 do edital nomeia a nova gestão pública; a exclusão era incoerente com a inclusão de CG 69–71 (QA, §5). Demais exclusões do §4 da produção confirmadas pela QA e pela GBQ.
Encaminhamento: tarefa nova T-143 (PRÓXIMO) — gbq-cfp incorpora CG 72, CG 73, E2 95 e, condicional, CG 68, do caderno e do gabarito definitivo do CDN (URLs já listadas na seção 1 da QA), com "QA PENDENTE"; QA gbq-cqe confere 100%; GBQ reconcilia. Ids atribuídos só depois da onda 1 (T-129 grava em staging com ids a partir de BQ-0212); nada foi escrito nesse intervalo.

## 3. Aplicado em banco/banco.csv (só linhas BQ-0153..BQ-0211)

- 59 linhas: "QA PENDENTE" → "QA APROVADO gbq-cqe 2026-10-25 (T-128)" (inclui BQ-0190, anulado: aprovado como registro, segue fora de simulado pelo X).
- 4 linhas, mecanismo (seção 2.1): BQ-0189, BQ-0192, BQ-0204, BQ-0208.
- 3 linhas, aderência parcial → direta na coluna aderencia e em observacoes (seção 2.2): BQ-0176, BQ-0183, BQ-0184.
- Linhas BQ-0001..BQ-0152 byte a byte intactas (diff conferido); 212 linhas (cabeçalho + 211), 18 campos em todas, CRLF preservado. Única "QA PENDENTE" remanescente no banco: BQ-0141 (D-BQ0141-REVERIFICAR).
- SHA-256 do banco: antes 5c95e2b7c8bb2028b13f77f205535c10ff5dfd47292b403be15f56adc6e14275; depois da9b0f14941478d553c7c2221a0f1b9cc37e431ba992a223202f9537cb07cc8f.

Contagens finais das 59 (BQ-0153..0211): gabarito 30 C / 28 E / 1 X; aderência 54 direta / 5 parcial; mecanismo LIT 28, CON 9, NEG 8, GEN 5, AP 5, AMB 2, SUP 1, indeterminado 1 (anulado); por item do edital: P1-DA-1 7, 2 3, 3 7, 4 3, 6 1, 7 2, 8 7, 9 4, 10 20, 11 2, 12 3 = 59 (contado por script sobre item_edital_camara).

Aptidão a simulado: as 58 não anuladas ficam aptas a banco de treino; a simulado final só as 53 diretas não anuladas (nenhuma é VOLÁTIL). Pela D-ADERENCIA, as 5 parciais só em simulado diagnóstico. Nenhuma entra na plataforma antes do gatilho A.

## 4. Gatilhos e pendências

- GATILHO A (GBQ) em PARA_PRESIDENCIA.md: aceite canônico das 59 linhas CEBRASPE_OFICIAL.
- Nenhum ponto de mérito de conteúdo de DA da GCB ficou aberto (mecanismo e aderência são da GBQ). Para a GCB (cópia, titular da ordem): CG 72–73 (P1-DA-8) e E2 95 (P1-DA-3.1) vão entrar pela T-143.
- Pistas da ordem (cerca de 15 itens rotulados "Cebraspe – Câmara dos Deputados/2026" no curso de mercado): a cobertura está na seção 5 do relatório da produção; nenhum texto de terceiro entrou no banco.
- Linha proposta para o Estado Canônico (secretaria): "T-128 (s19c1): 59 itens de DA do cd_25_ns (BQ-0153..BQ-0211; CEBRASPE_OFICIAL; 30 C / 28 E / 1 X; 54 diretos / 5 parciais) com QA gbq-cqe APROVADO e D1 da GBQ; aceite canônico pendente de gatilho A; omitidos CG 72, CG 73, E2 95 (+ CG 68 condicional) na T-143."
