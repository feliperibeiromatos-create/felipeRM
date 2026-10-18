# T85_reconciliacao_2026-10-18.md — T-85 — 2026-10-18 — gerado por gcb-gerencia

Objeto: reconciliação da T-85, errata de forma nos canônicos do Lote 4 e do Lote 5 (aberta pela D1 da GCB na T-83; AGORA por D-FUNDADOR-AGORA-3). Cadeia: gcb-cpp → gcb-cqfp → gcb-gerencia.
Entradas:
- produção: saida/gcb/T85_errata_proposta_2026-10-18.md (gcb-cpp; P1–P3 e B1–B3; nada aplicado);
- QA: saida/gcb/QA_T85_2026-10-18_gcb-cqfp.md (gcb-cqfp; P1–P3 APROVADO; B1–B3 APROVADO COM AJUSTE, com texto exato; R1 e R2 novos, com texto exato; O1–O4; 0/6 reprovados);
- precedente: saida/gcb/T83_reconciliacao_2026-10-17.md (a GCB transcreve o "leia-se" já redigido e conferido; rótulo de versão e linha na Tabela de Correções; T-47);
- pendência: DECISOES.md, D-L4-T83-DEVOLVIDO (Lote 4 v3.5 devolvido à GCB, base do Projeto não conferida).

## 1. Veredito
**T-85 reconciliada (D1 GCB). Os 8 pontos são ACEITOS e foram APLICADOS pela GCB nos espelhos:**
- P1, P2 e P3: como propostos.
- B1, B2 e B3: com o ajuste do QA.
- R1 e R2: com o texto do QA.

Resultado:
- Lote 4: v3.5 → **v3.6**.
- Lote 5: v3.2 → **v3.3**.

Nenhum gabarito, item, enunciado, [TS], VOLÁTIL, URL, citação literal ou data de verificação mudou. Nada volta à gcb-cpp. A GCB não redigiu nenhum texto de conteúdo. Ela transcreveu os "leia-se" aprovados e redigiu só o registro: rótulos e linhas da Tabela, como na T-83.

## 2. Decisão por ponto
| Ponto | Arquivo, linha (versão nova) | Decisão | Motivo |
|---|---|---|---|
| P1 | L4 v3.6, l. 146 (curso 5.2.5) | ACEITO como proposto | Sem isto, o estudante lê "É o que afirma:", frase sem sujeito. A redação é a mesma da errata T-83, e o QA abriu a página em 18/10/2026. |
| P2 | L4 v3.6, l. 147 | ACEITO como proposto | Sem isto, o estudante lê "ficar com a formulação e evitar", sem complemento. |
| P3 | L4 v3.6, l. 52 (rótulo F4) | ACEITO como proposto | O rótulo passa a seguir o título da página (H1 "What is Machine Learning?"). A URL não muda. |
| B1 | L4 v3.6, l. 108 | ACEITO COM O AJUSTE DO QA | A proposta da produção ("as técnicas de engenharia de prompts vistas neste curso") apagava do canônico a atribuição a F1/F2, o que é regressão de proveniência (regras/proveniencia.md). O texto do QA mantém "(F1, F2)" no canônico, e o gerador o retira da edição. A alternativa curta da gcb-cpp fica descartada. |
| B2 | L4 v3.6, l. 174 | ACEITO COM O AJUSTE DO QA | A proposta punha "GAN —" dentro do título entre aspas, o mesmo defeito que o P3 corrige. Também retirava o carimbo. O texto do QA usa o H1 da página e mantém "(F5, verificado em 7/10/2026)" no canônico. Isso resolve a pendência da proposta: o carimbo fica no canônico. |
| B3 | L5 v3.3, l. 266 (justificativa do A5-14) | ACEITO COM O AJUSTE DO QA | A proposta citava "Using Power BI" como título, mas o H1 atual é "Use Power BI". Além disso, em (2), "a documentação da Microsoft Learn" sugeria que o U2 é a mesma fonte do U1. O texto do QA descreve o U1 sem pôr título entre aspas e dá ao U2 o rótulo da tabela de fontes. Ficam intactos o gabarito C, VOLÁTIL, "(B)", "8.3", "Verificado em 8/10/2026" e "Risco BAIXO". |
| R1 | L5 v3.3, l. 148 (8.3, Data Studio, nome vigente) | ACEITO, entra já | Ver §3. |
| R2 | L5 v3.3, l. 150 (8.3, Data Studio, edições) | ACEITO, entra já | Ver §3. |

## 3. R1 e R2 — entram já, sem tarefa nova à gcb-cpp
Decisão: aplicar nesta errata o texto fixado pelo QA.
Motivos:
- (a) O ponto (4) da linha T-85 manda a gcb-cqfp varrer e listar outros resíduos "para a mesma errata". R1 e R2 estão dentro do objeto da tarefa e não são complemento novo (D-COMPLEMENTOS não se aplica).
- (b) É o rito já usado na T-83, Erratum 1, e aqui em B1–B3: quando o QA fixa o texto, a GCB o adota sem nova rodada.
- (c) As duas trocas são de forma e ficam dentro da linha. Elas só nomeiam em palavras uma fonte que já está na tabela, a U4 ("Welcome to Data Studio", aberta pelo QA em 18/10/2026), e mantêm o código "(U4)" no canônico. Nenhuma citação, data ou afirmação muda.
- (d) Mandar R1 e R2 à gcb-cpp custaria um ciclo a mais e abriria uma v3.4 do Lote 5 só para isso.

