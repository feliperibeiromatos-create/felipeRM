# T108_reconciliacao_GCB_2026-10-18.md — T-108 (ORDEM_V15_C, limpeza), reconciliação e consolidação da GCB — lotes 4, 4-C, 5, 5-C, 6a, 6b — 2026-10-18 — gerado por gcb-gerencia

Base: D1 de método `saida/gcb/T108_D1_GCB_2026-10-18.md`; D1 pós-R1 `saida/gcb/T108_D1_pos_R1_GCB_2026-10-18.md` (seção 7); pareceres R2 `saida/gcb/QA_T108_R2_parte{A,B,C}_2026-10-18_gcb-cqfp.md` (APROVADO nas três partes, 0 reprovado, 0,0%); especificação da GBQ `saida/pacote/T108_D1_pacote_M2_2026-10-18.md` (condição E2 e seção 1.3). Texto-base: `saida/pacote/pacote.json` v1.10, SHA-256 LF d43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed. A GCB não escreve em DECISOES.md nem nos estados de TAREFAS.md, não edita pacote nem arquivos de lote e não faz commit.

## 1. Veredito

**CONSOLIDADO. A tabela de substituição da GCB está pronta para o gatilho A.** As três partes v2 saíram APROVADAS na R2 (última rodada; D-V15-ENCOMENDA, no máximo 2 rodadas). A junção por script passa em todas as 44 checagens. Não há linha que volte à produção. Seguem a errata de forma P-1 e a decisão P-2 (seção 4).

## 2. Consolidação (item 1)

Arquivo: `saida/gcb/T108_substituicoes_GCB.csv`. É o nome-alvo da condição E2 da especificação da GBQ.
Script: `saida/gcb/T108_juntar_GCB.py`. Roda da raiz com `python -I -X utf8`, lê o pacote e o inventário só para leitura e grava só o consolidado. Resultado: TUDO OK, rc 0.

| Objeto | Linhas | SHA-256 dos bytes em disco |
|---|---|---|
| `T108_substituicoes_GCB_parteA_v2.csv` | 182 (GCB-A0001 a A0182) | 05b45e7106c5df6b3e317db3b37abfcab049a9e93abf18789f5e73399e85753b |
| `T108_substituicoes_GCB_parteB_v2.csv` | 182 (GCB-B0001 a B0182) | d39615c7053489babcec8655aa9862e48c7ec43521aeafecbd5e58b73f7e9881 |
| `T108_substituicoes_GCB_parteC_v2.csv` | 161 (GCB-C0001 a C0161) | 1973b966120145775a30b78d59da4d98735862a9b9c6154cb0bb50e9dcbfb137 |
| **`T108_substituicoes_GCB.csv`** | **525 + cabeçalho** (150.505 bytes) | **10d9e5588753bc9ad273a529b56148b20e1f643bb4f312751a8fbd371b8751ef** |

Forma: UTF-8 sem BOM e RFC 4180, com vírgula, CRLF entre registros, aspas mínimas e `\n` dentro dos campos. Há 13 colunas, na ordem da Parte A, e as partes vão em sequência A, B, C. A Parte A vinha com aspas em todos os campos e as partes B e C com aspas mínimas. A reserialização uniforme não muda nenhum valor: a releitura do consolidado dá exatamente o cabeçalho e as 525 linhas das partes, na ordem.

