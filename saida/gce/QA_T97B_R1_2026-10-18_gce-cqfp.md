# QA_T97B_R1_2026-10-18_gce-cqfp.md — T-97 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L2_reforco_onda3_B_v1.md (gce-cpp; 28 itens AUTORAL L2-R47 a L2-R74; P2-2.3 = R47–R60, P2-2.4 = R61–R74). Rodada R1 (de no máximo 2). Revisora: gce-cqfp (opus; não produziu). Ciclo 2026-10-18 s12c4. Nada foi reescrito no objeto; sem commit.
Lido: TAREFAS.md (T-97); DECISOES.md (D-REFORCO-1/2, D-FONTE-DATA-ANTERIOR, D-T89-R1-ACEITE, D-T96-ONDA2-ACEITE seção II, D-ONDA3-FILA, D-ADERENCIA); T90_reconciliacao (seção 4: legado de D em 2.4 e diluição; seção 1 e QA_T90_R1: norma não dirigida a transcrição = REPROVADO); T96_reconciliacao (seção 4); saida/banco/estilo_onda_2.md (seção 5); edital/modulo_RF_IA_P2.md (2.3 "Revisão e edição de transcrições: critérios de qualidade e fidelidade"; 2.4 "Formatação de transcrições parlamentares: identificação de oradores, marcação de pausa ruído, etc."; o RICD não consta de nenhum módulo do edital em edital/); pacote.json v1.9 (334 itens, varredura por script, python -I); L2_reforco_onda1_v3; L3_reforco_onda1_v3; finais da onda 2; onda 3: A_v2, C_v2 (versões mais recentes em disco), D_v1; QA_T97A_R1 e QA_T97C_R1 (critérios de aderência desta coordenação); QA_T97B_normativo (qa-normativo, gravado em paralelo: 19/19 CONFERE).

## 1. Evidência: todas as bases reabertas por esta coordenação em 18/10/2026 (curl com User-Agent de navegador; todas HTTP 200)

| fonte | resultado | itens |
|---|---|---|
| Legin, RICD (norma atualizada) | literal CONFERE: art. 17, I, "h" e "l"; 66, I e II; 73, XI e XIII; 74, I, IV–VII; 75, caput, I e II; 80, § 1º; 82, § 2º; 93, §§ 2º e 4º; 95, § 5º; 98, caput e §§ 2º, 3º, 6º, 7º; 176, §§ 1º, 2º (I, III), 4º. Notas: art. 98, § 3º, continua "em caso de indeferimento, poderá este recorrer ao Plenário"; art. 80, § 1º: o Presidente considera a declaração procedente ou não, "cabendo recurso ao Plenário" | R47–R55, R62–R65, R67, R70–R74 |
| Câmara, "Como pesquisar" | literal CONFERE ("Tipo Fala: selecione a natureza do discurso: "Discurso", "Fala do Presidente" ou "Questão de Ordem""; "Fala do Presidente: marque a caixa…"; "Fase: A sessão plenárias, de acordo com o tipo, está dividida por fases, caracterizando o tempo disponível para fala dos deputados e o tipo de discussão…") | R61, R66 |
| learn.microsoft.com …/how-to-custom-speech-evaluate-data | "Last updated on 2025-12-29"; ms.date 2025-12-19; "A WER of 5-10% is considered good quality… A WER of 20% is acceptable, but you might want to consider more training. A WER of 30% or more signals poor quality and requires customization and training." e "In the Microsoft Foundry portal and Speech Studio, the quotient is multiplied by 100… The Speech CLI and REST API results aren't multiplied by 100." CONFEREM | R56, R60 |
| learn.microsoft.com …/captioning-concepts | "Last updated on 2026-02-25"; "The duration in ticks doesn't include trailing or leading silence." CONFERE | R68 |
| cloud.google.com …/rest/v1/RecognitionConfig → docs.cloud.google.com (destino 200) | "Last updated 2025-10-23 UTC"; profanityFilter: "replacing all but the initial character in each filtered word with asterisks, e.g. "f***"" CONFERE | R57 |
| docs.aws.amazon.com …/pii-redaction.html | sem data visível; "your media is the only place where the complete conversation is stored. If you delete your original media, there is no record of the unredacted PII." e "may not identify and remove all instances… We strongly recommend that you review any redacted output" CONFEREM | R58, R59 |
| docs.aws.amazon.com …/subtitles.html | sem data visível; "Subtitles are displayed at the same time text is spoken, and remain visible until there is a natural pause or the speaker finishes talking." CONFERE | R69 |

