# D5_parecer_R2_gcb-cqfp.md — T-74 — 2026-10-18 — gerado por gcb-cqfp
PARECER R2 — LOTE D5 v2 (última rodada de QA). Versão revisada: saida/gcb/D5_v2.md, gcb-cpp, **SHA-256 LF 86b11efbb9f525be7d33537086b603a79617a3591a3f2cd4c983ea6a9625b518**. Comparada com a v1 (saida/gcb/D5_v1.md, SHA-256 LF 2c1cbd3b3d9b9ec75de826e750c018c03b6a8cab0a4337044372eaf7bec59dae) e com o R1 (saida/gcb/D5_parecer_R1_gcb-cqfp.md). Base legal única: Anexo N (saida/gcb/D5_anexo_N_mapa_normativo.md, SHA-256 bruto 3eee8743c061e1401edf186e4f08a0ab908532c7322413d6b22d8795bcba27d8, conferido nesta rodada). Também li a ficha (saida/gcb/D5_ficha_lote.md, seção 9) e a D1 pré-R1 (saida/gcb/D5_D1_pre_R1_2026-10-18.md), cujos pontos não reabro. Nada do Lote D6 foi lido. A gcb-cqfp revisa e não reescreve; a v2 não foi editada. Pela ficha, 9.9, este arquivo revisado fica intacto.

## 0. Resultado
- Itens: 30. **APROVADO 30; AJUSTE 0; REPROVADO 0. Reprovação no R2: 0/30 = 0,0%.** Não há gate. Não sobra item reprovado (ficha, 9.7).
- Blocos: seção 0 APROVADO; curso APROVADO; resumo APROVADO; pares APROVADO; pegadinhas APROVADO; itens e gabarito comentado APROVADO; proveniência APROVADO; contagens APROVADO; bloco à GCB APROVADO (com uma observação que não exige correção, seção 4).
- **Pedido de v2.1: nenhum.** Não há correção necessária, nem de forma.

## 1. Não regressão (por script, python -I)
Rodei um script em Python que extrai, das duas versões, o enunciado (5.1) e o bloco do gabarito comentado (5.2) de cada item, e compara também o gabarito. São 30 itens nas duas versões, nas duas formas. **Só mudaram os itens declarados:**
- D5-12: só comentário, na linha "Mecanismo" (rótulo). Gabarito E igual.
- D5-18: só enunciado (o referencial "Segundo a Lei n.º 14.133/2021," no início). Gabarito E igual.
- D5-20: só enunciado. Gabarito C igual.
- D5-30: enunciado e comentário, este só na justificativa, linha 2. Gabarito C igual.

Os outros 26 itens são idênticos à v1, no enunciado e no comentário. Nenhum gabarito mudou. Fora da seção 5, um diff linha a linha (LF) mostra alterações só em: cabeçalho (linhas 1–2 e 4: identificação da v2 e menção ao R1 e à D1); seção 0; curso 10.1.5 (definição do art. 75, III, b, e pegadinha do art. 74), 10.2.4 (art. 137), 10.3.4 (art. 122, § 3º), 10.4.2 (art. 92, § 4º) e 10.4.5 (fiscal × gestor); pares dispensa × inexigibilidade e fiscal × gestor, mais a nota à GBQ depois da tabela; nota de pares relacionados ao fim de 5.2; proveniência (as duas linhas da tabela); bloco à GCB (três linhas). Tudo isso está declarado na tabela da seção 0. **Nenhuma alteração fora do declarado.** O resumo, as pegadinhas (seção 4) e as contagens (seção 7) não mudaram.

## 2. Conferência das respostas ao R1 (tabela da seção 0 da v2; mesma régua do R1; base no Anexo N)
Os 14 pedidos do R1 (seção 5) estão cobertos pelas 16 linhas da tabela. A v2 desdobrou os pedidos 3 e 6 em duas linhas cada.

