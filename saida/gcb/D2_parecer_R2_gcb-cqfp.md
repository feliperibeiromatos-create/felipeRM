# D2_parecer_R2_gcb-cqfp.md — T-75 — 2026-10-20 — gerado por gcb-cqfp
PARECER R2 — LOTE D2 v2 (saida/gcb/D2_v2.md, gcb-cpp; SHA-256 50c213af26ac25cc217bc768a45cfa75f1d65778aadca155022a94e6d279cde7; 467.513 bytes; LF; 2.386 linhas). Conferido contra: o R1 (saida/gcb/D2_parecer_R1_gcb-cqfp.md, 2632a096…7d53); a v1 (saida/gcb/D2_v1.md, b357d93e…9b79, a mesma do R1), por diff de script; a D1 da GCB (saida/gcb/D2_D1_GCB_v2_2026-10-20.md, 0953de5c…7385); a leitura externa (saida/gcb/D2_leitura_critica.md, 89bddf07…a30c) e a seção 0.1 da v2; a ficha (saida/gcb/D2_ficha_lote.md, 5c98fc68…61e6); o Anexo N (saida/gcb/D2_anexo_N_mapa_normativo.md, b0a54fff…340a), única base de texto legal. Modelo: saida/gcb/D5_parecer_R2_gcb-cqfp.md. Revisão; a gcb-cqfp não reescreve. Os textos da seção "Ajustes residuais (texto exato)" são ajustes pontuais fixados. Scripts em python3 -I, no scratchpad (diretório r2d2, nomes com lote, tarefa e rodada: items_D2_T75_R2.py, cmp_D2_T75_R2.py, diff_D2_T75_R2.py, cit_D2_T75_R2.py, web_D2_T75_R2.py, seq_D2_T75_R2.py, copy2_D2_T75_R2.py, ajustes_D2_T75_R2.py); navegador não usado; sem commit.

## 0. Resultado
- Itens: 80 (D2-01 a D2-80). **APROVADO 80; AJUSTE 0; REPROVADO 0. Reprovação no R2: 0/80 = 0%** (limite do gate: 30%). Não há gate. Não sobra item reprovado (ficha, seção 11, critério 9).
- Os 15 itens "QA PENDENTE (R2)" estão todos APROVADOS (seção 5). Os 65 demais são idênticos à v1, campo a campo, e mantêm o veredito APROVADO do R1.
- Os 9 textos fixados no R1 (2.1, n. 1 a 9) entraram literalmente; as três decisões da GCB (troca na folha 4.1, art. 135, moldura) estão aplicadas e registradas; as sequências de gabaritos e de [TS] reproduzem as da D1 da GCB e passam no teste da ficha 6.4 na folha, nos itens 3 e 4 e no lote.
- Blocos: curso APROVADO COM AJUSTE (2 exemplos com erro de conteúdo, 1 omissão de condição legal, 2 marcas inexatas e 2 repetições de forma; tudo fora de item); resumo APROVADO (inalterado); pares APROVADO; pegadinhas APROVADO COM AJUSTE (redação copiada da leitura externa em 9 delas e em 3 pegadinhas de bloco); proveniência APROVADO; contagens APROVADO; registro de acatamento da leitura externa APROVADO COM RESSALVAS (seção 4).
- **Veredito geral: APROVADO COM RESSALVAS.** Nenhuma ressalva obrigatória toca item: enunciado, gabarito, [TS], ponto de julgamento ou contagem. São 11 ajustes residuais obrigatórios (ajustes 1 a 11, com 25 substituições de texto exato) e 1 opcional (ajuste 12, 2 substituições), todos na seção "Ajustes residuais (texto exato)". Podem entrar por errata na reconciliação ou numa v2.1, com conferência só do diff, sem nova rodada sobre os itens.
- Ficam com a GCB: o escopo do C3.3-10 e os pontos 19 e 22 (parecer técnico na seção 7); a regeração do arquivo de leitura crítica e a guarda dos scripts (pendentes (a) e (c) da v2).

## 1. Evidência e não regressão (por script)
1. **Itens.** Um script comparou campo a campo a v1 e a v2: enunciado (5.1), cabeçalho e cada campo do gabarito comentado (5.2), aplicado o mapa da folha 4.1. Mudaram só os 15 itens declarados:
   - 9 por ajuste do R1: D2-07, 14, 23, 33, 34, 36, 39, 74 e 80;
   - 3 por troca de conector (ponto 19): D2-15, 30 e 40;
   - 3 renumerados (ponto 10): D2-41, 43 e 44.
   Nos 15, além do que foi pedido, mudaram só a marca "QA PENDENTE (R2)" (cabeçalho e "Marcas") e o campo novo "Alteração na v2". Os outros 65 são idênticos à v1 (enunciado, campos, ordem dos campos e marcas). A ordem do 5.1 é igual à do 5.2; os 80 blocos têm todos os campos fixos da ficha 2.2, item 5; folha do campo igual à do cabeçalho; AUTORAL e QA PENDENTE nos 80.
2. **Fora dos itens.** O diff linha a linha (v1 → v2) mostra só alterações declaradas:
   - linhas 1 e 2 e bloco de convenções (uma vez, o texto da ficha 2.3 com a frase da v2); saíram "## 0. CABEÇALHOS DAS PARTES" e os subtítulos "### Parte A/B"; entraram "## 0" e "## 0.1";
   - curso: 21 blocos novos; 4 textos corrigidos pelo R1 (C3.2-03, C3.3-06, C4.1-06, C4.3-07); 1 correção de ofício declarada na seção 8 (C3.2-07: "cargo público ou da função de confiança", literal do art. 15, caput, conferido no Anexo N);
   - resumo: conteúdo idêntico (só saíram os subtítulos de parte);
   - pares: P-13 a P-26 e P-62 a P-70, e as duas linhas de contagem; pegadinhas: G-36 a G-50, G-104 a G-114 e G-80 (ponto 16);
   - proveniência: só as colunas de dispositivos e observações (as 10 URLs continuam idênticas às da seção 1 do Anexo N); seções 7 e 8 refeitas.
   Nada além do declarado.
3. **Citações (todas as linhas novas ou alteradas, 0, 0.1, curso, pares, pegadinhas, itens alterados, 7 e 8).** Um script extraiu as citações "art./arts.", deduziu a norma pelo contexto e conferiu artigo, parágrafo, inciso e alínea contra os rótulos da seção 4 do Anexo N, com a situação (vigente, revogado, vetado, vigência encerrada, posterior a 2/10/2026).
   - 1.169 caminhos conferidos e existentes, vigentes.
   - 117 avisos, conferidos um a um: nenhum é erro. São (i) menções expressas de dispositivo fora do lote ou excluído, como tal (CF, art. 5º, LIV e LV; CF, art. 169; Lei 8.112, art. 143, §§ 1º e 2º, e art. 8º, III e IV, revogados; art. 103, § 4º, que a seção 0.1 diz não existir; CF, art. 40, § 4º, na nota da EC 140/2026); (ii) remissões que estão dentro do próprio texto transcrito (CF, arts. 7º, 42, 142 e 202); (iii) artefatos de leitura (norma deduzida errada, enumerações "11, 12, caput, 13, II…", parágrafo atribuído ao artigo anterior).
   - Validei o teste com citações falsas plantadas, e ele acusou todas: CF, art. 37, § 17; Lei 8.112, art. 103, § 4º; art. 25, II, f; art. 143, § 1º (revogado); Lei 9.784, art. 49-A, § 2º (vetado); Decreto 10.835, art. 5º (revogado); CF, art. 40, § 5º-A (posterior); Lei 6.999, art. 2º, § 3º.
   - Leitura: li contra o texto do Anexo N cada um dos 21 blocos novos, os 23 pares novos e as 26 pegadinhas novas (seção 4.4). Os desvios estão nos ajustes 1 a 5 e 9.
