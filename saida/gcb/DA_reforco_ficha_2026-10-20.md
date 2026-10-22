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

## 8. Ficha das LEVAS 2 e 3 (gcb-gerencia, 20/10/2026, ciclo s15c4)
Acréscimo desta data, só acréscimo antes da última linha (SHA-256 da ficha antes dele: 6e90dc130678de333a5e1b3ff4a4af52b0bb7295b75cd8f4f9fa64f0b50ec41b, a versão citada na D-T116-LEVA1-ACEITE). Valem as regras da seção 1 com a seção 7 (Adendo após a leva 1), lida a seção 7.6 como a D-T116-LEVA1-ACEITE a fixou, as decisões da reconciliação da leva 1 (saida/gcb/DA_reforco_leva1_reconciliacao_2026-10-20.md, 422e63b1…2b6e: seções 4 e 5) e a D-T116-LEVA1-ACEITE (DECISOES.md). Onde esta seção diverge do plano da seção 2.1 para as levas 2 e 3, vale esta seção. A leva 3 só abre com o QA da leva 2 fechado (D-REFORCO-DA). Sem commit nem push.

### 8.1 Entradas e conferência
| objeto | SHA-256 (início…fim) | uso |
|---|---|---|
| saida/gcb/D1_anexo_N_adendo_2026-10-20.md | cb4d02f9…73f9 | lastro da folha 2.2 (seção 3.1: A2.2-01 a A2.2-27; textos na seção 4; alertas P1 a P8) |
| saida/gcb/D3_anexo_N_adendo_2026-10-20.md | bbfd3eed…a797 (com o "Adendo 2"); seções 1 a 5 inalteradas: os primeiros 56.943 bytes dão c8ad5bd2…b9f74a50, o SHA-256 da seção 0.1 | 6.4 (3.2), 6.5 (3.3), alertas A1 a A13 (5.2); 5.2 (A2.3.1) e 6.2 (A2.3.2), alertas C1 a C12 (A2.5.2) |
| saida/gcb/D4_anexo_N_adendo_2026-10-20.md | c32f58eb…16fb5 (igual à seção 0.1) | 8.4 (3.2; R59 a R81), alertas B1 a B10 |
| saida/gcb/DA_reforco_leva1_v2.md | 2c431529…a4f04 | pontos já usados na 8.4 (D4-R15 a D4-R17) e na 6.3 (CC, arts. 186 e 927; Lei 8.112, arts. 122 e 124) |
| D1_v2.md; D3_v2_1.md; D4_v2_1.md | 63bd27c3…, 0f7a8b09…, c1a7a935… | pontos, formatos e [TS] dos canônicos das seis folhas |
| saida/pacote/pacote.json v1.13; pacote_estudante.json v1.13-E | 82c4117c…f240; 04cbd593…0c40 | ordem do pacote, gabarito, aderência e núcleo dos canônicos |
| saida/banco/moldura_ce_itens_2026-10-20.csv; moldura_ce_2026-10-20.md | ed4b364d…daac | moldura oficial dos canônicos; critério (seção 1) e cotas (seção 4) |
| saida/banco/estilo_DA_reforco_leva1.md | 2d50c4cb…8878 | texto exato da AJ-E1 (D3-R13) |

Conferência própria (python3 -I, somente leitura; scripts no scratchpad da sessão, gcb_l23/canon.py, seq.py, final.py e count.py, fora do repositório): canônicos das seis folhas extraídos do pacote v1.13 na ordem do pacote, com gabarito, moldura do CSV, aderência, formato e [TS] dos arquivos canônicos; plano das duas levas codificado item a item; teste de sequência (seção 1, regra 6, e seção 7.3) e todas as contagens das seções 8.3 e 8.4 refeitos sobre o plano. Partidas conferidas: DA com moldura 46 C / 18 E (71,9%); D3 7/4; D4: K1 13/6, K2 7/6, K3 5/4, K4 23/17, fecho neutro 0/3, contraste ", e não" 0/2.

### 8.2 Decisões da GCB (D1) desta seção
1. **Formatos dos canônicos da 2.2** (D1_v2.md não tem o campo; seção 0.2, item 2): D1-53 NUM (quinze dias); D1-54 PAR (parecer obrigatório × facultativo); D1-55 DEF; D1-56 PAR (vinculante × não vinculante); D1-57 DEF; D1-58 PAR (dolo ou erro grosseiro × culpa leve); D1-59 DEF; D1-60 DEF. Partida da folha: DEF 4, PAR 3, NUM 1. [TS] dos canônicos: D1-54, D1-56, D1-58 e D1-59.
2. **CF, art. 5º, LXXV, fica com a 6.2** (alerta C7): A6.2-05 e A6.2-06 podem ir à 6.2; A6.4-03 e A6.4-04 ficam fora da 6.4. Motivo: a 6.2 tem o lastro mais curto (A2.3.2: 6 diretos, 2 deles os de LXXV) e os seus indiretos são do regime civil comum (C9), de pertinência mais fraca que os indiretos da 6.4 (regresso, sucessores, prazos). Efeito: a 6.4 usa os 6 diretos restantes na leva 2 e completa os 20 com 6 itens de aderência parcial (2 na leva 2, 4 na leva 3); piso 8 + 6 = 14 diretos.
3. **Lei 12.016 ("Vide ADIN 4296" no art. 1º, caput e § 2º, e no art. 23; alerta C2)**: o art. 1º, caput e § 1º, entra pela letra, sem afirmar efeito de decisão do STF (o mesmo tratamento dado aos arts. 186 e 927 do CC na leva 1, alerta A2); o § 2º do art. 1º (A5.2-09) e o art. 23 (A5.2-11) não entram.
4. **Moldura implícita**: pelo critério oficial (relatório da T-122, seção 1, questão 2), "Poder Legislativo" como único Poder da frase é moldura S (borda poder_isolado) e não conta para a cota. Logo, nenhum item sem moldura declarada nomeia o Poder Legislativo, a Câmara, o Congresso, parlamentar, comissão legislativa ou sessão plenária; o A5.2-18 (Lei 13.869, art. 2º, II, "membros do Poder Legislativo") só entra como o E com moldura de cena da 5.2. O Decreto 9.830 nunca leva moldura (alertas P3 e C6): os itens dele dizem "Segundo o Decreto nº 9.830/2019" e põem a cena com "agente público", sem órgão do Legislativo; o do art. 14 nomeia o alcance ("No âmbito do Poder Executivo federal").
5. **Concentração na 2.2** (sugestão do adendo do D1, seção 3.1, adotada): no máximo 5 itens do Decreto 9.830 e 4 da Lei 14.133; só pontos diretos (a folha chega a 20 diretos). Fora: LINDB, art. 28 (A2.2-05, gêmeo do D1-57; fica na reserva só como E de troca de sujeito), Lei 9.784, art. 47 (A2.2-04), Lei 14.133, art. 73 (A2.2-24), LC 73 (A2.2-25 a 27; alerta P7) e Decreto 9.830, art. 12, § 7º (contexto, P6).
6. **Pontos fora por gêmeo, atribuição ou gabarito discutível**: A8.4-04 (mesmo trecho R62 do D4-R24); A8.4-19 (mesma lista de cinco componentes do D4-28); A8.4-26 (verdade atribuída a Osborne; seção 0.2, item 4); A8.4-15 (lista de oito elos de autor, alerta B5); A8.4-22 e A8.4-23 (consumidos como contraste no D4-R19 e no D4-R27); A6.4-14 (LINDB, art. 28: gêmeo entre lotes do D1-57; alerta A9); A6.5-13 (seção 0.2, item 8); A6.5-18 (Lei 8.112, art. 126: a troca "administrativa → civil" esbarra no CC, art. 935, e o gabarito ficaria discutível; alerta A5).
7. **Sequência — desvios de legado**: na ordem do pacote v1.13, os canônicos de quatro folhas já reprovam o teste antes de qualquer item novo: 2.2, alternância de 6 (D1-53 a D1-58), no gabarito e no [TS]; 6.4, bloco de período 3 com 8 itens (D3-51 a D3-59), no gabarito; 6.5, alternância de 5 (D3-62 a D3-67), no gabarito e no [TS]; 6.2, bloco de período 4 com 8 itens (D3-33 a D3-81, posições 2 a 9), no gabarito. É legado canônico, não imputável à leva (seção 0.2, item 2; precedente do bloco da 8.4, reconciliação da leva 1, 4.1); fica registrado e não é corrigido (a ordem dos canônicos não muda no reforço; D-COMPLEMENTOS). Exigência desta ficha: o primeiro item novo de cada folha fecha a corrida ou o bloco aberto, e nenhuma janela reprovada inclui item novo. O plano das seções 8.3 e 8.4 cumpre isso (conferido por script; seção 8.5).
8. **Ajustes ao plano da seção 2.1** (o lastro e a sequência pedem; registrados): leva 2 sem mudança de folhas, números nem C/E (8.4 +10, 6/4; 2.2 +12, 6/6; 6.4 +8, 5/3). Leva 3 com as mesmas folhas e números (6.4 +4; 6.5 +12; 5.2 +11; 6.2 +3), mas a 6.2 passa de 2 C / 1 E para **1 C / 2 E** (nenhuma das três ordens com 2 C / 1 E passa o teste na 6.2 acumulada, que termina em C E E C: ou estende o bloco de período 4 do legado, ou forma alternância de 5 no [TS]; conferido por script). Efeitos: leva 3 com 16 C / 14 E, e não 17/13; a 6.2 da leva 4 passa a 5 C / 3 E, e não 4/4.
9. **Núcleo (seção 7.2)**: 8.4 sem núcleo novo (chegou a 10 na leva 1; D4-R19 a D4-R28 false); 2.2 → D1-R01 e D1-R02; 6.4 → D3-R14 e D3-R15; 6.5 → D3-R26 e D3-R27; 5.2 → D3-R38; 6.2 → D3-R49 (todos diretos, primeiros do ato de aceite na ordem do arquivo). Se um deles for reprovado, vale o k3 sobre os aceitos.

### 8.3 FICHA DA LEVA 2 — pronta para a gcb-cpp

#### 8.3.1 Objeto (edital, literal; edital/DA_itens_1_12_P1.md)
- "8.4 Valor Público, cadeia de valor público." — 10 itens novos, **D4-R19 a D4-R28** (seção 7.1); a folha vai de 10 a 20 e fecha.
- "2.2 Parecer: responsabilidade do emissor do parecer." — 12 itens novos, **D1-R01 a D1-R12**; a folha vai de 8 a 20.
- "6.4 Requisitos para a demonstração da responsabilidade do Estado." — 8 itens novos, **D3-R14 a D3-R21** (primeira parte; a segunda, 4 itens, é da leva 3).
Total: 30. Saída: saida/gcb/DA_reforco_leva2_v1.md (seção 7.5), ordem das folhas no arquivo: 8.4, 2.2, 6.4; última linha "FIM DA LEVA 02 — REFORÇO DA". Contexto de uso como na seção 3.1; exemplos hipotéticos, sem norma interna, sistema ou prática real da Câmara.

#### 8.3.2 Fontes admitidas na leva 2
- 8.4: só R59 a R81 do adendo do D4 (seção 5; URL e consulta de 20/10/2026 como lá), com os alertas B1 a B10; R82 e R83 não entram (Osborne; A8.4-27, seção 3.4). Rótulo REFERENCIAL OUTRA_OFICIAL; órgão (TCU, CGU, Casa Civil) pode ser nomeado; autor não (seção 0.2, item 4). Exigência (c): nenhum item da 8.4 usa, cita ou parafraseia o Decreto 9.203, art. 2º, II, nem o art. 4º, IV.
- 2.2: só os dispositivos da seção 4 do adendo do D1 (F1 a F5, planalto.gov.br, consulta de 20/10/2026), com os alertas P1 a P8; os arts. 10, 53 e 72 da Lei 14.133 citados pela tabela 4.4 desse adendo (reconfirmação de 20/10/2026). Nada sobre responsabilidade solidária do parecerista, classificação doutrinária de pareceres, teses de tribunal ou alcance do Decreto 9.830 ao Legislativo (P8).
- 6.4: só os dispositivos da seção 4 do adendo do D3, com os alertas A1 a A13; CC, arts. 186 e 927, pela letra, sem efeito de decisão do STF (A2); nada sobre o regime da responsabilidade do Estado, teoria do risco ou "dupla garantia" (A11; C12).
- Proibidos: memória, fonte secundária, jurisprudência, base doutrinária.

#### 8.3.3 Pontos já usados (não repetir; anti-gêmeo)
- 8.4: os da seção 3.3 (D4-27 a D4-33) e os da leva 1: A8.4-06 (D4-R15), A8.4-08 (D4-R16), A8.4-16 (D4-R17).
- 2.2: D1-53 a D1-60 (lista do adendo do D1, abertura).
- 6.4: D3-51 a D3-59 (adendo do D3, seção 3.2); na 6.3 (leva 1), CC, art. 186 (ação ou omissão; negligência e imprudência), art. 927, caput, e Lei 8.112, arts. 122, caput, e 124 — ângulo novo admitido, com "Difere de".

#### 8.3.4 Pontos de julgamento por item (ordem final dentro de cada folha; a gcb-cpp redige)
Colunas: id | ponto (código do adendo) | base | o que se julga (sentido da troca, sem redação) | formato | moldura | gab. | [TS] | aderência | abertura (CQ = "Considere que"; DC = declarativa) | difere de. Nenhum C leva [TS] (C-isca: nenhuma planejada; a 8.4 e a 6.4 já têm a sua; na 2.2, no máximo 1, com o teste da seção 8.5 refeito). Todo E leva [TS] com troca real e única; E sem troca sutil (contradição expressa) só com o teste refeito.

**Folha 8.4 — 10 itens (6 C / 4 E), D4-R19 a D4-R28**
| id | ponto | base | o que se julga | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D4-R19 | A8.4-21 | R77 (contraste R78) | processos são as ações que combinam os recursos disponíveis para produzir bens e serviços, **", e não"** os bens e serviços entregues, que são os produtos (seção 7.4.4) | PAR | N | **C** | **não** (seção 7.3) | direta | DC | D4-28 (lista dos elos; aqui o conceito de processos) |
| D4-R20 | A8.4-02 | R60 (TCU) | entre as diretrizes para a boa governança do referencial do TCU está apoiar e viabilizar a inovação para agregar valor público | APL | S — expositor — fecho **neutro** | C | não | direta | CQ | D4-32 (desempenho como geração de valor, R17) |
| D4-R21 | A8.4-10 | R66 (CGU) | no setor público em geral, observa-se a inexistência de padrão para representar a cadeia de valor (troca: inexistência → existência de padrão) | DEF | N | E | sim | direta | DC | D4-33 (adaptação de Porter, R16) |
| D4-R22 | A8.4-09 | R65 (CGU) | valor público está também associado ao grau de reconhecimento de atendimento ou satisfação do cidadão (sem citar nem parafrasear o Decreto 9.203) | DEF | N | C | não | direta | DC | D4-30 (definição do decreto) |
| D4-R23 | A8.4-25 | R81 (Casa Civil) | a avaliação das relações entre insumos, processos e produtos também investiga a eficiência operacional e a economicidade | SIT (gestor) | N — fecho **neutro** | C | não | direta | CQ | D4-31 (fluxo dos insumos ao valor) |
| D4-R24 | A8.4-05 | R62 (TCU; Porter não nomeado) | tecnologia está entre as atividades de apoio (troca: apoio → primárias) | SIT (gestor) | N — fecho acerto | E | sim | direta | CQ | D4-33 |
| D4-R25 | A8.4-20 | R76 (Casa Civil) | insumos: recursos do setor público, orçamentários ou não (troca: → exclusivamente orçamentários) | DEF | N | E | sim | direta | DC | D4-28 |
| D4-R26 | A8.4-11 | R67 (CGU) | a metodologia de gestão de processos fornece a estrutura para a elaboração da cadeia de valor, que auxilia o estabelecimento de objetivos estratégicos a partir da missão | SUJ | N | C | não | direta | DC | D4-33 |
| D4-R27 | A8.4-24 | R80 (contraste R79) | a mudança de mais longo prazo no problema é o impacto (troca: impactos → resultados) | PAR | N | E | sim | direta | DC | D4-28 (lista; aqui o conceito do componente) |
| D4-R28 | A8.4-18 | R74 (Casa Civil) | as avaliações aprofundadas inserem-se na análise dos componentes da cadeia de valor das políticas públicas ou, como diz o guia, dos componentes do modelo lógico | PAR | N | C | não | direta | DC | D4-28 |
Reserva da 8.4 (na ordem): A8.4-07, A8.4-12, A8.4-13, A8.4-03, A8.4-01 (vizinho do D4-32: só com "Difere de" explícito), A8.4-17 (B5; "atividades", não "processos"), A8.4-14 (vizinho do D4-31 e do D4-32; último). Substituto mantém formato, gabarito, moldura e abertura da linha, ou recalcula as seções 8.3.5 a 8.3.7.

**Folha 2.2 — 12 itens (6 C / 6 E), D1-R01 a D1-R12 (todos diretos)**
| id | ponto | base | o que se julga | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D1-R01 | A2.2-02 | Lei 9.784, art. 42, § 2º | o prosseguimento e a decisão com dispensa do parecer obrigatório e não vinculante não prejudicam a responsabilidade de quem se omitiu no atendimento | SUJ | N | C | não | direta | DC | D1-56 (efeito sobre o processo; aqui a responsabilidade do omisso) |
| D1-R02 | A2.2-08 | Decreto 9.830, art. 12, § 1º | erro grosseiro: manifesto, evidente e inescusável, praticado com culpa grave, com elevado grau de negligência, imprudência ou imperícia (sem troca de "culpa grave": P4) | DEF | N | C | não | direta | DC | D1-58 (LINDB; outra norma e outro elemento) |
| D1-R03 | A2.2-01 | Lei 9.784, art. 42, § 1º | responsabiliza-se quem der causa ao atraso (troca: → exclusivamente o órgão consultivo encarregado de emiti-lo) | SUJ | N | E | sim | direta | DC | D1-55 (paralisação do processo; aqui o sujeito responsabilizado) |
| D1-R04 | A2.2-10 | Decreto 9.830, art. 12, § 3º | o mero nexo de causalidade entre a conduta e o dano não implica responsabilização, salvo dolo ou erro grosseiro comprovado (troca: o nexo basta) | SIT (agente público; sem moldura) | N | E | sim | direta | CQ | D1-57 |
| D1-R05 | A2.2-03 | Lei 9.784, art. 43 (× art. 42, § 1º) | laudo técnico não entregue no prazo: o órgão de instrução solicita laudo a outro órgão equivalente (troca: o processo não terá seguimento até a apresentação) | PAR | N | E | sim | direta | DC | D1-55 (parecer vinculante; aqui laudo técnico) |
| D1-R06 | A2.2-17 | Lei 14.133, art. 10, caput | quem agiu com estrita observância de parecer jurídico do art. 53, § 1º, e precisa defender-se: a advocacia pública promove a representação, a critério do agente | SIT | N | C | não | direta | CQ | — |
| D1-R07 | A2.2-18 | Lei 14.133, art. 10, § 1º, II | a representação não se aplica quando provas de atos ilícitos **dolosos** constarem dos autos (troca: dolosos → culposos) | PAR | N | E | sim | direta | DC | D1-R06 (caput; aqui a exceção) |
| D1-R08 | A2.2-13 | Decreto 9.830, art. 12, § 6º, primeira parte | a responsabilização pela opinião técnica não se estende de forma automática ao decisor que a adotou como fundamento de decidir | SUJ | N | C | não | direta | DC | D1-57 (responsabilidade pessoal do agente; aqui emissor × decisor) |
| D1-R09 | A2.2-12 | Decreto 9.830, art. 12, § 5º | o montante do dano ao erário, ainda que expressivo, não pode, por si só, caracterizar erro grosseiro ou dolo | SIT (agente público; sem moldura) | N | C | não | direta | CQ | — |
| D1-R10 | A2.2-16 | Decreto 9.830, art. 17 | o art. 12 não afasta sanções disciplinares, inclusive por ação ou omissão culposas de natureza leve (troca: afasta) | PAR | N | E | sim | direta | DC | D1-58 (responsabilidade pela opinião; aqui sanção disciplinar) |
| D1-R11 | A2.2-20 | Lei 14.133, art. 53, caput | ao fim da fase preparatória, o órgão de assessoramento jurídico realiza controle **prévio** de legalidade (troca: prévio → posterior à contratação) | SIT | N | E | sim | direta | CQ | — |
| D1-R12 | A2.2-23 | Lei 14.133, art. 72, III | a contratação direta é instruída com parecer jurídico e pareceres técnicos, se for o caso | SIT | N | C | não | direta | CQ | — |
Decreto 9.830: D1-R02, R04, R08, R09, R10 (5, teto); Lei 14.133: D1-R06, R07, R11, R12 (4, teto). Reserva (na ordem; Decreto só no lugar de item do Decreto e Lei 14.133 só no lugar de item da Lei 14.133): A2.2-09, A2.2-11, A2.2-14 (nunca com o D1-R08), A2.2-15; A2.2-19, A2.2-21, A2.2-22; A2.2-05 (só E de troca de sujeito; gêmeo do D1-57 na forma C); A2.2-06 (vizinho do D1-60).

**Folha 6.4 — 8 itens (5 C / 3 E), D3-R14 a D3-R21 (primeira parte)**
| id | ponto | base | o que se julga | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D3-R14 | A6.4-17 | Lei 8.987, art. 25, caput | a concessionária responde por todos os prejuízos causados ao poder concedente, aos usuários ou a terceiros | SUJ | N | C | não | direta | DC | D3-59 (CC, art. 43) |
| D3-R15 | A6.4-05 | CC, art. 186 | há ato ilícito ainda que o dano seja exclusivamente moral | DEF | N | C | não | direta | DC | D3-R02 e D3-R05 (6.3: ação ou omissão; negligência) |
| D3-R16 | A6.4-01 | CF, art. 5º, V | indenização por dano material, moral ou à imagem (troca: excluído o dano à imagem) | APL | S — órgão/servidor do Poder Legislativo da União | E | sim | direta | CQ | D3-58 (elementos do § 6º) |
| D3-R17 | A6.4-06 | CC, art. 927, parágrafo único | obrigação de reparar, independentemente de culpa, quando a atividade normalmente desenvolvida pelo autor do dano implicar, por sua natureza, risco para os direitos de outrem (sem pôr o Estado na cena nem afirmar o regime dele: A2, A11) | SIT | N | C | não | direta | CQ | D3-55 |
| D3-R18 | A6.4-13 | Lei 8.112, art. 122, § 3º | a obrigação de reparar estende-se aos sucessores até o limite do valor da herança recebida (troca: sem limite) | APL | S — órgão/servidor do Poder Legislativo da União | E | sim | parcial | CQ | — |
| D3-R19 | A6.4-08 | CC, art. 944, caput | a indenização mede-se pela extensão do dano (troca: pela gravidade da culpa do agente) | APL | S — órgão/servidor do Poder Legislativo da União | E | sim | direta | CQ | D3-56 |
| D3-R20 | A6.4-12 | Lei 8.112, art. 122, § 2º | dano causado a terceiros: o servidor responde perante a Fazenda Pública, em ação regressiva (C com moldura, par R3 de um E além da cota) | APL | S — órgão/servidor do Poder Legislativo da União | C | não | parcial | CQ | D3-54 (CF: dolo ou culpa no regresso) |
| D3-R21 | A6.4-02 | CF, art. 5º, X | violação da intimidade, da vida privada, da honra ou da imagem: indenização pelo dano material ou moral | DEF | N | C | não | direta | DC | D3-R16 (inciso V; outro inciso) |
Moldura com a Lei 8.112 (D3-R18, D3-R20): a cena nomeia "servidor público civil da União lotado em órgão do Poder Legislativo da União" e a lei; nenhum regime próprio da Câmara. Reserva da 6.4 (só indiretos; nenhum direto sobra, seção 8.2, item 2): A6.4-18, A6.4-10 (A8), A6.4-07 (A3; último).

#### 8.3.5 Formatos ao fim da leva 2 (folha acumulada; teto 6 em 20)
| folha | DEF | SUJ | SIT | NUM | PAR | APL | total |
|---|---|---|---|---|---|---|---|
| 8.4 (canônicos 2/0/2/0/2/1 + leva 1 0/0/0/0/0/3 + leva 2 3/1/2/0/3/1) | 5 | 1 | 4 | 0 | 5 | 5 | 20 |
| 2.2 (canônicos 4/0/0/1/3/0 + 1/3/5/0/3/0) | 5 | 3 | 5 | 1 | **6** | 0 | 20 |
| 6.4 (canônicos 3/0/2/0/2/1 + 2/1/1/0/0/4) | 5 | 1 | 3 | 0 | 2 | 5 | 16 (leva 3 completa: + 0/2/0/2/0/0) |
PAR da 2.2 fica no teto: a gcb-cpp não declara outro PAR na folha; reclassificação pela QA obriga a mudar a construção de outro item. Formatos da leva 2: DEF 6, SUJ 5, SIT 8, NUM 0, PAR 6, APL 5.

#### 8.3.6 Gabarito, moldura, aderência e conjuntos ao fim da leva 2
- Leva: **17 C / 13 E (56,7%)**, faixa 12–18. Folhas: 8.4 10/10 (4/6 + 6/4); 2.2 10/10 (4/4 + 6/6); 6.4 8/8 parcial (3/5 + 5/3; fecha 10/10 com 2/2 na leva 3).
- Moldura nova (D-MOLDURA-CE; cota e R3): **2 C** (D4-R20; D3-R20) e **3 E** (D3-R16, D3-R18, D3-R19). DA: 46/18 → **48/21 (69,6%)**, igual à seção 2.2; E com moldura novos acumulados: 12 (meta da D-MOLDURA-CE prevista na leva 5, sem mudança). Por folha: 8.4 2 C / 3 E (40%), 5 com moldura; 6.4 2/3 (40%), 5; 2.2 0. Cota da T-122: 8.4 e 6.4 cumpridas (1 cada; 3 E entregues em cada uma); o C da 8.4 é par do E além da cota da leva 1 (R3).
- Aderência: 28 diretos / 2 parciais (D3-R18, D3-R20). Piso de 10 diretos: 8.4 20; 2.2 20; 6.4 14 (de 16).
- [TS]: 13 (todos E; nenhum C-isca). VOLÁTIL: 0. REVERIFICAR: 0 (adendos: nenhum dispositivo de 2025 ou 2026).
- Conjuntos do D4 (regra 11; seção 7.4.1): K1 moldura 13/6 → **14/6** (70,0%; equilíbrio nas levas 8 e 9, como na seção 3.6); K2 fecho de acerto 7/6 → **7/7 (50,0%)** (só D4-R24); K3 "pós-NPM" 5/4, sem item novo (nenhum item da 8.4 usa a expressão); K4 "Considere que" 23/17 → **25/18 (58,1%)** (D4-R20 C, D4-R23 C, D4-R24 E; **nenhum outro item do D4 da leva abre com "Considere que"**: K4 fica a 1,9 ponto do teto de 60%, e a folga, de 2 C, fica para as levas 8 e 9); fecho neutro 0/3 → **2/3 (40,0%)** (D4-R20 e D4-R23; nenhum E com fecho neutro); contraste ", e não" 0/2 → **1/2** (D4-R19).
- Conjunto do D3 (moldura): 7/4 → **8/7 (53,3%)**.
- Abertura × gabarito na leva (seção 7.4.2): "Considere que" 7 C / 6 E (53,8% de C ≥ 40%); declarativos 10 C / 7 E (41,2% de E ≥ 40%). Fórmula "Nessa situação, nos termos d…" (seção 7.4.3): na 6.4, no máximo 2 dos 5 itens com "Considere que"; na 2.2, contada e informada.
- SUJ (seção 7.4.4): sujeito trocado só no D1-R03 (órgão consultivo, que o próprio art. 42 menciona); nos SUJ em C, o sujeito é o da letra.

#### 8.3.7 Sequência (seção 7.3; plano conferido por script antes do despacho)
| escopo | gabarito | [TS] | resultado |
|---|---|---|---|
| 8.4, leva | CCECCEECEC | nnTnnTTnTn | passa |
| 8.4 acumulada (D4-27 a D4-33, D4-R15 a R17, leva) | CEECECCEEE·CCECCEECEC | nTTnTTnTTT·nnTnnTTnTn | gabarito passa; [TS] só o bloco aceito das posições 1 a 9 (seção 7.3); D4-R19 = C sem [TS] fecha a corrida E E E |
| 2.2, leva | CCEEECECCEEC | nnTTTnTnnTTn | passa |
| 2.2 acumulada | CECECEEC·CCEEECECCEEC | nTnTnTTn·nnTTTnTnnTTn | só o legado das posições 1 a 6 (seção 8.2, item 7) |
| 6.4, leva | CCECEECC | nnTnTTnn | passa |
| 6.4 acumulada (16) | CEECEECE·CCECEECC | nTnTTTnT·nnTnTTnn | gabarito: só o legado das posições 1 a 8 (o D3-R14, C, fecha o bloco); [TS] passa |
| leva 2 inteira (8.4, 2.2, 6.4) | CCECCEECEC·CCEEECECCEEC·CCECEECC | idem com T nos E | passa |
A gcb-cpp mantém esta ordem e esta numeração. Troca de posição só se o teste refeito (folha, folha acumulada, leva) passar e a seção 4 do arquivo registrar; troca de ponto, como na seção 3.7.

