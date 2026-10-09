# lote6_conferencia.md — T-04 — 2026-10-09 — gerado por gcb-cqfp

REMETENTE: GCB-CQFP — Coordenação QA, Fontes e Proveniência (conhecimentos básicos). Não produziu nem revisou antes estes lotes.
DESTINATÁRIO: GCB — Gerência de Conhecimentos Básicos (item a de .claude/agents/gcb-gerencia.md: conferência de aplicação e amostragem de 5 fontes por lote; com CONFERIDO, a GCB emite o gatilho A).
Objeto: Lotes 6a e 6b (P1, TI e Dados, itens 1 a 4; D-ESCOPO-2), produzidos pela EXEC e revisados por QA automatizado (Opus) em 08/10/2026.
Arquivos conferidos (somente leitura): saida/gcb/GCB_Lotes6_especificacao_PRES-S.md; GCB_Lote6a_v2_producao_auto.md; GCB_Lote6a_parecer_QA_R1_auto.md; GCB_Lote6b_v2_producao_auto.md; GCB_Lote6b_parecer_QA_R1_auto.md. Conferi que o espelho do Projeto (GCB/Lote6a_v2_producao_auto.md) tem o mesmo texto que saida/gcb.

## 0. Método e limites

- Regras aplicadas: CLAUDE.md, DECISOES.md (D-ESCOPO-2, D-CANONICOS, D-LEI-15352, D-REVERIFICACAO-JAN), regras/ (estilo_banca v1.0, semente, proveniência, padrão de resposta, contrato), protocolo EXEC e checklist do papel gcb-cqfp.
- Conferência de aplicação: cada apontamento dos pareceres R1 e das conferências de aplicação foi comparado com o texto da v2. Também conferi as alterações feitas depois da conferência de aplicação (6a: R-7, título e ATRIB; 6b: AJ-1 e AJ-2), que ninguém tinha conferido até agora. Não reescrevi nada.
- Escopo literal: o texto dos itens 1 a 4 de "TECNOLOGIA DA INFORMAÇÃO E DADOS" (edital 14.2.3) foi conferido contra o PDF do edital no Projeto ("Edital - Camara 2026.pdf"). Confere, palavra por palavra, com a especificação e com o cabeçalho dos dois lotes. Também conferem 7.1 (P1 = 90 itens), 8.11.2, 8.11.5 "a" (18,00) e 9.1.
- Fontes: baixei por acesso direto (curl, HTTP 200), em 09/10/2026, para /tmp/claude-0/-home-claude/3cf5e5a2-0a00-52ee-a3d1-ce0f04412748/scratchpad/t04/. Converti para texto com extração de HTML e pdftotext e procurei os trechos citados. Diferente do R1 (WebFetch, com paráfrase), esta leitura é do conteúdo bruto da página. As aspas abaixo são literais da página baixada.
- Divergência do checklist do papel com a especificação PRES-S: o checklist fala em "10 [TS]" e em "tabela dos 20 itens"; a especificação dos Lotes 6 fixa 15 itens e 7 ou 8 [TS]. Prevalece a especificação, que é a ordem específica destes lotes, e o veredito usa tabelas de 15 itens. Não gera apontamento.
- Critério de "item com problema": item cujo enunciado, gabarito ou d-G (justificativa que vai à plataforma) precise de alteração antes do gatilho A.

---

## 1. LOTE 6a — TI-FERRAMENTAS (itens 1 e 3)

### 1.1 Conferência de aplicação do parecer QA R1

