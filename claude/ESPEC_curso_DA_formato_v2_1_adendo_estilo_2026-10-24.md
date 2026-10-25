# ESPEC curso DA — adendo v2.1 (estilo da banca) — PROPOSTA, 24/10/2026

Sessão Cowork (análise do dossiê), a partir de DAD/ESTILO_banca_DA_Cebraspe2025_v1_2026-10-24.md (seção 6) e do kit_fabrica_v2. Altera só o que a ESPEC v2 diz sobre a FORMA dos itens; tudo o mais da v2 continua. Quem adota é o Fundador; até lá, a ORDEM_DA_V2_FASE1 não deve rodar com a regra "metade caso" da v2, que o corpus 2025 desmente.

## 1. Conflito a resolver antes da fase 1
- ESPEC v2 §7 e adendo PADRAO 1.11: verificação "metade `tipo: literal`, metade `tipo: caso`".
- ESTILO §1 e §6.4 (1.118 itens C/E de 2025): caso concreto em 5–6% dos itens; item típico é assertiva de 21–35 palavras; em 6.1 (responsabilidade) 0% de caso por regex.
- Dossiê DAD, Parte III princípio 9: "manter a proporção literalidade × aplicação da banca para o tema" — a proporção certa é a medida no corpus, não a intuição da Parte V do dossiê ("responsabilidade civil ~50% caso"), que veio das baterias do curso de mercado (com múltipla escolha e anos antigos). Prevalece o corpus.

Decisão proposta: §7 passa a "pelo menos 10 itens de verificação por item-folha; `tipo: caso` em 5–10% dos itens do tópico (mínimo 1), o restante `tipo: literal`; quando houver caso, o erro fica na consequência (AP), nunca no fato narrado". O campo `fechamento.caso` continua (lista do que a banca cobra por situação), mas pode ter 1 entrada.

## 2. Campos e regras novas (lotes `DA-v2`)
- `itens[].mecanismo`: um código da tabela ESTILO §4 — LIT, CON, SUP, PRA, GEN, AP, MIX, NEG, AUT, AMB, TEM. Obrigatório em item AUTORAL de lote DA-v2; em item real, preenchido pela varredura do banco (coluna `mecanismo_wb` da fila é só ponto de partida; reclassificação por agente de modelo distinto, ESTILO §7).
- `comentario.decisiva` começa pelo código do mecanismo seguido da palavra ou dado que decide ("CON: 'revogação' no lugar de 'anulação'"; "SUP: falta 'salvo comprovada má-fé'"). O código é o que a plataforma usa para agrupar erros da candidata.
- Distribuição por lote de 20 AUTORAL (ESTILO §6.1): 8–12 C, maioria LIT, 1–2 AP; 8–12 E com CON 3–4, SUP 2–3, GEN 1, NEG 1, PRA/AUT/AMB/TEM 1–2. Lotes de outro tamanho escalam as cotas.
- Nenhum item E cujo único erro seja um absolutizador acrescentado a frase que a lei não contém (ESTILO §6.2); absolutizador também em itens C (a banca tem ~40% dos absolutizadores em C).
- Item (sem o comando) com 21–35 palavras como alvo; acima de 60 só com justificativa. Comando nomeia 2–3 temas; fechamento sorteado entre os seis da banca (ESTILO §3). Texto-base só quando servir a 3 ou mais itens.
- `itens[].tipo`: "literal" | "caso" (já previsto na v2); "caso" exige mecanismo AP ou mecanismo de erro na consequência.

## 3. Conferência
- checa_pacote_v2.py: continua como está (bloqueios de forma). Acrescentar, quando o Fundador adotar, um AVISO para item DA-v2 sem `mecanismo` e um BLOQUEIO para `mecanismo` fora da tabela.
- checa_estilo_DA.py (novo, neste kit; só avisos): % C por lote, comprimento do item, % caso, absolutizadores (E e C), distribuição de mecanismos contra as cotas, `comentario.decisiva` nomeando o mecanismo, variedade de abertura e fechamento do comando, comandos com um só tema. Roda sobre pacote.json ou index.html; `--so-v2` limita aos lotes DA-v2; `--lote <id>` a um lote. Testado em pacote sintético; não rodado contra o pacote vigente (sem acesso ao repositório desta sessão).
- QA didático (gcb-cqfp-didatico): linha 11 no checklist — "distribuição de mecanismos e proporção literal × caso dentro das cotas; relatório do checa_estilo_DA.py anexado".

## 4. O que isto muda nas ordens do kit
- ORDEM_DA_V2_FASE1 e): trocar "metade literal, metade caso" por "caso em 5–10%"; acrescentar `mecanismo` obrigatório e `checa_estilo_DA.py` antes da entrega (avisos justificados no relatório do lote).
- ORDEM_BANCO_DA_CDN_ONDA1 c): a prova "AFP (SEFAZ RJ)" tem 21 candidatos e 0 Certo/Errado (resumo_por_prova_v2.csv); como a onda só incorpora C/E, substituí-la pela próxima com C/E (APC FUNPRESP-EXE, 20) ou declarar que entra só como insumo de pegadinha.
- ORDEM_BANCO_DA_CDN_ONDA1 e): registrar `mecanismo` do item real com a mesma tabela; a reclassificação de amostra (ESTILO §7, 100 itens, modelo distinto) vira parte do QA da onda 1, para que a tabela de mecanismos passe a ser da Fábrica e não do pacote de auditoria.

## 5. Na plataforma (v17; depende da ordem da v17)
1. Chip do mecanismo na tela de feedback de cada item de DA (lido de `mecanismo`), com a frase de leitura do ESTILO §6.6 ("procure a troca de vizinho e a condição que falta").
2. Painel da candidata: erros por mecanismo × item do edital ("você erra CON em 10.1 e SUP em 4.4"), calculado dos registros de resposta já existentes; sem campo novo além de `mecanismo`.
3. Modo "treino por mecanismo": filtro que monta uma rodada só com CON (ou SUP, GEN…) de um tópico, a partir do banco; usa itens reais quando houver.
4. Tela de abertura do módulo de DA, "Como a Cebraspe constrói o item" (uma tela): a tabela da seção 4 resumida em seis linhas, o aviso de que palavras absolutas pedem atenção e não resposta automática, e a estatística 49% C × 51% E. Conteúdo próprio (estatística da sessão), sem texto de terceiro.
5. Diagnóstico de 30 itens de DA (D-DIAG30-DA): composição por mecanismo proporcional à banca (≈ 50% LIT entre os C; CON/SUP/GEN dominando os E), não só por item do edital.
6. Revisão espaçada dos pares (1, 7, 30 dias) já no BACKLOG da v2: a fila de revisão prioriza os pares (A/B/MUDA) cujo mecanismo a candidata mais erra.

Classificação: itens 1, 2 e 5 AGORA junto com a v17 (campo `mecanismo` + agrupamento; sem layout novo); 3 e 4 PRÓXIMO; 6 BACKLOG.
