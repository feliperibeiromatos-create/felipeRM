# saida/pacote/fidelidade_v1_8_gbq-cqe.md — T-81 (D-T81-RESPOSTA; D-T12-V13) — 2026-10-17 — gerado por gbq-cqe

Ato próprio de QA de fidelidade da v1.8. Usei só leitura e scripts próprios (scratchpad da sessão, `cqe1.py` a `cqe5.py`). Não executei nem reutilizei nenhum script de `saida/pacote/gerador_v1_8/`; li `banco.py`, `validate.py`, `common.py`, `refs.py` e `build_pacote.py` apenas para criticar o diff. As bases vieram do git: `git show 62ab128:saida/pacote/pacote.json` e os 43 arquivos de `git show HEAD:saida/estudante/*`. Comparei tudo com conteúdo normalizado em LF.

## Veredito: **APROVADO COM RESSALVAS**

- Resíduo de PROCESSO: 0.
- Reprovação: 0% (0 de 286 itens; 0 de 34 arquivos da edição).
- Ressalvas: 3, todas de severidade baixa. Nenhuma delas impede o gatilho A. Duas são DÚVIDA de classificação, e a decisão é da gbq-gerencia (seção 3).

## 1. SHA-256 calculados por mim (LF)

| Objeto | Bytes | SHA-256 | Esperado (D1) |
|---|---|---|---|
| `pacote.json` v1.7 (`62ab128`, = HEAD) | 621907 | `f20216c22600b7af7cf54b4e79d83accf3568aee8de48ad970fe800451528c7a` | confere |
| `saida/pacote/pacote.json` v1.8 | 621907 | `09d4a457612781275659a3f7fbfd3a182f20fd9d4003e5ba38007d0c26c7a9c0` | confere (seção 8) |
| `saida/pacote/pacote_estudante.json` v1.8-E | 602815 | `851e2370a9f5e9c8e5db725ff84777f70c12f81044983d339434ac7504e04c3e` | confere com o valor da produtora (9.4) |
| `regras/pacote_contrato.md` v1.2.4 (HEAD) | — | `75e6a5009be70f5be3cb3e7b9b5087b96086a0884831419d6818fa27babdb27e` | confere (P3) |
| `regras/pacote_contrato.md` v1.2.5 | 35460, 154 linhas | `10eac696dbb83049ba12ee793ff4991a1884094b7b88cdaf39f10a3fcc33660e` | confere (CONTRATO-V125) |
| Manifesto da edição v1.7 (HEAD, 43 arq.) | — | `67d2bdf85925a232…` | confere (P2) |
| Manifesto da edição v1.8 (34 arq.) | — | `0b7391fa0178488924de8e6ed420c6108dd5fdad0e10fd1c5ccc40d9cd4bae6c` | confere (9.4) |
| `pacote_relatorio_2026-10-17_v1_8.md` | — | `c2b7bbd45c35989270957eb0e0ffb0b17754f36cb4ffa074d50d34b9472dba3a` | (sem valor de controle) |
| `contrato_v1_2_5_2026-10-17.md` | — | `320b3e50ba90ddc9028d4e090e938bad8a3199dd55ed61575a85b39a0e3a9381` | (sem valor de controle) |

Fórmula do manifesto: SHA-256 de `"<sha256>  <nome>\n"`, uma linha por arquivo, em ordem de nome. Ela reproduz o `67d2bdf8…` da v1.7.

Os arquivos promovidos estão gravados em LF no disco, sem CRLF. O SHA do disco é, portanto, o SHA LF.

## 2. Conferências (1) a (7)

