# FÁBRICA CÂMARA 2026 — v1 — guia do Fundador

## Instalação (ordem obrigatória — lições do piloto)
1. Descompacte a pasta inteira. Confira a árvore: `.claude/agents/` com 10 arquivos, `orquestradores/` com 4, `lotes/lote1..5/DESPACHO.md`, `edital/`, `regras/`, `estado/`, `banco/`, `saida/`. Pastas e arquivos com ponto são ocultos: ative "mostrar ocultos".
2. Libere na política de rede do ambiente do Claude Code, ANTES de abrir a sessão: cdn.cebraspe.org.br, cebraspe.org.br, planalto.gov.br, www2.camara.leg.br, learn.microsoft.com, help.tableau.com, tableau.com, docs.cloud.google.com, cloud.google.com, platform.openai.com, docs.aws.amazon.com. Sem isso, agentes de produção e QA ficam sem fonte e o gate de evidência bloqueia.
3. Só então abra o Claude Code dentro da pasta. Subagentes criados depois de aberta a sessão não carregam (foi o que aconteceu no piloto). Confira com `/agents` que os 10 aparecem.
4. Modelos: os agentes usam aliases `sonnet`, `opus`, `haiku` (verificados na documentação do Claude Code em 8/10/2026). Produção em sonnet e QA em opus é a regra de separação. Se quiser produção em modelo maior, edite `model:` nos arquivos `*-cpp.md` para um ID completo aceito pela sua conta — verifique na documentação; não chute.

## Operação
- Uma tarefa por sessão. Abra a sessão, cole o conteúdo do prompt de partida (`orquestradores/LOTE.md` com o N trocado, ou BANCO, SIMULADO, DISCURSIVA) e espere o "GATILHO A — aguardando decisão humana".
- Antes de cada sessão, copie o Estado_Canonico_Camara_2026.md mais recente do Projeto (claude.ai) para `estado/` se houver mudança lá; depois da sessão, leve o `estado/ESTADO_CANONICO.md` atualizado de volta ao Projeto. Esse é o único transporte que sobra.
- O que levar à Presidência: o resumo impresso + o RECONCILIADO.md (ou relatório da varredura / simulado / reconciliado da discursiva). Nunca os intermediários, salvo pedido.
- Autorizações já dadas: BANCO pode rodar agora. LOTE 2 e 3, SIMULADO e DISCURSIVA aguardam o veredito do QA comparativo do Lote 5 (D-PILOTO-RESULTADO). LOTE 1 e 4 estão em produção manual no claude.ai — não rodar aqui sem ordem da Presidência.
- Métricas a anotar por sessão: tempo seu, intervenções, gates disparados, itens aprovados/reprovados.

## O que a fábrica não faz
Não entrega nada à candidata; não decide mérito de divergências; não cria lotes ou agentes por conta própria; não usa fonte não oficial. Tudo isso é humano, por desenho.
