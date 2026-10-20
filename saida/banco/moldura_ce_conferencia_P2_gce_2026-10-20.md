# moldura_ce_conferencia_P2_gce_2026-10-20.md — T-122 (D-MOLDURA-CE; conferência independente da parte P2) — 2026-10-20 — gerado por gce-cpp

Conferência da contagem de moldura do Legislativo feita pela gcb-cpp (matéria P2, 564 itens, 208 S). Entrada somente leitura; nada de itens, pacotes, script ou CSV da gcb-cpp foi alterado. Sem commit nem push.

## 0. Objetos e método

| objeto | SHA-256 |
|---|---|
| saida/pacote/pacote.json (v1.13) | `82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240` |
| saida/banco/moldura_ce_itens_2026-10-20.csv | `ed4b364dffbca7d9e8878591914783258fa7048c4f1837d98c3d62e34981daac` |
| saida/banco/moldura_ce.py | `5723698e9a718b106a523cac6774f3ed5f23f39a09e9a0d02fd59ecf9ddcca96` |
| saida/banco/moldura_ce_contagem_2026-10-20.md | `07f59ffa4e0fc05b841666edfb4bace79e7a6e101b0e04e22ee61f9da40aacda` |

Os três primeiros coincidem com os da seção 0 da contagem (conferido).

**Cegamento.** Li o texto (comando + textoBase + enunciado, como no critério) de cada item sem a coluna `moldura`/`termo` à vista, anotei S ou N pelo critério da seção 1 e só depois cruzei com o CSV. A justificativa não foi lida como evidência de moldura.

**Sorteio.** `random.Random(20261020)`, `sample(pool_ordenado_por_id, 40)`, depois ordenado por id. Pools em P2: S = 208; N sem sinal fraco = 261; fronteira (N com `sinal_fraco`) = 95. Os 40 S e os 40 N saem dos dois primeiros pools; os 95 de fronteira foram lidos todos (não amostra). Lista completa nas seções 2 a 4.

**Rótulos GCE para a fronteira (leitura de ambiente).** `N` = nada indica cena legislativa (uso técnico de 'sessão', 'orador' como falante genérico, 'audiência' genérica, norma). `L` = limite: um cue de cena legislativa isolado (audiência pública com convidado, 'notas taquigráficas', 'questão de ordem', 'registro oficial'), que sozinho não distingue Legislativo de Judiciário ou Executivo. `S` = ambiente legislativo inequívoco por dois ou mais cues próprios do rito parlamentar ('Senhor Presidente', 'aparte', 'orador inscrito' com pauta, 'pronunciamentos' com 'proposições', 'notas oficiais de sessões', audiência com 'presidente da sessão'). É julgamento da GCE, não regra da gcb-cpp.

## 1. Resultado da concordância

| conjunto | n | concordo com a gcb-cpp (critério da seção 1) | divergo |
|---|---|---|---|
| P2 marcados S (sorteio) | 40 | 40 | 0 |
| P2 marcados N sem sinal fraco (sorteio) | 40 | 40 | 0 |
| P2 fronteira: N com sinal fraco (todos) | 95 | 95 | 0 |
| **total** | **175** | **175 (100%)** | **0** |

Na aplicação do critério escrito: 175/175. Na leitura de ambiente (seção 5), 6 dos 95 de fronteira eu contaria como moldura e 22 são limite; isso é divergência de critério, não de aplicação, e não altera as linhas acima.

Observações que não são divergência: (1) dos 40 S, 15 ancoram só em 'comissão', 'comissões' ou 'Casa' (L1-R55, L1-R85, L1-R93, L1-R95, L1-R100, L1-R101, L1-R113, L1-R124, L2-R17, L2-R40, L2-R56, L2-R98, L3-R07, L3-R08, L3-R45; marcadas 'âncora única' na tabela da seção 2). São S pelo critério (item 5 e item 4 da lista T) e eu concordo, porque em P2 toda comissão é legislativa; é a âncora mais fraca dentre as S. (2) Os 40 N sorteados não têm nenhum termo de cena; 5 citam norma (LGPD, Lei 9.610, Marco Civil), 24 são documentação de serviço (Whisper, Azure, AWS, Google) e 11 são conceito técnico.

