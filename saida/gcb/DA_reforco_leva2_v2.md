# DA_reforco_leva2_v2.md — T-116 — 2026-10-20 — gerado por gcb-cpp

## Resposta à R1

Parecer respondido: saida/gcb/QA_DA_reforco_leva2_R1_2026-10-20_gcb-cqfp.md (R1 sobre a v1, 30 itens, ciclo s15c4). Resposta item a item, antes do texto corrigido. Entradas conferidas em disco (SHA-256, 20/10/2026): DA_reforco_leva2_v1.md 40f2288a…ee788 (igual ao do parecer, seção 1); ficha 77f2e60a…5639; adendo do D1 cb4d02f9…73f9. Método (python3 -I, somente leitura das entradas): a v2 é a v1 com (a) os AJ-1 a AJ-11 por substituição exata, cada “substituir” com 1 ocorrência na v1 e o “por” com 0 antes da aplicação; (b) o D1-R03 trocado pelo D1-R13; (c) o cabeçalho e as seções 0, 3.2, 4, 5 e 6 atualizados e as contagens da seção 4 refeitas sobre este arquivo gravado. Os 22 blocos APROVADO (e seus enunciados) são idênticos aos da v1, e os 7 blocos AJUSTAR diferem da v1 só pelo texto dos AJ (comparação por script). Nada foi gravado na leva 1; sem commit nem push; nenhuma leitura externa.

**R.1 Resultado do R1 (parecer, seção 0).** APROVADO 22; AJUSTAR 7 (D1-R01, D1-R04, D1-R05, D1-R09, D3-R15, D3-R19, D3-R20; 11 AJ); REPROVADO 1 (D1-R03). Taxa de reprovação 1/30 = 3,3% (limite 30%): sem gate. Resposta: os 22 ficam como estavam; os 11 AJ foram aplicados (R.2); o D1-R03 foi substituído pelo D1-R13 (R.3).

**R.2 Os 11 AJ (seção 4 do parecer).** Cada um aplicado por substituição exata, com o texto do parecer, sem outra mudança no item.

| AJ | item | campo | v2 |
|---|---|---|---|
| AJ-1 | D1-R01 | enunciado | aplicado: «se um parecer obrigatório e não vinculante deixar de ser emitido no prazo fixado, subsiste a responsabilidade de quem se omitiu no atendimento.» (retira a premissa que entregava o gabarito do D1-56) |
| AJ-2 | D1-R04 | enunciado | aplicado: cenário «ao emitir opinião técnica, tenha dado causa a dano» (ancora a pertinência à 2.2 no art. 12, caput; segue para o R2 como item da amostra da gbq-estilo) |
| AJ-3 | D1-R05 | enunciado | aplicado: «… até que o órgão omisso apresente o laudo.» |
| AJ-4 | D1-R05 | Troca | aplicado: «→ o processo não terá seguimento até que o órgão omisso apresente o laudo (art. 43 × art. 42, § 1º)» (a linha “Ponto de julgamento” do bloco, que é resumo, não está no AJ e ficou como na v1) |
| AJ-5 | D1-R09 | enunciado | aplicado: cenário «ao emitir opinião técnica, tenha dado causa a dano ao erário de montante expressivo» |
| AJ-6 | D3-R15 | enunciado | aplicado: «o ato ilícito configura-se ainda que o dano causado a outrem seja exclusivamente moral.» (concessiva da letra no lugar de “pode configurar”) |
| AJ-7 | D3-R15 | Justificativa (linha 2) | aplicado: «… sem afirmar que ela basta;» |
| AJ-8 | D3-R19 | enunciado | aplicado: servidor como vítima («tenha sofrido dano causado por particular e pretenda ser indenizado») e «gravidade da culpa do particular»; mesma moldura S, mesmo tipo, mesmo gabarito e fórmula “Nessa situação, nos termos d…” |
| AJ-9 | D3-R19 | Troca | aplicado: «extensão do dano → gravidade da culpa do particular (art. 944, caput)» |
| AJ-10 | D3-R20 | enunciado | aplicado: «… agindo com culpa no exercício de suas atribuições, tenha causado dano a terceiros.» |
| AJ-11 | D3-R20 | Justificativa (linha 2) | aplicado: «a tentação é inverter os polos da ação regressiva, como se o servidor a movesse contra a Fazenda Pública.» |

Efeito: nenhum AJ muda gabarito, [TS], formato, moldura (S/N e tipo), aderência ou abertura (parecer, fim da seção 4); as contagens da seção 4 que dependem desses campos ficam iguais às da v1.

**R.3 REPROVADO: D1-R03 → D1-R13 (seção 3 do parecer).** Motivo aceito: gêmeo do canônico D1-55 da mesma folha (regra 2 da seção 1 da ficha). O id D1-R03 não é reutilizado; o substituto é o **D1-R13**, na posição 3 da 2.2, E com [TS] e abertura declarativa, de modo que os testes de sequência ficam intactos (gabarito CCEEECECCEEC e [TS] nnTTTnTnnTTn da 2.2).
- Ponto escolhido: **A2.2-09** (Decreto 9.830, art. 12, § 2º), E por inversão de polaridade da exigência de comprovação nos autos (E2), formato DEF, sem moldura.
- Por que não um ponto fora do Decreto 9.830: a reserva da ficha (8.3.4) para a 2.2 tem A2.2-09, 11, 14 e 15 e A2.2-06 (todos do Decreto 9.830), A2.2-19, 21 e 22 (Lei 14.133) e A2.2-05 (LINDB). Fora do Decreto, nenhum é viável: A2.2-19, 21 e 22 levariam a Lei 14.133 a 5 itens na folha, acima do teto de 4 fixado pela GCB na mesma seção 8.2, item 5 (e o art. 10 a 3 itens, ou o art. 53 a 2), isto é, trocariam um estouro de teto por outro; o A2.2-05 é gêmeo do D1-57 (mesmo critério que reprovou o D1-R03; o parecer não o recomenda). Aplica-se então o fallback: A2.2-09, o indicado pela QA, e a **extrapolação do teto do Decreto 9.830 (6 itens, contra 5) fica registrada como pendência para a GCB** (seção 6.4, item 1), com as alternativas.
- Conferências do substituto: não gêmeo de canônico (nenhum canônico do lote cita o Decreto 9.830; D1-57 e D1-58 julgam a LINDB) nem da leva (D1-R04 julga o § 3º, nexo de causalidade; D1-R09, o § 5º; D1-R02, o § 1º; D1-R08, o § 6º; D1-R10, o art. 17); ponto único na folha; troca única e literal (a letra diz que não será configurado se não restar comprovada a situação ou circunstância fática; o item diz que se configura ainda que não reste comprovada); sem pista de forma (sem “Considere que”, sem absoluto, sem “pode”; o “não” é conteúdo do dispositivo); sem moldura do Legislativo e sem afirmar o alcance do Decreto (P3); trecho de 24 palavras, subcadeia do adendo e da cópia; “Difere de: D1-R04” e nota “não pôr no mesmo simulado” D1-R13 × D1-R04 (parecer, seção 8, item 2).

**R.4 Os 22 APROVADO (seção 2 do parecer): mantidos, sem alteração.**

| item | folha | resposta |
|---|---|---|
| D4-R19 | 8.4 | mantido; fecha a corrida E E E da 8.4 acumulada (seção 4.3) |
| D4-R20 | 8.4 | mantido (amostra da gbq-estilo) |
| D4-R21 | 8.4 | mantido |
| D4-R22 | 8.4 | mantido (desvio 6.2.3 aceito) |
| D4-R23 | 8.4 | mantido |
| D4-R24 | 8.4 | mantido |
| D4-R25 | 8.4 | mantido |
| D4-R26 | 8.4 | mantido; observação da QA (construção mais próxima de DEF que de SUJ; reclassificar não muda teto) registrada na pendência 6.4, item 5, sem mudança de formato |
| D4-R27 | 8.4 | mantido (nota (u) da ficha) |
| D4-R28 | 8.4 | mantido |
| D1-R02 | 2.2 | mantido |
| D1-R06 | 2.2 | mantido |
| D1-R07 | 2.2 | mantido |
| D1-R08 | 2.2 | mantido |
| D1-R10 | 2.2 | mantido |
| D1-R11 | 2.2 | mantido; registro do desvio não declarado (“controle posterior de legalidade”) na pendência 6.4, item 5 |
| D1-R12 | 2.2 | mantido; registro da pertinência (o art. 72, III, não trata de responsabilidade) na pendência 6.4, item 5 |
| D3-R14 | 6.4 | mantido |
| D3-R16 | 6.4 | mantido (nota (k)) |
| D3-R17 | 6.4 | mantido |
| D3-R18 | 6.4 | mantido (pertinência parcial aceita; amostra da gbq-estilo) |
| D3-R21 | 6.4 | mantido |

**R.5 Desvios de redação declarados na v1 (seção 7 do parecer).** (1) D3-R15 “pode configurar”: não aceito; resolvido pelos AJ-6 e AJ-7 (o desvio deixa de existir). (2) D1-R04, cenário sem a exceção do § 3º: aceito; com o AJ-2 o cenário ancora-se na opinião técnica. (3) D4-R22 sem a ressalva do Decreto 9.203: aceito, sem mudança. (4) D1-R05, laudo × parecer: aceito com ajuste; AJ-3 e AJ-4 aplicados. (5) Dois trechos com “[…]” em 7 itens: aceito, sem mudança. (6) Mecanismo escolhido pela produção: aceito; o D1-R13 é E2 (o D1-R03 era E3). (7) Não declarado, D1-R11 “controle posterior”: aceito com registro; mantido.

**R.6 Lista para a v2 (seção 8 do parecer).** (1) AJ-1 a AJ-11 por substituição exata: feito (R.2). (2) D1-R03 → D1-R13 na posição 3, E, [TS], declarativo, bloco completo, “Difere de” do D1-R04 e nota D1-R13 × D1-R04: feito (R.3 e bloco do D1-R13). (3) Remover a nota (s) “D1-R03 … × D1-55” da seção 5 e atualizar as seções 0, 3.2, 4.1 a 4.7 e 5 por script (ids, pontos, formatos da 2.2, Decreto e Lei 14.133 por folha, sequência): feito na seção 5, na 3.2, em 4.1 a 4.7 e na nova 4.8 (concentração por norma); a nota (s) da ficha 8.5 é da GCB (pendência 6.4, item 2). (4) Coordenação com a amostra da gbq-estilo: o AJ-2 (D1-R04) está na v2; a auditoria de estilo não estava em disco (pendência 6.4, item 6). (5) O R2 confere cada AJ aplicado literalmente e examina só o que a v2 mudou além dos AJ e o D1-R13: as mudanças além dos AJ são o D1-R13 e as atualizações de contagem e de texto das seções 0, 3.2, 4.1, 4.5 a 4.8, 5 e 6.

**R.7 Conferências de leva (seção 5 do parecer).** (1) C/E da leva: 17 C / 13 E (56,7%), folhas 8.4 10/10, 2.2 10/10, 6.4 8/8 (de 16): iguais. (2) Tetos por folha: formatos da 8.4 e da 6.4 iguais; 2.2 passa a 6/2/5/1/6/0 (DEF 6 e PAR 6 no teto de 6), leva 7/4/8/0/6/5. (3) Moldura acumulada e conjuntos: iguais (DA 48/21; D4 K1 14/6, K2 7/7, K3 5/4, K4 25/18; fecho neutro 2/3; “, e não” 1/2; D3 8/7). (4) Pontos sem duplicata: o D1-R03 deixa a leva; 30 códigos distintos, A2.2-09 não repetido nem usado na leva 1 nem nos canônicos. (5) Exigências da leva (c) e (d): iguais. (6) Primeiro e último id por lote: D4-R19–R28; D1-R01–R13 (sem o R03); D3-R14–R21. (7) Linha 1 e última linha: “# DA_reforco_leva2_v2.md — T-116 — 2026-10-20 — gerado por gcb-cpp”; “FIM DA LEVA 02 — REFORÇO DA”. (8) Bases reabertas: 37 trechos, 37 de 37 no adendo e na cópia (D1-R13: 24 palavras). Sequência (regra 6): gabarito e [TS] iguais aos da v1, resultados iguais (seção 4.3).

**R.8 Notas à GCB e à GBQ (seção 9 do parecer) e errata AJ-E1.** A2.2-05 e a ficha de notas: encaminhados na seção 6.4, itens 2 e 4 (sem decisão da produção). Pertinência dos arts. 53 e 72 da Lei 14.133: registro na pendência 6.4, item 5. Acréscimo à lista (k) a (x): D1-R13 × D1-R04 (seção 5). Errata AJ-E1 (D3-R13, leva 1): CONFERIDA no R1 (seção 6) e fora desta v2; este arquivo não altera a leva 1; a errata segue ao gatilho A como item separado.

Reforço de Direito Administrativo (D-REFORCO-DA), LEVA 2 de 12: 30 itens AUTORAL Certo/Errado, em três folhas — 8.4, segunda parte (D4-R19 a D4-R28), 2.2 (D1-R01 a D1-R13, sem o D1-R03, que não volta) e 6.4, primeira parte (D3-R14 a D3-R21). Ciclo s15c4. Esta é a v2 (gcb-cpp, rodada de correção do R1: 11 AJ aplicados em texto exato e D1-R03 substituído pelo D1-R13; ficha saida/gcb/DA_reforco_ficha_2026-10-20.md, seções 1, 7 e 8.3). Todos levam QA PENDENTE (D-QA-PENDENTE) e não entram em simulado antes do QA. Bases: adendos do D4, do D1 e do D3 (2026-10-20), Anexos N e cópias em saida/gcb/normativo_cache/; nenhuma leitura externa. Sem commit nem push.

## 0. Cabeçalho de contagens

| Folha | Itens | C | E | %C | [TS] (E / C) | Moldura S (C / E) | Formatos da leva (DEF/SUJ/SIT/NUM/PAR/APL) | Aderência (direta / parcial) | VOLÁTIL | REVERIFICAR |
|---|---|---|---|---|---|---|---|---|---|---|
| 8.4 (lote D4) | 10 | 6 | 4 | 60,0% | 4 / 0 | 1 / 0 | 3/1/2/0/3/1 | 10 / 0 | 0 | 0 |
| 2.2 (lote D1) | 12 | 6 | 6 | 50,0% | 6 / 0 | 0 / 0 | 2/2/5/0/3/0 | 12 / 0 | 0 | 0 |
| 6.4 (lote D3) | 8 | 5 | 3 | 62,5% | 3 / 0 | 1 / 3 | 2/1/1/0/0/4 | 6 / 2 | 0 | 0 |
| **Leva** | **30** | **17** | **13** | **56,7%** | **13 / 0** | **2 / 3** | **7/4/8/0/6/5** | **28 / 2** | **0** | **0** |

Em relação à v1, só mudam os formatos da 2.2 e da leva (D1-R13 é DEF; o D1-R03 era SUJ); C/E, [TS], moldura, aderência e sequência ficam iguais. Moldura S = item com moldura do Legislativo. VOLÁTIL = item cuja resposta depende de produto ou norma sujeita a reverificação: 0 nesta leva. REVERIFICAR = 0 (nenhum dispositivo de 2025 ou 2026 nos adendos). A 8.4 fecha com esta leva (10 + 10 = 20); a 2.2 vai de 8 a 20; a 6.4 vai de 8 a 16 (a leva 3 acrescenta 4).

## 1. Versão do estudante

Julgue cada item como Certo ou Errado.

Folha 8.4 — Valor público, cadeia de valor

**D4-R19.** Segundo o guia prático de análise ex post da Casa Civil, os processos de uma política pública são as ações que combinam os recursos disponíveis para produzir bens e serviços, e não os bens e serviços entregues, que são os produtos.

**D4-R20.** Considere que, em audiência pública de comissão da Câmara dos Deputados, um expositor trate das diretrizes para a boa governança do Referencial Básico de Governança Organizacional do TCU. Nessa situação, é correto afirmar que, entre essas diretrizes, está a de apoiar e viabilizar a inovação para agregar valor público.

**D4-R21.** De acordo com documento didático da Controladoria-Geral da União (CGU), observa-se, no setor público em geral, a existência de um padrão para a representação da cadeia de valor.

**D4-R22.** De acordo com documento didático da Controladoria-Geral da União (CGU), valor público está também associado ao grau de reconhecimento de atendimento ou satisfação por parte do cidadão ou de outro público específico.

**D4-R23.** Considere que um gestor analise as relações entre insumos, processos e produtos de uma política pública. Nessa situação, é correto afirmar que, segundo o guia prático de análise ex post da Casa Civil, essa avaliação deve investigar também se as ações orçamentárias estão observando a eficiência operacional e a economicidade.

**D4-R24.** Considere que um gestor classifique as atividades da organização, de acordo com o Referencial Básico de Governança Organizacional do TCU, em primárias ou de apoio. Nessa situação, ele estará correto ao incluir a tecnologia entre as atividades primárias.

**D4-R25.** Segundo o guia prático de análise ex post da Casa Civil, os insumos de uma política pública são os recursos do setor público, exclusivamente orçamentários, necessários para atingir os objetivos da política.

**D4-R26.** De acordo com documento didático da Controladoria-Geral da União (CGU), a metodologia de gestão de processos fornece a estrutura para a elaboração da cadeia de valor, que auxilia o estabelecimento de objetivos estratégicos a partir da missão institucional.

**D4-R27.** Segundo o guia prático de análise ex post da Casa Civil, os resultados de uma política pública correspondem à mudança de mais longo prazo no problema que a política busca enfrentar, alinhada aos objetivos da política.

