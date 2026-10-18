# T106_errata_proposta_2026-10-18.md — T-106 — 2026-10-18 — gerado por gce-cpp

Objeto: ERRATA do Lote 2 em dois pontos (curso 2.8, "Riscos"; aspecto (xv) do quesito 2.4 do padrão de resposta da peça). PROPOSTA: nada foi aplicado nos arquivos canônicos (GCE_Lote2_v2_CPP.md e GCE_Lote2_padroes_GCE.md, ambos em CRLF: a aplicação deve preservar CRLF). Nenhum item, gabarito, [TS], VOLÁTIL, aspecto (contagem), quesito, conceito ou valor muda. Revisão: gce-cqfp; reconciliação: gce-gerencia (gatilho A para o curso; gatilho D para o aspecto (xv), padrão canônico de discursiva).

## 0. Base reaberta hoje (verificado em 18/10/2026)

Página: "Improve transcription results with model adaptation" (Google Cloud, Speech-to-Text), https://docs.cloud.google.com/speech-to-text/docs/adaptation-model. HTTP 200 em 18/10/2026; rodapé "Last updated 2026-10-13 UTC".

Trecho literal (seção "Overview"):
> "You can use the model adaptation feature to help Speech-to-Text recognize specific words or phrases more frequently than other options that might otherwise be suggested."
> "Model adaptation is particularly helpful in the following use cases:" [...] "Improving the accuracy of speech transcription when the supplied audio contains noise or is not very clear."

Leitura: a fonte afirma (i) que a adaptação enviesa a escolha entre palavras/frases alternativas, e (ii) que ela melhora a acurácia em áudio com ruído ou pouco claro. A fonte NÃO diz que a adaptação remove o ruído nem que trata sotaque; sobre a causa acústica ela é silenciosa. A frase atual do curso ("não corrige ... ruído") nega, por implicação, o que a fonte lista como uso (ii).

## 1. Ponto 1 — curso 2.8, "Riscos" (saida/gce/GCE_Lote2_v2_CPP.md, l. 504–507)

Texto atual (literal, 4 linhas; só a l. 507 muda):
```
 - Riscos: reforço excessivo faz o sistema inserir o termo reforçado
   onde ele não foi dito (falso positivo) e pode piorar outras palavras;
   listas ficam desatualizadas (nomes mudam a cada legislatura);
   adaptação não corrige sotaque nem ruído.
```
Texto proposto (as linhas 504–506 ficam intactas; a l. 507 passa a 3 linhas):
```
 - Riscos: reforço excessivo faz o sistema inserir o termo reforçado
   onde ele não foi dito (falso positivo) e pode piorar outras palavras;
   listas ficam desatualizadas (nomes mudam a cada legislatura);
   adaptação não remove o ruído nem trata a causa acústica (sotaque pede
   dados acústicos), embora possa melhorar o reconhecimento dos termos
   esperados quando o áudio é ruidoso ou pouco claro.
```
Base: (a) "Improving the accuracy of speech transcription when the supplied audio contains noise or is not very clear." (Google, URL acima, verificado em 18/10/2026) sustenta a oração concessiva; (b) "recognize specific words or phrases more frequently than other options" (mesma página e data) sustenta que a adaptação atua sobre a escolha de termos (viés), e não sobre o sinal acústico; (c) "sotaque pede dados acústicos" é a posição do próprio Lote 1 (GCE_Lote1_v2_CPP.md, l. 345–347 e 528; AUTORAL, não reaberta aqui por não depender de produto). A negativa "não remove o ruído nem trata a causa acústica" é conclusão autoral decorrente de (b); a fonte não a enuncia nem a contradiz. Rótulo: AUTORAL com apoio em OUTRA_OFICIAL (Google).

Efeito: nenhum item muda (ver seção 3). A tabela de proveniência do Lote 2 ganha a linha da página do Google com a data de hoje, se ainda não tiver linha para este uso.

