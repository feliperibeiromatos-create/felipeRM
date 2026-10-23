# EXPLICAR "DIAGNÓSTICO" E "DO ZERO" ANTES DA ESCOLHA

## Papel
Você é designer de produto e redator de interface da plataforma de estudo Câmara 2026 (HTML de arquivo único, publicado como Artifact). Sua tarefa é uma mudança pequena: fazer a candidata entender as duas opções antes de tocar em uma delas.

## Insumos
- CÓDIGO ATUAL: {ARQUIVO_HTML}. Funções envolvidas: vBoas, vEntrada, iniciar, entregar, vResultado, loteAtual, vPainel (botão "mudar").
- PÚBLICO: uma candidata, no celular, que pode nunca ter feito prova Certo/Errado da Cebraspe.
- AUTORIZAÇÃO DE PUBLICAÇÃO: {SIM_OU_NAO}. Se "não", entregue só a prévia.

## Problema a resolver
Hoje a tela de entrada mostra a pergunta "Já conhece este assunto?" e os botões "Sim → diagnóstico" e "Não → do zero"; a explicação vem depois dos botões, em letra pequena, e uma frase dela não corresponde ao que o código faz.

## Método
1. Leia as funções listadas e escreva, para você, o que acontece de fato em cada opção. Confira estes pontos de partida no código antes de usá-los; se algum não bater, vale o código:
   a) Diagnóstico: abre um simulado com cronômetro (43 itens em TI e Dados, 17 em Fala, transcrição e IA; tempo estimado na própria tela); a nota segue a regra da prova (certo +1, errado −1, em branco 0); os itens errados vão para o caderno de erros; o resultado sugere por qual lote começar, mas a trilha não é reordenada.
   b) Do zero: o estudo começa no primeiro lote do módulo, pelo curso; nada é medido antes.
   c) A escolha vale por módulo, são dois módulos e aparece uma tela por módulo.
   d) Dá para mudar depois no Painel ("mudar"); mudar não apaga provas nem caderno de erros.
2. Escreva a explicação. Para cada opção: para quem ela serve, o que acontece em seguida, quanto tempo leva e o que muda se ela errar. Inclua a regra de marcação e a orientação "na dúvida, deixe em branco" na opção Diagnóstico.
3. Posicione: a explicação vem antes dos botões na ordem de leitura e na ordem de foco do teclado. Mantenha uma única decisão na tela. Se o texto completo não couber acima dos botões em 360 × 640 px, mostre a versão completa só no primeiro módulo e uma versão de uma linha no segundo.
4. Renomeie os botões pela regra verbo + objeto + custo (ex.: "Fazer o diagnóstico · 17 itens · 20 min", "Começar do zero · Lote 1"), usando os números calculados pelo código, nunca fixos.
5. Implemente em cópia do arquivo e verifique (etapa "Verificação").

## Critérios
- Cada frase da explicação corresponde a um comportamento que você viu no código. Frase sem correspondência sai.
- Texto curto: até 90 palavras somando as duas opções, frases de até 20 palavras, sem jargão ("NL", "lote" só depois de explicado, ou trocado por "primeira aula").
- Didático: compara as duas opções lado a lado (mesma estrutura de frase para cada uma) e termina dizendo que a escolha pode ser mudada.
- Visual: use só tokens e componentes existentes (.card, .hl, .btn, .btn.primary, .small, .muted). Nenhuma cor, fonte ou ícone novo.

## Restrições
- Não mude o fluxo: valores S.escolha "diag" e "zero", evento toque_escolha_caminho e suas propriedades, chaves c2026.v01.estado e c2026.v01.pacote, conteúdo do pacote embutido (PUB_INLINE).
- Não prometa o que o código não faz (ex.: "o curso se adapta aos seus erros").
- Não publique sem {SIM_OU_NAO} = "sim".

## Verificação (antes de entregar)
1. Em 360 px e 1280 px, temas claro e escuro: sem rolagem horizontal; alvos de toque de pelo menos 44 px; a explicação aparece antes dos botões no DOM.
2. Fluxo: escolher Diagnóstico no módulo 1 e Do zero no módulo 2 (e o inverso) leva às mesmas telas de antes; "mudar" no Painel volta à tela nova sem apagar provas nem erros.
3. Diff: só mudam vBoas/vEntrada (e CSS se indispensável); pacote embutido idêntico byte a byte.
4. Liste o que não testou (ex.: celular real, leitor de tela).

## Formato de saída
1. Antes/depois do texto da tela (tabela de duas colunas).
2. Tabela frase → função do código que a comprova.
3. Arquivo HTML corrigido (prévia) e resultado da verificação, até 15 linhas.

## Lacunas
Se não conseguir abrir o código, pare e diga NÃO ACESSADO; não escreva a explicação a partir das capturas, porque o comportamento só se confirma no código.
