# MANIFESTO — T-57 — gerador v1.4 do pacote e da edição do estudante — 2026-10-13 — gerado por gbq-csc

Origem: cópia de `saida/pacote/gerador_v1_3/` (intacto: SHA-256 e bytes dos 93 arquivos conferidos contra o `MANIFESTO.md` dela, 0 divergências; `git status` sem alteração nela) para `saida/pacote/gerador_v1_4/`, alterada depois. `conferencias_v13.py` e `relatorio_v1_3.py` não foram trazidos (continuam na v1_3; os da v1.4 são `conferencias_v14.py` e `relatorio_v1_4.py`). Scripts temporários da ocorrência (aplicação do contrato, montagem do relatório) ficaram só no scratchpad. Comando de execução (a partir de qualquer pasta; `-B` evita `__pycache__`, `-I` não serve porque bloqueia os imports entre scripts): `sh saida/pacote/gerador_v1_4/rodar_tudo.sh` (roda o pipeline abaixo) ou `python3 -B saida/pacote/gerador_v1_4/<script>.py`.

## Ordem de execução

`rodar_tudo.sh` apaga e recria `out/` e roda os passos abaixo, na ordem, parando na primeira falha (`set -e`). Cada `out/*_stdout.txt` é a saída-padrão do script, **redirecionada pelo runner** (os scripts não gravam esses arquivos). Quem rodar os scripts à mão deve redirecionar do mesmo modo para obter os mesmos `*_stdout.txt`.

| # | Comando | Redirecionamento da saída-padrão | Arquivos que o próprio script grava em `out/` |
|---|---|---|---|
| 1 | `python3 -B build_pacote.py` | `> out/gen_stdout.txt` | `pacote.json`, `stats.json` |
| 2 | `python3 -B estudante_gen.py` | `>> out/gen_stdout.txt` (acrescenta ao do passo 1) | `estudante/` (43 arquivos), `estudante_contagem.json` |
| 3 | `python3 -B estudante_fidelidade.py` | `> out/fidelidade_stdout.txt` (caminhos impressos relativos à raiz do repositório; sem caminho absoluto) | `estudante_fidelidade.json` |
| 4 | `python3 -B sync_check.py` | `> out/sync_stdout.txt` (conteúdo igual ao de `sync_check.txt`) | `sync_check.txt`, `sync_check.json` |
| 5 | `python3 -B validate.py` | `> out/validate_stdout.txt` | `validate.json` |
| 6 | `python3 -B conferencias_v14.py` | `> out/conferencias_stdout.txt` (conteúdo igual ao de `conferencias_v14.txt`) | `conferencias_v14.txt`, `conferencias_v14.json`, `varredura_volatil_v14.json` |
| 7 | `python3 -B fidelidade_mutacao.py` (~2 min: 11 mutações, cada uma com a fidelidade completa) | `> out/mutacao_stdout.txt` | `fidelidade_mutacao.json` |
| 8 | `python3 -B relatorio_v1_4.py` | `> out/relatorio_stdout.txt` (uma linha: n.º de linhas) | `pacote_relatorio_2026-10-13_v1_4.md` |

Tudo grava em `out/`; a promoção para `saida/pacote/pacote.json`, `saida/estudante/` e `saida/pacote/pacote_relatorio_2026-10-13_v1_4.md` é um passo explícito (cópia) depois de todas as conferências com 0 falhas. Caminhos derivados de `__file__` (raiz do repositório = três níveis acima de `gerador_v1_4/`); as referências v1/v1.1/R0/v1.2/v1.3 vêm do git por `refs.py` (`git show <commit>:<caminho>`, somente leitura): v1 `5eab2d9`, v1.1 `e97ab1f`, R0 `27e594d`, v1.2 `2684ab1`, v1.3 `9622604`. A conferência (c) da v1.4 lê também o contrato v1.2.1 do git (`9622604`) e o arquivo `regras/pacote_contrato.md` atual (v1.2.2).

