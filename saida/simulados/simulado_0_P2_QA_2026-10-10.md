# simulado_0_P2_QA_2026-10-10.md — T-24 QA — 2026-10-10 — gerado por gbq-cqe

# QA independente do Simulado 0-P2 (T-24, diagnóstico de P2, D-SIM0-P2) como objeto

Agente: gbq-cqe (QA, opus). Não produzi, não montei e não reconciliei o Simulado 0-P2; a montagem é da gbq-csc (T-24). Trabalhei só com leitura: nenhum item, ordem, numeração, comando, texto ou gabarito foi alterado. O único arquivo gravado é este. Usei o git só para ler (`git status`, `git diff --stat`, `git show HEAD:`).

## Objeto e bases

- Objeto: `saida/simulados/simulado_0_P2.md` (folha; sha256 2415c3c58e06be42…) e `saida/simulados/simulado_0_P2_gabarito.md` (sha256 d8a2832ce33a68c4…).
- Bases canônicas (D-CANONICOS), seções (d) e (d-G):
  - `saida/gce/GCE_Lote1_v2_CPP.md` (5ac069292b122def…);
  - `GCE_Lote1C_v2_CPP.md` (a25e6e0b629899cb…);
  - `GCE_Lote2_v2_CPP.md` (6bb88330fe0f9200…);
  - `GCE_Lote3_v2_CPP.md` (d3388ecada7310ac…).
  - Os hashes são os mesmos que a produtora declarou.
  - Os Lotes 2 e 3 foram regravados às 15:21 com as erratas D1 da GCE (`GCE_erratas_reconciliacao_2026-10-10.md`; T-08 e T-28 CONCLUÍDAS pela gce-gerencia). As seções (d) e (d-G) dos dois continuam idênticas, byte a byte, às de HEAD.
- Erratas de consolidação: os quatro `GCE_Lote*_consolidacao_GCE.md`, sem modificação em relação a HEAD.
- Registro: `saida/gbq/claude_GBQ_Registro_AUTORAL_v3.md` (1c159213c93ab7d0…). Nos 90 ids de P2, as linhas são idênticas às do v2.
- Edital: `edital/modulo_RF_IA_P2.md`.
- Decisão de referência: D-SIM0-P2 — 25 itens AUTORAL dos Lotes 1, 1-C, 2 e 3, sem VOLÁTIL, cobrindo os 4 blocos em proporção ao edital, com gabarito separado.

## Método

- Script: `/tmp/claude-0/-home-claude/3cf5e5a2-0a00-52ee-a3d1-ce0f04412748/scratchpad/s3/qa_s0p2/qa_s0p2.py`, com saída em `result.json` na mesma pasta.
  - É uma adaptação do meu `qa_sim2.py` (QA do Simulado 2), escrito do zero por esta unidade, ajustada para N = 25.
  - Não li nem usei os scripts da produtora (`s3/t24/build24.py`, `s3/t24/verify24.py`).
- Comparações por igualdade exata de cadeia, com o mesmo método do QA do Simulado 2:
  - enunciado da folha = (d);
  - gabarito da grade = mapa = 1º caractere do d-G = registro v2 = registro v3;
  - [TS] do mapa = marca do d-G = registro;
  - justificativa do mapa = entrada integral do d-G sem "Qnn. ";
  - arquivo, subitem e nome do subitem = edital;
  - comando do bloco = comando canônico do lote.
- Elegibilidade, por marcas e por id:
  - VOLÁTIL, exceto a negação "NÃO VOLÁTIL";
  - REVERIFICAR ou L3-Q21;
  - PENDENTE, "a confirmar" ou DESATUALIZADO;
  - errata de consolidação em (d) ou (d-G);
  - presença no registro AUTORAL.
- Repetição, verificada de duas formas:
  - por id, nas linhas de mapa dos gabaritos dos Simulados 0, 0 v0.2, 1 e 2;
  - por texto, nas folhas `simulado_0.md`, `simulado_0_v0.2.md`, `simulado_1.md` e `simulado_2.md`.
