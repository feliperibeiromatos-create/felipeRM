PARECER DE QA — LOTE 6b v1 — RODADA 1 — QA automatizado (Opus) — 08/10/2026

REMETENTE: Coordenação de QA, Fontes e Proveniência (independente; não produziu o lote)
DESTINATÁRIO: PRES-S (Presidência interina), para devolução à Coordenação de Produção (TI e Dados)
Base: /home/claude/lotes/Lote6b_v1.md (392 linhas, íntegro; termina em "FIM DO LOTE 6b"), conferido contra /home/claude/lotes/ESPEC_Lotes6.md (lida inteira). Rodada 1 de no máximo 2. O lote não foi alterado.

Ressalva de método (vale para todas as citações deste parecer): as páginas foram abertas pela ferramenta WebFetch em 08/10/2026. A ferramenta devolve citações literais curtas (limite de cerca de 125 caracteres) e, nos PDFs da Cartilha, a extração perde acentos, que a ferramenta restaurou. Onde só obtive paráfrase, escrevo "paráfrase". O download direto por curl foi bloqueado pelo proxy (403), o que não afetou a leitura pelo WebFetch.

==================================================
1. CHECAGENS FORMAIS
==================================================
- Marcadores "FIM DA PARTE 1/3", "FIM DA PARTE 2/3", "FIM DA PARTE 3/3" e "FIM DO LOTE 6b": CONFEREM.
- Cabeçalho (título, escopo literal, dados da P1, TABELA DE CORREÇÕES vazia, FONTES com URL e data): CONFERE.
- 15 itens AUTORAL (6B-01 a 6B-15): CONFERE.
- Item 2 = 5 (6B-01 no 2; 6B-02 a 6B-05 no 2.1): CONFERE.
- Item 4 = 10, com 4.1 = 4 (06 a 09), 4.2 = 3 (10 a 12) e 4.3 = 3 (13 a 15), ou seja, no mínimo 2 em cada: CONFERE.
- Gabarito: 7 C (02, 04, 05, 08, 11, 14, 15) e 8 E (01, 03, 06, 07, 09, 10, 12, 13), dentro da faixa de 6 a 9 C: CONFERE.
- 8 [TS] (02, 03, 06, 07, 10, 13, 14, 15), sendo 3 C (02, 14, 15) e 5 E (03, 06, 07, 10, 13): CONFERE com a linha "Contagem".
- 0 VOLÁTIL: CONFERE. Nenhum item cobra produto, menu, versão, preço, licença ou limite.
- Nenhum item atribui afirmação a autor, banca ou fornecedor: CONFERE. Atribuições ("segundo a Cartilha") só aparecem no curso, o que é permitido.
- Frases de comando "Acerca de ..., julgue os itens ...": CONFEREM.
- Pares confundíveis: 18 (mínimo 12). CONFERE.
- Seção de ITENS REAIS fora dos 15, com a nota exigida pela especificação: CONFERE. O preenchimento está na seção 4 deste parecer.
- Observação sem ação: nos C de ancoragem (04, 05, 08, 11), o d-G registra "sem armadilha (ancoragem)" em vez de um mecanismo da lista TC/GI/AT/IC. A especificação descreve mecanismos de erro, e a prática é aceitável.
- Governança digital sem item: está dentro da especificação ("se houver base"). Avaliação na seção 5.

