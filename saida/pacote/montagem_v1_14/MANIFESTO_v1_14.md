# MANIFESTO_v1_14.md — T-123 (D1 da GBQ, passo 9 da seção 13) — 2026-10-23 — gerado por gbq-csc
Pacote v1.14 = v1.13 canônica (82c4117c…/04cbd593…) + 238 itens de reforço de DA + 36 itens de banco P1-DA, depois da limpeza da GCB (aceita pela reconciliação `saida/gcb/T123_limpeza_reconciliacao_GCB_2026-10-23.md`). Base: `saida/pacote/T123_D1_v1_14_2026-10-23.md`. Nada foi promovido a saida/pacote/, saida/estudante/, saida/gbq/ ou saida/plataforma/; sem commit; a plataforma não foi remontada. Scripts com `python -I`; `montagem_v1_13/` e `gerador_v1_12/` não foram alterados.

## 1. Valores esperados pela D1 e obtidos
| Item | Esperado | Obtido | Resultado | Onde na D1 |
|---|---|---|---|---|
| itens no pacote.json | 1433 | 1433 | OK | D1, 2.4 |
| C/E no pacote.json | 730/703 | 730/703 | OK | D1, 2.4 |
| itens de DA e C/E | 684 (350/334) | 684 (350/334) | OK | D1, 2.4 |
| itens de reforço e C/E | 238 (122/116) | 238 (122/116) | OK | D1, 2.1 |
| itens de banco P1-DA (novos) | 36 | 36 | OK | D1, 2.3 |
| parciais de reforço | 35 | 35 | OK | D1, 2.1 |
| VOLÁTEIS de DA (sem novos) | 5 | 5 | OK | D1, 2.4 |
| nucleo true no pacote_estudante | 775 | 775 | OK | D1, 6 |
| nucleo DA true/false | 408/276 | 408/276 | OK | D1, 6 |
| geradoEm posterior a 2026-10-20 | True | True | OK | D1, 4 (e) |
| conferencia_t123.json: FALHA e PENDENTE | 0 e 0 | 0 e 0 | OK | D1, 8.1 |
| mutacao_t123.json: detectadas | 15/15 | 15/15 | OK | D1, 8.3 |
| mutacao_t123.json: original com 0 FALHA | 0 | 0 | OK | D1, 8.3 |
| estudante_md_v1_14.json: arquivos e FALHA | 53 e 0 | 53 e 0 | OK | D1, 10 |
| cobertura_v1_14.json: FALHA | 0 | 0 | OK | D1, 9 |
| diag30_check_v1_14.json: FALHA | 0 | 0 | OK | D1, 11 |
| registro_adendo6.md sem "D<n>" isolado (scan_q) | 0 | 0 | OK | D1, 5 (achado 4) |
| regras/pacote_contrato.md (v1.2.12) SHA-256 LF | 3916ad994cd06ee74b13ba545de5af3b6c241d0004eb0625e922973ab76c38df | 3916ad994cd06ee74b13ba545de5af3b6c241d0004eb0625e922973ab76c38df | OK | D1, 7 |
| DA_reforco_substituicoes.csv SHA-256 LF | df9f53bd7dc3f18631c77528b32683dd89e77e27dea167918fd1edee014db501 | df9f53bd7dc3f18631c77528b32683dd89e77e27dea167918fd1edee014db501 | OK | reconciliação da GCB, 3 |
| DA_reforco_registro_formato.md SHA-256 LF | a511fd8d3b79b806dc3a87f06d294ed346d05f2d05766089b80103d6374b820e | a511fd8d3b79b806dc3a87f06d294ed346d05f2d05766089b80103d6374b820e | OK | reconciliação da GCB, 3 |
| montar_v1_13 (pasta) e gerador_v1_12 sem modificação no git | [] | [] | OK | D1, 4 e 8.1 |
| montar_v1_14.py | RESULTADO: 0 FALHA | `python -I montar_v1_14.py` saiu com código 0 e as conferências internas OK (rodado antes deste manifesto) | OK | D1, 13, passo 4 |

