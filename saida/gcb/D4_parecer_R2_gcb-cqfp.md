# D4_parecer_R2_gcb-cqfp.md — T-77 — 2026-10-20 — gerado por gcb-cqfp
PARECER R2 — LOTE D4 v2 (saida/gcb/D4_v2.md, gcb-cpp; SHA-256 71c55229fdf1fbcc5b188d1364fc99276cc9bd2a4ed07fb83ba476a698bd3eed; 313.793 bytes; LF; 2.120 linhas; gravado em 20/10/2026 às 08:33:17 −0300). Conferido contra: o R1 (saida/gcb/D4_parecer_R1_gcb-cqfp.md, f672f2c4…b01d, o mesmo citado na D1); a v1 (saida/gcb/D4_v1.md, 1cc27b31…57d4, a mesma do R1); a D1 da GCB (saida/gcb/D4_D1_GCB_v2_2026-10-20.md, 8a401185…6b3b); a leitura externa (saida/gcb/D4_leitura_critica.md, 746c6454…d6ad, gravada às 08:07:46 −0300); a ficha (saida/gcb/D4_ficha_lote.md, cb0b0c30…c7a0); e o Anexo N (saida/gcb/D4_anexo_N_mapa_normativo.md, 0d98c249…a05f), que é a única base (normas na seção 4; referencial literal na seção 5). Modelo: saida/gcb/D5_parecer_R2_gcb-cqfp.md. A gcb-cqfp revisa e não reescreve: o único texto de ajuste deste parecer é pontual e fixado. Scripts em python3 -I, no scratchpad. Navegador não usado. Sem commit.

## 0. Resultado
- **Itens: 79 (D4-01 a D4-79). APROVADO 79; AJUSTE 0; REPROVADO 0. Reprovação no R2: 0/79 = 0%** (limite do gate: 30%). Não há gate.
- 24 itens têm "QA PENDENTE (R2)" e estão todos APROVADOS:
  - 6 alterados (D4-08, D4-20, D4-44, D4-51, D4-66 e D4-69), com os textos fixados no R1, seção 2.1, e na D1-D4-03, aplicados literalmente;
  - 18 renumerados, com conteúdo idêntico ao do id de origem na v1.
  - Os outros 55 itens são idênticos à v1, campo a campo.
- A permutação aplicada é igual à tabela da D1-D4-01. As duas sequências do lote são iguais às linhas esperadas na D1. O teste da ficha 6.4 passa por folha, no caput, no item 8, no item 9 e no lote.
- Leitura externa: 6 sugestões acatadas e 34 não acatadas. Todo acatamento tem lastro literal no Decreto 9.203/2017 (Anexo N, seção 4.1), em artigo vigente. Nenhum item foi criado, e o material não copia o texto do leitor. As recusas estão justificadas.
- Blocos:
  - curso APROVADO (os 4 blocos novos também);
  - resumo APROVADO;
  - pares APROVADO (P-63 incluído);
  - pegadinhas APROVADO (G-77 a G-80 incluídas);
  - proveniência APROVADO;
  - contagens e sequência APROVADO;
  - registro de acatamento (seção 0.1) APROVADO COM 1 AJUSTE DOCUMENTAL;
  - forma: a remoção das marcas "Parte A/B" diverge da D1-D4-04. O parecer técnico está na seção 6, e a QA recomenda ratificar.
- **Veredito geral: APROVADO COM RESSALVAS.** Ressalvas:
  - (a) a GCB ratifica ou rejeita a forma (seção 6);
  - (b) há 1 ajuste residual documental, fora dos itens (seção "Ajustes residuais");
  - (c) ficam com o orquestrador as pendências que não são da v2: D1-D4-04, parte final, e D1-D4-06. Pelo cabeçalho da leitura, a D1-D4-06 cai no caso (b).
  - Nenhuma ressalva toca item, gabarito, ponto de julgamento, [TS] ou contagem.

## 1. Evidência e não regressão (por script)
1. **Itens.** Um script comparou cada item da v2 com o item de origem na v1.
   - Método: desfez a permutação por substituição simultânea, com o dicionário inverso da D1-D4-01, sobre o enunciado (5.1), o cabeçalho e cada campo (5.2). Ignorou só a marca "QA PENDENTE (R2)" e o campo "Alteração na v2".
   - Resultado: 73 itens idênticos (55 não tocados e 18 renumerados). As diferenças estão só nos 6 itens alterados e só nos campos que o R1 mandou mudar:
     - D4-08: cabeçalho (sem [TS]), enunciado, formato, gabarito, justificativa (linhas 1 e 2), mecanismo, campo Troca suprimido e marcas;
     - D4-20: enunciado, linha 2, mecanismo e troca;
     - D4-44: campo "Difere de" (novo);
     - D4-51: enunciado, linha 2 e troca;
     - D4-66: enunciado e linha 2;
     - D4-69: linha 2.
   - Em nenhum dos 79 itens mudaram folha, ponto de julgamento, tipo de base ou base.