==================================================
2. ITEM A ITEM
==================================================
6B-01 E — OK. Inversão LAN × WAN. E robusto. Item fácil, mas legítimo como âncora do item 2.
6B-02 C [TS] — OK. "Pode empregar ... e ainda assim ter o acesso limitado" não tem leitura que vire E. O [TS] funciona (a tentação "usa protocolos da Internet, logo é pública").
6B-03 E [TS] — OK. Intranet e extranet trocadas. E robusto.
6B-04 C — OK. O DNS associa nomes a endereços IP. O fato de o DNS ter outros registros não torna a afirmação incorreta.
6B-05 C — OK. "Em geral por meio do protocolo HTTP" abrange o HTTPS (HTTP sobre TLS). Sem risco relevante.
6B-06 E [TS] — OK. Integridade e disponibilidade trocadas. E robusto. É o mesmo tema dos itens reais 96 e 98, mas com outro ponto de julgamento (troca das definições, não o conteúdo de cada uma).
6B-07 E [TS] — FALHA GRAVE: existe leitura razoável, com documento oficial de fornecedor, que inverte o gabarito. O item afirma que o diferencial copia "desde o último backup de qualquer tipo, seja ele completo, seja incremental". A documentação da Microsoft (Microsoft Learn, "Types of backup", conteúdo arquivado do Windows Server 2003, aberta hoje) diz literalmente: "A differential backup copies files that have been created or changed since the last normal or incremental backup." A cláusula "seja ele completo, seja incremental" reproduz essa definição, e um candidato que a conheça marcará C. Ver O-1.
6B-08 C — OK. Reproduz a definição literal do F2, reconfirmada hoje: "Ransomware é um tipo de código malicioso que torna inacessíveis os dados armazenados em um equipamento,". A segunda oração ("contribui para reduzir o impacto") é prudente. O item é composto, mas as duas partes são verdadeiras e ancoradas.
6B-09 E — OK. Vírus e worm trocados. E robusto e agora ancorado em fonte aberta. O fascículo Códigos Maliciosos define o worm assim: "Propaga-se automaticamente pelas redes, explorando vulnerabilidades nos sistemas e aplicativos instalados". O livro (seção 4.1, paráfrase) diz que o vírus depende da execução do programa ou arquivo hospedeiro. Nuance de curso na R-2.
6B-10 E [TS] — OK. Firewall e antivírus trocados. Ancorado no F5 (reconfirmado hoje) e no fascículo Computadores: "Ele bloqueia conexões não autorizadas de entrada para programas e serviços executando em seu computador." e "Ferramentas antivírus (antimalware) podem ajudar a detectar uma infecção, preveni-la e/ou remover malware do computador."
6B-11 C — OK. A definição de spyware do item é quase literal à do fascículo Códigos Maliciosos: "Projetado para monitorar as atividades de um sistema e enviar as informações coletadas para terceiros." O antispyware não foi encontrado nas fontes abertas hoje (os fascículos falam em "antimalware"), e a definição do item, por ser descritiva e não restritiva ("voltado a detectar e remover"), fica como conceito geral seguro. Item composto com as duas partes verdadeiras: risco baixo.
6B-12 E — OK quanto ao gabarito. Porém julga dois pontos ("todos os códigos, inclusive desconhecidos" e "dispensáveis o firewall e as demais medidas"), ambos falsos, e o "todos" torna o item trivial. Ver R-3.
6B-13 E [TS] — gabarito correto, mas REPETE O PONTO DE JULGAMENTO do 6B-14. Os dois julgam o mesmo fato (o pharming redireciona por alteração da resolução de nomes, sem depender de link) em formas espelhadas: quem acerta um acerta o outro, e quem erra perde 2 pontos pelo mesmo desconhecimento. Além disso, o PHISHING, nomeado no edital 4.3, fica sem item próprio. Ver O-2.
6B-14 C [TS] — OK, e agora ANCORADO. O livro da Cartilha (seção 2.3.1), aberto hoje, define o pharming como tipo específico de phishing que redireciona a navegação para sites falsos "por meio de alterações no serviço de DNS (Domain Name System)". A paráfrase obtida acrescenta que, ao tentar acessar um site legítimo, o navegador é levado de forma transparente à página falsa, e que isso pode ocorrer por comprometimento do servidor DNS do provedor, por código malicioso que altera o DNS do computador ou por invasor com acesso às configurações de DNS do computador ou do modem. A dúvida (iii) da nota de produção fica resolvida: a ligação pharming–DNS tem fonte aberta hoje. O arquivo hosts, citado no curso, não aparece na Cartilha e permanece como conceito geral, sem prejuízo, porque o item só usa "como a adulteração de um servidor DNS".
6B-15 C [TS] — OK quanto ao gabarito. Risco residual: o HTTPS AUTENTICA o servidor para o domínio acessado (RFC 9110, seção 4.2.2), e um recurso poderia explorar "legítimo" nesse sentido técnico. A oração causal ("páginas fraudulentas também podem utilizar HTTPS") sustenta o C. O problema maior está no curso que fundamenta o item (O-3). Ajuste de redação na R-4.

==================================================
3. FONTES — CONFERÊNCIA (08/10/2026)
==================================================
ABERTAS PELO QA E USADAS NESTE PARECER
Q1 — CERT.br, Cartilha (livro, PDF), https://cartilha.cert.br/livro/cartilha-seguranca-internet.pdf — aberta. O WebFetch entrega cerca de 79.561 caracteres e para no início da seção 4.1. Lidos: 2.3 (phishing; paráfrase dos meios: páginas falsas, instalação de códigos maliciosos, formulários), 2.3.1 (pharming e DNS: trecho literal acima; prevenção, em paráfrase: desconfiar de site de comércio ou banco sem conexão segura e verificar se o certificado apresentado corresponde ao do site verdadeiro) e 4.1 (vírus, dependência do hospedeiro). NÃO alcançados pela ferramenta: 4.2 em diante (worm, bot, spyware etc.), 7.5 (backup), 7.7 (antimalware), 7.8 (firewall pessoal) e 10.1 (conexão segura). A tríade CIA não é definida no trecho alcançado, o que confirma o registro do produtor.
Q2 — CERT.br, fascículo "Códigos Maliciosos", https://cartilha.cert.br/fasciculos/codigos-maliciosos/fasciculo-codigos-maliciosos.pdf — aberto. Vírus: "Torna-se parte de programas e arquivos. Propaga-se enviando cópias de si mesmo por e-mails e mensagens." Worm: "Propaga-se automaticamente pelas redes, explorando vulnerabilidades nos sistemas e aplicativos instalados". Spyware: "Projetado para monitorar as atividades de um sistema e enviar as informações coletadas para terceiros." Antivírus: "Antivírus é nome popular para ferramentas antimalware, que atuam sobre diversos tipos de códigos maliciosos". Antispyware: não mencionado.
Q3 — CERT.br, fascículo "Computadores", https://cartilha.cert.br/fasciculos/computadores/fasciculo-computadores.pdf — aberto. Firewall: "O firewall protege seu computador contra ataques vindos pela rede." e "Ele bloqueia conexões não autorizadas de entrada para programas e serviços executando em seu computador." Antivírus: "Ferramentas antivírus (antimalware) podem ajudar a detectar uma infecção, preveni-la e/ou remover malware do computador."
Q4 — CERT.br, fascículo "Golpes: Evite Fraudes", https://cartilha.cert.br/fasciculos/golpes-evite-fraudes/fasciculo-golpes-evite-fraudes.pdf — aberto. Phishing: "Phishing é um tipo de fraude na qual golpistas tentam obter informações pessoais e financeiras," "combinando engenharia social com recursos técnicos." Não trata de pharming nem de DNS.
Q5 — CERT.br, fascículo "Backup", https://cartilha.cert.br/fasciculos/backup/fasciculo-backup.pdf — aberto. Não define completo, incremental ou diferencial. Traz "Armazene as cópias em locais diferentes" e orienta acessar os backups de tempos em tempos, para evitar surpresas como arquivos corrompidos (paráfrase). Não distingue sincronização de backup: a distinção do curso 4.1.2 é conceito geral (sem ação).
Q6 — Microsoft Learn, "Types of backup" (Windows Server 2003, conteúdo arquivado), https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc784306(v=ws.10) — aberta. Diferencial: "A differential backup copies files that have been created or changed since the last normal or incremental backup. It does not mark files as having been backed up". Restauração: "If you are performing a combination of normal and differential backups, restoring files and folders requires that you have the last normal as well as the last differential backup." Incremental: "An incremental backup backs up only those files that have been created or changed since the last normal or incremental backup. It marks files as having been backed up".
Q7 — IETF, RFC 9110, seção 4.2.2 ("https" URI scheme), https://www.rfc-editor.org/rfc/rfc9110.html — aberta. "Secured" significa que "the server has been authenticated as acting on behalf of the identified authority" e que "all HTTP communication with that server has confidentiality and integrity protection".

