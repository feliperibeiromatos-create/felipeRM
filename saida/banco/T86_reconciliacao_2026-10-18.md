# T86_reconciliacao_2026-10-18.md — T-86 — 2026-10-18 — gerado por gbq-gerencia

Objeto: T-86, varredura P1-DA das lacunas da T-79, linhas BQ-0153 a BQ-0192. Este arquivo traz a reconciliação e o D1.

Bases lidas:
- a linha T-86 de TAREFAS.md;
- saida/banco/varredura_2026-10-18.md (gbq-cfp, produção);
- saida/banco/QA_T86_2026-10-18_gbq-cqe.md (proveniência e aderência);
- saida/banco/QA_T86_normativo_2026-10-18_qa-normativo-da.md (texto vigente);
- banco/SCHEMA.md;
- em DECISOES.md: D-ADERENCIA, D-ROTULOS, D-QA-PENDENTE, D-REVERIFICACAO-JAN, D-BQ0151-DIVERGE e D-BQ0141-REVERIFICAR;
- o precedente saida/banco/T79_reconciliacao_2026-10-17.md.

A gbq-gerencia não produz nem revisa conteúdo. Aqui ela decide o D1 e altera só as colunas observacoes (40 linhas) e aderencia (1 linha, BQ-0191). Nenhum gabarito, texto, comando, texto-base, rótulo ou mapeamento foi tocado.

## 1. Situação dos QAs
**gbq-cqe:**
- Verificou 40 de 40 linhas e aprovou todas, sem nenhuma reprovação ou correção (0%, abaixo do gate de 30%).
- Os gabaritos somam 17 C, 23 E e 0 X. As 40 linhas conferem visualmente com o gabarito definitivo do CDN, e nenhuma aparece em justificativa de alteração ou de anulação.
- Rótulos: 20 CEBRASPE_OFICIAL (cd_25_ns) e 20 CEBRASPE_ANALOGA, de acordo com a D-ROTULOS. São as primeiras linhas do banco vindas do certame-alvo.
- Não há duplicidade.
- Ficaram para arbitragem 3 aderências (BQ-0179, 0180 e 0191) e 2 ajustes mecânicos (A1 na BQ-0174, A2 na BQ-0180).

**qa-normativo-da:**
- 23 itens CONFEREM, nenhum DIVERGE e nenhum fica para REVERIFICAR.
- 2 itens se apoiam em norma estadual e ficam fora do escopo do Planalto (BQ-0179 e 0180).
- 15 itens ficam fora do QA normativo: 12 de doutrina e 3 em que só o dispositivo correlato foi conferido, sem incompatibilidade.
- Nenhuma fonte não oficial foi usada.

