# QA — pacote.json v1 (EXEC-01) — pareceres consolidados


========== L1 ==========
PARECER DE QA — EXEC-01 — L1 — RODADA 1 — Opus — 12/10/2026

Escopo: fragmentos de /home/claude/exec01/frag/L1/ (itens.json, meta.json, curso.md, resumo.md, pares.json, pegadinhas.json, discursivas.json, relatorio.md), conferidos contra ESPEC_EXEC01.md e as fontes canônicas lidas pela ferramenta Projects em 12/10/2026: GCE_Lote1_v2_CPP.md, GCE_Lote1_consolidacao_GCE.md (E1–E6, Parte B, Adendo E7–E8, Adendo 2 E9 e R-J, Adendo 3 E10) e claude/GBQ_Registro_AUTORAL_v2.md. QA independente: não produzi os fragmentos e não os editei.

## CONCLUSÃO: APROVADO COM RESSALVAS

O lote pode seguir, desde que a EXEC aplique a correção obrigatória O-1 (uma entrada de pegadinhas.json; o texto substitutivo está abaixo). Não é necessária nova rodada. As correções R-1 a R-5 são recomendadas.

## 1. Conferência executada

### 1.1 itens.json (20 itens)
- Enunciados: os 20 foram comparados por script, palavra a palavra e sinal a sinal, com a seção (d) do v2, depois de aplicadas as erratas E1 (Q07), E2 (Q08) e E3 (Q11). Resultado: 20/20 idênticos.
- Justificativas: as 20 foram comparadas com o (d-G), com a E4 aplicada ao Q01. São 19 idênticas. No Q01, a única diferença é a maiúscula inicial em "No cálculo usual", que vem logo depois de ponto ("(era C). No cálculo..."). O ajuste é legítimo e não constitui achado.
- Gabarito, [TS] e VOLÁTIL foram derivados do (d-G) e conferidos com o registro GBQ v2: 20/20 conferem. São 10 C e 10 E, 10 [TS] (4 C e 6 E) e 4 VOLÁTEIS (Q14, Q16, Q18, Q19).
- itemEdital confere com a cobertura do (d-G) e com o registro GBQ: 1.1=2, 1.2=2, 1.3=2, 1.4=3, 1.5=2, 1.6=3, 1.7=3, 1.8=3.
- rotulo "AUTORAL" e aderencia "direta" estão corretos em todos os itens. comando é idêntico ao do bloco (d), textoBase está vazio (a fonte não tem texto-base) e o campo fonte está correto.
- observacao está correta: "VOLÁTIL — reverificar entre 4 e 8/1/2027" nos 4 voláteis, "texto conforme errata E1/E2/E3" em Q07, Q08 e Q11 e "justificativa conforme errata E4" no Q01.
- IDs: L1-Q01 a L1-Q20, sem duplicatas nem faltantes, com numero de 1 a 20 e lote "L1". O JSON é válido.

### 1.2 curso.md
O texto foi comparado integralmente com a seção (a), não apenas por amostragem. Trechos conferidos por subitem, no mínimo 3:
- 1.1: definição de ASR; pipeline clássico (5 etapas); WER com E4 aplicada ("No cálculo usual, sobre texto normalizado..."); pegadinha com E4 aplicada ("no cálculo usual ele ignora pontuação, e em qualquer convenção ignora locutores"). Conferem.
- 1.2: definição com F9/F10; as três negações de "end-to-end", a terceira com E9 aplicada literalmente; exemplo parlamentar; pegadinha. Conferem.
- 1.3: definição e cascata; evidências OpenAI [F2] e Google [F8, 32 tokens; gemini-3.5-transcribe]; contraste com o LLM speech do Azure [F4]; pegadinhas (1) a (5). Conferem.
- 1.4: definição e DER; os três conceitos; até quatro referências de 2 a 10 s [F1]; limitações por modo (chirp_3 [F3], OpenAI [F1], AWS ShowSpeakerLabel [F7]). Conferem.
- 1.5: pós-processamento e geração direta [F3, F6]; pontuação falada [F3]; exemplo "Aprovado." vs "Aprovado?". Conferem.
- 1.6: mapa dos 6 desafios; mitigação por fornecedor (Google até 1.000 frases; AWS CV/CLM [F6, F11, F5]; Azure; OpenAI 224 tokens); "Distinção decisiva"; exemplo dos 513 deputados. Conferem.
- 1.7: parciais e finais; endpointing [F3]; estabilização [F7]; recursos por modo; stream=true [F1]. Conferem.
- 1.8: Whisper (observação P6, MIT, 98 idiomas, whisper-1/gpt-transcribe, 25 MB, 224 tokens); Google; Azure [F12]; AWS; quadro-síntese, cujas células conferem uma a uma, inclusive a nota "*"; exemplo parlamentar com E10 aplicada; pegadinha. Conferem.
- Erratas: E4 nos dois pontos do 1.1; E9 no 1.2; E10 no 1.8. Aplicadas em todos os pontos que indicam.
- Omissões: a tabela de correções, o cabeçalho de entrega e a nota "Fontes F9 a F12 foram abertas e confirmadas pela CQFP... a CPP não as reabriu". São todas metadados ou notas entre unidades. A convenção de evidência, a lista F1–F12 e todos os "[V data]" foram mantidos.
- Não há conteúdo novo. Só a marcação foi ajustada: títulos, negrito, listas e a tabela Markdown do quadro.

### 1.3 resumo.md
O texto foi comparado integralmente com a seção (b) e confere. A E5 está aplicada: "CLM (texto; indisponível para pt-BR na AWS)". A linha END-TO-END do resumo não contém a generalização do espectrograma, de modo que a E9 não incide; a decisão do produtor está correta. A E4 não lista o resumo, por isso "não mede pontuação nem locutor" fica como na fonte; não há achado de extração (ver observação 3).

### 1.4 pares.json (17)
Os 17 pares conferem com a seção (c), sem paráfrase que mude sentido. O par 1, ternário, ficou com a = "ASR" e b = "diarização vs identificação de locutor". É forma literal e aceitável. O par 15 tem "como" vazio porque a fonte não traz glosa. Não há achado.

### 1.5 pegadinhas.json (31)
As 31 entradas foram conferidas com as "PEGADINHA PROVÁVEL" de 1.1 a 1.8, e o motivo de cada uma foi conferido com o texto do curso ou do (d-G). Trinta são fiéis. Uma altera o sentido da fonte (O-1).

### 1.6 discursivas.json (DISC-L1-Q)
- comando: o enunciado (e) está integral, com R3 ("necessária"). A E8 está aplicada: frase de abertura "15,00 / 0,70" e "[valor: 5,00 / 4,00 / 5,30 pontos]" ao fim das alíneas a, b e c. linhas = 20.
- Valores: 5,00 + 4,00 + 5,30 + 0,70 = 15,00, soma conferida. A E7 está aplicada (2.3 = 5,30; apresentação 0,70; nota de correção "(5,00 / 4,00 / 5,30), mais 0,70 de apresentação").
- padrao: integral, conferido com a Parte B. A divisão em 3 parágrafos coincide com as quebras temáticas da fonte.
- Quesitos 2.1, 2.2 e 2.3: as descrições, os conceitos 0–4, 0–3 e 0–4 e os critérios, incluindo os aspectos (i)–(v) e (i)–(iii), estão literais. As notas (verificação 1:1; anulações; normalização de números) e a notaCorrecao estão literais. baseNormativa = [] ("não se aplica"), correto.

## 2. Achados

### O-1 — pegadinhas.json, entrada de P2-1.3 nº 5 (13ª entrada do arquivo): paráfrase que muda o sentido
- Local: pegadinhas.json, objeto {"itemEdital": "P2-1.3", "texto": "A prova cobra o nome/versão do modelo → ERRADO (...)"}.
- Problema: a fonte (1.3, pegadinha (5)) diz: "Nomes e versões de modelos mudam em meses: a banca pode cobrar o CONCEITO, não o nome do produto." A fonte não afirma que a prova deixa de cobrar nome ou versão. A afirmação criada, "A prova cobra o nome/versão do modelo", marcada como ERRADO, transforma um "pode cobrar o conceito" em uma negação categórica, que não está na fonte. Além disso, o próprio edital 1.8 nomeia ferramentas (Whisper, Google, Azure, AWS). Trata-se de conteúdo novo com sentido alterado.
- Correção exata: substituir o valor de "texto" por:
  "Tratar nomes e versões de modelos como estáveis → ERRADO (nomes e versões de modelos mudam em meses: a banca pode cobrar o CONCEITO, não o nome do produto)"
  Alternativa equivalente: excluir a entrada. Nesse caso, P2-1.3 passa a 4 pegadinhas e o total a 30.

### R-1 — itens.json, campo justificativa: prefixo de metadados (regra de forma da EXEC)
- Local: os 20 itens. Os prefixos são gabarito, [TS], "convertido (era X)", "convertido (era item de produto)", "novo (substitui item de produto)" e "VOLÁTIL (verificado em 07/10/2026)". IDs: L1-Q01, Q02, Q03, Q04, Q05, Q06, Q07, Q08, Q09, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20.
- Correção exata: substituir cada justificativa pelo texto abaixo. O texto é o mesmo de hoje, sem o prefixo; nada mais muda. "Falsa pegadinha:" e "Erro por extrapolação/generalização" são comentário didático do d-G e permanecem.
  - L1-Q01: "No cálculo usual, pontuação e capitalização ficam fora do WER, e a atribuição de locutor fica fora em qualquer convenção, então WER 0% não garante fidelidade nesses aspectos. Erro por extrapolação."
  - L1-Q02: "ASR produz texto; atribuir falas a locutores é diarização (rótulos) ou identificação (nomes), módulos distintos."
  - L1-Q03: "Modelos end-to-end podem produzir trechos fluentes porém falsos onde o áudio é ruim; a arquitetura não imuniza contra alucinação. Erro por generalização."
  - L1-Q04: "Falsa pegadinha: \"supervisão fraca\" parece sugerir ausência de rótulos, mas significa transcrições preexistentes; pares áudio–texto continuam necessários."
  - L1-Q05: "É o que distingue o modelo nativo da arquitetura em cascata: áudio como entrada do próprio LLM [V 07/10/2026 — F8]."
  - L1-Q06: "Na cascata o LLM recebe apenas o texto do ASR; prosódia se perde — justamente a limitação que o áudio nativo pretende superar."
  - L1-Q07: "Diarização entrega rótulos genéricos (Locutor 1, 2...); exibir nomes exige identificação (amostra cadastrada ou revisão humana). Erro por extrapolação."
  - L1-Q08: "Falsa pegadinha: a frase soa invertida mas está correta — verificação é 1:1 contra identidade alegada; diarizar não exige verificar nem identificar."
  - L1-Q09: "DER soma erro de falante, fala perdida e falso alarme; WER soma substituições, deleções e inserções de palavras. Métricas distintas para tarefas distintas."
  - L1-Q10: "Modelos end-to-end podem emitir texto já pontuado e capitalizado; pipelines clássicos em geral restauram pontuação em etapa posterior."
  - L1-Q11: "Falsa pegadinha: o item parece confundir os dois recursos, mas os distingue corretamente — ditado do sinal versus inferência do sinal."
  - L1-Q12: "Adaptação de vocabulário enviesa o reconhecimento para termos esperados; não garante acerto em qualquer condição acústica nem corrige sotaque. Erro por generalização."
  - L1-Q13: "Adaptação é lista de termos que enviesa o reconhecimento, não retreino acústico; sotaque pede dados acústicos/modelo customizado."
  - L1-Q14: "Distinção documentada pela AWS: custom vocabulary amplia o vocabulário base [F6]; custom language model é treinado com dados de texto [F11]."
  - L1-Q15: "Funcionamento padrão do streaming: parciais revisáveis e final em geral consolidado após o fim do enunciado."
  - L1-Q16: "stream=true devolve texto incremental de um arquivo já completo; áudio ao vivo usa a transcrição Realtime, fluxo distinto [F1]."
  - L1-Q17: "Falsa pegadinha: o item parece afirmar ganho duplo, mas afirma o trade-off correto — menor latência, risco de fragmentar enunciados."
  - L1-Q18: "Código e pesos abertos no repositório openai/whisper, licença MIT [F10]; a API recomenda gpt-transcribe para transcrição geral e reserva whisper-1 a timestamps, legendas e tradução [F1]."
  - L1-Q19: "A documentação oficial prevê implantação em nuvem ou on-premises via contêineres [F4]."
  - L1-Q20: "Em serviço em nuvem o áudio é enviado a infraestrutura de terceiro; só a execução local mantém o áudio sob controle exclusivo da instituição. Equivalência de custódia é falsa."

### R-2 — itens.json, campo observacao de L1-Q14, Q16, Q18 e Q19: preservar a data de verificação retirada pela R-1
- Motivo: retirar o prefixo "VOLÁTIL (verificado em 07/10/2026)" elimina do item a data de verificação do fato de produto, que é exigida pela regra EVIDÊNCIA do Projeto.
- Correção exata: nos 4 itens, observacao = "VOLÁTIL (verificado em 07/10/2026) — reverificar entre 4 e 8/1/2027".

