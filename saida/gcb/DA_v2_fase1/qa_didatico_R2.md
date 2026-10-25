# qa_didatico_R2.md — T-130 — 2026-10-25 — gerado por gcb-cqfp-didatico

Ordem: ordens/ORDEM_DA_V2_FASE1.md. Rodada 2, a última. Objeto: saida/gcb/DA_v2_fase1/v2_producao.md (linhas citadas como L<n>), pacote_v1_15_DAv2_fase1_v2.json (JSON L<n>), resposta_R1.md, registro_alteracoes_v2.md, checa_pacote_v2_v2.md e checa_estilo_v2.txt. Referências: ESPEC v2 §§ 4–9; adendo v2.1; PADRAO_UNICO v1.1; regras/estilo_banca_DA_v1.md §§ 3, 4 e 6.
Fora do meu escopo: o texto normativo. Para a linha 8, apoio-me no qa_normativo_R2.md: APROVADO COM RESSALVAS, 0 de 60 itens com ERRO, ressalvas R2-1 a R2-4. Não alterei a produção nem o pacote e não fiz commit.
Classificação: **O** = obrigatório antes do gatilho A; **R** = recomendado.

## Resumo
- **DV1 (P1-DA-2.1): APROVADO COM RESSALVAS.** Nenhum achado O. Ficam só R.
- **DV2 (P1-DA-3.4): APROVADO COM RESSALVAS.** Uma condição O de execução mecânica (O-R2-2: números sem artigo).
- **DV3 (P1-DA-4.4): APROVADO COM RESSALVAS.** Duas condições O de execução mecânica (O-R2-1: verificação abaixo de 10; O-R2-2: números sem artigo).
- **Itens reprovados: 0 de 67 (0%).** Na R1 eram 10 de 67 (14,9%). Sem GATE.
- Achados da R1: as 9 O estão resolvidas. Das R, 14 estão resolvidas, 2 seguem abertas como PRÓXIMO (A15, A16) e 2 estão resolvidas só em parte (linha 5, linha 6).
- Como esta é a última rodada, as condições O-R2-1 e O-R2-2 não voltam para uma R3. A gcb-cpp as aplica e a gcb-gerencia confere antes do gatilho A. Nenhuma delas muda gabarito, e nenhuma exige texto normativo novo.

---

## 1. Achados da R1: RESOLVIDO ou NÃO RESOLVIDO

