ENTREGA DE LOTE — GCE-CPP-S1 → GCE
Data: 08/10/2026
LOTE 1-C v1 — PARTE 1/1 — RF-ASR, complemento D-LACUNAS do Lote 1
(P2, Cargo 11, itens 1.1 a 1.5). Não reabre o v2.
Base: GCE_Lote1_v2_CPP.md + GCE_Lote1_consolidacao_GCE.md (errata E1 a
E6; onde houver conflito, prevalece a errata). Todos os itens C/E são
AUTORAL. Sem discursiva e sem peça.

EVIDÊNCIA
Nenhuma fonte nova foi aberta neste complemento. As afirmações de
produto seguem as fontes F1 a F12 do v2, verificadas em 07/10/2026 e
confirmadas pela CQFP; esta unidade não as reabriu. Nenhum item deste
complemento depende de produto ou de fornecedor: VOLÁTEIS = nenhum.
Guia de estilo v1.0: não visível para esta unidade; não usado.

=====================================================================
(a) ADENDO AO CURSO DO 1.4 — A PEGADINHA DO TÍTULO DO EDITAL
=====================================================================
O edital intitula o 1.4 "Diarização de falantes: identificação e
separação de múltiplos oradores". A banca pode usar "identificar" em
dois sentidos, e o julgamento do item depende de qual deles o enunciado
adota.

SENTIDO AMPLO — "identificar" = DISTINGUIR
Perceber que há oradores diferentes e separar as falas de cada um:
"Locutor 1", "Locutor 2". É o que a diarização faz. Não implica saber
quem é cada pessoa. Frases típicas: "a diarização identifica os
diferentes oradores"; "identificação e separação de múltiplos
oradores".

SENTIDO PRÓPRIO — "identificar" = DIZER QUEM É
Associar a voz a uma pessoa determinada: por amostras de voz cadastradas
(identificação de locutor) ou por atribuição humana, com a lista de
inscritos e a ordem das falas. Frases típicas: "exibir o nome do
orador"; "informar a identidade"; "indicar qual parlamentar falou".

REGRA DE DECISÃO PARA A PROVA
 1. Se o item fala em IDENTIDADE, NOME, CADASTRO, "qual parlamentar" ou
    "quem é": é identificação propriamente dita. Diarização sozinha, sem
    amostras de referência (errata E1), não basta.
 2. Se o item fala em DISTINGUIR, SEPARAR, "quantos oradores" ou rótulos
    genéricos: é diarização, mesmo que use o verbo "identificar".
 3. Se o item usa "identificar" sem mais contexto, não o julgue pelo
    verbo: procure o OBJETO da frase. "Identifica que há três oradores"
    = distinguir. "Identifica os oradores pelo nome" = identificação.
 4. Verificação de locutor continua sendo outra coisa: 1 para 1,
    contra uma identidade alegada (v2, item 1.4).
Ligação com a prática da Casa: na nota taquigráfica, o nome do
parlamentar vem de cadastro ou da atribuição humana; o rótulo da
diarização é só ponto de partida (v2, exemplo parlamentar do 1.4).
Ponte que confunde: diarização ligada à identificação por amostras de
referência (a API da OpenAI aceita até quatro amostras com nomes
[V 07/10/2026 — F1, v2]) mapeia rótulos para nomes. Aí o nome existe
por causa das amostras, não da diarização em si.

PEGADINHAS ADICIONAIS
(1) Ler "identificação" do título como "o sistema sabe os nomes".
(2) Ler "identificar" no item como identificação de locutor sem checar
o objeto. (3) Dizer que diarização que distingue oradores também
verifica identidade. (4) Dizer que, por existirem amostras de
referência, a diarização "sempre" entrega nomes: depende de as
amostras terem sido fornecidas.

=====================================================================
(d) VERSÃO DO ESTUDANTE — 10 ITENS C/E (AUTORAL) — Q21 a Q30
=====================================================================
Julgue os itens a seguir (C = certo, E = errado).

Q21. No pipeline clássico de reconhecimento automático de fala, o
modelo de linguagem associa trechos de áudio a unidades sonoras, ao
passo que o modelo acústico estima quais sequências de palavras são
mais prováveis.

Q22. Como o WER é calculado pela divisão do número de erros pelo número
de palavras da transcrição de referência, ele nunca ultrapassa 100%.

Q23. Em sistemas de reconhecimento de fala end-to-end, em regra não há
dicionário de pronúncias separado a ser editado, de modo que corrigir o
reconhecimento de um nome próprio passa por adaptação de vocabulário ou
por mais dados, e não pela inclusão de uma entrada em um léxico.

Q24. Embora o modelo end-to-end mapeie o áudio diretamente ao texto
em uma rede única, o sinal continua sendo convertido em representação
acústica, como um espectrograma, antes de entrar na rede.

Q25. Por receber o áudio diretamente como entrada, um LLM multimodal de
áudio nativo produz sempre uma cópia literal da fala, o que dispensa a
revisão humana em registros oficiais.

