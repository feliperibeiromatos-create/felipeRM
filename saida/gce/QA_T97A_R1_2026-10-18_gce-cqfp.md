# QA_T97A_R1_2026-10-18_gce-cqfp.md — T-97 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L2_reforco_onda3_A_v1.md (gce-cpp; 28 itens AUTORAL L2-R19 a L2-R46; P2-2.1 = R19–R32, P2-2.2 = R33–R46). Rodada R1 (de no máximo 2). Revisão; nada foi reescrito no objeto.
Lido: TAREFAS.md (T-97); DECISOES.md (D-REFORCO-1/2, D-FONTE-DATA-ANTERIOR, D-T89-R1-ACEITE, D-T96-ONDA2-ACEITE seção II, D-ONDA3-FILA, D-ADERENCIA); T90_reconciliacao (seção 4, legado e diluição; seção 1, precedente de aderência do L2-R02); T96_reconciliacao (seção 4, ponto contra o pacote inteiro); saida/banco/estilo_onda_2.md (seção 5); edital/modulo_RF_IA_P2.md; saida/pacote/pacote.json v1.9 (334 itens, varredura por script, python -I); L2_reforco_onda1_v3.md; finais da onda 2 (L1_reforco_onda2_A_v3, B_v2, C_v2, D_v3, saldo_v2); QA_T90_R1 (precedente de escopo: R09–R11). Outras partes da onda 3: C_v1 (2.5/2.6, R75–R102) e D_v1 (2.7/2.8, R103–R130) lidas no mapa; B (2.3/2.4) ainda não existe — conferência de gêmeos com a 2.3/2.4 fica para a R2 ou para a Gerência.

## 1. Evidência: bases reabertas por esta coordenação em 18/10/2026 (curl com User-Agent de navegador; todas HTTP 200)

| fonte | resultado | itens |
|---|---|---|
| Legin, Ato da Mesa nº 251/2026, publicação original | arts. 1º a 7º conferidos literalmente (2º I, III, V, VI, VII, X; 3º I–IV; 4º VIII; 5º I, IV, V; 6º I, IV; 7º I). Página "Dados da Norma" (…-798819-norma-cd-mesa.html): "Situação: Não consta revogação expressa"; indexação: "Departamento de Taquigrafia, Revisão e Redação (DETAQ) (1971-2026) - transformação - … (DEREP)". Nomenclatura "Derep (antigo DETAQ)" CONFERE (art. 1º) | R20–R22, R29, R31, R32, R38, R39, R41, R42, R45, R46 |
| Legin, RICD (norma atualizada) | art. 98, § 1º, primeira e segunda partes, literal CONFERE ("por extenso na ata impressa…"; "…as correções constarão da seção 'Errata'") | R19, R28 |
| Rol do DETAQ (PDF, 24 p., "Setembro de 2009") | itens 5, 6, 9 e 10 literais CONFEREM; o próprio PDF nomeia unidades extintas (COREV, COREF, SATEN), URLs camara.gov.br e "Banco de Dados do DETAQ" | R23, R24, R40 |
| Câmara, "Como pesquisar" | trecho literal CONFERE (a página traz duas redações do mesmo trecho, ambas compatíveis) | R25 |
| Microsoft Learn, nota de transparência STT (URL final /azure/foundry/…) | ms.date 2026-03-31; trechos de R30, R33, R34, R35, R36, R43 CONFEREM | idem |
| Microsoft Learn, human-labeled transcriptions | ms.date 2025-12-29; "word-by-word transcriptions of an audio file" CONFERE | R26 |
| raw.githubusercontent.com, openai/whisper model-card.md | "We recommend against use in high-risk domains like decision-making contexts…" CONFERE | R27 |
| docs.aws.amazon.com, A2I human review | "low-confidence predictions or random prediction samples" CONFERE; topo da página: "Amazon SageMaker A2I is no longer open to new customers. Existing customers can continue to use the service as normal… we do not plan to introduce new features" | R37 |
| docs.cloud.google.com, STT best practices | "Last updated 2026-10-13 UTC"; "Listen to some sample audio…" CONFERE | R44 |

Nenhuma base de data anterior (D-FONTE-DATA-ANTERIOR não acionada). Todas as bases reabertas; nenhuma "não reaberta".

