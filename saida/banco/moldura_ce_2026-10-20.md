# moldura_ce_2026-10-20.md — T-122 (D-MOLDURA-CE) — 2026-10-20 — gerado por gbq-gerencia

Relatório da D-MOLDURA-CE (ordem do Fundador de 20/10/2026, sessão s15; DECISOES.md, linha 171): itens com moldura do Legislativo no pacote v1.13 canônico, C/E por matéria e por folha, META de itens E com moldura, distribuição da meta de DA pelo reforço da T-116, regra (c) para a T-119 e o que já está na plataforma publicada. Ciclo s15c2. Nada foi alterado em itens, pacotes, CSV, script da gcb-cpp nem saida/plataforma/. Sem commit nem push.

## 0. Objetos e conferência

| objeto | SHA-256 |
|---|---|
| saida/pacote/pacote.json (v1.13 canônico, D-PACOTE-V113-CANONICO; 1.159 itens, C/E 582/577) | `82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240` |
| saida/banco/moldura_ce.py (script oficial da contagem, gcb-cpp) | `5723698e9a718b106a523cac6774f3ed5f23f39a09e9a0d02fd59ecf9ddcca96` |
| saida/banco/moldura_ce_itens_2026-10-20.csv (marcação oficial, item a item) | `ed4b364dffbca7d9e8878591914783258fa7048c4f1837d98c3d62e34981daac` |
| saida/banco/moldura_ce_contagem_2026-10-20.md (contagem, gcb-cpp) | `07f59ffa4e0fc05b841666edfb4bace79e7a6e101b0e04e22ee61f9da40aacda` |
| saida/banco/moldura_ce_conferencia_P2_gce_2026-10-20.md (conferência de P2, gce-cpp) | `9cb259bdb4679c5c98e0cda6afd875f2f94cde158245e03b853e92fa6d73c59a` |
| saida/pacote/cobertura_v1_13.md (T-95; folhas de DA e "faltam para 20") | `13491263120b7b63f0891dc08c6de556245ecc94147687964390459b5bcbb8c1` |
| saida/plataforma/plataforma_v16_publicar.html (v16 publicada) | `4d19eb05f3da3b8eebd466ec62fb91b01791397a692e8dfd0c4ddff229a065fb` |
| saida/pacote/montagem_v1_13/out/diag30_DA.json | `eb1ced6df3d624ae62b82337db6a4cfe29b86baa9494e96aed1b3defe61a6800` |

**Conferência da GBQ por script próprio** (somente leitura; `python3 -I conf_t122.py /home/claude/fabrica`; scratchpad da sessão, t122/conf_t122.py, SHA-256 `13f8bc3c22c3ff952a0bf06dc0fb6415be246ceda29ce9cedf8211e14cb77633`): 17 verificações, 0 FALHA — os SHA-256 acima; CSV com os 1.159 ids na ordem do pacote e gabarito, itemEdital e matéria iguais ao pacote; tabela da seção 3 da contagem reproduzida (P1-TI 7 = 4/3; P2 208 = 112/96; P1-DA 53 = 44/9); soma "faltam para 20" de DA = 356 em 37 folhas e 396 itens em folha (cobertura v1.13); v16 com os mesmos 1.159 ids, na mesma ordem e com gabarito, comando, textoBase, enunciado e itemEdital iguais ao canônico; os 6 itens de "rito" da GCE são N no CSV. Além disso, um **classificador independente** escrito pela GBQ (lista de termos própria, sem importar a lógica do moldura_ce.py) marcou os 1.159 itens: **0 divergência** com a coluna moldura do CSV. Leitura manual da GBQ: os 53 itens S de DA (todos), os 7 de P1-TI S e os 10 N com sinal fraco de P1-TI e P1-DA — nenhum falso positivo ou negativo pelo critério da seção 1. P2 já tem dupla leitura manual (gcb-cpp: 32 S e 47 N; gce-cpp, às cegas: 40 S, 40 N e os 95 de fronteira, 175/175 de concordância).

## 1. Critério oficial (D1 da GBQ)

