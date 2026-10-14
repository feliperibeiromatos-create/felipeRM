# MANIFESTO — T-61 — gerador v1.5 do pacote e da edição do estudante — 2026-10-14 — gerado por gbq-csc

Origem: cópia de `saida/pacote/gerador_v1_4/` (intacta: `git status` da pasta sem alteração; SHA-256 e bytes dos 94 arquivos listados no `MANIFESTO.md` dela, 32 de código e 62 em `out/`, conferidos contra ele, 0 divergências; cópia integral guardada no scratchpad antes de qualquer gravação) para `saida/pacote/gerador_v1_5/`, alterada depois. `conferencias_v14.py` e `relatorio_v1_4.py` não foram trazidos (continuam na v1_4; os da v1.5 são `conferencias_v15.py` e `relatorio_v1_5.py`). Scripts temporários da ocorrência (aplicação do contrato, montagem das conferências e do relatório a partir dos da v1_4, geração deste manifesto, teste do clone) ficaram só no scratchpad. Comando de execução (a partir de qualquer pasta; `-B` evita `__pycache__`, `-I` não serve porque bloqueia os imports entre scripts; só `validar_erros.py`, que não importa módulo do gerador, roda com `-I`): `sh saida/pacote/gerador_v1_5/rodar_tudo.sh` (roda o pipeline abaixo) ou `python3 -B saida/pacote/gerador_v1_5/<script>.py`.

## Ordem de execução

`rodar_tudo.sh` apaga e recria `out/` e roda os passos abaixo, na ordem, parando na primeira falha (`set -e`). Cada `out/*_stdout.txt` é a saída-padrão do script, **redirecionada pelo runner** (os scripts não gravam esses arquivos). Quem rodar os scripts à mão deve redirecionar do mesmo modo para obter os mesmos `*_stdout.txt`.

| # | Comando | Redirecionamento da saída-padrão | Arquivos que o próprio script grava em `out/` |
|---|---|---|---|
| 1 | `python3 -B build_pacote.py` | `> out/gen_stdout.txt` | `pacote.json`, `stats.json` |
| 2 | `python3 -B estudante_gen.py` | `>> out/gen_stdout.txt` (acrescenta ao do passo 1) | `estudante/` (43 arquivos), `estudante_contagem.json` |
| 3 | `python3 -B estudante_fidelidade.py` | `> out/fidelidade_stdout.txt` (caminhos impressos relativos à raiz do repositório; sem caminho absoluto) | `estudante_fidelidade.json` |
| 4 | `python3 -B sync_check.py` | `> out/sync_stdout.txt` (conteúdo igual ao de `sync_check.txt`) | `sync_check.txt`, `sync_check.json` |
| 5 | `python3 -B validate.py` | `> out/validate_stdout.txt` | `validate.json` |
| 6 | `python3 -B conferencias_v15.py` | `> out/conferencias_stdout.txt` (conteúdo igual ao de `conferencias_v15.txt`) | `conferencias_v15.txt`, `conferencias_v15.json`, `varredura_volatil_v15.json` |
| 7 | `python3 -B fidelidade_mutacao.py` (~2 min: 11 mutações, cada uma com a fidelidade completa) | `> out/mutacao_stdout.txt` | `fidelidade_mutacao.json` |
| 8 | `python3 -B validar_erros_teste.py` (T-59) | `> out/validar_erros_stdout.txt` | `casos_erros/` (9 arquivos fictícios) |
| 9 | `python3 -B relatorio_v1_5.py` | `> out/relatorio_stdout.txt` (uma linha: n.º de linhas) | `pacote_relatorio_2026-10-14_v1_5.md` |

