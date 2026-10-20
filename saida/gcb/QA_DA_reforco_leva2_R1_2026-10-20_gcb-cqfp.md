# QA_DA_reforco_leva2_R1_2026-10-20_gcb-cqfp.md — T-116 — 2026-10-20 — gerado por gcb-cqfp

# PARECER QA R1 — REFORÇO DA, LEVA 2 (v1) — ciclo s15c4
Objeto: saida/gcb/DA_reforco_leva2_v1.md (30 itens: D4-R19 a D4-R28, folha 8.4; D1-R01 a D1-R12, folha 2.2; D3-R14 a D3-R21, folha 6.4). Critérios: ficha saida/gcb/DA_reforco_ficha_2026-10-20.md, seções 1, 4, 7 e 8 (8.2 e 8.3). A gcb-cqfp não produziu este texto e não o reescreve: os ajustes vêm em texto exato (seção 4.3 da ficha). Sem commit nem push; nenhum arquivo de produção foi alterado.

## 0. Resultado
- **APROVADO: 22. AJUSTAR: 7** (D1-R01, D1-R04, D1-R05, D1-R09, D3-R15, D3-R19, D3-R20; 11 AJ de texto exato). **REPROVADO: 1** (D1-R03).
- **Taxa de reprovação: 1/30 = 3,3%** (limite 30%): sem gate. A leva segue para a v2.
- Errata AJ-E1 (D3-R13, leva 1): **CONFERIDO** (seção 6, veredito separado).

## 1. Entradas (SHA-256 em disco, 20/10/2026) e método
| objeto | SHA-256 |
|---|---|
| saida/gcb/DA_reforco_leva2_v1.md | 40f2288a99286e744f48b9bb9d9c6dda45ed96bdf336217955a6f3ffa83ee788 |
| saida/gcb/DA_reforco_ficha_2026-10-20.md | 77f2e60af942b004fde8443030ff42c251e45057451f8d03845628f4df6e5639 |
| saida/gcb/D1_anexo_N_adendo_2026-10-20.md | cb4d02f9edbd0ec8f20b0bf8dec576868379f05fe1d7c1b6a54540a0177473f9 (= ficha 8.1) |
| saida/gcb/D3_anexo_N_adendo_2026-10-20.md | bbfd3eed1a69edef189a1fb8f07fee901daaf5bb636d8192bb1442e53a3fa797 (= ficha 8.1) |
| saida/gcb/D4_anexo_N_adendo_2026-10-20.md | c32f58eb78507f8c415c9b79f9cfdde0dfefdb7314ddd23045d312cb03d16fb5 (= ficha 8.1) |
| saida/gcb/DA_reforco_leva1_v2.md | 2c431529a5440d4a2bf2bb617bc75d496949dff28a824e0215322d00d79a4f04 (= ficha 8.1) |
| saida/banco/estilo_DA_reforco_leva1.md | 2d50c4cb210943105fabaeb35459a3137ed78b2393b6b15981cbbe8894728878 (= ficha 8.1) |
| saida/gcb/normativo_cache/Lei_8078_1990_CDC_compilada_2026-10-20.txt | 575478df6643d0495446b41db6828975477d8e7f57cadaca403b3dfe07784526 (= ficha 8.3.10) |

Método: leitura integral das seções 1 a 6 da v1; cada item confrontado com a linha do adendo (seção 3 e textos da seção 4/5) e com a cópia em saida/gcb/normativo_cache/; canônicos da folha relidos (D1_v2.md, D1-53 a D1-60, enunciados e blocos; D3_v2_1.md, D3-51 a D3-59; D4_v2_1.md, D4-27 a D4-33) e itens da leva 1 (DA_reforco_leva1_v2.md, D3-R01 a D3-R13; D4-R15 a D4-R17). Scripts próprios (python3 -I, somente leitura, scratchpad da sessão, fora do repositório): check.py (blocos, trechos × adendo × cache, URL, data, contagens, marcadores), seq.py (teste de sequência da regra 6), aje1.py (errata). Nenhuma leitura externa.

## 2. Veredito por item
Legenda das colunas de conferência: G = gabarito pela letra; P = ponto único; T = troca legítima / [TS]; F = sem pista de forma; Pe = pertinência à folha; Gê = não gêmeo (canônico da folha, leva 1, própria leva); M = moldura; J = justificativa e proveniência. ✓ confere; ✗ não confere; ~ confere com ajuste.

