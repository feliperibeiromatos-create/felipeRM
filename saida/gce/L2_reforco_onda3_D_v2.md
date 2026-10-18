# L2_reforco_onda3_D_v2.md — T-97 — 2026-10-18 — gerado por gce-cpp

## RESPOSTA AO RELATÓRIO DE QA (rodada de correção R2)
Lidos: saida/gce/QA_T97D_R1_2026-10-18_gce-cqfp.md (3 reprovados, 8 ajustes, 17 aprovados), saida/gce/QA_T97D_normativo_2026-10-18_qa-normativo.md (R127 a R130 CONFEREM), D-REFORCO-2, D-ADERENCIA, D-T90-R2-ACEITE (2.7: só itens novos de aderência direta), D-T96-ONDA2-ACEITE (II) e as partes A (v2), B (v1) e C (v1) da onda 3. Nenhum commit ou push. Nada mais foi alterado além do que consta abaixo e das linhas de contagem, mapa, proveniência e registros que dependem das mudanças.

| id | veredito do QA | resposta | o que mudou |
|---|---|---|---|
| L2-R103 | APROVADO | sem ajuste | nada |
| L2-R104 | AJUSTAR | acatado | orientação atribuída à documentação do Google Cloud Speech-to-Text ("Segundo a documentação…"), com a ambientação da Câmara em frase própria, fora da remissão |
| L2-R105 | APROVADO | acatado o registro (par com L2-Q06, 2.2: não vão ao mesmo caderno) | nada no texto; registro 5 da seção 1.4 |
| L2-R106 | AJUSTAR | acatado | fecho com juízo explícito: "Nessa situação, o entendimento da Câmara está correto." |
| L2-R107 | APROVADO | sem ajuste | nada |
| L2-R108 | REPROVADO (escopo; procedimento contratual de um fornecedor) | acatado; substituído por item novo (mesmo id) | novo item da 2.7, aderência direta, controle de qualidade da transcrição por conferência: na inspeção de qualidade do Azure Speech (dados somente de áudio), a pessoa reproduz o áudio e determina se o resultado está correto (E; TSj; [TS]; não VOLÁTIL) |
| L2-R109 | APROVADO | sem ajuste | nada |
| L2-R110 | APROVADO | sem ajuste | nada |
| L2-R111 | REPROVADO (escopo; minúcia de medição de contrato) | acatado; substituído por item novo (mesmo id) | novo item da 2.7, auditoria de amostras: amostra representativa para avaliar a acurácia e amostra grande para melhorar o reconhecimento, com as finalidades trocadas (E; PC; [TS]; não VOLÁTIL). A folha fica com 4 itens do SLA (R106, R107, R109, R110) |
| L2-R112 | AJUSTAR | acatado | "o sclite, do NIST, totaliza…" (a afirmação deixa de ser estendida a todas as ferramentas) |
| L2-R113 | APROVADO | sem ajuste | nada |
| L2-R114 | AJUSTAR | acatado, com o texto exato do QA | E que depende da base: "o valor global do WER basta para direcionar as melhorias, dispensando a análise da distribuição dos erros", sem a cauda que se denuncia |
| L2-R115 | APROVADO | sem ajuste | nada |
| L2-R116 | APROVADO (ressalva de registro) | acatado o registro | texto e gabarito inalterados; ressalva (critério da nota inclui recursos e latência) no registro 8 da seção 1.4 |
| L2-R117 | APROVADO | sem ajuste | nada |
| L2-R118 | AJUSTAR (formato AP errado; rótulo) | acatado | reclassificado de AP para D (2.8 fica com D 4/20 = 20% e AP 2/20 = 10%); mantido não VOLÁTIL, com registro expresso pedido à Gerência (ressalva de disponibilidade no próprio enunciado; T96, seção 2.2) |
| L2-R119 | APROVADO | acatado o registro (não VOLÁTIL, mesma ressalva do R118) | nada no texto; registro 1 da seção 1.4 |
| L2-R120 | APROVADO | sem ajuste (VOLÁTIL baixo mantido) | nada |
| L2-R121 | AJUSTAR | acatado | fecho com juízo explícito: "Nessa situação, a suposição da equipe está correta." |
| L2-R122 | APROVADO | sem ajuste | nada |
| L2-R123 | APROVADO | sem ajuste (ressalva da seção 2 do QA registrada: a mesma troca dita duas vezes; [TS] mantido) | nada |
| L2-R124 | AJUSTAR (paráfrase errada) | acatado | forma literal: "quando faltam dados de treinamento do próprio domínio" (enunciado, mapa e gabarito) |
| L2-R125 | AJUSTAR (rótulo) | acatado | marcado VOLÁTIL (baixo), critério (c); a 2.8 fica com 4/20 = 20% (R18, R120, R121, R125), no teto |
| L2-R126 | APROVADO | sem ajuste | nada |
| L2-R127 | APROVADO, PENDENTE NORMATIVO | acatado; qa-normativo: CONFERE | marca "CONFERE" no mapa e no gabarito |
| L2-R128 | REPROVADO (escopo; regra de procedimento, sem aderência ao 2.8) | acatado; substituído por item novo (mesmo id) | novo item da 2.8, vocabulário/termo: parecer (RICD, art. 126, caput), E por troca de Comissão por Plenário (D; [TS]; não VOLÁTIL). PENDENTE NORMATIVO, por ser item novo |
| L2-R129 | APROVADO, PENDENTE NORMATIVO | acatado; qa-normativo: CONFERE | marca "CONFERE" no mapa e no gabarito |
| L2-R130 | APROVADO; aderência PARCIAL proposta | acatado; qa-normativo: CONFERE; acrescentado o parágrafo único do art. 90 à base | aderência PARCIAL (D-ADERENCIA: só simulado diagnóstico; D1 da gce-gerencia); base: "arts. 66, IV e § 1º, 89, caput, e 90, caput e parágrafo único", com o trecho literal do parágrafo único; a justificativa cita o § 1º do art. 66, ao qual o art. 89 remete |

Demais pontos do QA:
- Registro da seção 5 (a afirmação da seção 1.3, de que nenhum outro item do pacote usa os arts. 66, 89, 90, 95 ou 118, ficou superada pela parte B): acatado; a seção 1.3 foi corrigida (L2-R49 e L2-R67, da parte B, declarados com ponto próprio).
- Pedido de sub-regra de VOLÁTIL para cláusula de contrato de fornecedor (seção 6): acatado como registro para a Gerência (registro 1 da seção 1.4); sem R108 e R111 antigos, a 2.7 tem 0/20 VOLÁTEIS.
- Lacunas de cobertura da 2.7 (revisão em dupla; auditoria de amostras): reposição por conferência do resultado (R108) e por amostra de transcrições (R111), com base aberta hoje e trecho literal. "Revisão em dupla" em sentido estrito segue com Q24 (e a passagem dupla de R103): não há, nas páginas oficiais abertas hoje, trecho literal sobre segundo revisor independente distinto desses; lacuna remanescente registrada, não resolvida nesta rodada.
- Observação da seção 7 (frase do curso "adaptação não corrige sotaque nem ruído"): não faz parte deste arquivo; competência da gce-gerencia (errata do curso e do aspecto (xv); pacote v1.10); registrada no registro 8 da seção 1.4. Não acatada aqui, por ser matéria de outro arquivo.
- Contagens após a R2: 28 itens; 14 C / 14 E (50,0%); [TS] 18 de 28 (13 em E, 5 em C); VOLÁTEIS novos 3 (R120, R121, R125; risco baixo); 2.7: 0/20 VOLÁTEIS; 2.8: 4/20 = 20%; aderência 27 direta e 1 parcial (R130). Pendente: conferência normativa do R128 novo (qa-normativo) e QA R2 de R108, R111, R128 e dos 8 ajustes (gce-cqfp).

Onda 3 do reforço, parte D, v2 (rodada de correção R2 do QA_T97D_R1; ciclo 2026-10-18 s12c4). Escopo: P2-2.7 (+14, ids L2-R103 a L2-R116) e P2-2.8 (+14, ids L2-R117 a L2-R130). Cada folha passa de 6 para 20. Total: 28 itens.
Rótulo de todos os itens: AUTORAL (produtor gce-cpp, lote L2-R, onda 3 do reforço, D-REFORCO-2). QA PENDENTE: nenhum item deste arquivo entra em simulado antes da QA e da reconciliação (D-QA-PENDENTE). Nenhum item existente foi alterado.
Convenção: "verificado em 18/10/2026" = página aberta e lida nesta data (curl com User-Agent de navegador, HTTP 200; trechos conferidos no texto extraído). Nenhuma base de data anterior foi usada (D-FONTE-DATA-ANTERIOR não se aplica). Nenhum item cita número de versão, preço ou limite numérico de produto como ponto de julgamento.
Legenda de formatos: D = definição; TSj = troca de sujeito; SH = situação hipotética; NP = número ou prazo; PC = par confundível; AP = aplicação parlamentar. Critério de classificação (T91_reconciliacao, seção 3.1): o formato é o da construção do ponto de julgamento, e não o do gabarito; o item C tem o formato da sua contraparte E. Os canônicos da folha foram classificados como em L2_reforco_onda1_v3.md, seção 2.
Critérios aplicados: D-REFORCO-1/2 (um ponto de julgamento por item, único na folha, inclusive frente aos canônicos e ao pacote inteiro, T96_reconciliacao, seção 4); critério de VOLÁTIL da D-T96-ONDA2-ACEITE (II) (VOLÁTIL = gabarito que depende de (a) versão, limite, preço ou modelo padrão; (b) comportamento padrão ou parâmetro nomeado de API; (c) existência ou disponibilidade de recurso condicionada pela documentação; (d) comportamento ilustrado só em saída de exemplo; funcionamento documentado de recurso central, sem número, versão, preço, padrão ou disponibilidade condicionada, é não VOLÁTIL, com conferência de base em 4–8/1/2027); registro da T90_reconciliacao (na 2.7, itens novos com aderência DIRETA até a folha ter 10: nenhum novo ponto da Lei 14.133 na 2.7; a folha tem hoje 2 de 6 itens de aderência parcial, R14 e R15, e passa a 2 de 20); registros O-1 a O-8 da T-93 e recomendações 1 a 7 do estilo_onda_2.md ("independentemente" também em C e em E, "pode" em E, concessiva alternada entre C e E, aberturas "Segundo a…" variadas, fonte nomeada quando o item usa "orientação" ou "recomendação", sem absolutos empilhados em E, ambientação parlamentar fora do escopo da remissão).