FONTES DO LOTE RECONFERIDAS
F1 (página inicial da Cartilha) — aberta. Não há página de malware, golpes ou mecanismos no menu atual. Os links que falharam para o produtor (/malware/, /golpes/, /mecanismos/) não existem mais na navegação do site, e o conteúdo equivalente está nos fascículos (Q2 a Q5).
F2 (ransomware) — CONFERE. A definição e a frase "Fazer backups regularmente também é essencial para proteger os seus dados" aparecem literalmente.
F3 (dicas rápidas) — CONFERE. As três frases aparecem literalmente: "Faça backups periódicos." em duas seções; "Instale um antivírus antes de qualquer aplicativo." em Celulares; "Use mecanismos de segurança, como antivírus e firewall pessoal." em Computadores.
F4 (livro) — CONFERE quanto a 2.3, 2.3.1 e 4.1. A afirmação do F4 de que "o trecho sobre o DNS não foi confirmado" está superada: o trecho existe (Q1). Ver R-1.
F5 (Firewall do Windows) — CONFERE, frase literal idêntica.
F6, F7, F8, F9 e F10 (RFCs 1918, 1034, 5321, 3501 e 1939) — não reabertas pelo QA. Não sustentam o gabarito de nenhum item (6B-04 é conceito geral; o F7 só ilustra).
F11 (RFC 9110) — aberta. O trecho da seção 4.2.2 (Q7) contradiz o curso 4.3.4 (O-3).
Página da Microsoft sobre phishing descartada pelo produtor: descarte correto (sem ação).
Nenhuma URL ou citação inventada foi encontrada no lote.

Avaliação do pedido especial (pharming–DNS, itens 6B-13 e 6B-14): a ligação está ANCORADA em fonte aberta hoje (Q1, seção 2.3.1). O 6B-14 se sustenta pela fonte, não só como conceito geral. O problema do 6B-13 não é de fonte: é a repetição do ponto (O-2).

==================================================
4. ITENS REAIS TRF6 2024 (CEBRASPE_ANALOGA) — PREENCHIMENTO
==================================================
Caderno oficial https://cdn.cebraspe.org.br/concursos/trf6_24/arquivos/034_TRF6_002_01.PDF — ABERTO pelo WebFetch em 08/10/2026. Os itens 96 e 98 estão no bloco "Julgue os itens a seguir, a respeito da segurança da informação e dos vários tipos de ataques e suas características." (itens 96 a 99), na parte de CONHECIMENTOS ESPECÍFICOS (itens 51 a 120).
Gabarito definitivo — ABERTO pelo Projects (GAB_DEFINITIVO_034_TRF6_002_01.pdf): "CARGO 2: ANALISTA JUDICIÁRIO – ÁREA: APOIO ESPECIALIZADO – ESPECIALIDADE: ANÁLISE DE DADOS", aplicação em 19/01/2025. Leitura da linha dos itens 91 a 110: 96 = E e 98 = C. CONFEREM com a especificação. Itens anulados no caderno: 58, 105 e 117. Nenhum deles é o 96 ou o 98, o que também coincide com GCE_ItensReais_P9_GCE.md.

| item | gabarito definitivo | ponto de julgamento (uma linha) | subitem do edital 14.2.3 | aderência |
| 96 | E | atribui à integridade a garantia de que dado ou informação TENHAM SIDO ALTERADOS sem registro da ação, mesmo sob necessidade de auditoria — inversão do conceito (integridade = proteção contra alteração não autorizada) | 4 / 4.1 (segurança da informação; tríade como conceito geral) | parcial |
| 98 | C | disponibilidade como garantia de acesso dos usuários a sistemas e(ou) informações quando necessário, inclusive com o sistema ou a infraestrutura sob pressão | 4 / 4.1 (idem) | parcial |

