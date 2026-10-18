# L1_reforco_onda1_v1.md — T-89 — 2026-10-18 — gerado por gce-cpp

Rótulo de todos os itens: AUTORAL (produtor gce-cpp, lote L1-R, onda 1 do reforço, D-REFORCO-1/2).
Escopo: P2 itens 1.1 a 1.8. Nenhum item existente foi alterado. QA PENDENTE até parecer da gce-cqfp.
Convenção: "verificado em 18/10/2026" = página aberta e lida nesta data. Itens não citam número de versão, preço ou limite de produto.

=====================================================================
PARTE 1/3 — MAPA
=====================================================================

## 1.1 Itens novos (um ponto de julgamento por item)

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (URL; verificado em 18/10/2026) | VOLÁTIL |
|---|---|---|---|---|---|
| L1-R01 | P2-1.1 | O WER de um sistema é medido sobre um conjunto de áudio e não se transfere automaticamente a outras condições acústicas (Plenário × sala silenciosa); não é propriedade fixa do modelo | situação hipotética | https://docs.cloud.google.com/speech-to-text/docs/transcription-model ; https://cloud.google.com/speech-to-text/docs/best-practices | n |
| L1-R02 | P2-1.1 | A saída do ASR traz, além do texto, marcas de tempo e medida de confiança, úteis para sincronizar com o vídeo e orientar a revisão | aplicação parlamentar | https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works.html ; https://docs.aws.amazon.com/transcribe/latest/dg/streaming-partial-results.html | n |
| L1-R03 | P2-1.2 | Em modelo end-to-end multitarefa, a tarefa (transcrever, traduzir, identificar idioma) é indicada por tokens especiais processados pelo próprio decodificador, não por módulos externos | troca de sujeito | https://github.com/openai/whisper (README, lido em https://raw.githubusercontent.com/openai/whisper/main/README.md) | n (estrutural; risco residual baixo) |
| L1-R04 | P2-1.2 | O Whisper transcreve arquivo longo por janelas sucessivas de 30 segundos, pois o modelo processa trechos de duração fixa | número ou prazo | https://github.com/openai/whisper (README, idem) | n (estrutural; risco residual baixo) |
| L1-R05 | P2-1.3 | O mesmo áudio, com instruções diferentes em linguagem natural, pode render transcrição, resumo ou tradução no mesmo LLM de áudio nativo | situação hipotética | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/audio-understanding | n |
| L1-R06 | P2-1.3 | O áudio vira tokens em proporção à duração; com taxa dada no enunciado, 2 h = 216.000 tokens (não 108.000) | número ou prazo | mesma URL da R05 (limite expresso em horas e em tokens, i.e. proporcionalidade) | n |
| L1-R07 | P2-1.4 | Falas em canais de áudio separados (um microfone por canal) permitem separação por canal, técnica distinta da diarização, que distingue vozes em um mesmo canal | situação hipotética | https://docs.aws.amazon.com/transcribe/latest/dg/feature-matrix.html ; https://cloud.google.com/speech-to-text/docs/best-practices | n |
| L1-R08 | P2-1.5 | A disponibilidade de pontuação/capitalização automática pode variar com idioma e modo de uso; confere-se na documentação do fornecedor para o pt-BR antes da adoção | situação hipotética | https://docs.cloud.google.com/speech-to-text/docs/automatic-punctuation ; https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works.html | n |
| L1-R09 | P2-1.5 | A forma "lexical" do resultado é a sem capitalização e sem pontuação; a forma de exibição (display) é a que as incorpora | troca de sujeito | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-speech-to-text-short | n |
| L1-R10 | P2-1.6 | O vocabulário personalizado deve conter termos de reconhecimento, não informação pessoal ou confidencial | aplicação parlamentar | https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html | n |
| L1-R11 | P2-1.6 | O desempenho de um modelo multilíngue varia amplamente entre idiomas; o WER em inglês não se transfere ao pt-BR | situação hipotética | https://github.com/openai/whisper (README, idem) | n |
| L1-R12 | P2-1.6 | A escolha entre homófonas (sessão/seção/cessão) depende do contexto linguístico (modelo de linguagem), não do modelo acústico | troca de sujeito | https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html | n |
| L1-R13 | P2-1.7 | Em streaming, o tamanho dos blocos enviados pelo cliente influencia a latência; ela não é fixada só pelo servidor | troca de sujeito | https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html | n |
| L1-R14 | P2-1.7 | PCM de 16 bits, 1 canal, 16.000 Hz: bloco de 100 ms = 3.200 bytes | número ou prazo | https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html (fórmula de tamanho de bloco) | n (aritmética) |
| L1-R15 | P2-1.7 | A rapidez do streaming sobre o lote pode vir com limitação de acurácia; não há garantia de acurácia igual ou superior | aplicação parlamentar | https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html | n |
| L1-R16 | P2-1.8 | A tarefa de tradução do Whisper converte fala em outro idioma em texto em inglês | situação hipotética | https://github.com/openai/whisper (README, idem) | n (estrutural; risco residual baixo) |
| L1-R17 | P2-1.8 | Lote recebe mídia previamente enviada; streaming recebe blocos sequenciais com resposta em tempo real | troca de sujeito | https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works.html ; https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html | n (estrutural; risco residual baixo) |
| L1-R18 | P2-1.8 | Tamanhos do Whisper: tiny ~39 milhões e large ~1.550 milhões de parâmetros | número ou prazo | https://github.com/openai/whisper (README, tabela "Available models and languages") | n (fato de lançamento; risco residual baixo) |

