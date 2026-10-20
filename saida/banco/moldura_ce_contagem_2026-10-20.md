# moldura_ce_contagem_2026-10-20.md — T-122 (parte de contagem; D-MOLDURA-CE; D-AUDITORIA-20OUT) — 2026-10-20 — gerado por gcb-cpp

Contagem dos itens com MOLDURA DO LEGISLATIVO no pacote v1.13 canônico, por matéria (P1-TI, P2, P1-DA) e por folha (itemEdital). Esta peça é só a contagem; a meta final de E (quantos E faltam para ficar entre 40% e 60% de C) é da gbq-gerencia, que consolida em saida/banco/moldura_ce_2026-10-20.md. A coluna "E faltante" abaixo é dado auxiliar, calculado só com a fórmula da ordem.

## 0. Objetos e reprodução

| objeto | SHA-256 |
|---|---|
| saida/pacote/pacote.json (v1.13 canônico, 1.159 itens, C/E 582/577; entrada, não alterada) | `82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240` |
| saida/banco/moldura_ce.py (script) | `5723698e9a718b106a523cac6774f3ed5f23f39a09e9a0d02fd59ecf9ddcca96` |
| saida/banco/moldura_ce_itens_2026-10-20.csv (1.159 linhas + cabeçalho; UTF-8, LF, separador ";") | `ed4b364dffbca7d9e8878591914783258fa7048c4f1837d98c3d62e34981daac` |

Reprodução: `python3 -I saida/banco/moldura_ce.py` (raiz do repositório como argumento opcional). O script aborta se o SHA-256 do pacote diferir do acima, lê só o pacote, grava só o CSV e imprime as tabelas das seções 3 a 5. Duas execuções seguidas produzem o mesmo CSV (conferido). Colunas do CSV: id; materia; itemEdital; gabarito; moldura (S/N); termo (até 3 termos distintos que dispararam, na ordem do texto); borda (decisão de fronteira aplicada, vazio se a moldura é inequívoca); sinal_fraco (nos itens N, termos fracos presentes: sessão, orador, audiência, pronunciamento, discurso, proposição, taquigrafia etc.).

## 1. Critério escrito

**Texto avaliado:** comando + textoBase + enunciado do item. Não entram justificativa, certame, cargo nem url (a justificativa pode citar a Câmara sem que o item o faça).

**moldura = S** quando o texto põe a situação no Poder Legislativo, por pelo menos um destes termos (regex em saida/banco/moldura_ce.py, lista T):
1. a Câmara dos Deputados ou "a Câmara" (Câmara com maiúscula; "Câmara de Comércio" e "Câmara Arbitral" ficam fora; palavra citada entre aspas como menção, ex.: "Câmara" × "câmara", também fica fora);
2. Congresso, Senado, Senador, parlamento (nacional, estrangeiro ou genérico), parlamentar (inclusive "termos/transcrições/textos parlamentares" e "Interparlamentar"), Deputado, vereador atuando como tal;
3. "Poder Legislativo", "órgão legislativo", "Casa legislativa", "sessão legislativa", Assembleia Legislativa, inclusive a abertura "Considere que um órgão do Poder Legislativo da União…" e "uma das Casas do Poder Legislativo da União";
4. Plenário e "sessão plenária"; Mesa (Ato da Mesa, Mesa Diretora); Derep/DETAQ, Coordenação de Registro Oficial, Pequeno Expediente, Colégio de Líderes; "a Casa" com maiúscula (nas fontes da fábrica, a Câmara; "Casa Civil" fica fora);
5. comissão/comissões: em P1-TI e P2, qualquer uso (nesses lotes só aparece a comissão legislativa: "reunião de comissão", "gravações de comissões", "Comissão de Constituição e Justiça"); em P1-DA só com qualificador legislativo (permanente, temática, mista, parlamentar), porque lá "comissão" é, de regra, cargo em comissão, comissão processante, comissão de licitação ou de recebimento;
6. fronteira de domínio (S com borda "dominio"/"cpi"/"assembleia"): "domínio, como o legislativo", "proposições legislativas", a sigla CPI e "assembleia" fora de "assembleia geral/de acionistas/de credores".

