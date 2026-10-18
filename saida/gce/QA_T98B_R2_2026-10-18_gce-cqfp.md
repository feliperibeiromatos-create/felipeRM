# QA_T98B_R2_2026-10-18_gce-cqfp.md — T-98 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L3_reforco_onda4_B_v2.md (gce-cpp; 28 itens AUTORAL, L3-R40 a L3-R67, P2-3.3 e P2-3.4). Esta é a R2, a última rodada da parte B da T-98. Revisão: aponto onde e por quê, sem reescrever. Não houve commit nem push.

Lido: QA_T98B_R1_2026-10-18_gce-cqfp.md; QA_T98B_normativo_2026-10-18_qa-normativo.md (3/3 CONFERE, art. 97, §§ 1º a 3º); a v2 (com a resposta item a item no topo); a v1, para o diff; e, em DECISOES.md, D-REFORCO-2, D-ADERENCIA e D-T97-META-FUNDADOR-RESP.

## 0. Resultado

- REPROVADO: 0. AJUSTAR: 0. APROVADO: 28 (3 com ressalva de registro ou de estilo, sem efeito no gabarito).
- Taxa de reprovação: 0/28 = 0%. Não aprovados: 0/28. O gate de 30% não foi acionado.
- PENDENTE NORMATIVO: nenhum. R51 a R53 foram conferidos pelo qa-normativo (CONFERE). O R50 novo (RICD, art. 98, § 5º) foi conferido literalmente por esta QA no Legin, hoje (seção 3). Ele não passou pelo qa-normativo, mas a base é norma da Câmara no Legin, que é a base admitida (T91_reconciliacao, seção 2). Ainda assim, registro para a Gerência o pedido de que o qa-normativo o confira antes do gatilho A, se a regra 6 do checklist for lida como exigência estrita.
- Veredito geral da parte B: APROVADO COM RESSALVAS (ressalvas de registro e de estilo, seção 5).

## 1. Diff v1 → v2 (diff completo, 170 linhas, conferido)

Mudou só o que está abaixo. Nenhum outro enunciado, gabarito, [TS] ou base mudou.

- Linha 1 (nome do arquivo); topo (tabela de resposta e parágrafo de abertura com as contagens novas).
- Mapa: R42 SH→PC; R50 linha nova inteira; R53 direta→parcial; R59 n→VOLÁTIL baixo (hipótese c); R64 NP→PC e direta→parcial; R65 SH→PC.
- Seções 1.3 a 1.5: pontos evitados (+L1-R54), conferência de gêmeo do R50 novo, vizinhanças, registros 1, 3, 5 e 6, e tabelas de formato, VOLÁTIL e aderência recalculadas.
- Parte 2: enunciado do R50 substituído, e o enunciado do R62 com a supressão.
- Parte 3: R42 (nota PC); R50 reescrito; R53 (PARCIAL); R59 (VOLÁTIL); R62 (nota na base); R64 (PC e PARCIAL); R65 (nota PC).
- Contagens e tabela de proveniência: a linha do Google "Audio understanding" saiu, e o Legin passou a servir a R50 a R53.

## 2. Ajustes e reclassificações (texto exato)

