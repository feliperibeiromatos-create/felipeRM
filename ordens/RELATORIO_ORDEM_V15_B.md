# RELATORIO_ORDEM_V15_B.md — T-110 (ORDEM_V15_B_PARES) — 2026-10-19 — gerado por orquestrador (sessão s14)

## O que mudou
- Pacote novo da Fábrica: **v1.12** (D-PACOTE-V112), sobre a v1.11.
- Os pares confundíveis que trazem conteúdo útil voltaram como pegadinhas do tópico, no formato "Não confunda A com B: …", cada uma com `itemEdital`. Elas ficam em `lotes[].pegadinhas`, que é o único lugar que a prévia v15.2 lê.
- O campo `lotes[].pares` ficou inalterado, porque a plataforma publicada (v1.9) ainda o lê.
- Sem fato novo e sem referências de produção. A origem de cada pegadinha (o par de que ela veio) está no registro de alterações da v1.12.

## Contagens
- P2 (GCE): 67 pares, dos quais 24 convertidos e 43 descartados. Motivos dos descartes: 41 duplicavam pegadinha já existente no tópico, 1 não era par e 1 exigiria fato fora do curso.
- P1 (GCB): 72 pares, dos quais 46 convertidos (em 49 pegadinhas) e 26 descartados. Motivos: 22 duplicavam pegadinha existente e 4 exigiriam fato fora do curso.
- Total: 73 pegadinhas novas; o pacote passa a ter 335 pegadinhas.

## Parecer de QA
- gce-cqfp:
  - R1: 61 aprovados, 4 a corrigir e 2 reprovados, que eram descartes indevidos e passaram a conversões.
  - R2: aprovado, com 0% de reprovação.
- gcb-cqfp:
  - R1: 67 aprovados, 3 a corrigir e 2 reprovados (duplicatas).
  - R2: aprovado, com 0%.
  - O Decreto 1.171 foi conferido no planalto.gov.br.
- Fidelidade do pacote pela gbq-cqe: as 73 pegadinhas estão iguais às entregas aprovadas e no lote certo.

## Pendente
- Publicação na plataforma: só com o seu "sim" (RESERVADA, D-PLATAFORMA-V112-FUNDADOR).
- Retirar `lotes[].pares` do pacote é decisão de plataforma.
