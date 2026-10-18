# T97_reconciliacao_2026-10-18.md — T-97 — 2026-10-18 — gerado por gce-gerencia

Objeto: reconciliação da T-97 (REFORÇO onda 3, P2 folhas 2.1 a 2.8; D-REFORCO-2), ciclo 2026-10-18 s12c4. 112 itens produzidos (L2-R19 a L2-R130), em 4 partes.
Base lida: TAREFAS.md (T-97); DECISOES.md (D-REFORCO-1, D-REFORCO-2, D-FONTE-DATA-ANTERIOR, D-T89-R1-ACEITE, D-T90-R2-ACEITE, D-T96-ONDA2-ACEITE, D-T103-SALDO-ACEITE, D-ONDA3-FILA, D-RITMO-MAX, D-ADERENCIA, D-ABSORCAO-V110, D-L2-T84-ERRATA); critérios desta Gerência em T90_, T96_ e T103_reconciliacao_2026-10-18.md; regras/pacote_contrato.md (aderência); finais v2: saida/gce/L2_reforco_onda3_A_v2.md (SHA-256 e6aef0a5…eeeeb01f, 58268 bytes), B_v2 (f7b67c43…a6dbb9), C_v2 (ff54e402…05d997), D_v2 (31a3c4c2…d01f4); pareceres QA_T97A/B/C/D_R1 e R2_2026-10-18_gce-cqfp.md, QA_T97A/B/D_normativo_2026-10-18_qa-normativo.md (com o adendo do L2-R128); saida/pacote/pacote.json v1.9 (334 itens; partida e gêmeos); finais das ondas 1 e 2 (gêmeos); GCE_Lote2_v2_CPP.md (l. 500–510) e GCE_Lote2_padroes_GCE.md (l. 130–142).
Conferência própria (python -I, somente leitura; scripts no scratchpad da sessão): mapa, Parte 2 e Parte 3 dos quatro v2 (28 ids em cada; Parte 2 sem marcas; FIM DO LOTE); contagens por folha contra o pacote.json v1.9 (6 existentes por folha, ids e folhas conferidos); varredura de trechos-base literais compartilhados entre os 112 itens e os das ondas 1 e 2.
A GCE não escreve em PARA_PRESIDENCIA.md nem em TAREFAS.md: os textos das seções 9 e 10 são para o orquestrador colar. Nenhum gabarito muda. O único texto de enunciado que muda é o do L2-R128, com a redação exata ditada pela QA (seção 5.4).

## 1. D1: L2-R67 RETIRADO; reposição por item novo em tarefa de saldo (L2-R131)
- O R67 da v2 foi reprovado na R2, a última rodada: o ponto é metafato (o que um guia do fornecedor declara cobrir), não conceito de formatação; o gabarito depende do escopo declarado na página; o E induz conclusão falsa sobre o produto (QA_T97B_R2, seção 5). É o mesmo vício do L1-R43 (T96_reconciliacao, seção 1). Ajuste não cabe. O item sai em definitivo, e o id L2-R67 não é reutilizado (já designou dois textos: art. 66 na v1, legendagem na v2).
- Deixar a 2.4 em 19 descumpriria a meta do Fundador ("no mínimo 20"; D-REFORCO-2), o que esta Gerência não pode decidir. Decisão: repor, como na T-103.
- A reposição é PRODUÇÃO NOVA (id L2-R131), com R1 própria da gce-cqfp e no máximo 2 rodadas; não é 3ª rodada da parte B. Requisitos:
  - folha P2-2.4; gabarito E com [TS] de troca única (devolve a parte B a 16 [TS] e a onda a 70);
  - aderência DIRETA ao texto da 2.4 (identificação de oradores, marcação de pausa, ruído ou evento não falado na transcrição), sem regra de condução da sessão (QA_T97B_R1, seção 2) e sem metafato de escopo de página;
  - formato diferente de SH (5/19) e de AP (4/19); de preferência NP ou PC; D só se nenhum outro couber (legado diluído);
  - ponto distinto dos 19 da folha e sem gêmeo no pacote inteiro (pacote v1.9, ondas 1 a 3; em especial 1.4, diarização, e L2-Q13 a Q16, R07, R08, R62, R68, R70, R72); vizinhança declarada;
  - base oficial aberta na data, com trecho literal (D-FONTE-DATA-ANTERIOR só nas condições dela);
  - não VOLÁTIL (a 2.4 iria a 4/20, no teto; a margem fica preservada).
- Cabe agora: é saldo da onda 3, não lote novo. Corre logo depois desta reconciliação, antes da produção da gcb-cpp na T-74 e antes da T-98 (D-RITMO-MAX; D-ONDA3-FILA, 3: leitura conservadora, nenhuma QA aberta na fábrica no início de produção nova).
- O gatilho A dos 111 não espera o saldo (precedentes T-96/T-103 e D-T92-R4-PARCIAL). O L2-R131 entra na mesma consolidação v1.10 se for aceito antes de a T-104 gerar o pacote; senão, na v1.11.
- Reprovado nas 2 rodadas, o caso volta a esta Gerência, e uma 2.4 com 19 vai à Presidência como gatilho.

## 2. D1: retirada de PENDENTE NORMATIVO (33 itens conferidos; nenhum pendente)
- Parte A: R19, R20, R21, R22, R28, R29, R31, R32, R38, R39, R41, R42, R45, R46 — 14/14 CONFERE (QA_T97A_normativo). A marca sai do mapa e do (d-G) no A_v3 (seção 5.1). O R20 mudou de texto na v2, mas o qa-normativo conferiu também o texto do ajuste.
- Parte B: R47 a R55, R63, R64, R65, R71 — 15 itens com base no RICD, CONFERE (QA_T97B_normativo, 19/19, que cobriu também os 6 ids da v1 depois substituídos — R62, R67, R70, R72, R73 e R74 —, registro superado quanto a esses ids). O B_v2 já não carrega a marca nos itens. R48 e R64 mudaram de texto depois do registro, sem troca de dispositivo nem de ponto de troca, e a QA R2 reabriu o Legin: o registro vale (condição do próprio qa-normativo).
- Parte D: R127, R129, R130 — CONFERE (QA_T97D_normativo); R128 (v2, art. 126, caput) — CONFERE no adendo. O ajuste "o Plenário da Câmara" (seção 5.4) não muda o dispositivo nem a troca (Comissão → Plenário): o registro do adendo vale. A marca sai no D_v3.
- Parte C: nenhuma norma citada.
- QA PENDENTE: cai com esta reconciliação nos 111 itens (precedente T-89, seção 5). O "QA PENDENTE" escrito nos v2/v3 é histórico.

