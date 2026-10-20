# D3_parecer_R2_gcb-cqfp.md — T-76 — 2026-10-20 — gerado por gcb-cqfp
PARECER R2 — LOTE D3 v2 (saida/gcb/D3_v2.md, gcb-cpp; SHA-256 9248c4a052aa3961d39aa910aa0de7a5a12d072946114a2ea2f4873e014a6bc5; 307.578 bytes; UTF-8, LF; 1.959 linhas). Conferido contra o R1 (saida/gcb/D3_parecer_R1_gcb-cqfp.md, 324cb160…b402), a v1 (saida/gcb/D3_v1.md, a97d5b82…a025db, a mesma do R1 e a declarada como base na seção 8 da v2), a D1 da GCB (saida/gcb/D3_D1_GCB_v2_2026-10-20.md, 35b09685…524e), a leitura externa (saida/gcb/D3_leitura_critica.md, 698929e5…e0d099), a ficha (saida/gcb/D3_ficha_lote.md, 71823790…e51a81a) e o Anexo N (saida/gcb/D3_anexo_N_mapa_normativo.md, 2ef58f9b…2ff1df), única base de texto legal. Modelo: saida/gcb/D5_parecer_R2_gcb-cqfp.md. A gcb-cqfp revisa e não reescreve: os textos da seção 9 são ajustes pontuais fixados. Scripts em python3 -I, no scratchpad; navegador não usado.

## 0. Resultado
- Itens: 71 (D3-01 a D3-81, sem os 10 ids reprovados no R1: D3-19, 31, 39, 42, 48, 50, 57, 60, 65 e 69). **APROVADO 69; APROVADO COM AJUSTE 2 (D3-81 e D3-37); REPROVADO 0. Reprovação no R2: 0/71 = 0%** (limite do gate: 30%). **Não há gate.**
- Os 11 itens "QA PENDENTE (R2)" foram conferidos um a um (seção 6): 9 com o texto fixado no R1 entrado literalmente, todos APROVADOS; D3-37 (só a linha 2 da justificativa) e D3-81 (novo) APROVADOS COM AJUSTE de texto, sem mudança de gabarito, ponto de julgamento ou [TS]. Os outros 60 são idênticos à v1 em todos os campos (script) e mantêm o APROVADO do R1; 15 deles só mudaram de posição.
- Decisões da GCB (D1-T76-01 a 08): todas aplicadas (seção 3). Ordem de apresentação igual, posição a posição, à tabela 3.2 da D1; teste de ordem refeito pela QA e igual ao da D1.
- Leitura externa (seção 0.1 da v2): APROVADA COM UMA RESSALVA. Os 14 acatamentos têm lastro literal e vigente no Anexo N e o artigo certo; as 46 recusas estão justificadas; nenhuma tese de tribunal nem dispositivo com "(Vide ADI …)" entrou; uma pegadinha (G-76) reproduz a redação do leitor (seção 5).
- Blocos: curso, resumo e pares APROVADOS (ajustes do R1 literais; acréscimos conferidos); pegadinhas APROVADO COM AJUSTE (G-76); contagens e sequência APROVADO; bloco à GCB APROVADO COM AJUSTE (notas à GBQ incompletas; uma afirmação inexata na seção 7.5).
- **Veredito geral: APROVADO COM AJUSTES RESIDUAIS.** São 7 ajustes de texto exato (seção 9): 5 a aplicar (2 em item, 3 fora de item), 1 condicionado à decisão da GCB (linha 2) e 1 opcional. Podem ser aplicados por errata na reconciliação ou numa v2.1, com conferência só do diff, sem nova rodada sobre os itens.

## 1. Evidência e não regressão (por script)
1. **Itens, campo a campo.** Um script leu a versão do estudante (5.1) e o gabarito comentado (5.2) das duas versões e comparou enunciado e cada campo (cabeçalho, folha, ponto, formato, gabarito, justificativas, base, mecanismo, troca, difere, marcas).
   - Saíram exatamente os 10 reprovados; entrou só o D3-81.
   - Mudaram só os 11 itens declarados: D3-06, 08, 13, 25, 26, 33, 37, 66, 71, 74 e 81. Nos outros 60, nada mudou além da posição (em D3-70 e D3-80, só a linha "---" vizinha, efeito da reordenação).
   - A ordem da 5.1 é igual à da 5.2; os 71 blocos têm todos os campos fixos; cabeçalho e linha de marcas são coerentes nos 71 ([TS], BASE DOUTRINÁRIA e "QA PENDENTE (R2)"); o campo "Alteração na v2" existe exatamente nos 11 marcados.
