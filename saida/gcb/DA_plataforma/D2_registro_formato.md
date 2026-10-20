# D2_registro_formato.md — T-75 (ordem DA 20/10/2026) — 2026-10-20 — gerado por gcb-cpp

Reformatação do Lote D2 (Agentes públicos e direito administrativo disciplinar, itens 3 e 4 do edital) para o formato da plataforma (FORMATO_PLATAFORMA_DA.md). Só forma; nenhum conteúdo novo. Gerado por `saida/gcb/DA_plataforma/scripts/formatar_D2.py --registro`; fidelidade por `saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D2.py`.

## 1. Fontes e conferências
- Canônico: saida/gcb/D2_v2_1.md, SHA-256 59cffaa689ea869cd11c13e6a833470b0b91d24b0f25ea2cc2e100ac9be8bd2c (igual ao esperado 59cffaa6…8bd2c: o script confere antes de ler e pararia se divergisse).
- Base normativa: saida/gcb/D2_anexo_N_mapa_normativo.md (consulta de 20/10/2026), SHA-256 b0a54fff4ddcf21a693e01ba71032efccf72e0a6fdf912221ff05413cc0e340a; usado só pelo validador e pelo visual baseLegal (texto copiado letra a letra da coluna de texto do mapa, `literal: true`, `conferido: 2026-10-20`).
- Seções do canônico NÃO usadas: 0 e 0.1 (resposta ao R1 e registro de acatamento), os dois parágrafos "Cada bloco: …" da seção 1 (convenções de produção; um abre a seção e outro fica solto antes da folha 4.1), o cabeçalho das seções 3 e 4 (contagens de produção: "Mínimo da ficha…", "Entregues…"), 6 (proveniência), 7 (contagens), 8 (bloco à GCB), as linhas Folha, Ponto de julgamento, Formato, Base, Mecanismo, Troca, Alteração na v2, "Difere de …" e Marcas de cada item, e as colunas "Código" e "Base" dos pares.
- JSON gerado: D2_plataforma.json, SHA-256 cba2e2769ba680ee028edf0f0a5e52a5bf55671c894f5c920edaf84f3cf139bf; tópicos incorporados de D2_topicos_fonte.json, SHA-256 2be70602378cd207e85fb949c96b6ba3de225fbd5991a540eef54f6b0d41eaae (escritos à mão); log das edições (lido pela conferência): D2_log_edicoes.json, SHA-256 4cd1c6b15f4fd650dd0ce26ce342f35d237bc4386960b4779ff3106f8b12d35d.