2. **Fora dos itens.** Fiz o diff linha a linha das seções 1 a 4 e 6 (v1 × v2, com os ids desfeitos). Só aparecem alterações declaradas:
   - (a) saíram os subtítulos "### Parte A/B", os separadores "---" internos e as introduções repetidas da Parte B ("Curso folha a folha", "Uma página do item 9.", o mínimo de pares da Parte B, o cabeçalho de tabela repetido dos pares e a abertura das pegadinhas). No lugar, entrou uma introdução por seção, com as faixas de códigos;
   - (b) entraram 4 blocos de curso, o P-63 e as G-77 a G-80;
   - (c) a seção 6 passou a "Fontes do item 8" e "Fontes do item 9" e ganhou o parágrafo "Acréscimos da v2".
   - Nenhuma linha de conteúdo da v1 (curso, resumo, pares, pegadinhas e proveniência) foi alterada ou perdida.
3. **Trechos literais.** Conferi, no arquivo inteiro, os trechos com 4 palavras ou mais, cortados nos "[…]":
   - 114 entre aspas curvas;
   - 50 entre aspas retas, nas seções 1 a 6.
   - A base foi a seção 4 e a seção 5 do Anexo N, mais a linha LAI, art. 10, do Anexo N do D6. A comparação ignorou espaços e aspas.
   - **Resultado: 164/164 literais.**
4. **Citações.** Conferi as citações dos acréscimos (C9.2-07, C9.4-10 a C9.4-12, P-63, G-77 a G-80 e o parágrafo de acréscimos da seção 6) e as dos 6 itens alterados.
   - Todas as citações do Decreto 9.203/2017 existem e estão vigentes na seção 4.1: art. 3º, I a VI; art. 4º, II; art. 5º, I, a a d; art. 7º-A; art. 9º-A, II, III, § 1º, I e II, e § 2º; art. 11-A, parágrafo único, III; art. 13-A, I e II; art. 15-A, caput; art. 17, II e III; art. 19, caput e II.
   - Revogados usados como norma: 0.
   - Os dispositivos que faltam no Anexo N aparecem só na seção 0.1, para justificar recusa: Lei 13.019, arts. 24 e 29 a 31; Lei 13.460, arts. 13, 18 e 19; Lei 9.790, arts. 9º a 11; Lei 9.637, arts. 5º e 8º; Lei 11.079, art. 5º; LAI, art. 8º, §§ 2º a 4º, e art. 10, § 3º. Conferi nas seções 4.2 a 4.7 que, de fato, não estão lá.
5. **Fontes reabertas.** Em 20/10/2026, às 12:16 UTC, baixei três fontes por curl, com User-Agent de navegador:
   - N1, Decreto 9.203 (planalto.gov.br): HTTP 200 e 86.892 bytes, o mesmo tamanho do Anexo N. O SHA-256 de hoje (d69834a1…) difere outra vez: é o terceiro valor do dia com o mesmo tamanho. As 141 linhas da seção 4.1 aparecem literalmente na página de hoje (141/141). Fica só o registro, como no R1, ponto 16.
   - F6, Ipea: 79.748 bytes, SHA dc9bd7ba…, idêntico ao do Anexo N.
   - F10, CGU: 556.930 bytes, SHA fc106e48…, idêntico ao do Anexo N.
6. **Proibições nos 79 enunciados** (varredura e leitura):
   - NGP 0; "exceto" 0; [SEM FONTE] 0; "terceiro setor" 0; valor em reais 0; autor de F4 a F9 nomeado 0;
   - NPG que "substitui" ou "convive com" a NPM: 0. "Substituir" aparece só no D4-75, sobre burocracia e patrimonialismo (R1);
   - corrupção e integridade só no D4-66, literais do art. 19;
   - Porter só no D4-33 (R16);
   - REVERIFICAR 0; VOLÁTIL 0.