4. **Fonte oficial.** Reabri em 20/10/2026, às 12:18 UTC, por curl com User-Agent de navegador (sem navegador), cinco URLs da proveniência, idênticas às do Anexo N: Fontes 1, 4, 6, 7 e 9. Todas deram HTTP 200, com bytes iguais aos do Anexo N (1.507.134; 343.733; 74.941; 71.902; 8.785). Os 446 dispositivos dessas cinco normas citados nas linhas novas ou alteradas aparecem literalmente na página de hoje (comparação sem espaços e sem sinal de ordinal): 446/446. Os SHA-256 do HTML de hoje diferem dos registrados no Anexo N, com o mesmo tamanho; fica só o registro.
5. **Itens sem regressão de regra.** Nos 80 enunciados: "razão pela qual" 0; "exceto" 0; ADI, ADPF, STF, TCU, doutrina 0; "[SEM FONTE" em item 0; VOLÁTIL 0; REVERIFICAR 2 (D2-01 e D2-28, inalterados).

## 2. Conferência das respostas aos 34 pontos do R1
| Ponto R1 | Objeto | Resposta da v2 | Texto fixado entrou literal? | Veredito R2 |
|---|---|---|---|---|
| 1 | D2-07 | Acolhido | Sim: enunciado, ponto e linha 2 (script, igualdade de cadeia) | APROVADO |
| 2 | D2-14 | Acolhido | Sim: enunciado, ponto, formato SIT e linha 2; folha 3.2 = DEF 3, SUJ 3, SIT 2, NUM 1, PAR 0, APL 1 (conferido) | APROVADO |
| 3 | D2-23 | Acolhido | Sim: enunciado, ponto e linha 2 | APROVADO |
| 4 | D2-33 | Acolhido | Sim: campo "troca" | APROVADO |
| 5 | D2-34 | Acolhido | Sim: "difere de BQ-0150" | APROVADO |
| 6 | D2-36 | Acolhido | Sim: "difere de BQ-0125" | APROVADO |
| 7 | D2-39 | Acolhido | Sim: "difere de BQ-0126" | APROVADO |
| 8 | D2-74 | Acolhido | Sim: enunciado e linha 2 | APROVADO |
| 9 | D2-80 | Acolhido | Sim: linha 2, base e "difere de BQ-0132" | APROVADO |
| 10 | Sequência (folha 4.1) | Acolhido (D1 da GCB, seção 2) | Mapa v1 → v2 conferido por script; texto dos três itens idêntico | APROVADO (seção 3) |
| 11 | Art. 135 | Acolhido (GCB, opção (i)) | Registro nas seções 7 e 8 conferido | APROVADO (seção 3) |
| 12 | Junção e forma | Acolhido em parte (forma fixada pela GCB, seção 5) | Linha 1, linha 2, convenções uma vez, títulos "##" 0, 0.1 e 1 a 8, "### 5.x" literais, "FIM DO LOTE D2" | APROVADO |
| 13 | Neutralidade e leitura crítica | Acolhido como registro | SHA-256 do arquivo enviado (linha 2 da leitura) = 96cd9140…282b = arquivo em disco = o que recebeu NEUTRO CONFERIDO (saida/gcb/QA_neutralidade_D2_D4_2026-10-20_gcb-cqfp.md, seção 7); a versão 558a24d4…b2e9 não saiu, e não há desvio a levar ao Fundador (D1 da GCB, seção 5, (c)) | APROVADO |
| 14 | C3.3-06 | Acolhido | Sim | APROVADO |
| 15 | C4.1-06 | Acolhido | Sim, mas a cauda antiga ficou ("… e não entram nesta folha") | APROVADO COM AJUSTE (ajuste 7, forma) |
| 16 | C4.3-07 e G-80 | Acolhido | Sim, nas duas ocorrências | APROVADO |
| 17 | C3.2-03, exemplo | Acolhido | Sim, mas a cauda antiga ficou ("reservada a quem tem cargo efetivo" duas vezes). O recorte do texto fixado no R1 não cobria a cauda | APROVADO COM AJUSTE (ajuste 6, forma) |
| 18 | Moldura (9 C de 10) | Não acolhido (GCB, opção (i)) | Contagem 10 APL, 9 C / 1 E, e regras (a) a (c) à GBQ conferidas | APROVADO (decisão da GCB) |
| 19 | Marcadores lexicais | Acolhido em parte | Conector variado nos D2-15, 30 e 40 (0 "razão pela qual" nos enunciados); o C com termo absoluto não foi feito, com motivo | Parte acolhida APROVADA; parte não acolhida: motivo aceito, parecer na seção 7; ajuste 11 (forma) |
| 20 | Notas à GBQ | Acolhido como registro | Os 8 pares do R1 conferidos, com ids da v2; acréscimo D2-41/43/49 pertinente | APROVADO |
| 21 | "Difere de D1-NN" | Acolhido | D1: D2-41, 43, 49, 72; BQ: 15 itens; 16 distintos (script) | APROVADO |
| 22 | Campo "Formato" | Não acolhido (opcional) | — | Motivo aceito; parecer na seção 7 |
| 23 | Contagens | Acolhido | Refeitas pela QA (seção 6): conferem | APROVADO |
| 24 a 34 | Dúvidas A-1 a A-5 e B-1 a B-12 | Acolhidos como registro | — | APROVADO |

As contagens da seção 8 da v2 conferem: 34 pontos, com 30 acolhidos (entre eles os "como registro" e "como regra de processo"), 2 em parte (12 e 19) e 2 não acolhidos (18 e 22).

## 3. Decisões da GCB aplicadas
- **Troca na folha 4.1 (ponto 10).** v1 D2-44 → D2-41; v1 D2-41 → D2-43; v1 D2-43 → D2-44; D2-42 e D2-45 a D2-50 sem mudança. Por script, cada item com o id novo tem o mesmo enunciado e os mesmos campos (ponto, formato, gabarito, justificativas, base, mecanismo, troca, "difere de" e marca [TS]) do item com o id antigo. Gabaritos de junção: D2-39 = E, D2-40 = E, D2-41 = C, D2-42 = C. A lista de "difere de D1-NN" e a tabela de correspondência da seção 8 usam a numeração nova. Sequências: seção 6.
- **Art. 135 (ponto 11, opção (i)).** Nenhum item da 4.2 foi trocado (os 10 da 4.2 são idênticos à v1). Seção 7 com "art. 135: sem item; dispensa da D1 da GCB (D2_D1_GCB_v2_2026-10-20.md, seção 3)"; seção 8 com o registro para o D2-R, na letra do caput ("exercido por não ocupante de cargo efetivo") e do parágrafo único. O tópico segue no curso (C4.2) e no par P-58.
- **Moldura (ponto 18, opção (i)).** Nenhum item alterado por este ponto. Contagem refeita: 10 itens com a moldura, todos APL (D2-05, 10, 19, 38, 45, 48, 52, 53, 61 e 74), 9 C e 1 E; nenhuma folha acima de 2; nenhum SIT com a moldura. As regras (a) a (c) de montagem e o registro para o D2-R (moldura nova preferencialmente E) estão na seção 8, iguais à D1.
- **Forma da v2 (D1 da GCB, seção 5).** Arquivo único; linha 1 "# D2_v2.md — T-75 — 2026-10-20 — gerado por gcb-cpp"; linha 2 literal; convenções uma vez (o texto da ficha 2.3, conferido por script, com a frase sobre "QA PENDENTE (R2)"); títulos e última linha conformes. O D2_v1.md e as partes não foram reescritos.

