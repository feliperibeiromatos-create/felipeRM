# QA_T96C_R1_2026-10-18_gce-cqfp.md — T-96 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L1_reforco_onda2_C_v1.md (gce-cpp; 28 itens AUTORAL, L1-R75 a L1-R102; folhas P2-1.5 e P2-1.6; sha256 09cc589c938e3c4507c3fa63b6e044875bcf673fadd9511e651a90cfbbd7cbb1). Rodada 1 de no máximo 2 (D-REFORCO-1/2).
Critérios: D-REFORCO-1 e 2 (regras 1 a 6); D-FONTE-DATA-ANTERIOR; D-T89-R1-ACEITE (critério de VOLÁTIL da T89_reconciliacao, seção 1); D-ONDA2-FILA; T89_reconciliacao, seção 3 ([TS] ≥ metade + 2; nenhum "par confundível" novo em 1.5 e 1.6); T93_reconciliacao O-1 a O-8; edital/modulo_RF_IA_P2.md (1.5 "Pontuação automática e capitalização em transcrições"; 1.6 "Desafios do ASR em Português Brasileiro: sotaques, vocabulário técnico e parlamentar"); pacote.json v1.9 (6 existentes de cada folha); canônicos do Lote 1; e, para conferir duplicata dentro da onda, as partes A, B e D da T-96 (L1_reforco_onda2_A_v1.md, B_v1.md, D_v2.md) e QA_T96A_R1.
A QA revisa; não reescreve. Os textos de ajuste abaixo são o texto exato a aplicar; nada mais muda.

## 1. Evidência — URLs reabertas pela QA em 18/10/2026 (curl; 18/18 HTTP 200)

Todos os 50 trechos literais citados na Parte 3 foram conferidos por script (python -I) contra o texto das páginas baixadas: 50/50 CONFERE.

| fonte | resultado | observação da QA |
|---|---|---|
| docs.aws.amazon.com …/how-it-works.html | CONFERE | "confidence scores and timestamps for each word or punctuation mark" (R75) |
| docs.aws.amazon.com …/how-numbers.html | CONFERE | "case distinction in their writing systems" (R78) |
| docs.aws.amazon.com …/streaming-partial-results.html | CONFERE | exemplo com "Content": ".", "Type": "punctuation", StartTime = EndTime = fim da palavra anterior; campo Stable; itálico (R75, R79) |
| docs.aws.amazon.com …/custom-vocabulary-create-table.html | CONFERE | "Defines the how you want your entry to look…"; DynamoDB (R84) |
| docs.cloud.google.com …/automatic-punctuation | CONFERE | "capitalize the first letter after each period and question mark" (R76) |
| docs.cloud.google.com …/adaptation-model | CONFERE | boost: menos falsos negativos, mais falsos positivos (R97) |
| docs.cloud.google.com …/best-practices | CONFERE, com ressalva em R90 | R91 literal; para R90 a página diz "Position the microphone as close as possible to the person that is speaking" e "Avoid audio clipping" (ver R90) |
| learn.microsoft.com …/display-text-format | CONFERE | R77, R83 |
| learn.microsoft.com …/how-to-custom-speech-evaluate-data | CONFERE | 9 trechos (R81, R82, R85, R93, R95, R102) |
| learn.microsoft.com …/custom-speech-overview | CONFERE | R96, R99 |
| learn.microsoft.com …/improve-accuracy-phrase-list | CONFERE | R94 |
| learn.microsoft.com/legal …/transparency-note | CONFERE | 9 trechos (R89–R92, R94); "Mismatched locales … accuracy would be reduced" |
| learn.microsoft.com …/batch-transcription-create | CONFERE | R87 |
| learn.microsoft.com …/fast-transcription-create | CONFERE | R88 |
| learn.microsoft.com …/how-to-recognize-speech | CONFERE | R86; a mesma seção registra "SDK version 1.41 or later" e "isn't available for all languages and locales" (confirma VOLÁTIL) |
| raw.githubusercontent.com/openai/whisper/main/README.md | CONFERE | R101 |
| raw.githubusercontent.com/openai/whisper/main/model-card.md | CONFERE | R98 |
| raw.githubusercontent.com/openai/whisper/main/whisper/transcribe.py | CONFERE | l. 51–52 (padrões prepend/append), l. 95–104 (docstring), l. 558–559 (ajuda da CLI) (R80, R100) |

Bases não reabertas: nenhuma. Nenhuma base de data anterior (D-FONTE-DATA-ANTERIOR não invocada; conferido). Nenhuma norma citada: sem PENDENTE NORMATIVO.

## 2. Respostas às dúvidas da produtora e pontos de julgamento