| Apontamento | Onde, na v2 | Resultado |
|---|---|---|
| O-1 (6A-02: "células adjacentes") | item (l. 345); d-G (l. 367); curso 1.1.3, 1ª frase (l. 103); resumo 1.1 (l. 303) | ATENDIDO. Texto idêntico ao do parecer nos quatro lugares. |
| O-2 (6A-03: "estilo de título, como o Título 1") | item (l. 346); d-G (l. 368); curso 1.1.4 (l. 107); P5 1.1.6 (l. 118); resumo 1.1 | ATENDIDO. Idêntico nos cinco lugares. |
| O-3 (6A-09: um único ponto) | item (l. 352); d-G (l. 374); curso 1.4.2, 1º marcador (l. 188) | ATENDIDO. Idêntico. O ponto "interromper o compartilhamento" ficou só no curso e no resumo. |
| R-1 ("Três recursos") | curso 1.1.1 (l. 88) | ATENDIDO. |
| R-2 (P6, "Atualizar Campo") | curso 1.1.6 P6 (l. 119) | ATENDIDO. |
| R-3 (RFC 9051 × SMTP) | curso 3.1.2, IMAP4 (l. 223) | ATENDIDO. |
| R-4 (exemplo 3.1.4; definição de cliente) | curso 3.1.4 (l. 233); 3.1.1 (l. 218) | ATENDIDO. Há uma leve redundância em 3.1.1, já aceita pelo R1. |
| R-5 (Meet: "Adicionar videoconferência do Google Meet") | curso 3.3.2 (l. 276); P3 3.3.5 (l. 290); resumo 3.3 (l. 309) | ATENDIDO. |
| R-6 (Ressalva de método; Tabela de Correções) | l. 14; l. 16–28 | ATENDIDO, com variação justificada: a v2 atribui a conferência de aspas ao "QA automatizado (Opus) ... conduzido pela PRES-S", e não à GCB-CQFP (linha ATRIB). Essa atribuição corresponde aos fatos: esta T-04 é a primeira conferência da gcb-cqfp sobre os Lotes 6. |
| R-7 (curso 3.3.4), aplicada depois da conferência de aplicação | l. 285 | ATENDIDO. Texto idêntico à redação substitutiva. Registrado na Tabela de Correções. |
| Título (linha 1 em "v2"), observação de forma | l. 1 | ATENDIDO. |
| Contagens após correções (parecer, seção 7) | linha "Contagem" (l. 364), recontada item a item | ATENDIDO. 15 itens; 7 C / 8 E; 8 [TS] (2 C, 6 E); 5 VOLÁTEIS; Word 3, Excel 3, PowerPoint 2, OneDrive 2, item 3 = 5. |

Resultado: 11 de 11 apontamentos ATENDIDOS. Nenhum NÃO ATENDIDO e nenhum PARCIAL.

### 1.2 Aderência à especificação PRES-S

| Requisito | Situação |
|---|---|
| Escopo literal do edital (itens 1 e 3) | OK. Conferido contra o PDF do edital. |
| Cabeçalho: dados da P1, Tabela de Correções, FONTES com URL e "verificado em 08/10/2026" | OK |
| Curso item a item (definição, conceitos, exemplo legislativo com Derep, pegadinhas) | OK (1.1 a 1.4 e 3.1 a 3.3) |
| Resumo com NOTA 8.11.2 | OK. Texto conforme o edital. |
| Pares confundíveis (mínimo 12) | OK (19) |
| 15 itens AUTORAL, numerados 6A-01 a 6A-15, com comando "Acerca de ..., julgue os itens ..." | OK |
| Distribuição: Word 3, Excel 3, PowerPoint 2, OneDrive 2; item 3 = 5, cobrindo webmail × cliente (6A-11), Teams (6A-14) e Meet (6A-15) | OK |
| Entre 6 e 9 C | OK (7 C = 46,7%, dentro da faixa de 45 a 60% de estilo_banca) |
| 7 ou 8 [TS] | OK (8) |
| VOLÁTIL ≤ 6 e corretamente marcado | OK (5: 01, 09, 10, 14, 15) |
| Nenhum item com preço, licença, plano, limite, versão ou atalho | OK |
| Nenhum item atribui afirmação a fornecedor; sem CEBRASPE_ESTILO; sem estratégia de marcação | OK |
| Itens fora de escopo | Nenhum |
| Marcadores FIM DA PARTE 1/3, 2/3, 3/3 e FIM DO LOTE 6a | OK |

### 1.3 Amostragem de 5 fontes (verificado em 09/10/2026)

Critério de escolha: as fontes dos 5 itens VOLÁTEIS, que são afirmações sobre produto e as de maior risco.