| # | Conferência | Resultado |
|---|---|---|
| 1a | Diff JSON v1.7 → v1.8 (chaves, ordem, tipos, valores) | Exatamente `$.geradoEm` e `$.nome` |
| 1b | Conferência byte a byte: as 2 trocas, cada uma com 1 ocorrência na v1.7, reproduzem a v1.8 | Igual |
| 1c | Contagens v1.8 | 286 itens; C/E 149/137; `volatil` 23; 0 "QA PENDENTE"; 10 lotes; 4 simulados; 5 discursivas |
| 2a | `pacote_estudante.json`: chaves de topo, `versao`, `geradoEm`, `nome` "Câmara 2026 — pacote do estudante (v1.8-E)", `edital` | OK. Reserialização `indent=1` + "\n" idêntica ao arquivo |
| 2b | Itens: ids e ordem; mesmas chaves na mesma ordem; todos os campos fora de `justificativa`/`nota`/`url` idênticos (gabarito, enunciado, comando, comandoOriginal, textoBase, itemEdital, aderência, volatil, rótulo, certame, cargo, ano, número) | 286/286, 0 falhas |
| 2c | `url`: banco intocada / AUTORAL "" | 106/106 e 180/180 |
| 2d | `justificativa` | 75 alteradas, todas subsequência da origem; banco: todas "" |
| 2e | `nota` | Só BQ-0003 muda, pela retirada exata de " (D-LEI-15352)" (1 ocorrência); BQ-0040 idêntica |
| 2f | Simulados | Idênticos, exceto `avisos[0]` do SIM-0: só a retirada de "D-ADERENCIA: " (subsequência) |
| 2g | Discursivas | `id`, `tipo`, `n`, `valor`, `quesitos[].id` idênticos; 3 textos alterados, todos subsequência |
| 2h | Lotes | Ordem L1, L2, L3, L4, L5, L6A, L6B; `id`, `nome`, `prova`, `itensEdital`, `legendaMecanismo` iguais aos do `pacote.json`; `pares[].id` e `pegadinhas[].itemEdital` iguais |
| 2i | Fusão | L1, L4 e L5 com 30 itens cada (por prefixo); L2 30, L3 30, L6A 15, L6B 15; banco 106. O separador `\n\n## Complemento\n\n` ocorre 1 vez e o curso do L1 termina exatamente com o curso do L1C; o curso do L1C não tem linha "## ". L1 tem 23 pegadinhas = 19 + as 4 do L1C, na ordem. L4C e L5C têm curso, resumo, pares e pegadinhas vazios; `itensEdital` ⊂ o do lote principal. Nenhum lote do estudante tem curso ou resumo vazio |
| 2j | "Só deleção" | Todos os campos alterados são subsequência da origem, salvo as 2 exceções fechadas: L6A.curso (CAIXA) e a cabeça do L1.curso (REALINHA). As duas são iguais, byte a byte, ao texto da edição v1.7 aceita (linha 5a) |
| 3 | Varredura (seção 4) | 0 de processo |
| 4a | Edição v1.7 (HEAD) × v1.8 | 9 retirados (L1C_, L4C_, L5C_ × 3); 0 acrescentados; 8 alterados (README, L1_estudo, L1_itens, L1_gabarito, L4_itens, L4_gabarito, L5_itens, L5_gabarito); 26 idênticos byte a byte |
| 4b | Natureza das alterações | Só inserções nos 7 arquivos de lote. No README: versão/data e retirada das 3 linhas L1C/L4C/L5C, ficando 7 linhas "Por lote" |
| 4c | Reconstrução | `L4_itens`/`L5_itens` v1.8 = v1.7 + "\n\n" + corpo do complemento. `L1_itens` v1.8 = v1.7 + corpo do L1C sem o cabeçalho "**Comando.**", porque o comando é o mesmo do último bloco do L1 (agrupamento previsto na 3.2). `*_gabarito` v1.8 = v1.7 + as 10 seções `###` do complemento, idênticas (L1/L4/L5). Cada gabarito tem só a legenda do próprio lote. Curso do L1 v1.8 = v1.7 + separador + curso L1C v1.7. Pegadinhas do L1 v1.8 = v1.7 + as 4 linhas do L1C |
| 5a | JSON do estudante × edição v1.7 aceita (HEAD) | resumo 7/7; curso 7/7 (L1 = L1 v1.7 + sep + L1C v1.7); linhas de pegadinha 7/7 lotes; pares 139/139 (2 pares de L3 com `b`/`como` vazios, que viram a linha "- **a**.", coerentes); justificativas AUTORAL 180/180 (com gabarito e item do edital); enunciado+comando 180/180; discursivas: comando 5/5, padrão 5/5, aspectos 19/19, quesitos 19/19, conceitos 76/76 |
| 5b | JSON do estudante × edição v1.8 | Mesmas contagens, 100% coerente (gabarito/itens do complemento conferidos nos arquivos fundidos) |
| 6 | Contrato v1.2.4 → v1.2.5 | Extraí eu mesma os blocos C-1 a C-3 da D1 e os apliquei (assert de ocorrência única) ao conteúdo de HEAD: o resultado é igual ao disco. Diff por linha: troca da linha 1, troca da linha 3 e inserção de 11 linhas (bloco de 10 + 1 em branco) antes de "---". Nada mais. Só acrescenta o arquivo opcional |
| 7a | `banco/` e `gerador_v1_7/` × HEAD | Sem diff, sem arquivo novo, sem ignorado (`git status --porcelain --ignored`; 108 arquivos no disco = 108 no git) |
| 7b | `saida/plataforma`, `saida/gce`, `saida/gcb`, `saida/simulados`, `saida/treino` | Sem diff |
| 7c | Lista de arquivos de `gerador_v1_8` × v1_7 | Só as trocas/acréscimos da 1.1. Alterados: build_pacote, common, refs, validate, estudante_gen, estudante_fidelidade, rodar_tudo, banco (Adendo 9.3) e MANIFESTO. O resto é idêntico byte a byte, inclusive `fidelidade_mutacao.py`, que não precisou de redirecionamento. Diffs de `banco.py`, `validate.py` (linhas 2, 26, 62, 329 + `sys.exit`), `common.py`, `refs.py` (`C_V17='62ab128'`, `v17()`) e `build_pacote.py` restritos ao admitido |
| 7d | Promoção | `out/pacote.json`, `out/pacote_estudante.json` e `out/pacote_relatorio…` idênticos aos de `saida/`; `diff -r out/estudante saida/estudante` vazio |
| 8 | Adendo 1 | "mapeamento adicional" e "D-DA-BANCO": 0 em `pacote.json`, 0 em `pacote_estudante.json` e 0 nos 34 arquivos da edição. `nota` do BQ-0003 na v1.8 idêntica à da v1.7 (o diff do pacote tem só 2 caminhos). No estudante só cai " (D-LEI-15352)". Nenhum outro campo foi afetado. `banco.py` mudou só em `SUF_MAPA`, `nota_de` (com o assert) e a docstring |