**D4-R28.** De acordo com o guia prático de análise ex post da Casa Civil, as diferentes abordagens de avaliações aprofundadas inserem-se na análise dos componentes da cadeia de valor das políticas públicas ou dos componentes do modelo lógico.

Folha 2.2 — Parecer: responsabilidade do emissor do parecer

**D1-R01.** Nos termos da Lei nº 9.784/1999, se um parecer obrigatório e não vinculante deixar de ser emitido no prazo fixado, subsiste a responsabilidade de quem se omitiu no atendimento.

**D1-R02.** Segundo o Decreto nº 9.830/2019, considera-se erro grosseiro aquele manifesto, evidente e inescusável, praticado com culpa grave, caracterizado por ação ou omissão com elevado grau de negligência, imprudência ou imperícia.

**D1-R13.** Segundo o Decreto nº 9.830/2019, configura-se dolo ou erro grosseiro do agente público ainda que não reste comprovada, nos autos do processo de responsabilização, situação ou circunstância fática capaz de caracterizá-los.

**D1-R04.** Considere que determinado agente público, ao emitir opinião técnica, tenha dado causa a dano. Nessa situação, segundo o Decreto nº 9.830/2019, o mero nexo de causalidade entre a conduta e o resultado danoso implica a responsabilização do agente.

**D1-R05.** Segundo a Lei nº 9.784/1999, a falta, no prazo assinalado, de laudo técnico previamente exigido por ato normativo produz o mesmo efeito da falta de parecer obrigatório e vinculante: o processo não terá seguimento até que o órgão omisso apresente o laudo.

**D1-R06.** Considere que servidor público que participou de procedimento relacionado a licitação precise defender-se na esfera controladora em razão de ato praticado com estrita observância de orientação constante em parecer jurídico elaborado na forma do art. 53, § 1º, da Lei nº 14.133/2021. Nessa situação, a advocacia pública promoverá, a critério do servidor, sua representação judicial ou extrajudicial.

**D1-R07.** Nos termos da Lei nº 14.133/2021, a representação do agente público pela advocacia pública, em razão de ato praticado com estrita observância de parecer jurídico, não se aplica quando provas da prática de atos ilícitos culposos constarem nos autos do processo administrativo ou judicial.

**D1-R08.** Segundo o Decreto nº 9.830/2019, a responsabilização pela opinião técnica não se estende de forma automática ao decisor que a adotou como fundamento de decidir.

**D1-R09.** Considere que determinado agente público, ao emitir opinião técnica, tenha dado causa a dano ao erário de montante expressivo. Nessa situação, segundo o Decreto nº 9.830/2019, o montante do dano, por si só, não pode ser elemento para caracterizar o erro grosseiro ou o dolo do agente.

**D1-R10.** Segundo o Decreto nº 9.830/2019, o disposto em seu art. 12 afasta a possibilidade de aplicação de sanções previstas em normas disciplinares, inclusive nos casos de ação ou de omissão culposas de natureza leve.

**D1-R11.** Considere que o processo licitatório tenha chegado ao final da fase preparatória. Nessa situação, nos termos da Lei nº 14.133/2021, ele seguirá para o órgão de assessoramento jurídico da Administração, que realizará controle posterior de legalidade mediante análise jurídica da contratação.

**D1-R12.** Considere que um órgão público faça contratação direta por inexigibilidade de licitação. Nessa situação, nos termos da Lei nº 14.133/2021, o processo deverá ser instruído com parecer jurídico e pareceres técnicos, se for o caso, que demonstrem o atendimento dos requisitos exigidos.

Folha 6.4 — Requisitos para a demonstração da responsabilidade do Estado

**D3-R14.** Nos termos da Lei nº 8.987/1995, incumbe à concessionária a execução do serviço concedido, cabendo-lhe responder por todos os prejuízos causados ao poder concedente, aos usuários ou a terceiros.

**D3-R15.** Nos termos do art. 186 do Código Civil, o ato ilícito configura-se ainda que o dano causado a outrem seja exclusivamente moral.

**D3-R16.** Considere que servidor de órgão do Poder Legislativo da União, ao ser alvo de agravo divulgado em meio de comunicação, busque a proteção prevista no art. 5º, V, da Constituição Federal. Nessa situação, além do direito de resposta proporcional ao agravo, é assegurada a indenização por dano material ou moral, mas não por dano à imagem.

**D3-R17.** Considere que determinada empresa desenvolva, normalmente, atividade que implique, por sua natureza, risco para os direitos de outrem e que dessa atividade resulte dano a terceiro. Nessa situação, nos termos do art. 927, parágrafo único, do Código Civil, haverá obrigação de reparar o dano, independentemente de culpa.

**D3-R18.** Considere que servidor público civil da União lotado em órgão do Poder Legislativo da União tenha causado dano ao erário e falecido. Nessa situação, a obrigação de reparar o dano estende-se aos sucessores, que respondem sem limite de valor, conforme a Lei nº 8.112/1990.

**D3-R19.** Considere que servidor de órgão do Poder Legislativo da União tenha sofrido dano causado por particular e pretenda ser indenizado. Nessa situação, nos termos do art. 944, caput, do Código Civil, a indenização mede-se pela gravidade da culpa do particular.

**D3-R20.** Considere que servidor público civil da União lotado em órgão do Poder Legislativo da União, agindo com culpa no exercício de suas atribuições, tenha causado dano a terceiros. Nessa situação, ele responderá perante a Fazenda Pública, em ação regressiva, conforme a Lei nº 8.112/1990.

**D3-R21.** Nos termos do art. 5º, X, da Constituição Federal, é assegurado o direito a indenização pelo dano material ou moral decorrente da violação da intimidade, da vida privada, da honra e da imagem das pessoas.

## 2. Gabarito comentado

Folha 8.4 — Valor público, cadeia de valor

**D4-R19** (folha 8.4) — AUTORAL — QA PENDENTE
- itemEdital: P1-DA-8.4
- Ponto de julgamento: A8.4-21 — R77 (contraste R78) — processos são as ações que combinam os recursos disponíveis para produzir bens e serviços, e não os bens e serviços entregues, que são os produtos
- Formato: PAR
- Moldura: N
- Aderência: direta
- Gabarito: C
- Justificativa (linha 1): R77 define processos como as ações que combinam os recursos disponíveis para produzir bens e serviços, e R78 define produtos como os bens ou serviços resultantes de um processo, as entregas.
- Justificativa (linha 2): O item reproduz o contraste sem troca; a tentação é confundir processos com produtos e marcar errado a frase que os distingue.
- Tipo de base: REFERENCIAL OUTRA_OFICIAL
- Base: R77 e R78 (fonte F3 do adendo do D4) — Casa Civil da Presidência da República, Avaliação de Políticas Públicas: guia prático de análise ex post, v. 2, 2018, p. 59 (Figura 1); https://www.gov.br/casacivil/pt-br/assuntos/governanca/comite-interministerial-de-governanca/arquivos/avaliacao-de-politicas-publicas-guia-pratico-de-analise-ex-post.pdf; consulta 20/10/2026; trecho: “as ações que combinam os recursos disponíveis para produzir bens e serviços” […] “os bens ou serviços resultantes de um processo, ou seja, as entregas (outputs)”; nota: primeiro trecho: célula “Processos” (R77); segundo: célula “Produtos” (R78), usada como contraste
- Mecanismo: Definição ou descrição canônica correta (C1)
- Difere de: D4-28 porque este julga os elos da cadeia de valor das políticas públicas (R18, com a troca de ‘resultados’ por ‘metas’); aqui se julga o conceito de processos em contraste com produtos (R77 e R78). Nota ao simulado: D4-R19, D4-R25 e D4-R27 compartilham os componentes do modelo lógico com o D4-28.
- Marcas: TS=não; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D4-R20** (folha 8.4) — AUTORAL — QA PENDENTE
- itemEdital: P1-DA-8.4
- Ponto de julgamento: A8.4-02 — R60 — entre as diretrizes para a boa governança do Referencial do TCU está apoiar e viabilizar a inovação para agregar valor público
- Formato: APL
- Moldura: S — audiência pública de comissão da Câmara dos Deputados, expositor — fecho: neutro
- Aderência: direta
- Gabarito: C
- Justificativa (linha 1): R60 lista, entre as diretrizes para a boa governança do Referencial do TCU, a de apoiar e viabilizar a inovação para agregar valor público e lidar com as limitações de recursos e com novas ameaças e oportunidades.
- Justificativa (linha 2): O item reproduz a diretriz sem troca e sem marcador de exclusividade; a tentação é duvidar de que a inovação conste de um referencial de governança e marcar errado.
- Tipo de base: REFERENCIAL OUTRA_OFICIAL
- Base: R60 (fonte F1 do adendo do D4) — TCU, Referencial Básico de Governança Organizacional, 3. ed., 2020, p. 48-49; https://portal.tcu.gov.br/data/files/FB/B6/FB/85/1CD4671023455957E18818A8/Referencial_basico_governanca_organizacional_3_edicao.pdf; consulta 20/10/2026; trecho: “f) apoiar e viabilizar a inovação para agregar valor público e lidar com as limitações de recursos e com novas ameaças e oportunidades;”; nota: alínea f da seção “Diretrizes para a boa governança” (Capítulo 4); a abertura da lista está na p. 48 e a alínea f, na p. 49
- Mecanismo: Reprodução próxima do texto (C2)
- Difere de: D4-32 porque este julga que o desempenho é processo de geração de valor (Ipea, R17); aqui se julga uma diretriz da boa governança no Referencial do TCU (R60).
- Marcas: TS=não; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D4-R21** (folha 8.4) — AUTORAL — QA PENDENTE [TS]
- itemEdital: P1-DA-8.4
- Ponto de julgamento: A8.4-10 — R66 (CGU) — no setor público em geral observa-se a inexistência de padrão para a representação da cadeia de valor (item troca por existência de padrão)
- Formato: DEF
- Moldura: N
- Aderência: direta
- Gabarito: E
- Justificativa (linha 1): R66 diz que, no setor público em geral, observa-se a inexistência de um padrão para representação da cadeia de valor.
- Justificativa (linha 2): O item troca ‘inexistência’ por ‘existência’ de padrão; a tentação é supor que haja um modelo único de representação da cadeia de valor no setor público.
- Tipo de base: REFERENCIAL OUTRA_OFICIAL
- Base: R66 (fonte F10 do adendo do D4) — Controladoria-Geral da União, documento didático Cadeia de valor da CGU (sem data impressa), p. 6 do PDF (sem numeração impressa); https://repositorio.cgu.gov.br/bitstream/1/29544/10/documento_didatico_cadeia_valor.pdf; consulta 20/10/2026; trecho: “no setor público em geral observa-se a inexistência de um padrão para representação da cadeia de valor”; nota: documento interno da CGU; o item usa o “setor público em geral”, literal do trecho, e não generaliza o que R68 e R69 dizem só da CGU (alerta B8)
- Mecanismo: Inversão de definição, de polaridade ou de relação (E2)
- Troca: inexistência de um padrão → existência de um padrão (R66)
- Difere de: D4-33 porque este julga que a cadeia de valor público é adaptação da cadeia de Porter (CGU, R16); aqui se julga a existência de padrão de representação da cadeia de valor (CGU, R66).
- Marcas: TS=sim; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D4-R22** (folha 8.4) — AUTORAL — QA PENDENTE
- itemEdital: P1-DA-8.4
- Ponto de julgamento: A8.4-09 — R65 (CGU) — valor público está também associado ao grau de reconhecimento de atendimento ou satisfação por parte do cidadão ou de outro público específico
- Formato: DEF
- Moldura: N
- Aderência: direta
- Gabarito: C
- Justificativa (linha 1): R65 diz que valor público está também associado ao grau de reconhecimento de atendimento ou satisfação por parte do cidadão, ou outro público específico.
- Justificativa (linha 2): O item reproduz o trecho, em que o advérbio ‘também’ acrescenta uma associação sem excluir outras; a tentação é tomar a frase como definição única de valor público e marcar errado.
- Tipo de base: REFERENCIAL OUTRA_OFICIAL
- Base: R65 (fonte F10 do adendo do D4) — Controladoria-Geral da União, documento didático Cadeia de valor da CGU (sem data impressa), p. 6 do PDF (sem numeração impressa); https://repositorio.cgu.gov.br/bitstream/1/29544/10/documento_didatico_cadeia_valor.pdf; consulta 20/10/2026; trecho: “valor público está também associado ao grau de reconhecimento de atendimento ou satisfação por parte do cidadão, ou outro público específico”; nota: documento interno da CGU; o item não cita nem parafraseia a definição do Decreto nº 9.203/2017 que o trecho ressalva (exigência (c) da ficha)
- Mecanismo: Reprodução próxima do texto (C2)
- Difere de: D4-30 porque este julga a definição de valor público como produtos e resultados gerados, preservados ou entregues (norma); aqui se julga a associação ao reconhecimento pelo cidadão no documento da CGU (R65).
- Marcas: TS=não; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D4-R23** (folha 8.4) — AUTORAL — QA PENDENTE
- itemEdital: P1-DA-8.4
- Ponto de julgamento: A8.4-25 — R81 (Casa Civil) — a avaliação das relações entre insumos, processos e produtos também investiga a eficiência operacional e a economicidade
- Formato: SIT
- Moldura: N — fecho: neutro
- Aderência: direta
- Gabarito: C
- Justificativa (linha 1): R81 diz que a avaliação que analisa as relações entre insumos, processos e produtos também deve investigar se as ações orçamentárias estão observando a eficiência operacional e a economicidade.
- Justificativa (linha 2): O item reproduz o trecho sem troca; a tentação é supor que a eficiência operacional e a economicidade ficariam fora da avaliação dessas relações.
- Tipo de base: REFERENCIAL OUTRA_OFICIAL
- Base: R81 (fonte F3 do adendo do D4) — Casa Civil da Presidência da República, Avaliação de Políticas Públicas: guia prático de análise ex post, v. 2, 2018, p. 41; https://www.gov.br/casacivil/pt-br/assuntos/governanca/comite-interministerial-de-governanca/arquivos/avaliacao-de-politicas-publicas-guia-pratico-de-analise-ex-post.pdf; consulta 20/10/2026; trecho: “avaliação que analisa as relações entre insumos, processos e produtos também deve investigar se as ações orçamentárias estão observando a eficiência operacional e a economicidade”
- Mecanismo: Reprodução próxima do texto (C2)
- Difere de: D4-31 porque este julga o desempenho como fluxo dos insumos ao valor público (Ipea, R17); aqui se julga o que a avaliação das relações entre insumos, processos e produtos investiga (Casa Civil, R81).
- Marcas: TS=não; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D4-R24** (folha 8.4) — AUTORAL — QA PENDENTE [TS]
- itemEdital: P1-DA-8.4
- Ponto de julgamento: A8.4-05 — R62 (TCU; o item não nomeia o autor) — a tecnologia está entre as atividades de apoio, e não entre as primárias (item troca por primárias)
- Formato: SIT
- Moldura: N — fecho: acerto
- Aderência: direta
- Gabarito: E
- Justificativa (linha 1): R62 registra, no Referencial do TCU, a classificação das atividades da organização em primárias (logísticas interna e externa, operações, marketing e vendas, serviços) ou de apoio, entre as quais está a tecnologia.
- Justificativa (linha 2): O item troca ‘de apoio’ por ‘primárias’ para a tecnologia, mantendo a classificação em dois grupos; a tentação é associar a tecnologia às operações e à produção.
- Tipo de base: REFERENCIAL OUTRA_OFICIAL
- Base: R62 (fonte F1 do adendo do D4) — TCU, Referencial Básico de Governança Organizacional, 3. ed., 2020, p. 82; https://portal.tcu.gov.br/data/files/FB/B6/FB/85/1CD4671023455957E18818A8/Referencial_basico_governanca_organizacional_3_edicao.pdf; consulta 20/10/2026; trecho: “ou de apoio (aquisições, tecnologia, recursos humanos, infraestrutura, planejamento, finanças, contabilidade, administração, assessoria jurídica)”; nota: o TCU atribui a classificação a Porter (1989); o item atribui ao Referencial do TCU e não nomeia o autor (alerta B2)
- Mecanismo: Troca de conceito vizinho (E1)
- Troca: tecnologia entre as atividades de apoio → tecnologia entre as atividades primárias (R62)
- Difere de: D4-33 porque este julga que a cadeia de valor público é adaptação da cadeia de Porter (CGU, R16); aqui se julga a classificação das atividades em primárias e de apoio no Referencial do TCU (R62).
- Marcas: TS=sim; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D4-R25** (folha 8.4) — AUTORAL — QA PENDENTE [TS]
- itemEdital: P1-DA-8.4
- Ponto de julgamento: A8.4-20 — R76 (Casa Civil) — insumos: recursos do setor público, orçamentários ou não, necessários para atingir os objetivos da política (item troca por exclusivamente orçamentários)
- Formato: DEF
- Moldura: N
- Aderência: direta
- Gabarito: E
- Justificativa (linha 1): R76 define insumos como recursos do setor público, orçamentários ou não, necessários para atingir os objetivos da política.
- Justificativa (linha 2): O item restringe os insumos a recursos ‘exclusivamente orçamentários’; a tentação é associar o insumo de uma política pública apenas à dotação orçamentária.
- Tipo de base: REFERENCIAL OUTRA_OFICIAL
- Base: R76 (fonte F3 do adendo do D4) — Casa Civil da Presidência da República, Avaliação de Políticas Públicas: guia prático de análise ex post, v. 2, 2018, p. 59 (Figura 1); https://www.gov.br/casacivil/pt-br/assuntos/governanca/comite-interministerial-de-governanca/arquivos/avaliacao-de-politicas-publicas-guia-pratico-de-analise-ex-post.pdf; consulta 20/10/2026; trecho: “Recursos do setor público – orçamentários ou não – necessários para atingir os objetivos da política.”; nota: célula “Insumos” do modelo lógico
- Mecanismo: Regra relativa convertida em absoluta (E6)
- Troca: orçamentários ou não → exclusivamente orçamentários (R76)
- Difere de: D4-28 porque este julga os elos da cadeia de valor das políticas públicas (R18); aqui se julga o conceito do componente insumos (R76).
- Marcas: TS=sim; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D4-R26** (folha 8.4) — AUTORAL — QA PENDENTE
- itemEdital: P1-DA-8.4
- Ponto de julgamento: A8.4-11 — R67 (CGU) — a metodologia de gestão de processos fornece a estrutura para a elaboração da cadeia de valor, que auxilia o estabelecimento de objetivos estratégicos a partir da missão institucional
- Formato: SUJ
- Moldura: N
- Aderência: direta
- Gabarito: C
- Justificativa (linha 1): R67 diz que a metodologia de gestão de processos fornece a estrutura para a elaboração da cadeia de valor, que auxilia o estabelecimento de objetivos estratégicos a partir da missão institucional.
- Justificativa (linha 2): O item dá a cada função o seu sujeito, sem troca (a metodologia fornece a estrutura; a cadeia de valor auxilia os objetivos); a tentação é inverter a ordem entre gestão de processos e cadeia de valor.
- Tipo de base: REFERENCIAL OUTRA_OFICIAL
- Base: R67 (fonte F10 do adendo do D4) — Controladoria-Geral da União, documento didático Cadeia de valor da CGU (sem data impressa), p. 7 do PDF (sem numeração impressa); https://repositorio.cgu.gov.br/bitstream/1/29544/10/documento_didatico_cadeia_valor.pdf; consulta 20/10/2026; trecho: “fornece a estrutura para elaboração da cadeia de valor, que auxilia o estabelecimento de objetivos estratégicos a partir da missão institucional”; nota: o sujeito de “fornece” é “uma metodologia de gestão de processos”, antecedente de “que, por sua vez” na mesma frase do documento (corte no início, como no adendo)
- Mecanismo: Reprodução próxima do texto (C2)
- Difere de: D4-33 porque este julga que a cadeia de valor público é adaptação da cadeia de Porter (CGU, R16); aqui se julga a relação entre gestão de processos, cadeia de valor e objetivos estratégicos (CGU, R67).
- Marcas: TS=não; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D4-R27** (folha 8.4) — AUTORAL — QA PENDENTE [TS]
- itemEdital: P1-DA-8.4
- Ponto de julgamento: A8.4-24 — R80 (contraste R79) — a mudança de mais longo prazo no problema, alinhada aos objetivos da política, é o impacto (item troca por resultados)
- Formato: PAR
- Moldura: N
- Aderência: direta
- Gabarito: E
- Justificativa (linha 1): R80 define impactos como a mudança de mais longo prazo no problema que a política busca enfrentar, e R79 define resultados como mudanças incidentes sobre as causas do problema, que decorrem de um ou mais produtos.
- Justificativa (linha 2): O item atribui aos resultados a definição dos impactos; a tentação é tratar resultados e impactos como sinônimos do efeito final da política.
- Tipo de base: REFERENCIAL OUTRA_OFICIAL
- Base: R80 e R79 (fonte F3 do adendo do D4) — Casa Civil da Presidência da República, Avaliação de Políticas Públicas: guia prático de análise ex post, v. 2, 2018, p. 59 (Figura 1); https://www.gov.br/casacivil/pt-br/assuntos/governanca/comite-interministerial-de-governanca/arquivos/avaliacao-de-politicas-publicas-guia-pratico-de-analise-ex-post.pdf; consulta 20/10/2026; trecho: “Mudança de mais longo prazo no problema que a política busca enfrentar, alinhado aos objetivos da política.” […] “mudanças incidentes sobre as causas do problema”; nota: primeiro trecho: célula “Impactos” (R80); segundo: célula “Resultados” (R79), usada como contraste
- Mecanismo: Troca de conceito vizinho (E1)
- Troca: impactos → resultados (R80)
- Difere de: D4-28 porque este julga os elos da lista de R18 (troca de ‘resultados’ por ‘metas’); aqui se julga o conceito do componente impactos, atribuído aos resultados (R80 e R79).
- Marcas: TS=sim; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D4-R28** (folha 8.4) — AUTORAL — QA PENDENTE
- itemEdital: P1-DA-8.4
- Ponto de julgamento: A8.4-18 — R74 (Casa Civil) — as avaliações aprofundadas inserem-se na análise dos componentes da cadeia de valor das políticas públicas ou dos componentes do modelo lógico
- Formato: PAR
- Moldura: N
- Aderência: direta
- Gabarito: C
- Justificativa (linha 1): R74 diz que as diferentes abordagens de avaliações aprofundadas inserem-se na análise dos componentes da cadeia de valor das políticas públicas ou, como será visto nos capítulos 3 e 5, dos componentes do modelo lógico.
- Justificativa (linha 2): O item reproduz o trecho sem troca; a tentação é ver a cadeia de valor das políticas públicas e o modelo lógico como conceitos excludentes e marcar errado.
- Tipo de base: REFERENCIAL OUTRA_OFICIAL
- Base: R74 (fonte F3 do adendo do D4) — Casa Civil da Presidência da República, Avaliação de Políticas Públicas: guia prático de análise ex post, v. 2, 2018, p. 41-42; https://www.gov.br/casacivil/pt-br/assuntos/governanca/comite-interministerial-de-governanca/arquivos/avaliacao-de-politicas-publicas-guia-pratico-de-analise-ex-post.pdf; consulta 20/10/2026; trecho: “na análise dos componentes da cadeia de valor das políticas públicas ou, como será visto nos capítulos 3 e 5, dos componentes do modelo lógico”; nota: a frase passa da p. 41 para a p. 42; o item omite o inciso “como será visto nos capítulos 3 e 5”, que é remissão do guia
- Mecanismo: Reprodução próxima do texto (C2)
- Difere de: D4-28 porque este julga os elos da lista de R18 (troca de ‘resultados’ por ‘metas’); aqui se julga o enquadramento das avaliações aprofundadas nos componentes da cadeia de valor ou do modelo lógico (R74).
- Marcas: TS=não; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

