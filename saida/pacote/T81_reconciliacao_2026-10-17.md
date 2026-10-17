# saida/pacote/T81_reconciliacao_2026-10-17.md — T-81 (D-T12-V13; D-T81-RESPOSTA) — 2026-10-17 — gerado por gbq-gerencia

REMETENTE: gbq-gerencia (reconciliação e D1; não produz nem revisa conteúdo).
DESTINATÁRIO: orquestrador (gatilhos em PARA_PRESIDENCIA.md; linhas novas em TAREFAS.md; fechamento da T-81). Cópia: gbq-csc, gbq-cqe, Secretaria de Estado Canônico.

Base:
- a D1 de escopo `saida/pacote/T81_D1_escopo_v1_8_2026-10-17.md`, seções 0 a 8, e o seu Adendo 1 (seção 9; correção de `banco.nota_de` depois da parada da produtora);
- o relatório da produção `saida/pacote/pacote_relatorio_2026-10-17_v1_8.md`;
- o QA de fidelidade `saida/pacote/fidelidade_v1_8_gbq-cqe.md`, da gbq-cqe, com leitura própria.

## 0. Conferência própria da GBQ

Feita em 17/10/2026, por script próprio no scratchpad, em modo somente leitura (`python -I`), sem gravar nada no repositório.

| Objeto | Esperado (D1) | Em disco | Confere |
|---|---|---|---|
| `saida/pacote/pacote.json` v1.8 | `09d4a457612781275659a3f7fbfd3a182f20fd9d4003e5ba38007d0c26c7a9c0`, 621907 bytes (valor de controle da GBQ, seção 8) | `09d4a457…` | SIM |
| `saida/pacote/pacote_estudante.json` v1.8-E | `851e2370…`, 602815 bytes (valor da produtora no contrafactual; Adendo 1, 9.4: reprodução exigida) | `851e2370a9f5e9c8e5db725ff84777f70c12f81044983d339434ac7504e04c3e` | SIM (também calculado pela gbq-cqe) |
| `regras/pacote_contrato.md` v1.2.5 | `10eac696dbb83049ba12ee793ff4991a1884094b7b88cdaf39f10a3fcc33660e` (CONTRATO-V125) | `10eac696…` | SIM |
| `saida/estudante/` v1.8 | 34 arquivos; manifesto ordenado `0b7391fa…` (Adendo 1, 9.4) | 34 arquivos; `0b7391fa0178488924de8e6ed420c6108dd5fdad0e10fd1c5ccc40d9cd4bae6c` | SIM |
| Relatório da produção | — | `c2b7bbd45c35989270957eb0e0ffb0b17754f36cb4ffa074d50d34b9472dba3a` | igual ao relato do orquestrador e ao do QA (I4) |

Conferências estruturais do `pacote_estudante.json`, feitas pela GBQ:
- chaves de topo iguais às do `pacote.json`;
- nome "Câmara 2026 — pacote do estudante (v1.8-E)" e geradoEm 2026-10-17;
- lotes L1, L2, L3, L4, L5, L6A, L6B;
- 286 itens, com ids, ordem, chaves e os 14 campos da 2.2 idênticos aos do `pacote.json`;
- `url` diferente em exatamente 180 itens, todos AUTORAL e com "";
- C/E 149/137 e `volatil` 23;
- 4 simulados com listas de itens idênticas, e edital idêntico;
- L1 com 1 separador "\n\n## Complemento\n\n" e 23 pegadinhas (19 + 4);
- varredura R da D1 (2.3) sobre todas as strings: 9 casamentos, exatamente X1–X8 e Y1, e 0 de processo.

O `pacote.json` v1.8 tem nome "… (v1.8)" e geradoEm 2026-10-17.

`git diff` de `banco/`, `saida/pacote/gerador_v1_7/`, `saida/plataforma/`, `saida/gce/`, `saida/gcb/` e `saida/simulados/`: vazio, ou seja, intactos.

