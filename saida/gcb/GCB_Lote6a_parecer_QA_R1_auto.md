PARECER DE QA — LOTE 6a v1 — RODADA 1 — QA automatizado (Opus) — 08/10/2026

REMETENTE: GCB-CQFP — Coordenação de QA, Fontes e Proveniência (TI e Dados), em execução automatizada independente (não produziu o lote)
DESTINATÁRIO: Coordenação de Produção (PRES-S) — cópia: GCB
Objeto: /home/claude/lotes/Lote6a_v1.md (LOTE 6a — TI-FERRAMENTAS — v1), conferido contra /home/claude/lotes/ESPEC_Lotes6.md.
Rodada: 1 de no máximo 2.

==================================================
0. MÉTODO E LIMITES DA CONFERÊNCIA
==================================================
- Lidos integralmente a especificação e o lote.
- Fontes: o acesso direto às páginas (curl, HTML bruto) foi bloqueado pelo proxy desta sessão (CONNECT 403) para todos os domínios. A conferência foi feita por WebFetch, em leitura independente da do produtor e com instrução expressa de transcrição literal, em 08/10/2026. As aspas abaixo são as que essa leitura devolveu como literais. O grau de confiança é alto, mas a leitura não é cópia do HTML bruto. Onde a ferramenta parafraseou em vez de citar, isso está dito.
- X1 e X2 (fontes que não abriram para o produtor) não foram reabertas, porque nenhum item ou trecho do curso se apoia nelas.
- Cruzamento com o Projeto: a remissão "Lote 4, item 6" (curso 3.1.4 e 3.2.3) foi conferida em GCB/Lote4_v3_canonica_GCB-CPP.md. O item 6 do Lote 4 é "Ética e responsabilidade digital no serviço público" e trata de ferramenta homologada e sigilo. A remissão está correta.

==================================================
1. CONFERÊNCIA FORMAL
==================================================
| Requisito (ESPEC) | Arquivo | Situação |
| Título do lote | "LOTE 6a — TI-FERRAMENTAS — v1 — produção automatizada (PRES-S) — 08/10/2026" | OK |
| Escopo literal do edital, dados da P1, TABELA DE CORREÇÕES (vazia), FONTES com URL e "verificado em 08/10/2026" | presentes | OK |
| Marcadores "FIM DA PARTE 1/3", "FIM DA PARTE 2/3", "FIM DA PARTE 3/3", "FIM DO LOTE 6a" | presentes (l. 282, 323, 373, 375) | OK |
| Curso item a item com definição, conceitos, exemplo legislativo (Derep, antigo DETAQ) e pegadinhas | presentes em 1.1 a 1.4 e 3.1 a 3.3 | OK |
| Resumo de uma página com NOTA 8.11.2 | presente | OK |
| Pares confundíveis (mínimo 12) | 19 (C1–C19) | OK |
| 15 itens AUTORAL | 15 (6A-01 a 6A-15) | OK |
| Distribuição: Word 3, Excel 3, PowerPoint 2, OneDrive 2; item 3 = 5 (webmail × cliente, Teams, Meet) | 01–03; 04–06; 07–08; 09–10; 11–15 (webmail × cliente = 6A-11; Teams = 6A-14; Meet = 6A-15) | OK |
| Entre 6 e 9 C | 7 C (02, 03, 05, 07, 09, 14, 15); 8 E (01, 04, 06, 08, 10, 11, 12, 13) | OK; declarado = contado |
| 7 ou 8 [TS] | 8 (01, 03, 04, 05, 06, 10, 12, 13): 2 C (03, 05) e 6 E | OK; declarado = contado |
| VOLÁTEIS ≤ 6, corretamente marcados | 5 (01, 09, 10, 14, 15) | OK. Os cinco dependem de nome de modo de exibição, de comportamento de serviço em nuvem ou de interface. Os demais julgam conceitos que a própria ESPEC lista como estáveis (referências, mesclar × dividir, mestre de slides, protocolos, Cco, webmail × cliente). A marcação de 6A-09 e 6A-10 como VOLÁTIL é conservadora (a ESPEC cita "controle de versão/histórico" e "compartilhamento com permissões" entre os conceitos estáveis) e é aceita. |
| Frase de comando "Acerca de ..., julgue os itens ..." por item do edital | presente (2 blocos) | OK |
| d-G: gabarito — [TS] — VOLÁTIL — subitem — mecanismo — justificativa com curso e fonte; linha "Contagem" | presente | OK |
| Nenhum item atribui afirmação a fornecedor | conferido nos 15 | OK |
| Nenhum item cobra preço, licença, plano, limite numérico, versão ou atalho | conferido nos 15 | OK |
| "Cada item julga UM ponto" | 6A-09 julga dois pontos independentes | VIOLAÇÃO → O-3 |
| Nenhuma afirmação no d-G além do curso | conferido | OK |
| Sem estratégia de marcação | conferido | OK |