VOLÁTIL novos: 0. Risco alto: 0. Os itens marcados "risco residual baixo" citam produto, mas afirmam propriedade arquitetural ou fato de lançamento documentado, sem versão, limite ou preço. Se a Gerência os reclassificar como VOLÁTIL, o teto de 4 por lote (já ocupado pelos 4 existentes) é excedido e a substituição é necessária (ver dúvidas na Parte 3).

## 2 Itens já existentes por folha (ponto de julgamento, formato, VOLÁTIL) e verificação dos tetos

Classificação de formato dos existentes feita por esta coordenação (julgamento da CPP): D = definição; TS = troca de sujeito; SH = situação hipotética; NP = número ou prazo; PC = par confundível; AP = aplicação parlamentar.

### P2-1.1 (4 existentes + 2 novos = 6)
| id | ponto | formato | VOL |
|---|---|---|---|
| L1-Q01 | WER 0% não garante fidelidade em pontuação, capitalização e locutor | D | n |
| L1-Q02 | ASR não atribui falas a locutores (isso é diarização/identificação) | PC | n |
| L1C-Q21 | Funções invertidas: modelo acústico × modelo de linguagem | TS | n |
| L1C-Q22 | WER pode ultrapassar 100% (inserções) | NP | n |
| L1-R01 / R02 | ver tabela acima | SH / AP | n / n |
Formatos: D 1, PC 1, TS 1, NP 1, SH 1, AP 1 (máx. 1 de 6 = 16,7% cada; teto 30% cumprido). VOLÁTIL 0/6.

### P2-1.2 (4 + 2 = 6)
| id | ponto | formato | VOL |
|---|---|---|---|
| L1-Q03 | End-to-end não é imune a alucinação | D | n |
| L1-Q04 | "Supervisão fraca" ainda usa pares áudio–texto | PC | n |
| L1C-Q23 | Sem dicionário de pronúncias; correção de nome próprio passa por adaptação ou mais dados | SH | n |
| L1C-Q24 | Em muitos sistemas há espectrograma antes da rede (não universal) | D | n |
| L1-R03 / R04 | ver tabela acima | TS / NP | n / n |
Formatos: D 2, PC 1, SH 1, TS 1, NP 1. D = 2/6 = 33,3%: excesso PRÉ-EXISTENTE (Q03 e Q24); os novos não acrescentam D. VOLÁTIL 0/6.

