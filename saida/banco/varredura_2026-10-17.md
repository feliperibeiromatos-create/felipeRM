# varredura_2026-10-17.md — T-79 varredura do banco com alvo P1-DA (s11c3) — 2026-10-17 — gerado por gbq-cfp

Todos os arquivos abaixo foram abertos por mim em 2026-10-17 (verificado em 17/10/2026) diretamente em cdn.cebraspe.org.br (PDF, texto extraído com pdftotext). Cada item registrado tem caderno e gabarito GAB_DEFINITIVO_ abertos. Nenhum espelho de terceiros foi usado (a busca web só serviu para localizar o certame; nenhum dado de item veio dela). Nenhum certame é cd_25_ns/cd_26_*, portanto todas as linhas novas são CEBRASPE_ANALOGA. Nenhum item de múltipla escolha apareceu nos cadernos varridos (todos C/E). Nenhuma linha existente foi alterada (diff de banco/banco.csv = 40 linhas acrescentadas, prefixo byte a byte idêntico).

## Resultado
- 40 linhas novas em banco/banco.csv, ids BQ-0113 a BQ-0152 (banco: 112 -> 152 linhas).
- Gabarito: 27 C, 11 E, 2 X (anulados: CNJ cargo 6 itens 63 e 66).
- Aderência: 39 direta, 1 parcial (TRF6 cargo 1 item 55).
- Todas com "QA PENDENTE" em observacoes (norma-alvo indicada para o qa-normativo-da; itens de doutrina/jurisprudência indicam gbq-cqe). Mapeamento principal gravado como P1-DA-<n> em item_edital_camara, com o subitem do edital em observacoes.
- Item novo em banco/mapeamento_adicional.csv: não houve (as linhas já nascem com mapeamento P1-DA principal).

## Certames, cadernos e gabaritos (todos abertos em 2026-10-17)
TRF6 2024 (Edital nº 1, 10/10/2024; aplicação 19/01/2025)
- Cargo 1 Analista Judiciário, Área Administrativa: https://cdn.cebraspe.org.br/concursos/TRF6_24/arquivos/034_TRF6_001_01.PDF e https://cdn.cebraspe.org.br/concursos/TRF6_24/arquivos/GAB_DEFINITIVO_034_TRF6_001_01.PDF
- Cargo 23 Analista Judiciário, Área Judiciária: https://cdn.cebraspe.org.br/concursos/trf6_24/arquivos/034_TRF6_023_01.PDF e .../GAB_DEFINITIVO_034_TRF6_023_01.PDF
- Cargo 24 Técnico Judiciário, Área Administrativa: https://cdn.cebraspe.org.br/concursos/trf6_24/arquivos/034_TRF6_024_01.PDF e .../GAB_DEFINITIVO_034_TRF6_024_01.PDF
CNJ 2024 (aplicação 30/6/2024)
- Cargo 6 Analista Judiciário, Área Judiciária: https://cdn.cebraspe.org.br/concursos/cnj_24/arquivos/979_CNJ_006_01.PDF e .../GAB_DEFINITIVO_979_CNJ_006_01.PDF
- Cargo 7 Técnico Judiciário, Área Administrativa: https://cdn.cebraspe.org.br/concursos/cnj_24/arquivos/979_CNJ_007_01.PDF e .../GAB_DEFINITIVO_979_CNJ_007_01.PDF
FUB 2025 (Edital nº 1, 3/4/2025; aplicação 29/06/2025), base https://cdn.cebraspe.org.br/concursos/fub_25/arquivos/
- 088_FUB_001_01.PDF (Cargo 1 Administrador), 088_FUB_002_01.PDF (Cargo 2 Arquiteto e Urbanista), 088_FUB_CB1_01.PDF (Conhecimentos Básicos cargos 1 a 14), 088_FUB_CB2_01.PDF (cargos 16, 17 e 19), 088_FUB_CB3_01.PDF (cargo 15); gabaritos GAB_DEFINITIVO_<mesmo código>.PDF no mesmo diretório.
ANM 2024 (aplicação 16/02/2025), base https://cdn.cebraspe.org.br/concursos/anm_24/arquivos/
- 038_ANM_013_01.PDF (Cargo 13 Comunicação), 038_ANM_015_01.PDF (Cargo 15 Direito, foco outorga), 038_ANM_023_01.PDF (Cargo 23 Qualquer área, suporte à gestão, estratégia e governança); gabaritos GAB_DEFINITIVO_038_ANM_0xx_01.PDF.

Varridos sem item aproveitável (sem tema P1-DA, ou só com tema de outro cargo): TRF6 cargos 3 a 22 e 25 a 28 (TI, engenharias, medicina, contabilidade etc.; só cargo 13/16 trazem governança/LGPD já cobertos por outros itens do banco ou fora de P1-DA); CNJ cargos 1, 3, 4, 5, 8 (cargo 2 já no banco); FUB cargos 3, 4, 5 e CB4 (CB4 repete CB3); ANM cargo 18 (governança pública geral, ver reserva). Cargos TRF6 acima de 28 (testado até 30) e CNJ acima de 8 (testado até 20) não foram localizados no CDN.