### R-3 — discursivas.json, aspectosValorados[].aspecto: rótulos compostos pelo produtor
- Local: os 3 objetos de aspectosValorados.
- Problema: os textos "a) Modos de processamento (tempo real e lote) e recurso disponível...", "b) ...", "c) ..." não existem na fonte. São resumos das alíneas. O sentido não muda, mas há fonte literal disponível: os títulos dos quesitos da Parte B.
- Correção exata:
  - [0].aspecto = "Modos de processamento (tempo real × lote)"
  - [1].aspecto = "Diarização × identificação de locutor"
  - [2].aspecto = "Desafios do pt-BR em plenário e mitigação"

### R-4 — discursivas.json, itensEdital inferido
- Local: "itensEdital": ["P2-1.4","P2-1.6","P2-1.7"].
- Problema: a fonte não declara os subitens da discursiva, e a ESPEC manda deixar vazio o campo inexistente na fonte. O mapeamento inferido, porém, é coerente com o conteúdo das alíneas (a ↔ 1.7, b ↔ 1.4, c ↔ 1.6), e o relatório o registra como dúvida.
- Correção exata, a critério da EXEC (há duas opções válidas):
  - aplicar a regra literal da ESPEC: "itensEdital": [];
  - ou manter ["P2-1.4","P2-1.6","P2-1.7"] por decisão expressa da EXEC. O QA confirma que esse mapeamento é fiel às alíneas.

### R-5 — relatorio.md: contagem de pegadinhas após O-1
- Se a O-1 for aplicada por substituição, nada muda.
- Se for aplicada por exclusão, substituir "Pegadinhas: 31 (1.1=5, 1.2=4, 1.3=5, ..." por "Pegadinhas: 30 (1.1=5, 1.2=4, 1.3=4, ...". O restante da linha não muda.

## 3. Observações (sem achado)
1. As chaves extras "notas" (quesitos 2.2 e 2.3) e "notaCorrecao" estão fora do esquema, mas o conteúdo é literal da Parte B e está declarado no relatório. Ficam a critério do consumidor.
2. A fonte tem uma incoerência interna, que não decorre da extração: o motivo do Adendo E7/E8 diz "Os tópicos de conteúdo somam 14,30 (6,00 + 7,00 + 1,30)", mas os valores corrigidos são 5,00 + 4,00 + 5,30 = 14,30. Os fragmentos usam corretamente 5,00 / 4,00 / 5,30. Sugere-se que a GCE corrija a parcela do motivo, se julgar útil.
3. O resumo diz que o WER "não mede pontuação nem locutor", com redação mais forte que a do curso pós-E4. A E4 não alcança o resumo, e a extração está fiel. Eventual errata cabe à GCE.
4. A E6 (risco: nenhum ALTO; Q16 e Q18 MÉDIO; Q14 e Q19 BAIXO) e o R-J (reverificar o fato de produto do curso 1.4, "até quatro referências de 2 a 10 s [F1]") estão corretamente registrados no relatório, sem campo próprio.
5. Os números do relatório (20 itens; 10 C e 10 E; 10 [TS], 4 C e 6 E; 4 VOLÁTEIS; 17 pares; 31 pegadinhas; 1 discursiva) foram conferidos e estão corretos.

FIM DO PARECER


========== L1C ==========
PARECER DE QA — EXEC-01 — L1C — RODADA 1 — Opus — 12/10/2026

Escopo: fragmentos de /home/claude/exec01/frag/L1C/ (itens.json, meta.json, curso.md, resumo.md, pares.json, pegadinhas.json, discursivas.json, relatorio.md), conferidos contra ESPEC_EXEC01.md e as fontes canônicas lidas pela ferramenta Projects em 12/10/2026: GCE_Lote1C_v2_CPP.md, GCE_Lote1C_consolidacao_GCE.md (E1–E4, NB5), GCE_Lote1_consolidacao_GCE.md (E1 do Lote 1, citada no adendo (a)) e claude/GBQ_Registro_AUTORAL_v2.md. QA independente: não produzi os fragmentos e não os editei.

## CONCLUSÃO: APROVADO COM RESSALVAS

Não há achado obrigatório. As correções R-1 a R-4 são recomendadas.

## 1. Conferência executada

### 1.1 itens.json (10 itens)
- Enunciados: os 10 foram comparados por script, palavra a palavra e sinal a sinal, com a seção (d) do v2, depois de aplicada a errata E3 (NB3) ao Q23. Resultado: 10/10 idênticos. No Q23, o primeiro "em regra" foi retirado e o segundo mantido, como manda a E3.
- Justificativas: as 10 foram comparadas com o (d-G), com as erratas aplicadas. São 8 idênticas.
  - L1C-Q26: a E1 (NB1) está aplicada. As aspas simples de 'por esse motivo' da errata foram passadas a aspas duplas. Isso só desfaz o aninhamento de aspas da errata e não constitui achado.
  - L1C-Q24: a E4 (NB4) está aplicada, mas fundida ao colchete existente (R-2).
- Gabarito e [TS] foram derivados do (d-G) e conferidos com o registro GBQ v2: 10/10 conferem. São 4 C (Q23, Q24, Q27, Q29) e 6 E, 5 [TS] (2 C: Q24 e Q27) e volatil = false em todos (VOLÁTEIS = 0).
- itemEdital confere com o (d-G) e com o GBQ: 1.1 a 1.5, 2 itens em cada.
- rotulo "AUTORAL" e aderencia "direta" estão corretos. comando é idêntico ao bloco (d), textoBase está vazio e o campo fonte está correto.
- observacao está correta em Q23 (E3), Q24 (E4) e Q26 (E1). No Q28 há uma ressalva (R-3).
- IDs: L1C-Q21 a L1C-Q30, sem duplicatas nem faltantes, com numero de 21 a 30 conforme o GBQ. O JSON é válido.

### 1.2 curso.md
O adendo (a) foi comparado integralmente com a fonte: título do edital; sentido amplo; sentido próprio; regras de decisão 1 a 4; "Ligação com a prática da Casa"; "Ponte que confunde" [F1]; pegadinhas adicionais (1) a (4). O texto confere sem alteração, e não há conteúdo novo. As omissões verificadas são todas metadados ou instruções entre unidades, e a omissão é legítima: tabela de correções, seção EVIDÊNCIA (fora da seção (a)), tabela de cobertura e "Fundador: gravar como...". A remissão à errata E1 do Lote 1 já está no texto-fonte.

### 1.3 resumo.md, pares.json, discursivas.json
Estão vazios (0 bytes, [] e []), e é o correto: a fonte não tem seção (b) nem (c) e declara "Sem discursiva e sem peça". O relatório registra os três.

### 1.4 pegadinhas.json (4)
As 4 entradas correspondem às "PEGADINHAS ADICIONAIS" (1) a (4), todas de P2-1.4. Os motivos foram extraídos do próprio adendo (regras 3 e 4, "Ponte que confunde") e do (d-G) do Q27. Não há conteúdo novo nem sentido alterado. Há uma ressalva de forma (R-4).

### 1.5 Erratas
- E1 (Q26, comentário) e E3 (Q23, texto) estão aplicadas.
- E4 (fonte wav2vec 2.0) está aplicada, com ressalva de forma (R-2).
- E2 só altera a tabela de correções, que não foi extraída, e por isso não tem efeito nos fragmentos.
- NB5 é registro sem alteração (ver R-3).

## 2. Achados

### R-1 — itens.json, campo justificativa: prefixo de metadados (regra de forma da EXEC)
- Local: os 10 itens. Os prefixos são gabarito, [TS] e subitem ("— 1.x"). IDs: L1C-Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28, Q29, Q30.
- Correção exata: substituir cada justificativa pelo texto abaixo. "Falsa pegadinha:" e "Erro por extrapolação/generalização:" são comentário didático do d-G e permanecem. O Q24 já incorpora a R-2.
  - L1C-Q21: "Inverte as funções: o modelo acústico liga o áudio a unidades sonoras; o de linguagem estima sequências de palavras."
  - L1C-Q22: "Erro por extrapolação: inserções entram no numerador, e o WER pode ultrapassar 100%."
  - L1C-Q23: "Sem léxico separado, a correção passa, em regra, por adaptação (1.6) ou mais dados; dados de pronúncia são recurso de custom speech (Azure [F4])."
  - L1C-Q24: "Falsa pegadinha: em muitos sistemas há espectrograma (ex.: Whisper [F9]), mas não é universal; o wav2vec 2.0 recebe áudio bruto [V 08/10/2026 — arXiv 2006.11477] [verificado pela GCE-CQFP (QAP) em 08/10/2026 — arxiv.org/pdf/2006.11477, seção 2]."
  - L1C-Q25: "Erro por generalização: o LLM nativo gera texto plausível, não copia; o edital mantém a revisão humana (2.2)."
  - L1C-Q26: "ASR reforçado por LLM não é LLM nativo: reforço por LLM não implica, por si, que o áudio entre como modalidade do próprio LLM; o nexo \"por esse motivo\" é falso."
  - L1C-Q27: "Falsa pegadinha: \"identificar\" no sentido amplo é distinguir; nomes exigem cadastro ou atribuição humana."
  - L1C-Q28: "O OBJETO decide: \"que há três oradores\" = distinguir; \"pelo nome\" = identificação própria (amostras ou atribuição humana)."
  - L1C-Q29: "A pontuação é inferida e pode mudar o sentido (\"Aprovado.\" × \"Aprovado?\"); a revisão a confere."
  - L1C-Q30: "Erro por generalização: a capitalização estima e pode errar (Câmara × câmara)."

### R-2 — itens.json, L1C-Q24, justificativa: a E4 foi fundida ao colchete original em vez de acrescentada
- Situação atual: "...recebe áudio bruto [V 08/10/2026 — arXiv 2006.11477; verificado pela GCE-CQFP (QAP) em 08/10/2026 — arxiv.org/pdf/2006.11477, seção 2]."
- A E4 manda acrescentar o colchete próprio "[verificado pela GCE-CQFP (QAP) em 08/10/2026 — arxiv.org/pdf/2006.11477, seção 2]". O conteúdo está presente; a forma não é a literal.
- Correção exata, se a R-1 não for aplicada: "C [TS] — 1.2. Falsa pegadinha: em muitos sistemas há espectrograma (ex.: Whisper [F9]), mas não é universal; o wav2vec 2.0 recebe áudio bruto [V 08/10/2026 — arXiv 2006.11477] [verificado pela GCE-CQFP (QAP) em 08/10/2026 — arxiv.org/pdf/2006.11477, seção 2]."
- Se a R-1 for aplicada, vale o texto do Q24 dado na R-1.

### R-3 — itens.json, L1C-Q28, observacao: nota interna de calibração
- Situação atual: "discriminação baixa (NB5 da consolidação; registro, sem alteração)".
- Problema: a NB5 é uma lição para lotes futuros, dirigida às unidades. Não é errata, VOLÁTIL nem REVERIFICAR, que são as categorias de observacao da ESPEC. O dado já consta do registro GBQ (coluna "Marca"), e um aviso desses não deve chegar à estudante.
- Correção exata: observacao = "". Se a EXEC quiser rastreabilidade, o lugar é o relatorio.md.

### R-4 — pegadinhas.json: aspas externas e aspas internas trocadas
- Problema: as 4 entradas envolvem a ação inteira em aspas duplas e passam as aspas internas da fonte a simples ('identificação', 'o sistema sabe os nomes', 'sempre'). A fonte usa aspas duplas nos termos citados e não cita a ação inteira. O L1 grava as pegadinhas sem aspas externas, o que gera inconsistência entre lotes.
- Correção exata do campo "texto":
  1. "Ler \"identificação\" do título como \"o sistema sabe os nomes\" → ERRADO (no título, \"identificação e separação\" pode ser sentido amplo, isto é, distinguir; saber os nomes exige cadastro ou atribuição humana)"
  2. "Ler \"identificar\" no item como identificação de locutor sem checar o objeto → ERRADO (não se julga pelo verbo: procure o OBJETO da frase)"
  3. "Dizer que diarização que distingue oradores também verifica identidade → ERRADO (verificação de locutor é outra coisa: 1 para 1, contra uma identidade alegada)"
  4. "Dizer que, por existirem amostras de referência, a diarização \"sempre\" entrega nomes → ERRADO (depende de as amostras terem sido fornecidas; o nome existe por causa das amostras, não da diarização em si)"

