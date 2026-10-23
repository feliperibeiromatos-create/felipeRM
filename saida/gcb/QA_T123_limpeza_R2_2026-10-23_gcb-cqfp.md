# QA_T123_limpeza_R2_2026-10-23_gcb-cqfp.md — T-123, QA R2 (última rodada) da limpeza das marcas de produção no reforço de DA — 2026-10-23 — gerado por gcb-cqfp

Objeto:
- `saida/gcb/T123_substituicoes_DA_v2.csv`: 91 linhas, UTF-8 sem BOM, LF. SHA-256 LF `de63b7c524797723c46690b45082d243583895846fdc144c11da8e2bfe233bde`.
- `saida/gcb/T123_producao_notas_DA.md`: seção "Rodada 2" e tabela de fontes.

Referência: `QA_T123_limpeza_R1_2026-10-23_gcb-cqfp.md`. Texto-base `reforco_bruto.json`, só leitura. Scripts próprios rodados com python -I no scratchpad `cqfp_t123/`: `qa_v2.py` e o diff de bytes.

## Veredito: CONFERIDO

91/91 APROVADO, 0 reprovadas. A tabela v2 pode ir à reconciliação da GCB com o SHA-256 acima.

## 1. Diff v1 × v2 (bytes)

| conferência | resultado |
|---|---|
| Tamanho | 93 linhas físicas em cada arquivo, sem CR |
| Linhas que diferem | Só as linhas 29 e 33 do arquivo, isto é, GCB-T123-0028 e GCB-T123-0032 |
| Cabeçalho e outras 89 linhas | Byte a byte iguais à v1. **PASSA.** |

## 2. Mecânica completa com a v2

| critério | resultado |
|---|---|
| (a) Cobertura | 103 MARCA cobertas uma vez cada. Nenhum VERIFICAR/FP coberto. Única EXTRA: GCB-EXTRA-01. **PASSA.** |
| (b) `antes` | Literal, 1 ocorrência no item, contém o `antes_unico` (R60 / R62 nas duas linhas novas), sem sobreposição. **PASSA.** |
| (c) Ação e operação | DELETAR só com `depois` vazio. Op. 6 com `fonte_origem`. 0028 e 0032 seguem SUBSTITUIR, op. 6. **PASSA.** |
| (d) Resíduo de marca | C-MARCAS: 108 → 0 nos 238 itens. "Pertinência parcial": 0. "Desconto em folha" do D3-R75 intacto. PROCESSO: só os 2 "Presidência da República" (D2-R21, D2-R24), que são conteúdo VERIFICAR e estão iguais antes e depois. **PASSA.** |
| (e) Intocáveis | Enunciado, gabarito, `itemEdital`, aderência, `j1` e `j2` idênticos nos 238. Os 153 itens sem MARCA estão byte a byte iguais. 85 itens editados, todos com MARCA. **PASSA.** |
| (f) VERIFICAR e FP | Os 4 VERIFICAR e os 2 FP estão intactos, inclusive "produção" no D4-R24. **PASSA.** |

## 3. As 2 linhas corrigidas

Nas duas linhas, `antes` e `depois` são o texto exato pedido na R1, e a `nota` é "alargado (sem repetir)". As frases resultantes foram lidas no contexto.

| linha | frase resultante | veredito |
|---|---|---|
| GCB-T123-0028 (D4-R20) | "O Referencial Básico de Governança Organizacional (TCU, 2020) lista, entre as diretrizes para a boa governança, a de apoiar e viabilizar a inovação…" | APROVADO |
| GCB-T123-0032 (D4-R24) | "O Referencial Básico de Governança Organizacional (TCU, 2020) registra a classificação das atividades da organização…" | APROVADO |

Nas duas linhas:
- sem repetição;
- sem palavra nova;
- sentido e fonte preservados (Base R60, p. 48-49; Base R62, p. 82).

## 4. Notas

A tabela de fontes ficou assim:
- **G6:** a linha diz agora que a l. 543 é a Base do D4-R52, e que o G6 está identificado no adendo de 22/10, seção 5, l. 175. Confere.
- **R39 e R46:** as linhas trazem agora as Bases do D4-R05 (l. 185) e do D4-R11 (l. 279). Confere.
- A seção "Rodada 2" relata o diff e a mecânica, e eles conferem com esta R2.

Ressalva de forma, sem efeito no veredito:
- o cabeçalho das notas (l. 3) ainda cita o SHA-256 da v1;
- a lista da seção (c) não traz as 2 linhas novas como alargadas (52 de 91, e não 50).

A própria "Rodada 2" registra os dois pontos. A reconciliação usa o SHA-256 da v2.

## 5. Pendência que continua (não é desta tabela)

P1 (GBQ): registrar "Presidência da República" (D2-R21, D2-R24) como exceção de conteúdo do PROCESSO antes de rodar o `conferir_t123.py`. Sem esse registro, o critério "0 PROCESSO" vai dar 2.