Base não reaberta: nenhuma. Base de data anterior: nenhuma (D-FONTE-DATA-ANTERIOR não acionada; correto). Base em código: nenhuma. Documento de unidade extinta: nenhum (a página "Como pesquisar" usa o nome anterior do departamento, mas é página viva do portal e descreve o sistema atual; os itens não nomeiam o órgão — correto).

## 2. Critério de escopo desta R1 (o mesmo das partes A e C, aplicado ao RICD)

- O RICD não é conteúdo autônomo de P2. Item com base no RICD é admissível em 2.3/2.4 quando o ponto julgado diz respeito ao registro, à publicação, à edição ou à rotulagem do texto da sessão (precedentes canônicos L2-R05, 2.3; L2-R08, 2.4; L3-R01, 3.1). Direta quando o ponto é critério de revisão/edição (2.3) ou de formatação/identificação (2.4); PARCIAL quando o ponto é competência, prazo, recurso ou regime de publicação/ata (precedente QA_T97A_R1, 2.3: "qual órgão faz X" = PARCIAL).
- REPROVADO quando o ponto é regra de condução da sessão sem efeito sobre o texto registrado (uso da palavra, duração de fase, interrupção, tratamento entre Deputados): é norma não dirigida a transcrição na folha (precedente QA_T90_R1, R09–R11), e a moldura "o revisor deve considerar" não muda o ponto julgado. A matéria é de vocabulário/regimento (2.8, parte D, já com 20) — relocação é D1 da Gerência, não desta QA.

## 3. Veredito por item