1. **Docstring/código do repositório oficial do Whisper (R80, R100) como "documentação do fornecedor".** SIM, vale: o docstring de transcribe() é a documentação de API escrita pelo fornecedor no repositório oficial (a mesma frase é a ajuda da CLI, l. 558–559), na mesma origem já aceita para README e model-card (D-T89-R1-ACEITE, cond. 1). Ressalva de proveniência: o ramo main muda mais que o README; recomenda-se registrar na tabela de proveniência o commit (SHA) do arquivo lido, para a conferência de janeiro. O que derruba o R80 não é o tipo de fonte, e sim o objeto (ver R80).
2. **VOLÁTIL (R86, R87, R88).** Classificação correta pelo critério da D-T89-R1-ACEITE (existência/condições de recurso de serviço gerenciado). R87 cai por outro motivo (duplicata); com isso, 1.5 fica em 2/20 VOLÁTEIS.
3. **R83 (oração não literal).** Aceita: o decisivo ("pode ser convertida no sinal") está na base literal; "independentemente de ter sido citada como assunto" é possibilidade ("pode"), não afirmação de que o sistema nunca distingue. Registro: o ponto do mapa ("o sistema não distingue a intenção") é mais forte que o item; a Gerência deve registrá-lo como "a palavra pode ser convertida mesmo quando citada como assunto".
4. **R90 (Microsoft × Google).** AJUSTAR: o Google manda pôr o microfone "as close as possible" ao orador; sem âncora, um recurso pode sustentar C com base no Google. Ver texto exato.
5. **TER em 1.5 (R81, R82, R85).** Aceito: três pontos distintos (atribuição WER × TER; cálculo; requisito da referência), 3/20 = 15%. Registro: concentração em métrica nomeada por um só fornecedor; se a Gerência quiser diluir, R85 é o de troca.

Proximidades declaradas: R77 × L1C-Q30 distinta (alcance × certeza); **R87 × L1-Q11 duplicata substancial** (ver R87); R88 × L1-R09 distinta (definição × capacidade de API); R94 × L1-Q13 distinta, mas ver R94 × L1-R120 (1.8); R98 × L1-Q12/Q13 distinta, mas a proximidade relevante é L1-R11 (idiomas × sotaques do mesmo idioma: distinta) e L1-R43 da parte A (ver R98); R100 × L1-R10 distinta.

Duplicatas DENTRO DA ONDA, em outra folha (não declaradas; achadas pela QA ao cruzar com as partes A e D):
- R101 (1.6) = L1-R117 (1.8, parte D): mesmo ponto (.en só inglês; português exige modelo multilíngue), mesma base.
- R99 (1.6) = L1-R128 (1.8, parte D): mesmo ponto (comparar modelo base com transcrição humana pelo WER; WER alto → treinar), mesmos trechos.
- R102 (1.6) × L2-R06 (2.3, canônico): mesmo julgamento (inserções entram no WER), com cálculo; e R102 × L1-R19 (1.1, parte A), fórmula do WER.
- R93 (1.6) × L1-R20 (1.1, parte A): mesma associação (omissões ↔ sinal fraco; substituições ↔ amostra de termos do domínio), mesmo trecho; R20 C, R93 E invertido. Tolerável pela regra 1 (folhas distintas; precedente R12 × L1C-Q21 na T89, seção 2), mas registrado para D1.
- R94 (1.6) × L1-R120 (1.8, parte D): metade do ponto (phrase list em tempo de execução, sem treino) coincide; R94 acrescenta o lado do custom speech. Registrado.
- R86 (1.5) × L1-R111 (1.7) e R79 (1.5) × L1-R103 (1.7): pontos distintos sobre a mesma seção de documentação; registrados.
- **Bloqueio de transferência:** a QA_T96A_R1 admite transferir L1-R43 (parte A, reprovado em 1.2) para 1.6. R43 tem o mesmo ponto do R98 (desempenho desigual do Whisper entre sotaques do mesmo idioma, mesma base). Se R98 for mantido, R43 não pode ir para 1.6.

## 3. Veredito por item

