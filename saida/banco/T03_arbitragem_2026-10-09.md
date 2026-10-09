# T03_arbitragem_2026-10-09.md — T-03 — 2026-10-09 — gerado por gbq-gerencia

- Parte da T-03 tratada aqui: arbitragem das aderências (D1 GBQ). A revisão da tipologia do guia (regras/estilo_banca.md v1.1) está com a gbq-estilo e não foi tocada; a GBQ a reconciliará depois.
- Entrada: saida/banco/qualidade_2026-10-09.md (gbq-cqe, seção "Divergências de mapeamento e de aderência"), saida/banco/R03_reconciliacao_2026-10-09.md, saida/simulados/simulado_0_v0.2_reconciliacao.md, banco/banco.csv, edital/TI_itens_5_8_P1.md, edital/modulo_RF_IA_P2.md, DECISOES.md, estado/ESTADO_CANONICO.md. Texto literal de TI 1–4 lido no Projeto (GCB/Lotes6_especificacao_PRES-S.md), só para a sugestão da GCB.
- Regras aplicadas: D-ADERENCIA (PARCIAL = só simulado diagnóstico), D-RECUPERACAO ("T-03 pelos ids originais"), D-ESCOPO / D-ESCOPO-2, D-ROTULOS. Critério de aderência (o mesmo da R-03 e do QA): DIRETA = o item cobra o que o subitem do edital nomeia; PARCIAL = tema vizinho ou genérico, ou ferramenta, norma ou recorte não nomeados no subitem.
- Nenhum gabarito, texto_integral, rótulo, URL ou anulado mudou. Só mudaram item_edital_camara (1 linha) e observacoes (12 linhas).

## As 7 aderências pendentes
São as 7 "Divergências registradas (duas leituras, sem decisão)" do QA de 09/10: **BQ-0001, BQ-0009, BQ-0014, BQ-0015, BQ-0016, BQ-0036, BQ-0040**. Delas, 6 foram marcadas "em arbitragem T-03" no Simulado 0 v0.2 (DIRETA*: 0001, 0009, 0015, 0016; DIRETA†: 0014, 0040). BQ-0036 já entrou no simulado como PARCIAL, com a observação do banco a corrigir (R-03 e R-04 a deixaram para a T-03).

