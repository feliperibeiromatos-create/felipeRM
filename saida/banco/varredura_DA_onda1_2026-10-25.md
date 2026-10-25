# varredura_DA_onda1_2026-10-25.md — T-129 — 2026-10-25 — gerado por gbq-cfp

Ordem: ordens/ORDEM_BANCO_DA_CDN_ONDA1.md (T-129, orquestrador BANCO). Fila: banco/candidatos/candidatos_DA_TEC2025_fila_v2.csv (a fila e o TEC são só localizadores; todo texto, número de item e comando vêm do caderno oficial; todo gabarito vem do GABARITO DEFINITIVO). Rótulo dos itens novos: CEBRASPE_ANALOGA. Todos os itens novos estão com "QA PENDENTE". Nada foi escrito em banco/banco.csv (staging em saida/banco/onda1/banco_onda1_staging.csv, ids BQ-0212 a BQ-0472); nada foi commitado.

## 1. Método e fontes
- Pasta de cada concurso e nomes de arquivo: API pública do próprio Cebraspe, https://apis.cebraspe.org.br/cebraspe/eventos/<código> (HTTP 200, JSON, campo arquivosGabarito; listagem do CDN dá 403). Cada PDF foi baixado direto de https://cdn.cebraspe.org.br/concursos/<código>/arquivos/<arquivo> (HTTP 200 em todos). Nenhum espelho de terceiro foi usado para texto ou gabarito. (Uma busca na web serviu só para descobrir o código do evento do TCU, tcu_25_tefc, e do PF administrativo, pf_25_adm; a confirmação foi pela API do Cebraspe.)
- Códigos de evento: fub_25, inoversasul_24, stm_25, trt10_24, tcu_25_tefc, anm_24, embrapa_24, trf6_24, tce_rs_25, icmbio_24, pf_25_adm, funpresp_24_exe (FUNPRESP-EXE APC no lugar de SEFAZ RJ AFP, que não tem item C/E: 21 itens de múltipla escolha, só insumo de pegadinha).
- Localização: texto do candidato comparado (normalizado: caixa, acentos preservados, pontuação, espaços e hifenização de quebra de linha desfeitos) ao texto extraído do caderno por pdftotext, restrito aos cadernos que servem ao cargo (caderno específico + caderno de conhecimentos básicos/gerais do cargo). Casamento exato do enunciado em 412 dos 414 candidatos; 2 casamentos aproximados (razão ≥ 0,88) por erro de digitação na fila (OCE item 65 do caderno 877A…: "reajustado valor" na fila; FUNPRESP item 75: "previsto projeto básico" na fila x "previsto no projeto básico" no caderno); nos dois o texto do banco é o do caderno.
- Gabarito: GABARITO DEFINITIVO do mesmo caderno (arquivo cuja descrição coincide com a do caderno), lido pelo bloco "Item/Gabarito" do PDF. Nenhum item dos 414 está anulado (X) no definitivo.
- Mecanismo: tabela da seção 4 de regras/estilo_banca_DA_v1.md; registrado em observacoes como "mecanismo=<código>"; é leitura desta execução, a conferir pela QA (reclassificação cega na seção 7). O banco.csv não tem coluna mecanismo; o schema não foi alterado.
- Enquadramento: item_edital_camara no nível P1-DA-n (convenção das linhas existentes); subitem literal do edital (ex.: 10.6) em observacoes ("edital da Câmara, item X.Y"). A coluna item_edital_wb da fila foi só ponto de partida e foi corrigida em dezenas de casos.
- Reserva (saida/banco/reserva_DA.csv): temas fora dos itens 1–12 do edital da Câmara (convênios, SRP, IN 65/2021, controle externo/judicial, Lei 12.846 e Decreto 11.129, Lei 13.303, concessões, bens públicos, fontes do DA) e normas internas de entidade (Regulamento da InoversaSul, RLCC da Embrapa, Regulamento da FUNPRESP-EXE, instrumento de padronização da Justiça do Trabalho). Cada linha traz o motivo. Nenhuma justificativa de enquadramento foi adotada para os temas FORA; o QA pode reabrir qualquer linha.
- VOLÁTIL-NORMATIVO: 16 itens apoiados na IN SEGES/MPOG 5/2017 (terceirização/fiscalização), cuja vigência não pôde ser reverificada nesta execução (portal planalto.gov.br inacessível a partir do ambiente); ficam fora de simulado final até a reverificação de 4–8/1/2027. Nenhum item de LGPD/ANPD (Lei 15.352/2026) nesta onda. Para os demais itens de Lei 14.133, Lei 8.112, Lei 8.429 e Lei 9.784, a conferência do texto vigente em 2026 é tarefa do qa-normativo-da (não foi feita aqui; sem fonte consultada, nada foi afirmado sobre alterações 2025–2026).