### P2-1.3 (4 + 2 = 6)
| id | ponto | formato | VOL |
|---|---|---|---|
| L1-Q05 | Áudio nativo entra no próprio LLM, sem ASR separado | D | n |
| L1-Q06 | Na cascata o LLM recebe só texto; prosódia se perde | TS | n |
| L1C-Q25 | LLM nativo não copia literalmente a fala; revisão humana permanece | AP | n |
| L1C-Q26 | ASR reforçado por LLM não é LLM de áudio nativo | PC | n |
| L1-R05 / R06 | ver tabela acima | SH / NP | n / n |
Formatos: D, TS, AP, PC, SH, NP com 1 cada (16,7%). VOLÁTIL 0/6.

### P2-1.4 (5 + 1 = 6)
| id | ponto | formato | VOL |
|---|---|---|---|
| L1-Q07 | Diarização entrega rótulos genéricos; nomes exigem identificação | AP | n |
| L1-Q08 | Verificação de locutor é 1:1; diarizar não exige verificar | PC | n |
| L1-Q09 | DER (falante, fala perdida, falso alarme) distinto de WER | D | n |
| L1C-Q27 | "Identificar" no sentido amplo = distinguir, não nomear | D | n |
| L1C-Q28 | O objeto de "identificar" decide o sentido (que há 3 × pelo nome) | PC | n |
| L1-R07 | ver tabela acima | SH | n |
Formatos: AP 1, PC 2, D 2, SH 1. PC e D = 33,3% cada: excesso PRÉ-EXISTENTE; o novo usa SH, formato ausente. VOLÁTIL 0/6.

### P2-1.5 (4 + 2 = 6)
| id | ponto | formato | VOL |
|---|---|---|---|
| L1-Q10 | End-to-end pode emitir texto pontuado; arquiteturas clássicas restauram pontuação depois | D | n |
| L1-Q11 | Pontuação falada × pontuação automática | PC | n |
| L1C-Q29 | Pontuação automática pode mudar o sentido; a revisão confere a pontuação | AP | n |
| L1C-Q30 | Capitalização estima e erra (Câmara × câmara) | PC | n |
| L1-R08 / R09 | ver tabela acima | SH / TS | n / n |
Formatos: D 1, PC 2, AP 1, SH 1, TS 1. PC = 33,3%: excesso PRÉ-EXISTENTE (Q11, Q30); os novos usam SH e TS. VOLÁTIL 0/6.

### P2-1.6 (3 + 3 = 6)
| id | ponto | formato | VOL |
|---|---|---|---|
| L1-Q12 | Lista de termos não garante acerto em qualquer condição nem corrige sotaque | D | n |
| L1-Q13 | Adaptação de vocabulário não é retreino acústico; sotaque pede dados acústicos | PC | n |
| L1-Q14 | Amazon Transcribe: custom vocabulary × custom language model | PC | S (baixo/médio) |
| L1-R10 / R11 / R12 | ver tabela acima | AP / SH / TS | n / n / n |
Formatos: D 1, PC 2, AP 1, SH 1, TS 1. PC = 33,3%: excesso PRÉ-EXISTENTE (Q13, Q14). VOLÁTIL 1/6 = 16,7% (teto de 20% cumprido; novos 0).

### P2-1.7 (3 + 3 = 6)
| id | ponto | formato | VOL |
|---|---|---|---|
| L1-Q15 | Resultados parciais revisáveis; final consolidado após o fim do enunciado | D | n |
| L1-Q16 | OpenAI: stream=true em arquivo ≠ transcrição Realtime de áudio ao vivo | PC | S (ALTO) |
| L1-Q17 | Sensibilidade de endpointing: menor latência × fragmentação | SH | n |
| L1-R13 / R14 / R15 | ver tabela acima | TS / NP / AP | n / n / n |
Formatos: D, PC, SH, TS, NP, AP com 1 cada (16,7%). VOLÁTIL 1/6 = 16,7% (cumprido; novos 0).

### P2-1.8 (3 + 3 = 6)
| id | ponto | formato | VOL |
|---|---|---|---|
| L1-Q18 | Whisper aberto (MIT) + API com modelos mais recentes | PC | S |
| L1-Q19 | Azure AI Speech admite contêineres on-premises | D | S |
| L1-Q20 | Custódia do áudio: local × nuvem não são equivalentes | AP | n |
| L1-R16 / R17 / R18 | ver tabela acima | SH / TS / NP | n / n / n |
Formatos: PC, D, AP, SH, TS, NP com 1 cada (16,7%). VOLÁTIL 2/6 = 33,3%: excesso PRÉ-EXISTENTE (2 de 3 antes da onda; os 3 novos o reduzem de 66,7% a 33,3%, sem acrescentar VOLÁTIL).

