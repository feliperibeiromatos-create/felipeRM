# D4_registro_formato.md — T-77 (ordem DA 20/10/2026) — 2026-10-20 — gerado por gcb-cpp

Reformatação do Lote D4 (Gestão pública e governança, itens 8 e 9 do edital) para o formato da plataforma (FORMATO_PLATAFORMA_DA.md). Só forma; nenhum conteúdo novo. Gerado por `saida/gcb/DA_plataforma/scripts/formatar_D4.py --registro`; fidelidade por `saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D4.py`.

## 1. Fontes e conferências
- Canônico: saida/gcb/D4_v2_1.md, SHA-256 c1a7a93598e9fd37b2009b9feaca3afd3898fa05f6f66e6de26dd40c2839e5d9 (igual ao esperado c1a7a935…e5d9: o script confere antes de ler e pararia se divergisse).
- Base normativa e de referencial: saida/gcb/D4_anexo_N_mapa_normativo.md (consulta de 20/10/2026), SHA-256 0d98c24969788d2baeb150535b6a7cd538ea856fb64d3d707bc53ede24e5a05f. Usada pelo validador, pelo visual baseLegal (texto copiado por script, letra a letra, da coluna de texto do mapa; `literal: true`; `conferido: 2026-10-20`) e para a identificação das publicações (órgão, autor, ano e página da seção 5; o script confere a página de cada R1 a R31 contra a tabela do mapa).
- Seções do canônico NÃO usadas: cabeçalho (linhas 1 a 6), 0 e 0.1 (resposta ao R1 e registro de acatamento), os parágrafos introdutórios da seção 1, o cabeçalho das seções 3, 4 e 5, 6 (proveniência), 7 (contagens), 8 (bloco à GCB); em cada item, as linhas Folha, Ponto de julgamento, Formato, Tipo de base, Base, Mecanismo, Troca, Difere de, Alteração na v2 e Marcas; nos pares, a coluna Código e a coluna Base de cada lado.
- JSON gerado: D4_plataforma.json, SHA-256 e44b66e785a8d4ce55449b2574153d7670a603cb8f457975248aede323c22806; tópicos incorporados de D4_topicos_fonte.json, SHA-256 c65772e4173acfc5982da707989434792fa9b28727c23a6af8b0999bad03abf0 (escritos à mão).

## 2. Correspondência bloco de origem → ## / ###
| Origem (D4_v2_1.md, seção 1) | Destino no curso |
|---|---|
| PARTE 1.0 — 8 (caput) Evolução dos modelos de gestão pública: patrimonialismo, administração burocrática e nova gestão pública (New Public Management) (caput; não é folha) | `## 8 EVOLUÇÃO DOS MODELOS DE GESTÃO PÚBLICA` |
| C8.0-01 Administração patrimonialista (R1) | `### Administração patrimonialista` |
| C8.0-02 Administração burocrática: adoção e traços (R1, R2, R4) | `### Administração burocrática: adoção e traços` |
| C8.0-03 Limites da administração burocrática (R2) | `### Limites da administração burocrática` |
| C8.0-04 Administração pública gerencial e paradigma gerencialista, NPM (R3, R4) | `### Administração pública gerencial e paradigma gerencialista, NPM` |
| C8.0-05 Fonte inspiradora de cada modelo (R8, primeira frase) | `### Fonte inspiradora de cada modelo` |
| C8.0-06 Plano Diretor da Reforma do Aparelho do Estado, PDRAE (R5): só curso | `### Plano Diretor da Reforma do Aparelho do Estado, PDRAE` |
| PARTE 1.1 — 8.1 Nova Governança Pública (New Public Governance): conceito, fundamentos e evolução | `## 8.1 NOVA GOVERNANÇA PÚBLICA (NEW PUBLIC GOVERNANCE): CONCEITO, FUNDAMENTOS E EVOLUÇÃO` |
| C8.1-01 Nova Governança Pública (NPG): o princípio orientador das redes (R6) | `### Nova Governança Pública (NPG): o princípio orientador das redes` |
| C8.1-02 Papel do governo e fundamentos da NPG (R7); pós-NPM (R4, R8) | `### Papel do governo e fundamentos da NPG; pós-NPM` |
| C8.1-03 Convenção de siglas: NPM, NPG e pós-NPM (e a sigla ‘NGP’ do Ipea) | `### Convenção de siglas: NPM, NPG e pós-NPM (e a sigla ‘NGP’ do Ipea)` |
| C8.1-04 Evolução da NPG: o que não se afirma | `### Evolução da NPG: o que não se afirma` |
| PARTE 1.2 — 8.2 Ação pública em redes de cooperação, articulação interinstitucional e parcerias com o setor privado e terceiro setor | `## 8.2 AÇÃO PÚBLICA EM REDES DE COOPERAÇÃO, ARTICULAÇÃO INTERINSTITUCIONAL E PARCERIAS COM O SETOR PRIVADO E TERCEIRO SETOR` |
| C8.2-01 Articulação interinstitucional: o meio (Decreto 9.203, art. 4º, IV) | `### Articulação interinstitucional: o meio (Decreto 9.203, art. 4º, IV)` |
| C8.2-02 Redes, colaboração e parcerias como tendências (R9, R10); R7 em 8.1 | `### Redes, colaboração e parcerias como tendências` |
| C8.2-03 Parceria público-privada (PPP) e concessão comum (Lei 11.079, art. 2º, caput e § 3º) | `### Parceria público-privada (PPP) e concessão comum (Lei 11.079, art. 2º, caput e § 3º)` |
| C8.2-04 Concessão patrocinada × concessão administrativa (Lei 11.079, art. 2º, §§ 1º e 2º) | `### Concessão patrocinada × concessão administrativa (Lei 11.079, art. 2º, §§ 1º e 2º)` |
| C8.2-05 Vedações do art. 2º, § 4º, da Lei 11.079 | `### Vedações do art. 2º, § 4º, da Lei 11.079` |
| C8.2-06 Organização da sociedade civil e parceria (Lei 13.019, art. 2º, I e III) | `### Organização da sociedade civil e parceria (Lei 13.019, art. 2º, I e III)` |
| C8.2-07 Termo de colaboração × termo de fomento × acordo de cooperação (Lei 13.019, art. 2º, VII, VIII e VIII-A) | `### Termo de colaboração × termo de fomento × acordo de cooperação (Lei 13.019, art. 2º, VII, VIII e VIII-A)` |
| C8.2-08 Organização social, OS (Lei 9.637, art. 1º) | `### Organização social, OS (Lei 9.637, art. 1º)` |
| C8.2-09 Organização da sociedade civil de interesse público, OSCIP (Lei 9.790, art. 1º) | `### Organização da sociedade civil de interesse público, OSCIP (Lei 9.790, art. 1º)` |
| C8.2-10 ‘Terceiro setor’: rótulo sem definição legal | `### ‘Terceiro setor’: rótulo sem definição legal` |
| PARTE 1.3 — 8.3 Coprodução do bem público, participação cidadã e transparência ativa | `## 8.3 COPRODUÇÃO DO BEM PÚBLICO, PARTICIPAÇÃO CIDADÃ E TRANSPARÊNCIA ATIVA` |
| C8.3-01 Coprodução (R11; R7 em 8.1) | `### Coprodução` |
| C8.3-02 Participação cidadã no processo decisório (R12, R13; Decreto 9.203, art. 4º, VIII e IX) | `### Participação cidadã no processo decisório` |
| C8.3-03 Participação do usuário de serviços públicos (Lei 13.460, arts. 1º e 6º, I) | `### Participação do usuário de serviços públicos (Lei 13.460, arts. 1º e 6º, I)` |
| C8.3-04 Transparência ativa (Decreto 9.203, art. 4º, XI; R14, R15; LAI, art. 8º) | `### Transparência ativa (Decreto 9.203, art. 4º, XI; LAI, art. 8º)` |
| C8.3-05 Transparência passiva (LAI, art. 10, caput; exceção da ficha) | `### Transparência passiva (LAI, art. 10, caput)` |
| C8.3-06 Conteúdo mínimo da divulgação (LAI, art. 8º, § 1º, I a VI) | `### Conteúdo mínimo da divulgação (LAI, art. 8º, § 1º, I a VI)` |
| C8.3-07 Coprodução do bem público: o que não se afirma | `### Coprodução do bem público: o que não se afirma` |
| PARTE 1.4 — 8.4 Valor Público, cadeia de valor público | `## 8.4 VALOR PÚBLICO, CADEIA DE VALOR PÚBLICO` |
| C8.4-01 Valor público (Decreto 9.203, art. 2º, II, parte inicial) | `### Valor público (Decreto 9.203, art. 2º, II, parte inicial)` |
| C8.4-02 Valor público como finalidade da articulação (Decreto 9.203, art. 4º, IV) | `### Valor público como finalidade da articulação (Decreto 9.203, art. 4º, IV)` |
| C8.4-03 Cadeia de valor público (R16, R17) | `### Cadeia de valor público` |
| C8.4-04 Elos da cadeia de valor das políticas públicas (R18) | `### Elos da cadeia de valor das políticas públicas` |
| C8.4-05 Valor público e cadeia de valor: o que não se afirma | `### Valor público e cadeia de valor: o que não se afirma` |
| PARTE 1.5 — 9.1 Governança pública: conceito, distinção entre governança e governabilidade e alinhamento estratégico | `## 9.1 GOVERNANÇA PÚBLICA` |
| C9.1-01 Conceito de governança pública no decreto (art. 2º, I) | `### Conceito de governança pública no decreto (art. 2º, I)` |
| C9.1-02 Conceito do TCU e origem do conceito do decreto (R19, R23) | `### Conceito do TCU e origem do conceito do decreto` |
| C9.1-03 Governança × gestão (R20) | `### Governança × gestão` |
| C9.1-04 Governança × governabilidade (R21; R5) | `### Governança × governabilidade` |
| C9.1-05 Alinhamento estratégico (R22; art. 5º, II) | `### Alinhamento estratégico (art. 5º, II)` |
| PARTE 1.6 — 9.2 Mecanismos de governança: liderança, estratégia e controle | `## 9.2 MECANISMOS DE GOVERNANÇA: LIDERANÇA, ESTRATÉGIA E CONTROLE` |
| C9.2-01 Os três mecanismos (art. 5º, caput; R24) | `### Os três mecanismos (art. 5º, caput)` |
| C9.2-02 Liderança (art. 5º, I; R25) | `### Liderança (art. 5º, I)` |
| C9.2-03 Estratégia (art. 5º, II; R26) | `### Estratégia (art. 5º, II)` |
| C9.2-04 Controle (art. 5º, III; R27) | `### Controle (art. 5º, III)` |
| C9.2-05 Alta administração e conteúdo mínimo (art. 6º) | `### Alta administração e conteúdo mínimo (art. 6º)` |
| C9.2-06 Diretrizes ligadas à liderança (art. 4º, V e X) | `### Diretrizes ligadas à liderança (art. 4º, V e X)` |
| C9.2-07 Condições mínimas da liderança × princípios da governança: competência e motivação (art. 5º, I, b e d; art. 3º) — acréscimo da v2 (leitura externa B12; QA PENDENTE (R2)) | `### Condições mínimas da liderança × princípios da governança: competência e motivação (art. 5º, I, b e d; art. 3º)` |
| PARTE 1.7 — 9.3 Valor público, entrega de resultados, sustentabilidade e avaliação de impactos | `## 9.3 CONCEITO DE VALOR PÚBLICO` |
| C9.3-01 Valor público: respostas efetivas e úteis (art. 2º, II, parte final) | `### Valor público: respostas efetivas e úteis (art. 2º, II, parte final)` |
| C9.3-02 Geração de valor público (R29) | `### Geração de valor público` |
| C9.3-03 Resultados para a sociedade e sustentabilidade (art. 4º, I; R28) | `### Resultados para a sociedade e sustentabilidade (art. 4º, I)` |
| C9.3-04 Monitoramento e avaliação de políticas (art. 4º, III e VII; art. 6º, parágrafo único, I) | `### Monitoramento e avaliação de políticas (art. 4º, III e VII; art. 6º, parágrafo único, I)` |
| C9.3-05 Avaliação de impacto (R30, R31) | `### Avaliação de impacto` |
| C9.3-06 Análise ex ante × avaliação ex post (R18, parte final) | `### Análise ex ante × avaliação ex post` |
| PARTE 1.8 — 9.4 Decreto Federal nº 9.203/2017 e suas alterações | `## 9.4 DECRETO FEDERAL Nº 9.203/2017 E SUAS ALTERAÇÕES (POLÍTICA DE GOVERNANÇA DA ADMINISTRAÇÃO PÚBLICA FEDERAL DIRETA, AUTÁRQUICA E FUNDACIONAL)` |
| C9.4-01 Âmbito e definições (arts. 1º e 2º) | `### Âmbito e definições (arts. 1º e 2º)` |
| C9.4-02 Princípios (art. 3º) | `### Princípios (art. 3º)` |
| C9.4-03 Diretrizes (art. 4º) | `### Diretrizes (art. 4º)` |
| C9.4-04 Comitê Interministerial de Governança — CIG (arts. 7º-A, 8º-A, 8º-B, 9º-A) | `### Comitê Interministerial de Governança — CIG (arts. 7º-A, 8º-A, 8º-B, 9º-A)` |
| C9.4-05 Grupos de trabalho, Secretaria-Executiva e participação (arts. 10-A, 10-B, 11-A, 12-A) | `### Grupos de trabalho, Secretaria-Executiva e participação (arts. 10-A, 10-B, 11-A, 12-A)` |
| C9.4-06 Órgãos, entidades e comitês internos de governança (arts. 13-A, 15-A, 16; art. 14 revogado) | `### Órgãos, entidades e comitês internos de governança (arts. 13-A, 15-A, 16; art. 14 revogado)` |
| C9.4-07 Gestão de riscos, controles internos e auditoria interna (arts. 17 e 18) | `### Gestão de riscos, controles internos e auditoria interna (arts. 17 e 18)` |
| C9.4-08 Programa de integridade (art. 19; art. 20-A revogado) | `### Programa de integridade (art. 19; art. 20-A revogado)` |
| C9.4-09 Alterações do decreto: vigente com letra × revogado | `### Alterações do decreto: vigente com letra × revogado` |
| C9.4-10 Manuais e guias do CIG, propostas dos órgãos e colegiado temático (art. 7º-A; art. 9º-A, II, III, § 1º e § 2º; art. 13-A) — acréscimo da v2 (leitura externa A11, B14, C10; QA PENDENTE (R2)) | `### Manuais e guias do CIG, propostas dos órgãos e colegiado temático (art. 7º-A; art. 9º-A, II, III, § 1º e § 2º; art. 13-A)` |
| C9.4-11 Simplificação, modernização e integração de serviços públicos (art. 4º, II) — acréscimo da v2 (leitura externa B13; QA PENDENTE (R2)) | `### Simplificação, modernização e integração de serviços públicos (art. 4º, II)` |
| C9.4-12 Gestão de riscos: integração em todos os níveis e controles proporcionais (art. 17, II e III) — acréscimo da v2 (leitura externa B16, C10; QA PENDENTE (R2)) | `### Gestão de riscos: integração em todos os níveis e controles proporcionais (art. 17, II e III)` |