| id | fl. | gab. | base | formato | VOL | aderência (após R1) | veredito |
|---|---|---|---|---|---|---|---|
| L2-R47 | 2.3 | E [TS] | CONFERE | TS | n | PARCIAL | APROVADO COM AJUSTE (aderência) · PEND. NORM. |
| L2-R48 | 2.3 | C [TS esp.] | CONFERE | SH | n | direta | AJUSTAR (texto) · PEND. NORM. |
| L2-R49 | 2.3 | C | CONFERE | SH | n | direta | APROVADO · PEND. NORM. |
| L2-R50 | 2.3 | E [TS] | CONFERE | TS | n | PARCIAL | APROVADO COM AJUSTE (aderência) · PEND. NORM. |
| L2-R51 | 2.3 | E [TS] | CONFERE | TS | n | PARCIAL (declarada) | APROVADO · PEND. NORM. |
| L2-R52 | 2.3 | E [TS] | CONFERE | PC | n | PARCIAL (declarada) | APROVADO · PEND. NORM. |
| L2-R53 | 2.3 | E [TS] | CONFERE | AP | n | PARCIAL | APROVADO COM AJUSTE (aderência) · PEND. NORM. |
| L2-R54 | 2.3 | C | CONFERE | D | n | PARCIAL (declarada) | APROVADO · PEND. NORM. |
| L2-R55 | 2.3 | C | CONFERE | PC | n | PARCIAL | AJUSTAR (justificativa; aderência) · PEND. NORM. |
| L2-R56 | 2.3 | E [TS] | CONFERE | NP | S médio | direta | APROVADO |
| L2-R57 | 2.3 | C | CONFERE | AP | S baixo | direta | APROVADO |
| L2-R58 | 2.3 | C [TS esp.] | CONFERE | SH | n | PARCIAL | APROVADO COM AJUSTE (aderência) |
| L2-R59 | 2.3 | E [TS] | CONFERE | D→SH | n | PARCIAL | APROVADO COM AJUSTE (formato; aderência) |
| L2-R60 | 2.3 | C | CONFERE | NP | S baixo | PARCIAL | APROVADO COM AJUSTE (aderência) |
| L2-R61 | 2.4 | C | CONFERE | PC | S baixo | PARCIAL | APROVADO COM AJUSTE (aderência) |
| L2-R62 | 2.4 | E [TS] | CONFERE | AP | n | — | **REPROVADO** · PEND. NORM. |
| L2-R63 | 2.4 | E [TS] | CONFERE | TS | n | PARCIAL | APROVADO COM AJUSTE (aderência) · PEND. NORM. |
| L2-R64 | 2.4 | E [TS] | CONFERE | TS | n | PARCIAL | AJUSTAR (texto; aderência) · PEND. NORM. |
| L2-R65 | 2.4 | E [TS] | CONFERE | NP | n | PARCIAL | APROVADO COM AJUSTE (aderência) · PEND. NORM. |
| L2-R66 | 2.4 | C | CONFERE | AP | S baixo | PARCIAL | APROVADO COM AJUSTE (aderência) |
| L2-R67 | 2.4 | E [TS] | CONFERE | NP | n | — | **REPROVADO** · PEND. NORM. |
| L2-R68 | 2.4 | E [TS] | CONFERE | PC | n | direta | APROVADO |
| L2-R69 | 2.4 | C | CONFERE | SH | n | PARCIAL | APROVADO COM AJUSTE (aderência) |
| L2-R70 | 2.4 | C [TS esp.] | CONFERE | PC | n | — | **REPROVADO** · PEND. NORM. |
| L2-R71 | 2.4 | E [TS] | CONFERE | TS | n | PARCIAL (declarada) | APROVADO · PEND. NORM. |
| L2-R72 | 2.4 | C | CONFERE | SH | n | — | **REPROVADO** · PEND. NORM. |
| L2-R73 | 2.4 | C [TS esp.] | CONFERE | SH | n | — | **REPROVADO** · PEND. NORM. |
| L2-R74 | 2.4 | C | CONFERE | AP | n | — | **REPROVADO** · PEND. NORM. |

**Reprovados: 6/28 = 21,4%** (R62, R67, R70, R72, R73, R74, todos em 2.4). Gate de 30%: não acionado. Nenhum gabarito errado; todos os gabaritos conferem com a base literal.

### Motivos e textos

**R62, R67, R70, R72, R73, R74 — REPROVADO (extrapolação da folha; seção 2).** O ponto é regra de condução da sessão sem efeito sobre o registro: R62 (hipóteses em que o Deputado pode falar, art. 74), R73 (palavra "a juízo do Presidente", art. 74, VII), R67 (duração do Grande Expediente, art. 66; vizinho de D-R128, duração das breves comunicações), R70 (quem pode interromper o orador, art. 73, XIII), R72 (interrupção do orador para a votação, art. 82, § 2º), R74 (tratamento entre Deputados, art. 73, XI; a regra é de conduta do orador, não de identificação de oradores na transcrição — discordo da PARCIAL declarada). R70 e R74 não têm sequer moldura de transcrição; R62 e R67 têm moldura artificial ("Ao classificar…", "Na marcação das fases…"). Substitutos (6, em 2.4): aderência direta (identificação de oradores, marcação de pausa, ruído, eventos não falados), base oficial aberta na data, conferidos contra 1.4 (diarização) e contra L2-Q13–Q16, R07, R08 e C-R95 (travessões por falante); preferir SH, NP, AP e TS (folha sem os 6: D 2, TS 4, SH 2, NP 1, PC 3, AP 2); D nova é admissível pela diluição da T90, seção 4 (folha já com mais de 7), mas não necessária; no máximo 1 VOLÁTIL (2.4 fica em 3/20 sem os substitutos); 4 C e 2 E para devolver a 2.4 a 7/7; ao menos 2 com [TS].

**R48 — AJUSTAR (texto).** "apartea" é forma inexistente (apartear → "aparteia"). Texto exato: "Um Deputado aparteia o orador sem solicitar nem obter a permissão deste. Nessa situação, o aparte, por ter sido proferido em desacordo com o Regimento Interno da Câmara dos Deputados, não será publicado."

