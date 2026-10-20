# D5_parecer_R2_gcb-cqfp.md — T-74 — 2026-10-20 — gerado por gcb-cqfp
PARECER R2 — LOTE D5 v2 (saida/gcb/D5_v2.md, gcb-cpp; SHA-256 4c61c5cf0c28aae533f8dc1510493e4db633f4423daabdea1c34c0cc1ea7d409; 313.079 bytes; LF; 1.747 linhas). Conferido contra o R1 (saida/gcb/D5_parecer_R1_gcb-cqfp.md, e34e66fa…0b40), a v1 (efcf3aba…4d2b, a mesma do R1), a leitura externa (saida/gcb/D5_leitura_critica.md, 29be8d3c…aaf3), a ficha (50260772…4a95) e o Anexo N (497af8e6…76eb), única base de texto legal. Modelo: saida/gcb/D1_parecer_R2_gcb-cqfp.md. Revisão; a gcb-cqfp não reescreve. Os textos da seção 9 são ajustes pontuais fixados. Scripts em python3 -I, no scratchpad; navegador não usado.

## 0. Resultado
- Itens: 70 (D5-01 a D5-53 e D5-55 a D5-71). **APROVADO 70; AJUSTE 0; REPROVADO 0. Reprovação no R2: 0/70 = 0%** (limite do gate: 30%). Não há gate. Não sobra item reprovado (ficha, seção 10, critério 8).
- Os 16 itens "QA PENDENTE (R2)" estão todos APROVADOS (seção 6). Os 54 demais são idênticos à v1 byte a byte e mantêm o veredito APROVADO do R1.
- Blocos: curso APROVADO COM AJUSTE (C10.1-12, uma frase; C10.5-07, uma pegadinha); resumo APROVADO (uma imprecisão de forma); pares APROVADO; pegadinhas APROVADO COM AJUSTE (G-68); proveniência APROVADO; contagens APROVADO; registro de acatamento da leitura externa APROVADO COM RESSALVAS (seção 5).
- **Veredito geral: APROVADO COM RESSALVAS.** Nenhuma ressalva toca item, gabarito, ponto de julgamento ou contagem. São 4 ajustes residuais de texto fora dos itens (seção 9, n. 1 a 4), com texto exato, e 1 opcional (n. 5). Podem ser aplicados por errata na reconciliação ou numa v2.1, sem nova rodada de QA sobre os itens.
- Ficam com a GCB: a divergência do ponto 20 (parecer técnico na seção 8), a regeração do arquivo de leitura crítica e do script (pontos 18 e 23), o arquivo de acatamento em separado (ponto 24) e o escopo dos blocos sem marca "Edital:" (seção 5.4).

## 1. Evidência e não regressão (por script)
1. **Não regressão dos itens.** Um script comparou campo a campo as duas versões: enunciado (5.1) e cada campo do gabarito comentado (5.2). Só mudaram os 16 itens declarados.
   - 8 por ajuste do R1: D5-03, 08, 22, 30, 43, 51, 59 e 65.
   - 1 por nota de mecanismo: D5-12.
   - 6 renumerados: D5-13, 15, 23, 25, 58 e 60.
   - 1 novo: D5-71. O D5-54 saiu.
   Os outros 54 itens são idênticos à v1 (enunciado, campos e marcas). A ordem do 5.1 é igual à do 5.2. Cada um dos 70 blocos tem todos os campos fixos da ficha (seção 2, item 5).
2. **Fora dos itens.** O diff linha a linha (v1 → v2) mostra só alterações declaradas:
   - seções 0 e 0.1 (novas) e nota de abertura do curso;
   - C10.2-02 (definição e pegadinha), C10.6-06 (título, definição, exemplo e pegadinha) e C10.7-05 (definição, exemplo e pegadinha);
   - 14 blocos novos;
   - resumo: as 7 linhas antigas são prefixo exato das novas, que só ganharam "Acrescentado na v2"; 2 linhas da tabela foram alteradas (art. 94; art. 96, § 3º) e 6 acrescentadas; nota de valores em reais com o § 7º;
   - pares: P-07, P-16 e P-17 a P-31;
   - pegadinhas: G-11, G-38, G-43 e G-45 a G-73;
   - proveniência, contagens e bloco à GCB.
   Nada além do declarado.
3. **Citações.** Um script (o mesmo critério do R1: artigo, parágrafo, inciso e alínea contra as linhas **vigentes** da seção 4 do Anexo N, excluídas as tachadas, as vetadas e o texto "[citado]") extraiu e conferiu as citações "art./arts." da v2.
   - Linhas novas ou alteradas (523 linhas): 706 citações, todas existentes e vigentes.
   - Arquivo inteiro: 1.308 citações, todas existentes e vigentes.
   - O script acusou 5 falhas nas linhas novas e 8 no arquivo inteiro. Conferidas uma a uma, são todas artefato de leitura, e nenhuma é erro: o pronome tomado por alínea ("art. 47, II, o condiciona"; "art. 6º, LIX, a define").
   - Validei o teste com citações falsas plantadas, e ele acusou todas: art. 158, § 5º; art. 14, VII; art. 79, parágrafo único; art. 102, parágrafo único, III; art. 94, § 4º (vetado); art. 20, § 3º (vetado).
   - Nenhum dispositivo com redação de 2025/2026 é usado. O art. 79 só aparece para dizer que não é usado; o art. 75, XVI, só no curso da v1, com REVERIFICAR. Os arts. 44-A, 87, 174 e 175 não são usados. VOLÁTIL = 0 e REVERIFICAR = 0 nos itens, como deve ser.