=====================================================================
PARTE 1/3 — MAPA
=====================================================================

## 1.1 P2-2.7 Controle de qualidade: revisão em dupla, auditorias de amostras, SLA — itens novos (um ponto de julgamento por item)

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL / risco | aderência |
|---|---|---|---|---|---|---|
| L2-R103 | P2-2.7 | A transcrição de referência (ground truth) para medir a acurácia é obtida por transcrição humana, em passagem única ou dupla, e não por outro sistema automático | TSj | Google Cloud, Speech-to-Text, "Measure and improve speech accuracy", seção "Measuring speech accuracy" (Get ground truth transcriptions): https://docs.cloud.google.com/speech-to-text/docs/v1/speech-accuracy (verificado em 18/10/2026) | n | direta |
| L2-R104 | P2-2.7 | Segundo a documentação do Google (orientação atribuída à fonte no enunciado), as convenções da transcrição de referência (pontuação, números, capitalização) devem coincidir, o máximo possível, com as do sistema avaliado; não existe formato de transcrição único aceito por todos | AP | Google Cloud, Speech-to-Text, "Measure and improve speech accuracy", seções "Ground-truth conventions" e "Measuring speech accuracy": https://docs.cloud.google.com/speech-to-text/docs/v1/speech-accuracy (verificado em 18/10/2026) | n | direta |
| L2-R105 | P2-2.7 | O WER e a medida de confiança são métricas independentes, que em geral não se correlacionam: confiança alta não permite concluir WER baixo | SH | Google Cloud, Speech-to-Text, "Measure and improve speech accuracy", seção "Relation of WER to a confidence score": https://docs.cloud.google.com/speech-to-text/docs/v1/speech-accuracy (verificado em 18/10/2026) | n | direta |
| L2-R106 | P2-2.7 | O SLA do serviço em nuvem mede disponibilidade (percentual mensal de tempo de atividade, a partir de erros de servidor), e não a acurácia das transcrições | SH | Google Cloud, "Speech-to-Text Service Level Agreement (SLA)": https://cloud.google.com/speech-to-text/sla (verificado em 18/10/2026) | n | direta |
| L2-R107 | P2-2.7 | O remédio previsto no SLA é crédito financeiro aplicado a faturas futuras, declarado como único e exclusivo remédio do cliente | TSj | Google Cloud, SLA do Speech-to-Text: https://cloud.google.com/speech-to-text/sla (verificado em 18/10/2026) | n | direta |
| L2-R108 | P2-2.7 | Na inspeção de qualidade com dados somente de áudio, a pessoa reproduz o áudio carregado e determina se o resultado do reconhecimento está correto; a decisão não é tomada automaticamente pelo serviço | TSj | Microsoft, "Test recognition quality of a custom speech model": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-inspect-data (verificado em 18/10/2026) | n | direta |
| L2-R109 | P2-2.7 | Erros decorrentes de uso do serviço em desacordo com a documentação (campos inválidos) ficam fora do SLA e não contam como indisponibilidade | SH | Google Cloud, SLA do Speech-to-Text, seção "SLA exclusions": https://cloud.google.com/speech-to-text/sla (verificado em 18/10/2026) | n | direta |
| L2-R110 | P2-2.7 | Cálculo do percentual mensal de tempo de atividade: (minutos do mês − minutos de indisponibilidade) ÷ minutos do mês; 432 de 43.200 minutos = 1% de indisponibilidade | NP | Google Cloud, SLA do Speech-to-Text, definição de "Monthly Uptime Percentage" (só a fórmula; nenhum objetivo numérico é cobrado): https://cloud.google.com/speech-to-text/sla (verificado em 18/10/2026) | n | direta |
| L2-R111 | P2-2.7 | Para avaliar a acurácia, recomenda-se amostra representativa de transcrições (vários locutores e falas típicas dos usuários); para melhorar o reconhecimento, exige-se amostra grande | PC | Microsoft, "How to create human-labeled transcriptions": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-human-labeled-transcriptions (verificado em 18/10/2026) | n | direta |
| L2-R112 | P2-2.7 | O sclite totaliza os erros por locutor e por par referência–hipótese, permitindo auditoria por estrato (orador) | AP | NIST SCTK, documentação do sclite, seção "The scoring process": https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm (verificado em 18/10/2026) | n | direta |
| L2-R113 | P2-2.7 | No sclite, só as falas presentes no arquivo de hipótese são pontuadas; a referência pode ter registros a mais, o que permite pontuar uma amostra | TSj | NIST SCTK, documentação do sclite, seção "The alignment process", "Utterance ID Matching": https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm (verificado em 18/10/2026) | n | direta |
| L2-R114 | P2-2.7 | Além do WER global, deve-se examinar como os erros se distribuem e analisar arquivo a arquivo, para direcionar as melhorias | AP | Microsoft, "Test accuracy of a custom speech model", seção "Resolve errors and improve WER": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data (verificado em 18/10/2026) | n | direta |
| L2-R115 | P2-2.7 | Dados somente de áudio servem à inspeção (qualitativa); quantificar a acurácia (WER) exige áudio com transcrições rotuladas por pessoas | PC | Microsoft, "Test and train data for custom speech", seção "Audio data for training or testing": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-test-and-train (verificado em 18/10/2026) | n | direta |
| L2-R116 | P2-2.7 | Um modelo só é considerado melhor quando mostra melhorias significativas em todos os cenários avaliados (critério da nota de transparência), e não em apenas alguns | SH | Microsoft, nota de transparência do Azure Speech (speech to text), seção "System performance": https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note (verificado em 18/10/2026) | n | direta |

## 1.2 P2-2.8 Vocabulário técnico parlamentar e vocabulário adaptado (language model adaptation) — itens novos (um ponto de julgamento por item)

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL / risco | aderência |
|---|---|---|---|---|---|---|
| L2-R117 | P2-2.8 | Frase de várias palavras na adaptação aumenta a probabilidade da sequência e também a de partes da frase, inclusive de palavras individuais | TSj | Google Cloud, Speech-to-Text, "Improve transcription results with model adaptation", seção "Improve recognition of words and phrases": https://docs.cloud.google.com/speech-to-text/docs/adaptation-model (verificado em 18/10/2026) | n | direta |
| L2-R118 | P2-2.8 | Classes agrupam palavras de um conceito comum (valores monetários, datas) sem exigir listar cada valor; a disponibilidade varia por modelo e idioma | D | Google Cloud, Speech-to-Text, "Improve transcription results with model adaptation", seção "Improve recognition using classes": https://docs.cloud.google.com/speech-to-text/docs/adaptation-model (verificado em 18/10/2026) | n | direta |
| L2-R119 | P2-2.8 | A classe personalizada (lista própria de itens) funciona como as predefinidas e pode ser combinada com elas na mesma frase | TSj | Google Cloud, Speech-to-Text, "Improve transcription results with model adaptation", seção "Custom classes": https://docs.cloud.google.com/speech-to-text/docs/adaptation-model (verificado em 18/10/2026) | n | direta |
| L2-R120 | P2-2.8 | Token de classe inválido ou malformado é ignorado sem erro, e o restante da frase continua sendo usado como contexto | SH | Google Cloud, Speech-to-Text, "Improve transcription results with model adaptation", seção "Class tokens": https://docs.cloud.google.com/speech-to-text/docs/adaptation-model (verificado em 18/10/2026) | S (BAIXO) | direta |
| L2-R121 | P2-2.8 | A lista de frases do Azure Speech não está disponível na transcrição em lote (API de lote não a suporta) | SH | Microsoft, "Improve recognition accuracy with phrase list": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/improve-accuracy-phrase-list (verificado em 18/10/2026) | S (BAIXO) | direta |
| L2-R122 | P2-2.8 | Quando se pode antecipar as palavras que serão faladas, usa-se a lista de frases; se a acurácia permanecer baixa, considera-se o custom speech | AP | Microsoft, nota de transparência do Azure Speech, seção "Best practices for improving system performance", itens "Add custom vocabularies" e "Use custom speech": https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note (verificado em 18/10/2026) | n | direta |
| L2-R123 | P2-2.8 | Dados de treinamento e de ajuste não devem se sobrepor; a sobreposição pode enviesar o modelo e prejudicar a acurácia | TSj | AWS, Amazon Transcribe, "Custom language models", seção "Training versus tuning data": https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html (verificado em 18/10/2026) | n | direta |
| L2-R124 | P2-2.8 | Treinamento ensina termos novos e contexto; ajuste (tuning) é opcional e recomendado quando faltam dados de treinamento do próprio domínio | PC | AWS, Amazon Transcribe, "Custom language models", seções "Data sources" e "Training versus tuning data": https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html (verificado em 18/10/2026) | n | direta |
| L2-R125 | P2-2.8 | O vocabulário personalizado só pode ser usado se criado na mesma região da AWS da transcrição | SH | AWS, Amazon Transcribe, "Custom vocabularies": https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html (verificado em 18/10/2026) | S (BAIXO) | direta |
| L2-R126 | P2-2.8 | Modelo implantado em endpoint do custom speech fica fixo até o usuário atualizá-lo; novo modelo base não altera a acurácia (dentro da vigência do modelo) | TSj | Microsoft, "What is custom speech?", seção "Model stability and lifecycle": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-speech-overview (verificado em 18/10/2026) | n | direta |
| L2-R127 | P2-2.8 | Definição regimental de questão de ordem: dúvida sobre a interpretação do Regimento, na sua prática exclusiva ou relacionada com a Constituição Federal | D | RICD, art. 95, caput, no Legin: https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html (verificado em 18/10/2026; CONFERE pelo qa-normativo em 18/10/2026) | n | direta |
| L2-R128 | P2-2.8 | Definição regimental de parecer: proposição com que uma Comissão (e não o Plenário) se pronuncia sobre qualquer matéria sujeita a seu estudo | D | RICD, art. 126, caput, no Legin: https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html (verificado em 18/10/2026; art. 126 lido no Legin na R2; PENDENTE NORMATIVO: item novo, conferência do qa-normativo solicitada) | n | direta |
| L2-R129 | P2-2.8 | Emenda de redação é a emenda modificativa (e não aditiva) que visa a sanar vício de linguagem, incorreção de técnica legislativa ou lapso manifesto | PC | RICD, art. 118, §§ 6º e 8º, no Legin: https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html (verificado em 18/10/2026; CONFERE pelo qa-normativo em 18/10/2026) | n | direta |
| L2-R130 | P2-2.8 | Quem fala nas Comunicações Parlamentares (representantes de Partidos e Blocos indicados pelos Líderes) e nas Comunicações de Lideranças (os Líderes, por tempo proporcional à bancada) | PC | RICD, arts. 66, IV e § 1º, 89, caput, e 90, caput e parágrafo único, no Legin: https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html (verificado em 18/10/2026; CONFERE pelo qa-normativo em 18/10/2026) | n | PARCIAL (D-ADERENCIA: só simulado diagnóstico; ver registro 4 da seção 1.4) |