### Folha 8.4 — D4-R19 a D4-R28 (base: adendo do D4, seção 5, R60 a R81; F1, F3, F10)
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D4-R19 | C ✓ | ✓ | sem [TS] ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | R77 e R78 (Figura 1, p. 59) conferidos na cópia por leitura das colunas (o pdftotext dispõe a figura em colunas; as 5 células R76–R80 conferem). Fecha a corrida E E E (seção 7.3). |
| D4-R20 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | S, expositor, fecho neutro ✓ | ✓ | **APROVADO** | R60 alínea f literal. Par R3 do D4-R16 (leva 1). Amostra da gbq-estilo. |
| D4-R21 | E ✓ | ✓ | [TS] inexistência → existência ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Usa "setor público em geral" (R66), sem generalizar R68/R69 (B8). |
| D4-R22 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Desvio 6.2.3 aceito: omite a ressalva do Decreto 9.203 (exigência (c)). |
| D4-R23 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N, fecho neutro ✓ | ✓ | **APROVADO** | R81 literal. |
| D4-R24 | E ✓ | ✓ | [TS] apoio → primárias ✓ | ✓ | ✓ | ✓ | N, fecho de acerto ✓ | ✓ | **APROVADO** | Atribuição ao Referencial do TCU, autor não nomeado: ficha 0.2, item 4, e precedente aprovado do D4-R15 (leva 1). |
| D4-R25 | E ✓ | ✓ | [TS] "orçamentários ou não" → "exclusivamente orçamentários" ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | E6; absoluto equilibrado na leva pelo "todos" literal do D3-R14 (C). |
| D4-R26 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Observação (sem AJ): a construção está mais para DEF que para SUJ; reclassificar não muda teto (8.4 ficaria DEF 6, SUJ 0). |
| D4-R27 | E ✓ | ✓ | [TS] impactos → resultados ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Nota (u) da ficha mantida (× D4-28). |
| D4-R28 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | R74 literal, sem a remissão "capítulos 3 e 5". |

Exigência (c): nenhum enunciado cita "9.203" (0 ocorrências); nenhum autor nomeado; "NGP" e "pós-NPM": 0.

### Folha 2.2 — D1-R01 a D1-R12 (base: adendo do D1, seção 4; F1, F3, F4)
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D1-R01 | C ✓ | ✓ | ✓ | ✓ | ✓ | ~ | N ✓ | ✓ | **AJUSTAR** (AJ-1) | O enunciado afirma, como premissa, que o processo é "decid[ido] com a dispensa" do parecer não vinculante: é exatamente o elemento do § 2º que o D1-56 (E, mesma folha) inverte. A premissa entrega o gabarito do D1-56. O AJ-1 retira a premissa e deixa só o ponto julgado (responsabilidade de quem se omitiu), sem mudar ponto, gabarito, formato nem abertura. |
| D1-R02 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 12, § 1º, literal, com "culpa grave" (P4). |
| D1-R03 | E | — | — | — | ✓ | **✗** | N | — | **REPROVADO** | Gêmeo do canônico D1-55 da mesma folha (regra 2 da seção 1; critério 4.1.3). O enunciado do D1-55 (C) reproduz o § 1º inteiro, inclusive "responsabilizando-se quem der causa ao atraso"; o D1-R03 julga esse mesmo elemento do mesmo dispositivo com o sinal trocado ("responsabiliza-se exclusivamente o órgão consultivo"). O "Difere de" (o D1-55 julgaria só a paralisação) não se sustenta: o ponto do D1-55 é declarado na justificativa, mas o enunciado o afirma por inteiro. Não há AJ que preserve o ponto. Substituto: seção 3. |
| D1-R04 | E ✓ | ✓ | [TS] polaridade ✓ | ✓ | ~ | ✓ | N ✓ | ✓ | **AJUSTAR** (AJ-2) | O cenário ("conduta da qual resultou dano") não toca parecer nem opinião técnica; a pertinência à 2.2 só existe pelo caput do art. 12, ausente do item. O AJ-2 ancora o cenário na opinião técnica (art. 12, caput), sem enumerar a exceção do § 3º (seção 7.4.5). Item da amostra da gbq-estilo: o AJ segue para a v2 com os AJ de estilo. |
| D1-R05 | E ~ | ✓ | [TS] ~ | ✓ | ✓ | ✓ | N ✓ | ✓ | **AJUSTAR** (AJ-3, AJ-4) | Risco de gabarito discutível: pelo art. 43 o laudo também tem de ser "previamente obtido", de modo que "o processo não terá seguimento até a apresentação do laudo" pode ser lido como verdadeiro (o processo aguarda um laudo, o do outro órgão). A troca legítima é de quem apresenta: o art. 43 manda solicitar a outro órgão; o § 1º do art. 42 espera o próprio omisso. O AJ-3/AJ-4 tornam a troca literal e única. Desvio 6.2.4 aceito com o ajuste. Nota (s) mantida (× D1-55 e D1-56). |
| D1-R06 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 10, caput, literal; protege quem seguiu o parecer (P5). |
| D1-R07 | E ✓ | ✓ | [TS] dolosos → culposos ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Inciso I vetado não usado. |
| D1-R08 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | § 6º, primeira parte (C6); A2.2-14 fora. |
| D1-R09 | C ✓ | ✓ | ✓ | ✓ | ~ | ✓ | N ✓ | ✓ | **AJUSTAR** (AJ-5) | Mesmo motivo do D1-R04 (cenário genérico de "ato"; ancoragem na opinião técnica). |
| D1-R10 | E ✓ | ✓ | [TS] não afasta → afasta ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 17 só (P4). |
| D1-R11 | E ✓ | ✓ | [TS] prévio → posterior ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Observação (sem AJ): a ficha previa "posterior à contratação"; o item diz "controle posterior de legalidade". A troca do qualificador literal é suficiente e segue o padrão E1/E2 da banca; registro de desvio não declarado pela produção. |
| D1-R12 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 72, III, literal. Pertinência direta pelo critério do adendo (dispositivo trata do parecer), embora não trate de responsabilidade: registro, sem ajuste (vale também para o D1-R11). |

