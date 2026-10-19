# MANIFESTO — T-115 — gerador v1.12 do pacote.json, do pacote_estudante.json e da edição .md (GERAÇÃO FINAL) — 2026-10-18 — gerado por gbq-csc (manifesto_v1_12.py)

Origem: cópia de `saida/pacote/gerador_v1_11/` (intacta; nenhum byte mudou — conferência C-G1), sem `out/`, `__pycache__/` e `ensaio/`, mais as mudanças da D1 da GBQ (`saida/pacote/T115_D1_v1_12_2026-10-18.md`). Base do pacote: o pacote.json v1.11 canônico (D-PACOTE-V111), lido do blob do commit `fe17830` (SHA-256 `1b5657c726b5852885fe0e69e7835d6ec331e6d43dd19191cf451ff4ac069517`, 560 itens). Mudam só: os 189 itens novos (onda 4 do reforço, onda 1 da ORDEM_V15_F P1 e P2) com as 3 erratas de enunciado e a limpeza L-1 a L-5 (campo `interno`), as 73 pegadinhas de pares, `topicos` (40 resumos, 3 pilotos), os nomes de lote e do SIM-0 sem código de produção, a `legendaMecanismo` não emitida, `nome` e `geradoEm`.

Modo desta execução: VERSAO=1.12; geradoEm 2026-10-18; FINAL=True. GERAÇÃO FINAL: nenhuma saída é promovida por este gerador (a promoção é ato separado, depois do aceite da fidelidade).

Pendências da geração final: nenhuma.

## Pipeline (`sh rodar_tudo.sh`; cada passo com `python -I -B _run.py <script>`)
| Passo | Script | Saída |
|---|---|---|
| 1 | `build_v112.py (com reforco_v112.py, topicos_v112.py, pegadinhas_v112.py, limpeza_v112.py)` | `out/pacote.json`, `out/stats_v1_12.json`, `out/folhas_v1_12.json` |
| 2 | `estudante_json_v112.py (com nucleo.py)` | `out/pacote_estudante.json`, `out/estudante_json.json` |
| 3 | `registro_adendo_v112.py` | `out/registro_adendo4.md` |
| 4 | `estudante_md_v112.py` | `out/estudante/` (35 arquivos), `out/estudante_md_v1_12.json` |
| 5 | `registro_alteracoes_v112.py` | `out/registro_alteracoes_v1_12.csv`, `_resumo.md` |
| 6 | `validate_v112.py` | `out/validate_v1_12.json` |
| 7 | `conferencias_v112.py` | `out/conferencias_v1_12.json`, `out/similaridade_v1_12.csv`, `out/casos_erros/` |
| 8 | `inventario_v112.py` | `out/inventario.csv`, `out/inventario.json` |
| 9 | `fidelidade_mutacao_v112.py` | `out/fidelidade_mutacao_v1_12.json` (bloco M) |
| 10 | `manifesto_v1_12.py` | este `MANIFESTO.md` |

## Contagens conferidas contra os arquivos canônicos (D1, instrução 5)
- Itens: 749 (560 + 189); C/E 380/369; novos 189 (onda 4 84; F1 P1 7; F1 P2 98).
  - ONDA4 (D-T98-ONDA4-ACEITE): n 84, C 42, E 42, [TS] 61, VOLÁTEIS 10, PARCIAIS 6; por folha {'P2-3.1': 14, 'P2-3.2': 14, 'P2-3.3': 14, 'P2-3.4': 14, 'P2-4.2': 14, 'P2-4.3': 14}.
  - F1P1 (D-V112-BAEF-P1-ACEITE): n 7, C 4, E 3, [TS] 3, VOLÁTEIS 0, PARCIAIS 0; por folha {'P1-5.2': 7}.
  - F1P2 (D-V112-BAEF-P2-ACEITE): n 98, C 49, E 49, [TS] 49, VOLÁTEIS 22, PARCIAIS 0; por folha {'P2-1.1': 9, 'P2-1.2': 10, 'P2-1.3': 10, 'P2-1.4': 10, 'P2-1.5': 10, 'P2-1.6': 10, 'P2-1.7': 10, 'P2-1.8': 10, 'P2-2.1': 7, 'P2-2.2': 1, 'P2-2.8': 1, 'P2-3.1': 6, 'P2-4.1': 4}.
- Folhas que mudam (total v1.11 → v1.12, C/E, diretos, PARCIAIS, VOLÁTEIS; seção 8 da D1): P1-5.2 23→30 16/14 29/1 0; P2-1.1 20→29 13/16 29/0 1; P2-1.2 20→30 16/14 30/0 0; P2-1.3 20→30 15/15 30/0 6; P2-1.4 20→30 15/15 30/0 6; P2-1.5 20→30 16/14 30/0 6; P2-1.6 20→30 13/17 30/0 6; P2-1.7 20→30 14/16 30/0 6; P2-1.8 20→30 16/14 30/0 2; P2-2.1 20→27 15/12 17/10 5; P2-2.2 20→21 10/11 14/7 1; P2-2.8 19→20 9/11 19/1 4; P2-3.1 7→27 13/14 22/5 5; P2-3.2 6→20 10/10 20/0 1; P2-3.3 6→20 10/10 18/2 0; P2-3.4 6→20 11/9 19/1 3; P2-4.1 26→30 18/12 9/21 1; P2-4.2 6→20 11/9 20/0 0; P2-4.3 6→20 9/11 19/1 2.
- P1-5.2 = 30 (23 da v1.11 + 7 itens do bloco json de `saida/gcb/T113_onda1_P1_v2.md` em P1-5.2); a Parte 4 do arquivo diz "23 + 7 = 30".
- VOLÁTEIS 86 (54 da v1.11 + 32 novos, lista de `saida/pacote/T115_volateis_T11.md`); PARCIAIS 94 (88 + 6).
- Pegadinhas 335 por lote (v1.11 → v1.12): L1 19→28; L1C 4→4; L2 43→49; L3 42→51; L4 32→43; L4C 0→0; L5 48→61; L5C 0→0; L6A 35→47; L6B 39→52.
- `topicos`: 40 resumos (P1 17, P2 23) e 3 pilotos (P1-8.2, P2-1.4, P2-2.5); tópicos com resumo no -E 40, com `emUmMinuto` 3, com `visuais` 3.
- Limpeza: 53 deleções em 52 itens (L-1 25, L-2 3, L-3 6, L-4 18, L-5 1). Erratas de enunciado: T115-E-01 (L1-R137), T115-E-02 (L1-R167), T115-E-03 (L3-R108). URL da LGPD: 2 registros (fora do pacote).
- Registro de alterações: 447 linhas.
- Núcleo: 367 itens com `nucleo` true no -E, em 41 folhas.
- Registros do `interno`: 869 no total (v1.11 799 + 53 + 10 + 1 + 6); os registros `pegadinhas[k]` do `interno` dos lotes foram reindexados (k da v1.11 → k da versão nova) por serem posicionais.