## 2. Conferência das respostas aos 18 pontos do R1
| Ponto R1 | Objeto | Resposta da v2 | Texto fixado entrou literal? | Veredito R2 |
|---|---|---|---|---|
| 1 | D4-08 | Acolhido | Sim: cabeçalho, enunciado, linhas 1 e 2, formato SIT, mecanismo "(C2), em situação hipotética", TS=não, sem Troca (script) | APROVADO |
| 2 | D4-20 | Acolhido | Sim: enunciado, troca "aumentar → reduzir (R13)", mecanismo E2 e linha 2 | APROVADO |
| 3 | D4-51 | Acolhido | Sim: enunciado, troca e linha 2 ("e a um de seus capítulos, como o trecho") | APROVADO |
| 4 | D4-44, "difere de BQ-0152" | Acolhido | Sim (campo literal) | APROVADO |
| 5 | D4-66, moldura | Acolhido | Sim: enunciado e linha 2 | APROVADO |
| 6 | D4-69, linha 2 | Acolhido | Sim | APROVADO |
| 7 | Contagens | Acolhido | A QA refez as contagens (seção 3). 8.2: C 6/E 4, [TS] 4, DEF 3/SUJ 1/SIT 2/NUM 2/PAR 1/APL 1. Item 8: C 21, [TS] 19. Lote: C 41, [TS] 39 | APROVADO |
| 8 | Ordem na 8.2 | Acolhido (D1-D4-01) | ECCCEEECCC / TnnnTTTnnn; maior corrida 3; maior alternância 2 | APROVADO |
| 9 | Junção e forma | Em parte: (a) a (e) feitos; (f) fica com o orquestrador (D1-D4-04) | Linhas 1 e 2 conforme a D1-D4-04 | APROVADO em (a) a (e); motivo de (f) aceito; forma na seção 6 |
| 10 | Costuras 33/34 e 73/74 | Acolhido | Permutação igual à da D1 (seção 3) | APROVADO |
| 11 | Formatos | Acolhido | Conferido (seção 3) | APROVADO |
| 12 | Remissões | Acolhido | Corretas, por script com os ids desfeitos: "Difere de", notas à GBQ, blocos à GCB e respostas às dúvidas. Os três "Difere de BQ-0121" do caput citam o id novo do próprio item | APROVADO |
| 13 | Arquivo neutro | Não acolhido: está fora da v2 (D1-D4-06) | — | Motivo aceito; pendência do orquestrador. O cabeçalho de D4_leitura_critica.md declara que o arquivo enviado foi o 505c5734…, o que põe o caso na alínea (b) da D1-D4-06: registrar o desvio na reconciliação |
| 14 | Leitura externa | Em parte: registro na seção 0.1 (D1-D4-05) | — | APROVADO COM 1 AJUSTE DOCUMENTAL (seção 5) |
| 15 | Notas à GBQ | Acolhido | As 6 notas da D1-D4-08 estão presentes, com os ids da v2. A lista da v1 foi remapeada corretamente (script) | APROVADO |
| 16 | SHA do Decreto | Acolhido como registro (seção 6 da v2) | — | APROVADO |
| 17 | R25, Capítulo 5 | Acolhido como registro. O dado não entra em curso nem em item ("Capítulo 5" só aparece nas seções 0 e 8) | — | APROVADO |
| 18 | Ordem de execução | Acolhido | — | APROVADO |

A contagem da seção 0 da v2 confere: 15 pontos acolhidos, 2 em parte (9 e 14) e 1 não acolhido (13). As respostas às dúvidas das partes usam os ids da v2 corretamente: D4-23 (era D4-22), D4-28 (era D4-29), D4-14 (era D4-11) e D4-27 (era D4-31).

## 3. Permutação, sequências e contagens (critérios 2 e 5)
- **Correspondência.** As tabelas da seção 8 e da seção 7 da v2 são idênticas à da D1-D4-01.
  - São 18 ids, e a permutação fecha dentro de cada grupo: 8.2, 8.3, 8.4 e caput. Os ids D4-34 a D4-73 ficaram inalterados.
  - Com o id novo, cada item traz o conteúdo do id antigo na v1: enunciado, gabarito, cabeçalho com ou sem [TS], troca, ponto, base e "Difere de".
  - **Gabarito e [TS] acompanham o conteúdo.**
- **Forma da seção 5.**
  - 5.1 e 5.2 estão na mesma ordem, a numérica (D4-01 a D4-79).
  - Os grupos seguem a ordem 8.1, 8.2, 8.3, 8.4, 9.1, 9.2, 9.3, 9.4 e, por último, o caput (D1-D4-02). Cada id está no grupo da sua folha.
  - Há uma só instrução "Julgue cada item como Certo ou Errado." e nenhum "Só enunciado".
  - Nos 79 itens, o [TS] do cabeçalho coincide com "TS=sim" nas marcas e com a presença do campo Troca.
- **Sequências do lote** (script próprio, sobre a ordem final):
  - Gabaritos: ECCEECECCCEEECCCECCEEECCECCEECECCCEECCECCEEECEECCECCEEECEECCECCCEECEECCECCEEECC, igual à linha da D1 (C 41; E 38).
  - [TS]: T..TT.T...TTT...T..TTT..T..TT.TT..TTT.T...TT.TT...T.TTT..T.TT...T..TT.TT..TTT.., igual à linha da D1 (39).
- **Teste da ficha 6.4** (regra da D1: corrida de 4 ou mais falha; alternância estrita acima de 4 falha; período p, de 2 a 8, por max(8, 2p) itens seguidos falha):

