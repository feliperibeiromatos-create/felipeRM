# L2_reforco_onda3_D_v1.md — T-97 — 2026-10-18 — gerado por gce-cpp

Onda 3 do reforço, parte D (ciclo 2026-10-18 s12c4). Escopo: P2-2.7 (+14, ids L2-R103 a L2-R116) e P2-2.8 (+14, ids L2-R117 a L2-R130). Cada folha passa de 6 para 20. Total: 28 itens.
Rótulo de todos os itens: AUTORAL (produtor gce-cpp, lote L2-R, onda 3 do reforço, D-REFORCO-2). QA PENDENTE: nenhum item deste arquivo entra em simulado antes da QA e da reconciliação (D-QA-PENDENTE). Nenhum item existente foi alterado.
Convenção: "verificado em 18/10/2026" = página aberta e lida nesta data (curl com User-Agent de navegador, HTTP 200; trechos conferidos no texto extraído). Nenhuma base de data anterior foi usada (D-FONTE-DATA-ANTERIOR não se aplica). Nenhum item cita número de versão, preço ou limite numérico de produto como ponto de julgamento; o único prazo de fornecedor que aparece (30 dias do SLA do Google, na citação da base de L2-R108) não é cobrado.
Legenda de formatos: D = definição; TSj = troca de sujeito; SH = situação hipotética; NP = número ou prazo; PC = par confundível; AP = aplicação parlamentar. Critério de classificação (T91_reconciliacao, seção 3.1): o formato é o da construção do ponto de julgamento, e não o do gabarito; o item C tem o formato da sua contraparte E. Os canônicos da folha foram classificados como em L2_reforco_onda1_v3.md, seção 2.
Critérios aplicados: D-REFORCO-1/2 (um ponto de julgamento por item, único na folha, inclusive frente aos canônicos e ao pacote inteiro, T96_reconciliacao, seção 4); critério de VOLÁTIL da D-T96-ONDA2-ACEITE (II) (VOLÁTIL = gabarito que depende de (a) versão, limite, preço ou modelo padrão; (b) comportamento padrão ou parâmetro nomeado de API; (c) existência ou disponibilidade de recurso condicionada pela documentação; (d) comportamento ilustrado só em saída de exemplo; funcionamento documentado de recurso central, sem número, versão, preço, padrão ou disponibilidade condicionada, é não VOLÁTIL, com conferência de base em 4–8/1/2027); registro da T90_reconciliacao (na 2.7, itens novos com aderência DIRETA até a folha ter 10: nenhum novo ponto da Lei 14.133 na 2.7; a folha tem hoje 2 de 6 itens de aderência parcial, R14 e R15, e passa a 2 de 20); registros O-1 a O-8 da T-93 e recomendações 1 a 7 do estilo_onda_2.md ("independentemente" também em C e em E, "pode" em E, concessiva alternada entre C e E, aberturas "Segundo a…" variadas, fonte nomeada quando o item usa "orientação" ou "recomendação", sem absolutos empilhados em E, ambientação parlamentar fora do escopo da remissão).

=====================================================================
PARTE 1/3 — MAPA
=====================================================================

## 1.1 P2-2.7 Controle de qualidade: revisão em dupla, auditorias de amostras, SLA — itens novos (um ponto de julgamento por item)

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL / risco | aderência |
|---|---|---|---|---|---|---|
| L2-R103 | P2-2.7 | A transcrição de referência (ground truth) para medir a acurácia é obtida por transcrição humana, em passagem única ou dupla, e não por outro sistema automático | TSj | Google Cloud, Speech-to-Text, "Measure and improve speech accuracy", seção "Measuring speech accuracy" (Get ground truth transcriptions): https://docs.cloud.google.com/speech-to-text/docs/v1/speech-accuracy (verificado em 18/10/2026) | n | direta |
| L2-R104 | P2-2.7 | As convenções da transcrição de referência (pontuação, números, capitalização) devem coincidir, o máximo possível, com as do sistema avaliado; não existe formato de transcrição único aceito por todos | AP | Google Cloud, Speech-to-Text, "Measure and improve speech accuracy", seções "Ground-truth conventions" e "Measuring speech accuracy": https://docs.cloud.google.com/speech-to-text/docs/v1/speech-accuracy (verificado em 18/10/2026) | n | direta |
| L2-R105 | P2-2.7 | O WER e a medida de confiança são métricas independentes, que em geral não se correlacionam: confiança alta não permite concluir WER baixo | SH | Google Cloud, Speech-to-Text, "Measure and improve speech accuracy", seção "Relation of WER to a confidence score": https://docs.cloud.google.com/speech-to-text/docs/v1/speech-accuracy (verificado em 18/10/2026) | n | direta |
| L2-R106 | P2-2.7 | O SLA do serviço em nuvem mede disponibilidade (percentual mensal de tempo de atividade, a partir de erros de servidor), e não a acurácia das transcrições | SH | Google Cloud, "Speech-to-Text Service Level Agreement (SLA)": https://cloud.google.com/speech-to-text/sla (verificado em 18/10/2026) | n | direta |
| L2-R107 | P2-2.7 | O remédio previsto no SLA é crédito financeiro aplicado a faturas futuras, declarado como único e exclusivo remédio do cliente | TSj | Google Cloud, SLA do Speech-to-Text: https://cloud.google.com/speech-to-text/sla (verificado em 18/10/2026) | n | direta |
| L2-R108 | P2-2.7 | O crédito financeiro não é automático: o cliente deve solicitá-lo ao suporte do fornecedor, com identificação do projeto e data e hora dos erros | TSj | Google Cloud, SLA do Speech-to-Text, seção "Customer must request financial credit": https://cloud.google.com/speech-to-text/sla (verificado em 18/10/2026) | n | direta |
| L2-R109 | P2-2.7 | Erros decorrentes de uso do serviço em desacordo com a documentação (campos inválidos) ficam fora do SLA e não contam como indisponibilidade | SH | Google Cloud, SLA do Speech-to-Text, seção "SLA exclusions": https://cloud.google.com/speech-to-text/sla (verificado em 18/10/2026) | n | direta |
| L2-R110 | P2-2.7 | Cálculo do percentual mensal de tempo de atividade: (minutos do mês − minutos de indisponibilidade) ÷ minutos do mês; 432 de 43.200 minutos = 1% de indisponibilidade | NP | Google Cloud, SLA do Speech-to-Text, definição de "Monthly Uptime Percentage" (só a fórmula; nenhum objetivo numérico é cobrado): https://cloud.google.com/speech-to-text/sla (verificado em 18/10/2026) | n | direta |
| L2-R111 | P2-2.7 | A indisponibilidade é medida pela taxa de erros no lado do servidor | TSj | Google Cloud, SLA do Speech-to-Text, definição de "Downtime": https://cloud.google.com/speech-to-text/sla (verificado em 18/10/2026) | n | direta |
| L2-R112 | P2-2.7 | O sclite totaliza os erros por locutor e por par referência–hipótese, permitindo auditoria por estrato (orador) | AP | NIST SCTK, documentação do sclite, seção "The scoring process": https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm (verificado em 18/10/2026) | n | direta |
| L2-R113 | P2-2.7 | No sclite, só as falas presentes no arquivo de hipótese são pontuadas; a referência pode ter registros a mais, o que permite pontuar uma amostra | TSj | NIST SCTK, documentação do sclite, seção "The alignment process", "Utterance ID Matching": https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm (verificado em 18/10/2026) | n | direta |
| L2-R114 | P2-2.7 | Além do WER global, deve-se examinar como os erros se distribuem e analisar arquivo a arquivo, para direcionar as melhorias | AP | Microsoft, "Test accuracy of a custom speech model", seção "Resolve errors and improve WER": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data (verificado em 18/10/2026) | n | direta |
| L2-R115 | P2-2.7 | Dados somente de áudio servem à inspeção (qualitativa); quantificar a acurácia (WER) exige áudio com transcrições rotuladas por pessoas | PC | Microsoft, "Test and train data for custom speech", seção "Audio data for training or testing": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-test-and-train (verificado em 18/10/2026) | n | direta |
| L2-R116 | P2-2.7 | Um modelo só é considerado melhor quando mostra melhorias significativas em todos os cenários avaliados (critério da nota de transparência), e não em apenas alguns | SH | Microsoft, nota de transparência do Azure Speech (speech to text), seção "System performance": https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note (verificado em 18/10/2026) | n | direta |