**moldura = N** quando o item: (a) só cita lei, edital ou norma; (b) cita o Poder Legislativo em rol com outro Poder ou com o Ministério Público (ex.: "Poderes Legislativo e Judiciário"); (c) usa "legislativo/a" como função ou espécie de norma (delegação legislativa, autorização legislativa, técnica legislativa); (d) usa "câmara" em sentido não legislativo ou como palavra citada; (e) usa só termos fracos sem âncora institucional: "sessão", "orador", "audiência (pública)", "pronunciamento", "discurso", "proposição", "ata", "notas taquigráficas", "registro oficial", "questão de ordem" e "tribuna" como expressão ou corpus, ou a sigla/nome de órgão legislativo ausente (ex.: PEC em mapa de sinônimos).

**Decisões de fronteira (registradas para a gbq-gerencia poder revê-las; todas aparecem na coluna borda ou sinal_fraco do CSV):**
- Legislativo municipal/estadual: contaria como S (Câmara Municipal, Assembleia Legislativa, vereador atuando como tal). Não há item com Câmara Municipal; "mandato de vereador" como causa de afastamento de servidor (D2-03, Lei 8.112) é regime do servidor e fica N.
- Legislativo estrangeiro (Câmara dos Comuns do Canadá, Parlamento da Estônia, Senado e Câmara dos Deputados da Itália, Conselho de Representantes do Bahrein, "um parlamento"): S, com borda "estrangeiro" (6 itens: 3 C, 3 E).
- "Poder Legislativo" como único Poder da frase, sem órgão, servidor ou Casa em cena (D1-08, D6-25): S, borda "poder_isolado" (2 itens, ambos C). Em rol com outros Poderes (D1-03, D1-16, D6-19): N.
- Nome de órgão legislativo usado como termo de vocabulário do ASR (sigla CPI, Comissão de Constituição e Justiça): S (o órgão é nomeado); expressão de jargão sem órgão ("questão de ordem") e "notas taquigráficas" como corpus: N.
- Sessão, orador, audiência e pronunciamento sem âncora institucional: N, mas contados na seção 5 (sensibilidade), porque no módulo P2 o leitor entende que são do Legislativo.

## 2. Amostra conferida à mão

Método: li o texto completo (comando, textoBase e enunciado) de cada item da amostra e anotei S ou N pelo critério da seção 1, sem olhar a coluna do script; depois comparei com o CSV. Amostra de **32 itens marcados S e 47 marcados N** (mínimo pedido: 20 e 20): os de fronteira escolhidos por termo (rol de Poderes, sessão/orador/audiência sem âncora, comissão em DA, Casa Civil, mandato de vereador, estrangeiros, domínio, CPI, taquigrafia) e, para cobrir os casos comuns, itens sorteados com `random.seed(20261020)` em cada matéria (entradas "sorteio").

**Rodadas.** Na 1ª rodada o script tinha 3 defeitos, achados na conferência e corrigidos antes desta versão: (1) erro de regex em "Poder Legislativo" (`Poderes?` não casava "Poder"), que deixava de marcar 38 itens de P1-DA (15 → 53 itens com moldura); (2) 7 falsos positivos em P2 — "registro oficial" genérico (L1C-Q29, L2-Q04), "questão de ordem" como expressão de vocabulário (L2-R117) e "notas taquigráficas" como corpus de modelo de linguagem ou de busca (L1-R39, L3-R19, L3-R23, L3-R27) —, resolvidos tirando "taquigrafia", "questão de ordem", "tribuna" e "registro oficial" (minúsculas) da lista de gatilhos (ficam como sinal fraco); (3) falta de marca de borda no caso de A5-10 ("comissões temáticas" em P1-TI), que agora sai com borda `comissao_sem_ancora`. Na 2ª rodada (script final, SHA da seção 0) a amostra inteira foi relida contra o CSV: **0 divergência em 32 itens S e 0 em 47 itens N; nenhum falso positivo nem falso negativo na amostra**.

Além da amostra, na 1ª rodada li, um a um, os 328 itens de P2 marcados N que não são BQ (os 7 que passaram a N na 2ª rodada estão na amostra) e os itens N de P1-TI e P1-DA com sinal fraco, procurando falso negativo; os casos duvidosos são os da lista de fronteira da seção 1. Os 21 itens BQ de P2 (CEBRASPE_ANALOGA de outros certames) não citam Câmara, Congresso, Senado, parlamento, Deputado nem Legislativo (conferido no CSV: os 21 saem N e sem sinal fraco; BQ-0084 cita o Regimento Geral da UnB, que não é o Regimento da Câmara).

### 2.1 Itens S (leitura manual S; script S)