Decreto 9.830: D1-R02, R04, R08, R09, R10 (5) sem moldura, sem afirmar alcance (P3); "Poder Legislativo", "Câmara", "comissão" ou "parlamentar" em item N: 0.

### Folha 6.4 — D3-R14 a D3-R21 (base: adendo do D3, seção 4; A1 a A4)
| id | G | P | T | F | Pe | Gê | M | J | veredito | nota |
|---|---|---|---|---|---|---|---|---|---|---|
| D3-R14 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Art. 25, caput, sem a parte final (reservada ao D3-R28). |
| D3-R15 | C ✓ | ✓ | ✓ | **~** | ✓ | ✓ | N ✓ | ~ | **AJUSTAR** (AJ-6, AJ-7) | Desvio 6.2.1 **não aceito**: "pode configurar" põe num C o marcador de possibilidade afirmativa, que no banco real está concentrado em C (regras/estilo_banca.md, seção 4: 15 C / 5 E); é o único "pode" afirmativo da leva. O receio de C incompleto não procede: pela seção 3.12 (C6), a concessiva literal "ainda que … exclusivamente moral", sem marcador de exclusividade, é C. O AJ-6 usa a concessiva da letra. |
| D3-R16 | E ✓ | ✓ | [TS] exclusão do dano à imagem ✓ | ✓ | ✓ | ✓ | S ✓ | ✓ | **APROVADO** | Moldura decorativa (servidor como vítima), não decide o gabarito. Nota (k) mantida. |
| D3-R17 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Estado fora da cena (A2, A11). |
| D3-R18 | E ✓ | ✓ | [TS] até o limite da herança → sem limite ✓ | ✓ | parcial ✓ | ✓ | S ✓ | ✓ | **APROVADO** | Pertinência parcial aceita (A1; ficha 0.2, item 5). Amostra da gbq-estilo. |
| D3-R19 | E ✓ | ✓ | [TS] extensão do dano → gravidade da culpa ✓ | ✓ | ✓ | ~ | S ✓ | ✓ | **AJUSTAR** (AJ-8, AJ-9) | A premissa "servidor … tenha causado dano a particular e deva indenizá-lo" põe o servidor como devedor direto do particular: toca a matéria vedada (responsabilidade direta do agente perante a vítima; A11 e C12) e colide, na mesma folha, com o D3-R20 (o servidor responde perante a Fazenda Pública, em regresso) e com o D3-58. O AJ-8 inverte a cena (servidor vítima de particular, como no D3-R16): mesmo ponto, mesmo gabarito, mesma moldura e mesmo tipo; a troca continua literal. |
| D3-R20 | C ✓ | ✓ | ✓ | ✓ | parcial ✓ | ✓ | S ✓ | ~ | **AJUSTAR** (AJ-10, AJ-11) | Sem o vínculo funcional, a cena admite dano em atividade particular, em que o servidor responde diretamente (é o que o canônico D3-52, da mesma folha, ensina), e o C fica discutível. O AJ-10 põe o servidor "agindo com culpa no exercício de suas atribuições" (Lei 8.112, arts. 121 e 122, caput, no adendo, seção 4.3). A linha 2 da justificativa afirma que o servidor não responde diretamente ao terceiro, o que está fora da base (A11; C12): o AJ-11 a troca por tentação da letra. |
| D3-R21 | C ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | N ✓ | ✓ | **APROVADO** | Inciso X literal; nota (k). |