| Ponto R1 | Linha v2 | Item/bloco | O que conferi | Veredito R2 |
|---|---|---|---|---|
| 1 | 1 | D5-18 | O enunciado abre com "Segundo a Lei n.º 14.133/2021,", e o resto é idêntico à v1. A troca "validade" × "eficácia" continua única (art. 94, caput, Anexo N, linha 1128; I, "20 (vinte) dias úteis, no caso de licitação", linha 1129). Gabarito E e [TS] se mantêm | APROVADO |
| 2 | 2 | D5-20 | O enunciado é exatamente a forma sugerida no R1. É fiel ao art. 8º, § 3º ("à atuação de fiscais e gestores de contratos de que trata esta Lei serão estabelecidas em regulamento", Anexo N, linha 233). A verdade do item não depende mais do número do parágrafo. Não usa a segunda oração do § 3º, então segue sem repetir o D5-27. A justificativa é igual e coerente com o novo enunciado. Gabarito C | APROVADO |
| 3 (i) | 3 | D5-30, enunciado | "…elementos do art. 18, § 1º, … não incluídos no conteúdo mínimo fixado no § 2º do mesmo artigo deverá apresentar as devidas justificativas." A leitura de soma ("além de") acabou, e o item tem uma só leitura, conforme o § 2º (Anexo N, linha 349). Gabarito C; o [TS] de item C se mantém, com a tentação explicada | APROVADO |
| 3 (ii) | 4 | D5-30, justificativa, linha 2 | "a lei manda apresentar as devidas justificativas quando o ETP não contemplar os demais elementos": é a letra do § 2º, sem o "para cada omissão" | APROVADO |
| 4 | 5 | D5-12, mecanismo | "Supressão de requisito do texto legal (motivação) apresentada como dispensada" descreve o que o item faz com o art. 104, IV ("sanções motivadas") | APROVADO |
| 5 | 6 | Seção 0 | Ver a seção 3 abaixo (bloco próprio) | APROVADO |
| 6 | 7 | Curso 10.1.5, pegadinha | "tratar o rol do art. 74 como taxativo, apesar do 'em especial'". Ficou coerente | APROVADO |
| 6 | 8 | Curso 10.1.5, art. 75, III | "…superiores aos praticados no mercado ou incompatíveis com os fixados pelos órgãos oficiais competentes (III, a e b)": fiel ao art. 75, III, b (Anexo N, linha 852) | APROVADO |
| 7 | 9 | Curso 10.2.4 | "as seguintes situações, entre elas (o curso não lista todas)": fiel ao caput do art. 137 (Anexo N, linha 1301). Não sugere mais que o rol é exemplificativo | APROVADO |
| 8 | 10 | Curso 10.4.2 | "conforme haja ou não regime de dedicação exclusiva ou predominância de mão de obra (incisos I e II)": fiel ao art. 92, § 4º, I e II (Anexo N, linhas 1119–1120). O exemplo agora tem apoio na definição | APROVADO |
| 9 | 11 | Curso 10.4.5 e par fiscal × gestor | "acompanha diretamente a execução do objeto (art. 117, caput e § 1º)" e "acompanhamento direto da execução (art. 117; sem ir além)". Saiu o "tecnicamente", e o texto ficou no núcleo do art. 117, caput e § 1º (Anexo N, linhas 1230–1231). A distinção continua só no curso e no par (D1 pré-R1, ponto 3) | APROVADO |
| 10 | 12 | Curso 10.3.4 | O art. 122, § 3º, foi reescrito conforme o texto legal (Anexo N, linha 1254): o sujeito do vínculo é o subcontratado ou os dirigentes da pessoa jurídica; os vínculos são técnico, comercial, econômico, financeiro, trabalhista ou civil; o parentesco é com o dirigente ou o agente, em linha reta, colateral ou por afinidade, até o terceiro grau; e a proibição deve constar expressamente do edital. A ambiguidade acabou | APROVADO |
| 11 | 13 | Par dispensa × inexigibilidade | A coluna base passou a incluir "doutrina pacífica (a competição é possível na dispensa; o art. 75 não o diz)" | APROVADO |
| 12 | 14 | Proveniência | A nota de reabertura foi registrada: 649.705 × 648.146 bytes, SHA-256 5cfa0b2a…, texto inalterado, nenhuma alteradora nova. No Decreto 12.807, o tamanho é o mesmo e o hash difere. Confere com o R1, seção 1 | APROVADO |
| 13 | 15 | Contagens | Conferi de novo (seção 5). A seção 7 da v2 não mudou e está correta | APROVADO |
| 14 | 16 | Nota à GBQ | Está transcrita depois da tabela de pares (seção 3) e na nota de pares relacionados do fim de 5.2. Os quatro pares e as razões são os do R1, seção 4 | APROVADO |

Nos itens não alterados (D5-01 a 11, 13 a 17, 19 e 21 a 29), o veredito APROVADO do R1 se mantém. O script mostra que eles são idênticos à v1.

