# L2_reforco_onda3_A_v1.md — T-97 — 2026-10-18 — gerado por gce-cpp

Tarefa T-97, onda 3 do reforço, parte A (ciclo s12c4), v1. Escopo: P2 folhas 2.1 e 2.2, 28 itens AUTORAL novos, ids L2-R19 a L2-R46 (L2-R19 a L2-R32 na folha 2.1; L2-R33 a L2-R46 na folha 2.2). Cada folha passa de 6 para 20 itens. As folhas 2.3 a 2.8 são das outras produtoras da onda 3 e não aparecem aqui. Nenhum item existente foi alterado.
Rótulo de todos os itens: AUTORAL (produtora gce-cpp, lote L2-R, onda 3 do reforço, D-REFORCO-2). QA PENDENTE: nenhum item deste arquivo passou por QA (D-QA-PENDENTE); não entra em simulado antes da QA da gce-cqfp.
Convenção de base: "verificado em 18/10/2026" significa página, arquivo ou PDF aberto e lido nesta data, nesta sessão (curl com User-Agent de navegador para o Legin; sem base de data anterior, D-FONTE-DATA-ANTERIOR). Nomenclatura: "Derep (antigo DETAQ)" (Ato da Mesa nº 251/2026, aberto e lido hoje no Legin). Itens não citam versão, preço nem limite numérico de produto.
Critérios aplicados: D-REFORCO-1/2 (um ponto de julgamento por item, único na folha e conferido contra o pacote inteiro; formato declarado, no máximo 30% de um formato por folha de 20; VOLÁTIL ≤ 20% por folha; gabarito da parte entre 40% e 60% de C); critério de VOLÁTIL da D-T96-ONDA2-ACEITE (D2 de rótulo); diluição do legado de T90_reconciliacao (nenhum item "aplicação parlamentar" na 2.1 e nenhum "definição" na 2.2); registros O-1 a O-8 e recomendações de saida/banco/estilo_onda_2.md (seção 5): "independentemente" também em E, "ainda que" também em C, aberturas variadas, fonte nomeada, um só absoluto por E, ambientação parlamentar fora do escopo da remissão, extensão equilibrada entre C e E.

=====================================================================
PARTE 1/3 — MAPA
=====================================================================

Formatos: D = definição; TS = troca de sujeito; SH = situação hipotética; NP = número ou prazo; PC = par confundível; AP = aplicação parlamentar.
Fontes citadas por sigla (URLs completas na tabela de proveniência, ao fim):
- RICD = Regimento Interno da Câmara dos Deputados (Legin).
- ATO251 = Ato da Mesa nº 251/2026 (Legin).
- PORTAL = páginas do portal da Câmara (Banco de Discursos, "Como pesquisar").
- TN = nota de transparência do Azure Speech para speech to text (Microsoft Learn).
- HL = Azure Speech, "How to create human-labeled transcriptions" (Microsoft Learn).
- WMC = model card do Whisper (repositório oficial openai/whisper).
- A2I = Amazon Augmented AI, "Using Amazon Augmented AI for Human Review" (AWS).
- GBP = Google Cloud Speech-to-Text, "Best practices".

## 1.1 Itens novos (um ponto de julgamento por item)

### Folha P2-2.1 (L2-R19 a L2-R32)

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (verificado em 18/10/2026) | VOLÁTIL | aderência |
|---|---|---|---|---|---|---|
| L2-R19 | P2-2.1 | A correção de erros e omissões de discurso já publicado no Diário consta da seção "Errata"; é vedada a nova reprodução do discurso com esse fundamento | SH | RICD, art. 98, § 1º (segunda parte) | n | PARCIAL (forma de publicação no Diário/ata, precedente L2-R02; D-ADERENCIA: só simulado diagnóstico) · PENDENTE NORMATIVO |
| L2-R20 | P2-2.1 | A responsabilidade pela veracidade, integridade e autenticidade do registro oficial é do Derep, e não do fornecedor da ferramenta de transcrição | TS | ATO251, art. 2º, VI | n | direta · PENDENTE NORMATIVO |
| L2-R21 | P2-2.1 | A redação final e a montagem dos discursos das sessões plenárias competem à Coordenação de Redação Final, e não à de Registro Oficial | TS | ATO251, arts. 5º e 6º, I | n | PARCIAL (competência entre órgãos e coordenações, contexto institucional; D-ADERENCIA: só simulado diagnóstico) · PENDENTE NORMATIVO |
| L2-R22 | P2-2.1 | O Ato nº 251/2026 transformou o Departamento de Taquigrafia, Revisão e Redação (DETAQ) no Derep | D | ATO251, art. 1º | n | PARCIAL (competência entre órgãos e coordenações, contexto institucional; D-ADERENCIA: só simulado diagnóstico) · PENDENTE NORMATIVO |
| L2-R23 | P2-2.1 | A nota de transparência manda esperar certo nível de imprecisão no texto de saída da transcrição automática, em razão das variações acústicas e linguísticas | SH | TN ("Limitations", "Transcription accuracy and system limitations") | n | direta |
| L2-R24 | P2-2.1 | No caso de uso do A2I com o Amazon Transcribe, as pessoas revisam as transcrições geradas pelo serviço, e não transcrevem o áudio do zero | PC | A2I ("Amazon A2I Use Case Examples") | S (BAIXO): a própria página avisa que o serviço não está aberto a novos clientes (hipótese (c)); REVERIFICAR | direta |
| L2-R25 | P2-2.1 | Notas taquigráficas são o conjunto de discursos; discurso é a transcrição tratada individualmente (e não o inverso) | TS | PORTAL, "Como pesquisar" | S (BAIXO) | PARCIAL (vocabulário do Banco de Discursos, tema de 2.4/3.2; D-ADERENCIA: só simulado diagnóstico) |
| L2-R26 | P2-2.1 | Transcrição rotulada por humanos é transcrição palavra por palavra do áudio, e não resumo | D | HL (parágrafo inicial) | n | direta |
| L2-R27 | P2-2.1 | O cartão do modelo Whisper recomenda contra o uso em domínios de alto risco, como contextos de tomada de decisão | SH | WMC, "Evaluated Use" | n | PARCIAL (advertência de uso em alto risco, tema de 4.2/1.8; D-ADERENCIA: só simulado diagnóstico) |
| L2-R28 | P2-2.1 | Os discursos são publicados por extenso na ata impressa (e não em sinopse), salvo restrições regimentais | PC | RICD, art. 98, § 1º (primeira parte) | n | PARCIAL (forma de publicação no Diário/ata, precedente L2-R02; D-ADERENCIA: só simulado diagnóstico) · PENDENTE NORMATIVO |
| L2-R29 | P2-2.1 | A elaboração das atas das sessões plenárias compete ao Derep, e não à Secretaria-Geral da Mesa | TS | ATO251, art. 2º, III | n | PARCIAL (tema de 3.3; D-ADERENCIA: só simulado diagnóstico) · PENDENTE NORMATIVO |
| L2-R30 | P2-2.1 | O reconhecimento de fala gera texto para as partes de voz; silêncio e ruído que não é fala não geram texto | PC | TN ("Key terms", "Audio input") | n | direta |
| L2-R31 | P2-2.1 | O Derep dá publicidade aos textos do registro oficial garantindo acesso a informação primária, íntegra e autêntica | D | ATO251, art. 2º, VII | n | PARCIAL (missão institucional; D-ADERENCIA: só simulado diagnóstico) · PENDENTE NORMATIVO |
| L2-R32 | P2-2.1 | O registro oficial e a redação final de reunião de comissão permanente competem ao Derep | SH | ATO251, art. 2º, I | n | PARCIAL (competência entre órgãos e coordenações, contexto institucional; D-ADERENCIA: só simulado diagnóstico) · PENDENTE NORMATIVO |

