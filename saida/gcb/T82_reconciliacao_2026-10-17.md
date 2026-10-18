# T82_reconciliacao_2026-10-17.md — T-82 — 2026-10-17 — gerado por gcb-gerencia

Objeto: reconciliação da errata do Anexo N do Lote D6 (dúvida 1 de saida/gcb/T72_reconciliacao_2026-10-17.md). Ciclo 2026-10-17 s11c3. Entregas do qa-normativo-da: saida/gcb/D6_anexo_N_mapa_normativo.md (errata) e saida/gcb/T82_errata_anexo_N_2026-10-17.md. O D6 v1 não foi lido (D-CEGO-2).

## 1. Conferência própria (script, somente leitura, contra git HEAD)
- SHA-256 em disco do Anexo N: 57e8c64d4f27fe2c7549ff9f9b16c16848a51558e9aa181a0ed48c2f85d3e80e — confere com o informado.
- `git diff HEAD`: 3 blocos. (a) linha 1: cabeçalho acrescido de "(errata T-82, seção 8)"; (b) linha 413: LGPD art. 8º, § 5º — colunas texto e "redação dada por" iguais; vigência "— (revogado)" → "art. 65, II (24 meses após a publicação)"; observação "Revogado." → nota ERRATA T-82; (c) nova seção 8 (registro), acrescida ao fim (linhas 871–883).
- Corpo do Anexo (linhas 2–867, sem o cabeçalho): 1 linha removida e 1 acrescida — só a do art. 8º, § 5º. Nenhuma outra linha mudou.
- Contagens: linhas de dispositivo da tabela 715 antes e depois; linhas de tabela 815 antes e depois; seções 2 e 7 (701 conferidos, LAI 244, LGPD 457; 0 NÃO CONFERIDOS; 12 REVERIFICAR + 1 rubrica) fora do diff, portanto inalteradas. O aumento de ocorrências de "(revogado)" e "vetado" vem só do texto da seção 8 e da nota da linha corrigida.
- Relatório T82_errata (35 linhas): 715 linhas varridas (251 LAI, 464 LGPD), 1 corrigida, revogados confirmados LGPD art. 7º §§ 1º–2º, art. 55-A §§ 1º–3º, art. 55-B, art. 55-C, V; fontes planalto.gov.br verificadas em 17/10/2026 com URL — coerente com a seção 8 do Anexo.

## 2. D1 da GCB
- Errata ACEITA. Fundamento: correção restrita à linha apontada na dúvida 1, com fonte oficial datada (Fonte 2, l13709compilado.htm, verificado em 17/10/2026) e coerência interna (art. 15, III, e art. 18, IX, remetem ao § 5º como vigente); varredura do mesmo padrão nos dois sentidos sem outra divergência; contagens intactas. A dúvida 1 da T-72 fica respondida e fechada.
- T-82: pode ser registrada CONCLUÍDA pelo orquestrador (esta Gerência não altera TAREFAS.md).

## 3. Efeito sobre a v2 do D6
- A base normativa da v2 é o Anexo N na versão SHA-256 57e8c64d…; o despacho da v2 (após o parecer do Fundador) deve citá-la por esse hash e dizer que a LGPD art. 8º, § 5º, é vigente, redação original, art. 65, II.
- Na resposta item a item da v2, a gcb-cpp confere qualquer item, justificativa ou trecho de curso que trate do § 5º (revogação do consentimento) contra a linha corrigida; a gcb-cqfp verifica isso no R2. Isso não é juízo sobre a v1 (não lida; D-CEGO-2) e não altera a v1 nem a cópia entregue ao QA comparativo.
- Nenhuma outra mudança para a v2: seção 6 (NÃO CONFERIDO) e a lista REVERIFICAR ficam como estão.

## 4. Gatilhos
- Nenhum. A errata é de insumo interno (mapa normativo), não de canônico nem de item exportável; não há aceite de canônico (A), conflito ou matéria reservada. PARA_PRESIDENCIA.md não alterado.

## 5. T-73 (condição "abre após o lote anterior da ordem D6, D1, …")
- Juízo da GCB (D-FUNDADOR-AGORA-2): CUMPRIDA — o D6 completou tudo o que a fábrica pode fazer antes do parecer (v1 entregue ao QA comparativo, D-D6-QA-FUNDADOR, "nada a executar na fábrica até o retorno"; T-82, única pendência pré-v2, concluída), e o D1 (itens 1–2) não depende do D6 em conteúdo; se o parecer trouxer achados de processo, eles se aplicam ao D1 no R1/v2.
