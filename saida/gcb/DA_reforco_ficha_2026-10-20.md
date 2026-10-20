# DA_reforco_ficha_2026-10-20.md — T-116 — 2026-10-20 — gerado por gcb-gerencia

# FICHA DO REFORÇO DE DIREITO ADMINISTRATIVO (P1-DA) — regras, plano de 12 levas e ficha da leva 1 — ciclo s15c3
Tarefa T-116 (complementa a T-100 sem alterá-la). Decisões: D-REFORCO-DA (Fundador, 20/10/2026; DECISOES.md, linha 173), D-REFORCO-2 (linha 95), D-MOLDURA-CE (linha 171), D-COBERTURA-AUTO-2 (linha 97), D-T97-META-FUNDADOR-RESP (linha 127), D-COMPLEMENTOS. Modelo de forma: saida/gcb/D6_ficha_teste_cego.md e saida/gcb/D4_ficha_lote.md. Esta ficha não traz curso nem item; a seleção do que vira item é da GCB e a redação é da gcb-cpp. Sem commit nem push.

## 0. Entradas, conferência e decisões da GCB nesta ficha

### 0.1 Entradas (SHA-256 em disco, 20/10/2026)
| objeto | SHA-256 (início…fim) | uso |
|---|---|---|
| saida/pacote/pacote.json v1.13 canônico | 82c4117c…7fddf240 | itemEdital, gabarito e enunciado dos 410 itens de DA |
| saida/pacote/cobertura_v1_13.md | 13491263…5bcbb8c1 | 34 folhas abaixo de 20; faltam 356; ordem da mais rala à mais cheia |
| saida/banco/moldura_ce_2026-10-20.md | 56dea18b…4a3c3f7d | meta 21; cotas por folha (seção 4); R1 a R6 |
| saida/banco/moldura_ce_itens_2026-10-20.csv | ed4b364d…4981daac | marcação oficial de moldura, item a item |
| saida/gcb/D4_anexo_N_adendo_2026-10-20.md | c32f58eb…03d16fb5 | lastro das folhas 8.1 e 8.4 (R32 a R85) |
| saida/gcb/D3_anexo_N_adendo_2026-10-20.md | c8ad5bd2…b9f74a50 | lastro das folhas 6.3, 6.4 e 6.5 (55 dispositivos) |
| Anexos N D1 a D6 | 73546bcf…, b0a54fff…, 2ef58f9b…, 0d98c249…, 497af8e6…, 57e8c64d… | lastro das demais folhas |
| D1_v2.md; D2_v2_1.md; D3_v2_1.md; D4_v2_1.md; D5_v2_1.md; D6_v2_1.md | 63bd27c3…, 59cffaa6…, 0f7a8b09…, c1a7a935…, 44ddcc98…, a9831058… | pontos de julgamento já usados (anti-gêmeo) |
| T73 a T77 e T101 (reconciliações) | — | exigências (a) a (d) da T-116 |

Conferência própria (python3 -I, somente leitura, scratchpad da sessão): os 410 itens de DA do pacote cruzados com o CSV de moldura e com os campos "Formato" e "Ponto de julgamento" dos canônicos; reproduzidos: 34 folhas abaixo de 20, soma "faltam" = 356; moldura de DA 44 C / 9 E; nas 34 folhas do reforço, 41/9; cotas da seção 4 do relatório da T-122 = 33.

### 0.2 Decisões da GCB (D1) fixadas por esta ficha
1. **Taxonomia de formatos do DA** (a mesma da ficha do D2, seção "Convenções", que já serviu ao D3 e ao D4): **DEF** = afirmação sobre o conteúdo, o conceito ou o comando da norma ou do trecho; **SUJ** = troca ou atribuição de sujeito ou de competência; **SIT** = situação hipotética **sem** moldura do Legislativo (inclui "um analista", "um gestor", "determinado órgão"); **NUM** = número, prazo, percentual ou contagem exata de rol, literal da fonte; **PAR** = par confundível (dois conceitos vizinhos, um deles trocado ou contrastado); **APL** = todo item com moldura do Legislativo pelo critério da seção 1 do relatório da T-122 (moldura S ⇔ formato APL; o APL prevalece sobre os demais). Correspondência com a D-REFORCO-2: definição = DEF; troca de sujeito = SUJ; situação hipotética = SIT; número ou prazo = NUM; par confundível = PAR; aplicação parlamentar = APL. O formato segue a construção do ponto, não o gabarito (D2 ratificada na D-T91-R3-ACEITE).
2. **Teto de formato** medido na folha inteira (canônicos + reforço aceito + leva): no máximo ⌊0,3 × total final da folha⌋ itens de um formato (6 numa folha de 20). Legado canônico conta como declarado; nos canônicos do D1 (sem campo "Formato"), a GCB classifica os da folha na ficha da leva em que ela entrar (precedente T92_D1, 2.4: legado não imputado à leva).
3. **Base**: só linha vigente transcrita num Anexo N de DA (D1 a D6) ou num adendo; dispositivo transcrito no Anexo N de outro lote vale, citado com o arquivo e a seção (ex.: Lei 14.133 do Anexo N do D5 para a folha 2.2). BASE DOUTRINÁRIA proibida no reforço (regra 2 da D-REFORCO-2: "artigo, documento oficial…"; sem base, não entra). Data verdadeira da consulta registrada no Anexo ou adendo (D-FONTE-DATA-ANTERIOR).
4. **Atribuição do referencial (D4)**: vale a seção 3.2 da ficha do D4 — item não nomeia autor; órgão (TCU, Casa Civil, CGU) pode ser nomeado. Por isso ficam FORA do reforço os pontos cuja verdade depende da atribuição a autor citado: A8.1-17 (raízes "a partir de Osborne"), A8.1-23 (termo "cunhado por Osborne"), A8.1-24 ("citando Jing") e A8.1-25 ("citando Rhodes"). Os pontos A8.4-04 a A8.4-06 (Porter; Kaplan e Norton) entram atribuídos ao TCU ("segundo o Referencial Básico de Governança Organizacional do TCU"), como o adendo exige (alerta B2).
5. **Aderência (exigência (d))**: ponto de pertinência "indireta" no adendo (outro regime: servidor, contratado, fornecedor, operador nuclear, poluidor) gera item de **aderência PARCIAL** (campo "Aderência: parcial"); conta para a meta de 20, só vai a simulado diagnóstico (D-ADERENCIA) e a folha mantém o piso de 10 diretos (D-T97-META-FUNDADOR-RESP). Nas 8 folhas com menos de 10 diretos (8.1 = 6; 6.3 = 7; 8.4 = 7; 2.2 = 8; 6.4 = 8; 6.5 = 8; 5.2 = 9; 6.2 = 9), os primeiros itens aceitos completam o piso com itens diretos.
6. **Correção de registro (exigência (d))**: o "faltam para 20" do D3 é **89** pela cobertura v1.13 (5.1 10; 5.2 11; 6.1 10; 6.2 11; 6.3 13; 6.4 12; 6.5 12; 7 10), e não 86: a D1 do D3 (D3_D1_GCB_v2, seção 1.4) contou "7 = 7", mas a folha 7 tem 10 itens no pacote v1.13. O plano usa 89 (D3-R01 a D3-R89).
7. **Correção de registro do adendo do D3**: a síntese (seções 3.1 a 3.4 e 5.4) diverge da tabela por ponto; vale a tabela. 6.3: 7 diretos / 8 indiretos (síntese: 8/7); 6.4: 8/10 (síntese: 9/9); 6.5: 12/8 (síntese: 13/7). Efeito: na 6.3, "só com os diretos" a folha chega a 14, não a 15.
8. **Gêmeos entre lotes evitados**: A6.3-10 (Lei 14.133, art. 121, caput e § 1º) é gêmeo do D5-37 (folha 10.4) e fica fora; A6.5-13 (art. 120) é gêmeo do D5-38 (10.4) e fica fora da 6.5. Nas folhas 10.x (levas 10 e 11), os arts. 120 e 121, § 2º, ficam reservados à 6.3 (nota à GBQ: não pôr no mesmo simulado D3-R de 6.3 sobre o art. 121, § 2º, e D5-37).
9. **Exigência (c) — par espelho D4-29/D4-30 (8.4), revisto**: os dois canônicos ficam como estão (pontos distintos, 8.4-1 e 8.4-2; nenhum erro; a T77_reconciliacao, linha 130, já os separa em simulado). O reforço dilui o par em vez de alterá-lo: **nenhum item novo da 8.4 usa o Decreto 9.203, art. 2º, II (nem a parte final, que fica na 9.3), nem o art. 4º, IV (D4-27)**; os 13 itens novos vêm do referencial do adendo (R59 a R83). O par passa de 2/7 a 2/20 da folha. Errata dos canônicos não é aberta (D-COMPLEMENTOS; D-MOLDURA-CE (b) não acionada).
10. **Núcleo**: pela D-REFORCO-2 ("nucleo" = 10 primeiros por ordem de canonização), nas folhas com menos de 10 canônicos os primeiros D<n>-R aceitos da folha (em ordem de id) recebem "nucleo": true até 10 (8.1: 4; 6.3: 3; 8.4: 3; 2.2, 6.4, 6.5: 2; 5.2, 6.2: 1). Nota à GBQ para a T-123.