## Arbitragem
| BQ-id | leitura A (banco) | leitura B (QA 09/10 ou alternativa) | decisão | motivo |
|---|---|---|---|---|
| BQ-0001 (TRF6 it. 63, comando "técnicas de visualização de dados") | P1-8.1, DIRETA ("poderia ser 8.1 ou 8.2") | P1-8.2 (gráficos em dois eixos), INDIRETA em 8.1 e em 8.2 | **P1-8.1, PARCIAL** (mantido o subitem) | O item diz só que gráficos exibem plotagens em dois eixos: não nomeia princípio (8.1) nem tipo (histograma, linha, barra, dispersão, box plot — 8.2). O próprio banco o chama de "item genérico de visualização", e genérico é PARCIAL pelo critério. Coerente com a leitura anterior da GCE/BIP (item 63: "P1-TI 8, aderência parcial"). 8.1 e 8.2 continuam com itens DIRETOS. |
| BQ-0009 (TRF6 it. 80, comando "inteligência artificial (IA)") | P1-5.3, DIRETA (alt. 5.2) | INDIRETA em 5.3 (análise preditiva não é IA generativa); mais próximo de P1-5 ou de 5.2 | **P1-5 (caput), DIRETA**. Subitem: P1-5.3 → P1-5 | O edital nomeia no caput "5 Conceitos básicos de inteligência artificial". Definir a análise preditiva como aplicação de IA que usa aprendizado de máquina sobre dados históricos é conceito básico de IA. Não é IA generativa (5.3) e não discrimina supervisionado, não supervisionado ou por reforço (5.2). Coerente com o destino que a GCE já tinha dado ao item 80 ("P1-TI 5", Estado Canônico). O mapeamento em caput tem precedente no banco (P1-6). |
| BQ-0014 (BCB it. 59, comando "LLM e IA generativa") | P1-5.3, DIRETA | DIRETA em 5.3; leitura possível em P1-5.1 | **P1-5.3, DIRETA** (sem mudança) | Temperature é parâmetro de amostragem da geração de texto de um LLM: conceito de IA generativa, sob comando literal de IA generativa. Não é técnica de redação de prompt (5.1). A leitura 5.1 fica registrada. |
| BQ-0015 (BCB it. 60, "thread") | P1-5.3, DIRETA (sem sinalização) | INDIRETA: conceito de API de fornecedor (objeto "thread" de API de assistentes), não nomeado no edital | **P1-5.3, PARCIAL** | O gabarito E depende do vocabulário de objetos de uma API de assistentes (a thread × a entidade configurável com modelo, instruções e ferramentas). Não é conceito, exemplo ou caso de uso de IA generativa no sentido do 5.3. A marca VOLÁTIL da R-04 (T-15, T-16) segue independente. |
| BQ-0016 (BCB it. 64, comando "privacidade em governança e ética de IA") | P1-6, DIRETA | INDIRETA em P1-6 (ética de IA em geral, não no serviço público); alt. P2-4.2, também INDIRETA | **P1-6, PARCIAL** (mantido o subitem) | O 6 nomeia "ética e responsabilidade digital **no serviço público**". O item cobra a transparência algorítmica em termos gerais, sem o recorte do serviço público. É o mesmo critério do recorte que já torna PARCIAIS os itens de LGPD geral (P2-4.1) e de segurança geral (P2-4.3). O P2-4.2 trata de direitos autorais e ética no conteúdo gerado por IA, e o item não trata disso. |
| BQ-0036 (CNJ it. 97, comando "LGPD e Marco Civil da Internet") | P2-4.1, PARCIAL ("LGPD/privacidade geral") | INDIRETA: cobra princípios do Marco Civil da Internet (Lei 12.965/2014), não a LGPD; a observação do banco descreve mal o conteúdo | **P2-4.1, PARCIAL** (mantido); observacoes corrigida | O 4.1 nomeia "LGPD e proteção de dados em sistemas de transcrição e IA". O item toca a proteção de dados (princípio do uso da Internet), mas por outra lei e sem o contexto de transcrição e IA. Nenhum outro subitem do escopo o acolhe melhor. A atualidade do gabarito frente ao texto vigente da lei não é conferida aqui: vai ao qa-normativo (T-21), porque a T-13 cobre só a LGPD. |
| BQ-0040 (CNJ it. 113, comando "Resoluções CNJ 468/2022, 396/2021, 335/2020 e 332/2020") | P1-6, DIRETA | DIRETA em P1-6; alt. P2-4.2, INDIRETA | **P1-6, DIRETA** (sem mudança) | O item cobra a conduta que uma norma de órgão público (o CNJ) impõe diante de viés discriminatório de IA: é ética e responsabilidade digital no serviço público, como o 6 nomeia. Não trata de conteúdo gerado nem de direitos autorais (4.2). A vigência e a redação atual das resoluções citadas não foram conferidas ([SEM FONTE — não afirmar]). Vão ao qa-normativo na T-21, e o gabarito não muda sem gatilho D. |

### Itens apontados como "em arbitragem T-03" fora dos 7
Nenhum. Os 6 itens apontados na R-03 e na R-04 (BQ-0001, 0009, 0014, 0015, 0016, 0040) estão entre os 7 acima.

### Sugestão da GCB (sem gatilho): remapear BQ-0011 e BQ-0012 de P2-4.3 para P1 TI 4/4.1
| BQ-id | leitura A (banco) | leitura B (GCB) | decisão | motivo |
|---|---|---|---|---|
| BQ-0011 (TRF6 it. 96, integridade, E), BQ-0012 (TRF6 it. 98, disponibilidade, C) | P2-4.3, PARCIAL (princípio geral de segurança; o 4.3 trata de pipelines de áudio e transcrição) | P1 TI 4/4.1, como no Lote 6b ("aderência parcial ao item 4/4.1") | **Mantido P2-4.3, PARCIAL**. Remapeamento em **gatilho D** (escopo do banco). Extensão: BQ-0038 (integridade, C) e BQ-0039 (autenticidade, E), mesma natureza. | O subitem proposto não está no escopo do banco: edital/TI_itens_5_8_P1.md transcreve só os itens 5–8 e declara os itens 1–4 "fora do escopo do Projeto". A D-ESCOPO-2 trouxe os itens 1–4 "via Lotes 6a/6b", e não pelo banco. Pelo texto literal (especificação dos Lotes 6), a âncora exata seria o caput "4 Conceitos gerais de segurança e governança digital", e não o 4.1, que nomeia backup, vírus, worms e pragas virtuais. Nesse caput, os 4 itens (tríade CIA e autenticidade) seriam DIRETOS. Mudar o universo de subitens do banco é decisão de escopo (D2), e não D1. Deduplicação P9 × BQ: TRF6 96 = BQ-0011, TRF6 98 = BQ-0012. O banco é a fonte, e o Lote 6b os cita fora dos seus 15 itens. |