## 3. Observações (sem achado)
1. O curso.md mantém, por fidelidade, remissões internas da fonte: "(errata E1)", "(v2, item 1.4)", "(v2, exemplo parlamentar do 1.4)" e "[V 07/10/2026 — F1, v2]". Não são instruções a unidades, e a ESPEC manda manter o texto. A EXEC pode decidir se a plataforma as exibe.
2. F1 e F9 são citados no L1C, mas a lista de fontes F1–F12 está no curso.md do L1. Convém que a montagem do pacote mantenha a lista acessível aos dois lotes.
3. Os números do relatório (10 itens; 4 C e 6 E; 5 [TS], 2 C; 0 VOLÁTEIS; 2 itens por subitem; 4 pegadinhas; resumo, pares e discursivas vazios) foram conferidos e estão corretos.

FIM DO PARECER


========== L2 ==========
PARECER DE QA — EXEC-01 — L2 — RODADA 1 — Opus — 12/10/2026

QA independente (não produziu os fragmentos). Fragmentos não editados.
Padrão conferido: /home/claude/exec01/ESPEC_EXEC01.md e ESPEC_QA_EXEC01.md.
Fontes lidas em 12/10/2026 (Projects/project_read): GCE_Lote2_v2_CPP.md, GCE_Lote2_padroes_GCE.md, GCE_Lote2_consolidacao_GCE.md (E1–E4, adendo 1 com E5–E6), claude/GBQ_Registro_AUTORAL_v2.md.

## CONCLUSÃO: APROVADO COM RESSALVAS

Nenhum achado O (obrigatório). 9 achados R (forma). Nenhum erro de enunciado, gabarito, comando, valor ou errata. Nenhum conteúdo inventado.

## 1. Conferências realizadas

### 1.1 itens.json (30 itens)
- Método: transcrevi as seções (d) e (d-G) do v2, apliquei as erratas E1(d) e E6 e comparei por script (python3 -I), com igualdade estrita de string, enunciado e justificativa de todos os 30 itens. Resultado: 30/30 enunciados idênticos à versão (d); 30/30 justificativas idênticas ao d-G sem o prefixo "Qnn. G [TS] — sub.".
- gabarito, itemEdital e ts: 30/30 conforme o d-G e o registro GBQ v2. volatil = false em todos (d-G: "VOLÁTEIS: 0"; Q23 NÃO VOLÁTIL).
- Contagens: C = 15, E = 15; [TS] = 15 (7 C); cobertura 2.1=4, 2.2=4, 2.3=4, 2.4=4, 2.5=4, 2.6=3, 2.7=4, 2.8=3. Iguais à Parte C da consolidação e à tabela de cobertura do v2.
- IDs L2-Q01..L2-Q30: sem duplicata, sem falta. lote, numero, rotulo AUTORAL, aderencia "direta", textoBase "", comando ("Julgue os itens a seguir (C = certo, E = errado).") conforme a fonte.
- Erratas nos itens: E6 aplicada na justificativa do L2-Q14 (texto idêntico ao do adendo 1); E1(d) aplicada na justificativa do L2-Q21. As duas registradas em observacao. Os enunciados não têm errata no Lote 2 (confirmado).
- Regra 6 (prefixo de metadados na justificativa): nenhum ID com prefixo. A menção "NÃO VOLÁTIL (classificação final da CQFP)" no L2-Q23 fica no fim do comentário, como no d-G, e não é prefixo.

### 1.2 curso.md
- Comparação integral (não só por amostra) das oito seções com a seção (a) do v2.
- Erratas no curso: E1(a) em 2.6 DEFINIÇÃO; E2 em 2.4, tipo de intervenção; E3 em 2.4, identificação de oradores; E4 em 2.1 (contexto institucional) e 2.3 (contexto oficial); E5 em 2.4, EXEMPLO PARLAMENTAR, com o texto idêntico ao do adendo 1. Todas aplicadas. Não há outra menção a "DETAQ" fora da forma "Derep, antigo DETAQ" nos fragmentos.
- Omissões: só os blocos fora da seção (a) (cabeçalho, tabela de correções, notas de conferência, fontes F1–F8, limites N1–N8). Correto pela especificação.
- Divergências textuais: R-2, R-3 e R-5 (forma).

### 1.3 resumo.md
- Igual à seção (b), com E1(b) aplicada na linha 2.6. Linha 2.4 mantida como na fonte (ver R-1).

### 1.4 pares.json (22) e pegadinhas.json (43)
- pares: 22/22 fiéis à seção (c), com E1(c) no par 15. As soluções de divisão dos pares 9 e 15, registradas no relatório, não mudam o sentido.
- pegadinhas: 43 (2.1=5, 2.2=5, 2.3=5, 2.4=6, 2.5=6, 2.6=6, 2.7=5, 2.8=5). Os motivos foram tirados do próprio curso, sem conteúdo novo e sem paráfrase que mude o sentido. Exceção de forma: R-4.

### 1.5 discursivas.json (2)
- DISC-L2-Q: comando idêntico à seção (e). Valores 5,00 + 5,00 + 4,30 = 14,30; + 0,70 = 15,00. 20 linhas. Padrão e quesitos 2.1 a 2.3 fiéis a GCE_Lote2_padroes_GCE.md.
- DISC-L2-P: comando idêntico à seção (f). Valores 2,00 + 8,00 + 6,00 + 7,00 + 5,50 = 28,50; + 1,50 = 30,00. 50 linhas. Gênero "parecer técnico". Padrão (síntese) e quesitos 2.1 a 2.5 fiéis aos padrões.
- Somas conferidas por script: conferem com os valores das alíneas e dos tópicos e com a Parte C da consolidação.
- Pontos de forma: R-6, R-7, R-8.

### 1.6 Dúvidas do produtor (relatorio.md)
- Dúvida 1: registrada como R-1. O conteúdo canônico não foi alterado. A decisão de mérito é da GCE.
- Dúvida 2 (marca [V — F2] no curso 2.1) e dúvida 3 ("pela ordem" no curso 2.4): sem achado. O texto segue o v2 aprovado pela CQFP e consolidado pela GCE. Não cabe à extração nem ao QA da extração alterá-lo.
- Dúvida 4: confirmada. Não há divergência de gabarito, subitem, [TS] ou contagem.

## 2. Achados

### Obrigatórios (O)
Nenhum.

### Recomendados (R)

R-1 — resumo.md, linha "2.4 FORMATAÇÃO", frase final "Convenção exata da Câmara: NÃO VERIFICADA." (dúvida 1 do produtor)
- Fato: depois da E3, o curso 2.4 diz que a forma de identificar o orador "foi observada nas notas oficiais de 2026 (N1)". A E3 manda alterar só o curso 2.4 e a nota N1. Não menciona o resumo (b). Por isso o produtor manteve o texto da fonte, e manteve corretamente.
- A contradição é PARCIAL. Na linha 2.4 do resumo, a frase cobre dois pontos. A identificação do orador (N1) foi superada pela E3. A convenção de marcação de pausas e de eventos não falados (N2) continua sem verificação, e nesse ponto a frase segue verdadeira.
- Recomendação: MANTER o texto do resumo sem alteração, porque não cabe aplicar errata que a GCE não emitiu. ACRESCENTAR observação no nível do lote. Proposta de texto, no campo "observacao" do meta.json (se a EXEC admitir o campo; senão, no relatorio.md e no despacho à GCE):
  "Resumo (b), linha 2.4: a frase 'Convenção exata da Câmara: NÃO VERIFICADA.' foi mantida como na fonte. Depois da errata E3, a forma de identificar o orador foi observada nas notas oficiais de 2026 (curso 2.4). A convenção de marcação de pausas e de eventos não falados continua sem verificação (N2). Pendente: decisão de mérito da GCE sobre estender a E3 ao resumo."
- Mérito (estender a E3 ao resumo, por exemplo com "Identificação do orador: observada nas notas oficiais de 2026; convenção de marcação de eventos: NÃO VERIFICADA."): decisão da GCE. Não é objeto deste parecer.

R-2 — curso.md, 2.5, PEGADINHA PROVÁVEL (6), linha 137
- Fato: o fragmento acrescenta uma palavra ausente da fonte. Onde está "e apenas o recomenda para os demais.", a fonte diz "e apenas recomenda para os demais.".
- Correção: substituir "a Portaria o torna obrigatório para documentos administrativos e apenas o recomenda para os demais." por "a Portaria o torna obrigatório para documentos administrativos e apenas recomenda para os demais.".
- Não muda o sentido, mas viola o "mantenha o texto". O mesmo "o" em pegadinhas.json (2.5, 6ª entrada) é paráfrase admitida e não precisa mudar.

R-3 — curso.md, 2.1, "Contexto institucional", linha 13
- Fato: ao aplicar a E4, o produtor trocou o conector da fonte "por força do Ato da Mesa" por "conforme o Ato da Mesa". A E4 fixa a denominação e a base ("pelo Ato da Mesa nº 251, de 16/03/2026, arts. 1º e 2º, I") e não pede essa troca.
- Correção: substituir ", conforme o Ato da Mesa nº 251, de 16/03/2026, arts. 1º e 2º, I [V 08/10/2026 — Legin; F8; NORMATIVO — QA]." por ", por força do Ato da Mesa nº 251, de 16/03/2026, arts. 1º e 2º, I [V 08/10/2026 — Legin; F8; NORMATIVO — QA].".

R-4 — pegadinhas.json, 4ª entrada de P2-2.6: "Cobrar recurso de produto específico → ERRADO (sem fonte datada, não é seguro; cobrar o CONCEITO)"
- Fato: a fonte (2.6, pegadinha 4) não traz uma afirmação a julgar. Traz uma orientação de elaboração: o que cobrar. No formato "<afirmação> → ERRADO", a entrada atribui valor de verdade a algo que não é proposição e, para o estudante, perde o sentido. O produtor já havia sinalizado o caso.
- Correção: excluir a entrada de pegadinhas.json. Ajustar o relatorio.md para "pegadinhas.json: 42 (… 2.6=5 …)" e registrar o motivo. O curso.md mantém a pegadinha (4) como está na fonte.

R-5 — curso.md, listas numeradas, linhas 35–42 (2.2, fluxo típico) e 60–62 (2.3, graus de tratamento)
- Fato: o marcador "- 1. …" combina um item de lista com outro marcador de lista ordenada. Em Markdown (CommonMark), isso gera uma lista ordenada aninhada dentro de cada item e mostra marcador duplo.
- Correção: trocar "- 1. ", "- 2. ", … por "1. ", "2. ", … (lista ordenada simples). Só marcação; o texto não muda.

R-6 — discursivas.json, notas internas em campos que o estudante vê
- (a) Critério do conceito "0" em DISC-L2-Q, quesitos 2.2 e 2.3. Substituir "Nenhum aspecto contabilizado (conceito 0 não explicitado na fonte; 'Conceito 0 a 4: por contagem, de \"apenas um\" a \"os quatro\"')." por "Nenhum aspecto contabilizado.".
- (b) Critério do conceito "0" em DISC-L2-P, quesito 2.3. Substituir pelo texto "Nenhum aspecto contabilizado, ou o candidato trata a normalização como correção do conteúdo.".
- (c) DISC-L2-P, campo padrao. Retirar a última linha "Nota (edital, 9.8.5.1, d): NQ = NC − 3 × NE ÷ TL.", que não faz parte do padrão de resposta (é regra de cálculo da nota), e acrescentá-la ao fim do campo observacao.
- (d) Acrescentar ao observacao das duas entradas: "Conceito 0 dos quesitos por contagem não explicitado na fonte ('Conceito 0 a 4: por contagem'); registrado como 'nenhum aspecto contabilizado'.".

R-7 — discursivas.json, DISC-L2-Q, aspectosValorados
- Fato: o texto das alíneas foi parafraseado: verbos no infinitivo e "o acordo de nível de serviço (SLA)" reduzido a "o SLA". Na DISC-L2-P, os tópicos foram transcritos literalmente. O sentido não muda, mas a fidelidade e a uniformidade ficam prejudicadas.
- Correção (texto literal das alíneas da seção (e), sem o "[valor]"):
  a) "a) diferencie transcrição automática, degravação e revisão humana, indicando a função da revisão humana nesse fluxo (human in the loop)"
  b) "b) apresente dois critérios de qualidade e fidelidade que a revisão deve observar, distinguindo o erro que altera o sentido do erro de forma, e indique como o revisor deve proceder diante de trecho inaudível"
  c) "c) explique como a revisão em dupla, a auditoria de amostras e o acordo de nível de serviço (SLA) contribuem para o controle de qualidade do fluxo, indicando uma limitação da auditoria por amostragem"

R-8 — discursivas.json, itensEdital das duas entradas (inferidos)
- Fato: a fonte não associa as discursivas a subitens. Pelo princípio da ESPEC_EXEC01 ("Se um campo não existir na fonte, deixe vazio"), o campo deveria ficar []. O produtor inferiu os subitens a partir dos títulos dos quesitos e registrou a inferência no observacao e no relatório. A inferência é coerente (questão: 2.1, 2.2, 2.3, 2.7; peça: 2.4, 2.5, 2.7, 2.8).
- Correção: a EXEC ratifica a inferência e mantém os valores, ou define "itensEdital": [] nas duas entradas. Sem ratificação, vale [].