## 1.3 Verificação de não repetição (ponto conferido contra o pacote inteiro)

Fontes conferidas por busca textual e leitura: saida/pacote/pacote.json v1.9 (334 itens; todas as folhas e o P1), saida/gce/GCE_Lote2_v2_CPP.md, GCE_Lote2_padroes_GCE.md, GCE_Lote2_consolidacao_GCE.md, L2_reforco_onda1_v3.md, L1_reforco_onda1_v2.md, L1_reforco_onda2_A_v3, B_v2, C_v2, D_v3 e saldo_v2 (inclusive L1-R131), L3_reforco_onda1_v3.md. Das outras partes da onda 3, existiam na conferência final saida/gce/L2_reforco_onda3_A_v1.md (folhas 2.1 e 2.2, ids L2-R19 a L2-R46) e saida/gce/L2_reforco_onda3_C_v1.md (folhas 2.5 e 2.6, ids L2-R75 a L2-R102), ambos lidos (mapa, enunciados e gabarito) e comparados por busca textual com cada ponto desta parte; na rodada R2 a parte B (saida/gce/L2_reforco_onda3_B_v1.md, folhas 2.3 e 2.4, ids L2-R47 a L2-R74) e a parte A em v2 (L2_reforco_onda3_A_v2.md) foram lidas e comparadas, por busca textual, com os três itens novos (R108, R111, R128) e com R127 a R130, sem gêmeo.
- P2-2.7 existentes: Q24 (revisão em dupla exige segundo revisor independente), Q25 (auditoria por amostragem estima a qualidade do conjunto), Q26 (amostra sem erro não prova ausência de erro nas peças não examinadas), Q27 (SLA pode fixar prazo e qualidade), R14 (terceiro que assiste o fiscal não exerce atribuição própria de fiscal; PARCIAL), R15 (prazos e métodos do recebimento definidos em regulamento ou no contrato; PARCIAL). Nenhum dos 14 novos repete esses pontos.
- P2-2.8 existentes: Q28 (LM adaptado altera a probabilidade de sequências), Q29 (OOV é termo ausente do vocabulário), Q30 (reforço excessivo insere o termo onde não foi dito), R16 (TECAD é vocabulário controlado), R17 (melhores dados de adaptação são transcrições precisas do domínio), R18 (limite de frases da phrase list; VOLÁTIL alto). Nenhum dos 14 novos repete esses pontos.
- Entre os 14 novos de cada folha, os pontos são todos distintos (comparação feita aos pares). Cada ponto da 2.7 e da 2.8 foi buscado também no restante do pacote e nos itens das ondas 1 e 2 (transcrição de referência humana, convenções da referência, confiança e WER, SLA, uptime, sclite, distribuição de erros, inspeção por reprodução do áudio, volume e finalidade da amostra de transcrições, áudio sem transcrição, critério de troca de versão, classe, token de classe, lista de frases em lote, pauta e inscritos, treinamento e ajuste, região da AWS, modelo fixo no endpoint, questão de ordem, parecer, emenda de redação, Comunicações Parlamentares): nenhuma ocorrência do mesmo ponto.
- R2 (reposição): R108, R111 (2.7) e R128 (2.8) foram trocados por pontos novos, buscados por texto no pacote v1.9 (pacote.json), nas ondas 1 e 2 e nas partes A, B e C da onda 3: "inspeção de qualidade por reprodução do áudio", "amostra representativa para avaliar e grande para melhorar" e "parecer" (RICD, art. 126). Nenhuma ocorrência do mesmo ponto. Os pontos retirados (crédito do SLA solicitado ao suporte; indisponibilidade medida no servidor; breves comunicações) não voltam; o id é reutilizado pelo item novo, conforme a determinação da Gerência.
- Pontos planejados e descartados por gêmeo (não produzidos): "o teste do modelo adaptado usa áudios diferentes dos usados no ajuste" (Microsoft, "Test accuracy of a custom speech model"), que já é o L1-R22; e, depois da leitura do L2_reforco_onda3_A_v1.md, quatro pontos que a 2.7 tinha planejado e que a parte A já tem: conjunto de teste de gravações reais amostradas ao acaso (A: L2-R43), o mesmo conjunto renovado periodicamente (A: L2-R43), canal de retorno dos usuários após a implantação (A: L2-R36) e a Errata do art. 98, § 1º, do RICD (A: L2-R19). Os quatro foram trocados por pontos novos (R103, R104, R105 e R116 desta parte), em vez de ficarem como gêmeos declarados.
- Proximidades que a Gerência pode querer ver (nenhuma é duplicata; todas por ponto próprio, e as de outra folha entram declaradas e com ângulo próprio da folha, conforme a T96_reconciliacao, seção 4):
  - R103 × L2-R26 (parte A, 2.1), L1-R21 e L1-R128 (1.1 e 1.8): R26 julga o que é transcrição rotulada por humanos (palavra por palavra, e não resumo); R21 julga o efeito de falhas na referência sobre o WER; R128 julga comparar o modelo base com a transcrição humana; R103 julga como a referência costuma ser obtida (por pessoas, em passagem única ou dupla, e não por outro sistema automático).
  - R104 × L2-R09 (2.5), L1-R81, R85 (1.5) e L2-R75 a R78 (parte C, 2.5): R09 julga em que textos se aplica a normalização no cálculo do WER; R81 e R85 julgam o TER e o formato de exibição da referência; R75 a R78 julgam regras de normalização das transcrições de treinamento da Microsoft (siglas, números, abreviações); R104 julga que as convenções da referência devem coincidir com as do sistema avaliado, porque não há formato único de transcrição.
  - R105 × L2-Q06 (2.2), L1-R32 (1.1) e L2-R13 (2.6): Q06 julga que alta confiança não significa correção por definição e que conferir só a baixa confiança não basta; R32 julga as versões alternativas com confiança; R13 julga usar a confiança por palavra para destacar trechos; R105 julga que WER e confiança são métricas independentes, sem correlação esperada.
  - R106 × L2-Q27 (2.7): Q27 julga o que um SLA contratual de transcrição pode fixar (prazo e qualidade); R106 julga o que o SLA de um serviço em nuvem de fato mede (disponibilidade). R107, R109 e R110 julgam outras cláusulas do mesmo SLA (remédio exclusivo, exclusão por uso fora da documentação, fórmula do percentual), uma por item.
  - R112 × L1-R30, R31 (1.1) e R113 × L1-R26, R28 (1.1): mesma ferramenta (sclite), outros pontos (pesos de palavras, taxa de erro de sentença, alinhamento, referências alternativas). R112 julga a totalização por locutor; R113 julga quais falas são pontuadas (as da hipótese).
  - R114 × L1-R20, R93, R95 (1.6 e 1.1): esses julgam a causa associada a cada tipo de erro; R114 julga o que a análise do teste deve cobrir (distribuição dos erros e exame arquivo a arquivo).
  - R115 × L1-R128 (1.8) e L2-R06 (2.3): R128 julga a comparação do modelo base com a transcrição humana por WER; R06 julga a fórmula do WER; R115 julga que dados somente de áudio servem à inspeção e não à quantificação.
  - R108 (novo) × R115 (2.7), L1-R128 (1.8) e L2-R44 (parte A, 2.2): R115 julga para que serve cada tipo de dado (áudio sem transcrição serve à inspeção; quantificar exige transcrição rotulada); R44 julga ouvir amostras do áudio antes do envio (preparo do áudio); R108 julga quem decide, na inspeção de qualidade, se o resultado do reconhecimento está correto (a pessoa que reproduz o áudio, e não o serviço).
  - R111 (novo) × L2-R43 (parte A, 2.2), L1-R21 e L2-R26 (parte A, 2.1): R43 julga a composição do conjunto de teste (entradas reais da produção, amostradas ao acaso e renovadas); R26 julga o que é a transcrição rotulada por humanos; R111 julga a finalidade de cada amostra de transcrições (representativa para avaliar, grande para melhorar o reconhecimento), sem tratar de aleatoriedade, origem ou renovação do conjunto.
  - R116 × L2-R04 (2.2): R04 julga que a avaliação do modelo no domínio de uso cabe à instituição; R116 julga o critério de melhoria em todos os cenários para trocar a versão do modelo. Ver o registro 5 da seção 1.4.
  - R117 × L2-Q28 (2.8): Q28 julga o efeito do LM adaptado sobre sequências de palavras; R117 julga o efeito de uma frase de adaptação do Google sobre a frase e suas partes. R117 × L1-R97 (1.6): R97 julga o excesso de boost; R117 não trata de boost.
  - R118 a R120 (classes do Google) × L1-R84, R99 (1.6): R84 e R99 julgam a forma de exibição e a pronúncia; R118 a R120 julgam classes, classe personalizada e token inválido.
  - R121 e R122 × L1-R94, R120 (1.6 e 1.8): R94 e R120 julgam que a lista de frases é de tempo de execução e dispensa treinamento; R121 julga a indisponibilidade na transcrição em lote; R122 julga em que situação a lista de frases é indicada (palavras previsíveis) e quando passar ao custom speech. R122 × L1-R128 (1.8): R128 parte do WER do modelo base; R122 parte da previsibilidade do que será falado.
  - R123 e R124 × L2-R17 (2.8): mesma página da AWS ("Custom language models"); R17 julga qual é o melhor dado; R123 julga a sobreposição entre treinamento e ajuste; R124 julga o papel e a obrigatoriedade do ajuste. R124 × L2-Q28 (2.8): Q28 julga o efeito do LM adaptado; R124 não repete.
  - R125 × L1-R101, R10 (1.6): R101 julga a grafia da entrada do vocabulário (espaço ou hífen); R10 julga o que não colocar na lista; R125 julga a região do vocabulário.
  - R126 × L1-R96, R128 (1.6 e 1.8): R96 julga modelos separados por área; R128 julga o uso do WER para decidir treinar; R126 julga a estabilidade do modelo implantado.
  - R127 a R130 (RICD): nenhum item do pacote v1.9 usa os arts. 66, 81, 89, 90, 95, 118 ou 126 do RICD; entre as partes da onda 3, a parte B usa o art. 95, § 5º (L2-R49) e o art. 66, II (L2-R67), em pontos próprios (R127 julga a definição do caput do art. 95; R130 julga o art. 66, IV e § 1º, e os arts. 89 e 90). R128 (novo, art. 126, caput): nenhum item do pacote ou das partes A, B e C define parecer (a parte B tem L2-R63, aparte a parecer oral, que julga o cabimento do aparte, e não o conceito). R129 e R130 seguem como na v1 (arts. 118 e 66, IV, 89, 90).