Motivo do "parcial": o edital 4/4.1 não nomeia a tríade; os itens são de Conhecimentos Específicos de cargo de Análise de Dados (nível mais técnico que o P1 do Cargo 11); e o 96 combina integridade com registro e auditoria (rastreabilidade).
Controle de leitura: a ausência de "não" no item 96 foi conferida em consulta dirigida. As oito palavras finais são "da ação correspondente, mesmo sob necessidade de auditoria.", e as 12 palavras após "garante que" são "um dado ou uma informação tenham sido alterados sem o registro da". O item 98 termina em "quando necessário, mesmo que o sistema ou a infraestrutura esteja sob pressão." Os textos não são transcritos integralmente, conforme a regra. Recomenda-se uma conferência visual do PDF por leitor humano quando o item for usado em simulado (BACKLOG), porque a leitura foi mediada por ferramenta.
Redação substitutiva para a tabela do lote (coluna "texto e ponto de julgamento"):
- 96: "ponto de julgamento: integridade descrita como garantia de que dado/informação tenham sido alterados sem registro da ação, mesmo sob necessidade de auditoria (inversão do conceito) — conferido pela QA contra o caderno oficial em 08/10/2026; texto não transcrito".
- 98: "ponto de julgamento: disponibilidade como acesso dos usuários a sistemas e(ou) informações quando necessário, mesmo com sistema ou infraestrutura sob pressão — conferido pela QA contra o caderno oficial em 08/10/2026; texto não transcrito".
Cargo: acrescentar "(Analista Judiciário – Apoio Especializado – Análise de Dados; Conhecimentos Específicos)".

==================================================
5. CURSO E RESUMO
==================================================
- 4.3.4 e 4.3.5 (HTTPS e cadeado): ERRO CONCEITUAL. O curso diz que o HTTPS "NÃO garante que o servidor pertença a quem diz pertencer" e, no exemplo de pharming, que "o cadeado pode até aparecer, se o site falso usar HTTPS". As duas afirmações contrariam a RFC 9110, 4.2.2 (Q7): com HTTPS, o servidor é autenticado como agindo em nome da autoridade identificada, isto é, o domínio. Se o usuário digitou o domínio verdadeiro (cenário de pharming), o servidor falso, em regra, não tem certificado válido para esse domínio, e o navegador alerta. A própria Cartilha orienta verificar se o certificado corresponde ao do site verdadeiro (Q1, 2.3.1, paráfrase). O curso levaria a candidata a marcar E num item verdadeiro do tipo "o HTTPS permite autenticar o servidor por meio de certificado digital". → O-3.
- 4.1.2 (tipos de backup) e o par C9, a pegadinha P3 e o resumo 4.1: o curso ensina como regra absoluta "diferencial = desde o último completo" e "desde o último de qualquer tipo = incremental". A documentação oficial da Microsoft (Q6) diz "since the last normal or incremental backup" para AMBOS e distingue os dois pela marcação do arquivo. Pela tabela do curso, a candidata erraria um item que reproduzisse a definição da Microsoft. → O-1 (junto com o 6B-07).
- 4.1.4 (vírus): "não se propaga sozinho pela rede" está correto no essencial, mas o fascículo (Q2) diz que o vírus "Propaga-se enviando cópias de si mesmo por e-mails e mensagens". Convém dizer que o vírus pode circular pela rede (e-mail, mensagens), mas cada infecção depende da execução do hospedeiro. → R-2.
- 4.3.1 (phishing): correto. Falta dizer que o golpe pode coletar dados também por formulário na própria mensagem e pela instalação de código malicioso (Q1, 2.3). O acréscimo é necessário para sustentar o novo 6B-13. → incluído na O-2.
- 4.0.2 (governança digital): o curso dá um conceito geral suficiente e honesto ("políticas, responsabilidades, processos e controles ... quem decide, quem responde, quais regras valem") e declara a ausência de fonte. A falta de item está conforme a especificação. Não procurei base normativa: a Lei 14.129/2021 é matéria do QA Normativo. → R-5 (BACKLOG).
- Demais conteúdos conferidos sem erro relevante: LAN/WAN, cliente-servidor, switch × roteador, IPv4/IPv6, faixas da RFC 1918 (não reabertas), DNS × DHCP, TCP × UDP, Internet × Web × intranet × extranet, navegação privada, tríade CIA, ransomware, trojan, spyware/adware, bot, antivírus, firewall, quarentena, pharming (agora ancorado). Não encontrei afirmação sem base apresentada como fato, além das já sinalizadas como "conceito geral".
- Resumo: a NOTA 8.11.2 é idêntica à dos lotes canônicos anteriores (sem ação). Os trechos de backup e HTTPS mudam pelas O-1 e O-3.

