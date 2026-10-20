# MANIFESTO_v1_13.md — T-118 (D1 da GBQ, passo 4.3.5) — 2026-10-20 — gerado por gbq-csc
Pacote v1.13, montagem depois da errata do achado 10 (conferida pela gcb-cqfp: saida/gcb/QA_D6_achado10_conferencia_2026-10-20_gcb-cqfp.md, CONFERIDO). Base: saida/pacote/T118_D1_v1_13_2026-10-20.md. Nada foi promovido a saida/pacote/, saida/estudante/ ou saida/plataforma/; sem commit; a plataforma não foi remontada. Scripts com `python3 -I`; o `montar_v1_13.py` não foi alterado.

## 1. Valores esperados pela D1 e obtidos
| Item | Esperado | Obtido | Resultado | Onde na D1 |
|---|---|---|---|---|
| montar_v1_13.py (sem alteração) | 723370f56fe830cace0d46056b681ce6c3e0b87f4497cbd1da84101ad6391ebe | 723370f56fe830cace0d46056b681ce6c3e0b87f4497cbd1da84101ad6391ebe | OK | D1, 4.3.1 |
| D6_plataforma.json (errata do achado 10) | f8691dd5a3fd968922bf8bac8e26b4dd4f1475183afc9d6a0e84418d08b17122 | f8691dd5a3fd968922bf8bac8e26b4dd4f1475183afc9d6a0e84418d08b17122 | OK | D1, 2 e 4.1 |
| out/pacote.json SHA-256 | 82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240 | 82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240 | OK | D1, 4.3.1 |
| out/pacote.json bytes | 2906558 | 2906558 | OK | D1, 4.3.1 |
| out/pacote_estudante.json SHA-256 | 04cbd593fdd30404ecb7f91f6b6722da6b2fc24e58d3c0eb68b10a4e792a0c40 | 04cbd593fdd30404ecb7f91f6b6722da6b2fc24e58d3c0eb68b10a4e792a0c40 | OK | D1, 4.3.1 |
| out/pacote_estudante.json bytes | 2644822 | 2644822 | OK | D1, 4.3.1 |
| out/diag30_DA.json (intocado) | eb1ced6df3d624ae62b82337db6a4cfe29b86baa9494e96aed1b3defe61a6800 | eb1ced6df3d624ae62b82337db6a4cfe29b86baa9494e96aed1b3defe61a6800 | OK | D1, 4.3.1 |
| out/registro_adendo5.md (regerado, achados 2 a 4) | a1ca16811394dd6ec5df186b44155704a498bc03f6ac1e8cddaf87b6f7a87437 | a1ca16811394dd6ec5df186b44155704a498bc03f6ac1e8cddaf87b6f7a87437 | OK | D1 achados, 2 |
| historico/registro_adendo5_R1_7224db40.md (versão anterior, achado 5) | 7224db40670608bff726f67b6b4769a509b225953146b80013b05d9c57f55918 | 7224db40670608bff726f67b6b4769a509b225953146b80013b05d9c57f55918 | OK | D1 achados, 5 |
| regras/pacote_contrato.md (v1.2.11) | 85b30fccadce4eb9782e1e056613a2d680cec0c01aed44fd173bda7d248e616b | 85b30fccadce4eb9782e1e056613a2d680cec0c01aed44fd173bda7d248e616b | OK | D1 achados, 1 |
| montagem (montar_v1_13.py) | RESULTADO: 0 FALHA | RESULTADO: 0 FALHA (32 verificações OK, as 16 de cada pacote) | OK | D1, 4.3.1 |
| diff dos dois pacotes contra a montagem anterior (007787e3…c192 e 8b5489b9…b8dd) | só `lotes[D6].pares[0].como` | só `/lotes[15]/pares[0]/como` (pacote.json) e `/lotes[12]/pares[0]/como` (estudante) | OK | D1, 4.3.1 |
| conferencia_t118.json | 0 FALHA | 100 critérios, 0 FALHA | OK | D1, 4.3.2 |
| edição .md (estudante_md_v113.py) | 53 arquivos; 0 FALHA | 53 arquivos; 29 conferências, 0 FALHA | OK | D1, 4.3.4 |

