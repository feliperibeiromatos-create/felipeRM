# D5_despacho_GCB-CPP.md — T-74 — 2026-10-18 — gerado por gcb-gerencia
# DESPACHO 13 — LOTE D5 (Licitações e contratos, Lei 14.133/2021; P1-DA, item 10) — v1 — AGORA (18/10/2026)
Origem: D-ESCOPO-3 (Fundador, 15/10/2026), D-DA-LOTES (ordem D6, D1, D5, D2, D3, D4), D-DA-BANCO, D-DA-INSUMOS e D-FUNDADOR-AGORA-3. Despacho-base: lotes/loteD5/DESPACHO.md. Condição de abertura ("abre após o lote anterior da ordem") cumprida: o D1 foi aceito canônico (D-LOTED1-CANONICO). Tarefa: T-74. Módulo na plataforma: "m-da". Sem discursiva.
Executor: agente gcb-cpp. QA normativo prévio: agente qa-normativo-da. QA de mérito: gcb-cqfp (R1 e R2). Titular e reconciliação: gcb-gerencia.

## 1. O que produzir
O Lote D5 v1, conforme "saida/gcb/D5_ficha_lote.md" e os anexos da seção 10 da ficha. Por isso:
- conteúdo apoiado só no Anexo N (saida/gcb/D5_anexo_N_mapa_normativo.md), que é a ÚNICA base normativa do lote, e, quando a ficha permitir, em doutrina pacífica sem autor, nos limites da seção 6 da ficha;
- não usar como fonte outros lotes, cursos, pacotes, memória ou espelhos de terceiros; os itens reais do Anexo R servem só para calibrar estilo;
- dúvida de conteúdo que a ficha não resolva vai ao bloco final de resposta à GCB, sem consulta a terceiros.

## 2. Rito (ciclo normal; NÃO é teste cego)
A D-CEGO-2 vale só para o D6. O D5 segue o ciclo do regras/PADRAO_UNICO_v1.md, seção 3, previsto no despacho-base:
qa-normativo-da (Anexo N) → gcb-cpp v1 → gcb-cqfp R1 → gcb-cpp v2 com resposta item a item (acatado / não acatado + motivo) → gcb-cqfp R2 → reconciliação gcb-gerencia → gatilho A.
- A v1 tem a linha de controle do CLAUDE.md (gerado por gcb-cpp). Não há cabeçalho neutro.
- Gate: se o R1 ou o R2 reprovar mais de 30% dos itens, o ciclo para com "GATE: QA reprovou >30% — decisão humana".
- Até o gatilho A aceito, todo item do D5 leva "QA PENDENTE" no registro e nada vai à plataforma nem à candidata (D-QA-PENDENTE).
- Lição do D1 (D-LOTED1-CANONICO; item AUDITORIA em PARA_FUNDADOR.md): a GCB NÃO edita o arquivo revisado no R2, nem por errata de forma. Correção pedida no R2 segue a ficha, seção 9, critério 9 (gcb-cpp grava saida/gcb/D5_v2_1.md com a lista das linhas mudadas → gcb-cqfp faz R2.1 só sobre elas em saida/gcb/D5_parecer_R2_1_gcb-cqfp.md). O parecer R2 registra o SHA-256 do arquivo revisado, que fica intacto.

