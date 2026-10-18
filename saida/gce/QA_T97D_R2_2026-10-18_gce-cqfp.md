# QA_T97D_R2_2026-10-18_gce-cqfp.md — T-97 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L2_reforco_onda3_D_v2.md (gce-cpp), SHA-256 31a3c4c2b1c2fab74bf351d56e125ce443202543e4c384f254b6379baf6d01f4. É a rodada R2, a última. Esta QA revisa e não reescreve: diz onde está o problema e por quê.
Lidos: meu parecer R1 (QA_T97D_R1_2026-10-18_gce-cqfp.md); QA_T97D_normativo_2026-10-18_qa-normativo.md (R127 a R130 da v1: CONFERE, 0 divergência); v1 e v2 do objeto; L2_reforco_onda3_A_v2.md (L2-R43); edital/modulo_RF_IA_P2.md (2.7 e 2.8); DECISOES.md (D-REFORCO-2, D-ADERENCIA, D-T90-R2-ACEITE; D-T96-ONDA2-ACEITE (II) nos termos citados no objeto); pacote.json v1.9, buscado por texto.

## 1. Diff v1 → v2 (script python -I: enunciado, gabarito e linha do mapa, item a item)
- Enunciados alterados: R104, R106, R108, R111, R112, R114, R121, R124 e R128. Os outros 19 estão idênticos.
- Gabaritos alterados: R104, R108, R111, R118, R124, R125, R127, R128, R129 e R130. Os outros 18 estão idênticos.
- Linhas de mapa alteradas: R104, R108, R111, R118, R124, R125, R127, R128, R129 e R130.
- Fora dos itens, mudaram só o bloco de resposta no topo e as seções 1.3, 1.4, 1.5, contagens, observações de estilo e proveniência, que dependem das mudanças. Não encontrei nenhuma alteração que a resposta não declare.
- Estrutura:
  - 28 enunciados e 28 gabaritos, com os mesmos ids.
  - A Parte 2 não tem gabarito, [TS], VOLÁTIL nem REVERIFICAR.
  - "FIM DO LOTE" está presente.
- Contagens:
  - Gabarito: 14 C / 14 E (50,0%); 7 C / 7 E em cada folha.
  - [TS]: 18 de 28.
  - VOLÁTIL: 3 novos (R120, R121 e R125).
  - Todas as contagens declaradas conferem.
- Extensão:
  - C: média de 46,3 palavras (de 40 a 51).
  - E: média de 47,4 palavras (de 28 a 58).
  - O E mais curto é o R114, com 28 palavras. Como o E é mais curto, não há pista de extensão a favor do C (O-1).

## 2. Ajustes e marcas da R1: conferência pelo texto exato
| id | pedido da R1 | texto da v2 | resultado |
|---|---|---|---|
| R104 | atribuir a orientação ao Google, com a ambientação fora da remissão | "A equipe da Câmara calcula o WER do ASR usado nas comissões. Segundo a documentação do Google Cloud Speech-to-Text, a transcrição de referência deve ter convenções…" | APLICADO |
| R106 | fechar com juízo explícito | "… Nessa situação, o entendimento da Câmara está correto." O gabarito continua E. | APLICADO |
| R112 | "o sclite, do NIST, totaliza…" | literal | APLICADO |
| R114 | o E deve depender da base, sem cauda que se denuncia | "o valor global do WER basta para direcionar as melhorias, dispensando a análise da distribuição dos erros." | APLICADO. O E agora depende de "How the errors are distributed is important." (página reaberta hoje, seção 3) |
| R118 | AP → D | O mapa traz D. A justificativa registra a reclassificação e o não VOLÁTIL com o pedido de registro à Gerência. | APLICADO |
| R121 | fechar com juízo explícito | "… Nessa situação, a suposição da equipe está correta." O gabarito continua E. | APLICADO |
| R124 | forma literal | "quando faltam dados de treinamento do próprio domínio", no enunciado, no mapa e no gabarito. Corresponde a "when you lack in-domain training data". | APLICADO |
| R125 | VOLÁTIL baixo, critério (c) | aparece no mapa ("S (BAIXO)"), no gabarito ("VOLÁTIL (baixo)") e no registro 1 | APLICADO |
| R127, R129 | marcar CONFERE | aparece no mapa e no gabarito | APLICADO |
| R130 | aderência PARCIAL; citar o art. 66, § 1º; acrescentar o parágrafo único do art. 90 (qa-normativo) | O mapa traz "PARCIAL (D-ADERENCIA…)". A base é "arts. 66, IV e § 1º, 89, caput, e 90, caput e parágrafo único", com o trecho literal do parágrafo único. A justificativa cita o § 1º. | APLICADO |

