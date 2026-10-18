# MANIFESTO — T-81 — gerador v1.8 do pacote, do pacote do estudante (JSON) e da edição do estudante — 2026-10-17 — gerado por gbq-csc

Origem: cópia de `saida/pacote/gerador_v1_7/` (intacta: `git status` da pasta sem alteração; os 36 arquivos de código e os 71 de `out/` da v1_7 não foram tocados) para `saida/pacote/gerador_v1_8/`, alterada depois (lista fechada da D1, `saida/pacote/T81_D1_escopo_v1_8_2026-10-17.md`, 1.1 e 1.2); `out/` da v1_7 não foi copiado (é regerado). `conferencias_v17.py`, `relatorio_v1_7.py`, `manifesto_v1_7.py` e `conferencia_f_2026-10-14_v1_7.json` não foram trazidos (continuam na v1_7; os da v1.8 são `conferencias_v18.py`, `relatorio_v1_8.py`, `manifesto_v1_8.py` e `conferencia_f_2026-10-17_v1_8.json`). Scripts temporários da ocorrência (aplicação das alterações às cópias, montagem de `conferencias_v18.py` a partir de trechos da v17, aplicação do contrato por programa, shim de execução no Windows) ficaram só no scratchpad; **nenhum deles é necessário para regenerar**: o MANIFESTO é gerado por `manifesto_v1_8.py` (passo 11) e tudo o mais por `rodar_tudo.sh`. Comando de execução (a partir de qualquer pasta; `-B` evita `__pycache__`; `-I` não serve para os scripts do gerador, porque bloqueia os imports entre scripts; só `validar_erros.py`, que não importa módulo do gerador, roda com `-I`): `sh saida/pacote/gerador_v1_8/rodar_tudo.sh` (roda o pipeline abaixo) ou `python3 -B saida/pacote/gerador_v1_8/<script>.py`.

## Ordem de execução

`rodar_tudo.sh` apaga e recria `out/` e roda os passos abaixo, na ordem, parando na primeira falha (`set -e`). Cada `out/*_stdout.txt` é a saída-padrão do script, **redirecionada pelo runner** (os scripts não gravam esses arquivos). Quem rodar os scripts à mão deve redirecionar do mesmo modo para obter os mesmos `*_stdout.txt`. `validate.py` e `conferencias_v18.py` saem com código 1 se houver falha (T-69 (4)), e por isso uma falha de validação para o pipeline no passo 6.

| # | Comando | Redirecionamento da saída-padrão | Arquivos que o próprio script grava em `out/` |
|---|---|---|---|
| 1 | `python3 -B build_pacote.py` | `> out/gen_stdout.txt` | `pacote.json`, `stats.json` |
| 2 | `python3 -B estudante_gen.py` | `>> out/gen_stdout.txt` (acrescenta ao do passo 1) | `estudante/` (34 arquivos), `estudante_contagem.json` |
| 3 | `python3 -B estudante_json.py` | `> out/estudante_json_stdout.txt` | `pacote_estudante.json`, `estudante_json.json` (contagens por regra e por campo, casamentos de R, termos fora da lista) |
| 4 | `python3 -B estudante_fidelidade.py` | `> out/fidelidade_stdout.txt` (caminhos impressos relativos à raiz do repositório; sem caminho absoluto) | `estudante_fidelidade.json` |
| 5 | `python3 -B sync_check.py` | `> out/sync_stdout.txt` (conteúdo igual ao de `sync_check.txt`; inclui a E13) | `sync_check.txt`, `sync_check.json` |
| 6 | `python3 -B validate.py` | `> out/validate_stdout.txt` | `validate.json` (118 verificações) |
| 7 | `python3 -B conferencias_v18.py` | `> out/conferencias_stdout.txt` (conteúdo igual ao de `conferencias_v18.txt`) | `conferencias_v18.txt`, `conferencias_v18.json` (214 conferências), `varredura_volatil_v18.json` |
| 8 | `python3 -B fidelidade_mutacao.py` (~2 min: 14 mutações, cada uma com a fidelidade completa) | `> out/mutacao_stdout.txt` | `fidelidade_mutacao.json` (14 mutações, todas detectadas) |
| 9 | `python3 -B validar_erros_teste.py` (T-59, registro) | `> out/validar_erros_stdout.txt` (12 conferências) | `casos_erros/` (8 arquivos fictícios) |
| 10 | `python3 -B relatorio_v1_8.py` | `> out/relatorio_stdout.txt` (uma linha: n.º de linhas) | `pacote_relatorio_2026-10-17_v1_8.md` |
| 11 | `python3 -B manifesto_v1_8.py` | nenhum (a saída-padrão vai ao stderr do runner; um arquivo em `out/` seria listado por este próprio passo) | nenhum em `out/`; grava `MANIFESTO.md` (fora de `out/`) |

