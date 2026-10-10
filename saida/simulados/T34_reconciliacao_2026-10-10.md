# T34_reconciliacao_2026-10-10.md — T-34 — 2026-10-10 — gerado por gbq-gerencia

REMETENTE: GBQ — Gerência de Banco de Questões e Simulados
DESTINATÁRIO: orquestrador (roteamento da T-35 à gbq-csc e da T-34, rodada 2, à gbq-cqe); Presidência: nenhum gatilho neste ciclo

- Entrada: `saida/simulados/simulado_1_QA_2026-10-10.md` (T-34, gbq-cqe, rodada 1): REPROVADO, 3/40 (7,5%), itens 35 (5C-10), 39 (5C-09) e 40 (5C-07), todos pelo critério (2) (divergência D-1 do Comando 8). Critérios (1), (3) e (4): 40/40. Abaixo de 30%: sem gate.
- Regras: CLAUDE.md (v2 + Adendo v2.1), DECISOES.md (D-SIM1-DEVOLVIDO, D-CANONICOS, D-QA-PENDENTE, D-ADERENCIA), regra (c) da gbq-gerencia, registro AUTORAL v2 (R1, R1-N, R2, R4), TAREFAS.md (R-04, T-31, T-34). Papéis: gbq-gerencia e gce-gerencia.
- Fato conferido pela GBQ, somente leitura: comando canônico do Lote 5 (`GCB_Lote5_v3_canonica_GCB-CPP.md`, l. 240) = "No que se refere ao storytelling para visualização de dados, julgue os itens A5-18 a A5-20."; do Lote 5-C (`GCB_Lote5C_v1_GCB-CPP.md`, l. 28) = "Acerca do storytelling para visualização de dados, julgue os itens de 5C-07 a 5C-10.". A folha usa só o primeiro para os 6 itens do Comando 8. Nenhum arquivo foi editado pela GBQ.

## 1. Arbitragem D1: leitura A (por item) — divergência PROCEDENTE

Fundamentos, em ordem de peso:

1. **A própria folha define o vínculo por item.** Instruções de `simulado_1.md`: "Cada item está vinculado ao comando que imediatamente o antecede". Para 5C-10, 5C-09 e 5C-07, o comando que os antecede não é o comando canônico deles. A leitura B (por bloco) contradiz a regra que a folha declara à candidata.
2. **Literalidade do canônico (D-CANONICOS; regra (c): "só itens aprovados").** O item aprovado pela CQFP é o da seção (d), e na (d) cada item está sob o seu comando. Copiar o enunciado e trocar o comando não reproduz o item aprovado. A literalidade vale para o item inteiro.
3. **Critério (2) de D-SIM1-DEVOLVIDO / T-34.** O critério foi fixado com veredito "por item e geral" e conferência 40/40. Pela regra do agente presidencia, falta de condição devolve "sem aceite com ressalva". Converter um REPROVADO por item em APROVADO por releitura do critério seria, em substância, uma ressalva. A GBQ não produz nem revisa conteúdo (agente; CLAUDE.md), por isso não lhe cabe desconsiderar a divergência registrada pelo QA independente.
4. **Precedente da fábrica.** O Simulado 0 v0.2 (R-04) foi montado "agrupado por comando original", com 34 comandos para 60 itens e cada item sob o seu próprio comando. A T-06 deveria ter seguido o mesmo princípio.
5. **Custo.** A correção é mecânica: muda bloco e numeração de 4 itens, sem tocar em texto, gabarito, [TS], seleção ou contagens. Ela cabe na rodada 2, a última permitida no ciclo.

Leitura B: **REJEITADA**. A identidade de escopo (8.4) e a diferença limitada à fórmula de abertura não afastam os pontos 1 e 2.
Veredito da T-34, rodada 1: **REPROVADO, aceito.** A T-34 continua aberta para a rodada 2.
Classe: **AGORA**, porque é condição do gatilho A.

## 2. Correção — T-35 (gbq-csc), especificação mecânica

**Princípio:** dividir o Comando 8 em dois blocos, cada um com o comando canônico do seu lote sem a faixa. Os itens 1–34 e os Comandos 1–7 ficam intactos. Dentro de cada lote, a ordem relativa atual é mantida. Entre as alternativas, esta é a que renumera menos itens: 4 itens, contra 5 se o bloco do 5-C viesse antes. A divisão em três blocos sem renumerar foi descartada porque repetiria o mesmo comando em blocos não contíguos e deixaria um bloco de um só item sob "julgue os itens".