## 1.4 Registros para a Gerência (sem alterar nada; competência D1/D2 da gce-gerencia)

1. VOLÁTIL (critério da D-T96-ONDA2-ACEITE (II)): 3 novos, todos na 2.8 e de risco baixo: R120 (critério (b): comportamento do serviço diante de token de classe inválido, ignorado sem erro), R121 (critério (c): a lista de frases não está disponível na transcrição em lote) e R125 (critério (c), marca acrescentada na R2 por determinação do QA: o vocabulário personalizado só é utilizável na região da AWS em que foi criado, condição de uso por localização que a documentação impõe). Com isso a 2.8 fica em 4/20 = 20% (R18, R120, R121, R125), no teto, sem margem para outro VOLÁTIL; se a Gerência ler a condição de região de outro modo, deve registrar. Nenhum de risco alto novo. Não VOLÁTEIS, com conferência de base em 4–8/1/2027: R106, R107, R109 e R110 (cláusulas do SLA do Google: o que o SLA mede, remédio, exclusão, fórmula; sem objetivo numérico, preço, versão ou disponibilidade condicionada), R108 e R111 novos (documentação de funcionamento e de recomendação, sem número, versão nem condição), R116 (critério de melhoria descrito pelo fornecedor, sem o percentual que a página cita), R118 (o item já ressalva que a disponibilidade das classes varia por modelo e idioma; o ponto julgado é o mecanismo da classe, T96, seção 2.2: registro expresso pedido à Gerência, como o QA pediu), R119, R126 (o item já delimita "enquanto vigente") e R128 novo (norma). Pedido de registro expresso da sub-regra proposta pelo QA (cláusula de contrato de fornecedor é VOLÁTIL quando o gabarito depende de redação particular, e NÃO VOLÁTIL quando o ponto é conceito do instrumento): sem R108 e R111 antigos, a 2.7 tem 0/20 VOLÁTEIS em qualquer leitura (quatro itens do SLA: R106, R107, R109, R110; se a Gerência os enquadrasse como VOLÁTEIS, seriam 4/20 = 20%, no teto).
2. Aderência: 27 itens são declarados de aderência DIRETA ao subitem da folha (2.7: qualidade, amostragem, SLA, revisão, inspeção; 2.8: vocabulário técnico parlamentar e vocabulário adaptado). R130 é declarado PARCIAL, conforme a proposta do QA (D-ADERENCIA: só simulado diagnóstico; ver o registro 4). Nenhum item novo da 2.7 é de aderência parcial; a 2.7 mantém 2 de 20 itens parciais (R14, R15, legado), em 10%, e os três itens repostos cobrem as lacunas apontadas pelo QA (R108: conferência do resultado ouvindo o áudio; R111: amostra de transcrições para avaliar e para melhorar), sem Regimento e sem Lei 14.133.
3. Tensão entre o curso e a documentação (não afeta nenhum item desta parte): a página "Improve transcription results with model adaptation" do Google traz, entre os usos da adaptação, "improving the accuracy of speech transcription when the supplied audio contains noise or is not very clear"; a frase do curso da 2.8 ("adaptação não corrige sotaque nem ruído", GCE_Lote2_v2_CPP.md, riscos) merece ressalva de fornecedor. Nenhum item desta parte julga esse ponto, de propósito.
4. Aderência dos itens RICD da 2.8: R127 (questão de ordem), R128 novo (parecer) e R129 (emenda de redação) são termos regimentais, de aderência direta defensável (o curso da 2.8 lista "termos regimentais (questão de ordem, destaque, requerimento)"). R130 (Comunicações Parlamentares × Comunicações de Lideranças) é declarado PARCIAL, conforme a proposta do QA (o ponto decisivo é quem fala e por quanto tempo, que é procedimento, mais do que o sentido do nome): vai só a simulado diagnóstico (D-ADERENCIA), o que a 2.8 admite; a Gerência decide em D1. Na 2.7, nenhum item novo tem Regimento ou Lei 14.133.
5. Trabalho paralelo na onda 3: as partes A, B e C existem e foram lidas na R2 (ver a seção 1.3); nenhum gêmeo nos itens novos (R108, R111, R128) nem em R127 a R130. Proximidades declaradas para a reconciliação: R103, R104 e R105 × itens da 2.3 e 2.4 sobre WER, referência e confiança (a parte B tem L2-R56 e L2-R60, faixas e escala do WER, em pontos próprios); R105 × L2-Q06 (2.2): o QA pede que o par não vá ao mesmo caderno da GBQ (T96, seção 4). Se houver gêmeo, o item desta parte cede.
6. Conferência normativa: R127, R128 (art. 81), R129 e R130 da v1 foram conferidos pelo qa-normativo em 18/10/2026 (QA_T97D_normativo_2026-10-18_qa-normativo.md): CONFERE, 0 divergência; o parágrafo único do art. 90 foi acrescentado à base do R130, conforme a observação de precisão. O R128 da v2 é item novo (RICD, art. 126, caput), lido no Legin em 18/10/2026 pela produtora e ainda sem conferência do qa-normativo (PENDENTE NORMATIVO). Não há item de lei federal nesta parte.
7. Lista de conferência de base de 4–8/1/2027 (T-11, parte P2, gce-cqfp): todos os 28 itens (todos têm base em página de fornecedor ou no Legin); 3 deles também VOLÁTEIS (R120, R121, R125). Páginas redirecionadas: a URL legal/cognitive-services/.../transparency-note redireciona para a URL de foundry/responsible-ai/... (citada aqui pela URL final); o SLA do Google não traz data própria (rodapé "Previous versions (Last modified January 9, 2020)").
8. Registro do QA (R1), sem alteração de texto: (a) R116: o critério da nota é o da Microsoft para os próprios modelos e inclui a condição de recursos e latência, que o item omite sem mudar o gabarito; (b) a frase do curso da 2.8 ("adaptação não corrige sotaque nem ruído") e o aspecto (xv) do padrão de resposta são objeto da errata proposta pelo QA (seção 7 do parecer; D1 da gce-gerencia; propagação ao pacote v1.10, T-104); não faz parte deste arquivo.

## 1.5 Formatos, VOLÁTEIS e gabarito por folha de 20

Formatos da folha P2-2.7 (20 itens = 6 existentes + 14 novos; teto de 30% = 6 por formato):
| formato | existentes | novos | total | % |
|---|---|---|---|---|
| definição (D) | Q25, Q27 | — | 2 | 10% |
| troca de sujeito (TSj) | — | R103, R107, R108, R113 | 4 | 20% |
| situação hipotética (SH) | Q26 | R105, R106, R109, R116 | 5 | 25% |
| número ou prazo (NP) | R15 | R110 | 2 | 10% |
| par confundível (PC) | Q24 | R111, R115 | 3 | 15% |
| aplicação parlamentar (AP) | R14 | R104, R112, R114 | 4 | 20% |
| soma | 6 | 14 | 20 | 100% |
Maior formato: situação hipotética (SH) com 25% (teto de 30% cumprido). Sem item novo de definição (D): o legado de 2/6 (Q25, Q27) cai para 2/20 = 10% (diluição pedida na T90_reconciliacao, seção 4). VOLÁTIL da folha: 0/20 (nenhum existente, nenhum novo).