## Alterações em banco/banco.csv (antes → depois)
Formato preservado byte a byte: csv.reader/csv.writer, delimiter=';', lineterminator='\n', QUOTE_MINIMAL. A releitura sem mudança reproduziu o arquivo idêntico antes da edição. Continuam 67 linhas e 15 colunas, terminação LF, sem CR. A comparação coluna a coluna com a cópia anterior mostra mudanças só nas colunas item_edital_camara (1) e observacoes (12).
| ID | campo | antes → depois |
|---|---|---|
| BQ-0001 | observacoes | "…; item genérico de visualização; poderia ser 8.1 ou 8.2" → "…; item genérico de visualização; aderência PARCIAL P1-8.1, D1 GBQ T-03 (só simulado diagnóstico, D-ADERENCIA; leitura alternativa 8.2 registrada)" |
| BQ-0009 | item_edital_camara | P1-5.3 → P1-5 |
| BQ-0009 | observacoes | "…; alternativa de enquadramento P1-5.2" → "…; aderência DIRETA P1-5, D1 GBQ T-03 (análise preditiva como aplicação de IA: conceito básico do item 5; leituras alternativas 5.2 e 5.3 registradas)" |
| BQ-0014 | observacoes | acréscimo ao final: "; aderência DIRETA P1-5.3, D1 GBQ T-03 (parâmetro de geração de LLM; leitura alternativa 5.1 registrada)" |
| BQ-0015 | observacoes | acréscimo ao final: "; aderência PARCIAL P1-5.3, D1 GBQ T-03 (objeto de API de assistentes de fornecedor, não nomeado no edital; só simulado diagnóstico, D-ADERENCIA)". O prefixo VOLÁTIL da T-15, ainda pendente, é compatível. |
| BQ-0016 | observacoes | acréscimo ao final: "; aderência PARCIAL P1-6, D1 GBQ T-03 (ética de IA em geral, sem o recorte do serviço público; leitura alternativa P2-4.2 registrada, também parcial; só simulado diagnóstico, D-ADERENCIA)" |
| BQ-0036 | observacoes | "…; aderência temática ampla (LGPD/privacidade geral; edital 4.1 trata de LGPD em sistemas de transcrição e IA)" → "…; aderência PARCIAL P2-4.1, D1 GBQ T-03 (cobra princípios do Marco Civil da Internet, Lei 12.965/2014 — privacidade e dados pessoais —, não a LGPD nem sistemas de transcrição e IA; só simulado diagnóstico, D-ADERENCIA); qa-normativo T-21" |
| BQ-0040 | observacoes | acréscimo ao final: "; aderência DIRETA P1-6, D1 GBQ T-03 (viés discriminatório de IA em norma de órgão público, CNJ; leitura alternativa P2-4.2 registrada); vigência e redação das Resoluções CNJ: qa-normativo T-21" |
| BQ-0011, BQ-0012, BQ-0038, BQ-0039 | observacoes | acréscimo ao final: "; remapeamento para P1 TI 4 (conceitos gerais de segurança; D-ESCOPO-2) fora do escopo do banco em edital/: mantido P2-4.3 PARCIAL, D1 GBQ T-03; gatilho D à Presidência" |

Contagem do banco após a T-03: 66 itens; nenhum gabarito alterado (60 válidos, 33 C e 27 E; 6 anulados). Por subitem: P1-5 = 1 (chave nova, caput), P1-5.3 = 13 (antes 14), sem outra mudança de contagem.

## Efeito no Simulado 0 v0.2 (não editado; ajuste vai à T-20)
| item | BQ-id | antes | depois | o que muda no simulado |
|---|---|---|---|---|
| 15 | BQ-0009 | DIRETA*, P1-5.3 | **DIRETA, P1-5** | sai a marca "[ADERÊNCIA EM ARBITRAGEM — T-03]"; subitem do mapa e cobertura (P1-5.3 −1; P1-5 +1) |
| 17 | BQ-0014 | DIRETA† | **DIRETA** | sai a nota de arbitragem do mapa |
| 18 | BQ-0015 | DIRETA* | **PARCIAL** (DIRETA → PARCIAL) | a marca de arbitragem dá lugar a "[ADERÊNCIA PARCIAL — objeto de API de assistentes de fornecedor, não nomeado no 5.3]"; segue VOLÁTIL (T-15) |
| 26 | BQ-0016 | DIRETA* | **PARCIAL** (DIRETA → PARCIAL) | marca "[ADERÊNCIA PARCIAL — ética de IA em geral, sem o recorte do serviço público do 6]" |
| 27 | BQ-0040 | DIRETA† | **DIRETA** | sai a nota de arbitragem do mapa |
| 31 | BQ-0001 | DIRETA* | **PARCIAL** (DIRETA → PARCIAL) | marca "[ADERÊNCIA PARCIAL — item genérico de visualização; não nomeia princípio (8.1) nem tipo (8.2)]" |
| 51 | BQ-0036 | PARCIAL | PARCIAL (sem mudança de classe) | o motivo no mapa e na marca passa a citar o Marco Civil, Lei 12.965/2014, e não "LGPD/privacidade geral"; a referência "T-03" passa a "T-21" |