### Folha P2-2.2 (L2-R33 a L2-R46)

| id | folha | ponto de julgamento (afirmação que decide C/E) | formato | base (verificado em 18/10/2026) | VOLÁTIL | aderência |
|---|---|---|---|---|---|---|
| L2-R33 | P2-2.2 | Manter humano no circuito é preservar o papel das pessoas (e não do modelo) na tomada de decisão, com supervisão humana constante | TS | TN ("Guidance for integration and responsible use", Human-in-the-loop) | n | direta |
| L2-R34 | P2-2.2 | Se o áudio reconhecido pode disparar uma ação, o usuário deve poder confirmá-la, vendo ou ouvindo o que foi reconhecido | SH | TN ("Confirm before you take an action by voice") | n | direta |
| L2-R35 | P2-2.2 | O erro por fala rápida, fala pouco clara ou pausa longa é associado a problema temporário, e não a limitação permanente do modelo | PC | TN ("Allow users to try again") | n | PARCIAL (UX de comando de voz, tema de 1.1/1.6; D-ADERENCIA: só simulado diagnóstico) |
| L2-R36 | P2-2.2 | Depois da implantação, convém manter canal de relato de problemas por usuários e afetados, porque o recurso de IA exige monitoramento e melhoria contínuos | AP | TN ("Customer feedback loop") | n | direta |
| L2-R37 | P2-2.2 | O Amazon A2I viabiliza revisão humana de previsões de baixa confiança e de amostras aleatórias de previsões | SH | A2I (parágrafo inicial) | S (BAIXO): a própria página avisa que o serviço não está aberto a novos clientes; REVERIFICAR | direta |
| L2-R38 | P2-2.2 | Aprovar e participar do planejamento do uso de ferramentas de IA relacionadas aos textos legislativos registrados compete ao Derep, e não à Secretaria-Geral da Mesa | TS | ATO251, art. 2º, X | n | PARCIAL (competência entre órgãos e coordenações, contexto institucional; D-ADERENCIA: só simulado diagnóstico) · PENDENTE NORMATIVO |
| L2-R39 | P2-2.2 | A gestão do processo de registro oficial e de redação final das reuniões de comissões compete à Coordenação de Gestão do Discurso, e não à de Registro Oficial | PC | ATO251, art. 7º, I | n | PARCIAL (competência entre órgãos e coordenações, contexto institucional; D-ADERENCIA: só simulado diagnóstico) · PENDENTE NORMATIVO |
| L2-R40 | P2-2.2 | A solução com human-in-the-loop deve permitir a intervenção humana em tempo real, para prevenir danos e gerir situações em que o modelo não tem o desempenho exigido, e não só posterior ao processamento | SH | TN ("Guidance for integration and responsible use", Human-in-the-loop) | n | direta |
| L2-R41 | P2-2.2 | Promover o uso de IA nos processos de trabalho e nos controles internos compete à Coordenação de Gestão Administrativa, e não à de Registro Oficial | TS | ATO251, art. 4º, VIII | n | PARCIAL (competência entre órgãos e coordenações, contexto institucional; D-ADERENCIA: só simulado diagnóstico) · PENDENTE NORMATIVO |
| L2-R42 | P2-2.2 | O registro dos discursos não é exclusivo da Coordenação de Registro Oficial: a de Redação Final também registra, de forma subsidiária | PC | ATO251, art. 6º, IV | n | PARCIAL (competência entre órgãos e coordenações, contexto institucional; D-ADERENCIA: só simulado diagnóstico) · PENDENTE NORMATIVO |
| L2-R43 | P2-2.2 | O conjunto de teste deve ser feito de entradas reais da produção, amostradas ao acaso e renovadas periodicamente | AP | TN ("Evaluating and integrating speech to text for your use") | n | direta |
| L2-R44 | P2-2.2 | No preparo do áudio, convém ouvir amostras, que devem soar claras, sem distorção nem ruído inesperado | AP | GBP ("Audio preprocessing") | n | direta |
| L2-R45 | P2-2.2 | O Derep registra reunião da Mesa Diretora e do Colégio de Líderes quando solicitado pela Secretaria-Geral da Mesa | SH | ATO251, art. 2º, V | n | PARCIAL (contexto institucional; D-ADERENCIA: só simulado diagnóstico) · PENDENTE NORMATIVO |
| L2-R46 | P2-2.2 | A estrutura do Derep tem quatro coordenações (não três) | NP | ATO251, art. 3º | n | PARCIAL (contexto institucional; D-ADERENCIA: só simulado diagnóstico) · PENDENTE NORMATIVO |

VOLÁTEIS novos: 3 (L2-R24 e L2-R25 na 2.1; L2-R37 na 2.2), todos de risco BAIXO; nenhum de risco alto. R25 descreve vocabulário de página do portal; R24 e R37 descrevem serviço (A2I) cuja página informa fechamento a novos clientes (hipótese (c) da D2 de rótulo). Os três itens do Rol do DETAQ de 2009 (v1) saíram do lote (parecer da gce-cqfp, seção 2.1). Os demais itens têm base normativa (RICD, Ato 251) ou boa prática/funcionamento documentado sem número, versão, preço ou padrão.

## 2 Itens já existentes por folha e contagem da folha de 20

Fonte dos existentes: saida/pacote/pacote.json v1.9 (itemEdital P2-2.1 e P2-2.2), conferido contra saida/gce/GCE_Lote2_v2_CPP.md, GCE_Lote2_padroes_GCE.md, GCE_Lote2_consolidacao_GCE.md e L2_reforco_onda1_v3.md. Formato dos existentes: classificação da T90_reconciliacao (seção 4) e do mapa canônico da onda 1.

### P2-2.1 (6 existentes + 14 novos = 20)
| id | ponto | formato | VOL |
|---|---|---|---|
| L2-Q01 | Inverte definições: transcrição automática (software) × degravação (pessoa) | TS | n |
| L2-Q02 | Revisão humana usa pauta, inscritos e glossário externos ao áudio | AP | n |
| L2-Q03 | Bom desempenho em áudio bom não dispensa revisão humana de nota oficial | AP | n |
| L2-Q04 | Rascunho automático sem revisão não é registro oficial | D | n |
| L2-R01 | Discurso não devolvido em cinco sessões é publicado sem a revisão do orador (RICD, art. 98, § 2º) | SH | n |
| L2-R02 | Extratos redigidos pelos autores e notas taquigráficas são alternativas distintas de publicação (RICD, art. 57, XVIII) | PC | n |
| L2-R19 a R32 | ver tabela acima | SH, TS, TS, D, SH, PC, TS, D, SH, PC, TS, PC, D, SH | 2 S (R24, R25) |