| id | folha | gab. | leitura manual | script | termo / sinal fraco | borda | nota |
|---|---|---|---|---|---|---|---|
| D1-08 | P1-DA-1 | C | S | S | poder legislativo | poder_isolado | Poder Legislativo isolado, sujeito único (borda) |
| D6-25 | P1-DA-11 | C | S | S | poder legislativo | poder_isolado | Poder Legislativo isolado, âmbito de norma (borda) |
| A5-10 | P1-8.2 | E | S | S | comissões | comissao_sem_ancora | "comissões temáticas" em TI, sem Câmara (borda) |
| A5-01 | P1-7.1 | C | S | S | proposições legislativas | dominio | "proposições legislativas" (borda de domínio) |
| L2-R81 | P2-2.5 | C | S | S | CPI; c.p.i. | cpi | sigla CPI como termo de vocabulário (borda) |
| L3-R38 | P2-3.2 | C | S | S | assembleia | assembleia | "assembleia" em P2 (borda) |
| L3-Q16 | P2-3.4 | C | S | S | domínio, como o legislativo | dominio | "domínio, como o legislativo" (borda) |
| L2-R143 | P2-2.2 | C | S | S | Câmara; interparlamentar; parlamentar | estrangeiro | Câmara dos Comuns do Canadá (estrangeiro) |
| L3-R99 | P2-3.1 | C | S | S | interparlamentar | estrangeiro | Conselho de Representantes do Bahrein (estrangeiro) |
| L1-R05 | P2-1.3 | C | S | S | casa | — | "equipe da Casa" (maiúscula) |
| L1-R70 | P2-1.4 | C | S | S | comissão | — | "reunião de comissão" sem Câmara |
| L1-R24 | P2-1.1 | E | S | S | Plenário | — | "gravações de Plenário" |
| L1-R15 | P2-1.7 | E | S | S | plenária | — | "sessão plenária" |
| L1-Q12 | P2-1.6 | E | S | S | parlamentares | — | "termos parlamentares" |
| L2-Q09 | P2-2.3 | E | S | S | parlamentares | — | "transcrições parlamentares" |
| L3-R20 | P2-3.1 | E | S | S | parlamento | — | "pronunciamentos de um parlamento" |
| L1-R16 | P2-1.8 | C | S | S | Câmara | — | "A Câmara" sem "dos Deputados" |
| L2-R42 | P2-2.2 | E | S | S | mesa; plenárias; registro oficial | — | Ato da Mesa / Derep |
| L4-R01 | P1-5.2 | C | S | S | Câmara | — | "unidade da Câmara" em TI |
| D2-53 | P1-DA-4.2 | C | S | S | poder legislativo; casa | — | "Casas do Poder Legislativo da União" |
| L6B-R01 | P1-4.3 | C | S | S | derep; detaq; casa | — | Derep em TI |
| D4-02 | P1-DA-8.1 | C | S | S | Câmara; Deputados | — | audiência de comissão da Câmara dos Deputados |
| L4-R06 | P1-5.2 | E | S | S | Câmara | — | sorteio |
| L3-R51 | P2-3.3 | E | S | S | Câmara; Deputados | — | sorteio |
| L3-R97 | P2-3.1 | C | S | S | senado; interparlamentar; plenário | estrangeiro | sorteio (Senado da Itália) |
| L2-R83 | P2-2.5 | C | S | S | comissão | — | sorteio |
| L3-R08 | P2-3.4 | C | S | S | comissão | — | sorteio |
| L3-Q03 | P2-3.1 | E | S | S | parlamentos | — | sorteio |
| D4-64 | P1-DA-9.4 | C | S | S | Câmara; Deputados | — | sorteio |
| D2-45 | P1-DA-4.1 | C | S | S | poder legislativo | — | sorteio |
| D5-16 | P1-DA-10.2 | C | S | S | poder legislativo | — | sorteio |
| D3-45 | P1-DA-6.3 | C | S | S | poder legislativo | — | sorteio |

### 2.2 Itens N (leitura manual N; script N)

