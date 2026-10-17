# Lote 1 — RF-ASR (reconhecimento de fala e transcrição, P2 1.1–1.8) — gabarito e justificativas

### L1-Q01 — Gabarito: E

- Item do edital: P2-1.1
- Justificativa: No cálculo usual, pontuação e capitalização ficam fora do WER, e a atribuição de locutor fica fora em qualquer convenção, então WER 0% não garante fidelidade nesses aspectos. Erro por extrapolação.

### L1-Q02 — Gabarito: E

- Item do edital: P2-1.1
- Justificativa: ASR produz texto; atribuir falas a locutores é diarização (rótulos) ou identificação (nomes), módulos distintos.

### L1-Q03 — Gabarito: E

- Item do edital: P2-1.2
- Justificativa: Modelos end-to-end podem produzir trechos fluentes porém falsos onde o áudio é ruim; a arquitetura não imuniza contra alucinação. Erro por generalização.

### L1-Q04 — Gabarito: C

- Item do edital: P2-1.2
- Justificativa: Falsa pegadinha: "supervisão fraca" parece sugerir ausência de rótulos, mas significa transcrições preexistentes; pares áudio–texto continuam necessários.

### L1-Q05 — Gabarito: C

- Item do edital: P2-1.3
- Justificativa: É o que distingue o modelo nativo da arquitetura em cascata: áudio como entrada do próprio LLM.

### L1-Q06 — Gabarito: E

- Item do edital: P2-1.3
- Justificativa: Na cascata o LLM recebe apenas o texto do ASR; prosódia se perde — justamente a limitação que o áudio nativo pretende superar.

### L1-Q07 — Gabarito: E

- Item do edital: P2-1.4
- Justificativa: Diarização entrega rótulos genéricos (Locutor 1, 2...); exibir nomes exige identificação (amostra cadastrada ou revisão humana). Erro por extrapolação.

### L1-Q08 — Gabarito: C

- Item do edital: P2-1.4
- Justificativa: Falsa pegadinha: a frase soa invertida mas está correta — verificação é 1:1 contra identidade alegada; diarizar não exige verificar nem identificar.

### L1-Q09 — Gabarito: C

- Item do edital: P2-1.4
- Justificativa: DER soma erro de falante, fala perdida e falso alarme; WER soma substituições, deleções e inserções de palavras. Métricas distintas para tarefas distintas.

### L1-Q10 — Gabarito: C

- Item do edital: P2-1.5
- Justificativa: Modelos end-to-end podem emitir texto já pontuado e capitalizado; pipelines clássicos em geral restauram pontuação em etapa posterior.

### L1-Q11 — Gabarito: C

- Item do edital: P2-1.5
- Justificativa: Falsa pegadinha: o item parece confundir os dois recursos, mas os distingue corretamente — ditado do sinal versus inferência do sinal.

### L1-Q12 — Gabarito: E

- Item do edital: P2-1.6
- Justificativa: Adaptação de vocabulário enviesa o reconhecimento para termos esperados; não garante acerto em qualquer condição acústica nem corrige sotaque. Erro por generalização.

### L1-Q13 — Gabarito: E

- Item do edital: P2-1.6
- Justificativa: Adaptação é lista de termos que enviesa o reconhecimento, não retreino acústico; sotaque pede dados acústicos/modelo customizado.

### L1-Q14 — Gabarito: C

- Item do edital: P2-1.6
- Justificativa: Distinção documentada pela AWS: custom vocabulary amplia o vocabulário base; custom language model é treinado com dados de texto.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-Q15 — Gabarito: C

- Item do edital: P2-1.7
- Justificativa: Funcionamento padrão do streaming: parciais revisáveis e final em geral consolidado após o fim do enunciado.

### L1-Q16 — Gabarito: E

- Item do edital: P2-1.7
- Justificativa: stream=true devolve texto incremental de um arquivo já completo; áudio ao vivo usa a transcrição Realtime, fluxo distinto.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-Q17 — Gabarito: C

- Item do edital: P2-1.7
- Justificativa: Falsa pegadinha: o item parece afirmar ganho duplo, mas afirma o trade-off correto — menor latência, risco de fragmentar enunciados.

### L1-Q18 — Gabarito: C

- Item do edital: P2-1.8
- Justificativa: Código e pesos abertos no repositório openai/whisper, licença MIT; a API recomenda gpt-transcribe para transcrição geral e reserva whisper-1 a timestamps, legendas e tradução.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-Q19 — Gabarito: E

- Item do edital: P2-1.8
- Justificativa: A documentação oficial prevê implantação em nuvem ou on-premises via contêineres.

> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.

### L1-Q20 — Gabarito: E

- Item do edital: P2-1.8
- Justificativa: Em serviço em nuvem o áudio é enviado a infraestrutura de terceiro; só a execução local mantém o áudio sob controle exclusivo da instituição. Equivalência de custódia é falsa.

### L1C-Q21 — Gabarito: E

- Item do edital: P2-1.1
- Justificativa: Inverte as funções: o modelo acústico liga o áudio a unidades sonoras; o de linguagem estima sequências de palavras.

### L1C-Q22 — Gabarito: E

- Item do edital: P2-1.1
- Justificativa: Erro por extrapolação: inserções entram no numerador, e o WER pode ultrapassar 100%.

### L1C-Q23 — Gabarito: C

- Item do edital: P2-1.2
- Justificativa: Sem léxico separado, a correção passa, em regra, por adaptação (1.6) ou mais dados; dados de pronúncia são recurso de custom speech (Azure).

### L1C-Q24 — Gabarito: C

- Item do edital: P2-1.2
- Justificativa: Falsa pegadinha: em muitos sistemas há espectrograma (ex.: Whisper), mas não é universal; o wav2vec 2.0 recebe áudio bruto.

### L1C-Q25 — Gabarito: E

- Item do edital: P2-1.3
- Justificativa: Erro por generalização: o LLM nativo gera texto plausível, não copia; o edital mantém a revisão humana (2.2).

### L1C-Q26 — Gabarito: E

- Item do edital: P2-1.3
- Justificativa: ASR reforçado por LLM não é LLM nativo: reforço por LLM não implica, por si, que o áudio entre como modalidade do próprio LLM; o nexo 'por esse motivo' é falso.

### L1C-Q27 — Gabarito: C

- Item do edital: P2-1.4
- Justificativa: Falsa pegadinha: "identificar" no sentido amplo é distinguir; nomes exigem cadastro ou atribuição humana.

### L1C-Q28 — Gabarito: E

- Item do edital: P2-1.4
- Justificativa: O OBJETO decide: "que há três oradores" = distinguir; "pelo nome" = identificação própria (amostras ou atribuição humana).

### L1C-Q29 — Gabarito: C

- Item do edital: P2-1.5
- Justificativa: A pontuação é inferida e pode mudar o sentido ("Aprovado." × "Aprovado?"); a revisão a confere.

### L1C-Q30 — Gabarito: E

- Item do edital: P2-1.5
- Justificativa: Erro por generalização: a capitalização estima e pode errar (Câmara × câmara).