Tudo grava em `out/`; a promoção para `saida/pacote/pacote.json`, `saida/estudante/` e `saida/pacote/pacote_relatorio_2026-10-14_v1_5.md` é um passo explícito (cópia) depois de todas as conferências com 0 falhas. Caminhos derivados de `__file__` (raiz do repositório = três níveis acima de `gerador_v1_5/`); as referências v1/v1.1/R0/v1.2/v1.3/v1.4 vêm do git por `refs.py` (`git show <commit>:<caminho>`, somente leitura): v1 `5eab2d9`, v1.1 `e97ab1f`, R0 `27e594d`, v1.2 `2684ab1`, v1.3 `9622604`, **v1.4 `e9b6402`**. As conferências (2) da v1.5 leem o contrato v1.2.2 do git (`e9b6402`), o arquivo `regras/pacote_contrato.md` atual (v1.2.3) e `saida/pacote/T59_decisoes_2026-10-14.md`; as conferências (6), `regras/importacao_erros.md`, `.gitignore` (e `git check-ignore`) e `saida/pacote/exemplo_erros_v1.json`.

## Scripts históricos (O-1, D-T56-05, D-T57-10: opção "marcar")

Não executáveis, mantidos **sem alteração** (idênticos, byte a byte, aos de `gerador_v1_4/`; conferência (4) T57 s3-6) como registro da R0/R1: cada um sai com código 1 e não grava nada no repositório (conferido na v1.4, em 13/10/2026, cwd `/tmp`): `relatorio_R1.py` (falta `out/conferencias_R1.json`), `report.py` (falta `stats.pkl`), `report2.py` (`ValueError`, formato de `stats` mudou), `diff.py` (`TypeError`) e `diff2.py` (`KeyError: legendaMecanismo`). Executáveis e também históricos: `conferencias_R1.py` (118 conferências, 0 falhas, lê R0 e R1 do git; grava `out/conferencias_R1.json` e `out/varredura_volatil.json`, fora do pipeline), `probe.py`, `resid.py` e `review.py`. `texts.py` é módulo auxiliar ativo.

## Arquivos (SHA-256 de cada um)

