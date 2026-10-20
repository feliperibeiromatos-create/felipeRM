# DA_reforco_leva1_reconciliacao_2026-10-20.md — T-116 — 2026-10-20 — gerado por gcb-gerencia

# RECONCILIAÇÃO DA LEVA 1 DO REFORÇO DE DIREITO ADMINISTRATIVO (D-REFORCO-DA) — D1 da GCB e gatilho A — ciclo s15c3
Titular: GCB (T-116). A GCB reconcilia e decide D1; não produz nem corrige item. Nenhum arquivo de produção ou de QA foi alterado. Sem commit nem push. Decisões aplicadas: D-REFORCO-DA, D-REFORCO-2 (regras 1 a 6), D-MOLDURA-CE, D-T97-META-FUNDADOR-RESP, D-ADERENCIA, D-QA-PENDENTE, D-NUCLEO-CRITERIO; precedentes D-T98-ONDA4-ACEITE e D-V112-BAEF-P2-ACEITE (texto do estilo com ou sem nova QA) e D-T89-R1-ACEITE (a reconciliação prevalece sobre o arquivo da leva na consolidação).

## 0. Entradas (SHA-256 em disco, 20/10/2026)
| objeto | papel | SHA-256 |
|---|---|---|
| saida/gcb/DA_reforco_leva1_v2.md | **objeto final** (30 itens; 95.081 bytes; 779 linhas LF) | 2c431529a5440d4a2bf2bb617bc75d496949dff28a824e0215322d00d79a4f04 |
| saida/gcb/DA_reforco_leva1_v1.md | objeto do R1 (rastro) | 047949049703a052b6233b6d5bb31b98021425a1854a768dbfd4ae1096215f01 |
| saida/gcb/QA_DA_reforco_leva1_R1_2026-10-20_gcb-cqfp.md | QA R1 | edf198440cafa91786fafd53b194ece929f49b60fe7993e179a41fa0379179f8 |
| saida/gcb/QA_DA_reforco_leva1_R2_2026-10-20_gcb-cqfp.md | QA R2 (última rodada) | 7f77a3151b964aa3de01db1bdef26acf1f00137400f9ee4db5a99aaf93b0a509 |
| saida/banco/estilo_DA_reforco_leva1.md | auditoria de estilo 10% (gbq-estilo) | 2d50c4cb210943105fabaeb35459a3137ed78b2393b6b15981cbbe8894728878 |
| saida/gcb/DA_reforco_ficha_2026-10-20.md | ficha — antes do adendo (critério do R1, R2 e estilo) | acf8b57af3f42e0bcab9a6d92f6cfa3dd70deacf3f521fc285e5b3a1b0d95133 |
| saida/gcb/DA_reforco_ficha_2026-10-20.md | ficha — com a seção 7 "Adendo após a leva 1" (esta reconciliação; só acréscimo antes da última linha) | 6e90dc130678de333a5e1b3ff4a4af52b0bb7295b75cd8f4f9fa64f0b50ec41b |
| saida/pacote/pacote.json v1.13 canônico | partida (canônicos das folhas) | 82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240 |
| saida/pacote/pacote_estudante.json v1.13-E | aderência e núcleo dos canônicos | 04cbd593fdd30404ecb7f91f6b6722da6b2fc24e58d3c0eb68b10a4e792a0c40 |
| saida/banco/moldura_ce_itens_2026-10-20.csv | moldura oficial dos canônicos | ed4b364dffbca7d9e8878591914783258fa7048c4f1837d98c3d62e34981daac |

As entradas do R1 e do R2 têm o mesmo SHA-256 citado nos pareceres; o estilo auditou o mesmo v2 (2c431529…).

## 1. Objeto aceito
**saida/gcb/DA_reforco_leva1_v2.md, SHA-256 2c431529a5440d4a2bf2bb617bc75d496949dff28a824e0215322d00d79a4f04**, sem alteração, com os registros desta reconciliação prevalecendo na consolidação (seções 4 e 5). 30 itens AUTORAL, todos aprovados (R1 + R2):
- 8.1 (14): D4-R01 a D4-R11, D4-R18, D4-R13, D4-R14 (ordem do arquivo);
- 6.3 (13): D3-R01 a D3-R13;
- 8.4 (3, primeira parte): D4-R15 a D4-R17.
Id vago: **D4-R12** (reprovado no R1 por gêmeo do D4-01; não reutilizado). Os 30 seguem com "QA PENDENTE" até o aceite (D-QA-PENDENTE); a marca sai só na exportação da GBQ.

