# MANIFESTO — T-56 — gerador v1.3 do pacote e da edição do estudante — 2026-10-13 — gerado por gbq-csc

Origem: cópia de `saida/pacote/gerador_v1_2/` (intacto; SHA-256 dos 42 arquivos conferidos contra o `MANIFESTO.md` dela: 0 divergências) para `saida/pacote/gerador_v1_3/`, alterada depois. Scripts temporários da ocorrência ficaram só no scratchpad (não persistidos). Comando de execução (a partir de qualquer pasta; `-B` evita `__pycache__`, `-I` não serve porque bloqueia os imports entre scripts): `python3 -B saida/pacote/gerador_v1_3/<script>.py`.

## Ordem de execução

1. `build_pacote.py` (grava `out/pacote.json`) e `estudante_gen.py` (grava `out/estudante/`); 2. `estudante_fidelidade.py`; 3. `sync_check.py`; 4. `validate.py`; 5. `conferencias_v13.py`; 6. `fidelidade_mutacao.py`; 7. `relatorio_v1_3.py` (grava `out/pacote_relatorio_2026-10-13_v1_3.md`). Tudo grava em `out/`; a promoção para `saida/pacote/pacote.json`, `saida/estudante/` e `saida/pacote/pacote_relatorio_2026-10-13_v1_3.md` é um passo explícito (cópia) depois de todas as conferências com 0 falhas. Caminhos derivados de `__file__` (raiz do repositório = três níveis acima de `gerador_v1_3/`); as referências v1.1/R0/v1.2 vêm do git por `refs.py` (`git show <commit>:<caminho>`, somente leitura): v1 `5eab2d9`, v1.1 `e97ab1f`, R0 `27e594d`, v1.2 `2684ab1`.

## Arquivos (SHA-256 de cada um)

