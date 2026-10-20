# QA_DA_reforco_leva1_R1_2026-10-20_gcb-cqfp.md — T-116 — 2026-10-20 — gerado por gcb-cqfp

# PARECER QA R1 — LEVA 1 DO REFORÇO DE DA (D-REFORCO-DA) — ciclo s15c3
QA independente (gcb-cqfp, opus). Não produziu o texto revisado e não reescreve itens: dá veredito, ajuste com texto exato e motivo de reprovação. O arquivo da produção não foi alterado. Sem commit nem push. Sem leitura externa (D-REFORCO-DA): as bases foram conferidas nos adendos e nas cópias de saida/gcb/normativo_cache/ (ficha, seção 4.4, item 8).

## 0. Objeto, entradas e método
| objeto | SHA-256 |
|---|---|
| saida/gcb/DA_reforco_leva1_v1.md (objeto do R1; 30 itens) | 047949049703a052b6233b6d5bb31b98021425a1854a768dbfd4ae1096215f01 |
| saida/gcb/DA_reforco_ficha_2026-10-20.md (critérios: seções 1, 3 e 4) | acf8b57af3f42e0bcab9a6d92f6cfa3dd70deacf3f521fc285e5b3a1b0d95133 |
| saida/gcb/D4_anexo_N_adendo_2026-10-20.md | c32f58eb78507f8c415c9b79f9cfdde0dfefdb7314ddd23045d312cb03d16fb5 |
| saida/gcb/D3_anexo_N_adendo_2026-10-20.md | c8ad5bd23bf94d6fb74b300d789fa8a21c76fc7349748ba468f68576b9f74a50 |
| saida/gcb/D4_v2_1.md (canônicos 8.1 e 8.4) | c1a7a93598e9fd37b2009b9feaca3afd3898fa05f6f66e6de26dd40c2839e5d9 |
| saida/gcb/D3_v2_1.md (canônicos 6.3) | 0f7a8b090fe6f2243ae55b36273dacdb719aaf04b19548dce70aad4867798930 |
| saida/banco/moldura_ce_itens_2026-10-20.csv | ed4b364dffbca7d9e8878591914783258fa7048c4f1837d98c3d62e34981daac |

Método (python3 -I, scratchpad da sessão, somente leitura): (a) extração dos 30 blocos e dos 30 enunciados; (b) cada trecho da coluna Base procurado como subcadeia no adendo e na cópia do cache (aspas e espaços normalizados), com contagem de palavras e conferência de URL e data; (c) contagens C/E, formatos, moldura, aderência, [TS], VOLÁTIL, por folha e na leva, com os canônicos; (d) partida de moldura recontada no CSV (DA 44 C / 9 E; D3 6/1; D4 12/0); (e) teste de sequência da ficha (corrida ≥ 4, alternância > 4, bloco de período 2 a 8 por max(8, 2p)) refeito do zero; (f) unicidade de cada trecho de ajuste no arquivo e aplicação simulada. Leitura manual do contexto, no cache, de R37, R39, R40 (F5), R53, R55, R57, R83 e Quadro 1 (F6), R72 (F7), R63 e R64 (F1), Lei 14.133, art. 121; Lei 8.112, arts. 122 e 124; CDC, art. 22; Lei 6.938, arts. 3º, IV, e 14, § 1º; CC, arts. 186 e 927.

## 1. Veredito geral
- APROVADO: 24. AJUSTAR: 5 (D4-R02, D4-R03, D4-R07, D3-R01, D3-R07). REPROVADO: 1 (D4-R12).
- **Taxa de reprovação: 1/30 = 3,3%** (abaixo do gate de 30%; sem GATE).
- **Veredito da leva: APROVADA COM AJUSTES**, condicionada a: 7 AJ aplicados literalmente (seção 3), substituição do D4-R12 (seção 4) e decisão da GCB sobre a sequência de [TS] da 8.4 acumulada (seção 5, C4).
- Gabarito: os 30 gabaritos conferem com a letra da base; nenhum E por ausência; nenhum E decidido pela moldura; nenhum item afirma SEM FONTE (A11, B3, B4, B7), efeito de decisão do STF, norma interna da Câmara ou alcance do Decreto 9.203.
- Cota de E com moldura: 9 de 9 aprovados (8.1: D4-R06, R08, R14; 6.3: D3-R02, R07, R11; 8.4: D4-R15, R16, R17); nenhuma reposição de moldura necessária (margem da leva 5 preservada).