## 2. Correspondência bloco de origem → ## / ###
| Origem (D2_v2_1.md, seção 1) | Destino no curso |
|---|---|
| Folha 3.1 — Disposições constitucionais aplicáveis | `## 3.1 DISPOSIÇÕES CONSTITUCIONAIS APLICÁVEIS` |
| C3.0-01 Caput 3 — Agentes públicos (curso curto; sem item, sem par e sem pegadinha próprios) (curso do caput 3, sem folha) | `### Caput 3 — Agentes públicos (primeiro ### do ## 3.1)` |
| C3.1-01 Concurso público: validade, prioridade e nulidade (CF, art. 37, II a IV e § 2º) | `### Concurso público: validade, prioridade e nulidade (CF, art. 37, II a IV e § 2º)` |
| C3.1-02 Acumulação remunerada de cargos, empregos e funções (CF, art. 37, XVI e XVII) | `### Acumulação remunerada de cargos, empregos e funções (CF, art. 37, XVI e XVII)` |
| C3.1-03 Remuneração, subsídio e teto (CF, art. 37, X a XV; art. 39, §§ 1º a 8º) | `### Remuneração, subsídio e teto (CF, art. 37, X a XV; art. 39, §§ 1º a 8º)` |
| C3.1-04 Servidor público em mandato eletivo (CF, art. 38) | `### Servidor público em mandato eletivo (CF, art. 38)` |
| C3.1-05 Regime próprio de previdência social (CF, art. 40) e nota sobre a EC 140/2026 | `### Regime próprio de previdência social (CF, art. 40) e nota sobre a EC 140/2026` |
| C3.1-06 Estabilidade e avaliação especial de desempenho (CF, art. 41, caput e § 4º) | `### Estabilidade e avaliação especial de desempenho (CF, art. 41, caput e § 4º)` |
| C3.1-07 Perda do cargo pelo servidor estável (CF, art. 41, § 1º) | `### Perda do cargo pelo servidor estável (CF, art. 41, § 1º)` |
| C3.1-08 Reintegração, recondução e disponibilidade do estável (CF, art. 41, §§ 2º e 3º) | `### Reintegração, recondução e disponibilidade do estável (CF, art. 41, §§ 2º e 3º)` |
| C3.1-09 Associação sindical, greve e reserva de vagas para pessoa com deficiência (CF, art. 37, VI, VII e VIII; Lei 8.112/1990, art. 5º, § 2º) — acréscimo da v2 (leitura externa A2, A3, B1, B2, C2; QA PENDENTE (R2)) | `### Associação sindical, greve e reserva de vagas para pessoa com deficiência (CF, art. 37, VI, VII e VIII; Lei 8.112/1990, art. 5º, § 2º)` |
| C3.1-10 Teto remuneratório e outras regras do art. 37 (CF, art. 37, XI e §§ 9º a 14) — acréscimo da v2 (leitura externa B3, B4, C3, C5; QA PENDENTE (R2)) | `### Teto remuneratório e outras regras do art. 37 (CF, art. 37, XI e §§ 9º a 14)` |
| C3.1-11 Sistema remuneratório: demais regras do art. 39 (CF, art. 39, §§ 1º a 3º, 5º e 7º a 9º) — acréscimo da v2 (leitura externa C4; QA PENDENTE (R2)) | `### Sistema remuneratório: demais regras do art. 39 (CF, art. 39, §§ 1º a 3º, 5º e 7º a 9º)` |
| C3.1-12 Regime próprio de previdência: regras complementares (CF, art. 40, §§ 4º-A, 4º-B, 4º-C, 5º, 6º, 14 a 16 e 19) — acréscimo da v2 (leitura externa C6; QA PENDENTE (R2)) | `### Regime próprio de previdência: regras complementares (CF, art. 40, §§ 4º-A, 4º-B, 4º-C, 5º, 6º, 14 a 16 e 19)` |
| Folha 3.2 — Cargo, emprego e função pública | `## 3.2 CARGO, EMPREGO E FUNÇÃO PÚBLICA` |
| C3.2-01 Acessibilidade e concurso público (CF, art. 37, I e II; Lei 8.112/1990, art. 10) | `### Acessibilidade e concurso público (CF, art. 37, I e II; Lei 8.112/1990, art. 10)` |
| C3.2-02 Servidor e cargo público (Lei 8.112/1990, arts. 2º e 3º) | `### Servidor e cargo público (Lei 8.112/1990, arts. 2º e 3º)` |
| C3.2-03 Função de confiança e cargo em comissão (CF, art. 37, V; Lei 8.112/1990, art. 15, caput) | `### Função de confiança e cargo em comissão (CF, art. 37, V; Lei 8.112/1990, art. 15, caput)` |
| C3.2-04 Contratação por tempo determinado (CF, art. 37, IX) | `### Contratação por tempo determinado (CF, art. 37, IX)` |
| C3.2-05 Vedação de serviço gratuito e requisitos de investidura (Lei 8.112/1990, arts. 4º e 5º) | `### Vedação de serviço gratuito e requisitos de investidura (Lei 8.112/1990, arts. 4º e 5º)` |
| C3.2-06 Nomeação em caráter efetivo e em comissão (Lei 8.112/1990, arts. 9º e 10) | `### Nomeação em caráter efetivo e em comissão (Lei 8.112/1990, arts. 9º e 10)` |
| C3.2-07 Emprego público e função pública: rótulos ao lado do dispositivo | `### Emprego público e função pública: rótulos ao lado do dispositivo` |
| Folha 3.3 — Requisição | `## 3.3 REQUISIÇÃO` |
| C3.3-01 Formas de movimentação do agente público (Decreto 10.835/2021, arts. 1º e 2º) | `### Formas de movimentação do agente público (Decreto 10.835/2021, arts. 1º e 2º)` |
| C3.3-02 Conceito de requisição (Decreto 10.835/2021, art. 9º, caput e §§ 1º a 3º) | `### Conceito de requisição (Decreto 10.835/2021, art. 9º, caput e §§ 1º a 3º)` |
| C3.3-03 Prazo e encerramento da requisição (Decreto 10.835/2021, art. 11) | `### Prazo e encerramento da requisição (Decreto 10.835/2021, art. 11)` |
| C3.3-04 Garantias do requisitado, reembolso, competência e dispensa de novo ato (Decreto 10.835/2021, arts. 9º, §§ 4º a 6º, 10, 29, 30 e 30-A) | `### Garantias do requisitado, reembolso, competência e dispensa de novo ato (Decreto 10.835/2021, arts. 9º, §§ 4º a 6º, 10, 29, 30 e 30-A)` |
| C3.3-05 Requisições para a Presidência da República (Lei 9.007/1995, arts. 2º e 3º) | `### Requisições para a Presidência da República (Lei 9.007/1995, arts. 2º e 3º)` |
| C3.3-06 Requisição de servidores pela Justiça Eleitoral (Lei 6.999/1982) | `### Requisição de servidores pela Justiça Eleitoral (Lei 6.999/1982)` |
| C3.3-07 Cessão como contraste (Decreto 10.835/2021, arts. 3º a 8º; Lei 8.112/1990, art. 93) | `### Cessão como contraste (Decreto 10.835/2021, arts. 3º a 8º; Lei 8.112/1990, art. 93)` |
| C3.3-08 Requisição no estágio probatório e prazo de retomada do exercício (Decreto 12.374/2025, art. 21; Lei 8.112/1990, arts. 18 e 20, § 3º) | `### Requisição no estágio probatório e prazo de retomada do exercício (Decreto 12.374/2025, art. 21; Lei 8.112/1990, arts. 18 e 20, § 3º)` |
| C3.3-09 Requisição administrativa (CF, art. 5º, XXV): contraste de termo | `### Requisição administrativa (CF, art. 5º, XXV): contraste de termo` |
| C3.3-10 Reembolso nas movimentações e comunicação na dispensa de novo ato (Decreto 10.835/2021, arts. 10, 17 a 22, 24, 25 e 30-A, parágrafo único) — acréscimo da v2 (leitura externa A16, B20, C9; QA PENDENTE (R2)) | `### Reembolso nas movimentações e comunicação na dispensa de novo ato (Decreto 10.835/2021, arts. 10, 17 a 22, 24, 25 e 30-A, parágrafo único)` |
| C3.3-11 Requisição pela Justiça Eleitoral: limites, exceções e encerramento (Lei 6.999/1982, art. 2º, §§ 1º e 2º; art. 3º, §§ 1º a 3º; art. 4º, parágrafo único) — acréscimo da v2 (leitura externa A15, B21; QA PENDENTE (R2)) | `### Requisição pela Justiça Eleitoral: limites, exceções e encerramento (Lei 6.999/1982, art. 2º, §§ 1º e 2º; art. 3º, §§ 1º a 3º; art. 4º, parágrafo único)` |
| Folha 3.4 — Regime jurídico dos servidores públicos federais (Lei 8.112/1990) | `## 3.4 REGIME JURÍDICO DOS SERVIDORES PÚBLICOS FEDERAIS (LEI 8.112/1990 E SUAS ALTERAÇÕES)` |
| C3.4-01 Âmbito, provimento e formas de provimento (Lei 8.112/1990, arts. 1º, 6º, 7º e 8º) | `### Âmbito, provimento e formas de provimento (Lei 8.112/1990, arts. 1º, 6º, 7º e 8º)` |
| C3.4-02 Posse e exercício (Lei 8.112/1990, arts. 13 a 16) | `### Posse e exercício (Lei 8.112/1990, arts. 13 a 16)` |
| C3.4-03 Estágio probatório e estabilidade: três textos, três referenciais (Lei 8.112/1990, arts. 20 a 22 e 34; CF, art. 41; Decreto 12.374/2025, art. 2º) | `### Estágio probatório e estabilidade: três textos, três referenciais (Lei 8.112/1990, arts. 20 a 22 e 34; CF, art. 41; Decreto 12.374/2025, art. 2º)` |
| C3.4-04 Readaptação e reversão (Lei 8.112/1990, arts. 24 a 27) | `### Readaptação e reversão (Lei 8.112/1990, arts. 24 a 27)` |
| C3.4-05 Reintegração, recondução, disponibilidade e aproveitamento (Lei 8.112/1990, arts. 28 a 32) | `### Reintegração, recondução, disponibilidade e aproveitamento (Lei 8.112/1990, arts. 28 a 32)` |
| C3.4-06 Vacância e exoneração (Lei 8.112/1990, arts. 33 a 35) | `### Vacância e exoneração (Lei 8.112/1990, arts. 33 a 35)` |
| C3.4-07 Remoção e redistribuição (Lei 8.112/1990, arts. 36 e 37) | `### Remoção e redistribuição (Lei 8.112/1990, arts. 36 e 37)` |
| C3.4-08 Licenças e afastamentos; cessão do art. 93 (Lei 8.112/1990, arts. 81 a 96-A) | `### Licenças e afastamentos; cessão do art. 93 (Lei 8.112/1990, arts. 81 a 96-A)` |
| C3.4-09 Direito de petição (Lei 8.112/1990, arts. 104 a 115) | `### Direito de petição (Lei 8.112/1990, arts. 104 a 115)` |
| C3.4-10 Acumulação na lei (Lei 8.112/1990, arts. 118 a 120) | `### Acumulação na lei (Lei 8.112/1990, arts. 118 a 120)` |
| C3.4-11 Seguridade social do servidor (Lei 8.112/1990, arts. 183 a 185) | `### Seguridade social do servidor (Lei 8.112/1990, arts. 183 a 185)` |
| C3.4-12 Posse, exercício, jornada e substituição: regras complementares (Lei 8.112/1990, art. 13, §§ 2º e 3º; art. 15, §§ 3º e 4º; art. 19; arts. 38 e 39) — acréscimo da v2 (leitura externa A6, B6, B7, B8, B9, C11; QA PENDENTE (R2)) | `### Posse, exercício, jornada e substituição: regras complementares (Lei 8.112/1990, art. 13, §§ 2º e 3º; art. 15, §§ 3º e 4º; art. 19; arts. 38 e 39)` |
| C3.4-13 Excedente, licenças no estágio probatório e ajuda de custo na remoção (Lei 8.112/1990, art. 24, § 2º; art. 25, II, e, e § 3º; art. 20, §§ 4º e 5º; art. 36, parágrafo único, II e III; art. 53, caput e § 3º) — acréscimo da v2 (leitura externa A7, B5, B10, B11, B12; QA PENDENTE (R2)) | `### Excedente, licenças no estágio probatório e ajuda de custo na remoção (Lei 8.112/1990, art. 24, § 2º; art. 25, II, e, e § 3º; art. 20, §§ 4º e 5º; art. 36, parágrafo único, II e III; art. 53, caput e § 3º)` |
| C3.4-14 Vencimento, remuneração, descontos e vantagens (Lei 8.112/1990, arts. 40, 41, 44, 46, 49, 51, 58 e 76-A) — acréscimo da v2 (leitura externa A4, A5, B13, C12; QA PENDENTE (R2)) | `### Vencimento, remuneração, descontos e vantagens (Lei 8.112/1990, arts. 40, 41, 44, 46, 49, 51, 58 e 76-A)` |
| C3.4-15 Férias (Lei 8.112/1990, arts. 77 a 80) — acréscimo da v2 (leitura externa B14, C13; QA PENDENTE (R2)) | `### Férias (Lei 8.112/1990, arts. 77 a 80)` |
| C3.4-16 Licenças e afastamentos específicos (Lei 8.112/1990, arts. 82 a 84, 86, 87, 92 e 96-A) — acréscimo da v2 (leitura externa A8, A9, A10, B15, B16, C14; QA PENDENTE (R2)) | `### Licenças e afastamentos específicos (Lei 8.112/1990, arts. 82 a 84, 86, 87, 92 e 96-A)` |
| C3.4-17 Concessões e contagem de tempo de serviço (Lei 8.112/1990, arts. 97 a 100, 102 e 103) — acréscimo da v2 (leitura externa A11, A12, B17, C15; QA PENDENTE (R2)) | `### Concessões e contagem de tempo de serviço (Lei 8.112/1990, arts. 97 a 100, 102 e 103)` |
| C3.4-18 Direito de petição: recurso, efeitos e prescrição (Lei 8.112/1990, art. 107, §§ 1º e 2º; art. 109, parágrafo único; art. 110, parágrafo único; arts. 111 e 112) — acréscimo da v2 (leitura externa A13, A14, B18, B19; QA PENDENTE (R2)) | `### Direito de petição: recurso, efeitos e prescrição (Lei 8.112/1990, art. 107, §§ 1º e 2º; art. 109, parágrafo único; art. 110, parágrafo único; arts. 111 e 112)` |
| C3.4-19 Benefícios do Plano de Seguridade Social: requisitos (Lei 8.112/1990, arts. 196, 202, 203, 207, 208, 226 e 229) — acréscimo da v2 (leitura externa C16, em parte; QA PENDENTE (R2)) | `### Benefícios do Plano de Seguridade Social: requisitos (Lei 8.112/1990, arts. 196, 202, 203, 207, 208, 226 e 229)` |
| Folha 4.1 — Fontes e princípios | `## 4.1 FONTES E PRINCÍPIOS` |
| C4.1-01 "Fontes" do direito disciplinar e o dever de apurar (Lei 8.112, art. 143, caput) | `### "Fontes" do direito disciplinar e o dever de apurar (Lei 8.112, art. 143, caput)` |
| C4.1-02 Dosimetria da penalidade (Lei 8.112, art. 128, caput) | `### Dosimetria da penalidade (Lei 8.112, art. 128, caput)` |
| C4.1-03 Fundamento e causa no ato de imposição (Lei 8.112, art. 128, parágrafo único) | `### Fundamento e causa no ato de imposição (Lei 8.112, art. 128, parágrafo único)` |
| C4.1-04 Independência das instâncias (Lei 8.112, arts. 121 e 125) | `### Independência das instâncias (Lei 8.112, arts. 121 e 125)` |
| C4.1-05 Absolvição criminal e responsabilidade administrativa (Lei 8.112, art. 126) | `### Absolvição criminal e responsabilidade administrativa (Lei 8.112, art. 126)` |
| C4.1-06 Critérios do processo administrativo (I): ética, adequação, motivação, formalidades e formas simples (Lei 9.784, art. 2º, parágrafo único, IV, VI, VII, VIII e IX) | `### Critérios do processo administrativo (I): ética, adequação, motivação, formalidades e formas simples (Lei 9.784, art. 2º, parágrafo único, IV, VI, VII, VIII e IX)` |
| C4.1-07 Critérios do processo administrativo (II): garantias e despesas processuais (Lei 9.784, art. 2º, parágrafo único, X e XI) | `### Critérios do processo administrativo (II): garantias e despesas processuais (Lei 9.784, art. 2º, parágrafo único, X e XI)` |
| C4.1-08 Princípios do caput do art. 2º (Lei 9.784) | `### Princípios do caput do art. 2º (Lei 9.784)` |
| C4.1-09 Aplicação subsidiária da Lei 9.784 aos processos específicos (art. 69) | `### Aplicação subsidiária da Lei 9.784 aos processos específicos (art. 69)` |
| C4.1-10 Dever funcional como fonte da advertência (Lei 8.112, art. 129, caput, só a proposição da fonte) | `### Dever funcional como fonte da advertência (Lei 8.112, art. 129, caput, só a proposição da fonte)` |
| Folha 4.2 — Ilícito de direito administrativo disciplinar | `## 4.2 ILÍCITO DE DIREITO ADMINISTRATIVO DISCIPLINAR` |
| C4.2-01 O ilícito disciplinar e onde estão os tipos (Lei 8.112, arts. 116, 117 e 132) | `### O ilícito disciplinar e onde estão os tipos (Lei 8.112, arts. 116, 117 e 132)` |
| C4.2-02 Deveres do servidor (Lei 8.112, art. 116) | `### Deveres do servidor (Lei 8.112, art. 116)` |
| C4.2-03 Proibições (Lei 8.112, art. 117) | `### Proibições (Lei 8.112, art. 117)` |
| C4.2-04 Responsabilidades civil, penal e civil-administrativa e proteção de quem comunica (Lei 8.112, arts. 121 a 124 e 126-A) | `### Responsabilidades civil, penal e civil-administrativa e proteção de quem comunica (Lei 8.112, arts. 121 a 124 e 126-A)` |
| C4.2-05 Rol de penalidades (Lei 8.112, art. 127) | `### Rol de penalidades (Lei 8.112, art. 127)` |
| C4.2-06 Advertência (Lei 8.112, art. 129, caput, penalidade) | `### Advertência (Lei 8.112, art. 129, caput, penalidade)` |
| C4.2-07 Suspensão (Lei 8.112, art. 130) | `### Suspensão (Lei 8.112, art. 130)` |
| C4.2-08 Cancelamento do registro das penalidades (Lei 8.112, art. 131) | `### Cancelamento do registro das penalidades (Lei 8.112, art. 131)` |
| C4.2-09 Demissão (Lei 8.112, arts. 132 e 136) | `### Demissão (Lei 8.112, arts. 132 e 136)` |
| C4.2-10 Abandono de cargo e inassiduidade habitual (Lei 8.112, arts. 138 e 139) | `### Abandono de cargo e inassiduidade habitual (Lei 8.112, arts. 138 e 139)` |
| C4.2-11 Destituição de cargo em comissão (Lei 8.112, art. 135) | `### Destituição de cargo em comissão (Lei 8.112, art. 135)` |
| C4.2-12 Competência para aplicar as penalidades (Lei 8.112, art. 141) | `### Competência para aplicar as penalidades (Lei 8.112, art. 141)` |
| C4.2-13 Prescrição da ação disciplinar (Lei 8.112, art. 142) | `### Prescrição da ação disciplinar (Lei 8.112, art. 142)` |
| Folha 4.3 — Procedimentos disciplinares | `## 4.3 PROCEDIMENTOS DISCIPLINARES DA ADMINISTRAÇÃO PÚBLICA` |
| C4.3-01 Apuração por autoridade de outro órgão (Lei 8.112, art. 143, § 3º) | `### Apuração por autoridade de outro órgão (Lei 8.112, art. 143, § 3º)` |
| C4.3-02 Denúncia (Lei 8.112, art. 144) | `### Denúncia (Lei 8.112, art. 144)` |
| C4.3-03 Sindicância (Lei 8.112, arts. 145 e 154) | `### Sindicância (Lei 8.112, arts. 145 e 154)` |
| C4.3-04 Obrigatoriedade do processo disciplinar (Lei 8.112, art. 146) | `### Obrigatoriedade do processo disciplinar (Lei 8.112, art. 146)` |
| C4.3-05 Afastamento preventivo (Lei 8.112, art. 147) | `### Afastamento preventivo (Lei 8.112, art. 147)` |
| C4.3-06 Processo disciplinar: conceito, fases e prazo (Lei 8.112, arts. 148, 151 e 152) | `### Processo disciplinar: conceito, fases e prazo (Lei 8.112, arts. 148, 151 e 152)` |
| C4.3-07 Comissão do processo disciplinar (Lei 8.112, arts. 149 e 150) | `### Comissão do processo disciplinar (Lei 8.112, arts. 149 e 150)` |
| C4.3-08 Inquérito administrativo: instrução e provas (Lei 8.112, arts. 153 a 160) | `### Inquérito administrativo: instrução e provas (Lei 8.112, arts. 153 a 160)` |
| C4.3-09 Indiciação, citação e defesa (Lei 8.112, arts. 161 a 164) | `### Indiciação, citação e defesa (Lei 8.112, arts. 161 a 164)` |
| C4.3-10 Relatório e julgamento (Lei 8.112, arts. 165 a 168) | `### Relatório e julgamento (Lei 8.112, arts. 165 a 168)` |
| C4.3-11 Nulidade, prescrição e outros atos do julgamento (Lei 8.112, arts. 169 a 173) | `### Nulidade, prescrição e outros atos do julgamento (Lei 8.112, arts. 169 a 173)` |
| C4.3-12 Revisão do processo disciplinar (Lei 8.112, arts. 174 a 182) | `### Revisão do processo disciplinar (Lei 8.112, arts. 174 a 182)` |
| C4.3-13 Rito sumário: acumulação ilegal, abandono de cargo e inassiduidade habitual (Lei 8.112, arts. 133 e 140) | `### Rito sumário: acumulação ilegal, abandono de cargo e inassiduidade habitual (Lei 8.112, arts. 133 e 140)` |
| C4.3-14 Inquérito: intimação de testemunhas, acareação, interrogatório, sanidade mental, citação e endereço (Lei 8.112, arts. 157, 158, § 2º, 159, §§ 1º e 2º, 160, parágrafo único, 161, § 4º, e 162) — acréscimo da v2 (leitura externa B30, C22; QA PENDENTE (R2)) | `### Inquérito: intimação de testemunhas, acareação, interrogatório, sanidade mental, citação e endereço (Lei 8.112, arts. 157, 158, § 2º, 159, §§ 1º e 2º, 160, parágrafo único, 161, § 4º, e 162)` |
| C4.3-15 Julgamento: alçada e pluralidade de indiciados (Lei 8.112, art. 167, caput e §§ 1º e 2º) — acréscimo da v2 (leitura externa B31, C23; QA PENDENTE (R2)) | `### Julgamento: alçada e pluralidade de indiciados (Lei 8.112, art. 167, caput e §§ 1º e 2º)` |
| C4.3-16 Acumulação ilegal: opção tempestiva e má-fé (Lei 8.112, art. 133, §§ 5º e 6º) — acréscimo da v2 (leitura externa B23, B24; QA PENDENTE (R2)) | `### Acumulação ilegal: opção tempestiva e má-fé (Lei 8.112, art. 133, §§ 5º e 6º)` |
| Folha 4.4 — Processo administrativo federal (Lei 9.784/1999) | `## 4.4 PROCESSO ADMINISTRATIVO FEDERAL (LEI Nº 9.784/1999 E SUAS ALTERAÇÕES)` |
| C4.4-01 Âmbito e definições (Lei 9.784, art. 1º) | `### Âmbito e definições (Lei 9.784, art. 1º)` |
| C4.4-02 Direitos e deveres do administrado (Lei 9.784, arts. 3º e 4º) | `### Direitos e deveres do administrado (Lei 9.784, arts. 3º e 4º)` |
| C4.4-03 Início do processo e requerimento (Lei 9.784, arts. 5º a 8º) | `### Início do processo e requerimento (Lei 9.784, arts. 5º a 8º)` |
| C4.4-04 Interessados e capacidade (Lei 9.784, arts. 9º e 10) | `### Interessados e capacidade (Lei 9.784, arts. 9º e 10)` |
| C4.4-05 Competência: delegação, avocação e início do processo (Lei 9.784, arts. 13, I e III, 14, caput e § 1º, 16 e 17) | `### Competência: delegação, avocação e início do processo (Lei 9.784, arts. 13, I e III, 14, caput e § 1º, 16 e 17)` |
| C4.4-06 Impedimento e suspeição (Lei 9.784, arts. 18 a 21) | `### Impedimento e suspeição (Lei 9.784, arts. 18 a 21)` |
| C4.4-07 Forma, tempo e lugar dos atos (Lei 9.784, arts. 22 a 25) | `### Forma, tempo e lugar dos atos (Lei 9.784, arts. 22 a 25)` |
| C4.4-08 Comunicação dos atos (Lei 9.784, arts. 26 a 28) | `### Comunicação dos atos (Lei 9.784, arts. 26 a 28)` |
| C4.4-09 Instrução (Lei 9.784, arts. 29 a 47, exceto o art. 42) | `### Instrução (Lei 9.784, arts. 29 a 47, exceto o art. 42)` |
| C4.4-10 Dever de decidir (Lei 9.784, arts. 48 e 49) | `### Dever de decidir (Lei 9.784, arts. 48 e 49)` |
| C4.4-11 Decisão coordenada (Lei 9.784, arts. 49-A a 49-G) | `### Decisão coordenada (Lei 9.784, arts. 49-A a 49-G)` |
| C4.4-12 Desistência e extinção do processo (Lei 9.784, arts. 51 e 52) | `### Desistência e extinção do processo (Lei 9.784, arts. 51 e 52)` |
| C4.4-13 Decadência e convalidação: os parágrafos do art. 54 | `### Decadência e convalidação: os parágrafos do art. 54` |
| C4.4-14 Recurso administrativo (Lei 9.784, arts. 56 a 64) | `### Recurso administrativo (Lei 9.784, arts. 56 a 64)` |
| C4.4-15 Revisão de processo sancionador (Lei 9.784, art. 65) | `### Revisão de processo sancionador (Lei 9.784, art. 65)` |
| C4.4-16 Prazos (Lei 9.784, arts. 66 e 67) | `### Prazos (Lei 9.784, arts. 66 e 67)` |
| C4.4-17 Sanções (art. 68) e prioridade na tramitação (art. 69-A) | `### Sanções (art. 68) e prioridade na tramitação (art. 69-A)` |
| C4.4-18 Participação de terceiros e reunião conjunta (Lei 9.784, arts. 31 a 35) — acréscimo da v2 (leitura externa A21, B34, C25; QA PENDENTE (R2)) | `### Participação de terceiros e reunião conjunta (Lei 9.784, arts. 31 a 35)` |
| C4.4-19 Instrução: complementos (Lei 9.784, arts. 29, §§ 1º e 2º, 37, 43, 45, 46 e 47) — acréscimo da v2 (leitura externa A22, B36, C26 em parte; QA PENDENTE (R2)) | `### Instrução: complementos (Lei 9.784, arts. 29, §§ 1º e 2º, 37, 43, 45, 46 e 47)` |
| C4.4-20 Decisão coordenada: definição, documentos, dissenso e ata (Lei 9.784, arts. 49-A, § 1º, 49-E, 49-F e 49-G) — acréscimo da v2 (leitura externa C29; QA PENDENTE (R2)) | `### Decisão coordenada: definição, documentos, dissenso e ata (Lei 9.784, arts. 49-A, § 1º, 49-E, 49-F e 49-G)` |
| C4.4-21 Recurso não conhecido (Lei 9.784, art. 63, caput, II, §§ 1º e 2º; art. 53 por remissão) — acréscimo da v2 (leitura externa A24, B39; QA PENDENTE (R2)) | `### Recurso não conhecido (Lei 9.784, art. 63, caput, II, §§ 1º e 2º; art. 53 por remissão)` |

