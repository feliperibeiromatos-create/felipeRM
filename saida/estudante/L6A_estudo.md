# Lote 6a — MSOffice 365; Ferramentas de comunicação e colaboração (P1 itens 1 e 3)

Prova: P1

## Itens do edital

- P1-1 — MSOffice 365 (Word, Excel, PowerPoint e OneDrive)
- P1-3 — Ferramentas de comunicação e colaboração: correio eletrônico (webmail, cliente de e-mail), aplicativos de comunicação (Microsoft Teams, Google Meet)

## Resumo

```text
NOTA DO EDITAL (8.11.2): na prova objetiva, cada item vale +1,00 ponto se a marcação concordar com o gabarito oficial definitivo, −1,00 ponto se discordar e 0,00 se não houver marcação ou houver marcação dupla (C e E) (Edital nº 1/2026, subitem 8.11.2).

1.1 WORD. Controle de alterações: "Aceitar" incorpora; "Rejeitar" descarta; "Avançar/Anterior" só navegam; o modo "Sem Marcação" apenas OCULTA (as marcas voltam ao reabrir); para remover é preciso aceitar ou rejeitar; Inspetor de Documentos verifica alterações, comentários e informações ocultas (Microsoft, documentação de suporte, "Aceitar ou rejeitar alterações controladas no Word"). Tabelas: MESCLAR = duas ou mais células adjacentes viram uma; DIVIDIR = uma célula vira várias linhas/colunas (Microsoft, documentação de suporte, "Mesclar ou dividir células em uma tabela"). Sumário automático: baseia-se nos títulos com estilo de título (Título 1, Título 2...); título sem esse estilo pode faltar; atualizar o campo após mudanças (Microsoft, documentação de suporte, "Inserir um sumário").
1.2 EXCEL. Referência RELATIVA (padrão) muda ao copiar; ABSOLUTA ($B$2) fixa coluna e linha; MISTA fixa só uma ($B2 fixa a coluna; B$2 fixa a linha): o $ trava o que vem logo depois (Microsoft, documentação de suporte, "Alternar entre referências relativas, absolutas e mistas"). SE(teste_lógico; valor_se_verdadeiro; [valor_se_falso]): o 2º argumento é para verdadeiro, o 3º, opcional, para falso (Microsoft, documentação de suporte, "SE (Função SE)"). PROCV: 4º argumento FALSO = correspondência exata; VERDADEIRO ou em branco = aproximada; pesquisa só da esquerda para a direita (Microsoft, documentação de suporte, "Pesquisar valores com PROCV, ÍNDICE ou CORRESP").
1.3 POWERPOINT. Slide mestre concentra fontes e imagens (logotipo); editar o mestre altera os slides baseados nele (Microsoft, documentação de suporte, "O que é um slide master no PowerPoint?"). ANIMAÇÃO = efeito num elemento do slide (vários por slide); TRANSIÇÃO = efeito no slide inteiro, na passagem de um slide a outro (um por slide) (Microsoft, documentação de suporte, "A diferença entre animações e transições").
1.4 ONEDRIVE. Compartilhar: permissão de exibir ou de editar; o proprietário pode interromper o compartilhamento; X ao lado do link o desabilita (Microsoft, documentação de suporte, "Colaborar no Microsoft OneDrive: partilhar, editar e gerir Files"; Microsoft, documentação de suporte, "Gerenciar compartilhamento e permissões no OneDrive e no SharePoint"). Histórico de versões: ver e restaurar versões anteriores; a versão restaurada vira a atual, e a atual anterior passa a constar como versão anterior (Microsoft, documentação de suporte, "Restaurar uma versão anterior de um ficheiro armazenado no OneDrive"). Prazos de retenção e planos: ficam fora do estudo.
3.1 CORREIO ELETRÔNICO. WEBMAIL = navegador, sem programa instalado (ex.: Outlook na Web, Microsoft, documentação de suporte, "Comparar o Outlook para PC, Outlook na web e o Outlook para iOS & Android"); CLIENTE = aplicativo instalado (ex.: Outlook para PC; definição geral). SMTP ENVIA (IETF, RFC 5321, "Simple Mail Transfer Protocol"; Microsoft Learn, "POP3 e IMAP4 em Exchange Online"); POP3 baixa e, por padrão, remove do servidor, uma única pasta (IETF, RFC 1939, "Post Office Protocol - Version 3"; Microsoft Learn, "POP3 e IMAP4 em Exchange Online"); IMAP4 acessa/sincroniza, por padrão mantém no servidor, várias pastas (IETF, RFC 9051, "Internet Message Access Protocol (IMAP) - Version 4rev2"; Microsoft Learn, "POP3 e IMAP4 em Exchange Online"). Cco: o destinatário recebe a cópia e seu endereço não é visível aos demais (Microsoft, documentação de suporte, "Mostre, oculte e exiba o campo Cco (cópia oculta) no Outlook para Windows").
3.2 TEAMS. Equipe = coleção de pessoas, conteúdo e ferramentas; canal = seção dentro da equipe; canal padrão (todos os membros), privado (membros selecionados), compartilhado (pessoas dentro e fora da equipe) (Microsoft Learn, "Visão geral de equipes e canais no Microsoft Teams").
3.3 MEET (Google). Iniciar por "Nova reunião" ou por evento do Agenda (link associado ao evento); participar por link, código/apelido ou Agenda; sem Conta Google, o organizador ou um participante precisa autorizar; apresentar = guia, janela ou tela inteira; o compartilhamento pode ser limitado por administrador ou organizador (Ajuda do Google Meet, "Apresentar durante uma videochamada - Computador"; Ajuda do Google Meet, "Participar de uma reunião - Computador"; Ajuda do Google Meet, "Inicie ou agende uma videoconferência do Google Meet").
Validade: os pontos sobre o modo de exibição das alterações no Word, o compartilhamento e a restauração de versões no OneDrive, os canais do Teams e a apresentação de tela no Meet dependem de interface e comportamento de serviço e estão sujeitos a mudança.
```

## Curso

