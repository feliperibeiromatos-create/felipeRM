# Ordem à Fábrica — BANCO-DA, fila 2024 (cadernos TEC "DAD - CEBRASPE - 2024", 4 PDFs, 800 candidatos) — 28/10/2026

Origem: o Fundador entregou em 28/10/2026 quatro cadernos do TEC Concursos ("Caderno DAD - CEBRASPE - 2024 - 001/201/401/601", 85 + 88 + 89 + 94 páginas), ordenados por matéria e assunto, com 200 questões cada. A sessão Cowork extraiu a fila no mesmo schema da fila 2025 (candidatos_DA_TEC2025_fila_v2.csv) e redigiu esta ordem. O TEC continua sendo só LOCALIZADOR (D-GCE-01; D-BANCO-LOCALIZADOR, T-129): nenhum texto, gabarito ou metadado do TEC entra no banco; entra o que for lido no caderno e no gabarito definitivo em cdn.cebraspe.org.br.

Anexos (banco/candidatos/ e saida/arquivo_projeto/cadernos_TEC_DA_2024/):
- candidatos_DA_TEC2024_fila.csv — 800 linhas, ';', aspas; colunas idênticas à fila 2025 v2. Todos Certo/Errado (0 múltipla escolha); 0 duplicatas internas por hash; 0 hashes coincidentes com a fila 2025. `item_edital_wb` e `aderencia_wb` são HEURÍSTICOS: herdados do rótulo TEC pela correspondência rótulo → item da fila 2025 (mapa_rotulo_item_2024.json: 111 rótulos herdados, 10 mapeados à mão pela Cowork, marcados "manual"); a decisão final de enquadramento é da produção, pelo critério do piloto (subitem literal mais específico).
- resumo_por_prova_2024.csv — 97 provas, por quantidade de candidatos (CAPES Ana CT 29; ANTT ERSTT 27; TSE TJ 26 e AJ 23; TCE AC Ana Adm Eng 24 e Dir 16, ACE 17; ANAC ERAC 20; CNJ TJ 20; CM Maceió Ap Adm 18; STJ AJ 16; CODEVASF AnDR 16; …).
- resumo_por_item_edital_2024.csv — contagem heurística por item: 1.1 27; 1.2 69; 2.1 68; 3.1 22; 3.4 12; 4.2 11; 4.3 2; 4.4 37; 5.1 30; 5.2 8; 6.1 19; 6.3 4; 6.5 7; 7 40; 8.2 41; 10.1 103; 10.2 60; 10.4 31; 10.5 24; 10.6 25; 10.7 54; sem enquadramento 98 (controle da Administração, convênios, serviços públicos/concessões, bens, consórcios); 2.2, 3.3, 4.1, 8.1, 8.4, 9, 11 e 12 sem candidato.
- parse_caderno_tec.py — extrator (pdftotext -layout → fila), reprodutível; mapa_rotulo_item_2024.json.
- Os 4 PDFs com SHA-256 (d5eee85d…, ecb22d87…, 54b8b417…, 3713dee9…) para a referência de página.

## Decisões prévias (Fundador) — matéria reservada
1. Gasto: esta fila abre até 97 cadernos + 97 gabaritos no CDN. Proposta: rodar em ondas de 15 provas como a fila 2025, DEPOIS das ondas pendentes da fila 2025 (T-129 devolvida, T-135 e T-139 pendentes), ou intercalada por item do edital quando a lacuna justificar (ver "Uso recomendado"). Sem "sim", nada roda.
2. Guarda dos cadernos: ficam em saida/arquivo_projeto/ (uso interno, localizador); não vão à plataforma nem à candidata.

