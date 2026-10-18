# D6_parecer_R2_gcb-cqfp.md — T-101 — 2026-10-18 — gerado por gcb-cqfp

QA R2 do Lote D6 v2 (LAI e LGPD), ciclo s12c3. Rodada R2 prevista pela D-CEGO-2 e pela D-D6-VEREDITO; o QA comparativo do Fundador (saida/gcb/D6_parecer_QA_comparativo.md) fez o papel da R1. A gcb-cqfp revisa e não reescreve: os ajustes abaixo trazem o texto exato, e quem os aplica é a GCB ou a gcb-cpp.

Objeto: saida/gcb/D6_v2.md, SHA-256 1b0f0b425ea38485d3c58f172c2cb4083b1193aea5a4f10a26d4092569c64fbe (957 linhas, conferido em 18/10/2026).
Base normativa: saida/gcb/D6_anexo_N_mapa_normativo.md, SHA-256 57e8c64d4f27fe2c7549ff9f9b16c16848a51558e9aa181a0ed48c2f85d3e80e. É o mesmo hash declarado na v2 (seção 6, linha 9), com a errata T-82 (seção 8).
Conferência por script (python -I, somente leitura): contagens; marcas; sequência C/E; v1 → v2 por tabela de correspondência (enunciado e gabarito); busca de autoria, modelo, serviço e URLs.

## 1. Evidência: URLs reabertas (regra de 3 URLs ou mais)
Fontes abertas em 18/10/2026 com User-Agent de navegador:

| URL | HTTP | Bytes | Dispositivos conferidos no texto baixado |
|---|---|---|---|
| https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm | 200 | 109.489 | art. 35, § 3º; art. 45; art. 126-A da Lei 8.112/1990 (texto do art. 44) |
| https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm | 200 | 230.913 | art. 5º, VIII; art. 8º, § 5º (vigente, sem tachado nem nota de revogação, o que confirma a errata T-82); art. 14, § 1º; art. 19, II; art. 35, caput; art. 52, § 3º; art. 55-A; art. 55-D, § 4º |
| https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15352.htm | 200 | 162.909 | redação do art. 55-A ("Agência Nacional de Proteção de Dados") |
| https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15141.htm | 200 | 799.134 | art. 8º-A da LAI |

Tudo confere com o Anexo N. A página da Lei 15.352 tem hoje 162.909 bytes; o Anexo registrou 164.468. O texto conferido não diverge e nenhum item é afetado. Fica só o registro.

## 2. Cumprimento da D-D6-VEREDITO

| # | Ponto | Veredito | Conferência |
|---|---|---|---|
| 1 | Base A; curso de A mais LAI-33 a LAI-37, LGPD-10 e LGPD-44 de B | CUMPRIDO | L20 a L24, G7 (§ 5º) e G23 correspondem aos blocos B LAI-33 a 37, LGPD-10 e LGPD-44. Foram reescritos sobre o Anexo N, com o dado literal (2 anos, 60 dias, 180 dias, art. 9º e Seção II do Cap. III no art. 45), e marcados "QA PENDENTE" |
| 2 | Pares e pegadinhas ausentes em A, importados de B | CUMPRIDO | Pares: L-P13 a L-P16, G-P16 a G-P20 e I-P7 (os 10 do parecer). Pegadinhas: LAI 21 a 32 (= B LAI-P07, 13, 16, 19, 22, 27, 30, 32 a 36) e LGPD 55 a 63 (= B LGPD-P14, 16, 25, 26, 31, 36, 40, 43, 44). Correspondência conferida uma a uma contra B |
| 3 | Itens D6-01 a D6-50 de A, com o D6-20 de B | CUMPRIDO | O script confirma que, pela tabela 0.5, os 50 enunciados são idênticos aos da v1 A. A única exceção é o novo D6-19 (antigo D6-20), cujo texto é idêntico ao D6-20 de B. Os 50 gabaritos não mudaram |
| 4 | Proveniência de A com a errata T-82 (nota G7) | CUMPRIDO | Seção 6, linhas 9 e 10, e Nota G7. O § 5º foi confirmado vigente na fonte reaberta hoje |
| 5 | Nenhuma URL de B; sem LGPD-P39 | CUMPRIDO | Há 7 URLs, todas iguais às do Anexo N, com 0 ocorrência de parâmetro de rastreio. P39 não foi importada. Não há ocorrência da denominação anterior da ANPD |
| 6 | LGPD-08 e LGPD-30 de B: só se corrigidos | CUMPRIDO (não importados) | O curso de A já traz "somente" no G6 (art. 7º, caput) e no G15 (art. 33, caput), conferido no Anexo N. Cobertura suficiente |
| 7 | [TS] de D6-03, 15 e 16: refazer ou retirar | CUMPRIDO (retirados) | Os novos D6-20, D6-01 e D6-28 ficaram sem [TS] e sem "tentação". As compensações (novos D6-02, D6-17 e D6-05) têm troca real única e gabarito E. A LAI mantém 15 [TS] |
| 8 | Desfazer a alternância C/E; tabela de correspondência | CUMPRIDO | LAI: CECEECECCECCCEECEECCCEEECCECEE. LGPD: CECCEEECCCEECECCCEEE. Sequência máxima de 3 iguais; não há alternância de 5 ou mais. Itens sobre o mesmo dispositivo não ficam adjacentes. A tabela 0.5 é completa e bijetiva (50 → 50) |
| 9 | Importados marcados "QA PENDENTE" | CUMPRIDO | Os 50 itens levam a marca, e os trechos importados também (curso, pares e pegadinhas) |

