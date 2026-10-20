# QA_DA_reforco_leva1_R2_2026-10-20_gcb-cqfp.md — T-116 — 2026-10-20 — gerado por gcb-cqfp

# PARECER QA R2 (ÚLTIMA RODADA) — LEVA 1 DO REFORÇO DE DA (D-REFORCO-DA) — ciclo s15c3
QA independente (gcb-cqfp, opus). Não produziu o texto revisado e não reescreve itens. O arquivo da produção não foi alterado. Sem commit nem push. Sem leitura externa (D-REFORCO-DA): bases conferidas no adendo e na cópia de saida/gcb/normativo_cache/. Escopo do R2 (R1, seção 9, item 7): cada AJ literalmente, o substituto por inteiro e só o que mudou além disso.

## 0. Objeto, entradas e método
| objeto | SHA-256 |
|---|---|
| saida/gcb/DA_reforco_leva1_v2.md (objeto do R2; 30 itens) | 2c431529a5440d4a2bf2bb617bc75d496949dff28a824e0215322d00d79a4f04 |
| saida/gcb/DA_reforco_leva1_v1.md (objeto do R1) | 047949049703a052b6233b6d5bb31b98021425a1854a768dbfd4ae1096215f01 |
| saida/gcb/QA_DA_reforco_leva1_R1_2026-10-20_gcb-cqfp.md (parecer R1) | — |
| saida/gcb/DA_reforco_ficha_2026-10-20.md | acf8b57af3f42e0bcab9a6d92f6cfa3dd70deacf3f521fc285e5b3a1b0d95133 |
| saida/gcb/D4_anexo_N_adendo_2026-10-20.md | c32f58eb78507f8c415c9b79f9cfdde0dfefdb7314ddd23045d312cb03d16fb5 |
| saida/gcb/D3_anexo_N_adendo_2026-10-20.md | c8ad5bd23bf94d6fb74b300d789fa8a21c76fc7349748ba468f68576b9f74a50 |
| saida/gcb/D4_v2_1.md / saida/gcb/D3_v2_1.md | c1a7a935…5e9d9 / 0f7a8b09…798930 |
| saida/banco/moldura_ce_itens_2026-10-20.csv | ed4b364dffbca7d9e8878591914783258fa7048c4f1837d98c3d62e34981daac |
| saida/gcb/normativo_cache/Ipea_BAPI19_Cavalcante_2018_2026-10-20.txt | 0cbba5ec37b03d59c0f99c2ddd1a1c1735c857feb62243d8054d2ead1cbe39fa |

Todas as entradas do R1 têm o mesmo SHA-256 da seção 0 do R1 (nenhuma mudou entre as rodadas).

Método (python3 -I, scratchpad da sessão, somente leitura): (a) os 7 AJ foram extraídos do texto do R1 e aplicados por substituição exata à v1 (cada trecho atual ocorre 1 vez na v1); (b) a v1 com os AJ aplicados foi comparada à v2 bloco a bloco (enunciado da seção 1 e bloco da seção 2, por id) e, fora dos itens, linha a linha (seções 0, 3, 4, 5 e 6); (c) o D4-R18 foi lido por inteiro e seu trecho procurado como subcadeia no adendo do D4 e na cópia do cache (espaços normalizados), com contexto da lista lido no cache (linhas 125 a 160); (d) contagens C/E, formatos, aderência, moldura, [TS] e teste de sequência refeitos do zero sobre os campos da v2; sequências acumuladas reconferidas com os prefixos canônicos do R1.

## 1. Veredito geral
- **APROVADO COM RESSALVAS.**
- Itens alterados na v2 (5 AJ de item + substituto): 6 de 6 APROVADOS. AJ de arquivo (AJ-1, AJ-7): aplicados.
- **Taxa de reprovação final: 0/30 = 0%** (v2). Acumulada no rito (R1 + R2): 1 reprovado (D4-R12, substituído) em 31 itens avaliados = 3,2%. Sem GATE.
- Itens APROVADOS no R1 mudados sem pedido: **nenhum** (24 de 24 idênticos, enunciado e bloco).
- Ressalvas (não reprovam; não pedem nova rodada): (R-1) a sequência de [TS] da 8.4 acumulada continua reprovando no teste de período 3 (C4 do R1), aguardando a decisão da GCB (Pendências, item 1); (R-2) registro de página no D4-R18 (seção 3).