Contagem de formatos na folha de 20: SH 5 (R01, R19, R23, R27, R32) = 25%; TS 5 (Q01, R20, R21, R25, R29) = 25%; PC 4 (R02, R24, R28, R30) = 20%; D 4 (Q04, R22, R26, R31) = 20%; AP 2 (Q02, Q03) = 10%; NP 0. Soma 20. Maior formato: 25% (teto de 30% cumprido). Legado "aplicação parlamentar" (2/6): nenhum item novo desse formato; a folha termina com 2/20 = 10%. Os substitutos R23 (SH) e R24 (PC) não elevam o TS da folha (5/20, abaixo do limite de 6/20 apontado pelo parecer).
VOLÁTEIS na folha: 2/20 = 10% (R24, R25; ambos BAIXO); existentes: 0.

### P2-2.2 (6 existentes + 14 novos = 20)
| id | ponto | formato | VOL |
|---|---|---|---|
| L2-Q05 | Definição de human in the loop: saída automática é rascunho, validação humana obrigatória | D | n |
| L2-Q06 | Alta confiança não garante acerto; conferir só baixa confiança não basta | D | n |
| L2-Q07 | Revisão só ao final não detecta sempre erros iniciais (atribuição de falas) | SH | n |
| L2-Q08 | Retroalimentar glossário melhora o fluxo, mas não elimina a revisão | AP | n |
| L2-R03 | Alucinação = inclusão de texto que não consta do áudio | PC | n |
| L2-R04 | A avaliação no contexto e no domínio de uso é recomendação ao usuário (instituição), não ao fornecedor | TS | n |
| L2-R33 a R46 | ver tabela acima | TS, SH, PC, AP, SH, TS, PC, SH, TS, PC, AP, AP, SH, NP | 1 S (R37) |

Contagem de formatos na folha de 20: SH 5 (Q07, R34, R37, R40, R45) = 25%; TS 4 (R04, R33, R38, R41) = 20%; PC 4 (R03, R35, R39, R42) = 20%; AP 4 (Q08, R36, R43, R44) = 20%; D 2 (Q05, Q06) = 10%; NP 1 (R46) = 5%. Soma 20. Maior formato: 25% (teto de 30% cumprido). Legado "definição" (2/6): nenhum item novo desse formato; a folha termina com 2/20 = 10%.
VOLÁTEIS na folha: 1/20 = 5% (R37; BAIXO); existentes: 0.

### Verificação de não repetição (ponto conferido contra o pacote inteiro, T96_reconciliacao, seção 4)
Cada ponto novo foi comparado, um a um, com os pontos listados acima, entre si e com os 334 itens do pacote v1.9, os 112 da onda 2 (L1-R19 a R131), os 18 do L2-R01 a R18 e os 11 do L3-R01 a R11. Nenhum repete ponto. Proximidades declaradas, sem gêmeo:
- R19 × L2-R01 e L3-R05 (art. 98, § 2º, prazo de cinco sessões): R19 julga o § 1º (canal de correção, "Errata"); ponto e parágrafo distintos.
- R28 × L3-R06 (art. 97, caput, sinopse e "padrão uniforme"): R28 julga o art. 98, § 1º (publicação por extenso dos discursos); artigo e ponto distintos.
- R25 × L2-R07 (2.4; mesma página "Como pesquisar"): R07 julga a ausência de discursos individualizados nas reuniões de comissão; R25 julga a definição dos termos. Pontos distintos.
- R23 × L2-Q03 e L2-Q04 (2.1): Q03 julga que o bom desempenho em áudio de boa qualidade não dispensa a revisão humana de nota oficial; Q04 julga que o rascunho sem revisão não é registro oficial; R23 julga o que a nota de transparência manda esperar de quem projeta a aplicação (certo nível de imprecisão no texto de saída, por variações acústicas e linguísticas). Pontos distintos. R23 × L1-R20, L1-R93 e L1-R95 (1.6 e 1.1): esses julgam a causa associada a cada tipo de erro; R23 julga a expectativa de projeto.
- R24 × L2-Q05, L2-Q08 e L2-R37 (2.2): Q05 julga o texto automático como rascunho a validar; Q08 julga a retroalimentação do glossário com as correções; R37 julga a revisão humana de previsões de baixa confiança e de amostras aleatórias (mesma página do A2I). R24 julga o papel das pessoas no caso de uso com o Amazon Transcribe (revisar o texto gerado, e não transcrever do zero). A frase seguinte da mesma página, sobre usar o resultado da revisão para criar vocabulário personalizado, não foi cobrada (seria gêmea de Q08).
- R40 × L2-R33 e L2-Q05 (2.2; mesmo item "Human-in-the-loop" da nota de transparência): R33 julga a supervisão humana constante e o papel das pessoas, e não do modelo, na decisão; Q05 julga o texto automático como rascunho com validação humana; R40 julga a intervenção humana em tempo real para prevenir danos. Três frases distintas.
- R20, R21, R22, R31, R32 (2.1) e R38, R39, R41, R42, R45, R46 (2.2), todos do Ato nº 251/2026: cada um julga um inciso ou artigo diferente (2º VI, 5º/6º I, 1º, 2º VII, 2º I; 2º X, 7º I, 4º VIII, 6º IV, 2º V, 3º). R21 (redação final de Plenário é da Coordenação de Redação Final) e R42 (registro é de Registro Oficial, com atuação subsidiária da Redação Final) são faces diferentes da divisão entre as duas coordenações: R21 julga a redação final de Plenário; R42 julga o registro. Não são o mesmo ponto.
- R30 × L1-R95 e L1-R89 (1.6; mesma nota de transparência): R89 e R95 julgam locale e inserções; R30 julga que só a voz gera texto. Distintos.
- R35 × L1-R89 (1.6): R89 julga idioma incompatível; R35 julga a natureza temporária do erro e a nova tentativa. Distintos.
- R43 × L1-R22 (1.1): R22 julga testar com áudio diferente do usado no ajuste; R43 julga a composição e a renovação do conjunto de teste em produção. Distintos. Possível vizinhança com itens de 2.7 (amostragem) das outras partes da onda 3: a conferência é da Gerência.
- R27 × L1-R37 e L1-R124 (1.2 e 1.8; mesmo "Evaluated Use" do model card): R37 julga a recomendação de avaliação antes da implantação; R124, a advertência sobre gravações sem consentimento; R27, a recomendação contra uso em domínios de alto risco. Três frases distintas do mesmo parágrafo.
- R36 × L2-Q08: Q08 julga retroalimentar o sistema com correções (glossário); R36 julga o canal de relato de problemas e o monitoramento contínuo. Distintos.
- R37 × L2-Q06: Q06 julga que alta confiança não garante acerto e que conferir só baixa confiança não basta; R37 julga a existência de serviço que permite as duas formas de revisão (baixa confiança e amostra aleatória). Distintos. R37 × R24 (mesma página do A2I): R24 julga o papel das pessoas no caso de uso com o Amazon Transcribe.
- R33 × L2-Q05: Q05 define human in the loop (saída automática como rascunho e validação obrigatória); R33 julga a recomendação da nota de transparência sobre quem mantém o papel na decisão. Distintos. R33 × R40: ver o registro de R40 acima.
- R26 × L1-R128 e L1-R19 (1.8 e 1.1): R128 julga a comparação com a transcrição humana por WER; R19, o denominador do WER; R26 julga apenas o que é a transcrição rotulada por humanos (palavra por palavra).
- R44 × L1-R125 (1.8, mesma seção "Audio preprocessing" das boas práticas do Google): R125 julga a redução de ruído e o controle automático de ganho; R44 julga ouvir amostras do áudio. Distintos.
- R32 × R22 (2.1): R22 julga o nome e a transformação do departamento (art. 1º); R32 julga a competência sobre reuniões de comissão (art. 2º, I).

