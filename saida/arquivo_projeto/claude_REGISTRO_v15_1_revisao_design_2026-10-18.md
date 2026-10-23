# Plataforma Câmara 2026 — revisão de design da prévia v15 → v15.1 (18/10/2026)

Pedido do Fundador (passagem de bastão, item 2): revisar a v15 com a skill design-plataformas-interativas e corrigir na própria prévia, sem publicar na plataforma da candidata.
Prévia: https://claude.ai/artifact/KyVNQZCzQzLbuuv4KXwibU — versão anterior 1792353020-d66e (v15); versão nova 1792354627-91f8 (v15.1). Corpo publicado sha256 4f25704ea6623fca…; conferido na releitura: igual ao arquivo local.
Não tocadas: plataforma da candidata (NePvzy9…), laboratório (5fyX…), prévia v14 (2QxJ…).
Inalterados: pacote embutido PUB_INLINE (byte a byte igual ao da v15), chaves c2026.v01.*, formato do estado. Nenhum campo novo no estado.

## 1. Como revisei
Chromium headless (Playwright), 360, 390 e 1280 px, tema claro e escuro, em todas as telas: apresentação, concurso, disciplinas, Painel, as duas matérias, os 40 cursos, bloco de questões, resultado, Erros, Resumo e leitura de resumo, Recomendações, prática de prova, diagnóstico, discursiva, véspera e dados. Medi rolagem lateral, alvos de toque (<44 px), contraste de cada texto contra o fundo efetivo (WCAG AA) e vazamento de metadados no texto visível. Li as capturas.

## 2. Achados na v15 e correção
| # | Achado (evidência) | Correção na v15.1 | Princípio |
|---|---|---|---|
| 1 | Marcas internas no texto que a candidata lê: [V 07/10/2026 — F4], [NORMATIVO — QA], [F12], (F4, seção…), "par C14", "Difere do item A5-10…", "(ver L2-Q06)", prefixos TC/IC/GI/AT, "(v2, item 1.4)", "Só o fato e a fonte." (604 ocorrências nas justificativas, cursos, resumos e pegadinhas) | Limpeza só na exibição (limpaProd, chamada por limpaRef): verificação vira "(verificado em DD/MM/AAAA)"; base legal fica "(LGPD, art. 5º, I)"; códigos de fonte, de item e de par saem; TC/IC/… vira "Armadilha do item:". Em quadro-síntese, o trecho removido vira espaço para não desalinhar colunas. Restam 146 códigos de fonte (F1…F22) e 6 menções a "QA" dentro de frases (ex.: "exemplos do F4"), que dependem de reescrita: ficaram para a Fábrica (ordem C) | Confiança, carga cognitiva |
| 2 | Pegadinha repetida: o curso mostra o quadro "Pegadinha provável" e o fim do tópico repete o mesmo texto (36 dos 39 tópicos com pegadinhas tinham todas repetidas) | Fim do tópico mostra aberta só a pegadinha que não aparece no texto; as repetidas ficam em lista recolhida "Rever em lista…". A Recomendação C abre essa lista | Carga cognitiva |
| 3 | Tabela do curso cortada no celular sem sinal de que rola (P2-1.4: terceira coluna escondida) | Até 480 px a tabela vira cartões, com o nome da coluna em cada valor; quadro-síntese largo ganha "Deslize o quadro para o lado para ver tudo →" | Responsividade |
| 4 | Linha de quadro tratada como tabela de uma linha só, que no celular ficava com altura 0 (P2-1.8, "translation)") | Linha com barras dentro de um quadro aberto continua no quadro | Responsividade |
| 5 | Resumo em bloco único de texto (L1: 354 palavras num parágrafo) | Cada linha que começa com número do edital ou RÓTULO: abre parágrafo, com o início em negrito | Carga cognitiva |
| 6 | Usuária nova vê no Painel o aviso "Diagnóstico de 30 itens" logo depois da tela que já oferece o diagnóstico; duas ações principais na mesma tela | O aviso fica só para quem nunca passou pela tela de disciplinas (usuária migrada) | Próximo passo claro |
| 7 | Contador "1 de 6" quebrando em três linhas no cabeçalho do bloco (360 px) | Contador sem quebra | Responsividade |
| 8 | Plurais: "Revisar 1 itens", "1 item(ns)", "Revisar os 1 mais errados" | Singular e plural corretos em Erros, Recomendações e confirmação de entrega | Clareza |
| 9 | "sem respostas" solto no fim de "Pratique este tópico" | "Nota do tópico: …" só aparece quando há respostas | Clareza |
| 10 | Resumos recolhíveis ("ver comando", "Dados técnicos", "Como as recomendações são calculadas") com 32 px de altura | 44 px | Acessibilidade |
| 11 | Links "curso"/"questões" no resumo com 31 px de largura | 44 px | Acessibilidade |
| 12 | Quadro de pegadinha dentro do curso em cinza menor, diferente do quadro do fim | Mesma cor e tamanho | Consistência |
| 13 | "Item inédito do Projeto" (linguagem interna) | "Questão inédita (não saiu em prova anterior)" | Confiança |

Sem achado: rolagem lateral (nenhuma tela, nos 6 cenários), contraste (nenhum texto abaixo de 4,5:1 nos dois temas), erros de JavaScript (nenhum).
Falsos positivos da medição, sem correção: links dentro de correção recolhida (link inline é exceção da regra de alvo); região rolável do quadro (não é alvo de toque); "lote" como termo técnico (transcrição em lote) e "F4" como tecla do Excel.

## 3. Testes da v15.1 (129/129)
Pacote idêntico; chaves; usuária nova (apresentação → concurso → disciplinas → Painel, sem aviso repetido, uma ação principal); bloco de questões até a nota aparecer com 30 respostas (+30/30 com acerto total); curso com pegadinhas recolhidas, tabela em cartões, quadro sem tabela vazia e colunas na mesma posição do texto-fonte; migração de estado da v14 (tentativa, erro, rascunho e escolhas preservados; 3 respostas convertidas; apresentação "A plataforma mudou de forma" uma vez); usuária da v12 vê o aviso do diagnóstico; Erros e Recomendações no singular; Exportar meus erros (sem capacidade de download: cai na área de transferência ou na caixa de texto, JSON válido); carregar outro pacote.json e voltar ao publicado com o progresso intacto; diagnóstico de 30 entregue e registrado; limpeza sem código de item, de par, de fonte entre colchetes ou de QA nas justificativas, cursos e resumos; resumo em parágrafos; sem rolagem lateral em 13 telas × 6 cenários; resumos recolhíveis com 44 px.

## 4. Não verificado
Celular real, leitor de tela, teclado completo, download real (a prévia continua sem a capacidade de download, decisão pendente com o Fundador). A limpeza é por expressão regular: pode haver caso raro que eu não vi; o inventário completo está em claude/INVENTARIO_marcas_producao_v1.9_2026-10-18.md.

## 5. Decisões provisórias mantidas (não mexi)
CONTA_REPETIDAS=true; peso = 90 ÷ nº de matérias; LIM_DISC 50%; LIM_SIM 60% e 7 dias; "Exportar meus erros" sem capacidade de download.
