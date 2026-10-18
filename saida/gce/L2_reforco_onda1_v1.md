# L2_reforco_onda1_v1.md — T-90 — 2026-10-18 — gerado por gce-cpp

Rótulo de todos os itens: AUTORAL (produtor gce-cpp, lote L2-R, onda 1 do reforço, D-REFORCO-1/2).
Escopo: P2 itens 2.1 a 2.8. Nenhum item existente foi alterado. QA PENDENTE até parecer da gce-cqfp.
Convenção: "verificado em 18/10/2026" = página aberta e lida nesta data. Nomenclatura: Derep (antigo DETAQ), Ato da Mesa nº 251/2026; o RICD e a página do Banco de Discursos ainda usam "Taquigrafia" e o nome antigo do departamento, e os itens usam só a palavra "Taquigrafia" do texto regimental.
Legenda de formatos: D = definição; TS = troca de sujeito (o enunciado atribui a um ator, recurso ou tipo de dado o papel que é de outro); SH = situação hipotética; NP = número ou prazo; PC = par confundível; AP = aplicação parlamentar. A classificação dos itens existentes é da CPP, por aproximação (muitos são afirmações gerais).

=====================================================================
PARTE 1/3 — MAPA
=====================================================================

## 1. Itens novos (um ponto de julgamento por item)

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL / risco |
|---|---|---|---|---|---|
| L2-R01 | P2-2.1 | O Deputado que retira o discurso para revisão e não o devolve em cinco sessões tem o texto publicado sem a revisão do orador | SH | RICD, art. 98, §2: https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html | n |
| L2-R02 | P2-2.1 | Extratos redigidos pelos próprios autores e notas taquigráficas são modalidades distintas de registro (RICD os lista separadamente) | PC | RICD, art. 57, XVIII (mesma URL) | n |
| L2-R03 | P2-2.2 | Alucinação = inclusão de texto que não consta do áudio (e não a grafia errada de palavra falada) | PC | Whisper, model card, "Performance and Limitations": https://github.com/openai/whisper/blob/main/model-card.md (lido em https://raw.githubusercontent.com/openai/whisper/main/model-card.md; a página github.com foi bloqueada pelo proxy) | n |
| L2-R04 | P2-2.2 | A avaliação do modelo no contexto e no domínio de uso, antes da implantação, é recomendação dirigida ao usuário (instituição), não ao fornecedor | TS | Whisper, model card, "Evaluated Use" (mesma URL) | n |
| L2-R05 | P2-2.3 | O aparteante só pode rever o seu aparte se o orador permitir | TS | RICD, art. 176, §5 (mesma URL do RICD) | n |
| L2-R06 | P2-2.3 | WER = (inserções + exclusões + substituições) / total de palavras da referência humana; com 3, 2, 5 e N = 50, WER = 20% | NP | Microsoft Learn, "Test accuracy of a custom speech model", "Evaluate word error rate (WER)": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | n (fórmula-padrão; o item não nomeia produto) |
| L2-R07 | P2-2.4 | Nas reuniões de comissão não há discursos individualizados, só a íntegra das notas taquigráficas (diferente do Plenário) | PC | Câmara, "Como pesquisar" (Banco de Discursos): https://www2.camara.leg.br/atividade-legislativa/discursos-e-notas-taquigraficas/pesquisa/como-pesquisar ; RICD, art. 41, XXII (mesma URL do RICD) | n (descrição institucional datada; ver observação) |
| L2-R08 | P2-2.4 | Dado o discurso por terminado pelo Presidente, os taquígrafos deixam de registrá-lo | SH | RICD, art. 73, VII e VIII (mesma URL do RICD) | n |
| L2-R09 | P2-2.5 | O art. 11 da LC 95/1998 rege a redação de leis e atos normativos; não é, por si só, a convenção de normalização das notas taquigráficas | PC | LC 95/1998, art. 1º, caput e parágrafo único, e art. 11, caput: https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp95.htm | n |
| L2-R10 | P2-2.5 | Na redação de disposições normativas, números e percentuais são grafados por extenso (exceto data e número de lei, entre outros), não em algarismos | NP | LC 95/1998, art. 11, II, "f" (redação da LC 107/2001) (mesma URL) | n |
| L2-R11 | P2-2.6 | A página de resultados do teste de precisão do Azure Speech mostra cada enunciado com a referência humana, filtra tipos de erro e permite ouvir o áudio | SH | Microsoft Learn, "Test accuracy of a custom speech model" (mesma URL de R06) | S (baixo): depende da interface do produto; REVERIFICAR |
| L2-R12 | P2-2.6 | Marcas de tempo por palavra são fornecidas pelo próprio serviço de reconhecimento, não produzidas à mão pelo revisor | TS | Google Cloud, "Get word timestamps": https://cloud.google.com/speech-to-text/docs/async-time-offsets ; AWS, "How Amazon Transcribe works": https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works.html | n (propriedade comum a mais de um fornecedor; item sem nome de produto) |
| L2-R13 | P2-2.6 | Há serviços que informam a confiança de cada palavra, dado que um editor pode usar para destacar trechos a conferir | AP | Google Cloud, "Specify word-level accuracy confidence levels": https://cloud.google.com/speech-to-text/docs/word-confidence ; AWS, "How Amazon Transcribe works" (mesma URL de R12) | n (afirmação existencial "alguns serviços") |
| L2-R14 | P2-2.7 | O terceiro contratado para assistir o fiscal do contrato não pode exercer atribuição própria e exclusiva de fiscal | AP | Lei 14.133/2021, art. 117, caput e §4º, I: https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm | n |
| L2-R15 | P2-2.7 | Os prazos e métodos do recebimento provisório e definitivo são definidos em regulamento ou no contrato, não fixados pela Lei 14.133 | NP | Lei 14.133/2021, art. 140, §3º (mesma URL de R14) | n |
| L2-R16 | P2-2.8 | O TECAD, usado na indexação dos discursos, é vocabulário controlado, com relações preestabelecidas entre os termos (não é vocabulário livre) | D | Câmara, "Como pesquisar", campo "Indexação" (mesma URL de R07) | n (descrição institucional datada; ver observação) |
| L2-R17 | P2-2.8 | Na adaptação de modelo de linguagem, os melhores dados são transcrições precisas do mesmo domínio; textos genéricos só entram na falta delas | SH → ver nota | AWS, "Custom language models", "Data sources": https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html | n (princípio de adaptação; item sem nome de produto) |
| L2-R18 | P2-2.8 | A lista de frases do Azure Speech não deve passar de 2.000 frases; listas maiores afetam qualidade e latência | NP | Microsoft Learn, "Improve recognition accuracy with phrase list": https://learn.microsoft.com/en-us/azure/ai-services/speech-service/improve-accuracy-phrase-list | S (ALTO: limite numérico de produto); REVERIFICAR |

