# QA_DA_reforco_leva3_R2_2026-10-22_gcb-cqfp.md — T-116 — 2026-10-22 — gerado por gcb-cqfp

# PARECER QA R2 (ÚLTIMA RODADA) — REFORÇO DA, LEVA 3 (v2) — ciclo s16c1
A gcb-cqfp (opus) faz este QA de forma independente. Ela não produziu o texto revisado e não reescreve itens. Nenhum arquivo de produção foi alterado, e não houve commit nem push. O que se examina nesta rodada segue a ficha (seção 4.3), o R1 (seção 8, itens 1 a 3) e a ficha (seção 9.3, item 6): cada AJ do R1 e da auditoria de estilo, conferido literalmente; o que a v2 mudou além dos AJ; e a pendência (d) do bloco 5, registrada aqui e deixada para a GCB decidir.

## 0. Objeto, entradas e método
| objeto | SHA-256 (em disco, 22/10/2026) |
|---|---|
| saida/gcb/DA_reforco_leva3_v2.md (objeto do R2; 30 itens) | e4c2a91191b4e5b3180317ce28653514a438896929291168c83b3a2c4a513237 (= despacho) |
| saida/gcb/DA_reforco_leva3_v1.md (objeto do R1; base do diff) | 7214e588c14f69b1acb72a8d3701efc77ab666824bfa487095c4389923fa91bb (= despacho = R1) |
| saida/gcb/QA_DA_reforco_leva3_R1_2026-10-22_gcb-cqfp.md | 28c392adeebbb33306f05c7e1a1107cafba7d565c85b9f994c58972a8cc710d4 (= despacho) |
| saida/banco/estilo_DA_reforco_leva3.md | f7d0181287455232317366ed63961e0521400b1b0f7dcfddb1ce2d0b569313e4 (= despacho) |
| normativo_cache/Lei_8078_1990_CDC_compilada_2026-10-20.txt | 575478df6643d0495446b41db6828975477d8e7f57cadaca403b3dfe07784526 (= R1) |
| normativo_cache/Lei_13869_2019_2026-10-20.txt | fb3b95c117e64fc0f26f0a915af3ae433d6ceb3aad2434fc5dcae72a64f04a33 (= R1) |
| normativo_cache/CF_1988_compilada_2026-10-20.txt | d6580cb327147e1beb69ccd09cd930613c06f39e1791b235729930a01cacb51d (= R1) |

Também foram lidos a ficha saida/gcb/DA_reforco_ficha_2026-10-20.md (seções 4, 7.4, 7.6, 8.4 e 9, com a 9.3 inteira), regras/ e CLAUDE.md. O modelo de forma é saida/gcb/QA_DA_reforco_leva2_R2_2026-10-20_gcb-cqfp.md.

Método: um script próprio (r2.py) roda com python3 -I, somente leitura, no scratchpad da sessão, fora do repositório. Ele faz o seguinte:
- (a) aplica os 5 AJ (AJ-1 do R1; AJ-L3-E1 a E4 do estilo), com o texto literal de cada parecer, por substituição exata às seções 1 e 2 da v1, e compara o resultado com as seções 1 e 2 da v2;
- (b) compara por id os 30 enunciados (seção 1) e os 30 blocos (seção 2) da v1 e da v2, campo a campo;
- (c) refaz sobre a v2 a abertura × gabarito, os fechos, os absolutos (L3-2), o contraste e o qualificador (L3-4 e L3-5), o gabarito, o [TS] e a sequência.

O diff integral v1 → v2 foi lido linha a linha.

Rede: em 22/10/2026, curl para https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/lei/l13869.htm terminou em timeout de 15 s, código 000 (bloqueado, como diz o despacho). As bases foram conferidas nas cópias de 20/10/2026 em normativo_cache/: a URL está na linha 1 de cada cópia, com "verificado em 20/10/2026". Nada foi suprido de memória.

## 1. Veredito geral
- **Leva: APROVADA.**
- Os 3 itens alterados estão APROVADOS: D3-R37, D3-R44 e D3-R50.
- Os 27 itens não alterados ficam APROVADOS, como no R1, e são idênticos aos da v1.
- **Reprovação final: 0/30 = 0,0%** (limite de 30%). No acumulado do rito (R1 + R2), também 0/30 = 0,0%. Não há GATE.
- Itens aprovados no R1 e mudados sem pedido: **nenhum**.
- Conferências pedidas pelo despacho: as (1) a (4) **CONFEREM**, e a (5) fica registrada na seção 6. **Nenhuma NÃO CONFERE.**
- Há um resíduo de harmonização além da pendência (d), sem efeito em gabarito nem em contagem (seção 6, item 3).