## 2. Veredito por item
Colunas de conferência: G = gabarito pela letra; P = ponto único e pertinência; T = troca legítima (E) / [TS] coerente; F = sem pista de forma no item; Gm = não gêmeo (canônico da folha e leva); M = moldura; J = justificativa e proveniência (trecho literal no adendo e no cache, URL e data). "ok" = confere.

### Folha 8.1 (D4-R01 a D4-R14)
| id | ponto | G | P | T | F | Gm | M | J | veredito |
|---|---|---|---|---|---|---|---|---|---|
| D4-R01 | A8.1-07 / R37 | C ok | ok, direta | sem TS, ok | ok | ok | N ok | ok (paráfrase fiel da parte "sic", B9) | APROVADO |
| D4-R02 | A8.1-09 / R39 | C ok | ok, direta | sem TS, ok | ok | vizinho do D4-05 (confiança) | S, expositor, acerto ok | "Difere de" incompleto | AJUSTAR (AJ-2) |
| D4-R03 | A8.1-27 i / R55 | E ok | ok, direta (pós-NPM, B6) | fortalecimento → enfraquecimento, ok | ok | ok | N, analista, acerto ok | "Difere de" só aponta item de outra folha | AJUSTAR (AJ-3) |
| D4-R04 | A8.1-14 / R43 | C ok | ok, direta | ok | ok | ok (elemento novo: múltiplos atores) | N ok | ok | APROVADO |
| D4-R05 | A8.1-10 / R39 | C ok (C6) | ok, direta | ok | ok | ok | N ok | ok (sem "copojetar", B9) | APROVADO |
| D4-R06 | A8.1-11 / R40 | E ok | ok, direta | informal → formal, ok | ok | ok | S, expositor, acerto ok | ok (contexto da p. 35 conferido: a citação seguinte não altera a frase) | APROVADO |
| D4-R07 | A8.1-20 / R46 | C ok | ok, direta | ok | ok | sobrepõe-se ao D4-01 (mercado × redes) | N ok | "Difere de" omite D4-01 | AJUSTAR (AJ-4) |
| D4-R08 | A8.1-16 / R45 | E ok | ok, direta | capital social → econômico, ok | ok | ok | S, expositor, neutro ok | ok | APROVADO |
| D4-R09 | A8.1-26 / R53 | E ok | ok, direta (pós-NPM) | polos invertidos, ok | ok | ok | N, analista, acerto ok | ok | APROVADO |
| D4-R10 | A8.1-29 / R57 | E ok | ok, direta; "pós-NPM do debate de governança" sustentado pelo título do Quadro 1 de F6 ("Pós-NGP no debate de governança pública") | direcionador → remador, ok | ok | ok | N ok | ok | APROVADO |
| D4-R11 | A8.1-18 / R46 | C ok | ok, direta | ok | ok | ok | N ok | ok ("Regulatório" conferido na linha da Tabela nº 2 no cache) | APROVADO |
| D4-R12 | A8.1-13 / R42 | C ok | **gêmeo** | — | — | **falha** | N | — | **REPROVADO** (seção 4) |
| D4-R13 | A8.1-30 / R83 | E ok | ok, direta (Quadro 1 de F6: "Foco … Cidadão como parceiro") | parceiro → beneficiário final, ok | ok | ok | N, analista, neutro ok | ok | APROVADO |
| D4-R14 | A8.1-15 / R44 | E ok | ok, direta | só a versão E (B4), ok | "integralmente" é literal de R44; registro à gbq-estilo | ok | S, expositor, acerto ok | ok | APROVADO |