## 2. Ponto 2 — aspecto (xv) do quesito 2.4 (saida/gce/GCE_Lote2_padroes_GCE.md, l. 136–138)

Texto atual (literal, 3 linhas):
```
 (xv) risco, em lista fechada: sobre-reforço com inserção de termo não
      dito; listas desatualizadas (a cada legislatura); a adaptação não
      corrige sotaque nem ruído;
```
Texto proposto (l. 136–137 intactas; a l. 138 muda):
```
 (xv) risco, em lista fechada: sobre-reforço com inserção de termo não
      dito; listas desatualizadas (a cada legislatura); a adaptação não
      trata a causa acústica (ruído, sotaque), que pede dados acústicos;
```
Alteração mínima: "não corrige sotaque nem ruído" -> "não trata a causa acústica (ruído, sotaque), que pede dados acústicos". Mantém a lista fechada de três riscos e a função do aspecto; deixa de contradizer a fonte porque não nega a melhora do reconhecimento dos termos em áudio ruidoso (a nuance concessiva fica no curso, não na régua).

Base: a mesma do ponto 1 (Google, URL acima, "Last updated 2026-10-13 UTC", verificado em 18/10/2026). Cuidado de correção: a candidata que escrever "a adaptação não corrige sotaque nem ruído" (formulação do curso até hoje) ainda cumpre o terceiro risco da lista, por equivalência de núcleo; sugere-se à gce-cqfp confirmar que isso não exige linha nova no padrão (a lista é fechada em riscos, não em palavras).

Efeito no padrão: o aspecto (xv) permanece um aspecto; o quesito 2.4 mantém "aspectos (xii) a (xvi)", conceitos 0–4, valor 7,00 e a regra "sem (xv), não se chega ao conceito máximo". Nenhuma pontuação muda. Está no pacote v1.9 em discursivas[2] (D3, peça; trecho "a adaptação não corrige sotaque nem ruído;") e no arquivo de origem; D2 (questão) não contém esta frase.

## 3. Varredura das demais ocorrências e dependências

A) Ocorrências do tema (fica ou muda):
| Local | Texto | Decisão |
|---|---|---|
| GCE_Lote1_v2_CPP.md l. 345–347 | "Sotaque se trata com dados acústicos (...), não com lista de palavras." | FICA. Só trata sotaque; a fonte é silente sobre sotaque. Não afirma nada sobre ruído. |
| GCE_Lote1_v2_CPP.md l. 566 (par 9) | "Adaptação de vocabulário vs modelo acústico customizado: termos / sotaque e ruído." | FICA, com ressalva: associa ruído ao modelo acústico, mas não afirma que a adaptação não ajude em áudio ruidoso. Se a gce-cqfp preferir, redação opcional: "termos / causa acústica (sotaque, ruído)". Não é necessária para a coerência com a fonte. |
| GCE_Lote1_v2_CPP.md l. 635–641 (L1-Q12) e l. 725–726 (gabarito) | Item E: lista "em qualquer condição acústica, independentemente do sotaque" | FICA. O gabarito E continua certo pela fonte, que lista a melhora em áudio ruidoso como UM uso, não como garantia "em qualquer condição". Na justificativa, "não garante acerto em qualquer condição acústica nem corrige sotaque" não afirma que a adaptação não ajude com ruído. |
| GCE_Lote1_v2_CPP.md l. 641 e 727–728 (L1-Q13) | Adaptação não é retreino acústico; sotaque pede dados acústicos | FICA. Só sotaque e retreino. |
| GCE_Lote1_consolidacao_GCE.md l. 56–61 e l. 119; pacote.json discursivas[0] (D1: "(iii) desafio acústico (sotaques, reverberação, ruído, sobreposição)"; "exigem customização acústica"; anulação "afirmar que lista de termos corrige sotaque") | Lote 1, padrão da discursiva | FICA. Afirma que as condições acústicas "exigem customização acústica", sem dizer que a adaptação de termos é inútil nelas; a anulação trata só de sotaque. Residual para a gce-cqfp avaliar: "exigem" é forte para ruído; se achar necessário, nota na Gerência, não nesta errata (fora do escopo de T-106). |
| saida/simulados/simulado_0_P2_gabarito.md l. 42 (L1-Q12) e simulado_2_gabarito.md l. 63 (L1-Q13) | Justificativas: "não garante ... nem corrige sotaque"; "sotaque pede dados acústicos" | FICAM. Mesmo motivo do Lote 1; nenhuma afirma que a adaptação não melhora áudio ruidoso. |
| pacote.json (item L1-Q12, justificativa) | idem | FICA. |
| pacote.json lotes[L2].curso (a mesma frase do ponto 1) | frase da l. 507 | MUDA com o ponto 1, na v1.10 (T-104), por absorção. |
| pacote.json discursivas[2] (D3) | a mesma frase do ponto 2 | MUDA com o ponto 2, na v1.10, se o aceite (gatilho D) vier antes da geração. |
| GCE_Lote2_v1_CPP.md l. 408 | mesma frase | NÃO MUDA: histórico (a QA já registrou que a v1 é histórico). |
| L2_reforco_onda3_D_v3.md l. 43, 125 e 130 (itens 3 e 8) | Registram a tensão e remetem à errata | FICAM; ao aplicar a errata, a Gerência pode atualizar o registro 3/8 para "tratada em T-106". |