| id | folha | gab. | leitura manual | script | termo / sinal fraco | borda | nota |
|---|---|---|---|---|---|---|---|
| D1-03 | P1-DA-1 | E | N | N | Poder em rol;legislativ(o/a) | — | rol dos Poderes da União |
| D1-16 | P1-DA-1.1 | E | N | N | Poder em rol;legislativ(o/a) | — | "Poderes Legislativo e Judiciário" em rol |
| D6-19 | P1-DA-11 | C | N | N | Poder em rol;legislativ(o/a) | — | Legislativo em rol com Judiciário e MP |
| D2-03 | P1-DA-3.1 | E | N | N | mandato de vereador | — | "mandato de vereador" como causa de afastamento do servidor (borda) |
| D3-13 | P1-DA-5.2 | E | N | N | legislativ(o/a) | — | "delegação legislativa" (função/norma) |
| D1-25 | P1-DA-1.2 | C | N | N | legislativ(o/a) | — | "autorização legislativa" |
| D2-13 | P1-DA-3.2 | E | N | N | — | — | "cargos em comissão" |
| D2-62 | P1-DA-4.3 | E | N | N | — | — | comissão processante |
| D4-28 | P1-DA-8.4 | E | N | N | — | — | Casa Civil |
| D1-45 | P1-DA-2.1 | C | N | N | ata | — | "órgãos colegiados e comissões", ata |
| D3-71 | P1-DA-7 | E | N | N | — | — | "cargo, mandato" |
| L1C-Q30 | P2-1.5 | E | N | N | câmara (sentido não legislativo) | — | "Câmara" entre aspas (menção) |
| L3-R21 | P2-3.1 | E | N | N | — | — | sigla PEC em mapa de sinônimos |
| L1-R12 | P2-1.6 | E | N | N | sessão | — | "sessão" como palavra |
| L2-Q03 | P2-2.1 | E | N | N | sessão | — | "notas oficiais de sessões" (sessão sem âncora) |
| L1-R132 | P2-1.1 | C | N | N | sessão | — | "sessão" sem âncora |
| L1-R171 | P2-1.4 | C | N | N | audiência;sessão | — | "audiência" e "presidente da sessão" sem âncora |
| L1-R170 | P2-1.4 | E | N | N | — | — | "comitê" |
| L3-R106 | P2-4.1 | E | N | N | audiência | — | "audiência", órgão público |
| L2-Q13 | P2-2.4 | C | N | N | orador | — | "oradores" |
| L4-R07 | P1-5.2 | C | N | N | — | — | "casa" (imóvel) |
| BQ-0084 | P2-4.1 | C | N | N | — | — | Regimento da UnB |
| A5-02 | P1-7.1 | C | N | N | proposição | — | "base de proposições", PL (sem âncora) |
| 4C-10 | P1-5.1 | E | N | N | orador | — | "orador" |
| L3-Q01 | P2-3.1 | C | N | N | pronunciamento;proposição | — | "pronunciamentos", "proposições" (sem âncora) |
| L3-R03 | P2-3.2 | E | N | N | pronunciamento | — | "acervo de pronunciamentos" |
| L1-R89 | P2-1.6 | C | N | N | audiência | — | "audiência pública" sem âncora |
| L1-R39 | P2-1.2 | C | N | N | taquigrafia | — | "notas taquigráficas" como corpus (só taquigrafia) |
| L3-R19 | P2-3.1 | E | N | N | taquigrafia | — | "notas taquigráficas de um acervo" |
| L3-R23 | P2-3.1 | C | N | N | taquigrafia | — | idem |
| L3-R27 | P2-3.2 | C | N | N | taquigrafia | — | idem |
| L2-R117 | P2-2.8 | E | N | N | questão de ordem | — | "questão de ordem" como expressão de vocabulário |
| L1C-Q29 | P2-1.5 | C | N | N | registro oficial | — | "registro oficial" genérico |
| L2-Q04 | P2-2.1 | C | N | N | registro oficial;sessão | — | "registro oficial da sessão" |
| 6B-10 | P1-4.2 | E | N | N | — | — | sorteio |
| BQ-0106 | P1-5.2 | C | N | N | — | — | sorteio |
| BQ-0079 | P1-2 | E | N | N | — | — | sorteio |
| A5-12 | P1-8.2 | E | N | N | — | — | sorteio |
| L1-R82 | P2-1.5 | C | N | N | — | — | sorteio |
| L3-R59 | P2-3.4 | E | N | N | orador | — | sorteio |
| L1-R14 | P2-1.7 | C | N | N | — | — | sorteio |
| L1-Q15 | P2-1.7 | C | N | N | — | — | sorteio |
| L1-R31 | P2-1.1 | C | N | N | — | — | sorteio |
| D6-15 | P1-DA-11 | E | N | N | — | — | sorteio |
| D6-37 | P1-DA-12 | E | N | N | — | — | sorteio |
| D5-17 | P1-DA-10.2 | E | N | N | — | — | sorteio |
| D2-59 | P1-DA-4.2 | C | N | N | — | — | sorteio |