Nota sobre R17: o enunciado compara o tipo de dado a usar (transcrição precisa do domínio × texto genérico); por atribuir a um tipo de dado o papel que é de outro, o formato declarado é TS, e a coluna acima fica corrigida aqui: formato de R17 = TS. (Não é SH.)

Observação sobre R07 e R16: descrevem a organização do Banco de Discursos no portal da Câmara (fonte institucional oficial, página aberta em 18/10/2026). Não dependem de produto de fornecedor; se a Gerência preferir tratá-las como dependentes de página, a reclassificação para VOLÁTIL (baixo) levaria 2.4 e 2.8 a 2/6 = 33,3% e 2.8 a 3 VOLÁTEIS por conta própria; por isso, a CPP as classificou como institucionais, como foram as fontes F1 e F2 do lote.

## 2. Folha a folha: pontos e formatos dos itens existentes + novos

### P2-2.1 (4 + 2 = 6)
| id | ponto | formato | VOL |
|---|---|---|---|
| L2-Q01 | Inverte definições: transcrição automática (software) × degravação (pessoa) | TS | n |
| L2-Q02 | Revisão humana usa pauta, inscritos e glossário externos ao áudio | AP | n |
| L2-Q03 | Bom desempenho em áudio bom não dispensa revisão humana de nota oficial | AP | n |
| L2-Q04 | Rascunho automático sem revisão não é registro oficial | D | n |
| L2-R01 / R02 | ver tabela acima | SH / PC | n / n |
Formatos: TS 1, AP 2, D 1, SH 1, PC 1. AP = 33,3%: excesso PRÉ-EXISTENTE (Q02, Q03); os novos não usam AP. VOLÁTIL 0/6.