Folha 2.2 — Parecer: responsabilidade do emissor do parecer

**D1-R01** (folha 2.2) — AUTORAL — QA PENDENTE
- itemEdital: P1-DA-2.2
- Ponto de julgamento: A2.2-02 — Lei 9.784, art. 42, § 2º — a dispensa do parecer obrigatório e não vinculante, com prosseguimento e decisão do processo, não prejudica a responsabilidade de quem se omitiu no atendimento
- Formato: SUJ
- Moldura: N
- Aderência: direta
- Gabarito: C
- Justificativa (linha 1): O art. 42, § 2º, prevê que, faltando no prazo o parecer obrigatório e não vinculante, o processo poderá ter prosseguimento e ser decidido com sua dispensa, sem prejuízo da responsabilidade de quem se omitiu no atendimento.
- Justificativa (linha 2): O item mantém a ressalva da responsabilidade de quem se omitiu; a tentação é supor que a dispensa do parecer livre de responsabilidade quem deixou de emiti-lo.
- Tipo de base: DISPOSITIVO
- Base: Lei 9.784/1999, art. 42, § 2º (fonte F1 do adendo do D1; adendo do D1, seção 4.1); https://www.planalto.gov.br/ccivil_03/leis/l9784.htm; consulta 20/10/2026; trecho: “o processo poderá ter prosseguimento e ser decidido com sua dispensa, sem prejuízo da responsabilidade de quem se omitiu no atendimento”; nota: reconfirmação de 20/10/2026 do Anexo N do D1, seção 5; alerta P1
- Mecanismo: Reprodução próxima do texto normativo (C2)
- Difere de: D1-56 porque este julga o efeito da falta do parecer não vinculante sobre o seguimento do processo (com a troca pelo efeito do § 1º); aqui se julga a ressalva da responsabilidade de quem se omitiu, parte final do mesmo § 2º (nota ao simulado: não pôr D1-R01 e D1-56 no mesmo simulado).
- Marcas: TS=não; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D1-R02** (folha 2.2) — AUTORAL — QA PENDENTE
- itemEdital: P1-DA-2.2
- Ponto de julgamento: A2.2-08 — Decreto 9.830, art. 12, § 1º — erro grosseiro é o manifesto, evidente e inescusável, praticado com culpa grave, com elevado grau de negligência, imprudência ou imperícia
- Formato: DEF
- Moldura: N
- Aderência: direta
- Gabarito: C
- Justificativa (linha 1): O art. 12, § 1º, do Decreto 9.830 considera erro grosseiro aquele manifesto, evidente e inescusável, praticado com culpa grave, caracterizado por ação ou omissão com elevado grau de negligência, imprudência ou imperícia.
- Justificativa (linha 2): O item reproduz o conceito sem troca, inclusive a ‘culpa grave’ (alerta P4); a tentação é estranhar um conceito normativo de erro grosseiro e marcar errado.
- Tipo de base: DISPOSITIVO
- Base: Decreto 9.830/2019, art. 12, § 1º (fonte F3 do adendo do D1; adendo do D1, seção 4.3); https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d9830.htm; consulta 20/10/2026; trecho: “Considera-se erro grosseiro aquele manifesto, evidente e inescusável praticado com culpa grave, caracterizado por ação ou omissão com elevado grau de negligência, imprudência ou imperícia.”; nota: “inescusável”, grafia do texto; o item não afirma que o Decreto alcance órgão do Poder Legislativo (alerta P3)
- Mecanismo: Reprodução próxima do texto normativo (C2)
- Difere de: D1-58 porque este julga a LINDB, art. 28, caput, com a troca do elemento subjetivo por ‘culpa, ainda que leve’; aqui se julga o conceito de erro grosseiro do Decreto 9.830, art. 12, § 1º, sem troca de ‘culpa grave’ (nota ao simulado: não pôr D1-R02 e D1-58 no mesmo simulado).
- Marcas: TS=não; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D1-R13** (folha 2.2) — AUTORAL — QA PENDENTE [TS]
- itemEdital: P1-DA-2.2
- Ponto de julgamento: A2.2-09 — Decreto 9.830, art. 12, § 2º — não se configura dolo ou erro grosseiro se não restar comprovada, nos autos do processo de responsabilização, situação ou circunstância fática capaz de caracterizá-los (item troca: configura-se ainda que não reste comprovada)
- Formato: DEF
- Moldura: N
- Aderência: direta
- Gabarito: E
- Justificativa (linha 1): O art. 12, § 2º, do Decreto 9.830 dispõe que não será configurado dolo ou erro grosseiro do agente público se não restar comprovada, nos autos do processo de responsabilização, situação ou circunstância fática capaz de caracterizá-los.
- Justificativa (linha 2): O item inverte a polaridade da exigência e afirma que dolo ou erro grosseiro se configuram ainda que a comprovação nos autos falte; a tentação é presumir o dolo ou o erro grosseiro do dano ou da conduta, sem a circunstância fática comprovada.
- Tipo de base: DISPOSITIVO
- Base: Decreto 9.830/2019, art. 12, § 2º (fonte F3 do adendo do D1; adendo do D1, seção 4.3); https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d9830.htm; consulta 20/10/2026; trecho: “Não será configurado dolo ou erro grosseiro do agente público se não restar comprovada, nos autos do processo de responsabilização, situação ou circunstância fática”; nota: o trecho termina antes de “capaz de caracterizar o dolo ou o erro grosseiro”, que o item mantém, por limite de 25 palavras; a cena não nomeia órgão do Legislativo e o item não afirma que o Decreto alcance órgão do Poder Legislativo (alerta P3); com este item o Decreto 9.830 chega a 6 na folha, acima do teto de 5 da ficha, seção 8.2, item 5 (pendência 6.4, item 1)
- Mecanismo: Inversão de definição, de polaridade ou de relação (E2)
- Troca: não será configurado dolo ou erro grosseiro se não restar comprovada situação ou circunstância fática → configura-se dolo ou erro grosseiro ainda que não reste comprovada (art. 12, § 2º)
- Difere de: D1-R04 porque este julga o nexo de causalidade (art. 12, § 3º: o mero nexo não implica responsabilização, exceto se comprovado o dolo ou o erro grosseiro); aqui se julga a exigência de comprovação nos autos para configurar dolo ou erro grosseiro (art. 12, § 2º). Nenhum canônico da folha cita o Decreto 9.830 (D1-57 e D1-58 julgam a LINDB, art. 28, caput). Nota ao simulado: não pôr D1-R13 e D1-R04 no mesmo simulado (mesma família: prova do dolo ou do erro grosseiro).
- Marcas: TS=sim; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D1-R04** (folha 2.2) — AUTORAL — QA PENDENTE [TS]
- itemEdital: P1-DA-2.2
- Ponto de julgamento: A2.2-10 — Decreto 9.830, art. 12, § 3º — o mero nexo de causalidade entre a conduta e o resultado danoso não implica responsabilização, salvo dolo ou erro grosseiro comprovado (item troca: o nexo implica)
- Formato: SIT
- Moldura: N
- Aderência: direta
- Gabarito: E
- Justificativa (linha 1): O art. 12, § 3º, do Decreto 9.830 prevê que o mero nexo de causalidade entre a conduta e o resultado danoso não implica responsabilização, exceto se comprovado o dolo ou o erro grosseiro do agente público.
- Justificativa (linha 2): O item afirma que o mero nexo implica a responsabilização; a tentação é equiparar causar o dano a responder por ele.
- Tipo de base: DISPOSITIVO
- Base: Decreto 9.830/2019, art. 12, § 3º (fonte F3 do adendo do D1; adendo do D1, seção 4.3); https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d9830.htm; consulta 20/10/2026; trecho: “O mero nexo de causalidade entre a conduta e o resultado danoso não implica responsabilização, exceto se comprovado o dolo ou o erro grosseiro”; nota: a cena não nomeia órgão do Legislativo e o item não julga o alcance do Decreto (alerta P3); o cenário não enumera os elementos do dispositivo (ficha, seção 7.4.5)
- Mecanismo: Inversão de definição, de polaridade ou de relação (E2)
- Troca: não implica responsabilização → implica a responsabilização (art. 12, § 3º)
- Difere de: D1-57 e D1-58 porque estes julgam a LINDB, art. 28 (dolo ou erro grosseiro; troca por culpa, ainda que leve); aqui se julga o nexo de causalidade no Decreto 9.830, art. 12, § 3º.
- Marcas: TS=sim; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D1-R05** (folha 2.2) — AUTORAL — QA PENDENTE [TS]
- itemEdital: P1-DA-2.2
- Ponto de julgamento: A2.2-03 — Lei 9.784, art. 43 (× art. 42, § 1º) — laudo técnico não entregue no prazo: o órgão de instrução solicita laudo a outro órgão equivalente (item troca: o processo não terá seguimento até a apresentação)
- Formato: PAR
- Moldura: N
- Aderência: direta
- Gabarito: E
- Justificativa (linha 1): O art. 43 manda o órgão de instrução solicitar laudo técnico a outro órgão de capacidade equivalente quando o encarregado não o entrega no prazo; a paralisação do processo é a consequência que o art. 42, § 1º, prevê para o parecer obrigatório e vinculante.
- Justificativa (linha 2): O item aplica ao laudo técnico o efeito do parecer obrigatório e vinculante; a tentação é tratar laudo e parecer como figuras do mesmo regime.
- Tipo de base: DISPOSITIVO
- Base: Lei 9.784/1999, art. 43 (× art. 42, § 1º) (fonte F1 do adendo do D1; adendo do D1, seção 4.1); https://www.planalto.gov.br/ccivil_03/leis/l9784.htm; consulta 20/10/2026; trecho: “deverá solicitar laudo técnico de outro órgão dotado de qualificação e capacidade técnica equivalentes” […] “o processo não terá seguimento até a respectiva apresentação”; nota: primeiro trecho: art. 43; segundo: art. 42, § 1º (efeito do parecer obrigatório e vinculante, usado como contraste)
- Mecanismo: Troca de conceito vizinho (E1)
- Troca: solicitação de laudo técnico a outro órgão equivalente → o processo não terá seguimento até que o órgão omisso apresente o laudo (art. 43 × art. 42, § 1º)
- Difere de: D1-55 e D1-56 porque estes julgam o efeito da falta do parecer obrigatório (art. 42, §§ 1º e 2º); aqui se julga o art. 43, que trata do laudo técnico. Nota ao simulado: não pôr D1-R05 e D1-56 no mesmo simulado (os dois fazem a comparação com o parecer obrigatório e vinculante).
- Marcas: TS=sim; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D1-R06** (folha 2.2) — AUTORAL — QA PENDENTE
- itemEdital: P1-DA-2.2
- Ponto de julgamento: A2.2-17 — Lei 14.133, art. 10, caput — quem agiu com estrita observância de parecer jurídico do art. 53, § 1º, e precisa defender-se tem representação promovida pela advocacia pública, a critério do agente
- Formato: SIT
- Moldura: N
- Aderência: direta
- Gabarito: C
- Justificativa (linha 1): O art. 10, caput, prevê que a advocacia pública promoverá, a critério do agente público, a representação judicial ou extrajudicial de quem precise defender-se por ato praticado com estrita observância de orientação constante em parecer jurídico elaborado na forma do art. 53, § 1º.
- Justificativa (linha 2): O item aplica a regra ao cenário descrito, sem troca; a tentação é supor que a representação seja imposta ao agente, e não prevista a critério dele.
- Tipo de base: DISPOSITIVO
- Base: Lei 14.133/2021, art. 10, caput (fonte F4 do adendo do D1; adendo do D1, seção 4.4); https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm; consulta 20/10/2026; trecho: “ato praticado com estrita observância de orientação constante em parecer jurídico” […] “a advocacia pública promoverá, a critério do agente público, sua representação judicial ou extrajudicial”; nota: reconfirmação de 20/10/2026 do Anexo N do D5; o art. 10 protege o agente que seguiu o parecer, e não o emissor (alerta P5); a cena não nomeia órgão do Legislativo
- Mecanismo: Reprodução próxima do texto normativo (C2)
- Difere de: Nenhum canônico da folha julga a Lei 14.133 (D1-53 a D1-60 são da Lei 9.784 e da LINDB); fora da folha, nenhum item do D5 usa o art. 10 (adendo do D1, alerta P5).
- Marcas: TS=não; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D1-R07** (folha 2.2) — AUTORAL — QA PENDENTE [TS]
- itemEdital: P1-DA-2.2
- Ponto de julgamento: A2.2-18 — Lei 14.133, art. 10, § 1º, II — a representação do caput não se aplica quando provas de atos ilícitos dolosos constarem dos autos (item troca dolosos por culposos)
- Formato: PAR
- Moldura: N
- Aderência: direta
- Gabarito: E
- Justificativa (linha 1): O art. 10, § 1º, II, afasta a representação do caput quando provas da prática de atos ilícitos dolosos constarem nos autos do processo administrativo ou judicial.
- Justificativa (linha 2): O item troca ‘dolosos’ por ‘culposos’; a tentação é supor que qualquer ato ilícito comprovado nos autos afaste a representação.
- Tipo de base: DISPOSITIVO
- Base: Lei 14.133/2021, art. 10, § 1º, II (fonte F4 do adendo do D1; adendo do D1, seção 4.4); https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm; consulta 20/10/2026; trecho: “Não se aplica o disposto no caput deste artigo quando:” […] “provas da prática de atos ilícitos dolosos constarem nos autos do processo administrativo ou judicial”; nota: primeiro trecho: art. 10, § 1º (caput do parágrafo); segundo: inciso II; o inciso I é vetado e não é usado (alerta P5)
- Mecanismo: Troca de conceito vizinho (E1)
- Troca: atos ilícitos dolosos → atos ilícitos culposos (art. 10, § 1º, II)
- Difere de: D1-R06 porque este julga a regra do caput (representação a critério do agente); aqui se julga a exceção do § 1º, II.
- Marcas: TS=sim; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D1-R08** (folha 2.2) — AUTORAL — QA PENDENTE
- itemEdital: P1-DA-2.2
- Ponto de julgamento: A2.2-13 — Decreto 9.830, art. 12, § 6º (primeira parte) — a responsabilização pela opinião técnica não se estende de forma automática ao decisor que a adotou como fundamento de decidir
- Formato: SUJ
- Moldura: N
- Aderência: direta
- Gabarito: C
- Justificativa (linha 1): O art. 12, § 6º, do Decreto 9.830 dispõe que a responsabilização pela opinião técnica não se estende de forma automática ao decisor que a adotou como fundamento de decidir.
- Justificativa (linha 2): O item reproduz só a primeira parte do parágrafo, sem afirmar que a extensão nunca ocorre; a tentação é supor que o decisor responda sempre pela opinião técnica que adotou.
- Tipo de base: DISPOSITIVO
- Base: Decreto 9.830/2019, art. 12, § 6º, primeira parte (fonte F3 do adendo do D1; adendo do D1, seção 4.3); https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d9830.htm; consulta 20/10/2026; trecho: “A responsabilização pela opinião técnica não se estende de forma automática ao decisor que a adotou como fundamento de decidir”; nota: a segunda parte do § 6º (A2.2-14) não é usada (adendo do D1, tabela 3.1); o item não afirma o alcance do Decreto (alerta P3)
- Mecanismo: Afirmação parcial verdadeira (C6)
- Difere de: D1-57 porque este julga a responsabilidade pessoal do agente por suas decisões ou opiniões técnicas (LINDB, art. 28); aqui se julga a relação entre o emissor da opinião técnica e o decisor que a adotou (Decreto 9.830, art. 12, § 6º).
- Marcas: TS=não; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D1-R09** (folha 2.2) — AUTORAL — QA PENDENTE
- itemEdital: P1-DA-2.2
- Ponto de julgamento: A2.2-12 — Decreto 9.830, art. 12, § 5º — o montante do dano ao erário, ainda que expressivo, não pode, por si só, caracterizar o erro grosseiro ou o dolo
- Formato: SIT
- Moldura: N
- Aderência: direta
- Gabarito: C
- Justificativa (linha 1): O art. 12, § 5º, do Decreto 9.830 dispõe que o montante do dano ao erário, ainda que expressivo, não poderá, por si só, ser elemento para caracterizar o erro grosseiro ou o dolo.
- Justificativa (linha 2): O item mantém a cláusula ‘por si só’ e o cenário de dano expressivo; a tentação é inferir dolo ou erro grosseiro da gravidade do prejuízo.
- Tipo de base: DISPOSITIVO
- Base: Decreto 9.830/2019, art. 12, § 5º (fonte F3 do adendo do D1; adendo do D1, seção 4.3); https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d9830.htm; consulta 20/10/2026; trecho: “O montante do dano ao erário, ainda que expressivo, não poderá, por si só, ser elemento para caracterizar o erro grosseiro ou o dolo.”; nota: a cena não nomeia órgão do Legislativo e o item não julga o alcance do Decreto (alerta P3)
- Mecanismo: Item C redigido para parecer E (C3)
- Difere de: Nenhum canônico da folha julga o art. 12 do Decreto 9.830 (D1-57 e D1-58 julgam a LINDB, art. 28); este item julga o § 5º (montante do dano).
- Marcas: TS=não; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D1-R10** (folha 2.2) — AUTORAL — QA PENDENTE [TS]
- itemEdital: P1-DA-2.2
- Ponto de julgamento: A2.2-16 — Decreto 9.830, art. 17 — o art. 12 não afasta sanções disciplinares, inclusive por ação ou omissão culposas de natureza leve (item troca por afasta)
- Formato: PAR
- Moldura: N
- Aderência: direta
- Gabarito: E
- Justificativa (linha 1): O art. 17 do Decreto 9.830 dispõe que o disposto no art. 12 não afasta a possibilidade de aplicação de sanções previstas em normas disciplinares, inclusive nos casos de ação ou de omissão culposas de natureza leve.
- Justificativa (linha 2): O item troca ‘não afasta’ por ‘afasta’; a tentação é estender à sanção disciplinar a exigência de dolo ou erro grosseiro do art. 12.
- Tipo de base: DISPOSITIVO
- Base: Decreto 9.830/2019, art. 17 (fonte F3 do adendo do D1; adendo do D1, seção 4.3); https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d9830.htm; consulta 20/10/2026; trecho: “não afasta a possibilidade de aplicação de sanções previstas em normas disciplinares, inclusive nos casos de ação ou de omissão culposas de natureza leve”; nota: o item julga só o art. 17 e não combina a responsabilização do art. 12 numa mesma afirmação com a sanção disciplinar (alerta P4)
- Mecanismo: Inversão de definição, de polaridade ou de relação (E2)
- Troca: não afasta → afasta (art. 17)
- Difere de: D1-58 porque este julga a LINDB, art. 28, caput (responsabilidade pessoal, com a troca por culpa, ainda que leve); aqui se julga a sanção disciplinar do Decreto 9.830, art. 17.
- Marcas: TS=sim; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D1-R11** (folha 2.2) — AUTORAL — QA PENDENTE [TS]
- itemEdital: P1-DA-2.2
- Ponto de julgamento: A2.2-20 — Lei 14.133, art. 53, caput — ao final da fase preparatória, o órgão de assessoramento jurídico realiza controle prévio de legalidade (item troca prévio por posterior)
- Formato: SIT
- Moldura: N
- Aderência: direta
- Gabarito: E
- Justificativa (linha 1): O art. 53, caput, determina que, ao final da fase preparatória, o processo licitatório seguirá para o órgão de assessoramento jurídico da Administração, que realizará controle prévio de legalidade mediante análise jurídica da contratação.
- Justificativa (linha 2): O item troca ‘prévio’ por ‘posterior’; a tentação é supor que a análise jurídica ocorra depois de fechada a contratação.
- Tipo de base: DISPOSITIVO
- Base: Lei 14.133/2021, art. 53, caput (fonte F4 do adendo do D1; adendo do D1, seção 4.4); https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm; consulta 20/10/2026; trecho: “o processo licitatório seguirá para o órgão de assessoramento jurídico da Administração, que realizará controle prévio de legalidade mediante análise jurídica da contratação”; nota: reconfirmação de 20/10/2026 do Anexo N do D5; nenhum item do D5 usa o art. 53 (alerta P5)
- Mecanismo: Inversão de definição, de polaridade ou de relação (E2)
- Troca: controle prévio de legalidade → controle posterior de legalidade (art. 53, caput)
- Difere de: Nenhum canônico da folha julga a Lei 14.133 (D1-53 a D1-60); D1-R06 e D1-R07 julgam o art. 10, e D1-R12, o art. 72, III.
- Marcas: TS=sim; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D1-R12** (folha 2.2) — AUTORAL — QA PENDENTE
- itemEdital: P1-DA-2.2
- Ponto de julgamento: A2.2-23 — Lei 14.133, art. 72, III — o processo de contratação direta é instruído com parecer jurídico e pareceres técnicos, se for o caso
- Formato: SIT
- Moldura: N
- Aderência: direta
- Gabarito: C
- Justificativa (linha 1): O art. 72, III, exige que o processo de contratação direta, que compreende a inexigibilidade e a dispensa de licitação, seja instruído com parecer jurídico e pareceres técnicos, se for o caso, que demonstrem o atendimento dos requisitos exigidos.
- Justificativa (linha 2): O item reproduz o inciso sem troca; a tentação é supor que a contratação direta, por dispensar a licitação, dispense também a instrução com pareceres.
- Tipo de base: DISPOSITIVO
- Base: Lei 14.133/2021, art. 72, caput e III (fonte F4 do adendo do D1; adendo do D1, seção 4.4); https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm; consulta 20/10/2026; trecho: “parecer jurídico e pareceres técnicos, se for o caso, que demonstrem o atendimento dos requisitos exigidos”; nota: reconfirmação de 20/10/2026 do Anexo N do D5; o D5 usa só o art. 72, VI (folha 10.1)
- Mecanismo: Item C redigido para parecer E (C3)
- Difere de: Nenhum canônico da folha julga a Lei 14.133 (D1-53 a D1-60); fora da folha, o D5 usa o art. 72, VI, e não o inciso III (adendo do D1, tabela 3.1).
- Marcas: TS=não; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