## 3. Cabeçalho neutro (D-CABECALHO-NEUTRO)
CUMPRIDO. A linha 1 é "LOTE D6 — LAI e LGPD — v2 — 18/10/2026". Busca no arquivo inteiro: 0 menção a autor, agente, unidade, modelo, fornecedor ou serviço (Claude, ChatGPT, utm, gcb, cpp, fábrica, externa, Fundador etc.). As ocorrências de "Presidência" são da República (art. 37 da LAI).

Observações à GCB (sem efeito no veredito):
(a) A v2 não tem a linha de controle do CLAUDE.md ("Formato de arquivos gravados"). A D-CABECALHO-NEUTRO, posterior e específica, prevalece para versão comparável. Convém registrar a exceção na reconciliação, como na T-72, 2.1.
(b) A seção 0 menciona "versão A/B", o parecer e as decisões, mas não diz quem produziu. Se a v2 for entregue fora da fábrica, a cópia deve começar na seção 1 ou omitir a seção 0.

## 4. Veredito por item (50)
Todos os itens foram conferidos contra o Anexo N: gabarito, base, [TS], forma Cebraspe e ponto único.

| Item | Gab. | Base (Anexo N) | [TS] | Veredito |
|---|---|---|---|---|
| D6-01 | C | LAI 11 § 2º (literal) | — | APROVADO |
| D6-02 | E | LAI 8º § 2º c/c 1º p.ú. I | [TS] alcance subjetivo | APROVADO |
| D6-03 | C | LAI 10 § 3º (literal) | — | APROVADO |
| D6-04 | E | LAI 2º p.ú. | [TS] parcela → totalidade | APROVADO |
| D6-05 | E | LAI 31 § 4º | [TS] "não poderá" → "poderá" | APROVADO |
| D6-06 | C | LAI 4º IV | — | APROVADO |
| D6-07 | E | LAI 15 caput | [TS] 10 → 5 dias | APROVADO |
| D6-08 | C | LAI 32 § 1º II | — | APROVADO |
| D6-09 | C | LAI 8º-A, I (REVERIFICAR) | — | APROVADO |
| D6-10 | E | LAI 11 § 1º | [TS] 20 → 30 dias | APROVADO |
| D6-11 | C | LAI 4º III | [TS] C, tentação concreta ("temporariamente") | APROVADO |
| D6-12 | C | LAI 8º caput | — | APROVADO |
| D6-13 | C | LAI 15 p.ú. | — | APROVADO |
| D6-14 | E | LAI 27 I e II | [TS] grau | APROVADO |
| D6-15 | E | LAI 8º § 1º IV | [TS] "todos" → "maior valor" | APROVADO |
| D6-16 | C | LAI 4º IV; LGPD 5º I | — (Interface) | APROVADO |
| D6-17 | E | LAI 16 § 1º | [TS] dispensa da instância prévia | APROVADO |
| D6-18 | E | LAI 32 I | — (generalização) | APROVADO |
| D6-19 | C | LAI 18 caput (importado de B) | — | APROVADO (retirar "QA PENDENTE (enunciado importado)" no aceite) |
| D6-20 | C | LAI 1º p.ú. II | — (marca retirada) | APROVADO |
| D6-21 | C | LAI 28 I a IV | — | APROVADO |
| D6-22 | E | LAI 10 caput | [TS] identificação "dispensada" | APROVADO |
| D6-23 | E | LAI 31 § 1º I | [TS] 100 → 50 anos | APROVADO |
| D6-24 | E | LAI 24 § 1º I | [TS] 25 → 20 anos | APROVADO |
| D6-25 | C | LAI 1º p.ú. I | — | APROVADO |
| D6-26 | C | LAI 21 p.ú. | — | APROVADO |
| D6-27 | E | LAI 4º VII × VIII | [TS] rótulo trocado | APROVADO |
| D6-28 | C | LAI 12 caput e § 1º | — (marca retirada) | APROVADO |
| D6-29 | E | LAI 24 § 4º | [TS] automático → após decisão | APROVADO |
| D6-30 | E | LAI 3º I | [TS] inversão | APROVADO |
| D6-31 | C | LGPD 26 § 1º IV | — | APROVADO |
| D6-32 | E | LGPD 5º VIII (REVERIFICAR) | [TS] ANPD → Conselho Nacional | APROVADO |
| D6-33 | C | LGPD 2º II e IV | — | APROVADO |
| D6-34 | C | LGPD 55-A (REVERIFICAR) | — | APROVADO |
| D6-35 | E | LGPD 19 II | [TS] 15 → 30 dias | APROVADO |
| D6-36 | E | LGPD 6º VII × VIII | [TS] conceito trocado | APROVADO |
| D6-37 | E | LGPD 11 II "f" | [TS] sujeito | APROVADO |
| D6-38 | C | LGPD 6º I (literal) | — | APROVADO |
| D6-39 | C | LGPD 41 § 2º I e II | — | APROVADO (obs. 1) |
| D6-40 | C | LGPD 18 VI | — | APROVADO |
| D6-41 | E | LGPD 23 § 2º | [TS] "não dispensa" → "dispensa" (Interface) | APROVADO |
| D6-42 | E | LGPD 4º I | [TS] "não econômicos" | APROVADO |
| D6-43 | C | LGPD 14 § 1º | [TS] C, tentação concreta ("ambos os pais") | APROVADO |
| D6-44 | E | LGPD 35 caput | [TS] ANPD → controlador | APROVADO |
| D6-45 | C | LGPD 23 caput (Interface) | — | APROVADO |
| D6-46 | C | LGPD 7º § 3º | — | APROVADO |
| D6-47 | C | LGPD 5º II | — | APROVADO |
| D6-48 | E | LGPD 48 caput | — (generalização "apenas") | APROVADO |
| D6-49 | E | LGPD 5º XIII × XIV | [TS] rótulo trocado | APROVADO |
| D6-50 | E | LGPD 52 § 3º | [TS] multa simples (inciso II) | APROVADO |