| Arquivo | Bytes | SHA-256 | Estado frente à v1_4 | Papel |
|---|---|---|---|---|
| banco.py | 3184 | `6d6e975561ae53c54021a64cd8f17a2fba68f945d7f5a9ed83992163e750cfaf` | igual à v1_4 | ativo |
| build_pacote.py | 7984 | `0683c0d2cc10a59b929f741f9632469aa8cafb49b2455cd7a9614817284c51e3` | alterado | ativo |
| common.py | 6178 | `2bd544aa84c84158208747327d7d2707997f7475a5cc293391dbbc9eced57704` | alterado | ativo |
| conferencias_R1.py | 31123 | `587a8d4212429b2c4917c669106af4cb4864cd811481de6b473828bc6e6cc92e` | igual à v1_4 | histórico (executável; v1.2/R0/R1; lê do git; se rodado grava out/conferencias_R1.json e out/varredura_volatil.json, que não fazem parte do pipeline) |
| conferencias_v15.py | 72320 | `ce72f3b66560281165ea2d9892bab448fcc842d3ab51004fe1ae86c9bc5bf976` | novo | ativo (conferências (0) a (6) da v1.5; 134) |
| diff.py | 1751 | `59fef679b240aa9e1ae7895813f4dd7be8251ae06a69921d37874ff843376bfb` | igual à v1_4 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| diff2.py | 1547 | `6513c3b66b2b0e09669a8624f77408fe8f4f1ce6f350a391e82558e5262901d0` | igual à v1_4 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| edital_p.py | 1183 | `0f7ed100392cdba1c09e1cf2dce107801c2fe8225920a5d501d6fc42bf89423d` | igual à v1_4 | ativo |
| estudante_fidelidade.py | 25345 | `41a52af98aea9652667fce979e84dcce9e4cf89d3b799b46cad05d9a150b11dd` | alterado | ativo |
| estudante_gen.py | 14499 | `68f7edaa4076946010e9ffc5faa733be2fd9e754cb0414ddde653605e057e921` | alterado | ativo |
| estudante_marcas.py | 9897 | `41cf6eecc05d9d52c5115a383a4a2e44af56502f04d6d81ea0bfa040999c485f` | igual à v1_4 | ativo |
| f4.py | 2542 | `e0fb812b44b2822c9d5caad8c5018b1b0df5c929e5182368e2434413f3f52727` | igual à v1_4 | ativo |
| fidelidade_mutacao.py | 3647 | `9ec19e96dfdf091df033900a7dccb24ace911a200f97959715626dc81f291c11` | alterado | ativo |
| gce.py | 5972 | `e007ddaeac3b07f7f47fe7472c1ec6a1d418f731e185f4baaf678e822153212c` | igual à v1_4 | ativo |
| literais.py | 14182 | `93c64cd58bff76ab3afb8a7429cb3ba2b4d8af7353191e015d8949531b08518b` | igual à v1_4 | ativo |
| lotes_tab.txt | 912 | `895e4d50479615c6963fcd35c01d3cd57aa8bad3994dec6c08a1a639517d27a2` | igual à v1_4 | ativo |
| p1.py | 11025 | `5cfc3a55b838d3f02f6b4f95302ba354aa1a036f08fe83d6817a3dc2e2981a5b` | igual à v1_4 | ativo |
| p2.py | 26268 | `475cc85ca4fe3a31542deb9db294a7537f06225bce0f3f627e0686c1cb040e1e` | alterado | ativo |
| peg.py | 4922 | `ee0071445a44c6c043a4e3359299e33aed17ea6da3515aa96f7d656e85115d61` | igual à v1_4 | ativo |
| probe.py | 441 | `f4eb95e47897fb0026e3943ef1aa7951af0d43590292ea4b7fc13be86f71fc7b` | igual à v1_4 | histórico (executável; v1.2/R0/R1) |
| refs.py | 2850 | `c5be83cb54abb00aab143f7119a91dbeda7e2939771e7ec663a2eaa906bea7bb` | alterado | ativo |
| registry.py | 897 | `6664fbc7a4bdb9a997a92def4c824c7cf2c1c6a4d31603cd22e77478c7bae78b` | igual à v1_4 | ativo |
| relatorio_R1.py | 19839 | `616bbbcc9ff4f5ee976f9b92fe1e3e40cb35919da9c3386fa495335ff0db45ea` | igual à v1_4 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| relatorio_v1_5.py | 94825 | `3b7a6f806579044f20fe85945c7bd0b6eeb6bb806ce63174d2a6714d3be9a851` | novo | ativo (relatório completo gerado pelo gerador, N-3) |
| report.py | 15830 | `397ac2117c430da380cfcf7d7ffc758db50192081da398abf04c0daa11092ac9` | igual à v1_4 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| report2.py | 44678 | `92c1fb9c6ac8c727831f16d2db5928bddf3f1f66cee3e6dbb87f35c523c08cc3` | igual à v1_4 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| resid.py | 481 | `3e43ef78e0c82b3927ed5108facf18e5bc47307d6f2a5a0c266075e06d368082` | igual à v1_4 | histórico (executável; v1.2/R0/R1) |
| review.py | 690 | `a1c4f135e564a160e0d09a6347c04c218693fd506e67a6678f9549e7996180ff` | igual à v1_4 | histórico (executável; v1.2/R0/R1) |
| rodar_tudo.sh | 1120 | `7fcaff01cdbff8cff53baa8828531750e6b1ef9519c8369696a60828b33614d9` | alterado | ativo (runner do pipeline) |
| sync_check.py | 2225 | `9aa9eb1bbd91e682319aaf04d14d82057e62ca1b787b52b831f98902c09b34a2` | igual à v1_4 | ativo |
| texts.py | 422 | `c3ca12b7283710222c8baf681738b3d0e462207a30b81167d48e84be77bb0102` | igual à v1_4 | ativo (módulo auxiliar importado por relatorio_v1_5.py e pelos históricos) |
| validar_erros.py | 18500 | `19ab9c8b359e4a59f209ecbca3e29f2ecc16a0dd5fb49b8892538bbe7eb8f33e` | novo | registro (T-59); versão mantida em `saida/treino/ferramentas/` (D-R59-08) — validador do arquivo `camara2026.erros` v1 como foi gerado na T-61; não muda; só biblioteca-padrão, somente leitura; roda com `python3 -I` |
| validar_erros_teste.py | 7993 | `33132d5a9d9aaf7ec4bf645ae57b84eca9c2094abdc70f18d6970465278f0186` | novo | registro (T-59); versão mantida em `saida/treino/ferramentas/` (D-R59-08) — teste do validador como foi gerado na T-61 (passo 8 do pipeline); não muda; grava casos fictícios em `out/casos_erros/` |
| validate.py | 41864 | `772eb7495b9549db7d9d525bd99034eb4d9ed20cd8422615c1410b0165f633c3` | alterado | ativo |
| out/casos_erros/importados_exportadoEm.json | 71 | `ca039c0b82972681b9902b442e44867d80422f9b29b1c0ba8617e17abd25ad71` | gerado | saída (T-59: caso do teste do validador; dados fictícios) |
| out/casos_erros/importados_sha.json | 134 | `ea47a0919f69bded8a0115ab5d560b39a3deeed0319147e4e84b380261a5d8f7` | gerado | saída (T-59: caso do teste do validador; dados fictícios) |
| out/casos_erros/incoerente_D.json | 1383 | `463a23847f577c0c5f6014bc6400cfed5c1cf41e480462faaab98a2de885ec22` | gerado | saída (T-59: caso do teste do validador; dados fictícios) |
| out/casos_erros/invalido_A_versaoFormato2.json | 1383 | `bae8aa0fc57ac23bd5e425c6b25e2e1c8370ce3921af88351a7be07e30687fcb` | gerado | saída (T-59: caso do teste do validador; dados fictícios) |
| out/casos_erros/invalido_B_campo_ausente_e_tipo.json | 1180 | `25fb6971761e1f39cb65b6bd1a48228bf5e942aa5e764e6ee41429a626a76b75` | gerado | saída (T-59: caso do teste do validador; dados fictícios) |
| out/casos_erros/invalido_C2_formato_errado.json | 1380 | `7a1540e0090f683a06902633167559b82660b066a51e61d94340e667b297eff9` | gerado | saída (T-59: caso do teste do validador; dados fictícios) |
| out/casos_erros/invalido_C_json_truncado.json | 588 | `f3fa562491ffc9597ca41671a149f7bc0f739bdcd966743f05087a4eb15b4588` | gerado | saída (T-59: caso do teste do validador; dados fictícios) |
| out/casos_erros/valido_ids_reais.json | 1594 | `adc474d83b47552a341cca1b7ae3fbdb8eaa47ebe51d2b8a32e38cd9fab24e98` | gerado | saída (T-59: caso do teste do validador; dados fictícios) |
| out/conferencias_stdout.txt | 24222 | `1798b720c96b956dad46e56c819e96e0b42e3e05ca3cec38a9a63fa2d81cb06a` | gerado | saída |
| out/conferencias_v15.json | 27388 | `f9e1b865e258a4b04ef20b7053cfc29a3af9545827b76ad20c7e690b2bdba448` | gerado | saída |
| out/conferencias_v15.txt | 24222 | `1798b720c96b956dad46e56c819e96e0b42e3e05ca3cec38a9a63fa2d81cb06a` | gerado | saída |
| out/estudante/BANCO_gabarito.md | 9340 | `f7d9bb470356e98962227bc7d19dbd6de2eff053aa718df002b26d6f2b4cb5ed` | gerado | saída (edição do estudante gerada) |
| out/estudante/BANCO_itens.md | 76551 | `879e1769c76c3bc655510a18a8fd66f49abb6dec52d7e3030adf93132a226c2c` | gerado | saída (edição do estudante gerada) |
| out/estudante/DISCURSIVAS.md | 6674 | `075b68c83526dab71905bc1370cf939a4d5135c7654d4d4bdc6b5d4374705f9a` | gerado | saída (edição do estudante gerada) |
| out/estudante/DISCURSIVAS_padrao.md | 31915 | `f14dc1c1588c6a47744b466dd2836a60d870bdcd791f53af8e4a48ce52e77c8e` | gerado | saída (edição do estudante gerada) |
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
| out/estudante/README.md | 2898 | `1c1aeaf66b3324310ae139ffd1553c1666ed09d5b9d8b940376a34c68081ab26` | gerado | saída (edição do estudante gerada) |
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
| out/fidelidade_mutacao.json | 1148 | `ece3a3dd8dab30d2c77e2b0d53d2e7cad0b07c169f98c07783c1371280ea8931` | gerado | saída |
| out/fidelidade_stdout.txt | 2185 | `1c0b9fe154b89191aed9e5b56277ff51d80422dbf10dcebd5941118b8d1ff27c` | gerado | saída |
| out/gen_stdout.txt | 1498 | `4ff18db1e885114760f141ae98ee5af6476ed5741d1260360f3bafee28c4e2a7` | gerado | saída |
| out/mutacao_stdout.txt | 958 | `b473bc91b1748f595b1240389cccd9cd70291ca3fbdc185a663faf0ba35e7332` | gerado | saída |
| out/pacote.json | 621887 | `b4bc65c7c5829994856665ae895f9b188be8167d5b78786819ea6cdeb97beef3` | gerado | saída |
| out/pacote_relatorio_2026-10-14_v1_5.md | 148566 | `912f0574deb39f3690c0440532201d10efb7b9de11c9faf99d950a0f2806eb2d` | gerado | saída |
| out/relatorio_stdout.txt | 12 | `b478829a78e5797d140db0310e1b33d25559196517b8b018c163290e32b78e46` | gerado | saída |
| out/stats.json | 104174 | `0797a1f3be5ed54403f70687d5b3fdf05ce8dc3dde380c2b72b82059b5a39b5e` | gerado | saída |
| out/sync_check.json | 1931 | `ab32033d7957c0ee57d6a01eeb0ffaf3f33f97d8271d5e6496cfaddcc1cc070f` | gerado | saída |
| out/sync_check.txt | 2243 | `f5f193737b9dbee88ce40544156bd77f031e1d8bb26aa77cec1c9f67433921b1` | gerado | saída |
| out/sync_stdout.txt | 2243 | `f5f193737b9dbee88ce40544156bd77f031e1d8bb26aa77cec1c9f67433921b1` | gerado | saída |
| out/validar_erros_stdout.txt | 1578 | `b154f9f9b248ac3f3aecba63a464b1eb70e8524a4969eadf27c5477b3cc813c0` | gerado | saída |
| out/validate.json | 16582 | `5ef57c33d5b2d63e4c3420c0b5b6cdb2b5300545e3c3b82dd8c9fe0fe2f1d5e9` | gerado | saída |
| out/validate_stdout.txt | 12341 | `3cc274d7eb86e57ca432507ca859abe629c12cacf671e712e65c3eac3a86684d` | gerado | saída |
| out/varredura_volatil_v15.json | 278 | `fc915993c98ad2a7b85545132dd81ca26041b680d3e958f1b4fc68baf72e8705` | gerado | saída |

