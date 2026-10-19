# RELATORIO_ORDEM_V15_E.md — T-112 (ORDEM_V15_E_PILOTO_VISUAL) — 2026-10-19 — gerado por orquestrador (sessão s14)

## O que mudou
- O pacote **v1.12** (D-PACOTE-V112) traz, em `pacote.topicos`, o piloto visual dos 3 tópicos sugeridos, sem troca: **P2-1.4** (diarização), **P2-2.5** (normalização de texto) e **P1-8.2** (tipos de gráficos).
- Cada tópico tem `emUmMinuto` com 3 pontos, `resumo` (da ORDEM A) e `visuais` com os campos exatos da ordem:
  - P2-1.4: fluxo das 5 etapas, tabela diarização × identificação × verificação e esquema das limitações;
  - P2-2.5: tabela categoria × decisão × exemplo e esquema normalização × ITN (normalização inversa);
  - P1-8.2: tabela "qual gráfico para qual pergunta" e esquema "como ler um box plot".
- **Nenhum "barras":** nenhum dos três cursos traz série numérica oficial com data, e a ordem exige fonte oficial e data em todo dado de barras.
- Também não há "linha" (falta cronologia no curso) nem "fluxo" no P1-8.2. Nada fora do curso e sem referências de produção.

## Parecer de QA
- P2, gce-cqfp: na R1, 7 de 11 elementos aprovados e 4 a corrigir (uma célula, um ponto do emUmMinuto, a tabela e o esquema do 2.5). Na R2, 11 de 11 aprovados.
- P1, gcb-cqfp: na R1, 3 de 5 aprovados e 2 pontos do emUmMinuto a corrigir. Na R2, aprovado.
- Fidelidade do pacote: os 3 pilotos estão iguais às entregas aprovadas, nos campos do contrato v1.2.9.

## Pendente
- **Peças com desenho (CDJ → CII):** nenhuma foi necessária, porque os componentes da prévia v15.2 renderizam os 3 tópicos.
- Publicação na plataforma: só com o seu "sim".