Regras gerais do curso: "- Definição:" → quadro DEFINIÇÃO (em lista, sem linha em branco, quando a definição tem 3 ou mais frases: operação 4; a divisão não corta citação entre aspas; em parágrafo único nos demais casos); quadro BASE LEGAL em lista com os dispositivos que o próprio bloco cita (no título, na definição ou na Base da pegadinha) e, para o referencial oficial, uma linha "Fonte: <órgão>, <publicação>, <ano>, p. <n>" por publicação citada (órgão, título, ano e página da seção 5 do Anexo N, como manda a ordem; artigo revogado não entra no quadro; o quadro é omitido nos blocos sem dispositivo nem publicação — nenhum neste lote); "- Exemplo (Legislativo, hipotético):" → EXEMPLO PARLAMENTAR (o canônico já termina cada exemplo com "O exemplo é hipotético."); "- Pegadinha provável: … [Desfeita por: X]" → PEGADINHA PROVÁVEL com "Base: X". Código de bloco ("C8.0-01 " etc.) removido do título; R-ids saem dos títulos. Títulos `##`: texto do edital em maiúsculas (P1-DA-8, o caput, e P1-DA-9.3 cortados no primeiro ":" por passarem de 90 caracteres). Resumo: seção 2 inteira (item 8 e item 9), uma só cadeia markdown. Pares: seção 3, 24; `a`/`b` = termos do campo "Par" (a = primeiro; b = demais unidos por " × "); `como` = coluna Diferença + " Como a banca troca: " + coluna "Como a banca troca"; a coluna Base de cada lado não entra. Pegadinhas: seção 4, 62, sem número, sem código do bloco e sem marca de versão; os rótulos " — Desfeita por: X" e " — Dispositivo ou trecho que a desfaz: X" viram " Base: X"; `itemEdital` pelo bloco ([C8.0-NN] → P1-DA-8; [C8.n-NN] → P1-DA-8.n; [C9.n-NN] → P1-DA-9.n).

## 3. Deleções e trocas (cada uma registrada)
Tipos: deleção de marca (v2, R2, QA PENDENTE, leitura externa, Anexo N, códigos de bloco); deleção de frase inteira ou de oração (processo, "[SEM FONTE]", cobertura de itens, cruzamento com item do banco, regra de produção); troca mínima (op. 6: R-id trocado pela identificação da publicação; "lote" → "curso"); troca de rótulo (operação 2).

Contagem por tipo (sem as da errata, seção "Errata de forma"): deleção de frase inteira: 21; deleção de marca: 41; deleção de oração de processo: 15; troca de rótulo: 124; troca mínima (op. 6): 264.

### 3.1 R-ids (códigos do Anexo N) trocados pela identificação da publicação
Regra aplicada: o R-id nunca aparece. Onde o bloco já identificava a publicação (autor e órgão, ou órgão, edição, ano e página), o R-id saiu e a frase foi mantida com o termo mínimo ("o artigo", "o texto", ou o título da publicação à frente do parêntese que já a citava) — itens 3.2 abaixo. Onde o bloco só trazia o código, a remissão foi trocada pela identificação curta da publicação (autor ou título, órgão, ano), tirada da seção 5 do Anexo N, e, nas listas "Base:", com a página; nos quadros BASE LEGAL a linha "Fonte:" traz órgão, publicação, ano e página. Onde a remissão era supérflua e só repetia o código ("(art. 5º, III; R27)"), foi retirada. As trocas mecânicas, por contexto:

- [curso C8.0-01 (exemplo)] `R1` → `o artigo de Bresser-Pereira (ENAP, 2022)`.
- [curso C8.0-01 (pegadinha)] `R1` → `Bresser-Pereira, ENAP, 2022, p. 58`.
- [curso C8.0-02 (exemplo)] `R1 e R2` → `o artigo de Bresser-Pereira (ENAP, 2022)`.
- [curso C8.0-02 (pegadinha)] `R4` → `o Guia da Política de Governança Pública (Casa Civil, 2018)`; `R4` → `Guia da Política de Governança Pública, Casa Civil, 2018, p. 29`; `R1 e R2` → `Bresser-Pereira, ENAP, 2022, p. 58`.
- [curso C8.0-03 (exemplo)] `R2` → `o artigo de Bresser-Pereira (ENAP, 2022)`.
- [curso C8.0-03 (pegadinha)] `R2` → `Bresser-Pereira, ENAP, 2022, p. 58`.
- [curso C8.0-04 (exemplo)] `R3` → `o artigo de Bresser-Pereira (ENAP, 2022)`.
- [curso C8.0-04 (pegadinha)] `R4` → `o Guia da Política de Governança Pública (Casa Civil, 2018)`; `R3` → `Bresser-Pereira, ENAP, 2022, p. 59`; `R4` → `Guia da Política de Governança Pública, Casa Civil, 2018, p. 29`.
- [curso C8.0-05 (exemplo)] `R8` → `o texto de Cavalcante (Ipea, 2018)`.
- [curso C8.0-05 (pegadinha)] `R6` → `Bouckaert, ENAP, 2024`; `R8` → `Cavalcante, Ipea, 2018, p. 21`; `R6` → `Bouckaert, ENAP, 2024, p. 17`.
- [curso C8.0-06 (pegadinha)] `R5` → `a análise de Cavalcante (Ipea, 2020)`; `de R5` → `da análise de Cavalcante (Ipea, 2020)`; `de R21` → `do Referencial Básico de Governança Organizacional (TCU, 2020)`; `R5` → `Cavalcante, Ipea, 2020, p. 40`.
- [curso C8.1-01 (exemplo)] `R6` → `o artigo de Bouckaert (ENAP, 2024)`.
- [curso C8.1-01 (pegadinha)] `R6` → `Bouckaert, ENAP, 2024, p. 17`; `R8` → `Cavalcante, Ipea, 2018, p. 21`.
- [curso C8.1-02 (exemplo)] `R7` → `o artigo de Bouckaert (ENAP, 2024)`.
- [curso C8.1-02 (pegadinha)] `R7` → `Bouckaert, ENAP, 2024, p. 25`; `R4 e R8` → `Guia da Política de Governança Pública, Casa Civil, 2018, p. 29; Cavalcante, Ipea, 2018, p. 21`.
- [curso C8.1-03 (definição)] `de R4 e R8` → `do Guia da Política de Governança Pública (Casa Civil, 2018) e do texto de Cavalcante (Ipea, 2018)`; `R4 e R8` → `O Guia da Política de Governança Pública (Casa Civil, 2018) e o texto de Cavalcante (Ipea, 2018)`; `R6 e R7` → `o artigo de Bouckaert (ENAP, 2024)`.
- [curso C8.1-03 (pegadinha)] `R8, R9 e R12` → `Cavalcante, Ipea, 2018, pp. 21, 19 e 20`; `R6 e R7` → `Bouckaert, ENAP, 2024, pp. 17 e 25`.
- [curso C8.1-04 (pegadinha)] `R6, R7 e R8` → `Bouckaert, ENAP, 2024, pp. 17 e 25; Cavalcante, Ipea, 2018, p. 21`.
- [curso C8.2-02 (pegadinha)] `R9` → `o texto de Cavalcante (Ipea, 2018)`; `R9` → `Cavalcante, Ipea, 2018, p. 19`; `R10` → `Guia da Política de Governança Pública, Casa Civil, 2018, p. 41`.
- [curso C8.3-01 (exemplo)] `R11` → `o capítulo de Lui et al. (Ipea, 2023)`.
- [curso C8.3-01 (pegadinha)] `R11` → `Lui et al., Ipea, 2023, p. 236`.
- [curso C8.3-02 (pegadinha)] `em R13` → `no Guia da Política de Governança Pública (Casa Civil, 2018)`; `R12 e R13` → `Cavalcante, Ipea, 2018, p. 20; Guia da Política de Governança Pública, Casa Civil, 2018, p. 51`.
- [curso C8.3-04 (definição)] `de R14 e R15` → `do Referencial Básico de Governança Organizacional (TCU, 2020) e do Guia da Política de Governança Pública (Casa Civil, 2018)`.
- [curso C8.3-04 (pegadinha)] `R15; R14` → `Guia da Política de Governança Pública, Casa Civil, 2018, p. 54; Referencial Básico de Governança Organizacional, TCU, 2020, p. 90`.
- [curso C8.3-05 (definição)] `de R14` → `do Referencial Básico de Governança Organizacional (TCU, 2020)`.
- [curso C8.3-05 (pegadinha)] `R14` → `Referencial Básico de Governança Organizacional, TCU, 2020, p. 90`.
- [curso C8.3-07 (pegadinha)] `R11 e R7` → `Lui et al., Ipea, 2023, p. 236; Bouckaert, ENAP, 2024, p. 25`.
- [curso C8.4-03 (exemplo)] `R17` → `o texto de Martins (Ipea, 2018)`.
- [curso C8.4-03 (pegadinha)] `R16; R17` → `documento didático da CGU, p. 6 do arquivo PDF (sem numeração impressa); Martins, Ipea, 2018, p. 58`.
- [curso C8.4-04 (exemplo)] `R18` → `o guia prático de análise ex post (Casa Civil, 2018)`.
- [curso C8.4-04 (pegadinha)] `R18` → `guia prático de análise ex post, Casa Civil, 2018, p. 13`.
- [curso C8.4-05 (definição)] `R18` → `guia prático de análise ex post, Casa Civil, 2018`.
- [curso C8.4-05 (pegadinha)] `de R18` → `do guia prático de análise ex post (Casa Civil, 2018)`; `R18` → `guia prático de análise ex post, Casa Civil, 2018, p. 13`.
- [curso C9.1-02 (pegadinha)] `R23; R19` → `Guia da Política de Governança Pública, Casa Civil, 2018, p. 15; Referencial Básico de Governança Organizacional, TCU, 2020, p. 15`.
- [curso C9.1-03 (exemplo)] `R20` → `o Referencial Básico de Governança Organizacional (TCU, 2020)`.
- [curso C9.1-03 (pegadinha)] `R20` → `Referencial Básico de Governança Organizacional, TCU, 2020, p. 16`.
- [curso C9.1-04 (exemplo)] `de R21` → `do Referencial Básico de Governança Organizacional (TCU, 2020)`.
- [curso C9.1-04 (pegadinha)] `R21; R5` → `Referencial Básico de Governança Organizacional, TCU, 2020, p. 111; Cavalcante, Ipea, 2020, p. 40`.
- [curso C9.1-05 (exemplo)] `R22` → `o Referencial Básico de Governança Organizacional (TCU, 2020)`.
- [curso C9.1-05 (pegadinha)] `de R22` → `do Referencial Básico de Governança Organizacional (TCU, 2020)`; `R22` → `Referencial Básico de Governança Organizacional, TCU, 2020, p. 21`.
- [curso C9.2-02 (exemplo)] `por R25` → `pelo Referencial Básico de Governança Organizacional (TCU, 2020)`.
- [curso C9.2-02 (pegadinha)] `R25` → `Referencial Básico de Governança Organizacional, TCU, 2020, p. 54`.
- [curso C9.2-03 (pegadinha)] `R26` → `Referencial Básico de Governança Organizacional, TCU, 2020, p. 69`.
- [curso C9.2-04 (exemplo)] `R27` → `o Referencial Básico de Governança Organizacional (TCU, 2020)`.
- [curso C9.2-04 (pegadinha)] `R27` → `Referencial Básico de Governança Organizacional, TCU, 2020, p. 88`.
- [curso C9.3-02 (pegadinha)] `R29` → `Martins, Ipea, 2018, p. 60`.
- [curso C9.3-03 (pegadinha)] `R28` → `Referencial Básico de Governança Organizacional, TCU, 2020, p. 15-16`.
- [curso C9.3-05 (exemplo)] `R31` → `o guia prático de análise ex post (Casa Civil, 2018)`.
- [curso C9.3-05 (pegadinha)] `R30; R31` → `guia prático de análise ex post, Casa Civil, 2018, p. 33`.
- [curso C9.3-06 (pegadinha)] `R18` → `guia prático de análise ex post, Casa Civil, 2018, p. 13`.
- [resumo] `| R1 (Bresser-Pereira, RSP/ENAP) |` → `| Bresser-Pereira, Revista do Serviço Público (ENAP, 2022) |`; `| R1, R2; R8 (Ipea); R4 (Guia da Casa Civil) |` → `| Bresser-Pereira (ENAP, 2022); Cavalcante (Ipea, 2018); Guia da Política de Governança Pública (Casa Civil, 2018) |`; `| R3; R4; R8 |` → `| Bresser-Pereira (ENAP, 2022); Guia da Política de Governança Pública (Casa Civil, 2018); Cavalcante (Ipea, 2018) |`; `| R4; R8; R9; R12 |` → `| Guia da Política de Governança Pública (Casa Civil, 2018); Cavalcante (Ipea, 2018) |`; `| R6; R7 (Bouckaert, RSP/ENAP) |` → `| Bouckaert, Revista do Serviço Público (ENAP, 2024) |`; `| R11 |` → `| Lui et al. (Ipea, 2023) |`; `| R12; R13 |` → `| Cavalcante (Ipea, 2018); Guia da Política de Governança Pública (Casa Civil, 2018) |`; `| Lei 12.527/2011, art. 8º, caput; R14; R15 |` → `| Lei 12.527/2011, art. 8º, caput; Referencial Básico de Governança Organizacional (TCU, 2020); Guia da Política de Governança Pública (Casa Civil, 2018) |`; `| R16 (CGU) |` → `| Documento didático da CGU |`; `| R17 |` → `| Martins (Ipea, 2018) |`; `| R18 |` → `| Guia prático de análise ex post (Casa Civil, 2018) |`; `de R14 e R15` → `do Referencial Básico de Governança Organizacional (TCU, 2020) e do Guia da Política de Governança Pública (Casa Civil, 2018)`; `R20` → `Referencial Básico de Governança Organizacional, TCU, 2020`; `R21` → `Referencial Básico de Governança Organizacional, TCU, 2020`; `R22` → `Referencial Básico de Governança Organizacional, TCU, 2020`; `R23` → `Guia da Política de Governança Pública, Casa Civil, 2018`; `R27` → `Referencial Básico de Governança Organizacional, TCU, 2020`; `R30, R31` → `guia prático de análise ex post, Casa Civil, 2018`; `R18` → `guia prático de análise ex post, Casa Civil, 2018`.
- [par P-03] `R4, R8` → `Guia da Política de Governança Pública, Casa Civil, 2018; Cavalcante, Ipea, 2018`.
- [par P-07] `R14` → `O Referencial Básico de Governança Organizacional (TCU, 2020)`.
- [par P-10] `R11` → `Lui et al., Ipea, 2023`.
- [par P-11] `de R18` → `do guia prático de análise ex post (Casa Civil, 2018)`.
- [par P-51] `de R21` → `do Referencial Básico de Governança Organizacional (TCU, 2020)`; `de R5` → `da análise de Cavalcante (Ipea, 2020)`.
- [par P-56] `a R18` → `ao guia prático de análise ex post (Casa Civil, 2018)`; `a R28` → `ao Referencial Básico de Governança Organizacional (TCU, 2020)`.
- [par P-57] `R27` → `Referencial Básico de Governança Organizacional, TCU, 2020`; `de R27` → `do Referencial Básico de Governança Organizacional (TCU, 2020)`.
- [pegadinha 1] `R1` → `Bresser-Pereira, ENAP, 2022, p. 58`.
- [pegadinha 2] `R4` → `o Guia da Política de Governança Pública (Casa Civil, 2018)`; `R4` → `Guia da Política de Governança Pública, Casa Civil, 2018, p. 29`; `R1 e R2` → `Bresser-Pereira, ENAP, 2022, p. 58`.
- [pegadinha 3] `R2` → `Bresser-Pereira, ENAP, 2022, p. 58`.
- [pegadinha 4] `R4` → `o Guia da Política de Governança Pública (Casa Civil, 2018)`; `R3` → `Bresser-Pereira, ENAP, 2022, p. 59`; `R4` → `Guia da Política de Governança Pública, Casa Civil, 2018, p. 29`.
- [pegadinha 5] `R6` → `Bouckaert, ENAP, 2024`; `R8` → `Cavalcante, Ipea, 2018, p. 21`; `R6` → `Bouckaert, ENAP, 2024, p. 17`.
- [pegadinha 6] `R5` → `a análise de Cavalcante (Ipea, 2020)`; `de R5` → `da análise de Cavalcante (Ipea, 2020)`; `de R21` → `do Referencial Básico de Governança Organizacional (TCU, 2020)`; `R5` → `Cavalcante, Ipea, 2020, p. 40`.
- [pegadinha 7] `R6` → `Bouckaert, ENAP, 2024, p. 17`; `R8` → `Cavalcante, Ipea, 2018, p. 21`.
- [pegadinha 8] `R7` → `Bouckaert, ENAP, 2024, p. 25`; `R4 e R8` → `Guia da Política de Governança Pública, Casa Civil, 2018, p. 29; Cavalcante, Ipea, 2018, p. 21`.
- [pegadinha 9] `R8, R9 e R12` → `Cavalcante, Ipea, 2018, pp. 21, 19 e 20`; `R6 e R7` → `Bouckaert, ENAP, 2024, pp. 17 e 25`.
- [pegadinha 10] `R6, R7 e R8` → `Bouckaert, ENAP, 2024, pp. 17 e 25; Cavalcante, Ipea, 2018, p. 21`.
- [pegadinha 12] `R9` → `o texto de Cavalcante (Ipea, 2018)`; `R9` → `Cavalcante, Ipea, 2018, p. 19`; `R10` → `Guia da Política de Governança Pública, Casa Civil, 2018, p. 41`.
- [pegadinha 21] `R11` → `Lui et al., Ipea, 2023, p. 236`.
- [pegadinha 22] `em R13` → `no Guia da Política de Governança Pública (Casa Civil, 2018)`; `R12 e R13` → `Cavalcante, Ipea, 2018, p. 20; Guia da Política de Governança Pública, Casa Civil, 2018, p. 51`.
- [pegadinha 24] `R15; R14` → `Guia da Política de Governança Pública, Casa Civil, 2018, p. 54; Referencial Básico de Governança Organizacional, TCU, 2020, p. 90`.
- [pegadinha 25] `R14` → `Referencial Básico de Governança Organizacional, TCU, 2020, p. 90`.
- [pegadinha 27] `R11 e R7` → `Lui et al., Ipea, 2023, p. 236; Bouckaert, ENAP, 2024, p. 25`.
- [pegadinha 30] `R16; R17` → `documento didático da CGU, p. 6 do arquivo PDF (sem numeração impressa); Martins, Ipea, 2018, p. 58`.
- [pegadinha 31] `R18` → `guia prático de análise ex post, Casa Civil, 2018, p. 13`.
- [pegadinha 32] `de R18` → `do guia prático de análise ex post (Casa Civil, 2018)`; `R18` → `guia prático de análise ex post, Casa Civil, 2018, p. 13`.
- [pegadinha 52] `R23; R19` → `Guia da Política de Governança Pública, Casa Civil, 2018, p. 15; Referencial Básico de Governança Organizacional, TCU, 2020, p. 15`.
- [pegadinha 53] `R20` → `Referencial Básico de Governança Organizacional, TCU, 2020, p. 16`.
- [pegadinha 54] `R21; R5` → `Referencial Básico de Governança Organizacional, TCU, 2020, p. 111; Cavalcante, Ipea, 2020, p. 40`.
- [pegadinha 55] `de R22` → `do Referencial Básico de Governança Organizacional (TCU, 2020)`; `R22` → `Referencial Básico de Governança Organizacional, TCU, 2020, p. 21`.
- [pegadinha 57] `R25` → `Referencial Básico de Governança Organizacional, TCU, 2020, p. 54`.
- [pegadinha 58] `R26` → `Referencial Básico de Governança Organizacional, TCU, 2020, p. 69`.
- [pegadinha 59] `R27` → `Referencial Básico de Governança Organizacional, TCU, 2020, p. 88`.
- [pegadinha 63] `R29` → `Martins, Ipea, 2018, p. 60`.
- [pegadinha 64] `R28` → `Referencial Básico de Governança Organizacional, TCU, 2020, p. 15-16`.
- [pegadinha 66] `R30; R31` → `guia prático de análise ex post, Casa Civil, 2018, p. 33`.
- [pegadinha 67] `R18` → `guia prático de análise ex post, Casa Civil, 2018, p. 13`.
- [justificativa D4-01] `de R6` → `do artigo de Bouckaert (ENAP, 2024)`; `R8` → `o texto de Cavalcante (Ipea, 2018)`.
- [justificativa D4-02] `R7` → `O artigo de Bouckaert (ENAP, 2024)`.
- [justificativa D4-03] `R8` → `O texto de Cavalcante (Ipea, 2018)`.
- [justificativa D4-04] `R7` → `O artigo de Bouckaert (ENAP, 2024)`; `R4` → `o Guia da Política de Governança Pública (Casa Civil, 2018)`.
- [justificativa D4-05] `R7` → `O artigo de Bouckaert (ENAP, 2024)`; `R4` → `o Guia da Política de Governança Pública (Casa Civil, 2018)`.
- [justificativa D4-06] `R4` → `O Guia da Política de Governança Pública (Casa Civil, 2018)`.
- [justificativa D4-08] `R9` → `O texto de Cavalcante (Ipea, 2018)`.
- [justificativa D4-10] `R10` → `O Guia da Política de Governança Pública (Casa Civil, 2018)`.
- [justificativa D4-17] `R15` → `o Guia da Política de Governança Pública (Casa Civil, 2018)`.
- [justificativa D4-18] `R12` → `O texto de Cavalcante (Ipea, 2018)`.
- [justificativa D4-20] `R13` → `O Guia da Política de Governança Pública (Casa Civil, 2018)`.
- [justificativa D4-23] `de R14` → `do Referencial Básico de Governança Organizacional (TCU, 2020)`.
- [justificativa D4-25] `R11` → `O capítulo de Lui et al. (Ipea, 2023)`.
- [justificativa D4-28] `R18` → `O guia prático de análise ex post (Casa Civil, 2018)`.
- [justificativa D4-31] `R17` → `O texto de Martins (Ipea, 2018)`.
- [justificativa D4-32] `R17` → `O texto de Martins (Ipea, 2018)`.
- [justificativa D4-33] `R16` → `O documento didático da CGU`.
- [justificativa D4-34] `R19` → `O Referencial Básico de Governança Organizacional (TCU, 2020)`.
- [justificativa D4-36] `R20` → `O Referencial Básico de Governança Organizacional (TCU, 2020)`.
- [justificativa D4-38] `R21` → `O Referencial Básico de Governança Organizacional (TCU, 2020)`; `de R21` → `do Referencial Básico de Governança Organizacional (TCU, 2020)`; `de R5` → `da análise de Cavalcante (Ipea, 2020)`.
- [justificativa D4-39] `R21` → `O Referencial Básico de Governança Organizacional (TCU, 2020)`.
- [justificativa D4-40] `R22` → `O Referencial Básico de Governança Organizacional (TCU, 2020)`.
- [justificativa D4-43] `R23` → `O Guia da Política de Governança Pública (Casa Civil, 2018)`.
- [justificativa D4-44] `R24` → `Referencial Básico de Governança Organizacional, TCU, 2020`.
- [justificativa D4-47] `R27` → `O Referencial Básico de Governança Organizacional (TCU, 2020)`.
- [justificativa D4-51] `R25` → `O Referencial Básico de Governança Organizacional (TCU, 2020)`.
- [justificativa D4-58] `R29` → `O texto de Martins (Ipea, 2018)`.
- [justificativa D4-59] `R28` → `O Referencial Básico de Governança Organizacional (TCU, 2020)`.
- [justificativa D4-61] `R30` → `O guia prático de análise ex post (Casa Civil, 2018)`.
- [justificativa D4-62] `R30` → `O guia prático de análise ex post (Casa Civil, 2018)`; `R31` → `o guia prático de análise ex post (Casa Civil, 2018)`.
- [justificativa D4-63] `R18` → `O guia prático de análise ex post (Casa Civil, 2018)`.
- [justificativa D4-74] `R3` → `O artigo de Bresser-Pereira (ENAP, 2022)`; `de R3` → `do artigo de Bresser-Pereira (ENAP, 2022)`.
- [justificativa D4-75] `R1` → `O artigo de Bresser-Pereira (ENAP, 2022)`; `R2` → `o artigo de Bresser-Pereira (ENAP, 2022)`.
- [justificativa D4-76] `R1` → `O artigo de Bresser-Pereira (ENAP, 2022)`.
- [justificativa D4-77] `R4` → `O Guia da Política de Governança Pública (Casa Civil, 2018)`.
- [justificativa D4-78] `R2` → `O artigo de Bresser-Pereira (ENAP, 2022)`; `R2` → `o artigo de Bresser-Pereira (ENAP, 2022)`.
- [justificativa D4-79] `R1` → `O artigo de Bresser-Pereira (ENAP, 2022)`.

