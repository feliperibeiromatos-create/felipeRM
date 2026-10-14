# MANIFESTO — T-67 — gerador v1.6 do pacote e da edição do estudante — 2026-10-14 — gerado por gbq-csc

Origem: cópia de `saida/pacote/gerador_v1_5/` (intacta: `git status` da pasta sem alteração; os 34 arquivos de código e os 71 de `out/` da v1_5 não foram tocados) para `saida/pacote/gerador_v1_6/`, alterada depois; `out/` da v1_5 não foi copiado (é regerado). `conferencias_v15.py` e `relatorio_v1_5.py` não foram trazidos (continuam na v1_5; os da v1.6 são `conferencias_v16.py` e `relatorio_v1_6.py`). Scripts temporários da ocorrência (aplicação das alterações às cópias, geração das conferências e do relatório a partir dos da v1_5, teste do clone) ficaram só no scratchpad; o MANIFESTO é gerado por `manifesto_v1_6.py` (passo 10). Comando de execução (a partir de qualquer pasta; `-B` evita `__pycache__`, `-I` não serve porque bloqueia os imports entre scripts; só `validar_erros.py`, que não importa módulo do gerador, roda com `-I`): `sh saida/pacote/gerador_v1_6/rodar_tudo.sh` (roda o pipeline abaixo) ou `python3 -B saida/pacote/gerador_v1_6/<script>.py`.

## Ordem de execução

`rodar_tudo.sh` apaga e recria `out/` e roda os passos abaixo, na ordem, parando na primeira falha (`set -e`). Cada `out/*_stdout.txt` é a saída-padrão do script, **redirecionada pelo runner** (os scripts não gravam esses arquivos). Quem rodar os scripts à mão deve redirecionar do mesmo modo para obter os mesmos `*_stdout.txt`.

| # | Comando | Redirecionamento da saída-padrão | Arquivos que o próprio script grava em `out/` |
|---|---|---|---|
| 1 | `python3 -B build_pacote.py` | `> out/gen_stdout.txt` | `pacote.json`, `stats.json` |
| 2 | `python3 -B estudante_gen.py` | `>> out/gen_stdout.txt` (acrescenta ao do passo 1) | `estudante/` (43 arquivos), `estudante_contagem.json` |
| 3 | `python3 -B estudante_fidelidade.py` | `> out/fidelidade_stdout.txt` (caminhos impressos relativos à raiz do repositório; sem caminho absoluto) | `estudante_fidelidade.json` |
| 4 | `python3 -B sync_check.py` | `> out/sync_stdout.txt` (conteúdo igual ao de `sync_check.txt`; inclui a E13) | `sync_check.txt`, `sync_check.json` |
| 5 | `python3 -B validate.py` | `> out/validate_stdout.txt` | `validate.json` (118 verificações) |
| 6 | `python3 -B conferencias_v16.py` | `> out/conferencias_stdout.txt` (conteúdo igual ao de `conferencias_v16.txt`) | `conferencias_v16.txt`, `conferencias_v16.json` (155 conferências), `varredura_volatil_v16.json` |
| 7 | `python3 -B fidelidade_mutacao.py` (~2 min: 14 mutações, cada uma com a fidelidade completa) | `> out/mutacao_stdout.txt` | `fidelidade_mutacao.json` (14 mutações, todas detectadas) |
| 8 | `python3 -B validar_erros_teste.py` (T-59, registro) | `> out/validar_erros_stdout.txt` (12 conferências) | `casos_erros/` (8 arquivos fictícios) |
| 9 | `python3 -B relatorio_v1_6.py` | `> out/relatorio_stdout.txt` (uma linha: n.º de linhas) | `pacote_relatorio_2026-10-14_v1_6.md` |
| 10 | `python3 -B manifesto_v1_6.py` | nenhum (a saída-padrão vai ao stderr do runner; um arquivo em `out/` seria listado por este próprio passo) | nenhum em `out/`; grava `MANIFESTO.md` (fora de `out/`) |