Fora de `out/`, o pipeline grava no repositório apenas o `MANIFESTO.md` desta pasta, no passo 11 (`fidelidade_mutacao.py` e `conferencias_R1.py` usam pastas temporárias fora do repositório; `conferencias_v18.py` e `validar_erros_teste.py` também). Tudo grava em `out/`; a promoção para `saida/pacote/pacote.json`, `saida/pacote/pacote_estudante.json`, `saida/estudante/` e `saida/pacote/pacote_relatorio_2026-10-17_v1_8.md` é um passo explícito (cópia) depois de todas as conferências com 0 falhas (D1, 6.5). Caminhos derivados de `__file__` (raiz do repositório = três níveis acima de `gerador_v1_8/`); as referências v1/v1.1/R0/v1.2/v1.3/v1.4/v1.5/v1.6/v1.7 vêm do git por `refs.py` (`git show <commit>:<caminho>`, somente leitura): v1 `5eab2d9`, v1.1 `e97ab1f`, R0 `27e594d`, v1.2 `2684ab1`, v1.3 `9622604`, v1.4 `e9b6402`, v1.5 `a889100`, v1.6 `569c5dd`, **v1.7 `62ab128`** (o commit da produção da T-71, o primeiro em que `saida/pacote/pacote.json` tem o SHA-256 `f20216c2…`; a edição v1.7 tem o manifesto ordenado `67d2bdf85925a232`; é a base do diff e da comparação de fontes). As conferências (2) da v1.8 reconstroem o contrato v1.2.5 (v1.2.4 do git + C-1 a C-3 lidas dos blocos literais da D1, seção 4); as (8), a regra `importacao_erros.md` v1.2, o exemplo e o validador mantido, o `rodar_tudo.sh`, a lista de arquivos frente à v1_7 e o T-69 (4).

## Scripts históricos (O-1, D-T56-05, D-T57-10: opção "marcar")

Não executáveis, mantidos **sem alteração** (idênticos, byte a byte, aos de `gerador_v1_4/` a `gerador_v1_7/`) como registro da R0/R1: cada um sai com código 1 e não grava nada no repositório: `relatorio_R1.py` (falta `out/conferencias_R1.json`), `report.py` (falta `stats.pkl`), `report2.py` (`ValueError`, formato de `stats` mudou), `diff.py` (`TypeError`) e `diff2.py` (`KeyError: legendaMecanismo`). Executáveis e também históricos: `conferencias_R1.py` (118 conferências, lê R0 e R1 do git; grava `out/conferencias_R1.json` e `out/varredura_volatil.json`, fora do pipeline), `probe.py`, `resid.py` e `review.py`. `texts.py` é módulo auxiliar ativo. `validar_erros.py` e `validar_erros_teste.py` são **registro (T-59)**, congelados com o SHA-256 da T-61 (`19ab9c8b…` e `33132d5a…`); a versão mantida é a de `saida/treino/ferramentas/`, que a T-66 alterou (SHA-256 `220dd559…` e `192581d9…`) e a T-71 e a T-81 mantiveram (T-69 (2) continua BACKLOG).

## Arquivos (SHA-256 de cada um, do conteúdo LF)