## 4. Registro de acatamento da leitura externa (seção 0.1 da v2)
### 4.1 Arquivo enviado e contagens
- O SHA-256 do arquivo enviado, na linha 2 do D2_leitura_critica.md, é 96cd914017d1d43e39a725397f21cafa9e05542824181c411e1b4f3ec7cd282b, igual ao do D2_para_leitura_critica.md em disco e ao que recebeu NEUTRO CONFERIDO (saida/gcb/QA_neutralidade_D2_D4_2026-10-20_gcb-cqfp.md, seção 7). A condição da D1 da GCB, seção 5, (c), está cumprida.
- 94 sugestões (24 A, 40 B, 30 C), todas com decisão. Contagens conferidas: A 23 acatadas e 1 não; B 34 (1 em parte) e 6 não; C 17 (4 em parte) e 13 não. Nenhum item foi criado ou alterado por causa da leitura; a seção 5 não mudou por ela (seção 1, n. 1).

### 4.2 Acatamentos: lastro e artigo
Todo acatamento tem lastro literal e vigente no Anexo N, dentro das folhas 3.1 a 4.4. Conferi a letra de cada dispositivo usado:
- CF, art. 37, VI, VII, VIII, XI e §§ 9º a 14; art. 39, §§ 1º, I a III, 2º, 3º, 5º, 7º, 8º e 9º; art. 40, §§ 4º-A, 4º-B, 4º-C, 5º, 6º, 14 a 16 e 19; art. 38, I a V; art. 37, III e IV;
- Lei 8.112, arts. 5º, § 2º; 9º, parágrafo único; 12, caput e § 2º; 13, §§ 2º e 3º; 15, §§ 3º e 4º; 19; 20, §§ 4º e 5º; 24, § 2º; 25, II, e, e § 3º; 36, parágrafo único, II e III; 38; 39; 40; 41; 44; 46; 49; 51; 53, caput e § 3º; 58; 76-A; 77 a 80; 82 a 84; 86; 87; 92; 96-A; 97 a 100; 102; 103; 107, §§ 1º e 2º; 108; 109; 110 a 112; 133, §§ 5º e 6º; 136; 142; 143, caput; 144; 149; 150; 156; 157 a 162; 167; 168; 182, parágrafo único; 196; 202; 203; 207; 208; 226; 229;
- Lei 9.784, arts. 11 a 15 (recordação); 29, §§ 1º e 2º; 31 a 37; 43; 45 a 47; 49-A, § 1º; 49-E a 49-G; 53 a 55 (recordação); 56 a 61; 63;
- Decreto 10.835, arts. 10, 17 a 25 e 30-A; Lei 6.999, arts. 2º a 4º e 8º.

Também estão certas as correções e as notas de artigo do registro: A12 (o art. 103 só tem os §§ 1º a 3º; a sugestão citava § 4º); A5 (art. 51 acrescentado); A7 (art. 53, § 3º); A9 (art. 103, III, por remissão do art. 86, § 2º); A10 (art. 96-A, §§ 1º a 7º); A11 (o § 4º do art. 98 existe e ficou fora do par); B4 e C3 (§ 11 na redação da EC 135/2024, vigente em 2/10/2026, sem REVERIFICAR, porque a emenda é de 2024); C5 (o § 14 é complementar 3.1 no Anexo N); C9 (arts. 17 a 25 marcados "Edital: compl. 3.3" no Anexo N; a marca é do Anexo, e não do Decreto, como diz o registro: imprecisão de forma, sem ajuste). As marcas de núcleo ou complemento citadas nos blocos novos conferem com a coluna "Observação" do Anexo N. As exclusões da ficha (seção 3.2, Vide ADI/ADPF; 3.3, EC 140/2026 e revogados; 3.4, estágio; 8) foram respeitadas: o art. 39, caput, e o art. 127, IV, só aparecem com a nota do compilado; o art. 40, § 18, não aparece; o art. 40, §§ 4º e 5º-A, só como nota; o C3.4-13 cita os prazos do estágio sempre com o referencial.

Os pares de recordação P-66 (A19) e P-69 (A23) têm base no Anexo N dos dois lados e seguem a ficha 5.3 (pares do D1 entram como recordação, sem item). As trocas de B32, B33 e B38, recusadas como ponto do D1, aparecem nesses pares; o registro precisa dizer isso (ajuste 10).

### 4.3 Recusas (A20; B32, B33, B35, B37, B38, B40; C1, C7, C8, C10, C17 a C21, C24, C27, C28, C30; em parte B24, C2, C4, C16, C26): justificadas
- Ponto do D1 (ficha, seção 7): A20, B35 e C26 (art. 42, D1-53 a D1-56); B32, B33 e C24 (arts. 11 a 15, D1-38 a D1-43); B38 e C28 (art. 54, caput, D1-50; arts. 53 e 55); C2 em parte (art. 37, caput, D1-09); C19 (art. 2º, parágrafo único, I, II, III, V e XIII, do D1, e XII, do BQ-0145); B37 e C27 (art. 50, D1-44, 45, 52, 59 e 60; a pegadinha passa pelo § 1º, do D1).
- Exclusão da ficha: B40 e C30 (art. 56, § 3º, e arts. 64-A e 64-B; ficha 5.2, folha 4.4, e 6.7); C21 (Vide ADPF/ADIN; ficha 3.2); B24 em parte (a cassação do § 6º do art. 133 remete ao art. 127, IV).
- Sem lastro no Anexo N: C7 (CF, art. 169, fora do recorte); C17 e C18 (CF, art. 5º, LIV e LV, "fora do despacho, não aberta"); C10 (prerrogativa de requisição da Câmara: [SEM FONTE — não afirmar], ficha, seção 4).
- Doutrina sem texto na norma (ficha 3.1): C1, C8, C20.
- C4 em parte: defensável, porque o conteúdo do art. 7º, a que remete o § 3º do art. 39, não foi aberto. Mas o C3.1-11 diz que a própria enumeração dos incisos "não foi aberta", e ela está no Anexo N (ajuste 5).
- C16 em parte: o art. 215 remete à Lei 10.887/2004, não aberta, e a recusa procede. O motivo dado ao art. 217 ("redações de 2015 e 2019 que dependem de normas não abertas") é inexato: o texto do art. 217 está no Anexo N, e a divergência do inciso IV, c, foi dirimida pela Fonte 5 (alerta 6). A recusa por escopo continua válida; o motivo é corrigido no ajuste 9.

