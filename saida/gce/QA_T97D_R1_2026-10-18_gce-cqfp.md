# QA_T97D_R1_2026-10-18_gce-cqfp.md — T-97 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L2_reforco_onda3_D_v1.md (gce-cpp; 28 itens AUTORAL L2-R103 a L2-R130; P2-2.7 = R103–R116, P2-2.8 = R117–R130), SHA-256 01b5a69d88b1be81140075f127e38a79768fc5aa08cb5b1ae87ba8c4c819e9a3. Rodada R1 (de no máximo 2). Esta QA revisa e não reescreve: diz onde está o problema e por quê.
Lidos: TAREFAS.md (linha T-97); DECISOES.md (D-REFORCO-1/2, D-FONTE-DATA-ANTERIOR, D-T89-R1-ACEITE, D-T90-R2-ACEITE, D-T96-ONDA2-ACEITE (II), D-ONDA3-FILA, D-ADERENCIA); T90_reconciliacao (seções 2 e 4); T96_reconciliacao (seções 2 a 4); saida/banco/estilo_onda_2.md (seção 5); edital/modulo_RF_IA_P2.md; saida/pacote/pacote.json v1.9 (334 itens; os 12 de P2-2.7 e P2-2.8 conferidos um a um); GCE_Lote2_v2_CPP.md e GCE_Lote2_padroes_GCE.md; L2_reforco_onda3_A_v1, B_v1 e C_v1 (a parte B já existe; a produtora não a tinha visto).

## 1. Evidência: URLs reabertas pela QA em 18/10/2026 (curl com User-Agent de navegador; texto extraído; script python -I)
Todas as 12 URLs citadas foram reabertas. Todas deram HTTP 200, sem redirecionamento.
| # | URL | resultado |
|---|---|---|
| 1 | https://docs.cloud.google.com/speech-to-text/docs/v1/speech-accuracy | 200; "Last updated 2026-10-13 UTC". Os 6 trechos de R103–R105 conferem literalmente (o de R105 tem só uma diferença de espaço antes da vírgula). A mesma página diz que "Punctuation is removed, and capitalization is ignored" antes da comparação (ver R104). |
| 2 | https://cloud.google.com/speech-to-text/sla | 200; rodapé "Previous versions (Last modified January 9, 2020)". Os 8 trechos de R106–R111 conferem. A página também traz "Downtime means more than a 5% Error Rate" e a tabela de crédito por faixas (99%–<99,9% = 10%), que nenhum item cobra. |
| 3 | https://raw.githubusercontent.com/usnistgov/SCTK/master/doc/sclite.htm | 200; os trechos de R112 ("scores are tallied for each speaker and each ref/hyp pair") e R113 ("Only the utterance ID's present in the HYP file…", no formato trn com alinhamento DP) conferem. |
| 4 | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | 200; os 3 trechos de R114 conferem. |
| 5 | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-test-and-train | 200; os 2 trechos de R115 conferem. |
| 6 | https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note | 200; os trechos de R116 e R122 conferem. Contexto de R116: "(such as a 5% relative WER improvement) in all scenarios (like transcription of conversation speech, call center transcription, dictation, and voice assistant) while being in line with the resource usage and response latency goals". |
| 7 | https://docs.cloud.google.com/speech-to-text/docs/adaptation-model | 200; "Last updated 2026-10-13 UTC". Os trechos de R117–R120 conferem. A página traz entre os usos da adaptação: "Improving the accuracy of speech transcription when the supplied audio contains noise or is not very clear." (ver a seção 5). |
| 8 | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/improve-accuracy-phrase-list | 200; os 2 trechos de R121 conferem. |
| 9 | https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html | 200; os trechos de R123 e R124 conferem. Há porém o problema de paráfrase descrito em R124. |
| 10 | https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html | 200; o trecho de R125 confere. |
| 11 | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-speech-overview | 200; os 3 trechos de R126 conferem. |
| 12 | Legin, RICD, texto atualizado (www2.camara.leg.br/…320110-normaatualizada-pl.html) | 200; conferem os arts. 66, I e IV (caput com redação dada pela Res. 21/2021), 66, § 1º, 81, caput, 89, caput, 90, caput, 95, caput, e 118, §§ 6º e 8º. A conferência formal é do qa-normativo (PENDENTE NORMATIVO, seção 4). |
Nenhuma afirmação deixou de ter fonte datada. Nenhuma base é de data anterior (D-FONTE-DATA-ANTERIOR não se aplica).

