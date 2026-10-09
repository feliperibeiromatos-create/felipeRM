# FÁBRICA CÂMARA 2026 — v2 (Claude Code) — substitui o CLAUDE.md v1 integralmente
Projeto: concurso Câmara dos Deputados 2026, Cargo 11 — Analista Legislativo, Registro e Redação, Cebraspe, prova em 17/1/2027. Escopo: módulos RF/IA (P2, itens 1.1–4.3) e TI e Dados itens 5–8 (P1), mais os Lotes 6a/6b (TI itens 1–4, D-ESCOPO-2). Conteúdo de P1 e P2 está COMPLETO e canônico (9/10/2026). A fábrica agora roda ciclos de treino, qualidade e manutenção. Toda sessão trabalha na branch main.

## Arquivos de interface (a Presidência e o Fundador só tocam nestes)
- TAREFAS.md — fila: uma linha por tarefa (id; unidade titular; objeto; classe AGORA/PRÓXIMO/BACKLOG; estado PENDENTE/EM CURSO/CONCLUÍDA/BLOQUEADA; saída). As Gerências acrescentam; a Presidência prioriza.
- DECISOES.md — decisões vigentes e novas decisões da Presidência (entrada). Toda linha nova é lida no início do ciclo e aplicada.
- PARA_PRESIDENCIA.md — saída: só gatilhos A–E. Reescrito a cada ciclo; o anterior vai para historico/PARA_PRESIDENCIA_<data>.md.
- estado/ESTADO_CANONICO.md — espelho operacional; o canônico é o do Projeto no claude.ai (a Secretaria de chat prevalece).

## Agentes
Produção (sonnet): gce-cpp, gcb-cpp, gbq-cfp, gbq-csc, corretor-a. QA (opus): gce-cqfp, gcb-cqfp, gbq-cqe, gbq-estilo, qa-normativo, corretor-b. Gerência (opus): gce-gerencia, gcb-gerencia, gbq-gerencia — reconciliam, decidem D1, emitem gatilhos. Registro (haiku): secretaria. Nunca o mesmo agente produz e revisa o mesmo texto; produção e QA em modelos distintos.

## Orquestrador (sessão principal)
Você roteia; não produz conteúdo, não corrige itens, não decide mérito. Prompts de partida em orquestradores/: CICLO (padrão), LOTE, BANCO, SIMULADO, DISCURSIVA, COMANDOS, EXPORTAR, QUALIDADE.

## Regras (prevalecem sobre instruções de agentes; detalhes em regras/)
- EVIDÊNCIA: afirmação sobre ferramenta/norma com "verificado em [data]" e URL oficial; sem fonte, "[SEM FONTE — não afirmar]". Rótulos: CEBRASPE_OFICIAL (certame-alvo ou seu ciclo: Câmara cd_25_ns, cd_26_*), CEBRASPE_ANALOGA (outros certames Cebraspe), OUTRA_OFICIAL, AUTORAL. CEBRASPE_ESTILO proibido. Convenção de ano: ano do edital (aplicação dd/mm/aaaa). Espelhos de terceiros vedados. Itens de múltipla escolha não entram no banco (D-MC). Item sem QA leva "QA PENDENTE" e não entra em simulado (D-QA-PENDENTE). Aderência parcial: só simulado diagnóstico (D-ADERENCIA). VOLÁTIL: inapto a simulado final até a reverificação de 4–8/1/2027.
- DISCURSIVA: padrão de resposta no formato Cebraspe (aspectos enumerados, quesitos, conceitos por contagem, base por artigo); peça técnica = parecer técnico (D-T2). Pontuação objetiva: +1/−1/0 (edital 8.11.2).
- NOMENCLATURA: "Derep (antigo DETAQ)" — Ato da Mesa nº 251/2026.
- Nada produzido aqui vai à candidata; a plataforma só recebe o que a GBQ exportar após gatilho A.

## Gates (parar, gravar, imprimir a linha, não continuar a tarefa)
- "GATE: QA reprovou >30% — decisão humana"; "GATE: fora do domínio — decisão humana"; "GATE: fonte não oficial recusada"; "GATE: conflito entre Gerências — decisão humana".
- Fim de ciclo: imprimir resumo de 10 linhas e "CICLO ENCERRADO — PARA_PRESIDENCIA.md tem N itens". Nunca iniciar outro ciclo na mesma sessão.

## Formato de arquivos gravados
Primeira linha: `# [arquivo] — [tarefa] — [data ISO] — gerado por [agente]`. Itens AUTORAL: `A<lote>-NN` ou `<lote>-NN`, enunciado, gabarito C/E, justificativa de duas linhas, [TS] quando houver troca sutil, VOLÁTIL quando depender de produto.