| Achado | Classe | Estado | Evidência na v2 |
|---|---|---|---|
| A1 extrato tratado como vício de forma | O | **RESOLVIDO** | CASO L306, RESPOSTA L323, EXEMPLO L326 (despacho em vez de portaria). A qualificação doutrinária está marcada em L310, L320 e L323. |
| A2 gravação clandestina | O | **RESOLVIDO** | CASO L1544 (interceptação sem ordem judicial); DEFINIÇÃO L1552; a controvérsia aparece só como [SEM FONTE] em L1567. |
| A3 par × texto do BQ-0127 e par repetido | O | **RESOLVIDO** | O par recurso × revisão ficou só em L1738 (evidência DV3-18). A prioridade tem pegadinha própria em L1775 e L1816, com `par` e `texto` coerentes. Ressalva sobre o item de evidência no §5(a). |
| A4 mecanismo da pegadinha × item | O | **RESOLVIDO** (4/4) | DV2-02 passou a CON (L1067, L1040). DV3-09 SUP (L1901, L1804). DV3-11 SUP (L1921, L1806). DV3-14 AUT (L1951, L1808). |
| A5 comando com um tema só | O | **RESOLVIDO** (10/10) | Li os 60 comandos (L454–644, L1059–1249, L1823–2013): todos nomeiam de 2 a 3 temas. |
| A6 resumo e pares de D1/D2 | O | **RESOLVIDO** | O item 2 do resumo de D1 agora traz só o 2.2 (JSON L37809). Em D2 aceito a descrição da produção (registro, seção 6); não conferi linha a linha. Ver R-R2-6. |
| A7 número sem norma (4 pontos) | O | **RESOLVIDO** nos 4 pontos | L60, L46, L721, L1311 e L1324. Achei **outros** números sem artigo, que não apontei na R1 (falha minha) e que já estavam na v1: ver O-R2-2. |
| A8 rito normativo | O | **RESOLVIDO** | qa_normativo_R2: APROVADO COM RESSALVAS, 0 de 60 itens com ERRO. Faltam aplicar as ressalvas R2-1 a R2-4. |
| A10 escopo do DV1 sem `onde` | O | **RESOLVIDO** | L81. |
| A9 extinção sem ressalva de convalidação | R | RESOLVIDO | L401. |
| A11 art. 58 (e arts. 60 e 62) | R | RESOLVIDO | L1717–1719. |
| A12 intercalado VOLÁTIL | R | RESOLVIDO | L855: DV2-06 virou o intercalado; DV2-05 passou à verificação. |
| A13 âmbito do Decreto 12.374 | R | RESOLVIDO | L715, L764 e L833–835. |
| A14 escopo do art. 2º, XII | R | RESOLVIDO | L1343. |
| A15 outras formas de extinção e espécies | R | **NÃO RESOLVIDO** (PRÓXIMO, declarado) | L81. |
| A16 itens D1/D2 sem `comentario`, `mecanismo` e `tipo` | R | **NÃO RESOLVIDO** (PRÓXIMO) | Agora pesa na meta de verificação: ver §5(c) e O-R2-1. |
| A17 comando que entrega o par | R | RESOLVIDO, exceto um | DV2-18 (L1229): "deslocamento de servidores e de cargos" entrega o MUDA servidor × cargo (R-R2-3). |
| Linha 1 (tarefas sem item) | R | RESOLVIDO | Tarefas estreitadas aos itens: L703, L1292 e L1293. |
| Linha 3 (glossário) | R | RESOLVIDO | Tabelas no §2. |
| Linha 5 (pares ausentes) | R | RESOLVIDO EM PARTE | Os 6 pares novos estão lá (L427–428, L1034–1035, L1792–1793). Faltam três instâncias (art. 57) × prazo do recurso e uma pegadinha própria para ato × fato. |
| Linha 6 (2º ITEM nas mini-lições densas) | R | RESOLVIDO EM PARTE | A contagem de ITEM subiu de 10/7/10 para 12/9/14. A meta de 1 a cada 3 quadros não foi atingida (aviso). Teve efeito colateral: ver §5(c). |
| Linha 7 (DV1, classificação) | R | RESOLVIDO | L272 e L276–277. |
| Linha 9 (fechamento × itens) | R | RESOLVIDO | L73–74 (DV1-07 e DV1-15 são `caso`); L748–749 (DV2-04 e DV2-20); L1338–1339 (DV3-04 e DV3-20). |
| Repetição "Nos termos/Segundo a Lei" no comando | R | RESOLVIDO | DV2-10 e DV3-06. |
| Prefixo "Ressalva:" | R | RESOLVIDO | DV2-05 (L1097). BQ-0122 e BQ-0148 conforme a resposta da produção. |

---

## 2. Checklist ESPEC v2 §9 refeito, por tópico

### 2.1 P1-DA-2.1 (DV1)
| # | Marca | Evidência |
|---|---|---|
| 1 | SIM | Cinco tarefas que começam por "Dado" (L24–28). Itens que verificam cada uma: DV1-01/02; DV1-03/04/05; BQ-0137 e DV1-06/07; DV1-12–15; BQ-0148 e DV1-17–20. |
| 2 | SIM | Mapa de chegada em L46. A plataforma repete o mapa no fechamento. |
| 3 | SIM | Tabela 2.1.1. |
| 4 | SIM | Os 8 CASOs terminam em "?" e não trazem a resposta. As RESPOSTAs aplicam a regra do bloco (L323, L363, L401). |
| 5 | SIM, com R | 13 pares e 8 pegadinhas, todas CON, SUP ou AUT, com mecanismo igual ao do item (L433–447). Falta uma pegadinha própria para ato × fato (R). A lista DAD continua ausente do repositório (BACKLOG). |
| 6 | NÃO (R) | 12 ITEM para cerca de 56 quadros (aviso do script). Os comentários têm três campos; os itens reais trazem o certame (L652+). Aceito como aviso; decisão da gcb-gerencia. |
| 7 | SIM | Uma representação por conceito. Cada classificação vem com a sua pergunta (L270, L276, L277). |
| 8 | SIM | Normativo R2: CONFERE / doutrina declarada. Não achei número sem artigo no curso do DV1. |
| 9 | SIM | Cinco frases (L57–61). As listas de literalidade e de caso (L65–74) batem com os itens. |
| 10 | SIM | Escopo com `onde` (L78–81). Nada de terceiro (§3). |
| adendo | SIM | C 10 (LIT 8, AP 2). E 10 (CON 4, SUP 3, GEN 1, NEG 1, AUT 1). Caso 2/23 = 8,7%. Comandos com 2–3 temas. checa_estilo: 0 avisos. |