## 2. Questões postas pela Presidência/orquestrador

**2.1 Rol do DETAQ de 2009 (R23, R24, R40) — INADMISSÍVEL como base.** (a) Para afirmar o funcionamento de hoje: não. O documento descreve unidade extinta (o Legin data o DETAQ de 1971 a 2026) e coordenações que o Ato nº 251/2026 não mantém (COREV, COREF; hoje Cogea, Coreg, Cored, Coged); fluxo, nomes de produto e ordem de etapas de 2009 não se presumem vigentes. (b) Ancorar o enunciado em "segundo o rol … de 2009" torna o gabarito estável, mas o item passa a cobrar o conteúdo de documento histórico e superado, fora do edital e sem forma de cobrança Cebraspe; e a marca VOLÁTIL fica incoerente: ou o item afirma fato atual (então a base de 2009 não o sustenta — regra 2 da D-REFORCO-2, "sem base, não entra"), ou afirma o conteúdo do documento (então não é VOLÁTIL, mas é extrapolação). Resposta à dúvida 1 da produtora: trocar os três.

**2.2 A2I fechado a novos clientes (R37).** VOLÁTIL (hipótese (c) da D-T96-ONDA2-ACEITE) correto; item admissível porque não afirma disponibilidade, mas a SH ("uma equipe deseja…") sugere adoção por cliente novo — ajuste no item (equipe que já usa o serviço). Se a página sair do ar ou mudar até 4–8/1/2027, retirar. Inapto a simulado final até a reverificação.

**2.3 Ato nº 251/2026 (12 itens) — base literal CONFERE em todos; aderência, não.** O Ato trata da estrutura e das competências do Derep. Pelo precedente da T-90 (L2-R02: norma que regula registro/publicação parlamentar, mas cujo ponto não é a diferença entre transcrição automática, degravação e revisão → PARCIAL; LC 95, norma não dirigida a transcrição → REPROVADO), item cujo ponto é "qual órgão ou coordenação faz X" é aderência PARCIAL a 2.1/2.2, e não REPROVADO. Só o R20 (responsabilidade humana pelo registro, contra a ferramenta) fica direto. Mesmo critério para RICD art. 98, § 1º (R19, R28: forma de publicação). Ver seção 5 (concentração).

**2.4 Escopo, formato e tetos.** Sem AP novo em 2.1: CONFERE. Sem D nova em 2.2: CONFERE. Maior formato 25% nas duas folhas: CONFERE na v1; depois das reprovações, 2.1 tem TS 5/18 (27,8%) — os substitutos não podem ser TS se a folha ficar acima de 6/20. **Defeito de formato:** R36 e R43 declarados AP sem nenhum elemento parlamentar; R44 só com "uma reunião" — ajuste no texto (seção 3).

**2.5 PENDENTE NORMATIVO.** Não há QA_T97_normativo do qa-normativo. R19, R20, R21, R22, R28, R29, R31, R32, R38, R39, R41, R42, R45 e R46 ficam PENDENTE NORMATIVO até o registro (conferência literal desta coordenação: CONFERE em todos; não substitui o qa-normativo — checklist 6).

## 3. Veredito por item