## 3. Totais por matéria (itens com moldura)

| matéria | itens com moldura | C | E | %C | E faltante p/ %C ≤ 60% (aux.) |
|---|---|---|---|---|---|
| P1-TI | 7 | 4 | 3 | 57.1% | 0 |
| P2 | 208 | 112 | 96 | 53.8% | 0 |
| P1-DA | 53 | 44 | 9 | 83.0% | 21 |
| TOTAL | 268 | 160 | 108 | 59.7% | 0 |

Fórmula do dado auxiliar: x = ceil(C/0,60 − (C+E)) quando %C > 60%, senão 0 (calculada em inteiros: x = ceil((2C − 3E)/3) se 2C > 3E). Não é a meta final: a meta, com o piso de 40% e a regra por leva, é da gbq-gerencia.

Universo (itens do pacote por matéria e fração com moldura):

| matéria | itens | com moldura | % do universo |
|---|---|---|---|
| P1-TI | 185 | 7 | 3.8% |
| P2 | 564 | 208 | 36.9% |
| P1-DA | 410 | 53 | 12.9% |

## 4. Totais por folha (itemEdital)

P1-DA-1 e P1-DA-8 são os itens de edital sem subitem; a contagem é a do itemEdital como gravado no pacote (a D-COBERTURA-AUTO as trata como itens fora de folha; aqui entram como linhas próprias).

### 4.1 P1-TI

| folha | itens no pacote | com moldura | C | E | %C | E faltante |
|---|---|---|---|---|---|---|
| P1-1 | 16 | 0 | 0 | 0 | — | 0 |
| P1-2 | 6 | 0 | 0 | 0 | — | 0 |
| P1-2.1 | 6 | 0 | 0 | 0 | — | 0 |
| P1-3 | 6 | 0 | 0 | 0 | — | 0 |
| P1-4 | 5 | 0 | 0 | 0 | — | 0 |
| P1-4.1 | 11 | 0 | 0 | 0 | — | 0 |
| P1-4.2 | 8 | 0 | 0 | 0 | — | 0 |
| P1-4.3 | 6 | 1 | 1 | 0 | 100.0% | 1 |
| P1-5 | 2 | 0 | 0 | 0 | — | 0 |
| P1-5.1 | 17 | 0 | 0 | 0 | — | 0 |
| P1-5.2 | 30 | 3 | 2 | 1 | 66.7% | 1 |
| P1-5.3 | 15 | 0 | 0 | 0 | — | 0 |
| P1-6 | 7 | 0 | 0 | 0 | — | 0 |
| P1-7.1 | 9 | 2 | 1 | 1 | 50.0% | 0 |
| P1-8.1 | 7 | 0 | 0 | 0 | — | 0 |
| P1-8.2 | 19 | 1 | 0 | 1 | 0.0% | 0 |
| P1-8.3 | 7 | 0 | 0 | 0 | — | 0 |
| P1-8.4 | 8 | 0 | 0 | 0 | — | 0 |

### 4.2 P2

| folha | itens no pacote | com moldura | C | E | %C | E faltante |
|---|---|---|---|---|---|---|
| P2-1.1 | 29 | 9 | 4 | 5 | 44.4% | 0 |
| P2-1.2 | 30 | 4 | 3 | 1 | 75.0% | 1 |
| P2-1.3 | 30 | 6 | 6 | 0 | 100.0% | 4 |
| P2-1.4 | 30 | 7 | 7 | 0 | 100.0% | 5 |
| P2-1.5 | 30 | 7 | 3 | 4 | 42.9% | 0 |
| P2-1.6 | 30 | 19 | 9 | 10 | 47.4% | 0 |
| P2-1.7 | 30 | 13 | 5 | 8 | 38.5% | 0 |
| P2-1.8 | 30 | 9 | 6 | 3 | 66.7% | 1 |
| P2-2.1 | 27 | 15 | 7 | 8 | 46.7% | 0 |
| P2-2.2 | 21 | 12 | 6 | 6 | 50.0% | 0 |
| P2-2.3 | 20 | 13 | 5 | 8 | 38.5% | 0 |
| P2-2.4 | 20 | 15 | 8 | 7 | 53.3% | 0 |
| P2-2.5 | 20 | 7 | 4 | 3 | 57.1% | 0 |
| P2-2.6 | 20 | 3 | 3 | 0 | 100.0% | 2 |
| P2-2.7 | 20 | 10 | 3 | 7 | 30.0% | 0 |
| P2-2.8 | 20 | 12 | 3 | 9 | 25.0% | 0 |
| P2-3.1 | 27 | 16 | 8 | 8 | 50.0% | 0 |
| P2-3.2 | 20 | 5 | 5 | 0 | 100.0% | 4 |
| P2-3.3 | 20 | 10 | 5 | 5 | 50.0% | 0 |
| P2-3.4 | 20 | 3 | 3 | 0 | 100.0% | 2 |
| P2-4.1 | 30 | 3 | 3 | 0 | 100.0% | 2 |
| P2-4.2 | 20 | 5 | 2 | 3 | 40.0% | 0 |
| P2-4.3 | 20 | 5 | 4 | 1 | 80.0% | 2 |

