# qa_normativo_R2.md — T-130 — 2026-10-25 — gerado por qa-normativo-da

QA normativo, rodada 2 (última), da produção v2 da ORDEM_DA_V2_FASE1 (gcb-cpp). Objeto: v2_producao.md, pacote_v1_15_DAv2_fase1_v2.json, registro_alteracoes_v2.md e resposta_R1.md, conferidos contra a minha R1 (DV1-17 e N1 a N10) e contra os pontos novos da produção. Só revisei a base normativa. Não alterei a produção e não fiz commit.

Taxa de itens novos com ERRO: **0 de 60 (0%)**. A taxa da R1 era 1 de 60. Não há gate.

## 0. Fontes reabertas em 2026-10-25

As URLs são as que localizei por WebSearch restrita a planalto.gov.br na R1. Não montei nenhuma de memória. Baixei de novo cada página com curl e a converti em texto localmente (cp1252). Nenhuma veio corrompida. O tamanho de cada página é igual ao da R1, o que indica que não houve alteração desde a manhã. Na Lei 9.784 não há nenhuma nota de 2025 ou 2026.

| Fonte | URL (texto compilado) | Bytes | Verificado em |
|---|---|---|---|
| Lei 9.784/1999 | https://www.planalto.gov.br/ccivil_03/leis/l9784.htm | 74.941 | 2026-10-25 |
| Lei 8.112/1990 | https://www.planalto.gov.br/ccivil_03/leis/l8112compilado.htm | 343.733 | 2026-10-25 |
| CF/1988 | https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm | 1.507.134 | 2026-10-25 |
| Decreto 12.374/2025 | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12374.htm | 42.715 | 2026-10-25 |
| Decreto 12.967/2026 | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/decreto/d12967.htm | 12.995 | 2026-10-25 |
| DL 4.657/1942 (LINDB) | https://www.planalto.gov.br/ccivil_03/decreto-lei/del4657compilado.htm | 48.971 | 2026-10-25 |

## 1. Dispositivos novos transcritos nesta rodada