## Scripts históricos (O-1, D-T56-05: opção "marcar")

Não executáveis, mantidos sem alteração como registro da R0/R1; conferido em 13/10/2026 (cwd `/tmp`): cada um sai com código 1 e não grava nada no repositório: `relatorio_R1.py` (falta `out/conferencias_R1.json`), `report.py` (falta `stats.pkl`), `report2.py` (`ValueError`, formato de `stats` mudou), `diff.py` (`TypeError`) e `diff2.py` (`KeyError: legendaMecanismo`). Executáveis e também históricos: `conferencias_R1.py` (118 conferências, 0 falhas, lê R0 e R1 do git; grava `out/conferencias_R1.json` e `out/varredura_volatil.json`, fora do pipeline), `probe.py`, `resid.py` e `review.py`. `texts.py` é módulo auxiliar ativo.

## Arquivos (SHA-256 de cada um)

| Arquivo | Bytes | SHA-256 | Estado frente à v1_3 | Papel |
|---|---|---|---|---|
| banco.py | 3184 | `6d6e975561ae53c54021a64cd8f17a2fba68f945d7f5a9ed83992163e750cfaf` | igual à v1_3 | ativo |
| build_pacote.py | 7973 | `4aae16c99e18707f08c059ae2b1bd5a10fb222f62b84842a3f358facafd3edba` | alterado | ativo |
| common.py | 6168 | `71728e87af8903a9c9a17a493c3dc3ad147da775ab085a2b4e2bc5852f31761a` | alterado | ativo |
| conferencias_R1.py | 31123 | `587a8d4212429b2c4917c669106af4cb4864cd811481de6b473828bc6e6cc92e` | igual à v1_3 | histórico (executável; v1.2/R0/R1; lê do git; se rodado grava out/conferencias_R1.json e out/varredura_volatil.json, que não fazem parte do pipeline) |
| conferencias_v14.py | 49024 | `d4a9ce0104a4d5481bce52b7770da68415633dccf04eaf0cee26f01bb5c88eaf` | novo | ativo |
| diff.py | 1751 | `59fef679b240aa9e1ae7895813f4dd7be8251ae06a69921d37874ff843376bfb` | igual à v1_3 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| diff2.py | 1547 | `6513c3b66b2b0e09669a8624f77408fe8f4f1ce6f350a391e82558e5262901d0` | igual à v1_3 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| edital_p.py | 1183 | `0f7ed100392cdba1c09e1cf2dce107801c2fe8225920a5d501d6fc42bf89423d` | igual à v1_3 | ativo |
| estudante_fidelidade.py | 25334 | `357e0b6808a5a0cdec7ac1ff75650acbbe131a694c560f79a99e980cc8c60a28` | alterado | ativo |
| estudante_gen.py | 14488 | `1422e5340e0401e6e42be63b331dd8634cd18a79c28a224ca0b51723b3f02215` | alterado | ativo |
| estudante_marcas.py | 9897 | `41cf6eecc05d9d52c5115a383a4a2e44af56502f04d6d81ea0bfa040999c485f` | alterado | ativo |
| f4.py | 2542 | `e0fb812b44b2822c9d5caad8c5018b1b0df5c929e5182368e2434413f3f52727` | igual à v1_3 | ativo |
| fidelidade_mutacao.py | 3112 | `e32336051ab48f58e2a2248d9cdc303eccce7d53aaeef84ca9fda82629537a99` | alterado | ativo |
| gce.py | 5972 | `e007ddaeac3b07f7f47fe7472c1ec6a1d418f731e185f4baaf678e822153212c` | igual à v1_3 | ativo |
| literais.py | 14182 | `93c64cd58bff76ab3afb8a7429cb3ba2b4d8af7353191e015d8949531b08518b` | alterado | ativo |
| lotes_tab.txt | 912 | `895e4d50479615c6963fcd35c01d3cd57aa8bad3994dec6c08a1a639517d27a2` | igual à v1_3 | ativo |
| out/conferencias_stdout.txt | 17000 | `3d4a31a6df474a710b0fc26478e0bc6f8f0eef79801d5a8dcf9d5b1e1d5a486a` | gerado | saída |
| out/conferencias_v14.json | 19603 | `11d4e9082519eda2ad1f6876605f313f168e0fb0b9faa2583055cea983f40067` | gerado | saída |
| out/conferencias_v14.txt | 17000 | `3d4a31a6df474a710b0fc26478e0bc6f8f0eef79801d5a8dcf9d5b1e1d5a486a` | gerado | saída |
| out/estudante/BANCO_gabarito.md | 9340 | `f7d9bb470356e98962227bc7d19dbd6de2eff053aa718df002b26d6f2b4cb5ed` | gerado | saída (edição do estudante gerada) |
| out/estudante/BANCO_itens.md | 76551 | `879e1769c76c3bc655510a18a8fd66f49abb6dec52d7e3030adf93132a226c2c` | gerado | saída (edição do estudante gerada) |
| out/estudante/DISCURSIVAS.md | 6674 | `075b68c83526dab71905bc1370cf939a4d5135c7654d4d4bdc6b5d4374705f9a` | gerado | saída (edição do estudante gerada) |
| out/estudante/DISCURSIVAS_padrao.md | 31772 | `884abe2c1675c44e9dedfa90a0141568eb9844145379501d5d969c9eb16abe20` | gerado | saída (edição do estudante gerada) |
| out/estudante/L1C_estudo.md | 3684 | `3dccee77e4a1eb4df12e0456dae9079843b49aa99a9f7789bd8025781f44be91` | gerado | saída (edição do estudante gerada) |
| out/estudante/L1C_gabarito.md | 1998 | `578698c50274793480ffd737559cc36cf3aa6ba15531c5966e08503b20541cf3` | gerado | saída (edição do estudante gerada) |
| out/estudante/L1C_itens.md | 2549 | `17c3920237a22564346db61b81f05e75cb8b103fd16d08999555a8473090b12c` | gerado | saída (edição do estudante gerada) |
| out/estudante/L1_estudo.md | 31818 | `04c2bacd39bf2301746d88848ad61b6dcdba954782102cf274fc02a3d49fec77` | gerado | saída (edição do estudante gerada) |
| out/estudante/L1_gabarito.md | 4784 | `e0a3084fe53efff0d2e58256340e3df86aecd6001b874a44e412917d563db80d` | gerado | saída (edição do estudante gerada) |
| out/estudante/L1_itens.md | 5121 | `9d888c024c20eb8ecb09d590f712b0f683ebf9cbc653ff5fc42b7564946642ab` | gerado | saída (edição do estudante gerada) |
| out/estudante/L2_estudo.md | 33400 | `d4e49cf68dd872e67db9cd0a63875e3ae8a9aac95ca882fb79f098a51772f143` | gerado | saída (edição do estudante gerada) |
| out/estudante/L2_gabarito.md | 6508 | `01b60a5e5ac6239e303419e4ca6615271a5dab410cde7484e94f264cf0ed366b` | gerado | saída (edição do estudante gerada) |
| out/estudante/L2_itens.md | 7391 | `a4ddb9ff0dfbf1e9487ccb93caa45406c2cc290c7f3b98b367d7160aad46ed66` | gerado | saída (edição do estudante gerada) |
| out/estudante/L3_estudo.md | 40424 | `3d226e76971a7e67f64feed0e8d8a10cdd695253f28fc58e9b734c9e505cefd3` | gerado | saída (edição do estudante gerada) |
| out/estudante/L3_gabarito.md | 6481 | `1cbc0474f03eaaede62a63e281b554f93ff5de6675df6480f0dc21d4e995b3ee` | gerado | saída (edição do estudante gerada) |
| out/estudante/L3_itens.md | 7594 | `5f340894de388b976ced1c17c67c34d80b74bba0c0aa3940aa71005e6ab27845` | gerado | saída (edição do estudante gerada) |
| out/estudante/L4C_estudo.md | 253 | `de79e9d124c9a83b3a7990da30d2440cdc4a7c498aa48d9aefc53d3ffdb3ba22` | gerado | saída (edição do estudante gerada) |
| out/estudante/L4C_gabarito.md | 6342 | `13d4a5cb284e04cd1e87b73740d2a2a80cfd8de80ebbc26e22187a8336cb9bdd` | gerado | saída (edição do estudante gerada) |
| out/estudante/L4C_itens.md | 2386 | `6955ac76f4724f46f3e187d0aced064770e8050de12f0e86ada71860e51c5f94` | gerado | saída (edição do estudante gerada) |
| out/estudante/L4_estudo.md | 49282 | `f9ea6165087e2bc3e54540b5515b6f987df9eb21d0ebe85a5f96a31ef774f1ed` | gerado | saída (edição do estudante gerada) |
| out/estudante/L4_gabarito.md | 5873 | `fe0574515510cd8f9115d5e18805a45ae16eb6d927bfca11020b6d017b3acafb` | gerado | saída (edição do estudante gerada) |
| out/estudante/L4_itens.md | 4527 | `58b63daca4fd6bb536c7db1e771eeb819c508ce240d35e9beb0efd1b2ed4a7e8` | gerado | saída (edição do estudante gerada) |
| out/estudante/L5C_estudo.md | 367 | `d66b4a9ac213ca9b15079c6d1303a9876309643c5aa7ad4aa344df708d8ccb3e` | gerado | saída (edição do estudante gerada) |
| out/estudante/L5C_gabarito.md | 4855 | `141c01fb0f0a0d65686b99eb39b8c2f2b51b58630c20b526b35992b951385027` | gerado | saída (edição do estudante gerada) |
| out/estudante/L5C_itens.md | 2321 | `8f0eaa89d72259e24496cfc80a61847c4b46c5bf62a53017cd3673fdcd5006e1` | gerado | saída (edição do estudante gerada) |
| out/estudante/L5_estudo.md | 31713 | `ecf286055639ae0ed0f510f87ce687ff4c6133e313b57c0f082cc851d0fa4859` | gerado | saída (edição do estudante gerada) |
| out/estudante/L5_gabarito.md | 5128 | `045ebb88f3d7a9d6f0ed595930601fb1bb0fda7ac2fff8d6cc4782e7fce7757e` | gerado | saída (edição do estudante gerada) |
| out/estudante/L5_itens.md | 4942 | `7a9d20523ede049979e9f46b373045dacdbc64a5df0602926bcb0d691b32fe3f` | gerado | saída (edição do estudante gerada) |
| out/estudante/L6A_estudo.md | 36959 | `a599f9f0160e82d8cdb2ea939898164c2f6382567f80b742644e85bd134fddb9` | gerado | saída (edição do estudante gerada) |
| out/estudante/L6A_gabarito.md | 4946 | `3b7658969f123d84a116512f0804dc7f1a1ed21c1a1ba417d02e414f75672a7a` | gerado | saída (edição do estudante gerada) |
| out/estudante/L6A_itens.md | 3764 | `a002e89404975d2382babb6c36750fde519522ccb45efbf0c95545d9aeef75a5` | gerado | saída (edição do estudante gerada) |
| out/estudante/L6B_estudo.md | 54664 | `454d6962e88296ab8a151ab21df48d20fd6402d0270ce9c7aa98db47350bd603` | gerado | saída (edição do estudante gerada) |
| out/estudante/L6B_gabarito.md | 5347 | `2c50bbe10ad8f183bb2d52e6a794a044711970e56b2ad3a2a522b99cda955733` | gerado | saída (edição do estudante gerada) |
| out/estudante/L6B_itens.md | 4268 | `9045a4fe386d210114f94dab229cf94975c9645fa0a712df6a3e1383c48b7f44` | gerado | saída (edição do estudante gerada) |
| out/estudante/README.md | 2898 | `f42c89e5c243cc930af25aa6aa27f7edb1444b54a099d50b25c7cfae4d176e0f` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-0-P2_folha.md | 6063 | `f69efe607e7b575c246b46eded5ce15d5b6cf1e14ae755bc1bff23087c8bdab5` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-0-P2_gabarito.md | 5889 | `1f3acd3ae9c994ca2ba046b238c8700c16043942ab8bfa9d2793c5b4f981e10a` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-0_folha.md | 19465 | `50d509be3f26a93f5d2fe0d8739dd8e66c9c963ce5c0b88ccd35f1987298baaa` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-0_gabarito.md | 5986 | `780a8f30abd0730cb5ca5945f2fc9456e94af2f0a1cd07ca2dcf947fc1a5f597` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-1_folha.md | 8625 | `e0e21ea32da954f4d20ac9df23937dab412179873d28211876600e938c2b9a38` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-1_gabarito.md | 13014 | `c67591ac09b29dea99723dd6eaa5b7e74411346e5278e1281a8d920bf1aa2d5a` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-2_folha.md | 9658 | `d576cc3fecc6f9973a028f82e303abb65aedd00ad14000cbc263c51423daaa92` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-2_gabarito.md | 9310 | `e298f570eacb7f5a17465ee2a2ac704cdc597e88513c41b8193e79af440387c6` | gerado | saída (edição do estudante gerada) |
| out/estudante_contagem.json | 6142 | `e22b3101580c2c3735d5398d28c7f6f16b6ce75530c180260d02573e43289d4b` | gerado | saída |
| out/estudante_fidelidade.json | 502 | `0c0ae5b09257126f3e5a9098815dc3ba034304408abf6a3be85ab3f4461f12b2` | gerado | saída |
| out/fidelidade_mutacao.json | 1014 | `9091675073402b4c574b790fd23e4bf4cf19aafabaa83457db4a584ba3cb2eef` | gerado | saída |
| out/fidelidade_stdout.txt | 2185 | `75cb132ba04d2a8670bf423ea1db364791c635cb61c2f782d1b0d541710fd145` | gerado | saída |
| out/gen_stdout.txt | 1498 | `4ff18db1e885114760f141ae98ee5af6476ed5741d1260360f3bafee28c4e2a7` | gerado | saída |
| out/mutacao_stdout.txt | 848 | `d1463cedd06c27cb55ded67c8eff056fdc50d1f959b3fcc463e770be449ce6aa` | gerado | saída |
| out/pacote.json | 621744 | `f8c0c131f16dab52b1646b3d302670a3afc498b23ac03a7b34a8ff97520ffa54` | gerado | saída |
| out/pacote_relatorio_2026-10-13_v1_4.md | 140577 | `a33c53529b4ed2a06d083fb61475d7669f6669cf5be01c0d71cdd6a8795785eb` | gerado | saída |
| out/relatorio_stdout.txt | 12 | `d2b709d35b823e9a4c048fce7016d1b4aa473d8c51997e77c017bbc7333060ae` | gerado | saída |
| out/stats.json | 104174 | `7c69e23c88b45509105d5674ab24586005b6e7d98fff5737d6de4de3212fb6e4` | gerado | saída |
| out/sync_check.json | 1931 | `ab32033d7957c0ee57d6a01eeb0ffaf3f33f97d8271d5e6496cfaddcc1cc070f` | gerado | saída |
| out/sync_check.txt | 2243 | `f5f193737b9dbee88ce40544156bd77f031e1d8bb26aa77cec1c9f67433921b1` | gerado | saída |
| out/sync_stdout.txt | 2243 | `f5f193737b9dbee88ce40544156bd77f031e1d8bb26aa77cec1c9f67433921b1` | gerado | saída |
| out/validate.json | 15583 | `7665f8559790a6e2174b56850fbc54e0d05e6a5168bf38ef8abf43b4a31ce6bd` | gerado | saída |
| out/validate_stdout.txt | 11508 | `e1072d0a6704ae03a1fc9e2890dade68caccece10a646f645467947b3804bc2c` | gerado | saída |
| out/varredura_volatil_v14.json | 278 | `fc915993c98ad2a7b85545132dd81ca26041b680d3e958f1b4fc68baf72e8705` | gerado | saída |
| p1.py | 11025 | `5cfc3a55b838d3f02f6b4f95302ba354aa1a036f08fe83d6817a3dc2e2981a5b` | alterado | ativo |
| p2.py | 25680 | `516ecfdba01c83ac46dc7b8dfcb11fecc1d2a236d906deb0b661639aa3427e40` | alterado | ativo |
| peg.py | 4922 | `ee0071445a44c6c043a4e3359299e33aed17ea6da3515aa96f7d656e85115d61` | igual à v1_3 | ativo |
| probe.py | 441 | `f4eb95e47897fb0026e3943ef1aa7951af0d43590292ea4b7fc13be86f71fc7b` | igual à v1_3 | histórico (executável; v1.2/R0/R1) |
| refs.py | 2673 | `e1bd3b24f4e25b91f45272974dd0862fbe2445d8510b58b4aa01c5094419da71` | alterado | ativo |
| registry.py | 897 | `6664fbc7a4bdb9a997a92def4c824c7cf2c1c6a4d31603cd22e77478c7bae78b` | igual à v1_3 | ativo |
| relatorio_R1.py | 19839 | `616bbbcc9ff4f5ee976f9b92fe1e3e40cb35919da9c3386fa495335ff0db45ea` | igual à v1_3 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| relatorio_v1_4.py | 83166 | `c80cd32ebc058266f045bb58109dc9d8cd637884b9cb979a3d41b2bdd4f388a3` | novo | ativo |
| report.py | 15830 | `397ac2117c430da380cfcf7d7ffc758db50192081da398abf04c0daa11092ac9` | igual à v1_3 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| report2.py | 44678 | `92c1fb9c6ac8c727831f16d2db5928bddf3f1f66cee3e6dbb87f35c523c08cc3` | igual à v1_3 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| resid.py | 481 | `3e43ef78e0c82b3927ed5108facf18e5bc47307d6f2a5a0c266075e06d368082` | igual à v1_3 | histórico (executável; v1.2/R0/R1) |
| review.py | 690 | `a1c4f135e564a160e0d09a6347c04c218693fd506e67a6678f9549e7996180ff` | igual à v1_3 | histórico (executável; v1.2/R0/R1) |
| rodar_tudo.sh | 1055 | `b1935431ddc16875bce6cab5efcec6ce11ac6774d019bbebd734bef86de039df` | novo | ativo (runner do pipeline) |
| sync_check.py | 2225 | `9aa9eb1bbd91e682319aaf04d14d82057e62ca1b787b52b831f98902c09b34a2` | igual à v1_3 | ativo |
| texts.py | 422 | `c3ca12b7283710222c8baf681738b3d0e462207a30b81167d48e84be77bb0102` | igual à v1_3 | ativo (módulo auxiliar importado por relatorio_v1_4.py e pelos históricos) |
| validate.py | 38829 | `8a4596fac186e598b50b096dbbcda356968e13c0a68a2504e80c27736111e801` | alterado | ativo |

