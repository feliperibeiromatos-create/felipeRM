# V15_BAEF_reconciliacao_GCE_2026-10-18.md — T-110 (B), T-111 (A), T-112 (E), T-113 onda 1 (F1), P2 — reconciliação final da GCE — ciclo 2026-10-18 s14c3 — gerado por gce-gerencia

Normas: saida/gce/V15_BAEF_D1_GCE_2026-10-18.md (seções 0 a 5); saida/pacote/V15_BAE_D1_GBQ_2026-10-18.md (contrato v1.2.9, seções 1 a 4); D-REFORCO-2 (regras 1 a 6); D-V15-ENCOMENDA; D-V112-ESCOPO; D-V15-PLATAFORMA.
Pareceres finais: saida/gce/QA_T110_R2, QA_T111_A1_R2 a A4_R2, QA_T112_R2, QA_T113_A_R2 a D_R2 (_2026-10-18_gce-cqfp.md); saida/gce/T113_D_normativo_2026-10-18_qa-normativo.md (SHA-256 cf15dac5…dc4c6); saida/banco/estilo_onda_F1.md (gbq-estilo, SHA-256 6087b1e1…51d3c).
Conferência por script próprio (`python -I`, scratchpad, somente leitura) sobre os arquivos finais e sobre saida/pacote/pacote.json v1.11 (SHA-256 1b5657c7…ac069517, idêntico a gerador_v1_11/out). A GCE não produz nem revisa; nenhum arquivo de produção ou de QA foi alterado. A única escrita de conteúdo é a transcrição da seção 3.1, prevista na D1 (seção 0, 4). Nada vai à plataforma nem à candidata.

## 1. Arquivos finais (os únicos que a GBQ consome para P2 na v1.12)

| Frente | Arquivo final | SHA-256 | Bytes | Fim de linha / linhas | Parecer final |
|---|---|---|--:|---|---|
| B | saida/gce/T110_pares_P2_v2.md | 83fba5e390a82e25f2eae86c26e15455fb41e73dda36256ce62a4ff1b7b568cc | 27877 | CRLF / 288 | R2 APROVADO |
| A1 | saida/gce/T111_resumos_P2_A1_v2_GCE.md (transcrição da GCE sobre a v2, seção 3.1) | 0ad69e62ad8c341316a30748a53c32760c32fe2c0a8924b83dfbe855034081a3 | 8930 | LF / 74 | R2 APROVADO, com a correção editorial da R2 transcrita |
| A2 | saida/gce/T111_resumos_P2_A2_v2.md | 33e93d9b144e9b9628019722e7f2f46558f5decd41b1c118b9aec7072cfb1cc7 | 29059 | CRLF / 215 | R2 APROVADO |
| A3 | saida/gce/T111_resumos_P2_A3_v2.md | 5ee79dce85db85a224d7473271ab8c7de62e352ed9b0a8731b5a9f1bf19e2a19 | 26230 | CRLF / 216 | R2 APROVADO |
| A4 | saida/gce/T111_resumos_P2_A4_v2.md | d63def08b9ac46a90bb1b3089ecf1bb87c7484214fdaa21fb5cb99e511640d6f | 30634 | LF / 242 | R2 APROVADO (ressalva de curso, seção 3.2) |
| E | saida/gce/T112_piloto_visual_P2_v2.md | bcd7d5f2e1536c7198bbdbbd8f84415e6aff2647185e7e8a2dae27f0364e6cb4 | 10461 | LF / 178 | R2 APROVADO |
| F1-A | saida/gce/T113_onda1_A_v2.md | 8c15789308f7a7f5d295ee1a740b0707701dfb723f7fb3ecee2ce201760df081 | 53611 | LF / 430 | R2 APROVADO 30/30; menos L1-R140 (estilo, seção 4.4); errata L1-R137 |
| F1-B | saida/gce/T113_onda1_B_v2.md | 74602cafd57d6bf10722068ecd30b54f771a46cc2c2e050e41a270b98016f01b | 66956 | LF / 486 | R2 APROVADO 30/30; errata L1-R167 |
| F1-C | saida/gce/T113_onda1_C_v2.md | 4176f744be8d7e6ad250553f1996652fa2b136ff2c36d9e1beab7adc06e2b047 | 75651 | CRLF / 477 | R2 APROVADO COM RESSALVAS 27/30 (L2-R136, R137, R140 vagos) |
| F1-D | saida/gce/T113_onda1_D_v2.md | 70a10dd095e332d1cc052900c4d48bb9e83eae5d6bb2b66bfe213718baa888fc | 37162 | CRLF / 229 | R2 APROVADO COM RESSALVAS 14/15 (L3-R101 vago); normativo CONFERE R105–R108; L3-R103 e R104 diferidos (seção 4.2); errata L3-R108 e URL |