Total: 105 arquivos listados (34 de código/auxiliares e 71 em `out/`), mais este `MANIFESTO.md` (não tem hash próprio). Código frente à v1_4: 21 iguais, 9 alterados (a regeração R1 acrescentou `p2.py`), 4 novos (`conferencias_v15.py`, `relatorio_v1_5.py`, `validar_erros.py`, `validar_erros_teste.py`; os dois últimos são agora "registro"). Manifesto ordenado da edição `out/estudante/` (SHA-256 das linhas "<sha256>  <nome>"): ver o relatório, seção 13.2 (v1.4 `562c51398d1e64f8` → v1.5 final `656e60e5085f3622`; primeira passagem `0f97d689316a8cf9`). A tabela acima é a da **regeração R1** (14/10/2026); a da primeira passagem da T-61 está no histórico do git. `out/estudante/` e `saida/estudante/` são idênticos (diff recursivo); `out/pacote.json` e `saida/pacote/pacote.json` têm o mesmo SHA-256; `out/pacote_relatorio_2026-10-14_v1_5.md` e `saida/pacote/pacote_relatorio_2026-10-14_v1_5.md` também.

## Mudanças frente à v1_4

- Novos: `conferencias_v15.py` (conferências (0) diff v1.4 → v1.5 do pacote, (1) diff acumulado v1.3 → v1.5, (2) contrato v1.2.2 → v1.2.3, (3) edição v1.4 → v1.5 e, acumulado, reconstrução 43/43 e testes T54-3 a T54-8, (4) não regressão, (5) contagens, (6) artefatos da T-59; 134 conferências), `relatorio_v1_5.py` (relatório completo gerado pelo gerador, N-3), `validar_erros.py` e `validar_erros_teste.py` (T-59 d: validador do arquivo "Exportar meus erros" e seu teste).
- Alterados (só o necessário): `refs.py` (referência da v1.4: `C_V14`, `v14()`), `common.py` (só o comentário do caminho), `build_pacote.py` (`nome` "Câmara 2026 — pacote F4 (v1.5)" e `geradoEm` "2026-10-14"), `estudante_gen.py` (README v1.5), `estudante_fidelidade.py` (versão esperada no README), `validate.py` (nome e data esperados), `fidelidade_mutacao.py` (só o cabeçalho), `rodar_tudo.sh` (nomes dos scripts da v1.5 e o passo 8).
- **Regeração R1 (T59_T60_reconciliacao seção 5 item 3; D-T64-V15; D1-T64-5 da GCE):** `p2.py` (a R6, antes escrita no código nas linhas 392–393, passa a ser lida de `saida/gce/GCE_Lote3_padroes_GCE.md`: linhas da decisão `R6. …` até a linha em branco, unidas por espaço, sem recuo e sem o rótulo; achado O-4 do QA da gce-cqfp), `validate.py` (D3, D4 e D5 = v1.1 com uma troca cada + estado esperado da GCE; 116 verificações), `conferencias_v15.py` (141 conferências: (0) com 5 diferenças e reconstrução byte a byte por 5 trocas, (1) e (3) com D3, D4, D5 e as 3 linhas de `DISCURSIVAS_padrao.md`, (6) com a regra `importacao_erros.md` v1.1 reconstruída por script e a conferência do validador mantido e da marca "registro" abaixo), `fidelidade_mutacao.py` (13 mutações: +2 sobre as notas da T-64) e `relatorio_v1_5.py` (estado final nas seções 1 a 13 e seção 14 nova). `validar_erros.py` e `validar_erros_teste.py` aqui **não mudam** (SHA-256 `19ab9c8b…` e `33132d5a…`) e ficam marcados "registro (T-59); versão mantida em `saida/treino/ferramentas/` (D-R59-08)"; `report.py` (linha 91, registro da R0/R1) também não muda. `rodar_tudo.sh` não mudou. Pacote: `d6b8a5be…` (primeira passagem) → `b4bc65c7c5829994856665ae895f9b188be8167d5b78786819ea6cdeb97beef3` (621887 bytes; v1.4: 621744).
- Fora do diretório (não copiados): `__pycache__/` (não gerado), `out/` da v1_4 (regerado), `MANIFESTO.md`, `conferencias_v14.py` e `relatorio_v1_4.py`.