## 1.2 P2-2.8 Vocabulário técnico parlamentar e vocabulário adaptado (language model adaptation) — itens novos (um ponto de julgamento por item)

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL / risco | aderência |
|---|---|---|---|---|---|---|
| L2-R117 | P2-2.8 | Frase de várias palavras na adaptação aumenta a probabilidade da sequência e também a de partes da frase, inclusive de palavras individuais | TSj | Google Cloud, Speech-to-Text, "Improve transcription results with model adaptation", seção "Improve recognition of words and phrases": https://docs.cloud.google.com/speech-to-text/docs/adaptation-model (verificado em 18/10/2026) | n | direta |
| L2-R118 | P2-2.8 | Classes agrupam palavras de um conceito comum (valores monetários, datas) sem exigir listar cada valor; a disponibilidade varia por modelo e idioma | AP | Google Cloud, Speech-to-Text, "Improve transcription results with model adaptation", seção "Improve recognition using classes": https://docs.cloud.google.com/speech-to-text/docs/adaptation-model (verificado em 18/10/2026) | n | direta |
| L2-R119 | P2-2.8 | A classe personalizada (lista própria de itens) funciona como as predefinidas e pode ser combinada com elas na mesma frase | TSj | Google Cloud, Speech-to-Text, "Improve transcription results with model adaptation", seção "Custom classes": https://docs.cloud.google.com/speech-to-text/docs/adaptation-model (verificado em 18/10/2026) | n | direta |
| L2-R120 | P2-2.8 | Token de classe inválido ou malformado é ignorado sem erro, e o restante da frase continua sendo usado como contexto | SH | Google Cloud, Speech-to-Text, "Improve transcription results with model adaptation", seção "Class tokens": https://docs.cloud.google.com/speech-to-text/docs/adaptation-model (verificado em 18/10/2026) | S (BAIXO) | direta |
| L2-R121 | P2-2.8 | A lista de frases do Azure Speech não está disponível na transcrição em lote (API de lote não a suporta) | SH | Microsoft, "Improve recognition accuracy with phrase list": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/improve-accuracy-phrase-list (verificado em 18/10/2026) | S (BAIXO) | direta |
| L2-R122 | P2-2.8 | Quando se pode antecipar as palavras que serão faladas, usa-se a lista de frases; se a acurácia permanecer baixa, considera-se o custom speech | AP | Microsoft, nota de transparência do Azure Speech, seção "Best practices for improving system performance", itens "Add custom vocabularies" e "Use custom speech": https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note (verificado em 18/10/2026) | n | direta |
| L2-R123 | P2-2.8 | Dados de treinamento e de ajuste não devem se sobrepor; a sobreposição pode enviesar o modelo e prejudicar a acurácia | TSj | AWS, Amazon Transcribe, "Custom language models", seção "Training versus tuning data": https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html (verificado em 18/10/2026) | n | direta |
| L2-R124 | P2-2.8 | Treinamento ensina termos novos e contexto; ajuste (tuning) é opcional e recomendado quando faltam transcrições precisas do domínio | PC | AWS, Amazon Transcribe, "Custom language models", seções "Data sources" e "Training versus tuning data": https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html (verificado em 18/10/2026) | n | direta |
| L2-R125 | P2-2.8 | O vocabulário personalizado só pode ser usado se criado na mesma região da AWS da transcrição | SH | AWS, Amazon Transcribe, "Custom vocabularies": https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html (verificado em 18/10/2026) | n | direta |
| L2-R126 | P2-2.8 | Modelo implantado em endpoint do custom speech fica fixo até o usuário atualizá-lo; novo modelo base não altera a acurácia (dentro da vigência do modelo) | TSj | Microsoft, "What is custom speech?", seção "Model stability and lifecycle": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-speech-overview (verificado em 18/10/2026) | n | direta |
| L2-R127 | P2-2.8 | Definição regimental de questão de ordem: dúvida sobre a interpretação do Regimento, na sua prática exclusiva ou relacionada com a Constituição Federal | D | RICD, art. 95, caput, no Legin: https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html (verificado em 18/10/2026; conferência do qa-normativo solicitada) | n | direta (ver registro 4 da seção 1.4) |
| L2-R128 | P2-2.8 | Nas breves comunicações (Pequeno Expediente), cada Deputado fala por cinco minutos e não são permitidos apartes | D | RICD, art. 81, caput (e art. 66, I), no Legin: https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html (verificado em 18/10/2026; conferência do qa-normativo solicitada) | n | direta (ver registro 4 da seção 1.4) |
| L2-R129 | P2-2.8 | Emenda de redação é a emenda modificativa (e não aditiva) que visa a sanar vício de linguagem, incorreção de técnica legislativa ou lapso manifesto | PC | RICD, art. 118, §§ 6º e 8º, no Legin: https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html (verificado em 18/10/2026; conferência do qa-normativo solicitada) | n | direta (ver registro 4 da seção 1.4) |
| L2-R130 | P2-2.8 | Quem fala nas Comunicações Parlamentares (representantes de Partidos e Blocos indicados pelos Líderes) e nas Comunicações de Lideranças (os Líderes, por tempo proporcional à bancada) | PC | RICD, arts. 66, IV, 89, caput, e 90, caput, no Legin: https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html (verificado em 18/10/2026; conferência do qa-normativo solicitada) | n | direta (ver registro 4 da seção 1.4) |