## 1. Regras de todo item do reforço (valem para as 12 levas)
1. **Uma folha e um ponto de julgamento único** por item (código do Anexo N ou do adendo + dispositivo ou R-id + a proposição julgada, em uma linha). Dois itens da mesma folha não usam o mesmo ponto — contam os canônicos da folha (campo "Ponto de julgamento" dos D<n>_v2/v2_1 e a lista "Pontos já usados" dos adendos) e os D<n>-R já aceitos. A gcb-gerencia rejeita duplicata na reconciliação.
2. **Sem gêmeo de item canônico da mesma folha**: proibido o mesmo dispositivo com o mesmo elemento (mesmo ponto com o sinal trocado, ou a mesma troca). Ângulo novo sobre dispositivo já usado é admitido e vai no campo "Difere de: <id> porque …". Gêmeo com canônico de outra folha ou lote: evitado; se inevitável, nota "não pôr no mesmo simulado" à GBQ.
3. **Base por item**: dispositivo (norma, artigo, inciso, parágrafo, alínea, "Anexo N do D<n>, seção x" ou "adendo de 20/10/2026, seção 4.x") ou referencial (R-id, publicação, órgão, ano, página, URL idêntica à do Anexo/adendo, "consulta dd/mm/aaaa" verdadeira e o trecho decisivo literal, entre aspas, até 25 palavras). Base vaga, doutrinária ou fora do Anexo/adendo: o item não entra. Nenhum "[SEM FONTE]" em item; os SEM FONTE dos Anexos e o alerta A11 do adendo do D3 nunca viram ponto.
4. **Formato** declarado (seção 0.2, item 1); **teto de 30% por formato na folha** (seção 0.2, item 2).
5. **VOLÁTIL ≤ 20% por folha** (com os canônicos: 3.1, 3.3, 11 e 12 já têm 1, 1, 1 e 2). Esperado no reforço: 0 (norma e referencial, sem produto). REVERIFICAR: todo item apoiado em redação de 2025 ou 2026 (ex.: CF, art. 37, XVI, b, EC 138/2025) leva a marca e vai à fila de janeiro (T-11/T-120).
6. **Gabarito de cada leva entre 40% e 60% de C** (30 itens: 12 a 18 C; 28 itens: 12 a 16 C), conferido sobre os itens aceitos na reconciliação. Alvo por folha: o total final da folha perto de 10 C / 10 E (faixa 8 a 12 C), sem forçar com item fraco. Sequência: na ordem final, por folha e na leva, nenhuma corrida de 4 ou mais gabaritos iguais, nenhuma alternância estrita C/E por mais de 4 itens e nenhum bloco de período p (2 a 8) repetido por max(8, 2p) itens (teste do D4, seção 6.4); o mesmo teste vale para a sequência de [TS].
7. **[TS]** quando houver troca sutil real e única de um elemento do dispositivo ou do trecho (sujeito, número, prazo, verbo de comando, competência, rol, regra × exceção, conceito vizinho). Campo "Troca": "texto da fonte → texto do item". [TS] com gabarito C só com elemento-isca literal ("elemento-isca: … (literal em …)"), no máximo 1 por folha. Sem troca real, sem marca.
8. **Troca legítima nos E**: o item E é errado pela letra da base (contradição expressa ou troca de um elemento); "E por ausência" é proibido, salvo rol fechado do texto citado como tal. A moldura nunca decide o gabarito (R1 da T-122: nunca "errado porque é o Legislativo").
9. **Uma afirmação por item**; sem "exceto"; sem alternativas; sem duas exigências somadas quando uma já decide o gabarito. Fidelidade literal de número, sujeito, verbo ("deverá", "poderá", "somente", "exclusivamente") e termos-chave.
10. **Moldura do Legislativo** (D-MOLDURA-CE; exigência (a)): todo item com moldura declara "Moldura: S" e o tipo; tipo da cota = tipo que causa o excesso de C na folha (R2 da T-122): "audiência pública de comissão da Câmara dos Deputados, um expositor afirme…" nas folhas 8.x e 9.x; "órgão/servidor do Poder Legislativo da União" nas do D2, D3 e D5; "comissão/sessão da Câmara dos Deputados" na 5.2. "Poder Legislativo" isolado não conta. Item com moldura é preferencialmente E (T-74, T-75, T-76, T-77); C com moldura só em par 1:1 com um E com moldura além da cota, na mesma folha (R3); no máximo 6 itens com moldura por folha (com os canônicos). Nenhuma afirmação sobre norma interna, sistema ou prática real da Câmara sem fonte oficial datada; nenhum item julga se o Decreto 9.203 alcança a Câmara (ficha do D4, alerta 5).
11. **Conjuntos-marcador do D4** (exigência (a), T77_reconciliacao, linha 135; R2 do D4, seção 7): nas folhas 8.x e 9.x, item novo com moldura de expositor ou analista, com "pós-NPM" ou com abertura "Considere que" é preferencialmente E (troca de elemento literal), até cada conjunto ficar entre 40% e 60% de C. Partida: K1 moldura do Legislativo do D4 12 C / 0 E; K2 fecho de "acerto" ("a afirmação do expositor é correta"; "ele estará correto ao") 5/0; K3 "pós-NPM" 4/0; K4 abertura "Considere que" 21/8. Fecho "neutro" (sem K2): "Nessa situação, é correto afirmar que …". Nenhum item iguala pós-NPM e NPG; "NGP" nunca aparece em texto próprio (ficha do D4, seção 3.3; adendo, alerta B1).
12. **Ids**: D<n>-R<nn>, por lote, contínuos, na ordem das levas; id reprovado não é reutilizado; item substituto recebe o próximo id livre do lote. Primeiro id de cada lote: **D4-R01 e D3-R01 (leva 1); D1-R01 (leva 2); D2-R01 (leva 4); D5-R01 (leva 10)**. Faixas previstas na seção 2.1 (deslocam-se se houver substituição).
13. **Rótulo e marcas**: AUTORAL; "QA PENDENTE" até o gatilho A aceito (D-QA-PENDENTE); nenhum rótulo "estilo" da banca, orientação de marcação, autor nomeado, dispositivo revogado como vigente, ponto controverso ou classificação disputada.
14. **Formato de entrega igual ao dos canônicos** (D4_v2_1.md, seção 5.2), com os campos obrigatórios desta tarefa. Arquivo da leva: saida/gcb/DA_reforco_L<nn>_v1.md (v2: _v2.md), uma leva por arquivo, com:
   - linha 1: `# DA_reforco_L<nn>_v1.md — T-116 — <data ISO> — gerado por gcb-cpp`;
   - `## 1. Versão do estudante` (por folha, na ordem da leva; só enunciado);
   - `## 2. Gabarito comentado`, um bloco por item:
     ```
     **D4-R01** (folha 8.1) — AUTORAL — QA PENDENTE [TS]
     - itemEdital: P1-DA-8.1
     - Ponto de julgamento: A8.1-07 — R37 — <proposição julgada, uma linha>
     - Formato: DEF | SUJ | SIT | NUM | PAR | APL
     - Moldura: N  |  S — <tipo> — fecho: acerto | neutro
     - Aderência: direta | parcial
     - Gabarito: C | E
     - Justificativa (linha 1): <o que a base diz>
     - Justificativa (linha 2): <onde está a troca ou a tentação>
     - Tipo de base: DISPOSITIVO | REFERENCIAL OUTRA_OFICIAL
     - Base: <dispositivo e seção do Anexo/adendo | R-id, publicação, página, URL, consulta dd/mm/aaaa; trecho: "…">
     - Mecanismo: E1–E6 | C1–C6 (regras/estilo_banca.md)
     - Troca: <texto da fonte → texto do item>   (só com [TS])
     - Difere de: <id canônico mais próximo da folha> porque …
     - Marcas: TS=sim|não; REVERIFICAR=sim|não; VOLÁTIL=sim|não; QA PENDENTE=sim
     ```
   - `## 3. Proveniência` (toda fonte citada, URL e data, idênticas às do Anexo/adendo);
   - `## 4. Contagens` (por script, python3 -I, sobre o arquivo gravado): por folha (canônicos + leva) — itens, C/E, formatos, moldura C/E, diretos/parciais, VOLÁTIL, [TS]; na leva — C/E e %C, [TS], teste de sequência; moldura acumulada de DA (partida 44/9) e dos conjuntos por lote e K1 a K4; lista dos pontos da leva sem duplicata entre si e com os canônicos;
   - `## 5. Bloco à GCB` (dúvidas, pontos de reserva usados, notas "não pôr no mesmo simulado");
   - última linha: `FIM DA LEVA <nn> — REFORÇO DA`.