**Definição.** Item com moldura do Legislativo = item cujo texto avaliado (comando + textoBase + enunciado; nunca justificativa, certame ou url) põe a situação, o sujeito ou o cenário de uso no Poder Legislativo, nomeando-o: Câmara dos Deputados ou "a Câmara"; Congresso, Senado, Senador, Deputado, parlamento ou parlamentar; "órgão/servidor/Casa do Poder Legislativo (da União)"; Plenário, sessão plenária ou legislativa; comissão (em P1-TI e P2, qualquer uso; em P1-DA, só a comissão legislativa); "a Casa" com maiúscula (não Casa Civil); Mesa; Derep/DETAQ; Assembleia Legislativa; CPI; o domínio legislativo nomeado como cenário de uso. O parêntese da ordem ("situação na Câmara, no Congresso ou com parlamentar") é exemplificativo: a moldura que motivou a D-MOLDURA-CE é a abertura "Considere que um órgão do Poder Legislativo da União…", que não nomeia nenhum dos três. Não têm moldura: item que só cita lei ou norma; Legislativo em rol com outro Poder ou com o MP; "legislativo/a" como função ou espécie normativa (delegação, autorização, técnica legislativa); "câmara" como palavra citada ou em sentido não legislativo; termos de cena sem órgão nomeado (sessão, orador, audiência, pronunciamento, proposição, ata, notas taquigráficas, questão de ordem, tribuna, registro oficial em minúsculas).

**Leitura oficial = o critério escrito da gcb-cpp (seção 1 da contagem), aplicado por saida/banco/moldura_ce.py; a marcação oficial é a coluna `moldura` do CSV.** As quatro questões de fronteira ficam decididas assim:

| questão | decisão | razão | efeito (itens; C/E) |
|---|---|---|---|
| (1) Legislativo estrangeiro (Câmara dos Comuns do Canadá, Parlamento da Estônia, Câmara e Senado da Itália, Conselho de Representantes do Bahrein, "um parlamento") | **S** (borda `estrangeiro`) | o item põe a cena num parlamento, que é o sinal que a candidata pode associar ao gabarito; a nacionalidade não muda o sinal | 6 itens de P2; 3/3 — neutro |
| (2) "Poder Legislativo" como único Poder da frase, sem órgão em cena (D1-08, D6-25) | **S** (borda `poder_isolado`) | o Legislativo é o sujeito da proposição e o sinal para a candidata é o mesmo da abertura "órgão do Poder Legislativo"; a escolha é a conservadora (aumenta a meta de E de 19 para 21) e não muda a ação. Para a produção, porém, item desse tipo **não conta para a cota de E** da seção 4 (a cota pede a moldura de cena da folha, regra R2), para que a meta não seja cumprida com afirmação doutrinária em vez de moldura | 2 itens de DA (DA 1 e DA 11, fora do reforço); 2/0 |
| (3) Ambiente de sessão sem âncora institucional (sessão, orador, audiência, pronunciamento, proposição; inclusive os 6 "rito" da GCE: L1-R171, L1-R181, L1-R71, L2-Q03, L2-R122, L3-Q01) | **N** | em P2 essas palavras são polissêmicas nos próprios itens (sessão da Realtime API, orador como falante genérico, audiência de "órgão público"); a candidata só lê a moldura como pista quando o órgão é nomeado; a lista fechada mantém o critério reprodutível por script e aplicável pelo montador de simulados. A proposta de borda "rito" da GCE fica registrada como sensibilidade (seção 2.3), sem efeito sobre a meta | 95 itens N com sinal fraco em P2 (44/51); os 6 de rito, 4/2 |
| (4) Âncora única "comissão" ou "Casa" em P2 | **S** | em P2 toda comissão e toda "Casa" com maiúscula é a legislativa (a gce-cpp concorda, 15/15 na amostra); tirar o bloco subestimaria a moldura | 55 itens de P2; 38/17 |

Demais bordas do CSV, confirmadas como S: `dominio` (A5-01, L3-Q16; 2 C), `cpi` (L2-R81; 1 C), `assembleia` (L3-R38; 1 C), `comissao_sem_ancora` (A5-10; 1 E). Para itens novos (reforço da T-116 e ondas seguintes), o produtor declara a moldura (S/N) e o tipo (seção 4, R2), e a contagem oficial é a do script reaplicado ao pacote em que o item entrar.

## 2. Contagem oficial

### 2.1 Por matéria

| matéria | itens no pacote | com moldura | % do universo | C | E | %C | situação |
|---|---|---|---|---|---|---|---|
| P1-TI | 185 | 7 | 3,8% | 4 | 3 | 57,1% | na faixa |
| P2 | 564 | 208 | 36,9% | 112 | 96 | 53,8% | na faixa |
| P1-DA | 410 | 53 | 12,9% | 44 | 9 | **83,0%** | **acima de 60%** |
| total | 1.159 | 268 | 23,1% | 160 | 108 | 59,7% | (o total só fica abaixo de 60% porque P2 pesa 78% da moldura; a leitura que vale é por matéria) |

