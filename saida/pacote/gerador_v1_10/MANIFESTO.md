# MANIFESTO — T-104 — gerador v1.10 do pacote.json, do pacote_estudante.json e da edição .md (ENSAIO) — 2026-10-18 — gerado por gbq-gerencia (manifesto_v1_10.py)

Origem: cópia de `saida/pacote/gerador_v1_9/` (intacta), sem `out/`, mais as mudanças mínimas da D1 da GBQ (`saida/pacote/T104_D1_v1_10_2026-10-18.md`). Base do pacote: a v1.9 aceita (D-PACOTE-V19), lida do git no commit `c26fc13` (SHA-256 `13660554…`); os 334 itens e os demais blocos não são regenerados, salvo as trocas da D-ABSORCAO-V110 e da D-ABSORCAO-V110-E. Novos: 225 itens (L6B-R01/R02, onda 2, L1-R131, onda 3).

Modo desta execução: E_CURSO=False; E_PADRAO=True; E_L2R131=False; geradoEm 2026-10-18. ENSAIO: nenhuma saída promovida; `saida/pacote/pacote.json` e `pacote_estudante.json` continuam a v1.9.

## Pipeline (`sh rodar_tudo.sh`; cada passo com `python3 -I -B _run.py <script>`)
| Passo | Script | Saída |
|---|---|---|
| 1 | `build_v110.py` | `out/pacote.json`, `out/stats_v110.json`, `out/gen_stdout.txt` |
| 2 | `estudante_json.py` | `out/pacote_estudante.json`, `out/estudante_json.json`, `out/estudante_json_stdout.txt` |
| 3 | `registro_adendo_v110.py` | `out/registro_adendo2.md`, `out/registro_stdout.txt` |
| 4 | `estudante_md_v110.py` | `out/estudante/` (35 arquivos), `out/estudante_md_stdout.txt` |
| 5 | `validate_v110.py` | `out/validate_v110.json`, `out/validate_stdout.txt` |
| 6 | `conferencias_v110.py` | `out/conferencias_v110.json`, `out/conferencias_stdout.txt` |
| 7 | `validar_erros_teste.py` | `out/casos_erros/`, `out/validar_erros_stdout.txt` |
| 8 | `manifesto_v1_10.py` | este `MANIFESTO.md` |