15. **Rito por leva** (D-REFORCO-DA): ficha da leva (gcb-gerencia) → v1 (gcb-cpp, sonnet) → R1 (gcb-cqfp, opus) → v2 → R2 (no máximo 2 rodadas) → auditoria de estilo 10% (gbq-estilo, saida/banco/estilo_onda_DA_L<nn>.md) → reconciliação (saida/gcb/T116_L<nn>_reconciliacao_<data>.md, com moldura acumulada, R5 da T-122) → gatilho A da GCB. Sem leitura externa (não há curso novo). Nenhuma leva nova com QA da anterior aberto. Pareceres: saida/gcb/QA_T116_L<nn>_R<k>_<data>_gcb-cqfp.md. Consolidação no pacote v1.14 (T-123); publicação só com o sim do Fundador.

## 2. PLANO DE LEVAS

### 2.1 Composição (ordem da cobertura v1.13: das folhas mais ralas às mais cheias; empate pela ordem do edital)
Doze levas somam 356 itens. Com levas de até 30 e folhas inteiras, seriam 13 (a de 14 itens não fecha par de 30 com nenhuma outra sem sobra maior que a folga total de 4); a partição ótima, calculada por script, divide **três folhas entre duas levas consecutivas (8.4, 6.4 e 6.2)** e deixa as levas 4 a 12 com folhas inteiras. Folha dividida: os limites da folha (teto de formato, VOLÁTIL, ponto único, cota de moldura) são conferidos sobre a folha acumulada; os pontos da segunda parte saem da reserva que a primeira não usar.

| leva | itens | folhas (itens novos; total final) | lote e faixa de ids prevista | C/E alvo (faixa) | E com moldura (C com moldura) por folha | lastro (pontos disponíveis) |
|---|---|---|---|---|---|---|
| 1 | 30 | 8.1 (14; 20); 6.3 (13; 20); 8.4 (3 de 13) | D4-R01–R14 (8.1); D3-R01–R13 (6.3); D4-R15–R17 (8.4) | 15/15 (12–18) | 8.1 3 (1); 6.3 3 (1); 8.4 3 (0) | adendo D4 §3.1 (30 pontos; 4 fora pela seção 0.2, item 4); adendo D3 §3.1 (15; A6.3-10 fora); adendo D4 §3.2 (27 + 1) — CONFIRMADO |
| 2 | 30 | 8.4 (10; 20); 2.2 (12; 20); 6.4 (8 de 12) | D4-R18–R27; D1-R01–R12; D3-R14–R21 | 17/13 (12–18) | 8.4 0 (1); 2.2 0; 6.4 3 (1) | 8.4: adendo D4 §3.2 sem art. 2º, II, e art. 4º, IV (seção 0.2, item 9) e sem A8.4-27 (mesmo trecho R83 do A8.1-30 da leva 1); 6.4: adendo D3 §3.2 (18: 8 diretos, 10 indiretos); **2.2: A CONFIRMAR** — Anexo N do D1 §5 (Lei 9.784, arts. 42 e 50) e §6.6 (LINDB, art. 28), mais a Lei 14.133 (arts. 10, 53, 72) do Anexo N do D5; estimativa bruta ≤ 15 pontos para 12 itens além dos 8 usados: **adendo ao Anexo N do D1 (qa-normativo-da) antes da ficha da leva 2** |
| 3 | 30 | 6.4 (4; 20); 6.5 (12; 20); 5.2 (11; 20); 6.2 (3 de 11) | D3-R22–R25; D3-R26–R37; D3-R38–R48; D3-R49–R51 | 17/13 (12–18) | 6.5 3 (1); 5.2 1 (0) | 6.5: adendo D3 §3.3 (20; A6.5-13 fora); **5.2 e 6.2: A CONFIRMAR** — Anexo N do D3 §3 e §4.2, 4.3, 4.5, 4.6, 4.8 (CF, art. 37, § 6º; CC, art. 43; CF, art. 49, V; CTN, art. 78; Lei 4.717, art. 2º) e, para a 6.2, o adendo D3 §4 (CC, arts. 186, 927, 944; CF, art. 5º, LXXV); lastro curto para 11 e 11: **adendo do D3 (5.2, 6.1, 6.2) antes da ficha da leva 3** |
| 4 | 28 | 6.2 (8; 20); 3.1 (10; 20); 3.2 (10; 20) | D3-R52–R59; D2-R01–R10; D2-R11–R20 | 14/14 (12–16) | 3.1 3 (0); 3.2 0 | 3.1: Anexo N do D2 §4.1 (CF, arts. 37 a 41; 94 dispositivos de núcleo); 3.2: §3 e §4.1/4.3 (CF, art. 37, I, II, V, IX; Lei 8.112, arts. 2º a 10 e compl.) — CONFIRMADO |
| 5 | 30 | 3.3 (10); 3.4 (10); 4.1 (10) | D2-R21–R30; D2-R31–R40; D2-R41–R50 | 16/14 (12–18) | 3.4 3 (1); 4.1 3 (0) | 3.3: D2 §4.5 a 4.8 (Decreto 10.835; Leis 9.007 e 6.999; Decreto 12.374, art. 21; Lei 8.112, art. 18) — CONFIRMADO; 3.4: D2 §4.3 (Lei 8.112 integral) — CONFIRMADO, com a exigência (b); **4.1: A CONFIRMAR** (Lei 9.784, art. 2º; Lei 8.112, arts. 125, 126, 128, 143; CF, art. 37, caput, e 41, § 1º) |
| 6 | 30 | 4.2 (10); 4.3 (10); 4.4 (10) | D2-R51–R60; D2-R61–R70; D2-R71–R80 | 14/16 (12–18) | 4.2 2; 4.3 1; 4.4 1 | D2 §4.3 (Lei 8.112, arts. 116, 117, 121 a 142; arts. 133, 140, 143 a 182) e §4.4 (Lei 9.784 integral) — CONFIRMADO; **art. 135 = primeiro ponto da 4.2 (D2-R51)** |
| 7 | 30 | 5.1 (10); 6.1 (10); 7 (10) | D3-R60–R69; D3-R70–R79; D3-R80–R89 | 15/15 (12–18) | 6.1 1; 7 1 | 7: D3 §4.9 (Lei 8.429 integral) — CONFIRMADO; **5.1 e 6.1: A CONFIRMAR** (5.1: Lei 9.784, arts. 11 a 15 e 17; CF, art. 84; CTN, art. 78 — discricionário e disciplinar sem dispositivo no recorte; 6.1: CF, art. 37, § 6º; CC, art. 43; adendo D3: CF, art. 5º, LXXV, Decreto 20.910, Lei 8.987, art. 25) |
| 8 | 30 | 8.2 (10); 8.3 (10); 9.1 (10) | D4-R28–R37; D4-R38–R47; D4-R48–R57 | 14/16 (12–18) | 8.2 1; 8.3 2; 9.1 1 | **A CONFIRMAR**: Anexo N do D4 §4.2 a 4.7 e §5 (Leis 11.079, 13.019, 9.637, 9.790, LAI art. 8º, Lei 13.460; R1 a R31) e, na 8.3, R84 (adendo D4 §3.4) |
| 9 | 30 | 9.2 (10); 9.3 (10); 9.4 (10) | D4-R58–R67; D4-R68–R77; D4-R78–R87 | 15/15 (12–18) | 9.2 1; 9.3 2; 9.4 2 | 9.4: Decreto 9.203 integral (D4 §4.1; revogados fora, alertas 1 a 3) — CONFIRMADO; **9.2 e 9.3: A CONFIRMAR** (art. 5º; art. 2º, II, parte final; R19 a R31; R85 e "Capítulo 5" do adendo D4 §3.4) |
| 10 | 30 | 10.1 (10); 10.2 (10); 10.3 (10) | D5-R01–R10; D5-R11–R20; D5-R21–R30 | 15/15 (12–18) | 10.3 2 | Anexo N do D5 §4 (Lei 14.133 integral) — CONFIRMADO |
| 11 | 30 | 10.4 (10); 10.5 (10); 10.6 (10) | D5-R31–R40; D5-R41–R50; D5-R51–R60 | 15/15 (12–18) | 10.4 1; 10.5 1; 10.6 2 | D5 §4 — CONFIRMADO; arts. 120 e 121 fora (seção 0.2, item 8) |
| 12 | 28 | 10.7 (10); 1.1 (9); 1.2 (9) | D5-R61–R70; D1-R13–R21; D1-R22–R30 | 14/14 (12–16) | 10.7 1 | 10.7: D5 §4 — CONFIRMADO; **1.1 e 1.2: A CONFIRMAR** (D1 §3, §5: CF, art. 37; Lei 9.784, art. 2º — princípios só "doutrinários" não têm base; D1 §4, §6.2, §6.4, §6.7: DL 200, arts. 4º a 6º e 10; Lei 11.107, art. 6º; Lei 13.303, arts. 3º e 4º) |
| **soma** | **356** | 34 folhas | D1 30; D2 80; D3 89; D4 87; D5 70 | 181/175 | **47 E (6 C)** | — |

