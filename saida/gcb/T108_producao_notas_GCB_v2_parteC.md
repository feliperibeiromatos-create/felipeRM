# T108_producao_notas_GCB_v2_parteC.md — T-108, GCB, v2 da Parte C (lotes 5, 5-C, 6b) — 2026-10-18 — gerado por gcb-cpp

Arquivos: `saida/gcb/T108_substituicoes_GCB_parteC_v2.csv` (155 da v1 + 6 novas = 161 linhas) e uma linha nova em `saida/gcb/T108_fontes_GCB.md` (Lote 5, CI). Base: `saida/pacote/pacote.json` v1.10, SHA-256 LF d43c32de... (conferido). A v1, o pacote, os lotes, DECISOES, TAREFAS e PARA_PRESIDENCIA não foram tocados; sem commit.

## 1. Resposta ao QA R1 (parecer da Parte C), item a item

| Item do QA | Resposta |
|---|---|
| A-1, GCB-C0006 (código CI) | ACEITO. `antes` = `(CI, verificado pela CQFP em 8/10/2026)`; `depois` = `(Google Cloud, Data Studio, "Conversational Analytics — Code Interpreter", verificado em 8/10/2026)`; regra 2; `fonte_origem` = `T108_fontes_GCB.md, lote 5, CI`. Texto exato do parecer. Por D1 (seção 1), `ids_ocorrencia` passa a `D-C07-9077e927;GCB-EXTRA-12`. Ajustei também `categoria` (C07;C05), `trecho` e `nota` para refletir o código CI. Linha nova na tabela de fontes do Lote 5, logo após GG4, com o texto exato do A-1. |
| A-2, GCB-C0097 (escopo do tópico) | ACEITO. `depois` = "Não foi aberta fonte institucional que defina o termo, e o edital não o detalha; por isso, este material não traz item sobre governança digital (tópico 4 de TI e Dados)." |
| A-3, GCB-C0002, C0004, C0005 (`regra`) | ACEITO. `regra` 4 → 5. Texto igual à v1. |
| R-1 (trecho da errata T-83 absorvido na v1.10 e retirado pela T-108) | Não é correção de linha; vai à reconciliação (D1, seção 1). Nada a fazer na v2. |
| R-2 (forma única de "invertida") | Resolvido pelo D1, seção 3: ", às avessas". As quatro linhas da Parte C (C0059, C0128, C0151, C0154) ficam como estão. |
| R-3 ("hoje" e "seção ITENS REAIS") | Entra na T-108 pelo D1 (seções 2 e 4); ver seção 2. |
| Ponto 1 (nomes abreviados), 2 (C0075), 3 (C0034, C0036, C0037, C0094, C0104, C0081), 4 (C0097, retirada da especificação), 5 | APROVADOS pelo QA; linhas iguais à v1. |

## 2. Linhas corrigidas (9) e novas (6)

Corrigidas, e só nos campos citados: C0002, C0004, C0005 (`regra`); C0006 (ver acima); C0097 (`depois`); C0103, C0105, C0108, C0116 (seção 4 do D1).
- C0103 (EXTRA-16, caso c): `depois` "sem fonte consultada."; sem data.
- C0105, C0108, C0116 (EXTRA-17, 18, 19, caso a): `depois` perde "aberta hoje " e fica "(CERT.br, ...". A frase já traz "verificado em 08/10/2026". Resultado: "Definição de vírus (CERT.br, ...", "Definição de ransomware (CERT.br, ...", "Definição (CERT.br, ...".
- `nota` de C0103, C0105, C0108 e C0116 acrescenta a menção ao EXTRA.

Novas (todas lote 6b, regra 5, modo LIVRE; `antes` literal e único):

| id_edicao | ids_ocorrencia | caminho | antes | depois | ação |
|---|---|---|---|---|---|
| GCB-C0156 | GCB-EXTRA-13 | lotes[L6B].curso | `sem base aberta hoje)` | `sem base consultada)` | SUBSTITUIR (caso c) |
| GCB-C0157 | GCB-EXTRA-14 | lotes[L6B].curso | `A leitura de hoje ` | `A leitura de 08/10/2026 ` | SUBSTITUIR (caso b) |
| GCB-C0158 | GCB-EXTRA-15 | lotes[L6B].curso | `Fontes abertas hoje:` | `Fontes consultadas em 08/10/2026:` | SUBSTITUIR (caso b) |
| GCB-C0159 | GCB-EXTRA-20 | itens[6B-06].justificativa | `em fonte aberta hoje` | `em fonte consultada` | SUBSTITUIR (caso c) |
| GCB-C0160 | GCB-EXTRA-21 | lotes[L6B].curso | ` (seção ITENS REAIS acima)` | (vazio) | DELETAR |
| GCB-C0161 | GCB-EXTRA-22 | itens[6B-06].justificativa | ` (seção ITENS REAIS)` | (vazio) | DELETAR |

Absorções: nenhuma linha nova se sobrepõe a outra. Observação: C0157 (EXTRA-14) fica adjacente a C0098, que troca "do F4 (Cartilha, livro) menciona" por "de CERT.br, ..."; o `antes` de C0157 termina no espaço antes de "do", sem sobreposição, e o resultado lê "A leitura de 08/10/2026 de CERT.br, ...". O `antes` de C0157 e o de C0158 têm espaço final / dois-pontos finais por conta da adjacência com linhas existentes (C0098 e C0100). Os EXTRA-12 a 22 de Parte C ficam assim: 12 em C0006; 13, 14, 15, 20, 21, 22 em C0156 a C0161; 16, 17, 18, 19 em C0103, C0105, C0108, C0116.

## 3. Autoconferência (python -I, somente leitura; scripts no scratchpad)

1. Diff v1 × v2: só mudam C0002, C0004, C0005, C0006, C0097, C0103, C0105, C0108, C0116 (9); 146 linhas byte a byte iguais; 6 novas ao fim. A releitura/gravação do CSV da v1 reproduz os bytes da v1.
2. `antes` literal e único no campo da v1.10 nas 161 linhas; 0 sobreposição entre linhas.
3. Cobertura: todos os ids de ocorrência da v1 mantidos, uma vez cada; EXTRA-12 a 22 da Parte C presentes, uma vez cada; nenhum id a mais.
4. Nenhum DELETAR com `depois` não vazio; nenhum SUBSTITUIR com `depois` vazio.
5. Aplicada a v2 numa cópia em memória do pacote, varredura do `T108_inventario.py` nos lotes 5, 5-C e 6b: antes 68 P + 3 V (5), 24 P + 3 V (5-C), 78 P + 4 V (6b); depois 0 PROCESSO e 0 VERIFICAR; FP-CONTEUDO do 6b 39 = 39.
6. No texto resultante dos campos tocados, 0 casamentos de "(O11)", "fundamenta item", "neste chat", "não sutil", "entra em item", "entram em item", "(CI,", "hoje", "ITENS REAIS", "TC/GI/IC/AT invertida" e "indevida invertida"; 0 do código CI e 0 de "hoje"/"ITENS REAIS" no curso inteiro dos lotes 5 e 6b. (A checagem de "A tecla F4" é da Parte B e não se aplica aqui.)
7. Fontes: a linha CI foi acrescentada à tabela do Lote 5; o resumo do arquivo diz "Lote 5 = 8 (U1-U6, TB2, GG4)" e não foi alterado (a instrução do D1 limita a mudança à linha; a contagem fica a cargo da reconciliação, porque CI é código fora do padrão do inventário).