R118 e o teto de formato: na 2.8, o formato D fica com R16, R118, R127 e R128 = 4/20 = 20%. Está dentro do teto de 30% (6/20), e o maior formato da folha é TSj, com 5/20 = 25%. Na R1 eu tinha estimado D em 3/20 contando com a saída do R128 antigo. Como o R128 novo também é D, a conta correta é 4/20, ainda sob o teto. Na 2.7, o maior formato é SH, com 25%, e D fica em 2/20 (legado diluído).

VOLÁTIL por folha:
- 2.7: 0/20.
- 2.8: 4/20 = 20% (R18, R120, R121, R125), no teto. O R128 novo é norma e não é VOLÁTIL. Cumpre a regra 4 da D-REFORCO-2.

## 3. Evidência: URLs reabertas pela QA hoje (18/10/2026; curl com User-Agent de navegador; texto extraído com python -I)
| # | URL | resultado |
|---|---|---|
| 1 | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-inspect-data | HTTP 200. Trecho do R108 literal: "You can play back uploaded audio and determine if the provided recognition result is correct." A mesma página diz: "For an objective measure of accuracy, which requires transcription datase[ts]…", o que reforça o E. Sobre a data: o metadado ms.date é 2025-12-29, mas a página exibe "Last updated on 2026-06-02". A proveniência cita só o ms.date e deve registrar a data exibida (correção de registro na reconciliação, sem efeito no item). |
| 2 | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-human-labeled-transcriptions | HTTP 200; "Last updated on 2025-12-29", que coincide com o ms.date. Os dois trechos do R111 são literais: "A representative sample of transcription data is recommended to evaluate model accuracy. The data should cover various speakers and utterances…" e "A large sample of transcription data is required to improve recognition." Os números da página (1 a 100 horas, 40 s) não são cobrados. |
| 3 | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | HTTP 200. O trecho do R114 reajustado ("How the errors are distributed is important.") continua na página. |
| 4 | Legin, RICD, texto atualizado (www2.camara.leg.br/…320110-normaatualizada-pl.html) | HTTP 200, 1.007.742 bytes. Art. 126, caput, literal e sem marca de alteração: "Parecer é a proposição com que uma Comissão se pronuncia sobre qualquer matéria sujeita a seu estudo." O art. 100, § 1º, inclui "parecer" entre as proposições, o que confirma "proposição". No mesmo texto aparece "Plenário da Comissão" ("A discussão e a votação do parecer e da proposição serão realizadas pelo Plenário da Comissão"), o que pesa no R128 (seção 4). A conferência formal é do qa-normativo, em paralelo. |

Nenhuma afirmação dos itens novos ficou sem fonte datada.

## 4. Os três itens novos, por inteiro
- **L2-R108 (2.7; E [TS]; TSj; não VOLÁTIL): APROVADO.**
  - Gabarito E firme. A base atribui à pessoa que reproduz o áudio a decisão sobre a correção do resultado, e a medida objetiva exige transcrições.
  - Troca única: pessoa → serviço automático. A oração "e a equipe não precisa reproduzir o áudio" é corolário da mesma troca, e não um segundo conceito. Isoladamente seria discutível, porque a página diz "You can", mas o E é decidido pela primeira oração.
  - Aderência direta: é conferência humana do resultado, controle de qualidade do 2.7.
  - Não VOLÁTIL é defensável: é funcionamento documentado, sem número, versão nem condição.
  - Ponto único na folha: é vizinho do R115 (dados somente de áudio servem à inspeção, e não à quantificação), mas com outro ponto (quem decide na inspeção). Registro para a GBQ: R108 e R115 não devem ir ao mesmo caderno. No pacote, nenhum item tem o mesmo ponto (busca por "inspeção", "play back" e "reproduz o áudio").
  - Estilo: a ambientação está em frase própria, fora da remissão.