**2.1.1 Linha 3 — termo do GLOSSÁRIO → primeira ocorrência no curso** (títulos não contam)
- Conceito (L101–105): Ato administrativo 101; Fato administrativo 102; Contrato administrativo 103; Unilateral 104; Regime de direito público 105. Todos aparecem pela primeira vez na própria linha.
- Requisitos (L137–144): Competência 137; Forma 138; Objeto 139; Motivo 140; Finalidade 141; Vício 142; Incompetência 143; Desvio de finalidade 144. Todos na própria linha; a antecipação da R1 (L148) foi eliminada.
- Motivo (L182–186): Motivo 182 (já em 140); Motivação 183; Motivos determinantes 184; Congruente 185; Anulação/revogação/convalidação 186. Nenhuma antecipação.
- Atributos (L224–229): Atributo 224; Presunção de legitimidade 225; Presunção relativa 226; Imperatividade 227; Terceiros 228; Autoexecutoriedade 229. Nenhuma antecipação. "Terceiros" está fora do bloco em que é usado no sentido do art. 55; é cosmético.
- Classificação (L262–265): Ato vinculado 262; Ato discricionário 263; Conveniência e oportunidade 264 (usado em 263, no mesmo quadro: aceito); Espécie de ato 265.
- Nulidades (L298–303): Nulidade 298; Defeito sanável 299; Convalidação 300 (já em 186); Lesão ao interesse público 301; Anulação 302 (já em 186); Revogação 303 (já em 186).
- Anulação (L339–342): Decadência 339; Efeitos favoráveis 340; Efeitos patrimoniais contínuos 341; Comprovada má-fé 342. Nenhuma antecipação.
- Extinção (L379–382): Extinção do ato 379; Ex tunc 380; Ex nunc 381; Direito adquirido 382. Nenhuma antecipação.

### 2.2 P1-DA-3.4 (DV2)
| # | Marca | Evidência |
|---|---|---|
| 1 | SIM | L699–703. A tarefa 5 foi reduzida a remoção × redistribuição, verificada por DV2-17 a 20. |
| 2 | SIM | Fluxo L721 com os artigos. O passo "Retorno" ainda não traz recondução e aproveitamento (R, menor). |
| 3 | SIM | Tabela 2.2.1. |
| 4 | SIM | Os 6 CASOs terminam em "?". As RESPOSTAs (L807, L850, L890, L929, L968, L1008) aplicam o artigo do bloco. |
| 5 | SIM | 13 pares, entre eles exoneração × demissão e as formas revogadas (L1034–1035). As 7 pegadinhas têm mecanismo igual ao do item (L1040–1053). |
| 6 | NÃO (R) | 9 ITEM para 42 quadros (aviso). Os comentários têm três campos; o item real traz o certame. |
| 7 | SIM | As formas de retorno vêm por pergunta (L874, L914). O compare tem 6 linhas e 2 colunas. |
| 8 | **NÃO (O-R2-2)** | Números sem artigo: no resumo do tópico, L713 ("trinta dias" e "quinze dias"); no quadro do deslocamento, L994 ("dez a trinta dias", art. 18). R, menor: L876 ("cinco condições", sem o art. 25, II). |
| 9 | SIM | Cinco frases (L732–736). A literalidade e o caso (L740–749) batem com os itens; DV2-04 e DV2-20 são `caso`. |
| 10 | SIM | L753–756, com `onde`. |
| adendo | SIM, com R | C 9 (LIT 7, AP 2). E 11 (CON 5, SUP 3, GEN 1, NEG 1, AMB 1). Caso 2/21 = 9,5%. Aviso E/CON = 5: ver §5(b). |