Tudo grava em `out/`; a promoção para `saida/pacote/pacote.json`, `saida/estudante/` e `saida/pacote/pacote_relatorio_2026-10-14_v1_6.md` é um passo explícito (cópia) depois de todas as conferências com 0 falhas. Caminhos derivados de `__file__` (raiz do repositório = três níveis acima de `gerador_v1_6/`); as referências v1/v1.1/R0/v1.2/v1.3/v1.4/v1.5 vêm do git por `refs.py` (`git show <commit>:<caminho>`, somente leitura): v1 `5eab2d9`, v1.1 `e97ab1f`, R0 `27e594d`, v1.2 `2684ab1`, v1.3 `9622604`, v1.4 `e9b6402`, **v1.5 `a889100`** (o primeiro commit em que `saida/pacote/pacote.json` tem o SHA-256 `b4bc65c7…`; é a base do diff e da comparação de fontes do relatório). As conferências (2) da v1.6 reconstroem o contrato v1.2.4 (v1.2.3 do git + C-1 a C-5 lidas dos blocos literais de `saida/pacote/T66_decisoes_2026-10-14.md`, seção 6.1); as (6), a regra `importacao_erros.md` v1.2 (bloco D-T59-07 de `T59_decisoes_2026-10-14.md` + E-1 a E-5 + E-6 a E-10 lidas da seção 6.2 de `T66_decisoes`), o exemplo, `.gitignore` (e `git check-ignore`), o validador mantido e seu teste; a (7), a E13 e a consolidação do L1 (SHA-256 `604fa711…`).

## Scripts históricos (O-1, D-T56-05, D-T57-10: opção "marcar")

Não executáveis, mantidos **sem alteração** (idênticos, byte a byte, aos de `gerador_v1_4/` e aos de `gerador_v1_5/`; conferência (4) T57 s3-6) como registro da R0/R1: cada um sai com código 1 e não grava nada no repositório (conferido na v1.4, em 13/10/2026, cwd `/tmp`): `relatorio_R1.py` (falta `out/conferencias_R1.json`), `report.py` (falta `stats.pkl`), `report2.py` (`ValueError`, formato de `stats` mudou), `diff.py` (`TypeError`) e `diff2.py` (`KeyError: legendaMecanismo`). Executáveis e também históricos: `conferencias_R1.py` (118 conferências, 0 falhas, lê R0 e R1 do git; grava `out/conferencias_R1.json` e `out/varredura_volatil.json`, fora do pipeline), `probe.py`, `resid.py` e `review.py`. `texts.py` é módulo auxiliar ativo. `validar_erros.py` e `validar_erros_teste.py` são **registro (T-59)**, congelados com o SHA-256 da T-61 (`19ab9c8b…` e `33132d5a…`); a versão mantida é a de `saida/treino/ferramentas/`, que a T-66 alterou (SHA-256 `220dd559…` e `192581d9…`).

## Arquivos (SHA-256 de cada um)