| Arquivo | Bytes | SHA-256 | Estado frente à v1_2 | Papel |
|---|---|---|---|---|
| banco.py | 3184 | `6d6e975561ae53c54021a64cd8f17a2fba68f945d7f5a9ed83992163e750cfaf` | igual à v1_2 | ativo |
| build_pacote.py | 7966 | `c8caa24c1c57e6da83b10aee36995a78926745a27046ace15cc42f38189684bb` | alterado | ativo |
| common.py | 6133 | `0e80199fae555c543eb2e36436e4258ca7946246a30b79cd4008faf9f39b32c7` | alterado | ativo |
| conferencias_R1.py | 31123 | `587a8d4212429b2c4917c669106af4cb4864cd811481de6b473828bc6e6cc92e` | alterado | histórico (v1.2/R0/R1; lê do git) |
| conferencias_v13.py | 24011 | `4d5f23ace689f70aefc3c75b7393a90f62a665c269af35121843fb171b8a8530` | novo | ativo |
| diff.py | 1751 | `59fef679b240aa9e1ae7895813f4dd7be8251ae06a69921d37874ff843376bfb` | alterado | histórico (v1.2/R0/R1; lê do git) |
| diff2.py | 1547 | `6513c3b66b2b0e09669a8624f77408fe8f4f1ce6f350a391e82558e5262901d0` | alterado | histórico (v1.2/R0/R1; lê do git) |
| edital_p.py | 1183 | `0f7ed100392cdba1c09e1cf2dce107801c2fe8225920a5d501d6fc42bf89423d` | igual à v1_2 | ativo |
| estudante_fidelidade.py | 21489 | `71c7c0d5f43619db1453dd07a6de8c3beb305f95d74e08f73457fe8b5f81de8f` | alterado | ativo |
| estudante_gen.py | 12958 | `e85f3c8456a2a0136c14fd9a39f97c6100eaf7c1b6c29380b212c64e1078c192` | alterado | ativo |
| estudante_marcas.py | 8633 | `80355d3b6631e29e10e1140c523e0678645255170b06f32524579ff745715eeb` | igual à v1_2 | ativo |
| f4.py | 2542 | `e0fb812b44b2822c9d5caad8c5018b1b0df5c929e5182368e2434413f3f52727` | igual à v1_2 | ativo |
| fidelidade_mutacao.py | 2035 | `d8174dcb87af5071f9a593d1ab0cd72b882ce20227730c603856f557277e7fa6` | novo | ativo |
| gce.py | 5972 | `e007ddaeac3b07f7f47fe7472c1ec6a1d418f731e185f4baaf678e822153212c` | igual à v1_2 | ativo |
| literais.py | 12655 | `410eddd5df8b246d468f5b34cf064e5820f14f11544d9a8ed7504525c888e3e7` | alterado | ativo |
| lotes_tab.txt | 912 | `895e4d50479615c6963fcd35c01d3cd57aa8bad3994dec6c08a1a639517d27a2` | igual à v1_2 | ativo |
| out/conferencias_stdout.txt | 9502 | `0c206fc3e79b16e9068507e32e22a7e5a304ccb0e483f8734df849374ffb71b0` | gerado | saída |
| out/conferencias_v13.json | 11468 | `3abc409ad02017589e9d8fea1fe90b0380bbd6d77b6b427af475e9e1c2206a91` | gerado | saída |
| out/conferencias_v13.txt | 9502 | `0c206fc3e79b16e9068507e32e22a7e5a304ccb0e483f8734df849374ffb71b0` | gerado | saída |
| out/estudante/BANCO_gabarito.md | 9352 | `9dc8e2e306c7d3ed3e21e9d72646e64bf56223f173950e6fcc01dd86ed4672d3` | gerado | saída (edição do estudante gerada) |
| out/estudante/BANCO_itens.md | 76563 | `99ed346a4d1471fa006a8ede692067de2eee25ed39c853138872618256f6e1a0` | gerado | saída (edição do estudante gerada) |
| out/estudante/DISCURSIVAS.md | 6674 | `075b68c83526dab71905bc1370cf939a4d5135c7654d4d4bdc6b5d4374705f9a` | gerado | saída (edição do estudante gerada) |
| out/estudante/DISCURSIVAS_padrao.md | 32197 | `d8fcc706c3bd537f8cd3961461106fc8184176bbbf82f84f06f60fae321eccd0` | gerado | saída (edição do estudante gerada) |
| out/estudante/L1C_estudo.md | 3684 | `3dccee77e4a1eb4df12e0456dae9079843b49aa99a9f7789bd8025781f44be91` | gerado | saída (edição do estudante gerada) |
| out/estudante/L1C_gabarito.md | 1998 | `578698c50274793480ffd737559cc36cf3aa6ba15531c5966e08503b20541cf3` | gerado | saída (edição do estudante gerada) |
| out/estudante/L1C_itens.md | 2549 | `17c3920237a22564346db61b81f05e75cb8b103fd16d08999555a8473090b12c` | gerado | saída (edição do estudante gerada) |
| out/estudante/L1_estudo.md | 31853 | `901051d16f6623556a4c2fae78da7a20d14f69776d891009af2f104232f2f759` | gerado | saída (edição do estudante gerada) |
| out/estudante/L1_gabarito.md | 4784 | `e0a3084fe53efff0d2e58256340e3df86aecd6001b874a44e412917d563db80d` | gerado | saída (edição do estudante gerada) |
| out/estudante/L1_itens.md | 5121 | `9d888c024c20eb8ecb09d590f712b0f683ebf9cbc653ff5fc42b7564946642ab` | gerado | saída (edição do estudante gerada) |
| out/estudante/L2_estudo.md | 33430 | `f9eec1650fd222184e33fd8ab0a2c5c33793b27b47b9b4d71901c6f9b46d444b` | gerado | saída (edição do estudante gerada) |
| out/estudante/L2_gabarito.md | 6508 | `01b60a5e5ac6239e303419e4ca6615271a5dab410cde7484e94f264cf0ed366b` | gerado | saída (edição do estudante gerada) |
| out/estudante/L2_itens.md | 7391 | `a4ddb9ff0dfbf1e9487ccb93caa45406c2cc290c7f3b98b367d7160aad46ed66` | gerado | saída (edição do estudante gerada) |
| out/estudante/L3_estudo.md | 40440 | `c193b182b4ee9c93a20368201b77f446cdd8d630cf5f5c7834fb2b348572217a` | gerado | saída (edição do estudante gerada) |
| out/estudante/L3_gabarito.md | 6481 | `1cbc0474f03eaaede62a63e281b554f93ff5de6675df6480f0dc21d4e995b3ee` | gerado | saída (edição do estudante gerada) |
| out/estudante/L3_itens.md | 7594 | `5f340894de388b976ced1c17c67c34d80b74bba0c0aa3940aa71005e6ab27845` | gerado | saída (edição do estudante gerada) |
| out/estudante/L4C_estudo.md | 253 | `de79e9d124c9a83b3a7990da30d2440cdc4a7c498aa48d9aefc53d3ffdb3ba22` | gerado | saída (edição do estudante gerada) |
| out/estudante/L4C_gabarito.md | 6342 | `13d4a5cb284e04cd1e87b73740d2a2a80cfd8de80ebbc26e22187a8336cb9bdd` | gerado | saída (edição do estudante gerada) |
| out/estudante/L4C_itens.md | 2386 | `6955ac76f4724f46f3e187d0aced064770e8050de12f0e86ada71860e51c5f94` | gerado | saída (edição do estudante gerada) |
| out/estudante/L4_estudo.md | 49231 | `103d3ae4dd8057453e95b22eb86a09e958a97dc80d0ab37e0e9ac56f6151fd2b` | gerado | saída (edição do estudante gerada) |
| out/estudante/L4_gabarito.md | 5873 | `fe0574515510cd8f9115d5e18805a45ae16eb6d927bfca11020b6d017b3acafb` | gerado | saída (edição do estudante gerada) |
| out/estudante/L4_itens.md | 4527 | `58b63daca4fd6bb536c7db1e771eeb819c508ce240d35e9beb0efd1b2ed4a7e8` | gerado | saída (edição do estudante gerada) |
| out/estudante/L5C_estudo.md | 367 | `d66b4a9ac213ca9b15079c6d1303a9876309643c5aa7ad4aa344df708d8ccb3e` | gerado | saída (edição do estudante gerada) |
| out/estudante/L5C_gabarito.md | 4855 | `141c01fb0f0a0d65686b99eb39b8c2f2b51b58630c20b526b35992b951385027` | gerado | saída (edição do estudante gerada) |
| out/estudante/L5C_itens.md | 2321 | `8f0eaa89d72259e24496cfc80a61847c4b46c5bf62a53017cd3673fdcd5006e1` | gerado | saída (edição do estudante gerada) |
| out/estudante/L5_estudo.md | 31677 | `05fc54f055c2e6fb86393287a3539cd14d0ea2ae4b574f98c91188de0e4b77bb` | gerado | saída (edição do estudante gerada) |
| out/estudante/L5_gabarito.md | 5128 | `045ebb88f3d7a9d6f0ed595930601fb1bb0fda7ac2fff8d6cc4782e7fce7757e` | gerado | saída (edição do estudante gerada) |
| out/estudante/L5_itens.md | 4942 | `7a9d20523ede049979e9f46b373045dacdbc64a5df0602926bcb0d691b32fe3f` | gerado | saída (edição do estudante gerada) |
| out/estudante/L6A_estudo.md | 36911 | `fda000cb8bd5ab0a63f72eb16c3aaedc4b76024c02a513d242c0784adcb05fb4` | gerado | saída (edição do estudante gerada) |
| out/estudante/L6A_gabarito.md | 4946 | `3b7658969f123d84a116512f0804dc7f1a1ed21c1a1ba417d02e414f75672a7a` | gerado | saída (edição do estudante gerada) |
| out/estudante/L6A_itens.md | 3764 | `a002e89404975d2382babb6c36750fde519522ccb45efbf0c95545d9aeef75a5` | gerado | saída (edição do estudante gerada) |
| out/estudante/L6B_estudo.md | 54619 | `15f37d79ca2ed01d454f7bc226fcb6ee5d1b70555b32c3b044bd4b1f1de13fb3` | gerado | saída (edição do estudante gerada) |
| out/estudante/L6B_gabarito.md | 5420 | `b7f85f570081553bc405c3e888062148a56d774682be3457a2ce5e8f70a441d2` | gerado | saída (edição do estudante gerada) |
| out/estudante/L6B_itens.md | 4268 | `9045a4fe386d210114f94dab229cf94975c9645fa0a712df6a3e1383c48b7f44` | gerado | saída (edição do estudante gerada) |
| out/estudante/README.md | 2898 | `e0054ce46393ead63c19e17dca8ef6e9f1f66dfe77c1ef4f017dc14ceeb0083a` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-0-P2_folha.md | 6063 | `f69efe607e7b575c246b46eded5ce15d5b6cf1e14ae755bc1bff23087c8bdab5` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-0-P2_gabarito.md | 5889 | `1f3acd3ae9c994ca2ba046b238c8700c16043942ab8bfa9d2793c5b4f981e10a` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-0_folha.md | 19477 | `4229c2e36280aaa637ac67b4b70f6443ce2ffc7ad7c693c1ec7084b786f41cde` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-0_gabarito.md | 5998 | `d34f4d8acee5f282a28e77f016ab9d8f2565a6ed51a7d47f6ba15f32ee59c727` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-1_folha.md | 8625 | `e0e21ea32da954f4d20ac9df23937dab412179873d28211876600e938c2b9a38` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-1_gabarito.md | 12745 | `e7979c81ba32c2544b672733c634aae528fa1c42b55c21b47f7155b21ca1646e` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-2_folha.md | 9658 | `d576cc3fecc6f9973a028f82e303abb65aedd00ad14000cbc263c51423daaa92` | gerado | saída (edição do estudante gerada) |
| out/estudante/SIM-2_gabarito.md | 9310 | `e298f570eacb7f5a17465ee2a2ac704cdc597e88513c41b8193e79af440387c6` | gerado | saída (edição do estudante gerada) |
| out/estudante_contagem.json | 6142 | `6f54874904e5e956cb2815d0b014c44b4f6cad7dc1e619940b8e9b87756f268c` | gerado | saída |
| out/estudante_fidelidade.json | 502 | `69fa5fb10740050b27d906ae26925937b9b180f5d87f60dbc2e5b64e6417bac3` | gerado | saída |
| out/fidelidade_mutacao.json | 297 | `6b4b6be8ba49ce1ade443703c8389e39ec44eac03441f0d1eaade54d58b5942d` | gerado | saída |
| out/fidelidade_stdout.txt | 1777 | `dc7634d9eb181d10dcc2d10cc63bc917e9a223447b1ee93bf574492c99458915` | gerado | saída |
| out/gen_stdout.txt | 1498 | `34c53732e880de7c691b1e75b78523d092143cb75d49529296a08f182d044097` | gerado | saída |
| out/mutacao_stdout.txt | 267 | `f344fd70ac411bf275aad19cb7c80bed60d7fc966db80ddd08fca275d335502a` | gerado | saída |
| out/pacote.json | 620956 | `fdcb7afdb4fb449229c6d530e877d839f8d334cd9667731e1b7222c9c7fb0eca` | gerado | saída |
| out/pacote_relatorio_2026-10-13_v1_3.md | 107842 | `e70a1fdaec50472b64d85f359927b7a00de7f9d83c08e8a6cf608701b3c329ff` | gerado | saída |
| out/relatorio_stdout.txt | 11 | `dc41e75b7d9965329d6a0f8c5b7f480d138972dad96aaef94c59355874e9c630` | gerado | saída |
| out/stats.json | 104174 | `02d5827b812f085fae7fbdfd942cbc20312ec5e0728b61b8ec709d82163a9271` | gerado | saída |
| out/sync_check.json | 1931 | `ab32033d7957c0ee57d6a01eeb0ffaf3f33f97d8271d5e6496cfaddcc1cc070f` | gerado | saída |
| out/sync_check.txt | 2243 | `f5f193737b9dbee88ce40544156bd77f031e1d8bb26aa77cec1c9f67433921b1` | gerado | saída |
| out/sync_stdout.txt | 2243 | `f5f193737b9dbee88ce40544156bd77f031e1d8bb26aa77cec1c9f67433921b1` | gerado | saída |
| out/validate.json | 13965 | `ce46a125d42281a3fba149c5ec8c980a9469f9e70f4f55edf3bda080ad15ca9c` | gerado | saída |
| out/validate_stdout.txt | 10099 | `fc013bfed3ddf5f8d438f9f4534fd2abb7f5bf148fe3ce26c0aca5b1d76f0a04` | gerado | saída |
| out/varredura_volatil_v13.json | 278 | `fc915993c98ad2a7b85545132dd81ca26041b680d3e958f1b4fc68baf72e8705` | gerado | saída |
| p1.py | 10865 | `11e8fcf3ab3aa6f547f31719185bb84072f8a0e475e6691f46346db85d747715` | alterado | ativo |
| p2.py | 25030 | `ef313ef0485f7706aeb9c21cd50070b2d16ba4b7ad67fe02526ad1e5f0bfc5bc` | igual à v1_2 | ativo |
| peg.py | 4922 | `ee0071445a44c6c043a4e3359299e33aed17ea6da3515aa96f7d656e85115d61` | igual à v1_2 | ativo |
| probe.py | 441 | `f4eb95e47897fb0026e3943ef1aa7951af0d43590292ea4b7fc13be86f71fc7b` | igual à v1_2 | histórico (v1.2/R0/R1; lê do git) |
| refs.py | 2496 | `9e87a0747440abf538944e6352a4622d2af24fcbe9c12fe2e1e48a0c0b3c9b44` | novo | ativo |
| registry.py | 897 | `6664fbc7a4bdb9a997a92def4c824c7cf2c1c6a4d31603cd22e77478c7bae78b` | igual à v1_2 | ativo |
| relatorio_R1.py | 19839 | `616bbbcc9ff4f5ee976f9b92fe1e3e40cb35919da9c3386fa495335ff0db45ea` | alterado | histórico (v1.2/R0/R1; lê do git) |
| relatorio_v1_3.py | 61768 | `f9fb593de0ce1e4d3985f2d0fc754caf91dc62fa1fd6efe738cae0fc4bc4f940` | novo | ativo |
| report.py | 15830 | `397ac2117c430da380cfcf7d7ffc758db50192081da398abf04c0daa11092ac9` | alterado | histórico (v1.2/R0/R1; lê do git) |
| report2.py | 44678 | `92c1fb9c6ac8c727831f16d2db5928bddf3f1f66cee3e6dbb87f35c523c08cc3` | alterado | histórico (v1.2/R0/R1; lê do git) |
| resid.py | 481 | `3e43ef78e0c82b3927ed5108facf18e5bc47307d6f2a5a0c266075e06d368082` | igual à v1_2 | histórico (v1.2/R0/R1; lê do git) |
| review.py | 690 | `a1c4f135e564a160e0d09a6347c04c218693fd506e67a6678f9549e7996180ff` | igual à v1_2 | histórico (v1.2/R0/R1; lê do git) |
| sync_check.py | 2225 | `9aa9eb1bbd91e682319aaf04d14d82057e62ca1b787b52b831f98902c09b34a2` | alterado | ativo |
| texts.py | 422 | `c3ca12b7283710222c8baf681738b3d0e462207a30b81167d48e84be77bb0102` | alterado | histórico (v1.2/R0/R1; lê do git) |
| validate.py | 34312 | `eb260bfa45e258e694a88f24f49fa182dbbd7c44c8c39715748d5ac58ded90de` | alterado | ativo |

