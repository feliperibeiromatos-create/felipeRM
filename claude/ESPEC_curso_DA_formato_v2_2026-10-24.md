# Especificação do curso de Direito Administrativo na plataforma — formato v2

24/10/2026 · sessão Cowork, por ordem do Fundador ("pode seguir com a produção automática"), a partir do Dossiê Didático DAD v1 (Partes III e IV) e do plano DAD/PLANO_implementacao_Dossie_DAD_v1_2026-10-24.md.
Substitui a ESPEC v1 (19/10) para os lotes de Direito Administrativo produzidos a partir da ORDEM_DA_V2. Tudo da v1 que não é alterado aqui continua valendo (identificadores, quadros, visuais, regras de lei, o que o script recusa). Lotes de TI e de Fala não mudam.

## 0. O que muda em uma frase
A unidade deixa de ser "texto com quadros" e passa a ser "tarefa → mapa → glossário → caso → regra → pares → itens no meio → fechamento → verificação", com toda citação datada e sem nenhum trecho de material de terceiro (D-ESTRATEGIA).

## 1. Marcação de versão
- `lotes[].formato = "DA-v2"`. O script aplica as regras desta especificação só a lotes com essa marca; lotes antigos seguem na v1.
- `topicos[id].formato = "DA-v2"` nos tópicos que receberem os campos novos.

## 2. Abertura do tópico — `topicos["P1-DA-<n>"]`
```json
{"formato": "DA-v2",
 "tarefas": ["Dado um deslocamento de servidor, decidir se é remoção ou redistribuição e o que muda (pessoa, cargo, quadro).", "..."],
 "emUmMinuto": ["...", "...", "..."],
 "resumo": "...",
 "visuais": [ {"tipo": "esquema", ...}, {"tipo": "compare", ...} ],
 "fechamento": {"levar": ["...", "...", "...", "...", "..."],
                "literalidade": ["o que a banca cobra pela letra da lei (até 6)"],
                "caso": ["o que a banca cobra por situação hipotética (até 6)"]},
 "escopo": [{"tema": "Acumulação de cargos", "onde": "P1-DA-3.2"}]}
```
- `tarefas`: 3 a 6 frases, cada uma no formato "Dado X, decidir/dizer/calcular Y" (começa com "Dad" e contém um verbo de decisão). Até 220 caracteres. É o primeiro bloco que a candidata vê, antes de emUmMinuto.
- `visuais`: o primeiro visual é o mapa de chegada do tópico (esquema, linha, fluxo ou compare); a plataforma o repete no fechamento, preenchido só com o título "o que você já sabe".
- `fechamento.levar`: exatamente 5 frases de até 160 caracteres. `literalidade` e `caso`: listas de 1 a 6 textos curtos.
- `escopo`: o que o tópico declara que NÃO cobre e onde está; lista pode ser vazia, mas o campo existe.

## 3. Curso — `lotes[].curso` (texto), por subitem `## <número> <TÍTULO>`
Ordem obrigatória dentro de cada bloco de subitem:

| Ordem | Linha em maiúsculas | Vira | Regra |
|---|---|---|---|
| 1 | `GLOSSÁRIO` | lista de pares "termo — definição em uma linha" | 2 a 10 linhas no formato `Termo: definição`. Todo termo técnico usado no bloco antes da sua DEFINIÇÃO aparece aqui. Vem ANTES do primeiro parágrafo. |
| 2 | `CASO` | quadro de abertura com pergunta | situação concreta de 2 a 5 frases terminando em pergunta ("?"), sem resposta. Caso próprio, de preferência derivado de item real do banco. |
| 3 | (parágrafos) | texto | até 4 frases por parágrafo; uma representação por conceito (prosa OU esquema OU tabela) |
| 4 | `DEFINIÇÃO` | quadro amarelo | como na v1 |
| 5 | `BASE LEGAL` | quadro com barra | como na v1 (artigo, inciso, conferido) |
| 6 | `RESPOSTA DO CASO` | quadro cinza | fecha o CASO: a regra aplicada em até 3 frases |
| 7 | `EXEMPLO PARLAMENTAR` | quadro cinza | como na v1 |
| 8 | `ITEM <id>` | item C/E respondível, comentário oculto até a resposta | ver seção 4. Pelo menos 1 por bloco de subitem; recomendado 1 a cada 3 quadros |
| 9 | `PEGADINHA PROVÁVEL` | quadro com borda amarela | passa a ter três linhas fixas: `A: <termo A>` / `B: <termo B>` / `MUDA: <palavra ou dado que muda a resposta>` (D-PEGADINHA-UNICA) |

Marcações da v1 que continuam: tabela Markdown (até 4 colunas, cabe numa tela) e sequência `A → B → C` (3 a 7 etapas de até 48 caracteres).
Proibições: termo técnico antes da linha do GLOSSÁRIO que o define; o mesmo conteúdo em prosa E esquema E tabela; classificação listada como rótulos sem a pergunta que a distingue ("quantos órgãos manifestam vontade?" em vez de "simples/composto/complexo"); número sem norma e data; "recente" sem ano; qualquer texto, exemplo, tabela ou questão de curso de terceiro.

## 4. Item intercalado — `ITEM <id>`
- A linha `ITEM L-DA2-Q07` (um id por linha) manda a plataforma renderizar o item `itens[id]` dentro do curso: comando, enunciado, botões C/E, e, depois da resposta, o comentário em três linhas.
- O id precisa existir em `itens`, ter `itemEdital` do mesmo tópico, rótulo permitido e o campo `comentario` (seção 5). Item real (CEBRASPE_OFICIAL/ANALOGA) tem preferência; AUTORAL onde não houver real.
- Um item intercalado não entra no bloco de verificação do mesmo tópico (sem duplicata teoria × verificação) nem em simulado final enquanto for VOLÁTIL.