| Dispositivo | Texto (transcrição) | Redação dada por | Vigência | Data | Observação |
|---|---|---|---|---|---|
| CF, art. 5º, XII | "é inviolável o sigilo da correspondência e das comunicações telegráficas, de dados e das comunicações telefônicas, salvo, no último caso, por ordem judicial, nas hipóteses e na forma que a lei estabelecer para fins de investigação criminal ou instrução processual penal; (Vide Lei nº 9.296, de 1996)" | orig. | vigente | 2026-10-25 | A DEFINIÇÃO do DV3 recorta o inciso às comunicações telefônicas. O recorte é fiel. |
| CF, art. 5º, LVI | "são inadmissíveis, no processo, as provas obtidas por meios ilícitos;" | orig. | vigente | 2026-10-25 | confere |
| Lei 9.784, art. 58, I a IV | "Têm legitimidade para interpor recurso administrativo: I - os titulares de direitos e interesses que forem parte no processo; II - aqueles cujos direitos ou interesses forem indiretamente afetados pela decisão recorrida; III - as organizações e associações representativas, no tocante a direitos e interesses coletivos; IV - os cidadãos ou associações, quanto a direitos ou interesses difusos." | orig. | vigente | 2026-10-25 | confere |
| Lei 9.784, art. 59, § 2º | "O prazo mencionado no parágrafo anterior poderá ser prorrogado por igual período, ante justificativa explícita." | orig. | vigente | 2026-10-25 | confere |
| Lei 9.784, art. 60 | "O recurso interpõe-se por meio de requerimento no qual o recorrente deverá expor os fundamentos do pedido de reexame, podendo juntar os documentos que julgar convenientes." | orig. | vigente | 2026-10-25 | confere. A DEFINIÇÃO omite a juntada de documentos, sem mudar o sentido. |
| Lei 9.784, art. 62 | "Interposto o recurso, o órgão competente para dele conhecer deverá intimar os demais interessados para que, no prazo de cinco dias úteis, apresentem alegações." | orig. | vigente | 2026-10-25 | confere |
| Lei 9.784, arts. 57; 63, §§ 1º e 2º; 49-G, § 3º | art. 57: "...no máximo por três instâncias administrativas, salvo disposição legal diversa." § 1º do art. 63: "Na hipótese do inciso II, será indicada ao recorrente a autoridade competente, sendo-lhe devolvido o prazo para recurso." § 2º do art. 63: "O não conhecimento do recurso não impede a Administração de rever de ofício o ato ilegal, desde que não ocorrida preclusão administrativa." § 3º do art. 49-G: ata "publicada por extrato no Diário Oficial da União" | orig.; o art. 49-G foi incluído pela Lei 14.210/2021 | vigente | 2026-10-25 | conferem |
| Decreto 12.374/2025, art. 1º | "Este Decreto dispõe sobre os critérios e os procedimentos a serem observados pelos órgãos e pelas entidades integrantes do Sistema de Pessoal Civil da Administração Federal – Sipec, para avaliação de desempenho de servidores ocupantes de cargo público efetivo durante o estágio probatório previsto no art. 20 da Lei nº 8.112, de 11 de dezembro de 1990." | orig. | vigente | 2026-10-25 | **REVERIFICAR** (norma de 2025) |
| Decreto 12.374/2025, art. 2º e par. único | "...ficará sujeito ao estágio probatório por período de trinta e seis meses, contado da data de início do efetivo exercício no cargo." / "É vedado o aproveitamento do tempo de serviço público exercido em outro cargo..." | orig. | vigente | 2026-10-25 | **REVERIFICAR** |
| Decreto 12.374/2025, art. 24 | "As disposições deste Decreto aplicam-se aos servidores públicos nomeados para cargos de provimento efetivo cujas nomeações ocorram após a data de sua publicação." | orig. | vigente | 2026-10-25 | **REVERIFICAR** |
| Decreto 12.967/2026, arts. 1º e 2º | art. 1º: "O Decreto nº 12.374, de 6 de fevereiro de 2025, passa a vigorar com as seguintes alterações: 'Art. 9º ... § 6º Os servidores deverão concluir as ações de desenvolvimento ... no prazo de trinta meses ... § 8º O programa de desenvolvimento inicial abordará: I - ...; e II - ...' (NR)". art. 2º: vigência na data da publicação. Assinado em 12 de maio de 2026. | — | vigente | 2026-10-25 | **REVERIFICAR**. Só altera o art. 9º do Decreto 12.374. Os arts. 1º, 2º e 24 não mudaram. |

Itens reescritos: reabri na mesma data a base de cada um. São a Lei 8.112, arts. 7º, 13, caput e § 1º, e 15, § 1º; e a Lei 9.784, arts. 13, II, 24, 30, 38, § 2º, 51, § 2º, 53 e 55. A letra é a que a R1 transcreveu. A LINDB, art. 21, parágrafo único, traz "deverá, quando for o caso, indicar as condições", o que confere com a restauração feita no DV1.

## 2. Achados da R1