### 3.2 Demais deleções e trocas

1. [curso C8.0-01 (título)] deleção de marca: `(R1)` → (nada). Motivo: R-id entre parênteses no título do bloco.
2. [curso C8.0-01 (definição)] deleção de frase inteira: `Datas e marcos históricos do modelo (por exemplo, o DASP de 1936 e o Decreto-Lei 200/1967): [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
3. [curso C8.0-01 (definição)] troca mínima (op. 6): `R1 descreve o modelo` → `o trecho descreve o modelo`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
4. [curso C8.0-02 (título)] deleção de marca: `(R1, R2, R4)` → (nada). Motivo: R-id entre parênteses no título do bloco.
5. [curso C8.0-02 (definição)] troca mínima (op. 6): `R1 diz que a administração burocrática` → `O artigo de Bresser-Pereira (ENAP, 2022) diz que a administração burocrática`. Motivo: o bloco não identificava a publicação neste ponto; o código sai e a identificação (autor, órgão, ano) vem da seção 5 do Anexo N, como manda a ordem.
6. [curso C8.0-02 (definição)] troca mínima (op. 6): `e R2 completa:` → `e o mesmo artigo completa:`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
7. [curso C8.0-02 (definição)] troca mínima (op. 6): `, em R4, associa` → `associa`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
8. [curso C8.0-03 (título)] deleção de marca: `(R2)` → (nada). Motivo: R-id entre parênteses no título do bloco.
9. [curso C8.0-03 (definição)] troca mínima (op. 6): `R2 aponta o limite` → `o trecho aponta o limite`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
10. [curso C8.0-04 (título)] deleção de marca: `(R3, R4)` → (nada). Motivo: R-id entre parênteses no título do bloco.
11. [curso C8.0-04 (definição)] troca mínima (op. 6): `R3 situa o início` → `o trecho situa o início`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
12. [curso C8.0-04 (definição)] troca mínima (op. 6): `Governança Pública (R4) associa` → `Governança Pública (Casa Civil, 2018) associa`. Motivo: o bloco só tinha o código (R-id); ele é trocado pelo órgão e ano da publicação (seção 5 do Anexo N).
13. [curso C8.0-04 (definição)] troca mínima (op. 6): `No texto próprio do lote` → `No texto próprio do curso`. Motivo: "lote" é referência de produção (seção 6); trocado por "curso", que o próprio texto já usa.
14. [curso C8.0-05 (título)] deleção de marca: `(R8, primeira frase)` → (nada). Motivo: R-id entre parênteses no título do bloco.
15. [curso C8.0-05 (definição)] troca mínima (op. 6): `R8 resume:` → `o trecho resume:`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
16. [curso C8.0-05 (definição)] troca mínima (op. 6): `A segunda frase de R8 (redes) é tratada em C8.1-02.` → `A segunda frase do trecho (redes) é tratada em 8.1.`. Motivo: código de bloco (C8.1-02) trocado pelo número do tópico (8.1) e R-id trocado por "do texto", pois a frase anterior já identifica a publicação (seção 6).
17. [curso C8.0-05 (pegadinha)] troca mínima (op. 6): `no Ipea (R8, R9, R12), ‘NGP’ é` → `em Cavalcante (Ipea, 2018, pp. 19, 20 e 21), ‘NGP’ é`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
18. [curso C8.0-06 (título)] deleção de marca: `(R5)` → (nada). Motivo: R-id entre parênteses no título do bloco.
19. [curso C8.0-06 (título)] deleção de marca: `: só curso` → (nada). Motivo: marca de cobertura ("só curso") no título do bloco.
20. [curso C8.0-06 (definição)] deleção de frase inteira: `O texto do PDRAE (1995) não foi aberto: [SEM FONTE — não afirmar] o que ele diz literalmente.` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
21. [curso C8.0-06 (definição)] troca mínima (op. 6): `(R5, Cavalcante)` → `(Cavalcante)`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
22. [curso C8.0-06 (definição)] troca mínima (op. 6): `R5 é paráfrase do Ipea, e nenhum item do lote versa sobre o conteúdo do PDRAE. R5 usa a palavra` → `A análise é paráfrase do Ipea. A análise usa a palavra`. Motivo: R-id trocado por "a análise" (o bloco já a identifica como análise do Ipea); a oração "e nenhum item do lote versa sobre o conteúdo do PDRAE" fala de cobertura de itens (seção 6).
23. [curso C8.1-01 (título)] deleção de marca: `(R6)` → (nada). Motivo: R-id entre parênteses no título do bloco.
24. [curso C8.1-01 (definição)] troca mínima (op. 6): `R6 diz:` → `o trecho diz:`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
25. [curso C8.1-01 (definição)] troca mínima (op. 6): `No texto próprio do lote` → `No texto próprio do curso`. Motivo: "lote" é referência de produção (seção 6); trocado por "curso", que o próprio texto já usa.
26. [curso C8.1-01 (definição)] deleção de frase inteira: `Autoria e ano de origem da NPG: [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
27. [curso C8.1-02 (título)] deleção de marca: `(R7)` → (nada). Motivo: R-id entre parênteses no título do bloco.
28. [curso C8.1-02 (título)] deleção de marca: `(R4, R8)` → (nada). Motivo: R-id entre parênteses no título do bloco.
29. [curso C8.1-02 (definição)] troca mínima (op. 6): `em artigo da RSP/ENAP, R7: “O governo` → `em artigo da RSP/ENAP: “O governo`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
30. [curso C8.1-02 (definição)] troca mínima (op. 6): `Governança Pública (R4) a relaciona` → `Governança Pública (Casa Civil, 2018) a relaciona`. Motivo: o bloco só tinha o código (R-id); ele é trocado pelo órgão e ano da publicação (seção 5 do Anexo N).
31. [curso C8.1-02 (definição)] troca mínima (op. 6): `publicação do Ipea (R8), escreve` → `publicação do Ipea, escreve`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
32. [curso C8.1-02 (pegadinha)] troca mínima (op. 6): `(R7 diz confiança na rede)` → `(o artigo diz confiança na rede)`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
33. [curso C8.1-02 (pegadinha)] troca mínima (op. 6): `(R7 diz teorias de rede)` → `(o artigo diz teorias de rede)`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
34. [curso C8.1-03 (definição)] troca mínima (op. 6): `No texto próprio do lote:` → `No texto próprio do curso:`. Motivo: "lote" é referência de produção (seção 6); trocado por "curso", que o próprio texto já usa.
35. [curso C8.1-03 (definição)] troca mínima (op. 6): `em citação literal de R8, R9 e R12 (Ipea), ‘NGP’ significa` → `em citação literal de Cavalcante (Ipea, 2018), ‘NGP’ significa`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
36. [curso C8.1-03 (definição)] troca mínima (op. 6): `e em R6 e R7 (ENAP), NPG significa` → `e em Bouckaert (ENAP, 2024), NPG significa`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
37. [curso C8.1-03 (definição)] troca mínima (op. 6): `nenhum bloco do lote afirma` → `nenhum bloco do curso afirma`. Motivo: "lote" é referência de produção (seção 6); trocado por "curso", que o próprio texto já usa.
38. [curso C8.1-04 (definição)] deleção de frase inteira: `Cronologia da ‘evolução’ da NPG, fundamentos além de redes, colaboração, confiança e reciprocidade, autoria ou ano de origem do conceito: [SEM FONTE — não afirmar]. Se a NPG ‘substitui’ a nova gestão pública (NPM) ou convive com ela é classificação disputada: [SEM FONTE — não afirmar] em nenhum dos dois sentidos.` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6) (duas frases marcadas).
39. [curso C8.1-04 (definição)] troca mínima (op. 6): `A sequência de R8 (hierarquia, mercado, redes) é` → `A sequência de Cavalcante (Ipea, 2018: hierarquia, mercado, redes) é`. Motivo: R-id trocado por autor, órgão e ano (seção 5 do Anexo N); o parêntese original é mantido dentro do novo.
40. [curso C8.1-04 (pegadinha)] deleção de oração de processo: `; Anexo N, seção 5 (SEM FONTE b e c)` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); a remissão ao Anexo N e à sua seção 5 também sai (seção 6).
41. [curso C8.2-01 (definição)] troca mínima (op. 6): `este lote não afirma` → `este curso não afirma`. Motivo: "lote" é referência de produção (seção 6); trocado por "curso", que o próprio texto já usa.
42. [curso C8.2-02 (título)] deleção de marca: `(R9, R10)` → (nada). Motivo: R-id entre parênteses no título do bloco.
43. [curso C8.2-02 (título)] deleção de marca: `; R7 em 8.1` → (nada). Motivo: R-id com remissão ("R7 em 8.1") no título do bloco.
44. [curso C8.2-02 (definição)] troca mínima (op. 6): `publicação do Ipea, R9: “as tendências` → `publicação do Ipea: “as tendências`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
45. [curso C8.2-02 (definição)] troca mínima (op. 6): `Casa Civil), em R10: “Com múltiplas` → `Casa Civil): “Com múltiplas`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
46. [curso C8.2-02 (definição)] troca mínima (op. 6): `ver C8.1-02 (R7).` → `ver 8.1.`. Motivo: código de bloco (C8.1-02) trocado pelo número do tópico (8.1) e remissão R7 retirada (seção 6).
47. [curso C8.2-10 (definição)] deleção de frase inteira: `Definição legal de ‘terceiro setor’: [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
48. [curso C8.2-10 (definição)] deleção de frase inteira: `As parcerias com o setor privado em sentido de PPP são as do bloco C8.2-03 a C8.2-05.` → (nada). Motivo: remissão a código interno de bloco (seção 6).
49. [curso C8.3-01 (título)] deleção de marca: `(R11; R7 em 8.1)` → (nada). Motivo: R-id entre parênteses no título do bloco.
50. [curso C8.3-01 (definição)] troca mínima (op. 6): `política urbana, R11: “O conceito` → `política urbana: “O conceito`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
51. [curso C8.3-01 (definição)] troca mínima (op. 6): `R7 (Bouckaert, ENAP) cita` → `Bouckaert (ENAP) cita`. Motivo: o código (R-id) sai e fica o autor e o órgão que o bloco já cita.
52. [curso C8.3-01 (definição)] troca mínima (op. 6): `; ver C8.1-02.` → `; ver 8.1.`. Motivo: código de bloco (C8.1-02) trocado pelo número do tópico (8.1).
53. [curso C8.3-02 (título)] deleção de marca: `(R12, R13; Decreto 9.203, art. 4º, VIII e IX)` → (nada). Motivo: R-id entre parênteses no título do bloco.
54. [curso C8.3-02 (definição)] troca mínima (op. 6): `R12 inclui entre as tendências` → `o trecho inclui entre as tendências`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
55. [curso C8.3-02 (definição)] troca mínima (op. 6): `Governança Pública (R13): “manter` → `Governança Pública (Casa Civil, 2018): “manter`. Motivo: o bloco só tinha o código (R-id); ele é trocado pelo órgão e ano da publicação (seção 5 do Anexo N).
56. [curso C8.3-03 (definição)] troca mínima (op. 6): `Este lote não afirma` → `Este curso não afirma`. Motivo: "lote" é referência de produção (seção 6); trocado por "curso", que o próprio texto já usa.
57. [curso C8.3-04 (título)] deleção de marca: `; R14, R15` → (nada). Motivo: R-id dentro do parêntese do título do bloco.
58. [curso C8.3-04 (definição)] troca mínima (op. 6): `Governança Pública (R15) lê a diretriz` → `Governança Pública (Casa Civil, 2018) lê a diretriz`. Motivo: o bloco só tinha o código (R-id); ele é trocado pelo órgão e ano da publicação (seção 5 do Anexo N).
59. [curso C8.3-04 (definição)] troca mínima (op. 6): `O Referencial do TCU (R14) inclui` → `O Referencial do TCU (2020) inclui`. Motivo: o bloco só tinha o código (R-id); ele é trocado pelo ano da publicação (seção 5 do Anexo N).
60. [curso C8.3-05 (título)] deleção de marca: `; exceção da ficha` → (nada). Motivo: remissão à ficha no título do bloco.
61. [curso C8.3-05 (definição)] deleção de frase inteira: `Lado passivo do par, pela exceção única da ficha (curso e par; nunca item), com o texto do Anexo N do D6, seção 4, consulta de 17/10/2026 (mesma URL da fonte N9):` → (nada). Motivo: fala de produção (cobertura de itens, cruzamento com item do banco, regra de redação, pedido de exceção); não é conteúdo para a candidata (seção 6); cita "ficha", "Anexo N", "D6" e o código de fonte N9 (seção 6).
62. [curso C8.3-07 (definição)] deleção de frase inteira: `Definição de ‘coprodução do bem público’ em referencial institucional de governança (TCU ou Casa Civil): [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
63. [curso C8.3-07 (definição)] troca mínima (op. 6): `As fontes do lote são R11 (Ipea, política urbana, capítulo de autoria) e R7 (ENAP, artigo traduzido).` → `As fontes do curso são Lui et al. (Ipea, política urbana, capítulo de autoria) e Bouckaert (ENAP, artigo traduzido).`. Motivo: "lote" trocado por "curso" (seção 6) e R-ids trocados pelos autores, que a seção 5 do Anexo N atribui às publicações já citadas no parêntese.
64. [curso C8.3-07 (pegadinha)] troca mínima (op. 6): `as fontes do lote não trazem` → `as fontes do curso não trazem`. Motivo: "lote" é referência de produção (seção 6); trocado por "curso", que o próprio texto já usa.
65. [curso C8.3-07 (pegadinha)] deleção de oração de processo: `Anexo N, seção 5 (SEM FONTE e);` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); a remissão ao Anexo N e à sua seção 5 também sai (seção 6).
66. [curso C8.4-01 (definição)] deleção de frase inteira: `Autoria ou obra de origem do conceito de valor público: [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
67. [curso C8.4-03 (título)] deleção de marca: `(R16, R17)` → (nada). Motivo: R-id entre parênteses no título do bloco.
68. [curso C8.4-03 (definição)] troca mínima (op. 6): `documento interno do órgão (R16):` → `documento interno do órgão:`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
69. [curso C8.4-03 (definição)] troca mínima (op. 6): `publicação do Ipea (R17):` → `publicação do Ipea:`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
70. [curso C8.4-04 (título)] deleção de marca: `(R18)` → (nada). Motivo: R-id entre parênteses no título do bloco.
71. [curso C8.4-04 (definição)] troca mínima (op. 6): `(Casa Civil), em R18, menciona` → `(Casa Civil) menciona`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
72. [curso C8.4-05 (definição)] deleção de frase inteira: `Etapas de uma ‘cadeia de valor público’ além das de R18, origem do conceito de valor público e autoria: [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
73. [curso C8.4-05 (definição)] troca mínima (op. 6): `R16 é documento interno da CGU` → `O documento didático é documento interno da CGU`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
74. [curso C8.4-05 (pegadinha)] troca mínima (op. 6): `Anexo N, seção 5 (SEM FONTE b e g).` → `Decreto 9.203/2017, art. 2º, II; R18.`. Motivo: a Base citava só o Anexo N (SEM FONTE b e g), que a seção 6 manda tirar; passa a valer a Base com os dispositivos que o próprio bloco cita (art. 2º, II, e a publicação da cadeia de valor das políticas públicas).
75. [curso C9.1-02 (título)] deleção de marca: `(R19, R23)` → (nada). Motivo: R-id entre parênteses no título do bloco.
76. [curso C9.1-02 (definição)] troca mínima (op. 6): `R19 (TCU, Referencial Básico de Governança Organizacional, 3. ed., 2020, p. 15):` → `Referencial Básico de Governança Organizacional (TCU, 3. ed., 2020, p. 15):`. Motivo: o código (R-id) sai e o título e o órgão que o parêntese já citava passam à frente.
77. [curso C9.1-02 (definição)] troca mínima (op. 6): `R23 (Casa Civil, Guia da Política de Governança Pública, 2018, p. 15):` → `Guia da Política de Governança Pública (Casa Civil, 2018, p. 15):`. Motivo: o código (R-id) sai e o título e o órgão que o parêntese já citava passam à frente.
78. [curso C9.1-03 (título)] deleção de marca: `(R20)` → (nada). Motivo: R-id entre parênteses no título do bloco.
79. [curso C9.1-03 (definição)] troca mínima (op. 6): `R20 (TCU, 3. ed., 2020, p. 16):` → `Referencial Básico de Governança Organizacional (TCU, 3. ed., 2020, p. 16):`. Motivo: o código (R-id) é trocado pelo título da publicação (seção 5 do Anexo N); órgão, edição, ano e página já estavam no bloco.
80. [curso C9.1-03 (definição)] deleção de marca: `, segundo o Anexo N,` → (nada). Motivo: referência ao Anexo N (seção 6).
81. [curso C9.1-04 (título)] deleção de marca: `(R21; R5)` → (nada). Motivo: R-id entre parênteses no título do bloco.
82. [curso C9.1-04 (definição)] troca mínima (op. 6): `R21 (TCU, 3. ed., 2020, p. 111;` → `Referencial Básico de Governança Organizacional (TCU, 3. ed., 2020, p. 111;`. Motivo: o código (R-id) é trocado pelo título da publicação (seção 5 do Anexo N); órgão, edição, ano e página já estavam no bloco.
83. [curso C9.1-04 (pegadinha)] deleção de frase inteira: `O texto literal do plano de 1995 e a sua definição de governabilidade: [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
84. [curso C9.1-04 (pegadinha)] deleção de oração de processo: `, e nenhum item os mistura` → (nada). Motivo: fala de produção (cobertura de itens, cruzamento com item do banco, regra de redação, pedido de exceção); não é conteúdo para a candidata (seção 6).
85. [curso C9.1-04 (pegadinha)] troca mínima (op. 6): `misturar R21 com R5, em que` → `misturar o trecho do Referencial Básico de Governança Organizacional (TCU, 2020) com o de Cavalcante, em que`. Motivo: R-ids trocados pela identificação das publicações (seção 5 do Anexo N); o bloco já falava de "análise publicada pelo Ipea".
86. [curso C9.1-05 (título)] deleção de marca: `(R22;` → (nada). Motivo: R-id no início do parêntese do título do bloco.
87. [curso C9.1-05 (definição)] troca mínima (op. 6): `R22 (TCU, 3. ed., 2020, p. 21):` → `Referencial Básico de Governança Organizacional (TCU, 3. ed., 2020, p. 21):`. Motivo: o código (R-id) é trocado pelo título da publicação (seção 5 do Anexo N); órgão, edição, ano e página já estavam no bloco.
88. [curso C9.2-01 (título)] deleção de marca: `; R24` → (nada). Motivo: R-id dentro do parêntese do título do bloco.
89. [curso C9.2-01 (definição)] troca mínima (op. 6): `R24 (TCU, 3. ed., 2020, p. 37):` → `Referencial Básico de Governança Organizacional (TCU, 3. ed., 2020, p. 37):`. Motivo: o código (R-id) é trocado pelo título da publicação (seção 5 do Anexo N); órgão, edição, ano e página já estavam no bloco.
90. [curso C9.2-02 (título)] deleção de marca: `; R25` → (nada). Motivo: R-id dentro do parêntese do título do bloco.
91. [curso C9.2-02 (definição)] troca mínima (op. 6): `R25 (TCU, 3. ed., 2020, p. 54):` → `Referencial Básico de Governança Organizacional (TCU, 3. ed., 2020, p. 54):`. Motivo: o código (R-id) é trocado pelo título da publicação (seção 5 do Anexo N); órgão, edição, ano e página já estavam no bloco.
92. [curso C9.2-02 (pegadinha)] troca mínima (op. 6): `equivalência de R25 (instâncias internas)` → `equivalência do referencial do TCU (instâncias internas)`. Motivo: R-id trocado por "referencial do TCU" (o bloco já identifica a publicação; evita parêntese dentro de parêntese).
93. [curso C9.2-03 (título)] deleção de marca: `; R26` → (nada). Motivo: R-id dentro do parêntese do título do bloco.
94. [curso C9.2-03 (definição)] troca mínima (op. 6): `R26 (TCU, 3. ed., 2020, p. 69):` → `Referencial Básico de Governança Organizacional (TCU, 3. ed., 2020, p. 69):`. Motivo: o código (R-id) é trocado pelo título da publicação (seção 5 do Anexo N); órgão, edição, ano e página já estavam no bloco.
95. [curso C9.2-03 (pegadinha)] troca mínima (op. 6): `atribuir a R26 (que fala` → `atribuir ao referencial do TCU (que fala`. Motivo: R-id trocado por "referencial do TCU" (o bloco já identifica a publicação; evita parêntese dentro de parêntese).
96. [curso C9.2-04 (título)] deleção de marca: `; R27` → (nada). Motivo: R-id dentro do parêntese do título do bloco.
97. [curso C9.2-04 (definição)] troca mínima (op. 6): `R27 (TCU, 3. ed., 2020, p. 88, nota 12):` → `Referencial Básico de Governança Organizacional (TCU, 3. ed., 2020, p. 88, nota 12):`. Motivo: o código (R-id) é trocado pelo título da publicação (seção 5 do Anexo N); órgão, edição, ano e página já estavam no bloco.
98. [curso C9.2-07 (título)] deleção de marca: `— acréscimo da v2 (leitura externa B12; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa").
99. [curso C9.2-07 (definição)] deleção de frase inteira: `O ponto do BQ-0152 (integridade como princípio e também como condição da liderança) é de item real bloqueado e não é julgado aqui.` → (nada). Motivo: fala de produção (cobertura de itens, cruzamento com item do banco, regra de redação, pedido de exceção); não é conteúdo para a candidata (seção 6); cita item do banco (BQ-0152).
100. [curso C9.3-02 (título)] deleção de marca: `(R29)` → (nada). Motivo: R-id entre parênteses no título do bloco.
101. [curso C9.3-02 (definição)] deleção de frase inteira: `Origem e autoria do conceito de valor público: [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
102. [curso C9.3-03 (título)] deleção de marca: `; R28` → (nada). Motivo: R-id dentro do parêntese do título do bloco.
103. [curso C9.3-03 (definição)] troca mínima (op. 6): `R28 (TCU, 3. ed., 2020, p. 15-16):` → `Referencial Básico de Governança Organizacional (TCU, 3. ed., 2020, p. 15-16):`. Motivo: o código (R-id) é trocado pelo título da publicação (seção 5 do Anexo N); órgão, edição, ano e página já estavam no bloco.
104. [curso C9.3-03 (definição)] deleção de frase inteira: `Definição oficial de sustentabilidade de políticas públicas: [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
105. [curso C9.3-03 (pegadinha)] troca mínima (op. 6): `(R28, sentido genérico)` → `(referencial do TCU, sentido genérico)`. Motivo: R-id trocado por "referencial do TCU" (o bloco já identifica a publicação).
106. [curso C9.3-05 (título)] deleção de marca: `(R30, R31)` → (nada). Motivo: R-id entre parênteses no título do bloco.
107. [curso C9.3-05 (definição)] troca mínima (op. 6): `R30 (Casa Civil, guia prático de análise ex post, v. 2, 2018, p. 33):` → `Guia prático de análise ex post (Casa Civil, v. 2, 2018, p. 33):`. Motivo: o código (R-id) sai e o título e o órgão que o parêntese já citava passam à frente.
108. [curso C9.3-05 (definição)] troca mínima (op. 6): `R31 (mesma obra, p. 33):` → `Na mesma obra (p. 33):`. Motivo: o código (R-id) sai; "mesma obra" já remetia à publicação do trecho anterior.
109. [curso C9.3-06 (título)] deleção de marca: `(R18, parte final)` → (nada). Motivo: R-id entre parênteses no título do bloco.
110. [curso C9.3-06 (definição)] troca mínima (op. 6): `R18 (Casa Civil, guia prático de análise ex post, v. 2, 2018, p. 13):` → `Guia prático de análise ex post (Casa Civil, v. 2, 2018, p. 13):`. Motivo: o código (R-id) sai e o título e o órgão que o parêntese já citava passam à frente.
111. [curso C9.4-02 (pegadinha)] deleção de frase inteira: `Observação: o ponto do BQ-0152 (integridade como princípio e também como condição da liderança) é de item real bloqueado e não é julgado aqui.` → (nada). Motivo: fala de produção (cobertura de itens, cruzamento com item do banco, regra de redação, pedido de exceção); não é conteúdo para a candidata (seção 6); cita item do banco (BQ-0152).
112. [curso C9.4-04 (definição)] deleção de frase inteira: `Resoluções e manuais do CIG: [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
113. [curso C9.4-06 (pegadinha)] deleção de oração de processo: `(lição do item real inapto BQ-0151, por causa do art. 14 revogado)` → (nada). Motivo: fala de produção (cobertura de itens, cruzamento com item do banco, regra de redação, pedido de exceção); não é conteúdo para a candidata (seção 6); cita item do banco (BQ-0151).
114. [curso C9.4-07 (pegadinha)] troca mínima (op. 6): `(art. 5º, III; R27)` → `(art. 5º, III)`. Motivo: o bloco só tinha o código interno (R-id do Anexo N); a remissão sai (seção 6).
115. [curso C9.4-10 (título)] deleção de marca: `— acréscimo da v2 (leitura externa A11, B14, C10; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa").
116. [curso C9.4-10 (definição)] deleção de frase inteira: `Conteúdo dos manuais, guias e resoluções do CIG: [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
117. [curso C9.4-11 (título)] deleção de marca: `— acréscimo da v2 (leitura externa B13; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa").
118. [curso C9.4-12 (título)] deleção de marca: `— acréscimo da v2 (leitura externa B16, C10; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa").
119. [curso C9.4-12 (definição)] deleção de oração de processo: `(os quatro princípios do artigo estão em C9.4-07)` → (nada). Motivo: remissão a código interno de bloco (seção 6).
120. [resumo] deleção de frase inteira: `Fontes: Anexo N (normas, seção 4; referencial R1 a R18, seção 5).` → (nada). Motivo: frase de proveniência com "Anexo N", sua seção e R-ids (seção 6).
121. [resumo] deleção de frase inteira: `Autor de periódico ou livro (F4 a F9) nunca é atribuído ao órgão.` → (nada). Motivo: regra de redação de produção com códigos de fonte (F4 a F9) (seção 6).
122. [resumo] troca mínima (op. 6): `| Só no curso e atribuído (paráfrase publicada pelo Ipea); texto do plano: [SEM FONTE — não afirmar] | R5 |` → `| Atribuído (paráfrase publicada pelo Ipea) | Cavalcante (Ipea, 2020) |`. Motivo: "Só no curso" é fala de cobertura de itens; "texto do plano: [SEM FONTE — não afirmar]" é frase marcada (seção 6); R-id trocado pela identificação.
123. [resumo] deleção de oração de processo: `(só curso e par)` → (nada). Motivo: parêntese de cobertura de itens (seção 6).
124. [resumo] deleção de marca: `(Anexo N do D6)` → (nada). Motivo: referência ao Anexo N e a outro lote (seção 6).
125. [resumo] deleção de oração de processo: `; ‘terceiro setor’ e ‘coprodução do bem público’ não têm definição legal ou institucional nas fontes do lote ([SEM FONTE — não afirmar])` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); a oração marcada também cita "fontes do lote".
126. [resumo] deleção de frase inteira: `Definição oficial de sustentabilidade de políticas públicas: [SEM FONTE — não afirmar].` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6).
127. [par P-07] deleção de oração de processo: `; só curso e par)` → `)`. Motivo: parêntese de cobertura de itens ("só curso e par") (seção 6).
128. [par P-60] deleção de frase inteira: `O par não julga a integridade como mecanismo (ponto bloqueado do BQ-0152).` → (nada). Motivo: fala de produção (cobertura de itens, cruzamento com item do banco, regra de redação, pedido de exceção); não é conteúdo para a candidata (seção 6); cita item do banco (BQ-0152).
129. [par P-63] deleção de marca: `— acréscimo da v2 (leitura externa A11; QA PENDENTE (R2))` → (nada). Motivo: marca de produção no campo Par (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa").
130. [pegadinha 5] troca mínima (op. 6): `no Ipea (R8, R9, R12), ‘NGP’ é` → `em Cavalcante (Ipea, 2018, pp. 19, 20 e 21), ‘NGP’ é`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
131. [pegadinha 8] troca mínima (op. 6): `(R7 diz confiança na rede)` → `(o artigo diz confiança na rede)`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
132. [pegadinha 8] troca mínima (op. 6): `(R7 diz teorias de rede)` → `(o artigo diz teorias de rede)`. Motivo: o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6).
133. [pegadinha 10] deleção de oração de processo: `; Anexo N, seção 5 (SEM FONTE b e c)` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); a remissão ao Anexo N e à sua seção 5 também sai (seção 6).
134. [pegadinha 27] troca mínima (op. 6): `as fontes do lote não trazem` → `as fontes do curso não trazem`. Motivo: "lote" é referência de produção (seção 6); trocado por "curso", que o próprio texto já usa.
135. [pegadinha 27] deleção de oração de processo: `Anexo N, seção 5 (SEM FONTE e);` → (nada). Motivo: "[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6); a remissão ao Anexo N e à sua seção 5 também sai (seção 6).
136. [pegadinha 32] troca mínima (op. 6): `Anexo N, seção 5 (SEM FONTE b e g).` → `Decreto 9.203/2017, art. 2º, II; R18.`. Motivo: a Base citava só o Anexo N (SEM FONTE b e g), que a seção 6 manda tirar; passa a valer a Base com os dispositivos que o próprio bloco cita (art. 2º, II, e a publicação da cadeia de valor das políticas públicas).
137. [pegadinha 54] deleção de oração de processo: `, e nenhum item os mistura` → (nada). Motivo: fala de produção (cobertura de itens, cruzamento com item do banco, regra de redação, pedido de exceção); não é conteúdo para a candidata (seção 6).
138. [pegadinha 54] troca mínima (op. 6): `misturar R21 com R5, em que` → `misturar o trecho do Referencial Básico de Governança Organizacional (TCU, 2020) com o de Cavalcante, em que`. Motivo: R-ids trocados pela identificação das publicações (seção 5 do Anexo N); o bloco já falava de "análise publicada pelo Ipea".
139. [pegadinha 57] troca mínima (op. 6): `equivalência de R25 (instâncias internas)` → `equivalência do referencial do TCU (instâncias internas)`. Motivo: R-id trocado por "referencial do TCU" (o bloco já identifica a publicação; evita parêntese dentro de parêntese).
140. [pegadinha 58] troca mínima (op. 6): `atribuir a R26 (que fala` → `atribuir ao referencial do TCU (que fala`. Motivo: R-id trocado por "referencial do TCU" (o bloco já identifica a publicação; evita parêntese dentro de parêntese).
141. [pegadinha 64] troca mínima (op. 6): `(R28, sentido genérico)` → `(referencial do TCU, sentido genérico)`. Motivo: R-id trocado por "referencial do TCU" (o bloco já identifica a publicação).
142. [pegadinha 73] deleção de oração de processo: `(lição do item real inapto BQ-0151, por causa do art. 14 revogado)` → (nada). Motivo: fala de produção (cobertura de itens, cruzamento com item do banco, regra de redação, pedido de exceção); não é conteúdo para a candidata (seção 6); cita item do banco (BQ-0151).
143. [pegadinha 74] troca mínima (op. 6): `(art. 5º, III; R27)` → `(art. 5º, III)`. Motivo: o bloco só tinha o código interno (R-id do Anexo N); a remissão sai (seção 6).
144. [pegadinha 77] deleção de marca: `(acréscimo da v2; leitura externa B12; QA PENDENTE (R2))` → (nada). Motivo: marca de produção ao fim da pegadinha (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa").
145. [pegadinha 78] deleção de marca: `(acréscimo da v2; leitura externa A11, B14, C10; QA PENDENTE (R2))` → (nada). Motivo: marca de produção ao fim da pegadinha (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa").
146. [pegadinha 79] deleção de marca: `(acréscimo da v2; leitura externa B13; QA PENDENTE (R2))` → (nada). Motivo: marca de produção ao fim da pegadinha (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa").
147. [pegadinha 80] deleção de marca: `(acréscimo da v2; leitura externa B16, C10; QA PENDENTE (R2))` → (nada). Motivo: marca de produção ao fim da pegadinha (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa").
148. [justificativa D4-36] deleção de oração de processo: `a nota do Anexo N registra que, na mesma página` → `na mesma página`. Motivo: a oração "a nota do Anexo N registra que" cita o Anexo N (seção 6); fica a informação (na mesma página, o referencial diz…).
149. [justificativa D4-48] deleção de oração de processo: `; a contagem exata de alíneas do rol vigente é admitida pela ficha` → (nada). Motivo: oração de regra de produção ("admitida pela ficha") (seção 6).
150. [justificativa D4-67] deleção de oração de processo: `é admitida pela ficha e` → (nada). Motivo: regra de produção ("admitida pela ficha") (seção 6); fica "a contagem exata não julga o conteúdo de nenhum princípio".

Trocas de rótulo (operação 2): 62 pegadinhas do curso ("[Desfeita por: X]" → "Base: X") e 62 pegadinhas da lista consolidada (" — Desfeita por: X" e " — Dispositivo ou trecho que a desfaz: X" → " Base: X").

Decisões de leitura que o orquestrador pode querer revisar (nenhuma altera conteúdo normativo):
- Siglas: NPM, NPG e pós-NPM como no canônico; a sigla ‘NGP’ só aparece onde o canônico a cita para explicá-la (o "(NGP = nova gestão pública (NPM))" das citações literais do Ipea foi mantido).
- Frases e orações marcadas "[SEM FONTE — não afirmar]" saíram com a marca (16 no curso, 3 no resumo; mais as remissões "SEM FONTE b/c/e/g" que apareciam dentro de Bases do curso e da lista de pegadinhas, 6 ao todo, que saíram com a remissão ao Anexo N). Os blocos C8.1-04 e C8.4-05, que no canônico eram quase só ressalva de "o que não se afirma", ficam com o que restava (uma frase de definição cada), o exemplo e a pegadinha; os títulos "o que não se afirma" foram mantidos. A Base de C8.4-05 citava só "Anexo N, seção 5 (SEM FONTE b e g)": passou a citar os dispositivos e a publicação que o próprio bloco cita (art. 2º, II, e a publicação da cadeia de valor das políticas públicas); a de C8.1-04 perdeu só a remissão ao Anexo N.
- Transparência passiva (C8.3-05): saiu o início da definição que falava da "exceção da ficha" e do "Anexo N do D6"; o texto do art. 10, caput, da LAI e a ressalva sobre o rótulo "passiva" ficaram. O art. 10 da LAI não consta do mapa deste lote; por isso o tópico 8.3 não o usa em baseLegal.
- Remissões do tipo "ver 8.x", "ver 9.x", "tratado em 9.1" foram mantidas (são números de tópico do edital, que são os `##` do curso); só as remissões a código de bloco (C8.1-02 etc.) saíram ou viraram o número do tópico (8.1).
- "[REVOGADO]" e "[REVOGADOS]" no curso, nos pares e no resumo foram mantidos: não constam da lista da seção 6 e distinguem artigo revogado de artigo vigente com letra.
- Palavra "isca" em justificativas (D4-37, D4-51, D4-60, D4-71): mantida; só "elemento-isca" consta da lista da seção 6 e não ocorre nas justificativas deste lote.
- Enunciados: o canônico não separa texto-base nem traz comando por item (a seção 5.1 traz "Julgue cada item como Certo ou Errado."): `textoBase` "" e `comando` "Julgue o item a seguir.", como no D5.
- Ordem dos itens no JSON: crescente pelo id (D4-01 a D4-79); no canônico os itens do caput (D4-74 a D4-79) vêm por último, como os ids já indicam.
- Falso positivo do validador: nenhum. Observação sobre o validador (não alterado): o padrão `\bR[12]\b` só pega R1 e R2; os demais R-ids (R3 a R31) são conferidos por este script e pelo de fidelidade (nenhum R-id restou em curso, resumo, pares, pegadinhas, justificativas ou tópicos).

## 4. Itens
- Total 79; C 41 / E 38.
- Por itemEdital: P1-DA-8: 6; P1-DA-8.1: 6; P1-DA-8.2: 10; P1-DA-8.3: 10; P1-DA-8.4: 7; P1-DA-9.1: 10; P1-DA-9.2: 10; P1-DA-9.3: 10; P1-DA-9.4: 10.
- volatil true: nenhum (todas as linhas "Marcas:" trazem REVERIFICAR=não e VOLÁTIL=não).
- Justificativa: linhas 1 e 2 unidas por um espaço; as edições são as da seção 3 (R-ids; D4-36, D4-48 e D4-67). As linhas "Difere de" e "Mecanismo" são campos à parte no canônico e não entram. Enunciado e gabarito: iguais caractere a caractere.
- Pares: 24; pegadinhas: 62 (P1-DA-8: 6; P1-DA-8.1: 4; P1-DA-8.2: 10; P1-DA-8.3: 7; P1-DA-8.4: 5; P1-DA-9.1: 5; P1-DA-9.2: 7; P1-DA-9.3: 6; P1-DA-9.4: 12); tópicos: 9 (P1-DA-8, P1-DA-8.1, P1-DA-8.2, P1-DA-8.3, P1-DA-8.4, P1-DA-9.1, P1-DA-9.2, P1-DA-9.3, P1-DA-9.4).

### 4.1 Tópicos (escritos à mão em D4_topicos_fonte.json; um por "##")
- P1-DA-8: emUmMinuto 3 frases; resumo 239 palavras; visuais: linha (Sucessão dos modelos, segundo Bresser-Pereira (ENAP, 2022)); compare (Modelo burocrático × nova gestão pública (NPM)).
- P1-DA-8.1: emUmMinuto 3 frases; resumo 235 palavras; visuais: esquema (Nova Governança Pública (NPG), segundo Bouckaert (ENAP, 2024)); compare (Nova gestão pública (NPM) × Nova Governança Pública (NPG)).
- P1-DA-8.2: emUmMinuto 3 frases; resumo 242 palavras; visuais: compare (Termo de colaboração × termo de fomento (Lei 13.019/2014, art. 2º)); baseLegal (Parceria público-privada e suas modalidades).
- P1-DA-8.3: emUmMinuto 3 frases; resumo 228 palavras; visuais: compare (Transparência ativa × transparência passiva); baseLegal (Texto do decreto e da LAI sobre divulgação).
- P1-DA-8.4: emUmMinuto 3 frases; resumo 198 palavras; visuais: fluxo (Elos da cadeia de valor das políticas públicas (Casa Civil, 2018)); baseLegal (Valor público no decreto).
- P1-DA-9.1: emUmMinuto 3 frases; resumo 246 palavras; visuais: compare (Governabilidade × governança (Referencial do TCU, 2020, p. 111)); baseLegal (Governança pública e estratégia no decreto).
- P1-DA-9.2: emUmMinuto 3 frases; resumo 229 palavras; visuais: esquema (Mecanismos de governança pública (Decreto 9.203/2017, art. 5º)); baseLegal (Os três mecanismos no decreto).
- P1-DA-9.3: emUmMinuto 3 frases; resumo 248 palavras; visuais: esquema (Valor público (Decreto 9.203/2017, art. 2º, II)); baseLegal (Valor público, resultados e avaliação no decreto).
- P1-DA-9.4: emUmMinuto 3 frases; resumo 234 palavras; visuais: tabela (Princípios, diretrizes e mecanismos do Decreto 9.203/2017); baseLegal (Comitê Interministerial de Governança: reunião e grupos de trabalho).
- Visuais pedidos na ordem e como ficaram: compare governança × governabilidade em 9.1, nova gestão pública (NPM) × Nova Governança Pública (NPG) em 8.1, termo de colaboração × termo de fomento em 8.2 e transparência ativa × passiva em 8.3 (com o acordo de cooperação na legenda de 8.2); esquema dos mecanismos liderança, estratégia e controle em 9.2; baseLegal com o Decreto 9.203/2017 em 8.3 (com a LAI), 8.4, 9.1, 9.2, 9.3 e 9.4, e com a Lei 11.079/2004 em 8.2; fluxo (elos da cadeia de valor das políticas públicas) em 8.4 e tabela (princípios, diretrizes e mecanismos) em 9.4, onde o pedido não indicava visual.
- Linha em 8 (patrimonialismo → burocracia → anos 80): só com os três marcos que o curso dá (monarquias absolutas; em substituição à patrimonialista; anos 80, países centrais). A NPG ficou fora da linha de propósito: o curso (8.1, "Evolução da NPG: o que não se afirma") não data a NPG nem afirma que ela substitui a NPM; ela aparece no compare de 8.1 e no esquema de 8.1.
- baseLegal: texto copiado da coluna de texto do mapa por script de busca do rótulo do dispositivo (letra a letra; `literal: true`; `conferido: 2026-10-20`, a data da coluna Consulta). Em 8.4, o art. 2º, II, entra só na parte inicial que o curso cita ("valor público - produtos e resultados gerados, preservados ou entregues pelas atividades de uma organização"), trecho copiado letra a letra da mesma linha do mapa; a continuação é da folha 9.3. Nenhum dispositivo revogado (arts. 7º a 15 e 20 do Decreto 9.203 sem letra): 9.4 usa os arts. 8º-B, caput, 10-B, II e III, e 12-A, caput; o art. 11-A, caput, ficou de fora porque cita órgão que o curso não afirma existir. Em 8.3 não há o art. 10 da LAI, que não consta do mapa; o compare traz a transparência passiva com o que o curso diz do art. 10, caput. O referencial oficial (TCU, Casa Civil, Ipea, ENAP, CGU) não entra em baseLegal, só nos quadros BASE LEGAL do curso.
- Arquivos dos tópicos: D4_topicos_fonte.json é gravado por scripts/gerar_topicos_D4.py (os textos estão nele, escritos à mão; o script só busca no mapa o texto de cada dispositivo de baseLegal); o formatador lê o JSON pronto e confere que as chaves são as dos blocos ##.
- Texto dos tópicos: cada frase vem do curso da própria folha; a conferência de fidelidade checa que todo número do tópico existe no curso da folha, que todo artigo de baseLegal é citado no curso da folha, a data da consulta e a ausência de artigo revogado.

## 5. Saída do validador
Comando: `python3 -I saida/gcb/DA_plataforma/scripts/validar_da.py saida/gcb/DA_plataforma/D4_plataforma.json saida/gcb/D4_v2_1.md saida/gcb/D4_anexo_N_mapa_normativo.md`
```
D4_plataforma.json: lote D4; itensEdital 9; blocos ## 9; itens 79 (C 41 / E 38); pares 24; pegadinhas 62; topicos 9
quadros: {'EXEMPLO PARLAMENTAR': 62, 'BASE LEGAL': 62, 'PEGADINHA PROVÁVEL': 62, 'DEFINIÇÃO': 62}
RESULTADO: 0 FALHA, 0 AVISO
```

## 6. Conferência de fidelidade
Comando: `python3 -I saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D4.py`

### 6.1 Curso: palavras do bloco de saída × bloco de origem (62 blocos)

Origem = título + definição + exemplo + pegadinha do bloco, com os rótulos "Definição:", "Exemplo (Legislativo, hipotético):", "Pegadinha provável:" e "[Desfeita por:" mantidos na origem (o alinhamento os classifica), e com os códigos R1 a R31 e F1 a F22 retirados. Saída = título + texto dos três quadros, sem os rótulos de quadro e sem a lista BASE LEGAL. Cada diferença é supressão (só frase com marca de produção) ou acréscimo (só vocabulário de identificação das publicações, conectivos mínimos e "Base").

- C8.0-01: supressões 1; acréscimos 2; trocas 1; linhas Fonte 1
- C8.0-02: supressões 1; acréscimos 3; trocas 3; linhas Fonte 2
- C8.0-03: supressões 0; acréscimos 2; trocas 1; linhas Fonte 1
- C8.0-04: supressões 0; acréscimos 5; trocas 2; linhas Fonte 2
- C8.0-05: supressões 2; acréscimos 4; trocas 4; linhas Fonte 2
- C8.0-06: supressões 1; acréscimos 6; trocas 2; linhas Fonte 2
- C8.1-01: supressões 1; acréscimos 3; trocas 2; linhas Fonte 1
- C8.1-02: supressões 0; acréscimos 4; trocas 2; linhas Fonte 3
- C8.1-03: supressões 0; acréscimos 10; trocas 6; linhas Fonte 3
- C8.1-04: supressões 1; acréscimos 2; trocas 2; linhas Fonte 1
- C8.2-01: supressões 0; acréscimos 0; trocas 4; linhas Fonte 0
- C8.2-02: supressões 3; acréscimos 2; trocas 2; linhas Fonte 2
- C8.2-03: supressões 0; acréscimos 0; trocas 1; linhas Fonte 0
- C8.2-04: supressões 0; acréscimos 0; trocas 1; linhas Fonte 0
- C8.2-05: supressões 0; acréscimos 0; trocas 1; linhas Fonte 0
- C8.2-06: supressões 0; acréscimos 0; trocas 1; linhas Fonte 0
- C8.2-07: supressões 0; acréscimos 0; trocas 1; linhas Fonte 0
- C8.2-08: supressões 0; acréscimos 0; trocas 1; linhas Fonte 0
- C8.2-09: supressões 0; acréscimos 0; trocas 1; linhas Fonte 0
- C8.2-10: supressões 2; acréscimos 0; trocas 1; linhas Fonte 0
- C8.3-01: supressões 2; acréscimos 1; trocas 2; linhas Fonte 2
- C8.3-02: supressões 1; acréscimos 2; trocas 2; linhas Fonte 2
- C8.3-03: supressões 0; acréscimos 0; trocas 2; linhas Fonte 0
- C8.3-04: supressões 0; acréscimos 6; trocas 1; linhas Fonte 2
- C8.3-05: supressões 1; acréscimos 3; trocas 1; linhas Fonte 1
- C8.3-06: supressões 0; acréscimos 0; trocas 1; linhas Fonte 0
- C8.3-07: supressões 1; acréscimos 2; trocas 3; linhas Fonte 2
- C8.4-01: supressões 1; acréscimos 0; trocas 1; linhas Fonte 0
- C8.4-02: supressões 0; acréscimos 0; trocas 2; linhas Fonte 0
- C8.4-03: supressões 0; acréscimos 1; trocas 1; linhas Fonte 2
- C8.4-04: supressões 1; acréscimos 1; trocas 1; linhas Fonte 1
- C8.4-05: supressões 0; acréscimos 2; trocas 2; linhas Fonte 2
- C9.1-01: supressões 0; acréscimos 0; trocas 1; linhas Fonte 0
- C9.1-02: supressões 2; acréscimos 2; trocas 1; linhas Fonte 2
- C9.1-03: supressões 1; acréscimos 2; trocas 1; linhas Fonte 1
- C9.1-04: supressões 1; acréscimos 5; trocas 1; linhas Fonte 2
- C9.1-05: supressões 0; acréscimos 3; trocas 2; linhas Fonte 1
- C9.2-01: supressões 0; acréscimos 1; trocas 1; linhas Fonte 1
- C9.2-02: supressões 0; acréscimos 2; trocas 3; linhas Fonte 1
- C9.2-03: supressões 0; acréscimos 2; trocas 2; linhas Fonte 1
- C9.2-04: supressões 0; acréscimos 3; trocas 1; linhas Fonte 1
- C9.2-05: supressões 0; acréscimos 0; trocas 1; linhas Fonte 0
- C9.2-06: supressões 0; acréscimos 0; trocas 1; linhas Fonte 0
- C9.2-07: supressões 2; acréscimos 0; trocas 1; linhas Fonte 0
- C9.3-01: supressões 0; acréscimos 0; trocas 1; linhas Fonte 0
- C9.3-02: supressões 1; acréscimos 0; trocas 1; linhas Fonte 1
- C9.3-03: supressões 1; acréscimos 3; trocas 1; linhas Fonte 1
- C9.3-04: supressões 0; acréscimos 0; trocas 1; linhas Fonte 0
- C9.3-05: supressões 1; acréscimos 3; trocas 1; linhas Fonte 1
- C9.3-06: supressões 1; acréscimos 1; trocas 1; linhas Fonte 1
- C9.4-01: supressões 0; acréscimos 0; trocas 1; linhas Fonte 0
- C9.4-02: supressões 1; acréscimos 0; trocas 1; linhas Fonte 0
- C9.4-03: supressões 1; acréscimos 0; trocas 1; linhas Fonte 0
- C9.4-04: supressões 1; acréscimos 0; trocas 1; linhas Fonte 0
- C9.4-05: supressões 0; acréscimos 0; trocas 1; linhas Fonte 0
- C9.4-06: supressões 1; acréscimos 0; trocas 1; linhas Fonte 0
- C9.4-07: supressões 0; acréscimos 0; trocas 1; linhas Fonte 0
- C9.4-08: supressões 0; acréscimos 0; trocas 1; linhas Fonte 0
- C9.4-09: supressões 0; acréscimos 0; trocas 1; linhas Fonte 0
- C9.4-10: supressões 2; acréscimos 0; trocas 1; linhas Fonte 0
- C9.4-11: supressões 1; acréscimos 0; trocas 1; linhas Fonte 0
- C9.4-12: supressões 2; acréscimos 0; trocas 1; linhas Fonte 0

Total curso: supressões 38; acréscimos 88; trocas 92; blocos com defeito 0.

### 6.2 Resumo (seção 2)

- Supressões 6; acréscimos 23; trocas 6.

### 6.3 Pares (24)

Origem = campos "Par", "Diferença" e "Como a banca troca" (a coluna "Base de cada lado" não entra); saída = a + b + como. Palavras acrescentadas permitidas: as do rótulo " Como a banca troca: ".

- Pares com defeito: 0.

### 6.4 Pegadinhas (62)

- Pegadinhas com defeito: 0.

### 6.5 Itens (79): enunciado, gabarito, itemEdital e justificativa

- Itens com defeito: 0. (Enunciado e gabarito: iguais caractere a caractere; justificativa: alinhada por palavras.)

### 6.6 Tópicos (9)

- Problemas nos tópicos (número ausente do curso da folha; dispositivo de baseLegal que não bate letra a letra com o mapa, sem a data 2026-10-20, revogado ou fora do curso): 0.

### 6.7 Códigos internos no JSON inteiro: nenhum R-id nem F-id.

RESULTADO DA CONFERÊNCIA DE FIDELIDADE: 0 defeito(s).

## Errata de forma — QA final 20/10/2026
Origem: QA final do pacote v1.13 (gbq-cqe, 20/10/2026), achados 1, 6 e 7. Achado 1: a palavra de produção "folha" no texto exibido (a candidata não conhece "folha"; o validador passou a acusá-la). Regra da ordem: frase que só fala do processo ou da organização da produção é DELETADA; remissão útil ao estudo vira "subitem". Achado 6: o resumo do tópico P1-DA-8.4 deve usar só o curso de 8.4. Achado 7: repetição da identificação da publicação criada pela troca dos R-códigos em D4-62, D4-75 e D4-78, e parênteses duplos em D4-38. Só forma: nenhum enunciado, gabarito, itemEdital ou id foi tocado.

### Achados 1 e 7: curso, resumo do lote e justificativas (edições no formatador; conferidas pela conferência de fidelidade)
1. [curso C8.2-01 (definição)] troca mínima (op. 6): `Nesta folha vale o meio` → `Neste subitem vale o meio`. Motivo: errata de forma (QA final 20/10/2026, achado 1): "folha" é termo de produção (seção 6); a remissão serve ao estudo e passa a "subitem", o número é o do `##` do curso.
2. [curso C8.2-01 (definição)] troca mínima (op. 6): `é da folha 8.4.` → `é do subitem 8.4.`. Motivo: errata de forma (QA final 20/10/2026, achado 1): "folha" é termo de produção (seção 6); a remissão serve ao estudo e passa a "subitem", o número é o do `##` do curso.
3. [curso C8.4-02 (definição)] troca mínima (op. 6): `é da folha 8.2;` → `é do subitem 8.2;`. Motivo: errata de forma (QA final 20/10/2026, achado 1): "folha" é termo de produção (seção 6); a remissão serve ao estudo e passa a "subitem", o número é o do `##` do curso.
4. [curso C9.1-05 (definição)] troca mínima (op. 6): `é da folha 9.2)` → `é do subitem 9.2)`. Motivo: errata de forma (QA final 20/10/2026, achado 1): "folha" é termo de produção (seção 6); a remissão serve ao estudo e passa a "subitem", o número é o do `##` do curso.
5. [curso C9.4-03 (definição)] deleção de frase inteira: `Distribuição por folha: ver 8.x (IV, VIII, IX, XI), 9.2 (V, X) e 9.3 (I, III, VII).` → (nada). Motivo: errata de forma (QA final 20/10/2026, achado 1): a frase só diz como a produção distribuiu os incisos do art. 4º entre os blocos ("Distribuição por folha"); o estudo não depende dela.
6. [resumo] troca mínima (op. 6): `(caput) e folhas 8.1 a 8.4.**` → `(caput) e subitens 8.1 a 8.4.**`. Motivo: errata de forma (QA final 20/10/2026, achado 1): "folha" é termo de produção (seção 6); o título do resumo do item 8 aponta os subitens 8.1 a 8.4 (números dos `##` do curso).
7. [justificativa D4-14] troca mínima (op. 6): `tratada na folha 8.4` → `tratada no subitem 8.4`. Motivo: errata de forma (QA final 20/10/2026, achado 1): "folha" é termo de produção (seção 6); a remissão serve ao estudo e passa a "subitem", o número é o do `##` do curso.
8. [justificativa D4-27] deleção de oração de processo: `; o meio (integração entre níveis e esferas) é ponto da folha 8.2` → (nada). Motivo: errata de forma (QA final 20/10/2026, achado 1): a oração só situa o "meio" como ponto de outra folha da produção (seção 7 da especificação: frase que só fala do processo fica fora); o item trata da finalidade da diretriz.
9. [justificativa D4-30] troca mínima (op. 6): `é tratada na folha 9.3` → `é tratada no subitem 9.3`. Motivo: errata de forma (QA final 20/10/2026, achado 1): "folha" é termo de produção (seção 6); a remissão serve ao estudo e passa a "subitem", o número é o do `##` do curso.
10. [justificativa D4-38] troca mínima (op. 6): `(TCU, 2020) (única fonte institucional da distinção) e não mistura` → `(TCU, 2020), única fonte institucional da distinção, e não mistura`. Motivo: errata de forma (QA final 20/10/2026, achado 7): a troca do código de referencial pelo nome da publicação deixou dois parênteses em sequência; o segundo vira aposto entre vírgulas (nenhuma palavra muda; só a pontuação).
11. [justificativa D4-49] deleção de oração de processo: `, ponto da folha 9.1)` → `)`. Motivo: errata de forma (QA final 20/10/2026, achado 1): o aposto só situa o "alinhamento" como ponto de outra folha da produção; fica "(sem o alinhamento)".
12. [justificativa D4-52] troca mínima (op. 6): `da folha 9.3)` → `do subitem 9.3)`. Motivo: errata de forma (QA final 20/10/2026, achado 1): "folha" é termo de produção (seção 6); a remissão serve ao estudo e passa a "subitem", o número é o do `##` do curso.
13. [justificativa D4-62] troca mínima (op. 6): `; o guia prático de análise ex post (Casa Civil, 2018) acrescenta` → `; o mesmo guia acrescenta`. Motivo: errata de forma (QA final 20/10/2026, achado 7): a troca de R30 e R31 pelo nome da publicação repetiu "o guia prático de análise ex post (Casa Civil, 2018)"; a segunda menção volta a "o mesmo guia" (a primeira já identifica a publicação).
14. [justificativa D4-63] deleção de oração de processo: `(ponto da folha 8.4)` → (nada). Motivo: errata de forma (QA final 20/10/2026, achado 1): o parêntese só situa os "elos da cadeia de valor" como ponto de outra folha da produção (frase de processo).
15. [justificativa D4-75] troca mínima (op. 6): `, e o artigo de Bresser-Pereira (ENAP, 2022) a chama` → `, e o mesmo artigo a chama`. Motivo: errata de forma (QA final 20/10/2026, achado 7): a troca de R1 e R2 pelo nome da publicação repetiu "o artigo de Bresser-Pereira (ENAP, 2022)"; a segunda menção volta a "o mesmo artigo".
16. [justificativa D4-78] troca mínima (op. 6): `; o artigo de Bresser-Pereira (ENAP, 2022) acrescenta` → `; o mesmo artigo acrescenta`. Motivo: errata de forma (QA final 20/10/2026, achado 7): a troca de R2 pelo nome da publicação repetiu "o artigo de Bresser-Pereira (ENAP, 2022)"; a segunda menção volta a "o mesmo artigo".

### Achados 1 e 6: tópicos (edições em D4_topicos_fonte.json, gerado por scripts/gerar_topicos_D4.py)
1. [topicos P1-DA-8.2 resumo] troca mínima: `é de outra folha` → `é do subitem 8.4`. Motivo: achado 1: "folha" é termo de produção; a remissão serve ao estudo e passa a "subitem" (o curso de 8.2 traz agora "a finalidade (valor público) é do subitem 8.4").
2. [topicos P1-DA-8.4 resumo] deleção de frase inteira: `A continuação do inciso, sobre as respostas efetivas e úteis às necessidades ou às demandas de interesse público, é tratada em 9.3.` → (nada). Motivo: achado 6: a frase traz conteúdo do curso de 9.3 ("respostas efetivas e úteis…") que não está no curso de 8.4, e a remissão "é tratada em 9.3" (o FORMATO, seção 5, pede só o curso do próprio tópico).
3. [topicos P1-DA-8.4 resumo] deleção de oração: `; o meio, a integração entre níveis e esferas, é tratado em 8.2` → (nada; o período termina em "…gerar, preservar e entregar valor público."). Motivo: achado 6: remissão "é tratado em 8.2" e conteúdo do tópico 8.2.
Resultado do 8.4: resumo com 198 palavras (faixa 150–250), só com frases do curso de 8.4, sem remissão a outro tópico e sem fato novo (a conferência de tópicos confere números e artigos contra o curso do tópico).

Nota de formato (C9.4-03): com a deleção de "Distribuição por folha…" a definição do bloco fica com 2 frases e, pela regra geral do curso (lista só a partir de 3 frases, operação 4), passa de lista de 3 itens a parágrafo único; nenhuma palavra muda além da deleção.

Total: 16 mudanças no curso/resumo do lote/justificativas + 3 nos tópicos = 19 no D4.