| id | folha | gab. | [TS] | formato | VOL | veredito | motivo |
|---|---|---|---|---|---|---|---|
| L1-R75 | 1.5 | E | sim | D | n | APROVADO | troca única (sinal como item próprio × anexado); nota: na saída em lote o sinal não traz tempos próprios, mas a primeira oração já torna o item E, sem ambiguidade de gabarito |
| L1-R76 | 1.5 | C | não | NP | n | AJUSTAR | "13 palavras iniciadas por maiúscula" admite leitura de total do trecho (a 1ª palavra do trecho e nomes próprios também vêm em maiúscula) → recurso; ver A-1 |
| L1-R77 | 1.5 | E | sim | TS | n | APROVADO | base literal; ponto distinto de L1C-Q30 |
| L1-R78 | 1.5 | C | não | D | n | APROVADO | correto; registro: baixa discriminação (verdade quase lógica) |
| L1-R79 | 1.5 | C | sim | AP | n | APROVADO | base literal; registro: [TS] espelho fraco (O-6 admite) e formato AP sem elemento parlamentar (é "legenda ao vivo"; reclassificar como D não estoura o teto: D 4/20) |
| L1-R80 | 1.5 | E | sim | TS | n | REPROVADO | extrapolação do edital: o ponto é detalhe de implementação (fusão de pontuação ao alinhar marcas de tempo por palavra), não pontuação automática; e o gabarito depende dos valores padrão de append/prepend_punctuations na assinatura do ramo main (item dependente de versão) |
| L1-R81 | 1.5 | E | sim | TS | n | APROVADO | troca única WER × TER |
| L1-R82 | 1.5 | C | não | NP | n | APROVADO | (1+2+3)/80 = 7,5% conferido |
| L1-R83 | 1.5 | C | não | AP | n | APROVADO | ver seção 2, item 3 (registro do ponto) |
| L1-R84 | 1.5 | C | não | AP | n | AJUSTAR | a condição inicial ("serviços que permitem associar… a forma como deve aparecer") entrega a conclusão; o item não testa nada; ver A-2 |
| L1-R85 | 1.5 | E | sim | SH | n | APROVADO | base literal; concentração TER registrada |
| L1-R86 | 1.5 | E | sim | TS | S | APROVADO | VOLÁTIL correto (SDK mínimo; indisponível para alguns idiomas) |
| L1-R87 | 1.5 | E | sim | SH | S | REPROVADO | duplicata substancial de L1-Q11 na folha: quem sabe que pontuação "ditada" é a falada (Q11) responde o item; o rótulo de API acrescenta só VOLÁTIL |
| L1-R88 | 1.5 | C | não | SH | S | APROVADO | ponto distinto de R09; VOLÁTIL correto |
| L1-R89 | 1.6 | C | não | SH | n | APROVADO | "tende" protege contra detecção automática de idioma |
| L1-R90 | 1.6 | E | sim | D | n | AJUSTAR | conflito Microsoft ("too close") × Google ("as close as possible"); ancorar; ver A-3 |
| L1-R91 | 1.6 | C | não | AP | n | APROVADO | dupla base literal |
| L1-R92 | 1.6 | C | não | D | n | AJUSTAR | afirmação absoluta e genérica ("o resultado é um erro") é imprecisa para modelos end-to-end com subpalavras, que podem grafar palavra não vista; a banca puniria; ancorar no fornecedor; ver A-4 |
| L1-R93 | 1.6 | E | sim | TS | n | APROVADO | troca única; registro × L1-R20 (seção 2) |
| L1-R94 | 1.6 | E | sim | TS | n | APROVADO | troca única; registro × Q13, Q14 e L1-R120 |
| L1-R95 | 1.6 | C | sim | SH | n | APROVADO | espelho legítimo de R93 (O-6) |
| L1-R96 | 1.6 | C | não | AP | n | APROVADO | base literal |
| L1-R97 | 1.6 | E | sim | TS | n | APROVADO | troca única FP × FN |
| L1-R98 | 1.6 | E | não | D | n | APROVADO | base literal; bloqueia a transferência de L1-R43 (seção 2) |
| L1-R99 | 1.6 | C | sim | SH | n | REPROVADO | mesmo ponto e mesmos trechos de L1-R128 (1.8, parte D) na mesma onda; o banco teria o item duas vezes (D1 da Gerência pode manter este e retirar o R128, mas não os dois) |
| L1-R100 | 1.6 | C | não | AP | n | APROVADO | docstring é documentação do fornecedor; "mais provável, sem garantia" literal; recomendar SHA do commit |
| L1-R101 | 1.6 | E | sim | TS | n | REPROVADO | mesmo ponto de L1-R117 (1.8, parte D); além disso o ponto (catálogo de modelos) é de 1.8, não desafio de pt-BR |
| L1-R102 | 1.6 | E | sim | NP | n | REPROVADO | escopo da folha: fórmula do WER é de 1.1 (avaliação), sem relação com sotaque ou vocabulário; julgamento já coberto por L2-R06 (inserções entram no WER) e próximo de L1-R19 |

## 4. Textos exatos de ajuste (A-1 a A-4)