## 2. Resultado por prova

Colunas: cand = candidatos da fila; achados = encontrados no caderno com gabarito definitivo; incorp = incorporados ao staging; reserva = achados mas fora do edital; dup = já em banco/banco.csv (hash do texto normalizado); anul = anulados no definitivo; diverg = gabarito do definitivo difere do gabarito_tec da fila; não loc = não localizados.

| Prova | cand | achados | incorp | reserva | dup | anul | diverg | não loc |
|---|---|---|---|---|---|---|---|---|
| FUB Adm | 42 | 42 | 28 | 8 | 6 | 0 | 0 | 0 |
| InoversaSul Ana (Contratos) | 36 | 36 | 0 | 36 | 0 | 0 | 1 | 0 |
| STM TJ | 34 | 34 | 31 | 3 | 0 | 0 | 0 | 0 |
| TRT10 TJ | 34 | 34 | 24 | 10 | 0 | 0 | 0 | 0 |
| TCU TEFC | 33 | 33 | 24 | 9 | 0 | 0 | 0 | 0 |
| ANM ERM (Eng. Minas/Correcional) | 29 | 29 | 21 | 8 | 0 | 0 | 0 | 0 |
| STM AJ | 28 | 28 | 26 | 2 | 0 | 0 | 0 | 0 |
| Embrapa Tec (Ativos Patrimoniais) | 24 | 24 | 1 | 23 | 0 | 0 | 0 | 0 |
| TRF6 TJ | 23 | 23 | 16 | 2 | 5 | 0 | 0 | 0 |
| TCE-RS APE (Arquitetura) | 23 | 23 | 22 | 1 | 0 | 0 | 0 | 0 |
| Embrapa Ana (Suprimento) | 23 | 23 | 9 | 14 | 0 | 0 | 0 | 0 |
| ICMBio AA | 23 | 23 | 20 | 3 | 0 | 0 | 0 | 0 |
| PF Ag Adm | 21 | 21 | 18 | 3 | 0 | 0 | 0 | 0 |
| TCE-RS OCE | 21 | 21 | 20 | 1 | 0 | 0 | 0 | 0 |
| FUNPRESP-EXE APC (Adm e Planejamento) | 20 | 20 | 1 | 19 | 0 | 0 | 0 | 0 |
| **Total** | 414 | 414 | 261 | 142 | 11 | 0 | 1 | 0 |

Divergência de gabarito com o gabarito_tec da fila (oficial prevalece): InoversaSul Contratos, item 74 do caderno (fila = Certo; definitivo = E). O item é de regulamento interno da InoversaSul e foi para a reserva; a divergência está registrada na linha da reserva (gabarito_oficial x gabarito_tec). Não houve divergência em item incorporado.

Os 11 itens "dup" já estavam em banco/banco.csv (hash do texto normalizado idêntico): BQ-0137 (candidato 5), BQ-0138 (candidato 6), BQ-0136 (candidato 7), BQ-0139 (candidato 14), BQ-0140 (candidato 24), BQ-0143 (candidato 41), BQ-0124 (candidato 261), BQ-0128 (candidato 265), BQ-0125 (candidato 268), BQ-0126 (candidato 270), BQ-0127 (candidato 278). O gabarito do definitivo coincide com o já registrado em cada uma; não foram reincorporados.

### Cadernos e gabaritos abertos (URL, HTTP 200)