| Fonte | Item | Oficial? | Abriu? | Sustenta a afirmação como escrita? (trecho literal da página) |
|---|---|---|---|---|
| F1 support.microsoft.com/pt-br/word/accept-or-reject-tracked-changes-in-word | 6A-01 (E) | Sim (Microsoft) | Sim (200) | SIM. "A escolha do modo de exibição Sem Marcação oculta as alterações apenas temporariamente. Eles ficarão visíveis novamente na próxima vez que alguém abrir o documento." e "Para remover alterações controladas, você deve aceitá-las ou rejeitá-las." Também está o Inspetor de Documentos ("verifica se há alterações controladas e comentários, texto oculto..."). |
| F9 support.microsoft.com/pt-br/office/colaborar-no-microsoft-onedrive-... | 6A-09 (C) | Sim (Microsoft) | Sim (200, com REDIRECIONAMENTO para support.microsoft.com/pt-br/onedrive/collaborate-in-microsoft-onedrive-sharing-editing-and-managing-files; título igual) | SIM. "Selecione Permitir edição se quiser que outras pessoas possam editá-lo." / "Desmarque Permitir edição se quiser que outras pessoas possam apenas visualizar o arquivo." Também "Se você for o proprietário do arquivo ou tiver permissões de edição, pode parar o compartilhamento ou alterar as permissões." (curso 1.4.2) e "Pode editar"/"Pode exibir". |
| F11 support.microsoft.com/pt-br/onedrive/restore-a-previous-version-of-a-file-stored-in-onedrive | 6A-10 (E) | Sim (Microsoft) | Sim (200) | SIM. "A versão do documento selecionado torna-se a versão atual. A versão atual anterior torna-se a versão anterior na lista." Também "funciona com todos os tipos de ficheiros", "o administrador poderá ter desativado o controlo de versões" e "só pode restaurar um ficheiro de cada vez". O prazo de retenção numérico aparece na página e, corretamente, não é cobrado. |
| F18 learn.microsoft.com/pt-br/microsoftteams/teams-channels-overview | 6A-14 (C) | Sim (Microsoft Learn; "Última atualização em 2026-08-22") | Sim (200) | SIM, de forma literal. "Os canais podem ser abertos para todos os membros da equipe (canais padrão), membros da equipe selecionados (canais privados) ou pessoas selecionadas dentro e fora da equipe (canais compartilhados)." Também "As equipes são coleções de pessoas, conteúdo e ferramentas..." |
| F20 support.google.com/meet/answer/9308856?hl=pt-br | 6A-15 (C) | Sim (Google) | Sim (200) | SIM. "Você pode apresentar uma guia, uma janela específica ou a tela inteira em uma reunião." / "Selecione Uma guia, Uma janela ou A tela inteira." Confere também o curso 3.3.3 (áudio da guia do Chrome por padrão; "Compartilhar também o áudio do sistema"; restrição por administrador ou organizador). |

Resultado: 5 de 5 fontes oficiais abriram e sustentam a afirmação. Nenhuma fonte não oficial. Observação para a fila de janeiro (FV, D-REVERIFICACAO-JAN): a URL da F9 hoje redireciona para outro endereço da Microsoft; na reverificação de 4 a 8/1/2027, registrar a URL final.

### 1.4 Checklist do papel por amostragem

- Correção conceitual (conferida em todos os 15): nenhum gabarito discutível. 6A-04 (B$2 fixa a linha), 6A-06 (omitido = aproximada), 6A-12 (POP3 × IMAP4 trocados) e 6A-13 (Cco) estão corretos e ancorados (F4, F6, F14, F12, lidas pelo R1).
- Estilo Cebraspe: comandos "Acerca de ..., julgue os itens"; afirmação única por item (O-3 resolveu o único caso de dois pontos); mecanismos coerentes com estilo_banca (E1 troca de conceito, E2 inversão, C3 em 6A-03); proporção de 7 C em 15.
- Normativo: o lote não cita lei. A NOTA 8.11.2 remete ao edital e confere com ele. Não se aplica PENDENTE.
- Fonte datada: toda afirmação de produto traz F1–F22 com "verificado em 08/10/2026". O que não tem fonte está marcado como "conceito geral" e não é afirmação de ferramenta (ex.: "compartilhar não transfere a propriedade").

| Item | Gab. | [TS] | VOLÁTIL | Subitem | Veredito CQFP |
|---|---|---|---|---|---|
| 6A-01 | E | sim | sim | 1.1 | APROVADO (F1 aberta hoje) |
| 6A-02 | C | — | — | 1.1 | APROVADO |
| 6A-03 | C | sim | — | 1.1 | APROVADO |
| 6A-04 | E | sim | — | 1.2 | APROVADO |
| 6A-05 | C | sim | — | 1.2 | APROVADO |
| 6A-06 | E | sim | — | 1.2 | APROVADO |
| 6A-07 | C | — | — | 1.3 | APROVADO |
| 6A-08 | E | — | — | 1.3 | APROVADO |
| 6A-09 | C | — | sim | 1.4 | APROVADO (F9 aberta hoje) |
| 6A-10 | E | sim | sim | 1.4 | APROVADO (F11 aberta hoje) |
| 6A-11 | E | — | — | 3.1 | APROVADO |
| 6A-12 | E | sim | — | 3.1 | APROVADO |
| 6A-13 | E | sim | — | 3.1 | APROVADO |
| 6A-14 | C | — | sim | 3.2 | APROVADO (F18 aberta hoje) |
| 6A-15 | C | — | sim | 3.3 | APROVADO (F20 aberta hoje) |

### 1.5 Observações não bloqueantes (PRÓXIMO; decisão da GCB)

