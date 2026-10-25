# resposta_R1.md — T-130 — 2026-10-25 — gerado por gcb-cpp

Resposta da produção (gcb-cpp) à rodada 1 dos dois QAs da ORDEM_DA_V2_FASE1: `qa_normativo_R1.md` (qa-normativo-da) e `qa_didatico_R1.md` (gcb-cqfp-didatico). Cada achado traz o que foi feito e onde. "L<n>" é linha de `v2_producao.md`; "JSON" é o campo do `pacote_v1_15_DAv2_fase1_v2.json`. Gabaritos e ids: nenhum mudou. Mecanismo recodificado em 5 itens E (DV2-02, DV3-02, DV3-09, DV3-11, DV3-14), todos registrados por id em `registro_alteracoes_v2.md`, seção 3. Nada foi commitado.

## 1. qa_normativo_R1

| Achado | O que foi feito | Onde |
|---|---|---|
| DV1-17 ERRO: o art. 53 não fala do Judiciário (regra e justificativa) | Regra reescrita pela letra do art. 53 ("deve anular seus próprios atos eivados de vício de legalidade"); o controle judicial da legalidade passa a doutrina, marcado [SEM FONTE — não afirmar como letra do art. 53]. Justificativa e `correta` ajustadas ("o Judiciário também os controla, por lição doutrinária"). Texto do item, gabarito E e mecanismo AUT mantidos. A tabela de proveniência do DV1 ganhou a ressalva. | L612 a 619; proveniência L683; JSON itens DV1-17 |
| N1 (erro de sentido): art. 69 na DEFINIÇÃO do DV3 | Reescrita pela letra: "os processos administrativos específicos continuam a reger-se por lei própria, aplicando-se-lhes apenas subsidiariamente os preceitos da Lei 9.784". O sentido deixou de ser invertido. | L1759; JSON lotes DV3.curso |
| N2 (REVERIFICAR): Decreto 12.967/2026 altera o Decreto 12.374/2025 e não consta da proveniência do DV2 | Linha própria na tabela de proveniência do DV2 (art. 9º, § 6º, nova redação, e § 8º, incluído; 12/5/2026, DOU 13/5/2026; arts. 1º, 2º e 24 inalterados; REVERIFICAR). No curso, a DEFINIÇÃO e a BASE LEGAL citam o Decreto 12.967/2026 como alteradora que não toca os artigos usados. DV2-05 segue VOLÁTIL. | proveniência L1274; curso L843 e L847 |
| Sugestão sobre DV2-05 (regra com Sipec, arts. 1º, 2º e 24) | Regra reescrita: "Decreto 12.374/2025 (arts. 1º, 2º e 24): 36 meses nos órgãos e entidades do Sipec, nas nomeações posteriores à sua publicação". O prefixo "Ressalva:" foi para o início (ESPEC §5). O art. 1º do Decreto, antes "não transcrito", está agora na DEFINIÇÃO, e o glossário ganhou "Sipec". O resumo do tópico e o resumo de uma página trazem o âmbito (A13). | L1097; DEFINIÇÃO L842; glossário L828 |
| N3 (literalidade): art. 1º, § 2º, I | Restaurado "integrante da estrutura da Administração direta e da estrutura da Administração indireta". | L1425 |
| N4 (literalidade): art. 69-A, II, e regra do BQ-0127 | DEFINIÇÃO com a letra "pessoa portadora de deficiência, física ou mental (II)" e o inciso IV com a letra "portadora de doença grave, com base em conclusão da medicina especializada". A regra e a decisiva do BQ-0127 citam a letra entre aspas; o conteúdo do item real não mudou. | L1760; L2039 |
| N5 (inferência, não letra): decisão coordenada na Casa | RESPOSTA DO CASO reescrita: "pela letra do art. 49-A, I e II, as condições estão presentes"; que o dispositivo (escrito para a Administração Pública federal) alcance órgãos da Casa é dito "inferência pelo art. 1º, § 1º, e não letra do dispositivo". A segunda parte (Poderes distintos, § 6º, III) é letra e ficou como estava. A tabela de proveniência registra a inferência. | L1650; proveniência L2051 |
| N6 (literalidade): LINDB, art. 21, parágrafo único | Restaurado "quando for o caso": "e, quando for o caso, indicar as condições para que a regularização ocorra de modo proporcional e equânime". | L356 |
| N7 (base parcial): definição de motivo é doutrinária | "(doutrina)" na regra do DV1-06 e "(conceito doutrinário)" nas duas entradas "Motivo" do glossário; `ref` do item separa motivação (art. 50) de motivo (doutrina). | L502+; glossário L140 e L182 |
| N8 (doutrina em caso): falta de publicação do extrato | Ver A1 (caso substituído). O que restou de doutrina (vício de forma como defeito sanável) está marcado como leitura doutrinária na BASE LEGAL, na RESPOSTA e na regra do BQ-0122: [SEM FONTE — não afirmar como letra de lei]. | L320 |
| N9 (datas): BASE LEGAL com datas antigas | Todas as BASE LEGAL passam a dizer "texto conferido em [data do mapa] e reconferido em 2026-10-25 em planalto.gov.br", só para os dispositivos que a R1 reabriu. Onde a R1 não transcreveu o artigo (arts. 58, 60, 62 e 59, § 2º da Lei 9.784; CF, art. 5º, XII e LVI) a data é a do mapa (2026-10-20), sem "reconferido". Datas também na proveniência. | p. ex. L1726 e L1566 |
| N10: pegadinha de DV3-09 rotulada CON com item PRA; BQ-0127 com exemplo de prioridade sob o par recurso × revisão | Ver A4 (DV3-09 virou SUP) e A3 (pegadinha de prioridade separada do par recurso × revisão). | linhas citadas em A3 e A4 |
| Tabela por item: 53 CONFERE, 6 NÃO CONFERIDO (doutrina declarada) | Sem ação: nenhum texto de item CONFERE foi alterado, exceto os que a própria R1 mandou (DV1-17) e os recodificados por A4 (DV2-02, DV3-09, DV3-11, DV3-14), que ficam como texto novo para a R2. | registro_alteracoes_v2.md, seção 3 |