## 3. D1: aderência (D-ADERENCIA) — folhas, meta de 20 e piso de diretas
3.1 Marcas fixadas (mapa e (d-G) dos v3 prevalecem): 43 PARCIAIS entre os 111 (A 16; B 19, com R73 e R74 passados a PARCIAL pelo texto exato da QA_T97B_R2, seção 5; C 7; D 1, R130). R22: motivo lido "contexto institucional" (QA_T97A_R2, ressalva 3). Os PARCIAIS vão só a simulado diagnóstico. O contrato admite AUTORAL "parcial" (precedente v1.9: L2-R02, L2-R14, L2-R15 exportados com "aderencia": "parcial").

| folha | diretas / itens da folha | PARCIAIS (canônicos + novos) |
|---|---|---|
| P2-2.1 | 10/20 | R02 + R19, R21, R22, R25, R27, R28, R29, R31, R32 |
| P2-2.2 | 13/20 | R35, R38, R39, R41, R42, R45, R46 |
| P2-2.3 | 10/20 | R47, R50, R51, R52, R53, R54, R55, R58, R59, R60 |
| P2-2.4 | 10/19 (11/20 com o saldo direto) | R61, R63, R64, R65, R66, R69, R71, R73, R74 |
| P2-2.5 | 17/20 | R79, R84, R85 |
| P2-2.6 | 16/20 | R91, R94, R101, R102 |
| P2-2.7 | 18/20 | R14, R15 (legado) |
| P2-2.8 | 19/20 | R130 |
| total 2.x | 113/159 (114/160) | 46 (3 legados + 43 novos) |

3.2 Meta de 20: pelo precedente desta Gerência (T90_reconciliacao, seção 2: os PARCIAIS "contam para a meta de 6 da folha, como na T-91"), aceito pela Presidência (D-T90-R2-ACEITE), a GCE conta os PARCIAIS na meta. A escala agora é outra (metade da 2.1 e da 2.3; 46 PARCIAIS em 160), e a meta é do Fundador: a leitura vai à Presidência como gatilho D (seção 10.2). Enquanto não houver resposta, vale a leitura do precedente e nada se repõe.
3.3 Piso de diretas (D1, critério desta Gerência para as ondas 3 e 4): nenhuma folha fica com menos de 10 itens diretos. Cumprido em todas (mínimo 10/20 na 2.1 e na 2.3; 10/19 na 2.4). Por isso não se troca mais nenhum item institucional da 2.1 (a QA deixou a decisão à Gerência; não há rodada para isso, e a troca seria produção nova sem ganho de regra).
3.4 Instrução para a onda 4 (T-98): item novo de folha com menos de 12 diretas é de aderência direta; norma de estrutura ou competência de órgão (Ato 251, RICD) entra só quando o ponto é o próprio registro, a revisão ou a publicação do texto.
3.5 Registro para a GBQ (D1 dela, campo "nucleo"): dentro da mesma canonização, recomenda-se preferir itens diretos para os 10 primeiros de cada folha.

## 4. D1: VOLÁTIL — sub-regra de cláusula contratual (SLA) e casos de rótulo
4.1 Sub-regra (aplicação do critério da D-T96-ONDA2-ACEITE, II; vai à ratificação como D2 de rótulo no gatilho A):
- cláusula de contrato ou SLA de fornecedor é NÃO VOLÁTIL quando o ponto é conceito do instrumento (o que o SLA mede, a natureza do remédio, a exclusão por uso fora da documentação, a fórmula do percentual), sem objetivo numérico, faixa de crédito, prazo, preço ou procedimento particular;
- é VOLÁTIL quando o gabarito depende da redação particular da cláusula (objetivo de disponibilidade, faixas de crédito, prazo ou forma de pedido, método específico de medição);
- todos ficam com conferência de base em 4–8/1/2027 (a página do SLA tem versões publicadas, "Last modified January 9, 2020").
- Aplicação: R106, R107, R109 e R110 NÃO VOLÁTEIS. Os R108 e R111 da v1 (que seriam VOLÁTEIS) já saíram por escopo. A 2.7 fica com 0/20; mesmo com leitura contrária (4/20) ficaria no teto.
4.2 Casos de rótulo (D1):
- R125 VOLÁTIL baixo, hipótese (c): "local" na hipótese (c) abrange a região do recurso, e não só o idioma. Com ele, a 2.8 fica com 4/20 (R18, R120, R121, R125), no teto e sem margem.
- R118 e R119 NÃO VOLÁTEIS (registro expresso pedido pela QA): o ponto é o mecanismo da classe, e o próprio R118 ressalva que a disponibilidade varia por modelo e idioma, sem afirmar disponibilidade.
- R85 VOLÁTIL baixo, hipótese (c) (opção de módulo periférico): a 2.5 fica com 4/20, no teto e sem margem.
- R96 NÃO VOLÁTIL (procedimento documentado do editor, sem condição; a QA admitiu os dois rótulos). A marcação conservadora não é adotada, para não levar a 2.6 ao teto sem necessidade.
- R70 NÃO VOLÁTIL, com nota para a T-11 (página da API V1, exemplos speech_v1p1beta1: conferir se o comportamento continua documentado).
- R72 NÃO VOLÁTIL: a falante por frase está documentada fora do exemplo, e o trecho da tabela de opções entra na base (B_v3, seção 5.2). Assim o item sai da hipótese (d).
- R62 NÃO VOLÁTIL: o item não afirma o padrão (suppress_tokens) e diz "podem ser suprimidos". O SHA-256 do tokenizer.py entra na base (B_v3) e na T-11.
- Mesmo trecho, mesmo rótulo (conferido): R24 e R37 (A2I, aviso de fechamento a novos clientes) são VOLÁTEIS; R25, R61 e R66 ("Como pesquisar"), também VOLÁTEIS, como L2-R07; R56 e R60 (evaluate-data, faixa e escala) são VOLÁTEIS, e R114 (mesma página, outra frase, boa prática) não é.
4.3 Resultado: 18 VOLÁTEIS novos, nenhum de risco alto (R56 médio; R77, R81, R82, R94 e R100 baixo/médio; os demais baixo). Por folha, o máximo é 4/20 = 20% (2.5 e 2.8).

