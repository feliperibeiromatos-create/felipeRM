# T110_pares_P2_v2.md — T-110 (v2, após QA R1) pares → pegadinhas (P2, 67 pares) — 2026-10-18 — gerado por gce-cpp

Base: pacote v1.11 (`lotes[].pares` e `lotes[].pegadinhas` de L1, L1C, L2, L3; cursos segmentados por `## `). Regras: seção 1.1 da D1 da GCE de 18/10/2026. Cada par é identificado por `<lote>#<posição>`.

## Resposta ao QA R1 (QA_T110_R1_2026-10-18_gce-cqfp.md), item a item

| Item do QA | Resposta |
|---|---|
| L1#12 (P2-1.7) CORRIGIR | acatado: texto exato do QA aplicado ("preciso ... corre menos risco de cortá-lo"; sem "completo") |
| L1#15 (P2-1.8) CORRIGIR | acatado: texto exato do QA aplicado (tradução PARA o inglês, pelo /audio/translations; parêntese removido) |
| L2#22 (P2-2.8) CORRIGIR | acatado: texto exato do QA aplicado ("reforço excessivo", lados A e B descritos) |
| L3#27 (P2-4.3) CORRIGIR | acatado: texto exato do QA aplicado (transmissão em geral; gestão de chaves como acompanhamento) |
| L1#9 descarte REPROVADO | acatado: convertido em P2-1.6, rótulo do 1.6, inserirDepois 13, logo após L1#8, com o texto do QA |
| L3#9 descarte REPROVADO | acatado: convertido em P2-3.3, rótulo do 3.3, inserirDepois 15, logo após L3#8, com o texto do QA |
| Seção 3.1, ordem do JSON (P2-1.4) | acatado: entrada de 1.4 movida antes das de 1.6; ordem L1: 1.1, 1.2, 1.3, 1.4, 1.6 (L1#8, L1#9), 1.7, 1.8, 1.8 |
| Seção 3.2 a 3.4, contagem e tabela (a) | acatado: 24 convertidos, 43 descartados (D1 41, D2 1, D3 1); L1#9 e L3#9 CONVERTIDO na tabela |
| Demais 61 pares | aprovados pelo QA; mantidos sem alteração |


## (a) Tabela de rastro

| Par | A | B | itemEdital | Resultado | Motivo | Bloco e frase que sustentam / observação |
|---|---|---|---|---|---|---|
| L1#1 | ASR | diarização vs identificação de locutor | P2-1.1 | CONVERTIDO | 1 par → 1 pegadinha | 1.1: "Faz apenas isso: fala → texto. Não decide quem falou (isso é diarização/identificação de locutor)"; par: texto, quem-quando, quem-é. |
| L1#2 | Diarização | verificação de locutor | P2-1.4 | DESCARTADO | D1 (L1.pegadinhas#8 e L1C.pegadinhas#3) | já opõem diarização a verificação e a identidade |
| L1#3 | End-to-end | modular | P2-1.2 | CONVERTIDO | 1 par → 1 pegadinha | 1.2: "uma única rede neural ... substituindo a construção separada de modelo acústico + léxico + modelo de linguagem"; par: ambos supervisionados. |
| L1#4 | End-to-end | não supervisionado | P2-1.2 | DESCARTADO | D1 (L1.pegadinhas#2) | mesma troca end-to-end por não supervisionado |
| L1#5 | LLM de áudio nativo | cascata ASR→LLM→TTS | P2-1.3 | CONVERTIDO | 1 par → 1 pegadinha | 1.3: "O contraste é com a arquitetura EM CASCATA ... em que o LLM só vê texto e perde o que não está nas palavras". |
| L1#6 | Transcrição por LLM | ASR dedicado | P2-1.3 | DESCARTADO | D1 (L1.pegadinhas#5) | mesma confusão transcrição por LLM com ASR dedicado |
| L1#7 | Pontuação automática | pontuação falada | P2-1.5 | DESCARTADO | D1 (L1.pegadinhas#9) | mesma oposição, com o critério falada x inferida |
| L1#8 | Custom vocabulary (adaptação) | custom language model | P2-1.6 | CONVERTIDO | 1 par → 1 pegadinha | 1.6: "custom vocabulary (acrescenta termos ao vocabulário base)"; "custom language model (CLM), treinado com dados de TEXTO do domínio"; "adaptação de vocabulário é VIÉS de reconhecimento". |
| L1#9 | Adaptação de vocabulário | modelo acústico customizado | P2-1.6 | CONVERTIDO | 1 par → 1 pegadinha (R1: descarte reprovado) | 1.6: "Sotaque se trata com dados acústicos (modelo customizado ou mais dados), não com lista de palavras"; "adaptação de vocabulário é VIÉS de reconhecimento". |
| L1#10 | Streaming (tempo real) | batch (arquivo) | P2-1.7 | DESCARTADO | D1 (L1.pegadinhas#14) | já opõe streaming e batch (precisão, recursos) |
| L1#11 | stream=true em arquivo | Realtime | P2-1.7 | DESCARTADO | D1 (L1.pegadinhas#14) | já traz "stream=true em arquivo = tempo real" (não) |
| L1#12 | Endpointing sensível | preciso | P2-1.7 | CONVERTIDO | 1 par → 1 pegadinha | 1.7: "endpointing: decisão de que o orador terminou uma frase, geralmente por silêncio; sensibilidade maior = resposta mais rápida, mas risco de cortar o orador"; par: lento e completo. |
| L1#13 | WER | DER | P2-1.4 | CONVERTIDO | 1 par → 1 pegadinha | 1.4: "DER ..., que soma erro de falante, fala perdida e falso alarme — distinta do WER, que mede erros de palavras". |
| L1#14 | Whisper (modelo aberto) | API OpenAI (serviço) | P2-1.8 | DESCARTADO | D1 (L1.pegadinhas#16) | mesma oposição modelo aberto x API (e #19 para a custódia) |
| L1#15 | Tradução (whisper-1, só para inglês) | transcrição (idioma original) | P2-1.8 | CONVERTIDO | 1 par → 1 pegadinha | 1.8: "tradução para o inglês (endpoint /audio/translations, só para inglês)"; par: transcrição no idioma original. |
| L1#16 | Timestamps por palavra | por enunciado | P2-1.8 | CONVERTIDO | 1 par → 1 pegadinha | 1.8: "whisper-1 é indicado quando se precisa de timestamps por palavra/segmento"; critério de granularidade: do par ("enunciado" do par = "segmento" do bloco). |
| L1#17 | LLM de áudio nativo | ASR aprimorado por LLM | P2-1.3 | DESCARTADO | D1 (L1.pegadinhas#6) | mesma confusão ASR aprimorado por LLM com LLM de áudio nativo |
| L2#1 | Transcrição automática | degravação | P2-2.1 | DESCARTADO | D1 (L2.pegadinhas#1) | mesma troca das definições |
| L2#2 | Degravação | taquigrafia | P2-2.1 | DESCARTADO | D1 (L2.pegadinhas#3) | mesma oposição, com o critério posterior x simultânea |
| L2#3 | Transcrição automática | revisão humana | P2-2.1 | CONVERTIDO | 1 par → 1 pegadinha | 2.1: "A saída é um RASCUNHO: não garante fidelidade em nomes, siglas, números, pontuação nem atribuição de falas"; "Revisão humana ... responde pela versão publicada". |
| L2#4 | Human IN the loop | human ON the loop | P2-2.2 | DESCARTADO | D1 (L2.pegadinhas#8) | já opõe HITL a ON the loop pelo critério de validar cada saída |
| L2#5 | Confiança do ASR | correção | P2-2.2 | CONVERTIDO | 1 par → 1 pegadinha | 2.2: "Serve para PRIORIZAR a atenção do revisor, não para dispensar a leitura: o sistema pode errar com alta confiança". |
| L2#6 | Fidelidade | literalidade | P2-2.3 | DESCARTADO | D1 (L2.pegadinhas#11) | mesma oposição fidelidade x literalidade |
| L2#7 | Erro de sentido | erro de forma | P2-2.3 | CONVERTIDO | 1 par → 1 pegadinha | 2.3: "erro que ALTERA O SENTIDO (omitir 'não', trocar número, nome ou orador) é mais grave que erro de forma que não impede a compreensão (acento, grafia)". |
| L2#8 | Inaudível marcado | inaudível completado | P2-2.3 | DESCARTADO | D1 (L2.pegadinhas#13) | mesma oposição inaudível marcado x completado |
| L2#9 | Aparte | fala do Presidente vs discurso principal | P2-2.4 | DESCARTADO | D1 (L2.pegadinhas#18) | mesma mistura aparte, fala do Presidente e discurso |
| L2#10 | Marcação de evento | fala | P2-2.4 | DESCARTADO | D1 (L2.pegadinhas#16) | mesma confusão marcação (evento) com fala |
| L2#11 | Rótulo de diarização | identificação do orador | P2-2.4 | DESCARTADO | D1 (L2.pegadinhas#20) | mesma confusão rótulo de diarização com identificação |
| L2#12 | Normalização (texto→fala) | normalização inversa, ITN (fala→texto escrito) | P2-2.5 | CONVERTIDO | 1 par → 1 pegadinha | 2.5: "Normalização (texto → fala) ...; Normalização INVERSA (fala → texto escrito), ou ITN ... etapa de formatação posterior ao reconhecimento". |
| L2#13 | Normalização de texto | correção de conteúdo | P2-2.5 | DESCARTADO | D1 (L2.pegadinhas#22) | mesma oposição normalização x correção de conteúdo |
| L2#14 | Normalização de texto | normalização de áudio (volume) | P2-2.5 | DESCARTADO | D1 (L2.pegadinhas#24) | mesma oposição com a normalização de áudio (volume) |
| L2#15 | CAT, transcrição assistida (traduz as notas estenotípicas em texto) | memória de tradução (reaproveita segmentos já traduzidos entre idiomas); e "tradução das notas" (decifrar sinais e passar para texto) vs tradução de idioma | P2-2.6 | DESCARTADO | D1 (L2.pegadinhas#28 e L2.pegadinhas#33) | as duas oposições do par composto já existem: CAT x memória de tradução (#28) e "tradução das notas" x tradução de idioma (#33); não há desdobramento |
| L2#16 | Editor de transcrição | ASR | P2-2.6 | DESCARTADO | D1 (L2.pegadinhas#29) | mesma confusão editor x ASR |
| L2#17 | Revisão em dupla (2º revisor independente) | releitura pelo mesmo revisor | P2-2.7 | DESCARTADO | D1 (L2.pegadinhas#34) | mesma confusão revisão em dupla x mesmo revisor |
| L2#18 | Auditoria de amostras (estima) | revisão integral (examina tudo) | P2-2.7 | DESCARTADO | D1 (L2.pegadinhas#37) | mesma confusão auditoria x revisão integral |
| L2#19 | SLA (prazo e qualidade) | apenas prazo | P2-2.7 | DESCARTADO | D1 (L2.pegadinhas#36) | mesma confusão SLA x apenas prazo |
| L2#20 | OOV (ausente do vocabulário) | baixa confiança | P2-2.8 | DESCARTADO | D1 (L2.pegadinhas#39) | mesma confusão OOV x baixa confiança |
| L2#21 | Adaptação de modelo de linguagem (sequências, contexto) | reforço de termos (palavras isoladas, com peso) | P2-2.8 | CONVERTIDO | 1 par → 1 pegadinha | 2.8: "Adaptar o LM com textos do domínio eleva a probabilidade de sequências típicas"; "reforço contextual de termos (biasing, lista de termos com peso)". |
| L2#22 | Reforço moderado | sobre-reforço (falsos positivos) | P2-2.8 | CONVERTIDO | 1 par → 1 pegadinha | 2.8: "reforço excessivo faz o sistema inserir o termo reforçado onde ele não foi dito (falso positivo) e pode piorar outras palavras". |
| L3#1 | Transcrição | sumarização | P2-3.1 | DESCARTADO | D1 (L3.pegadinhas#1) | mesma oposição transcrição x sumarização |
| L3#2 | Sumarização extrativa | abstrativa | P2-3.1 | CONVERTIDO | 1 par → 1 pegadinha | 3.1: "EXTRATIVA (seleciona e copia trechos do original) ou ABSTRATIVA (redige frases novas a partir do original; é o caso dos LLMs)". |
| L3#3 | Indexação | busca | P2-3.1 | DESCARTADO | D1 (L3.pegadinhas#4) | mesma troca indexação x busca |
| L3#4 | Busca lexical | busca semântica | P2-3.2 | DESCARTADO | D1 (L3.pegadinhas#7) | já opõe semântica a lexical (nome e número exato) |
| L3#5 | Busca semântica | busca híbrida | P2-3.2 | CONVERTIDO | 1 par → 1 pegadinha | 3.2: "Busca híbrida: combina as duas, porque termos exatos (número de proposição, nome próprio, sigla) e semelhança de sentido atendem a necessidades diferentes". |
| L3#6 | Busca semântica | RAG | P2-3.2 | CONVERTIDO | 1 par → 1 pegadinha | 3.2: "a busca devolve os trechos mais próximos da consulta"; "RAG ...: recupera trechos e pede a um LLM que responda com base neles, citando a origem". |
| L3#7 | Precisão | revocação | P2-3.2 | DESCARTADO | D1 (L3.pegadinhas#10) | mesma confusão precisão x revocação |
| L3#8 | Ata | resumo | P2-3.3 | CONVERTIDO | 1 par → 1 pegadinha | 3.3: "Ata: documento formal que registra o ocorrido numa reunião ... Resumo: condensação do conteúdo, de caráter informativo". |
| L3#9 | Alucinação | reformulação | P2-3.3 | CONVERTIDO | 1 par → 1 pegadinha (R1: descarte reprovado) | 3.3: "Alucinação: conteúdo NÃO SUSTENTADO pela fonte". |
| L3#10 | Fluência | fidelidade do texto gerado | P2-3.3 | DESCARTADO | D1 (L3.pegadinhas#12) | mesma oposição fluência x fidelidade |
| L3#11 | Modelo multilíngue | especializado em português | P2-3.4 | CONVERTIDO | 1 par → 1 pegadinha | 3.4: "Modelo multilíngue: um único modelo treinado com dados de vários idiomas ... o desempenho varia por idioma"; "Modelo especializado em português: treinado ou ajustado com corpora em português". |
| L3#12 | Especializado (treinado/ajustado em pt) | exclusivo (só pt) | P2-3.4 | DESCARTADO | D1 (L3.pegadinhas#17) | mesma confusão especializado x exclusivo |
| L3#13 | Ajuste fino | RAG | P2-3.4 | CONVERTIDO | 1 par → 1 pegadinha | 3.4: "Modelo de domínio ... por ajuste fino com textos do domínio, por recuperação de documentos oficiais (RAG, 3.2) ou por instruções; não exige treinar do zero"; par: altera o modelo, fornece documentos na consulta. |
| L3#14 | Controlador (decide) | operador (executa em nome) | P2-4.1 | DESCARTADO | D1 (L3.pegadinhas#24) | mesma troca controlador x operador |
| L3#15 | Controlador | encarregado | P2-4.1 | DESCARTADO | D1 (L3.pegadinhas#28) | mesma confusão controlador x encarregado |
| L3#16 | Dado pessoal | dado pessoal sensível (enumeração do art. 5º, II) | P2-4.1 | CONVERTIDO | 1 par → 1 pegadinha | 4.1: "Dado pessoal: informação relacionada a pessoa natural identificada ou identificável (art. 5º, I)"; "o art. 5º, II, enumera origem racial ou étnica ... opinião política ... saúde ... dado genético". |
| L3#17 | Anonimização (art. 12: dado deixa de ser pessoal, salvo reversão por meios próprios ou com esforço razoável) | pseudonimização (art. 13, § 4º, definida "para os efeitos deste artigo", com informação adicional guardada separadamente) | P2-4.1 | DESCARTADO | D1 (L3.pegadinhas#27) | mesma confusão pseudonimização x anonimização (e #38 em 4.3) |
| L3#18 | Consentimento | outras hipóteses do art. 7º | P2-4.1 | DESCARTADO | D1 (L3.pegadinhas#21) | mesma confusão consentimento x demais hipóteses |
| L3#19 | Dado de acesso público | dado livre para qualquer uso | P2-4.1 | DESCARTADO | D1 (L3.pegadinhas#22) | mesma confusão dado de acesso público x livre |
| L3#20 | Revisão de decisão automatizada (art. 20) | revisão por pessoa natural (redação original, suprimida pela MP nº 869/2018, convertida na Lei 13.853/2019) | P2-4.1 | DESCARTADO | D1 (L3.pegadinhas#25) | mesma redação superada da revisão por pessoa natural |
| L3#21 | Autoridade nacional (art. 5º, XIX) | ANPD criada pela Lei 15.352/2026 (autarquia vinculada ao MJSP); órgão da Presidência (redação superada) | P2-4.1 | DESCARTADO | D1 (L3.pegadinhas#26) | mesma redação superada da autoridade nacional |
| L3#22 | Obra protegida | ato oficial não protegido (art. 8º, IV) | P2-4.2 | DESCARTADO | D1 (L3.pegadinhas#30) | mesma confusão obra protegida x ato oficial (art. 8º, IV) |
| L3#23 | Domínio público | disponível na internet | P2-4.2 | DESCARTADO | D1 (L3.pegadinhas#31) | mesma confusão domínio público x disponível na internet |
| L3#24 | Direitos morais | patrimoniais | P2-4.2 | DESCARTADO | D1 (L3.pegadinhas#32) | já opõe direitos morais a patrimoniais (cessão) |
| L3#25 | Citação (art. 46, III) | reprodução integral | P2-4.2 | DESCARTADO | D1 (L3.pegadinhas#35) | mesma confusão citação x reprodução integral |
| L3#26 | Confidencialidade, integridade, disponibilidade |  | P2-4.3 | DESCARTADO | D2 (bloco 4.3) | tríade sem B; o bloco apresenta confidencialidade, integridade e disponibilidade sem opor dois deles |
| L3#27 | Criptografia em trânsito | em repouso | P2-4.3 | CONVERTIDO | 1 par → 1 pegadinha | 4.3: "2. Transmissão: criptografia em trânsito. 3. Armazenamento (áudio bruto, transcrições, embeddings, registros de acesso, backups): criptografia em repouso, gestão de chaves". |
| L3#28 | Incidente de segurança (comunica o controlador) | vazamento interno sem risco relevante | P2-4.3 | DESCARTADO | D3 (bloco 4.3 (art. 48)) | o bloco só diz que o incidente que possa acarretar risco ou dano relevante é comunicado pelo controlador; que o vazamento interno sem risco relevante dispense a comunicação é fato que o bloco não traz (a parte "controlador comunica" já está em L3.pegadinhas#39) |

## (b) Contagem (final, após QA R1)

- Pares: 67 (L1 17, L2 22, L3 28; L1C 0).
- Convertidos: 24 (cada um em 1 pegadinha; nenhum desdobramento) → 24 pegadinhas novas.
- Descartados: 43 — D1 41, D2 1, D3 1, D4 0.
- Conferência: 24 + 43 = 67.
- Por lote: L1 9 convertidos e 8 D1; L2 6 convertidos e 16 D1; L3 9 convertidos, 17 D1, 1 D2 (L3#26) e 1 D3 (L3#28).
- Pegadinhas novas por itemEdital: P2-1.1 1, P2-1.2 1, P2-1.3 1, P2-1.4 1, P2-1.6 2, P2-1.7 1, P2-1.8 2, P2-2.1 1, P2-2.2 1, P2-2.3 1, P2-2.5 1, P2-2.8 2, P2-3.1 1, P2-3.2 2, P2-3.3 2, P2-3.4 2, P2-4.1 1, P2-4.3 1.

## Observações para a Gerência e o QA

- L3#2 (extrativa x abstrativa): o bloco que ensina a distinção primeiro é o 3.1, que não tem pegadinha sobre ela; por isso foi convertida em 3.1, ainda que L3.pegadinhas#11 (itemEdital 3.3) já traga a mesma troca. Se a Gerência preferir comparar entre tópicos, o par vira D1.
- L2#15: a D1 da GCE previa o desdobramento em 2 pegadinhas, mas as duas oposições já existem (L2.pegadinhas#28 e #33); descartado por D1.
- L1#16: o par diz "por enunciado"; o bloco 1.8 usa "por palavra/segmento". O texto usa "segmento"; o critério de granularidade vem do par.
- L1#1: o texto ficou nos limites do bloco 1.1 e do par (o critério "banco de vozes cadastradas" é do 1.4 e não foi usado).
- Descartes de fronteira: L1#2, L1#11, L2#4 e L3#24 confirmados pelo QA R1; L1#9 e L3#9 foram revertidos (convertidos).

## (c) JSON

## (c) JSON

```json
{
 "pegadinhas_novas": [
  {
   "lote": "L1",
   "inserirDepois": 1,
   "itemEdital": "P2-1.1",
   "rotulo": "Reconhecimento automático de fala (ASR – Automatic Speech Recognition)",
   "texto": "Não confunda ASR com diarização nem com identificação de locutor: o ASR só converte fala em texto; a diarização responde a quem falou e quando; a identificação de locutor diz quem é a pessoa. Decidir quem falou não é função do ASR."
  },
  {
   "lote": "L1",
   "inserirDepois": 2,
   "itemEdital": "P2-1.2",
   "rotulo": "Modelos de fala end-to-end",
   "texto": "Não confunda modelo end-to-end com modelo modular: no end-to-end, uma única rede neural é treinada para mapear diretamente o áudio ao texto; no modular, modelo acústico, léxico e modelo de linguagem são componentes separados. Os dois são supervisionados."
  },
  {
   "lote": "L1",
   "inserirDepois": 7,
   "itemEdital": "P2-1.3",
   "rotulo": "LLMs multimodais de áudio nativo",
   "texto": "Não confunda LLM de áudio nativo com cascata ASR → LLM → TTS: no modelo nativo, o áudio entra no próprio LLM, sem módulo ASR separado; na cascata, o LLM só vê texto e perde o que não está nas palavras, como entonação, hesitação, sobreposição e risos."
  },
  {
   "lote": "L1",
   "inserirDepois": 8,
   "itemEdital": "P2-1.4",
   "rotulo": "Diarização de falantes: identificação e separação de múltiplos oradores",
   "texto": "Não confunda WER (Word Error Rate) com DER (Diarization Error Rate): o WER mede erros de palavras; o DER soma erro de falante, fala perdida e falso alarme."
  },
  {
   "lote": "L1",
   "inserirDepois": 13,
   "itemEdital": "P2-1.6",
   "rotulo": "Desafios do ASR em Português Brasileiro: sotaques, vocabulário técnico e parlamentar",
   "texto": "Não confunda custom vocabulary com custom language model (CLM): o custom vocabulary acrescenta termos ao vocabulário base e age como viés de reconhecimento; o CLM, no Amazon Transcribe, é treinado com dados de texto do domínio, e não com áudio."
  },
  {
   "lote": "L1",
   "inserirDepois": 13,
   "itemEdital": "P2-1.6",
   "rotulo": "Desafios do ASR em Português Brasileiro: sotaques, vocabulário técnico e parlamentar",
   "texto": "Não confunda adaptação de vocabulário com modelo acústico customizado: a adaptação de vocabulário é viés de reconhecimento, que empurra o decodificador para termos esperados, e não altera o modelo acústico; sotaque e ruído se tratam com dados acústicos, em modelo customizado ou com mais dados."
  },
  {
   "lote": "L1",
   "inserirDepois": 14,
   "itemEdital": "P2-1.7",
   "rotulo": "Transcrição em tempo real",
   "texto": "Não confunda endpointing sensível com endpointing preciso: o endpointing decide que o orador terminou a frase, em geral por silêncio. O sensível responde mais rápido, mas corre o risco de cortar o orador; o preciso é mais lento, porém corre menos risco de cortá-lo."
  },
  {
   "lote": "L1",
   "inserirDepois": 19,
   "itemEdital": "P2-1.8",
   "rotulo": "Ferramentas e APIs: Whisper (Open AI), Google Speech-to-text, Azure Speech, AWS Transcribe",
   "texto": "Não confunda tradução com transcrição no whisper-1: a tradução, pelo endpoint /audio/translations, devolve o texto em inglês, e só para o inglês; a transcrição mantém o idioma original do áudio."
  },
  {
   "lote": "L1",
   "inserirDepois": 19,
   "itemEdital": "P2-1.8",
   "rotulo": "Ferramentas e APIs: Whisper (Open AI), Google Speech-to-text, Azure Speech, AWS Transcribe",
   "texto": "Não confunda timestamps por palavra com timestamps por segmento: os primeiros marcam início e fim de cada palavra, em granularidade fina; os segundos marcam cada frase ou trecho, em granularidade grossa. O whisper-1 é indicado quando se precisa de timestamps por palavra ou por segmento."
  },
  {
   "lote": "L2",
   "inserirDepois": 5,
   "itemEdital": "P2-2.1",
   "rotulo": "Diferença entre transcrição automática, degravação e revisão humana",
   "texto": "Não confunda transcrição automática com revisão humana: a transcrição automática é um rascunho, produzido por software sem intervenção humana, que não garante fidelidade em nomes, siglas, números, pontuação nem atribuição de falas; a revisão humana confronta o texto com o áudio e responde pela versão publicada."
  },
  {
   "lote": "L2",
   "inserirDepois": 10,
   "itemEdital": "P2-2.2",
   "rotulo": "Fluxo de trabalho de degravação assistida por IA (Human in the loop)",
   "texto": "Não confunda confiança do ASR com correção: a pontuação de confiança por palavra serve para priorizar a atenção do revisor, não para dispensar a leitura, porque o sistema pode errar com alta confiança."
  },
  {
   "lote": "L2",
   "inserirDepois": 15,
   "itemEdital": "P2-2.3",
   "rotulo": "Revisão e edição de transcrições: critérios de qualidade e fidelidade",
   "texto": "Não confunda erro de sentido com erro de forma: o erro de sentido altera o que foi dito, como omitir \"não\" ou trocar número, nome ou orador, e é mais grave; o erro de forma, como acento ou grafia, não impede a compreensão."
  },
  {
   "lote": "L2",
   "inserirDepois": 27,
   "itemEdital": "P2-2.5",
   "rotulo": "Normalização de texto: números, siglas, abreviações e termos técnicos",
   "texto": "Não confunda normalização (texto para fala) com normalização inversa (ITN): a primeira converte a forma escrita em forma falada, como \"25%\" em \"vinte e cinco por cento\", típica de síntese de voz; a ITN converte a forma falada reconhecida em forma escrita convencional, etapa de formatação posterior ao reconhecimento."
  },
  {
   "lote": "L2",
   "inserirDepois": 43,
   "itemEdital": "P2-2.8",
   "rotulo": "Vocabulário técnico parlamentar e vocabulário adaptado (language model adaptation)",
   "texto": "Não confunda adaptação do modelo de linguagem (LM) com reforço contextual de termos: a adaptação usa textos do domínio e eleva a probabilidade de sequências de palavras, ajudando a escolher entre palavras de som parecido pelo contexto; o reforço atua sobre uma lista de termos com peso."
  },
  {
   "lote": "L2",
   "inserirDepois": 43,
   "itemEdital": "P2-2.8",
   "rotulo": "Vocabulário técnico parlamentar e vocabulário adaptado (language model adaptation)",
   "texto": "Não confunda reforço moderado com reforço excessivo: o moderado favorece os termos esperados; o excessivo faz o sistema inserir o termo reforçado onde ele não foi dito, um falso positivo, e pode piorar outras palavras."
  },
  {
   "lote": "L3",
   "inserirDepois": 5,
   "itemEdital": "P2-3.1",
   "rotulo": "Aplicações de IA em parlamentos: transcrição de sessões, sumarização, indexação e busca",
   "texto": "Não confunda sumarização extrativa com sumarização abstrativa: a extrativa seleciona e copia trechos do original; a abstrativa redige frases novas a partir do original, caso dos LLMs."
  },
  {
   "lote": "L3",
   "inserirDepois": 10,
   "itemEdital": "P2-3.2",
   "rotulo": "Sistemas de busca semântica em acervos parlamentares",
   "texto": "Não confunda busca semântica com busca híbrida: a semântica converte consulta e trechos em vetores (embeddings) e devolve os mais próximos; a híbrida combina busca lexical e semântica, porque termos exatos, como número de proposição, nome próprio e sigla, e semelhança de sentido atendem a necessidades diferentes."
  },
  {
   "lote": "L3",
   "inserirDepois": 10,
   "itemEdital": "P2-3.2",
   "rotulo": "Sistemas de busca semântica em acervos parlamentares",
   "texto": "Não confunda busca semântica com RAG (geração com recuperação): a busca semântica devolve os trechos mais próximos da consulta; o RAG recupera trechos e pede a um LLM que responda com base neles, citando a origem."
  },
  {
   "lote": "L3",
   "inserirDepois": 15,
   "itemEdital": "P2-3.3",
   "rotulo": "Geração automática de atas e resumos de sessões",
   "texto": "Não confunda ata com resumo: a ata é o documento formal que registra o ocorrido numa reunião, com data, local, presenças, pauta, deliberações, votações e encaminhamentos; o resumo é a condensação do conteúdo, de caráter informativo."
  },
  {
   "lote": "L3",
   "inserirDepois": 15,
   "itemEdital": "P2-3.3",
   "rotulo": "Geração automática de atas e resumos de sessões",
   "texto": "Não confunda alucinação com reformulação: alucinação é conteúdo não sustentado pela fonte, isto é, informação que a transcrição não contém; a reformulação é frase nova com sentido fiel, própria da sumarização abstrativa. Frase nova, por si, não é erro."
  },
  {
   "lote": "L3",
   "inserirDepois": 20,
   "itemEdital": "P2-3.4",
   "rotulo": "Modelos de IA multilíngues e especializados em português",
   "texto": "Não confunda modelo multilíngue com modelo especializado em português: o multilíngue é um único modelo treinado com dados de vários idiomas, com desempenho que varia por idioma; o especializado é treinado ou ajustado com corpora em português, para captar vocabulário e variedades do pt-BR."
  },
  {
   "lote": "L3",
   "inserirDepois": 20,
   "itemEdital": "P2-3.4",
   "rotulo": "Modelos de IA multilíngues e especializados em português",
   "texto": "Não confunda ajuste fino com recuperação de documentos oficiais (RAG): o ajuste fino com textos do domínio altera o modelo; o RAG fornece documentos na consulta, por recuperação. Nenhum dos dois exige treinar do zero."
  },
  {
   "lote": "L3",
   "inserirDepois": 29,
   "itemEdital": "P2-4.1",
   "rotulo": "LGPD e proteção de dados em sistemas de transcrição e IA",
   "texto": "Não confunda dado pessoal com dado pessoal sensível: dado pessoal é a informação relacionada a pessoa natural identificada ou identificável (art. 5º, I); sensível é o que o art. 5º, II, enumera, como origem racial ou étnica, opinião política, dado referente à saúde e dado genético."
  },
  {
   "lote": "L3",
   "inserirDepois": 42,
   "itemEdital": "P2-4.3",
   "rotulo": "Segurança da informação em pipelines de áudio e transcrição",
   "texto": "Não confunda criptografia em trânsito com criptografia em repouso: a primeira protege os dados durante a transmissão; a segunda protege os dados armazenados, como áudio bruto, transcrições, embeddings, registros de acesso e backups, e se acompanha de gestão de chaves."
  }
 ]
}
```

FIM DO ARQUIVO