## 2. qa_didatico_R1 — achados obrigatórios (O)

| Achado | O que foi feito | Onde |
|---|---|---|
| A1 — DV1, extrato não publicado tratado como vício de forma sanável | Caso substituído por defeito inequívoco: benefício concedido por despacho quando a norma da Casa exigia portaria, por quem tinha competência e sem lesão ou prejuízo. RESPOSTA e EXEMPLO acompanham. Corrigido pela letra do art. 55; a qualificação do vício como sanável é leitura doutrinária, marcada. A divergência sobre extrato (forma × eficácia) ficou fora do texto. | CASO L306; RESPOSTA L323; EXEMPLO L326; BASE L320 |
| A2 — DV3, "gravação clandestina" como prova ilícita | Caso trocado por interceptação de comunicação telefônica sem ordem judicial; a DEFINIÇÃO traz a letra da CF, art. 5º, XII e LVI (texto do cache do qa-normativo-da, 2026-10-20), ao lado do art. 30. A gravação feita por um dos interlocutores aparece só como "matéria controvertida [SEM FONTE — não afirmar]". A RESPOSTA liga a recusa ao art. 30 e à exigência de decisão fundamentada (art. 38, § 2º). | CASO L1544; DEFINIÇÃO L1552; BASE L1566-1567; RESPOSTA L1570 |
| A3 — pegadinha do BQ-0127 (par e texto não correspondem) e par recurso × revisão repetido | A mini-lição de revisão, prazos e prioridade passa a ter a pegadinha "prioridade a requerimento, com prova (art. 69-A, § 1º)" × "prioridade automática" [SUP], evidência DV3-20 e BQ-0127, como a R1 indicou. O par recurso × revisão ficou só na mini-lição do recurso (evidência DV3-18). Nas duas, A/B/MUDA, `par` e `texto` batem. Segundo ITEM acrescentado a cada uma (DV3-18 no recurso; DV3-20 na prioridade). Exceção declarada: ver seção 5. | mini do recurso L1738; mini da prioridade L1775; pegadinhas do lote L1816 |
| A4 — mecanismo da pegadinha × mecanismo do item de evidência (4 casos) | DV2 posse × exercício: par passa a "investidura com a posse × com o exercício" [CON] e DV2-02 foi reescrito como CON (a banca atribui a investidura ao exercício); DV3 prazo supletivo: DV3-09 virou SUP (suprime "inexistindo disposição específica") e a pegadinha é SUP; DV3 prova: DV3-11 virou SUP (dispensa a decisão fundamentada) e a pegadinha é SUP; DV3 desistência: DV3-14 virou AUT (troca quem avalia o interesse público) e a pegadinha é AUT. Para fechar as cotas, DV3-02 foi recodificado de SUP para NEG (a vedação do art. 13, II, é invertida). Gabaritos e ids intactos. As demais pegadinhas conferem (DV1: 8 de 8; DV2: 7 de 7; DV3: 9 de 10, exceto a da prioridade, seção 5). | DV2 L1040, item L1067; DV3 L1804, L1806, L1808; itens L1901, L1921, L1951, L1831 |
| A5 — 10 comandos com um tema só (DV2-10, 14, 15, 16, 19; DV3-04, 12, 15, 19, 20) | Os 10 comandos passam a nomear 2 ou 3 temas do item do edital (exemplo: DV2-14 "vacância, exoneração e remoção de servidores públicos"; DV3-20 "revisão, prazos e prioridade na tramitação"). Repetição "Nos termos da Lei" saiu do comando de DV2-10 e DV3-12, e "Segundo a Lei" de DV3-06. Recomendados A17: DV1-02, DV1-06, DV2-06, 09, 13, 18, DV3-07, 16, 18 também ampliados. Leitura manual dos 60 comandos: todos nomeiam dois ou três temas. | comandos em `(d)` de cada lote, p. ex. L1189 e L2013 |
| A6 — `resumo` e `pares` de D1 e D2 com o conteúdo retirado | D1: o item 2 do `resumo` passa a ter só o parecer (2.2), com remissão a DV1 e DV3; retirados 9 pares (anulação × revogação, convalidação × revogação, motivo × motivação, delegação × avocação, incompetência × desvio, inexistência dos motivos × ilegalidade do objeto, vinculado × discricionário, presunção relativa × absoluta, prazo do parecer × decadência); ficam 13 de 22. D2: as entradas 3.4 e 4.4 do `resumo` remetem a DV2 e DV3; retiradas as 6 linhas da tabela de números do 3.4 retirado e as 7 da Lei 9.784, mais a frase de estágio e estabilidade; retirados 13 pares (estágio × estabilidade, reintegração × recondução, remoção × redistribuição, readaptação × reversão, disponibilidade × aproveitamento, remoção a pedido a critério × independentemente, recurso × revisão, impedimento × suspeição, delegação × avocação, consulta × audiência, ônus da prova, anulação × revogação × convalidação, recurso não conhecido × revisão de ofício); ficam 33 de 46. Texto, não consolidação: feito aqui. | JSON lotes D1 e D2 (`resumo`, `pares`); registro_alteracoes_v2.md, seção 6 |
| A7 — número sem norma: DV1 "levar" 4; DV2 fluxo; DV3 fluxo e "levar" 3 | DV1: "cinco anos" com art. 54 (e arts. 53 e 55 na mesma frase), esquema com os artigos e a legenda do compare com a data de conferência. DV2: fluxo com "Posse: 30 dias da publicação (art. 13, § 1º)" e "Exercício: 15 dias da posse (art. 15, § 1º)", data de conferência no título. DV3: fluxo com arts. 5º, 18 a 21, 29 a 47, 49 e 59; "levar" 3 com os quatro números e seus artigos (24, 26, § 2º, 49 e 59). As legendas dos três compare trazem "Texto conferido em 2026-10-25 em planalto.gov.br". | DV1 L60, L46; DV2 L721; DV3 L1311, L1324 |
| A8 — linha 8 em todos os tópicos (rito: o qa-normativo-da ainda não confirmou o texto novo) | Pendência de rito, não de produção. Os trechos novos que dependem dessa confirmação estão listados na seção 8 (R2). | seção 8 |
| A10 — escopo do DV1 sem `onde` | `onde` = "P1-DA-2.1, fase 2 da ORDEM_DA_V2 (PRÓXIMO)"; o tema passou a nomear também a renúncia e as espécies de ato (A15). | L81; JSON topicos[P1-DA-2.1].escopo |