### Folha 6.3 (D3-R01 a D3-R13)
| id | ponto | G | P | T | F | Gm | M | J | veredito |
|---|---|---|---|---|---|---|---|---|---|
| D3-R01 | A6.3-03 / CC, art. 927, caput | C ok | **aderência mal declarada** (seção 2.1) | sem TS, ok | ok | ok | N ok | ok | AJUSTAR (AJ-5) |
| D3-R02 | A6.3-01 / CC, art. 186 | E ok | ok, direta; não toca A11 (nada afirma sobre o Estado) | negação da omissão voluntária, ok (E3) | negação frontal de cenário que descreve todos os elementos do art. 186: item fácil; registro à gbq-estilo | ok | S, Legislativo da União ok | ok | APROVADO |
| D3-R03 | A6.3-07 / Lei 14.133, art. 121, § 2º | C ok (C6; omite o tipo de responsabilidade, ponto do D3-R11) | ok, direta | ok | ok | ok (ver nota GBQ (a)) | S ok (C do par R3) | ok | APROVADO |
| D3-R04 | A6.3-11 / CDC, art. 22, p. único | C ok | ok, parcial (A7) | ok | ok | ok | N ok | ok | APROVADO |
| D3-R05 | A6.3-02 / CC, art. 186 | C ok | ok, direta (adendo §4.2: art. 186 "núcleo 6.3") | ok | ok | ok (elemento distinto do D3-R02) | N ok | ok | APROVADO |
| D3-R06 | A6.3-06 / Lei 8.112, art. 124 | E ok | ok, parcial (A1) | no → fora do desempenho, ok | ok | ok | N ok | ok; formato DEF aceito (seção 6, desvio 1) | APROVADO |
| D3-R07 | A6.3-09 / Lei 14.133, art. 121, § 2º | E ok ("Exclusivamente" é rol fechado; caput "Somente o contratado"; § 1º) | ok, direta | ok | ok | vizinho do D5-37 (10.4), nota já feita | S ok | **mecanismo mal declarado** (E6 → E3) | AJUSTAR (AJ-6) |
| D3-R08 | A6.3-14 / Lei 6.938, art. 14, § 1º | E ok | ok, parcial; 2ª frase não usada (A12) | independentemente de culpa → depende, ok | ok | ok | N ok | ok | APROVADO |
| D3-R09 | A6.3-05 / Lei 8.112, art. 122, caput | C ok | parcial (A1); pertinência fraca (o elemento julgado não é a omissão), aceita pela classificação do adendo | sem TS, ok | ok | ok (elemento distinto do D3-R12) | N ok | ok | APROVADO |
| D3-R10 | A6.3-13 / Lei 6.938, art. 3º, IV | C ok (C3, isca literal "de direito público"; única C-isca da folha) | ok, parcial | ok | ok | ok | N ok | ok | APROVADO |
| D3-R11 | A6.3-08 / Lei 14.133, art. 121, § 2º | E ok | ok, direta | permuta solidária ↔ subsidiária, ok | ok | ok | S ok | ok | APROVADO |
| D3-R12 | A6.3-04 / Lei 8.112, art. 122, caput | C ok | ok, parcial (A1, sujeito nomeado) | sem TS, ok | ok | ok | N ok | ok | APROVADO |
| D3-R13 | A6.3-12 / CDC, art. 22, caput | C ok | ok, parcial (A7) | sem TS, ok | ok | ok | N ok | ok | APROVADO |

