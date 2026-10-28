# ESPEC — Plataforma v17.2: janela de 20 na nota do tópico (D-V17-2-JANELA-20) — v1.1

v1.1 (26/10, depois da QA R1 opus da produção): (a) o status conta as questões vistas na janela, inclusive em branco (valem 0), e por isso diz "n de k questões", não "respondidas" (D6); (b) o status aparece também na linha do tópico do Painel/matéria, como "n/k" sob o %, só quando há respostas e a nota não está completa (D1); (c) o aviso de uma visita fica no Painel (a apresentação não reaparece para quem já usa) e só aparece quando o % exibido de algum tópico mudou de fato entre a regra antiga e a nova (D4, D10); (d) "Falta 1 questão" (D5); (e) o card pós-bloco mostra o status uma vez só, junto do % (D7); (f) registro latente D9: um resultado de bloco gravado na v17.1 teria "Antes:" dividido pelo divisor novo — hoje inalcançável, porque a tela de resultado só abre logo depois de entregar().

26/10/2026 · sessão Cowork, por ordem do Fundador ("Pode escrever a linha de decisão e especificação"). Lida contra o código da v17.1 (saida/plataforma/plataforma_v17_1_template.html, linhas 806–1030, 1280–1320, 1417–1422). Substitui a D-V17-NOTA-TOPICO (Fundador, 23/10) só no número da janela; tudo o mais daquela decisão continua.

## 0. O que já existe e o que muda (uma frase cada)
- JÁ EXISTE: a rodada de questões do tópico é de 10 (`BLOCO=10`, função `montarBloco`): primeiro as que a candidata nunca viu, depois as que errou, depois as demais; sem cronômetro. O pedido "10 questões por tópico" já está implementado desde a v17 — não há mudança aqui.
- JÁ EXISTE: só questões distintas contam (decisão do Fundador de 18/10; `CONTA_REPETIDAS=false`); o item intercalado do curso fica fora da nota (D-V17-1-INLINE).
- MUDA: a janela da nota passa de 30 para 20 (`JANELA=30` → `JANELA=20`), e, com ela, o divisor da nota do tópico passa a ser o menor entre 20 e o número de questões distintas do tópico no banco (`divTopico`).
- MUDA: a candidata passa a ver quantas questões faltam para a nota ficar completa ("12 de 20 questões"; no Painel, "12/20" sob o %) e a marca "nota completa" quando chega a 20.
- NÃO MUDA: o diagnóstico de entrada continua com até 30 itens por matéria (D-AUDITORIA-20OUT, condição 3; T-124); as médias por matéria, P1, P2 e Nota Final continuam compostas a partir da nota do tópico, pela mesma fórmula (D-V17-NOTA-TOPICO).

## 1. Regra da nota do tópico (texto da decisão)
1. Janela: as 20 questões distintas do tópico respondidas mais recentemente (`janela(tid)` com `JANELA=20`); respostas a itens intercalados não entram.
2. Divisor: menor entre 20 e o número de questões distintas do tópico no banco, descontados os intercalados (`divTopico`). Tópico com menos de 20 questões: divisor = o que existe (quem acerta tudo vê 100%, como hoje).
3. Nota em %: `(acertos − erros) ÷ divisor`, as respostas que faltam valem 0 (em branco), como hoje (`pctDe`). Começa em 0%.
4. Nota completa: quando a janela tem `n ≥ divisor` questões vistas (isto é, 20, ou todas as do tópico quando há menos de 20); questão deixada em branco entra na contagem e vale 0, como já valia na janela da v17.1. Antes disso a nota é PARCIAL e a interface diz "n de 20 questões" (ou "n de k", com k = divisor, quando o tópico tem menos de 20).
5. O campo `nota` de `notaTopico` (hoje `n>=JANELA ? c−e : null`) passa a `n>=divTopico(tid) ? c−e : null`, para que "nota recente +x/20" em `porque()` e o sinal de completa usem o mesmo critério.

