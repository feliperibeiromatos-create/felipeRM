# MANIFESTO — T-108 e T-109 — gerador v1.11 do pacote.json, do pacote_estudante.json e da edição .md (GERAÇÃO FINAL) — 2026-10-18 — gerado por gbq-csc (manifesto_v1_11.py)

Origem: cópia de `saida/pacote/gerador_v1_10/` (intacta; nenhum byte mudou), sem `out/` e sem `__pycache__/`, mais as mudanças da D1 da GBQ (`saida/pacote/T108_D1_pacote_M2_2026-10-18.md`). Base do pacote: o pacote.json v1.10 aceito, lido do git no commit `cacd606` (SHA-256 `d43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed`); itens, ids, ordem, enunciados, gabaritos, simulados e demais blocos não mudam. Mudam só as edições das tabelas de limpeza (registradas no campo `interno`), o `itemEdital` do L2-R16 (T-109), `nome` e `geradoEm`.

Modo desta execução: ALVO=M2; VERSAO=1.11; E_L2R16=True (ATO_L2R16 D-T109-L2R16-ACEITE); geradoEm 2026-10-18. GERAÇÃO FINAL.

Condições de entrada da geração final ainda não cumpridas: nenhuma.

## Pipeline (`sh rodar_tudo.sh`; cada passo com `python3 -I -B _run.py <script>`)
| Passo | Script | Saída |
|---|---|---|
| 0 | `ensaio/gera_tabelas_ensaio.py (só ENSAIO)` | `ensaio/*.csv`, `ensaio/relatorio_ensaio.json`, `ensaio/excecoes_ensaio.json` |
| 1 | `build_v111.py` | `out/pacote.json`, `out/stats_v1_11.json`, `out/folhas_v1_11.json` |
| 2 | `estudante_json_v111.py` | `out/pacote_estudante.json`, `out/estudante_json.json` |
| 3 | `registro_adendo_v111.py` | `out/registro_adendo3.md` |
| 4 | `estudante_md_v111.py` | `out/estudante/` (35 arquivos), `out/estudante_md_v1_11.json` |
| 5 | `registro_alteracoes_v111.py` | `out/registro_alteracoes_v1_11.csv`, `_manter.csv`, `_resumo.md` |
| 6 | `validate_v111.py` | `out/validate_v1_11.json` (C-4, C-9, C-10, C-13, C-16) |
| 7 | `conferencias_v111.py` | `out/conferencias_v1_11.json` (C-1 a C-3, C-5 a C-8, C-11, C-12, C-14, C-15, C-17), `out/casos_erros/` |
| 8 | `inventario_v111.py` | `out/inventario.csv`, `out/inventario.json` |
| 9 | `fidelidade_mutacao_v111.py` | `out/fidelidade_mutacao_v1_11.json` (bloco M) |
| 10 | `manifesto_v1_11.py` | este `MANIFESTO.md` |