### Verificação de não repetição
Em cada folha, o ponto de cada item novo difere dos pontos listados acima (comparação feita item a item). Proximidades que a Gerência pode querer ver: R13 e R14 (1.7) usam a mesma página da AWS, mas julgam coisas distintas (quem influencia a latência × cálculo de bytes); R12 (1.6) toca o par modelo acústico × modelo de linguagem de L1C-Q21 (1.1), em folha diferente e por outro ponto (homófonas resolvidas por contexto).

### Tetos (resumo)
- Formato: nenhum formato recebe item novo quando já está em 2 de 4 (ou mais) na folha; os excessos de 33,3% em 1.2, 1.4, 1.5 e 1.6 são anteriores à onda e não mudam (regra "nenhum item existente muda").
- VOLÁTIL: 0 novos; lote com 4 existentes (Q14, Q16, Q18, Q19), 1 de risco alto (Q16), nenhum risco alto novo.
- Gabarito: 9 C e 9 E (50% de C), dentro de 7 a 11 C.

FIM DA PARTE 1/3

=====================================================================
PARTE 2/3 — (d) ITENS DO ESTUDANTE
=====================================================================

L1-R01. Julgue o item.
Um sistema de reconhecimento automático de fala obteve WER baixo em testes com gravações de reuniões de comissão, captadas em sala silenciosa. Com base nesse resultado, a equipe concluiu que o desempenho será equivalente no Plenário, em sessões com apartes, ruído de fundo e microfones variados, uma vez que o WER é propriedade do modelo e independe do conjunto de áudio avaliado.

L1-R02. Julgue o item.
Sistemas de reconhecimento automático de fala podem entregar, além do texto, marcas de tempo e uma medida de confiança associadas às palavras reconhecidas, informações que, no registro de sessões da Câmara, podem ser usadas para sincronizar o texto com o vídeo e para orientar a revisão humana para os trechos de menor confiança.

L1-R03. Julgue o item.
Em modelos de fala end-to-end multitarefa, como o Whisper, a escolha entre transcrever, traduzir a fala ou identificar o idioma é definida por módulos externos encadeados ao modelo, e não por tokens especiais processados pelo próprio decodificador.

L1-R04. Julgue o item.
Na implementação de referência do Whisper, um arquivo de áudio longo é transcrito por meio de janelas sucessivas de 30 segundos, porque o modelo processa trechos de áudio de duração fixa, e não o arquivo inteiro de uma só vez.

L1-R05. Julgue o item.
Uma equipe da Casa envia a um LLM multimodal de áudio nativo a gravação de uma audiência pública e, em requisições separadas, pede ao mesmo modelo a transcrição, um resumo e uma tradução da fala, alterando apenas a instrução em linguagem natural enviada junto com o áudio. Esse uso é compatível com o funcionamento desse tipo de modelo.

L1-R06. Julgue o item.
Considere que um LLM de áudio nativo converta cada segundo de áudio em 30 tokens de entrada. Nessa hipótese, a gravação integral de uma sessão de 2 horas ocuparia 108.000 tokens do contexto do modelo.

L1-R07. Julgue o item.
Em uma reunião de comissão na qual cada parlamentar fala em um microfone gravado em canal de áudio próprio, a atribuição das falas pode apoiar-se na separação por canais, abordagem distinta da diarização, que distingue os falantes a partir das características da voz em um mesmo canal.

L1-R08. Julgue o item.
Ao planejar o uso de pontuação e capitalização automáticas na transcrição do Plenário, a equipe deve confirmar, na documentação do fornecedor, se o recurso é suportado para o português do Brasil e para o modo de uso pretendido (em lote ou em tempo real), pois a disponibilidade de recursos pode variar conforme o idioma e o modo.