## 5. Comentário em três linhas — `itens[].comentario`
```json
"comentario": {"decisiva": "a palavra ou dado que decide o item (ex.: \"necessariamente\")",
               "regra": "a regra em uma frase, com base legal (art., inciso) ou tese (tribunal, nº, data)",
               "correta": "versão correta do item, quando o gabarito é E; quando é C, a troca que o tornaria E"}
```
- Obrigatório em todo item de lote `DA-v2` (intercalado ou de verificação). `justificativa` continua existindo (texto corrido) para compatibilidade com a plataforma atual; a v17 mostra `comentario` quando houver.
- Cada campo com até 280 caracteres. Divergência entre posição da banca e do produtor é marcada em `regra` com o prefixo "Banca:" / "Ressalva:".

## 6. Pares que a banca troca — `lotes[].pegadinhas[]`
```json
{"itemEdital": "P1-DA-2.1", "rotulo": "Extinção do ato",
 "par": {"a": "anulação", "b": "revogação", "muda": "ilegalidade (anula) × conveniência (revoga); efeitos ex tunc × ex nunc"},
 "texto": "..."}
```
- `par` obrigatório na v2 (três campos não vazios); `texto` mantém o formato "afirmação → ERRADO (motivo)" da v1.2.
- A lista de pares de cada tópico vem da seção 7 dos relatórios DAD/Relatorios_aulas (como conhecimento sobre a banca) e dos itens reais do banco; não do texto do curso de terceiro.

## 7. Verificação do tópico — questões por `itemEdital`
- Mínimo de 10 por item-folha além dos intercalados. Proporção (adendo v2.1, D-ESPEC-DA-V2-1, Fundador 25/10): `tipo: "caso"` em 5–10% dos itens do tópico (mínimo 1), o restante `tipo: "literal"`; quando houver caso, o erro fica na consequência (mecanismo AP), nunca no fato narrado. Todo item traz `mecanismo` (LIT, CON, SUP, PRA, GEN, AP, MIX, NEG, AUT, AMB, TEM — regras/estilo_banca_DA_v1.md, §4) e `comentario.decisiva` começa pelo código do mecanismo. [Substitui a regra anterior "metade literal, metade situação hipotética", que o corpus Cebraspe 2025 desmente: caso em 5–6% dos itens.]
- Todas com `comentario`. Nenhuma repetida entre intercalados e verificação do mesmo tópico.
- Metas de volume continuam as do Projeto: 20 por item-folha (D-REFORCO-2), 30 onde não houver real análogo (D-LACUNAS); proporções C/E e [TS] da D-REFORCO-2.

## 8. O que o script recusa a mais (bloqueio), para lotes/tópicos `DA-v2`
- `topicos[id]` sem `tarefas` (3 a 6, formato "Dado…"), sem `fechamento.levar` (5), sem `escopo` (lista, pode ser vazia).
- Bloco `## ` do curso sem `GLOSSÁRIO` como primeiro quadro, sem `CASO` antes da `DEFINIÇÃO`, sem `RESPOSTA DO CASO`, ou sem nenhum `ITEM`.
- `ITEM <id>` com id inexistente, de outro tópico, sem `comentario`, ou repetido na verificação.
- Item de lote `DA-v2` sem `comentario` com os três campos; campo acima de 280 caracteres.
- `PEGADINHA PROVÁVEL` sem as linhas `A:` / `B:` / `MUDA:`; pegadinha sem `par`.
- Qualquer linha do curso ou comentário com o padrão de referência de material de terceiro ("Estratégia", "Herbert", "p. <n> da aula", "Aula <nn>").
Avisos: tópico com menos de 10 questões de verificação; menos de 1 ITEM a cada 3 quadros; tabela com mais de 4 colunas; parágrafo com mais de 4 frases; termo em maiúsculas de quadro fora da lista (indica erro de digitação).

## 9. Lista de verificação do QA didático (gcb-cqfp, por tópico)
Marcar cada linha com SIM / NÃO / N/A e página ou linha do curso:
1. Tarefas no formato "dado X, decidir Y"; cada tarefa verificada por ao menos um item (intercalado ou de verificação).
2. Mapa de chegada no primeiro visual; repetido no fechamento.
3. Nenhum termo usado antes da sua linha no GLOSSÁRIO (busca pelos termos do glossário no texto que o antecede).
4. CASO sem resposta embutida; RESPOSTA DO CASO aplica a regra do bloco.
5. Quadro de pares cobre as confusões listadas para o tópico (seção 7 do relatório da aula correspondente e banco real).
6. ITEM a cada 2–3 quadros, com banca e certame identificados, comentário em três linhas oculto até a resposta.
7. Uma representação por conceito; nenhuma tabela quebrada; nenhuma classificação sem pergunta.
8. Toda citação CONFIRMADA pelo qa-normativo-da (data); nenhum número sem norma e data.
9. Fechamento com 5 frases e as listas literalidade × caso coerentes com os itens do tópico.
10. Escopo declarado; nenhum trecho, exemplo, tabela ou questão de material de terceiro (D-ESTRATEGIA).

## 10. Classificação
AGORA: esta especificação; `checa_pacote_v2.py`; regras no PADRAO_UNICO v1.1 (adendo); agente de QA didático. PRÓXIMO: a plataforma v17 na prévia lendo `tarefas`, `GLOSSÁRIO`, `CASO`, `RESPOSTA DO CASO`, `ITEM`, `comentario`, `fechamento`, `escopo` e `par`; ORDEM_DA_V2 fase 1. BACKLOG: revisão espaçada dos pares (1, 7 e 30 dias) e diagnóstico de 30 em DA.