Fim de linha:
- `git status` mostra como "M" os 26 arquivos da edição que deveriam estar idênticos à v1.7. A causa é só o fim de linha: foram promovidos em LF, e o checkout usa `core.autocrlf=true` (I3 do QA).
- Ignorando a diferença de fim de linha (`git diff --ignore-cr-at-eol`), a mudança real da v1.7 para a v1.8 é a esperada pela D1 (3.3 e 1.3): 9 arquivos retirados, 8 alterados e `saida/pacote/pacote.json`, ou seja, 18 arquivos.
- Amostra conferida por SHA do conteúdo normalizado: L2_estudo, SIM-1_gabarito, BANCO_itens e L4_estudo são iguais ao HEAD; L1_itens difere, como esperado.
- O commit normaliza o fim de linha, e nenhum SHA de controle (LF) é afetado.

## 1. Reconciliação produção × QA

| # | Ponto | Produção (gbq-csc) | QA (gbq-cqe) | GBQ |
|---|---|---|---|---|
| 1 | Pipeline | 11 passos, código 0; validate 118/0; conferencias_v18 214/0; mutações 8/8 (JSON), 14/14 (edição) e 12/12 (validador-registro) | regeração e cálculos próprios; mesmos SHA | Conferido (seção 0). Os 214 = 211 do contrafactual + as 3 do Adendo 1 (9.3). |
| 2 | Conferência (f) | 2 clones de HEAD e uma 3ª cópia, idênticos byte a byte | — | Cumpre a 6.4 com o Adendo 1, 9.6 (banco de HEAD). |
| 3 | Diff pacote v1.7 → v1.8 | `$.nome` e `$.geradoEm` | idem | Cumpre a 1.3. A falha de 3 caminhos foi resolvida pelo Adendo 1 sem tocar no `banco/`. |
| 4 | Fidelidade do JSON do estudante (só deleções da lista; 0 marca de processo; itens, gabaritos e enunciados idênticos) | conferências (4) a (7) | APROVADO COM RESSALVAS, 0% de reprovação; R1–R3 baixas; I1–I4 informativos | Ressalvas arbitradas na seção 2. Nenhuma toca a fidelidade, um gabarito, um enunciado ou um comando. |
| 5 | Adaptações da produtora | X5–X7 em grupo na edição; histórico por transitividade | — | Aceitas no Adendo 1 (9.5), com condições, cumpridas segundo o relatório e o QA. |
| 6 | Contrato v1.2.5 e registro | `regras/pacote_contrato.md` e `saida/pacote/contrato_v1_2_5_2026-10-17.md` | SHA conferido | SIM |
| 7 | T-69 | (4) feita: `validate.py` com `sys.exit` | — | (4) executada nesta T-81. (2) continua BACKLOG (D1, seção 5). O orquestrador atualiza a linha da T-69. |

## 2. D1 sobre as ressalvas do QA

**D-RT81-01 — R2: CONTEÚDO, sem ação na v1.8.**
- O trecho é "(CEBRASPE_ANALOGA; gabarito definitivo E, conferido no GAB_DEFINITIVO_034_TRF6_002_01)", em `itens[L4-11].justificativa` e `lotes[L4].curso`.
- O referente é a proveniência oficial de um item real da Cebraspe (TRF6 2024, Cargo 2, item 81): o rótulo, o gabarito definitivo e o nome do documento oficial do gabarito. Essa é informação de matéria e de fonte oficial, que a camada do estudante já mostra de outros modos: em `BANCO_itens.md`, "Itens de provas anteriores (rótulo CEBRASPE_ANALOGA)", e nas URLs oficiais dos itens de banco.
- O trecho não traz data nem agente, e não casa com nenhuma regex da varredura R. Pelo critério operacional da D1 (2.3), não é processo.
- "conferido no" registra o ato, mas o seu objeto é o documento oficial, não a fábrica.

**D-RT81-02 — R3: CONTEÚDO, sem ação na v1.8; coerência pós-fusão vai para errata opcional (T-83).**
- O trecho é "É o item deste lote mais próximo de um canônico (A5-20)", em `itens[5C-08].justificativa`.
- "Um canônico" designa o item de referência do mesmo princípio (A5-20). Esse item fica visível à candidata no mesmo gabarito do L5, e a frase anterior da mesma justificativa já o compara a ele ("Difere do item A5-20 porque…").
- A palavra não está na lista ampliada nem na varredura R.
- Depois da fusão, "deste lote" (o 5-C) e o contraste com o "canônico" perdem nitidez, porque A5-20 e 5C-08 passam a estar no mesmo lote L5. Isso é coerência de forma, não marca de processo. Uma retirada por deleção pura ("mais próximo de A5-20") pediria regra nova e nova versão, e não se justifica para um item de forma (T-12: "itens só de forma não abrem versão").
- Vai, como opção da GCB, junto com Y1 na T-83. Não bloqueia a v1.8.

