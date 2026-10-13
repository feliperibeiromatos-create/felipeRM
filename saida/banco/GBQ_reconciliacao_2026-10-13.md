# GBQ_reconciliacao_2026-10-13.md — T-29, T-42, T-36, T-37, T-38, T-43, T-40 (reconciliação única) — 2026-10-13 — gerado por gbq-gerencia

## 0. Objeto, base e limites

- Reconciliação única, em D1, das tarefas T-29 + T-42 (D-SCHEMA-02-EXEC), T-36, T-37, T-38 + T-43 (com as dúvidas da seção "Regras da v1.2" do contrato) e T-40.
- Decisões de entrada lidas em DECISOES.md: D-PACOTE-V11 (gatilho A do pacote v1.1 aceito; D1-a/b/c ratificadas), D-T12-V12 (pacote v1.2 pela T-12, ocorrência T-48), D-SCHEMA-02-EXEC (colunas de comando e texto-base) e D-FUNDADOR-DELEGA-1. Resumo do gatilho A da GBQ no Projeto: cópia de trabalho do orquestrador (scratchpad s4/gbq_gatilhoA_v11.md), lida como dados.
- Arquivos alterados pela GBQ nesta reconciliação (aplicação de D1, cada uma conferida por script; cópias de antes em scratchpad s4/gbq_rec/):
  - banco/banco.csv: T-40 na coluna observacoes de 6 linhas e coluna nova `aderencia` ao final (seções 5 e 6).
  - banco/SCHEMA.md: R-1 da gbq-cqe e descrição da coluna `aderencia`.
  - saida/simulados/simulado_0_v0.2.md: errata de forma do Aviso 6 (uma linha).
  - regras/pacote_contrato.md: seção "Regras da v1.2" passa de proposta a decidida (D1), com as regras (a) a (j); frase de abertura ajustada.
- Não toquei em TAREFAS.md, PARA_PRESIDENCIA.md, DECISOES.md nem estado/. Sem git.
- SHA-256 finais: banco/banco.csv b0906e1d…7300ea (antes 6ce6d5ec…8d87, que é o "depois" da T-29); banco/SCHEMA.md 8f758f98…3a83; regras/pacote_contrato.md d8ab26b6…5b56; regras/estilo_banca.md 530c580d…2517 (igual ao "depois" da T-37); simulado_0_v0.2.md 03db759d…2874; simulado_0_v0.2_gabarito.md e4cff206…39c3 (não alterado nesta reconciliação).
- Separação de funções: as aplicações da GBQ são mecânicas (texto do QA copiado, coluna derivada por regra fixa, frase de aviso sem conteúdo novo de item) e a T-48 traz conferência independente da gbq-cqe sobre elas (seção "INSTRUÇÕES PARA A T-48", itens 1 e 11).

## 1. T-29 + T-42 — colunas texto_comando e texto_base (D-SCHEMA-02-EXEC)

Produção: saida/banco/schema02_2026-10-13.md (gbq-csc). QA: saida/banco/QA_schema02_2026-10-13_gbq-cqe.md (gbq-cqe), APROVADO COM RESSALVAS.

Conferido na reconciliação:
- banco/banco.csv aprovado sem correção pela gbq-cqe: 15 colunas antigas idênticas em 112/112; ids e ordem idênticos; formato preservado (LF, sem BOM, QUOTE_MINIMAL, roundtrip byte-idêntico); texto_comando literal em 112/112 contra os 19 cadernos de cdn.cebraspe.org.br (script independente 105/112 exato + 7 conferidos à mão); amostra de 32 linhas cobrindo os 19 cadernos, 32/32 OK; varredura dos 50 grupos de comando: 0 texto-base omitido; texto_base preenchido só em BQ-0049 a 0051 (373 caracteres, exato).
- Comando dos 60 itens do pacote v1.1: 60/60 idêntico (produção, conferência (c)).