### P2-2.2 (4 + 2 = 6)
| id | ponto | formato | VOL |
|---|---|---|---|
| L2-Q05 | Definição de human in the loop: saída automática é rascunho, validação humana obrigatória | D | n |
| L2-Q06 | Alta confiança não garante acerto; conferir só baixa confiança não basta | D | n |
| L2-Q07 | Revisão só ao final não detecta sempre erros iniciais (atribuição de falas) | SH | n |
| L2-Q08 | Retroalimentar glossário melhora o fluxo, mas não elimina a revisão | AP | n |
| L2-R03 / R04 | ver tabela acima | PC / TS | n / n |
Formatos: D 2, SH 1, AP 1, PC 1, TS 1. D = 33,3%: excesso PRÉ-EXISTENTE (Q05, Q06); os novos não usam D. VOLÁTIL 0/6.

### P2-2.3 (4 + 2 = 6)
| id | ponto | formato | VOL |
|---|---|---|---|
| L2-Q09 | Fidelidade não é literalidade; há graus | D | n |
| L2-Q10 | Erro que altera o sentido é mais grave que erro de grafia | PC | n |
| L2-Q11 | Trecho inaudível não se completa por conjectura sem marcação | SH | n |
| L2-Q12 | Corrigir concordância pode ser fiel, com critério editorial explícito e sentido preservado | AP | n |
| L2-R05 / R06 | ver tabela acima | TS / NP | n / n |
Formatos: D, PC, SH, AP, TS, NP com 1 cada (16,7%). VOLÁTIL 0/6.

### P2-2.4 (4 + 2 = 6)
| id | ponto | formato | VOL |
|---|---|---|---|
| L2-Q13 | Orador padronizado e troca de orador sinalizada | D | n |
| L2-Q14 | Aparteante tem rótulo próprio, distinto do orador com a palavra (RICD, art. 176, caput) | TS | n |
| L2-Q15 | Convenção de eventos não falados varia entre instituições, mas é uniforme na transcrição | AP | n |
| L2-Q16 | Nem toda pausa se registra; depende do grau de fidelidade | D | n |
| L2-R07 / R08 | ver tabela acima | PC / SH | n / n |
Formatos: D 2, TS 1, AP 1, PC 1, SH 1. D = 33,3%: excesso PRÉ-EXISTENTE (Q13, Q16); os novos não usam D. VOLÁTIL 0/6.

### P2-2.5 (4 + 2 = 6)
| id | ponto | formato | VOL |
|---|---|---|---|
| L2-Q17 | Normalização inversa converte fala em forma escrita, depois do reconhecimento | D | n |
| L2-Q18 | Normalização padroniza a forma; não corrige o conteúdo dito | D | n |
| L2-Q19 | Sem regra, a mesma sigla ou número aparece grafado de formas diferentes | SH | n |
| L2-Q20 | Expandir ou não a sigla é convenção; "sempre" e "única forma" erram | AP | n |
| L2-R09 / R10 | ver tabela acima | PC / NP | n / n |
Formatos: D 2, SH 1, AP 1, PC 1, NP 1. D = 33,3%: excesso PRÉ-EXISTENTE (Q17, Q18); os novos não usam D. VOLÁTIL 0/6.

### P2-2.6 (3 + 3 = 6)
| id | ponto | formato | VOL |
|---|---|---|---|
| L2-Q21 | CAT do edital é transcrição assistida, não memória de tradução | PC | n |
| L2-Q22 | Editores sincronizam texto e áudio por marcas de tempo | D | n |
| L2-Q23 | WebVTT (W3C) organiza segmentos com tempo e pode indicar o falante | D | n |
| L2-R11 / R12 / R13 | ver tabela acima | SH / TS / AP | S (baixo) / n / n |
Formatos: PC 1, D 2, SH 1, TS 1, AP 1. D = 33,3%: excesso PRÉ-EXISTENTE (Q22, Q23); os novos não usam D. VOLÁTIL 1/6 = 16,7% (teto de 20% cumprido).