## Conferência (f): regeração byte a byte numa cópia limpa (primeira passagem da T-61; histórico)

Método: `git clone` do repositório (HEAD `a4e2c44`) em pasta nova do scratchpad, mais a sobreposição do que a ocorrência cria fora do git (`regras/pacote_contrato.md` v1.2.3, `regras/importacao_erros.md`, `.gitignore`, `saida/pacote/contrato_v1_2_3_2026-10-14.md`, `saida/pacote/exemplo_erros_v1.json` e as fontes de `gerador_v1_5/` sem `out/` e sem `MANIFESTO.md`), execução de `rodar_tudo.sh` a partir de outro diretório de trabalho e comparação de `out/` arquivo a arquivo (`filecmp`, byte a byte).

| Cópia | cwd | PYTHONHASHSEED | arquivos em `out/` (original / cópia) | idênticos byte a byte | diferenças de nome |
|---|---|---|---|---|---|
| A | `/` | 1 | 71 / 71 | 71 | nenhuma |
| B | `/usr` | 4242 | 71 / 71 | 71 | nenhuma |

Resultado: **as duas cópias regeram `out/` idêntico ao original**. Inclui `pacote.json` (SHA-256 `d6b8a5beae074851c1ebb4799aa01e58645e220c6e727d0f51eab9e294678289`), os 43 arquivos de `out/estudante/`, o relatório, os casos do teste do validador e todos os `*_stdout.txt`.