Formatos da folha P2-2.8 (20 itens = 6 existentes + 14 novos; teto de 30% = 6 por formato):
| formato | existentes | novos | total | % |
|---|---|---|---|---|
| definição (D) | R16 | R118, R127, R128 | 4 | 20% |
| troca de sujeito (TSj) | R17 | R117, R119, R123, R126 | 5 | 25% |
| situação hipotética (SH) | Q30 | R120, R121, R125 | 4 | 20% |
| número ou prazo (NP) | R18 | — | 1 | 5% |
| par confundível (PC) | Q29 | R124, R129, R130 | 4 | 20% |
| aplicação parlamentar (AP) | Q28 | R122 | 2 | 10% |
| soma | 6 | 14 | 20 | 100% |
Maior formato: troca de sujeito (TSj) com 25% (teto de 30% cumprido). VOLÁTIL da folha: R18 (existente, risco alto), R120, R121 e R125 (novos, risco baixo) = 4/20 = 20% (no teto de 20%; nenhum novo de risco alto). R118 reclassificado de AP para D na R2 (não tem aplicação parlamentar).

Gabarito da P2-2.7: novos 7 C / 7 E; com os 6 existentes (2 C / 4 E), a folha fecha em 9 C / 11 E (45% de C).
Gabarito da P2-2.8: novos 7 C / 7 E; com os 6 existentes (2 C / 4 E), a folha fecha em 9 C / 11 E (45% de C).
Gabarito da parte D: 14 C / 14 E = 50,0% de C (faixa de 40% a 60%, regra 5). [TS]: 18 de 28 (meta: 16 ou mais), sendo 13 em itens E e 5 em itens C (convenção "espelho" da GCE, O-6). VOLÁTEIS novos da parte: 3 (R120, R121, R125), nenhum de risco alto.

FIM DA PARTE 1/3

=====================================================================
PARTE 2/3 — (d) ITENS DO ESTUDANTE
=====================================================================

L2-R103. Julgue o item.
Ao preparar a medição da acurácia de um serviço de ASR para as reuniões de comissão, a equipe da Câmara consulta a documentação do Google Cloud Speech-to-Text, segundo a qual a transcrição de referência (ground truth) costuma ser obtida por transcrição feita por outro sistema automático, em passagem única ou dupla.

L2-R104. Julgue o item.
A equipe da Câmara calcula o WER do ASR usado nas comissões. Segundo a documentação do Google Cloud Speech-to-Text, a transcrição de referência deve ter convenções, como as de pontuação, números e capitalização, o mais próximas possível das do sistema avaliado, pois não existe formato de transcrição único aceito por todos.

L2-R105. Julgue o item.
A equipe da Câmara notou que a confiança atribuída pelo ASR às transcrições das reuniões é alta e concluiu que o WER será baixo. Essa conclusão não se sustenta, porque, segundo a documentação do Google Cloud Speech-to-Text, WER e confiança são métricas independentes, sem correlação esperada.

L2-R106. Julgue o item.
A Câmara contratou o Google Cloud Speech-to-Text para transcrever reuniões de comissão e entende que o SLA do serviço, ao fixar o percentual mensal de tempo de atividade, assegura uma taxa máxima de erros de palavras nas transcrições entregues, de modo que a equipe poderia dispensar a auditoria de amostras. Nessa situação, o entendimento da Câmara está correto.

L2-R107. Julgue o item.
De acordo com o SLA do Google Cloud Speech-to-Text, o descumprimento do objetivo de nível de serviço dá ao cliente que cumpra as exigências do acordo direito a crédito financeiro em faturas futuras, e o próprio acordo declara esse crédito como o único e exclusivo remédio do cliente para a falha.

L2-R108. Julgue o item.
A equipe da Câmara usa o teste de inspeção de qualidade do Azure Speech, com dados somente de áudio, para examinar a transcrição automática de reuniões de comissão. Segundo a documentação do serviço, a decisão sobre a correção do resultado do reconhecimento é tomada automaticamente pelo serviço, e a equipe não precisa reproduzir o áudio carregado.

L2-R109. Julgue o item.
O sistema da Câmara que envia áudios ao Google Cloud Speech-to-Text passou a receber respostas de erro porque as suas requisições continham campos inválidos. Segundo o SLA do serviço, esses erros devem ser computados como indisponibilidade no cálculo do percentual mensal de tempo de atividade, ainda que as requisições não estivessem de acordo com a documentação.

L2-R110. Julgue o item.
Em um mês de 30 dias, um serviço de reconhecimento de fala somou 432 minutos de indisponibilidade. Pelo cálculo do percentual mensal de tempo de atividade adotado no SLA do Google Cloud Speech-to-Text (minutos do mês menos minutos de indisponibilidade, divididos pelos minutos do mês), esse percentual foi de 99%.

L2-R111. Julgue o item.
A equipe da Câmara prepara transcrições das reuniões de comissão para avaliar e para melhorar um modelo do Azure Speech. Segundo a documentação do serviço sobre transcrições rotuladas por pessoas, para avaliar a acurácia recomenda-se uma grande amostra, ao passo que, para melhorar o reconhecimento, basta uma amostra representativa dos locutores e das falas dos usuários.

L2-R112. Julgue o item.
Na avaliação de transcrições automáticas de sessões, o sclite, do NIST, totaliza os erros por locutor e por par de referência e hipótese, o que permite à equipe de qualidade identificar os oradores cujas falas o sistema transcreve pior e orientar a auditoria para elas.

L2-R113. Julgue o item.
Com referência e hipótese em formato trn e alinhamento por programação dinâmica, o sclite pontua apenas as falas identificadas no arquivo de hipótese, de modo que o arquivo de referência pode conter registros a mais, o que permite pontuar somente uma parte das falas.

L2-R114. Julgue o item.
Em um teste do Azure Speech com gravações de várias comissões, o valor global do WER basta para direcionar as melhorias, dispensando a análise da distribuição dos erros.

L2-R115. Julgue o item.
Para medir quantitativamente o WER de um modelo no Azure Speech, a equipe da Câmara pode usar gravações de reuniões em áudio sem as transcrições de referência produzidas por pessoas, pois os dados somente de áudio servem à avaliação quantitativa da acurácia do modelo avaliado.

L2-R116. Julgue o item.
Quando decide se substitui a versão do modelo de ASR em uso nas comissões, a equipe da Câmara só aprova o novo modelo se ele apresentar melhorias significativas em todos os cenários avaliados, e não apenas em alguns, critério que corresponde ao descrito na nota de transparência do Azure Speech.

L2-R117. Julgue o item.
No Google Cloud Speech-to-Text, ao se incluir na adaptação do modelo uma expressão de várias palavras, como questão de ordem, aumenta-se a probabilidade de a expressão ser reconhecida por inteiro, sem efeito sobre a probabilidade de reconhecimento das palavras que a compõem, tomadas isoladamente.

L2-R118. Julgue o item.
Para reconhecer melhor valores monetários e datas que variam a cada fala, a adaptação de modelo do Google Cloud Speech-to-Text oferece classes, cuja disponibilidade depende do modelo e do idioma, que agrupam palavras de um conceito comum e dispensam listar cada valor, independentemente de quais sejam ditos.

L2-R119. Julgue o item.
No Google Cloud Speech-to-Text, a classe personalizada, formada por lista de itens definida pelo usuário, como os nomes dos municípios de um estado, funciona como as classes predefinidas, e uma mesma frase de adaptação pode combinar classes predefinidas e personalizadas.

L2-R120. Julgue o item.
Considere que a equipe da Câmara digitou de forma incorreta o token de uma classe em uma frase de adaptação do Google Cloud Speech-to-Text. Nessa situação, o serviço ignora o token malformado, sem gerar erro, mas ainda usa o restante da frase como contexto.

L2-R121. Julgue o item.
Uma equipe da Câmara pretende degravar sessões já gravadas com a API de transcrição em lote do Azure Speech e supõe que a lista de frases (phrase list), por não exigir treinamento de modelo, também pode ser usada nesse modo para favorecer o reconhecimento de nomes de parlamentares. Nessa situação, a suposição da equipe está correta.

L2-R122. Julgue o item.
Em reunião cuja pauta e cujos oradores inscritos são conhecidos de antemão, a equipe pode prever os nomes e termos que serão falados. Nesse caso, a nota de transparência do Azure Speech sugere a lista de frases para favorecer esses termos e, se a acurácia permanecer baixa, o custom speech.

L2-R123. Julgue o item.
Na criação de um modelo de linguagem personalizado no Amazon Transcribe com dados de treinamento e de ajuste (tuning), a equipe da Câmara deve usar os mesmos textos nos dois conjuntos, pois a sobreposição reforça o aprendizado dos termos das comissões e não prejudica a acurácia do modelo.

L2-R124. Julgue o item.
No Amazon Transcribe, ao contrário dos dados de treinamento, que ensinam o modelo de linguagem personalizado a reconhecer novos termos e o contexto em que são usados, os dados de ajuste não são obrigatórios e são recomendados quando faltam dados de treinamento do próprio domínio.

L2-R125. Julgue o item.
Uma equipe da Câmara criou o vocabulário personalizado com siglas e nomes de comissões no Amazon Transcribe em uma região da AWS e pretende iniciar a transcrição em outra região. Nessa situação, o vocabulário poderá ser usado, independentemente da região em que foi criado.

L2-R126. Julgue o item.
Um modelo personalizado do Azure Speech, implantado em ponto de extremidade próprio, permanece fixo até que o usuário decida atualizá-lo, de modo que, ainda que seja lançado um novo modelo base, enquanto vigente o modelo mantém sua acurácia e o desempenho com o vocabulário adaptado.

L2-R127. Julgue o item.
Em sessão do Plenário, um Deputado formulou uma questão de ordem. Segundo o Regimento Interno da Câmara dos Deputados, questão de ordem é toda dúvida sobre a interpretação do Regimento, na sua prática exclusiva ou relacionada com a Constituição Federal.