## Uso recomendado (Cowork, para a GBQ decidir no seu nível)
- A fila 2024 vale mais pelas lacunas do que pelo volume: 10.7 (ETP/TR) tem 54 candidatos aqui contra 19 na fila 2025; 8.2 tem 41; 5.1 tem 30; 6.1 tem 19. Em 1.2, 2.1, 4.4, 7 e 10.1 a fila 2025 já é farta.
- Não resolve as lacunas 2.2, 3.3, 4.1, 8.1, 8.4, 9, 11 e 12: continuam exigindo varredura temática no CDN (T-86, T-136).
- Temporal (regra 7 da ONDA1, reforçada para 2024): conferir, item a item, as normas alteradas entre a prova e hoje — EC 138/2025 (art. 37, XVI, b); Decreto 12.374/2025 (estágio probatório); Lei 15.371/2026 e LC 229/2026 (licença-paternidade: não alteram a Lei 8.112); Lei 15.352/2026 (ANPD) e as ADIs de 2026 sobre a LIA (hipóteses a confirmar em fonte oficial — vieram da triagem do ChatGPT de 28/10); Lei 14.133 (todas as provas de 2024 já são do regime novo, mas itens sobre a transição ou sobre a Lei 8.666 revogada são VOLÁTIL-NORMATIVO, fora de simulado final). Item cujo gabarito mudaria com a norma atual → VOLÁTIL-NORMATIVO, reverificação 4–8/1/2027 (T-11).

---

```
ORQUESTRADOR: BANCO
REMETENTE: Cowork/Fable (registro da entrega do Fundador de 28/10/2026)
DESTINATÁRIO: gbq-gerencia (GBQ), com GCB em cópia (Direito Administrativo, D-DA-LOTES)
PROMPT:
a) Objeto: incorporar à fila de candidatos de Direito Administrativo a fila 2024 (banco/candidatos/candidatos_DA_TEC2024_fila.csv, 800 candidatos C/E, 97 provas Cebraspe de 2024) e planejar sua verificação no CDN oficial nas mesmas regras da ORDEM_BANCO_DA_CDN_ONDA1 (fonte única cdn.cebraspe.org.br; texto do caderno, gabarito definitivo; rótulo CEBRASPE_ANALOGA com certame, ano, cargo, número do item, URLs, data_verificacao e verificado_por; item_edital pelo conhecimento necessário; `mecanismo` registrado (D-ESPEC-DA-V2-1); deduplicação por hash; nenhuma publicação sem gatilho A e sim do Fundador).
b) Antes de qualquer onda: (1) a GBQ decide, no seu nível, a ordem entre a fila 2025 (ondas pendentes) e a fila 2024, propondo ao Fundador o plano de ondas com a estimativa de cadernos a abrir (decisão de gasto é dele); (2) reconciliar o critério de contagem (T-155) para que as etiquetas da plataforma e os relatórios usem um só número.
c) Primeira onda sugerida da fila 2024 (se o Fundador aprovar): as 15 provas com mais candidatos em resumo_por_prova_2024.csv (~290 candidatos), com a conferência temporal da seção "Uso recomendado" obrigatória por item — é o motivo da devolução da T-129 e não pode repetir-se.
d) Saída: fila 2024 com status por candidato (localizado / não localizado / anulado / divergente / VOLÁTIL-NORMATIVO / duplicata), banco/banco.csv com os aceitos, relatório saida/banco/varredura_DA_2024_onda<n>_<data>.md com contagem por item do edital antes e depois, parecer do QA (modelo distinto), reserva_DA.csv para os "sem enquadramento".
e) Classificação: PRÓXIMO (depois das ondas pendentes da fila 2025, salvo decisão da GBQ de intercalar pelas lacunas 10.7, 8.2, 5.1 e 6.1). Sugestão de criação (regra PARALELIZAÇÃO): CRIAÇÃO: CHAT ESPECIALIZADO NOVO / "gbq-cfp-2024" / "GBQ — Varredura CDN fila 2024" / Sonnet / esforço médio / custo-benefício: a localização no CDN é trabalho mecânico e volumoso (97 provas), separável do chat gbq-cfp que trata a fila 2025; QA no Opus já existente / superior: gbq-gerencia / missão: localizar e incorporar os candidatos 2024 nas ondas aprovadas / instalação: regras e) e f) da ORDEM_BANCO_DA_CDN_ONDA1 + seção temporal desta ordem. A GBQ pode recusar com uma linha.
```
