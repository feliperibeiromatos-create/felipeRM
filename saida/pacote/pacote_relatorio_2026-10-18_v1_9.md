# pacote_relatorio_2026-10-18_v1_9.md — T-94 — 2026-10-18 — gerado por gbq-gerencia

REMETENTE: gbq-gerencia (geração da v1.9, executando a própria D1: `saida/pacote/T94_D1_v1_9_2026-10-18.md`).
DESTINATÁRIO: gbq-cqe (fidelidade, com leitura própria; `saida/pacote/fidelidade_v1_9_gbq-cqe.md`); depois gbq-gerencia (reconciliação e gatilho A). Cópia: orquestrador. Sem commit (do orquestrador). Nada vai à plataforma nem à candidata.

## 1. Arquivos de saída: SHA-256 e bytes (conteúdo LF)

| Arquivo | Bytes | SHA-256 |
|---|---|---|
| `saida/pacote/pacote.json` v1.9 (= `gerador_v1_9/out/pacote.json`) | 663235 | `1366055496457792bf55f541d901e2d1f277ee42611060b03bbf82b4427610bb` |
| `saida/pacote/pacote_estudante.json` v1.9-E (= `out/pacote_estudante.json`) | 642374 | `8fa81b45a92095f8973c2787083d144869fdc195031455f7ff75ecb337e509e2` |
| `regras/pacote_contrato.md` v1.2.6 | 39544 | `7e749c88ae1e194a38529e13105b5b43c53571e0e06d76747cab21fb83d510a8` |
| `saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo1_2026-10-18.md` (= `out/registro_adendo1.md`) | 14248 | `801a0724462521e30f5fedcd4b1b8aef772491a2621c80e3a39e130aaaaf8df9` |
| `saida/pacote/gerador_v1_9/MANIFESTO.md` | — | SHA-256 de cada arquivo do gerador e de `out/` no próprio manifesto (passo 7) |

Base: v1.8 aceita (D-PACOTE-V18), `git show 46496ca:saida/pacote/pacote.json` = `09d4a457…` (621907 bytes) e `…/pacote_estudante.json` = `851e2370…` (602815 bytes). Determinismo: o pipeline completo rodou várias vezes (uma com `PYTHONHASHSEED=7`) e deu sempre os mesmos SHA. Não há leitura de relógio. O `geradoEm` é literal no `build_v19.py` e no `estudante_json.py`.

## 2. Diff v1.8 → v1.9

| Caminho | v1.8 | v1.9 |
|---|---|---|
| `$.geradoEm` | `2026-10-17` | `2026-10-18` |
| `$.nome` | `Câmara 2026 — pacote F4 (v1.8)` | `Câmara 2026 — pacote F4 (v1.9)` |
| `$.itens` | 286 | 334 (os 286 da v1.8, idênticos e na mesma ordem, mais 48 no fim) |

`edital` (47), `simulados` (4), `lotes` (10) e `discursivas` (5) estão idênticos. A reconstrução prova que os 286 não mudaram: tirar os 48 do fim e voltar `nome` e `geradoEm` dá a v1.8 byte a byte (`conferencias_v19.py`, (0)). O `pacote_estudante.json` segue o mesmo padrão frente à v1.8-E: nome "… (v1.9-E)", data, 48 itens no fim e reconstrução byte a byte (conferência (1)).

## 3. Contagens

| Quesito | v1.8 | v1.9 |
|---|---|---|
| itens | 286 | 334 |
| C / E | 149 / 137 | 172 / 162 |
| banco / AUTORAL | 106 / 180 | 106 / 228 |
| `volatil` | 23 | 25 (+ L2-R07, L2-R18) |
| aderência parcial | 39 (banco) | 45 (+ L2-R02, R14, R15, L3-R01, R02, R05) |
| "QA PENDENTE" | 0 | 0 |
| lotes (dados / estudante) | 10 / 7 | 10 / 7 |
| simulados | 4 | 4 (sem item de reforço) |

Reforço da onda 1:

| Lote | Itens | C | E | [TS] | VOLÁTIL | Parcial | Arquivo final (SHA-256 da decisão de aceite) |
|---|---|---|---|---|---|---|---|
| L1 | 18 | 9 | 9 | 7 | 0 | 0 | `saida/gce/L1_reforco_onda1_v2.md` (`75e4a535…`) |
| L2 | 18 | 8 | 10 | 10 | 2 | 3 | `saida/gce/L2_reforco_onda1_v3.md` (`cff8b71e…`) |
| L3 | 11 | 6 | 5 | 5 | 0 | 3 | `saida/gce/L3_reforco_onda1_v3.md` (`79404c22…`) |
| L6A | 1 | 0 | 1 | 1 | 0 | 0 | `saida/gcb/L6_reforco_onda1_v3.md` (`58933b0a…`) |
| Onda 1 | 48 | 23 | 25 | 23 | 2 | 6 | 47,9% de C (faixa de 40% a 60%) |

Itens por folha depois da v1.9 (banco e AUTORAL):
- P2-1.1 a 1.8, 2.1 a 2.8, 3.1 a 3.4, 4.2 e 4.3, e P1-3: 6 cada (23 folhas com item novo; meta intermediária da D-REFORCO-1; corrigido na reconciliação, A-1 da fidelidade: o texto dizia "25 folhas");
- P1-4.3: 4 (sem item novo; a meta fica com a T-102). A onda 1 tem 24 folhas: as 23 acima e a P1-4.3.

L6B-R01 e L6B-R02 não entram (SUSPENSOS).

## 4. Pacote do estudante (v1.9-E)

