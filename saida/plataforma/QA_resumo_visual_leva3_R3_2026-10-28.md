# QA R3 — Resumo visual de Direito Administrativo, leva 3 (verificação pontual B1, B2, C1, C2, S1)

- Data: 28/10/2026
- Revisor: QA (Opus). Não produziu nenhum dos artefatos revisados e não editou nenhum arquivo em /home/claude/v17_3/. Este relatório é o único arquivo criado.
- Escopo: verificação pontual das correções pedidas no R2 (B1, B2, C1, C2) e da sugestão S1, em P1-DA-7. Os tópicos 8 e 9 já estavam aprovados desde o R1 e não foram reabertos.

## 1. Insumos (SHA-256)

| Arquivo | Hash |
|---|---|
| resumo_visual_leva3.json (R3) | 6ec85505dbd8096a29d744e5f751b6e6292aed54e91de84a53413bff732b8646 |
| resumo_visual_leva3.py | eae7c92e… |
| pacote_previa_v114_rv3.json | 0807ebb0… |
| plataforma_v17_3_previa_leva3.html | bed3bae0… (3.364.008 bytes) |
| TRIAGEM leva 3 | f8bd5da9… |
| template da plataforma | 11b99a41… (inalterado) |
| checa_resumo_visual.py v1.2 | 43ed8198… (inalterado) |

## 2. Testes rodados (só leitura, cópias de scripts no scratchpad)

| Teste | Resultado |
|---|---|
| Diff R2→R3 do JSON | Mudaram só P1-DA-7: texto do § 8º (B1), box do art. 21 (B2), fluxo [2] indisponibilidade (C1), fluxo [4] § 10-F (S1) e fontes (C2). Nenhum outro tópico mudou. |
| checa_resumo_visual.py v1.2 `--pacote` (leva 3, pacote rv3, 30 tópicos) | 0 erros / 0 avisos |
| regr_v17_3.js | 104/110 telas; 30 RV; 10 diferenças esperadas; 0 não esperadas; 0 erros JS |
| t_janela20.js | 0 falhas |
| Integridade da prévia | prévia = template + pacote embutido; meta "…levas 1 a 3 (prévia, QA R3)"; levas 1–3 íntegras; restante do pacote idêntico ao rv2 |

## 3. Conferência contra as certidões de julgamento do STF

Os portais foram lidos em 28/10/2026 (fonte: portal.stf.jus.br, abas Andamentos e Decisões das ADIs 7.156 e 7.236). As transcrições literais estão na seção 6.

| Item | Bloco (P1-DA-7) | Texto R3 | Certidão | Resultado |
|---|---|---|---|---|
| B1 | texto, § 8º | "divergência interpretativa da lei baseada em jurisprudência assentada no STF ou nos tribunais superiores ou, na falta dela, em decisão de mérito transitada em julgado de órgão colegiado de 2º grau, salvo dolo ou erro grosseiro (§ 8º, com a interpretação conforme fixada pelo STF nas ADIs 7.156 e 7.236, 2026)" | 6(b) (A)(i) e 6(c) | CONFERE. "Assentada" e "decisão de mérito transitada em julgado… órgão colegiado de 2º Grau" são literais. A ressalva "dolo ou erro grosseiro" está na certidão. O erro do R2 ("não pacificado") foi removido. |
| B2 | box, art. 21 § 4º | Só a decisão criminal transitada em julgado com as excludentes do CPP art. 65, a prova da inexistência do fato (art. 386, I) ou a prova de não concorrência (art. 386, IV) impede a ação; vale também para a rejeição da denúncia e o arquivamento precluso | 6(e) | CONFERE. As três hipóteses, a exigência de trânsito em julgado e a extensão à rejeição da denúncia e ao arquivamento precluso são literais. A palavra "prova" corrige o R2, porque a certidão diz "estar provada" e "estar provado". A ressalva do art. 18 do CPP não aparece no box. É uma omissão aceitável em um resumo, porque não torna a afirmação errada (ver S2). |
| C1 | fluxo [2], art. 16 | "em caráter excepcional e por decisão fundamentada, cabe com base em tutela de evidência ou com presunção de urgência; alcança o ressarcimento, a multa civil e o enriquecimento ilícito (STF, ADI 7.156)" | 6(d) (iii) | CONFERE. Cita a excepcionalidade e a fundamentação; a tutela de evidência e a presunção de urgência; e o alcance sobre multa civil e enriquecimento ilícito. As expressões declaradas inconstitucionais ("apenas", "não podendo a urgência ser presumida", "sem incidir… multa civil") não aparecem mais. A citação só da ADI 7.156 está correta, porque o item (iii) está na certidão de 24/6 da ADI 7.156. |
| C2 | fontes | Certidões das sessões de 28/5, 24/6, 25/6 e 1º/7/2026; atas no DJE de 2/7 e 4/8/2026; acórdão pendente | Andamentos da ADI 7.236 | CONFERE quanto às datas, mas há a observação O1 abaixo. |
| S1 | fluxo [4], art. 17 | "afastando os §§ 10-C, 10-D e 10-F, I" | 6(d) (ii) | CONFERE. Só o inciso I do § 10-F foi declarado inconstitucional. |

