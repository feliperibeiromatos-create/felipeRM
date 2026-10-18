# L6B_reforco_onda1_saldo_v1.md — T-102 — 2026-10-18 — gerado por gcb-cpp

Despacho executado: saida/gcb/T102_D1_2026-10-18.md, seção 5. Nenhum item existente muda. Rótulo de todos os itens: AUTORAL.

## PARTE 1/3 — Mapa
### 1.1 Itens do saldo do R4 (P1-4.3)
| id | folha | ponto de julgamento | formato | base | VOLÁTIL | QA |
|---|---|---|---|---|---|---|
| L6B-R01 | P1-4.3 | conduta diante de mensagem com link que pede dados: não usar o link e confirmar pelo canal oficial | aplicação parlamentar | Microsoft Support, https://support.microsoft.com/pt-br/security/protect-yourself-from-phishing, verificado em 18/10/2026 (aberta hoje, HTTP 200, trecho literal presente) | n | QA: PENDENTE (gcb-cqfp, R1) |
| L6B-R02 | P1-4.3 | relação gênero-espécie entre phishing e pharming, apresentada invertida (phishing como tipo específico de pharming) | troca de sujeito | Cartilha de Segurança para Internet (CERT.br/NIC.br), seção 2.3.1: verificado em 09/10/2026 (registro canônico: saida/gcb/lote6_conferencia.md, seção 2.3, linha 154, F4 — Cartilha de Segurança para Internet, seção 2.3.1, https://cartilha.cert.br/livro/cartilha-seguranca-internet.pdf); não reaberta em 18/10/2026 por restrição de rede | n | QA: PENDENTE (gcb-cqfp, R1) |

### 1.2 Conferência de ponto e de formato em P1-4.3
- Pontos distintos dos existentes: L6B-R01 não repete o 6B-13 (meios do phishing: página falsa, formulário, código malicioso); L6B-R02 não repete o 6B-14 (mecanismo do pharming) e o enunciado não menciona DNS, resolução de nomes, redirecionamento nem digitação do endereço.
- Formatos em P1-4.3 depois da inclusão: aplicação parlamentar 1/6 e troca de sujeito 1/6 (teto de 30% cumprido). Nenhum item usa "definição".
- VOLÁTIL novo: 0 (risco alto: 0). Legado não imputado: definição 3/6 em P1-4.3 (D1 da GCB, T92_D1, 2.4).
- Coincidência de ponto com o curso 4.3.2 (linha 285 do Lote 6b: chamar o pharming de "espécie de golpe de phishing" não é erro): o L6B-R02 inverte a relação, o que é o erro.

### 1.3 Gabarito do R4 (fixado na D1)
L6B-R01 C; L6B-R02 E. Com o L6A-R01 (E), o R4 fica com 1 C / 2 E. Sem relação fixa entre [TS] e gabarito.

### 1.4 Verificação de rede desta produção (18/10/2026, curl -sL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36")
- A URL do L6B-R01 (também a forma antiga, support.microsoft.com/pt-br/windows/proteja-se-contra-phishing-0c7ea947-ba98-3bd9-7184-430e1f860a44, que redireciona para ela) respondeu HTTP 200, 114.587 bytes, título "Protejer-se de phishing | Microsoft Support". As quatro orações do trecho literal da D1 estão na página (busca textual no HTML decodificado). O tamanho difere dos 114.574 bytes da GCB (conteúdo dinâmico da página); o trecho não mudou.
- A URL do L6B-R02 (cartilha.cert.br) não foi reaberta; a citação segue a D-FONTE-DATA-ANTERIOR, condição 2. Conferi na linha 154 de saida/gcb/lote6_conferencia.md que a oração "Pharming é um tipo específico de phishing que envolve a redireção da navegação do usuário para sites falsos, por meio de alterações no serviço de DNS (Domain Name System)." está registrada entre aspas, com a F4 e a URL.
FIM DA PARTE 1/3

## PARTE 2/3 — (d) Itens do estudante
L6B-R01 (P1-4.3). AUTORAL. Um servidor do Derep (antigo DETAQ) recebeu uma mensagem eletrônica que diz ter sido enviada por uma área administrativa da Casa e que traz um link para "confirmar dados" cadastrais. Considerando essa mensagem e as boas práticas de segurança da informação, julgue o item a seguir.
A conduta adequada do servidor é não acessar o endereço indicado no link e confirmar a solicitação com a área apontada como remetente, por meio de endereço eletrônico ou telefone oficiais obtidos de forma independente da mensagem recebida.

L6B-R02 (P1-4.3). AUTORAL. Acerca de golpes praticados pela Internet, julgue o item a seguir.
O phishing é um tipo específico de pharming, pois este é o golpe mais abrangente e inclui o phishing como uma de suas modalidades.
FIM DA PARTE 2/3

## PARTE 3/3 — (d-G) Gabarito comentado
### L6B-R01 — Gabarito: C
Justificativa (duas linhas): diante de mensagem suspeita que pede dados por link, a orientação é não clicar no link e verificar a solicitação com a organização por meio de canais oficiais, obtidos de forma independente da mensagem. O item descreve exatamente essa conduta, sem exigir que a mensagem seja de fato fraudulenta.
[TS]: não (item direto; sem troca sutil).
VOLÁTIL: não (julga conduta, não versão, menu, limite ou disponibilidade de produto; o enunciado não nomeia produto).
REVERIFICAR: 4–8/1/2027 (conferência de base, T-11, parte P1, gcb-cqfp; sem efeito de VOLÁTIL).
Ponto de julgamento: conduta diante de mensagem com link que pede dados. Formato: aplicação parlamentar. Rótulo: AUTORAL. QA: PENDENTE (gcb-cqfp, R1).
Base: Microsoft Support, "Proteger-se de phishing" (título da página: "Protejer-se de phishing | Microsoft Support"), https://support.microsoft.com/pt-br/security/protect-yourself-from-phishing, verificado em 18/10/2026. Trecho literal (seção "Se receber um e-mail ou mensagem de phishing no Teams"; grafia da página, que mistura pt-PT e pt-BR, mantida): "Nunca clique em ligações ou anexos em e-mails suspeitos ou mensagens do Teams. Se receber uma mensagem suspeita de uma organização e recear que a mensagem possa ser legítima, aceda ao seu browser e abra um novo separador. Em seguida, aceda ao site da organização a partir do seu favorito guardado ou através de uma pesquisa na Web. Fale com eles usando números oficiais ou e-mails de seu site." Complementar (mesma seção): "Se a mensagem suspeita parecer ser proveniente de uma pessoa que conhece, contacte essa pessoa através de outros meios".

### L6B-R02 — Gabarito: E
Justificativa (duas linhas): a relação é a inversa da apresentada: o pharming é um tipo específico de phishing, e não o contrário. O item faz do phishing a espécie e do pharming o gênero.
[TS]: sim — a troca está em "O phishing é um tipo específico de pharming" (o correto é: pharming é tipo específico de phishing).
VOLÁTIL: não (relação conceitual estável).
REVERIFICAR: 4–8/1/2027, com reabertura obrigatória da URL (D-FONTE-DATA-ANTERIOR, condição 4); se a página não sustentar mais o trecho, o caso volta à Gerência titular como errata ou D2, sem efeito automático de VOLÁTIL.
Ponto de julgamento: relação gênero-espécie phishing/pharming. Formato: troca de sujeito. Rótulo: AUTORAL. QA: PENDENTE (gcb-cqfp, R1).
Base: "Pharming é um tipo específico de phishing" — verificado em 09/10/2026 (registro canônico: saida/gcb/lote6_conferencia.md, seção 2.3, linha 154, F4 — Cartilha de Segurança para Internet, seção 2.3.1, https://cartilha.cert.br/livro/cartilha-seguranca-internet.pdf); não reaberta em 18/10/2026 por restrição de rede.

### Contagem
Itens: 2 (L6B-R01, L6B-R02). Gabarito: C 1 / E 1. [TS]: 1 (L6B-R02). VOLÁTEIS: 0 (risco alto: 0). R4 completo: 3 itens (L6A-R01 E, L6B-R01 C, L6B-R02 E) = 1 C / 2 E. Onda 1 (conforme D1): 24 C / 26 E (48%), a reconferir pela Gerência.

### Tabela de proveniência
| fonte | URL | data de verificação | trecho literal | uso |
|---|---|---|---|---|
| Microsoft Support (documentação do fornecedor; rótulo OUTRA_OFICIAL) | https://support.microsoft.com/pt-br/security/protect-yourself-from-phishing | verificado em 18/10/2026 (aberta hoje por esta produção, HTTP 200) | ver L6B-R01 acima (quatro orações; complementar) | sustenta L6B-R01 (C) |
| CERT.br/NIC.br, Cartilha de Segurança para Internet, seção 2.3.1 (rótulo OUTRA_OFICIAL) | https://cartilha.cert.br/livro/cartilha-seguranca-internet.pdf | verificado em 09/10/2026 (registro canônico: saida/gcb/lote6_conferencia.md, seção 2.3, linha 154, F4 — Cartilha de Segurança para Internet, seção 2.3.1); não reaberta em 18/10/2026 por restrição de rede | "Pharming é um tipo específico de phishing que envolve a redireção da navegação do usuário para sites falsos, por meio de alterações no serviço de DNS (Domain Name System)." (o item usa só a oração "Pharming é um tipo específico de phishing") | sustenta L6B-R02 (E) |
| learn.microsoft.com (anti-phishing-protection-about), RFC 5321, gov.br | — | — | — | não usadas como base |
FIM DA PARTE 3/3
FIM DO LOTE