| Arquivo | Bytes | SHA-256 | Estado frente à v1_7 | Papel |
|---|---|---|---|---|
| banco.py | 3688 | `754571b7c0c30dfce76d23851b822d5fea16c2552a07383500a50f17f5c5ae97` | alterado | ativo |
| build_pacote.py | 8017 | `8e3547c0e2dfce3f382c48470a52c57f913c9baa7678e91b00d127d252589052` | alterado | ativo |
| common.py | 6205 | `e81bc75dfb4faae7832f5ae8262c5f4b4c3992a249bb8529370112f1f3771848` | alterado | ativo |
| conferencia_f_2026-10-17_v1_8.json | 1553 | `3badf68f4f9a0d188c23f7c6558b67d3b92b8178553b51b9ce58d0e8e9399d02` | novo | registro datado da conferência (f) da produção da T-81, 17/10/2026; não é regerado |
| conferencias_R1.py | 31123 | `587a8d4212429b2c4917c669106af4cb4864cd811481de6b473828bc6e6cc92e` | igual à v1_7 | histórico (executável; v1.2/R0/R1; lê do git; se rodado grava out/conferencias_R1.json e out/varredura_volatil.json, que não fazem parte do pipeline) |
| conferencias_v18.py | 107983 | `0b41b1cf8d02e148de32b7480a84ea0f7c28138b52f58b353c936a72b4e357e1` | novo | ativo (conferências (0) a (9) da v1.8: 214; substitui `conferencias_v17.py`, que continua na v1_7) |
| diff.py | 1751 | `59fef679b240aa9e1ae7895813f4dd7be8251ae06a69921d37874ff843376bfb` | igual à v1_7 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| diff2.py | 1547 | `6513c3b66b2b0e09669a8624f77408fe8f4f1ce6f350a391e82558e5262901d0` | igual à v1_7 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| edital_p.py | 1183 | `0f7ed100392cdba1c09e1cf2dce107801c2fe8225920a5d501d6fc42bf89423d` | igual à v1_7 | ativo |
| estudante_fidelidade.py | 26847 | `13b707b4b5ac41ecc431e6ad67703d32a5af1abc08521a1d135ec9c81f3b695a` | alterado | ativo |
| estudante_gen.py | 17343 | `12f50cf57a10e812954009aa372cb757aafa9f3e878e0dcf5476f5cb1ed49120` | alterado | ativo |
| estudante_json.py | 17361 | `4fbcb571ca183d2be786374d5b2221e211ee1e81c20fcecfc4480e2e9a2610b9` | novo | ativo, passo 3: gera `out/pacote_estudante.json` (v1.8-E) a partir de `out/pacote.json`, só por deleção (mais CAIXA, REALINHA e a fusão 1-C/4-C/5-C), com as asserções (a) a (f) de 6.1; sai com código 1 se alguma falhar |
| estudante_marcas.py | 9897 | `41cf6eecc05d9d52c5115a383a4a2e44af56502f04d6d81ea0bfa040999c485f` | igual à v1_7 | ativo |
| f4.py | 2542 | `e0fb812b44b2822c9d5caad8c5018b1b0df5c929e5182368e2434413f3f52727` | igual à v1_7 | ativo |
| fidelidade_mutacao.py | 3935 | `e5e4b7bf4026e309bb40c309c43cee8102134170b478455f1230dba6f1f1c52d` | igual à v1_7 | ativo |
| gce.py | 5972 | `e007ddaeac3b07f7f47fe7472c1ec6a1d418f731e185f4baaf678e822153212c` | igual à v1_7 | ativo |
| literais.py | 14182 | `93c64cd58bff76ab3afb8a7429cb3ba2b4d8af7353191e015d8949531b08518b` | igual à v1_7 | ativo |
| lotes_tab.txt | 912 | `895e4d50479615c6963fcd35c01d3cd57aa8bad3994dec6c08a1a639517d27a2` | igual à v1_7 | ativo |
| manifesto_v1_8.py | 18423 | `0c8c61f097bc749a7acaa782bcf9ef5755e8222fb970686ffac8f8b79e825030` | novo | ativo, passo 11: gera este MANIFESTO inteiro a partir de `out/` (T66 7.2.3; D1-T67-R1; D-T71-04); substitui `manifesto_v1_7.py`, que continua na v1_7 |
| marcas_processo.py | 8200 | `7ee30de455a5c0332aca1dae2148d7670eb86bac08294f0c61a80da4484cc140` | novo | ativo: a varredura R (seção 2.3 da D1) e as listas fechadas X (conteúdo) e Y (dúvida), transcritas da D1; usado por `estudante_json.py` e `conferencias_v18.py` |
| p1.py | 11025 | `5cfc3a55b838d3f02f6b4f95302ba354aa1a036f08fe83d6817a3dc2e2981a5b` | igual à v1_7 | ativo |
| p2.py | 27070 | `2fd6fbc7f2f12550ece27cd1022e701bf2f88f2c71ef9ffd0dbd14e4647913f9` | igual à v1_7 | ativo |
| peg.py | 4922 | `ee0071445a44c6c043a4e3359299e33aed17ea6da3515aa96f7d656e85115d61` | igual à v1_7 | ativo |
| probe.py | 441 | `f4eb95e47897fb0026e3943ef1aa7951af0d43590292ea4b7fc13be86f71fc7b` | igual à v1_7 | histórico (executável; v1.2/R0/R1) |
| refs.py | 3637 | `960cc05f2bb56621cdf38ad86f35b7ebd5b545807cf447d43be9a136bca10cc2` | alterado | ativo |
| registry.py | 897 | `6664fbc7a4bdb9a997a92def4c824c7cf2c1c6a4d31603cd22e77478c7bae78b` | igual à v1_7 | ativo |
| relatorio_R1.py | 19839 | `616bbbcc9ff4f5ee976f9b92fe1e3e40cb35919da9c3386fa495335ff0db45ea` | igual à v1_7 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| relatorio_v1_8.py | 25065 | `8f72f40ebc38b6376da12aa66db54a180aa3e2545de04bda967bfb50fe6c0d7c` | novo | ativo (relatório gerado pelo gerador com o conteúdo mínimo da seção 6.6 da D1 da T-81; substitui `relatorio_v1_7.py`, que continua na v1_7) |
| report.py | 15830 | `397ac2117c430da380cfcf7d7ffc758db50192081da398abf04c0daa11092ac9` | igual à v1_7 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| report2.py | 44678 | `92c1fb9c6ac8c727831f16d2db5928bddf3f1f66cee3e6dbb87f35c523c08cc3` | igual à v1_7 | não executável; registro da R0/R1 (sai com código 1, sem gravar nada) |
| resid.py | 481 | `3e43ef78e0c82b3927ed5108facf18e5bc47307d6f2a5a0c266075e06d368082` | igual à v1_7 | histórico (executável; v1.2/R0/R1) |
| review.py | 690 | `a1c4f135e564a160e0d09a6347c04c218693fd506e67a6678f9549e7996180ff` | igual à v1_7 | histórico (executável; v1.2/R0/R1) |
| rodar_tudo.sh | 1509 | `3d0a0bb15804bb76a580ca8fc2a738b82e208d37b0c3dd3359971dd3e2fe5b72` | alterado | ativo (runner do pipeline) |
| sync_check.py | 2868 | `b828c4291295034480eda023081d9b399bdfe11398f611172cf21ccc41e4b7d6` | igual à v1_7 | ativo |
| texts.py | 422 | `c3ca12b7283710222c8baf681738b3d0e462207a30b81167d48e84be77bb0102` | igual à v1_7 | ativo (módulo auxiliar importado por relatorio_v1_8.py e pelos históricos) |
| validar_erros.py | 18500 | `19ab9c8b359e4a59f209ecbca3e29f2ecc16a0dd5fb49b8892538bbe7eb8f33e` | igual à v1_7 | registro (T-59); versão mantida em `saida/treino/ferramentas/` (D-R59-08) — validador do arquivo `camara2026.erros` v1 como foi gerado na T-61; não muda; só biblioteca-padrão, somente leitura; roda com `python3 -I` |
| validar_erros_teste.py | 7993 | `33132d5a9d9aaf7ec4bf645ae57b84eca9c2094abdc70f18d6970465278f0186` | igual à v1_7 | registro (T-59); versão mantida em `saida/treino/ferramentas/` (D-R59-08) — teste do validador como foi gerado na T-61 (passo 8 do pipeline); não muda; grava casos fictícios em `out/casos_erros/` |
| validate.py | 44115 | `7cde528368ee261693addfb8642ba3deac40fa5db36177eabdb27d493bb795f5` | alterado | ativo |
| out/casos_erros/importados_exportadoEm.json | 71 | `ca039c0b82972681b9902b442e44867d80422f9b29b1c0ba8617e17abd25ad71` | gerado | saída (T-59: caso do teste do validador-registro; dados fictícios) |
| out/casos_erros/importados_sha.json | 134 | `7c2b3afd60182ce1c3ae36d744272baac4b1d8e2cc108d3849fdc06980fb7ceb` | gerado | saída (T-59: caso do teste do validador-registro; dados fictícios) |
| out/casos_erros/incoerente_D.json | 1383 | `463a23847f577c0c5f6014bc6400cfed5c1cf41e480462faaab98a2de885ec22` | gerado | saída (T-59: caso do teste do validador-registro; dados fictícios) |
| out/casos_erros/invalido_A_versaoFormato2.json | 1383 | `bae8aa0fc57ac23bd5e425c6b25e2e1c8370ce3921af88351a7be07e30687fcb` | gerado | saída (T-59: caso do teste do validador-registro; dados fictícios) |
| out/casos_erros/invalido_B_campo_ausente_e_tipo.json | 1180 | `25fb6971761e1f39cb65b6bd1a48228bf5e942aa5e764e6ee41429a626a76b75` | gerado | saída (T-59: caso do teste do validador-registro; dados fictícios) |
| out/casos_erros/invalido_C2_formato_errado.json | 1380 | `7a1540e0090f683a06902633167559b82660b066a51e61d94340e667b297eff9` | gerado | saída (T-59: caso do teste do validador-registro; dados fictícios) |
| out/casos_erros/invalido_C_json_truncado.json | 588 | `f3fa562491ffc9597ca41671a149f7bc0f739bdcd966743f05087a4eb15b4588` | gerado | saída (T-59: caso do teste do validador-registro; dados fictícios) |
| out/casos_erros/valido_ids_reais.json | 1594 | `90b3a20ce30178a759adf18d0f1a43d27fb0a1f7a693c779b49785c932517083` | gerado | saída (T-59: caso do teste do validador-registro; dados fictícios) |
| out/conferencias_stdout.txt | 38412 | `5d962d834a062a99403640ea2694750b54ba6e6abcd1ef96ef1500e087cfb035` | gerado | saída |
| out/conferencias_v18.json | 43134 | `1630f6806586f9bf12f2f1f3c382258ca0861c1933ea39bd8aa2c09fcec1399b` | gerado | saída |
| out/conferencias_v18.txt | 38412 | `5d962d834a062a99403640ea2694750b54ba6e6abcd1ef96ef1500e087cfb035` | gerado | saída |
| out/estudante/BANCO_gabarito.md | 9340 | `f7d9bb470356e98962227bc7d19dbd6de2eff053aa718df002b26d6f2b4cb5ed` | gerado | saída (edição do estudante gerada) |
| out/estudante/BANCO_itens.md | 76551 | `879e1769c76c3bc655510a18a8fd66f49abb6dec52d7e3030adf93132a226c2c` | gerado | saída (edição do estudante gerada) |
| out/estudante/DISCURSIVAS.md | 6694 | `7777c52ca635cdd0e33a525aadd3b86699d333def9bb61816c79b67653f17bd0` | gerado | saída (edição do estudante gerada) |
| out/estudante/DISCURSIVAS_padrao.md | 31915 | `f14dc1c1588c6a47744b466dd2836a60d870bdcd791f53af8e4a48ce52e77c8e` | gerado | saída (edição do estudante gerada) |
| out/estudante/L1_estudo.md | 34999 | `146708b5eb002d2a2a450b65e857ce2cf0c0bbaa29385be2003b8fdb1af147ec` | gerado | saída (edição do estudante gerada) |
| out/estudante/L1_gabarito.md | 6702 | `1f4dcd4b0b20aef62061e1dbee6e7a9584cd19f907012eb534b30b1b78576054` | gerado | saída (edição do estudante gerada) |
| out/estudante/L1_itens.md | 7448 | `337c49ede363d92c6a41bb367e3a2ce6f1f15105909260ae01efe9a1df9a59c3` | gerado | saída (edição do estudante gerada) |
| out/estudante/L2_estudo.md | 33400 | `d4e49cf68dd872e67db9cd0a63875e3ae8a9aac95ca882fb79f098a51772f143` | gerado | saída (edição do estudante gerada) |
| out/estudante/L2_gabarito.md | 6508 | `01b60a5e5ac6239e303419e4ca6615271a5dab410cde7484e94f264cf0ed366b` | gerado | saída (edição do estudante gerada) |
| out/estudante/L2_itens.md | 7391 | `a4ddb9ff0dfbf1e9487ccb93caa45406c2cc290c7f3b98b367d7160aad46ed66` | gerado | saída (edição do estudante gerada) |
| out/estudante/L3_estudo.md | 40424 | `3d226e76971a7e67f64feed0e8d8a10cdd695253f28fc58e9b734c9e505cefd3` | gerado | saída (edição do estudante gerada) |
| out/estudante/L3_gabarito.md | 6481 | `1cbc0474f03eaaede62a63e281b554f93ff5de6675df6480f0dc21d4e995b3ee` | gerado | saída (edição do estudante gerada) |
| out/estudante/L3_itens.md | 7594 | `5f340894de388b976ced1c17c67c34d80b74bba0c0aa3940aa71005e6ab27845` | gerado | saída (edição do estudante gerada) |
| out/estudante/L4_estudo.md | 49282 | `f9ea6165087e2bc3e54540b5515b6f987df9eb21d0ebe85a5f96a31ef774f1ed` | gerado | saída (edição do estudante gerada) |
| out/estudante/L4_gabarito.md | 12003 | `a5f570372ccae8253e906a89ca051d104d0fd0f2d52b810db7e2bee146d91025` | gerado | saída (edição do estudante gerada) |
| out/estudante/L4_itens.md | 6761 | `6bac01242ecd239589d5098c326d06a3cf08fe02f0fb099608a23ab7859751d2` | gerado | saída (edição do estudante gerada) |
| out/estudante/L5_estudo.md | 31713 | `ecf286055639ae0ed0f510f87ce687ff4c6133e313b57c0f082cc851d0fa4859` | gerado | saída (edição do estudante gerada) |
| out/estudante/L5_gabarito.md | 9758 | `61d9f3c0a8fce6ff44575e18e8a12bb215a8048654fa4ac4cb33b06c1acbb1c0` | gerado | saída (edição do estudante gerada) |
| out/estudante/L5_itens.md | 7098 | `a51ca726cd3331cc452bbf3d6c26b36a67204f87e562b5483e37cf8df3564678` | gerado | saída (edição do estudante gerada) |
| out/estudante/L6A_estudo.md | 36959 | `a599f9f0160e82d8cdb2ea939898164c2f6382567f80b742644e85bd134fddb9` | gerado | saída (edição do estudante gerada) |
| out/estudante/L6A_gabarito.md | 4946 | `3b7658969f123d84a116512f0804dc7f1a1ed21c1a1ba417d02e414f75672a7a` | gerado | saída (edição do estudante gerada) |
| out/estudante/L6A_itens.md | 3764 | `a002e89404975d2382babb6c36750fde519522ccb45efbf0c95545d9aeef75a5` | gerado | saída (edição do estudante gerada) |
| out/estudante/L6B_estudo.md | 54664 | `454d6962e88296ab8a151ab21df48d20fd6402d0270ce9c7aa98db47350bd603` | gerado | saída (edição do estudante gerada) |
| out/estudante/L6B_gabarito.md | 5347 | `2c50bbe10ad8f183bb2d52e6a794a044711970e56b2ad3a2a522b99cda955733` | gerado | saída (edição do estudante gerada) |
| out/estudante/L6B_itens.md | 4268 | `9045a4fe386d210114f94dab229cf94975c9645fa0a712df6a3e1383c48b7f44` | gerado | saída (edição do estudante gerada) |
| out/estudante/README.md | 2334 | `fcc54c60fd485852e79c1bf3708f63f7a03dc3198c29e10e1e37b2f7e8fec541` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-0-P2_folha.md | 6063 | `f69efe607e7b575c246b46eded5ce15d5b6cf1e14ae755bc1bff23087c8bdab5` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-0-P2_gabarito.md | 5889 | `1f3acd3ae9c994ca2ba046b238c8700c16043942ab8bfa9d2793c5b4f981e10a` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-0_folha.md | 19465 | `50d509be3f26a93f5d2fe0d8739dd8e66c9c963ce5c0b88ccd35f1987298baaa` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-0_gabarito.md | 5986 | `780a8f30abd0730cb5ca5945f2fc9456e94af2f0a1cd07ca2dcf947fc1a5f597` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-1_folha.md | 8625 | `e0e21ea32da954f4d20ac9df23937dab412179873d28211876600e938c2b9a38` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-1_gabarito.md | 13014 | `c67591ac09b29dea99723dd6eaa5b7e74411346e5278e1281a8d920bf1aa2d5a` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-2_folha.md | 9658 | `d576cc3fecc6f9973a028f82e303abb65aedd00ad14000cbc263c51423daaa92` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-2_gabarito.md | 9310 | `e298f570eacb7f5a17465ee2a2ac704cdc597e88513c41b8193e79af440387c6` | gerado | saída (edição do estudante gerada) |
| out/estudante_contagem.json | 5956 | `c83b34054c8c6387c3ab3cec0bf50f0a674b9c889cc8bcb522120dd6fac8992f` | gerado | saída |
| out/estudante_fidelidade.json | 502 | `570685426734c50900b9b3aaecb9ce79031730b0ae34dbf3a85d4d6d00fbb6a9` | gerado | saída |
| out/estudante_json.json | 8811 | `cec5a6cceb4b7ea03c464586963ad2ba0178ec915588d5810c40dca7a6b2586e` | gerado | saída |
| out/estudante_json_stdout.txt | 1668 | `10962c655734b615df8068322d12e18dc4c09d2f38df2c9b4cce9dc901ba0d51` | gerado | saída |
| out/fidelidade_mutacao.json | 1228 | `3562310b292d2f50b454f5361184fa89f08c3fc7f39b3cf14a0d8380755f9ead` | gerado | saída |
| out/fidelidade_stdout.txt | 2185 | `abdca607a2d1bec2db9ca4d47003a779f6e5d7b6b73c2e82b3aa079ecd4a6128` | gerado | saída |
| out/gen_stdout.txt | 1498 | `eb23cb020d6ca3720686238976a0207e919c911d4732508c3cf7fba365e6474a` | gerado | saída |
| out/mutacao_stdout.txt | 1024 | `cfed16cb481de8dca1a951c765c604bac59c1bb03b14193262e9aa7ed752e8c6` | gerado | saída |
| out/pacote.json | 621907 | `09d4a457612781275659a3f7fbfd3a182f20fd9d4003e5ba38007d0c26c7a9c0` | gerado | saída |
| out/pacote_estudante.json | 602815 | `851e2370a9f5e9c8e5db725ff84777f70c12f81044983d339434ac7504e04c3e` | gerado | saída |
| out/pacote_relatorio_2026-10-17_v1_8.md | 18888 | `c2b7bbd45c35989270957eb0e0ffb0b17754f36cb4ffa074d50d34b9472dba3a` | gerado | saída |
| out/relatorio_stdout.txt | 4 | `d5c6c5db0511989f8b2db87038d1fc6952a2f828e46aef7f3836d4a5d457b775` | gerado | saída |
| out/stats.json | 104433 | `44cf56ec38359599023507c92e09e250266384ed1842b615a1b71d23d9f8650b` | gerado | saída |
| out/sync_check.json | 1999 | `3439f4ee4614dd5a5f4cc9064cba8a6cac46586497c505350ea732259fa3aff1` | gerado | saída |
| out/sync_check.txt | 2322 | `069d35733c49b35e30ea8fed14b14f15505fddc09bd2c47ebfdc426e2526af81` | gerado | saída |
| out/sync_stdout.txt | 2322 | `069d35733c49b35e30ea8fed14b14f15505fddc09bd2c47ebfdc426e2526af81` | gerado | saída |
| out/validar_erros_stdout.txt | 1578 | `a96eb28566ac456533bf65c5345e5f17422d6462619b7c90df97ddac36b29d2d` | gerado | saída |
| out/validate.json | 17467 | `d3948df4c98b7106ebf2961159a0125e86f4254a602bc840051a1cb913523099` | gerado | saída |
| out/validate_stdout.txt | 13140 | `d014a4aa1b706fff97fba046c96f1823829a8dab57051c1d349d711bfa8db544` | gerado | saída |
| out/varredura_volatil_v18.json | 278 | `fc915993c98ad2a7b85545132dd81ca26041b680d3e958f1b4fc68baf72e8705` | gerado | saída |

