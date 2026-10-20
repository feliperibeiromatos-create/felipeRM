# T118_reconciliacao_v1_13_2026-10-20.md — T-118 — reconciliação e gatilho A do pacote v1.13 — 2026-10-20 — gerado por gbq-gerencia

REMETENTE: gbq-gerencia (D1; passo 4.6 da D1 da T-118).
DESTINATÁRIO: presidencia (gatilho A em PARA_PRESIDENCIA.md, seção 7); orquestrador (promoção e commit, seção 5, só depois do sim); secretaria (mudanças em TAREFAS.md, seção 6).
Base: D1 da T-118 (`saida/pacote/T118_D1_v1_13_2026-10-20.md`, bbef6770…eaae), a D1 dos achados (`saida/pacote/T118_D1_achados_fidelidade_2026-10-20.md`, 03bbe6b6…257b), conferência da errata do achado 10 (`saida/gcb/QA_D6_achado10_conferencia_2026-10-20_gcb-cqfp.md`, 5e625c67…b202, CONFERIDO), MANIFESTO (`saida/pacote/montagem_v1_13/MANIFESTO_v1_13.md`), conferência de contagens (`out/conferencia_t118.json`), cobertura (`saida/pacote/cobertura_v1_13.md`), contrato v1.2.10 (`saida/pacote/contrato_v1_2_10_2026-10-20.md`, ponto 11 e seção 5) e v1.2.11 (`saida/pacote/contrato_v1_2_11_2026-10-20.md`), fidelidade R1 (`saida/pacote/montagem_v1_13/fidelidade_v1_13_T118_gbq-cqe.md`, 6c5f71f0…4ba4, APROVADO COM RESSALVAS) e R2 (`saida/pacote/fidelidade_v1_13_T118_R2_gbq-cqe.md`, 60d4bbeb…01dd6, ACEITO, achados R2-A a R2-D INFO), QA final (`saida/pacote/montagem_v1_13/QA_final_v1_13_v16_2026-10-20_gbq-cqe.md`, 67a61080…3910, seções 6, 7 e 8.7 a 8.9), DECISOES.md (D-AUDITORIA-20OUT, D-PACOTE-V113, D-CONTRATO-V1210, D-LOTED1 a 6-CANONICO, D-V15-PLATAFORMA). Precedente: `saida/pacote/T115_reconciliacao_v1_12_2026-10-18.md`.
Gate: nenhum. Matéria de forma do pacote, domínio da GBQ; sem conflito entre Gerências; a gbq-cqe aceitou (R2). A GBQ não produz nem corrige item.
Gravei só este arquivo e o item de PARA_PRESIDENCIA.md. Não alterei `out/`, `saida/plataforma/`, `saida/gbq/`, `saida/estudante/`, DECISOES.md nem TAREFAS.md. Nada promovido, nada publicado, sem commit.

Conferência própria (script `rec.py`, `python3 -I`, só leitura do repositório, no scratchpad da sessão `ger_t118_rec/`), em 20/10/2026:
- SHA-256 e bytes de todos os objetos da seção 2 iguais ao MANIFESTO, à R1 e à R2.
- `out/pacote.json`: 1.159 itens, C/E 582/577; 410 de DA (lotes D1 a D6: 60, 80, 71, 79, 70 e 50); 46 entradas P1-DA; 16 lotes (13 no estudante); 79 tópicos, 39 de DA; `volatil` em D2-01, D2-28, D6-09, D6-32 e D6-34; 0 item DA em `simulados`; nenhum dos BQ-0113 a BQ-0152 no pacote.
- `out/pacote_estudante.json`: `nucleo` DA 366 true e 44 false; 733 no total; os 14 itens fora de folha (P1-DA-1: 8; P1-DA-8: 6) todos true, o que fecha 352 (cobertura, em folha) + 14 = 366.
- `out/registro_adendo5.md`: os 410 ids DA do pacote presentes; 0 prefixos de 60 caracteres dos 410 enunciados.
- `out/estudante/`: 53 arquivos; 33 iguais byte a byte a `saida/estudante/`; mudam `NUCLEO.md` e `README.md`; 18 novos; nenhum arquivo da base sem par. Digest c6ecc6e5…29a9 (forma na seção 2, nota 2).
- `saida/gbq/`: só os adendos 1 a 4 (o adendo 5 não está lá; achado 5 da R1 cumprido).
- `saida/pacote/pacote.json` e `pacote_estudante.json` continuam os da v1.12 (3476525…e6024f e 23224c96…612abd): nada promovido.
- O template da v16 tem 0 ocorrências de "pares". O blob de HEAD de `out/pacote.json` é 007787e3…c192, o que a v16 publicada embute.