- OB-6a-1 (estilo, viés de marcador): os 4 itens com possibilidade afirmativa ("pode", "pode optar", "pode definir", "pode incluir": 6A-03, 6A-09, 6A-14, 6A-15) são todos C, e nenhum E usa esse marcador. estilo_banca, seção 5, pede que o marcador não coincida sempre com o mesmo gabarito. Não altera gabarito; vale considerar na próxima edição.
- OB-6a-2 (forma): no curso 1.1.5 (l. 111), a grafia é "Derep, antigo DETAQ", e não "Derep (antigo DETAQ)". O sentido é o mesmo de D-DEREP.
- OB-6a-3 (FV): a URL da F9 redireciona (ver 1.3).

### 1.6 Veredito — Lote 6a

**CONFERIDO — pronto para o gatilho A da GCB.** Itens com problema: 0 de 15 (0%). Apontamentos do R1: 11 de 11 atendidos. Fontes amostradas: 5 de 5 ok.

---

## 2. LOTE 6b — TI-REDES-SEGURANCA (itens 2 e 4)

### 2.1 Conferência de aplicação do parecer QA R1

| Apontamento | Onde, na v2 | Resultado |
|---|---|---|
| O-1 (a) 6B-07 (rotina completo + diferenciais) | item (l. 369) | ATENDIDO. Idêntico. Revalidado contra a F12 aberta hoje (2.3). |
| O-1 (b)–(g) d-G 6B-07, curso 4.1.2, P3, C9, resumo 4.1, F12 | l. 393; 196–199; 228; 340; 322; 38 | ATENDIDO. Idêntico. |
| O-2 (a)–(e) 6B-13 passa a julgar o phishing; d-G; curso 4.3.1; P8; distribuição | l. 379; 399; 279; 304; 356 e 403 | ATENDIDO. Revalidado contra a F4, seção 2.3, aberta hoje (2.3). |
| O-3 (a)–(f) HTTPS: curso 4.3.4, 4.3.5, 2.0.6, C17, resumo 4.3 | l. 290–291; 294; 93; 348; 326 | ATENDIDO. Revalidado contra a RFC 9110, 4.2.2, aberta hoje (2.3). |
| R-1 (DNS confirmado; F13–F15; rodapé NÃO ABERTAS) | F4 (l. 30), 4.3.2, d-G 6B-09/10/11/14, l. 39–42 | ATENDIDO. |
| R-2 (vírus pode circular por e-mail; C11) | 4.1.4 (l. 209); C11 (l. 342) | ATENDIDO. |
| R-3 (6B-12 com um único ponto) | l. 376; d-G l. 398 | ATENDIDO. |
| R-4 (6B-15, nova redação) | l. 381; d-G l. 401 | ATENDIDO. |
| R-5 (governança digital sem item; BACKLOG ao QA Normativo) | 4.0.2; Tabela de Correções; nota de produção | ATENDIDO (registrado como BACKLOG). |
| R-6 (curso 4.1.1; tabela dos itens reais 96/98) | l. 188; l. 45–52 | ATENDIDO. Revalidado contra o caderno e o gabarito oficiais (2.4). |
| AJ-1 (trojan na lista do F4), aplicado depois da conferência de aplicação | F4 (l. 30) | ATENDIDO no F4. Resíduo de forma: a Nota de produção (i), na l. 403, ainda lista "tríade CIA, backdoor, rootkit, bot e antispyware" sem o trojan (OB-6b-3). |
| AJ-2 ("tentação" do d-G 6B-15), aplicado depois da conferência de aplicação | l. 401 | ATENDIDO. Idêntico à redação da QA. |
| Contagens (parecer, seção 8) | linha "Contagem" (l. 385), recontada | ATENDIDO. 15 itens; 7 C / 8 E; 8 [TS] (3 C, 5 E); 0 VOLÁTIL; 2 = 1, 2.1 = 4, 4.1 = 4, 4.2 = 3, 4.3 = 3. |

Resultado: 11 de 11 apontamentos ATENDIDOS (R-5 atendido como BACKLOG). Nenhum NÃO ATENDIDO e nenhum PARCIAL.

### 2.2 Aderência à especificação PRES-S