Folha 6.4 — Requisitos para a demonstração da responsabilidade do Estado

**D3-R14** (folha 6.4) — AUTORAL — QA PENDENTE
- itemEdital: P1-DA-6.4
- Ponto de julgamento: A6.4-17 — Lei 8.987, art. 25, caput — a concessionária responde por todos os prejuízos causados ao poder concedente, aos usuários ou a terceiros
- Formato: SUJ
- Moldura: N
- Aderência: direta
- Gabarito: C
- Justificativa (linha 1): O art. 25, caput, da Lei 8.987 incumbe à concessionária a execução do serviço concedido e a faz responder por todos os prejuízos causados ao poder concedente, aos usuários ou a terceiros.
- Justificativa (linha 2): O item mantém o sujeito certo (a concessionária) e o termo ‘todos’, literal do dispositivo; a tentação é restringir a responsabilidade aos prejuízos dos usuários ou transferi-la ao poder concedente.
- Tipo de base: DISPOSITIVO
- Base: Lei 8.987/1995, art. 25, caput (fonte A4; adendo do D3, seção 4.4); https://www.planalto.gov.br/ccivil_03/leis/l8987compilada.htm; consulta 20/10/2026; trecho: “cabendo-lhe responder por todos os prejuízos causados ao poder concedente, aos usuários ou a terceiros”; nota: o item não usa a parte final do caput (fiscalização que não exclui nem atenua a responsabilidade), reservada ao D3-R28 (folha 6.5, leva 3)
- Mecanismo: Reprodução próxima do texto normativo (C2)
- Difere de: D3-59 porque este julga o art. 43 do Código Civil (pessoas jurídicas de direito público interno e dano a terceiros); aqui se julga o art. 25 da Lei 8.987 (responsabilidade da concessionária).
- Marcas: TS=não; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D3-R15** (folha 6.4) — AUTORAL — QA PENDENTE
- itemEdital: P1-DA-6.4
- Ponto de julgamento: A6.4-05 — CC, art. 186 — há ato ilícito ainda que o dano seja exclusivamente moral
- Formato: DEF
- Moldura: N
- Aderência: direta
- Gabarito: C
- Justificativa (linha 1): O art. 186 do Código Civil define como ato ilícito o de quem, por ação ou omissão voluntária, negligência ou imprudência, viola direito e causa dano a outrem, ainda que exclusivamente moral.
- Justificativa (linha 2): O item julga só a locução ‘ainda que exclusivamente moral’, sem afirmar que ela basta; a tentação é supor que apenas o dano material caracterize o ato ilícito (alerta A2: sem afirmar efeito de decisão do STF).
- Tipo de base: DISPOSITIVO
- Base: CC, art. 186 (fonte A2; adendo do D3, seção 4.2); https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm; consulta 20/10/2026; trecho: “violar direito e causar dano a outrem, ainda que exclusivamente moral, comete ato ilícito”; nota: compilado traz “Vide ADI nº 7055” e “Vide ADI nº 6792”; nenhum item afirma efeito de decisão do STF (alerta A2)
- Mecanismo: Reprodução próxima do texto normativo (C2)
- Difere de: D3-R02 e D3-R05 (folha 6.3) porque estes julgam a omissão voluntária e a negligência e a imprudência do art. 186; aqui se julga o dano exclusivamente moral (A6.4-05). Nenhum canônico da 6.4 julga o art. 186.
- Marcas: TS=não; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D3-R16** (folha 6.4) — AUTORAL — QA PENDENTE [TS]
- itemEdital: P1-DA-6.4
- Ponto de julgamento: A6.4-01 — CF, art. 5º, V — é assegurada indenização por dano material, moral ou à imagem (item exclui o dano à imagem)
- Formato: APL
- Moldura: S — órgão/servidor do Poder Legislativo da União — fecho: neutro
- Aderência: direta
- Gabarito: E
- Justificativa (linha 1): O art. 5º, V, da CF assegura o direito de resposta, proporcional ao agravo, além da indenização por dano material, moral ou à imagem.
- Justificativa (linha 2): O item exclui o dano à imagem do rol da indenização, mantendo o direito de resposta e os danos material e moral; a tentação é supor que a imagem tenha tutela apenas no inciso X.
- Tipo de base: DISPOSITIVO
- Base: CF, art. 5º, V (fonte A1; adendo do D3, seção 4.1); https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm; consulta 20/10/2026; trecho: “é assegurado o direito de resposta, proporcional ao agravo, além da indenização por dano material, moral ou à imagem”; nota: redação original (promulgação, 5.10.1988); a cena nomeia “servidor de órgão do Poder Legislativo da União” e a norma citada é constitucional, sem regime próprio da Câmara
- Mecanismo: Alteração do comando normativo (E3)
- Troca: indenização por dano material, moral ou à imagem → indenização por dano material ou moral, mas não por dano à imagem (art. 5º, V)
- Difere de: D3-58 porque este julga os elementos extraídos do art. 37, § 6º (conduta do agente nessa qualidade e dano a terceiro); aqui se julga a abrangência do dano indenizável no art. 5º, V. Nota ao simulado: D3-R16 e D3-R21 (art. 5º, V e X).
- Marcas: TS=sim; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D3-R17** (folha 6.4) — AUTORAL — QA PENDENTE
- itemEdital: P1-DA-6.4
- Ponto de julgamento: A6.4-06 — CC, art. 927, parágrafo único — há obrigação de reparar o dano, independentemente de culpa, quando a atividade normalmente desenvolvida pelo autor do dano implicar, por sua natureza, risco para os direitos de outrem
- Formato: SIT
- Moldura: N
- Aderência: direta
- Gabarito: C
- Justificativa (linha 1): O art. 927, parágrafo único, do CC prevê a obrigação de reparar o dano, independentemente de culpa, nos casos especificados em lei ou quando a atividade normalmente desenvolvida pelo autor do dano implicar, por sua natureza, risco para os direitos de outrem.
- Justificativa (linha 2): O item aplica a segunda hipótese do parágrafo a uma empresa, sem pôr o Estado em cena (alertas A2 e A11); a tentação é exigir culpa em todo dever de reparar.
- Tipo de base: DISPOSITIVO
- Base: CC, art. 927, parágrafo único (fonte A2; adendo do D3, seção 4.2); https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm; consulta 20/10/2026; trecho: “independentemente de culpa,” […] “quando a atividade normalmente desenvolvida pelo autor do dano implicar, por sua natureza, risco para os direitos de outrem”; nota: o item não afirma o regime da responsabilidade do Estado nem a teoria do risco (alertas A2 e A11)
- Mecanismo: Reprodução próxima do texto normativo (C2)
- Difere de: D3-55 e D3-56 porque estes julgam, em base doutrinária, o nexo de causalidade e o rol de requisitos da responsabilidade do Estado; aqui se julga a letra do art. 927, parágrafo único, do Código Civil, sobre empresa e risco da atividade.
- Marcas: TS=não; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D3-R18** (folha 6.4) — AUTORAL — QA PENDENTE [TS]
- itemEdital: P1-DA-6.4
- Ponto de julgamento: A6.4-13 — Lei 8.112, art. 122, § 3º — a obrigação de reparar o dano estende-se aos sucessores até o limite do valor da herança recebida (item troca por sem limite)
- Formato: APL
- Moldura: S — órgão/servidor do Poder Legislativo da União — fecho: neutro
- Aderência: parcial
- Gabarito: E
- Justificativa (linha 1): O art. 122, § 3º, da Lei 8.112 dispõe que a obrigação de reparar o dano estende-se aos sucessores e contra eles será executada, até o limite do valor da herança recebida.
- Justificativa (linha 2): O item retira o limite do valor da herança recebida, mantendo a extensão aos sucessores; a tentação é supor que a obrigação se transmita integralmente, como dívida do falecido.
- Tipo de base: DISPOSITIVO
- Base: Lei 8.112/1990, art. 122, § 3º (fonte A3; adendo do D3, seção 4.3); https://www.planalto.gov.br/ccivil_03/leis/l8112compilado.htm; consulta 20/10/2026; trecho: “A obrigação de reparar o dano estende-se aos sucessores e contra eles será executada, até o limite do valor da herança recebida”; nota: pertinência parcial (regime do servidor; alerta A1); o item nomeia a lei e o sujeito e não afirma regime próprio da Câmara; ordinal “§ 3o” no original
- Mecanismo: Alteração do comando normativo (E3)
- Troca: até o limite do valor da herança recebida → sem limite de valor (art. 122, § 3º)
- Difere de: Nenhum canônico da 6.4 julga a Lei 8.112; D3-R20 julga o art. 122, § 2º (regresso), e D3-R06, R09 e R12 (folha 6.3), o art. 124 e o caput do art. 122. Nota ao simulado: D3-R18 e D3-R20 (mesma lei, mesma moldura e mesmo cenário de servidor).
- Marcas: TS=sim; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D3-R19** (folha 6.4) — AUTORAL — QA PENDENTE [TS]
- itemEdital: P1-DA-6.4
- Ponto de julgamento: A6.4-08 — CC, art. 944, caput — a indenização mede-se pela extensão do dano (item troca por gravidade da culpa do agente)
- Formato: APL
- Moldura: S — órgão/servidor do Poder Legislativo da União — fecho: neutro
- Aderência: direta
- Gabarito: E
- Justificativa (linha 1): O art. 944, caput, do Código Civil dispõe que a indenização mede-se pela extensão do dano.
- Justificativa (linha 2): O item troca ‘extensão do dano’ por ‘gravidade da culpa’; a tentação é medir a indenização pelo grau de culpa de quem causou o dano.
- Tipo de base: DISPOSITIVO
- Base: CC, art. 944, caput (fonte A2; adendo do D3, seção 4.2); https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm; consulta 20/10/2026; trecho: “A indenização mede-se pela extensão do dano.”; nota: o parágrafo único do art. 944 (redução equitativa) não é usado
- Mecanismo: Troca de conceito vizinho (E1)
- Troca: extensão do dano → gravidade da culpa do particular (art. 944, caput)
- Difere de: D3-56 porque este julga o rol doutrinário de requisitos da responsabilidade do Estado (conduta, dano, nexo causal e culpa da pessoa jurídica); aqui se julga a medida da indenização (art. 944, caput). Nota ao simulado: D3-R19 e D3-R34 (art. 944, caput e parágrafo único, na 6.5).
- Marcas: TS=sim; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D3-R20** (folha 6.4) — AUTORAL — QA PENDENTE
- itemEdital: P1-DA-6.4
- Ponto de julgamento: A6.4-12 — Lei 8.112, art. 122, § 2º — tratando-se de dano causado a terceiros, o servidor responde perante a Fazenda Pública, em ação regressiva
- Formato: APL
- Moldura: S — órgão/servidor do Poder Legislativo da União — fecho: neutro
- Aderência: parcial
- Gabarito: C
- Justificativa (linha 1): O art. 122, § 2º, da Lei 8.112 dispõe que, tratando-se de dano causado a terceiros, responderá o servidor perante a Fazenda Pública, em ação regressiva.
- Justificativa (linha 2): O item reproduz o parágrafo sem troca, nomeia a lei e o sujeito (o servidor) e não afirma o regime da responsabilidade do Estado (alerta A1); a tentação é inverter os polos da ação regressiva, como se o servidor a movesse contra a Fazenda Pública.
- Tipo de base: DISPOSITIVO
- Base: Lei 8.112/1990, art. 122, § 2º (fonte A3; adendo do D3, seção 4.3); https://www.planalto.gov.br/ccivil_03/leis/l8112compilado.htm; consulta 20/10/2026; trecho: “Tratando-se de dano causado a terceiros, responderá o servidor perante a Fazenda Pública, em ação regressiva.”; nota: pertinência parcial (regime do servidor; alerta A1); C com moldura em par com um E com moldura além da cota da folha (R3 da T-122); ordinal “§ 2o” no original
- Mecanismo: Reprodução próxima do texto normativo (C2)
- Difere de: D3-54 porque este julga a posição do dolo e da culpa na cláusula do regresso do art. 37, § 6º, da CF; aqui se julga a letra do art. 122, § 2º, da Lei 8.112 (o servidor responde perante a Fazenda Pública, em ação regressiva).
- Marcas: TS=não; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

