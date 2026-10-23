# DPE-01 v0.1 — Execução 1 (18/10/2026): EXTRAIR + REVISAR

Objeto: plataforma publicada https://claude.ai/artifact/5fyXGpFMomSHwZuRnu36rC, versão 1792332640-8bc6 (pacote v1.9 embutido). Edital: Câmara 2026, cargo 11. Executor: Claude (parte interessada: autor do prompt). Nada foi alterado nem publicado.

Verificado: CSS e JS lidos no arquivo; renderização em Chromium headless a 360 px e 1280 px, temas claro e escuro, 6 telas + folha de respostas + lote em leitura, com estado sintético; contraste calculado pela fórmula WCAG sobre os tokens. NÃO verificado: celular real, leitor de tela, ordem de tabulação, exportação de erros, carga de outro pacote.

## EXTRAIR — tokens (todos "lido do CSS"; sistema visual v0.2 da CDJ, 13/10/2026)

| Token | Claro | Escuro | Uso |
|---|---|---|---|
| --paper | #FBFBF8 | #14181E | fundo |
| --ink | #1B2A41 | #ECEEF1 | texto, botão primário, bordas fortes |
| --ink-2 | #4F5B6B | #AEB5BF | texto secundário |
| --rule | #D9DCE1 | #2F343C | divisórias, trilho de barra |
| --soft | #F1F2EE | #1E232A | caixa de comando, desabilitado |
| --marker | #F2C94C | #E2BB45 | aba ativa, pílula amarela |
| --marker-soft | #FFF7D6 | #2E2A1A | destaques .hl (nota de vigência, "por onde começar") |
| --c / --e | #2E7D5B / #9C2E2E | #5EBE92 / #E27A7A | acerto / erro, pílulas |
| --focus | #1B6BB2 | #7DB8F0 | contorno de foco 3 px |
| Fonte | Atkinson Hyperlegible 400/700 (Google Fonts) | | corpo 17 px (18 px ≥ 600 px) |
| Escala | h1 26 · h2 21 · h3 17 · small 14 · xs 13 | | |
| Forma | raio 8 px; botão 56 px (grande 64); borda 2 px; coluna 560 px; margem 18 px | | |

Componentes: header.top, .btn / .btn.primary / .btn.big, .card / .card.on, .hl, .vazio, nav.tabs com badge, .bolha C/E (80 px; 64 no caderno), .pill v/a/g/n, .barras, .ped (linha do painel), .folhad (folha discursiva), .chk (véspera), toast.

Contraste medido (texto, mínimo 4,5): claro 4,82 (verde sobre papel) a 13,93; escuro 6,06 a 15,32 — todos passam. Não-texto: indicador dourado da aba ativa 1,53:1 no claro (estado também marcado por negrito e cor de texto, então não depende só de cor).

## REVISAR — achados verificados

| # | Achado | Evidência | Ponto violado | Proposta | Risco a dados |
|---|---|---|---|---|---|
| 1 | Plataforma cobre 2 de 9 disciplinas do cargo 11 e o Painel não mostra isso (ERRATA 18/10: a versão anterior dizia 10 e incluía Comunicação Social na P1; Comunicação Social é específica do Cargo 1) | Edital 14.2.3/14.2.4: P1 tem Português, Inglês, Dir. Adm./Adm. Pública, Dir. Const./RICD, TI e Dados; P2 tem Linguística, Fala/Transcrição/IA, Processo Legislativo/Regimentos, Ciência Política. Pacote: 47 itens de edital, só TI e Fala | 9 e progresso honesto | Painel lista todas as disciplinas; as sem conteúdo aparecem como "ainda sem conteúdo" | nenhum (só leitura) |
| 2 | Rolagem horizontal na trilha a 360 px | scrollWidth 362; lista "2.1 · … · 2.8" com nowrap; título "Lote 3 · IA / no / Parlamento" quebra em 5 linhas | largura 360 | permitir quebra dos números ou movê-los para a 2ª linha do cartão | nenhum |
| 3 | "deixar em branco" avança para o próximo item; C e E não avançam | código vProva: bB faz i++ | regra dos botões | rótulo "Deixar em branco e seguir" ou não avançar | nenhum |
| 4 | No 1º bloco do lote, botão desabilitado diz "Início" | captura lote 360 | regra dos botões | esconder o botão ou rótulo "Primeiro bloco" | nenhum |
| 5 | Mensagem "Pacote carregado: N itens" apagada por render() | código vDados: msg preenchida e render() em seguida (toast de 2,6 s permanece) | 9 / confiança | gravar a mensagem no estado de tela antes do render | nenhum |
| 6 | Cabeçalho quebra em duas linhas a 360 px | captura estudo 360 | 2 | encurtar para "Câmara 2026 · Reg. e Redação" ou 15 px | nenhum |
| 7 | "Próximo" / "Anterior" sem objeto | folha de respostas | regra dos botões (baixa) | "Próximo item" / "Item anterior" | nenhum |