Separação de funções:
- O QA redigiu R1 e R2, mas não os aplicou.
- A GCB conferiu os dois por script: o "onde se lê" ocorre 1 vez, as marcas por linha ficam iguais e a saída do gerador sai completa e sem código. Ver §5.
- Os dois entram na conferência de aplicação da presidencia no gatilho E.

## 4. Observações do QA
- **O1** (L4_gabarito.md:58, "O F4 afirma que…"): sem ação aqui. É a errata T-83, já no canônico v3.5/v3.6. O pacote a absorve só depois do aceite do Lote 4 (D-L4-T83-DEVOLVIDO).
- **O2** (4C-04, a fonte da temperatura se perde na edição): SEM ERRATA, de acordo com o QA. A frase fica completa.
- **O3** (rótulos da tabela de fontes que divergem do H1: F5, L4 l. 53, "GAN — Background: …"; U1, L5 l. 31, "Using Power BI"): **não entra agora. Vira tarefa nova à gcb-cpp (T-90, PRÓXIMO).**
  - O QA não fixou o texto dos rótulos, só registrou o H1. A GCB não redige.
  - Os rótulos não chegam ao estudante.
  - O rótulo do U1 está em fonte da zona VOLÁTIL do 8.3. Mudar um rótulo dado como "verificado em 8/10/2026" pede verificação datada própria, e a janela natural é a reverificação de janeiro (FV).
  - A T-90 não bloqueia o aceite da v3.6 nem o da v3.3.
- **O4** (gerador v1.8, literais.py, linhas 40, 45, 47, 48, 135 e 136, que ficam inertes depois da errata): é da GBQ. Vai na tarefa nova T-89, que liga a absorção da T-83/T-85 à próxima T-12. A GCB não é dona do gerador. Na mesma tarefa vai, como sugestão opcional, a conferência de frase truncada proposta pela gcb-cpp (proposta, seção C).
- **Correção de registro:** a proposta da gcb-cpp diz "VOLÁTIL 10 → 10". Isso conta linhas. O QA conta ocorrências (13 → 13). As duas contagens estão certas e foram conferidas abaixo.

## 5. Conferência por script (python -I; bases copiadas no scratchpad antes da edição; scripts aplicar.py e conferir.py no scratchpad)
| Verificação | Lote 4 (v3.5 → v3.6) | Lote 5 (v3.2 → v3.3) |
|---|---|---|
| "Onde se lê" | 5 trocas (P1, P2, P3, B1, B2), cada uma 1× | 4 trocas (R1, R2, B3(1), B3(2)), cada uma 1× |
| Operações do diff (ignorando CR) | 2 inserções (l. 12, rótulo v3.6; l. 46, Tabela) + 5 linhas trocadas (52, 108, 146, 147, 174) | 2 inserções (l. 9, rótulo v3.3; l. 29, Tabela) + 3 linhas trocadas (148, 150, 266) |
| "[TS]" (ocorrências / linhas) | 12/12 → 12/12 | 16/15 → 16/15 |
| "VOLÁTIL" (ocorrências / linhas) | 13/10 → 13/10 | 13/13 → 13/13 |
| Gabaritos do d-G | 20 → 20, 10 C/10 E, sequência idêntica | 20 → 20, 10 C/10 E, sequência idêntica |
| URLs | 5 → 5, idênticas | 10 → 10, idênticas |
| "verificado em" | 31 → 33 (+2: a linha nova da Tabela cita o "onde se lia" e o "lê-se" do B2; o curso não muda) | 4 → 4; "Verificado em" 4 → 4 |
| Fim de linha | CRLF, 383 → 385, sem CR solto | CRLF, 285 → 287, sem CR solto |
| Bytes | 67899 → 69857 | 44363 → 45894 |
| Saída do gerador v1.8 (strip_text) nas linhas trocadas | completas, sem código: "…as técnicas descritas nos guias de engenharia de prompts da Anthropic e da OpenAI."; "É o que afirma a página "What is Machine Learning?", do curso Introduction to Machine Learning do Google for Developers: …"; "…ficar com a formulação da página "What is Machine Learning?" e evitar…"; "Segundo a página "Background: What is a Generative Model?", do curso sobre GAN do Google for Developers:" | completas, sem código U: "…página de boas-vindas da documentação do Data Studio: "In April 2026, …""; "(página de boas-vindas da documentação, seção "Upgrade to Data Studio Pro"; …)"; A5-14 conforme o QA |