### 4.4 Os 21 blocos novos, os 23 pares e as 26 pegadinhas: veredito
| Conteúdo novo | Veredito | Observação |
|---|---|---|
| C3.1-09 | APROVADO | Art. 37, VI a VIII, e art. 5º, § 2º, literais; "até 20%" na lei, e não no inciso |
| C3.1-10 | APROVADO | XI e §§ 9º a 14 literais. O "(90,25%)" do § 12 é conversão aritmética exata de "noventa inteiros e vinte e cinco centésimos por cento" |
| C3.1-11 | APROVADO COM AJUSTE | Ajuste 5 (§ 3º: enumeração dos incisos) |
| C3.1-12 | APROVADO | §§ 4º-A a 4º-C, 5º, 6º, 14 a 16 e 19 literais; sem § 4º, § 5º-A e § 18 |
| C3.3-10 | APROVADO COM AJUSTE | Definições literais (arts. 10, 17 a 22, 24, 25 e 30-A, parágrafo único). Exemplo errado (ajuste 2). Escopo: seção 7 |
| C3.3-11 | APROVADO | Lei 6.999, arts. 2º a 4º, literais; "[SEM FONTE]" sobre a Câmara mantido |
| C3.4-12 | APROVADO | Arts. 13, §§ 2º e 3º; 15, §§ 3º e 4º; 19; 38; 39 literais |
| C3.4-13 | APROVADO | Arts. 24, § 2º; 25, II, e, e § 3º; 20, §§ 4º e 5º; 36; 53, § 3º; estágio com referencial |
| C3.4-14 | APROVADO COM AJUSTE | Ajuste 3 (art. 76-A, condição do inciso III omitida) |
| C3.4-15 | APROVADO | Arts. 77 a 80 literais; §§ 1º e 2º do art. 78 e parágrafo único do art. 79 ditos revogados |
| C3.4-16 | APROVADO | Arts. 82 a 84, 86, 87, 92 e 96-A literais (no § 2º do art. 96-A a paráfrase omite o segundo requisito, mas não o nega; sem efeito) |
| C3.4-17 | APROVADO COM AJUSTE | Arts. 97 a 103 literais; pegadinha copiada (ajuste 8c) |
| C3.4-18 | APROVADO COM AJUSTE | Arts. 107 a 112 literais; pegadinha copiada (ajuste 8a) |
| C3.4-19 | APROVADO COM AJUSTE | Arts. 196 a 229 literais; marca inexata sobre o art. 207 (ajuste 4) e motivo do art. 217 (ajuste 9b) |
| C4.3-14 | APROVADO | Arts. 157 a 162 literais |
| C4.3-15 | APROVADO | Art. 167, caput e §§ 1º e 2º literais |
| C4.3-16 | APROVADO | Art. 133, §§ 5º e 6º; a cassação do § 6º só com a nota da ficha 3.2 |
| C4.4-18 | APROVADO | Arts. 31 a 35 literais |
| C4.4-19 | APROVADO | Arts. 29, §§ 1º e 2º, 36, 37, 43, 45, 46 e 47 literais; art. 42 fora (D1) |
| C4.4-20 | APROVADO COM AJUSTE | Arts. 49-A, § 1º, e 49-E a 49-G literais. Exemplo contrário ao art. 49-A, caput e § 6º, III (ajuste 1) |
| C4.4-21 | APROVADO COM AJUSTE | Art. 63 literal; pegadinha copiada (ajuste 8k) |
| P-13 a P-26 | APROVADOS | Diferença e base conferidas com o Anexo N, dispositivo de cada lado; cada troca da coluna "como a banca troca" é falsa pela letra |
| P-62 a P-70 | APROVADOS | Idem; P-66 e P-69 são recordação (ficha 5.3); P-63 cita o art. 56, § 1º (BQ-0132), só como contraste, sem item |
| G-36 a G-41, G-43 a G-47, G-50, G-106, G-109, G-111 a G-113 | APROVADAS | Dispositivo que a desfaz correto; semelhança com a sugestão abaixo do critério (seção 4.5) |
| G-42, G-48, G-49, G-104, G-105, G-107, G-108, G-110, G-114 | APROVADAS COM AJUSTE | Redação copiada (ajustes 8b, 8d a 8j, 8l) |

As 26 G novas apontam blocos existentes, e cada uma tem "— Dispositivo:". Contagens conferidas por script: curso 109 blocos (12/7/11/19/10/13/16/21), mais o C3.0-01; pares 26 + 20; pegadinhas 50 + 64 (G-01 a G-114, sem falta e sem repetição); todo bloco, exceto o de caput, tem pegadinha provável.

Forma (sem ajuste): os blocos novos levam "QA PENDENTE (R2)" no título, mas as 26 G novas levam só "[acréscimo da v2]", e os pares novos estão marcados só na linha de introdução da seção 3. A D1 da GCB, seção 6, pede a marca em tudo o que foi acatado. Com este R2, a marca perde o objeto: o conteúdo novo está conferido.

### 4.5 Redação copiada da sugestão externa
Script: cada oração nova (curso, pares e pegadinhas) foi comparada com cada sugestão da leitura, pela razão de semelhança e pelo maior trecho comum de palavras que não é letra do Anexo N. O critério é o do D5 R2 (G-68): razão ≥ 0,85, ou trecho comum de 10 ou mais palavras fora da letra da lei, é cópia.
- **Cópia (ajuste 8):**
  - pegadinha do C3.4-18 e G-49 × B19: 0,98 e 0,81; trecho de 17 e 13 palavras;
  - G-107 × B28: 0,77; 17 palavras;
  - G-104 × B25: 0,83; 12 palavras;
  - pegadinha do C3.4-17 e G-48 × B17: 0,89 e 0,89; 12 e 9 palavras;
  - G-105 × B26: 0,80; 11 palavras;
  - G-110 × B31: 0,93;
  - G-114 e pegadinha do C4.4-21 × B39: 0,87 e 0,81 (a mesma frase);
  - G-108 × B29: 0,86;
  - G-42 (segunda oração) × B22: 0,85.
  O texto novo de cada um baixa a semelhança para 0,38 a 0,70, sem trecho comum fora da letra da lei acima de 6 palavras, e mantém o dispositivo.
- **Não é cópia:** os títulos dos pares que repetem o nome dos institutos (P-18, P-20 a P-25, P-63); orações dominadas pela letra da lei (G-40 × B20, 0,80, trecho não legal de 7 palavras; G-106 × B23); estrutura de frase curta determinada pela norma (G-36 × B1, 0,83, 7 palavras; G-45 × B13, 0,78, 8 palavras). No D5 foram aceitos até 0,77, com trechos de 8 e 9 palavras. G-36 (0,83) e G-40 (0,80) passam de 0,77, mas o trecho comum que não é letra da lei tem só 7 palavras e a frase é ditada pela norma; ficam sem ajuste.

## 5. Itens "QA PENDENTE (R2)": veredito item a item (15)
| Item | Folha | Gab. | Objeto do R2 | Veredito |
|---|---|---|---|---|
| D2-07 | 3.1 | E | Texto fixado; moldura verdadeira (§ 2º, inciso II) e segmento falso único (prazo de validade "sem nulidade"); não toca o D1-18 nem o D2-02; E5 sem [TS], como na v1 | APROVADO |
| D2-14 | 3.2 | C | Texto fixado; SIT com moldura genérica; não traz mais a proposição do D2-13; [TS] isca "mínimos" literal do art. 37, V; nota à GBQ (D2-13 × D2-14) mantida | APROVADO |
| D2-15 | 3.2 | E | "de modo que … nunca poderá" × art. 9º, parágrafo único; E5, um erro | APROVADO |
| D2-23 | 3.3 | E | Texto fixado; um só erro (efetivo exercício, parágrafo único da Lei 9.007, art. 2º) | APROVADO |
| D2-30 | 3.3 | E | "e, por isso, não lhe é facultado declinar" × art. 18, § 2º; E5 | APROVADO |
| D2-33 | 3.4 | E | Campo "troca" fixado; troca única (inclusão da exoneração, art. 33, I) | APROVADO |
| D2-34 | 3.4 | C | "Difere de BQ-0150" fixado e pertinente | APROVADO |
| D2-36 | 3.4 | E | "Difere de BQ-0125" fixado e pertinente | APROVADO |
| D2-39 | 3.4 | E | "Difere de BQ-0126" fixado e pertinente; gabarito de junção E | APROVADO |
| D2-40 | 3.4 | E | "o que significa que, indeferido o pedido, não cabe recurso" × art. 107, I; E5; gabarito de junção E | APROVADO |
| D2-41 | 4.1 | C | Renumerado (v1 D2-44); conteúdo idêntico; gabarito de junção C | APROVADO |
| D2-43 | 4.1 | C | Renumerado (v1 D2-41); conteúdo idêntico; [TS] isca | APROVADO |
| D2-44 | 4.1 | E | Renumerado (v1 D2-43); conteúdo idêntico; [TS] | APROVADO |
| D2-74 | 4.4 | C | Texto fixado; "interessado" afasta a leitura da lei própria do servidor (arts. 104 a 115 da Lei 8.112); APL; o gabarito não depende do Legislativo | APROVADO |
| D2-80 | 4.4 | E | Linha 2, base (art. 56, caput) e "difere de BQ-0132" fixados | APROVADO |