#### 8.3.8 Amostra da gbq-estilo (10%; seção 5 e seção 7.6, como lida pela D-T116-LEVA1-ACEITE)
3 itens (10%), designados antes da produção: **D4-R20** (C com moldura de expositor e fecho neutro: pista K4 e fecho); **D1-R04** (E, SIT do Decreto 9.830 sem moldura, "Considere que"; lote D1); **D3-R18** (E com moldura do Legislativo, aderência parcial, Lei 8.112). Cobre: E com moldura, os três lotes, um C, um parcial. A auditoria corre sobre a v1, em paralelo ao R1 (recomendação da presidência na D-T116-LEVA1-ACEITE); os AJ de estilo vão com os AJ do R1 para a v2 e são conferidos no R2. Texto de estilo sobre item já aprovado no R2 só entra em aceite com conferência da gcb-cqfp. Saída: saida/banco/estilo_DA_reforco_leva2.md.

#### 8.3.9 Despacho à gcb-cpp (leva 2)
- Executor: gcb-cpp (sonnet), uma instância. Objeto: leva 2, conforme esta seção 8.3, as seções 1 e 7 e os anexos abaixo. Saída: saida/gcb/DA_reforco_leva2_v1.md, no formato da regra 14 (nomes da seção 7.5), linha 1 `# DA_reforco_leva2_v1.md — T-116 — <data ISO> — gerado por gcb-cpp`.
- Anexos (lista exaustiva): esta ficha; saida/gcb/D4_anexo_N_adendo_2026-10-20.md (seções 3.2, 5 e 6.2); saida/gcb/D1_anexo_N_adendo_2026-10-20.md (seções 3.1, 4 e 5.2); saida/gcb/D3_anexo_N_adendo_2026-10-20.md (seções 3.2, 4 e 5.2); saida/gcb/D4_anexo_N_mapa_normativo.md (seção 5, só contraste) e saida/gcb/D4_ficha_lote.md (seções 3.2, 3.3 e 6); regras/estilo_banca.md; modelo de bloco: saida/gcb/DA_reforco_leva1_v2.md (blocos aprovados) e saida/gcb/D4_v2_1.md, seção 5.2; canônicos D1_v2.md (D1-53 a D1-60), D3_v2_1.md e D4_v2_1.md só para os pontos já usados; cópias em saida/gcb/normativo_cache/.
- A seção 4 do arquivo traz, por script: as contagens da regra 14; abertura × gabarito e fecho × gabarito por lote (canônicos, leva, acumulado; seção 7.4.6); a contagem da fórmula "Nessa situação, nos termos d…"; o teste da seção 8.3.7 refeito; e a moldura acumulada (DA, D3, K1 a K4, fecho neutro, ", e não").
- Dúvida de conteúdo vai ao bloco à GCB, sem consulta a terceiros. Nada vai à plataforma nem à candidata. Sem commit.

#### 8.3.10 Errata AJ-E1 do D3-R13 — conferência da gcb-cqfp no R1 da leva 2 (D-T116-LEVA1-ACEITE, parte (II))
O parecer R1 da leva 2 (saida/gcb/QA_DA_reforco_leva2_R1_<data>_gcb-cqfp.md) traz uma **seção própria**, "Errata AJ-E1 (D3-R13, leva 1)", separada do veredito da leva 2, em que a gcb-cqfp confere a AJ-E1 como errata textual de item canônico:
- texto: o de saida/banco/estilo_DA_reforco_leva1.md (2d50c4cb…8878), linha da AJ-E1, idêntico ao da reconciliação da leva 1, seção 4.4 — antes: «são obrigados a fornecer serviços adequados, eficientes, seguros e, quanto aos essenciais, contínuos os órgãos públicos, por si ou suas empresas, concessionárias, permissionárias ou sob qualquer outra forma de empreendimento.» — depois: «os órgãos públicos, por si ou suas empresas, concessionárias, permissionárias ou sob qualquer outra forma de empreendimento, são obrigados a fornecer serviços adequados, eficientes, seguros e, quanto aos essenciais, contínuos.»;
- conferências: (1) o "antes" ocorre exatamente 1 vez na seção 1 de saida/gcb/DA_reforco_leva1_v2.md (2c431529…a4f04) e o "depois", 0 vez; (2) o "depois" é literal ao CDC, art. 22, caput, na cópia saida/gcb/normativo_cache/Lei_8078_1990_CDC_compilada_2026-10-20.txt (575478df…4526); (3) mesmas palavras, só a ordem muda; (4) gabarito C, ponto A6.3-12, mecanismo C2, formato SUJ, aderência parcial e demais campos do bloco inalterados; (5) o enunciado resultante, lido inteiro, não muda o sentido nem cria pista;
- veredito próprio: **CONFERIDO** ou **NÃO CONFERIDO** (com motivo). Não é terceira rodada da leva 1 nem QA aberto que impeça a leva 3; não altera o arquivo da leva 1.
- Destino: a GCB leva a errata ao gatilho A seguinte (o da leva 2), como item separado; aceita, a GBQ a aplica na T-123 por substituição exata, com aborto se o "antes" não ocorrer exatamente 1 vez na seção 1, registro por id no registro de alterações da v1.14 e conferência da gbq-cqe na fidelidade. Sem esse aceite até a geração final da v1.14, o D3-R13 entra como aprovado no R2.

### 8.4 FICHA DA LEVA 3 — despachável depois do fecho do QA da leva 2

#### 8.4.1 Objeto (edital, literal)
- "6.4 Requisitos para a demonstração da responsabilidade do Estado." — 4 itens, **D3-R22 a D3-R25** (segunda parte; a folha vai a 20).
- "6.5 Causas excludentes e atenuantes da responsabilidade do Estado." — 12 itens, **D3-R26 a D3-R37**; de 8 a 20.
- "5.2 Uso e abuso do poder." — 11 itens, **D3-R38 a D3-R48**; de 9 a 20.
- "6.2 Responsabilidade por ato comissivo do Estado." — 3 itens, **D3-R49 a D3-R51** (primeira parte; a segunda, 8 itens, D3-R52 a D3-R59, é da leva 4).
Total: 30. Saída: saida/gcb/DA_reforco_leva3_v1.md; ordem no arquivo: 6.4, 6.5, 5.2, 6.2; última linha "FIM DA LEVA 03 — REFORÇO DA". Se a leva 2 terminar com substituto no D3, as faixas da leva 3 andam pelo próximo id livre (regra 12) e a reconciliação da leva 2 as republica.

#### 8.4.2 Fontes admitidas na leva 3
- 6.4 e 6.5: seção 4 do adendo do D3, alertas A1 a A13. 5.2 e 6.2: "Adendo 2" do mesmo arquivo (A2.4; alertas C1 a C12), com a CF, art. 5º, LXXV, reconfirmada em A2.4.1. Lei 12.016: só art. 1º, caput e § 1º (seção 8.2, item 3). Decreto 9.830, art. 14: só com o nome do Decreto e o alcance, sem moldura (C6). Lei 9.494, art. 1º-C: sem termo inicial (C8). Lei 13.869: nomeia a lei e o sujeito; nunca a apresenta como definição do abuso de poder administrativo (C1); nada sobre imunidade, tipos penais ou norma interna da Câmara (C4).
- Continuam [SEM FONTE — não afirmar]: A11 e C12 (regime da omissão, risco integral, fortuito × força maior, ônus das excludentes no § 6º, "excesso" e "desvio" como espécies, dupla garantia, responsabilidade por atos legislativos ou jurisdicionais em geral).

#### 8.4.3 Pontos já usados (não repetir)
- 6.4: os da seção 8.3.3 e os da leva 2 (A6.4-01, 02, 05, 06, 08, 12, 13, 17).
- 6.5: D3-61 a D3-70 (adendo do D3, seção 3.3).
- 5.2: D3-11 a D3-20 (A2.3.1, abertura); fora por gêmeo os do alerta C10.
- 6.2: D3-32 a D3-40 e D3-81 (A2.3.2, abertura); CC, arts. 186 e 927 (6.3 e 6.4) e Lei 8.112, art. 122 (6.3 e 6.4) não voltam.

#### 8.4.4 Pontos de julgamento por item (ordem final; colunas da seção 8.3.4)

**Folha 6.4 — 4 itens (2 C / 2 E), D3-R22 a D3-R25 (todos de aderência parcial; seção 8.2, item 2)**
| id | ponto | base | o que se julga | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D3-R22 | A6.4-15 | Decreto 20.910, art. 1º | todo direito ou ação contra a Fazenda federal, estadual ou municipal prescreve em cinco anos contados da data do ato ou fato (sem prestadoras privadas: A10) | NUM | N | C | não | parcial | DC | — |
| D3-R23 | A6.4-09 | Lei 4.619, art. 1º, parágrafo único | funcionário, para a lei, é qualquer pessoa investida em função pública, seja qual for a forma de investidura ou a natureza da função (troca: só o ocupante de cargo efetivo) | SUJ | N | E | sim | parcial | DC | D3-52 ("nessa qualidade") |
| D3-R24 | A6.4-11 | Lei 4.619, art. 2º | ação regressiva: prazo de sessenta dias do trânsito em julgado da condenação da Fazenda (troca de número; nunca "cinco anos") | NUM | N | E | sim | parcial | DC | — |
| D3-R25 | A6.4-16 | CDC, art. 14, caput | o fornecedor de serviços responde, independentemente da existência de culpa, pelos danos por defeitos na prestação dos serviços (A7) | SUJ | N | C | não | parcial | DC | — |
Lei 4.619 só "nos termos da Lei nº 4.619/1965", sem atualizar órgão ou carreira (A8). Se a gcb-cqfp recusar a pertinência de indiretos da 6.4 sem reserva para repor (A6.4-18, A6.4-10, A6.4-07), a folha fica abaixo de 20, com registro (seção 2.1).

**Folha 6.5 — 12 itens (7 C / 5 E), D3-R26 a D3-R37**
| id | ponto | base | o que se julga | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D3-R26 | A6.5-01 | CC, art. 393, parágrafo único | o caso fortuito ou de força maior verifica-se no fato necessário cujos efeitos não era possível evitar ou impedir (sem distinguir um do outro: A3, A11) | DEF | N | C | não | direta | DC | D3-63 (força maior como excludente, base doutrinária) |
| D3-R27 | A6.5-08 | CC, art. 945 | vítima que concorreu culposamente: indenização fixada pela gravidade da sua culpa em confronto com a do autor (troca: sem considerar a culpa da vítima) | APL | S — órgão/servidor do Poder Legislativo da União | E | sim | direta | CQ | D3-61 (atenua × exclui; aqui o critério de fixação) |
| D3-R28 | A6.5-12 | Lei 8.987, art. 25, caput | a fiscalização exercida pelo órgão competente não exclui nem atenua a responsabilidade da concessionária | SIT | N | C | não | direta | CQ | D3-R14 (6.4: mesmo artigo, outro elemento) |
| D3-R29 | A6.5-07 | CC, art. 930 | perigo por culpa de terceiro: o autor do dano tem ação regressiva contra o terceiro | SUJ | N | C | não | direta | DC | D3-70 (regresso contra o servidor) |
| D3-R30 | A6.5-17 | CC, art. 935 | responsabilidade civil independente da criminal, mas não se questiona mais a existência do fato ou a autoria decididas no juízo criminal (troca: podem ser rediscutidas no cível) | PAR | N | E | sim | direta | DC | — |
| D3-R31 | A6.5-19 | Lei 8.112, art. 125 | sanções civis, penais e administrativas podem cumular-se e são independentes (troca: a administrativa afasta a civil) | APL | S — órgão/servidor do Poder Legislativo da União | E | sim | parcial | CQ | — |
| D3-R32 | A6.5-14 | CF, art. 21, XXIII, d | a responsabilidade civil por danos nucleares independe da existência de culpa (sem "risco integral" e sem excludentes: A6) | DEF | N | C | não | direta | DC | D3-64 |
| D3-R33 | A6.5-05 | CC, art. 188, parágrafo único | no caso do inciso II, o ato só é legítimo quando as circunstâncias o tornarem absolutamente necessário, sem exceder o indispensável (C com moldura, par R3) | APL | S — órgão/servidor do Poder Legislativo da União | C | não | direta | CQ | — |
| D3-R34 | A6.5-09 | CC, art. 944, parágrafo único | excessiva desproporção entre a gravidade da culpa e o dano: o juiz pode reduzir, equitativamente, a indenização | SUJ | N | C | não | direta | DC | D3-67; D3-R19 (6.4, caput) |
| D3-R35 | A6.5-06 | CC, art. 929 | o lesado não culpado do perigo tem direito à indenização, mesmo no caso do art. 188, II (troca: só se provar culpa do autor do dano; sem cenário que enumere todos os elementos para negar o fecho: seção 7.4.5) | APL | S — órgão/servidor do Poder Legislativo da União | E | sim | direta | CQ | D3-R33 |
| D3-R36 | A6.5-20 | Lei 4.619, art. 5º | a cessação do exercício da função pública não exclui o funcionário da responsabilidade perante a Fazenda (A8) | SIT | N | C | não | parcial | CQ | D3-66 |
| D3-R37 | A6.5-11 | CDC, art. 14, § 3º, II | excludente do fornecedor de serviços: culpa **exclusiva** do consumidor ou de terceiro (troca: exclusiva → concorrente) | PAR | N | E | sim | parcial | DC | D3-61 |
Reserva da 6.5 (na ordem): A6.5-03, A6.5-04 (art. 188; não junto do D3-R33 e do D3-R35), A6.5-10 (CDC, ônus do fornecedor), A6.5-02 (A3), A6.5-15 e A6.5-16 (Lei 6.453; A6; nunca no mesmo simulado que o D3-64).

**Folha 5.2 — 11 itens (6 C / 5 E), D3-R38 a D3-R48**
| id | ponto | base | o que se julga | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D3-R38 | A5.2-03 | CF, art. 5º, LXVIII | habeas corpus por ilegalidade **ou abuso de poder** (troca: só por ilegalidade) | DEF | N | E | sim | direta | DC | D3-11 |
| D3-R39 | A5.2-04 | CF, art. 5º, LXIX | mandado de segurança quando o responsável for autoridade pública ou agente de pessoa jurídica no exercício de atribuições do Poder Público | SUJ | N | C | não | direta | DC | D3-13 |
| D3-R40 | A5.2-02 | CF, art. 5º, XXXIV, caput e a | direito de petição contra ilegalidade ou abuso de poder, independentemente do pagamento de taxas (troca: mediante taxas) | SIT (particular; sem moldura) | N | E | sim | direta | CQ | — |
| D3-R41 | A5.2-05 | CF, art. 5º, LXIX | o mandado de segurança protege direito líquido e certo não amparado por habeas corpus ou habeas data | PAR | N | C | não | direta | DC | D3-12 |
| D3-R42 | A5.2-12 | Lei 8.112, art. 116, XII | é dever do servidor representar contra ilegalidade, omissão ou abuso de poder | SIT (servidor público federal; sem moldura) | N | C | não | parcial | CQ | D3-16 (poder-dever de agir) |
| D3-R43 | A5.2-06 | Lei 12.016, art. 1º, caput | mandado de segurança também com justo receio de violação (troca: só violação consumada) | DEF | N | E | sim | direta | DC | — |
| D3-R44 | A5.2-18 | Lei 13.869, art. 2º, caput e II | rol de sujeitos ativos "compreendendo, mas não se limitando a", com membros do Poder Legislativo (troca: rol taxativo) | APL | S — comissão/sessão da Câmara dos Deputados (cota da 5.2) | E | sim | parcial | CQ | D3-18 |
| D3-R45 | A5.2-07 | Lei 12.016, art. 1º, caput | a autoridade pode ser de qualquer categoria e exercer quaisquer funções | SUJ | N | C | não | direta | DC | D3-R43 |
| D3-R46 | A5.2-17 | Lei 13.869, art. 1º, § 2º | a divergência na interpretação de lei ou na avaliação de fatos e provas não configura abuso de autoridade | SIT (agente público; sem moldura) | N | C | não | parcial | CQ | — |
| D3-R47 | A5.2-08 | Lei 12.016, art. 1º, § 1º | dirigentes de pessoas jurídicas ou pessoas naturais no exercício de atribuições do poder público equiparam-se às autoridades somente no que disser respeito a essas atribuições | SUJ | N | C | não | direta | DC | — |
| D3-R48 | A5.2-13 | Lei 8.112, art. 116, parágrafo único | a representação é apreciada pela autoridade superior àquela contra a qual é formulada (troca: pela própria autoridade representada) | SUJ | N | E | sim | parcial | DC | D3-R42 |
Reserva da 5.2 (na ordem): A5.2-16, A5.2-19, A5.2-20, A5.2-10, A5.2-14, A5.2-01 (nunca com o D3-R40), A5.2-15 (C1, C5); A5.2-21 e A5.2-22 só como último recurso (C3).

**Folha 6.2 — 3 itens (1 C / 2 E), D3-R49 a D3-R51 (primeira parte)**
| id | ponto | base | o que se julga | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D3-R49 | A6.2-02 | Lei 9.494, art. 1º-C | o prazo de cinco anos alcança também os danos causados por agentes de pessoas jurídicas de direito privado prestadoras de serviços públicos (troca: só de direito público; sem termo inicial: C8) | SUJ | N | E | sim | direta | DC | D3-35 (sujeitos do § 6º) |
| D3-R50 | A6.2-06 | CF, art. 5º, LXXV | o Estado indenizará também quem ficar preso além do tempo fixado na sentença (troca: a indenização depende de erro judiciário) | SIT | N | E | sim | direta | CQ | — |
| D3-R51 | A6.2-04 | Decreto 9.830, art. 14 | no âmbito do Poder Executivo federal, o regresso observa a proporcionalidade e a razoabilidade | DEF | N | C | não | direta | DC | D3-32 e D3-36 (C6) |
Para a leva 4 (8 itens, 5 C / 3 E; seção 8.2, item 8) ficam: A6.2-01, A6.2-03, A6.2-05 (nunca no mesmo simulado que o D3-R50) e os indiretos A6.2-07 a A6.2-15 (C9, C11). Formatos já usados na 6.2 depois da leva 3: DEF 4, PAR 3, SIT 4, SUJ 1 (de 12).

#### 8.4.5 Formatos ao fim da leva 3 (folha acumulada; teto 6 em 20)
| folha | DEF | SUJ | SIT | NUM | PAR | APL | total |
|---|---|---|---|---|---|---|---|
| 6.4 (16 da leva 2 + 0/2/0/2/0/0) | 5 | 3 | 3 | 2 | 2 | 5 | 20 |
| 6.5 (canônicos 3/0/2/0/2/1 + 2/2/2/0/2/4) | 5 | 2 | 4 | 0 | 4 | 5 | 20 |
| 5.2 (canônicos 3/1/2/0/2/1 + 2/4/3/0/1/1) | 5 | 5 | 5 | 0 | 3 | 2 | 20 |
| 6.2 (canônicos 3/0/3/0/3/0 + 1/1/1/0/0/0) | 4 | 1 | 4 | 0 | 3 | 0 | 12 |
Máximo 25% em toda folha fechada. Formatos da leva 3: DEF 5, SUJ 9, SIT 6, NUM 2, PAR 3, APL 5.

#### 8.4.6 Gabarito, moldura, aderência e conjuntos ao fim da leva 3
- Leva: **16 C / 14 E (53,3%)**, faixa 12–18. Folhas: 6.4 10/10; 6.5 10/10 (3/5 + 7/5); 5.2 10/10 (4/5 + 6/5); 6.2 5/7 parcial (4/5 + 1/2; fecha 10/10 com 5/3 na leva 4).
- Moldura nova: **1 C** (D3-R33) e **4 E** (D3-R27, D3-R31, D3-R35; D3-R44). DA: 48/21 → **49/25 (66,2%)**, igual à seção 2.2; E com moldura novos acumulados: 16. Por folha: 6.5 2 C / 3 E (40%), 5 com moldura; 5.2 1/1 (50%), 2; 6.4 sem item novo com moldura (fica 2/3); 6.2 0. Cotas da T-122: 6.5 (1) e 5.2 (1) cumpridas; tipo da cota: órgão/servidor do Poder Legislativo da União na 6.5; comissão/sessão da Câmara dos Deputados na 5.2 (R2).
- Conjunto do D3 (moldura): 8/7 → **9/11 (45,0%)**; no fim do plano 9/13 (seção 2.2), sem C com moldura além do previsto (seção 6, risco 3).
- Aderência: 19 diretos / 11 parciais (D3-R22 a R25, R31, R36, R37, R42, R44, R46, R48). Piso de 10 diretos: 6.4 14; 6.5 17; 5.2 16; 6.2 12 (de 12).
- [TS]: 14 (todos E; nenhum C-isca; na 6.5, que não tem C-isca, no máximo 1, com o teste refeito). VOLÁTIL 0; REVERIFICAR 0.
- Abertura × gabarito (seção 7.4.2): "Considere que" 5 C / 6 E (45,5% de C); declarativos 11 C / 8 E (42,1% de E). Fórmula "Nessa situação, nos termos d…" (7.4.3): no máximo 5 dos 11 itens com "Considere que" da leva.

#### 8.4.7 Sequência (plano conferido por script)
| escopo | gabarito | [TS] | resultado |
|---|---|---|---|
| 6.4, leva / acumulada (20) | CEEC / CEECEECE·CCECEECC·CEEC | nTTn / nTnTTTnT·nnTnTTnn·nTTn | passa; acumulada: só o legado 1 a 8 do gabarito |
| 6.5, leva / acumulada | CECCEECCCECE / EECECEEC·CECCEECCCECE | nTnnTTnnnTnT / TTnTnTTn·nTnnTTnnnTnT | passa; acumulada: só o legado 2 a 6 (gabarito e [TS]), já fechado dentro dos canônicos (D3-68, E, depois de D3-67) |
| 5.2, leva / acumulada | ECECCEECCCE / ECEECCECE·ECECCEECCCE | TnTnnTTnnnT / TnTTnnnTT·TnTnnTTnnnT | passa |
| 6.2, leva / acumulada (12) | EEC / ECEECCEEC·EEC | TTn / TnTTTnnTn·TTn | passa; acumulada: só o legado 2 a 9 do gabarito; o D3-R49, E, fecha o bloco |
| leva 3 inteira (6.4, 6.5, 5.2, 6.2) | CEEC·CECCEECCCECE·ECECCEECCCE·EEC | idem com T nos E | passa |
Mesma regra de troca de posição da seção 8.3.7.

#### 8.4.8 Amostra da gbq-estilo (leva 3)
4 itens (13,3%): **D3-R33** (C com moldura, par R3, art. 188); **D3-R44** (E com moldura de comissão da Câmara, cota da 5.2, parcial); **D3-R50** (E, SIT, CF, art. 5º, LXXV); **D3-R24** (E, NUM, Lei 4.619, parcial). Mesmo rito da seção 8.3.8. Saída: saida/banco/estilo_DA_reforco_leva3.md.

#### 8.4.9 Despacho à gcb-cpp (leva 3)
Como na seção 8.3.9, com: saída saida/gcb/DA_reforco_leva3_v1.md; anexos: esta ficha; saida/gcb/D3_anexo_N_adendo_2026-10-20.md (seções 3.2, 3.3, 4 e 5.2, e o "Adendo 2", A2.3 a A2.5); D3_v2_1.md (pontos já usados); o arquivo final da leva 2 (pontos da 6.4); regras/estilo_banca.md; modelo de bloco da leva 1; cópias em saida/gcb/normativo_cache/. A ficha da leva 3 é confirmada na reconciliação da leva 2 (ids, se houver substituto; pontos da 6.4 aceitos); sem essa confirmação, não há despacho.

### 8.5 Notas de simulado das levas 2 e 3 (destino: T-119 e T-123; continuam a lista (a) a (j) da reconciliação da leva 1)
| # | itens | motivo |
|---|---|---|
| (k) | D3-R16 × D3-R21 | CF, art. 5º, V e X: mesmo binômio dano material/moral; o C do inciso X confunde o E do inciso V |
| (l) | D3-R19 × D3-R34 | CC, art. 944, caput e parágrafo único |
| (m) | D3-R18 × D3-R20 | Lei 8.112, art. 122, §§ 2º e 3º; mesma moldura e mesma cena |
| (n) | D3-R22 × D3-R49 | dois prazos de cinco anos (Decreto 20.910 × Lei 9.494; C8) |
| (o) | D3-R51 × D3-32 e D3-36 | Decreto 9.830, art. 14 × CF, art. 37, § 6º (C6) |
| (p) | D3-R37 × D3-61 | culpa exclusiva (CDC) × culpa concorrente |
| (q) | D3-R43 × D3-R45 | Lei 12.016, art. 1º, caput |
| (r) | D3-R33 × D3-R35 (e D3-R29) | CC, arts. 188, II, 929 e 930: mesma cena de remoção de perigo |
| (s) | D1-R01 × D1-56; D1-R03 e D1-R05 × D1-55; D1-R02 × D1-58 | mesmo dispositivo ou mesmo conceito (P1, P4) |
| (t) | D3-R14 × D3-R28 | Lei 8.987, art. 25, caput |
| (u) | D4-R19, D4-R25 e D4-R27 × D4-28 | componentes do modelo lógico (Casa Civil) |
| (v) | parciais: D3-R18, D3-R20, D3-R22 a D3-R25, D3-R31, D3-R36, D3-R37, D3-R42, D3-R44, D3-R46, D3-R48 | só simulado diagnóstico (D-ADERENCIA) |
| (w) | as levas 2 e 3 inteiras (ou só itens de reforço) | não formam simulado isolado; entram misturadas por folha com os canônicos (nota (i)) |
| (x) | os 10 itens com moldura das duas levas (D4-R20; D3-R16, R18, R19, R20; D3-R27, R31, R33, R35, R44) | contam para o teto de 50% de C com moldura por simulado (D-MOLDURA-CE (c)) |

### 8.6 Riscos e registros
1. Lastro: nenhuma folha das levas 2 e 3 fica sem fonte. Folhas que dependem de indiretos: 6.4 (6 parciais) e 5.2 (4); se a gcb-cqfp recusar pertinência sem reserva, a folha fica abaixo de 20, com registro (seção 2.1). A 6.2 (leva 4) dependerá de ao menos 5 indiretos do regime civil comum (A2.3.2).
2. Moldura: margem da leva 5 (seção 2.2) inalterada: 2 C + 3 E na leva 2 e 1 C + 4 E na leva 3, como no plano. E com moldura reprovado é reposto na v2 da mesma leva (ponto da reserva da folha, mesmo tipo de moldura).
3. K4 do D4 fica em 58,1% depois da leva 2 (folga de 2 C até 60%): nas levas 8 e 9, item do D4 com "Considere que" é preferencialmente E até o conjunto voltar ao centro da faixa.
4. Quatro desvios de legado na sequência dos canônicos (seção 8.2, item 7): registrados, não corrigidos, a conferir na reconciliação de cada leva junto com o bloco aceito da 8.4.
5. Nenhuma tarefa nova (D-COMPLEMENTOS); nenhum gatilho em PARA_PRESIDENCIA.md por esta seção (função própria da Gerência titular). A errata AJ-E1 vai ao gatilho A da leva 2 como item separado (seção 8.3.10).

## 9. Adendo após a leva 2 (gcb-gerencia, 20/10/2026, ciclo s15c4)
Fonte: reconciliação saida/gcb/DA_reforco_leva2_reconciliacao_2026-10-20.md (seções 4 e 5), pareceres R1 e R2 da gcb-cqfp da leva 2 e auditoria de estilo saida/banco/estilo_DA_reforco_leva2.md (seções 5 a 7). Só acréscimo antes da última linha; o texto acima fica como estava (SHA-256 da ficha antes deste adendo: 77f2e60af942b004fde8443030ff42c251e45057451f8d03845628f4df6e5639, a versão citada no R1, no R2 e no estilo da leva 2). Este adendo prevalece sobre as seções 0 a 8 onde divergir; vale para as levas 3 a 12.

### 9.1 Ids, faixas e confirmação da ficha da leva 3 (seção 8.4.9)
- **D1-R03 vago** (reprovado no R1 da leva 2, gêmeo do D1-55; não volta). **D1-R13 usado** na 2.2, posição 3. Faixas do D1 na leva 12 deslocadas em +1: 1.1 = **D1-R14 a D1-R22**; 1.2 = **D1-R23 a D1-R31**. Faixas de D2, D3, D4 e D5 inalteradas (D3 segue em D3-R22; D4 segue como na seção 7.1).
- **Ficha da leva 3 (seção 8.4) CONFIRMADA**, com a mudança da seção 9.3 (L3-1) e a conferência da seção 9.4 no R1: os pontos da 6.4 usados na leva 2 são os da seção 8.3.4, sem substituto na 6.4; nenhum ponto da leva 3 (A6.4-15, 09, 11, 16 na 6.4) coincide com os da leva 2. A leva 3 pode ser despachada: o QA da leva 2 está fechado (R2, última rodada; D-REFORCO-DA).