## 2. P2 marcados S (40 sorteados)

| # | id | folha | gab. | gcb | GCE | âncora (coluna termo) | nota |
|---|---|---|---|---|---|---|---|
| 1 | L1-R100 | P2-1.6 | C | S | S | casa | âncora única (comissão/Casa) |
| 2 | L1-R101 | P2-1.6 | E | S | S | comissão | âncora única (comissão/Casa) |
| 3 | L1-R106 | P2-1.7 | E | S | S | Câmara | âncora forte |
| 4 | L1-R113 | P2-1.7 | C | S | S | comissões | âncora única (comissão/Casa) |
| 5 | L1-R114 | P2-1.7 | E | S | S | plenária | âncora forte |
| 6 | L1-R124 | P2-1.8 | C | S | S | comissões | âncora única (comissão/Casa) |
| 7 | L1-R131 | P2-1.2 | E | S | S | Câmara | âncora forte |
| 8 | L1-R169 | P2-1.4 | C | S | S | comissão; parlamentares | âncora forte |
| 9 | L1-R194 | P2-1.7 | C | S | S | Plenário | âncora forte |
| 10 | L1-R198 | P2-1.7 | C | S | S | Câmara; comissão | âncora forte |
| 11 | L1-R20 | P2-1.1 | C | S | S | comissão; parlamentares | âncora forte |
| 12 | L1-R45 | P2-1.2 | C | S | S | Plenário | âncora forte |
| 13 | L1-R55 | P2-1.3 | C | S | S | casa | âncora única (comissão/Casa) |
| 14 | L1-R64 | P2-1.4 | C | S | S | parlamentares | âncora forte |
| 15 | L1-R85 | P2-1.5 | E | S | S | casa | âncora única (comissão/Casa) |
| 16 | L1-R93 | P2-1.6 | E | S | S | casa | âncora única (comissão/Casa) |
| 17 | L1-R95 | P2-1.6 | C | S | S | comissão | âncora única (comissão/Casa) |
| 18 | L2-R01 | P2-2.1 | C | S | S | Deputado; Plenário; Câmara | âncora forte |
| 19 | L2-R02 | P2-2.1 | C | S | S | Câmara; Deputados; comissão | âncora forte |
| 20 | L2-R04 | P2-2.2 | E | S | S | sessões legislativas | âncora forte |
| 21 | L2-R13 | P2-2.6 | C | S | S | parlamentares | âncora forte |
| 22 | L2-R141 | P2-2.1 | C | S | S | senado | âncora forte |
| 23 | L2-R17 | P2-2.8 | E | S | S | comissão | âncora única (comissão/Casa) |
| 24 | L2-R22 | P2-2.1 | C | S | S | mesa; detaq; registro oficial | âncora forte |
| 25 | L2-R28 | P2-2.1 | E | S | S | Câmara; Deputados | âncora forte |
| 26 | L2-R36 | P2-2.2 | C | S | S | comissão; Câmara; Deputados | âncora forte |
| 27 | L2-R40 | P2-2.2 | E | S | S | casa | âncora única (comissão/Casa) |
| 28 | L2-R44 | P2-2.2 | C | S | S | comissão; Câmara; Deputados | âncora forte |
| 29 | L2-R49 | P2-2.3 | C | S | S | Deputado; Câmara; Deputados | âncora forte |
| 30 | L2-R56 | P2-2.3 | E | S | S | comissões | âncora única (comissão/Casa) |
| 31 | L2-R98 | P2-2.6 | C | S | S | comissão | âncora única (comissão/Casa) |
| 32 | L3-Q19 | P2-4.1 | C | S | S | parlamentares | âncora forte |
| 33 | L3-R07 | P2-3.4 | C | S | S | comissão | âncora única (comissão/Casa) |
| 34 | L3-R08 | P2-3.4 | C | S | S | comissão | âncora única (comissão/Casa) |
| 35 | L3-R45 | P2-3.3 | C | S | S | comissão | âncora única (comissão/Casa) |
| 36 | L3-R50 | P2-3.3 | C | S | S | Câmara; Deputados; comissão | âncora forte |
| 37 | L3-R52 | P2-3.3 | C | S | S | Câmara; Deputados; sessão legislativa | âncora forte |
| 38 | L3-R81 | P2-4.2 | E | S | S | Câmara; Deputados | âncora forte |
| 39 | L3-R94 | P2-4.3 | E | S | S | Câmara; Deputados | âncora forte |
| 40 | L3-R96 | P2-3.1 | E | S | S | Câmara; Deputados; interparlamentar | âncora forte; borda estrangeiro |