## 3. Reprovação e substituto
**D1-R03 — REPROVADO** (critério 4.1.3: gêmeo de canônico da mesma folha). Motivo: seção 2. O id D1-R03 não volta; o substituto recebe **D1-R13** (próximo id livre do lote D1; as faixas da leva 12 passam a D1-R14–R22 na 1.1 e D1-R23–R31 na 1.2), na **posição 3 da folha 2.2**, como **E com [TS] e abertura declarativa**, para não alterar o teste de sequência (gabarito CCEEECECCEEC e [TS] nnTTTnTnnTTn ficam iguais).

Substituto sugerido (reserva da ficha, seção 8.3.4), com a restrição de concentração da seção 8.2, item 5 — a escolha exige decisão da GCB, porque nenhum ponto da reserva cabe sem tocar uma decisão dela:
- **Preferido: A2.2-09** (Decreto 9.830, art. 12, § 2º; direta; adendo do D1, seção 4.3: "Não será configurado dolo ou erro grosseiro do agente público se não restar comprovada, nos autos do processo de responsabilização, situação ou circunstância fática capaz de caracterizar o dolo ou o erro grosseiro."). Troca de polaridade da exigência de comprovação nos autos; formato DEF (2.2 fica com DEF 6 = teto; PAR 6 = teto; SUJ 2). Custo: o Decreto 9.830 passa a 6 itens na folha, acima do teto de 5 da seção 8.2, item 5 (decisão da GCB, não regra da seção 1). Sem moldura (P3). Nota "não pôr no mesmo simulado" com o D1-R04 (§ 3º, mesma família de prova do dolo ou erro grosseiro).
- **Não recomendado: A2.2-05** (LINDB, art. 28, "só E de troca de sujeito"): pelo mesmo critério que reprova o D1-R03, seria gêmeo do D1-57 (o C reproduz "responderá pessoalmente"; o E trocaria esse elemento). Além disso, o art. 28 não menciona outro ator plausível para a troca de sujeito (seção 7.4.4).
- Alternativa dentro do teto do Decreto: A2.2-19 (Lei 14.133, art. 10, § 2º): leva a Lei 14.133 a 5 (teto 4) e o art. 10 a 3 itens na folha (D1-R06, R07): pior concentração.

Sem o substituto, a 2.2 fica com 19 itens e a leva com 17 C / 12 E (58,6%; ainda na faixa 12–18).

## 4. Ajustes em texto exato (seção 4.3 da ficha; cada "substituir" ocorre 1 vez no arquivo, conferido por script)
`AJ-1 | D1-R01 | enunciado (seção 1) | substituir: «a decisão do processo com a dispensa de parecer obrigatório e não vinculante que não tenha sido emitido no prazo fixado não prejudica a responsabilidade de quem se omitiu no atendimento.» | por: «se um parecer obrigatório e não vinculante deixar de ser emitido no prazo fixado, subsiste a responsabilidade de quem se omitiu no atendimento.»`

`AJ-2 | D1-R04 | enunciado (seção 1) | substituir: «Considere que determinado agente público tenha praticado conduta da qual resultou dano.» | por: «Considere que determinado agente público, ao emitir opinião técnica, tenha dado causa a dano.»`