Os itens N1 a N8 do R1, já aceitos no R2, continuam no texto R3 sem alteração. Foram conferidos de novo contra as certidões:

| N | Assunto | Certidão |
|---|---|---|
| N1 | art. 23, § 5º: inconstitucional a "metade do prazo"; prescrição intercorrente com prazo máximo de 20 anos | 6(a) |
| N2 | art. 12, § 10, inconstitucional | 6(d) (ii) |
| N3 | art. 16, indisponibilidade (igual a C1) | 6(d) (iii) |
| N4 | art. 12, § 1º (perda da função como poder-dever, extensão aos demais vínculos) e § 4º inconstitucional | 6(d) (i); 6(b) (B)(iv); 6(c) (B)(ii) |
| N5 | art. 17, §§ 10-C, 10-D e 10-F, I, e art. 17-B, § 3º, inconstitucionais | 6(d) (ii) |
| N6 | art. 21, § 4º (igual a B2) | 6(e) |
| N7 | art. 17-C, § 2º: sem solidariedade para sanção, ressalvada a responsabilidade patrimonial | 6(d) (v) |
| N8 | art. 3º, § 1º: inconstitucional a expressão "e benefícios diretos", com efeitos ex tunc e ressalva da coisa julgada | 6(b) (B)(i) |
| relâmpago [8] | art. 11, caput, constitucional, com a revogação dos incisos I e II | 6(b) (B)(ii); 6(c) (B)(i) |

## 4. Achados

### O1 — CORRIGIR (de forma, sem nova rodada). Classe P, tópico P1-DA-7, bloco "fontes"

- Texto atual: "…lidas no portal do STF pelo QA em 28/10/2026…"
- Problema: o trecho mostra à candidata um jargão interno do processo ("pelo QA"). É a mesma família de defeito do achado D6 da leva 2, que já foi corrigido.
- Redação proposta: "…certidões de julgamento das sessões de 28/5, 24/6, 25/6 e 1º/7/2026 (atas no DJE de 2/7 e 4/8/2026), lidas no portal do STF em 28/10/2026, e notícias oficiais das mesmas datas; acórdão pendente de publicação e leitura".
- Não afeta o direito. Pode ser aplicada pela produção e confirmada por diff e checa, sem nova revisão de mérito.

### S2 — SUGESTÃO (opcional). Classe N, tópico P1-DA-7, box do art. 21

- Pode-se acrescentar ao fim do box: "…ressalvado o art. 18 do CPP (novas provas)". Isso reproduziria a certidão de forma integral.
- Não é obrigatório. Sem esse trecho, o box não fica errado.
- Classificação: BACKLOG.

Não há BLOQUEIA nem outro CORRIGIR.

## 5. Veredito

**APROVADO, com a ressalva O1.**