4. **Fonte oficial.** Reabri, em 20/10/2026, às 09:42 UTC, por curl com User-Agent de navegador, as quatro URLs da proveniência. São idênticas às do Anexo N, sem parâmetro.
   - Todas responderam HTTP 200, com bytes iguais aos do Anexo N: 649.705, 72.507, 22.251 e 14.239.
   - Os 315 dispositivos citados nas linhas novas ou alteradas aparecem literalmente na página da Lei 14.133 de hoje (comparação sem espaços em branco): 315/315.
   - O SHA-256 do HTML de hoje (3d747214…1d13) difere do registrado no Anexo N e do de 08:41 UTC. O tamanho e o texto são os mesmos; fica só o registro.
5. **Reais.** Nenhum "R$" nem "reais" nos 70 enunciados. Os valores de 2026 da leitura externa (B12) não aparecem em lugar nenhum da v2 (grep dos três valores: 0).

## 2. Conferência das respostas aos 24 pontos do R1
| Ponto R1 | Objeto | Resposta da v2 | Texto fixado entrou literal? | Veredito R2 |
|---|---|---|---|---|
| 1 | D5-03, linha 2 | Acolhido | Sim (script: igual ao texto 2.1, n. 1) | APROVADO |
| 2 | D5-08, "difere de BQ-0113" | Acolhido | Sim (campo literal; o item entra na lista "difere de") | APROVADO |
| 3 | D5-22 | Acolhido. "dar-se-á por repactuação"; o ponto e a linha 1 foram alinhados ao art. 92, § 4º, II, e ao art. 135, caput | Sim no enunciado. A base da v1 já trazia o art. 92, § 4º, II (conferido na v1); o pedido do R1 estava cumprido | APROVADO |
| 4 | D5-30 | Acolhido; ressalva completa do art. 137, § 3º, I | Sim (enunciado e linha 1, literais) | APROVADO |
| 5 | D5-43 | Acolhido | Sim (enunciado e ponto de julgamento literais); o D5-49 ficou com "caracterizada pelo planejamento" | APROVADO |
| 6 | D5-51 | Acolhido | Sim (enunciado e troca literais) | APROVADO |
| 7 | D5-59 | Acolhido | Sim (enunciado literal; base "art. 7º, caput, § 1º e § 2º; art. 117, caput", sem o § 3º) | APROVADO |
| 8 | D5-65 | Acolhido | Sim (enunciado e linha 2 literais) | APROVADO |
| 9 | D5-54 (reprovado) | Acolhido; D5-71 pela opção (b), art. 137, caput e II | Não se aplica (texto da produtora) | APROVADO (seção 4) |
| 10 | Contagens 10.6 e lote | Acolhido | Refeitas pela QA (seção 7) | APROVADO |
| 11 | 70 pontos de julgamento | Acolhido | A tabela da seção 7 da v2 confere com os 70 campos (script): 70 distintos, ordem e gabarito iguais; nenhum coincide com BQ-0113, 0134, 0135 ou 0142 | APROVADO |
| 12 | D5-12 em E6 | Acolhido | Mecanismo trocado; resto idêntico | APROVADO |
| 13 e 22 | Notas à GBQ | Acolhido como registro, com os ids da v2 (nenhum mudou). Acrescenta D5-13/15 e D5-23/25 | — | APROVADO |
| 14 | Projeto básico (C10.7-05, P-07, G-43) | Acolhido | Seção 3 | APROVADO |
| 15 | Resumo, art. 96, § 3º | Acolhido | Sim ("prazo mínimo de 1 mês, contado da homologação e anterior à assinatura") | APROVADO |
| 16 | C10.2-02 e G-11 | Acolhido | Sim; "quando exigidas" (art. 92, XII), separado de IX e X | APROVADO |
| 17 | P-16 | Acolhido | Sim; § 6º, I e II, fiéis ao Anexo N, inclusive "no desempenho da função administrativa" e "na forma de regulamento" | APROVADO |
| 18 | Regerar D5_para_leitura_critica.md | Não acolhido: é decisão da GCB, e a tarefa grava só a v2 | — | Motivo aceito; pendente da GCB |
| 19 | Sequência de gabaritos | Acolhido; três trocas C×E dentro de folha | Seção 7. O bloco de período 6 caiu de 26 para 13 itens. A afirmação de que nenhuma combinação de até três trocas reduz mais os períodos 5 a 8 é da produtora, é informativa e não foi refeita pela QA | APROVADO |
| 20 | Moldura do Legislativo | Não acolhido; divergência para a GCB. Só o D5-71 é neutro | Seção 8 (parecer técnico) | Pendente da GCB |
| 21 | Formatos | Acolhido | Conferido (seção 7) | APROVADO |
| 23 | Script da leitura crítica | Não acolhido: o script é da gcb-gerencia (ficha, seção 9) e depende do ponto 18 | — | Motivo aceito; pendente da GCB |
| 24 | Acatamento da leitura externa | Acolhido em parte. O registro está na seção 0.1 da v2, e não em saida/gcb/D5_acatamento_leitura_critica.md (o arquivo que a ficha, seção 9, nomeia) | — | Registro APROVADO COM RESSALVAS (seção 5); a GCB decide se aceita a seção 0.1 ou manda extrair o arquivo |

