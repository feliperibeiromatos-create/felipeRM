# PADRAO_UNICO v1 — adendo v1.1 (proposta, 24/10/2026)

Quem muda o PADRAO_UNICO é o Fundador; esta sessão propõe. O adendo vale para lotes marcados `formato: "DA-v2"` e não altera as regras de TI e Fala. Fonte do método: Dossiê Didático DAD v1 (Partes III e IV); fonte de conteúdo: nenhuma de terceiro (D-ESTRATEGIA).

## Seção 1 (lote) — acréscimos
1.7 Toda unidade (tópico do edital) abre com `tarefas` (3–6, "Dado X, decidir Y") e fecha com `fechamento` (5 frases "o que levar" + listas literalidade × caso) e `escopo` (o que fica para outra unidade).
1.8 Dentro de cada subitem do curso, a ordem é GLOSSÁRIO → CASO → texto → DEFINIÇÃO → BASE LEGAL → RESPOSTA DO CASO → EXEMPLO PARLAMENTAR → ITEM → PEGADINHA PROVÁVEL (A/B/MUDA). Nenhum termo técnico antes da sua linha no GLOSSÁRIO.
1.9 Uma representação por conceito (prosa OU esquema OU tabela). Classificação só com a pergunta que distingue as classes; rótulo sem questão conhecida vai para apêndice ou sai.
1.10 Item intercalado (`ITEM <id>`) pelo menos um por subitem, de preferência real (CEBRASPE_OFICIAL/ANALOGA); comentário em três linhas (`comentario.decisiva / regra / correta`), oculto até a resposta. Intercalado não repete na verificação nem entra em simulado final enquanto VOLÁTIL.
1.11 Verificação por item-folha: mínimo 10 além dos intercalados, metade `tipo: literal`, metade `tipo: caso`; metas de volume e proporções continuam as da D-REFORCO-2 e D-LACUNAS.
1.12 Pegadinha = par (`a`, `b`, `muda`) + armadilha + explicação + item (D-PEGADINHA-UNICA), em todas as pegadinhas do lote.

## Seção 2 (evidência) — acréscimos
2.6 Todo número (valor, prazo, quantidade) traz norma e data de conferência; toda tese traz tribunal, número e data; "recente" sem ano é vedado.
2.7 Material de curso de terceiro (Estratégia ou qualquer outro) não é fonte de texto, exemplo, tabela ou questão; só de análise de forma (D-ESTRATEGIA). O checa_pacote_v2.py bloqueia referência explícita; o QA didático confere o resto.

## Seção 3 (separação) — acréscimo
3.6 Lotes DA-v2 têm três QAs: normativo (qa-normativo-da), didático (gcb-cqfp-didatico, checklist da ESPEC v2 seção 9) e o de forma do pacote (checa_pacote_v2.py, zero bloqueios). Modelos distintos da produção. Máximo de 2 rodadas.

## Seção 7 (contrato do pacote) — acréscimos
7.x Campos novos: `lotes[].formato`, `topicos[].formato|tarefas|fechamento|escopo`, `itens[].comentario|tipo`, `pegadinhas[].par`, marcador `ITEM <id>` no curso. Compatíveis com a plataforma atual (campos ignorados até a v17); obrigatórios para lotes DA-v2.