- P1-DA-7: B1, B2, C1 e C2 foram resolvidos e S1 foi aplicada. Todo o conteúdo normativo confere com as certidões de julgamento do STF.
- O1 é uma correção só de redação na lista de fontes, que a produção aplica e confirma por diff e checa.
- Os tópicos 8 e 9 continuam aprovados.

O que mudar: apenas O1. S2 é opcional e fica em BACKLOG.

## 6. Evidência: transcrição literal das certidões de julgamento

- Fonte oficial: Supremo Tribunal Federal, portal de processos.
  - ADI 7.236: https://portal.stf.jus.br/processos/detalhe.asp?incidente=6475588
  - ADI 7.156: https://portal.stf.jus.br/processos/detalhe.asp?incidente=6396615
- As certidões foram lidas nas abas Decisões e Andamentos, verificado em 28/10/2026.
- Atas de julgamento publicadas no DJE em 02/07/2026 (divulgado em 01/07) e em 04/08/2026 (divulgado em 03/08), conforme os andamentos da ADI 7.236.
- Antecedente: em 23/09/2025, uma medida cautelar ad referendum suspendeu a expressão "pela metade do prazo previsto no caput deste artigo" (art. 23, § 5º).
- Acórdão: ainda não publicado em 28/10/2026.
- A transcrição reproduz o texto exibido pelo portal. As reticências […] marcam trechos omitidos que não interessam aos itens.

### (a) ADI 7.236, sessão de 1º/7/2026 (também na aba Decisões). Sustenta N1

> "Decisão: Concluindo o julgamento, o Tribunal, por maioria, julgou parcialmente procedente a ação direta para, com relação ao art. 23, § 5º, da Lei 8.429/1992, incluído pela Lei 14.230/2021, declarar a inconstitucionalidade da expressão "pela metade do prazo previsto no caput deste artigo", com prazo máximo de 20 (vinte) anos de prescrição, nos termos do voto do Ministro Alexandre de Moraes (Relator), vencidos os Ministros Nunes Marques, Luiz Fux e Gilmar Mendes, que julgavam improcedente a ação neste ponto e modulavam os efeitos da decisão. O Ministro Dias Toffoli também julgava improcedente a ação no tocante ao § 5º do art. 23, mas, vencido, acompanhou o Relator. Nesta assentada, o Ministro Dias Toffoli consignou que acompanha o Relator no julgamento do art. 21, § 4º, da citada lei, ocorrido na sessão de 25.6.2026. Presidência do Ministro Edson Fachin. Plenário, 1º.7.2026."

### (b) ADI 7.156, sessão de 28/5/2026. Sustenta B1, N4 (§ 4º), N8 e relâmpago [8]

> "Decisão: Em continuidade de julgamento, o Tribunal julgou parcialmente procedente a ação direta para, com relação aos artigos da Lei 8.429/1992, incluídos ou alterados pela Lei 14.230/2021: (A) por unanimidade: (i) conferir interpretação conforme a Constituição ao art. 1º, § 8º, para fixar o seguinte sentido: "exceto nos casos que evidenciado o dolo ou erro grosseiro, consideradas as circunstâncias do caso e a gravidade da infração, nos termos do art. 14 do Decreto nº 9.830/2019, não configura improbidade a ação ou omissão decorrente de divergência interpretativa da lei, baseada em jurisprudência assentada nos Tribunais Superiores ou no Supremo Tribunal Federal e, na falta dessa jurisprudência, em decisão de mérito transitada em julgado proferida por órgão colegiado de 2º Grau, mesmo que não venha a ser posteriormente prevalecente"; e (ii) julgar improcedente o pedido relacionado ao art. 12, I, II, e § 9º, declarando-os constitucionais; (B) por maioria: (i) declarar, com efeitos ex tunc, a inconstitucionalidade da expressão "e benefícios diretos" do § 1º do art. 3º, ressalvados os casos já transitados em julgado, vencidos os Ministros Flávio Dino, Luiz Fux e Nunes Marques, que julgavam improcedente o pedido; (ii) julgar improcedente o pedido relacionado ao art. 11, caput, incisos I e II, e §§ 3º e 4º, declarando-os constitucionais, vencido o Ministro Edson Fachin (Presidente); (iii) julgar improcedente o pedido relacionado ao art. 12, III, reafirmando a constitucionalidade da nova redação conferida ao citado artigo, mantida a autoridade da medida cautelar deferida na ADI nº 6.678/DF, para reconhecer que os atos de improbidade culposos e aqueles violadores de princípios - portanto, que não tenham ensejado locupletamento ilícito ou dano ao erário - não devem ensejar a aplicação da pena de suspensão dos direitos políticos desde 1º/10/2021, vencidos os Ministros Flávio Dino e Cármen Lúcia; e (iv) declarar a inconstitucionalidade do art. 12, § 4º, vencidos os Ministros Gilmar Mendes, Cristiano Zanin, Nunes Marques e Dias Toffoli. Tudo nos termos do voto do Ministro André Mendonça (Relator). […] Plenário, 28.5.2026."

