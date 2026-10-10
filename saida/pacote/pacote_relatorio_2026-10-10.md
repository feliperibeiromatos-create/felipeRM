# pacote_relatorio_2026-10-10.md — T-27 — 2026-10-10 — gerado por gbq-csc

Saída: `saida/pacote/pacote.json` v1.1 (`"versao": 1` mantido; v1.1 indicada em `"nome"`: "Câmara 2026 — pacote F4 (v1.1)"; `geradoEm` 2026-10-10; 541532 bytes UTF-8 mais a quebra final de linha). Contrato: `regras/pacote_contrato.md` v1.1 (T-26) e a decisão D1 da GBQ de que a regra de aderência vale sem distinção de maiúsculas e minúsculas (`saida/banco/GBQ_reconciliacao_2026-10-10_lote1.md`, seção 5; T-38). Gerador: scripts no scratchpad da sessão (`.../scratchpad/s3/t27/`, fora do repositório). Nenhum outro arquivo do repositório foi alterado; `git` não foi usado. Nada deste pacote vai à candidata sem a conferência da gbq-gerencia, o gatilho A e a decisão do Fundador.

## 1. Fontes

| Objeto | Arquivo | Observação |
|---|---|---|
| L1 | `saida/gce/GCE_Lote1_v2_CPP.md` | erratas E1–E5, E9, E10 aplicadas no texto; E7/E8 (D1) e E4a–c da consolidação, como na v1 |
| L1C | `saida/gce/GCE_Lote1C_v2_CPP.md` | erratas E1 e E3, como na v1 |
| L2 | `saida/gce/GCE_Lote2_v2_CPP.md` | **T-28 CONCLUÍDA incorporada** (curso lido do arquivo atual: "Derep (antigo DETAQ)" e reembrulho da linha 152); erratas E1a–d, E2, E3b, E5, E6 como na v1; padrões D2/D3 em `GCE_Lote2_padroes_GCE.md` |
| L3 | `saida/gce/GCE_Lote3_v2_CPP.md` | **T-08 CONCLUÍDA incorporada** (bloco "CONTEXTO NORMATIVO INTERNO", sem item, no curso do 3.1, já com [NORMATIVO — QA] da G1); erratas E1a–b, E2, E3a–b como na v1; padrões D4/D5 em `GCE_Lote3_padroes_GCE.md` |
| L4 | `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` | arquivo atual (v3.4 pela T-32 CONCLUÍDA; ver seção 5, item 3) |
| L4C | `saida/gcb/GCB_Lote4C_v1_GCB-CPP.md` | só itens AUTORAL |
| L5 | `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` | sem mudança |
| L5C | `saida/gcb/GCB_Lote5C_v1_GCB-CPP.md` | só itens AUTORAL |
| L6A | `saida/gcb/GCB_Lote6a_v2_producao_auto.md` | **reextraído com a errata T-17** |
| L6B | `saida/gcb/GCB_Lote6b_v2_producao_auto.md` | **reextraído com a errata T-17** (A-6b-1 mantida) |
| Registro AUTORAL | `saida/gbq/claude_GBQ_Registro_AUTORAL_v3.md` | 180 itens (T-30); substitui a v2 na conferência |
| Banco | `banco/banco.csv` | 112 linhas; exportadas só BQ-0001 a BQ-0066 com gabarito C/E (60) |
| Simulados | `saida/simulados/simulado_0_v0.2.md` + gabarito; `simulado_1.md` + gabarito | comando dos itens de banco extraído do bloco "Comando" do SIM-0 v0.2 (regra 3 do contrato v1.1) |
| Edital | `edital/TI_itens_1_4_P1.md`, `edital/TI_itens_5_8_P1.md`, `edital/modulo_RF_IA_P2.md` | 47 entradas, igual à v1 |

## 2. Contagens

