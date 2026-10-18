# QA_T98C_R2_2026-10-18_gce-cqfp.md — T-98 — 2026-10-18 — gerado por gce-cqfp

Objeto: saida/gce/L3_reforco_onda4_C_v2.md (gce-cpp), 28 itens AUTORAL L3-R68 a L3-R95 (P2-4.2: R68–R81; P2-4.3: R82–R95). Rodada R2 (última permitida). Revisão; o arquivo de produção não foi alterado. Sem commit.
Lidos: o v2 inteiro (resposta item a item no topo, Partes 1–3); meu parecer R1 (QA_T98C_R1_2026-10-18_gce-cqfp.md); QA_T98AC_normativo_2026-10-18_qa-normativo.md, inclusive o "Adendo v2 — L3-R80 e L3-R95"; DECISOES.md (D-REFORCO-2; D-T97-META-FUNDADOR-RESP; D-ADERENCIA; D-T96-ONDA2-ACEITE (II)); edital/modulo_RF_IA_P2.md (4.2 e 4.3); pacote.json v1.10 (560 itens); partes A e B da onda 4 (v2); saida/gcb/D6_v2_1.md.
Itens inalterados e aprovados na R1 não foram revistos de novo, salvo o efeito de contagem.

## 1. Evidência — bases reabertas por esta QA em 18/10/2026 (curl, User-Agent de navegador; texto extraído e conferido por grep)

| base | HTTP | o que encontrei |
|---|---|---|
| https://www.planalto.gov.br/ccivil_03/leis/l9610.htm | 200 | art. 46, III: "a citação em livros, jornais, revistas ou qualquer outro meio de comunicação, de passagens de qualquer obra, para fins de estudo, crítica ou polêmica, na medida justificada para o fim a atingir, indicando-se o nome do autor e a origem da obra" — igual à justificativa do R80. Art. 14: "não podendo opor-se a outra adaptação, arranjo, orquestração ou tradução, salvo se for cópia da sua" — igual à citação corrigida do R76 |
| https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm | 200 | art. 37: "O controlador e o operador devem manter registro das operações de tratamento de dados pessoais que realizarem, especialmente quando baseado no legítimo interesse" — igual ao R95. Localização: CAPÍTULO VI "Dos Agentes de Tratamento de Dados Pessoais", Seção I "Do Controlador e do Operador" (a segurança está no CAPÍTULO VII, "Da Segurança e das Boas Práticas"). Art. 46, § 1º — igual ao R92. Art. 41, § 2º: atividades do encarregado (I a IV), sem competência para dispor sobre padrões técnicos mínimos — o contraste do R92 é verdadeiro |
| https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/speech-to-text/data-privacy-security | 200 | "only on the Azure's server memory, and no data is stored at rest" confere (R91); rodapé datetime 2026-08-26 = registro novo do v2 |
| https://docs.cloud.google.com/speech-to-text/docs/v1/data-logging | 200 | "not deleted when you delete your project. Fill out the..." confere (R94) |

## 2. Conferência dos ajustes e registros do R1

| ponto do R1 | aplicado como pedido? | o que conferi |
|---|---|---|
| R92 (AJUSTAR) | SIM | linha 190 = texto exato sugerido no R1, palavra por palavra ("a autoridade nacional, e não o encarregado, poderá dispor sobre padrões técnicos mínimos..."). Mapa (l. 66), (d-G) (l. 326) e Contagens (l. 348) atualizados; [TS] espelho e C mantidos |
| R76 (AJUSTAR o (d-G)) | SIM | l. 246 reproduz a letra do art. 14 (conferida acima); enunciado e gabarito inalterados |
| R73 (registro) | SIM | l. 232 |
| R81 (registro) | SIM | l. 107 (vizinhança corrigida, par com L1-R98) e l. 272 |
| R89 (registro) | SIM | l. 312 e l. 367 (rodapé 2026-10-15) |
| R90 (estilo, opcional) | SIM (mantido com registro) | l. 317; aceito, a ressalva era opcional |
| R91 (registro) | SIM | l. 322 e l. 365 (rodapé 2026-08-26, conferido) |
| R94 (hipótese) | SIM | l. 68 e l. 337: hipótese (c), recurso periférico |
| R80 e R95 (REPROVADOS) | SIM, substituídos | itens novos julgados na seção 3 |

## 3. Itens novos