| Requisito | Situação |
|---|---|
| Escopo literal do edital (itens 2 e 4) | OK. Conferido contra o PDF do edital. |
| Cabeçalho, Tabela de Correções, FONTES datadas | OK. Forma: as linhas REMETENTE/DESTINATÁRIO vêm antes do título (l. 1–4), sem efeito. |
| Curso (com tríade CIA em 4.1), resumo com NOTA 8.11.2, pares (mínimo 12) | OK (18 pares) |
| 15 itens AUTORAL; item 2 = 5; item 4 = 10, com 4.1 = 4, 4.2 = 3 e 4.3 = 3 (mínimo 2 em cada) | OK |
| Governança digital: pelo menos 1 item "se houver base" | Sem item e sem base aberta. Conforme a especificação (R-5 em BACKLOG). |
| Entre 6 e 9 C; 7 ou 8 [TS]; 0 VOLÁTIL | OK (7 C = 46,7%; 8 [TS]; 0 VOLÁTIL) |
| Itens reais TRF6 96 (E) e 98 (C) em seção própria, CEBRASPE_ANALOGA, fora dos 15, sem transcrição, aderência parcial a 4/4.1 | OK. Ano no formato D-ANO: "TRF6 2024 (aplicação em 19/01/2025)". |
| Sem itens fora de escopo; sem atribuição a fornecedor; sem CEBRASPE_ESTILO | OK |
| Marcadores FIM DA PARTE 1/3, 2/3, 3/3 e FIM DO LOTE 6b | OK |

### 2.3 Amostragem de 5 fontes (verificado em 09/10/2026)

Critério de escolha: as fontes dos três itens reescritos pelo R1 (6B-07, 6B-13, 6B-15), do item com pedido especial (6B-14) e das definições de malware com citação literal no d-G.

| Fonte | Itens | Oficial? | Abriu? | Sustenta a afirmação como escrita? (trecho literal) |
|---|---|---|---|---|
| F12 learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc784306(v=ws.10) | 6B-07 (E); curso 4.1.2; C9 | Sim (Microsoft Learn, conteúdo arquivado) | Sim (200) | SIM. "If you are performing a combination of normal and differential backups, restoring files and folders requires that you have the last normal as well as the last differential backup." As duas definições citadas ("since the last normal or incremental backup", para o diferencial e para o incremental) são literais. O 6B-07 (E) se sustenta. |
| F11 rfc-editor.org/rfc/rfc9110, seção 4.2.2 | 6B-15 (C); curso 4.3.4; 2.0.6; C17 | Sim (IETF) | Sim (200) | SIM. "'secured' specifically means that the server has been authenticated as acting on behalf of the identified authority and all HTTP communication with that server has confidentiality and integrity protection". Também "a stateless application-level protocol" (l. 93). A correção O-3 está conceitualmente correta. |
| F4 cartilha.cert.br/livro/cartilha-seguranca-internet.pdf, seções 2.3, 2.3.1 e 4.1 | 6B-13 (E); 6B-14 (C); 6B-09 (d-G); curso 4.1.3, 4.3.1, 4.3.2; resumo 4.1 | Sim (CERT.br/NIC.br) | Sim (200; PDF lido por inteiro) | CONTEÚDO: SIM. 2.3: o phishing tenta induzir o usuário a fornecer dados "por meio do acesso a páginas falsas [...]; da instalação de códigos maliciosos, projetados para coletar informações sensíveis; e do preenchimento de formulários", o que sustenta o 6B-13 (E). 2.3.1: "Pharming é um tipo específico de phishing que envolve a redireção da navegação do usuário para sites falsos, por meio de alterações no serviço de DNS (Domain Name System). Neste caso, quando você tenta acessar um site legítimo, o seu navegador Web é redirecionado, de forma transparente, para uma página falsa", o que sustenta o 6B-14 (C). LITERALIDADE: PROBLEMA (apontamento A-6b-1). O original traz "de um usuário" (2.3) e "se propaga inserindo cópias de si mesmo" (4.1). O lote cita "usuario [sic]" e "copias [sic]"/"copias", ou seja, reproduz como erro da fonte uma perda de acento da extração do PDF, que a própria F4 do lote reconhece ("a extração do PDF corrompe os acentos"). |
| F13 cartilha.cert.br/fasciculos/codigos-maliciosos/fasciculo-codigos-maliciosos.pdf | 6B-09 (E); 6B-11 (C); curso 4.1.3, 4.2.1 | Sim (CERT.br) | Sim (200) | SIM (a extração separa a letra capitular). Worm: "[P]ropaga-se automaticamente pelas redes, explorando vulnerabilidades nos sistemas e aplicativos instalados". Spyware: "[P]rojetado para monitorar as atividades de um sistema e enviar as informações coletadas para terceiros." Vírus: "Propaga-se enviando cópias de si mesmo por e-mails e mensagens." Antivírus: "[A]ntivírus é nome popular para ferramentas antimalware". Antispyware: não mencionado, como o lote declara. |
| F2 cartilha.cert.br/ransomware/ | 6B-08 (C) | Sim (CERT.br) | Sim (200) | SIM. "Ransomware é um tipo de código malicioso que torna inacessíveis os dados armazenados em um equipamento, geralmente usando criptografia, e que exige pagamento de resgate" e "Fazer backups regularmente também é essencial para proteger os seus dados". |