| Escopo | Gabaritos: corrida / alternância / maior bloco p2…p8 | [TS]: corrida / alternância / maior bloco p2…p8 | Resultado |
|---|---|---|---|
| 8.1, 8.2, 8.3, 8.4, 9.1, 9.2, 9.3, 9.4, caput | corrida ≤ 3; alternância ≤ 4; nenhum bloco no limite | corrida ≤ 3; alternância ≤ 4; nenhum bloco no limite | APROVADO |
| Item 8 (D4-01 a D4-33 e D4-74 a D4-79) | 3 / 4 / 4, 7, 7, 9, 11, 11, 15 | 3 / 4 / 4, 7, 7, 9, 11, 12, 15 | APROVADO |
| Item 9 (D4-34 a D4-73) | 3 / 3 / 3, 7, 7, 7, 8, 10, 12 | 3 / 4 / 4, 7, 7, 7, 10, 13, 13 | APROVADO |
| Lote (D4-01 a D4-79) | 3 / 4 / 4, 7, 7, 9, 11, 12, 15 | 3 / 4 / 4, 7, 7, 9, 11, 13, 15 | APROVADO |

  - Limites por período: 8, 8, 8, 10, 12, 14 e 16 itens.
  - Costuras: D4-30 a D4-37 com CECCCEEC / nTTnnTTT; D4-70 a D4-79 com CCECCEEECC / nTTnnTTTnn.
  - Tudo igual ao que a seção 7 da v2 declara.
- **Contagens** (script). São iguais às da tabela da seção 7 da v2:
  - C/E e [TS] por folha;
  - iscas D4-32, 37, 51, 60 e 71, uma por folha (8.4 e 9.1 a 9.4);
  - formatos do lote 23/5/17/7/15/12, com os tetos de 3 e 2 respeitados e APL no máximo 2 nas folhas de 10 itens e 1 nas demais;
  - tipo de base 43 DISPOSITIVO e 36 REFERENCIAL;
  - moldura do Legislativo = APL = 12;
  - E5 = 4;
  - "QA PENDENTE (R2)" = 24 (8.1: 0; 8.2: 3; 8.3: 7; 8.4: 6; 9.1: 0; 9.2: 2; 9.3: 0; 9.4: 2; caput: 4).
  - As faixas da ficha 5.1 estão cumpridas. A 8.2 chega a C 6, que é o teto.
  - A lista de pontos da seção 7 tem 79 linhas, iguais aos campos dos itens (folha, gabarito, [TS] e ponto), com 79 pontos distintos.

## 4. Os 6 itens alterados e os 18 renumerados (critério 4)
| Item | Gab. / [TS] | Objeto do R2 | Veredito |
|---|---|---|---|
| D4-08 | C / não | Reproduz R9 (alíneas a e b) em situação hipotética. "Incluir entre elas" não afirma que a lista se esgota nem que as práticas faltem à NPM, e o gabarito C é único. Sem Troca; TS=não. A 8.2 fica com SIT 2. | APROVADO |
| D4-20 | E / sim | Troca única "aumentar → reduzir", contra R13 literal. O ponto 8.3-3 e a linha 1, que não mudaram, são coerentes com a troca nova. E2. | APROVADO |
| D4-44 | E / sim | "Difere de BQ-0152" pertinente: conta os mecanismos e não julga a integridade. | APROVADO |
| D4-51 | C / isca | "Em um de seus capítulos" é verdadeiro por R25 ("neste Capítulo") e não nomeia o capítulo. A equivalência é atribuída ao TCU. A linha 1 ("no capítulo respectivo") é coerente. | APROVADO |
| D4-66 | E / não (E5) | A moldura é o art. 19, caput, literal, e "corresponde ao previsto" é verdadeiro. O único erro é que os eixos dispensariam a unidade responsável, contra o inciso II. Afirmação única. | APROVADO |
| D4-69 | E / sim | A linha 2 tem o art. 11-A, parágrafo único, III, literal (Anexo N, seção 4.1). | APROVADO |

**Renumerados (18): APROVADOS.** Em cada um, o conteúdo é idêntico ao do id de origem na v1:
- 8.2: D4-11 ← 14; D4-14 ← 11;
- 8.3: D4-17 ← 21; D4-21 ← 26; D4-22 ← 23; D4-23 ← 22; D4-25 ← 17; D4-26 ← 25;
- 8.4: D4-27 ← 31; D4-28 ← 29; D4-29 ← 28; D4-30 ← 27; D4-31 ← 33; D4-33 ← 30;
- caput: D4-74 ← 77; D4-75 ← 74; D4-77 ← 79; D4-79 ← 75.

Observação de forma, sem ajuste: o campo "Alteração na v2" tem o mesmo texto-padrão nos 18. Ele diz "troca de posição dentro da folha … (folha 8.2 e as duas costuras)". O texto é impreciso para os 4 itens do caput, que não é folha, e para os da 8.3 e da 8.4, cujo motivo é só a costura. É nota interna e não vai à edição do estudante.

