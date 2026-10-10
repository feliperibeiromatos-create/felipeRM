# simulado_2_QA_2026-10-10.md — T-10 QA — 2026-10-10 — gerado por gbq-cqe

# QA independente do Simulado 2 (P2, final; T-10) como objeto

Agente: gbq-cqe (QA, opus). Não produzi, não montei e não reconciliei o Simulado 2: a montagem é da gbq-csc (T-10). Este QA atende ao critério de aceite de simulado final da D-SIM1-DEVOLVIDO e da D-SIM1-CANONICO: QA independente sobre o simulado como objeto. Trabalhei só com leitura. Nenhum item, ordem, numeração, comando, texto ou gabarito foi alterado. O único arquivo gravado é este. O git foi usado só para ler (`git status`, `git log`, `git show HEAD:`).

## Objeto e bases

- Objeto: `saida/simulados/simulado_2.md` (folha; sha256 47ddd4bfe6b77d3c…) e `saida/simulados/simulado_2_gabarito.md` (grade, mapa, verificação e exclusões; sha256 a2a3ce823e00ff75…).
- Bases canônicas (D-CANONICOS), seções (d) e (d-G):
  - `saida/gce/GCE_Lote1_v2_CPP.md` (5ac069292b122def…)
  - `GCE_Lote1C_v2_CPP.md` (a25e6e0b629899cb…)
  - `GCE_Lote2_v2_CPP.md` (2638d1317c307696…, com a errata T-28 no curso)
  - `GCE_Lote3_v2_CPP.md` (76ee8d3b9a36382a…, com a errata T-08 no curso)
  - Os quatro hashes são iguais aos que a produtora declarou. Portanto ela conferiu os mesmos arquivos que eu, já com as duas erratas.
- Erratas de consolidação: `GCE_Lote1_consolidacao_GCE.md`, `GCE_Lote1C_…`, `GCE_Lote2_…` e `GCE_Lote3_…` (Parte A e adendos).
- Registro: `saida/gbq/claude_GBQ_Registro_AUTORAL_v2.md` (c8e6c4758edb55cc…) e `claude_GBQ_Registro_AUTORAL_v3.md` (1c159213c93ab7d0…). Nos 90 ids de P2, as linhas do v2 e do v3 são idênticas: o v3 só acrescenta os Lotes 6a e 6b.
- Edital: `edital/modulo_RF_IA_P2.md` (transcrição literal; 23 subitens).
- Regras: R1, R1-N, R2, R3 e R4 do registro AUTORAL v2 (seção "Regras de elegibilidade"); D-QA-PENDENTE, D-ADERENCIA e D-CANONICOS (DECISOES.md e CLAUDE.md).
- Para o critério (5), também: `banco/banco.csv` (BQ-0002 a 0008), `saida/banco/T03_arbitragem_2026-10-09.md`, `saida/banco/qa_normativo_lgpd_2026-10-10.md` (T-13), `saida/gce/GCE_ItensReais_P9_GCE.md` e a linha T-10 de TAREFAS.md.

## Método