### 4.3 P1-DA

| folha | itens no pacote | com moldura | C | E | %C | E faltante |
|---|---|---|---|---|---|---|
| P1-DA-1 | 8 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-1.1 | 11 | 0 | 0 | 0 | — | 0 |
| P1-DA-1.2 | 11 | 0 | 0 | 0 | — | 0 |
| P1-DA-2.1 | 22 | 0 | 0 | 0 | — | 0 |
| P1-DA-2.2 | 8 | 0 | 0 | 0 | — | 0 |
| P1-DA-3.1 | 10 | 2 | 2 | 0 | 100.0% | 2 |
| P1-DA-3.2 | 10 | 1 | 0 | 1 | 0.0% | 0 |
| P1-DA-3.3 | 10 | 0 | 0 | 0 | — | 0 |
| P1-DA-3.4 | 10 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-4.1 | 10 | 2 | 2 | 0 | 100.0% | 2 |
| P1-DA-4.2 | 10 | 2 | 2 | 0 | 100.0% | 2 |
| P1-DA-4.3 | 10 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-4.4 | 10 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-5.1 | 10 | 1 | 0 | 1 | 0.0% | 0 |
| P1-DA-5.2 | 9 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-6.1 | 10 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-6.2 | 9 | 0 | 0 | 0 | — | 0 |
| P1-DA-6.3 | 7 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-6.4 | 8 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-6.5 | 8 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-7 | 10 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-8 | 6 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-8.1 | 6 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-8.2 | 10 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-8.3 | 10 | 2 | 2 | 0 | 100.0% | 2 |
| P1-DA-8.4 | 7 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-9.1 | 10 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-9.2 | 10 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-9.3 | 10 | 2 | 2 | 0 | 100.0% | 2 |
| P1-DA-9.4 | 10 | 2 | 2 | 0 | 100.0% | 2 |
| P1-DA-10.1 | 10 | 4 | 1 | 3 | 25.0% | 0 |
| P1-DA-10.2 | 10 | 2 | 1 | 1 | 50.0% | 0 |
| P1-DA-10.3 | 10 | 3 | 3 | 0 | 100.0% | 2 |
| P1-DA-10.4 | 10 | 4 | 3 | 1 | 75.0% | 1 |
| P1-DA-10.5 | 10 | 3 | 2 | 1 | 66.7% | 1 |
| P1-DA-10.6 | 10 | 2 | 2 | 0 | 100.0% | 2 |
| P1-DA-10.7 | 10 | 4 | 3 | 1 | 75.0% | 1 |
| P1-DA-11 | 30 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-12 | 20 | 0 | 0 | 0 | — | 0 |

### 4.4 P1-DA: folhas com moldura ordenadas por %C

Ordem: %C decrescente, depois nº de itens com moldura decrescente, depois ordem do edital. Das 32 folhas de DA com moldura, 25 têm 100% de C; as 5 de maior %C com mais itens são 10.3 (3/3) e, em ordem do edital entre as de 2/2, 3.1, 4.1, 4.2 e 8.3.