Regras gerais do curso: "- Definição:" → quadro DEFINIÇÃO (em lista, sem linha em branco, quando a definição tem 3 ou mais frases: operação 4; em parágrafo único nos demais casos); quadro BASE LEGAL em lista com os dispositivos que o próprio título do bloco cita entre parênteses ("(CF, art. 37, VI, VII e VIII; Lei 8.112/1990, art. 5º, § 2º)" → duas linhas; dispositivo sem norma no título herda a norma anterior do mesmo parêntese); nos blocos cujo título não traz norma e artigo juntos (C3.2-07, C4.1-08, C4.1-09, C4.4-13) usam-se os dispositivos da lista "[Desfeita por: …]" do próprio bloco, sem os comentários entre parênteses; em C4.1-10, C4.2-06 e C4.4-17 a lista foi fixada à mão com o que o bloco cita ("Lei 8.112, art. 129, caput"; "Lei 9.784/1999, art. 68" e "art. 69-A"). "- Exemplo (Legislativo, hipotético):" → EXEMPLO PARLAMENTAR (o canônico já termina cada exemplo com "O exemplo é hipotético…": mantido, sem acréscimo); "- Pegadinha provável: … [Desfeita por: X]" → PEGADINHA PROVÁVEL com "Base: X". Código de bloco ("C3.1-01 ") removido do título; sufixo " — acréscimo da v2 (leitura externa …; QA PENDENTE (R2))" removido (30 blocos). Títulos `##`: texto do edital em maiúsculas (nenhum passa de 90 caracteres, então não há corte no primeiro ":"). Resumo: seção 2 inteira (as duas páginas, "Item 3" e "Item 4", em sequência, sem os subtítulos "### Resumo do item N"). Pares: seção 3, 46 (26 do item 3 e 20 do item 4); `a`/`b` = termos do campo "Par" (a = primeiro; b = demais unidos por " × ", caso de P-01 e P-69); `como` = coluna Diferença + " Como a banca troca: " + coluna "Como a banca troca"; a coluna Base não entra. Pegadinhas: seção 4, 114, sem número, sem código do bloco e sem marca de versão; " — Dispositivo: X" vira " Base: X"; `itemEdital` pela folha do bloco ([C3.3-06; C3.3-11] e [C4.3-07; C4.3-08] → a folha comum, 3.3 e 4.3).