- Script próprio, escrito do zero nesta tarefa: `/tmp/claude-0/-home-claude/3cf5e5a2-0a00-52ee-a3d1-ce0f04412748/scratchpad/s3/qa_sim2/qa_sim2.py`. A saída está em `result.json`, na mesma pasta. Não li nem usei o `s3/t10/verify.py` da produtora nem o script da T-34.
- O script faz o seguinte:
  1. Extrai de cada lote o bloco "(d) VERSÃO DO ESTUDANTE" (comando e 90 enunciados) e o bloco "(d-G) GABARITO COMENTADO" (90 entradas). Cada entrada vai de "Qnn." até a linha em branco. As linhas são unidas por espaço simples, sem espaço apenas depois de hífen ou travessão-ene colado à palavra ("áudio–texto", "completá-lo").
  2. Extrai da folha os blocos "### Comando N" e os 40 itens `**n.**`. Do gabarito, extrai a grade 8×5 e as 40 linhas do mapa, desescapando `\|`.
  3. Compara por igualdade exata de cadeia:
     - enunciado da folha = (d);
     - gabarito da grade = mapa = 1º caractere do d-G = registro v2 = registro v3;
     - [TS] do mapa = marca "[TS]" logo depois do gabarito no d-G = presença de "[TS]" no d-G = coluna TS do v2 e do v3;
     - justificativa do mapa = entrada d-G integral sem "Qnn. ";
     - arquivo e lote do mapa = arquivo onde o id foi achado;
     - subitem do mapa = registro, e nome do subitem = edital literal;
     - comando do bloco da folha = comando canônico do lote do item, sem faixa ("julgue os itens [de] X a Y." → "julgue os itens a seguir.").
     - Sem considerar espaços, a comparação dá o mesmo resultado.
  4. Elegibilidade. São marcas de exclusão:
     - VOLÁTIL no d-G ou no registro (excluída a negação "NÃO VOLÁTIL");
     - REVERIFICAR, ou o id L3-Q21;
     - "PENDENTE", "a confirmar" ou "DESATUALIZADO";
     - item tocado por errata de consolidação: busca de "(d) Qnn", "(d-G) Qnn" e "(d-G), Qnn" nos quatro consolidados;
     - id fora do registro AUTORAL.
  5. Folha sem pistas. Busca de:
     - ids de lote ou de banco, "Lote", "Q" seguido de dois dígitos;
     - VOLÁTIL, REVERIFICAR, PENDENTE, TRF6, [TS] ou "troca sutil";
     - contagens C/E, "%", "certos/errados";
     - AUTORAL, CEBRASPE, ANALOGA, QA, "[V ", NORMATIVO, "convertido", ADERÊNCIA, "F" seguido de dígito.
     - Também confere que as 40 linhas "Resposta: [   ]" estão vazias.
  6. Globais. O script confere:
     - numeração contínua e ids únicos;
     - contagens C/E, [TS], por lote, por bloco e por subitem;
     - a sequência declarada, a maior corrida e o número de C em cada dezena;
     - a partição do universo P2 (90 = 40 selecionados + 50 excluídos declarados), conferindo o subitem e o gabarito de cada excluído contra o registro;
     - a repetição de texto contra `simulado_0.md`, `simulado_0_v0.2.md` e `simulado_1.md`;
     - as seções (d) e (d-G) dos Lotes 2 e 3, atuais × HEAD, para isolar as erratas T-28 e T-08.
- Ajuste do próprio script, feito antes do resultado final: a primeira execução acusou o item 28 (L2-Q24) como "PENDENTE". Era um falso positivo do meu regex, que não distinguia maiúsculas e casava com "inde**pendente**" na justificativa. Também listou L2-Q23 como VOLÁTIL, por causa do texto "NÃO VOLÁTIL (classificação final da CQFP)". Corrigi o regex (maiúsculas exatas e exclusão da negação) e rodei de novo.
- Controle negativo: fiz uma cópia temporária com quatro alterações:
  - retirada de um acento no item 2;
  - gabarito do item 7 trocado na grade;
  - justificativa do item 15 truncada;
  - id "(L1-Q17)" inserido numa linha de resposta.
  - O script acusou as quatro alterações (itens 2, 7 e 15; pista na folha; respostas não vazias) e nada além delas. A cópia foi apagada.

## (1) Literalidade — 40/40

- Enunciado da folha = (d) canônico: 40/40.
- Gabarito: grade = mapa = d-G = registro v2 = registro v3, em 40/40.
- [TS]: mapa = d-G = registro, em 40/40 (20 com a marca: 8 C e 12 E).
- Justificativa do mapa = entrada integral do d-G sem o identificador: 40/40.
- Arquivo e lote de origem: 40/40. Subitem do mapa = registro: 40/40. Nome do subitem = edital literal: 40/40.
- As seções (d) e (d-G) dos Lotes 2 e 3 são idênticas, byte a byte, às de HEAD. As erratas T-28 (Derep, no "Contexto institucional" do curso do L2) e T-08 (Ato da Mesa nº 225/2025, no curso do 3.1 do L3) não tocam item, gabarito, [TS] nem justificativa. O Simulado 2 não depende do desfecho delas, que ainda estão EM CURSO (gce-cqfp → gce-gerencia).