## 2. D1 — aderência (D-ADERENCIA)
**BQ-0179 (TJ-ES 2023, CG, #44, C): PARCIAL, mantida, e o item fica só para simulado diagnóstico.** O comando manda julgar "De acordo com o Regime Jurídico dos Servidores Públicos Civis do Estado do Espírito Santo", uma norma que não está no edital da Câmara. O conteúdo é próximo da regra federal (Lei 8.112/1990, arts. 125 e 126). Mesmo assim, o qa-normativo-da registra que o art. 126 fala só em responsabilidade "administrativa", enquanto o item afirma o efeito também sobre a responsabilidade civil. Por isso a correspondência com o regime federal não é literal. Em simulado final, o item apareceria com um comando estadual, o que destoa da prova-alvo. A leitura direta da gbq-cqe fica registrada e não é acolhida.

**BQ-0180 (MPTO 2024, CG nível médio, #17, C): PARCIAL, mantida. Proponho a inaptidão a qualquer simulado, inclusive diagnóstico, por GATILHO D.**
- O C só vale para a Lei TO 1.818/2007.
- Na Lei 8.112/1990, art. 145, II, a sindicância admite advertência ou suspensão de até 30 dias, e o art. 146 exige PAD acima disso (gbq-cqe e qa-normativo-da, verificado em 18/10/2026). Pela regra federal, o enunciado seria E.
- Com isso, até o uso diagnóstico distorce o resultado: a candidata que domina a Lei 8.112 marca E e leva −1 (+1/−1/0), e quem estuda o C aprende "90 dias" para a sindicância federal (4.3). É risco de transferência negativa.
- O precedente é a D-BQ0151-DIVERGE: a inaptidão permanente a qualquer simulado foi decidida pela Presidência (competência D). Por isso, até a decisão, a linha mantém "QA PENDENTE", com o motivo reescrito, e fica fora de qualquer simulado e do pacote.

**BQ-0191 (TRF6 2024, Cargo 26, #51, E): DIRETA, P1-DA-9 (9.1).** A coluna aderencia passa de "parcial" para "direta", e o motivo fica registrado em observacoes, como exige o SCHEMA. Fundamentos:
- A afirmação testa exatamente a distinção governança × governabilidade do 9.1: o erro é atribuir à governabilidade a "capacidade financeira, gerencial e técnica de governar", que é a definição usual de governança.
- O comando de teoria e história da administração não retira o conteúdo do 9.1 e, de todo modo, cabe no item 8 do edital.
- O cargo de origem não é critério da D-ADERENCIA, que é de conteúdo. O precedente é a BQ-0114 (D1 da T-79).
- A leitura parcial da produtora fica registrada e não é acolhida.

**Itens do Cargo 2 (Técnico Legislativo) do cd_25_ns (BQ-0164 a 0172): DIRETOS, e o rótulo CEBRASPE_OFICIAL fica mantido.**
- A D-ROTULOS define o rótulo pelo certame, não pelo cargo.
- A D-ADERENCIA é critério de conteúdo e de edital, e os 9 itens cobrem literalmente os subitens 3.1 e 10.3 a 10.5.
- Não adoto "cargo distinto do certame-alvo" como critério de aderência.
- A calibragem é de nível de Técnico, o que fica registrado como informação para a montagem e não impede o uso.

**Mapeamentos alternativos** (BQ-0155, 0166, 0171, 0177, 0178 e 0192): sem alteração. As duas alternativas são diretas em todos os casos, então a escolha não muda a aptidão.

**Tipologia do guia (regras/estilo_banca.md):** não muda. Nenhum padrão novo foi proposto, então a regra "menos de 3 itens = removido ou indício" não se aplica.

## 3. D1 — ajustes mecânicos (só em observacoes, acrescentados ao fim da célula)
- **A1 (BQ-0174): ACEITO**, com o texto sugerido pela gbq-cqe: "comando literal do caderno (licitações, contratos administrativos e responsabilidade civil) não corresponde ao tema do item (PAD); transcrição conferida, não corrigir".
- **A2 (BQ-0180): ACEITO**, com o texto sugerido pela gbq-cqe: "atenção: o C vale para a Lei TO 1.818/2007; na Lei 8.112/1990, art. 145, II, a sindicância admite advertência ou suspensão de até 30 dias".

## 4. D1 — retirada de "QA PENDENTE" (D-QA-PENDENTE; precedentes R-03, T-40 e T-79)
Em cada linha, o trecho "QA PENDENTE; norma-alvo para o qa-normativo-da: …" (até "; comando:") foi substituído no mesmo lugar. O resto de observacoes não muda.

- **23 normativos com CONFERE** (BQ-0153, 0154, 0155, 0163 a 0178, 0181, 0182, 0186 e 0187) recebem: "QA T-86 concluído: proveniência APROVADA (gbq-cqe, 18/10/2026); qa-normativo-da T-86: <norma, dispositivo>, sustenta <C|E> (verificado em 18/10/2026, planalto.gov.br [e portal.stf.jus.br quando há tese ou súmula do STF])".
- **12 de doutrina** (BQ-0156 a 0162 e 0188 a 0192) recebem: "QA T-86 concluído: proveniência APROVADA (gbq-cqe, 18/10/2026); fora do QA normativo (doutrina; qa-normativo-da T-86)".
- **3 com dispositivo correlato conferido** (BQ-0183, 0184 e 0185) recebem o mesmo texto, mais "CF, art. 37, § 6º, conferido e compatível com o item".
- **BQ-0179** sai de QA PENDENTE como norma estadual fora do QA normativo federal. A linha registra o análogo federal e o D1 de aderência parcial.
- **Mantida com "QA PENDENTE": BQ-0180**, com o motivo reescrito no parêntese: QA concluído, mas o item fica fora de qualquer simulado até a decisão do gatilho D, ciclo s12c1.
- **VOLÁTIL:** nenhuma das 40 linhas depende de produto, então nenhuma é marcada.

## 5. Conferência por script e contagens
Comparei o banco.csv com a cópia anterior à reconciliação (= HEAD + 40 linhas da gbq-cfp):
- há 193 linhas (o cabeçalho e 192 registros), com 18 colunas em todas e ids únicos;
- só mudaram as colunas observacoes (40 células, BQ-0153 a 0192) e aderencia (1 célula, BQ-0191);
- as linhas BQ-0001 a 0152 e o cabeçalho ficaram idênticos;
- o CRLF continua uniforme (193 CRLF e 193 LF), e o arquivo termina em CRLF;
- `git diff --stat` mostra 40 inserções e 0 remoções frente ao HEAD.

Em todo o banco, "QA PENDENTE" fica só em BQ-0141 (T-87) e BQ-0180 (gatilho D).

**Aptidão das 40 linhas da T-86:**

| Classe | Qtde | Ids | C/E |
|---|---|---|---|
| Apto a simulado final (C/E, sem QA PENDENTE, sem VOLÁTIL, direta) | 38 | BQ-0153 a 0178, 0181 a 0192 | 15 C / 23 E |
| Só diagnóstico (parcial) | 1 | BQ-0179 | 1 C |
| Inapto, por ora (QA PENDENTE até o gatilho D) | 1 | BQ-0180 | 1 C |

**Lotes T-79 e T-86 somados (P1-DA), aptos a simulado final: 74, com 41 C e 33 E.** O reforço de E pedido na T-86 foi cumprido: o desequilíbrio da T-79 (26 C/10 E) ficou compensado.

| Item | DA-1 | DA-2 | DA-3 | DA-4 | DA-5 | DA-6 | DA-7 | DA-8 | DA-9 | DA-10 | DA-11 | DA-12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aptos | 4 | 3 | 9 | 10 | 3 | 6 | 4 | 7 | 9 | 11 | 4 | 4 |

As lacunas da T-79 ficaram cobertas, com pelo menos 1 item apto em cada uma:
- 3.1;
- 4.1 e 4.3;
- 6.1 a 6.3;
- 8.1 a 8.3;
- 9.1, 9.3 e 9.4;
- 10.3 a 10.5.

Seguem sem item apto direto: 8.4, 9.2 isolado (há a BQ-0187, mapeada em 9.1/9.2) e 10.2. Esses subitens ficam para uma próxima varredura, sem tarefa aberta agora. O alvo já está registrado aqui.

**Deduplicação P9 × BQ:** não houve. O banco é a fonte. Os pares de afinidade temática sem repetição de item, com gabaritos coerentes, são BQ-0173 × 0175 (SV 5) e BQ-0155 × 0172 (encargos de contratada). Ninguém deve montá-los no mesmo bloco como se fossem um par confundível sem revisão.

**Pacote:** sem gatilho A agora. As 38 linhas aptas e a BQ-0179 (como diagnóstico) entram na próxima T-12, com a gbq-csc conferindo as contagens contra os arquivos canônicos. Ficam fora do pacote a BQ-0180 (até o gatilho D), a BQ-0141 (T-87) e a BQ-0151.

## 6. Item #98, Cargo 2, cd_25_ns (X, anulado, não registrado)
**D1: registrar** como anulado e inapto a simulado, como leitura da banca do certame-alvo em P1-DA-3 (3.1; CF, art. 37, XIII). Os precedentes são BQ-0131 e 0133 (T-79) e BQ-0060, 0062 e 0063 (R-03).

A linha não é criada pela gerência. Fica a tarefa T-91 à gbq-cfp, com id no próximo livre (BQ-0193 se nenhuma outra varredura o ocupar antes) e QA da gbq-cqe.

## 7. Informação para a T-87 (registro; BQ-0141 não muda)
O qa-normativo-da informa, a partir da notícia oficial do STF de 1º/7/2026 (https://noticias.stf.jus.br/postsnoticias/stf-invalida-novos-dispositivos-da-reforma-da-lei-de-improbidade/), que o julgamento das ADIs 7156 e 7236 foi **concluído** nessa data. O registro de 17/10, na T-79 e na BQ-0141, dizia "sem resultado final com fonte".

A notícia de 24/6/2026 registra a tese acolhida sobre a perda da função pública: perda de todas as funções, com exceção fundamentada. O texto do art. 12, § 1º, e a ata ou acórdão não foram conferidos.

**D1:** a informação vai como insumo à T-87, que continua titular da reverificação. A BQ-0141 fica como está: gabarito E, "QA PENDENTE", fora de qualquer simulado. Se a T-87 confirmar que a tese acolhida diverge do E, isso é um novo gatilho D, como já está previsto na T-87. Nenhuma alteração é feita agora.

## 8. Reverificação de janeiro (D-REVERIFICACAO-JAN)
Os 23 ids normativos conferidos são BQ-0153, 0154, 0155, 0163, 0164, 0165, 0166, 0167, 0168, 0169, 0170, 0171, 0172, 0173, 0174, 0175, 0176, 0177, 0178, 0181, 0182, 0186 e 0187. Eles vão para a janela de 4–8/1/2027 pela tarefa nova T-92 (PRÓXIMO), que complementa a T-51 e a T-88 sem alterá-las.

## 9. Gatilhos e tarefas
- **GATILHO D | GBQ | BQ-0180:** inaptidão a qualquer simulado, inclusive diagnóstico. A recomendação é SIM.
- **Tarefas novas (PRÓXIMO):**
  - T-91: registrar o item #98 do cd_25_ns, Cargo 2, pela gbq-cfp, com QA da gbq-cqe.
  - T-92: incluir os 23 ids normativos da T-86 na reverificação de janeiro, pelo qa-normativo-da.

Estado da T-86: reconciliada pela GBQ. A linha da T-86 em TAREFAS.md não foi alterada por esta Gerência.