## 2. Saídas principais (bytes e SHA-256)
| Saída | Bytes | SHA-256 |
|---|--:|---|
| `out/pacote.json` | 3194690 | `070bc237fcc7371a23365f6e66c9341cf5c0aee08ad9206a9f7be6c06150d495` |
| `out/pacote_estudante.json` | 2930776 | `6b56a7f8a1c7c42a01e145b0da35ab48691496fde82d2a9ee8fd4a6ff195b9ab` |
| `out/registro_adendo6.md` | 16428 | `74855f037108303454990e27f45447bac0a0d4322bda75a944dd00ce1c37970b` |
| digest da edição .md (forma R2-D: linhas `estudante/<nome>.md` TAB sha256, em ordem de bytes, com `\n` final; SHA-256 desse texto) | — | `f9c1c0651e9fb50009220d5424d441f99ba5fb93e46164fe4d900de0c010916b` |

## 3. Contagens
- Itens: 1433 (C/E 730/703). Itens de DA: 684 (C/E 350/334), dos quais 238 de reforço, 36 de banco e 410 dos lotes de estudo.
- Reforço do lote D1: 12 (C/E 6/6); vagos: D1-R03.
- Reforço do lote D2: 80 (C/E 40/40); vagos: nenhum.
- Reforço do lote D3: 89 (C/E 49/40); vagos: nenhum.
- Reforço do lote D4: 57 (C/E 27/30); vagos: D4-R12.
- `nucleo`: 775 true no pacote_estudante (367 fora de DA + 408 de DA); os 12 itens da v1.13 que passam a false e os 18 de reforço estão em conferencia_t123.json (C-ESTUDANTE.nucleo_12 e nucleo_18).
- Cobertura: 75 folhas; DA com 644 itens em folha e 40 fora; 12 folhas de DA abaixo de 20 (faltam 118 para 20).
- Moldura (D-MOLDURA-CE, recontagem oficial): P1-TI 7 itens (C 4, E 3, %C 57.1); P2 208 itens (C 112, E 96, %C 53.8); P1-DA 94 itens (C 50, E 44, %C 53.2); TOTAL 309 itens (C 166, E 143, %C 53.7); divergências do campo "Moldura:" das levas: 0 de 238.
- Conferência: 99 critérios, 99 OK, 0 FALHA, 0 PENDENTE; por grupo: C-SHA {'OK': 19}; C-INTACTA {'OK': 13}; C-TOTAIS {'OK': 11}; C-REFORCO {'OK': 9}; C-JUST {'OK': 2}; C-MARCAS {'OK': 4}; C-BANCO {'OK': 8}; C-ESTUDANTE {'OK': 9}; C-FOLHAS {'OK': 6}; C-DIAG30 {'OK': 4}; C-MOLDURA {'OK': 4}; C-MD {'OK': 9}; C-MANIFESTO {'OK': 1}.