2. **Fora dos itens.** As linhas novas ou alteradas das seções 1 a 4 (44 linhas) são só as declaradas: nota de abertura do curso; C5.1-03, C6.2-03 e C7-15 (títulos marcados "[alterado na v2 …]" e textos fixados); C7-21 a C7-24 (acréscimos); resumo, "Sistema e dolo" e linha do art. 16, § 13, mais a nota de alterações; abertura dos pares e P-61 a P-68; abertura das pegadinhas e G-71 a G-78. As linhas da v1 que saíram são os cabeçalhos "Parte A/B", as aberturas por parte (fundidas em uma) e os textos substituídos pelos ajustes. A tabela de pares é única. Nada além do declarado.
3. **Citações novas.** Script de citações (art., §, inciso, alínea) da Lei 8.429 contra as linhas da seção 4.9 do Anexo N e contra a lista dos 26 bloqueados (ficha 3.4), sobre as 51 linhas novas ou alteradas que citam a lei (0.1, C7-21 a C7-24, P-61 a P-68, G-71 a G-78, resumo): 174 citações, todas existentes; 0 dispositivo bloqueado como base. As únicas acusações foram artefato de leitura (CF, art. 37, tomado como art. da Lei 8.429; "art. 17, caput (remissão a ADI, bloqueado)", que é a menção de não uso). Validei o teste com citações falsas plantadas (art. 9º, XV; art. 10, § 3º; art. 11, XIII; art. 11, § 6º; art. 12, § 11; art. 1º, § 9º; art. 8º-B; art. 17-B, § 3º bloqueado): acusou todas. Nas bases dos 11 itens alterados, as citações (Lei 9.784, arts. 12 e 15; CF, arts. 37, § 6º, 49, V, e 84, IV e VI; CC, art. 43; Lei 8.429, arts. 9º, caput, e 11, caput, XI e § 5º) existem no Anexo N e nenhuma é bloqueada.
4. **Fonte oficial.** Reabri em 20/10/2026, às 12:15 UTC, por curl com User-Agent de navegador, sem parâmetro, https://planalto.gov.br/ccivil_03/leis/l8429compilada.htm e https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm (URLs idênticas às do Anexo N e da proveniência): HTTP 200; 173.931 e 923.899 bytes, iguais aos do Anexo N. O texto do Anexo N de 36 dispositivos usados na v2 (art. 1º, §§ 1º, 6º e 7º; 8º; 8º-A, caput e parágrafo único; 9º, caput, II, III e IV; 10, caput, IV, V, VIII, XIII e § 2º; 11, caput, III, V, VII, XI, XII e §§ 1º, 3º, 4º e 5º; 12, caput e §§ 2º, 5º e 9º; 14, caput e § 3º; 16, §§ 13 e 14; 17, § 19, I; 20, caput) aparece literalmente no texto não tachado de hoje: 36/36. CC, art. 43: confere.
5. **Jurisprudência e ADI.** Nos 71 enunciados, pontos e justificativas: 0 ocorrência de STF, STJ, tribunal, jurisprudência, súmula, tema, ADI, "imprescritível" ou doutrinador. Nas linhas novas do curso, dos pares e das pegadinhas: 0. As menções a STF, ADI e jurisprudência na seção 0.1 estão só nos motivos de recusa.

## 2. Conferência das respostas aos 34 pontos do R1
| Ponto R1 | Objeto | Resposta da v2 | Texto fixado entrou literal? | Veredito R2 |
|---|---|---|---|---|
| 1 | D3-06 | Acolhido | Sim (enunciado) | APROVADO |
| 2 | D3-08 | Acolhido | Sim (enunciado e troca) | APROVADO |
| 3 | D3-13 | Acolhido | Sim (enunciado e linha 2) | APROVADO |
| 4 | D3-25 | Acolhido; linha 2 alinhada (declarada) | Sim (enunciado, ponto, C3) | APROVADO |
| 5 | D3-26 | Acolhido; linha 2 alinhada (declarada) | Sim (enunciado) | APROVADO |
| 6 | D3-33 | Acolhido | Sim (enunciado, linha 2, campo "Difere") | APROVADO |
| 7 | D3-66 | Acolhido | Sim (enunciado, "Difere") | APROVADO |
| 8 | D3-71 | Acolhido | Sim (enunciado, ponto, linhas 1 e 2, troca, base). Mecanismo "E6" escrito por extenso, no padrão do arquivo | APROVADO |
| 9 | D3-74 | Acolhido; linha 2 alinhada (declarada) | Sim (enunciado e base) | APROVADO |
| 10 | D3-19 | Acolhido em parte: sai sem substituto (D1) | — | APROVADO (decisão da GCB) |
| 11 | D3-31 | Acolhido: D3-81 | Ponto de julgamento literal do R1 | APROVADO; D3-81 com ajuste (seção 4) |
| 12 a 19 | D3-39, 42, 48, 50, 57, 60, 65, 69 | Acolhidos: saem sem substituto, falta declarada | — | APROVADO (D1, seção 1.2) |
| 20 | C6.2-03 | Acolhido; consequência no D3-37 | Sim | APROVADO; D3-37 com ajuste (seção 6) |
| 21 | C5.1-03 e C7-15 | Acolhido | Sim (os dois exemplos, com a frase final de hipótese mantida) | APROVADO |
| 22 | Resumo do item 7 | Acolhido | Sim (art. 1º, § 1º; art. 16, § 13) | APROVADO |
| 23 | Contagens e teste de ordem | Acolhido em parte: ordem da D1, não a regra "só na folha 7" | Refeitos pela QA (seção 7) | APROVADO |
| 24 | Lista dos pontos | Acolhido | 71 pontos da 7.3 iguais, posição a posição, aos campos do 5.2 (script); 0 duplicata | APROVADO |
| 25 | Formato da junção | Acolhido em parte (arquivo único, D1) | Linha 1 conforme; linha 2 sem o qualificador da D1 | APROVADO COM RESSALVA (seção 8, b; ajuste 6) |
| 26 | Proporção C | Acolhido (contagem da D1) | Conferida (seção 7) | APROVADO |
| 27 a 31 | Decisões da GCB | Remissão à D1 | — | APROVADO (seção 3) |
| 32 | Leitura crítica | Acolhido em parte (seção 0.1; arquivo neutro não regerado) | — | APROVADO; pendente da GCB (seção 8, a) |
| 33 | Notas à GBQ | Acolhido | Consolidação incompleta | APROVADO COM AJUSTE (ajuste 4) |
| 34 | QA PENDENTE | Acolhido | 11 marcados, conferidos | APROVADO |