Obs. 1 (D6-39, sem efeito no veredito): "consistem em" seguido de só 2 dos 4 incisos do § 2º do art. 41. Pelo critério Cebraspe, item incompleto não é item errado, e o parecer comparativo não o apontou. Fica como cautela para a GBQ não pareá-lo, no mesmo simulado, com item que cobre os incisos III e IV.

Contagens (script): LAI 30 itens, 15 C e 15 E, 15 [TS] (14 E e 1 C), REVERIFICAR 1 (D6-09), Interface 1 (D6-16). LGPD 20 itens, 10 C e 10 E, 10 [TS] (9 E e 1 C), REVERIFICAR 2 (D6-32 e D6-34), Interface 2 (D6-41 e D6-45). VOLÁTIL 0. "QA PENDENTE" 50/50. "Tentação" aparece em todo item [TS] e em nenhum outro. A versão do estudante tem 50 itens e a última linha é "FIM DO LOTE D6". Tudo confere com a seção 7 da v2. Cobertura mínima da ficha (seção 5) cumprida em todos os tópicos; LAI "informações pessoais" tem 3 itens (D6-05, 16 e 23).

## 5. Blocos importados e reescritos de B (todos "QA PENDENTE"), conferidos contra o Anexo N

| Bloco | Dispositivos | Veredito |
|---|---|---|
| L20 (B LAI-33) | arts. 36 a 38 | APROVADO |
| L21 (B LAI-34) | art. 39, caput e §§ 1º a 4º | APROVADO |
| L22 (B LAI-35) | art. 40, I a IV | APROVADO |
| L23 (B LAI-36) | art. 41, I a IV | APROVADO |
| L24 (B LAI-37) | arts. 42 a 47 | APROVADO COM AJUSTE OBRIGATÓRIO (A-1) |
| G7, § 5º (B LGPD-10) | art. 8º, § 5º (errata T-82) | APROVADO |
| G23 (B LGPD-44) | arts. 60 a 65 | APROVADO |
| Pares L-P13 a L-P16 | art. 4º I, II, VIII e IX; art. 11 caput e § 1º; arts. 15, 17 e 29 | APROVADO |
| Pares G-P16 a G-P20 | art. 5º VI e VIII; arts. 14, 15, 16, 19, 41 e 48 | APROVADO |
| Par I-P7 | LAI arts. 23, 24 e 31 § 1º; LGPD art. 5º I e II | APROVADO |
| Pegadinhas LAI 21 a 32 | arts. 8º § 4º, 11, 13, 15/17, 23/24, 29 § 3º, 33/34, 36/37, 39, 40/27, 41, 45 | APROVADO (a 25 foi bem reformulada: "inconveniência institucional" não está na Lei) |
| Pegadinhas LGPD 56 a 63 | arts. 13 § 4º, 24, 25, 33 a 36, 48, 55-D, 55-C/58-A/58-B, 64/65 | APROVADO |
| Pegadinha LGPD 55 | art. 11 § 4º | APROVADO COM AJUSTE OBRIGATÓRIO (A-2) |
| Enunciado do D6-19 (B D6-20) | art. 18 | APROVADO |