| Achado R1 | Situação | Conferência na v2 (md e JSON) |
|---|---|---|
| DV1-17 (ERRO: o art. 53 não fala do Judiciário) | **RESOLVIDO** | Regra, justificativa, `correta` e `ref` seguem agora a letra do art. 53. O controle judicial aparece como doutrina, com [SEM FONTE]. No md e no JSON não restou "pode ser decretada pelo Judiciário" nem "o Judiciário também pode anulá-los". O gabarito E se sustenta. |
| N1 (art. 69 com o sentido invertido) | **RESOLVIDO** | A DEFINIÇÃO (L1759) usa a letra "aplicando-se-lhes apenas subsidiariamente os preceitos da Lei 9.784". O texto errado não aparece mais. Ressalva R2-4: redação imprecisa na tabela de proveniência. |
| N2 (Decreto 12.967/2026 sem registro) | **RESOLVIDO**, com ressalva | A linha própria na proveniência do DV2 (L1274) está correta. Ressalva R2-1: na DEFINIÇÃO (L843) e na BASE LEGAL (L847) a alteração é citada como "Decreto 12.967/2026, art. 9º". |
| Sugestão DV2-05 (Sipec; arts. 1º, 2º e 24) | **RESOLVIDO** | A regra confere com os três artigos transcritos acima. VOLÁTIL e REVERIFICAR mantidos. |
| N3 (art. 1º, § 2º, I) | **RESOLVIDO** | O texto literal foi restaurado (L1425). |
| N4 (art. 69-A, II) | **RESOLVIDO** | A letra está entre aspas na DEFINIÇÃO e nas linhas decisiva e regra do BQ-0127. |
| N5 (inferência na decisão coordenada) | **RESOLVIDO** | A RESPOSTA (L1650) e a proveniência dizem que a aplicação à Casa é "inferência pelo art. 1º, § 1º, e não letra". O § 6º, III, segue como letra. |
| N6 (LINDB, "quando for o caso") | **RESOLVIDO** | A expressão foi restaurada (L356) e confere com a página. |
| N7 (motivo como conceito doutrinário) | **RESOLVIDO** | "(doutrina)" foi acrescentado à regra do DV1-06 e ao glossário. |
| N8 (extrato tratado como vício de forma) | **RESOLVIDO** | O caso foi trocado (ver P2 na seção 3). |
| N9 (datas) | **RESOLVIDO**, com ressalva | As BASE LEGAL trazem "reconferido em 2026-10-25". Ressalva R2-2: os dispositivos que a v2 deixou só com 2026-10-20 foram reabertos hoje. |
| N10 (rótulo da pegadinha do DV3-09; BQ-0127) | **RESOLVIDO** no aspecto normativo | O DV3-09 agora é SUP, e a pegadinha de prioridade remete ao art. 69-A, § 1º, que confere. O mérito didático fica com o QA didático. |

## 3. Pontos novos

| Ponto | Resultado | Motivo |
|---|---|---|
| P1. CF, art. 5º, XII e LVI, no DV3 (instrução) | CONFERE | A transcrição está na seção 1. Interceptação telefônica sem ordem judicial é prova obtida por meio ilícito pela própria letra do XII e do LVI e do art. 30 da Lei 9.784. Na RESPOSTA, "recusa cabível, mas em decisão fundamentada" confere com o art. 38, § 2º, e "arquivamento" confere com o art. 40. Marcar a gravação feita por um dos interlocutores como [SEM FONTE — não afirmar] é correto, porque nenhuma norma do módulo trata dela. A data na BASE LEGAL é ressalva R2-2. |
| P2. Caso do despacho no lugar de portaria (DV1) | CONFERE | O art. 55 sustenta a RESPOSTA nas condições de lesão e de prejuízo e na expressão "poderão ser convalidados". O texto trata a sanabilidade do vício de forma como doutrina, com a marca [SEM FONTE], o que está correto. A Lei 4.717, art. 2º, b, também lista o vício de forma entre as causas de nulidade, de modo que a qualificação depende mesmo da doutrina, como o texto já diz. Não há erro normativo. |
| P3. Lei 9.784, arts. 58, 59, § 2º, 60 e 62 (DEFINIÇÃO do recurso) | CONFERE | São paráfrases fiéis. A BASE LEGAL pode passar a dizer "reconferido em 2026-10-25" (R2-2). |
| P4. Decreto 12.374/2025, arts. 1º, 2º e 24, e Decreto 12.967/2026 | CONFERE, com **REVERIFICAR**; ressalva R2-1 | O âmbito Sipec, os 36 meses, a regra das nomeações posteriores e o DOU de 7/2/2025 conferem. A citação "Decreto 12.967/2026, art. 9º" é imprecisa (R2-1). |
| P5. DV2-02 (reescrito; CON) | CONFERE | Pela letra do art. 7º, a investidura se dá com a posse. O art. 15, caput e § 1º, sustenta o resto. E |
| P6. DV3-09 (reescrito; SUP) | CONFERE | O art. 24 condiciona o prazo a "Inexistindo disposição específica". O item diz "mesmo que haja". E |
| P7. DV3-11 (reescrito; SUP) | CONFERE | O art. 38, § 2º, diz "Somente poderão ser recusadas, mediante decisão fundamentada, as provas propostas ... quando sejam ilícitas...". O item dispensa a decisão fundamentada. E |
| P8. DV3-14 (reescrito; AUT) | CONFERE | O art. 51, § 2º, diz "se a Administração considerar que o interesse público assim o exige". O item atribui a avaliação ao interessado. E |
| P9. DV3-02 (só recodificado, NEG) | CONFERE | O texto não mudou. O item declara delegável a matéria que o art. 13, II, veda. E |
| P10. Regras de BQ-0122 e BQ-0148 (prefixo "Ressalva:") | CONFERE | O conteúdo normativo não mudou. |
| P11. Demais alterações do registro_alteracoes_v2.md | sem efeito normativo | Comandos de 19 itens, `url` e `resumo`/`pares` de D1 e D2 (retiradas). Nenhuma toca base legal. As retiradas não deixam artigo sem cobertura nos lotes DV. |