DA por tipo de moldura: abertura "órgão/servidor/Casa do Poder Legislativo da União" 37 itens (29 C / 8 E; D2 10, D3 5, D5 22); "audiência pública de comissão da Câmara dos Deputados, um expositor afirme…" 12 itens (12 C / 0 E; todos do D4); sessão ou comissão da Câmara 2 (D3-07 E, D3-18 C); Poder Legislativo isolado 2 (D1-08, D6-25; C). Os 9 E são D2-19, D3-07, D5-06, D5-08, D5-09, D5-14, D5-40, D5-47 e D5-70.

### 2.2 Por folha (itemEdital)

"E faltante" = menor número de itens E com moldura que leva a folha a ≤ 60% de C: x = ⌈(2C − 3E)/3⌉ se 2C > 3E. "C faltante" = menor número de C com moldura que a leva a ≥ 40%: ⌈(2E − 3C)/3⌉ se 2E > 3C. DA 1 e DA 8 são os caputs (itens fora de folha na cobertura); entram como linhas próprias.

#### P1-TI

| folha | itens na folha | moldura | C | E | %C | situação | E faltante (≤ 60%) | C faltante (≥ 40%) |
|---|---|---|---|---|---|---|---|---|
| P1 4.3 | 6 | 1 | 1 | 0 | 100,0% | acima de 60% | 1 | 0 |
| P1 5.2 | 30 | 3 | 2 | 1 | 66,7% | acima de 60% | 1 | 0 |
| P1 7.1 | 9 | 2 | 1 | 1 | 50,0% | na faixa | 0 | 0 |
| P1 8.2 | 19 | 1 | 0 | 1 | 0,0% | abaixo de 40% | 0 | 1 |

Folhas sem item com moldura (14): P1 1 (16), P1 2 (6), P1 2.1 (6), P1 3 (6), P1 4 (5), P1 4.1 (11), P1 4.2 (8), P1 5 (2), P1 5.1 (17), P1 5.3 (15), P1 6 (7), P1 8.1 (7), P1 8.3 (7), P1 8.4 (8).

#### P2

| folha | itens na folha | moldura | C | E | %C | situação | E faltante (≤ 60%) | C faltante (≥ 40%) |
|---|---|---|---|---|---|---|---|---|
| P2 1.1 | 29 | 9 | 4 | 5 | 44,4% | na faixa | 0 | 0 |
| P2 1.2 | 30 | 4 | 3 | 1 | 75,0% | acima de 60% | 1 | 0 |
| P2 1.3 | 30 | 6 | 6 | 0 | 100,0% | acima de 60% | 4 | 0 |
| P2 1.4 | 30 | 7 | 7 | 0 | 100,0% | acima de 60% | 5 | 0 |
| P2 1.5 | 30 | 7 | 3 | 4 | 42,9% | na faixa | 0 | 0 |
| P2 1.6 | 30 | 19 | 9 | 10 | 47,4% | na faixa | 0 | 0 |
| P2 1.7 | 30 | 13 | 5 | 8 | 38,5% | abaixo de 40% | 0 | 1 |
| P2 1.8 | 30 | 9 | 6 | 3 | 66,7% | acima de 60% | 1 | 0 |
| P2 2.1 | 27 | 15 | 7 | 8 | 46,7% | na faixa | 0 | 0 |
| P2 2.2 | 21 | 12 | 6 | 6 | 50,0% | na faixa | 0 | 0 |
| P2 2.3 | 20 | 13 | 5 | 8 | 38,5% | abaixo de 40% | 0 | 1 |
| P2 2.4 | 20 | 15 | 8 | 7 | 53,3% | na faixa | 0 | 0 |
| P2 2.5 | 20 | 7 | 4 | 3 | 57,1% | na faixa | 0 | 0 |
| P2 2.6 | 20 | 3 | 3 | 0 | 100,0% | acima de 60% | 2 | 0 |
| P2 2.7 | 20 | 10 | 3 | 7 | 30,0% | abaixo de 40% | 0 | 2 |
| P2 2.8 | 20 | 12 | 3 | 9 | 25,0% | abaixo de 40% | 0 | 3 |
| P2 3.1 | 27 | 16 | 8 | 8 | 50,0% | na faixa | 0 | 0 |
| P2 3.2 | 20 | 5 | 5 | 0 | 100,0% | acima de 60% | 4 | 0 |
| P2 3.3 | 20 | 10 | 5 | 5 | 50,0% | na faixa | 0 | 0 |
| P2 3.4 | 20 | 3 | 3 | 0 | 100,0% | acima de 60% | 2 | 0 |
| P2 4.1 | 30 | 3 | 3 | 0 | 100,0% | acima de 60% | 2 | 0 |
| P2 4.2 | 20 | 5 | 2 | 3 | 40,0% | na faixa | 0 | 0 |
| P2 4.3 | 20 | 5 | 4 | 1 | 80,0% | acima de 60% | 2 | 0 |

