# MANIFESTO — T-108 e T-109 — gerador v1.11 do pacote.json, do pacote_estudante.json e da edição .md (ENSAIO) — 2026-10-18 — gerado por gbq-csc (manifesto_v1_11.py)

Origem: cópia de `saida/pacote/gerador_v1_10/` (intacta; nenhum byte mudou), sem `out/` e sem `__pycache__/`, mais as mudanças da D1 da GBQ (`saida/pacote/T108_D1_pacote_M2_2026-10-18.md`). Base do pacote: o pacote.json v1.10 aceito, lido do git no commit `cacd606` (SHA-256 `d43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed`); itens, ids, ordem, enunciados, gabaritos, simulados e demais blocos não mudam. Mudam só as edições das tabelas de limpeza (registradas no campo `interno`), o `itemEdital` do L2-R16 (T-109), `nome` e `geradoEm`.

Modo desta execução: ALVO=M2; VERSAO=1.11; E_L2R16=True (ATO_L2R16 None); geradoEm 2026-10-18. ENSAIO: lê as tabelas de ensaio de `ensaio/` (linhas reais das Gerências onde passam nas conferências, mais linhas sintéticas); nenhuma saída é promovida; `saida/pacote/pacote.json` e `pacote_estudante.json` continuam a v1.10.