As contagens da seção 0 da v2 conferem: 24 pontos, com 20 acolhidos (13 e 22 "como registro"), 1 em parte (24) e 3 não acolhidos (18, 20 e 23). Também conferem as do registro: grupo A com 15 acatados e 2 não; grupo B com 24 e 3; grupo C com 10 (2 em parte) e 0.

## 3. Erro do projeto básico (art. 18, § 3º): corrigido em todo lugar
- Na v1, o erro estava em cinco trechos: C10.7-05 (definição: "o projeto básico, para obras e serviços de engenharia"; exemplo da reforma de auditório: "exige projeto básico, e não apenas TR"; pegadinha "usar TR para obra"), P-07 ("Projeto básico: obra ou serviço de engenharia") e G-43. A v2 alterou os cinco.
- Varredura da v2 (regex "projeto básico" a até 80 caracteres de "engenharia" ou "obra"; "TR para obra"; "auditório"; "não apenas TR"): nenhum trecho restringe o projeto básico a obras e serviços de engenharia nem nega o art. 18, § 3º. As ocorrências restantes são letra da lei: art. 14, I; art. 46, §§ 2º e 5º; art. 6º, XXV e XXVI; art. 18, § 3º; integrada × semi-integrada.
- O texto novo de C10.7-05, P-07, G-43 e da linha 10.7 do resumo segue a letra do art. 6º, XXV ("a obra ou o serviço") e do art. 18, § 3º (obras e serviços comuns de engenharia; especificação "apenas em termo de referência ou em projeto básico", se demonstrada a inexistência de prejuízo). C10.7-02 já transcrevia o § 3º corretamente.
- Nenhum item continha o erro. O D5-69 (anteprojeto × projeto executivo) está inalterado e correto.

## 4. D5-71 e itens renumerados
**D5-71 (novo; substitui o D5-54): APROVADO.**
- Ponto: art. 137, caput e II. Moldura verdadeira, com o texto do inciso II quase literal. Segmento falso: "razão pela qual a extinção dispensa o contraditório e a ampla defesa", que o caput expressamente assegura. Há um único erro; gabarito E seguro; E5 sem [TS], coerente com a convenção.
- Ponto distinto de todos os do lote: D5-30 (§ 2º, II, e § 3º, I), D5-25 (art. 104, II), D5-23 (art. 138, II) e D5-58 (art. 104, III). Distinto também dos quatro do Anexo R.
- Não toca o art. 117. A fronteira da ficha 5.2 fica preservada, e a ausência de "difere de" está correta.
- Aderência à 10.6: o art. 137, II, é complementar da 10.6 no Anexo N (seção 3), e era a opção (b) do R1.
- Moldura neutra ("Considere que, em contrato regido pela Lei nº 14.133/2021, …"), formato SIT; a 10.6 fica com 1 SIT.
- Estilo Cebraspe: afirmação única, sem "exceto"; o conector "razão pela qual" segue o padrão E5 (estilo_banca, 5.2).
- Curso C10.6-06 e G-38 ajustados à mesma base (art. 137, caput e II), conferidos.

**Renumerados (13 ↔ 15, 23 ↔ 25, 58 ↔ 60): APROVADOS.** Por script, o item com o id novo tem o mesmo conteúdo do item com o id antigo na v1:
- enunciado no 5.1;
- folha, ponto de julgamento, formato, gabarito, as duas linhas da justificativa, base, mecanismo e troca no 5.2.
Mudaram só o cabeçalho e a marca ("QA PENDENTE (R2)"), e entrou o campo "Alteração na v2". Enunciado, gabarito e justificativa acompanharam o id nas duas formas. O mapa da seção 8 da v2 está correto:
- D5-13 = garantia até 5%, "vedada a majoração" (E, [TS]); D5-15 = o contratado escolhe a modalidade (C);
- D5-23 = extinção consensual, isca "desde que haja interesse da Administração" (C, [TS]); D5-25 = extinção unilateral "mesmo fora dos casos" (E, [TS]);
- D5-58 = prerrogativa de fiscalizar atribuída ao contratado (E, [TS]); D5-60 = segregação de funções, art. 7º, § 1º, literal com a finalidade (C).
As referências a esses ids fora dos itens (seções 0, 0.1, 7 e 8) estão corretas, com uma exceção documental no bloco à GCB (seção 9, n. 3).