## 5. D1: correções de registro sem R3 e versões finais (v3 de transcrição nas quatro partes)
- Não há R3: nenhum gabarito ou [TS] muda. O único enunciado que muda é o do R128, com o texto exato da QA, e a R2 o deixou para a reconciliação. O resto é retirada de item reprovado, marca, rótulo, contagem e base.
- Precedentes: T-90 (v3), T-91 e T-96 (A_v3, D_v3). Diferença em relação à T-96: aqui também a parte C tem v3, porque a imprecisão da base do R85 ("assinatura") e o formato do R88 estão no (d-G), e a base do (d-G) não deve levar defeito à consolidação.
- Os quatro v3 = v2 com SÓ as operações do Apêndice (por linha da v2: troca de substring exata, linha substituída inteira ou linha apagada), mais a linha 1 nova, uma linha em branco e a linha "Versão v3" inseridas depois dela. A gce-cpp transcreve, sem nenhuma outra mudança. O SHA-256 esperado de cada v3 (aplicação literal, LF, sem quebra final acrescentada) é este:

| v3 | linhas trocadas (com a 1) | apagadas | SHA-256 esperado | bytes |
|---|---|---|---|---|
| saida/gce/L2_reforco_onda3_A_v3.md | 31 | 0 | b6911efb412198ff7685a1dfd7d7451c9f55c33152dbd9d42cf6b614019d7b9c | 58150 |
| saida/gce/L2_reforco_onda3_B_v3.md | 30 | 9 | f3b3320408e36265638a0f742b4df5a10121520e2631ebc16994df83069510f1 | 73648 |
| saida/gce/L2_reforco_onda3_C_v3.md | 8 | 0 | 4bbde472b049203c784f2e1840119ab13aad2a17c34accc35465661228c4ff3d | 74421 |
| saida/gce/L2_reforco_onda3_D_v3.md | 6 | 0 | 892526fcb3fd62ba266976e2f223fd49fb392e766ac3eb26fade700af646d293 | 79332 |

5.1 A: sai PENDENTE NORMATIVO dos 14 itens (mapa e (d-G), contagens); R22 com motivo "contexto institucional". A legenda da Parte 3 (definição da marca) fica, porque é legenda.
5.2 B: sai L2-R67 (mapa, folha, vizinhança, Parte 2 e Parte 3); R73 e R74 PARCIAIS com o texto exato da R2; base do R62 com o SHA-256 do tokenizer.py (3b48e361…ae30b85; 12.338 bytes); base do R72 com o trecho da tabela de opções; contagens e tetos refeitos (27 itens; 2.4 com 19).
5.3 C: R88 com formato SH (mapa, (d-G) e contagens; 2.5 com SH 6/20 = 30%, no teto: a folha não admite mais SH); base do R85: o parâmetro é do construtor de BasicTextNormalizer; lista de janeiro: a reverificação se faz pelo texto e pelo SHA-256, e a execução é só corroboração. Registro sem efeito no arquivo: as regex de colchetes e parênteses do basic.py estão nas l. 69–70 (correção da R2 ao parecer R1; o C_v2 não cita linha).
5.4 D: R128 com "o Plenário da Câmara" (Parte 2, mapa, troca sutil) e CONFERE no lugar de PENDENTE NORMATIVO; R108 com a data exibida da página ("Last updated on 2026-06-02"), na base e na proveniência.
- Valem só nesta reconciliação, que prevalece sobre os registros da Parte 1 na consolidação (precedente T-89, seção 4): o bloco de resposta ao parecer e as dúvidas dos quatro v2 (histórico); em D, a seção 1.3 (registro do R67 da v1, art. 66) e o registro 6 da seção 1.4 (R128 "PENDENTE NORMATIVO"); em C, a remissão de linhas do basic.py.
- Conferência dos v3: pela gce-gerencia ou pelo orquestrador, por script (python -I) que aplica o Apêndice à v2 e compara com o v3 gravado. Critério: arquivo idêntico (SHA-256 da tabela acima). Se idêntico, valem a seção 9 (CONCLUÍDA, depois do passo da seção 8) e o gatilho A. Se divergente, a gce-cpp refaz a transcrição.

## 6. D1: duplicatas e gêmeos (os 112 pontos, conferidos pela Gerência)
- Método: leitura dos 112 pontos de julgamento (mapa) contra os 6 canônicos de cada folha, contra as outras três partes, contra os finais das ondas 1 e 2 e contra o pacote v1.9. Depois, varredura por script dos trechos-base literais (≥ 45 caracteres) compartilhados entre itens. Resultado: nenhum trecho-base partilhado entre dois itens da onda 3 nem com as ondas 1 e 2, salvo títulos de página e o aviso de fechamento do A2I (R24 × R37, que têm frases-base distintas).
- Dentro de cada folha: nenhuma duplicata. As vizinhanças de mesma folha declaradas pela produção e pela QA estão aceitas: R19 × R28 (art. 98, § 1º, 1ª e 2ª partes); R53 × R65 (art. 75, I e II); R61 × R66; R68 × R74; R123 × R124; R117 × L2-Q28; R127 × R49 (questão de ordem: conceito × consequência).
- Entre folhas e com o pacote: NENHUM GÊMEO (o mesmo ponto em outra folha). A instrução da T96_reconciliacao, seção 4 (ponto contra o pacote inteiro), foi cumprida pelas quatro produtoras e conferida pela QA em cada parte.
- Proximidades entre folhas, sem gêmeo, registradas para a GBQ (D2 de montagem dela; os pares não devem figurar no mesmo simulado ou caderno):

| par | folhas | razão |
|---|---|---|
| R23 × L2-Q03 | 2.1 × 2.1 (canônico) | imprecisão esperada × revisão não dispensada |
| R40 × R33 | 2.2 | mesmo item Human-in-the-loop, frases distintas |
| R55 × R64 | 2.3 × 2.4 | publicação de documentos na ata (Presidente × Mesa) |
| R105 × L2-Q06 | 2.7 × 2.2 | confiança × acerto |
| R108 × R115 | 2.7 | inspeção só com áudio |
| R111 × R43 | 2.7 × 2.2 | amostra de avaliação × conjunto de teste |
| R24 × R37 | 2.1 × 2.2 | mesma página do A2I |
| R27 × L1-R37 | 2.1 × 1.2 | model card do Whisper, "Evaluated Use" (alto risco × avaliação robusta) |
| R122 × L1-R94 | 2.8 × 1.6 | lista de frases e custom speech (ordem de escolha × tempo de execução/treino) |
| R121 × L1-R120 | 2.8 × 1.8 | mesma página da phrase list (lote × tempo de execução) |
| R62 × R84 | 2.4 × 2.5 | marcas não faladas: supressão na geração × remoção na comparação |

## 7. Contagens finais (111 itens aceitáveis; L2-R67 fora)