**2.2.1 Linha 3**
- Provimento (L777–786): Provimento 777; Forma de provimento 778; Nomeação 779; Investidura 780; Posse 781 (usada em 780, no mesmo quadro: aceito); Exercício 782; Cargo efetivo 783; Readaptação/reversão/aproveitamento/reintegração/recondução 784; Exoneração e demissão 785; Cargo em comissão e função de confiança 786 ("função de confiança" aparece em 782, no mesmo quadro: aceito).
- Estágio (L823–828): Estágio probatório 823; Estabilidade 824; Avaliação especial 825; Recondução 826 (já em 784); Referencial 827; Sipec 828. Nenhuma antecipação.
- Readaptação (L865–869): Readaptação 865 (784); Reversão 866 (784); Aposentadoria voluntária 867; Cargo vago 868; Excedente 869. Nenhuma antecipação.
- Reintegração (L905–909): Reintegração 905 (784); Recondução 906; Disponibilidade 907; Aproveitamento 908 (784); Demissão invalidada 909. Nenhuma antecipação.
- Vacância (L945–949): Vacância 945; Exoneração 946 (785); Demissão 947 (785); Cargo em comissão 948 (786); Cargo efetivo 949 (783). Nenhuma antecipação.
- Deslocamento (L983–987): Remoção 983; Redistribuição 984; Cessão 985; Ex officio 986; SIPEC 987. Nenhuma antecipação. R, menor: "Sipec" (L828) e "SIPEC" (L987) aparecem com grafias diferentes, e "requisição" e "exercício provisório" (L994) ficam sem definição.

### 2.3 P1-DA-4.4 (DV3)
| # | Marca | Evidência |
|---|---|---|
| 1 | SIM | L1289–1293. As tarefas 4 e 5 foram estreitadas: arts. 53 e 55 (DV3-16, DV3-17); arts. 64, 65 e 69-A (DV3-18, DV3-20, BQ-0127). |
| 2 | SIM | Fluxo L1311 com os artigos. |
| 3 | SIM | Tabela 2.3.1. |
| 4 | SIM | Os 10 CASOs terminam em "?". As RESPOSTAs aplicam a regra (L1570 já sem a gravação clandestina; L1650 com a inferência declarada). |
| 5 | SIM, com R | 13 pares e 10 pegadinhas. Falta o par três instâncias (art. 57) × prazo do recurso (R). Sobre a pegadinha da prioridade, ver §5(a). |
| 6 | NÃO (R) | 14 ITEM para 70 quadros (aviso). Os comentários têm três campos; os itens reais trazem o certame (L2025, L2033, L2041). |
| 7 | SIM, com R | Impedimento × suspeição vem com pergunta (L1461). O compare delegação × avocação repete a prosa, o que é aceitável. |
| 8 | **NÃO (O-R2-2)** | Números sem artigo: no resumo do tópico, L1305 ("cinco dias", "três dias úteis") e L1307 ("trinta dias"); no curso, L1501 (art. 24), L1503 (art. 26, § 2º) e L1594 (art. 49). |
| 9 | SIM | Cinco frases (L1322–1326). A literalidade (L1330–1334) tem item para cada linha: o art. 27 é o DV3-10. O caso (L1338–1339) corresponde a DV3-04 e DV3-20. |
| 10 | SIM | L1343–1346; o inciso XII já está ressalvado. |
| adendo | SIM, com R | C 10 (LIT 8, AP 2). E 10 (CON 3, SUP 4, AUT 2, NEG 1, GEN 0). Caso 2/23 = 8,7%. Avisos E/SUP = 4 e E/GEN = 0: ver §5(b). |