## 5. Registro de acatamento da leitura externa (seção 0.1 da v2) e tudo o que ele mudou
### 5.1 Acatamentos (49 decisões de acatar: 15 do grupo A, 24 do B e 10 do C, entre elas C1 e C2 "em parte")
Todo acatamento tem lastro literal e vigente no Anexo N, e os artigos que o registro cita estão certos. Conferi a letra de cada dispositivo contra a seção 4 do Anexo N:
- arts. 6º, XIII, XIV, XV, XVII, XXXII, XXXIII e XLIII; 14; 23; 24; 28; 29; 33; 34; 44; 46; 47;
- 74, II, III, V e §§ 2º, 3º e 5º; 75, III e §§ 1º, 2º, 3º e 7º; 78;
- 90, §§ 2º a 7º; 94; 95; 99; 102; 111; 116; 118; 121, §§ 3º e 4º; 122; 124, II, d; 131; 132; 136;
- 140, § 4º; 141; 143; 145; 156, § 6º; 157; 158; 163; 18, § 1º, V e X; 117, § 2º.

Também estão certas as afirmações sobre as marcas do Anexo N: art. 14 é compl. da 10.1; arts. 157, 158 e 163, compl. da 10.2; arts. 141, 143 e 145, compl. da 10.4; art. 23, compl. da 10.5; art. 44, compl. da 10.7; arts. 90, 94 e 95, núcleo da 10.4; arts. 99 e 102, compl. da 10.3. As correções e os acréscimos de artigo que o registro declara também se sustentam:
- A6: as "propostas válidas" estão na alínea a, junto com a ausência de interessados;
- A10: art. 131, parágrafo único;
- A15: art. 46, §§ 2º e 5º;
- C5: art. 99.

Uma imprecisão: A7 e C10.1-12 dizem que o art. 79 "tem redação de 2025". Pelo Anexo N, o caput e os incisos I a III estão na redação original. Têm redação de 2025, com REVERIFICAR, só o inciso IV, o § 1º (caput e inciso VII, com as alíneas) e o § 2º. A decisão de não usar o artigo continua correta, porque ele está fora dos núcleos e os procedimentos auxiliares ficam só no curso (ficha, seção 8). Ajuste na seção 9, n. 1.

### 5.2 Recusas (A5, A8, B8, B10, B12; C1 e C2 em parte): justificadas
- **A5 e o art. 56 de C1 (modo de disputa).** O art. 56 está no Capítulo IV ("Da apresentação de propostas e lances", arts. 55 a 58), sem marca "Edital:". O "modo de disputa" como parâmetro da fase preparatória já está em C10.5-03 (art. 18, VIII). A recusa tem coerência com a ficha, seção 8. Os arts. 33 e 34 foram acatados por servirem à 10.1 pelas definições de concorrência e pregão (art. 6º, XXXVIII e XLI), o que é distinção legítima.
- **A8 e B10 (garantia de proposta, art. 58).** Mesmo Capítulo IV, sem marca. A garantia contratual já está coberta (C10.2-03, P-15, G-12, D5-13 e D5-15).
- **B8 (Sicx).** A base é o art. 79, IV, e § 1º, VII, com redação de 2025 e REVERIFICAR. O art. 28, § 2º, já está em G-05.
- **B12 (valores de 2026).** Decretos de atualização NÃO CONFERIDOS no Anexo N (seções 7 e 8), e a ficha 6.6 veda valor em reais em item. Nenhum valor foi reproduzido.
- **C2, art. 79.** Mesma razão do B8, com a imprecisão do n. 1.

### 5.3 Os 14 blocos novos de curso, os pares P-17 a P-31 e as pegadinhas G-45 a G-73
- **Blocos novos: APROVADOS pela letra do Anexo N.** São 14, todos com "acréscimo da v2 (QA PENDENTE (R2))" no título: C10.1-10 a 14; C10.2-08; C10.3-06; C10.4-06 a 09; C10.5-07; C10.6-07; C10.7-07.
  - Li cada definição contra o texto do dispositivo. Números e prazos são literais: 5% do capital e 5 anos (art. 14); 3 fornecedores, 6 meses e 1 ano (art. 23); 3 dias úteis (art. 75, § 3º); 30% (art. 99); 15 dias úteis, 2 ou mais servidores estáveis, 3 anos de serviço e 5 anos de prescrição (arts. 157 e 158); 1 e 3 anos (art. 163, III); 20 e 10 dias úteis (art. 94).
  - A ordem dos incisos também está certa: art. 33, I a VI; art. 46, I a VII; art. 78, I a V; art. 141, § 1º, I a V; art. 163, I a V. Os verbos de comando seguem a lei: "preferencialmente" (art. 75, § 3º; art. 158, § 1º); "poderá" (art. 121, § 3º; art. 34, § 1º); "exclusivamente" (art. 141, § 1º); "somente" (art. 145, § 1º).
  - Exceções:
    - C10.1-12: frase do art. 79 (seção 9, n. 1).
    - C10.5-07: primeira pegadinha (seção 9, n. 2).
  - Os exemplos são hipotéticos e dizem que o são, sem afirmação sobre a Câmara real. Os rótulos doutrinários ("deserta", "fracassada") ficam só como rótulo, ao lado do art. 75, III, a e b.