Divisão de C/E das folhas divididas: 8.4 = 0/3 (L1) + 6/4 (L2); 6.4 = 5/3 (L2) + 2/2 (L3); 6.2 = 2/1 (L3) + 4/4 (L4). Alvos por folha das demais levas: o que leva a folha a 10/10 (ex.: 2.2 6/6; 6.5 7/5; 5.2 6/5; 3.3 6/4; 4.2 4/6; 8.2 4/6; 1.1 5/4; 1.2 4/5; demais 5/5).

**Regra para lastro "A CONFIRMAR"**: na ficha de cada leva, a GCB lista por folha os pontos com lastro literal ainda não usados; se forem menos que os itens previstos, pede adendo ao qa-normativo-da antes da produção (precedente das folhas 6.3, 8.1 e 8.4). Folha sem fonte oficial localizável fica abaixo de 20, com registro na reconciliação da leva (D-REFORCO-DA), e nunca recebe item sem base; a vaga não é preenchida com item de outra folha fora da ordem — a leva sai menor, e o plano das levas seguintes não muda. Folha cujo lastro dependa de pontos indiretos (6.3, 6.4) chega a 20 com itens de aderência parcial, piso de 10 diretos; se a gcb-cqfp recusar a pertinência dos indiretos, a folha fica abaixo (6.3: 14 só com diretos) e a reconciliação registra.

### 2.2 Moldura do Legislativo: meta da D-MOLDURA-CE cumprida na leva 5
Padrão adotado para cumprir a meta "o quanto antes" sem tirar nenhuma folha nem nenhum conjunto por lote da faixa de 40% a 60% de C e sem passar de 6 itens com moldura por folha:
- **Antecipação (levas 1 a 5)**: folhas com moldura 1 C / 0 E (8.1, 6.3, 8.4, 6.4, 6.5, 3.4) recebem **3 E e 1 C com moldura** (folha 2/3 = 40%; o C vai em par com um E além da cota, R3); folhas 2/0 (3.1, 4.1) recebem **3 E** (2/3 = 40%); a 5.2 recebe só a cota (1 E), para o conjunto do D3 não cair abaixo de 40%.
- **Depois da meta (levas 6 a 12)**: só a cota da seção 4 da T-122 (folha ≤ 60%); C com moldura só pela R3.
- **R4 da T-122**: se uma folha da antecipação não puder receber itens, a cota (não a antecipação) passa à próxima folha do mesmo lote com moldura, registrada na reconciliação.

| após a leva | novos C / E com moldura | acumulado novos | DA com moldura (C/E) | %C | meta (≤ 60%) |
|---|---|---|---|---|---|
| partida | — | — | 44/9 | 83,0% | — |
| 1 | 2 / 9 | 2 / 9 | 46/18 | 71,9% | — |
| 2 | 2 / 3 | 4 / 12 | 48/21 | 69,6% | — |
| 3 | 1 / 4 | 5 / 16 | 49/25 | 66,2% | — |
| 4 | 0 / 3 | 5 / 19 | 49/28 | 63,6% | — |
| **5** | 1 / 6 | 6 / 25 | **50/34** | **59,5%** | **cumprida** (25 E novos ≥ 21; 2C ≤ 3E: 100 ≤ 102) |
| 6 | 0 / 4 | 6 / 29 | 50/38 | 56,8% | mantida |
| 7 | 0 / 2 | 6 / 31 | 50/40 | 55,6% | mantida |
| 8 | 0 / 4 | 6 / 35 | 50/44 | 53,2% | mantida |
| 9 | 0 / 5 | 6 / 40 | 50/49 | 50,5% | mantida |
| 10 | 0 / 2 | 6 / 42 | 50/51 | 49,5% | mantida |
| 11 | 0 / 4 | 6 / 46 | 50/55 | 47,6% | mantida |
| 12 | 0 / 1 | 6 / 47 | 50/56 | 47,2% | mantida |

Conjuntos por lote ao fim do plano (exigência (a): cada um entre 40% e 60% de C): D4 14 C / 15 E (48,3%); D3 9/13 (40,9%); D2 10/14 (41,7%); D5 15/14 (51,7%). Na leva indicativa da T-122 a meta só se cumpria na leva 9; aqui, na 5. A margem da leva 5 é de 2 pontos (100 ≤ 102): E com moldura reprovado nas levas 1 a 5 é reposto na v2 da mesma leva (ponto da reserva, mesmo tipo de moldura); sem reposição, a meta passa à leva 6 e a reconciliação registra (R5 da T-122). A recontagem oficial é da GBQ, pelo script reaplicado ao pacote v1.14 (T-123).

