# lote6_errata_2026-10-10.md — T-17 — 2026-10-10 — gerado por gcb-cpp

REMETENTE: gcb-cpp (GCB — produção)
DESTINATÁRIO: gcb-cqfp (conferência restrita da errata); depois gcb-gerencia
Base: saida/gcb/lote6_reconciliacao.md (D1 GCB, T-04) e saida/gcb/lote6_conferencia.md (gcb-cqfp, 09/10/2026). Arquivos editados: saida/gcb/GCB_Lote6a_v2_producao_auto.md e saida/gcb/GCB_Lote6b_v2_producao_auto.md. Errata de forma: nenhum enunciado, gabarito, [TS], VOLÁTIL, ponto de julgamento ou contagem foi alterado.

## 1. Tabela antes → depois

| nº | arquivo; linha (HEAD → atual) | antes | depois |
|---|---|---|---|
| (a) OB-6b-1 | 6b; curso 4.0.2, l. 171 → 172 | "...NÃO HÁ ITEM sobre governança digital neste lote (a especificação previa o item "se houver base"). Observação para a GCB-CQFP: a Lei 14.129/2021 (Governo Digital) consta do Lote 4 como referência normativa já tratada pelo QA Normativo; não foi reaberta aqui e não fundamenta item." | Frase da observação retirada do curso (o parágrafo termina em "..."se houver base")."). Levada à Nota de produção (Parte 3), como (vi), l. 404: "governança digital (curso 4.0.2): a Lei 14.129/2021 (Governo Digital) consta do Lote 4 como referência normativa já tratada pelo QA Normativo; não foi reaberta aqui, não fundamenta item e só entra no curso com artigo conferido pelo qa-normativo." |
| (b) OB-6a-2 | 6a; curso 1.1.5, l. 111 | "...(trabalho típico do Derep, antigo DETAQ) chega ao revisor em Word." | "...de comissão, trabalho típico do Derep (antigo DETAQ), chega ao revisor em Word." |
| (b) OB-6b-2 | 6b; curso 2.0.6, l. 98 → 99 | "o servidor da unidade de taquigrafia (Derep, antigo DETAQ) que consulta uma página interna..." | "o servidor da unidade de taquigrafia, o Derep (antigo DETAQ), que consulta uma página interna..." |
| (c) OB-6b-3 | 6b; Nota de produção (i), l. 403 → 404 | "(i) tríade CIA, backdoor, rootkit, bot e antispyware seguem como conceito geral" | "(i) tríade CIA, trojan, backdoor, rootkit, bot e antispyware seguem como conceito geral" |
| (d) CQFP-1 (A-6b-1) | 6b; Tabela de Correções, linha nova após AJ-1 (l. 24) | (sem linha) | "CQFP-1 (A-6b-1) | FONTES F4 (seções 2.3 e 4.1); curso 4.1.3; curso 4.3.1; resumo 4.1; d-G 6B-09 | grafia das citações da F4 corrigida para "usuário" e "cópias", conforme o PDF oficial; retirada a marca de erro atribuída à fonte (era da extração do PDF); gabarito, marcações de troca sutil e de volatilidade e contagens inalterados | gcb-cqfp (conferência, 09/10/2026); aplicada pela GCB (D1) | aplicada; CONFERIDA (gcb-cqfp, R2, 09/10/2026)". Redigida sem os grafismos antigos, para não reintroduzir os termos que o grep de 09/10 exige em zero. |
| (e) TRF6 96/98 — seção ITENS REAIS | 6b; Nota, l. 52 → 53 | "Conferência visual humana do PDF pendente (BACKLOG) antes de uso em simulado, porque a leitura foi mediada por ferramenta." | "Conferência visual humana do PDF: cumprida por conferência direta do PDF oficial (gcb-cqfp, 09/10/2026; D1 GCB)." |
| (e) TRF6 96/98 — Nota de produção (v) | 6b; l. 403 → 404 | "(v) BACKLOG: conferência visual humana do PDF dos itens reais 96 e 98 antes de uso em simulado." | "(v) conferência visual humana do PDF dos itens reais 96 e 98: cumprida por conferência direta do PDF oficial (gcb-cqfp, 09/10/2026; D1 GCB);" seguido de (vi), item (a) |
| (e) TRF6 96/98 — linha R-6 | 6b; Tabela de Correções, l. 22 | nota "conferência visual humana do PDF pendente (BACKLOG) antes de uso em simulado"; status "aplicada (v2); conferência visual BACKLOG" | nota "conferência visual humana do PDF: cumprida por conferência direta do PDF oficial (gcb-cqfp, 09/10/2026; D1 GCB)"; status "aplicada (v2); conferência visual cumprida (gcb-cqfp, 09/10/2026; D1 GCB)" |

Não tocados (conforme a reconciliação): R-5 (governança digital sem item, BACKLOG, T-19) e OB-6a-1 (BACKLOG); a restrição de aderência parcial dos itens 96 e 98 (D-ADERENCIA) permanece na coluna "aderência" da tabela de itens reais.

## 2. Verificações (script em scratchpad s3/t17/verify.py; HEAD por git show, somente leitura)

