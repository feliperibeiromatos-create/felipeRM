# MANIFESTO — T-94 — gerador v1.9 do pacote.json e do pacote_estudante.json — 2026-10-18 — gerado por gbq-gerencia (manifesto_v1_9.py)

Origem: cópia de `saida/pacote/gerador_v1_8/` (intacta), sem `out/`, mais as mudanças mínimas da D1 da GBQ (`saida/pacote/T94_D1_v1_9_2026-10-18.md`). Base do pacote: a v1.8 aceita (D-PACOTE-V18), lida do git no commit `46496ca` (SHA-256 `09d4a457…`); os 286 itens e os demais blocos não são regenerados. Novos: os 48 itens da onda 1 do reforço.

## Pipeline (`sh rodar_tudo.sh`; cada passo com `python3 -I -B _run.py <script>`)
| Passo | Script | Saída |
|---|---|---|
| 1 | `build_v19.py` | `out/pacote.json`, `out/stats_v19.json`, `out/gen_stdout.txt` |
| 2 | `estudante_json.py` | `out/pacote_estudante.json`, `out/estudante_json.json`, `out/estudante_json_stdout.txt` |
| 3 | `registro_adendo_v19.py` | `out/registro_adendo1.md`, `out/registro_stdout.txt` |
| 4 | `validate_v19.py` | `out/validate_v19.json`, `out/validate_stdout.txt` |
| 5 | `conferencias_v19.py` | `out/conferencias_v19.json`, `out/conferencias_stdout.txt` |
| 6 | `validar_erros_teste.py` | `out/casos_erros/`, `out/validar_erros_stdout.txt` |
| 7 | `manifesto_v1_9.py` | este `MANIFESTO.md` |