Todas as 23 folhas de P2 têm item com moldura.

#### P1-DA

| folha | itens na folha | moldura | C | E | %C | situação | E faltante (≤ 60%) | C faltante (≥ 40%) |
|---|---|---|---|---|---|---|---|---|
| DA 1 (caput) | 8 | 1 | 1 | 0 | 100,0% | acima de 60% | 1 | 0 |
| DA 3.1 | 10 | 2 | 2 | 0 | 100,0% | acima de 60% | 2 | 0 |
| DA 3.2 | 10 | 1 | 0 | 1 | 0,0% | abaixo de 40% | 0 | 1 |
| DA 3.4 | 10 | 1 | 1 | 0 | 100,0% | acima de 60% | 1 | 0 |
| DA 4.1 | 10 | 2 | 2 | 0 | 100,0% | acima de 60% | 2 | 0 |
| DA 4.2 | 10 | 2 | 2 | 0 | 100,0% | acima de 60% | 2 | 0 |
| DA 4.3 | 10 | 1 | 1 | 0 | 100,0% | acima de 60% | 1 | 0 |
| DA 4.4 | 10 | 1 | 1 | 0 | 100,0% | acima de 60% | 1 | 0 |
| DA 5.1 | 10 | 1 | 0 | 1 | 0,0% | abaixo de 40% | 0 | 1 |
| DA 5.2 | 9 | 1 | 1 | 0 | 100,0% | acima de 60% | 1 | 0 |
| DA 6.1 | 10 | 1 | 1 | 0 | 100,0% | acima de 60% | 1 | 0 |
| DA 6.3 | 7 | 1 | 1 | 0 | 100,0% | acima de 60% | 1 | 0 |
| DA 6.4 | 8 | 1 | 1 | 0 | 100,0% | acima de 60% | 1 | 0 |
| DA 6.5 | 8 | 1 | 1 | 0 | 100,0% | acima de 60% | 1 | 0 |
| DA 7 | 10 | 1 | 1 | 0 | 100,0% | acima de 60% | 1 | 0 |
| DA 8 (caput) | 6 | 1 | 1 | 0 | 100,0% | acima de 60% | 1 | 0 |
| DA 8.1 | 6 | 1 | 1 | 0 | 100,0% | acima de 60% | 1 | 0 |
| DA 8.2 | 10 | 1 | 1 | 0 | 100,0% | acima de 60% | 1 | 0 |
| DA 8.3 | 10 | 2 | 2 | 0 | 100,0% | acima de 60% | 2 | 0 |
| DA 8.4 | 7 | 1 | 1 | 0 | 100,0% | acima de 60% | 1 | 0 |
| DA 9.1 | 10 | 1 | 1 | 0 | 100,0% | acima de 60% | 1 | 0 |
| DA 9.2 | 10 | 1 | 1 | 0 | 100,0% | acima de 60% | 1 | 0 |
| DA 9.3 | 10 | 2 | 2 | 0 | 100,0% | acima de 60% | 2 | 0 |
| DA 9.4 | 10 | 2 | 2 | 0 | 100,0% | acima de 60% | 2 | 0 |
| DA 10.1 | 10 | 4 | 1 | 3 | 25,0% | abaixo de 40% | 0 | 1 |
| DA 10.2 | 10 | 2 | 1 | 1 | 50,0% | na faixa | 0 | 0 |
| DA 10.3 | 10 | 3 | 3 | 0 | 100,0% | acima de 60% | 2 | 0 |
| DA 10.4 | 10 | 4 | 3 | 1 | 75,0% | acima de 60% | 1 | 0 |
| DA 10.5 | 10 | 3 | 2 | 1 | 66,7% | acima de 60% | 1 | 0 |
| DA 10.6 | 10 | 2 | 2 | 0 | 100,0% | acima de 60% | 2 | 0 |
| DA 10.7 | 10 | 4 | 3 | 1 | 75,0% | acima de 60% | 1 | 0 |
| DA 11 | 30 | 1 | 1 | 0 | 100,0% | acima de 60% | 1 | 0 |