## Edição .md do estudante: arquivos que mudam (26 de 35)
`L1_estudo.md`, `L1_gabarito.md`, `L1_itens.md`, `L2_estudo.md`, `L2_gabarito.md`, `L2_itens.md`, `L3_estudo.md`, `L3_gabarito.md`, `L3_itens.md`, `L4_estudo.md`, `L4_gabarito.md`, `L4_itens.md`, `L5_estudo.md`, `L5_gabarito.md`, `L5_itens.md`, `L6A_estudo.md`, `L6A_gabarito.md`, `L6A_itens.md`, `L6B_estudo.md`, `L6B_gabarito.md`, `L6B_itens.md`, `NUCLEO.md`, `README.md`, `SIM-0_folha.md`, `SIM-0_gabarito.md`, `SIM-1_gabarito.md`.
Itens novos por lote nos _itens.md e _gabarito.md: {'L1': 79, 'L2': 9, 'L3': 94, 'L4': 7}; tópicos renderizados: 40.

## Entradas X de `marcas_x_v112.py` (D1 da GBQ, T115_reconciliacao seção 5)
Confirmadas pela GBQ como conteúdo (FP), não marca de produção: X7 (ANPD "órgão da Presidência", pegadinha 32 do L3), X17 e X18 (medida F1, L3-R64), X19 (medida F1, L1-R176), X20 (tecla F4, resumo de P1-1) e X21 ("órgão da Presidência", resumo de P2-4.1). A X21, de mesma natureza da X7, passa a integrar a lista MANTER da D1, seção 3.5 (precisão de registro; nenhum dado muda; `marcas_x_v112.py` não muda).

## Fim de linha
Todos os arquivos desta pasta, fora de `out/` e `__pycache__/`, estão em LF (conferência C-LF); a coluna "Frente ao gerador_v1_11" compara o conteúdo LF dos dois lados, e os SHA-256 e bytes abaixo são os do disco (iguais aos do blob depois do commit).

