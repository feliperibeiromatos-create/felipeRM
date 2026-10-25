# Kit fábrica v2 — 24/10/2026 — como entrar no repositório felipeRM

Copie o conteúdo desta pasta para a raiz do clone (C:\Users\Felipe\felipeRM_push ou a pasta E:\ da Fase 0 do FAB-AUTO), preservando os caminhos:

- claude/ESPEC_curso_DA_formato_v2_2026-10-24.md — especificação do formato DA-v2 (também gravada no Projeto, em DAD/)
- claude/PADRAO_UNICO_v1_1_adendo_DA-v2.md — proposta de adendo (o Fundador adota ou não)
- claude/PLANO_implementacao_Dossie_DAD_v1_2026-10-24.md — plano (cópia do Projeto)
- claude/kit_pacote/checa_pacote_v2.py — conferência de pacote com as regras v2 (testado: idêntico ao v1 em pacotes sem DA-v2; bloqueia os defeitos da ESPEC v2)
- .claude/agents/gcb-cqfp-didatico.md — agente de QA didático (Opus, sem Edit)
- ordens/ORDEM_DA_QA12.md, ORDEM_CD2026_LOCALIZAR.md, ORDEM_BANCO_DA_CDN_ONDA1.md, ORDEM_DA_V2_FASE1.md
- banco/candidatos/ — fila v2 de 1.321 candidatos (7 cadernos TEC; localizador, não fonte), com enquadramento/mecanismo do pacote de auditoria v1 como ponto de partida, e resumos v2 por prova e por item (a fila v1 de 1.000 fica como histórico)
- regras/estilo_banca_DA_v1.md — estilo da banca em DA medido em 1.118 itens C/E (equilíbrio, gatilhos, comandos, mecanismos, regras de produção propostas)
- TAREFAS_linhas_para_colar.md e PROMPT_DE_PARTIDA_sessao_fabrica.md — não vão para o repositório: são para colar em TAREFAS.md/DECISOES.md e na sessão

Sequência sugerida:
1. git pull; copiar os arquivos; `git add -A && git commit -m "fábrica: kit DA-v2 (ESPEC v2, checa_pacote_v2, QA didático, 4 ordens, fila BANCO-DA)"`; git push (junto com os 5 commits pendentes de 20/10 e o zip da higiene em saida/arquivo_projeto/).
2. Colar as linhas de TAREFAS_linhas_para_colar.md em TAREFAS.md e DECISOES.md; commit.
3. Abrir a sessão da Fábrica com PROMPT_DE_PARTIDA_sessao_fabrica.md.
4. Em paralelo (sessão de design, não a Fábrica): v17 na prévia lendo os campos da ESPEC v2; regressão R3 passa a conferir tarefas, GLOSSÁRIO, CASO, ITEM e fechamento na tela.

O que esta sessão NÃO fez e por quê: não executou nada na Fábrica (sem acesso ao repositório daqui, HTTP 403); não alterou o PADRAO_UNICO (matéria do Fundador); não publicou nada na plataforma (D-AUDITORIA-20OUT).

# Acréscimo de 25/10/2026 (noite) — o que esta sessão Cowork gravou direto no clone
Gravado pela ponte com o computador (sem git daqui): o Fundador faz `git add -A && git commit -m "fábrica: ciclo contínuo v2, FILA, ESTILO v1.1, zip da higiene" && git push`.
- orquestradores/CICLO_CONTINUO_v2_proposta.md — critério de parada, fila, laço v2 (prompt pronto) e as decisões que faltam; reconciliado com TAREFAS/DECISOES/PARA_FUNDADOR da s18.
- ordens/FILA.md — leitura ordenada de TAREFAS.md (não é um segundo estado); a secretaria reescreve a cada ciclo.
- DECISOES_linhas_novas_2026-10-25.md — 8 linhas NOVA prontas (D-CICLO-V2, D-V17-1-PUBLICAR, D-ONDAS, D-INLINE-REFAZER, D-D18-D30, D-MULTI-IA, D-CEGO-2-D6, D-REDE-GOVBR); trocar [SIM/NÃO], colar no fim de DECISOES.md, apagar este arquivo.
- regras/estilo_banca_DA_v1.md — v1.1: só a frase da seção 4 apontada pela QA R3/R5 ("o item LITERAL é quase sempre CERTO", não o inverso).
- saida/arquivo_projeto/arquivo_projeto_higiene_2026-10-23.zip — backup byte a byte dos 70 documentos apagados do Projeto em 23/10 (MANIFESTO com SHA-256; D-HIGIENE).
Não tocado: ordens/ORDEM_*.md, claude/, .claude/agents/, TAREFAS.md, DECISOES.md, PARA_FUNDADOR.md (todos alterados pela s18 em 25/10 e mais novos que o kit da manhã).