- **Pares P-17 a P-31: APROVADOS.** As 15 diferenças e bases conferem com o Anexo N.
  - Em "como a banca troca", cada troca é falsa pela letra: o pregão com técnica e preço (P-18); os custos indiretos obrigatórios, que o § 1º do art. 34 só admite (P-20); o pedido de restabelecimento "a qualquer tempo", contra o art. 131, parágrafo único (P-24); o projeto básico na semi-integrada a cargo do contratado (P-29); o contrato de urgência sem publicação (P-31).
  - No P-28, "aplica ao parcelamento de serviços as exceções do art. 40, § 3º" é troca válida: o § 3º é da subseção de compras, e o art. 47 não o reproduz.
  - Com a leitura externa, o maior trecho comum por par é de 3 a 10 palavras, quase sempre letra da lei. Não há cópia.
- **Pegadinhas G-45 a G-73: APROVADAS, com um ajuste.**
  - São 29, cada uma com o dispositivo que a desfaz. As 24 vindas do grupo B correspondem às sugestões indicadas no registro (mapa conferido); as 5 restantes (G-45, 47, 56, 57 e 70) vêm dos grupos A e C ou do próprio bloco.
  - O texto de cada G é o mesmo da pegadinha do bloco correspondente.
  - Ajuste: **G-68** (e a mesma frase em C10.5-07) reproduz quase literalmente a sugestão B9 do leitor externo (razão de semelhança 0,85; trecho comum de 12 palavras que não é letra da lei). A ficha, seção 9, diz "texto do leitor não é copiado". Texto exato na seção 9, n. 2.
  - Nas demais G vindas do grupo B, a semelhança fica entre 0,24 e 0,77. Os trechos comuns mais longos são letra da lei (art. 74, § 3º; art. 18, § 1º, X) ou só estrutura de frase (G-51 e G-64, trechos de 8 e 9 palavras), paráfrase aceitável.

### 5.4 Escopo (pendente (c) da seção 0 da v2 e (b) da seção 8)
Os blocos sem marca "Edital:" estão permitidos pela ficha. Seção 8: "fase de julgamento, habilitação, instrumentos auxiliares e PNCP só no curso, se servirem a uma folha, e sem item próprio". Seção 9: artigo "presente e vigente no Anexo N". Não geram item.

A lista de dispositivos sem marca está incompleta: faltam o art. 6º, XIII e XIV (C10.1-10 e P-17), o art. 6º, XV e XVII (P-23) e o art. 6º, XLIII (C10.1-12 e P-22). Completar a lista é documental (seção 9, n. 4). Retirar esses blocos ou mantê-los é decisão da GCB, sem efeito sobre os itens.

## 6. Itens "QA PENDENTE (R2)": veredito item a item (16)
| Item | Folha | Gab. | Objeto do R2 | Veredito |
|---|---|---|---|---|
| D5-03 | 10.1 | E | Linha 2 fixada; [TS] (segurança jurídica → finalidade), troca única | APROVADO |
| D5-08 | 10.1 | E | "Difere de BQ-0113" pertinente (art. 72, VI × art. 74, I e § 1º); E5 sem [TS] | APROVADO |
| D5-12 | 10.2 | E | E6 ("em qualquer hipótese" × art. 92, IX, "quando for o caso"); [TS] mantido | APROVADO |
| D5-13 | 10.2 | E | Renumerado; art. 98, "autorizada a majoração" → "vedada" | APROVADO |
| D5-15 | 10.2 | C | Renumerado; art. 96, § 1º | APROVADO |
| D5-22 | 10.3 | C | "dar-se-á", conforme o art. 92, § 4º, II ("será por") e o art. 135; resposta única | APROVADO |
| D5-23 | 10.3 | C | Renumerado; art. 138, II, isca literal | APROVADO |
| D5-25 | 10.3 | E | Renumerado; art. 104, II, "nos casos especificados" suprimido | APROVADO |
| D5-30 | 10.3 | C | Ressalva completa do art. 137, § 3º, I; não há mais leitura parcial | APROVADO |
| D5-43 | 10.5 | C | Art. 18, caput, sem "caracterizada pelo planejamento"; separado do D5-49 | APROVADO |
| D5-51 | 10.6 | E | "alcança somente até o segundo grau" × art. 7º, III ("até o terceiro grau"); gabarito E inequívoco | APROVADO |
| D5-71 | 10.6 | E | Seção 4 | APROVADO |
| D5-58 | 10.6 | E | Renumerado; art. 104, III, Administração → contratado | APROVADO |
| D5-59 | 10.6 | C | Ancorado no fiscal (art. 117, caput, e art. 7º, § 2º); não entrega o D5-56 | APROVADO |
| D5-60 | 10.6 | C | Renumerado; art. 7º, § 1º, literal | APROVADO |
| D5-65 | 10.7 | C | Incisos VI e XIII, obrigatórios pelo § 2º; C6 ("entre os elementos… estão"); "difere de BQ-0142" pertinente | APROVADO |