==================================================
2. CONFERÊNCIA DE FONTES (verificado em 08/10/2026, WebFetch)
==================================================
| Fonte | Abriu? | O que o lote afirma × o que a página diz |
| F1 Word, alterações controladas | Sim (pt-BR) | Confere. Literal: "A escolha do modo de exibição Sem Marcação oculta as alterações apenas temporariamente." / "Eles ficarão visíveis novamente na próxima vez que alguém abrir o documento." / "Para revisar as alterações no documento sem aceitá-las ou rejeitá-las, selecione Avançar ou Anterior." / "Aceitar Todas as Alterações", "Rejeitar Todas as Alterações". Inspetor de Documentos: "Essa ferramenta verifica se há alterações controladas e comentários, texto oculto, nomes pessoais em propriedades [...]". Sustenta 6A-01. |
| F2 Word, mesclar/dividir | Sim (pt-BR) | Confere com ressalva. Literal: "Você pode combinar duas ou mais células da tabela na mesma linha ou coluna em uma única célula." Passos de dividir: "Selecione uma ou mais células para dividir." / "Insira o número de colunas ou linhas em que dividir a célula selecionada e selecione OK." Também consta: "Se você não vir a opção Mesclar Células, verifique se selecionou várias células adjacentes." A restrição "na mesma linha ou coluna", levada ao item como definição, gera risco (O-1). |
| F3 Word, sumário | Sim (pt-BR, com trechos em pt-PT) | Confere. Literal: "Os sumários no Word se baseiam nos títulos do documento." / "As entradas em falta acontecem com frequência porque os títulos não estão formatados como cabeçalhos." / "Aceda a Estilos de Base e, em seguida, selecione Título 1." / "[...] clicando com o botão direito no sumário e escolhendo Atualizar Campo." A palavra "cabeçalhos" é da página (tradução de "headings"), mas no Word em pt-BR "Cabeçalho" é o nome do recurso de cabeçalho de página (O-2). |
| F4 Excel, referências | Sim | Confere. Literal: "Por padrão, uma referência de célula é uma referência relativa". A tabela da página mostra A$1 → C$1 (linha fixa) e $A1 → $A3 (coluna fixa). Sustenta 6A-04 (E). |
| F5 Excel, SE | Sim | Confere. Sintaxe literal: "SE(teste_lógico, valor_se_verdadeiro, [valor_se_falso])"; valor_se_falso consta como opcional; "O primeiro resultado é se a comparação for Verdadeira, o segundo se a comparação for Falsa." Sustenta 6A-05 (C). |
| F6 Excel, PROCV | Sim | Confere. Literal: "Se você inserir VERDADEIRO ou deixar o argumento em branco, a função retornará uma correspondência aproximada"; "Se você inserir FALSO, a função retornará uma correspondência exata"; "[...] a função PROCV só pode pesquisar um valor da esquerda para a direita." Sustenta 6A-06 (E). |
| F7 PowerPoint, slide mestre | Sim (título literal "O que é um slide master no PowerPoint?") | Confere. Literal: "Quando você edita o slide mestre, todos os slides baseados nele conterão essas alterações." / "Quando você quiser que todos os seus slides contenham as mesmas fontes e imagens (como logotipos), [...]". Caminho: guia Exibir > Slide Mestre. Sustenta 6A-07 (C). |
| F8 PowerPoint, animação × transição | Sim | Confere. Literal: "Uma animação é aplicada a um único elemento"; "Uma transição é aplicada a um slide inteiro."; "Somente um efeito de transição pode ser aplicado a um slide." Sustenta 6A-08 (E). |
| F9 OneDrive, colaborar | Sim (pt-BR, título com formas de pt-PT) | Confere. Seção "Compartilhar arquivos ou pastas": "Selecione Permitir edição se quiser que outras pessoas possam editá-lo." / "Desmarque Permitir edição se quiser que outras pessoas possam apenas visualizar o arquivo.", no passo de configuração do link ("Todas as pessoas com este link podem editar este item"). Também: "Se você for o proprietário do arquivo ou tiver permissões de edição" (parar o compartilhamento/alterar permissões); "Selecione o X ao lado de um link para desabilitá-lo."; rótulos "Pode editar" e "Pode exibir". |
| F10 OneDrive, gerenciar compartilhamento | Sim | Confere. Literal: "Se você for o proprietário do arquivo, poderá parar de compartilhar o arquivo ou a pasta."; "você também poderá alterar as permissões de compartilhamento entre exibir e editar."; "Você não pode alterar a permissão de um link de compartilhamento de edição para exibição ou de exibição para edição."; "A alternativa é excluir o link de compartilhamento e criar um novo com uma permissão diferente." |
| F11 OneDrive, versões | Sim (URL pt-br, texto em pt-PT) | Confere. Literal: "O histórico de versões funciona com todos os tipos de ficheiros [...]"; "o administrador poderá ter desativado o controlo de versões do documento"; "A versão do documento selecionado torna-se a versão atual."; "A versão atual anterior torna-se a versão anterior na lista."; "só pode restaurar um ficheiro de cada vez". Descreve restauração pelo site e pelo Explorador de Arquivos com a aplicação de sincronização. Sustenta 6A-10 (E). |
| F12 Outlook, Cco | Sim | Confere. Literal: "esse destinatário recebe uma cópia do email sem que seu nome seja visível para os outros destinatários."; "Outras pessoas que recebem a mensagem não veem o endereço de quem está na linha Cco." Sustenta 6A-13 (E). |
| F13 Outlook, comparação | Sim (pt-BR, com formas de pt-PT) | Confere. Literal: "O Outlook é a nossa aplicação de e-mail e calendário com as funcionalidades mais completa, otimizada para PCs e portáteis."; "Acessível a partir da maioria dos browsers no portal do Microsoft 365."; "Disponível para compra como parte do Microsoft 365 ou Microsoft 365." A página não usa "instalado/instalar", como o lote já declara. |
| F14 Exchange Online, POP3 e IMAP4 | Sim (pt-BR) | Confere integralmente. Literal: "Por padrão, os clientes POP3 removem mensagens baixadas do servidor de email. Esse comportamento dificulta o acesso de email em vários computadores [...]"; "Os programas cliente POP3 baixam mensagens em uma única pasta no computador cliente [...]. O POP3 não consegue sincronizar várias pastas [...]"; "Por padrão, os clientes IMAP4 não removem mensagens baixadas do servidor de email. Esse comportamento facilita o acesso a mensagens de email de vários computadores."; "Programas de email que usam POP3 e IMAP4 dependem do protocolo SMTP para enviar mensagens." Sustenta 6A-12 (E). |
| F15 RFC 1939 | Sim | Confere. Literal (seção 1): POP3 "is intended to permit a workstation to dynamically access a maildrop on a server host in a useful fashion"; "normally, mail is downloaded and then deleted". |
| F16 RFC 9051 | Sim (primeiros 100.000 caracteres) | Confere com ressalva. Literal (Abstract): "allows a client to access and manipulate electronic mail messages on a server"; "permits manipulation of mailboxes (remote message folders)"; "IMAP4rev2 also provides the capability for an offline client to resynchronize with the server."; "IMAP4rev2 does not specify a means of posting mail;". A frase continua e remete o envio a um protocolo de submissão (RFC 6409), não ao "SMTP" nomeado (R-3). |
| F17 RFC 5321 | Sim (primeiros 100.000 caracteres) | Confere. Literal (1.1): "The objective of the Simple Mail Transfer Protocol (SMTP) is to transfer mail reliably and efficiently." |
| F18 Teams, equipes e canais | Sim (Learn; "Last updated on 2026-08-22") | Confere. Literal: "As equipes são coleções de pessoas, conteúdo e ferramentas que envolvem diferentes projetos e resultados dentro de uma organização."; "Os canais são seções dedicadas dentro de uma equipe [...]"; "Os canais podem ser abertos para todos os membros da equipe (canais padrão), membros da equipe selecionados (canais privados) ou pessoas selecionadas dentro e fora da equipe (canais compartilhados)." Tabela: só o canal compartilhado admite pessoas sem adicioná-las à equipe e participantes externos (Conexão Direta B2B). Sustenta 6A-14 (C). |
| F19 Teams, nova experiência | Sim | Confere. Literal: "A nova experiência de chat e canais simplifica as conversas ao colocar o chat, as equipas e os canais num único local." ("equipas" está na página). |
| F20 Meet, apresentar | Sim | Confere. Literal: "Você pode apresentar uma guia, uma janela específica ou a tela inteira em uma reunião."; opções "Uma guia", "Uma janela", "A tela inteira"; "Quando você apresenta uma guia do Chrome, o áudio é compartilhado por padrão."; "Compartilhar também o áudio do sistema"; "Parar apresentação"; "O compartilhamento da tela pode estar desativado devido a configurações do administrador ou controles do organizador da reunião." Sustenta 6A-15 (C). |
| F21 Meet, participar | Sim | Confere. "Participar agora"; código ou apelido; "Entrar com o Google Meet"; trecho "o organizador ou um participante precisa autorizar seu acesso"; "Pedir para participar". |
| F22 Meet, iniciar/agendar | Sim (página em pt-PT: "Calendário Google", "Guardar") | Confere em parte. A página manda clicar em "Adicionar videoconferência do Google Meet" ao criar o evento. O curso diz que "o link nasce com o evento", e a pegadinha 3.3.5 P3 marca CERTO uma generalização (R-5). |