## 2. Conferência (1) — AJ aplicados por substituição exata
| AJ | item / campo | "substituir" na v1 | "substituir" na v2 | "por" na v2 | v1 + AJ = v2 (enunciado e bloco) | veredito |
|---|---|---|---|---|---|---|
| AJ-1 (R1) | D3-R37 / enunciado | 1 | 0 | 1 no item (l. 119); a 2ª ocorrência está só na tabela da "Resposta à R1" (l. 17) | idêntico | **APLICADO** |
| AJ-L3-E1 (estilo) | D3-R44 / enunciado | 1 | 0 | 1 no item (l. 135); 2ª na "Resposta à R1" (l. 18) | idêntico (com o E2) | **APLICADO** |
| AJ-L3-E2 (estilo) | D3-R44 / Troca | 1 | 0 | 1 no bloco (l. 513); 2ª na "Resposta à R1" (l. 19) | idêntico (com o E1) | **APLICADO** |
| AJ-L3-E3 (estilo) | D3-R50 / enunciado | 1 | 0 | 1 no item (l. 149); 2ª na "Resposta à R1" (l. 20) | idêntico (com o E4) | **APLICADO** |
| AJ-L3-E4 (estilo) | D3-R50 / Troca | 1 | 0 | 1 no bloco (l. 608); 2ª na "Resposta à R1" (l. 21) | idêntico (com o E3) | **APLICADO** |

Com os 5 AJ aplicados em memória, a v1 fica igual à v2, byte a byte, nas seções 1 e 2 (comparação por script: True/True). Efeito colateral nos 3 blocos: **nenhum**. Pela comparação campo a campo:
- D3-R37: nenhum campo da seção 2 muda; só o enunciado da seção 1 muda (de 25 para 24 palavras).
- D3-R44: só o campo Troca muda na seção 2, mais o enunciado (de 47 para 51 palavras).
- D3-R50: só o campo Troca muda na seção 2, mais o enunciado (de 33 para 37 palavras).

Ficam iguais à v1, nos três itens: gabarito, [TS], ponto, mecanismo, formato, moldura, aderência, justificativas, Base, "Difere de" e Marcas.

Os AJ-L3-E2 e E4 mudam o campo Troca, o que a ficha (7.6) não admite depois do R2 sem QA própria. Aqui eles entraram antes do R2 (ficha 9.3, item 6), e este R2 é a QA própria deles: **CONFERE**.

## 3. Conferência (2) — os 27 blocos não alterados
**CONFERE.** Na comparação por id, 27 enunciados e 27 blocos são idênticos aos da v1. Só D3-R37, D3-R44 e D3-R50 diferem, e apenas pelo texto dos AJ.

Fora dos itens, o diff v1 → v2 tem só estas mudanças, todas declaradas na Resposta à R1, R.6, item (2):
- linha 1 (nome do arquivo);
- parágrafo de abertura (l. 3) e linha de entradas (l. 5);
- nova seção "Resposta à R1" (l. 7 a 67);
- seção 4.6 (tabela L3-2, contagem L3-2 e tabela do lote D3);
- bloco 5: "Arquivo", amostra da gbq-estilo, dúvida (vi) e a nova linha de recomendações (a) a (d).

As seções 0, 3, 4.1 a 4.5, 4.7, 4.8 e 6 são idênticas às da v1.

## 4. Conferência (3) — resposta item a item da v2
**CONFERE.** As 8 partes da Resposta à R1 (R.1 a R.8) batem com o R1 e com o estilo:
- **R.1:** os números do R1 (29/1/0) e do estilo (2 CONFORMES, 2 AJUSTE) estão corretos.
- **R.2:** os 5 AJ foram acatados, sem recusa. Os textos citados conferem com os pareceres, e as contagens de palavras conferem: 25 → 24, 47 → 51 e 33 → 37.
- **R.3:** as diferenças da seção 4 conferem com o diff (ver seção 5).
- **R.4:** os 29 aprovados ficam mantidos. As observações do R1 sobre D3-R27, R36, R40 e R48 estão registradas sem alterar os itens, e eles de fato não mudaram.
- **R.5:** é o mapeamento correto da seção 7 do R1. A dúvida (vi) perdeu o objeto: o D3-R44 deixou de ter o fecho "é correto afirmar que".
- **R.6:** os itens 1 a 6 da seção 8 do R1 estão cumpridos. As recomendações (a) e (b) estão no bloco 5 como registro, não como AJ.
- **R.7:** as 8 conferências de leva estão iguais às do R1, o que foi refeito (seção 5).
- **R.8:** a errata AJ-L2-E1 continua fora da v2. A leva 2 não foi tocada.