Folhas sem item com moldura (7): DA 1.1 (11), DA 1.2 (11), DA 2.1 (22), DA 2.2 (8), DA 3.3 (10), DA 6.2 (9), DA 12 (20).

### 2.3 Sensibilidade (não muda a meta de P2 nem de P1-TI)

| leitura | P2: moldura, C/E, %C | P1-DA: moldura, C/E, %C, meta |
|---|---|---|
| oficial (seção 1) | 208; 112/96; 53,8% | 53; 44/9; 83,0%; **21** |
| + 6 itens de "rito" (proposta da GCE) | 214; 116/98; 54,2% | igual |
| + todos os 95 N com sinal fraco de P2 | 303; 156/147; 51,5% | — |
| − âncora única comissão/Casa (55 itens) | 153; 74/79; 48,4% | — |
| − Poder Legislativo isolado (D1-08, D6-25) | — | 51; 42/9; 82,4%; 19 |

Em todas as leituras P2 e P1-TI ficam entre 40% e 60% e P1-DA fica acima de 80%. A decisão de fronteira não muda a ação.

## 3. META por matéria

Fórmula: x itens E com moldura acrescentados (sem C com moldura novo) levam a matéria a C/(C+E+x). **Piso** (≤ 60%): x ≥ ⌈(2C − 3E)/3⌉. **Teto** (≥ 40%): x ≤ ⌊(3C − 2E)/2⌋.

| matéria | C/E hoje | %C | META: E com moldura que faltam (≤ 60%) | teto (não abaixo de 40%) | %C com a meta |
|---|---|---|---|---|---|
| P1-TI | 4/3 | 57,1% | **0** | 3 | — |
| P2 | 112/96 | 53,8% | **0** | 72 | — |
| P1-DA | 44/9 | 83,0% | **21** | 57 | 44/74 = 59,5% |

A meta de DA é **21** (obrigatória) dentro da faixa admissível de 21 a 57. A distribuição por folha da seção 4 soma **33** e leva DA a 44/86 = **51,2%**: cumpre a meta (na leva 9) e, além disso, põe cada folha do reforço com moldura em ≤ 60% de C. Se o reforço acrescentar C com moldura (só em par, regra R3), o teto passa a 57 + 1,5 × (C com moldura acrescentados).

## 4. DA — distribuição da meta pelas folhas do reforço (T-116)

Ordem da D-REFORCO-DA (cobertura v1.13: das mais ralas às mais cheias; empate pela ordem do edital). **Cota** = E com moldura que a folha deve receber = E faltante da folha (seção 2.2). "Leva indicativa" = folhas inteiras, até 30 itens, nessa ordem (a gcb-gerencia pode compor as levas de outro modo; a cota acompanha a folha, não o número da leva). A coluna "%C DA após a leva" supõe as cotas cumpridas e nenhum C com moldura novo.