- Nenhum item muda de PARCIAL para DIRETA. Três mudam de DIRETA (marcada em arbitragem) para PARCIAL: 18, 26 e 31. Três saem da arbitragem como DIRETA: 15, 17 e 27.
- Contagens novas: DIRETA 33 (todos de P1), PARCIAL 27 (P1 6: 5.3, 6, 7.1, 8.1 e 8.3 ×2; P2 21), em arbitragem 0. Aviso 1/2: 24 → 27 PARCIAIS. Aviso 3 (arbitragem T-03) sai ou é substituído por "resolvida na T-03". A linha "Marcas de montagem" e a legenda (DIRETA*/DIRETA†) também mudam.
- Elegibilidade: nenhum item sai do diagnóstico, nem a montagem muda. Gabarito, ordem, numeração e comandos ficam iguais. A cobertura de P1 continua com item DIRETO em 8 dos 9 subitens (5.3, 6 e 8.1 mantêm DIRETOS: BQ-0010/0014, BQ-0040, BQ-0021/0022), e entra a chave P1-5 (caput). Falta o 8.4.
- O gatilho A pendente do Simulado 0 v0.2 (PARA_PRESIDENCIA.md: "30 DIRETA, 6 em arbitragem T-03, 24 PARCIAL") fica com contagens desatualizadas, sem mudar a pergunta. Isso vai como informação no gatilho D.

## Tarefas novas (append único em TAREFAS.md)
- T-20 (PRÓXIMO): ajuste mecânico do Simulado 0 v0.2 pós-T-03, junto com a T-15 ou depois dela, antes de qualquer entrega. Não muda item, ordem, numeração, comando nem gabarito.
- T-21 (PRÓXIMO): qa-normativo de BQ-0036 (Marco Civil, Lei 12.965/2014, planalto.gov.br compilado) e de BQ-0040 (vigência e redação das Resoluções CNJ 332/2020 e correlatas, em fonte oficial do CNJ). Confere a atualidade do gabarito sem mudá-lo; divergência vira gatilho D. Complementa a T-13, que cobre só a LGPD.
- T-22 (PRÓXIMO, BLOQUEADA até a resposta ao gatilho D): se a resposta for SIM, transcrever o texto literal de TI 1–4 em edital/ e remapear BQ-0011, 0012, 0038 e 0039 para P1-4, DIRETA.

## Gatilhos
- GATILHO D (escopo do banco: itens 1–4 de TI), um único append em PARA_PRESIDENCIA.md. As demais decisões são D1 do domínio da GBQ: não mudam gabarito, rótulo nem escopo, e não há conflito.

## Revisão da tipologia v1.1 (regras/estilo_banca.md, gbq-estilo) — item (a) da GBQ
- Método: conferência automatizada de cada BQ-id citado como item de padrão (seções 3.1 a 3.12, excluídos contrastes e contraexemplos) contra banco/banco.csv. Para cada um: gabarito igual ao do guia, anulado=nao, sem "QA PENDENTE", e trecho entre aspas contido literalmente no texto_integral. Também conferi a partição da base, com cada item em exatamente um padrão.
- Resultado: os 60 itens com gabarito válido estão classificados uma única vez (0 faltando, 0 duplicados, 0 anulados ou X). Gabarito confere em 60 de 60. Todos os trechos são literais. A única ocorrência fora do texto foi o "todo" de BQ-0001 (C6), que é comentário do guia ("não diz 'todo'") e não citação. As somas fecham: E 27 (E1 6, E2 5, E3 5, E4 5, E5 3, E6 3) e C 33 (C1 17, C2 4, C3 6, C4 2, C5 1, C6 3).
- Regra "padrão com menos de 3 itens = removido ou indício": CUMPRIDA. Os 10 padrões têm n ≥ 3. C4 (2) e C5 (1) são indícios, assim como os traços "prioritariamente" (1), "causa falsa" pura (1) e "desde que" (2). Sem VOLÁTIL, nenhum padrão cai abaixo de 3: E1 fica com 5 sem BQ-0015, e C1 com 14 sem BQ-0017, 0035 e 0064.