## 5. Conferência (4) — seção 4 refeita, conferida contra o arquivo (script próprio sobre a v2)
| verificação | refeito pela QA | v2 | resultado |
|---|---|---|---|
| gabarito da leva | 16 C / 14 E (53,3%) | 16/14 (seção 0) | CONFERE |
| sequência de gabarito da leva | CEECCECCEECCCECEECECCEECCCEEEC | igual à ficha 8.4.7 e à v1 | CONFERE (nenhum gabarito mudou, então a 4.3 e o teste da regra 6 ficam inalterados) |
| [TS] | 14 (TS=sim, todos E) | 14 / 0 | CONFERE |
| moldura S | 1 C / 4 E (D3-R33 / R27, R31, R35, R44) | 1/4; o D3-R44 continua S ("sessão de comissão da Câmara dos Deputados" permanece no cenário) | CONFERE; o acumulado DA 49/25 e D3 9/11 fica inalterado |
| abertura × gabarito | "Considere que" 6 C / 6 E; declarativos 10 C / 8 E | iguais | CONFERE |
| "Nessa situação, nos termos d…" | 2 C / 1 E (D3-R27, R33, R36) | 2/1 (3 de 12) | CONFERE |
| fecho neutro "é correto afirmar que" | 0 C / 0 E | 0/0 (era 0/1 na v1) | CONFERE |
| outra "Nessa situação," | 4 C / 5 E (o D3-R44 entra aqui) | 4/5 (era 4/4); acumulado do D3 20/17; a soma 6/6 é igual ao total "Considere que" | CONFERE |
| absolutos L3-2 | E inserido: R23 "apenas", R35 "só", R38 e R43 "somente", R44 "exaustiva"; C literal: R22, R33, R45, R47; nenhum E com absoluto literal que não seja a troca | 4 C / 5 E / 0, por folha 1×1, 1×1, 3×2, 0×0; o D3-R37 saiu da tabela | CONFERE |
| L3-4 e L3-5 | 0 "mas não", ", e não", "mero", "por si só", "simples" nos enunciados | 0 | CONFERE (o "mas não se limitando a" do D3-R44 continua fora do enunciado) |
| extensão | D3-R37 24, D3-R44 51, D3-R50 37 palavras | iguais à R.2 | CONFERE (dentro da faixa de E, 19 a 62) |

## 6. Conferência (5) — pendência (d) do bloco 5 (D3-R44, campo "Ponto de julgamento"). Registro; a decisão é da GCB.
1. **Fato.** O campo "Ponto de julgamento" do D3-R44 termina em «em rol que compreende, mas não se limita a (item troca por rol exaustivo)». Ele aparece no bloco (seção 2, l. 503) e na seção 4.5 (l. 789), que reproduz o mesmo campo. O AJ-L3-E2 mudou só o campo Troca, de "rol exaustivo" para "enumeração exaustiva". A v2 declarou o resíduo no bloco 5, (d), e não o tocou. Isso está correto: tocá-lo seria mudança fora de texto exato (ficha 4.3).
2. **Leitura da gcb-cqfp.**
   - Não é defeito de item e não afeta a aprovação.
   - O defeito que o AJ-L3-E1 corrigiu estava no enunciado, que é o texto lido pelo candidato. O referente "esse rol" podia ser lido como a categoria-gênero que o caput fecha ("qualquer agente público") e abria espaço a recurso.
   - No campo de ponto, que fica no gabarito comentado e não vai ao candidato como item, "rol que compreende, mas não se limita a" descreve corretamente os incisos da Lei 13.869, art. 2º (cópia, l. 22 a 24). O parêntese "(item troca por rol exaustivo)" resume a mesma troca que o campo Troca nomeia como "enumeração exaustiva".
   - Gabarito (E), ponto (A5.2-18), mecanismo (E6) e troca não mudam, e não há afirmação sem fonte.
   - A divergência é só de rótulo. Nenhuma das hipóteses da ficha 4.1 ou 4.2 se aplica.
   - Se a GCB quiser uniformizar, a via cabível é a errata da reconciliação (ficha 7.6): o campo não é Troca, gabarito nem construção, então não exige QA própria.
   - Ressalva de forma: o trecho "(item troca por rol exaustivo)" ocorre **2 vezes** no arquivo, e o "antes" de uma errata tem de ser único. As cadeias únicas (1 ocorrência cada, conferido por grep -cF) são a linha inteira "- Ponto de julgamento: A5.2-18 — … (item troca por rol exaustivo)" e a linha da 4.5 iniciada por "| D3-R44 | 5.2 | A5.2-18 |".
   - Esta QA não redige a errata nem decide se ela é feita.