## 1. Decisão (D1)

**ACEITO, para gatilho A.** A GBQ propõe à Presidência os objetos da seção 2 como canônicos da v1.13, fechando a T-118, com as pendências da seção 4 registradas.

Diferente do precedente (T-115), não há condição de produção pendente. A errata do achado 10, a remontagem, as contagens, o adendo 5 regerado, a edição .md, a errata v1.2.11 e o MANIFESTO já foram conferidos pela gbq-cqe (R1 e R2). Depois do sim, restam só atos do orquestrador: promoção byte a byte e commit (seção 5).

| Objeto da fidelidade | R1 | R2 | Situação |
|---|---|---|---|
| Errata do achado 10 (fonte do lote D6) | APROVADO | — | Fechado |
| `pacote.json` e `pacote_estudante.json` | APROVADO | integridade OK (R2-7) | Fechado |
| `conferencia_t118.json`, `stats_v1_13_DA.json`, cobertura | APROVADO | integridade OK (R2-7) | Fechado |
| Adendo 5 | COM RESSALVAS (achados 2 a 5) | ACEITO (R2-3, R2-5) | Fechado |
| Edição .md (53 arquivos) | COM RESSALVAS (achado 1) | ACEITO (R2-1, R2-2) | Fechado pela errata v1.2.11 |
| MANIFESTO | APROVADO (achado 6) | ACEITO (R2-6), **70 arquivos** | Fechado |

**Registro do R2-A.** O número correto de arquivos do MANIFESTO é **70** (53 em `out/estudante/` e 17 fora). O "71" do passo 6 da D1 dos achados contou `run_manif.py`, auxiliar do meu ensaio no scratchpad, que não existe no repositório. O erro foi do critério, não do objeto. Fica corrigido aqui: vale 70.

## 2. Objetos aceitos (bytes e SHA-256 em disco, 20/10/2026)

| Objeto | Arquivo (hoje) | Bytes | SHA-256 |
|---|---|--:|---|
| `pacote.json` v1.13 | `saida/pacote/montagem_v1_13/out/pacote.json` | 2.906.558 | `82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240` |
| `pacote_estudante.json` v1.13-E | `saida/pacote/montagem_v1_13/out/pacote_estudante.json` | 2.644.822 | `04cbd593fdd30404ecb7f91f6b6722da6b2fc24e58d3c0eb68b10a4e792a0c40` |
| Adendo 5 do registro AUTORAL (111 linhas, LF) | `saida/pacote/montagem_v1_13/out/registro_adendo5.md` | 11.582 | `a1ca16811394dd6ec5df186b44155704a498bc03f6ac1e8cddaf87b6f7a87437` |
| Edição .md v1.13-E (53 arquivos) | `saida/pacote/montagem_v1_13/out/estudante/` | — | digest `c6ecc6e535f47d8aab8ebbbf0f143134f56c57fbdadbf8254901bf185d9329a9` (nota 2) |
| Contrato v1.2.11 (regra vigente) | `regras/pacote_contrato.md` | 72.183 | `85b30fccadce4eb9782e1e056613a2d680cec0c01aed44fd173bda7d248e616b` |
| Registro da errata v1.2.11 | `saida/pacote/contrato_v1_2_11_2026-10-20.md` | 8.331 | `fa5f5f69add75da798e1f25600186dbbcde3c0640b09653150c271a11fcd2e86` |
| Cobertura v1.13 (T-95) | `saida/pacote/cobertura_v1_13.md` | 15.134 | `13491263120b7b63f0891dc08c6de556245ecc94147687964390459b5bcbb8c1` |
| MANIFESTO (70 arquivos) | `saida/pacote/montagem_v1_13/MANIFESTO_v1_13.md` | 19.501 | `d56cb806def3e7264b73529614e09de2b2b9becc1732346eb52d363e31ec0403` |

Registros que ficam em `out/` como contraprova, sem promoção:

| Arquivo | Bytes | SHA-256 |
|---|--:|---|
| `out/conferencia_t118.json` (100 critérios, 0 FALHA) | 2.100.552 | `6c5250c90f99af57cb28c907789923403c2e8a6b404dc65369608f9e2b99844f` |
| `out/stats_v1_13_DA.json` | 2.145 | `f077cb33900b3f765b8c3259c1768b0dc3699ff2872fdfe24cf028b997dc7320` |
| `out/diag30_DA.json` (intocado; D-DIAG30-DA) | 988 | `eb1ced6df3d624ae62b82337db6a4cfe29b86baa9494e96aed1b3defe61a6800` |
| `out/estudante_md_v1_13.json` | 14.582 | `ad7374ddfe448e7ee3cfbbdbd72f79f4fd08fd3bd6537cf6f77d54946215f5fa` |
| `historico/registro_adendo5_R1_7224db40.md` (versão R1, achado 5) | 10.245 | `7224db40670608bff726f67b6b4769a509b225953146b80013b05d9c57f55918` |

Fontes de DA já no lugar (corrigidas na fonte, sem promoção): `saida/gcb/DA_plataforma/D6_plataforma.json` (184.191; `f8691dd5…7122`) e `D6_registro_formato.md` (`7998cc7b…90ca`). Os demais `D<n>_plataforma.json`, `D<n>_registro_formato.md` e `edital_DA.json` têm os SHA-256 da seção 4 do MANIFESTO.

Notas:
1. **A versão continua "v1.13".** O canônico (82c4117c…) difere da montagem embutida na v16 publicada (007787e3…c192, D-PACOTE-V113) só em `lotes[D6].pares[0].como`, campo que a v16 não lê (D1 da T-118, seção 2). Os dois SHA-256 ficam registrados. O mesmo vale para o estudante (04cbd593… × 8b5489b9…b8dd).
2. **Forma do digest da .md (fixada aqui; R2-D).** Uma linha por arquivo `estudante/<nome>.md` TAB `<sha256>`, ordenadas por caminho em ordem de bytes (`LC_ALL=C sort`), unidas por `\n` **com** `\n` final; o digest é o SHA-256 desse texto. Sem o `\n` final o valor seria ea14bef6…7fe6, que não vale.
3. **Os 20 arquivos .md que mudam ou entram em `saida/estudante/`** (os outros 33 são iguais byte a byte aos atuais):

| Arquivo | Bytes | SHA-256 |
|---|--:|---|
| NUCLEO.md (733 ids núcleo) | 7.567 | `daf80aa5113be8916a3109c50c4e821c6fc2a28aa7613775fc52f507c8f530a0` |
| README.md (v1.13-E) | 4.358 | `e5f58436cbceb6ff550ba88fe936abf59c929f221731f097e9b33d4eb8c41eaa` |
| DA_D1_estudo.md | 71.783 | `bbab97c4ba4cb970aa79d7ae962e6434bf1c0c0a83a2d7dd93bfe17155a7a570` |
| DA_D1_gabarito.md | 19.538 | `b5412f727a3739289a503fa82bfbbbd9579128776958a68318cec89575a97b47` |
| DA_D1_itens.md | 13.594 | `6101aa686ee904eada28168a34a3fab3c593d9aca22b831a0b40000ef9919064` |
| DA_D2_estudo.md | 322.779 | `7518e6b27bada606ecf8c7f5bb748387eebe8743a8b2215ffb84fb8c1e642e44` |
| DA_D2_gabarito.md | 29.784 | `d1a10d22d7d1d07d07b7013b6a5bd62a1ccac6e506e4953ee781aa05e0952dbf` |
| DA_D2_itens.md | 20.377 | `7516d728e72c9de27056747aec0c1cca8df8bf19a6cc1b742eedcd0f39feb7d6` |
| DA_D3_estudo.md | 160.728 | `7301bb18a32c076feacdf5abe7ae9289182a93fd82756358bbc554f3a72e5e6c` |
| DA_D3_gabarito.md | 25.152 | `30839f7eeefad4cbe06c61ab239d5b5ca6f3b3a612cbbc5f7d3fe3fc5b044837` |
| DA_D3_itens.md | 18.503 | `e6eca373951ab9ab337d58c8f18c575c9cfbc7e0e4cf8cea0e11e617fb362117` |
| DA_D4_estudo.md | 166.485 | `6386186b19341f95a0b6dd473faef452153dbd16859b0c0171d352badcfde839` |
| DA_D4_gabarito.md | 29.844 | `13906a8be474e91393800ee8b0f52d5d73350a143e520a1db6e2e28a796c49b1` |
| DA_D4_itens.md | 21.306 | `298331ecf5861ba8c487e281068ed4357ab9f86a376d988e7add0573589eff46` |
| DA_D5_estudo.md | 211.320 | `00784bbcf9a1771c02b706d83b2fe2c8213ce0e416f33b6b6a1b32595a42d65f` |
| DA_D5_gabarito.md | 24.462 | `f84ef589bf4bac7852dff70adf85d76daeaaf170b60892e20df5d5219fdce09a` |
| DA_D5_itens.md | 18.961 | `538f74c5a6822f07bccae02e3bc3f9d0b2dde9e8ab0f6e9a3ca14722eb9ceda3` |
| DA_D6_estudo.md | 131.726 | `c849c448c84cbcb9810eff970b01b577e88d12703049186f94d0872fff0f4988` |
| DA_D6_gabarito.md | 17.334 | `8b4878363a6f0d0c907d9aa8109a385b6ac01594c8f462ceb0fa9d66d2479676` |
| DA_D6_itens.md | 12.227 | `1f37c2f95d1986f469ab591334a868729911dbdfa63d6be485a140cf825a593b` |

