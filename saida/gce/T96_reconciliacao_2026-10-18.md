# T96_reconciliacao_2026-10-18.md — T-96 — 2026-10-18 — gerado por gce-gerencia

Objeto: reconciliação da T-96 (REFORÇO onda 2, P2 folhas 1.1 a 1.8; D-REFORCO-2), ciclo 2026-10-18 s12c3. 112 itens produzidos (L1-R19 a L1-R130), em 4 partes.
Base lida: TAREFAS.md (T-96); DECISOES.md (D-REFORCO-1, D-REFORCO-2, D-FONTE-DATA-ANTERIOR, D-T89-R1-ACEITE, D-T91-R3-ACEITE, D-ONDA2-FILA, D-RITMO-MAX); critérios desta Gerência em T89_, T90_ e T91_reconciliacao_2026-10-18.md; finais saida/gce/L1_reforco_onda2_A_v2.md (SHA-256 667ae95a…3088a26c), B_v2 (201a3172…4c7b23e), C_v2 (37043a8c…64cfce3), D_v2 (2762f17b…3d77a5fb); pareceres QA_T96A/B/C/D_R1 e R2_2026-10-18_gce-cqfp.md; edital/modulo_RF_IA_P2.md; saida/pacote/pacote.json v1.9 (busca de gêmeos em P2).
A GCE não escreve em PARA_PRESIDENCIA.md nem em TAREFAS.md: os textos das seções 8 e 9 são para o orquestrador colar. Nenhum enunciado nem gabarito muda. As únicas mudanças de texto em (d-G) são a regência do R129, ditada pela QA, e dois rótulos de VOLÁTIL (seção 2).

## 1. D1: L1-R43 RETIRADO; reposição por item novo em tarefa de saldo (L1-R131)
- O R43 da v2 foi reprovado na R2, que é a última rodada: é fato de tabela de repositório, não conceito de 1.2 (QA_T96A_R2, seção 4). Ajuste nesta parte não cabe mais. O item sai em definitivo, e o id L1-R43 não é reutilizado: já designou dois textos (sotaques na v1, wav2vec na v2).
- Deixar a 1.2 em 19 de vez descumpriria a meta do Fundador ("no mínimo 20"; D-REFORCO-2), e isso esta Gerência não pode decidir. Por isso a decisão é repor.
- A reposição é PRODUÇÃO NOVA, com id novo (L1-R131), R1 própria da gce-cqfp e no máximo 2 rodadas. Não é uma 3ª rodada da parte A.
- Requisitos do item novo:
  - folha P2-1.2;
  - gabarito E com [TS] de troca única, o que devolve o [TS] da parte A a 16;
  - formato diferente de "definição" (restrição da T-89) e de "par confundível" (PC já está em 5/19); de preferência, troca de sujeito;
  - ponto conceitual de modelo end-to-end, e não célula de tabela, checkpoint ou lista;
  - ponto distinto dos 19 da folha e sem gêmeo em outra folha (seção 4);
  - base oficial aberta na data, com trecho literal;
  - não VOLÁTIL.
- Cabe agora: é saldo da onda 2, e não lote novo. Deve correr logo depois desta reconciliação e antes de a T-97 começar, porque nenhum lote novo começa com QA aberta (D-RITMO-MAX).
- O gatilho A dos 111 não espera o saldo (precedente D-T92-R4-PARCIAL/T-102). O L1-R131 entra na mesma consolidação v1.10 (D-REFORCO-2), sem perda de calendário.
- Se o saldo for reprovado nas 2 rodadas, o caso volta a esta Gerência. Uma 1.2 com 19 itens iria então à Presidência como gatilho.

## 2. D1: VOLÁTIL (R120, R128; R87 × R101/R84; uniformização dos gêmeos)
2.1 Precisão do critério. É a aplicação do critério da T-89, seção 1, ratificado na D-T89-R1-ACEITE, que já tratou o R17 (divisão estrutural de serviço) como não VOLÁTIL. Vai à ratificação no gatilho A.
- VOLÁTIL é o item cujo gabarito depende de:
  - (a) versão, limite, preço ou modelo padrão;
  - (b) comportamento PADRÃO de produto ou exigência de parâmetro NOMEADO de API;
  - (c) existência ou disponibilidade de recurso que a própria documentação condiciona (modelo, local, versão de SDK, prévia) ou que é periférico;
  - (d) comportamento ilustrado só em saída de exemplo de um serviço.