## 4. Arquivos desta pasta (bytes e SHA-256; o manifesto não lista a si mesmo)
| Arquivo | Bytes | SHA-256 |
|---|--:|---|
| saida/pacote/montagem_v1_14/T123_ocorrencias_DA.csv | 18072 | 3ca0b82e16c7ae01808c942386876aca0bf6f717c7103c89be9126eb7e076486 |
| saida/pacote/montagem_v1_14/T123_ocorrencias_DA_resumo.md | 3195 | 59d62723eb78715f04289053c0515d430b12292503c31f5697c757337151c724 |
| saida/pacote/montagem_v1_14/cobertura_v1_14.py | 9091 | 0a6ae7589934fb6641fd42f4913646f5f3d070857651d92be6621b45b05667ee |
| saida/pacote/montagem_v1_14/conferir_t123.py | 39076 | e16eeb617b80c269dfe79c9560c24c022cd61e86021ba8990a61174f011ed39b |
| saida/pacote/montagem_v1_14/contrato_v1_2_12.py | 7306 | 5dc4d68529c6f642a2b212fd03c34a889f85db1a035bce5e90a29ccd3c5eeceb |
| saida/pacote/montagem_v1_14/diag30_check.py | 4228 | e29f46cc04f87095b29a24a9503b77b279eef87967003a8d28d5e1b48f9b0308 |
| saida/pacote/montagem_v1_14/estudante_md_v114.py | 18721 | 6d534cbeff605ff5c8b0c8894f42558e9c3a5de39155345d4cb42c0b7260cc47 |
| saida/pacote/montagem_v1_14/extrair_reforco_da.py | 27313 | 2ff0354bcc7cbb033fff3d34cc3a1031b543b0a247f3cfb0db058cdbea179ac8 |
| saida/pacote/montagem_v1_14/manifesto_v1_14.py | 13244 | 0c2276abd337ed4a5568ab66de780adc34b012b48c4332cd66a292841eac2903 |
| saida/pacote/montagem_v1_14/marcas_v114.py | 4274 | 866b297e1071e3d3d6b6bbde4dea736dd4eef4510a01514dd0b922043c13a61d |
| saida/pacote/montagem_v1_14/moldura_v1_14.py | 6653 | 37dc847e5b6a15c3fbbed41f51bc605848b5f58db34420962fd8f57efd0251b3 |
| saida/pacote/montagem_v1_14/montar_v1_14.py | 15258 | 302db35f03026a275d5745fbf611892b1d23b4faac2fbadc5af9aeb2dc6d5f26 |
| saida/pacote/montagem_v1_14/mutacao_t123.py | 8531 | b73b841c78f313401525b82a8b0b1d352ac9df978e68ca2187b0582aa8a5caf0 |
| saida/pacote/montagem_v1_14/nucleo_v114.py | 4485 | a3464c74dcd7e6aa402b8a2b410a910dbfe9725b2cad24279d58cdb5e02593a4 |
| saida/pacote/montagem_v1_14/out/cobertura_v1_14.json | 31146 | 19d26f9a7d43ab482b91090cb7e4589edc1e3a3fb1cb1bc4ff18c1e1365345cc |
| saida/pacote/montagem_v1_14/out/conferencia_t123.json | 43587 | 4dc21e584ad985e454188d80efbab81a4d80af08e39de014d74eb639aaa69b2f |
| saida/pacote/montagem_v1_14/out/diag30_check_v1_14.json | 4809 | 02c1f7a5ceae97d1544cce4d7e36f4ea0e4349d0f13e3ae65b6159fa33da5f6b |
| saida/pacote/montagem_v1_14/out/estudante/BANCO_gabarito.md | 12124 | 253b6291e63da0cd914cb097ffe15373076560eb8272a7aadef43d69a81d2f6f |
| saida/pacote/montagem_v1_14/out/estudante/BANCO_itens.md | 100223 | 2535197eccad20d9f9d1caee1e5526b0bdf41dfcf06de13ffcac8a1877a63ca4 |
| saida/pacote/montagem_v1_14/out/estudante/DA_D1_estudo.md | 71783 | bbab97c4ba4cb970aa79d7ae962e6434bf1c0c0a83a2d7dd93bfe17155a7a570 |
| saida/pacote/montagem_v1_14/out/estudante/DA_D1_gabarito.md | 25122 | 1399cd8cf1bb4b8f21eb300e8bff113eac53cfbe8bf427b8a4c3293e5b1c2edb |
| saida/pacote/montagem_v1_14/out/estudante/DA_D1_itens.md | 16969 | b870ecbb4513b408f79a4203122a3dc6846c81ae7ad3f80dcfcd1678db886738 |
| saida/pacote/montagem_v1_14/out/estudante/DA_D2_estudo.md | 322779 | 7518e6b27bada606ecf8c7f5bb748387eebe8743a8b2215ffb84fb8c1e642e44 |
| saida/pacote/montagem_v1_14/out/estudante/DA_D2_gabarito.md | 69071 | 56d3886cfaf37235ee45a37e13b5bd151a7849ec2eb3832cd02299e6e6415efc |
| saida/pacote/montagem_v1_14/out/estudante/DA_D2_itens.md | 40975 | 3ff5c06f76ea858d880c08a8a2b175b2e4c2afc2408e20776b1bab9842ee4f6f |
| saida/pacote/montagem_v1_14/out/estudante/DA_D3_estudo.md | 160728 | 7301bb18a32c076feacdf5abe7ae9289182a93fd82756358bbc554f3a72e5e6c |
| saida/pacote/montagem_v1_14/out/estudante/DA_D3_gabarito.md | 68120 | 733d6657d66aca809775084754fbaa9309df109ada5578dfa6c1dda2903da1fc |
| saida/pacote/montagem_v1_14/out/estudante/DA_D3_itens.md | 41611 | 4c998cc16c6ec9a512e938b1f27fd9763d70d3d4d21d7887b5b0ddb48d75ff8e |
| saida/pacote/montagem_v1_14/out/estudante/DA_D4_estudo.md | 166485 | 6386186b19341f95a0b6dd473faef452153dbd16859b0c0171d352badcfde839 |
| saida/pacote/montagem_v1_14/out/estudante/DA_D4_gabarito.md | 56800 | 8b4d301308010f88470d9ecafd32839702c7eefe394bf5c2ac84137439aad5bf |
| saida/pacote/montagem_v1_14/out/estudante/DA_D4_itens.md | 37794 | 74a714b9e3a98d35eebb67d690d1f3f269ce386fd16992dd59b8d7297fb4e23c |
| saida/pacote/montagem_v1_14/out/estudante/DA_D5_estudo.md | 211320 | 00784bbcf9a1771c02b706d83b2fe2c8213ce0e416f33b6b6a1b32595a42d65f |
| saida/pacote/montagem_v1_14/out/estudante/DA_D5_gabarito.md | 24462 | f84ef589bf4bac7852dff70adf85d76daeaaf170b60892e20df5d5219fdce09a |
| saida/pacote/montagem_v1_14/out/estudante/DA_D5_itens.md | 18961 | 538f74c5a6822f07bccae02e3bc3f9d0b2dde9e8ab0f6e9a3ca14722eb9ceda3 |
| saida/pacote/montagem_v1_14/out/estudante/DA_D6_estudo.md | 131726 | c849c448c84cbcb9810eff970b01b577e88d12703049186f94d0872fff0f4988 |
| saida/pacote/montagem_v1_14/out/estudante/DA_D6_gabarito.md | 17334 | 8b4878363a6f0d0c907d9aa8109a385b6ac01594c8f462ceb0fa9d66d2479676 |
| saida/pacote/montagem_v1_14/out/estudante/DA_D6_itens.md | 12227 | 1f37c2f95d1986f469ab591334a868729911dbdfa63d6be485a140cf825a593b |
| saida/pacote/montagem_v1_14/out/estudante/DISCURSIVAS.md | 6694 | 7777c52ca635cdd0e33a525aadd3b86699d333def9bb61816c79b67653f17bd0 |
| saida/pacote/montagem_v1_14/out/estudante/DISCURSIVAS_padrao.md | 32002 | 4d5a4e6e9cb23fffee9b401f7b8b9537ce9475cdc8127e34cd27c6592f77dcb4 |
| saida/pacote/montagem_v1_14/out/estudante/L1_estudo.md | 55866 | 12ebe1ac46ce54b2d2f53dfce680e90c235ed6f1743bbb7d41b836e4247dda7f |
| saida/pacote/montagem_v1_14/out/estudante/L1_gabarito.md | 69895 | 2947f638e5f9f1a08133716a7bb3b4d6f961330aa87dc5fc9d5252bec363cf7a |
| saida/pacote/montagem_v1_14/out/estudante/L1_itens.md | 70462 | 94e106e720f28ace0fedabb9e5050ee018e2e5147cef926700cff45929325050 |
| saida/pacote/montagem_v1_14/out/estudante/L2_estudo.md | 48933 | 4b3d27b2ea186da1d97d9571608d36f00160696d450b2f2e9c193258d3346d3c |
| saida/pacote/montagem_v1_14/out/estudante/L2_gabarito.md | 53394 | 7aa74384f5dd7e5bac2f49dc3d6b50af0322ccc10ba07cfcd0a41f9cb166d2b4 |
| saida/pacote/montagem_v1_14/out/estudante/L2_itens.md | 52495 | 9bb73429f2a9e29713c49247a61b58b1c4537aeac3850a47e3c698af5ffe7924 |
| saida/pacote/montagem_v1_14/out/estudante/L3_estudo.md | 54586 | a6ea08ad469fb819db5bfb8609ad2ec3f436f62fddb049a3277669bb0e61435d |
| saida/pacote/montagem_v1_14/out/estudante/L3_gabarito.md | 38836 | 5a2516422ebb27293f0a337fcae04ad539de3122e6e9c97c0cfdfd450028ce92 |
| saida/pacote/montagem_v1_14/out/estudante/L3_itens.md | 41600 | b4ca1f7707a5789eb1750caa833d9a4d6a60d930642dc4908065e2b128bf2281 |
| saida/pacote/montagem_v1_14/out/estudante/L4_estudo.md | 64066 | 7f9bedfcc79f896c0b3ed162474649b5d6c021f9bc43767752bac98438bacf27 |
| saida/pacote/montagem_v1_14/out/estudante/L4_gabarito.md | 17579 | 66f95d58f2154763b7b362ee0ae426d3e86b6fa472c081a863716cf488aa5575 |
| saida/pacote/montagem_v1_14/out/estudante/L4_itens.md | 8920 | 6620555a3b368b66c1ca21a2ebc1faf9a2515016e747d64acf567d6a523c6545 |
| saida/pacote/montagem_v1_14/out/estudante/L5_estudo.md | 45121 | 50abca622f917d20406241ded6fccd576c55683e30c5a7b4ff29931c351ac5e2 |
| saida/pacote/montagem_v1_14/out/estudante/L5_gabarito.md | 9627 | bbd753e15773894ad70c20b11286f3d5b7b440635ca7ce47b5d8409c344703bc |
| saida/pacote/montagem_v1_14/out/estudante/L5_itens.md | 7115 | e110570384225bda943dd709e1a4272faa6581b94eadad6ebf6f42fc488afaa3 |
| saida/pacote/montagem_v1_14/out/estudante/L6A_estudo.md | 56408 | 8ae7516d4b409f7944c81cb879b9941f1621a5d0bfab5eaca31ac3bb3e9f2065 |
| saida/pacote/montagem_v1_14/out/estudante/L6A_gabarito.md | 8055 | c2fab83b8520fbb20427647236a51c51103cbb7dc92389c07eb472ee955a995a |
| saida/pacote/montagem_v1_14/out/estudante/L6A_itens.md | 4206 | afa0a0e333ff7ac2d4857ee80e72142a8825befb417832c15921f1663ff31b1e |
| saida/pacote/montagem_v1_14/out/estudante/L6B_estudo.md | 70677 | 3a5c7eca9a7f507a976422b2ef2e36b388d371a8e352897919c7720466c7c4c8 |
| saida/pacote/montagem_v1_14/out/estudante/L6B_gabarito.md | 8767 | 8b23a83303888f821334d100186648807ae6562a4a683f11d88cb9f988798b91 |
| saida/pacote/montagem_v1_14/out/estudante/L6B_itens.md | 5089 | cac479bf65a9d8fc9e8d94822eed87e8f6b0257cf49c2028dab6f43873565077 |
| saida/pacote/montagem_v1_14/out/estudante/NUCLEO.md | 8103 | 0ee0016e21c3ad05908d5f15d3bad81518cae701507ce72883c33af26e5c0e8d |
| saida/pacote/montagem_v1_14/out/estudante/README.md | 4610 | dd3c4fc26cb6cc810958ebf28b9d20ab7b18797704ab8527009052ce505b82c5 |
| saida/pacote/montagem_v1_14/out/estudante/SIM-0-P2_folha.md | 6063 | f69efe607e7b575c246b46eded5ce15d5b6cf1e14ae755bc1bff23087c8bdab5 |
| saida/pacote/montagem_v1_14/out/estudante/SIM-0-P2_gabarito.md | 5956 | cdd8a6588d0e24ebd4e445a50a7d11334e324eb4a85dbfd46b7babe0bbdcc081 |
| saida/pacote/montagem_v1_14/out/estudante/SIM-0_folha.md | 19458 | 7ef04f37578a2da082ab8c016ac06a06e8463db96089c268cd7e9b100815cd16 |
| saida/pacote/montagem_v1_14/out/estudante/SIM-0_gabarito.md | 5979 | 2df79ffa2501e38c66564a8b2a23cd5632372255bf7214c9179ca8ece3788374 |
| saida/pacote/montagem_v1_14/out/estudante/SIM-1_folha.md | 8625 | e0e21ea32da954f4d20ac9df23937dab412179873d28211876600e938c2b9a38 |
| saida/pacote/montagem_v1_14/out/estudante/SIM-1_gabarito.md | 15085 | 17b0de7a1e3e34943dfeffe91fdfb1f746bcabffbe6c976516e6623a4ad84c96 |
| saida/pacote/montagem_v1_14/out/estudante/SIM-2_folha.md | 9658 | d576cc3fecc6f9973a028f82e303abb65aedd00ad14000cbc263c51423daaa92 |
| saida/pacote/montagem_v1_14/out/estudante/SIM-2_gabarito.md | 9565 | 2113d4a7c1e399a1ce25b71d5819fe565121d3fc41c9a4d4c2b3e3e75e248c9e |
| saida/pacote/montagem_v1_14/out/estudante_md_v1_14.json | 23530 | 693e96a70beb037e7d3d919694d3568ab115232f4350a211a25c17b642b1cd49 |
| saida/pacote/montagem_v1_14/out/extracao_t123.json | 7229 | d9d97df3d902e1e05bcac513524a432dd460ae2fc211a78efb4162bd4554db2f |
| saida/pacote/montagem_v1_14/out/moldura_v1_14.json | 10417 | f46004c88be1c07872a617633e57cd6e7ccf2e7e3758eb1810c28a48d28f4edf |
| saida/pacote/montagem_v1_14/out/mutacao_t123.json | 4886 | e502f0ecfb5e6444a64da5823e25f8b40bf849cbfe6e4856a63165d15d528483 |
| saida/pacote/montagem_v1_14/out/pacote.json | 3194690 | 070bc237fcc7371a23365f6e66c9341cf5c0aee08ad9206a9f7be6c06150d495 |
| saida/pacote/montagem_v1_14/out/pacote_estudante.json | 2930776 | 6b56a7f8a1c7c42a01e145b0da35ab48691496fde82d2a9ee8fd4a6ff195b9ab |
| saida/pacote/montagem_v1_14/out/reforco_bruto.json | 299261 | 87264c2f3f1dc5447127bba6757b5b31432e85beb0a743fac4e304589adee497 |
| saida/pacote/montagem_v1_14/out/reforco_marcas.json | 56742 | d0dfd959230ac0d013b11dba8c208b60bfe113b46885a61f82d808dd93b172a4 |
| saida/pacote/montagem_v1_14/out/registro_adendo6.md | 16428 | 74855f037108303454990e27f45447bac0a0d4322bda75a944dd00ce1c37970b |
| saida/pacote/montagem_v1_14/out/registro_alteracoes_v1_14.csv | 74200 | 56a7a90d6434ea0d4dbaab9fd73d68cf1040500e6c0afbe62ad17b6b637b3abc |
| saida/pacote/montagem_v1_14/out/registro_alteracoes_v1_14_resumo.md | 1371 | 61e12fbe859df70e3eb5c7c45583bb0fd6c20654c2736d68d22b7d3b5659de68 |
| saida/pacote/montagem_v1_14/registro_adendo_v114.py | 15987 | 4b658cc5f133fe789079d69ecefa5452d55f0439a107a10d99361524df5e92c0 |
| saida/pacote/montagem_v1_14/registro_alteracoes_v114.py | 5584 | c657dc536528b14741fef0ca4c01b257d7e056076f34229a14e1e750836a9d1e |