Decisões (D1):
- (1-a) **R-1 aplicada pela GBQ** em banco/SCHEMA.md, com o texto exato da gbq-cqe: "(o pacote exporta o vazio como "nenhum")" → "(o pacote v1.1/v1.1.1 exporta o vazio como "nenhum"; a partir da v1.2, como "" — F2, D-T12-V12)". Só o parêntese mudou nessa linha.
- (1-b) **Convenção de BQ-0070, 0071 e 0112 mantida**: a situação hipotética que está na própria frase do comando fica inteira em texto_comando, e texto_base fica vazio. Motivos da gbq-cqe acolhidos: o caderno não tem bloco de texto-base distinto; separá-lo exigiria cortar uma frase do caderno ou redigir texto novo.
- (1-c) A cautela da gbq-cqe para a T-48 vira regra do contrato: a normalização do comando nunca retira premissa (regra (h) da v1.2; seção 4).
- (1-d) O-1 (a produção conferiu BQ-0067..0112 contra observacoes, fonte interna) fica suprida pela conferência independente da gbq-cqe contra o PDF (46/46). Sem providência.
- (1-e) Os 46 itens BQ-0067 a BQ-0112 deixam de esperar as colunas (regra 3 do contrato v1.1): com gabarito C/E, entram no pacote v1.2 (T-48), observada a seção 5 para os 6 da T-40.

Estado: T-29 CONCLUÍDA; T-42 CONCLUÍDA.

## 2. T-36 — ajuste mecânico do Simulado 0 v0.2 pós-T-13/T-21

Produção: saida/simulados/T36_2026-10-13.md (gbq-csc), conferência por script TUDO OK.

Conferido na reconciliação (script próprio, só leitura): nota de vigência presente uma vez abaixo do Comando 15; 16 linhas do mapa com "T-13: gabarito mantido (qa_normativo_lgpd_2026-10-10.md)" e 0 com "T-13 (qa-normativo"; item 51 com "T-21: gabarito mantido"; "Ajuste T-36" em Marcas de montagem; mapa 60 linhas, gabarito = banco 60/60, 33 C/27 E; texto da folha = texto_integral do banco 60/60.

Decisões (D1):
- (2-a) **16, não 17.** A contagem certa é 16: o 17.º item da T-13, BQ-0031, é anulado e está fora do simulado (D1 da GBQ: anulados não entram em simulado; reconciliação lote1, seção 8). A redação "17 itens LGPD presentes no simulado" da linha da T-36 fica superada por esta decisão; a produção agiu corretamente.
- (2-b) **Aviso 6 da folha: errata de forma aplicada agora pela GBQ.** Única mudança (linha 15 de saida/simulados/simulado_0_v0.2.md):
  - de: "16 desses itens aguardam a conferência do qa-normativo (T-13); o gabarito segue o definitivo do certame de origem."
  - para: "16 desses itens passaram pela conferência do qa-normativo (T-13, 10/10/2026), com gabarito mantido diante do texto vigente; o gabarito segue o definitivo do certame de origem."
  - Conferência por script: 465 linhas antes e depois; só a linha 15 difere; prefixo e frase final da linha intactos; 0 ocorrência de "aguardam a conferência" na folha. Item, ordem, numeração, comando, texto e gabarito inalterados. Fonte do fato: saida/banco/qa_normativo_lgpd_2026-10-10.md (17/17 MANTIDO).
  - A frase foi escrita por quem reconcilia; a gbq-cqe a confere na T-48 (instrução 11).
- (2-c) Cabeçalhos dos dois arquivos mantidos (decisão de forma da produção, aceita); o registro do ajuste fica na linha "Ajuste T-36" do gabarito e nesta reconciliação. A versão do simulado continua "v0.2" (regra (e) da v1.2: ajuste de forma não muda versão).
- (2-d) A liberação do SIM-0 à candidata segue reservada ao Fundador (exceção mantida em D-FUNDADOR-DELEGA-1).

Estado: T-36 CONCLUÍDA.

## 3. T-37 — regras/estilo_banca.md v1.1.1 → v1.1.2

Produção: saida/banco/T37_estilo_v1_1_2_2026-10-13.md (gbq-estilo), script APROVADO: diff só no cabeçalho e nos pontos (1) a (5); 12 contagens de padrão iguais (27 E/33 C); seções 2, 4, 5, 3.13, tabela histórica v1.0 → v1.1 e registro v1.1 → v1.1.1 idênticos; C5 continua INDÍCIO. SHA-256 do arquivo atual = "depois" do relatório (530c580d…2517).

