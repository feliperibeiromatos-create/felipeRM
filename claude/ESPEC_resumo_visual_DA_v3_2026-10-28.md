# ESPEC — Resumo visual de Direito Administrativo (formato v3.1) — plataforma v17.3

28/10/2026 · sessão Cowork (Fable), por ordem do Fundador (28/10: "sim; (a); sim; ordem do edital em levas de 3"). Fonte da estética: os 16 resumos de Direito Administrativo da MapasPro (marca do Fundador). Fonte do conteúdo: o pacote canônico da plataforma (resumo, visuais e base legal já conferidos) e o texto das leis; os resumos MapasPro entram como conteúdo só depois de conferidos (seção 5 e a triagem em TRIAGEM_resumos_MapasPro_DA_2026-10-28.md).

## 0. Decisões do Fundador que esta ESPEC aplica
1. Conteúdo dos resumos MapasPro pode entrar, com QA normativo (não é material de terceiro; a D-ESTRATEGIA não se aplica).
2. Estética traduzida para o sistema visual v0.2 da plataforma (opção a): papel, tinta, marcador; tema claro e escuro; contraste AA; verde e vermelho só para certo e errado.
3. Infográficos em vetor (SVG) desenhados aqui, com as cores do sistema; onde faltar uma ilustração, o produtor aponta e o Fundador gera fora.
4. Ordem do edital, em levas de três itens: leva 1 = itens 1, 2 e 3 (tópicos P1-DA-1, 1.1, 1.2, 2.1, 2.2, 3.1, 3.2, 3.3, 3.4); leva 2 = 4, 5, 6; leva 3 = 7, 8, 9; leva 4 = 10, 11, 12.

## 1. O que é o Resumo visual e onde aparece
Hoje o botão "Resumo" do tópico abre `topicos[id].resumo` (prosa) pelo renderizador do curso. Na v17.3, quando `topicos[id].resumoVisual` existir, o botão abre a tela nova (`vResumoVisual`); sem ele, abre a tela atual. Nada muda no curso, nas questões, na nota ou no pacote dos outros módulos. `emUmMinuto`, `resumo` e `visuais` continuam existindo (o curso os usa).