## Arquivos da pasta (SHA-256 e bytes, como em disco)
| Arquivo | SHA-256 | Bytes | Frente à v1_8 | Uso na v1.9 |
|---|---|---|---|---|
| `_run.py` | `531034aea2e719cf857acc6c32ec78757f86505dd787eb35bd060bdfa42d766f` | 525 | novo | passos 1–7 (executor isolado) |
| `banco.py` | `754571b7c0c30dfce76d23851b822d5fea16c2552a07383500a50f17f5c5ae97` | 3688 | igual | herdado; só registro (não executado) |
| `build_pacote.py` | `8e3547c0e2dfce3f382c48470a52c57f913c9baa7678e91b00d127d252589052` | 8017 | igual | herdado; só registro (não executado) |
| `build_v19.py` | `dea7944fd993cdc9eefc5f19c990b3893f473ed09e7210df9ba911a1a91b9077` | 2686 | novo | passo 1 |
| `common.py` | `e81bc75dfb4faae7832f5ae8262c5f4b4c3992a249bb8529370112f1f3771848` | 6205 | igual | módulo |
| `conferencia_f_2026-10-17_v1_8.json` | `3badf68f4f9a0d188c23f7c6558b67d3b92b8178553b51b9ce58d0e8e9399d02` | 1553 | igual | herdado; só registro (não executado) |
| `conferencias_R1.py` | `587a8d4212429b2c4917c669106af4cb4864cd811481de6b473828bc6e6cc92e` | 31123 | igual | herdado; só registro (não executado) |
| `conferencias_v18.py` | `0b41b1cf8d02e148de32b7480a84ea0f7c28138b52f58b353c936a72b4e357e1` | 107983 | igual | herdado; só registro (não executado) |
| `conferencias_v19.py` | `7989b577d1e5424feba5817c1b352c8ee69b827e37878b1cbbf3b66acfc9727c` | 11042 | novo | passo 5 |
| `diff.py` | `59fef679b240aa9e1ae7895813f4dd7be8251ae06a69921d37874ff843376bfb` | 1751 | igual | herdado; só registro (não executado) |
| `diff2.py` | `6513c3b66b2b0e09669a8624f77408fe8f4f1ce6f350a391e82558e5262901d0` | 1547 | igual | herdado; só registro (não executado) |
| `edital_p.py` | `0f7ed100392cdba1c09e1cf2dce107801c2fe8225920a5d501d6fc42bf89423d` | 1183 | igual | módulo (validate_v19) |
| `estudante_fidelidade.py` | `13b707b4b5ac41ecc431e6ad67703d32a5af1abc08521a1d135ec9c81f3b695a` | 26847 | igual | passo 2 (módulo: only_deletions) |
| `estudante_gen.py` | `c6c31a5ebd4fca5b86d4e4ba3a6548eb2f2ca979209d082d5f2e27cb9aa2893a` | 17433 | alterado | passo 2 (módulo: lote_of, lote_fund, COMPL, FUSAO) |
| `estudante_json.py` | `a7f29ce0da92a0a855c9942153825724193fcf289e9773d1b138840e15953dfc` | 18868 | alterado | passo 2 |
| `estudante_marcas.py` | `41cf6eecc05d9d52c5115a383a4a2e44af56502f04d6d81ea0bfa040999c485f` | 9897 | igual | passo 2 (módulo) |
| `f4.py` | `e0fb812b44b2822c9d5caad8c5018b1b0df5c929e5182368e2434413f3f52727` | 2542 | igual | herdado; só registro (não executado) |
| `fidelidade_mutacao.py` | `e5e4b7bf4026e309bb40c309c43cee8102134170b478455f1230dba6f1f1c52d` | 3935 | igual | herdado; só registro (não executado) |
| `gce.py` | `e007ddaeac3b07f7f47fe7472c1ec6a1d418f731e185f4baaf678e822153212c` | 5972 | igual | herdado; só registro (não executado) |
| `literais.py` | `93c64cd58bff76ab3afb8a7429cb3ba2b4d8af7353191e015d8949531b08518b` | 14182 | igual | herdado; só registro (não executado) |
| `lotes_tab.txt` | `895e4d50479615c6963fcd35c01d3cd57aa8bad3994dec6c08a1a639517d27a2` | 912 | igual | herdado; só registro (não executado) |
| `manifesto_v1_8.py` | `0c8c61f097bc749a7acaa782bcf9ef5755e8222fb970686ffac8f8b79e825030` | 18423 | igual | herdado; só registro (não executado) |
| `manifesto_v1_9.py` | `2b7b4bb020daa347a747ac3adac692e9262ab4f5bf2fe76a122c4cf4642113cc` | 4712 | novo | passo 7 |
| `marcas_processo.py` | `7ee30de455a5c0332aca1dae2148d7670eb86bac08294f0c61a80da4484cc140` | 8200 | igual | passo 2 (módulo: varredura R) |
| `p1.py` | `5cfc3a55b838d3f02f6b4f95302ba354aa1a036f08fe83d6817a3dc2e2981a5b` | 11025 | igual | herdado; só registro (não executado) |
| `p2.py` | `2fd6fbc7f2f12550ece27cd1022e701bf2f88f2c71ef9ffd0dbd14e4647913f9` | 27070 | igual | herdado; só registro (não executado) |
| `peg.py` | `ee0071445a44c6c043a4e3359299e33aed17ea6da3515aa96f7d656e85115d61` | 4922 | igual | herdado; só registro (não executado) |
| `probe.py` | `f4eb95e47897fb0026e3943ef1aa7951af0d43590292ea4b7fc13be86f71fc7b` | 441 | igual | herdado; só registro (não executado) |
| `reforco.py` | `252191a8d4efd47d7c84a075bf6f01d61ea8495ef5474323d444860e264c594f` | 13810 | novo | passo 1 (módulo) |
| `reforco_marcas.py` | `01be597885c6d1e6cf3c361922be43185e093507e3c746154b3c5f6ddd893793` | 1459 | novo | passo 2 (módulo) |
| `refs.py` | `ea8467cb6dde069c00329de6709fba77f712e7a0060d6b76c4fae5b177ae9988` | 3909 | alterado | módulo |
| `registro_adendo_v19.py` | `7e7c4ac1cc9a137d906e50abc65d744617128e0c761977fcb0c89b99f74acb3b` | 5817 | novo | passo 3 |
| `registry.py` | `6664fbc7a4bdb9a997a92def4c824c7cf2c1c6a4d31603cd22e77478c7bae78b` | 897 | igual | herdado; só registro (não executado) |
| `relatorio_R1.py` | `616bbbcc9ff4f5ee976f9b92fe1e3e40cb35919da9c3386fa495335ff0db45ea` | 19839 | igual | herdado; só registro (não executado) |
| `relatorio_v1_8.py` | `8f72f40ebc38b6376da12aa66db54a180aa3e2545de04bda967bfb50fe6c0d7c` | 25065 | igual | herdado; só registro (não executado) |
| `report.py` | `397ac2117c430da380cfcf7d7ffc758db50192081da398abf04c0daa11092ac9` | 15830 | igual | herdado; só registro (não executado) |
| `report2.py` | `92c1fb9c6ac8c727831f16d2db5928bddf3f1f66cee3e6dbb87f35c523c08cc3` | 44678 | igual | herdado; só registro (não executado) |
| `resid.py` | `3e43ef78e0c82b3927ed5108facf18e5bc47307d6f2a5a0c266075e06d368082` | 481 | igual | herdado; só registro (não executado) |
| `review.py` | `a1c4f135e564a160e0d09a6347c04c218693fd506e67a6678f9549e7996180ff` | 690 | igual | herdado; só registro (não executado) |
| `rodar_tudo.sh` | `7240b344e38fc7f39d0066eaafb9b036d3c5bd0a00eb214f7a8e5988fa798924` | 1475 | alterado | runner |
| `sync_check.py` | `b828c4291295034480eda023081d9b399bdfe11398f611172cf21ccc41e4b7d6` | 2868 | igual | herdado; só registro (não executado) |
| `texts.py` | `c3ca12b7283710222c8baf681738b3d0e462207a30b81167d48e84be77bb0102` | 422 | igual | herdado; só registro (não executado) |
| `validar_erros.py` | `19ab9c8b359e4a59f209ecbca3e29f2ecc16a0dd5fb49b8892538bbe7eb8f33e` | 18500 | igual | passo 6 (módulo e CLI) |
| `validar_erros_teste.py` | `33132d5a9d9aaf7ec4bf645ae57b84eca9c2094abdc70f18d6970465278f0186` | 7993 | igual | passo 6 |
| `validate.py` | `7cde528368ee261693addfb8642ba3deac40fa5db36177eabdb27d493bb795f5` | 44115 | igual | herdado; só registro (não executado) |
| `validate_v19.py` | `49e0721d99ce0d0274c93c09792a0f738e0012ed2029e1d4fe580b3eff68a48f` | 14477 | novo | passo 4 |