- Os SHA-256 de A4 e C conferem com os citados nos pareceres R2 (C: 4176f744…047).
- A v2 da A1 (saida/gce/T111_resumos_P2_A1_v2.md, SHA-256 89ebde77…6f0d) fica como rastro; a GBQ consome a _v2_GCE. Diferença entre as duas, por diff: só a linha 1 (título) e a 1ª frase do P5 de P2-1.4, no corpo (l. 40) e no JSON (l. 65).
- Os _v1 e os pareceres R1 ficam como rastro e não entram na v1.12.
- Os fins de linha mistos (CRLF em 5 arquivos) não afetam o conteúdo; a GBQ lê em texto (precedente do .gitattributes da v1.11).

## 2. Conferência por script

Em cada .md de B, A e E, exatamente 1 bloco ```json```, JSON válido; última linha "FIM DO ARQUIVO". Os quatro arquivos de F1 têm o formato da onda 4 (PARTE 1/3 MAPA, 2/3 itens, 3/3 gabarito; "FIM DO LOTE"), sem bloco JSON, como manda a D1 (4.1, 9).

**B (T-110)**
- JSON `{"pegadinhas_novas":[…]}`: 24 entradas (L1 9, L2 6, L3 9), cada uma só com `lote`, `inserirDepois`, `itemEdital`, `rotulo`, `texto`.
- Por itemEdital: L1 1.1 1, 1.2 1, 1.3 1, 1.4 1, 1.6 2, 1.7 1, 1.8 2; L2 2.1 1, 2.2 1, 2.3 1, 2.5 1, 2.8 2; L3 3.1 1, 3.2 2, 3.3 2, 3.4 2, 4.1 1, 4.3 1.
- Tabela (a): 67 pares = 24 CONVERTIDO + 43 DESCARTADO (D1 41, D2 1, D3 1, D4 0).
- Contra o pacote v1.11: `inserirDepois` = posição (1-based) da última pegadinha do mesmo itemEdital no lote em 24/24; `rotulo` igual ao das existentes em 24/24; prefixo "Não confunda " em 24/24; até 60 palavras depois dos dois-pontos em 24/24; itemEdital do edital em 24/24.
- Marcas de produção no texto e no rótulo: zero. Única "/" é o nome do endpoint "/audio/translations" (L1, P2-1.8), não separador; admitida.
- Pegadinhas de P2 na v1.12: 108 + 24 = 132.

**A (T-111)**
- 23 tópicos de P2 com resumo (A1 2, A2 7, A3 7, A4 7), cada chave só com `resumo`, ordem do edital em cada arquivo. Não são 22: os 23 de P2 da seção 2 da D1 da GBQ estão cobertos, e nenhum fica sem resumo.
- Regra 2.1 da D1 da GCE cumprida nos 23 (total entre 120 e o teto efetivo; 3 a 6 parágrafos; 25 a 80 palavras por parágrafo; quebra só por `\n\n`; nenhum início por algarismo ou RÓTULO em maiúsculas com dois-pontos; marcas de produção zero):

| Tópico | Palavras / teto | Parágrafos | Tópico | Palavras / teto | Parágrafos |
|---|---|--:|---|---|--:|
| P2-1.1 | 188 / 188 | 4 | P2-2.5 | 221 / 222 | 4 |
| P2-1.2 | 172 / 173 | 3 | P2-2.6 | 211 / 218 | 5 |
| P2-1.3 | 265 / 277 | 5 | P2-2.7 | 125 / 138 | 3 |
| P2-1.4 | 294 / 300 | 5 | P2-2.8 | 215 / 216 | 5 |
| P2-1.5 | 148 / 148 | 4 | P2-3.1 | 268 / 268 | 5 |
| P2-1.6 | 220 / 247 | 4 | P2-3.2 | 159 / 159 | 5 |
| P2-1.7 | 176 / 177 | 4 | P2-3.3 | 151 / 155 | 4 |
| P2-1.8 | 276 / 300 | 5 | P2-3.4 | 187 / 188 | 5 |
| P2-2.1 | 194 / 216 | 4 | P2-4.1 | 298 / 300 | 6 |
| P2-2.2 | 175 / 179 | 4 | P2-4.2 | 269 / 300 | 6 |
| P2-2.3 | 183 / 209 | 4 | P2-4.3 | 255 / 300 | 5 |
| P2-2.4 | 204 / 205 | 4 | | | |