### (c) ADI 7.236, sessão de 28/5/2026. Sustenta B1 (o mesmo texto do § 8º de (b)), N4 e relâmpago [8]

A certidão traz o mesmo texto da interpretação conforme do art. 1º, § 8º, transcrito em (b). Também contém:

> "(A) por unanimidade: (i) declarou a constitucionalidade do artigo 1º, §§ 1º, 2º e 3º, e do artigo 10, julgando improcedente o pedido; […] (B) por maioria: (i) julgou improcedente a presente ação em relação ao artigo 11, caput, e revogação dos incisos I e II […] declarando-os constitucionais […]; e (ii) julgou inconstitucional o artigo 12, §, 4º, vencidos os Ministros Gilmar Mendes, Cristiano Zanin, Nunes Marques e Dias Toffoli."

### (d) ADI 7.156, sessão de 24/6/2026. Sustenta C1/N3, N2, N4 (§ 1º), N5, N7 e S1

A certidão da ADI 7.236 da mesma sessão traz os mesmos itens (i), (ii) e o item relativo ao art. 23-C.

> "Decisão: Em continuidade de julgamento, o Tribunal, por unanimidade, julgou parcialmente procedente a ação direta para, com relação aos artigos da Lei 8.429/1992, incluídos ou alterados pela Lei 14.230/2021: (i) no que se refere ao art. 12, § 1º: declarar a inconstitucionalidade das expressões "apenas" e ", na hipótese do inciso I do caput deste artigo, e em caráter excepcional,"; e conferir interpretação conforme a Constituição à expressão "podendo", devendo ser entendida como poder-dever, somente sendo permitido ao magistrado deixar de estender a sanção aos demais vínculos em caráter excepcional, consideradas as circunstâncias do caso e a gravidade da infração; (ii) no que se refere aos arts. 12, § 10; 17, §§ 10-C, 10-D e 10-F, I; e 17-B, § 3º: declarar a inconstitucionalidade dos dispositivos; (iii) no que se refere ao art. 16, parágrafos 3º, 4º e 10: declarar, com efeitos ex nunc, a inconstitucionalidade das expressões [a] "apenas" e "mediante a demonstração no caso concreto de perigo de dano irreparável ou de risco ao resultado útil do processo" do art. 16, § 3º; [b] "não podendo a urgência ser presumida" do art. 16, § 4º; e [c] "sem incidir sobre os valores a serem eventualmente aplicados a título de multa civil ou sobre acréscimo patrimonial decorrente de atividade lícita" do art. 16, § 10; e atribuir interpretação conforme a Constituição ao art. 16, §§ 3º, 4º e 10, de modo a admitir [a] em hipóteses excepcionais, por meio de decisão devidamente fundamentada, a indisponibilidade de bens com base em tutela de evidência; [b] igualmente em caráter excepcional, por meio de decisão devidamente fundamentada, a presunção de urgência; e [c] como regra geral, que a medida de indisponibilidade recai sobre montante suficiente a garantir o integral ressarcimento do dano ao erário, para que o valor possa abranger a multa civil e o enriquecimento ilícito, se houver, podendo abranger, até esse limite, a integralidade dos bens dos requeridos, independentemente da sua origem, observadas as situações de impenhorabilidade previstas na legislação processual e em normas específicas; (iv) no que se refere ao art. 17, § 19, II: reconhecer a constitucionalidade do dispositivo, julgando improcedente, neste ponto, a ação direta, com observações constantes da fundamentação do voto do Relator; (v) no que se refere ao art. 17-C, § 2º: declarar a inconstitucionalidade, com efeitos ex nunc, da expressão "e dos benefícios diretos", com interpretação conforme, para assentar que fica "vedada qualquer solidariedade para fins de sanção, ressalvada a possibilidade para fins de responsabilidade patrimonial"; (vi) no que se refere ao art. 17-D: atribuir interpretação conforme a Constituição para fixar que "A ação por improbidade administrativa é repressiva, destinada à aplicação de sanções de caráter pessoal previstas nesta Lei, não podendo ser utilizada como substitutiva da ação civil pública"; (vii) no que se refere ao parágrafo único do art. 17-D: julgar inconstitucional a expressão "agentes públicos, inclusive políticos"; e (viii) no que se refere ao art. 23-C: atribuir interpretação conforme a Constituição, para fixar a exegese de que "os atos que ensejem enriquecimento ilícito, perda patrimonial, desvio, apropriação, malbaratamento ou dilapidação de recursos públicos dos partidos políticos, ou de suas fundações, poderão ser responsabilizados nos termos da Lei 9.096/1995, mas sem prejuízo da incidência da Lei de Improbidade Administrativa". Tudo nos termos do voto do Ministro André Mendonça (Relator). […] Plenário, 24.6.2026."