| verificação | 6a | 6b |
|---|---|---|
| linhas de item (enunciado e d-G, ids 6A-01..15 / 6B-01..15) | 30/30 idênticas ao HEAD | 30/30 idênticas ao HEAD |
| gabarito por item (15) | idêntico; 7 C / 8 E | idêntico; 7 C / 8 E |
| itens com [TS] | 8, mesmos ids | 8, mesmos ids |
| ocorrências de "[TS]" / "VOLÁTIL" no arquivo | 14 / 11 → 14 / 11 | 13 / 6 → 13 / 6 |
| linhas alteradas (diff contra HEAD) | 1 (-1 +1); total 387 → 387 | 5 alteradas e 1 acrescentada (l. 22, 52, 98, 171, 403 e a linha nova); total 408 → 409 |
| "Observação para a GCB-CQFP" | 0 | 0 |
| "Derep, antigo DETAQ" | 0 | 0 |
| "Derep (antigo DETAQ)" | 1 → 2 | 5 → 6 |
| "pendente (BACKLOG)" | 0 → 0 | 2 → 0 (R-5 permanece "BACKLOG", sem a palavra "pendente") |
| "usuario", "copias", "[sic]" (6b) | n/a | 0 |

Contagens inalteradas: 6a 15 AUTORAL, 7 C / 8 E, 8 [TS], 5 VOLÁTEIS; 6b 15 AUTORAL, 7 C / 8 E, 8 [TS], 0 VOLÁTIL, 2 itens reais fora dos 15.
Pendente (fora desta tarefa): conferência restrita pela gcb-cqfp; sincronizar o espelho do Projeto (GCB/Lote6a_v2_producao_auto.md e GCB/Lote6b_v2_producao_auto.md) e liberar a T-27 depois da reconciliação da GCB.

## QA — gcb-cqfp — 2026-10-10

Escopo: conferência restrita da errata T-17 (somente leitura; `git diff` HEAD × árvore de trabalho dos dois lotes) e script próprio, independente do da produção (scratchpad t17qa/qa.py; HEAD lido por `git show`).

| item T-17 | conferido | resultado |
|---|---|---|
| (a) OB-6b-1 | curso 4.0.2 (l. 172) termina em "...(a especificação previa o item "se houver base")."; a observação foi para a Nota de produção como (vi) (l. 404), com "só entra no curso com artigo conferido pelo qa-normativo". "Observação para a GCB-CQFP": 1 → 0. "14.129" no 6b: 3 → 3, todas fora do curso (R-5 l. 21; Nota (iv) e (vi) l. 404); 0 no 6a | CONFERE |
| (b) OB-6a-2 / OB-6b-2 | 6a l. 111 e 6b l. 99 com "Derep (antigo DETAQ)". "Derep, antigo DETAQ": 6a 1 → 0, 6b 1 → 0. Todas as ocorrências de "DETAQ" nos dois lotes (6a 2; 6b 6) estão na forma "Derep (antigo DETAQ)" | CONFERE |
| (c) OB-6b-3 | Nota de produção (i), l. 404: "tríade CIA, trojan, backdoor, rootkit, bot e antispyware"; único acréscimo na frase | CONFERE |
| (d) linha CQFP-1 | linha "CQFP-1 (A-6b-1)" inserida na Tabela de Correções do 6b (l. 24, após AJ-1), com partes, descrição, origem e status coerentes com a seção 2 de lote6_reconciliacao.md | CONFERE |
| (e) TRF6 96/98 | texto "cumprida por conferência direta do PDF oficial (gcb-cqfp, 09/10/2026; D1 GCB)" nos três pontos: seção ITENS REAIS (Nota, l. 53), Nota de produção (v) (l. 404) e R-6 (l. 22, colunas nota e status). "pendente (BACKLOG)": 2 → 0. A coluna "aderência" (parcial) dos itens 96 e 98 permanece (D-ADERENCIA) | CONFERE |
| Nada além disso | diff: 6a = 1 linha substituída (l. 111); 6b = 5 linhas substituídas (HEAD 22, 52, 98, 171, 403) + 1 linha inserida (l. 24). Não há outro hunk | CONFERE |
| Itens e contagens (script próprio) | enunciados 15/15 + d-G 15/15 idênticos ao HEAD em cada lote (30/30 por lote); gabarito, [TS] e VOLÁTIL por item idênticos; 6a 7 C / 8 E, 8 [TS], 5 VOLÁTEIS; 6b 7 C / 8 E, 8 [TS], 0 VOLÁTIL; ocorrências de "[TS]"/"VOLÁTIL" no arquivo: 6a 14/11 → 14/11, 6b 13/6 → 13/6; linha "Contagem:" idêntica nos dois; "usuario", "copias" e "[sic]" = 0 no 6b | CONFERE |

Observações (não bloqueiam; não exigem nova rodada):
- O-1: o relatório da produção informa totais de linhas com +1 (6a 387; 6b 408 → 409); pelo `wc -l` os valores são 6a 386 → 386 e 6b 407 → 408. O número de linhas alteradas e inseridas está correto.
- O-2: a redação da linha CQFP-1 citada na seção 1 deste relatório difere da gravada no lote apenas na pontuação ("(era da extração do PDF); gabarito" × ", que era da extração do PDF. Gabarito"). O sentido é o mesmo. Vale o texto do lote.

VEREDITO: CONFERIDO. Os itens (a) a (e) foram aplicados como especificado, sem nenhuma outra alteração. Itens, gabaritos, [TS], VOLÁTIL e contagens estão intactos. Segue para a gcb-gerencia (reconciliação), que depois sincroniza o espelho do Projeto e libera a T-27.