Condições de entrada da geração final ainda não cumpridas: E1-E3: SHA-256 da tabela GCE não fixado; E1-E3: SHA-256 da tabela GCB não fixado; E1-E3: SHA-256 da tabela GBQ não fixado; E4: ATO_L2R16 ausente.

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
| `conferencias_v111.py` | `a4cce62232fd399d126e19861bcee454a8c4dbd3fe33adb7776d5bf4de365212` | 16461 | novo | passo 7 |
| `conferencias_v18.py` | `097f61747ae108ebc1bfa77028cbc39dc33b4996424937bbe7311418218c4efd` | 108913 | igual | herdado; só registro (não executado) |
| `conferencias_v19.py` | `9c5acdd936c3d11eeb725761416c40049982902b6bd7934f7d3f52321c002bf8` | 11156 | igual | herdado; só registro (não executado) |
| `config_v110.py` | `0871b2d7af08f42540931e9ccc9e053a8bf4c07f22b2c198b79ccc83f229081b` | 1660 | igual | módulo (E_L2R131, ATO_L2R131 lidos por nucleo.py e estudante_json_v111.py) |
| `config_v111.py` | `3ceedbae4cedd404652f3738fe46360b7fc4c88982921172c462071dc832b150` | 4794 | novo | módulo (chaves da ocorrência; único lugar do número da versão) |
| `diff.py` | `a992af7d0bc1a5f587a99db51facf56412dbc99603148faf929132289b2a73b4` | 1786 | igual | herdado; só registro (não executado) |
| `diff2.py` | `88ec4bd7fd5df6587c547961b237cd49c572a7920f4e89fdd4bc8d5096becb60` | 1578 | igual | herdado; só registro (não executado) |
| `edital_p.py` | `76adfd601e8dbc4b7cea35f8a3538939e67b9307f65524cdae6dcf70d036d67e` | 1211 | igual | herdado; só registro (não executado) |
| `estudante_fidelidade.py` | `58e77d0274c256748e75277ae3811adc1e356ae4981c809d785774c4d9b06f99` | 27275 | igual | passo 2 (módulo: only_deletions) |
| `estudante_gen.py` | `16eed1bed5a3eccc8c5bae8516812b1806829c3cb8643178c47bfbcc2bddb8d0` | 17729 | igual | passos 2 e 4 (módulo: lote_of, lote_fund, COMPL, FUSAO) |
| `estudante_json.py` | `8dd215a4f33e32aeec66f5dd68cb401c7965106e0c7575dcc5623ea0c2c92688` | 21711 | igual | herdado; só registro (não executado) |
| `estudante_json_v111.py` | `6c521466f1188889acf39295bf5af5b995fc4c3ddf4d31808229a8dd77c97c55` | 24357 | novo | passo 2 |
| `estudante_marcas.py` | `598cfce4be4ffc30bb2817b54c25efdf26586eaef8b4be8fef1a522c4addbd8b` | 10065 | igual | passo 2 (módulo) |
| `estudante_md_v110.py` | `ee7ce49f45fa76ccf4baed7e505c46597f27462e8cef8ec271dac5aff4f3e6f2` | 6095 | igual | herdado; só registro (não executado) |
| `estudante_md_v111.py` | `895e498b3caf24d8e87c421c7800cb0be31268f8e81c6f297617dd4dbf776391` | 13304 | novo | passo 4 |
| `f4.py` | `084421fbea636c9264580ad8baef50e27778dcfb7cce6e23c6ac68b0fc7603b8` | 2597 | igual | herdado; só registro (não executado) |
| `fidelidade_mutacao.py` | `50cfb459b0210b205841e2527b98b0454976b62f114b349ace2b5ba93cf8f776` | 3989 | igual | herdado; só registro (não executado) |
| `fidelidade_mutacao_v111.py` | `4b3c6c95bebf864e15a52c896ce7d13359d680d2f407b2c4be5eba006e4eb00b` | 15117 | novo | passo 9 |
| `gce.py` | `ba575e4c66a0da2bba65c05fd8318378908ebaffbca5bc36b40a0640966d2417` | 6171 | igual | herdado; só registro (não executado) |
| `inventario_v111.py` | `16e3cf25ba053531e0c8db24a484d7bbe2095af53978f72d98190d491188a222` | 16988 | novo | passo 8 e módulo (posições dos casamentos; extensão aos .md) |
| `limpeza_v111.py` | `6f7303ef432a0fa00ab114c58a408908b7acfe98ab9d4357a6a2094d509b49ca` | 10199 | novo | módulo (aplicação ocorrência a ocorrência; `interno`) |
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
| `registro_alteracoes_v111.py` | `3d6643fe34aa7ecbdd46fc13d8b3e79b1a2e32302266e9502b411842f6f54b54` | 6856 | novo | passo 5 |
| `registry.py` | `b207f93606e5f5f9ded316f01cda586812416c36f6c97434a43ad8a12d653546` | 918 | igual | herdado; só registro (não executado) |
| `relatorio_R1.py` | `22b76c83b69311de7fffcd51ce5716a10b157dc34527d31ebee9bb98f45aae6c` | 19988 | igual | herdado; só registro (não executado) |
| `relatorio_v1_8.py` | `9ff7a0cea99488cbcb4a4bf00287cf23a8e31ec47f55479bf353292ba2000033` | 25389 | igual | herdado; só registro (não executado) |
| `report.py` | `53acb4c813e1f6be28bc1ec04395010c332811b0a47de20c01cc54dc9de4ea45` | 15932 | igual | herdado; só registro (não executado) |
| `report2.py` | `1e418a7d5908152b88161d394fb4729899793dd1a759b5f87875afe2da33afe8` | 45143 | igual | herdado; só registro (não executado) |
| `resid.py` | `21f636b5857e8082e37b269fdd905be5221c3c90bfc97b8acecdaf12d003c207` | 494 | igual | herdado; só registro (não executado) |
| `review.py` | `97ca017b42394314433bbe4a01c595948eb5c68da70b23afcb0c3a1cae6f2aaf` | 708 | igual | herdado; só registro (não executado) |
| `rodar_tudo.sh` | `cda6013ff968017ea65d384d356eccb8c83ad0e264920f099028b8304a783b2f` | 2123 | alterado | runner |
| `sync_check.py` | `c1804b93f20c30782bb4b04c82b49550d95a84687d584ca0a1e47cb682cc4592` | 2918 | igual | herdado; só registro (não executado) |
| `tabelas_v111.py` | `e365b56cf5a53262423e87f4a513f388eded73ded47838961e0db1319ac0d28d` | 11121 | novo | módulo (leitura e validação das tabelas, inventário e caminhos) |
| `texts.py` | `83353c975f401a62a2699a98f2ab7b2618d076ece0f7f4b4d26bdd7662fb2970` | 435 | igual | herdado; só registro (não executado) |
| `validar_erros.py` | `540dd6aabc9ecd3b1aee1d08176e8a06db0eac991984ee01d2929bc81616ab78` | 18764 | igual | passo 7 (módulo e CLI) |
| `validar_erros_teste.py` | `fe1202a3b4cabbac57c4376c4b489aa3f7f3274d16ef233bbd0fb1602336c998` | 8136 | alterado | passo 7 (C-15) |
| `validate.py` | `7da151a3ded9e3184f6265a383d27c5259f3275efbad76d802d37df5a3dd68d8` | 44517 | igual | herdado; só registro (não executado) |
| `validate_v110.py` | `8edf47de79481bd3a4b0f27d476abab1e09dc0eb8a5e1f25c47c5c8cbc5e54ee` | 16262 | igual | herdado; só registro (não executado) |
| `validate_v111.py` | `cf7dc8f0a8d244431956d6a1106e31253d3c449f37019162a99f92a0e4a03518` | 10610 | novo | passo 6 |
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