## Arquivos da pasta (SHA-256 e bytes, como em disco)
| Arquivo | SHA-256 | Bytes | Frente ao v1_10 | Uso na v1.11 |
|---|---|---|---|---|
| `_run.py` | `ebdc3800a04ec950637d33409bc892b6d716ab126530c3f4d6ec831ee3d3fa1e` | 664 | alterado | executor isolado de todos os passos (saída em UTF-8) |
| `banco.py` | `02f089439a2a4ce714a80b98d37936458605439a6580d821aedae2ce35b92f5d` | 3766 | igual | herdado; só registro (não executado) |
| `build_pacote.py` | `fcc9109356ccec28cfb0561fc7d2874b72ce43928e032690cac62c7f3455e819` | 8173 | igual | herdado; só registro (não executado) |
| `build_v110.py` | `aca3b809dcee621b5d9008e945d7925ad8699869040ee971e60f36954f9f6ccf` | 6548 | igual | herdado; só registro (não executado) |
| `build_v111.py` | `641a38f48197b105bedaceda3362d5299667c71fbd3ac40e330f8d83150dfe48` | 8074 | novo | passo 1 |
| `build_v19.py` | `e3873c33f2c0cd2df4a0985cb5d485616a038e1b36d1ac17051015d63313415e` | 2726 | igual | herdado; só registro (não executado) |
| `common.py` | `421ee3976657c388ee4c5c0c16391e1c293b644dfe2f67e21b9816ad9543a32a` | 6366 | igual | módulo |
| `conferencia_f_2026-10-17_v1_8.json` | `3badf68f4f9a0d188c23f7c6558b67d3b92b8178553b51b9ce58d0e8e9399d02` | 1553 | igual | herdado; só registro (não executado) |
| `conferencias_R1.py` | `99dcdd33c9af370f71f14e87fe6b53319ced4103c71c20316eba315882ca8620` | 31439 | igual | herdado; só registro (não executado) |
| `conferencias_v110.py` | `6ecf299fc9f81e2a0bcbda1ff2b8337224e232fe7f761e60e9d747c46ac4dadd` | 12146 | igual | herdado; só registro (não executado) |
| `conferencias_v111.py` | `b8675958b19504fedc960a7a6111c616a28f6e97f71c58dcaa8d6cc2f4a9bd39` | 20857 | novo | passo 7 |
| `conferencias_v18.py` | `097f61747ae108ebc1bfa77028cbc39dc33b4996424937bbe7311418218c4efd` | 108913 | igual | herdado; só registro (não executado) |
| `conferencias_v19.py` | `9c5acdd936c3d11eeb725761416c40049982902b6bd7934f7d3f52321c002bf8` | 11156 | igual | herdado; só registro (não executado) |
| `config_v110.py` | `0871b2d7af08f42540931e9ccc9e053a8bf4c07f22b2c198b79ccc83f229081b` | 1660 | igual | módulo (E_L2R131, ATO_L2R131 lidos por nucleo.py e estudante_json_v111.py) |
| `config_v111.py` | `7e0f1fda1df07dca020940853827260fa8d01f168b8b23e1225a0582415f6136` | 9059 | novo | módulo (chaves da ocorrência; único lugar do número da versão) |
| `diff.py` | `a992af7d0bc1a5f587a99db51facf56412dbc99603148faf929132289b2a73b4` | 1786 | igual | herdado; só registro (não executado) |
| `diff2.py` | `88ec4bd7fd5df6587c547961b237cd49c572a7920f4e89fdd4bc8d5096becb60` | 1578 | igual | herdado; só registro (não executado) |
| `edital_p.py` | `76adfd601e8dbc4b7cea35f8a3538939e67b9307f65524cdae6dcf70d036d67e` | 1211 | igual | herdado; só registro (não executado) |
| `estudante_fidelidade.py` | `58e77d0274c256748e75277ae3811adc1e356ae4981c809d785774c4d9b06f99` | 27275 | igual | passo 2 (módulo: only_deletions) |
| `estudante_gen.py` | `16eed1bed5a3eccc8c5bae8516812b1806829c3cb8643178c47bfbcc2bddb8d0` | 17729 | igual | passos 2 e 4 (módulo: lote_of, lote_fund, COMPL, FUSAO) |
| `estudante_json.py` | `8dd215a4f33e32aeec66f5dd68cb401c7965106e0c7575dcc5623ea0c2c92688` | 21711 | igual | herdado; só registro (não executado) |
| `estudante_json_v111.py` | `8b76fd1c67fab22f2e00d84b263d3de179fe0fe36982d7cbf8fdbad8a3483764` | 24782 | novo | passo 2 |
| `estudante_marcas.py` | `598cfce4be4ffc30bb2817b54c25efdf26586eaef8b4be8fef1a522c4addbd8b` | 10065 | igual | passo 2 (módulo) |
| `estudante_md_v110.py` | `ee7ce49f45fa76ccf4baed7e505c46597f27462e8cef8ec271dac5aff4f3e6f2` | 6095 | igual | herdado; só registro (não executado) |
| `estudante_md_v111.py` | `895e498b3caf24d8e87c421c7800cb0be31268f8e81c6f297617dd4dbf776391` | 13304 | novo | passo 4 |
| `f4.py` | `084421fbea636c9264580ad8baef50e27778dcfb7cce6e23c6ac68b0fc7603b8` | 2597 | igual | herdado; só registro (não executado) |
| `fidelidade_mutacao.py` | `50cfb459b0210b205841e2527b98b0454976b62f114b349ace2b5ba93cf8f776` | 3989 | igual | herdado; só registro (não executado) |
| `fidelidade_mutacao_v111.py` | `04a382fd4363b44f738476b6cad26b4a9db20972291784d824d4f522357e720a` | 16938 | novo | passo 9 |
| `gce.py` | `ba575e4c66a0da2bba65c05fd8318378908ebaffbca5bc36b40a0640966d2417` | 6171 | igual | herdado; só registro (não executado) |
| `inventario_v111.py` | `16e3cf25ba053531e0c8db24a484d7bbe2095af53978f72d98190d491188a222` | 16988 | novo | passo 8 e módulo (posições dos casamentos; extensão aos .md) |
| `limpeza_v111.py` | `e3fe3f4f17bc95b81c502752ab342c173912bae0a5b442efd538f15737113e95` | 11651 | novo | módulo (aplicação ocorrência a ocorrência; `interno`) |
| `literais.py` | `ef637881862fc6c9ee72e8f25686abef4bccaeb84514d4aae6c7defc68c97314` | 14340 | igual | herdado; só registro (não executado) |
| `lotes_tab.txt` | `d3ca792baeb70967479abc27b63213558b121fd70554140f5bdd521538ad1f94` | 921 | igual | herdado; só registro (não executado) |
| `manifesto_v1_10.py` | `f73c3b668565adee30ba384922c28449effd3db4650500cc14a3704d04ff408f` | 5441 | igual | herdado; só registro (não executado) |
| `manifesto_v1_11.py` | `6c579ae0b14c26bb844ba16c6770798e4be8f26f458777501bc70c9627596335` | 7349 | novo | passo 10 |
| `manifesto_v1_8.py` | `e176863b21d18345a649340f32025a0d53ef939b68a36d85c3ec57b66c90a59a` | 18560 | igual | herdado; só registro (não executado) |
| `manifesto_v1_9.py` | `416322b60d127a1f729831574c3a0b93c0b1e958c9c7a871193b0da9ec6bb642` | 4772 | igual | herdado; só registro (não executado) |
| `marcas_processo.py` | `b89ee0380dba0918e1495f29707119e257b9e08f4504d5f6da975498b17f1a5a` | 8349 | igual | passo 2 (módulo: varredura R) |
| `marcas_x_v110.py` | `8ff6ce669d777745d5936e819c5910e728b635c3e071a8508be1841cc6317c85` | 1130 | igual | passo 2 (módulo) |
| `marcas_x_v111.py` | `078511a93c4abe3884cdf0bfd142de9fecca5a8d11640ee07ad795d87fa1f032` | 727 | novo | passo 2 (módulo: entradas X propostas pelo ensaio) |
| `nucleo.py` | `9aa41b9e96c34151fe5b516a9719842c4f97cde2cb0fb4aee741979a3d7d71a2` | 4334 | igual | passo 2 (módulo: nucleo) |
| `p1.py` | `2f7912b5de0e4a5559f1ae0c2c36a9dc2d008f1e380a666fea137260d11d2c0d` | 11279 | igual | herdado; só registro (não executado) |
| `p2.py` | `4b1d53725a48e9704ee523bb321f5e8f3f1d5eb604a18e7fb5dda30784ef7140` | 27503 | igual | herdado; só registro (não executado) |
| `peg.py` | `665462377058c399fc47698379de6b9c72ffece6e3ac17abce85cd0b48a839a8` | 5058 | igual | herdado; só registro (não executado) |
| `probe.py` | `6942a41943ada2ba5ecf96a0ca7127f97168c6f5ac302be64b9c83c68f526a1b` | 454 | igual | herdado; só registro (não executado) |
| `reforco.py` | `f804a023a4a152521142ab5fcd8802a115d6a269cc53e70e4d46f43fcd6b2a6b` | 14053 | igual | herdado; só registro (não executado) |
| `reforco_marcas.py` | `d1966e41fde35ecd86360da00b4793818c98134e22ea2d845e909c368d4bb68d` | 1485 | igual | passo 2 (módulo) |
| `reforco_marcas_v110.py` | `bc92e43c2fea5fa72096cabe245e8924e74ff8b923bb5ecc740ea99ba9f20106` | 2980 | igual | passo 2 (módulo) |
| `reforco_v110.py` | `10d1dc4203f4f7d412030b762afc2d8c12e18adcb78ff0a30d6fedce6d60e7f2` | 15562 | igual | herdado; só registro (não executado) |
| `refs.py` | `d6294063326f21508a3862af14c56fd3b33c62944b5259a819000de484ccacfc` | 4256 | igual | módulo |
| `registro_adendo_v110.py` | `e9a449af1675ceb53d16135411c19a7eb5909c7182f7effec67e866dded54124` | 6252 | igual | herdado; só registro (não executado) |
| `registro_adendo_v111.py` | `443a5fbeb30128d88387a4f9e96667d1b03aa9a9208b3066e860810b03b40aa4` | 3688 | novo | passo 3 |
| `registro_adendo_v19.py` | `ce6940a319c243a411ed5b4672f09e49613eaa6982b364a2b85ffcfe0824e56d` | 5883 | igual | herdado; só registro (não executado) |
| `registro_alteracoes_v111.py` | `5f8e52f63ccaa8b729044220260e021164979dd4e4441c73ba5ab0a5cdfef5ec` | 7887 | novo | passo 5 |
| `registry.py` | `b207f93606e5f5f9ded316f01cda586812416c36f6c97434a43ad8a12d653546` | 918 | igual | herdado; só registro (não executado) |
| `relatorio_R1.py` | `22b76c83b69311de7fffcd51ce5716a10b157dc34527d31ebee9bb98f45aae6c` | 19988 | igual | herdado; só registro (não executado) |
| `relatorio_v1_8.py` | `9ff7a0cea99488cbcb4a4bf00287cf23a8e31ec47f55479bf353292ba2000033` | 25389 | igual | herdado; só registro (não executado) |
| `report.py` | `53acb4c813e1f6be28bc1ec04395010c332811b0a47de20c01cc54dc9de4ea45` | 15932 | igual | herdado; só registro (não executado) |
| `report2.py` | `1e418a7d5908152b88161d394fb4729899793dd1a759b5f87875afe2da33afe8` | 45143 | igual | herdado; só registro (não executado) |
| `resid.py` | `21f636b5857e8082e37b269fdd905be5221c3c90bfc97b8acecdaf12d003c207` | 494 | igual | herdado; só registro (não executado) |
| `review.py` | `97ca017b42394314433bbe4a01c595948eb5c68da70b23afcb0c3a1cae6f2aaf` | 708 | igual | herdado; só registro (não executado) |
| `rodar_tudo.sh` | `cda6013ff968017ea65d384d356eccb8c83ad0e264920f099028b8304a783b2f` | 2123 | alterado | runner |
| `sync_check.py` | `c1804b93f20c30782bb4b04c82b49550d95a84687d584ca0a1e47cb682cc4592` | 2918 | igual | herdado; só registro (não executado) |
| `tabelas_v111.py` | `6ddabc4c880e1af72c50de41d428c0807dabc6e5a92e60f51cfaf2fbe0053635` | 12287 | novo | módulo (leitura e validação das tabelas, inventário e caminhos) |
| `texts.py` | `83353c975f401a62a2699a98f2ab7b2618d076ece0f7f4b4d26bdd7662fb2970` | 435 | igual | herdado; só registro (não executado) |
| `validar_erros.py` | `540dd6aabc9ecd3b1aee1d08176e8a06db0eac991984ee01d2929bc81616ab78` | 18764 | igual | passo 7 (módulo e CLI) |
| `validar_erros_teste.py` | `fe1202a3b4cabbac57c4376c4b489aa3f7f3274d16ef233bbd0fb1602336c998` | 8136 | alterado | passo 7 (C-15) |
| `validate.py` | `7da151a3ded9e3184f6265a383d27c5259f3275efbad76d802d37df5a3dd68d8` | 44517 | igual | herdado; só registro (não executado) |
| `validate_v110.py` | `8edf47de79481bd3a4b0f27d476abab1e09dc0eb8a5e1f25c47c5c8cbc5e54ee` | 16262 | igual | herdado; só registro (não executado) |
| `validate_v111.py` | `cff58f6685fbb0dd1abdf7f0660c869c85f83e7ca8febb5282f3d90a2ebd3fc6` | 12274 | novo | passo 6 |
| `validate_v19.py` | `1ed674a5bed2db1071cc724ec68f9be6a89310735190533f4491fe5d84a88da4` | 14667 | igual | herdado; só registro (não executado) |