R-9 — relatorio.md, seção "Campos vazios ou ajustados", 2º marcador
- Fato: diz "Q14 e Q21 trazem a nota de errata no comentário", mas a nota está no campo observacao. A justificativa traz o texto já corrigido, sem nota.
- Correção: substituir por "Q14 e Q21 trazem a nota de errata no campo observacao.".

## 3. Resumo para a EXEC
- O: 0. R: 9 (R-1 a R-9).
- Gabaritos, subitens, [TS], VOLÁTIL, enunciados, valores e erratas E1–E6: sem divergência.
- Pode seguir para montagem depois dos ajustes de forma. A rodada 2 é dispensável se a EXEC aplicar R-2 a R-9 de modo mecânico.
- R-1 depende da decisão de mérito da GCE.

FIM DO PARECER


========== L3 ==========
PARECER DE QA — EXEC-01 — L3 — RODADA 1 — Opus — 12/10/2026

QA independente (não produziu os fragmentos). Padrão conferido: /home/claude/exec01/ESPEC_EXEC01.md e ESPEC_QA_EXEC01.md.
Fontes lidas (Projects, project_read, 12/10/2026): GCE_Lote3_v2_CPP.md; GCE_Lote3_padroes_GCE.md; GCE_Lote3_consolidacao_GCE.md (Partes A–D); claude/GBQ_Registro_AUTORAL_v2.md; GCE_ItensReais_P9_GCE.md (apoio).
Itens reais: caderno oficial https://cdn.cebraspe.org.br/concursos/trf6_24/arquivos/034_TRF6_002_01.PDF e gabarito https://cdn.cebraspe.org.br/concursos/trf6_24/arquivos/GAB_DEFINITIVO_034_TRF6_002_01.PDF, baixados do cdn.cebraspe.org.br em 12/10/2026 (HTTP 200) e lidos com pdftotext.

## CONCLUSÃO: APROVADO COM RESSALVAS

Aplicar O-1 e O-2 antes da consolidação. São correções pontuais, com texto substitutivo dado abaixo; a EXEC pode conferi-las por diff, sem rodada 2. Os R são recomendados.

## 1. itens.json — o que foi conferido

- 30 AUTORAL: enunciado, gabarito, subitem, [TS] e justificativa de cada item comparados por script, palavra a palavra, com (d) e (d-G) do v2, já com a errata E3 aplicada ao comentário de Q20. Resultado: 0 diferenças. Os 30 enunciados são idênticos à versão do estudante; nenhuma errata da Parte A incide sobre enunciado.
- Gabarito, subitem e [TS] contra a tabela "Lote 3" do registro da GBQ v2: 0 divergências. Totais: 16 C / 14 E; 15 [TS], 6 deles com gabarito C (Q04, Q08, Q12, Q16, Q19, Q25); VOLÁTEIS = 0. Cobertura por subitem: 3.1–3.4 com 4 itens cada; 4.1 e 4.2 com 5; 4.3 com 4.
- observacao: Q20 "comentário conforme errata E3 da consolidação" e Q21 "REVERIFICAR (normativo) entre 4 e 8/1/2027" estão corretas; nenhum item VOLÁTIL. volatil = false em todos.
- rotulo e aderencia: AUTORAL = "direta"; reais = CEBRASPE_ANALOGA / "parcial" (ver o ponto P1).
- Itens reais 70 a 76: os 7 enunciados e os 2 comandos de bloco foram conferidos palavra a palavra contra o caderno oficial (substring exata após normalizar espaços, mais leitura visual do layout). Estão idênticos, inclusive a ausência de vírgula antes de "pois" no item 71 e a expressão "de forma absoluta" no 72. Os comandos de bloco também coincidem: 70–73 "Julgue os próximos itens, com base no disposto na Lei Geral de Proteção de Dados Pessoais (LGPD)." e 74–76 "Julgue os próximos itens, relativos ao tratamento de dados pessoais no poder público, conforme orientação da ANPD.".
- Gabarito definitivo oficial: 70 E, 71 E, 72 E, 73 C, 74 C, 75 C, 76 C. Coincide com itens.json e com a Parte D; nenhum dos 7 foi anulado (no cargo, os anulados são 58, 105 e 117).
- Cargo ("Cargo 2: Analista Judiciário — Área: Apoio Especializado — Especialidade: Análise de Dados"), aplicação (19/01/2025), ano do edital (2024) e url conferem com o cabeçalho do gabarito e com o P9.
- Justificativas dos reais: fiéis à Parte D, com as notas do 71 e do 73 e as ressalvas do 75 e do 76.
- IDs: 37 objetos, 37 IDs únicos, nenhum faltante (L3-Q01..Q30 e TRF6-2024-C2-070..076). O campo numero bate com o ID.
- Regra 6 (prefixo de metadados na justificativa): nenhuma justificativa começa com gabarito, [TS], VOLÁTIL, subitem ou "convertido". Atende. Ver R-6 (sufixo no Q21) e P3.

## 2. curso.md e resumo.md

- Comparei por script, palavra a palavra, todo o texto de 3.1 a 4.3 com a seção (a) do v2, já com as erratas e as omissões declaradas. A única diferença de texto é a de R-1; as demais diferenças são só títulos e marcação. Isso cobre, com folga, a amostra mínima de 3 trechos por subitem.
- Erratas:
  - E1(a), item 4.1, art. 20: aplicada ("consta como vetado na página compilada, com remissão à VEP nº 288/2019; o conteúdo do veto não foi conferido").
  - E1(b), resumo, linha 4.1: aplicada.
  - E2, dado sensível: aplicada ("enumera origem", sem "entre outros,").
  - E3: aplicada no curso, item 4.1, e na justificativa de Q20.
  - Gabarito de Q20 (E) inalterado.
- Omissões: só instruções internas às unidades ("(N5)", "(N6)", "(N6: não cobrar descrição de sistema real.)", "; não cobrar" no art. 5º, II e nas sanções, "— N7", "Fundador: gravar..."). Estão corretas.
- resumo.md: idêntico à seção (b), com E1(b) aplicada.
- Seção "Itens reais verificados": fiel à Parte D. Sobre o rótulo "(aderência parcial ao 4.1)" no título, ver P1.
- O-2: marca de verificação no cabeçalho de fontes.

## 3. pares.json

- 28 pares fiéis à seção (c). O campo "como" está vazio nos 17 pares sem descrição (10, 11, 12, 14 e 16 a 28), o que está correto.
- Ver R-2 (maiúscula no par 17) e R-3 (par 26, que é uma tríade).

## 4. pegadinhas.json

- 42 entradas: 3.1 a 3.4 com 5 cada, 4.1 com 9, 4.2 com 7 e 4.3 com 6, como no curso.
- Conferi as 42, uma a uma, contra o curso. Em todas o motivo do "ERRADO" vem do parêntese da própria pegadinha ou do texto do curso do mesmo subitem, e não há conteúdo novo.
- Achados: O-1 (pegadinha 4.1-(6) incompleta) e R-4 (pegadinha 3.4-(5)).

## 5. discursivas.json

- Questão (DISC-L3-Q): o comando é idêntico ao (e). Valores: 5,00 + 5,00 + 4,30 = 14,30; com a apresentação de 0,70, total de 15,00. Confere.
- Peça (DISC-L3-P): o comando é idêntico ao (f). Valores: 2,00 + 6,00 + 7,00 + 8,00 + 5,50 = 28,50; com a apresentação de 1,50, total de 30,00. Confere. Gênero: "parecer técnico".
- Aspectos (i)–(x) e (i)–(xix), quesitos e conceitos: idênticos ao bloco da CQFP. Os valorMax coincidem com os valores do enunciado.
- Notas de correção:
  - Questão: R2, R3, R4 e R6 fiéis, sem as passagens entre unidades.
  - Peça: R3 e R4 usam a redação dos "PONTOS PARA A RECONCILIAÇÃO" 2 e 3. O conteúdo é equivalente às decisões R3 e R4, sem efeito de mérito.
- baseNormativa: ver R-5.

## ACHADOS OBRIGATÓRIOS (O)

O-1 — pegadinhas.json, entrada nº 26 (itemEdital P2-4.1).
Problema: a pegadinha (6) do curso, item 4.1, tem duas partes: "ANPD como órgão da Presidência (redação superada), ou 'a autoridade nacional é a Agência' sem a criação pela Lei 15.352/2026". A paráfrase manteve só a primeira e trocou o sujeito "ANPD" por "a autoridade nacional". Perdeu-se a segunda pegadinha, justamente a que contrasta com L3-Q21 (gabarito C) e com o curso ("A autoridade nacional não 'é' a Agência por definição; passou a ser exercida por ela"). O sentido da entrada ficou reduzido.
Correção: substituir o "texto" da entrada nº 26 por:
"A ANPD é órgão da Presidência da República, ou a autoridade nacional é a Agência por definição, sem a criação pela Lei 15.352/2026 → ERRADO (a redação anterior, de órgão da Presidência da República, está superada; a Lei 15.352/2026 cria a Agência Nacional de Proteção de Dados (ANPD), autarquia de natureza especial vinculada ao MJSP, e a autoridade nacional não "é" a Agência por definição: passou a ser exercida por ela)"
A contagem de pegadinhas não muda (42).

O-2 — curso.md, cabeçalho de fontes, 3º bullet (F3).
Problema: o produtor criou a marca "[V 08/10/2026 — F3]". No v2, a convenção [V data — Fn] não é aplicada a nenhuma fonte, e a nota N2 registra que a unidade NÃO abriu a página da Lei 15.352/2026: as alterações foram lidas na LGPD compilada (F1). A marca afirma uma verificação que a fonte nega, o que fere a regra de EVIDÊNCIA e conta como conteúdo inventado. Em F1 e F2, a marca coincide com "Aberta e lida integralmente em 08/10/2026" e pode ficar.
Correção: onde se lê "- [V 08/10/2026 — F3] Lei 15.352/2026: as alterações foram lidas na própria LGPD compilada (F1), com a anotação", leia-se "- F3 Lei 15.352/2026: as alterações foram lidas na própria LGPD compilada (F1), com a anotação". O resto do bullet fica inalterado.

## ACHADOS RECOMENDADOS (R)

R-1 — curso.md, item 4.1, bullet "Anonimização e pseudonimização", última frase. O curso acrescentou "só". Onde se lê "Pseudonimizar NÃO é, por si só, anonimizar.", leia-se "Pseudonimizar NÃO é, por si, anonimizar." (texto do v2).

R-2 — pares.json, par 17, campo "b". Só neste par o "b" começa com maiúscula. Onde se lê "Pseudonimização (art. 13, § 4º, ...", leia-se "pseudonimização (art. 13, § 4º, ...".

R-3 — pares.json, par 26. A fonte traz uma tríade, sem contraste A × B. O desdobramento "Confidencialidade" × "Integridade e disponibilidade" cria uma oposição que a fonte não tem. Substituir por {"a": "Confidencialidade, integridade, disponibilidade", "b": "", "como": ""} e registrar no relatorio.md.

R-4 — pegadinhas.json, entrada nº 20 (P2-3.4). O curso diz "A banca pode cobrar o CONCEITO, e não o nome do produto"; a paráfrase endureceu a frase. Onde se lê "(nomes e versões são voláteis e não verificados; o que se cobra é o conceito)", leia-se "(nomes e versões de modelos mudam em meses e não foram verificados; a banca pode cobrar o conceito, e não o nome do produto)".

R-5 — discursivas.json, DISC-L3-P, baseNormativa[0]. O intervalo "V-VII" inclui o art. 5º, V (titular), que nenhum aspecto do padrão cita. Onde se lê "Lei 13.709/2018 (LGPD), art. 5º, I, V-VII, X, XV e XVII", leia-se "Lei 13.709/2018 (LGPD), art. 5º, I, VI, VII, X, XV e XVII".

R-6 — itens.json, L3-Q21, justificativa. É sufixo, não prefixo, mas segue a mesma lógica da regra 6: o dado já está em observacao, e a plataforma mostra a justificativa ao estudante. Retirar o trecho final " REVERIFICAR (normativo) 04–08/01/2027; não VOLÁTIL.", de modo que a justificativa termine em "a \"autoridade nacional\" passou a ser exercida por ela." Se a EXEC preferir o "texto integral" do d-G, manter e registrar.

## PONTOS PARA A EXEC (sem achado contra o produtor)