**D3-R21** (folha 6.4) — AUTORAL — QA PENDENTE
- itemEdital: P1-DA-6.4
- Ponto de julgamento: A6.4-02 — CF, art. 5º, X — a violação da intimidade, da vida privada, da honra e da imagem assegura indenização pelo dano material ou moral
- Formato: DEF
- Moldura: N
- Aderência: direta
- Gabarito: C
- Justificativa (linha 1): O art. 5º, X, da CF declara invioláveis a intimidade, a vida privada, a honra e a imagem das pessoas e assegura o direito a indenização pelo dano material ou moral decorrente de sua violação.
- Justificativa (linha 2): O item reproduz a garantia sem troca; a tentação é confundi-la com o inciso V, que alcança o dano material, moral ou à imagem, e marcar errado.
- Tipo de base: DISPOSITIVO
- Base: CF, art. 5º, X (fonte A1; adendo do D3, seção 4.1); https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm; consulta 20/10/2026; trecho: “são invioláveis a intimidade, a vida privada, a honra e a imagem das pessoas” […] “assegurado o direito a indenização pelo dano material ou moral”; nota: redação original (promulgação, 5.10.1988); o segundo trecho é cortado antes de “decorrente de sua violação”, que o item mantém, por limite de 25 palavras
- Mecanismo: Reprodução próxima do texto normativo (C2)
- Difere de: D3-R16 porque este julga o inciso V do art. 5º (dano material, moral ou à imagem, com o direito de resposta); aqui se julga o inciso X (violação da intimidade, da vida privada, da honra e da imagem). Nota ao simulado: D3-R16 e D3-R21.
- Marcas: TS=não; REVERIFICAR=não; VOLÁTIL=não; QA PENDENTE=sim

## 3. Proveniência

### 3.1 Fontes citadas (URL e data idênticas às do adendo; cópia do texto lido em saida/gcb/normativo_cache/)

| Fonte | Publicação ou norma | URL | Verificado em | Cópia gravada | Registro no adendo |
|---|---|---|---|---|---|
| F1 (adendo do D4) | TCU — Referencial Básico de Governança Organizacional, 3. ed., 2020 | https://portal.tcu.gov.br/data/files/FB/B6/FB/85/1CD4671023455957E18818A8/Referencial_basico_governanca_organizacional_3_edicao.pdf | 20/10/2026 | TCU_ReferencialGovernancaOrganizacional_3ed_2020_TRECHOS_2026-10-20.txt | D4_anexo_N_adendo_2026-10-20.md, seções 1 e 5 |
| F3 (adendo do D4) | Casa Civil da Presidência da República — Avaliação de Políticas Públicas: guia prático de análise ex post, v. 2, 2018 | https://www.gov.br/casacivil/pt-br/assuntos/governanca/comite-interministerial-de-governanca/arquivos/avaliacao-de-politicas-publicas-guia-pratico-de-analise-ex-post.pdf | 20/10/2026 | CasaCivil_AvaliacaoExPost_v2_2018_2026-10-20.txt | D4_anexo_N_adendo_2026-10-20.md, seções 1 e 5 |
| F10 (adendo do D4) | Controladoria-Geral da União — documento didático “Cadeia de valor da CGU” (sem data impressa) | https://repositorio.cgu.gov.br/bitstream/1/29544/10/documento_didatico_cadeia_valor.pdf | 20/10/2026 | CGU_CadeiaDeValor_doc_didatico_2026-10-20.txt | D4_anexo_N_adendo_2026-10-20.md, seções 1 e 5 |
| F1 (adendo do D1) | Lei 9.784/1999 (página principal) | https://www.planalto.gov.br/ccivil_03/leis/l9784.htm | 20/10/2026 | Lei_9784_1999_2026-10-20.txt | D1_anexo_N_adendo_2026-10-20.md, seções 1 e 4.1 |
| F3 (adendo do D1) | Decreto 9.830/2019 | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d9830.htm | 20/10/2026 | Decreto_9830_2019_2026-10-20.txt | D1_anexo_N_adendo_2026-10-20.md, seções 1 e 4.3 |
| F4 (adendo do D1) | Lei 14.133/2021 (página principal) | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm | 20/10/2026 | Lei_14133_2021_2026-10-20.txt | D1_anexo_N_adendo_2026-10-20.md, seções 1 e 4.4 |
| A1 (adendo do D3) | CF/1988, compilada | https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm | 20/10/2026 | CF_1988_compilada_2026-10-20.txt | D3_anexo_N_adendo_2026-10-20.md, seções 1 e 4.1 |
| A2 (adendo do D3) | Código Civil (Lei 10.406/2002), compilado | https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm | 20/10/2026 | Lei_10406_2002_CodigoCivil_compilada_2026-10-20.txt | D3_anexo_N_adendo_2026-10-20.md, seções 1 e 4.2 |
| A3 (adendo do D3) | Lei 8.112/1990, compilada | https://www.planalto.gov.br/ccivil_03/leis/l8112compilado.htm | 20/10/2026 | Lei_8112_1990_compilada_2026-10-20.txt | D3_anexo_N_adendo_2026-10-20.md, seções 1 e 4.3 |
| A4 (adendo do D3) | Lei 8.987/1995, compilada | https://www.planalto.gov.br/ccivil_03/leis/l8987compilada.htm | 20/10/2026 | Lei_8987_1995_compilada_2026-10-20.txt | D3_anexo_N_adendo_2026-10-20.md, seções 1 e 4.4 |

### 3.2 Tabela de proveniência: id → dispositivo/fonte → URL → verificado em

| id | folha | dispositivo ou referencial (ponto) | URL | verificado em (base) |
|---|---|---|---|---|
| D4-R19 | 8.4 | R77 e R78 — Casa Civil da Presidência da República, Avaliação de Políticas Públicas: guia prático de análise ex post, v. 2, 2018, p. 59 (Figura 1) (A8.4-21) | https://www.gov.br/casacivil/pt-br/assuntos/governanca/comite-interministerial-de-governanca/arquivos/avaliacao-de-politicas-publicas-guia-pratico-de-analise-ex-post.pdf | 20/10/2026 (adendo) |
| D4-R20 | 8.4 | R60 — TCU, Referencial Básico de Governança Organizacional, 3. ed., 2020, p. 48-49 (A8.4-02) | https://portal.tcu.gov.br/data/files/FB/B6/FB/85/1CD4671023455957E18818A8/Referencial_basico_governanca_organizacional_3_edicao.pdf | 20/10/2026 (adendo) |
| D4-R21 | 8.4 | R66 — Controladoria-Geral da União, documento didático Cadeia de valor da CGU (sem data impressa), p. 6 do PDF (sem numeração impressa) (A8.4-10) | https://repositorio.cgu.gov.br/bitstream/1/29544/10/documento_didatico_cadeia_valor.pdf | 20/10/2026 (adendo) |
| D4-R22 | 8.4 | R65 — Controladoria-Geral da União, documento didático Cadeia de valor da CGU (sem data impressa), p. 6 do PDF (sem numeração impressa) (A8.4-09) | https://repositorio.cgu.gov.br/bitstream/1/29544/10/documento_didatico_cadeia_valor.pdf | 20/10/2026 (adendo) |
| D4-R23 | 8.4 | R81 — Casa Civil da Presidência da República, Avaliação de Políticas Públicas: guia prático de análise ex post, v. 2, 2018, p. 41 (A8.4-25) | https://www.gov.br/casacivil/pt-br/assuntos/governanca/comite-interministerial-de-governanca/arquivos/avaliacao-de-politicas-publicas-guia-pratico-de-analise-ex-post.pdf | 20/10/2026 (adendo) |
| D4-R24 | 8.4 | R62 — TCU, Referencial Básico de Governança Organizacional, 3. ed., 2020, p. 82 (A8.4-05) | https://portal.tcu.gov.br/data/files/FB/B6/FB/85/1CD4671023455957E18818A8/Referencial_basico_governanca_organizacional_3_edicao.pdf | 20/10/2026 (adendo) |
| D4-R25 | 8.4 | R76 — Casa Civil da Presidência da República, Avaliação de Políticas Públicas: guia prático de análise ex post, v. 2, 2018, p. 59 (Figura 1) (A8.4-20) | https://www.gov.br/casacivil/pt-br/assuntos/governanca/comite-interministerial-de-governanca/arquivos/avaliacao-de-politicas-publicas-guia-pratico-de-analise-ex-post.pdf | 20/10/2026 (adendo) |
| D4-R26 | 8.4 | R67 — Controladoria-Geral da União, documento didático Cadeia de valor da CGU (sem data impressa), p. 7 do PDF (sem numeração impressa) (A8.4-11) | https://repositorio.cgu.gov.br/bitstream/1/29544/10/documento_didatico_cadeia_valor.pdf | 20/10/2026 (adendo) |
| D4-R27 | 8.4 | R80 e R79 — Casa Civil da Presidência da República, Avaliação de Políticas Públicas: guia prático de análise ex post, v. 2, 2018, p. 59 (Figura 1) (A8.4-24) | https://www.gov.br/casacivil/pt-br/assuntos/governanca/comite-interministerial-de-governanca/arquivos/avaliacao-de-politicas-publicas-guia-pratico-de-analise-ex-post.pdf | 20/10/2026 (adendo) |
| D4-R28 | 8.4 | R74 — Casa Civil da Presidência da República, Avaliação de Políticas Públicas: guia prático de análise ex post, v. 2, 2018, p. 41-42 (A8.4-18) | https://www.gov.br/casacivil/pt-br/assuntos/governanca/comite-interministerial-de-governanca/arquivos/avaliacao-de-politicas-publicas-guia-pratico-de-analise-ex-post.pdf | 20/10/2026 (adendo) |
| D1-R01 | 2.2 | Lei 9.784/1999, art. 42, § 2º — adendo do D1, seção 4.1 (A2.2-02) | https://www.planalto.gov.br/ccivil_03/leis/l9784.htm | 20/10/2026 (adendo) |
| D1-R02 | 2.2 | Decreto 9.830/2019, art. 12, § 1º — adendo do D1, seção 4.3 (A2.2-08) | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d9830.htm | 20/10/2026 (adendo) |
| D1-R13 | 2.2 | Decreto 9.830/2019, art. 12, § 2º — adendo do D1, seção 4.3 (A2.2-09) | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d9830.htm | 20/10/2026 (adendo) |
| D1-R04 | 2.2 | Decreto 9.830/2019, art. 12, § 3º — adendo do D1, seção 4.3 (A2.2-10) | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d9830.htm | 20/10/2026 (adendo) |
| D1-R05 | 2.2 | Lei 9.784/1999, art. 43 (× art. 42, § 1º) — adendo do D1, seção 4.1 (A2.2-03) | https://www.planalto.gov.br/ccivil_03/leis/l9784.htm | 20/10/2026 (adendo) |
| D1-R06 | 2.2 | Lei 14.133/2021, art. 10, caput — adendo do D1, seção 4.4 (A2.2-17) | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm | 20/10/2026 (adendo) |
| D1-R07 | 2.2 | Lei 14.133/2021, art. 10, § 1º, II — adendo do D1, seção 4.4 (A2.2-18) | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm | 20/10/2026 (adendo) |
| D1-R08 | 2.2 | Decreto 9.830/2019, art. 12, § 6º, primeira parte — adendo do D1, seção 4.3 (A2.2-13) | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d9830.htm | 20/10/2026 (adendo) |
| D1-R09 | 2.2 | Decreto 9.830/2019, art. 12, § 5º — adendo do D1, seção 4.3 (A2.2-12) | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d9830.htm | 20/10/2026 (adendo) |
| D1-R10 | 2.2 | Decreto 9.830/2019, art. 17 — adendo do D1, seção 4.3 (A2.2-16) | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d9830.htm | 20/10/2026 (adendo) |
| D1-R11 | 2.2 | Lei 14.133/2021, art. 53, caput — adendo do D1, seção 4.4 (A2.2-20) | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm | 20/10/2026 (adendo) |
| D1-R12 | 2.2 | Lei 14.133/2021, art. 72, caput e III — adendo do D1, seção 4.4 (A2.2-23) | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm | 20/10/2026 (adendo) |
| D3-R14 | 6.4 | Lei 8.987/1995, art. 25, caput — adendo do D3, seção 4.4 (A6.4-17) | https://www.planalto.gov.br/ccivil_03/leis/l8987compilada.htm | 20/10/2026 (adendo) |
| D3-R15 | 6.4 | CC, art. 186 — adendo do D3, seção 4.2 (A6.4-05) | https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm | 20/10/2026 (adendo) |
| D3-R16 | 6.4 | CF, art. 5º, V — adendo do D3, seção 4.1 (A6.4-01) | https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm | 20/10/2026 (adendo) |
| D3-R17 | 6.4 | CC, art. 927, parágrafo único — adendo do D3, seção 4.2 (A6.4-06) | https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm | 20/10/2026 (adendo) |
| D3-R18 | 6.4 | Lei 8.112/1990, art. 122, § 3º — adendo do D3, seção 4.3 (A6.4-13) | https://www.planalto.gov.br/ccivil_03/leis/l8112compilado.htm | 20/10/2026 (adendo) |
| D3-R19 | 6.4 | CC, art. 944, caput — adendo do D3, seção 4.2 (A6.4-08) | https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm | 20/10/2026 (adendo) |
| D3-R20 | 6.4 | Lei 8.112/1990, art. 122, § 2º — adendo do D3, seção 4.3 (A6.4-12) | https://www.planalto.gov.br/ccivil_03/leis/l8112compilado.htm | 20/10/2026 (adendo) |
| D3-R21 | 6.4 | CF, art. 5º, X — adendo do D3, seção 4.1 (A6.4-02) | https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm | 20/10/2026 (adendo) |
## 4. Contagens