### P2-2.7 (4 + 2 = 6)
| id | ponto | formato | VOL |
|---|---|---|---|
| L2-Q24 | Revisão em dupla exige segundo revisor independente | PC | n |
| L2-Q25 | Auditoria por amostragem reexamina parte para estimar a qualidade do conjunto | D | n |
| L2-Q26 | Amostra sem erro não prova ausência de erro nas peças não examinadas | SH | n |
| L2-Q27 | SLA pode fixar prazo e qualidade; prazo cumprido não comprova o acordo | D | n |
| L2-R14 / R15 | ver tabela acima | AP / NP | n / n |
Formatos: PC 1, D 2, SH 1, AP 1, NP 1. D = 33,3%: excesso PRÉ-EXISTENTE (Q25, Q27); os novos não usam D. VOLÁTIL 0/6.

### P2-2.8 (3 + 3 = 6)
| id | ponto | formato | VOL |
|---|---|---|---|
| L2-Q28 | LM adaptado muda a probabilidade de sequências e ajuda a desambiguar pelo contexto | AP | n |
| L2-Q29 | OOV é termo ausente do vocabulário, não termo de baixa confiança | PC | n |
| L2-Q30 | Reforço máximo de termos não é sempre vantajoso; pode inserir o termo onde não foi dito | SH | n |
| L2-R16 / R17 / R18 | ver tabela acima | D / TS / NP | n / n / S (ALTO) |
Formatos: AP, PC, SH, D, TS, NP com 1 cada (16,7%). VOLÁTIL 1/6 = 16,7% (teto de 20% cumprido).

## 3. Verificação de não repetição
Em cada folha, o ponto de cada item novo foi comparado, item a item, com os pontos acima (que vêm de saida/pacote/pacote.json e dos canônicos GCE_Lote2_v2_CPP.md, GCE_Lote2_padroes_GCE.md e GCE_Lote2_consolidacao_GCE.md). Nenhum coincide. Proximidades que a Gerência pode querer ver:
- R12 (2.6) × Q22 (2.6): ambos tratam de marca de tempo; Q22 julga a função (sincronizar texto e áudio), R12 julga a origem (o serviço fornece, o revisor não digita).
- R15 (2.7) × Q27 (2.7): ambos tocam prazo contratual; Q27 julga o que o SLA pode fixar (prazo e qualidade), R15 julga quem define os prazos do recebimento (regulamento ou contrato, não a lei).
- R17 (2.8) × Q28 (2.8): ambos tratam de modelo de linguagem; Q28 julga o efeito do LM adaptado (sequências), R17 julga qual dado de treino é o melhor.
- R05 (2.3) × Q14 (2.4): mesmo artigo (RICD, art. 176), folhas diferentes e parágrafos diferentes (caput × §5).
- R03 (2.2) × Q06 (2.2): ambos tocam erro de modelo com texto fluente; Q06 julga a confiança como critério de revisão, R03 julga o que a palavra "alucinação" designa.

## 4. Tetos (resumo)
- Formato: nenhum formato recebe item novo quando já está em 2 de 4 (ou 2 de 3) na folha. Excessos de 33,3% (2 de 6) em 2.1, 2.2, 2.4, 2.5, 2.6 e 2.7 são anteriores à onda e não mudam (regra "nenhum item existente muda"); com 6 itens por folha, 30% equivale a 1,8 e só seria cumprido com seis formatos distintos. Em 2.3 e 2.8, os seis formatos aparecem uma vez cada.
- VOLÁTIL: 2 novos (R11, R18) + 0 existentes = 2 no lote (teto 4); 1 de risco alto (R18); por folha, 2.6 e 2.8 com 1/6 = 16,7% (teto 20%), as demais com 0.
- Gabarito: 8 C e 10 E (44% de C), dentro de 7 a 11 C.

FIM DA PARTE 1/3

=====================================================================
PARTE 2/3 — (d) ITENS DO ESTUDANTE
=====================================================================