## 3. P2 marcados N sem sinal fraco (40 sorteados)

| # | id | folha | gab. | gcb | GCE | nota |
|---|---|---|---|---|---|---|
| 1 | BQ-0003 | P2-4.1 | E | N | N | norma (LGPD/Lei 9.610/Marco Civil), sem cena |
| 2 | BQ-0036 | P2-4.1 | C | N | N | norma (LGPD/Lei 9.610/Marco Civil), sem cena |
| 3 | L1-Q04 | P2-1.2 | C | N | N | conceito técnico, sem cena |
| 4 | L1-Q05 | P2-1.3 | C | N | N | conceito técnico, sem cena |
| 5 | L1-Q06 | P2-1.3 | E | N | N | conceito técnico, sem cena |
| 6 | L1-Q20 | P2-1.8 | E | N | N | conceito técnico, sem cena |
| 7 | L1-R04 | P2-1.2 | C | N | N | documentação de serviço/ferramenta, sem cena |
| 8 | L1-R108 | P2-1.7 | E | N | N | documentação de serviço/ferramenta, sem cena |
| 9 | L1-R118 | P2-1.8 | C | N | N | documentação de serviço/ferramenta, sem cena |
| 10 | L1-R123 | P2-1.8 | E | N | N | documentação de serviço/ferramenta, sem cena |
| 11 | L1-R126 | P2-1.8 | C | N | N | documentação de serviço/ferramenta, sem cena |
| 12 | L1-R127 | P2-1.8 | E | N | N | documentação de serviço/ferramenta, sem cena |
| 13 | L1-R164 | P2-1.4 | E | N | N | documentação de serviço/ferramenta, sem cena |
| 14 | L1-R17 | P2-1.8 | E | N | N | documentação de serviço/ferramenta, sem cena |
| 15 | L1-R187 | P2-1.6 | E | N | N | documentação de serviço/ferramenta, sem cena |
| 16 | L1-R25 | P2-1.1 | C | N | N | documentação de serviço/ferramenta, sem cena |
| 17 | L1-R26 | P2-1.1 | C | N | N | documentação de serviço/ferramenta, sem cena |
| 18 | L1-R32 | P2-1.1 | C | N | N | conceito técnico, sem cena |
| 19 | L1-R40 | P2-1.2 | E | N | N | documentação de serviço/ferramenta, sem cena |
| 20 | L1-R78 | P2-1.5 | C | N | N | conceito técnico, sem cena |
| 21 | L1C-Q23 | P2-1.2 | C | N | N | conceito técnico, sem cena |
| 22 | L1C-Q26 | P2-1.3 | E | N | N | conceito técnico, sem cena |
| 23 | L2-Q08 | P2-2.2 | C | N | N | conceito técnico, sem cena |
| 24 | L2-Q25 | P2-2.7 | C | N | N | conceito técnico, sem cena |
| 25 | L2-Q29 | P2-2.8 | E | N | N | conceito técnico, sem cena |
| 26 | L2-R107 | P2-2.7 | C | N | N | documentação de serviço/ferramenta, sem cena |
| 27 | L2-R138 | P2-2.1 | C | N | N | documentação de serviço/ferramenta, sem cena |
| 28 | L2-R139 | P2-2.1 | E | N | N | documentação de serviço/ferramenta, sem cena |
| 29 | L2-R24 | P2-2.1 | E | N | N | documentação de serviço/ferramenta, sem cena |
| 30 | L2-R37 | P2-2.2 | C | N | N | documentação de serviço/ferramenta, sem cena |
| 31 | L3-R10 | P2-4.3 | E | N | N | norma (LGPD/Lei 9.610/Marco Civil), sem cena |
| 32 | L3-R32 | P2-3.2 | E | N | N | documentação de serviço/ferramenta, sem cena |
| 33 | L3-R40 | P2-3.3 | C | N | N | documentação de serviço/ferramenta, sem cena |
| 34 | L3-R44 | P2-3.3 | E | N | N | documentação de serviço/ferramenta, sem cena |
| 35 | L3-R55 | P2-3.4 | E | N | N | documentação de serviço/ferramenta, sem cena |
| 36 | L3-R58 | P2-3.4 | C | N | N | documentação de serviço/ferramenta, sem cena |
| 37 | L3-R61 | P2-3.4 | C | N | N | documentação de serviço/ferramenta, sem cena |
| 38 | L3-R66 | P2-3.4 | E | N | N | documentação de serviço/ferramenta, sem cena |
| 39 | L3-R68 | P2-4.2 | C | N | N | norma (LGPD/Lei 9.610/Marco Civil), sem cena |
| 40 | L3-R70 | P2-4.2 | E | N | N | norma (LGPD/Lei 9.610/Marco Civil), sem cena |

