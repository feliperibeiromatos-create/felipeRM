# T83_errata_proposta_2026-10-17.md — T-83 — 2026-10-17 — gerado por gcb-cpp

PROPOSTA DE ERRATA DE FORMA (não aplicada ao canônico). Nenhum gabarito, enunciado, [TS], VOLÁTIL ou fonte muda; só a frase indicada. QA pendente (gcb-cqfp), depois gcb-gerencia.

## Erratum 1 — L4-11, justificativa (aceita)

Fonte nomeada, conforme a tabela de fontes do próprio Lote 4 (canônico, linha 48): F4 = Google for Developers, "Introduction to ML: What is Machine Learning?", developers.google.com/machine-learning/intro-to-ml/what-is-ml (verificada em 7/10/2026). A fonte é identificada, portanto não há invenção.

Ocorrências do mesmo trecho "O F4 afirma que":
- saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md, linha 366 (item 11 da seção de gabarito). É a única no canônico.
- saida/estudante/L4_gabarito.md, linha 58 (arquivo derivado, gerado pelo gerador a partir do canônico; corrige-se na regeneração, não à mão).
- No curso do L4 (5.2.5, linha 142 do canônico) o trecho NÃO é idêntico: lê-se "É o que afirma o F4: ...". Não é a frase da T-83; ver observação (b).

Onde se lê:
"O F4 afirma que "generative models are initially trained using an unsupervised approach" e que "the model is sometimes trained further using supervised or reinforcement learning"; o item descreve o pré-treino como "sem rótulos atribuídos manualmente", sem classificar o "auto-supervisionado"."

Leia-se:
"A página "Introduction to ML: What is Machine Learning?", do Google for Developers, afirma que "generative models are initially trained using an unsupervised approach" e que "the model is sometimes trained further using supervised or reinforcement learning"; o item descreve o pré-treino como "sem rótulos atribuídos manualmente", sem classificar o "auto-supervisionado"."

Fundamento: Y1 da D1 da T-81 e D-T81-05 (código interno de fonte F4 em texto que chega ao estudante). A fonte nomeada preserva a proveniência; as duas citações literais, o gabarito C, "v3 (O10)", [TS] (não há) e o resto da justificativa ficam intactos.

Observações:
(a) A mesma justificativa termina com "Fonte: F4, reverificado em 7/10/2026." Esta frase NÃO foi tocada, por estar fora da frase indicada; o código F4 permanece ali (e em dezenas de outras linhas do lote: 7, 8, 9, 10, curso e pares). Se a Gerência quiser eliminar o código na camada do estudante, é decisão de outra natureza (regra de fonte no gerador ou errata ampla), não esta errata.
(b) Curso 5.2.5 (linha 142), se a Gerência quiser coerência local: "É o que afirma o F4:" poderia ser "É o que afirma a página do Google for Developers sobre ML (F4):" — NÃO proposto como errata, apenas registrado; a T-83 limita-se à frase da justificativa.

## Erratum 2 — 5C-08, justificativa (aceita)

Ocorrências de "É o item deste lote mais próximo de um canônico (A5-20)":
- saida/gcb/GCB_Lote5C_v1_GCB-CPP.md, linha 48 (fim da justificativa do 5C-08). Canônico.
- saida/estudante/L5_gabarito.md, linha 151 (derivado; regenerar).
- Derivados antigos (gerador_v1_3 a v1_7, out/estudante/L5C_gabarito.md e out/pacote.json; saida/pacote/pacote.json e pacote_estudante.json): são saídas geradas de versões anteriores, não canônicas; não se corrigem à mão.

Onde se lê:
"É o item deste lote mais próximo de um canônico (A5-20): o ponto de julgamento é outro instrumento, mas o princípio, dirigir a atenção, é o mesmo."

Leia-se:
"É, entre os itens 5C, o mais próximo do item A5-20: o ponto de julgamento é outro instrumento, mas o princípio, dirigir a atenção, é o mesmo."

Fundamento: após a fusão na v1.8 o 5-C é apresentado dentro do Lote 5; "deste lote" e "canônico" (por oposição a complementar) perdem o referente (T81_reconciliacao, linhas 65 e 68). A redação proposta tira a oposição lote/canônico, mantém a referência a A5-20 e o raciocínio (outro instrumento, mesmo princípio). Frase anterior ("Difere do item A5-20 porque aquele julga cor de destaque e anotações; este julga o título.") fica intacta e é coerente.

Observação: a linha 52 do canônico 5-C ("Os itens 5C-01 a 5C-10 não alteram o Lote 5 v3.1" e "Nenhum repete o ponto de julgamento dos itens A5-08 a A5-13...") é nota de produção, fora do escopo.

## Encaminhamento
Se aceita pela gcb-gerencia (gatilho A da errata), é absorvida na próxima ocorrência da T-12 (itens só de forma não abrem versão); os derivados em saida/estudante/ são regenerados pelo gerador, não editados.