## 3. qa_didatico_R1 — achados recomendados (R) e demais linhas

| Achado | O que foi feito | Onde |
|---|---|---|
| A9 — DV1, RESPOSTA da extinção anula por incompetência sem ressalvar a convalidação | Ressalva acrescentada: "só se o defeito fosse sanável e atendidas as condições do art. 55 caberia convalidar". | L401 |
| A11 — DV3, recurso: DEFINIÇÃO sem o art. 58 (e sem os arts. 60 e 62) | DEFINIÇÃO com os quatro legitimados do art. 58, o § 2º do art. 59, o art. 60 e o art. 62, com a letra do mapa D2 (2026-10-20). Esses artigos não estavam na tabela do qa_normativo_R1 e entram na lista da R2. BASE LEGAL separa o que a R1 reconferiu do que não reconferiu. Par novo "interessado (art. 9º) × legitimado para recorrer (art. 58)". | L1717-1719; pares L1792 |
| A12 — DV2, estágio: intercalado VOLÁTIL DV2-05 | Intercalado trocado por DV2-06 (estágio × estabilidade); DV2-05 (VOLÁTIL) passa à verificação. | L855 |
| A13 — DV2, resumo e resumo de uma página afirmam os 36 meses sem a ressalva de âmbito | Resumo do tópico: "36 meses para os órgãos e entidades do Sipec, nas nomeações posteriores à sua publicação (sem afirmar a aplicação à Câmara)"; resumo de uma página: arts. 1º, 2º e 24, mesma ressalva. Segue para o qa-normativo-da (R2). | JSON topicos[P1-DA-3.4].resumo; lotes DV2.resumo (L758) |
| A14 — DV3, escopo do art. 2º, parágrafo único, × XII tratado no tópico | Escopo: "art. 2º, caput e parágrafo único, exceto o inciso XII (impulsão de ofício), tratado neste tópico". | L1343 |
| A15 — DV1, outras formas de extinção e espécies de ato | Não produzido nesta fase (PRÓXIMO, fase 2). Declarado no escopo com `onde`. | L81 |
| A16 — itens antigos D1 e D2 sem `comentario`, `mecanismo` e `tipo` | Não tratado (PRÓXIMO). Registrado como limitação: a proporção de caso do tópico inteiro continua não mensurável. | — |
| A17 — comandos que entregam o par do item CON | Ampliados para temas do item do edital: DV1-02, DV1-06, DV2-06, DV2-09, DV2-13, DV2-18, DV3-07, DV3-16, DV3-18. | comandos em `(d)` de cada lote |
| Linha 1 — DV2 tarefa 5 (cessão sem item); DV3 tarefas 4 e 5 (art. 54; arts. 59, 61, 63) | Tarefas estreitadas aos itens existentes. DV2 tarefa 5: remoção ou redistribuição (arts. 36 e 37; a cessão fica como contraste no quadro). DV3 tarefa 4: anular, revogar e convalidar (arts. 53 e 55; o prazo do art. 54 é treinado no tópico 2.1). DV3 tarefa 5: recurso, revisão de sanção e prioridade (arts. 64, 65 e 69-A), verificada por DV3-18, BQ-0127 e DV3-20. | JSON topicos tarefas; L703, L1292, L1293 |
| Linha 3 — termo antes do glossário (três tópicos) | Tabela da seção 4. DV1: Anulação, Revogação e Convalidação (combinadas no glossário do Motivo, onde o art. 50, VIII as usa), Incompetência, Desvio de finalidade, Terceiros e Anulação/Revogação no bloco das nulidades. DV2: cinco formas de provimento, Exoneração, Demissão, Cargo em comissão e Função de confiança no glossário do primeiro bloco; Sipec no estágio. DV3: Autoridade, Diligência, Renúncia, Ata, Efeito suspensivo, Sanção e Revisão do processo sancionador antecipados. | seção 4 |
| Linha 5 — pares | Acrescentados os pares que a R1 apontou como ausentes: DV1 (revogação × ato que gerou direito adquirido; defeito sanável × vício que impõe anulação), DV2 (exoneração × demissão; formas de provimento vigentes × incisos III e IV revogados), DV3 (interessado × legitimado para recorrer; prioridade a requerimento × automática). A lista de pares dos relatórios DAD (seção 7) continua ausente do repositório: a conferência final contra ela segue pendente; nada de terceiro foi usado. | L415, L1022, L1780 |
| Linha 6 — ITEM a cada 2-3 quadros: segundo ITEM nas mini-lições densas | Segundo ITEM em: DV1 requisitos (DV1-03 e DV1-04) e anulação (DV1-14 e DV1-13); DV2 provimento (DV2-01 e DV2-02) e deslocamento (DV2-18 e DV2-17); DV3 atos (DV3-09 e DV3-10), instrução (DV3-11 e DV3-12), recurso (BQ-0132 e DV3-18) e prioridade (BQ-0127 e DV3-20). Total de ITEM por tópico: DV1 12 (antes 10), DV2 9 (7), DV3 14 (10). Efeito no aviso do checa_pacote: seção 9. | L172, L369, L813, L1014, L1525, L1576, L1735, L1772 |
| Linha 7 (DV1) — Classificação: simples/complexo/composto duas vezes; espécies sem pergunta | Prosa cortada (fica a DEFINIÇÃO com a pergunta "quantos órgãos manifestam vontade?"); espécies com a pergunta "qual o conteúdo e a finalidade do ato?" e a ressalva de que as listas variam. | L272; L277 |
| Linha 9 — `fechamento.caso` e `literalidade` sem item | DV1: caso = motivos determinantes (DV1-07) e decadência (DV1-15); literalidade com art. 50, caput e LINDB, art. 21 (DV1-06, DV1-16). DV2: caso = posse fora do prazo (DV2-04) e remoção de ofício (DV2-20); literalidade sem o art. 8º. DV3: caso = delegação ou avocação (DV3-04) e prioridade (DV3-20); literalidade com arts. 11 a 15, 24, 27, 30, 38, § 2º, 49, 49-A e 53 a 55, todos com item. | L73, L749, L1339 |
| DV2-10 e DV3-06 — comando e enunciado repetem "Nos termos / Segundo a Lei" | Comandos reescritos sem a repetição (ver A5). | comandos de DV2-10 e DV3-06 |
| DV2-10 e DV2-16 (SUP com "apenas") | Aceitos pela R1; sem ação. | — |
| Sobreposição DV1 × DV3 nos arts. 53-55 | Aceita pela R1 como adequada entre tópicos; condensar a mini-lição 8 do DV3 é BACKLOG. Sem ação. | — |
| Segunda leitura do mecanismo dos 7 itens reais | 7 de 7 de acordo; sem ação além do prefixo "Ressalva:" no início da regra (BQ-0122, BQ-0148, DV2-05). | L654, L670 |
| §10 — decisões do produtor (quatro unidades do item 2; DV3 como uma unidade; resumo e pares) | As duas primeiras ficam para ratificação da gcb-gerencia (D1); a terceira foi desfeita em A6. | — |