## 2. Conferência própria (python3 -I, somente leitura; script em scratchpad gcb_l1/conf.py, fora do repositório)
| conferência | resultado |
|---|---|
| SHA-256 do final | = 2c431529…a4f04 (igual ao R2 e ao estilo) |
| Linha 1 / última linha | "# DA_reforco_leva1_v2.md — T-116 — 2026-10-20 — gerado por gcb-cpp" / "FIM DA LEVA 01 — REFORÇO DA" — CONFERE |
| Ids | 30 únicos, mesma ordem na seção 1 (estudante), 2 (gabarito), 3.2 (proveniência) e 4.5 (pontos); nenhum no pacote.json v1.13; D4-R12 ausente — CONFERE |
| Seção 1 (estudante) | sem gabarito, [TS], VOLÁTIL, REVERIFICAR ou URL — CONFERE |
| Campos | itemEdital = P1-DA-<folha> em 30/30; Marcas TS × [TS] do cabeçalho e campo Troca × [TS] coerentes; Moldura S ⇔ formato APL; AUTORAL; VOLÁTIL = 0; REVERIFICAR = 0 — CONFERE |
| C/E da leva | **15 C / 15 E (50,0%)** — faixa 12–18 (regra 5 da D-REFORCO-2) CONFERE |
| C/E por folha (canônicos + leva) | 8.1 10/10; 6.3 10/10; 8.4 4/6 (10 itens; fecha na leva 2) |
| Formatos por folha (DEF/SUJ/SIT/NUM/PAR/APL) | 8.1 6/0/5/0/4/5; 6.3 6/2/5/0/2/5; 8.4 2/0/2/0/2/4 (de 10) — maior 30% (DEF na 8.1 e na 6.3, no teto); 8.4 APL 4 = 20% de 20 — regra 3 CONFERE |
| Formatos da leva | 8/2/6/0/3/11 (8.1 4/0/4/0/2/4; 6.3 4/2/2/0/1/4; 8.4 0/0/0/0/0/3) |
| [TS] | 16 (15 E; 1 C-isca, D3-R10, único da 6.3; 8.1 e 8.4 sem C-isca novo) — CONFERE |
| VOLÁTIL / REVERIFICAR | 0 / 0 (regra 4; nada à T-11/T-120) |
| Aderência | 8.1 20 diretos; 6.3 12 diretos / 8 parciais (D3-R01, R04, R06, R08, R09, R10, R12, R13); 8.4 10 diretos — piso de 10 diretos (D-T97-META-FUNDADOR-RESP) CONFERE; leva 22 / 8 |
| Pontos | 30 pontos distintos (A8.1-27 em duas alíneas, i e d); nenhum item da 8.4 usa o Decreto 9.203, art. 2º, II, nem o art. 4º, IV (exigência (c)) — CONFERE |
| Moldura (D-MOLDURA-CE) | leva 2 C / 9 E; DA 44/9 → **46/18 (71,9%)**, igual à ficha 3.6; D3 6/1 → 7/4; D4 (K1) 12/0 → 13/6; por folha 8.1 5, 6.3 5, 8.4 4 (≤ 6) — CONFERE; cota de E com moldura 9/9 (margem da leva 5 preservada) |
| Conjuntos do D4 (96 itens) | K2 fecho de acerto 7/6 (53,8%); K3 "pós-NPM" 5/4 (55,6%); K4 "Considere que" 23/17 (57,5%); fecho neutro 0/3 — K2 a K4 em 40–60% CONFERE (desvio de +1 C em K2–K4 sobre a ficha 3.6 pelo substituto D4-R18; registrado) |
| Teste de sequência (corrida ≥ 4; alternância > 4; bloco de período 2–8 até max(8, 2p)) | gabarito: 8.1, 6.3 e 8.4 (leva e acumuladas) e leva inteira APROVADO; [TS]: tudo APROVADO, **exceto 8.4 acumulada nTTnTTnTTT (período 3, 9/8)** — decisão na seção 4.1 |
| Núcleo (canônicos) | 8.1 6, 6.3 7, 8.4 7 canônicos, todos diretos e nucleo = true na v1.13-E |
| Texto do estilo | AJ-E1: "antes" 1 vez no v2; "depois" 0 vez; o "depois" é literal ao CDC, art. 22, caput, na cópia do cache (Lei_8078_1990_CDC_compilada_2026-10-20.txt); AJ-E2 e AJ-E3: "antes" 1 vez cada |
| Página do D4-R18 (R-2 do R2) | alínea d de R54 na p. 20 da cópia do Ipea (cabeçalho "20" na linha 146; alínea nas linhas 150–151) |