- P2-1.4 depois da transcrição: 294 palavras, P5 com 67, como previsto na R2.

**E (T-112)**
- Chaves P2-1.4 e P2-2.5, cada uma só com `emUmMinuto` e `visuais`, sem `resumo` (a GBQ funde com a A).
- `emUmMinuto`: 3 strings em cada tópico (1.4: 25, 27, 22 palavras; 2.5: 20, 27, 21), até 30.
- `visuais`: 1.4 fluxo (5 passos, maior 46 caracteres), tabela (3 colunas × 3 linhas, células iguais às colunas, maior 70), esquema (4 ramos, maior 42); 2.5 tabela (3 × 5, maior 69), esquema (4 ramos, maior 58). Tipos distintos por tópico; campos só os do contrato; sem `barras`. Marcas de produção zero.

**F1 (T-113 onda 1)**
- Ids e ordem iguais nas três partes, iguais aos da D1: A 30, B 30, C 30, D 15; "FIM DO LOTE" na última linha dos quatro.
- Parte 2 (enunciados): sem gabarito, [TS], VOLÁTIL, REVERIFICAR, URL ou "você".
- Linhas "Justificativa:" da Parte 3 (o que vai ao pacote): zero marcas de produção. As linhas de metadado ("Base:", VOLÁTIL, "REVERIFICAR", "Conferência de base … (T-11, gce-cqfp)", "Aderência:") são do formato da onda 4 e ficam fora do texto do estudante, como na consolidação da onda 4.
- Aderência DIRETA em 105/105. Formato de cada item novo conferido entre o MAPA e as tabelas do cabeçalho de cada parte: coincidem nas 13 folhas.

## 3. Frentes B, A e E — decisões D1

### 3.1 P2-1.4, P5 (correção editorial da R2 da A1) — aplicada

Transcrita pela GCE em saida/gce/T111_resumos_P2_A1_v2_GCE.md, texto exato da R2, sem nova rodada (a R2 é a última e o defeito é de redação, não de conteúdo):
- antes: "A diarização tem limites técnicos e de oferta: falham a fala sobreposta, as vozes parecidas e o ruído de plenário em canal único."
- depois: "A diarização tem limites técnicos e de oferta: sofre com fala sobreposta, vozes parecidas e ruído de plenário em canal único."
- Conferido por script: 2 ocorrências trocadas (corpo e JSON), 0 resíduo da frase antiga; nenhuma outra string do JSON mudou.

### 3.2 Ressalva de curso do 4.2 (Lei 9.610/1998, art. 7º) — errata de curso da GCE, não gatilho B

- Achado (QA_T111_A4_R2, seção 3): o curso canônico do Lote 3 (saida/gce/GCE_Lote3_v2_CPP.md, l. 430–431, SHA-256 c9840292…aa16; no pacote, lotes[L3].curso, bloco 4.2) diz "criações do espírito fixadas em qualquer suporte". O art. 7º, caput, diz "expressas por qualquer meio ou fixadas em qualquer suporte, tangível ou intangível". Como está, o curso leva a julgar C um item que a lei faria E.
- Classificação: errata textual de curso dentro do domínio da GCE (precedente T-106 / D-L2-T84-ERRATA). Não é gatilho B (nada fora do domínio) nem D (não muda gabarito, item, rótulo nem escopo).
- Encaminhamento: tarefa nova T-114 em TAREFAS.md (qa-normativo confere o art. 7º no Planalto; gce-cpp propõe o texto exato da troca no curso e, depois, a do resumo do 4.2; gce-cqfp revisa; GCE reconcilia e emite gatilho A da errata). O resumo do 4.2 entra na v1.12 como aprovado: ele segue o curso, não afirma "apenas" fixadas e não contradiz a lei; a reescrita entra na ocorrência seguinte com a errata do curso.