## 1.3 Verificação de não repetição (ponto conferido contra o pacote inteiro)

Fontes conferidas por busca textual e leitura: saida/pacote/pacote.json v1.9 (334 itens; todas as folhas e o P1), saida/gce/GCE_Lote2_v2_CPP.md, GCE_Lote2_padroes_GCE.md, GCE_Lote2_consolidacao_GCE.md, L2_reforco_onda1_v3.md, L1_reforco_onda1_v2.md, L1_reforco_onda2_A_v3, B_v2, C_v2, D_v3 e saldo_v2 (inclusive L1-R131), L3_reforco_onda1_v3.md. Das outras partes da onda 3, existiam na conferência final saida/gce/L2_reforco_onda3_A_v1.md (folhas 2.1 e 2.2, ids L2-R19 a L2-R46) e saida/gce/L2_reforco_onda3_C_v1.md (folhas 2.5 e 2.6, ids L2-R75 a L2-R102), ambos lidos (mapa, enunciados e gabarito) e comparados por busca textual com cada ponto desta parte; a parte B (folhas 2.3 e 2.4) ainda não existia.
- P2-2.7 existentes: Q24 (revisão em dupla exige segundo revisor independente), Q25 (auditoria por amostragem estima a qualidade do conjunto), Q26 (amostra sem erro não prova ausência de erro nas peças não examinadas), Q27 (SLA pode fixar prazo e qualidade), R14 (terceiro que assiste o fiscal não exerce atribuição própria de fiscal; PARCIAL), R15 (prazos e métodos do recebimento definidos em regulamento ou no contrato; PARCIAL). Nenhum dos 14 novos repete esses pontos.
- P2-2.8 existentes: Q28 (LM adaptado altera a probabilidade de sequências), Q29 (OOV é termo ausente do vocabulário), Q30 (reforço excessivo insere o termo onde não foi dito), R16 (TECAD é vocabulário controlado), R17 (melhores dados de adaptação são transcrições precisas do domínio), R18 (limite de frases da phrase list; VOLÁTIL alto). Nenhum dos 14 novos repete esses pontos.
- Entre os 14 novos de cada folha, os pontos são todos distintos (comparação feita aos pares). Cada ponto da 2.7 e da 2.8 foi buscado também no restante do pacote e nos itens das ondas 1 e 2 (transcrição de referência humana, convenções da referência, confiança e WER, SLA, crédito, uptime, sclite, distribuição de erros, áudio sem transcrição, critério de troca de versão, classe, token de classe, lista de frases em lote, pauta e inscritos, treinamento e ajuste, região da AWS, modelo fixo no endpoint, questão de ordem, breves comunicações, emenda de redação, Comunicações Parlamentares): nenhuma ocorrência do mesmo ponto.
- Pontos planejados e descartados por gêmeo (não produzidos): "o teste do modelo adaptado usa áudios diferentes dos usados no ajuste" (Microsoft, "Test accuracy of a custom speech model"), que já é o L1-R22; e, depois da leitura do L2_reforco_onda3_A_v1.md, quatro pontos que a 2.7 tinha planejado e que a parte A já tem: conjunto de teste de gravações reais amostradas ao acaso (A: L2-R43), o mesmo conjunto renovado periodicamente (A: L2-R43), canal de retorno dos usuários após a implantação (A: L2-R36) e a Errata do art. 98, § 1º, do RICD (A: L2-R19). Os quatro foram trocados por pontos novos (R103, R104, R105 e R116 desta parte), em vez de ficarem como gêmeos declarados.
- Proximidades que a Gerência pode querer ver (nenhuma é duplicata; todas por ponto próprio, e as de outra folha entram declaradas e com ângulo próprio da folha, conforme a T96_reconciliacao, seção 4):
  - R103 × L2-R26 (parte A, 2.1), L1-R21 e L1-R128 (1.1 e 1.8): R26 julga o que é transcrição rotulada por humanos (palavra por palavra, e não resumo); R21 julga o efeito de falhas na referência sobre o WER; R128 julga comparar o modelo base com a transcrição humana; R103 julga como a referência costuma ser obtida (por pessoas, em passagem única ou dupla, e não por outro sistema automático).
  - R104 × L2-R09 (2.5), L1-R81, R85 (1.5) e L2-R75 a R78 (parte C, 2.5): R09 julga em que textos se aplica a normalização no cálculo do WER; R81 e R85 julgam o TER e o formato de exibição da referência; R75 a R78 julgam regras de normalização das transcrições de treinamento da Microsoft (siglas, números, abreviações); R104 julga que as convenções da referência devem coincidir com as do sistema avaliado, porque não há formato único de transcrição.
  - R105 × L2-Q06 (2.2), L1-R32 (1.1) e L2-R13 (2.6): Q06 julga que alta confiança não significa correção por definição e que conferir só a baixa confiança não basta; R32 julga as versões alternativas com confiança; R13 julga usar a confiança por palavra para destacar trechos; R105 julga que WER e confiança são métricas independentes, sem correlação esperada.
  - R106 × L2-Q27 (2.7): Q27 julga o que um SLA contratual de transcrição pode fixar (prazo e qualidade); R106 julga o que o SLA de um serviço em nuvem de fato mede (disponibilidade). R107 a R111 julgam outras cláusulas do mesmo SLA (remédio exclusivo, solicitação do crédito, exclusão por uso fora da documentação, fórmula do percentual, medição no servidor), uma por item.
  - R112 × L1-R30, R31 (1.1) e R113 × L1-R26, R28 (1.1): mesma ferramenta (sclite), outros pontos (pesos de palavras, taxa de erro de sentença, alinhamento, referências alternativas). R112 julga a totalização por locutor; R113 julga quais falas são pontuadas (as da hipótese).
  - R114 × L1-R20, R93, R95 (1.6 e 1.1): esses julgam a causa associada a cada tipo de erro; R114 julga o que a análise do teste deve cobrir (distribuição dos erros e exame arquivo a arquivo).
  - R115 × L1-R128 (1.8) e L2-R06 (2.3): R128 julga a comparação do modelo base com a transcrição humana por WER; R06 julga a fórmula do WER; R115 julga que dados somente de áudio servem à inspeção e não à quantificação.
  - R116 × L2-R04 (2.2): R04 julga que a avaliação do modelo no domínio de uso cabe à instituição; R116 julga o critério de melhoria em todos os cenários para trocar a versão do modelo. Ver o registro 5 da seção 1.4.
  - R117 × L2-Q28 (2.8): Q28 julga o efeito do LM adaptado sobre sequências de palavras; R117 julga o efeito de uma frase de adaptação do Google sobre a frase e suas partes. R117 × L1-R97 (1.6): R97 julga o excesso de boost; R117 não trata de boost.
  - R118 a R120 (classes do Google) × L1-R84, R99 (1.6): R84 e R99 julgam a forma de exibição e a pronúncia; R118 a R120 julgam classes, classe personalizada e token inválido.
  - R121 e R122 × L1-R94, R120 (1.6 e 1.8): R94 e R120 julgam que a lista de frases é de tempo de execução e dispensa treinamento; R121 julga a indisponibilidade na transcrição em lote; R122 julga em que situação a lista de frases é indicada (palavras previsíveis) e quando passar ao custom speech. R122 × L1-R128 (1.8): R128 parte do WER do modelo base; R122 parte da previsibilidade do que será falado.
  - R123 e R124 × L2-R17 (2.8): mesma página da AWS ("Custom language models"); R17 julga qual é o melhor dado; R123 julga a sobreposição entre treinamento e ajuste; R124 julga o papel e a obrigatoriedade do ajuste. R124 × L2-Q28 (2.8): Q28 julga o efeito do LM adaptado; R124 não repete.
  - R125 × L1-R101, R10 (1.6): R101 julga a grafia da entrada do vocabulário (espaço ou hífen); R10 julga o que não colocar na lista; R125 julga a região do vocabulário.
  - R126 × L1-R96, R128 (1.6 e 1.8): R96 julga modelos separados por área; R128 julga o uso do WER para decidir treinar; R126 julga a estabilidade do modelo implantado.
  - R127 a R130 (RICD): nenhum outro item do pacote usa os arts. 66, 81, 89, 90, 95 ou 118 do RICD. Em R128 × R130, a mesma estrutura de sessão ordinária (art. 66), pontos distintos (prazo e apartes das breves comunicações; destinatários das Comunicações Parlamentares).