Resultado: 5 de 5 fontes oficiais abriram e sustentam o conteúdo dos itens. Uma delas (F4) tem problema de literalidade na transcrição feita pelo lote, que é o apontamento A-6b-1. Nenhuma fonte não oficial.

### 2.4 Itens reais TRF6 2024 (CEBRASPE_ANALOGA): conferência por acesso direto (extra à amostra)

- Caderno oficial https://cdn.cebraspe.org.br/concursos/trf6_24/arquivos/034_TRF6_002_01.PDF: abriu (200; 4 páginas), lido por extração direta (pdftotext -raw). Comando: "Julgue os itens a seguir, a respeito da segurança da informação e dos vários tipos de ataques e suas características." Item 96: integridade descrita como garantia de que dado ou informação "tenham sido alterados sem o registro da ação correspondente, mesmo sob necessidade de auditoria". Item 98: disponibilidade como garantia de "acessar sistemas e(ou) informações quando necessário, mesmo que o sistema ou a infraestrutura esteja sob pressão". Os pontos de julgamento registrados no lote CONFEREM.
- Gabarito definitivo oficial https://cdn.cebraspe.org.br/concursos/trf6_24/arquivos/GAB_DEFINITIVO_034_TRF6_002_01.PDF: abriu (200). "CARGO 2: ANALISTA JUDICIÁRIO – ÁREA: APOIO ESPECIALIZADO – ESPECIALIDADE: ANÁLISE DE DADOS". 96 = E; 98 = C; anulados 58, 105 e 117. CONFERE.
- Isso cumpre a nota da especificação ("ponto de julgamento a preencher pela GCB-CQFP contra o caderno oficial"). A pendência de BACKLOG "conferência visual humana do PDF" foi atendida por extração direta do PDF oficial, não por leitura humana. Cabe à GCB (D1) decidir se a dá por cumprida.

### 2.5 Checklist do papel por amostragem

- Correção conceitual (conferida em todos os 15): nenhum gabarito discutível. Pontos de risco revalidados: 6B-07 (F12), 6B-13 (F4 2.3), 6B-14 (F4 2.3.1), 6B-15 (RFC 9110 4.2.2). O curso corrigido pela O-3 está alinhado com a própria Cartilha, cuja 2.3 diz: "Caso a página falsa utilize conexão segura, um novo certificado será apresentado e, possivelmente, o endereço mostrado no navegador Web será diferente".
- Estilo Cebraspe: comandos corretos; uma afirmação por item (6B-08 e 6B-11 são compostos, com as duas partes verdadeiras, risco aceito no R1); 6B-12 usa a generalização "todos" como mecanismo E (estilo_banca, traço de termo absoluto; uso legítimo); C3 presente (6B-02, 6B-15). O 6B-06 trata da tríade com o par integridade × disponibilidade, que não é o par do item real 96 (integridade × alteração sem registro). Não há cópia de moldura.
- Normativo: o curso 4.0.2 (l. 171) menciona a "Lei 14.129/2021 (Governo Digital)" sem artigo, numa nota dirigida à GCB-CQFP dentro do curso. Ela não fundamenta item nem afirma conteúdo normativo, e o Lote 4 v3 já a cita com artigo (art. 2º, I) e conferência. Por isso não a marco PENDENTE normativo. Mas é nota interna em texto que vai à candidata: ver OB-6b-1.
- Fonte datada: afirmações sobre ferramenta (F5, firewall do Windows; F12) trazem data e URL oficial. Redes e segurança estão como "conceito geral", o que a especificação permite.

| Item | Gab. | [TS] | Subitem | Veredito CQFP |
|---|---|---|---|---|
| 6B-01 | E | — | 2 | APROVADO |
| 6B-02 | C | sim | 2.1 | APROVADO |
| 6B-03 | E | sim | 2.1 | APROVADO |
| 6B-04 | C | — | 2.1 | APROVADO |
| 6B-05 | C | — | 2.1 | APROVADO |
| 6B-06 | E | sim | 4.1 | APROVADO |
| 6B-07 | E | sim | 4.1 | APROVADO (F12 aberta hoje) |
| 6B-08 | C | — | 4.1 | APROVADO (F2 aberta hoje) |
| 6B-09 | E | — | 4.1 | PENDENTE. Item e gabarito corretos (F13 e F4 abertas hoje); o d-G (l. 395) cita a F4 de forma não literal ("copias"). Ver A-6b-1. |
| 6B-10 | E | sim | 4.2 | APROVADO |
| 6B-11 | C | — | 4.2 | APROVADO (F13 aberta hoje) |
| 6B-12 | E | — | 4.2 | APROVADO |
| 6B-13 | E | sim | 4.3 | APROVADO (F4 2.3 aberta hoje) |
| 6B-14 | C | sim | 4.3 | APROVADO (F4 2.3.1 aberta hoje) |
| 6B-15 | C | sim | 4.3 | APROVADO (RFC 9110 aberta hoje) |