### 3.3 Demais

- B: as notas "(R1: …)" e a seção "Resposta ao QA R1" do T110_pares_P2_v2.md ficam fora do JSON; sem efeito.
- Regra de tamanho do resumo: a GCE mantém a da sua D1 (2.1); a diferença com a da GCB já foi registrada pela GCB para arbitragem da GBQ, se ela quiser regra única.

## 4. Frente F1 — decisões D1

### 4.1 PENDENTE NORMATIVO de L3-R105 a R108 — baixado

O parecer do qa-normativo (T113_D_normativo, 18/10/2026) dá CONFERE aos quatro (art. 6º, V, VIII e IX; art. 9º, § 1º; art. 41, caput e § 1º; todos em redação original, sem marca da Lei 13.853/2019 nem da Lei 15.352/2026; "não VOLÁTIL" confere). O PENDENTE NORMATIVO da R2 da parte D fica baixado.

**Errata de forma (URL), a aplicar pela GBQ na consolidação:** em saida/gce/T113_onda1_D_v2.md, "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm" → "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm" nas 3 ocorrências (MAPA, linha de R105; Base de R105, l. 207; Base de R108, l. 222). Os R106 e R107 remetem a "mesma URL" e ficam cobertos. Texto dos dispositivos idêntico nas duas URLs (parecer, observações 1 e 4); nada muda no enunciado nem no gabarito.

### 4.2 P2-3.1: VOLÁTIL 6/29 e SH 9/29 — dois itens diferidos para a onda 2

- Fato: com o L3-R101 vago, a 3.1 ficaria com 29 itens, 6 VOLÁTEIS (20,7%) e também 9 SH (31,0%). A R2 registrou o VOLÁTIL, mas deu o formato como cumprido ("8,7 de 29"); 9 > 8,7, então o teto de 30% da regra 3 da D-REFORCO-2 também seria excedido. Ambos os excessos vêm só do denominador (o produtor fechou 6/30 e 9/30), mas as regras 3 e 4 são do Fundador e valem "na folha depois da onda"; a GCE não tem alçada para consolidar a folha acima delas.
- Opções examinadas: (a) reclassificação — recusada: o rótulo VOLÁTIL baixo do R104 foi fixado na R1 e confirmado na R2, e mudar rótulo para fechar conta é o que o revisor recusou com razão; (b) declarar 6/29 com saldo — recusada: publicaria a v1.12 com duas regras canônicas excedidas, o que exigiria gatilho C; (c) **diferir para a fila — adotada**.
- **Decisão:** L3-R104 (VOLÁTIL baixo, D, E [TS]; Microsoft Learn) e L3-R103 (SH, C; Microsoft Learn) ficam **diferidos**: aprovados na R2, não entram na v1.12, mantêm o id (não são vagos) e entram na onda 2 da F, sem nova QA de conteúdo (só a conferência de base de janeiro já prevista). Escolhidos por serem os dois de fornecedor da folha, o que também atende à preferência da D1 (4.1, 3) por base de parlamento ou órgão público depois da concentração da onda 4 em Microsoft.
- Efeito na 3.1 da v1.12: 27 itens; VOLÁTIL 5/27 (18,5%); formatos D 7, TSj 3, SH 8, NP 1, PC 6, AP 2 (maior 8/27 = 29,6%); novos 3 C / 3 E (faixa de 3 a 6 C cumprida); fornecedor: UIP 4, Google 1, Câmara 1.
- Condição para a onda 2 na 3.1: R103 + R104 + 1 item novo, não VOLÁTIL e não SH → 30 itens, VOLÁTIL 6/30, SH 9/30.

### 4.3 Auditoria de estilo (saida/banco/estilo_onda_F1.md) — 11/108, sem GATE

7 CONFORME, 3 AJUSTE (texto), 1 NÃO CONFORME (9,1%; gate 30%). Decisões:

**AJUSTE (texto) — erratas de forma aplicadas na consolidação pela GBQ, sem nova rodada de QA** (precedente D1 pós-R2 da T-108 / T-78; o texto é o do gbq-estilo, o gabarito, o [TS], o ponto do MAPA, a base e a justificativa ficam iguais). Conferência por script da GCE: cada "antes" ocorre 1 vez no arquivo (Parte 2); cada "depois" é idêntico ao texto proposto na seção 2 do estilo; a justificativa existente sustenta o novo enunciado sem mudança (R137: "will result in the most accurate transcription and billing"; R167: WDER × WER; R108: art. 6º, IX × VIII, conferido pelo qa-normativo).