## 4. P2 fronteira: N com sinal fraco (95, todos)

Coluna 'GCE-critério' = leitura pelo critério escrito (todas N, concordo). Coluna 'GCE-ambiente' = rótulo da seção 0 (N / L / S).

| # | id | folha | gab. | sinal fraco (CSV) | gcb | GCE-critério | GCE-ambiente | nota |
|---|---|---|---|---|---|---|---|---|
| 1 | L1-Q07 | P2-1.4 | E | audiência | N | N | L | audiência pública + convidados; sem sessão/órgão |
| 2 | L1-Q08 | P2-1.4 | C | sessão | N | N | N | 'diarizar uma sessão' é uso técnico |
| 3 | L1-Q11 | P2-1.5 | C | orador | N | N | N | orador = falante genérico (pontuação falada) |
| 4 | L1-Q16 | P2-1.7 | E | sessão | N | N | N | 'sessão' da Realtime API (sessão técnica) |
| 5 | L1-Q17 | P2-1.7 | C | orador | N | N | N | orador = falante genérico (endpointing) |
| 6 | L1-R06 | P2-1.3 | E | sessão | N | N | N | 'sessão de 2 horas' genérica |
| 7 | L1-R111 | P2-1.7 | E | orador | N | N | N | orador genérico |
| 8 | L1-R12 | P2-1.6 | E | sessão | N | N | N | 'sessão' como palavra homófona |
| 9 | L1-R121 | P2-1.8 | E | audiência | N | N | L | audiência pública de 8 kHz; sem órgão |
| 10 | L1-R132 | P2-1.1 | C | sessão | N | N | N | 'sessão' como trecho de áudio (CMUSphinx) |
| 11 | L1-R135 | P2-1.1 | E | sessão | N | N | N | 'sessão' genérica (sclite) |
| 12 | L1-R147 | P2-1.2 | C | sessão | N | N | N | 'sessões em português' genérico |
| 13 | L1-R165 | P2-1.4 | C | orador | N | N | L | orador rotulado 'Presidente' na referência; cue de Mesa, mas só isso |
| 14 | L1-R168 | P2-1.4 | E | orador | N | N | N | orador genérico (estéreo) |
| 15 | L1-R171 | P2-1.4 | C | audiência;sessão | N | N | S | audiência + 'presidente da sessão' (dois cues da Mesa) |
| 16 | L1-R180 | P2-1.5 | C | sessão | N | N | L | legenda ao vivo de 'uma sessão'; genérico |
| 17 | L1-R181 | P2-1.5 | C | sessão | N | N | S | fórmula 'Senhor Presidente, a sessão' (tratamento parlamentar) |
| 18 | L1-R185 | P2-1.6 | C | audiência | N | N | N | audiências genéricas |
| 19 | L1-R190 | P2-1.6 | E | sessão | N | N | N | 'sessão'/'seção' como palavras |
| 20 | L1-R192 | P2-1.7 | C | orador;sessão | N | N | N | 'troca de orador' genérica |
| 21 | L1-R196 | P2-1.7 | C | orador;sessão | N | N | L | legenda ao público 'à medida que o orador fala'; genérico |
| 22 | L1-R200 | P2-1.7 | C | sessão | N | N | L | legenda ao vivo de sessão; genérico |
| 23 | L1-R204 | P2-1.8 | C | sessão | N | N | N | degravar 'sessões' genérico |
| 24 | L1-R205 | P2-1.8 | E | sessão | N | N | N | 'órgão' + sessões; sem Casa |
| 25 | L1-R207 | P2-1.8 | E | audiência | N | N | N | audiência (arquivo); genérico |
| 26 | L1-R208 | P2-1.8 | C | sessão | N | N | N | degravação de sessões; genérico |
| 27 | L1-R23 | P2-1.1 | E | sessão | N | N | N | acervo das sessões; genérico |
| 28 | L1-R27 | P2-1.1 | E | sessão | N | N | N | avaliação de uma sessão; genérico |
| 29 | L1-R34 | P2-1.2 | C | sessão | N | N | N | acervo de áudios de sessões; genérico |
| 30 | L1-R39 | P2-1.2 | C | taquigrafia | N | N | L | 'notas taquigráficas' como corpus de LM |
| 31 | L1-R49 | P2-1.3 | C | sessão | N | N | N | gravação de uma sessão (LLM); genérico |
| 32 | L1-R52 | P2-1.3 | E | sessão | N | N | N | 'sessão conversacional' = sessão técnica |
| 33 | L1-R59 | P2-1.3 | E | sessão | N | N | N | gravação de uma sessão; genérico |
| 34 | L1-R60 | P2-1.3 | E | sessão | N | N | N | 'conexão/sessão' técnica |
| 35 | L1-R66 | P2-1.4 | C | orador;sessão | N | N | N | 'sessão longa' em vários arquivos; genérico |
| 36 | L1-R69 | P2-1.4 | E | orador | N | N | N | orador por canal; genérico |
| 37 | L1-R71 | P2-1.4 | E | orador | N | N | S | 'aparte' (termo próprio do Plenário) |
| 38 | L1-R74 | P2-1.4 | E | orador;sessão | N | N | L | 45 oradores na mesma sessão; genérico |
| 39 | L1-R86 | P2-1.5 | E | sessão | N | N | N | sessão ao vivo; genérico |
| 40 | L1-R89 | P2-1.6 | C | audiência | N | N | L | audiência pública + convidado estrangeiro |
| 41 | L1C-Q27 | P2-1.4 | C | orador | N | N | N | orador (menção ao verbo identificar) |
| 42 | L1C-Q28 | P2-1.4 | E | orador | N | N | N | orador (menção) |
| 43 | L1C-Q29 | P2-1.5 | C | registro oficial | N | N | L | 'registro oficial' genérico |
| 44 | L1C-Q30 | P2-1.5 | E | câmara (sentido não legislativo) | N | N | N | 'Câmara' citada como palavra (menção; capitalização) |
| 45 | L2-Q03 | P2-2.1 | E | sessão | N | N | S | 'notas oficiais de sessões' (produto do registro oficial) |
| 46 | L2-Q04 | P2-2.1 | C | registro oficial;sessão | N | N | L | 'registro oficial da sessão' genérico |
| 47 | L2-Q07 | P2-2.2 | E | orador | N | N | N | degravação + oradores; genérico |
| 48 | L2-Q11 | P2-2.3 | E | pronunciamento | N | N | N | pronunciamento; genérico |
| 49 | L2-Q12 | P2-2.3 | C | orador | N | N | N | orador; genérico |
| 50 | L2-Q13 | P2-2.4 | C | orador | N | N | N | reuniões com oradores; genérico |
| 51 | L2-Q16 | P2-2.4 | E | orador | N | N | N | pausa do orador; genérico |
| 52 | L2-Q18 | P2-2.5 | E | orador | N | N | N | orador cita números; genérico |
| 53 | L2-R09 | P2-2.5 | E | sessão | N | N | N | WER de sessões; genérico |
| 54 | L2-R102 | P2-2.6 | C | sessão | N | N | N | sessão em vídeo; genérico |
| 55 | L2-R112 | P2-2.7 | C | orador;sessão | N | N | N | sclite por locutor/orador; genérico |
| 56 | L2-R117 | P2-2.8 | E | questão de ordem | N | N | L | 'questão de ordem' como frase de vocabulário |
| 57 | L2-R122 | P2-2.8 | C | orador | N | N | S | 'reunião' com 'pauta' e 'oradores inscritos' (rito deliberativo) |
| 58 | L2-R133 | P2-2.1 | C | audiência | N | N | N | audiência (ground truth); genérico |
| 59 | L2-R14 | P2-2.7 | E | sessão | N | N | N | fiscal de contrato; norma administrativa, sem cena legislativa |
| 60 | L2-R68 | P2-2.4 | E | sessão | N | N | N | pausas de sessão; genérico |
| 61 | L2-R70 | P2-2.4 | E | audiência;orador | N | N | L | audiência pública + orador identificado |
| 62 | L2-R76 | P2-2.5 | C | audiência;orador | N | N | L | audiência pública em inglês (cena não legislativa) |
| 63 | L2-R84 | P2-2.5 | E | sessão | N | N | L | [aplausos]/(risos) em sessão; genérico |
| 64 | L2-R91 | P2-2.6 | C | sessão | N | N | N | exportação de sessão; genérico |
| 65 | L2-R93 | P2-2.6 | E | sessão | N | N | N | revisão das sessões; genérico |
| 66 | L2-R96 | P2-2.6 | E | audiência | N | N | L | audiência pública (Video Indexer) |
| 67 | L3-Q01 | P2-3.1 | C | pronunciamento;proposição | N | N | S | 'pronunciamentos' + 'números de proposições' (dois cues) |
| 68 | L3-Q02 | P2-3.1 | E | orador;sessão | N | N | N | sumarização de sessão; genérico |
| 69 | L3-Q04 | P2-3.1 | C | sessão | N | N | N | sessão como insumo; genérico |
| 70 | L3-Q07 | P2-3.2 | E | proposição | N | N | L | 'número de uma proposição' (um cue) |
| 71 | L3-Q11 | P2-3.3 | E | sessão | N | N | N | resumo da sessão; genérico |
| 72 | L3-Q23 | P2-4.2 | E | discurso | N | N | N | Lei 9.610 (norma); 'discursos' como espécie de obra |
| 73 | L3-Q26 | P2-4.2 | C | sessão | N | N | N | resumos de sessões; genérico |
| 74 | L3-Q28 | P2-4.3 | E | orador | N | N | N | orador anonimizado (LGPD) |
| 75 | L3-Q30 | P2-4.3 | C | sessão | N | N | N | áudio de sessões (LGPD) |
| 76 | L3-R03 | P2-3.2 | E | pronunciamento | N | N | N | acervo de pronunciamentos (vetorial) |
| 77 | L3-R106 | P2-4.1 | E | audiência | N | N | N | órgão público + audiência (diz 'órgão público', não Casa) |
| 78 | L3-R107 | P2-4.1 | C | audiência | N | N | N | órgão público + audiências (idem) |
| 79 | L3-R11 | P2-4.3 | E | sessão | N | N | N | áudios de sessões (LGPD) |
| 80 | L3-R15 | P2-3.1 | E | sessão | N | N | N | transcrições de sessões (busca) |
| 81 | L3-R17 | P2-3.1 | E | sessão | N | N | N | transcrições de sessões (busca) |
| 82 | L3-R18 | P2-3.1 | C | sessão | N | N | N | transcrições de sessões (busca) |
| 83 | L3-R19 | P2-3.1 | E | taquigrafia | N | N | L | notas taquigráficas como corpus |
| 84 | L3-R23 | P2-3.1 | C | taquigrafia | N | N | L | notas taquigráficas como corpus |
| 85 | L3-R26 | P2-3.2 | E | pronunciamento | N | N | N | acervo de pronunciamentos (embeddings) |
| 86 | L3-R27 | P2-3.2 | C | taquigrafia | N | N | L | notas taquigráficas como corpus |
| 87 | L3-R34 | P2-3.2 | C | pronunciamento;sessão | N | N | N | pronunciamentos + data da sessão |
| 88 | L3-R35 | P2-3.2 | E | pronunciamento | N | N | N | dotProduct; pronunciamentos |
| 89 | L3-R37 | P2-3.2 | E | pronunciamento;sessão | N | N | N | ordenação por data da sessão |
| 90 | L3-R46 | P2-3.3 | C | sessão | N | N | L | 'sessão com vários itens de pauta' |
| 91 | L3-R54 | P2-3.4 | C | audiência;orador | N | N | L | audiência pública + oradores PT/ES |
| 92 | L3-R57 | P2-3.4 | E | orador | N | N | N | orador; idioma |
| 93 | L3-R59 | P2-3.4 | E | orador | N | N | N | orador; idioma |
| 94 | L3-R65 | P2-3.4 | C | pronunciamento | N | N | N | acervo de pronunciamentos |
| 95 | L3-R84 | P2-4.3 | C | sessão | N | N | N | LGPD; sessões |