==================================================
6. CORREÇÕES OBRIGATÓRIAS (O)
==================================================
O-1 — 6B-07 (gabarito com leitura que se inverte) e base de backup no curso
(a) Versão do estudante, substituir o 6B-07 por:
"6B-07. Em uma rotina com backup completo aos domingos e backups diferenciais nos demais dias da semana, a recuperação dos dados tal como estavam no backup de quarta-feira exige o backup completo de domingo e todos os backups diferenciais realizados de segunda a quarta-feira."
(b) d-G, substituir por:
"6B-07. E — [TS] — 4.1 — TC (lógica de restauração do incremental atribuída ao diferencial). Curso 4.1.2: numa rotina de completo + diferenciais, cada diferencial acumula tudo o que mudou desde o completo; a restauração exige o último completo e apenas o último diferencial (o de quarta-feira). Fonte: F12 (Microsoft Learn, 'Types of backup', verificado em 08/10/2026): 'If you are performing a combination of normal and differential backups, restoring files and folders requires that you have the last normal as well as the last differential backup.' O item não depende da divergência de definição registrada no curso 4.1.2."
(c) Curso 4.1.2: substituir os tópicos INCREMENTAL e DIFERENCIAL e a "Chave de prova" por:
"- INCREMENTAL: copia SOMENTE o que mudou desde o último backup completo ou incremental e marca os arquivos como copiados. Backup rápido e pequeno; a restauração exige o último completo MAIS todos os incrementais até o ponto desejado, na ordem.
- DIFERENCIAL: NÃO marca os arquivos como copiados; por isso, numa rotina de completo + diferenciais, cada diferencial acumula tudo o que mudou desde o último completo e cresce até o próximo completo. A restauração exige o último completo MAIS o último diferencial.
Chave de prova: a diferença segura está na marcação e na restauração. O incremental 'zera' o controle de alterações (cada um guarda só o que mudou desde o anterior; restaura-se com o completo + todos os incrementais). O diferencial não 'zera' (acumula desde o completo; restaura-se com o completo + o último diferencial). ATENÇÃO: o material de concurso costuma resumir o diferencial como 'desde o último completo', mas a documentação da Microsoft define o diferencial como cópia do que mudou 'since the last normal or incremental backup' (F12). Portanto, afirmação de que o diferencial copia o que mudou desde o último completo ou incremental NÃO é erro seguro."
(d) Curso 4.1.6, substituir a P3 por:
"P3. 'Numa rotina de completo + diferenciais, a restauração exige o completo e todos os diferenciais posteriores' → ERRADO (basta o completo e o último diferencial)."
(e) Par C9, substituir por:
"C9. Backup completo × incremental × diferencial | copia tudo | copia o que mudou desde o último completo ou incremental e marca os arquivos; restaura com o completo + todos os incrementais | não marca os arquivos; numa rotina de completo + diferenciais, acumula o que mudou desde o completo; restaura com o completo + o último diferencial | Troca: atribuir ao diferencial a restauração em cadeia do incremental, ou ao incremental o acúmulo do diferencial. Cuidado: 'diferencial = desde o último completo ou incremental' é a definição da Microsoft (F12), não erro."
(f) Resumo 4.1, substituir o trecho "BACKUP: completo (tudo); incremental (...); diferencial (...)" por:
"BACKUP: completo (tudo); incremental (mudou desde o último completo ou incremental; marca os arquivos; restaura com completo + todos os incrementais); diferencial (não marca; numa rotina completo + diferenciais, acumula desde o completo; restaura com completo + último diferencial). 'Desde o último completo ou incremental' também aparece como definição do diferencial (Microsoft, F12): não é erro seguro."
(g) FONTES, acrescentar: "F12 — Microsoft Learn, 'Types of backup' (Windows Server 2003, conteúdo arquivado), https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc784306(v=ws.10) — aberta em 08/10/2026 (pelo QA; a produção deve reabrir e confirmar). Usada só como apoio conceitual; não torna o item VOLÁTIL."
Contagens: inalteradas (6B-07 continua E, [TS], 4.1).

O-2 — 6B-13 (repetição do ponto de julgamento do 6B-14; phishing sem item)
(a) Versão do estudante, substituir o 6B-13 por:
"6B-13. No phishing, o golpista envia mensagem que imita a comunicação de instituição conhecida para obter dados pessoais e financeiros da vítima; nesse golpe, a obtenção dos dados depende de a vítima digitá-los em página falsa, uma vez que o phishing não envolve a instalação de código malicioso no equipamento."
(b) d-G, substituir por:
"6B-13. E — [TS] — 4.3 — GI (restrição indevida dos meios do phishing). Curso 4.3.1: o phishing induz a vítima a clicar em link para página falsa, a abrir anexo malicioso ou a preencher dados; a coleta pode ocorrer por página falsa, por formulário na própria mensagem ou pela instalação de código malicioso. A primeira oração é correta (isca que imita instituição conhecida); o erro está em restringir o golpe à página falsa e negar o código malicioso. Fonte: F4 (livro, seção 2.3, verificado em 08/10/2026; paráfrase: as mensagens induzem o usuário a fornecer dados por páginas falsas, pela instalação de códigos maliciosos ou pelo preenchimento de formulários; entre as situações, 'mensagens com links para código malicioso')."
(c) Curso 4.3.1, acrescentar após "...digitar senha e dados.":
"A coleta pode ocorrer por página falsa, por formulário na própria mensagem ou pela instalação de código malicioso a partir de link ou anexo (F4, seção 2.3, paráfrase)."
(d) Curso 4.3.6, acrescentar:
"P8. 'O phishing só funciona quando a vítima digita dados em página falsa; não envolve instalação de código malicioso' → ERRADO."
(e) Contagem: na linha "Distribuição" e na Nota de produção, registrar 4.3: 6B-13 (phishing), 6B-14 (pharming), 6B-15 (HTTPS).
Contagens: inalteradas (6B-13 continua E, [TS], 4.3). O 6B-14 fica como está.