## 4. Ressalvas (não afetam item nem gabarito)

- **R2-1 (citação da alteradora).** O Decreto 12.967/2026 tem dois artigos. É o art. 1º que dá nova redação ao art. 9º, § 6º, do Decreto 12.374 e lhe inclui o § 8º. Em L843 e L847 (2 ocorrências no JSON), trocar "Decreto 12.967/2026, art. 9º" por "Decreto 12.967/2026 (art. 1º), que alterou o art. 9º, §§ 6º e 8º, do Decreto 12.374".
- **R2-2 (datas).** A CF, art. 5º, XII e LVI, e a Lei 9.784, arts. 58, 59, § 2º, 60 e 62, foram reabertos hoje. As BASE LEGAL e a proveniência (L1566, L1726, L2051) podem dizer "reconferido em 2026-10-25 (qa_normativo_R2)".
- **R2-3 (BASE LEGAL do Decreto).** L847 diz "conferido em 2026-10-20" para os arts. 1º e 24. Segundo a R1, o mapa D2 não transcreveu o art. 1º. A data correta da primeira conferência do art. 1º é 2026-10-25.
- **R2-4 (proveniência do DV3, L2051, só no md).** "Art. 69: aplicam-se à lei própria apenas subsidiariamente os preceitos da Lei 9.784" fica mais claro como "aos processos regidos por lei própria aplicam-se apenas subsidiariamente os preceitos da Lei 9.784". O sentido não está invertido.

## 5. Veredito

**APROVADO COM RESSALVAS.** Dos 60 itens novos: 54 CONFERE (DV2-05 com REVERIFICAR e VOLÁTIL) e 6 NÃO CONFERIDO, por serem doutrina declarada sem atribuição a artigo (DV1-01, 02, 08, 09, 10, 11). Nenhum item tem ERRO, de modo que a taxa é de 0%. Os 7 intercalados reais conferem. As ressalvas R2-1 a R2-4 são de citação e de data. A produção pode aplicá-las sem nova rodada normativa.

REVERIFICAR na janela de 4 a 8/1/2027: Decreto 12.374/2025 (arts. 1º, 2º e 24) e Decreto 12.967/2026. Não encontrei alteração posterior a 2/10/2026 nas páginas abertas.

## 6. Leis que alteraram cada norma (páginas de 2026-10-25)

- Lei 9.784/1999: Lei 11.417/2006, Lei 12.008/2009 e Lei 14.210/2021. Nenhuma de 2025 ou 2026.
- Lei 8.112/1990, nos dispositivos citados: Lei 9.527/1997, Lei 8.270/1991, Lei 11.784/2008 e MP 2.225-45/2001. Remissão "(Vide Decreto nº 12.374, de 2025)" no art. 20 (ALERTA).
- CF, art. 5º, XII e LVI: redação original, com remissão à Lei 9.296/1996 no XII. Art. 41: EC 19/1998.
- LINDB, arts. 20 e 21: Lei 13.655/2018.
- Decreto 12.374/2025: Decreto 12.967/2026 (art. 9º, § 6º, com redação dada, e § 8º, incluído). **REVERIFICAR.**