P1 — Aderência "parcial" dos itens 70 a 76: vem da ESPEC da EXEC. Nem a Parte D nem o P9 qualificam esses itens como "parcial"; no P9, "aderência parcial" aparece só para o item 63. O produtor seguiu a ESPEC e registrou a dúvida. O mesmo vale para o rótulo "(aderência parcial ao 4.1)" no título da seção de itens reais do curso.md e para "aderência parcial" na observacao dos 7 itens. A EXEC deve confirmar.
P2 — Par 20 ("suprimida pela Lei 13.853/2019"): a errata E3 não lista esse ponto, então manter o texto é fiel. Harmonizar com o curso ("MP nº 869/2018, convertida na Lei 13.853/2019") exige errata da GCE e está fora do escopo da extração.
P3 — 13 justificativas AUTORAL (Q17–Q25 e Q27–Q30) começam com "[NORMATIVO — QA: <dispositivo>]". Essa marca não está na lista da regra 6 e carrega a base legal, útil ao estudante. Por isso não registrei achado. Se a EXEC estender a regra a essa marca, a aplicação deve ser uniforme em todos os lotes.
P4 — itensEdital das discursivas: a fonte não os mapeia. A inferência do produtor é coerente com o conteúdo das alíneas e dos tópicos e pode ser mantida: questão P2-3.2, 3.3, 4.1 e 4.2; peça P2-4.1 e 4.3.
P5 — "Falsa pegadinha:" no início das justificativas de Q04, Q08, Q12 e Q16 (e após a marca normativa em Q19 e Q25) é texto didático do d-G, não metadado. Nada a fazer.

## RESUMO

O: 2 (O-1 pegadinha 26 incompleta; O-2 marca [V] indevida em F3).
R: 6 (R-1 a R-6).
Enunciados: 30/30 AUTORAL idênticos ao (d); 7/7 reais idênticos ao caderno oficial. Gabaritos: 37/37 corretos. Erratas E1–E3 aplicadas em todos os pontos indicados. Somas das discursivas conferidas.

FIM DO PARECER


========== L4 ==========
PARECER DE QA — EXEC-01 — L4 — RODADA 1 — Opus — 12/10/2026

QA independente (não produziu os fragmentos). Fragmentos não editados.
Padrão: /home/claude/exec01/ESPEC_EXEC01.md e ESPEC_QA_EXEC01.md.
Fontes canônicas lidas por project_read: GCB/Lote4_v3_canonica_GCB-CPP.md (v3.3), claude/GBQ_Registro_AUTORAL_v2.md; GCE_ItensReais_P9_GCE.md (por project_search) para o item 81 do TRF6.
Arquivos conferidos: itens.json, meta.json, curso.md, resumo.md, pares.json, pegadinhas.json, discursivas.json, relatorio.md.

CONCLUSÃO: APROVADO COM RESSALVAS
Nenhum achado O. Seis achados R (forma), nenhum altera enunciado, gabarito, comando, valor ou errata.

## 1. itens.json
- Enunciados: os 20 conferidos palavra a palavra (comparação por python3 com transcrição da seção (d) da fonte): 20/20 idênticos, inclusive pontuação.
- Comandos: os 4 comandos de bloco conferem com a fonte ("Acerca da engenharia de prompts, julgue os itens de 1 a 6." etc.).
- gabarito, itemEdital, ts, volatil: conferem com o d-G e com o registro GBQ v2 em todos os 20 IDs. Contagens: 10 C / 10 E; [TS] = 10 (5 C, 5 E); VOLÁTIL = 1 (L4-15); 5.1 = 6, 5.2 = 5, 5.3 = 5, 6 = 4.
- rotulo = AUTORAL e aderencia = direta em todos: correto.
- observacao: L4-15 "VOLÁTIL — reverificar entre 4 e 8/1/2027" correto; L4-11 traz a regra R2 da GBQ (aceitável; ver R-1); demais vazias, correto (nenhum item REVERIFICAR nem errata própria).
- justificativa: texto do d-G de cada item, integral, após o cabeçalho de metadados; conferido item a item. Nenhuma justificativa começa por gabarito, [TS], VOLÁTIL, subitem ou "convertido" (regra 6 cumprida). Os rótulos de status "v3 (R9)", "v3 (O10)", "v3 (O11)", "v3.1" foram retirados do início; restam marcas de status no fim/meio de três justificativas (ver R-2).
- Itens reais: não há neste lote.

## 2. Contagens e IDs
L4-01 a L4-20, sem duplicata nem falta. JSON válidos (todos os arquivos carregados por python3).

## 3. curso.md e resumo.md
- Fidelidade: comparação integral (não só amostra) de 5.1.1–5.1.6, 5.2.1–5.2.7, 5.3.1–5.3.6, 6.1–6.5 e do resumo (b) contra a fonte. Texto idêntico, salvo marcação Markdown e as retiradas listadas abaixo. Amostras com conferência literal registrada: 5.1.1 (definição F3 e fine-tuning), 5.1.4 (temperatura, alucinação, injeção), 5.1.6 P1–P7; 5.2.3 (distinção clustering × classificação, redação O12), 5.2.5 (redação O10 e item 81), 5.2.7 P6; 5.3.1 (distinção O11), 5.3.3 (fundação × LLM, redação O1; modalidades O8), 5.3.6 P8; 6.1 (Decreto 1.171, Seção I, II), 6.3 (art. 5º, VIII e XIX pela Lei 15.352/2026; art. 12; art. 20 com redação O9; Decreto XV, "l"; Lei 8.112, art. 117, IX e XVI; N10), 6.5 P1–P3.
- Erratas/correções da Tabela (O1–O12, R8, R9, NOTA 8.11.2 com "ou houver marcação dupla (C e E)", L1, ANPD, itens 18–20, Conferência A CONFIRMAR, Fechamento 1b/1g): todas presentes em todos os pontos indicados (curso, resumo, pares, d-G).
- Conteúdo novo: nenhum, salvo a troca de palavras apontada em R-3.
- Omissões: só de anotações internas a unidades; uma substituição e algumas retiradas não declaradas no relatório (R-3, R-4); uma anotação interna remanescente no resumo (R-6).

## 4. pares.json e pegadinhas.json
- pares: 20 (C1–C20), separados em a/b/como sem reescrita; "como" literal. Qualificadores normativos ligados a um só termo em C16 e C18 de modo que desloca a referência (R-5).
- pegadinhas: 32 (5.1 = 7; 5.2 = 7; 5.3 = 8; 6 = 10), literais, no formato "afirmação → ERRADO (motivo)", itemEdital correto.

## 5. discursivas.json
[] — correto (P1 não tem discursiva; edital 9.1).

## 6. Regra de forma (prefixo de metadados na justificativa)
Nenhum prefixo de metadados. Sem achado. (As justificativas começam pelo código de mecanismo — TC, GI, AT, IC — ou por "sem armadilha (ancoragem)"; isso não está na lista da regra 6.)

## ACHADOS

### O (obrigatórios)
Nenhum.

### R (recomendados)

R-1 — Item 81 do TRF6 2024 "a confirmar contra o GAB_DEFINITIVO" (ponto específico da ordem).
Local: L4/itens.json, L4-11 (justificativa e observacao); L4/curso.md, 5.2.5 (linha 132) e 5.3.6 P2 (linha 198); L4/pegadinhas.json, 2º registro de P1-5.3; L4/relatorio.md, "Dúvidas".
Fato: o gabarito definitivo do item 81 (TRF6 2024, Cargo 2, caderno 034_TRF6_002_01) é E, não anulado, já conferido no GAB_DEFINITIVO (GCE_ItensReais_P9_GCE.md, Parte B: "81 | E"; GCE_BIP_retorno_v2.md: "item 81 = E no GAB definitivo, não anulado"). O texto "a confirmar" é conteúdo canônico da GCB (v3.3, Tabela O6) e a retirada da marca cabe à GCB, não à EXEC.
Correção: manter o texto da justificativa, do curso e da pegadinha como está (não alterar o canônico). Substituir a observacao do L4-11 por:
"R2: nunca no mesmo simulado que o item real TRF6 2024, Cargo 2, nº 81. Item 81: gabarito definitivo E, já conferido no GAB_DEFINITIVO (GCE_ItensReais_P9_GCE.md, Parte B; não anulado); o texto canônico da GCB (v3.3, O6) ainda traz \"a confirmar\"."
E acrescentar ao relatorio.md, em "Dúvidas": "Item 81 do TRF6 2024: gabarito definitivo E conferido (GCE_ItensReais_P9_GCE.md); o texto \"a confirmar\" foi mantido por ser canônico da GCB e anotado na observacao do L4-11."

R-2 — Marcas de status da Tabela de Correções dentro de justificativas exibidas ao estudante.
Local: L4/itens.json, L4-08, L4-09 (sufixo " (v3 — O12)") e L4-13 (" (O1)").
Motivo: são rótulos internos do mesmo tipo dos retirados do início das justificativas dos itens 5, 11, 12 e 18–20 (relatório, "Campos vazios"); a regra 6 visa justamente impedir que metadados apareçam ao estudante. Tratamento hoje inconsistente.
Correção exata:
- L4-08: fim da justificativa "Fonte: F4, verificado em 7/10/2026. (v3 — O12)" → "Fonte: F4, verificado em 7/10/2026."
- L4-09: idem, "Fonte: F4, verificado em 7/10/2026. (v3 — O12)" → "Fonte: F4, verificado em 7/10/2026."
- L4-13: "o F3 define os termos separadamente (O1). Fonte:" → "o F3 define os termos separadamente. Fonte:"
Se a EXEC preferir manter a justificativa literal, registrar a escolha no relatorio.md e manter os três como estão.

R-3 — Substituição de palavras na lista de fontes normativas do curso.
Local: L4/curso.md, linha 28.
Fonte: "N10 — Ato da Mesa nº 225/2025 (Câmara dos Deputados; norma interna; referência sem item)". Fragmento: "(...; norma interna; referência de contexto)". A omissão de "referência sem item" é admissível (anotação de banco); a troca por outra expressão não é.
Correção: "- N10 — Ato da Mesa nº 225/2025 (Câmara dos Deputados; norma interna)".

R-4 — Retiradas não declaradas e tratamento desigual de "sem item".
Local: L4/curso.md e L4/relatorio.md.
Retiradas feitas e não listadas no relatório (todas admissíveis, por serem anotações internas): "R8 — " (escopo); "arquivo \"Edital - Camara 2026.pdf\" do Projeto" (escopo); "para o QA Normativo" (títulos de FONTES NORMATIVAS e de 6.3); "GCB; " (regra de legislação); "; não usada em item" (N3 na lista); "(GCB-CPP)" (título de 6.2); " e não entra em item" (6.3, Contexto VOLÁTIL); "; sem item" (6.3, EBIA). Em sentido contrário, o "; sem item" foi mantido em 6.3, art. 5º, XIX (linha 237).
Correção: (a) linha 237: "a redação anterior não foi conferida, e nada se afirma sobre o que mudou; sem item)." → "a redação anterior não foi conferida, e nada se afirma sobre o que mudou)."; (b) acrescentar ao relatorio.md, em "Retirado do curso", a lista acima.

R-5 — Qualificador normativo ligado a um só termo em C16 e C18.
Local: L4/pares.json, C16 e C18.
Motivo: na fonte, o qualificador é do par. Em C16 o "Decreto 1.171, Seção I, II" fundamenta sobretudo o lado ético (honesto × desonesto) e foi ligado a "Legal"; em C18 o XV, "e" é a vedação de omitir tecnologia e foi ligado a "Usar IA". Não chega a mudar o sentido, mas desloca a referência.
Correção exata (mesma solução já usada em C15, qualificador nos dois termos):
- C16: "a": "Legal (Decreto 1.171, Seção I, II): conforme a lei"; "b": "Ético (Decreto 1.171, Seção I, II): conforme a honestidade e o interesse público, além da lei".
- C18: "a": "Usar IA (Decreto 1.171, XV, \"e\"): permitido e esperado, em canais autorizados"; "b": "Omitir tecnologia (Decreto 1.171, XV, \"e\"): vedado deixar de usar avanços técnicos".

R-6 — Anotação interna remanescente no resumo.
Local: L4/resumo.md, NOTA DO EDITAL (8.11.2), última frase.
Motivo: "Só o fato e a fonte." é marca de cumprimento da instrução da GCB (Tabela: "só fato e fonte"), não conteúdo para o estudante; mesmo critério usado para retirar notas internas do curso.
Correção: "(Edital nº 1/2026, subitem 8.11.2). Só o fato e a fonte." → "(Edital nº 1/2026, subitem 8.11.2)."

## Observações sem achado
- curso.md põe o escopo e as listas F1–F5 e N1–N10 no início: escolha de forma declarada, sem perda de texto.
- As justificativas mantêm anotações de proveniência ("conferido pela CQFP...", "Aprovado pela CQFP", "Risco MÉDIO; mantido como está") — texto integral do d-G, conforme a ESPEC.
- meta.json correto (id, nome, itensEdital, arquivos).

FIM DO PARECER


========== L4C ==========
PARECER DE QA — EXEC-01 — L4C — RODADA 1 — Opus — 12/10/2026

QA independente (não produziu os fragmentos). Fragmentos não editados.
Padrão: /home/claude/exec01/ESPEC_EXEC01.md e ESPEC_QA_EXEC01.md.
Fontes canônicas lidas por project_read: GCB/Lote4C_v1_GCB-CPP.md (v1.1, com a Retificação 6-A), claude/GBQ_Registro_AUTORAL_v2.md; GCB/Lote4_v3_canonica_GCB-CPP.md (v3.3) para as remissões ao curso.
Arquivos conferidos: itens.json, meta.json, curso.md, resumo.md, pares.json, pegadinhas.json, discursivas.json, relatorio.md.