## Conferência (f) da regeração R1: regeração byte a byte em duas cópias limpas

Método (o mesmo): `git clone` do repositório (HEAD `3acbff3`) em duas pastas novas do scratchpad, mais a sobreposição da árvore de trabalho da ocorrência (tudo o que não está no git ou difere dele: `regras/importacao_erros.md` v1.1, `saida/treino/`, as fontes de `gerador_v1_5/` com este `MANIFESTO.md`, `saida/pacote/pacote.json`, `saida/estudante/`, o relatório; sem `.git` e sem `gerador_v1_5/out/`), execução de `rodar_tudo.sh` (as duas cópias em paralelo) a partir de outro diretório de trabalho e comparação de `out/` arquivo a arquivo (`filecmp`, byte a byte).

| Cópia | cwd | PYTHONHASHSEED | arquivos em `out/` (original / cópia) | idênticos byte a byte | diferenças de nome |
|---|---|---|---|---|---|
| A | `/tmp` | 99 | 71 / 71 | 71 | nenhuma |
| B | `/var` | 2026 | 71 / 71 | 71 | nenhuma |

Resultado: **as duas cópias regeram `out/` idêntico ao original (`PYTHONHASHSEED` 7)**, inclusive `pacote.json` (SHA-256 `b4bc65c7c5829994856665ae895f9b188be8167d5b78786819ea6cdeb97beef3`), os 43 arquivos de `out/estudante/`, o relatório (SHA-256 `912f0574deb39f3690c0440532201d10efb7b9de11c9faf99d950a0f2806eb2d`), os casos do teste do validador-registro e todos os `*_stdout.txt`. Nas três execuções: `validate.py` 116 verificações, 0 falhas; `conferencias_v15.py` 141 conferências, 0 falhas; `fidelidade_mutacao.py` 13 mutações, todas detectadas (258 diferenças); `estudante_fidelidade.py` 5793 comparações, 0 diferenças; `sync_check.py` TUDO OK. Promoção (cópia, depois das conferências com 0 falhas): `out/pacote.json` = `saida/pacote/pacote.json`; `out/estudante/` = `saida/estudante/` (diff recursivo vazio); `out/pacote_relatorio_2026-10-14_v1_5.md` = `saida/pacote/pacote_relatorio_2026-10-14_v1_5.md`. `gerador_v1_4/` sem alteração (`git status` vazio).

## Determinismo

O pipeline completo foi executado a partir de `out/` vazio em 3 execuções independentes na primeira passagem e de novo em 3 na regeração R1 (o original, mais as cópias limpas acima, em pastas e com `PYTHONHASHSEED` diferentes: original 7); `out/pacote.json`, `out/estudante/` e o relatório têm os mesmos SHA-256 em todas. Nenhum script lê data ou hora do sistema, nem o `HEAD` do git (o relatório não imprime o HEAD).