## 3. Condições do gatilho A da v1.13 (contrato v1.2.10, ponto 11; seção 5 do registro), uma a uma

| Condição | Situação | Evidência |
|---|---|---|
| **(a)** Achado 1 do QA final resolvido (correção na GCB ou MANTER do Fundador), com nova montagem | **CUMPRIDA** | Correção na GCB por errata de forma registrada em cada `D<n>_registro_formato.md` ("Errata de forma — QA final 20/10/2026"). QA final, seção 8.7: achado 1 RESOLVIDO, varredura com 0 "folha" e 0 códigos R/F (eram 23), validador 0 FALHA. Nova montagem feita (`montar_v1_13.py` 723370f5…1ebe, "RESULTADO: 0 FALHA", 32 OK), refeita depois da errata do achado 10 (MANIFESTO, seção 1; R1, seção 3). O registro também consta da D-PACOTE-V113. |
| **(b)** Aceite canônico dos lotes D2 a D5 em DECISOES.md, com o SHA-256 da tabela do ponto 2 | **CUMPRIDA** | D-LOTED5-CANONICO (linha 162, `44ddcc98…1333`), D-LOTED2-CANONICO (163, `59cffaa6…bd2c`), D-LOTED3-CANONICO (164, `0f7a8b09…7930`) e D-LOTED4-CANONICO (165, `c1a7a935…e5d9`). Os quatro SHA-256 coincidem com a tabela do ponto 2 e com `entradas` de `conferencia_t118.json`. Para os lotes D1 e D6: linhas 93 e 117 (`63bd27c3…3d56`, `a9831058…4090`). DECISOES.md em disco (3fd7bed9…2d74) é o mesmo lido pelo MANIFESTO, e as linhas dos atos são as do mapeamento do `nucleo_k1k4`. |
| **(c)** Adendo 5 do registro GBQ, com os 410 ids DA | **CUMPRIDA** | `out/registro_adendo5.md`, `a1ca1681…7437`, 111 linhas. R1 (achado 2) corrigido no script (`registro_adendo_v113.py` `42b7025b…fa70`) e regerado. R2-3 ACEITO: faixas pela ordem numérica (lote D3 "D3-01 a D3-81 (sem os vagos da seção 4)", lote D5 "D5-01 a D5-71 (sem o vago da seção 4)"), 0 id de lote solto, seção 10 com os seis registros de formato, 0 enunciado. Minha conferência: 410/410 ids. Fica só em `out/` até a promoção (R2-5). |
| **(d)** Conferência de contagens da gbq-csc contra os canônicos | **CUMPRIDA** | `out/conferencia_t118.json` (`6c5250c9…844f`): 100 critérios, 0 FALHA. 410 itens com id e gabarito do canônico; 46 entradas P1-DA contíguas em 20–65; 6 lotes DA (16 no total); 39 tópicos DA (79); `nucleo` 366/44 com a distribuição prevista; `nucleo_k1k4` igual em 410/410 (letra (e)); 749 itens da v1.12 byte a byte; 38 do banco ausentes. Recontagem independente da gbq-cqe: R1, seção 4 (OK). |

Critérios de aceite do passo 4.6 da D1 da T-118:

