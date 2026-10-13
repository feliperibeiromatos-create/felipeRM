# Lote 6b — TI-REDES-SEGURANCA (P1 itens 2 e 4: redes e segurança)

Prova: P1

## Itens do edital

- P1-2 — Redes de computadores
- P1-2.1 — Conceitos básicos, ferramentas, aplicativos e procedimentos de Internet e intranet
- P1-4.1 — Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais
- P1-4.2 — Programas de proteção (antivírus, firewall, antispyware)
- P1-4.3 — Ameaças digitais (phishing, pharming)

## Resumo

```text
NOTA DO EDITAL (8.11.2): na prova objetiva, cada item vale +1,00 ponto se a marcação concordar com o gabarito oficial definitivo, −1,00 ponto se discordar e 0,00 se não houver marcação ou houver marcação dupla (C e E) (Edital nº 1/2026, subitem 8.11.2). Só o fato e a fonte.

2 REDES. Rede = equipamentos interligados que seguem protocolos. Alcance: PAN (pessoal), LAN (área restrita: sala, prédio, campus), MAN (cidade), WAN (áreas distantes; a Internet é a maior WAN). Cliente solicita, servidor oferece; par a par = ambos. Switch interliga equipamentos da LAN; roteador interliga REDES e escolhe a rota; modem converte o sinal do provedor; access point dá Wi-Fi. IP identifica o equipamento (IPv4 32 bits; IPv6 128 bits); faixas privadas (RFC 1918): 10/8, 172.16/12, 192.168/16; porta identifica o serviço; DHCP atribui endereços; DNS traduz nome em IP. TCP = confiável e ordenado; UDP = sem essas garantias. HTTP/HTTPS (Web), FTP (arquivos), SMTP (envio/repasse de e-mail), IMAP (acesso com mensagens no servidor), POP3 (acesso à caixa, em geral baixando).

2.1 INTERNET E INTRANET. Internet = rede mundial de redes (TCP/IP); Web = serviço SOBRE a Internet (páginas, HTTP/HTTPS, URLs); não são sinônimos. Intranet = rede PRIVADA que usa as MESMAS tecnologias da Internet, com acesso RESTRITO ao público interno. Extranet = extensão CONTROLADA da intranet a externos autorizados. Navegador = programa cliente; mecanismo de busca = serviço que indexa e localiza. Cookies, cache, histórico; navegação privada NÃO oculta a navegação do provedor nem do administrador da rede. VPN = canal cifrado que leva o usuário externo à rede interna. DNS adulterado leva ao site errado mesmo com o endereço certo digitado.

4 SEGURANÇA. Ativo, ameaça, vulnerabilidade, risco, controle, incidente. Engenharia social = manipular pessoas. Governança digital: políticas, responsabilidades e controles (conceito geral; sem item neste lote).

4.1 TRÍADE CIA. CONFIDENCIALIDADE = só quem está autorizado ACESSA; INTEGRIDADE = não há alteração indevida; DISPONIBILIDADE = acessível quando necessário. Negação de serviço e ransomware atingem a disponibilidade; spyware e phishing, a confidencialidade; adulteração, a integridade. BACKUP: completo (tudo); incremental (mudou desde o último completo ou incremental; marca os arquivos; restaura com completo + todos os incrementais); diferencial (não marca; numa rotina completo + diferenciais, acumula desde o completo; restaura com completo + último diferencial). "Desde o último completo ou incremental" também aparece como definição do diferencial (Microsoft): não é erro seguro. Cópia em local diferente; testar a restauração; sincronização não é backup sem histórico de versões. MALWARE: vírus = precisa de HOSPEDEIRO e de execução ("se propaga inserindo cópias de si mesmo"); worm = independente, propaga-se sozinho pela rede; trojan = parece legítimo, não se replica; spyware = monitora e envia a terceiros; ransomware = bloqueia dados e cobra resgate; bot/botnet = controle remoto; backdoor = porta de volta; rootkit = esconde presença. Backup é a defesa essencial contra ransomware.

4.2 PROTEÇÃO. ANTIVÍRUS = arquivos e programas: detecta, bloqueia, remove malware (assinaturas e heurística; precisa de atualização; não detecta tudo). FIREWALL = tráfego: permite ou bloqueia conexões por regras ("filtrar o tráfego de rede que entra e sai do dispositivo"); não remove malware nem substitui o antivírus. ANTISPYWARE = detecta e remove programas espiões. Quarentena = isola, não exclui. Suítes reúnem os três, mas as funções são distintas.

4.3 AMEAÇAS. PHISHING = fraude para obter dados pessoais e financeiros, engenharia social; spear phishing, smishing, vishing. PHARMING = tipo específico de phishing que REDIRECIONA a navegação para site falso, por adulteração da resolução de nomes (DNS, hosts); o usuário digita o endereço certo. HTTPS = comunicação cifrada e servidor autenticado para o domínio acessado; NÃO prova que o domínio é o legítimo nem a boa-fé do site.

PEGADINHAS-CHAVE: LAN × WAN invertidos; intranet "sem TCP/IP"; extranet × intranet trocadas; Internet = Web; integridade × disponibilidade trocadas; incremental × diferencial trocados; vírus × worm trocados; firewall × antivírus trocados; antivírus infalível; phishing × pharming trocados; HTTPS = site legítimo.
```

## Curso