**2.3.1 Linha 3**
- Competência (L1368–1375): Competência 1368; Delegação 1369; Avocação 1370; Delegante/delegado 1371; Competência exclusiva 1372; Ato normativo 1373; Recurso administrativo 1374; Autoridade 1375. "Autoridade" aparece em 1368 e 1372, no mesmo quadro: aceito. A antecipação da R1 foi eliminada.
- Âmbito (L1411–1414): Interessado 1411; Administrado 1412; Requerimento inicial 1413; Impulsão de ofício 1414. Nenhuma antecipação.
- Impedimento (L1452–1456): Impedimento 1452 ("impedimento legal" em 1386, em outro sentido: aceito na R1); Suspeição 1453; Falta grave 1454; Parente e afim 1455; Efeito suspensivo 1456 (antes 1679, com 1ª ocorrência em 1445; agora a 1ª ocorrência é 1463, depois do glossário).
- Atos (L1490–1496): Intimação 1490; Prazo supletivo 1491; Antecedência mínima 1492; Dia útil 1493; Suprir a falta 1494; Diligência 1495 (usada em 1490, no mesmo quadro: aceito); Renúncia 1496 (1ª ocorrência em 1499).
- Instrução (L1535–1541): Instrução 1535; Prova ilícita 1536; Perícia 1537; Providência acauteladora 1538; Consulta pública 1539; Audiência pública 1540; Ata 1541 (1ª ocorrência em 1556). Nenhuma antecipação.
- Dever de decidir (L1586–1589): Dever de decidir 1586; Desistência 1587; Extinção do processo 1588; Fato superveniente 1589. Nenhuma antecipação.
- Decisão coordenada (L1624–1627): Decisão coordenada 1624; Discordância 1625; Ouvinte 1626; Sanção 1627 (1ª ocorrência em 1639, "sancionador"). Nenhuma antecipação.
- Arts. 53–55 (L1665–1669): Autotutela 1665; Anulação 1666; Revogação 1667 (a revogação da delegação, em 1388, tem outro sentido: aceito); Decadência 1668; Convalidação 1669.
- Recurso (L1702–1706): Recurso administrativo 1702 (já em 1374); Legitimidade recursal 1703; Não conhecer 1704; Preclusão administrativa 1705; Revisão do processo sancionador 1706 (1ª ocorrência em 1739). Nenhuma antecipação.
- Revisão e prioridade (L1745–1747): Contagem contínua 1745; Prioridade na tramitação 1746; Aplicação subsidiária 1747. Nenhuma antecipação.

---

## 3. Proveniência (D-ESTRATEGIA), os três lotes
- Busquei "Estratégia", "Herbert", "da aula" e "Aula <n>" em v2_producao.md: 0 ocorrências. O checa_pacote_v2 não tem bloqueio por esse padrão.
- Os CASOs e EXEMPLOs novos (despacho × portaria em L306; interceptação em L1544) são próprios e hipotéticos. Não achei tabela, exemplo ou questão de curso de terceiro. **Nenhum achado O.**

## 4. Itens intercalados
- DV1: DV1-01, 03, 04, 08, 10, 12, 13, 14, 17 e BQ-0137, BQ-0122, BQ-0148 (12). DV2: DV2-01, 02, 06, 09, 13, 15, 17, 18 e BQ-0150 (9). DV3: DV3-02, 07, 09, 10, 11, 12, 14, 15, 16, 18, 20 e BQ-0145, BQ-0132, BQ-0127 (14).
- Todos existem, são do tópico, têm rótulo AUTORAL ou CEBRASPE_ANALOGA e trazem `comentario` com três campos; a `decisiva` começa pelo código do mecanismo (adendo). Nenhum se repete na verificação (checa_pacote_v2 sem bloqueio).
- Proporção de caso: DV1 2/23 = 8,7%; DV2 2/21 = 9,5%; DV3 2/23 = 8,7%. Todos dentro da faixa de 5–10%.
- R, para o gbq-estilo: DV3-09 (L1904, "mesmo que haja disposição específica") nega a condição em vez de suprimi-la, e a segunda leitura daria NEG. Mantenho SUP, porque a pegadinha é SUP e a `decisiva` explica a troca. Na pegadinha do recurso (L1740), "atribui efeito suspensivo ao recurso (SUP)" não é SUP; é CON ou NEG (R).

## 5. Os três pontos levados à gcb-gerencia