Total: 103 arquivos listados (38 de código/auxiliares e 65 em `out/`), mais este `MANIFESTO.md` (não tem hash próprio). Código frente à v1_7: 24 iguais, 8 alterados, 6 novos (`conferencia_f_2026-10-17_v1_8.json`, `conferencias_v18.py`, `estudante_json.py`, `manifesto_v1_8.py`, `marcas_processo.py`, `relatorio_v1_8.py`). A edição em `out/estudante/` tem 34 arquivos (34: 1-C, 4-C e 5-C fundidos nos Lotes 1, 4 e 5). Manifesto ordenado da edição (SHA-256 das linhas "<sha256>  <nome>"): v1.7 `67d2bdf85925a232` → v1.8 `0b7391fa01784889`. A tabela acima é a da execução do pipeline cujo `out/` foi promovido. Depois da promoção, `out/estudante/` e `saida/estudante/` são idênticos (diff recursivo); `out/pacote.json` e `saida/pacote/pacote.json`, `out/pacote_estudante.json` e `saida/pacote/pacote_estudante.json`, e `out/pacote_relatorio_2026-10-17_v1_8.md` e `saida/pacote/pacote_relatorio_2026-10-17_v1_8.md` têm o mesmo SHA-256.

## Mudanças frente à v1_7