### Folha 8.4 (D4-R15 a D4-R17)
| id | ponto | G | P | T | F | Gm | M | J | veredito |
|---|---|---|---|---|---|---|---|---|---|
| D4-R15 | A8.4-06 / R63 (TCU) | E ok | ok, direta; atribuição ao TCU conforme ficha 0.2, item 4 | internos → externos, ok | ok ("quase sempre" literal) | ok | S, expositor, acerto ok | ok | APROVADO |
| D4-R16 | A8.4-08 / R64 (TCU) | E ok | ok, direta | liderança → unidades de apoio (troca de sujeito), ok | ok | ok | S, acerto ok (formato APL prevalece sobre SUJ) | ok (sem "de acordo os", B9) | APROVADO |
| D4-R17 | A8.4-16 / R72 | E ok | ok, direta | não geram → geram, ok | ok | ok | S, neutro ok | ok | APROVADO |

### 2.1 Fundamentos dos vereditos que não são APROVADO
- **D4-R12 — REPROVADO** (ficha 4.1, item 3: gêmeo de canônico da mesma folha). O ponto decisivo do item (mercados ↔ nova gestão pública; redes ↔ NPG) é o ponto 8.1-1 do D4-01 com o sinal trocado: o D4-01 é E por atribuir o mercado à NPG ("O princípio orientador do mercado resulta na Nova Governança Pública"), e a tentação que a própria justificativa do D4-R12 aponta é "deslocar os mercados para a NPG" — a mesma troca. O terceiro elemento (hierarquia ↔ administração pública tradicional) já está na mesma frase de Cavalcante que sustenta o D4-03 (R8: hierarquia, mercado, redes) e na justificativa do D4-01. A ficha já excluíra o A8.1-02 (NPM ↔ mercado; NPG ↔ rede) como gêmeo do D4-01; o A8.1-13 contém esse ponto. Além disso, na própria leva, o D4-R07 repete a associação NPG ↔ networks e nova gestão pública ↔ mercado. O próprio bloco à GCB (nota (b)) registrou o contato com o D4-01. Não há ajuste de texto exato que dê ao item um ponto novo.
- **D3-R01 — AJUSTAR (aderência)**. O enunciado reproduz o art. 927, caput, sem nenhum elemento de omissão ou do Estado; a pertinência à 6.3 só existe pela remissão ao art. 186 (que inclui a omissão), e a ligação desse regime à omissão estatal é exatamente o que o alerta A11 deixa sem fonte. O próprio adendo do D3 (seção 4.2) classifica o art. 927, caput, como "núcleo 6.4; compl. 6.3" (a tabela 3.1 diz "direta": divergência interna do adendo; vale, para a 6.3, a leitura de complemento). Aderência: parcial. A 6.3 fica com 7 + 5 = 12 diretos (piso de 10 mantido).
- **D3-R07 — AJUSTAR (mecanismo)**. E6 (regra relativa convertida em absoluta, com "sempre", "só" etc.) não descreve a construção: o item estende a hipótese restrita do § 2º a caso fora dela, isto é, altera a condição do comando (E3, regras/estilo_banca.md, linha 404, passo 2).
- **D4-R02, D4-R03, D4-R07 — AJUSTAR ("Difere de")**. Campo incompleto ou impertinente (ficha 4.2): o D4-R02 afirma a confiança mútua, elemento cuja troca decide o D4-05; o D4-R07 repete a associação mercado × redes do D4-01; o D4-R03 aponta só o D4-08 (folha 8.2), sem o canônico mais próximo da folha (D4-03, D4-06). Os ajustes acrescentam as notas "não pôr no mesmo simulado".

## 3. Ajustes com texto exato (ficha 4.3)
Convenção: dentro de «», a sequência \n representa quebra de linha do arquivo; todo o resto é literal. Cada trecho atual foi conferido por script: ocorre exatamente uma vez em saida/gcb/DA_reforco_leva1_v1.md.

AJ-1 | arquivo (linha 3) | cabeçalho | substituir: «LEVA 1 de 2: 30 itens» | por: «LEVA 1 de 12: 30 itens»

AJ-2 | D4-R02 | Difere de | substituir: «aqui se julga o resultado do tipo ideal, o “Estado de rede” (R39).» | por: «aqui se julga o resultado do tipo ideal, o “Estado de rede” (R39); e D4-05 porque este julga, com troca de “confiança” por “concorrência”, o que o governo apoia na rede (R7), e aqui a confiança mútua é o princípio de ligação do “Estado de rede” (nota ao simulado: não pôr D4-R02 e D4-05 no mesmo simulado).»