Total: 94 arquivos listados (32 de código/auxiliares e 62 em `out/`), mais este `MANIFESTO.md` (não tem hash próprio). Código frente à v1_3: 18 iguais, 11 alterados, 3 novos (`conferencias_v14.py`, `relatorio_v1_4.py`, `rodar_tudo.sh`). Manifesto ordenado da edição `out/estudante/` (SHA-256 das linhas "<sha256>  <nome>"): ver o relatório, seção 13.6. `out/estudante/` e `saida/estudante/` são idênticos (diff recursivo); `out/pacote.json` e `saida/pacote/pacote.json` têm o mesmo SHA-256; `out/pacote_relatorio_2026-10-13_v1_4.md` e `saida/pacote/pacote_relatorio_2026-10-13_v1_4.md` também.

## Mudanças frente à v1_3

- Novos: `conferencias_v14.py` (conferências (1) diff do pacote, (2) contrato, (3) edição com reconstrução 43/43 e testes T54-3 a T54-8, (4) não regressão, (5) contagens; 117 conferências), `relatorio_v1_4.py` (relatório completo gerado pelo gerador, N-3), `rodar_tudo.sh` (runner do pipeline, O-2).
- Alterados: `refs.py` (referência da v1.3: `C_V13`, `v13()`), `common.py` (só o comentário do caminho), `build_pacote.py` (nome "Câmara 2026 — pacote F4 (v1.4)"), `p1.py` (`id` de par nos 72 pares GCB, primeira chave), `p2.py` (anexo de notas da D5 só com R3–R4; D4 mantém R2–R4), `estudante_marcas.py` (exceção fechada REALINHA: só espaços antes de `|`, fora da contagem de remoções), `literais.py` (regra do 6B-06 que apaga o parêntese inteiro; regra do rótulo " (GCE, R3–R4)" da D5; duas regras REALINHA do quadro do L1), `estudante_gen.py` (README v1.4; pares com os separadores do canônico e `id`; `nota` sem o rótulo "Nota: "; legendas de lote nos `SIM-*_gabarito.md`), `estudante_fidelidade.py` (parser dos dois formatos de par, `id` exibido, nota sem rótulo, legendas dos SIM, desfazimento do REALINHA, teste de subsequência linear antes do difflib, caminhos relativos no `print`), `validate.py` (v1.4: 112 verificações, 5 novas e 2 ajustadas), `fidelidade_mutacao.py` (11 mutações, uma por classe de mudança da v1.4).
- Fora do diretório (não copiados): `__pycache__/` (não gerado), `pacote_v1_1.json` e `R0/` (lidos do git por `refs.py`).

