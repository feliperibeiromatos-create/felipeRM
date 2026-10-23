# Roteiro de entrada de pacote novo da Fábrica na Plataforma Câmara 2026

Versão 1 · 18/10/2026 · sessão de design da plataforma (DPE-01). Vale a partir da v15.2 publicada.

Plataforma da candidata: https://claude.ai/artifact/5fyXGpFMomSHwZuRnu36rC ("Plataforma Câmara 2026", v15.2, versão 1792363883-b584, capacidade de download declarada).
Laboratório (prévia): https://claude.ai/artifact/KyVNQZCzQzLbuuv4KXwibU.
Painel de acompanhamento: https://claude.ai/artifact/HZGbj3xcVD9cVjjkYTXdZ5.
Ferramentas: claude/kit_pacote/checa_pacote.py, embute_pacote.py, regressao_pacote.py (testadas em 18/10, ver seção 5).

## 0. Regras que não mudam
- Publicar na plataforma da candidata só com o "sim" do Felipe, para aquele pacote.
- Atualizar o painel é obrigatório a cada pacote novo, no mesmo turno em que ele chega, mesmo antes de publicar (skill atualizar-painel-camara). A linha final diz "painel reflete o pacote X; plataforma ainda no Y".
- A página não lê o pacote.json publicado ao lado: o pacote vai embutido na linha `const PUB_INLINE = …;` do index.html.
- Chaves c2026.v01.estado e c2026.v01.pacote não mudam de nome nem de formato.

## 1. Receber
Pedir à Fábrica (ou ao Felipe) dois arquivos: o pacote.json e o registro de alterações (JSON `{"alteracoes":[{"id":…,"campo":…}]}` ou o relatório em texto). Esta sessão não lê o repositório nem a pasta da Fábrica; o arquivo precisa vir anexado ao chat ou gravado no Projeto.

## 2. Conferir antes de tudo (somente leitura)
Ler a plataforma publicada com Artifact (action "read") e usar o arquivo salvo como base:
`python3 -I checa_pacote.py <index.html publicado> <pacote_novo.json> --registro <registro> --saida conferencia.md`

Bloqueia (não segue para a regressão), entre outros:
- id que sumiu, ou gabarito, itemEdital, enunciado ou rótulo que mudou sem estar no registro;
- id repetido, item sem enunciado ou gabarito C/E, itemEdital fora do edital (a plataforma recusaria o pacote);
- diagnóstico de 30 com id ausente (o diagnóstico some) ou com gabarito mudado;
- simulado citando id inexistente; rótulo CEBRASPE_ESTILO;
- `pacote.topicos` fora do formato (uma tabela com linha de tamanho errado ou um visual sem campo obrigatório quebra o curso inteiro do tópico na tela); gráfico de barras sem fonte.

Avisa: prefixo de id novo (precisa entrar no script do painel), lote novo, módulo que a plataforma ainda não exibe (ex.: Direito Administrativo precisa de mudança no código antes de aparecer), aumento de marcas de produção.

Informa: contagens antes e depois, voláteis, tópicos com 30+ e 40+ questões, campos de texto que mudaram.

## 3. Atualizar o painel (obrigatório, mesmo sem publicar)
Seguir a skill atualizar-painel-camara: gerar as 5 tabelas, subir como anexos, apontar `datasets/<id>` para os novos anexos com `if_version`, apagar os anexos antigos, revisar à mão `escopo`, `marcos` e `pendencias`. Não republicar a página do painel.

## 4. Regressão (cópia local, nada publicado)
`python3 -I embute_pacote.py <index.html publicado> <pacote_novo.json> teste.html --versao "v15.x · teste"`
`python3 regressao_pacote.py teste.html --saida regressao.md`