Totais da coluna GCE-ambiente: N 67, L 22, S 6.

## 5. Divergências e a pergunta do ambiente de sessão legislativa

**Divergências de aplicação do critério: nenhuma (0 em 175).**

**Divergência de critério (leitura de ambiente), 6 itens que a GCE contaria como moldura (hoje N):**

| id | gab. | cues |
|---|---|---|
| L1-R171 | C | audiência + 'presidente da sessão' (dois cues da Mesa) |
| L1-R181 | C | fórmula 'Senhor Presidente, a sessão' (tratamento parlamentar) |
| L1-R71 | E | 'aparte' (termo próprio do Plenário) |
| L2-Q03 | E | 'notas oficiais de sessões' (produto do registro oficial) |
| L2-R122 | C | 'reunião' com 'pauta' e 'oradores inscritos' (rito deliberativo) |
| L3-Q01 | C | 'pronunciamentos' + 'números de proposições' (dois cues) |

**Pergunta: um item cujo cenário é claramente de sessão legislativa deve contar como moldura em P2?** Sim, mas só quando o texto traz cue próprio do rito parlamentar, não pela palavra solta. Razões: (a) em P2 todo o módulo é transcrição na Câmara, de modo que o contexto natural não discrimina; se 'sessão', 'orador' e 'audiência' bastassem, quase todos os 564 itens teriam moldura e a métrica perderia sentido; (b) as três palavras são polissêmicas nos próprios itens (sessão da Realtime API, sessão como palavra homófona, trecho de áudio no CMUSphinx; 'orador' é o termo genérico de falante na documentação de diarização; 'audiência pública' ocorre também no Judiciário e no Executivo, e dois itens dizem expressamente 'órgão público'); (c) a candidata só reconhece a moldura como pista quando o enunciado a diz; (d) o critério, para ser reproduzível, precisa de lista fechada. Proposta de regra para a gbq-gerencia: acrescentar à lista T, como borda 'rito', os cues 'Senhor Presidente', 'aparte', 'orador(es) inscrito(s)', 'notas oficiais de sessões' e a combinação pronunciamento(s) + proposição(ões); sessão, orador, audiência e pronunciamento isolados continuam N.