## 7. Contagens e sequência de gabaritos (refeitas por script sobre a v2)
- 70 itens; 10 por folha; C = 5 em cada folha (35/35, 50%); [TS] = 5 por folha (4 E e 1 C com elemento-isca registrado), 35 no lote. Nenhum [TS] sem campo "troca".
- Iscas: D5-10, 18, 23, 36, 42, 52 e 68.
- Formatos (D/S/Si/N/P/A), com teto de 3 respeitado e APL rotulado ≤ 2 por folha:
  - 10.1: 3/0/2/1/2/2;
  - 10.2: 3/2/1/2/1/1;
  - 10.3: 3/0/1/3/1/2;
  - 10.4: 3/1/2/1/1/2;
  - 10.5: 3/1/2/0/2/2;
  - 10.6: 3/2/1/1/1/2;
  - 10.7: 3/0/2/0/3/2.
  Todos iguais aos da v2.
- "QA PENDENTE (R2)" = 16 (2/3/4/0/1/5/1 por folha), igual ao declarado; cabeçalho e marca coerentes nos 70. VOLÁTIL 0; REVERIFICAR 0. A tabela de moldura da v2 (22 enunciados: 13 APL e 9 SIT) confere item a item.
- Sequência do lote, na ordem de apresentação: CEECCECEECCEEECCECCEECCCEEECECCEECECCECEECCECCEECEECCECEEECCCEECCECCEE (igual à declarada).
  - Maior corrida 3; maior alternância 4.
  - Maior bloco repetido de período 2: 4 itens; de período 3: 7; de período 4: 7. Nenhum chega a 8: **APROVADO** (ficha 6.4), por folha e no lote.
  - Períodos 5 a 8 (informativo), iguais aos declarados: 10 itens (D5-08 a 17), 13 (D5-26 a 38), 11 (D5-13 a 23) e 13 (D5-09 a 21).
- Sequência de [TS]: igual à declarada. Corrida 3; alternância 4; períodos 2 a 4 com no máximo 7 itens: **APROVADO**.
- O ponto 19 do R1 ficou atendido: o bloco "CEECEC" de 26 itens caiu para 13. Um bloco de período 6 com 13 itens equivale a pouco mais de duas repetições e não é padrão perceptível na prova. Não peço nova troca.

## 8. Ponto 20 — moldura "Considere que um órgão do Poder Legislativo da União…": parecer técnico (a decisão é da GCB)
1. **Pela letra da ficha, a leitura (ii) tem apoio.** A seção 4 define o contexto pela própria moldura ("o exemplo é hipotético e diz que é ('considere que um órgão do Poder Legislativo da União…')"), e a 6.3 diz que "aplicação parlamentar exige o contexto da seção 4 e no máximo 2 por folha". Lidos juntos, os 9 SIT com a moldura (D5-08, 09, 14, 28, 37, 40, 47, 68 e 70) têm o contexto da seção 4. Por essa leitura, ficam acima de 2 as folhas 10.1 (4), 10.3 (3), 10.4 (4), 10.5 (3) e 10.7 (4).
2. **Pela finalidade, a leitura (i) também se sustenta.** O teto é de formato, e a candidata não vê o rótulo; vê a moldura. Nos 9 SIT, o gabarito não depende do Legislativo: a moldura é cenário, e o ponto de julgamento é o dispositivo. Nos APL, o contexto é parte do julgamento (por exemplo, D5-01, art. 1º, I).
3. **O dado que pesa mais é o gabarito associado à moldura, e ele desaconselha a opção (ii) tal como formulada.**
   - Os 22 enunciados com a moldura têm 15 C e 7 E (68% de C, contra 50% no lote).
   - Os 13 APL têm 12 C e 1 E (só o D5-06).
   - Os 9 SIT com moldura têm 3 C e 6 E.
   - Neutralizar os 8 SIT necessários para ficar com ≤ 2 por folha (D5-08, 09, 28, 37, 40, 47, 68 e 70; o D5-14 fica) tiraria da moldura 6 E e 2 C. Ela passaria a 12 C e 2 E (86% de C), um marcador visível que coincide com o gabarito. É isso que o estilo_banca, 5.1, manda evitar ("não deixe o marcador coincidir sempre com o mesmo gabarito"). Hoje, a moldura já tem viés de C; com a opção (ii), o viés fica forte.
