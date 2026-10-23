# Onboarding multiconcursos — Fase 1 (18/10/2026)

Base: PROMPT-ONBOARDING-MULTICONCURSOS-CARGO11-v1.0 (GPT), executado na Fase 1 com as decisões do Fundador de 18/10/2026. Executor: Claude (Cowork). Nada publicado; plataforma da candidata intacta (versão 12, id 1792342912-c3ff).

## Decisões do Fundador que alteram o prompt v1.0
1. Produto geral (MapasPro), só com o concurso da Câmara por enquanto.
2. Diagnóstico de 30 itens por disciplina (o prompt dizia 50). Lançar para a candidata quando houver diagnóstico em pelo menos uma disciplina (substitui a condição da Fase 3 de "todas as disciplinas").
3. GPT autorizado para revisão independente (matéria reservada; registra exceção à regra "tudo roda exclusivamente em Claude").

## 1. Leitura efetiva
Lidos: HTML v12 inteiro (funções vInicio, vBoas, vEntrada, listaSimulados, iniciar, entregar, vResultado, loteAtual, vPainel e o botão "mudar"); pacote embutido v1.9 (334 itens, 4 simulados, 10 lotes); edital (7.1, 8.11.2, 9.1, 14.2.3, 14.2.4, Anexo I). NÃO ACESSADO: prototipo-entrada-camara-cargo11-v01.html (só a imagem do mockup).

## 2. Fluxo atual × novo
| Etapa | Hoje (v12) | Novo |
|---|---|---|
| Primeira visita | boas-vindas → escolha por módulo (P1 = TI, P2 = Fala) → estudo | concurso (1 toque) → disciplinas (escolha opcional, não bloqueia) → estudo |
| Escolha | S.escolha.P1/P2 = "diag" ou "zero" | por disciplina, id estável (cd26-c11/p1/ti, cd26-c11/p2/fala…) |
| Diagnóstico | recorte do Simulado 0: 43 itens (TI), 17 (Fala) | 30 itens por disciplina, lista fixa revisada, por subitem |
| Mudar | "mudar" no Painel, sem registro de evento | "Mudar meu caminho", com evento novo caminho_mudado |

Migração (candidata já usa a v12): S.concurso = "cd26-c11" sem passar pela tela 1; S.escolha.P1 → cd26-c11/p1/ti e S.escolha.P2 → cd26-c11/p2/fala (o código prova que P1 é exatamente TI e P2 exatamente Fala); S.escolha é mantido, não apagado. Eventos antigos não são reinterpretados; toque_escolha_caminho ganha o campo disciplina. Tentativas antigas (DIAG-P1/DIAG-P2) continuam no histórico com o nome original. Chaves c2026.v01.* e PUB_INLINE inalterados.

## 3. Telas
Prévia visual: https://claude.ai/artifact/FsV9s9Tw99MiLwDsAzLY8L (privada). Explicação das duas opções: 66 palavras, antes dos botões. Disciplinas sem conteúdo aparecem como "em preparação", sem botões inativos (desvio deliberado do T03, que pedia SIM/NÃO nas nove).

## 4. Matriz de cobertura
| Disciplina | Itens | Curso | Diagnóstico de 30 |
|---|---|---|---|
| Língua Portuguesa | 0 | em preparação | indisponível |
| Língua Inglesa | 0 | em preparação | indisponível |
| Dir. Administrativo e Adm. Pública | 0 | em preparação | indisponível |
| Dir. Constitucional e RICD | 0 | em preparação | indisponível |
| TI e Dados | 176 | disponível | viável: 30 únicos, 18/18 subitens, 5 do SIM-0, 18 autorais + 12 Cebraspe análogos, 14 C / 16 E |
| Linguística | 0 | em preparação | indisponível |
| Fala, Transcrição e IA | 158 | disponível | viável: 30 únicos, 23/23 subitens, nenhum do SIM-0, 30 autorais, 13 C / 17 E |
| Processo Legislativo e Regimentos | 0 | em preparação | indisponível |
| Ciência Política | 0 | em preparação | indisponível |

Regra: elegível = não volátil, aderência plena, fora de SIM-1, SIM-2 e SIM-0-P2; 1 por subitem, resto aos subitens com mais elegíveis (empate pela ordem do edital); dentro do subitem, fora do SIM-0 primeiro, depois por id. Seleção exportada em diag30_selecao_para_revisao.json (60 itens, sha256 0ab3e493).

## 5. Pendências e autorização
- Revisão independente (GPT) da seleção de 60 itens: gabarito, aderência ao subitem, repetição de ideia, equilíbrio C/E.
- Decisão: ao lançar o diagnóstico de 30, esconder os diagnósticos antigos (43/17) da lista de simulados? Recomendado: sim, mantendo o histórico.
- Decisão: TI usa 5 itens do Simulado 0; se a candidata fizer depois o Simulado 0 completo, verá esses 5 de novo. Aceitável ou retirar?
- Fase 2 (prévia funcional em cópia) começa após aprovação das telas. Publicação só com "sim".