Resultado: todas as 22 fontes usadas abriram. Nenhuma URL ou citação inventada foi encontrada. As aspas do lote conferem com a leitura desta rodada, salvo as observações de F2, F3, F16 e F22, que geram O-1, O-2, R-3 e R-5.

==================================================
3. CONFERÊNCIA ITEM A ITEM
==================================================
6A-01 (E, [TS], VOLÁTIL). Gabarito inequívoco. F1 diz literalmente que "Sem Marcação" oculta só temporariamente e que as alterações reaparecem. Não há leitura razoável que leve a C. [TS] procede ("sem marcação" = "sem alterações"). Sem repetição. OK.
6A-02 (C). O gabarito tem apoio literal na F2, mas o item transforma em DEFINIÇÃO ("mesclar células significa...") uma descrição da página que restringe a mesclagem a células "de uma mesma linha ou coluna". Lida como exaustiva, a restrição permite marcar E a quem sabe que a seleção de mesclagem não precisa ficar numa só linha ou coluna. A própria F2 só exige células adjacentes ("verifique se selecionou várias células adjacentes"). O risco de recurso é real e eliminá-lo não custa nada. → O-1.
6A-03 (C, [TS]). O conteúdo está correto (F3), mas o item usa "formatado como cabeçalho". No Word em pt-BR, "Cabeçalho" é o recurso de cabeçalho de página (guia Inserir > Cabeçalho), e o estilo que alimenta o sumário chama-se "Título 1, Título 2...". A candidata que ler "cabeçalho" como cabeçalho de página tende a julgar que a frase associa o sumário a um recurso sem relação com ele e a marcar E. A palavra está na F3, mas o item não deve depender de uma tradução que colide com o nome de outro recurso do mesmo programa. → O-2. O [TS] se mantém.
6A-04 (E, [TS]). Inequívoco. A tabela da F4 (A$1 → C$1) mostra que a linha fica fixa. OK.
6A-05 (C, [TS]). Inequívoco (F5: sintaxe e argumento opcional). O [TS] numa C, como "falsa pegadinha", segue a convenção dos lotes anteriores. OK.
6A-06 (E, [TS]). Inequívoco (F6: em branco = aproximada). "Somente a correspondência exata" é falso mesmo que a aproximada também devolva o valor exato quando ele existe. OK.
6A-07 (C). Reproduz a F7. Risco residual baixo: um layout pode ocultar os gráficos de fundo, mas o item segue a regra geral literal da fonte. Aceito sem alteração. OK.
6A-08 (E). Inversão evidente (F8). Sem [TS], coerente. OK.
6A-09 (C, VOLÁTIL). Os dois enunciados são verdadeiros (F10: o proprietário pode parar de compartilhar; F9: "Permitir edição" ou só visualizar na configuração do link). Porém o item julga DOIS pontos independentes ligados por "e", contra a regra "Cada item julga UM ponto" da ESPEC. O ponto mais cobrável (permissão exibir × editar) basta, e a redação nova continua fora da divergência F9 × F10 sobre alterar a permissão de link já criado. → O-3.
6A-10 (E, [TS], VOLÁTIL). Inequívoco. F11 literal: "A versão atual anterior torna-se a versão anterior na lista." Sobre a ressalva do administrador (ponto c do produtor), ver seção 5. OK.
6A-11 (E). Inversão evidente. Teste de recurso: alguém pode alegar que o navegador também é um aplicativo instalado. Mesmo assim, a segunda oração ("o cliente de e-mail é acessado por meio de navegador, dispensando a instalação de programa") permanece falsa, e o gabarito E se mantém em qualquer leitura. OK.
6A-12 (E, [TS]). Inequívoco. A F14 diz literalmente o padrão de cada protocolo, e a RFC 1939 corrobora o POP3. OK.
6A-13 (E, [TS]). Inequívoco (F12, literal). OK.
6A-14 (C, VOLÁTIL). Reproduz a F18 literalmente. A tabela da página, atualizada em 22/08/2026, confirma que o canal privado não admite quem não está na equipe. Políticas de administrador podem impedir a criação de certos canais, mas o item descreve o alcance de cada tipo, não a disponibilidade. OK.
6A-15 (C, VOLÁTIL). Reproduz a F20 literalmente ("em um computador" delimita a plataforma). Risco residual baixo: o suporte do navegador à opção "guia" pode variar, mas "pode optar" acompanha a fonte. Aceito. OK.
Repetição: nenhum item repete o ponto de outro. 6A-11, 6A-12 e 6A-13 julgam pontos distintos de 3.1, e 6A-12 não se sobrepõe à pegadinha P7 (pastas), que não virou item.