### Tetos (resumo da parte)
- Formato: maior formato por folha = 25% (2.1: SH e TS; 2.2: SH); teto de 30% cumprido; "aplicação parlamentar" novo em 2.1: 0; "definição" nova em 2.2: 0.
- VOLÁTIL: 3 novos (todos BAIXO); 2.1 = 2/20 (10%); 2.2 = 1/20 (5%); risco alto: 0.
- Gabarito da parte: 14 C e 14 E (50,0% de C). Por folha: 2.1 com 7 C e 7 E; 2.2 com 7 C e 7 E.
- [TS]: 18/28 (64,3%; mínimo 16): 14 em itens E (todos os E) e 4 em itens C (espelho: R26, R37, R39, R45); R31 deixou de ter [TS] (parecer da gce-cqfp). Dos 3 substitutos, 2 têm [TS] de troca única (R24 e R40).
- Aderência: 12 direta (R20, R23, R24, R26, R30, R33, R34, R36, R37, R40, R43, R44); 16 PARCIAL (R19, R21, R22, R25, R27, R28, R29, R31, R32, R35, R38, R39, R41, R42, R45, R46; só simulado diagnóstico). Folha 2.1 com 10 diretas em 20; folha 2.2 com 13 diretas em 20.
- PENDENTE NORMATIVO: 14 itens (R19, R20, R21, R22, R28, R29, R31, R32, R38, R39, R41, R42, R45, R46), até o registro do qa-normativo.

FIM DA PARTE 1/3

=====================================================================
PARTE 2/3 — (d) ITENS DO ESTUDANTE
=====================================================================

L2-R19. Julgue o item.
Ao ler no Diário da Câmara dos Deputados o discurso que proferiu em Plenário, um Deputado constatou omissões e erros no texto publicado. Nessa situação, de acordo com o Regimento Interno da Câmara dos Deputados, a correção deve ser feita pela nova reprodução do discurso no Diário, e não pela seção "Errata".

L2-R20. Julgue o item.
Segundo o Ato da Mesa nº 251/2026, independentemente do apoio de ferramenta automática na produção do texto do registro oficial, a responsabilidade pela veracidade, pela integridade e pela autenticidade desse registro é do fornecedor da ferramenta, e não do Derep (antigo DETAQ).

L2-R21. Julgue o item.
De acordo com o Ato da Mesa nº 251/2026, no Derep (antigo DETAQ), a redação final e a montagem dos discursos, debates e votações das sessões plenárias competem à Coordenação de Registro Oficial.

L2-R22. Julgue o item.
O Ato da Mesa nº 251/2026 transformou o Departamento de Taquigrafia, Revisão e Redação, antigo DETAQ, no Departamento de Registro Oficial e Redação Parlamentar (Derep).

L2-R23. Julgue o item.
Uma equipe projeta uma aplicação que utilizará a transcrição automática de áudio. Segundo a nota de transparência do Azure Speech, em razão das variações acústicas e linguísticas do áudio, a equipe deve esperar certo nível de imprecisão no texto de saída.

L2-R24. Julgue o item.
Segundo a documentação do Amazon Augmented AI (A2I), no caso de uso com o Amazon Transcribe, a revisão humana consiste em as pessoas transcreverem o áudio do zero, e não em revisarem as transcrições geradas pelo Amazon Transcribe.

L2-R25. Julgue o item.
De acordo com a página "Como pesquisar" do Banco de Discursos da Câmara dos Deputados, discurso é o conjunto de notas taquigráficas que compõe tudo o que é registrado nas sessões plenárias e nas reuniões das comissões, ao passo que a nota taquigráfica é a transcrição tratada individualmente do pronunciamento.

L2-R26. Julgue o item.
Na documentação do Azure Speech sobre o custom speech, as transcrições rotuladas por humanos (human-labeled transcriptions) são transcrições palavra por palavra de um arquivo de áudio, e não resumos do conteúdo falado.

L2-R27. Julgue o item.
Uma equipe cogita usar transcrições geradas pelo Whisper em um contexto de tomada de decisão de alto risco. Nesse caso, segundo o cartão do modelo Whisper, a recomendação é contra esse uso, pois falhas de acurácia podem levar a falhas pronunciadas nos resultados.

L2-R28. Julgue o item.
Segundo o Regimento Interno da Câmara dos Deputados, os discursos proferidos durante a sessão são publicados na ata impressa em forma de sinopse, salvo expressas restrições regimentais.

L2-R29. Julgue o item.
De acordo com o Ato da Mesa nº 251/2026, a elaboração das atas das sessões plenárias compete à Secretaria-Geral da Mesa, e não ao Derep (antigo DETAQ).

L2-R30. Julgue o item.
Segundo a nota de transparência do Azure Speech, o áudio de entrada pode conter, além de voz, silêncio e ruído que não é fala, e o serviço de reconhecimento de fala gera texto para as partes de voz desse áudio.

L2-R31. Julgue o item.
O Ato da Mesa nº 251/2026 estabelece que o Derep (antigo DETAQ) dá publicidade aos textos produzidos a partir do registro oficial dos discursos e debates orais, garantindo o acesso a informação primária, íntegra e autêntica.

L2-R32. Julgue o item.
Uma audiência pública realizada por comissão permanente da Câmara dos Deputados é reunião de comissão. Nessa situação, de acordo com o Ato da Mesa nº 251/2026, o registro oficial e a redação final dos discursos e debates competem ao Derep (antigo DETAQ).

L2-R33. Julgue o item.
Segundo a nota de transparência do Azure Speech, manter o ser humano no circuito (human-in-the-loop) inclui assegurar supervisão humana constante do recurso de IA e preservar o papel do modelo, e não o das pessoas, na tomada de decisão.

L2-R34. Julgue o item.
Em uma aplicação na qual o áudio reconhecido pode disparar uma ação, como o envio de um texto, a nota de transparência do Azure Speech orienta oferecer ao usuário a oportunidade de confirmar a ação, em especial exibindo ou reproduzindo o que foi reconhecido ou transcrito.

L2-R35. Julgue o item.
A nota de transparência do Azure Speech associa o erro de reconhecimento causado por fala rápida, fala pouco clara ou pausa longa a uma limitação permanente do modelo, e não a um problema temporário.