## 4. Linha 3 — termo × primeira linha (v2_producao.md)

Método: para cada entrada do GLOSSÁRIO, busca-se o termo (ou cada termo de uma entrada combinada) nas linhas anteriores do curso do lote, sem contar os títulos de mini-lição e o próprio quadro do glossário. Resultado: DV1 0, DV2 0 e DV3 2 antecipações, ambas em outro sentido e aceitas pela R1 (impedimento legal no art. 12; revogação da delegação no art. 14). A tabela lista os termos que a R1 apontou, com o glossário de antes e o de agora.

| Lote | Termo | Antes (v1) | Agora: linha do glossário | Primeira ocorrência antes dela |
|---|---|---|---|---|
| DV1 | Incompetência | sem glossário; usado antes da DEFINIÇÃO (L148) | L143 | nenhuma |
| DV1 | Desvio de finalidade | sem glossário; usado antes da DEFINIÇÃO (L148) | L144 | nenhuma |
| DV1 | Anulação | glossário L331; 1ª em L289 | L186 | nenhuma |
| DV1 | Revogação | glossário L372; 1ª em L307 | L186 | nenhuma |
| DV1 | Convalidação | glossário L294; usada antes, na DEFINIÇÃO do art. 50, VIII | L186 | nenhuma |
| DV2 | Reversão | glossário L852; 1ª em L770 | L784 | nenhuma |
| DV2 | Reintegração | glossário L891; 1ª em L770 | L784 | nenhuma |
| DV2 | Exoneração | glossário L932; 1ª em L790 | L785 | nenhuma |
| DV2 | Demissão | glossário L933; 1ª em L891 | L785 | nenhuma |
| DV2 | Cargo em comissão | glossário L934; 1ª em L771 | L786 | nenhuma |
| DV2 | Função de confiança | sem glossário (L774) | L786 | nenhuma |
| DV3 | Autoridade | glossário L1394; 1ª em L1351 | L1375 | nenhuma |
| DV3 | Diligência | glossário L1516; 1ª em L1472 | L1495 | nenhuma |
| DV3 | Renúncia | glossário L1563; 1ª em L1483 | L1496 | nenhuma |
| DV3 | Ata | glossário L1603; 1ª em L1534 | L1541 | nenhuma |
| DV3 | Efeito suspensivo | glossário L1679; 1ª em L1445 | L1456 | nenhuma |
| DV3 | Sanção | glossário L1718; 1ª em L1615 | L1627 | nenhuma |
| DV3 | Revisão do processo sancionador | glossário L1717; 1ª em L1711 | L1706 | nenhuma |
| DV3 | Legitimidade recursal | glossário sem o art. 58 na DEFINIÇÃO | L1703 | nenhuma |