## Arquivos da pasta (SHA-256 e bytes, como em disco)
| Arquivo | SHA-256 | Bytes | Frente à v1_9 | Uso na v1.10 |
|---|---|---|---|---|
| `_run.py` | `531034aea2e719cf857acc6c32ec78757f86505dd787eb35bd060bdfa42d766f` | 525 | igual | passos 1–8 (executor isolado) |
| `banco.py` | `754571b7c0c30dfce76d23851b822d5fea16c2552a07383500a50f17f5c5ae97` | 3688 | igual | herdado; só registro (não executado) |
| `build_pacote.py` | `8e3547c0e2dfce3f382c48470a52c57f913c9baa7678e91b00d127d252589052` | 8017 | igual | herdado; só registro (não executado) |
| `build_v110.py` | `745a90f14525f3fbed302d718723ee0090d0eba6d8c14ee1bac13572c53ea051` | 6462 | novo | passo 1 |
| `build_v19.py` | `dea7944fd993cdc9eefc5f19c990b3893f473ed09e7210df9ba911a1a91b9077` | 2686 | igual | herdado; só registro (não executado) |
| `common.py` | `e81bc75dfb4faae7832f5ae8262c5f4b4c3992a249bb8529370112f1f3771848` | 6205 | igual | módulo |
| `conferencia_f_2026-10-17_v1_8.json` | `3badf68f4f9a0d188c23f7c6558b67d3b92b8178553b51b9ce58d0e8e9399d02` | 1553 | igual | herdado; só registro (não executado) |
| `conferencias_R1.py` | `587a8d4212429b2c4917c669106af4cb4864cd811481de6b473828bc6e6cc92e` | 31123 | igual | herdado; só registro (não executado) |
| `conferencias_v110.py` | `17b2debb768bae58ea07c5a150fe32dd960de290df59cad990c0477a27b2eada` | 6469 | novo | passo 6 |
| `conferencias_v18.py` | `0b41b1cf8d02e148de32b7480a84ea0f7c28138b52f58b353c936a72b4e357e1` | 107983 | igual | herdado; só registro (não executado) |
| `conferencias_v19.py` | `7989b577d1e5424feba5817c1b352c8ee69b827e37878b1cbbf3b66acfc9727c` | 11042 | igual | herdado; só registro (não executado) |
| `config_v110.py` | `5d2d29a6eac570c7ef46d8d7821fbe8da8e2594bbca5770bf3afcae86d1f8343` | 1396 | novo | módulo (chaves da ocorrência) |
| `diff.py` | `59fef679b240aa9e1ae7895813f4dd7be8251ae06a69921d37874ff843376bfb` | 1751 | igual | herdado; só registro (não executado) |
| `diff2.py` | `6513c3b66b2b0e09669a8624f77408fe8f4f1ce6f350a391e82558e5262901d0` | 1547 | igual | herdado; só registro (não executado) |
| `edital_p.py` | `0f7ed100392cdba1c09e1cf2dce107801c2fe8225920a5d501d6fc42bf89423d` | 1183 | igual | herdado; só registro (não executado) |
| `estudante_fidelidade.py` | `13b707b4b5ac41ecc431e6ad67703d32a5af1abc08521a1d135ec9c81f3b695a` | 26847 | igual | passo 2 (módulo: only_deletions) |
| `estudante_gen.py` | `c6c31a5ebd4fca5b86d4e4ba3a6548eb2f2ca979209d082d5f2e27cb9aa2893a` | 17433 | igual | passo 2 (módulo: lote_of, lote_fund, COMPL, FUSAO) |
| `estudante_json.py` | `854f13c4cae1c76146b05d97740bc553fe444e15e792e4de8b4863fab125daae` | 21406 | alterado | passo 2 |
| `estudante_marcas.py` | `41cf6eecc05d9d52c5115a383a4a2e44af56502f04d6d81ea0bfa040999c485f` | 9897 | igual | passo 2 (módulo) |
| `estudante_md_v110.py` | `488e4e3799ef387a04d2763059b73e5ffdb86d99285a93cc14840994240b31ec` | 5994 | novo | passo 4 |
| `f4.py` | `e0fb812b44b2822c9d5caad8c5018b1b0df5c929e5182368e2434413f3f52727` | 2542 | igual | herdado; só registro (não executado) |
| `fidelidade_mutacao.py` | `e5e4b7bf4026e309bb40c309c43cee8102134170b478455f1230dba6f1f1c52d` | 3935 | igual | herdado; só registro (não executado) |
| `gce.py` | `e007ddaeac3b07f7f47fe7472c1ec6a1d418f731e185f4baaf678e822153212c` | 5972 | igual | herdado; só registro (não executado) |
| `literais.py` | `93c64cd58bff76ab3afb8a7429cb3ba2b4d8af7353191e015d8949531b08518b` | 14182 | igual | herdado; só registro (não executado) |
| `lotes_tab.txt` | `895e4d50479615c6963fcd35c01d3cd57aa8bad3994dec6c08a1a639517d27a2` | 912 | igual | herdado; só registro (não executado) |
| `manifesto_v1_10.py` | `672491db8f10077dc1f21f2cbeb9bbc924e5e6870996287a543c46804a390a35` | 4803 | novo | passo 8 |
| `manifesto_v1_8.py` | `0c8c61f097bc749a7acaa782bcf9ef5755e8222fb970686ffac8f8b79e825030` | 18423 | igual | herdado; só registro (não executado) |
| `manifesto_v1_9.py` | `2b7b4bb020daa347a747ac3adac692e9262ab4f5bf2fe76a122c4cf4642113cc` | 4712 | igual | herdado; só registro (não executado) |
| `marcas_processo.py` | `7ee30de455a5c0332aca1dae2148d7670eb86bac08294f0c61a80da4484cc140` | 8200 | igual | passo 2 (módulo: varredura R) |
| `marcas_x_v110.py` | `adac74d52033a3484afc23d41b8f3385a0df5fcc84938adf21d451f8fb28db50` | 1118 | novo | passo 2 (módulo: X9–X14) |
| `nucleo.py` | `8c4599d62b37d61df0431ae5c6b32a53293ad22bbab0f09aa2918edcfb343c0a` | 4255 | novo | passo 2 (módulo: nucleo) |
| `p1.py` | `5cfc3a55b838d3f02f6b4f95302ba354aa1a036f08fe83d6817a3dc2e2981a5b` | 11025 | igual | herdado; só registro (não executado) |
| `p2.py` | `2fd6fbc7f2f12550ece27cd1022e701bf2f88f2c71ef9ffd0dbd14e4647913f9` | 27070 | igual | herdado; só registro (não executado) |
| `peg.py` | `ee0071445a44c6c043a4e3359299e33aed17ea6da3515aa96f7d656e85115d61` | 4922 | igual | herdado; só registro (não executado) |
| `probe.py` | `f4eb95e47897fb0026e3943ef1aa7951af0d43590292ea4b7fc13be86f71fc7b` | 441 | igual | herdado; só registro (não executado) |
| `reforco.py` | `252191a8d4efd47d7c84a075bf6f01d61ea8495ef5474323d444860e264c594f` | 13810 | igual | herdado; só registro (não executado) |
| `reforco_marcas.py` | `01be597885c6d1e6cf3c361922be43185e093507e3c746154b3c5f6ddd893793` | 1459 | igual | passo 2 (módulo; onda 1) |
| `reforco_marcas_v110.py` | `0bf36b9b608734d9b9bf30d7e09524cad05a61c29036a4965d1e45f4282b4b71` | 2944 | novo | passo 2 (módulo; 225 novos) |
| `reforco_v110.py` | `20a081e36790583b4f7f4347e9fb696425976ee9fd50ac3afc2d7154521f8db7` | 15313 | novo | passo 1 (módulo) |
| `refs.py` | `c3135e2eaf196f7651bf98a9d4fb3a0675069ce74ac90cf78ebcf24699a94524` | 4183 | alterado | módulo |
| `registro_adendo_v110.py` | `776a5c734f01764f9b576d4d50a8d6d01edf72cb8b31baa8c325e27fe23c13b9` | 5828 | novo | passo 3 |
| `registro_adendo_v19.py` | `7e7c4ac1cc9a137d906e50abc65d744617128e0c761977fcb0c89b99f74acb3b` | 5817 | igual | herdado; só registro (não executado) |
| `registry.py` | `6664fbc7a4bdb9a997a92def4c824c7cf2c1c6a4d31603cd22e77478c7bae78b` | 897 | igual | herdado; só registro (não executado) |
| `relatorio_R1.py` | `616bbbcc9ff4f5ee976f9b92fe1e3e40cb35919da9c3386fa495335ff0db45ea` | 19839 | igual | herdado; só registro (não executado) |
| `relatorio_v1_8.py` | `8f72f40ebc38b6376da12aa66db54a180aa3e2545de04bda967bfb50fe6c0d7c` | 25065 | igual | herdado; só registro (não executado) |
| `report.py` | `397ac2117c430da380cfcf7d7ffc758db50192081da398abf04c0daa11092ac9` | 15830 | igual | herdado; só registro (não executado) |
| `report2.py` | `92c1fb9c6ac8c727831f16d2db5928bddf3f1f66cee3e6dbb87f35c523c08cc3` | 44678 | igual | herdado; só registro (não executado) |
| `resid.py` | `3e43ef78e0c82b3927ed5108facf18e5bc47307d6f2a5a0c266075e06d368082` | 481 | igual | herdado; só registro (não executado) |
| `review.py` | `a1c4f135e564a160e0d09a6347c04c218693fd506e67a6678f9549e7996180ff` | 690 | igual | herdado; só registro (não executado) |
| `rodar_tudo.sh` | `190dcd7d712e35e33da0e5ca49d68710f5894959ba7e57a8367a712812943154` | 1670 | alterado | runner |
| `sync_check.py` | `b828c4291295034480eda023081d9b399bdfe11398f611172cf21ccc41e4b7d6` | 2868 | igual | herdado; só registro (não executado) |
| `texts.py` | `c3ca12b7283710222c8baf681738b3d0e462207a30b81167d48e84be77bb0102` | 422 | igual | herdado; só registro (não executado) |
| `validar_erros.py` | `19ab9c8b359e4a59f209ecbca3e29f2ecc16a0dd5fb49b8892538bbe7eb8f33e` | 18500 | igual | passo 7 (módulo e CLI) |
| `validar_erros_teste.py` | `33132d5a9d9aaf7ec4bf645ae57b84eca9c2094abdc70f18d6970465278f0186` | 7993 | igual | passo 7 |
| `validate.py` | `7cde528368ee261693addfb8642ba3deac40fa5db36177eabdb27d493bb795f5` | 44115 | igual | herdado; só registro (não executado) |
| `validate_v110.py` | `85c29703b02fd2b8cc5b4879427464c6897fe25000a513aa85c88212ee7a4cdf` | 16075 | novo | passo 5 |
| `validate_v19.py` | `5e3581239299b9c90faf991733599b4e93adac1e1a5e739816ab97282ed7ae9d` | 14513 | igual | herdado; só registro (não executado) |