## 2. Contagens (de conferencia_t118.json)
- Itens de DA: 410 (D1 60, D2 80, D3 71, D4 79, D5 70, D6 50); C/E por lote: D1 30/30; D2 40/40; D3 31/40; D4 41/38; D5 35/35; D6 25/25.
- Entradas de edital P1-DA: 46 (posições 20 a 65, bloco contíguo); lotes DA: 6 (16 no total); tópicos DA: 39 (79 no total).
- nucleo DA: 366 true e 44 false; nucleo total do pacote_estudante: 733. Letra (e): nucleo recalculado pelo critério k1 a k4 com os atos D1 a D6 mapeados = nucleo do pacote em 410/410.
- Folhas de DA: 37; itens em folha: 396; fora de folha: 14 (P1-DA-1 8, P1-DA-8 6). Itens no pacote: 1159.
- VOLÁTEIS: D2-01, D2-28, D6-09, D6-32, D6-34. Ids vagos: D3-19, D3-31, D3-39, D3-42, D3-48, D3-50, D3-57, D3-60, D3-65, D3-69, D5-54.

## 3. Saídas e arquivos desta pasta (bytes e SHA-256; o manifesto não lista a si mesmo)
| Arquivo | Bytes | SHA-256 |
|---|--:|---|
| saida/pacote/montagem_v1_13/QA_final_v1_13_v16_2026-10-20_gbq-cqe.md | 37839 | 67a6108036db66e0eb5c7c47dbcf4b735390505b805fe9d1e3e053f73f043910 |
| saida/pacote/montagem_v1_13/cobertura_v1_13.py | 12329 | 72a89f86f001aebb6f4b5cf33b88c27b7f3eecbbfc75a3f0a6ccad3c8cf95312 |
| saida/pacote/montagem_v1_13/conferir_t118.py | 21048 | 3fa09b7db7e69a340e4e401cf9d824d9611c75cb51aa1d715908af425b2d0768 |
| saida/pacote/montagem_v1_13/diag30_da.py | 2090 | b587a624c000d45d9317979ab8d0e36f0b4fadd53bbe54028fc978fbf0e628e9 |
| saida/pacote/montagem_v1_13/estudante_md_v113.py | 18167 | 54faa3bf2d2b57b161e004bd3cc0567408a0a8b37d397059c39ef4a986f7c976 |
| saida/pacote/montagem_v1_13/fidelidade_v1_13_T118_gbq-cqe.md | 25932 | 6c5f71f0d95f24e7b144cc482a138e6231c7bce91c3de25b9c9b7ac7d8ab4ba4 |
| saida/pacote/montagem_v1_13/historico/registro_adendo5_R1_7224db40.md | 10245 | 7224db40670608bff726f67b6b4769a509b225953146b80013b05d9c57f55918 |
| saida/pacote/montagem_v1_13/manifesto_v1_13.py | 11394 | e06115ee417d1d0e07d973822d36a74822fefea3ffc3b52e6f1a24aa2dbb9f53 |
| saida/pacote/montagem_v1_13/montar_v1_13.py | 7056 | 723370f56fe830cace0d46056b681ce6c3e0b87f4497cbd1da84101ad6391ebe |
| saida/pacote/montagem_v1_13/out/conferencia_t118.json | 2100552 | 6c5250c90f99af57cb28c907789923403c2e8a6b404dc65369608f9e2b99844f |
| saida/pacote/montagem_v1_13/out/diag30_DA.json | 988 | eb1ced6df3d624ae62b82337db6a4cfe29b86baa9494e96aed1b3defe61a6800 |
| saida/pacote/montagem_v1_13/out/estudante/BANCO_gabarito.md | 9340 | f7d9bb470356e98962227bc7d19dbd6de2eff053aa718df002b26d6f2b4cb5ed |
| saida/pacote/montagem_v1_13/out/estudante/BANCO_itens.md | 76551 | 879e1769c76c3bc655510a18a8fd66f49abb6dec52d7e3030adf93132a226c2c |
| saida/pacote/montagem_v1_13/out/estudante/DA_D1_estudo.md | 71783 | bbab97c4ba4cb970aa79d7ae962e6434bf1c0c0a83a2d7dd93bfe17155a7a570 |
| saida/pacote/montagem_v1_13/out/estudante/DA_D1_gabarito.md | 19538 | b5412f727a3739289a503fa82bfbbbd9579128776958a68318cec89575a97b47 |
| saida/pacote/montagem_v1_13/out/estudante/DA_D1_itens.md | 13594 | 6101aa686ee904eada28168a34a3fab3c593d9aca22b831a0b40000ef9919064 |
| saida/pacote/montagem_v1_13/out/estudante/DA_D2_estudo.md | 322779 | 7518e6b27bada606ecf8c7f5bb748387eebe8743a8b2215ffb84fb8c1e642e44 |
| saida/pacote/montagem_v1_13/out/estudante/DA_D2_gabarito.md | 29784 | d1a10d22d7d1d07d07b7013b6a5bd62a1ccac6e506e4953ee781aa05e0952dbf |
| saida/pacote/montagem_v1_13/out/estudante/DA_D2_itens.md | 20377 | 7516d728e72c9de27056747aec0c1cca8df8bf19a6cc1b742eedcd0f39feb7d6 |
| saida/pacote/montagem_v1_13/out/estudante/DA_D3_estudo.md | 160728 | 7301bb18a32c076feacdf5abe7ae9289182a93fd82756358bbc554f3a72e5e6c |
| saida/pacote/montagem_v1_13/out/estudante/DA_D3_gabarito.md | 25152 | 30839f7eeefad4cbe06c61ab239d5b5ca6f3b3a612cbbc5f7d3fe3fc5b044837 |
| saida/pacote/montagem_v1_13/out/estudante/DA_D3_itens.md | 18503 | e6eca373951ab9ab337d58c8f18c575c9cfbc7e0e4cf8cea0e11e617fb362117 |
| saida/pacote/montagem_v1_13/out/estudante/DA_D4_estudo.md | 166485 | 6386186b19341f95a0b6dd473faef452153dbd16859b0c0171d352badcfde839 |
| saida/pacote/montagem_v1_13/out/estudante/DA_D4_gabarito.md | 29844 | 13906a8be474e91393800ee8b0f52d5d73350a143e520a1db6e2e28a796c49b1 |
| saida/pacote/montagem_v1_13/out/estudante/DA_D4_itens.md | 21306 | 298331ecf5861ba8c487e281068ed4357ab9f86a376d988e7add0573589eff46 |
| saida/pacote/montagem_v1_13/out/estudante/DA_D5_estudo.md | 211320 | 00784bbcf9a1771c02b706d83b2fe2c8213ce0e416f33b6b6a1b32595a42d65f |
| saida/pacote/montagem_v1_13/out/estudante/DA_D5_gabarito.md | 24462 | f84ef589bf4bac7852dff70adf85d76daeaaf170b60892e20df5d5219fdce09a |
| saida/pacote/montagem_v1_13/out/estudante/DA_D5_itens.md | 18961 | 538f74c5a6822f07bccae02e3bc3f9d0b2dde9e8ab0f6e9a3ca14722eb9ceda3 |
| saida/pacote/montagem_v1_13/out/estudante/DA_D6_estudo.md | 131726 | c849c448c84cbcb9810eff970b01b577e88d12703049186f94d0872fff0f4988 |
| saida/pacote/montagem_v1_13/out/estudante/DA_D6_gabarito.md | 17334 | 8b4878363a6f0d0c907d9aa8109a385b6ac01594c8f462ceb0fa9d66d2479676 |
| saida/pacote/montagem_v1_13/out/estudante/DA_D6_itens.md | 12227 | 1f37c2f95d1986f469ab591334a868729911dbdfa63d6be485a140cf825a593b |
| saida/pacote/montagem_v1_13/out/estudante/DISCURSIVAS.md | 6694 | 7777c52ca635cdd0e33a525aadd3b86699d333def9bb61816c79b67653f17bd0 |
| saida/pacote/montagem_v1_13/out/estudante/DISCURSIVAS_padrao.md | 32002 | 4d5a4e6e9cb23fffee9b401f7b8b9537ce9475cdc8127e34cd27c6592f77dcb4 |
| saida/pacote/montagem_v1_13/out/estudante/L1_estudo.md | 55866 | 12ebe1ac46ce54b2d2f53dfce680e90c235ed6f1743bbb7d41b836e4247dda7f |
| saida/pacote/montagem_v1_13/out/estudante/L1_gabarito.md | 69895 | 2947f638e5f9f1a08133716a7bb3b4d6f961330aa87dc5fc9d5252bec363cf7a |
| saida/pacote/montagem_v1_13/out/estudante/L1_itens.md | 70462 | 94e106e720f28ace0fedabb9e5050ee018e2e5147cef926700cff45929325050 |
| saida/pacote/montagem_v1_13/out/estudante/L2_estudo.md | 48933 | 4b3d27b2ea186da1d97d9571608d36f00160696d450b2f2e9c193258d3346d3c |
| saida/pacote/montagem_v1_13/out/estudante/L2_gabarito.md | 53394 | 7aa74384f5dd7e5bac2f49dc3d6b50af0322ccc10ba07cfcd0a41f9cb166d2b4 |
| saida/pacote/montagem_v1_13/out/estudante/L2_itens.md | 52495 | 9bb73429f2a9e29713c49247a61b58b1c4537aeac3850a47e3c698af5ffe7924 |
| saida/pacote/montagem_v1_13/out/estudante/L3_estudo.md | 54586 | a6ea08ad469fb819db5bfb8609ad2ec3f436f62fddb049a3277669bb0e61435d |
| saida/pacote/montagem_v1_13/out/estudante/L3_gabarito.md | 38836 | 5a2516422ebb27293f0a337fcae04ad539de3122e6e9c97c0cfdfd450028ce92 |
| saida/pacote/montagem_v1_13/out/estudante/L3_itens.md | 41600 | b4ca1f7707a5789eb1750caa833d9a4d6a60d930642dc4908065e2b128bf2281 |
| saida/pacote/montagem_v1_13/out/estudante/L4_estudo.md | 64066 | 7f9bedfcc79f896c0b3ed162474649b5d6c021f9bc43767752bac98438bacf27 |
| saida/pacote/montagem_v1_13/out/estudante/L4_gabarito.md | 17579 | 66f95d58f2154763b7b362ee0ae426d3e86b6fa472c081a863716cf488aa5575 |
| saida/pacote/montagem_v1_13/out/estudante/L4_itens.md | 8920 | 6620555a3b368b66c1ca21a2ebc1faf9a2515016e747d64acf567d6a523c6545 |
| saida/pacote/montagem_v1_13/out/estudante/L5_estudo.md | 45121 | 50abca622f917d20406241ded6fccd576c55683e30c5a7b4ff29931c351ac5e2 |
| saida/pacote/montagem_v1_13/out/estudante/L5_gabarito.md | 9627 | bbd753e15773894ad70c20b11286f3d5b7b440635ca7ce47b5d8409c344703bc |
| saida/pacote/montagem_v1_13/out/estudante/L5_itens.md | 7115 | e110570384225bda943dd709e1a4272faa6581b94eadad6ebf6f42fc488afaa3 |
| saida/pacote/montagem_v1_13/out/estudante/L6A_estudo.md | 56408 | 8ae7516d4b409f7944c81cb879b9941f1621a5d0bfab5eaca31ac3bb3e9f2065 |
| saida/pacote/montagem_v1_13/out/estudante/L6A_gabarito.md | 8055 | c2fab83b8520fbb20427647236a51c51103cbb7dc92389c07eb472ee955a995a |
| saida/pacote/montagem_v1_13/out/estudante/L6A_itens.md | 4206 | afa0a0e333ff7ac2d4857ee80e72142a8825befb417832c15921f1663ff31b1e |
| saida/pacote/montagem_v1_13/out/estudante/L6B_estudo.md | 70677 | 3a5c7eca9a7f507a976422b2ef2e36b388d371a8e352897919c7720466c7c4c8 |
| saida/pacote/montagem_v1_13/out/estudante/L6B_gabarito.md | 8767 | 8b23a83303888f821334d100186648807ae6562a4a683f11d88cb9f988798b91 |
| saida/pacote/montagem_v1_13/out/estudante/L6B_itens.md | 5089 | cac479bf65a9d8fc9e8d94822eed87e8f6b0257cf49c2028dab6f43873565077 |
| saida/pacote/montagem_v1_13/out/estudante/NUCLEO.md | 7567 | daf80aa5113be8916a3109c50c4e821c6fc2a28aa7613775fc52f507c8f530a0 |
| saida/pacote/montagem_v1_13/out/estudante/README.md | 4358 | e5f58436cbceb6ff550ba88fe936abf59c929f221731f097e9b33d4eb8c41eaa |
| saida/pacote/montagem_v1_13/out/estudante/SIM-0-P2_folha.md | 6063 | f69efe607e7b575c246b46eded5ce15d5b6cf1e14ae755bc1bff23087c8bdab5 |
| saida/pacote/montagem_v1_13/out/estudante/SIM-0-P2_gabarito.md | 5956 | cdd8a6588d0e24ebd4e445a50a7d11334e324eb4a85dbfd46b7babe0bbdcc081 |
| saida/pacote/montagem_v1_13/out/estudante/SIM-0_folha.md | 19458 | 7ef04f37578a2da082ab8c016ac06a06e8463db96089c268cd7e9b100815cd16 |
| saida/pacote/montagem_v1_13/out/estudante/SIM-0_gabarito.md | 5979 | 2df79ffa2501e38c66564a8b2a23cd5632372255bf7214c9179ca8ece3788374 |
| saida/pacote/montagem_v1_13/out/estudante/SIM-1_folha.md | 8625 | e0e21ea32da954f4d20ac9df23937dab412179873d28211876600e938c2b9a38 |
| saida/pacote/montagem_v1_13/out/estudante/SIM-1_gabarito.md | 15085 | 17b0de7a1e3e34943dfeffe91fdfb1f746bcabffbe6c976516e6623a4ad84c96 |
| saida/pacote/montagem_v1_13/out/estudante/SIM-2_folha.md | 9658 | d576cc3fecc6f9973a028f82e303abb65aedd00ad14000cbc263c51423daaa92 |
| saida/pacote/montagem_v1_13/out/estudante/SIM-2_gabarito.md | 9565 | 2113d4a7c1e399a1ce25b71d5819fe565121d3fc41c9a4d4c2b3e3e75e248c9e |
| saida/pacote/montagem_v1_13/out/estudante_md_v1_13.json | 14582 | ad7374ddfe448e7ee3cfbbdbd72f79f4fd08fd3bd6537cf6f77d54946215f5fa |
| saida/pacote/montagem_v1_13/out/pacote.json | 2906558 | 82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240 |
| saida/pacote/montagem_v1_13/out/pacote_estudante.json | 2644822 | 04cbd593fdd30404ecb7f91f6b6722da6b2fc24e58d3c0eb68b10a4e792a0c40 |
| saida/pacote/montagem_v1_13/out/registro_adendo5.md | 11582 | a1ca16811394dd6ec5df186b44155704a498bc03f6ac1e8cddaf87b6f7a87437 |
| saida/pacote/montagem_v1_13/out/stats_v1_13_DA.json | 2145 | f077cb33900b3f765b8c3259c1768b0dc3699ff2872fdfe24cf028b997dc7320 |
| saida/pacote/montagem_v1_13/registro_adendo_v113.py | 14341 | 42b7025ba268cd0b6040328f6ac28997a596d06d60be073079a2d1ef3255fa70 |