L2-R36. Julgue o item.
Depois de implantar um recurso de transcrição apoiado em IA nas reuniões de comissão da Câmara dos Deputados, a nota de transparência do Azure Speech recomenda oferecer um canal pelo qual usuários e pessoas afetadas relatem problemas, pois o recurso exige monitoramento e melhoria contínuos, ainda que tenha sido testado antes da implantação.

L2-R37. Julgue o item.
Uma equipe que já utiliza o Amazon Augmented AI (A2I) deseja que revisores humanos examinem as previsões de um modelo quando ele não alcançar alta confiança e que auditem, ainda, amostras aleatórias dessas previsões. Segundo a documentação do serviço, o A2I permite obter revisão humana tanto de previsões de baixa confiança quanto de amostras aleatórias de previsões.

L2-R38. Julgue o item.
De acordo com o Ato da Mesa nº 251/2026, compete à Secretaria-Geral da Mesa, e não ao Derep (antigo DETAQ), aprovar e participar do planejamento do uso de ferramentas de interatividade, de tecnologia e de inteligência artificial relacionadas aos textos legislativos registrados.

L2-R39. Julgue o item.
No Derep (antigo DETAQ), segundo o Ato da Mesa nº 251/2026, a gestão do processo de registro oficial e de redação final das reuniões de comissões compete à Coordenação de Gestão do Discurso, e não à Coordenação de Registro Oficial.

L2-R40. Julgue o item.
Uma equipe da Casa implanta um recurso de transcrição apoiado em IA em um fluxo com human-in-the-loop. Segundo a nota de transparência do Azure Speech, para prevenir danos quando o modelo de IA não tiver o desempenho exigido, a solução deve permitir a intervenção humana posterior ao processamento do áudio, e não a intervenção em tempo real.

L2-R41. Julgue o item.
Segundo o Ato da Mesa nº 251/2026, compete à Coordenação de Registro Oficial do Derep (antigo DETAQ) promover a informatização e o uso de inteligência artificial aplicada aos processos de trabalho e aos controles internos do departamento.

L2-R42. Julgue o item.
De acordo com o Ato da Mesa nº 251/2026, o registro dos discursos, debates e votações das sessões plenárias é atribuição exclusiva da Coordenação de Registro Oficial do Derep (antigo DETAQ), sem atuação subsidiária da Coordenação de Redação Final.

L2-R43. Julgue o item.
Para avaliar o desempenho do reconhecimento de fala usado na transcrição das sessões plenárias da Câmara dos Deputados, a nota de transparência do Azure Speech recomenda que o conjunto de teste seja composto por entradas de voz reais coletadas na própria aplicação em produção, amostradas aleatoriamente ao longo de um período e atualizado periodicamente.

L2-R44. Julgue o item.
Antes de enviar a gravação de uma audiência pública de comissão da Câmara dos Deputados ao Google Cloud Speech-to-Text, a equipe pode ouvir trechos do áudio, que, segundo as boas práticas do serviço, deve soar claro, sem distorção nem ruído inesperado.

L2-R45. Julgue o item.
Quando a Secretaria-Geral da Mesa solicita o registro de uma reunião do Colégio de Líderes, o Derep (antigo DETAQ), segundo o Ato da Mesa nº 251/2026, tem competência para registrá-la.

L2-R46. Julgue o item.
De acordo com o Ato da Mesa nº 251/2026, o Derep (antigo DETAQ) tem estrutura administrativa composta por três coordenações: Gestão Administrativa, Registro Oficial e Redação Final.

FIM DA PARTE 2/3

=====================================================================
PARTE 3/3 — (d-G) GABARITO COMENTADO
=====================================================================

Legenda: [TS] = troca sutil de um único conceito (em item E, o conceito trocado; em item C, "espelho": o item parece conter a troca, mas está correto). VOLÁTIL = gabarito que depende de fato mutável (critério da D-T96-ONDA2-ACEITE); REVERIFICAR = reabrir a base em 4–8/1/2027. CONFERÊNCIA DE BASE = reabrir a URL em 4–8/1/2027 sem efeito de VOLÁTIL. PENDENTE NORMATIVO = base normativa (RICD, Ato 251) ainda sem registro do qa-normativo; PARCIAL = aderência parcial, só simulado diagnóstico (D-ADERENCIA).

## Folha P2-2.1

L2-R19. E [TS]. O art. 98, § 1º, veda a reprodução de discursos no Diário com o fundamento de corrigir erros e omissões; as correções constam da seção "Errata". O item troca o canal da correção.
Base: RICD, art. 98, § 1º ("Não são permitidas as reproduções de discursos no Diário da Câmara dos Deputados com o fundamento de corrigir erros e omissões; as correções constarão da seção 'Errata'"), Legin, verificado em 18/10/2026. Aderência: PARCIAL (forma de publicação no Diário/ata, precedente L2-R02; D-ADERENCIA: só simulado diagnóstico). PENDENTE NORMATIVO.

L2-R20. E [TS]. O Ato atribui ao Derep garantir a precisão do texto do registro oficial e a responsabilidade pela sua veracidade, integridade e autenticidade; nada transfere essa responsabilidade a ferramenta. A troca é do responsável (Derep → fornecedor da ferramenta).
Base: Ato da Mesa nº 251/2026, art. 2º, VI ("garantir a precisão do texto do registro oficial e a responsabilidade pela sua veracidade, integridade e autenticidade"), Legin, verificado em 18/10/2026. Aderência: direta. PENDENTE NORMATIVO.

L2-R21. E [TS]. A redação final e a montagem dos discursos, debates e votações das sessões plenárias são da Coordenação de Redação Final (art. 6º, I); à de Registro Oficial cabe a redação final só de reuniões de comissões e outros eventos, de forma subsidiária (art. 5º, IV). O item troca a coordenação.
Base: Ato da Mesa nº 251/2026, art. 5º, IV, e art. 6º, I, Legin, verificado em 18/10/2026. Aderência: PARCIAL (competência entre órgãos e coordenações, contexto institucional; D-ADERENCIA: só simulado diagnóstico). PENDENTE NORMATIVO.

L2-R22. C. O art. 1º do Ato transforma o Departamento de Taquigrafia, Revisão e Redação (DETAQ) em Departamento de Registro Oficial e Redação Parlamentar (Derep).
Base: Ato da Mesa nº 251/2026, art. 1º e ementa, Legin, verificado em 18/10/2026. Aderência: PARCIAL (competência entre órgãos e coordenações, contexto institucional; D-ADERENCIA: só simulado diagnóstico). PENDENTE NORMATIVO.

L2-R23. C. A nota de transparência manda esperar, ao projetar a aplicação, certo nível de imprecisão no texto de saída, em razão das variações acústicas e linguísticas do áudio. O item reproduz a recomendação, sem acrescentar condição.
Base: Microsoft, Azure Speech, nota de transparência de speech to text, "Limitations", "Transcription accuracy and system limitations" ("Because of these acoustic and linguistic variations, you should expect a certain level of inaccuracy in the output text when you design an application"), https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note, "Last updated on 2026-03-31", verificado em 18/10/2026. Boa prática documentada, sem número; CONFERÊNCIA DE BASE. Aderência: direta.