### 2.6 Apontamento obrigatório (AGORA)

A-6b-1. Citação não literal da F4 em texto que vai à plataforma (regra de proveniência: citação literal do que foi lido). O original (PDF oficial, lido hoje) traz "usuário" e "cópias". O lote transcreve a perda de acento da extração como se fosse erro da fonte ("[sic]"). Ocorrências exatas a corrigir, sem outra mudança:
1. l. 30 (FONTES, F4): "de um usuario [sic]" → "de um usuário"; "inserindo copias de si mesmo" → "inserindo cópias de si mesmo".
2. l. 205 (curso 4.1.3): "inserindo copias de si mesmo [sic]" → "inserindo cópias de si mesmo".
3. l. 279 (curso 4.3.1): "de um usuario [sic]" → "de um usuário".
4. l. 322 (resumo 4.1): "inserindo copias de si mesmo" → "inserindo cópias de si mesmo".
5. l. 395 (d-G 6B-09): "inserindo copias de si mesmo" → "inserindo cópias de si mesmo".
Nenhum gabarito, [TS], VOLÁTIL ou contagem muda. Basta registrar a correção na Tabela de Correções (por exemplo, "CQFP-1"). Para conferir, basta comparar as cinco linhas.

### 2.7 Observações não bloqueantes (PRÓXIMO; podem entrar na mesma correção)

- OB-6b-1: curso 4.0.2 (l. 171). A frase "Observação para a GCB-CQFP: a Lei 14.129/2021 [...] não fundamenta item" é nota interna dentro do curso, que vai à candidata. Sugestão: levá-la para a Nota de produção ou retirá-la. Se a referência à lei ficar no curso, citar o artigo, como no Lote 4 (art. 2º, I).
- OB-6b-2 (forma): no curso 2.0.6 (l. 98), a grafia é "Derep, antigo DETAQ", e não "Derep (antigo DETAQ)".
- OB-6b-3 (forma): a Nota de produção (i), na l. 403, não inclui o trojan na lista de conceitos gerais, ao contrário do F4 (AJ-1).

### 2.8 Veredito — Lote 6b

**NÃO CONFERIDO.** Falta só a aplicação do A-6b-1: cinco substituições literais nas linhas 30, 205, 279, 322 e 395. Itens com problema: 1 de 15 (6,7%, o d-G do 6B-09); os demais trechos afetados são curso, resumo e cabeçalho, fora de item. Apontamentos do R1: 11 de 11 atendidos. Fontes amostradas: 5 de 5 abriram e sustentam o conteúdo, e 1 tem transcrição não literal (F4). Aplicado o A-6b-1, uma conferência restrita às cinco linhas basta para CONFERIDO, sem nova rodada de QA.

---

## 3. Síntese para a GCB

| Lote | Itens | Apontamentos R1 + pós-conferência | Fontes amostradas | Itens com problema | Veredito |
|---|---|---|---|---|---|
| 6a | 15 (7 C / 8 E; 8 [TS]; 5 VOLÁTEIS) | 11 atendidos / 0 não atendidos / 0 parciais | 5 ok / 0 problema | 0 (0%) | CONFERIDO: pronto para o gatilho A |
| 6b | 15 (7 C / 8 E; 8 [TS]; 0 VOLÁTIL) | 11 atendidos / 0 não atendidos / 0 parciais | 5 abriram e sustentam / 1 com literalidade a corrigir (F4) | 1 (6,7%) | NÃO CONFERIDO: falta o A-6b-1 |

Classificação:
- AGORA: A-6b-1 (correção mecânica pela produção; a ordem à EXEC vem da Presidência, conforme o protocolo EXEC, item 2).
- PRÓXIMO: OB-6a-1, OB-6a-2, OB-6b-1, OB-6b-2, OB-6b-3.
- BACKLOG mantido: R-5 do 6b (governança digital via QA Normativo).
- Decisão da GCB (D1): dar por cumprida, com base em 2.4, a conferência visual humana dos itens 96 e 98.
- FV de janeiro (D-REVERIFICACAO-JAN): 6A-01, 09, 10, 14 e 15. A URL da F9 hoje redireciona.

Nenhum lote passou de 30% de itens reprovados (6a: 0%; 6b: 6,7%). Não se aplica o gate.

---

## Rodada 2 — 2026-10-09 — gcb-cqfp

Objeto: conferência restrita da aplicação do A-6b-1 (errata textual da GCB, tabela CQFP-1.1 a CQFP-1.6 em saida/gcb/lote6_reconciliacao.md, seção 2) em saida/gcb/GCB_Lote6b_v2_producao_auto.md. Não foi feita nova rodada de QA de mérito. O lote não foi editado.