```text
## ITEM 2 — REDES DE COMPUTADORES

### 2.0.1 DEFINIÇÃO
Rede de computadores é um conjunto de equipamentos (computadores, celulares, impressoras, servidores, roteadores) interligados por meios físicos (cabos de cobre, fibra óptica) ou sem fio (Wi-Fi, rádio) para trocar dados e compartilhar recursos (arquivos, impressoras, acesso à Internet). Para que equipamentos de fabricantes diferentes se entendam, usam PROTOCOLOS: conjuntos de regras que definem formato e sequência das mensagens. Conceito geral.

2.0.2 CLASSIFICAÇÃO POR ALCANCE (conceito geral)
- PAN (rede pessoal): poucos metros, em torno de uma pessoa (ex.: fone Bluetooth ligado ao celular).
- LAN (rede local): área geográfica restrita, como uma sala, um edifício ou um campus. Ex.: a rede interna de um prédio de gabinetes.
- MAN (rede metropolitana): abrange uma cidade ou região metropolitana.
- WAN (rede de longa distância): interliga redes ou equipamentos em áreas geograficamente distantes (cidades, estados, países). A Internet é a maior WAN existente, formada pela interligação de milhares de redes.
Chave de prova: o critério é o ALCANCE GEOGRÁFICO. LAN = restrita; WAN = distante. A banca troca as duas definições.

2.0.3 MODELO CLIENTE-SERVIDOR E PAR A PAR (conceito geral)
- Cliente: aplicativo ou equipamento que SOLICITA um serviço (o navegador solicita uma página).
- Servidor: equipamento ou programa que OFERECE o serviço (servidor web, servidor de arquivos, servidor de e-mail, servidor de nomes).
- Par a par (peer-to-peer): cada equipamento atua, ao mesmo tempo, como cliente e servidor, sem servidor central dedicado.

2.0.4 EQUIPAMENTOS DE REDE (conceito geral)
- Placa de rede (NIC): conecta o equipamento à rede; tem um endereço físico (MAC).
- Switch (comutador): interliga equipamentos de uma LAN e encaminha os dados só para a porta do destinatário.
- Roteador: interliga REDES DIFERENTES e escolhe o caminho dos pacotes entre elas; em casa e em escritórios costuma acumular as funções de roteador, switch, ponto de acesso Wi-Fi e firewall básico.
- Ponto de acesso (access point): disponibiliza a rede por Wi-Fi.
- Modem: converte o sinal do provedor (linha telefônica, cabo, fibra) para o formato usado na rede local.
- Gateway: ponto de saída da rede local para outra rede (em geral, a Internet).

2.0.5 ENDEREÇAMENTO IP E PORTAS (conceito geral)
- Endereço IP identifica um equipamento na rede e permite que os pacotes cheguem ao destino. IPv4 usa 32 bits (escritos em quatro números de 0 a 255 separados por pontos, como 200.10.20.30); IPv6 usa 128 bits (hexadecimal), criado por causa do esgotamento dos endereços IPv4.
- Endereços PRIVADOS (RFC 1918): a IANA reservou três blocos para redes privadas: 10.0.0.0 a 10.255.255.255 (10/8); 172.16.0.0 a 172.31.255.255 (172.16/12); 192.168.0.0 a 192.168.255.255 (192.168/16). São usados dentro de organizações (inclusive em intranets) e em residências. Não identificam um equipamento de modo único na Internet pública: o acesso à Internet a partir deles depende de tradução de endereços (NAT) feita pelo roteador. Ponto de prova: o nome de "privado" não significa "seguro"; significa "de uso interno".
- Porta: número que identifica o serviço no equipamento (ex.: 80 para HTTP, 443 para HTTPS, 25 para SMTP). Não se cobra numeração de porta como regra, mas é útil para entender o firewall (4.2).
- DHCP: serviço que atribui automaticamente endereço IP (e outros parâmetros) aos equipamentos que entram na rede.

2.0.6 TCP/IP E PROTOCOLOS DE APLICAÇÃO (conceito geral, com fontes quando abertas)
A Internet usa a família de protocolos TCP/IP. IP cuida do endereçamento e do encaminhamento; TCP entrega os dados de forma confiável, ordenada e com controle de erros; UDP entrega sem essas garantias, com menor atraso (usado em voz e vídeo ao vivo). Na camada de aplicação:
- HTTP: protocolo da Web; o RFC 9110 o descreve como "a stateless application-level protocol". HTTPS = HTTP sobre conexão TLS: autentica o servidor para o domínio acessado (certificado digital) e protege o conteúdo contra leitura e alteração no caminho (ver 4.3.4).
- DNS: traduz nomes de domínio em endereços IP; o RFC 1034 introduz "domain style names, their use for Internet mail and host address support,". Detalhe em 2.1.5.
- DHCP: atribuição automática de endereços (ver acima).
- FTP: transferência de arquivos entre cliente e servidor.
- SMTP: transferência de mensagens de e-mail ("transfer mail reliably and efficiently", RFC 5321); usado no ENVIO e no repasse entre servidores. IMAP: o cliente "access and manipulate electronic mail messages on a server", mantendo as mensagens no servidor. POP3: permite a uma estação "access a maildrop", em geral baixando as mensagens. O tratamento didático completo de e-mail está no Lote 6a.
Exemplo aplicado: o servidor da unidade de taquigrafia, o Derep (antigo DETAQ), que consulta uma página interna de pauta de comissão usa HTTP/HTTPS; envia o texto revisado por e-mail via SMTP; e o nome do servidor interno é resolvido em endereço por DNS.

### 2.0.7 PEGADINHAS PROVÁVEIS (ITEM 2)
P1. "A LAN interliga redes situadas em países distintos; a WAN restringe-se a um edifício" → ERRADO (invertido: LAN = área restrita; WAN = área distante).
P2. "O switch interliga redes diferentes e escolhe a rota entre elas" → ERRADO (isso é o roteador; o switch interliga equipamentos da mesma LAN).
P3. "O protocolo UDP garante a entrega ordenada e confiável dos dados" → ERRADO (garantias são do TCP).
P4. "Endereço IP privado é, por definição, protegido contra qualquer ataque" → ERRADO (privado = uso interno).
P5. "O DHCP traduz nomes de domínio em endereços IP" → ERRADO (isso é o DNS; DHCP atribui endereços).

## ITEM 2.1 — CONCEITOS BÁSICOS, FERRAMENTAS, APLICATIVOS E PROCEDIMENTOS DE INTERNET E INTRANET

### 2.1.1 INTERNET, WEB E INTRANET (DEFINIÇÕES)
- INTERNET: rede mundial de computadores formada pela interligação de redes de todo o planeta, que usa o conjunto de protocolos TCP/IP. É a INFRAESTRUTURA.
- WEB (World Wide Web, WWW): serviço que funciona SOBRE a Internet: conjunto de páginas e recursos interligados por hiperlinks, acessados por meio do protocolo HTTP/HTTPS e identificados por URLs. A Web é UM dos serviços da Internet; outros: e-mail, transferência de arquivos, mensagens e chamadas de voz e vídeo. Internet e Web NÃO são sinônimos.
- INTRANET: rede PRIVADA de uma organização, que usa as mesmas tecnologias e protocolos da Internet (TCP/IP, navegador, páginas, e-mail) para uso interno, com ACESSO RESTRITO ao público autorizado (servidores, empregados, colaboradores). O que a define é o público e o controle de acesso, não uma tecnologia diferente.
- EXTRANET: extensão CONTROLADA da intranet para um público externo autorizado (parceiros, fornecedores, clientes), geralmente mediante autenticação e canal protegido.
Tabela de comparação (conceito geral):
| Rede | Público | Tecnologia | Exemplo |
| Internet | aberto, mundial | TCP/IP | sites públicos |
| Intranet | interno, autorizado | as mesmas tecnologias da Internet | portal interno de servidores da Casa |
| Extranet | externo, autorizado e controlado | as mesmas tecnologias, com acesso restrito | portal restrito a fornecedor contratado |
Chave de prova: usar navegador e protocolos da Internet NÃO torna uma intranet pública; ela continua restrita. E a intranet não é uma "internet menor": é rede privada com tecnologia de Internet.

2.1.2 ANATOMIA DE UMA URL (conceito geral)
Exemplo: https://www.exemplo.gov.br:443/caminho/pagina.html?x=1
- https = protocolo; www.exemplo.gov.br = nome de domínio (host); :443 = porta (em geral omitida); /caminho/pagina.html = recurso no servidor; ?x=1 = parâmetros. O sufixo .gov.br indica domínio de governo brasileiro; a aparência do nome não prova a autenticidade do site (ver 4.3).

2.1.3 NAVEGADOR E MECANISMO DE BUSCA (conceito geral)
- Navegador (browser): programa CLIENTE que solicita páginas aos servidores web e as exibe. Recursos comuns: abas, favoritos (marcadores), histórico, cache, cookies, downloads, extensões, modo de navegação privada.
- Mecanismo de busca: serviço (site) que indexa páginas e as localiza por palavras-chave. O navegador é o programa; a busca é um serviço acessado por meio dele.
- Cookies: pequenos arquivos que o site grava no navegador para lembrar informações (sessão, preferências). Cache: cópia local de recursos para acelerar novos acessos. Histórico: lista de páginas visitadas.
- Navegação privada (anônima): não grava histórico, cookies e dados de formulário NO EQUIPAMENTO ao fechar a janela; NÃO oculta a navegação do provedor, do administrador da rede nem dos sites visitados. Pegadinha clássica.
- Download: copiar arquivo do servidor para o equipamento; upload: enviar arquivo do equipamento ao servidor.

2.1.4 PROCEDIMENTOS BÁSICOS E FERRAMENTAS (conceito geral)
- Acesso remoto e VPN: a VPN (rede privada virtual) cria um canal protegido (cifrado) sobre a Internet, que permite ao usuário externo acessar recursos da rede interna como se estivesse nela. É a forma usual de acessar uma intranet de fora da organização.
- Compartilhamento de arquivos e pastas na rede interna, com permissões por usuário.
- Diagnóstico simples: ping testa se um destino responde; traceroute (tracert) mostra o caminho dos pacotes. Citação genérica; não se cobra sintaxe.
- Boas práticas de navegação: atualizar o navegador e o sistema, evitar baixar de fontes desconhecidas, desconfiar de links (ver item 4).

2.1.5 DNS EM DETALHE (conceito geral)
O DNS é um sistema distribuído e hierárquico de nomes. Ele permite que o usuário acesse um site pelo NOME (www.exemplo.gov.br) sem decorar o endereço IP: o navegador pergunta a um servidor de nomes (resolvedor) qual o endereço do nome, recebe a resposta e só então se conecta ao servidor. O RFC 1034 introduz os "domain style names" e seu uso para correio da Internet e endereços de máquinas. Duas consequências para a prova: (1) se a resposta do DNS for adulterada, o usuário é levado a outro servidor mesmo digitando o nome correto — base do PHARMING (4.3.2); (2) o computador também consulta um arquivo local de nomes (arquivo hosts), cuja adulteração produz efeito semelhante.

### 2.1.6 EXEMPLO APLICADO AO LEGISLATIVO
O servidor do Derep (antigo DETAQ) acessa, de dentro do prédio, a intranet da Casa para consultar a pauta e os modelos de redação: o portal é restrito a servidores autorizados, mas usa navegador, HTTP/HTTPS e DNS como qualquer site. Em teletrabalho, ele usa VPN para chegar à mesma intranet de casa. Já um fornecedor contratado que acompanha o andamento de um serviço usaria um portal de extranet, com acesso limitado ao que lhe cabe. O site público da Casa, aberto a qualquer cidadão, é Internet. Se o mesmo servidor digitar o endereço correto e cair numa página falsa por DNS adulterado, o problema não é de digitação: é pharming.

### 2.1.7 PEGADINHAS PROVÁVEIS (ITEM 2.1)
P1. "A intranet é uma rede que não pode usar TCP/IP nem navegador, por ser de uso interno" → ERRADO (usa as mesmas tecnologias da Internet; o que a distingue é o acesso restrito).
P2. "Intranet é a mesma coisa que extranet" → ERRADO (a extranet estende o acesso, de modo controlado, a parceiros externos).
P3. "A extranet é a rede interna acessível só a empregados; a intranet é a aberta a parceiros" → ERRADO (invertido).
P4. "Internet e Web são sinônimos" → ERRADO (a Web é um serviço sobre a Internet).
P5. "A janela de navegação anônima impede o provedor de Internet de saber quais sites o usuário visita" → ERRADO.
P6. "O DNS atribui automaticamente endereços IP aos equipamentos" → ERRADO (DHCP).
P7. "Endereços da faixa 192.168.0.0 a 192.168.255.255 são públicos e identificam um único equipamento na Internet" → ERRADO (faixa privada, RFC 1918).
P8. "O navegador e o mecanismo de busca são o mesmo programa" → ERRADO.

## ITEM 4 — CONCEITOS GERAIS DE SEGURANÇA E GOVERNANÇA DIGITAL

### 4.0.1 SEGURANÇA DA INFORMAÇÃO: CONCEITOS GERAIS
Segurança da informação é o conjunto de medidas para proteger a informação, em qualquer meio, de acesso, alteração, destruição ou indisponibilidade indevidos. Vocabulário (conceito geral):
- Ativo: tudo que tem valor para a organização (informação, sistemas, equipamentos, pessoas).
- Ameaça: causa potencial de um incidente (um código malicioso, um golpista, uma falha elétrica).
- Vulnerabilidade: fraqueza que pode ser explorada por uma ameaça (sistema sem atualização, senha fraca, usuário desatento).
- Risco: combinação da probabilidade de a ameaça explorar a vulnerabilidade e do impacto resultante.
- Controle (medida de segurança): o que reduz o risco (antivírus, firewall, backup, treinamento, política).
- Incidente: evento que compromete a segurança.
Engenharia social: manipulação de pessoas, e não de máquinas, para obter informação ou acesso. Boa parte dos golpes do 4.3 explora o fator humano.

4.0.2 GOVERNANÇA DIGITAL (conceito geral; sem base aberta hoje)
Governança digital, no sentido amplo do edital, é o conjunto de políticas, responsabilidades, processos e controles pelos quais uma organização dirige e acompanha o uso da tecnologia e dos dados: quem decide, quem responde, quais regras valem (política de segurança, classificação da informação, gestão de acessos, resposta a incidentes, conscientização dos usuários). Nesta produção NÃO foi aberta fonte institucional que defina o termo, e o edital não o detalha; por isso, NÃO HÁ ITEM sobre governança digital neste lote (a especificação previa o item "se houver base").

### 4.0.3 EXEMPLO APLICADO AO LEGISLATIVO
Política de segurança: o servidor do Derep (antigo DETAQ) não compartilha a senha da conta institucional, não deixa notas taquigráficas de reunião reservada em pasta aberta e comunica ao setor responsável qualquer e-mail suspeito. Cada medida é um controle; a falta delas é vulnerabilidade.

## ITEM 4.1 — SEGURANÇA DA INFORMAÇÃO: BACKUP, VÍRUS, WORMS E PRAGAS VIRTUAIS

### 4.1.1 A TRÍADE CIA (CONCEITO GERAL)
Os três pilares clássicos da segurança da informação, conhecidos como tríade CIA (em inglês, Confidentiality, Integrity, Availability):
| Propriedade | Garante que a informação... | Se for violada... | Exemplo |
| CONFIDENCIALIDADE | seja acessível SOMENTE a quem está autorizado | vazamento, acesso indevido | notas de reunião reservada lidas por quem não tem acesso |
| INTEGRIDADE | NÃO seja alterada, apagada ou corrompida de modo não autorizado ou acidental; permaneça exata e completa | adulteração | alguém altera o texto final de um discurso na pasta compartilhada |
| DISPONIBILIDADE | esteja ACESSÍVEL e utilizável por quem está autorizado SEMPRE QUE necessário | indisponibilidade | sistema fora do ar por ataque de negação de serviço ou por ransomware |
Mnemônico: C = quem pode LER; I = ninguém pode ALTERAR indevidamente; D = pode ACESSAR quando precisar. O erro clássico é trocar INTEGRIDADE por DISPONIBILIDADE (a banca desloca as definições). Propriedades complementares citadas na literatura (autenticidade, não repúdio, legalidade): conceito geral, fora da tríade.
Fonte: conceito geral.
Relação com os itens reais: a tríade CIA é o tema dos itens 96 e 98 do TRF6 2024 (seção ITENS REAIS acima), cujo ponto de julgamento foi conferido contra o caderno oficial em 08/10/2026. Os itens reais exploram (96) a integridade descrita às avessas, como garantia de que dados tenham sido alterados sem registro, mesmo sob necessidade de auditoria (E), e (98) a disponibilidade mantida mesmo com sistema ou infraestrutura sob pressão (C): disponibilidade inclui resistir a sobrecarga.
Mapeamento ameaça × propriedade (conceito geral): vazamento e espionagem (spyware, phishing que captura senhas) atingem a CONFIDENCIALIDADE; vírus e programas que alteram arquivos, ou invasor que modifica registros, atingem a INTEGRIDADE; negação de serviço, ransomware que bloqueia dados e falta de backup atingem a DISPONIBILIDADE. Um mesmo ataque pode atingir mais de uma propriedade (ransomware: disponibilidade; se há extorsão por vazamento, também confidencialidade).

### 4.1.2 BACKUP (CÓPIA DE SEGURANÇA)
Definição: cópia dos dados feita para permitir a RECUPERAÇÃO após perda, corrupção, exclusão acidental, falha de hardware, desastre ou ataque (ransomware, por exemplo). Está ligado à DISPONIBILIDADE e à INTEGRIDADE: permite voltar a uma versão íntegra dos dados.
Fontes abertas hoje: "Faça backups periódicos." e "Fazer backups regularmente também é essencial para proteger os seus dados".
Tipos de backup (conceito geral; a nomenclatura é a usual em provas):
- COMPLETO (full): copia TODOS os dados selecionados, independentemente de terem mudado. Restauração simples (basta o último completo); ocupa mais espaço e tempo.
- INCREMENTAL: copia SOMENTE o que mudou desde o último backup completo ou incremental e marca os arquivos como copiados. Backup rápido e pequeno; a restauração exige o último completo MAIS todos os incrementais até o ponto desejado, na ordem.
- DIFERENCIAL: NÃO marca os arquivos como copiados; por isso, numa rotina de completo + diferenciais, cada diferencial acumula tudo o que mudou desde o último completo e cresce até o próximo completo. A restauração exige o último completo MAIS o último diferencial.
Exemplo numérico: completo no domingo; segunda, terça e quarta com alterações em arquivos distintos (A na segunda, B na terça, C na quarta). INCREMENTAL: segunda guarda A, terça guarda B, quarta guarda C; restaurar a quarta = domingo + segunda + terça + quarta. DIFERENCIAL: segunda guarda A, terça guarda A+B, quarta guarda A+B+C; restaurar a quarta = domingo + quarta.
Chave de prova: a diferença segura está na marcação e na restauração. O incremental "zera" o controle de alterações (cada um guarda só o que mudou desde o anterior; restaura-se com o completo + todos os incrementais). O diferencial não "zera" (acumula desde o completo; restaura-se com o completo + o último diferencial). ATENÇÃO: o material de concurso costuma resumir o diferencial como "desde o último completo", mas a documentação da Microsoft define o diferencial como cópia do que mudou "since the last normal or incremental backup". Portanto, afirmação de que o diferencial copia o que mudou desde o último completo ou incremental NÃO é erro seguro.
Boas práticas (conceito geral): backups periódicos e automatizados; cópia em local DIFERENTE do original (não só no mesmo disco ou no mesmo computador); cópias fora do ambiente (offline ou em nuvem) para o caso de desastre ou ransomware; TESTAR a restauração (backup que nunca foi restaurado não é garantia de recuperação); proteger a própria cópia (acesso restrito, cifra) — a cópia também contém informação (confidencialidade). Regra 3-2-1, divulgada como boa prática (três cópias, em dois tipos de mídia, uma fora do local), sem fonte aberta hoje e sem item.
Backup × sincronização: a sincronização de pastas na nuvem mantém os locais IGUAIS, de modo que uma exclusão ou uma criptografia por ransomware pode ser replicada; só funciona como backup se houver HISTÓRICO de versões e retenção. Backup guarda um ponto no tempo; sincronização espelha o estado atual. (O tratamento do OneDrive está no Lote 6a.)

### 4.1.3 CÓDIGOS MALICIOSOS (MALWARE): O GÊNERO
Malware, ou código malicioso, ou "praga virtual", é todo programa criado para executar ações danosas ou não autorizadas em um equipamento. Vírus, worm, trojan, spyware, ransomware, bot, backdoor e rootkit são ESPÉCIES. Cuidado: "vírus" é uma espécie, e o linguajar comum o usa para tudo; a prova distingue.
Definição de vírus aberta hoje: "programa ou parte de um programa de computador, normalmente malicioso, que se propaga inserindo cópias de si mesmo" (acrescenta-se, na obra, que se torna parte de outros programas e arquivos — complemento da definição usual). O fascículo Códigos Maliciosos da Cartilha descreve o worm como o que "Propaga-se automaticamente pelas redes, explorando vulnerabilidades nos sistemas e aplicativos instalados" e o spyware como "Projetado para monitorar as atividades de um sistema e enviar as informações coletadas para terceiros."; segundo o mesmo fascículo, o vírus "Propaga-se enviando cópias de si mesmo por e-mails e mensagens." As demais definições abaixo são CONCEITO GERAL.

### 4.1.4 ESPÉCIES DE MALWARE (QUADRO DIDÁTICO)
| Espécie | Como age | Característica de prova |
| VÍRUS | insere cópias de si em programas e arquivos (hospedeiros); só age quando o hospedeiro é executado | depende de hospedeiro e de execução; pode circular por e-mails e mensagens, mas cada infecção depende de o hospedeiro ser executado; não explora sozinho vulnerabilidades da rede, como o worm |
| WORM | programa independente que se replica e se propaga automaticamente pelas redes, explorando vulnerabilidades ou falhas de configuração | NÃO precisa de hospedeiro nem de ação do usuário; consome rede e recursos |
| TROJAN (cavalo de Troia) | parece um programa legítimo (jogo, planilha, "atualização"), mas executa também funções maliciosas | NÃO se replica; depende de o usuário instalá-lo e executá-lo |
| SPYWARE | monitora as atividades do usuário e envia as informações a terceiros | atinge a confidencialidade; ex.: keylogger (registra teclas), screenlogger (registra telas), adware (propaganda) |
| RANSOMWARE | torna inacessíveis os dados do equipamento (em geral, por criptografia) e exige resgate para restabelecer o acesso | atinge a disponibilidade; defesa essencial: backup |
| BOT / BOTNET | programa que permite controle remoto do equipamento; vários bots formam uma botnet, usada em ataques de negação de serviço, envio de spam e fraudes | equipamento "zumbi" |
| BACKDOOR | deixa aberta uma porta para o invasor voltar ao equipamento | acesso remoto não autorizado |
| ROOTKIT | esconde a presença do invasor ou de outros códigos maliciosos | dificulta a detecção |
Definição de ransomware aberta hoje: "Ransomware é um tipo de código malicioso que torna inacessíveis os dados armazenados em um equipamento"; o acesso é, em geral, bloqueado por criptografia, e se cobra um resgate. Ponto central: pagar o resgate não garante a devolução dos dados; o backup é a defesa.
VÍRUS × WORM: a diferença decisiva. Vírus precisa de um HOSPEDEIRO (arquivo ou programa) e da EXECUÇÃO desse hospedeiro; worm é independente e se espalha sozinho pela rede. A banca troca as duas descrições.
Vias de infecção (conceito geral): anexos e links em mensagens; downloads de fontes não confiáveis; mídias removíveis (pendrive); vulnerabilidades de sistema ou de aplicativo sem atualização; macros em documentos; sites comprometidos.
Defesas (conceito geral): atualizar sistema e aplicativos (correções de segurança), antivírus (4.2), firewall (4.2), backup, não executar anexos e arquivos desconhecidos, privilégio mínimo (não usar conta de administrador no dia a dia).

### 4.1.5 EXEMPLO APLICADO AO LEGISLATIVO
Um servidor do Derep (antigo DETAQ) recebe, por e-mail, um arquivo de texto com macro, aparentemente com a transcrição de uma reunião. Ao abri-lo e habilitar a macro, um ransomware criptografa a pasta de notas taquigráficas do computador e das unidades de rede mapeadas. Efeitos: DISPONIBILIDADE perdida (não se acessa os arquivos); o resgate não garante recuperação. Resposta correta: isolar o equipamento da rede, comunicar a área de segurança e restaurar a partir de BACKUP íntegro, mantido em local diferente, cuja restauração tenha sido testada. Se existisse apenas sincronização em nuvem sem histórico de versões, os arquivos criptografados poderiam ter sido replicados. Em outro cenário, um worm explora uma vulnerabilidade de um servidor sem atualização e se espalha pela rede interna sem que ninguém abra nada: é o que o diferencia do vírus.

### 4.1.6 PEGADINHAS PROVÁVEIS (ITEM 4.1)
P1. "A integridade garante que a informação esteja disponível ao usuário autorizado sempre que necessária" → ERRADO (isso é disponibilidade; integridade = não alteração indevida).
P2. "A disponibilidade assegura que a informação só seja acessada por quem está autorizado" → ERRADO (isso é confidencialidade).
P3. "Numa rotina de completo + diferenciais, a restauração exige o completo e todos os diferenciais posteriores" → ERRADO (basta o completo e o último diferencial).
P4. "Para restaurar com backups incrementais, basta o último incremental" → ERRADO (é preciso o completo e todos os incrementais em sequência).
P5. "O backup completo copia apenas o que mudou" → ERRADO.
P6. "Manter a cópia no mesmo disco do original é suficiente para recuperar dados em caso de falha desse disco" → ERRADO.
P7. "O worm depende de um arquivo hospedeiro e da ação do usuário para se propagar" → ERRADO (isso descreve o vírus).
P8. "O trojan se replica automaticamente pela rede" → ERRADO (não se replica; depende de o usuário executá-lo).
P9. "Sincronizar uma pasta na nuvem equivale a ter backup, em qualquer situação" → ERRADO.
P10. "O ransomware é um programa que apenas exibe propagandas indesejadas" → ERRADO (isso é adware, um tipo de spyware no uso comum; ransomware bloqueia dados e cobra resgate).
P11. "Pagar o resgate assegura a recuperação dos dados" → ERRADO.

## ITEM 4.2 — PROGRAMAS DE PROTEÇÃO: ANTIVÍRUS, FIREWALL, ANTISPYWARE

### 4.2.1 ANTIVÍRUS (CONCEITO GERAL)
Programa que DETECTA, bloqueia e REMOVE códigos maliciosos (vírus, worms, trojans e outros), por varredura de arquivos e memória. Métodos: ASSINATURAS (identifica por padrões já conhecidos — exige base atualizada); HEURÍSTICA e COMPORTAMENTO (suspeita por características e ações de programas, o que permite alguma detecção de ameaças novas, com risco de falso positivo). Recursos usuais: proteção em tempo real, varredura sob demanda, quarentena (isola o arquivo suspeito), atualização automática. Limites: nenhum antivírus detecta todas as ameaças, principalmente as novas; não impede o usuário de ser enganado por golpe (phishing); precisa estar atualizado. "Instale um antivírus antes de qualquer aplicativo". O fascículo Códigos Maliciosos descreve o antivírus como "nome popular para ferramentas antimalware".

### 4.2.2 FIREWALL (CONCEITO GERAL)
Mecanismo que CONTROLA o tráfego de rede entre redes ou entre o equipamento e a rede, permitindo ou bloqueando conexões segundo REGRAS (origem, destino, porta, protocolo, sentido). A página da Microsoft sobre o Windows o descreve como "uma funcionalidade de segurança que ajuda a proteger o seu dispositivo ao filtrar o tráfego de rede que entra e sai do dispositivo". Tipos: firewall PESSOAL (software no equipamento do usuário) e firewall de REDE (equipamento ou software no perímetro da rede). A Cartilha recomenda: "Use mecanismos de segurança, como antivírus e firewall pessoal.". O fascículo Computadores diz que o firewall "protege seu computador contra ataques vindos pela rede".
Limites (conceito geral): o firewall filtra COMUNICAÇÕES; não é feito para varrer arquivos e remover vírus, e não evita, por si só, que o usuário abra um arquivo malicioso recebido por uma conexão permitida (anexo de e-mail, por exemplo). Não substitui o antivírus. Um firewall mal configurado (regras liberais demais) perde a eficácia.
Chave de prova: ANTIVÍRUS = olha ARQUIVOS e PROGRAMAS (detecta e remove malware). FIREWALL = olha TRÁFEGO (permite ou bloqueia conexões por regras). A banca troca as funções.

### 4.2.3 ANTISPYWARE (CONCEITO GERAL)
Programa voltado a detectar e remover SPYWARE, o código que monitora as atividades do usuário e envia as informações a terceiros (keyloggers, screenloggers, adwares). Hoje, muitos produtos de segurança incorporam antivírus, antispyware e firewall num pacote ("suíte de segurança"); a distinção conceitual permanece: a função de cada mecanismo é distinta, ainda que venham juntos.

4.2.4 OUTROS CONTROLES CITADOS (conceito geral, sem item)
Atualização de sistemas (correções de segurança), autenticação forte (segundo fator), cifração, controle de acesso, IDS/IPS (detecção/prevenção de intrusão), proxy, VPN. Servem de apoio à compreensão; fora do núcleo do edital.

### 4.2.5 QUADRO COMPARATIVO
| Mecanismo | O que olha | O que faz | Não faz |
| Antivírus | arquivos, programas, memória | detecta, bloqueia, remove malware | não controla regras de conexão; não detecta todo malware novo |
| Firewall | tráfego de rede | permite ou bloqueia conexões por regras | não varre e remove malware de arquivos; não impede o usuário de ser enganado |
| Antispyware | programas espiões | detecta e remove spyware | não substitui firewall nem os demais controles |

### 4.2.6 EXEMPLO APLICADO AO LEGISLATIVO
Na rede do Derep (antigo DETAQ): o firewall de perímetro barra conexões vindas da Internet para o servidor de arquivos de notas taquigráficas, permitindo só as necessárias; o antivírus das estações varre o anexo baixado de um e-mail permitido; o antispyware (ou o módulo equivalente) detecta um keylogger que tentava capturar a senha do sistema. Cada um age numa camada; a falha de um não é suprida pelos outros.

### 4.2.7 PEGADINHAS PROVÁVEIS (ITEM 4.2)
P1. "O firewall é o programa destinado a detectar e remover códigos maliciosos instalados; o antivírus controla o tráfego" → ERRADO (funções invertidas).
P2. "O antivírus atualizado detecta todos os códigos maliciosos, inclusive os desconhecidos" → ERRADO (nenhum antivírus é infalível).
P3. "Com um firewall ativo, não é necessário antivírus" → ERRADO.
P4. "O antispyware serve para filtrar o tráfego conforme regras de acesso" → ERRADO (função do firewall).
P5. "O firewall impede que o usuário seja vítima de phishing" → ERRADO.
P6. "O antivírus funciona sem necessidade de atualização" → ERRADO.
P7. "Quarentena é a exclusão definitiva do arquivo suspeito" → ERRADO (isola o arquivo; pode ser restaurado ou excluído).

## ITEM 4.3 — AMEAÇAS DIGITAIS: PHISHING E PHARMING

### 4.3.1 PHISHING
Definição aberta hoje: o phishing é "o tipo de fraude por meio da qual um golpista tenta obter dados pessoais e financeiros de um usuário". O golpista se passa por entidade conhecida (banco, órgão público, empresa, colega, chefia) e usa e-mail, mensagem de texto, rede social ou telefone para induzir a vítima a clicar em link para página falsa, abrir anexo malicioso ou digitar senha e dados. A coleta pode ocorrer por página falsa, por formulário na própria mensagem ou pela instalação de código malicioso a partir de link ou anexo. O fascículo Golpes: Evite Fraudes define: "Phishing é um tipo de fraude na qual golpistas tentam obter informações pessoais e financeiras". É ENGENHARIA SOCIAL: atua sobre a pessoa, não sobre a máquina. Variantes (conceito geral): spear phishing (direcionado a pessoa ou grupo específico, com dados reais da vítima), smishing (por SMS ou aplicativo de mensagem), vishing (por voz). Sinais de alerta: urgência ou ameaça; remetente ou link que parece o oficial, mas com letras trocadas; pedido de senha, token ou dados que a instituição não pediria por mensagem; erros de português; anexo inesperado. Defesas: não clicar; digitar o endereço oficial; conferir pelo canal oficial; ativar segundo fator de autenticação; manter antivírus atualizado; relatar à área de segurança.
Alvo: CONFIDENCIALIDADE (captura de credenciais e dados) e, depois, as demais propriedades, pois o acesso obtido pode ser usado para alterar ou apagar.

### 4.3.2 PHARMING
O pharming é, segundo a Cartilha, um tipo específico de phishing que envolve o REDIRECIONAMENTO da navegação do usuário para sites falsos, "por meio de alterações no serviço de DNS (Domain Name System)" (trecho confirmado em 08/10/2026). O mecanismo (ancorado no DNS) é a adulteração da RESOLUÇÃO DE NOMES: como o DNS associa o nome do site ao endereço IP do servidor, quem consegue alterar essa associação faz o nome correto apontar para o servidor do golpista. Formas usuais: adulteração (envenenamento) do cache de um servidor DNS; alteração do servidor DNS configurado no equipamento ou no roteador por malware ou invasão; alteração do arquivo hosts do computador. Consequência: o usuário digita o endereço CORRETO e cai no site falso, sem ter clicado em link nenhum. Nota: a ligação com o DNS tem fonte aberta; as formas de adulteração listadas acima (cache de servidor DNS, roteador, arquivo hosts) são conceito geral, e o arquivo hosts não aparece na Cartilha.
Diferença de prova: PHISHING = engodo ("isca") para a vítima agir (clicar, abrir, informar); a vítima é levada a ir ao site falso, em regra por mensagem. PHARMING = redirecionamento da navegação por adulteração da resolução de nomes: a vítima não precisa ser enganada por mensagem, e digita o endereço certo. Atenção: como o pharming é "tipo específico de phishing", dizer que ele é "espécie de golpe de phishing" não é erro; o erro é trocar o mecanismo de um pelo do outro.

4.3.3 OUTRAS AMEAÇAS CITADAS (conceito geral)
Spam (mensagem não solicitada, em geral em massa); falso suporte técnico; golpe do falso boleto ou do falso pagamento; sequestro de contas; engenharia social presencial. Fora do núcleo do edital (que cita só phishing e pharming), mas úteis para o estudante reconhecer o padrão.

4.3.4 HTTPS E CADEADO: O QUE ELES GARANTEM (conceito geral)
HTTPS é o HTTP sobre conexão protegida por TLS. Com o certificado digital do site, o navegador autentica o servidor como responsável pelo DOMÍNIO acessado, e a comunicação ganha confidencialidade e integridade (RFC 9110, seção 4.2.2: "secured" significa que "the server has been authenticated as acting on behalf of the identified authority" e que a comunicação tem "confidentiality and integrity protection"). O que o HTTPS NÃO garante: que o domínio seja o da instituição que o usuário pretendia acessar, nem que o titular do site aja de boa-fé. Um golpista pode registrar domínio parecido (com letras trocadas) e obter certificado válido para ESSE domínio, e o cadeado aparecerá. Logo, "tem https/cadeado, então é o site verdadeiro" é pegadinha frequente, e "o HTTPS não oferece autenticação alguma" também é erro. Conferir o domínio completo (letra a letra), não ignorar alertas de certificado do navegador e conferir o canal pelo qual o link chegou.
Fonte: o restante é conceito geral.

### 4.3.5 EXEMPLO APLICADO AO LEGISLATIVO
PHISHING: um servidor do Derep (antigo DETAQ) recebe e-mail, aparentemente da Central de Atendimento de TI, avisando que "a senha vence em duas horas" e trazendo um link para "atualizar" a credencial. O link leva a página idêntica à de login da Casa. Quem digita a senha a entrega ao golpista (confidencialidade). Resposta: não clicar, digitar o endereço oficial e comunicar a área de segurança. PHARMING: o mesmo servidor digita corretamente o endereço do portal e, por estar com o servidor DNS do roteador doméstico adulterado, vê página falsa quase idêntica; como ele digitou o domínio verdadeiro, o servidor falso, em regra, não consegue apresentar certificado válido para esse domínio: o navegador tende a exibir alerta de certificado, ou a página aparece sem conexão segura. São sinais que não podem ser ignorados (desconfiar de site de banco ou comércio sem conexão segura e verificar se o certificado apresentado corresponde ao do site verdadeiro). Lição: o ataque não depende de link recebido; o cadeado comprova o domínio, não a boa-fé de quem o registrou.

### 4.3.6 PEGADINHAS PROVÁVEIS (ITEM 4.3)
P1. "O pharming consiste no envio de mensagens que induzem a vítima a clicar em link, sem alterar a resolução de nomes" → ERRADO (o pharming redireciona a navegação por adulteração da resolução de nomes).
P2. "No phishing, o redirecionamento ocorre pela adulteração do DNS, e o pharming é o envio de mensagem falsa" → ERRADO (trocado).
P3. "No pharming, o usuário só é levado ao site falso se clicar em link recebido" → ERRADO.
P4. "O uso de HTTPS comprova que o site é legítimo" → ERRADO.
P5. "O phishing é um ataque exclusivamente técnico, que independe da ação do usuário" → ERRADO (engenharia social).
P6. "Mensagem com a logomarca do banco e boa redação é prova de autenticidade" → ERRADO.
P7. "O antivírus elimina por completo o risco de phishing" → ERRADO.
P8. "O phishing só funciona quando a vítima digita dados em página falsa; não envolve instalação de código malicioso" → ERRADO.
```