Total: 93 arquivos listados, mais este `MANIFESTO.md` (não tem hash próprio). Manifesto ordenado da edição `out/estudante/` (SHA-256 das linhas "<sha256>  <nome>"): ver o relatório, seção 13. `out/estudante/` e `saida/estudante/` são idênticos (diff recursivo); `out/pacote.json` e `saida/pacote/pacote.json` têm o mesmo SHA-256; `out/pacote_relatorio_2026-10-13_v1_3.md` e `saida/pacote/pacote_relatorio_2026-10-13_v1_3.md` também.

## Mudanças frente à v1_2

- Novos: `refs.py` (leitura de referências do git), `conferencias_v13.py` (conferências (1), (3), (4), (5)), `fidelidade_mutacao.py` (teste negativo da fidelidade), `relatorio_v1_3.py` (relatório completo gerado pelo gerador, N-3).
- Alterados: `common.py` (REPO e OUT derivados de `__file__`), `p1.py` (campo `legendaMecanismo`), `build_pacote.py` (nome v1.3; `avisos` do SIM-0 lidos de `saida/simulados/simulado_0_v0.2.md`; `legendaMecanismo` por lote), `literais.py` (duas regras literais da N-1 em `L6B_estudo`), `estudante_gen.py` (legenda no topo dos 6 `*_gabarito.md`; versão v1.3 no README), `estudante_fidelidade.py` (confere legendas e a não exibição dos avisos), `validate.py` (v1.3; ordem determinística das chaves; leitura da v1.1 pelo git), `sync_check.py`, `texts.py`, `diff.py`, `diff2.py`, `conferencias_R1.py`, `relatorio_R1.py`, `report.py`, `report2.py` (só caminhos: relativos à raiz, leitura de v1.1/R0 pelo git, saídas em `out/`).
- Fora do diretório (não copiados): `__pycache__/` (não gerado), `pacote_v1_1.json` e `R0/` (lidos do git por `refs.py`).
- Determinismo: o pipeline completo foi executado duas vezes a partir de `out/` vazio e variações de `PYTHONHASHSEED` testadas; o `out/pacote.json` tem o mesmo SHA-256 em todas as execuções.