- **A-1 (L1-R76, Parte 2):** trocar "isso resulta em 13 palavras iniciadas por maiúscula." por "essa regra resulta na capitalização de 13 palavras." (gabarito C mantido; justificativa sem mudança).
- **A-2 (L1-R84, Parte 2):** trocar "Em serviços de ASR que permitem associar, a cada termo de um vocabulário personalizado, a forma como ele deve aparecer na saída, a equipe pode fazer constar da transcrição siglas e nomes próprios da Casa com a grafia e as maiúsculas desejadas." por "Há serviços de ASR em que o vocabulário personalizado permite associar a cada termo a forma como ele deve aparecer na saída, o que possibilita fazer constar da transcrição siglas e nomes próprios da Casa com a grafia e as maiúsculas desejadas." (gabarito C; não VOLÁTIL, afirmação existencial sustentada pelo Amazon Transcribe).
- **A-3 (L1-R90, Parte 2):** inserir no início "Segundo a nota de transparência do Azure Speech, " e trocar "Na captação" por "na captação" (gabarito E mantido; O-4 respeitado: a cauda falsa "por captar a voz com mais nitidez" é a própria troca).
- **A-4 (L1-R92, Parte 2):** trocar "Quando uma palavra ausente do vocabulário do modelo aparece no áudio, o resultado é um erro de transcrição, razão pela qual" por "Segundo a nota de transparência do Azure Speech, quando uma palavra que não existe no modelo aparece no áudio, o resultado é um erro de transcrição; por isso," (gabarito C mantido).

## 5. Conferências de conjunto

- Cobertura do edital: 1.5 e 1.6 transcritos literalmente; 1.5 bem coberta (pontuação, capitalização, formas lexical/exibição, avaliação). 1.6: dos 14 novos, só R89 (idioma) e R98 (sotaques) tocam o pt-BR/sotaque; o resto é vocabulário (adequado) ou condição acústica genérica (R90, R95). Recomenda-se que as substituições de 1.6 tratem de sotaques regionais ou vocabulário parlamentar pt-BR, com base oficial.
- Formato e tetos (como entregue): conferidos; nenhum formato > 30%; nenhum PC novo (restrição T89 cumprida). Após as reprovações: 1.5 D 3, TS 4, SH 3, NP 2, PC 2, AP 4 (18); 1.6 D 4, TS 4, SH 3, NP 0, PC 2, AP 4 (17). Substituições sem PC, sem "definição" se a Gerência reclassificar R79 para D.
- VOLÁTIL: 1.5 3/20 como entregue → 2/20 sem R87; 1.6 1/20 (Q14). Teto de 20% cumprido; risco alto 0.
- [TS]: 16/28 como entregue (exigência 16); conferidos um a um: os 13 em E trocam exatamente um conceito; os 3 C (R79, R95, R99) seguem o O-6 (R79 fraco). Sem os reprovados: 11/23. As 5 substituições precisam TODAS de [TS] para fechar 16/28.
- Gabarito: 14 C / 14 E (50%) conferido por script. Sem os reprovados: 13 C / 10 E; por folha 1.5 7 C / 5 E e 1.6 6 C / 5 E. Substituições sugeridas: 1.5 2 E; 1.6 2 E + 1 C (fecha 14/14 e 7/7 por folha).
- Estilo (O-1 a O-8): conferido; médias de extensão equilibradas (C 43,8 × E 43,4); O-2 (R83), O-3 (R98), O-7 (R78), O-8 (R85) presentes. Sem cauda autocontraditória.
- Estrutura: linha 1 no formato; PARTE 1/3–3/3 e FIM DO LOTE presentes; Parte 2 com 28 itens e 0 marcas de gabarito/[TS]/VOLÁTIL/REVERIFICAR (script); rótulo AUTORAL; "QA PENDENTE" declarado.

## 6. Taxa e veredito

Reprovados: 5/28 = 17,9% (R80, R87, R99, R101, R102), abaixo do gate de 30%. AJUSTAR: 4 (R76, R84, R90, R92). APROVADOS: 19.
Veredito geral: APROVADO COM RESSALVAS. Para a R2: aplicar A-1 a A-4 literalmente; substituir R80 e R87 (1.5) e R99, R101 e R102 (1.6) por 5 itens novos, todos com [TS], sem PC, ponto único contra os 20 da folha e sem repetir ponto das partes A, B e D da onda (conferir em especial 1.7 e 1.8 da parte D); não transferir L1-R43 para 1.6 enquanto R98 estiver mantido. Registros para a Gerência (D1): R83 (ponto), R79 (formato/[TS]), R93 × L1-R20, R94 × L1-R120, SHA de commit para R100, concentração TER em 1.5.