| folha | com moldura | C | E | %C | E faltante (aux.) |
|---|---|---|---|---|---|
| P1-DA-10.3 | 3 | 3 | 0 | 100.0% | 2 |
| P1-DA-3.1 | 2 | 2 | 0 | 100.0% | 2 |
| P1-DA-4.1 | 2 | 2 | 0 | 100.0% | 2 |
| P1-DA-4.2 | 2 | 2 | 0 | 100.0% | 2 |
| P1-DA-8.3 | 2 | 2 | 0 | 100.0% | 2 |
| P1-DA-9.3 | 2 | 2 | 0 | 100.0% | 2 |
| P1-DA-9.4 | 2 | 2 | 0 | 100.0% | 2 |
| P1-DA-10.6 | 2 | 2 | 0 | 100.0% | 2 |
| P1-DA-1 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-3.4 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-4.3 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-4.4 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-5.2 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-6.1 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-6.3 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-6.4 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-6.5 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-7 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-8 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-8.1 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-8.2 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-8.4 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-9.1 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-9.2 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-11 | 1 | 1 | 0 | 100.0% | 1 |
| P1-DA-10.4 | 4 | 3 | 1 | 75.0% | 1 |
| P1-DA-10.7 | 4 | 3 | 1 | 75.0% | 1 |
| P1-DA-10.5 | 3 | 2 | 1 | 66.7% | 1 |
| P1-DA-10.2 | 2 | 1 | 1 | 50.0% | 0 |
| P1-DA-10.1 | 4 | 1 | 3 | 25.0% | 0 |
| P1-DA-3.2 | 1 | 0 | 1 | 0.0% | 0 |
| P1-DA-5.1 | 1 | 0 | 1 | 0.0% | 0 |

## 5. Sensibilidade (fronteira) — para a gbq-gerencia decidir

Itens com moldura por tipo de borda (todos já contados na seção 3):

| borda | itens | C | E |
|---|---|---|---|
| assembleia | 1 | 1 | 0 |
| comissao_sem_ancora | 1 | 0 | 1 |
| cpi | 1 | 1 | 0 |
| dominio | 2 | 2 | 0 |
| estrangeiro | 6 | 3 | 3 |
| poder_isolado | 2 | 2 | 0 |
| (sem borda) | 255 | 151 | 104 |

Itens N com sinal fraco (sessão, orador, audiência, pronunciamento, discurso, proposição, taquigrafia, ata, diário, "Poder em rol", "mandato de vereador", "câmara" em sentido não legislativo), NÃO contados na seção 3. Se a gerência optar por contá-los, a moldura de P2 sobe e a de DA muda pouco:

| matéria | itens N com sinal fraco | C | E |
|---|---|---|---|
| P1-TI | 3 | 2 | 1 |
| P2 | 95 | 44 | 51 |
| P1-DA | 7 | 3 | 4 |

Efeitos sobre a conta auxiliar de DA: sem os 2 itens "poder_isolado" (ambos C), DA fica com 51 itens, 42 C, 9 E, 82,4% de C e E faltante 19 (em vez de 21). P1-TI e P2 ficam em 0 em qualquer cenário acima (P1-TI 57,1% e P2 53,8%; contando todos os sinais fracos, P2 iria a 303 itens com 156 C, 51,5%).

## 6. Observações para a gbq-gerencia

1. O problema de proporção está em P1-DA (83,0% de C com moldura, 44 C × 9 E); P2 e P1-TI já estão dentro de 40–60% (53,8% e 57,1%). O total geral, 59,7%, fica abaixo de 60% só porque P2 pesa 78% dos itens com moldura; a leitura por matéria é a que importa para o reforço de DA (T-116).
2. Em DA, dos 53 itens com moldura, 37 são a abertura "órgão/servidor/Casa do Poder Legislativo da União" (D2, D3 e D5), 12 são "audiência pública de comissão da Câmara dos Deputados" (D4, todos C), 2 são sessão ou comissão da Câmara (D3-07 E; D3-18 C) e 2 são Poder Legislativo isolado (D1-08, D6-25, ambos C). Os 9 E são D2-19, D3-07, D5-06, D5-08, D5-09, D5-14, D5-40, D5-47 e D5-70.
3. Das 32 folhas de DA com moldura, 25 têm 100% de C. As folhas com E são 3.2 (0 C × 1 E), 5.1 (0 × 1), 10.1 (1 × 3), 10.2 (1 × 1), 10.4 (3 × 1), 10.5 (2 × 1) e 10.7 (3 × 1); entre as folhas sem E, a de mais itens é a 10.3 (3 C).
4. Nada foi alterado em itens, pacotes nem saida/plataforma/; o script só grava o CSV. Sem commit nem push.