- FUB Adm: caderno PROVA OBJETIVA - CONHECIMENTOS ESPECÍFICOS – CARGO 1 — https://cdn.cebraspe.org.br/concursos/fub_25/arquivos/088_FUB_001_01.pdf (HTTP 200); gabarito GABARITO DEFINITIVO - CONHECIMENTOS ESPECÍFICOS – CARGO 1 — https://cdn.cebraspe.org.br/concursos/fub_25/arquivos/Gab_Definitivo_088_FUB_001_01.pdf (HTTP 200)
- FUB Adm: caderno PROVA OBJETIVA - CONHECIMENTOS BÁSICOS PARA OS CARGOS DE 1 A 14 — https://cdn.cebraspe.org.br/concursos/fub_25/arquivos/088_FUB_CB1_01.pdf (HTTP 200); gabarito GABARITO DEFINITIVO - CONHECIMENTOS BÁSICOS PARA OS CARGOS DE 1 A 14 — https://cdn.cebraspe.org.br/concursos/fub_25/arquivos/Gab_Definitivo_088_FUB_CB1_01.pdf (HTTP 200)
- InoversaSul Ana (Contratos): caderno PROVA OBJETIVA  – CONHECIMENTOS ESPECÍFICOS – CARGO 3 — https://cdn.cebraspe.org.br/concursos/inoversasul_24/arquivos/033_INOVERSASUL_003_01.PDF (HTTP 200); gabarito GABARITO DEFINITIVO – CONHECIMENTOS ESPECÍFICOS – CARGO 3 — https://cdn.cebraspe.org.br/concursos/inoversasul_24/arquivos/GAB_DEFINITIVO_033_INOVERSASUL_003_01.PDF (HTTP 200)
- STM TJ: caderno PROVA OBJETIVA – CONHECIMENTOS ESPECÍFICOS – CARGO 8 — https://cdn.cebraspe.org.br/concursos/stm_25/arquivos/072_STM_008_01.pdf (HTTP 200); gabarito GABARITO DEFINITIVO – CONHECIMENTOS ESPECÍFICOS – CARGO 8 — https://cdn.cebraspe.org.br/concursos/stm_25/arquivos/Gab_Definitivo_072_STM_008_01.pdf (HTTP 200)
- STM TJ: caderno PROVA OBJETIVA - CONHECIMENTOS GERAIS PARA O CARGO 8 — https://cdn.cebraspe.org.br/concursos/stm_25/arquivos/072_STM_CG4_01.pdf (HTTP 200); gabarito GABARITO DEFINITIVO - CONHECIMENTOS GERAIS PARA O CARGO 8 — https://cdn.cebraspe.org.br/concursos/stm_25/arquivos/Gab_Definitivo_072_STM_CG4_01.pdf (HTTP 200)
- TRT10 TJ: caderno PROVA OBJETIVA - CONHECIMENTOS BÁSICOS PARA OS CARGOS 14 E 15 — https://cdn.cebraspe.org.br/concursos/trt10_24/arquivos/050_TRT10_CB4_01.pdf (HTTP 200); gabarito GABARITO DEFINITIVO - CONHECIMENTOS BÁSICOS PARA OS CARGOS 14 E 15 — https://cdn.cebraspe.org.br/concursos/trt10_24/arquivos/Gab_Definitivo_050_TRT10_CB4_01.pdf (HTTP 200)
- TRT10 TJ: caderno PROVA OBJETIVA – CONHECIMENTOS ESPECÍFICOS – CARGO 14 — https://cdn.cebraspe.org.br/concursos/trt10_24/arquivos/050_TRT10_014_01.pdf (HTTP 200); gabarito GABARITO DEFINITIVO - CONHECIMENTOS ESPECÍFICOS – CARGO 14 — https://cdn.cebraspe.org.br/concursos/trt10_24/arquivos/Gab_Definitivo_050_TRT10_014_01.pdf (HTTP 200)
- TCU TEFC: caderno PROVA OBJETIVA – CONHECIMENTOS ESPECÍFICOS — https://cdn.cebraspe.org.br/concursos/tcu_25_tefc/arquivos/108_TCUTEFC_001_01.pdf (HTTP 200); gabarito GABARITO DEFINITIVO – CONHECIMENTOS ESPECÍFICOS — https://cdn.cebraspe.org.br/concursos/tcu_25_tefc/arquivos/E53AB5C65454510E881F7667E620F44B6DDD1C083D5175412CF8725A3C9B9C9F.pdf (HTTP 200)
- ANM ERM (Eng. Minas/Correcional): caderno PROVA OBJETIVA – CONHECIMENTOS ESPECÍFICOS – CARGO 19 — https://cdn.cebraspe.org.br/concursos/anm_24/arquivos/038_ANM_019_01.PDF (HTTP 200); gabarito GABARITO DEFINITIVO – CONHECIMENTOS ESPECÍFICOS – CARGO 19 — https://cdn.cebraspe.org.br/concursos/anm_24/arquivos/Gab_Definitivo_038_ANM_019_01.PDF (HTTP 200)
- STM AJ: caderno PROVA OBJETIVA - CONHECIMENTOS GERAIS PARA O CARGO 1 — https://cdn.cebraspe.org.br/concursos/stm_25/arquivos/072_STM_CG3_01.pdf (HTTP 200); gabarito GABARITO DEFINITIVO - CONHECIMENTOS GERAIS PARA O CARGO 1 — https://cdn.cebraspe.org.br/concursos/stm_25/arquivos/Gab_Definitivo_072_STM_CG3_01.pdf (HTTP 200)
- STM AJ: caderno PROVA OBJETIVA – CONHECIMENTOS ESPECÍFICOS – CARGO 1 — https://cdn.cebraspe.org.br/concursos/stm_25/arquivos/072_STM_001_01.pdf (HTTP 200); gabarito GABARITO DEFINITIVO – CONHECIMENTOS ESPECÍFICOS – CARGO 1 — https://cdn.cebraspe.org.br/concursos/stm_25/arquivos/Gab_Definitivo_072_STM_001_01.pdf (HTTP 200)
- Embrapa Tec (Ativos Patrimoniais): caderno PROVA OBJETIVA – CONHECIMENTOS ESPECÍFICOS - OPÇÃO 40001388: TÉCNICO — https://cdn.cebraspe.org.br/concursos/embrapa_24/arquivos/043_EMBRAPA_011_01.pdf (HTTP 200); gabarito GABARITO DEFINITIVO – CONHECIMENTOS ESPECÍFICOS - OPÇÃO 40001388: TÉCNICO — https://cdn.cebraspe.org.br/concursos/embrapa_24/arquivos/Gab_Definitivo_043_EMBRAPA_011_01.PDF (HTTP 200)
- TRF6 TJ: caderno PROVA OBJETIVA – CONHECIMENTOS ESPECÍFICOS – CARGO 24 — https://cdn.cebraspe.org.br/concursos/trf6_24/arquivos/034_TRF6_024_01.PDF (HTTP 200); gabarito GABARITO DEFINITIVO - CONHECIMENTOS ESPECÍFICOS – CARGO 24 — https://cdn.cebraspe.org.br/concursos/trf6_24/arquivos/GAB_DEFINITIVO_034_TRF6_024_01.PDF (HTTP 200)
- TRF6 TJ: caderno PROVA OBJETIVA - CONHECIMENTOS GERAIS SOMENTE PARA OS CARGOS DE 24 A 26 — https://cdn.cebraspe.org.br/concursos/trf6_24/arquivos/034_TRF6_CG5_01.PDF (HTTP 200); gabarito GABARITO DEFINITIVO - CONHECIMENTOS GERAIS SOMENTE PARA OS CARGOS DE 24 A 26 — https://cdn.cebraspe.org.br/concursos/trf6_24/arquivos/GAB_DEFINITIVO_034_TRF6_CG5_01.PDF (HTTP 200)
- TCE-RS APE (Arquitetura): caderno PROVA OBJETIVA (MODELO) – CONHECIMENTOS GERAIS PARA OS CARGOS 1 A 4 — https://cdn.cebraspe.org.br/concursos/tce_rs_25/arquivos/A07A9AB36794D46172971974AB0E10DD59F725E5E98C1B038920626F1434115E.pdf (HTTP 200); gabarito GABARITO DEFINITIVO (MODELO) – CONHECIMENTOS GERAIS PARA OS CARGOS 1 A 4 — https://cdn.cebraspe.org.br/concursos/tce_rs_25/arquivos/ED939BAF5B74F70525E21D4DA001CD500810EF5A5D2FC68B75B1935797F5D7D7.pdf (HTTP 200)
- TCE-RS APE (Arquitetura): caderno PROVA OBJETIVA (MODELO) – CONHECIMENTOS ESPECÍFICOS – CARGO 1 — https://cdn.cebraspe.org.br/concursos/tce_rs_25/arquivos/2498E3C7584F604DC8E95B1290A88F561AFCEBFE69251C4FD3BD3D6702C38DC9.pdf (HTTP 200); gabarito GABARITO DEFINITIVO (MODELO) – CONHECIMENTOS ESPECÍFICOS – CARGO 1 — https://cdn.cebraspe.org.br/concursos/tce_rs_25/arquivos/914267BDB7DDDCC5DEB863C72B48D14B90DF87796AC917C6BE67BAFCEF937F74.pdf (HTTP 200)
- Embrapa Ana (Suprimento): caderno PROVA OBJETIVA - CONHECIMENTOS COMPLEMENTARES PARA AS OPÇÕES 40002271, 40006388, 40008640, 40004441, 40004461 E 40003340: ANALISTA — https://cdn.cebraspe.org.br/concursos/embrapa_24/arquivos/042_EMBRAPA_ANALISTA_C18_01.pdf (HTTP 200); gabarito GABARITO DEFINITIVO - CONHECIMENTOS COMPLEMENTARES PARA AS OPÇÕES 40002271, 40006388, 40008640, 40004441, 40004461 E 40003340: ANALISTA — https://cdn.cebraspe.org.br/concursos/embrapa_24/arquivos/Gab_Definitivo_042_EMBRAPA_ANALISTA_C18_01.PDF (HTTP 200)
- Embrapa Ana (Suprimento): caderno PROVA OBJETIVA – CONHECIMENTOS ESPECÍFICOS - OPÇÃO 40002271: ANALISTA — https://cdn.cebraspe.org.br/concursos/embrapa_24/arquivos/042_EMBRAPA_ANALISTA_065_01.pdf (HTTP 200); gabarito GABARITO DEFINITIVO – CONHECIMENTOS ESPECÍFICOS - OPÇÃO 40002271: ANALISTA — https://cdn.cebraspe.org.br/concursos/embrapa_24/arquivos/Gab_Definitivo_042_EMBRAPA_ANALISTA_065_01.PDF (HTTP 200)
- ICMBio AA: caderno PROVA OBJETIVA – CONHECIMENTOS BÁSICOS PARA O CARGO 1 — https://cdn.cebraspe.org.br/concursos/icmbio_24/arquivos/045_ICMBIO_CB1_01.pdf (HTTP 200); gabarito GABARITO DEFINITIVO – CONHECIMENTOS BÁSICOS PARA O CARGO 1 — https://cdn.cebraspe.org.br/concursos/icmbio_24/arquivos/Gab_Definitivo_045_ICMBIO_CB1_01.PDF (HTTP 200)
- ICMBio AA: caderno PROVA OBJETIVA – CONHECIMENTOS ESPECÍFICOS – CARGO 1 — https://cdn.cebraspe.org.br/concursos/icmbio_24/arquivos/045_ICMBIO_001_01.pdf (HTTP 200); gabarito GABARITO DEFINITIVO – CONHECIMENTOS ESPECÍFICOS – CARGO 1 — https://cdn.cebraspe.org.br/concursos/icmbio_24/arquivos/Gab_Definitivo_045_ICMBIO_001_01.PDF (HTTP 200)
- PF Ag Adm: caderno PROVA OBJETIVA - CONHECIMENTOS ESPECÍFICOS – CARGO 15 — https://cdn.cebraspe.org.br/concursos/pf_25_adm/arquivos/094_PF_015_01.pdf (HTTP 200); gabarito GABARITO DEFINITIVO - CONHECIMENTOS ESPECÍFICOS – CARGO 15 — https://cdn.cebraspe.org.br/concursos/pf_25_adm/arquivos/Gab_Definitivo_094_PF_015_01.pdf (HTTP 200)
- PF Ag Adm: caderno PROVA OBJETIVA - CONHECIMENTOS BÁSICOS PARA O CARGO 15 — https://cdn.cebraspe.org.br/concursos/pf_25_adm/arquivos/094_PF_CB2_01.pdf (HTTP 200); gabarito GABARITO DEFINITIVO - CONHECIMENTOS BÁSICOS PARA O CARGO 15 — https://cdn.cebraspe.org.br/concursos/pf_25_adm/arquivos/Gab_Definitivo_094_PF_CB2_01.pdf (HTTP 200)
- TCE-RS OCE: caderno PROVA OBJETIVA (MODELO) – CONHECIMENTOS ESPECÍFICOS – CARGO 5 — https://cdn.cebraspe.org.br/concursos/tce_rs_25/arquivos/877A4AC2DDD6EBE7E2BFD3D7547822BF761DF6F2473F18041246B3886C9CB15E.pdf (HTTP 200); gabarito GABARITO DEFINITIVO (MODELO) – CONHECIMENTOS ESPECÍFICOS – CARGO 5 — https://cdn.cebraspe.org.br/concursos/tce_rs_25/arquivos/9C04C8B977600E25B7AD360E5A7BCB75DA6AF6ADE848CA618CE19F7330C0C4EA.pdf (HTTP 200)
- FUNPRESP-EXE APC (Adm e Planejamento): caderno PROVA OBJETIVA – CONHECIMENTOS ESPECÍFICOS – CARGO 1 — https://cdn.cebraspe.org.br/concursos/funpresp_24_exe/arquivos/040_FUNPRESPEXE_001_01.PDF (HTTP 200); gabarito GABARITO DEFINITIVO – CONHECIMENTOS ESPECÍFICOS – CARGO 1 — https://cdn.cebraspe.org.br/concursos/funpresp_24_exe/arquivos/Gab_Definitivo_040_FUNPRESPEXE_001_01.PDF (HTTP 200)