- **L2-R111 (2.7; E [TS]; PC; não VOLÁTIL): APROVADO.**
  - Gabarito E firme. A segunda oração ("basta uma amostra representativa" para melhorar) contraria frontalmente "A large sample… is required to improve recognition".
  - Troca única: as duas finalidades são permutadas, o que é um só conceito.
  - Aderência direta: amostra para avaliação, que é o lado de "auditoria de amostras" do 2.7.
  - Não VOLÁTIL: recomendação sem número cobrado.
  - Comparação com o L2-R43 (parte A v2, 2.2; C), que julga a composição do conjunto de teste (entradas reais da produção, amostradas ao acaso e renovadas periodicamente). O R111 julga a finalidade de cada amostra (representativa para avaliar, grande para melhorar). A vizinhança está em "representativa do que os usuários dizem", que tangencia "real user variations" do R43, mas o que decide o R111 é a troca de finalidade e de tamanho, que o R43 não toca.
  - Conclusão: não é gêmeo; o ponto é único na folha e no pacote. Registro para a GBQ: R111 e L2-R43 não devem ir ao mesmo caderno (T96, seção 4). O par está declarado na seção 1.3 do objeto.
- **L2-R128 (2.8; E [TS]; D; não VOLÁTIL): AJUSTAR (mínimo, não bloqueante; D1 da gce-gerencia; PENDENTE NORMATIVO até o parecer do qa-normativo).**
  - Gabarito E firme pelo art. 126, caput. Troca única: Comissão → Plenário.
  - Aderência direta: "parecer" é termo regimental central do vocabulário técnico parlamentar (o curso do 2.8 lista termos regimentais), e a ambientação na revisão de nota taquigráfica de comissão é verossímil.
  - Ponto único: nenhum item do pacote v1.9 nem das partes A, B ou C define parecer (a busca por "art. 126" e "Parecer é a proposição" não encontrou nada). O L2-R63, da parte B, julga o aparte a parecer oral, que é outro ponto.
  - Formato: D. Não VOLÁTIL. A ambientação está fora da remissão.
  - Defeito de redação: o RICD usa "Plenário da Comissão" (lido hoje no Legin). Com "o Plenário" sem qualificação, um recurso pode sustentar que a Comissão se pronuncia por seu Plenário, o que daria leitura C.
  - Texto exato do ajuste: trocar "com que o Plenário se pronuncia" por "com que o Plenário da Câmara se pronuncia". O gabarito, o [TS] e a justificativa não mudam ("Troca sutil: Comissão por Plenário da Câmara").
  - Por ser a última rodada, o ajuste fica para a reconciliação, sem R3.

## 5. Posição sobre o "não acatado"
- **Revisão em dupla em sentido estrito.** A produtora não repôs item sobre segundo revisor independente, por falta de trecho literal oficial aberto hoje, e registrou a lacuna. Minha recomendação na R1 foi "de preferência", e não condição, e a regra 2 da D-REFORCO-2 proíbe item sem base. Aceito a recusa como fundamentada.
  - A cobertura do 2.7 fica assim: revisão em dupla com Q24 e, indiretamente, R103 (passagem dupla) e R108 (conferência humana); auditoria de amostras com Q25, Q26, R111, R112 e R113; SLA com Q27, R106, R107, R109 e R110. A lacuna é de profundidade, e não de cobertura do enunciado do edital.
  - Peço à gce-gerencia o registro da lacuna para a consolidação v1.10 ou para uma onda posterior, com base na própria Câmara ou em norma técnica oficial, se houver.
- **Errata do curso (seção 7 da R1).** Fica fora deste arquivo, o que está correto. Continua aberta para a gce-gerencia: errata da linha 507 do GCE_Lote2_v2_CPP.md e do aspecto (xv) do padrões, e depois propagação ao pacote v1.10 (T-104). Não é condição do aceite desta parte.