## Arquivos da pasta (SHA-256 e bytes, como em disco)
| Arquivo | SHA-256 | Bytes | Frente ao gerador_v1_11 | Uso na v1.12 |
|---|---|---|---|---|
| `_run.py` | `ebdc3800a04ec950637d33409bc892b6d716ab126530c3f4d6ec831ee3d3fa1e` | 664 | igual | executor isolado de todos os passos (saída em UTF-8) |
| `banco.py` | `754571b7c0c30dfce76d23851b822d5fea16c2552a07383500a50f17f5c5ae97` | 3688 | igual | herdado; só registro (não executado) |
| `build_pacote.py` | `8e3547c0e2dfce3f382c48470a52c57f913c9baa7678e91b00d127d252589052` | 8017 | igual | herdado; só registro (não executado) |
| `build_v110.py` | `745a90f14525f3fbed302d718723ee0090d0eba6d8c14ee1bac13572c53ea051` | 6462 | igual | herdado; só registro (não executado) |
| `build_v111.py` | `641a38f48197b105bedaceda3362d5299667c71fbd3ac40e330f8d83150dfe48` | 8074 | igual | herdado; só registro (não executado) |
| `build_v112.py` | `0cfa241b96d3485529ce70bb9ac90ee7aae447d8c30523a602a1fe9cf95348ce` | 15338 | novo | passo 1 |
| `build_v19.py` | `dea7944fd993cdc9eefc5f19c990b3893f473ed09e7210df9ba911a1a91b9077` | 2686 | igual | herdado; só registro (não executado) |
| `checks_v112.py` | `9a099395973efa49d4a7bcae6cac6e628a0d27943efbb7857044588712cc6479` | 24472 | novo | passos 6, 7 e 9 (módulo: conferências) |
| `common.py` | `e81bc75dfb4faae7832f5ae8262c5f4b4c3992a249bb8529370112f1f3771848` | 6205 | igual | módulo |
| `conferencia_f_2026-10-17_v1_8.json` | `3badf68f4f9a0d188c23f7c6558b67d3b92b8178553b51b9ce58d0e8e9399d02` | 1553 | igual | herdado; só registro (não executado) |
| `conferencias_R1.py` | `587a8d4212429b2c4917c669106af4cb4864cd811481de6b473828bc6e6cc92e` | 31123 | igual | herdado; só registro (não executado) |
| `conferencias_v110.py` | `243f458ca1b7bb33559900f8940572b5bb4534ba0c609b926ca35cec38eea179` | 12000 | igual | herdado; só registro (não executado) |
| `conferencias_v111.py` | `b8675958b19504fedc960a7a6111c616a28f6e97f71c58dcaa8d6cc2f4a9bd39` | 20857 | igual | herdado; só registro (não executado) |
| `conferencias_v112.py` | `19cda92804e9777f4e7555631047941575bbddfbbf52f57770ae84003943277a` | 21846 | novo | passo 7 |
| `conferencias_v18.py` | `0b41b1cf8d02e148de32b7480a84ea0f7c28138b52f58b353c936a72b4e357e1` | 107983 | igual | herdado; só registro (não executado) |
| `conferencias_v19.py` | `7989b577d1e5424feba5817c1b352c8ee69b827e37878b1cbbf3b66acfc9727c` | 11042 | igual | herdado; só registro (não executado) |
| `config_v110.py` | `cfe023934ef0153b994349299fbf0210c7898c8c4d32edcd67a63c3b5d97a281` | 1640 | igual | módulo (E_L2R131, ATO_L2R131 lidos por nucleo.py e estudante_json_v112.py) |
| `config_v111.py` | `7e0f1fda1df07dca020940853827260fa8d01f168b8b23e1225a0582415f6136` | 9059 | igual | herdado; só registro (não executado) |
| `config_v112.py` | `d158d3a6014929fea8878015359cdeda78fc9793cc65d0d9d3cb9a341878332c` | 15675 | novo | módulo (chaves da ocorrência; único lugar do número da versão) |
| `diff.py` | `59fef679b240aa9e1ae7895813f4dd7be8251ae06a69921d37874ff843376bfb` | 1751 | igual | herdado; só registro (não executado) |
| `diff2.py` | `6513c3b66b2b0e09669a8624f77408fe8f4f1ce6f350a391e82558e5262901d0` | 1547 | igual | herdado; só registro (não executado) |
| `edital_p.py` | `0f7ed100392cdba1c09e1cf2dce107801c2fe8225920a5d501d6fc42bf89423d` | 1183 | igual | herdado; só registro (não executado) |
| `estudante_fidelidade.py` | `13b707b4b5ac41ecc431e6ad67703d32a5af1abc08521a1d135ec9c81f3b695a` | 26847 | igual | passo 2 (módulo: only_deletions) |
| `estudante_gen.py` | `c6c31a5ebd4fca5b86d4e4ba3a6548eb2f2ca979209d082d5f2e27cb9aa2893a` | 17433 | igual | passos 2 e 4 (módulo: lote_of, lote_fund, COMPL, FUSAO) |
| `estudante_json.py` | `854f13c4cae1c76146b05d97740bc553fe444e15e792e4de8b4863fab125daae` | 21406 | igual | herdado; só registro (não executado) |
| `estudante_json_v111.py` | `8b76fd1c67fab22f2e00d84b263d3de179fe0fe36982d7cbf8fdbad8a3483764` | 24782 | igual | herdado; só registro (não executado) |
| `estudante_json_v112.py` | `0fa7ff38ec63ee36ee142ccdb4c5dfecfe8ebd68e80ce98632156344a6b0b35a` | 25441 | novo | passo 2 |
| `estudante_marcas.py` | `41cf6eecc05d9d52c5115a383a4a2e44af56502f04d6d81ea0bfa040999c485f` | 9897 | igual | passo 2 (módulo) |
| `estudante_md_v110.py` | `488e4e3799ef387a04d2763059b73e5ffdb86d99285a93cc14840994240b31ec` | 5994 | igual | herdado; só registro (não executado) |
| `estudante_md_v111.py` | `895e498b3caf24d8e87c421c7800cb0be31268f8e81c6f297617dd4dbf776391` | 13304 | igual | herdado; só registro (não executado) |
| `estudante_md_v112.py` | `9ff1489fa0999f9ed687230c805bc158b79752098490e0049b6bfda603c744e4` | 15908 | novo | passo 4 |
| `f4.py` | `e0fb812b44b2822c9d5caad8c5018b1b0df5c929e5182368e2434413f3f52727` | 2542 | igual | herdado; só registro (não executado) |
| `fidelidade_mutacao.py` | `e5e4b7bf4026e309bb40c309c43cee8102134170b478455f1230dba6f1f1c52d` | 3935 | igual | herdado; só registro (não executado) |
| `fidelidade_mutacao_v111.py` | `04a382fd4363b44f738476b6cad26b4a9db20972291784d824d4f522357e720a` | 16938 | igual | herdado; só registro (não executado) |
| `fidelidade_mutacao_v112.py` | `264dc96bc40dacafc3d3b4566f5fa95838f86a804261a4dac12e2ad21669c088` | 12084 | novo | passo 9 |
| `fontes_v112.py` | `ce1cc463a32799d0424eadfe937cd1b47628cf6182f2008e4d1c63482d8da9dc` | 1978 | novo | módulo (leitura dos 23 insumos, SHA-256 LF) |
| `gce.py` | `e007ddaeac3b07f7f47fe7472c1ec6a1d418f731e185f4baaf678e822153212c` | 5972 | igual | herdado; só registro (não executado) |
| `inventario_v111.py` | `16e3cf25ba053531e0c8db24a484d7bbe2095af53978f72d98190d491188a222` | 16988 | igual | passo 8 (módulo importado sem mudança: regras do inventário) |
| `inventario_v112.py` | `8f40989e94850e2b3097aea19477ba0ac154e082de0b68ad43ec7336d1bdbb74` | 4014 | novo | passo 8 e módulo |
| `limpeza_v111.py` | `e3fe3f4f17bc95b81c502752ab342c173912bae0a5b442efd538f15737113e95` | 11651 | igual | herdado; só registro (não executado) |
| `limpeza_v112.py` | `f1d669a81bd4a2e124598a7e9923233f6ed47930b436084b042f89745141eb54` | 6300 | novo | passo 1 (módulo: erratas e limpeza L-1 a L-5) |
| `literais.py` | `93c64cd58bff76ab3afb8a7429cb3ba2b4d8af7353191e015d8949531b08518b` | 14182 | igual | herdado; só registro (não executado) |
| `lotes_tab.txt` | `895e4d50479615c6963fcd35c01d3cd57aa8bad3994dec6c08a1a639517d27a2` | 912 | igual | herdado; só registro (não executado) |
| `manifesto_v1_10.py` | `794ba0f10e64a4e44fe30f05bb5a84d9fc2164924a4b4fe7d0feddee0e7ddbb6` | 5384 | igual | herdado; só registro (não executado) |
| `manifesto_v1_11.py` | `6c579ae0b14c26bb844ba16c6770798e4be8f26f458777501bc70c9627596335` | 7349 | igual | herdado; só registro (não executado) |
| `manifesto_v1_12.py` | `4583108f4335441db69b8f4655b663ae8643de04d2ea5d02048ecb30d6a0ad7d` | 13905 | novo | passo 10 |
| `manifesto_v1_8.py` | `0c8c61f097bc749a7acaa782bcf9ef5755e8222fb970686ffac8f8b79e825030` | 18423 | igual | herdado; só registro (não executado) |
| `manifesto_v1_9.py` | `2b7b4bb020daa347a747ac3adac692e9262ab4f5bf2fe76a122c4cf4642113cc` | 4712 | igual | herdado; só registro (não executado) |
| `marcas_processo.py` | `7ee30de455a5c0332aca1dae2148d7670eb86bac08294f0c61a80da4484cc140` | 8200 | igual | passo 2 (módulo: varredura R) |
| `marcas_x_v110.py` | `adac74d52033a3484afc23d41b8f3385a0df5fcc84938adf21d451f8fb28db50` | 1118 | igual | passo 2 (módulo) |
| `marcas_x_v111.py` | `078511a93c4abe3884cdf0bfd142de9fecca5a8d11640ee07ad795d87fa1f032` | 727 | igual | passo 2 (módulo) |
| `marcas_x_v112.py` | `f81f9634021bca32e2c750e696b9396c7f986c26fa2b86421b16bd15d6100da7` | 1521 | novo | passo 2 (módulo: entradas X propostas, a confirmar pela GBQ) |
| `nucleo.py` | `de5bf4ec6ac8c41ad335a738138ee9b4b492a846a00897029092f9735df6e5d2` | 5066 | alterado | passo 1 e 2 (módulo: nucleo; atos novos por registra_extra) |
| `p1.py` | `5cfc3a55b838d3f02f6b4f95302ba354aa1a036f08fe83d6817a3dc2e2981a5b` | 11025 | igual | herdado; só registro (não executado) |
| `p2.py` | `2fd6fbc7f2f12550ece27cd1022e701bf2f88f2c71ef9ffd0dbd14e4647913f9` | 27070 | igual | herdado; só registro (não executado) |
| `peg.py` | `ee0071445a44c6c043a4e3359299e33aed17ea6da3515aa96f7d656e85115d61` | 4922 | igual | herdado; só registro (não executado) |
| `pegadinhas_v112.py` | `1b753de6a5359c0f65737f519204453fbfbc72a129fc388dfe9a718f193c3665` | 9577 | novo | passo 1 (módulo: pegadinhas de pares) |
| `probe.py` | `f4eb95e47897fb0026e3943ef1aa7951af0d43590292ea4b7fc13be86f71fc7b` | 441 | igual | herdado; só registro (não executado) |
| `reforco.py` | `252191a8d4efd47d7c84a075bf6f01d61ea8495ef5474323d444860e264c594f` | 13810 | igual | herdado; só registro (não executado) |
| `reforco_marcas.py` | `01be597885c6d1e6cf3c361922be43185e093507e3c746154b3c5f6ddd893793` | 1459 | igual | passo 2 (módulo) |
| `reforco_marcas_v110.py` | `0bf36b9b608734d9b9bf30d7e09524cad05a61c29036a4965d1e45f4282b4b71` | 2944 | igual | passo 2 (módulo) |
| `reforco_v110.py` | `20a081e36790583b4f7f4347e9fb696425976ee9fd50ac3afc2d7154521f8db7` | 15313 | igual | herdado; só registro (não executado) |
| `reforco_v112.py` | `14d17bc8e2221d27688203560694296048b92def1a95767a296153137ee7d5fe` | 15056 | novo | passo 1 (módulo: itens novos) |
| `refs.py` | `c3135e2eaf196f7651bf98a9d4fb3a0675069ce74ac90cf78ebcf24699a94524` | 4183 | igual | módulo |
| `registro_adendo_v110.py` | `8d977fee42567649a60e70c807c7ed7b839aa663fdf57db7cf23debf15406297` | 6183 | igual | herdado; só registro (não executado) |
| `registro_adendo_v111.py` | `443a5fbeb30128d88387a4f9e96667d1b03aa9a9208b3066e860810b03b40aa4` | 3688 | igual | herdado; só registro (não executado) |
| `registro_adendo_v112.py` | `ea66118e57b641499397e2f6b8463de83ab1283df45b231a83f90f96c7f3dfe7` | 7053 | novo | passo 3 |
| `registro_adendo_v19.py` | `7e7c4ac1cc9a137d906e50abc65d744617128e0c761977fcb0c89b99f74acb3b` | 5817 | igual | herdado; só registro (não executado) |
| `registro_alteracoes_v111.py` | `5f8e52f63ccaa8b729044220260e021164979dd4e4441c73ba5ab0a5cdfef5ec` | 7887 | igual | herdado; só registro (não executado) |
| `registro_alteracoes_v112.py` | `87a10194f5245f5e4ecc6544a6a8abe3f6abc810cf31ec85ab548be49b9f4381` | 12288 | novo | passo 5 |
| `registry.py` | `6664fbc7a4bdb9a997a92def4c824c7cf2c1c6a4d31603cd22e77478c7bae78b` | 897 | igual | herdado; só registro (não executado) |
| `relatorio_R1.py` | `616bbbcc9ff4f5ee976f9b92fe1e3e40cb35919da9c3386fa495335ff0db45ea` | 19839 | igual | herdado; só registro (não executado) |
| `relatorio_v1_8.py` | `8f72f40ebc38b6376da12aa66db54a180aa3e2545de04bda967bfb50fe6c0d7c` | 25065 | igual | herdado; só registro (não executado) |
| `report.py` | `397ac2117c430da380cfcf7d7ffc758db50192081da398abf04c0daa11092ac9` | 15830 | igual | herdado; só registro (não executado) |
| `report2.py` | `92c1fb9c6ac8c727831f16d2db5928bddf3f1f66cee3e6dbb87f35c523c08cc3` | 44678 | igual | herdado; só registro (não executado) |
| `resid.py` | `3e43ef78e0c82b3927ed5108facf18e5bc47307d6f2a5a0c266075e06d368082` | 481 | igual | herdado; só registro (não executado) |
| `review.py` | `a1c4f135e564a160e0d09a6347c04c218693fd506e67a6678f9549e7996180ff` | 690 | igual | herdado; só registro (não executado) |
| `rodar_tudo.sh` | `2d7bd256d5c4cd0c9dcbf97681a0d112d8026acd10fd351a6741a00b18585b68` | 1972 | alterado | runner |
| `sync_check.py` | `b828c4291295034480eda023081d9b399bdfe11398f611172cf21ccc41e4b7d6` | 2868 | igual | herdado; só registro (não executado) |
| `tabelas_v111.py` | `6ddabc4c880e1af72c50de41d428c0807dabc6e5a92e60f51cfaf2fbe0053635` | 12287 | igual | herdado; só registro (não executado) |
| `texts.py` | `c3ca12b7283710222c8baf681738b3d0e462207a30b81167d48e84be77bb0102` | 422 | igual | herdado; só registro (não executado) |
| `topicos_v112.py` | `2ab4eabc31897485e7ae3fa89ed7d8febb6b947ee73be8e493d7c9470b369f94` | 6980 | novo | passo 1 (módulo: `topicos`) |
| `validar_erros.py` | `19ab9c8b359e4a59f209ecbca3e29f2ecc16a0dd5fb49b8892538bbe7eb8f33e` | 18500 | igual | passo 7 (módulo e CLI) |
| `validar_erros_teste.py` | `fe1202a3b4cabbac57c4376c4b489aa3f7f3274d16ef233bbd0fb1602336c998` | 8136 | igual | passo 7 (C-15) |
| `validate.py` | `7cde528368ee261693addfb8642ba3deac40fa5db36177eabdb27d493bb795f5` | 44115 | igual | herdado; só registro (não executado) |
| `validate_v110.py` | `85c29703b02fd2b8cc5b4879427464c6897fe25000a513aa85c88212ee7a4cdf` | 16075 | igual | herdado; só registro (não executado) |
| `validate_v111.py` | `cff58f6685fbb0dd1abdf7f0660c869c85f83e7ca8febb5282f3d90a2ebd3fc6` | 12274 | igual | herdado; só registro (não executado) |
| `validate_v112.py` | `57a8e8204f2a21215dbc4bdfdb14e726a09e0eb062f44f9cbbd0b95b26b33c8f` | 5742 | novo | passo 6 |
| `validate_v19.py` | `5e3581239299b9c90faf991733599b4e93adac1e1a5e739816ab97282ed7ae9d` | 14513 | igual | herdado; só registro (não executado) |