## 5. Registro de acatamento da leitura externa (seção 0.1) e o que ele mudou
**5.1 Momento e completude.**
- A leitura foi gravada às 08:07:46, antes da v2 (08:33:17). Pela D1-D4-05, a seção 0.1 é preenchida na própria v2, e foi.
- As 40 sugestões (A 12, B 18, C 10) estão todas registradas. Totais: 6 acatadas e 34 não acatadas, como declarado.

**5.2 Acatadas (6: A11, B12, B13, B14, B16 e C10). APROVADAS.**
- Lastro: todas têm lastro literal em artigo vigente do Decreto 9.203/2017 (seção 4.1).
- Artigos completados: onde a sugestão citou base incompleta, o registro diz o que acrescentou: art. 9º-A, II e III no A11; alínea b no B12; inciso II no B16.
- Destino:
  - C9.2-07: o art. 5º, I, é núcleo da 9.2;
  - C9.4-10 a C9.4-12, P-63 e G-77 a G-80.
- Numeração: segue a fronteira da ficha 5.3 (item 9 com P-63 e G-77 em diante; C9.x em sequência). Há uma pegadinha por bloco: 62 blocos e 62 pegadinhas.
- Marcas: todos levam "acréscimo da v2" e "QA PENDENTE (R2)" no título ou na linha. A forma literal é "acréscimo da v2 (leitura externa …; QA PENDENTE (R2))", e as duas marcas estão presentes.
- Nenhum item foi criado.
- Mérito, conferido contra a letra:
  - C9.2-07 escolhe as alíneas b e d. Deixa de fora a alínea a, que é o ponto bloqueado do BQ-0152, e a alínea c, que coincide em parte com o princípio V ("prestação de contas e responsabilidade"). A escolha é correta.
  - C9.4-10 e C9.4-12 transcrevem os dispositivos literalmente.
  - C9.4-11 marca o "especialmente" do art. 4º, II.
  - No P-63, cada troca da coluna "como a banca troca" é falsa pela letra (arts. 7º-A, 9º-A, § 2º, e 15-A).
- Coerência entre B11 (recusada) e B12 (acatada):
  - A recusa da B11 como "já coberto" está certa: o C9.4-02 e a G-69 já trazem "acrescentar ao rol um princípio que o decreto não traz".
  - A B12 é outra confusão, entre o art. 5º, I, e o art. 3º, e não estava coberta.

**5.3 Recusas (34): justificadas.** Conferi cada motivo:
- Dispositivo que não está no Anexo N: seções 4.2 a 4.7 (seção 1, n. 4).
- Páginas do TCU e referencial de controle que não estão entre R1 e R31.
- SEM FONTE da ficha 3.4, alíneas (a) a (g), e marcos históricos.
- B10 bloqueada: a sugestão julga o âmbito do decreto quanto à Câmara, e a ficha veda as duas direções.
- Já cobertas: A8, A10, B3, B8 e B11. Os códigos de destino existem e tratam o ponto.
- C5: a página citada (237) não é a de R11 (236).
- A1 e C2: TD 2319 do Ipea não aberto (Anexo N, seção 6.1).

**5.4 Cópia do texto do leitor.** Um script mediu o maior trecho comum, em palavras, entre cada acréscimo e a sugestão de origem:
- O maior trecho que não é letra da lei tem 7 palavras: "irrelevantes para os comitês internos de governança", no C9.4-10 e na G-78.
- A razão de semelhança é de no máximo 0,39.
- O maior trecho comum de todos (13 palavras) é letra do art. 9º-A, § 2º.
- É paráfrase aceitável. Compare com o precedente D5, G-68: 0,85 de razão e 12 palavras fora da lei.
- Na coluna "Texto curto" da 0.1, os rótulos repetem até 8 palavras do leitor (por exemplo, B4 e B16). Os rótulos só identificam a sugestão e não entram no material. Mesmo assim, a frase "nenhum trecho do arquivo de leitura foi copiado" fica inexata para essa coluna. Ajuste residual 1.

**5.5 Arquivo entregue ao leitor.** Era o 505c5734… e foi gerado sobre a v1. Os acréscimos não estão nele, e a v2 registra isso (seção 8, pendente (e)). Não há regeração a fazer, salvo nova rodada de leitura.

## 6. Forma: remoção das marcas "Parte A/B" contra a D1-D4-04 — parecer técnico para a GCB
1. **Fato.**
   - A D1-D4-04 mandou manter "### Parte A" e "### Parte B" nas seções 1 a 4 e 6 a 8, "porque as faixas de códigos (C8.x/C9.x, P-01/P-51, G-01/G-51) dependem deles".
   - A v2 removeu esses 14 subtítulos. A produtora declara ter seguido "a ordem desta tarefa" (seção 0, ponto 9; seção 8, pendente (a)). Essa ordem não está no repositório: não há arquivo em ordens/ nem em lotes/loteD4/ para a v2. A QA não conferiu o texto dela.
   - A divergência foi declarada pela própria produção, que é o procedimento correto.