| Arquivo | Bytes | SHA-256 | Estado frente à v1_5 | Papel |
|---|---|---|---|---|
| banco.py | 3184 | `6d6e975561ae53c54021a64cd8f17a2fba68f945d7f5a9ed83992163e750cfaf` | igual à v1_5 | ativo |
| build_pacote.py | 7995 | `51cd87e568ad2a7c2b30c8ef15fecc2d05254e8bcc31a0aae695fb3eed857ff9` | alterado | ativo |
| common.py | 6187 | `d34744a8cbfcc85dddda51bcd426eef97005af370424eab7eb963a126ee46859` | alterado | ativo |
| conferencia_f_2026-10-14.json | 675 | `9eef708d10a8fe33ee6202db80d4287d29b34964db3c7047b6125899309ab6ce` | novo | registro datado da conferência (f) da produção, 14/10/2026; não é regerado |
| conferencias_R1.py | 31123 | `587a8d4212429b2c4917c669106af4cb4864cd811481de6b473828bc6e6cc92e` | igual à v1_5 | histórico (executável; v1.2/R0/R1; lê do git; se rodado grava out/conferencias_R1.json e out/varredura_volatil.json, que não fazem parte do pipeline) |
| conferencias_v16.py | 83219 | `a46512129bcd14be2dc46443f23d0f8f9fc43e5d5ef41b41073e57723c5853f0` | novo | ativo (conferências (0) a (7) da v1.6: 155; substitui `conferencias_v15.py`, que continua na v1_5) |
| diff.py | 1751 | `59fef679b240aa9e1ae7895813f4dd7be8251ae06a69921d37874ff843376bfb` | igual à v1_5 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| diff2.py | 1547 | `6513c3b66b2b0e09669a8624f77408fe8f4f1ce6f350a391e82558e5262901d0` | igual à v1_5 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| edital_p.py | 1183 | `0f7ed100392cdba1c09e1cf2dce107801c2fe8225920a5d501d6fc42bf89423d` | igual à v1_5 | ativo |
| estudante_fidelidade.py | 25356 | `5c49851edb72493414b7ec57962992cc9c977bc01e0109a41a2fbfbcd428a5a1` | alterado | ativo |
| estudante_gen.py | 14510 | `6d4f6c4b2a6422a5c9a9f891f83d4acb1cdddcba0ee07973e825a0e5113cdaba` | alterado | ativo |
| estudante_marcas.py | 9897 | `41cf6eecc05d9d52c5115a383a4a2e44af56502f04d6d81ea0bfa040999c485f` | igual à v1_5 | ativo |
| f4.py | 2542 | `e0fb812b44b2822c9d5caad8c5018b1b0df5c929e5182368e2434413f3f52727` | igual à v1_5 | ativo |
| fidelidade_mutacao.py | 3935 | `e5e4b7bf4026e309bb40c309c43cee8102134170b478455f1230dba6f1f1c52d` | alterado | ativo |
| gce.py | 5972 | `e007ddaeac3b07f7f47fe7472c1ec6a1d418f731e185f4baaf678e822153212c` | igual à v1_5 | ativo |
| literais.py | 14182 | `93c64cd58bff76ab3afb8a7429cb3ba2b4d8af7353191e015d8949531b08518b` | igual à v1_5 | ativo |
| lotes_tab.txt | 912 | `895e4d50479615c6963fcd35c01d3cd57aa8bad3994dec6c08a1a639517d27a2` | igual à v1_5 | ativo |
| manifesto_v1_6.py | 15208 | `46105133b6896abf7bd80f63dfc2472c3f4bbde1977288673900fa0193456f14` | novo | ativo, passo 10: gera este MANIFESTO inteiro a partir de `out/` (T66 7.2.3; D1-T67-R1) |
| p1.py | 11025 | `5cfc3a55b838d3f02f6b4f95302ba354aa1a036f08fe83d6817a3dc2e2981a5b` | igual à v1_5 | ativo |
| p2.py | 27070 | `2fd6fbc7f2f12550ece27cd1022e701bf2f88f2c71ef9ffd0dbd14e4647913f9` | alterado | ativo |
| peg.py | 4922 | `ee0071445a44c6c043a4e3359299e33aed17ea6da3515aa96f7d656e85115d61` | igual à v1_5 | ativo |
| probe.py | 441 | `f4eb95e47897fb0026e3943ef1aa7951af0d43590292ea4b7fc13be86f71fc7b` | igual à v1_5 | histórico (executável; v1.2/R0/R1) |
| refs.py | 3118 | `b07889518c0581907f3a2f0fd7ce467b9b092f5e7e65ac595cf924dd9d1f92b4` | alterado | ativo |
| registry.py | 897 | `6664fbc7a4bdb9a997a92def4c824c7cf2c1c6a4d31603cd22e77478c7bae78b` | igual à v1_5 | ativo |
| relatorio_R1.py | 19839 | `616bbbcc9ff4f5ee976f9b92fe1e3e40cb35919da9c3386fa495335ff0db45ea` | igual à v1_5 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| relatorio_v1_6.py | 99727 | `0bafb31a3886fafe5193dd6e41673c1137c1b41b2fe5be9fc9b0b299e2018898` | novo | ativo (relatório completo gerado pelo gerador, N-3; a frase de canônicos alterados é derivada por SHA-256 contra `refs.C_V15`, T66_decisoes 7.1; substitui `relatorio_v1_5.py`, que continua na v1_5) |
| report.py | 15830 | `397ac2117c430da380cfcf7d7ffc758db50192081da398abf04c0daa11092ac9` | igual à v1_5 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| report2.py | 44678 | `92c1fb9c6ac8c727831f16d2db5928bddf3f1f66cee3e6dbb87f35c523c08cc3` | igual à v1_5 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| resid.py | 481 | `3e43ef78e0c82b3927ed5108facf18e5bc47307d6f2a5a0c266075e06d368082` | igual à v1_5 | histórico (executável; v1.2/R0/R1) |
| review.py | 690 | `a1c4f135e564a160e0d09a6347c04c218693fd506e67a6678f9549e7996180ff` | igual à v1_5 | histórico (executável; v1.2/R0/R1) |
| rodar_tudo.sh | 1319 | `92d7b0904b9a340de2fb5e534df17404aa9f0b89851385cdd590ff0153372720` | alterado | ativo (runner do pipeline) |
| sync_check.py | 2868 | `b828c4291295034480eda023081d9b399bdfe11398f611172cf21ccc41e4b7d6` | alterado | ativo |
| texts.py | 422 | `c3ca12b7283710222c8baf681738b3d0e462207a30b81167d48e84be77bb0102` | igual à v1_5 | ativo (módulo auxiliar importado por relatorio_v1_6.py e pelos históricos) |
| validar_erros.py | 18500 | `19ab9c8b359e4a59f209ecbca3e29f2ecc16a0dd5fb49b8892538bbe7eb8f33e` | igual à v1_5 | registro (T-59); versão mantida em `saida/treino/ferramentas/` (D-R59-08) — validador do arquivo `camara2026.erros` v1 como foi gerado na T-61; não muda; só biblioteca-padrão, somente leitura; roda com `python3 -I` |
| validar_erros_teste.py | 7993 | `33132d5a9d9aaf7ec4bf645ae57b84eca9c2094abdc70f18d6970465278f0186` | igual à v1_5 | registro (T-59); versão mantida em `saida/treino/ferramentas/` (D-R59-08) — teste do validador como foi gerado na T-61 (passo 8 do pipeline); não muda; grava casos fictícios em `out/casos_erros/` |
| validate.py | 43699 | `fe73a7fdeb3754ff0acf5b6d9424a5da7c34ba32f444947dd08cbea2332ba358` | alterado | ativo |
| out/casos_erros/importados_exportadoEm.json | 71 | `ca039c0b82972681b9902b442e44867d80422f9b29b1c0ba8617e17abd25ad71` | gerado | saída (T-59: caso do teste do validador-registro; dados fictícios) |
| out/casos_erros/importados_sha.json | 134 | `ea47a0919f69bded8a0115ab5d560b39a3deeed0319147e4e84b380261a5d8f7` | gerado | saída (T-59: caso do teste do validador-registro; dados fictícios) |
| out/casos_erros/incoerente_D.json | 1383 | `463a23847f577c0c5f6014bc6400cfed5c1cf41e480462faaab98a2de885ec22` | gerado | saída (T-59: caso do teste do validador-registro; dados fictícios) |
| out/casos_erros/invalido_A_versaoFormato2.json | 1383 | `bae8aa0fc57ac23bd5e425c6b25e2e1c8370ce3921af88351a7be07e30687fcb` | gerado | saída (T-59: caso do teste do validador-registro; dados fictícios) |
| out/casos_erros/invalido_B_campo_ausente_e_tipo.json | 1180 | `25fb6971761e1f39cb65b6bd1a48228bf5e942aa5e764e6ee41429a626a76b75` | gerado | saída (T-59: caso do teste do validador-registro; dados fictícios) |
| out/casos_erros/invalido_C2_formato_errado.json | 1380 | `7a1540e0090f683a06902633167559b82660b066a51e61d94340e667b297eff9` | gerado | saída (T-59: caso do teste do validador-registro; dados fictícios) |
| out/casos_erros/invalido_C_json_truncado.json | 588 | `f3fa562491ffc9597ca41671a149f7bc0f739bdcd966743f05087a4eb15b4588` | gerado | saída (T-59: caso do teste do validador-registro; dados fictícios) |
| out/casos_erros/valido_ids_reais.json | 1594 | `e488b4b0f574724c57c1ebdadb8b5961de35f90080b633013cdbf9891a910cac` | gerado | saída (T-59: caso do teste do validador-registro; dados fictícios) |
| out/conferencias_stdout.txt | 28957 | `b830780de2f6fd06b2c90a320b22d68eb82c3e6f809724574d4dd927207be0f2` | gerado | saída |
| out/conferencias_v16.json | 32430 | `c95f5c7ff26864036a171cca1199c70ccb26f81178c0ee4cfb99a7b9eb3d21bf` | gerado | saída |
| out/conferencias_v16.txt | 28957 | `b830780de2f6fd06b2c90a320b22d68eb82c3e6f809724574d4dd927207be0f2` | gerado | saída |
| out/estudante/BANCO_gabarito.md | 9340 | `f7d9bb470356e98962227bc7d19dbd6de2eff053aa718df002b26d6f2b4cb5ed` | gerado | saída (edição do estudante gerada) |
| out/estudante/BANCO_itens.md | 76551 | `879e1769c76c3bc655510a18a8fd66f49abb6dec52d7e3030adf93132a226c2c` | gerado | saída (edição do estudante gerada) |
| out/estudante/DISCURSIVAS.md | 6694 | `7777c52ca635cdd0e33a525aadd3b86699d333def9bb61816c79b67653f17bd0` | gerado | saída (edição do estudante gerada) |
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
| out/estudante/README.md | 2898 | `f986ec24151cb2d81d95707de4403a92da593da0c0a447ab63dcf59a0fbcc357` | gerado | saída (edição do estudante gerada) |
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
| out/fidelidade_mutacao.json | 1228 | `3562310b292d2f50b454f5361184fa89f08c3fc7f39b3cf14a0d8380755f9ead` | gerado | saída |
| out/fidelidade_stdout.txt | 2185 | `77aebd40fe1b838123d60b55cf2e523155158e4fce3aadc4d85858ad5309d25f` | gerado | saída |
| out/gen_stdout.txt | 1498 | `4ff18db1e885114760f141ae98ee5af6476ed5741d1260360f3bafee28c4e2a7` | gerado | saída |
| out/mutacao_stdout.txt | 1024 | `cfed16cb481de8dca1a951c765c604bac59c1bb03b14193262e9aa7ed752e8c6` | gerado | saída |
| out/pacote.json | 621907 | `ecc284f9055f21046612e5afff7927eb72bf8a2283b7841c2c32c19c172d0a2e` | gerado | saída |
| out/pacote_relatorio_2026-10-14_v1_6.md | 152445 | `6f1846e84fff531915775f2028c9793f8071bb383b9bc43eef00974c8a5bb5d9` | gerado | saída |
| out/relatorio_stdout.txt | 12 | `cd1eef5520c83d13c56bf937415a47a2106c27f4a7615eb6b68ddc641deb2610` | gerado | saída |
| out/stats.json | 104433 | `44cf56ec38359599023507c92e09e250266384ed1842b615a1b71d23d9f8650b` | gerado | saída |
| out/sync_check.json | 1999 | `3439f4ee4614dd5a5f4cc9064cba8a6cac46586497c505350ea732259fa3aff1` | gerado | saída |
| out/sync_check.txt | 2322 | `069d35733c49b35e30ea8fed14b14f15505fddc09bd2c47ebfdc426e2526af81` | gerado | saída |
| out/sync_stdout.txt | 2322 | `069d35733c49b35e30ea8fed14b14f15505fddc09bd2c47ebfdc426e2526af81` | gerado | saída |
| out/validar_erros_stdout.txt | 1578 | `b154f9f9b248ac3f3aecba63a464b1eb70e8524a4969eadf27c5477b3cc813c0` | gerado | saída |
| out/validate.json | 17396 | `79da1f823d6cc1ea405b727768566ce500e34f3b4ba8294960e1c23a09cdb533` | gerado | saída |
| out/validate_stdout.txt | 13069 | `30839636343a1c24e7cb1e4ab4c997fde6b3e58dd520922dd5f2db69326c5c6a` | gerado | saída |
| out/varredura_volatil_v16.json | 278 | `fc915993c98ad2a7b85545132dd81ca26041b680d3e958f1b4fc68baf72e8705` | gerado | saída |