- Na partição do universo, a lista "Já no Simulado 2" declarada pela produtora foi conferida contra o mapa do Simulado 2.
- Folha sem pistas: os mesmos padrões do QA do Simulado 2.
- Controle negativo, numa cópia temporária com quatro alterações. O script acusou as quatro e nada além delas:
  - acento retirado no item 1;
  - "[TS]" inserido no item 5;
  - gabarito do item 4 trocado na grade;
  - justificativa do item 23 truncada.
  - Acusações: itens 1, 4, 5 e 23, e a pista no item 5. A cópia foi apagada.

## (1) Literalidade — 25/25

- Enunciado da folha = (d) canônico: 25/25.
- Gabarito (grade = mapa = d-G = registro v2 = registro v3): 25/25.
- [TS] (mapa = d-G = registro): 25/25. São 14 com [TS]: 8 C e 6 E.
- Justificativa do mapa = entrada integral do d-G sem o identificador: 25/25.
- Arquivo e lote de origem, subitem = registro e nome do subitem = edital: 25/25.

## (2) Comando literal do lote — 25/25

- A folha tem um único bloco, "Comando 1": `Julgue os itens a seguir (C = certo, E = errado).`.
- É idêntico, caractere a caractere, à única linha de comando da seção (d) dos quatro lotes, que não tem faixa de numeração.
- O mapa indica "Comando 1" para os 25 itens.

## (3) Elegibilidade — 25/25

- VOLÁTIL: nenhum dos 25 está marcado, nem no registro v3 nem no d-G.
  - Os 4 VOLÁTEIS de P2 (L1-Q14, Q16, Q18, Q19) estão fora.
  - Item 22 (L2-Q23): o d-G traz "[V 08/10/2026 — F3] … NÃO VOLÁTIL (classificação final da CQFP)". O script trata a negação; o registro v3 não marca o item; a consolidação do Lote 2 (Parte C) diz "VOLÁTEIS = 0 (Q23, W3C, é NÃO VOLÁTIL)". O item não é VOLÁTIL. A palavra aparece só na justificativa do mapa, no gabarito, e não na folha.
- REVERIFICAR: L3-Q21 está fora; nenhum dos 25 tem a marca.
- QA PENDENTE:
  - não há ocorrência nos quatro lotes;
  - nenhum d-G selecionado traz PENDENTE, "a confirmar" ou DESATUALIZADO;
  - os lotes de origem são canônicos (D-CANONICOS).
- Erratas de consolidação. Os itens tocados são 9: L1-Q01, Q07, Q08, Q11; L1C-Q23, Q26; L2-Q14, Q21; L3-Q20. Nenhum está entre os 25, como a produtora declarou.
- AUTORAL: 25/25 estão no registro v3, com aderência direta por construção (R4). Não há item de banco; R2 não se aplica.
- Itens marcados "normativo" no registro: 6, 8, 13 e 21 (L3-Q29, Q19, Q30 e Q23).
  - Dispositivos citados: LGPD arts. 48; 7º, § 3º; 5º, XV; 33, I e II; Lei 9.610/1998, art. 8º, IV.
  - Nenhum foi alterado pela Lei 15.352/2026, que mexeu no art. 5º, VIII e XIX, no Capítulo IX e nos arts. 55-A e 55-C.

## (4) Repetição — nenhuma

- Por id: nenhum dos 25 aparece no mapa dos Simulados 0, 1 ou 2. O Simulado 0 v0.2 só tem itens de banco (BQ); nenhum id AUTORAL de P2 aparece em `simulado_0*`.
- Por texto: nenhum enunciado aparece nas folhas dos Simulados 0, 0 v0.2, 1 ou 2.
- A lista "Já no Simulado 2 (40)" do gabarito é igual aos 40 ids do mapa do Simulado 2.
- Partição do universo P2: 25 selecionados + 5 inelegíveis + 40 do Simulado 2 + 20 elegíveis não selecionados = 90. O subitem e o gabarito declarados dos excluídos conferem com o registro.

## (5) Folha sem pistas — cumprida

- A busca não encontrou nenhuma destas ocorrências na folha:
  - id de lote ou de banco, "Lote";
  - VOLÁTIL, REVERIFICAR, PENDENTE, TRF6;
  - [TS] ou "troca sutil";
  - contagem C/E;
  - rótulo, "QA", marca [V], NORMATIVO ou ADERÊNCIA.