L1-R09. Julgue o item.
Em serviços de reconhecimento de fala que devolvem mais de uma representação do mesmo trecho reconhecido, a forma lexical já incorpora capitalização e pontuação, ao passo que a forma de exibição traz apenas as palavras como reconhecidas, sem esses ajustes.

L1-R10. Julgue o item.
Na montagem de um vocabulário personalizado para o ASR usado nas comissões, a equipe deve limitar a lista a termos úteis ao reconhecimento, como siglas e nomes de proposições, e evitar nela informações pessoais ou confidenciais, ainda que a finalidade da lista seja apenas melhorar o reconhecimento.

L1-R11. Julgue o item.
Um fornecedor divulga que seu modelo multilíngue de ASR alcança baixo WER em inglês. Com base apenas nessa informação, a equipe da Câmara conclui que o desempenho em português brasileiro será igualmente bom, pois, em modelos multilíngues, o desempenho independe do idioma.

L1-R12. Julgue o item.
Para escolher entre as grafias de palavras homófonas, como "sessão", "seção" e "cessão", o ASR recorre sobretudo ao modelo acústico, responsável por usar o contexto das palavras vizinhas para decidir a grafia.

L1-R13. Julgue o item.
Na transcrição em streaming, o tamanho dos blocos de áudio enviados pelo cliente não influencia a latência, que é determinada exclusivamente pelo modelo de reconhecimento no servidor.

L1-R14. Julgue o item.
Em transmissão de áudio para reconhecimento em streaming, com áudio PCM de 16 bits (2 bytes por amostra), um canal e taxa de amostragem de 16.000 Hz, cada bloco de 100 ms de áudio equivale a 3.200 bytes.

L1-R15. Julgue o item.
Na cobertura ao vivo de uma sessão plenária, a transcrição em streaming, por entregar o texto mais rápido, tem acurácia garantidamente igual ou superior à da transcrição em lote do mesmo áudio.

L1-R16. Julgue o item.
A Câmara pretende obter, diretamente do áudio em português de uma sessão, um texto em inglês para a imprensa estrangeira. De acordo com a documentação do repositório do Whisper, isso é possível por meio da tarefa de tradução do modelo, que converte fala em outro idioma em texto em inglês.

L1-R17. Julgue o item.
No Amazon Transcribe, a transcrição em lote exige que o áudio seja entregue em blocos sequenciais e que a resposta seja devolvida em tempo real, ao passo que a transcrição em streaming opera sobre arquivos de mídia previamente enviados ao serviço.

L1-R18. Julgue o item.
O Whisper é distribuído em modelos de tamanhos diferentes, que trocam velocidade por acurácia: o modelo tiny tem cerca de 39 milhões de parâmetros e o modelo large, cerca de 1.550 milhões.

FIM DA PARTE 2/3

=====================================================================
PARTE 3/3 — (d-G) GABARITO COMENTADO
=====================================================================
Legenda: [TS] = troca sutil de um único conceito. Nenhum item é VOLÁTIL; nenhum exige REVERIFICAR de janeiro (ver observação sobre risco residual ao final). Todas as páginas foram abertas em 18/10/2026.

L1-R01. E [TS]. O WER é medido sobre um conjunto de áudio e depende da semelhança entre as condições de teste e de uso; ele não é propriedade fixa do modelo.
Base: modelos rendem melhor em áudio semelhante ao de treinamento (Google Cloud STT, "Compare transcription models") e ruído/eco reduzem a acurácia (Google, "Best practices").

L1-R02. C. Os resultados costumam trazer confiança e tempo por palavra, que servem para sincronizar com o vídeo e para priorizar a conferência humana.
Base: AWS, "How Amazon Transcribe works" (confiança e marcas de tempo por palavra ou sinal) e "Streaming and partial results" (tempos para sincronizar com o diálogo de vídeo).

L1-R03. E [TS]. A tarefa é especificada por tokens especiais do formato de treinamento multitarefa, previstos pelo decodificador; um único modelo substitui várias etapas do pipeline tradicional.
Base: repositório openai/whisper, README, seção "Approach" (tarefas representadas como sequência de tokens; tokens especiais como especificadores de tarefa).