| ponto da R1 | conferência na v2 | veredito |
|---|---|---|
| R50 REPROVADO (gêmeo do L1-R54) | O item foi substituído, com mesmo id e mesma folha. O ponto antigo foi listado entre os pontos evitados. | conferido (o item novo está na seção 3) |
| R59 VOLÁTIL baixo (c) | O mapa traz "VOLÁTIL baixo (hipótese c)". O (d-G) traz "E [TS]. VOLÁTIL (baixo). REVERIFICAR", com o motivo da hipótese (c). O enunciado não mudou. A 3.4 fica com 3/20 = 15%, nenhum de risco alto. | conferido |
| R62: suprimir ", e não em um corpus multilíngue" | A Parte 2 termina exatamente em "…um grande corpus de língua portuguesa.". O gabarito C e o [TS] espelho foram mantidos. A nota do link markdown está na base. | conferido |
| R53 e R64 PARCIAIS | Mapa e (d-G) com "parcial" e "só simulado diagnóstico" (D-ADERENCIA). A 3.3 fica com 18/20 diretos (PARCIAIS: R05 e R53), e a 3.4 com 19/20 (PARCIAL: R64). O piso de 10 está cumprido (D-T97-META-FUNDADOR-RESP). | conferido |
| R42, R64 e R65 em PC | Mapa e notas no (d-G). Na 3.3, PC = Q10, R41, R42, R44 e R53 = 5/20. Na 3.4, PC = Q14, R58, R61, R64, R65 e R66 = 6/20 = 30%, exatamente no teto. A soma por formato dá 20 nas duas folhas. | conferido; a 3.4 não admite mais PC |
| R51 a R53 PENDENTE NORMATIVO | Marca retirada após o parecer 3/3 CONFERE. O REVERIFICAR foi mantido, e a baixa fica com a Gerência, como diz o parecer. | conferido |

## 3. Pontos não acatados

- Concessivas de R47, R59 e R60, sem contraste: aceito a posição. A R1 já as classificou como questão de estilo, com texto opcional e sem efeito no gabarito, e as remeteu ao gbq-estilo. Continuam registradas para a amostra da onda 4.
- Reposição com C em vez de E: aceito a posição. A aritmética da produtora está certa e corrige a R1. Sem o R50 antigo (C), a 3.3 ficaria com 9 C / 10 E. Só um C devolve a folha a 10/10, e um E a levaria a 9/11 (45% de C, ainda na faixa). A sugestão "preferência por E" da R1 foi erro desta QA.

## 4. L3-R50 novo, por inteiro: APROVADO (ressalva de estilo)

- **Enunciado (52 palavras):** "Uma minuta de ata gerada automaticamente inclui o inteiro teor de um documento oficial de caráter reservado, enviado à Câmara dos Deputados a pedido de uma Comissão. Segundo o Regimento Interno da Câmara dos Deputados, essa inclusão é indevida, porque não se dará publicidade a informações e documentos oficiais de caráter reservado."
- **Base literal:** reabri o Legin hoje, 18/10/2026, no texto atualizado da Resolução nº 17/1989 (www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html). A resposta veio com HTTP 200 e 1.007.742 bytes. Extraí o texto por script (python3 -I).
  - § 5º, literal: "Não se dará publicidade a informações e documentos oficiais de caráter reservado. As informações solicitadas por Comissão serão confiadas ao Presidente desta pelo Presidente da Câmara para que as leia a seus pares; […] serão fechadas em invólucro lacrado, etiquetado, datado e rubricado por dois Secretários, e assim arquivadas."
  - O § 5º não traz marca de redação dada ou de inclusão (redação original).
  - O trecho citado na base do (d-G) confere byte a byte. O contraste com o § 4º ("serão, em regra, publicadas na ata impressa, antes de entregues, em cópia autêntica, ao solicitante") também confere.
  - O caput do art. 98 (publicação da ata no Diário) sustenta a ligação entre ata e publicidade.
