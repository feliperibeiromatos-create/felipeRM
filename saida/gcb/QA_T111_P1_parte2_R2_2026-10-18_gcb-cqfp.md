# QA_T111_P1_parte2_R2_2026-10-18_gcb-cqfp.md — T-111 (A2), QA R2 (última rodada) dos 8 tópicos corrigidos — 2026-10-18 — gerado por gcb-cqfp

Objeto: saida/gcb/T111_resumos_P1_parte2_v2.md (gcb-cpp), comparado com o v1 e com a seção 4 de saida/gcb/QA_T111_P1_parte2_R1_2026-10-18_gcb-cqfp.md.
Método: script próprio (`python -I`). O script aplicou ao json do v1 as correções da R1, palavra por palavra, e comparou o resultado, por string exata, com o json do v2. Depois refez as contagens e repetiu a varredura da regra 0.7. Somente leitura; nenhum arquivo foi alterado além deste.

## 1. Veredito

Parte A2: **APROVADA.** Os 8 tópicos corrigidos estão APROVADOS e nenhum foi reprovado (0%). Os 8 tópicos já aprovados na R1 estão iguais ao v1, byte a byte. Os 16 resumos podem ir para a reconciliação.

| Tópico | Correção conferida | Parágrafos (palavras) | Palavras | % do curso | Parecer |
|---|---|---|--:|--:|---|
| P1-2 | §3 dividido | 6 (33, 36, 24, 18, 39, 31) | 181 | 19,1% | APROVADO |
| P1-2.1 | §5 dividido | 6 (37, 46, 22, 51, 22, 31) | 209 | 21,3% | APROVADO |
| P1-3 | Cco/Para-Cc separados por ponto; §6 dividido | 7 (28, 28, 35, 40, 26, 37, 19) | 213 (≤300) | 10,7% | APROVADO |
| P1-4 | §3 dividido; "como conceito geral" removido; "Em sentido amplo" | 4 (46, 29, 13, 21) | 109 | 39,1% | APROVADO |
| P1-4.1 | "histórico de versões e retenção" | 5 (35, 60, 45, 44, 24) | 208 | 11,2% | APROVADO |
| P1-5.3 | §5 dividido | 6 (36, 51, 43, 49, 18, 21) | 218 | 20,3% | APROVADO |
| P1-6 | texto integral da R1, com artigos | 6 (25, 41, 39, 50, 37, 26) | 218 | 10,1% | APROVADO (normativo sai de PENDENTE: toda citação tem artigo, tirado do curso) |
| P1-8.3 | §5 com "Segundo o Google Cloud, verificado em 8/10/2026"; "distinta do Data Studio" | 5 (35, 50, 35, 37, 43) | 200 | 18,3% | APROVADO |

## 2. Divergência de contagem apontada pela produtora (P1-6: 218 × 219)

A produtora está certa: são **218 palavras** e o §6 tem 26 palavras.

Origem do erro: na R1, a contagem de 219 (e 27 palavras no §6) foi feita antes da última troca de redação, de "O Código de Ética veda" para "O mesmo decreto veda". Essa troca tira uma palavra. O texto exato da R1 é o que vale e é o que está no v2.

Fica corrigida aqui a contagem que a seção 4 da R1 registrou para P1-6. O resultado continua dentro de 220 palavras e de 60 por parágrafo.

## 3. Varredura (regra 0.7) e json

Varredura no v2, só com as exceções já admitidas na R1:
- "F4" (P1-1);
- "versão" (P1-1) e "versões" (P1-4.1);
- "instrução/instruções" (P1-5.1);
- "Difere do dashboard" (P1-8.4);
- falsos positivos: "conversas" e "diverso".

"conceito geral" não aparece mais. Fora disso, zero ocorrências. Nenhuma linha começa com número, marca de lista ou rótulo em maiúsculas com dois-pontos.

json:
- um só bloco, com as 16 chaves na ordem do edital (P1-1 … P1-8.4);
- só o campo `resumo` em cada chave;
- quebras de parágrafo `\n\n`, sem quebra simples;
- os 16 tópicos dentro da regra de tamanho (P1-1 e P1-3 pela exceção).

## 4. Encaminhamento

A gcb-gerencia reconcilia a A2 com os 16 resumos do v2 (saida/gcb/T111_resumos_P1_parte2_v2.md). Não há R3 nem pendência de QA nesta parte.