3. **Resíduos da mesma natureza, não citados na (d).** São registro para a mesma decisão da GCB, sem efeito em gabarito, contagem ou aprovação:
   - (i) bloco 5, "Pistas de forma", item (4) (l. 939): «R44 ‘exaustivo’». A seção 4.6 refeita diz "exaustiva". O rótulo do marcador ficou da v1, e só ele diverge da seção 4.
   - (ii) D3-R44, Justificativa (linha 2): «O item torna exaustivo o rol que a lei declara não exaustivo». O texto é verdadeiro e descreve a troca.
   - (iii) D3-R44, "Difere de": «o caráter não exaustivo do rol». Também verdadeiro.
   - (iv) seção 6, item 7: «rol aberto por rol exaustivo (D3-R44)». É a descrição do mecanismo.
   - (v) D3-R50, Justificativa (linha 2): «à configuração de erro judiciário». A expressão é a que o AJ-L3-E3 tirou do enunciado. Na justificativa ela segue verdadeira, como o estilo registrou ("A justificativa, linha 2, continua verdadeira sem mudança"), porque ali é explicação da troca, não afirmação julgada.

## 7. Veredito por item (os 3 alterados)
| id | folha | gab. | [TS] | enunciado da v2 (lido inteiro) | base (cópia) | veredito | nota |
|---|---|---|---|---|---|---|---|
| D3-R37 | 6.5 | E | sim | «Segundo o Código de Defesa do Consumidor, o fornecedor de serviços não será responsabilizado quando provar a culpa concorrente do consumidor ou de terceiro.» | CDC, art. 14, § 3º, caput e II (l. 114 e 116): «só não será responsabilizado quando provar: … II - a culpa exclusiva do consumidor ou de terceiro» | **APROVADO** | Resta uma única troca, exclusiva → concorrente (E1). O E vem da letra do rol fechado do § 3º (ficha, regra 8; não é "E por ausência" fora de rol fechado). A eventual redução da indenização por culpa concorrente não torna C a exclusão de responsabilidade. O defeito do R1 (excludente única que apagava o inciso I) foi eliminado. O "não" do enunciado é o da própria norma e não nega um cenário (7.4.5). Nota (p) com D3-61 mantida. |
| D3-R44 | 5.2 | E | sim | «Considere que, durante sessão de comissão da Câmara dos Deputados, seja debatido o rol de sujeitos ativos do crime de abuso de autoridade. Nessa situação, segundo a Lei nº 13.869/2019, a enumeração dos agentes públicos considerados sujeitos ativos desse crime, na qual se incluem os membros do Poder Legislativo, é exaustiva.» | Lei 13.869, art. 2º, caput e II (l. 22 e 24): «compreendendo, mas não se limitando a: … II - membros do Poder Legislativo» | **APROVADO** | O referente agora é a enumeração, que a lei declara aberta, e não a categoria-gênero. O E fica nítido pela letra do caput (E6), e o risco de "mais de uma interpretação" do estilo foi eliminado. O fecho "é correto afirmar que" saiu, e o D3 fica em 0/0. "Rol" sobrevive só no cenário, que é moldura decorativa e não decide o gabarito, porque o fecho nomeia o objeto julgado. Nada sobre imunidade, tipo penal ou norma interna da Câmara (C1 e C4). Moldura S, da cota da 5.2, mantida. A pendência (d) fica na seção 6. |
| D3-R50 | 6.2 | E | sim | «Considere que determinado condenado tenha ficado preso além do tempo fixado na sentença. Nessa situação, segundo o art. 5º, LXXV, da Constituição Federal, a indenização pelo Estado depende de que a condenação tenha decorrido de erro judiciário.» | CF, art. 5º, LXXV (l. 149): «o Estado indenizará o condenado por erro judiciário, assim como o que ficar preso além do tempo fixado na sentença» | **APROVADO** | A condição inventada agora nomeia a primeira hipótese do inciso pelos elementos dela, e o E fica nítido pela letra ("assim como": hipótese autônoma; E3). A leitura ampla de "erro judiciário", que poderia tornar o item C, foi eliminada. O fecho não nega a conclusão (7.4.5). Nada sobre atos jurisdicionais em geral (C7). A nota com o A6.2-05 da leva 4 fica mantida. |