## 3. Rito e QA
- R1 (gcb-cqfp, opus; não produziu): 24 APROVADOS, 5 AJUSTAR, 1 REPROVADO (D4-R12) — 3,3%, sem GATE. R2 (última): 6/6 alterados APROVADOS, 24 inalterados, 0% — APROVADO COM RESSALVAS, ressalvas só de registro e D1 (R-1 [TS] da 8.4; R-2 página), fechadas aqui. Acumulado: 1/31 = 3,2%.
- Estilo (gbq-estilo, opus; não produziu): amostra designada pela ficha antes da produção, 4/30 (13,3%; D4-R03, D3-R03, D3-R13, D4-R16); 3 CONFORMES, 1 AJUSTE de texto (D3-R13), 0 NÃO CONFORME; sem GATE; nenhum item decidido pela moldura.
- Nenhum gabarito em disputa. O aceite é do objeto, não "com ressalva": as ressalvas estão fechadas pelas decisões da seção 4.

## 4. Decisões da GCB (D1)

### 4.1 Pendência 1 — sequência de [TS] da 8.4 acumulada (C4 do R1; R-1 do R2)
**ACEITA e registrada, sem mudar item aprovado; correção prospectiva na leva 2.** Fundamentos: (a) a marca [TS] é metadado da produção e não chega à candidata — o pacote.json e o pacote_estudante.json v1.13 não têm campo de [TS] (conferido por script nas chaves dos itens); o que ela vê é a sequência de gabarito, que passa em todas as linhas; (b) a redistribuição da 8.4 entre as levas 1 e 2 tiraria da leva itens aprovados e devolveria itens ao QA, numa terceira rodada que a D-REFORCO-DA não admite; (c) a causa é o plano da ficha (8.4 = 0 C / 3 E, todo E com troca), corrigido no adendo (ficha 7.3: o teste roda sobre o plano antes do despacho). Medidas: (i) **D4-R19, primeiro item da 8.4 na leva 2, é C sem [TS]** — a 8.4 acumulada termina em E E E (um E a mais seria corrida de 4) e o bloco de [TS] para em 9 (simulado por script: com C sem [TS] o gabarito passa e o bloco não cresce); (ii) o bloco das posições 1 a 9 da 8.4 (D4-27 a D4-33, D4-R15, D4-R16) fica como desvio aceito e não conta como falha da leva 2; o resto da folha de 20 passa o teste inteiro, conferido na reconciliação da leva 2; (iii) **ordem de apresentação na montagem (T-123)**: dentro de cada folha, os canônicos na ordem do pacote v1.13 e depois os D<n>-R na ordem do arquivo da leva (na 8.1, D4-R18 entre D4-R11 e D4-R13) — ordem em que o teste e o núcleo foram calculados.

### 4.2 Pendência 2 — núcleo da 6.3 com o D3-R01 parcial (R1, seção 6, item 9)
**Núcleo da 6.3 = D3-R02, D3-R03 e D3-R05.** Não é critério novo: é o k3 da D1 da GBQ, sem objeção da presidência (D-NUCLEO-CRITERIO: k1 data → k2 ato → k3 direta antes de parcial só no empate dentro do mesmo ato → k4 posição). O aceite desta leva é um ato; dentro dele, os diretos da 6.3 em ordem são D3-R02, R03, R05, R07, R11; os três primeiros completam os 10 (7 canônicos + 3). A "ordem de id" da ficha (0.2, item 10) ignorava o k3 e fica corrigida no adendo (ficha 7.2). Demais folhas: 8.1 → D4-R01 a D4-R04; 8.4 → D4-R15 a D4-R17 (os 10 itens da 8.4 da leva 2 ficam false). Os parciais seguem só em simulado diagnóstico (D-ADERENCIA); o campo não muda aptidão.

### 4.3 Pendência 3 — pista "Considere que" e fecho neutro
**Sem efeito sobre os 30 itens** (no banco acumulado não há pista: D4 phi −0,13, p = 0,30; D3 −0,18, p = 0,12; folhas 8.1 e 6.3 equilibradas; a correlação só aparece na leva isolada, 73,3%, por efeito do plano de antecipação da moldura). **Regra para as levas 2 a 12** gravada na ficha, seção 7.4 (recomendações L2-1 a L2-4 da gbq-estilo, generalizadas, mais uma regra derivada do D3-R02): fecho neutro do D4 com ao menos 2 C na 8.4 da leva 2 e nenhum E novo com ele até 40% de C; "Considere que" ≥ 40% C e declarativos ≥ 40% E por leva; fórmula "Nessa situação, nos termos d…" em no máximo metade dos "Considere que" do D3; ao menos 1 C com ", e não …" no D4; sujeito trocado plausível em todo SUJ; vedada a negação frontal de cenário que enumera todos os elementos. K1 a K4, a cota de E com moldura e a R3 prevalecem. À GBQ: a leva 1 não forma simulado isolado (seção 5).