Decisões (D1) sobre os resíduos apontados pela produção:
- (3-a) **AVISO final mantido como está.** "apta a orientar produção após os ajustes 1–3 (aplicados nesta v1.1.1, T-23)" é registro histórico verdadeiro: os ajustes 1–3 foram aplicados na v1.1.1, e a v1.1.2 não mexe na classificação. Sem errata.
- (3-b) **3.2 (E2, nota de BQ-0056, linha 117) e 3.8 (C2, linha 245)** ainda remetem à T-13 como pendente. São erratas de forma sem efeito em padrão, contagem ou recomendação, fora do escopo literal da T-37. Vão para tarefa nova PRÓXIMO (v1.1.3), que não bloqueia a T-48 (BLOCO TAREFAS, primeira linha), com textos de substituição fixados:
  - linha 117: "O texto vigente da definição na LGPD fica com o qa-normativo (T-13)." → "Vigência conferida pelo qa-normativo na T-13: gabarito mantido (10/10/2026; saida/banco/qa_normativo_lgpd_2026-10-10.md)."
  - linha 245: "A proximidade com o texto vigente não foi conferida por artigo e fica com o qa-normativo (T-13)." → "Vigência conferida por artigo pelo qa-normativo: BQ-0006, BQ-0024 e BQ-0037 na T-13 e BQ-0036 na T-21, gabaritos mantidos (10/10/2026; saida/banco/qa_normativo_lgpd_2026-10-10.md e qa_normativo_marco_civil_cnj_2026-10-10.md)."

Estado: T-37 CONCLUÍDA.

## 4. T-38 + T-43 — contrato v1.1.1 e decisões da v1.2

Produção: regras/pacote_contrato.md v1.1.1 e saida/pacote/contrato_v1_1_1_2026-10-13.md (gbq-csc), script TUDO OK: exemplo JSON parseia; versao 1; 14 campos obrigatórios do item iguais; regra 2 só com a frase "sem distinção de maiúsculas e minúsculas"; exemplo de BQ-0001 sem volatil e com aderencia "parcial"; campo opcional `nota` (regras 3 e 4) com as notas literais de BQ-0003 e BQ-0040, conferidas com o banco.

T-38 e T-43 aceitas como produzidas. Decisões (D1) sobre as dúvidas da v1.2, gravadas no contrato (seção "Regras da v1.2 (D-T12-V12; decidida pela GBQ, D1, 13/10/2026; vigora a partir da T-48)"):