## 2. Estrutura, contagens e estilo (script sobre o objeto)
- Partes 1/3 a 3/3, "FIM DA PARTE n/3" e "FIM DO LOTE" estão presentes. A Parte 2 tem 28 enunciados e nenhum gabarito, [TS], VOLÁTIL ou REVERIFICAR. A Parte 3 tem 28 gabaritos, com os mesmos ids.
- Gabarito: 14 C / 14 E, ou seja, 50,0% de C (regra 5 cumprida). Por folha, 7/7 nos novos. Com os 6 existentes do pacote (2.7: Q25 e Q27 C; Q24, Q26, R14 e R15 E; 2.8: Q28 e R18 C; Q29, Q30, R16 e R17 E), cada folha fecha em 9 C / 11 E. A declaração confere.
- [TS]: 18/28 confere (9 em cada folha; 5 C espelho, conforme a O-6). Troca única: confirmada nos 13 E com [TS]. A ressalva está no R123: "deve usar os mesmos textos" e "não prejudica a acurácia" dizem a mesma troca duas vezes, e não são dois conceitos, de modo que o [TS] fica.
- Extensão: C tem média de 46,0 palavras (de 40 a 51) e E, 46,1 (de 37 a 56). Não há pista de extensão (O-1).
- Estilo (estilo_onda_2, recomendações 1 a 7): cumpridas no conjunto. Há duas falhas de discriminação ou fechamento, tratadas em R106, R114 e R121.
- Diluição de LEGADO (T90_reconciliacao, seção 4): nenhum item novo de definição na 2.7. Cumprida.