Refeitas na v2 e conferidas por script (python3 -I) sobre este arquivo gravado (seções 1 e 2, relido do disco), sobre as linhas dos canônicos em saida/gcb/D4_v2_1.md (D4-27 a D4-33, e o lote D4 inteiro para os conjuntos K), saida/gcb/D1_v2.md (D1-53 a D1-60) e saida/gcb/D3_v2_1.md (D3-51 a D3-56, D3-58 e D3-59, e o lote D3 inteiro para a moldura e a abertura), sobre saida/gcb/DA_reforco_leva1_v2.md (itens aceitos da leva 1) e sobre o CSV saida/banco/moldura_ce_itens_2026-10-20.csv (moldura dos canônicos; o script moldura_ce.py não foi executado, para não reescrever o CSV; os regex dele foram copiados para classificar os itens novos). Ordem do arquivo: folhas 8.4, 2.2 e 6.4; dentro de cada folha, a ordem final da ficha (seção 8.3.4). Ordem dos canônicos na folha acumulada: a do pacote v1.13, isto é, a ordem numérica dos ids.

### 4.1 Por folha (canônicos + leva)

| Folha | Itens (can. + leva 1 + leva 2 = total) | C/E canônicos | C/E leva 1 | C/E leva 2 | C/E folha | Formatos canônicos (DEF/SUJ/SIT/NUM/PAR/APL) | Formatos da folha | Maior formato (teto 6 em 20) | Moldura C/E (can. + leva 1 + leva 2) | Diretos (can. + leva) / parciais | VOLÁTIL | [TS] (E / C), can. + levas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8.4 | 7 + 3 + 10 = 20 | 4/3 | 0/3 | 6/4 | 10/10 | 2/0/2/0/2/1 | 5/1/4/0/5/5 | DEF 5 (25,0% de 20; 25,0% dos 20 itens) | 2/3 (5 com moldura; teto 6) | 10 + 10 = 20 / 0 | 0 | 10/1 |
| 2.2 | 8 + 0 + 12 = 20 | 4/4 | 0/0 | 6/6 | 10/10 | 4/0/0/1/3/0 | 6/2/5/1/6/0 | DEF 6 e PAR 6 (30,0% de 20; 30,0% dos 20 itens) | 0/0 (0 com moldura; teto 6) | 8 + 12 = 20 / 0 | 0 | 10/0 |
| 6.4 | 8 + 0 + 8 = 16 | 3/5 | 0/0 | 5/3 | 8/8 | 3/0/2/0/2/1 | 5/1/3/0/2/5 | DEF 5 (25,0% de 20; 31,2% dos 16 itens) | 2/3 (5 com moldura; teto 6) | 8 + 6 = 14 / 2 | 0 | 7/1 |

Teto de formato = ⌊0,3 × 20⌋ = 6 por formato na folha final de 20. A 8.4 e a 2.2 chegam a 20 nesta leva; a 6.4 chega a 16 (a leva 3 acrescenta 4 itens, 0/2/0/2/0/0 em DEF/SUJ/SIT/NUM/PAR/APL, segundo a ficha 8.3.5). Os canônicos são tratados como diretos (partida da ficha, 8.3.6). Piso de 10 diretos: 8.4 = 20; 2.2 = 20; 6.4 = 14 (de 16; os 2 parciais são D3-R18 e D3-R20). Formatos dos canônicos: 8.4 e 6.4 pela ficha (8.3.5; os arquivos canônicos usam rótulos próprios), 2.2 pela decisão da GCB (ficha 8.2, item 1). DEF e PAR da 2.2 em 6 (30,0% cada): no teto; nenhum outro DEF nem PAR foi declarado na folha (o D1-R13 é DEF, como indica o parecer R1, seção 3; o DEF da folha era 5 e o SUJ, 3).

### 4.2 Leva (30 itens)

- Gabarito: 17 C / 13 E (56,7% de C); faixa da ficha (seção 1, regra 6): 12 a 18 C em 30 itens — CONFERE.
  - Folha 8.4: leva 6 C / 4 E; folha com os canônicos e a leva 1 10 C / 10 E (50,0% de C).
  - Folha 2.2: leva 6 C / 6 E; folha com os canônicos e a leva 1 10 C / 10 E (50,0% de C).
  - Folha 6.4: leva 5 C / 3 E; folha com os canônicos e a leva 1 8 C / 8 E (50,0% de C; fecha com 2 C / 2 E na leva 3).
- [TS]: 13 (todos com gabarito E e nenhum com gabarito C; nenhum elemento-isca planejado na ficha, seção 8.3.4); [TS] com gabarito C: 0 por folha.
- Moldura do Legislativo (S) na leva: 2 C / 3 E (ficha, seção 8.3.6: 2 C e 3 E); por folha: 8.4 1/0; 2.2 0/0; 6.4 1/3.
- VOLÁTIL = 0 e REVERIFICAR = 0 em todos os itens; rótulo AUTORAL e QA PENDENTE em todos; valor em reais: 0 ocorrências de “R$”; “NGP” em enunciado: 0; em justificativa: 0; “exceto” em enunciado: 0.
- Autor nomeado em enunciado (busca pelos nomes do referencial: Porter, Osborne, Bouckaert, Silvestre, Cavalcante, Martins, Mazzucato, Moore, Bryson, Hood, Pollitt, Kettl, Peters, Matias-Pereira, Marcos Marques): nenhum; órgãos nomeados (TCU, CGU, Casa Civil) são admitidos.

### 4.3 Teste de sequência (ficha, seção 1, regra 6; seções 7.3 e 8.3.7)

Regras: nenhuma sequência de 4 ou mais gabaritos iguais; nenhuma alternância estrita C/E por mais de 4 itens seguidos; nenhum trecho que se repita com período p de 2 a 8 por max(8, 2p) itens seguidos (a coluna dá o maior bloco de cada período e o limite; o bloco falha se chegar ao limite). O mesmo teste vale para a sequência de [TS] (T = com [TS]; n = sem). A coluna “acumulada” põe os canônicos da folha (ordem numérica dos ids = ordem do pacote), os itens da leva 1 (8.4) e os itens desta leva, nessa ordem. Legados aceitos pela ficha (seção 8.2, item 7, e seção 7.3): 2.2, alternância de 6 nas posições 1 a 6 (gabarito e [TS]); 6.4, bloco de período 3 com 8 itens nas posições 1 a 8 (gabarito); 8.4, bloco de período 3 com 9 itens nas posições 1 a 9 ([TS]).

| Escopo | Sequência | Maior corrida | Maior alternância | Bloco repetido, período 2 a 8 (maior bloco / limite, em itens) | Resultado |
|---|---|---|---|---|---|
| Folha 8.4 (leva 2), gabarito | CCECCEECEC | 2 | 4 | p2 4/8; p3 6/8; p4 6/8; p5 6/10; p6 9/12; p7 8/14; p8 9/16 | APROVADO |
| Folha 8.4 acumulada (20 itens), gabarito | CEECECCEEECCECCEECEC | 3 | 4 | p2 4/8; p3 7/8; p4 6/8; p5 9/10; p6 9/12; p7 10/14; p8 14/16 | APROVADO |
| Folha 8.4 (leva 2), [TS] | nnTnnTTnTn | 2 | 4 | p2 4/8; p3 6/8; p4 6/8; p5 6/10; p6 9/12; p7 8/14; p8 9/16 | APROVADO |
| Folha 8.4 acumulada (20 itens), [TS] | nTTnTTnTTTnnTnnTTnTn | 3 | 4 | p2 4/8; p3 9/8; p4 7/8; p5 7/10; p6 9/12; p7 10/14; p8 11/16 | REPROVADO no teste da folha inteira, só no legado aceito (posições 1 a 9; ficha, seções 7.3 e 8.2 item 7); sem as posições 1 a 9: APROVADO; as métricas que reprovam (período 3 9) são idênticas sem os itens da leva 2, isto é, a leva não cria nem estende a falha: sim |
| Folha 2.2 (leva 2), gabarito | CCEEECECCEEC | 3 | 4 | p2 4/8; p3 5/8; p4 6/8; p5 6/10; p6 9/12; p7 11/14; p8 9/16 | APROVADO |
| Folha 2.2 acumulada (20 itens), gabarito | CECECEECCCEEECECCEEC | 3 | 6 | p2 6/8; p3 5/8; p4 6/8; p5 8/10; p6 9/12; p7 11/14; p8 11/16 | REPROVADO no teste da folha inteira, só no legado aceito (posições 1 a 6; ficha, seções 7.3 e 8.2 item 7); sem as posições 1 a 6: APROVADO; as métricas que reprovam (alternância 6) são idênticas sem os itens da leva 2, isto é, a leva não cria nem estende a falha: sim |
| Folha 2.2 (leva 2), [TS] | nnTTTnTnnTTn | 3 | 4 | p2 4/8; p3 5/8; p4 6/8; p5 6/10; p6 9/12; p7 11/14; p8 9/16 | APROVADO |
| Folha 2.2 acumulada (20 itens), [TS] | nTnTnTTnnnTTTnTnnTTn | 3 | 6 | p2 6/8; p3 5/8; p4 6/8; p5 8/10; p6 9/12; p7 11/14; p8 11/16 | REPROVADO no teste da folha inteira, só no legado aceito (posições 1 a 6; ficha, seções 7.3 e 8.2 item 7); sem as posições 1 a 6: APROVADO; as métricas que reprovam (alternância 6) são idênticas sem os itens da leva 2, isto é, a leva não cria nem estende a falha: sim |
| Folha 6.4 (leva 2), gabarito | CCECEECC | 2 | 4 | p2 4/8; p3 5/8; p4 5/8; p5 6/10; p6 8/12; p7 8/14; p8 0/16 | APROVADO |
| Folha 6.4 acumulada (16 itens), gabarito | CEECEECECCECEECC | 2 | 4 | p2 4/8; p3 8/8; p4 5/8; p5 8/10; p6 9/12; p7 8/14; p8 13/16 | REPROVADO no teste da folha inteira, só no legado aceito (posições 1 a 8; ficha, seções 7.3 e 8.2 item 7); sem as posições 1 a 8: APROVADO; as métricas que reprovam (período 3 8) são idênticas sem os itens da leva 2, isto é, a leva não cria nem estende a falha: sim |
| Folha 6.4 (leva 2), [TS] | nnTnTTnn | 2 | 4 | p2 4/8; p3 5/8; p4 5/8; p5 6/10; p6 8/12; p7 8/14; p8 0/16 | APROVADO |
| Folha 6.4 acumulada (16 itens), [TS] | nTnTTTnTnnTnTTnn | 3 | 4 | p2 4/8; p3 6/8; p4 7/8; p5 8/10; p6 9/12; p7 9/14; p8 11/16 | APROVADO |
| Leva 2 inteira (30), gabarito | CCECCEECECCCEEECECCEECCCECEECC | 3 | 4 | p2 4/8; p3 6/8; p4 7/8; p5 8/10; p6 10/12; p7 12/14; p8 14/16 | APROVADO |
| Leva 2 inteira (30), [TS] | nnTnnTTnTnnnTTTnTnnTTnnnTnTTnn | 3 | 4 | p2 4/8; p3 6/8; p4 7/8; p5 8/10; p6 10/12; p7 12/14; p8 14/16 | APROVADO |

Plano da ficha (seção 8.3.7), conferido contra o arquivo: gabarito da 8.4 CCECCEECEC, da 2.2 CCEEECECCEEC e da 6.4 CCECEECC; [TS] da 8.4 nnTnnTTnTn, da 2.2 nnTTTnTnnTTn e da 6.4 nnTnTTnn. Os itens da leva ficam na ordem do plano, sem troca de posição. D4-R19 é C sem [TS] e fecha a corrida E E E da 8.4 acumulada (seção 7.3). Nenhum desvio novo de sequência.

### 4.4 Moldura acumulada de DA e conjuntos (ficha, seções 1 regra 11, 7.4 e 8.3.6)

| Conjunto | Canônicos (C/E) | Leva 1 (C/E) | Partida da leva 2 | Leva 2 (C/E) | Depois da leva 2 | %C | Referência da ficha |
|---|---|---|---|---|---|---|---|
| DA com moldura (34 folhas + canônicos) | 44/9 | 2/9 | 46/18 | 2/3 | 48/21 | 69,6% | 46/18 → 48/21 (69,6%) |
| D4 K1 — moldura do Legislativo | 12/0 | 1/6 | 13/6 | 1/0 | 14/6 | 70,0% | 13/6 → 14/6 (70,0%) |
| D4 K2 — fecho de acerto | 5/0 | 2/6 | 7/6 | 0/1 | 7/7 | 50,0% | 7/6 → 7/7 (50,0%) |
| D4 K3 — “pós-NPM” | 4/0 | 1/4 | 5/4 | 0/0 | 5/4 | 55,6% | 5/4, sem item novo |
| D4 K4 — abertura “Considere que” | 21/8 | 2/9 | 23/17 | 2/1 | 25/18 | 58,1% | 23/17 → 25/18 (58,1%) |
| D4 fecho neutro (“Nessa situação, é correto afirmar que”) | 0/0 | 0/3 | 0/3 | 2/0 | 2/3 | 40,0% | 0/3 → 2/3 (40,0%) |
| D4 contraste “, e não” | 0/0 | 0/2 | 0/2 | 1/0 | 1/2 | 33,3% | 0/2 → 1/2 |
| D3 — moldura do Legislativo | 6/1 | 1/3 | 7/4 | 1/3 | 8/7 | 53,3% | 7/4 → 8/7 (53,3%) |

Canônicos de DA e do D3: coluna “moldura” do CSV da T-122 (DA 44/9; D3 6/1; D4 12/0). Canônicos dos conjuntos K2, K3, K4, fecho neutro e contraste: leitura dos enunciados do D4_v2_1.md por regex (K2: “a afirmação do expositor é correta” e “ele estará correto ao”; fecho neutro: “Nessa situação, é correto afirmar que”). Leva 1: relida de DA_reforco_leva1_v2.md. Moldura por folha (canônicos + leva 1 + leva 2): 8.4 2/3 (5 itens com moldura), 6.4 2/3 (5), 2.2 0/0; máximo 6 por folha — CONFERE. Classificador da moldura (regex do moldura_ce.py) sobre os 30 itens: declarada S ⇔ classificada S, desacordos: nenhum. Todos os itens com moldura S declaram o tipo; nenhum item com moldura trata a moldura como razão do gabarito; E com moldura: 3, todos com troca de elemento literal declarada no campo Troca. R3 (C com moldura só em par 1:1 com um E com moldura além da cota, na mesma folha): o D4-R20 (8.4) é par do E com moldura além da cota da leva 1 (D4-R16); o D3-R20 (6.4) é par de um dos E com moldura além da cota da folha (D3-R16, D3-R18 e D3-R19: 3 E entregues para a cota de 1).

### 4.5 Pontos de julgamento da leva