## 6. Contagens e sequência de gabaritos (refeitas por script sobre a v2)
- 80 itens; 10 por folha; C por folha 5/5/4/5 e 5/6/5/5; item 3 com 19 C, item 4 com 21 C, lote com 40 C / 40 E (50%). [TS] = 5 por folha (4 E e 1 C com elemento-isca), 20 por item do edital, 40 no lote; marca coerente nos três lugares (cabeçalho, "Marcas" e campo "troca") nos 80; nenhum [TS] C sem "elemento-isca".
- Formatos (DEF/SUJ/SIT/NUM/PAR/APL), teto de 3 respeitado e APL ≤ 2 por folha:
  - 3.1: 3/1/1/2/1/2;
  - 3.2: 3/3/2/1/0/1;
  - 3.3: 3/1/2/2/2/0;
  - 3.4: 3/0/2/2/2/1;
  - 4.1: 3/0/3/0/2/2;
  - 4.2: 3/0/2/3/0/2;
  - 4.3: 3/0/2/3/1/1;
  - 4.4: 3/0/2/3/1/1.
  Todos iguais aos da v2.
- REVERIFICAR 2 (3.1 e 3.3); VOLÁTIL 0. "QA PENDENTE (R2)" = 15 (1/2/2/5/3/0/0/2 por folha), igual ao declarado. 80 pontos de julgamento distintos; a lista da seção 7 da v2 é igual aos 80 campos.
- Gabaritos do lote, na ordem de apresentação: ECECCEECECCCECEECCEEECEECECCEECEECCECCEECCCECEECEEECCCEECECCCEECCECCEEECCCECCEEE, idêntica à da D1 da GCB, seção 1.
  - Lote: maior corrida 3; maior alternância 4; maior bloco repetido de período 2/3/4 = 4/7/7; de período 5/6 = 8/11. **APROVADO** (ficha 6.4).
  - Item 3: 3; 4; 4/7/7; 8/11. Item 4: 3; 4; 4/7/7; 8/9. As 8 folhas também estão APROVADAS.
  - Informativo: período 7 = 14 (D2-51 a D2-64); período 8 = 13 (D2-13 a D2-25). Igual ao declarado.
- [TS]: TnTTnTnnTnnnTTnTnnTTTnnTnTTnTnnTTnTTnnTnnnTTnnTnTTTnnnTTnTTnnTTTnTnnTnTTnnTnnTTn, idêntica à da D1.
  - Lote: corrida 3; alternância 4; períodos 2/3/4 = 4/7/7; 5/6 = 9/11. **APROVADO** na folha, nos itens 3 e 4 e no lote.
  - Informativo: período 7 = 11; período 8 = 15 (D2-34 a D2-48).
- A falha de junção do R1 (período 4 por 8 itens, D2-36 a D2-43; alternância de [TS] por 7, D2-38 a D2-44) está corrigida. Os números da seção 7 da v2 conferem um a um com os meus.

## 7. Pendências da produção — parecer técnico à GCB (a decisão é da GCB)
### 7.1 Escopo do C3.3-10 (Decreto 10.835, arts. 17 a 22, 24 e 25, "compl. 3.3"; pendente (b) da v2)
1. **O bloco cabe nas regras.** Os dispositivos estão no Anexo N, vigentes, marcados "Edital: compl. 3.3", e o Decreto foi transcrito na íntegra. A ficha 5.2 lista o reembolso (art. 10) entre os tópicos da folha 3.3. O critério da D1 da GCB, seção 6, está cumprido: lastro literal, dentro do item 3, nenhum ponto do D1 ou do Anexo R, sem item novo. Nada na ficha (seções 3.2, 3.3, 3.4 e 8) exclui esses artigos.
2. **O que pesa contra:** nível e extensão. A ficha, seção 1, fixa "noções", e os arts. 24 e 25 (prazos do pedido de reembolso e rol de parcelas) são operacionais, com baixa probabilidade de cobrança no cargo. O bloco é o mais longo da folha. O exemplo do bloco também estava errado (ajuste 2).
3. **Recomendação da QA:** manter o C3.3-10, com o ajuste 2. Se a GCB quiser enxugar, retirar só os arts. 24 e 25 da definição, o trecho correspondente da pegadinha ("trocar o prazo do pedido de reembolso…") e a última oração do G-41. Isso não mexe em item, par obrigatório ou contagem. Os arts. 10, 18, 19, 21, 22 e 30-A, parágrafo único, têm o maior valor de prova (regra × exceção do reembolso; dispensa de novo ato × comunicação prévia) e devem ficar.

### 7.2 Ponto 19, parte não acolhida (C com termo absoluto definicional)
1. **Dado:** 14 enunciados com termo absoluto, 13 E e 1 C (D2-37), ou 93% de E, contra 50% no lote. No banco de referência (estilo_banca, seção 4), a proporção é de 2 C para 6 E, e o guia manda incluir "item C com termo absoluto definicional, para que o marcador não vire atalho" (5.2, E6, passo 4; 5.1).
2. **Registro de causa:** a QA concorreu para o número. O texto fixado no R1 para o D2-14 tirou do lote o seu único C com "exclusivamente".
3. **O motivo da produtora é aceito.** Criar o C pediria item novo ou reescrita de item C aprovado, fora do escopo da v2 e contra a ordem de entrega.
4. **Recomendação, sem efeito no veredito:**
   - (a) registro para o D2-R: ao menos 3 itens C com termo absoluto que é a própria letra da norma, por exemplo "para qualquer efeito" (Lei 8.112, art. 49, § 1º), "nenhum servidor" (art. 41, § 5º) e "somente" (art. 20, § 4º), dispositivos que não são ponto de item da v1;
   - (b) regra de montagem à GBQ, enquanto o D2-R não existir: simulado com 3 ou mais itens do D2 com termo absoluto leva o D2-37, ou um C equivalente de outro lote.

### 7.3 Ponto 22 (normalizar o campo "Formato")
O motivo é aceito. A diferença é de forma: a parte B escreve "DEF — afirmação …", e a parte A só o código. O código das três primeiras letras é o que as contagens usam. A QA conferiu os 80 campos por esse código, sem ambiguidade. Recomendação: não normalizar agora. Na exportação, a GBQ toma só o código (as 3 primeiras letras do campo). Se houver v2.1 por errata, a normalização pode ir junto, por substituição mecânica, sem rodada de QA.