- Novos: `conferencias_v18.py` (conferências (0) diff v1.7 → v1.8 do pacote, só `$.nome` e `$.geradoEm`, (1) histórico v1.6 → v1.7, v1.5 → v1.6 e o diff acumulado v1.3 → v1.8, (2) contrato v1.2.4 → v1.2.5 por C-1 a C-3, (3) edição v1.7 → v1.8 (9 retirados, 8 alterados, 26 idênticos, reconstrução da fusão), (4) identidade `pacote.json` × `pacote_estudante.json`, (5) JSON × edição v1.7, (6) JSON × edição v1.8, (7) varredura R no JSON e na edição, (8) não regressão (T-59 e T-66, lista de arquivos, `rodar_tudo.sh`, T-69 (4), varreduras da seção 3.5, CAIXA, REUNIÃO, contagens), (9) mutações M1 a M8 do JSON; **214 conferências**), `estudante_json.py`, `marcas_processo.py`, `relatorio_v1_8.py`, `manifesto_v1_8.py` (passo 11) e `conferencia_f_2026-10-17_v1_8.json` (registro datado da conferência (f)).
- Alterados (só o necessário, lista fechada da D1, 1.2): `banco.py`, `build_pacote.py`, `common.py`, `estudante_fidelidade.py`, `estudante_gen.py`, `refs.py`, `rodar_tudo.sh`, `validate.py`. Em síntese: `build_pacote.py` (`nome` "Câmara 2026 — pacote F4 (v1.8)"; `geradoEm` "2026-10-17"), `common.py` (só o comentário do caminho), `refs.py` (`C_V17`, `v17()`), `validate.py` (`nome` e `geradoEm` esperados, caminho do `p2.py`, e, como última instrução, `sys.exit(1 if fails else 0)` — T-69 (4); as 118 verificações continuam), `estudante_gen.py` e `estudante_fidelidade.py` (fusão 1-C/4-C/5-C e versão v1.8; escopo das deleções = nome de arquivo de origem da v1.7) e `rodar_tudo.sh` (os 11 passos de 6.3, cabeçalho no padrão R-1 a R-6 da T-71). `fidelidade_mutacao.py` não muda (14 mutações; nenhuma tinha como alvo arquivo L1C_, L4C_ ou L5C_).
- Iguais à v1_7: 24 arquivos de código (os 5 históricos não executáveis, `conferencias_R1.py`, `probe.py`, `resid.py`, `review.py`, `estudante_marcas.py`, `literais.py`, `p1.py`, `p2.py`, `peg.py`, `gce.py`, `banco.py`, `edital_p.py`, `f4.py`, `registry.py`, `sync_check.py`, `texts.py`, `lotes_tab.txt`, `fidelidade_mutacao.py`, `validar_erros.py` e `validar_erros_teste.py`).
- Desta ocorrência: o pacote v1.8 é a v1.7 com só `$.nome` e `$.geradoEm` trocados (SHA-256 `09d4a457612781275659a3f7fbfd3a182f20fd9d4003e5ba38007d0c26c7a9c0`, 621907 bytes; v1.7: `f20216c2…`, 621907 bytes); o `pacote_estudante.json` v1.8-E (SHA-256 `851e2370a9f5e9c8e5db725ff84777f70c12f81044983d339434ac7504e04c3e`, 602815 bytes) é novo; a edição do estudante perde os 9 arquivos dos complementos e muda 8 (README, L1_estudo, L1_itens, L1_gabarito, L4_itens, L4_gabarito, L5_itens, L5_gabarito); o `MANIFESTO.md` é gerado só pelo passo 11 (D-T71-04), nunca à mão.
- Fora do diretório (não copiados): `__pycache__/` (não gerado), `out/` da v1_7 (regerado), `MANIFESTO.md` da v1_7, `conferencias_v17.py`, `relatorio_v1_7.py`, `manifesto_v1_7.py` e `conferencia_f_2026-10-14_v1_7.json`.