| id | folha | ponto (código — base — proposição julgada) |
|---|---|---|
| D4-R19 | 8.4 | A8.4-21 — R77 (contraste R78) — processos são as ações que combinam os recursos disponíveis para produzir bens e serviços, e não os bens e serviços entregues, que são os produtos |
| D4-R20 | 8.4 | A8.4-02 — R60 — entre as diretrizes para a boa governança do Referencial do TCU está apoiar e viabilizar a inovação para agregar valor público |
| D4-R21 | 8.4 | A8.4-10 — R66 (CGU) — no setor público em geral observa-se a inexistência de padrão para a representação da cadeia de valor (item troca por existência de padrão) |
| D4-R22 | 8.4 | A8.4-09 — R65 (CGU) — valor público está também associado ao grau de reconhecimento de atendimento ou satisfação por parte do cidadão ou de outro público específico |
| D4-R23 | 8.4 | A8.4-25 — R81 (Casa Civil) — a avaliação das relações entre insumos, processos e produtos também investiga a eficiência operacional e a economicidade |
| D4-R24 | 8.4 | A8.4-05 — R62 (TCU; o item não nomeia o autor) — a tecnologia está entre as atividades de apoio, e não entre as primárias (item troca por primárias) |
| D4-R25 | 8.4 | A8.4-20 — R76 (Casa Civil) — insumos: recursos do setor público, orçamentários ou não, necessários para atingir os objetivos da política (item troca por exclusivamente orçamentários) |
| D4-R26 | 8.4 | A8.4-11 — R67 (CGU) — a metodologia de gestão de processos fornece a estrutura para a elaboração da cadeia de valor, que auxilia o estabelecimento de objetivos estratégicos a partir da missão institucional |
| D4-R27 | 8.4 | A8.4-24 — R80 (contraste R79) — a mudança de mais longo prazo no problema, alinhada aos objetivos da política, é o impacto (item troca por resultados) |
| D4-R28 | 8.4 | A8.4-18 — R74 (Casa Civil) — as avaliações aprofundadas inserem-se na análise dos componentes da cadeia de valor das políticas públicas ou dos componentes do modelo lógico |
| D1-R01 | 2.2 | A2.2-02 — Lei 9.784, art. 42, § 2º — a dispensa do parecer obrigatório e não vinculante, com prosseguimento e decisão do processo, não prejudica a responsabilidade de quem se omitiu no atendimento |
| D1-R02 | 2.2 | A2.2-08 — Decreto 9.830, art. 12, § 1º — erro grosseiro é o manifesto, evidente e inescusável, praticado com culpa grave, com elevado grau de negligência, imprudência ou imperícia |
| D1-R13 | 2.2 | A2.2-09 — Decreto 9.830, art. 12, § 2º — não se configura dolo ou erro grosseiro se não restar comprovada, nos autos do processo de responsabilização, situação ou circunstância fática capaz de caracterizá-los (item troca: configura-se ainda que não reste comprovada) |
| D1-R04 | 2.2 | A2.2-10 — Decreto 9.830, art. 12, § 3º — o mero nexo de causalidade entre a conduta e o resultado danoso não implica responsabilização, salvo dolo ou erro grosseiro comprovado (item troca: o nexo implica) |
| D1-R05 | 2.2 | A2.2-03 — Lei 9.784, art. 43 (× art. 42, § 1º) — laudo técnico não entregue no prazo: o órgão de instrução solicita laudo a outro órgão equivalente (item troca: o processo não terá seguimento até a apresentação) |
| D1-R06 | 2.2 | A2.2-17 — Lei 14.133, art. 10, caput — quem agiu com estrita observância de parecer jurídico do art. 53, § 1º, e precisa defender-se tem representação promovida pela advocacia pública, a critério do agente |
| D1-R07 | 2.2 | A2.2-18 — Lei 14.133, art. 10, § 1º, II — a representação do caput não se aplica quando provas de atos ilícitos dolosos constarem dos autos (item troca dolosos por culposos) |
| D1-R08 | 2.2 | A2.2-13 — Decreto 9.830, art. 12, § 6º (primeira parte) — a responsabilização pela opinião técnica não se estende de forma automática ao decisor que a adotou como fundamento de decidir |
| D1-R09 | 2.2 | A2.2-12 — Decreto 9.830, art. 12, § 5º — o montante do dano ao erário, ainda que expressivo, não pode, por si só, caracterizar o erro grosseiro ou o dolo |
| D1-R10 | 2.2 | A2.2-16 — Decreto 9.830, art. 17 — o art. 12 não afasta sanções disciplinares, inclusive por ação ou omissão culposas de natureza leve (item troca por afasta) |
| D1-R11 | 2.2 | A2.2-20 — Lei 14.133, art. 53, caput — ao final da fase preparatória, o órgão de assessoramento jurídico realiza controle prévio de legalidade (item troca prévio por posterior) |
| D1-R12 | 2.2 | A2.2-23 — Lei 14.133, art. 72, III — o processo de contratação direta é instruído com parecer jurídico e pareceres técnicos, se for o caso |
| D3-R14 | 6.4 | A6.4-17 — Lei 8.987, art. 25, caput — a concessionária responde por todos os prejuízos causados ao poder concedente, aos usuários ou a terceiros |
| D3-R15 | 6.4 | A6.4-05 — CC, art. 186 — há ato ilícito ainda que o dano seja exclusivamente moral |
| D3-R16 | 6.4 | A6.4-01 — CF, art. 5º, V — é assegurada indenização por dano material, moral ou à imagem (item exclui o dano à imagem) |
| D3-R17 | 6.4 | A6.4-06 — CC, art. 927, parágrafo único — há obrigação de reparar o dano, independentemente de culpa, quando a atividade normalmente desenvolvida pelo autor do dano implicar, por sua natureza, risco para os direitos de outrem |
| D3-R18 | 6.4 | A6.4-13 — Lei 8.112, art. 122, § 3º — a obrigação de reparar o dano estende-se aos sucessores até o limite do valor da herança recebida (item troca por sem limite) |
| D3-R19 | 6.4 | A6.4-08 — CC, art. 944, caput — a indenização mede-se pela extensão do dano (item troca por gravidade da culpa do agente) |
| D3-R20 | 6.4 | A6.4-12 — Lei 8.112, art. 122, § 2º — tratando-se de dano causado a terceiros, o servidor responde perante a Fazenda Pública, em ação regressiva |
| D3-R21 | 6.4 | A6.4-02 — CF, art. 5º, X — a violação da intimidade, da vida privada, da honra e da imagem assegura indenização pelo dano material ou moral |

- Códigos de ponto: 30 itens, 30 códigos distintos; duplicatas entre si: nenhuma; códigos já usados na leva 1 (qualquer folha): nenhum.
- Conferência com a tabela da ficha (seção 8.3.4; ponto, formato, moldura S/N, gabarito, [TS], aderência e abertura CQ/DC, lidos da própria tabela por script): 29 de 30 linhas conferem; divergência: D1-R13, que substitui o D1-R03 por decisão do R1 (ponto A2.2-09 no lugar do A2.2-01 e formato DEF no lugar de SUJ; gabarito E, [TS], moldura N, aderência direta e abertura declarativa iguais). Os 11 AJ mudam só texto de enunciado, Troca e Justificativa, nenhum campo da tabela.
- R-ids da leva (D4): R60, R62, R65, R66, R67, R74, R76, R77, R78, R79, R80, R81. Interseção com os R-ids da leva 1: nenhuma. Interseção com os R-ids citados pelos canônicos da folha 8.4 (D4-27 a D4-33; campos Ponto e Base): nenhuma (canônicos: R16, R17, R18).
- Bases repetidas na mesma folha, com pontos distintos (dispositivo com elementos diferentes; o “Difere de” de cada item trata o caso): 2.2 Decreto 9.830, art. 12: D1-R02, D1-R04, D1-R08, D1-R09, D1-R13; 2.2 Lei 14.133, art. 10: D1-R06, D1-R07; 2.2 Lei 9.784, art. 42: D1-R01 (§ 2º) e D1-R05 (art. 43 × § 1º); 6.4 CF, art. 5º: D3-R16, D3-R21; 6.4 Lei 8.112, art. 122: D3-R18, D3-R20.
- Dispositivo do mesmo artigo também citado, nos campos Ponto ou Base, por canônicos do lote (varredura por script; informativa, cada caso já tem “Difere de”): D1-R01 (Lei 9.784, art. 42, § 2º) × D1-53, D1-54, D1-55, D1-56; D1-R13 (Decreto 9.830, art. 12, § 2º): nenhum canônico do lote cita o Decreto 9.830; D3-R16 (CF, art. 5º, V) × D3-24; D3-R21 (CF, art. 5º, X) × D3-24.
- Pontos canônicos (anti-gêmeo, ficha 8.3.3): 8.4, D4-27 a D4-33 e os pontos A8.4-06, A8.4-08 e A8.4-16 da leva 1: nenhum repetido; 2.2, D1-53 a D1-60: nenhum repetido (o D1-R01 julga parte do art. 42 que o D1-56 toca por outro ângulo: ver “Difere de”; o ponto A2.2-01, do art. 42, § 1º, foi reprovado no R1 como gêmeo do D1-55 e saiu da leva); 6.4, D3-51 a D3-59: nenhum repetido; 6.3 (leva 1), CC, art. 186 e art. 927, caput, e Lei 8.112, art. 122, caput, e art. 124: o D3-R15 (art. 186, dano exclusivamente moral), o D3-R17 (art. 927, parágrafo único) e o D3-R18 e D3-R20 (art. 122, §§ 3º e 2º) são ângulo novo, com “Difere de”.
- Itens da leva com ponto no Decreto 9.203: 0 (exigência (c): nenhum item da 8.4 usa o art. 2º, II, nem o art. 4º, IV; “9.203” ocorre em enunciado: 0; ocorre só na nota do D4-R22, para registrar que o item não cita nem parafraseia o decreto).

### 4.6 Verificações textuais, abertura × gabarito e fecho × gabarito

- Enunciados que começam por “Considere que”: 13 (D4: 3; D1: 5; D3: 5).
- Abertura × gabarito na leva (ficha 7.4.2): “Considere que” 7 C / 6 E (53,8% de C; exigido ≥ 40% — CONFERE); declarativos 10 C / 7 E (41,2% de E; exigido ≥ 40% — CONFERE). Ficha 8.3.6: 7 C / 6 E e 10 C / 7 E.
- Fórmula “Nessa situação, nos termos d…” (ficha 7.4.3): folhas do D3 (6.4): 2 dos 5 itens com “Considere que” (D3-R17, D3-R19; limite: metade, no máximo 2) — CONFERE; lote D1 (2.2), só informado: 2 dos 5 (D1-R11, D1-R12).
- SUJ (ficha 7.4.4): D4-R26 (C), D1-R01 (C), D1-R08 (C), D3-R14 (C); nenhum SUJ da leva troca o sujeito (o D1-R03, único com sujeito trocado, foi reprovado); nos SUJ o sujeito é o da letra.
- Negação frontal (ficha 7.4.5): E com “não” ou “nem” no enunciado: D1-R05, D1-R07, D1-R13, D3-R16. O “não” do D1-R05, do D1-R07 e do D1-R13 é conteúdo do dispositivo citado (efeito da falta de parecer; hipótese de não aplicação; “não reste comprovada”, exigência do art. 12, § 2º), não negação de cenário. Nenhum E monta cenário que enumere todos os elementos do dispositivo para negá-lo no fecho; no D3-R16 o “mas não por dano à imagem” é a própria troca do rol (o cenário não descreve os elementos do art. 5º, V); o cenário do D1-R04 não enumera os elementos do art. 12, § 3º.
- “pós-NPM” em enunciado: 0; “Poder Legislativo”, “Câmara dos Deputados” ou “comissão” em itens declarados N: 0; itens do Decreto 9.830 (D1-R02, R04, R08, R09, R10, R13) com moldura S: 0; E com moldura: 3 (todos com Troca declarada); itens com moldura S sem tipo declarado: 0.
- Trechos da coluna Base (inclusive o do D1-R13, 24 palavras): 37 (em 30 itens; 7 itens com dois trechos separados por “[…]”: D4-R19, D4-R27, D1-R05, D1-R06, D1-R07, D3-R17, D3-R21); subcadeia do texto do adendo: 37 de 37; subcadeia da cópia em normativo_cache/: 37 de 37 (normalização: espaços colapsados; hifenização de fim de linha desfeita; Figura 1 do guia da Casa Civil lida pela cópia reconstruída coluna a coluna); maior trecho: 25 palavras; maior soma por item: 25 palavras (limite 25). URL de cada item idêntica à do adendo: 30 de 30.

Abertura × gabarito e fecho × gabarito — Lote D4 (C/E).

| Conjunto | Itens | “Considere que” | Declarativos | Fecho de acerto | Fecho neutro | “Nessa situação, nos termos d…” | Outra “Nessa situação,” | Sem “Nessa situação,” |
|---|---|---|---|---|---|---|---|---|
| Canônicos | 79 | 21/8 | 20/30 | 5/0 | 0/0 | 3/0 | 11/7 | 22/31 |
| Leva 1 | 17 | 2/9 | 5/1 | 2/6 | 0/3 | 0/0 | 0/0 | 5/1 |
| Leva 2 | 10 | 2/1 | 4/3 | 0/1 | 2/0 | 0/0 | 0/0 | 4/3 |
| Acumulado | 106 | 25/18 | 29/34 | 7/7 | 2/3 | 3/0 | 11/7 | 31/35 |

Abertura × gabarito e fecho × gabarito — Lote D1 (C/E).

| Conjunto | Itens | “Considere que” | Declarativos | Fecho de acerto | Fecho neutro | “Nessa situação, nos termos d…” | Outra “Nessa situação,” | Sem “Nessa situação,” |
|---|---|---|---|---|---|---|---|---|
| Canônicos | 60 | 0/0 | 30/30 | 0/0 | 0/0 | 0/0 | 0/0 | 30/30 |
| Leva 1 | 0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 |
| Leva 2 | 12 | 3/2 | 3/4 | 0/0 | 0/0 | 1/1 | 2/1 | 3/4 |
| Acumulado | 72 | 3/2 | 33/34 | 0/0 | 0/0 | 1/1 | 2/1 | 33/34 |

Abertura × gabarito e fecho × gabarito — Lote D3 (C/E).

| Conjunto | Itens | “Considere que” | Declarativos | Fecho de acerto | Fecho neutro | “Nessa situação, nos termos d…” | Outra “Nessa situação,” | Sem “Nessa situação,” |
|---|---|---|---|---|---|---|---|---|
| Canônicos | 71 | 15/10 | 16/30 | 0/0 | 0/0 | 0/0 | 15/10 | 16/30 |
| Leva 1 | 13 | 3/3 | 5/2 | 0/0 | 0/0 | 3/3 | 0/0 | 5/2 |
| Leva 2 | 8 | 2/3 | 3/0 | 0/0 | 0/0 | 1/1 | 1/2 | 3/0 |
| Acumulado | 92 | 20/16 | 24/32 | 0/0 | 0/0 | 4/4 | 16/12 | 24/32 |

Os canônicos do D1 não usam “Considere que” nem “Nessa situação,” no lote inteiro (relidos de D1_v2.md); a leva 1 não tem itens do D1. “Fecho neutro” e “fecho de acerto” só se aplicam ao D4 (K2 é conjunto do D4); nas folhas do D3 e do D1 as colunas servem à comparação.

### 4.7 Formatos máximos por folha, em %

| Folha | DEF | SUJ | SIT | NUM | PAR | APL | Maior |
|---|---|---|---|---|---|---|---|
| 8.4 (sobre 20 itens) | 5 (25,0%) | 1 (5,0%) | 4 (20,0%) | 0 (0,0%) | 5 (25,0%) | 5 (25,0%) | DEF 5 (25,0%) |
| 2.2 (sobre 20 itens) | 6 (30,0%) | 2 (10,0%) | 5 (25,0%) | 1 (5,0%) | 6 (30,0%) | 0 (0,0%) | DEF 6 e PAR 6 (30,0%) |
| 6.4 (sobre 20 itens; a folha tem 16 agora) | 5 (25,0%) | 1 (5,0%) | 3 (15,0%) | 0 (0,0%) | 2 (10,0%) | 5 (25,0%) | DEF 5 (25,0%) |

Na leva, só os 30 itens novos: 8.4 3/1/2/0/3/1; 2.2 2/2/5/0/3/0; 6.4 2/1/1/0/0/4 (DEF/SUJ/SIT/NUM/PAR/APL). Os percentuais da tabela têm por base os 20 itens da folha final; a 6.4 tem 16 itens agora (APL 5 = 31,3% de 16, 25,0% de 20). Formatos da leva: DEF 7, SUJ 4, SIT 8, NUM 0, PAR 6, APL 5; a ficha 8.3.5 previa DEF 6 e SUJ 5, e a diferença é só o D1-R13 (DEF) no lugar do D1-R03 (SUJ); SIT, NUM, PAR e APL conferem. Teto de 6 por formato na folha final de 20: respeitado em todas as folhas (2.2: DEF 6 e PAR 6).

### 4.8 Concentração por norma na folha 2.2 (ficha, seção 8.2, item 5)

| Norma | Itens da leva na 2.2 | Teto da ficha | Situação |
|---|---|---|---|
| Decreto 9.830/2019 | 6 (D1-R02, D1-R04, D1-R08, D1-R09, D1-R10, D1-R13) | 5 | ACIMA em 1: extrapolação registrada na pendência 6.4, item 1 (decisão da GCB) |
| Lei 14.133/2021 | 4 (D1-R06, D1-R07, D1-R11, D1-R12) | 4 | no teto |
| Lei 9.784/1999 | 2 (D1-R01, D1-R05) | — | — |
| LINDB | 0 | — | — |
| Total | 12 | — | — |

Na v1 o Decreto 9.830 estava em 5 (teto) e a Lei 9.784 em 3 (D1-R01, D1-R03, D1-R05). Os 6 itens do Decreto não levam moldura do Legislativo e nenhum afirma o alcance do Decreto (alerta P3).

## 5. Bloco à GCB