**(a) Pegadinha da prioridade ligada a DV3-20 e BQ-0127, dois itens C.** Aceitável nesta fase como exceção declarada (R → PRÓXIMO), com uma correção de rota. Fui eu que, na R1 (A3), indiquei esses dois itens como evidência. A pegadinha está certa em si: SUP, A/B/MUDA coerentes, `par` e `texto` batem, e os dois itens mostram a regra certa ("Viraria E se a prioridade fosse concedida automaticamente", L2018). O defeito está no agrupamento de erros da plataforma: quem erra o DV3-20 cai em AP, não em SUP. A troca do DV3-19 que a produção propõe muda um gabarito sem necessidade. Recomendo o caminho mais barato: **acrescentar um DV3-21**, E SUP de prioridade ("deferida de ofício, independentemente de requerimento"), como item de verificação. Ele também resolve o (c). Outra saída é dar `comentario` e `mecanismo` ao D2-R69 (JSON L26957; E, 55 × 60 anos), que é CON e não SUP: aí a pegadinha passaria a CON. Não bloqueia o gatilho A.

**(b) Cotas fora da faixa: DV2 E/CON = 5; DV3 E/SUP = 4 e E/GEN = 0.** Aceito como ressalva R, não como O. Mas a causa alegada (§6.5) só explica uma parte:
- DV3: com 10 mini-lições, cada uma pedindo um E de evidência CON, SUP ou AUT, o conflito com a cota é real, porque o teto da cota soma 9 (CON 4 + SUP 3 + AUT 2). Hoje, porém, a evidência E cobre só 9 mini-lições (a da prioridade usa C), e o CON está em 3, abaixo do teto de 4. Recodificar uma das pegadinhas SUP como CON (por exemplo a do prazo, "cinco dias × três dias úteis") caberia na cota. GEN = 0 é o efeito de manter 10 E com um NEG; um 11º E caberia (a faixa é de 8 a 12).
- DV2: o conflito não é estrutural. São 6 mini-lições e 7 pegadinhas, e o 5º CON foi uma escolha. Uma das pegadinhas CON poderia ser AUT (por exemplo, quem aprecia a redistribuição) sem ferir o §6.5.
- Por que não é O: as cotas são aproximadas ("≈", ±3 pontos sobre o corpus), o desvio é de 1 item por código, e o §6.5 é regra qualitativa que deve prevalecer no conflito.
- Recomendo que a gcb-gerencia registre uma interpretação: "§6.5 prevalece sobre a cota de mecanismo; desvio de ±1 por código é aceito com justificativa". O reequilíbrio entra junto com os itens reais da onda 1 (PRÓXIMO).

**(c) Script com 8 (DV1) e 6 (DV3) questões de verificação, contra 33 e 29 por itemEdital.** As duas contas estão erradas, e a meta só se confirma no DV1 e no DV2.
- O script subtrai os intercalados reais (BQ) dos 20 itens DV, embora esses reais não estejam entre os 20. Por isso 20 − 12 = 8 e 20 − 14 = 6 (BACKLOG para a GBQ: contar por `itemEdital` e exigir `comentario`).
- A conta da produção inclui os itens antigos de D1/D2, que não têm `comentario`, `mecanismo` nem `tipo` (JSON L26830+; A16). A ESPEC §7 manda "mínimo de 10 por item-folha" e "todas com comentario". Minha R1 (§6) também argumentou por `itemEdital` sem esse filtro; corrijo aqui.
- Contando só os itens conformes (com `comentario`, fora dos intercalados): **DV1 11, DV2 12, DV3 9.** O DV3 fica abaixo de 10, e a pendência vira a O-R2-1.

## 6. Achados novos e condições