AJ-3 | D4-R03 | Difere de | substituir: «- Difere de: D4-08 (folha 8.2) porque este julga outra alínea da mesma lista (colaboração, parcerias e atuação em redes); aqui, a alínea i.» | por: «- Difere de: D4-03 porque este julga a fonte inspiradora do pós-NPM (as redes, R8), e D4-06 porque este julga a relação do pós-NPM com integração, colaboração e processo decisório inclusivo (R4); aqui se julga a alínea i da lista de tendências (R55). Fora da folha: D4-08 (folha 8.2) julga as alíneas a e b da mesma lista.»

AJ-4 | D4-R07 | Difere de | substituir: «- Difere de: D4-04 porque este julga os fundamentos teóricos da NPG (R7); aqui se julga o mecanismo de alocação de recursos (R46); e D4-R11» | por: «- Difere de: D4-01 porque este julga qual princípio orientador resulta na NPG (as redes, e não o mercado; R6), e aqui se julga o mecanismo de alocação de recursos, com os contratos relacionais (NPG) e os clássicos ou neoclássicos (nova gestão pública) (R46) (nota ao simulado: não pôr D4-R07 e D4-01 no mesmo simulado); D4-04 porque este julga os fundamentos teóricos da NPG (R7); e D4-R11»

AJ-5 | D3-R01 | Aderência | substituir: «- Aderência: direta\n- Gabarito: C\n- Justificativa (linha 1): O art. 927, caput,» | por: «- Aderência: parcial\n- Gabarito: C\n- Justificativa (linha 1): O art. 927, caput,»

AJ-6 | D3-R07 | Mecanismo | substituir: «- Mecanismo: Regra relativa convertida em absoluta (E6)» | por: «- Mecanismo: Alteração do comando normativo (E3)»

AJ-7 | arquivo (seção 4.3) | nota do teste de sequência | substituir: «Nota: na 8.4 acumulada, o teste de [TS] é informativo; a folha só fecha na leva 2, que reordena dentro da faixa D4-R18 a R27 e pode quebrar o bloco de período 3 já presente nos canônicos (nTTnTTn). Os resultados REPROVADO que apareçam nas linhas “8.4 acumulada” não valem como falha desta leva.» | por: «Nota: na 8.4 acumulada, o bloco de período 3 da sequência de [TS] (nTTnTTnTT) atinge 8 itens no D4-R15 e nenhuma ordem da leva 2 o desfaz, porque os itens da leva 2 vêm depois do D4-R17 e os três itens da 8.4 desta leva têm [TS]; desvio registrado para decisão da GCB (parecer QA R1 da leva 1, conferência C4).»

Efeito derivado (não é AJ; a v2 refaz por script): seções 0 e 4 com a aderência da 6.3 em 12 diretos / 8 parciais (leva: 22 / 8 com o substituto do D4-R12), a remoção do D4-R12 e a entrada do substituto.