## Distribuição por item do edital (P1-DA)
Contagem: DA-1 = 5; DA-2 = 3; DA-3 = 5; DA-4 = 4; DA-5 = 3; DA-6 = 1; DA-7 = 4; DA-8 = 1; DA-9 = 2; DA-10 = 4; DA-11 = 4; DA-12 = 4. Total 40.

## Itens incluídos (id; certame-cargo-item; gabarito; P1-DA; tema)
Tabela abaixo; texto literal, comando e URLs em banco/banco.csv. Ordem das linhas = TRF6 (1: 53, 55, 56, 57, 59, 60, 61, 62, 76; 23: 53, 57; 24: 65, 67, 68, 70, 88), CNJ (6: 51, 62, 63 X, 65, 66 X; 7: 116, 118), FUB (1: 73, 94, 96, 100, 101, 105; 2: 98; CB1: 29, 30; CB2: 25; CB3: 25), ANM (13: 70; 15: 71, 76, 79; 23: 109, 111), correspondendo a BQ-0113 a BQ-0152 na mesma sequência.

| id | certame / cargo / item | gab | P1-DA | aderência |
|---|---|---|---|---|
| BQ-0113 | TRF6 2024 Cargo 1 #53 | C | P1-DA-10 | direta |
| BQ-0114 | TRF6 2024 Cargo 1 #55 | C | P1-DA-3 | parcial |
| BQ-0115 | TRF6 2024 Cargo 1 #56 | C | P1-DA-1 | direta |
| BQ-0116 | TRF6 2024 Cargo 1 #57 | E | P1-DA-5 | direta |
| BQ-0117 | TRF6 2024 Cargo 1 #59 | C | P1-DA-12 | direta |
| BQ-0118 | TRF6 2024 Cargo 1 #60 | E | P1-DA-12 | direta |
| BQ-0119 | TRF6 2024 Cargo 1 #61 | E | P1-DA-11 | direta |
| BQ-0120 | TRF6 2024 Cargo 1 #62 | E | P1-DA-11 | direta |
| BQ-0121 | TRF6 2024 Cargo 1 #76 | C | P1-DA-8 | direta |
| BQ-0122 | TRF6 2024 Cargo 23 #53 | C | P1-DA-2 | direta |
| BQ-0123 | TRF6 2024 Cargo 23 #57 | C | P1-DA-12 | direta |
| BQ-0124 | TRF6 2024 Cargo 24 #65 | C | P1-DA-1 | direta |
| BQ-0125 | TRF6 2024 Cargo 24 #67 | C | P1-DA-3 | direta |
| BQ-0126 | TRF6 2024 Cargo 24 #68 | C | P1-DA-3 | direta |
| BQ-0127 | TRF6 2024 Cargo 24 #70 | C | P1-DA-4 | direta |
| BQ-0128 | TRF6 2024 Cargo 24 #88 | C | P1-DA-3 | direta |
| BQ-0129 | CNJ 2024 Cargo 6 #51 | C | P1-DA-1 | direta |
| BQ-0130 | CNJ 2024 Cargo 6 #62 | C | P1-DA-5 | direta |
| BQ-0131 | CNJ 2024 Cargo 6 #63 | X | P1-DA-1 | direta |
| BQ-0132 | CNJ 2024 Cargo 6 #65 | C | P1-DA-4 | direta |
| BQ-0133 | CNJ 2024 Cargo 6 #66 | X | P1-DA-7 | direta |
| BQ-0134 | CNJ 2024 Cargo 7 #116 | C | P1-DA-10 | direta |
| BQ-0135 | CNJ 2024 Cargo 7 #118 | E | P1-DA-10 | direta |
| BQ-0136 | FUB 2025 Cargo 1 #73 | C | P1-DA-1 | direta |
| BQ-0137 | FUB 2025 Cargo 1 #94 | C | P1-DA-2 | direta |
| BQ-0138 | FUB 2025 Cargo 1 #96 | E | P1-DA-5 | direta |
| BQ-0139 | FUB 2025 Cargo 1 #100 | C | P1-DA-6 | direta |
| BQ-0140 | FUB 2025 Cargo 1 #101 | C | P1-DA-7 | direta |
| BQ-0141 | FUB 2025 Cargo 1 #105 | E | P1-DA-7 | direta |
| BQ-0142 | FUB 2025 Cargo 2 #98 | C | P1-DA-10 | direta |
| BQ-0143 | FUB 2025 Conhecimentos Básicos para os Cargos de 1 a 14 #29 | E | P1-DA-11 | direta |
| BQ-0144 | FUB 2025 Conhecimentos Básicos para os Cargos de 1 a 14 #30 | C | P1-DA-12 | direta |
| BQ-0145 | FUB 2025 Conhecimentos Básicos para os Cargos 16, 17 e 19 #25 | C | P1-DA-4 | direta |
| BQ-0146 | FUB 2025 Conhecimentos Básicos para o Cargo 15 #25 | E | P1-DA-4 | direta |
| BQ-0147 | ANM 2024 Cargo 13 #70 | E | P1-DA-11 | direta |
| BQ-0148 | ANM 2024 Cargo 15 #71 | E | P1-DA-2 | direta |
| BQ-0149 | ANM 2024 Cargo 15 #76 | C | P1-DA-7 | direta |
| BQ-0150 | ANM 2024 Cargo 15 #79 | C | P1-DA-3 | direta |
| BQ-0151 | ANM 2024 Cargo 23 #109 | C | P1-DA-9 | direta |
| BQ-0152 | ANM 2024 Cargo 23 #111 | C | P1-DA-9 | direta |
Alvos prioritários cobertos: LGPD/ANPD (DA-12): TRF6-1 #59, #60; TRF6-23 #57; FUB CB1 #30. LAI (DA-11): TRF6-1 #61, #62; FUB CB1 #29; ANM-13 #70. Lei 8.112 (DA-3.4/4.2): TRF6-24 #67, #68, ANM-15 #79, FUB CB3 #25, TRF6-24 #88 (requisição). Lei 9.784 (DA-4.4): CNJ6 #65, TRF6-24 #70, FUB CB2 #25. Lei 8.429 (DA-7): CNJ6 #66 (X), FUB-1 #101, #105, ANM-15 #76. Lei 14.133 (DA-10): TRF6-1 #53, CNJ7 #116, #118, FUB-2 #98. Decreto 9.203 (DA-9.4): ANM-23 #109, #111.