CONCLUSÃO: APROVADO COM RESSALVAS
Nenhum achado O. Um achado R (forma), submetido à decisão da EXEC.

## 1. itens.json
- Enunciados: os 10 conferidos palavra a palavra (comparação por python3 com transcrição da seção (d) da fonte v1.1): 10/10 idênticos. Correções aplicadas: O-4C1 (4C-06, item de zero-shot) e R-4C1 + Retificação 6-A (4C-09, "sem acesso a ferramentas externas (como a busca) ou a RAG e sem retreinamento").
- Comando: "Acerca da engenharia de prompts, julgue os itens de 4C-01 a 4C-10." — literal da fonte.
- gabarito, itemEdital, ts, volatil: conferem com o d-G e com o registro GBQ v2 nos 10 IDs. Contagens: 5 C (02, 03, 06, 07, 09) / 5 E (01, 04, 05, 08, 10); [TS] = 5 (01, 03, 04, 06, 08 — 2 C e 3 E); VOLÁTIL = 0; P1-5.1 = 10.
- rotulo = AUTORAL e aderencia = direta: correto.
- observacao = "" em todos: correto (sem VOLÁTIL, REVERIFICAR ou errata própria; R2 não se aplica).
- justificativa: texto integral do d-G após o cabeçalho "4C-nn. G — marcas — 5.1 —", conferido item a item, sem perda nem acréscimo.

## 2. Contagens e IDs
4C-01 a 4C-10, sem duplicata nem falta; sem colisão com L4-01..L4-20. JSON válidos.

## 3. curso.md e resumo.md
Vazios por desenho: a fonte do Lote 4-C não tem seções (a), (b) nem (c); a BASE é o curso, o resumo e os pares do Lote 4. Ausência registrada no relatorio.md, como manda a ESPEC. Sem achado.
Remissões das justificativas ao curso do Lote 4 (5.1.1, 5.1.2 itens 3–6, 5.1.3, 5.1.4, 5.1.5, 5.1.6 P5, 5.3.3, 5.3.5, 6.2 princípio 7): conferidas contra o L4/curso.md; todas encontram o texto citado.

## 4. pares.json e pegadinhas.json
[] — correto (fonte sem pares e sem pegadinhas próprios).

## 5. discursivas.json
[] — correto (P1 sem discursiva; edital 9.1).

## 6. Regra de forma (prefixo de metadados na justificativa)
Nenhum prefixo de metadados (as justificativas começam pelo código de mecanismo ou por "sem armadilha (ancoragem"). Sem achado.

## ACHADOS

### O (obrigatórios)
Nenhum.

### R (recomendados)

R-1 — Referências internas de QA dentro de justificativas exibidas ao estudante (decisão da EXEC).
Local: L4C/itens.json, 4C-06, 4C-08, 4C-09.
Motivo: a ESPEC manda texto integral do d-G, e o produtor o seguiu; mas três justificativas trazem rótulos de tramitação que não servem ao estudante e são do mesmo tipo que a regra 6 quer fora da justificativa: "conforme o parecer da rodada 1" (4C-06), "Lição O10:" (4C-08), "R-4C1" e a frase da "Retificação 6-A" (4C-09).
Correção, se a EXEC estender a regra 6 a esses rótulos (do contrário, manter e registrar no relatorio.md):
- 4C-06: ", conferido pela CQFP em 07/10/2026, conforme o parecer da rodada 1)" → ", conferido pela CQFP em 07/10/2026)".
- 4C-08: "Lição O10: o item não depende" → "O item não depende".
- 4C-09: "sem armadilha (ancoragem; R-4C1)." → "sem armadilha (ancoragem)."; e excluir a frase "Retificação 6-A: a redação \"sem acesso a busca\" não excluía outras ferramentas; \"ferramentas externas (como a busca)\" alinha o item ao curso 5.3.3 (\"sem ferramentas ou RAG\")." (o restante da justificativa já explica a ressalva).

## Observações sem achado
- As justificativas remetem a "item n do Lote 4"; na plataforma os IDs são L4-nn. A correspondência é direta (item n = L4-0n/L4-nn) e não exige alteração.
- meta.json correto (id, nome, itensEdital ["P1-5.1"], arquivos).

FIM DO PARECER


========== L5 ==========
PARECER DE QA — EXEC-01 — L5 — RODADA 1 — Opus — 12/10/2026

QA independente (não produziu os fragmentos). Fragmentos não editados.
Padrão: /home/claude/exec01/ESPEC_EXEC01.md e ESPEC_QA_EXEC01.md.
Fontes conferidas (Projects, project_read em 12/10/2026): GCB/Lote5_v3_canonica_GCB-CPP.md (v3.1); claude/GBQ_Registro_AUTORAL_v2.md. Lidos também: L5/relatorio.md e scripts/gen_l5.py.

## CONCLUSÃO: APROVADO COM RESSALVAS

Nenhum achado O. Três achados R (forma). Itens, gabaritos, [TS], VOLÁTIL, subitens e correções da v3.1 estão corretos. O curso tem duas pequenas alterações de redação no 8.3 (R-1 e R-2), e há um prefixo de escopo em duas pegadinhas (R-3).

## Método
- Comparação feita com python3, caractere a caractere, entre o texto da fonte e: (i) os 20 enunciados; (ii) as 20 justificativas, verificando se a justificativa é o d-G sem o prefixo; (iii) o curso.md normalizado (retirados "### " e as linhas em branco) contra a seção (a) inteira; (iv) o bloco "Fontes de ferramenta" contra o bloco FONTES DE FERRAMENTA do cabeçalho da fonte.
- resumo.md, pares.json e pegadinhas.json: conferidos entrada por entrada contra (b), (c) e as linhas de "Pegadinha" do curso.
- Contagens e metadados: conferidos por script contra o registro da GBQ v2.

## 1. itens.json
- 20 itens (A5-01 a A5-20), sem ID duplicado nem faltante. Numeração de 1 a 20.
- Enunciados: os 20 são idênticos à versão (d) da v3.1, já com F3 b (A5-02) e F4 (A5-09). 0 divergências.
- Gabarito, itemEdital e [TS] por ID: 0 divergências com a GBQ v2 e o d-G. Totais: 10 C / 10 E; 10 [TS]; 4 VOLÁTEIS (A5-14 a A5-17). Por subitem: 7.1 = 4, 8.1 = 3, 8.2 = 6, 8.3 = 4, 8.4 = 3. Os IDs de itemEdital existem em frag/edital.json.
- rotulo "AUTORAL" e aderencia "direta" nos 20 itens.
- comando: os 5 comandos são idênticos aos da fonte. textoBase "" (a fonte não tem texto-base).
- observacao: "VOLÁTIL — reverificar entre 4 e 8/1/2027" em A5-14 a A5-17, conforme o d-G; A5-02 e A5-09 registram F3 b e F4. Não há REVERIFICAR normativo no lote.
- justificativa: em todos os itens, o texto é o d-G literal depois de retirado o prefixo ("C — [TS] — v3 (F3 b) — 7.1 — ", "E — novo — 8.2 — " etc.). Nenhuma palavra foi alterada no comentário.
- Regra de forma 6 (prefixo de metadados): nenhuma justificativa começa por gabarito, [TS], VOLÁTIL, subitem ou "convertido". Conforme. As justificativas começam pelo mecanismo (TC, GI, AT, IC) ou direto pelo comentário. O mecanismo não está na lista de metadados da regra.

## 2. Contagens e IDs
Conformes. Os números do relatorio.md (20 itens; 15 pares; 52 pegadinhas: 7.1 = 15, 8.1 = 5, 8.2 = 17, 8.3 = 10, 8.4 = 5) foram reconferidos por script.

## 3. curso.md e resumo.md
- Fidelidade: o diff contra a seção (a) mostra só estas diferenças:
  (a) 8.3, definição: retirados "pela CQFP" e "; o recurso não é objeto de item". Aceitável: a primeira é referência a unidade, e a data [V] foi mantida; a segunda é instrução interna.
  (b) 8.3, Power BI e Tableau: "PENDENTE (não afirmar)" passou a "PENDENTE (não afirmado)" e saiu "(o silêncio da fonte não é base para item)". A retirada da nota é aceitável (instrução interna). A troca de "afirmar" por "afirmado" não é → R-1.
  (c) 8.3: acréscimo do bloco "Fontes de ferramenta" (ver abaixo) → R-2 para uma linha dele.
  Todo o resto da seção (a) (7.1.1 a 8.4) é idêntico ao texto da fonte. A amostragem exigida (no mínimo 3 trechos por subitem) fica coberta com folga.
- Bloco "Fontes de ferramenta" (verificação pedida). As linhas U1, U2, U3, TB2, U4, U5, U6 e GG4 são cópia exata, com URLs, do bloco FONTES DE FERRAMENTA do cabeçalho da fonte. Alterações encontradas:
  - no título, retirados "pela CQFP" e "U1 en-us, GG4 e TB2 reabertas pela CPP em 8/10/2026";
  - na linha CI, retirados "pela CQFP" e "; F1";
  - a linha "PENDENTES (não afirmados)" foi omitida (o conteúdo já está nas linhas PENDENTE do curso);
  - na linha VOLÁTIL, retirados "A5-14 a A5-17" e "pela CQFP (FV)".
  Não há conteúdo novo: é texto da fonte, mudado de lugar e enxugado. Ficar fora da seção (a) é decisão de forma, documentada no relatorio.md, e é útil, porque o curso cita U1 a U6, TB2, GG4 e CI e sem a lista o estudante não chegaria às fontes. A EXEC deve ratificá-la. A única ressalva é o corte dos IDs na linha VOLÁTIL (R-2).
- Erratas e correções em TODOS os pontos indicados: F1 (definição da categoria, menção VOLÁTIL ao CI, pegadinha do Data Studio, exemplo aplicado e resumo 8.3), F2 (exemplo aplicado), F3 a (7.1.4, resumo 7.1, par C6), F4 (curso 8.2, par C1), R1 ("download gratuito" no par C13 e no resumo 8.3), NOTA 8.11.2 com "ou houver marcação dupla (C e E)" (v3.1). Todas aplicadas.
- resumo.md: idêntico à seção (b). A única mudança é de marcação: o rótulo de cada subitem virou título "### ", e saiu o "(b)" do título.

## 4. pares.json e pegadinhas.json (verificação pedida sobre os prefixos)
- pares.json: 15 pares (C1 a C15), na ordem da fonte. Os campos a/b/como são o texto da fonte, palavra por palavra. O prefixo de cada lado vem do título do par ("Histograma × gráfico de barras" → "Histograma:" / "Gráfico de barras:"). Em C5, "Atributo × métrica (dimensão × medida)" foi redistribuído como "Atributo (dimensão)" / "Métrica (medida)". Em C9, "Paleta" foi distribuído aos três termos. Em C9 e C11 o 3º termo foi anexado a "b" com " | ". Conclusão: só rearranjo do texto da fonte, sem conteúdo novo e sem mudança de sentido.
- pegadinhas.json: 52 entradas, cada uma correspondendo a um segmento separado por ";" na fonte. Nenhuma pegadinha faltante ou acrescentada. O "motivo" entre parênteses só aparece onde a fonte o traz. Prefixos ("Histograma:", "Gráfico de linha:", "Power BI:", "Tableau:", "Data Studio:" etc.) vêm do título da subseção. Nos 3 últimos itens de box plot e em "Gráfico de linha: … → ERRADO (sugere continuidade inexistente)" houve só resolução de elipse e reposição do motivo da fonte. Conclusão: rearranjo do texto da fonte, sem conteúdo novo. Ressalva única em R-3.

## 5. discursivas.json
[] — correto (a P1 não tem discursiva).

## 6. meta.json
Conforme: id, nome, os 5 itensEdital e os arquivos de origem.

## ACHADOS

O — nenhum.

R-1 (curso.md, linhas 83 e 89; relatorio.md, "Decisões de forma"). A fonte diz "PENDENTE (não afirmar)" nas subseções Power BI e Tableau. O fragmento troca por "PENDENTE (não afirmado)", forma que aparece só no cabeçalho da fonte ("PENDENTES (não afirmados)"). O relatório afirma que "PENDENTE (não afirmado)" foi "mantido", o que não confere. Não muda o sentido, mas é troca de palavra dentro da seção (a).
Correção exata:
- linha 83: "- PENDENTE (não afirmar): DAX, Report Server, versões, licenças, preços, limites, execução em macOS."
- linha 89: "- PENDENTE (não afirmar): versões e preços."
- relatorio.md: no lugar de '"PENDENTE (não afirmado)" mantido.', escrever '"PENDENTE (não afirmar)" mantido.'