## out/ (regerado a cada execução; prévia do ensaio)
| Arquivo | SHA-256 | Bytes |
|---|---|---|
| `out/conferencias_stdout.txt` | `9a273ab93294eba416fdf151913aaf36b899daa8f2715d8cd31ce17f84f8a54e` | 2226 |
| `out/conferencias_v110.json` | `0871d1b23e38ca60428c8648311a4eef757632125e33fe1d56cbdd325381bbeb` | 2751 |
| `out/estudante_json.json` | `8b20160fdde6e0f57c9ef78d3ba1f82376dee85aa28631eed7ef08f96228bea5` | 32596 |
| `out/estudante_json_stdout.txt` | `e9d76ed337c82fa4fa956c83a7f6579402cbb7fda96728cfb47485947e905957` | 2438 |
| `out/estudante_md_stdout.txt` | `4e6b799ad8070e45f66e1395050d547ca767d459d31b6f8e531aedcd9b8bd2a9` | 201 |
| `out/gen_stdout.txt` | `8d9cb779860411f1cc683d8c8809011649efa90e680287af4db0eba256ecccd1` | 388 |
| `out/pacote.json` | `1816020369e481ca06a633a75cfa7291272aee02c4b6eb9c77200540941884a8` | 858857 |
| `out/pacote_estudante.json` | `562516d4cb7b71f58034224327ced70109a4aa8e5a7bee978f15609a315f2f9b` | 838639 |
| `out/registro_adendo2.md` | `b2f3cd92e7477f190fbec7e1a51596af69eaafefe10a336127f8109c53dfea42` | 49148 |
| `out/registro_stdout.txt` | `e6ba56ade2ec22ec651d02fb0e1923335c46425fde4004313e33f871f4cf1bd2` | 43 |
| `out/stats_v110.json` | `4e1e09caf18a08be77b92c80622ce5745992825f83abddd13cb825dfe221761a` | 156758 |
| `out/validar_erros_stdout.txt` | `b154f9f9b248ac3f3aecba63a464b1eb70e8524a4969eadf27c5477b3cc813c0` | 1578 |
| `out/validate_stdout.txt` | `58514bb74ee3649c282127369160a500d4ee0bbac8c3f5e1f9a75b0ed0f5ec8a` | 2436 |
| `out/validate_v110.json` | `9688f4991e2d61ead05da8622f6c0b6126975ea00375fd489bd88ebabe9518fe` | 3944 |
| `out/casos_erros/importados_exportadoEm.json` | `ca039c0b82972681b9902b442e44867d80422f9b29b1c0ba8617e17abd25ad71` | 71 |
| `out/casos_erros/importados_sha.json` | `ea47a0919f69bded8a0115ab5d560b39a3deeed0319147e4e84b380261a5d8f7` | 134 |
| `out/casos_erros/incoerente_D.json` | `463a23847f577c0c5f6014bc6400cfed5c1cf41e480462faaab98a2de885ec22` | 1383 |
| `out/casos_erros/invalido_A_versaoFormato2.json` | `bae8aa0fc57ac23bd5e425c6b25e2e1c8370ce3921af88351a7be07e30687fcb` | 1383 |
| `out/casos_erros/invalido_B_campo_ausente_e_tipo.json` | `25fb6971761e1f39cb65b6bd1a48228bf5e942aa5e764e6ee41429a626a76b75` | 1180 |
| `out/casos_erros/invalido_C2_formato_errado.json` | `7a1540e0090f683a06902633167559b82660b066a51e61d94340e667b297eff9` | 1380 |
| `out/casos_erros/invalido_C_json_truncado.json` | `f3fa562491ffc9597ca41671a149f7bc0f739bdcd966743f05087a4eb15b4588` | 588 |
| `out/casos_erros/valido_ids_reais.json` | `d563643b9bb78380bab9f427c6915e19e355489e32bb31b60e14964f78b9c30c` | 1595 |
| `out/estudante/BANCO_gabarito.md` | `f7d9bb470356e98962227bc7d19dbd6de2eff053aa718df002b26d6f2b4cb5ed` | 9340 |
| `out/estudante/BANCO_itens.md` | `879e1769c76c3bc655510a18a8fd66f49abb6dec52d7e3030adf93132a226c2c` | 76551 |
| `out/estudante/DISCURSIVAS.md` | `7777c52ca635cdd0e33a525aadd3b86699d333def9bb61816c79b67653f17bd0` | 6694 |
| `out/estudante/DISCURSIVAS_padrao.md` | `a1433a21a032ac801ffa343d16c08ac2a04da2edf70856e1087c39615561c9a0` | 31957 |
| `out/estudante/L1_estudo.md` | `146708b5eb002d2a2a450b65e857ce2cf0c0bbaa29385be2003b8fdb1af147ec` | 34999 |
| `out/estudante/L1_gabarito.md` | `0102316f3fe2158f9999ad0014ab2b160ead34e80b8b5697db90fd11245edc7c` | 43395 |
| `out/estudante/L1_itens.md` | `f1efb02761da3382315e9c3e80910edb146c06f181a87255a7b1270fb9fd1f67` | 44578 |
| `out/estudante/L2_estudo.md` | `be325c0aa741ef3ca9c23bcd6282c543479e257aa7c4ffa2aac713c9ad6af815` | 33431 |
| `out/estudante/L2_gabarito.md` | `178d864f78dc90ce315f09846a023b483448a75bb8d992d7e418423988ef01ae` | 47632 |
| `out/estudante/L2_itens.md` | `d4c82030387910ead200a691ca207978e19b8e3be0d58993c0fc263dfb2a7b20` | 48651 |
| `out/estudante/L3_estudo.md` | `3d226e76971a7e67f64feed0e8d8a10cdd695253f28fc58e9b734c9e505cefd3` | 40424 |
| `out/estudante/L3_gabarito.md` | `c0fff87eeaa317d4fed5655c327c05f87ed1c1ae533d94ee9321de5323942c57` | 9987 |
| `out/estudante/L3_itens.md` | `0364d5f683db642c1e92b2b600de6c194e94d1456a53c911a3ed5cb91e0ef751` | 11220 |
| `out/estudante/L4_estudo.md` | `f9ea6165087e2bc3e54540b5515b6f987df9eb21d0ebe85a5f96a31ef774f1ed` | 49282 |
| `out/estudante/L4_gabarito.md` | `a5f570372ccae8253e906a89ca051d104d0fd0f2d52b810db7e2bee146d91025` | 12003 |
| `out/estudante/L4_itens.md` | `6bac01242ecd239589d5098c326d06a3cf08fe02f0fb099608a23ab7859751d2` | 6761 |
| `out/estudante/L5_estudo.md` | `ecf286055639ae0ed0f510f87ce687ff4c6133e313b57c0f082cc851d0fa4859` | 31713 |
| `out/estudante/L5_gabarito.md` | `67d7a106a5de47475113afe698ecc411a81ccc499c34823f8467d9da8dacad3a` | 9752 |
| `out/estudante/L5_itens.md` | `a51ca726cd3331cc452bbf3d6c26b36a67204f87e562b5483e37cf8df3564678` | 7098 |
| `out/estudante/L6A_estudo.md` | `a599f9f0160e82d8cdb2ea939898164c2f6382567f80b742644e85bd134fddb9` | 36959 |
| `out/estudante/L6A_gabarito.md` | `3c90f27011c253e138292ef954d9b450daca7976a53f9b4aadd3aa95744a8a05` | 5265 |
| `out/estudante/L6A_itens.md` | `56d6fad58fd1cf88febc4f24509ecd9acfd4d473201999020e00fc05802f4e40` | 4206 |
| `out/estudante/L6B_estudo.md` | `454d6962e88296ab8a151ab21df48d20fd6402d0270ce9c7aa98db47350bd603` | 54664 |
| `out/estudante/L6B_gabarito.md` | `782b3f66127c79c7b914f1a9e590957b0ef232a50b4aef6932098bad7b9ff0cc` | 5985 |
| `out/estudante/L6B_itens.md` | `e8e4baf9d7fb9aec02b8b8a67ae96820fa2b12e0b4aad962ae66f218a281b0ed` | 5052 |
| `out/estudante/NUCLEO.md` | `3ce3f759867e78db74fc937946fdbb6058271351ba1a3ebc105d0a941a0ad1c3` | 3924 |
| `out/estudante/README.md` | `49ccc58871d82f0426a4d8ba7fe51459198b6edb198cf73edbaf3684b2f71b1c` | 2564 |
| `out/estudante/SIM-0-P2_folha.md` | `f69efe607e7b575c246b46eded5ce15d5b6cf1e14ae755bc1bff23087c8bdab5` | 6063 |
| `out/estudante/SIM-0-P2_gabarito.md` | `1f3acd3ae9c994ca2ba046b238c8700c16043942ab8bfa9d2793c5b4f981e10a` | 5889 |
| `out/estudante/SIM-0_folha.md` | `50d509be3f26a93f5d2fe0d8739dd8e66c9c963ce5c0b88ccd35f1987298baaa` | 19465 |
| `out/estudante/SIM-0_gabarito.md` | `780a8f30abd0730cb5ca5945f2fc9456e94af2f0a1cd07ca2dcf947fc1a5f597` | 5986 |
| `out/estudante/SIM-1_folha.md` | `e0e21ea32da954f4d20ac9df23937dab412179873d28211876600e938c2b9a38` | 8625 |
| `out/estudante/SIM-1_gabarito.md` | `c67591ac09b29dea99723dd6eaa5b7e74411346e5278e1281a8d920bf1aa2d5a` | 13014 |
| `out/estudante/SIM-2_folha.md` | `d576cc3fecc6f9973a028f82e303abb65aedd00ad14000cbc263c51423daaa92` | 9658 |
| `out/estudante/SIM-2_gabarito.md` | `e298f570eacb7f5a17465ee2a2ac704cdc597e88513c41b8193e79af440387c6` | 9310 |

Resultado desta execução: validate_v110 37/37 OK; conferencias_v110 18/18 OK.