## 4. Reprovação e substituição (ficha 4.1, último parágrafo; regra 12)
- D4-R12 sai; o id não volta. Substituto: **D4-R18** (próximo id livre do lote D4), folha 8.1. Consequência: a faixa da 8.4 na leva 2 passa a D4-R19 a D4-R28 (ficha 2.1: "deslocam-se se houver substituição").
- Ponto do substituto (reserva da 8.1, na ordem da ficha, com motivo de cada salto): A8.1-04 não (R35, cooperação e solidariedade do modelo de rede: vizinho do D4-05, cooperação mútua, e mais um C sobre "rede" — seção 7, item 2); A8.1-21 não (só admite E e mudaria o C/E da folha; além disso espelha o D4-R14, não substituição); A8.1-19 não (terceira célula da Tabela nº 2 na mesma folha, depois do D4-R07 e do D4-R11). **Primeiro ponto aceitável: A8.1-27, uma alínea entre d, e, g ou h** (não a: e b: D4-08; não c: "integração" vizinha do D4-06; não i: D4-R03).
- Construção que mantém todas as faixas: gabarito C; formato SIT; abertura "Considere que um analista…"; "pós-NPM" escrito por extenso como nos D4-R03 e D4-R09; fecho de acerto ("ele estará correto ao incluir entre elas…") ou neutro; Moldura N; aderência direta; sem [TS] (C sem isca); "Difere de" D4-R03 (alínea i da mesma lista) e D4-08 (alíneas a e b, folha 8.2). Efeitos: leva 15/15; 8.1 10/10; 8.1 SIT 5 (teto 6); K2 7/6 (53,8%) com fecho de acerto ou 6/6 com neutro; K3 5/4 (55,6%); K4 23/17 (57,5%); "Considere que" na folha 8.1 sobe de 3 C / 6 E (33%) para 4 C / 6 E (40%).
- **Posição**: o D4-R18 fica no lugar do D4-R12 (entre D4-R11 e D4-R13). Simulado por script: nessa posição as sequências de gabarito e de [TS] (folha, folha acumulada e leva) ficam idênticas às da v1 e passam; no fim da folha (depois do D4-R14) reprovam (bloco de período 4, 8/8, nas oito sequências testadas).

## 5. Conferências de leva (ficha 4.4)
| # | conferência | resultado | registro |
|---|---|---|---|
| C1 | C/E da leva | CONFERE | 15 C / 15 E (50%); com o substituto C, 15/15. Folhas: 8.1 10/10; 6.3 10/10; 8.4 4/6 parcial (fecha na leva 2) |
| C2 | tetos de formato, VOLÁTIL, moldura ≤ 6, piso de 10 diretos | CONFERE | 8.1: DEF 6, SIT 4, PAR 5, APL 5 (após a substituição: DEF 6, SIT 5, PAR 4, APL 5); 6.3: DEF 6, SUJ 2, SIT 5, PAR 2, APL 5; 8.4: APL 4 de 10 (5 no fim). DEF no teto em 8.1 e 6.3 (margem zero: nenhum item novo DEF nessas folhas). VOLÁTIL 0. Moldura: 8.1 5; 6.3 5; 8.4 4. Diretos: 8.1 20; 6.3 12 (com AJ-5); 8.4 10 |
| C3 | moldura acumulada e conjuntos | CONFERE | partida recontada no CSV: DA 44/9, D3 6/1 (D3-07, 18, 28, 45, 58, 70, 74), D4 12/0. Depois da leva: DA 46/18 (71,9%); D3 7/4; K1 13/6; K2 6/6; K3 4/4; K4 22/17 — iguais à ficha 3.6 (com o substituto: K3 5/4, K4 23/17, K2 7/6 ou 6/6; todos em 40–60%) |
| C4 | teste de sequência | **NÃO CONFERE (só [TS] da 8.4 acumulada)** | gabarito: todas as linhas passam (refeito). [TS]: 8.1, 6.3, leva e 8.4 da leva passam; 8.4 acumulada nTTnTTnTTT reprova (período 3, 9/8). O bloco fecha no D4-R15 (posição 8) e não é desfeito pela leva 2 — a nota da seção 4.3 da v1 está errada (AJ-7). Causa: o plano da ficha (8.4 = 0 C / 3 E nesta leva; todo E com troca leva [TS]); não há troca de posição dentro da leva que resolva. **Decisão da GCB**: aceitar e registrar na reconciliação, ou redistribuir a 8.4 entre as levas 1 e 2 (pôr na leva 1 um item da 8.4 sem [TS]) |
| C5 | pontos sem duplicata | CONFERE entre si; **NÃO CONFERE com os canônicos** | 30 códigos distintos; D4-R12 gêmeo do D4-01 (seção 2.1). Ponto do substituto conferido contra D4-01 a D4-06, D4-08 e os itens da leva |
| C6 | exigências da leva (2.3) | CONFERE | (a) cota de E com moldura 9/9 e conjuntos K1 a K4; (c) nenhum item da 8.4 usa o Decreto 9.203, art. 2º, II, nem o art. 4º, IV; (d) 6.3 com aderência parcial declarada e piso de diretos |
| C7 | ids, linha 1 e última linha | CONFERE, com registro | D4-R01–R17, D3-R01–R13; linha 1 no formato; última linha "FIM DA LEVA 01 — REFORÇO DA". Cabeçalho "LEVA 1 de 2" errado (AJ-1). Nome do arquivo difere da ficha (regra 14: DA_reforco_L01_v1.md); a produção seguiu o despacho — a GCB decide na reconciliação |
| C8 | bases | CONFERE | 36 trechos: 36 no adendo, literal; 34 subcadeias da cópia do cache; 2 (D4-R07, D4-R11) juntam o rótulo da coluna à célula da Tabela nº 2, ambas conferidas nas linhas 10 e 11 da cópia de F11. Nenhum trecho passa de 25 palavras. URL e data (20/10/2026) idênticas às do adendo em 30 de 30. Nenhum [SEM FONTE] afirmado em item (a única ocorrência está na nota da Base do D4-R12, que sai) |