L2-R01. Julgue o item.
Um Deputado retirou na Taquigrafia, para revisão, o texto de um discurso que proferiu em Plenário e não o devolveu dentro de cinco sessões. Nessa situação, a Taquigrafia dá à publicação o texto sem a revisão do orador.

L2-R02. Julgue o item.
O Regimento Interno da Câmara dos Deputados, ao tratar da publicação dos trabalhos das Comissões, menciona separadamente os extratos redigidos pelos próprios autores e as notas taquigráficas, tratando-os como modalidades distintas de registro, e não como expressões sinônimas.

L2-R03. Julgue o item.
No contexto dos modelos de reconhecimento de fala, denomina-se alucinação o erro em que uma palavra efetivamente pronunciada é grafada de modo incorreto, e não a inclusão, na transcrição, de texto que não consta do áudio.

L2-R04. Julgue o item.
Em um fluxo de degravação assistida por IA, compete ao fornecedor do modelo de reconhecimento de fala, e não à instituição que pretende adotá-lo, avaliar o desempenho do modelo no contexto e no domínio de uso, como o das sessões legislativas, antes de sua implantação.

L2-R05. Julgue o item.
Segundo o Regimento Interno da Câmara dos Deputados, o Deputado que proferiu um aparte pode rever o texto desse aparte independentemente de permissão do orador que estava com a palavra.

L2-R06. Julgue o item.
Para avaliar uma transcrição automática, tomou-se como referência a transcrição revisada por pessoa, com 50 palavras. O sistema acrescentou 3 palavras que não constam da referência, deixou de reconhecer 2 e substituiu 5. Nessa situação, a taxa de erro de palavras (WER) foi de 20%.

L2-R07. Julgue o item.
No Banco de Discursos da Câmara dos Deputados, as reuniões de comissão, tal como as sessões plenárias, são organizadas em discursos individualizados de cada orador, de modo que a consulta recupera o pronunciamento isolado de cada participante.

L2-R08. Julgue o item.
Em sessão plenária, o Presidente adverte o Deputado que insiste em permanecer na tribuna de modo antirregimental e, diante da persistência, dá o discurso por terminado. A partir desse momento, os taquígrafos deixam de registrar o que o Deputado continuar a dizer.

L2-R09. Julgue o item.
As regras do art. 11 da Lei Complementar nº 95/1998 sobre o uso de siglas e a grafia de números destinam-se à redação de leis e demais atos normativos, de modo que não constituem, por si sós, a convenção de normalização aplicável às notas taquigráficas das sessões.

L2-R10. Julgue o item.
Segundo o art. 11, inciso II, alínea "f", da Lei Complementar nº 95/1998, na redação de disposições normativas, as referências a números e percentuais devem ser grafadas em algarismos, exceto data e número de lei.

L2-R11. Julgue o item.
Uma equipe da Casa avalia, no Azure Speech, a transcrição automática de reuniões de comissão. Conforme a documentação do fornecedor, a página de resultados do teste de precisão lista cada enunciado do conjunto, exibe o resultado do reconhecimento ao lado da transcrição de referência feita por pessoas, permite alternar tipos de erro, como inserção, exclusão e substituição, e permite ouvir o áudio para comparar os resultados.

L2-R12. Julgue o item.
Nos serviços de reconhecimento de fala que oferecem marcação de tempo por palavra, os carimbos de tempo são produzidos manualmente pelo revisor, e não fornecidos pelo próprio serviço na saída do reconhecimento.

L2-R13. Julgue o item.
Alguns serviços de reconhecimento de fala informam, além da confiança da transcrição como um todo, a confiança de cada palavra reconhecida; em um editor de transcrição de sessões parlamentares, essa informação pode ser usada para destacar os trechos que merecem conferência pelo revisor.

L2-R14. Julgue o item.
Para auxiliá-lo na aferição da qualidade dos serviços de transcrição das sessões, o fiscal do contrato pode contratar uma empresa de apoio, a qual passa a poder exercer, em lugar do fiscal, as atribuições próprias e exclusivas da fiscalização do contrato.