Contagens da seção 0 da v2 conferem (script): 34 pontos; 29 ACOLHIDO e 5 ACOLHIDO EM PARTE (10, 23, 25, 30 e 32); 0 NÃO ACOLHIDO.

## 3. Decisões da GCB aplicadas
1. **Retiradas (D1-T76-02).** Os 10 reprovados saíram de todas as seções de conteúdo; nenhum id foi reutilizado; o único id novo é o D3-81. Os ids reprovados só aparecem na seção 0, no título da seção 5, no campo "Alteração na v2" do D3-81 e no bloco à GCB (D3-39, como limite da D1); a seção 7.5 omite esta última ocorrência (ajuste 5). Nenhum "Difere" e nenhuma nota citam reprovado.
2. **Folhas com menos de 10 (D1-T76-01 e 03, seção 1.4).** 5.1 = 10; 5.2 = 9; 6.1 = 10; 6.2 = 9; 6.3 = 7; 6.4 = 8; 6.5 = 8; 7 = 10; lote 71. A folha 6.3 tem exatamente os 7 ids da D1 (D3-41, 43, 44, 45, 46, 47, 49), 2 C/5 E. "Faltam para 20" (86) igual ao da D1.
3. **D3-81 (D1-T76-02, seção 1.3).** Id, folha, posição 30, ponto de julgamento literal, gabarito C, sem [TS], SIT com moldura neutra, só o Código Civil, "difere de" D3-32, 36, 38 e 70 com o porquê de cada um, nota à GBQ: conferidos. Um limite da D1 não foi cumprido à letra (seção 4).
4. **Ordem (D1-T76-06, seção 3.2).** Um script comparou as 71 posições da v2 (5.1 e 5.2) com a tabela 3.2 da D1 (posição, folha, id, gabarito e [TS]): iguais nas 71. Os 18 movimentos declarados são os da D1; 5.1 e 6.1 intactas. A regra da fronteira (D3-71 e D3-72 no início da folha 7) foi abandonada, como a D1 decidiu.
5. **D3-67 (D1-T76-04).** Item intacto (AP); BASE DOUTRINÁRIA da 6.5 = 5 (teto 8); convenções da v2 registram o adendo à lista fechada. Nota "D3-61 e D3-67 nunca juntos" mantida.
6. **Adendo do CC não antecipado (D1-T76-05).** Nenhum artigo do CC além do 43 foi usado em lugar nenhum da v2; as sugestões que dependiam dele foram recusadas com remissão à T-100.
7. **Arquivo único e seção 0.1 (D1-T76-08).** Cumprido. Divergências de forma declaradas pela própria produção (linha 2 e preâmbulo único): seção 8.

## 4. D3-81 (novo): APROVADO COM AJUSTE
- **Mérito.** CC, art. 43: "ressalvado direito regressivo contra os causadores do dano, se houver, por parte destes, culpa ou dolo". O item afirma que o regresso depende de culpa ou dolo do causador: C seguro, pela letra; C2 em SIT; moldura neutra (sem Legislativo); não cita a CF; não trata da responsabilidade da pessoa jurídica (a primeira oração é premissa do cenário, não objeto de julgamento). Estilo Cebraspe: afirmação única, sem "exceto".
- **Limite da D1 não cumprido à letra.** A D1 (seção 1.3) diz que o D3-81 "não usa 'assegura × ressalva' (ponto do D3-34) nem os destinatários do regresso (ponto do D3-33 ajustado)". O enunciado diz "o direito regressivo **ressalvado** pelo art. 43 do Código Civil contra **o causador do dano**". Não há o contraste, mas os dois elementos literais do CC estão no item: quem lê o D3-81 tem o verbo do CC (que decide o D3-34, E) e o destinatário do CC (metade do D3-33, C), na mesma folha. A seção 8 da v2, escolha (5), declara o limite cumprido; não está. O ajuste 1 tira os dois elementos sem mudar gabarito, ponto, base, mecanismo nem justificativas.
- **Vizinhança com o D3-32 (registro técnico, sem efeito no veredito).** O D3-81 (C: no CC o regresso depende de culpa ou dolo) e o D3-32 (E: na CF o regresso cabe em qualquer caso, independentemente de dolo ou culpa) julgam a mesma condição em dois dispositivos de redação equivalente. Pelo precedente do R1 (D3-41 × D3-49, distintos pelo dispositivo) e pela própria sugestão do R1 e da D1, o par fica, com a nota à GBQ (nunca no mesmo simulado). Mas a ordem da D1 os põe em posições contíguas (30 e 31), o que, num teste de lote, entrega a pista. Ver seção 8, f.