## 3. Totais
- Candidatos: 414; localizados no caderno com gabarito definitivo: 414; não localizados: 0.
- Incorporados ao staging: 261 (C = 126, E = 135, X = 0); ids BQ-0212 a BQ-0472. Aderência: direta 236, parcial 25. VOLÁTIL-NORMATIVO: 16.
- Reserva (achados, fora do edital): 142 linhas em saida/banco/reserva_DA.csv; já no banco (dup): 11.
- Reserva por motivo:
  - 36 × regulamento interno de licitações e contratos da Fundação InoversaSul (Resolução 16/2024-CONSET); norma não coberta pelo edital
  - 23 × Regulamento de Licitações, Contratos e Convênios da Embrapa (RLCC) / Lei 13.303/2016 / sistemas federais
  - 9 × Lei 13.303/2016 (empresas estatais): FORA
  - 9 × Regulamento Interno de Licitações e Contratações da FUNPRESP-EXE
  - 8 × Lei 12.846/2013 (anticorrupção): FORA
  - 4 × Decreto 11.531/2023 (convênios): FORA
  - 4 × sistema de registro de preços: FORA
  - 4 × convênios e instrumentos congêneres: FORA
  - 3 × adesão a ata de registro de preços (SRP): FORA
  - 2 × controle administrativo
  - 2 × Instrumento de Padronização dos Procedimentos de Contratação (Justiça do Trabalho)
  - 2 × IN SEGES/ME 65/2021 (pesquisa de preços): FORA
  - 2 × Decreto 11.129/2022 (anticorrupção): FORA
  - 2 × Lei 8.987/1995 (concessões): FORA
  - 2 × Resolução CGPAR 45/2022 (empresas estatais): FORA
  - 1 × fontes do direito administrativo; tema fora dos itens 1–12 do edital
  - 1 × controle externo (CF arts. 70–75): FORA
  - 1 × controle externo (TCU e sustação de contrato): FORA
  - 1 × alienação de bens inservíveis (bens públicos): FORA
  - 1 × sistema de controle e unidade de jurisdição
  - 1 × função comissionada no Judiciário da União (Lei 11.416/2006)
  - 1 × plano de contratações da Justiça do Trabalho (norma de órgão); fora do edital
  - 1 × controle judicial x controle administrativo
  - 1 × controle concomitante
  - 1 × controle de mérito
  - 1 × controle parlamentar: sustação de atos normativos (CF art. 49, V)
  - 1 × contencioso administrativo e jurisdição una
  - 1 × jurisdição una e coisa julgada administrativa
  - 1 × controle jurisdicional
  - 1 × IN SEGES 5/2017 (instituição sem fins lucrativos)
  - 1 × Decreto 11.129/2022 (anticorrupção, programa de integridade): FORA
  - 1 × controle financeiro do Legislativo
  - 1 × controle judicial da banca examinadora de concurso
  - 1 × garantia contratual em contratações de empresa pública (Lei 13.303/2016): FORA
  - 1 × matriz de risco na Lei 13.303/2016: FORA
  - 1 × licitação em empresa pública (Lei 13.303/2016): FORA
  - 1 × oportunidades de negócio da Embrapa (Lei 13.303/2016): FORA
  - 1 × contratações compartilhadas na Embrapa (Lei 13.303/2016): FORA
  - 1 × mandado de segurança e controle
  - 1 × convênios com entidades privadas sem fins lucrativos: FORA
  - 1 × controle legislativo e TCU: FORA
  - 1 × requisição administrativa de bens (intervenção na propriedade)
  - 1 × Decreto 11.462/2023 (SRP): FORA
  - 1 × Decreto 7.983/2013 (orçamento de referência de obras): FORA
  - 1 × Decreto 7.983/2013 (orçamento de referência de obras) / Lei 13.303: FORA