O-3 — Curso 4.3.4, 4.3.5, 2.0.6, par C17 e resumo 4.3 (erro conceitual sobre HTTPS)
(a) Curso 4.3.4, substituir o corpo por:
"HTTPS é o HTTP sobre conexão protegida por TLS. Com o certificado digital do site, o navegador autentica o servidor como responsável pelo DOMÍNIO acessado, e a comunicação ganha confidencialidade e integridade (F11, RFC 9110, seção 4.2.2: 'secured' significa que 'the server has been authenticated as acting on behalf of the identified authority' e que a comunicação tem 'confidentiality and integrity protection'; verificado em 08/10/2026). O que o HTTPS NÃO garante: que o domínio seja o da instituição que o usuário pretendia acessar, nem que o titular do site aja de boa-fé. Um golpista pode registrar domínio parecido (com letras trocadas) e obter certificado válido para ESSE domínio, e o cadeado aparecerá. Logo, 'tem https/cadeado, então é o site verdadeiro' é pegadinha frequente, e 'o HTTPS não oferece autenticação alguma' também é erro. Conferir o domínio completo (letra a letra), não ignorar alertas de certificado do navegador e conferir o canal pelo qual o link chegou."
(b) Curso 4.3.4, substituir a linha "Fonte: conceito geral. O F11 descreve o HTTP; ..." por: "Fonte: F11 (seção 4.2.2), verificado em 08/10/2026; o restante é conceito geral."
(c) Curso 4.3.5, no exemplo de PHARMING, substituir "o cadeado pode até aparecer, se o site falso usar HTTPS. Lição: o ataque não depende de link recebido, e o HTTPS não prova a legitimidade." por:
"como ele digitou o domínio verdadeiro, o servidor falso, em regra, não consegue apresentar certificado válido para esse domínio: o navegador tende a exibir alerta de certificado, ou a página aparece sem conexão segura. São sinais que não podem ser ignorados (F4, seção 2.3.1, paráfrase: desconfiar de site de banco ou comércio sem conexão segura e verificar se o certificado apresentado corresponde ao do site verdadeiro). Lição: o ataque não depende de link recebido; o cadeado comprova o domínio, não a boa-fé de quem o registrou."
(d) Curso 2.0.6, substituir a frase do HTTPS por:
"HTTPS = HTTP sobre conexão TLS: autentica o servidor para o domínio acessado (certificado digital) e protege o conteúdo contra leitura e alteração no caminho (ver 4.3.4)."
(e) Par C17, substituir por:
"C17. HTTPS × legitimidade do site | conexão cifrada, com o servidor autenticado para o domínio acessado (certificado) | o domínio ser o da instituição pretendida e o titular agir de boa-fé | Troca: 'HTTPS ou cadeado prova que o site é o verdadeiro' (errado) ou 'HTTPS não oferece autenticação alguma' (errado)."
(f) Resumo 4.3, substituir "HTTPS = comunicação cifrada, NÃO prova legitimidade do site." por:
"HTTPS = comunicação cifrada e servidor autenticado para o domínio acessado; NÃO prova que o domínio é o legítimo nem a boa-fé do site."
Contagens: inalteradas. Item 6B-15: gabarito C mantido (ver R-4).

==================================================
7. RECOMENDADAS (R) — não condicionam a aprovação
==================================================
R-1 — Fontes e notas superadas. (a) Corrigir no F4, no curso 4.3.2, no d-G do 6B-14 e na Nota de produção (iii) a afirmação de que o trecho sobre DNS "não foi confirmado". Redação para o F4: "...seção 2.3.1 define o pharming como tipo específico de phishing que redireciona a navegação para sites falsos 'por meio de alterações no serviço de DNS (Domain Name System)' (trecho confirmado pela QA em 08/10/2026)". No d-G do 6B-14, trocar "detalhe do DNS é conceito geral" por "F4, seção 2.3.1 (DNS confirmado); arquivo hosts: conceito geral". (b) Acrescentar ao bloco FONTES os fascículos Q2 (Códigos Maliciosos), Q3 (Computadores) e Q4 (Golpes: Evite Fraudes), com as URLs da seção 3, e citá-los nos d-G dos itens 6B-09 (worm), 6B-10 (firewall e antivírus) e 6B-11 (spyware), no lugar de "conceito geral". Pela regra "citação literal só do que você leu hoje", a produção reabre as páginas ou registra "verificado pela QA em 08/10/2026". (c) Atualizar o rodapé NÃO ABERTAS: as URLs /malware/, /golpes/ e /mecanismos/ não constam mais da navegação atual; o conteúdo equivalente está em https://cartilha.cert.br/fasciculos/. Contagens: inalteradas.
R-2 — Curso 4.1.4, linha VÍRUS, coluna "Característica de prova": substituir "depende de hospedeiro e de execução; não se propaga sozinho pela rede" por "depende de hospedeiro e de execução; pode circular por e-mails e mensagens, mas cada infecção depende de o hospedeiro ser executado; não explora sozinho vulnerabilidades da rede, como o worm". Base: Q2 ("Propaga-se enviando cópias de si mesmo por e-mails e mensagens."). Ajustar igualmente o par C11 ("precisa de hospedeiro e de execução; pode circular por e-mail, mas não se autoexecuta | independente; propaga-se automaticamente pelas redes, explorando vulnerabilidades"). Contagens: inalteradas.
R-3 — 6B-12, para julgar um único ponto: "6B-12. Mantido atualizado, o antivírus é capaz de identificar todos os códigos maliciosos, inclusive os ainda desconhecidos." Gabarito E, GI e 4.2 mantidos. No d-G, retirar a remissão ao firewall e ao F3 ou mantê-la só como complemento. Contagens: inalteradas.
R-4 — 6B-15, para afastar o argumento técnico "o HTTPS autentica o servidor": "6B-15. A utilização do protocolo HTTPS indica que a comunicação entre o navegador e o site é cifrada, mas, por si só, não garante que o site pertença à instituição que o usuário pretende acessar, pois páginas fraudulentas, hospedadas em domínios próprios, também podem utilizar HTTPS." Gabarito C, [TS], 4.3 mantidos. No d-G, remeter ao curso 4.3.4 corrigido (O-3) e ao F11 (seção 4.2.2). Contagens: inalteradas.
R-5 — Governança digital: manter sem item neste lote. Em BACKLOG, pedir ao QA Normativo a ancoragem do conceito (por exemplo, na Lei 14.129/2021, se o texto vigente a sustentar) antes de qualquer item. O curso 4.0.2 é suficiente como conceito geral.
R-6 — Curso 4.1.1, acrescentar ao fim do parágrafo "Relação com os itens reais": "Os itens reais exploram (96) a integridade descrita às avessas, como garantia de que dados tenham sido alterados sem registro, mesmo sob necessidade de auditoria (E), e (98) a disponibilidade mantida mesmo com sistema ou infraestrutura sob pressão (C): disponibilidade inclui resistir a sobrecarga." Atualizar a tabela de ITENS REAIS com a redação da seção 4 deste parecer. Contagens: inalteradas.