## (2) Comando literal do lote — 40/40

| Comando | itens | comando da folha | comando canônico (seção (d)) | resultado |
|---|---|---|---|---|
| 1 | 1–40 (L1 8, L1-C 5, L2 14, L3 13) | Julgue os itens a seguir (C = certo, E = errado). | Lote 1, Lote 1-C, Lote 2 e Lote 3: uma única linha de comando, idêntica nos quatro, sem faixa de numeração | ok, 40/40 |

- Cada um dos quatro (d) tem uma só linha de comando. Ela é idêntica, caractere a caractere, à linha do Comando 1 da folha.
- A leitura por item e a leitura por bloco coincidem: não há bloco que junte comandos de redação diferente. A divergência D-1 do Simulado 1 não pode ocorrer aqui.
- O mapa indica "Comando 1" para os 40 itens.

## (3) Elegibilidade — 40/40

- R1 (VOLÁTIL): nenhum dos 40 tem a marca. Os 4 VOLÁTEIS de P2 (L1-Q14, Q16, Q18, Q19) estão fora.
  - L2-Q23 traz "NÃO VOLÁTIL (classificação final da CQFP)". Não é VOLÁTIL e, de todo modo, não foi selecionado.
- R1-N (REVERIFICAR): L3-Q21 está fora. Nenhum dos 40 tem a marca.
- D-QA-PENDENTE:
  - 0 ocorrência de "QA PENDENTE" nos quatro arquivos canônicos.
  - Nenhum d-G selecionado traz "PENDENTE", "a confirmar" ou "DESATUALIZADO".
  - Situação de QA dos lotes de origem, segundo os consolidados: L1 APROVADO (CQFP R2); L1-C, L2 e L3 APROVADO COM RESSALVAS, sem bloqueante (CQFP R2). Os quatro são canônicos por D-CANONICOS.
- Erratas de consolidação. Estes são os itens tocados em (d) ou (d-G), segundo a minha busca nos consolidados:
  - L1-Q07 (E1), L1-Q08 (E2), L1-Q11 (E3) e L1-Q01 (E4, coerência do d-G);
  - L1C-Q26 (E1) e L1C-Q23 (E3);
  - L2-Q21 (E1 d) e L2-Q14 (E6);
  - L3-Q20 (E3).
  - São 9 itens, exatamente os 9 que a produtora declarou ter deixado de fora. Nenhum deles está no simulado. Nos 40 selecionados, o texto canônico do v2 vale sem emenda, tal como a produtora declarou.
- R2: não se aplica, porque não há item do Lote 4 nem do banco.
- R3 e D-ADERENCIA: os 40 são AUTORAL do registro (90/90 ids de P2 no v2 e no v3), com aderência direta por construção (R4). Nenhum item real.
- Itens marcados "normativo" no registro: 1, 4, 12, 30, 31 e 36 (L3-Q25, Q24, Q28, Q27, Q17 e Q18). A marca não os exclui, porque não é REVERIFICAR.
  - Os dispositivos citados nos d-G são: Lei 9.610/1998, arts. 24, II; 27; 41; 45; 49, I; LGPD, arts. 5º, I, III, VI, VII e XI; 12; 13, § 4º; 39; 46.
  - Nenhum deles está entre os alterados pela Lei 15.352/2026, que alterou o art. 5º, VIII e XIX, o Capítulo IX e os arts. 55-A e 55-C (D-LEI15352-PROV; confirmado pela tabela de alterações em `qa_normativo_lgpd_2026-10-10.md`).
- Inéditos: nenhum dos 40 enunciados aparece em `simulado_0.md`, `simulado_0_v0.2.md` ou `simulado_1.md`. Não existe arquivo do Simulado 0-P2 (T-24 PENDENTE).
- Partição: 40 selecionados + 5 inelegíveis + 45 elegíveis não selecionados = 90 (universo P2 AUTORAL). O subitem e o gabarito declarados para os 50 excluídos conferem com o registro.