L1-R04. C. O método transcribe() processa o arquivo com janela deslizante de 30 segundos, e o áudio é ajustado (pad/trim) a 30 s para o modelo.
Base: repositório openai/whisper, README, seção "Python usage".

L1-R05. C. LLM de áudio nativo recebe o áudio como entrada e é guiado por instrução em texto; a documentação lista compreensão de fala para sumarização, transcrição e tradução no mesmo modelo.
Base: Google Cloud, "Audio understanding" (Vertex AI), tabela de modelos e exemplos de transcrição.

L1-R06. E. A conta é 2 h × 3.600 s × 30 tokens/s = 216.000 tokens; 108.000 corresponde a 1 hora. O consumo de contexto cresce em proporção à duração.
Base: Google Cloud, "Audio understanding" (limite de áudio expresso ao mesmo tempo em horas e em tokens, i.e. conversão proporcional).

L1-R07. C [TS]. Falsa pegadinha: separação por canal e diarização são recursos distintos, e a primeira não depende de inferir a voz; ela revela o canal (microfone), não o nome.
Base: AWS, "Amazon Transcribe features" (channel identification e speaker diarization como recursos distintos); Google, "Best practices" (falantes em canais separados são enviados por canal).

L1-R08. C. A documentação remete à lista de recursos por idioma, e o suporte pode diferir entre lote e streaming; a verificação para o pt-BR é prudente antes da adoção.
Base: Google, "Enable automatic punctuation" (consultar recursos por idioma); AWS, "How Amazon Transcribe works" (recursos e idiomas diferem entre lote e streaming).

L1-R09. E [TS]. Trocados os papéis: a forma lexical é a das palavras sem capitalização e pontuação, e a de exibição é a que as aplica (além de normalização e máscara de palavrões).
Base: Microsoft, "Speech to text REST API for short audio", propriedades Display/DisplayText e Lexical nos exemplos de resposta detalhada.

L1-R10. C. A orientação da documentação é não inserir informação confidencial, pessoal (PII) ou de saúde em vocabulário personalizado; a lista serve a termos de domínio, como siglas e nomes próprios.
Base: AWS, "Custom vocabularies" (aviso "Important").

L1-R11. E. O desempenho de um mesmo modelo multilíngue varia amplamente conforme o idioma, e o WER em inglês não se transfere ao pt-BR; é preciso avaliar com áudio do domínio.
Base: repositório openai/whisper, README ("performance varies widely depending on the language"; WER por idioma).

L1-R12. E [TS]. Quem usa o contexto das palavras vizinhas é o modelo de linguagem; o acústico liga som a unidades sonoras e não separa homófonas.
Base: AWS, "Custom language models" (modelo que aprende como e quando a palavra é usada, p.ex. "ice floe" × "ice flow", ao contrário do vocabulário personalizado, que fornece dicas).

L1-R13. E [TS]. A latência depende do tamanho dos blocos de áudio enviados; a própria documentação recomenda blocos de tamanho uniforme e curto para reduzir o atraso. O erro está em atribuir a latência só ao servidor.
Base: AWS, "Transcribing streaming audio" (boas práticas).

L1-R14. C. 100/1000 × 16.000 × 2 = 3.200 bytes (a fórmula de tamanho de bloco considera 2 bytes por amostra, áudio mono).
Base: AWS, "Transcribing streaming audio" (fórmula chunk_size_in_bytes).

L1-R15. E. A documentação afirma que o streaming é mais rápido, mas que essa velocidade pode trazer limitações de acurácia em alguns casos; não há garantia de acurácia igual ou superior à do lote.
Base: AWS, "Transcribing streaming audio" (vantagens do streaming e ressalva de acurácia).

L1-R16. C. A tarefa de tradução do Whisper converte fala não inglesa em texto em inglês (ex.: --task translate).
Base: repositório openai/whisper, README, seção "Command-line usage".

L1-R17. E [TS]. Papéis trocados: o lote opera sobre arquivos de mídia previamente enviados, e o streaming recebe blocos sequenciais com resposta em tempo real.
Base: AWS, "How Amazon Transcribe works" (lote × streaming) e "Transcribing streaming audio" (blocos sequenciais).