## 3. Sequência
1. O qa-normativo-da grava "saida/gcb/D5_anexo_N_mapa_normativo.md" (em gravação nesta data) com o núcleo da ficha, seção 3.1 (Lei 14.133/2021, texto compilado vigente em 2/10/2026). A gcb-cpp SÓ inicia o D5 (nem curso nem itens) depois de o Anexo N estar gravado e de o qa-normativo-da ter entregue o bloco à GCB (seção 5), e usa só ele como base normativa.
2. Dispositivos complementares (ficha, seção 3.2) e núcleo faltante: se o Anexo N gravado não trouxer algum, a GCB pede ao qa-normativo-da um adendo no mesmo arquivo (seção "Complementares D5"). A gcb-cpp pode iniciar o curso e os itens apoiados no que o Anexo N já traz, mas NÃO grava item apoiado em dispositivo ausente do Anexo N; no curso, esse dispositivo só aparece com "[SEM FONTE — não afirmar]" até o adendo. Dispositivo que o Anexo N marcar NÃO CONFERIDO não fundamenta item.
3. Insumos (D-DA-INSUMOS): a pasta saida/insumos/ NÃO existe nesta data (conferido pela GCB em 18/10/2026). A v1 é feita sem nenhum insumo externo. Se o Fundador colocar ali o Insumo_ChatGPT_DA_Lab_M01.md depois, a GCB decide se ele entra na v2, só como referência não canônica de estrutura e exemplos, nunca copiado sem QA.
4. A gcb-cpp grava a v1 em "saida/gcb/D5_v1.md", terminando em "FIM DO LOTE D5". Prazo: o ciclo em que a T-74 rodar depois do Anexo N.
5. Responder à GCB em bloco curto, no fim do arquivo ou na resposta: arquivo salvo; contagens por subitem e no total (C/E, [TS], REVERIFICAR, VOLÁTIL, itens de base doutrinária); dispositivos que faltaram no Anexo N; tópicos da cobertura mínima (ficha, seção 5.3) sem base possível; pares espelhados de itens; dúvidas de conteúdo. A GCB decide as dispensas de cobertura ANTES do R1, por escrito, e as informa à gcb-cqfp.
6. A gcb-cqfp faz o R1 em "saida/gcb/D5_parecer_R1_gcb-cqfp.md": conferência de cada item contra o Anexo N (dispositivo citado existe e sustenta o gabarito; prazo, percentual, rol e verbo literais), mecanismo e [TS], ponto controverso, ausência de valor monetário, repetição de ponto de julgamento do Anexo R ou entre itens do lote, delimitação da ficha, seção 5.2, contagens e critérios da ficha, seção 9; veredito por item (APROVADO / APROVADO COM AJUSTE / REPROVADO) e por bloco (curso, resumo, pares, pegadinhas, proveniência).
7. A gcb-cpp grava a v2 em "saida/gcb/D5_v2.md", com a tabela de resposta item a item ao R1 na seção 0 (só afirmações que o arquivo comprove). A gcb-cqfp faz o R2 em "saida/gcb/D5_parecer_R2_gcb-cqfp.md", com a seção 0 avaliada como bloco próprio e o SHA-256 do arquivo revisado. Correções pedidas no R2: seção 2 deste despacho (v2.1 e R2.1).
8. A gcb-gerencia reconcilia em "saida/gcb/T74_reconciliacao_<data ISO>.md", sem alterar nenhum arquivo de produção, e emite o gatilho A em PARA_PRESIDENCIA.md, se todas as condições estiverem cumpridas.

## 4. Meta
v1 no primeiro ciclo depois do Anexo N; canônico (gatilho A aceito) até 1/11/2026, salvo gate.

## 5. QA normativo prévio (agente qa-normativo-da, já instalado)
Mesmo método dos Despachos 11 (D6) e 12 (D1): texto compilado do planalto.gov.br; transcrição por artigo, inciso, parágrafo e alínea; "redação dada por" e "incluído por"; data da consulta; "não aberta" ou "texto corrompido" → NÃO CONFERIDO, nunca de memória; REVERIFICAR em dispositivo com redação dada por norma de 2025 ou 2026; edital 13.33 (vale a norma vigente em 2/10/2026; alteração posterior registrada sem incorporação).
- TAREFA DO D5: "saida/gcb/D5_anexo_N_mapa_normativo.md" — núcleo da ficha, seção 3.1 (em gravação em 18/10/2026) e, por adendo se faltar, os complementares da seção 3.2. Os valores monetários atualizáveis só entram se o qa-normativo-da transcrever o valor vigente em 2/10/2026 e o ato de atualização; do contrário, o lote não usa valor (ficha, seção 3.3).
- Entrega: o arquivo e um bloco curto à GCB com os dispositivos NÃO CONFERIDOS.

D1 da GCB (18/10/2026), para registro: (i) o D5 não segue a D-CEGO-2 (só D6) e corre no ciclo normal do despacho-base; (ii) número de itens = 30 (ficha, seção 5.1: um item do edital; subitens 10.2 a 10.5 sem análogo real apto no banco; os 10 adicionais concentrados neles), com [TS] = 15 e C entre 12 e 18; (iii) base doutrinária só em ponto pacífico, com teto de 4 (1 em 10.1, 1 em 10.2, 2 em 10.3), porque o lote é de letra de lei e o 10.3 ("características") é o único subitem de natureza doutrinária; (iv) delimitação entre 10.4, 10.5, 10.6 e 10.7 fixada na ficha, seção 5.2, para que os subitens com texto parecido não repitam ponto de julgamento; (v) VOLÁTIL = 0 pela exclusão de valores monetários; (vi) lições do D1 incorporadas: dispensas de cobertura decididas antes do R1; pares obrigatórios não exigem item; nenhuma errata de Gerência depois do R2 (v2.1 + R2.1); SHA-256 do arquivo revisado registrado no R2.