### 7.4 Demais pendentes da v2
- **(a) Regeração do D2_para_leitura_critica.md.** Não é necessária para o aceite: a leitura externa já veio e foi tratada. Regerar só se a GCB quiser uma segunda leitura. Nesse caso, gerar o arquivo pelos mesmos scripts e pedir novo NEUTRO CONFERIDO.
- **(c) Scripts.** Recomendo guardar no repositório, em tarefa própria, os scripts de teste da v2 e os deste R2, para reprodutibilidade (a T-75 grava só o parecer).
- **(e) Acatamento.** Conferido na seção 4.

## Ajustes residuais (texto exato)
Todos ficam fora dos itens, exceto o opcional 12, que muda só o campo "ponto" do D2-13. Nenhum muda gabarito, [TS], ponto de julgamento de item avaliado no R2 ou contagem. Cada "trecho atual" foi copiado do D2_v2.md (SHA-256 50c213af…cde7) e ocorre nele uma única vez. Por script (ajustes_D2_T75_R2.py), os 27 trechos foram aplicados em sequência numa cópia no scratchpad, e todos continuaram únicos em cada passo. Os textos novos se apoiam na letra do Anexo N (dispositivos indicados em cada justificativa). Nos ajustes 8, o "Dispositivo" de cada pegadinha não muda. Depois dos ajustes 8c e 8d, a pegadinha do C3.4-17 e a G-48 passam a ter o mesmo texto; depois dos 8k e 8l, o mesmo vale para a pegadinha do C4.4-21 e a G-114. Aplicados por errata, a QA confere só o diff.

### Ajuste 1
Obrigatório (conteúdo). O exemplo põe órgão do Poder Legislativo da União numa decisão coordenada; o art. 49-A, caput, a restringe ao "âmbito da Administração Pública federal", e o § 6º, III, a exclui quando estejam envolvidas autoridades de Poderes distintos. O exemplo do C4.4-11 (v1) diz o contrário deste.

**1. C4.4-20, exemplo.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
Considere que, em decisão coordenada de que participe órgão do Poder Legislativo da União no desempenho de função administrativa, um órgão participante discorde da solução proposta: o dissenso deve ser manifestado durante as reuniões, de forma fundamentada, com as propostas de solução e de alteração necessárias (art. 49-F, caput). O exemplo é hipotético; a moldura não afirma regra interna da Câmara.
```
Texto novo:
```text
Considere que, em decisão coordenada no âmbito da administração pública federal, com três órgãos participantes, um deles discorde da solução proposta: o dissenso deve ser manifestado durante as reuniões, de forma fundamentada, com as propostas de solução e de alteração necessárias (art. 49-F, caput). A decisão coordenada não se aplica aos processos em que estejam envolvidas autoridades de Poderes distintos (art. 49-A, § 6º, III; C4.4-11). O exemplo é hipotético.
```

### Ajuste 2
Obrigatório (conteúdo e ficha, seção 4). O exemplo aplica o art. 19 do Decreto 10.835 a movimentação para órgão do Poder Legislativo; a conclusão ("não há reembolso pela administração pública federal") não responde quem arcaria com o ônus no destino (art. 21) e aproxima o lote da afirmação vedada de que o Decreto rege o Legislativo. Os exemplos da v1 na folha 3.3 (C3.3-01 a C3.3-09) evitam esse destino.

**2. C3.3-10, exemplo.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
Considere que servidor de autarquia federal seja movimentado para órgão do Poder Legislativo da União: a movimentação ocorre no âmbito dos Poderes da União e de suas autarquias, e não há reembolso pela administração pública federal (art. 19). O exemplo é hipotético; não afirma regra interna da Câmara.
```
Texto novo:
```text
Considere que servidor de autarquia federal seja cedido a órgão da administração direta federal: a movimentação ocorre no âmbito dos Poderes da União e de suas autarquias, e não há reembolso pela administração pública federal (art. 19). O exemplo é hipotético; não afirma que o Decreto se aplica à Câmara.
```

### Ajuste 3
Obrigatório (ficha 6.5: paráfrase não omite o dado literal). A definição omite a condição do inciso III ("quando tais atividades não estiverem incluídas entre as suas atribuições permanentes"), o que induz a leitura falsa de que toda participação na logística de concurso gera a gratificação. Completam-se também os incisos I e IV pela letra.

**3. C3.4-14, definição, art. 76-A.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
atue como instrutor em curso de formação, de desenvolvimento ou de treinamento, participe de banca examinadora ou de comissão para exames orais, para análise curricular, para correção de provas discursivas, para elaboração de questões de provas ou para julgamento de recursos intentados por candidatos, participe da logística de preparação e de realização de concurso público ou participe da aplicação, fiscalize ou avalie provas de exame vestibular ou de concurso público;
```
Texto novo:
```text
atue como instrutor em curso de formação, de desenvolvimento ou de treinamento regularmente instituído no âmbito da administração pública federal (I), participe de banca examinadora ou de comissão para exames orais, para análise curricular, para correção de provas discursivas, para elaboração de questões de provas ou para julgamento de recursos intentados por candidatos (II), participe da logística de preparação e de realização de concurso público, quando essas atividades não estiverem incluídas entre as suas atribuições permanentes (III), ou participe da aplicação, fiscalize ou avalie provas de exame vestibular ou de concurso público ou supervisione essas atividades (IV);
```

### Ajuste 4
Obrigatório (exatidão). O caput do art. 207 está no Anexo N e fixa 120 dias consecutivos; o que não foi aberto é o Decreto 6.690/2008. A marca [SEM FONTE] sobre "a duração da licença" é inexata.

**4. C3.4-19, definição, art. 207, caput.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
O caput do art. 207 traz remissão a decreto de 2008, não aberto: [SEM FONTE — não afirmar] sobre a duração da licença.
```
Texto novo:
```text
Art. 207, caput: será concedida licença à servidora gestante por 120 (cento e vinte) dias consecutivos, sem prejuízo da remuneração; a remissão do caput ao Decreto 6.690/2008 não foi aberta: [SEM FONTE — não afirmar] sobre o conteúdo do decreto.
```

### Ajuste 5
Obrigatório (exatidão). A enumeração dos incisos do art. 7º está no texto do § 3º transcrito no Anexo N; o que não foi aberto é o conteúdo do art. 7º.

**5. C3.1-11, definição, CF, art. 39, § 3º.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
o disposto no art. 7º, nos incisos que o parágrafo enumera (a enumeração não foi aberta neste material)
```
Texto novo:
```text
o disposto no art. 7º, IV, VII, VIII, IX, XII, XIII, XV, XVI, XVII, XVIII, XIX, XX, XXII e XXX (o texto desses incisos do art. 7º não foi aberto neste material: [SEM FONTE — não afirmar])
```

### Ajuste 6
Forma. Repetição criada ao aplicar o ponto 17 (o recorte do texto fixado no R1 deixou a cauda antiga).

**6. C3.2-03, exemplo (repetição criada na aplicação do ponto 17).** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
a função é reservada a quem tem cargo efetivo, reservada a quem tem cargo efetivo (art. 37, V)
```
Texto novo:
```text
a função é reservada a quem tem cargo efetivo (art. 37, V)
```

### Ajuste 7
Forma. Cauda redundante e sem concordância deixada ao aplicar o ponto 15.