| Bloco | O que confere |
|---|---|
| R1 | abre sem erro; diagnósticos de 30 nas duas matérias |
| R2 | usuária antiga: tentativas, erros, rascunho e escolhas intactos; id ausente do pacote não quebra a aba Erros; só a chave de estado no armazenamento |
| R3 | todos os cursos abrem; "Em 1 minuto" e visuais do pacote.topicos aparecem; conta marcas de produção ainda visíveis |
| R4 | cada resumo de tópico aparece na aba Resumo e abre com o texto |
| R5 | bloco de questões de todos os tópicos: até 10, distintas, do próprio tópico |
| R6 | todos os simulados e diagnósticos abrem; entrega com nota −1 e caderno; Exportar meus erros gera JSON válido |
| R7 | carregar outro pacote.json e voltar ao publicado sem perder progresso |
| R8 | se algum tópico tiver 30+ questões: a nota aparece com 30 questões distintas |
| R9 | sem rolagem lateral em 10 telas, 360/390/1280 px, claro e escuro |

Depois, revisão visual curta (capturas a 360 px e no PC) dos tópicos que ganharam visuais, com a skill design-plataformas-interativas.

## 5. Mostrar e pedir o "sim"
Publicar o teste.html na prévia (laboratório), nunca na plataforma da candidata, e mandar ao Felipe: conferência, regressão, painel atualizado e o que muda para a candidata. Pedir o "sim, publicar <pacote>".

## 6. Publicar (só com o "sim")
- Ler de novo a plataforma publicada; partir do arquivo lido (se alguém publicou depois, a versão nova é a base).
- Guardar a versão em uso para reverter (id da versão no registro).
- Publicar com `url` da plataforma, sem passar `capabilities` (mantém o download), título "Plataforma Câmara 2026", meta `mapaspro:versao` atualizada.
- Ler de volta e comparar com o arquivo enviado; abrir e conferir a tela inicial.
- Registrar em claude/REGISTRO_*.md e no PLANO; ajustar a linha "plataforma no Y" do painel.

## 7. Situação conhecida em 18/10/2026
- No ar: pacote F4 v1.9 (334 itens); igual ao da prévia v15.2 (conferido nesta sessão) e, segundo o registro da publicação, igual byte a byte ao da v13.
- Pacote v1.10 da Fábrica (pelo painel, sem o arquivo nesta sessão): 560 itens, 226 novos (L1 112, L2 112, L6B 2). A tabela de itens do painel confirma: nenhum id do v1.9 sumiu, nenhum gabarito ou itemEdital mudou. Os tópicos 1.1 a 2.8 de Fala passam de 6 para 20; 3.1 a 3.4, 4.2 e 4.3 seguem com 6; 4.1 com 26. Nenhum tópico chega a 30, então a nota por tópico continua impossível com o v1.10. A T-104 estava em curso e o arquivo pode ser regerado (campo "nucleo" previsto e ausente).
- Prefixos L6A-/L6B-: o código v15 da plataforma não depende de prefixo (agrupa por itemEdital); o script do painel já trata L6A-R01 e L6B-R01/R02.
- pacote.topicos: a v15.2 lê `resumo` (aba Resumo, item por tópico no topo da matéria), `emUmMinuto` e `visuais` (no curso, antes do texto). O objeto do pacote substitui a demonstração do P2-1.4. Tópico sem curso (hoje só P1-5) não mostra emUmMinuto nem visuais.
- Ordens em curso na Fábrica (sessão s14): C, D, B, A, E e F (F = T-113). O ajuste "só projeção antes de produzir" da F ainda depende de o Felipe colar na s14.

## 8. Atualização de 19/10/2026 (v15.5, Direito Administrativo)
- A partir da v15.5 (hoje só na prévia), a plataforma mostra Direito Administrativo. Antes de publicar o primeiro pacote com DA, a plataforma da candidata precisa estar na v15.5 ou posterior; publicar pacote com DA sobre a v15.4 faria as questões de DA aparecerem dentro de TI.
- Use a prévia v15.5 como base do embute_pacote.py quando o pacote trouxer DA; o script desliga a demonstração (`DEMO_DA=false`) sozinho. Para manter a demonstração na prévia, passe `--demo`.
- A conferência agora também recusa: lote misturando DA e outra matéria, prefixos de DA misturados, Compare malformado, Base legal sem data de conferência e texto de demonstração no pacote. A regressão confere que cada tópico e cada questão ficaram na matéria certa.
- Formato do curso de DA: claude/ESPEC_curso_DA_formato_v1_2026-10-19.md.