==================================================
4. CURSO, RESUMO E PARES
==================================================
- Nenhum erro conceitual nas pegadinhas e nos pares que afete gabarito.
- 1.1.1: diz "Dois recursos" e enumera três, (i) a (iii). Ver R-1.
- 1.1.6 P6: o motivo "não se afirma atualização automática em tempo real" justifica um ERRADO pelo silêncio da fonte. O motivo positivo está na F3: o sumário é um campo, atualizado por "Atualizar Campo" após mudanças. Ver R-2.
- 3.1.2: "o envio fica com outro protocolo (SMTP)" atribui à RFC 9051 algo que ela não diz nesses termos. A RFC remete a um protocolo de submissão de mensagens (RFC 6409). Ver R-3.
- 3.1.4: o exemplo afirma que o cliente instalado "sincroniza as pastas pelo IMAP", o que soa como fato sobre o ambiente da Casa. O protocolo efetivamente configurado na Câmara não tem fonte. Ver R-4.
- 3.3.2 e 3.3.5 P3: "o link nasce com o evento" e a pegadinha CERTO "O link da reunião do Meet é criado no Google Agenda junto com o evento" generalizam. A F22 mostra que o link também nasce em "Nova reunião", no próprio Meet, e que no Agenda ele é acrescentado pelo clique em "Adicionar videoconferência do Google Meet". Uma pegadinha CERTO com generalização ensina o padrão errado. Ver R-5.
- 1.1.3, 1.1.4 e resumo 1.1 precisam acompanhar O-1 e O-2 (redações na seção 6).
- Resumo: tem a NOTA 8.11.2 e a linha de validade (reverificar de 4 a 8/1/2027). OK.
- Pares: 19, no formato pedido. Nenhum par inverte conceito. OK.