## 6. %C de P2 sob cada leitura (itens com moldura)

| leitura | itens com moldura | C | E | %C |
|---|---|---|---|---|
| A. critério escrito da gcb-cpp (reproduz a seção 3 da contagem) | 208 | 112 | 96 | 53.8% |
| B1. A + 6 itens de ambiente inequívoco (regra 'rito' da seção 5) | 214 | 116 | 98 | 54.2% |
| B2. A + 28 itens (S e L: qualquer cue isolado de cena) | 236 | 129 | 107 | 54.7% |
| B3. A + os 95 de fronteira (sessão/orador/audiência etc. contam) | 303 | 156 | 147 | 51.5% |
| C. A sem os 55 S de âncora única (comissão/Casa) | 153 | 74 | 79 | 48.4% |
| (ref.) P2 inteiro, 564 itens, como se todo item tivesse a moldura do módulo | 564 | 284 | 280 | 50.4% |

Todas as leituras ficam dentro de 40 a 60% de C: a conclusão da gcb-cpp (P2 sem E faltante) se mantém em A, B1, B2, B3 e C. A escolha da leitura não muda a ação em P2 no total da matéria.

Efeito por folha (itens com moldura, C/E e %C), onde a escolha de leitura pesa; as demais folhas variam pouco:

| folha | A | B1 | B3 |
|---|---|---|---|
| P2-1.1 | 4/5 (44%) | 4/5 (44%) | 5/8 (38%) |
| P2-1.2 | 3/1 (75%) | 3/1 (75%) | 6/1 (86%) |
| P2-1.3 | 6/0 (100%) | 6/0 (100%) | 7/4 (64%) |
| P2-1.4 | 7/0 (100%) | 8/1 (89%) | 12/6 (67%) |
| P2-1.5 | 3/4 (43%) | 4/4 (50%) | 7/6 (54%) |
| P2-1.6 | 9/10 (47%) | 9/10 (47%) | 11/12 (48%) |
| P2-1.7 | 5/8 (38%) | 5/8 (38%) | 9/10 (47%) |
| P2-1.8 | 6/3 (67%) | 6/3 (67%) | 8/6 (57%) |
| P2-2.1 | 7/8 (47%) | 7/9 (44%) | 9/9 (50%) |
| P2-2.2 | 6/6 (50%) | 6/6 (50%) | 6/7 (46%) |
| P2-2.3 | 5/8 (38%) | 5/8 (38%) | 6/9 (40%) |
| P2-2.4 | 8/7 (53%) | 8/7 (53%) | 9/10 (47%) |
| P2-2.5 | 4/3 (57%) | 4/3 (57%) | 5/6 (45%) |
| P2-2.6 | 3/0 (100%) | 3/0 (100%) | 5/2 (71%) |
| P2-2.7 | 3/7 (30%) | 3/7 (30%) | 4/8 (33%) |
| P2-2.8 | 3/9 (25%) | 4/9 (31%) | 4/10 (29%) |
| P2-3.1 | 8/8 (50%) | 9/8 (53%) | 12/12 (50%) |
| P2-3.2 | 5/0 (100%) | 5/0 (100%) | 7/5 (58%) |
| P2-3.3 | 5/5 (50%) | 5/5 (50%) | 6/6 (50%) |
| P2-3.4 | 3/0 (100%) | 3/0 (100%) | 5/2 (71%) |
| P2-4.1 | 3/0 (100%) | 3/0 (100%) | 4/1 (80%) |
| P2-4.2 | 2/3 (40%) | 2/3 (40%) | 3/4 (43%) |
| P2-4.3 | 4/1 (80%) | 4/1 (80%) | 6/3 (67%) |

