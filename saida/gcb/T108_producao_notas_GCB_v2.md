# T108_producao_notas_GCB_v2.md — T-108, GCB, v2 após o QA R1 — 2026-10-18 — gerado por gcb-cpp

## Parte A (lotes 4 e 4-C) — gcb-cpp, 2026-10-18

Arquivo: saida/gcb/T108_substituicoes_GCB_parteA_v2.csv (182 linhas: 178 da v1, das quais 33 corrigidas e 145 byte a byte iguais, mais 4 novas, GCB-A0179 a A0182). Conferência: saida/gcb/T108_conferir_parteA_v2.py (python -I -X utf8, da raiz do repositório, somente leitura). Texto-base: pacote.json v1.10, SHA-256 LF d43c32de… (conferido). Saída em QUOTE_ALL, LF, como a v1.

### Resposta ao QA R1 (parecer A), item a item

| id_edicao | Achado do QA | Resposta | O que mudou |
|---|---|---|---|
| A0060, A0061, A0063, A0064, A0065, A0066, A0067, A0068, A0069, A0070, A0071, A0072, A0073, A0074, A0075, A0076, A0077, A0079, A0080, A0081, A0082, A0083, A0087, A0092, A0100, A0102, A0174 (27) | formato: DELETAR com `depois` não vazio | ACEITA | `acao` = SUBSTITUIR; `antes`, `depois`, `regra`, `nota` iguais |
| A0078 | mérito: "Não usada em item" é instrução interna | ACEITA | `antes` = " Não usada em item, por despacho da GCB." (espaço inicial); `depois` vazio; `acao` DELETAR; `regra` 5 |
| A0025 | português: faltava o artigo | ACEITA | `depois` = `as técnicas descritas pela Anthropic ("Prompt engineering overview") e pela OpenAI ("Prompt engineering").` |

Ressalvas do QA sem correção (D1 pós-R1, seção 1): A0007 e A0016 (editor repetido) ficam como estão.

### Harmonização "às avessas" (D1 pós-R1, seção 3)

| id_edicao | Item | O que mudou no `depois` |
|---|---|---|
| A0111 | L4-05 | "generalização indevida invertida (" -> "generalização indevida, às avessas (" |
| A0126 | L4-11 | idem |
| A0147 | L4-20 | "…indevida invertida. LAI" -> "…indevida, às avessas. LAI" |
| A0155 | 4C-03 | "…indevida invertida (" -> "…indevida, às avessas (" |

(Os 2 outros casos da seção 3, B0145 e B0149, são da Parte B.)

### Linhas novas (D1 pós-R1, seção 2)

| id_edicao | id | caminho | `antes` | `depois` | acao | regra | cat. |
|---|---|---|---|---|---|---|---|
| GCB-A0179 | GCB-EXTRA-01 | lotes[L4].curso | " (O11)" | vazio | DELETAR | 5 | C02 |
| GCB-A0180 | GCB-EXTRA-02 | lotes[L4].curso | " Não fundamenta item." | vazio | DELETAR | 5 | C10 |
| GCB-A0181 | GCB-EXTRA-03 | lotes[L4].curso | " neste chat" | vazio | DELETAR | 5 | C08 |
| GCB-A0182 | GCB-EXTRA-04 | itens[4C-10].justificativa | "; não sutil" | vazio | DELETAR | 4 | C06 |

Cada `antes` é literal e único no campo na v1.10 e não se sobrepõe a outra linha. Nenhuma absorção em linha existente foi necessária na Parte A. Resultado: fica "(Distinção de vocabulário: …)" sem o código, "situação de tramitação não verificada" e "TC (formato × restrição)" (que a A0178 troca por "Armadilha: troca de conceito (formato × restrição)").

### Autoconferência (T108_conferir_parteA_v2.py): TUDO OK

1. diff v1 × v2: 33 corrigidas, 4 novas, 0 removidas, ordem preservada.
2. `antes` literal e único; sem sobreposição no campo: 0 falhas.
3. Cobertura: 196 ocorrências do CSV mais 4 EXTRA (200), cada uma em exatamente uma linha.
4. Nenhum DELETAR com `depois` não vazio; nenhum SUBSTITUIR vazio.
5. Aplicada a v2 sobre cópia: varredura do T108_inventario.py dá 0 PROCESSO e 0 VERIFICAR nos lotes 4 e 4-C; 33 FP-CONTEUDO antes e depois; FP-R1 = 0 (a tecla F4 é do 6a); só mudam curso, justificativa e pegadinhas[].texto/pares[].como; enunciado, gabarito e itemEdital intactos.
6. Texto resultante dos lotes 4 e 4-C: 0 casamentos de "(O11)", "fundamenta item", "neste chat", "não sutil", "entra(m) em item", "(CI,", "ITENS REAIS", "TC invertida", "indevida invertida", "Não usada em item".

Contagem da v2: SUBSTITUIR 167, DELETAR 15 (todos com `depois` vazio: 11 da v1, entre eles A0078, mais as 4 novas); lote 4 = 151, 4-C = 31.