2. **Perda de conteúdo: nenhuma** (seção 1, n. 2). Saíram só subtítulos, separadores e introduções repetidas.
3. **As faixas de códigos ficaram preservadas e conferíveis.** Estão em seis lugares:
   - nas convenções (linha 6);
   - na introdução do curso (C8.0 a C8.4 para o item 8; C9.1 a C9.4 para o item 9);
   - nas introduções dos pares e das pegadinhas;
   - na seção 6 ("Fontes do item 8" e "Fontes do item 9");
   - na seção 7 ("Item 8 (antiga Parte A)" e "Item 9 (antiga Parte B)");
   - nas notas da seção 8.
   Os códigos novos seguem a fronteira da ficha 5.3. Este R2 conferiu tudo sem precisar dos subtítulos.
4. **Equivalência exata.** "Item 8" corresponde à antiga Parte A, e "item 9" à antiga Parte B. São as mesmas folhas, os mesmos ids (D4-01 a D4-33 e D4-74 a D4-79; D4-34 a D4-73) e as mesmas faixas. O rótulo novo é o do edital, e não o da organização da produção.
5. **Ganhos.**
   - Neutralidade: "Parte A/B" está na lista de aborto da ficha 9.2, e o R1, ponto 13, registrou o vazamento. Com o termo fora da fonte, a próxima regeração do arquivo de leitura tem menos risco.
   - Scripts: nenhum depende dos subtítulos. O scripts_orq/leitura_critica_gen.py só filtra essas linhas, e o juntar_partes.py não se aplica à v2, que é arquivo único.
   - Coerência com o D5 v2, também em arquivo único.
6. **Custo.** A ficha 5.3, o R1 e a D1 falam em Parte A/B. A seção 7 da v2 dá a equivalência, e isso basta.
7. **Recomendação técnica.**
   - Ratificar a forma da v2 por errata à D1-D4-04, na reconciliação. Sugestão de texto: "na v2, os subtítulos de parte são substituídos por 'item 8' e 'item 9', com as faixas de códigos nas introduções das seções". Nenhum item é reaberto.
   - Se a GCB preferir a letra da D1, a reinserção dos 14 subtítulos é mecânica. Nesse caso, a QA confere só o diff, sem efeito em item.
   - Não há gate. A divergência é de forma e opõe uma ordem do orquestrador a uma D1 vigente; não é conflito entre Gerências. Cabe à GCB registrá-la. Cabe ao orquestrador não dar ordem de produção contrária a uma D1 vigente sem passar pela GCB.

## 7. Observações sem efeito no veredito
1. **O marcador de moldura coincide com o gabarito** (estilo_banca, 5.1: "Não deixe o marcador coincidir sempre com o mesmo gabarito").
   - As 5 molduras de "acerto" ("a afirmação do expositor é correta" ou "ele estará correto ao") são todas C: D4-02, D4-03, D4-08, D4-32 e D4-79.
   - Os 4 enunciados que nomeiam o "pós-NPM" são todos C: D4-03, D4-06, D4-08 e D4-18.
   - Dos 29 enunciados que abrem com "Considere que", 21 são C (72%), contra 52% no lote.
   - Na v1, essas contagens eram 4/4 (molduras de acerto), 3/3 (pós-NPM) e 20/28 ("Considere que"). A conversão do D4-08, com texto fixado por esta QA no R1, somou um caso a cada grupo.
   - Não reprovo nada: cada item está correto, e a conversão eliminou um E por ausência.
   - Recomendação: seguir as notas à GBQ da seção 9 e, no reforço (T-100), preferir itens E com moldura de expositor ou analista e com "pós-NPM", trocando um elemento literal de R4, R8, R9 ou R12.
2. **Seção 6 da v2.** A introdução geral é seguida do parágrafo da v1 sobre o item 8, quase igual. Há também linhas em branco duplas, na seção 6 e no início da seção 2. É questão de forma, sem ajuste.