## 2. Mudanças no código (todas no template; o pacote não muda)
| Onde (v17.1) | Hoje | v17.2 |
|---|---|---|
| l. 805 `VERSAO_APP` | "v17.1" | "v17.2" |
| l. 806 `JANELA` | 30 | 20 |
| l. 807–808 comentário | D-V17-NOTA-TOPICO | acrescentar "v17.2 (D-V17-2-JANELA-20): janela 20" |
| l. 960 `notaTopico` | `nota:n>=JANELA?c-e:null` | `nota:n>=divTopico(tid)?c-e:null` e novo campo `completa:n>=divTopico(tid)` |
| l. 962 `notaHtmlTop` | só o % | % + `<span class="xs muted">` com "(nota completa)" ou "(n de k questões)" (k = `divTopico`) |
| l. 368 CSS e l. 1073 `linhaTopico` (Painel/matéria) | só o % | % e, sob ele, `<span class="st">n/k</span>` quando `n>0` e a nota não está completa (v1.1, QA D1) |
| l. 1003 texto de ajuda | "até ${JANELA} questões diferentes…" | mesmo texto com 20 (já lê a constante) + "A nota fica completa com 20 questões diferentes respondidas (ou todas as do tópico, se houver menos); até lá você vê quantas faltam. Questão deixada em branco conta na contagem e vale 0." |
| l. 1130 fim do curso | "10 questões, sem cronômetro…" | acrescentar, quando houver respostas e a nota não estiver completa, "Faltam x questões para a nota completa." ("Falta 1 questão" no singular) |
| l. 1317 texto pós-bloco | "Calculado sobre até ${JANELA}…" | mesmo, lê a constante (20); o status já vai no % pelo `notaHtmlTop`, sem repetição (v1.1, QA D7) |
| l. 1422 `porque()` | `nota recente ${sinal}/${JANELA}` | `/${divTopico(o.id)}` |
Nada mais muda: `montarBloco` (10 por rodada), `pctDe`, `mediaProva`, `notaProva` (90 × média), `notaFinal`, `lacuna()`, caderno de erros, painel de mecanismos, `S.cursoResp`.

## 3. Dados já gravados (S.resp)
Nenhuma migração: a janela é recalculada a cada leitura sobre `S.resp`. Efeito na primeira abertura da v17.2, em dois casos: (i) tópico com mais de 20 questões no banco e alguma resposta — o divisor cai de min(30, banco) para 20 e o % sobe em módulo (ex.: 8 C / 4 E em banco de 30: 13% → 20%); (ii) tópico com 21 a 30 questões distintas respondidas — a janela corta as mais antigas e a nota pode subir ou descer. Aviso de uma visita no Painel (`S.avisoV172`), só quando o % exibido de algum tópico muda entre as duas regras (v1.1, QA D4): "A partir desta versão, a nota de cada tópico é calculada sobre até 20 questões diferentes (antes eram 30)…". Sem mudança visível, sem aviso.

## 4. Casos a cobrir nos testes (Playwright 390×844 e 1280×900, claro e escuro, mais a regressão R1–R9 da v17.1)
1. Tópico com 25 questões no banco, 0 respondidas: 0%, "0 de 20 questões".
2. 10 respondidas (1 rodada), 8 C / 2 E: (8−2)/20 = 30%, "10 de 20 questões", nota não completa; `porque()` não mostra "nota recente"; no Painel, "30%" com "10/20" embaixo.
3. 20 respondidas distintas: nota completa; "nota recente +x/20" aparece.
4. 30 respondidas distintas: só as 20 mais recentes contam (conferir contra a ordem de registro, que é a ordem de `t`); responder de novo uma questão antiga a leva ao fim da janela com a resposta nova.
5. Tópico com 12 questões no banco, 12 respondidas, todas C: 100% e "completa"; com 7 respondidas: "7 de 12".
6. Item intercalado respondido no curso (clique real na bolha): S.resp não muda; n, c, e e o contador "n de k" não mudam; k = banco do tópico menos os intercalados.
7. Repetir uma questão já respondida (segunda rodada pega as erradas): continua contando uma vez, com a resposta mais recente.
8. Médias por matéria, P1, P2 e Nota Final: recalculadas a partir das novas notas de tópico; num estado salvo da v17.1 só mudam pelos efeitos (i) e (ii) da seção 3 — regressão com oráculo independente da regra, em estado com até 17 distintas e em estado com 30 distintas em dois tópicos, conferindo no DOM cada % de tópico exibido.
9. Diagnóstico de entrada: segue com 30 itens, inalterado.
10. Textos (apresentação, Painel, matéria, curso, pós-bloco, recomendações), nas quatro combinações 390×844/1280×900 × claro/escuro: nenhuma ocorrência de "30" ligada à nota do tópico, fora do aviso ("antes eram 30") e do diagnóstico de 30.
11. Aviso de uma visita: aparece com 25 C em banco de 30 (83% → 100%) e com 5 C em banco de 30 (17% → 25%); não aparece com banco ≤ 20, com saldo 0 (0% → 0%) nem na segunda visita.