## 3. Veredito por item
| id | folha | gab. | veredito | motivo |
|---|---|---|---|---|
| L2-R103 | 2.7 | E [TS] | APROVADO | Troca única (referência humana → outro sistema automático). Base literal. Ponto distinto de L2-R26, L1-R21 e L1-R128. |
| L2-R104 | 2.7 | C | AJUSTAR | O enunciado afirma como verdade geral, sem remissão, uma recomendação do Google (casar as convenções da referência com as do sistema avaliado). Como proposição geral, é contestável: a prática alternativa é normalizar os dois textos, e a própria página remove a pontuação e ignora a capitalização antes de comparar. Ajuste: atribuir à documentação do Google Cloud Speech-to-Text (recomendação 4 do estilo_onda_2), mantendo a ambientação fora da remissão. |
| L2-R105 | 2.7 | C | APROVADO | A conclusão vem fechada ("Essa conclusão não se sustenta") e a base é literal. Fica um gêmeo próximo, em outra folha, com L2-Q06 (2.2: alta confiança não significa correção). O ângulo é próprio (métrica agregada × confiança), mas o par é registrado para a GBQ: não devem ir ao mesmo caderno (T96, seção 4). |
| L2-R106 | 2.7 | E [TS] | AJUSTAR | A troca (disponibilidade → acurácia) é boa e é conceito de SLA, mas o enunciado só narra o entendimento da Câmara ("entende que…, de modo que poderia dispensar…"). Uma leitura literal admite C, porque é verdade que a Câmara entende isso. Ajuste: fechar com juízo explícito ("Nessa situação, o entendimento da Câmara está correto"), como fazem R105 e R120. |
| L2-R107 | 2.7 | C [TS] | APROVADO | Crédito financeiro como remédio do SLA é conceito do instrumento. "Único e exclusivo remédio" é cláusula típica de SLA de nuvem. Base literal. Não VOLÁTIL (seção 6). |
| L2-R108 | 2.7 | E [TS] | REPROVADO | Extrapola o edital. O ponto (o crédito só vale se o cliente o pedir ao suporte do Google) é procedimento contratual próprio de um fornecedor, sem relação com controle de qualidade da transcrição. Uma banca não cobraria isso como "SLA" do 2.7. Se fosse mantido, seria VOLÁTIL, porque o gabarito depende só da redação atual de uma cláusula (seção 6). Concentração: 6 dos 14 novos da folha vêm da mesma página. |
| L2-R109 | 2.7 | E [TS] | APROVADO | Exclusão do SLA por uso fora da documentação é conceito geral do instrumento. Troca única. Base literal. |
| L2-R110 | 2.7 | C | APROVADO | A fórmula do percentual de disponibilidade é conceito geral. A conta confere: (43.200 − 432) ÷ 43.200 = 99%. Nenhum objetivo numérico do fornecedor é cobrado. |
| L2-R111 | 2.7 | E [TS] | REPROVADO | Extrapola o edital, pela mesma razão do R108. Medir a indisponibilidade pela taxa de erros do servidor, e não do cliente, é minúcia de medição de um contrato, fora de "controle de qualidade". A troca servidor ↔ cliente não é conceito do edital. Se fosse mantido, seria VOLÁTIL. |
| L2-R112 | 2.7 | C | AJUSTAR | "ferramentas de pontuação como o sclite… totalizam" estende a todas as ferramentas o que a base só afirma do sclite, sem fonte para isso. Ajuste: "o sclite, do NIST, totaliza…". O resto é fiel. |
| L2-R113 | 2.7 | C [TS] | APROVADO | Fiel à base (formato trn, alinhamento DP, só as falas da hipótese). É o único item novo que toca diretamente a pontuação de uma amostra. |
| L2-R114 | 2.7 | E | AJUSTAR | Baixa discriminação: o item é falso pela própria lógica do enunciado, porque um valor global único não pode dizer "em quais arquivos" os erros ocorrem. O candidato acerta sem conhecer a base. Ajuste: o E deve depender da base (por exemplo, "o WER global basta para direcionar as melhorias, dispensando a análise da distribuição dos erros"), sem a cauda que se denuncia (O-5). |
| L2-R115 | 2.7 | E [TS] | APROVADO | Inspeção × quantificação; troca única; base literal. |
| L2-R116 | 2.7 | C [TS] | APROVADO | O que se julga é a correspondência com o critério da nota, que confere. Ressalva de registro: o critério da nota é o da Microsoft para os próprios modelos e inclui a condição de recursos e latência, que o item omite sem mudar o gabarito. |
| L2-R117 | 2.8 | E [TS] | APROVADO | Base literal. Fica próximo de L2-Q28 (efeito sobre sequências), mas com ângulo inverso e próprio (efeito também sobre as palavras isoladas). Não é duplicata. |
| L2-R118 | 2.8 | C | AJUSTAR | Formato errado: o item é declarado AP, mas não tem aplicação parlamentar (valores monetários e datas). É definição (D). Reclassificar: a 2.8 fica com D em 3/20 (com a saída de R128) e AP em 2/20, dentro do teto. Rótulo: o item ressalva no texto a disponibilidade condicionada ("depende do modelo e do idioma"), e o ponto julgado é o mecanismo da classe. O não VOLÁTIL é defensável pela T96, seção 2.2, mas a Gerência deve registrar isso expressamente. |
| L2-R119 | 2.8 | C [TS] | APROVADO | Funcionamento da classe personalizada; base literal; não VOLÁTIL (mesma ressalva de registro do R118). |
| L2-R120 | 2.8 | C | APROVADO | VOLÁTIL baixo pela hipótese (b) (comportamento diante de entrada inválida). Marcação correta. |
| L2-R121 | 2.8 | E [TS] | AJUSTAR | Tem o mesmo defeito do R106: termina na suposição da equipe ("supõe que… também pode ser usada"), sem juízo explícito, e uma leitura literal admite C. Ajuste: fechar com "Nessa situação, a suposição da equipe está correta". VOLÁTIL baixo pela hipótese (c), marcação correta. |
| L2-R122 | 2.8 | C | APROVADO | A remissão está nomeada ("a nota de transparência do Azure Speech sugere") e a ambientação fica fora dela. Base literal. |
| L2-R123 | 2.8 | E [TS] | APROVADO | Base literal. Ressalva da seção 2 (a mesma troca dita duas vezes). |
| L2-R124 | 2.8 | C | AJUSTAR | A paráfrase da base está errada. A AWS diz "Tuning data are recommended when you lack in-domain training data". O item diz "quando faltam transcrições precisas do domínio". Na mesma página, os dados de ajuste são justamente uma parte (10–25%) das transcrições do domínio (cenário 2), e, sem nenhuma transcrição do domínio, a orientação é enviar tudo como treinamento (cenário 3). Como está, o C pode ser derrubado com a própria fonte. Ajuste: usar a forma literal ("quando faltam dados de treinamento do próprio domínio"). |
| L2-R125 | 2.8 | E [TS] | AJUSTAR | Ajuste de rótulo. O ponto julgado é a própria condição de uso do recurso por localização (o vocabulário só serve na região em que foi criado). Isso é a hipótese (c) da D-T96-ONDA2-ACEITE ("disponibilidade de recurso que a própria documentação condiciona (… local …)"), e não o funcionamento de um recurso central. Marcar VOLÁTIL baixo. A 2.8 fica com 4/20 = 20% (R18, R120, R121, R125), no teto e sem margem para outro VOLÁTIL na reposição. Se a Gerência ler "local" só como locale (idioma), deve registrar isso. Marcação a menos não é admitida (T96, seção 2.1). |
| L2-R126 | 2.8 | C [TS] | APROVADO | Base literal. O item já delimita a vigência ("enquanto vigente"), conforme "use the model for a limited time". Não VOLÁTIL. |
| L2-R127 | 2.8 | C | APROVADO — PENDENTE NORMATIVO | Definição literal do art. 95, caput. Aderência direta defensável: "questão de ordem" é termo regimental que o curso do 2.8 lista. Fica próximo do L2-R49 da parte B (art. 95, § 5º), em outro ponto. |
| L2-R128 | 2.8 | E [TS] | REPROVADO — PENDENTE NORMATIVO | Escopo: o ponto (cinco minutos e vedação de apartes nas breves comunicações) é regra de procedimento da sessão. Não é o sentido de um termo nem tem relação com vocabulário adaptado. Não há aderência ao 2.8. O formato declarado (D) também não corresponde (é regra, com prazo). Repor por item E, não VOLÁTIL. |
| L2-R129 | 2.8 | E [TS] | APROVADO — PENDENTE NORMATIVO | Sentido do termo "emenda de redação" (art. 118, § 8º); troca modificativa → aditiva. Aderência direta defensável (termo do vocabulário técnico do revisor). |
| L2-R130 | 2.8 | E [TS] | APROVADO — PENDENTE NORMATIVO | Gabarito firme (arts. 66, IV e § 1º, 89 e 90). Aderência: proponho PARCIAL (D1 da gce-gerencia; D-ADERENCIA), porque o ponto decisivo é quem fala e por quanto tempo, que é procedimento, mais do que o sentido do nome. Se ficar PARCIAL, o item vai só a simulado diagnóstico, o que a 2.8 admite. Registro: a justificativa pode citar o § 1º do art. 66, ao qual o art. 89 remete. |