| folha | partida v1.9 | novos | nova | C/E novos | C/E folha | [TS] novos | VOLÁTIL folha | formatos (folha) | maior | diretas |
|---|---|---|---|---|---|---|---|---|---|---|
| P2-2.1 | 6 | R19–R32 (14) | 20 | 7/7 | 11/9 | 8 | 2/20 (R24, R25) | SH5 TS5 D4 PC4 AP2 NP0 | 25% | 10/20 |
| P2-2.2 | 6 | R33–R46 (14) | 20 | 7/7 | 9/11 | 10 | 1/20 (R37) | SH5 TS4 PC4 AP4 D2 NP1 | 25% | 13/20 |
| P2-2.3 | 6 | R47–R60 (14) | 20 | 7/7 | 10/10 | 9 | 3/20 (R56, R57, R60) | SH5 TS4 PC3 AP3 D2 NP3 | 25% | 10/20 |
| P2-2.4 | 6 | R61–R74 sem R67 (13) | 19 (+1 saldo, R131) | 7/6 | 10/9 | 6 | 3/19 (R07, R61, R66) | SH5 TS4 AP4 PC3 D2 NP1 | 26,3% | 10/19 |
| P2-2.5 | 6 | R75–R88 (14) | 20 | 7/7 | 10/10 | 9 | 4/20 (R77, R81, R82, R85) | SH6 AP5 PC4 TS3 D2 NP0 | 30% (no teto) | 17/20 |
| P2-2.6 | 6 | R89–R102 (14) | 20 | 7/7 | 11/9 | 9 | 3/20 (R94, R99, R100) | PC4 SH4 AP4 TS4 D2 NP2 | 20% | 16/20 |
| P2-2.7 | 6 | R103–R116 (14) | 20 | 7/7 | 9/11 | 9 | 0/20 | SH5 TS4 AP4 PC3 D2 NP2 | 25% | 18/20 |
| P2-2.8 | 6 | R117–R130 (14) | 20 | 7/7 | 9/11 | 9 | 4/20 (R18, R120, R121, R125) | TS5 D4 SH4 PC4 AP2 NP1 | 25% | 19/20 |
| total | 48 | 111 | 159 (160 com o saldo) | 56 C / 55 E | — | 69 | 18 novos, 0 alto | — | ≤ 30% | 113/159 |

- Regra 5: 56 C / 55 E = 50,5% de C (faixa de 40% a 60%). Com o saldo (E), 56/112 = 50,0%. Por parte: A 14/14, B 14/13, C 14/14, D 14/14.
- [TS]: 69 de 111 (62,2%). A meta (metade da onda mais 2 = 58) está cumprida, com folga de 11. Há 15 C espelho (O-6) e 1 E sem [TS] (R114, cujo E depende da base depois do ajuste da R1). Com o saldo, 70/112.
- Regra 4 (≤ 20% por folha): máximo de 4/20 na 2.5 e na 2.8, ambas no teto; nenhum VOLÁTIL novo é de risco alto.
- Regra 3 (≤ 30% por formato): o máximo é 30% (SH na 2.5, sem folga). Na contagem, TSj (notação da parte D) = TS.
- Aderência: 43 PARCIAIS novos (38,7%), seção 3.
- QA:
  - R1 por parte: A 3/28 (10,7%), B 6/28 (21,4%), C 2/28 (7,1%), D 3/28 (10,7%); na onda, 14/112 = 12,5%;
  - R2: A 0, B 1 (R67; 3,6%), C 0, D 0; na onda, 1/112 = 0,9%;
  - gate de 30% não acionado.
- Normativo: 33 itens CONFEREM, nenhum DIVERGE e nenhum fica pendente (seção 2).
- Pacote: v1.9 (334) + 112 (onda 2, D-T96-ONDA2-ACEITE e D-T103-SALDO-ACEITE) + 111 = 557 na v1.10 (558 com o L2-R131), além do escopo da D-ABSORCAO-V110.
- Cobertura registrada (sem efeito no aceite): a "revisão em dupla" da 2.7 fica rasa (Q24; indiretamente R103 e R108), por falta de base literal oficial aberta na data, e a recusa da produtora foi aceita pela QA. Fica como lacuna de profundidade para a onda de complemento, com base da própria Câmara ou norma técnica oficial, se houver.

## 8. D1: auditoria de estilo da onda 3 (D-REFORCO-2, regra 6): roda ANTES do gatilho A
- Auditor: gbq-estilo.
- Objeto: os quatro v3 conferidos.
- Amostra: 10% dos 111, isto é, 12 itens sorteados com semente registrada, com pelo menos 1 por folha. Mais o L1-R131 (saldo da onda 2), como item fixo, fora do sorteio e sem contar nele, com registro "L1-R131 — saldo da onda 2" (D-T103-SALDO-ACEITE; não condicionante para o L1-R131).
- Conferências:
  - a faixa de C da onda (50,5%);
  - os registros de estilo das QAs: concessiva também em E não cumprida na parte A (rec. 2 do estilo_onda_2); molduras formulares "o revisor deve considerar" (R50, R54, R55, R63, R68) e "Uma equipe… Nessa situação, segundo a documentação" (R56, R59, R70, R72, R73); C de baixa discriminação (R54, R66, R72, R73, R74, R88, R90, R98); R24 (tensão "revisar × transcrever do zero"); R40 ("Uma equipe da Casa");
  - a extensão C × E por parte.
- Saída: saida/banco/estilo_onda_3.md.
- Devolução à gce-gerencia, que fecha a T-97. Um defeito apontado volta como errata textual (D1), sem mudança de gabarito. Uma reprovação acima de 30% é GATE.
- O L2-R131 (saldo) não entra nesta amostra: fica como item fixo na amostra da onda 4 (T-98), não condicionante, como foi feito com o L1-R131.

## 9. Estado da T-97 e tarefas novas (textos para TAREFAS.md)
Estado, até os v3 conferidos e o estilo_onda_3.md sem GATE:
EM CURSO (ciclo 2026-10-18 s12c4; QA R1 12,5% e R2 0,9% na onda; normativo 33 CONFERE; reconciliada em saida/gce/T97_reconciliacao_2026-10-18.md: L2-R67 retirado, com saldo em tarefa própria (L2-R131); A, B, C e D com v3 de transcrição fixado na seção 5 e no Apêndice; aguarda o diff dos v3 e a auditoria do gbq-estilo, saida/banco/estilo_onda_3.md)