### (e) ADIs 7.156 e 7.236, sessão de 25/6/2026. Sustenta B2/N6

> "[…] com relação ao art. 21, § 4º, da Lei 8.429/1992, incluído pela Lei 14.230/2021, declarar a sua parcial inconstitucionalidade, com interpretação conforme a Constituição, no sentido de que a decisão criminal transitada em julgado, em ação que discuta os mesmos fatos, somente impede a tramitação da ação de improbidade administrativa nas hipóteses dos arts. 65 (sentença penal que reconhecer ter sido o ato praticado em estado de necessidade, em legítima defesa, em estrito cumprimento de dever legal ou no exercício regular de direito); 386, I (estar provada a inexistência do fato); e 386, IV (estar provado que o réu não concorreu para a infração penal), todos do Código de Processo Penal. Aplica-se essa mesma compreensão seja na absolvição, seja na rejeição da denúncia, seja na hipótese de preclusão da decisão de arquivamento por proposição do Ministério Público, ressalvada a hipótese do art. 18 do Código de Processo Penal."

A certidão da ADI 7.156 da mesma sessão acrescenta:

> "(i) no que se refere ao art. 8º: não conhecer do pedido relacionado à expressão "apenas" […]"

### Mapa de uso

| Item do resumo | Trecho |
|---|---|
| B1 (§ 8º) | (b) (A)(i); (c) |
| B2 / N6 (art. 21, § 4º) | (e) |
| C1 / N3 (art. 16) | (d) (iii) |
| N1 (art. 23, § 5º) | (a) |
| N2 (art. 12, § 10) | (d) (ii) |
| N4 (art. 12, §§ 1º e 4º) | (d) (i); (b) (B)(iv); (c) (B)(ii) |
| N5 / S1 (art. 17, §§ 10-C, 10-D, 10-F, I; art. 17-B, § 3º) | (d) (ii) |
| N7 (art. 17-C, § 2º) | (d) (v) |
| N8 (art. 3º, § 1º) | (b) (B)(i) |
| relâmpago [8] (art. 11) | (b) (B)(ii); (c) (B)(i) |