Checagens (as da seção 1.3 e 1.4 da especificação da GBQ que a GCB consegue rodar antes do gerador):
- Cabeçalho único e igual nas três partes. Nenhuma parte tem BOM. Todas as linhas têm 13 colunas.
- Os ids são únicos e cada parte usa só o próprio prefixo (GCB-A, GCB-B, GCB-C). A contagem é 182 + 182 + 161 = 525, igual à soma das partes.
- Nenhum `\r` em `antes` ou `depois`. `acao` é DELETAR ou SUBSTITUIR (não há MANTER). `regra` está entre 1 e 5. Todo DELETAR tem `depois` vazio e todo SUBSTITUIR tem `depois` não vazio e diferente de `antes`.
- Todos os caminhos resolvem a uma string. Cada `antes` é literal e aparece uma só vez no campo da v1.10. Nenhuma edição se sobrepõe a outra.
- Cobertura: as 575 ocorrências PROCESSO + VERIFICAR da GCB no `T108_ocorrencias.csv` e as 22 GCB-EXTRA aparecem uma vez cada, 597 no total. Não falta nenhuma, nenhuma sobra, e o caminho de cada id é o caminho da sua linha. Nenhum FP é citado em linha.
- Proibições do `depois` (1.4, item 7): 0 casamentos, então a lista de exceções da GCB fica **vazia**. "Verificado em" e base legal (1.4, item 8) não se perdem em nenhuma linha. Os 108 FP-R1 e FP-CONTEUDO da GCB, localizados por posição, ficam fora de todo `antes` ou intactos dentro dele (1.4, item 5).
- Com a tabela aplicada numa cópia em memória, a nova varredura do `T108_inventario.py` dá 0 PROCESSO e 0 VERIFICAR. Os FP-CONTEUDO ficam iguais (4 = 33, 6a = 35, 6b = 39). "A tecla F4" continua 1 → 1, casada por texto. Só mudam justificativa, curso, resumo, pegadinhas e pares (99 campos), e enunciado, gabarito e itemEdital ficam intactos.
- Resíduo zero de "(O11)", "fundamenta item", "neste chat", "não sutil", "entra(m) em item", "(CI,", "ITENS REAIS", "TC invertida", "indevida invertida", "Não usada em item" e "invertida (". "hoje" minúsculo: 0. ", às avessas": 10.

## 3. Contagens finais

Total da tabela: **525 linhas** (SUBSTITUIR 490, DELETAR 35; regra 2 = 341, 3 = 18, 4 = 87, 5 = 79; modo LIVRE 315, TEMPLATE 210).

### 3.1 Por lote

| Lote | Parte | Linhas | DELETAR | Ocorrências do CSV | EXTRA | Total coberto | PROCESSO + VERIFICAR depois | FP que ficam |
|---|---|---|---|---|---|---|---|---|
| 4 | A | 151 | 6 | 163 | 3 (01–03) | 166 | 0 | 33 FP-CONTEUDO |
| 4-C | A | 31 | 9 | 33 | 1 (04) | 34 | 0 | 0 |
| 5 | C | 58 | 1 | 71 | 1 (12) | 72 | 0 | 0 |
| 5-C | C | 21 | 11 | 27 | 0 | 27 | 0 | 0 |
| 6a | B | 182 | 5 | 199 | 7 (05–11) | 206 | 0 | 35 FP-CONTEUDO + 1 FP-R1 |
| 6b | C | 82 | 3 | 82 | 10 (13–22) | 92 | 0 | 39 FP-CONTEUDO |
| **Total** | | **525** | **35** | **575** | **22** | **597** | **0** | **108** |

### 3.2 Por categoria (meta: zero, salvo os FP da regra 1)

| Categoria | Ocorrências do CSV | EXTRA | Total | Depois da aplicação | FP que ficam (regra 1) |
|---|---|---|---|---|---|
| C01 | 22 | 0 | 22 | 0 | 0 |
| C02 | 21 | 1 | 22 | 0 | 0 |
| C03 | 5 | 0 | 5 | 0 | 106 FP-CONTEUDO (4 = 32, 6a = 35, 6b = 39) |
| C05 | 375 | 1 | 376 | 0 | 1 FP-R1 (6a, "A tecla F4") |
| C06 | 85 | 3 | 88 | 0 | 0 |
| C07 | 20 | 0 | 20 | 0 | 0 |
| C08 | 6 | 3 | 9 | 0 | 1 FP-CONTEUDO (lote 4) |
| C10 | 41 | 14 | 55 | 0 | 0 |
| **Total** | **575** | **22** | **597** | **0** | **108** |

Meta cumprida: zero PROCESSO e zero VERIFICAR em todas as categorias. Ficam só os 108 falsos positivos da regra 1, que são conteúdo.

Na coluna `categoria` das linhas: C05 338, C06 86, C10 36, C01 16, C07 16, C02 11, C08 5, C03 3, mais 14 linhas com categoria composta, isto é, uma edição que cobre ocorrências de mais de uma categoria.