Estado, depois dos dois passos:
CONCLUÍDA (18/10/2026, s12c4): 111 dos 112 itens L2-R19 a L2-R130 (sem L2-R67, retirado; id não reutilizado); 56 C / 55 E; [TS] 69; 18 VOLÁTEIS novos, nenhum de risco alto; 43 com aderência PARCIAL (só simulado diagnóstico); folhas 2.1 a 2.3 e 2.5 a 2.8 com 20 itens e 2.4 com 19 (o saldo L2-R131 está na T-<saldo>); finais A_v3, B_v3, C_v3, D_v3; normativo 33 CONFERE; estilo_onda_3.md sem GATE; gatilho A emitido.

Linha nova 1 (o orquestrador atribui o número):
T-<saldo>; GCE; REFORÇO onda 3 — saldo da T-97 (D-REFORCO-2): 1 item AUTORAL L2-R131 em P2-2.4, que repõe o L2-R67 retirado (id não reutilizado). Requisitos: gabarito E com [TS] de troca única; aderência direta ao texto da 2.4 (identificação de oradores, marcação de pausa, ruído ou evento não falado), sem regra de condução da sessão e sem metafato de escopo de página; formato diferente de SH e de AP, de preferência NP ou PC; ponto distinto dos 19 da folha e sem gêmeo no pacote inteiro (T97_reconciliacao, seções 1 e 6); base oficial aberta na data, com trecho literal; não VOLÁTIL. QA própria da gce-cqfp, R1 e no máximo 2 rodadas. Entra na consolidação v1.10 se aceito antes da geração da T-104; senão, na v1.11. Estilo: item fixo na amostra do gbq-estilo da onda 4, não condicionante. AGORA (logo após esta reconciliação; antes da produção da gcb-cpp na T-74 e da T-98; D-RITMO-MAX); PENDENTE; gce-cpp → gce-cqfp → gce-gerencia; saida/gce/L2_reforco_onda3_saldo_v1.md