## 1.4 Registros para a Gerência (sem alterar nada; competência D1/D2 da gce-gerencia)

1. VOLÁTIL (critério da D-T96-ONDA2-ACEITE (II)): 2 novos, ambos na 2.8 e de risco baixo: R120 (critério (b): comportamento do serviço diante de token de classe inválido, ignorado sem erro) e R121 (critério (c): a lista de frases não está disponível na transcrição em lote). Nenhum de risco alto nesta parte. Não VOLÁTEIS, com conferência de base em 4–8/1/2027: R106 a R111 (cláusulas do SLA do Google: o que o SLA mede, remédio, solicitação do crédito, exclusão, fórmula, medição; sem objetivo numérico, preço, versão ou disponibilidade condicionada), R116 (critério de melhoria descrito pelo fornecedor, sem o percentual que a página cita), R118 (o item já ressalva que a disponibilidade das classes varia por modelo e idioma), R119, R125 (exigência documentada de funcionamento, sem parâmetro nomeado) e R126 (o item já delimita "durante o período de validade do modelo"). Se a Gerência enquadrar as cláusulas do SLA como VOLÁTEIS, a 2.7 iria a 6/20 = 30% e passaria do teto de 20%; peço registro expresso do enquadramento, como foi pedido e feito na D-T96-ONDA2-ACEITE.
2. Aderência: todos os 28 itens são declarados de aderência DIRETA ao subitem da folha (2.7: qualidade, amostragem, SLA, revisão; 2.8: vocabulário técnico parlamentar e vocabulário adaptado). Nenhum item novo é de aderência parcial; a 2.7 mantém 2 de 20 itens parciais (R14, R15, legado), em 10%.
3. Tensão entre o curso e a documentação (não afeta nenhum item desta parte): a página "Improve transcription results with model adaptation" do Google traz, entre os usos da adaptação, "improving the accuracy of speech transcription when the supplied audio contains noise or is not very clear"; a frase do curso da 2.8 ("adaptação não corrige sotaque nem ruído", GCE_Lote2_v2_CPP.md, riscos) merece ressalva de fornecedor. Nenhum item desta parte julga esse ponto, de propósito.
4. Itens cuja aderência a Gerência pode querer decidir: R127 a R130 (termos regimentais: questão de ordem, breves comunicações, emenda de redação, Comunicações Parlamentares; declarados como vocabulário técnico parlamentar, 2.8, cujo curso lista "termos regimentais (questão de ordem, destaque, requerimento)"). Se forem enquadrados como PARCIAL, a 2.8 não tem restrição de aderência direta como a 2.7, mas ficariam só para simulado diagnóstico (D-ADERENCIA). Na 2.7, todos os 14 novos são de qualidade, amostragem, referência, SLA e controle de versão, sem Regimento nem Lei 14.133.
5. Trabalho paralelo na onda 3: as partes A e C foram lidas (nenhum gêmeo restante: os pontos coincidentes da parte A foram trocados, ver a seção 1.3; a parte C declara evitar teste de acurácia e WER como métrica de produto e não toca os pontos desta parte); a parte B (folhas 2.3 e 2.4) não existia na conferência final. Gêmeos possíveis a conferir na reconciliação: R103, R104 e R105 (referência, convenções, confiança e WER) × itens da 2.3 e 2.4 sobre WER, referência e confiança; R112 a R115 (sclite e testes do Azure) × itens da 2.3 sobre avaliação e revisão; R127 a R130 × itens da 2.4 sobre fases e períodos da sessão do Plenário. Se houver gêmeo, o item desta parte cede (o ponto de cada um está declarado nas seções 1.1 e 1.2).
6. Conferência normativa: os 4 itens com base no RICD (R127 a R130) foram lidos no Legin hoje (texto atualizado da Resolução nº 17/1989); pede-se a conferência do qa-normativo, como nas ondas anteriores. Não há item de lei federal nesta parte.
7. Lista de conferência de base de 4–8/1/2027 (T-11, parte P2, gce-cqfp): todos os 28 itens (todos têm base em página de fornecedor ou no Legin); 2 deles também VOLÁTEIS (R120, R121). Páginas redirecionadas: a URL legal/cognitive-services/.../transparency-note redireciona para a URL de foundry/responsible-ai/... (citada aqui pela URL final); o SLA do Google não traz data própria (rodapé "Previous versions (Last modified January 9, 2020)").