### 9.2 Concentração por norma (corrige a seção 8.2, item 5, só para a 2.2 fechada)
- A 2.2 fecha com **Decreto 9.830 = 6** (D1-R02, R13, R04, R08, R09, R10), acima do teto de 5, e Lei 14.133 = 4 (no teto). Extrapolação aceita com registro (reconciliação, seção 4.1). Os tetos por norma da seção 8.2, item 5, são parâmetro de composição da GCB, não regra da seção 1; substituto ditado pela QA pode excedê-los em 1 quando toda alternativa da reserva excede outro teto ou é gêmea, com registro na reconciliação e nota de simulado para o par mais próximo. Nas levas seguintes o teto fixado em cada ficha continua a valer no plano.
- Reserva da 2.2 (folha fechada, sem uso previsto): A2.2-01 fora (gêmeo do D1-55); **A2.2-05 fora** (gêmeo do D1-57; R1, seção 9); A2.2-09 usado. Fica: A2.2-06, 11, 14 (nunca com o D1-R08), 15, 19, 21, 22.
- Corrige a seção 8.3.5: formatos da 2.2 ao fim da leva 2 = **6/2/5/1/6/0** (DEF e PAR no teto de 6); formatos da leva 2 = DEF 7, SUJ 4, SIT 8, NUM 0, PAR 6, APL 5. Corrige a seção 8.3.6: nenhum SUJ da leva 2 troca o sujeito (o D1-R03 saiu).

### 9.3 Recomendações da gbq-estilo aceitas (L3-1 a L3-5; estilo da leva 2, seção 6)
1. **L3-1 — abertura por folha fechada.** A regra 7.4.2 (CQ com ao menos 40% de C; declarativos com ao menos 40% de E) também é conferida na folha fechada (canônicos + reforço). **Aplicação na leva 3: o D3-R25 (A6.4-16, CDC, art. 14, caput; C; sem [TS]; parcial) passa a abrir com "Considere que", sem moldura, formato SIT** (no lugar de SUJ); sem a fórmula "Nessa situação, nos termos d…" (a norma vai no cenário ou no fim do enunciado; seção 7.4.3); cenário que não repete, até o fecho, o do D3-R17 ("Considere que determinada empresa desenvolva…"; L3-3); nenhuma menção a Poder Legislativo, Câmara, Congresso, parlamentar ou comissão (seção 8.2, item 4). Efeitos (conferidos por script sobre o plano): 6.4 fechada com CQ 4 C / 5 E (44,4%); leva 3 com CQ 6 C / 6 E e declarativos 10 C / 8 E (44,4% de E); fórmula na leva 3 em no máximo 5 dos 12 CQ, na 6.4 em 2 dos 6; formatos da 6.4 ao fim da leva 3 = 5/2/4/2/2/5 (teto 6) e da leva 3 = DEF 5, SUJ 8, SIT 7, NUM 2, PAR 3, APL 5; gabarito, [TS], moldura, aderência, núcleo e sequência (seção 8.4.7) inalterados.
2. **L3-2 — absoluto inserido pela troca.** Em item E cuja troca insere absoluto que não está na fonte ("sem limite", "exclusivamente", "qualquer"), a leva traz ao menos um C com absoluto literal da fonte na mesma folha ou no mesmo lote. A seção 4 do arquivo da leva informa a contagem de absolutos por gabarito. Quando a fonte permitir, prefere-se a troca por conceito vizinho (E1) à troca por absoluto.
3. **L3-3 — cenário gêmeo.** Dois itens da mesma folha com cenário literal idêntico até o fecho só entram com a nota "não pôr no mesmo simulado" declarada pela gcb-cpp no próprio arquivo da leva (bloco à GCB).
4. **L3-4 — contraste "mas não".** Contraste "mas não" / ", e não" em item E só se a leva ou o lote tiver C com o mesmo contraste literal (DA acumulado: "mas não" 0 C / 2 E; ", e não" 6 C / 5 E).
5. **L3-5 — qualificador minimizador.** Em item E de inversão de polaridade de dispositivo com "mero", "por si só" ou "simples", a folha traz um C com qualificador equivalente (2.2: D1-R09 C equilibra D1-R04 E). Na dúvida, o qualificador fica, se tirá-lo tornar o gabarito discutível.
6. **Rito do estilo** (registro 1 do estilo da leva 2): a auditoria da amostra da seção 8.4.8 corre **sobre a v1, em paralelo ao R1**, despachada junto com o R1; os AJ de estilo vão com os AJ do R1 para a v2 e são conferidos no R2. Texto de estilo sobre item já aprovado no R2 continua só como errata com conferência da gcb-cqfp (seção 7.6, lida pela D-T116-LEVA1-ACEITE).
7. Medida: a reconciliação de cada leva confere L3-1 a L3-5 junto com as regras da seção 7.4.

### 9.4 Errata AJ-L2-E1 do D3-R18 — conferência da gcb-cqfp no R1 da leva 3 (como a seção 8.3.10)
O parecer R1 da leva 3 (saida/gcb/QA_DA_reforco_leva3_R1_<data>_gcb-cqfp.md) traz uma **seção própria**, "Errata AJ-L2-E1 (D3-R18, leva 2)", separada do veredito da leva 3:
- texto: o de saida/banco/estilo_DA_reforco_leva2.md (ff94acfd…0300), seção 5 — antes: «tenha causado dano ao erário e falecido.» — depois: «tenha causado dano ao erário e, posteriormente, tenha falecido.»;
- conferências: (1) o "antes" ocorre exatamente 1 vez na seção 1 de saida/gcb/DA_reforco_leva2_v2.md (5baec20d…1bbe) e 1 vez no arquivo, e o "depois", 0 vez; (2) gabarito E, ponto A6.4-13, Troca, mecanismo E3, formato APL, moldura S (mesmo tipo), aderência parcial, abertura CQ e demais campos do bloco inalterados; (3) o enunciado resultante, lido inteiro, não muda o sentido, não cria pista e fica na faixa de extensão da base; (4) a ordem dos fatos (dano, depois falecimento) é a pressuposta pela Lei 8.112, art. 122, § 3º, no adendo do D3 e na cópia em normativo_cache/;
- veredito próprio: **CONFERIDO** ou **NÃO CONFERIDO** (com motivo). Não é terceira rodada da leva 2, não altera o arquivo da leva 2 e não é QA aberto que impeça a leva 4;
- destino: a GCB leva a errata ao gatilho A da leva 3, como item separado; aceita, a GBQ a aplica por substituição exata, com aborto se o "antes" não ocorrer exatamente 1 vez na seção 1, registro por id no registro de alterações do pacote e conferência da gbq-cqe na fidelidade, na T-123 se o aceite vier antes da geração final da v1.14, ou na consolidação seguinte; sem aceite, o D3-R18 fica como aprovado no R2 (defeito só de clareza).

### 9.5 Notas de simulado (substitui a nota (s) e completa a lista (k) a (x) da seção 8.5; destino: T-119 e T-123)
| # | itens | motivo |
|---|---|---|
| (s) | D1-R01 × D1-56; D1-R05 × D1-55 e D1-56; D1-R02 × D1-58 | mesmo dispositivo ou mesmo conceito (P1, P4); a parte "D1-R03 × D1-55" sai (D1-R03 reprovado) |
| (s2) | D1-R13 × D1-R04 | Decreto 9.830, art. 12, §§ 2º e 3º: prova do dolo ou do erro grosseiro |
| (s3) | D1-R04 × D1-R09 | mesmo cenário literal ("determinado agente público, ao emitir opinião técnica, tenha dado causa a dano") e mesmo fecho ("Nessa situação, segundo o Decreto nº 9.830/2019"); o C do D1-R09 (§ 5º) sinaliza o erro do D1-R04 (§ 3º) (gbq-estilo, AJ-L2-E2) |
| (y) | D1-R06 × D1-R07 | Lei 14.133, art. 10, caput e § 1º, II: mesma representação pela advocacia pública |
| (z) | D4-R19 × D4-R27 | mesma Figura 1 do guia da Casa Civil (processos × produtos; impactos × resultados) |
As notas (k), (l), (m), (t), (u), (v), (w) e (x) ficam como na seção 8.5; na leva 2, (v) = D3-R18 e D3-R20 e (x) = D4-R20, D3-R16, R18, R19 e R20.

### 9.6 Núcleo da leva 2 (seção 8.2, item 9, confirmado)
2.2 → D1-R01 e D1-R02; 6.4 → D3-R14 e D3-R15; 8.4 sem núcleo novo (D4-R19 a D4-R28 false); D1-R13 e os demais itens da leva 2 false.

## 10. Adendo após a leva 3 (gcb-gerencia, 22/10/2026, ciclo s16c1)
Fonte: reconciliação saida/gcb/DA_reforco_leva3_reconciliacao_2026-10-22.md (seções 4 e 5), pareceres R1 e R2 da gcb-cqfp da leva 3 e auditoria de estilo saida/banco/estilo_DA_reforco_leva3.md (seção 6). Só acréscimo antes da última linha; o texto acima fica como estava (SHA-256 da ficha antes deste adendo: a09139bc3c05a68230f3aea5746490debb4418840d629574622927e1f2bc8493, a versão citada no R1, no R2 e no estilo da leva 3 e na D-T116-LEVA2-ACEITE). Este adendo prevalece sobre as seções 0 a 9 onde divergir; vale para as levas 4 a 12. Sem commit nem push.

### 10.1 Ids, faixas e núcleo
- Leva 3 sem reprovação e sem substituto: **D3-R22 a D3-R51** usados na ordem da seção 8.4.4; nenhum id vago no D3. Faixas seguintes inalteradas: leva 4 = **D3-R52 a D3-R59** (6.2, segunda parte), **D2-R01 a D2-R10** (3.1) e **D2-R11 a D2-R20** (3.2); leva 5 = D2-R21 a D2-R50; leva 6 = D2-R51 a D2-R80; leva 7 = D3-R60 a D3-R89; D4 como na seção 7.1; D1 como na seção 9.1; D5 como na seção 2.1.
- Núcleo da leva 3 (seção 8.2, item 9, confirmado; D-NUCLEO-CRITERIO): 6.5 → D3-R26 e D3-R27; 5.2 → D3-R38; 6.2 → D3-R49; 6.4 sem núcleo novo; os outros 26 itens false. Com o D3-R49 a 6.2 chega a 10 de núcleo, e a 3.1 e a 3.2 já têm 10 canônicos: **nenhum item da leva 4 recebe núcleo** (todos false).

### 10.2 Regras de forma aceitas depois da leva 3 (estilo da leva 3, seção 6; R1 da leva 3, seção 8, item 4)
As regras das seções 1, 7.4 e 9.3 continuam; estas as completam:
1. **L4-1 — fecho "Nessa situação, é correto afirmar que" fora do D4.** Nos lotes D1, D2, D3 e D5, o fecho só entra se a mesma leva tiver ao menos um C com o mesmo fecho no mesmo lote. A seção 4 do arquivo da leva informa o conjunto por gabarito em cada lote, e não só no D4. Na leva 4: nenhum item usa o fecho.
2. **L4-2 — abertura da 6.2.** A 6.2 chega à leva 4 com "Considere que" 1 C / 3 E; os itens novos da folha com "Considere que" são C até a folha fechada ter CQ com ao menos 40% de C. Aplicada no plano (seção 10.4.4): 2 CQ, ambos C; 6.2 fechada com CQ 3 C / 3 E.
3. **L4-3 — referente de rol ou conjunto.** Item E que troca rol aberto por fechado (E6) nomeia a enumeração que a fonte declara aberta ("os incisos", "a enumeração", "a lista de …"), e não um "rol" que possa ser lido como a categoria-gênero que a própria fonte fecha.
4. **L4-4 — condição inventada sobre hipótese autônoma.** Item E que condiciona uma hipótese autônoma a outra (E3) nomeia a outra hipótese pelos elementos que a lei lhe dá, e não por rótulo que admita sentido amplo.
5. **R1 (a), complementa a seção 7.4.5.** Item E não põe no cenário a hipótese inteira do dispositivo para negar a consequência com "sem" ou "não"; prefere-se trocar o critério ou o elemento por conceito vizinho (E1) a negá-lo (registro do D3-R27).
6. **R1 (b), complementa a seção 7.4.4.** Em item SUJ com gabarito E, o ator posto no lugar do sujeito da letra é mencionado pela fonte e plausível à primeira leitura; ator cuja intervenção seja implausível de saída (a própria autoridade representada, D3-R48) não é usado, porque facilita o E.
7. Medida: a reconciliação de cada leva confere L4-1 a L4-4 e os itens 5 e 6 junto com as regras das seções 7.4 e 9.3.

### 10.3 Registros da leva 3 que valem para as seguintes
- Concentração por norma sem teto fixado na ficha (6.5: Código Civil em 7 de 12 itens da leva): aceita com registro; o teto por norma continua só onde a ficha da leva o fixar (seção 9.2).
- Rótulos de campo que não vão ao pacote.json ("Ponto de julgamento", bloco à GCB) não são harmonizados depois do R2 (reconciliação da leva 3, seção 4.1; precedente da reconciliação da leva 2, seção 4.6, item 1).
- Nenhuma errata pendente de conferência da gcb-cqfp para o R1 da leva 4: a AJ-L2-E1 (D3-R18) já foi CONFERIDA no R1 da leva 3 e vai ao gatilho A da leva 3; o estilo da leva 3 não propôs errata pós-R2.

### 10.4 FICHA DA LEVA 4 — pronta para despacho à gcb-cpp

#### 10.4.1 Objeto (edital, literal; edital/DA_itens_1_12_P1.md)
- "6.2 Responsabilidade por ato comissivo do Estado." — 8 itens, **D3-R52 a D3-R59** (segunda parte; a folha vai de 12 a 20 e fecha).
- "3.1 Disposições constitucionais aplicáveis." — 10 itens, **D2-R01 a D2-R10**; de 10 a 20.
- "3.2 Cargo, emprego e função pública." — 10 itens, **D2-R11 a D2-R20**; de 10 a 20.
Total: 28 (plano da seção 2.1). Saída: saida/gcb/DA_reforco_leva4_v1.md (nomes da seção 7.5); ordem das folhas no arquivo: 6.2, 3.1, 3.2; última linha "FIM DA LEVA 04 — REFORÇO DA". Contexto de uso como na seção 3.1; exemplos hipotéticos, sem norma interna, sistema ou prática real da Câmara.