## out/ (regerado a cada execução; prévia do ensaio, nada promovido)
| Arquivo | SHA-256 | Bytes |
|---|---|---|
| `out/conferencias_stdout.txt` | `002591e94977dfb96b0fd58cca795e6752c7280c404e7f7161abfa338ce1dd63` | 4060 |
| `out/conferencias_v1_11.json` | `ee84b7db7fae82a98e931cc78c599fd0661564e6edb8b7ca9616a71c2573deb8` | 4884 |
| `out/ensaio_stdout.txt` | `d121efc584d075e1501233e0f2fc4a05f94b9b5a34bc34200d9978488bb3b926` | 373 |
| `out/estudante_json.json` | `46e2b1bdc5c0b94af24735732b59ca3b3984148702f5ebe4bbfdbb6e9617f6a7` | 23209 |
| `out/estudante_json_stdout.txt` | `91b8da3ab513c982d7c3d1735d86d627b3e5d92aafe9057d81431abe101846e4` | 2741 |
| `out/estudante_md_stdout.txt` | `c8ac62fadbb3e2e6278936d9c05209e4157f22600c3701a648ae3b0977c154d5` | 132 |
| `out/estudante_md_v1_11.json` | `6a7ec16210bd6984dc3f4e4a3d2d0b1ad835d9931a13559c60a1ec676f83bab9` | 31512 |
| `out/fidelidade_mutacao_stdout.txt` | `608885ec1daa9e31e3c4b1aa14a546d9834d62b8dbffe030e58dd7ef4e6bcb87` | 2856 |
| `out/fidelidade_mutacao_v1_11.json` | `dfadd51da29da099ac7d2076f92ffcc2c20f14ad3a70432001b27ba1821cfb22` | 5409 |
| `out/folhas_v1_11.json` | `8791434d61e21190cbddb8ef108211067c1930041a038d21f41b5c6bc21ca3b1` | 3257 |
| `out/gen_stdout.txt` | `ff5ce96d4ad51b0c978e49a7fb24138ae52cd89cd17e59d543d9c36a6c390f8d` | 395 |
| `out/inventario.csv` | `729a9cc8db535f9a0d4afee1a32d3f1f4d3a450379de20ecb7dd1c0d2acf1fe5` | 142822 |
| `out/inventario.json` | `77bb8a0a8c0184443036ba69c26bafb7eea489c7fc0eeba81c77268890bbf4a1` | 596 |
| `out/inventario_stdout.txt` | `d7065531536255fc8f7da50a885d9b4220cd4f9fe29072a3abb00808a74b4f8b` | 598 |
| `out/pacote.json` | `34c131e276b5b74a2cc4f30a9099a48cdbac231189f6e418415b5a41bed17c78` | 1114632 |
| `out/pacote_estudante.json` | `4f423e707631210c829cbb17511bcffee50c90bc1826da9686482df5bce1ee77` | 880331 |
| `out/registro_adendo3.md` | `5da45403400d54dbb89b260e003913a9b37e4220c79dbf04bf0aee073b7af46d` | 3920 |
| `out/registro_alteracoes_stdout.txt` | `e460e81b2c0119b201c09fb73265dd2db8b35f8540f7257235778e3396ee3a32` | 102 |
| `out/registro_alteracoes_v1_11.csv` | `910f201116f1fb994858cf1be8d491bceebf79dc19c32600f459e3a90bd8dfb0` | 288645 |
| `out/registro_alteracoes_v1_11_manter.csv` | `a985b8692c48dc874b3d75a73236fe95109f951d85798a990d823b097a9ac8ac` | 547 |
| `out/registro_alteracoes_v1_11_resumo.md` | `c8effbb0c060dc8406ecda925be3d571b24ab62f043d62346839c22067dd5bfa` | 5107 |
| `out/registro_stdout.txt` | `d96c206dbb5ad1fe30591148119a9b2e92e4aec6342f90640d136efe8e3a2003` | 92 |
| `out/stats_v1_11.json` | `b25fa706d2484d9f116e03af4af8c3cad3897bf8fef72966e8f70e68322d199a` | 4550 |
| `out/validar_erros_stdout.txt` | `a96eb28566ac456533bf65c5345e5f17422d6462619b7c90df97ddac36b29d2d` | 1578 |
| `out/validate_stdout.txt` | `c1b60ed3504217d4295a72798823d3f55da88ea65b84b48561510fce0cd43190` | 1996 |
| `out/validate_v1_11.json` | `5b3c19678d12b636ec77f3e798d7ddc2a814225ace59b056d6cf90fb4afb1ccf` | 2773 |
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
| `out/estudante/DISCURSIVAS_padrao.md` | `7805b84684f12e32d9e7b241c97af4137db4cba61c887c04770e76fd996b7577` | 31976 |
| `out/estudante/L1_estudo.md` | `5ca71cf9b411eb688b8fb317103a0c67c120682909bbcc021ca7ccecab79347f` | 39186 |
| `out/estudante/L1_gabarito.md` | `a80a63205ba5a434e3db55a4794f26cc00ce4acad97a4d9a1f8cb0a565060707` | 44222 |
| `out/estudante/L1_itens.md` | `f1efb02761da3382315e9c3e80910edb146c06f181a87255a7b1270fb9fd1f67` | 44578 |
| `out/estudante/L2_estudo.md` | `e60e2e9dac6fcfa62a48b1525b7db40790770f43348dd0083ed5954dd42ccf64` | 34521 |
| `out/estudante/L2_gabarito.md` | `f1750fd7ad8f7bdc07b584e72f3f1939db11fe8d9dd3bd1850136aa8eb3037e7` | 50070 |
| `out/estudante/L2_itens.md` | `9e0e3b1139ee9cbf799d708c42ffb2345b27cda2cde102a90e21e9411ac5a7b0` | 48961 |
| `out/estudante/L3_estudo.md` | `3a429d9c6bbd26c4ef5b512712e9afaa1a9d3026a10c6b3752737cf5e823e9a3` | 40471 |
| `out/estudante/L3_gabarito.md` | `9dac83f670351f72bcc4c9ae3cf57da6e1ebe597eead431aa57ffec97a3c824f` | 10007 |
| `out/estudante/L3_itens.md` | `0364d5f683db642c1e92b2b600de6c194e94d1456a53c911a3ed5cb91e0ef751` | 11220 |
| `out/estudante/L4_estudo.md` | `e4a9cef51da6dda1d2e2a9a18450618d87bfd792f412ec19989e819422af0e1e` | 54394 |
| `out/estudante/L4_gabarito.md` | `abda4dd5aa515ff0de48dbfadf377c5e3f8a04c47d7b90846ef0c2d9fe6283b6` | 15004 |
| `out/estudante/L4_itens.md` | `6bac01242ecd239589d5098c326d06a3cf08fe02f0fb099608a23ab7859751d2` | 6761 |
| `out/estudante/L5_estudo.md` | `5bc013bdd5a66564b919cf2b61450569a6530e721664c97147d8b1cb0fd1a4bc` | 33809 |
| `out/estudante/L5_gabarito.md` | `96b39703fda1647ccfaf8213306852eec9e3fd3ffedc6066bffae79ee5c8bd47` | 9641 |
| `out/estudante/L5_itens.md` | `a51ca726cd3331cc452bbf3d6c26b36a67204f87e562b5483e37cf8df3564678` | 7098 |
| `out/estudante/L6A_estudo.md` | `e0bfde9af8cdf1ac8ac4a6c010ef26685296a9dee6f58235f5ce2ce5f6ac1f89` | 49491 |
| `out/estudante/L6A_gabarito.md` | `0b0cdc856e7a450cd234b05c1c36a094874b8337c64762058c8855808bdbe56c` | 8211 |
| `out/estudante/L6A_itens.md` | `56d6fad58fd1cf88febc4f24509ecd9acfd4d473201999020e00fc05802f4e40` | 4206 |
| `out/estudante/L6B_estudo.md` | `d4dd07131c34bd44886e80aa56a959f3436c3f74fad61b2340fee4d770d2d8e0` | 58036 |
| `out/estudante/L6B_gabarito.md` | `1e25660998d4ac8139e92ac97b497c00da533a5e84e2f0a46ed4ae762394d074` | 8794 |
| `out/estudante/L6B_itens.md` | `e8e4baf9d7fb9aec02b8b8a67ae96820fa2b12e0b4aad962ae66f218a281b0ed` | 5052 |
| `out/estudante/NUCLEO.md` | `a61f095db8579354baf51c06052b8e9ae3f849d4429b1ed9c877c7e6ae0088ad` | 3933 |
| `out/estudante/README.md` | `bdb05cbe09489884490f3d22f3f2ad60f72400ba1453cba43695220ff59d3951` | 2564 |
| `out/estudante/SIM-0-P2_folha.md` | `f69efe607e7b575c246b46eded5ce15d5b6cf1e14ae755bc1bff23087c8bdab5` | 6063 |
| `out/estudante/SIM-0-P2_gabarito.md` | `cdd8a6588d0e24ebd4e445a50a7d11334e324eb4a85dbfd46b7babe0bbdcc081` | 5956 |
| `out/estudante/SIM-0_folha.md` | `50d509be3f26a93f5d2fe0d8739dd8e66c9c963ce5c0b88ccd35f1987298baaa` | 19465 |
| `out/estudante/SIM-0_gabarito.md` | `780a8f30abd0730cb5ca5945f2fc9456e94af2f0a1cd07ca2dcf947fc1a5f597` | 5986 |
| `out/estudante/SIM-1_folha.md` | `e0e21ea32da954f4d20ac9df23937dab412179873d28211876600e938c2b9a38` | 8625 |
| `out/estudante/SIM-1_gabarito.md` | `61d3ebad39cc2d231ea2cb392fb8329533d8746f0f86a6ff21dfa4bef02485e8` | 15352 |
| `out/estudante/SIM-2_folha.md` | `d576cc3fecc6f9973a028f82e303abb65aedd00ad14000cbc263c51423daaa92` | 9658 |
| `out/estudante/SIM-2_gabarito.md` | `71c8290b31732e0a83bac2aa881b5ed654dc6868c038b981d66beb1b761b024a` | 9567 |

Resultado desta execução: validate_v111 20/20 OK; conferencias_v111 17 OK, 3 PENDENTE, 0 FALHA; fidelidade_mutacao_v111 22/22 casos.