## Itens excluídos / não registrados e motivo
- FUB CB2 item 30 (LGPD, dados sensíveis): já no banco (BQ-0084); não duplicado.
- FUB CB4 itens 13 a 17, 21, 22 e CB3 itens correspondentes: mesmo enunciado em dois cadernos; registrado só o do CB3 (CB3 #25, nota em observacoes sobre CB4 #17). Os demais itens repetidos CB3/CB4 (ex.: CB3 #21 a #24, #29, #30) ficam na reserva.
- Itens aderentes identificados e deixados de fora só pelo teto do ciclo (reserva para a próxima varredura, todos com gabarito definitivo já lido): TRF6-1 #51, #52, #54, #58 (X), #78 (X); TRF6-23 #54 a #56, #58; TRF6-24 #63, #64, #66, #69, #71, #72, #89, #90; CNJ6 #59 a #61, #64; CNJ7 #113 a #115, #117, #119; FUB-1 #54, #60, #71 a #74, #91 a #93, #95, #97 a #99, #104, #106 a #110, #111, #112, #117, #118; FUB-2 #96 a #103 (exceto #98); FUB-3 #83, #87, #90, #91; FUB CB1 #48 a #50; FUB CB2 #21 a #24, #26, #30 (já BQ-0084); FUB CB3 #21 a #24, #29, #30; ANM-13 #66 a #69; ANM-15 #72 a #75, #77 a #80; ANM-18 #69 a #86 (governança, com #80 e #81 X); ANM-23 #110, #112, #117, #118, #120.
- Fora do escopo P1-DA (não registrados): itens de contabilidade, orçamento, gestão de estoques, Constituição (controle de constitucionalidade, Judiciário), LINDB/civil/penal/processo penal (CNJ6 #68 a #93), TCU/controle (parcial, só em reserva), gestão de pessoas.
- Anulados (X) incluídos: CNJ6 #63 (princípio da motivação) e #66 (retroatividade das alterações da Lei 8.429). Ficam no banco com anulado=sim e não entram em simulado.

## Lacunas de cobertura (P1-DA sem item nesta varredura)
Sem itens: 3.1 (disposições constitucionais sobre agentes), 4.1 e 4.3 (fontes e procedimentos disciplinares: sindicância, PAD), 6.1 a 6.3 isolados (só 6.5 coberto), 8.1 a 8.4 (NPG, valor público: só patrimonialismo), 9.1 a 9.3 só em reserva (ANM-18, FUB-1 #54), 10.2/10.3/10.5 só em reserva. Recomendação: próxima varredura em certames com Direito Administrativo pleno (cargos de Analista Judiciário, Área Judiciária e de Técnico em tribunais e MPU 2023–2025) e busca de PAD/sindicância na Lei 8.112 arts. 143 a 182.

## Observações ao QA
1. Gabarito lido pelo texto extraído do PDF (ordem de colunas conferida em todos os arquivos; amostras conferidas à mão em TRF6-1, CNJ6 e ANM-23). O gbq-cqe deve reabrir cada gabarito.
2. Itens com redação sensível a mudança legislativa (Lei 14.230/2021 em DA-7; Lei 14.133/2021 em DA-10; LGPD com Lei 15.352/2026 em DA-12) estão marcados para o qa-normativo-da; este agente não afirma o texto vigente dos artigos.
3. TRF6-1 #61 (LAI) e #62: gabarito E; conferir se a fundamentação do E é a delimitação a órgãos da administração direta (#61) e o encaminhamento do recurso (#62).
4. FUB CB2 #25: o comando do caderno cita "Lei n.º 9.784/1992" (grafia literal do caderno, transcrita sem correção).
5. Data de aplicação ANM: 16/02/2025 (ano_aplicacao 2025, igual às linhas ANM já no banco).