- As 25 linhas "Resposta: [   ]" estão vazias. A numeração vai de 1 a 25 sem lacuna.

## (6) Proporção por bloco e cobertura

| Bloco | subitens | proporção simples (25 × subitens/23) | arredondamento por maiores restos | no simulado (itens, C) | elegíveis disponíveis fora do Simulado 2, sem errata/VOLÁTIL |
|---|---|---|---|---|---|
| 1 | 8 | 8,7 | 9 | 7 (3 C) | 7 (todos usados) |
| 2 | 8 | 8,7 | 9 | 9 (5 C) | 15 |
| 3 | 4 | 4,3 | 4 | 5 (3 C) | 11 |
| 4 | 3 | 3,3 | 3 | 4 (2 C) | 10 |

- Os 4 blocos estão cobertos, como exige a D-SIM0-P2.
- O bloco 1 está 2 itens abaixo da proporção, e os blocos 3 e 4 estão 1 item acima cada.
- Conferi por contagem que a falta é forçada pelo conjunto elegível. O bloco 1 tem 30 itens AUTORAL. Saem 4 VOLÁTEIS, 13 já usados no Simulado 2 e 6 com errata (L1-Q01, Q07, Q08, Q11; L1C-Q23, Q26). Restam 7, e os 7 foram usados.
- Subitens 1.2 e 1.8 sem item: 21 de 23 cobertos. Falta registrada pela produtora, com motivo que confere com a contagem:
  - 1.2: L1-Q03, L1-Q04 e L1C-Q24 estão no Simulado 2, e o L1C-Q23 tem a errata E3.
  - 1.8: L1-Q18 e L1-Q19 são VOLÁTEIS, e o L1-Q20 está no Simulado 2.
- Duas leituras para a Gerência, sem decisão:
  - A. Cumprida "em proporção ao edital" no limite do conjunto elegível. É um simulado diagnóstico, a falta está registrada e não há item disponível que respeite ao mesmo tempo a literalidade, a não repetição e a exclusão de VOLÁTIL.
  - B. Proporção não atendida no bloco 1. Para atendê-la, seria preciso uma de duas coisas, ambas decisão D1 da GBQ e fora deste QA:
    - admitir itens com errata, com a errata aplicada ao texto por quem pode editar item (por exemplo, L1C-Q23 cobriria também o 1.2);
    - admitir repetição de itens do Simulado 2.
- Essas leituras não afetam o veredito por item.

## Globais (recalculados)

- 25 itens, ids únicos, um só comando.
- 13 C / 12 E; 14 [TS] (8 C, 6 E).
- Por lote: L1 = 4, L1-C = 3, L2 = 9, L3 = 9.
  - Isso confere com o gabarito. O resumo da ordem recebida ("L1 3, L1C 4") inverte os dois números: os itens de L1 são Q02, Q06, Q12 e Q15; os de L1-C são Q25, Q27 e Q29.
- Por bloco (itens, C): 1 (7, 3) · 2 (9, 5) · 3 (5, 3) · 4 (4, 2).
- Por subitem (itens, C):
  - 1.1 (1, 0) · 1.3 (2, 0) · 1.4 (1, 1) · 1.5 (1, 1) · 1.6 (1, 0) · 1.7 (1, 1)
  - 2.1 (1, 1) · 2.2 (1, 0) · 2.3 (1, 0) · 2.4 (1, 1) · 2.5 (1, 1) · 2.6 (1, 1) · 2.7 (1, 0) · 2.8 (2, 1)
  - 3.1 (1, 1) · 3.2 (1, 1) · 3.3 (1, 1) · 3.4 (2, 0)
  - 4.1 (1, 1) · 4.2 (1, 0) · 4.3 (2, 1)
- Sequência: CCCECEECCCEECCECCECEECEEE, igual à declarada. Maior corrida: 3.
- Número de C: 7 nos itens 1–12 e 6 nos itens 13–25.
- Ordem dos itens:
  - nenhum par consecutivo do mesmo subitem;
  - nunca três itens seguidos do mesmo bloco;
  - os 11 pares de pista fraca declarados ficam a 5 ou mais posições de distância (mínimo 5: L1-Q12 × L2-Q30 e L2-Q07 × L2-Q26).
