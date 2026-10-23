# Plataforma Câmara 2026 — v15.5 no laboratório: módulo Direito Administrativo (19/10/2026)

Pedido do Fundador (19/10): deixar o curso de Direito Administrativo mais bonito e automatizar a criação; "pode começar sem mim".
Prévia (laboratório): https://claude.ai/artifact/KyVNQZCzQzLbuuv4KXwibU — versão 1792458611-3067. Base: prévia v15.4 (versão 1792381667-d397), igual em código à plataforma publicada v15.4 (versão 1792404196-59b0). Plataforma da candidata NÃO tocada.
Inalterados: pacote embutido F4 v1.12 (749 itens), chaves c2026.v01.*, formato do estado.

## O que mudou no código
- Módulo Direito Administrativo: questões e tópicos com itemEdital `P1-DA-…` (ou `DA-…`) vão para "Noções de Direito Administrativo e Administração Pública", não para TI. Os títulos `## 2.1 …` de um lote de DA ligam a `P1-DA-2.1`. Matéria com curso e ainda sem questões já aparece (curso pode chegar antes do banco).
- Componentes novos: quadro BASE LEGAL no texto do curso; visual `baseLegal` (dispositivos com referência, texto, "texto da lei" ou "paráfrase" e data de conferência; sem data aparece "não conferido" em vermelho); visual `compare` (dois lados com cabeçalho escuro, um aspecto por linha, legível a 360 px).
- Leitura: título longo do tópico com fonte menor; grupos do edital sem nenhum tópico com conteúdo não aparecem mais na matéria; texto da aba Resumo atualizado agora que cada tópico tem resumo.
- Demonstração de formato (só laboratório): `DEMO_DA=true` acrescenta o edital de DA (46 entradas, texto do edital) e três tópicos de exemplo (1.2, 2.1, 4.4) com textos marcados "[demonstração de formato]" e aviso vermelho em cada tela. Some sozinha quando o pacote traz DA; o embute_pacote.py desliga em toda cópia para publicação.

## Testes
- Regressão do kit (R1–R9 e a nova verificação "cada tópico e cada questão na matéria certa"): 23/23 na prévia com demonstração, 23/23 na cópia sem demonstração (equivalente à publicação), 23/23 com um pacote de teste que traz DA de verdade (12 questões de DA, Compare e Base legal conferida), sem nenhuma questão de DA cair em TI.
- Conferência estendida: o pacote de teste correto passa; o pacote com defeito plantado é barrado nos 3 pontos plantados (lote misturando DA e TI, linha de Compare com 2 células, Base legal sem data de conferência).
- Telas de DA (Painel, matéria, três cursos, Resumo e resumo do tópico) em 360, 390 e 1280 px, claro e escuro: sem rolagem lateral, alvos de toque de 44 px ou mais, contraste AA. Não testei em celular real nem com leitor de tela.

## Observação sobre o pacote v1.12
Já há tópicos com 30 questões (P1-5.2, P2-1.2 a 1.8 e P2-4.1), então a nota por tópico já é possível neles. Nenhum chega a 40.

## Documentos
claude/ESPEC_curso_DA_formato_v1_2026-10-19.md (formato e regras); claude/ORDEM_DA_FORMATO_2026-10-19.md (ordem à Fábrica, PRÓXIMO, depende do Fundador colar e decidir a cota); claude/kit_pacote/ (conferência, embutir e regressão atualizados).