## ensaio/ (regerado no passo 0; só ENSAIO)
| Arquivo | SHA-256 | Bytes |
|---|---|---|
| `ensaio/T108_substituicoes_GBQ_ensaio.csv` | `528eb620dc6c95e1e27390fe90774acb861e391a467ff969932cd12f97a323dd` | 983 |
| `ensaio/T108_substituicoes_GCB_ensaio.csv` | `2a634da3b7e2508a1bc98b95f56abbb55f691ca4396eccd9f9a2bb6526c1103d` | 126135 |
| `ensaio/T108_substituicoes_GCE_ensaio.csv` | `c0b71558291095c73e18997fe37984573caeb0f91dea25561d1c66b32c0ae0c4` | 61476 |
| `ensaio/excecoes_ensaio.json` | `ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356` | 3 |
| `ensaio/gera_tabelas_ensaio.py` | `871e07a4541eda08c67dcd12fa98cc9eb556b2a2a0a6b858a079144471a184c4` | 11990 |
| `ensaio/relatorio_ensaio.json` | `febaec8b0c76df656b5ef05a4fe7be4a042d44f2e62f86d0c313c2c456c16ab6` | 15296 |

## out/ (regerado a cada execução; fonte dos promovidos)
| Arquivo | SHA-256 | Bytes |
|---|---|---|
| `out/conferencias_stdout.txt` | `d9808f7046b2b376feb5c5f45cead572783c7ff545587626a0f10878a886f298` | 4493 |
| `out/conferencias_v1_11.json` | `80d47588b1b192c9ece09b4857beed0f49b8c0f9c03c4f0b221ada9444e8c015` | 5452 |
| `out/estudante_json.json` | `f309c984c3d8ee6bac71c0022047460cfa2e9a61cf9aa0754785917eb22f49dd` | 21692 |
| `out/estudante_json_stdout.txt` | `b0a2f67b12cb6751a7787fa41aba2ba23615aca693120e08872a3e1192cbbf18` | 2738 |
| `out/estudante_md_stdout.txt` | `bff197fd9cc91d7ae19dfcd2101f42ce49e2543adc27b4c4609748e96d6a2ae9` | 131 |
| `out/estudante_md_v1_11.json` | `b016e12ca0d0dbf59f1e21e2616112657e7b8f8a6a3cb570c0145799a1e77400` | 26474 |
| `out/fidelidade_mutacao_stdout.txt` | `ba54d093803047519f09e24ff3f22bc2882cbb0c26a16c9fa5fcf7743015c3af` | 3343 |
| `out/fidelidade_mutacao_v1_11.json` | `f31e9473c24f5a532d50a01dcf3bffc9a0289132150c99f468ab6299167fae60` | 6204 |
| `out/folhas_v1_11.json` | `8791434d61e21190cbddb8ef108211067c1930041a038d21f41b5c6bc21ca3b1` | 3257 |
| `out/gen_stdout.txt` | `337fa5f8582aa8f1d575a42f4e7c03b00cdc8b01bb656c15001cb3224d4878df` | 408 |
| `out/inventario.csv` | `6c771ec984cb05d62593e99de72dfef2e78d6926c9ae42c093e8a03b360ce21f` | 142815 |
| `out/inventario.json` | `9acbe258ce23f5785d376ec376a5c2f898d71d0c6052567d1948c314f838251e` | 596 |
| `out/inventario_stdout.txt` | `54a7406a2ba939ee20c8aa8e9b707fd28c8d707cb55d45cfbb2eb9115935669e` | 598 |
| `out/pacote.json` | `1b5657c726b5852885fe0e69e7835d6ec331e6d43dd19191cf451ff4ac069517` | 1123649 |
| `out/pacote_estudante.json` | `8533b0c085594a42dd066b3e7a6161f0ea94f4f60bb2ad2cfbafc969369f6bd7` | 880435 |
| `out/registro_adendo3.md` | `b9f8e2837ef28ad9632464557dcb85990086fe579c5652cf426a6eafd72f611e` | 3817 |
| `out/registro_alteracoes_stdout.txt` | `ead02ebc6f6e42c45e53550562f0e667398c7ba0189b8a27bbe3b60f8efb7b23` | 102 |
| `out/registro_alteracoes_v1_11.csv` | `faf9007df6760c1f6223efe0966fa10f2697241aec42e00425f744d9441f36fb` | 464765 |
| `out/registro_alteracoes_v1_11_manter.csv` | `d210cb87546cbf0341cb646ab6a42f420b18ce2ba981401a78464f7eb7ba0805` | 563 |
| `out/registro_alteracoes_v1_11_resumo.md` | `9ea415b85553a03fbe037181c5e8de7d579ec3a51bacca7d235c4293b2d8b67e` | 5712 |
| `out/registro_stdout.txt` | `9bcc6ee9edb955fe079950338de0fa3f0992adc37b0e016cdb4eb49b9802f298` | 92 |
| `out/stats_v1_11.json` | `9fe957e43458c6d949ac5f296b23eed523fea3dcaaed71898eeae1c44955a667` | 4681 |
| `out/validar_erros_stdout.txt` | `a96eb28566ac456533bf65c5345e5f17422d6462619b7c90df97ddac36b29d2d` | 1578 |
| `out/validate_stdout.txt` | `3888f7ddd9658ada9a05b964a48f53093ff4cd160f0c2fc664f9a22f7953a060` | 2298 |
| `out/validate_v1_11.json` | `a21d1138a1f0e41aee8fb7dc7e4069c8823df866134ae731170b04e78bb39a6a` | 3153 |
| `out/casos_erros/importados_exportadoEm.json` | `ca039c0b82972681b9902b442e44867d80422f9b29b1c0ba8617e17abd25ad71` | 71 |
| `out/casos_erros/importados_sha.json` | `7c2b3afd60182ce1c3ae36d744272baac4b1d8e2cc108d3849fdc06980fb7ceb` | 134 |
| `out/casos_erros/incoerente_D.json` | `463a23847f577c0c5f6014bc6400cfed5c1cf41e480462faaab98a2de885ec22` | 1383 |
| `out/casos_erros/invalido_A_versaoFormato2.json` | `bae8aa0fc57ac23bd5e425c6b25e2e1c8370ce3921af88351a7be07e30687fcb` | 1383 |
| `out/casos_erros/invalido_B_campo_ausente_e_tipo.json` | `25fb6971761e1f39cb65b6bd1a48228bf5e942aa5e764e6ee41429a626a76b75` | 1180 |
| `out/casos_erros/invalido_C2_formato_errado.json` | `7a1540e0090f683a06902633167559b82660b066a51e61d94340e667b297eff9` | 1380 |
| `out/casos_erros/invalido_C_json_truncado.json` | `9f05598e3fd28b6a96ba7abcb147f650e1f995b49f4826c6da804e2b9ef9d0c6` | 596 |
| `out/casos_erros/valido_ids_reais.json` | `d27adcbca867eabeae0c7cf93630e97a3ba1ff845407f200a6c1b7bcfba5c6e8` | 1595 |
| `out/estudante/BANCO_gabarito.md` | `f7d9bb470356e98962227bc7d19dbd6de2eff053aa718df002b26d6f2b4cb5ed` | 9340 |
| `out/estudante/BANCO_itens.md` | `879e1769c76c3bc655510a18a8fd66f49abb6dec52d7e3030adf93132a226c2c` | 76551 |
| `out/estudante/DISCURSIVAS.md` | `7777c52ca635cdd0e33a525aadd3b86699d333def9bb61816c79b67653f17bd0` | 6694 |
| `out/estudante/DISCURSIVAS_padrao.md` | `4d5a4e6e9cb23fffee9b401f7b8b9537ce9475cdc8127e34cd27c6592f77dcb4` | 32002 |
| `out/estudante/L1_estudo.md` | `a43a55df8c57e43c5908b760d49d2437d92b90849033905a13c55c7d20cfee61` | 39180 |
| `out/estudante/L1_gabarito.md` | `57cc505f623da7d28baabd0407ce7147b90d5d13c8a130011f8d40e0834f2f23` | 44168 |
| `out/estudante/L1_itens.md` | `f1efb02761da3382315e9c3e80910edb146c06f181a87255a7b1270fb9fd1f67` | 44578 |
| `out/estudante/L2_estudo.md` | `5e09d1e5cccfd443767e61bebb550e53d7d737a275292f77565d90e5a787c8b4` | 34589 |
| `out/estudante/L2_gabarito.md` | `2438f956e8c9ae1c78d3739e4b4513d1f3d804ab81d700f79165d9431595e0d0` | 49992 |
| `out/estudante/L2_itens.md` | `9e0e3b1139ee9cbf799d708c42ffb2345b27cda2cde102a90e21e9411ac5a7b0` | 48961 |
| `out/estudante/L3_estudo.md` | `f2132f27da95f4ac90b0a1a10a0244a9b165f870733789c45ded12f42ee63861` | 40427 |
| `out/estudante/L3_gabarito.md` | `7e410a86e835a3eb055ae521d1b15d7e90fd3aea8ca8538c532523ea008ef176` | 9988 |
| `out/estudante/L3_itens.md` | `0364d5f683db642c1e92b2b600de6c194e94d1456a53c911a3ed5cb91e0ef751` | 11220 |
| `out/estudante/L4_estudo.md` | `160b63aea41e0bbf963ceef019f7809ed4f98919404285b636def2d1bc239d55` | 54480 |
| `out/estudante/L4_gabarito.md` | `2b7493a1f8f01268d86d5524eee9d2b452f392bf09b44a2bd51c4a728cb3cffd` | 15003 |
| `out/estudante/L4_itens.md` | `6bac01242ecd239589d5098c326d06a3cf08fe02f0fb099608a23ab7859751d2` | 6761 |
| `out/estudante/L5_estudo.md` | `9804c6f7d8c3c0c65cd3e280ab7eab10eee77523dc9ed151b9d329a4a6e5c8a5` | 33881 |
| `out/estudante/L5_gabarito.md` | `cd36b24596d3eb6a974ac8c63d84a6cda7d9e6570b72b6d8f7a7dc14638abf2b` | 9741 |
| `out/estudante/L5_itens.md` | `a51ca726cd3331cc452bbf3d6c26b36a67204f87e562b5483e37cf8df3564678` | 7098 |
| `out/estudante/L6A_estudo.md` | `3a7515c5d7328ae76e4bb6127b5eaf1e327e4043dcbcd128c3d9c2c62d3654da` | 49433 |
| `out/estudante/L6A_gabarito.md` | `fd4b9095ca8291b634cbe6352d1391af7f83c463093ea6ee38fe7babaa64c01b` | 8181 |
| `out/estudante/L6A_itens.md` | `56d6fad58fd1cf88febc4f24509ecd9acfd4d473201999020e00fc05802f4e40` | 4206 |
| `out/estudante/L6B_estudo.md` | `653d683685bea5e1fd04daf2f40cab6697001a2e0a8d5b6d9d40666bfc501fd7` | 58017 |
| `out/estudante/L6B_gabarito.md` | `eb5a045ae17afec2a7b7094924c9a392f4e4eb4b5365ccefc693312975d655a0` | 8856 |
| `out/estudante/L6B_itens.md` | `e8e4baf9d7fb9aec02b8b8a67ae96820fa2b12e0b4aad962ae66f218a281b0ed` | 5052 |
| `out/estudante/NUCLEO.md` | `a61f095db8579354baf51c06052b8e9ae3f849d4429b1ed9c877c7e6ae0088ad` | 3933 |
| `out/estudante/README.md` | `bdb05cbe09489884490f3d22f3f2ad60f72400ba1453cba43695220ff59d3951` | 2564 |
| `out/estudante/SIM-0-P2_folha.md` | `f69efe607e7b575c246b46eded5ce15d5b6cf1e14ae755bc1bff23087c8bdab5` | 6063 |
| `out/estudante/SIM-0-P2_gabarito.md` | `cdd8a6588d0e24ebd4e445a50a7d11334e324eb4a85dbfd46b7babe0bbdcc081` | 5956 |
| `out/estudante/SIM-0_folha.md` | `50d509be3f26a93f5d2fe0d8739dd8e66c9c963ce5c0b88ccd35f1987298baaa` | 19465 |
| `out/estudante/SIM-0_gabarito.md` | `780a8f30abd0730cb5ca5945f2fc9456e94af2f0a1cd07ca2dcf947fc1a5f597` | 5986 |
| `out/estudante/SIM-1_folha.md` | `e0e21ea32da954f4d20ac9df23937dab412179873d28211876600e938c2b9a38` | 8625 |
| `out/estudante/SIM-1_gabarito.md` | `535287fa7cfe59fd2e1f5297cd7058ac7af3234d728934eaeb8b09238462c2ca` | 15354 |
| `out/estudante/SIM-2_folha.md` | `d576cc3fecc6f9973a028f82e303abb65aedd00ad14000cbc263c51423daaa92` | 9658 |
| `out/estudante/SIM-2_gabarito.md` | `2113d4a7c1e399a1ce25b71d5819fe565121d3fc41c9a4d4c2b3e3e75e248c9e` | 9565 |

Resultado desta execução: validate_v111 22/22 OK; conferencias_v111 24 OK, 0 PENDENTE, 0 FALHA; fidelidade_mutacao_v111 25/25 casos.