## Pares

- **LAN** × **WAN** — área geográfica restrita (sala, edifício, campus) | áreas geograficamente distantes (cidades, países); a Internet é a maior | Troca: inverter as duas definições.
- **Internet** × **Web** — rede mundial de redes (infraestrutura, TCP/IP) | serviço sobre a Internet (páginas, HTTP/HTTPS) | Troca: tratá-las como sinônimos ou chamar a Web de rede.
- **Internet** × **intranet × extranet** — aberta e mundial | privada, uso interno, acesso restrito, mesmas tecnologias | extensão controlada para parceiros e fornecedores autorizados | Troca: dizer que a intranet "não usa TCP/IP nem navegador"; trocar intranet e extranet.
- **Switch** × **roteador** — interliga equipamentos da mesma LAN | interliga redes diferentes e escolhe a rota | Troca: atribuir ao switch a função do roteador.
- **DNS** × **DHCP** — traduz nomes de domínio em endereços IP | atribui automaticamente endereços IP aos equipamentos | Troca: inverter as funções.
- **TCP** × **UDP** — entrega confiável, ordenada, com controle de erros | entrega sem essas garantias, com menor atraso | Troca: atribuir a garantia ao UDP.
- **Navegador** × **mecanismo de busca** — programa cliente que acessa e exibe páginas | serviço que indexa páginas e as localiza por palavras-chave | Troca: tratá-los como o mesmo aplicativo.
- **Confidencialidade** × **integridade × disponibilidade** — só quem é autorizado acessa | sem alteração indevida (exata e completa) | acessível quando necessária | Troca: deslocar as definições (integridade como "estar disponível"; disponibilidade como "só autorizados acessam").
- **Backup completo** × **incremental × diferencial** — copia tudo | copia o que mudou desde o último completo ou incremental e marca os arquivos; restaura com o completo + todos os incrementais | não marca os arquivos; numa rotina de completo + diferenciais, acumula o que mudou desde o completo; restaura com o completo + o último diferencial | Troca: atribuir ao diferencial a restauração em cadeia do incremental, ou ao incremental o acúmulo do diferencial. Cuidado: "diferencial = desde o último completo ou incremental" é a definição da Microsoft, não erro.
- **Backup** × **sincronização** — guarda pontos no tempo, com retenção, em local diferente | espelha o estado atual (exclusões e criptografias se replicam) | Troca: "sincronizar a pasta equivale a ter backup" ou "backup no mesmo disco basta".
- **Vírus** × **worm** — precisa de hospedeiro e de execução; pode circular por e-mail, mas não se autoexecuta | independente; propaga-se automaticamente pelas redes, explorando vulnerabilidades | Troca: atribuir ao worm o hospedeiro e ao vírus a autopropagação pela rede.
- **Vírus** × **trojan** — propaga-se inserindo cópias de si | parece legítimo e executa também funções maliciosas; não se replica | Troca: dizer que o trojan se replica automaticamente.
- **Spyware** × **ransomware** — monitora e envia informações a terceiros (confidencialidade) | bloqueia dados e cobra resgate (disponibilidade) | Troca: dizer que o ransomware "apenas exibe propaganda" ou que o spyware cobra resgate.
- **Antivírus** × **firewall** — olha arquivos e programas; detecta e remove malware | olha o tráfego; permite ou bloqueia conexões por regras | Troca: inverter as funções; "com firewall ativo, o antivírus é dispensável".
- **Firewall** × **antispyware** — controle de tráfego por regras | detecção e remoção de programas espiões | Troca: atribuir ao antispyware a filtragem de tráfego.
- **Phishing** × **pharming** — fraude que induz a vítima a fornecer dados, em regra por mensagem e link falso (engenharia social) | tipo específico de phishing que redireciona a navegação para site falso por adulteração da resolução de nomes | Troca: atribuir ao pharming o envio de mensagem com link e ao phishing o redirecionamento por DNS; dizer que o pharming exige clique em link.
- **HTTPS** × **legitimidade do site** — conexão cifrada, com o servidor autenticado para o domínio acessado (certificado) | o domínio ser o da instituição pretendida e o titular agir de boa-fé | Troca: "HTTPS ou cadeado prova que o site é o verdadeiro" (errado) ou "HTTPS não oferece autenticação alguma" (errado).
- **Quarentena** × **exclusão** — isola o arquivo suspeito, que pode ser restaurado ou excluído | remove definitivamente o arquivo | Troca: tratar quarentena como exclusão definitiva.

