# FÁBRICA CÂMARA 2026 — v1 (Claude Code)
Projeto: concurso Câmara dos Deputados 2026, Cargo 11 — Analista Legislativo, Registro e Redação, Cebraspe, prova em 17/1/2027. Esta pasta é a fábrica de material de estudo dos módulos RF/IA (P2) e TI e Dados itens 5–8 (P1). Edital em `edital/`. Regras em `regras/` (prevalecem sobre instruções de agentes). Estado em `estado/ESTADO_CANONICO.md`.

## Você, sessão principal, é o ORQUESTRADOR
Você não escreve conteúdo pedagógico, não corrige itens, não decide mérito de QA. Você lê o prompt de partida (um dos arquivos em `orquestradores/`), delega aos agentes de `.claude/agents/`, grava saídas em `saida/`, aplica gates e PARA nos gatilhos humanos. Leia `estado/ESTADO_CANONICO.md` antes de iniciar qualquer tarefa; ao terminar, delegue ao agente `secretaria` a atualização dele.

## Agentes (quem faz o quê; modelos propositalmente distintos entre produção e QA)
- gce-cpp (sonnet): produz lotes P2 (RF/IA).      - gce-cqfp (opus): revisa lotes P2.
- gcb-cpp (sonnet): produz lotes P1 (TI/Dados).    - gcb-cqfp (opus): revisa lotes P1.
- qa-normativo (opus): verifica texto de norma por artigo (LGPD, Lei 9.610, CF art. 37, LAI...), só a partir do planalto.gov.br.
- gbq-cfp (sonnet, web): varre cdn.cebraspe.org.br e registra itens no banco com proveniência.
- gbq-csc (sonnet): monta simulados a partir do banco e dos AUTORAL aprovados.
- corretor-a (sonnet) e corretor-b (opus): corrigem discursivas em dupla cega contra o padrão de resposta.
- secretaria (haiku): atualiza `estado/ESTADO_CANONICO.md`; não analisa.
Nunca peça ao mesmo agente para produzir e revisar o mesmo texto.

## Tarefas (um prompt de partida por sessão; nunca duas tarefas na mesma sessão)
- `orquestradores/LOTE.md` — produz e revisa um lote (v1 → QA1 → v2 → QA2 → RECONCILIADO).
- `orquestradores/BANCO.md` — varredura de certames e registro no banco.
- `orquestradores/SIMULADO.md` — monta um simulado numerado.
- `orquestradores/DISCURSIVA.md` — corrige uma resposta de discursiva/peça em dupla cega.

## Gates (parar, gravar o que houver, imprimir a linha indicada, não continuar)
- QA reprovou > 30% dos itens de um lote: "GATE: QA reprovou >30% — decisão humana".
- Afirmação sobre ferramenta/norma sem fonte datada após QA2: vai para "pendente" no RECONCILIADO; nunca aprovar.
- Fonte não oficial (espelho, blog, cursinho) proposta como proveniência: recusar e registrar.
- Qualquer necessidade fora do escopo dos dois módulos: "GATE: fora do domínio — decisão humana".
- Fim de tarefa: "GATILHO A — aguardando decisão humana". Nunca iniciar outra tarefa.
Nada produzido aqui vai à candidata; tudo é material para revisão humana.

## Formato de arquivos gravados
Primeira linha: `# [arquivo] — [tarefa] — [data ISO] — gerado por [agente]`. Markdown simples. Itens AUTORAL: `A<lote>-NN`, enunciado, gabarito C/E, justificativa de duas linhas, marcador [TS] quando houver troca sutil.