### 2.3 Exigências (b), (c) e (d) — onde entram
| exigência | conteúdo | leva | como |
|---|---|---|---|
| (a) | item novo com moldura (D5, D2, D3, D4) e, no D4, expositor/analista, "pós-NPM" e "Considere que" preferencialmente E até 40–60% | 1 a 12 | seção 1, regras 10 e 11; seção 2.2; na leva 1, K1 a K4 com metas na seção 3.6 |
| (b) | D2-R: ao menos 3 C com termo absoluto que é a letra da norma — Lei 8.112, art. 49, § 1º ("para qualquer efeito"), art. 41, § 5º ("Nenhum servidor"), art. 20, § 4º ("somente") | **5** (folha 3.4) | três pontos reservados na 3.4 (D2-R31 a D2-R40), gabarito C, aderência direta; no máximo 1 com [TS] de elemento-isca (regra 7); os três dispositivos estão transcritos no Anexo N do D2 (§4.3, linhas do art. 20, § 4º, art. 41, § 5º, e art. 49, § 1º) e não são ponto de item canônico (T75_reconciliacao, linha 58; o D2 usa o art. 20, caput e § 3º, e o art. 41 da CF — "Difere de" obrigatório) |
| (b) | art. 135 da Lei 8.112 como primeiro ponto da folha 4.2 | **6** | D2-R51 = Lei 8.112, art. 135 (caput ou parágrafo único; Anexo N do D2 §4.3) — primeiro item da 4.2 no reforço |
| (c) | rever o par espelho D4-30/D4-29 (8.4) | **1 e 2** | decidido na seção 0.2, item 9 (sem errata; 8.4 sem novo item sobre o art. 2º, II, nem o art. 4º, IV); a gcb-cqfp confere nas duas levas |
| (d) | "faltam para 20" do D3 e aderência parcial com piso de 10 diretos | 1 a 7 (D3) | 89, não 86 (seção 0.2, item 6); regra da aderência parcial (seção 0.2, item 5) |

## 3. FICHA DA LEVA 1 — pronta para a gcb-cpp

### 3.1 Objeto (edital, literal; edital/DA_itens_1_12_P1.md)
- "8.1 Nova Governança Pública (New Public Governance): conceito, fundamentos e evolução." — 14 itens novos (D4-R01 a D4-R14); a folha vai de 6 a 20.
- "6.3 Responsabilidade por omissão do Estado." — 13 itens novos (D3-R01 a D3-R13); a folha vai de 7 a 20.
- "8.4 Valor Público, cadeia de valor público." — 3 itens novos (D4-R15 a D4-R17), primeira parte da folha (a segunda, 10 itens, é da leva 2).
Total: 30 itens. Saída: saida/gcb/DA_reforco_L01_v1.md, na estrutura da regra 14 (ordem das folhas no arquivo: 8.1, 6.3, 8.4). Contexto de uso: o analista legislativo do registro e da redação de sessões e reuniões da Câmara dos Deputados; exemplos hipotéticos, sem afirmar norma interna, sistema ou prática real da Câmara.

### 3.2 Fontes admitidas na leva 1
- 8.1 e 8.4: só os trechos R32 a R83 do adendo do D4 (saida/gcb/D4_anexo_N_adendo_2026-10-20.md, seção 5; URLs e consulta de 20/10/2026 como lá), com os alertas B1 a B10 (seção 6.2) de cumprimento obrigatório; para o contraste de justificativa, os trechos R1 a R31 do Anexo N do D4 (seção 5). Rótulo REFERENCIAL OUTRA_OFICIAL. Nenhum autor nomeado em item (seção 0.2, item 4); órgão (TCU, Casa Civil, CGU) pode ser nomeado.
- 6.3: só os dispositivos da seção 4 do adendo do D3 (saida/gcb/D3_anexo_N_adendo_2026-10-20.md; planalto.gov.br, consulta de 20/10/2026), com os alertas A1 a A13 (seção 5.2). CC, arts. 186 e 927: usados pela letra, sem afirmar efeito de decisão do STF (alerta A2). Nada sobre o regime da responsabilidade do Estado por omissão (objetiva × subjetiva, "culpa anônima", omissão genérica × específica): alerta A11, [SEM FONTE — não afirmar].
- Proibidos: memória, fonte secundária, jurisprudência, base doutrinária.

### 3.3 Pontos já usados pelos canônicos (não repetir; anti-gêmeo)
- 8.1 (D4-01 a D4-06): redes → NPG (R6); governo facilitador e participante das redes (R7); apoio à cooperação mútua, coprodução, parcerias e confiança (R7); fundamentos nas teorias de rede (R7); pós-NPM ligado a integração, colaboração e decisão inclusiva (R4); no pós-NPM a inspiração vem das redes (R8).
- 6.3 (D3-41, 43, 44, 45, 46, 47, 49): "causarem" no § 6º sem menção a omissão; CC, art. 43, sem menção a omissão; dever jurídico de agir; sem dano não há dever de indenizar; sem nexo não há dever (D3-45, com moldura, C); Estado não é segurador universal; conceito de conduta omissiva.
- 8.4 (D4-27 a D4-33): Decreto 9.203, art. 2º, II (definição e "preservados"); art. 4º, IV (articulação); cadeia de Porter adaptada (R16, CGU); desempenho como fluxo dos insumos ao valor (R17); desempenho como processo de geração de valor (R17, D4-32, com moldura, C); elos da cadeia das políticas públicas (R18).

### 3.4 Pontos de julgamento por item (sugeridos; a gcb-cpp redige, ordena dentro da folha pelo teste de sequência e numera na faixa da folha)
Colunas: ponto (código do adendo) | trecho/dispositivo | o que se julga (sentido da troca, sem redação) | formato | moldura | gab. | [TS] | aderência | difere de.

**Folha 8.1 — 14 itens (7 C / 7 E), D4-R01 a D4-R14**
| # | ponto | base | o que se julga | form. | moldura | gab. | [TS] | ader. | difere de |
|---|---|---|---|---|---|---|---|---|---|
| 1 | A8.1-07 | R37 | a NPG molda espaço de governança orientado para redes no setor sem fins lucrativos e entre o público e o privado com fins lucrativos | DEF | N | C | não | direta | D4-05 (o que o governo apoia, não o espaço) |
| 2 | A8.1-09 | R39 | o tipo ideal da NPG resulta num "Estado de rede", com a confiança mútua como princípio de ligação para a prestação de serviços | APL | S — expositor — fecho acerto | C | não | direta | D4-02 (papel do governo nas redes, não o "Estado de rede") |
| 3 | A8.1-10 | R39 | a legitimidade da NPG baseia-se em valores compartilhados e na cultura de coprojeto, codecisão, coprodução e coavaliação | DEF | N | C | opcional (isca: "coavaliação", literal) | direta | D4-05 |
| 4 | A8.1-11 | R40 | hierarquia na NPG: provavelmente mais informal (troca para "mais formal/rígida") | APL | S — expositor — fecho acerto | E | sim (informal → formal) | direta | — |
| 5 | A8.1-29 | R57 | no pós-NPM do debate de governança, a função estatal não é a de único remador, e sim a de direcionador (troca para "único remador") | DEF | N | E | sim | direta | D4-06 (integração, colaboração; não o papel do Estado) |
| 6 | A8.1-13 | R42 | correspondência hierarquia → administração pública tradicional; mercados → nova gestão pública; redes → NPG | PAR | N | C | não | direta | D4-03 (inspiração nas redes no pós-NPM; aqui a correspondência entre mecanismo e modelo) |
| 7 | A8.1-14 | R43 | a NPG avança pela relação de múltiplos atores na prestação de serviços por meio de redes | DEF | N | C | não | direta | D4-02 |
| 8 | A8.1-15 | R44 (apoio R41) | a NPG não substituirá integralmente os arranjos anteriores (troca para "substituirá integralmente") — **só a versão E** (alerta B4) | APL | S — expositor — fecho acerto | E | sim | direta | — |
| 9 | A8.1-16 | R45 | NPM: capital econômico e competição; NPG: capital social (troca do capital atribuído à NPG) | APL | S — expositor — fecho neutro | E | sim (capital social → capital econômico e competição) | direta | D4-01 (princípio orientador, não o capital) |
| 10 | A8.1-18 | R46 | natureza do Estado na NPG: plural e pluralista (unitário na administração pública; regulatório na nova gestão pública) | PAR | N | C | não | direta | — |
| 11 | A8.1-20 | R46 | mecanismo de alocação de recursos na NPG: networks e contratos relacionais (hierarquia; mercado e contratos clássicos ou neoclássicos, nos outros dois) | PAR | N | C | não | direta | D4-04 (fundamentos teóricos, não o mecanismo de alocação) |
| 12 | A8.1-26 | R53 | no pós-NPM, as práticas de gestão são mais continuidade e incrementalismo do que ruptura (troca para "ruptura") | SIT (analista) | N — fecho acerto ("ele estará correto ao afirmar") | E | sim | direta | D4-03 |
| 13 | A8.1-27 (alínea i) | R55 | tendência do pós-NPM: fortalecimento da burocracia pública (troca para "enfraquecimento/redução") | SIT (analista) | N — fecho acerto | E | sim | direta | D4-08 (colaboração e parcerias; outra alínea) |
| 14 | A8.1-30 | R83 | na lógica de governança (pós-NPM), o cidadão é parceiro da formulação e da implementação (troca para "apenas beneficiário final") | SIT (analista) | N — fecho neutro | E | sim | direta | — |