Total: 70 arquivos em montagem_v1_13/ (dos quais 53 em out/estudante/). Nenhum arquivo fora desta pasta: o adendo 5 fica só em out/ até a promoção (achado 5 da fidelidade T-118).

## 4. Entradas lidas (SHA-256)
| Entrada | SHA-256 |
|---|---|
| saida/gcb/D1_v2.md | 63bd27c34baec035dd39904ef565f6b5a662c0a30886a4a3d0b13b8b702e3d56 |
| saida/gcb/D2_v2_1.md | 59cffaa689ea869cd11c13e6a833470b0b91d24b0f25ea2cc2e100ac9be8bd2c |
| saida/gcb/D3_v2_1.md | 0f7a8b090fe6f2243ae55b36273dacdb719aaf04b19548dce70aad4867798930 |
| saida/gcb/D4_v2_1.md | c1a7a93598e9fd37b2009b9feaca3afd3898fa05f6f66e6de26dd40c2839e5d9 |
| saida/gcb/D5_v2_1.md | 44ddcc982642df66b246108cb7e3ef86031e8a99762aa2262a6c0bdde24e1333 |
| saida/gcb/D6_v2_1.md | a983105818ad84e96a57a4f70ff19baa12224e11e939d023c6f7a29ca5414090 |
| saida/gcb/DA_plataforma/D1_plataforma.json | 5d953b134307f40e3f51485c5550d6eadbda3a96a64ea3dfb3a3ae845439fbe9 |
| saida/gcb/DA_plataforma/D2_plataforma.json | cba2e2769ba680ee028edf0f0a5e52a5bf55671c894f5c920edaf84f3cf139bf |
| saida/gcb/DA_plataforma/D3_plataforma.json | 917827abb6a2c5d01af386eaa0bf7678cbd0e02b8896e9cb9262216eb4c8f9c1 |
| saida/gcb/DA_plataforma/D4_plataforma.json | e44b66e785a8d4ce55449b2574153d7670a603cb8f457975248aede323c22806 |
| saida/gcb/DA_plataforma/D5_plataforma.json | 5ebec2854beb00ac0fb2581c028095d4dc306fec61118080cd37666c47e3a0c2 |
| saida/gcb/DA_plataforma/D6_plataforma.json | f8691dd5a3fd968922bf8bac8e26b4dd4f1475183afc9d6a0e84418d08b17122 |
| saida/gcb/DA_plataforma/edital_DA.json | 39ee7e4bafc5f729209b384c476885628c12afc2c7e2985367422a01d4c1c239 |
| saida/pacote/gerador_v1_12/out/pacote.json | 3476525319b027fe4427bf93598d516087ad6f18fb8dd5bbed4ad8c04be6024f |
| saida/pacote/gerador_v1_12/out/pacote_estudante.json | 23224c96b4189097012f139f52a9b995c29d930c6ac72801659720d6db612abd |
| saida/gcb/DA_plataforma/D1_registro_formato.md | 66c65194a3bd58fd2bee379c0ed05ed35f224904e9621dd83ac3e177e726a0a2 |
| saida/gcb/DA_plataforma/D2_registro_formato.md | a05e0defce09f0690a3e101d32948d2f6cc6adbba542522e71b5daac57833b8e |
| saida/gcb/DA_plataforma/D3_registro_formato.md | 8e49aaa00290c1a96b9cd753e0fed14eee90fc37ea50866f3230f0d7653d0f87 |
| saida/gcb/DA_plataforma/D4_registro_formato.md | 8f7cc0995b16f4508676c4fab7d94561c7d7352f3b62410ebac921ac4c52a0d1 |
| saida/gcb/DA_plataforma/D5_registro_formato.md | 77bb5787f2553171118d20c222b23b3cb4eb871128f38e095d7112dfddd95234 |
| saida/gcb/DA_plataforma/D6_registro_formato.md | 7998cc7be19676125ba13bdcc7f52537012488371ec8e1f9e01aa916b09890ca |
| DECISOES.md | 3fd7bed93b63491e3a8852a8ee0540b2ee3ea0c259ce0231628e77c8ae632d74 |
| regras/pacote_contrato.md | 85b30fccadce4eb9782e1e056613a2d680cec0c01aed44fd173bda7d248e616b |
| saida/estudante/ (35 .md da base) | SHA-256 de cada um conferido contra saida/pacote/T115_promocao_v1_12_2026-10-18.md (M0.2: OK) |