Taxa: REPROVADO 3/28 = 10,7% (R108, R111, R128); AJUSTAR 8/28 (R104, R106, R112, R114, R118, R121, R124, R125); APROVADO 17/28. Não atinge o GATE de 30%.

## 4. Normativo
PENDENTE NORMATIVO: R127, R128, R129 e R130, com base no RICD. A conferência é do qa-normativo, em paralelo. A QA conferiu os trechos no Legin nesta data (seção 1, linha 12), e todos são literais. Não há item de lei federal nesta parte.

## 5. Escopo e aderência
- 2.7 (D-T90-R2-ACEITE: itens novos com aderência direta até a folha ter 10). Os 14 são de qualidade, medição, amostragem, SLA e troca de versão, e os primeiros quatro a cinco (R103 a R107) são diretos. A condição está cumprida, sem Regimento e sem Lei 14.133. Ficam duas lacunas de cobertura do enunciado do edital ("revisão em dupla, auditorias de amostras, SLA"):
  - "revisão em dupla" continua com um só item na folha (Q24);
  - "auditoria de amostras" tem só R113 e, indiretamente, R112.
  - A recomendação à reposição de R108 e R111 é usar dois itens E, não VOLÁTEIS, sobre revisão em dupla ou auditoria de amostras, com base oficial aberta na data. Assim a folha volta a 9 C / 11 E e o SLA cai de 6 para 4 itens da mesma página.