Reserva da 8.1 (para reprovado ou substituição, na ordem): A8.1-04, A8.1-21 (só E: "substituição"; nunca a versão C de "alternativa" como fato), A8.1-19, A8.1-27 (alíneas c, d, e, g ou h; uma por item, com "pós-NPM"), A8.1-28 (com "pós-NPM"), A8.1-22. Fora (seção 0.2, item 4, e gêmeos): A8.1-02 (gêmeo do D4-01), A8.1-06 e A8.1-17 (gêmeos do D4-04), A8.1-08 (vizinho do D4-01), A8.1-12 (vizinho do item 8 desta leva), A8.1-23, 24, 25; A8.1-01, 03 (Estado Neoweberiano e "4M's": fora do núcleo da folha).

**Folha 6.3 — 13 itens (8 C / 5 E), D3-R01 a D3-R13**
| # | ponto | base | o que se julga | form. | moldura | gab. | [TS] | ader. | difere de |
|---|---|---|---|---|---|---|---|---|---|
| 1 | A6.3-01 | CC, art. 186 | o ato ilícito resulta de ação **ou omissão** voluntária (troca para "só ação") | APL | S — órgão/servidor do Poder Legislativo da União | E | sim (ação ou omissão → ação) | direta | D3-49 (art. 43, não o 186) |
| 2 | A6.3-02 | CC, art. 186 | negligência e imprudência configuram o ato ilícito | DEF | N | C | não | direta | — |
| 3 | A6.3-03 | CC, art. 927, caput | quem causar dano por ato ilícito (arts. 186 e 187) fica obrigado a repará-lo; a remissão alcança o art. 186 | DEF | N | C | não | direta | D3-44 (base doutrinária; aqui a letra do art. 927) |
| 4 | A6.3-07 | Lei 14.133, art. 121, § 2º | a responsabilidade da Administração pelos encargos depende de **comprovada falha na fiscalização** | APL | S — órgão do Poder Legislativo da União (contratante) | C | não | direta | D3-45 (nexo, base doutrinária) |
| 5 | A6.3-08 | Lei 14.133, art. 121, § 2º | solidária nos encargos previdenciários, subsidiária nos trabalhistas (permuta) | APL | S — órgão do Poder Legislativo da União | E | sim (solidariamente ↔ subsidiariamente) | direta | — |
| 6 | A6.3-09 | Lei 14.133, art. 121, § 2º | a hipótese vale **exclusivamente** nos serviços contínuos com dedicação exclusiva de mão de obra (situação fora dela) | APL | S — órgão do Poder Legislativo da União | E | sim (exclusivamente → em qualquer contratação) | direta | — |
| 7 | A6.3-04 | Lei 8.112, art. 122, caput | a responsabilidade civil **do servidor** decorre de ato omissivo ou comissivo (sujeito nomeado: servidor; alerta A1) | SUJ | N | C | não | parcial | — |
| 8 | A6.3-05 | Lei 8.112, art. 122, caput | o ato pode ser doloso ou culposo e o prejuízo, ao erário ou a terceiros | DEF | N | C | opcional (isca: "ou a terceiros", literal) | parcial | item 7 (outro elemento do caput) |
| 9 | A6.3-06 | Lei 8.112, art. 124 | a responsabilidade civil-administrativa resulta de ato praticado **no desempenho do cargo ou função** (troca para "independentemente de…") | PAR | N | E | sim | parcial | item 7 (art. 124, não o 122) |
| 10 | A6.3-11 | CDC, art. 22, parágrafo único | descumprimento, total ou parcial, do dever de serviço adequado: as pessoas jurídicas são compelidas a cumprir e a reparar | SIT | N | C | não | parcial | — |
| 11 | A6.3-12 | CDC, art. 22, caput | o dever alcança os órgãos públicos, por si ou suas empresas, concessionárias, permissionárias ou outra forma de empreendimento | SUJ | N | C | não | parcial | — |
| 12 | A6.3-13 | Lei 6.938, art. 3º, IV | poluidor inclui a pessoa jurídica de direito público, responsável direta ou indiretamente | SIT | N | C | opcional (isca: "de direito público", literal) — no máximo 1 isca na folha | parcial | — |
| 13 | A6.3-14 | Lei 6.938, art. 14, § 1º | o poluidor indeniza **independentemente da existência de culpa** (troca para "mediante culpa"); a segunda frase do § 1º não é usada (alerta A12) | PAR | N | E | sim | parcial | D3-46 (segurador universal, base doutrinária) |

Piso de diretos: 7 canônicos + 6 diretos novos = 13 ≥ 10. Aderência parcial: 7 (itens 7 a 13). Reserva da 6.3: A6.3-15 (Lei 4.619, art. 3º; só "nos termos da Lei 4.619/1965", sem atualizar órgão ou carreira, alerta A8). Fora: A6.3-10 (gêmeo do D5-37, seção 0.2, item 8). Se a gcb-cqfp recusar a pertinência de indiretos sem reserva para repor, a folha fica abaixo de 20 com registro (seção 2.1).

**Folha 8.4 — 3 itens (0 C / 3 E), D4-R15 a D4-R17 (primeira parte)**
| # | ponto | base | o que se julga | form. | moldura | gab. | [TS] | ader. | difere de |
|---|---|---|---|---|---|---|---|---|---|
| 1 | A8.4-06 | R63 (TCU, citando Kaplan e Norton; item atribui ao TCU) | nas unidades de apoio, os clientes são quase sempre internos (troca para "externos") | APL | S — expositor — fecho acerto | E | sim | direta | D4-33 (Porter adaptado, não unidades de apoio) |
| 2 | A8.4-08 | R64 (TCU) | cabe **à liderança** implementar as formas de criação de valor para a sociedade (troca de sujeito para "às unidades de apoio") | APL | S — expositor — fecho acerto | E | sim (liderança → unidades de apoio) | direta | D4-32 (desempenho como geração de valor) |
| 3 | A8.4-16 | R72 | atuações econômicas e eficientes, mas inefetivas, não geram valor público (troca para "geram valor mesmo inefetivas") | APL | S — expositor — fecho neutro | E | sim | direta | D4-31 e D4-32 (R17) |

O C com moldura da 8.4 (par da R3) e os outros 9 itens vão na leva 2. Reserva da primeira parte: A8.4-07, A8.4-01. Fora da 8.4 em todo o reforço: Decreto 9.203, art. 2º, II, e art. 4º, IV (seção 0.2, item 9); A8.4-27 (mesmo trecho R83 do item 14 da 8.1).

### 3.5 Formatos ao fim da leva (folha inteira; teto 6 em 20)
| folha | DEF | SUJ | SIT | NUM | PAR | APL | total |
|---|---|---|---|---|---|---|---|
| 8.1 (canônicos 2/0/1/0/2/1 + leva) | 2+4 = **6** | 0 | 1+3 = 4 | 0 | 2+3 = 5 | 1+4 = 5 | 20 |
| 6.3 (canônicos 2/0/3/0/1/1 + leva) | 2+3 = 5 | 0+2 = 2 | 3+2 = 5 | 0 | 1+2 = 3 | 1+4 = 5 | 20 |
| 8.4 (canônicos 2/0/2/0/2/1 + 3) | 2 | 0 | 2 | 0 | 2 | 1+3 = 4 | 10 (leva 2 completa; APL final 5) |
DEF da 8.1 fica no teto (6): a gcb-cpp não declara outro DEF na folha; item que a QA reclassifique para DEF obriga a trocar o formato de outro.