```text
## ITEM 1 — MSOFFICE 365 (WORD, EXCEL, POWERPOINT E ONEDRIVE) — VISÃO GERAL

### 1.0.1 O QUE É
O edital escreve "MSOffice 365". Nas páginas de suporte consultadas em 08/10/2026, a Microsoft trata Word, Excel, PowerPoint e Outlook como aplicativos do pacote Microsoft 365 (Microsoft, documentação de suporte, "Comparar o Outlook para PC, Outlook na web e o Outlook para iOS & Android": o Outlook para PC é descrito como "disponível para compra como parte do Microsoft 365", conforme a leitura de 08/10/2026). Para a prova, o que importa é o que cada aplicativo FAZ e a lógica de seus recursos, não o plano de assinatura. Preço, licença, plano e versão: ficam fora do estudo dos itens 1 e 3 de TI e Dados (informação sujeita a mudança).
Mapa mental dos quatro aplicativos do item 1:
- Word: texto (documentos, relatórios, minutas, ofícios).
- Excel: cálculo e análise de dados em planilhas (células, fórmulas, funções).
- PowerPoint: apresentações em slides.
- OneDrive: armazenamento de arquivos em nuvem, com compartilhamento e histórico de versões.
Observação metodológica: o curso abaixo prefere conceitos estáveis (que a banca costuma cobrar e que pouco mudam). Nomes de botões e caminhos de menu mudam entre versões; por isso os pontos sujeitos a mudança são poucos e vêm sinalizados.

## ITEM 1.1 — WORD

### 1.1.1 DEFINIÇÃO
Word é o editor de texto do pacote. Organiza o documento em parágrafos, estilos, tabelas, seções, cabeçalhos/rodapés e referências (sumário, notas). Três recursos de revisão e estruturação merecem atenção especial, porque aparecem nas provas: (i) controle de alterações; (ii) tabelas (mesclar × dividir células); (iii) sumário automático baseado em estilos.

### 1.1.2 CONTROLE DE ALTERAÇÕES (REVISÃO)
Conceito: o recurso registra as edições feitas por revisores (inserções, exclusões, formatações) sem apagar o texto original, para que o autor decida depois.
O que a fonte Microsoft, documentação de suporte, "Aceitar ou rejeitar alterações controladas no Word" afirma (leitura de 08/10/2026):
- Na guia "Revisão", no grupo "Acompanhamento", escolhe-se "Aceitar" ou "Rejeitar" para cada alteração; "Avançar" e "Anterior" apenas navegam, sem decidir.
- Para decidir de uma vez: lista suspensa "Aceitar" > "Aceitar Todas as Alterações"; lista suspensa "Rejeitar" > "Rejeitar Todas as Alterações".
- Antes de compartilhar o documento: o modo "Sem Marcação" só oculta as alterações temporariamente, e elas voltam a aparecer quando o documento é reaberto. Para removê-las de fato, é preciso aceitá-las ou rejeitá-las. A página também recomenda o Inspetor de Documentos para verificar alterações, comentários e informações ocultas.
Distinções que a banca explora:
- OCULTAR (modo de exibição) × RESOLVER (aceitar/rejeitar). Ocultar muda só a exibição; aceitar/rejeitar decide o conteúdo.
- ACEITAR (incorpora a alteração ao texto) × REJEITAR (descarta a alteração, restabelecendo o texto original).
- Navegar (Avançar/Anterior) não aceita nem rejeita.
Limite do curso: a fonte Microsoft, documentação de suporte, "Aceitar ou rejeitar alterações controladas no Word" NÃO descreve como ativar o acompanhamento.

### 1.1.3 TABELAS: MESCLAR × DIVIDIR CÉLULAS
Conforme Microsoft, documentação de suporte, "Mesclar ou dividir células em uma tabela" (leitura de 08/10/2026): mesclar combina duas ou mais células da tabela em uma única célula; a página descreve a combinação de células "na mesma linha ou coluna" e orienta, se o comando não aparecer, verificar se foram selecionadas "várias células adjacentes"; há comando para desfazer a mesclagem. O item sobre mesclar células usa o requisito de adjacência e não reproduz a expressão "na mesma linha ou coluna", para que ela não seja lida como definição exaustiva. Dividir parte de uma ou mais células marcadas e pergunta em quantas colunas ou linhas se quer subdividir. Os comandos ficam no contexto da tabela (guia "Layout" da tabela; também no clique com o botão direito, para mesclar). A página não diz o que acontece com o conteúdo das células.
Chave de prova: MESCLAR = muitas células viram uma; DIVIDIR = uma célula vira várias. Quem inverte, erra.

### 1.1.4 SUMÁRIO AUTOMÁTICO
Conforme Microsoft, documentação de suporte, "Inserir um sumário": "Os sumários no Word se baseiam nos títulos do documento." Quando faltam entradas, a causa costuma ser que os títulos não receberam estilo de título (a fonte Microsoft, documentação de suporte, "Inserir um sumário" diz "não estão formatados como cabeçalhos", no sentido de títulos de seção, e não do recurso Cabeçalho, que é o cabeçalho de página); a solução indicada é aplicar o estilo Título 1 ao texto de cada título que deve constar. Para atualizar após mudanças, clica-se com o botão direito no sumário e escolhe-se "Atualizar Campo". O sumário automático é inserido pela guia "Referências".
Ideia estável: o sumário automático é GERADO a partir dos estilos de título; digitar manualmente "Capítulo 1 ...... 3" não cria estrutura que o Word reconheça.

1.1.5 EXEMPLO APLICADO AO TRABALHO LEGISLATIVO (situação hipotética de redação/revisão)
Uma nota taquigráfica de reunião de comissão, trabalho típico do Derep (antigo DETAQ), chega ao revisor em Word. O revisor ativa o acompanhamento e corrige concordância, pontuação e grafia de nomes. O chefe da seção quer devolver o texto ao orador "limpo". Procedimento correto: percorrer as alterações, aceitar as pertinentes e rejeitar as indevidas (Microsoft, documentação de suporte, "Aceitar ou rejeitar alterações controladas no Word"); só trocar o modo para "Sem Marcação" NÃO limpa o arquivo, e as marcas voltariam ao reabrir. Antes de enviar a versão a terceiros, passar o Inspetor de Documentos (Microsoft, documentação de suporte, "Aceitar ou rejeitar alterações controladas no Word"). Em relatório longo com capítulos, usar estilos de título e inserir sumário automático; ao reorganizar capítulos, atualizar o campo. Em quadro de presenças com cabeçalho comum a várias colunas, usar mesclar para o cabeçalho e dividir para criar subcolunas.

### 1.1.6 PEGADINHAS PROVÁVEIS
P1. "O modo Sem Marcação exclui definitivamente as alterações controladas do arquivo" → ERRADO (só oculta; Microsoft, documentação de suporte, "Aceitar ou rejeitar alterações controladas no Word").
P2. "Avançar e Anterior, no grupo Acompanhamento, aceitam ou rejeitam a alteração" → ERRADO (apenas navegam).
P3. "Mesclar células divide uma célula em várias" → ERRADO (mesclar combina; dividir subdivide).
P4. "Aceitar uma alteração controlada restabelece o texto original" → ERRADO (isso é rejeitar).
P5. "O sumário automático independe da formatação dos títulos" → ERRADO (baseia-se nos títulos com estilo de título; Microsoft, documentação de suporte, "Inserir um sumário").
P6. "O sumário do Word se atualiza sozinho, sem qualquer ação, a cada alteração no documento" → ERRADO (o sumário é um campo: após mudanças que o afetem, atualiza-se com o botão direito > "Atualizar Campo"; Microsoft, documentação de suporte, "Inserir um sumário").

## ITEM 1.2 — EXCEL

### 1.2.1 DEFINIÇÃO
Excel é o programa de planilhas: dados em células (identificadas por coluna e linha, como B2), organizados em planilhas de uma pasta de trabalho; cálculos feitos por fórmulas (começam com "=") e funções.

### 1.2.2 REFERÊNCIAS: RELATIVA, ABSOLUTA E MISTA
Conforme Microsoft, documentação de suporte, "Alternar entre referências relativas, absolutas e mistas" (leitura de 08/10/2026):
- Por padrão, uma referência de célula é RELATIVA: muda de posição conforme a fórmula é copiada para outra célula.
- ABSOLUTA: para manter fixa a referência ao copiar, precede-se coluna e linha com o cifrão ($), por exemplo $B$2.
- MISTA: mistura as duas, fixando só a coluna ($B2) ou só a linha (B$2).
- A tecla F4, com a referência selecionada na barra de fórmulas, alterna entre os tipos (a página documenta isso).
Regra de ouro: O $ TRAVA o que vem imediatamente depois dele. $B2 trava a coluna B; B$2 trava a linha 2; $B$2 trava ambas.
Exemplo de leitura: fórmula =C3*$F$1 em D3, copiada para D4, vira =C4*$F$1: C3 (relativa) acompanhou a linha; $F$1 (absoluta) ficou. Uso típico: uma taxa ou um total fixo numa célula usado por muitas linhas.

### 1.2.3 FUNÇÃO SE
Conforme Microsoft, documentação de suporte, "SE (Função SE)": a função SE compara um valor com o esperado e verifica se a condição é atendida. Sintaxe: SE(teste_lógico, valor_se_verdadeiro, [valor_se_falso]). O primeiro resultado vale se a comparação for Verdadeira; o segundo, se for Falsa. O colchete na sintaxe indica o argumento opcional (valor_se_falso).
Exemplo: =SE(B2>=10; "Quórum"; "Sem quórum") devolve "Quórum" se B2 (presentes) for 10 ou mais; caso contrário, "Sem quórum". (Valores do exemplo são ilustrativos.)

### 1.2.4 FUNÇÃO PROCV
Conforme Microsoft, documentação de suporte, "Pesquisar valores com PROCV, ÍNDICE ou CORRESP": o PROCV pesquisa um valor e devolve outro, relacionado, de uma coluna do intervalo. O quarto argumento é opcional: com FALSO, devolve correspondência EXATA; com VERDADEIRO, ou deixando o argumento em branco, devolve correspondência APROXIMADA (o valor mais próximo que não ultrapasse o procurado). A página afirma que o PROCV "só pode pesquisar um valor da esquerda para a direita": a coluna com o valor procurado precisa estar à esquerda da coluna de retorno; caso contrário, recomenda ÍNDICE e CORRESP.
Chave de prova: para código, matrícula, nome (identificadores) quase sempre se quer EXATA (FALSO); aproximada serve a faixas ordenadas (ex.: tabela de alíquotas). Omitir o quarto argumento NÃO equivale a FALSO.

1.2.5 EXEMPLO APLICADO AO TRABALHO LEGISLATIVO (hipotético)
Planilha de controle de entrega de notas taquigráficas por comissão: coluna A com o código da reunião, B com o número de laudas, C com o prazo. Para marcar atraso: =SE(D2>C2; "Atrasado"; "No prazo"). Para trazer o nome do revisor responsável, a partir de uma tabela de revisores, usa-se PROCV com FALSO (correspondência exata do código). Ao copiar a fórmula por centenas de linhas, a referência à tabela de revisores precisa estar travada com $ (absoluta), senão ela "desliza" e o PROCV passa a procurar numa área errada.

### 1.2.6 PEGADINHAS PROVÁVEIS
P1. "Na referência B$2, a coluna fica fixa e a linha se ajusta ao copiar" → ERRADO (o $ antes do 2 trava a linha; a coluna se ajusta).
P2. "Toda referência de célula é absoluta por padrão" → ERRADO (por padrão é relativa; Microsoft, documentação de suporte, "Alternar entre referências relativas, absolutas e mistas").
P3. "No PROCV, omitir o quarto argumento produz correspondência exata" → ERRADO (em branco = aproximada; Microsoft, documentação de suporte, "Pesquisar valores com PROCV, ÍNDICE ou CORRESP").
P4. "O PROCV pesquisa o valor em qualquer coluna do intervalo e devolve valores de colunas à esquerda dela" → ERRADO (só da esquerda para a direita; Microsoft, documentação de suporte, "Pesquisar valores com PROCV, ÍNDICE ou CORRESP").
P5. "Na função SE, o segundo argumento é o resultado para teste falso" → ERRADO (o segundo é para verdadeiro).
P6. "O valor_se_falso é obrigatório na função SE" → ERRADO (aparece entre colchetes na sintaxe, isto é, opcional; Microsoft, documentação de suporte, "SE (Função SE)").

## ITEM 1.3 — POWERPOINT

### 1.3.1 DEFINIÇÃO
PowerPoint é o programa de apresentações: slides com texto, imagens, gráficos e mídia, exibidos em sequência. Dois temas são estáveis e cobráveis: slide mestre e animações × transições.

### 1.3.2 SLIDE MESTRE
Conforme Microsoft, documentação de suporte, "O que é um slide master no PowerPoint?": o propósito é fazer todos os slides terem as mesmas fontes e imagens (como logotipos). "Quando você edita o slide mestre, todos os slides baseados nele conterão essas alterações." Acesso: guia "Exibir" > "Slide Mestre". Ideia estável: o mestre concentra o padrão visual; alterar o mestre muda os slides baseados nele, de uma vez; alterar um slide individual muda só aquele.

### 1.3.3 ANIMAÇÕES × TRANSIÇÕES
Conforme Microsoft, documentação de suporte, "A diferença entre animações e transições": a animação é aplicada a um único elemento em um slide (um slide pode ter várias); a transição é aplicada a um slide inteiro (só uma por slide) e acontece na passagem do slide anterior para aquele que a recebe.
Chave de prova: ANIMAÇÃO = efeito num OBJETO dentro do slide; TRANSIÇÃO = efeito na MUDANÇA DE SLIDE.

1.3.4 EXEMPLO APLICADO AO TRABALHO LEGISLATIVO (hipotético)
Apresentação institucional de treinamento sobre fluxo de revisão de notas taquigráficas, com 30 slides: o logotipo e a fonte padrão são colocados uma única vez no slide mestre (Microsoft, documentação de suporte, "O que é um slide master no PowerPoint?"); todos os slides herdam. Para fazer um tópico de lista aparecer ponto a ponto, aplica-se animação ao texto (objeto); para suavizar a passagem de um slide a outro, aplica-se transição ao slide (Microsoft, documentação de suporte, "A diferença entre animações e transições"). Efeitos em excesso distraem do conteúdo; a apresentação serve ao orador, não o contrário.

### 1.3.5 PEGADINHAS PROVÁVEIS
P1. "A transição é aplicada a um objeto individual do slide e a animação, ao slide inteiro" → ERRADO (inverso; Microsoft, documentação de suporte, "A diferença entre animações e transições").
P2. "Alterar o slide mestre afeta apenas o slide que está selecionado" → ERRADO (afeta os slides baseados nele; Microsoft, documentação de suporte, "O que é um slide master no PowerPoint?").
P3. "Cada slide pode receber várias transições simultâneas" → ERRADO (uma transição por slide; Microsoft, documentação de suporte, "A diferença entre animações e transições").
P4. "O slide mestre é aberto na guia Inserir" → ERRADO (guia Exibir; Microsoft, documentação de suporte, "O que é um slide master no PowerPoint?") — informação sujeita a mudança.

## ITEM 1.4 — ONEDRIVE

### 1.4.1 DEFINIÇÃO
OneDrive é o serviço de armazenamento de arquivos em nuvem da Microsoft: o arquivo fica guardado online, acessível por navegador e (com o aplicativo de sincronização) pelo Explorador de Arquivos (Microsoft, documentação de suporte, "Restaurar uma versão anterior de um ficheiro armazenado no OneDrive"). Recursos cobráveis: compartilhamento com permissões e histórico de versões.

### 1.4.2 COMPARTILHAMENTO E PERMISSÕES
Conforme Microsoft, documentação de suporte, "Colaborar no Microsoft OneDrive: partilhar, editar e gerir Files" e Microsoft, documentação de suporte, "Gerenciar compartilhamento e permissões no OneDrive e no SharePoint" (leitura de 08/10/2026):
- Seleciona-se o item e escolhe-se Compartilhar (Partilhar); na configuração do link ("Todas as pessoas com este link podem editar este item"), marca-se "Permitir edição" para que outras pessoas possam editar ou desmarca-se para que possam apenas visualizar (Microsoft, documentação de suporte, "Colaborar no Microsoft OneDrive: partilhar, editar e gerir Files"). A fonte Microsoft, documentação de suporte, "Colaborar no Microsoft OneDrive: partilhar, editar e gerir Files" também usa os rótulos "Pode editar" e "Pode exibir".
- Se você for o proprietário do arquivo (ou tiver permissão de edição), pode parar o compartilhamento ou alterar as permissões (Microsoft, documentação de suporte, "Colaborar no Microsoft OneDrive: partilhar, editar e gerir Files"); selecionando o X ao lado de um link, desabilita-se o link (Microsoft, documentação de suporte, "Colaborar no Microsoft OneDrive: partilhar, editar e gerir Files").
- A fonte Microsoft, documentação de suporte, "Gerenciar compartilhamento e permissões no OneDrive e no SharePoint" trata de "Interromper o compartilhamento" e de alternar permissões "entre exibir e editar" para quem tem acesso direto; ela ainda avisa que NÃO é possível mudar o tipo de permissão de um LINK de compartilhamento (de edição para exibição ou o contrário) e orienta excluir o link e criar outro. As duas páginas descrevem a gestão de permissões de maneiras diferentes; por isso fica fora do estudo o ponto "como alterar a permissão de um link existente".
Chave de prova: EXIBIR = ler; EDITAR = ler e alterar. Compartilhar não transfere a propriedade do arquivo (conceito geral).

### 1.4.3 HISTÓRICO DE VERSÕES
Conforme Microsoft, documentação de suporte, "Restaurar uma versão anterior de um ficheiro armazenado no OneDrive": o histórico de versões permite ver e restaurar versões mais antigas dos arquivos; "funciona com todos os tipos de ficheiros"; em contas escolares ou profissionais o administrador pode ter desativado o controle de versões. Para restaurar: selecionar o arquivo > "Histórico de versões" > reticências ao lado da versão > "Restaurar"; só um arquivo por vez. A versão restaurada torna-se a versão atual, e a versão que era a atual passa a aparecer na lista como versão anterior. A página menciona um prazo de retenção do histórico; esse dado é numérico e fica fora do estudo.
Chave de prova: restaurar uma versão NÃO apaga a versão que era a atual; ela vira "anterior". Histórico de versões ≠ lixeira (que recupera arquivo excluído — conceito geral, sem fonte aberta).

1.4.4 EXEMPLO APLICADO AO TRABALHO LEGISLATIVO (hipotético)
Uma minuta de ato é produzida em Word e guardada no OneDrive. A chefia compartilha o link com dois revisores com permissão de edição e com o gabinete solicitante apenas com exibição (Microsoft, documentação de suporte, "Colaborar no Microsoft OneDrive: partilhar, editar e gerir Files"). Um revisor salva por engano uma versão com trecho apagado; o autor abre o histórico de versões, restaura a versão anterior à edição indevida, e a versão que estava em vigor permanece listada como versão anterior (Microsoft, documentação de suporte, "Restaurar uma versão anterior de um ficheiro armazenado no OneDrive"). Terminado o trabalho, o autor interrompe o compartilhamento (Microsoft, documentação de suporte, "Gerenciar compartilhamento e permissões no OneDrive e no SharePoint").

### 1.4.5 PEGADINHAS PROVÁVEIS
P1. "Ao restaurar uma versão anterior, a versão que era a atual é descartada" → ERRADO (passa a constar como versão anterior; Microsoft, documentação de suporte, "Restaurar uma versão anterior de um ficheiro armazenado no OneDrive").
P2. "Quem recebe um link com permissão apenas de exibição pode editar o arquivo original" → ERRADO.
P3. "O histórico de versões do OneDrive só funciona com arquivos do Word" → ERRADO (funciona com todos os tipos de arquivo; Microsoft, documentação de suporte, "Restaurar uma versão anterior de um ficheiro armazenado no OneDrive").
P4. "Só é possível restaurar versões usando o aplicativo de sincronização, nunca pelo site" → ERRADO (a fonte Microsoft, documentação de suporte, "Restaurar uma versão anterior de um ficheiro armazenado no OneDrive" descreve os dois caminhos).
P5. "Interromper o compartilhamento transfere a propriedade do arquivo ao destinatário" → ERRADO (conceito geral; o proprietário mantém o arquivo).

## ITEM 3 — FERRAMENTAS DE COMUNICAÇÃO E COLABORAÇÃO

## ITEM 3.1 — CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL)

### 3.1.1 DEFINIÇÃO
Correio eletrônico é o serviço de troca de mensagens entre caixas postais, mantidas em servidores. Há duas formas de acesso, que a banca costuma confrontar:
- WEBMAIL: acesso à caixa postal por navegador, sem necessidade de aplicativo específico instalado no dispositivo. Exemplo documentado: Outlook na Web, "acessível a partir da maioria dos browsers" (Microsoft, documentação de suporte, "Comparar o Outlook para PC, Outlook na web e o Outlook para iOS & Android", leitura de 08/10/2026).
- CLIENTE DE E-MAIL: programa de correio próprio, em regra instalado no computador ou no celular, que acessa a caixa postal no servidor (por exemplo, por POP3 ou IMAP4) e envia por SMTP (conceito geral; Microsoft Learn, "POP3 e IMAP4 em Exchange Online" para os protocolos) (exemplo documentado: Outlook para PC, "aplicação de e-mail e calendário com as funcionalidades mais completa", Microsoft, documentação de suporte, "Comparar o Outlook para PC, Outlook na web e o Outlook para iOS & Android"). A definição de "cliente = aplicativo instalado" é conceito geral; a fonte Microsoft, documentação de suporte, "Comparar o Outlook para PC, Outlook na web e o Outlook para iOS & Android" não usa a palavra "instalado".

3.1.2 PROTOCOLOS (CONCEITO ESTÁVEL; RFCs DA IETF E Microsoft Learn, "POP3 e IMAP4 em Exchange Online")
- SMTP: transferência de mensagens. A RFC 5321 (IETF, RFC 5321, "Simple Mail Transfer Protocol") diz que "The objective of the Simple Mail Transfer Protocol (SMTP) is to transfer mail reliably and efficiently" (seção 1.1; leitura de 08/10/2026). Cliente de e-mail POP3/IMAP4 depende do SMTP para ENVIAR (Microsoft Learn, "POP3 e IMAP4 em Exchange Online": "dependem do protocolo SMTP para enviar mensagens").
- POP3 (IETF, RFC 1939, "Post Office Protocol - Version 3"): permite à estação de trabalho acessar a caixa postal no servidor; normalmente, "mail is downloaded and then deleted". Segundo Microsoft Learn, "POP3 e IMAP4 em Exchange Online", por padrão os clientes POP3 removem as mensagens baixadas do servidor, o que dificulta o acesso por vários computadores (pode-se configurar para manter cópias); baixam para uma única pasta e não sincronizam várias pastas.
- IMAP4 (IETF, RFC 9051, "Internet Message Access Protocol (IMAP) - Version 4rev2"): permite a um cliente acessar e manipular mensagens no servidor, com caixas de correio (pastas remotas) e ressincronização de cliente offline. Segundo Microsoft Learn, "POP3 e IMAP4 em Exchange Online", por padrão os clientes IMAP4 NÃO removem as mensagens baixadas do servidor (facilita o acesso por vários computadores) e dão suporte a várias pastas. A RFC 9051 diz que o IMAP4rev2 "does not specify a means of posting mail" e remete o envio a um protocolo de submissão de mensagens (RFC 6409); na prática do cliente de e-mail, o envio fica com o SMTP (Microsoft Learn, "POP3 e IMAP4 em Exchange Online": os programas POP3 e IMAP4 "dependem do protocolo SMTP para enviar mensagens").
Resumo: SMTP = ENVIA; POP3 = BAIXA (e, por padrão, apaga do servidor); IMAP4 = ACESSA/SINCRONIZA (as mensagens ficam no servidor).
A fonte Microsoft Learn, "POP3 e IMAP4 em Exchange Online" lista portas e criptografia do Exchange Online; esses números são específicos de produto e ficam fora do estudo.

### 3.1.3 CAMPOS DE DESTINATÁRIO: PARA, CC E CCO
- Para: destinatários principais. Cc (com cópia): destinatários de ciência; os endereços aparecem para todos (conceito geral).
- Cco (cópia oculta): conforme Microsoft, documentação de suporte, "Mostre, oculte e exiba o campo Cco (cópia oculta) no Outlook para Windows" (leitura de 08/10/2026), quem é inserido no campo Cco recebe a cópia do e-mail "sem que seu nome seja visível para os outros destinatários"; "Outras pessoas que recebem a mensagem não veem o endereço de quem está na linha Cco."
Chave de prova: Cco RECEBE a mensagem, mas fica OCULTO para os demais.

3.1.4 EXEMPLO APLICADO AO TRABALHO LEGISLATIVO (hipotético)
Servidor do Derep (antigo DETAQ) envia a convocação de uma reunião de revisão a trinta colegas externos à unidade. Se colocar todos em "Para" ou "Cc", os endereços ficam visíveis uns para os outros; para preservar os endereços, usa-se o campo Cco (Microsoft, documentação de suporte, "Mostre, oculte e exiba o campo Cco (cópia oculta) no Outlook para Windows"). Em casa, o servidor lê o e-mail pelo webmail, no navegador, sem instalar nada; no computador de trabalho, usa um cliente de e-mail instalado, que, quando configurado com IMAP4, mantém as mensagens no servidor e sincroniza as pastas (Microsoft Learn, "POP3 e IMAP4 em Exchange Online") e envia por SMTP (Microsoft Learn, "POP3 e IMAP4 em Exchange Online"). Fora do ambiente institucional (conta pessoal, rede externa), valem os cuidados de sigilo do tópico 6 de TI e Dados.

### 3.1.5 PEGADINHAS PROVÁVEIS
P1. "O webmail exige a instalação de um programa cliente no computador" → ERRADO (acesso por navegador; Microsoft, documentação de suporte, "Comparar o Outlook para PC, Outlook na web e o Outlook para iOS & Android").
P2. "O cliente de e-mail é acessado exclusivamente pelo navegador" → ERRADO (aplicativo próprio; conceito geral).
P3. "Por padrão, clientes IMAP4 removem do servidor as mensagens baixadas" → ERRADO (isso é o padrão do POP3; Microsoft Learn, "POP3 e IMAP4 em Exchange Online").
P4. "O POP3 serve para enviar mensagens ao servidor de saída" → ERRADO (o envio é do SMTP; Microsoft Learn, "POP3 e IMAP4 em Exchange Online"; IETF, RFC 5321, "Simple Mail Transfer Protocol").
P5. "O destinatário incluído em Cco não recebe a mensagem" → ERRADO (recebe, mas fica oculto; Microsoft, documentação de suporte, "Mostre, oculte e exiba o campo Cco (cópia oculta) no Outlook para Windows").
P6. "Os endereços do campo Cco são visíveis aos demais destinatários" → ERRADO (Microsoft, documentação de suporte, "Mostre, oculte e exiba o campo Cco (cópia oculta) no Outlook para Windows").
P7. "O IMAP4 baixa as mensagens para uma única pasta do cliente e não sincroniza várias pastas" → ERRADO (essa limitação é do POP3; Microsoft Learn, "POP3 e IMAP4 em Exchange Online").

## ITEM 3.2 — MICROSOFT TEAMS

### 3.2.1 DEFINIÇÃO
Microsoft Teams é a plataforma de comunicação e colaboração da Microsoft. A fonte Microsoft, documentação de suporte, "Explore a nova experiência de chat e canais no Microsoft Teams" descreve a nova experiência como a que "simplifica as conversas ao colocar o chat, as equipas e os canais num único local" (leitura de 08/10/2026). Reuniões e chamadas existem no Teams (conceito geral; sem fonte consultada para detalhes).

### 3.2.2 EQUIPES E CANAIS
Conforme Microsoft Learn, "Visão geral de equipes e canais no Microsoft Teams" (leitura de 08/10/2026):
- Equipes são "coleções de pessoas, conteúdo e ferramentas que envolvem diferentes projetos e resultados dentro de uma organização".
- Canais são seções dedicadas dentro de uma equipe para manter as conversas organizadas por tópicos, projetos etc.
- Os canais podem ser abertos a todos os membros da equipe (canais padrão), a membros selecionados da equipe (canais privados) ou a pessoas selecionadas dentro e fora da equipe (canais compartilhados). Segundo a tabela da página, no canal compartilhado pessoas podem ser adicionadas sem entrarem na equipe e participantes externos (Conexão Direta B2B) podem participar.
Hierarquia: ORGANIZAÇÃO > EQUIPE > CANAIS. A equipe agrupa; o canal organiza a conversa por assunto.
Limite: a fonte Microsoft Learn, "Visão geral de equipes e canais no Microsoft Teams" não define o canal padrão em sentença própria (a frase acima é a descrição mais próxima) e a fonte Microsoft, documentação de suporte, "Explore a nova experiência de chat e canais no Microsoft Teams" não diz quem pode ver as conversas.

3.2.3 EXEMPLO APLICADO AO TRABALHO LEGISLATIVO (hipotético)
Uma equipe "Revisão de notas" com canais por comissão para discutir dúvidas de grafia de nomes; um canal privado reservado à chefia; um canal compartilhado com pessoa de outro órgão convidada a colaborar sem integrar a equipe (Microsoft Learn, "Visão geral de equipes e canais no Microsoft Teams"). Informações sigilosas só podem circular em ferramenta homologada pela Casa (tópico 6 de TI e Dados).

### 3.2.4 PEGADINHAS PROVÁVEIS
P1. "No Teams, o canal privado é aberto a todos os membros da equipe e o canal padrão é restrito a membros selecionados" → ERRADO (inverso; Microsoft Learn, "Visão geral de equipes e canais no Microsoft Teams").
P2. "O canal compartilhado só pode ter membros da própria equipe" → ERRADO (inclui pessoas dentro e fora da equipe; Microsoft Learn, "Visão geral de equipes e canais no Microsoft Teams").
P3. "Equipe e canal são sinônimos" → ERRADO (o canal é uma seção dentro da equipe; Microsoft Learn, "Visão geral de equipes e canais no Microsoft Teams").

## ITEM 3.3 — GOOGLE MEET

### 3.3.1 DEFINIÇÃO
Google Meet é o serviço de videoconferência do Google (conceito geral; as fontes Ajuda do Google Meet, "Apresentar durante uma videochamada - Computador"; Ajuda do Google Meet, "Participar de uma reunião - Computador"; Ajuda do Google Meet, "Inicie ou agende uma videoconferência do Google Meet" descrevem o uso). É produto DISTINTO do Teams: Teams é da Microsoft; Meet é do Google.

### 3.3.2 INICIAR, AGENDAR E PARTICIPAR
- Iniciar: no computador, abre-se o Meet e escolhe-se "Nova reunião" (criar para mais tarde, com link para compartilhar, ou iniciar instantânea) (Ajuda do Google Meet, "Inicie ou agende uma videoconferência do Google Meet").
- Agendar: ao criar um evento no Google Agenda (a fonte Ajuda do Google Meet, "Inicie ou agende uma videoconferência do Google Meet", em pt-PT, chama-o "Calendário Google"), clica-se em "Adicionar videoconferência do Google Meet" para associar um link de videoconferência ao evento, que é compartilhado com os convidados (Ajuda do Google Meet, "Inicie ou agende uma videoconferência do Google Meet").
- Participar: pelo link da reunião (clicar e "Participar agora"); por código ou apelido, em meet.google.com; ou pelo evento do Google Agenda ("Entrar com o Google Meet") (Ajuda do Google Meet, "Participar de uma reunião - Computador").
- Sem Conta do Google: a página diz que "o organizador ou um participante precisa autorizar seu acesso"; o usuário digita o nome e escolhe "Pedir para participar" (Ajuda do Google Meet, "Participar de uma reunião - Computador").

### 3.3.3 APRESENTAR (COMPARTILHAR TELA)
Conforme Ajuda do Google Meet, "Apresentar durante uma videochamada - Computador" (leitura de 08/10/2026): "Você pode apresentar uma guia, uma janela específica ou a tela inteira em uma reunião"; no passo de apresentação seleciona-se "Uma guia", "Uma janela" ou "A tela inteira". Ao apresentar uma guia do Chrome, o áudio é compartilhado por padrão; em janela ou tela inteira, o áudio do sistema só é compartilhado se a opção "Compartilhar também o áudio do sistema" for ativada. Para parar: "Parar apresentação". A página informa que o compartilhamento pode estar desativado por configurações do administrador ou limitado por controles do organizador. A página não diz que os participantes precisam de permissão para ver a apresentação.
Chave de prova: três escopos de compartilhamento: GUIA, JANELA, TELA INTEIRA. Quanto mais restrito o escopo, menos conteúdo exposto (conceito geral).

3.3.4 EXEMPLO APLICADO AO TRABALHO LEGISLATIVO (hipotético)
Reunião de alinhamento de revisão com colaboradores externos que usam o Meet: o organizador cria o evento no Agenda e associa a ele um link de videoconferência, clicando em "Adicionar videoconferência do Google Meet" (Ajuda do Google Meet, "Inicie ou agende uma videoconferência do Google Meet"); para mostrar apenas o documento de trabalho, compartilha-se a janela do programa, e não a tela inteira, evitando expor e-mails ou outras janelas abertas (Ajuda do Google Meet, "Apresentar durante uma videochamada - Computador"; cuidado de privacidade é conceito geral).

### 3.3.5 PEGADINHAS PROVÁVEIS
P1. "Ao apresentar no Meet, só é possível compartilhar a tela inteira" → ERRADO (guia, janela ou tela inteira; Ajuda do Google Meet, "Apresentar durante uma videochamada - Computador").
P2. "Teams e Meet são produtos da mesma empresa" → ERRADO (Microsoft × Google; conceito geral).
P3. "O link de uma reunião do Meet só pode ser criado por meio de um evento do Google Agenda" → ERRADO (também se cria em "Nova reunião", no próprio Meet; Ajuda do Google Meet, "Inicie ou agende uma videoconferência do Google Meet").
P4. "O compartilhamento de tela no Meet nunca pode ser restringido" → ERRADO (pode ser desativado por administrador ou limitado pelo organizador; Ajuda do Google Meet, "Apresentar durante uma videochamada - Computador").
```