## 5. Registro de acatamento da leitura externa (seção 0.1 da v2)
1. **Forma.** Tabela "Sugestão | Texto curto | Decisão | Motivo | Onde entrou", 60 linhas (A1–A20, B1–B30, C1–C10), totais conferidos: A 8/12, B 6/24, C 0/10; nenhuma "em parte". Resíduos de interface ignorados. Resposta dentro do prazo de 48 horas.
2. **Acatamentos (A12 a A19; B10 a B15): lastro literal e artigo certo.** Conferi a letra de cada dispositivo usado contra a seção 4.9 do Anexo N e contra a página de hoje (seção 1, n. 4). As correções de base que o registro declara se sustentam: A12 apoia a imposição das cominações no art. 20, caput, e não no art. 17, caput (bloqueado); A16 acrescenta o art. 11, § 4º; B12 fica só no art. 11, XII, sem afirmar o texto do § 1º do art. 37 da CF, que o Anexo N não transcreve; B15 com o art. 16, § 14, e o art. 9º. Nenhum acatamento depende de jurisprudência, de doutrina sem dispositivo, de dispositivo bloqueado ou de tema vedado; todos estão no item 7 do edital. As remissões "onde já estava" conferem (C7-03, C7-05, C7-06 a C7-09, C7-13, C7-14, G-53, G-55, G-57).
3. **Recusas: justificadas.** Lei 9.784 fora dos arts. 11 a 17 (A1 a A5, B1 a B7, C1, C3); CF, arts. 87, 129, 144 e 5º, XXXVI e XLIX, e CC, arts. 393, 402, 403, 944 e 945, fora do Anexo N (A8, A10, A11, B8, B9, C5, C7); CTN, art. 77 (A9); Lei 4.717, art. 3º (A7, C4). Pontos bloqueados do D1 conferidos no D1_v2.md: D1-32 (rol do art. 2º), D1-34 (inexistência dos motivos), D1-35 (ilegalidade do objeto), D1-40 (decisão de recursos). Os 26 dispositivos com "(Vide ADI …)" (A20, B16 a B29, C8, C9) e os temas vedados (B18, B30, C2, C5, C6, C10) foram recusados. Em A6, o art. 2º, b e c, da Lei 4.717 está no Anexo N; a recusa se sustenta pelo escopo (vícios do ato são do item 2) e pelo D1-35.
4. **Nada de item.** Nenhum item foi criado ou alterado por causa da leitura (script: os 11 itens alterados correspondem só a pontos do R1 e da D1).
5. **Cópia da redação do leitor (ficha 9; precedente do D5, G-68).** Comparei, por script, cada par e pegadinha novos com a sugestão de origem (maior trecho comum em palavras, fora da letra da lei).
   - P-61 a P-68: semelhança 0,10 a 0,24; maior trecho comum de 3 a 6 palavras, quase sempre letra da lei ou nome do tema. Sem cópia.
   - G-72 (0,64; "tratar a mera perda patrimonial decorrente da atividade econômica como"), G-73 (0,51; "com referência genérica à ilegalidade"), G-77 (0,49; trecho comum que é letra do art. 12, § 5º): a coincidência é letra da lei ou estrutura de frase curta. Aceitas, no critério do D5 R2.
   - **G-76** reproduz a frase do leitor (B13) com uma palavra trocada: "Afirmar que a multa civil [pode ser → é] duplicada automaticamente em razão da gravidade do ato" (13 das 15 palavras, em ordem; nada disso é letra do art. 12, § 2º). Ajuste 3.
   - Opcional: a pegadinha do C7-23 traz "com o nome ou a imagem do agente", expressão do leitor (B12) que não é letra do Anexo N (é matéria do § 1º do art. 37 da CF, não transcrito); a G-74 já a evitou. Ajuste 7.
6. **Blocos C7-21 a C7-24, P-61 a P-68 e G-71 a G-78: APROVADOS pela letra**, com a exceção da G-76. Números e verbos de comando literais ("até o dobro", "se o juiz considerar", "limitar-se-á à aplicação de multa", "salvo se comprovado", "somente poderão ser executadas", "exceto no caso de simulação ou de evidente intuito de fraude"). Os exemplos dizem que são hipotéticos e não afirmam nada sobre a Câmara real. O agrupamento de três sugestões no C7-21 e na G-71 (pendente (d) da v2) segue o formato da v1 (pegadinha com várias armadilhas do mesmo bloco) e não pede separação.