## 1.5 Formatos, VOLÁTEIS e gabarito por folha de 20

Formatos da folha P2-2.7 (20 itens = 6 existentes + 14 novos; teto de 30% = 6 por formato):
| formato | existentes | novos | total | % |
|---|---|---|---|---|
| definição (D) | Q25, Q27 | — | 2 | 10% |
| troca de sujeito (TSj) | — | R103, R107, R108, R111, R113 | 5 | 25% |
| situação hipotética (SH) | Q26 | R105, R106, R109, R116 | 5 | 25% |
| número ou prazo (NP) | R15 | R110 | 2 | 10% |
| par confundível (PC) | Q24 | R115 | 2 | 10% |
| aplicação parlamentar (AP) | R14 | R104, R112, R114 | 4 | 20% |
| soma | 6 | 14 | 20 | 100% |
Maior formato: troca de sujeito (TSj) com 25% (teto de 30% cumprido). Sem item novo de definição (D): o legado de 2/6 (Q25, Q27) cai para 2/20 = 10% (diluição pedida na T90_reconciliacao, seção 4). VOLÁTIL da folha: 0/20 (nenhum existente, nenhum novo).

Formatos da folha P2-2.8 (20 itens = 6 existentes + 14 novos; teto de 30% = 6 por formato):
| formato | existentes | novos | total | % |
|---|---|---|---|---|
| definição (D) | R16 | R127, R128 | 3 | 15% |
| troca de sujeito (TSj) | R17 | R117, R119, R123, R126 | 5 | 25% |
| situação hipotética (SH) | Q30 | R120, R121, R125 | 4 | 20% |
| número ou prazo (NP) | R18 | — | 1 | 5% |
| par confundível (PC) | Q29 | R124, R129, R130 | 4 | 20% |
| aplicação parlamentar (AP) | Q28 | R118, R122 | 3 | 15% |
| soma | 6 | 14 | 20 | 100% |
Maior formato: troca de sujeito (TSj) com 25% (teto de 30% cumprido). VOLÁTIL da folha: R18 (existente, risco alto), R120 e R121 (novos, risco baixo) = 3/20 = 15% (teto de 20% cumprido; nenhum novo de risco alto).

Gabarito da P2-2.7: novos 7 C / 7 E; com os 6 existentes (2 C / 4 E), a folha fecha em 9 C / 11 E (45% de C).
Gabarito da P2-2.8: novos 7 C / 7 E; com os 6 existentes (2 C / 4 E), a folha fecha em 9 C / 11 E (45% de C).
Gabarito da parte D: 14 C / 14 E = 50,0% de C (faixa de 40% a 60%, regra 5). [TS]: 18 de 28 (meta: 16 ou mais), sendo 13 em itens E e 5 em itens C (convenção "espelho" da GCE, O-6). VOLÁTEIS novos da parte: 2 (R120, R121), nenhum de risco alto.

FIM DA PARTE 1/3

=====================================================================
PARTE 2/3 — (d) ITENS DO ESTUDANTE
=====================================================================

L2-R103. Julgue o item.
Ao preparar a medição da acurácia de um serviço de ASR para as reuniões de comissão, a equipe da Câmara consulta a documentação do Google Cloud Speech-to-Text, segundo a qual a transcrição de referência (ground truth) costuma ser obtida por transcrição feita por outro sistema automático, em passagem única ou dupla.

L2-R104. Julgue o item.
Ao calcular o WER do ASR usado nas comissões, a equipe da Câmara elabora a transcrição de referência com convenções, como as de pontuação, números e capitalização, o mais próximas possível das do sistema avaliado, pois não existe formato de transcrição único aceito por todos.

L2-R105. Julgue o item.
A equipe da Câmara notou que a confiança atribuída pelo ASR às transcrições das reuniões é alta e concluiu que o WER será baixo. Essa conclusão não se sustenta, porque, segundo a documentação do Google Cloud Speech-to-Text, WER e confiança são métricas independentes, sem correlação esperada.

L2-R106. Julgue o item.
A Câmara contratou o Google Cloud Speech-to-Text para transcrever reuniões de comissão e entende que o SLA do serviço, ao fixar o percentual mensal de tempo de atividade, assegura uma taxa máxima de erros de palavras nas transcrições entregues, de modo que a equipe poderia dispensar a auditoria de amostras.

L2-R107. Julgue o item.
De acordo com o SLA do Google Cloud Speech-to-Text, o descumprimento do objetivo de nível de serviço dá ao cliente que cumpra as exigências do acordo direito a crédito financeiro em faturas futuras, e o próprio acordo declara esse crédito como o único e exclusivo remédio do cliente para a falha.

L2-R108. Julgue o item.
No SLA do Google Cloud Speech-to-Text, o crédito financeiro devido pelo descumprimento do objetivo de nível de serviço é aplicado pelo fornecedor às faturas seguintes, independentemente de solicitação do cliente, bastando que o percentual mensal de tempo de atividade apurado fique abaixo do objetivo.