### L3-R80 (4.2; Lei 9.610/1998, art. 46, III; C)
- Mérito: o enunciado traz as três condições do inciso (finalidade de estudo, crítica ou polêmica; medida justificada; nome do autor e origem da obra), em forma condicional ("se for feita..."), que corresponde à letra do inciso. Gabarito C correto. Sem [TS], o que está correto (não há restritivo nem contraste).
- Aderência: DIRETA. É uma limitação ao direito de autor (4.2, "Direitos autorais"), com o mesmo critério dos itens R68–R79 já aprovados. O cenário (estudo técnico de unidade da Câmara) é verossímil e não muda o juízo. O formato "aplicação parlamentar" fica aceito.
- Gêmeo: nenhum. Nenhum item do pacote v1.10 nem das partes A e B julga o art. 46. Jaccard máximo 0,15 (L3-R02, P2-3.1, outro ponto); contra as partes A e B, 0,09. O vizinho declarado (L3-Q22, art. 29, regra da autorização) tem outro ponto.
- Base literal: confere (seção 1). O qa-normativo deu CONFERE no Adendo v2.
- Risco residual baixo: dá para discutir se um "estudo técnico" interno é "meio de comunicação". O qa-normativo considera que ele cabe em "qualquer outro meio de comunicação", e o C resiste.
- **APROVADO.**

### L3-R95 (4.3; LGPD, art. 37; C)
- Mérito: reproduz o dever dos dois agentes. Não julga a parte "especialmente quando baseado no legítimo interesse", o que não altera o sentido. A contratada "em nome da Câmara" é operadora (art. 5º, VII). O item não afirma quem é o controlador no poder público e por isso evita a armadilha União/órgão. Gabarito C correto. Sem [TS], correto.
- Aderência: o produtor a declara direta mas defensável. **Divirjo: a aderência é PARCIAL à 4.3.**
  - O art. 37 está no Cap. VI, Seção I ("Do Controlador e do Operador"), e não no Cap. VII ("Da Segurança e das Boas Práticas"). A frase do v2 "no capítulo de agentes de tratamento e boas práticas" (l. 24) é imprecisa.
  - O registro das operações de tratamento é um dever de documentação e de responsabilização dos agentes. Não é um controle de segurança da informação do pipeline, como trilha técnica de acesso ou log.
  - A matéria cabe por inteiro na 4.1 ("LGPD e proteção de dados em sistemas de transcrição e IA"). O próprio pacote põe o vizinho L3-Q18 (controlador × operador) na 4.1, e o D6 agrupa o art. 37 em "Controlador, operador, registro e relatório de impacto".
  - A banca aceitaria o item. O problema é a classificação na folha, e não o mérito.
  - Efeito pela D-T97-META-FUNDADOR-RESP: a 4.3 continua com 20 itens, sendo 19 diretos e 1 parcial. O piso de 10 diretos é cumprido e a meta de 20 também, porque o parcial conta. Pela D-ADERENCIA, o R95 vai só para simulado diagnóstico.
  - A troca pelo art. 50, § 1º, sugerida pelo produtor, não cabe: esta é a última rodada e item novo não teria QA.
- Gêmeo: nenhum. Nenhum item do pacote v1.10 nem das partes A e B julga o art. 37. O D6 trata o art. 37 só no texto de curso (G16, l. 341), não em item. Jaccard máximo 0,19 (BQ-0056, definição de operador, outro ponto), 0,18 (L3-R11, art. 47) e 0,14 (L3-Q18); contra as partes A e B, 0,08.
- Base literal: confere (seção 1). O qa-normativo deu CONFERE no Adendo v2.
- **APROVADO, com aderência PARCIAL** (a reclassificação é D1 da Gerência; não exige alterar o texto).

## 4. Veredito por item alterado

| id | folha | gab. | [TS] | veredito | motivo |
|---|---|---|---|---|---|
| L3-R73 | 4.2 | E | TS | APROVADO | registro da ressalva feito; enunciado inalterado |
| L3-R76 | 4.2 | C | TS esp. | APROVADO | citação do art. 14 agora literal (conferida) |
| L3-R80 | 4.2 | C | — | APROVADO | item novo; mérito, base literal e aderência direta; sem gêmeo |
| L3-R81 | 4.2 | E | TS | APROVADO | par com L1-R98 registrado; vizinhança corrigida |
| L3-R89 | 4.3 | C | — | APROVADO | rodapé registrado |
| L3-R90 | 4.3 | E | TS | APROVADO | registro de estilo feito; a ressalva era opcional |
| L3-R91 | 4.3 | E | TS | APROVADO | rodapé registrado e conferido |
| L3-R92 | 4.3 | C | TS esp. | APROVADO · PENDENTE NORMATIVO (confirmação) | texto exato do R1; o contraste "e não o encarregado" é verdadeiro (art. 41, § 2º, conferido por mim). Porém o ponto de contraste mudou (controlador → encarregado), e o qa-normativo (§ 5) disse que o item com ponto de troca alterado volta a ele; o Adendo v2 só cobriu R80/R95. O v2 (l. 17 e 28) retirou a marca do R92 cedo demais: falta a confirmação curta do qa-normativo |
| L3-R94 | 4.3 | E | TS | APROVADO | hipótese (c) corrigida; VOLÁTIL baixo mantido |
| L3-R95 | 4.3 | C | — | APROVADO (aderência PARCIAL) | item novo; mérito e base literal corretos; sem gêmeo; art. 37 fora do capítulo de segurança (seção 3) |