## 8. Tabela-resumo dos 30 itens (v2)
| id | folha | ponto | gab. | [TS] | formato | moldura | aderência | R1 | R2 |
|---|---|---|---|---|---|---|---|---|---|
| D3-R22 | 6.4 | A6.4-15 | C | não | NUM | N | parcial | APROVADO | APROVADO (idêntico à v1) |
| D3-R23 | 6.4 | A6.4-09 | E | sim | SUJ | N | parcial | APROVADO | APROVADO (idêntico) |
| D3-R24 | 6.4 | A6.4-11 | E | sim | NUM | N | parcial | APROVADO | APROVADO (idêntico) |
| D3-R25 | 6.4 | A6.4-16 | C | não | SIT | N | parcial | APROVADO | APROVADO (idêntico) |
| D3-R26 | 6.5 | A6.5-01 | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R27 | 6.5 | A6.5-08 | E | sim | APL | S | direta | APROVADO | APROVADO (idêntico) |
| D3-R28 | 6.5 | A6.5-12 | C | não | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R29 | 6.5 | A6.5-07 | C | não | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R30 | 6.5 | A6.5-17 | E | sim | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R31 | 6.5 | A6.5-19 | E | sim | APL | S | parcial | APROVADO | APROVADO (idêntico) |
| D3-R32 | 6.5 | A6.5-14 | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R33 | 6.5 | A6.5-05 | C | não | APL | S | direta | APROVADO | APROVADO (idêntico) |
| D3-R34 | 6.5 | A6.5-09 | C | não | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R35 | 6.5 | A6.5-06 | E | sim | APL | S | direta | APROVADO | APROVADO (idêntico) |
| D3-R36 | 6.5 | A6.5-20 | C | não | SIT | N | parcial | APROVADO | APROVADO (idêntico) |
| D3-R37 | 6.5 | A6.5-11 | E | sim | PAR | N | parcial | AJUSTAR (AJ-1) | **APROVADO** (AJ-1 aplicado) |
| D3-R38 | 5.2 | A5.2-03 | E | sim | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R39 | 5.2 | A5.2-04 | C | não | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R40 | 5.2 | A5.2-02 | E | sim | SIT | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R41 | 5.2 | A5.2-05 | C | não | PAR | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R42 | 5.2 | A5.2-12 | C | não | SIT | N | parcial | APROVADO | APROVADO (idêntico) |
| D3-R43 | 5.2 | A5.2-06 | E | sim | DEF | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R44 | 5.2 | A5.2-18 | E | sim | APL | S | parcial | APROVADO | **APROVADO** (AJ-L3-E1 e E2 aplicados) |
| D3-R45 | 5.2 | A5.2-07 | C | não | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R46 | 5.2 | A5.2-17 | C | não | SIT | N | parcial | APROVADO | APROVADO (idêntico) |
| D3-R47 | 5.2 | A5.2-08 | C | não | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R48 | 5.2 | A5.2-13 | E | sim | SUJ | N | parcial | APROVADO | APROVADO (idêntico) |
| D3-R49 | 6.2 | A6.2-02 | E | sim | SUJ | N | direta | APROVADO | APROVADO (idêntico) |
| D3-R50 | 6.2 | A6.2-06 | E | sim | SIT | N | direta | APROVADO | **APROVADO** (AJ-L3-E3 e E4 aplicados) |
| D3-R51 | 6.2 | A6.2-04 | C | não | DEF | N | direta | APROVADO | APROVADO (idêntico) |

Percentual de reprovados: **0/30 = 0,0%**. APROVADO: 30 (100%). REPROVADO: 0.

## 9. Notas à GCB (sem decisão desta QA)
1. A leva segue para a reconciliação e o gatilho A. A errata AJ-L2-E1, CONFERIDA no R1 (seção 6), vai como item separado.
2. Pendência (d) e resíduos da seção 6: harmonização de rótulo, opcional, por errata da reconciliação (ficha 7.6), a critério da GCB.
3. Recomendações (a) D3-R27 e (b) D3-R48 do R1, e L4-1 a L4-4 do estilo: ficam para a ficha da leva 4, se a GCB aceitar.
4. Núcleo, conforme a ficha 8.2, item 9: D3-R26 e D3-R27 (6.5), D3-R38 (5.2), D3-R49 (6.2). Inalterado, pois nenhum item foi reprovado.

FIM DO PARECER QA R2 — LEVA 3 — REFORÇO DA