## out/ (regerado a cada execução; fonte dos promovidos)
| Arquivo | SHA-256 | Bytes |
|---|---|---|
| `out/conferencias_stdout.txt` | `bae1774b883173fe74a1e49765e0d6bc36d5bb675264f4eecb3afd2acab6d384` | 5060 |
| `out/conferencias_v1_12.json` | `e755986805cdcfc1ed49b5d5622e5aafa65c2de765d5a5a2a12749f621bf818e` | 6158 |
| `out/estudante_json.json` | `43b75e623da71b321d07758d9ef41ad5a31aaa092e630d8ee7f47d8ccdae92e7` | 23292 |
| `out/estudante_json_stdout.txt` | `5825afff12e516ccfa0cbfc8ab3e679b4b5ea05cb66f4e65111bd088ff6ed315` | 3344 |
| `out/estudante_md_stdout.txt` | `18cd66f685e9851d7ccc015a278cad22bc70c9b09cb3126dcce709c1648f4b36` | 129 |
| `out/estudante_md_v1_12.json` | `3a14457a743d7a2cca7901a01aeec6ade3e357be7abf886681512eecdb7025bb` | 1810 |
| `out/fidelidade_mutacao_stdout.txt` | `6a97a1e856e9a7b820a0266cbd08324fd4c6ad52c51915f6384745de0adddc15` | 2560 |
| `out/fidelidade_mutacao_v1_12.json` | `c33d3e7ba8585657e0bd9a537e0a391142706b7a9c8e145db866dd9cfed6c386` | 6355 |
| `out/folhas_v1_12.json` | `b7e859051d98bdf730ba4d00f3fc2113c5fd002be0079783e8e19f34b7cb1c8a` | 6097 |
| `out/gen_stdout.txt` | `e774e0e50f7dbe78575d2c91241358d33bf40d4b851ac27caf298928d806f98f` | 245 |
| `out/inventario.csv` | `20dc11ff855732f81a9471381a95df9088415f487751761c1b94270495939d01` | 149097 |
| `out/inventario.json` | `9adfc248f358e76618b1d8d9f897bc38694d5bb7400b310498ddeb39c721dad6` | 634 |
| `out/inventario_stdout.txt` | `eb5085ad0905b8a776706a87460275366e9ce1cbb3a863b28dba6fd0973f337f` | 636 |
| `out/pacote.json` | `3476525319b027fe4427bf93598d516087ad6f18fb8dd5bbed4ad8c04be6024f` | 1396410 |
| `out/pacote_estudante.json` | `23224c96b4189097012f139f52a9b995c29d930c6ac72801659720d6db612abd` | 1134920 |
| `out/registro_adendo4.md` | `52a47eec0f7c33e63ff73968fc5064d8665a18e08b6c2e45694f5da63b6af228` | 7320 |
| `out/registro_alteracoes_stdout.txt` | `c7a6c71e864fa3f3fb95a19b9abb3fa440c1946c1c9fbebe8128c9fffe816f3f` | 182 |
| `out/registro_alteracoes_v1_12.csv` | `437e2303172e25e1c45a9500b0d1fffb54e75fb59e3aa952b3eacf1c4da98662` | 149187 |
| `out/registro_alteracoes_v1_12_resumo.md` | `e5a92904ce3abda41415d6403474fee63280c1eb88afb3d4eeecac5b5744ff84` | 2820 |
| `out/registro_stdout.txt` | `81c5b4ad5a9ffb5231e86587cfaee9df1941fcf663afe509223d83891ecad525` | 69 |
| `out/similaridade_v1_12.csv` | `ab5218ebd8f62f10a1648b12adad0752c32c88a7a020b2792049c63cea343f2c` | 65 |
| `out/stats_v1_12.json` | `50a3ca3f29656f6b22b3e4c913125a457075e1f360a6579d6a07f2f59094e22e` | 18515 |
| `out/validar_erros_stdout.txt` | `a96eb28566ac456533bf65c5345e5f17422d6462619b7c90df97ddac36b29d2d` | 1578 |
| `out/validate_stdout.txt` | `f9e8690b953bcd692d863935c78d7d1ace2c7489dc3ff1db1451474a3027b32b` | 4626 |
| `out/validate_v1_12.json` | `f45300e7a890e976a4028d8f786fc249091099049a00c3b248e21f9f7df18c38` | 5856 |
| `out/casos_erros/importados_exportadoEm.json` | `ca039c0b82972681b9902b442e44867d80422f9b29b1c0ba8617e17abd25ad71` | 71 |
| `out/casos_erros/importados_sha.json` | `7c2b3afd60182ce1c3ae36d744272baac4b1d8e2cc108d3849fdc06980fb7ceb` | 134 |
| `out/casos_erros/incoerente_D.json` | `463a23847f577c0c5f6014bc6400cfed5c1cf41e480462faaab98a2de885ec22` | 1383 |
| `out/casos_erros/invalido_A_versaoFormato2.json` | `bae8aa0fc57ac23bd5e425c6b25e2e1c8370ce3921af88351a7be07e30687fcb` | 1383 |
| `out/casos_erros/invalido_B_campo_ausente_e_tipo.json` | `25fb6971761e1f39cb65b6bd1a48228bf5e942aa5e764e6ee41429a626a76b75` | 1180 |
| `out/casos_erros/invalido_C2_formato_errado.json` | `7a1540e0090f683a06902633167559b82660b066a51e61d94340e667b297eff9` | 1380 |
| `out/casos_erros/invalido_C_json_truncado.json` | `9f05598e3fd28b6a96ba7abcb147f650e1f995b49f4826c6da804e2b9ef9d0c6` | 596 |
| `out/casos_erros/valido_ids_reais.json` | `0763f9dd80bf20006eaf95547a3db7c028bf328c9d8ac7c66fcec7d0c3ff0647` | 1595 |
| `out/estudante/BANCO_gabarito.md` | `f7d9bb470356e98962227bc7d19dbd6de2eff053aa718df002b26d6f2b4cb5ed` | 9340 |
| `out/estudante/BANCO_itens.md` | `879e1769c76c3bc655510a18a8fd66f49abb6dec52d7e3030adf93132a226c2c` | 76551 |
| `out/estudante/DISCURSIVAS.md` | `7777c52ca635cdd0e33a525aadd3b86699d333def9bb61816c79b67653f17bd0` | 6694 |
| `out/estudante/DISCURSIVAS_padrao.md` | `4d5a4e6e9cb23fffee9b401f7b8b9537ce9475cdc8127e34cd27c6592f77dcb4` | 32002 |
| `out/estudante/L1_estudo.md` | `12ebe1ac46ce54b2d2f53dfce680e90c235ed6f1743bbb7d41b836e4247dda7f` | 55866 |
| `out/estudante/L1_gabarito.md` | `2947f638e5f9f1a08133716a7bb3b4d6f961330aa87dc5fc9d5252bec363cf7a` | 69895 |
| `out/estudante/L1_itens.md` | `94e106e720f28ace0fedabb9e5050ee018e2e5147cef926700cff45929325050` | 70462 |
| `out/estudante/L2_estudo.md` | `4b3d27b2ea186da1d97d9571608d36f00160696d450b2f2e9c193258d3346d3c` | 48933 |
| `out/estudante/L2_gabarito.md` | `7aa74384f5dd7e5bac2f49dc3d6b50af0322ccc10ba07cfcd0a41f9cb166d2b4` | 53394 |
| `out/estudante/L2_itens.md` | `9bb73429f2a9e29713c49247a61b58b1c4537aeac3850a47e3c698af5ffe7924` | 52495 |
| `out/estudante/L3_estudo.md` | `a6ea08ad469fb819db5bfb8609ad2ec3f436f62fddb049a3277669bb0e61435d` | 54586 |
| `out/estudante/L3_gabarito.md` | `5a2516422ebb27293f0a337fcae04ad539de3122e6e9c97c0cfdfd450028ce92` | 38836 |
| `out/estudante/L3_itens.md` | `b4ca1f7707a5789eb1750caa833d9a4d6a60d930642dc4908065e2b128bf2281` | 41600 |
| `out/estudante/L4_estudo.md` | `7f9bedfcc79f896c0b3ed162474649b5d6c021f9bc43767752bac98438bacf27` | 64066 |
| `out/estudante/L4_gabarito.md` | `66f95d58f2154763b7b362ee0ae426d3e86b6fa472c081a863716cf488aa5575` | 17579 |
| `out/estudante/L4_itens.md` | `6620555a3b368b66c1ca21a2ebc1faf9a2515016e747d64acf567d6a523c6545` | 8920 |
| `out/estudante/L5_estudo.md` | `50abca622f917d20406241ded6fccd576c55683e30c5a7b4ff29931c351ac5e2` | 45121 |
| `out/estudante/L5_gabarito.md` | `bbd753e15773894ad70c20b11286f3d5b7b440635ca7ce47b5d8409c344703bc` | 9627 |
| `out/estudante/L5_itens.md` | `e110570384225bda943dd709e1a4272faa6581b94eadad6ebf6f42fc488afaa3` | 7115 |
| `out/estudante/L6A_estudo.md` | `8ae7516d4b409f7944c81cb879b9941f1621a5d0bfab5eaca31ac3bb3e9f2065` | 56408 |
| `out/estudante/L6A_gabarito.md` | `c2fab83b8520fbb20427647236a51c51103cbb7dc92389c07eb472ee955a995a` | 8055 |
| `out/estudante/L6A_itens.md` | `afa0a0e333ff7ac2d4857ee80e72142a8825befb417832c15921f1663ff31b1e` | 4206 |
| `out/estudante/L6B_estudo.md` | `3a5c7eca9a7f507a976422b2ef2e36b388d371a8e352897919c7720466c7c4c8` | 70677 |
| `out/estudante/L6B_gabarito.md` | `8b23a83303888f821334d100186648807ae6562a4a683f11d88cb9f988798b91` | 8767 |
| `out/estudante/L6B_itens.md` | `cac479bf65a9d8fc9e8d94822eed87e8f6b0257cf49c2028dab6f43873565077` | 5089 |
| `out/estudante/NUCLEO.md` | `bf13d9dff214e1e3dd699028c27617c11f96e640c4bbdf8bba42e96e0d15260a` | 4129 |
| `out/estudante/README.md` | `8048d862c58afbedd9d952e576e758c43989b1245815a367e8990e261ea0379a` | 2742 |
| `out/estudante/SIM-0-P2_folha.md` | `f69efe607e7b575c246b46eded5ce15d5b6cf1e14ae755bc1bff23087c8bdab5` | 6063 |
| `out/estudante/SIM-0-P2_gabarito.md` | `cdd8a6588d0e24ebd4e445a50a7d11334e324eb4a85dbfd46b7babe0bbdcc081` | 5956 |
| `out/estudante/SIM-0_folha.md` | `7ef04f37578a2da082ab8c016ac06a06e8463db96089c268cd7e9b100815cd16` | 19458 |
| `out/estudante/SIM-0_gabarito.md` | `2df79ffa2501e38c66564a8b2a23cd5632372255bf7214c9179ca8ece3788374` | 5979 |
| `out/estudante/SIM-1_folha.md` | `e0e21ea32da954f4d20ac9df23937dab412179873d28211876600e938c2b9a38` | 8625 |
| `out/estudante/SIM-1_gabarito.md` | `17b0de7a1e3e34943dfeffe91fdfb1f746bcabffbe6c976516e6623a4ad84c96` | 15085 |
| `out/estudante/SIM-2_folha.md` | `d576cc3fecc6f9973a028f82e303abb65aedd00ad14000cbc263c51423daaa92` | 9658 |
| `out/estudante/SIM-2_gabarito.md` | `2113d4a7c1e399a1ce25b71d5819fe565121d3fc41c9a4d4c2b3e3e75e248c9e` | 9565 |