Total: 107 arquivos listados (36 de código/auxiliares e 71 em `out/`), mais este `MANIFESTO.md` (não tem hash próprio). Código frente à v1_5: 22 iguais, 10 alterados, 4 novos (`conferencia_f_2026-10-14.json`, `conferencias_v16.py`, `manifesto_v1_6.py`, `relatorio_v1_6.py`). A edição em `out/estudante/` tem 43 arquivos. Manifesto ordenado da edição (SHA-256 das linhas "<sha256>  <nome>"): ver o relatório, seção 13.2 (v1.5 `656e60e5085f3622` → v1.6 `01af0e342b9a7796`). A tabela acima é a da execução do pipeline cujo `out/` foi promovido. Depois da promoção, `out/estudante/` e `saida/estudante/` são idênticos (diff recursivo); `out/pacote.json` e `saida/pacote/pacote.json` têm o mesmo SHA-256; `out/pacote_relatorio_2026-10-14_v1_6.md` e `saida/pacote/pacote_relatorio_2026-10-14_v1_6.md` também.

## Mudanças frente à v1_5

- Novos: `conferencias_v16.py` (conferências (0) diff v1.5 → v1.6 do pacote e literais da E13, (1) diff acumulado v1.3 → v1.6 e estado da T-64, (2) contrato v1.2.3 → v1.2.4 por C-1 a C-5, (3) edição v1.5 → v1.6 e, acumulado, reconstrução 43/43 e testes T54-1 a T54-8, (4) não regressão, (5) contagens, (6) artefatos da T-59 e da T-66 (regra v1.2 por E-1 a E-10, validador mantido e seu teste), (7) E13; **155 conferências**) e `relatorio_v1_6.py` (relatório completo gerado pelo gerador, N-3, com a frase de canônicos alterados derivada por SHA-256 contra `refs.C_V15` e por classe de fonte, T66_decisoes 7.1, e as asserções de 7.1.4 e da O-5).
- Alterados (só o necessário): `build_pacote.py`, `common.py`, `estudante_fidelidade.py`, `estudante_gen.py`, `fidelidade_mutacao.py`, `p2.py`, `refs.py`, `rodar_tudo.sh`, `sync_check.py`, `validate.py`. Em síntese: `refs.py` (`C_V15`, `v15()`), `common.py` (só o comentário do caminho), `build_pacote.py` (`nome` "Câmara 2026 — pacote F4 (v1.6)"; `geradoEm` continua "2026-10-14"), `p2.py` (a E13 aplicada ao comando da D1 depois da E8, por `apply_errata(…, expect=1)` e asserção de exatamente 1 ocorrência), `sync_check.py` (a E13 confere contra o Adendo 6), `validate.py` (nome esperado; D1 igual à da v1.1 salvo o `comando`; estado da E13; caminho do `p2.py`), `estudante_gen.py` e `estudante_fidelidade.py` (versão v1.6 no README), `fidelidade_mutacao.py` (+1 mutação: o comando da D1 sem a E13; **14 mutações** no total), `rodar_tudo.sh` (nomes dos scripts da v1.6).
- Iguais à v1_5: 22 arquivos de código (os 5 históricos não executáveis, `conferencias_R1.py`, `probe.py`, `resid.py`, `review.py`, `validar_erros.py` e `validar_erros_teste.py` entre eles).
- Desta ocorrência para a v1.6 (T66_decisoes, seção 7): o relatório deixa de trazer frase fixa sobre canônicos alterados; o `MANIFESTO.md` foi **reescrito inteiro** a partir das saídas (as R-1 e R-2 do QA da T-61 estão fechadas no gerador). Pacote: `b4bc65c7…` (v1.5, 621887 bytes) → `ecc284f9055f21046612e5afff7927eb72bf8a2283b7841c2c32c19c172d0a2e` (621907 bytes).
- Fora do diretório (não copiados): `__pycache__/` (não gerado), `out/` da v1_5 (regerado), `MANIFESTO.md` da v1_5, `conferencias_v15.py` e `relatorio_v1_5.py`.