Entradas combinadas (uma linha de glossário define vários termos): DV1 "Anulação, revogação e convalidação" (L186); DV2 "Readaptação, reversão, aproveitamento, reintegração e recondução" (L784), "Exoneração e demissão" (L785) e "Cargo em comissão e função de confiança" (L786). Cada termo também mantém a sua entrada completa no bloco em que é estudado.

## 5. Exceções e cotas que ficaram abertas

1. **Pegadinha da prioridade (DV3, última mini-lição).** A R1 indicou como evidência DV3-20 ou BQ-0127. Os dois são itens C (AP e LIT); o lote não tem item E sobre prioridade, e todos os 10 itens E do DV3 já sustentam outras pegadinhas. A pegadinha SUP foi mantida como a R1 pediu. Se a gcb-gerencia ou a R2 exigir item E de mesmo código, a saída é trocar o DV3-19 (contagem de prazos, C) por um E de prioridade, o que muda gabarito e fica fora desta rodada.
2. **Cotas de mecanismo (checa_estilo_DA, 3 avisos).** DV2: E/CON = 5 (cota 3-4); DV3: E/SUP = 4 (cota 2-3) e E/GEN = 0 (cota 1). Causa única: a regra do estilo §6.5 pede que toda pegadinha seja CON, SUP ou AUT, e cada lote tem uma pegadinha por mini-lição (seis no DV2, dez no DV3) sobre 11 e 10 itens E. No DV2, a pegadinha de posse × exercício exigiu um segundo CON (A4); no DV3, dez minis exigem dez itens E em CON/SUP/AUT, e as cotas dão no máximo nove. Preferi cumprir a regra da pegadinha a cumprir a cota. O DV1 tem zero avisos.