### 3.3 As 22 GCB-EXTRA (fora do `T108_ocorrencias.csv`)

| id | Lote | Linha | Marca retirada | Categoria / regra |
|---|---|---|---|---|
| GCB-EXTRA-01 | 4 | GCB-A0179 | " (O11)" | C02 / 5 |
| GCB-EXTRA-02 | 4 | GCB-A0180 | " Não fundamenta item." | C10 / 5 |
| GCB-EXTRA-03 | 4 | GCB-A0181 | " neste chat" | C08 / 5 |
| GCB-EXTRA-04 | 4-C | GCB-A0182 | "; não sutil" (4C-10) | C06 / 4 |
| GCB-EXTRA-05 | 6a | GCB-B0176 | "; nada sobre isso entra em item" (1.1.2) | C10 / 5 |
| GCB-EXTRA-06 | 6a | GCB-B0177 | idem (1.1.3) | C10 / 5 |
| GCB-EXTRA-07 | 6a | GCB-B0178 | "; esses pontos não entram em item além da descrição acima" | C10 / 5 |
| GCB-EXTRA-08 | 6a | GCB-B0179 | "; não sutil" (6A-08) | C06 / 4 |
| GCB-EXTRA-09 | 6a | GCB-B0180 | "; não sutil" (6A-11) | C06 / 4 |
| GCB-EXTRA-10 | 6a | GCB-B0181 | "abertas hoje" → "consultadas em 08/10/2026" (caso b) | C10 / 5 |
| GCB-EXTRA-11 | 6a | GCB-B0182 | "sem fonte aberta hoje" → "sem fonte consultada" (caso c) | C10 / 5 |
| GCB-EXTRA-12 | 5 | GCB-C0006 (absorvida) | "CI" e "verificado pela CQFP" | C05 / 2 |
| GCB-EXTRA-13 | 6b | GCB-C0156 | "hoje" no título 4.0.2 (caso c) | C10 / 5 |
| GCB-EXTRA-14 | 6b | GCB-C0157 | "A leitura de hoje" (caso b) | C10 / 5 |
| GCB-EXTRA-15 | 6b | GCB-C0158 | "Fontes abertas hoje:" (caso b) | C10 / 5 |
| GCB-EXTRA-16 | 6b | GCB-C0103 (absorvida) | "sem fonte aberta hoje" (caso c) | C10 / 5 |
| GCB-EXTRA-17 | 6b | GCB-C0105 (absorvida) | "aberta hoje" (caso a) | C10 / 5 |
| GCB-EXTRA-18 | 6b | GCB-C0108 (absorvida) | idem (caso a) | C10 / 5 |
| GCB-EXTRA-19 | 6b | GCB-C0116 (absorvida) | idem (caso a) | C10 / 5 |
| GCB-EXTRA-20 | 6b | GCB-C0159 | "hoje" em 6B-06 (caso c) | C10 / 5 |
| GCB-EXTRA-21 | 6b | GCB-C0160 | " (seção ITENS REAIS acima)" | C08 / 5 |
| GCB-EXTRA-22 | 6b | GCB-C0161 | " (seção ITENS REAIS)" (6B-06) | C08 / 5 |

## 4. Pendências da R2 da Parte C (item 2)

- **P-1, errata de forma da GCB, aplicada.** Em `saida/gcb/T108_fontes_GCB.md`, o resumo da linha 99 dizia "Lote 5 = 8 (U1-U6, TB2, GG4)", mas a tabela do Lote 5 tem 9 códigos desde que a linha CI foi acrescentada (aprovada na R2 C, seção 3). O resumo passa a "Lote 5 = 9 (U1-U6, TB2, GG4, CI …)", com a nota de que CI é código fora do padrão U/GG/TB do inventário, acrescentado na T-108 pela GCB-C0006. Só essa linha mudou. Não entra fonte nova, a tabela não muda e nenhuma linha do CSV muda. Como é forma, não volta à QA.
- **P-2, decisão da GCB: é conteúdo e fica.** "Hoje, muitos produtos de segurança incorporam antivírus, antispyware e firewall num pacote" (`lotes[L6B].curso`, 4.2.3) descreve o estado atual do mercado para a candidata. Não fala do momento da produção nem afirma uma consulta. A regra da seção 4 do D1 pós-R1 não se aplica. A frase não está entre as EXTRA e não entra na T-108, de acordo com o entendimento da QA. Nenhum complemento ou ajuste de conteúdo se abre por isso (D-COMPLEMENTOS).