## Conferência (f): regeração byte a byte numa cópia limpa (registro datado da ocorrência de 14/10/2026: clone de `c54ce21` com `gerador_v1_6/` sobreposto; a regeração em clone puro de `569c5dd` está no QA_T67, seção 6)

Método: `git clone` do repositório local (HEAD `c54ce21`) em pasta nova do scratchpad (`s8/clone/` e `s8/clone2/`); o clone só enxerga o que está commitado. Como a T-65 e a T-66 já estão no git (contrato v1.2.4, regra v1.2, `T66_decisoes`, `saida/treino/ferramentas/`, consolidação do L1 com o Adendo 6), a única sobreposição necessária é a pasta nova `saida/pacote/gerador_v1_6/` (sem `out/`, com este `MANIFESTO.md`), ainda não commitada. `saida/pacote/pacote.json` e `saida/estudante/` não foram sobrepostos (ficam na v1.5 do HEAD; a regeração não os lê). Execução de `rodar_tudo.sh` em cada cópia (uma de dentro da própria cópia, outra a partir de `/tmp`) e comparação de `out/` arquivo a arquivo (`filecmp`, byte a byte).

| Cópia | cwd | PYTHONHASHSEED | arquivos em `out/` (original / cópia) | idênticos byte a byte | diferenças de nome |
|---|---|---|---|---|---|
| cópia 1 | `raiz da cópia 1 (s8/clone)` | 1 | 71 / 71 | 71 | nenhuma |
| cópia 2 | `/tmp` | 4242 | 71 / 71 | 71 | nenhuma |

Resultado: **71 de 71 arquivos de `out/` idênticos byte a byte nas duas cópias** (inclui `pacote.json`, `estudante/` com 43 arquivos e o relatório); nenhuma diferença de nome; em ambas, 155 conferências, 118 verificações, 14 mutações detectadas e 12 conferências do teste do registro, 0 falhas. As cópias foram rodadas com `PYTHONHASHSEED` e pastas diferentes das do original.

## Determinismo

O pipeline completo foi executado a partir de `out/` vazio no original (`PYTHONHASHSEED` 7) e nas cópias limpas acima (pastas e `PYTHONHASHSEED` diferentes); `out/pacote.json`, `out/estudante/` e o relatório têm os mesmos SHA-256 em todas. Nenhum script lê data ou hora do sistema, nem o `HEAD` do git (o relatório não imprime o HEAD).