## 6. Avaliação dos desvios declarados (seção 5 da v1)
1. A6.3-06 (D3-R06) como DEF, e não PAR — **ACEITO**. A troca nega um qualificador do art. 124 ("no desempenho" → "fora do desempenho") sem pôr o conceito vizinho no lugar; o D3-R08 continua PAR porque a troca coloca o regime vizinho (culpa × independentemente de culpa). Efeito: 6.3 com DEF no teto (6).
2. Uma só C-isca na 6.3 (D3-R10) e nenhuma em 8.1 e 8.4 — **ACEITO** (limite: 1 por folha; a 8.4 já tem a do D4-32).
3. Paráfrases de R37 e R39 sem as grafias defeituosas — **ACEITO** (B9; sentido conferido no cache, p. 25 e 33).
4. Fecho "neutro" nos itens com moldura do D3 — **ACEITO** (K2 é conjunto do D4).
5. Fecho neutro em A8.1-16, A8.4-16 e A8.1-30 — **ACEITO** (é o plano da ficha 3.6).
6. Atribuição: B6/B2 do adendo pedem o autor; a ficha (0.2, item 4) proíbe autor nomeado — **ACEITO**, prevalece a ficha; nenhum item nomeia autor; A8.4-06 e A8.4-08 atribuídos ao TCU, como a ficha manda. Registro: os itens de Silvestre, Bouckaert, Cavalcante e Martins afirmam, sem atribuição, proposições de autor; é a escolha da ficha (ficha do D4, 3.2), não falha do item.
7. Tabela nº 2 (fonte da tabela: Osborne, 2010) em A8.1-18 e A8.1-20 — **ACEITO** (pontos escolhidos pela ficha; a verdade das células não depende de nomear Osborne; "Aberto fechado" não usado, B7).
8. Dúvidas (i) a (iii) — (i) D3-R02 não se aproxima do A11: aplica o art. 186 à conduta do servidor e nada afirma sobre a responsabilidade do Estado; reserva A6.3-15 não acionada. (ii) D4-R17 sem atribuição: conforme a ficha. (iii) CDC pela letra, sem o art. 37, § 6º: conforme A7.
9. Núcleo — **REGISTRO À GCB**: com o AJ-5, o D3-R01 (núcleo pela ordem de id) passa a parcial; a GCB decide se o núcleo da 6.3 recai nos três primeiros diretos aceitos (D3-R02, D3-R03, D3-R05) ou se mantém a regra da ordem de id (ficha 0.2, item 10). Na 8.1, com a saída do D4-R12 e a entrada do D4-R18, os quatro primeiros aceitos por ordem de id continuam D4-R01 a D4-R04.