L2-R24. E [TS]. VOLÁTIL (baixo); REVERIFICAR. A documentação do A2I descreve o caso de uso com o Amazon Transcribe como pessoas que revisam as transcrições geradas pelo serviço; as pessoas não transcrevem o áudio do zero. O item troca a revisão do texto automático pela transcrição humana integral.
Base: AWS, "Using Amazon Augmented AI for Human Review", seção "Amazon A2I Use Case Examples" ("Use Amazon A2I with Amazon Transcribe – Have humans review Amazon Transcribe transcriptions of video or audio files"), https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.html, verificado em 18/10/2026. A mesma página avisa que "Amazon SageMaker A2I is no longer open to new customers"; por isso a marca VOLÁTIL (hipótese (c) da D2 de rótulo); o item não afirma disponibilidade. Aderência: direta.

L2-R25. E [TS]. VOLÁTIL (baixo); REVERIFICAR. A página define notas taquigráficas como o conjunto de discursos e discurso como a transcrição tratada individualmente; o item inverte os dois termos.
Base: Câmara, "Como pesquisar" (Banco de Discursos): "notas taquigráficas são o conjunto de discursos que compõe tudo o que é registrado nas sessões plenárias e nas reuniões das comissões. Discurso é a transcrição tratada individualmente do pronunciamento", https://www2.camara.leg.br/atividade-legislativa/discursos-e-notas-taquigraficas/pesquisa/como-pesquisar, verificado em 18/10/2026. Vocabulário de página do portal, sem data de edição. Aderência: PARCIAL (vocabulário do Banco de Discursos, tema de 2.4/3.2; D-ADERENCIA: só simulado diagnóstico).

L2-R26. C [TS] (espelho). O item parece trocar o conceito (rotulado por humanos × resumo), mas a documentação define human-labeled transcriptions como transcrições palavra por palavra de um arquivo de áudio.
Base: Microsoft, Azure Speech, "How to create human-labeled transcriptions" ("Human-labeled transcriptions are word-by-word transcriptions of an audio file"), "Last updated on 2025-12-29", verificado em 18/10/2026. Funcionamento documentado, sem número; CONFERÊNCIA DE BASE.

L2-R27. C. O cartão do modelo recomenda contra o uso em domínios de alto risco, como contextos de tomada de decisão, em que falhas de acurácia podem levar a falhas pronunciadas nos resultados.
Base: repositório oficial openai/whisper, model-card.md, "Evaluated Use" ("We recommend against use in high-risk domains like decision-making contexts, where flaws in accuracy can lead to pronounced flaws in outcomes"), https://raw.githubusercontent.com/openai/whisper/main/model-card.md, verificado em 18/10/2026. CONFERÊNCIA DE BASE. Aderência: PARCIAL (advertência de uso em alto risco, tema de 4.2/1.8; D-ADERENCIA: só simulado diagnóstico).

L2-R28. E [TS]. Os discursos são publicados POR EXTENSO na ata impressa, salvo expressas restrições regimentais; a sinopse é da ata em si (art. 97, caput). O item troca "por extenso" por "em forma de sinopse".
Base: RICD, art. 98, § 1º ("Os discursos proferidos durante a sessão serão publicados por extenso na ata impressa, salvo expressas restrições regimentais"), Legin, verificado em 18/10/2026. Aderência: PARCIAL (forma de publicação no Diário/ata, precedente L2-R02; D-ADERENCIA: só simulado diagnóstico). PENDENTE NORMATIVO.

L2-R29. E [TS]. Pelo art. 2º, III, compete ao Derep elaborar as atas de sessões plenárias; o item troca o órgão por Secretaria-Geral da Mesa.
Base: Ato da Mesa nº 251/2026, art. 2º, III ("elaborar as atas de sessões plenárias"; art. 5º, V, repete a atribuição para a Coordenação de Registro Oficial), Legin, verificado em 18/10/2026. Aderência: PARCIAL (tema de 3.3; D-ADERENCIA: só simulado diagnóstico). PENDENTE NORMATIVO.

L2-R30. C. A nota define o áudio de entrada como podendo conter voz, silêncio e ruído que não é fala, e diz que o serviço gera texto para as partes de voz.
Base: Microsoft, Azure Speech, nota de transparência de speech to text, "Key terms" ("Audio input can contain not only voice, but also silence and non-speech noise. Speech to text generates text for the voice parts of audio input"), https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note (a URL antiga, /legal/cognitive-services/..., redireciona para esta), "Last updated on 2026-03-31", verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L2-R31. C. O art. 2º, VII, atribui ao Derep dar publicidade aos textos produzidos a partir do registro oficial dos discursos e debates orais, garantindo o acesso a informação primária, íntegra e autêntica.
Base: Ato da Mesa nº 251/2026, art. 2º, VII ("dar publicidade aos textos produzidos a partir do registro oficial dos discursos e debates orais, garantindo o acesso a informação primária, íntegra e autêntica"), Legin, verificado em 18/10/2026. Aderência: PARCIAL (missão institucional; D-ADERENCIA: só simulado diagnóstico). PENDENTE NORMATIVO.

L2-R32. C. Reunião de comissão permanente é abrangida pelo art. 2º, I; o Derep procede ao registro oficial e à redação final dos discursos e debates dessas reuniões.
Base: Ato da Mesa nº 251/2026, art. 2º, I ("proceder ao registro oficial e à redação final dos discursos, debates, procedimentos e votações das sessões plenárias, das reuniões de comissões permanentes e temporárias da Câmara dos Deputados e de outros eventos legislativos"), Legin, verificado em 18/10/2026. Aderência: PARCIAL (competência entre órgãos e coordenações, contexto institucional; D-ADERENCIA: só simulado diagnóstico). PENDENTE NORMATIVO.

## Folha P2-2.2

L2-R33. E [TS]. A nota fala em assegurar supervisão humana constante e em manter o papel dos HUMANOS na tomada de decisão; o item troca por papel do modelo.
Base: Microsoft, Azure Speech, nota de transparência de speech to text, "Guidance for integration and responsible use" ("Human-in-the-loop: Keep a human-in-the-loop and include human oversight ... ensuring constant human oversight of the AI-powered product or feature and maintaining the role of humans in decision making"), mesma URL de R30, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L2-R34. C. A nota recomenda dar ao usuário oportunidade de confirmar a ação disparada por áudio, exibindo ou reproduzindo o que foi reconhecido ou transcrito.
Base: Azure Speech, nota de transparência, "Confirm before you take an action by voice" ("users should be given an opportunity to confirm the action, especially by displaying or playing back what was recognized or transcribed"), mesma URL de R30, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L2-R35. E [TS]. A nota atribui o erro por fala rápida, fala pouco clara ou pausa longa a problema TEMPORÁRIO ("temporary issue"); o item troca por limitação permanente.
Base: Azure Speech, nota de transparência, "Allow users to try again" ("Misrecognition might occur due to a temporary issue, such as unclear or fast speech or a long pause"), mesma URL de R30, verificado em 18/10/2026. CONFERÊNCIA DE BASE. Aderência: PARCIAL (UX de comando de voz, tema de 1.1/1.6; D-ADERENCIA: só simulado diagnóstico).