## 3. Varredura independente (conferência 3)

Rodei a regex R da D1 (2.3) e uma lista mais larga, minha, sobre TODAS as strings do `pacote_estudante.json` e sobre os 34 arquivos da edição v1.8. A lista larga cobriu: Presidência/Fundador/Secretaria/PRES-S/EXEC/BIP/FV sem distinção de caixa; fábrica; T-/D-/E-/O-/R-/N-xx; F1–F99; "[V "; "NORMATIVO — QA"; CQFP/CQE/CPP/CFP/GCE/GCB/GBQ/CSC/QA; nomes de agente; Claude/Sonnet/Opus/Haiku/ChatGPT/GPT*/Gemini/Anthropic/OpenAI/DeepSeek/Llama/Copilot; claude.ai/Insumo; carimbos; e, como exploração, Gerência, D1, gatilho, reconcilia, canônic, sNcN, caminhos, rótulos internos, "QA PENDENTE", errata, "Lote N", Projeto, Presidente, ciclo.

Pela regex R da D1:
- JSON: 9 casamentos, X1–X8 + Y1, todos com a contagem esperada.
- Edição: 11 casamentos. X1 e X2 aparecem 2 vezes cada (BANCO_itens, SIM-0_folha); X3 1 (L2_estudo); X4 a X7 1 cada (L3_estudo: curso 338 e 363, pares 559, pegadinhas 595); X8 1 (L6A_estudo:83); Y1 1 (L4_gabarito:58).
- Processo: 0.

Pela lista larga, classifiquei cada ocorrência que não está em X/Y:

| Termo | Onde | Classe |
|---|---|---|
| OpenAI, Open AI, Gemini, GPT, GPT-Live, gpt-transcribe, gpt-4o-transcribe-diarize, gpt-live-transcribe, openai/whisper, Anthropic, DeepSeek (61 no JSON, 63 na edição) | edital 1.8, L1 resumo/curso, L1-Q16/Q18, L4 curso, L4-05 | CONTEÚDO (matéria P2-1.8 e P1-5.1; termos fora da lista, conforme a 2.3) |
| "insumo" em minúscula | L3-Q04, discursiva D1 | CONTEÚDO |
| "D1" | id da discursiva D1 | CONTEÚDO (id de questão) |
| "Presidente"/"presidente" (16) | L1, L2, discursivas | CONTEÚDO (presidente da sessão) |
| "ciclo"/"Ciclo" (6) | human-in-the-loop, ciclo de treinamento, ciclo de vida dos dados | CONTEÚDO |
| "Projeto" | `certame` "Projeto Câmara 2026" dos AUTORAL; "HIPÓTESE do Projeto" nas discursivas; Projeto de Lei | fora da lista por regra expressa (2.3), sem ação |
| "AUTORAL", "CEBRASPE_ANALOGA" no campo `rotulo` | 286 itens | campo do contrato, cópia literal obrigatória |
| "rótulo CEBRASPE_ANALOGA" | BANCO_itens.md:3 | CONTEÚDO de edição (descreve o campo rótulo); idêntico à v1.7 |
| "Lote N"/"Lote 6a" em remissões ("Difere do item 2 do Lote 4", "Lote 1, item 1.8") e nos `nome`/`cargo` | vários | CONTEÚDO de navegação (os lotes são as unidades de estudo da candidata) |
| "t-4" (dentro de "gpt-4o") | L1 curso | falso positivo da minha regex sem distinção de caixa; a regex `id` da D1 diferencia caixa e não casa |
| "conferido no GAB_DEFINITIVO…" com "CEBRASPE_ANALOGA;" | L4-11 justificativa; L4 curso | DÚVIDA, ressalva R2 |
| "um canônico (A5-20)" | 5C-08 justificativa | DÚVIDA, ressalva R3 |

