# L6_reforco_onda1_v1.md — T-92 — 2026-10-18 — gerado por gcb-cpp

STATUS: NENHUM ITEM ENTRA. Nenhuma fonte oficial pôde ser aberta em 18/10/2026 (rede da sessão bloqueada: curl com "CONNECT tunnel failed, response 403"; WebFetch com "getaddrinfo ENOTFOUND" para www.rfc-editor.org, datatracker.ietf.org, cartilha.cert.br e www.gov.br). Pela D-REFORCO-2, regra 2 ("sem base, não entra"), a produção não grava item com "verificado em 18/10/2026" que não foi aberto. As Partes 2/3 e 3/3 ficam sem item. Abaixo, o mapa das folhas e as propostas de ponto, para a Gerência decidir (reexecutar com rede liberada ou autorizar base do pacote já verificada em 08/10/2026).

## PARTE 1/3 — Mapa

### 1.1 Itens novos (propostas NÃO verificadas; não entram)
| id | folha | ponto de julgamento (proposto) | formato | base pretendida (NÃO ABERTA hoje) | VOLÁTIL |
|---|---|---|---|---|---|
| L6A-R01 | P1-3 | O SMTP serve ao envio/transferência de mensagens entre cliente e servidor e entre servidores; POP3 e IMAP4 servem ao acesso do usuário à caixa postal | situação hipotética | RFC 5321, seção 1.1, https://www.rfc-editor.org/rfc/rfc5321 — NÃO ABERTA em 18/10/2026 | n (conceito estável) |
| L6B-R01 | P1-4.3 | Diante de mensagem com link que pede dados, a conduta correta é não usar o link e confirmar pelo canal oficial da instituição | aplicação parlamentar | Cartilha CERT.br, fascículo "Golpes: Evite Fraudes", https://cartilha.cert.br/fasciculos/golpes-evite-fraudes/fasciculo-golpes-evite-fraudes.pdf — NÃO ABERTA hoje | n |
| L6B-R02 | P1-4.3 | Relação entre os golpes: o pharming é espécie de phishing (não golpe sem relação) | par confundível | Cartilha CERT.br (livro), seção 2.3.1, https://cartilha.cert.br/livro/cartilha-seguranca-internet.pdf — lida em 08/10/2026 pela produção do Lote 6b (F4); NÃO REABERTA hoje | n |
Observação: o ponto de L6B-R02 toca o de 6B-14 (mecanismo DNS); redigir sem mencionar DNS ou clique. Gabarito sugerido para a onda: L6A-R01 C, L6B-R01 C, L6B-R02 E (2C/1E), a confirmar com a produção efetiva.

### 1.2 Itens existentes, P1-3 (5): pontos e formatos
| id | ponto | formato | VOLÁTIL |
|---|---|---|---|
| 6A-11 | webmail (navegador) × cliente (aplicativo) | par confundível | n |
| 6A-12 | comportamento padrão POP3 × IMAP4 quanto a remover mensagens | troca de sujeito | n |
| 6A-13 | Cco: recebe a cópia, endereço oculto | definição | n |
| 6A-14 | tipos de canal do Teams (padrão, privado, compartilhado) | definição | s |
| 6A-15 | Meet: apresentar guia, janela ou tela | definição | s |
Nenhum ponto de L6A-R01 (função do SMTP) repete os acima.

### 1.3 Itens existentes, P1-4.3 (4): pontos e formatos
| id | ponto | formato | VOLÁTIL |
|---|---|---|---|
| BQ-0076 | SmartScreen alerta sobre sites suspeitos | definição | s |
| 6B-13 | meios do phishing (página falsa, formulário, código malicioso) | definição | n |
| 6B-14 | pharming: redirecionamento por alteração da resolução de nomes | definição | n |
| 6B-15 | HTTPS cifra, mas não garante que o site é o da instituição | par confundível | n |
Nenhum ponto de L6B-R01 (conduta) ou L6B-R02 (relação gênero-espécie) repete os acima.

### 1.4 Tetos, com o resultado honesto
- Formato (30%, folha de 6 itens = no máximo 1 por formato, pois 2/6 = 33%): os existentes já violam o teto antes do reforço (P1-3: definição 3/5; P1-4.3: definição 3/4). Os novos usam formatos de ocorrência 1/6 (situação hipotética; aplicação parlamentar; par confundível 2/6 = 33% em P1-4.3 se L6B-R02 entrar, ver dúvida). Não corrijo item existente. Pergunta à Gerência na seção abaixo.
- VOLÁTIL (20%): existentes P1-3 2/5 (40%) e P1-4.3 1/4 (25%) já acima do teto; os novos são 0 VOLÁTIL, logo P1-3 2/6 (33%) e P1-4.3 1/6 (17%, cumpre). Risco alto: 0.

Dúvidas para a Gerência: (1) liberar rede para as fontes ou aceitar a base verificada em 08/10/2026 (F4, F14, F15 do Lote 6b)?; (2) o teto de 30% é aplicável a folha de 6 itens (máximo 1 por formato) ou só à meta de 20?; (3) trocar o formato de L6B-R02 para evitar 2 pares confundíveis em P1-4.3.
FIM DA PARTE 1/3

## PARTE 2/3 — (d) Itens do estudante
Sem item: nenhuma base aberta em 18/10/2026 (D-REFORCO-2, regra 2).
FIM DA PARTE 2/3

## PARTE 3/3 — (d-G) Gabarito comentado
Contagem: 0 itens; C 0 / E 0; [TS] 0; VOLÁTEIS 0.

Tabela de proveniência (nenhuma fonte aberta em 18/10/2026):
| fonte | URL | situação |
|---|---|---|
| RFC 5321 | https://www.rfc-editor.org/rfc/rfc5321 | não aberta (403/ENOTFOUND) |
| CERT.br, fascículo Golpes | https://cartilha.cert.br/fasciculos/golpes-evite-fraudes/fasciculo-golpes-evite-fraudes.pdf | não aberta |
| CERT.br, Cartilha (livro) | https://cartilha.cert.br/livro/cartilha-seguranca-internet.pdf | não aberta |
FIM DA PARTE 3/3
FIM DO LOTE