## Entregáveis (fonte dos promovidos; a promoção é ato separado, depois do aceite da fidelidade; nada é promovido por este gerador)
| Saída | Destino na promoção | SHA-256 | Bytes |
|---|---|---|---|
| `out/pacote.json` | `saida/pacote/pacote.json` | `3476525319b027fe4427bf93598d516087ad6f18fb8dd5bbed4ad8c04be6024f` | 1396410 |
| `out/pacote_estudante.json` | `saida/pacote/pacote_estudante.json` | `23224c96b4189097012f139f52a9b995c29d930c6ac72801659720d6db612abd` | 1134920 |
| `out/registro_adendo4.md` | `saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo4_2026-10-18.md` | `52a47eec0f7c33e63ff73968fc5064d8665a18e08b6c2e45694f5da63b6af228` | 7320 |
| `out/registro_alteracoes_v1_12.csv` | `saida/pacote/registro_alteracoes_v1_12.csv` | `437e2303172e25e1c45a9500b0d1fffb54e75fb59e3aa952b3eacf1c4da98662` | 149187 |
| `out/registro_alteracoes_v1_12_resumo.md` | `saida/pacote/registro_alteracoes_v1_12_resumo.md` | `e5a92904ce3abda41415d6403474fee63280c1eb88afb3d4eeecac5b5744ff84` | 2820 |
| `out/estudante/BANCO_gabarito.md` | `saida/estudante/BANCO_gabarito.md` | `f7d9bb470356e98962227bc7d19dbd6de2eff053aa718df002b26d6f2b4cb5ed` | 9340 |
| `out/estudante/BANCO_itens.md` | `saida/estudante/BANCO_itens.md` | `879e1769c76c3bc655510a18a8fd66f49abb6dec52d7e3030adf93132a226c2c` | 76551 |
| `out/estudante/DISCURSIVAS.md` | `saida/estudante/DISCURSIVAS.md` | `7777c52ca635cdd0e33a525aadd3b86699d333def9bb61816c79b67653f17bd0` | 6694 |
| `out/estudante/DISCURSIVAS_padrao.md` | `saida/estudante/DISCURSIVAS_padrao.md` | `4d5a4e6e9cb23fffee9b401f7b8b9537ce9475cdc8127e34cd27c6592f77dcb4` | 32002 |
| `out/estudante/L1_estudo.md` | `saida/estudante/L1_estudo.md` | `12ebe1ac46ce54b2d2f53dfce680e90c235ed6f1743bbb7d41b836e4247dda7f` | 55866 |
| `out/estudante/L1_gabarito.md` | `saida/estudante/L1_gabarito.md` | `2947f638e5f9f1a08133716a7bb3b4d6f961330aa87dc5fc9d5252bec363cf7a` | 69895 |
| `out/estudante/L1_itens.md` | `saida/estudante/L1_itens.md` | `94e106e720f28ace0fedabb9e5050ee018e2e5147cef926700cff45929325050` | 70462 |
| `out/estudante/L2_estudo.md` | `saida/estudante/L2_estudo.md` | `4b3d27b2ea186da1d97d9571608d36f00160696d450b2f2e9c193258d3346d3c` | 48933 |
| `out/estudante/L2_gabarito.md` | `saida/estudante/L2_gabarito.md` | `7aa74384f5dd7e5bac2f49dc3d6b50af0322ccc10ba07cfcd0a41f9cb166d2b4` | 53394 |
| `out/estudante/L2_itens.md` | `saida/estudante/L2_itens.md` | `9bb73429f2a9e29713c49247a61b58b1c4537aeac3850a47e3c698af5ffe7924` | 52495 |
| `out/estudante/L3_estudo.md` | `saida/estudante/L3_estudo.md` | `a6ea08ad469fb819db5bfb8609ad2ec3f436f62fddb049a3277669bb0e61435d` | 54586 |
| `out/estudante/L3_gabarito.md` | `saida/estudante/L3_gabarito.md` | `5a2516422ebb27293f0a337fcae04ad539de3122e6e9c97c0cfdfd450028ce92` | 38836 |
| `out/estudante/L3_itens.md` | `saida/estudante/L3_itens.md` | `b4ca1f7707a5789eb1750caa833d9a4d6a60d930642dc4908065e2b128bf2281` | 41600 |
| `out/estudante/L4_estudo.md` | `saida/estudante/L4_estudo.md` | `7f9bedfcc79f896c0b3ed162474649b5d6c021f9bc43767752bac98438bacf27` | 64066 |
| `out/estudante/L4_gabarito.md` | `saida/estudante/L4_gabarito.md` | `66f95d58f2154763b7b362ee0ae426d3e86b6fa472c081a863716cf488aa5575` | 17579 |
| `out/estudante/L4_itens.md` | `saida/estudante/L4_itens.md` | `6620555a3b368b66c1ca21a2ebc1faf9a2515016e747d64acf567d6a523c6545` | 8920 |
| `out/estudante/L5_estudo.md` | `saida/estudante/L5_estudo.md` | `50abca622f917d20406241ded6fccd576c55683e30c5a7b4ff29931c351ac5e2` | 45121 |
| `out/estudante/L5_gabarito.md` | `saida/estudante/L5_gabarito.md` | `bbd753e15773894ad70c20b11286f3d5b7b440635ca7ce47b5d8409c344703bc` | 9627 |
| `out/estudante/L5_itens.md` | `saida/estudante/L5_itens.md` | `e110570384225bda943dd709e1a4272faa6581b94eadad6ebf6f42fc488afaa3` | 7115 |
| `out/estudante/L6A_estudo.md` | `saida/estudante/L6A_estudo.md` | `8ae7516d4b409f7944c81cb879b9941f1621a5d0bfab5eaca31ac3bb3e9f2065` | 56408 |
| `out/estudante/L6A_gabarito.md` | `saida/estudante/L6A_gabarito.md` | `c2fab83b8520fbb20427647236a51c51103cbb7dc92389c07eb472ee955a995a` | 8055 |
| `out/estudante/L6A_itens.md` | `saida/estudante/L6A_itens.md` | `afa0a0e333ff7ac2d4857ee80e72142a8825befb417832c15921f1663ff31b1e` | 4206 |
| `out/estudante/L6B_estudo.md` | `saida/estudante/L6B_estudo.md` | `3a5c7eca9a7f507a976422b2ef2e36b388d371a8e352897919c7720466c7c4c8` | 70677 |
| `out/estudante/L6B_gabarito.md` | `saida/estudante/L6B_gabarito.md` | `8b23a83303888f821334d100186648807ae6562a4a683f11d88cb9f988798b91` | 8767 |
| `out/estudante/L6B_itens.md` | `saida/estudante/L6B_itens.md` | `cac479bf65a9d8fc9e8d94822eed87e8f6b0257cf49c2028dab6f43873565077` | 5089 |
| `out/estudante/NUCLEO.md` | `saida/estudante/NUCLEO.md` | `bf13d9dff214e1e3dd699028c27617c11f96e640c4bbdf8bba42e96e0d15260a` | 4129 |
| `out/estudante/README.md` | `saida/estudante/README.md` | `8048d862c58afbedd9d952e576e758c43989b1245815a367e8990e261ea0379a` | 2742 |
| `out/estudante/SIM-0-P2_folha.md` | `saida/estudante/SIM-0-P2_folha.md` | `f69efe607e7b575c246b46eded5ce15d5b6cf1e14ae755bc1bff23087c8bdab5` | 6063 |
| `out/estudante/SIM-0-P2_gabarito.md` | `saida/estudante/SIM-0-P2_gabarito.md` | `cdd8a6588d0e24ebd4e445a50a7d11334e324eb4a85dbfd46b7babe0bbdcc081` | 5956 |
| `out/estudante/SIM-0_folha.md` | `saida/estudante/SIM-0_folha.md` | `7ef04f37578a2da082ab8c016ac06a06e8463db96089c268cd7e9b100815cd16` | 19458 |
| `out/estudante/SIM-0_gabarito.md` | `saida/estudante/SIM-0_gabarito.md` | `2df79ffa2501e38c66564a8b2a23cd5632372255bf7214c9179ca8ece3788374` | 5979 |
| `out/estudante/SIM-1_folha.md` | `saida/estudante/SIM-1_folha.md` | `e0e21ea32da954f4d20ac9df23937dab412179873d28211876600e938c2b9a38` | 8625 |
| `out/estudante/SIM-1_gabarito.md` | `saida/estudante/SIM-1_gabarito.md` | `17b0de7a1e3e34943dfeffe91fdfb1f746bcabffbe6c976516e6623a4ad84c96` | 15085 |
| `out/estudante/SIM-2_folha.md` | `saida/estudante/SIM-2_folha.md` | `d576cc3fecc6f9973a028f82e303abb65aedd00ad14000cbc263c51423daaa92` | 9658 |
| `out/estudante/SIM-2_gabarito.md` | `saida/estudante/SIM-2_gabarito.md` | `2113d4a7c1e399a1ce25b71d5819fe565121d3fc41c9a4d4c2b3e3e75e248c9e` | 9565 |

Resultado desta execução: validate_v112 32/32 OK; conferencias_v112 27 OK, 0 PENDENTE, 0 FALHA; fidelidade_mutacao_v112 30/30 casos (23 aplicáveis).
