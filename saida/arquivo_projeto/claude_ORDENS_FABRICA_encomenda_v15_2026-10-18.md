# Ordens à Fábrica — encomenda da v15 (18/10/2026)

Origem: encomenda do Fundador na passagem de bastão da v15 (claude/REGISTRO_v15_previa_2026-10-18.md, itens a–f), registrada pela sessão de design da plataforma (DPE-01). Esta sessão não decide matéria reservada; só registra e formata as ordens.

Atualizado em 18/10/2026 (noite) com as decisões do Fundador: piloto visual confirmado (ordem E deixa de aguardar), nova ordem F (banco de 40), item f resolvido. Entrega: o Fundador cola as ordens direto na sessão da Fábrica no Claude Code (formato FAB-AUTO v1, claude/FABRICA_Protocolo_Autonomia_v1.md, seção 9: um bloco por ordem, equivalente a `ordens/ORDEM_*.md`).

Pacote de referência: F4 v1.9 embutido nas prévias v14/v15 (334 itens, 10 lotes; pacote.json sha256 6cace34e46d1d9d6…).

| Ordem | Item da encomenda | Classificação | Pode rodar sem novo "sim"? |
|---|---|---|---|
| ORDEM_V15_C_LIMPEZA | c) referências de produção | AGORA | Sim (pedido expresso do Fundador) |
| ORDEM_V15_D_L2R16 | d) reclassificar L2-R16 | AGORA | Sim |
| ORDEM_V15_B_PARES | b) pares → pegadinhas | PRÓXIMO (depois de C) | Sim |
| ORDEM_V15_A_RESUMOS | a) resumo por tópico | PRÓXIMO (depois de C) | Sim, mas a ordem dos tópicos precisa de decisão (ver ordem) |
| ORDEM_V15_E_PILOTO_VISUAL | e) piloto de curso visual | AGORA | Sim (confirmado pelo Fundador em 18/10, noite: P2-1.4, P2-2.5, P1-8.2) |
| ORDEM_V15_F_BANCO40 | f) meta do banco por tópico | AGORA para a projeção; produção em ondas | Sim (meta decidida pelo Fundador em 18/10, noite); gasto das ondas segue matéria do Fundador |

Regras comuns a todas: a nota da plataforma conta só questões distintas (decisão de 18/10, noite; prévia v15.2); produção em Sonnet e QA em Opus, subagentes distintos (quem produz não revisa); máximo de 2 rodadas de QA; ids e gabaritos inalterados, exceto o que a ordem D pede; nenhuma publicação na plataforma da candidata; o pacote de saída ganha número novo da Fábrica (a numeração que vale é a da Fábrica) e um registro de alterações por id.

---

## ORDEM_V15_C_LIMPEZA.md

```
ORQUESTRADOR: LOTE
REMETENTE: Fundador (encomenda de 18/10/2026, item c), registrada pela sessão DPE-01
DESTINATÁRIO: EXEC (Fábrica)
PROMPT:
a) Objeto: retirar do texto que a candidata lê (curso, resumo, pegadinhas e justificativas de todos os lotes) as referências de produção; produção + QA (máx. 2 rodadas).
b) Gerência titular: GCE (lotes 1, 1-C, 2, 3) e GCB (lotes 4, 4-C, 5, 5-C, 6a, 6b).
c) Escopo: as 10 categorias do inventário anexo (INVENTARIO_marcas_producao_v1.9_2026-10-18.md): "Lote N"/"neste lote"/"do lote" no sentido de lote de produção; códigos de item (6A-02, L2-Q06, A5-10…); códigos de par (par C14); etiquetas [V data — Fx], [NORMATIVO — QA…], [F12]; códigos de fonte F1…F22 e N1…N6 no texto; prefixos TC/IC/GI/AT das justificativas; menções a QA, produção, errata e versão (v2); instruções internas ("Só o fato e a fonte", "SEM ITEM", "NÃO GABARITO", "não cobrar…").
d) Arquivos-base: pacote F4 v1.9; estado/Estado_Canonico_Camara_2026.md; o inventário anexo.
e) Regras específicas:
   1. NÃO trocar o termo técnico "lote" (transcrição em lote/batch) nem a tecla F4 do Excel (tópico 1 de TI).
   2. Fonte: trocar o código pelo nome da fonte por extenso quando ele estiver identificado no lote (ex.: "Cartilha de Segurança para Internet", "documentação da Microsoft"); manter "verificado em DD/MM/AAAA" em texto corrido. Base legal fica (lei, artigo, inciso).
   3. Frases "Difere do item X porque…" são nota de deduplicação do QA: sair do texto da candidata (podem ir para um campo interno, se a Fábrica quiser guardar).
   4. Prefixo TC/IC/GI/AT: reescrever como frase legível (ex.: "Armadilha: …") ou retirar, sem perder a explicação.
   5. Não alterar enunciado, gabarito, itemEdital nem o sentido das justificativas.
f) Saída: pacote novo (número da Fábrica), relatório de alterações por id/lote, parecer de QA; contagem final por categoria do inventário (meta: zero, salvo os falsos positivos da regra 1).
g) Classificação: AGORA
```