| id | fl. | gab. | conferido | formato | VOL | veredito |
|---|---|---|---|---|---|---|
| L2-R19 | 2.1 | E [TS] | CONFERE | SH | n | APROVADO COM AJUSTE (aderência PARCIAL) · PEND. NORM. |
| L2-R20 | 2.1 | E [TS] | CONFERE | TS | n | APROVADO COM AJUSTE (texto) · PEND. NORM. |
| L2-R21 | 2.1 | E [TS] | CONFERE | TS | n | APROVADO COM AJUSTE (aderência PARCIAL) · PEND. NORM. |
| L2-R22 | 2.1 | C | CONFERE | D | n | APROVADO COM AJUSTE (aderência PARCIAL) · PEND. NORM. |
| L2-R23 | 2.1 | E [TS] | literal confere; base inadmissível | PC | S | **REPROVADO** |
| L2-R24 | 2.1 | C | literal confere; base inadmissível | SH | S | **REPROVADO** |
| L2-R25 | 2.1 | E [TS] | CONFERE | TS | S baixo | APROVADO COM AJUSTE (aderência PARCIAL) |
| L2-R26 | 2.1 | C [TS esp.] | CONFERE | D | n | APROVADO |
| L2-R27 | 2.1 | C | CONFERE | SH | n | APROVADO COM AJUSTE (aderência PARCIAL) |
| L2-R28 | 2.1 | E [TS] | CONFERE | PC | n | APROVADO COM AJUSTE (aderência PARCIAL) · PEND. NORM. |
| L2-R29 | 2.1 | E [TS] | CONFERE | TS | n | APROVADO · PEND. NORM. (PARCIAL já declarada) |
| L2-R30 | 2.1 | C | CONFERE | PC | n | APROVADO |
| L2-R31 | 2.1 | C | CONFERE | D | n | APROVADO COM AJUSTE ([TS] retirado; aderência PARCIAL) · PEND. NORM. |
| L2-R32 | 2.1 | C | CONFERE | SH | n | APROVADO COM AJUSTE (aderência PARCIAL) · PEND. NORM. |
| L2-R33 | 2.2 | E [TS] | CONFERE | TS | n | APROVADO COM AJUSTE (texto) |
| L2-R34 | 2.2 | C | CONFERE | SH | n | APROVADO |
| L2-R35 | 2.2 | E [TS] | CONFERE | PC | n | APROVADO COM AJUSTE (texto; aderência PARCIAL) |
| L2-R36 | 2.2 | C | CONFERE | AP | n | APROVADO COM AJUSTE (texto: AP) |
| L2-R37 | 2.2 | C [TS esp.] | CONFERE | SH | S baixo | APROVADO COM AJUSTE (texto) |
| L2-R38 | 2.2 | E [TS] | CONFERE | TS | n | APROVADO COM AJUSTE (aderência PARCIAL) · PEND. NORM. |
| L2-R39 | 2.2 | C [TS esp.] | CONFERE | PC | n | APROVADO COM AJUSTE (aderência PARCIAL) · PEND. NORM. |
| L2-R40 | 2.2 | E [TS] | literal confere; base inadmissível | SH | S | **REPROVADO** |
| L2-R41 | 2.2 | E [TS] | CONFERE | TS | n | APROVADO COM AJUSTE (aderência PARCIAL) · PEND. NORM. |
| L2-R42 | 2.2 | E [TS] | CONFERE | PC | n | APROVADO COM AJUSTE (aderência PARCIAL) · PEND. NORM. |
| L2-R43 | 2.2 | C | CONFERE | AP | n | APROVADO COM AJUSTE (texto: AP) |
| L2-R44 | 2.2 | C | CONFERE | AP | n | APROVADO COM AJUSTE (texto: AP) |
| L2-R45 | 2.2 | C [TS esp.] | CONFERE | SH | n | APROVADO · PEND. NORM. (PARCIAL já declarada) |
| L2-R46 | 2.2 | E [TS] | CONFERE | NP | n | APROVADO · PEND. NORM. (PARCIAL já declarada) |

**Reprovados: 3/28 = 10,7%** (R23, R24, R40). Gate de 30%: não acionado.

### Motivos e textos exatos

**L2-R23, L2-R24, L2-R40 — REPROVADO.** Base inadmissível (seção 2.1): documento de 2009 de unidade extinta, com estrutura superada pelo Ato nº 251/2026; o item ou afirma fato atual sem base vigente, ou cobra documento histórico fora do edital; VOLÁTIL incoerente. Adicional R24: vizinho do L2-Q04 (texto sem revisão não é registro oficial / não se publica). Substitutos: aderência direta (2.1: R23 e R24; 2.2: R40), sem TS em 2.1 se a folha passar de 6/20, gabarito livre (a parte fica em 40–60% de C com qualquer combinação). Para indexação há base vigente (Ato 251, art. 7º, V), mas o tema é 3.1, não 2.2.