L2-R109. Julgue o item.
O sistema da Câmara que envia áudios ao Google Cloud Speech-to-Text passou a receber respostas de erro porque as suas requisições continham campos inválidos. Segundo o SLA do serviço, esses erros devem ser computados como indisponibilidade no cálculo do percentual mensal de tempo de atividade, ainda que as requisições não estivessem de acordo com a documentação.

L2-R110. Julgue o item.
Em um mês de 30 dias, um serviço de reconhecimento de fala somou 432 minutos de indisponibilidade. Pelo cálculo do percentual mensal de tempo de atividade adotado no SLA do Google Cloud Speech-to-Text (minutos do mês menos minutos de indisponibilidade, divididos pelos minutos do mês), esse percentual foi de 99%.

L2-R111. Julgue o item.
No SLA do Google Cloud Speech-to-Text, a indisponibilidade que dá direito ao crédito financeiro é aferida, em cada período de apuração, a partir da taxa de erros observada pelo cliente nas suas próprias requisições, e não da taxa de erros medida no lado do servidor.

L2-R112. Julgue o item.
Na avaliação de transcrições automáticas de sessões, ferramentas de pontuação como o sclite, do NIST, totalizam os erros por locutor e por par de referência e hipótese, o que permite à equipe de qualidade identificar os oradores cujas falas o sistema transcreve pior e orientar a auditoria para elas.

L2-R113. Julgue o item.
Com referência e hipótese em formato trn e alinhamento por programação dinâmica, o sclite pontua apenas as falas identificadas no arquivo de hipótese, de modo que o arquivo de referência pode conter registros a mais, o que permite pontuar somente uma parte das falas.

L2-R114. Julgue o item.
Em um teste do Azure Speech com gravações de várias comissões, o valor global do WER é suficiente para que a equipe saiba que tipos de erro ocorrem e em quais arquivos, de modo que se torna desnecessário examinar os resultados arquivo a arquivo para direcionar as melhorias.

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
Uma equipe da Câmara pretende degravar sessões já gravadas com a API de transcrição em lote do Azure Speech e supõe que a lista de frases (phrase list), por não exigir treinamento de modelo, também pode ser usada nesse modo para favorecer o reconhecimento de nomes de parlamentares.

L2-R122. Julgue o item.
Em reunião cuja pauta e cujos oradores inscritos são conhecidos de antemão, a equipe pode prever os nomes e termos que serão falados. Nesse caso, a nota de transparência do Azure Speech sugere a lista de frases para favorecer esses termos e, se a acurácia permanecer baixa, o custom speech.

L2-R123. Julgue o item.
Na criação de um modelo de linguagem personalizado no Amazon Transcribe com dados de treinamento e de ajuste (tuning), a equipe da Câmara deve usar os mesmos textos nos dois conjuntos, pois a sobreposição reforça o aprendizado dos termos das comissões e não prejudica a acurácia do modelo.

L2-R124. Julgue o item.
No Amazon Transcribe, ao contrário dos dados de treinamento, que ensinam o modelo de linguagem personalizado a reconhecer novos termos e o contexto em que são usados, os dados de ajuste não são obrigatórios e são recomendados quando faltam transcrições precisas do domínio.

L2-R125. Julgue o item.
Uma equipe da Câmara criou o vocabulário personalizado com siglas e nomes de comissões no Amazon Transcribe em uma região da AWS e pretende iniciar a transcrição em outra região. Nessa situação, o vocabulário poderá ser usado, independentemente da região em que foi criado.

L2-R126. Julgue o item.
Um modelo personalizado do Azure Speech, implantado em ponto de extremidade próprio, permanece fixo até que o usuário decida atualizá-lo, de modo que, ainda que seja lançado um novo modelo base, enquanto vigente o modelo mantém sua acurácia e o desempenho com o vocabulário adaptado.

L2-R127. Julgue o item.
Em sessão do Plenário, um Deputado formulou uma questão de ordem. Segundo o Regimento Interno da Câmara dos Deputados, questão de ordem é toda dúvida sobre a interpretação do Regimento, na sua prática exclusiva ou relacionada com a Constituição Federal.

L2-R128. Julgue o item.
Em sessão ordinária do Plenário, no tempo que se segue à leitura da matéria do expediente, destinado aos Deputados inscritos para breves comunicações, cada orador pode falar por cinco minutos, sendo permitidos apartes, conforme o Regimento Interno da Câmara dos Deputados.

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

L2-R104. C. REVERIFICAR. A referência deve seguir, o mais possível, as convenções do sistema avaliado (pontuação, números, capitalização), porque não há um formato de transcrição único aceito por todos para o mesmo áudio.
O item pede o cuidado na elaboração da referência; não cobra o conjunto de convenções da página, que é detalhado e específico do Google.
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

L2-R108. E [TS]. REVERIFICAR. O cliente precisa notificar o suporte do fornecedor, no prazo do SLA e com dados do projeto e do horário dos erros; sem isso, perde o direito ao crédito.
Troca sutil: crédito solicitado pelo cliente por crédito aplicado automaticamente. O prazo numérico do SLA não é cobrado.
Base: Google Cloud, SLA do Speech-to-Text, seção "Customer must request financial credit": https://cloud.google.com/speech-to-text/sla, verificado em 18/10/2026: "In order to receive any of the Financial Credits described above, Customer must notify Google technical support within 30 days from the time Customer becomes eligible to receive a Financial Credit."

L2-R109. E [TS]. REVERIFICAR. O SLA exclui os erros resultantes de uso do serviço em desacordo com a documentação, inclusive campos inválidos na requisição; só requisições válidas entram no cálculo.
Troca sutil: erro excluído do cálculo por erro computado como indisponibilidade.
Base: Google Cloud, SLA do Speech-to-Text, seção "SLA exclusions": https://cloud.google.com/speech-to-text/sla, verificado em 18/10/2026: "(v) that resulted from Customer use of the Covered Service inconsistent with the Documentation, including but not limited to invalid request fields, unauthorized users, or inaccessible data."

L2-R110. C. REVERIFICAR. Um mês de 30 dias tem 43.200 minutos; (43.200 − 432) ÷ 43.200 = 0,99, isto é, 99%.
O item usa só a fórmula do SLA, sem o objetivo numérico do fornecedor, que não é cobrado.
Base: Google Cloud, SLA do Speech-to-Text, definição de "Monthly Uptime Percentage" (só a fórmula; nenhum objetivo numérico é cobrado): https://cloud.google.com/speech-to-text/sla, verificado em 18/10/2026: ""Monthly Uptime Percentage" means total number of minutes in a month, minus the number of minutes of Downtime suffered from all Downtime Periods in a month, divided by the total number of minutes in a month."

