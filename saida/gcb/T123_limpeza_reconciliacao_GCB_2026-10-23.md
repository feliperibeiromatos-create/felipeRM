# T123_limpeza_reconciliacao_GCB_2026-10-23.md — T-123 (pacote v1.14, seção 3: limpeza das justificativas do reforço de DA) — 2026-10-23 — gerado por gcb-gerencia

Objeto: reconciliação da GCB (D1 de forma; passo 3.4 do D1 da GBQ) da limpeza das marcas de produção nas justificativas dos 238 itens de reforço de DA.
Normas: `saida/gcb/T123_limpeza_D1_GCB_2026-10-23.md` (D1 de método; seção 1, itens 6 e 7) e `saida/pacote/T123_D1_v1_14_2026-10-23.md` (seções 3 e 8.1).
A GCB não escreve em DECISOES.md nem nos estados de TAREFAS.md, não produz texto de substituição e não faz commit.

## 1. Rito cumprido

| Etapa | Arquivo | Resultado |
|---|---|---|
| Produção v1 (gcb-cpp) | `saida/gcb/T123_substituicoes_DA.csv`; `T123_producao_notas_DA.md` | 91 linhas |
| QA R1 (gcb-cqfp) | `saida/gcb/QA_T123_limpeza_R1_2026-10-23_gcb-cqfp.md` | DEVOLVIDO. 89 APROVADO, 2 CORRIGIR (GCB-T123-0028 e 0032, repetição do nome na op. 6), 0 REPROVADO. A taxa de 2,2% fica abaixo do gate de 30%. |
| Produção v2 (gcb-cpp) | `saida/gcb/T123_substituicoes_DA_v2.csv` | Mudaram só as 2 linhas. |
| QA R2 (gcb-cqfp, última) | `saida/gcb/QA_T123_limpeza_R2_2026-10-23_gcb-cqfp.md` | **CONFERIDO**: 91/91, diff só nas 2 linhas, mecânica completa PASSA. |

## 2. Decisão (D1)

**ACEITA a tabela `saida/gcb/T123_substituicoes_DA_v2.csv`**, SHA-256 LF `de63b7c524797723c46690b45082d243583895846fdc144c11da8e2bfe233bde` (conferido pela GCB; 0 CR).

- **Universo.** 91 edições cobrem as 103 MARCA, cada uma uma vez, mais a GCB-EXTRA-01 ("pertinência parcial", D3-R25). Ficam 85 itens alterados e os 153 sem marca intactos.
- **Operações.** 6 (troca pelo nome da publicação): 29. 3 (deleção de marca): 39. Processo (frase ou oração de processo): 23.
- **Intocáveis.** Enunciado, gabarito, `itemEdital` e aderência ficam intactos nos 238.
- **Sem edição.** Os 4 VERIFICAR e os 2 FP ficam sem edição, como decidido na D1 de método.
- **Ressalvas de forma do QA R2.** Nas notas da produção, o cabeçalho ainda cita o SHA da v1, e a seção (c) lista 50 linhas alargadas, quando são 52. As duas ressalvas não mudam texto nem veredito. Vale o SHA da v2, acima.
- **Item não limpo.** Nenhum. Nada vai à GBQ para MANTER nem para exclusão da v1.14.

## 3. Projeção para o formato da GBQ (por script, sem mudar texto)

Script: `saida/gcb/T123_projetar_GCB.py` (`python -I`). Ele aborta se o SHA da v2 divergir.
- **Conferências do script.** Cada `antes` ocorre 1 vez na justificativa do item. Com a projeção relida, o texto resultante é igual ao da tabela aceita nos 238, e (id, antes, depois, operacao) são iguais linha a linha.
- **Conferência própria da GCB.** Aplicada a projeção sobre `reforco_bruto.json`, a C-MARCAS da seção 8.1 do D1 da GBQ dá 0 nos 238 (enunciado e justificativa). "Pertinência parcial" também dá 0. A exceção é "desconto em folha" no D3-R75.

| Arquivo (caminho que a GBQ lê) | SHA-256 LF | Bytes | Conteúdo |
|---|---|--:|---|
| `saida/gcb/DA_plataforma/DA_reforco_substituicoes.csv` | `df9f53bd7dc3f18631c77528b32683dd89e77e27dea167918fd1edee014db501` | 11.937 | 91 linhas. Colunas `id;campo;antes;depois;operacao;motivo`, ";", UTF-8, LF. `operacao` ∈ {3, processo, 6}. `motivo` = id_edicao, categoria, nota e fonte. |
| `saida/gcb/DA_plataforma/DA_reforco_registro_formato.md` | `a511fd8d3b79b806dc3a87f06d294ed346d05f2d05766089b80103d6374b820e` | 20.204 | No formato dos `D<n>_registro_formato.md`: fontes e conferências, contagem por tipo, uma entrada por substituição e os casos sem edição. |

O `montar_v1_14.py` fixa o SHA-256 do CSV acima (passo 3.4 do D1 da GBQ).

## 4. Pendência para a GBQ (registro; não é desta tabela)

**P1 (lista X da GBQ).** Nas justificativas do D2-R21 e do D2-R24, a expressão "Presidência da República" casa a regra PROCESSO de `marcas_processo.py` 2 vezes. É conteúdo: a remissão à Lei 9.007, art. 2º, parágrafo único, foi classificada como VERIFICAR, sem edição, e ficou igual antes e depois. Antes de rodar o `conferir_t123.py`, a GBQ deve registrá-la como exceção de conteúdo do critério "0 PROCESSO". Sem esse registro, o critério dá 2.

## 5. Gatilho

GATILHO A, da GCB, em PARA_PRESIDENCIA.md: aceite da tabela de limpeza para a consolidação da v1.14. Objeto: os dois arquivos da seção 3.