## 4. Achados

| # | Severidade | Achado | Encaminhamento |
|---|---|---|---|
| R1 | Baixa (coerência pós-fusão) | Remissão a lote que não existe mais. `$.lotes[L2].curso` e `L2_estudo.md:237` dizem "Adendo de pegadinha do título do edital: ver Lote 1-C.". Na camada do estudante o 1-C não existe mais como lote: o conteúdo agora fica em "## Complemento" no fim do curso do L1. Não é processo e é idêntico à v1.7. A D1 só admite deleção, então não cabe correção na produção. Relacionado, só para registro: o campo `cargo` dos 30 itens dos complementos continua "Lote 1-C/4-C/5-C", por identidade obrigatória (2.2) | Errata opcional da GCE (redação: "ver Lote 1, Complemento"). A plataforma tem de associar os itens por prefixo (contrato v1.2.5, regra 3), o que já está previsto |
| R2 | Baixa (DÚVIDA de classificação) | `$.itens[L4-11].justificativa` (`L4_gabarito.md:58`) e `$.lotes[L4].curso` (`L4_estudo.md:106`) dizem "(CEBRASPE_ANALOGA; gabarito definitivo E, conferido no GAB_DEFINITIVO_034_TRF6_002_01)". Leitura (a), CONTEÚDO: cita a fonte oficial e o rótulo que o próprio campo `rotulo` já mostra; o carimbo não tem data e não casa com a regex de carimbo da D1 ("conferid… pel[ao]"). Leitura (b), PROCESSO: "conferido no" registra o ato de verificação da fábrica, e CEBRASPE_ANALOGA é rótulo interno de proveniência (CLAUDE.md), fora da lista ampliada da D-T12-V13 (a). Fica no mesmo período de Y1 (L4-11) | gbq-gerencia arbitra. Se prevalecer (b), a retirada é deleção possível ("(CEBRASPE_ANALOGA; …)") e exige nova D1 (nova entrada de regra) |
| R3 | Baixa (DÚVIDA de classificação) | `$.itens[5C-08].justificativa` (`L5_gabarito.md:151`) diz "É o item deste lote mais próximo de um canônico (A5-20)". Leitura (a), CONTEÚDO: "canônico" no sentido de item clássico/padrão do tema. Leitura (b), PROCESSO: alude ao estatuto "canônico" da fábrica (Lote 5 × complemento), o que, depois da fusão, também perde sentido para a candidata | gbq-gerencia arbitra; se (b), errata da GCB |
| I1 | Informativo | Y1 (L4-11, "O F4 afirma que") continua literal, como manda a D1 (DÚVIDA prevista) | Errata da GCB, se ela quiser |
| I2 | Informativo | A `legendaMecanismo` do L5C ("Mecanismo: …") difere da do L5 ("Mecanismos: …") e não aparece no L5 fundido; os códigos são os mesmos. Consequência já registrada pela D1 (3.1) e no relatório | Nenhum |
| I3 | Informativo | O pedido dizia que o disco estava em CRLF. Os arquivos promovidos estão em LF no disco (0 CRLF em pacote.json, pacote_estudante.json, contrato e nos 34 da edição). Nenhum SHA é afetado | Nenhum |
| I4 | Informativo | O relatório da produtora (`pacote_relatorio_2026-10-17_v1_8.md`) declara os mesmos 4 SHA de controle que eu calculei e registra o Adendo 1, Y1 e a nota do L5C | Nenhum |

## 5. Contagens

- Itens: 286 conferidos; 286 aprovados; 0 corrigir; 0 reprovados; 0 não verificados.
- Edição: 34 arquivos conferidos (26 idênticos + 8 alterados conforme o previsto), 9 retiradas conforme o previsto, 0 divergências.
- Campos de texto do estudante conferidos contra a edição v1.7 e a v1.8: 7 resumos, 7 cursos, 262 pegadinhas (inclui as 4 do L1C), 139 pares, 180 justificativas, 5 + 5 textos de discursiva, 19 aspectos, 19 quesitos, 76 conceitos. Divergências: 0.
- Varredura R: JSON 9 (X1–X8, Y1), edição 11, processo 0.
- Ressalvas: 3 baixas (R1–R3), 2 das quais com as duas leituras para arbitragem; 4 informativos.