R-2 (curso.md, linha 112, bloco "Fontes de ferramenta"). A linha VOLÁTIL corta a delimitação dos itens que a fonte traz ("itens A5-14 a A5-17"), e "itens" fica indeterminado.
Correção exata: "- VOLÁTIL: todo o 8.3 (curso, resumo, pares e itens A5-14 a A5-17); reverificação entre 4 e 8/1/2027."

R-3 (pegadinhas.json, entradas 8.3 nas linhas 184 e 188). O prefixo "Data Studio:" foi aplicado às duas últimas pegadinhas do 8.3, que são de categoria: a de F1 vale para qualquer ferramenta, como diz a "Definição precisa (categoria)", e a do Excel/Office é delimitação de escopo do lote. Na fonte elas estão na linha de pegadinhas da subseção Data Studio, mas o prefixo explícito restringe o alcance aparente da regra de F1 a um só produto.
Correção exata (retirar o prefixo, mantendo o texto da fonte):
- "atribuir à ferramenta a responsabilidade pela adequação do gráfico → ERRADO (a ferramenta pode sugerir ou gerar visuais, mas a adequação ao dado e à pergunta é do analista)"
- "misturar com Excel/Office → ERRADO (item 1 do edital, MSOffice 365, fora do escopo deste lote)"

## NOTAS À EXEC (não são achados; matéria de decisão de forma da EXEC)
- N1. Os pares não têm ID no esquema {a,b,como}. A justificativa de A5-09 cita "par C1", e as do L5C citam "par C1"/"par C14". A correspondência só existe pela ordem do array (índice n = Cn). Se a EXEC quiser, pode acrescentar um campo "id" ao esquema.
- N2. Algumas justificativas têm notas de produção visíveis ao estudante ("Risco BAIXO/MÉDIO", códigos de fonte U1 a U6 e GG4) e usam as siglas de mecanismo (TC, GI, AT, IC) sem legenda. Estão fiéis ao d-G, como a ESPEC exige. Cabe à EXEC decidir se a plataforma mostra a legenda do d-G.
- N3. Ficaram mantidos, por estarem no texto canônico: "Só o fato e a fonte." (NOTA 8.11.2 do resumo) e "fora do escopo deste lote" (pegadinha 8.3). Têm cara de nota editorial interna. A ESPEC não obriga retirar.
- N4. Os comandos contêm faixa de IDs ("julgue os itens A5-01 a A5-04."), fiel à fonte. Em simulado com itens embaralhados, a faixa deixa de corresponder.

FIM DO PARECER


========== L5C ==========
PARECER DE QA — EXEC-01 — L5C — RODADA 1 — Opus — 12/10/2026

QA independente (não produziu os fragmentos). Fragmentos não editados.
Padrão: /home/claude/exec01/ESPEC_EXEC01.md e ESPEC_QA_EXEC01.md.
Fontes conferidas (Projects, project_read em 12/10/2026): GCB/Lote5C_v1_GCB-CPP.md (v1.1); claude/GBQ_Registro_AUTORAL_v2.md; e, para as referências ao curso, GCB/Lote5_v3_canonica_GCB-CPP.md (v3.1). Lidos também: L5C/relatorio.md e scripts/gen_l5.py.

## CONCLUSÃO: APROVADO

Sem achados O nem R.

## Método
Comparação feita com python3, caractere a caractere, entre a fonte e: os 10 enunciados (d) e as 10 justificativas (d-G sem o prefixo). Metadados e contagens conferidos por script contra o registro da GBQ v2.

## 1. itens.json
- 10 itens (5C-01 a 5C-10), sem ID duplicado nem faltante. Numeração de 1 a 10.
- Enunciados: os 10 são idênticos à versão (d) da v1.1. 5C-03 está na redação de R-5C1, sem "lado a lado". 0 divergências.
- Gabarito, itemEdital (P1-8.2 = 6; P1-8.4 = 4) e [TS] (01, 03, 06, 07, 08): 0 divergências com a GBQ v2 e o d-G. Totais: 5 C / 5 E; 5 [TS]; 0 VOLÁTIL.
- rotulo "AUTORAL" e aderencia "direta" nos 10 itens. comando: os 2 comandos são idênticos aos da fonte. textoBase "".
- observacao: "texto conforme R-5C1 (v1.1)" em 5C-03, "" nos demais. Conforme.
- justificativa: em todos os itens, o texto é o d-G literal sem o prefixo ("C — [TS] — 8.2 — " etc.). Nenhuma palavra foi alterada.
- Regra de forma 6 (prefixo de metadados): nenhuma justificativa começa com metadado. Conforme.
- As referências ao curso nas justificativas ("Curso 8.2, …", "Curso 8.4, …", "resumo 8.1: título afirmativo", "par C14") foram conferidas contra a v3.1 do Lote 5 e existem lá com o teor citado.

## 2. Contagens e IDs
Conformes e iguais ao relatorio.md.

## 3. curso.md e resumo.md
Vazios (0 bytes). A fonte não tem seções (a) e (b): o 5-C usa o curso e o resumo 8.2/8.4 do Lote 5. Está conforme a ESPEC ("se um campo não existir na fonte, deixe vazio") e registrado no relatório. Não há erratas de curso a aplicar.

## 4. pares.json e pegadinhas.json
[] e [] — corretos. A fonte não tem (c) nem "PEGADINHAS PROVÁVEIS". Os pares citados (C1 a C3, C14, C15) estão em L5/pares.json.

## 5. discursivas.json
[] — correto (a P1 não tem discursiva).

## 6. meta.json
Conforme.

## ACHADOS
O — nenhum.
R — nenhum.

## NOTAS À EXEC (não são achados)
- N1. Algumas justificativas têm notas de produção visíveis ao estudante: em 5C-03, "(redação da v1.1, R-5C1: …)"; em 5C-06, "Lição O10" e "Sem atribuição a autor."; em 5C-08, "É o item deste lote mais próximo de um canônico (A5-20) …". Também citam IDs de outros itens (A5-xx). Estão fiéis ao d-G, como a ESPEC exige. Se a plataforma mostra a justificativa ao estudante, cabe à EXEC decidir se esses trechos devem ser filtrados (decisão de forma, não da produção).
- N2. "par C1"/"par C14" só se resolvem pela ordem de L5/pares.json, porque o esquema não tem ID de par (ver N1 do parecer L5).

FIM DO PARECER


========== CONFERÊNCIA FINAL ==========
CONFERÊNCIA DE APLICAÇÃO E CONFERÊNCIA FINAL — EXEC-01 — pacote_v1_auto.json — QA independente (Opus) — 12/10/2026

Natureza: conferência de aplicação dos pareceres da rodada 1 e conferência final do pacote. Não é rodada 2. O QA não editou fragmentos nem o pacote.
Objetos conferidos: /home/claude/exec01/frag/<LOTE>/ (L1, L1C, L2, L3, L4, L4C, L5, L5C), com parecer_QA_R1.md e relatorio.md de cada pasta; /home/claude/exec01/out/pacote_v1_auto.json; /home/claude/exec01/out/stats.json; /home/claude/exec01/scripts/montar.py.
Fontes canônicas lidas pela ferramenta Projects (project_read/project_search) em 12/10/2026: claude/GBQ_Registro_AUTORAL_v2.md; GCE_Lote1_v2_CPP.md; GCE_Lote2_v2_CPP.md; GCB/Lote4_v3_canonica_GCB-CPP.md (v3.3); GCB/Lote5_v3_canonica_GCB-CPP.md (v3.1, trecho da Parte 3/3).
Decisões de forma da EXEC tratadas como não achados: prefixos de metadados retirados; referências internas do d-G mantidas (PRÓXIMO, edição do estudante); marca [NORMATIVO — QA] mantida; itensEdital das discursivas inferido, com observacao; aderência "parcial" dos itens 70–76 (base GCE_BIP_retorno_v2.md); L4C R-1 não aplicada; comandos com faixa de IDs normalizados, com o original em "comandoOriginal".

## CONCLUSÃO: CONFERIDO

Todos os achados O e R da rodada 1 estão aplicados no fragmento e no pacote ou estão cobertos por decisão da EXEC. Contagens, gabaritos (150/150), VOLÁTEIS, REVERIFICAR, regras do carregador do Protótipo 0 e amostra de fidelidade (10/10) conferem. Não há pendência. As observações da seção 5 não bloqueiam e não exigem correção.

## 0. Integridade do pacote em relação aos fragmentos

- montar.py foi executado em cópia, com saída redirecionada ao diretório de rascunho do QA. O pacote e o stats.json gerados são byte a byte idênticos aos entregues em /home/claude/exec01/out/ (cmp sem diferença). Conclusão: o pacote reflete exatamente o estado atual dos fragmentos. Toda correção conferida no fragmento está também no pacote, salvo a normalização de comandos, que só ocorre na montagem e é conferida no ponto 3.
- A validação interna do montar.py ("erros") retornou lista vazia: nenhum ID duplicado, nenhum campo obrigatório vazio, gabaritos em C/E, todo itemEdital presente no edital e aderência em {direta, parcial}.
- Carimbos de hora: o último fragmento foi alterado às 18:15:17 e o pacote foi gerado às 18:15:53 de 12/10/2026, depois de todas as correções.

## 1. Conferência de aplicação dos achados da rodada 1

Método: script python3 -I sobre o fragmento e o pacote. O texto exigido é o texto substitutivo do parecer, extraído do próprio parecer por expressão regular no caso das listas de justificativas.

### L1 (parecer: APROVADO COM RESSALVAS; O-1, R-1 a R-5)
- O-1 — CONFERE. Local: L1/pegadinhas.json e pacote lotes[L1].pegadinhas, 5ª entrada de P2-1.3 (índice 13, 14ª do arquivo; o parecer a chamou de "13ª", erro de contagem sem efeito). O texto é idêntico ao substitutivo: "Tratar nomes e versões de modelos como estáveis → ERRADO (...)". A frase "A prova cobra o nome/versão do modelo" não existe mais. Total: 31.
- R-1 — CONFERE. Local: itens L1-Q01 a L1-Q20, campo justificativa. São 20/20 idênticas ao texto do parecer, no fragmento e no pacote.
- R-2 — CONFERE. Local: observacao de L1-Q14, Q16, Q18 e Q19 = "VOLÁTIL (verificado em 07/10/2026) — reverificar entre 4 e 8/1/2027".
- R-3 — CONFERE. Local: DISC-L1-Q.aspectosValorados[0..2].aspecto, com os 3 rótulos do parecer. Valores 5,00 / 4,00 / 5,30 inalterados.
- R-4 — CONFERE por decisão da EXEC. itensEdital ["P2-1.4","P2-1.6","P2-1.7"] foi mantido, com observacao "itensEdital inferido pela EXEC a partir das alíneas; confirmação pela GCE".
- R-5 — CONFERE (sem efeito). A O-1 foi aplicada por substituição, e as pegadinhas continuam 31.

### L1C (parecer: APROVADO COM RESSALVAS; R-1 a R-4)
- R-1 — CONFERE. Local: L1C-Q21 a L1C-Q30, justificativa. São 10/10 idênticas ao texto do parecer.
- R-2 — CONFERE. Local: L1C-Q24, justificativa. A E4 está em colchete próprio: "[V 08/10/2026 — arXiv 2006.11477] [verificado pela GCE-CQFP (QAP) em 08/10/2026 — arxiv.org/pdf/2006.11477, seção 2]."
- R-3 — CONFERE. Local: L1C-Q28.observacao = "".
- R-4 — CONFERE. Local: L1C/pegadinhas.json e pacote lotes[L1C].pegadinhas. As 4 entradas são idênticas ao texto do parecer: sem aspas externas e com aspas duplas internas.

### L2 (parecer: APROVADO COM RESSALVAS; R-1 a R-9)
- R-1 — CONFERE. O resumo.md está inalterado: "Convenção exata da Câmara: NÃO VERIFICADA." continua presente. O meta.json e lotes[L2].observacao no pacote trazem o texto do parecer, idêntico e integral.
- R-2 — CONFERE. Local: curso 2.5, pegadinha (6): "e apenas recomenda para os demais.". A forma com "o" não aparece mais.
- R-3 — CONFERE. Local: curso 2.1: ", por força do Ato da Mesa nº 251, de 16/03/2026, arts. 1º e 2º, I [V 08/10/2026 — Legin; F8; NORMATIVO — QA]."
- R-4 — CONFERE. A entrada "Cobrar recurso de produto específico" foi excluída. São 42 pegadinhas, com P2-2.6 = 5.
- R-5 — CONFERE. Não resta nenhum marcador "- N. " no curso. Há 11 itens de lista ordenada simples.
- R-6 — CONFERE. (a) Conceito 0 dos quesitos 2.2 e 2.3 da DISC-L2-Q = "Nenhum aspecto contabilizado."; (b) conceito 0 do quesito 2.3 da DISC-L2-P conforme o parecer; (c) a linha "Nota (edital, 9.8.5.1, d): NQ = NC − 3 × NE ÷ TL." saiu do padrao e está no fim do observacao da DISC-L2-P; (d) a nota sobre o conceito 0 está no observacao das duas entradas.
- R-7 — CONFERE. Local: DISC-L2-Q.aspectosValorados, com as alíneas a), b) e c) literais da seção (e). Valores 5,00 / 5,00 / 4,30.
- R-8 — CONFERE por decisão da EXEC. Os itensEdital foram mantidos, com observacao "itensEdital inferido pela EXEC a partir dos quesitos; confirmação pela GCE".
- R-9 — CONFERE. Local: L2/relatorio.md, com o texto "Q14 e Q21 trazem a nota de errata no campo observacao". O relatório não vai ao pacote.