**L2-R20 — AJUSTE (texto).** O enunciado de duas frases se autocontradiz ("atribui ao Derep a garantia…" / "Entretanto, … é da ferramenta"), e o "Entretanto" entrega o E; "ferramenta" responsável é distrator implausível. Texto exato:
"Segundo o Ato da Mesa nº 251/2026, independentemente do apoio de ferramenta automática na produção do texto do registro oficial, a responsabilidade pela veracidade, pela integridade e pela autenticidade desse registro é do fornecedor da ferramenta, e não do Derep (antigo DETAQ)."
Gabarito E [TS] mantido; na justificativa, "A troca é do responsável (Derep → fornecedor da ferramenta)."

**L2-R33 — AJUSTE (texto).** "independentemente de seu desempenho" não está na fonte (que, ao contrário, liga a supervisão a "situations when the AI model does not perform as required"); é um segundo ponto discutível num E com [TS] de troca única. Texto exato:
"Segundo a nota de transparência do Azure Speech, manter o ser humano no circuito (human-in-the-loop) inclui assegurar supervisão humana constante do recurso de IA e preservar o papel do modelo, e não o das pessoas, na tomada de decisão."

**L2-R35 — AJUSTE (texto; aderência PARCIAL).** "limitação permanente … e por isso recomenda que o usuário possa tentar de novo" é incoerente por construção (permanente → nova tentativa) e entrega o E. Texto exato:
"A nota de transparência do Azure Speech associa o erro de reconhecimento causado por fala rápida, fala pouco clara ou pausa longa a uma limitação permanente do modelo, e não a um problema temporário."
Justificativa: retirar "A recomendação de nova tentativa está correta." Ponto no mapa: "O erro por fala rápida, fala pouco clara ou pausa longa é associado a problema temporário, e não a limitação permanente do modelo". Aderência PARCIAL (UX de comando de voz; tema de 1.1/1.6, não de fluxo de degravação).

**L2-R36 — AJUSTE (texto: formato AP sem elemento parlamentar).** Texto exato: "Depois de implantar um recurso de transcrição apoiado em IA nas reuniões de comissão da Câmara dos Deputados, a nota de transparência do Azure Speech recomenda oferecer um canal pelo qual usuários e pessoas afetadas relatem problemas, pois o recurso exige monitoramento e melhoria contínuos, ainda que tenha sido testado antes da implantação."

**L2-R43 — AJUSTE (texto: AP).** Texto exato: "Para avaliar o desempenho do reconhecimento de fala usado na transcrição das sessões plenárias da Câmara dos Deputados, a nota de transparência do Azure Speech recomenda que o conjunto de teste seja composto por entradas de voz reais coletadas na própria aplicação em produção, amostradas aleatoriamente ao longo de um período e atualizado periodicamente." Registro: conferido contra a parte D (2.7): sem gêmeo (R114 = análise da distribuição de erros; R116 = melhoria em todos os cenários).

**L2-R44 — AJUSTE (texto: AP).** Texto exato: "Antes de enviar a gravação de uma audiência pública de comissão da Câmara dos Deputados ao Google Cloud Speech-to-Text, a equipe pode ouvir trechos do áudio, que, segundo as boas práticas do serviço, deve soar claro, sem distorção nem ruído inesperado."

**L2-R37 — AJUSTE (texto).** A SH com equipe genérica sugere adoção de serviço fechado a novos clientes. Texto exato: "Uma equipe que já utiliza o Amazon Augmented AI (A2I) deseja que revisores humanos examinem as previsões de um modelo quando ele não alcançar alta confiança e que auditem, ainda, amostras aleatórias dessas previsões. Segundo a documentação do serviço, o A2I permite obter revisão humana tanto de previsões de baixa confiança quanto de amostras aleatórias de previsões." VOLÁTIL (baixo) e REVERIFICAR mantidos.

**L2-R31 — AJUSTE ([TS] retirado; aderência PARCIAL).** Nada no enunciado parece trocado ("primária, íntegra e autêntica" é a letra do inciso); "espelho" sem troca aparente infla a contagem. Gabarito: "L2-R31. C." Aderência PARCIAL (missão institucional do Derep).