L2-R128. Julgue o item.
Ao revisar a nota taquigráfica de uma reunião de comissão, o revisor encontra o termo parecer. Segundo o Regimento Interno da Câmara dos Deputados, parecer é a proposição com que o Plenário se pronuncia sobre qualquer matéria sujeita a seu estudo.

L2-R129. Julgue o item.
Ao revisar uma nota taquigráfica sobre emendas, o revisor encontra a expressão emenda de redação. Segundo o Regimento Interno da Câmara dos Deputados, emenda de redação é a emenda aditiva que visa a sanar vício de linguagem, incorreção de técnica legislativa ou lapso manifesto.

L2-R130. Julgue o item.
Nas sessões ordinárias do Plenário, segundo o Regimento Interno da Câmara dos Deputados, as Comunicações Parlamentares destinam-se aos Líderes que queiram fazer uso da palavra, por período de tempo proporcional ao número de membros das respectivas bancadas.

FIM DA PARTE 2/3

=====================================================================
PARTE 3/3 — (d-G) GABARITO COMENTADO
=====================================================================
Legenda: [TS] = troca sutil de um único conceito (em item C, a convenção "espelho" da GCE: a versão verdadeira de uma troca sutil). VOLÁTIL = gabarito depende de fato mutável de serviço (critério da D-T96-ONDA2-ACEITE (II)); inapto a simulado final até a reverificação de 4–8/1/2027. REVERIFICAR = reabrir a URL da base e conferir o trecho em 4–8/1/2027 (conferência de base, sem efeito de VOLÁTIL). Todas as páginas foram abertas em 18/10/2026. QA PENDENTE em todos.

### P2-2.7

L2-R103. E [TS]. REVERIFICAR. A documentação indica que a referência costuma ser obtida por transcrição humana, em passagem única ou dupla, para ser uma transcrição precisa contra a qual se medem os resultados automáticos.
Troca sutil: transcrição humana por transcrição de outro sistema automático. O item não afirma que a passagem dupla seja feita por dois revisores independentes.
Base: Google Cloud, Speech-to-Text, "Measure and improve speech accuracy", seção "Measuring speech accuracy" (Get ground truth transcriptions): https://docs.cloud.google.com/speech-to-text/docs/v1/speech-accuracy, verificado em 18/10/2026 (página com "Last updated 2026-10-13 UTC"; a URL /docs/speech-accuracy redireciona para esta): "Get accurate transcriptions of the audio. This usually involves a single or a double-pass human transcription of the target audio."

L2-R104. C. REVERIFICAR. A documentação do Google orienta que a referência siga, o mais possível, as convenções do sistema avaliado (pontuação, números, capitalização), porque não há um formato de transcrição único aceito por todos para o mesmo áudio.
O item atribui a orientação à documentação do Google (R1 do QA) e pede o cuidado na elaboração da referência; não cobra o conjunto de convenções da página, que é detalhado e específico do Google.
Base: Google Cloud, Speech-to-Text, "Measure and improve speech accuracy", seções "Ground-truth conventions" e "Measuring speech accuracy": https://docs.cloud.google.com/speech-to-text/docs/v1/speech-accuracy, verificado em 18/10/2026: "It's important when getting ground truth transcriptions to match the transcription conventions of your target ASR system as closely as possible. For example, ensure that punctuation, numbers, and capitalization are consistent."; "It is important to recognize that there isn't a single human-agreed transcription format for any given audio."

L2-R105. C. REVERIFICAR. A confiança se baseia em verossimilhança, e o WER, em a palavra estar ou não correta; por isso as métricas são independentes e não se deve esperar correlação entre elas.
A conclusão da equipe passa da confiança ao WER sem base; a confiança pode orientar a revisão, mas não substitui a medição do WER contra uma referência.
Base: Google Cloud, Speech-to-Text, "Measure and improve speech accuracy", seção "Relation of WER to a confidence score": https://docs.cloud.google.com/speech-to-text/docs/v1/speech-accuracy, verificado em 18/10/2026: "The WER metric is independent from a confidence score, and they usually don't correlate with each other."; "In summary, the confidence and WER metrics are independent and shouldn't be expected to correlate."

L2-R106. E [TS]. REVERIFICAR. O objetivo do SLA é o percentual mensal de tempo de atividade, calculado a partir de respostas de erro do servidor; ele não fixa taxa de erros de palavras.
Troca sutil: disponibilidade do serviço por qualidade (acurácia) da transcrição. A qualidade continua dependendo de revisão e auditoria.
Base: Google Cloud, "Speech-to-Text Service Level Agreement (SLA)": https://cloud.google.com/speech-to-text/sla, verificado em 18/10/2026 (página sem data própria; rodapé "Previous versions (Last modified January 9, 2020)"): "the Covered Service will provide a Monthly Uptime Percentage to Customer"; ""Error Rate" means the number of Valid Requests that result in a response with HTTP Status 500 and Code "Internal Error" divided by the total number of Valid Requests during that period."

L2-R107. C [TS]. REVERIFICAR. O SLA prevê crédito financeiro em faturas futuras e afirma que ele é o único e exclusivo remédio do cliente para o descumprimento do objetivo.
Espelho de [TS]: a versão verdadeira de "o crédito é cumulável com outros remédios" (exclusivo por cumulativo).
Base: Google Cloud, SLA do Speech-to-Text: https://cloud.google.com/speech-to-text/sla, verificado em 18/10/2026: "This SLA states Customer’s sole and exclusive remedy for any failure by Google to meet the SLO."; "Financial Credits will be made in the form of a monetary credit applied to future use of the Service"

L2-R108. E [TS]. REVERIFICAR. Na inspeção de qualidade com dados somente de áudio, a pessoa reproduz o áudio carregado e determina se o resultado do reconhecimento fornecido está correto; a decisão não é tomada automaticamente pelo serviço.
Troca sutil: pessoa que reproduz o áudio e julga o resultado por serviço que decide sozinho. O item não cobra o passo a passo do portal nem a comparação entre dois modelos.
Base: Microsoft, "Test recognition quality of a custom speech model": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-inspect-data, verificado em 18/10/2026 (metadado ms.date 2025-12-29): "You can play back uploaded audio and determine if the provided recognition result is correct."

L2-R109. E [TS]. REVERIFICAR. O SLA exclui os erros resultantes de uso do serviço em desacordo com a documentação, inclusive campos inválidos na requisição; só requisições válidas entram no cálculo.
Troca sutil: erro excluído do cálculo por erro computado como indisponibilidade.
Base: Google Cloud, SLA do Speech-to-Text, seção "SLA exclusions": https://cloud.google.com/speech-to-text/sla, verificado em 18/10/2026: "(v) that resulted from Customer use of the Covered Service inconsistent with the Documentation, including but not limited to invalid request fields, unauthorized users, or inaccessible data."

L2-R110. C. REVERIFICAR. Um mês de 30 dias tem 43.200 minutos; (43.200 − 432) ÷ 43.200 = 0,99, isto é, 99%.
O item usa só a fórmula do SLA, sem o objetivo numérico do fornecedor, que não é cobrado.
Base: Google Cloud, SLA do Speech-to-Text, definição de "Monthly Uptime Percentage" (só a fórmula; nenhum objetivo numérico é cobrado): https://cloud.google.com/speech-to-text/sla, verificado em 18/10/2026: ""Monthly Uptime Percentage" means total number of minutes in a month, minus the number of minutes of Downtime suffered from all Downtime Periods in a month, divided by the total number of minutes in a month."

L2-R111. E [TS]. REVERIFICAR. Para avaliar a acurácia, a documentação recomenda amostra representativa, que cubra vários locutores e falas típicas dos usuários; para melhorar o reconhecimento, exige amostra grande.
Troca sutil: as finalidades das duas amostras trocadas (grande para avaliar; representativa para melhorar). Nenhum número de horas ou de segundos da página é cobrado.
Base: Microsoft, "How to create human-labeled transcriptions" (Human-labeled transcriptions guidelines): https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-human-labeled-transcriptions, verificado em 18/10/2026 (metadado ms.date 2025-12-29): "A representative sample of transcription data is recommended to evaluate model accuracy. The data should cover various speakers and utterances that are representative of what users say to the application."; "A large sample of transcription data is required to improve recognition."

L2-R112. C. REVERIFICAR. O sclite tabula os erros por locutor e por par referência–hipótese; a quebra por locutor permite ver onde o sistema falha mais.
A conclusão sobre direcionar a auditoria é aplicação do item ao registro de sessões, sem número, versão ou preço.
Base: NIST SCTK, documentação do sclite, seção "The scoring process": https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm, verificado em 18/10/2026 (documentação sem data própria na página): "scores are tallied for each speaker and each ref/hyp pair"

L2-R113. C [TS]. REVERIFICAR. Só os identificadores de fala presentes na hipótese são alinhados e pontuados; a referência pode ter mais registros, o que viabiliza pontuar só uma amostra.
Espelho de [TS]: a versão verdadeira de "só as falas da referência são pontuadas" (hipótese por referência).
Base: NIST SCTK, documentação do sclite, seção "The alignment process", "Utterance ID Matching": https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm, verificado em 18/10/2026: "Only the utterance ID's present in the HYP file are aligned and scored. This means the REF file may contain more utterance records than the HYP."

L2-R114. E. REVERIFICAR. A documentação ressalta que a distribuição dos erros importa e que a análise por arquivo mostra os tipos de erro próprios de cada um e ajuda a direcionar a melhoria.
Erro por generalização: o valor global esconde onde e como o sistema falha.
Base: Microsoft, "Test accuracy of a custom speech model", seção "Resolve errors and improve WER": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data, verificado em 18/10/2026 (página com "Last updated on 2025-12-29"): "How the errors are distributed is important."; "By analyzing individual files, you can determine what type of errors exist and which errors are unique to a specific file. Understanding problems at the file level helps you target improvements."