### 2.1 `simulado_1.md`
- **Linha 1:** `# simulado_1.md — T-06; T-31; T-35 — 2026-10-10 — gerado por gbq-csc`.
- **Linhas 2–181:** sem nenhuma alteração. A linha de base é 8797 bytes, sha256 `e59b73ce67e86205…`, e cobre tudo até antes de "### Comando 8".
- **"### Comando 8":** mantido, com o mesmo comando ("No que se refere ao storytelling para visualização de dados, julgue os itens a seguir."). Passa a conter só os itens abaixo, com o texto atual inalterado:
  - **35.** = atual 36 (A5-20)
  - **36.** = atual 37 (A5-18)
  - **37.** = atual 38 (A5-19)
- **Novo bloco, logo depois:** cabeçalho `### Comando 9`, linha em branco e depois `> Acerca do storytelling para visualização de dados, julgue os itens a seguir.`. Itens, com o texto atual inalterado:
  - **38.** = atual 35 (5C-10)
  - **39.** = 5C-09, sem mudança
  - **40.** = 5C-07, sem mudança
- **Formato:** o mesmo dos blocos existentes (linha em branco, `**n.** texto`, linha em branco, `Resposta: [   ]`). A folha continua terminando no "Resposta: [   ]" do item 40. Nada mais é acrescentado: nenhuma nota, id ou contagem.

### 2.2 `simulado_1_gabarito.md`
- **Linha 1:** `# simulado_1_gabarito.md — T-06; T-31; T-35 — 2026-10-10 — gerado por gbq-csc`.
- **Grade:** 35 = C, 36 = C, 37 = E, 38 = E. As demais 36 células ficam inalteradas (39 = C e 40 = E já estão assim).
- **Mapa:**
  - as linhas 35–38 passam a ser as linhas atuais de A5-20, A5-18, A5-19 e 5C-10, nessa ordem;
  - só a coluna nº muda, e as outras colunas são copiadas sem alteração;
  - as linhas 1–34, 39 e 40 ficam inalteradas.
- **"Sequência do gabarito":** passa a ser `CCEEECCEECECCCEECECEECECEECEECCCECCCEECE — maior corrida de mesma resposta: 3 (embaralhamento por bloco, semente 0; itens 35–38 reordenados na T-35)`.
- **Contagens:** 20 C/20 E, 19 [TS], por lote e por subitem, ficam inalteradas.
- **Seção "Regras e falta registrada":** acrescentar uma linha ao final: "Ajuste T-35 (10/10/2026, gbq-csc): Comando 8 dividido em dois blocos com os comandos canônicos literais sem a faixa (Comando 8, Lote 5: itens 35–37 = A5-20, A5-18, A5-19; Comando 9, Lote 5-C: itens 38–40 = 5C-10, 5C-09, 5C-07), conforme T34_reconciliacao_2026-10-10.md; texto, gabarito, [TS] e justificativa inalterados."
- Nenhuma outra linha do gabarito muda.

### 2.3 Vedado na T-35
- Mudar texto, gabarito, [TS], justificativa ou seleção.
- Tocar nos itens 1–34 ou nos Comandos 1–7.
- Editar lotes, registro ou banco.
- Usar git para escrever.

**Relatório da gbq-csc:** `saida/simulados/T35_2026-10-10.md`, com o diff e a conferência por script.

## 3. Rodada 2 — T-34 (gbq-cqe), conferência
- **Mesmo método da rodada 1, sobre os arquivos corrigidos:** critérios (1) a (4), 40/40, com veredito por item e geral.
- **Critério (2) por item:** o comando do bloco de cada item é igual ao comando canônico do próprio item sem a faixa, com 9 blocos esperados.
- **Diff contra a versão de rodada 1:** só são aceitas as mudanças de 2.1 e 2.2. O sha256 das linhas 2–181 da folha deve ser `e59b73ce67e86205…`.
- **Saída:** `saida/simulados/simulado_1_QA_R2_2026-10-10.md`.
- **Se o resultado for APROVADO/CONFERIDO 40/40:** a GBQ reconcilia e reemite o gatilho A, citando o QA independente da T-34 nas duas rodadas.
- **Se não for:** não haverá terceira rodada no ciclo. Gatilho C à Presidência no ciclo seguinte.

## 4. Tarefas novas (append único a TAREFAS.md)
- **T-35** (GBQ, AGORA): correção mecânica do Comando 8 do Simulado 1, conforme a seção 2 acima, com fluxo gbq-csc → gbq-cqe (T-34, rodada 2) → gbq-gerencia.