Total: 83 arquivos em montagem_v1_14/ (dos quais 53 em out/estudante/), contados na pasta real. Nenhum arquivo fora desta pasta, salvo o registro do contrato `saida/pacote/contrato_v1_2_12_2026-10-23.md` e a errata em `regras/pacote_contrato.md` (passo 5).

## 5. Entradas lidas (SHA-256 do conteúdo LF)
| Entrada | SHA-256 |
|---|---|
| saida/pacote/montagem_v1_13/out/pacote.json | 82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240 |
| saida/pacote/montagem_v1_13/out/pacote_estudante.json | 04cbd593fdd30404ecb7f91f6b6722da6b2fc24e58d3c0eb68b10a4e792a0c40 |
| banco/banco.csv | b1c1588f8b4a80a233e7b8d485992d07e9adeb2570fb2343573ab7fde9a5721f |
| saida/gcb/DA_plataforma/DA_reforco_substituicoes.csv | df9f53bd7dc3f18631c77528b32683dd89e77e27dea167918fd1edee014db501 |
| saida/gcb/DA_plataforma/DA_reforco_registro_formato.md | a511fd8d3b79b806dc3a87f06d294ed346d05f2d05766089b80103d6374b820e |
| saida/gcb/DA_plataforma/FORMATO_PLATAFORMA_DA.md | f3fd4667af5b1c0ad8d8ef9e21259074599a3f09b7c3610f36923de029d75068 |
| saida/pacote/montagem_v1_14/out/reforco_bruto.json | 87264c2f3f1dc5447127bba6757b5b31432e85beb0a743fac4e304589adee497 |
| saida/gcb/DA_reforco_leva1_v2.md | 2c431529a5440d4a2bf2bb617bc75d496949dff28a824e0215322d00d79a4f04 |
| saida/gcb/DA_reforco_leva2_v2.md | 5baec20d81eea47f50e79275375668284d58ff5649f85a06c37552cd0f161bbe |
| saida/gcb/DA_reforco_leva3_v2.md | e4c2a91191b4e5b3180317ce28653514a438896929291168c83b3a2c4a513237 |
| saida/gcb/DA_reforco_leva4_v2.md | 57203ae3a68042012989b549d19f2dbd5703623b5de3619275b3f05a2f8338da |
| saida/gcb/DA_reforco_leva5_v2.md | b531014bcf2cf158890ffa4293062e796e505151a57dced14e8462875a8f81c4 |
| saida/gcb/DA_reforco_leva6_v2.md | 0b8ccd4d07bf7d97cb9c1728c6bf4c18e3c5f7c9ac557e27f4537c068c96090b |
| saida/gcb/DA_reforco_leva7_v2.md | c4f50b9ecabb3f0c99592d4bd997012b647a2b6b5b10ab5521eece385fe1f764 |
| saida/gcb/DA_reforco_leva8_v2.md | 1fdce9bde3393b445cabd75d50064fb2a2fdde103c03415dc82256c203bf6f2c |
| saida/pacote/T123_D1_v1_14_2026-10-23.md | 1e3da24ccae03150ecdbbb0ffba520da9df9cccac50b8539f46ab0443927413c |
| saida/gcb/T123_limpeza_reconciliacao_GCB_2026-10-23.md | 19ec015da8ae890160fd8c878e67313c001c48c6011172bdbb6b77b4b9304cb8 |
| saida/gcb/T123_substituicoes_DA_v2.csv | de63b7c524797723c46690b45082d243583895846fdc144c11da8e2bfe233bde |
| saida/gcb/QA_T123_limpeza_R2_2026-10-23_gcb-cqfp.md | 70c9e86d1f4d82cdcf9e26c1bc0095050b5e4a82bf1300d2bda61692a4672757 |
| saida/pacote/gerador_v1_12/marcas_processo.py | 7ee30de455a5c0332aca1dae2148d7670eb86bac08294f0c61a80da4484cc140 |
| saida/banco/moldura_ce.py | 5723698e9a718b106a523cac6774f3ed5f23f39a09e9a0d02fd59ecf9ddcca96 |
| saida/pacote/montagem_v1_13/out/diag30_DA.json | eb1ced6df3d624ae62b82337db6a4cfe29b86baa9494e96aed1b3defe61a6800 |
| saida/plataforma/plataforma_v16_final_template.html | c6de3f2a699597e124540eb4a59f451938ba44da9fa9c86d2a6e4b9d5fc0b46c |
| edital/DA_itens_1_12_P1.md | f9e8ba916e94ee3fc58d83912bac96994263a91e483fcad0aed0ad2466ed6f4e |
| DECISOES.md (linhas 93, 117, 162 a 165, 175 a 179, 181, 182, 184 e 185 conferidas pelo nucleo_v114.py) | f3c80535eb657a8145f20cc01fd0da32937a284e98d52a078e8bb1ef7e3e7966 |
| regras/pacote_contrato.md (antes: 85b30fcc…616b; depois) | 3916ad994cd06ee74b13ba545de5af3b6c241d0004eb0625e922973ab76c38df |
| saida/estudante/ (v1.13-E promovida) e montagem_v1_13/out/estudante/ (53 .md) | iguais em LF (estudante_md_v114.py, M0.2: OK) |