==================================================
5. PONTOS LEVANTADOS PELO PRODUTOR
==================================================
(a) Aspas obtidas por resumo. Conferidas de novo nesta rodada, em leitura independente com instrução de transcrição literal (ver seção 2). Todas as aspas usadas no curso e no d-G conferem. Divergências só de forma, sem efeito: F13 "Disponível para compra como parte do Microsoft 365 ou Microsoft 365." (o lote cita a primeira parte); F20 "desativado devido a configurações do administrador ou controles do organizador" (o curso diz "limitado", que é paráfrase e não aspas). Limite declarado na seção 0: não houve cópia do HTML bruto. Registrar na TABELA DE CORREÇÕES (R-6).
(b) F9 × F10 sobre alterar a permissão de link (6A-09). As páginas não se contradizem no mérito. A F9 trata de alterar a permissão de pessoas com acesso ("Pode editar"/"Pode exibir") e de desabilitar link (X). A F10 diz literalmente que não se altera a permissão de um LINK, que deve ser excluído e recriado. A divergência real é outra: quem pode parar o compartilhamento (F9: proprietário OU quem tem permissão de edição; F10: proprietário). O curso 1.4.2 já registra as duas. A decisão de não cobrar a alteração de link existente está correta e se mantém na redação de O-3.
(c) 6A-10 sem a ressalva do administrador. Sem alteração. O item pressupõe que uma restauração ocorre; se o administrador desativou o controle de versões, não há versão anterior a restaurar e a premissa não se realiza. Acrescentar "quando habilitado" não muda o gabarito e só alonga o enunciado. A ressalva fica no curso 1.4.3, onde já está.
(d) 6A-12 apoiado na F14 e na RFC 1939. Apoio suficiente e literal (ver seção 2). Sem alteração.
(e) "Cliente de e-mail = aplicativo instalado" como conceito geral. Aceito como conceito geral marcado, que é o uso consolidado em provas de informática básica. O gabarito de 6A-11 não depende da palavra "instalado" (ver seção 3). Sem alteração obrigatória. Sugestão de redação mais precisa no curso 3.1.1, incluída em R-4.

==================================================
6. ACHADOS E REDAÇÕES SUBSTITUTIVAS
==================================================