O total de remoções é 760, em 38 regras: as 709 da v1.8 (36 regras, iguais), mais 48 de url AUTORAL e mais 3 do reforço, em 2 regras novas (`reforco_marcas.py`, lista fechada da D1, seção 3):

| Regra | Itens | Ocorrências |
|---|---|---|
| V (classificação interna de VOLÁTIL no início da justificativa do reforço) | L2-R07, L2-R18 | 2 |
| V (instrução de montagem e de reescrita do item volátil, L2-R18) | L2-R18 | 1 |
| url AUTORAL (valor inteiro apagado) | os 48 | 48 (228 no total) |

- Campos comparados no teste de só deleção: 1313 (1265 + 48), com 0 falha.
- CAIXA 8/8 e REALINHA 2/2 continuam como na v1.8.
- Varredura R: 9 casamentos (X1–X8, Y1; os mesmos da v1.8) e 0 de processo.
- Termos fora da lista, só contagem, sem ação: "Presidente" 24 (+9), "Projeto" 236 (+48, campo `certame`), "Whisper" 26 (+5), "insumo" 3 (+1); os demais, como na v1.8.
- Lotes do estudante e contagem por prefixo (contrato v1.2.6, ponto 1): L1 48 (30 + 18), L2 48, L3 41, L4 30, L5 30, L6A 16, L6B 15.

## 5. Validadores (pipeline completo, `sh gerador_v1_9/rodar_tudo.sh`, código 0)

| Passo | Script | Resultado |
|---|---|---|
| 1 | `build_v19.py` | 334 itens; base v1.8 com SHA conferido; 48 lidos com os SHA das decisões e as contagens das decisões (falha se divergir) |
| 2 | `estudante_json.py` | 0 falhas (estrutura, identidade fora da lista, só deleção, CAIXA/REALINHA, varredura R, contagem por lote, deleções do reforço = lista fechada) |
| 3 | `registro_adendo_v19.py` | adendo 1 com 48 itens, igual ao promovido |
| 4 | `validate_v19.py` | 47/47 OK (rótulo da linha 119 corrigido na reconciliação, A-1: "23 folhas"; verificação e lista `FOLHAS` sem mudança; pipeline rodado de novo com código 0 e os mesmos 3 SHA de saída; MANIFESTO atualizado só em 3 linhas: `validate_v19.py`, `out/validate_stdout.txt` e `out/validate_v19.json`) |
| 5 | `conferencias_v19.py` | 23/23 OK, entre elas 9 testes negativos (gabarito trocado, campo `nucleo`, item retirado, aderência, volatil, texto novo no estudante, linha Base na justificativa, 1 espaço num item da v1.8, 1 caractere a menos na v1.8-E), todos acusados |
| 6 | `validar_erros_teste.py` (herdado, sem mudança) | 12/12 OK com o pacote v1.9 |
| 7 | `manifesto_v1_9.py` | `MANIFESTO.md` com SHA-256 e bytes de cada arquivo do gerador e de `out/`; saídas promovidas iguais à origem: sim (3/3) |

Os scripts herdados que regeneram a partir das fontes (`build_pacote.py`, `estudante_gen.py` como programa, `estudante_fidelidade.py`, `sync_check.py`, `validate.py`, `conferencias_v18.py`, `fidelidade_mutacao.py`, `relatorio_v1_8.py`, `manifesto_v1_8.py`) não rodam na v1.9 (D1, D-V19-04).

Gerador frente à v1_8 (lista fechada, conferida em (4)):
- alterados: `estudante_gen.py` (prefixos `L6A`/`L6B` em `lote_of`), `estudante_json.py` (nome, data, ramo do reforço e contagens), `refs.py` (`C_V18 = '46496ca'`) e `rodar_tudo.sh`;
- novos: `_run.py`, `build_v19.py`, `reforco.py`, `reforco_marcas.py`, `registro_adendo_v19.py`, `validate_v19.py`, `conferencias_v19.py` e `manifesto_v1_9.py`.

## 6. Pastas intactas

`git status` está vazio em `banco/`, `saida/pacote/gerador_v1_8/`, `saida/estudante/` (edição v1.8, que não é objeto), `saida/simulados/`, `saida/plataforma/` e `saida/treino/`, nos 4 arquivos finais do reforço e no registro v3. O repositório mudou só em:
- `saida/pacote/pacote.json` e `pacote_estudante.json`;
- `regras/pacote_contrato.md` (v1.2.6);
- `saida/pacote/gerador_v1_9/`;
- os registros `saida/pacote/contrato_v1_2_6_2026-10-18.md`, `saida/pacote/T94_D1_v1_9_2026-10-18.md` e este relatório;
- `saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo1_2026-10-18.md`;
- `saida/banco/T93_reconciliacao_2026-10-18.md` (T-93).

## 7. DÚVIDAS e pendências (não tocadas)

- O L4-11 em disco (`GCB_Lote4_v3_canonica_GCB-CPP.md`) já traz o texto do Erratum 1 devolvido (D-L4-T83-DEVOLVIDO). A v1.9 mantém o da v1.8. Antes de regenerar a partir das fontes, a GCB tem de restaurar o arquivo ou a GBQ tem de fixar o texto (D1, D-V19-03 (d)).
- 5C-08 (D-TRANSPORTE-L5C-T83) e L2 curso (D-L2-T84-ERRATA): adiados para a v1.10 (D-V19-03 (b) e (c)).
- 38 itens DA do banco (BQ-0113 a BQ-0152) fora do pacote: o edital do pacote não tem P1-DA (D-V19-03 (a)).
- Campo `nucleo`: v1.10 (D-V19-05).