Os 18 itens restantes (R68–R72, R74, R75, R77–R79, R82–R88, R93) não mudaram e seguem com o veredito do R1. A marca normativa deles foi retirada pelo CONFERE do qa-normativo.

## 5. Contagens (script próprio, python3 -I, somente leitura)
- Estrutura: 28 ids na Parte 2 e 28 gabaritos na Parte 3, na mesma ordem. A Parte 2 não traz Gabarito, [TS], VOLÁTIL nem REVERIFICAR. "FIM DO LOTE" está na última linha.
- Gabarito: 14 C / 14 E (50,0%). 4.2: 7 C / 7 E. 4.3: 7 C / 7 E. Dentro de 40–60%.
- [TS]: 18/28 (14 em E com troca única; 4 em C espelho: R76, R77, R84, R92). Por folha, 9/14 em cada uma, que é exatamente o mínimo de metade + 2 (9). No lote, o mínimo seria 16. Os dois itens novos são C sem [TS], o que está correto.
- VOLÁTIL: 4.2 com 0/20 e 4.3 com 2/20 = 10% (R91, R94, ambos baixos). O teto de 20% é cumprido. O R95 deixou de ser VOLÁTIL: lei federal.
- Formato (folhas de 20): na 4.2 o maior formato tem 4/20 = 20% (troca de sujeito e situação hipotética), e a aplicação parlamentar tem 3. Na 4.3 o maior formato também tem 4/20 = 20% (definição, troca de sujeito, aplicação parlamentar com Q30, R87, R94 e R95, e situação hipotética). O teto de 30% é cumprido.
- Diretos por folha: 4.2 com 20/20; 4.3 com 19/20 pela minha leitura (R95 parcial) ou 20/20 pela leitura do produtor. O piso de 10 é cumprido nas duas leituras, e a meta de 20 também (o parcial conta).

## 6. Taxa de reprovação da parte
0/28 reprovados nesta R2 (0%). Os dois itens reprovados no R1 (R80 e R95 da v1) foram substituídos, e os substitutos foram aprovados. Não houve GATE.

## 7. Registros residuais para a Gerência (D1)
1. **R95 — aderência:** recomendo PARCIAL na 4.3 (só simulado diagnóstico, D-ADERENCIA). Alternativa da Gerência: manter direta com fundamentação própria. Nas duas leituras a meta e o piso da folha ficam cumpridos. Corrigir na consolidação a descrição "no capítulo de agentes de tratamento e boas práticas" (l. 24): o art. 37 está no Cap. VI, Seção I.
2. **R92 — PENDENTE NORMATIVO:** é preciso a confirmação curta do qa-normativo sobre o novo contraste (encarregado, art. 41) antes do gatilho A. Nas l. 17, 28 e 356 do v2, a marca foi retirada antes dessa confirmação.
3. **R80 e R95 — marca normativa:** o Adendo v2 do qa-normativo deu CONFERE. A Gerência pode retirar o PENDENTE NORMATIVO, que ainda aparece nas l. 28, 268, 343 e 356. O QA PENDENTE cai com esta R2.
4. **R81 × L1-R98:** a GBQ deve evitar os dois no mesmo simulado (registro já feito pelo produtor).
5. **4.2 sem ética de conteúdo gerado** além de Q26 e R81: registro sem efeito (já anotado no R1).
6. **[TS] por folha no limite exato (9/14):** qualquer mudança futura de gabarito ou retirada de [TS] na consolidação fura o mínimo da folha.

## 8. Veredito geral
**APROVADO COM RESSALVAS.** Reprovados 0/28 (0%). Ressalvas: R95 com aderência PARCIAL (D1); R92 PENDENTE NORMATIVO, só confirmação. Todos os ajustes do R1 foram aplicados como pedido. Nenhum gabarito está errado nem em disputa.
