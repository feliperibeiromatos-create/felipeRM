# Lote 6b — TI-REDES-SEGURANCA (P1 itens 2 e 4: redes e segurança) — gabarito e justificativas

Mecanismo: troca de conceito (TC), generalização indevida (GI), atribuição errada (AT), inversão de causa e efeito (IC)

### 6B-01 — Gabarito: E

- Item do edital: P1-2
- Justificativa: TC (definições de LAN e WAN invertidas). Curso 2.0.2: LAN interliga equipamentos em área geográfica restrita (sala, edifício, campus); WAN interliga redes em áreas geograficamente distantes; o critério é o alcance. Fonte: conceito geral.

### 6B-02 — Gabarito: C

- Item do edital: P1-2.1
- Justificativa: GI invertida (tentação: "usa protocolos da Internet, logo é pública" → marcar E). Curso 2.1.1: a intranet é rede privada que usa as mesmas tecnologias e protocolos da Internet, com acesso restrito ao público autorizado; o que a define é o público e o controle de acesso. Fonte: conceito geral.

### 6B-03 — Gabarito: E

- Item do edital: P1-2.1
- Justificativa: TC (intranet e extranet trocadas). Curso 2.1.1: a intranet é a rede de uso interno; a extranet é a extensão controlada a parceiros e fornecedores externos autorizados. O item atribui à extranet o que é da intranet, e vice-versa. Fonte: conceito geral.

### 6B-04 — Gabarito: C

- Item do edital: P1-2.1
- Justificativa: sem armadilha (ancoragem). Curso 2.1.5 e 2.0.6: o DNS associa nomes de domínio a endereços IP, de modo que o usuário acessa o site pelo nome. Fonte: conceito geral.

### 6B-05 — Gabarito: C

- Item do edital: P1-2.1
- Justificativa: sem armadilha (ancoragem). Curso 2.1.1: a Internet é a rede mundial de redes (infraestrutura); a Web é um serviço sobre ela (páginas e recursos acessados por HTTP/HTTPS); os termos não são sinônimos. Fonte: conceito geral.

### 6B-06 — Gabarito: E

- Item do edital: P1-4.1
- Justificativa: TC (integridade e disponibilidade trocadas). Curso 4.1.1: integridade = não alteração indevida; disponibilidade = acesso sempre que necessário. Fonte: conceito geral. Tema da tríade CIA também nos itens reais 96 e 98 do TRF6 2024, com outro ponto de julgamento (seção ITENS REAIS).

### 6B-07 — Gabarito: E

- Item do edital: P1-4.1
- Justificativa: TC (lógica de restauração do incremental atribuída ao diferencial). Curso 4.1.2: numa rotina de completo + diferenciais, cada diferencial acumula tudo o que mudou desde o completo; a restauração exige o último completo e apenas o último diferencial (o de quarta-feira). O item não depende da divergência de definição registrada no curso 4.1.2.

### 6B-08 — Gabarito: C

- Item do edital: P1-4.1
- Justificativa: sem armadilha (ancoragem). Curso 4.1.4: ransomware é "um tipo de código malicioso que torna inacessíveis os dados armazenados em um equipamento"; curso 4.1.2: backups periódicos são a defesa essencial. Item não afirma que o backup evita o ataque, só que reduz o impacto.

### 6B-09 — Gabarito: E

- Item do edital: P1-4.1
- Justificativa: TC (vírus e worm trocados). Curso 4.1.3 e 4.1.4: o vírus depende de hospedeiro e de execução; o worm é independente e se propaga sozinho pela rede.

### 6B-10 — Gabarito: E

- Item do edital: P1-4.2
- Justificativa: TC (firewall e antivírus trocados). Curso 4.2.1, 4.2.2 e 4.2.5: o antivírus detecta e remove malware (olha arquivos e programas); o firewall controla o tráfego por regras.

### 6B-11 — Gabarito: C

- Item do edital: P1-4.2
- Justificativa: sem armadilha (ancoragem). Curso 4.1.3, 4.1.4 (spyware) e 4.2.3 (antispyware): spyware monitora e envia informações a terceiros; antispyware detecta e remove esse tipo de código. Fonte: conceito geral.

### 6B-12 — Gabarito: E

- Item do edital: P1-4.2
- Justificativa: GI. Curso 4.2.1 e 4.2.7: nenhum antivírus detecta todas as ameaças, principalmente as novas; o antivírus depende de atualização e tem limites. Fonte: conceito geral.

### 6B-13 — Gabarito: E

- Item do edital: P1-4.3
- Justificativa: GI (restrição indevida dos meios do phishing). Curso 4.3.1: o phishing induz a vítima a clicar em link para página falsa, a abrir anexo malicioso ou a preencher dados; a coleta pode ocorrer por página falsa, por formulário na própria mensagem ou pela instalação de código malicioso. A primeira oração é correta (isca que imita instituição conhecida); o erro está em restringir o golpe à página falsa e negar o código malicioso.

### 6B-14 — Gabarito: C

- Item do edital: P1-4.3
- Justificativa: IC invertida (tentação: achar que o clique em link é condição do ataque → marcar E). Curso 4.3.2: no pharming, o usuário digita o endereço correto e é redirecionado por alteração da resolução de nomes (DNS ou arquivo hosts). Fonte: arquivo hosts: conceito geral.

### 6B-15 — Gabarito: C

- Item do edital: P1-4.3
- Justificativa: GI invertida (tentação: saber que o HTTPS autentica o servidor e concluir que ele garante que o site é o da instituição pretendida → marcar E). Curso 4.3.4: HTTPS é o HTTP sobre conexão TLS; o servidor é autenticado para o domínio acessado e a comunicação ganha confidencialidade e integridade, mas isso não garante que o domínio seja o da instituição pretendida nem a boa-fé do titular; páginas fraudulentas, em domínios próprios, também podem usar HTTPS. Fonte: o restante é conceito geral.

## Itens de reforço

### L6B-R01 — Gabarito: C

- Item do edital: P1-4.3
- Justificativa: diante de mensagem suspeita que pede dados por link, a orientação é não clicar no link e verificar a solicitação com a organização por meio de canais oficiais, obtidos de forma independente da mensagem. O item descreve exatamente essa conduta, sem exigir que a mensagem seja de fato fraudulenta.

### L6B-R02 — Gabarito: E

- Item do edital: P1-4.3
- Justificativa: a relação é a inversa da apresentada: o pharming é um tipo específico de phishing, e não o contrário. O item faz do phishing a espécie e do pharming o gênero.