### 4.4 Pendência 4 — AJ-E1 e AJ-E3 (texto do estilo)
- **AJ-E1 (D3-R13, enunciado): NÃO aplicado ao objeto; registrado como ERRATA para a v1.14.** Caminho escolhido para que nenhum item chegue ao gatilho sem QA: o objeto aceito é o v2 tal como aprovado no R1/R2 (30 de 30 com QA), e a D-REFORCO-DA limita a QA a 2 rodadas (uma conferência nova da gcb-cqfp seria a terceira). A errata é texto exato fixado por agente de QA independente (gbq-estilo, opus, que não produziu), transcrito sem redação nova, só com ordem direta, e o "depois" é a letra do CDC, art. 22, caput (conferido no cache); não muda gabarito (C), ponto (A6.3-12), mecanismo (C2), formato (SUJ) nem outro campo — o caso da D-V112-BAEF-P2-ACEITE, e não o da D-T98-ONDA4-ACEITE (sugestão sem texto exato). Aplicação na T-123 pela GBQ, por substituição exata com aborto se o "antes" não ocorrer exatamente 1 vez na seção 1 do v2, registrada por id no registro de alterações da v1.14 e conferida pela gbq-cqe na fidelidade:
  - antes: «são obrigados a fornecer serviços adequados, eficientes, seguros e, quanto aos essenciais, contínuos os órgãos públicos, por si ou suas empresas, concessionárias, permissionárias ou sob qualquer outra forma de empreendimento.»
  - depois: «os órgãos públicos, por si ou suas empresas, concessionárias, permissionárias ou sob qualquer outra forma de empreendimento, são obrigados a fornecer serviços adequados, eficientes, seguros e, quanto aos essenciais, contínuos.»
  - Se a presidência não aceitar a errata, o D3-R13 entra na v1.14 como aprovado no R2 (o defeito é de clareza, sem erro de gabarito).
- **AJ-E3 (D3-R02, opcional): NÃO aceito.** Muda a construção do E e o campo Troca, e a própria gbq-estilo diz que volta à gcb-cqfp; seria QA fora do rito. O D3-R02 fica como aprovado (E, troca literal declarada, não decidido pela moldura); a pista moderada fica registrada e a regra 7.4.5 da ficha a previne nas levas seguintes. Errata futura só com QA e aceite próprios (precedente D-T98-ONDA4-ACEITE), sem tarefa aberta agora (D-COMPLEMENTOS).
- **AJ-E2: NÃO aplicado ao arquivo** (é texto do bloco à GCB, não de item); as notas (g) e (h) entram na lista da seção 5, que prevalece.

### 4.5 Pendência 5 — notas de simulado: ver seção 5 (destino T-119 e T-123).

### 4.6 Outros registros (D1)
1. Nome dos arquivos: ficam os nomes do despacho (leva1, e não L01), sem renomear, para não quebrar SHA-256 e referências; o padrão fica fixado na ficha 7.5.
2. R-2 do R2: a página de R54, alínea d (D4-R18), é **p. 20**, e não "p. 19-20"; vale este registro na consolidação (proveniência), sem mudar o item.
3. K2 a K4 com +1 C sobre a ficha 3.6 (D4-R18, C, "Considere que um analista…", fecho de acerto, "pós-NPM"), prescrito pelo R1; todos em 40–60%.
4. Desvios 1 a 5 da produção (seção 5 do v2), aceitos no R1 (seção 6): confirmados. Em especial, a 6.3 e a 8.1 ficam com DEF no teto (6/20).
5. Faixas de ids: leva 2, 8.4 = D4-R19 a D4-R28; D4 seguinte deslocado em +1 (ficha 7.1).