## (4) Folha sem pistas — cumprida

- Nenhuma ocorrência de: id de lote ou de banco, "Lote", VOLÁTIL, REVERIFICAR, PENDENTE, TRF6, [TS] ou "troca sutil", contagem C/E, rótulo de fonte, "QA", marca [V], NORMATIVO ou ADERÊNCIA.
- A busca teve dois acertos, ambos falsos positivos no texto dos próprios itens: "100%" no item 21 (enunciado canônico de L1C-Q22) e "convertido" no item 23 (enunciado canônico de L1C-Q24, sobre o sinal de áudio).
- As 40 linhas "Resposta: [   ]" estão vazias. A numeração vai de 1 a 40 sem lacuna.
- A folha remete gabarito, mapa e justificativas a arquivo separado e não traz nota de montagem nem contagem.

## (5) Falta dos 7 CEBRASPE_ANALOGA do Lote 3 frente à D-ADERENCIA — duas leituras, sem decisão

Fatos conferidos:
- A linha T-10 de TAREFAS.md diz: "SIMULADO 2 — P2 com itens inéditos dos Lotes 1, 1-C, 2, 3 (40) + 7 ANALOGA do Lote 3".
- O simulado tem 40 itens e registra a falta na seção "Regras e falta registrada" do gabarito.
- BQ-0002 a BQ-0008 (TRF6 2024, aplicação 19/01/2025, Cargo 2, itens 70 a 76, P2-4.1) trazem no banco "aderência temática ampla (LGPD/privacidade geral; edital 4.1 trata de LGPD em sistemas de transcrição e IA)".
  - Pelo mapeamento do contrato v1.1 (T-26), isso equivale a "parcial".
  - Esses itens não estavam entre as 7 aderências arbitradas na T-03, e nenhuma decisão os reclassificou.
- D-ADERENCIA ("parcial = só simulado diagnóstico") e CLAUDE.md têm a mesma redação.
- O registro AUTORAL v2 manda tratá-los como itens do banco (R3), sujeitos à D-ADERENCIA (R4).
- Os 7 já estão no Simulado 0 v0.2, que é diagnóstico (D-SIM0-V02).
- A regra da gbq-csc é "não repita item de simulado anterior".
- Correção de fato para a Gerência. A produtora escreveu que "não há parecer que a feche" (a T-13). Na verdade, há um parecer gravado: `saida/banco/qa_normativo_lgpd_2026-10-10.md` (qa-normativo, 10/10/2026, 14:56, anterior à montagem das 15:03).
  - Esse parecer dá BQ-0002 a 0008 como MANTIDOS (7/7), sem nenhuma candidata a gatilho D.
  - Ainda não foi reconciliado pela gbq-gerencia: a T-13 segue EM CURSO em TAREFAS.md.
  - O parecer registra uma observação sobre BQ-0003: o item usa a denominação anterior, "Autoridade Nacional de Proteção de Dados".

Leitura A (a falta é correta; o simulado cumpre a T-10 nos limites da decisão superior):
- A D-ADERENCIA é decisão da Presidência e prevalece sobre o texto da linha de tarefa.
- O Simulado 2 é final. Itens de aderência parcial não podem entrar nele, com ou sem T-13 reconciliada.
- Incluí-los também repetiria itens do Simulado 0 v0.2.
- A falta está registrada e motivada, com as condições de inclusão futura: (a) T-13 reconciliada sem gatilho D; (b) exceção decidida pela Presidência ou reclassificação de aderência pela GBQ; (c) bloco próprio sob o comando original do caderno (T-29).
- Nessa leitura, o objeto está completo com 40 itens, e o veredito abaixo não muda.