4. **Alternativas que a GCB pode considerar, sem efeito no veredito deste R2:**
   - (i) aceitar que SIT com moldura não conta como APL, com errata na ficha ("APL = rótulo; a moldura em SIT é cenário") e nota à GBQ para não concentrar itens com a moldura no mesmo simulado;
   - (ii) neutralizar SIT, mas preferindo os C (D5-28, 37 e 68) e mantendo SIT E com moldura, para não agravar o viés. Essa opção não basta sozinha para o teto de 2 nas folhas 10.1 e 10.4;
   - (iii) qualquer opção acompanhada de rever 2 ou 3 APL C, para trazer o APL para perto de 50%. Isso mexe em itens aprovados e exige nova rodada de QA sobre eles.
   A neutralização, se houver, é troca só da moldura ("Considere que, em contrato regido pela Lei nº 14.133/2021, …"), sem mudar gabarito, ponto de julgamento ou [TS]. Pede conferência leve (enunciado contra a v2), não um R3 completo.
5. A QA não decide. Pelo critério técnico de imprevisibilidade do gabarito, a ordem de preferência é (i) ou (iii), e depois (ii) na forma "neutralizar os C". A opção (ii) na forma "neutralizar os SIT que excedem" é a menos indicada.

## 9. Ajustes residuais (texto exato; fora dos itens; não reprovam nada)
1. **C10.1-12 (curso), definição, última frase.**
   - Substituir "O art. 79, que trata das hipóteses de uso do credenciamento, tem redação de 2025 (Lei 15.266/2025) e está marcado REVERIFICAR no Anexo N: não é usado neste lote."
   - por "O art. 79, que trata das hipóteses de uso do credenciamento, tem o inciso IV, o § 1º (caput e inciso VII, com as alíneas) e o § 2º com redação dada ou incluída pela Lei 15.266/2025, marcados REVERIFICAR no Anexo N; o artigo não é usado neste lote."
   - Na seção 0.1, linha A7, substituir "O art. 79 (redação de 2025, REVERIFICAR no Anexo N, fora dos núcleos) foi retirado da base e não é usado." por "O art. 79 (inciso IV e §§ 1º e 2º com redação de 2025, REVERIFICAR no Anexo N; artigo fora dos núcleos) foi retirado da base e não é usado."
2. **C10.5-07 (pegadinha provável) e G-68.** A frase ocorre 2 vezes no arquivo; substituir nas duas.
   - Substituir "Afirmar que o sigilo do orçamento estimado pode ser imposto sem justificativa, que prevalece perante os órgãos de controle interno e externo ou que o preço estimado ou o máximo aceitável pode ser omitido do edital quando o julgamento for por maior desconto"
   - por "Dar caráter sigiloso ao orçamento estimado sem justificativa, opor o sigilo aos órgãos de controle interno e externo ou deixar fora do edital, na licitação por maior desconto, o preço estimado ou o máximo aceitável".
   - O dispositivo não muda (art. 24, caput, I e parágrafo único).
3. **Seção 8 da v2 (bloco à GCB), "Fronteira do art. 117".** Substituir "(requisitos e segregação, D5-51, D5-52, D5-58, D5-59)" por "(requisitos e segregação, D5-51, D5-52, D5-59, D5-60)". Depois da renumeração, o D5-58 é o da prerrogativa (art. 104, III), e a segregação passou ao D5-60.
4. **Seções 0 (pendente (c)) e 8 (pendente (b)) da v2.** A frase ocorre 2 vezes; substituir nas duas.
   - Substituir "C10.1-10 (arts. 33, 34 e 24, parágrafo único), C10.1-12 (art. 78),"
   - por "C10.1-10 (art. 6º, XIII e XIV; arts. 33, 34 e 24, parágrafo único), C10.1-12 (art. 78; art. 6º, XLIII), pares P-17 (art. 6º, XIII e XIV), P-22 (art. 6º, XLIII) e P-23 (art. 6º, XV e XVII),".
5. **(Opcional, forma) Resumo, linha 10.6.** Substituir "(art. 117, § 2º; só no curso e nos pares)" por "(art. 117, § 2º; só no curso, no par P-27 e na pegadinha G-71, sem item)".

Se aplicados por errata, a QA confere só os trechos acima (diff), sem nova rodada sobre os itens.