`AJ-3 | D1-R05 | enunciado (seção 1) | substituir: «e vinculante: o processo não terá seguimento até a apresentação do laudo.» | por: «e vinculante: o processo não terá seguimento até que o órgão omisso apresente o laudo.»`

`AJ-4 | D1-R05 | Troca | substituir: «→ o processo não terá seguimento até a apresentação do laudo (art. 43» | por: «→ o processo não terá seguimento até que o órgão omisso apresente o laudo (art. 43»`

`AJ-5 | D1-R09 | enunciado (seção 1) | substituir: «Considere que determinado agente público tenha praticado ato do qual resultou dano ao erário de montante expressivo.» | por: «Considere que determinado agente público, ao emitir opinião técnica, tenha dado causa a dano ao erário de montante expressivo.»`

`AJ-6 | D3-R15 | enunciado (seção 1) | substituir: «a violação de direito que cause dano exclusivamente moral a outrem pode configurar ato ilícito.» | por: «o ato ilícito configura-se ainda que o dano causado a outrem seja exclusivamente moral.»`

`AJ-7 | D3-R15 | Justificativa (linha 2) | substituir: «O item julga só a locução ‘ainda que exclusivamente moral’, com ‘pode configurar’;» | por: «O item julga só a locução ‘ainda que exclusivamente moral’, sem afirmar que ela basta;»`

`AJ-8 | D3-R19 | enunciado (seção 1) | substituir: «Considere que servidor de órgão do Poder Legislativo da União tenha causado dano a particular e deva indenizá-lo. Nessa situação, nos termos do art. 944, caput, do Código Civil, a indenização mede-se pela gravidade da culpa do servidor.» | por: «Considere que servidor de órgão do Poder Legislativo da União tenha sofrido dano causado por particular e pretenda ser indenizado. Nessa situação, nos termos do art. 944, caput, do Código Civil, a indenização mede-se pela gravidade da culpa do particular.»`

`AJ-9 | D3-R19 | Troca | substituir: «- Troca: extensão do dano → gravidade da culpa do servidor (art. 944, caput)» | por: «- Troca: extensão do dano → gravidade da culpa do particular (art. 944, caput)»`

`AJ-10 | D3-R20 | enunciado (seção 1) | substituir: «lotado em órgão do Poder Legislativo da União tenha causado dano a terceiros.» | por: «lotado em órgão do Poder Legislativo da União, agindo com culpa no exercício de suas atribuições, tenha causado dano a terceiros.»`

`AJ-11 | D3-R20 | Justificativa (linha 2) | substituir: «a tentação é supor que o servidor responda diretamente ao terceiro.» | por: «a tentação é inverter os polos da ação regressiva, como se o servidor a movesse contra a Fazenda Pública.»`

Efeito dos AJ nas contagens: nenhum muda gabarito, [TS], formato, moldura (S/N e tipo), aderência ou abertura; D3-R19 e D3-R20 continuam com "servidor … do Poder Legislativo da União" (moldura S, tipo órgão/servidor); a fórmula "Nessa situação, nos termos d…" na 6.4 continua 2 de 5. A v2 refaz as seções 4.1 a 4.7 por script com o D1-R13.