- edital: 47 entradas (P1 itens 1–4: 8; P1 itens 5–8: 12; P2: 27).
- itens: 240 = 60 do banco + 180 AUTORAL; 122 C / 118 E. Banco: 33 C / 27 E; aderência 23 parcial / 37 direta. AUTORAL: 89 C / 91 E, todos "direta".
- banco: 112 linhas no CSV; BQ-0001 a BQ-0066 = 66 linhas (60 C/E + 6 anuladas X: BQ-0029, 0030, 0031, 0060, 0062, 0063); **BQ-0067 a BQ-0112 (46 linhas) fora do pacote** até a T-42 (colunas `texto_comando`/`texto_base`; regra 3 do contrato v1.1).
- `volatil: true`: **19** (banco 4: BQ-0015, 0017, 0035, 0064; AUTORAL 15: L1-Q14, Q16, Q18, Q19; **L3-Q21** (REVERIFICAR normativo, R1-N); L4-15; A5-14, A5-15, A5-16, A5-17; 6A-01, 09, 10, 14, 15). Campo ausente nos demais (nunca `false`).
- [TS] (não exportado como campo): 91 no registro v3 (P2 45; P1 46).
- simulados: **2**.
  - SIM-0 "Simulado 0 — diagnóstico (v0.2)", tipo diagnóstico: 60 ids do banco, na ordem do simulado (33 C / 27 E; 4 VOLÁTEIS; 23 parciais).
  - SIM-1 "Simulado 1 — P1 final (TI e Dados, itens 5 a 8)", tipo final: 40 ids AUTORAL na ordem do simulado (20 C / 20 E; 19 [TS]; 0 volátil; 0 parcial; L4 16, 4-C 4, L5 14, 5-C 6).
- discursivas: 5 (D1, D2, D4 questão: 14,30 + 0,70 = 15,00; D3, D5 peça: 28,50 + 1,50 = 30,00), como na v1; D4 e D5 com o anexo de correção.

| Lote | AUTORAL | C | E | VOLÁTEIS / REVERIF. | itens do edital cobertos | curso (car.; variação sobre a v1) | resumo (car.) | pares | pegadinhas |
|---|---|---|---|---|---|---|---|---|---|
| L1 | 20 | 10 | 10 | 4 | P2-1.1, P2-1.2, P2-1.3, P2-1.4, P2-1.5, P2-1.6, P2-1.7, P2-1.8 | 22641 (+0) | 2446 | 17 | 8 |
| L1C | 10 | 4 | 6 | 0 | P2-1.1, P2-1.2, P2-1.3, P2-1.4, P2-1.5 | 2374 (+0) | 0 | 0 | 1 |
| L2 | 30 | 15 | 15 | 0 | P2-2.1, P2-2.2, P2-2.3, P2-2.4, P2-2.5, P2-2.6, P2-2.7, P2-2.8 | 20011 (-39) | 2609 | 22 | 8 |
| L3 | 30 | 16 | 14 | 1 | P2-3.1, P2-3.2, P2-3.3, P2-3.4, P2-4.1, P2-4.2, P2-4.3 | 26978 (+1612) | 2594 | 28 | 7 |
| L4 | 20 | 10 | 10 | 1 | P1-5.1, P1-5.2, P1-5.3, P1-6 | 34278 (+28) | 4243 | 20 | 32 |
| L4C | 10 | 5 | 5 | 0 | P1-5.1 | 0 (+0) | 0 | 0 | 0 |
| L5 | 20 | 10 | 10 | 4 | P1-7.1, P1-8.1, P1-8.2, P1-8.3, P1-8.4 | 18901 (+0) | 3471 | 15 | 14 |
| L5C | 10 | 5 | 5 | 0 | P1-8.2, P1-8.4 | 0 (+0) | 0 | 0 | 0 |
| L6A | 15 | 7 | 8 | 5 | P1-1, P1-3 | 25052 (+1) | 3059 | 19 | 35 |
| L6B | 15 | 7 | 8 | 0 | P1-2, P1-2.1, P1-4.1, P1-4.2, P1-4.3 | 37108 (-179) | 4348 | 18 | 39 |

## 3. Inclusões e exclusões de simulados (regra 5 do contrato v1.1)

| Simulado | Decisão | Motivo |
|---|---|---|
| SIM-0 v0.2 | **incluído** | T-25 CONCLUÍDA e reconciliada pela GBQ (mapa = banco: 60/60 em aderência, VOLÁTIL, gabarito e subitem, conferido por script nesta tarefa); T-13 CONCLUÍDA sem gatilho D (17/17 gabarito mantido); T-21 idem (BQ-0036 e BQ-0040). |
| Simulado 1 | **incluído** | canônico por D-SIM1-CANONICO (gatilho A aceito; QA independente APROVADO/CONFERIDO 40/40, T-34 R2; T-31 e T-35 aplicadas; reconciliação `T34_reconciliacao_2026-10-10.md`). Conferido nesta tarefa: 40 ids do mapa existem em `itens`, rótulo AUTORAL, gabarito do pacote = mapa 40/40, 20 C / 20 E, 0 volátil, 0 parcial, sem L4-11 e sem BQ-0010. |
| Simulado 2 | **não incluído** | aguarda o aceite (gatilho A pendente); a regra 5 exige as condições da decisão de aceite cumpridas. |
| Simulado 0-P2 | **não incluído** | em produção (T-24 EM CURSO; os arquivos `simulado_0_P2*.md` existem como rascunho, sem reconciliação nem aceite). |