- NÃO VOLÁTIL é o item que julga o funcionamento documentado de um recurso CENTRAL do serviço, isto é, o papel, o mecanismo, a divisão estrutural ou a sintaxe do recurso, sem número, versão, preço, padrão ou disponibilidade condicionada. Também é não VOLÁTIL a boa prática documentada sem esses elementos.
- Todo item com base em página de fornecedor fica com REVERIFICAR / conferência de base em 4–8/1/2027 (T-11, parte P2, gce-cqfp).
- A marcação conservadora (VOLÁTIL a mais) é admitida dentro do teto. A marcação a menos não é.
2.2 R120 (phrase list em tempo de execução, sem treino) e R128 (WER contra transcrição humana como critério para treinar custom speech): NÃO VOLÁTEIS. A folha 1.8 fica com 2/20 (Q18, Q19; 10%).
- Sem esta precisão, a leitura literal ("existência de recurso") faria virar VOLÁTEIS também R123 e R130. A 1.8 iria a 6/20 (30%), acima do teto da regra 4, e só fecharia com substituições, que é exatamente o risco evitado na T-89.
2.3 R87 × R101/R84:
- R87 continua VOLÁTIL (baixo/médio), pelas hipóteses (b) e (c): nomes de seção (#rewrite/#itn) de recurso que a página condiciona a modelos base e locais com suporte.
- R101 (hífen na entrada de várias palavras) e R84 (coluna DisplayAs) ficam NÃO VOLÁTEIS: sintaxe e função de recurso central, sem nome condicionado.
- Na mesma linha, ficam mantidos: R54, R67 e R69 VOLÁTEIS (parâmetro nomeado ou padrão); R65 VOLÁTIL (saída de exemplo); R71 não (refutado por dois serviços). R57 VOLÁTIL baixo fica por marcação conservadora.
2.4 Uniformização dos gêmeos de mesmo trecho-base (D1, seção 4). R24 e R29 (1.1) estavam como VOLÁTIL baixo, e os gêmeos R125 (1.8) e R91 (1.6), sobre os mesmos trechos da página "Best practices" do Google, estavam como não VOLÁTEIS. Pela regra "mesmo trecho, mesmo rótulo" e pela hipótese de boa prática da 2.1 (a mesma que a QA aplicou a R23 e R25, da mesma página), R24 e R29 passam a NÃO VOLÁTEIS, com conferência de base mantida. A 1.1 vai a 0/20. A mudança é transcrita no A_v3 (seção 5.1).
2.5 A restrição da T-89, seção 3 ("nenhum VOLÁTIL novo em 1.8 até a folha voltar a ≤ 20%"), está cumprida (0 novos em 1.8). O teto "4 VOLÁTEIS por lote" é da D-REFORCO-1 (onda 1). Na onda 2 vale a regra 4 da D-REFORCO-2 (≤ 20% por folha). Fica registrado para a Presidência: o Lote 1 passa de 4 para 15 VOLÁTEIS, 11 deles novos e nenhum de risco alto novo.

## 3. D1: R99 e correções de registro sem R3
- R99: o "C [TS]" segue a convenção O-6 (espelho admitido) e fica. O formato é reclassificado para PAR CONFUNDÍVEL, pelo critério ratificado na D-T91-R3-ACEITE (o formato segue a construção do ponto).
  - A 1.6 fica com D 4, PC 3 (15%), dentro do teto.
  - A diluição de PC pedida na T-89 está cumprida: a folha de 20 está em 15%.
  - A notação "C [TS] (espelho)" na parte A e "C [TS]. Falsa pegadinha" nas partes B, C e D é equivalente e não afeta a consolidação.
- Valem só nesta reconciliação, que prevalece sobre o mapa e a proveniência na consolidação (precedente T-89, seção 4):
  - C_v2: R99 com formato PC (linhas 64, 98, 348, 378 e 379 da v2 ficam superadas por este registro);
  - C_v2, proveniência: a linha 400 inclui R102 por erro (a base do R102 é o Google adaptation-model); a linha 405 ("Create a batch transcription") não sustenta nenhum item da v2;
  - B_v2: o mapa de R47, R48, R52 e R54 mantém a URL citada, e a URL final está na proveniência, o que basta;
  - R58 fica com o formato declarado (definição), e a leitura alternativa como PC (4/20) fica registrada, sem efeito.
- Linhas do arquivo final que mudam, para não levar defeito ao (d-G), transcritas no D_v3 (seção 5.2):
  - regência da justificativa do R129, na linha 288, com o texto aceito pela QA;
  - localização do trecho do R124, na linha 79: o trecho está no 3º parágrafo de "Evaluated Use", e o do R126 no 2º.
- A_v3 (seção 5.1): saída do R43; R24 e R29 com o rótulo da 2.4; linhas 345 e 346 da proveniência, que atribuíam R43 e R44 ao model card e R43 ao fairseq.
- Registros de estilo, sem efeito, a observar pelo gbq-estilo:
  - O-1 na parte B: C 40,5 × E 39,4;
  - abertura "Segundo a…" repetida (parte C, 5 itens);
  - R124: o contexto "reuniões reservadas" fica perto de vínculo implícito;
  - R68: baixa discriminação.
- QA PENDENTE: cai com esta reconciliação nos 111 itens (precedente T-89, seção 5). O "QA PENDENTE" escrito nos v2/v3 é histórico.

## 4. D1: duplicatas, conferidas pela Gerência nos 112 pontos, entre as partes e contra a onda 1 e os canônicos
- Dentro de cada folha: nenhuma duplicata, conferida item a item contra os 6 existentes e entre os 14 novos. As vizinhanças declaradas pelas produtoras e pela QA estão aceitas: R19 × Q22; R32 × R02; R45 × R04; R41 × R44; R81/R82/R85 (concentração de TER em 1.5, 3/20); R93 × R95; R109 × Q15; R111 × Q17; R124 × R126/R122.
- Entre folhas: há GÊMEOS, isto é, o mesmo ponto em folhas diferentes. Pela regra 1 (o ponto é vedado por folha) e pelo precedente R12 × L1C-Q21 (T-89), todos são ACEITOS como reforço em outra folha, sem rejeição.

| gêmeo | folhas | gab. | trecho-base comum | VOLÁTIL (após a seção 2) |
|---|---|---|---|---|
| R35 × R119 | 1.2 × 1.8 | E × E | model card do Whisper, 65% inglês/inglês | n / n |
| R23 × R118 | 1.1 × 1.8 | E × C | Google, codec sem perdas | n / n |
| R25 × R121 | 1.1 × 1.8 | C × E | Google, não reamostrar 8.000 Hz | n / n |
| R24 × R125 | 1.1 × 1.8 | E × E | Google, redução de ruído reduz a acurácia | n / n |
| R29 × R91 | 1.1 × 1.6 | E × C | Google, vozes simultâneas tratadas como ruído | n / n |
| R20 × R93 | 1.1 × 1.6 | C × E | Azure, supressões × sinal fraco; substituições × domínio | n / n |
| R94 × R120 | 1.6 × 1.8 | E × C | Azure, phrase list em tempo de execução, sem treino | n / n |
| R115 × L1-Q07 | 1.7 × 1.4 | E × (canônico) | rótulo genérico, e não nome do orador | n / n |

- Proximidades sem gêmeo, registradas: R58 × R107 (requisição completa × fluxo); R62 × Q20/Q18; R36 × R11; R37 × L2-R04; R105 × R25 (16 kHz); R19 × R82 (denominador na referência, WER × TER); R120/R94 × L2-R18 (2.8: limite numérico da phrase list, outro ponto).
- Registro para a GBQ, cuja decisão é da GBQ: os gêmeos não devem figurar no mesmo simulado ou caderno.
- Instrução desta Gerência para as ondas 3 e 4 (T-97, T-98): a produção confere o ponto contra o pacote inteiro, e não só contra a folha. Gêmeo em outra folha só entra declarado e com ângulo próprio da folha.

## 5. D1: versões finais e transcrição (sem R3)
- B: L1_reforco_onda2_B_v2.md é FINAL (sem v3).
- C: L1_reforco_onda2_C_v2.md é FINAL (sem v3), com os registros da seção 3.
- A e D: v3 por transcrição literal pela gce-cpp, com números de linha da v2.
- Não há R3, porque nenhum enunciado, gabarito ou [TS] muda. A regência do R129 é o texto da própria QA. O resto é retirada de item reprovado, rótulo, contagem e proveniência.

### 5.1 saida/gce/L1_reforco_onda2_A_v3.md = A_v2 com só estas mudanças
L1 →
# L1_reforco_onda2_A_v3.md — T-96 — 2026-10-18 — gerado por gce-cpp

Inserir, logo depois da linha 1, uma linha em branco e a linha:
Versão v3: transcrição da reconciliação saida/gce/T96_reconciliacao_2026-10-18.md, seção 5.1. L1-R43 foi retirado (reprovado na R2 da gce-cqfp; id não reutilizado) e não integra esta versão; a parte A tem 27 itens (P2-1.1: 14; P2-1.2: 13). R24 e R29 passam a não VOLÁTEIS (D1 da gce-gerencia, seção 2). A resposta ao parecer, a descrição de escopo e de QA PENDENTE (linhas 29–30), a verificação de não repetição, a linha de registros de estilo O-1 a O-8 e as dúvidas são histórico da v2.

APAGAR as linhas 75, 211, 212, 213, 306, 307 e 308 (L1-R43 no mapa, na Parte 2 e na Parte 3, com as linhas em branco que as seguem).

L51 →
| L1-R24 | P2-1.1 | Segundo a documentação do Google, o processamento de redução de ruído aplicado antes do envio tende a reduzir, e não a elevar, a acurácia | PC | https://cloud.google.com/speech-to-text/docs/best-practices (seção "Audio preprocessing") | n |
L56 →
| L1-R29 | P2-1.1 | Segundo a documentação do Google, vozes simultâneas ou em volumes diferentes, em canal único, podem ser interpretadas como ruído de fundo e ignoradas | AP | https://cloud.google.com/speech-to-text/docs/best-practices (tabela de recomendações) | n |
L80 →
VOLÁTIL novos: 0 (R24 e R29 reclassificados como não VOLÁTEIS: boa prática documentada, sem número, versão ou padrão de produto, com o mesmo rótulo dos gêmeos L1-R125 e L1-R91; D1 da gce-gerencia, reconciliação T-96, seção 2). Risco alto: 0.
L95 →
| L1-R19 a R32 | ver tabela acima | NP, AP, SH, SH, AP, PC, NP, D, TS, AP, AP, PC, PC, D | n (14) |
L98 →
VOLÁTEIS na folha: 0/20; existentes: 0.
L109 →
| L1-R33 a R46 (sem R43) | ver tabela acima | PC, AP, NP, SH, AP, AP, SH, TS, PC, AP, PC, SH, PC | n (13) |
L111 →
Contagem de formatos na folha de 19 (L1-R43 retirado): D 2 (Q03, Q24) = 10,5%, sem item novo de definição (restrição da T-89, seção 3); PC 5 (Q04, R33, R41, R44, R46) = 26,3%; TS 2 (R03, R40) = 10,5%; NP 2 (R04, R35) = 10,5%; SH 4 (Q23, R36, R39, R45) = 21,1%; AP 4 (R34, R37, R38, R42) = 21,1%. Soma 19. Maior formato: PC com 26,3% (teto de 30% cumprido).
L112 →
VOLÁTEIS na folha: 0/19.
L129 →
- VOLÁTIL: 0 novos; 1.1 = 0/20; 1.2 = 0/19.
L130 →
- Gabarito da parte: 14 C e 13 E (51,9% de C). Por folha: 1.1 com 7 C e 7 E; 1.2 com 7 C e 6 E.
L131 →
- [TS]: 15/27 (55,6%); a meta de metade dos itens mais 2 é conferida na onda inteira (reconciliação T-96, seção 6). 11 em itens E e 4 em itens C (espelho); 2 itens E sem [TS] (R21, R38).
L248 →
Base: Google Cloud, "Best practices", seção "Audio preprocessing" (https://cloud.google.com/speech-to-text/docs/best-practices; "Last updated 2026-10-13"), verificado em 18/10/2026. Não VOLÁTIL (boa prática documentada, sem número, versão ou padrão de produto; D1 da gce-gerencia, reconciliação T-96, seção 2). CONFERÊNCIA DE BASE em 4–8/1/2027: reabrir a URL e conferir "applying noise-reduction signal processing to the audio before sending it to the service typically reduces recognition accuracy".
L263 →
Base: Google Cloud, "Best practices", tabela de recomendações (https://cloud.google.com/speech-to-text/docs/best-practices; "Last updated 2026-10-13"), verificado em 18/10/2026. Não VOLÁTIL (boa prática documentada, sem número, versão ou padrão de produto; D1 da gce-gerencia, reconciliação T-96, seção 2). CONFERÊNCIA DE BASE em 4–8/1/2027: reabrir a URL e conferir "Multiple people talking at the same time, or at different volumes may be interpreted as background noise and ignored".
L322 →
| total | 27 (14 em P2-1.1, 13 em P2-1.2; L1-R43 retirado) |
L323 →
| C | 14 (R20, R22, R25, R26, R28, R31, R32, R34, R36, R37, R39, R42, R45, R46) = 51,9% |
L324 →
| E | 13 (R19, R21, R23, R24, R27, R29, R30, R33, R35, R38, R40, R41, R44) = 48,1% |
L325 →
| C por folha | 1.1: 7 C / 7 E; 1.2: 7 C / 6 E |
L326 →
| [TS] | 15 (R19, R23, R24, R25, R27, R28, R29, R30, R33, R35, R39, R40, R41, R44, R46): 11 em E e 4 em C (R25, R28, R39, R46); E sem [TS]: R21 e R38 |
L327 →
| VOLÁTIL | 0 novos (R24 e R29 reclassificados; reconciliação T-96, seção 2); risco alto: 0 |
L328 →
| VOLÁTEIS por folha | P2-1.1: 0/20; P2-1.2: 0/19 |
L330 →
| Formatos P2-1.2 (de 19) | D 2, PC 5, TS 2, NP 2, SH 4, AP 4 (maior: 26,3%); definição nova: 0 |
L331 →
| CONFERÊNCIA DE BASE (jan/2027) | R19 a R42 e R44 a R46 (todos os 27; nenhum VOLÁTIL) |
L332 →
| REVERIFICAR (VOLÁTEIS) | nenhum |
L345 →
| OpenAI, repositório oficial openai/whisper, model-card.md (ramo main) | https://raw.githubusercontent.com/openai/whisper/main/model-card.md | arquivo aberto e lido em 18/10/2026 (HTTP 200) | R35, R36, R37, R38 |
L346 →
| Meta, repositório oficial facebookresearch/fairseq, README do wav2vec 2.0 | https://raw.githubusercontent.com/facebookresearch/fairseq/main/examples/wav2vec/README.md | arquivo aberto e lido em 18/10/2026 (HTTP 200) | R34, R42 |

Nada mais muda.

### 5.2 saida/gce/L1_reforco_onda2_D_v3.md = D_v2 com só estas mudanças
L1 →
# L1_reforco_onda2_D_v3.md — T-96 — 2026-10-18 — gerado por gce-cpp

Inserir, logo depois da linha 1, uma linha em branco e a linha:
Versão v3: transcrição da reconciliação saida/gce/T96_reconciliacao_2026-10-18.md, seção 5.2. Mudam só a regência da justificativa de L1-R129 (texto aceito pela gce-cqfp na R2, seção 3) e a localização dos trechos-base de L1-R126 e L1-R124 na seção "Evaluated Use" do model card. Enunciados, gabaritos, [TS] e VOLÁTEIS não mudam. A resposta ao parecer e os registros que vêm a seguir são histórico da v2.

L79 →
  - R124 × R126 (1.8) e R124 × R122 (1.8): mesmo model card; R126 julga a diarização não avaliada de forma robusta (seção "Evaluated Use", segundo parágrafo), R122 julga a alucinação (seção "Performance and Limitations"); R124 julga a advertência sobre gravações feitas sem consentimento (seção "Evaluated Use", terceiro parágrafo). R124 × R106 (1.7): R106 julga a ausência de tempo real fora da caixa; ponto distinto. Nenhuma das partes A, B e C usa o ponto.
L288 →
L1-R129. C. REVERIFICAR. O README informa, e a conduta de ressalvar é a correta, porque as velocidades relativas foram medidas com fala em inglês em uma A100 e a velocidade real pode variar significativamente com idioma, velocidade da fala e hardware.

Nada mais muda.

Conferência dos v3: feita pela gce-gerencia ou pelo orquestrador, por diff textual v2 → v3 (script, python -I). Critério: só mudam as linhas listadas, com texto idêntico ao fixado aqui; entram a linha em branco e a linha inseridas depois da linha 1; no A saem as 7 linhas apagadas. Se o texto for idêntico, valem a seção 8 (CONCLUÍDA, depois do passo da seção 7) e o gatilho A. Se for divergente, a gce-cpp refaz a transcrição.

## 6. Contagens finais (111 itens aceitáveis; L1-R43 fora)

| folha | partida v1.9 | novos | nova | C/E novos | [TS] novos | VOLÁTIL folha | formatos (folha) | maior formato |
|---|---|---|---|---|---|---|---|---|
| P2-1.1 | 6 | R19–R32 (14) | 20 | 7/7 | 8 | 0/20 | D3 PC4 TS2 NP3 SH3 AP5 | 25% |
| P2-1.2 | 6 | R33–R46 sem R43 (13) | 19 (+1 saldo, R131) | 7/6 | 7 | 0/19 | D2 PC5 TS2 NP2 SH4 AP4 | 26,3% |
| P2-1.3 | 6 | R47–R60 (14) | 20 | 7/7 | 8 | 3/20 (R49, R54, R57) | D3 TS3 SH4 NP3 PC3 AP4 | 20% |
| P2-1.4 | 6 | R61–R74 (14) | 20 | 7/7 | 9 | 3/20 (R65, R67, R69) | D2 PC2 AP5 SH4 TS5 NP2 | 25% |
| P2-1.5 | 6 | R75–R88 (14) | 20 | 7/7 | 8 | 3/20 (R86, R87, R88) | D3 TS5 SH4 NP2 PC2 AP4 | 25% |
| P2-1.6 | 6 | R89–R102 (14) | 20 | 7/7 | 8 | 1/20 (Q14) | D4 TS5 SH4 NP0 PC3 AP4 (R99 = PC) | 25% |
| P2-1.7 | 6 | R103–R116 (14) | 20 | 6/8 | 9 | 3/20 (Q16 alto, R110, R114) | D4 TS3 SH4 NP2 PC3 AP4 | 20% |
| P2-1.8 | 6 | R117–R130 (14) | 20 | 8/6 | 8 | 2/20 (Q18, Q19) | D4 TS2 SH6 NP2 PC3 AP3 | 30% (no teto) |
| total | 48 | 111 | 159 (160 com o saldo) | 56 C / 55 E | 65 | 11 VOLÁTEIS novos, 0 de risco alto | — | ≤ 30% |

- Regra 5: 56 C / 55 E = 50,5% de C, dentro da faixa de 40% a 60%. Com o saldo (E), fica em 56/112 = 50,0%.
- [TS]: 65 de 111 (58,6%). A meta da T-89 (metade da onda mais 2 = 58) está cumprida. O acumulado de reforço do Lote 1 fica em 72 de 129 (55,8%).
- Regra 4: o maior valor por folha é 15%, e nenhum VOLÁTIL novo é de risco alto. Regra 3: o maior formato é 30% (SH na 1.8, sem folga). A 1.8 não admite mais SH.
- QA:
  - R1 por parte: A 10,7%, B 3,6%, C 17,9%, D 3,6% (onda: 10 em 112 = 8,9%);
  - R2: A 1 em 28 (R43), B, C e D 0%;
  - gate de 30% não acionado.
- Pacote: v1.9 (334) + 111 = 445 na v1.10, além do que a D-ABSORCAO-V110 e a onda 3 acrescentarem.

## 7. D1: auditoria de estilo da onda 2 (D-REFORCO-2, regra 6): roda ANTES do gatilho A
Ela integra o fluxo da própria linha T-96 ("+ gbq-estilo"; "saida/banco/estilo_onda_2.md"). Há três razões para rodar antes:
- a QA deixou registros de estilo dirigidos ao gbq-estilo (seção 3);
- uma reprovação acima de 30% é GATE e tornaria inútil um aceite anterior;
- correr antes da T-97 evita QA aberta no início de lote novo (D-RITMO-MAX).

Especificação:
- auditor: gbq-estilo;
- objeto: os textos finais (A_v3, B_v2, C_v2, D_v3);
- amostra: 10% dos 111, ou seja, 12 itens sorteados com semente registrada, com pelo menos 1 por folha;
- conferências: a faixa de C da onda (50,5%) e os registros da seção 3;
- saída: saida/banco/estilo_onda_2.md;
- devolução: à gce-gerencia, que fecha a T-96.

O L1-R131 não entra nesta amostra: fica para a amostra da onda 3, ou para conferência pela gbq-estilo no aceite do saldo.

## 8. Estado da T-96 e tarefa de saldo (textos para TAREFAS.md)
Estado, até os v3 conferidos e o estilo_onda_2.md sem GATE:
EM CURSO (ciclo 2026-10-18 s12c3; QA R1 8,9% e R2 0,9% na onda; reconciliada em saida/gce/T96_reconciliacao_2026-10-18.md: L1-R43 retirado, com saldo em tarefa própria (L1-R131); A e D com v3 de transcrição fixado na seção 5; B e C v2 finais; aguarda o diff dos v3 e a auditoria do gbq-estilo, saida/banco/estilo_onda_2.md)

Estado, depois dos dois passos:
CONCLUÍDA (18/10/2026, s12c3): 111 dos 112 itens L1-R19 a L1-R130 (sem L1-R43, retirado; id não reutilizado); 56 C / 55 E; [TS] 65; 11 VOLÁTEIS novos, nenhum de risco alto; folhas 1.1 e 1.3 a 1.8 com 20 itens e 1.2 com 19 (o saldo L1-R131 está na T-<saldo>); finais A_v3, B_v2, C_v2, D_v3; estilo_onda_2.md sem GATE; gatilho A emitido.

Linha nova (o orquestrador atribui o número):
T-<saldo>; GCE; REFORÇO onda 2 — saldo da T-96 (D-REFORCO-2): 1 item AUTORAL L1-R131 em P2-1.2, que repõe o L1-R43 retirado (id não reutilizado). Requisitos: gabarito E com [TS] de troca única; formato diferente de definição e de par confundível, de preferência troca de sujeito; ponto conceitual de modelo end-to-end, e não fato de tabela, checkpoint ou lista de repositório; ponto distinto dos 19 da folha e sem gêmeo em outra folha do pacote (T96_reconciliacao, seções 1 e 4); base oficial aberta na data, com trecho literal; não VOLÁTIL. QA própria da gce-cqfp, R1 e no máximo 2 rodadas. Entra na consolidação v1.10. AGORA (antes da T-97; D-RITMO-MAX); PENDENTE; gce-cpp → gce-cqfp → gce-gerencia; saida/gce/L1_reforco_onda2_saldo_v1.md

## 9. Gatilho A (texto para PARA_PRESIDENCIA.md; colar só depois dos v3 conferidos e do estilo_onda_2.md sem GATE)
GATILHO A | GCE | T-96 — REFORÇO onda 2, P2 folhas 1.1 a 1.8 (D-REFORCO-2): 111 itens AUTORAL reconciliados (L1-R19 a L1-R130, sem L1-R43) | saida/gce/L1_reforco_onda2_A_v3.md; B_v2.md; C_v2.md; D_v3.md; QA_T96A/B/C/D_R1 e R2_2026-10-18_gce-cqfp.md; saida/gce/T96_reconciliacao_2026-10-18.md; saida/banco/estilo_onda_2.md | Por folha (partida v1.9 → nova): 1.1, 1.3, 1.4, 1.5, 1.6, 1.7 e 1.8 de 6 → 20; 1.2 de 6 → 19 (+1 pelo saldo L1-R131, em tarefa AGORA com QA própria); 48 → 159. Gabarito: 56 C / 55 E (50,5%). [TS]: 65 (58,6%; meta de 58). VOLÁTEIS novos: 11, nenhum de risco alto; o máximo por folha é 15%. Formato: máximo de 30% (SH na 1.8). QA: R1 8,9% e R2 0,9% (só o L1-R43, retirado). D1 registradas: precisão do critério de VOLÁTIL (seção 2: funcionamento documentado de recurso central e boa prática sem número, versão, padrão ou disponibilidade condicionada = não VOLÁTIL, com conferência de base em 4–8/1/2027; R120 e R128 não VOLÁTEIS; R24 e R29 uniformizados com os gêmeos); R99 = PC; 8 gêmeos entre folhas aceitos pela regra 1 e recomendados para não coexistir em simulado. Registro: o teto de 4 VOLÁTEIS por lote da D-REFORCO-1 não se aplica à onda 2 (regra 4 da D-REFORCO-2), e o Lote 1 passa de 4 para 15 VOLÁTEIS. | Pergunta fechada: aceitar os 111 itens para consolidação no pacote v1.10 e ratificar, como D2 de rótulo, a precisão do critério de VOLÁTIL da seção 2 da reconciliação — SIM ou NÃO? (Com NÃO à precisão, R120, R123, R128 e R130 viram VOLÁTEIS, a 1.8 vai a 6/20 e só fecha com substituições.)

## 10. Ordem imediata
1. A gce-cpp grava A_v3 e D_v3 conforme a seção 5. O orquestrador ou a gce-gerencia confere por diff.
2. O gbq-estilo faz a auditoria da seção 7.
3. O orquestrador abre a linha do saldo (seção 8), em AGORA, antes da T-97.
4. Com o diff idêntico e a auditoria sem GATE, o estado passa a CONCLUÍDA e o gatilho A da seção 9 é colado.
5. A lista de conferência de janeiro (T-11, parte P2) recebe:
   - VOLÁTEIS: R49, R54, R57, R65, R67, R69, R86, R87, R88, R110, R114;
   - conferência de base (sem efeito de VOLÁTIL): os outros 100 itens; no R100, comparar o SHA-256 do transcribe.py; as 3 URLs redirecionadas da parte B, reabertas na URL final.

## Conferência dos v3 (orquestrador, 18/10/2026)
Conferência por script (python -I) contra as seções 5.1 e 5.2: A_v3 = A_v2 com as 26 linhas fixadas, a linha inserida e as 7 linhas apagadas (L1-R43) — IDÊNTICO; D_v3 = D_v2 com as 3 linhas fixadas e a linha inserida — IDÊNTICO. Sem R3. Próximo passo: auditoria do gbq-estilo (seção 7).

## Fechamento (orquestrador, 18/10/2026)
saida/banco/estilo_onda_2.md sem GATE (12/12 aprovados; 56 C / 55 E). Condições da seção 10 cumpridas; estado final da seção 8 aplicado em TAREFAS.md e gatilho A da seção 9 colado em PARA_PRESIDENCIA.md (saldo = T-103).