L2-R36. C. A nota recomenda canal de feedback depois da implantação e afirma que o recurso de IA exige monitoramento e melhoria contínuos; a concessiva não altera isso.
Base: Azure Speech, nota de transparência, "Customer feedback loop" ("Provide a feedback channel that allows users and individuals to report issues with the service once it's been deployed. After you've deployed an AI-powered product or feature, it requires ongoing monitoring and improvement"), mesma URL de R30, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L2-R37. C [TS] (espelho). VOLÁTIL (baixo); REVERIFICAR. O item parece contradizer a ideia de que a revisão só de baixa confiança não basta, mas a documentação lista as duas formas de revisão humana (baixa confiança e amostras aleatórias).
Base: AWS, "Using Amazon Augmented AI for Human Review" ("you can use Amazon Augmented AI to get human review of low-confidence predictions or random prediction samples"), https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.html, verificado em 18/10/2026. A mesma página avisa que "Amazon SageMaker A2I is no longer open to new customers"; por isso a marca VOLÁTIL (hipótese (c) da D2 de rótulo); o item não afirma disponibilidade.

L2-R38. E [TS]. O art. 2º, X, atribui ao Derep aprovar e participar do planejamento do uso de ferramentas de IA relacionadas aos textos legislativos registrados; o item troca o órgão pela Secretaria-Geral da Mesa.
Base: Ato da Mesa nº 251/2026, art. 2º, X ("aprovar e participar do planejamento do uso de ferramentas de interatividade, de tecnologia e de inteligência artificial relacionadas aos textos legislativos registrados"), Legin, verificado em 18/10/2026. Aderência: PARCIAL (competência entre órgãos e coordenações, contexto institucional; D-ADERENCIA: só simulado diagnóstico). PENDENTE NORMATIVO.

L2-R39. C [TS] (espelho). O item parece trocar as coordenações, mas o art. 7º, I, dá à Coordenação de Gestão do Discurso a gestão do processo de registro oficial e de redação final de reuniões de comissões.
Base: Ato da Mesa nº 251/2026, art. 7º, I ("gerir o processo de registro oficial e de redação final de reuniões de comissões e de outros eventos legislativos"), Legin, verificado em 18/10/2026. Aderência: PARCIAL (competência entre órgãos e coordenações, contexto institucional; D-ADERENCIA: só simulado diagnóstico). PENDENTE NORMATIVO.

L2-R40. E [TS]. A nota recomenda assegurar a possibilidade de intervenção humana em tempo real na solução, para prevenir danos e gerir situações em que o modelo de IA não tem o desempenho exigido. O item troca "em tempo real" por "posterior ao processamento do áudio".
Base: Microsoft, Azure Speech, nota de transparência de speech to text, "Guidance for integration and responsible use with speech to text", Human-in-the-loop ("Ensure that you can have real-time human intervention in the solution to prevent harm. This enables you to manage situations when the AI model does not perform as required"), mesma URL de R23, "Last updated on 2026-03-31", verificado em 18/10/2026. Boa prática documentada, sem número; CONFERÊNCIA DE BASE. Aderência: direta.

L2-R41. E [TS]. O art. 4º, VIII, dá à Coordenação de Gestão Administrativa promover a informatização e o uso de IA aplicada aos processos de trabalho e aos controles internos; o item troca pela de Registro Oficial.
Base: Ato da Mesa nº 251/2026, art. 4º, VIII ("promover a informatização e o uso de inteligência artificial aplicada aos processos de trabalho e aos controles internos"), Legin, verificado em 18/10/2026. Aderência: PARCIAL (competência entre órgãos e coordenações, contexto institucional; D-ADERENCIA: só simulado diagnóstico). PENDENTE NORMATIVO.

L2-R42. E [TS]. O art. 6º, IV, dá à Coordenação de Redação Final o registro dos discursos, debates e votações de forma subsidiária à de Registro Oficial; o item afirma que não há atuação subsidiária. A troca é de "subsidiária" por "exclusiva".
Base: Ato da Mesa nº 251/2026, art. 5º, I, e art. 6º, IV ("registrar, subsidiariamente à Coordenação de Registro Oficial, os discursos, debates e votações"), Legin, verificado em 18/10/2026. Aderência: PARCIAL (competência entre órgãos e coordenações, contexto institucional; D-ADERENCIA: só simulado diagnóstico). PENDENTE NORMATIVO.

L2-R43. C. A nota recomenda conjunto de teste com entradas reais da produção, amostradas aleatoriamente ao longo de um período e renovado periodicamente.
Base: Azure Speech, nota de transparência, "Evaluating and integrating speech to text for your use" ("A test voice dataset should consist of actual voice inputs that were collected in your applications in production. You should randomly sample data to reflect real user variations over a certain period of time. Also, the test dataset should be refreshed periodically"), mesma URL de R30, verificado em 18/10/2026. CONFERÊNCIA DE BASE.

L2-R44. C. As boas práticas do Google recomendam ouvir amostras do áudio, que deve soar claro, sem distorção nem ruído inesperado.
Base: Google Cloud, Speech-to-Text, Best practices, "Audio preprocessing" ("Listen to some sample audio. It should sound clear, without distortion or unexpected noise"), https://docs.cloud.google.com/speech-to-text/docs/best-practices, "Last updated 2026-10-13 UTC", verificado em 18/10/2026. Boa prática documentada, sem número nem padrão; CONFERÊNCIA DE BASE.

L2-R45. C [TS] (espelho). O item parece condicionar uma competência a solicitação alheia, mas o art. 2º, V, dá ao Derep registrar as reuniões da Mesa Diretora e do Colégio de Líderes quando solicitado pela Secretaria-Geral da Mesa.
Base: Ato da Mesa nº 251/2026, art. 2º, V ("registrar as reuniões da Mesa Diretora e do Colégio de Líderes quando solicitado pela Secretaria-Geral da Mesa"), Legin, verificado em 18/10/2026. Aderência: PARCIAL (contexto institucional; D-ADERENCIA: só simulado diagnóstico). PENDENTE NORMATIVO.

L2-R46. E [TS]. O art. 3º lista quatro coordenações (Gestão Administrativa, Registro Oficial, Redação Final e Gestão do Discurso); o item diz três e omite a Gestão do Discurso.
Base: Ato da Mesa nº 251/2026, art. 3º, I a IV, Legin, verificado em 18/10/2026. Aderência: PARCIAL (contexto institucional; D-ADERENCIA: só simulado diagnóstico). PENDENTE NORMATIVO.

## Contagens