L2-R111. E [TS]. REVERIFICAR. O SLA define a indisponibilidade com base na taxa de erros medida no lado do servidor.
Troca sutil: lado do servidor por lado do cliente. O limite numérico da taxa de erros não é cobrado.
Base: Google Cloud, SLA do Speech-to-Text, definição de "Downtime": https://cloud.google.com/speech-to-text/sla, verificado em 18/10/2026: "Downtime is measured based on server side Error Rate."

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
O item ressalva que a disponibilidade varia por modelo e idioma e não afirma suporte ao português.
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

L2-R124. C. REVERIFICAR. Os dados de treinamento ensinam termos e contexto; os de ajuste refinam as relações aprendidas, não são exigidos e são recomendados na falta de transcrições do domínio.
Par confundível: treinamento (necessário) por ajuste (opcional).
Base: AWS, Amazon Transcribe, "Custom language models", seções "Data sources" e "Training versus tuning data": https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html, verificado em 18/10/2026: "Tuning data are not required to create a custom language model."; "Tuning data are recommended when you lack in-domain training data."

L2-R125. E [TS]. REVERIFICAR. Para usar um vocabulário personalizado, ele deve ter sido criado na mesma região da AWS da transcrição.
Troca sutil: mesma região por qualquer região. Exigência documentada de funcionamento (não é número, versão nem parâmetro nomeado).
Base: AWS, Amazon Transcribe, "Custom vocabularies": https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html, verificado em 18/10/2026 (página sem data própria): "To use a custom vocabulary, it must have been created in the same AWS Region as your transcription."

L2-R126. C [TS]. REVERIFICAR. O modelo implantado em endpoint próprio é fixo até a decisão do usuário e mantém acurácia e qualidade mesmo com novo modelo base, o que preserva o vocabulário adaptado; vale pelo período de vigência do modelo.
Espelho de [TS]: a versão verdadeira de "é atualizado automaticamente para o novo modelo base".
Base: Microsoft, "What is custom speech?", seção "Model stability and lifecycle": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-speech-overview, verificado em 18/10/2026 (página com "Last updated on 2026-02-25"): "A base model or custom model deployed to an endpoint using custom speech is fixed until you decide to update it. The speech recognition accuracy and quality remain consistent, even when a new base model is released."; "you can use the model for a limited time"

L2-R127. C. REVERIFICAR. O art. 95 considera questão de ordem toda dúvida sobre a interpretação do Regimento, na sua prática exclusiva ou relacionada com a Constituição Federal.
Termo do vocabulário técnico parlamentar que o revisor encontra nas notas taquigráficas; o item cobra a definição regimental.
Base: RICD, art. 95, caput, no Legin: https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html, verificado em 18/10/2026 (Legin, texto atualizado): "Considera-se questão de ordem toda dúvida sobre a interpretação deste Regimento, na sua prática exclusiva ou relacionada com a Constituição Federal."

L2-R128. E [TS]. REVERIFICAR. O art. 81 destina o tempo seguinte à leitura do expediente a breves comunicações, de cinco minutos por orador, sem apartes.
Troca sutil: "não sendo permitidos apartes" por "sendo permitidos apartes" (o prazo de cinco minutos do enunciado é o do artigo).
Base: RICD, art. 81, caput (e art. 66, I), no Legin: https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html, verificado em 18/10/2026 (Legin, texto atualizado): "O tempo que se seguir à leitura da matéria do expediente será destinado aos Deputados inscritos para breves comunicações, podendo cada um falar por cinco minutos, não sendo permitidos apartes."

L2-R129. E [TS]. REVERIFICAR. O § 8º do art. 118 denomina emenda de redação a modificativa que visa a sanar vício de linguagem, incorreção de técnica legislativa ou lapso manifesto; a aditiva é a que se acrescenta a outra proposição (§ 6º).
Troca sutil: modificativa por aditiva.
Base: RICD, art. 118, §§ 6º e 8º, no Legin: https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html, verificado em 18/10/2026 (Legin, texto atualizado): "Denomina-se emenda de redação a modificativa que visa a sanar vício de linguagem, incorreção de técnica legislativa ou lapso manifesto."

L2-R130. E [TS]. REVERIFICAR. As Comunicações de Lideranças (art. 89) destinam-se aos Líderes, por tempo proporcional às bancadas; as Comunicações Parlamentares (arts. 66, IV, e 90) cabem a oradores indicados pelos Líderes, alternadamente por Partidos e Blocos.
Troca sutil: o nome Comunicações de Lideranças por Comunicações Parlamentares.
Base: RICD, arts. 66, IV, 89, caput, e 90, caput, no Legin: https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html, verificado em 18/10/2026 (Legin, texto atualizado): "As Comunicações de Lideranças [...] destinam-se aos Líderes que queiram fazer uso da palavra, por período de tempo proporcional ao número de membros das respectivas bancadas"; "Comunicações Parlamentares, desde que haja tempo, destinadas a representantes de Partidos e Blocos Parlamentares, alternadamente, indicados pelos Líderes"

## Contagens
| quesito | valor |
|---|---|
| total | 28 (P2-2.7: 14; P2-2.8: 14) |
| C | 14 (P2-2.7: R104, R105, R107, R110, R112, R113, R116; P2-2.8: R118, R119, R120, R122, R124, R126, R127) = 50,0% (faixa de 40% a 60% cumprida); por folha: 2.7 com 7 C / 7 E; 2.8 com 7 C / 7 E |
| E | 14 (P2-2.7: R103, R106, R108, R109, R111, R114, R115; P2-2.8: R117, R121, R123, R125, R128, R129, R130) |
| [TS] | 18 de 28 = 64,3% (meta: 16 ou mais, cumprida): P2-2.7: R103, R106, R107, R108, R109, R111, R113, R115, R116 (9); P2-2.8: R117, R119, R121, R123, R125, R126, R128, R129, R130 (9) |
| [TS] com gabarito C | 5 (R107, R113, R116, R119, R126), por convenção "espelho", cada um com a troca do espelho declarada na justificativa; sem relação fixa entre [TS] e gabarito. Só em itens E: 13 de 14 |
| VOLÁTIL | 2 novos, ambos em P2-2.8: R120 e R121 (risco baixo); risco alto novo 0. P2-2.7: 0 novos |
| VOLÁTIL por folha de 20 | P2-2.7: 0/20 = 0%; P2-2.8: R18, R120, R121 = 3/20 = 15% |
| formato máximo por folha de 20 | P2-2.7: 25% (SH e TSj com 5 cada); P2-2.8: 25% (TSj com 5) |
| aderência | 28 DIRETA; 0 PARCIAL novos (legado da 2.7: R14, R15) |
| REVERIFICAR (4–8/1/2027) | 28 (base em página de fornecedor ou no Legin); 2 desses também VOLÁTEIS (R120, R121) |
| extensão (palavras do enunciado) | C: média 46,0 (de 40 a 51); E: média 46,1 (de 37 a 56); nenhum C acima de 65 palavras (O-1) |