Linha nova 2 (o orquestrador atribui o número):
T-<errata>; GCE; ERRATA do Lote 2 — curso 2.8, "Riscos" (saida/gce/GCE_Lote2_v2_CPP.md, l. 507: "adaptação não corrige sotaque nem ruído") e aspecto (xv) do quesito 2.4 do padrão de resposta (saida/gce/GCE_Lote2_padroes_GCE.md, l. 136–138), já no pacote v1.9 (lotes[L2].curso e discursiva). Achado da gce-cqfp (QA_T97D_R1, seção 7): a documentação do Google ("Improve transcription results with model adaptation", https://docs.cloud.google.com/speech-to-text/docs/adaptation-model; "Last updated 2026-10-13 UTC") lista entre os usos da adaptação "Improving the accuracy of speech transcription when the supplied audio contains noise or is not very clear". A frase do curso, como está, leva a marcar C num item que a fonte faria E. Produção: a gce-cpp grava a proposta com o texto exato das duas trocas (núcleo apontado pela QA: a adaptação não remove o ruído nem trata a causa acústica, e sotaque pede dados acústicos, como diz o Lote 1; mas pode melhorar o reconhecimento dos termos esperados quando o áudio é ruidoso ou pouco claro), com a base reaberta na data e trecho literal, e a varredura das demais ocorrências ("lista de termos não corrige sotaque" no Lote 1 e no gabarito do Simulado 0 P2; L1-Q12), dizendo, para cada uma, se fica ou se muda. Nenhum item, gabarito objetivo, [TS] ou VOLÁTIL muda. Revisão: gce-cqfp (opus; não produziu), uma rodada mais uma, se houver ajuste. Reconciliação: gce-gerencia, com entrada na Tabela de Correções do GCE_Lote2_v2_CPP.md. Gatilhos: A para a errata do curso (errata textual, precedente D-L2-T84-ERRATA); D para o aspecto (xv), porque muda o padrão de resposta canônico de discursiva (D2). Absorção: na v1.10 (T-104) se os aceites vierem antes da geração, por acréscimo da Presidência ao escopo da D-ABSORCAO-V110; senão, na ocorrência seguinte. AGORA (depois do saldo da T-97 na fila da gce-cqfp); PENDENTE; gce-cpp → gce-cqfp → gce-gerencia; saida/gce/T<errata>_errata_proposta_2026-10-18.md

Acréscimo à T-11 (parte P2, gce-cqfp; janeiro, 4–8/1/2027):
- VOLÁTEIS (inaptos a simulado final até a reverificação): R24, R25, R37, R56, R57, R60, R61, R66, R77, R81, R82, R85, R94, R99, R100, R120, R121, R125.
- Conferência de base, sem efeito de VOLÁTIL: os outros 93. Notas: no R62, comparar o SHA-256 do tokenizer.py (3b48e361…ae30b85); em R79, R83 a R85, R89, R91, R93, R97 a R99, comparar os SHA-256 registrados no C_v3; no R70, verificar se a página da API V1 continua documentando o comportamento; no R108, conferir a data exibida; nos itens do SLA (R106, R107, R109, R110), conferir se a versão do SLA mudou (sub-regra da seção 4.1); nos itens RICD e Ato 251, conferir a vigência no Legin.

## 10. Gatilhos (texto para PARA_PRESIDENCIA.md; colar só depois dos v3 conferidos e do estilo_onda_3.md sem GATE)
10.1 GATILHO A | GCE | T-97 — REFORÇO onda 3, P2 folhas 2.1 a 2.8 (D-REFORCO-2): 111 itens AUTORAL reconciliados (L2-R19 a L2-R130, sem L2-R67) | saida/gce/L2_reforco_onda3_A_v3.md; B_v3.md; C_v3.md; D_v3.md; QA_T97A/B/C/D_R1 e R2_2026-10-18_gce-cqfp.md; QA_T97A/B/D_normativo_2026-10-18_qa-normativo.md; saida/gce/T97_reconciliacao_2026-10-18.md; saida/banco/estilo_onda_3.md | Por folha (partida v1.9 → nova): 2.1, 2.2, 2.3, 2.5, 2.6, 2.7 e 2.8 de 6 → 20; 2.4 de 6 → 19 (+1 pelo saldo L2-R131, em tarefa AGORA com QA própria); 48 → 159. Gabarito: 56 C / 55 E (50,5%). [TS]: 69 (62,2%; meta de 58). VOLÁTEIS novos: 18, nenhum de risco alto; o máximo por folha é 4/20 (2.5 e 2.8, no teto). Formato: máximo de 30% (SH na 2.5). Aderência: 43 PARCIAIS novos (só simulado diagnóstico); diretas por folha 10 a 19 (piso de 10 cumprido). QA: R1 12,5% e R2 0,9% (só o L2-R67, retirado). Normativo: 33 CONFEREM, 0 pendente. Gêmeos: 0 (11 proximidades registradas para a GBQ). D1 registradas: sub-regra de VOLÁTIL para cláusula de SLA (seção 4.1: conceito do instrumento = não VOLÁTIL; redação particular = VOLÁTIL; R106, R107, R109 e R110 não VOLÁTEIS, com conferência de base); R125 VOLÁTIL ("local" inclui região); R118 e R119 não VOLÁTEIS; R88 = SH; R128 com "o Plenário da Câmara" (texto exato da QA, sem R3). | Pergunta fechada: aceitar os 111 itens para consolidação no pacote v1.10 e ratificar, como D2 de rótulo, a sub-regra de VOLÁTIL para cláusula contratual da seção 4.1 — SIM ou NÃO? (Com NÃO à sub-regra, R106, R107, R109 e R110 viram VOLÁTEIS: a 2.7 vai a 4/20, no teto, e a onda a 22.)

10.2 GATILHO D | GCE | T-97 — leitura da meta "no mínimo 20 itens por item-folha" (D-REFORCO-2, Fundador) diante dos itens de aderência PARCIAL | saida/gce/T97_reconciliacao_2026-10-18.md (seção 3); saida/gce/T90_reconciliacao_2026-10-18.md (seção 2) | Folhas 2.x: 113 diretas e 46 PARCIAIS em 159; diretas por folha: 2.1 10/20, 2.2 13/20, 2.3 10/20, 2.4 10/19, 2.5 17/20, 2.6 16/20, 2.7 18/20, 2.8 19/20. Precedente: os PARCIAIS contaram para a meta de 6 (T-90/T-91, aceitos em D-T90-R2-ACEITE e D-T91-R3-ACEITE). Os PARCIAIS só servem a simulado diagnóstico (D-ADERENCIA). | Pergunta fechada: os itens de aderência PARCIAL contam para a meta "no mínimo 20 por item-folha" da D-REFORCO-2 — SIM ou NÃO? (SIM: nada muda, e vale o piso de 10 diretas por folha da seção 3.3. NÃO: abre-se saldo de 46 itens diretos nas folhas 2.x (2.1 10, 2.2 7, 2.3 10, 2.4 9 depois do L2-R131, 2.5 3, 2.6 4, 2.7 2, 2.8 1) e a mesma conta nas folhas 1.x e 3.x; se a Presidência entender que a leitura é do Fundador, encaminha-a pelo PARA_FUNDADOR.md.)

## 11. Ordem imediata
1. A gce-cpp grava os quatro v3 conforme a seção 5 e o Apêndice. O orquestrador ou a gce-gerencia confere por script (SHA-256 da tabela da seção 5).
2. O gbq-estilo faz a auditoria da seção 8.
3. O orquestrador abre as linhas novas da seção 9 (saldo e errata) e o acréscimo à T-11.
4. Com os v3 idênticos e a auditoria sem GATE, o estado passa a CONCLUÍDA e os gatilhos da seção 10 são colados.
5. O saldo L2-R131 corre antes da produção da gcb-cpp na T-74 e antes da T-98. A T-104 (v1.10) passa a AGORA com o aceite do gatilho A (D-ONDA3-FILA, 4).

## Apêndice — especificação literal dos v3 (números de linha da v2)
Operações: ('sub', L, antigo, novo) troca a substring exata, que ocorre uma vez na linha L; ('rep', L, novo) substitui a linha L inteira; ('del', L) apaga a linha L. Depois, a linha 1 passa a ser "hdr" e, logo abaixo dela, entram uma linha em branco e a linha "ver". Aplicação de referência: o script apply.py abaixo (python -I), que lê a v2 e grava o v3. A gce-cpp pode usar o script ou transcrever à mão, e o resultado tem de ser idêntico.

```python
# spec.py
# Especificação dos v3 (números de linha da v2). ops: ('sub', L, old, new) | ('rep', L, new) | ('del', L)
V='Versão v3: transcrição da reconciliação saida/gce/T97_reconciliacao_2026-10-18.md, seção 5.{s}. {txt} A resposta ao parecer, as descrições de escopo e de QA PENDENTE, os registros de estilo e as dúvidas são histórico da v2.'
PN=' · PENDENTE NORMATIVO'
S={}
S['A']=dict(hdr='# L2_reforco_onda3_A_v3.md — T-97 — 2026-10-18 — gerado por gce-cpp',
 ver=V.format(s=1,txt='Mudam só: a retirada da marca PENDENTE NORMATIVO dos 14 itens conferidos pelo qa-normativo (14/14 CONFERE) e o motivo da aderência PARCIAL de L2-R22 ("contexto institucional"). Enunciados, gabaritos, [TS], VOLÁTEIS e aderências não mudam.'),
 ops=[('sub',L,PN,'') for L in (80,81,82,89,90,92,93,104,105,107,108,111,112)]+
 [('sub',83,'PARCIAL (competência entre órgãos e coordenações, contexto institucional; D-ADERENCIA: só simulado diagnóstico) · PENDENTE NORMATIVO','PARCIAL (contexto institucional; D-ADERENCIA: só simulado diagnóstico)')]+
 [('sub',L,' PENDENTE NORMATIVO.','') for L in (277,280,283,304,307,313,316,336,339,345,348,357,360)]+
 [('sub',286,'Aderência: PARCIAL (competência entre órgãos e coordenações, contexto institucional; D-ADERENCIA: só simulado diagnóstico). PENDENTE NORMATIVO.','Aderência: PARCIAL (contexto institucional; D-ADERENCIA: só simulado diagnóstico).'),
  ('rep',174,'- PENDENTE NORMATIVO: nenhum (marca retirada dos 14 itens normativos pela D1 da gce-gerencia, reconciliação T-97, seção 2, depois do registro do qa-normativo: 14/14 CONFERE).'),
  ('rep',378,'| PENDENTE NORMATIVO | nenhum (14/14 CONFERE, QA_T97A_normativo_2026-10-18_qa-normativo.md; marca retirada na reconciliação T-97, seção 2) |')])
S['B']=dict(hdr='# L2_reforco_onda3_B_v3.md — T-97 — 2026-10-18 — gerado por gce-cpp',
 ver=V.format(s=2,txt='L2-R67 foi retirado (reprovado na R2 da gce-cqfp; id não reutilizado; reposição pelo saldo L2-R131, em tarefa própria) e não integra esta versão; a parte B tem 27 itens (P2-2.3: 14; P2-2.4: 13). Mudam ainda: aderência PARCIAL de L2-R73 e L2-R74 (texto exato da R2); SHA-256 do tokenizer.py na base de L2-R62; trecho da tabela de opções na base de L2-R72; contagens e tetos. Enunciados, gabaritos e [TS] dos 27 itens não mudam.'),
 ops=[('del',58),('del',110),('del',141),('del',225),('del',226),('del',227),('del',316),('del',317),('del',318),
  ('sub',64,'| n | direta |','| n | PARCIAL (formato do arquivo de transcrições de referência do Custom Speech, tema de 1.8/2.7; mesma página de C-R75 a R78 e D-R111; D-ADERENCIA: só simulado diagnóstico) |'),
  ('sub',65,'| n | direta |','| n | PARCIAL (transparência sobre legenda gerada por serviço automatizado, tema de 4.2 e 1.7/2.6; D-ADERENCIA: só simulado diagnóstico) |'),
  ('rep',118,'Formatos da folha (19; L2-R67 retirado): D 2, TS 4, SH 5, NP 1, PC 3, AP 4 (soma 19); maior formato: 5/19 = 26,3% (teto de 30% cumprido).'),
  ('rep',119,'VOLÁTEIS na folha (19): 3/19 = 15,8% (R07 existente, R61 e R66; teto de 20% cumprido); nenhum de risco alto.'),
  ('sub',147,'× R67 e R68 (mesma página)','× R68 (mesma página)'),
  ('rep',152,'- Formato (T89/T91): medido na folha, com os existentes contados pela classificação da CPP. 2.3: máximo 5/20 = 25% (SH 5, R59 reclassificado); 2.4 (19; L2-R67 retirado): máximo 5/19 = 26,3% (SH 5). Teto de 30% cumprido. Nenhum item novo usa "definição" em 2.4 (D fica em 2/19, legado de Q13 e Q16).'),
  ('rep',153,'- VOLÁTIL: 5 no lote (R56 médio; R57, R60, R61 e R66 baixo); nenhum de risco alto; nenhum entre os 5 substitutos de 2.4 que ficam. Por folha: 2.3 com 3/20 = 15% (R56, R57, R60); 2.4 com 3/19 = 15,8% (R07 existente, R61, R66). Teto de 20% cumprido.'),
  ('rep',154,'- Gabarito: 14 C e 13 E (51,9% de C), dentro da faixa de 40% a 60%. Por folha (novos): 2.3 com 7 C e 7 E; 2.4 com 7 C e 6 E. Folhas: 2.3 com 10 C e 10 E (20); 2.4 com 10 C e 9 E (19).'),
  ('rep',155,'- [TS]: 15 de 27: 13 em itens E (todos) e 2 em itens C (espelho: R48, R58). Dos 5 substitutos de 2.4 que ficam, 1 tem [TS] de troca única (R70). A meta de [TS] é conferida na onda inteira (reconciliação T-97, seção 7).'),
  ('sub',302,'aberto e lido em 18/10/2026 (HTTP 200; arquivo sem data de edição visível).','aberto e lido em 18/10/2026 (HTTP 200; arquivo sem data de edição visível; SHA-256 3b48e361a7e95b4ec0356ca6d72bba635778aa10269153136ee7bc34cae30b85, 12.338 bytes, registrado pela gce-cqfp na R2; na conferência de janeiro, comparar o SHA-256 e reabrir o trecho).'),
  ('sub',332,'for all speakers in a single channel." https://','for all speakers in a single channel." Na tabela de opções da mesma página, fora do exemplo: "Then the transcription file contains speaker entries (such as "speaker": 0 or "speaker": 1) for each transcribed phrase." https://'),
  ('sub',335,'Aderência: direta (formatação do arquivo de transcrição).','Aderência: PARCIAL (formato do arquivo de transcrições de referência do Custom Speech, tema de 1.8/2.7; mesma página de C-R75 a R78 e D-R111; D-ADERENCIA: só simulado diagnóstico).'),
  ('sub',338,'Aderência: direta.','Aderência: PARCIAL (transparência sobre legenda gerada por serviço automatizado, tema de 4.2 e 1.7/2.6; D-ADERENCIA: só simulado diagnóstico).'),
  ('rep',343,'| total | 27 (14 em P2-2.3, L2-R47 a L2-R60; 13 em P2-2.4, L2-R61 a L2-R74, sem L2-R67, retirado) |'),
  ('sub',344,'= 50,0%','= 51,9%'),
  ('rep',345,'| E | 13 (R47, R50, R51, R52, R53, R56, R59, R63, R64, R65, R68, R70, R71) = 48,1% |'),
  ('rep',346,'| faixa de C | 40% a 60% cumprida (51,9%) |'),
  ('rep',347,'| C por folha (novos) | 2.3: 7 C / 7 E; 2.4: 7 C / 6 E |'),
  ('rep',348,'| C por folha | 2.3: 10 C / 10 E (20); 2.4: 10 C / 9 E (19) |'),
  ('rep',349,'| [TS] | 15: 13 em itens E (R47, R50, R51, R52, R53, R56, R59, R63, R64, R65, R68, R70, R71) e 2 em itens C, espelho (R48, R58); meta conferida na onda (reconciliação T-97, seção 7); substituto [TS] que fica: R70 |'),
  ('rep',350,'| VOLÁTIL | 5 no lote: R56 (médio), R57, R60, R61 e R66 (baixo); risco alto: 0; novos por folha: 2.3 com 3, 2.4 com 2 |'),
  ('rep',351,'| VOLÁTIL por folha | 2.3: 3/20 = 15%; 2.4: 3/19 = 15,8% (R07 existente + R61 + R66); teto de 20% cumprido |'),
  ('rep',352,'| aderência | 8 direta (R48, R49, R56, R57, R62, R68, R70, R72); 19 PARCIAL (R47, R50, R51, R52, R53, R54, R55, R58, R59, R60, R61, R63, R64, R65, R66, R69, R71, R73, R74): só simulado diagnóstico (D-ADERENCIA); por folha: 2.3 com 10 diretas em 20 (6 canônicos + R48, R49, R56, R57) e 2.4 com 10 diretas em 19 (6 canônicos + R62, R68, R70, R72) |'),
  ('sub',353,'TS: R47, R50, R51, R63, R64, R67, R71;','TS: R47, R50, R51, R63, R64, R71;'),
  ('rep',355,'| formatos P2-2.4 (de 19) | D 2, TS 4, SH 5, NP 1, PC 3, AP 4 (maior: 26,3%); definição nova: 0 |'),
  ('rep',356,'| QA | R1 e R2 da gce-cqfp concluídas (R2: 1/28 reprovado, L2-R67, retirado); reconciliada em saida/gce/T97_reconciliacao_2026-10-18.md |'),
  ('sub',357,'R56 a R62, R66 a R70 e R72 a R74','R56 a R62, R66, R68 a R70 e R72 a R74'),
  ('sub',357,'os 6 VOLÁTEIS','os 5 VOLÁTEIS'),
  ('sub',157,' e só R67 usa "deve ter presente"',''),
  ('sub',365,'| R67, R68, R74 |','| R68, R74 |')])
S['C']=dict(hdr='# L2_reforco_onda3_C_v3.md — T-97 — 2026-10-18 — gerado por gce-cpp',
 ver=V.format(s=3,txt='Mudam só: formato de L2-R88 (NP → SH; QA_T97C_R2, seção 3), com as contagens de formato da P2-2.5 e da parte; a descrição do parâmetro remove_diacritics na base de L2-R85 (construtor de BasicTextNormalizer); a nota da lista de janeiro sobre a execução de teste. Enunciados, gabaritos, [TS], VOLÁTEIS e aderências não mudam.'),
 ops=[('sub',60,' | NP | ',' | SH | '),
  ('rep',91,'Contagem de formatos da folha de 20 (existentes + novos): D 2 (10%); SH 6 (30%); AP 5 (25%); PC 4 (20%); TS 3 (15%); NP 0. Soma 20. Teto de 30% (6 de 20) cumprido em todos os formatos, sem folga em SH (L2-R88 reclassificado como SH; reconciliação T-97): a folha não admite mais SH. D fica em 2 de 20 = 10% (legado de 33,3% diluído; nenhum D novo).'),
  ('sub',288,'; assinatura: “remove_diacritics: bool = False”','; parâmetro do construtor de BasicTextNormalizer (__init__): “remove_diacritics: bool = False”'),
  ('sub',304,'Formato: NP (número ou prazo): o julgamento decide por contagem de ocorrências (2 de 3).','Formato: SH (situação hipotética): a contagem de ocorrências é criada pelo cenário, e o ponto é o mecanismo da busca sensível à caixa (QA_T97C_R2, seção 3).'),
  ('rep',388,'| formatos de P2-2.5 (20) | D 2; SH 6; AP 5; PC 4; TS 3; NP 0 |'),
  ('rep',390,'| formatos dos 28 novos | PC 6; SH 8; AP 7; TS 5; NP 2; D 0 |'),
  ('sub',397,'; em R83 a R85, repetir a execução de teste.','; a reverificação se faz pelo texto e pelo SHA-256, e a execução de teste é só corroboração.')])
S['D']=dict(hdr='# L2_reforco_onda3_D_v3.md — T-97 — 2026-10-18 — gerado por gce-cpp',
 ver=V.format(s=4,txt='Mudam só: o ajuste mínimo do enunciado de L2-R128 ("o Plenário da Câmara", texto exato da QA_T97D_R2, seção 4), com a troca sutil correspondente; a retirada da marca PENDENTE NORMATIVO de L2-R128 (CONFERE, adendo do qa-normativo); a data exibida da página do L2-R108. Gabaritos, [TS], VOLÁTEIS e aderências não mudam.'),
 ops=[('sub',88,'(e não o Plenário)','(e não o Plenário da Câmara)'),
  ('sub',88,'PENDENTE NORMATIVO: item novo, conferência do qa-normativo solicitada','CONFERE: qa-normativo, adendo de 18/10/2026'),
  ('sub',242,'com que o Plenário se pronuncia','com que o Plenário da Câmara se pronuncia'),
  ('sub',281,'(metadado ms.date 2025-12-29)','(página com "Last updated on 2026-06-02"; metadado ms.date 2025-12-29)'),
  ('sub',362,'Troca sutil: Comissão por Plenário.','Troca sutil: Comissão por Plenário da Câmara.'),
  ('sub',362,' PENDENTE NORMATIVO (item novo).',' CONFERE (qa-normativo, adendo de 18/10/2026).'),
  ('sub',406,'| metadado ms.date 2025-12-29; verificado','| página com "Last updated on 2026-06-02"; metadado ms.date 2025-12-29; verificado')])
```

```python
# apply.py (lê spec.py; saída v3_<parte>.md no diretório corrente; renomear para saida/gce/L2_reforco_onda3_<parte>_v3.md)
import hashlib,sys
sys.path.insert(0,'.')
from spec import S
G='/home/user/felipeRM/saida/gce/'
for p,s in S.items():
    raw=open(G+f'L2_reforco_onda3_{p}_v2.md',encoding='utf-8').read()
    L=raw.split('\n'); N=L[:]
    dels=set(); nsub=nrep=0
    for op in s['ops']:
        i=op[1]-1
        if op[0]=='sub':
            c=N[i].count(op[2]); assert c==1,(p,op[1],op[2][:40],c); N[i]=N[i].replace(op[2],op[3]); nsub+=1
        elif op[0]=='rep': N[i]=op[2]; nrep+=1
        else: dels.add(i)
    N[0]=s['hdr']
    out=[N[0],'',s['ver']]+[x for j,x in enumerate(N) if j>0 and j not in dels]
    txt='\n'.join(out)
    open(f'v3_{p}.md','w',encoding='utf-8').write(txt)
    changed=sorted(set(op[1] for op in s['ops'] if op[0]!='del')|{1})
    print(p,'linhas trocadas',len(changed),'apagadas',len(dels),'subs',nsub,'reps',nrep,'sha',hashlib.sha256(txt.encode()).hexdigest(),len(txt.encode()))
    print('  ',changed)
    print('   PENDENTE NORMATIVO restantes:',[j+1 for j,x in enumerate(out) if 'PENDENTE NORMATIVO' in x][:20], ' R67 restantes:',[j+1 for j,x in enumerate(out) if 'R67' in x])
```

## Conferência dos v3 (orquestrador, 18/10/2026)
SHA-256 de A_v3, B_v3, C_v3 e D_v3 iguais aos esperados no Apêndice (b6911efb…, f3b33204…, 4bbde472…, 892526fc…). Sem R3. Próximo passo: auditoria do gbq-estilo (seção 8).

Fechamento (orquestrador, 18/10/2026): saida/banco/estilo_onda_3.md sem GATE (12/12 e L1-R131 aprovados; 56 C / 55 E). Estado final da seção 9 aplicado em TAREFAS.md (saldo = T-105; errata = T-106) e gatilhos 10.1 e 10.2 colados em PARA_PRESIDENCIA.md.
