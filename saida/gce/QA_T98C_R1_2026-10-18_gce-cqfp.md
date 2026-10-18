# QA_T98C_R1_2026-10-18_gce-cqfp.md — T-98 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L3_reforco_onda4_C_v1.md (gce-cpp), 28 itens AUTORAL L3-R68 a L3-R95 (P2-4.2: R68–R81; P2-4.3: R82–R95). Rodada R1. Revisão; nada foi reescrito no objeto. Ciclo 2026-10-18 s13c2.
Lidos: TAREFAS.md (T-98); DECISOES.md (D-REFORCO-1/2, D-FONTE-DATA-ANTERIOR, D-T89-R1-ACEITE, D-T96-ONDA2-ACEITE (II), D-T97-ONDA3-ACEITE, D-T97-META-FUNDADOR-RESP, D-ADERENCIA, D-LEI-15352); T91_reconciliacao (3.1–3.3); T96_reconciliacao (seção 4); T97_reconciliacao (3.4, 4, 6); estilo_onda_3 (seção 5); edital/modulo_RF_IA_P2.md (4.2 e 4.3); pacote.json v1.10 (560 itens; P2-4.1 com 26, 4.2 com 6, 4.3 com 6); saida/gcb/D6_v2_1.md; partes A (v1) e B (v2) da onda 4; finais das ondas 1–3.

## 1. Evidência — bases reabertas por esta QA em 18/10/2026 (curl, User-Agent de navegador; texto extraído e conferido por grep)

| base | HTTP | o que encontrei |
|---|---|---|
| planalto.gov.br/ccivil_03/leis/l9610.htm | 200 | arts. 5º, VI; 7º, XIII e § 2º; 5º, VIII, "h"; 11; 14; 17 caput e § 2º; 18; 19; 24, § 2º; 37; 41; 43; 47; 49, III e V conferem com as justificativas, SALVO a citação do art. 14 no (d-G) do R76 (ver R76) |
| planalto.gov.br/.../l13709compilado.htm | 200 | arts. 44 (caput, III, par. único); 46, § 1º; 48, §§ 2º, I, e 3º; 49; 50, § 2º, I, "g" conferem. Art. 50, caput, lido por esta QA: controladores e operadores "poderão formular regras de boas práticas... que estabeleçam... as normas de segurança, os padrões técnicos..." (relevante para R92). Arts. 55-A ss. com "Agência Nacional de Proteção de Dados" (Lei 15.352/2026; D-LEI-15352) |
| docs.aws.amazon.com/transcribe/latest/dg/data-protection.html | 200 | "shared responsibility model", "set up individual users... only the permissions necessary", "We strongly recommend that you never put confidential or sensitive information... into tags or free-form text fields such as a Name field... may be used for billing or diagnostic logs" — conferem (R85, R87, R93) |
| docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html | 200 | "may not identify and remove all instances of sensitive data... We strongly recommend that you review any redacted output" — confere (R95) |
| docs.cloud.google.com/gemini-enterprise-agent-platform/models/responsible-ai | 200 | "Mitigate risks from rendered model output (Markdown and HTML)... you may be vulnerable to indirect prompt injection and data exfiltration... Sanitize output" — confere (R89). Rodapé "Last updated 2026-10-15 UTC" (não registrado na proveniência) |
| docs.cloud.google.com/speech-to-text/docs/v1/data-logging | 200 | "Caution Your logged data is not deleted when you delete your project. Fill out the deletion request form" — confere (R94). Rodapé 2026-10-13 confere |
| learn.microsoft.com/.../speech-to-text/transparency-note | 200 | "Customer feedback loop..." e "without conscious effort... vary across groups..." — conferem (R80, R81). Rodapé 2026-03-31 confere |
| learn.microsoft.com/.../speech-to-text/data-privacy-security | 200 | tempo real "processed only on the Azure's server memory, and no data is stored at rest"; lote "The customer controls the storage... including the retention" — confere (R91). Rodapé "Last updated on 2026-08-26" (não registrado) |

Todas as 8 bases citadas foram reabertas; nenhuma base deixou de ser reaberta. Nenhuma usa data anterior (D-FONTE-DATA-ANTERIOR não incide). Legin não é usado.