## Pares

- C1. **Referência relativa** × **absoluta × mista (Excel)** | relativa: muda ao copiar (padrão) | absoluta ($B$2): fixa coluna e linha; mista: fixa só uma ($B2 coluna; B$2 linha) | Troca: dizer que B$2 fixa a coluna; que a referência é absoluta por padrão.
- C2. **Mesclar** × **dividir células (Word)** | mesclar: várias células viram uma | dividir: uma célula vira várias | Troca: inverter os verbos.
- C3. **Ocultar** × **resolver alterações controladas (Word)** | "Sem Marcação": oculta, temporariamente | aceitar ou rejeitar: decide e remove a marca | Troca: "Sem Marcação remove definitivamente as alterações".
- C4. **Aceitar** × **rejeitar alteração (Word)** | aceitar: incorpora ao texto | rejeitar: descarta, restabelece o original | Troca: inverter; ou dizer que "Avançar" aceita.
- C5. **Sumário automático** × **digitado à mão** | gerado a partir dos títulos com estilo | texto digitado sem vínculo com a estrutura | Troca: "o sumário automático independe da formatação dos títulos".
- C6. **SE: verdadeiro** × **falso** | 2º argumento: resultado se verdadeiro | 3º argumento (opcional): resultado se falso | Troca: inverter a ordem; tornar o 3º obrigatório.
- C7. **PROCV exata** × **aproximada** | FALSO: exata | VERDADEIRO ou omitido: aproximada | Troca: "omitir o 4º argumento dá correspondência exata".
- C8. **PROCV** × **ÍNDICE/CORRESP (direção da pesquisa)** | PROCV: pesquisa da esquerda para a direita | ÍNDICE e CORRESP: alternativa quando o valor procurado não está à esquerda | Troca: dizer que o PROCV pesquisa para a esquerda.
- C9. **Animação** × **transição (PowerPoint)** | animação: elemento do slide (vários por slide) | transição: slide inteiro (um por slide), na passagem de slides | Troca: inverter o alvo.
- C10. **Slide mestre** × **alteração em slide isolado** | mestre: afeta os slides baseados nele | slide isolado: só aquele | Troca: "editar o mestre afeta só o slide selecionado".
- C11. **Compartilhar com exibição** × **com edição (OneDrive)** | exibir: leitura | editar: leitura e alteração | Troca: dizer que quem só exibe pode editar o original.
- C12. **Restaurar versão** × **descartar a atual (OneDrive)** | restaurar: a restaurada vira a atual; a atual anterior vira versão anterior | descartar/apagar | Troca: "ao restaurar, a atual é descartada".
- C13. **Webmail** × **cliente de e-mail** | navegador, sem instalação de programa de e-mail | aplicativo instalado no dispositivo | Troca: inverter as formas de acesso.
- C14. **SMTP** × **POP3 × IMAP4** | SMTP: envia | POP3: baixa (por padrão remove do servidor); IMAP4: acessa e sincroniza (por padrão mantém no servidor) | Troca: "POP3 envia"; "IMAP remove do servidor por padrão"; "IMAP baixa só para uma pasta".
- C15. **Para/Cc** × **Cco** | endereços visíveis a todos | Cco: recebe a cópia, endereço oculto aos demais | Troca: "Cco não recebe a mensagem"; "Cco é visível aos demais".
- C16. **Equipe** × **canal (Teams)** | equipe: coleção de pessoas, conteúdo e ferramentas | canal: seção dentro da equipe, por tópico/projeto | Troca: tratar como sinônimos.
- C17. **Canal padrão** × **privado × compartilhado (Teams)** | padrão: todos os membros da equipe | privado: membros selecionados; compartilhado: pessoas dentro e fora da equipe | Troca: inverter padrão e privado; limitar o compartilhado à equipe.
- C18. **Apresentar guia** × **janela × tela inteira (Meet)** | guia: uma aba (áudio da guia compartilhado por padrão) | janela específica; tela inteira (áudio do sistema só se a opção for ativada) | Troca: "só é possível a tela inteira".
- C19. **Teams** × **Meet** | Teams: Microsoft | Meet: Google | Troca: atribuir os dois à mesma empresa (conceito geral).