O-1 — 6A-02: restrição "de uma mesma linha ou coluna" lida como definição exaustiva (risco de recurso contra o C).
Item (substituir integralmente):
"6A-02. Em uma tabela do Word, mesclar células significa combinar duas ou mais células adjacentes em uma única célula, ao passo que dividir células significa subdividir uma célula em mais linhas ou colunas."
d-G (substituir):
"6A-02. C — 1.1 — sem armadilha (ancoragem). Curso 1.1.3: mesclar combina duas ou mais células adjacentes selecionadas em uma única; dividir subdivide a célula em linhas ou colunas, em número informado pelo usuário. Fonte: F2, verificado em 08/10/2026."
Curso 1.1.3 (substituir a primeira frase):
"Conforme a F2 (leitura de 08/10/2026): mesclar combina duas ou mais células da tabela em uma única célula; a página descreve a combinação de células "na mesma linha ou coluna" e orienta, se o comando não aparecer, verificar se foram selecionadas "várias células adjacentes"; há comando para desfazer a mesclagem. O item 6A-02 usa o requisito de adjacência e não reproduz a expressão "na mesma linha ou coluna", para que ela não seja lida como definição exaustiva."
Resumo, 1.1 (substituir o trecho):
"MESCLAR = duas ou mais células adjacentes viram uma; DIVIDIR = uma célula vira várias linhas/colunas (F2)."
Contagens: inalteradas (C, sem [TS], não VOLÁTIL).

O-2 — 6A-03: "formatado como cabeçalho" colide com o recurso "Cabeçalho" (de página) do Word.
Item (substituir integralmente):
"6A-03. No Word, o sumário automático baseia-se nos títulos do documento; por isso, um título ao qual não tenha sido aplicado um estilo de título, como o Título 1, pode deixar de constar do sumário."
d-G (substituir):
"6A-03. C — [TS] — 1.1 — GI invertida (tentação: ler "pode deixar de constar" como erro e marcar E, ou supor que o Word identifica títulos pelo aspecto do texto). Curso 1.1.4: o sumário se baseia nos títulos do documento; quando faltam entradas, a causa costuma ser títulos sem estilo de título, e a solução indicada é aplicar o Título 1. O item diz "pode deixar de constar", não "sempre deixa". Fonte: F3, verificado em 08/10/2026."
Curso 1.1.4 (substituir a segunda frase):
"Quando faltam entradas, a causa costuma ser que os títulos não receberam estilo de título (a F3 diz "não estão formatados como cabeçalhos", no sentido de títulos de seção, e não do recurso Cabeçalho, que é o cabeçalho de página); a solução indicada é aplicar o estilo Título 1 ao texto de cada título que deve constar."
Pegadinha 1.1.6 P5 (substituir o motivo): "→ ERRADO (baseia-se nos títulos com estilo de título; F3)."
Resumo, 1.1 (substituir o trecho): "Sumário automático: baseia-se nos títulos com estilo de título (Título 1, Título 2...); título sem esse estilo pode faltar; atualizar o campo após mudanças (F3)."
Contagens: inalteradas (C, [TS], não VOLÁTIL).

O-3 — 6A-09: o item julga dois pontos (interromper compartilhamento + permissão do link), contra a ESPEC ("Cada item julga UM ponto").
Item (substituir integralmente):
"6A-09. No OneDrive, ao compartilhar um arquivo por link, o usuário pode definir se as pessoas que receberem o link poderão apenas visualizar o arquivo ou também editá-lo."
d-G (substituir):
"6A-09. C — VOLÁTIL — 1.4 — sem armadilha (ancoragem). Curso 1.4.2: ao compartilhar, na configuração do link, marca-se "Permitir edição" para que outros possam editar ou desmarca-se para que possam apenas visualizar (F9). O item não julga a alteração de permissão de um link já criado (a F10 informa que ela não é possível; exclui-se o link e cria-se outro; ver curso 1.4.2). Fonte: F9, verificado em 08/10/2026."
Curso 1.4.2, primeiro marcador (substituir):
"- Seleciona-se o item e escolhe-se Compartilhar (Partilhar); na configuração do link ("Todas as pessoas com este link podem editar este item"), marca-se "Permitir edição" para que outras pessoas possam editar ou desmarca-se para que possam apenas visualizar (F9). A F9 também usa os rótulos "Pode editar" e "Pode exibir"."
Contagens: inalteradas (C, sem [TS], VOLÁTIL). O ponto "o proprietário pode interromper o compartilhamento" continua no curso (F10) e na pegadinha 1.4.5 P5, sem item.