## 8. Tabela final dos 79 itens (ordem de apresentação)
| Item | Folha | Ponto | Gab. | [TS] | Marca | Veredito R2 | Observação |
|---|---|---|---|---|---|---|---|
| D4-01 | 8.1 | 8.1-1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-02 | 8.1 | 8.1-2 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-03 | 8.1 | 8.1-6 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-04 | 8.1 | 8.1-4 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-05 | 8.1 | 8.1-3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-06 | 8.1 | 8.1-5 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-07 | 8.2 | 8.2-10 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-08 | 8.2 | 8.2-2 | C | não | QA PENDENTE (R2) | APROVADO | ajuste 1 do R1 aplicado literalmente: E → C, sem [TS], SIT, C2; texto da D1-D4-03 |
| D4-09 | 8.2 | 8.2-6 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-10 | 8.2 | 8.2-3 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-11 | 8.2 | 8.2-11 | E | sim | QA PENDENTE (R2) | APROVADO | renumerado (era D4-14); conteúdo idêntico ao D4-14 da v1 (script) |
| D4-12 | 8.2 | 8.2-5 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-13 | 8.2 | 8.2-8 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-14 | 8.2 | 8.2-1 | C | não | QA PENDENTE (R2) | APROVADO | renumerado (era D4-11); conteúdo idêntico ao D4-11 da v1 (script) |
| D4-15 | 8.2 | 8.2-13 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-16 | 8.2 | 8.2-14 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-17 | 8.3 | 8.3-6 | E | sim | QA PENDENTE (R2) | APROVADO | renumerado (era D4-21); conteúdo idêntico ao D4-21 da v1 (script) |
| D4-18 | 8.3 | 8.3-2 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-19 | 8.3 | 8.3-4 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-20 | 8.3 | 8.3-3 | E | sim | QA PENDENTE (R2) | APROVADO | ajuste 2 aplicado literalmente: troca "aumentar → reduzir (R13)", E2; E por ausência eliminado |
| D4-21 | 8.3 | 8.3-11 | E | sim | QA PENDENTE (R2) | APROVADO | renumerado (era D4-26); conteúdo idêntico ao D4-26 da v1 (script) |
| D4-22 | 8.3 | 8.3-5 | E | sim | QA PENDENTE (R2) | APROVADO | renumerado (era D4-23); conteúdo idêntico ao D4-23 da v1 (script) |
| D4-23 | 8.3 | 8.3-7 | C | não | QA PENDENTE (R2) | APROVADO | renumerado (era D4-22); conteúdo idêntico ao D4-22 da v1 (script) |
| D4-24 | 8.3 | 8.3-8 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-25 | 8.3 | 8.3-1 | E | sim | QA PENDENTE (R2) | APROVADO | renumerado (era D4-17); conteúdo idêntico ao D4-17 da v1 (script) |
| D4-26 | 8.3 | 8.3-9 | C | não | QA PENDENTE (R2) | APROVADO | renumerado (era D4-25); conteúdo idêntico ao D4-25 da v1 (script) |
| D4-27 | 8.4 | 8.4-3 | C | não | QA PENDENTE (R2) | APROVADO | renumerado (era D4-31); conteúdo idêntico ao D4-31 da v1 (script) |
| D4-28 | 8.4 | 8.4-7 | E | sim | QA PENDENTE (R2) | APROVADO | renumerado (era D4-29); conteúdo idêntico ao D4-29 da v1 (script) |
| D4-29 | 8.4 | 8.4-2 | E | sim | QA PENDENTE (R2) | APROVADO | renumerado (era D4-28); conteúdo idêntico ao D4-28 da v1 (script) |
| D4-30 | 8.4 | 8.4-1 | C | não | QA PENDENTE (R2) | APROVADO | renumerado (era D4-27); conteúdo idêntico ao D4-27 da v1 (script) |
| D4-31 | 8.4 | 8.4-5 | E | sim | QA PENDENTE (R2) | APROVADO | renumerado (era D4-33); conteúdo idêntico ao D4-33 da v1 (script) |
| D4-32 | 8.4 | 8.4-6 | C | isca | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-33 | 8.4 | 8.4-4 | C | não | QA PENDENTE (R2) | APROVADO | renumerado (era D4-30); conteúdo idêntico ao D4-30 da v1 (script) |
| D4-34 | 9.1 | 9.1-4 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-35 | 9.1 | 9.1-1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-36 | 9.1 | 9.1-5 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-37 | 9.1 | 9.1-2 | C | isca | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-38 | 9.1 | 9.1-6 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-39 | 9.1 | 9.1-7 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-40 | 9.1 | 9.1-9 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-41 | 9.1 | 9.1-10 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-42 | 9.1 | 9.1-3 | E | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-43 | 9.1 | 9.1-11 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-44 | 9.2 | 9.2-1 | E | sim | QA PENDENTE (R2) | APROVADO | ajuste 4 aplicado literalmente: "Difere de: BQ-0152" |
| D4-45 | 9.2 | 9.2-2 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-46 | 9.2 | 9.2-5 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-47 | 9.2 | 9.2-9 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-48 | 9.2 | 9.2-3 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-49 | 9.2 | 9.2-4 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-50 | 9.2 | 9.2-12 | E | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-51 | 9.2 | 9.2-7 | C | isca | QA PENDENTE (R2) | APROVADO | ajuste 3 aplicado literalmente: "em um de seus capítulos"; isca literal de R25 |
| D4-52 | 9.2 | 9.2-11 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-53 | 9.2 | 9.2-10 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-54 | 9.3 | 9.3-1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-55 | 9.3 | 9.3-5 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-56 | 9.3 | 9.3-4 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-57 | 9.3 | 9.3-3 | E | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-58 | 9.3 | 9.3-8 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-59 | 9.3 | 9.3-7 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-60 | 9.3 | 9.3-2 | C | isca | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-61 | 9.3 | 9.3-9 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-62 | 9.3 | 9.3-10 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-63 | 9.3 | 9.3-11 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-64 | 9.4 | 9.4-1 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-65 | 9.4 | 9.4-3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-66 | 9.4 | 9.4-17 | E | não | QA PENDENTE (R2) | APROVADO | ajuste 5 aplicado literalmente: moldura = art. 19, caput, literal; um só segmento falso (inciso II) |
| D4-67 | 9.4 | 9.4-4 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-68 | 9.4 | 9.4-5 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-69 | 9.4 | 9.4-7 | E | sim | QA PENDENTE (R2) | APROVADO | ajuste 6 aplicado literalmente: linha 2 com o art. 11-A, parágrafo único, III |
| D4-70 | 9.4 | 9.4-13 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-71 | 9.4 | 9.4-8 | C | isca | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-72 | 9.4 | 9.4-10 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-73 | 9.4 | 9.4-15 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-74 | caput 8 | c8-5 | C | não | QA PENDENTE (R2) | APROVADO | renumerado (era D4-77); conteúdo idêntico ao D4-77 da v1 (script) |
| D4-75 | caput 8 | c8-1 | E | sim | QA PENDENTE (R2) | APROVADO | renumerado (era D4-74); conteúdo idêntico ao D4-74 da v1 (script) |
| D4-76 | caput 8 | c8-3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-77 | caput 8 | c8-6 | E | sim | QA PENDENTE (R2) | APROVADO | renumerado (era D4-79); conteúdo idêntico ao D4-79 da v1 (script) |
| D4-78 | caput 8 | c8-4 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D4-79 | caput 8 | c8-2 | C | não | QA PENDENTE (R2) | APROVADO | renumerado (era D4-75); conteúdo idêntico ao D4-75 da v1 (script) |
Resumo da tabela: 79 APROVADOS. São 55 idênticos à v1, 6 com o texto fixado do R1 aplicado literalmente e 18 renumerados com conteúdo idêntico. Reprovação: 0/79 = 0%.