**R55 — AJUSTAR (justificativa; aderência PARCIAL).** O C está correto (art. 17, I, "l"), mas a justificativa diz que "a pegadinha seria atribuir a autorização a outro órgão": o art. 98, § 3º (base do vizinho R64), dá à **Mesa** a autorização da publicação integral dos documentos não lidos. Uma contraparte "compete à Mesa autorizar…" seria defensável. Texto exato da segunda frase da justificativa: "O item repete o dispositivo. Registro: para documentos não lidos integralmente pelo Deputado, a publicação integral depende de autorização da Mesa, a requerimento do orador (art. 98, § 3º; ver L2-R64); os dois itens não devem figurar no mesmo simulado." Aderência PARCIAL (competência; ata).

**R64 — AJUSTAR (texto; aderência PARCIAL).** Ressalva do qa-normativo acolhida: "documentos de representante de outro Poder" restringe a leitura ambígua do § 3º. Texto exato: "Segundo o Regimento Interno da Câmara dos Deputados, ainda que não tenham sido integralmente lidos pelo Deputado durante o discurso, as informações e documentos ou discursos de representantes de outro Poder são publicados na íntegra na ata, sem necessidade de autorização da Mesa." Gabarito E [TS] mantido.

**R59 — AJUSTE de formato.** Construção "Uma equipe ativa… Nessa situação…" é SH, não D. Reclassificar SH (2.3: D 2, SH 5 = 25%; teto cumprido).

**Aderência PARCIAL (D-ADERENCIA; só simulado diagnóstico), 13 itens, a acrescentar às 4 declaradas que subsistem (R51, R52, R54, R71; a quinta, R74, foi reprovada):** R47 (o ponto é o destinatário do recurso), R50 e R55 (competência), R53 e R65 (regime do discurso escrito, não transcrição), R63 (admissibilidade do aparte; vínculo ao registro só pelo § 4º), R64 (o que consta da ata; fronteira 3.3, como R54), R58 e R59 (ocultação de dados pessoais: tema de 4.1/4.3; a revisão da saída é só a consequência), R60 (escala de apresentação do WER por interface; o critério de qualidade é o WER, já em L2-R06), R61 e R66 (campo de pesquisa do Banco de Discursos: tema de 3.2; precedente A-R25), R69 (regra de exibição da legenda: tema de 1.7/2.6; mesma página de C-R94/R102, PARCIAIS). Texto: "PARCIAL (<motivo>; D-ADERENCIA: só simulado diagnóstico)".

**Aprovados sem ajuste de texto:** R49, R51, R52, R54, R56, R57, R68, R71 (e os de ajuste só de aderência/formato). Observações sem efeito: R51 — a brecha do recurso ao Plenário (art. 80, § 1º) não muda o E, porque o § 7º fixa a decisão no Presidente; R54 e R66 — C de baixa discriminação (estilo_onda_2, rec. 7); R57 — "ainda que tenham sido pronunciadas pelo orador" é concessiva vazia (toda palavra filtrada foi pronunciada); pode sair sem mudar o gabarito; R56 — vizinho de L1-R128 (1.8: WER alto → treinar modelo), ponto distinto (patamar numérico).

## 4. Conferências da parte