| Critério | Situação |
|---|---|
| gbq-cqe ACEITO | R1 APROVADO COM RESSALVAS; as ressalvas bloqueantes (achados 1 e 2) foram fechadas e a R2 deu **ACEITO** (R2-1 a R2-7). |
| Contagens da secretaria iguais às de `conferencia_t118.json` | Iguais (tabela abaixo). |
| Pendências da seção 3 da D1 transcritas com responsável | Seção 4 deste arquivo. |

| Contagem | Secretaria (`cobertura_v1_13.md`) | `conferencia_t118.json` | Igual? |
|---|---|---|---|
| Itens no pacote | 1.159 | 1.159 (`itens_total`) | sim |
| Itens de DA por lote | lotes D1 a D6: 60, 80, 71, 79, 70 e 50 (ressalva (e)) | o mesmo (`da_por_lote`) | sim |
| Folhas de DA | 37 | 37 (`folhas_da`) | sim |
| DA em folha / fora de folha | 396 / 14 (P1-DA-1 8; P1-DA-8 6) | 396 / 14 (`itens_fora_por_entrada` igual) | sim |
| VOLÁTEIS de DA | 5 | 5 (`volateis`) | sim |
| Núcleo de DA | 352 em folha (+ 14 fora, todos true) | 366 true / 44 false | sim (352 + 14 = 366) |
| Folhas de DA com 20 ou mais | 3 (2.1 = 22, 11 = 30, 12 = 20) | `itens_por_folha` dá os mesmos três | sim |
| C/E do pacote | 582 / 577 | soma dos lotes DA 202/208 + v1.12 380/369 = 582/577 | sim |

As condições adicionais da D-AUDITORIA-20OUT também estão atendidas: a T-118 é a primeira da fila, e as ressalvas da gbq-cqe ficam como pendências com responsável (seção 4). A errata v1.2.11 do contrato não é condição do ponto 11, mas é condição para promover a edição .md. Ela está registrada e conferida (R2-1).

## 4. PENDÊNCIAS (ressalvas com responsável e tarefa de destino; D-AUDITORIA-20OUT)

Nenhuma bloqueia o gatilho A.