- **Gabarito C:** correto. O enunciado reproduz a primeira parte do § 5º. O cenário (documento enviado a pedido de Comissão) é justamente o caso em que o § 4º daria a regra geral de publicação e o § 5º a afasta.
- **[TS] espelho:** a versão E levaria o § 4º ao documento reservado. É a troca de um conceito só, declarada na justificativa, e segue a convenção espelho já aceita.
- **Aderência DIRETA:** confirmada. O ponto é o conteúdo da própria ata que se publica, e o cenário é a revisão de uma minuta gerada automaticamente. Segue o critério da T97_reconciliacao, seção 3.4, e o precedente L3-R06.
- **Não VOLÁTIL:** é norma. O REVERIFICAR fica para a janela de 4 a 8/1/2027.
- **Formato SH:** procede. O cenário pesa no juízo ("essa inclusão é indevida").
- **Ponto e frase-base sem gêmeo.** Grep próprio:
  - "caráter reservado", "se dará publicidade", "invólucro" e "98, § 5" no pacote.json v1.10 e em todos os arquivos saida/gce/*reforco*, inclusive L3_reforco_onda4_A_v1.md e C_v1.md: zero ocorrências fora da própria parte B. A parte D não existe em disco.
  - As ocorrências de "reservad*" são de "reuniões reservadas" (L1 onda 2 B e D; L2 onda 3 B: diarização local, model card do Whisper, ocultação de PII), com outros pontos.
  - O art. 98 já usado no pacote e nas ondas cobre caput e §§ 1º, 2º, 3º, 6º e 7º. O § 5º é inédito.
  - Há vizinhança declarada com L2-R52 e com o § 3º (L2 onda 3 B), com pontos distintos.
- **Ressalva de estilo, sem efeito no gabarito:**
  - (a) R50 e R51 abrem com a mesma moldura ("minuta de ata gerada automaticamente"). Convém que não figurem no mesmo simulado; fica para o gbq-estilo.
  - (b) Um recorrente poderia alegar que a minuta ainda não é publicada. O juízo, porém, é sobre incluir o documento na ata que se publica (art. 98, caput), e a justificativa diz isso. Não vejo ambiguidade que a banca anularia.

## 5. Estrutura e contagens (script próprio)

- Parte 2 sem marcas. Em todos os itens, "Julgue o item." e "FIM DO LOTE" estão presentes.
- Gabarito: 14 C / 14 E = 50,0%. Por folha: 3.3 com 10 C / 10 E e 3.4 com 11 C / 9 E.
- [TS]: 25 de 28 (14 em E e 11 em C, espelho; o R50 novo entrou).
- VOLÁTIL: 3.3 com 0/20; 3.4 com 3/20 (R56, R59, R65), nenhum de risco alto.
- Formato máximo: 3.3 com 5/20 (PC); 3.4 com 6/20 (PC, no teto).
- Ressalvas que permanecem:
  - concessivas de R47, R59 e R60;
  - moldura repetida em R50 e R51;
  - concentração de bases da R1, seção 4, item 4, para a conferência em bloco em janeiro (T-11, P2: 28 bases; VOLÁTEIS R56, R59 e R65).

## 6. Tabela final (28 itens)

| id | veredito | | id | veredito |
|---|---|---|---|---|
| L3-R40 | APROVADO | | L3-R54 | APROVADO |
| L3-R41 | APROVADO | | L3-R55 | APROVADO |
| L3-R42 | APROVADO (PC) | | L3-R56 | APROVADO |
| L3-R43 | APROVADO | | L3-R57 | APROVADO |
| L3-R44 | APROVADO | | L3-R58 | APROVADO |
| L3-R45 | APROVADO | | L3-R59 | APROVADO (ajuste conferido; estilo) |
| L3-R46 | APROVADO | | L3-R60 | APROVADO (estilo) |
| L3-R47 | APROVADO (estilo) | | L3-R61 | APROVADO |
| L3-R48 | APROVADO | | L3-R62 | APROVADO (ajuste conferido) |
| L3-R49 | APROVADO | | L3-R63 | APROVADO |
| L3-R50 (novo) | APROVADO (estilo: moldura igual à do R51) | | L3-R64 | APROVADO (PC; PARCIAL) |
| L3-R51 | APROVADO | | L3-R65 | APROVADO (PC) |
| L3-R52 | APROVADO | | L3-R66 | APROVADO |
| L3-R53 | APROVADO (PARCIAL) | | L3-R67 | APROVADO |

Reprovados: 0/28 = 0%. Veredito geral: APROVADO COM RESSALVAS.