## Conferência (f): regeração byte a byte numa cópia limpa

Método: `git clone` do repositório (HEAD `c6e3b39`) em pasta nova do scratchpad, mais a sobreposição do que a ocorrência cria fora do git (`regras/pacote_contrato.md` v1.2.2, `saida/pacote/contrato_v1_2_2_2026-10-13.md` e as fontes de `gerador_v1_4/` sem `out/` e sem `MANIFESTO.md`), execução de `rodar_tudo.sh` a partir de outro diretório de trabalho e comparação de `out/` arquivo a arquivo (`filecmp`, byte a byte).

| Cópia | cwd | PYTHONHASHSEED | arquivos em `out/` (original / cópia) | idênticos byte a byte | diferenças de nome |
|---|---|---|---|---|---|
| A | `/` | 1 | 62 / 62 | 62 | nenhuma |
| B | `/usr` | 4242 | 62 / 62 | 62 | nenhuma |

Resultado: **as duas cópias regeram `out/` idêntico ao original**. Inclui `pacote.json` (SHA-256 `f8c0c131f16dab52b1646b3d302670a3afc498b23ac03a7b34a8ff97520ffa54`), os 43 arquivos de `out/estudante/`, o relatório e todos os `*_stdout.txt`.

## Determinismo

O pipeline completo foi executado a partir de `out/` vazio em 3 execuções independentes (o original, mais as duas cópias limpas acima, em pastas e com `PYTHONHASHSEED` diferentes); `out/pacote.json`, `out/estudante/` e o relatório têm os mesmos SHA-256 em todas. Nenhum script lê data ou hora do sistema, nem o `HEAD` do git (o relatório não imprime o HEAD).
