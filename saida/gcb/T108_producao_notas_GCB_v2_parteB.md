# T108_producao_notas_GCB_v2_parteB.md — T-108, GCB, Parte B (lote 6a), v2 após o QA R1 — 2026-10-18 — gerado por gcb-cpp

Arquivo gravado: `saida/gcb/T108_substituicoes_GCB_parteB_v2.csv` (182 linhas: 175 da v1 + 7 novas). Texto-base: `saida/pacote/pacote.json` v1.10, SHA-256 LF d43c32de… (conferido). Instrução: seção 5 de `T108_D1_pos_R1_GCB_2026-10-18.md`. Nada foi editado fora deste arquivo e do CSV v2; sem commit.

## 1. Resposta ao QA R1 (parecer B), item a item

| Item do QA | Resposta | Onde |
|---|---|---|
| 4.1-1 GCB-B0020 (instrução de reverificação) | ACEITO. `depois` com o texto exato do parecer; `nota` corrigida para o texto do parecer. | v2, linha B0020 |
| 4.1-2 GCB-B0058 ("o lote NÃO cobra") | ACEITO. `depois` = `fica fora do estudo o ponto`. Resultado: "por isso fica fora do estudo o ponto "como alterar a permissão de um link existente"." | v2, linha B0058 |
| 4.1-3 GCB-B0103 (`fonte_origem` sem F21) | ACEITO. `fonte_origem` com F20, F21 e F22. `antes` e `depois` iguais à v1. | v2, linha B0103 |
| 4.2 ressalva B0027 ("O item sobre mesclar células usa…") | Mantida como está (D1 pós-R1, seção 1: reescrever seria texto novo). | linha igual à v1 |
| 4.2 ressalva "Conforme Microsoft, documentação de suporte" | Mantida (forma de nome fixada na seção 2 do D1). | linhas iguais à v1 |
| 4.2 ressalva "invertida" de dois jeitos (B0145 × B0149) | ACEITO pelo D1 pós-R1, seção 3: forma única ", às avessas" em B0145 ("Armadilha: generalização indevida, às avessas (") e B0149 ("Armadilha: troca de conceito, às avessas ("). Resto do `depois` igual. | v2, linhas B0145 e B0149 |
| 5 pendência: "nada sobre isso entra em item" (1.1.2 e 1.1.3) e "esses pontos não entram em item…" (3.2.2) | ACEITO como linhas adicionais (GCB-EXTRA-05, 06, 07). | B0176, B0177, B0178 |
| 5 pendência de menor peso: "abertas hoje" e "sem fonte aberta hoje" | ACEITO (D1 pós-R1, seção 4): EXTRA-10 caso (b), data do lote; EXTRA-11 caso (c), sem data. | B0181, B0182 |
| Registro: FP-R1 da tecla F4 casada por texto, não por id | Anotado. "A tecla F4…" está fora de todo `antes` e intacta após a aplicação. | autoconferência (5) |

## 2. Linhas corrigidas (5)

GCB-B0020, GCB-B0058, GCB-B0103 (QA) e GCB-B0145, GCB-B0149 (D1 pós-R1, seção 3). Todas as outras 170 linhas da v1 estão idênticas à v1 (campos iguais e mesma ordem de colunas; o CSV é regravado com o mesmo escritor, e o ida-e-volta da v1 reproduz a v1 byte a byte).

## 3. Linhas novas (7), ids_ocorrencia = GCB-EXTRA-nn

| id_edicao | EXTRA | caminho | `antes` → `depois` | ação | cat. / regra |
|---|---|---|---|---|---|
| GCB-B0176 | EXTRA-05 | lotes[L6A].curso (1.1.2) | "acompanhamento; nada sobre isso entra em item." → "acompanhamento." | SUBSTITUIR | C10 / 5 |
| GCB-B0177 | EXTRA-06 | lotes[L6A].curso (1.1.3) | "células; nada sobre isso entra em item." → "células." | SUBSTITUIR | C10 / 5 |
| GCB-B0178 | EXTRA-07 | lotes[L6A].curso (3.2.2) | "; esses pontos não entram em item além da descrição acima" → vazio | DELETAR | C10 / 5 |
| GCB-B0179 | EXTRA-08 | itens[6A-08].justificativa | "; não sutil" → vazio (fica "(inversão)") | DELETAR | C06 / 4 |
| GCB-B0180 | EXTRA-09 | itens[6A-11].justificativa | "; não sutil" → vazio (fica "(inversão)") | DELETAR | C06 / 4 |
| GCB-B0181 | EXTRA-10 | lotes[L6A].curso (1.0.1) | "abertas hoje" → "consultadas em 08/10/2026" | SUBSTITUIR | C10 / 5 |
| GCB-B0182 | EXTRA-11 | lotes[L6A].curso (3.2.1) | "sem fonte aberta hoje" → "sem fonte consultada" | SUBSTITUIR | C10 / 5 |

Nenhuma absorção em linha existente: nenhum `antes` novo se sobrepõe a outro. Em 3.2.1 o "; sem item" já tinha saído pela linha aprovada (B0061/B0094), então só o "hoje" restava. A data 08/10/2026 consta da tabela do Lote 6a de `T108_fontes_GCB.md`. Nenhum fato novo.

## 4. Autoconferência (python -I, somente leitura, cópia em memória)

1. diff v1 × v2: alteradas = B0020, B0058, B0103, B0145, B0149; novas = B0176 a B0182; total 182. OK.
2. `antes` literal e único no campo em 182/182; 0 sobreposições. OK.
3. Cobertura: 199 ocorrências do 6a do CSV (0 faltando, 0 duplicadas, 0 id estranho) mais EXTRA-05 a 11, uma vez cada. OK.
4. Nenhum DELETAR com `depois` não vazio; nenhum SUBSTITUIR com `depois` vazio. OK.
5. Aplicada a v2 e rodada a varredura do `T108_inventario.py`: 6a com 0 PROCESSO e 0 VERIFICAR; 36 FP (1 FP-R1 + 35 FP-CONTEUDO), iguais aos de antes; "A tecla F4…" intacta; nenhum campo de item além de `justificativa` alterado (enunciado, gabarito, itemEdital intactos). OK.
6. Texto resultante do 6a (curso, resumo, pegadinhas, justificativas): 0 casamentos de "(O11)", "fundamenta item", "neste chat", "não sutil", "entra em item", "entram em item", "(CI,", "hoje", "ITENS REAIS", "TC invertida", "indevida invertida" e "em sentido invertido"; ", às avessas" aparece 2 vezes (B0145 e B0149). OK.

Pendências: nenhuma na Parte B. A linha CI de `T108_fontes_GCB.md` e as EXTRA-13 a 22 são da Parte C, fora deste lote.