- **[TS]:** 18/28 CONFERE; cada E troca exatamente um conceito (R47 Plenário→Mesa; R50 Presidente→Mesa Diretora; R51 Presidente→Plenário; R52 uma→cinco sessões; R53 devolução→cortes; R56 aceitável→má; R59 pode não→todas; R62 exclui reclamação; R63 inadmite→admite; R64 indicação→íntegra sem autorização; R65 três→cinco; R67 50→60; R68 não inclui→abrange; R71 Câmara→Presidente); espelhos R48, R58, R70, R73 coerentes (O-6). Após R1: 14/22; os 6 substitutos precisam de ≥2 [TS] para chegar a 16/28.
- **Gabarito:** v1 14 C / 14 E (50%); 2.3 7/7, 2.4 7/7. Após R1: 10 C / 12 E em 22 (45,5%); 2.4 com 3 C / 5 E; com 4 C + 2 E nos substitutos, 14/14.
- **VOLÁTIL:** 5 CONFEREM com o critério da D-T96-ONDA2-ACEITE: R56 médio (a, faixa numérica de orientação), R57 e R60 (b), R61 e R66 (c, organização de recurso do portal, como L2-R07). R58, R59, R68, R69 não VOLÁTEIS (funcionamento documentado de recurso central): correto. Por folha: 2.3 3/20; 2.4 3/20. Risco alto: 0. Os 5 inaptos a simulado final até 4–8/1/2027; os demais na conferência de base de janeiro.
- **Ponto único e vizinhanças:** nenhuma duplicata na folha nem gêmeo no pacote v1.9 (busca própria: profan, ocult, PII, WER de, lauda, secreta, decoro, retifica, Tipo Fala, silêncio, pausa natural, outro Poder, inteiro teor; acertos só em itens alheios) nem em A_v2, C_v2 e D_v1. Vizinhanças declaradas conferidas e distintas: R68 × C-R90/R92 (offset em ticks e marco zero × duração sem silêncio); R69 × C-R94/R95/R102 (índice, travessões, arquivo regular × permanência da legenda); R55 × R64 (ver ajuste de R55); R53 × R65 (art. 75, incisos II e I). Novas: R67 × D-R128 (reprovado); R56 × L1-R128; R61/R66 × A-R25 e L2-R07 (mesma página: 2.4 ficaria com 3 itens de "Como pesquisar").
- **Formato e tetos:** declarados conferem (maior 20% em cada folha; nenhuma D nova em 2.4 — legado respeitado). Após R1: 2.3 D 2, TS 4, SH 5, NP 3, PC 3, AP 3; 2.4 (14) D 2, TS 4, SH 2, NP 1, PC 3, AP 2.
- **Estilo (estilo_onda_2, rec. 1–7):** "independentemente" em E (R53) CONFERE; concessiva em C (R57) e E (R64) CONFERE; "Segundo" abre 3/28 CONFERE; sem absolutos empilhados; fonte nomeada. Observação: moldura formular "o revisor deve considerar/ter em conta que" em 7 enunciados (R50, R54, R55, R62, R63, R67, R68) — repetição de forma, sem pista de gabarito; variar nos substitutos. Extensão: C 33–52 e E 35–54 palavras, sem pista.
- **Estrutura:** linha 1 no formato; PARTE 1/3–3/3, FIM DA PARTE e FIM DO LOTE presentes; Parte 2 com 28 ids, sem gabarito, [TS], VOLÁTIL ou REVERIFICAR; Parte 3 com os mesmos 28 ids, na mesma ordem (script). CONFERE.
- **Normativo:** 19 itens com base no RICD (R47–R55, R62–R65, R67, R70–R74) marcados PENDENTE NORMATIVO, conforme a instrução. O QA_T97B_normativo_2026-10-18_qa-normativo.md já registra 19/19 CONFERE; a retirada da marca é ato da Gerência na reconciliação. A conferência literal desta coordenação também dá CONFERE nos 19.

## 5. Veredito geral

**APROVADO COM RESSALVAS — 6/28 reprovados (21,4%)**, todos em 2.4 e pelo mesmo motivo (regra de condução da sessão sem efeito sobre o registro). Ajustes de texto em 3 itens (R48, R55 na justificativa, R64), 1 de formato (R59) e aderência PARCIAL em mais 13 itens (total de 17 PARCIAIS entre os 22 que ficam). Ressalva à Gerência (D1): 2.3 fica com 10 diretas em 20 e 2.4 com 7 diretas em 14 (6 canônicos + R68); os 6 substitutos de 2.4 devem ser diretos, e a Gerência decide se troca mais algum item PARCIAL. Todos os itens seguem QA PENDENTE até a R2 e a reconciliação (D-QA-PENDENTE).