Observações de estilo (registros O-1 a O-8 da T-93 e recomendações do estilo_onda_2.md):
- O-1 (extensão): C com média 46,0 e E com média 46,1 palavras; a diferença é de 0,1 palavra, sem pista de extensão; o E mais longo (R109, 56 palavras) supera o C mais longo (51).
- O-2 ("independe"): em C: R118; em E: R108, R125. Presente nos dois gabaritos, como pedido na recomendação 1.
- O-3 ("pode/poderá"): em C: R113, R119, R122; em E: R115, R121, R125, R128.
- O-4 (remissão): nas remissões a documentação ou norma ("Segundo", "De acordo com", "a nota de transparência sugere", "conforme"), a ambientação parlamentar (reuniões de comissão, pauta, oradores inscritos, sessão do Plenário) fica fora do escopo da remissão, em frase própria ou no sujeito.
- O-5 (cauda que se denuncia): não há cauda falsa autocontraditória (o R103 foi escrito sem a cauda "para que a referência seja precisa", que denunciaria a troca); os erros são trocas de conceito, de sujeito, de número ou de condição. Nenhum E empilha absolutos: R115 tem um "somente".
- O-6 ([TS] em C): R107, R113, R116, R119, R126 são C com espelho declarado.
- O-7 (restritivos e causais): "apenas" em C: R113, R116; em E: nenhum. "somente" em C: R113; em E: R115. "só" restritivo em C: R116. "pois" em C: R104; em E: R115, R123. "porque" em C: R105; em E: R109.
- O-8 (concessiva): "ainda que" em C: R126; em E: R109; alternada entre os dois gabaritos.
- Aberturas (recomendação 3): "Segundo" abre nenhum item; "De acordo com" abre R107; os demais abrem com sujeito, circunstância ou "Considere que"; não há concentração de "Segundo a…".

## Tabela de proveniência (todas abertas e lidas em 18/10/2026)
| fonte | URL oficial | data da página / verificação | usada em |
|---|---|---|---|
| Google Cloud, Speech-to-Text, Measure and improve speech accuracy | https://docs.cloud.google.com/speech-to-text/docs/v1/speech-accuracy | página com "Last updated 2026-10-13 UTC"; a URL /docs/speech-accuracy redireciona para esta; verificado em 18/10/2026 (HTTP 200); seções "Relation of WER to a confidence score", "Ground-truth conventions" e "Measuring speech accuracy"; a URL /docs/speech-accuracy redireciona para esta | R103, R104, R105 |
| Google Cloud, Speech-to-Text Service Level Agreement (SLA) | https://cloud.google.com/speech-to-text/sla | página sem data própria; rodapé "Previous versions (Last modified January 9, 2020)"; verificado em 18/10/2026 (HTTP 200) | R106, R107, R108, R109, R110, R111 |
| NIST, SCTK, documentação do sclite (repositório oficial usnistgov/SCTK, arquivo bruto) | https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm | documentação sem data própria na página; verificado em 18/10/2026 (HTTP 200) | R112, R113 |
| Microsoft, Azure Speech, Test accuracy of a custom speech model | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | página com "Last updated on 2025-12-29"; verificado em 18/10/2026 (HTTP 200) | R114 |
| Microsoft, Azure Speech, Test and train data for custom speech | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-test-and-train | página com "Last updated on 2025-12-19"; confirmado também em custom-speech-overview ("Last updated on 2026-02-25"); verificado em 18/10/2026 (HTTP 200) | R115 |
| Microsoft, Azure Speech, nota de transparência de speech to text (Use cases for Speech to text) | https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note | página com "Last updated on 2026-03-31"; verificado em 18/10/2026 (HTTP 200); seções "Evaluating and integrating speech to text for your use", "Best practices for improving system performance" e "Guidance for integration and responsible use" | R116, R122 |
| Google Cloud, Speech-to-Text, Improve transcription results with model adaptation | https://docs.cloud.google.com/speech-to-text/docs/adaptation-model | página com "Last updated 2026-10-13 UTC"; verificado em 18/10/2026 (HTTP 200) | R117, R118, R119, R120 |
| Microsoft, Azure Speech, Improve recognition accuracy with phrase list | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/improve-accuracy-phrase-list | página com "Last updated on 2026-06-29"; verificado em 18/10/2026 (HTTP 200) | R121 |
| AWS, Amazon Transcribe, Custom language models | https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html | página sem data própria; verificado em 18/10/2026 (HTTP 200) | R123, R124 |
| AWS, Amazon Transcribe, Custom vocabularies | https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html | página sem data própria; verificado em 18/10/2026 (HTTP 200) | R125 |
| Microsoft, Azure Speech, What is custom speech? | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-speech-overview | página com "Last updated on 2026-02-25"; verificado em 18/10/2026 (HTTP 200) | R126 |
| Câmara dos Deputados, Regimento Interno (Resolução nº 17/1989, texto atualizado, Legin) | https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html | Legin, texto atualizado; verificado em 18/10/2026 (HTTP 200); arts. 66, I e IV; 81, caput; 89, caput; 90, caput; 95, caput; 118, §§ 6º e 8º | R127, R128, R129, R130 |

Itens sem fonte: nenhum. Nenhuma afirmação deste arquivo sobre ferramenta, serviço ou norma está sem URL oficial e data de verificação; o que não pôde ser sustentado foi retirado (ver seção 1.3, ponto descartado por gêmeo).

FIM DA PARTE 3/3

FIM DO LOTE