## 5. Opcional na mesma rodada — só se D-INLINE-REFAZER = SIM em DECISOES.md
Botão "Refazer" no item intercalado depois da resposta: limpa a bolha e aceita nova resposta; grava em `S.cursoResp` como novo registro (o anterior fica); nada entra em `S.resp`. Teste: refazer não altera nota, caderno nem "n de 20". Se a decisão não estiver registrada, fica fora da v17.2.

## 6. Execução, QA e publicação
- Produção: sessão de design (Cowork, Fable) sobre cópia do template v17.1 → `plataforma_v17_2_template.html`; `patch_v17_2_janela20.py` com as substituições da seção 2 (como o patch da v17.1), para ser reaplicável sobre a v17.1 e verificável por diff.
- Build: `build_plataforma_v17.py --template plataforma_v17_2_template.html --pacote <pacote vigente>`; `checa_pacote_v2.py` e `regressao_pacote.py` como no roteiro de entrada.
- QA: modelo distinto (opus), com os 10 casos da seção 4 e a regressão da v17.1; relatório `QA_v17_2_<data>.md`.
- Publicação no link da candidata: pela D-V17-1-PUBLICAR, se registrada com SIM a (ii); senão, sim do Fundador por esta publicação (D-AUDITORIA-20OUT). A v17.2 pode sair junto com a v17.1 numa única publicação, se a v17.1 ainda não tiver sido publicada quando a v17.2 passar na QA.

## 7. Classificação
AGORA: linha de decisão em DECISOES.md; esta ESPEC; produção e QA da v17.2 (uma sessão de design). PRÓXIMO: publicação (depende do sim). BACKLOG: painel por mecanismo (D30) e revisão espaçada, que não entram aqui. DESCARTADO: mudar o tamanho da rodada (já é 10) e mudar o diagnóstico de 30.

## 8. Linhas para colar

DECISOES.md (fim do arquivo):
```
NOVA | D-V17-2-JANELA-20 | (Fundador, 26/10) A janela da nota do tópico passa de 30 para 20 questões distintas respondidas mais recentemente; o divisor é o menor entre 20 e o número de questões distintas do tópico no banco (sem os itens intercalados); a nota é completa com 20 respondidas (ou todas as do tópico, se houver menos) e, antes disso, a interface mostra "n de 20". A rodada de questões continua de 10 (BLOCO=10: nunca vistas → erradas → demais). Substitui a D-V17-NOTA-TOPICO só no número 30 → 20; médias por matéria, P1, P2 e Nota Final seguem compostas pela mesma fórmula; o diagnóstico de entrada continua com até 30 por matéria. Implementação na plataforma v17.2 (claude/ESPEC_plataforma_v17_2_janela20_2026-10-26.md), sessão de design com QA por modelo distinto; publicação pela D-V17-1-PUBLICAR ou por sim próprio.
```

TAREFAS.md (bloco de tarefas abertas; usar o próximo número livre — na cópia de 25/10 o último é T-133):
```
T-134; PLATAFORMA; Plataforma v17.2 — janela de 20 na nota do tópico (D-V17-2-JANELA-20): JANELA=30→20, divisor e "nota completa", textos; opcional "Refazer" no item intercalado se D-INLINE-REFAZER=SIM; ESPEC claude/ESPEC_plataforma_v17_2_janela20_2026-10-26.md; AGORA; PENDENTE; produção Cowork (Fable) → QA-plataforma (opus, 10 casos + regressão R1–R9) → gbq-gerencia; saida/plataforma/plataforma_v17_2_template.html, patch_v17_2_janela20.py, QA_v17_2_<data>.md
```