## Pegadinhas

- [P1-2] **Redes de computadores** — "A LAN interliga redes situadas em países distintos; a WAN restringe-se a um edifício" → ERRADO (invertido: LAN = área restrita; WAN = área distante).
- [P1-2] **Redes de computadores** — "O switch interliga redes diferentes e escolhe a rota entre elas" → ERRADO (isso é o roteador; o switch interliga equipamentos da mesma LAN).
- [P1-2] **Redes de computadores** — "O protocolo UDP garante a entrega ordenada e confiável dos dados" → ERRADO (garantias são do TCP).
- [P1-2] **Redes de computadores** — "Endereço IP privado é, por definição, protegido contra qualquer ataque" → ERRADO (privado = uso interno).
- [P1-2] **Redes de computadores** — "O DHCP traduz nomes de domínio em endereços IP" → ERRADO (isso é o DNS; DHCP atribui endereços).
- [P1-2.1] **Conceitos básicos, ferramentas, aplicativos e procedimentos de Internet e intranet** — "A intranet é uma rede que não pode usar TCP/IP nem navegador, por ser de uso interno" → ERRADO (usa as mesmas tecnologias da Internet; o que a distingue é o acesso restrito).
- [P1-2.1] **Conceitos básicos, ferramentas, aplicativos e procedimentos de Internet e intranet** — "Intranet é a mesma coisa que extranet" → ERRADO (a extranet estende o acesso, de modo controlado, a parceiros externos).
- [P1-2.1] **Conceitos básicos, ferramentas, aplicativos e procedimentos de Internet e intranet** — "A extranet é a rede interna acessível só a empregados; a intranet é a aberta a parceiros" → ERRADO (invertido).
- [P1-2.1] **Conceitos básicos, ferramentas, aplicativos e procedimentos de Internet e intranet** — "Internet e Web são sinônimos" → ERRADO (a Web é um serviço sobre a Internet).
- [P1-2.1] **Conceitos básicos, ferramentas, aplicativos e procedimentos de Internet e intranet** — "A janela de navegação anônima impede o provedor de Internet de saber quais sites o usuário visita" → ERRADO.
- [P1-2.1] **Conceitos básicos, ferramentas, aplicativos e procedimentos de Internet e intranet** — "O DNS atribui automaticamente endereços IP aos equipamentos" → ERRADO (DHCP).
- [P1-2.1] **Conceitos básicos, ferramentas, aplicativos e procedimentos de Internet e intranet** — "Endereços da faixa 192.168.0.0 a 192.168.255.255 são públicos e identificam um único equipamento na Internet" → ERRADO (faixa privada, RFC 1918).
- [P1-2.1] **Conceitos básicos, ferramentas, aplicativos e procedimentos de Internet e intranet** — "O navegador e o mecanismo de busca são o mesmo programa" → ERRADO.
- [P1-4.1] **Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais** — "A integridade garante que a informação esteja disponível ao usuário autorizado sempre que necessária" → ERRADO (isso é disponibilidade; integridade = não alteração indevida).
- [P1-4.1] **Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais** — "A disponibilidade assegura que a informação só seja acessada por quem está autorizado" → ERRADO (isso é confidencialidade).
- [P1-4.1] **Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais** — "Numa rotina de completo + diferenciais, a restauração exige o completo e todos os diferenciais posteriores" → ERRADO (basta o completo e o último diferencial).
- [P1-4.1] **Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais** — "Para restaurar com backups incrementais, basta o último incremental" → ERRADO (é preciso o completo e todos os incrementais em sequência).
- [P1-4.1] **Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais** — "O backup completo copia apenas o que mudou" → ERRADO.
- [P1-4.1] **Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais** — "Manter a cópia no mesmo disco do original é suficiente para recuperar dados em caso de falha desse disco" → ERRADO.
- [P1-4.1] **Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais** — "O worm depende de um arquivo hospedeiro e da ação do usuário para se propagar" → ERRADO (isso descreve o vírus).
- [P1-4.1] **Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais** — "O trojan se replica automaticamente pela rede" → ERRADO (não se replica; depende de o usuário executá-lo).
- [P1-4.1] **Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais** — "Sincronizar uma pasta na nuvem equivale a ter backup, em qualquer situação" → ERRADO.
- [P1-4.1] **Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais** — "O ransomware é um programa que apenas exibe propagandas indesejadas" → ERRADO (isso é adware, um tipo de spyware no uso comum; ransomware bloqueia dados e cobra resgate).
- [P1-4.1] **Segurança da informação: procedimentos de cópia de segurança (backup), noções de vírus, worms e pragas virtuais** — "Pagar o resgate assegura a recuperação dos dados" → ERRADO.
- [P1-4.2] **Programas de proteção (antivírus, firewall, antispyware)** — "O firewall é o programa destinado a detectar e remover códigos maliciosos instalados; o antivírus controla o tráfego" → ERRADO (funções invertidas).
- [P1-4.2] **Programas de proteção (antivírus, firewall, antispyware)** — "O antivírus atualizado detecta todos os códigos maliciosos, inclusive os desconhecidos" → ERRADO (nenhum antivírus é infalível).
- [P1-4.2] **Programas de proteção (antivírus, firewall, antispyware)** — "Com um firewall ativo, não é necessário antivírus" → ERRADO.
- [P1-4.2] **Programas de proteção (antivírus, firewall, antispyware)** — "O antispyware serve para filtrar o tráfego conforme regras de acesso" → ERRADO (função do firewall).
- [P1-4.2] **Programas de proteção (antivírus, firewall, antispyware)** — "O firewall impede que o usuário seja vítima de phishing" → ERRADO.
- [P1-4.2] **Programas de proteção (antivírus, firewall, antispyware)** — "O antivírus funciona sem necessidade de atualização" → ERRADO.
- [P1-4.2] **Programas de proteção (antivírus, firewall, antispyware)** — "Quarentena é a exclusão definitiva do arquivo suspeito" → ERRADO (isola o arquivo; pode ser restaurado ou excluído).
- [P1-4.3] **Ameaças digitais (phishing, pharming)** — "O pharming consiste no envio de mensagens que induzem a vítima a clicar em link, sem alterar a resolução de nomes" → ERRADO (o pharming redireciona a navegação por adulteração da resolução de nomes).
- [P1-4.3] **Ameaças digitais (phishing, pharming)** — "No phishing, o redirecionamento ocorre pela adulteração do DNS, e o pharming é o envio de mensagem falsa" → ERRADO (trocado).
- [P1-4.3] **Ameaças digitais (phishing, pharming)** — "No pharming, o usuário só é levado ao site falso se clicar em link recebido" → ERRADO.
- [P1-4.3] **Ameaças digitais (phishing, pharming)** — "O uso de HTTPS comprova que o site é legítimo" → ERRADO.
- [P1-4.3] **Ameaças digitais (phishing, pharming)** — "O phishing é um ataque exclusivamente técnico, que independe da ação do usuário" → ERRADO (engenharia social).
- [P1-4.3] **Ameaças digitais (phishing, pharming)** — "Mensagem com a logomarca do banco e boa redação é prova de autenticidade" → ERRADO.
- [P1-4.3] **Ameaças digitais (phishing, pharming)** — "O antivírus elimina por completo o risco de phishing" → ERRADO.
- [P1-4.3] **Ameaças digitais (phishing, pharming)** — "O phishing só funciona quando a vítima digita dados em página falsa; não envolve instalação de código malicioso" → ERRADO.