## 2. Ajustes do R1 — conferência literal
| AJ | onde | trecho antigo na v2 | trecho novo na v2 | bloco do item = v1 + AJ | veredito |
|---|---|---|---|---|---|
| AJ-1 | cabeçalho (linha 3) | 0 | presente (linha 3; 2ª ocorrência só na tabela de resposta, linha 11) | — | APLICADO (12 levas: ficha, título e seção 2) |
| AJ-2 | D4-R02, Difere de | 0 | 1 | idêntico | APROVADO |
| AJ-3 | D4-R03, Difere de | 0 | 1 | idêntico | APROVADO |
| AJ-4 | D4-R07, Difere de | 0 | 1 | idêntico | APROVADO |
| AJ-5 | D3-R01, Aderência | 0 | 1 | idêntico | APROVADO |
| AJ-6 | D3-R07, Mecanismo | 0 | 1 no bloco do D3-R07 (a 2ª ocorrência do texto é o campo pré-existente do D3-R02, inalterado) | idêntico | APROVADO |
| AJ-7 | seção 4.3, nota | 0 | 1 (linha 681) | — | APLICADO |

Nenhum dos 5 itens com AJ mudou fora do campo do AJ (comparação bloco a bloco após aplicação simulada: diferença zero).

## 3. Substituto D4-R18 — conferência completa
| verificação | resultado |
|---|---|
| Enunciado | “Considere que um analista descreva as tendências da gestão pública no pós-nova gestão pública (pós-NPM). Nessa situação, ele estará correto ao incluir entre elas o fortalecimento das capacidades de coordenação e monitoramento das políticas estratégicas, especialmente pelo núcleo de governo.” |
| Base literal | trecho de R54 (alínea d), 19 palavras: subcadeia exata do adendo do D4 (linha de R54) e da cópia do cache do Ipea (linhas 150–151). URL e data (20/10/2026) idênticas às do adendo. Contexto no cache: a lista é introduzida por “Assim, as tendências do pós-NGP são:” e vai de a) a i) — sustenta “tendências … no pós-NPM” e “incluir entre elas”. |
| Gabarito | C confere: a proposição reproduz a descrição da alínea d sem troca; “incluir entre elas” não afirma exclusividade (lista de nove alíneas, nota do adendo a R55). Não é C por moldura nem C-isca. |
| Ponto único | sim: uma alínea (d), um julgamento. |
| Pertinência à 8.1 | direta: A8.1-27 está no adendo como ponto da 8.1 (“fundamentos, uma alínea por item”), mesmo enquadramento já aprovado no D4-R03; “pós-NPM” (B6) sem equiparar pós-NPM e NPG; sem autor nomeado (ficha 0.2, item 4). |
| Não gêmeo | ok: alínea d não é julgada por nenhum canônico (D4-01 a D4-06; D4-06 = integração/colaboração/decisão inclusiva, R4) nem por item da leva (D4-R03 = alínea i; D4-R16 = liderança, R64); D4-08 (8.2) = alíneas a e b; D4-27 (8.4) = “coordenação de processos” do Decreto 9.203, art. 4º, IV, outro dispositivo. Escolha da d entre d, e, g e h motivada no bloco à GCB (vizinhos de e, g e h): ACEITA. |
| Campos da regra 14 | completos: itemEdital P1-DA-8.1; ponto; Formato SIT; Moldura N, fecho acerto; Aderência direta; Gabarito C; justificativa em duas linhas; Tipo de base; Base; Mecanismo C2; Difere de (D4-R03, D4-08); Marcas TS=não, REVERIFICAR=não, VOLÁTIL=não, QA PENDENTE=sim. Linha na 3.2 e na 4.5 presentes. |
| Posição | entre D4-R11 e D4-R13 (seções 1, 2, 3.2 e 4.5), como pedido no R1, seção 4. |
| Efeito nas faixas | D4-R12 (C, sem [TS]) → D4-R18 (C, sem [TS]): sequências de gabarito e de [TS] idênticas às da v1. 8.1: 10/10, formatos 6/0/5/0/4/5 (DEF 6 = teto; nenhum DEF novo); moldura 5; diretos 20. |
| Registro (R-2) | a coluna Base diz “p. 19-20” (faixa herdada da linha de R54 do adendo, que cobre c, d e e); no cache, a alínea d está inteira na p. 20 (cabeçalho de página na linha 145–146). Não altera o item; corrigir na reconciliação ou na consolidação (T-123), se a GCB quiser. |
| **Veredito** | **APROVADO** |

Observação (não reprova; à gbq-estilo): D4-R18 (C) repete a moldura de abertura e de fecho do D4-R03 (E) e do D4-08 (C, folha 8.2), como o R1 prescreveu; as alíneas são distintas e os gabaritos dos dois itens da 8.1 são opostos, sem pista. A produção registrou (Pendências, registro ii).