| # | Pendência | Origem | Gravidade | Situação | Responsável | Tarefa de destino |
|---|---|---|---|---|---|---|
| P1 | Ids de lote D1 a D5 iguais aos das discursivas D1 a D5 | QA final, achado 4 | BAIXA | REGISTRADO e mantido (D1-V1210-06; contrato v1.2.10, ponto 9). Aplicado na v1.13: adendo 5 e MANIFESTO com "lote D<n>" (scan_q = 0). Nenhuma discursiva nova pode repetir o id do lote D6. | gbq-gerencia (regra) e gbq-csc (aplicação em todo relatório e registro) | Regra permanente, sem tarefa; a T-123 aplica o scan_q ao adendo 6 |
| P2 | Notas editoriais no texto de DA ("o curso não afirma…", "[REVOGADO]", "No texto próprio do curso", "Item C com elemento que parece trocado", "O documento da CGU é documento interno do órgão…") | QA final, achado 8 | BAIXA | Ressalva mantida; a candidata vê, sem erro de conteúdo | gbq-estilo revisa; se mudar, gcb-cpp faz errata de forma registrada (sem tocar enunciado nem gabarito) e gcb-cqfp confere | T-117 (BACKLOG); consolidação na T-123 |
| P3 | Meta `mapaspro:versao` "publicada em 20/10/2026" | QA final, achado 9 | INFO | Coincide com a data da publicação; sem ação | desenvolvedor-plataforma | T-123 (ajustar a data na próxima montagem da plataforma) |
| P4 | Frase "O exemplo é hipotético." (26 exemplos do lote D1; o lote D6 não a traz) | D1 da T-118, seção 3 | — | Decisão pendente do Fundador; não bloqueia | Fundador decide; gcb-cpp aplica por errata de forma | T-117 |
| P5 | A v16 publicada embute o pacote anterior à errata do achado 10 (007787e3…c192); o canônico é 82c4117c…f240. Diferença só em `lotes[D6].pares[0].como` (pares), campo que a v16 não lê (0 referências no template): invisível à candidata | D1 da T-118, seção 2; R1, achado 8 | INFO | Registrada. A v16 **não** é remontada nem republicada | orquestrador e desenvolvedor-plataforma | T-123 (a próxima plataforma embute o canônico) |
| P6 | 38 itens de banco com `itemEdital` P1-DA (BQ-0113 a BQ-0152, sem BQ-0131 e BQ-0133), fora da v1.13; BQ-0151 inapto (art. 14 revogado) | contrato v1.2.10, ponto 10; D1-V1210-08; T-118 (d) | — | Fora da v1.13 (exceção registrada). A entrada muda o `nucleo` de DA (banco antes, k2 = 0) e exige conferir a aptidão item a item | gbq-gerencia (D1 própria) → gbq-csc | T-123 |
| P7 | Mapeamento de atos no gerador: `nucleo.py` sem ato para o prefixo D; atos dos lotes D1 a D6 (D1 da T-118, seção 4.3) e ato de aceite de cada leva para os ids D<n>-R<nn> | T-118 (e); D-CONTRATO-V1210 | — | Mapeamento verificado na v1.13 (`nucleo_k1k4` 410/410); o gerador_v1_12 fica congelado | gbq-csc | T-123 |
| P8 | Critério "71 arquivos" do MANIFESTO; o certo é 70 | R2-A | INFO | Corrigido e registrado aqui (seção 1). Para critérios futuros: contagem de manifesto tirada da pasta real, nunca de ensaio no scratchpad | gbq-gerencia | Regra para a D1 da T-123 |
| P9 | "Seções 2 e 9 iguais byte a byte" contradiz a linha 26 (seção 2), que mudou só pela qualificação | R2-B | INFO | Registrado; o objeto está certo (tabela da seção 2 e seção 9 iguais) | gbq-gerencia | Sem tarefa |
| P10 | Remissão errada no ponto 4 da errata v1.2.11 ("ponto 6 da v1.2.9 e ponto 8 da v1.2.10"); a regra do `NUCLEO.md` está no ponto 6 da v1.2.7, e as de itens e gabaritos .md nas v1.2.1 (ponto 1) e v1.2.5 (ponto 4) | R2-C | INFO | Sem efeito ("nada mais muda" está certo) | gbq-gerencia | Próxima errata do contrato (T-123) |
| P11 | Digest da .md sem forma fixada (`\n` final) | R2-D | INFO | Fixada aqui (seção 2, nota 2) | gbq-gerencia | Regra para a D1 da T-123 |
| P12 | 34 folhas de DA abaixo de 20 (faltam 356; 8 com menos de 10) | cobertura v1.13, ressalvas (a4) e (f) | — | Todas na onda programada; nada em PARA_PRESIDENCIA.md | GCB (titular) | T-116 (depois da T-122) |
| P13 | Coluna "Onda programada" de P1 não reconstruída (n/r); 14 folhas de P1 abaixo de 20 | cobertura v1.13, ressalva (d) | — | Sem mudança de P1 desde a v1.12 | secretaria | T-95, ocorrência v1.14 |
| P14 | Itens com `volatil`: D2-01, D2-28 (REVERIFICAR), D6-09, D6-32, D6-34; fora de simulado final até a reverificação de janeiro | adendo 5, R1; D-LOTED2 e 6-CANONICO | — | Já registrados | qa-normativo-da → gcb-gerencia | T-120 (sem mudança) |
| P15 | Pendências da execução de 20/10 fora da T-118: GitHub, transporte aos chats, `juntar_partes.py` | D1 da T-118, seção 3 | — | Fora do escopo; sem efeito sobre o gatilho. O item (a) da T-121 (branch em main) consta como cumprido pela D-BRANCH-MERGE-20OUT | orquestrador e Fundador | T-121 |
| P16 | Commit dos arquivos da T-118 (hoje não versionados ou modificados na árvore) | git status de 20/10 | — | Ato do orquestrador depois do sim | orquestrador | Seção 5 |
| — | Achados 1, 2, 3, 5, 6, 7 e 10 do QA final; achados 1 a 6 da R1 | QA final 8.7; R1; R2 | — | RESOLVIDOS (achado 10 pela errata na fonte, CONFERIDO pela gcb-cqfp; achados da R1 pela D1 dos achados e R2 ACEITO). Achados 7 e 8 da R1 eram INFO, sem ação | — | — |

## 5. Plano de promoção (ato separado do orquestrador, só depois do sim da Presidência)

Promoção byte a byte, a partir da raiz do repositório. Promover não é publicar.