## 3. Deleções e trocas (cada uma registrada)
Tipos: deleção de marca (v2, R2, QA PENDENTE, leitura externa, Anexo N, REVERIFICAR, códigos de bloco, de par e de item do banco, "núcleo"/"complementar" do mapa); deleção de frase inteira ou de oração (processo, "[SEM FONTE]", cobertura do lote, remissão a outro lote ou a outro bloco); troca mínima (op. 6); troca de rótulo (operação 2).

Contagem por tipo (sem as da errata, seção "Errata de forma"): deleção de frase inteira: 56; deleção de marca: 70; deleção de oração de processo: 23; pontuação (nenhuma palavra alterada): 14; troca de rótulo: 223; troca mínima (op. 6): 4.

1. [curso C3.0-01 (título)] deleção de oração de processo: `(curso curto; sem item, sem par e sem pegadinha próprios)` → (nada). Motivo: nota de produção no título ("curso curto; sem item, sem par e sem pegadinha próprios"; seção 6).
2. [curso C3.0-01 (texto)] deleção de oração de processo: `, sem texto próprio no Anexo N` → (nada). Motivo: cita o Anexo N (seção 6); fica "são rótulos de curso; o conteúdo normativo está na CF…".
3. [curso C3.0-01 (texto)] deleção de frase inteira: `Sobre classificação doutrinária: [SEM FONTE — não afirmar]; nenhum item a julga.` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
4. [curso C3.1-02 (definição)] deleção de marca: `Nota REVERIFICAR: a alínea b` → `Nota: a alínea b`. Motivo: marca REVERIFICAR (seção 6); o conteúdo da nota (redação da EC 138/2025 vigente; redação anterior superada) é mantido.
5. [curso C3.1-05 (definição)] deleção de frase inteira: `Nenhum item deste lote julga o art. 40, § 4º, ou o § 5º-A.` → (nada). Motivo: fala do lote/da produção (cobertura de itens, remissão a outro lote ou ao lote); não é conteúdo para a candidata (seção 6).
6. [curso C3.1-06 (definição)] troca mínima (op. 6): `ver C3.4-03, que traz` → `ver o item 3.4, que traz`. Motivo: o código de bloco C3.4-03 é referência de produção (seção 6); trocado por "o item 3.4" (o curso do item 3.4 traz os três textos; como no exemplo "(subitem 1.0)" → "do item 1" da seção 7, op. 6).
7. [curso C3.1-09 (título)] deleção de marca: `— acréscimo da v2 (leitura externa A2, A3, B1, B2, C2; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
8. [curso C3.1-09 (definição)] deleção de frase inteira: `Anexo N: art. 37, VI a VIII, núcleo 3.1; art. 5º, § 2º, núcleo 3.4 e 3.2.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
9. [curso C3.1-09 (definição)] deleção de frase inteira: `O inciso VII é citado só pela letra: o conteúdo da lei específica não foi aberto neste material ([SEM FONTE — não afirmar]).` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
10. [curso C3.1-10 (título)] deleção de marca: `— acréscimo da v2 (leitura externa B3, B4, C3, C5; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
11. [curso C3.1-10 (definição)] deleção de frase inteira: `Anexo N: art. 37, XI e §§ 10 a 13, núcleo 3.1; §§ 9º e 14, complementar 3.1.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
12. [curso C3.1-11 (título)] deleção de marca: `— acréscimo da v2 (leitura externa C4; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
13. [curso C3.1-11 (definição)] deleção de oração de processo: `(o texto desses incisos do art. 7º não foi aberto neste material: [SEM FONTE — não afirmar])` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); fica "…XXII e XXX, podendo a lei estabelecer requisitos diferenciados…".
14. [curso C3.1-11 (definição)] deleção de oração de processo: `(subsídio, já em C3.1-03)` → `(subsídio)`. Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
15. [curso C3.1-11 (definição)] deleção de frase inteira: `O caput do art. 39 segue como em C3.1-03 (remissão a ação no STF; efeito não conferido).` → (nada). Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6); a frase só remete a outro bloco (a nota sobre a remissão a ação no STF está no bloco da remuneração, subsídio e teto).
16. [curso C3.1-11 (definição)] deleção de frase inteira: `Anexo N: §§ 1º, I a III, e 3º, núcleo 3.1 e complementar 3.2; demais, núcleo 3.1.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
17. [curso C3.1-12 (título)] deleção de marca: `— acréscimo da v2 (leitura externa C6; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
18. [curso C3.1-12 (definição)] deleção de marca: `Nota (REVERIFICAR, EC 140/2026)` → `Nota (EC 140/2026)`. Motivo: marca REVERIFICAR (seção 6).
19. [curso C3.1-12 (definição)] deleção de oração de processo: `; ver C3.1-05 (redação posterior ao edital` → `(redação posterior ao edital`. Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6); fica "…não são tratados neste bloco (redação posterior ao edital, registrada e não incorporada).".
20. [curso C3.1-12 (definição)] deleção de frase inteira: `Anexo N: todos os dispositivos citados, núcleo 3.1.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
21. [curso C3.2-02 (definição)] deleção de marca: `(ver C3.2-07)` → (nada). Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
22. [curso C3.2-04 (definição)] deleção de frase inteira: `A Lei 8.745/1993, que regula a contratação temporária, não consta do Anexo N: [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); a frase também cita o Anexo N.
23. [curso C3.2-07 (definição)] deleção de marca: `(Anexo N, seção 3)` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
24. [curso C3.2-07 (definição)] deleção de frase inteira: `A classificação de agentes públicos (agentes políticos, honoríficos e outros) é rótulo doutrinário, sem texto próprio no Anexo N: [SEM FONTE — não afirmar]; nenhum item a julga.` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); a frase também cita o Anexo N.
25. [curso C3.3-01 (definição)] deleção de frase inteira: `O Anexo N não traz norma que aplique o Decreto 10.835 à Câmara dos Deputados: [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); a frase também cita o Anexo N.
26. [curso C3.3-02 (definição)] deleção de frase inteira: `O Anexo N localizou prerrogativa expressa de requisitar só na Lei 9.007/1995 (Presidência da República) e na Lei 6.999/1982 (Justiça Eleitoral); sobre qualquer outro órgão requisitante: [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); a frase é relato da busca do Anexo N e termina na marca.
27. [curso C3.3-08 (definição)] deleção de marca: `Decreto 12.374/2025 (REVERIFICAR; norma de 2025, vigente)` → `Decreto 12.374/2025 (norma de 2025, vigente)`. Motivo: marca REVERIFICAR (seção 6).
28. [curso C3.3-08 (definição)] deleção de frase inteira: `Que o Decreto 12.374 se aplique à Câmara dos Deputados: [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
29. [curso C3.3-10 (título)] deleção de marca: `— acréscimo da v2 (leitura externa A16, B20, C9; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
30. [curso C3.3-10 (definição)] deleção de marca: `ônus do ressarcimento (núcleo 3.3). Art. 17` → `ônus do ressarcimento. Art. 17`. Motivo: indicação de "núcleo"/"complementar" do mapa normativo (nota de produção; seção 6).
31. [curso C3.3-10 (definição)] deleção de marca: `Constituição (complementar 3.3). Art. 18` → `Constituição. Art. 18`. Motivo: indicação de "núcleo"/"complementar" do mapa normativo (nota de produção; seção 6).
32. [curso C3.3-10 (definição)] deleção de oração de processo: `(os incisos VI e VII não foram usados)` → (nada). Motivo: fala do lote/da produção (cobertura de itens, remissão a outro lote ou ao lote); não é conteúdo para a candidata (seção 6) (cobertura de incisos).
33. [curso C3.3-10 (definição)] deleção de marca: `Art. 30-A, parágrafo único (núcleo 3.3): nas` → `Art. 30-A, parágrafo único: nas`. Motivo: indicação de "núcleo"/"complementar" do mapa normativo (nota de produção; seção 6).
34. [curso C3.3-10 (definição)] deleção de marca: `(art. 30-A, caput, I a III, em C3.3-04)` → `(art. 30-A, caput, I a III)`. Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
35. [curso C3.3-10 (definição)] deleção de frase inteira: `O parágrafo único do art. 22 e o art. 23 remetem ao ato conjunto do art. 32, não aberto: [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
36. [curso C3.3-10 (definição)] deleção de frase inteira: `Anexo N: arts. 17 a 25, complementar 3.3.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
37. [curso C3.3-11 (título)] deleção de marca: `— acréscimo da v2 (leitura externa A15, B21; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
38. [curso C3.3-11 (definição)] deleção de frase inteira: `Anexo N: todos os dispositivos citados, núcleo 3.3.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
39. [curso C3.3-11 (definição)] deleção de frase inteira: `A Lei 6.999 traz a prerrogativa expressa de requisitar da Justiça Eleitoral; sobre a Câmara dos Deputados: [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
40. [curso C3.4-03 (definição)] deleção de marca: `Decreto 12.374/2025 (REVERIFICAR), art. 2º, caput` → `Decreto 12.374/2025, art. 2º, caput`. Motivo: marca REVERIFICAR (seção 6).
41. [curso C3.4-03 (definição)] deleção de frase inteira: `A conciliação entre esses textos é matéria de doutrina e jurisprudência não aberta neste material — [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); ficam os três textos, cada um no seu referencial, sem conciliação.
42. [curso C3.4-05 (definição)] deleção de oração de processo: `(ponto bloqueado do BQ-0150; só curso)` → (nada). Motivo: fala do lote/da produção (cobertura de itens, remissão a outro lote ou ao lote); não é conteúdo para a candidata (seção 6); cita item do banco (BQ-0150).
43. [curso C3.4-06 (definição)] deleção de oração de processo: `(parte B deste lote)` → (nada). Motivo: fala do lote/da produção (cobertura de itens, remissão a outro lote ou ao lote); não é conteúdo para a candidata (seção 6); fica "é penalidade; aqui, só como causa de vacância (art. 33, II).".
44. [curso C3.4-08 (definição)] deleção de oração de processo: `(ponto bloqueado do BQ-0126; só curso)` → (nada). Motivo: fala do lote/da produção (cobertura de itens, remissão a outro lote ou ao lote); não é conteúdo para a candidata (seção 6); cita item do banco (BQ-0126).
45. [curso C3.4-11 (definição)] deleção de frase inteira: `Os arts. 186 a 231 não foram usados em item.` → (nada). Motivo: fala do lote/da produção (cobertura de itens, remissão a outro lote ou ao lote); não é conteúdo para a candidata (seção 6) (cobertura de itens).
46. [curso C3.4-12 (título)] deleção de marca: `— acréscimo da v2 (leitura externa A6, B6, B7, B8, B9, C11; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
47. [curso C3.4-12 (definição)] deleção de oração de processo: `por opção de remuneração; C3.2-03 e P-18)` → `por opção de remuneração)`. Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
48. [curso C3.4-12 (definição)] deleção de frase inteira: `Anexo N: todos os dispositivos citados, núcleo 3.4.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
49. [curso C3.4-13 (título)] deleção de marca: `— acréscimo da v2 (leitura externa A7, B5, B10, B11, B12; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
50. [curso C3.4-13 (definição)] deleção de marca: `(já em C3.4-03)` → (nada). Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
51. [curso C3.4-13 (definição)] deleção de frase inteira: `O prazo do estágio (24 meses na lei; 36 no decreto remetido) segue o tratamento de C3.4-03, sem afirmação nova.` → (nada). Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6); a frase só remete ao bloco do estágio probatório.
52. [curso C3.4-13 (definição)] deleção de frase inteira: `Anexo N: todos os dispositivos citados, núcleo 3.4 (art. 20, §§ 4º e 5º, também complementar 3.2).` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
53. [curso C3.4-14 (título)] deleção de marca: `— acréscimo da v2 (leitura externa A4, A5, B13, C12; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
54. [curso C3.4-14 (definição)] deleção de frase inteira: `O caput do art. 76-A traz remissões a regulamento e a decreto, não abertos: [SEM FONTE — não afirmar] sobre limites e valores.` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
55. [curso C3.4-14 (definição)] deleção de frase inteira: `Anexo N: todos os dispositivos citados, núcleo 3.4.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
56. [curso C3.4-15 (título)] deleção de marca: `— acréscimo da v2 (leitura externa B14, C13; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
57. [curso C3.4-15 (definição)] deleção de frase inteira: `Os arts. 77, 78 e 80 trazem remissão a lei de 1997, não aberta: [SEM FONTE — não afirmar] sobre o seu conteúdo.` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
58. [curso C3.4-15 (definição)] deleção de frase inteira: `Anexo N: todos os dispositivos citados, núcleo 3.4.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
59. [curso C3.4-16 (título)] deleção de marca: `— acréscimo da v2 (leitura externa A8, A9, A10, B15, B16, C14; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
60. [curso C3.4-16 (definição)] deleção de oração de processo: `(o caput traz remissão a decreto, não aberto: [SEM FONTE — não afirmar])` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
61. [curso C3.4-16 (definição)] deleção de frase inteira: `Anexo N: todos os dispositivos citados, núcleo 3.4.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
62. [curso C3.4-17 (título)] deleção de marca: `— acréscimo da v2 (leitura externa A11, A12, B17, C15; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
63. [curso C3.4-17 (definição)] deleção de oração de processo: `(IV; o inciso traz remissão a decreto, não aberto: [SEM FONTE — não afirmar])` → `(IV)`. Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); fica o número do inciso.
64. [curso C3.4-17 (definição)] deleção de frase inteira: `O art. 103 tem, no Anexo N, só os §§ 1º a 3º.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
65. [curso C3.4-17 (definição)] deleção de frase inteira: `Anexo N: todos os dispositivos citados, núcleo 3.4.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
66. [curso C3.4-18 (título)] deleção de marca: `— acréscimo da v2 (leitura externa A13, A14, B18, B19; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
67. [curso C3.4-18 (definição)] deleção de frase inteira: `Complementa C3.4-09 (arts. 106 a 110).` → (nada). Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
68. [curso C3.4-18 (definição)] deleção de frase inteira: `Contraste: a prescrição da ação disciplinar (art. 142) está em C4.2-13; o recurso da Lei 9.784 (arts. 56 a 64), em C4.4-14 (par P-63).` → (nada). Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6); a frase só remete a outros blocos e a um par.
69. [curso C3.4-18 (definição)] deleção de frase inteira: `Anexo N: todos os dispositivos citados, núcleo 3.4.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
70. [curso C3.4-19 (título)] deleção de marca: `— acréscimo da v2 (leitura externa C16, em parte; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
71. [curso C3.4-19 (definição)] deleção de oração de processo: `; a remissão do caput ao Decreto 6.690/2008 não foi aberta: [SEM FONTE — não afirmar] sobre o conteúdo do decreto` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
72. [curso C3.4-19 (definição)] deleção de frase inteira: `Ficam fora deste bloco os arts. 215 e 217 (pensão por morte): o art. 215 remete à Lei 10.887/2004, não aberta ([SEM FONTE — não afirmar]), e o art. 217, cujo texto está no Anexo N, fica fora por escolha de escopo.` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); a frase também cita o Anexo N e trata de escopo de produção.
73. [curso C3.4-19 (definição)] deleção de frase inteira: `O bloco é só de curso (sem item) e complementa o bloco C3.4-11 (arts. 183 a 185).` → (nada). Motivo: fala do lote/da produção (cobertura de itens, remissão a outro lote ou ao lote); não é conteúdo para a candidata (seção 6) ("sem item") e remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
74. [curso C3.4-19 (definição)] deleção de frase inteira: `Anexo N: todos os dispositivos citados, núcleo 3.4.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
75. [curso C4.1-01 (definição)] deleção de oração de processo: `; a classificação doutrinária das fontes é matéria não aberta neste material — [SEM FONTE — não afirmar]` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
76. [curso C4.1-01 (definição)] deleção de frase inteira: `O conteúdo normativo da folha está nos artigos dos blocos C4.1-01 a C4.1-10.` → (nada). Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
77. [curso C4.1-04 (definição)] deleção de frase inteira: `O conteúdo de cada responsabilidade (arts. 122 a 124) está no bloco C4.2-04.` → (nada). Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
78. [curso C4.1-05 (definição)] deleção de oração de processo: `; o efeito de outras formas de absolvição não é tratado neste material — [SEM FONTE — não afirmar]` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); fica "O artigo trata só desse tipo de absolvição.".
79. [curso C4.1-06 (definição)] deleção de frase inteira: `Os incisos I, II, III, V e XIII são pontos do D1, e o inciso XII é ponto do item real BQ-0145; nenhum deles é ponto de item desta folha.` → (nada). Motivo: fala do lote/da produção (cobertura de itens, remissão a outro lote ou ao lote); não é conteúdo para a candidata (seção 6); cita o lote D1 e item do banco (BQ-0145).
80. [curso C4.1-08 (definição)] deleção de oração de processo: `; o fundamento constitucional do contraditório e da ampla defesa no art. 5º, LV, da CF não foi aberto neste material — [SEM FONTE — não afirmar]` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); fica "A ampla defesa e o contraditório constam do rol.".
81. [curso C4.1-10 (definição)] deleção de frase inteira: `A forma escrita e as proibições do art. 117 estão no bloco C4.2-06.` → (nada). Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
82. [curso C4.2-01 (definição)] deleção de oração de processo: `, e a doutrina sobre o conceito não foi aberta neste material — [SEM FONTE — não afirmar]` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); fica "…traz os tipos, e não um artigo de definição.".
83. [curso C4.2-04 (definição)] deleção de frase inteira: `A responsabilidade civil do Estado é matéria de outro lote.` → (nada). Motivo: fala do lote/da produção (cobertura de itens, remissão a outro lote ou ao lote); não é conteúdo para a candidata (seção 6).
84. [curso C4.2-06 (definição)] deleção de oração de processo: `(a fonte do dever está no bloco C4.1-10)` → (nada). Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
85. [curso C4.2-10 (definição)] deleção de marca: `(bloco C4.3-13)` → (nada). Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
86. [curso C4.3-14 (título)] deleção de marca: `— acréscimo da v2 (leitura externa B30, C22; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
87. [curso C4.3-14 (definição)] deleção de oração de processo: `(o caput está em C4.3-08)` → (nada). Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
88. [curso C4.3-14 (definição)] deleção de frase inteira: `Anexo N: todos os dispositivos citados, núcleo 3.4 e 4.3.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
89. [curso C4.3-15 (título)] deleção de marca: `— acréscimo da v2 (leitura externa B31, C23; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
90. [curso C4.3-15 (definição)] deleção de frase inteira: `Os §§ 3º e 4º ficam fora deste bloco (já estão em C4.3-10).` → (nada). Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
91. [curso C4.3-15 (definição)] deleção de frase inteira: `Anexo N: art. 167, caput e §§ 1º e 2º, núcleo 3.4 e 4.3.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
92. [curso C4.3-16 (título)] deleção de marca: `— acréscimo da v2 (leitura externa B23, B24; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
93. [curso C4.3-16 (definição)] deleção de oração de processo: `a penalidade de demissão e a de destituição são as tratadas em C4.2-09 e C4.2-11;` → (nada). Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6); fica "(a cassação de aposentadoria ou disponibilidade, que o texto do § 6º também cita, é a do art. 127, IV, …)".
94. [curso C4.3-16 (definição)] deleção de oração de processo: `e que este lote não usa)` → `)`. Motivo: fala do lote/da produção (cobertura de itens, remissão a outro lote ou ao lote); não é conteúdo para a candidata (seção 6).
95. [curso C4.3-16 (definição)] deleção de marca: `(C4.3-13)` → (nada). Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
96. [curso C4.3-16 (definição)] deleção de frase inteira: `Anexo N: art. 133, §§ 5º e 6º, núcleo 3.4, 4.2 e 4.3.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
97. [curso C4.4-01 (definição)] deleção de frase inteira: `O § 1º e o § 2º, I e II, também são cobrados em outro lote.` → (nada). Motivo: fala do lote/da produção (cobertura de itens, remissão a outro lote ou ao lote); não é conteúdo para a candidata (seção 6).
98. [curso C4.4-05 (definição)] deleção de frase inteira: `Os demais dispositivos da delegação e da avocação (arts. 11, 12, 13, II, 14, §§ 2º e 3º, e 15) são tratados em outro lote.` → (nada). Motivo: fala do lote/da produção (cobertura de itens, remissão a outro lote ou ao lote); não é conteúdo para a candidata (seção 6).
99. [curso C4.4-13 (definição)] deleção de frase inteira: `O caput do art. 54 e os arts. 53 e 55 (anulação, revogação, decadência de cinco anos e convalidação) são tratados em outro lote.` → (nada). Motivo: fala do lote/da produção (cobertura de itens, remissão a outro lote ou ao lote); não é conteúdo para a candidata (seção 6).
100. [curso C4.4-14 (definição)] deleção de frase inteira: `Ficam fora do recorte desta folha o art. 56, § 3º, e os arts. 64-A e 64-B (súmula vinculante).` → (nada). Motivo: fala do lote/da produção (cobertura de itens, remissão a outro lote ou ao lote); não é conteúdo para a candidata (seção 6) (recorte de cobertura).
101. [curso C4.4-18 (título)] deleção de marca: `— acréscimo da v2 (leitura externa A21, B34, C25; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
102. [curso C4.4-18 (definição)] deleção de frase inteira: `Anexo N: arts. 31 a 35, núcleo 4.4.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
103. [curso C4.4-19 (título)] deleção de marca: `— acréscimo da v2 (leitura externa A22, B36, C26 em parte; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
104. [curso C4.4-19 (definição)] deleção de marca: `Art. 36 (já em C4.4-09): cabe` → `Art. 36: cabe`. Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
105. [curso C4.4-19 (definição)] deleção de marca: `Art. 45 (já em C4.4-09): em caso` → `Art. 45: em caso`. Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
106. [curso C4.4-19 (definição)] deleção de frase inteira: `O art. 42 (parecer) é ponto do D1 e não é tratado aqui.` → (nada). Motivo: fala do lote/da produção (cobertura de itens, remissão a outro lote ou ao lote); não é conteúdo para a candidata (seção 6); cita o lote D1.
107. [curso C4.4-19 (definição)] deleção de frase inteira: `Anexo N: todos os dispositivos citados, núcleo 4.4.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
108. [curso C4.4-20 (título)] deleção de marca: `— acréscimo da v2 (leitura externa C29; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
109. [curso C4.4-20 (definição)] deleção de frase inteira: `Complementa C4.4-11.` → (nada). Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
110. [curso C4.4-20 (definição)] deleção de frase inteira: `Anexo N: todos os dispositivos citados, núcleo 4.4.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
111. [curso C4.4-20 (exemplo)] deleção de marca: `(art. 49-A, § 6º, III; C4.4-11)` → `(art. 49-A, § 6º, III)`. Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
112. [curso C4.4-21 (título)] deleção de marca: `— acréscimo da v2 (leitura externa A24, B39; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas).
113. [curso C4.4-21 (definição)] deleção de oração de processo: `(tratado em outro lote)` → (nada). Motivo: fala do lote/da produção (cobertura de itens, remissão a outro lote ou ao lote); não é conteúdo para a candidata (seção 6).
114. [curso C4.4-21 (definição)] deleção de frase inteira: `Complementa C4.4-14 (que traz o caput do art. 63).` → (nada). Motivo: remissão a código de bloco, de par ou de pegadinha do curso (seção 6).
115. [curso C4.4-21 (definição)] deleção de frase inteira: `Anexo N: art. 63, núcleo 4.4.` → (nada). Motivo: referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6).
116. [resumo] deleção de marca: `### Resumo do item 3` → (nada). Motivo: subtítulo de produção da seção 2 do canônico ("uma página por item do edital"); cada página já abre com "**Item 3 — …**".
117. [resumo] deleção de marca: `### Resumo do item 4` → (nada). Motivo: subtítulo de produção da seção 2 do canônico ("uma página por item do edital"); cada página já abre com "**Item 4 — …**".
118. [resumo] deleção de marca: `(EC 138/2025; REVERIFICAR)` → `(EC 138/2025)`. Motivo: marca REVERIFICAR (seção 6).
119. [resumo] deleção de marca: `| Número literal do Anexo N | Dispositivo |` → `| Número literal | Dispositivo |`. Motivo: sai "do Anexo N" do cabeçalho da tabela (seção 6); a tabela é mantida.
120. [resumo] deleção de marca: `(estágio probatório, no referencial do Decreto; REVERIFICAR)` → `(estágio probatório, no referencial do Decreto)`. Motivo: marca REVERIFICAR (seção 6).
121. [par P-06] deleção de marca: `(REVERIFICAR)` → (nada). Motivo: marca REVERIFICAR (seção 6).
122. [par P-06] deleção de frase inteira: `A conciliação entre esses textos é matéria de doutrina e jurisprudência não aberta neste material — [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); ficam os dois referenciais (Lei 8.112 e Decreto) e a estabilidade, cada um na sua norma, sem conciliação.
123. [par P-62] deleção de oração de processo: `, hipótese que este lote não usa` → (nada). Motivo: fala do lote/da produção (cobertura de itens, remissão a outro lote ou ao lote); não é conteúdo para a candidata (seção 6).
124. [pegadinha 36] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
125. [pegadinha 37] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
126. [pegadinha 38] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
127. [pegadinha 39] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
128. [pegadinha 40] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
129. [pegadinha 41] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
130. [pegadinha 42] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
131. [pegadinha 43] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
132. [pegadinha 44] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
133. [pegadinha 45] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
134. [pegadinha 46] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
135. [pegadinha 47] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
136. [pegadinha 48] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
137. [pegadinha 49] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
138. [pegadinha 50] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
139. [pegadinha 104] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
140. [pegadinha 105] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
141. [pegadinha 106] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
142. [pegadinha 107] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
143. [pegadinha 108] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
144. [pegadinha 109] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
145. [pegadinha 110] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
146. [pegadinha 111] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
147. [pegadinha 112] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
148. [pegadinha 113] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
149. [pegadinha 114] deleção de marca: `[acréscimo da v2]` → (nada). Motivo: marca "v2" (seção 6).
150. [justificativa D2-02] pontuação (nenhuma palavra alterada): `Não há troca:` → `Não há troca;`. Motivo: a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula (mesmo tratamento dado no D1, item D1-01, e no D5, item D5-04).
151. [justificativa D2-04] pontuação (nenhuma palavra alterada): `Não há troca:` → `Não há troca;`. Motivo: a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula (mesmo tratamento dado no D1, item D1-01, e no D5, item D5-04).
152. [justificativa D2-08] pontuação (nenhuma palavra alterada): `Não há troca:` → `Não há troca;`. Motivo: a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula (mesmo tratamento dado no D1, item D1-01, e no D5, item D5-04).
153. [justificativa D2-11] pontuação (nenhuma palavra alterada): `Não há troca:` → `Não há troca;`. Motivo: a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula (mesmo tratamento dado no D1, item D1-01, e no D5, item D5-04).
154. [justificativa D2-12] pontuação (nenhuma palavra alterada): `Não há troca:` → `Não há troca;`. Motivo: a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula (mesmo tratamento dado no D1, item D1-01, e no D5, item D5-04).
155. [justificativa D2-14] pontuação (nenhuma palavra alterada): `Não há troca:` → `Não há troca;`. Motivo: a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula (mesmo tratamento dado no D1, item D1-01, e no D5, item D5-04).
156. [justificativa D2-17] pontuação (nenhuma palavra alterada): `Não há troca:` → `Não há troca;`. Motivo: a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula (mesmo tratamento dado no D1, item D1-01, e no D5, item D5-04).
157. [justificativa D2-18] pontuação (nenhuma palavra alterada): `Não há troca:` → `Não há troca;`. Motivo: a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula (mesmo tratamento dado no D1, item D1-01, e no D5, item D5-04).
158. [justificativa D2-22] pontuação (nenhuma palavra alterada): `Não há troca:` → `Não há troca;`. Motivo: a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula (mesmo tratamento dado no D1, item D1-01, e no D5, item D5-04).
159. [justificativa D2-25] pontuação (nenhuma palavra alterada): `Não há troca:` → `Não há troca;`. Motivo: a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula (mesmo tratamento dado no D1, item D1-01, e no D5, item D5-04).
160. [justificativa D2-27] pontuação (nenhuma palavra alterada): `Não há troca:` → `Não há troca;`. Motivo: a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula (mesmo tratamento dado no D1, item D1-01, e no D5, item D5-04).
161. [justificativa D2-34] pontuação (nenhuma palavra alterada): `Não há troca:` → `Não há troca;`. Motivo: a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula (mesmo tratamento dado no D1, item D1-01, e no D5, item D5-04).
162. [justificativa D2-35] pontuação (nenhuma palavra alterada): `Não há troca:` → `Não há troca;`. Motivo: a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula (mesmo tratamento dado no D1, item D1-01, e no D5, item D5-04).
163. [justificativa D2-37] pontuação (nenhuma palavra alterada): `Não há troca:` → `Não há troca;`. Motivo: a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula (mesmo tratamento dado no D1, item D1-01, e no D5, item D5-04).
164. [justificativa D2-59] troca mínima (op. 6): `elemento-isca:` → `elemento que parece trocado:`. Motivo: "elemento-isca" é marca de produção (seção 6); trocado pela expressão equivalente "elemento que parece trocado" (mesma troca do D5); o restante da frase fica igual.
165. [justificativa D2-64] troca mínima (op. 6): `elemento-isca:` → `elemento que parece trocado:`. Motivo: "elemento-isca" é marca de produção (seção 6); trocado pela expressão equivalente "elemento que parece trocado" (mesma troca do D5); o restante da frase fica igual.
166. [justificativa D2-72] troca mínima (op. 6): `elemento-isca:` → `elemento que parece trocado:`. Motivo: "elemento-isca" é marca de produção (seção 6); trocado pela expressão equivalente "elemento que parece trocado" (mesma troca do D5); o restante da frase fica igual.
167. [justificativa D2-74] deleção de marca: `, ponto do D1-16)` → `)`. Motivo: código de item de outro lote ("ponto do D1-16"; seção 6); fica "(art. 1º, § 1º)".

Trocas de rótulo (operação 2): 109 pegadinhas do curso ("[Desfeita por: X]" → "Base: X") e 114 pegadinhas da lista consolidada (" — Dispositivo: X" → " Base: X").

Decisões de leitura que o orquestrador pode querer revisar (nenhuma altera conteúdo normativo):
- Curso do caput 3 (bloco C3.0-01, sem itens, sem par e sem pegadinha): o bloco tem uma única linha de cerca de 55 palavras depois das deleções, sem Definição, Exemplo ou Pegadinha. Não foi possível dar-lhe um tópico próprio (`## 3 AGENTES PÚBLICOS` com `P1-DA-3`) com resumo de 150 palavras sem fato novo; por isso ele vai como PRIMEIRO `###` do `## 3.1 DISPOSIÇÕES CONSTITUCIONAIS APLICÁVEIS`, com o título "Caput 3 — Agentes públicos" (sai a nota de produção "curso curto; sem item, sem par e sem pegadinha próprios"), em parágrafo simples, sem quadros (o original não tem os rótulos). Em consequência `itensEdital` não traz `P1-DA-3` nem `P1-DA-4`, e `topicos` tem as 8 folhas 3.1 a 4.4.
- Estágio probatório e estabilidade (blocos de 3.4, 3.1 e 3.3, par P-06, resumo e tópico 3.4): só a letra de cada norma, cada uma no seu referencial (Lei 8.112, art. 20, caput: 24 meses; CF, art. 41, caput: três anos para a estabilidade; Decreto 12.374/2025, art. 2º, caput: trinta e seis meses). Saíram a frase "A conciliação entre esses textos é matéria de doutrina e jurisprudência não aberta neste material — [SEM FONTE]" (curso 3.4 e par P-06) e a frase de C3.4-13 que remetia ao tratamento do bloco do estágio. O tópico 3.4 não concilia: apresenta os três textos lado a lado.
- Marcas REVERIFICAR (CF, art. 37, XVI, b, EC 138/2025; Decreto 12.374/2025; EC 140/2026): as marcas saíram e o conteúdo foi mantido, como o D5 fez com a Lei 15.471/2026. A posição sobre a EC 140/2026 (posterior ao edital, registrada, não incorporada; vale a redação da EC 103/2019) permanece no curso e no resumo.
- Remissões "folha 3.4" (C3.1-02, C3.1-08), "Nesta folha vale só a proposição da fonte" (C4.1-10) e "edital 13.33" (base de C3.1-05): as de "folha" foram mantidas na primeira entrega e TRATADAS PELA ERRATA DE 20/10/2026 (seção "Errata de forma": "folha" vira "subitem" ou a frase sai); "edital 13.33" segue mantida (não está na lista da seção 6) e os números 3.4 etc. são os dos títulos `##` do curso. As remissões a código de bloco (C3.4-03 etc.), a par (P-18, P-63) e a lote (D1, "outro lote") saíram; só em C3.1-06 ("ver C3.4-03") a troca foi por "o item 3.4", registrada.
- Frases de nota sobre ação no STF ("o compilado remete a ação no STF; efeito não conferido neste material", curso e resumo) foram mantidas: são conteúdo para a candidata (ressalva de que o efeito da decisão não foi conferido) e não constam da lista da seção 6.
- Enunciados começam com "Considere…" ou são frases soltas e trazem a situação no próprio enunciado; o canônico não separa texto-base: `textoBase` "" e `comando` "Julgue o item a seguir." (o canônico só traz "Julgue cada item como Certo ou Errado." no cabeçalho da seção 5.1).
- Pegadinhas G-42 e G-107 trazem dois blocos de origem ([C3.3-06; C3.3-11] e [C4.3-07; C4.3-08]); o `itemEdital` é o da folha comum (P1-DA-3.3 e P1-DA-4.3).
- Tópicos (8, um por `##`, de P1-DA-3.1 a P1-DA-4.4; escritos à mão em D2_topicos_fonte.json): `emUmMinuto` com 3 frases; `resumo` só com fatos, números e dispositivos que estão no curso da folha (a conferência confere que todo número e todo artigo do tópico aparece no curso dela), de 202 a 248 palavras (3.1: 202; 3.2: 248; 3.3: 231; 3.4: 232; 4.1: 231; 4.2: 240; 4.3: 222; 4.4: 242); visuais por tópico: 3.1: baseLegal + tabela; 3.2: tabela + baseLegal; 3.3: compare + baseLegal; 3.4: baseLegal + compare; 4.1: esquema + baseLegal; 4.2: tabela + baseLegal; 4.3: compare + fluxo; 4.4: tabela + baseLegal.
- Visuais pedidos como comparação de três figuras (cargo × emprego × função, na 3.2; advertência × suspensão × demissão, na 4.2): o tipo `compare` só tem dois lados (a, b), então foram feitos como `tabela` (3 e 4 colunas). As comparações de dois lados usam `compare`: requisição × cessão (3.3), remoção × redistribuição (3.4) e sindicância × processo disciplinar (4.3). Prazos e fases em `fluxo` (4.3: 60 dias, defesa de 10 dias, julgamento em 20 dias) e em `tabela` (4.4: arts. 24, 26, § 2º, 44, 49, 56, § 1º, 59 e 66) só os que estão no curso da folha e no mapa normativo.
- `baseLegal` (7 dos 8 tópicos; todos com `literal: true` e `conferido: 2026-10-20`, data da consulta do mapa normativo): o texto de cada dispositivo foi copiado letra a letra da coluna de texto do mapa, inclusive a grafia do compilado ("observados os seguinte fatores", no art. 20, caput, da Lei 8.112) e a nota do compilado do art. 21 ("(prazo 3 anos - vide EMC nº 19)"); a conferência de fidelidade e o validador confirmam a literalidade. No tópico 4.3 não há `baseLegal`: os dois visuais (`compare` e `fluxo`) já trazem os artigos e os prazos, e o limite é de 2 visuais.
- Estágio probatório (tópico 3.4): o `baseLegal` traz lado a lado a letra de cada texto (Lei 8.112, art. 20, caput e art. 21, caput; CF, art. 41, caput; Decreto 12.374/2025, art. 2º, caput), e o resumo e o `emUmMinuto` dizem o que cada norma diz, sem conciliar.

## 4. Itens
- Total 80; C 40 / E 40.
- Por itemEdital: P1-DA-3.1: 10; P1-DA-3.2: 10; P1-DA-3.3: 10; P1-DA-3.4: 10; P1-DA-4.1: 10; P1-DA-4.2: 10; P1-DA-4.3: 10; P1-DA-4.4: 10.
- volatil true: D2-01, D2-28 (as linhas "Marcas:" com REVERIFICAR=sim; as demais trazem REVERIFICAR=não e VOLÁTIL=não).
- Justificativa: linhas 1 e 2 unidas por um espaço; edições: a pontuação "Não há troca:" → "Não há troca;" em 14 itens (nenhuma palavra alterada), a troca mínima "elemento-isca:" → "elemento que parece trocado:" em 3 itens e a deleção de ", ponto do D1-16" em D2-74; as demais são idênticas às duas linhas. As linhas "Difere de …" e "Mecanismo" são campos à parte no canônico e não entram.
- Pares: 46; pegadinhas: 114 (P1-DA-3.1: 12; P1-DA-3.2: 7; P1-DA-3.3: 12; P1-DA-3.4: 19; P1-DA-4.1: 10; P1-DA-4.2: 15; P1-DA-4.3: 18; P1-DA-4.4: 21); tópicos: 8 (P1-DA-3.1, P1-DA-3.2, P1-DA-3.3, P1-DA-3.4, P1-DA-4.1, P1-DA-4.2, P1-DA-4.3, P1-DA-4.4).

## 5. Saída do validador
Comando: `python3 -I saida/gcb/DA_plataforma/scripts/validar_da.py saida/gcb/DA_plataforma/D2_plataforma.json saida/gcb/D2_v2_1.md saida/gcb/D2_anexo_N_mapa_normativo.md`
```
D2_plataforma.json: lote D2; itensEdital 8; blocos ## 8; itens 80 (C 40 / E 40); pares 46; pegadinhas 114; topicos 8
quadros: {'BASE LEGAL': 109, 'DEFINIÇÃO': 109, 'PEGADINHA PROVÁVEL': 109, 'EXEMPLO PARLAMENTAR': 109}
RESULTADO: 0 FALHA, 0 AVISO
```

## 6. Conferência de fidelidade
Comando: `python3 -I saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D2.py`

### 6.0 Registro das edições, conferido contra o canônico

- 394 edições registradas em D2_log_edicoes.json; edições que acrescentam palavra sem declarar, deleção que acrescenta palavra ou "pontuação" que muda palavra: 0.

### 6.1 Curso: palavras do bloco de saída × bloco de origem (com as edições registradas)

Origem = título (com a marca de versão, que o registro manda tirar) + campos do bloco, sem os rótulos "Definição:", "Exemplo (Legislativo, hipotético):" e "Pegadinha provável:"; aplicam-se à origem as edições registradas do bloco. Saída = título + texto dos quadros DEFINIÇÃO, EXEMPLO PARLAMENTAR e PEGADINHA PROVÁVEL (sem os rótulos de quadro e sem a lista BASE LEGAL). Comparação palavra por palavra, na ordem (maiúsculas ignoradas).

- 110 blocos conferidos (109 regulares + o bloco do caput 3, que abre a folha 3.1); blocos com divergência: 0.
- Cabeçalhos `##`: 8, com o texto do edital em maiúsculas; divergências: 0.
- Parágrafos de convenção de produção que não entram ("Cada bloco: …"): 2 registrados, todos existem no canônico: sim.

### 6.2 Resumo (seção 2 do canônico)

- Palavras da origem (com as 5 edições registradas) × palavras da saída: 1712 × 1712; divergência: nenhuma.

### 6.3 Pares

- 46 pares: termos a/b reconstituem a coluna "Par" (a + " × " + b); "como" = Diferença (com as edições registradas) + "Como a banca troca:" + coluna "Como a banca troca"; a coluna Base não entra. Pares com divergência: 0.

### 6.4 Pegadinhas

- 114 pegadinhas: texto = origem com as edições registradas (marca de versão sai; " — Dispositivo:" vira " Base:"); itemEdital = folha do bloco; rótulo = texto do edital. Divergências: 0.

### 6.5 Itens: enunciado, gabarito, itemEdital, volatil e justificativa

- 80 itens (C 40 / E 40): enunciado e gabarito iguais caractere a caractere ao canônico; itemEdital = folha do item; volatil conforme a linha "Marcas" (D2-01, D2-28); justificativa = linhas 1 e 2 com as edições registradas. Divergências: 0.

- Edições registradas aplicadas ao canônico: 394 de 394.

### 6.6 Tópicos

- 8 tópicos: números e artigos dos textos e dos visuais presentes no curso da folha; baseLegal com `literal: true` bate letra a letra com a coluna de texto do mapa normativo e traz a data da consulta (2026-10-20). Problemas: 0.

RESULTADO DA CONFERÊNCIA DE FIDELIDADE: 0 defeito(s).

## Errata de forma — QA final 20/10/2026
Origem: QA final do pacote v1.13 (gbq-cqe, 20/10/2026), achado 1: a palavra de produção "folha" no texto exibido (a candidata não conhece "folha"; o validador passou a acusá-la). Regra da ordem: frase que só fala do processo ou da organização da produção é DELETADA; remissão útil ao estudo vira "subitem". Só forma: nenhum enunciado, gabarito, itemEdital ou id foi tocado. Cada entrada abaixo está também no log de edições (D2_log_edicoes.json) e é conferida pela conferência de fidelidade.

1. [curso C3.0-01 (texto)] deleção de frase inteira: `O caput 3 não é folha. Todo conteúdo cobrável está nas folhas 3.1 a 3.4.` → (nada). Motivo: errata de forma (QA final 20/10/2026, achado 1): as duas frases só falam da organização da produção (o que é "folha" e onde está o conteúdo cobrável); nada de estudo se perde.
2. [curso C3.1-02 (definição)] troca mínima (op. 6): `(contraste, folha 3.4)` → `(contraste, subitem 3.4)`. Motivo: errata de forma (QA final 20/10/2026, achado 1): "folha" é termo de produção (seção 6); a remissão serve ao estudo e passa a "subitem", o número 3.4 é o do `##` do curso.
3. [curso C3.1-08 (definição)] troca mínima (op. 6): `arts. 28 a 32 (folha 3.4)` → `arts. 28 a 32 (subitem 3.4)`. Motivo: errata de forma (QA final 20/10/2026, achado 1): "folha" é termo de produção (seção 6); a remissão serve ao estudo e passa a "subitem", o número 3.4 é o do `##` do curso.
4. [curso C4.1-10 (definição)] deleção de frase inteira: `Nesta folha vale só a proposição da fonte: o dever funcional pode estar previsto em lei, regulamentação ou norma interna.` → (nada). Motivo: errata de forma (QA final 20/10/2026, achado 1): a frase só delimita o recorte da produção ("nesta folha vale só a proposição da fonte") e repete o que a frase anterior (art. 129, caput) e o título do bloco já dizem.

Total: 4 mudanças no D2 (curso). Resumo, pares, pegadinhas, justificativas e tópicos do D2 não tinham a palavra "folha" nem código R/F.