L2-R15. Julgue o item.
Em contrato de prestação de serviços de transcrição, a Lei nº 14.133/2021 fixa em quinze dias o prazo para o recebimento provisório do objeto, não podendo o contrato nem o regulamento dispor de modo diverso.

L2-R16. Julgue o item.
No Banco de Discursos da Câmara dos Deputados, a indexação temática dos discursos recorre ao Tesauro da Câmara dos Deputados (TECAD), concebido como vocabulário livre, no qual não há estrutura preestabelecida de relações entre os termos.

L2-R17. Julgue o item.
Para adaptar um modelo de linguagem ao vocabulário das reuniões de uma comissão, os dados de treinamento mais indicados são textos genéricos, como notícias, e não transcrições precisas de reuniões semelhantes àquelas que se pretende transcrever.

L2-R18. Julgue o item.
A documentação do Azure Speech recomenda que uma lista de frases (phrase list) não ultrapasse 2.000 frases, porque listas mais longas afetam a qualidade e a latência do reconhecimento.

FIM DA PARTE 2/3

=====================================================================
PARTE 3/3 — (d-G) GABARITO COMENTADO
=====================================================================
Legenda: [TS] = troca sutil de um único conceito (nos itens C, "espelho": item construído como a negação de uma troca sutil). VOLÁTIL = depende de produto/versão. REVERIFICAR = reabrir a fonte na reverificação de 4–8/1/2027. Páginas abertas em 18/10/2026.

L2-R01. C. Se o Deputado não devolve o discurso retirado para revisão em cinco sessões, a Taquigrafia publica o texto sem a revisão do orador.
Base: RICD, art. 98, §2 (o RICD diz "Taquigrafia"; a denominação atual do órgão é Derep, antigo DETAQ, Ato da Mesa nº 251/2026, o que não altera o artigo).

L2-R02. C [TS]. O inciso XVIII do art. 57 lista, em alternativa, as exposições escritas e os resumos das orais, os extratos redigidos pelos próprios autores e as notas taquigráficas, a critério da Comissão; são modalidades distintas, não sinônimos.
Base: RICD, art. 57, XVIII. Espelho da troca sutil "extrato = nota taquigráfica".

L2-R03. E [TS]. Troca: alucinação é a inclusão de texto que não foi dito no áudio, não o erro de grafia de palavra falada.
Base: Whisper, model card, "Performance and Limitations" ("the predictions may include texts that are not actually spoken in the audio input (i.e. hallucination)").

L2-R04. E [TS]. Troca de sujeito: a documentação recomenda que os usuários façam avaliações robustas no contexto e no domínio de uso antes da implantação; a avaliação cabe à instituição, não ao fornecedor.
Base: Whisper, model card, "Evaluated Use" ("We strongly recommend that users perform robust evaluations of the models in a particular context and domain before deploying them").

L2-R05. E [TS]. Os apartes só são sujeitos a revisão do autor se o orador a permitir; o item troca a condição ("se permitida pelo orador") por "independentemente de permissão". O trecho final do parágrafo ("que não poderá modificá-los") não foi usado por ser ambíguo quanto ao antecedente.
Base: RICD, art. 176, §5.

L2-R06. C. WER = (I + D + S) / N × 100 = (3 + 2 + 5) / 50 × 100 = 20%, em que N é o total de palavras da transcrição de referência feita por pessoa. Item aritmético; o erro típico é dividir pelo número de palavras do sistema ou ignorar as inserções.
Base: Microsoft Learn, "Test accuracy of a custom speech model", seção "Evaluate word error rate (WER)" (WER como padrão da indústria; inserção, exclusão e substituição; divisão pelo total de palavras da transcrição rotulada por humanos).

L2-R07. E. Nas sessões plenárias há discursos individualizados; nas reuniões de comissão "não há discursos individualizados", apenas a íntegra das notas taquigráficas. Além disso, nem toda reunião de comissão tem nota taquigráfica, pois o registro taquigráfico é determinado pelo Presidente da Comissão quando julgar necessário.
Base: Câmara, "Como pesquisar" (informações sobre notas taquigráficas de Comissões); RICD, art. 41, XXII.