## 5. Conferências de leva (seção 4.4 da ficha)
| # | conferência | resultado |
|---|---|---|
| 1 | C/E da leva | **CONFERE**: 17 C / 13 E (56,7%; faixa 12–18). Com o D1-R03 fora e o substituto E: 17/13. Folhas: 8.4 10/10; 2.2 10/10 (com o substituto); 6.4 8/8 (de 16). |
| 2 | tetos por folha | **CONFERE**: formatos da leva 8.4 3/1/2/0/3/1, 2.2 1/3/5/0/3/0, 6.4 2/1/1/0/0/4 (DEF/SUJ/SIT/NUM/PAR/APL), iguais à ficha 8.3.5; maior formato na folha final: 8.4 5, 2.2 PAR 6 (teto), 6.4 5 (de 20). VOLÁTIL 0; REVERIFICAR 0. Moldura por folha: 8.4 5, 6.4 5, 2.2 0 (≤ 6). Piso de 10 diretos: 8.4 20; 2.2 20 (19 até o substituto); 6.4 14. |
| 3 | moldura acumulada e conjuntos | **CONFERE**: leva 2 C / 3 E com moldura (D4-R20, D3-R20 / D3-R16, R18, R19); DA 46/18 → 48/21 (69,6%), igual à seção 2.2; D3 7/4 → 8/7; K1 13/6 → 14/6; K2 7/6 → 7/7; K3 5/4 sem item novo; K4 23/17 → 25/18 (58,1%); fecho neutro 0/3 → 2/3; ", e não" 0/2 → 1/2. Partidas do D4 recontadas nos canônicos (K4 21/8; K2 5/0; K3 4/0). Classificação de moldura: termos do Legislativo só nos 5 itens S. |
| 4 | pontos sem duplicata | **NÃO CONFERE** só no D1-R03 (gêmeo do D1-55; reprovado). Demais: 30 códigos distintos, nenhum repetido da leva 1 nem dos canônicos; R-ids da 8.4 sem interseção com os da leva 1 e dos canônicos (R16, R17, R18). |
| 5 | exigências da leva (seção 2.3) | **CONFERE**: (c) nenhum item da 8.4 usa o Decreto 9.203, art. 2º, II, nem o art. 4º, IV (0 ocorrências de "9.203" em enunciado); (d) aderência parcial só em D3-R18 e D3-R20, declarada. |
| 6 | primeiro e último id por lote | **CONFERE**: D4-R19–R28; D1-R01–R12; D3-R14–R21. Na v2: D1-R13 substitui o D1-R03 (seção 3). |
| 7 | linha 1 e última linha | **CONFERE**: "# DA_reforco_leva2_v1.md — T-116 — 2026-10-20 — gerado por gcb-cpp"; "FIM DA LEVA 02 — REFORÇO DA". |
| 8 | bases reabertas no cache | **CONFERE**: os 37 trechos (30 itens) estão no adendo (37/37); 32 por subcadeia direta na cópia em normativo_cache/ e 5 (R76 a R80, Figura 1 da Casa Civil, p. 59) por leitura das colunas da cópia (linhas 2589–2601), texto idêntico; nenhum item passa de 25 palavras de trecho; URL e "consulta 20/10/2026" idênticas às do adendo em 30/30. |
| — | teste de sequência (regra 6; 7.3; 8.2, item 7) | **CONFERE** (seq.py): leva e folhas da leva passam (gabarito e [TS]); nas folhas acumuladas só os legados registrados: 8.4 [TS] p3 = 9 (posições 1–9), 2.2 alternância 6 (1–6, gabarito e [TS]), 6.4 gabarito p3 = 8 (1–8). Nenhuma janela reprovada inclui item novo. |
| — | marcadores e pistas | Abertura × gabarito: "Considere que" 7 C / 6 E, declarativos 10 C / 7 E (≥ 40% cada; seção 7.4.2). Possibilidade afirmativa ("pode"): só D3-R15 (C) → AJ-6. Absolutos: D4-R25 E, D1-R03 E (reprovado), D3-R14 C (literal). Negação frontal (7.4.5): nenhuma. |

## 6. Errata AJ-E1 (D3-R13, leva 1) — seção própria (D-T116-LEVA1-ACEITE, parte (II); ficha 8.3.10)
Texto conferido: linha da AJ-E1 em saida/banco/estilo_DA_reforco_leva1.md (2d50c4cb…8878, linha 125), idêntico ao da ficha 8.3.10 e ao da reconciliação da leva 1 (o "antes" e o "depois" ocorrem 1 vez em cada um dos dois arquivos).
1. Ocorrência: o "antes" ocorre **1 vez** na seção 1 de saida/gcb/DA_reforco_leva1_v2.md (2c431529…a4f04) e 1 vez no arquivo inteiro; o "depois" ocorre **0 vez** (seção 1 e arquivo). **CONFERE.**
2. Literalidade: o "depois" é o CDC, art. 22, caput, na cópia saida/gcb/normativo_cache/Lei_8078_1990_CDC_compilada_2026-10-20.txt (575478df…4526, linha 150), palavra por palavra e vírgula por vírgula; a única diferença é a minúscula inicial ("os órgãos públicos"), exigida por vir depois de "Nos termos do art. 22 do Código de Defesa do Consumidor,". **CONFERE.**
3. Mesmas palavras: 30 palavras antes e depois, mesmo multiconjunto; muda só a ordem (e a vírgula acrescida é a da letra do caput, depois de "empreendimento"). **CONFERE.**
4. Campos do bloco: a errata toca só o enunciado da seção 1; gabarito C, ponto A6.3-12, mecanismo C2, formato SUJ, aderência parcial, moldura N, Base e Marcas inalterados. **CONFERE.** (Registro sem efeito: a Justificativa (linha 1) do bloco conserva a ordem inversa; é paráfrase de justificativa, fora do alcance da errata, e não precisa mudar.)
5. Leitura do enunciado resultante: «Nos termos do art. 22 do Código de Defesa do Consumidor, os órgãos públicos, por si ou suas empresas, concessionárias, permissionárias ou sob qualquer outra forma de empreendimento, são obrigados a fornecer serviços adequados, eficientes, seguros e, quanto aos essenciais, contínuos.» Reprodução literal do caput (C2), sentido inalterado, sem marcador novo nem pista; a leitura de passagem errada "contínuos os órgãos públicos" desaparece. **CONFERE.**