- Arquivo: saida/gcb/DA_reforco_leva2_v2.md (nome do despacho; ficha, seção 7.5). A v1 (SHA-256 40f2288a…ee788) fica intacta. Não houve commit nem push. Nenhuma leitura externa: tudo vem dos adendos do D4 (R59 a R81, com os alertas B), do D1 (seção 4, alertas P) e do D3 (seção 4, alertas A) e das cópias em saida/gcb/normativo_cache/; cada trecho da coluna Base foi conferido por script como subcadeia do adendo e da cópia (37 de 37 trechos, cada item com até 25 palavras no conjunto dos trechos), inclusive o do D1-R13. Nada foi gravado na leva 1 (a errata AJ-E1 do D3-R13 segue no gatilho como item separado).
- Ids e ordem: D4-R19 a D4-R28 (8.4); D1-R01, D1-R02, D1-R13, D1-R04 a D1-R12 (2.2; o D1-R13 ocupa a posição 3, no lugar do D1-R03, reprovado, cujo id não volta); D3-R14 a D3-R21 (6.4), na ordem da ficha (seção 8.3.4). Itens sem lastro: nenhum (30 de 30 com trecho literal). Pontos de reserva usados: A2.2-09 (2.2), no D1-R13; os demais continuam intactos (8.4: A8.4-07, 12, 13, 03, 01, 17, 14; 2.2: A2.2-11, 14, 15, 19, 21, 22, 05, 06; 6.4: A6.4-18, 10, 07). Pontos sugeridos pela ficha trocados: A2.2-01 → A2.2-09 (R1, seção 3); o A2.2-01 não volta (gêmeo do D1-55).
- Núcleo (ficha, seção 8.2, item 9; nota à GBQ para a T-123): 8.4 sem núcleo novo (D4-R19 a D4-R28 com nucleo=false); 2.2: D1-R01 e D1-R02; 6.4: D3-R14 e D3-R15 (todos diretos e primeiros do arquivo em suas folhas). O D1-R13 não é núcleo.
- Pistas de forma (ficha, seção 7.4), resultado: (1) fecho neutro do D4: D4-R20 (C, com moldura) e D4-R23 (C, sem moldura) usam “Nessa situação, é correto afirmar que”; nenhum E novo do D4 o usa (2 C / 3 E, 40,0%); (2) abertura: “Considere que” 7 C / 6 E e declarativos 10 C / 7 E (seção 4.6), iguais à v1 (o D1-R13 é declarativo e E, como o D1-R03); (3) fórmula “Nessa situação, nos termos d…” na 6.4: 2 de 5 (D3-R17 e D3-R19); o D3-R18 e o D3-R20 citam a Lei 8.112 no fim do enunciado, e o D3-R16 não cita a norma no fecho; (4) contraste “, e não”: D4-R19 (C); nenhum SUJ da leva troca o sujeito; (5) negação frontal: nenhuma (seção 4.6). K4 do D4 fecha em 25/18 (58,1%), a 1,9 ponto do teto de 60%: nas levas 8 e 9, item do D4 com “Considere que” é preferencialmente E (ficha, seção 8.6, item 3).
- Amostra da gbq-estilo, designada pela ficha (seção 8.3.8), nos ids finais: D4-R20 (A8.4-02; APL, C com moldura de expositor e fecho neutro), D1-R04 (A2.2-10; SIT, E, Decreto 9.830, “Considere que”, sem moldura; já com o AJ-2) e D3-R18 (A6.4-13; APL, E com moldura do Legislativo, aderência parcial, Lei 8.112). Saída esperada: saida/banco/estilo_DA_reforco_leva2.md (ver pendência 6.4, item 6).
- Alertas e exigências cumpridos: nenhum “NGP” em texto próprio; D4-R24 atribui a classificação em primárias e de apoio ao Referencial do TCU e não nomeia o autor (alerta B2); D4-R21 usa o “setor público em geral”, literal de R66, e não generaliza o que R68 e R69 dizem só da CGU (alerta B8); D4-R22 não cita nem parafraseia a definição do Decreto 9.203 que o trecho de R65 ressalva, e nenhum item da 8.4 usa o Decreto 9.203, art. 2º, II, nem o art. 4º, IV (exigência (c)); D1-R02, R04, R08, R09, R10 e R13 não levam moldura e não afirmam o alcance do Decreto 9.830 (alerta P3); D1-R02 mantém a “culpa grave” e o D1-R10 julga só o art. 17 (alerta P4); D1-R06, R07, R11 e R12 usam a Lei 14.133 nos arts. 10, 53 e 72, III (reconfirmação de 20/10/2026), sem o inciso I vetado do § 1º do art. 10 (alerta P5); nada sobre responsabilidade solidária do parecerista (P8); itens da Lei 8.112 (D3-R18, D3-R20) nomeiam a lei e o sujeito e não afirmam regime próprio da Câmara (alerta A1); CC, arts. 186 e 927, pela letra, sem efeito de decisão do STF (alerta A2); D3-R17 não põe o Estado em cena nem afirma o regime ou a teoria do risco (alerta A11); D3-R19 e D3-R20, após os AJ-8 e AJ-10, não põem o servidor como devedor direto do particular (A11 e C12).
- Notas “não pôr no mesmo simulado” (à GBQ; as de (k) a (x) são as da ficha, seção 8.5): (k) D3-R16 e D3-R21 (CF, art. 5º, V e X); (l) D3-R19 e D3-R34 (CC, art. 944, caput e parágrafo único; o D3-R34 é da leva 3); (m) D3-R18 e D3-R20 (Lei 8.112, art. 122, §§ 3º e 2º; mesma moldura e mesma cena de servidor); (s) D1-R01 e D1-56, D1-R05 com D1-55 e D1-56 (os dois fazem a comparação com o parecer obrigatório), D1-R02 e D1-58; (s2) NOVA: D1-R13 e D1-R04 (Decreto 9.830, art. 12, §§ 2º e 3º: prova do dolo ou do erro grosseiro). A parte “D1-R03 × D1-55” da nota (s) saiu desta seção (R1, seção 8, item 3); a ficha 8.5 é da GCB (pendência 6.4, item 2). (t) D3-R14 e D3-R28 (Lei 8.987, art. 25, caput; o D3-R28 é da leva 3); (u) D4-R19, D4-R25 e D4-R27 com D4-28 (componentes do modelo lógico); (v) parciais da leva: D3-R18 e D3-R20, só simulado diagnóstico (D-ADERENCIA); (x) os 5 itens com moldura desta leva (D4-R20; D3-R16, R18, R19, R20) contam para o teto de 50% de C com moldura por simulado. Acréscimos meus, sem decisão: D4-R19 e D4-R27 saem da mesma Figura 1 do guia da Casa Civil (processos × produtos; impactos × resultados) e D1-R06 e D1-R07 da Lei 14.133, art. 10 (caput e § 1º, II): cabe à GBQ não pô-los juntos se achar útil.
- Dúvidas de conteúdo (sem consulta a terceiros): (i) D3-R15: resolvida pelo R1 (AJ-6 e AJ-7): o enunciado passa à concessiva da letra (“ainda que o dano … seja exclusivamente moral”) e a justificativa não afirma que ela basta; sem dúvida remanescente; (ii) D1-R08 reproduz só a primeira parte do § 6º do art. 12 do Decreto 9.830 (a segunda, A2.2-14, não entra), e o mecanismo declarado é C6 (afirmação parcial verdadeira); (iii) D3-R18 e D3-R20: pertinência parcial (Lei 8.112 é regime do servidor; alerta A1); se a gcb-cqfp recusar a pertinência sem reserva direta, a 6.4 fica com 14 diretos + o que a QA aceitar e a reserva da 6.4 (A6.4-18, A6.4-10, A6.4-07) é só de indiretos (ficha, seção 8.2, item 2); no R1, ambos com pertinência parcial aceita; (iv) D1-R13: o ponto A2.2-09 é do Decreto 9.830, cujo alcance ao Legislativo é [SEM FONTE — não afirmar] (P3); o item nomeia o Decreto e o “agente público” e não diz a que órgãos se aplica.
- Errata AJ-E1 do D3-R13 (leva 1): fora desta tarefa; a conferência é da gcb-cqfp (CONFERIDO no R1, seção 6), segue ao gatilho A da leva 2 como item separado (ficha, seção 8.3.10), e este arquivo não altera o da leva 1.
- Registro da seção 3: a tabela de proveniência está na seção 3.2 (id → dispositivo/fonte → URL → verificado em), imediatamente antes das contagens, como no arquivo da leva 1.

## 6. Desvios da ficha e pendências para a GCB

**6.1 Desvios de conteúdo da tabela da ficha (seção 8.3.4).** Um único desvio, decidido pelo R1: o D1-R13 substitui o D1-R03 na posição 3 da 2.2 (ponto A2.2-09, Decreto 9.830, art. 12, § 2º, no lugar do A2.2-01; formato DEF no lugar de SUJ). Gabarito E, [TS] sim, moldura N, aderência direta e abertura declarativa ficam como na linha da ficha. Ponto, formato, moldura S/N (e tipo e fecho), gabarito, [TS], aderência e abertura CQ/DC dos outros 29 itens foram lidos da tabela da ficha por script e comparados com este arquivo: 29 de 29 linhas iguais. As contagens das seções 8.3.6 (C/E, moldura, aderência, [TS], K1 a K4, fecho neutro, contraste, abertura × gabarito) e 8.3.7 (sequências) conferem com as da seção 4 deste arquivo; as da seção 8.3.5 (formatos) mudam só na 2.2 (DEF 5 → 6 e SUJ 3 → 2) e na leva (DEF 6 → 7 e SUJ 5 → 4), por causa do D1-R13.

**6.2 Desvios de redação e de forma (a GCB e a gcb-cqfp julgam).**
1. D3-R15 (A6.4-05): o desvio da v1 (“pode configurar”) foi eliminado pelo AJ-6; o enunciado usa a concessiva da letra, sem marcador de possibilidade.
2. D1-R04 (A2.2-10): o cenário não enumera a exceção do § 3º (dolo ou erro grosseiro), para não montar a negação frontal da seção 7.4.5 (aceito no R1); com o AJ-2 o cenário passa a ancorar-se na opinião técnica (art. 12, caput). O item afirma que o mero nexo implica a responsabilização (troca da polaridade).
3. D4-R22 (A8.4-09): o enunciado reproduz só a primeira oração do trecho de R65 e omite a ressalva final sobre a definição do Decreto 9.203, como a ficha exige (aceito no R1).
4. D1-R05 (A2.2-03): o enunciado compara o laudo técnico (art. 43) com o parecer obrigatório e vinculante (art. 42, § 1º); com os AJ-3 e AJ-4 a troca fica no sujeito que apresenta o laudo (o órgão omisso, e não o órgão de instrução que o solicita a outro órgão). A linha “Ponto de julgamento” (resumo) do D1-R05 ficou como na v1, porque o AJ-3/AJ-4 não a alcança.
5. Itens com dois trechos na coluna Base, separados por “[…]” (cada trecho é subcadeia contínua do adendo e da cópia): D4-R19, D4-R27, D1-R05, D1-R06, D1-R07, D3-R17, D3-R21 (aceito no R1).
6. Campo Mecanismo: a ficha não indica o código; escolhi entre E1 a E6 e C1 a C6 (regras/estilo_banca.md) item a item (C1: 1; C2: 13; C3: 2; C6: 1; E1: 5; E2: 5; E3: 2; E6: 1); o D1-R13 é E2 (o D1-R03 era E3). A gcb-cqfp aceitou a escolha no R1.
7. D1-R13 (A2.2-09): único item novo da v2; o enunciado inverte a polaridade da exigência de comprovação nos autos (“configura-se … ainda que não reste comprovada”), com a letra do § 2º como única fonte, e é o 6º item do Decreto 9.830 na folha (pendência 6.4, item 1).

**6.3 Conformidades registradas por clareza (não são desvios).** (a) D3-R18 e D3-R20 citam a Lei 8.112 no fim do enunciado (“conforme a Lei nº 8.112/1990”) e não no fecho “Nessa situação, nos termos d…”, para cumprir a seção 7.4.3; isso muda a posição da norma em relação aos itens da leva 1. (b) Os 5 itens com moldura declaram o tipo da cota (8.4: expositor em audiência pública de comissão da Câmara dos Deputados; 6.4: órgão/servidor do Poder Legislativo da União); D3-R18 e D3-R20 dizem “servidor público civil da União lotado em órgão do Poder Legislativo da União”, e a cena não atribui regime próprio à Câmara. (c) D3-R19, após o AJ-8, põe o servidor como vítima de dano causado por particular (como o D3-R16), e não como devedor.

**6.4 Pendências para a GCB (a produção não as decide).**
1. **Extrapolação do teto do Decreto 9.830 na 2.2 (decisão da GCB).** O D1-R13 usa o A2.2-09 (Decreto 9.830, art. 12, § 2º), indicado pela QA (R1, seção 3), e a folha 2.2 fica com 6 itens do Decreto (D1-R02, R04, R08, R09, R10, R13) contra o teto de 5 da ficha (seção 8.2, item 5). Motivo: nenhum ponto viável da reserva da ficha (8.3.4) está fora do Decreto. A reserva da ficha admite “Decreto só no lugar de item do Decreto e Lei 14.133 só no lugar de item da Lei 14.133”, e o D1-R03 era da Lei 9.784, sem ponto de reserva na mesma lei (por isso o R1 remeteu a escolha à GCB). Dos pontos fora do Decreto, (a) A2.2-19, A2.2-21 e A2.2-22 são da Lei 14.133 e fariam dela o 5º item da folha, contra o teto de 4 da mesma seção 8.2, item 5 (a regra da reserva só admite Lei 14.133 no lugar de item da Lei 14.133), além de concentrar o art. 10 (A2.2-19: 3º item, com D1-R06 e D1-R07) ou o art. 53 (A2.2-21 e A2.2-22: 2º item, com D1-R11); trocaria um estouro de teto por outro e piora a concentração (R1, seção 3); (b) A2.2-05 (LINDB, art. 28) é gêmeo do D1-57 pelo mesmo critério que reprovou o D1-R03 (R1, seções 3 e 9). O A2.2-06 também é do Decreto 9.830 (art. 2º, § 3º). Alternativas, se a GCB não aceitar o 6º item: (i) A2.2-19, E por troca, a custo do teto da Lei 14.133 (5 de 4); (ii) A2.2-04 (Lei 9.784, art. 47; ponto indireto, aderência parcial, fora da reserva da ficha), que respeita os dois tetos mas exige relaxar “só pontos diretos” (seção 8.2, item 5). Qualquer troca de ponto depois desta v2 exige QA própria; não foi feita aqui.
2. **Ficha 8.5 e 8.3.5/8.3.6 (GCB).** Nota (s): retirar “D1-R03 … × D1-55” e acrescentar D1-R13 × D1-R04 (R1, seções 8 e 9). Ficha 8.3.5: formatos da 2.2 passam a 6/2/5/1/6/0 e os da leva 2 a DEF 7, SUJ 4, SIT 8, NUM 0, PAR 6, APL 5. Ficha 8.3.6: “sujeito trocado só no D1-R03” deixa de valer (nenhum SUJ da leva troca sujeito).
3. **Ids do D1.** D1-R03 vago (não volta); D1-R13 usado. Pelo R1 (seção 3), as faixas seguintes do D1 passam a D1-R14–R22 (1.1) e D1-R23–R31 (1.2); a reconciliação republica.
4. **Reserva da 2.2.** O R1 sugere retirar o A2.2-05 da reserva (seção 9). O A2.2-01 sai de vez (gêmeo do D1-55). Reserva restante da 2.2: A2.2-11, 14 (nunca com o D1-R08), 15, 19, 21, 22, 05, 06; o A2.2-09 foi usado.
5. **Registros do R1 sem AJ.** D4-R26 fica SUJ, como na ficha (a QA observa que a construção está mais para DEF; reclassificar não muda teto: 8.4 ficaria DEF 6 e SUJ 0); D1-R11: a troca é “prévio → posterior” no controle de legalidade, e a ficha dizia “posterior à contratação”; D1-R11 e D1-R12: pertinência direta pelo critério do adendo, embora os arts. 53, caput, e 72, III, não tratem de responsabilidade (registro para a auditoria de cobertura).
6. **Auditoria de estilo da amostra (gbq-estilo).** Em 20/10/2026, ao gravar a v2, o arquivo saida/banco/estilo_DA_reforco_leva2.md não existia em disco. Nenhum AJ de estilo foi aplicado além dos AJ-1 a AJ-11 do despacho. Se a auditoria sair com AJ de estilo (D4-R20, D1-R04, D3-R18), cabe à GCB decidir se entram no R2 (ficha, seção 8.3.8) ou por errata (seção 7.6).
7. **Sequência.** Nenhuma pendência nova. Os três legados (2.2, alternância de 6, gabarito e [TS]; 6.4, bloco de período 3 com 8 itens, gabarito; 8.4, bloco de período 3 com 9 itens, [TS]) continuam como estavam (ficha, seções 7.3 e 8.2, item 7); nenhum deles inclui item da leva 2; o D1-R13 mantém E e [TS] na posição 3 (seção 4.3 igual à da v1).
8. **Moldura e conjuntos.** D3-R20 é o C com moldura em par com os E com moldura além da cota (D3-R16, R18, R19); se a gcb-cqfp reprovar um deles no R2, a R3 e a cota da folha ainda se sustentam com dois E; K4 do D4 em 58,1% (folga de 2 C até 60%): ver seção 5.
9. **Errata AJ-E1 (D3-R13, leva 1).** Fora desta v2; CONFERIDA no R1 (seção 6); vai ao gatilho A da leva 2 como item separado.

Registros sem decisão minha: (i) nome do arquivo conforme o despacho; (ii) o script saida/banco/moldura_ce.py não foi executado (ele reescreve o CSV da T-122); os regex foram copiados e aplicados aos 30 itens, e a moldura dos canônicos veio do CSV; (iii) as tabelas da seção 4 foram refeitas por script (python3 -I) a partir deste arquivo gravado, dos canônicos, da leva 1 e do CSV; as da moldura, da abertura e da sequência não mudam em relação à v1 porque nenhum AJ nem o D1-R13 altera moldura, abertura, gabarito ou [TS].

FIM DA LEVA 02 — REFORÇO DA