L2-R08. C. O art. 73, VII, prevê a advertência e, na insistência, o término do discurso pelo Presidente; o inciso VIII manda os taquígrafos deixarem de registrá-lo quando o Presidente der por findo o discurso.
Base: RICD, art. 73, VII e VIII.

L2-R09. C [TS]. O art. 1º da LC 95/1998 submete à lei complementar a elaboração, a redação, a alteração e a consolidação das leis e os atos normativos do art. 59 da CF; o art. 11 trata das "disposições normativas". Notas taquigráficas não são ato normativo; espelho da troca sutil "a LC 95 dita a normalização das transcrições".
Base: LC 95/1998, art. 1º, caput e parágrafo único; art. 11, caput.

L2-R10. E [TS]. Troca: a regra manda grafar por extenso (não em algarismos) as referências a números e percentuais, exceto data, número de lei e casos de prejuízo para a compreensão.
Base: LC 95/1998, art. 11, II, "f" (redação dada pela LC 107/2001).

L2-R11. C. VOLÁTIL (baixo); REVERIFICAR. A documentação descreve a página de resultados com a lista de enunciados, o resultado ao lado da transcrição do conjunto de dados rotulado por humanos, a alternância dos tipos de erro (inserção, exclusão e substituição) e a audição do áudio para comparar.
Base: Microsoft Learn, "Test accuracy of a custom speech model" (seção de resultados do teste). Depende da interface do produto; fonte oficial do fornecedor.

L2-R12. E [TS]. Troca de sujeito: as saídas de reconhecimento trazem os tempos de cada palavra (início e fim, a partir do início do áudio) calculados pelo serviço; o revisor os usa, não os digita.
Base: Google Cloud, "Get word timestamps" (valores de deslocamento de tempo retornados na resposta ao solicitar); AWS, "How Amazon Transcribe works" (transcrições com confiança e marcas de tempo de cada palavra ou sinal).

L2-R13. C. Há serviços que fornecem a confiança por palavra além da confiança da transcrição inteira; o uso para destacar trechos é aplicação possível, não recurso atribuído a produto. A confiança orienta a conferência, sem garantir acerto (ver L2-Q06).
Base: Google Cloud, "Specify word-level accuracy confidence levels"; AWS, "How Amazon Transcribe works".

L2-R14. E [TS]. A contratação de terceiros para assistir o fiscal é permitida, mas o terceiro "não poderá exercer atribuição própria e exclusiva de fiscal de contrato", e o fiscal continua responsável nos limites das informações recebidas.
Base: Lei 14.133/2021, art. 117, caput e §4º, I e II.

L2-R15. E [TS]. Troca: os prazos e os métodos dos recebimentos provisório e definitivo são definidos em regulamento ou no contrato (art. 140, §3º); a lei não fixa "quinze dias" para o recebimento provisório.
Base: Lei 14.133/2021, art. 140, §3º (leitura do art. 140 inteiro: não há prazo numérico para o recebimento provisório nesse artigo).

L2-R16. E [TS]. Troca: o TECAD é "vocabulário controlado organizado em uma ordem preestabelecida", com relacionamentos de equivalência, homografia, hierarquia e associação entre termos, não vocabulário livre.
Base: Câmara, "Como pesquisar", campo "Indexação" (TECAD 1.0, Tesauros da Câmara dos Deputados).

L2-R17. E [TS]. Troca: os melhores dados são transcrições precisas (dados do mesmo domínio, com os mesmos termos, uso e contexto do áudio); textos relacionados, como artigos, atas e notícias, só são alternativa quando faltam transcrições.
Base: AWS, "Custom language models", seção "Data sources" ("the closer your text content is to your audio content, the more accurate your model"; "the best data for training a model are accurate transcripts").

L2-R18. C. VOLÁTIL (ALTO: limite numérico de produto); REVERIFICAR. A página afirma que uma lista de frases não deve ter mais de 2.000 frases e que listas mais longas afetam a qualidade e a latência.
Base: Microsoft Learn, "Improve recognition accuracy with phrase list" (fonte oficial do fornecedor). Se a página mudar o número antes de janeiro, reescrever o item sem o limite.