## Conferência (f): regeração byte a byte em cópias limpas (registro datado da ocorrência de 17/10/2026: clone de `73e9d49` com `gerador_v1_8/` sobreposto)

Método: `git clone` do repositório local (HEAD `73e9d49`) em pasta nova do scratchpad (uma rodada a partir de /tmp); o clone só enxerga o que está commitado. Sobrepõe-se só o que ainda não está no git: `saida/pacote/gerador_v1_8/` (sem `out/`, com este `MANIFESTO.md` e o registro datado desta conferência), `regras/pacote_contrato.md` (v1.2.5), `saida/pacote/contrato_v1_2_5_2026-10-17.md` e a D1. `saida/pacote/pacote.json`, `saida/pacote/pacote_estudante.json` e `saida/estudante/` não são sobrepostos (a regeração não os lê). Execução de `rodar_tudo.sh` em cada cópia (uma de dentro da própria cópia, outra a partir de /tmp, `PYTHONHASHSEED` e pastas diferentes das do original) e comparação de `out/` arquivo a arquivo (`filecmp`, byte a byte) e do `MANIFESTO.md` regerado (passo 11) com o desta pasta.

| Cópia | cwd | PYTHONHASHSEED | arquivos em `out/` (original / cópia) | idênticos byte a byte | diferenças de nome |
|---|---|---|---|---|---|
| cópia 1 | `raiz da cópia 1 (scratchpad/cf/cA)` | 7 | 65 / 65 | 65 | nenhuma |
| cópia 2 | `/tmp` | 4242 | 65 / 65 | 65 | nenhuma |

