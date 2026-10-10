# simulado_1_reconciliacao.md — T-06 — 2026-10-10 — gerado por gbq-gerencia

REMETENTE: GBQ — Gerência de Banco de Questões e Simulados
DESTINATÁRIO: orquestrador (roteamento e estado da T-06); GCB (T-32, para conhecimento); Presidência: nenhum gatilho neste ciclo

- Entrada: `saida/simulados/simulado_1.md` e `saida/simulados/simulado_1_gabarito.md` (T-06, gbq-csc, 10/10/2026).
- Conferido contra:
  - os arquivos canônicos `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` (v3.3), `GCB_Lote4C_v1_GCB-CPP.md` (v1.1), `GCB_Lote5_v3_canonica_GCB-CPP.md` (v3.1) e `GCB_Lote5C_v1_GCB-CPP.md` (v1.1), nas seções (d) e (d-G);
  - o registro `saida/gbq/claude_GBQ_Registro_AUTORAL_v2.md`;
  - `banco/banco.csv`;
  - os Simulados 0 e 0 v0.2, com seus gabaritos;
  - `edital/TI_itens_5_8_P1.md`.
- Regras aplicadas: CLAUDE.md (com o Adendo v2.1), DECISOES.md (D-CANONICOS, D-QA-PENDENTE, D-ADERENCIA, D-REVERIFICACAO-JAN, D-COMPLEMENTOS), regra (c) da gbq-gerencia, registro v2 (R1, R1-N, R2, R4) e pontuação +1/−1/0 (edital 8.11.2). Papéis: gbq-gerencia e gce-gerencia.
- A conferência foi feita por script, somente leitura (scratchpad `t06_gbq/verify_gbq.py`). Nenhum arquivo do simulado, do banco ou dos lotes foi editado.
- Linha de base para o ajuste T-31:
  - instruções + corpo (de "## Instruções" até antes de "## Verificação (montagem)"): sha256 `427ad5d06ec47341…`, 9408 caracteres;
  - `simulado_1_gabarito.md`: `4c19e45a98fa08db…`.

## 1. Regras de montagem (item c da GBQ): 32 de 32 verificações OK

| Regra | Resultado | Evidência (script) |
|---|---|---|
| Só aprovados e canônicos | CUMPRIDA | 40/40 ids estão no registro v2 e nos d-G dos quatro arquivos (D-CANONICOS: Lote 4 v3.3, 4-C, Lote 5 v3.1, 5-C). Pareceres: 4-C e 5-C CONFERIDOS; Lotes 4 e 5 v3 CONFERIDOS pela CQFP (8/10). Itens substituídos já estão na redação final (4C-06, 4C-09, 5C-03, A5-02, A5-09). |
| Nenhum VOLÁTIL, REVERIFICAR, PENDENTE ou "a confirmar" | CUMPRIDA | Os VOLÁTEIS do registro em P1 5–8 são L4-15 e A5-14 a A5-17, e nenhum foi selecionado. Nos 40 d-G usados: 0 ocorrência de VOLÁTIL, REVERIFICAR, PENDENTE ou "a confirmar". Nos quatro arquivos: 0 "QA PENDENTE". No corpo: 0 VOLÁTIL, REVERIFICAR, PENDENTE, L4-11, BQ- ou TRF6. |
| Equilíbrio C/E | CUMPRIDA | 20 C / 20 E. Sequência `CCEEECCEECECCCEECECEECECEECEECCCECECCECE`, maior corrida 3. 19 [TS]. |
| Literalidade | CUMPRIDA | Enunciado = (d) canônico: 40/40. Gabarito da tabela = mapa = d-G: 40/40. Gabarito = registro v2: 40/40. Subitem = registro: 40/40. [TS] no mapa = d-G = registro: 40/40. Justificativa = entrada integral do d-G: 40/40. Numeração 1–40 contínua, 40 ids distintos. |
| Cobertura do edital | CUMPRIDA com falta registrada | 8 dos 9 subitens-folha de P1 5–8: 5.1 = 8 (4 C), 5.2 = 4 (2), 5.3 = 4 (2), 6 = 4 (2), 7.1 = 4 (2), 8.1 = 3 (1), 8.2 = 7 (4), 8.4 = 6 (3). Os cinco gráficos de 8.2 estão presentes. 8.3 fica sem item: ver 3(a). Por lote: L4 16, 4-C 4, L5 14, 5-C 6. |
| Sem repetição de simulado anterior | CUMPRIDA | Simulados 0 e 0 v0.2 (corpo e gabarito): 0 id e 0 enunciado coincidentes, com texto normalizado. Nenhum enunciado coincide com texto do banco. A única menção a id AUTORAL nos simulados anteriores é "L4-11", na regra R2, sem o item. |
| L4-11 × TRF6 item 81 (R2) | CUMPRIDA | L4-11 está fora do simulado. Nenhum item do banco está no corpo, logo BQ-0010 (TRF6 item 81) também não. |
| D-ADERENCIA | CUMPRIDA | 40/40 AUTORAL, aderência direta por construção (registro v2, R4). |