## 6. Itens "QA PENDENTE (R2)": veredito item a item (11)
| Item | Pos. | Folha | Gab. | O que mudou | Conferência | Veredito |
|---|---|---|---|---|---|---|
| D3-06 | 6 | 5.1 | C | Enunciado | Literal do R1 (3.1, n. 1). Correto: art. 84, IV × VI | APROVADO |
| D3-08 | 8 | 5.1 | E | Enunciado, troca | Literais (n. 2). A avocação recai sobre órgão inferior (art. 15); a delegação admite não subordinado (art. 12). E seguro; [TS] com troca única | APROVADO |
| D3-13 | 13 | 5.2 | E | Enunciado, linha 2 | Literais (n. 3). Sem o titular da competência; "difere de D3-07" continua pertinente | APROVADO |
| D3-25 | 24 | 6.1 | C | Enunciado, ponto, mecanismo; linha 2 por consequência | Literais (n. 4). Linha 2 nova ("parece errado ao negar a menção, mas reproduz o que o art. 43 dispõe") é fiel ao art. 43 e ao C3; não volta ao ponto do D3-30 no enunciado | APROVADO |
| D3-26 | 25 | 6.1 | E | Enunciado; linha 2 por consequência | Literal (n. 5). Linha 2 nova ("risco administrativo → risco integral") correta; não entrega o D3-29 | APROVADO |
| D3-33 | 34 | 6.2 | C | Enunciado, linha 2, "Difere"; movido | Literais (n. 6). Só os destinatários do regresso | APROVADO |
| D3-37 | 38 | 6.2 | C | Linha 2 da justificativa; movido | Enunciado, gabarito, base e marcas iguais à v1. A frase nova "Pacificidade confirmada no R1." é nota interna de processo na justificativa, que vai ao pacote e à edição do estudante (PADRÃO ÚNICO, 7: edição sem notas internas de QA). Ajuste 2 | APROVADO COM AJUSTE |
| D3-66 | 58 | 6.5 | C | Enunciado, "Difere" | Literais (n. 7). Sem a oração "pois…"; distinto do D3-54 | APROVADO |
| D3-71 | 71 | 7 | E | Enunciado, ponto, linhas 1 e 2, mecanismo, troca, base; movido | Literais (n. 8). Art. 9º, caput: "qualquer tipo de vantagem … e notadamente" → "exclusivamente nas hipóteses enumeradas nos incisos". E seguro; E6; [TS] de troca única; não toca dolo (distinto do D3-73) nem dispositivo bloqueado | APROVADO |
| D3-74 | 65 | 7 | C | Enunciado, base; linha 2 por consequência | Literais (n. 9). Art. 11, XI (servidor em cargo de direção como autoridade nomeante; dolo no cenário); § 5º só como registro. Linha 2 nova fiel ao texto | APROVADO |
| D3-81 | 30 | 6.2 | C | Item novo | Seção 4. Ajuste 1 | APROVADO COM AJUSTE |

## 7. Contagens, base doutrinária e sequência (refeitas por script sobre a v2)
- Por folha (itens; C/E; [TS] total / C; BASE DOUTRINÁRIA (teto); formatos DEF/SUJ/SIT/NUM/PAR/APL): 5.1 — 10; 5/5; 5/1; 2 (3); 3/1/2/0/3/1. 5.2 — 9; 4/5; 5/1; 2 (3); 3/1/2/0/2/1. 6.1 — 10; 5/5; 5/1; 3 (4); 3/1/2/0/3/1. 6.2 — 9; 4/5; 5/1; 1 (3); 3/0/3/0/3/0. 6.3 — 7; 2/5; 5/0; 5 (8); 2/0/3/0/1/1. 6.4 — 8; 3/5; 5/1; 2 (4); 3/0/2/0/2/1. 6.5 — 8; 3/5; 5/0; 5 (8); 3/0/2/0/2/1. 7 — 10; 5/5; 5/1; 0 (0); 3/1/2/2/1/1.
- Lote: 71 itens; 31 C/40 E (43,7%; faixa da D1: 29 a 42 C); [TS] 40 (6 C com elemento-isca: D3-02, 18, 22, 36, 54, 76); BASE DOUTRINÁRIA 20 (teto 33; subtetos da 5.1: discricionário 1, disciplinar 1, hierarquia 0); teto de 3 por formato e APL ≤ 2 por folha respeitados; a moldura do Legislativo aparece exatamente nos 7 APL; NUM = 2 (folha 7, números literais); VOLÁTIL 0; REVERIFICAR 0; "QA PENDENTE (R2)" = 11 (2/1/2/3/0/0/1/2 por folha). Tudo igual à tabela 7.1 da v2.
- Base doutrinária: os 20 pontos são os 20 já aprovados como pacíficos no R1 (nenhum novo; o D3-81 tem dispositivo); todos dentro da lista fechada da 6.7 com o adendo do D3-67; nenhum ponto vedado.
- Pontos de julgamento: a lista 7.3 da v2 é igual, posição a posição, aos 71 campos (script); 0 duplicata literal. Duplicata de sentido: nenhuma além do par D3-81 × D3-32 (seção 4, registro).
- Sequência (ficha 6.4; D1, 3.3), na ordem de apresentação:
  - Gabarito: ECCEECEECCECEECCECEECECCEECECCEEECCEECEEECCEECEECCEEECEECCEEECECCECEECE. Maior corrida 3; maior alternância 4; maiores blocos repetidos p2 a p8 = 4, 7, 7, 10, 17, 13, 20 (limites 8, 8, 8, 15, 18, 21, 24).
  - [TS]: TTnnTnTTnnTnTTnTnnTTTnnnTTnTnnTTTnTTnnTTTnnTTnTTTnnTTnTTnnTTTnTnnnTTTnT. Corrida 3; alternância 4; p2 a p8 = 4, 7, 7, 11, 15, 13, 19.
  - Por folha: as 8 aprovadas (gabarito e [TS]), com os valores da tabela 7.2 da v2.
  - **APROVADO**, idêntico à D1 (3.3) e à v2 (7.2). Os ajustes residuais não mudam gabarito, [TS] nem posição.