**Aderência PARCIAL (D-ADERENCIA; só simulado diagnóstico) — R19, R21, R22, R25, R27, R28, R31, R32, R35, R38, R39, R41, R42**, a acrescentar às já declaradas R29, R45, R46. Motivos: R19, R28 — forma de publicação no Diário/ata (precedente L2-R02); R21, R22, R32, R38, R39, R41, R42 — ponto é a competência entre órgãos e coordenações (contexto institucional, como R29/R45/R46); R31 — missão institucional; R25 — vocabulário do Banco de Discursos (tema de 2.4/3.2; mesma página do L2-R07, 2.4); R27 — advertência de uso em alto risco (tema de 4.2/1.8; irmão do L1-R37 e do L1-R124); R35 — acima. Texto exato no mapa e no (d-G): "PARCIAL (<motivo>; D-ADERENCIA: só simulado diagnóstico)".

**Aprovados sem ajuste de texto:** R26, R29, R30, R34, R45, R46 (e R19, R21, R22, R25, R27, R28, R32, R38, R39, R41, R42 só com o ajuste de aderência). Todos os E têm exatamente um conceito trocado (R19 canal; R20 responsável; R21, R29, R38, R41 órgão/coordenação; R25 inversão de termos, precedente L2-Q01; R28 extenso → sinopse; R33 humanos → modelo, após ajuste; R35 temporário → permanente, após ajuste; R42 subsidiária → exclusiva; R46 quatro → três).

## 4. Contagens (v1 → após esta R1, sem os 3 substitutos)

- Gabarito: 14 C / 14 E → 13 C / 12 E (52%); por folha 2.1 6/6, 2.2 7/6. Qualquer combinação dos 3 substitutos mantém a parte entre 40% e 60%.
- [TS]: 19 → 16 (sem R23, R40 e o espelho de R31), de 25.
- VOLÁTIL: 5 → 2 (R25, R37); 2.1 1/18, 2.2 1/19; nenhum alto.
- Formatos: 2.1 SH 4, TS 5, PC 3, D 4, AP 2 (18); 2.2 SH 4, TS 4, PC 4, AP 4, D 2, NP 1 (19).
- Aderência: 2.1 — diretas 8 (Q01–Q04, R01, R20, R26, R30), PARCIAIS 10 (R02, R19, R21, R22, R25, R27, R28, R29, R31, R32); 2.2 — diretas 12 (Q05–Q08, R03, R04, R33, R34, R36, R37, R43, R44), PARCIAIS 7 (R35, R38, R39, R41, R42, R45, R46).
- Ponto único: nenhum duplicado na folha; varredura do pacote v1.9 e da onda 2 sem gêmeo (sem "Errata", "Ato da Mesa", "Derep", "A2I", "alto risco", "temporário", "silêncio" em item do pacote); proximidades declaradas pela produtora conferidas e aceitas; sem gêmeo com C_v1 e D_v1 (R43 × R114/R116 distintos; R26 × R103/R115 distintos, vizinhança já declarada pela parte D; R37, R34, R36 sem par); parte B ainda não existe.
- Estilo: recomendação 2 do estilo_onda_2 (concessiva também em E) não cumprida ("ainda que" só em C: R24, R36); registro, sem reprovação.

## 5. Ressalvas à Gerência (D1 da gce-gerencia)

1. **Concentração institucional na 2.1:** 10 de 18 itens com aderência PARCIAL; 12 dos 28 itens da parte vêm de um único Ato. Recomendação, por analogia ao registro da T-90 para a 2.7: os 2 substitutos da 2.1 e o da 2.2 com aderência direta (a 2.1 fecha então com 10 diretas em 20); a Gerência decide se troca mais algum item institucional.
2. PENDENTE NORMATIVO nos 14 itens normativos até o registro do qa-normativo.
3. Gêmeos entre folhas: contra C_v1 e D_v1, nenhum; contra a parte B (2.3/2.4; Ato 251 art. 2º IV e 6º V; página "Como pesquisar" × R25), a conferir quando ela existir.

## 6. Veredito geral

**APROVADO COM RESSALVAS — 3/28 reprovados (10,7%)**; 8 ajustes de texto ou marca (R20, R31, R33, R35, R36, R37, R43, R44) + reclassificação de aderência em 13 itens; 14 PENDENTE NORMATIVO. Para a v2: substituir R23, R24, R40; aplicar os textos exatos acima; reclassificar aderência; levar os 14 itens normativos ao qa-normativo. Todos os itens continuam QA PENDENTE até a R2 e a reconciliação (D-QA-PENDENTE).