Folhas com 100% de C em A: 1.3, 1.4, 2.6, 3.2, 3.4 e 4.1. Em B1 só a 1.4 muda (7/0 para 8/1, 89%). Em B3 as seis passam a 58 a 80% (1.3: 7/4; 1.4: 12/6; 2.6: 5/2; 3.2: 7/5; 3.4: 5/2; 4.1: 4/1), mas a 1.1 cai a 38,5% e a 2.7 e a 2.8 seguem abaixo de 40% em qualquer leitura. Se a gbq-gerencia equilibra por folha, a leitura B3 reduz o reforço de E nessas seis folhas e não resolve 2.7 e 2.8; se equilibra só por matéria, não há ação em P2 em nenhuma leitura.

Observação sobre a âncora única: os 55 S ancorados só em 'comissão' ou 'Casa' têm 38 C e 17 E (69,1% de C); os 153 S de âncora forte têm 74 C e 79 E (48,4%). O excesso de C em P2-S vem desse bloco; se a gerência quiser a moldura mais restrita (leitura C), o %C de P2 é 48,4%, também dentro da faixa. Ressalva: a amostra S sorteada tem 26 C e 14 E, coerente com esse viés.

## 7. Limites

Os rótulos S/L/N da leitura de ambiente são julgamento da GCE e a decisão é da gbq-gerencia. A GCE não revisou o texto dos itens (nenhum foi alterado) e não conferiu P1-TI nem P1-DA (parte da GCB). Os 6 itens de ambiente inequívoco e os 22 limite estão listados na seção 4 para reaplicação por outra unidade (QA: gce-cqfp).