L2-R115. E [TS]. REVERIFICAR. Áudio sem transcrição serve para inspecionar a acurácia; para quantificá-la, usam-se áudio e transcrições rotuladas por pessoas.
Troca sutil: inspeção qualitativa (só áudio) por avaliação quantitativa.
Base: Microsoft, "Test and train data for custom speech", seção "Audio data for training or testing": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-test-and-train, verificado em 18/10/2026 (página com "Last updated on 2025-12-19"; confirmado também em custom-speech-overview ("Last updated on 2026-02-25")): "audio data is used to inspect the accuracy of speech regarding a specific model's performance. If you want to quantify the accuracy of a model, use audio + human-labeled transcripts."

L2-R116. C [TS]. REVERIFICAR. O critério descrito na nota considera melhor o modelo que mostra melhorias significativas em todos os cenários avaliados, e não em apenas alguns; serve de exemplo de controle de qualidade na troca de versão.
Espelho de [TS]: a versão verdadeira de "basta melhorar em um dos cenários" (todos por apenas alguns). O percentual citado na página não é cobrado.
Base: Microsoft, nota de transparência do Azure Speech (speech to text), seção "System performance": https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note, verificado em 18/10/2026 (página com "Last updated on 2026-03-31"): "A model is considered better only when it shows significant improvements [...] in all scenarios [...]"

### P2-2.8

L2-R117. E [TS]. REVERIFICAR. Com uma frase de várias palavras, o serviço tende a reconhecê-las em sequência e também aumenta a probabilidade de reconhecer partes da frase, inclusive palavras individuais.
Troca sutil: efeito também sobre as palavras isoladas por efeito apenas sobre a expressão inteira.
Base: Google Cloud, Speech-to-Text, "Improve transcription results with model adaptation", seção "Improve recognition of words and phrases": https://docs.cloud.google.com/speech-to-text/docs/adaptation-model, verificado em 18/10/2026 (página com "Last updated 2026-10-13 UTC"): "When you provide a multi-word phrase, Speech-to-Text is more likely to recognize those words in sequence. Providing a phrase also increases the probability of recognizing portions of the phrase, including individual words."

L2-R118. C. REVERIFICAR. Classes servem a grandes grupos de palavras que remetem a um conceito comum sem serem idênticas, como unidades monetárias e datas; listar todos os valores seria impraticável.
O item ressalva que a disponibilidade varia por modelo e idioma e não afirma suporte ao português. Formato D (reclassificado de AP na R1: o item não tem aplicação parlamentar). Não VOLÁTIL: o ponto julgado é o mecanismo da classe, com a condição de disponibilidade já ressalvada no enunciado (T96, seção 2.2); registro expresso pedido à Gerência.
Base: Google Cloud, Speech-to-Text, "Improve transcription results with model adaptation", seção "Improve recognition using classes": https://docs.cloud.google.com/speech-to-text/docs/adaptation-model, verificado em 18/10/2026: "A class helps you improve transcription accuracy for large groups of words that map to a common concept, but that don't always include identical words or phrases."; "Note: Class availability varies by transcription model and language."

L2-R119. C [TS]. REVERIFICAR. A classe personalizada reúne itens do usuário (a página dá como exemplo nomes de restaurantes) e funciona como os tokens predefinidos; uma frase pode usar os dois tipos.
Espelho de [TS]: a versão verdadeira de "não pode ser combinada com as predefinidas".
Base: Google Cloud, Speech-to-Text, "Improve transcription results with model adaptation", seção "Custom classes": https://docs.cloud.google.com/speech-to-text/docs/adaptation-model, verificado em 18/10/2026: "Custom classes function in the same way as the pre-built class tokens."; "A phrase can include both prebuilt class tokens and custom classes."

L2-R120. C. VOLÁTIL (baixo). REVERIFICAR. O serviço ignora o token inválido sem acionar erro e aproveita o resto da frase como contexto; a falha é silenciosa.
VOLÁTIL (BAIXO): depende do comportamento do serviço diante de entrada inválida, que pode mudar (critério (b) da D-T96-ONDA2-ACEITE).
Base: Google Cloud, Speech-to-Text, "Improve transcription results with model adaptation", seção "Class tokens": https://docs.cloud.google.com/speech-to-text/docs/adaptation-model, verificado em 18/10/2026: "If you use an invalid or malformed class token, Speech-to-Text ignores the token without triggering an error but still uses the rest of the phrase for context."

L2-R121. E [TS]. VOLÁTIL (baixo). REVERIFICAR. A lista de frases é recurso de tempo de execução, não exige treinamento, mas não é suportada pela API de transcrição em lote.
Troca sutil: modo em que o recurso está disponível (tempo real e transcrição rápida, mas não lote). VOLÁTIL (BAIXO): disponibilidade de recurso por modo de uso (critério (c)).
Base: Microsoft, "Improve recognition accuracy with phrase list": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/improve-accuracy-phrase-list, verificado em 18/10/2026 (página com "Last updated on 2026-06-29"): "It doesn't require model training and isn't available with batch transcription."; "The Batch transcription API doesn't support phrase lists."

L2-R122. C. REVERIFICAR. A nota sugere a lista de frases quando se pode antecipar o que será falado, e a personalização por custom speech quando a acurácia continua baixa.
A pauta e os oradores inscritos são a ambientação parlamentar, fora do escopo da remissão.
Base: Microsoft, nota de transparência do Azure Speech, seção "Best practices for improving system performance", itens "Add custom vocabularies" e "Use custom speech": https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note, verificado em 18/10/2026 (página com "Last updated on 2026-03-31"): "If you can anticipate which words and phrases will be spoken (for instance, when a user selects an item from a list), you might want to use the phrasal list grammar."; "Use custom speech: If speech to text accuracy in your application scenarios remains low, you might want to consider customizing the model for your acoustic and linguistic variations."

L2-R123. E [TS]. REVERIFICAR. Ao usar os dois tipos de dados, não se deve sobrepô-los: treinamento e ajuste devem ser distintos, porque a sobreposição pode enviesar o modelo e afetar a acurácia.
Troca sutil: conjuntos distintos por mesmos textos nos dois conjuntos.
Base: AWS, Amazon Transcribe, "Custom language models", seção "Training versus tuning data": https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html, verificado em 18/10/2026 (página sem data própria): "If you choose to include both data types, do not overlap your training and tuning data; training and tuning data should be unique. Overlapping data can bias and skew your custom language model, impacting its accuracy."

L2-R124. C. REVERIFICAR. Os dados de treinamento ensinam termos e contexto; os de ajuste refinam as relações aprendidas, não são exigidos e são recomendados na falta de dados de treinamento do próprio domínio.
Par confundível: treinamento (necessário) por ajuste (opcional). O texto do item segue a forma literal da página (R1 do QA): a falta é de dados de treinamento do domínio, e não de transcrições precisas.
Base: AWS, Amazon Transcribe, "Custom language models", seções "Data sources" e "Training versus tuning data": https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html, verificado em 18/10/2026: "Tuning data are not required to create a custom language model."; "Tuning data are recommended when you lack in-domain training data."

L2-R125. E [TS]. VOLÁTIL (baixo). REVERIFICAR. Para usar um vocabulário personalizado, ele deve ter sido criado na mesma região da AWS da transcrição.
Troca sutil: mesma região por qualquer região. VOLÁTIL (BAIXO): a utilização do recurso é condicionada pela documentação à região em que foi criado (critério (c) da D-T96-ONDA2-ACEITE; marca acrescentada na R2 por determinação do QA).
Base: AWS, Amazon Transcribe, "Custom vocabularies": https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html, verificado em 18/10/2026 (página sem data própria): "To use a custom vocabulary, it must have been created in the same AWS Region as your transcription."

L2-R126. C [TS]. REVERIFICAR. O modelo implantado em endpoint próprio é fixo até a decisão do usuário e mantém acurácia e qualidade mesmo com novo modelo base, o que preserva o vocabulário adaptado; vale pelo período de vigência do modelo.
Espelho de [TS]: a versão verdadeira de "é atualizado automaticamente para o novo modelo base".
Base: Microsoft, "What is custom speech?", seção "Model stability and lifecycle": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-speech-overview, verificado em 18/10/2026 (página com "Last updated on 2026-02-25"): "A base model or custom model deployed to an endpoint using custom speech is fixed until you decide to update it. The speech recognition accuracy and quality remain consistent, even when a new base model is released."; "you can use the model for a limited time"

L2-R127. C. REVERIFICAR. O art. 95 considera questão de ordem toda dúvida sobre a interpretação do Regimento, na sua prática exclusiva ou relacionada com a Constituição Federal.
Termo do vocabulário técnico parlamentar que o revisor encontra nas notas taquigráficas; o item cobra a definição regimental. CONFERE (qa-normativo, 18/10/2026).
Base: RICD, art. 95, caput, no Legin: https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html, verificado em 18/10/2026 (Legin, texto atualizado): "Considera-se questão de ordem toda dúvida sobre a interpretação deste Regimento, na sua prática exclusiva ou relacionada com a Constituição Federal."

L2-R128. E [TS]. REVERIFICAR. O art. 126 define parecer como a proposição com que uma Comissão se pronuncia sobre qualquer matéria sujeita a seu estudo.
Troca sutil: Comissão por Plenário. Termo do vocabulário técnico parlamentar que o revisor encontra nas notas taquigráficas de reuniões de comissão; o item cobra a definição regimental. PENDENTE NORMATIVO (item novo).
Base: RICD, art. 126, caput, no Legin: https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html, verificado em 18/10/2026 (Legin, texto atualizado; sem marcação de alteração): "Parecer é a proposição com que uma Comissão se pronuncia sobre qualquer matéria sujeita a seu estudo."