## 2. Amostragem: 5 itens contra os arquivos canônicos (semente 20261010)

| nº | id | Texto: simulado = canônico | Gabarito: simulado / d-G / registro | Subitem |
|---|---|---|---|---|
| 3 | 4C-05 | idêntico ("Um prompt que reúna papel, formato de saída e restrições bem definidos elimina o risco de alucinação…") | E / E / E | 5.1 |
| 15 | L4-13 | idêntico ("Todo modelo de fundação é um grande modelo de linguagem (LLM)…") | E / E / E | 5.3 |
| 17 | L4-17 | idêntico ("Segundo a LGPD, os dados anonimizados não são considerados dados pessoais, salvo…") | C / C / C | 6 |
| 22 | A5-02 | idêntico ("A padronização das grafias "PL", "P.L." e "Projeto de Lei"…"), redação v3 (F3 b) | C / C / C | 7.1 |
| 23 | A5-04 | idêntico ("Dados estruturados são aqueles que não seguem esquema predefinido…") | E / E / E | 7.1 |

Resultado da amostra: 5/5 conferem, em texto e gabarito literais. Coincide com a conferência integral 40/40 da produtora.

## 3. Reconciliação ponto a ponto (D1 GBQ)

### (a) Subitem 8.3 sem item: falta ACEITA
- O subitem 8.3 (Power BI, Tableau e Data Studio) não tem item apto a simulado final em toda a fábrica:
  - os 4 AUTORAL (A5-14 a A5-17) são VOLÁTEIS;
  - no banco, BQ-0017 e BQ-0035 são VOLÁTEIS e de aderência parcial;
  - o único item apto, BQ-0048, já está no Simulado 0 v0.2 (item 39) e é de banco, fora do escopo da T-06 (só AUTORAL).
- "Nunca VOLÁTIL em simulado final" (CLAUDE.md; R1) prevalece sobre a cobertura. A falta é de cobertura, não de quantidade.
- Itens novos de 8.3 sem dependência de produto: DESCARTADO por ora. Abrir itens novos exige ordem da Presidência (D-COMPLEMENTOS), e a reverificação de 4–8/1/2027 (T-11) é o caminho já decidido para liberar A5-14 a A5-17 antes da prova.
- **Decisões:**
  - a folha de prova passa a avisar a candidata, numa linha neutra, que 8.3 não é coberto (vai na T-31);
  - a cobertura de 8.3 em simulado final fica para depois da T-11 (T-33).
- **Classe: AGORA (aviso, T-31); PRÓXIMO, datado (T-33).**

### (b) L4-11 e o Despacho 9 não aplicado ao arquivo do Lote 4: tarefa para a GCB, sem gatilho
- Fato conferido:
  - o arquivo-espelho `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` está no cabeçalho v3.3;
  - o d-G do item 11 ainda diz "gabarito a confirmar contra o GAB_DEFINITIVO";
  - a cópia do Projeto no claude.ai (busca no Projeto, 10/10/2026) também mostra a linha O6 só como "conferida", sem a v3.4;
  - `Despachos_pendentes_GCB-CPP.md` registra "Pendente: Despacho 9 (Lote 4 v3.4)".
  
  Conclusão: o Despacho 9 não foi executado em lugar nenhum, e nenhuma tarefa da fila o cobre.
- **Mérito para o simulado:** o Despacho 9 só muda texto de curso e do d-G. Enunciado e gabarito (C) de L4-11 não mudam, e o gabarito definitivo E do TRF6 81 é confirmado no GAB_DEFINITIVO do Projeto.
  - L4-11 é **apto** a simulado final sem o BQ-0010.
  - A exclusão é aceita como escolha de montagem, porque o mapa copiaria a justificativa defasada. Não é inelegibilidade.
  - O 5.2 ficou com 4 itens, o que é suficiente.
- **Domínio:** executar o Despacho 9 é da GCB, que é titular do arquivo, despachou à GCB-CPP e cuida do canônico no Projeto. A decisão de mérito já foi tomada pela Presidência em 9/10.
  - Não há decisão nova a pedir, por isso não cabe gatilho B.
  - A GBQ registra a tarefa para a GCB (T-32), como fez com a T-28 para a GCE.
  - Reclassificar a tarefa cabe à GCB ou à Presidência.
- **Efeito no pacote:** o curso do L4 exportado leva os mesmos trechos ("a confirmar" e "unidade de taquigrafia"). A T-32 deve vir antes da T-27, mas não a bloqueia, pelo mesmo critério da T-28: o fato está certo e só a forma está defasada.
- **Classe: PRÓXIMO (T-32).**