## ORDEM_V15_D_L2R16.md

```
ORQUESTRADOR: BANCO
REMETENTE: Fundador (encomenda de 18/10/2026, item d), registrada pela sessão DPE-01
DESTINATÁRIO: EXEC (Fábrica)
PROMPT:
a) Objeto: reclassificar o itemEdital de L2-R16; QA independente confirma ou recusa.
b) Gerência titular: GCE.
c) Escopo: L2-R16 (AUTORAL, gabarito E). Enunciado trata da indexação temática do Banco de Discursos da Câmara pelo TECAD. Hoje: P2-2.8 ("Vocabulário técnico parlamentar e vocabulário adaptado"). Proposta do Fundador: P2-3.1 ("Aplicações de IA em parlamentos: transcrição de sessões, sumarização, indexação e busca"), marcada como "provável".
d) Arquivos-base: pacote F4 v1.9; edital (subitens 2.8 e 3.1 da disciplina de Fala); estado canônico.
e) Regras específicas: gabarito e texto inalterados; registrar a decisão e a razão; conferir efeito colateral: L2-R16 saiu do diagnóstico de 30 na revisão independente de 18/10 (troca por L2-R17), então o DIAG30 não muda; muda só a contagem de questões dos tópicos 2.8 e 3.1.
f) Saída: pacote novo com a alteração (ou registro da recusa), parecer de QA.
g) Classificação: AGORA
```

## ORDEM_V15_B_PARES.md

```
ORQUESTRADOR: LOTE
REMETENTE: Fundador (encomenda de 18/10/2026, item b), registrada pela sessão DPE-01
DESTINATÁRIO: EXEC (Fábrica)
PROMPT:
a) Objeto: converter os pares confundíveis em pegadinhas "não confunda A com B", cada uma com itemEdital; produção + QA.
b) Gerência titular: GCE (L1, L2, L3) e GCB (L4, L5, L6a, L6b).
c) Escopo: 139 pares no pacote v1.9 (L1 17, L2 22, L3 28, L4 20, L5 15, L6a 19, L6b 18). Formato atual: {"a","b","como"}, sem itemEdital.
d) Arquivos-base: pacote F4 v1.9 (campo lotes[].pares e lotes[].pegadinhas).
e) Regras específicas: saída no formato das pegadinhas existentes {"itemEdital","rotulo","texto"}; texto começando por "Não confunda A com B:" e dizendo a diferença em uma ou duas frases; não duplicar pegadinha que já existe no mesmo tópico (fundir quando for o mesmo ponto); o campo pares pode ficar no pacote para uso interno (a plataforma não o mostra desde a v15).
f) Saída: pacote novo, relatório (quantos pares viraram pegadinha, quantos foram fundidos, quantos descartados e por quê), parecer de QA.
g) Classificação: PRÓXIMO (rodar depois da ORDEM_V15_C)
```

## ORDEM_V15_A_RESUMOS.md

```
ORQUESTRADOR: LOTE
REMETENTE: Fundador (encomenda de 18/10/2026, item a), registrada pela sessão DPE-01
DESTINATÁRIO: EXEC (Fábrica)
PROMPT:
a) Objeto: resumo por tópico do edital, no campo pacote.topicos["<id>"].resumo (ex.: pacote.topicos["P2-1.4"].resumo); produção + QA.
b) Gerência titular: GCE (P2) e GCB (P1).
c) Escopo: os 40 tópicos que têm curso na prévia (das 41 linhas com questões: 38 subitens-folha e os itens-pai 2, 4 e 5 de TI; o item 5 de TI não tem curso). Hoje há 7 resumos por lote, sem divisão por tópico.
d) Arquivos-base: pacote F4 v1.9 (resumos e cursos por lote); prévia v15.2, que já lê pacote.topicos[id].resumo e mostra o resumo do tópico na aba Resumo.
e) Regras específicas: resumo derivado do curso do próprio tópico, sem fato novo; sem referências de produção (regras da ORDEM_V15_C); um parágrafo por ideia. Ordem "dos tópicos de maior peso": o peso provisório da plataforma NÃO diferencia os tópicos (cerca de 1,00 item por tópico em TI e 0,98 em Fala, porque o edital não informa itens por matéria). Até a Presidência dar outra ordem ou a estimativa de pesos por provas anteriores existir, sugestão: os 3 tópicos do piloto visual primeiro (P2-1.4, P2-2.5, P1-8.2; a ordem E também pede o resumo deles), depois P2 na ordem do edital, depois P1. Tamanho do resumo: PENDENTE COM O FUNDADOR (não há regra registrada); até a decisão, a Fábrica pode propor um tamanho no relatório, sem tomá-lo como regra.
f) Saída: pacote novo com o objeto "topicos", relatório por tópico, parecer de QA.
g) Classificação: PRÓXIMO (rodar depois da ORDEM_V15_C)
```

## ORDEM_V15_E_PILOTO_VISUAL.md — confirmada em 18/10/2026 (noite)