L2-R129. E [TS]. REVERIFICAR. O § 8º do art. 118 denomina emenda de redação a modificativa que visa a sanar vício de linguagem, incorreção de técnica legislativa ou lapso manifesto; a aditiva é a que se acrescenta a outra proposição (§ 6º).
Troca sutil: modificativa por aditiva. CONFERE (qa-normativo, 18/10/2026).
Base: RICD, art. 118, §§ 6º e 8º, no Legin: https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html, verificado em 18/10/2026 (Legin, texto atualizado): "Denomina-se emenda de redação a modificativa que visa a sanar vício de linguagem, incorreção de técnica legislativa ou lapso manifesto."

L2-R130. E [TS]. REVERIFICAR. As Comunicações de Lideranças (art. 89, a que remete o art. 66, § 1º) destinam-se aos Líderes, por tempo proporcional às bancadas; as Comunicações Parlamentares (arts. 66, IV, e 90) cabem a oradores indicados pelos Líderes, chamados alternadamente por Partidos e Blocos (art. 90, parágrafo único).
Troca sutil: o nome Comunicações de Lideranças por Comunicações Parlamentares. Aderência PARCIAL (proposta do QA; D1 da gce-gerencia): só simulado diagnóstico (D-ADERENCIA). CONFERE (qa-normativo, 18/10/2026).
Base: RICD, arts. 66, IV e § 1º, 89, caput, e 90, caput e parágrafo único, no Legin: https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html, verificado em 18/10/2026 (Legin, texto atualizado): "As Comunicações de Lideranças [...] destinam-se aos Líderes que queiram fazer uso da palavra, por período de tempo proporcional ao número de membros das respectivas bancadas"; "Comunicações Parlamentares, desde que haja tempo, destinadas a representantes de Partidos e Blocos Parlamentares, alternadamente, indicados pelos Líderes"; "Os oradores serão chamados, alternadamente, por Partidos e Blocos Parlamentares, por período não excedente a dez minutos para cada Deputado."

## Contagens
| quesito | valor |
|---|---|
| total | 28 (P2-2.7: 14; P2-2.8: 14) |
| C | 14 (P2-2.7: R104, R105, R107, R110, R112, R113, R116; P2-2.8: R118, R119, R120, R122, R124, R126, R127) = 50,0% (faixa de 40% a 60% cumprida); por folha: 2.7 com 7 C / 7 E; 2.8 com 7 C / 7 E |
| E | 14 (P2-2.7: R103, R106, R108, R109, R111, R114, R115; P2-2.8: R117, R121, R123, R125, R128, R129, R130) |
| [TS] | 18 de 28 = 64,3% (meta: 16 ou mais, cumprida): P2-2.7: R103, R106, R107, R108, R109, R111, R113, R115, R116 (9); P2-2.8: R117, R119, R121, R123, R125, R126, R128, R129, R130 (9) |
| [TS] com gabarito C | 5 (R107, R113, R116, R119, R126), por convenção "espelho", cada um com a troca do espelho declarada na justificativa; sem relação fixa entre [TS] e gabarito. Só em itens E: 13 de 14 |
| VOLÁTIL | 3 novos, todos em P2-2.8: R120, R121 e R125 (risco baixo); risco alto novo 0. P2-2.7: 0 novos |
| VOLÁTIL por folha de 20 | P2-2.7: 0/20 = 0%; P2-2.8: R18, R120, R121, R125 = 4/20 = 20% (no teto) |
| formato máximo por folha de 20 | P2-2.7: 25% (SH com 5; TSj com 4); P2-2.8: 25% (TSj com 5; D com 4 = 20%) |
| aderência | 27 DIRETA; 1 PARCIAL (R130, proposta do QA, D-ADERENCIA: só simulado diagnóstico); 0 PARCIAL novos na 2.7 (legado: R14, R15) |
| REVERIFICAR (4–8/1/2027) | 28 (base em página de fornecedor ou no Legin); 3 desses também VOLÁTEIS (R120, R121, R125) |
| extensão (palavras do enunciado) | C: média 46.3 (de 40 a 51); E: média 47.4 (de 28 a 58); nenhum C acima de 65 palavras (O-1) |

Observações de estilo (registros O-1 a O-8 da T-93 e recomendações do estilo_onda_2.md):
- O-1 (extensão): C com média 46.3 e E com média 47.4 palavras; a diferença é de 1.1 palavra, sem pista de extensão; o E mais longo (R106, 58 palavras) supera o C mais longo (R104, 51).
- O-2 ("independe"): em C: R118; em E: R125. Presente nos dois gabaritos, como pedido na recomendação 1.
- O-3 ("pode/poderá"): em C: R113, R119, R122; em E: R115, R121, R125.
- O-4 (remissão): nas remissões a documentação ou norma ("Segundo", "De acordo com", "a nota de transparência sugere", "conforme"), a ambientação parlamentar (reuniões de comissão, pauta, oradores inscritos, sessão do Plenário) fica fora do escopo da remissão, em frase própria ou no sujeito (na v2, R104, R108, R111 e R128 passaram a separar a ambientação da remissão em frase própria; R104 passou a atribuir a orientação à documentação do Google).
- O-5 (cauda que se denuncia): não há cauda falsa autocontraditória (o R103 foi escrito sem a cauda "para que a referência seja precisa", que denunciaria a troca); os erros são trocas de conceito, de sujeito, de número ou de condição. Nenhum E empilha absolutos: R115 tem um "somente".
- O-6 ([TS] em C): R107, R113, R116, R119, R126 são C com espelho declarado.
- O-7 (restritivos e causais): "apenas" em C: R113, R116; em E: nenhum. "somente" em C: R113; em E: R115. "só" restritivo em C: R116. "pois" em C: R104; em E: R115, R123. "porque" em C: R105; em E: R109.
- O-8 (concessiva): "ainda que" em C: R126; em E: R109; alternada entre os dois gabaritos.
- Aberturas (recomendação 3): "Segundo" abre nenhum item; "De acordo com" abre R107; os demais abrem com sujeito, circunstância ou "Considere que"; não há concentração de "Segundo a…".

## Tabela de proveniência (todas abertas e lidas em 18/10/2026)
| fonte | URL oficial | data da página / verificação | usada em |
|---|---|---|---|
| Google Cloud, Speech-to-Text, Measure and improve speech accuracy | https://docs.cloud.google.com/speech-to-text/docs/v1/speech-accuracy | página com "Last updated 2026-10-13 UTC"; a URL /docs/speech-accuracy redireciona para esta; verificado em 18/10/2026 (HTTP 200); seções "Relation of WER to a confidence score", "Ground-truth conventions" e "Measuring speech accuracy"; a URL /docs/speech-accuracy redireciona para esta | R103, R104, R105 |
| Google Cloud, Speech-to-Text Service Level Agreement (SLA) | https://cloud.google.com/speech-to-text/sla | página sem data própria; rodapé "Previous versions (Last modified January 9, 2020)"; verificado em 18/10/2026 (HTTP 200) | R106, R107, R109, R110 |
| NIST, SCTK, documentação do sclite (repositório oficial usnistgov/SCTK, arquivo bruto) | https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm | documentação sem data própria na página; verificado em 18/10/2026 (HTTP 200) | R112, R113 |
| Microsoft, Azure Speech, Test accuracy of a custom speech model | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | página com "Last updated on 2025-12-29"; verificado em 18/10/2026 (HTTP 200) | R114 |
| Microsoft, Azure Speech, Test recognition quality of a custom speech model | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-inspect-data | metadado ms.date 2025-12-29; verificado em 18/10/2026 (HTTP 200) | R108 |
| Microsoft, Azure Speech, How to create human-labeled transcriptions (Human-labeled transcriptions guidelines) | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-human-labeled-transcriptions | metadado ms.date 2025-12-29; verificado em 18/10/2026 (HTTP 200) | R111 |
| Microsoft, Azure Speech, Test and train data for custom speech | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-test-and-train | página com "Last updated on 2025-12-19"; confirmado também em custom-speech-overview ("Last updated on 2026-02-25"); verificado em 18/10/2026 (HTTP 200) | R115 |
| Microsoft, Azure Speech, nota de transparência de speech to text (Use cases for Speech to text) | https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note | página com "Last updated on 2026-03-31"; verificado em 18/10/2026 (HTTP 200); seções "Evaluating and integrating speech to text for your use", "Best practices for improving system performance" e "Guidance for integration and responsible use" | R116, R122 |
| Google Cloud, Speech-to-Text, Improve transcription results with model adaptation | https://docs.cloud.google.com/speech-to-text/docs/adaptation-model | página com "Last updated 2026-10-13 UTC"; verificado em 18/10/2026 (HTTP 200) | R117, R118, R119, R120 |
| Microsoft, Azure Speech, Improve recognition accuracy with phrase list | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/improve-accuracy-phrase-list | página com "Last updated on 2026-06-29"; verificado em 18/10/2026 (HTTP 200) | R121 |
| AWS, Amazon Transcribe, Custom language models | https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html | página sem data própria; verificado em 18/10/2026 (HTTP 200) | R123, R124 |
| AWS, Amazon Transcribe, Custom vocabularies | https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html | página sem data própria; verificado em 18/10/2026 (HTTP 200) | R125 |
| Microsoft, Azure Speech, What is custom speech? | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-speech-overview | página com "Last updated on 2026-02-25"; verificado em 18/10/2026 (HTTP 200) | R126 |
| Câmara dos Deputados, Regimento Interno (Resolução nº 17/1989, texto atualizado, Legin) | https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html | Legin, texto atualizado; verificado em 18/10/2026 (HTTP 200); arts. 66, IV e § 1º; 89, caput; 90, caput e parágrafo único; 95, caput; 118, §§ 6º e 8º; 126, caput (art. 126 lido na R2) | R127, R128, R129, R130 |

Itens sem fonte: nenhum. Nenhuma afirmação deste arquivo sobre ferramenta, serviço ou norma está sem URL oficial e data de verificação; o que não pôde ser sustentado foi retirado (ver seção 1.3, ponto descartado por gêmeo).

FIM DA PARTE 3/3

FIM DO LOTE