## 6. Mecanismos dos itens E após a v2

| Lote | CON | SUP | GEN | NEG | AUT/PRA/AMB/TEM | Mudanças |
|---|---|---|---|---|---|---|
| DV1 | 4 | 3 | 1 | 1 | 1 (AUT) | nenhuma |
| DV2 | 5 | 3 | 1 | 1 | 1 (AMB) | DV2-02 PRA para CON |
| DV3 | 3 | 4 | 0 | 1 | 2 (AUT) | DV3-02 SUP para NEG; DV3-09 PRA para SUP; DV3-11 NEG para SUP; DV3-14 GEN para AUT |

Cotas de C, [TS] (10 por lote), tamanho (21 a 35 palavras), caso (2 por lote) e fechamentos: inalteradas e dentro da faixa (checa_estilo_v2.txt).

## 7. Não feito nesta rodada

- A15 (mini-lição de outras formas de extinção e espécies de ato): PRÓXIMO, fase 2.
- A16 (comentario, mecanismo e tipo nos 22 + itens antigos de D1/D2): PRÓXIMO.
- Heurística "comando com um tema" do checa_estilo_DA e condensação do DV3 nos arts. 53-55: BACKLOG, GBQ.
- Conferência dos pares contra a lista DAD: depende do anexo do Fundador.
- Painel, LOTE_INFO, DISCIPLINAS/MODULOS e DIAG30 com o index.html: GBQ no build. Conferência manual feita nesta rodada: o DIAG30 de `saida/plataforma/plataforma_v17_1_template.html` não contém nenhum dos 7 ids reais movidos (BQ-0122, 0127, 0132, 0137, 0145, 0148, 0150) nem id DV.

## 8. Para a R2 do qa-normativo-da (texto novo)