==================================================
8. CONTAGENS APÓS AS CORREÇÕES
==================================================
Inalteradas: 15 itens; 7 C (02, 04, 05, 08, 11, 14, 15) e 8 E (01, 03, 06, 07, 09, 10, 12, 13); 8 [TS] (02, 03, 06, 07, 10, 13, 14, 15), sendo 3 C e 5 E; 0 VOLÁTIL; 2 = 1, 2.1 = 4, 4.1 = 4, 4.2 = 3, 4.3 = 3 (item 2 = 5; item 4 = 10); governança digital = 0. Na linha "Contagem", só muda o mecanismo do 6B-13 (TC → GI) e, se adotada a R-3, nada mais.

==================================================
9. CONCLUSÃO — RODADA 1: APROVADO COM RESSALVAS
==================================================
A estrutura, as contagens e 13 dos 15 itens estão aprovados como estão (o 6B-15 fica com gabarito mantido; a O-3 corrige só o curso que o fundamenta). A aprovação fica condicionada à aplicação, na v2, das O-1 (6B-07 e base de backup), O-2 (6B-13 → phishing) e O-3 (HTTPS no curso), nas redações acima. A rodada 2 desta QA será uma conferência restrita aos trechos alterados (6B-07, 6B-13, d-G correspondentes, curso 4.1.2, 4.1.6, 4.3.1, 4.3.4, 4.3.5, 4.3.6 e 2.0.6, pares C9 e C17, resumo 4.1 e 4.3, FONTES e tabela de ITENS REAIS). As R ficam a critério da produção ou da PRES-S.
Classificação: O-1, O-2 e O-3 — AGORA. R-1, R-2, R-4 e R-6 — PRÓXIMO (podem entrar na mesma v2). R-3 — PRÓXIMO (opcional). R-5 e a conferência visual humana dos itens 96 e 98 — BACKLOG.
Sugestão de paralelização (template obrigatório): RECUSADA por esta Coordenação. A v2 é uma aplicação pontual de três correções com redação pronta, e um chat novo custaria mais do que a própria correção.

FIM DO PARECER

==========================================================================
CONFERÊNCIA DE APLICAÇÃO | QA automatizado (Opus) → PRES-S | 08/10/2026 | LOTE 6b v2 (correções da rodada 1) — não conta como rodada 2
Base: /home/claude/lotes/Lote6b_v2.md (405 linhas, íntegro; termina em "FIM DO LOTE 6b"), comparado linha a linha (diff) com /home/claude/lotes/Lote6b_v1.md.

1. OBRIGATÓRIAS
- O-1 (a) 6B-07, versão do estudante: texto idêntico ao do parecer — CONFERE.
  Texto × gabarito E × d-G: o item afirma que a restauração exige o completo e TODOS os diferenciais; o curso 4.1.2, o d-G e o F12 dizem que bastam o completo e o ÚLTIMO diferencial. Logo, E. O item vale nas duas definições de diferencial (com só completo + diferenciais, não há incremental na rotina) — CONFERE. [TS] e 4.1 mantidos — CONFERE.
- O-1 (b) d-G 6B-07 — CONFERE (texto idêntico; citação do F12 igual à lida pela QA).
- O-1 (c) curso 4.1.2 (INCREMENTAL, DIFERENCIAL, Chave de prova) — CONFERE. O exemplo numérico, que não mudou, continua coerente com a nova redação.
- O-1 (d) P3 — CONFERE. (e) C9 — CONFERE. (f) resumo 4.1 — CONFERE. (g) F12 — CONFERE (três trechos idênticos aos lidos pela QA).
- O-2 (a) 6B-13, versão do estudante: texto idêntico — CONFERE. Gabarito E, [TS], 4.3; julga o phishing; não repete o 6B-14 — CONFERE.
- O-2 (b) d-G 6B-13 — CONFERE. (c) acréscimo ao curso 4.3.1 — CONFERE. (d) P8 em 4.3.6 — CONFERE. (e) distribuição 4.3 e nota de produção — CONFERE.
- O-3 (a) curso 4.3.4 — CONFERE. (b) linha de fonte do 4.3.4 — CONFERE. (c) exemplo de pharming no 4.3.5 — CONFERE. (d) 2.0.6 — CONFERE. (e) C17 — CONFERE. (f) resumo 4.3 — CONFERE. O F11 ganhou o trecho da seção 4.2.2, idêntico ao lido pela QA — CONFERE.