## 10. Tabela final dos 70 itens (ordem de apresentação; posição 54 = D5-71)
| Item | Folha | Gab. | [TS] | Marca | Veredito R2 | Observação |
|---|---|---|---|---|---|---|
| D5-01 | 10.1 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-02 | 10.1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-03 | 10.1 | E | sim | QA PENDENTE (R2) | APROVADO | ajuste 1 do R1 aplicado literalmente (linha 2) |
| D5-04 | 10.1 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-05 | 10.1 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-06 | 10.1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-07 | 10.1 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-08 | 10.1 | E | não | QA PENDENTE (R2) | APROVADO | ajuste 2 aplicado literalmente ("difere de BQ-0113") |
| D5-09 | 10.1 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-10 | 10.1 | C | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-11 | 10.2 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-12 | 10.2 | E | sim | QA PENDENTE (R2) | APROVADO | nota 12 do R1: mecanismo E6; resto idêntico |
| D5-13 | 10.2 | E | sim | QA PENDENTE (R2) | APROVADO | renumerado (era D5-15); conteúdo idêntico ao D5-15 da v1 |
| D5-14 | 10.2 | E | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-15 | 10.2 | C | não | QA PENDENTE (R2) | APROVADO | renumerado (era D5-13); conteúdo idêntico ao D5-13 da v1 |
| D5-16 | 10.2 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-17 | 10.2 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-18 | 10.2 | C | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-19 | 10.2 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-20 | 10.2 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-21 | 10.3 | E | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-22 | 10.3 | C | não | QA PENDENTE (R2) | APROVADO | ajuste 3 aplicado ("dar-se-á"); base já tinha o art. 92, § 4º, II |
| D5-23 | 10.3 | C | sim | QA PENDENTE (R2) | APROVADO | renumerado (era D5-25); conteúdo idêntico ao D5-25 da v1 |
| D5-24 | 10.3 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-25 | 10.3 | E | sim | QA PENDENTE (R2) | APROVADO | renumerado (era D5-23); conteúdo idêntico ao D5-23 da v1 |
| D5-26 | 10.3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-27 | 10.3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-28 | 10.3 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-29 | 10.3 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-30 | 10.3 | C | não | QA PENDENTE (R2) | APROVADO | ajuste 4 aplicado literalmente (enunciado e linha 1) |
| D5-31 | 10.4 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-32 | 10.4 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-33 | 10.4 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-34 | 10.4 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-35 | 10.4 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-36 | 10.4 | C | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-37 | 10.4 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-38 | 10.4 | E | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-39 | 10.4 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-40 | 10.4 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-41 | 10.5 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-42 | 10.5 | C | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-43 | 10.5 | C | não | QA PENDENTE (R2) | APROVADO | ajuste 5 aplicado literalmente (enunciado e ponto) |
| D5-44 | 10.5 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-45 | 10.5 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-46 | 10.5 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-47 | 10.5 | E | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-48 | 10.5 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-49 | 10.5 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-50 | 10.5 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-51 | 10.6 | E | sim | QA PENDENTE (R2) | APROVADO | ajuste 6 aplicado literalmente (enunciado e troca) |
| D5-52 | 10.6 | C | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-53 | 10.6 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-71 | 10.6 | E | não | QA PENDENTE (R2) | APROVADO | novo (substitui o D5-54, reprovado no R1); art. 137, caput e II; E5 |
| D5-55 | 10.6 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-56 | 10.6 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-57 | 10.6 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-58 | 10.6 | E | sim | QA PENDENTE (R2) | APROVADO | renumerado (era D5-60); conteúdo idêntico ao D5-60 da v1 |
| D5-59 | 10.6 | C | não | QA PENDENTE (R2) | APROVADO | ajuste 7 aplicado literalmente (enunciado e base) |
| D5-60 | 10.6 | C | não | QA PENDENTE (R2) | APROVADO | renumerado (era D5-58); conteúdo idêntico ao D5-58 da v1 |
| D5-61 | 10.7 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-62 | 10.7 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-63 | 10.7 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-64 | 10.7 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-65 | 10.7 | C | não | QA PENDENTE (R2) | APROVADO | ajuste 8 aplicado literalmente (enunciado e linha 2) |
| D5-66 | 10.7 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-67 | 10.7 | C | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-68 | 10.7 | C | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-69 | 10.7 | E | sim | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |
| D5-70 | 10.7 | E | não | QA PENDENTE | APROVADO | idêntico à v1 (script); veredito do R1 mantido |

Resumo da tabela: 70 APROVADOS (54 idênticos à v1; 8 com o ajuste do R1 aplicado literalmente; 1 com nota de mecanismo; 6 renumerados com conteúdo idêntico; 1 novo). Reprovação: 0/70 = 0%.

## 11. Veredito final
Lote D5 v2: **APROVADO COM RESSALVAS no R2.** São 70/70 itens aprovados, com reprovação de 0%. Não há gate.

Pela QA, o aceite pode seguir à reconciliação da gcb-gerencia, com as seguintes condições:
- aplicar ou registrar por errata os ajustes 1 a 4 da seção 9, que estão fora dos itens (o 5 é opcional);
- decidir a divergência do ponto 20 (parecer técnico na seção 8);
- decidir os pendentes: regeração do arquivo de leitura crítica e do script (pontos 18 e 23), arquivo de acatamento em separado (ponto 24) e escopo dos blocos sem marca "Edital:" (seção 5.4).

Notas à GBQ, para simulado, mantidas do R1 e da v2:
- D5-61 com D5-62 ou D5-70;
- D5-39 com D5-57;
- D5-24 com D5-26;
- D5-66 com D5-67;
- D5-43 com D5-49;
- D5-13 com D5-15;
- D5-23 com D5-25.

Todo item segue "QA PENDENTE" no registro até o gatilho A aceito (D-QA-PENDENTE). Nada vai à plataforma nem à candidata.

GATE: não acionado (reprovação 0/70 = 0%, limite 30%).

FIM DO PARECER R2 — LOTE D5