| Origem (`saida/pacote/montagem_v1_13/out/`) | Destino canônico | SHA-256 esperado no destino |
|---|---|---|
| `pacote.json` | `saida/pacote/pacote.json` (substitui a v1.12) | `82c4117c…f240` |
| `pacote_estudante.json` | `saida/pacote/pacote_estudante.json` (substitui a v1.12-E) | `04cbd593…0c40` |
| `registro_adendo5.md` | `saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo5_2026-10-20.md` | `a1ca1681…7437` |
| `estudante/` (53 .md) | `saida/estudante/` (substitui os 35; acrescenta 18) | digest `c6ecc6e5…29a9`; os 20 da seção 2, nota 3 |

Não são promovidos (ficam em `out/` como registro e contraprova): `conferencia_t118.json`, `stats_v1_13_DA.json`, `diag30_DA.json`, `estudante_md_v1_13.json` e `historico/`. Os demais objetos da seção 2 (contrato, registro da errata, cobertura, MANIFESTO) já estão no lugar definitivo. A v1.13 não tem registro de alterações por id: para DA, esse papel é dos `D<n>_registro_formato.md` (contrato v1.2.10, ponto 2), já em `saida/gcb/DA_plataforma/`.

```sh
O=saida/pacote/montagem_v1_13/out
cp "$O/pacote.json" "$O/pacote_estudante.json" saida/pacote/
cp "$O/registro_adendo5.md" saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo5_2026-10-20.md
cp "$O"/estudante/*.md saida/estudante/
cmp "$O/pacote.json" saida/pacote/pacote.json && cmp "$O/pacote_estudante.json" saida/pacote/pacote_estudante.json \
 && cmp "$O/registro_adendo5.md" saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo5_2026-10-20.md \
 && for f in "$O"/estudante/*.md; do cmp "$f" "saida/estudante/$(basename "$f")" || exit 1; done && echo promocao-ok
ls saida/estudante/*.md | wc -l                                   # esperado 53
(cd saida && find estudante -type f -name '*.md' | LC_ALL=C sort | while read p; do printf '%s\t%s\n' "$p" "$(sha256sum "$p" | cut -d' ' -f1)"; done) | sha256sum   # esperado c6ecc6e5…29a9
sha256sum saida/pacote/pacote.json saida/pacote/pacote_estudante.json saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo5_2026-10-20.md   # 82c4117c…, 04cbd593…, a1ca1681…
```

**Commit (orquestrador).** O commit do ciclo leva os arquivos da T-118: `saida/pacote/montagem_v1_13/` (sem `__pycache__/`), os promovidos, `regras/pacote_contrato.md`, `saida/gcb/DA_plataforma/D6_plataforma.json`, `D6_registro_formato.md`, `saida/gcb/QA_D6_achado10_conferencia_2026-10-20_gcb-cqfp.md` e os arquivos `saida/pacote/T118_*`, `contrato_v1_2_11_*`, `cobertura_v1_13.md` e `fidelidade_v1_13_T118_R2_*`. Recomendação da GBQ, pelo precedente da T-115 (seção 4; nenhum arquivo da pasta tem CR hoje): acrescentar ao `.gitattributes` as linhas `saida/pacote/montagem_v1_13/** text eol=lf` e `saida/pacote/montagem_v1_13/out/** -text -eol`, para que um checkout com autocrlf não mude os bytes fixados. Depois do `git add`, confira:

```sh
git cat-file -p :saida/pacote/pacote.json | sha256sum                                   # 82c4117c…
git cat-file -p :saida/pacote/pacote_estudante.json | sha256sum                         # 04cbd593…
git cat-file -p :saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo5_2026-10-20.md | sha256sum   # a1ca1681…
for f in $(git ls-files saida/pacote/montagem_v1_13/out saida/estudante); do git cat-file -p ":$f" | cmp -s - "$f" || echo "DIFERE $f"; done   # esperado: nada
```

Se algum `cmp` ou SHA-256 divergir, o orquestrador não commita e devolve à GBQ com o arquivo e os dois valores.

Depois da promoção e do commit: a T-118 fica CONCLUÍDA (competência D da Presidência), a ocorrência v1.13 da T-12 também, e a fila segue para a T-122 (D-AUDITORIA-20OUT, condição 1). O registro GBQ vigente passa a ser "v3 + adendos 1 a 5" (contrato v1.2.10, ponto 2).

**Declaração.** Nada vai à plataforma. A T-118 não remonta nem republica a v16 e não toca `saida/plataforma/` (4d19eb05… e c6de3f2a… inalterados). Qualquer publicação futura exige o gatilho A fechado (D-AUDITORIA-20OUT) e o "sim" do Fundador (D-V15-PLATAFORMA). A próxima plataforma (T-123) embute o canônico.