## 5. Notas de produção (item 3), por remissão

A GCB não reescreve as notas. O registro de produção da T-108 da GCB fica formado por estes cinco arquivos:
- v1: `saida/gcb/T108_producao_notas_GCB_parteA.md` (Parte A) e `saida/gcb/T108_producao_notas_GCB_parteB.md` (Parte B). A Parte C v1 não teve arquivo de notas: os pontos da produtora foram julgados no parecer R1 C, seção 4.
- v2: `saida/gcb/T108_producao_notas_GCB_v2.md` (Parte A), `saida/gcb/T108_producao_notas_GCB_v2_parteB.md` e `saida/gcb/T108_producao_notas_GCB_v2_parteC.md`.
- Autoconferências da produção: `saida/gcb/T108_conferir_parteA.py`, `T108_conferir_parteA_v2.py` e `T108_conferir_parteB.py`. Junção e conferência da GCB: `saida/gcb/T108_juntar_GCB.py`.
As contagens das notas conferem com o consolidado: A 178 + 4 = 182, B 175 + 7 = 182, C 155 + 6 = 161.

## 6. Registros pedidos pela D1 pós-R1 (seção 1)

- **R-1 (Parte C):** o trecho da errata T-83 (D-TRANSPORTE-L5C-T83) no 5C-08, "É, entre os itens 5C, o mais próximo do item A5-20: …", foi absorvido na v1.10 (D-ABSORCAO-V110) e é retirado pela T-108 na linha GCB-C0075 (DELETAR, regra 3 por analogia). A fidelidade da gbq-cqe no pacote novo não deve ler isso como absorção perdida. O canônico `GCB_Lote5C_v1` não muda.
- **Convenção `regra` = 5:** nas três partes, `regra` 5 marca a retirada de nota de QA, de produção ou de instrução interna (79 linhas). Nenhuma dessas linhas altera enunciado, gabarito ou itemEdital, o que a re-varredura confirmou.
- Ressalvas sem correção: A0007 e A0016 (editor repetido), B0027 e a forma "Conforme Microsoft, documentação de suporte, …" ficam como foram aprovadas.

## 7. Para a GBQ

1. Os ids GCB-EXTRA-01 a 22 não estão no `saida/pacote/T108_ocorrencias.csv`. Para a GCB, o universo de cobertura é 575 + 22 = 597. O item 4 da seção 1.3 da especificação ("nenhuma linha cita id fora dele") precisa aceitar esses 22 ids na tabela da GCB, ou a GBQ abre errata do inventário mapeando cada EXTRA a um id novo e avisa a GCB. O texto das tabelas não muda em nenhum dos dois casos.
2. A FP-R1 D-C05-4a878e59 (6a, a tecla F4 do Excel) é casada **por texto**, "A tecla F4", e não por id. Depois da aplicação, a nova varredura dá a ela outro hash. As linhas B0035 e B0039 têm outros "F4", que são códigos de fonte, no mesmo campo e fora da posição da FP.
3. A lista de exceções da GCB às proibições do `depois` (1.4, item 7) é vazia.
4. A tabela usa CRLF entre registros e aspas mínimas. O SHA-256 acima vale para os bytes em disco, como manda a seção 1.3, item 1.
5. Lacunas do `T108_inventario.py` (D1 pós-R1, seção 2, item 3) ficam como registro, sem efeito na GCB.

## 8. Encaminhamento

Gatilho A da GCB em `PARA_PRESIDENCIA.md`: aceite de `saida/gcb/T108_substituicoes_GCB.csv` (SHA-256 10d9e558…51ef) para a consolidação no pacote novo pela GBQ (condição E2). Nada vai à plataforma da candidata sem o sim do Fundador (D-V15-PLATAFORMA).