## 4. Mecanismo dos itens incorporados (leitura desta execução)

| Mecanismo | Itens | C | E |
|---|---|---|---|
| AMB | 8 | 0 | 8 |
| AP | 25 | 18 | 7 |
| AUT | 7 | 0 | 7 |
| CON | 32 | 0 | 32 |
| GEN | 16 | 0 | 16 |
| LIT | 106 | 106 | 0 |
| NEG | 23 | 0 | 23 |
| PRA | 14 | 2 | 12 |
| SUP | 26 | 0 | 26 |
| TEM | 4 | 0 | 4 |

## 5. Contagem por item do edital antes e depois (reais = CEBRASPE_OFICIAL + CEBRASPE_ANALOGA com gabarito C/E; "antes" já inclui BQ-0153 a BQ-0211 do cd_25_ns; sem X)

Subitem lido de observacoes ("item X.Y"); P1-DA-n é o nível da coluna item_edital_camara. Entre parênteses, só aderência direta (D-ADERENCIA: parcial vale só para simulado diagnóstico).

| Grupo do edital | antes | + onda 1 | depois | depois (direta) | meta 30 | situação |
|---|---|---|---|---|---|---|
| 1.1 | 2 | 4 | 6 | 6 | 30 | faltam 24 |
| 1.2 | 9 | 11 | 20 | 18 | 30 | faltam 10 |
| 2 | 6 | 12 | 18 | 18 | 30 | faltam 12 |
| 3 (sem 3.4) | 5 | 18 | 23 | 21 | 30 | faltam 7 |
| 3.4 | 6 | 11 | 17 | 17 | 30 | faltam 13 |
| 4.1-4.3 | 1 | 9 | 10 | 10 | 30 | faltam 20 |
| 4.4 | 6 | 25 | 31 | 31 | 30 | atingida |
| 5 | 3 | 9 | 12 | 12 | 30 | faltam 18 |
| 6 | 2 | 15 | 17 | 17 | 30 | faltam 13 |
| 7 | 5 | 22 | 27 | 25 | 30 | faltam 3 |
| 8 | 8 | 0 | 8 | 6 | - | - |
| 9 | 6 | 0 | 6 | 5 | - | - |
| 10 | 24 | 114 | 138 | 118 | 30 | atingida |
| 11 | 6 | 11 | 17 | 16 | - | - |
| 12 | 7 | 0 | 7 | 7 | - | - |