| # | folha | faltam p/ 20 | moldura hoje (C/E) | tipo de moldura da folha | **cota E com moldura** | folha depois (C/E) | leva indicativa (itens) | cota acumulada | %C DA após a leva |
|---|---|---|---|---|---|---|---|---|---|
| 1 | DA 8.1 | 14 | 1/0 | expositor (D4) | **1** | 1/1 | 1 (27) | | |
| 2 | DA 6.3 | 13 | 1/0 | órgão/servidor (D3) | **1** | 1/1 | 1 | 2 | 80,0% |
| 3 | DA 8.4 | 13 | 1/0 | expositor (D4) | **1** | 1/1 | 2 (25) | | |
| 4 | DA 2.2 | 12 | — | — | 0 | — | 2 | 3 | 78,6% |
| 5 | DA 6.4 | 12 | 1/0 | órgão/servidor (D3) | **1** | 1/1 | 3 (24) | | |
| 6 | DA 6.5 | 12 | 1/0 | órgão/servidor (D3) | **1** | 1/1 | 3 | 5 | 75,9% |
| 7 | DA 5.2 | 11 | 1/0 | comissão/sessão da Câmara (D3) | **1** | 1/1 | 4 (22) | | |
| 8 | DA 6.2 | 11 | — | — | 0 | — | 4 | 6 | 74,6% |
| 9 | DA 3.1 | 10 | 2/0 | órgão/servidor (D2) | **2** | 2/2 | 5 (30) | | |
| 10 | DA 3.2 | 10 | 0/1 | órgão/servidor (D2) | 0 | 0/1 | 5 | | |
| 11 | DA 3.3 | 10 | — | — | 0 | — | 5 | 8 | 72,1% |
| 12 | DA 3.4 | 10 | 1/0 | órgão/servidor (D2) | **1** | 1/1 | 6 (30) | | |
| 13 | DA 4.1 | 10 | 2/0 | órgão/servidor (D2) | **2** | 2/2 | 6 | | |
| 14 | DA 4.2 | 10 | 2/0 | órgão/servidor (D2) | **2** | 2/2 | 6 | 13 | 66,7% |
| 15 | DA 4.3 | 10 | 1/0 | órgão/servidor (D2) | **1** | 1/1 | 7 (30) | | |
| 16 | DA 4.4 | 10 | 1/0 | órgão/servidor (D2) | **1** | 1/1 | 7 | | |
| 17 | DA 5.1 | 10 | 0/1 | comissão/sessão da Câmara (D3) | 0 | 0/1 | 7 | 15 | 64,7% |
| 18 | DA 6.1 | 10 | 1/0 | órgão/servidor (D3) | **1** | 1/1 | 8 (30) | | |
| 19 | DA 7 | 10 | 1/0 | órgão/servidor (D3) | **1** | 1/1 | 8 | | |
| 20 | DA 8.2 | 10 | 1/0 | expositor (D4) | **1** | 1/1 | 8 | 18 | 62,0% |
| 21 | DA 8.3 | 10 | 2/0 | expositor (D4) | **2** | 2/2 | 9 (30) | | |
| 22 | DA 9.1 | 10 | 1/0 | expositor (D4) | **1** | 1/1 | 9 | | |
| 23 | DA 9.2 | 10 | 1/0 | expositor (D4) | **1** | 1/1 | 9 | **22 (meta 21 cumprida)** | **58,7%** |
| 24 | DA 9.3 | 10 | 2/0 | expositor (D4) | **2** | 2/2 | 10 (30) | | |
| 25 | DA 9.4 | 10 | 2/0 | expositor (D4) | **2** | 2/2 | 10 | | |
| 26 | DA 10.1 | 10 | 1/3 | órgão (D5) | 0 | 1/3 | 10 | 26 | 55,7% |
| 27 | DA 10.2 | 10 | 1/1 | órgão (D5) | 0 | 1/1 | 11 (30) | | |
| 28 | DA 10.3 | 10 | 3/0 | órgão (D5) | **2** | 3/2 | 11 | | |
| 29 | DA 10.4 | 10 | 3/1 | órgão (D5) | **1** | 3/2 | 11 | 29 | 53,7% |
| 30 | DA 10.5 | 10 | 2/1 | órgão (D5) | **1** | 2/2 | 12 (30) | | |
| 31 | DA 10.6 | 10 | 2/0 | órgão (D5) | **2** | 2/2 | 12 | | |
| 32 | DA 10.7 | 10 | 3/1 | órgão (D5) | **1** | 3/2 | 12 | 33 | 51,2% |
| 33 | DA 1.1 | 9 | — | — | 0 | — | 13 (18) | | |
| 34 | DA 1.2 | 9 | — | — | 0 | — | 13 | 33 | 51,2% |
| | **soma** | **356** | 41/9 nas 34 folhas | | **33** | 41/42 | 13 levas | | |

Por leva indicativa (cota de E com moldura / itens da leva / faixa de E da leva pela regra 40–60%): L1 2/27/11–16; L2 1/25/10–15; L3 2/24/10–14; L4 1/22/9–13; L5 2/30/12–18; L6 5/30/12–18; L7 2/30/12–18; L8 3/30/12–18; L9 4/30/12–18; L10 4/30/12–18; L11 3/30/12–18; L12 4/30/12–18; L13 0/18/8–10. Em todas a cota cabe com folga no número de E que a leva pode ter, de modo que nenhuma leva precisa sair de 40–60% de C no total para cumprir a cota; a moldura de DA cai de 83,0% a 51,2% sem nunca chegar a 40%. Por tipo de moldura, depois das cotas: expositor (D4) 12/11 (52%); órgão/servidor 29/29 (50%); comissão/sessão da Câmara 1/2. Ficam fora do reforço, sem cota, DA 1 e DA 8 (caputs, 1 C cada) e DA 11 (1 C), já com 20 ou mais itens ou fora de folha: dado, sem ação.