### 3.6 Gabarito, moldura e conjuntos ao fim da leva
- Leva: **15 C / 15 E (50%)**; faixa admitida 12–18 C. Folhas: 8.1 10/10 (canônicos 3/3 + 7/7); 6.3 10/10 (2/5 + 8/5); 8.4 4/6 parcial (4/3 + 0/3; fecha em 10/10 na leva 2).
- Moldura nova: 2 C (8.1 item 2; 6.3 item 4) e 9 E (8.1 itens 4, 8, 9; 6.3 itens 1, 5, 6; 8.4 itens 1, 2, 3). DA: 46/18 (71,9%). Folhas: 8.1 2/3; 6.3 2/3; 8.4 1/3 (2/3 com o C da leva 2). No máximo 6 com moldura por folha: 8.1 5; 6.3 5; 8.4 4 (5 na leva 2).
- Conjuntos do D4 (regra 11), com os 17 itens D4-R da leva: K1 moldura 13 C / 6 E (68,4%; a leva 2 e as levas 8 e 9 completam: fim do plano 14/15); **K2 fecho de acerto 6/6 (50%)** — fecho acerto só nos itens 2, 4, 8, 12, 13 da 8.1 e 1, 2 da 8.4; fecho neutro nos itens 9 e 14 da 8.1 e 3 da 8.4; **K3 "pós-NPM" 4/4 (50%)** — itens 5, 12, 13 e 14 da 8.1 dizem "pós-NPM"; nenhum outro item da leva usa a expressão; **K4 "Considere que" 22/17 (56,4%)** — abrem com "Considere que" os 10 itens de moldura ou analista da 8.1 e da 8.4 (2, 4, 8, 9, 12, 13, 14; 1, 2, 3 da 8.4) e nenhum outro item C do D4 nesta leva.
- Conjunto do D3: 7 C / 4 E (63,6%; fecha em 9/13 no fim do plano).

### 3.7 Despacho à gcb-cpp
- Executor: gcb-cpp (sonnet), uma instância. Objeto: leva 1 do reforço de DA, conforme esta seção 3, as regras da seção 1 e os anexos abaixo. Saída: saida/gcb/DA_reforco_L01_v1.md, terminando em "FIM DA LEVA 01 — REFORÇO DA".
- Anexos (lista exaustiva): esta ficha; saida/gcb/D4_anexo_N_adendo_2026-10-20.md (seções 3.1, 3.2, 5 e 6.2); saida/gcb/D3_anexo_N_adendo_2026-10-20.md (seções 3.1, 4 e 5.2); saida/gcb/D4_anexo_N_mapa_normativo.md (seção 5, só para contraste em justificativa) e saida/gcb/D4_ficha_lote.md (seções 3.2, 3.3 e 6); regras/estilo_banca.md (mecanismos E1–E6, C1–C6); modelo de bloco: saida/gcb/D4_v2_1.md, seção 5.2. Os canônicos D4_v2_1.md e D3_v2_1.md só para conferir os pontos já usados (seção 3.3).
- A gcb-cpp pode trocar um ponto sugerido por outro da reserva da mesma folha, com o motivo no bloco à GCB, desde que mantenha formato, gabarito, moldura e aderência da linha ou recalcule as seções 3.5 e 3.6 e continue dentro de todas as faixas.
- Dúvida de conteúdo vai ao bloco à GCB, sem consulta a terceiros. Nada vai à plataforma nem à candidata. Sem commit.

## 4. Critérios de QA da gcb-cqfp (R1 e R2 de cada leva)
O parecer dá veredito por item (APROVADO | APROVADO COM AJUSTE | REPROVADO), por folha e na leva, refaz por script próprio as contagens da seção 4 do arquivo da leva e confere cada base contra o Anexo/adendo (arquivo e linha).

### 4.1 O que reprova o item
1. Base ausente, fora do Anexo N/adendo, revogada, doutrinária, de autor nomeado no item ou atribuída ao órgão quando é de autor; trecho que não confere literalmente com a linha do Anexo/adendo; URL ou data diferentes das registradas.
2. Gabarito errado ou discutível pela letra da base; "E por ausência" (fora de rol fechado); E decidido pela moldura; item que afirme SEM FONTE (alerta A11 do D3; seção 3.4 da ficha do D4; B3, B4 e B7 do adendo do D4).
3. Ponto de julgamento repetido na folha (canônico ou D<n>-R já aceito) ou gêmeo de canônico da mesma folha (regras 1 e 2); ponto fora da folha (pertinência nem direta nem parcial).
4. Duas afirmações, "exceto", alternativas, ou duas exigências somadas quando uma já decide o gabarito.
5. Afirmação sobre norma interna, sistema ou prática real da Câmara; afirmação de que o Decreto 9.203 alcança (ou não) a Câmara; efeito de decisão do STF.
O item reprovado é substituído na v2 por item novo, de ponto da reserva da mesma folha, com o próximo id livre do lote; o id reprovado não volta. Reprovação acima de 30% dos itens da leva: "GATE: QA reprovou >30% — decisão humana" (a leva para; nenhuma leva nova). Item reprovado no R2: sai sem substituto (lacuna registrada na reconciliação); a leva segue se ficar na faixa de C/E.

### 4.2 O que pede ajuste (não reprova)
Formato mal declarado; [TS] sem troca real ou troca não declarada no campo "Troca"; C-isca acima de 1 por folha; moldura S/N, tipo ou fecho (acerto/neutro) errados; aderência mal declarada; justificativa com mais de duas linhas ou com afirmação fora da base; "Difere de" ausente ou impertinente; campo faltante; teste de sequência reprovado (troca de posição dentro da folha); teto de formato, VOLÁTIL ou moldura por folha excedido (corrige-se trocando a construção de um item, sem mudar o ponto); C/E da leva ou de K1 a K4 fora da faixa da ficha.

### 4.3 Texto exato do ajuste (obrigatório)
Cada ajuste vem numa linha, no formato:
`AJ-<n> | <id> | <campo> | substituir: «<trecho atual, literal, único no arquivo>» | por: «<texto novo, literal>»`
O trecho atual tem de ocorrer uma única vez no arquivo da leva; o texto novo é aplicado pela gcb-cpp por substituição exata, sem outra mudança, e a reconciliação confere por diff (precedente do aplicar_substituicoes.py). Ajuste que dependa de escolha da produção não é "texto exato": vira reprovação com motivo. O R2 confere cada AJ aplicado literalmente e examina só o que a v2 mudou além dos AJ.

### 4.4 Conferências de leva (o parecer registra cada uma como CONFERE / NÃO CONFERE)
(1) C/E da leva na faixa; (2) por folha, tetos de formato, VOLÁTIL ≤ 20%, moldura ≤ 6, piso de 10 diretos; (3) moldura acumulada de DA e dos conjuntos por lote igual à da seção 2.2 (ou desvio registrado); K1 a K4 do D4 na faixa da seção 3.6; (4) pontos da leva sem duplicata entre si e com os canônicos; (5) exigências da leva (seção 2.3); (6) primeiro e último id de cada lote; (7) linha 1 e última linha; (8) amostra de 5 bases reabertas no cache saida/gcb/normativo_cache/ (texto) e, para os referenciais, conferência do trecho na cópia gravada do adendo.

## 5. Amostra para a gbq-estilo (10% por leva; D-REFORCO-2, regra 6)
- Tamanho: ⌈10% dos itens da leva⌉, com acréscimo quando a regra de composição exigir. Composição: ao menos 1 E com moldura enquanto a leva tiver cota (R1 da T-122); ao menos 1 item de cada lote da leva; ao menos 1 C; ao menos 1 item de aderência parcial quando houver. A GCB designa a amostra por ponto na ficha da leva, antes da produção (amostra cega quanto ao resultado do QA); a gbq-estilo audita sobre a versão aprovada no R2 e grava saida/banco/estilo_onda_DA_L<nn>.md; reprovação de estilo de item aprovado volta como AJ (seção 4.3) antes da reconciliação.
- **Leva 1 (4 itens, 13%)**: 8.1 item 13 (A8.1-27, alínea i; SIT, E, pós-NPM, K2/K3/K4); 6.3 item 4 (A6.3-07; APL, C com moldura do par da R3 no D3); 6.3 item 11 (A6.3-12; SUJ, C, parcial); 8.4 item 2 (A8.4-08; APL, E com moldura, troca de sujeito).