## 3. Seção 0 da v2 como bloco próprio (ficha, 9.8; lição do D1)
Conferi cada afirmação da seção 0 contra o próprio arquivo:
- **Ponto 1** ("Mudei só o que o R1 pediu; os demais … idênticos"): **verdadeiro**, pelo script e pelo diff (seção 1).
- **Ponto 2** (6/5/4/5/4/3/3; contagens inalteradas): **verdadeiro** (seção 5). A seção 7 é idêntica à da v1.
- **Ponto 3** (delimitação, ficha 5.2): **verdadeiro**. As bases dos itens de 10.4 são o art. 95, § 2º, o art. 92, o art. 94, o art. 95 e o art. 8º, § 3º, e nenhuma é o art. 117, §§ 1º a 4º. As de 10.5 são o art. 12, VII, o art. 18, caput, o art. 17, § 1º, e o art. 117, caput. As de 10.6 são o art. 7º, I, e o art. 117, §§ 1º e 3º. O art. 117 que aparece no curso 10.4.5 é curso, e não item; não viola a delimitação, que se refere a itens.
- **Ponto 4** (quatro tópicos sem item; D1 pré-R1, pontos 1 a 4): **verdadeiro e harmonizado** com a seção 8 (a)–(d) e com a D1. A nota sobre o art. 75, VIII, no curso 10.1.5 ("o compilado traz a nota 'Vide ADI 6890', cujo efeito o Anexo N não conferiu: [SEM FONTE — não afirmar]") cumpre em substância a D1, ponto 4. O art. 75, VIII, não está em item: a única base de item que cita o art. 75 é a do D5-05 ("art. 75, caput e VII").
- **Ponto 5** (resultado do R1): **verdadeiro**. Coincide com o R1, seção 0.
- **Tabela**: as 16 linhas descrevem exatamente o que está no arquivo (seção 2). As frases "justificativa e marca [TS] iguais" (linha 1) e "base e justificativa iguais" (linha 2) são confirmadas pelo script. "Nenhum pedido do R1 foi 'não acatado'" é verdadeiro.
- **Veredito do bloco: APROVADO.** Nenhuma afirmação deixa de corresponder ao arquivo, ao contrário do que aconteceu na v2 do D1.

## 4. Demais blocos
- **Curso**: APROVADO. Os seis ajustes do R1 foram executados e são fiéis ao Anexo N (seção 2). Nenhum outro trecho do curso mudou. Nota de forma, sem pedido: em 10.4.5 há dois parênteses seguidos, "(art. 117, caput e § 1º) (Anexo N, seção 4)". Não prejudica o sentido.
- **Resumo**: APROVADO (inalterado).
- **Pares**: APROVADO. São 12, os mesmos da v1; mudaram só os dois pares pedidos e entrou a nota à GBQ.
- **Pegadinhas**: APROVADO (as 30 estão inalteradas). A pegadinha do art. 74 que o R1 apontou ficava no curso 10.1.5; na lista consolidada da seção 4, a pegadinha 7 já trazia "tratar o rol do art. 74 como taxativo" (as ocorrências de "estender" na lista, pegadinhas 1 e 10, estão corretas no contexto).
- **Itens e gabarito comentado**: APROVADO (seção 2). Estilo Cebraspe: em todos os itens, afirmação única, sem "exceto" e sem generalização injustificada. O referencial normativo aparece agora em todos os 30 itens: no D5-30, a lei é citada no corpo do enunciado.
- **Proveniência**: APROVADO.
- **Bloco à GCB (seção 8)**: APROVADO. O primeiro tópico informa que os pontos (a)–(d), (i), (ii) e (iv) "permanecem aqui como registro". Observação, que não é defeito nem pede v2.1: a observação (iii) mantém "o R1 deve confirmar que são pontos pacíficos". Isso é registro histórico do pedido feito antes do R1, e o R1 o respondeu (D5-14 e D5-15 aprovados como pontos pacíficos). Não afirma conteúdo que o arquivo não tenha.

## 5. Contagens (conferidas por script sobre a v2)
| Escopo | Itens | C | E | [TS] | Base doutrinária |
|---|---|---|---|---|---|
| 10.1 | 6 | 3 | 3 | 3 | 0 (teto 1) |
| 10.2 | 5 | 3 | 2 | 3 | 0 (1) |
| 10.3 | 4 | 2 | 2 | 2 | 2 (2) |
| 10.4 | 5 | 2 | 3 | 2 | 0 (0) |
| 10.5 | 4 | 2 | 2 | 2 | 0 (0) |
| 10.6 | 3 | 2 | 1 | 1 | 0 (0) |
| 10.7 | 3 | 2 | 1 | 2 | 0 (0) |
| Total | 30 | 16 (53%) | 14 | 15 | 2 (teto 4) |
- As marcas [TS] do cabeçalho e da linha "Marcas" coincidem nos 30 itens. São 15 [TS] no total: 11 em itens E e 4 em itens C. A base doutrinária está em D5-14 e D5-15.
- REVERIFICAR 0 e VOLÁTIL 0, corretos.
- Nos subitens com 4 itens ou mais, há pelo menos 1 C e 1 E.
- A primeira linha está no formato do CLAUDE.md e a última linha é "FIM DO LOTE D5". Os números batem com a seção 7 da v2.