Leitura da meta "3.4/4": 3.4 sozinho = 17; 4.1 a 4.3 = 10; 3.4 + 4.1–4.3 = 27. Meta ≥ 30 atingida em: 10, 4.4. Faltam: 1.1: 24; 2: 12; 3 (sem 3.4): 7; 5: 18; 6: 13.

Por nível P1-DA-n (coluna item_edital_camara) nas linhas do staging: P1-DA-1 = 15, P1-DA-2 = 12, P1-DA-3 = 29, P1-DA-4 = 34, P1-DA-5 = 9, P1-DA-6 = 15, P1-DA-7 = 22, P1-DA-10 = 114, P1-DA-11 = 11.

## 6. Observações para o QA
- 25 itens (aderência parcial) valem só para simulado diagnóstico: IN SEGES 5/2017 (fiscalização setorial, preposto, indicadores), Decreto 11.878/2024 e IN SEGES 73/2022 (credenciamento, fases), fundações de apoio, declaração de bens (Lei 8.730/1993 x LIA), exploração de atividade econômica pelo Estado, publicidade do PCA. Conferir arbitragem.
- Itens apoiados em jurisprudência do STF (poder de polícia em etapas; escusa de consciência; teto em acumulação; inquérito e concurso; recontratação em emergência; licença-paternidade monoparental; Súmula Vinculante 5; fraude em concurso) precisam de conferência do entendimento vigente pelo qa-normativo-da.
- Itens E em que a banca depende de redação de lei alterada em 2021 (Lei 14.230 na LIA, Lei 14.210 na Lei 9.784 — decisão coordenada) ou de dispositivo de Lei 14.133 conferem ao qa-normativo-da (art. a art.).
- Comandos: texto_comando e texto_base são literais do caderno; nos itens com situação hipotética a narrativa foi separada do comando final (24 itens). BQ de CB1/CG compartilhados citam o caderno de conhecimentos básicos/gerais do cargo.
- TCE-RS: os arquivos do CDN são "PROVA OBJETIVA (MODELO)" e "GABARITO DEFINITIVO (MODELO)" (único modelo publicado); citados como tal.
- Todos os itens têm "QA PENDENTE" e não entram em simulado até a QA (D-QA-PENDENTE).