Resultado: **65 de 65 arquivos de `out/` idênticos byte a byte nas duas cópias** (inclui `pacote.json`, `pacote_estudante.json`, `estudante/` com 34 arquivos e o relatório); nenhuma diferença de nome; o `MANIFESTO.md` regerado pelo passo 11 em cada cópia é igual, byte a byte, ao desta pasta na primeira passagem (com o registro provisório); em ambas, 214 conferências, 118 verificações, 14 mutações da fidelidade detectadas, 8 mutações do JSON detectadas e 12 conferências do teste do registro, 0 falhas. As cópias são clones limpos do HEAD (com o `banco/banco.csv` do HEAD, T-78) e foram rodadas com `PYTHONHASHSEED` e pastas diferentes das do original. Depois de gravado este registro definitivo, o pipeline rodou de novo no original (segunda passagem: `out/` igual ao da primeira, exceto o relatório e `relatorio_stdout.txt`, que citam este registro) e numa terceira cópia limpa (`PYTHONHASHSEED` 99, a partir de /tmp), com `out/` (65/65) e `MANIFESTO.md` iguais, byte a byte, aos do original. Os scripts temporários da ocorrência não são necessários para regenerar: só `gerador_v1_8/` e o que já está no git. No Windows, a execução usou um shim de ambiente (LF na escrita de texto e UTF-8 nos filhos), fora do repositório.

## Determinismo

O pipeline completo foi executado a partir de `out/` vazio no original e nas cópias limpas acima (pastas e `PYTHONHASHSEED` diferentes); `out/pacote.json`, `out/pacote_estudante.json`, `out/estudante/`, o relatório e o `MANIFESTO.md` têm os mesmos SHA-256 em todas. Nenhum script lê data ou hora do sistema, nem o `HEAD` do git (o relatório não imprime o HEAD); `geradoEm` é literal.