## out/ (regerado a cada execução)
| Arquivo | SHA-256 | Bytes |
|---|---|---|
| `out/conferencias_stdout.txt` | `976ce924871eb53eace1ef671b45bdd0968f37aea26b6ab718c7696fa7757658` | 3012 |
| `out/conferencias_v19.json` | `07acda1fa6da55d2263fc792e904bd4f97166af2e53913148fefea00157c0ec5` | 4290 |
| `out/estudante_json.json` | `2f30bdb834646450f01776c35d74f3ccb84f6ec1991b62f7d8bb3b349e9305ae` | 9629 |
| `out/estudante_json_stdout.txt` | `d38dcc4871b853a48529cd870fcbd9af89bd8e08353a457fc04c6943630ca444` | 1670 |
| `out/gen_stdout.txt` | `7731875e3e0ea0728ce8bb0442e4a588302cbc77f768f24ddc7c9b1d0eac2c2b` | 299 |
| `out/pacote.json` | `1366055496457792bf55f541d901e2d1f277ee42611060b03bbf82b4427610bb` | 663235 |
| `out/pacote_estudante.json` | `8fa81b45a92095f8973c2787083d144869fdc195031455f7ff75ecb337e509e2` | 642374 |
| `out/registro_adendo1.md` | `801a0724462521e30f5fedcd4b1b8aef772491a2621c80e3a39e130aaaaf8df9` | 14248 |
| `out/registro_stdout.txt` | `0df2479b64c0a766a43cfa956dc12dd8d44fc389c0b960cd50b2e5abe4b25736` | 42 |
| `out/stats_v19.json` | `98bde429f04b857c5604563ce8879e406dc59e5d4c8713724886b4270bef9fba` | 42191 |
| `out/validar_erros_stdout.txt` | `b154f9f9b248ac3f3aecba63a464b1eb70e8524a4969eadf27c5477b3cc813c0` | 1578 |
| `out/validate_stdout.txt` | `52a27f50b741121f71b6952afc9ce4606f41fc237bb85b9ca13c2c23a9b42592` | 4080 |
| `out/validate_v19.json` | `383b746b9a39d2acdec21294643ce720a87c7e8dd7a8f3d58a8cb10fba0f7638` | 6284 |
| `out/casos_erros/importados_exportadoEm.json` | `ca039c0b82972681b9902b442e44867d80422f9b29b1c0ba8617e17abd25ad71` | 71 |
| `out/casos_erros/importados_sha.json` | `ea47a0919f69bded8a0115ab5d560b39a3deeed0319147e4e84b380261a5d8f7` | 134 |
| `out/casos_erros/incoerente_D.json` | `463a23847f577c0c5f6014bc6400cfed5c1cf41e480462faaab98a2de885ec22` | 1383 |
| `out/casos_erros/invalido_A_versaoFormato2.json` | `bae8aa0fc57ac23bd5e425c6b25e2e1c8370ce3921af88351a7be07e30687fcb` | 1383 |
| `out/casos_erros/invalido_B_campo_ausente_e_tipo.json` | `25fb6971761e1f39cb65b6bd1a48228bf5e942aa5e764e6ee41429a626a76b75` | 1180 |
| `out/casos_erros/invalido_C2_formato_errado.json` | `7a1540e0090f683a06902633167559b82660b066a51e61d94340e667b297eff9` | 1380 |
| `out/casos_erros/invalido_C_json_truncado.json` | `f3fa562491ffc9597ca41671a149f7bc0f739bdcd966743f05087a4eb15b4588` | 588 |
| `out/casos_erros/valido_ids_reais.json` | `7f9de859a354ee26d26c5f2f89a1ac6821f670bd6f957e41d4ad3bc37d553e87` | 1594 |

## Saídas promovidas ao repositório (cópia byte a byte de out/)
| Destino | Origem | SHA-256 | Bytes | Igual à origem |
|---|---|---|---|---|
| `saida/pacote/pacote.json` | `out/pacote.json` | `1366055496457792bf55f541d901e2d1f277ee42611060b03bbf82b4427610bb` | 663235 | sim |
| `saida/pacote/pacote_estudante.json` | `out/pacote_estudante.json` | `8fa81b45a92095f8973c2787083d144869fdc195031455f7ff75ecb337e509e2` | 642374 | sim |
| `saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo1_2026-10-18.md` | `out/registro_adendo1.md` | `801a0724462521e30f5fedcd4b1b8aef772491a2621c80e3a39e130aaaaf8df9` | 14248 | sim |

Resultado desta execução: validate_v19 47/47 OK; conferencias_v19 23/23 OK.