**7. C4.1-06, definição (repetição criada na aplicação do ponto 15).** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
nenhum deles é ponto de item desta folha e não entram nesta folha.
```
Texto novo:
```text
nenhum deles é ponto de item desta folha.
```

### Ajuste 8
Redação copiada da leitura externa (ficha, seção 9; D1 da GCB, seção 6: "texto do leitor não é copiado"). Mesmo critério do D5 R2 (G-68): razão de semelhança ≥ 0,85 ou trecho comum de 10 ou mais palavras que não é letra da lei. O dispositivo de cada pegadinha não muda.

**8a. C3.4-18, pegadinha provável.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
dizer que o pedido de reconsideração e o recurso não interrompem a prescrição do direito de requerer
```
Texto novo:
```text
contar a prescrição do direito de requerer sem a interrupção causada pelo pedido de reconsideração ou pelo recurso cabível
```
**8b. G-49.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
dizer que o pedido de reconsideração e o recurso não interrompem a prescrição; dizer que a administração pode relevar
```
Texto novo:
```text
contar a prescrição sem a interrupção causada pelo pedido de reconsideração ou pelo recurso cabível; dizer que a administração pode relevar
```
**8c. C3.4-17, pegadinha provável.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
Exigir compensação de horário do servidor com deficiência ou do servidor com cônjuge, filho ou dependente com deficiência, aplicando-lhes a regra do servidor estudante
```
Texto novo:
```text
Condicionar à compensação de horário o horário especial do servidor com deficiência, ou do que tem cônjuge, filho ou dependente com deficiência, como se fosse o do servidor estudante
```
**8d. G-48.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
Exigir compensação de horário do servidor com deficiência ou com dependente com deficiência, aplicando-lhes a regra do servidor estudante
```
Texto novo:
```text
Condicionar à compensação de horário o horário especial do servidor com deficiência, ou do que tem cônjuge, filho ou dependente com deficiência, como se fosse o do servidor estudante
```
**8e. G-42, segunda oração.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
admitir, sem ressalvas, a requisição de ocupantes de cargos técnicos, científicos ou do magistério, ignorando as restrições e a exceção da nomeação para cargo em comissão
```
Texto novo:
```text
requisitar para a Justiça Eleitoral, fora da hipótese de nomeação para cargo em comissão, ocupante de cargo isolado, de cargo ou emprego técnico ou científico ou de cargo ou emprego do magistério
```
**8f. G-104.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
Atribuir indistintamente a toda demissão os efeitos de indisponibilidade dos bens e de ressarcimento ao erário
```
Texto novo:
```text
Estender a qualquer demissão a indisponibilidade dos bens e o ressarcimento ao erário
```
**8g. G-105.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
Dizer que os prazos de prescrição disciplinar são sempre os de cinco anos, dois anos ou 180 dias, mesmo quando a infração também é crime
```
Texto novo:
```text
Aplicar os prazos de cinco anos, dois anos e 180 dias do art. 142 à infração disciplinar capitulada também como crime, à qual o § 2º manda aplicar os prazos de prescrição da lei penal
```
**8h. G-107, segunda oração.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
dizer que o caráter reservado das reuniões da comissão elimina o direito do acusado de acompanhar o processo
```
Texto novo:
```text
negar ao acusado, por causa do caráter reservado das reuniões e das audiências da comissão, o direito de acompanhar o processo pessoalmente ou por intermédio de procurador
```
**8i. G-108.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
Considerar obrigatória a perícia pedida pelo acusado, mesmo quando a comprovação do fato independe de conhecimento especial de perito
```
Texto novo:
```text
Deferir sempre o pedido de prova pericial do acusado, que o § 2º do art. 156 manda indeferir quando a comprovação do fato independer de conhecimento especial de perito
```
**8j. G-110.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
Atribuir o julgamento de processo com vários indiciados e sanções diversas à autoridade competente para a penalidade mais leve
```
Texto novo:
```text
Entregar à autoridade competente para a pena mais leve o julgamento de processo com mais de um indiciado e diversidade de sanções
```
**8k. C4.4-21, pegadinha provável.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
- Pegadinha provável: Dizer que o recurso apresentado a órgão incompetente implica perda definitiva do prazo recursal
```
Texto novo:
```text
- Pegadinha provável: Negar a devolução do prazo ao recorrente que interpôs o recurso perante órgão incompetente
```
**8l. G-114.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
[C4.4-21] Dizer que o recurso apresentado a órgão incompetente implica perda definitiva do prazo recursal
```
Texto novo:
```text
[C4.4-21] Negar a devolução do prazo ao recorrente que interpôs o recurso perante órgão incompetente
```

### Ajuste 9
Registro (motivo inexato da recusa parcial do C16). O texto do art. 217 está no Anexo N, e a divergência do inciso IV, c, foi dirimida pela Fonte 5 (alerta 6); a recusa por escopo continua válida.

**9a. Seção 0.1, linha C16 (motivo da recusa parcial).** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
Ficam fora os arts. 215 e 217: remissão a outra lei e redações de 2015 e 2019 que dependem de normas não abertas (ficha, seção 3.3, alerta 6).
```
Texto novo:
```text
Ficam fora o art. 215, que remete à Lei 10.887/2004, não aberta, e o art. 217, cujo texto está no Anexo N (inciso IV, alínea c, conferido pela Fonte 5; ficha, seção 3.3, alerta 6), por escolha de escopo, sem efeito sobre item.
```
**9b. C3.4-19, definição (mesmo motivo).** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
o art. 215 remete a outra lei, e o art. 217 traz redações de 2015 e de 2019 que dependem de normas não abertas ([SEM FONTE — não afirmar])
```
Texto novo:
```text
o art. 215 remete à Lei 10.887/2004, não aberta ([SEM FONTE — não afirmar]), e o art. 217, cujo texto está no Anexo N, fica fora por escolha de escopo
```

### Ajuste 10
Registro. As trocas de B32, B33 e B38 aparecem na coluna "como a banca troca" dos pares de recordação P-66 e P-69 (A19 e A23); o registro deve dizer isso para não parecer que a sugestão recusada entrou.

**10a. Seção 0.1, linha B32.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
| NÃO ACATADO | Ponto do D1 (art. 13, II: D1-38 a D1-43; ficha, seção 7). |
```
Texto novo:
```text
| NÃO ACATADO | Ponto do D1 (art. 13, II: D1-38 a D1-43; ficha, seção 7); sem pegadinha própria: a troca aparece só como recordação no par P-66 (A19). |
```
**10b. Seção 0.1, linha B33.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
| NÃO ACATADO | Ponto do D1 (art. 14, §§ 2º e 3º: D1-38 a D1-43). |
```
Texto novo:
```text
| NÃO ACATADO | Ponto do D1 (art. 14, §§ 2º e 3º: D1-38 a D1-43); sem pegadinha própria: a troca aparece só como recordação no par P-66 (A19). |
```
**10c. Seção 0.1, linha B38.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
| NÃO ACATADO | Ponto do D1 (art. 54, caput: D1-50). Os §§ 1º e 2º estão em C4.4-13. |
```
Texto novo:
```text
| NÃO ACATADO | Ponto do D1 (art. 54, caput: D1-50). Os §§ 1º e 2º estão em C4.4-13; a troca do caput aparece só como recordação no par P-69 (A23). |
```

### Ajuste 11
Forma. A seção 0 cita o enunciado do D2-30 com uma vírgula que o enunciado não tem.