B) Itens que dependem da frase (folha 2.8 e demais):
- Pacote v1.9: a 2.8 tem 6 itens (L2-Q28, Q29, Q30, R16, R17, R18). Nenhum enuncia ou julga ruído, sotaque ou "pouco claro" (conferido por busca no enunciado e na justificativa). L2-Q28 julga LM adaptado × probabilidade de sequências; Q29, OOV × baixa confiança; Q30, reforço máximo; R16, Tesauro; R17, dados de treinamento do LM; R18, 2.000 frases do Azure. Nenhum depende da frase.
- Ondas (onda 1 v3 e onda 3 A–D v3): L2-R117 a R130 (2.8, onda 3 D v3) conferidos um a um. R117 (frase de várias palavras), R118/R119/R120 (classes, classe personalizada, token inválido), R121 (lista de frases em lote), R122 (lista de frases × custom speech), R123/R124 (treinamento × ajuste), R125 (região AWS), R126 (modelo fixo), R127–R130 (RICD). Nenhum trata de ruído, sotaque ou áudio pouco claro. As ocorrências de "fala pouco clara" na onda 3 A (L2-R23, R35) são da 2.1/2.2, sobre a nota de transparência do Azure (erro temporário), sem relação com adaptação.
- Itens do banco geral (334 itens do pacote v1.9) que misturem "adaptação" e ruído/sotaque/acústica: apenas L1-Q12 e L1-Q13 (1.6), tratados acima; gabaritos E mantidos.
- Conclusão: nenhum item do pacote depende da frase; nenhum gabarito, [TS] ou VOLÁTIL muda. O único objeto afetado é texto de curso e de padrão de resposta.

## 4. Pergunta para a QA e encaminhamento

1. Confirmar que "(ruído, sotaque), que pede dados acústicos" no (xv) não precisa de apoio adicional além do Lote 1 (posição autoral, não depende de produto).
2. Decidir sobre o par 9 do Lote 1 e a expressão "exigem customização acústica" (opcional; fora do núcleo desta errata).
3. Se aceita: entrada na Tabela de Correções do GCE_Lote2_v2_CPP.md (curso) e errata equivalente no GCE_Lote2_padroes_GCE.md (aspecto (xv), com nota "sem mudança de aspectos, quesitos, conceitos, valores ou gabarito", no formato da errata de 14/10/2026 ali registrada); absorção na v1.10 (T-104).