## 5. Notas de simulado — "não pôr no mesmo simulado" e restrições de uso (destino: T-119, regra de montagem; e T-123, campos de montagem)
| # | itens | motivo | origem |
|---|---|---|---|
| (a) | D3-R03, D3-R07, D3-R11 e D5-37 (10.4) | mesma hipótese do art. 121, § 2º, da Lei 14.133; no máximo dois dos três D3-R por simulado e nenhum deles com o D5-37 | v2, bloco à GCB; ficha 0.2, item 8; R1, seção 8 (a) |
| (b) | D4-R07 × D4-01 | associação mercado × redes | AJ-4 |
| (c) | D4-R02 × D4-05 | confiança mútua | AJ-2 |
| (d) | D3-R04 × D3-R13 | mesmo art. 22 do CDC; o cenário do R04 contém os sujeitos do R13 | R1, seção 8 (d) |
| (e) | parciais da 6.3: D3-R01, R04, R06, R08, R09, R10, R12, R13 | só simulado diagnóstico | D-ADERENCIA |
| (f) | D3-R05 × D3-R02 | mesmo art. 186 do CC (preventiva) | v2, bloco à GCB |
| (g) | D4-R03 × D4-R18 | mesma abertura e mesma lista; o "fortalecimento" do R18 (C) sinaliza o erro do R03 (E) | estilo, AJ-E2 |
| (h) | D4-R15 × D4-R16 | mesma abertura, mesma fonte (TCU, unidades de apoio), mesmo fecho e mesmo gabarito E | estilo, AJ-E2 |
| (i) | a leva 1 inteira (ou só itens de reforço) | não forma simulado isolado; entra misturada por folha com os canônicos (CQ → E acerta 73,3% na leva isolada) | estilo, seção 4.1 e rec. "À GBQ" |
| (j) | os 11 itens com moldura (D4-R02, R06, R08, R14, R15, R16, R17; D3-R02, R03, R07, R11) | contam para o teto de 50% de C com moldura por simulado enquanto a moldura de DA estiver acima de 60% (hoje 71,9%) | D-MOLDURA-CE (c) |
Os 30 só vão a simulado depois do gatilho A aceito e da consolidação (D-QA-PENDENTE); nenhum é VOLÁTIL.

## 6. Para a GBQ (T-123, consolidação v1.14)
1. Fonte: saida/gcb/DA_reforco_leva1_v2.md (2c431529…), com esta reconciliação prevalecendo (precedente D-T89-R1-ACEITE).
2. Errata AJ-E1 (seção 4.4), se aceita no gatilho A.
3. Ordem dentro da folha (seção 4.1 (iii)); núcleo pela seção 4.2 (8.1 D4-R01–R04; 6.3 D3-R02, R03, R05; 8.4 D4-R15–R17; os demais false).
4. Aderência: 8 parciais na 6.3 (seção 2); proveniência do D4-R18 com p. 20.
5. Ato de aceite desta leva para os 30 ids no gerador (T-123: "ato de aceite de cada leva").

## 7. Pendências com destino
| pendência | destino | condição |
|---|---|---|
| D4-R19 = C sem [TS]; teste da 8.4 de 20 | ficha da leva 2 (GCB) e reconciliação da leva 2 | antes do despacho da leva 2 |
| Regras 7.4 (pista) e 7.3 (sequência sobre o plano) | fichas das levas 2 a 12 (GCB); conferência na gcb-cqfp e na gbq-estilo | toda leva |
| Errata AJ-E1 do D3-R13 | T-123 (GBQ), registro de alterações da v1.14; fidelidade gbq-cqe | se aceita no gatilho A |
| AJ-E3 do D3-R02 | nenhum (registro); errata futura só com QA e aceite próprios | não aberta |
| Notas (a) a (j) | T-119 (regra de montagem, GBQ) e T-123 | antes do primeiro simulado com DA |
| Núcleo e ordem na folha | T-123 (GBQ) | consolidação |
| Moldura de DA 46/18 (71,9%) | levas 2 a 5 (plano da ficha 2.2); recontagem oficial da GBQ na v1.14 | meta prevista na leva 5 |
| Leva 2 | pode abrir: o QA da leva 1 está fechado (R2 último) | D-REFORCO-DA: nenhuma leva nova com QA da anterior aberto |

## 8. Gatilho
Tudo em condição: QA independente concluído em 2 rodadas (0% na R2), estilo sem NÃO CONFORME, contagens, C/E, formatos, moldura e SHA-256 conferidos por script, ressalvas fechadas pelas decisões da seção 4. Gatilho A escrito em PARA_PRESIDENCIA.md (um item). Nada vai à plataforma nem à candidata sem o sim do Fundador.

FIM DA RECONCILIAÇÃO — LEVA 01 — REFORÇO DA