Leitura B (a falta é descumprimento da ordem da T-10):
- A T-10 nomeia expressamente "+ 7 ANALOGA do Lote 3", e a D-FUNDADOR-AGORA-1 a promoveu nesses termos. Seria ordem específica, que pressupõe a inclusão.
- A Parte D da consolidação do Lote 3 integra os itens 70 a 76 ao pacote canônico do lote, e a decisão C1 da GCE (P9) só os vedava em simulado até a conferência normativa. Essa condição foi cumprida pela GCE-CQFP em 08/10 e agora também pelo parecer da T-13, ainda não reconciliado.
- Nessa leitura, o simulado estaria incompleto: 40 de 47.
- Como a inclusão em simulado final contraria a D-ADERENCIA, sanar a falta exigiria uma de duas coisas: a reclassificação de aderência pela GBQ (D1) ou uma exceção decidida pela Presidência (D2), já que a GBQ não revoga decisão da Presidência.
- A inclusão também teria de lidar com a repetição dos itens no Simulado 0 v0.2.
- Na falta de qualquer dessas providências, a alternativa é corrigir a linha T-10 para "40 AUTORAL".

A arbitragem entre A e B cabe à gbq-gerencia (e, na leitura B, à Presidência, por ser D2), não a este QA. O veredito de (1) a (4) vale para os 40 itens do objeto em qualquer das duas leituras.

## Globais (recalculados)

- 40 itens, numeração 1–40 contínua na folha, na grade e no mapa; ids únicos; um só comando.
- 20 C / 20 E. 20 [TS] (8 C, 12 E). Número de C por dezena: 5 / 5 / 5 / 5. Maior corrida: 3.
- Sequência: CCEECECEECEECCCECECEEECECCCEECCECECECECE, igual à declarada.
- Por lote: L1 = 8, L1-C = 5, L2 = 14, L3 = 13.
- Por bloco (itens, C): 1 (13, 6) · 2 (14, 7) · 3 (7, 4) · 4 (6, 3).
- Por subitem (itens, C):
  - 1.1 (2, 0) · 1.2 (3, 2) · 1.3 (1, 1) · 1.4 (2, 1) · 1.5 (2, 1) · 1.6 (1, 0) · 1.7 (1, 1) · 1.8 (1, 0)
  - 2.1 a 2.5 e 2.7 (2, 1) cada · 2.6 (1, 1) · 2.8 (1, 0)
  - 3.1 a 3.3 (2, 1) cada · 3.4 (1, 1)
  - 4.1 a 4.3 (2, 1) cada
  - Cobertura: 23/23.
- Ordem: nenhum par de itens consecutivos do mesmo subitem; nunca três itens seguidos do mesmo bloco.
- Tudo confere com a seção "Verificação" do gabarito.

## Observações (sem efeito no veredito; para a Gerência)

- O-1. Pista cruzada fraca (conteúdo, não metadado), item 9 (L3-Q02, E):
  - O item 16 (L3-Q10, E) traz a premissa de que um tipo de sumarização "redige frases novas", o que desmente o "ambas reproduzem as falas" do item 9.
  - O item 13 (L3-Q09, C), "resumos podem omitir ou distorcer", aponta no mesmo sentido.
  - O item 16 é E no todo (inversão), por isso a pista é indireta.
  - É a mesma natureza de pista que a produtora usou para excluir o L3-Q12. Trocar ou não é D1 da Gerência.
- O-2. Pista cruzada muito fraca: o item 33 (L2-Q08, C), "a revisão humana continua necessária", e o item 20 (L2-Q06, E), "basta conferir os trechos de baixa confiança". O 33 não decide o 20.
- O-3. O item 6 (L1C-Q28) tem no registro a marca "discriminação baixa (NB5)". A consolidação do L1-C a registra "sem alteração". Não é regra de exclusão.
- O-4. As justificativas dos itens 14 (L1-Q05, [V 07/10/2026 — F8]) e 23 (L1C-Q24, [V 08/10/2026 — arXiv 2006.11477]) têm marca de verificação de fonte. Não são VOLÁTEIS pelo registro nem pelo d-G.
- O-5. A errata E4 do L1-C (registro de verificação do wav2vec 2.0) acrescenta texto à "Fonte nova da C1" do cabeçalho de evidência (linha 27), e não ao d-G do Q24. Por isso a justificativa do item 23 é a do v2 sem emenda, como a produtora declarou. Numa leitura ampla, que estendesse a E4 a toda citação da fonte, o d-G do Q24 ganharia o acréscimo; a justificativa não muda de sentido nem de gabarito.
- O-6. A folha diz "itens 1 a 4 do edital (item 14.2.4)". O conteúdo dos subitens confere com o edital do Projeto, mas o número 14.2.4 não foi conferido nesta tarefa. Isso é informativo, não pista.