- 2.8: dos itens com base no RICD, R127 e R129 são diretos e defensáveis (sentido de termo), R130 é PARCIAL (proposto) e R128 é REPROVADO por escopo.
- Registro para a reconciliação: a afirmação da seção 1.3 do objeto, de que "nenhum outro item do pacote usa os arts. 66, 81, 89, 90, 95 ou 118", ficou superada pela parte B (L2-R49, art. 95, § 5º; L2-R67, art. 66, II). A própria parte B declara as vizinhanças. Não há gêmeo.
- Não foi encontrado gêmeo nas partes A, B e C (busca por sclite, SLA, confiança, referência, classe, região, lote, ajuste, questão de ordem, emenda de redação e Comunicações Parlamentares).

## 6. VOLÁTIL (critério da D-T96-ONDA2-ACEITE (II)); pergunta "SLA é fato mutável?"
- O SLA é instrumento contratual com versões publicadas ("Previous versions", última alteração em 9/1/2020): as cláusulas podem mudar por ato do fornecedor. As hipóteses (a)–(d), porém, foram escritas para recursos de serviço e não tratam cláusula de contrato sem número. Leitura desta QA:
  - R106 (o que um SLA de disponibilidade mede) e R110 (fórmula do percentual): o gabarito vale para qualquer SLA de disponibilidade. São NÃO VOLÁTEIS.
  - R107 (crédito como remédio) e R109 (exclusão por uso fora da documentação): são cláusulas estruturais e típicas. São NÃO VOLÁTEIS, com conferência de base em 4–8/1/2027.
  - R108 e R111: o gabarito depende só da redação atual de cláusulas particulares de um fornecedor. Se fossem mantidos, seriam VOLÁTEIS por marcação conservadora. Estão REPROVADOS por escopo (seção 3).
  - Resultado: a 2.7 fica com 0/18 VOLÁTEIS, ou 2/20 = 10% se a Gerência mantiver R108 e R111 como VOLÁTEIS. Não chega a 6/20 = 30% em nenhuma leitura.
  - Peço à gce-gerencia o registro expresso, como D2 de rótulo, desta sub-regra: cláusula de contrato de fornecedor é VOLÁTIL quando o gabarito depende de redação particular, e NÃO VOLÁTIL quando o ponto é conceito do instrumento.
- R120 (hipótese b) e R121 (hipótese c): VOLÁTIL baixo, mantidos.
- R125: deve passar a VOLÁTIL baixo (hipótese c). Com isso a 2.8 fica em 4/20 = 20%, no teto.
- R118 e R119: NÃO VOLÁTEIS, defensável, com registro expresso.
- R116, R122, R123, R124 e R126: NÃO VOLÁTEIS.
- Todos os 28 entram na conferência de base de 4–8/1/2027 (T-11, parte P2).