R-1 — Curso 1.1.1: "Dois recursos de revisão e estruturação merecem atenção especial" → "Três recursos de revisão e estruturação merecem atenção especial".

R-2 — Curso 1.1.6 P6 (substituir o motivo): "→ ERRADO (o sumário é um campo: após mudanças que o afetem, atualiza-se com o botão direito > "Atualizar Campo"; F3)."

R-3 — Curso 3.1.2, marcador do IMAP4 (substituir a última frase):
"A RFC 9051 diz que o IMAP4rev2 "does not specify a means of posting mail" e remete o envio a um protocolo de submissão de mensagens (RFC 6409); na prática do cliente de e-mail, o envio fica com o SMTP (F14: os programas POP3 e IMAP4 "dependem do protocolo SMTP para enviar mensagens")."

R-4 — Curso 3.1.4 (substituir a frase do computador de trabalho):
"[...] no computador de trabalho, usa um cliente de e-mail instalado, que, quando configurado com IMAP4, mantém as mensagens no servidor e sincroniza as pastas (F14) e envia por SMTP (F14)."
Opcional no curso 3.1.1 (cliente): "CLIENTE DE E-MAIL: programa de correio próprio, em regra instalado no computador ou no celular, que acessa a caixa postal no servidor (por exemplo, por POP3 ou IMAP4) e envia por SMTP (conceito geral; F14 para os protocolos)."

R-5 — Meet, curso 3.3.2 e pegadinha 3.3.5 P3.
3.3.2, marcador "Agendar" (substituir):
"- Agendar: ao criar um evento no Google Agenda (a F22, em pt-PT, chama-o "Calendário Google"), clica-se em "Adicionar videoconferência do Google Meet" para associar um link de videoconferência ao evento, que é compartilhado com os convidados (F22)."
3.3.5 P3 (substituir):
"P3. "O link de uma reunião do Meet só pode ser criado por meio de um evento do Google Agenda" → ERRADO (também se cria em "Nova reunião", no próprio Meet; F22)."
Par C18/C19 e resumo 3.3: sem mudança obrigatória. No resumo, "(link nasce com o evento)" → "(link associado ao evento)".

R-6 — TABELA DE CORREÇÕES da v2: registrar O-1 a O-3 e R-1 a R-5 e acrescentar à "Ressalva de método" (l. 13): "Aspas conferidas pela GCB-CQFP na Rodada 1 de QA, em 08/10/2026, por leitura independente com instrução de transcrição literal; conferem, salvo as observações do parecer R1 (F2, F3, F16, F22), já incorporadas."

Riscos residuais aceitos, sem alteração: 6A-07 (layout que oculta gráficos de fundo); 6A-11 (o navegador também é programa instalado, mas o gabarito E se sustenta pela segunda oração); 6A-14 (políticas de administrador); 6A-15 (suporte do navegador à opção "guia").

==================================================
7. CONTAGENS APÓS AS CORREÇÕES
==================================================
Nenhuma correção altera gabarito, [TS], VOLÁTIL ou distribuição:
15 itens; 7 C (02, 03, 05, 07, 09, 14, 15) e 8 E (01, 04, 06, 08, 10, 11, 12, 13); 8 [TS] (01, 03, 04, 05, 06, 10, 12, 13: 2 C e 6 E); 5 VOLÁTEIS (01, 09, 10, 14, 15); Word 3, Excel 3, PowerPoint 2, OneDrive 2, item 3 = 5 (3.1 = 3, 3.2 = 1, 3.3 = 1).

==================================================
8. CONCLUSÃO
==================================================
APROVADO COM RESSALVAS.
Aplicar obrigatoriamente, com as redações da seção 6: O-1 (6A-02), O-2 (6A-03) e O-3 (6A-09), com os ajustes correspondentes no curso, no resumo e no d-G.
Aplicar, salvo recusa motivada em uma linha: R-1 a R-6.
A v2 com as correções aplicadas literalmente não precisa de Rodada 2, desde que a TABELA DE CORREÇÕES registre cada uma e as contagens permaneçam as da seção 7. Qualquer redação diferente da proposta para O-1 a O-3 volta para a Rodada 2.
Classificação: AGORA — aplicar O-1 a O-3 e R-1 a R-6 na v2.

FIM DO PARECER

==================================================
CONFERÊNCIA DE APLICAÇÃO — LOTE 6a v2 — 08/10/2026 (não conta como Rodada 2)
==================================================
Objeto: /home/claude/lotes/Lote6a_v2.md, comparado linha a linha (diff) com /home/claude/lotes/Lote6a_v1.md e com as redações da seção 6 deste parecer.