**Veredito: CONFERIDO.** Não é terceira rodada da leva 1, não altera o arquivo da leva 1 e não impede a leva 3; a GCB leva a errata ao gatilho A da leva 2 como item separado (ficha 8.3.10).

## 7. Desvios de redação declarados pela produção (seção 6.2 da v1)
| # | desvio | avaliação |
|---|---|---|
| 1 | D3-R15 "pode configurar" | **Não aceito** → AJ-6 e AJ-7 (seção 2). |
| 2 | D1-R04 cenário sem a exceção do § 3º | **Aceito** (evita negação frontal); cenário ancorado na opinião técnica pelo AJ-2. |
| 3 | D4-R22 sem a ressalva do Decreto 9.203 | **Aceito** (exigência (c)). |
| 4 | D1-R05 laudo × parecer | **Aceito com ajuste** (AJ-3, AJ-4: a troca fica no sujeito que apresenta o laudo). |
| 5 | Dois trechos com "[…]" (7 itens) | **Aceito**: cada trecho é subcadeia contínua do adendo e da cópia; soma ≤ 25 palavras. |
| 6 | Mecanismo escolhido pela produção | **Aceito**; nenhuma reclassificação necessária nos itens que seguem (o E3 do D1-R03 seria E6, sem efeito). |
| — | não declarado: D1-R11 "controle posterior" (ficha: "posterior à contratação") | Aceito, com registro (seção 2). |

## 8. Lista para a v2 (gcb-cpp)
1. Aplicar AJ-1 a AJ-11 por substituição exata, sem outra mudança.
2. Substituir o D1-R03 por **D1-R13** na posição 3 da 2.2 (E, [TS], declarativo), com ponto decidido pela GCB (seção 3: preferido A2.2-09, com o Decreto 9.830 a 6 na folha); bloco completo (regra 14), "Difere de" do D1-R04 e nota "não pôr no mesmo simulado" D1-R13 × D1-R04.
3. Remover a nota (s) "D1-R03 … × D1-55" da seção 5 e da ficha de notas; atualizar as seções 0, 3.2, 4.1 a 4.7 e 5 por script (ids, pontos, formatos da 2.2, Decreto/Lei 14.133 por folha, sequência).
4. Coordenação: o D1-R04 está na amostra da gbq-estilo (8.3.8); o AJ-2 vai para a v2 junto com os AJ de estilo e é conferido no R2.
5. O R2 confere cada AJ aplicado literalmente e examina só o que a v2 mudar além dos AJ e o D1-R13.

## 9. Notas à GCB e à GBQ (sem decisão desta QA)
- A2.2-05 (reserva da 2.2): pelo critério do D1-R03, o E de troca de sujeito do art. 28 da LINDB seria gêmeo do D1-57; sugere-se retirá-lo da reserva.
- Pertinência dos pontos da Lei 14.133, arts. 53 e 72 (D1-R11, D1-R12): diretos pelo critério do adendo (o dispositivo trata do parecer), mas não tratam de responsabilidade; aceitos, com registro para a auditoria de cobertura.
- Notas de simulado (k) a (x) da ficha 8.5: mantidas; acrescentar D1-R13 × D1-R04 (se o substituto for o A2.2-09).

FIM DO PARECER QA R1 — LEVA 2 — REFORÇO DA