## 7. Observação da produtora: frase do curso "adaptação não corrige sotaque nem ruído"
- Onde está:
  - saida/gce/GCE_Lote2_v2_CPP.md, linha 507: seção 2.8, DEFINIÇÃO, item "Riscos", linhas 504–507;
  - a mesma frase na v1 (GCE_Lote2_v1_CPP.md, linha 408, que é histórico);
  - o campo "curso" do lote L2 em saida/pacote/pacote.json v1.9 (linha 6167 do JSON), o que significa que já foi para o pacote;
  - saida/gce/GCE_Lote2_padroes_GCE.md, linha 138: aspecto (xv) do quesito 2.4 do padrão de resposta, em lista fechada de riscos ("a adaptação não corrige sotaque nem ruído").
  - Nenhuma errata do Lote 2 (lote2_errata*.md) trata o ponto.
- É erro de curso? Não é erro frontal, mas é simplificação punível. A página do Google (aberta hoje, "Last updated 2026-10-13 UTC") lista como uso da adaptação "Improving the accuracy of speech transcription when the supplied audio contains noise or is not very clear". Um item da banca do tipo "a adaptação do modelo não melhora a acurácia em áudio ruidoso" seria E por essa fonte, e a frase do curso leva a candidata a marcar C.
- O núcleo correto: a adaptação de vocabulário ou de LM não remove o ruído nem trata a causa acústica (sotaque e ruído pedem dados acústicos, como já diz o Lote 1), mas pode melhorar o reconhecimento dos termos esperados quando o áudio é ruidoso ou pouco claro.
- O risco maior está no padrão da discursiva: o aspecto (xv) pontua a frase como está.
- Recomendação: errata do curso (linha 507) e do aspecto (xv) do padrões, D1 da gce-gerencia, com a base do Google datada. Depois, propagar ao pacote v1.10 (T-104). Esta QA não reescreve o texto.

## 8. Veredito geral
APROVADO COM RESSALVAS. Reprovados: 3/28 = 10,7%, abaixo do GATE de 30%.

Para a R2:
- repor R108 e R111 (2.7; de preferência dois E, sobre revisão em dupla ou auditoria de amostras, não VOLÁTEIS);
- repor R128 (2.8; E, não VOLÁTIL, porque a folha está no teto de 20%);
- aplicar os 8 ajustes de texto ou rótulo;
- registrar a aderência PARCIAL proposta para R130;
- obter o parecer do qa-normativo para R127–R130.

Com a saída dos três reprovados, sem reposição, o gabarito da parte fica em 14 C / 11 E (56%), ainda na faixa.

| # | id | gab. | veredito |
|---|---|---|---|
| 1 | L2-R103 | E | APROVADO |
| 2 | L2-R104 | C | AJUSTAR |
| 3 | L2-R105 | C | APROVADO |
| 4 | L2-R106 | E | AJUSTAR |
| 5 | L2-R107 | C | APROVADO |
| 6 | L2-R108 | E | REPROVADO |
| 7 | L2-R109 | E | APROVADO |
| 8 | L2-R110 | C | APROVADO |
| 9 | L2-R111 | E | REPROVADO |
| 10 | L2-R112 | C | AJUSTAR |
| 11 | L2-R113 | C | APROVADO |
| 12 | L2-R114 | E | AJUSTAR |
| 13 | L2-R115 | E | APROVADO |
| 14 | L2-R116 | C | APROVADO |
| 15 | L2-R117 | E | APROVADO |
| 16 | L2-R118 | C | AJUSTAR |
| 17 | L2-R119 | C | APROVADO |
| 18 | L2-R120 | C | APROVADO |
| 19 | L2-R121 | E | AJUSTAR |
| 20 | L2-R122 | C | APROVADO |
| 21 | L2-R123 | E | APROVADO |
| 22 | L2-R124 | C | AJUSTAR |
| 23 | L2-R125 | E | AJUSTAR |
| 24 | L2-R126 | C | APROVADO |
| 25 | L2-R127 | C | APROVADO (PENDENTE NORMATIVO) |
| 26 | L2-R128 | E | REPROVADO (PENDENTE NORMATIVO) |
| 27 | L2-R129 | E | APROVADO (PENDENTE NORMATIVO) |
| 28 | L2-R130 | E | APROVADO (PENDENTE NORMATIVO; aderência PARCIAL proposta) |