Observação: as marcas e a nota de vigência do SIM-0 pendentes na T-36 (PENDENTE) não afetam o pacote, que lista só ids do banco; as aderências e o `volatil` vêm do banco. A liberação do SIM-0 e do SIM-1 à candidata continua reservada ao Fundador.

## 4. Validações (todas OK; as da T-05 refeitas e ampliadas)

- JSON relido do disco e parseado sem erro; 8 chaves de topo; `versao` 1.
- Nenhum item sem id, enunciado e gabarito C/E; 240 ids, 0 duplicados.
- Contagem por lote igual à declarada (L1 20, L1C 10, L2 30, L3 30, L4 20, L4C 10, L5 20, L5C 10, L6A 15, L6B 15 = 180) e igual ao registro v3.
- AUTORAL contra o registro v3: ids 180/180; gabarito 180/180; subitem 180/180 (asserções no gerador e conferência independente); [TS] 180/180; VOLÁTIL + REVERIFICAR = 15/15; totais 89 C / 91 E; 91 [TS].
- Banco contra `banco.csv` (BQ-0001 a 0066): ids, gabarito, texto e `itemEdital` 60/60; 33 C / 27 E; 6 anulados fora; texto de cada item do simulado = `texto_integral` do banco, 60/60; comando não vazio 60/60 (34 comandos distintos); `textoBase` só em BQ-0049, 0050 e 0051.
- Aderência (regra 2, sem distinção de caixa): 23 parcial / 37 direta; conjunto idêntico ao das 23 linhas PARCIAL do mapa do SIM-0 v0.2 (diferença simétrica vazia). `aderencia` só direta|parcial.
- Todo `itemEdital`, `itensEdital` e `pegadinhas.itemEdital` existe no `edital`.
- `justificativa` não vazia em todo AUTORAL e vazia em todo item de banco; rótulos permitidos.
- Nenhum texto exportado contém "QA PENDENTE", "ENTREGA DE LOTE", "FIM DA PARTE", "FIM DO LOTE", "Fundador: gravar" ou linhas "=====".
- **Lotes 6 (item 1 da T-27):** 0 ocorrência de "Observação para a GCB-CQFP" e 0 de "Derep, antigo DETAQ" tanto nos arquivos canônicos `GCB_Lote6a_v2_producao_auto.md` e `GCB_Lote6b_v2_producao_auto.md` quanto no JSON (lotes e itens 6A/6B). A forma "Derep (antigo DETAQ)" aparece 12 vezes no JSON; a única "Derep, antigo DETAQ" é a do L1 (E10, aceita pela D1 GBQ).
- **Item 2 da T-27:** L3-Q21 com `"volatil": true`; total 19 (banco 4, AUTORAL 15).
- **Item 3 da T-27:** `padrao` de D4 e de D5 termina com "Notas de correção (GCE, R2–R4)" seguida das linhas 14 a 23 de `saida/gce/GCE_Lote3_padroes_GCE.md` (R2, R3, R4), cópia literal conferida por igualdade de cadeia; R1 e R5 não vão (D1 GBQ).
- Erratas da produção aplicadas por substituição tolerante a quebra de linha, cada uma com exatamente 1 ocorrência (26 aplicações, como na v1); 28 quebras de linha hifenizadas reparadas (como na v1). Nenhuma errata nova de gerador foi necessária: os arquivos de lote já trazem T-08, T-17, T-28 e T-32.
- Soma dos aspectos das discursivas: questões 14,30 + 0,70 = 15,00; peças 28,50 + 1,50 = 30,00.

## 5. Diff de contagens v1 → v1.1

| Objeto | v1 (T-05) | v1.1 (T-27) |
|---|---|---|
| bytes do JSON | 537983 | 541532 (+3549) |
| `nome` | "Câmara 2026 — pacote F4" | "Câmara 2026 — pacote F4 (v1.1)" |
| edital | 47 | 47 (idêntico) |
| itens (total / banco / AUTORAL) | 240 / 60 / 180 | 240 / 60 / 180 |
| C / E (total, banco, AUTORAL) | 122/118; 33/27; 89/91 | 122/118; 33/27; 89/91 |
| aderência do banco | 23 parcial / 37 direta | 23 parcial / 37 direta |
| `volatil: true` | 18 (banco 4, AUTORAL 14) | **19** (banco 4, AUTORAL 15; + L3-Q21) |
| simulados | 1 (SIM-0) | **2** (SIM-0, SIM-1) |
| lotes | 10 | 10 |
| discursivas | 5 | 5 |