## 6. Divergências e observações (nenhum valor foi ajustado à força)
1. Valores esperados pela D1: nenhuma divergência (seção 1: tudo OK).
2. Lista X de conteúdo da varredura PROCESSO: "Presidência da República" no D2-R21 e no D2-R24 (justificativa; remissão à Lei 9.007, art. 2º, parágrafo único), 1 casamento em cada, registrada como conteúdo por pedido da reconciliação da GCB (seção 4, P1). Fora isso, C-MARCAS e PROCESSO dão 0 nos 274 itens novos.
3. Ordem de execução: `conferir_t123.py` roda depois dos scripts 6 a 11 (usa os arquivos que eles gravam) e é refeito depois deste manifesto, para que o C-MANIFESTO compare a pasta real com ele; este manifesto é regerado então, para listar o SHA-256 final da conferencia_t123.json. A conferencia_t123.json não entra na comparação do C-MANIFESTO (não pode conter o próprio SHA-256).
4. A "Onda programada" de P1 (ressalva (d) da cobertura v1.13) não é calculável pelo pacote: o cobertura_v1_14.json a deixa para a secretaria, que a reconstrói de TAREFAS.md.
5. Leitura: todo insumo de texto é lido como bytes com CRLF→LF antes do decode, porque a árvore de trabalho tem `core.autocrlf=true`; os SHA-256 desta tabela de entradas são os do conteúdo LF. Os arquivos de out/ são gravados com LF (0 CR).
6. AJ-L8-E3 (D4-R42) e AJ-L8-E4 (D4-R52) sem aceite: o "antes" de cada uma continua 1 vez no enunciado (C-REFORCO.e3e4). BQ-0141 (QA PENDENTE) e BQ-0151 (DIVERGE) ficam fora (C-BANCO.ausentes). O pacote v1.14 não foi promovido nem publicado.