### R2.1 Diff (git diff, somente leitura, contra HEAD c15fa24)

- `git diff --numstat`: 5 inserções e 5 remoções. As linhas alteradas são exatamente 30, 205, 279, 322 e 395. O arquivo continua com 407 linhas.
- `git diff --word-diff`: as únicas palavras alteradas são "usuario [sic]" → "usuário" (l. 30 e 279), "copias" → "cópias" (l. 30, 205, 322 e 395) e "mesmo [sic]" → "mesmo" (l. 205). Nenhuma outra palavra mudou.
- Invariantes conferidos entre HEAD e a versão atual: as 16 linhas de gabarito `6B-NN. C/E` são idênticas (diff vazio); as ocorrências de [TS] são 13 nas duas versões; as de VOLÁTIL são 5 nas duas (nenhum item VOLÁTIL); a linha "Contagem" está inalterada (15 itens; 7 C e 8 E). Resíduos: "[sic]" passou de 3 para 0, "usuario" de 2 para 0 e "copias" de 4 para 0.

### R2.2 Confronto com o PDF oficial da F4

Fonte: https://cartilha.cert.br/livro/cartilha-seguranca-internet.pdf, baixada em 09/10/2026 (HTTP 200, application/pdf, 12.607.309 bytes, SHA-256 49ff9c78…757cab; "Cartilha de Segurança para Internet – Versão 4.0", CERT.br). O texto foi extraído com pdftotext e normalizado em Unicode NFC, e a comparação foi literal. No PDF não há ocorrência de "usuario" nem de "copias" sem acento.

| Linha | Trecho no lote (atual) | PDF oficial | Resultado |
|---|---|---|---|
| 30 (FONTES, F4, seção 2.3) | "o tipo de fraude por meio da qual um golpista tenta obter dados pessoais e financeiros de um usuário" | p. 25 do PDF, seção 2.3: "...é o tipo de fraude por meio da qual um golpista tenta obter dados pessoais e financeiros de um usuário, pela utilização combinada de..." | CONFERE |
| 30 (FONTES, F4, seção 4.1) | "programa ou parte de um programa de computador, normalmente malicioso, que se propaga inserindo cópias de si mesmo" | p. 40 do PDF, seção 4.1: "Vírus é um programa ou parte de um programa de computador, normalmente malicioso, que se propaga inserindo cópias de si mesmo e se tornando parte de..." | CONFERE |
| 205 (curso 4.1.3) | "programa ou parte de um programa de computador, normalmente malicioso, que se propaga inserindo cópias de si mesmo" (sem "[sic]") | idem, p. 40 | CONFERE |
| 279 (curso 4.3.1) | "o tipo de fraude por meio da qual um golpista tenta obter dados pessoais e financeiros de um usuário" (sem "[sic]") | idem, p. 25 | CONFERE |
| 322 (resumo 4.1) | "se propaga inserindo cópias de si mesmo" | idem, p. 40 | CONFERE |
| 395 (d-G 6B-09) | "se propaga inserindo cópias de si mesmo" | idem, p. 40 | CONFERE |

O corte das citações nas vírgulas ("usuário", "mesmo") não altera o sentido. Na l. 205, o complemento ("que se torna parte de outros programas e arquivos") aparece como paráfrase declarada, fora das aspas.

### R2.3 Atribuição indevida de erro à fonte

- Não há "[sic]", "usuario" nem "copias" em nenhuma parte do arquivo.
- A ressalva que resta na l. 30 ("a extração do PDF corrompe os acentos") atribui o defeito à extração, não à obra, e por isso está correta.
- Também foram confrontadas com o PDF as demais citações literais da F4 no lote: "por meio de alterações no serviço de DNS (Domain Name System)" (l. 30, 283 e 400; p. 27 do PDF) e "indisponibilidades ao alvo" (l. 187). As duas conferem literalmente.

### R2.4 Veredito final — Lote 6b

**CONFERIDO.** O A-6b-1 foi aplicado exatamente nas linhas 30, 205, 279, 322 e 395, sem outra alteração. Os cinco trechos reproduzem literalmente o PDF oficial da F4, e nenhuma atribuição indevida de erro à fonte permanece. Itens com problema: 0 de 15 (0%). Gabarito (7 C / 8 E), [TS] e contagem estão inalterados, com 0 VOLÁTIL. O Lote 6b está liberado para o gatilho A pela GCB. As observações OB-6b-1 a OB-6b-3 seguem como PRÓXIMO, não bloqueantes, e o R-5 segue em BACKLOG.