Mudanças de conteúdo (única comparação campo a campo v1 → v1.1; ids iguais; nenhuma mudança de gabarito, subitem, enunciado ou aderência):
1. Item L3-Q21: campo `volatil` acrescentado.
2. Item L4-11, `justificativa`, e pegadinha do L4 (P1-5.3): "gabarito a confirmar contra o GAB_DEFINITIVO" → "gabarito definitivo E" (L4 v3.4, T-32 CONCLUÍDA; sem mudar gabarito).
3. Curso do L2 (−39 car.): "Derep (antigo DETAQ)" e reembrulho (T-28). Curso do L3 (+1612 car.): bloco T-08 (Ato da Mesa nº 225/2025; sem item). Curso do L4 (+28 car.): D-DEREP da T-32. Curso do L6A (+1 car.): "Derep (antigo DETAQ)" (T-17(b)). Curso do L6B (−179 car.): "Derep (antigo DETAQ)" (T-17(b)) e retirada da nota "Observação para a GCB-CQFP" (T-17(a)). Resumos, pares e pegadinhas: iguais, exceto o ponto 2.
4. `padrao` de D4 (+649 car.) e D5 (+649 car.): anexo R2–R4. D1, D2 e D3 iguais.

## 6. Escolhas, mapeamentos e pendências (a conferir pela Gerência)

1. **Mapeamentos da v1 mantidos** (extensões 4 a 11 da seção 4 do relatório da T-05): `comando`/`textoBase` do banco pela regra 3; `certame`, `cargo` e `url` do banco sem encurtar; campos dos AUTORAL; 4-C e 5-C sem curso, resumo e pares; pegadinhas, pares e conceitos das discursivas pelos mesmos critérios.
2. **Aderência:** a regra 2 do contrato v1.1 foi aplicada sem distinção de caixa e com as três expressões literais do contrato ("parcial", "aderência temática ampla", "aderência apenas por tema"); o resultado é o da v1 (23 parciais), igual ao mapa do SIM-0 v0.2.
3. **T-32 não estava na lista de itens da T-27**, mas o L4 canônico atual (v3.4) já a contém; o pacote lê o arquivo atual, como manda o contrato (fonte única). O efeito é só o do item 2 da seção 5 e a forma D-DEREP no curso do L4; nenhum gabarito mudou.
4. **Rótulo interno no curso do L3.** O bloco do T-08 foi copiado literalmente do arquivo canônico e leva o título "CONTEXTO NORMATIVO INTERNO (ERRATA T-08, 10/10/2026; SEM ITEM)" e a nota de processo "(registro da GCB-CQFP, 08/10/2026)"; como o curso vai à candidata, a Gerência/GCE decide se o rótulo "ERRATA T-08" deve sair por errata de forma. Não alterei o texto (regra: extrair literalmente).
5. **Itens do L6B / 96 e 98:** a divergência TRF6 96/98 (texto do 6b "parcial ao item 4/4.1" × banco P1-4 direta) deixou de existir no texto exportado (T-17(e)); o pacote continua usando o banco (direta). Esses dois itens reais ficam fora do 6b, como no registro v3 (R3-b).
6. **Itens do banco e T-13/T-21:** os 16 itens de LGPD exportados (os 17 da T-13 menos BQ-0031, anulado), BQ-0036 e BQ-0040 saem com o gabarito do banco (mantido pelo qa-normativo). Nas `observacoes` não exportadas constam as notas de vigência (BQ-0040: Resolução CNJ 332/2020 revogada pela 615/2025; BQ-0003: ANPD = Agência Nacional de Proteção de Dados, Lei 15.352/2026); o JSON não tem campo para elas (a nota no simulado segue pela T-36).
7. **Itens `volatil` e simulados:** o SIM-0 (diagnóstico) contém 4 VOLÁTEIS e 23 parciais, aptos só a diagnóstico; o SIM-1 (final) não contém nenhum. Contrato: a plataforma não deve usar item `volatil` em simulado final antes de 4–8/1/2027.
8. **Fora do pacote por regra:** BQ-0067 a BQ-0112 (T-42); Simulado 2 (gatilho A pendente); Simulado 0-P2 (em produção); [TS] (sem campo no contrato; BACKLOG da D1 GBQ).
9. **Próximo passo:** conferência por script da gbq-gerencia e gatilho A. Este arquivo e o `pacote.json` não alteram `TAREFAS.md`, que a Gerência/orquestrador atualizam.
