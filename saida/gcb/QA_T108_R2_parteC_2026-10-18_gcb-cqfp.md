# QA_T108_R2_parteC_2026-10-18_gcb-cqfp.md — T-108, GCB, QA R2 (última rodada), Parte C — 2026-10-18 — gcb-cqfp

Objeto (D1 pós-R1, seção 6): em `saida/gcb/T108_substituicoes_GCB_parteC_v2.csv`, as 9 linhas corrigidas (C0002, C0004, C0005, C0006, C0097, C0103, C0105, C0108, C0116) e as 6 novas (C0156 a C0161); a linha CI nova de `saida/gcb/T108_fontes_GCB.md`; as respostas em `saida/gcb/T108_producao_notas_GCB_v2_parteC.md`. As 146 linhas aprovadas na R1 não voltaram ao mérito. Texto-base: `saida/pacote/pacote.json` v1.10, SHA-256 LF d43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed (conferido). Somente leitura: a QA não editou CSV, tabela de fontes, pacote, lotes, DECISOES, TAREFAS nem PARA_PRESIDENCIA; sem commit. Script próprio (python -I, fora do repositório; cópia do `T108_inventario.py` importada só para `varre`/`campos`, sem chamar `main`, que gravaria o CSV de ocorrências).

## 1. Veredito da Parte C

APROVADO. Objeto: 15 linhas + 1 linha de fonte. REPROVADO: 0/15 (0,0%). APROVADO: 15/15; linha CI: APROVADA. Nada volta à D1 da GCB. Duas pendências de registro para a reconciliação (seção 5), nenhuma delas é reprovação.

## 2. Mecânica

| checagem | resultado |
|---|---|
| (a) linhas fora do objeto iguais à v1 | OK. Comparação por registro bruto (bytes, CRLF, sem BOM nas duas): cabeçalho igual; ordem da v1 preservada; 146 registros byte a byte iguais; mudam só os 9 do objeto; 6 novos no fim (C0156 a C0161). Campos alterados: C0002, C0004, C0005 só `regra`; C0097 só `depois`; C0103, C0105, C0108, C0116 `ids_ocorrencia`, `depois`, `nota`; C0006 `ids_ocorrencia`, `categoria`, `trecho`, `antes`, `depois`, `regra`, `fonte_origem`, `nota` (os três últimos descritivos, acompanhando o código CI; aceitos). |
| (b) `antes` literal e único na v1.10 | OK nas 161 linhas (não só no objeto). |
| (b) sobreposição | 0 em todo o conjunto v2. Uma adjacência sem sobreposição: C0157 termina onde começa C0098 (lotes[L6B].curso). Aplicação em sequência na ordem do CSV e em ordem inversa: cada `antes` ainda único no momento de aplicar; resultados idênticos. |
| (c) cobertura | OK. Universo da Parte C: 180 ocorrências PROCESSO+VERIFICAR do CSV (lotes 5, 5-C, 6b) + GCB-EXTRA-12 a 22 (11) = 191; cada id em exatamente uma linha; 0 faltando, 0 sobrando; caminho de cada id do CSV = caminho da linha. EXTRA: 12→C0006; 13→C0156; 14→C0157; 15→C0158; 16→C0103; 17→C0105; 18→C0108; 19→C0116; 20→C0159; 21→C0160; 22→C0161 (confere com a seção 2 do D1 e com a nota de produção). |
| (d) re-varredura após aplicação | Antes: 5 = 68 P + 3 V; 5-C = 24 P + 3 V; 6b = 78 P + 4 V. Depois: 0 PROCESSO, 0 VERIFICAR nos três lotes. FP-CONTEUDO do 6b: 39 = 39, mesmos casamentos por campo. "A tecla F4" é da Parte B; não se aplica. |
| (d) resíduo das marcas (seção 5, checagem 6) | 0 de "(O11)", "fundamenta item", "neste chat", "não sutil", "entra em item", "entram em item", "(CI,", código CI isolado, "ITENS REAIS", "TC/GI/IC/AT invertida", "indevida invertida", "CQFP" em todos os campos dos lotes 5, 5-C e 6b. "hoje" minúsculo: 0. Resta 1 "Hoje," maiúsculo em lotes[L6B].curso, 4.2.3 ("Hoje, muitos produtos de segurança incorporam antivírus, antispyware e firewall num pacote"): é conteúdo (estado atual do mercado), não marca de produção; não está entre os EXTRA do D1. Ver seção 5, P-2. |
| (e) DELETAR / SUBSTITUIR | 0 DELETAR com `depois` não vazio (C0160 e C0161 vazios); 0 SUBSTITUIR com `depois` vazio. |
| (e) intactos | Com os campos tocados zerados, o resto do pacote é idêntico; enunciado, gabarito e itemEdital idênticos em todos os itens. |
| ", às avessas" | C0059, C0128, C0151, C0154 entre as 146 iguais à v1 (seção 3 do D1: ficam como estão). |