## 2. Ponto único e gêmeos (grep e script próprio, python3 -I, somente leitura)
Método: (a) busca por termos-chave de cada ponto em pacote.json v1.10 (enunciado + justificativa), nos finais saida/gce/*reforco* e no D6_v2_1.md; (b) maior sequência literal de palavras e índice de Jaccard de cada enunciado contra os 560 enunciados e as partes A e B. O script da produção (só sequência literal) não pega paráfrase: os dois gêmeos abaixo têm sequência literal ≤ 8 palavras, mas Jaccard 0,40 e 0,32, os maiores da parte.
- **R80 × L2-R36 (P2-2.2, canônico v1.10): GÊMEO não declarado.** Mesmo trecho-base ("Customer feedback loop"), mesmo ponto (canal de relato depois da implantação + monitoramento e melhoria contínuos), mesmo gabarito (C), mesma moldura ("depois de implantar recurso de transcrição... Câmara dos Deputados... canal... usuários e afetados"). A produção declarou vizinhança só com L2-R35, R40 e R43. Pela T96_reconciliacao, seção 4, gêmeo em outra folha "só entra declarado e com ângulo próprio da folha"; aqui não há declaração nem ângulo de 4.2 (direito autoral ou ética de conteúdo gerado).
- **R95 × L2-R59 (P2-2.3, canônico v1.10): GÊMEO não declarado.** Mesmo trecho-base da pii-redaction ("may not identify and remove all instances... review any redacted output"), mesmo ponto, gabarito espelho (C × E). A produção declarou só L2-R58 (outro ponto da mesma página). Sem ângulo próprio da 4.3 além do já julgado.
- R81 × L1-R98 (P2-1.6): mesmo juízo de fundo (desempenho não uniforme entre grupos; avaliação de um grupo não dispensa os demais), fontes distintas (Azure TN "Fairness considerations" × model card do Whisper, sotaques), mesma construção de E ("uniforme... dispensa"). O ângulo de 4.2 (equidade/ética) é próprio; aceito como vizinhança, mas a declaração da produção ("itens de sotaque da 1.6... fator de erro") não descreve o L1-R98, que é exatamente "uniforme... dispensa testes". Registrar o par para a GBQ (não figurar no mesmo simulado).
- Demais 25: nenhum gêmeo. LGPD (R82–R92) contra a P2-4.1 (26 itens), D6 (itens D6-nn) e Lote 4: nenhum ponto repetido; o D6 traz art. 50 e o plano de resposta a incidentes só no curso (linhas 361–362), não em item. Vizinhanças declaradas na seção 1.3 conferidas e aceitas.

## 3. Veredito por item
Marca normativa: os 19 itens de lei federal (R68–R79 na Lei 9.610/1998; R82, R83, R84, R86, R88, R90, R92 na LGPD) ficam **PENDENTE NORMATIVO** até a conferência do qa-normativo (em paralelo). Meu exame literal está registrado, mas não substitui o dele.

| id | folha | gab. | [TS] | veredito | motivo |
|---|---|---|---|---|---|
| L3-R68 | 4.2 | C | — | APROVADO · PENDENTE NORMATIVO | art. 11 e par. único literais |
| L3-R69 | 4.2 | E | TS | APROVADO · PENDENTE NORMATIVO | art. 5º, VI ("permanente ou temporário"); troca única |
| L3-R70 | 4.2 | E | TS | APROVADO · PENDENTE NORMATIVO | art. 43 (primeira publicação × falecimento); troca única; vizinho de R09 declarado |
| L3-R71 | 4.2 | C | — | APROVADO · PENDENTE NORMATIVO | art. 49, III literal |
| L3-R72 | 4.2 | E | TS | APROVADO · PENDENTE NORMATIVO | art. 24, § 2º (Estado × sucessores); troca única |
| L3-R73 | 4.2 | E | TS | APROVADO (ressalva) · PENDENTE NORMATIVO | art. 17, § 2º; troca única. Ressalva: "coletânea de estudos" pode ser lida como compilação (art. 7º, XIII) e não obra coletiva (art. 5º, VIII, "h", exige fusão das contribuições); o E resiste nas duas leituras, mas dizer "obra coletiva" no enunciado tiraria a margem de recurso (D1 da Gerência; opcional) |
| L3-R74 | 4.2 | C | — | APROVADO · PENDENTE NORMATIVO | arts. 18 e 19 |
| L3-R75 | 4.2 | E | TS | APROVADO · PENDENTE NORMATIVO | art. 37; a consequência deriva da única troca |
| L3-R76 | 4.2 | C | TS esp. | AJUSTAR (só registro do (d-G)) · PENDENTE NORMATIVO | enunciado e gabarito corretos; a justificativa cita entre aspas "não podendo, porém, opor-se", mas o texto compilado é "não podendo opor-se a outra adaptação, arranjo, orquestração ou tradução, salvo se for cópia da sua" — base literal errada; corrigir a citação |
| L3-R77 | 4.2 | C | TS esp. | APROVADO · PENDENTE NORMATIVO | art. 49, V; contrato de 1999 já sob a Lei 9.610 |
| L3-R78 | 4.2 | E | TS | APROVADO · PENDENTE NORMATIVO | art. 7º, XIII e § 2º; troca única |
| L3-R79 | 4.2 | C | — | APROVADO · PENDENTE NORMATIVO | art. 47 literal |
| L3-R80 | 4.2 | C | — | **REPROVADO** | gêmeo não declarado de L2-R36 (seção 2); além disso, aderência à 4.2 fraca (canal de feedback não é direito autoral nem ética de conteúdo gerado) e cenário decorativo ("como nas sessões") |
| L3-R81 | 4.2 | E | TS | APROVADO (ressalva) | TN "Fairness considerations" confere; troca única; registrar o par com L1-R98 (seção 2) e corrigir a vizinhança declarada |
| L3-R82 | 4.3 | E | TS | APROVADO · PENDENTE NORMATIVO | art. 44, III (época do tratamento × apuração do dano) |
| L3-R83 | 4.3 | E | TS | APROVADO · PENDENTE NORMATIVO | art. 44, par. único; troca única |
| L3-R84 | 4.3 | C | TS esp. | APROVADO · PENDENTE NORMATIVO | art. 49 literal |
| L3-R85 | 4.3 | E | TS | APROVADO | AWS-DP confere; NÃO VOLÁTIL correto (conceito documentado) |
| L3-R86 | 4.3 | C | — | APROVADO · PENDENTE NORMATIVO | art. 48, § 3º literal; o item não afirma dispensa da comunicação |
| L3-R87 | 4.3 | C | — | APROVADO | AWS-DP confere |
| L3-R88 | 4.3 | E | TS | APROVADO · PENDENTE NORMATIVO | art. 50, § 2º ("poderá"), I, "g"; troca faculdade × dever |
| L3-R89 | 4.3 | C | — | APROVADO (ressalva de registro) | GCP-RAI confere; registrar o rodapé "Last updated 2026-10-15" |
| L3-R90 | 4.3 | E | TS | APROVADO (ressalva de estilo) · PENDENTE NORMATIVO | art. 48, § 2º, I; troca única. "pode apenas recomendar... sem poder determiná-la" é restritivo duplo (estilo_onda_3, rec. 5); opcional |
| L3-R91 | 4.3 | E | TS | APROVADO (ressalva de registro) | MS-DPS confere; inversão dos modos = uma troca; VOLÁTIL (b) baixo correto; registrar o rodapé 2026-08-26 |
| L3-R92 | 4.3 | C | TS esp. | **AJUSTAR** · PENDENTE NORMATIVO | o contraste "e não o controlador" é contestável: o art. 50, caput, permite a controladores e operadores formular regras que estabeleçam "as normas de segurança, os padrões técnicos". O C fica sujeito a recurso. Texto exato sugerido (mantém troca de sujeito e [TS] espelho, com contraste verdadeiro): "Segundo a Lei Geral de Proteção de Dados Pessoais, a autoridade nacional, e não o encarregado, poderá dispor sobre padrões técnicos mínimos para tornar aplicável o dever de os agentes de tratamento adotarem medidas de segurança, considerados a natureza das informações tratadas, as características específicas do tratamento e o estado atual da tecnologia." Alternativa: retirar o contraste (C sem [TS]; [TS] da parte cai a 17) |
| L3-R93 | 4.3 | C | — | APROVADO | AWS-DP confere; NÃO VOLÁTIL correto |
| L3-R94 | 4.3 | E | TS | APROVADO (ressalva de registro) | GCP-LOG confere; VOLÁTIL baixo mantido, mas a hipótese declarada (d) "saída de exemplo" não se aplica (é aviso expresso da página): ler (c), recurso periférico (programa de registro de dados), ou (b) |
| L3-R95 | 4.3 | C | — | **REPROVADO** | gêmeo não declarado de L2-R59 (seção 2) |

## 4. Demais pontos do checklist
- Cobertura/escopo (4.2 direitos autorais e ética no uso de IA; 4.3 segurança em pipelines de áudio e transcrição): 12 itens de Lei 9.610 e 7 de LGPD (art. 44–50, capítulo de segurança e boas práticas) estão no escopo e diretos; 4.3 de fornecedor (R85, R87, R89, R91, R93, R94) diretos. A pergunta controversa (titularidade de conteúdo gerado por IA) não é julgada — correto. A 4.2 continua sem item de ética de conteúdo gerado além de Q26 e R81 (registro para a Gerência, sem efeito).
- Correção conceitual: nenhum gabarito errado; um C contestável (R92).
- Formato e tetos: maior formato 4/20 em cada folha (20%); com as retiradas propostas, 4.2 fica com AP 2/19 e 4.3 com AP 3/19 — dentro de 30%.
- VOLÁTIL: R91, R94, R95 marcados (baixo); critério da D-T96-ONDA2-ACEITE (II) bem aplicado nos NÃO VOLÁTEIS (R80, R81, R85, R87, R89, R93: boa prática ou conceito documentado). 4.3: 3/20 = 15% (2/19 sem R95). 4.2: 0/20.
- [TS]: 18/28 conferidos (14 E com troca única, 4 C espelho); confirmados um a um na tabela. Após esta R1: 18 (sem R80/R95, que não têm [TS]) se R92 mantiver o contraste corrigido.
- Gabarito: 14 C / 14 E (50%). Sem R80 e R95: 12 C / 14 E = 46,2% (na faixa 40–60%); 4.2 6/7, 4.3 6/7.
- Estrutura: script próprio — 28 ids na Parte 2 e 28 gabaritos na Parte 3, mesma ordem; Parte 2 sem Gabarito/[TS]/VOLÁTIL/REVERIFICAR; "FIM DO LOTE" na última linha; linha 1 no padrão.
- Estilo: ", e não" 1 C (R92) / 1 E (R72); concessiva em E (R81, R83); molduras variadas; cenários decorativos em R80/R81 (só ressalva).
- Aderência e piso: 28 diretos declarados, conferidos. Com as retiradas, cada folha fica com 19 itens, todos diretos (piso de 10 cumprido), mas abaixo da meta de 20: a Gerência decide reposição (2 itens, um por folha) em R2 ou saldo (precedente L2-R131).
- Contagem declarada pela produção na seção 1.3 ("nenhum gêmeo"; "frase-base" pelo maior trecho literal) está incorreta para R80 e R95: o método literal não detecta paráfrase; recomenda-se, nas próximas partes, conferir também por sobreposição de vocabulário (Jaccard ≥ 0,3) e pelo trecho-base da fonte.
- Discursiva/peça: não se aplica a esta parte.

## 5. Veredito geral
**APROVADO COM RESSALVAS.** Reprovados 2/28 = 7,1% (R80, R95; gêmeos não declarados). AJUSTAR 2 (R92 enunciado; R76 só (d-G)). Ressalvas de registro: R73, R81, R89, R90, R91, R94. PENDENTE NORMATIVO: 19 itens (R68–R79, R82, R83, R84, R86, R88, R90, R92). Abaixo do gate de 30%; sem GATE. Nenhum gabarito errado. QA PENDENTE mantido até R2/conferência normativa (D-QA-PENDENTE).