| ponto | decisão D1 | motivo |
|---|---|---|
| Inclusão de BQ-0025 (E6) | CONFIRMADA. E6 fica como padrão (n = 3: BQ-0025, 0052, 0053) | É coerente com a D1 (i) da R-04: o CORRIGIR do QA de 09/10 foi só em observacoes, e o banco já registra "gabarito preliminar C alterado para E no definitivo". Texto literal, gabarito E definitivo e proveniência foram conferidos pela gbq-cqe. A pendência normativa (T-13) afeta o conteúdo vigente, não o mecanismo de estilo, e o guia já faz essa ressalva. |
| Ampliação do E5 ("cauda" → "segmento acessório") | ACEITA. E5 fica como padrão (n = 3: BQ-0002, 0041, 0058) | O tipo 3 da semente já junta causa e consequência falsas ("verdadeira com causa/consequência falsa"). BQ-0041 (consequência) e BQ-0058 (premissa causal no meio da frase) têm o mesmo mecanismo: moldura verdadeira e um só segmento falso. A regra de desempate E4/E5/E6 do guia delimita bem a fronteira. A marca "sensível" fica como ressalva de n pequeno, e não como pendência. |
| C6 (padrão novo) | ACEITO (n = 3: BQ-0001, 0059, 0065) | Os três itens afirmam uma parte verdadeira sem marcador de exclusividade, e o gabarito C confirma que incompleto não é errado. É o espelho do E6, útil para o pareamento E6 × C6 na produção. É coerente com a T-03: BQ-0001 é "genérico" (PARCIAL), o que não afeta o mecanismo. |
| Fronteiras (BQ-0050, 0053, 0004, 0048, 0054) | MANTIDAS como o guia as classificou | A regra de desempate explícita resolve todas, e nenhuma muda a contagem de padrão abaixo de 3. |
| Coerência com a arbitragem T-03 | Ajuste de texto necessário, sem mudar a tipologia | O guia cita BQ-0009 em P1-5.3 (tabela C1 e tabela por subitem da seção 2), e o banco agora diz P1-5. A seção 6.6 ainda dá as 7 divergências como "em arbitragem". A seção 6.7 não cita a T-21. |

### Ajustes a fazer no guia (sem reescrita pela GBQ) — destinatário: gbq-estilo (T-23)
1. Seção 2, tabela por subitem: a linha P1-5.3 passa de "7 | 4 | 3" para "6 | 4 | 3", com a observação "BQ-0009 remapeado para P1-5 (T-03)". Acrescentar a linha "P1-5 | 1 | 0 | 0 | ausente | BQ-0009; DIRETA (D1 T-03)". A soma de P1 não muda (21/18/5).
2. Seção 3.7, tabela C1: o subitem de BQ-0009 passa de "P1-5.3" para "P1-5".
3. Seção 6, ressalva 1: registrar a revisão da GBQ em 09/10 (T-03): BQ-0025 confirmada, E5 ampliado aceito, C6 aceito, fronteiras mantidas. Ressalva 4: BQ-0025 confirmada. Ressalva 6: trocar "em arbitragem paralela" pelos resultados da T-03 (DIRETA: 0009 em P1-5, 0014 e 0040; PARCIAL: 0001, 0015, 0016 e 0036). Ressalva 7: BQ-0036 e BQ-0040 vão à T-21. Seção 7: anotar "revisada pela GBQ (T-03)".
4. AVISO final: "exige revisão da GBQ antes de orientar produção" → "revisada pela GBQ em 09/10/2026 (T-03); apta a orientar produção após os ajustes 1–3".
- Enquanto a T-23 não for aplicada, a v1.1 pode orientar a produção quanto à tipologia: nada nos ajustes muda padrão, contagem de padrão ou recomendação.

### Gatilho A do Simulado 0 v0.2 (PARA_PRESIDENCIA.md)
Só a linha da GBQ foi corrigida, numa única leitura e regravação. "30 DIRETA, 6 em arbitragem T-03, 24 PARCIAL" passou a "33 DIRETA, 27 PARCIAL, 0 em arbitragem (após a arbitragem T-03 de 09/10; marcas no simulado pelo ajuste mecânico T-20, sem item retirado)". As demais linhas não mudaram (diferença conferida: só a linha 4).

### Estado da T-03
A parte da GBQ está CONCLUÍDA: arbitragem das aderências e revisão da tipologia v1.1. Ficam pendentes a T-20, a T-21, a T-22 (aguarda o gatilho D) e a T-23 (errata do guia).