## 3. Linha CI de `T108_fontes_GCB.md` contra o arquivo do lote

`git diff`: uma única linha acrescentada, na tabela do Lote 5, logo após GG4; nada mais no arquivo mudou. Texto idêntico ao do achado A-1 do parecer R1. Contra `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md`: l. 29 é o cabeçalho FONTES DE FERRAMENTA; l. 38 = "CI — Google Cloud, Data Studio "Conversational Analytics — Code Interpreter" (verificada pela CQFP em 8/10/2026; F1)" com a URL docs.cloud.google.com/data-studio/conversational-analytics-code-interpreter. Nome, linha, cabeçalho e data (08/10/2026, verificada pela CQFP) conferem; nenhuma fonte nova. APROVADA.

URLs reabertas pela QA hoje (18/10/2026, curl): docs.cloud.google.com/data-studio/conversational-analytics-code-interpreter (200; a frase citada em C0005/C0006, "translates natural language questions into Python code to provide advanced analysis and visualizations", consta); cartilha.cert.br/ransomware/ (200; "torna inacessíveis os dados armazenados em um equipamento", citado na C0108); cartilha.cert.br/dicas-rapidas/ (200; "Faça backups periódicos.", citado no trecho da C0158). Datas de verificação no texto (8/10/2026 e 08/10/2026) constam das tabelas dos lotes 5 e 6b.

## 4. Mérito, linha a linha