**D-RT81-03 — R1: encaminhado à GCE (T-84), errata opcional, sem efeito na v1.8.**
- O trecho é "ver Lote 1-C." no curso do L2 (`L2_estudo.md:237`). É uma remissão que, na camada do estudante, deixou de ter lote correspondente; o conteúdo agora está em "## Complemento", no fim do curso do L1.
- É idêntico à v1.7 e não é processo. Pela regra "só deleção" não cabe correção na produção. A redação no canônico é da GCE (D-EDITOR-UNICO).
- Junto, a N4 de `GCE_Lote3_v2_CPP.md` (D-T81-05; fora do pacote), se a GCE quiser.
- O campo `cargo` "Lote 1-C/4-C/5-C" dos 30 itens dos complementos continua por identidade obrigatória. Só a plataforma o exibiria, e a adaptação dela é do Fundador (gatilho E).

**D-RT81-04 — Y1 / I1: encaminhado à GCB (T-83).**
- O trecho é "O F4 afirma que" (L4-11). Continua literal, como DÚVIDA prevista na D1 (2.4).
- Retirá-lo exige reescrita, que é do canônico da GCB (D-EDITOR-UNICO). Errata opcional, sem mudança de gabarito, absorvida na próxima ocorrência da T-12 se for aceita.

**D-RT81-05 — I2, I3, I4: registro, sem ação.**
- I2: a legenda do L5C já estava prevista na D1 (3.1).
- I3: arquivos promovidos em LF, sem efeito em nenhum SHA.
- I4: os SHA do relatório da produtora conferem.

**D-RT81-06 — Natureza do aceite.**
- Com R2 e R3 classificados como conteúdo (D-RT81-01 e 02) e R1 e Y1 fora do objeto (errata de canônico em tarefa própria, que não altera a v1.8), não sobra condição pendente sobre o objeto.
- O veredito do QA, sobre o objeto v1.8, reduz-se a APROVADO, no mesmo sentido do precedente D-RV17 ("o aceite é do objeto, não 'com ressalva'").
- Nenhum item tem gabarito em disputa. Os 23 voláteis seguem na fila de janeiro (T-11, T-14, T-16, T-18, T-41), como na D-PACOTE-V17.

**D-RT81-07 — Defeito latente no gerador_v1_7 (Adendo 1, 9.1–9.3): registro, sem ação.** O `gerador_v1_7` é registro intacto da v1.7. Uma regeração futura parte do `gerador_v1_8`.

**D-RT81-08 — Plataforma v1.7 × pacote_estudante.json (P8 da D1): gatilho E, separado do A.**
- A plataforma v1.7 associa itens a lotes por prefixos fixos (`LOTE_INFO`) e tem as listas de lotes por módulo fixas, com L1C, L4C e L5C. Se ela ler o `pacote_estudante.json` sem adaptação, os 30 itens dos complementos ficam fora dos testes de lote; só aparecem nos simulados.
- Adaptar, testar e entregar é do Fundador (D-T12-V13; D-T81-RESPOSTA). O aceite da v1.8 não depende disso: o `pacote.json` v1.8 tem a estrutura da v1.7 e a plataforma v1.7 o lê como lê a v1.7.

## 3. Saídas deste ato
- PARA_PRESIDENCIA.md (ciclo s11c1): GATILHO A (aceite da v1.8) e GATILHO E (P8, ao Fundador). 2 gatilhos.
- TAREFAS.md: T-83 (GCB, errata opcional de forma: Y1 e R3) e T-84 (GCE, errata opcional de forma: R1 e N4), ambas PRÓXIMO.
- Fica com o orquestrador: fechar a T-81; atualizar a T-69 ((4) executada; (2) BACKLOG); o commit.