## 6. Mudanças que a secretaria deve fazer em TAREFAS.md (a GBQ não edita a fila)

1. **T-118**: estado de "EM CURSO (ciclo s15c1)" para "EM CURSO — gatilho A emitido (ciclo s15c1; saida/pacote/T118_reconciliacao_v1_13_2026-10-20.md); aguarda a Presidência". Com o sim, a promoção e o commit (seção 5), passa a "CONCLUÍDA (D-<ato da Presidência>; pacote.json 82c4117c…, pacote_estudante.json 04cbd593…, adendo 5 a1ca1681…, edição .md 53 arquivos c6ecc6e5…, contrato v1.2.11 85b30fcc…, cobertura 13491263…)". Corrigir a saída: de `saida/pacote/registro_adendo5_v1_13.md` para `saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo5_2026-10-20.md` (via `out/registro_adendo5.md`; D1 da T-118, seção 1), mais esta reconciliação e `saida/pacote/cobertura_v1_13.md`. Anotar por letra: (a), (b), (c), (f) e (g) cumpridas; (e) verificada (`nucleo_k1k4` 410/410), uso no gerador → T-123; (d) → T-123.
2. **T-117**: anotar "achado 10 CONCLUÍDO (correção na fonte, gcb-cpp; CONFERIDO pela gcb-cqfp, QA_D6_achado10_conferencia_2026-10-20_gcb-cqfp.md; remontagem 82c4117c…/04cbd593…; a plataforma não foi remontada nem republicada: a D1 da T-118, seção 2, substituiu a rota build_plataforma_v16.py e conferência D)". Tirar a classe "PRÓXIMO (o achado 10)". Ficam: achado 8 (BACKLOG; gbq-estilo; consolidação na T-123) e a frase "O exemplo é hipotético." (decisão do Fundador). O achado 9 passa à T-123. Estado: PENDENTE.
3. **T-123**: acrescentar ao objeto: "e os 38 itens de banco P1-DA por D1 própria da GBQ (T-118 (d); BQ-0151 inapto, art. 14 revogado); gerador com o mapeamento de atos dos lotes D1 a D6 (D1 da T-118, seção 4.3) e o ato de aceite de cada leva para os ids D<n>-R<nn>; a próxima plataforma embute o pacote canônico (fecha a divergência da v16, 007787e3 × 82c4117c); meta `mapaspro:versao` com a data da publicação (achado 9); edição .md de DA na forma do ponto 2 da v1.2.11; remissão do ponto 4 da v1.2.11 corrigida na próxima errata (R2-C); critérios com digest de forma fixada e contagem de manifesto pela pasta real (R2-A, R2-D)". Base: "sobre a v1.13 canônica (82c4117c…/04cbd593…)".
4. **T-12**: anotar "ocorrência v1.13 concluída pela T-118 (D-PACOTE-V113 e o gatilho A de 20/10/2026, ciclo s15c1)" depois do sim e da promoção; próxima ocorrência: v1.14 (T-123).
5. **T-95**: anotar "ocorrência v1.13 CONCLUÍDA (ciclo s15c1; saida/pacote/cobertura_v1_13.md, 13491263…; 75 folhas; DA 3 com 20 ou mais e 34 abaixo, todas na onda da T-116; nada a escrever em PARA_PRESIDENCIA)". Na ocorrência v1.14, reconstruir a coluna "Onda programada" de P1 (ressalva (d)).
6. **T-122**: sem mudança de texto. Com o fechamento da T-118, passa a ser a primeira da fila AGORA (D-AUDITORIA-20OUT). O pacote a contar é o v1.13 canônico (82c4117c…).
7. **T-116**: sem mudança de texto; a contagem de partida é a de `cobertura_v1_13.md` (13491263…).
8. **T-121**: anotar no item (a) "cumprido pela D-BRANCH-MERGE-20OUT (PR #3 mesclado em main, 19e7ca9)", se a secretaria confirmar na linha de DECISOES.md.
9. **T-119, T-120, T-11 e T-124**: sem mudança.

## 7. Gatilho

GATILHO A da GBQ em PARA_PRESIDENCIA.md (ciclo 2026-10-20 s15c1): aceitar como canônicos da v1.13 os objetos da seção 2, fechando a T-118, com as pendências da seção 4 registradas; promoção pela seção 5 só depois do sim; nada à plataforma.