## Pegadinhas

- [P1-1] **WORD** — "O modo Sem Marcação exclui definitivamente as alterações controladas do arquivo" → ERRADO (só oculta; Microsoft, documentação de suporte, "Aceitar ou rejeitar alterações controladas no Word").
- [P1-1] **WORD** — "Avançar e Anterior, no grupo Acompanhamento, aceitam ou rejeitam a alteração" → ERRADO (apenas navegam).
- [P1-1] **WORD** — "Mesclar células divide uma célula em várias" → ERRADO (mesclar combina; dividir subdivide).
- [P1-1] **WORD** — "Aceitar uma alteração controlada restabelece o texto original" → ERRADO (isso é rejeitar).
- [P1-1] **WORD** — "O sumário automático independe da formatação dos títulos" → ERRADO (baseia-se nos títulos com estilo de título; Microsoft, documentação de suporte, "Inserir um sumário").
- [P1-1] **WORD** — "O sumário do Word se atualiza sozinho, sem qualquer ação, a cada alteração no documento" → ERRADO (o sumário é um campo: após mudanças que o afetem, atualiza-se com o botão direito > "Atualizar Campo"; Microsoft, documentação de suporte, "Inserir um sumário").
- [P1-1] **EXCEL** — "Na referência B$2, a coluna fica fixa e a linha se ajusta ao copiar" → ERRADO (o $ antes do 2 trava a linha; a coluna se ajusta).
- [P1-1] **EXCEL** — "Toda referência de célula é absoluta por padrão" → ERRADO (por padrão é relativa; Microsoft, documentação de suporte, "Alternar entre referências relativas, absolutas e mistas").
- [P1-1] **EXCEL** — "No PROCV, omitir o quarto argumento produz correspondência exata" → ERRADO (em branco = aproximada; Microsoft, documentação de suporte, "Pesquisar valores com PROCV, ÍNDICE ou CORRESP").
- [P1-1] **EXCEL** — "O PROCV pesquisa o valor em qualquer coluna do intervalo e devolve valores de colunas à esquerda dela" → ERRADO (só da esquerda para a direita; Microsoft, documentação de suporte, "Pesquisar valores com PROCV, ÍNDICE ou CORRESP").
- [P1-1] **EXCEL** — "Na função SE, o segundo argumento é o resultado para teste falso" → ERRADO (o segundo é para verdadeiro).
- [P1-1] **EXCEL** — "O valor_se_falso é obrigatório na função SE" → ERRADO (aparece entre colchetes na sintaxe, isto é, opcional; Microsoft, documentação de suporte, "SE (Função SE)").
- [P1-1] **POWERPOINT** — "A transição é aplicada a um objeto individual do slide e a animação, ao slide inteiro" → ERRADO (inverso; Microsoft, documentação de suporte, "A diferença entre animações e transições").
- [P1-1] **POWERPOINT** — "Alterar o slide mestre afeta apenas o slide que está selecionado" → ERRADO (afeta os slides baseados nele; Microsoft, documentação de suporte, "O que é um slide master no PowerPoint?").
- [P1-1] **POWERPOINT** — "Cada slide pode receber várias transições simultâneas" → ERRADO (uma transição por slide; Microsoft, documentação de suporte, "A diferença entre animações e transições").
- [P1-1] **POWERPOINT** — "O slide mestre é aberto na guia Inserir" → ERRADO (guia Exibir; Microsoft, documentação de suporte, "O que é um slide master no PowerPoint?") — informação sujeita a mudança.
- [P1-1] **ONEDRIVE** — "Ao restaurar uma versão anterior, a versão que era a atual é descartada" → ERRADO (passa a constar como versão anterior; Microsoft, documentação de suporte, "Restaurar uma versão anterior de um ficheiro armazenado no OneDrive").
- [P1-1] **ONEDRIVE** — "Quem recebe um link com permissão apenas de exibição pode editar o arquivo original" → ERRADO.
- [P1-1] **ONEDRIVE** — "O histórico de versões do OneDrive só funciona com arquivos do Word" → ERRADO (funciona com todos os tipos de arquivo; Microsoft, documentação de suporte, "Restaurar uma versão anterior de um ficheiro armazenado no OneDrive").
- [P1-1] **ONEDRIVE** — "Só é possível restaurar versões usando o aplicativo de sincronização, nunca pelo site" → ERRADO (a fonte Microsoft, documentação de suporte, "Restaurar uma versão anterior de um ficheiro armazenado no OneDrive" descreve os dois caminhos).
- [P1-1] **ONEDRIVE** — "Interromper o compartilhamento transfere a propriedade do arquivo ao destinatário" → ERRADO (conceito geral; o proprietário mantém o arquivo).
- [P1-1] **EXCEL** — Não confunda referência relativa com absoluta e mista: a relativa, que é o padrão, muda de posição quando a fórmula é copiada; a absoluta ($B$2) fixa coluna e linha; a mista fixa só a coluna ($B2) ou só a linha (B$2). Armadilha: o $ trava o que vem imediatamente depois dele.
- [P1-1] **WORD** — Não confunda ocultar alterações com resolvê-las no Word: o modo Sem Marcação só oculta as alterações, temporariamente, e elas voltam ao reabrir o documento; aceitar ou rejeitar decide o conteúdo e é o que as remove de fato. Armadilha: trocar para Sem Marcação não limpa o arquivo.
- [P1-1] **WORD** — Não confunda aceitar com rejeitar uma alteração controlada: aceitar incorpora a alteração ao texto; rejeitar a descarta, restabelecendo o texto original. Armadilha: Avançar e Anterior apenas navegam, sem aceitar nem rejeitar.
- [P1-1] **WORD** — Não confunda sumário automático com sumário digitado à mão: o automático é gerado a partir dos títulos com estilo de título e é atualizado com Atualizar Campo; o digitado à mão não cria estrutura que o Word reconheça. Armadilha: dizer que o sumário automático independe da formatação dos títulos.
- [P1-1] **EXCEL** — Não confunda correspondência exata com aproximada no PROCV: com FALSO no quarto argumento, a correspondência é exata; com VERDADEIRO ou com o argumento em branco, é aproximada, isto é, o valor mais próximo que não ultrapasse o procurado. Armadilha: omitir o quarto argumento não equivale a FALSO.
- [P1-1] **EXCEL** — Não confunda PROCV com ÍNDICE e CORRESP quanto à direção da pesquisa: o PROCV só pesquisa da esquerda para a direita, e a coluna do valor procurado precisa estar à esquerda da coluna de retorno; se não estiver, recomendam-se ÍNDICE e CORRESP.
- [P1-1] **ONEDRIVE** — Não confunda compartilhar com exibição e com edição no OneDrive: com exibição, quem recebe o link apenas lê; com edição, lê e altera o arquivo. Armadilha: achar que compartilhar transfere a propriedade do arquivo.
- [P1-3] **CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL)** — "O webmail exige a instalação de um programa cliente no computador" → ERRADO (acesso por navegador; Microsoft, documentação de suporte, "Comparar o Outlook para PC, Outlook na web e o Outlook para iOS & Android").
- [P1-3] **CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL)** — "O cliente de e-mail é acessado exclusivamente pelo navegador" → ERRADO (aplicativo próprio; conceito geral).
- [P1-3] **CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL)** — "Por padrão, clientes IMAP4 removem do servidor as mensagens baixadas" → ERRADO (isso é o padrão do POP3; Microsoft Learn, "POP3 e IMAP4 em Exchange Online").
- [P1-3] **CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL)** — "O POP3 serve para enviar mensagens ao servidor de saída" → ERRADO (o envio é do SMTP; Microsoft Learn, "POP3 e IMAP4 em Exchange Online"; IETF, RFC 5321, "Simple Mail Transfer Protocol").
- [P1-3] **CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL)** — "O destinatário incluído em Cco não recebe a mensagem" → ERRADO (recebe, mas fica oculto; Microsoft, documentação de suporte, "Mostre, oculte e exiba o campo Cco (cópia oculta) no Outlook para Windows").
- [P1-3] **CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL)** — "Os endereços do campo Cco são visíveis aos demais destinatários" → ERRADO (Microsoft, documentação de suporte, "Mostre, oculte e exiba o campo Cco (cópia oculta) no Outlook para Windows").
- [P1-3] **CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL)** — "O IMAP4 baixa as mensagens para uma única pasta do cliente e não sincroniza várias pastas" → ERRADO (essa limitação é do POP3; Microsoft Learn, "POP3 e IMAP4 em Exchange Online").
- [P1-3] **MICROSOFT TEAMS** — "No Teams, o canal privado é aberto a todos os membros da equipe e o canal padrão é restrito a membros selecionados" → ERRADO (inverso; Microsoft Learn, "Visão geral de equipes e canais no Microsoft Teams").
- [P1-3] **MICROSOFT TEAMS** — "O canal compartilhado só pode ter membros da própria equipe" → ERRADO (inclui pessoas dentro e fora da equipe; Microsoft Learn, "Visão geral de equipes e canais no Microsoft Teams").
- [P1-3] **MICROSOFT TEAMS** — "Equipe e canal são sinônimos" → ERRADO (o canal é uma seção dentro da equipe; Microsoft Learn, "Visão geral de equipes e canais no Microsoft Teams").
- [P1-3] **GOOGLE MEET** — "Ao apresentar no Meet, só é possível compartilhar a tela inteira" → ERRADO (guia, janela ou tela inteira; Ajuda do Google Meet, "Apresentar durante uma videochamada - Computador").
- [P1-3] **GOOGLE MEET** — "Teams e Meet são produtos da mesma empresa" → ERRADO (Microsoft × Google; conceito geral).
- [P1-3] **GOOGLE MEET** — "O link de uma reunião do Meet só pode ser criado por meio de um evento do Google Agenda" → ERRADO (também se cria em "Nova reunião", no próprio Meet; Ajuda do Google Meet, "Inicie ou agende uma videoconferência do Google Meet").
- [P1-3] **GOOGLE MEET** — "O compartilhamento de tela no Meet nunca pode ser restringido" → ERRADO (pode ser desativado por administrador ou limitado pelo organizador; Ajuda do Google Meet, "Apresentar durante uma videochamada - Computador").
- [P1-3] **CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL)** — Não confunda SMTP com POP3: o SMTP transfere e envia as mensagens; o POP3 permite à estação acessar a caixa postal no servidor, em geral baixando as mensagens. Armadilha: o POP3 não envia; o programa de e-mail depende do SMTP para enviar.
- [P1-3] **CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL)** — Não confunda POP3 com IMAP4: por padrão, os clientes POP3 removem as mensagens baixadas do servidor, baixam para uma única pasta e não sincronizam várias pastas; os clientes IMAP4 não as removem por padrão e dão suporte a várias pastas (Microsoft Learn, "POP3 e IMAP4 em Exchange Online").
- [P1-3] **CORREIO ELETRÔNICO (WEBMAIL, CLIENTE DE E-MAIL)** — Não confunda Para e Cc com Cco: em Para (destinatários principais) e em Cc (ciência), os endereços aparecem para todos; quem está em Cco recebe a cópia, mas seu endereço fica oculto para os demais. Armadilha: dizer que o destinatário em Cco não recebe a mensagem.
- [P1-3] **MICROSOFT TEAMS** — Não confunda equipe com canal no Teams: a equipe é a coleção de pessoas, conteúdo e ferramentas dos projetos e resultados de uma organização; o canal é uma seção dedicada dentro da equipe, que organiza as conversas por tópicos ou projetos.
- [P1-3] **GOOGLE MEET** — Não confunda apresentar uma guia com apresentar uma janela ou a tela inteira no Meet: a guia é uma aba do Chrome, com áudio compartilhado por padrão; na janela ou na tela inteira, o áudio do sistema só é compartilhado se a opção for ativada (Ajuda do Google Meet, verificado em 08/10/2026).