Blocos importados: 14, todos aprovados, 2 com ajuste de forma obrigatório. Nenhum bloco reprovado.

## 6. Achados próprios da produção (seção 0.6), conferidos contra o Anexo N
| Achado | Veredito |
|---|---|
| L14, art. 23, caput e I a VIII literais | CONFERE |
| L14, art. 24, § 2º, com "ou do último mandato, em caso de reeleição" | CONFERE |
| G11, art. 14, caput ("crianças e de adolescentes") | CONFERE |
| G22, art. 55-D, § 4º (2, 3, 4, 5 e 6 anos) | CONFERE |
| L19, art. 35, §§ 3º a 5º (4 anos; desclassificação automática; mandato de 2 anos) | CONFERE |
| L24, art. 45 ("art. 9º e Seção II do Capítulo III") | CONFERE |
| G12 e G13, remissão de art. 15, III, e art. 18, IX, ao art. 8º, § 5º | CONFERE |

## 7. Não acatados (R-3 e R-7)
- Tabela de prazos de B (R-3): NÃO ACATAMENTO ACEITO. O parecer a dava como facultativa ("pode entrar") e a D-D6-VEREDITO não a exige. Os prazos estão no resumo (2.1 e 2.2) e nos pares L-P4, L-P15 e G-P18.
- Banco de reserva de B (R-7): NÃO ACATAMENTO ACEITO. Nenhum item de A foi reprovado nesta R2, então não há troca a fazer, e o banco não é necessário.

## 8. Ajustes com texto exato

A-1 (obrigatório; L24, art. 44, texto do art. 126-A da Lei 8.112/1990). A paráfrase suprime a condição legal da comunicação à "outra autoridade".
- Onde está: "nenhum servidor poderá ser responsabilizado civil, penal ou administrativamente por dar ciência à autoridade superior ou a outra autoridade competente de informação concernente à prática de crimes ou improbidade de que tenha conhecimento"
- Leia-se: "nenhum servidor poderá ser responsabilizado civil, penal ou administrativamente por dar ciência à autoridade superior ou, quando houver suspeita de envolvimento desta, a outra autoridade competente para apuração de informação concernente à prática de crimes ou improbidade de que tenha conhecimento"

A-2 (obrigatório; seção 4, pegadinha 55, art. 11, § 4º). Os incisos I e II não são exceções autônomas. São as finalidades da exceção relativa aos serviços de saúde.
- Onde está: "— art. 11, § 4º (vedação com as exceções dos incisos I e II e das hipóteses de serviços de saúde, assistência farmacêutica e assistência à saúde, observado o § 5º)."
- Leia-se: "— art. 11, § 4º (a vedação admite exceção nas hipóteses relativas a prestação de serviços de saúde, de assistência farmacêutica e de assistência à saúde, observado o § 5º, para permitir a portabilidade solicitada pelo titular (I) ou as transações financeiras e administrativas resultantes desses serviços (II))."

A-3 (forma; seção 0.7, registro). O registro diverge da R-2 e do título do G23, e o § 4º do art. 55-D aparece ao mesmo tempo como achado próprio (0.6, 4) e como trecho importado.
- Onde está: "G7 (§ 5º do art. 8º) e G23 (arts. 60 a 63), com marca no corpo; G22 (art. 55-D, § 4º)."
- Leia-se: "G7 (§ 5º do art. 8º) e G23 (arts. 60 a 65), com marca no corpo; G22 (art. 55-D, § 4º: acréscimo conferido no Anexo N, âncora da pegadinha importada 61)."

Os três ajustes estão fixados aqui e não tocam item, gabarito nem contagem. A GCB pode aplicá-los como errata pedida pela QA (precedente D-LOTED1-CANONICO), sem nova rodada.

## 9. Veredito geral
- Itens: 50 APROVADOS, 0 REPROVADOS. Taxa de reprovação: 0/50 = 0%. GATE de 30% não acionado.
- Blocos importados: 14 APROVADOS (2 com ajuste obrigatório de forma, A-1 e A-2). 0 reprovados.
- D-D6-VEREDITO: 9/9 pontos cumpridos. D-CABECALHO-NEUTRO: cumprida.
- Segue para reconciliação da gcb-gerencia com os ajustes A-1 a A-3. A retirada das marcas "QA PENDENTE" fica para o rito do pacote (GCB/GBQ). Nada vai à plataforma nem à candidata.