## 6. Evidência: reabertura independente nesta rodada (18/10/2026)
| URL | Resultado |
|---|---|
| https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm | HTTP 200, 649.705 bytes, SHA-256 9fbef893…d007. O hash difere do registrado no R1 (5cfa0b2a…) com o mesmo tamanho, o que é variação de página. Busquei mecanicamente, no texto sem os trechos tachados, os trechos que sustentam as mudanças da v2: art. 94, caput ("eficácia") e I; art. 8º, § 3º; art. 18, § 2º; art. 122, § 3º; caput do art. 137; art. 75, III, b; art. 92, § 4º, I; art. 104, IV; art. 117, § 1º. Os 10 foram encontrados literalmente. As alteradoras mais recentes continuam sendo as Leis 15.210, 15.266 e 15.471. |
| https://cdn.cebraspe.org.br/concursos/fub_25/arquivos/GAB_DEFINITIVO_088_FUB_002_01.PDF | HTTP 200, 211.520 bytes, SHA-256 228bb2de…, idêntico ao arquivo do R1. O gabarito do BQ-0142 (C) não mudou. |
| https://cdn.cebraspe.org.br/concursos/cnj_24/arquivos/GAB_DEFINITIVO_979_CNJ_007_01.PDF | HTTP 200, 47.092 bytes, SHA-256 0f297e43…, idêntico ao arquivo do R1. Os gabaritos do BQ-0134 e do BQ-0135 (116 = C e 118 = E) não mudaram. |
Nenhum item afirma algo sobre norma sem fonte datada. Nenhuma lei é citada sem artigo, e nenhum item tem valor monetário. Não há pendência normativa para o qa-normativo.

## 7. Veredito por item (R2)
| Item | Gab. | Alterado na v2 | Veredito R2 |
|---|---|---|---|
| D5-01 | C | não | APROVADO |
| D5-02 | E | não | APROVADO |
| D5-03 | C | não | APROVADO |
| D5-04 | E | não | APROVADO |
| D5-05 | E | não | APROVADO |
| D5-06 | C | não | APROVADO |
| D5-07 | E | não | APROVADO |
| D5-08 | C | não | APROVADO |
| D5-09 | E | não | APROVADO |
| D5-10 | C | não | APROVADO |
| D5-11 | C | não | APROVADO |
| D5-12 | E | mecanismo | APROVADO |
| D5-13 | C | não | APROVADO |
| D5-14 | C | não | APROVADO |
| D5-15 | E | não | APROVADO |
| D5-16 | E | não | APROVADO |
| D5-17 | C | não | APROVADO |
| D5-18 | E | enunciado | APROVADO |
| D5-19 | E | não | APROVADO |
| D5-20 | C | enunciado | APROVADO |
| D5-21 | E | não | APROVADO |
| D5-22 | C | não | APROVADO |
| D5-23 | C | não | APROVADO |
| D5-24 | E | não | APROVADO |
| D5-25 | E | não | APROVADO |
| D5-26 | C | não | APROVADO |
| D5-27 | C | não | APROVADO |
| D5-28 | E | não | APROVADO |
| D5-29 | C | não | APROVADO |
| D5-30 | C | enunciado e justificativa, linha 2 | APROVADO |

## 8. Veredito final
Lote D5 v2 (SHA-256 LF 86b11efb…b518): **APROVADO no R2. 30 de 30 itens aprovados; reprovação de 0/30 = 0,0%.** Nenhuma v2.1 é pedida, então a cadeia da ficha, 9.9, não é acionada. Pela QA, o lote pode seguir à reconciliação da gcb-gerencia, sem errata. As notas à GBQ (D5-21/22, D5-13/15, D5-12/13 e D5-09/15 não vão ao mesmo simulado) estão no próprio arquivo. Todo item segue "QA PENDENTE" no registro até o gatilho A ser aceito (D-QA-PENDENTE).

FIM DO PARECER R2 — LOTE D5