- CF, art. 5º, XII e LVI (DEFINIÇÃO e BASE LEGAL do DV3, instrução).
- Lei 9.784/1999, arts. 58, 60 e 62 e art. 59, § 2º (DEFINIÇÃO do recurso), com a letra do mapa D2.
- Decreto 12.374/2025, arts. 1º, 2º e 24, agora transcritos na DEFINIÇÃO do DV2, e a remissão ao Decreto 12.967/2026.
- RESPOSTA do caso da decisão coordenada (inferência pelo art. 1º, § 1º).
- Itens reescritos: DV2-02, DV3-09, DV3-11, DV3-14 (texto novo) e DV3-02 (só recodificado), e os comentários de DV1-17, DV2-05 e BQ-0127.
- DEFINIÇÃO do DV3 (art. 69, art. 69-A, art. 1º, § 2º) e do DV1 (LINDB, art. 21, parágrafo único).

## 9. Avisos dos dois scripts, um a um (checa_pacote_v2_v2.md: 0 bloqueios, 12 avisos; checa_estilo_v2.txt: 3 avisos)

1. "base sem DIAG30": a base é o pacote.json, não o index.html. Verificação manual feita (seção 7). A GBQ repete com o index.html no build.
2. "prefixos de id novos" (DV1-, DV2-, DV3-) e 3. "lotes novos": esperados; pendência da GBQ (painel, LOTE_INFO, DISCIPLINAS/MODULOS). Registrados como pendência, não como defeito (R1, seção 6).
4 a 8 e 11. "ITEM para N quadros (recomendado 1 a cada 3)" (DV1 4 blocos, DV2 e DV3 um bloco cada): cada mini-lição tem sete quadros fixos mais os visuais, e o ITEM é um só ou dois por mini-lição. A v2 subiu de 10 para 12 (DV1), de 7 para 9 (DV2) e de 10 para 14 (DV3) ITEM, seguindo a recomendação da R1 (seção 6 do parecer), sem chegar a 1 em 3 porque os quadros GLOSSÁRIO, BASE LEGAL e EXEMPLO não exigem item. Mantido como aviso, com decisão final da gcb-gerencia.
9 e 10. "tópico P1-DA-2.1 com 8 questão(ões) de verificação além dos intercalados (meta 10)" e "P1-DA-4.4 com 6": novo na v2, efeito direto do segundo ITEM. O script conta só os itens DV do lote (20) menos todos os intercalados (inclusive os reais). Contando por `itemEdital`, que é o que a ESPEC §7 manda ("mínimo de 10 por item-folha além dos intercalados"), o P1-DA-2.1 tem 45 questões e 12 intercaladas (33 de verificação); o P1-DA-3.4, 41 e 9 (32); o P1-DA-4.4, 43 e 14 (29). A R1 (seção 6) já apontava essa diferença de contagem. Aviso mantido por ser do script; sem prejuízo para a meta.
12. "o pacote novo tem MAIS marcas de produção que o atual" (0 para 7): as 7 ocorrências são as linhas `ITEM BQ-nnnn` do curso, autorizadas pela ESPEC §4; a plataforma renderiza o item, não o id. A GBQ confirma no build que o id não aparece em texto. Igual à v1.
checa_estilo_DA (3 avisos): seção 5, item 2. Medidas: 40-60% C em todos os lotes (50%, 45%, 50%); mediana de 29, 28 e 26 palavras e 100% entre 21 e 35; caso em 10% (2 por lote); absolutizador em 15%, 15% e 10% dos itens (DV3 caiu com o fim dos E de "sempre"/"encerra sempre"); fechamentos dos seis tipos da banca, com "o item a seguir" em 5, 5 e 6 comandos.

## 10. Conferências desta rodada

- `checa_pacote_v2.py` contra `saida/pacote/pacote.json`: 0 bloqueios (checa_pacote_v2_v2.md); registro em JSON (registro_alteracoes_v2.json).
- `checa_estilo_DA.py --so-v2`: checa_estilo_v2.txt.
- Comparação v1 e v2 do pacote: gabaritos e ids idênticos nos 1.493 itens; diferem 63 itens (60 por `url`, que passou a apontar para v2_producao.md, e os campos listados em registro_alteracoes_v2.md, seção 3), os lotes D1, D2, DV1, DV2 e DV3 e os três tópicos; simulados, discursivas e edital idênticos.
- Busca por "Estratégia", "Herbert", "da aula" e "Aula <n>" nos três lotes: nenhuma ocorrência (D-ESTRATEGIA).