| id | arquivo | antes (enunciado, Parte 2) | depois | gabarito | formato (MAPA e Parte 3) |
|---|---|---|---|---|---|
| L1-R137 | T113_onda1_A_v2.md | "Ao enviar as gravações de uma comissão ao Google Cloud Speech-to-Text, a equipe descreve na configuração da requisição a codificação do áudio, o idioma falado e o modelo de reconhecimento realmente adequados a essas gravações. De acordo com a documentação do Google Cloud, descrever com exatidão os dados de áudio enviados contribui para a obtenção da transcrição mais precisa e da cobrança correta da requisição." | "De acordo com a documentação do Google Cloud Speech-to-Text, descrever na configuração da requisição a codificação correta do áudio e usar o idioma e o modelo de reconhecimento corretos contribui para a transcrição mais precisa e para a cobrança correta da requisição." | C (mantido) | SH → D (sem cenário) |
| L1-R167 | T113_onda1_B_v2.md | "Segundo a nota de transparência do Azure Speech, a qualidade da diarização é medida pela taxa de erro de palavras (WER), de modo que o serviço não adota métrica específica para a atribuição das palavras aos falantes." | "Segundo a nota de transparência do Azure Speech, a qualidade da diarização é medida pela taxa de erro de palavras (WER)." | E [TS] (mantido) | TSj (mantido) |
| L3-R108 | T113_onda1_D_v2.md | "Um órgão público utiliza sistema de inteligência artificial para classificar as falas de audiências públicas. Nessa situação, segundo a Lei Geral de Proteção de Dados Pessoais, a impossibilidade de realização do tratamento para fins discriminatórios ilícitos ou abusivos corresponde ao princípio da prevenção." | "Segundo a Lei Geral de Proteção de Dados Pessoais, o princípio da prevenção corresponde à impossibilidade de realização do tratamento para fins discriminatórios ilícitos ou abusivos." | E [TS] (mantido) | SH → TSj (atribui ao VIII a definição do IX; D não, porque D já está acima do teto por LEGADO na 4.1) |

Reclassificação de formato conferida: 1.1 fica D 6/29, SH 4/29; 4.1 fica SH 3, TSj 3, D 22 (LEGADO, sem novo D). Nenhum teto excedido.

**L1-R140 (NÃO CONFORME: o nome InitialSilenceTimeout entrega o gabarito) — retirado, id vago.** A R2 foi a última rodada e a D1 (5.2) não admite terceira; refazer na mesma onda seria R3. O id L1-R140 não é reutilizado; o saldo +1 da 1.1 passa à onda 2, com a recomendação 3 do estilo (troca que não seja dedutível do nome). Com isso a ressalva da R1 da parte A (pontos de API de fornecedor na 1.1) fica com R137 e R139, admitidos com precedente canônico, e o par de aberturas R139 × R140 deixa de existir.

**L1-R136 (exame opcional, pista de raiz "di-"/"tri-")** — não reaberto. A R2 julgou a troca detectável pela definição correta de trifone presente no próprio item, e o estilo classificou a pista como mais fraca que a do R140, sem veredito. Fica para a montagem de simulado e para a recomendação 3 da onda 2. Recomendações 1 a 6 do estilo (extensão C × E, molduras "Nessa situação, segundo" e "Uma equipe", "ao passo que" em C) vão à D1 da onda 2; não alteram os itens desta onda.

### 4.4 Ressalvas sem efeito

- Proveniência do Manual de Comunicação da Câmara (R2 da parte D): só servia ao L3-R101 e ao L2-R140, ambos vagos. Sem objeto.
- VOLÁTEIS e conferências de base vão à fila de janeiro (4–8/1/2027), como dizem as R2.

## 5. Contagens por folha, antes e depois (o que entra na v1.12)

Existentes: v1.11 e, na 3.1, a onda 4 (D-T98-ONDA4-ACEITE). C/E por script sobre o pacote.json v1.11 e os arquivos da onda 4; VOLÁTEIS existentes da D1 (seção 4).