**11. Seção 0, ponto 19 (citação do D2-30).** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
D2-30 "…, prazo obrigatório, e, por isso, não lhe é facultado declinar dele"
```
Texto novo:
```text
D2-30 "…, prazo obrigatório e, por isso, não lhe é facultado declinar dele"
```

### Ajuste 12
Opcional (forma; ficha 6.1). O campo do D2-13 descreve, na oração principal, a mesma proposição do ponto do D2-14 (fixado no R1); a proposição julgada no D2-13 é a exclusividade. Só o campo muda; enunciado, gabarito e [TS] ficam.

**12a. (Opcional) D2-13, ponto de julgamento, seção 5.2.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
- Ponto de julgamento: CF, art. 37, V — cargos em comissão são preenchidos por servidores de carreira nos casos, condições e percentuais previstos em lei (a exclusividade de servidores de cargo efetivo é das funções de confiança)
```
Texto novo:
```text
- Ponto de julgamento: CF, art. 37, V — a exclusividade de servidores ocupantes de cargo efetivo é das funções de confiança, e não dos cargos em comissão
```
**12b. (Opcional) D2-13, lista de pontos, seção 7.** Trecho atual (ocorre 1 vez no D2_v2.md):
```text
- D2-13: CF, art. 37, V — cargos em comissão são preenchidos por servidores de carreira nos casos, condições e percentuais previstos em lei (a exclusividade de servidores de cargo efetivo é das funções de confiança)
```
Texto novo:
```text
- D2-13: CF, art. 37, V — a exclusividade de servidores ocupantes de cargo efetivo é das funções de confiança, e não dos cargos em comissão
```

## 8. Tabela final dos 80 itens (ordem de apresentação)
| Item | Folha | Gab. | [TS] | Marca | Veredito R2 | Observação |
|---|---|---|---|---|---|---|
| D2-01 | 3.1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-02 | 3.1 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-03 | 3.1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-04 | 3.1 | C | sim (isca) | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-05 | 3.1 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-06 | 3.1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-07 | 3.1 | E | não | QA PENDENTE (R2) | APROVADO | ajuste 1 do R1 aplicado literalmente (enunciado, ponto, linha 2) |
| D2-08 | 3.1 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-09 | 3.1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-10 | 3.1 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-11 | 3.2 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-12 | 3.2 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-13 | 3.2 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido; ajuste opcional 12 (só o campo "ponto") |
| D2-14 | 3.2 | C | sim (isca) | QA PENDENTE (R2) | APROVADO | ajuste 2 aplicado literalmente; PAR → SIT; isca "mínimos" mantida |
| D2-15 | 3.2 | E | não | QA PENDENTE (R2) | APROVADO | ponto 19: conector "de modo que"; resto idêntico |
| D2-16 | 3.2 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-17 | 3.2 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-18 | 3.2 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-19 | 3.2 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-20 | 3.2 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-21 | 3.3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-22 | 3.3 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-23 | 3.3 | E | não | QA PENDENTE (R2) | APROVADO | ajuste 3 aplicado literalmente; um só erro |
| D2-24 | 3.3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-25 | 3.3 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-26 | 3.3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-27 | 3.3 | C | sim (isca) | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-28 | 3.3 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-29 | 3.3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-30 | 3.3 | E | não | QA PENDENTE (R2) | APROVADO | ponto 19: conector "e, por isso,"; resto idêntico |
| D2-31 | 3.4 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-32 | 3.4 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-33 | 3.4 | E | sim | QA PENDENTE (R2) | APROVADO | ajuste 4 aplicado literalmente (campo "troca") |
| D2-34 | 3.4 | C | não | QA PENDENTE (R2) | APROVADO | ajuste 5: "difere de BQ-0150" literal |
| D2-35 | 3.4 | C | sim (isca) | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-36 | 3.4 | E | sim | QA PENDENTE (R2) | APROVADO | ajuste 6: "difere de BQ-0125" literal |
| D2-37 | 3.4 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-38 | 3.4 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-39 | 3.4 | E | sim | QA PENDENTE (R2) | APROVADO | ajuste 7: "difere de BQ-0126" literal |
| D2-40 | 3.4 | E | não | QA PENDENTE (R2) | APROVADO | ponto 19: conector "o que significa que"; resto idêntico |
| D2-41 | 4.1 | C | não | QA PENDENTE (R2) | APROVADO | renumerado (era D2-44); conteúdo idêntico ao D2-44 da v1 |
| D2-42 | 4.1 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-43 | 4.1 | C | sim (isca) | QA PENDENTE (R2) | APROVADO | renumerado (era D2-41); conteúdo idêntico ao D2-41 da v1 |
| D2-44 | 4.1 | E | sim | QA PENDENTE (R2) | APROVADO | renumerado (era D2-43); conteúdo idêntico ao D2-43 da v1 |
| D2-45 | 4.1 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-46 | 4.1 | E | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-47 | 4.1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-48 | 4.1 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-49 | 4.1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-50 | 4.1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-51 | 4.2 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-52 | 4.2 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-53 | 4.2 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-54 | 4.2 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-55 | 4.2 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-56 | 4.2 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-57 | 4.2 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-58 | 4.2 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-59 | 4.2 | C | sim (isca) | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-60 | 4.2 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-61 | 4.3 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-62 | 4.3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-63 | 4.3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-64 | 4.3 | C | sim (isca) | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-65 | 4.3 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-66 | 4.3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-67 | 4.3 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-68 | 4.3 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-69 | 4.3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-70 | 4.3 | E | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-71 | 4.4 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-72 | 4.4 | C | sim (isca) | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-73 | 4.4 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-74 | 4.4 | C | não | QA PENDENTE (R2) | APROVADO | ajuste 8 aplicado literalmente (sujeito "interessado"; linha 2) |
| D2-75 | 4.4 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-76 | 4.4 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-77 | 4.4 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-78 | 4.4 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-79 | 4.4 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D2-80 | 4.4 | E | não | QA PENDENTE (R2) | APROVADO | ajuste 9 aplicado literalmente (linha 2, base, "difere de BQ-0132") |

Resumo da tabela: 80 APROVADOS.
- 65 idênticos à v1, com o veredito do R1 mantido.
- 9 com o ajuste do R1 aplicado literalmente.
- 3 com o conector variado (ponto 19).
- 3 renumerados, com conteúdo idêntico.

Reprovação: 0/80 = 0%. O único ajuste que toca campo de item é o opcional 12 (ponto do D2-13), e ele não muda enunciado, gabarito nem [TS].

## 9. Veredito final
Lote D2 v2: **APROVADO COM RESSALVAS no R2.** São 80/80 itens aprovados, com reprovação de 0%. Não há gate.

Pela QA, o aceite pode seguir à reconciliação da gcb-gerencia, com as seguintes condições:
- aplicar por errata (ou numa v2.1) os ajustes residuais obrigatórios 1 a 11 da seção "Ajustes residuais (texto exato)". Todos estão fora dos itens. Os ajustes 1 a 5 corrigem conteúdo de curso, e os demais são de cópia, de registro ou de forma. O ajuste 12 é opcional;
- decidir as pendências da seção 7: escopo do C3.3-10; registro para o D2-R e regra de montagem do ponto 19; ponto 22; regeração da leitura crítica; guarda dos scripts.

Notas à GBQ, para simulado (mantidas do R1 e da v2, com os ids da v2):
- D2-13 com D2-14 ou com D2-19;
- D2-63 com D2-70;
- D2-71 com D2-73;
- D2-25 com D2-27;
- D2-42 com D2-47;
- D2-45 com D2-55;
- D2-21 com D2-26;
- D2-06 com D2-31;
- D2-41, D2-43 e D2-49 entre si;
- regras (a) a (c) da moldura (D1 da GCB, seção 4).

Todo item segue "QA PENDENTE" no registro até o gatilho A aceito (D-QA-PENDENTE). Nada vai à plataforma nem à candidata.

GATE: não acionado (reprovação 0/80 = 0%, limite 30%).

FIM DO PARECER R2 — LOTE D2