| id_edicao | lote | caminho | ação | regra | veredito | motivo |
|---|---|---|---|---|---|---|
| GCB-C0002 | 5 | lotes[L5].resumo | SUBSTITUIR | 5 | APROVADO | A-3 aplicado: só `regra` 4→5; texto igual à v1. |
| GCB-C0004 | 5 | lotes[L5].curso | SUBSTITUIR | 5 | APROVADO | A-3 aplicado: só `regra`. |
| GCB-C0005 | 5 | lotes[L5].curso | SUBSTITUIR | 5 | APROVADO | A-3 aplicado: só `regra`. |
| GCB-C0006 | 5 | lotes[L5].curso | SUBSTITUIR | 2 | APROVADO | A-1 aplicado no texto exato (`antes`, `depois`, regra 2, `fonte_origem`); EXTRA-12 em `ids_ocorrencia`; nome igual ao da tabela; data mantida; sai a menção à CQFP. |
| GCB-C0097 | 6b | lotes[L6B].curso | SUBSTITUIR | 5 | APROVADO | A-2 aplicado no texto exato; só `depois` mudou. |
| GCB-C0103 | 6b | lotes[L6B].curso | SUBSTITUIR | 5 | APROVADO | Caso (c): "sem fonte consultada."; sem data; EXTRA-16. |
| GCB-C0105 | 6b | lotes[L6B].curso | SUBSTITUIR | 2 | APROVADO | Caso (a): sai "aberta hoje"; a frase mantém "verificado em 08/10/2026"; nome F4 = tabela; EXTRA-17. |
| GCB-C0108 | 6b | lotes[L6B].curso | SUBSTITUIR | 2 | APROVADO | Caso (a); nome F2 = tabela; data mantida; EXTRA-18. |
| GCB-C0116 | 6b | lotes[L6B].curso | SUBSTITUIR | 2 | APROVADO | Caso (a); nome F4 = tabela; data mantida; EXTRA-19. |
| GCB-C0156 | 6b | lotes[L6B].curso | SUBSTITUIR | 5 | APROVADO | Caso (c), título 4.0.2: "sem base consultada"; sem data. |
| GCB-C0157 | 6b | lotes[L6B].curso | SUBSTITUIR | 5 | APROVADO | Caso (b): "A leitura de 08/10/2026 "; data do lote 6b (tabela, F4 08/10/2026). Adjacente a C0098 sem sobreposição; resultado "A leitura de 08/10/2026 de CERT.br, "Cartilha de Segurança para Internet" (livro, PDF), menciona…", forma prevista na seção 4 do D1; português correto. |
| GCB-C0158 | 6b | lotes[L6B].curso | SUBSTITUIR | 5 | APROVADO | Caso (b): "Fontes consultadas em 08/10/2026:"; termina nos dois-pontos, antes do trecho da C0100 (F3); sem sobreposição. A frase já dizia "ambos verificados em 08/10/2026": a repetição da data é a forma fixada pelo D1, sem fato novo. |
| GCB-C0159 | 6b | itens[6B-06].justificativa | SUBSTITUIR | 5 | APROVADO | Caso (c): "não foi confirmada em fonte consultada"; sem data. |
| GCB-C0160 | 6b | lotes[L6B].curso | DELETAR | 5 | APROVADO | Sai só " (seção ITENS REAIS acima)"; a referência aos itens 96 e 98 do TRF6 2024 fica; com C0099 (aprovada na R1) a frase lê "…cujo ponto de julgamento foi conferido contra o caderno oficial em 08/10/2026." |
| GCB-C0161 | 6b | itens[6B-06].justificativa | DELETAR | 5 | APROVADO | Sai só " (seção ITENS REAIS)"; a justificativa fecha em "…com outro ponto de julgamento." |

Critérios: correção do R1 no texto exato; cada EXTRA retirou só a marca, sem perder informação útil, sem fato novo; data posta no lugar de "hoje" só 08/10/2026 e só nos casos (b); nenhuma data nos casos (c). Itens do checklist geral sem objeto nesta rodada: não há item AUTORAL, [TS] nem enunciado no escopo (enunciados intactos); nenhuma linha do objeto cita lei.

## 5. Respostas da produtora e pendências (sem veredito de linha)

- Seção 1 das notas: todas as respostas conferem com o aplicado (A-1, A-2, A-3; R-1 e R-3 encaminhados como diz o D1). Contagem "155 da v1 + 6 novas = 161" confere.
- P-1 (item 7 das notas): o resumo de `T108_fontes_GCB.md` (l. 99) continua "Lote 5 = 8 (U1-U6, TB2, GG4)", mas a tabela do Lote 5 tem agora 9 códigos (com CI). A produtora não alterou por força do D1 ("nada mais nesse arquivo muda"), corretamente. Fica para a reconciliação atualizar o resumo para 9 e registrar que CI é código fora do padrão do inventário. Não é reprovação.
- P-2 (item 6 das notas): a frase "0 de 'hoje' no curso inteiro dos lotes 5 e 6b" só vale para o minúsculo. Resta "Hoje, muitos produtos de segurança…" (6b, 4.2.3), que é conteúdo e não marca de produção; não está entre os EXTRA do D1 e não se pede ação na T-108. Registro para a reconciliação (a GCB decide se é conteúdo a manter, como esta QA entende).
- Adjacências C0157/C0098 e C0158/C0100: conferidas por script (fim de um `antes` = início do outro, ou separados); sem sobreposição; aplicação independente da ordem.

## 6. Resumo

Parte C v2: APROVADA, 15/15 linhas do objeto e a linha CI; 0% de reprovação; mecânica sem falha (146 iguais à v1, `antes` único, 0 sobreposição, cobertura 180 + 11 EXTRA, 0 PROCESSO e 0 VERIFICAR, FP-CONTEUDO 39 = 39). Pendências P-1 (resumo "Lote 5 = 8") e P-2 ("Hoje," de conteúdo) para a reconciliação.