| quesito | valor |
|---|---|
| total | 28 (14 em P2-2.1, 14 em P2-2.2) |
| C | 14 (R22, R23, R26, R27, R30, R31, R32, R34, R36, R37, R39, R43, R44, R45) = 50,0% |
| E | 14 (R19, R20, R21, R24, R25, R28, R29, R33, R35, R38, R40, R41, R42, R46) = 50,0% |
| C por folha | 2.1: 7 C / 7 E; 2.2: 7 C / 7 E |
| [TS] | 18 (64,3%; mínimo de metade mais 2 = 16): 14 em itens E (todos) e 4 em itens C (espelho: R26, R37, R39, R45); R31 sem [TS]; substitutos com [TS]: R24 e R40 |
| VOLÁTIL | 3 novos, todos de risco BAIXO (R24, R25, R37); risco alto: 0 |
| VOLÁTEIS por folha | P2-2.1: 2/20 (10%); P2-2.2: 1/20 (5%) |
| Formatos P2-2.1 (de 20) | SH 5, TS 5, PC 4, D 4, AP 2, NP 0 (maior: 25%) |
| Formatos P2-2.2 (de 20) | SH 5, TS 4, PC 4, AP 4, D 2, NP 1 (maior: 25%) |
| Aderência | 12 direta; 16 PARCIAL (R19, R21, R22, R25, R27, R28, R29, R31, R32, R35, R38, R39, R41, R42, R45, R46) |
| CONFERÊNCIA DE BASE (jan/2027) | os 28 (as bases do RICD e do Ato 251 no Legin; as demais, páginas de fornecedor ou do portal) |
| REVERIFICAR (VOLÁTEIS) | R24, R25, R37 |
| PENDENTE NORMATIVO | 14 (R19, R20, R21, R22, R28, R29, R31, R32, R38, R39, R41, R42, R45, R46) |

Registros de estilo (O-1 a O-8, recomendações da estilo_onda_2.md, seção 5):
- O-1 extensão (recontada por script): C média 40,1 palavras (máximo 52); E média 39,9 (máximo 52); nenhum C acima de 65.
- O-2: "independentemente" em E (R20, R33).
- O-3: "pode" aparece em C (R24, R30, R44) e em E (R25 não; R35 não); sem uso sistemático que denuncie o gabarito.
- O-4: remissões a norma ficam no sujeito ("de acordo com o Ato", "segundo o RICD"); a ambientação parlamentar (R24, R27, R32, R37) não entra no escopo da fonte além do que a fonte diz.
- O-5: um só absoluto por E (R42 "exclusiva"; R33 "constante" é da fonte).
- O-7: "apenas"/"somente" não usados; causais "pois" em C (R27, R36) e "por isso" em E (R35).
- O-8: "ainda que" em C (R24, R36) e nenhum em E nesta parte.
- Aberturas "Segundo a…" no máximo 7 em 28 e variadas; fonte nomeada em todo item que usa "a nota", "a documentação", "o cartão" ou "o rol".

## Tabela de proveniência (todas as páginas, arquivos e PDFs abertos e lidos em 18/10/2026)
| fonte | URL oficial | data da página / verificação | usada em |
|---|---|---|---|
| Câmara dos Deputados, Regimento Interno (Resolução nº 17/1989, texto atualizado, Legin) | https://www2.camara.leg.br/legin/fed/rescad/1989/resolucaodacamaradosdeputados-17-21-setembro-1989-320110-normaatualizada-pl.html | HTTP 200 em 18/10/2026 (art. 98, § 1º, primeira e segunda partes) | R19, R28 |
| Câmara dos Deputados, Ato da Mesa nº 251, de 16/03/2026 (Legin, publicação original) | https://www2.camara.leg.br/legin/int/atomes/2026/atodamesa-251-16-marco-2026-798819-publicacaooriginal-178493-cd-mesa.html | HTTP 200 em 18/10/2026; publicado no Diário da Câmara de 17/3/2026, p. 1251; arts. 1º, 2º (I, III, V, VI, VII, X), 3º, 4º (VIII), 5º, 6º, 7º (I) | R20, R21, R22, R29, R31, R32, R38, R39, R41, R42, R45, R46 |
| Câmara dos Deputados, "Produtos e Serviços do Departamento de Taquigrafia, Revisão e Redação – DETAQ" (PDF, setembro de 2009) | https://www2.camara.leg.br/a-camara/estruturaadm/consultoria-geral/estrutura-1/detaq/discursos/rol-do-detaq (devolve PDF de 24 páginas) | PDF aberto e lido em 18/10/2026 (itens 5, 6, 9 e 10); documento de 2009, do então DETAQ | R23, R24, R40 |
| Câmara dos Deputados, Banco de Discursos, "Como pesquisar" | https://www2.camara.leg.br/atividade-legislativa/discursos-e-notas-taquigraficas/pesquisa/como-pesquisar | HTTP 200 em 18/10/2026; página sem data de edição | R25 |
| Microsoft, Azure Speech, nota de transparência de speech to text ("Use cases for Speech to text") | https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/transparency-note (a URL /legal/cognitive-services/speech-service/speech-to-text/transparency-note redireciona para esta) | "Last updated on 2026-03-31"; verificado em 18/10/2026 | R30, R33, R34, R35, R36, R43 |
| Microsoft, Azure Speech, "How to create human-labeled transcriptions" | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-custom-speech-human-labeled-transcriptions | "Last updated on 2025-12-29"; verificado em 18/10/2026 | R26 |
| OpenAI, repositório oficial openai/whisper, model-card.md (ramo main) | https://raw.githubusercontent.com/openai/whisper/main/model-card.md | arquivo aberto e lido em 18/10/2026 (HTTP 200) | R27 |
| AWS, Amazon SageMaker AI, "Using Amazon Augmented AI for Human Review" | https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.html | verificado em 18/10/2026 (a página informa que o A2I não está aberto a novos clientes) | R37 |
| Google Cloud, Speech-to-Text, Best practices | https://docs.cloud.google.com/speech-to-text/docs/best-practices | "Last updated 2026-10-13 UTC"; verificado em 18/10/2026 | R44 |

Fontes que tentei abrir e não abri (nenhum item depende delas): www.camara.leg.br e www12.senado.leg.br (conexão recusada pelo proxy), páginas "Discursos em tempo real" e "Arquivo sonoro" do portal da Câmara (conteúdo em iframe ou host fechado), A2I "Core Components" e "Use Cases" (a URL tentada devolveu a página-índice). Nenhum item usa base de data anterior (D-FONTE-DATA-ANTERIOR).

## Dúvidas à Gerência (D1 da gce-gerencia)
1. Documento de 2009 (ROL) como base de R23, R24 e R40: é documento oficial da Câmara, aberto hoje, mas descreve o então DETAQ e fluxo de serviço de 2009. Foi tratado como VOLÁTIL baixo, sem número (os prazos de 2 horas e 2 dias úteis do documento não foram cobrados). Se a Gerência preferir não usar documento de 2009 em item, R23, R24 e R40 precisam ser trocados; os demais não são afetados.
2. Aderência do Ato nº 251/2026 à 2.1 e à 2.2: R29, R45 e R46 foram marcados PARCIAL (ata e estrutura do departamento). Os demais itens do Ato (R20, R21, R22, R31, R32, R38, R39, R41, R42) tratam do registro oficial, da redação final, da responsabilidade pelo texto e do uso de IA no processo, e foram marcados direta. A Gerência decide se mantém.
3. Proximidade com as partes B, C e D da onda 3 (folhas 2.3 a 2.8): a nota de transparência do Azure e o Ato nº 251/2026 podem servir também às folhas 2.3 (supressão de expressões antirregimentais, art. 2º, IV), 2.4, 2.7 (qualidade, art. 6º, V; amostragem) e às folhas 3.x. Os pontos desta parte são os listados na Parte 1; a conferência cruzada com as outras partes fica com a Gerência.

FIM DA PARTE 3/3
FIM DO LOTE