## 7. Amostra para a reclassificação cega de mecanismo (100 itens)

Semente: random.Random(20261025).sample(ids dos 261 itens incorporados, 100), ids em ordem crescente. O classificador de modelo distinto lê texto_integral e texto_comando em saida/banco/onda1/banco_onda1_staging.csv sem olhar a observação "mecanismo=". Limiar da ordem: concordância < 80% devolve a tabela de mecanismos à Presidência antes do uso na plataforma.

BQ-0212, BQ-0217, BQ-0220, BQ-0222, BQ-0223, BQ-0225, BQ-0226, BQ-0227, BQ-0231, BQ-0232, BQ-0233, BQ-0237, BQ-0242, BQ-0246, BQ-0248, BQ-0250, BQ-0254, BQ-0256, BQ-0258, BQ-0267, BQ-0269, BQ-0270, BQ-0277, BQ-0281, BQ-0283, BQ-0286, BQ-0288, BQ-0289, BQ-0293, BQ-0294, BQ-0295, BQ-0298, BQ-0302, BQ-0303, BQ-0304, BQ-0305, BQ-0306, BQ-0309, BQ-0311, BQ-0312, BQ-0313, BQ-0314, BQ-0316, BQ-0319, BQ-0324, BQ-0327, BQ-0328, BQ-0330, BQ-0331, BQ-0332, BQ-0335, BQ-0338, BQ-0343, BQ-0347, BQ-0351, BQ-0353, BQ-0354, BQ-0360, BQ-0361, BQ-0362, BQ-0364, BQ-0369, BQ-0371, BQ-0372, BQ-0374, BQ-0379, BQ-0380, BQ-0384, BQ-0387, BQ-0388, BQ-0389, BQ-0390, BQ-0402, BQ-0404, BQ-0405, BQ-0406, BQ-0407, BQ-0408, BQ-0418, BQ-0421, BQ-0423, BQ-0424, BQ-0425, BQ-0427, BQ-0429, BQ-0437, BQ-0439, BQ-0443, BQ-0444, BQ-0446, BQ-0448, BQ-0449, BQ-0453, BQ-0456, BQ-0457, BQ-0462, BQ-0466, BQ-0467, BQ-0471, BQ-0472