## 7. Observações (não reprovam; à GCB e à gbq-estilo)
1. Pista de abertura no D4 (leva): "Considere que" 1 C / 9 E; enunciado declarativo 6 C / 1 E. Em nível de lote o K4 está na faixa (22/17), mas, dentro da folha 8.1, "Considere que" fica em 3 C / 6 E (33%). O substituto recomendado na seção 4 leva a 4/6 (40%). Fecho "Nessa situação, é correto afirmar que" na leva: 0 C / 3 E (D4-R08, R13, R17) — a gbq-estilo pode pedir C com esse fecho na leva 2.
2. Pista lexical na 8.1: os itens cuja verdade gira em torno de "rede(s)/networks" ficam 6 C / 2 E na folha final (sem o D4-R12). É conteúdo nuclear da NPG, não falha de item; a reserva não deve acrescentar outro C sobre "rede" (motivo do salto do A8.1-04).
3. Concentração na 6.3: três itens sobre o mesmo § 2º do art. 121 da Lei 14.133 (D3-R03, R07, R11; 15% da folha) e dois sobre o mesmo caput do art. 122 da Lei 8.112 (D3-R09, R12). Pontos distintos, aceitos; ver notas à GBQ.
4. Estilo (amostra da gbq-estilo e itens a acompanhar): D3-R02 (negação frontal de cenário que descreve todos os elementos do art. 186 — item fácil); D4-R14 ("integralmente", literal de R44, em item E).

## 8. Notas à GBQ (simulado)
(a) D3-R03, D3-R07 e D3-R11 (art. 121, § 2º) e D5-37 (10.4): mantida a nota da v1 (no máximo dois dos três por simulado; nenhum deles com o D5-37). (b) D4-R07 e D4-01 (AJ-4). (c) D4-R02 e D4-05 (AJ-2). (d) D3-R04 e D3-R13 (mesmo art. 22 do CDC; o cenário do D3-R04 contém os sujeitos que o D3-R13 julga): não no mesmo simulado. (e) Parciais da 6.3 (D3-R01 após o AJ-5, R04, R06, R08, R09, R10, R12, R13): só simulado diagnóstico (D-ADERENCIA).

## 9. O que a v2 deve fazer
1. Aplicar AJ-1 a AJ-7 por substituição exata, sem outra mudança nos trechos.
2. Retirar o D4-R12 (enunciado, bloco, linhas das seções 3.2 e 4.5 e a nota (b) do bloco à GCB); não reutilizar o id.
3. Incluir o substituto D4-R18 (folha 8.1) com ponto da reserva conforme a seção 4 (A8.1-27, alínea d, e, g ou h; C; SIT; "Considere que um analista…"; "pós-NPM"; sem [TS]; Moldura N; direta), com todos os campos da regra 14 e trecho literal de R54 ou R55 (até 25 palavras, idêntico ao adendo); posicioná-lo entre D4-R11 e D4-R13; se a produção escolher outro ponto, declarar o motivo no bloco à GCB e manter gabarito C, teto de formato (nenhum DEF novo na 8.1) e faixas de K2 a K4.
4. Registrar no bloco à GCB o deslocamento da faixa da 8.4 na leva 2 (D4-R19 a D4-R28).
5. Refazer por script as seções 0 e 4 (contagens, formatos, aderência — 6.3 com 12 diretos e 8 parciais —, moldura, K1 a K4, teste de sequência, lista de pontos) sobre o arquivo da v2.
6. Registrar no bloco à GCB a decisão pendente sobre a sequência de [TS] da 8.4 acumulada (C4) e sobre o núcleo da 6.3 (seção 6, item 9).
7. Resposta item a item a este parecer (acatado / não acatado + motivo), como no PADRAO_UNICO, seção 3. O R2 confere cada AJ literalmente, o substituto por inteiro e só o que mudar além disso.

FIM DO PARECER QA R1 — LEVA 01 — REFORÇO DA