**Regras de produção para a gcb-cpp (ficha do reforço; valem com as da D-REFORCO-2):**
- **R1 — legitimidade.** Cada E com moldura é um item errado pelo ponto de julgamento da folha (troca legítima: sujeito, prazo, competência, exceção, requisito), com base por item; a moldura não decide o gabarito (nunca "errado porque é o Legislativo"). Passa pelo QA da gcb-cqfp como qualquer item; o gbq-estilo, na auditoria de 10% por leva, inclui ao menos 1 E com moldura quando a leva tiver cota.
- **R2 — tipo de moldura.** O E da cota usa o mesmo tipo de moldura que causa o excesso de C na folha: "audiência pública de comissão da Câmara dos Deputados, um expositor afirme…" nas folhas do D4 (8.x e 9.x); "órgão/servidor do Poder Legislativo da União" nas do D2, D3 e D5; "comissão/sessão da Câmara" na DA 5.2. "Poder Legislativo" isolado não conta para a cota.
- **R3 — C com moldura.** Durante o reforço, item C com moldura só entra em par com 1 E com moldura a mais na mesma folha, além da cota (1:1), e a folha fica com no máximo 6 itens com moldura (30% de 20; teto prudencial alinhado ao limite de formato da D-REFORCO-2). Nenhuma folha passa de 5 com as cotas.
- **R4 — folha sem lastro.** Se uma folha não puder receber itens (8.1, 8.4, 6.3, 6.4, 6.5 dependem do adendo do qa-normativo-da), a cota dela passa à próxima folha da ordem do mesmo lote com moldura (D4: 8.2, 8.3, 9.x; D3: 6.1, 7), registrada na reconciliação da leva.
- **R5 — conferência por leva.** A reconciliação de cada leva (gcb-gerencia) informa, por folha, os E e os C com moldura aceitos, a cota acumulada e o %C projetado de DA (C/E de partida 44/9). Quando a cota acumulada passar de 21, a meta da D-MOLDURA-CE está cumprida no projetado; o equilíbrio é declarado pela GBQ na recontagem oficial (script reaplicado) sobre o pacote v1.14 canônico (T-123).
- **R6 — erratas (b).** Não são acionadas: o reforço basta (capacidade de E das levas muito acima de 33). Só se, ao fim das folhas com cota, a soma aceita ficar abaixo de 21 (falta de lastro ou QA), a GBQ lista por D1 os itens canônicos candidatos (troca legítima, gate de QA, registro de acatamento, D-MOLDURA-CE (b)); errata que mude o gabarito de item canônico é aceita por gatilho próprio.

## 5. Recomendação para P2 e P1-TI por folha (dado para as ondas seguintes; sem tarefa nova sem ordem)

As duas matérias estão na faixa (P2 53,8%; P1-TI 57,1%): **meta 0**, nenhuma ação agora. Folhas fora da faixa, como dado:
- **P2, acima de 60% (9 folhas; E faltante somado 23):** 1.2 (3/1; 1), 1.3 (6/0; 4), 1.4 (7/0; 5), 1.8 (6/3; 1), 2.6 (3/0; 2), 3.2 (5/0; 4), 3.4 (3/0; 2), 4.1 (3/0; 2), 4.3 (4/1; 2). **Abaixo de 40% (4 folhas; C faltante somado 7):** 1.7 (5/8; 1), 2.3 (5/8; 1), 2.7 (3/7; 2), 2.8 (3/9; 3). Se houver onda nova de P2 por ordem, item com moldura nessas folhas segue o sinal indicado (E nas primeiras, C nas segundas), sem tirar a matéria da faixa.
- **P1-TI (3 folhas, n ≤ 3):** 4.3 (1/0; 1 E), 5.2 (2/1; 1 E), 8.2 (0/1; 1 C). Amostra pequena demais para ação; a onda de P1 que vier (T-99 ou sucessora, por ordem) observa o sinal.
- **DA abaixo de 40%:** 3.2 (0/1), 5.1 (0/1), 10.1 (1/3): sem cota de E; a regra R3 vale; dado.