2. RECOMENDADAS
- R-1 — CONFERE. Notas "DNS não confirmado" retiradas do F4, do curso 4.3.2, do d-G 6B-14 e da nota de produção. F13 a F15 inseridos e citados nos d-G 6B-09, 6B-10 e 6B-11. Rodapé NÃO ABERTAS atualizado. Observação sem efeito sobre o resultado: o F4 lista como conceito geral "tríade CIA, backdoor, rootkit, bot e antispyware", mas o trojan também é conceito geral (nenhuma fonte aberta o define). O curso 4.1.3 está correto, porque diz que "as demais definições abaixo são CONCEITO GERAL". Ajuste facultativo no F4: "Tríade CIA, trojan, backdoor, rootkit, bot e antispyware ficam como CONCEITO GERAL neste lote."
- R-2 — CONFERE (linha VÍRUS do 4.1.4 e par C11 idênticos).
- R-3 — CONFERE. 6B-12 com um único ponto; E, GI, 4.2; d-G sem a remissão ao firewall e ao F3.
- R-4 — CONFERE. 6B-15 idêntico; C, [TS], 4.3; d-G remete ao 4.3.4 corrigido e ao F11 (4.2.2). Observação sem efeito: a "tentação" do d-G cita "não garante a legitimidade", expressão que não está mais no item. Ajuste facultativo: "(tentação: saber que o HTTPS autentica o servidor e concluir que ele garante que o site é o da instituição pretendida → marcar E)".
- R-5 — CONFERE (BACKLOG registrado; sem item).
- R-6 — CONFERE (acréscimo ao 4.1.1 idêntico).

3. CITAÇÕES NOVAS DO PRODUTOR (cursos 4.1.3, 4.2.1, 4.2.2 e 4.3.1) × páginas lidas pela QA em 08/10/2026
- 4.1.3, F13: worm "Propaga-se automaticamente pelas redes, explorando vulnerabilidades nos sistemas e aplicativos instalados"; spyware "Projetado para monitorar as atividades de um sistema e enviar as informações coletadas para terceiros."; vírus "Propaga-se enviando cópias de si mesmo por e-mails e mensagens." — CONFEREM.
- 4.2.1, F13: "nome popular para ferramentas antimalware" — CONFERE.
- 4.2.2, F14: "protege seu computador contra ataques vindos pela rede" — CONFERE.
- 4.3.1, F15: "Phishing é um tipo de fraude na qual golpistas tentam obter informações pessoais e financeiras" — CONFERE.
- Nos d-G 6B-10 (F14) e 6B-11 (F13), as citações também conferem. A afirmação de que o F13 não menciona antispyware coincide com a leitura da QA.

4. ITENS REAIS 96 E 98 — CONFERE
Tabela, cargo (Analista Judiciário – Apoio Especializado – Análise de Dados; Conhecimentos Específicos), gabaritos definitivos (96 = E; 98 = C), pontos de julgamento, subitem 4/4.1, aderência parcial e motivo, bloco de comando e nota de BACKLOG: tudo conforme o parecer. Nenhum texto transcrito.

5. TABELA DE CORREÇÕES, CONTAGENS E MARCADORES
- Tabela de Correções: 9 linhas (O-1 a O-3, R-1 a R-6), com parte/item, correção, origem e status. A R-5 está como BACKLOG e a R-6 registra a conferência visual em BACKLOG — CONFERE.
- Contagens (conferidas nas linhas do d-G): 15 itens; 7 C (02, 04, 05, 08, 11, 14, 15) e 8 E (01, 03, 06, 07, 09, 10, 12, 13); 8 [TS], sendo 3 C e 5 E; 0 VOLÁTIL; 2 = 1, 2.1 = 4, 4.1 = 4, 4.2 = 3, 4.3 = 3 — CONFEREM, e a linha "Contagem" bate.
- Marcadores "FIM DA PARTE 1/3", "FIM DA PARTE 2/3", "FIM DA PARTE 3/3" e "FIM DO LOTE 6b" — CONFEREM. Título "v2" com a linha "v2 — correções da QA rodada 1, 08/10/2026" — CONFERE.

6. ALTERAÇÕES FORA DO PARECER (diff v1 × v2)
Fora das O e R, só há alterações decorrentes delas: o d-G do 6B-06, que deixa de dizer "a conferir pela GCB-CQFP" por causa da R-6; a "tentação" do d-G do 6B-15, por causa da R-4; e a legenda "Fontes F1 a F15", por causa da R-1. Com as citações do item 3 acima, ficam satisfeitas a regra "nenhuma afirmação no d-G além do que está no curso" e a regra de citação literal. Nenhum outro item, gabarito, par ou seção foi alterado — CONFERE.

RESULTADO: LOTE 6b v2 — CONFERIDO. Pronto para a reconciliação. Sem pendências. Os dois ajustes facultativos (lista do F4 e "tentação" do d-G 6B-15) não condicionam o resultado e ficam a critério da produção ou da PRES-S (PRÓXIMO). BACKLOG mantido: R-5 e a conferência visual humana dos itens 96 e 98.
FIM DA CONFERÊNCIA DE APLICAÇÃO