| Ponto | Onde (v2) | Resultado |
| O-1 | 6A-02; d-G 6A-02; curso 1.1.3 (primeira frase); resumo 1.1 | CONFERE. Texto idêntico ao do parecer nos quatro lugares. O restante de 1.1.3 foi preservado. |
| O-2 | 6A-03; d-G 6A-03; curso 1.1.4 (segunda frase); pegadinha 1.1.6 P5; resumo 1.1 | CONFERE. Texto idêntico ao do parecer nos cinco lugares. |
| O-3 | 6A-09; d-G 6A-09; curso 1.4.2 (primeiro marcador) | CONFERE. Texto idêntico ao do parecer. O ponto "interromper o compartilhamento" continua no curso (1.4.2, segundo e terceiro marcadores; resumo 1.4) e sai do item. |
| R-1 | curso 1.1.1 | CONFERE. |
| R-2 | curso 1.1.6 P6 | CONFERE. |
| R-3 | curso 3.1.2 (IMAP4) | CONFERE. |
| R-4 | curso 3.1.4; curso 3.1.1 (cliente, opcional) | CONFERE. Em 3.1.4 o texto é idêntico. Em 3.1.1 a redação opcional foi inserida mantendo o exemplo da F13 e a frase final ("A definição de 'cliente = aplicativo instalado' é conceito geral [...]"). O resultado tem uma leve redundância, sem contradição nem efeito em item. Aceito. |
| R-5 | curso 3.3.2 (Agendar); pegadinha 3.3.5 P3; resumo 3.3 | CONFERE. Texto idêntico ao do parecer nos três lugares. |
| R-6 | cabeçalho (Ressalva de método); TABELA DE CORREÇÕES | CONFERE. A frase foi acrescentada à Ressalva de método. |
| Tabela de Correções | l. 18–26 | CONFERE. Há uma linha para cada correção, de O-1 a O-3 e de R-1 a R-6, com parte/item, correção, origem "QA R1 (Opus)" e status "aplicada (v2)". As descrições correspondem ao que foi alterado. |
| Contagens | linha "Contagem" do d-G (não alterada) | CONFERE. Recontado na v2: 15 itens; 7 C (02, 03, 05, 07, 09, 14, 15) e 8 E (01, 04, 06, 08, 10, 11, 12, 13); 8 [TS] (2 C e 6 E); 5 VOLÁTEIS (01, 09, 10, 14, 15); Word 3, Excel 3, PowerPoint 2, OneDrive 2, item 3 = 5. Igual à seção 7. |
| Marcadores | FIM DA PARTE 1/3, 2/3 e 3/3; FIM DO LOTE 6a | CONFERE. Os quatro estão presentes. |
| Nada alterado fora do parecer | diff v1 × v2 | CONFERE. Todas as diferenças correspondem a O-1 a O-3 e R-1 a R-6, exceto a nova linha 2 ("v2 — correções da QA rodada 1, 08/10/2026"), que é marca de versão e é aceita. Itens, gabaritos e d-G não tocados pelo parecer estão idênticos à v1. |

Observação de forma (não bloqueante; decisão da Coordenação): a linha 1 da v2 ainda diz "LOTE 6a — TI-FERRAMENTAS — v1 — produção automatizada (PRES-S) — 08/10/2026", e só a linha 2 indica a v2. Para que o título não divirja do arquivo, redação sugerida para a linha 1: "LOTE 6a — TI-FERRAMENTAS — v2 — produção automatizada (PRES-S) — 08/10/2026" (a linha 2 pode ser mantida).

R-7 — frase remanescente análoga a R-5 (curso 3.3.4). Exige ajuste, pelo mesmo motivo de R-5. A F22 mostra que o link é associado ao evento pelo clique em "Adicionar videoconferência do Google Meet"; o evento não "gera" o link por si.
Trecho atual (v2, l. 283): "o organizador cria o evento no Agenda, que gera o link (F22);"
Redação substitutiva exata: "o organizador cria o evento no Agenda e associa a ele um link de videoconferência, clicando em "Adicionar videoconferência do Google Meet" (F22);"
O restante da frase não muda. Sem efeito em item ou contagens. Se aplicada, registrar como R-7 na TABELA DE CORREÇÕES.

RESULTADO: CONFERIDO. As correções O-1 a O-3 e R-1 a R-6 estão aplicadas com a redação do parecer, e a Tabela de Correções, as contagens e os marcadores conferem. Ficam à decisão da Coordenação, sem bloquear a reconciliação: R-7 (3.3.4) e o ajuste do título da linha 1.

FIM DA CONFERÊNCIA DE APLICAÇÃO