## 6. Normativo
- R127, R129 e R130: CONFERE pelo qa-normativo. Sai a marca PENDENTE NORMATIVO.
- R128 (novo; RICD, art. 126, caput): PENDENTE NORMATIVO até o parecer paralelo do qa-normativo. A QA conferiu o trecho literal no Legin hoje.
- Não há lei federal nesta parte.

## 7. Veredito por item (R2)
| # | id | folha | gab. | veredito R2 |
|---|---|---|---|---|
| 1 | L2-R103 | 2.7 | E | APROVADO |
| 2 | L2-R104 | 2.7 | C | APROVADO (ajuste aplicado) |
| 3 | L2-R105 | 2.7 | C | APROVADO (par com L2-Q06 registrado) |
| 4 | L2-R106 | 2.7 | E | APROVADO (ajuste aplicado) |
| 5 | L2-R107 | 2.7 | C | APROVADO |
| 6 | L2-R108 | 2.7 | E | APROVADO (novo; não ir ao mesmo caderno que R115) |
| 7 | L2-R109 | 2.7 | E | APROVADO |
| 8 | L2-R110 | 2.7 | C | APROVADO |
| 9 | L2-R111 | 2.7 | E | APROVADO (novo; não ir ao mesmo caderno que L2-R43) |
| 10 | L2-R112 | 2.7 | C | APROVADO (ajuste aplicado) |
| 11 | L2-R113 | 2.7 | C | APROVADO |
| 12 | L2-R114 | 2.7 | E | APROVADO (ajuste aplicado) |
| 13 | L2-R115 | 2.7 | E | APROVADO |
| 14 | L2-R116 | 2.7 | C | APROVADO (ressalva registrada) |
| 15 | L2-R117 | 2.8 | E | APROVADO |
| 16 | L2-R118 | 2.8 | C | APROVADO (D; não VOLÁTIL com registro da Gerência) |
| 17 | L2-R119 | 2.8 | C | APROVADO |
| 18 | L2-R120 | 2.8 | C | APROVADO (VOLÁTIL baixo) |
| 19 | L2-R121 | 2.8 | E | APROVADO (ajuste aplicado; VOLÁTIL baixo) |
| 20 | L2-R122 | 2.8 | C | APROVADO |
| 21 | L2-R123 | 2.8 | E | APROVADO |
| 22 | L2-R124 | 2.8 | C | APROVADO (ajuste aplicado) |
| 23 | L2-R125 | 2.8 | E | APROVADO (VOLÁTIL baixo aplicado) |
| 24 | L2-R126 | 2.8 | C | APROVADO |
| 25 | L2-R127 | 2.8 | C | APROVADO (CONFERE) |
| 26 | L2-R128 | 2.8 | E | AJUSTAR (mínimo: "Plenário da Câmara"; PENDENTE NORMATIVO) |
| 27 | L2-R129 | 2.8 | E | APROVADO (CONFERE) |
| 28 | L2-R130 | 2.8 | E | APROVADO (CONFERE; aderência PARCIAL, só simulado diagnóstico) |

Taxa: REPROVADO 0/28 = 0%; AJUSTAR 1/28 (R128, não bloqueante); APROVADO 27/28. O GATE de 30% não é atingido.

## 8. Veredito geral
APROVADO COM RESSALVAS, com 0% de reprovação. As ressalvas são para a reconciliação da gce-gerencia:
- (1) aplicar o ajuste exato do R128 e receber o CONFERE do qa-normativo sobre o art. 126;
- (2) corrigir a data da proveniência do R108 ("Last updated on 2026-06-02");
- (3) fazer em D1/D2 os registros pedidos: R118/R119 não VOLÁTEIS; sub-regra de cláusula de SLA; R130 PARCIAL; lacuna da revisão em dupla em sentido estrito;
- (4) registrar para a GBQ os pares R105 × L2-Q06, R108 × R115 e R111 × L2-R43;
- (5) a errata do curso (seção 7 da R1) segue em separado.

Todos os 28 itens entram na conferência de base de 4–8/1/2027 (T-11, parte P2), e R120, R121 e R125 também como VOLÁTEIS.