## 8. Pendências da produção — parecer técnico para a GCB (a decisão é da GCB)
a. **Arquivo neutro não regerado (pendente (a) das seções 0 e 8 da v2; R1, ponto 32).** A leitura externa já foi feita sobre o arquivo neutro da v1, e o que ela produziu entrou na 0.1. Regerar agora só serviria a uma segunda leitura externa, que não está prevista. A QA não vê necessidade técnica de regerar; recomenda registrar na reconciliação a falta do script de geração e da hora em TAREFAS.md, como a D1 (seção 6) já previu.
b. **Linha 2 sem "(P1-DA, itens 5 a 7)" (ponto 25; pendente (b)).** A D1 (seção 5, item 1) fixa a linha 2 com o qualificador. A produção invoca uma "ordem da T-76" que não está em documento lido por esta QA (a linha da T-76 em TAREFAS.md não fixa a linha 2). É só forma; o qualificador está no parágrafo de abertura. Se a GCB mantiver a D1, aplica-se o ajuste 6.
c. **Linhas 2 alteradas por consequência (D3-25, D3-26, D3-37, D3-74; pendente (c)).** Declaradas no campo "Alteração na v2" e conferidas (seção 6): as três primeiras estão corretas e eram necessárias, porque a linha 2 antiga contradizia o enunciado novo; a do D3-37 pede o ajuste 2.
d. **Preâmbulo único (pendente (d) da seção 0; (c) da seção 8).** O parágrafo "Convenções próprias do item 7" preserva o conteúdo da abertura da Parte B da v1 (BASE DOUTRINÁRIA 0; remissões a ADI só no curso; números literais). É equivalente em conteúdo ao que a D1 pediu; a QA recomenda aceitar sem errata.
e. **Agrupamento de sugestões no C7-21 e na G-71 (pendente (d) da seção 8) e base da G-74 (pendente (e)).** Aceitos (seção 5, n. 6 e n. 2).
f. **Ordem: D3-81 contíguo ao D3-32 (registro da QA).** Uma permuta entre o D3-81 (posição 30) e o D3-33 (posição 34), ambos C e sem [TS], deixa as sequências de gabarito e de [TS] idênticas, logo o teste da D1 continua APROVADO sem novo cálculo; o D3-81 ficaria a 3 posições do D3-32. É opcional e só a GCB pode decidir, porque a ordem é dela. Sem a permuta, a nota à GBQ (D3-81 nunca com D3-32) protege o simulado, mas não o teste de lote.
g. **"Faltam para 20" e reforço (pendente (f)).** Coerente com a D1; sem ação neste R2.

## 9. Ajustes residuais (texto exato)
Cada trecho atual foi copiado do D3_v2.md e ocorre uma única vez no arquivo (conferido por grep). Nenhum muda gabarito, ponto de julgamento, [TS], posição ou contagem.

1. **D3-81, enunciado (seção 5.1).** Motivo: limite da D1, seção 1.3 (seção 4 deste parecer).
   - Trecho atual: "o direito regressivo ressalvado pelo art. 43 do Código Civil contra o causador do dano depende"
   - Texto novo: "o direito regressivo contra o agente, previsto no art. 43 do Código Civil, depende"
   - Enunciado resultante: "Considere que pessoa jurídica de direito público interno tenha de indenizar terceiro por dano que um agente seu, nessa qualidade, lhe causou. Nessa situação, o direito regressivo contra o agente, previsto no art. 43 do Código Civil, depende de ter havido, por parte deste, culpa ou dolo." Gabarito C, ponto, base, mecanismo e justificativas mantidos.