- Tudo confere com a seção "Verificação" do gabarito.

## Observações (sem efeito no veredito)

- O-1. A pista mais forte entre as aceitas pela produtora é L1-Q06 (item 24) × L1C-Q25 (item 7): a premissa sobre o áudio nativo sugere o contraste com a cascata. Os dois itens estão a 17 posições de distância. A aceitação é D1 da Gerência; a alternativa reduziria o bloco 1 para 6 itens.
- O-2. Item 22 (L2-Q23): a marca [V 08/10/2026 — F3] é de verificação de fonte (padrão WebVTT). Não é VOLÁTIL. Se a Gerência preferir evitar o item, o único substituto no 2.6 é o L2-Q21, que tem errata E1(d), como a produtora registrou.
- O-3. Informação cruzada sobre o Simulado 2. Com os Lotes 2 e 3 regravados às 15:21, rodei de novo o meu `qa_sim2.py` sobre os arquivos atuais. O resultado é 40/40, sem falha, e as seções (d) e (d-G) estão idênticas a HEAD. O veredito de `simulado_2_QA_2026-10-10.md` (registrado com os hashes anteriores 2638…/76ee…) continua válido. Este arquivo apenas registra o fato; o QA do Simulado 2 não foi editado.

## Veredito por item

| nº | id | sub | gab | [TS] | enunciado = (d) | gab (grade = mapa = d-G = reg v2 = reg v3) | [TS] | justificativa = d-G | arquivo/subitem/edital | comando = canônico | elegibilidade (VOLÁTIL/REVERIFICAR/QA PENDENTE/errata/AUTORAL) | não repetido | veredito |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L1C-Q29 | 1.5 | C | não | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 2 | L1C-Q27 | 1.4 | C | sim | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 3 | L2-Q19 | 2.5 | C | não | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 4 | L3-Q15 | 3.4 | E | não | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 5 | L2-Q04 | 2.1 | C | sim | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 6 | L3-Q29 | 4.3 | E | sim | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 7 | L1C-Q25 | 1.3 | E | não | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 8 | L3-Q19 | 4.1 | C | sim | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 9 | L3-Q12 | 3.3 | C | sim | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 10 | L2-Q28 | 2.8 | C | sim | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 11 | L1-Q02 | 1.1 | E | sim | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 12 | L3-Q14 | 3.4 | E | sim | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 13 | L3-Q30 | 4.3 | C | não | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 14 | L2-Q15 | 2.4 | C | não | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 15 | L2-Q09 | 2.3 | E | sim | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 16 | L3-Q04 | 3.1 | C | sim | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 17 | L3-Q08 | 3.2 | C | sim | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 18 | L2-Q07 | 2.2 | E | não | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 19 | L1-Q15 | 1.7 | C | não | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 20 | L1-Q12 | 1.6 | E | não | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 21 | L3-Q23 | 4.2 | E | sim | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 22 | L2-Q23 | 2.6 | C | sim | ok | ok | ok | ok | ok | ok | ok (NÃO VOLÁTIL) | ok | APROVADO |
| 23 | L2-Q26 | 2.7 | E | não | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 24 | L1-Q06 | 1.3 | E | sim | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |
| 25 | L2-Q30 | 2.8 | E | não | ok | ok | ok | ok | ok | ok | ok | ok | APROVADO |

## Veredito geral

**APROVADO / CONFERIDO — 25/25 (100%); 0 REPROVADO (0%); 0 CORRIGIR.**

- Cumprido em 25/25: literalidade, comando, elegibilidade, não repetição e folha sem pistas.
- Proporção por bloco: 7 / 9 / 5 / 4, com o bloco 1 abaixo da proporção por esgotamento comprovado do conjunto elegível. A falta dos subitens 1.2 e 1.8 está registrada.
- As leituras A e B da seção (6) vão à gbq-gerencia, sem decisão deste QA.
- Nenhum gate atingido.
- Próximo passo: reconciliação pela gbq-gerencia. A entrega à candidata (PILOT_01) é reservada ao Fundador.