## 5. Divergências e observações (nenhum valor foi ajustado à força)
1. Valores esperados pela D1: nenhuma divergência (seção 1: tudo OK).
2. Scripts: a D1 cita `conferir_t118.py`, `registro_adendo_v113.py` e `estudante_md_v113.py` como "scripts novos" em montagem_v1_13/; não existiam e foram escritos pela gbq-csc nesta execução (mais `manifesto_v1_13.py`). O `montar_v1_13.py` e o gerador_v1_12 não foram alterados.
3. Ordem de apresentação do canônico: nos lotes D3 e D5 a ordem da seção 5.1 do canônico difere da ordem numérica do id (ex.: D5-71 vem depois de D5-53). O pacote segue a ordem numérica do id (contrato v1.2.10, ponto 3; D1 da GBQ; FORMATO, seção 4), e o `nucleo` usa a posição no pacote. Informativo em conferencia_t118.json; não é critério.
4. Adendo 5, formatos: o canônico dos lotes D1 e D6 não traz o campo "Formato" por item (só "Mecanismo"); o adendo traz os códigos dos lotes D2 a D5 (código de 3 letras, T75_reconciliacao, 5.5) e declara os lotes D1 e D6 como não classificados. A D1 não manda classificar.
5. Adendo 5, restrições de montagem: a D1 pede a remissão às seções 5.5 da T75, 4.5 da T76 e 5.5 da T77, à "D1 da T-74" e às reconciliações dos lotes D1 e D6. Para o lote D5 o adendo remete a T74_reconciliacao_2026-10-20.md (seções 2 e 5.5); para o lote D1, a T73_reconciliacao_2026-10-17.md (seções 2 e 4); para o lote D6, a T101_reconciliacao_2026-10-18.md (seções 2 a 4 e 6). Escolha da gbq-csc entre as seções existentes.
6. Edição .md: pares e pegadinhas de DA saem sem marcas (`- a × b | como`; `- [item] rótulo — texto`), para cumprir "0 `**` nas seções de pares e pegadinhas" (o formato dos L<n> usa negrito). Resumo e curso vão em bloco de texto, como nos L<n>. README: linhas de DA (uma por lote, mais uma nota) acrescentadas depois da linha do L6B; versão "v1.13-E" e data 2026-10-20. NUCLEO.md: ordem das linhas pela ordem do edital; as linhas anteriores ficaram idênticas. Forma admitida pela errata v1.2.11 do contrato (saida/pacote/contrato_v1_2_11_2026-10-20.md), que substitui o último subitem do ponto 8 da v1.2.10 (achado 1 da fidelidade T-118).
7. Conferência M6.3: duas tabelas (P1-DA-4.2 e P1-DA-7) têm "Aspecto" como primeira coluna e foram descontadas da contagem das tabelas `compare` (23).
8. A montagem anterior em out/ (007787e3…c192 e 8b5489b9…b8dd, as embutidas na plataforma v16) foi substituída pela montagem canônica (82c4117c… e 04cbd593…); stats_v1_13_DA.json mudou só no `sha_json` do lote D6. A plataforma v16 não foi remontada (D1, seção 2).
9. Pendente (outros responsáveis): cobertura v1.13 (secretaria), fidelidade (gbq-cqe), reconciliação e gatilho A (gbq-gerencia); promoção byte a byte e publicação só depois do aceite e do "sim" do Fundador.
10. Correções pós-fidelidade (D1 da GBQ, saida/pacote/T118_D1_achados_fidelidade_2026-10-20.md): registro_adendo_v113.py corrigido (achados 2, 3 e 4) e out/registro_adendo5.md regerado; a cópia antecipada do adendo em saida/gbq/ (7224db40…) foi movida para historico/registro_adendo5_R1_7224db40.md, sem promoção (achado 5); este manifesto passou a listar todos os arquivos da pasta, inclusive cobertura_v1_13.py e fidelidade_v1_13_T118_gbq-cqe.md (achado 6). out/pacote.json, out/pacote_estudante.json, out/stats_v1_13_DA.json, out/conferencia_t118.json, out/diag30_DA.json, out/estudante_md_v1_13.json e os 53 arquivos de out/estudante/ não mudaram.