## 4. Diff v1 → v2 fora dos itens (todas as mudanças são derivadas e pedidas)
- Seção “Resposta à R1” (nova; regra do R1, seção 9, item 7): item a item, sem item não acatado; o que ficou “não decidido” é matéria da GCB.
- Seção 0 e 4.1/4.7: 8.1 leva 4/0/4/0/2/4 e folha 6/0/5/0/4/5; 6.3 diretos 5 / parciais 8 (folha 12/8); leva 8/2/6/0/3/11 e 22/8 — conferidos por script.
- 3.2 e 4.5: linha do D4-R12 trocada pela do D4-R18; R-ids da leva com R54 no lugar de R42.
- 4.4: K2 7/6 (53,8%), K3 5/4 (55,6%), K4 23/17 (57,5%) — conferidos; DA 46/18 e D3 7/4 inalterados (D4-R18 sem moldura).
- 4.6: “Considere que” 17 (D4 11; D3 6); “pós-NPM” 5 — conferidos.
- Seção 5: bloco à GCB atualizado (deslocamento da 8.4 na leva 2 para D4-R19 a D4-R28; nota (b) do D4-R12 retirada; notas (b) e (c) dos AJ-4 e AJ-2; parciais da 6.3 com o D3-R01 na nota (e)). Seção 6 (nova): Pendências para a GCB.
- D4-R12: ausente das seções 1, 2, 3.2 e 4.5; o id só aparece em menções narrativas à reprovação; não reutilizado.

## 5. Contagens e faixas (refeitas do zero sobre a v2)
| conferência | resultado |
|---|---|
| C/E leva | 15 C / 15 E (50%) — faixa 12–18: CONFERE |
| C/E por folha | 8.1 leva 7/7, folha 10/10; 6.3 leva 8/5, folha 10/10; 8.4 leva 0/3, acumulada 4/6 (fecha na leva 2) — CONFERE |
| Formatos ≤ 30% por folha | 8.1 DEF 6/20 (30%); 6.3 DEF 6/20 (30%); 8.4 APL 4 (20% de 20; 5 ao fim da leva 2) — CONFERE (margem zero de DEF em 8.1 e 6.3) |
| Moldura | leva 2 C / 9 E; DA 46/18 (71,9%, como a ficha 3.6); D3 7/4; K1 13/6; K2 7/6; K3 5/4; K4 23/17 (conjuntos K2–K4 em 40–60%); ≤ 6 por folha (8.1 5; 6.3 5; 8.4 4) — CONFERE |
| Aderência | 8.1 20 diretos; 6.3 12 diretos / 8 parciais (piso 10); 8.4 10 — CONFERE |
| [TS] | 16 (15 E, 1 C-isca no D3-R10; 1 por folha no máximo) — CONFERE |
| VOLÁTIL / REVERIFICAR | 0 / 0 — CONFERE |
| Teste de sequência | gabarito: todas as linhas passam; [TS]: folhas, leva e acumuladas de 8.1 e 6.3 passam; **8.4 acumulada nTTnTTnTTT reprova (p3 9/8)** — inalterado desde o R1 (ressalva R-1) |
| Pontos | 30 pontos distintos (A8.1-27 em alíneas i e d); nenhum gêmeo de canônico; nenhum item da 8.4 usa o Decreto 9.203, art. 2º, II, nem o art. 4º, IV — CONFERE |

## 6. Pendências para a GCB (comentário só no que toca a aprovação)
1. **[TS] da 8.4 acumulada (C4)** — afeta a aprovação apenas como ressalva: é a única linha reprovada do teste de sequência, e não tem conserto dentro desta leva sem redistribuir a 8.4 entre as levas 1 e 2. A leva fica aprovada com essa ressalva; a decisão (aceitar e registrar na reconciliação, ou redistribuir) deve constar da reconciliação antes do gatilho A da leva. Se a GCB optar pela redistribuição, o item da 8.4 que entrar ou sair desta leva volta ao QA.
2. Núcleo da 6.3 — não afeta a aprovação.
3. Pista “Considere que” no D4 — não afeta a aprovação (K4 23/17 na faixa).

## 7. Tabela de vereditos (itens alterados na v2)
| id | alteração | veredito R2 |
|---|---|---|
| D4-R02 | AJ-2 (Difere de) | APROVADO |
| D4-R03 | AJ-3 (Difere de) | APROVADO |
| D4-R07 | AJ-4 (Difere de) | APROVADO |
| D3-R01 | AJ-5 (Aderência: parcial) | APROVADO |
| D3-R07 | AJ-6 (Mecanismo E3) | APROVADO |
| D4-R18 | substituto do D4-R12 (A8.1-27, alínea d; C; SIT) | APROVADO (registro R-2) |
| D4-R12 | retirado (reprovado no R1) | — |
| demais 24 | sem alteração | APROVADO (mantido do R1) |

Resultado da leva para a reconciliação: 30 itens aprovados (14 da 8.1, 13 da 6.3, 3 da 8.4). Próximo passo do rito (ficha, regra 15): auditoria de estilo de 10% (gbq-estilo) e reconciliação da GCB.

FIM DO PARECER QA R2 — LEVA 01 — REFORÇO DA