## Tópico P1-1 — MSOffice 365 (Word, Excel, PowerPoint e OneDrive)

### Resumo do tópico

O edital escreve MSOffice 365; segundo a documentação de suporte da Microsoft, lida em 08/10/2026, Word, Excel, PowerPoint e Outlook são aplicativos do pacote Microsoft 365. Importa o que cada aplicativo faz, e não plano, licença ou preço. Word trata texto, Excel calcula, PowerPoint apresenta e OneDrive guarda arquivos na nuvem.

No Word, o controle de alterações registra as edições sem apagar o texto original. O modo Sem Marcação só oculta as marcas, que voltam ao reabrir o documento. Aceitar incorpora a alteração, rejeitar restabelece o texto original, e Avançar e Anterior só navegam.

Mesclar combina células adjacentes em uma; dividir subdivide uma célula em várias. O sumário automático é gerado a partir dos estilos de título e, após mudanças, atualiza-se com Atualizar Campo.

No Excel, a referência é relativa por padrão e muda quando a fórmula é copiada. O cifrão trava o que vem logo depois: $B$2 fixa coluna e linha, $B2 só a coluna e B$2 só a linha. A tecla F4 alterna entre os tipos.

A função SE tem teste lógico, valor se verdadeiro e valor se falso, este opcional. O PROCV pesquisa da esquerda para a direita; no quarto argumento, FALSO dá correspondência exata, e VERDADEIRO ou em branco dá aproximada.