## Veredito por item

| nº | id | sub | gab | [TS] | enunciado = (d) | gab (grade = mapa = d-G = reg v2 = reg v3) | [TS] (mapa = d-G = reg) | justificativa = d-G | arquivo/subitem/edital | comando = canônico do lote | elegibilidade (R1/R1-N/D-QA-PENDENTE/errata/R3-R4) | veredito |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L3-Q25 | 4.2 | C | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 2 | L2-Q27 | 2.7 | C | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 3 | L1-Q03 | 1.2 | E | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 4 | L3-Q24 | 4.2 | E | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 5 | L2-Q22 | 2.6 | C | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 6 | L1C-Q28 | 1.4 | E | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 7 | L2-Q17 | 2.5 | C | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 8 | L2-Q01 | 2.1 | E | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 9 | L3-Q02 | 3.1 | E | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 10 | L1-Q17 | 1.7 | C | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 11 | L3-Q07 | 3.2 | E | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 12 | L3-Q28 | 4.3 | E | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 13 | L3-Q09 | 3.3 | C | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 14 | L1-Q05 | 1.3 | C | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 15 | L3-Q05 | 3.2 | C | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 16 | L3-Q10 | 3.3 | E | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 17 | L1-Q04 | 1.2 | C | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 18 | L2-Q16 | 2.4 | E | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 19 | L3-Q01 | 3.1 | C | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 20 | L2-Q06 | 2.2 | E | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 21 | L1C-Q22 | 1.1 | E | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 22 | L2-Q11 | 2.3 | E | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 23 | L1C-Q24 | 1.2 | C | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 24 | L1C-Q21 | 1.1 | E | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 25 | L2-Q02 | 2.1 | C | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 26 | L2-Q13 | 2.4 | C | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 27 | L3-Q16 | 3.4 | C | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 28 | L2-Q24 | 2.7 | E | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 29 | L2-Q20 | 2.5 | E | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 30 | L3-Q27 | 4.3 | C | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 31 | L3-Q17 | 4.1 | C | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 32 | L2-Q29 | 2.8 | E | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 33 | L2-Q08 | 2.2 | C | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 34 | L1C-Q30 | 1.5 | E | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 35 | L1-Q09 | 1.4 | C | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 36 | L3-Q18 | 4.1 | E | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 37 | L1-Q10 | 1.5 | C | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 38 | L1-Q13 | 1.6 | E | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 39 | L2-Q10 | 2.3 | C | não | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 40 | L1-Q20 | 1.8 | E | sim | ok | ok | ok | ok | ok | ok | ok | APROVADO |

## Veredito geral

**APROVADO / CONFERIDO — 40/40 (100%); 0 REPROVADO (0%); 0 CORRIGIR.**

- Os critérios (1) a (4) foram cumpridos em 40/40.
- O critério (5) fica registrado em duas leituras (A e B) para a gbq-gerencia, sem decisão deste QA. Na leitura B, a falta dos 7 ANALOGA é questão de completude da ordem e de decisão superior (D-ADERENCIA), não defeito dos 40 itens conferidos.
- Nenhum gate de CLAUDE.md foi atingido (reprovação de 0%).
- Próximo passo, fora deste QA: reconciliação pela gbq-gerencia, inclusive a arbitragem do (5) e das observações O-1 e O-2, e depois o gatilho A.
- Se um dos quatro lotes for regravado nas seções (d) ou (d-G) antes do aceite, este QA deve ser refeito: a T-28 e a T-08 ainda estão em QA na GCE, embora hoje não toquem essas seções.