Sem achados: contraste de texto, alvos de toque (checkbox de 28 px está dentro de rótulo de 52 px), confirmação de "Apagar meu progresso", legenda do painel, avisos de vigência.

## Divergências entre o prompt v0.1 e o CSS (para a v0.2 do prompt)
1. A cor de destaque não é exclusiva da aba ativa: --marker-soft é o fundo de todos os destaques .hl.
2. A família tipográfica é Atkinson Hyperlegible (explica o zero cortado).
3. A margem lateral real é 18 px, não 16 px.

## Execução 2 (18/10/2026): IMPLEMENTAR achados 1 a 7 — em cópia, aguardando "sim"

Autorização: Felipe ("Pode corrigir os achados de 2 a 7, bem como deixar claro o que falta, considerando o achado 1"). A versão da candidata (5fyXGpFMomSHwZuRnu36rC) NÃO foi alterada. Prévia privada: https://claude.ai/artifact/1rJinXCvnYiA8JMnEtSEHW (versão 1792342756-b958).

| Achado | Correção |
|---|---|
| 1 | Painel ganhou "Cobertura do edital": as 9 disciplinas por prova (P1 e P2, 90 itens cada, edital 7.1, 14.2.3, 14.2.4), com "N itens · curso" ou "ainda sem conteúdo"; a trilha diz "cobre 2 das 9 disciplinas" com botão "Ver o que falta". A contagem é calculada do pacote, então se atualiza quando entrarem novos módulos. |
| 2 | Números do edital nos cartões de lote podem quebrar linha; o título ocupa a largura. |
| 3 | Rótulo "deixar em branco e seguir" (no último item, "deixar em branco"); comportamento mantido. |
| 4 | No 1º bloco do lote não há botão de voltar; nos demais, "← 1.1" etc. |
| 5 | Mensagem do pacote guardada antes do render; aparece também em "Voltar ao publicado" e some ao reabrir a tela. |
| 6 | Até 400 px de largura, cabeçalho "Câmara 2026 · Reg. e Redação" em 16 px: uma linha. |
| 7 | "Item anterior" / "Próximo item". |

Regressão automatizada (Chromium headless, estado sintético): 67 verificações, 0 falhas — simulado P2 respondido e entregue; caderno de erros atualizado; exportar erros produz saída; carregar outro pacote.json; voltar ao publicado; progresso e chaves c2026.v01.* intactos; pacote embutido idêntico byte a byte; sem rolagem horizontal e cabeçalho em 1 linha em 6 telas × 360/1280 px × claro/escuro; nenhum alvo de toque < 44 px; fonte Atkinson carregada. Sensibilidade conferida no original (362 px e 2 linhas). NÃO verificado: celular real, leitor de tela, teclado. Limitação da prévia: não declara a capacidade "downloads", então lá "Exportar meus erros" cai na cópia de texto; ao republicar na URL da candidata a declaração existente é mantida.

Conteúdo que falta (para a Fábrica, não para o design): P1 — Língua Portuguesa; Língua Inglesa; Noções de Direito Administrativo e Administração Pública; Noções de Direito Constitucional e de Regimento Interno da Câmara dos Deputados. P2 — Linguística; Processo Legislativo e Regimento Interno da CD, Regimento Comum do CN; Ciência Política. Nas duas disciplinas cobertas, todos os subitens-folha do edital têm itens (TI e Dados: 176; Fala, transcrição e IA: 158). As 5 discursivas do pacote não cobrem as 3 disciplinas específicas sem conteúdo.

### Publicação (18/10/2026)
Autorizada por Felipe ("Sim... pode publicar"). Publicada na URL da candidata como versão 12 (id 1792342912-c3ff), conteúdo idêntico à prévia salvo o título. Capacidade "downloads" mantida. Pós-publicação: versão lida de volta, pacote embutido idêntico ao anterior, regressão automatizada repetida sobre o publicado: 67 verificações, 0 falhas. O progresso da candidata fica no navegador dela e não foi tocado (mesmas chaves c2026.v01.*). Versão anterior para reversão: 1792332640-8bc6.