- (4-a) **`versao` do JSON continua 1**, com `nome` "Câmara 2026 — pacote F4 (v1.2)" (regra (g)). Motivo: as regras (b) e (d) mudam o valor de campos existentes, não o nome, o tipo nem a obrigatoriedade; todos os campos novos são acréscimos; um leitor da v1.1.1 lê a v1.2. `versao` 2 fica reservada para mudança que quebre leitor (campo obrigatório novo, renomeado, retirado ou com tipo trocado).
- (4-b) **Aderência explícita (D1-b): coluna nova `aderencia` ao final de banco/banco.csv, executada agora pela GBQ** (seção 6), preenchida pela regra 2 do contrato (sem distinção de caixa) a partir de observacoes. O pacote v1.2 lê a coluna sem inferência (regra (c)). A T-48 não recalcula a aderência; só a exporta e a confere.
- (4-c) **`rotulo` de cada pegadinha (F3)** (regra (d)): o objeto da pegadinha, como trecho literal do arquivo canônico do lote, a saber o título do bloco ou subseção que contém a linha "Pegadinha"/"Pegadinha provável" (ex.: "Histograma", "Box plot (diagrama de caixa)"), sem numeração inicial e sem marcas internas; sem bloco próprio, o texto do subitem no edital/*.md. Desdobramento só nas fronteiras que o texto canônico marca (";" fora de parênteses e aspas, enumeradores "(1)", "(2)"…, marcadores de lista); fragmento literal; texto corrido que não se separa sem reescrever fica em uma entrada e é listado no relatório.
- (4-d) **Normalização do comando (D1-c)** (regra (h)): só o comando com faixa ou lista de numeração de itens ("julgue os itens de 1 a 6.", "julgue os itens de 4C-01 a 4C-10.", "julgue os itens A5-05 a A5-07.") troca apenas a numeração: "julgue os itens [de] X a Y." → "julgue os itens a seguir."; o resto da frase fica literal; o literal vai em `comandoOriginal`. Premissa, situação hipotética, lei, IP, quartis ou outro dado no comando nunca é retirado (BQ-0070, 0071 e 0112 saem com o comando inteiro, sem `comandoOriginal`). Comando sem faixa sai literal, sem `comandoOriginal`.
  - Simulação sobre o pacote v1.1: 90 itens casam a regra (L4 20, A5 20, 4C 10, 5C 10, 6A 15, 6B 15); 0 item de banco; 0 linha do banco (texto_comando, 112) casaria a regra.
- (4-e) **`nota` com o rótulo "nota de vigência:" no valor** (regra (i)), literal, como a regra 4 da v1.1.1 já manda; nenhuma edição. A edição do estudante exibe a nota literal junto do item.
- (4-f) **Simulados** (regra (e)): `versao` = a versão do cabeçalho (Simulado 0: "v0.2"); sem versão declarada, "v1" (Simulados 1, 2 e 0-P2); ids "SIM-0", "SIM-1", "SIM-2", "SIM-0-P2"; ajuste de forma não muda versão.
- (4-g) Regra (j): o PROMPT DE PARTIDA do contrato se lê, na T-48, com as regras da v1.2 onde conflitarem.

Conferência por script do contrato (scratchpad s4/gbq_rec/confere_contrato_saida.txt):
```
OK exemplo JSON idêntico (parse) e versao = 1
chaves do item: ['id', 'rotulo', 'certame', 'cargo', 'ano', 'numero', 'comando', 'textoBase', 'enunciado', 'gabarito', 'justificativa', 'itemEdital', 'aderencia', 'url']
blocos alterados (linhas antes -> depois): [('replace', 3, 3, 3, 3), ('replace', 61, 61, 61, 61), ('replace', 63, 63, 63, 63), ('replace', 65, 69, 65, 72), ('replace', 71, 71, 74, 77)]
OK nenhuma alteração fora da linha 3 e da seção v1.2: []
OK presente: Regras da v1.1 (T-26): / Regras da v1.1.1 (T-38, T-43): / tabela de fonte | L1 | / PROMPT DE PARTIDA
OK seção marcada como decidida
OK regras (a)-(j) presentes
regra (h) no pacote v1.1: normalizados 90 {'L4': 20, '4C': 10, 'A5': 20, '5C': 10, '6A': 15, '6B': 15}
OK nenhum item de banco normalizado []
OK nenhuma linha do banco (112, texto_comando) casaria a regra (h) []
```
Nenhum campo obrigatório muda: os 14 campos obrigatórios do item, as chaves de topo e as estruturas de edital, lotes, simulados e discursivas do exemplo estão idênticos; as regras da v1.1 e da v1.1.1 e a tabela de fonte por lote não foram tocadas.

Estado: T-38 CONCLUÍDA; T-43 CONCLUÍDA (a exportação de `nota` é da T-48).

## 5. T-40 — QA normativo dos 6 itens normativos da terceira varredura

Relatório: saida/banco/qa_normativo_T07_2026-10-13.md (qa-normativo): 6/6 SUSTENTA (BQ-0072 C, BQ-0077 C, BQ-0084 C, BQ-0109 C, BQ-0110 E, BQ-0111 C); 0 divergência; 0 gatilho D; fontes planalto.gov.br abertas em 13/10/2026; Lei 15.352/2026 sem efeito nos dispositivos decisivos.

Decisões (D1):
- (5-a) **Substituição em observacoes aplicada agora pela GBQ**, nas 6 linhas, pelos textos literais do relatório (tabela "Recomendação para a coluna observacoes"); o restante de cada célula ficou como estava.
- (5-b) BQ-0110: o segmento já existente "QA de banco T-07: art. 4º, III, a e b, e §§ 1º a 3º sem alteração pela Lei 15.352/2026 (verificado em 2026-10-10)" fica (compatível com a T-40; mudança mínima).
- (5-c) **Nota de vigência de BQ-0110: nenhuma no pacote.** O enunciado não cita a autoridade nacional; item de banco tem `justificativa` vazia; o campo `nota` só leva texto rotulado "nota de vigência:" (regra 4 da v1.1.1), e o texto novo de observacoes não traz esse rótulo. A identificação da ANPD fica registrada em observacoes.
- (5-d) **Entrada no pacote v1.2:** os 6 entram na T-48 (gabarito C/E, QA normativo concluído, colunas de comando presentes, 0 "QA PENDENTE").
- (5-e) **BQ-0072 e BQ-0111: aderência DIRETA confirmada; aptos a simulado final futuro.** BQ-0072 → P1-6 ("Ética e responsabilidade digital no serviço público": dever ético de usar os recursos técnicos disponíveis, inclusive IA, no serviço público; o comando delimita a norma, e o item se julga por ela). BQ-0111 → P1-4 ("Conceitos gerais de segurança e governança digital": princípios e diretrizes do Governo Digital, Lei 14.129/2021). Ambos sem VOLÁTIL e sem QA PENDENTE. Entram em simulado final pelas regras de montagem (equilíbrio C/E, cobertura, sem repetição); nenhum simulado atual muda por isso.
- (5-f) **BQ-0077, 0084, 0109 e 0110: PARCIAL (P2-4.1), só simulado diagnóstico** (D-ADERENCIA).
- (5-g) **Reverificação normativa de janeiro:** acolhida a recomendação do qa-normativo; tarefa datada nova (BLOCO TAREFAS, segunda linha) para os 25 itens de fonte normativa do banco (17 da T-13, 2 da T-21, 6 da T-40), na janela de D-REVERIFICACAO-JAN.

Estado: T-40 CONCLUÍDA.

## 6. D1-b — coluna `aderencia` no banco (executada pela GBQ)

- Coluna `aderencia` acrescentada ao final de banco/banco.csv (depois de texto_base), "direta" ou "parcial" em 112/112 linhas, inclusive as 6 anuladas, calculada pela regra 2 do contrato (observacoes contendo "parcial", "aderência temática ampla" ou "aderência apenas por tema", sem distinção de caixa → "parcial"; senão "direta") sobre observacoes já com a T-40.
- Ordem de aplicação (scratchpad s4/gbq_rec/aplica_banco.py): roundtrip prévio byte-idêntico → T-40 nas 6 células → coluna nova → gravação com csv.writer (delimiter=';', lineterminator='\n', QUOTE_MINIMAL). Roundtrip do arquivo final também byte-idêntico; 0 CR; sem BOM; termina em LF.
- banco/SCHEMA.md descreve a coluna: fonte da aderência daqui em diante; linha nova traz o valor arbitrado pela GBQ; mudança de aderência muda a coluna e registra o motivo em observacoes.

Conferência por script (scratchpad s4/gbq_rec/confere_banco.py; saída literal):
```
OK    cabeçalho = antigo + aderencia ao final
OK    linhas 113 / 113
OK    todas as linhas com 18 campos
OK    só observacoes das 6 linhas T-40 mudou: [('BQ-0072', 'observacoes'), ('BQ-0077', 'observacoes'), ('BQ-0084', 'observacoes'), ('BQ-0109', 'observacoes'), ('BQ-0110', 'observacoes'), ('BQ-0111', 'observacoes')]
OK    BQ-0072 só o trecho T-40 trocado (prefixo e sufixo intactos)
OK    BQ-0077 só o trecho T-40 trocado (prefixo e sufixo intactos)
OK    BQ-0084 só o trecho T-40 trocado (prefixo e sufixo intactos)
OK    BQ-0109 só o trecho T-40 trocado (prefixo e sufixo intactos)
OK    BQ-0110 só o trecho T-40 trocado (prefixo e sufixo intactos)
OK    BQ-0111 só o trecho T-40 trocado (prefixo e sufixo intactos)
OK    0 "aguarda qa-normativo (T-40)" no banco
OK    0 "QA PENDENTE" nas 6 linhas
OK    valores {'parcial': 40, 'direta': 72}
OK    aderencia = pacote v1.1: 60/60
OK    60 do pacote: {'parcial': 23, 'direta': 37}
OK    declaração explícita em observacoes = coluna (incoerências: [])
OK    aderencia = mapa do SIM-0 v0.2: 60/60
OK    T-40: {'BQ-0072': 'direta', 'BQ-0077': 'parcial', 'BQ-0084': 'parcial', 'BQ-0109': 'parcial', 'BQ-0110': 'parcial', 'BQ-0111': 'direta'}
OK    "nota de vigência:" só em ['BQ-0003', 'BQ-0040']
total 112: {'parcial': 40, 'direta': 72} | BQ-0067..0112: {'parcial': 16, 'direta': 30}
RESULTADO: TUDO OK
```
- Contagens: 112 linhas = 72 direta/40 parcial; os 60 do pacote v1.1 = 37/23 (17 P2-4.1, 2 P1-8.3, 1 P1-5.3, 1 P1-6, 1 P1-7.1, 1 P1-8.1, como no gatilho A); BQ-0067..0112 = 30/16; os 6 anulados também têm valor (fora do pacote).

## 7. Gatilhos

Nenhum. Tudo foi decidido em D1 no domínio da GBQ, dentro das ordens do Fundador (D-SCHEMA-02-EXEC, D-PACOTE-V11, D-T12-V12). Nenhum gabarito mudou; não houve divergência normativa (gatilho D) nem conflito entre Gerências. O gatilho A da v1.2 sai depois da T-48. A liberação de qualquer material à candidata segue reservada ao Fundador.

## 8. Estado final proposto

- T-29: CONCLUÍDA
- T-42: CONCLUÍDA
- T-36: CONCLUÍDA
- T-37: CONCLUÍDA
- T-38: CONCLUÍDA
- T-40: CONCLUÍDA
- T-43: CONCLUÍDA

Efeito na T-48: com estas conclusões, das condições da T-48 faltam só T-44, T-46 e T-47 (GCE/GCB). T-37 e T-40 estão concluídas; da T-40 entram os 6 itens.

## BLOCO PARA_PRESIDENCIA

nenhum

## BLOCO TAREFAS

T-?; GBQ; Errata de forma de regras/estilo_banca.md v1.1.2 → v1.1.3 (D1 GBQ, saida/banco/GBQ_reconciliacao_2026-10-13.md, seção 3 (3-b)), sem mudar padrão, contagem de padrão ou recomendação: (1) 3.2 (E2), linha 117 (nota de BQ-0056): "O texto vigente da definição na LGPD fica com o qa-normativo (T-13)." → "Vigência conferida pelo qa-normativo na T-13: gabarito mantido (10/10/2026; saida/banco/qa_normativo_lgpd_2026-10-10.md)."; (2) 3.8 (C2), linha 245: "A proximidade com o texto vigente não foi conferida por artigo e fica com o qa-normativo (T-13)." → "Vigência conferida por artigo pelo qa-normativo: BQ-0006, BQ-0024 e BQ-0037 na T-13 e BQ-0036 na T-21, gabaritos mantidos (10/10/2026; saida/banco/qa_normativo_lgpd_2026-10-10.md e qa_normativo_marco_civil_cnj_2026-10-10.md)."; (3) seção 7: subseção "v1.1.2 → v1.1.3"; cabeçalho v1.1.3; AVISO final inalterado; conferência por script (diff só nesses pontos; 12 contagens iguais); não bloqueia a T-48; PRÓXIMO; PENDENTE; gbq-estilo → gbq-gerencia; regras/estilo_banca.md v1.1.3 + saida/banco/T_estilo_v1_1_3_<data>.md
T-?; GBQ; Reverificação normativa de janeiro (4–8/1/2027, D-REVERIFICACAO-JAN) dos itens de fonte normativa do banco, por artigo e inciso, texto vigente no planalto.gov.br (CNJ: fonte oficial do CNJ), "verificado em [data]", sem mudar gabarito (divergência = gatilho D): 17 da T-13 (BQ-0002 a 0008, 0023, 0024, 0025, 0031, 0032, 0037, 0045, 0046, 0056, 0057), 2 da T-21 (BQ-0036, BQ-0040) e 6 da T-40 (BQ-0072, 0077, 0084, 0109, 0110, 0111), por recomendação do qa-normativo (qa_normativo_T07_2026-10-13.md) e por a LGPD ter sido alterada em 2026; complementa T-14, T-16 e T-41; PRÓXIMO (datado); PENDENTE; qa-normativo → gbq-gerencia; saida/banco/reverificacao_jan2027_normativa.md

## INSTRUÇÕES PARA A T-48

O que a gbq-csc faz na v1.2 em consequência destas decisões (contrato: regras/pacote_contrato.md, "Regras da v1.2", decidida em D1):

1. **Itens de banco.** Exportar BQ-0001 a BQ-0112 com gabarito C/E (anulados fora; 106 itens, 60 C/46 E, contra 60 na v1.1), inclusive os 6 da T-40. `comando` = coluna `texto_comando`; `textoBase` = coluna `texto_base`, ou `""` quando vazia (nunca "nenhum"). Conferir por script: 60/60 dos itens da v1.1 com o mesmo comando; 3 com textoBase não vazio (BQ-0049 a 0051).
2. **Aderência.** `aderencia` = coluna `aderencia` do banco, sem recalcular (contagem esperada nos 106 exportáveis: 67 direta/39 parcial; nos 60 da v1.1, 37/23). AUTORAL = "direta". Relatório com a contagem.
3. **`volatil`.** Como na v1.1 (regra 1), agora também para BQ-0075, 0076, 0086 e 0089 (VOLÁTIL em observacoes, T-41): 8 itens de banco com `volatil` (BQ-0015, 0017, 0035, 0064, 0075, 0076, 0086, 0089), contra 4 na v1.1.
4. **`nota`.** Só BQ-0003 e BQ-0040, valor = texto literal de observacoes a partir de "nota de vigência:", inclusive o rótulo. Nenhuma nota em BQ-0110 nem em outro item.
5. **Normalização do comando (regra (h)).** Aplicar só a comandos com faixa/lista de numeração de itens: "julgue os itens [de] X a Y." → "julgue os itens a seguir.", resto literal, original em `comandoOriginal`. Conferir: na base v1.1, 90 itens (L4 20, A5 20, 4C 10, 5C 10, 6A 15, 6B 15); qualquer diferença na v1.2 (por exemplo, Lote 4 v3.4) explicada item a item no relatório; 0 item de banco normalizado; BQ-0070, 0071 e 0112 com o comando inteiro e sem `comandoOriginal`; todo `comandoOriginal` difere do `comando` só no trecho da numeração.
6. **Pegadinhas (F3, regra (d)).** Uma por entrada, com `itemEdital`, `rotulo` e `texto`. `rotulo` = título literal do bloco/subseção do arquivo canônico do lote que contém a pegadinha (sem numeração inicial e sem marcas internas), ou o texto do subitem no edital quando não houver bloco. Desdobrar só em ";" fora de parênteses e aspas, em "(1)", "(2)"… ou em marcadores de lista; fragmento literal. Conferir por script: todo `rotulo` é trecho literal do arquivo canônico do lote ou do edital; a junção dos fragmentos reproduz cada entrada da v1.1 (salvo o ponto final); entradas por lote v1.1 → v1.2 no relatório; listar as entradas de texto corrido não desdobradas.
7. **Simulados (regra (e)).** Entradas SIM-0 ("v0.2", diagnóstico, com a T-36 e a errata do Aviso 6), SIM-1 ("v1", final), SIM-2 ("v1", final; D-SIM2-CANONICO) e SIM-0-P2 ("v1", diagnóstico; D-SIM0P2-DIAGNOSTICO), cada uma com `n` = tamanho de `itens`. Conferir `n`: 60, 40, 40 e 25.
8. **Topo.** `versao`: 1; `nome`: "Câmara 2026 — pacote F4 (v1.2)"; `itensEdital`, `pares` e `pegadinhas` sempre listas JSON.
9. **Demais itens da D-T12-V12** (Lote 4 v3.4; erratas da GCE nos Lotes 1, 2 e 3; T-44; F1, F4 e F5; Tukey/T-47; E12/T-46; edições do estudante), conforme a linha da T-48, sem relação com estas decisões.
10. **Validação.** JSON sem erro de parse; nenhum item sem id, enunciado e gabarito; 0 id duplicado; 0 "QA PENDENTE"; 14 campos obrigatórios de item presentes em todos; relatório saida/pacote/pacote_relatorio_2026-10-13.md com o diff de contagens v1.1 → v1.2.
11. **QA (gbq-cqe), além da fidelidade textual da D-T12-V12.** Conferir por script independente: (a) a coluna `aderencia` do banco contra a regra 2 do contrato e contra as declarações de observacoes (112/112), e a exportação contra a coluna; (b) as 6 células T-40 de observacoes contra a tabela do relatório do qa-normativo (texto literal); (c) a frase nova do Aviso 6 do SIM-0 contra saida/banco/qa_normativo_lgpd_2026-10-10.md (16 itens no simulado, gabarito mantido); (d) os pontos 5 e 6 acima (comandos e pegadinhas), com amostra de pegadinhas contra o arquivo canônico.