## Ajustes residuais (texto exato)
1. **Seção 0.1, parágrafo de critério** (documental; fora dos itens; não reprova nada).
   - Trecho atual (ocorre uma única vez no D4_v2.md): A coluna "Texto curto" é redação própria: nenhum trecho do arquivo de leitura foi copiado.
   - Texto novo: A coluna "Texto curto" só identifica a sugestão e pode repetir termos do leitor; no curso, nos pares e nas pegadinhas, o texto é próprio ou é letra do decreto, sem cópia do arquivo de leitura.

O ajuste pode entrar por errata na reconciliação. A QA confere só esse trecho (diff), sem nova rodada sobre os itens.

## 9. Veredito final
Lote D4 v2: **APROVADO COM RESSALVAS no R2.** São 79/79 itens aprovados, com reprovação de 0%. Não há gate.

Pela QA, o lote pode seguir à reconciliação da gcb-gerencia, com estas condições:
- decidir a forma (seção 6). A recomendação é ratificar a remoção das marcas "Parte A/B" por errata à D1-D4-04;
- aplicar ou registrar por errata o ajuste residual 1;
- registrar na reconciliação as pendências do orquestrador:
  - D1-D4-06, caso (b): o arquivo neutro entregue foi o 505c5734…, sem "NEUTRO CONFERIDO";
  - D1-D4-04, parte final: corrigir o juntar_partes.py antes do D2 e do D3;
  - registro em DECISOES.md dos desvios da ficha 9.4 e da forma em arquivo único.

Notas à GBQ, para simulado:
- Mantidas as notas da seção 8 da v2, com a lista da v1 remapeada e as 6 da D1-D4-08.
- Acréscimos da QA:
  - {D4-03, D4-06, D4-08, D4-18}: os quatro tratam do pós-NPM e são todos C. No máximo um por simulado;
  - {D4-02, D4-03, D4-08, D4-32, D4-79}: moldura de "acerto", todos C. No máximo um por simulado, ou ao lado de item E com a mesma moldura, de outro lote.

Todo item segue "QA PENDENTE" no registro até o gatilho A aceito (D-QA-PENDENTE). Nada vai à plataforma nem à candidata.

GATE: não acionado (reprovação 0/79 = 0%, limite 30%).

FIM DO PARECER R2 — LOTE D4