No PowerPoint, alterar o slide mestre, aberto na guia Exibir, muda de uma vez os slides baseados nele. A animação age num elemento do slide; a transição age no slide inteiro, uma só por slide.

O OneDrive guarda arquivos na nuvem, com permissões de exibição, que é ler, ou de edição, que é ler e alterar. Restaurar uma versão não apaga a atual, que passa a constar como anterior.

## Tópico P1-3 — Ferramentas de comunicação e colaboração: correio eletrônico (webmail, cliente de e-mail), aplicativos de comunicação (Microsoft Teams, Google Meet)

### Resumo do tópico

No correio eletrônico, o webmail é acessado pelo navegador, sem programa instalado, e o cliente de e-mail é um programa próprio que acessa a caixa postal no servidor.

O SMTP envia; o POP3 baixa e, por padrão, apaga do servidor; o IMAP4 acessa e sincroniza, mantendo as mensagens no servidor e dando suporte a várias pastas.

Segundo a documentação de suporte da Microsoft, lida em 08/10/2026, quem está em Cco recebe a mensagem, mas seu endereço não é visto pelos outros destinatários. Em Para e Cc, os endereços aparecem para todos.

O Microsoft Teams é a plataforma de comunicação e colaboração da Microsoft. Segundo o Microsoft Learn, lido em 08/10/2026, a equipe reúne pessoas, conteúdo e ferramentas, e o canal é uma seção dentro dela que organiza as conversas por assunto.

Os canais padrão são abertos a todos os membros, os privados a membros selecionados e os compartilhados a pessoas de dentro e de fora da equipe.

O Google Meet é o serviço de videoconferência do Google, produto distinto do Teams, que é da Microsoft. A reunião pode ser iniciada em Nova reunião ou agendada pelo evento do Google Agenda, e acessada pelo link.

Ao apresentar, escolhe-se guia, janela ou tela inteira; o compartilhamento pode ser desativado pelo administrador ou limitado pelo organizador.