L1-R18. C. A tabela do README traz tiny com 39 milhões e large com 1.550 milhões de parâmetros, com relação de velocidade e acurácia entre tamanhos.
Base: repositório openai/whisper, README, seção "Available models and languages".

## Contagens
| quesito | valor |
|---|---|
| total | 18 |
| C | 9 (R02, R04, R05, R07, R08, R10, R14, R16, R18) |
| E | 9 (R01, R03, R06, R09, R11, R12, R13, R15, R17) |
| [TS] | 7 (R01, R03, R07, R09, R12, R13, R17): 1 com gabarito C (R07) e 6 com gabarito E |
| VOLÁTIL | 0 novos (P2-1.1 a 1.5: 0; 1.6: 0; 1.7: 0; 1.8: 0). Existentes no lote: 4 (Q14, Q16, Q18, Q19), 1 de risco alto (Q16) |
| distribuição por folha | 1.1: 2; 1.2: 2; 1.3: 2; 1.4: 1; 1.5: 2; 1.6: 3; 1.7: 3; 1.8: 3 (soma 18) |

Observação sobre risco residual: R03, R04, R11, R16 e R18 (Whisper) e R17 (Amazon Transcribe) nomeiam produto e foram classificados como não VOLÁTEIS por afirmarem propriedade arquitetural ou fato de lançamento. Se a Gerência discordar, a reclassificação ultrapassa o teto do lote (4 existentes) e o item deve ser trocado por ponto sem dependência de produto.

## Tabela de proveniência (todas abertas e lidas em 18/10/2026)
| fonte | URL oficial | data da página / verificação | usada em |
|---|---|---|---|
| Google Cloud, Speech-to-Text, Compare transcription models | https://docs.cloud.google.com/speech-to-text/docs/transcription-model | "Last updated 2026-10-13"; verificado em 18/10/2026 | R01 |
| Google Cloud, Speech-to-Text, Best practices | https://cloud.google.com/speech-to-text/docs/best-practices | "Last updated 2026-10-13"; verificado em 18/10/2026 | R01, R07 |
| Google Cloud, Speech-to-Text, Enable automatic punctuation | https://docs.cloud.google.com/speech-to-text/docs/automatic-punctuation | verificado em 18/10/2026 | R08 |
| Google Cloud, Vertex AI, Audio understanding | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/audio-understanding | "Last updated 2026-10-15"; verificado em 18/10/2026 | R05, R06 |
| AWS, Amazon Transcribe, How Amazon Transcribe works | https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works.html | verificado em 18/10/2026 | R02, R08, R17 |
| AWS, Amazon Transcribe, Streaming and partial results | https://docs.aws.amazon.com/transcribe/latest/dg/streaming-partial-results.html | verificado em 18/10/2026 | R02 |
| AWS, Amazon Transcribe, Transcribing streaming audio | https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html | verificado em 18/10/2026 | R13, R14, R15, R17 |
| AWS, Amazon Transcribe features | https://docs.aws.amazon.com/transcribe/latest/dg/feature-matrix.html | verificado em 18/10/2026 | R07 |
| AWS, Amazon Transcribe, Custom vocabularies | https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html | verificado em 18/10/2026 | R10 |
| AWS, Amazon Transcribe, Custom language models | https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html | verificado em 18/10/2026 | R12 |
| Microsoft, Azure Speech, Speech to text REST API for short audio | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-speech-to-text-short | verificado em 18/10/2026 | R09 |
| OpenAI, repositório openai/whisper (README) | https://github.com/openai/whisper | README lido via https://raw.githubusercontent.com/openai/whisper/main/README.md em 18/10/2026 (a página github.com foi bloqueada pelo proxy do ambiente) | R03, R04, R11, R16, R18 |

Fontes que não consegui abrir (nenhum item delas entrou): developers.openai.com e platform.openai.com (documentação da API da OpenAI), arxiv.org (artigo do Whisper), planalto.gov.br e camara.leg.br (nenhuma norma foi usada), ai.google.dev. Em 18/10/2026 o acesso a esses hosts falhou no proxy do ambiente.

FIM DA PARTE 3/3
FIM DO LOTE