**Condições O (sem R3; aplica a gcb-cpp, confere a gcb-gerencia):**
- **O-R2-1 (DV3):** levar a verificação conforme a 10 ou mais, por um destes caminhos: (i) devolver o DV3-10 (2º ITEM em Atos, L1525) à verificação; (ii) criar o DV3-21 do §5(a); (iii) dar `comentario`, `mecanismo` e `tipo` a 1 ou mais itens D2 do 4.4. Recomendo o (ii) se houver QA normativo disponível; senão, o (i).
- **O-R2-2 (DV2, DV3):** pôr o artigo entre parênteses nos números de L713 (arts. 13, § 1º, e 15, § 1º), L994 (art. 18), L1305 (arts. 24 e 26, § 2º), L1307 (art. 49), L1501 (art. 24), L1503 (art. 26, § 2º) e L1594 (art. 49). A data já está na BASE LEGAL de cada bloco. Esses números estavam na v1, e a R1 não os apontou.

**R:**
- R-R2-1: DV2 L876 "cinco condições" ganha "(art. 25, II)".
- R-R2-2: uniformizar Sipec/SIPEC (L828, L987) e definir "requisição" e "exercício provisório" (L994), ou retirá-los.
- R-R2-3: o comando do DV2-18 (L1229) deixa de entregar o MUDA; sugestão: "provimento, vacância e deslocamento".
- R-R2-4: no mapa do DV2 (L721), o passo "Retorno" passa a incluir recondução e aproveitamento.
- R-R2-5: o MUDA de L1740 sai como "(CON)". A pegadinha própria de ato × fato e o par art. 57 × prazo do recurso ficam para a fase 2.
- R-R2-6: no resumo de D1 (JSON L37809), "estão nos lotes DV1 e DV3; este lote mantém" é vocabulário interno que a candidata vai ler. Trocar por "ver os módulos Ato administrativo e Processo administrativo". Conferir o mesmo em D2.

## 7. checa_pacote_v2 e checa_estilo_DA
- checa_pacote_v2_v2.md: **0 bloqueios confirmado.** Julgamento dos 12 avisos:
  - DIAG30, prefixos e lotes novos: aceitos (GBQ no build).
  - ITEM/quadros (6 avisos): aceitos como R.
  - Verificação 8 e 6: o número do script está errado, mas o DV3 tem de fato 9 conformes, e isso é a O-R2-1.
  - Marcas de produção 0 → 7: aceito (linhas `ITEM BQ-nnnn`; a GBQ confirma no build).
- checa_estilo_v2.txt: os 3 avisos de cota foram julgados no §5(b). As demais medidas estão dentro da faixa.

## 8. Veredito e pendências

| Lote | Veredito | Itens reprovados | Condição antes do gatilho A |
|---|---|---|---|
| DV1 (P1-DA-2.1) | **APROVADO COM RESSALVAS** | 0/23 | só R |
| DV2 (P1-DA-3.4) | **APROVADO COM RESSALVAS** | 0/21 | O-R2-2 |
| DV3 (P1-DA-4.4) | **APROVADO COM RESSALVAS** | 0/23 | O-R2-1, O-R2-2 |
| Total | APROVADO COM RESSALVAS | **0/67 = 0%** | sem GATE |

Pendências:
- **AGORA:** O-R2-1 e O-R2-2 (gcb-cpp, conferência da gcb-gerencia); ressalvas R2-1 a R2-4 do qa_normativo_R2; R-R2-3 e R-R2-6 (texto que a candidata lê, custo mínimo); ratificar em D1 as duas decisões do produtor (as quatro unidades do item 2; o DV3 como uma unidade) e a exceção (a).
- **PRÓXIMO:** DV3-21 SUP de prioridade (se não for a via da O-R2-1); reequilíbrio das cotas (b) com a onda 1; A15 (fase 2); A16; R-R2-1, 2, 4 e 5; DIAG30, painel e LOTE_INFO (GBQ no build).
- **BACKLOG:** checa_pacote_v2.py contando a verificação por `itemEdital` e com `comentario`; heurística de "comando que entrega o par" no checa_estilo_DA; lista DAD de pares (anexo do Fundador); condensar os arts. 53–55 do DV3.
- **DESCARTADO:** tratar os avisos de ITEM/quadros e de marcas de produção como defeito; trocar o gabarito do DV3-19 para resolver (a).
- **Em aberto para a GCB após a rodada final:** a linha 6 (ITEM a cada 2–3 quadros) segue como aviso nos três lotes, por decisão de formato. A linha 5 continua sem a lista DAD. A A16 impede medir a proporção de caso no tópico inteiro.