## 6. Regra (c) para a T-119 (montador de simulados)

Regra provisória (D-MOLDURA-CE (c)), vigente desde 20/10/2026 até o equilíbrio:
1. **Alcance:** todo simulado montado ou remontado a partir de agora, final ou diagnóstico, de qualquer matéria, inclusive os diagnósticos fixos da plataforma (listas DIAG30).
2. **Limite:** entre os itens com moldura = S pelo critério oficial (coluna `moldura` do CSV desta T-122; para itens que entrarem depois, o script oficial reaplicado ao pacote vigente), **nº de C ≤ nº de E** (C ≤ 50%). Em simulado com DA, o limite vale também para o subconjunto de DA com moldura. Sem item com moldura, a regra está cumprida.
3. **Conflito:** com os limiares por lote que a T-119 vai unificar (D5, D2, D3, D4, termo absoluto, pós-NPM, "Considere que"), vale o mais restritivo; a GBQ decide por D1 se a combinação não fechar.
4. **Fim:** quando a recontagem oficial sobre um pacote canônico (v1.14 ou posterior) der P1-DA, P2 e P1-TI entre 40% e 60% de C; a GBQ registra o fim por D1 no relatório da recontagem. Depois disso, vale só o equilíbrio C/E geral do simulado (gbq-gerencia, função (c)).
5. **Situação dos simulados existentes (dado):** SIM-0 (60) sem moldura; SIM-1 (40) 3 com moldura, 1 C / 2 E — cumpre; **SIM-2 (40) 4, 3 C / 1 E (75%) — não cumpriria**; SIM-0-P2 (25) 7, 3 C / 4 E — cumpre; DIAG30 P1 sem moldura; DIAG30 P2 9, 4 C / 5 E — cumpre; **DIAG30 DA 2, 2 C / 0 E (D2-52, D4-56) — não cumpriria**. Nada publicado é remontado sem ordem; a próxima montagem do SIM-2 e do DIAG30 DA (T-119 ou a plataforma da T-123) aplica a regra, e a publicação continua dependendo do sim do Fundador (D-V15-PLATAFORMA).

## 7. O que já está na plataforma publicada (v16)

A v16 publicada embute a montagem da v1.13 (007787e3…), que difere do canônico (82c4117c…) só em `lotes[D6].pares[0].como`, campo que o template não lê (D-PACOTE-V113-CANONICO). Conferido por script: os 1.159 itens da v16 têm id, ordem, gabarito, comando, textoBase, enunciado e itemEdital iguais ao canônico, de modo que a contagem desta T-122 vale para a plataforma. **A candidata vê hoje 53 itens de DA com moldura, 44 C e 9 E: 83,0% de C** (12,9% dos 410 itens de DA; nas 25 folhas de DA em que todos os itens com moldura são C, a pista "Legislativo → certo" não tem contraexemplo). No diagnóstico DA de 30 itens (DIAG30 DA, igual a diag30_DA.json) há 2 itens com moldura, ambos C (D2-52, D4-56). Nenhum item de DA está em simulado (0). No total da plataforma, 268 itens com moldura, 160 C / 108 E (59,7%); P2 e P1-TI na faixa. O reforço (T-116), consolidado na v1.14 (T-123) e publicado com o sim do Fundador, é o caminho que corrige o que a candidata vê; até lá, a regra (c) protege só os simulados que forem montados.

## 8. Gatilho

**Nenhum gatilho em PARA_PRESIDENCIA.md.** A tarefa fecha na Gerência: (1) as decisões de fronteira são critério de contagem, função própria da GBQ (arbitrar a tipologia de estilo; titular da T-122 pela D-MOLDURA-CE), e não mudam gabarito, rótulo, escopo, item nem gênero de peça (nada da lista D2/D); (2) a meta sai da fórmula fixada na ordem do Fundador; (3) a execução já está autorizada: a D-REFORCO-DA manda o reforço seguir "a meta de E da D-MOLDURA-CE" e a regra (c) foi fixada pelo Fundador; (4) as erratas (b) não são acionadas; (5) nada vai à plataforma; (6) as folhas fora da faixa em P2 e P1-TI são dado, sem tarefa nova. Atualizados em TAREFAS.md: linha T-122 (CONCLUÍDA) e acréscimo à T-119 com a regra (c).