### (c) L4-05 excluído "por precaução": exclusão ACEITA, motivo REJEITADO como critério
- Na v3 (R9), o d-G decidiu "Sem marca VOLÁTIL: o item afirma o conceito, não recurso de produto". O registro v2 não marca L4-05.
- L4-05 é **apto** a simulado final. Citar fonte de fornecedor (F1/F2) para um conceito não torna o item VOLÁTIL.
- A exclusão fica como escolha de proporção, porque 5.1 já tinha 8 itens. A "precaução" não deve ser repetida como motivo de exclusão em simulados futuros.
- **Classe: DESCARTADO** (sem ação).

### (d) Folha de prova com a seção "Verificação (montagem)": AJUSTE MECÂNICO necessário antes do aceite
- O `simulado_1.md`, que é a folha da candidata, termina com a seção "Verificação (montagem)". Ela traz:
  - o total "20 C e 20 E";
  - a divisão C/E **por subitem** (por exemplo, 8.1: "1 C, 2 E"; 5.2, 5.3, 6 e 7.1: "2 C, 2 E");
  - a distribuição por lote, ids e regras internas (L4-11, TRF6 item 81, VOLÁTIL, REVERIFICAR, versões de arquivo).
- O parágrafo de abertura também traz jargão de montagem ("AUTORAL canônicos dos Lotes 4, 4-C, 5 e 5-C (saida/gcb/), sem nenhum item VOLÁTIL, sem item pendente de QA").
- Num simulado **final**, com pontuação +1/−1/0, saber a divisão C/E por subitem permite chute dirigido e falseia a medida. A própria instrução da folha diz que gabarito e mapa "não fazem parte da folha de prova".
- No Simulado 0 v0.2 o aviso C/E era deliberado, porque se tratava de diagnóstico com desequilíbrio a sinalizar. Aqui não é.
- O conteúdo da seção já está, idêntico, no `simulado_1_gabarito.md`. Retirá-la da folha não perde informação.
- **Decisão D1:** ajuste mecânico (T-31), sem mudar item, ordem, numeração, comando, texto ou gabarito:
  - retirar a seção da folha;
  - neutralizar a frase de montagem da abertura;
  - acrescentar a linha de aviso de 3(a).
- Até a T-31 ser reconciliada, o Simulado 1 **não está pronto para aceite como simulado final**.
- **Classe: AGORA (T-31).** É AGORA, e não PRÓXIMO, porque o gatilho A depende dela (precedente: T-15).

### (e) Pista cruzada: ACEITA
- A5-18 (C, storytelling a serviço de uma mensagem) e 5C-07 (E, storytelling × dashboard trocados) tocam o mesmo conceito.
- O ponto de julgamento é distinto (d-G do 5C-07), e só quem já sabe A5-18 deduz 5C-07. É vizinhança normal de bloco Cebraspe.
- A produtora tratou como impeditivos os casos em que um enunciado entrega o outro (L4-02 × 4C-02; 4C-09 × L4-06), o que está correto.
- **Classe: DESCARTADO.**

## 4. Veredito da T-06

**T-06: CONCLUÍDA** e reconciliada em 10/10/2026.
- A montagem está correta: 40 AUTORAL aptos, 20 C / 20 E, literais 40/40, regras (c) cumpridas e cobertura de 8 dos 9 subitens, com falta justificada.
- **Ainda não está pronta para aceite como simulado final:** depende do ajuste mecânico T-31 da folha de prova, feito pela gbq-csc e reconciliado pela GBQ.
- Depois disso, a GBQ confere por script e emite o gatilho A: o corpo deve continuar igual à linha de base, e a folha deve ficar sem contagens C/E e sem ids.
- **Gatilho A: não emitido**, porque o simulado não está pronto.
- Nenhum outro gatilho (B a E) se configura:
  - o Despacho 9 é execução de decisão já tomada, registrada para a GCB (T-32);
  - não há conflito acima de D1 nem decisão D2;
  - a entrega à candidata (PILOT_01) segue reservada ao Fundador e será perguntada no gatilho A.
- O orquestrador marca a T-06 como CONCLUÍDA no seu controle de estados. A GBQ não reescreve linhas de TAREFAS.md.

## 5. Tarefas novas (append único a TAREFAS.md)
- T-31 (GBQ, AGORA): ajuste mecânico da folha do Simulado 1. Condição do gatilho A.
- T-32 (GCB, PRÓXIMO): executar o Despacho 9 (Lote 4 v3.4) no canônico do Projeto e no espelho da fábrica.
- T-33 (GBQ, PRÓXIMO, datado): cobertura de 8.3 em simulado final depois da T-11.

## 6. Gatilhos
Nenhum.
