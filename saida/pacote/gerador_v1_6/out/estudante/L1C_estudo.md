# Lote 1-C — RF-ASR, complemento (P2 1.1–1.5)

Prova: P2

## Itens do edital

- P2-1.1 — Reconhecimento automático de fala (ASR – Automatic Speech Recognition)
- P2-1.2 — Modelos de fala end-to-end
- P2-1.3 — LLMs multimodais de áudio nativo
- P2-1.4 — Diarização de falantes: identificação e separação de múltiplos oradores
- P2-1.5 — Pontuação automática e capitalização em transcrições

## Resumo

```text
```

## Curso

```text
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
    amostras de referência, não basta.
 2. Se o item fala em DISTINGUIR, SEPARAR, "quantos oradores" ou rótulos
    genéricos: é diarização, mesmo que use o verbo "identificar".
 3. Se o item usa "identificar" sem mais contexto, não o julgue pelo
    verbo: procure o OBJETO da frase. "Identifica que há três oradores"
    = distinguir. "Identifica os oradores pelo nome" = identificação.
 4. Verificação de locutor continua sendo outra coisa: 1 para 1,
    contra uma identidade alegada (item 1.4).
Ligação com a prática da Casa: na nota taquigráfica, o nome do
parlamentar vem de cadastro ou da atribuição humana; o rótulo da
diarização é só ponto de partida (exemplo parlamentar do 1.4).
Ponte que confunde: diarização ligada à identificação por amostras de
referência (a API da OpenAI aceita até quatro amostras com nomes) mapeia rótulos para nomes. Aí o nome existe
por causa das amostras, não da diarização em si.

PEGADINHAS ADICIONAIS
(1) Ler "identificação" do título como "o sistema sabe os nomes".
(2) Ler "identificar" no item como identificação de locutor sem checar
o objeto. (3) Dizer que diarização que distingue oradores também
verifica identidade. (4) Dizer que, por existirem amostras de
referência, a diarização "sempre" entrega nomes: depende de as
amostras terem sido fornecidas.
```

## Pares

_Nenhum par neste lote._

## Pegadinhas

- [P2-1.4] **Diarização de falantes: identificação e separação de múltiplos oradores** — Ler "identificação" do título como "o sistema sabe os nomes".
- [P2-1.4] **Diarização de falantes: identificação e separação de múltiplos oradores** — Ler "identificar" no item como identificação de locutor sem checar o objeto.
- [P2-1.4] **Diarização de falantes: identificação e separação de múltiplos oradores** — Dizer que diarização que distingue oradores também verifica identidade.
- [P2-1.4] **Diarização de falantes: identificação e separação de múltiplos oradores** — Dizer que, por existirem amostras de referência, a diarização "sempre" entrega nomes: depende de as amostras terem sido fornecidas.