2. **D3-37, justificativa (linha 2).** Motivo: nota interna de processo em texto que vai ao pacote.
   - Trecho atual: "a tentação é equiparar responsabilidade a ilicitude. Pacificidade confirmada no R1."
   - Texto novo: "a tentação é equiparar responsabilidade a ilicitude."
3. **G-76 (seção 4).** Motivo: redação do leitor (B13) reproduzida (ficha 9; precedente do D5, G-68).
   - Trecho atual: "Afirmar que a multa civil é duplicada automaticamente em razão da gravidade do ato, quando o § 2º permite aumentá-la até o dobro se o juiz"
   - Texto novo: "Vincular à gravidade do fato o aumento da multa até o dobro, que o § 2º só admite se o juiz"
   - O dispositivo não muda (art. 12, § 2º).
4. **Seção 8, notas à GBQ.** Motivo: a consolidação omitiu notas do R1, ponto 33, que continuam válidas na v2.
   - Trecho atual: "Os D3-54 e D3-66, o D3-81 e a predominância de E são as notas novas da v2; as notas de itens reprovados saíram."
   - Texto novo: "Mantidas do R1 (ponto 33), que a consolidação omitira: D3-15, D3-17 e D3-20 com D1-32; D3-21 com D3-35; D3-28 com D3-30; D3-41 com D3-49; D3-45 com D3-55; D3-51 com D3-58; D3-54 com D3-56; D3-62 com D3-63; D3-72 com BQ-0149 (dolo); D3-58 tem baixa discriminação (preferir em teste de lote a simulado). Os D3-54 e D3-66, o D3-81 e a predominância de E são as notas novas da v2; as notas de itens reprovados saíram."
5. **Seção 7.5, quarta conferência.** Motivo: a afirmação omite uma ocorrência (D3-39 no bloco à GCB).
   - Trecho atual: "aparecem só na seção 0, no título da seção 5 e no campo "Alteração na v2" do D3-81;"
   - Texto novo: "aparecem só na seção 0, no título da seção 5, no campo "Alteração na v2" do D3-81 e no bloco à GCB (seção 8, escolha (5), D3-39, como limite da D1);"
6. **(Condicionado à GCB manter a D1, seção 5, item 1) Linha 2.**
   - Trecho atual: "LOTE D3 — Poderes administrativos, responsabilidade civil do Estado e improbidade — v2 — 2026-10-20"
   - Texto novo: "LOTE D3 — Poderes administrativos, responsabilidade civil do Estado e improbidade (P1-DA, itens 5 a 7) — v2 — 2026-10-20"
   - O ponto 25 da seção 0 e o pendente (b) da seção 8 ficam como registro histórico.
7. **(Opcional, forma) C7-23, pegadinha provável.** Motivo: expressão do leitor (B12) que não é letra do Anexo N.
   - Trecho atual: "equiparar a qualquer publicidade com o nome ou a imagem do agente o ato do inciso XII"
   - Texto novo: "equiparar ao ato do inciso XII toda publicidade com recursos do erário que mencione o agente público"

Se aplicados por errata, a QA confere só os trechos acima (diff), sem nova rodada sobre os itens.

