# RELATORIO_ORDEM_V15_C.md — T-108 (ORDEM_V15_C_LIMPEZA) — 2026-10-18 — gerado por orquestrador (sessão s14)

## O que mudou
- Pacote novo da Fábrica: **v1.11** (D-V111-NUMERACAO; aceito como canônico pela D-PACOTE-V111), sobre a v1.10, que já contém a v1.9. `saida/pacote/pacote.json` (SHA-256 1b5657c7…9517) e `pacote_estudante.json` v1.11-E (8533b0c0…6bd7); edição .md do estudante (35 arquivos) regenerada.
- Método M2, por decisão do Fundador (D-V15-C-M2): a limpeza vale no próprio `pacote.json`, que a plataforma e a prévia leem. As notas internas ("Difere do item X…", códigos e etiquetas de fonte, restrições de simulado) foram para o campo novo `interno`, presente em 210 objetos. O campo é reversível byte a byte à v1.10 e está no contrato v1.2.8.
- Enunciado, gabarito, itemEdital e ids dos 560 itens ficaram inalterados (salvo a ORDEM D). Também não mudaram simulados nem comandos.

## Contagens
- Inventário inicial (script da GBQ): 860 ocorrências no pacote.json v1.10 e 243 no -E. Com as marcas que o inventário não pegou (35 EXTRA/NAO_INVENTARIADA), o universo ficou em 907 ids.
- 799 edições: GCE 271 (tabela v3), GCB 525 e GBQ 3, além de 1 MANTER. Registro por id em `saida/pacote/registro_alteracoes_v1_11.csv`, com 800 linhas contando a T-109.
- Por regra: regra 2 (fonte por extenso) 471; regra 3 ("Difere…") 18; regra 4 (TC/IC/GI/AT → frase) 93; regra 5 / demais categorias 253.
- Por lote: L1 88, L1-C 7, L2 107, L3 56, L4 151, L4-C 31, L5 58, L5-C 21, L6a 182, L6b 82, discursivas 13, outros 3.
- Contagem final nos campos da ordem: **0 PROCESSO**. Sobra 1 VERIFICAR, que é o MANTER GBQ-0004.
- Falsos positivos que ficam:
  - 28 da regra 1 ("lote" técnico e a tecla F4);
  - 115 de conteúdo, que não são marca de produção.

## Parecer de QA
- QA opus independente, no máximo 2 rodadas:
  - GCE: gce-cqfp R1 com 260/263 aprovadas e 0 reprovada; R2 com 12/12.
  - GCB: gcb-cqfp R1 com 0% de reprovação nas três partes (37 CORRIGIR); R2 com 100% aprovado.
- Fidelidade do pacote (gbq-cqe): ACEITO COM RESSALVAS.
  - Reconstrução independente igual byte a byte.
  - Reversão à v1.10 igual byte a byte.
  - Leitura de 30 trechos editados, todos com o sentido mantido.
- Achado 1 (reprodutibilidade em clone limpo): corrigido com `.gitattributes`. A conferência em dois clones deu CONFERE (`saida/pacote/T108_conferencia_clone_v1_11_2026-10-18.md`).

## Pendente
- **Publicação na plataforma da candidata: só com o seu "sim"** (item RESERVADA D-PLATAFORMA-V111-FUNDADOR em PARA_FUNDADOR.md).
- Resíduos fora dos campos da ordem vão para a v1.12 ou para a ORDEM A (item AUDITORIA em PARA_FUNDADOR.md):
  - nomes de lote com código em `lotes[].nome`;
  - "(v0.2)" no nome do SIM-0;
  - a legenda TC/GI/AT/IC;
  - ids no `comandoOriginal`;
  - o aviso "NÃO VERIFICADO".
- Duas ressalvas de forma da GCE (GCE-0128 e GCE-0243) e o rótulo da conferência C-5 ficam para a v1.12.