SHA-256:
| Arquivo | Versão | Disco (CRLF) | LF |
|---|---|---|---|
| saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md | v3.5 (base) | 5930eba9ca94eebf834e248206efa9e4b67c1e6edd0f06f6c66b1974886b3699 | fc6f1648bf5732dffa9f4c810623512111658ee03c4359b99789220646817f91 |
| idem | **v3.6** | 846b8ef00eedb318c3af5a5b93820366d43a4a201066a9f8e891d7300c1f9475 | **e26032129ce56a55f83dd2deee62311126733f2a625dbb17558a4a31d0cd83e1** |
| saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md | v3.2 (base, canônica) | 8f7027f25ce017707633be05355a9448c1f3d3da3b298287a3432721d04b44de | 5f7f736cd369a6a1968112a51fb0c45e7fad9015de602815de6acefd9b8e441c (= o 5f7f736c… da D-TRANSPORTE-L5-V32) |
| idem | **v3.3** | 9953fc148047b2808fb80dfbda163e90ac00d2771001a7d7ba5a566f6bcc0569 | **2572d1fcafdc7e79265820929cddc43cc2db1455dc320b575a7531d2c4af64d0** |

Registro, no padrão da T-83:
- Lote 4: rótulo "v3.6 — errata de forma T-85 (…)" na linha 12 e linha "Errata T-85 (D1 da GCB na T-83, 18/10/2026)" na Tabela, linha 46.
- Lote 5: rótulo "v3.3 — errata de forma T-85 (…)" na linha 9 e linha "Errata T-85 (…)" na Tabela, linha 29.
- Nenhum dos rótulos e nenhuma das linhas da Tabela traz "[TS]" ou "VOLÁTIL".

## 6. Encadeamento com a D-L4-T83-DEVOLVIDO (Lote 4)
- A v3.6 é igual à v3.5 mais a T-85. As duas erratas, T-83 e T-85, estão sobre a mesma base: o Lote 4 de HEAD 1bfae55 (LF d7d82036…; CRLF 7c4bb117…), que a fábrica tem como v3.4.
- A condição da D-L4-T83-DEVOLVIDO **continua não cumprida**. Ninguém conferiu, por leitura do Projeto do claude.ai, que GCB/Lote4_v3_canonica_GCB-CPP.md é, ignorando CR, igual a essa base. A fábrica (Claude Code) não tem acesso de leitura ao Projeto.
- Por isso a GCB **não reemite o gatilho E de aceite e transporte do Lote 4** neste ciclo. Escreve só um gatilho E de encaminhamento: a conferência vai ao Fundador, sem pedir aceite nem transporte.
- Até lá, a v3.6 é ativo de trabalho da GCB. O canônico do Lote 4 continua a v3.4 do Projeto, e a D-CANONICOS do Lote 4 não muda.
- Com o resultado da conferência:
  - **(i) igual:** a GCB reemite um só gatilho E para a v3.6 (T-83 + T-85; LF e26032129…), com a conferência registrada. A presidencia examina a ressalva "o Lote 4 não vai da fábrica ao Projeto".
  - **(ii) diferente:** a GCB alinha o espelho ao texto do Projeto, e as duas erratas são refeitas sobre ele pela cadeia gcb-cpp → gcb-cqfp → gcb-gerencia. Os textos de "leia-se" aprovados aqui e na T-83 servem de insumo a essa cadeia, mas não são reaplicados fora dela.
- A próxima T-12 não absorve nem a T-83 nem a T-85 no L4 antes do aceite. Se correr antes, a GBQ gera o L4 do texto de HEAD 1bfae55 (D-L4-T83-DEVOLVIDO).

## 7. Lote 5
- A base é a v3.2 canônica, já transportada (D-TRANSPORTE-L5-V32; LF 5f7f736c…, igual ao disco de HEAD). Não há pendência de base do lado da fábrica.
- A GCB emite o gatilho E: aceite da v3.3 como canônica e transporte ao Projeto no rito da D-TRANSPORTE-L5C-T83, com a mesma condição de execução: antes de substituir, conferir que o arquivo do Projeto é, ignorando CR, igual a LF 5f7f736c….
- Os derivados (saida/estudante/L5_estudo.md e L5_gabarito.md, pacote.json, pacote_estudante.json) absorvem na próxima T-12 após o aceite. Não há gatilho A agora: o pacote não muda nesta tarefa.

## 8. Não tocados
- saida/estudante/, saida/pacote/ e os geradores.
- Os registros históricos da T-83 (proposta, QA, reconciliação).
- A linha T-85 em TAREFAS.md, que o orquestrador fecha.
- Os Lotes 4-C e 5-C, sem resíduo segundo a produção e o QA.

## 9. Saídas
- PARA_PRESIDENCIA.md, ciclo s12c1: GATILHO E (Lote 5 v3.3, aceite e transporte) e GATILHO E (Lote 4 v3.6, encaminhamento ao Fundador da conferência de base; sem aceite nem transporte).
- TAREFAS.md: T-89 (GBQ, PRÓXIMO: absorção da T-83/T-85 na T-12 e O4) e T-90 (GCB, PRÓXIMO: O3, rótulos F5 e U1).