```
ORQUESTRADOR: LOTE
REMETENTE: Fundador (encomenda de 18/10/2026, item e), registrada pela sessão DPE-01
DESTINATÁRIO: EXEC (Fábrica)
PROMPT:
a) Objeto: piloto de curso visual em 3 tópicos, dois de Fala e um de TI (confirmado pelo Fundador em 18/10/2026). Sugestão enviada pelo Fundador: P2-1.4 (Diarização de falantes: identificação e separação de múltiplos oradores), P2-2.5 (Normalização de texto: números, siglas, abreviações e termos técnicos) e P1-8.2 (Tipos de gráficos: histograma, linha, barra, dispersão, box plot).
b) Gerência titular: GCE e GCB; peças gráficas que precisarem de desenho seguem CDJ → CII.
c) Escopo: formato
   "topicos": {"P2-1.4": {"emUmMinuto":[...], "resumo":"...", "visuais":[{"tipo":"fluxo"|"tabela"|"linha"|"esquema"|"barras", ...}]}}
   fluxo: titulo, passos[]; tabela: titulo, colunas[], linhas[[]], legenda; linha: titulo, marcos[{quando,texto}]; esquema: titulo, centro, ramos[]; barras: titulo, dados[{rotulo,valor}], unidade, fonte.
   O 1.4 já tem demonstração no código da prévia (TOPICOS_DEMO), feita só com frases do curso e do resumo; o objeto que a Fábrica entregar substitui a demonstração. O 8.2 já tem uma figura (box plot anotado, SVG no código), que continua.
d) Arquivos-base: pacote F4 v1.9; prévia v15.2 (componentes já prontos e testados em 360 px, claro e escuro; tabela vira cartões no celular).
e) Regras específicas: todo dado de "barras" com fonte oficial e data; nada que não esteja no curso; sem referências de produção.
f) Saída: objeto "topicos" para os tópicos do piloto, parecer de QA.
g) Classificação: AGORA
```

## ORDEM_V15_F_BANCO40.md — nova em 18/10/2026 (noite)

```
ORQUESTRADOR: BANCO
REMETENTE: Fundador (decisão de 18/10/2026, noite, item 4), registrada pela sessão DPE-01
DESTINATÁRIO: EXEC (Fábrica)
PROMPT:
a) Objeto: levar o banco a 40 questões distintas por tópico nas duas matérias da plataforma (Tecnologia da Informação e Dados, da P1; Reconhecimento de Fala, Transcrição e Inteligência Artificial, da P2). Primeira entrega: projeção de prazo e de rodadas.
b) Gerência titular: GBQ (banco e proveniência), com GCE (Fala) e GCB (TI) para itens AUTORAL; QA independente.
c) Escopo e situação no pacote v1.9 (contagem desta sessão, 18/10/2026): 41 linhas do edital com questões (38 subitens-folha e os itens-pai 2, 4 e 5 de TI), 334 questões; máximo 26 (P2-4.1), mínimo 2 (P1-5); os 22 demais tópicos de Fala têm 6 cada. Para 40 em todas as 41 linhas faltam 1.306 questões (TI 544; Fala 762). Se os itens-pai 2, 4 e 5 de TI não tiverem meta própria, faltam 1.199. Esse ponto e o de contar ou não itens voláteis (fatos datados) dentro dos 40 não foram decididos: a projeção deve trazer os dois cenários.
d) Arquivos-base: pacote F4 v1.9; GBQ/banco.csv; estado canônico; regras de rótulo das Regras Comuns v2.1.
e) Regras específicas: rótulos CEBRASPE_OFICIAL, CEBRASPE_ANALOGA, OUTRA_OFICIAL ou AUTORAL (CEBRASPE_ESTILO proibido); questão real só de fonte oficial (cdn.cebraspe.org.br, sem espelho de terceiros); nenhuma duplicata de questão já existente (distinta = outro ponto de julgamento, não só outra redação); regras de lote da GCE para AUTORAL (8 a 12 C em 20; no máximo 4 dependentes de produto por lote); sem referências de produção no texto (ordem C). A meta de 20 por item-folha nas demais matérias (Direito Administrativo etc.) continua como estava.
f) Saída: (1) projeção: questões a produzir por tópico, número de ondas, prazo provável e estimativa de custo por onda, para decisão do Fundador; (2) depois, ondas de produção no ciclo contínuo, cada uma com pacote novo e parecer de QA.
g) Classificação: AGORA para a projeção; as ondas de produção seguem a decisão de gasto do Fundador.
```

## Item f — RESOLVIDO em 18/10/2026 (noite)
Meta: 40 questões distintas por tópico nas duas matérias da plataforma (ordem F); 20 por item-folha nas demais matérias; prazo a projetar. A nota conta só questões distintas (prévia v15.2, CONTA_REPETIDAS=false); hoje nenhum tópico chega à nota.

## Entrega à Fábrica
O Fundador cola as ordens C, D, B, A, E e F direto na sessão da Fábrica no Claude Code. Esta sessão não grava na pasta da Fábrica.