## Contagens
| quesito | valor |
|---|---|
| total | 18 |
| C | 8 (R01, R02, R06, R08, R09, R11, R13, R18) |
| E | 10 (R03, R04, R05, R07, R10, R12, R14, R15, R16, R17) |
| [TS] | 11 (R02, R03, R04, R05, R09, R10, R12, R14, R15, R16, R17): 2 com gabarito C (R02, R09) e 9 com gabarito E |
| VOLÁTIL | 2 novos: R11 (2.6, risco baixo) e R18 (2.8, risco ALTO). Existentes no lote: 0. Total no lote: 2 (teto 4); risco alto: 1 (teto 1) |
| VOLÁTIL por folha | 2.1: 0; 2.2: 0; 2.3: 0; 2.4: 0; 2.5: 0; 2.6: 1 de 6 (16,7%); 2.7: 0; 2.8: 1 de 6 (16,7%) |
| distribuição por folha | 2.1: 2; 2.2: 2; 2.3: 2; 2.4: 2; 2.5: 2; 2.6: 3; 2.7: 2; 2.8: 3 (soma 18) |
| C por folha | 2.1: 2 C; 2.2: 0; 2.3: 1; 2.4: 1; 2.5: 1; 2.6: 2; 2.7: 0; 2.8: 1 |

## Tabela de proveniência (todas abertas e lidas em 18/10/2026)
| fonte | URL oficial | data da página / verificação | usada em |
|---|---|---|---|
| Câmara dos Deputados, Regimento Interno (Resolução nº 17/1989, texto atualizado, Legin) | https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html | verificado em 18/10/2026 (arts. 41, XXII; 57, XVIII; 73, VI a VIII; 98, §§1º e 2º; 176, §§4º e 5º) | R01, R02, R05, R07, R08 |
| Câmara dos Deputados, Banco de Discursos, "Como pesquisar" | https://www2.camara.leg.br/atividade-legislativa/discursos-e-notas-taquigraficas/pesquisa/como-pesquisar | verificado em 18/10/2026 (página sem data de edição visível) | R07, R16 |
| Presidência da República, Lei Complementar nº 95/1998 (compilada) | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp95.htm | verificado em 18/10/2026 (art. 11, II, "f", com a redação da LC 107/2001) | R09, R10 |
| Presidência da República, Lei nº 14.133/2021 (compilada) | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm | verificado em 18/10/2026 (arts. 117 e 140) | R14, R15 |
| OpenAI, repositório openai/whisper, model card | https://github.com/openai/whisper/blob/main/model-card.md | arquivo lido em https://raw.githubusercontent.com/openai/whisper/main/model-card.md em 18/10/2026 (a página github.com foi bloqueada pelo proxy do ambiente) | R03, R04 |
| Microsoft Learn, Azure Speech, "Test accuracy of a custom speech model" | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-evaluate-data | verificado em 18/10/2026 (página sem data de edição extraída) | R06, R11 |
| Microsoft Learn, Azure Speech, "Improve recognition accuracy with phrase list" | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/improve-accuracy-phrase-list | verificado em 18/10/2026 | R18 |
| Google Cloud, Speech-to-Text, "Get word timestamps" | https://cloud.google.com/speech-to-text/docs/async-time-offsets | verificado em 18/10/2026 | R12 |
| Google Cloud, Speech-to-Text, "Specify word-level accuracy confidence levels" | https://cloud.google.com/speech-to-text/docs/word-confidence | verificado em 18/10/2026 | R13 |
| AWS, Amazon Transcribe, "How Amazon Transcribe works" | https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works.html | verificado em 18/10/2026 | R12, R13 |
| AWS, Amazon Transcribe, "Custom language models" | https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html | verificado em 18/10/2026 | R17 |

Fontes que não consegui abrir (nenhum item delas entrou): w3.org (WebVTT), platform.openai.com e github.com (HTML), docs.nvidia.com, ojp.gov (resumo do OJP sobre CAT), camara.leg.br/internet/SitaqWeb (Banco de Discursos, pesquisa avançada). O PDF "Rol do DETAQ" abriu, mas é de setembro de 2009 e não foi usado como base.

FIM DA PARTE 3/3
FIM DO LOTE