| Folha | Antes (C/E) | VOLÁTIL antes | Novos que entram (C/E) | [TS] novos | VOLÁTIL novos | Depois (C/E) | VOLÁTIL depois | Maior formato depois | Vagos / diferidos |
|---|---|---|---|--:|--:|---|---|---|---|
| P2-1.1 | 20 (8/12) | 0 | 9 (5/4) | 4 | 1 | 29 (13/16) | 1/29 | PC 7/29 | L1-R140 vago |
| P2-1.2 | 20 (11/9) | 0 | 10 (5/5) | 5 | 0 | 30 (16/14) | 0/30 | SH 7/30 | — |
| P2-1.3 | 20 (9/11) | 3 | 10 (6/4) | 4 | 3 | 30 (15/15) | 6/30 | D, TSj 6/30 | — |
| P2-1.4 | 20 (11/9) | 3 | 10 (4/6) | 5 | 3 | 30 (15/15) | 6/30 | SH 8/30 | — |
| P2-1.5 | 20 (11/9) | 3 | 10 (5/5) | 5 | 3 | 30 (16/14) | 6/30 | D 8/30 | — |
| P2-1.6 | 20 (9/11) | 1 | 10 (4/6) | 6 | 5 | 30 (13/17) | 6/30 | D, SH 8/30 | — |
| P2-1.7 | 20 (9/11) | 3 | 10 (5/5) | 5 | 3 | 30 (14/16) | 6/30 | SH, AP 7/30 | — |
| P2-1.8 | 20 (11/9) | 2 | 10 (5/5) | 5 | 0 | 30 (16/14) | 2/30 | SH 8/30 | — |
| P2-2.1 | 20 (11/9) | 2 | 7 (4/3) | 3 | 3 | 27 (15/12) | 5/27 | D 7/27 | L2-R136, R137, R140 vagos |
| P2-2.2 | 20 (9/11) | 1 | 1 (1/0) | 0 | 0 | 21 (10/11) | 1/21 | TSj, SH 7/21 (LEGADO) | — |
| P2-2.8 | 19 (9/10) | 4 | 1 (0/1) | 1 | 0 | 20 (9/11) | 4/20 | D 7/20 (LEGADO) | — |
| P2-3.1 | 21 (10/11) | 4 | 6 (3/3) | 4 | 1 | 27 (13/14) | 5/27 | SH 8/27 | L3-R101 vago; L3-R103, R104 diferidos |
| P2-4.1 | 26 (16/10) | 1 | 4 (2/2) | 2 | 0 | 30 (18/12) | 1/30 | D 22/30 (LEGADO) | — |

**Por parte (o que entra):** A 29 (16 C / 13 E, 55,2%); B 30 (13 / 17, 43,3%); C 27 (14 / 13, 51,9%); D 12 (6 / 6, 50,0%). **Total F1 P2: 98 itens, 49 C / 49 E (50,0%)**, [TS] 49, VOLÁTEIS novos 22, aderência direta 98/98. Faixas de C cumpridas por folha de +10 (4 a 6), na 3.1 (3 a 6), na 4.1 (2) e por parte.

**Ids:** produzidos 105; entram 98; vagos 5 (L1-R140, L2-R136, L2-R137, L2-R140, L3-R101), não reutilizados; diferidos 2 (L3-R103, L3-R104), aprovados, com id mantido.

**Saldo para a onda 2 da F (P2):** 7 = P2-1.1 +1 (id novo; não PC); P2-2.1 +3 (ids novos; até 1 VOLÁTIL); P2-3.1 +3 (L3-R103 e R104 diferidos + 1 id novo não VOLÁTIL e não SH). Com o saldo, as 12 folhas-alvo de P2 chegam a 30 (2.2 a 21 e 2.8 a 20, como previsto).

## 6. Gatilho

Gatilho A da GCE em PARA_PRESIDENCIA.md (ciclo s14c3): aceite de B, A, E e F1 de P2, nos arquivos da seção 1, com as erratas das seções 3.1, 4.1 e 4.3 e as exclusões da seção 5, para consolidação pela GBQ na v1.12. A condição de estilo do F1 está satisfeita (auditoria recebida, sem GATE, decidida em 4.3). Tarefa nova: T-114 (seção 3.2).

FIM DO ARQUIVO
