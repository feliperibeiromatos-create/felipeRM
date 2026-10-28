# Avaliação — "Pacote_Resumos_Visuais_DAD_MapasPro_v1" (ChatGPT, 28/10/2026) × produção Cowork v17.3 leva 1

Cowork (Fable 5.1), 28/10/2026. O Fundador entregou, no fim da leva 1, um pacote paralelo produzido pelo ChatGPT para a mesma tarefa: triagem dos 16 PDFs (404 páginas), guia visual, prévia do item 1 (1, 1.1 e 1.2) em HTML/PDF, dois SVGs, JSON de blocos e notas de integração. Esta avaliação compara os dois trabalhos e propõe o aproveitamento. Nada do pacote entrou na plataforma; a adoção de IA é matéria reservada ao Fundador e o conteúdo externo só entra após QA normativo por modelo distinto.

## O que o pacote tem de bom (e que convém aproveitar)

1. **Triagem dos 16 PDFs com 31 achados dirigidos e fontes datadas.** Doze achados coincidem com a triagem Cowork da leva 1 (COFIFOMOB/elementos, prazo em quádruplo, Embrapa, contrato de desempenho, incompetência insanável, desvio de finalidade sanável, maioria votante, falência das estatais, Súmula 343, Temas 532 e 592, ANPD). A convergência de dois modelos independentes dá confiança a essas correções. Dezenove são novos ou mais precisos e interessam às levas 2–4: SV 43 (promoção/ascensão), art. 37, II × III (R15 p. 7), art. 10-A da LIA revogado, ADIs 7.156/7.236 de 2026 (prescrição), vigência da Lei 14.133, seis critérios do art. 33, contagem de prazos da LAI, art. 32 × 33 da LAI, agentes de tratamento na LGPD, consentimento de crianças, Lei 15.352/2026 (ANPD) e outros. **Nenhum deles foi conferido por mim**; entram na triagem das levas 2–4 como hipóteses a confirmar em fonte oficial, não como fatos.
2. **Guia visual convergente.** As decisões de tradução são as mesmas da ESPEC v3 (preto → tinta, amarelo → marcador, emoji → ícone, etiqueta de probabilidade → contagem auditada, pirâmide só quando a relação é verdadeira, verde/vermelho só para C/E). Os tokens batem com os da v17 (o ChatGPT leu o template v17 de 21/10). Duas regras valem adotar na ESPEC: "não colocar recados de integração, hashes ou pendências de QA dentro da experiência da candidata" (o QA R1 pegou exatamente isso em D13) e "o resumo do pai apenas organiza os filhos" (1 organiza 1.1 e 1.2).
3. **Processo.** Hashes dos originais, índice das 404 páginas, roteiro de QA independente e a declaração honesta de que a própria conferência não é QA. É o mesmo padrão da fábrica.
4. **Tabela de imagens propostas por item** (19 recursos, com o que deve tornar visível e o cuidado de cada um) — útil como lista de ilustrações para as levas 2–4, a somar às quatro indicações já registradas na leva 1.

## O que não convém aproveitar como está

1. **Formato.** A prévia é um documento autônomo de oito páginas (HTML com logotipo, seletor de tema e fonte própria embutida; PDF A4) que reúne 1, 1.1 e 1.2 numa só leitura. A plataforma já tem, desde a v17.3, o Resumo visual por tópico, integrado à tela "Resumo", com regressão 0/0, QA R1–R3 aprovado e nove tópicos prontos. O esquema de blocos do ChatGPT (`p`, `cards`, `callout`, `table`, `diagram`, `principles`, `entities`, `judgments`) é outro contrato; as próprias notas dizem que é "formato de autoria, não contrato de API" e que o kit "não é patch aplicado". Migrar para ele seria refazer o que está feito e testado.
2. **Base técnica desatualizada.** As notas de integração partem do template v17 de 21/10 (`vResumoVer` lendo `extra.resumo`); a v17.3 já estendeu esse ponto com `resumoVisual` e renderização por tipos fechados (sem HTML/SVG arbitrário), que é justamente o que o ChatGPT recomenda.
3. **Fonte Atkinson Hyperlegible embutida** e cabeçalho/seletor próprios: a plataforma usa a tipografia e o tema do sistema; não entra um segundo seletor dentro do Resumo (as notas do pacote concordam).
4. **Contagens do corpus** ligeiramente diferentes das usadas na leva 1 (3/30/75 "aderência integral" contra 3/33/79 na ESPEC, que inclui enquadramentos parciais). Reconciliar o critério na GBQ antes de citar números na etiqueta das próximas levas.
5. **Os dois SVGs** são esquemáticos: `organizacao.svg` (órgãos A e B dentro de uma pessoa; pessoas 1 e 2 ligadas por linha tracejada) é uma versão mínima da ilustração pedida para 1.2 e pode servir se receber os rótulos "hierarquia" e "vinculação sem hierarquia" e as cores do tema; `lentes.svg` (dois cartões com "?") não acrescenta nada ao compare já existente.

## Comparação direta da prévia do item 1 com o Resumo visual de P1-DA-1, 1.1 e 1.2

- Conteúdo: as duas versões cobrem o mesmo núcleo (Estado/governo/Administração; sentidos subjetivo/objetivo e amplo/estrito; três Poderes; LIMPE; princípios da Lei 9.784; órgão/entidade; desconcentração/descentralização; entidades da indireta). A versão Cowork tem mais blocos e cita artigo em cada afirmação; a do ChatGPT é mais enxuta e tem três ideias que valem absorver, com QA: a "Atenção à palavra exclusiva" (estrito ≠ exclusivo do Executivo), o "limite" de cada princípio na lista LIMPE e o exemplo didático "mesmo caso, lentes diferentes".
- Estética: mesma família (faixa de tinta com título em marcador, caixa de atenção com filete amarelo, tabela de cabeçalho em tinta, cartões). As diferenças são de detalhe (título em duas linhas com ponto final; "Neste resumo" vazio na prévia).
- Verificação: ambas testadas em 320/390/1280 nos dois temas; só a Cowork passou por QA de outro modelo.

## Proposta de aproveitamento (classificação)

- **AGORA** — (a) Juntar os 31 achados à triagem das levas 2–4 como hipóteses a conferir (arquivo `dados/achados_dirigidos.json` do pacote, guardado em `saida/arquivo_projeto/`); (b) incorporar à ESPEC v3.1 as duas regras do item 2 acima; (c) absorver no Resumo visual de P1-DA-1 e 1.1 as três ideias apontadas, numa revisão pontual com QA; (d) manter v17.3 como base e seguir para a leva 2.
- **PRÓXIMO** — Se o Fundador quiser usar o ChatGPT de forma contínua: dar-lhe um papel que não duplique a produção — triagem e segunda leitura normativa dos PDFs de cada leva antes da produção Cowork, e desenho de SVGs sob encomenda (com o formato `imagem` da ESPEC: data URI ≤ 150 KB, alt, tokens do tema). Dois produtores no mesmo tópico, como aconteceu hoje, é retrabalho.
- **BACKLOG** — `organizacao.svg` adaptado como ilustração de 1.2, depois dos rótulos e do QA.
- **DESCARTADO** — Substituir o Resumo visual integrado pelo formato de documento autônomo; a fonte embutida; o seletor de tema interno; `lentes.svg`.

Decisão reservada ao Fundador (adoção de IA e divisão de papéis). Nada do pacote foi alterado; os arquivos ficam em `saida/arquivo_projeto/ChatGPT_resumos_DAD_v1_2026-10-28/` como referência.