## 2. Tradução da estética MapasPro → sistema v0.2
| Elemento MapasPro | Na plataforma (v17.3) | Por quê |
|---|---|---|
| Capa preta com título amarelo | Cabeçalho do tópico: número e nome em tinta; faixa de marcador de 4 px à esquerda; etiqueta de cobrança (seção 4) | Preto sólido não existe no sistema; a tinta (#1B2A41 / #ECEEF1 no escuro) faz o papel do preto |
| Barra de seção preta com ícone e título amarelo | `.rv-sec`: fundo tinta, texto papel, ícone SVG em marcador, letras espaçadas | Mesma hierarquia, mesma leitura, contraste 12:1 nos dois temas |
| Subtítulo com faixa amarela em degradê | `.rv-sub`: fundo marcador-suave, borda esquerda marcador, sem degradê | Degradê não passa no tema escuro; a faixa plana mantém o ritmo |
| Tabela com cabeçalho preto | `.rv table`: cabeçalho tinta sobre papel, linhas zebradas com `--soft`, empilhável no celular (já existe `.pilha`) | Reaproveita o componente de tabela do curso |
| Caixa azul "ATENÇÃO / ≠" | `.rv-box.atencao`: fundo `--soft`, borda esquerda 4 px tinta-2, rótulo em versalete | Azul é reservado ao foco; a caixa conserva a função de "pare aqui" |
| Caixa vermelha "REGRA GERAL: VEDAÇÃO" | `.rv-box.regra`: fundo marcador-suave, borda marcador, rótulo "Regra" | Vermelho é só para erro |
| Etiqueta "ALTÍSSIMA PROBABILIDADE" | `.rv-cob`: "Cebraspe 2025 · n itens neste tópico" com os números do corpus (seção 4) | Troca a opinião por medida; o rótulo de probabilidade não tem fonte |
| Emojis | Conjunto de 14 ícones SVG em linha (`ICONES`): alvo, pino, balança, prédio, pessoas, documento, relógio, cadeado, aviso, confere, x, raio, chave, livro | Emoji muda por sistema e não respeita o tema; SVG em `currentColor` sim |
| "Resumo Relâmpago" | `.rv-relampago`: lista de 6 a 10 frases de uma linha, numeradas, com raio em marcador | Igual ao original, no fim |
| "Possíveis Pegadinhas" (Errado/Correto) | `.rv-peg`: pares "Errado: … / Certo: …" com os sinais ✕ e ✓ em tinta (não em vermelho/verde: não é resposta da candidata) | Mantém o par, respeita a regra de cor |
| Infográficos ilustrados (pirâmide, mapa, cronograma, dois painéis) | Tipos SVG/HTML da seção 3: `piramide`, `mapa`, `dois`, `escala`, `linhaTempo`; `fluxo`, `compare`, `tabela`, `baseLegal`, `esquema`, `linha` já existem | Vetor, leve, tema-adaptável |
| Ilustrações figurativas (personagens, prédios desenhados) | Não entram. Onde uma ilustração faria falta, o produtor registra em `ilustracaoSugerida` (seção 6) | Decisão 3 do Fundador |

## 3. Formato do dado — `topicos["P1-DA-n"].resumoVisual`
```json
{"versao":"v3",
 "cobranca":{"itens":70,"ce":59,"fonte":"corpus Cebraspe 2025 (fila v2, enquadramento do pacote, a confirmar no CDN)"},
 "blocos":[
  {"t":"secao","titulo":"Conceito e requisitos","icone":"alvo"},
  {"t":"sub","titulo":"Conceito amplo × restrito","icone":"pino"},
  {"t":"texto","md":"Parágrafo curto, com **negrito** permitido."},
  {"t":"tabela","titulo":"...","colunas":["A","B","C"],"linhas":[["..","..",".."]],"legenda":"..."},
  {"t":"box","tipo":"atencao|regra|exemplo","rotulo":"Ato ≠ fato","md":"..."},
  {"t":"lei","norma":"Lei 9.784/1999","dispositivos":[{"ref":"art. 53","texto":"...","literal":true,"conferido":"2026-10-20"}]},
  {"t":"piramide","titulo":"...","niveis":[{"titulo":"Topo","texto":"..."},{"titulo":"Meio","texto":"..."},{"titulo":"Base","texto":"..."}],"legenda":"..."},
  {"t":"mapa","titulo":"...","centro":"Conceito de Direito Administrativo","ramos":[{"titulo":"...","texto":"..."}]},
  {"t":"dois","titulo":"...","a":{"titulo":"Vinculado","itens":["..."]},"b":{"titulo":"Discricionário","itens":["..."]},"pe":"Discricionariedade ≠ arbitrariedade"},
  {"t":"escala","titulo":"...","esquerda":"Mais público","direita":"Mais privado","pontos":[{"rotulo":"Autarquia","texto":"..."}]},
  {"t":"linhaTempo","titulo":"...","marcos":[{"quando":"Dia 0","titulo":"Nomeação","texto":"..."}]},
  {"t":"relampago","itens":["...","..."]},
  {"t":"pegadinhas","itens":[{"errado":"...","certo":"..."}]}
 ],
 "ilustracaoSugerida":[{"onde":"após o mapa do conceito","oQue":"...","porQue":"..."}],
 "fontes":["pacote v1.14 (resumo e baseLegal do tópico)","MapasPro — Atos Administrativos (seções 2, 6, 11), conferido"]}
```
Regras: `cobranca.itens` e `ce` vêm de banco/candidatos/resumo_por_item_edital_v2.csv e a `fonte` é obrigatória (regra EVIDÊNCIA: número sem fonte é vedado); `lei` reaproveita o `baseLegal` do pacote (os dispositivos já têm `conferido`); `piramide` 3 a 5 níveis; `mapa` 3 a 8 ramos, cada um com título de até 60 e texto de até 180 caracteres; `dois` 2 a 7 itens por lado (sete porque o art. 8º da Lei 8.112 tem sete formas de provimento e o art. 33, sete causas de vacância — emenda v3.1 após QA R1, D19); `escala` 3 a 6 pontos; `linhaTempo` 3 a 7 marcos; `relampago` 6 a 10 frases de até 140 caracteres; `pegadinhas` 4 a 10 pares. Todos os limites são bloqueio no checa_resumo_visual.py (v1.1), que também valida o `icone` contra a lista do template, exige `conferido` em data ISO e cruza cada dispositivo de `lei` com o `baseLegal` do pacote (`--pacote`), e barra os termos vedados pela triagem (COFIFOMOB, quádruplo, contrato de desempenho, OAB como autarquia, "Pegadinha provável", "cada vez mais cobrada"). Todo número ou prazo vem com norma e artigo no mesmo bloco ou num bloco `lei` do tópico.

## 4. Etiqueta de cobrança
Texto: "Cebraspe 2025: n questões deste item no corpus (c de Certo/Errado)". Ao toque, a nota: "Corpus de 1.321 questões de Direito Administrativo de 143 provas Cebraspe de 2025, enquadradas por item do edital pelo pacote de auditoria (a confirmar no CDN); medida de forma, não de conteúdo." Itens com até 3 questões no corpus (1, 2.2, 3.2 e 3.3): a etiqueta diz "poucas questões deste item no corpus" (com 0: "nenhuma questão enquadrada neste item no corpus") e o número exato fica só na nota ao toque (regra implementada na v17.3 após QA R1 D21 e R2 N9).

## 5. Regras de conteúdo (o que o script e o QA recusam)
1. Fonte primária de cada afirmação: lei (artigo e inciso), CF, súmula/tese com número, ou o resumo canônico do pacote. Afirmação dos resumos MapasPro sem lastro é descartada, não "adaptada".
2. Nenhum rótulo de probabilidade de cobrança; só a etiqueta da seção 4.
3. Nenhuma "questão comentada" dos PDFs entra: são AUTORAL sem rótulo; o treino vem do banco.
4. Acrônimos de memorização só quando corresponderem ao direito vigente (ex.: "COFIFOMOB" com nove elementos NÃO entra; os cinco requisitos da Lei 4.717/1965, art. 2º, sim).
5. Exemplos de entidades só quando verificáveis e atuais (Vale e Embraer não são sociedades de economia mista; Embrapa é empresa pública; OAB não é autarquia comum pelo STF — ADI 3.026 — então não serve de exemplo de autarquia).
6. Jurisprudência só com identificação (Súmula n., SV n., ADI n., Tema n.) e, quando o pacote tiver a conferência, com a data.
7. Cada bloco `lei` só com dispositivos já conferidos no pacote ou conferidos pelo QA normativo desta leva, com data.
8. O checa_pacote_v2.py ganha a seção "3c. resumoVisual": tipos válidos, limites da seção 3, `cobranca.fonte` obrigatória, nenhum termo de probabilidade ("ALTÍSSIMA", "ALTA PROBABILIDADE"), nenhum emoji, nenhuma referência a página de PDF, `lei` com `conferido`.

9. Nenhum recado de produção na experiência da candidata: hashes, pendências de QA, "conferir antes de citar", números de tarefa (T-120) ou referências ao "pacote" ficam em `fontes`, no relatório de produção ou no QA — nunca em legenda, box ou relâmpago (QA R1 D13, R2 N5; regra convergente com o guia do ChatGPT de 28/10).
10. O resumo do item pai (1, 2, 3…) organiza os filhos e trata só do que é próprio dele; não repete o conteúdo dos subitens (regra convergente com o guia do ChatGPT de 28/10).

11. Todo achado externo (ChatGPT, segunda leitura, triagem) traz um estado — confirmado em fonte primária (com data) / atualização posterior / síntese doutrinária / hipótese pendente — e só entra na plataforma nos dois primeiros estados ou, no terceiro, com o rótulo de doutrina; hipótese pendente não entra (CONCILIACAO_papeis_ChatGPT_Cowork_2026-10-28.md, §3).

## 6. Ilustrações sugeridas ao Fundador
Cada tópico lista em `ilustracaoSugerida` onde um desenho figurativo acrescentaria algo que o vetor não dá (ex.: a cena do controlador/operador/titular da LGPD). O produtor descreve a cena em uma frase e o motivo; o Fundador gera a imagem onde quiser; a inserção é um bloco `{"t":"imagem","src":"data:...","alt":"...","legenda":"..."}`, com limite de 150 KB por imagem e no máximo 2 por tópico, para a plataforma não passar de 4 MB.

## 7. Testes e QA (por leva)
- Script: checa_pacote_v2.py 3c zero bloqueios; build da prévia com o pacote vigente + os `resumoVisual` da leva; capturas 390×844 e 1280×900, claro e escuro, de cada tópico; contraste dos novos componentes ≥ 4,5:1 medido.
- QA normativo (qa-normativo-da, modelo distinto): cada bloco `lei`, cada número, cada súmula; fidelidade ao que o pacote já tinha.
- QA didático (gcb-cqfp-didatico): leitura em 60 segundos do Relâmpago responde às tarefas do tópico; nenhuma tabela com mais de 4 colunas; nenhuma classificação sem a pergunta que a distingue.
- QA de interface (QA-plataforma, Opus): tema escuro, celular, leitor de tela (ícones com `aria-hidden`, SVG com `role="img"` e `aria-label`), regressão R1–R9 e a da v17.2 sem diferença fora do previsto.
- Publicação: sim do Fundador por leva; a leva 1 pode sair junto com a v17.2.

## 8. Classificação
AGORA: v17.3 (renderizador + CSS + ícones + 5 tipos novos), checa 3c, leva 1. PRÓXIMO: levas 2–4. BACKLOG: bloco `imagem` com ilustrações do Fundador; versão impressa (PDF) do Resumo visual no estilo MapasPro. DESCARTADO: reproduzir a capa preta e os emojis; etiquetas de probabilidade.