## 6. Riscos e registros
1. Lastro "A CONFIRMAR" em 13 folhas (2.2, 5.2, 6.2, 4.1, 5.1, 6.1, 8.2, 8.3, 9.1, 9.2, 9.3, 1.1, 1.2): adendos prováveis antes das levas 2, 3, 5, 7, 8, 9 e 12; folha sem fonte fica abaixo de 20 (a soma 356 é teto, não promessa).
2. Margem estreita da meta de moldura na leva 5 (seção 2.2): reposição obrigatória de E com moldura reprovado nas levas 1 a 5.
3. Conjunto do D3 termina em 40,9% (perto do piso): nas levas 3 e 7, C com moldura além do plano não entra no D3.
4. Leva 1 com 11 itens com moldura de 30 (37%) e 7 de aderência parcial na 6.3: a auditoria de estilo cobre os dois; parcial só em simulado diagnóstico.
5. Três folhas divididas entre levas (8.4, 6.4, 6.2): limites conferidos na folha acumulada.
6. Nenhuma tarefa nova (D-COMPLEMENTOS); nenhum gatilho em PARA_PRESIDENCIA.md por esta ficha (função própria da Gerência titular: ficha do lote, D-REFORCO-2 e D-DA-PRODUTOR).

## 7. Adendo após a leva 1 (gcb-gerencia, 20/10/2026, ciclo s15c3)
Fonte: reconciliação saida/gcb/DA_reforco_leva1_reconciliacao_2026-10-20.md (seção 4), parecer QA R1/R2 da gcb-cqfp e auditoria de estilo saida/banco/estilo_DA_reforco_leva1.md (seção 6). Este adendo prevalece sobre as seções 0 a 5 onde divergir; o texto acima fica como estava (SHA-256 antes do adendo: acf8b57af3f42e0bcab9a6d92f6cfa3dd70deacf3f521fc285e5b3a1b0d95133). Vale para as levas 2 a 12.

### 7.1 Ids e faixas
- D4-R12 vago (reprovado no R1 da leva 1; não volta). D4-R18 usado na 8.1 (substituto). Faixas do D4 deslocadas em +1: leva 2, 8.4 = **D4-R19 a D4-R28**; leva 8 = D4-R29 a R58; leva 9 = D4-R59 a R88. Faixas de D1, D2, D3 e D5 inalteradas (D3 segue em D3-R14).

### 7.2 Núcleo (corrige a seção 0.2, item 10)
- O campo "nucleo" segue o critério já fixado na D1 da GBQ e sem objeção da presidência (D-NUCLEO-CRITERIO): k1 data de canonização → k2 ordem do ato → **k3 direta antes de parcial, só no empate dentro do mesmo ato** → k4 posição no pacote. Cada gatilho A de leva é um ato; dentro dele, os diretos da folha vêm antes dos parciais e, entre iguais, vale a ordem do arquivo da leva. A "ordem de id" da seção 0.2, item 10, só vale quando não há parcial no ato.
- Leva 1: 8.1 → D4-R01 a D4-R04; 6.3 → **D3-R02, D3-R03 e D3-R05** (o D3-R01 é parcial); 8.4 → D4-R15 a D4-R17 (a 8.4 chega a 10 de núcleo; os itens da leva 2 nessa folha ficam false).

### 7.3 Teste de sequência (complementa a regra 6 da seção 1)
- A ficha de cada leva roda o teste (gabarito e [TS]) sobre o **plano** de cada folha acumulada (canônicos na ordem do pacote + reforço já aceito + plano da leva) antes do despacho; plano que reprove é refeito antes da produção.
- Folha dividida entre levas (8.4, 6.4, 6.2): o primeiro item da segunda parte fecha qualquer corrida ou bloco aberto no fim da primeira. **Leva 2: D4-R19 (primeiro item da 8.4) é C sem [TS]** (a 8.4 acumulada termina em E E E e o bloco de [TS] de período 3 em 9 itens; com C sem [TS] o gabarito passa e o bloco não cresce). O bloco de [TS] das posições 1 a 9 da 8.4 (nTTnTTnTT) é desvio aceito e registrado na reconciliação da leva 1 e não conta como falha das levas seguintes; o resto da folha passa o teste inteiro.
- Ordem de apresentação: na consolidação (T-123), dentro de cada folha, canônicos na ordem do pacote v1.13 e depois os D<n>-R na ordem do arquivo da leva (na 8.1, o D4-R18 entre D4-R11 e D4-R13) — é a ordem sobre a qual o teste e o núcleo foram calculados.

### 7.4 Pista de forma — "Considere que", fecho neutro e negação frontal (recomendações L2-1 a L2-4 da gbq-estilo, generalizadas)
As faixas de K1 a K4 (regra 11), a cota de E com moldura (seção 2.2) e a R3 prevalecem; dentro delas:
1. **Fecho neutro do D4** ("Nessa situação, é correto afirmar que …"; partida 0 C / 3 E: D4-R08, R13, R17): na 8.4 da leva 2, ao menos 2 itens C usam esse fecho (um deles pode ser o C com moldura do par da R3); nenhum E novo do D4 usa o fecho neutro até o D4 acumulado com ele chegar a 40% de C; depois, o conjunto fica entre 40% e 60% de C (levas 8 e 9). A ficha da leva 2 confere K4 com esses C (K4 hoje 23/17; não pode passar de 60%).
2. **Abertura por leva**: em cada leva, os itens com "Considere que" ficam com ao menos 40% de C e os declarativos (sem "Considere que") com ao menos 40% de E (leva 1: 5 C / 12 E e 10 C / 3 E; regra ingênua "Considere que → E" com 73,3% de acerto na leva isolada). O equilíbrio vem dos itens sem moldura.
3. **Fórmula repetida**: nas folhas do D3 (levas 2, 3, 4 e 7), no máximo metade dos itens com "Considere que" usa "Nessa situação, nos termos d…"; os demais citam a norma no cenário ou no fim do enunciado (leva 1: 6 de 6). A mesma métrica é contada e informada, sem limite, nos lotes D1, D2 e D5.
4. **Contraste e troca de sujeito**: no D4, ao menos 1 item C novo usa o contraste ", e não …" (acumulado 0 C / 2 E). Em todo item SUJ (todos os lotes), o sujeito trocado é ator que a própria fonte menciona e seria plausível na função, nunca um cujo nome já negue a função (D4-R16, "unidades de apoio").
5. **Negação frontal**: item E não monta cenário que enumere todos os elementos do dispositivo para negar a conclusão no fecho (D3-R02, registro da gbq-estilo, seção 3).
6. Medida: a seção 4 do arquivo de cada leva traz, por script, abertura × gabarito e fecho × gabarito por lote (canônicos, leva, acumulado), e a reconciliação confere.

### 7.5 Nomes de arquivo (substitui os nomes das regras 14 e 15)
Vale o padrão do despacho usado na leva 1: saida/gcb/DA_reforco_leva<n>_v<k>.md; saida/gcb/QA_DA_reforco_leva<n>_R<k>_<data>_gcb-cqfp.md; saida/banco/estilo_DA_reforco_leva<n>.md; saida/gcb/DA_reforco_leva<n>_reconciliacao_<data>.md. A última linha do arquivo da leva continua "FIM DA LEVA <nn> — REFORÇO DA".

### 7.6 Texto do estilo sobre itens já aprovados
Texto exato da gbq-estilo sobre item aprovado no R2 não é aplicado ao objeto da leva depois do R2 (a D-REFORCO-DA limita a QA a 2 rodadas): vira errata registrada na reconciliação, com "antes" e "depois" literais, e entra na consolidação pela GBQ por substituição exata com aborto, se o aceite da leva a incluir (precedente D-V112-BAEF-P2-ACEITE). Texto que mude campo Troca, gabarito ou construção (ex.: AJ-E3) não entra sem QA própria. Para evitar o caso, a amostra do estilo da leva seguinte pode ser auditada sobre a v1, em paralelo ao R1, e os AJ de estilo seguem com os AJ do R1 para a v2.

FIM DA FICHA DO REFORÇO DA