## 10. Tabela final dos 71 itens (ordem de apresentação)
| Pos. | Item | Folha | Gab. | [TS] | Marca | Veredito R2 | Observação |
|---|---|---|---|---|---|---|---|
| 1 | D3-01 | 5.1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 2 | D3-02 | 5.1 | C | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 3 | D3-03 | 5.1 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 4 | D3-04 | 5.1 | E | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 5 | D3-05 | 5.1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 6 | D3-06 | 5.1 | C | não | QA PENDENTE (R2) | APROVADO | ajuste 1 do R1 aplicado literalmente (enunciado) |
| 7 | D3-07 | 5.1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 8 | D3-08 | 5.1 | E | sim | QA PENDENTE (R2) | APROVADO | ajuste 2 aplicado literalmente (enunciado e troca) |
| 9 | D3-09 | 5.1 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 10 | D3-10 | 5.1 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 11 | D3-11 | 5.2 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 12 | D3-12 | 5.2 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 13 | D3-13 | 5.2 | E | sim | QA PENDENTE (R2) | APROVADO | ajuste 3 aplicado literalmente (enunciado e linha 2); difere de D3-07 pertinente |
| 14 | D3-14 | 5.2 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 15 | D3-15 | 5.2 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 16 | D3-18 | 5.2 | C | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); só mudou de posição; veredito do R1 mantido |
| 17 | D3-17 | 5.2 | E | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 18 | D3-16 | 5.2 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); só mudou de posição; veredito do R1 mantido |
| 19 | D3-20 | 5.2 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 20 | D3-21 | 6.1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 21 | D3-22 | 6.1 | C | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 22 | D3-23 | 6.1 | E | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 23 | D3-24 | 6.1 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 24 | D3-25 | 6.1 | C | não | QA PENDENTE (R2) | APROVADO | ajuste 4 aplicado literalmente (enunciado, ponto, C3); linha 2 alinhada e correta |
| 25 | D3-26 | 6.1 | E | sim | QA PENDENTE (R2) | APROVADO | ajuste 5 aplicado literalmente (enunciado); linha 2 alinhada e correta |
| 26 | D3-27 | 6.1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 27 | D3-28 | 6.1 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 28 | D3-29 | 6.1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 29 | D3-30 | 6.1 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 30 | D3-81 | 6.2 | C | não | QA PENDENTE (R2) | APROVADO COM AJUSTE | novo (vaga do D3-31); C, art. 43 do CC pela letra; enunciado usa "ressalvado" e "causador do dano" (ajuste residual 1) |
| 31 | D3-32 | 6.2 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 32 | D3-35 | 6.2 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); só mudou de posição; veredito do R1 mantido |
| 33 | D3-34 | 6.2 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 34 | D3-33 | 6.2 | C | não | QA PENDENTE (R2) | APROVADO | ajuste 6 aplicado literalmente (enunciado, linha 2, difere); movido |
| 35 | D3-36 | 6.2 | C | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 36 | D3-40 | 6.2 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); só mudou de posição; veredito do R1 mantido |
| 37 | D3-38 | 6.2 | E | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 38 | D3-37 | 6.2 | C | não | QA PENDENTE (R2) | APROVADO COM AJUSTE | só a linha 2 mudou; nota de processo na justificativa (ajuste residual 2); movido |
| 39 | D3-41 | 6.3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 40 | D3-43 | 6.3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 41 | D3-46 | 6.3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); só mudou de posição; veredito do R1 mantido |
| 42 | D3-45 | 6.3 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 43 | D3-44 | 6.3 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); só mudou de posição; veredito do R1 mantido |
| 44 | D3-47 | 6.3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 45 | D3-49 | 6.3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 46 | D3-51 | 6.4 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 47 | D3-52 | 6.4 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 48 | D3-55 | 6.4 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); só mudou de posição; veredito do R1 mantido |
| 49 | D3-54 | 6.4 | C | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 50 | D3-58 | 6.4 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); só mudou de posição; veredito do R1 mantido |
| 51 | D3-53 | 6.4 | E | não | QA PENDENTE | APROVADO | idêntico à v1 (script); só mudou de posição; veredito do R1 mantido |
| 52 | D3-56 | 6.4 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); só mudou de posição; veredito do R1 mantido |
| 53 | D3-59 | 6.4 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 54 | D3-63 | 6.5 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); só mudou de posição; veredito do R1 mantido |
| 55 | D3-62 | 6.5 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 56 | D3-61 | 6.5 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); só mudou de posição; veredito do R1 mantido |
| 57 | D3-70 | 6.5 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); só mudou de posição; veredito do R1 mantido |
| 58 | D3-66 | 6.5 | C | não | QA PENDENTE (R2) | APROVADO | ajuste 7 aplicado literalmente (enunciado e difere) |
| 59 | D3-67 | 6.5 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 60 | D3-68 | 6.5 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 61 | D3-64 | 6.5 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); só mudou de posição; veredito do R1 mantido |
| 62 | D3-80 | 7 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); só mudou de posição; veredito do R1 mantido |
| 63 | D3-72 | 7 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 64 | D3-73 | 7 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 65 | D3-74 | 7 | C | não | QA PENDENTE (R2) | APROVADO | ajuste 9 aplicado literalmente (enunciado e base); linha 2 alinhada e correta |
| 66 | D3-75 | 7 | E | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 67 | D3-76 | 7 | C | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 68 | D3-77 | 7 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 69 | D3-78 | 7 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 70 | D3-79 | 7 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| 71 | D3-71 | 7 | E | sim | QA PENDENTE (R2) | APROVADO | ajuste 8 aplicado literalmente (enunciado, ponto, linhas 1 e 2, E6, troca, base); movido |
Resumo da tabela: 71 itens; 69 APROVADOS (60 idênticos à v1, 15 deles só com mudança de posição; 9 com o ajuste do R1 aplicado literalmente); 2 APROVADOS COM AJUSTE (D3-37, linha 2; D3-81, enunciado); 0 REPROVADOS. Reprovação: 0/71 = 0%.

## 11. Veredito final
Lote D3 v2: **APROVADO COM AJUSTES RESIDUAIS no R2.** 71/71 itens aprovados (2 com ajuste de texto), reprovação 0%. Não há gate.

Pela QA, o aceite pode seguir à reconciliação da gcb-gerencia, com as seguintes condições:
- aplicar ou registrar por errata os ajustes 1 a 5 da seção 9 (o 6 depende da decisão da GCB sobre a linha 2; o 7 é opcional);
- decidir os pendentes da seção 8 (a: arquivo neutro e script; b: linha 2; d: preâmbulo único; f: permuta opcional D3-81 × D3-33).

Todo item segue "QA PENDENTE" no registro até o gatilho A aceito (D-QA-PENDENTE). Nada vai à plataforma nem à candidata.

GATE: não acionado (reprovação 0/71 = 0%, limite 30%).

FIM DO PARECER R2 — LOTE D3