#### 10.4.2 Lastro e fontes admitidas — a leva 4 NÃO depende de adendo de lastro
- **Nenhum adendo do qa-normativo-da é necessário antes da produção da leva 4.** Pela regra da seção 2.1 ("lastro A CONFIRMAR"), a GCB listou por folha os pontos com lastro literal ainda não usados (seção 10.4.4): 6.2 — 12 pontos livres do Adendo 2 do adendo do D3 (A6.2-01, 03, 05, 07 a 15) para 8 itens; 3.1 — Anexo N do D2, seção 4.1 (CF, arts. 37 a 41; 94 dispositivos de núcleo), 10 pontos e 11 de reserva; 3.2 — Anexo N do D2, seções 4.1 e 4.3 (CF, arts. 37 e 39; Lei 8.112), 10 pontos e 7 de reserva. Conferência própria por script (python3 -I, somente leitura): o trecho decisivo de cada um dos 28 pontos do plano é subcadeia, 1 vez, da cópia em saida/gcb/normativo_cache/ (CF d6580cb3…cb51d; Lei 8.112 72f45d30…2efe; Lei 9.494 e0cde6a9…ee94; Decreto 9.830 ae022402…b232; Lei 13.869 fb3b95c1…4a33; Código Civil 97e0ffaa…a828) e do Anexo N do D2 (b0a54fff…340a) ou do adendo do D3 (bbfd3eed…a797): 28 de 28.
- 6.2: só o "Adendo 2" do adendo do D3 (A2.3.2; textos A2.4.1, A2.4.4, A2.4.5, A2.4.6 e A2.4.7), com os alertas C1 a C12 (A2.5.2), em especial: C6 (Decreto 9.830, art. 14: nome do Decreto e o alcance "No âmbito do Poder Executivo federal"; nunca moldura; a relação entre "dolo ou erro grosseiro" e o "dolo ou culpa" da CF continua [SEM FONTE — não afirmar]); C7 (CF, art. 5º, LXXV: só as duas hipóteses do texto); C8 (Lei 9.494, art. 1º-C: sem termo inicial; nada sobre qual prazo prevalece); C9 (Código Civil e CF, art. 5º, XXIV: o item nomeia a norma e o sujeito dela — "o empregador ou comitente", "o ofensor" —, não diz que o Estado responde por esses artigos e não chama a desapropriação de responsabilidade civil); C11 (Lei 13.869, art. 4º, I: o obrigado é o condenado, não o Estado).
- 3.1 e 3.2: só a seção 4.1 (CF; Fonte 1, https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm) e a seção 4.3 (Lei 8.112; Fonte 4, https://planalto.gov.br/ccivil_03/leis/l8112compilado.htm) do Anexo N do D2 (saida/gcb/D2_anexo_N_mapa_normativo.md), consulta de 20/10/2026, com os alertas 1 a 11 da seção 5.2 do Anexo. A URL é a do Anexo (seção 1, regra 3): a Fonte 4 é grafada sem "www" e a primeira linha da cópia em normativo_cache/ traz "https://www.planalto.gov.br/…" — mesma página, diferença só de grafia do host; o item usa a URL do Anexo e a QA confere o texto na cópia, registrando a grafia.
- Fora da leva 4: CF, art. 37, XVI, b (REVERIFICAR, EC 138/2025; D2-01); art. 40, § 4º, e § 5º-A (EC 140/2026, posterior a 2/10/2026; edital 13.33: nenhum item usa a redação da EC 140 nem afirma o § 5º-A); Decreto 12.374/2025 (REVERIFICAR); art. 39, caput ("Vide ADI 2.135"); CF, art. 37, § 6º (pontos dos canônicos do D3); CF, art. 37, XII, e art. 39, § 6º (nomeiam o Poder Legislativo: moldura implícita, seção 8.2, item 4); Lei 8.112, art. 20, § 4º, art. 41, § 5º, e art. 49, § 1º (reservados à 3.4, exigência (b), leva 5); Lei 8.112, art. 135 (primeiro ponto da 4.2, leva 6); números do estágio probatório (alerta 3 do Anexo N do D2; D2-06 e D2-31); Leis 9.962/2000 e 8.745/1993 (não abertas: [SEM FONTE]); conceitos de "emprego público" e "função pública" além da letra da CF, art. 37 (doutrinários; BASE DOUTRINÁRIA vedada).
- Pertinência na 3.2: dispositivo marcado "núcleo 3.2" ou "compl. 3.2" na seção 3 do Anexo N do D2 que trate do cargo, da função, da investidura ou do exercício conta como aderência **direta** (o próprio mapa o liga à folha); se a gcb-cqfp recusar a pertinência direta, o item passa a parcial por AJ, sem efeito no piso de 10 diretos (a 3.2 tem 10 canônicos diretos).
- Proibidos: memória, fonte secundária, jurisprudência, base doutrinária.

#### 10.4.3 Pontos já usados (não repetir; anti-gêmeo)
- 6.2: D3-32 a D3-40 e D3-81 (A2.3.2, abertura); leva 3: A6.2-02 (D3-R49), A6.2-06 (D3-R50), A6.2-04 (D3-R51); CC, arts. 186 e 927, e Lei 8.112, art. 122, não voltam.
- 3.1 (D2-01 a D2-10; D2_v2_1.md, seção 7): CF, art. 37, III, X, XVI (caput, a, b e c) e § 2º; art. 38, III (com o II como contraste); art. 41, caput, § 1º, III, § 3º e § 4º.
- 3.2 (D2-11 a D2-20): CF, art. 37, I, II, V (dois pontos) e IX; Lei 8.112, arts. 2º, 3º (caput e parágrafo único), 5º, V, e 9º, II e parágrafo único.
- Lote D2, outras folhas (gêmeo entre folhas evitado; "Difere de" obrigatório quando o tema é vizinho): Lei 8.112, arts. 8º (D2-33), 13, § 1º (D2-35), 18 (D2-30), 20, caput e § 3º (D2-31, D2-36), 25 (D2-34), 28 (D2-37), 35 (D2-38) e 91 (D2-39).

#### 10.4.4 Pontos de julgamento por item (ordem final dentro de cada folha; a gcb-cpp redige)
Colunas como na seção 8.3.4. Código do ponto: na 6.2, o do adendo do D3 (A6.2-NN); na 3.1 e na 3.2 (o Anexo N do D2 não tem códigos de ponto), o dispositivo com a seção do Anexo ("CF, art. 37, XVII (Anexo N do D2, 4.1)"). Nenhum C leva [TS] (as três folhas já têm o seu C-isca: D3-36, D2-04, D2-14). Todo E leva [TS] com troca real e única de um elemento literal.

**Folha 6.2 — 8 itens (5 C / 3 E), D3-R52 a D3-R59 (segunda parte; 3 diretos, 5 parciais)**
| id | ponto | base | o que se julga (sentido da troca, sem redação) | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D3-R52 | A6.2-07 | CC, art. 932, caput e III | o empregador ou comitente é também responsável pela reparação civil por seus empregados, serviçais e prepostos, no exercício do trabalho que lhes competir, ou em razão dele (sujeito da letra; sem o Estado na cena: C9) | SUJ | N | C | não | parcial | DC | D3-35 (sujeitos do § 6º da CF; aqui o regime civil do empregador) |
| D3-R53 | A6.2-12 | CF, art. 5º, XXIV | a desapropriação por necessidade ou utilidade pública, ou por interesse social, faz-se mediante justa e prévia indenização em dinheiro, ressalvados os casos previstos na CF (sem chamá-la de responsabilidade civil: C9) | SIT | N | C | não | parcial | CQ | D3-37 (conduta lícita, base doutrinária; aqui a letra do inciso) |
| D3-R54 | A6.2-03 | Decreto 9.830, art. 14 | no âmbito do Poder Executivo federal, o regresso do § 6º do art. 37 da CF depende de dolo ou erro grosseiro do agente em suas decisões ou opiniões técnicas (troca: dolo ou erro grosseiro → dolo ou culpa); nome do Decreto e alcance no enunciado; sem "somente", "apenas" ou "só" no enunciado (o absoluto da letra não pode ficar num E cuja troca é outra); nenhuma afirmação sobre a relação com a CF (C6) | DEF | N | E | sim | direta | DC | D3-R51 (mesmo art. 14, outro elemento: proporcionalidade e razoabilidade); D3-32 e D3-36 (CF: dolo ou culpa) |
| D3-R55 | A6.2-01 | Lei 9.494, art. 1º-C | prescreve em cinco anos o direito de obter indenização dos danos causados por agentes de pessoas jurídicas de direito público (sem termo inicial: C8) | NUM | N | C | não | direta | DC | D3-R49 (mesmo artigo, outro elemento: as prestadoras de direito privado) |
| D3-R56 | A6.2-14 | CC, art. 949 | na lesão ou outra ofensa à saúde, o ofensor indeniza o ofendido das despesas do tratamento e dos lucros cessantes até ao fim da convalescença, além de outro prejuízo que prove ter sofrido (C9) | SIT | N | C | não | parcial | CQ | — |
| D3-R57 | A6.2-13 | Lei 13.869, art. 4º, I | efeito da condenação por abuso de autoridade: tornar certa a obrigação de indenizar, devendo o juiz fixar na sentença o valor mínimo da reparação a requerimento do ofendido (troca: a requerimento do ofendido → de ofício); o obrigado é o condenado (C11) | PAR | N | E | sim | parcial | DC | D3-R44 e D3-R46 (5.2: mesma lei, arts. 2º e 1º, § 2º) |
| D3-R58 | A6.2-10 | CC, art. 942, caput | se a ofensa tiver mais de um autor, todos respondem solidariamente pela reparação (troca: solidariamente → cada autor na proporção da sua participação) | PAR | N | E | sim | parcial | DC | — |
| D3-R59 | A6.2-05 | CF, art. 5º, LXXV | o Estado indenizará o condenado por erro judiciário (só a hipótese do texto; nada sobre atos jurisdicionais em geral: C7) | SUJ | N | C | não | direta | DC | D3-R50 (mesmo inciso, outra hipótese) |
Reserva da 6.2 (na ordem): A6.2-11 (CC, art. 948), A6.2-15 (CC, art. 950), A6.2-08 (CC, art. 933; nunca no mesmo simulado que o D3-R52), A6.2-09 (CC, art. 934; troca por ator que a fonte mencione, seção 10.2, item 6). Substituto mantém formato, gabarito, aderência e abertura da linha ou recalcula as seções 10.4.5 a 10.4.7.

**Folha 3.1 — 10 itens (5 C / 5 E), D2-R01 a D2-R10 (todos diretos)**
| id | ponto | base | o que se julga | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D2-R01 | CF, art. 37, XVII (Anexo N do D2, 4.1) | CF, art. 37, XVII | a proibição de acumular estende-se a empregos e funções e abrange autarquias, fundações, empresas públicas, sociedades de economia mista, suas subsidiárias e sociedades controladas, direta ou indiretamente, pelo poder público | SUJ | N | **C** | não | direta | DC | D2-01 e D2-08 (inciso XVI: hipóteses admitidas; aqui o alcance da proibição) |
| D2-R02 | CF, art. 37, IV (4.1) | CF, art. 37, IV | durante o prazo improrrogável previsto no edital de convocação, o aprovado em concurso é convocado com prioridade sobre novos concursados para assumir cargo ou emprego, na carreira (cenário sem órgão do Legislativo) | SIT | N | C | não | direta | CQ | D2-02 (inciso III: validade e prorrogação; aqui a prioridade no prazo do edital) |
| D2-R03 | CF, art. 38, I (4.1) | CF, art. 38, caput e I (III como contraste) | servidor da administração direta, autárquica ou fundacional no exercício de mandato eletivo federal, estadual ou distrital fica afastado do cargo (troca: afastado → havendo compatibilidade de horários, perceberá as vantagens do cargo sem prejuízo da remuneração do cargo eletivo, que é o regime do inciso III); cena: mandato eletivo estadual, sem nomear parlamentar nem Casa legislativa | APL | S — órgão/servidor do Poder Legislativo da União | E | sim | direta | CQ | D2-03 (inciso III, vereador; aqui o inciso I) |
| D2-R04 | CF, art. 37, VII (4.1) | CF, art. 37, VII | o direito de greve do servidor é exercido nos termos e nos limites definidos em lei específica (troca: lei específica → lei complementar) | DEF | N | E | sim | direta | DC | D2-09 (inciso X: lei específica da remuneração; outro inciso) |
| D2-R05 | CF, art. 37, § 13 (4.1) | CF, art. 37, § 13 | o titular de cargo efetivo com limitação na capacidade física ou mental pode ser readaptado para cargo compatível, desde que tenha a habilitação e a escolaridade exigidas para o cargo de destino, mantida a remuneração do cargo de origem (troca: remuneração do cargo de origem → do cargo de destino) | APL | S — órgão/servidor do Poder Legislativo da União | E | sim | direta | CQ | D2-33 (3.4: Lei 8.112, art. 8º, rol do provimento; aqui a CF e a remuneração do readaptado) |
| D2-R06 | CF, art. 37, XIV (4.1) | CF, art. 37, XIV | os acréscimos pecuniários percebidos por servidor público não são computados nem acumulados para fins de concessão de acréscimos ulteriores | DEF | N | C | não | direta | DC | D2-09 (inciso X; outro inciso) |
| D2-R07 | CF, art. 40, § 1º, II (4.1) | CF, art. 40, § 1º, II (III como contraste) | a aposentadoria compulsória do servidor do regime próprio ocorre aos 70 anos de idade, ou aos 75, na forma de lei complementar (troca: 70 → 65 anos, a idade da aposentadoria voluntária do homem na União, inciso III); nada sobre o § 4º nem o § 5º-A | NUM | N | E | sim | direta | DC | D2-06 (art. 41, caput: três anos; outro número e outro instituto) |
| D2-R08 | CF, art. 37, § 10 (4.1) | CF, art. 37, § 10 | a vedação de perceber simultaneamente proventos de aposentadoria do art. 40 e remuneração de cargo ressalva os cargos em comissão declarados em lei de livre nomeação e exoneração: o aposentado nomeado para esse cargo percebe os dois (cenário sem órgão do Legislativo) | SIT | N | C | não | direta | CQ | D2-08 (acumulação de cargos em atividade; aqui proventos com remuneração) |
| D2-R09 | CF, art. 39, § 2º (4.1) | CF, art. 39, § 2º | a União, os Estados e o Distrito Federal manterão escolas de governo para a formação e o aperfeiçoamento dos servidores públicos, e a participação nos cursos é um dos requisitos para a promoção na carreira | SUJ | N | C | não | direta | DC | — |
| D2-R10 | CF, art. 41, § 2º (4.1) | CF, art. 41, § 2º | invalidada por sentença judicial a demissão do servidor estável, ele é reintegrado, e o eventual ocupante da vaga, se estável, é reconduzido ao cargo de origem, sem direito a indenização (troca: reconduzido → reintegrado ao cargo de origem) | APL | S — órgão/servidor do Poder Legislativo da União | E | sim | direta | CQ | D2-37 (3.4: Lei 8.112, art. 28, conceito de reintegração; aqui a CF e o destino do ocupante da vaga); D2-05 (art. 41, § 3º) |
Moldura da 3.1 (D2-R03, R05, R10): cena com "servidor de órgão do Poder Legislativo da União" (tipo da cota das folhas do D2, seção 1, regra 10); nenhuma norma interna, carreira ou prática real da Câmara; a moldura não decide o gabarito; as três cenas não repetem o mesmo texto até o fecho (L3-3). Reserva da 3.1 (na ordem): CF, art. 37, VI; art. 38, IV; art. 37, XIII; art. 37, XV; art. 39, § 9º; art. 41, § 1º, I; art. 40, § 1º, I; art. 38, II (só como ponto próprio, não como contraste do D2-03); art. 39, § 1º; art. 37, VIII (nunca no mesmo simulado que o D2-R18); art. 38, V.

**Folha 3.2 — 10 itens (5 C / 5 E), D2-R11 a D2-R20 (todos diretos; seção 10.4.2, pertinência)**
| id | ponto | base | o que se julga | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D2-R11 | Lei 8.112, art. 7º (Anexo N do D2, 4.3) | Lei 8.112, art. 7º | a investidura em cargo público ocorre com a posse (troca: posse → nomeação) | PAR | N | **E** | sim | direta | DC | D2-19 (CF, art. 37, II: investidura depende de concurso); D2-33 (3.4: formas de provimento) |
| D2-R12 | Lei 8.112, art. 4º (4.3) | Lei 8.112, art. 4º | é proibida a prestação de serviços gratuitos, salvo os casos previstos em lei | DEF | N | C | não | direta | DC | — |
| D2-R13 | Lei 8.112, art. 19, caput (4.3) | Lei 8.112, art. 19, caput | a jornada é fixada em razão das atribuições do cargo, respeitada a duração máxima de quarenta horas semanais e os limites de seis e oito horas diárias (troca: quarenta → quarenta e quatro horas semanais) | NUM | N | E | sim | direta | CQ | D2-R15 (mesmo artigo, § 1º) |
| D2-R14 | CF, art. 39, § 3º (Anexo N do D2, 4.1) | CF, art. 39, § 3º | a lei pode estabelecer requisitos diferenciados de admissão quando a natureza do cargo o exigir (troca: a lei → o edital do concurso); sem enumerar os incisos do art. 7º | SUJ | N | E | sim | direta | DC | D2-11 (CF, art. 37, I: requisitos estabelecidos em lei para o acesso; aqui requisitos diferenciados pela natureza do cargo); D2-16 e D2-20 (outras trocas de instrumento normativo) |
| D2-R15 | Lei 8.112, art. 19, § 1º (4.3) | Lei 8.112, art. 19, § 1º | o ocupante de cargo em comissão ou função de confiança submete-se a regime de integral dedicação ao serviço, podendo ser convocado sempre que houver interesse da Administração | SIT | N | C | não | direta | CQ | D2-R13 |
| D2-R16 | Lei 8.112, art. 5º, § 3º (4.3) | Lei 8.112, art. 5º, § 3º | as universidades e instituições de pesquisa científica e tecnológica federais poderão prover seus cargos com professores, técnicos e cientistas estrangeiros, de acordo com as normas e os procedimentos da lei | SUJ | N | C | não | direta | DC | D2-11 (CF, art. 37, I: estrangeiros, na forma da lei; aqui as entidades autorizadas pela Lei 8.112) |
| D2-R17 | Lei 8.112, art. 15, caput (4.3) | Lei 8.112, art. 15, caput | exercício é o efetivo desempenho das atribuições do cargo público ou da função de confiança | DEF | N | C | não | direta | DC | D2-18 (conceito de cargo; aqui o de exercício) |
| D2-R18 | Lei 8.112, art. 5º, § 2º (4.3) | Lei 8.112, art. 5º, § 2º | às pessoas portadoras de deficiência são reservadas até 20% das vagas oferecidas no concurso (troca: até 20% → no mínimo 20%) | NUM | N | E | sim | direta | DC | D2-17 (art. 5º, V, idade mínima; outro elemento do artigo) |
| D2-R19 | Lei 8.112, art. 120 (4.3) | Lei 8.112, art. 120 | quem acumula licitamente dois cargos efetivos e é investido em cargo em comissão fica afastado de ambos, salvo compatibilidade de horário e local com um deles, declarada pelas autoridades máximas dos órgãos ou entidades envolvidos | SIT | N | C | não | direta | CQ | D2-15 (art. 9º: interinidade em cargo de confiança) |
| D2-R20 | Lei 8.112, art. 34, parágrafo único, II (4.3) | Lei 8.112, art. 34, caput e parágrafo único, II | quem tomou posse e não entrou em exercício no prazo estabelecido é exonerado de ofício (troca: exonerado de ofício → demitido) | SIT | N | E | sim | direta | CQ | D2-38 (3.4: art. 35, exoneração de cargo em comissão) |
Na 3.2, "lei" como instrumento normativo fica 3 C / 3 E na folha fechada (D2-11, D2-14, D2-R12 / D2-16, D2-20, D2-R14), sem pista "lei trocada → E". Reserva da 3.2 (na ordem): Lei 8.112, art. 10, caput; art. 13, § 4º; art. 13, § 5º; art. 14, caput e parágrafo único; art. 62, caput; art. 118, § 2º; art. 119, caput (nunca no mesmo simulado que o D2-15).

#### 10.4.5 Formatos ao fim da leva 4 (folha final de 20; teto 6)
| folha | DEF | SUJ | SIT | NUM | PAR | APL | total |
|---|---|---|---|---|---|---|---|
| 6.2 (12 após a leva 3: 4/1/4/0/3/0 + leva 1/2/2/1/2/0) | 5 | 3 | **6** | 1 | 5 | 0 | 20 |
| 3.1 (canônicos 3/1/1/2/1/2 + 2/2/2/1/0/3) | 5 | 3 | 3 | 3 | 1 | 5 | 20 |
| 3.2 (canônicos 3/3/2/1/0/1 + 2/2/3/2/1/0) | 5 | 5 | 5 | 3 | 1 | 1 | 20 |
SIT da 6.2 fica no teto (6): a gcb-cpp não declara outro SIT na folha; reclassificação pela QA obriga a mudar a construção de outro item. Formatos da leva 4: DEF 5, SUJ 6, SIT 7, NUM 4, PAR 3, APL 3. A recomendação do produtor da leva 3 (bloco 5: na 6.2, no máximo DEF 2, SIT 2 e PAR 3) está cumprida (1, 2 e 2).

#### 10.4.6 Gabarito, moldura, aderência e conjuntos ao fim da leva 4
- Leva: **15 C / 13 E (53,6%)**; faixa de 28 itens: 12 a 16 C. Folhas: 6.2 10/10 (5/7 + 5/3); 3.1 10/10 (5/5 + 5/5); 3.2 10/10 (5/5 + 5/5).
- Moldura nova: **0 C / 3 E** (D2-R03, D2-R05, D2-R10; todos na 3.1). DA: 49/25 → **49/28 (63,6%)**, igual à seção 2.2. Por folha: 3.1 2 C / 3 E (40,0%), 5 com moldura (≤ 6); 3.2 0/1; 6.2 0/0. Cota da T-122 na 3.1 cumprida (3 E). Conjunto do D2 (moldura): 9/1 → **9/4 (69,2%)**; no fim do plano, 10/14 (seção 2.2). Conjuntos do D3 (9/11) e do D4 (K1 a K4, fecho neutro, ", e não") sem item novo.
- Aderência: 23 diretos / 5 parciais (D3-R52, R53, R56, R57, R58). Piso de 10 diretos: 6.2 15; 3.1 20; 3.2 20.
- [TS]: 13 (todos E; nenhum C-isca). VOLÁTIL 0. REVERIFICAR 0 (nenhum dispositivo do plano tem redação de 2025 ou 2026).
- Abertura × gabarito (seção 7.4.2; L3-1; L4-2): leva "Considere que" 6 C / 5 E (54,5% de C); declarativos 9 C / 8 E (47,1% de E). Folhas fechadas: 6.2 CQ 3 C / 3 E e DC 7 C / 7 E; 3.1 CQ 4/4 e DC 6/6; 3.2 CQ 4/3 e DC 6/7.
- Fórmula "Nessa situação, nos termos d…" (seção 7.4.3): na 6.2 (D3), no máximo 1 dos 2 itens com "Considere que"; no D2, contada e informada (no máximo 4 dos 9 CQ, como orientação). Fecho "é correto afirmar que": 0 (L4-1).
- L3-2: nenhum E com absoluto inserido pela troca no plano; se a redação inserir absoluto em E, a mesma folha precisa de C com absoluto literal, e a seção 4 do arquivo informa. L3-4 e L3-5: nenhum contraste "mas não" / ", e não" e nenhum "mero", "por si só" ou "simples" planejados. Seção 10.2, itens 5 e 6: todas as trocas do plano são de elemento por conceito vizinho; nenhum SUJ E troca o sujeito por ator implausível (o D2-R14 troca o instrumento: lei → edital).

#### 10.4.7 Sequência (seção 7.3; plano conferido por script antes do despacho)
| escopo | gabarito | [TS] | resultado |
|---|---|---|---|
| 6.2, leva / acumulada (20) | CCECCEEC / ECEECCEECEEC·CCECCEEC | nnTnnTTn / TnTTTnnTnTTn·nnTnnTTn | passa; acumulada: só o legado de período 4 nas posições 2 a 9 do gabarito (seção 8.2, item 7); nenhuma janela reprovada inclui item novo; [TS] passa |
| 3.1, leva / acumulada (20) | CCEEECECCE / ECECCEECEC·CCEEECECCE | nnTTTnTnnT / TnTTnTnnTn·nnTTTnTnnT | passa (o D2-R01, C, fecha a alternância de 4 com que terminam os canônicos) |
| 3.2, leva / acumulada (20) | ECEECCCECE / CCECEECCEE·ECEECCCECE | TnTTnnnTnT / nnTTnTnnTT·TnTTnnnTnT | passa |
| leva 4 inteira (6.2, 3.1, 3.2) | CCECCEEC·CCEEECECCE·ECEECCCECE | idem com T nos E | passa (corrida máx. 3; alternância máx. 4) |
Mesma regra de troca de posição da seção 8.3.7.

#### 10.4.8 Amostra da gbq-estilo (leva 4)
4 itens (14,3%), designados antes da produção: **D2-R05** (E com moldura do Legislativo, APL, CF, art. 37, § 13); **D2-R14** (E, SUJ, troca de instrumento lei → edital, na folha com D2-16 e D2-20); **D3-R54** (E, Decreto 9.830, art. 14, alerta C6); **D3-R56** (C, SIT com "Considere que", aderência parcial, CC, art. 949). Cobre: E com moldura, os dois lotes, um C, um parcial. Rito da seção 9.3, item 6: auditoria sobre a v1, em paralelo ao R1; os AJ de estilo vão com os AJ do R1 para a v2 e são conferidos no R2. Saída: saida/banco/estilo_DA_reforco_leva4.md.

#### 10.4.9 Notas de simulado previstas para a leva 4 (destino: T-119 e T-123; continuam (a) a (ae))
| # | itens | motivo |
|---|---|---|
| (af) | D3-R55 × D3-R49 e D3-R22 | prazos de cinco anos (Lei 9.494, art. 1º-C; Decreto 20.910); amplia a (n) |
| (ag) | D3-R54 × D3-R51, D3-32 e D3-36 | Decreto 9.830, art. 14 × CF, art. 37, § 6º (C6); amplia a (o) |
| (ae) | D3-R59 × D3-R50 | CF, art. 5º, LXXV, as duas hipóteses (C7) |
| (ah) | D2-R03 × D2-03 | CF, art. 38, I × III |
| (ai) | D2-R10 × D2-37 e D2-05 | reintegração, recondução e disponibilidade (CF, art. 41, §§ 2º e 3º; Lei 8.112, art. 28) |
| (aj) | D2-R05 × D2-33 | readaptação (CF, art. 37, § 13; Lei 8.112, art. 8º) |
| (ak) | D2-R13 × D2-R15 | Lei 8.112, art. 19, caput e § 1º |
| (al) | D2-R16 × D2-11 | estrangeiros (Lei 8.112, art. 5º, § 3º; CF, art. 37, I) |
| (am) | D2-R14 × D2-16 e D2-20 | trocas de instrumento normativo na mesma folha |
| (an) | D2-R11 × D2-R20 | posse, investidura e exercício |
| (v) | parciais da leva 4: D3-R52, R53, R56, R57, R58 | só simulado diagnóstico (D-ADERENCIA) |
| (w) | a leva 4 inteira (ou só itens de reforço) | não forma simulado isolado; entra misturada por folha com os canônicos |
| (x) | os 3 itens com moldura (D2-R03, R05, R10) | contam para o teto de 50% de C com moldura por simulado (D-MOLDURA-CE (c)) |

#### 10.4.10 Despacho à gcb-cpp (leva 4)
- Executor: gcb-cpp (sonnet), uma instância. Objeto: leva 4, conforme esta seção 10.4, as seções 1, 7, 8.2 (itens 4 e 7), 9.3 e 10.2 e os anexos abaixo. Saída: saida/gcb/DA_reforco_leva4_v1.md, no formato da regra 14 (nomes da seção 7.5), linha 1 `# DA_reforco_leva4_v1.md — T-116 — <data ISO> — gerado por gcb-cpp`.
- Anexos (lista exaustiva): esta ficha; saida/gcb/D2_anexo_N_mapa_normativo.md (seções 1, 2.3, 3, 4.1, 4.3 e 5.2); saida/gcb/D3_anexo_N_adendo_2026-10-20.md ("Adendo 2": A2.3.2, A2.4.1, A2.4.4 a A2.4.7 e A2.5.2); saida/gcb/D2_v2_1.md (pontos D2-01 a D2-40, seção 7, e formato dos blocos canônicos) e saida/gcb/D3_v2_1.md (pontos da 6.2), só para os pontos já usados; os arquivos finais das levas 1 a 3 (saida/gcb/DA_reforco_leva1_v2.md, leva2_v2.md e leva3_v2.md: pontos e modelo de bloco); regras/estilo_banca.md; cópias em saida/gcb/normativo_cache/.
- A seção 4 do arquivo traz, por script: as contagens da regra 14; abertura × gabarito e fecho × gabarito por lote (D2 e D3: canônicos, levas anteriores, leva, acumulado; L4-1); a fórmula "Nessa situação, nos termos d…"; absolutos por gabarito (L3-2); o teste da seção 10.4.7 refeito; a moldura acumulada (DA, D2, D3).
- A gcb-cpp pode trocar um ponto pela reserva da mesma folha, com o motivo no bloco à GCB, nas condições da seção 3.7. Dúvida de conteúdo vai ao bloco à GCB, sem consulta a terceiros. O R1 da leva 4 não tem errata a conferir (seção 10.3). Nada vai à plataforma nem à candidata. Sem commit.

### 10.5 Riscos e registros
1. A 6.2 fecha em 20 com 5 itens de aderência parcial (C9, C11); se a gcb-cqfp recusar a pertinência de um indireto, o substituto sai da reserva (seção 10.4.4); sem reserva aceita, a folha fica abaixo de 20, com registro (seção 2.1).
2. SIT da 6.2 no teto (6); PAR da 6.2 em 5.
3. Moldura: leva 4 com 0 C / 3 E, como no plano; a meta da D-MOLDURA-CE continua prevista para a leva 5 (seção 2.2, margem de 2 pontos); E com moldura reprovado na leva 4 é reposto na v2 da mesma leva (reserva da 3.1, mesmo tipo de moldura).
4. Leva 5 (3.3, 3.4 e 4.1): a 4.1 está "A CONFIRMAR" (seção 2.1; o Anexo N do D2 diz que "fontes" do direito disciplinar não têm dispositivo próprio e não transcreve a CF, art. 5º, LIV e LV). A GCB lista o lastro da 4.1 na ficha da leva 5; se faltar, pede adendo ao qa-normativo-da antes da produção da leva 5 — o pedido pode correr em paralelo à leva 4, sem tarefa nova (primeiro passo da T-116).
5. Nenhuma tarefa nova (D-COMPLEMENTOS); nenhum gatilho em PARA_PRESIDENCIA.md por esta seção (o gatilho da leva 3 é da reconciliação).

## 11. Adendo após a leva 4 (gcb-gerencia, 22/10/2026, ciclo s16c2)
Fonte: reconciliação saida/gcb/DA_reforco_leva4_reconciliacao_2026-10-22.md (seções 4 e 5), pareceres R1 e R2 da gcb-cqfp da leva 4 e auditoria de estilo saida/banco/estilo_DA_reforco_leva4.md (seções 4, 6 e 7). Só acréscimo antes da última linha; o texto acima fica como estava (SHA-256 da ficha antes deste adendo: 777e6eb6a2d871f5d6afc26b22a479a9ccfcb9ede3285d68ab06e391c761a03a, a versão citada no R1, no R2 e no estilo da leva 4 e na D-T116-LEVA3-ACEITE). Este adendo prevalece sobre as seções 0 a 10 onde divergir; vale para as levas 5 a 12. Sem commit nem push.

### 11.1 Ids, faixas e núcleo
- Leva 4 sem reprovação e sem substituto: **D3-R52 a D3-R59** (6.2, segunda parte), **D2-R01 a D2-R10** (3.1) e **D2-R11 a D2-R20** (3.2), na ordem da seção 10.4.4; nenhum id vago. As folhas 6.2, 3.1 e 3.2 fecham em 20. O D3 fica em D3-R59 (próximo: D3-R60, leva 7).
- Faixas seguintes inalteradas: leva 5 = **D2-R21 a D2-R30** (3.3), **D2-R31 a D2-R40** (3.4) e **D2-R41 a D2-R50** (4.1); leva 6 = D2-R51 a D2-R80 (D2-R51 = Lei 8.112, art. 135, exigência (b)); leva 7 = D3-R60 a D3-R89; D4 como na seção 7.1; D1 como na seção 9.1; D5 como na seção 2.1.
- Núcleo da leva 4: os 28 itens false (seção 10.1). Leva 5: a 3.3, a 3.4 e a 4.1 já têm 10 canônicos cada; **nenhum item da leva 5 recebe núcleo** (todos false).

### 11.2 Regras de forma aceitas depois da leva 4 (estilo da leva 4, seção 6; R2 da leva 4, seção 6, item 3)
As regras das seções 1, 7.4, 9.3 e 10.2 continuam; estas as completam:
1. **L5-1 — extensão (texto da gbq-estilo, com o complemento da GCB).** "Item E não passa de 62 palavras no enunciado (teto de E da base, estilo_banca, seção 4). Quando a letra traz mais de uma condição verdadeira antes do elemento trocado, o item mantém só a que dá contexto à troca. A seção 4 do arquivo da leva lista por script todo item fora da faixa da base (C de 8 a 65; E de 19 a 62)." Complemento: o plano e a redação também evitam E abaixo de 19 palavras (registro do D2-R11, 14 palavras); E curto fora da faixa só entra com o motivo no bloco à GCB.
2. **L5-2 — absoluto da letra retirado de E com outra troca (texto da gbq-estilo).** "Quando a ficha manda tirar do E o absoluto da letra ('somente será exercido na hipótese de'), o item mantém a moldura do dispositivo sem o absoluto ('será exercido na hipótese de'), e não um verbo de condição necessária ('depende de', 'exige', 'pressupõe'). Isso vale sempre que o termo posto pela troca puder abranger o da letra (culpa × erro grosseiro; D3-R54, AJ-L4-E2)." Aplicação na leva 5: D2-R41 e D2-R46 (CF, art. 41, § 1º, "só perderá o cargo") não usam "só" nem verbo de condição necessária.
3. Medida: a reconciliação de cada leva confere L5-1 e L5-2 junto com as regras das seções 7.4, 9.3 e 10.2.

### 11.3 Registros da leva 4 que valem para as seguintes
- SHA abreviado no bloco à GCB do arquivo da leva (campo que não vai ao pacote.json): erro de transcrição não abre errata depois do R2; vale o valor completo registrado na reconciliação (reconciliação da leva 4, seção 4.1).
- Um mesmo texto de AJ pedido pelo R1 e pela gbq-estilo é aplicado uma vez e registrado como um só ajuste, com as duas origens (AJ-1 = AJ-L4-E2).
- Nenhuma errata pendente de conferência da gcb-cqfp para o R1 da leva 5.

### 11.4 FICHA DA LEVA 5 — despachável depois do adendo de lastro da 4.1 (seção 11.4.2)

#### 11.4.1 Objeto (edital, literal; edital/DA_itens_1_12_P1.md)
- "3.3 Requisição." — 10 itens, **D2-R21 a D2-R30**; de 10 a 20.
- "3.4 Regime jurídico dos servidores públicos federais (Lei 8.112/1990 e suas alterações)." — 10 itens, **D2-R31 a D2-R40**; de 10 a 20; exigência (b).
- "4.1 Fontes e princípios." — 10 itens, **D2-R41 a D2-R50**; de 10 a 20.
Total: 30 (plano da seção 2.1). Saída: saida/gcb/DA_reforco_leva5_v1.md (nomes da seção 7.5); ordem das folhas no arquivo: 3.3, 3.4, 4.1; última linha "FIM DA LEVA 05 — REFORÇO DA". Exemplos hipotéticos, sem norma interna, sistema ou prática real da Câmara.

#### 11.4.2 Lastro, rede e adendo — situação da leva 5
Conferência própria (python3 -I, somente leitura, scratchpad gcb_l4/plan5b.py, stats5b.py e lines5.py): o trecho decisivo de cada um dos 30 pontos do plano foi procurado no Anexo N do D2 (b0a54fff…340a) e nas cópias de saida/gcb/normativo_cache/.
- **3.3 — lastro CONFIRMADO no Anexo N do D2, sem cópia própria em cache.** O Anexo traz o texto literal do Decreto 10.835/2021 (seção 4.5, integral; Fonte 7), da Lei 9.007/1995 (seção 4.6, arts. 2º, 3º e 6º; Fonte 8), da Lei 6.999/1982 (seção 4.7, integral; Fonte 9) e do Decreto 12.374/2025 (seção 4.8, arts. 2º, 21, 24 e 25; Fonte 10), transcrito por script do HTML oficial baixado em 20/10/2026 (SHA-256 de cada HTML na seção 1 do Anexo; conferência por segundo extrator na seção 5.3, que inclui o Decreto 10.835, art. 9º, § 1º, e art. 24, § 3º, e a Lei 6.999, art. 2º, § 1º). Os 10 trechos da 3.3 ocorrem 1 vez cada no Anexo (linhas 1631, 1673, 1677, 1679, 1767, 1778, 1818, 1821, 1822 e 1828). Não há cópia dessas normas em normativo_cache/, e www.planalto.gov.br está bloqueado neste ambiente: a conferência da 3.3 é trecho × linha do Anexo (seção 4.1, item 1), e a conferência (8) da seção 4.4 (bases reabertas no cache) não se aplica à 3.3 — a amostra de 5 bases reabertas sai da 3.4 e da 4.1, e o parecer registra. O Decreto 12.374/2025 (REVERIFICAR, seção 2.3 do Anexo) fica fora da leva 5.
- **3.4 — lastro CONFIRMADO** (Anexo N do D2, seção 4.3; cópia Lei_8112_1990_compilada_2026-10-20.txt, 72f45d30…2efe): 10 de 10 trechos, 1 vez no Anexo e 1 vez na cópia.
- **4.1 — lastro INSUFICIENTE sem adendo.** Pontos com lastro literal ainda não usados (seção 3 do Anexo: núcleo e compl. 4.1): Lei 9.784, art. 2º, parágrafo único, I, IV, V, VII, VIII, IX e XII (os incisos II, III, VI, X, XI e XIII e o caput já são pontos de D1-11 a D1-15, D2-41, D2-43 e D2-49), e CF, art. 41, § 1º, I e II (o III é o D2-04) — 9 pontos para 10 itens; Lei 8.112, arts. 125, 126, 128 e 143, caput, e CF, art. 37, caput, já são pontos de canônicos (D2-42, D2-44, D2-46 a D2-48; D1-09); o inciso I do art. 2º, parágrafo único, fica reservado à folha 1.1 (leva 12; legalidade). Pela regra da seção 2.1, a GCB pede **adendo ao qa-normativo-da** com a **CF, art. 5º, LIV e LV** (devido processo legal; contraditório e ampla defesa no processo administrativo), que o próprio Anexo do D2 (seção 3, nota da 4.1, e seção 5.1) declara "[SEM FONTE — não afirmar]" por não transcritos e indica para inclusão. Os dois incisos estão na cópia CF_1988_compilada_2026-10-20.txt (d6580cb3…cb51d; linha 1: mesma URL da Fonte 1 do Anexo, "verificado em 20/10/2026"), linhas 124 e 125, sem nota de alteração — trecho do plano 1 vez cada.
- **(a) A leva 5 NÃO é despachável já.** Fica despachável à gcb-cpp assim que o adendo estiver gravado e a GCB conferir, por script, que os dois trechos do plano (D2-R42 e D2-R49) ocorrem 1 vez no adendo e na cópia (conferência de linha, sem nova ficha nem novo gatilho). Nada mais da ficha depende do adendo.
- **(b) Depende de adendo do qa-normativo-da, e o adendo é possível só com o cache**: a transcrição sai da cópia oficial da CF já gravada (20/10/2026), com a data verdadeira da consulta (D-FONTE-DATA-ANTERIOR), sem rede; o qa-normativo-da registra que não reabriu o planalto. Escopo do adendo (fechado): CF, art. 5º, caput, LIV e LV, marcados "Edital: núcleo 4.1", com a mesma convenção da seção 4 do Anexo; nada mais.
- **(c) Nenhuma folha da leva 5 fica impossível sem rede.** Registro de limitação (não bloqueio): a reabertura das Fontes 7 a 10 do Anexo N do D2 (Decreto 10.835, Leis 9.007 e 6.999, Decreto 12.374) é impossível neste ambiente, e a 3.3 se apoia só na transcrição do Anexo (que é o lastro exigido pela seção 0.2, item 3). Se o adendo não for feito, a 4.1 não fica impossível: o D2-R42 passa ao inciso I do art. 2º, parágrafo único (C, DEF, DC; com registro do conflito com a folha 1.1) e o D2-R49 fica vago, a 4.1 fecha em 19 e a leva sai com 29 itens (15 C / 14 E; seção 2.1, "a leva sai menor").
- Fontes admitidas: só o Anexo N do D2 (seções 1, 2.3, 3, 4.1, 4.3, 4.4, 4.5, 4.6, 4.7 e 5) e, para a CF, art. 5º, LIV e LV, o adendo; URL e data da Fonte do Anexo (Fonte 1 CF; Fonte 4 Lei 8.112, grafada sem "www", como na leva 4; Fonte 6 Lei 9.784; Fonte 7 Decreto 10.835; Fonte 9 Lei 6.999). Proibidos: memória, fonte secundária, jurisprudência, base doutrinária.
- Fora da leva 5: Decreto 12.374/2025 (REVERIFICAR; D2-28 e T-120); Decreto 10.835, arts. 12, 16, 23, 31 a 33 (atos de autoridade com denominação de ministério anterior) e art. 5º (revogado); qualquer órgão requisitante além da Presidência da República (Lei 9.007) e da Justiça Eleitoral (Lei 6.999) ("[SEM FONTE — não afirmar]", Anexo 5.1); Lei 8.112, art. 20, caput, e números do estágio probatório (alerta 3); art. 143, §§ 1º e 2º (revogados); art. 135 (D2-R51, leva 6); arts. 116 a 182 como ponto da 3.4 (são das folhas 4.2 e 4.3); CF, art. 37, XVI, b, e art. 40, §§ 4º e 5º-A; "fontes" do direito disciplinar como conceito (doutrinário, sem dispositivo).

#### 11.4.3 Pontos já usados (não repetir; anti-gêmeo)
- 3.3 (D2-21 a D2-30): Decreto 10.835, art. 9º, caput, § 1º e §§ 2º e 3º; art. 11, caput e parágrafo único (com o art. 8º como contraste); Lei 9.007, art. 2º, caput e parágrafo único; Lei 6.999, art. 2º, § 1º; Decreto 12.374, art. 21, § 1º; CF, art. 5º, XXV; Lei 8.112, art. 18, caput e § 2º.
- 3.4 (D2-31 a D2-40): Lei 8.112, arts. 8º, 13, § 1º, 20, caput e § 3º, 25, 28, 35, 36 e 37, 91, 106 e 107. Lote D2, outras folhas: arts. 2º a 10, 15, 19, 34 e 120 (3.2; leva 4 incluída) e os arts. 116 a 182 (4.2 e 4.3).
- 4.1 (D2-41 a D2-50): Lei 9.784, art. 2º, parágrafo único, VI, X e XI, e art. 69; Lei 8.112, arts. 125, 126, 128 (caput e parágrafo único), 129, caput, e 143, caput. Outros lotes: Lei 9.784, art. 2º, caput e parágrafo único, II, III e XIII (D1-11 a D1-15, folha 1.1); CF, art. 37, caput (D1-09).

#### 11.4.4 Pontos de julgamento por item (ordem final dentro de cada folha; a gcb-cpp redige)
Colunas como na seção 10.4.4; código do ponto = dispositivo com a seção do Anexo. Nenhum C leva [TS] (as três folhas já têm o seu C-isca: D2-27, D2-35, D2-43). Todo E leva [TS] com troca real e única de um elemento literal. Todos os pontos são "núcleo" ou "compl." da folha na seção 3 do Anexo e contam como aderência **direta**; se a gcb-cqfp recusar a pertinência direta de um "compl." (D2-R41, D2-R46), o item passa a parcial por AJ, sem efeito no piso (as três folhas têm 10 canônicos diretos).

**Folha 3.3 — 10 itens (6 C / 4 E), D2-R21 a D2-R30 (todos diretos; sem moldura)**
| id | ponto | base | o que se julga (sentido da troca, sem redação) | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D2-R21 | Decreto 10.835, art. 9º, § 4º (Anexo N do D2, 4.5) | idem | na requisição não há prejuízo da remuneração ou do salário permanente do agente público, incluídos encargos sociais, abono pecuniário, gratificação natalina, férias e adicional de um terço | DEF | N | C | não | direta | DC | D2-23 (Lei 9.007, art. 2º, parágrafo único: requisição para a Presidência; aqui a regra geral do Decreto) |
| D2-R22 | Decreto 10.835, art. 29, caput (4.5) | idem, sem a ressalva final (art. 93, § 4º, da Lei 8.112) | a competência para disponibilizar a requisição é do Ministro de Estado ou da autoridade máxima da entidade a que pertencer o agente público (troca: … a que pertencer o agente público → a autoridade máxima do órgão ou da entidade requisitante, ator que a fonte menciona no art. 9º; seção 10.2, item 6) | SUJ | N | E | sim | direta | DC | D2-22 (art. 9º, § 1º: quem pode requisitar; aqui quem disponibiliza) |
| D2-R23 | Lei 6.999, art. 3º, caput (4.7) | idem | no acúmulo ocasional de serviço na zona eleitoral, outros servidores podem ser requisitados pelo prazo máximo e improrrogável de seis meses (troca: seis meses → um ano, o número do art. 2º, § 1º) | NUM | N | E | sim | direta | DC | D2-27 (art. 2º, § 1º: um ano, prorrogável, nos cartórios) |
| D2-R24 | Lei 6.999, art. 9º (4.7) | idem | o servidor requisitado para o serviço eleitoral conserva os direitos e vantagens inerentes ao exercício de seu cargo ou emprego (cenário: servidor de órgão federal requisitado para cartório eleitoral; sem órgão do Legislativo) | SIT | N | C | não | direta | CQ | D2-23 (Presidência, Lei 9.007) |
| D2-R25 | Lei 6.999, art. 3º, § 3º (4.7) | art. 3º, caput e § 3º | na requisição por acúmulo ocasional, somente depois de decorrido um ano pode haver nova requisição do mesmo servidor ("somente" literal; L3-2) | NUM | N | C | não | direta | DC | D2-R23 (mesmo artigo, caput: nota (at)) |
| D2-R26 | Decreto 10.835, art. 30-A, caput e III (4.5) | idem | a conversão da cessão em requisição dispensa novo ato de requisição (nada sobre o parágrafo único) | SIT | N | C | não | direta | CQ | D2-26 (art. 11, parágrafo único × art. 8º: encerramento; aqui a conversão) |
| D2-R27 | Decreto 10.835, art. 9º, § 5º, II, e § 6º (4.5) | idem | ao requisitado é garantida a participação em concurso de remoção, e a eventual alteração material do local de exercício ou de lotação se dá quando encerrada a requisição (troca: quando encerrada a requisição → de imediato, ainda durante a requisição) | SIT | N | E | sim | direta | CQ | D2-R21 (mesmo art. 9º, § 4º: nota (ax)) |
| D2-R28 | Decreto 10.835, art. 10 (4.5) | idem | as requisições que impliquem reembolso pela administração pública federal ocorrem com a observância da disponibilidade orçamentária e financeira do órgão ou da entidade responsável pelo ônus do ressarcimento (sem "somente": o absoluto não é o ponto) | DEF | N | C | não | direta | DC | — |
| D2-R29 | Decreto 10.835, art. 1º, § 1º, III (4.5) | art. 1º, caput e § 1º, III | o Decreto abrange também os empregados de empresas estatais | SUJ | N | C | não | direta | DC | D2-21 a D2-26 (outros elementos do Decreto) |
| D2-R30 | Lei 6.999, art. 4º, caput (4.7) | idem | as requisições para as Secretarias dos Tribunais Eleitorais que não se destinem a nomeação para cargo em comissão são feitas por prazo certo, não excedente de um ano (troca: prazo certo, não excedente de um ano → prazo indeterminado, a regra geral do Decreto 10.835, art. 11); sem "exceto" | PAR | N | E | sim | direta | DC | D2-25 (Decreto 10.835, art. 11: prazo indeterminado; nota (au)) |
Reserva da 3.3 (na ordem): Decreto 10.835, art. 2º, caput (conceito de movimentação); art. 9º, § 5º, I; art. 30-A, parágrafo único, I; art. 30; art. 22 (nunca no mesmo simulado que o D2-R28); Lei 6.999, art. 2º, caput; art. 3º, § 2º (nunca no mesmo simulado que o D2-R23); art. 8º.

**Folha 3.4 — 10 itens (5 C / 5 E), D2-R31 a D2-R40 (todos diretos; exigência (b))**
| id | ponto | base | o que se julga | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D2-R31 | Lei 8.112, art. 49, § 1º (Anexo N do D2, 4.3) | idem | as indenizações não se incorporam ao vencimento ou provento para qualquer efeito (exigência (b): absoluto literal "para qualquer efeito"; cenário com indenização genérica, sem a ajuda de custo do D2-R40) | SIT | N | **C** | não | direta | CQ | D2-R06 (CF, art. 37, XIV: acréscimos não computados; outra norma; nota (ba)) |
| D2-R32 | Lei 8.112, art. 97, III, a (4.3) | art. 97, caput e III, a | sem qualquer prejuízo, o servidor pode ausentar-se do serviço por oito dias consecutivos em razão de casamento (troca: oito → cinco dias consecutivos) | APL | S — órgão/servidor do Poder Legislativo da União | E | sim | direta | CQ | — |
| D2-R33 | Lei 8.112, art. 46, § 1º (4.3) | idem | o valor de cada parcela da reposição ao erário não pode ser inferior a dez por cento da remuneração, provento ou pensão (troca: dez → cinco por cento) | NUM | N | E | sim | direta | DC | — |
| D2-R34 | Lei 8.112, art. 41, § 5º (4.3) | idem | nenhum servidor receberá remuneração inferior ao salário mínimo (exigência (b): "Nenhum servidor") | SUJ | N | **C** | não | direta | DC | D2-09 (CF, art. 37, X; outro dispositivo) |
| D2-R35 | Lei 8.112, art. 76 (4.3) | idem | independentemente de solicitação, é pago ao servidor, por ocasião das férias, adicional de um terço da remuneração do período das férias (C com moldura do par da R3, com os E D2-R32, R37 e R39) | APL | S — idem | C | não | direta | CQ | — |
| D2-R36 | Lei 8.112, art. 20, § 4º (4.3) | idem | ao servidor em estágio probatório somente podem ser concedidas as licenças e os afastamentos previstos nos arts. 81, I a IV, 94, 95 e 96, e o afastamento para curso de formação decorrente de aprovação em concurso para outro cargo na Administração Pública Federal (exigência (b): "somente"; nenhum número do estágio probatório; nada do caput, do § 5º nem do Decreto 12.374) | DEF | N | **C** | não | direta | DC | D2-31 (art. 20, caput), D2-36 (art. 20, § 3º) e D2-39 (art. 91): nota (ay) |
| D2-R37 | Lei 8.112, art. 87, caput (4.3) | idem | após cada quinquênio de efetivo exercício, o servidor pode, no interesse da Administração, afastar-se do cargo efetivo, com a respectiva remuneração, por até três meses, para curso de capacitação profissional (troca: três → seis meses) | APL | S — idem | E | sim | direta | CQ | — |
| D2-R38 | Lei 8.112, art. 30 (4.3) | idem | o retorno à atividade do servidor em disponibilidade faz-se mediante aproveitamento obrigatório em cargo de atribuições e vencimentos compatíveis com o anteriormente ocupado (cenário sem órgão do Legislativo) | SIT | N | C | não | direta | CQ | D2-05 (CF, art. 41, § 3º: disponibilidade) e D2-34 (art. 25: reversão): nota (az) |
| D2-R39 | Lei 8.112, art. 77, caput (4.3) | idem, sem a ressalva final | as férias podem ser acumuladas até o máximo de dois períodos, no caso de necessidade do serviço (troca: no caso de necessidade do serviço → a pedido do servidor) | APL | S — idem | E | sim | direta | CQ | — |
| D2-R40 | Lei 8.112, art. 53, caput (4.3) | art. 53, caput (art. 58, caput, como contraste) | a ajuda de custo destina-se a compensar as despesas de instalação do servidor que, no interesse do serviço, passa a ter exercício em nova sede, com mudança de domicílio em caráter permanente (troca: a ajuda de custo → as diárias, a indenização do art. 58) | PAR | N | E | sim | direta | DC | — |
Exigência (b) (seção 2.3): três C com o absoluto que é a letra (D2-R31, R34, R36), aderência direta, sem [TS] (a 3.4 já tem o C-isca D2-35); "Difere de" obrigatório para o art. 20 (D2-R36). Moldura da 3.4 (D2-R32, R35, R37, R39): cena com "servidor de órgão do Poder Legislativo da União"; nenhuma norma interna, carreira ou prática real da Câmara; a moldura não decide o gabarito; as quatro cenas não repetem o mesmo texto até o fecho (L3-3); a troca de número (D2-R32, R37) e a de conceito (D2-R39) variam entre os E com moldura. Reserva da 3.4 (na ordem): Lei 8.112, art. 40; art. 41, § 3º; art. 47; art. 98, § 2º; art. 44, I; art. 97, I (nunca no mesmo simulado que o D2-R32).

**Folha 4.1 — 10 itens (5 C / 5 E), D2-R41 a D2-R50 (todos diretos)**
| id | ponto | base | o que se julga | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D2-R41 | CF, art. 41, § 1º, I (Anexo N do D2, 4.1; compl. 4.1) | art. 41, § 1º, caput e I | o servidor estável perde o cargo em virtude de sentença judicial transitada em julgado (troca: transitada em julgado → ainda sujeita a recurso); sem "só" (L5-2) | APL | S — órgão/servidor do Poder Legislativo da União | E | sim | direta | CQ | D2-04 (3.1: § 1º, III) e D2-R10 (3.1: § 2º): nota (bb) |
| D2-R42 | **CF, art. 5º, LV (ADENDO, seção 11.4.2)** | idem | aos litigantes, em processo judicial ou administrativo, e aos acusados em geral são assegurados o contraditório e a ampla defesa, com os meios e recursos a ela inerentes (cenário: servidor acusado em processo administrativo disciplinar; sem órgão do Legislativo) | SIT | N | C | não | direta | CQ | D2-46 (Lei 8.112, art. 143) e D2-49 (Lei 9.784, art. 2º, X): nota (bc) |
| D2-R43 | Lei 9.784, art. 2º, parágrafo único, IV (4.4) | idem | nos processos administrativos observa-se o critério de atuação segundo padrões éticos de probidade, decoro e boa-fé | DEF | N | C | não | direta | DC | D1-13 e D1-14 (1.1: incisos III e II) |
| D2-R44 | Lei 9.784, art. 2º, parágrafo único, V (4.4) | idem | critério de divulgação oficial dos atos administrativos, ressalvadas as hipóteses de sigilo previstas na Constituição (troca: na Constituição → em regulamento do órgão) | SUJ | N | E | sim | direta | DC | D2-43 (inciso XI) |
| D2-R45 | Lei 9.784, art. 2º, parágrafo único, VII (4.4) | idem | critério de indicação dos pressupostos de fato e de direito que determinarem a decisão | DEF | N | C | não | direta | DC | D2-41 (inciso VI) |
| D2-R46 | CF, art. 41, § 1º, II (4.1; compl. 4.1) | art. 41, § 1º, caput e II | o servidor estável pode perder o cargo mediante processo administrativo em que lhe seja assegurada ampla defesa (sem "só"; cenário sem órgão do Legislativo) | SIT | N | C | não | direta | CQ | D2-04 (inciso III): nota (bb) |
| D2-R47 | Lei 9.784, art. 2º, parágrafo único, XII (4.4) | idem | critério de impulsão, de ofício, do processo administrativo, sem prejuízo da atuação dos interessados (troca: sem prejuízo da atuação dos interessados → vedada a atuação dos interessados); cena "no desempenho de função administrativa" (art. 1º, § 1º, Anexo 4.4), sem afirmar norma interna | APL | S — idem | E | sim | direta | CQ | D2-74 (4.4: art. 61, moldura com função administrativa) |
| D2-R48 | Lei 9.784, art. 2º, parágrafo único, IX (4.4) | idem | critério de adoção de formas simples, suficientes para propiciar adequado grau de certeza, segurança e respeito aos direitos dos administrados (troca: formas simples → formas solenes) | PAR | N | E | sim | direta | DC | D2-R50 (inciso VIII: nota (bd)) |
| D2-R49 | **CF, art. 5º, LIV (ADENDO, seção 11.4.2)** | idem | ninguém será privado da liberdade ou de seus bens sem o devido processo legal ("ninguém" literal) | SUJ | N | C | não | direta | DC | D6-08 (folha 11; menção ao devido processo legal) |
| D2-R50 | Lei 9.784, art. 2º, parágrafo único, VIII (4.4) | idem | critério de observância das formalidades essenciais à garantia dos direitos dos administrados (troca: dos direitos dos administrados → do interesse da Administração); cena como no D2-R47 | APL | S — idem | E | sim | direta | CQ | D2-R48 |
Moldura da 4.1 (D2-R41, R47, R50): cena com "servidor" ou "processo administrativo em órgão do Poder Legislativo da União" (nos itens da Lei 9.784, "no desempenho de função administrativa"); nada sobre norma interna, regimento ou prática real da Câmara; a moldura não decide o gabarito; cenas distintas até o fecho (L3-3). L3-2: o D2-R47 insere "vedada" pela troca; a 4.1 tem C com absoluto literal (D2-R49, "ninguém"). Reserva da 4.1: Lei 9.784, art. 2º, parágrafo único, I (só na falta do adendo, seção 11.4.2, (c)); sem outra reserva com lastro.

#### 11.4.5 Formatos ao fim da leva 5 (folha final de 20; teto 6)
| folha | DEF | SUJ | SIT | NUM | PAR | APL | total |
|---|---|---|---|---|---|---|---|
| 3.3 (canônicos 3/1/2/2/2/0 + leva 2/2/3/2/1/0) | 5 | 3 | 5 | 4 | 3 | 0 | 20 |
| 3.4 (canônicos 3/0/2/2/2/1 + leva 1/1/2/1/1/4) | 4 | 1 | 4 | 3 | 3 | 5 | 20 |
| 4.1 (canônicos 3/0/3/0/2/2 + leva 2/2/2/0/1/3) | 5 | 2 | 5 | 0 | 3 | 5 | 20 |
Maior formato 25% (5 em 20) nas três folhas. Formatos da leva 5: DEF 5, SUJ 5, SIT 7, NUM 3, PAR 3, APL 7. Formatos dos canônicos: D2_v2_1.md, seção 7.

#### 11.4.6 Gabarito, moldura, aderência e conjuntos ao fim da leva 5
- Leva: **16 C / 14 E (53,3%)**; faixa de 30 itens: 12 a 18 C. Folhas: 3.3 10/10 (4/6 + 6/4); 3.4 10/10 (5/5 + 5/5); 4.1 10/10 (5/5 + 5/5).
- Moldura nova: **1 C / 6 E** (D2-R35 C; D2-R32, R37, R39, R41, R47, R50 E). DA: 49/28 → **50/34 (59,5%)** — **meta da D-MOLDURA-CE cumprida na leva 5**, igual à seção 2.2 (25 E novos com moldura ≥ 21; 2 × 50 = 100 ≤ 3 × 34 = 102). Margem: 2 pontos; E com moldura reprovado é reposto na v2 da mesma leva (reserva da mesma folha, mesmo tipo; seção 2.2). Por folha: 3.4 2 C / 3 E (40,0%), 5 com moldura; 4.1 2 C / 3 E (40,0%), 5 com moldura; 3.3 0/0. Cotas da T-122 na 3.4 (3 E) e na 4.1 (3 E) cumpridas; C com moldura da 3.4 em par com E além da cota (R3). Conjunto do D2: 9/4 → **10/10 (50,0%)**.
- Aderência: 30 diretos / 0 parciais. VOLÁTIL 0. REVERIFICAR 0 (nenhuma redação de 2025 ou 2026; Decreto 11.306/2022 e Leis 9.527/1997, 11.784/2008 e MP 2.225-45/2001 são anteriores).
- [TS]: 14 (todos E; nenhum C-isca).
- Abertura × gabarito (seções 7.4.2, 9.3 e 10.2): leva "Considere que" 7 C / 7 E (50,0% de C); declarativos 9 C / 7 E (43,8% de E). Folhas fechadas: 3.3 CQ 4 C / 1 E e DC 6 C / 9 E (60,0% de E); 3.4 CQ 4/5 (44,4% de C) e DC 6/5 (45,5% de E); 4.1 CQ 6/4 (60,0% de C) e DC 4/6 (60,0% de E).
- Absolutos (L3-2): C com absoluto literal: D2-R25 ("somente"), R31 ("para qualquer efeito"), R34 ("Nenhum"), R36 ("somente") e R49 ("ninguém"); E com absoluto inserido: só o D2-R47 ("vedada"), com C literal na mesma folha. Conjunto do D2 (canônicos 13 E / 1 C com absoluto; seção 7 do D2_v2_1.md) passa a ter C com absoluto literal em 7 itens com a leva 4 (D2-R15) e a leva 5.
- Fórmula "Nessa situação, nos termos d…": no D2, contada e informada (orientação: no máximo 7 dos 14 CQ). Fecho "é correto afirmar que": 0 (L4-1). L3-4 e L3-5: nenhum contraste "mas não" / ", e não" e nenhum "mero", "por si só" ou "simples" planejados (o "formas simples" do D2-R48 é letra do inciso IX e não é qualificador minimizador). L5-1: todo E entre 19 e 62 palavras. Seção 10.2, itens 5 e 6: nenhum E nega no fecho a hipótese inteira do cenário; o único SUJ E com ator trocado (D2-R22) usa a autoridade do órgão requisitante, que a fonte menciona.

#### 11.4.7 Sequência (seção 7.3; plano conferido por script antes do despacho)
| escopo | gabarito | [TS] | resultado |
|---|---|---|---|
| 3.3, leva / acumulada (20) | CEECCCECCE / ECEECECCEE·CEECCCECCE | nTTnnnTnnT / TnnTnTTnTn·nTTnnnTnnT | passa (o D2-R21, C, fecha o par de E do fim dos canônicos) |
| 3.4, leva / acumulada (20) | CEECCCECEE / CEECCECCEE·CEECCCECEE | nTTnnnTnTT / nTTnTTnnTn·nTTnnnTnTT | passa |
| 4.1, leva / acumulada (20) | ECCECCEECE / CCCECEECEE·ECCECCEECE | TnnTnnTTnT / nnTTnnTnTT·TnnTnnTTnT | passa (corrida máxima 3 na junção) |
| leva 5 inteira (3.3, 3.4, 4.1) | CEECCCECCE·CEECCCECEE·ECCECCEECE | idem com T nos E | passa (corrida máx. 3; alternância máx. 4) |
Nenhum par de itens com moldura fica em posições vizinhas; os pares (D2-R23, R25), (D2-R21, R27), (D2-R31, R34, R36), (D2-R41, R46), (D2-R42, R49) e (D2-R48, R50) não ficam vizinhos. Mesma regra de troca de posição da seção 8.3.7.

#### 11.4.8 Amostra da gbq-estilo (leva 5)
4 itens (13,3%), designados antes da produção: **D2-R32** (E com moldura do Legislativo, APL, Lei 8.112, art. 97, troca de número); **D2-R47** (E com moldura, APL, Lei 9.784, art. 2º, XII, absoluto inserido "vedada"); **D2-R36** (C da exigência (b), absoluto literal "somente", estágio probatório); **D2-R30** (E, PAR, Lei 6.999, art. 4º, folha sem cópia em cache). Cobre: E com moldura nas duas folhas com cota, o único lote da leva (D2), um C, a 3.3 (leva sem parcial). Rito da seção 9.3, item 6: sobre a v1, em paralelo ao R1; os AJ de estilo vão com os AJ do R1 para a v2 e são conferidos no R2; texto igual pedido pelos dois é aplicado uma vez (seção 11.3). Saída: saida/banco/estilo_DA_reforco_leva5.md.

#### 11.4.9 Notas de simulado previstas para a leva 5 (destino: T-119 e T-123; continuam (a) a (as))
| # | itens | motivo |
|---|---|---|
| (at) | D2-R23 × D2-R25 × D2-27 | Lei 6.999, prazos da requisição (art. 2º, § 1º; art. 3º, caput e § 3º) |
| (au) | D2-R30 × D2-25 | prazo certo nas Secretarias dos TRE × prazo indeterminado do Decreto 10.835, art. 11 |
| (av) | D2-R21 × D2-R24 × D2-23 | direitos e vantagens do requisitado em três normas (Decreto 10.835; Lei 6.999; Lei 9.007) |
| (aw) | D2-R22 × D2-22 | quem pode requisitar × quem disponibiliza a requisição |
| (ax) | D2-R21 × D2-R27 | Decreto 10.835, art. 9º, §§ 4º a 6º |
| (ay) | D2-R36 × D2-31, D2-36 e D2-39 | estágio probatório (Lei 8.112, art. 20, caput, §§ 3º e 4º; art. 91) |
| (az) | D2-R38 × D2-05, D2-34 e D2-R10 | disponibilidade, aproveitamento, reversão e recondução (amplia a (ai)) |
| (ba) | D2-R31 × D2-R06 | incorporação e cômputo de vantagens (Lei 8.112, art. 49, § 1º; CF, art. 37, XIV) |
| (bb) | D2-R41 × D2-R46 × D2-04 | CF, art. 41, § 1º, incisos I, II e III |
| (bc) | D2-R42 × D2-46 e D2-49 | ampla defesa (CF, art. 5º, LV; Lei 8.112, art. 143; Lei 9.784, art. 2º, X) |
| (bd) | D2-R48 × D2-R50 | Lei 9.784, art. 2º, parágrafo único, VIII e IX |
| (be) | D2-R43, R44, R45, R47, R48, R50 com D1-13, D1-14, D1-15, D2-41, D2-43 e D2-49 | mesmo parágrafo único do art. 2º da Lei 9.784: no máximo 2 desses itens por simulado |
| (w) | a leva 5 inteira (ou só itens de reforço) | não forma simulado isolado; entra misturada por folha com os canônicos |
| (x) | os 7 itens com moldura (D2-R32, R35, R37, R39, R41, R47, R50) | contam para o teto de 50% de C com moldura por simulado (D-MOLDURA-CE (c)) |

#### 11.4.10 Despacho (leva 5)
1. **Primeiro, ao qa-normativo-da** (uma instância; agora, sem esperar outra coisa): adendo ao Anexo N do D2, saida/gcb/D2_anexo_N_adendo_<data>.md, linha 1 no formato do CLAUDE.md, com a CF, art. 5º, caput, LIV e LV, transcritos da cópia saida/gcb/normativo_cache/CF_1988_compilada_2026-10-20.txt (d6580cb3…cb51d; linhas 124 e 125), com a URL da Fonte 1 do Anexo, "verificado em 20/10/2026" (data verdadeira; D-FONTE-DATA-ANTERIOR), SHA-256 da cópia, notas de redação do compilado, marca "Edital: núcleo 4.1" e o registro de que o planalto não foi reaberto (rede bloqueada). Nada além desses três dispositivos (D-COMPLEMENTOS). Não é tarefa nova: é o primeiro passo da T-116 para a 4.1 (seção 2.1, regra do lastro "A CONFIRMAR").
2. **Depois, a GCB confere** por script que os trechos do D2-R42 e do D2-R49 (seção 11.4.4) ocorrem 1 vez no adendo e na cópia; conferido, a leva 5 está despachável, sem nova ficha. Sem o adendo, vale a seção 11.4.2, (c).
3. **À gcb-cpp** (sonnet), uma instância. Objeto: leva 5, conforme esta seção 11.4, as seções 1, 7, 8.2 (itens 4 e 7), 9.3, 10.2 e 11.2 e os anexos abaixo. Saída: saida/gcb/DA_reforco_leva5_v1.md, no formato da regra 14 (nomes da seção 7.5), linha 1 `# DA_reforco_leva5_v1.md — T-116 — <data ISO> — gerado por gcb-cpp`. Anexos (lista exaustiva): esta ficha; saida/gcb/D2_anexo_N_mapa_normativo.md (seções 1, 2.3, 3, 4.1, 4.3, 4.4, 4.5, 4.6, 4.7 e 5); o adendo do item 1; saida/gcb/D2_v2_1.md (pontos D2-21 a D2-50, seção 7, e formato dos blocos canônicos) e saida/gcb/D1_v2.md (pontos D1-09 a D1-15), só para os pontos já usados; os arquivos finais das levas 1 a 4 (pontos e modelo de bloco); regras/estilo_banca.md; cópias em saida/gcb/normativo_cache/. A seção 4 do arquivo traz, por script, as contagens da regra 14, abertura × gabarito e fecho × gabarito no D2 (canônicos, leva 4, leva 5, acumulado), a fórmula, absolutos por gabarito (L3-2), extensão fora da faixa (L5-1), o teste da seção 11.4.7 refeito e a moldura acumulada (DA e D2). A gcb-cpp pode trocar um ponto pela reserva da mesma folha, com o motivo no bloco à GCB, nas condições da seção 3.7. O R1 da leva 5 não tem errata a conferir. Nada vai à plataforma nem à candidata. Sem commit.

### 11.5 Riscos e registros
1. 3.3 sem cópia própria em cache: a QA confere a 3.3 só contra o Anexo N do D2; registro de limitação, não bloqueio (seção 11.4.2, (c)). Se a gcb-cqfp entender que algum trecho da 3.3 exige reabertura da fonte, o item vai a "pendente" no parecer, sem reprovação por falta de rede, e a GCB decide na reconciliação.
2. Meta de moldura com margem de 2 pontos na leva 5 (seção 2.2): reposição obrigatória de E com moldura reprovado (reservas da 3.4 e da 4.1, mesmo tipo); na 4.1 não há reserva com lastro além do inciso I do art. 2º, parágrafo único — se um E com moldura da 4.1 for reprovado, a reposição vai para a 3.4 (R4 da T-122) e a reconciliação registra.
3. Conflito de lastro 4.1 × 1.1 (Lei 9.784, art. 2º): a 4.1 usa seis incisos do parágrafo único; o inciso I fica para a 1.1 (leva 12), cuja ficha lista o lastro restante e pede adendo se faltar.
4. Nenhuma tarefa nova (D-COMPLEMENTOS): o adendo da seção 11.4.10, item 1, é passo da T-116. Nenhum gatilho em PARA_PRESIDENCIA.md por esta seção (o gatilho da leva 4 é da reconciliação).

### 11.6 Conferência do adendo da 4.1 (ciclo s16c3)
GCB, 22/10/2026, ficha 11.4.10, item 2; acréscimo antes da última linha. SHA-256 da ficha antes deste acréscimo: 52f80184a6eb1ff3c9340c3b32ce15221b64b32b4cdfebf670fd54096ef9c64a. Script: python3 -I, somente leitura, scratchpad gcb_l5/conf_adendo.py. Objetos conferidos em disco: adendo saida/gcb/D2_anexo_N_adendo_2026-10-22.md (abed6f934ca9d8881e9d2c6944de86a453018e90ee9e2a8ac139d876d1a8af61, do qa-normativo-da) e cópia saida/gcb/normativo_cache/CF_1988_compilada_2026-10-20.txt (d6580cb327147e1beb69ccd09cd930613c06f39e1791b235729930a01cacb51d) — iguais aos declarados.

| item | trecho do plano (cadeia exata; o mesmo da conferência da seção 11.4.2, scratchpad gcb_l4/plan5b.py) | adendo | cópia (linha) | resultado |
|---|---|---|---|---|
| D2-R42 | "aos litigantes, em processo judicial ou administrativo, e aos acusados em geral são assegurados o contraditório e ampla defesa, com os meios e recursos a ela inerentes" | 1 | 1 (l. 125) | CONFERE |
| D2-R49 | "ninguém será privado da liberdade ou de seus bens sem o devido processo legal" | 1 | 1 (l. 124) | CONFERE |

- **Resultado: CONFERE** (2 de 2). O caput do art. 5º, também no adendo, é só contexto (nenhum item da leva 5 o tem como ponto).
- Registro de redação (sem errata da ficha; a coluna "o que se julga" da 11.4.4 é sentido, não redação): na linha do D2-R42 da seção 11.4.4 está "o contraditório e **a** ampla defesa"; essa forma ocorre 0 vez no adendo e na cópia. A letra é "o contraditório e ampla defesa" (adendo, seção 2; cópia, l. 125). A gcb-cpp redige o D2-R42 pelo texto do adendo, não pela coluna da ficha; o R1 da leva 5 confere a letra contra a cópia (D-T116-LEVA4-ACEITE, (c)).
- **Duas datas na coluna Consulta do adendo — decisão da GCB: ficam as duas; ambas são verdadeiras** (cópia verificada em 20/10/2026, D-FONTE-DATA-ANTERIOR; página reaberta, HTTP 200, e conferida em 22/10/2026, preferência da D-T116-LEVA4-ACEITE, (b)). Base de referência: a cópia de 20/10 (l. 124 e 125), que é a que está gravada no repositório e contra a qual o R1 confere; a reabertura de 22/10 é conferência (HTML só no scratchpad do qa-normativo-da, não é base). Na Base do D2-R42 e do D2-R49: URL da Fonte 1 do Anexo, "consulta 20/10/2026 (cópia em cache); página reaberta e conferida em 22/10/2026 (adendo de 22/10/2026)". Não se usa a fórmula "não reaberta … por restrição de rede" nesses dois itens (seria falsa). O registro "planalto não reaberto (rede bloqueada)" pedido na 11.4.10, item 1, não se aplica: a condição (b) da D-T116-LEVA4-ACEITE dá preferência à reabertura, e o adendo a fez.
- **Fato de rede (orquestrador, conferido em 22/10/2026):** o www.planalto.gov.br NÃO está bloqueado neste ambiente; devolve resposta vazia a pedido sem User-Agent e HTTP 200 com User-Agent de navegador (ex.: `curl -A "Mozilla/5.0"`). O adendo confirma (2026-10-22T21:05:35Z, HTTP 200, 1.507.134 bytes). Fica superada, daqui em diante, a frase da 11.4.2 "www.planalto.gov.br está bloqueado neste ambiente" (o texto da 11.4.2 não é alterado; vale este registro).
  - Efeito na regra "Rede" das próximas levas (6 a 12): o planalto.gov.br conta como acessível; pedido ao qa-normativo-da usa User-Agent de navegador, e a reabertura da página tem preferência sobre a cópia em cache; "não reaberta por restrição de rede" só vale com tentativa real que falhou, registrada literalmente (comando, hora, código). A cópia em cache continua base válida quando já gravada com data e hash (D-FONTE-DATA-ANTERIOR). O fato vale só para o www.planalto.gov.br; outros hosts não foram testados. Na leva 5, nada muda na ficha: a 3.3 segue conferida contra o Anexo N do D2 (D-T116-LEVA4-ACEITE, (e); 11.5, item 1), agora como limitação de método, não de rede.
  - **Leitura da GCB sobre a T-120 (f)** (sem alterar TAREFAS.md; decisão do orquestrador/presidencia): a reabertura de 22/10 **não substitui** a T-120 (f), que **fica para janeiro** (4–8/1/2027). Ela atende ao que a (f) supria no presente — já não há dispositivo do adendo tomado "só da cópia por falta de rede" — mas a T-120 é a janela única de reverificação (D-REVERIFICACAO-JAN): reabrir perto da prova para pegar alteração posterior a outubro, como em todos os itens da lista; e o HTML de 22/10 não foi gravado em saida/. Sugestão de registro: a (f) perde o motivo "por falta de rede" e passa a ser conferência de base comum dos três dispositivos (sem VOLÁTIL), como as demais.
- **Leva 5 despachável à gcb-cpp (seção 11.4.10, item 3).** Com o anexo "o adendo do item 1" = saida/gcb/D2_anexo_N_adendo_2026-10-22.md (abed6f93…af61). Sem nova ficha, sem novo gatilho (D-T116-LEVA4-ACEITE, (c)).

## 12. Adendo após a leva 5 (gcb-gerencia, 22/10/2026, ciclo s16c3)
Fonte: reconciliação saida/gcb/DA_reforco_leva5_reconciliacao_2026-10-22.md (seções 4 e 5), pareceres R1 e R2 da gcb-cqfp da leva 5, auditoria de estilo saida/banco/estilo_DA_reforco_leva5.md (seções 4 e 6) e adendo saida/gcb/D2_anexo_N_adendo_2026-10-22.md. Só acréscimo antes da última linha; o texto acima fica como estava (SHA-256 da ficha antes deste adendo: 2e676c62d45487ed5f267f40d8f70d9761e2e67534991aa9564a9550c88a4899, a versão citada no R1, no R2 e no estilo da leva 5, com a seção 11.6). Este adendo prevalece sobre as seções 0 a 11 onde divergir; vale para as levas 6 a 12. Sem commit nem push.

### 12.1 Ids, faixas e núcleo
- Leva 5 sem reprovação e sem substituto: **D2-R21 a D2-R30** (3.3), **D2-R31 a D2-R40** (3.4) e **D2-R41 a D2-R50** (4.1), na ordem da seção 11.4.4; nenhum id vago. As folhas 3.3, 3.4 e 4.1 fecham em 20. O D2 segue em D2-R51.
- **Leva 6 — faixas por folha (corrige a seção 2.1 só nesta leva):** 4.2 = **D2-R51 a D2-R60** (D2-R51 = Lei 8.112, art. 135, exigência (b)); 4.4 = **D2-R61 a D2-R70**; 4.3 = **D2-R71 a D2-R80**. Motivo: a ordem das folhas no arquivo da leva 6 é 4.2, 4.4, 4.3 (seção 12.4.7: com 4.2, 4.3, 4.4 nenhum plano passa o teste da leva inteira), e os ids seguem a ordem do arquivo. A ordem de apresentação na consolidação continua por folha (seção 7.3) e não depende da ordem do arquivo. Leva 7 = D3-R60 a D3-R89; D4 como na seção 7.1; D1 como na seção 9.1; D5 como na seção 2.1.
- Núcleo: os 30 itens da leva 5 false (seção 11.1). Leva 6: a 4.2, a 4.3 e a 4.4 já têm 10 canônicos cada; **nenhum item da leva 6 recebe núcleo** (todos false).

### 12.2 Regras de forma aceitas depois da leva 5 (estilo da leva 5, seção 6)
As regras das seções 1, 7.4, 9.3, 10.2 e 11.2 continuam; estas as completam:
1. **L6-1 — sentido da troca de número (texto da gbq-estilo).** "Em item E cuja troca é um número (prazo, percentual, período ou quantidade), a leva não põe todas as trocas no mesmo sentido. Quando a letra afirma o número como permissão, teto ou piso ('poderá … por', 'por até', 'não pode ser inferior a') e a troca para menor ficaria compatível com a letra, o item afirma o número como valor da regra ('o período de ausência … é de cinco dias', 'o percentual mínimo de cada parcela é de cinco por cento'). Assim, a troca para menor também contradiz a letra. A seção 4 do arquivo da leva lista, por script, o sentido de cada troca de número (para mais ou para menos) e a contagem por leva." Aplicação na leva 6: 5 trocas de número, 3 para menos (D2-R52, D2-R69, D2-R73) e 2 para mais (D2-R54, D2-R65); o D2-R73 afirma o prazo como valor da regra.
2. **L6-2 — absoluto literal que não é a troca (texto da gbq-estilo).** "Absoluto que é letra da fonte e não é o elemento trocado fica no enunciado também em item E ('sem qualquer prejuízo', Lei 8.112, art. 97; D2-R32, AJ-L5-E1). A seção 4 do arquivo da leva conta por gabarito o absoluto literal que não é a troca, ao lado do absoluto inserido (L3-2)." Aplicação na leva 6: E com absoluto literal que não é a troca: D2-R72 ("a qualquer tempo") e D2-R69 ("em qualquer órgão ou instância"); C com absoluto literal: D2-R64 ("somente"), D2-R70 e D2-R71 ("sempre"); nenhum E com absoluto inserido.
3. **Fórmula "Nessa situação, nos termos d…"** (estilo da leva 5, seção 6, à GCB; ficha 7.4.3): no D2, a leva 6 usa a fórmula em no máximo 6 dos 12 itens com "Considere que", no máximo 2 por folha; os demais citam a norma no cenário ou no fim do enunciado.
4. Medida: a reconciliação de cada leva confere L6-1 e L6-2 junto com as regras das seções 7.4, 9.3, 10.2 e 11.2.

### 12.3 Registros da leva 5 que valem para as seguintes
- A coluna "o que se julga" da tabela de pontos é sentido, não redação: número trocado diferente do sugerido, com motivo declarado no bloco à GCB e aceito pela QA, não abre errata da ficha (D2-R32 e D2-R33; reconciliação da leva 5, 4.4).
- Frase verdadeira acrescentada à seção 4 do arquivo da leva e não listada na "Resposta à R1" é registro, sem errata depois do R2 (reconciliação da leva 5, 4.1; como o SHA abreviado da 11.3).
- Nota de simulado marcada "obrigatória" vale com o escopo fixado na reconciliação (reconciliação da leva 5, 4.2).
- Cota da T-122 e antecipação da seção 2.2 são coisas distintas: na 3.4 a cota era 1 E e a 4.1 2 E (saida/banco/moldura_ce_2026-10-20.md, seção 4); os 3 E com moldura por folha vieram da antecipação (registro do R1 sobre a redação da 11.4.6).
- Nenhuma errata pendente de conferência da gcb-cqfp para o R1 da leva 6.

### 12.4 FICHA DA LEVA 6 — despachável (sem adendo de lastro)

#### 12.4.1 Objeto (edital, literal; edital/DA_itens_1_12_P1.md)
- "4.2 Ilícito de direito administrativo disciplinar." — 10 itens, **D2-R51 a D2-R60**; de 10 a 20; exigência (b) (art. 135 = D2-R51).
- "4.4 Processo Administrativo Federal (Lei nº 9.784/1999 e suas alterações)." — 10 itens, **D2-R61 a D2-R70**; de 10 a 20.
- "4.3 Procedimentos disciplinares da administração pública." — 10 itens, **D2-R71 a D2-R80**; de 10 a 20.
Total: 30 (plano da seção 2.1). Saída: saida/gcb/DA_reforco_leva6_v1.md (nomes da seção 7.5); **ordem das folhas no arquivo: 4.2, 4.4, 4.3** (seção 12.1); última linha "FIM DA LEVA 06 — REFORÇO DA". Exemplos hipotéticos, sem norma interna, sistema ou prática real da Câmara.

#### 12.4.2 Lastro, rede e adendo — situação da leva 6
Conferência própria (python3 -I, somente leitura, scratchpad gcb_l5r/plan6.py): o trecho decisivo de cada um dos 30 pontos foi procurado no Anexo N do D2 (b0a54fff…340a), seções 4.3 e 4.4, e nas cópias de normativo_cache/.
- **4.2 e 4.3 — lastro CONFIRMADO** (Anexo N do D2, seção 4.3, Fonte 4; cópia Lei_8112_1990_compilada_2026-10-20.txt, 72f45d30…2efe): 23 trechos dos 20 itens, 1 vez cada no Anexo e na cópia.
- **4.4 — lastro CONFIRMADO** (Anexo N do D2, seção 4.4, Fonte 6; cópia Lei_9784_1999_2026-10-20.txt, f9452916…ae19): 11 trechos dos 10 itens, 1 vez cada no Anexo e na cópia.
- **(a) A leva 6 é despachável já**: o lastro não depende de adendo, e o QA da leva 5 está fechado (R2, última rodada; D-REFORCO-DA). O despacho é ato do orquestrador; a sessão desta reconciliação para no gatilho A (CLAUDE.md), e a leva 6 é despachada no ciclo seguinte, sem nova ficha.
- **(b) Não há adendo do qa-normativo-da para a leva 6.** Todos os pontos são de normas transcritas por inteiro no Anexo N do D2 (Lei 8.112 e Lei 9.784), com cópia em cache, nenhum com redação de 2025 ou 2026 (os dispositivos do plano são redação original, salvo o art. 69-A da Lei 9.784, incluído pela Lei 12.008/2009). Pedir adendo seria complemento sem ordem (D-COMPLEMENTOS).
- **(c) Rede.** O www.planalto.gov.br responde com User-Agent de navegador (fato da seção 11.6; confirmado no adendo de 22/10, no R1 e no R2 da leva 5, HTTP 200). O qa-normativo-da **pode** reabrir as Fontes 4 e 6 (pedido com User-Agent de navegador; comando, hora e código registrados), mas não há pedido a ele nesta leva: a base dos itens é a do Anexo e da cópia, consulta de 20/10/2026 (D-FONTE-DATA-ANTERIOR). A reabertura das páginas pela gcb-cqfp no R1, como na leva 5, é conferência, não base; o HTML fica no scratchpad. Nenhum item ou seção do arquivo afirma "rede bloqueada" ou "não reaberta por restrição de rede".
- Fontes admitidas: só o Anexo N do D2 (seções 1, 2.3, 3, 4.3, 4.4 e 5) e as duas cópias; URL e data da Fonte do Anexo (Fonte 4 Lei 8.112, grafada sem "www", como nas levas 4 e 5; Fonte 6 Lei 9.784). Proibidos: memória, fonte secundária, jurisprudência, base doutrinária.
- **Fora da leva 6:** Lei 8.112, art. 127, IV, e art. 134 ("Vide ADPF nº 418"); art. 137 ("Vide ADIN 2975"); art. 143, §§ 1º e 2º (revogados); art. 169, § 2º (remissão ao "art. 142, § 2º", sentido duvidoso); art. 176 ("simples", L3-5); art. 119 (gêmeo do D2-15); art. 118, § 2º, e art. 120 (acumulação, já em D2-01, D2-03, D2-08, D2-R03 e D2-R19); art. 132, XIII (entrega o D2-55); arts. 116 a 120 como ponto da 4.3; Lei 9.784, arts. 1º (D1-16, D1-20), 2º (4.1 e 1.1), 11 a 17 (reservados à 5.1, leva 7), 42 e 43 (2.2), 50 e 53 a 55 (folha 2.1), 49-A a 49-G (D2-78), 64-A e 64-B (súmula vinculante, efeito de decisão do STF: fora do método do Anexo, seção 5.1); qualquer afirmação sobre conceito doutrinário de ilícito disciplinar (Anexo, seção 3, nota da 4.2).

#### 12.4.3 Pontos já usados (não repetir; anti-gêmeo)
- 4.2 (D2-51 a D2-60): Lei 8.112, art. 132, VII; art. 116, IV; art. 141, I; art. 142, I a III; art. 129, caput; art. 117, VIII; art. 142, § 3º; art. 131, caput; art. 126-A; art. 130, § 2º. Outras folhas e levas: arts. 116, XII e parágrafo único (5.2, leva 3); 120 (3.2, leva 4); 122, caput, §§ 2º e 3º, e 124 (6.3 e 6.4, levas 1 e 2); 125 (D2-47; D3-R31); 126 (D2-42); 128 (D2-44, D2-48); 129, parte final (D2-45); 143, caput (D2-46).
- 4.3 (D2-61 a D2-70): Lei 8.112, art. 147, caput; art. 149, caput; art. 145, II; art. 168, parágrafo único; art. 161, § 2º; art. 175; art. 140; art. 152, caput; art. 169, § 1º; art. 146.
- 4.4 (D2-71 a D2-80): Lei 9.784, art. 65, parágrafo único; art. 54, § 1º; art. 64, parágrafo único; art. 61, caput; art. 19, parágrafo único; art. 49; art. 24, caput; art. 49-A, § 6º, II; art. 59, caput; art. 38, § 2º. Outros lotes: arts. 1º, § 1º e § 2º; 2º; 11 a 15; 42, § 2º; 43; 53; 69.

#### 12.4.4 Pontos de julgamento por item (ordem final dentro de cada folha; a gcb-cpp redige)
Colunas como na seção 11.4.4; código do ponto = dispositivo com a seção do Anexo. Nenhum C leva [TS] (as três folhas já têm o seu C-isca: D2-59, D2-64, D2-72). Todo E leva [TS] com troca real e única de um elemento literal, **salvo o D2-R72** (E sem [TS] e sem campo Troca: o erro está no contraste com outro dispositivo, art. 182, parágrafo único, e não na troca sutil de um elemento; precedentes D2-70 e D2-80, E sem [TS]; necessário ao teste de [TS] da 4.3, seção 12.4.7). Todos os pontos são "núcleo" da folha na seção 3 do Anexo e contam como aderência **direta**.

**Folha 4.2 — 10 itens (4 C / 6 E), D2-R51 a D2-R60 (todos diretos)**
| id | ponto | base | o que se julga (sentido da troca, sem redação) | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D2-R51 | Lei 8.112, art. 135, caput (Anexo N do D2, 4.3) | idem | a destituição de cargo em comissão **exercido por não ocupante de cargo efetivo** será aplicada nos casos de infração sujeita às penalidades de suspensão e de demissão (exigência (b); o elemento "exercido por não ocupante de cargo efetivo" fica no enunciado; D2_D1_GCB_v2, seção 3) | DEF | N | C | não | direta | DC | D2-53 (art. 141, I: quem aplica a demissão); D2-R19 (3.2: art. 120): nota (bk) |
| D2-R52 | Lei 8.112, art. 138 (4.3) | idem | configura abandono de cargo a ausência intencional ao serviço por mais de trinta dias consecutivos (troca: trinta → vinte dias; para menos, incompatível com a letra) | NUM | N | E | sim | direta | DC | D2-67 (art. 140: rito sumário): nota (bl) |
| D2-R53 | Lei 8.112, art. 142, § 2º (4.3) | idem | os prazos de prescrição da lei penal aplicam-se às infrações disciplinares capituladas também como crime (cenário: infração disciplinar também capitulada como crime) | SIT | N | C | não | direta | CQ | D2-54 (art. 142, I a III) e D2-57 (§ 3º): nota (bm) |
| D2-R54 | Lei 8.112, art. 130, § 1º (4.3) | idem | é punido com suspensão de até quinze dias o servidor que, injustificadamente, se recusar a inspeção médica determinada pela autoridade competente (troca: quinze → trinta dias; teto para mais) | APL | S — órgão/servidor do Poder Legislativo da União | E | sim | direta | CQ | D2-60 (§ 2º: conversão em multa): nota (bn) |
| D2-R55 | Lei 8.112, art. 141, IV (inciso III como contraste) (4.3) | art. 141, caput e IV | a destituição de cargo em comissão é aplicada pela autoridade que houver feito a nomeação (troca: → pelo chefe da repartição, ator do inciso III; seção 10.2, item 6) | SUJ | N | E | sim | direta | DC | D2-53 (inciso I): nota (bo) |
| D2-R56 | Lei 8.112, art. 139 (4.3) | idem | inassiduidade habitual é a falta ao serviço, sem causa justificada, por sessenta dias, interpoladamente, durante o período de doze meses | NUM | N | C | não | direta | DC | D2-67: nota (bl) |
| D2-R57 | Lei 8.112, art. 142, § 1º (4.3) | idem | o prazo de prescrição começa a correr da data em que o fato se tornou conhecido (troca: se tornou conhecido → foi praticado) | PAR | N | E | sim | direta | DC | D2-57 (§ 3º: interrupção): nota (bm) |
| D2-R58 | Lei 8.112, art. 132, caput e V (4.3) | idem | incontinência pública e conduta escandalosa, na repartição, é caso de demissão (troca: demissão → suspensão; conceito vizinho, E1) | APL | S — idem | E | sim | direta | CQ | D2-51 (inciso VII): nota (bp) |
| D2-R59 | Lei 8.112, art. 123 (4.3) | idem | a responsabilidade penal abrange os crimes e contravenções imputados ao servidor, nessa qualidade (troca: inclui as infrações disciplinares, objeto da responsabilidade administrativa, art. 124; sem absoluto inserido e sem "mas não") | DEF | N | E | sim | direta | DC | D2-47 (4.1, art. 125) e D3-R31 (6.5, art. 125): nota (bq) |
| D2-R60 | Lei 8.112, art. 136 (art. 132, XI) (4.3) | art. 136; art. 132, XI | a demissão por corrupção implica a indisponibilidade dos bens e o ressarcimento ao erário, sem prejuízo da ação penal cabível (cenário: servidor demitido por corrupção) | SIT | N | C | não | direta | CQ | D2-51 e D2-R58 (outros incisos do art. 132) |
Reserva da 4.2 (na ordem): art. 132, IX (nunca no mesmo simulado que o D2-R58); art. 131, parágrafo único (nunca com o D2-58); art. 116, VIII; art. 118, § 3º; art. 141, III (nunca com o D2-R55); art. 117, XVIII.

**Folha 4.4 — 10 itens (5 C / 5 E), D2-R61 a D2-R70 (todos diretos)**
| id | ponto | base | o que se julga | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D2-R61 | Lei 9.784, art. 20 (art. 18 como contraste) (Anexo N do D2, 4.4) | idem | pode ser arguida a suspeição de autoridade ou servidor que tenha amizade íntima ou inimizade notória com algum dos interessados (par suspeição × impedimento; o trecho da Base mantém a grafia "argüida" da fonte) | PAR | N | C | não | direta | DC | D2-75 (art. 19, parágrafo único: impedimento): nota (bs) |
| D2-R62 | Lei 9.784, art. 45 (4.4) | idem | em caso de risco iminente, a Administração pode motivadamente adotar providências acauteladoras sem a prévia manifestação do interessado | SIT | N | C | não | direta | CQ | D2-73 (art. 64, parágrafo único: gravame no recurso) |
| D2-R63 | Lei 9.784, art. 21 (4.4) | idem | o indeferimento de alegação de suspeição pode ser objeto de recurso, sem efeito suspensivo (troca: sem → com efeito suspensivo) | DEF | N | E | sim | direta | DC | D2-74 (art. 61, caput: recurso sem efeito suspensivo): nota (br) |
| D2-R64 | Lei 9.784, art. 51, § 1º (4.4) | art. 51, caput e § 1º | havendo vários interessados, a desistência ou renúncia atinge somente quem a tenha formulado ("somente" literal) | SIT | N | C | não | direta | CQ | — |
| D2-R65 | Lei 9.784, art. 44 (art. 1º, § 1º, como cenário) (4.4) | idem | encerrada a instrução, o interessado tem o direito de manifestar-se no prazo máximo de dez dias, salvo outro prazo legal (troca: dez → quinze dias; teto para mais); cena "no desempenho de função administrativa", sem afirmar norma interna | APL | S — idem | E | sim | direta | CQ | D2-76 (art. 49: prazo para decidir): nota (bt) |
| D2-R66 | Lei 9.784, art. 56, § 1º (4.4) | idem | o recurso é dirigido à autoridade que proferiu a decisão, que, se não reconsiderar em cinco dias, o encaminha à autoridade superior (troca: → dirigido diretamente à autoridade superior, ator que a fonte menciona) | SUJ | N | E | sim | direta | DC | D2-79 (art. 59: prazo de interposição): nota (bu) |
| D2-R67 | Lei 9.784, art. 66, § 2º (4.4) | idem | os prazos expressos em dias contam-se de modo contínuo (troca: → em dias úteis, conceito que a lei usa em outros prazos, arts. 26, § 2º, 41 e 62); E com ao menos 19 palavras (L5-1), com contexto do processo administrativo federal, sem "apenas" | PAR | N | E | sim | direta | DC | D2-77 (art. 24: prazo supletivo) |
| D2-R68 | Lei 9.784, art. 26, § 4º (4.4) | idem | no caso de interessados indeterminados, desconhecidos ou com domicílio indefinido, a intimação deve ser efetuada por meio de publicação oficial | SIT | N | C | não | direta | CQ | — |
| D2-R69 | Lei 9.784, art. 69-A, caput e I (4.4) | idem | têm prioridade na tramitação, em qualquer órgão ou instância, os procedimentos em que figure como parte ou interessado pessoa com idade igual ou superior a sessenta anos (troca: sessenta → cinquenta e cinco; para menos; "em qualquer órgão ou instância" fica, L6-2) | NUM | N | E | sim | direta | DC | — |
| D2-R70 | Lei 9.784, art. 68 (4.4) | idem | as sanções têm natureza pecuniária ou consistem em obrigação de fazer ou de não fazer, assegurado sempre o direito de defesa ("sempre" literal) | DEF | N | C | não | direta | DC | D2-71 (art. 65: revisão de sanções) |
Reserva da 4.4 (na ordem): art. 30; art. 26, § 2º; art. 57; art. 63, § 2º; art. 48; art. 22, § 2º; art. 40.

**Folha 4.3 — 10 itens (5 C / 5 E), D2-R71 a D2-R80 (todos diretos)**
| id | ponto | base | o que se julga | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D2-R71 | Lei 8.112, art. 165, § 1º (Anexo N do D2, 4.3) | idem | o relatório da comissão será sempre conclusivo quanto à inocência ou à responsabilidade do servidor ("sempre" literal) | DEF | N | C | não | direta | DC | D2-64 (art. 168, parágrafo único: julgamento × relatório) |
| D2-R72 | Lei 8.112, art. 174, caput (art. 182, parágrafo único, como contraste) (4.3) | idem | o processo disciplinar pode ser revisto, a qualquer tempo, a pedido ou de ofício, quando houver fatos novos que justifiquem a inocência do punido ou a inadequação da penalidade (o item põe "justificar o agravamento da penalidade"; **sem [TS]**, ver acima; "a qualquer tempo" fica, L6-2) | DEF | N | E | **não** | direta | DC | D2-66 (art. 175: ônus da prova); D2-71 (Lei 9.784, art. 65): nota (bv) |
| D2-R73 | Lei 8.112, art. 161, § 1º (4.3) | idem | o indiciado é citado para apresentar defesa escrita no prazo de dez dias (troca: dez → cinco dias; para menos, afirmado como valor da regra, L6-1) | NUM | N | E | sim | direta | DC | D2-65 (§ 2º: dois ou mais indiciados, 20 dias): nota (bw) |
| D2-R74 | Lei 8.112, art. 147, parágrafo único (4.3) | idem | o afastamento preventivo pode ser prorrogado por igual prazo, findo o qual cessam os seus efeitos, ainda que não concluído o processo (cenário: afastamento já prorrogado; troca: cessam → continuam a produzir efeitos até a conclusão; sem "sem"/"não" no fecho, seção 10.2, item 5) | SIT | N | E | sim | direta | CQ | D2-61 (caput: medida cautelar, 60 dias): nota (bx) |
| D2-R75 | Lei 8.112, art. 154, parágrafo único (4.3) | idem | se o relatório da sindicância concluir que a infração está capitulada como ilícito penal, a autoridade competente encaminha cópia dos autos ao Ministério Público, independentemente da imediata instauração do processo disciplinar | SIT | N | C | não | direta | CQ | D2-63 (art. 145, II: resultados da sindicância) |
| D2-R76 | Lei 8.112, art. 182, caput (4.3) | idem | julgada procedente a revisão, a destituição do cargo em comissão é convertida em exoneração (par com o art. 135, parágrafo único: exoneração convertida em destituição) | PAR | N | C | não | direta | DC | D2-66 (art. 175): notas (bk) e (bv) |
| D2-R77 | Lei 8.112, art. 172, caput (4.3) | idem | o servidor que responde a processo disciplinar só pode ser exonerado a pedido após a conclusão do processo e o cumprimento da penalidade (troca: após → antes da conclusão do processo; sem "só" e sem verbo de condição necessária, L5-2) | APL | S — idem | E | sim | direta | CQ | D2-70 (art. 146) |
| D2-R78 | Lei 8.112, art. 158, caput (4.3) | idem | o depoimento é prestado oralmente e reduzido a termo, não sendo lícito à testemunha trazê-lo por escrito (cenário: testemunha que pretende entregar depoimento escrito) | SIT | N | C | não | direta | CQ | D2-62 (art. 149: comissão) |
| D2-R79 | Lei 8.112, art. 167, § 2º (4.3) | idem | havendo mais de um indiciado e diversidade de sanções, o julgamento cabe à autoridade competente para a imposição da pena mais grave | PAR | N | C | não | direta | DC | D2-53 (4.2, art. 141, I) |
| D2-R80 | Lei 8.112, art. 164, § 2º (4.3) | idem | para defender o indiciado revel, a autoridade instauradora designa servidor como defensor dativo (troca: → o presidente da comissão, ator dos arts. 156, § 1º, e 161, § 1º) | SUJ | N | E | sim | direta | DC | D2-65 e D2-R73 (art. 161) |
Reserva da 4.3 (na ordem): art. 149, § 2º; art. 156, § 2º; art. 151; art. 179; art. 144, caput; art. 160, caput.
Moldura da leva 6 (D2-R54, R58, R65, R77): cena com "servidor de órgão do Poder Legislativo da União" (4.2 e 4.3) ou "processo administrativo conduzido por órgão do Poder Legislativo da União no desempenho de função administrativa" (4.4; art. 1º, § 1º, só como cenário); nada sobre norma interna, regimento, carreira ou prática real da Câmara; a moldura não decide o gabarito; cenas distintas até o fecho (L3-3), inclusive em relação ao D2-74 e aos D2-R47 e D2-R50 (nota (bt)).

#### 12.4.5 Formatos ao fim da leva 6 (folha final de 20; teto 6)
| folha | DEF | SUJ | SIT | NUM | PAR | APL | total |
|---|---|---|---|---|---|---|---|
| 4.2 (canônicos 3/0/2/3/0/2 + leva 2/1/2/2/1/2) | 5 | 1 | 4 | 5 | 1 | 4 | 20 |
| 4.4 (canônicos 3/0/2/3/1/1 + leva 2/1/3/1/2/1) | 5 | 1 | 5 | 4 | 3 | 2 | 20 |
| 4.3 (canônicos 3/0/2/3/1/1 + leva 2/1/3/1/2/1) | 5 | 1 | 5 | 4 | 3 | 2 | 20 |
Maior formato 25% (5 em 20) nas três folhas. Formatos da leva 6: DEF 6, SUJ 3, SIT 8, NUM 4, PAR 5, APL 4. Formatos dos canônicos: D2_v2_1.md (campo Formato).

#### 12.4.6 Gabarito, moldura, aderência e conjuntos ao fim da leva 6
- Leva: **14 C / 16 E (46,7%)**; faixa de 30 itens: 12 a 18 C. Folhas: 4.2 10/10 (6/4 + 4/6); 4.4 10/10 (5/5 + 5/5); 4.3 10/10 (5/5 + 5/5).
- Moldura nova: **0 C / 4 E** (D2-R54, R58, R65, R77) — as cotas da T-122 (4.2 2 E; 4.3 1 E; 4.4 1 E; saida/banco/moldura_ce_2026-10-20.md, seção 4). DA: 50/34 → **50/38 (56,8%)**, meta da D-MOLDURA-CE mantida (seção 2.2). Por folha: 4.2 2 C / 2 E (50,0%); 4.4 1/1; 4.3 1/1; no máximo 6 com moldura por folha (4, 2, 2). Conjunto do D2: 10/10 → **10/14 (41,7%)**.
- Aderência: 30 diretos / 0 parciais. VOLÁTIL 0. REVERIFICAR 0.
- [TS]: 15 (todos E; o D2-R72 é E sem [TS]; nenhum C-isca).
- Abertura × gabarito (7.4.2, 9.3, 10.2): leva "Considere que" 7 C / 5 E (58,3% de C); declarativos 7 C / 11 E (61,1% de E). Folhas fechadas: 4.2 CQ 5 C / 3 E e DC 5 C / 7 E; 4.4 CQ 5/2 e DC 5/8; 4.3 CQ 4/3 e DC 6/7 — mínimos de 40% cumpridos.
- Absolutos (L3-2; L6-2): seção 12.2, item 2. Nenhum E com absoluto inserido; L3-4 e L3-5: nenhum "mas não" / ", e não", "mero", "por si só" ou "simples" planejados. L4-1: nenhum fecho "é correto afirmar que". L5-1: todo E entre 19 e 62 palavras (atenção ao D2-R67). L5-2: o D2-R77 não usa "só" nem verbo de condição necessária. Seção 10.2, itens 5 e 6: o D2-R74 troca a consequência sem negar com "sem" ou "não"; os SUJ E (D2-R55, R66, R80) usam ator que a fonte menciona.
- Concentração por norma e artigo (informativo; seção 10.3): 4.2 com 4 itens do art. 142 (D2-54, D2-57, D2-R53, D2-R57; nota (bm)); 4.4 com 6 itens de recurso (D2-71, 73, 74, 79; D2-R63, R66).

#### 12.4.7 Sequência (seção 7.3; plano conferido por script antes do despacho; scratchpad gcb_l5r/seq6f.py)
| escopo | gabarito | [TS] | resultado |
|---|---|---|---|
| 4.2, leva / acumulada (20) | CECEECEEEC / ECCCEECECC·CECEECEEEC | nTnTTnTTTn / TnnnTTnTTn·nTnTTnTTTn | passa (corrida máxima 3) |
| 4.4, leva / acumulada (20) | CCECEEECEC / ECCCECCEEE·CCECEEECEC | nnTnTTTnTn / TTnnTnnTTn·nnTnTTTnTn | passa (o D2-R61, C, fecha a corrida EEE dos canônicos) |
| 4.3, leva / acumulada (20) | CEEECCECCE / CEECCECCEE·CEEECCECCE | nnTTnnTnnT / nTTTnTnnTn·nnTTnnTnnT | passa (com o D2-R72 sem [TS]) |
| leva 6 inteira (4.2, 4.4, 4.3) | CECEECEEEC·CCECEEECEC·CEEECCECCE | idem | passa (corrida máx. 3; alternância máx. 4) |
Com a ordem 4.2, 4.3, 4.4 e todo E com [TS], nenhuma combinação dos planos válidos por folha passa o teste da leva inteira; a ordem 4.2, 4.4, 4.3 com o D2-R72 sem [TS] passa (seção 12.1). Nenhum par de itens com moldura fica em posições vizinhas; os pares (D2-R52, R56), (D2-R53, R57), (D2-R61, R63), (D2-R72, R76) e (D2-R73, R80) não ficam vizinhos. Mesma regra de troca de posição da seção 8.3.7.

#### 12.4.8 Amostra da gbq-estilo (leva 6)
5 itens (16,7%), designados antes da produção: **D2-R51** (C da exigência (b), art. 135); **D2-R54** (E com moldura, APL, troca de número para mais); **D2-R65** (E com moldura na 4.4, cena "função administrativa"); **D2-R72** (E sem [TS], erro por contraste com o art. 182, parágrafo único); **D2-R73** (E, NUM, troca para menos afirmada como valor da regra, L6-1). Cobre: E com moldura em duas folhas, as três folhas, um C, a L6-1 nos dois sentidos e o único E sem [TS]. Rito da seção 9.3, item 6: sobre a v1, em paralelo ao R1; texto igual pedido pelos dois é aplicado uma vez (seção 11.3). Saída: saida/banco/estilo_DA_reforco_leva6.md.

#### 12.4.9 Notas de simulado previstas para a leva 6 (destino: T-119 e T-123; continuam (a) a (bj))
| # | itens | motivo |
|---|---|---|
| (bk) | D2-R51 × D2-R76 × D2-38 | destituição de cargo em comissão e exoneração (Lei 8.112, arts. 135, 182 e 35) |
| (bl) | D2-R52 × D2-R56 × D2-67 | abandono de cargo e inassiduidade habitual (arts. 138, 139 e 140) |
| (bm) | D2-R53, D2-R57, D2-54 e D2-57 | art. 142 (incisos e §§ 1º a 3º): no máximo 2 desses itens por simulado |
| (bn) | D2-R54 × D2-60 e D2-63 | suspensão (art. 130, §§ 1º e 2º; art. 145, II) |
| (bo) | D2-R55 × D2-53 | art. 141, IV × I |
| (bp) | D2-R58 × D2-51 e D2-R60 | casos de demissão do art. 132 |
| (bq) | D2-R59 × D2-47 e D3-R31 | responsabilidades civil, penal e administrativa (arts. 123 a 125) |
| (br) | D2-R63 × D2-74 | efeito suspensivo do recurso (Lei 9.784, arts. 21 e 61); a QA diz se é obrigatória |
| (bs) | D2-R61 × D2-75 | suspeição × impedimento (arts. 18 a 21) |
| (bt) | D2-R65 × D2-74, D2-R47 e D2-R50 | cena-tipo "processo administrativo em órgão do Poder Legislativo da União" |
| (bu) | D2-R66 × D2-79 e D2-71 | recurso administrativo (arts. 56, 59 e 65) |
| (bv) | D2-R72 × D2-R76, D2-66 e D2-71 | revisão (Lei 8.112, arts. 174, 175 e 182; Lei 9.784, art. 65) |
| (bw) | D2-R73 × D2-65 e D2-R80 | defesa do indiciado (art. 161, §§ 1º e 2º; art. 164, § 2º) |
| (bx) | D2-R74 × D2-61 | afastamento preventivo (art. 147, caput e parágrafo único) |
| (w) | a leva 6 inteira (ou só itens de reforço) | não forma simulado isolado; entra misturada por folha com os canônicos |
| (x) | os 4 itens com moldura (D2-R54, R58, R65, R77) | contam para o teto de 50% de C com moldura por simulado (D-MOLDURA-CE (c)) |

#### 12.4.10 Despacho (leva 6)
1. **À gcb-cpp** (sonnet), uma instância, no ciclo seguinte ao gatilho A da leva 5 (seção 12.4.2, (a)). Objeto: leva 6, conforme esta seção 12.4, as seções 1, 7, 8.2 (itens 4 e 7), 9.3, 10.2, 11.2, 11.6 (regra "Rede") e 12.2, e os anexos abaixo. Saída: saida/gcb/DA_reforco_leva6_v1.md, no formato da regra 14 (nomes da seção 7.5), linha 1 `# DA_reforco_leva6_v1.md — T-116 — <data ISO> — gerado por gcb-cpp`, folhas na ordem 4.2, 4.4, 4.3. Anexos (lista exaustiva): esta ficha; saida/gcb/D2_anexo_N_mapa_normativo.md (seções 1, 2.3, 3, 4.3, 4.4 e 5); saida/gcb/D2_v2_1.md (pontos D2-51 a D2-80 e formato dos blocos canônicos), só para os pontos já usados; os arquivos finais das levas 1 a 5 (pontos e modelo de bloco); regras/estilo_banca.md; cópias Lei_8112_1990_compilada_2026-10-20.txt e Lei_9784_1999_2026-10-20.txt em saida/gcb/normativo_cache/. A seção 4 do arquivo traz, por script, as contagens da regra 14, abertura × gabarito e fecho × gabarito no D2 (canônicos, levas 4 e 5, leva 6, acumulado), a fórmula, absolutos por gabarito (L3-2 e L6-2), sentido das trocas de número (L6-1), extensão fora da faixa (L5-1), o teste da seção 12.4.7 refeito e a moldura acumulada (DA e D2). A gcb-cpp pode trocar um ponto pela reserva da mesma folha, com o motivo no bloco à GCB, nas condições da seção 3.7. O R1 da leva 6 não tem errata a conferir. Nada vai à plataforma nem à candidata. Sem commit.
2. **À gcb-cqfp** (R1, opus) e **à gbq-estilo** (amostra da 12.4.8), em paralelo, sobre a v1; a gcb-cqfp pode reabrir as Fontes 4 e 6 com User-Agent de navegador, como conferência (seção 12.4.2, (c)).
3. **Ao qa-normativo-da:** nenhum pedido nesta leva.

### 12.5 Riscos e registros
1. Ordem das folhas 4.2, 4.4, 4.3 no arquivo e faixas 4.4 = R61–R70, 4.3 = R71–R80 (seção 12.1): a reconciliação da leva 6 confere ids × folha; a GBQ consolida por itemEdital (seção 7.3).
2. D2-R72 sem [TS]: se a gcb-cqfp entender que há troca sutil de elemento e pedir [TS], o teste de [TS] da 4.3 reprova (seção 12.4.7); a reconciliação registra o desvio, sem efeito no gabarito.
3. Margem da meta de moldura: DA fica em 56,8% depois da leva 6; E com moldura reprovado nesta leva não precisa de reposição para a meta (seção 2.2), mas a cota da folha fica por cumprir e a reconciliação registra (R4 da T-122).
4. Nenhuma tarefa nova (D-COMPLEMENTOS). Nenhum gatilho em PARA_PRESIDENCIA.md por esta seção (o gatilho da leva 5 é da reconciliação).

## 13. Adendo após a leva 6 (gcb-gerencia, 22/10/2026, ciclo s16c4)
Fonte: reconciliação saida/gcb/DA_reforco_leva6_reconciliacao_2026-10-22.md (seções 4 e 5), pareceres R1 e R2 da gcb-cqfp da leva 6 e auditoria de estilo saida/banco/estilo_DA_reforco_leva6.md (seções 4 a 6). Só acréscimo antes da última linha; o texto acima fica como estava (SHA-256 da ficha antes deste adendo: 8a86e4bdb816824cc3e7e0c63991c5bd012021a2b02cbdf160416cce66c0eb6c, a versão citada no despacho, no R1, no R2 e no estilo da leva 6). Este adendo prevalece sobre as seções 0 a 12 onde divergir; vale para as levas 7 a 12. Sem commit nem push.

### 13.1 Ids, faixas e núcleo
- Leva 6 sem reprovação e sem substituto: **D2-R51 a D2-R60** (4.2), **D2-R61 a D2-R70** (4.4) e **D2-R71 a D2-R80** (4.3), na ordem do arquivo (4.2, 4.4, 4.3; seção 12.1); nenhum id vago. As folhas 4.2, 4.4 e 4.3 fecham em 20. O D2 fecha o reforço em D2-R80 (80 itens, como na seção 2.1).
- **Leva 7 — faixas por folha (as da seção 2.1):** 5.1 = **D3-R60 a D3-R69**; 6.1 = **D3-R70 a D3-R79**; 7 = **D3-R80 a D3-R89**; ordem das folhas no arquivo: 5.1, 6.1, 7 (o teste da seção 13.4.7 passa nessa ordem). D4 como na seção 7.1; D1 como na seção 9.1; D5 como na seção 2.1.
- Núcleo: os 30 itens da leva 6 ficam false (seção 12.1). Leva 7: a 5.1, a 6.1 e a 7 já têm 10 canônicos cada; **nenhum item da leva 7 recebe núcleo** (todos false).

### 13.2 Regras de forma aceitas depois da leva 6 (estilo da leva 6, seção 6)
As regras das seções 1, 7.4, 9.3, 10.2, 11.2 e 12.2 continuam; estas as completam:
1. **L7-1 — valor da troca de número igual ao da mesma figura em outro rito (texto da gbq-estilo).** "Em item E cuja troca é um número, o valor posto pelo item não é o valor que a mesma norma dá à mesma figura (mesmo ato, mesmo sujeito) em outro rito ou regime. Exemplo: o prazo de defesa escrita do indiciado é de dez dias no inquérito (Lei 8.112, art. 161, § 1º) e de cinco no procedimento sumário (art. 133, § 2º). Se a troca usar esse valor, o enunciado nomeia o rito da letra por um elemento que só ele tem ('na fase de inquérito administrativo'; D2-R73, AJ-L6-E1). Valor igual ao de outra figura da mesma lei é admitido como conceito vizinho (D2-R65: quinze dias, art. 42). A seção 4 do arquivo da leva lista, por script, para cada troca de número, as outras ocorrências do valor posto na cópia da norma e a figura a que cada uma se refere." Aplicação na leva 7: uma troca de número, D3-R75 (Lei 4.619, art. 6º: "uma quinta parte" → "um terço", para mais, teto "não excederá"); "terço" não ocorre na Lei 4.619. Na folha 7 (Lei 8.429, sem cópia em normativo_cache/), a lista da seção 4 sai do Anexo N do D3, seção 4.9.
2. **L7-2 — moldura e fórmula (texto da gbq-estilo).** "Nos lotes em que o item com moldura é de preferência E, a fórmula 'Nessa situação, nos termos d…' não fica concentrada nos itens com moldura. Em cada leva, no máximo metade dos E com moldura usa a fórmula, e os demais citam a norma no cenário ou de outro modo ('segundo …', 'conforme …', 'a Lei … prevê'). A seção 4 do arquivo da leva conta moldura × fórmula × gabarito, por lote e no acumulado (D2, levas 4 a 6: moldura com fórmula 0 C / 8 E; fórmula sem moldura 7 C / 1 E)." Aplicação na leva 7: 2 E com moldura; só o D3-R77 usa a fórmula; o D3-R85 cita a lei de outro modo. A seção 4 conta também o D3 (levas 1 a 3 e 7).
3. **L7-3 — restritivo literal em E, por marcador (texto da gbq-estilo).** "A contagem de absolutos da seção 4 do arquivo da leva sai por marcador, e não só por classe. Quando um restritivo literal ('somente', 'sempre') aparecer só em C no lote acumulado, a leva traz, se a fonte permitir, ao menos um E em que esse restritivo é letra da fonte e não é o elemento trocado (L6-2). D2, levas 4 a 6: 'sempre' 3 C / 0 E; 'somente' 3 C / 0 E; 'qualquer' 1 C / 3 E." Aplicação na leva 7 (contagem da GCB sobre as seções 1 das levas 1 a 4, D3-R01 a D3-R59): "somente" 2 C / 3 E, "sempre" 0 / 0 — sem gatilho no D3; ainda assim a leva 7 põe "somente" literal em C (D3-R79) e em E fora da troca (D3-R82).
4. **E sem [TS] (registro do D2-R72, R1, seção 2; estilo, seção 2).** E sem [TS] só nos mecanismos em que não há troca sutil de um elemento: E3 por contraste com outro dispositivo, E5 (segmento acessório falso) ou E6 (generalização), declarado na ficha da leva e nunca em E1 ou E2 (estilo_banca, seção 5.1). Aplicação na leva 7: D3-R81 e D3-R82 (E5), exigidos pelo teste de [TS] da folha 7 (seção 13.4.7).
5. Medida: a reconciliação de cada leva confere L7-1 a L7-3 e o item 4 junto com as regras das seções 7.4, 9.3, 10.2, 11.2 e 12.2.

### 13.3 Registros da leva 6 que valem para as seguintes
- Mecanismo na fronteira E2/E3 de E sem [TS] fica como declarado, quando a QA não pede [TS]: o campo não vai ao pacote.json e a reclassificação mudaria só contagens (reconciliação da leva 6, 4.1).
- Nota marcada "obrigatória" depois do R2 vale com o escopo fixado na reconciliação (leva 6: (bw) obrigatória só para D2-R73 × D2-65; reconciliação da leva 6, 4.3, item 3).
- Acréscimo de contexto pedido por AJ (D2-R73, "na fase de inquérito administrativo") pode ficar fora da coluna Base quando o ponto julgado continua o do dispositivo citado e o acréscimo tem lastro no mesmo Anexo (R2, seção 8, item 2).
- SHA abreviado com número diferente de caracteres, valor correto: registro, sem errata (como na seção 11.3).
- Nenhuma errata pendente de conferência da gcb-cqfp para o R1 da leva 7.

### 13.4 FICHA DA LEVA 7 — despachável depois do adendo de lastro da 5.1 e da 6.1 (seção 13.4.2)

#### 13.4.1 Objeto (edital, literal; edital/DA_itens_1_12_P1.md)
- "5.1 Discricionário, hierárquico, disciplinar, regulamentar e de polícia." — 10 itens, **D3-R60 a D3-R69**; de 10 a 20.
- "6.1 Responsabilidade civil do Estado no direito brasileiro." — 10 itens, **D3-R70 a D3-R79**; de 10 a 20.
- "7 Improbidade Administrativa (Lei nº 8.429/1992 e suas alterações)." — 10 itens, **D3-R80 a D3-R89**; de 10 a 20.
Total: 30 (plano da seção 2.1). Saída: saida/gcb/DA_reforco_leva7_v1.md (nomes da seção 7.5); ordem das folhas no arquivo: 5.1, 6.1, 7; última linha "FIM DA LEVA 07 — REFORÇO DA". Exemplos hipotéticos, sem norma interna, sistema ou prática real da Câmara.

#### 13.4.2 Lastro, rede e adendo — situação da leva 7
Conferência própria (python3 -I, somente leitura, scratchpad gcb_l6r/plan7b.py e seq.py): o trecho decisivo de cada um dos 30 pontos foi procurado no Anexo N do D3 (2ef58f9b…1df), no adendo do D3 (bbfd3eed…a797) e nas cópias de saida/gcb/normativo_cache/; os pontos já usados vêm do pacote.json v1.13 (canônicos de todas as folhas de DA) e dos arquivos finais das levas 1 a 6.
- **7 — lastro CONFIRMADO** (Anexo N do D3, seção 4.9, Lei 8.429 integral; Fonte 1): 12 trechos dos 10 itens, 1 vez cada no Anexo. Sem cópia da Lei 8.429 em normativo_cache/: a conferência é trecho × linha do Anexo, como na 3.3 da leva 5 (limitação de método, seção 11.4.2 (c)); a gcb-cqfp pode reabrir a Fonte 1 como conferência. Fora: os 28 revogados, os 9 vetados (art. 17-A) e todo dispositivo com "(Vide ADI 7042/7043/7156/7236)" (Anexo, seção 2.2; T-120 (e)); nenhum item afirma efeito de decisão do STF (Anexo, seção 5.1).
- **5.1 — lastro CURTO sem adendo.** Pontos diretos com lastro literal ainda não usados (Anexo N do D3, seções 4.4, 4.6 e 4.7): Lei 9.784, art. 13, I e III, art. 14, caput e § 1º (outros elementos que não a ressalva do D3-02), art. 17; CF, art. 84, VI, b, e parágrafo único (dois pontos); CTN, art. 78, caput (elemento não usado pelo D3-03) — **9 pontos diretos para 10 itens, sem reserva direta**. Já usados: Lei 9.784, arts. 11, 12, caput, 13, II, 14, §§ 2º e 3º, e 15 (D1-38 a D1-43, folha 2.1), art. 12, parágrafo único, 14, § 1º (ressalva), e 15 (D3-01, D3-02, D3-08); CTN, art. 78, caput e parágrafo único (D3-03, D3-04, D3-11); CF, art. 84, IV e VI, a (D3-05, D3-06), art. 49, V (D3-07, D3-13, D3-18). "Discricionário" e "disciplinar" não têm dispositivo no recorte do Anexo (seção 3; alerta 4).
- **6.1 — lastro INSUFICIENTE sem adendo.** O Anexo N do D3 dá à 6.1 só a CF, art. 37, § 6º, o CC, art. 43, e a CF, art. 5º, XXV (seção 3), e os dois primeiros estão esgotados pelos canônicos das folhas 6.1 a 6.5 (D3-21 a D3-23, D3-25, D3-28, D3-30, D3-32 a D3-36, D3-38, D3-40, D3-41, D3-49, D3-51, D3-52, D3-54, D3-58, D3-59, D3-68, D3-70 e D3-81); o adendo do D3 não mapeou a 6.1 (o Adendo 2 tratou só da 5.2 e da 6.2). Ponto direto livre: **1** (CF, art. 5º, XXV, indenização "ulterior"; D3-R74). Os dispositivos de regresso e prescrição já transcritos (Lei 4.619, arts. 1º, caput, e 3º; adendo do D3, 4.8) estão mapeados a outras folhas, como indiretos.
- **(a) A leva 7 NÃO é despachável já.** Fica despachável à gcb-cpp assim que o adendo do qa-normativo-da estiver gravado e a GCB conferir, por script, que os 11 trechos do plano que dependem dele (D3-R68, D3-R69, D3-R70 (2), D3-R71, D3-R72, D3-R75, D3-R76, D3-R77, D3-R78 e D3-R79) ocorrem 1 vez no adendo e na cópia, conferir o mapa do D3-R73 e fixar a aderência dos itens da 6.1 pelo mapa do adendo (seção 13.6, sem nova ficha nem novo gatilho). A folha 7 não depende do adendo, mas a leva sai inteira (seção 1, regra 15; precedente da leva 5).
- **(b) Depende de adendo do qa-normativo-da, com escopo fechado.** Arquivo: saida/gcb/D3_anexo_N_adendo_<data ISO>.md (novo; os anexos e o adendo de 20/10 ficam como estão). Convenção da seção 4 do Anexo N do D3 (texto, redação, vigência, consulta, observação "Edital: núcleo/compl. 5.1 ou 6.1"); mapa folha → pontos com pertinência direta/indireta, como na seção 3 do adendo do D3. Nada além disto (D-COMPLEMENTOS):
  - **Folha 5.1 — transcrição nova:** CF/1988, art. 84, caput (contexto), II e XXV; art. 87, caput (contexto) e parágrafo único, caput, I, II e IV. URL: https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm (Fonte 4 do Anexo N do D3; Fonte A1 do adendo do D3). Cópia de 20/10/2026: CF_1988_compilada_2026-10-20.txt (d6580cb3…cb51d), linhas 1036, 1038, 1063, 1088 a 1091 e 1093.
  - **Folha 6.1 — transcrição nova:** Código Civil, arts. 40, 41 (caput, I a V e parágrafo único) e 42 — https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm (Fonte 5; A2; cópia Lei_10406_2002_CodigoCivil_compilada_2026-10-20.txt, 97e0ffaa…a828, linhas 116 a 124); CF/1988, art. 136, caput (contexto), § 1º, caput e II — URL da CF acima (cópia, linhas 1620, 1621 e 1626); Lei 4.619/1965, art. 4º (caput, §§ 1º e 2º) e art. 6º — http://www.planalto.gov.br/ccivil_03/leis/1950-1969/l4619.htm (A8; cópia Lei_4619_1965_2026-10-20.txt, b91ef03d…082f); Decreto 20.910/1932, arts. 2º a 10 — https://www.planalto.gov.br/ccivil_03/decreto/antigos/d20910.htm (A10; cópia Decreto_20910_1932_2026-10-20.txt, a8a216f2…818a).
  - **Folha 6.1 — só mapeamento (sem nova transcrição):** CF, art. 5º, XXV (Anexo N do D3, 4.1); Lei 4.619, arts. 1º, caput, e 3º (adendo do D3, 4.8).
  - Rede (ficha 11.6; D-T120F-REDACAO): pedido ao www.planalto.gov.br com User-Agent de navegador; a reabertura tem preferência sobre a cópia; comando, hora (UTC), código HTTP, bytes e SHA-256 registrados; texto comparado com a cópia de 20/10/2026. "Não reaberta por restrição de rede" só com tentativa real que falhou, registrada literalmente; a cópia gravada com data e hash continua base válida (D-FONTE-DATA-ANTERIOR). Dispositivo com redação de 2025 ou 2026 leva REVERIFICAR (seção 1, regra 5); nas linhas citadas da cópia de 20/10/2026 não há nota de 2025 ou 2026 (conferido por script; o CC, art. 41, IV, tem a nota da Lei 11.107/2005).
- **(c) Folha abaixo de 20 por falta de lastro:** com o adendo no escopo acima, **nenhuma** (a 5.1 fica com 5 pontos de reserva, 3 deles diretos; a 6.1, com 6). Sem o adendo: **a 6.1 fica abaixo de 20** (1 ponto direto livre e 2 indiretos já transcritos: a folha chegaria a 13, e a leva teria de ser refeita com nova ficha); a 5.1 fecha em 20 com 9 diretos e 1 item da reserva cruzada (Lei 8.112, art. 141, II, Anexo N do D2, 4.3; aderência parcial), sem reserva; a 7 fecha em 20. Na 6.1, se a gcb-cqfp recusar a pertinência dos pontos indiretos do adendo, a folha fica abaixo e a reconciliação registra (seção 2.1, regra do lastro "A CONFIRMAR"); o piso de 10 diretos já está cumprido pelos 10 canônicos.
- Fontes admitidas: só o Anexo N do D3 (seções 1, 2, 3, 4.1, 4.4, 4.6, 4.7, 4.9 e 5), o adendo do D3 (seções 1, 4.8 e 5.2), o adendo novo e as cópias citadas; para a reserva cruzada da 5.1, o Anexo N do D2 (seção 4.3). URL e data da Fonte do Anexo ou do adendo. Proibidos: memória, fonte secundária, jurisprudência, base doutrinária.
- **Fora da leva 7:** CF, art. 37, § 6º, e CC, art. 43 (esgotados; acima); Lei 9.784, arts. 11, 12, 13, II, 14, §§ 2º e 3º, e 15 (folha 2.1 e canônicos da 5.1); CF, art. 49, V; CTN, art. 78, parágrafo único; Lei 4.717, art. 2º (5.2); CF, art. 5º, XXIV e LXXV, Lei 9.494, art. 1º-C, Decreto 9.830, art. 14, CC, arts. 932 a 950 (6.2); Decreto 20.910, art. 1º, Lei 4.619, arts. 1º, parágrafo único, 2º e 5º, Lei 8.112, arts. 121 a 126 (6.4 e 6.5); LINDB, art. 28 (gêmeo do D1-57); Lei 8.112, art. 116, IV (D2-52) e art. 127, IV ("Vide ADPF nº 418"); Lei 8.429: revogados, vetados, dispositivos com "(Vide ADI …)", art. 1º, § 3º, art. 10, § 2º, e art. 11, § 5º ("mero"/"mera", L3-5), e os pontos dos canônicos (art. 3º, caput; art. 9º, caput; art. 10, caput; art. 11, XI e § 4º; art. 14, § 2º; art. 17-B, § 1º, II; art. 17-C, § 1º; art. 20, caput; art. 23, caput); qualquer conceito doutrinário de poder discricionário, de poder disciplinar ou de teorias da responsabilidade (risco administrativo, risco integral, evolução histórica).

#### 13.4.3 Pontos já usados (não repetir; anti-gêmeo)
- 5.1 (D3-01 a D3-10): Lei 9.784, art. 12, parágrafo único; art. 14, § 1º (ressalva de exercício); art. 15 (com o art. 12, caput, como contraste); CTN, art. 78, caput (conceito; segurança, ordem, propriedade e direitos) e parágrafo único (processo legal); CF, art. 84, IV, e VI, a; art. 49, V; D3-09 e D3-10 BASE DOUTRINÁRIA (disciplinar × polícia; controle do ato discricionário). Outras folhas: Lei 9.784, arts. 11, 12, caput, 13, II, 14, §§ 2º e 3º, e 15 (D1-38 a D1-43, folha 2.1); CTN, art. 78, parágrafo único (D3-11, 5.2); CF, art. 49, V (D3-13, D3-18, 5.2).
- 6.1 (D3-21 a D3-30): CF, art. 37, § 6º (sujeitos; concessionária; "danos" sem restrição; PJ de direito público responde); CF, art. 5º, XXV ("se houver dano"); CC, art. 43 (sem prestadoras privadas; PJ de direito público interno responde); BASE DOUTRINÁRIA: risco integral × administrativo, evolução histórica, natureza objetiva (D3-26, D3-27, D3-29). Outras folhas: CF, art. 37, § 6º, e CC, art. 43 (6.2 a 6.5, lista da seção 13.4.2); Lei 4.619, art. 1º, parágrafo único, art. 2º e art. 5º (D3-R23, D3-R24, D3-R36); Decreto 20.910, art. 1º (D3-R22); CF, art. 5º, XXIV e LXXV (D3-R53, D3-R50, D3-R59).
- 7 (D3-71 a D3-80): Lei 8.429, art. 3º, caput; art. 9º, caput; art. 10, caput; art. 11, XI e § 4º; art. 14, § 2º; art. 17-B, § 1º, II; art. 17-C, § 1º; art. 20, caput; art. 23, caput. Nenhum outro item de DA usa a Lei 8.429 (pacote.json v1.13; levas 1 a 6).

#### 13.4.4 Pontos de julgamento por item (ordem final dentro de cada folha; a gcb-cpp redige)
Colunas como na seção 12.4.4; código do ponto = dispositivo com a seção do Anexo ou do adendo. Nenhum C leva [TS] (as três folhas já têm o seu C-isca: D3-02, D3-22, D3-76). Todo E leva [TS] com troca real e única de um elemento literal, **salvo o D3-R81 e o D3-R82** (E5, segmento acessório falso, sem [TS] e sem campo Troca; seção 13.2, item 4; necessários ao teste de [TS] da folha 7, seção 13.4.7). Aderência: na 5.1 e na 7, todos **diretos** (núcleo ou compl. da folha na seção 3 do Anexo; na 5.1, os dois do adendo conforme o mapa dele); na 6.1, direta no D3-R74 e **a fixar pelo mapa do adendo** nos demais (direta se "núcleo/compl. 6.1"; parcial se indireta — conta para a meta, só vai a simulado diagnóstico, D-ADERENCIA; o piso de 10 diretos está cumprido pelos canônicos).

**Folha 5.1 — 10 itens (5 C / 5 E), D3-R60 a D3-R69 (todos diretos)**
| id | ponto | base | o que se julga (sentido da troca, sem redação) | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D3-R60 | Lei 9.784, art. 13, caput e III (Anexo N do D3, 4.7) | idem | as matérias de competência exclusiva do órgão ou autoridade não podem ser objeto de delegação (cenário: autoridade que pretende delegar matéria de sua competência exclusiva) | SIT | N | C | não | direta | CQ | D1-40 (2.1, art. 13, II); D3-01 (art. 12, parágrafo único): nota (ce) |
| D3-R61 | Lei 9.784, art. 13, caput e I (4.7) | idem | a edição de atos de caráter normativo não pode ser objeto de delegação (troca: não podem → pode ser delegada, se não houver impedimento legal) | DEF | N | E | sim | direta | DC | D1-40: nota (ce) |
| D3-R62 | Lei 9.784, art. 14, caput (4.7) | idem | o ato de delegação e a sua revogação devem ser publicados no meio oficial | DEF | N | C | não | direta | DC | D1-41 (§ 2º); D3-02 (§ 1º): nota (cf) |
| D3-R63 | Lei 9.784, art. 14, § 1º (4.7) | idem | o ato de delegação especifica, entre outros elementos, a duração e os objetivos da delegação e o recurso cabível (cenário: autoridade que edita ato de delegação; sem a ressalva de exercício, ponto do D3-02) | SIT | N | C | não | direta | CQ | D3-02 (mesmo parágrafo, outro elemento): nota (cf) |
| D3-R64 | Lei 9.784, art. 17 (4.7) | idem | inexistindo competência legal específica, o processo administrativo é iniciado perante a autoridade de menor grau hierárquico para decidir (troca: menor → maior grau hierárquico) | PAR | N | E | sim | direta | DC | D3-08 (art. 15); D1-43: nota (cg) |
| D3-R65 | CF, art. 84, VI, b (4.4) | idem | o Presidente dispõe, mediante decreto, sobre extinção de funções ou cargos públicos quando vagos (cenário: decreto que extingue cargos ocupados; troca: quando vagos → ainda que ocupados, afirmado como autorizado pela CF; fórmula admitida, a única da folha) | SIT | N | E | sim | direta | CQ | D3-05 (alínea a): nota (ch) |
| D3-R66 | CF, art. 84, parágrafo único (4.4) | idem, sem os incisos | o Presidente pode delegar atribuições aos Ministros de Estado, ao Procurador-Geral da República ou ao Advogado-Geral da União, que observarão os limites traçados nas delegações (o enunciado **não** lista os incisos delegáveis) | SUJ | N | C | não | direta | DC | D3-06: nota (ci) |
| D3-R67 | CF, art. 84, parágrafo único (inciso IV como contraste; alerta 6 do Anexo) (4.4) | idem | as atribuições delegáveis são as dos incisos VI, XII e XXV, primeira parte; a de expedir decretos e regulamentos para a fiel execução das leis (inciso IV) não está entre elas (troca: o item afirma delegável aos Ministros a do inciso IV; rol fechado citado como tal, regra 8) | PAR | N | E | sim | direta | DC | D3-06 (inciso IV, C): nota (ci) |
| D3-R68 | CF, art. 84, caput e II (**adendo**, 13.4.2) | idem | compete privativamente ao Presidente exercer, com o auxílio dos Ministros de Estado, a direção superior da administração federal (troca: atribui a direção superior aos Ministros de Estado, com o auxílio do Presidente; atores da fonte, seção 10.2, item 6) | SUJ | N | E | sim | direta | DC | D3-R66, D3-R69: nota (cj) |
| D3-R69 | CF, art. 87, parágrafo único, II (**adendo**) | idem | compete ao Ministro de Estado expedir instruções para a execução das leis, decretos e regulamentos | DEF | N | C | não | direta | DC | D3-06 (art. 84, IV): nota (cj) |
Reserva da 5.1 (na ordem): CF, art. 87, parágrafo único, I (adendo); art. 87, parágrafo único, IV (adendo); CTN, art. 78, caput — "ao exercício de atividades econômicas dependentes de concessão ou autorização do Poder Público" (Anexo, 4.6; elemento não usado pelo D3-03); Lei 8.112, art. 141, II (Anexo N do D2, 4.3; aderência parcial); Lei 8.112, art. 127, caput, I a III, V e VI (Anexo N do D2, 4.3; parcial; nunca o inciso IV). Sem o adendo: o D3-R68 passa ao art. 141, II (E, [TS], parcial) e o D3-R69 ao CTN, art. 78, caput (C, DEF, direto), com o teste da seção 13.4.7 refeito pela gcb-cpp (mesmo gabarito e [TS] por posição).

**Folha 6.1 — 10 itens (6 C / 4 E), D3-R70 a D3-R79 (aderência: D3-R74 direta; os demais pelo mapa do adendo)**
| id | ponto | base | o que se julga | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D3-R70 | CC, art. 41, caput e IV (**adendo**; art. 43 no Anexo N do D3, 4.5) | CC, art. 41, caput e IV | as autarquias, inclusive as associações públicas, são pessoas jurídicas de direito público interno (sujeitos do art. 43) | DEF | N | C | não | adendo | DC | D3-25 e D3-30 (art. 43): nota (ck) |
| D3-R71 | CF, art. 136, § 1º, caput e II (**adendo**) | idem | no estado de defesa, na ocupação e uso temporário de bens e serviços públicos na hipótese de calamidade pública, a União responde pelos danos e custos decorrentes (cenário: decreto de estado de defesa com ocupação temporária; sem menção ao Congresso) | SIT | N | C | não | adendo | CQ | D3-24 (art. 5º, XXV) e D3-28 (art. 37, § 6º): nota (co) |
| D3-R72 | CC, art. 42 (art. 41 como contraste) (**adendo**) | idem | os Estados estrangeiros são pessoas jurídicas de direito público externo (troca: externo → interno, alcançados pelo art. 43) | PAR | N | E | sim | adendo | DC | D3-R70: nota (ck) |
| D3-R73 | Lei 4.619, art. 1º, caput (adendo do D3, 4.8; mapa à 6.1 no adendo novo) | idem | os Procuradores da República são obrigados a propor ação regressiva contra os funcionários declarados culpados por lesões que a Fazenda Nacional seja condenada judicialmente a reparar (cenário: condenação da União por dano causado por servidor culpado) | SIT | N | C | não | adendo | CQ | D3-R23, D3-R24: nota (cm) |
| D3-R74 | CF, art. 5º, XXV (Anexo N do D3, 4.1; alerta 2) | idem | na requisição por iminente perigo público, a indenização ao proprietário é ulterior, se houver dano (troca: ulterior → prévia, conceito vizinho do art. 5º, XXIV) | PAR | N | E | sim | direta | DC | D3-24 ("se houver dano"): nota (cl), **obrigatória** |
| D3-R75 | Lei 4.619, art. 6º (**adendo**) | idem | o desconto em folha da liquidação do que o funcionário estável deve à Fazenda não excede uma quinta parte do vencimento ou remuneração (troca: uma quinta parte → um terço; teto, para mais; L6-1, L7-1) | NUM | N | E | sim | adendo | DC | D3-R73: nota (cm) |
| D3-R76 | Decreto 20.910, art. 6º (**adendo**) | idem | o direito à reclamação administrativa sem prazo fixado em lei prescreve em um ano a contar do ato ou fato de que se originar | NUM | N | C | não | adendo | DC | D3-R22 (art. 1º: cinco anos): nota (cn) |
| D3-R77 | Decreto 20.910, art. 4º, caput (**adendo**) | idem | não corre a prescrição durante a demora da repartição no estudo, no reconhecimento ou no pagamento da dívida considerada líquida (cenário: particular que requereu a órgão do Poder Legislativo da União o pagamento de dívida líquida; troca: não corre → corre normalmente; fórmula admitida, L7-2) | APL | S — órgão/servidor do Poder Legislativo da União | E | sim | adendo | CQ | D3-R22: nota (cn) |
| D3-R78 | Lei 4.619, art. 4º, caput (**adendo**) | idem | a competência para iniciar a ação regressiva cabe ao Procurador lotado no Estado em que haja corrido o processo judicial cuja decisão contra a Fazenda transitou em julgado | SUJ | N | C | não | adendo | DC | D3-R73: nota (cm) |
| D3-R79 | Decreto 20.910, art. 8º (**adendo**) | idem | a prescrição somente pode ser interrompida uma vez ("somente" literal; L6-2, L7-3) | NUM | N | C | não | adendo | DC | D3-R76, D3-R77: nota (cn) |
Reserva da 6.1 (na ordem): Decreto 20.910, art. 9º; art. 3º; art. 4º, parágrafo único; Lei 4.619, art. 3º (adendo do D3, 4.8; A6.3-15); CC, art. 41, parágrafo único; CC, art. 40.

**Folha 7 — 10 itens (4 C / 6 E), D3-R80 a D3-R89 (todos diretos)**
| id | ponto | base | o que se julga | form. | moldura | gab. | [TS] | ader. | abert. | difere de |
|---|---|---|---|---|---|---|---|---|---|---|
| D3-R80 | Lei 8.429, art. 2º, caput (Anexo N do D3, 4.9) | idem | é agente público, para a lei, também quem exerce mandato, cargo, emprego ou função ainda que transitoriamente ou sem remuneração (troca: "ainda que … sem remuneração" → "desde que remunerado"; um elemento) | SUJ | N | E | sim | direta | DC | D3-80 (art. 3º, caput): nota (cs) |
| D3-R81 | Lei 8.429, art. 8º (4.9) | idem | o sucessor ou o herdeiro está sujeito apenas à obrigação de reparar o dano até o limite da herança ou do patrimônio transferido (cenário: herdeiro de quem causou dano ao erário; o item acrescenta segmento acessório falso, "sujeitando-se também à multa civil"; E5, **sem [TS]**) | SIT | N | E | **não** | direta | CQ | D3-R18 (6.4; Lei 8.112, art. 122, § 3º): nota (cp) |
| D3-R82 | Lei 8.429, art. 12, § 9º (4.9) | idem | as sanções do art. 12 somente podem ser executadas após o trânsito em julgado da sentença condenatória (o item acrescenta exceção falsa, "salvo a multa civil, executável desde a sentença"; E5, **sem [TS]**; "somente" literal fica, L6-2, L7-3) | DEF | N | E | **não** | direta | DC | D3-76 (art. 20, caput): nota (cq) |
| D3-R83 | Lei 8.429, art. 1º, § 2º (4.9) | idem | dolo é a vontade livre e consciente de alcançar o resultado ilícito tipificado nos arts. 9º, 10 e 11, não bastando a voluntariedade do agente | DEF | N | C | não | direta | DC | D3-72 e D3-73: nota (cr) |
| D3-R84 | Lei 8.429, art. 13, § 3º (4.9) | idem | o agente público que se recusar a prestar a declaração de bens no prazo, ou prestar declaração falsa, é apenado com demissão (troca: demissão → suspensão) | PAR | N | E | sim | direta | DC | — |
| D3-R85 | Lei 8.429, art. 21, caput e II (4.9) | idem | a aplicação das sanções independe da aprovação ou rejeição das contas pelo controle interno ou pelo Tribunal de Contas (cenário: contas de gestor de órgão do Poder Legislativo da União aprovadas; troca: independe → a aprovação impede a aplicação; **sem a fórmula**, L7-2) | APL | S — órgão/servidor do Poder Legislativo da União | E | sim | direta | CQ | D3-75 (art. 11, § 4º): nota (ct) |
| D3-R86 | Lei 8.429, art. 7º, caput (4.9) | idem | havendo indícios de ato de improbidade, a autoridade que conhecer dos fatos representará ao Ministério Público competente (cenário: autoridade que toma conhecimento de indícios; fórmula admitida, a única da folha) | SIT | N | C | não | direta | CQ | D3-77 (art. 14, § 2º): nota (cu) |
| D3-R87 | Lei 8.429, art. 23, § 1º (4.9) | idem | a instauração de inquérito civil ou de processo administrativo suspende o curso do prazo prescricional por, no máximo, 180 dias corridos (troca: suspende → interrompe, conceito do § 4º) | PAR | N | E | sim | direta | DC | D3-78 (caput): nota (cv) |
| D3-R88 | Lei 8.429, art. 20, § 2º (4.9) | idem | o afastamento do agente determinado pela autoridade judicial é de até 90 dias, prorrogáveis uma única vez por igual prazo, mediante decisão motivada | NUM | N | C | não | direta | DC | D3-76 (caput): nota (cw) |
| D3-R89 | Lei 8.429, art. 3º, § 2º (4.9) | idem | as sanções da Lei 8.429 não se aplicam à pessoa jurídica se o ato também for sancionado como ato lesivo à administração pública pela Lei 12.846/2013 (cenário: pessoa jurídica beneficiada por ato sancionado nas duas leis) | SIT | N | C | não | direta | CQ | D3-80 (art. 3º, caput): nota (cs) |
Reserva da 7 (na ordem): art. 16, § 13; art. 16, § 14; art. 13, § 2º; art. 14, caput; art. 18; art. 22; art. 12, III.
Moldura da leva 7 (D3-R77, D3-R85): cena com "órgão do Poder Legislativo da União" como devedor (Fazenda federal) ou como órgão cujas contas foram aprovadas; nada sobre norma interna, regimento, carreira ou prática real da Câmara; a moldura não decide o gabarito; cenas distintas até o fecho (L3-3), inclusive em relação ao D3-28 e ao D3-74.

#### 13.4.5 Formatos ao fim da leva 7 (folha final de 20; teto 6)
| folha | DEF | SUJ | SIT | NUM | PAR | APL | total |
|---|---|---|---|---|---|---|---|
| 5.1 (canônicos 3/1/2/0/3/1 + leva 3/2/3/0/2/0) | 6 | 3 | 5 | 0 | 5 | 1 | 20 |
| 6.1 (canônicos 3/1/2/0/3/1 + leva 1/1/2/3/2/1) | 4 | 2 | 4 | 3 | 5 | 2 | 20 |
| 7 (canônicos 3/1/2/2/1/1 + leva 2/1/3/1/2/1) | 5 | 2 | 5 | 3 | 3 | 2 | 20 |
Maior formato: DEF 6 em 20 na 5.1 (30%, no teto, como a 4.1 na leva 5; a 5.1 não tem ponto de número no lastro); 25% na 6.1 e na 7. Formatos da leva 7: DEF 6, SUJ 4, SIT 8, NUM 4, PAR 6, APL 2. Formatos dos canônicos: D3_v2_1.md (campo Formato).

#### 13.4.6 Gabarito, moldura, aderência e conjuntos ao fim da leva 7
- Leva: **15 C / 15 E (50,0%)**; faixa de 30 itens: 12 a 18 C. Folhas: 5.1 10/10 (5/5 + 5/5); 6.1 11/9 (5/5 + 6/4); 7 9/11 (5/5 + 4/6) — todas na faixa de 8 a 12 C. A 6.1 e a 7 saem de 10/10 por causa do teste da seção 13.4.7.
- Moldura nova: **0 C / 2 E** (D3-R77, D3-R85) — as cotas da T-122 (6.1 1 E; 7 1 E; saida/banco/moldura_ce_2026-10-20.md, seção 4). DA: 50/38 → **50/40 (55,6%)**, meta da D-MOLDURA-CE mantida (seção 2.2). Por folha: 6.1 1 C / 1 E (D3-28 / D3-R77); 7 1/1 (D3-74 / D3-R85); 5.1 0/1 (D3-07); no máximo 6 por folha. Conjunto do D3: 9 C / 11 E → **9/13 (40,9%)**, dentro da faixa (seção 2.2).
- Aderência: 5.1 e 7, 20 diretos; 6.1, D3-R74 direto e os outros 9 pelo mapa do adendo (piso de 10 diretos já cumprido). VOLÁTIL 0. REVERIFICAR 0 (nenhuma redação de 2025 ou 2026 nos dispositivos do plano; a confirmar no adendo).
- [TS]: 13 (todos E; D3-R81 e D3-R82 são E sem [TS]; nenhum C-isca).
- Abertura × gabarito (7.4.2; L3-1): leva "Considere que" 6 C / 4 E (60,0% de C); declarativos 9 C / 11 E (55,0% de E). Folhas fechadas: 5.1 CQ 3 C / 3 E e DC 7 C / 7 E; 6.1 CQ 5/1 e DC 6/8; 7 CQ 4/3 e DC 5/8 — mínimos de 40% cumpridos.
- Fórmula "Nessa situação, nos termos d…": no máximo 1 por folha (D3-R65, D3-R77, D3-R86), 3 dos 10 CQ; nunca no D3-R85 (L7-2).
- Absolutos (L3-2; L6-2; L7-3): C com absoluto literal — D3-R79 ("somente"), D3-R88 ("uma única vez"); E com absoluto literal que não é a troca — D3-R82 ("somente"); nenhum E com absoluto inserido. L3-4 e L3-5: nenhum "mas não" / ", e não", "mero", "por si só" ou "simples" planejados. L4-1: nenhum fecho "é correto afirmar que". L5-1: todo E entre 19 e 62 palavras. L5-2: o D3-R81 não usa "só" nem verbo de condição necessária. Seção 10.2, itens 5 e 6: nenhum E nega a hipótese inteira no fecho; os SUJ E (D3-R68, D3-R80) usam ator ou elemento que a fonte menciona.
- Concentração por norma (informativo; seção 10.3): 5.1 com 5 itens da Lei 9.784 (arts. 13, 14 e 17) e 5 da CF; 6.1 com 3 itens do Decreto 20.910 e 3 da Lei 4.619 (notas (cm) e (cn)).

#### 13.4.7 Sequência (seção 7.3; plano conferido por script antes do despacho; scratchpad gcb_l6r/seq.py e plan7b.py)
| escopo | gabarito | [TS] | resultado |
|---|---|---|---|
| 5.1, leva / acumulada (20) | CECCEECEEC / ECCEECEECC·CECCEECEEC | nTnnTTnTTn / TTnnTnTTnn·nTnnTTnTTn | passa |
| 6.1, leva / acumulada (20) | CCECEECECC / ECECCEECEC·CCECEECECC | nnTnTTnTnn / TTnnnTTnTn·nnTnTTnTnn | passa |
| 7, leva / acumulada (20) | EEECEECECC / EECCECEECC·EEECEECECC | TnnnTTnTnn / TTnnnTTTnn·TnnnTTnTnn | passa (com D3-R81 e D3-R82 sem [TS]) |
| leva 7 inteira (5.1, 6.1, 7) | CECCEECEEC·CCECEECECC·EEECEECECC | nTnnTTnTTn·nnTnTTnTnn·TnnnTTnTnn | passa |
Na folha 7, com todo E com [TS], **nenhum** plano de 3 a 7 C passa o teste da folha acumulada: o [TS] dos canônicos (TTnnnTTTnn) forma bloco de período 6 com qualquer início da leva; só passam os dois planos de 4 C / 6 E com dois E sem [TS] nas posições 2 e 3 (EEECEECECC / TnnnTTnTnn, o adotado, e EEECEECCEC / TnnnTTnnTn). Os pares (D3-R60, D3-R61), (D3-R66, D3-R67) e (D3-R80, D3-R82) não leem um ao outro (notas (ce), (ci) e (cs)); nenhum par com moldura fica vizinho. Mesma regra de troca de posição da seção 8.3.7.

#### 13.4.8 Amostra da gbq-estilo (leva 7)
5 itens (16,7%), designados antes da produção: **D3-R60** (C da 5.1, abertura "Considere que"); **D3-R75** (E, NUM, troca de número, L7-1); **D3-R77** (E com moldura na 6.1, com a fórmula); **D3-R81** (E sem [TS], E5, segmento acessório falso); **D3-R85** (E com moldura na folha 7, sem a fórmula, L7-2). Cobre: as três folhas, um C, os dois E com moldura, L7-1 e L7-2 e um dos dois E sem [TS]. Rito da seção 9.3, item 6: sobre a v1, em paralelo ao R1; texto igual pedido pelos dois é aplicado uma vez (seção 11.3). Saída: saida/banco/estilo_DA_reforco_leva7.md.

#### 13.4.9 Notas de simulado previstas para a leva 7 (destino: T-119 e T-123; continuam (a) a (cd))
| # | itens | motivo |
|---|---|---|
| (ce) | D3-R60, D3-R61 e D1-40 | matérias indelegáveis (Lei 9.784, art. 13): no máximo 2 por simulado |
| (cf) | D3-R62 × D3-R63 × D3-02, D1-41 e D1-42 | ato de delegação (art. 14) |
| (cg) | D3-R64 × D3-08 e D1-43 | grau hierárquico (arts. 15 e 17) |
| (ch) | D3-R65 × D3-05 | CF, art. 84, VI, a e b |
| (ci) **OBRIGATÓRIA** | D3-R66 × D3-R67 (obrigatória); D3-R67 × D3-06 (comum) | delegação do art. 84, parágrafo único: o D3-R66 lido junto do D3-R67 pode sinalizar o rol |
| (cj) | D3-R68 × D3-R69 × D3-R66 | Presidente × Ministros de Estado (CF, arts. 84, II e parágrafo único, e 87, parágrafo único) |
| (ck) | D3-R70 × D3-R72 × D3-25 e D3-30 | pessoas jurídicas de direito público interno e externo (CC, arts. 41 a 43) |
| (cl) **OBRIGATÓRIA** | D3-R74 × D3-24 (obrigatória); D3-R74 × D3-R53 (comum) | o D3-24 traz literalmente "indenização ulterior" e entrega o E do D3-R74; o D3-R53 é o vizinho "prévia" (art. 5º, XXIV) |
| (cm) | D3-R73, D3-R75, D3-R78, D3-R23, D3-R24 e D3-R36 | Lei 4.619: no máximo 2 por simulado |
| (cn) | D3-R76, D3-R77, D3-R79 e D3-R22 | Decreto 20.910: no máximo 2 por simulado |
| (co) | D3-R71 × D3-24 e D3-28 | União responde (CF, art. 136, § 1º, II × art. 5º, XXV × art. 37, § 6º) |
| (cp) | D3-R81 × D3-R18 | limite da herança (Lei 8.429, art. 8º × Lei 8.112, art. 122, § 3º) |
| (cq) | D3-R82 × D3-76 | trânsito em julgado (Lei 8.429, art. 12, § 9º × art. 20, caput) |
| (cr) | D3-R83 × D3-72 e D3-73 | dolo (art. 1º, § 2º; art. 10, caput; art. 17-C, § 1º) |
| (cs) | D3-R80, D3-R89 e D3-80 | sujeitos (arts. 2º e 3º): no máximo 2 por simulado |
| (ct) | D3-R85 × D3-75 | "independe" (art. 21, II × art. 11, § 4º) |
| (cu) | D3-R86 × D3-77 | representação (arts. 7º e 14) |
| (cv) | D3-R87 × D3-78 | prescrição (art. 23, caput e § 1º) |
| (cw) | D3-R88 × D3-76 | afastamento × efetivação das sanções (art. 20, caput e § 2º) |
| (w) | a leva 7 inteira (ou só itens de reforço) | não forma simulado isolado; entra misturada por folha com os canônicos |
| (x) | os 2 itens com moldura (D3-R77, D3-R85) | contam para o teto de 50% de C com moldura por simulado (D-MOLDURA-CE (c)) |

#### 13.4.10 Despacho (leva 7)
1. **Ao qa-normativo-da** (primeiro passo; não produz item): adendo no escopo fechado da seção 13.4.2 (b), com a regra de rede dela; saída saida/gcb/D3_anexo_N_adendo_<data ISO>.md; SHA-256 no relato. Nada mais.
2. **À gcb-gerencia**: conferência do adendo por script (seção 13.6, a acrescentar antes da última linha desta ficha, como a 11.6 da leva 5): os 11 trechos e o mapa do D3-R73 da seção 13.4.2 (a), 1 vez no adendo e na cópia; aderência dos itens da 6.1 pelo mapa; ponto não confirmado vai à reserva da mesma folha, com o teste da seção 13.4.7 refeito; se a folha ficar com menos de 10 pontos, fecha menor e a reconciliação registra. Sem nova ficha nem novo gatilho.
3. **À gcb-cpp** (sonnet), uma instância, depois do item 2. Objeto: leva 7, conforme esta seção 13.4, as seções 1, 7, 8.2 (itens 4 e 7), 9.3, 10.2, 11.2, 11.6 (regra "Rede"), 12.2, 13.2 e 13.6, e os anexos abaixo. Saída: saida/gcb/DA_reforco_leva7_v1.md, no formato da regra 14 (nomes da seção 7.5), linha 1 `# DA_reforco_leva7_v1.md — T-116 — <data ISO> — gerado por gcb-cpp`, folhas na ordem 5.1, 6.1, 7. Anexos (lista exaustiva): esta ficha; saida/gcb/D3_anexo_N_mapa_normativo.md (seções 1, 2, 3, 4.1, 4.4, 4.6, 4.7, 4.9 e 5); saida/gcb/D3_anexo_N_adendo_2026-10-20.md (seções 1, 4.8 e 5.2); o adendo novo; saida/gcb/D2_anexo_N_mapa_normativo.md (seção 4.3, só para a reserva cruzada da 5.1); saida/gcb/D3_v2_1.md e saida/gcb/D1_v2.md (pontos já usados e formato dos blocos canônicos), só para os pontos já usados; os arquivos finais das levas 1 a 6 (pontos e modelo de bloco); regras/estilo_banca.md; cópias em saida/gcb/normativo_cache/ (CF, Código Civil, Lei 4.619, Decreto 20.910, Lei 9.784). A seção 4 do arquivo traz, por script, as contagens da regra 14, abertura × gabarito e fecho × gabarito no D3 (canônicos, levas 1 a 3, leva 7, acumulado), a fórmula e moldura × fórmula × gabarito (L7-2), absolutos por marcador e por gabarito (L3-2, L6-2, L7-3), sentido das trocas de número e as outras ocorrências do valor posto (L6-1, L7-1), extensão fora da faixa (L5-1), o teste da seção 13.4.7 refeito e a moldura acumulada (DA e D3). A gcb-cpp pode trocar um ponto pela reserva da mesma folha, com o motivo no bloco à GCB, nas condições da seção 3.7. O R1 da leva 7 não tem errata a conferir. Nada vai à plataforma nem à candidata. Sem commit.
4. **À gcb-cqfp** (R1, opus) e **à gbq-estilo** (amostra da 13.4.8), em paralelo, sobre a v1; a gcb-cqfp pode reabrir as Fontes 1, 4, 5 e 7 do Anexo N do D3 e as do adendo novo com User-Agent de navegador, como conferência; a pertinência dos pontos indiretos da 6.1 é dela.

### 13.5 Riscos e registros
1. 6.1 depende do adendo: sem ele, a folha fica abaixo de 20 e a leva 7 precisa de nova ficha (seção 13.4.2 (c)); se a gcb-cqfp recusar a pertinência dos indiretos, a 6.1 fecha menor, com registro.
2. Folha 7 com dois E sem [TS] (D3-R81, D3-R82): se a gcb-cqfp pedir [TS] em qualquer um, o teste de [TS] da folha 7 reprova (seção 13.4.7); a reconciliação registra o desvio, sem efeito no gabarito.
3. Folha 7 sem cópia da Lei 8.429 em normativo_cache/: lastro só no Anexo N do D3 (limitação de método, sem bloqueio).
4. Nenhuma tarefa nova (D-COMPLEMENTOS). Nenhum gatilho em PARA_PRESIDENCIA.md por esta seção (o gatilho da leva 6 é da reconciliação).

FIM DA FICHA DO REFORÇO DA