## 5. Gatilhos
Nenhum. O gatilho A do Simulado 1 aguarda a T-35 e a rodada 2 da T-34 com APROVADO/CONFERIDO. A entrega à candidata (PILOT_01) segue reservada ao Fundador.

## Rodada 2 — reconciliação de T-35 e T-34 R2 (gbq-gerencia, 10/10/2026)

- **Entradas:**
  - `saida/simulados/T35_2026-10-10.md` (gbq-csc): correção aplicada conforme a seção 2.
  - `saida/simulados/simulado_1_QA_R2_2026-10-10.md` (gbq-cqe, T-34, rodada 2): APROVADO/CONFERIDO 40/40, 0% de reprovados, D-1 SANADA.
- **Conferência própria da GBQ:**
  - por script, somente leitura: scratchpad `t34_gbq_r2/verify.py`, com `git show HEAD:<arquivo>` comparado à árvore de trabalho e difflib;
  - script independente dos da gbq-csc (`t35/`) e da gbq-cqe (`t34/qa_t34.py`);
  - resultado: **28/28 OK**.

| Verificação | Resultado |
|---|---|
| Folha, linhas 2–181 | iguais ao HEAD; sha256 `e59b73ce67e86205…`, 8797 bytes |
| Folha, linha 1 | "T-06; T-31; T-35" |
| Itens 1–34 e Comandos 1–7 | idênticos ao HEAD |
| Itens 35–40 | texto do HEAD permutado exatamente (35←36, 36←37, 37←38, 38←35; 39 e 40 fixos) |
| Blocos de comando | 9 blocos |
| Comando 8 (itens 35–37: A5-20, A5-18, A5-19) | = canônico do Lote 5 sem a faixa (l. 240) |
| Comando 9 (itens 38–40: 5C-10, 5C-09, 5C-07) | = canônico do Lote 5-C sem a faixa (l. 28) |
| Fim da folha | termina no item 40 |
| Linhas "Resposta: [   ]" | 40, vazias |
| Pistas na folha | 0 (ids, "Lote", VOLÁTIL, REVERIFICAR, PENDENTE, TRF6, [TS], AUTORAL, CEBRASPE_, ANALOGA, QA, contagens C/E) |
| Grade e mapa | = HEAD com a mesma permutação; no mapa só a coluna nº mudou |
| Grade 35–38 | C, C, E, E |
| Gabarito do mapa | = grade, 40/40 |
| Diff do gabarito (17 linhas) | só cabeçalho, grade, mapa 35–38, sequência e a linha "Ajuste T-35" |
| Sequência | `CCEEECCEECECCCEECECEECECEECEECCCECCCEECE` declarada = recalculada; sequência antiga ausente; maior corrida 3 |
| Contagens | 40 itens; 20 C/20 E; 19 [TS] |
| Por lote | L4 16, 4-C 4, L5 14, 5-C 6 |
| Por subitem (itens, C) | 5.1 (8, 4), 5.2 (4, 2), 5.3 (4, 2), 6 (4, 2), 7.1 (4, 2), 8.1 (3, 1), 8.2 (7, 4), 8.4 (6, 3) — inalterado |
| `saida/gcb`, `saida/gbq`, `edital`, `banco` | sem modificação |

- **Diff da folha:** `git diff --stat` dá +9 −5 na folha e +9 −8 no gabarito, iguais aos relatados pela gbq-cqe.
- **Script da gbq-csc:** o relatório da gbq-csc cita "base_qa.py" como reutilização do script de QA da T-34. A rodada 2 da gbq-cqe não o usou, porque rodou o próprio `qa_t34.py`, e a conferência da GBQ é independente dos dois. A separação produção × QA está preservada. **Aceito (D1)**, sem efeito.
- **Vereditos:**
  - **T-35: CONCLUÍDA** e reconciliada.
  - **T-34: CONCLUÍDA**, com APROVADO/CONFERIDO na rodada 2, a última do ciclo.
  - **D-SIM1-DEVOLVIDO: condição cumprida.** O QA independente está concluído, com APROVADO/CONFERIDO, sobre o simulado como objeto.
- **Mantidos:**
  - falta do 8.3, com aviso na folha, e a T-33;
  - a entrega à candidata (PILOT_01), que segue reservada ao Fundador.
- **Tarefas novas:** nenhuma.
- **Gatilho:** GATILHO A do Simulado 1 reemitido em PARA_PRESIDENCIA.md, por append único.
