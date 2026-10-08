# PILOTO DE AUTOMAÇÃO — LOTE 5 — como rodar

1. Instale o Claude Code seguindo a documentação oficial: https://docs.claude.com/en/docs/claude-code/overview (não reproduzo comandos de instalação aqui para não citar versão sem fonte datada; a página oficial está sempre atual).
2. Descompacte esta pasta em um local qualquer e abra o terminal dentro dela (ou abra a pasta no app desktop, aba Code).
3. Antes de iniciar, confira o modelo da sessão principal: o subagente gcb-cpp usa `model: inherit` (herda o modelo da sessão). Para manter a regra "produção e QA em modelos distintos", a sessão principal deve estar em um modelo diferente de Opus — idealmente o mesmo que usamos na CPP do claude.ai. Se não for possível, troque no arquivo `.claude/agents/gcb-cpp.md` o campo `model` por um alias aceito (a documentação lista `sonnet`, `opus`, `haiku`, `inherit` ou ID completo de modelo).
4. Inicie o Claude Code e cole o conteúdo de `KICKOFF.md`.
5. Ao final, você terá em `saida/lote5/`: v1_producao.md, qa1_relatorio.md, v2_producao.md, qa2_relatorio.md e RECONCILIADO.md.
6. Leve o `RECONCILIADO.md` à GCB-CQFP do claude.ai (a mesma que revisa os lotes manuais) para a comparação de qualidade. Só depois disso a Presidência decide se o piloto vira regra.

O que este piloto NÃO faz, de propósito: não entrega nada à candidata; não cria outros lotes; não decide divergências de QA (lista-as para você).
Anote o tempo que você gastou e o número de intervenções manuais: é a métrica do piloto.