Q26. Um serviço de reconhecimento de fala cuja qualidade é reforçada
por um LLM, mas que apenas converte áudio em texto, é, por esse motivo,
um LLM de áudio nativo.

Q27. Quando se afirma que a diarização "identifica" os diferentes
oradores de uma gravação, o verbo pode ser entendido no sentido de
distinguir um orador do outro, sem que isso implique saber o nome de
cada um.

Q28. Se um sistema exibe o nome do parlamentar que falou em cada trecho,
trata-se apenas de diarização, pois, nesse contexto, identificar
significa tão somente distinguir um orador do outro.

Q29. Em registro oficial, a pontuação inserida automaticamente pode
alterar o sentido de um enunciado, como na diferença entre uma
afirmação e uma pergunta, razão pela qual a revisão deve conferir a
pontuação, e não apenas as palavras.

Q30. A capitalização automática distingue com segurança os nomes
próprios das palavras comuns, de modo que "Câmara", como instituição, e
"câmara", como sala, nunca são confundidas por esse recurso.

=====================================================================
(d-G) GABARITO COMENTADO
=====================================================================
Legenda: [TS] = troca sutil de conceito; VOLÁTIL = depende de fato de
produto verificado (nenhum neste complemento); "falsa pegadinha" = item
[TS] com gabarito C.

Q21. E [TS] — 1.1. Inverte as funções: o modelo acústico associa o áudio
a unidades sonoras; o modelo de linguagem estima as sequências de
palavras prováveis.

Q22. E — 1.1. Erro por extrapolação: as inserções entram no numerador e
não no denominador, então o WER pode ultrapassar 100%.

Q23. C — 1.2. Sem léxico separado, a correção do nome passa por
adaptação de vocabulário (1.6) ou mais dados; "em regra" ressalva
sistemas que acoplam recursos externos.

Q24. C [TS] — 1.2. Falsa pegadinha: "end-to-end" parece dispensar o
pré-processamento, mas o áudio continua convertido em espectrograma
antes da rede.

Q25. E — 1.3. Erro por generalização ("sempre", "dispensa"): o modelo
nativo GERA texto plausível, não copia, e o edital mantém a revisão
humana (2.2).

Q26. E [TS] — 1.3. Confunde ASR aprimorado por LLM com LLM de áudio
nativo: usar LLM para reforçar o reconhecimento não faz do serviço um
modelo que recebe o áudio como modalidade de entrada do próprio LLM.

Q27. C [TS] — 1.4. Falsa pegadinha: parece confundir diarização com
identificação, mas "identificar" no sentido amplo é distinguir; nomes
exigem cadastro ou atribuição humana.

Q28. E [TS] — 1.4. Quando o item fala em NOME, é identificação própria
(amostras de referência ou atribuição humana, errata E1); diarização
sozinha entrega rótulos genéricos.

Q29. C — 1.5. A pontuação é inferida e pode mudar o sentido
("Aprovado." × "Aprovado?"); por isso a revisão confere pontuação
além das palavras.

Q30. E — 1.5. Erro por generalização ("com segurança", "nunca"): a
capitalização estima e pode errar em decisões de contexto, como Câmara
× câmara.

Distribuição: 4 C (Q23, Q24, Q27, Q29) e 6 E (Q21, Q22, Q25, Q26, Q28,
Q30): 40% de itens C.
Itens [TS]: 5 (Q21, Q24, Q26, Q27, Q28), dos quais 2 com gabarito C
(falsas pegadinhas: Q24, Q27) e 3 com gabarito E.
Itens sem troca sutil: 5, dos quais 2 C (Q23, Q29) e 3 E por
extrapolação ou generalização (Q22, Q25, Q30).
VOLÁTEIS: 0; nenhum de risco ALTO.
Sem repetição: nenhum item repete o ponto de julgamento de Q01 a Q20 do
v2 (Q22 julga o limite do WER, que o v2 só trazia no curso; Q28 e Q27
julgam o sentido de "identificar", que o Q07 e o Q08 do v2 não julgam).

TABELA DE COBERTURA
Subitem | Itens        | C | E | [TS]         | VOLÁTEIS
1.1     | Q21–Q22 (2)  | 0 | 2 | Q21 (1)      | —
1.2     | Q23–Q24 (2)  | 2 | 0 | Q24 (1)      | —
1.3     | Q25–Q26 (2)  | 0 | 2 | Q26 (1)      | —
1.4     | Q27–Q28 (2)  | 1 | 1 | Q27, Q28 (2) | —
1.5     | Q29–Q30 (2)  | 1 | 1 | —            | —
Total   | 10           | 4 | 6 | 5            | 0
Prioridade atendida: os subitens 1.1, 1.2, 1.3 e 1.5, que tinham 2
itens no v2, recebem mais 2 cada; o 1.4 recebe 2 itens sobre a
ambiguidade do título (Q27 e Q28), acima do mínimo de 1.

PRÓXIMO: Lote 3 (despacho B), sem esperar QA. Entrega a seguir.
Fundador: gravar como GCE_Lote1C_v1_CPP.md.

FIM DO LOTE 1-C v1