### L3 (parecer: APROVADO COM RESSALVAS; O-1, O-2, R-1 a R-6; P1 a P5)
- O-1 — CONFERE. Local: pegadinhas, entrada nº 26 (índice 25, P2-4.1), com o texto idêntico ao substitutivo, que contém a segunda pegadinha ("a autoridade nacional é a Agência por definição"). Total: 42.
- O-2 — CONFERE. Local: curso, cabeçalho de fontes, bullet F3: "- F3 Lei 15.352/2026: as alterações foram lidas na própria LGPD compilada (F1), com a anotação". A marca "[V 08/10/2026 — F3]" não aparece mais no curso.
- R-1 — CONFERE. Local: curso 4.1: "Pseudonimizar NÃO é, por si, anonimizar." A expressão "por si só" não aparece mais.
- R-2 — CONFERE. Local: pares[16].b começa com "pseudonimização (art. 13, § 4º".
- R-3 — CONFERE. Local: pares[25] = {"a":"Confidencialidade, integridade, disponibilidade","b":"","como":""}. Total: 28.
- R-4 — CONFERE. Local: pegadinhas, entrada nº 20 (P2-3.4), com o motivo substitutivo do parecer.
- R-5 — CONFERE. Local: DISC-L3-P.baseNormativa[0] = "Lei 13.709/2018 (LGPD), art. 5º, I, VI, VII, X, XV e XVII".
- R-6 — CONFERE. Local: L3-Q21.justificativa termina em 'a "autoridade nacional" passou a ser exercida por ela.', sem o sufixo REVERIFICAR, que continua no campo observacao.
- P1 e P4 — CONFEREM com as decisões da EXEC. Itens 70–76: aderencia "parcial", com observacao iniciada por "aderência parcial conforme GCE_BIP_retorno_v2.md". DISC-L3-Q e DISC-L3-P: observacao "itensEdital inferido pela EXEC; confirmação pela GCE".
- P3 — A marca [NORMATIVO — QA] foi mantida, por decisão da EXEC. P2 (par 20) e P5 não pedem ação.

### L4 (parecer: APROVADO COM RESSALVAS; R-1 a R-6)
- R-1 — CONFERE. Local: L4-11.observacao, com o texto idêntico ao do parecer (item 81 = E, já conferido; "a confirmar" segue no texto canônico da GCB). Em "Dúvidas" do relatorio.md consta "Item 81 do TRF6 2024". A justificativa, o curso e a pegadinha foram mantidos, como mandou o parecer.
- R-2 — CONFERE. As justificativas de L4-08 e L4-09 terminam em "Fonte: F4, verificado em 7/10/2026.", sem "(v3 — O12)". A de L4-13 traz "separadamente. Fonte:", sem "(O1)".
- R-3 — CONFERE. Local: curso, lista de fontes normativas: "- N10 — Ato da Mesa nº 225/2025 (Câmara dos Deputados; norma interna)". Nota de conferência: a expressão "referência de contexto" que permanece no curso 6.3, parágrafo "Norma interna da Câmara (N10)", é literal da fonte v3.3 ("Norma interna; referência de contexto; sem item."). Só "; sem item" foi retirado ali, retirada já declarada no relatório. Sem achado.
- R-4 — CONFERE. Local: curso 6.3, art. 5º, XIX: "...e nada se afirma sobre o que mudou)." O "; sem item" foi retirado. As retiradas adicionais estão listadas no relatorio.md.
- R-5 — CONFERE. Local: pares C16 e C18, com o qualificador nos dois termos, nos textos exatos do parecer. O campo "como" ficou inalterado.
- R-6 — CONFERE. Local: resumo, NOTA DO EDITAL (8.11.2), que termina em "(Edital nº 1/2026, subitem 8.11.2)." sem "Só o fato e a fonte.".

### L4C (parecer: APROVADO COM RESSALVAS; R-1)
- R-1 — CONFERE com a decisão da EXEC de não aplicar. As justificativas de 4C-06, 4C-08 e 4C-09 mantêm o texto do d-G. A decisão e a classificação PRÓXIMO (edição do estudante) estão registradas no relatorio.md.

### L5 (parecer: APROVADO COM RESSALVAS; R-1 a R-3)
- R-1 — CONFERE. Local: curso 8.3, Power BI e Tableau: "- PENDENTE (não afirmar): DAX, Report Server, versões, licenças, preços, limites, execução em macOS." e "- PENDENTE (não afirmar): versões e preços.". A forma "não afirmado" não aparece mais no curso. O relatorio.md foi corrigido.
- R-2 — CONFERE. Local: curso, bloco "Fontes de ferramenta": "- VOLÁTIL: todo o 8.3 (curso, resumo, pares e itens A5-14 a A5-17); reverificação entre 4 e 8/1/2027."
- R-3 — CONFERE. As duas últimas pegadinhas do 8.3 estão sem o prefixo "Data Studio:", com os textos exatos do parecer. Total: 52.

### L5C (parecer: APROVADO, sem achados)
- Nada a aplicar. CONFERE.

### Regra de forma 6 (prefixo de metadados na justificativa), em todo o pacote
- CONFERE. Nenhuma das 157 justificativas começa por gabarito, [TS], VOLÁTIL, subitem, "convertido" ou "novo".

## 2. Contagens do pacote contra os arquivos canônicos

| Conferência | Esperado | Pacote | Resultado |
|---|---|---|---|
| P2 AUTORAL | 90 | 90 (L1 20 + L1C 10 + L2 30 + L3 30) | CONFERE |
| P2 CEBRASPE_ANALOGA | 7 | 7 (TRF6-2024-C2-070 a 076; 4 C / 3 E) | CONFERE |
| P1 AUTORAL | 60 | 60 (L4 20 + 4C 10 + A5 20 + 5C 10) | CONFERE |
| Total de itens / IDs únicos | 157 | 157 / 157 | CONFERE |
| AUTORAL: C / E / [TS] | 75 / 75 / 75 (GBQ v2) | 75 / 75 / 75 | CONFERE |
| Gabaritos AUTORAL × registro GBQ v2, por script | 150 | 150/150 iguais; subitem e [TS] também 150/150; nenhum ID faltante ou excedente | CONFERE |
| VOLÁTEIS | L1-Q14, Q16, Q18, Q19; L4-15; A5-14 a A5-17 (9) | volatil=true exatamente nesses 9 IDs, cada um com observacao de reverificação entre 4 e 8/1/2027 | CONFERE |
| REVERIFICAR | L3-Q21 | volatil=false; observacao "REVERIFICAR (normativo) entre 4 e 8/1/2027"; é o único item com REVERIFICAR | CONFERE |
| VOLÁTIL + REVERIF. | 10 (GBQ v2) | 9 + 1 | CONFERE |

Método do gabarito: as 150 linhas das tabelas por lote do registro da GBQ v2 (ID | Gab | Sub | [TS]) foram transcritas para arquivo e comparadas por script com itens[].gabarito, itemEdital e ts do pacote. A comparação deu 0 divergência.
O stats.json confere com o pacote, porque foi regenerado de forma idêntica (ponto 0). As contagens por lote (C, E, TS, VOL) coincidem com a tabela "Totais" do registro.

## 3. Compatibilidade com o consumidor (Protótipo 0)

| Regra do carregador | Resultado |
|---|---|
| JSON.parse sem erro | CONFERE (json.loads sobre o arquivo inteiro; 410.923 bytes) |
| "itens" e "simulados" são arrays | CONFERE (itens: 157; simulados: [] — exclusão declarada em "exclusoes") |
| Todo item tem id, enunciado (string não vazia) e gabarito em ["C","E"] | CONFERE (157/157) |
| Lotes têm nome, itensEdital[], resumo, curso, pares[{a,b,como}] e pegadinhas[{itemEdital,texto}] | CONFERE (8 lotes; todos os campos presentes e com o tipo certo; 102 pares, todos com a, b e como em string; 203 pegadinhas, todas com itemEdital e texto não vazio; todo itemEdital de pegadinha e de lote existe no edital) |
| edital[{id,prova,texto}] | CONFERE (40 entradas: 23 P2 e 17 P1; os três campos são strings não vazias) |
| Comandos com faixa de IDs | CONFERE (60 itens normalizados para "... julgue os itens a seguir.", com "comandoOriginal" preservado; não resta nenhum comando com faixa) |

## 4. Amostra de fidelidade (10 itens)

Sorteio: random.seed(20261012) e random.sample sobre a lista ordenada dos 157 IDs do pacote.
IDs sorteados: L1-Q01, L1-Q03, L1-Q12, L1-Q13, L1-Q18, L2-Q27, L4-04, L4-08, A5-09, A5-17.
Comparação: enunciado do pacote × texto (d) da fonte canônica, com espaços normalizados (a fonte quebra linhas) e igualdade estrita de string.

| ID | Fonte canônica | Enunciado | Gab. pacote / GBQ | [TS] / VOL |
|---|---|---|---|---|
| L1-Q01 | GCE_Lote1_v2_CPP.md, (d) Q01 | IDÊNTICO | E / E | – / – |
| L1-Q03 | GCE_Lote1_v2_CPP.md, (d) Q03 | IDÊNTICO | E / E | – / – |
| L1-Q12 | GCE_Lote1_v2_CPP.md, (d) Q12 | IDÊNTICO | E / E | – / – |
| L1-Q13 | GCE_Lote1_v2_CPP.md, (d) Q13 | IDÊNTICO | E / E | TS / – |
| L1-Q18 | GCE_Lote1_v2_CPP.md, (d) Q18 | IDÊNTICO | C / C | – / VOL |
| L2-Q27 | GCE_Lote2_v2_CPP.md, (d) Q27 | IDÊNTICO | C / C | TS / – |
| L4-04 | GCB/Lote4_v3_canonica_GCB-CPP.md, (d) item 4 | IDÊNTICO | C / C | TS / – |
| L4-08 | GCB/Lote4_v3_canonica_GCB-CPP.md, (d) item 8 | IDÊNTICO | E / E | TS / – |
| A5-09 | GCB/Lote5_v3_canonica_GCB-CPP.md, (d) A5-09 | IDÊNTICO | C / C | TS / – |
| A5-17 | GCB/Lote5_v3_canonica_GCB-CPP.md, (d) A5-17 | IDÊNTICO | E / E | TS / VOL |

Resultado: 10/10 idênticos. Nenhum item sorteado é alvo de errata de enunciado (no Lote 1, as erratas de enunciado são E1 Q07, E2 Q08 e E3 Q11; o Lote 2 não tem errata de enunciado). Por isso o texto (d) do v2 é a fonte vigente.
Os comandos dos itens sorteados conferem com a fonte: L1 e L2 "Julgue os itens a seguir (C = certo, E = errado)."; L4 e A5 com o original preservado em comandoOriginal.

## 5. Observações (sem pendência; não exigem correção)

1. L1 O-1: o parecer chamou a entrada de "13ª"; ela é a 14ª do arquivo (5ª de P2-1.3). A correção foi aplicada na entrada certa. O erro é de contagem no parecer, sem efeito.
2. Os lotes L1C, L4C e L5C têm curso e resumo como string vazia (""), por desenho: a fonte não tem seções (a) e (b), e eles se apoiam nos cursos de L1, L4 e L5. A regra do carregador exige presença e tipo, o que se cumpre. Se o Protótipo 0 rejeitar string vazia, isso aparece no teste do Fundador com o pacote carregado (D-PILOT-PROTOTIPO0). Classificação: PRÓXIMO, a verificar nesse teste.
3. L3-Q21 (REVERIFICAR) tem volatil=false, conforme o registro da GBQ, que separa VOLÁTIL de REVERIF. Pela regra R1-N, porém, ele recebe o mesmo tratamento dos voláteis: fica inapto a simulado final até a reverificação. O pacote não tem simulados hoje. Quando o montador de simulados existir, ele deve excluir também os itens com "REVERIFICAR" em observacao, e não só os que têm volatil=true. Classificação: PRÓXIMO (GBQ/montagem de simulados).
4. A amostra aleatória não incluiu itens de L1C, L3, 4C ou 5C nem itens reais. Esses itens foram conferidos integralmente, palavra a palavra, na rodada 1 (os reais, contra o caderno e o gabarito oficiais do cdn.cebraspe.org.br). A conferência de aplicação acima confirma que as correções nesses lotes não tocaram enunciado nem gabarito.

## 6. Pendências

Nenhuma.

FIM DA CONFERÊNCIA
