# D3_parecer_R1_gcb-cqfp.md — T-76 — 2026-10-20 — gerado por gcb-cqfp
PARECER R1 — LOTE D3 v1 (saida/gcb/D3_v1.md, SHA-256 a97d5b82428eceb506668d9a5a414f8e51a428fd8b83c7be02d1915bdda025db, 253.216 bytes; junção mecânica, pelo orquestrador, de saida/gcb/D3_v1_parteA.md, SHA-256 77a59f344cbab17e862dc1ada7471eb36817161eb3712f948d05092a6c77bf78, 165.241 bytes, e saida/gcb/D3_v1_parteB.md, SHA-256 c8fb303c442a185aa45c3ac1b4b5db33dea847d684b764c1e0e5c3fe1d533707, 87.893 bytes, produzidas por duas instâncias da gcb-cpp). Revisão de mérito. A gcb-cqfp revisa e não reescreve: os textos de ajuste abaixo são pontuais e fixados; a redação final e a substituição dos itens reprovados são da gcb-cpp na v2.

Referências: ficha saida/gcb/D3_ficha_lote.md (SHA-256 71823790…e51a81a; seções 2 a 7, 9 e 10); despacho-base lotes/loteD3/DESPACHO.md (09f4b8af…3fbe1); regras/PADRAO_UNICO_v1.md; regras/estilo_banca.md (v1.1.3); regras/proveniencia.md; Anexo N saida/gcb/D3_anexo_N_mapa_normativo.md (2ef58f9b…2ff1df), única base de texto legal; banco/banco.csv (b1c1588f…5721f) e banco/mapeamento_adicional.csv (c6f8a355…302e5); Anexo D1 = saida/gcb/D1_v2.md (63bd27c3…3d56). Modelos: saida/gcb/D5_parecer_R1_gcb-cqfp.md e saida/gcb/D1_parecer_R1_gcb-cqfp.md. Scripts da QA em diretório próprio do scratchpad, todos com python3 -I. O arquivo saida/gcb/D3_leitura_critica.md não existia durante o R1 e não foi lido.

## 0. Resultado
- Itens: 80. APROVADO 61; APROVADO COM AJUSTE 9; REPROVADO 10.
- **Reprovação: 10/80 = 12,5%** (limite do gate: 30%). **Não há gate.**
- Por folha: 5.1, 6.1 e 7 sem reprovado; 5.2 com 1 (10%); 6.2 com 2 (20%); 6.3 com 3 (30%); 6.4 com 2 (20%); 6.5 com 2 (20%). Parte A: 10/70 (14,3%); Parte B: 0/10.
- Padrão da reprovação: os 10 reprovados são todos itens C sem [TS] que espelham um item E da mesma folha ou repetem ponto bloqueado (seção 3.2). A Parte A fechou 5 C por folha escrevendo o C como negação do E vizinho; a contagem de [TS] (40) não muda com as substituições, mas a proporção C das folhas 6.2 a 6.5 sim.
- Blocos: junção AJUSTE (conteúdo íntegro; estrutura e conferências da ficha 2.6 faltando; teste de ordem do lote falha na emenda); curso AJUSTE; resumo AJUSTE; pares APROVADO; pegadinhas APROVADO; proveniência APROVADO; contagens por folha e por parte APROVADO, do lote REPROVADO (seção 5.1); BASE DOUTRINÁRIA APROVADA no mérito (26 itens, todos pacíficos; 1 fora da lista fechada, seção 4); leitura crítica NEUTRO CONFERIDO, com ressalvas de forma (seção 5.9).
- Veredito geral: **APROVADO COM AJUSTES E SUBSTITUIÇÕES** — a v2 responde aos 34 pontos da seção 8. Há decisões da GCB pendentes (pontos 27 a 31), sobretudo a da folha 6.3, que a ficha não permite fechar com 10 itens de pontos distintos.

## 1. Evidência: conferência independente (checklist 2 e 6)
1. **URLs reabertas** em 20/10/2026, às 10:24 UTC, por curl com User-Agent de navegador, sem parâmetro nem sufixo, em diretório próprio do scratchpad. Extração por script (cp1252; texto em `<strike>`/`<s>`/`<del>`/line-through retirado; tags apagadas; espaços normalizados), sem redigitação.

| URL (idêntica à do Anexo N e à da tabela de proveniência) | HTTP | Bytes (hoje × Anexo N) | Resultado |
|---|---|---|---|
| https://planalto.gov.br/ccivil_03/leis/l8429compilada.htm | 200 | 173.931 × 173.931 | 256/256 dispositivos da seção 4.9 aparecem literalmente no texto não tachado de hoje. |
| https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm | 200 | 1.507.134 × 1.507.134 | CF, arts. 5º, XXV; 37, caput e §§ 4º a 6º; 49, caput e V; 84, caput, IV, VI, a e b, e parágrafo único: 13/13 conferem. |
| https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm | 200 | 923.899 × 923.899 | CC, art. 43: confere. |
| https://planalto.gov.br/ccivil_03/leis/l5172compilado.htm | 200 | 289.910 × 289.910 | CTN, art. 78, caput e parágrafo único: conferem (grafia "interêsse", "intêresse", "tranqüilidade"). |
| https://www.planalto.gov.br/ccivil_03/leis/l9784.htm | 200 | 74.941 × 74.941 | Lei 9.784, arts. 11 a 17 (14 dispositivos): conferem. |
| https://www.planalto.gov.br/ccivil_03/leis/l4717.htm | 200 | 35.908 × 35.908 | Lei 4.717, art. 2º (12 dispositivos): conferem. |

Total: 298/298 dispositivos da seção 4 do Anexo N conferem com as páginas de hoje; nenhuma divergência; nenhuma alteração posterior a 2/10/2026 visível.
2. **Citações**: um script extraiu as 794 citações "art./arts." do D3_v1 (curso, resumo, pares, pegadinhas, itens, justificativas, proveniência) e conferiu artigo e parágrafo contra a seção 4 do Anexo N. Restaram 4 "suspeitas", todas remissões que estão dentro do próprio texto da Lei 8.429 (CF, art. 37, § 1º, no art. 11, XII; CPC, arts. 330, 133 a 137 e 489, no art. 17 e no art. 17-C): corretas. As 80 bases dos itens existem e são vigentes; nenhuma é revogada, vetada ou um dos 26 dispositivos com "(Vide ADI …)" (ficha 3.4). Varredura de pares e pegadinhas: nenhum dispositivo bloqueado como base ou diferença.
3. **Por leitura**, conferi contra o Anexo N o texto, os números, os prazos e os verbos dos 80 enunciados e das 160 linhas de justificativa, da tabela do resumo (12 linhas), dos 23 pares e das 63 pegadinhas. Os trechos entre aspas nos itens: os que não estão no Anexo N são todos falas do próprio item (campo "troca") ou da justificativa, e não citação da lei; o único texto superado é o "dolosa ou culposa" do D3-72, item E admitido pela ficha 3.2. Desvios de redação: seção 5 (resumo, curso).
4. **Jurisprudência e ADI**: 0 ocorrência de STF, STJ, TCU, tribunal, jurisprudência, súmula, ADI, "imprescritível" ou doutrinador nos 80 enunciados e no gabarito comentado. "[SEM FONTE]" em item: 0. VOLÁTIL = 0 e REVERIFICAR = 0, corretos (Anexo N, seção 2.3).
5. **Itens reais**: banco/banco.csv tem exatamente 8 itens mapeados a P1-DA-5, 6 e 7 (BQ-0116, 0130, 0133 [X, anulado], 0138, 0139, 0140, 0141, 0149), os do Anexo R, com texto e gabarito conferidos; banco/mapeamento_adicional.csv não tem nenhuma linha para P1-DA-5, 6 ou 7. **Anexo D1**: os pontos D1-32 a D1-43 conferidos no D1_v2.md (linhas 350 a 372).

## 2. Junção e coerência entre as partes (checklist 1)
1. **Integridade do conteúdo**: script de comparação de linhas. Todas as 1.241 linhas não vazias da Parte A e as 328 da Parte B estão no D3_v1.md, exceto as linhas 1 e finais de cada parte e quatro cabeçalhos de seção da Parte B (descartados na fusão das seções). O D3_v1.md acrescenta só 7 linhas de moldura (linha 1, linha 2, "Fontes…", "## 0. CABEÇALHOS DAS PARTES", dois "### Parte A/B" e "FIM DO LOTE D3"). Ids D3-01 a D3-80 contínuos, sem lacuna nem duplicata, na versão do estudante e no gabarito; códigos C, P e G sem colisão (C5.1-01 a C6.5-06 e C7-01 a C7-20; P-01 a P-13 e P-51 a P-60; G-01 a G-43 e G-51 a G-70). "Nenhum texto alterado": confirmado.
2. **Desvios da ficha 2.6** (forma; AJUSTE da junção, ponto 25):
   (a) linha 1 fora do formato ("— junção mecânica pelo orquestrador … nenhum texto alterado"); a ficha e o CLAUDE.md pedem "# D3_v1.md — T-76 — 2026-10-20 — gerado por gcb-cpp". Linha 2 sem "(P1-DA, itens 5 a 7)" e com "(partes A e B)".
   (b) "## 0. CABEÇALHOS DAS PARTES" no lugar do preâmbulo da A seguido de "Parte B — convenções próprias".
   (c) Em "## 3", a tabela da Parte B manteve cabeçalho próprio; em "## 5", o título diz "D3-01 a D3-70".
   (d) "## 7" sem a linha "Lote" calculada por script, sem o teste de ordem refeito na sequência D3-01 a D3-80 e sem a lista unificada dos 80 pontos com conferência de duplicata. A QA refez o teste: **falha na emenda** (seção 5.1).
   (e) "## 8" sem "### Junção" (SHA-256 das partes e do D3_v1.md; resultado das conferências). Os SHA-256 das partes estão só na linha 4.
   (f) O script saida/gcb/D3_juntar_v1.py, que a ficha manda usar também na v2, não existe no repositório.
3. **Coerência entre as partes**: convenções iguais ([TS], E5 sem [TS], elemento-isca, formatos, APL pela moldura); fronteira D3-69 = D3-70 = C e D3-71 = D3-72 = E, como manda a ficha; nenhuma parte invadiu a matéria da outra (Parte A só com "ver item 7"; Parte B só com "ver itens 5 e 6"); nenhum ponto de julgamento repetido entre as partes. O único efeito cruzado é o padrão de período 4 na emenda (seção 5.1).

## 3. Veredito por item (checklist 4)
Legenda: AP = APROVADO; AJ = APROVADO COM AJUSTE (texto exato em 3.1); REP = REPROVADO (motivo em 3.2). Colunas G = gabarito; TS = [TS]; BD = BASE DOUTRINÁRIA.

| Item | Folha | G | TS | BD | Veredito | Motivo curto |
|---|---|---|---|---|---|---|
| D3-01 | 5.1 | E | sim | — | AP | Lei 9.784, art. 12, p. ú.; inversão colegiado → presidente (E2), troca única. Difere de D1-39 pertinente. |
| D3-02 | 5.1 | C | sim (isca) | — | AP | Art. 14, § 1º, literal; isca literal. Ângulo distinto de D1-41/42. |
| D3-03 | 5.1 | C | — | — | AP | CTN, art. 78, caput; rol parcial com "entre outros" (C6), sem pretensão de completude. |
| D3-04 | 5.1 | E | — | — | AP | CTN, art. 78, p. ú.; E5 (exceção de urgência inexistente). |
| D3-05 | 5.1 | E | sim | — | AP | CF, art. 84, VI, a; condição negada como um só elemento. |
| D3-06 | 5.1 | C | — | — | AJ | CF, art. 84, IV × VI; correto, mas "matérias disponíveis mediante decreto" é impreciso. |
| D3-07 | 5.1 | E | sim | — | AP | CF, art. 49, caput e V; Congresso → Câmara isoladamente. APL. |
| D3-08 | 5.1 | E | sim | — | AJ | Art. 15 × art. 12; gabarito certo, mas "subordinado ao titular da competência" é ambíguo na avocação (o titular é o órgão inferior). |
| D3-09 | 5.1 | C | — | sim | AP | Disciplinar × polícia: pacífico, na lista. |
| D3-10 | 5.1 | C | — | sim | AP | Controle judicial do discricionário: pacífico como redigido ("apenas por discordar"). Dúvida respondida (seção 6). |
| D3-11 | 5.2 | E | sim | — | AP | CTN, art. 78, p. ú.; discricionária → vinculada. Distinto de D3-04. |
| D3-12 | 5.2 | C | — | sim | AP | Abuso como gênero: pacífico, na lista; distinto de BQ-0138. |
| D3-13 | 5.2 | E | sim | — | AJ | Gabarito certo; a moldura "competência exclusiva do Congresso Nacional" entrega o gabarito do D3-07. |
| D3-14 | 5.2 | E | sim | — | AP | Lei 4.717, art. 2º, p. ú., e; supressão de "implicitamente" (E6). |
| D3-15 | 5.2 | C | — | — | AP | Art. 2º, a, e p. ú., a, aplicados a cenário (ângulo previsto na ficha 5.2). |
| D3-16 | 5.2 | C | — | sim | AP | Poder-dever de agir: pacífico, na lista (1 item). |
| D3-17 | 5.2 | E | — | — | AP | Art. 2º, caput; "nulos" → "meramente anulável" (E5). Difere de D1-32 aceito. |
| D3-18 | 5.2 | C | sim (isca) | — | AP | CF, art. 49, V; isca literal "ou dos limites de delegação legislativa". APL. |
| D3-19 | 5.2 | C | — | — | **REP** | Repete o ponto do BQ-0130 e espelha o D3-17. |
| D3-20 | 5.2 | E | sim | — | AP | Art. 2º, caput; supressão de "lesivos" (E6). Nota com D1-32. |
| D3-21 | 6.1 | E | sim | — | AP | CF, art. 37, § 6º; prestadoras → todas as de direito privado. |
| D3-22 | 6.1 | C | sim (isca) | — | AP | § 6º; isca literal; concessionária. |
| D3-23 | 6.1 | E | — | — | AP | § 6º; restrição a dano patrimonial que a letra não tem (E5). |
| D3-24 | 6.1 | C | — | — | AP | CF, art. 5º, XXV, só como contraste (alerta 2); 1 item, no teto. |
| D3-25 | 6.1 | C | — | — | AJ | CC, art. 43; a oração "como civilmente responsáveis por atos dos seus agentes" contém o ponto do D3-30. |
| D3-26 | 6.1 | E | sim | sim | AJ | Risco administrativo × integral: pacífico; mas "A responsabilidade civil objetiva" entrega o gabarito do D3-29. |
| D3-27 | 6.1 | E | sim | sim | AP | Evolução invertida: pacífico, na lista (1 item). |
| D3-28 | 6.1 | C | — | — | AP | § 6º aplicado ao Legislativo sem afirmar personalidade de órgão. APL. |
| D3-29 | 6.1 | E | sim | sim | AP | Objetiva → subjetiva: pacífico ("como regra"). |
| D3-30 | 6.1 | C | — | — | AP | CC, art. 43, aplicado; fica distinto do D3-25 depois do ajuste deste. |
| D3-31 | 6.2 | C | — | — | **REP** | Mesmo ponto do D3-22 (prestadora de direito privado responde pelo § 6º), só com outro nome. |
| D3-32 | 6.2 | E | sim | — | AP | § 6º; condição do regresso suprimida (E3). |
| D3-33 | 6.2 | C | — | — | AJ | Contém "assegura" (CF) e "ressalva" (CC), que é o ponto do D3-34, e "culpa ou dolo", que é o do D3-32/36. |
| D3-34 | 6.2 | E | sim | — | AP | Verbos permutados (E2). |
| D3-35 | 6.2 | E | sim | — | AP | Sociedade econômica fora do § 6º; aplicação do ponto abstrato do D3-21 (nota à GBQ). |
| D3-36 | 6.2 | C | sim (isca) | — | AP | "dolo ou culpa": a culpa basta; distinto do D3-32. |
| D3-37 | 6.2 | C | — | sim | AP | Conduta comissiva lícita: pacífico como redigido ("podendo"). Dúvida respondida (seção 6). |
| D3-38 | 6.2 | E | — | — | AP | E5: o regresso não é afastado. |
| D3-39 | 6.2 | C | — | — | **REP** | Negação literal do erro do D3-38 (regresso contra o agente doloso), somada ao ponto do D3-28. |
| D3-40 | 6.2 | E | sim | — | AP | CC, art. 43; restrição aos atos dolosos (E6). |
| D3-41 | 6.3 | E | sim | — | AP | § 6º: "por ação ou por omissão" acrescentado; só a letra. |
| D3-42 | 6.3 | C | — | — | **REP** | Soma dos pontos do D3-41 (CF) e do D3-49 (CC) e responde aos dois. |
| D3-43 | 6.3 | E | sim | sim | AP | Dever jurídico × mera possibilidade: pacífico, na lista. |
| D3-44 | 6.3 | C | — | sim | AP | Sem dano não há dever de indenizar: pacífico. Ver ponto 28 (teto de 1 item por tópico). |
| D3-45 | 6.3 | C | — | sim | AP | Sem nexo (contrafactual) na omissão: pacífico; distinto de D3-55. APL. Ver ponto 28. |
| D3-46 | 6.3 | E | sim | sim | AP | Segurador universal: pacífico, na lista. |
| D3-47 | 6.3 | E | sim | sim | AP | Conceito de conduta omissiva trocado (E1): pacífico. |
| D3-48 | 6.3 | C | — | sim | **REP** | Espelho do D3-47 e segundo item do tópico "conduta comissiva × omissiva", que a ficha limita a 1. |
| D3-49 | 6.3 | E | sim | — | AP | CC, art. 43: "omissões" acrescentado; distinto do D3-41 pelo dispositivo. |
| D3-50 | 6.3 | C | — | sim | **REP** | Segundo item do tópico "dever jurídico de agir" (ficha: no máximo 1); responde ao D3-43. |
| D3-51 | 6.4 | C | — | — | AP | "nessa qualidade" nos dois textos, literal. |
| D3-52 | 6.4 | E | sim | — | AP | Atividade estritamente particular fora do "nessa qualidade". |
| D3-53 | 6.4 | E | — | — | AP | E5: condição de processo prévio inexistente. |
| D3-54 | 6.4 | C | sim (isca) | — | AP | Posição de "dolo ou culpa" no § 6º; isca literal. Par com o D3-66 (ver ajuste deste). |
| D3-55 | 6.4 | E | sim | sim | AP | Nexo × coincidência temporal: pacífico. |
| D3-56 | 6.4 | E | sim | sim | AP | Requisitos + culpa da PJ: pacífico; 1 item de enumeração, no teto. |
| D3-57 | 6.4 | C | — | sim | **REP** | Negação literal do erro do D3-55 (conduta e dano sem causação). |
| D3-58 | 6.4 | C | — | — | AP | Elementos da letra aplicados; baixa discriminação (nota à GBQ). APL. |
| D3-59 | 6.4 | E | sim | — | AP | CC, art. 43; dano efetivo → potencialidade. |
| D3-60 | 6.4 | C | — | sim | **REP** | Responde ao D3-56 (enumera conduta, dano e nexo e afasta a culpa da PJ). |
| D3-61 | 6.5 | E | sim | sim | AP | Culpa concorrente → excludente: pacífico. |
| D3-62 | 6.5 | E | sim | sim | AP | Fato exclusivo de terceiro rebaixado a atenuante: pacífico. |
| D3-63 | 6.5 | C | — | sim | AP | Força maior como excludente, sem distinção: pacífico. |
| D3-64 | 6.5 | E | sim | sim | AP | Risco integral sem excludentes (conceito): pacífico; sem hipótese concreta. |
| D3-65 | 6.5 | C | — | sim | **REP** | Responde ao D3-61 e, na outra metade, repete o ponto do BQ-0139. |
| D3-66 | 6.5 | C | — | — | AJ | Tópico obrigatório da 6.5, mas a oração "pois…" reproduz o D3-54. |
| D3-67 | 6.5 | E | sim | sim | AP | Efeitos permutados: pacífico. Ponto fora da lista fechada da 6.7 (ver ponto 29). |
| D3-68 | 6.5 | E | sim | — | AP | § 6º não enumera excludentes; só a letra. |
| D3-69 | 6.5 | C | — | sim | **REP** | Mesmo ponto e mesma moldura do D3-63, com "caso fortuito" no lugar de "força maior" (distinção vedada). |
| D3-70 | 6.5 | C | — | — | AP | CC, art. 43: o regresso ressalvado não exclui nem atenua. APL. |
| D3-71 | 7 | E | sim | — | AJ | Gabarito certo, mas o erro (dispensa do dolo) é respondido pelo D3-73 (C) da mesma folha. Trocar o elemento. |
| D3-72 | 7 | E | sim | — | AP | Art. 10, caput; "dolosa ou culposa" (texto superado): único da folha, admitido pela ficha 3.2. |
| D3-73 | 7 | C | — | — | AP | Art. 17-C, § 1º, literal; ângulo distinto do BQ-0149, como pede a ficha (tópico 2). |
| D3-74 | 7 | C | — | — | AJ | Art. 11, XI; o cenário pode ser lido como nomeação por detentor de mandato (art. 11, § 5º) e não diz o dolo do caput. APL. |
| D3-75 | 7 | E | — | — | AP | Art. 11, § 4º; E5 ("razão pela qual"); sem [TS], correto. |
| D3-76 | 7 | C | sim (isca) | — | AP | Art. 20, caput, literal; isca "só" literal. |
| D3-77 | 7 | E | sim | — | AP | Art. 14, § 2º; "não impede" → "impede". Distinto do BQ-0140. |
| D3-78 | 7 | E | sim | — | AP | Art. 23, caput; termo inicial trocado. NUM. |
| D3-79 | 7 | C | — | — | AP | Art. 17-B, § 1º, II, literal (60 dias). Nome do acordo: letra, sem efeito afirmado. Dúvida respondida. |
| D3-80 | 7 | C | — | — | AP | Art. 3º, caput, literal (C3). |

### 3.1 Textos exatos dos ajustes (APROVADO COM AJUSTE)
1. **D3-06** — Enunciado: "A competência do Presidente da República para expedir decretos e regulamentos para a fiel execução das leis está prevista no inciso IV do art. 84 da Constituição Federal, e não nas alíneas do inciso VI, que tratam de outras matérias sobre as quais o Presidente dispõe mediante decreto." Gabarito C mantido.
2. **D3-08** — Enunciado: "Nos termos da Lei nº 9.784/1999, tanto a delegação quanto a avocação de competência podem envolver órgão que não seja hierarquicamente subordinado à autoridade que delega ou que avoca." Troca: "avocação de competência atribuída a órgão hierarquicamente inferior → avocação que pode envolver órgão não subordinado à autoridade que avoca". Gabarito E e [TS] mantidos.
3. **D3-13** — Enunciado: "Segundo a Constituição Federal, a sustação de atos normativos que exorbitem do poder regulamentar ou dos limites de delegação legislativa alcança os atos normativos de qualquer dos Poderes." Justificativa, linha 2: "O item amplia o objeto da sustação a atos de qualquer Poder; a tentação é aceitar a extensão por reconhecer as duas hipóteses do inciso V." Gabarito E, [TS] e troca mantidos. (Tira da moldura o titular da competência, que é o ponto do D3-07.)
4. **D3-25** — Enunciado: "O art. 43 do Código Civil, ao tratar da responsabilidade civil por atos de agentes, não menciona as pessoas jurídicas de direito privado prestadoras de serviços públicos, que constam do art. 37, § 6º, da Constituição Federal." Ponto de julgamento: "Código Civil, art. 43 — o dispositivo não menciona as pessoas jurídicas de direito privado prestadoras de serviços públicos". Mecanismo: C3. Gabarito C mantido.
5. **D3-26** — Enunciado: "Como regra, a responsabilidade civil do Estado pelos danos que seus agentes, nessa qualidade, causem a terceiros segue a modalidade do risco integral, e não a do risco administrativo." Gabarito E, [TS] e troca mantidos.
6. **D3-33** — Enunciado: "O art. 37, § 6º, da Constituição Federal refere-se ao direito de regresso contra o responsável, ao passo que o art. 43 do Código Civil se refere ao direito regressivo contra os causadores do dano." Justificativa, linha 2: "Os destinatários do regresso têm redação diferente nos dois textos; o item registra a diferença sem troca." Gabarito C mantido; acrescentar "Difere: difere de D3-34 (verbo assegurado × ressalvado) e de D3-32/D3-36 (condição de dolo ou culpa)".
7. **D3-66** — Enunciado: "Pela redação do art. 37, § 6º, da Constituição Federal, a ausência de culpa do agente não exclui a responsabilidade da pessoa jurídica pelos danos que ele, nessa qualidade, causar a terceiros." Difere: "difere de D3-54 porque este julga a posição do dolo e da culpa no texto; aqui se julga o efeito da ausência de culpa do agente sobre a responsabilidade perante o terceiro". Gabarito C mantido. Nota à GBQ: D3-54 e D3-66 nunca no mesmo simulado.
8. **D3-71** — Enunciado: "Constitui ato de improbidade administrativa importando em enriquecimento ilícito auferir, mediante a prática de ato doloso, vantagem patrimonial indevida em razão do exercício de cargo, de mandato, de função, de emprego ou de atividade nas entidades referidas no art. 1º da Lei nº 8.429/1992, exclusivamente nas hipóteses enumeradas nos incisos do art. 9º dessa lei." Ponto de julgamento: "Lei 8.429, art. 9º, caput — o caput alcança qualquer tipo de vantagem patrimonial indevida, e os incisos vêm precedidos de 'e notadamente' (não formam rol exclusivo)". Justificativa, linha 1: "O art. 9º, caput, alcança 'qualquer tipo de vantagem patrimonial indevida' auferida mediante ato doloso e enumera os incisos com 'e notadamente'." Linha 2: "O item converte em rol exclusivo os incisos que a lei apresenta como destaque; a tentação é ler a lista como completa." Mecanismo: E6. Troca: "qualquer tipo de vantagem patrimonial indevida …, e notadamente → vantagem patrimonial indevida … exclusivamente nas hipóteses enumeradas nos incisos". Base: Lei 8.429/1992, art. 9º, caput. Gabarito E e [TS] mantidos. (Se a produtora preferir outro elemento do caput do art. 9º, pode, desde que o erro não seja a dispensa do dolo nem toque dispositivo bloqueado.)
9. **D3-74** — Enunciado: "Considere que, em órgão do Poder Legislativo da União, servidor investido em cargo de direção, na condição de autoridade nomeante, nomeie dolosamente o próprio cônjuge para o exercício de cargo em comissão. Nessa situação, a conduta descrita corresponde a uma das condutas relacionadas no art. 11 da Lei nº 8.429/1992, dispositivo que alcança a nomeação para cargo em comissão na administração pública direta e indireta em qualquer dos Poderes da União." Base: art. 11, caput e XI; art. 11, § 5º (só para registrar que o cenário não é de detentor de mandato eletivo). Gabarito C mantido.

### 3.2 Itens reprovados (substituir na v2, sem repetir ponto do lote, do Anexo R ou do Anexo D1)
Critério (precedente do D5-54, ficha 6.1): reprova-se o item cujo ponto decisivo já é o de outro item, de modo que quem acerta um acerta o outro, quando a ficha não exige os dois tópicos. Quando a ficha exige os dois tópicos, ou quando um ajuste de texto separa as proposições, o item fica (AP ou AJ) com nota à GBQ.
1. **D3-19 (5.2, C)** — Agente "dentro de suas atribuições" que visa fim diverso: é o ponto bloqueado do BQ-0130 (desvio de finalidade mesmo com competência); o "difere" (desapropriação × Lei 4.717) é só de cenário. Além disso, o C ("o ato é nulo, por desvio de finalidade") responde ao D3-17. Substituto (C, sem [TS]): sugestão — CTN, art. 78, parágrafo único, em situação hipotética: ato de polícia em atividade que a lei tenha como discricionária, praticado pelo órgão competente, nos limites da lei e com processo legal, mas com desvio de poder, não é exercício regular ("difere de D3-11", que julga a condição discricionária × vinculada). A folha fica com 4 C/5 E se não houver substituto, dentro de 4 a 6 C.
2. **D3-31 (6.2, C)** — Permissionária no lugar da concessionária do D3-22: mesma proposição, no mesmo nível (aplicação). A exigência da ficha (6.2: ao menos 2 SIT com sujeitos diferentes) continua cumprida por D3-35 (sociedade que não presta serviço público) e D3-38 (pessoa jurídica de direito público). Substituto (C): sugestão — Código Civil, art. 43, só pela letra: "o direito regressivo contra os causadores do dano depende de haver, por parte destes, culpa ou dolo" (DEF; distinto do D3-32 pelo dispositivo, depois do ajuste do D3-33).
3. **D3-39 (6.2, C, APL)** — "tem assegurado o direito de regresso contra o servidor [que agiu com dolo]" é a negação literal do segmento falso do D3-38; a outra metade é o ponto do D3-28. Substituto (C) de ponto novo da 6.2, se houver no Anexo N; senão, ponto 30.
4. **D3-42 (6.3, C)** — Afirma, para os dois textos, o que D3-41 (CF) e D3-49 (CC) julgam separadamente; responde aos dois. A ficha ("ao menos 2 itens pela letra") fica cumprida por D3-41 e D3-49.
5. **D3-48 (6.3, C)** — "A conduta comissiva consiste em uma ação positiva do agente, e não em uma abstenção" responde ao D3-47 e é o segundo item do tópico "conduta comissiva × omissiva (conceito)", que a ficha 5.2 limita a 1.
6. **D3-50 (6.3, C)** — Segundo item do tópico "omissão relevante pressupõe dever jurídico de agir" (ficha 5.2: no máximo 1); "dever jurídico, e não moral" responde ao D3-43.
7. **D3-57 (6.4, C)** — "sem que a conduta tenha causado o dano, não se configura a responsabilidade" é a negação literal do segmento falso do D3-55.
8. **D3-60 (6.4, C, APL)** — O cenário enumera conduta, dano e nexo e afasta a culpa da pessoa jurídica: responde ao D3-56 (requisitos com a culpa da pessoa jurídica acrescentada). O tópico obrigatório "dispensa de prova de culpa da pessoa jurídica" fica com D3-54 (letra) e D3-56 (enumeração).
9. **D3-65 (6.5, C)** — "a culpa concorrente da vítima apenas atenua" responde ao D3-61; a outra metade ("a culpa exclusiva da vítima exclui") é o ponto do BQ-0139. O ângulo "exclusiva × concorrente" era permitido, não obrigatório.
10. **D3-69 (6.5, C)** — Mesma moldura e mesmo ponto do D3-63, com "caso fortuito" no lugar de "força maior". Como a ficha veda distinguir os dois, os itens são a mesma proposição.
Substitutos das folhas 6.3, 6.4 e 6.5 (e o segundo da 6.2): a QA não encontrou, no Anexo N e na lista fechada da 6.7, ponto novo de gabarito C que não espelhe item já aprovado. A produtora tenta. Se não achar, declara no bloco à GCB, e a GCB decide (pontos 28 e 30).

## 4. BASE DOUTRINÁRIA (checklist 3)
- Contagem: 26 itens (teto 33). Por folha: 5.1 = 2/3; 5.2 = 2/3; 6.1 = 3/4; 6.2 = 1/3; 6.3 = 7/8; 6.4 = 4/4; 6.5 = 7/8; 7 = 0/0. Subtetos da 5.1: discricionário 1 (D3-10), disciplinar 1 (D3-09), hierarquia 0. Todos dentro do teto. Depois das reprovações: 6.3 = 5, 6.4 = 2, 6.5 = 5, total 20.
- Pacificidade: os 26 pontos, como redigidos, são pacíficos, sem atribuição a autor, sem classificação disputada e sem tese de tribunal. Nenhum ponto vedado pela ficha 6.7 é usado: abuso por omissão, elementos sempre vinculados, distinção caso fortuito × força maior, teoria nomeada do regime da omissão, hipóteses concretas de risco integral e ônus da prova da excludente.
- Lista fechada: 25 dos 26 estão nela. **D3-67** (excludente afasta; atenuante reduz) não está na lista dos itens da 6.5, mas é o par não obrigatório "excludente × atenuante (BASE DOUTRINÁRIA)" que a própria ficha admite (5.3), e é o núcleo do subitem 6.5. A QA o aprova no mérito e pede ratificação da GCB (ponto 29).
- Pontos sob dúvida da produtora: **D3-10**, pacífico. O item diz só que o Judiciário não anula o ato legal "apenas por discordar da conveniência e da oportunidade"; não nega o controle de legalidade nem diz "nunca". **D3-37**, pacífico. A responsabilidade por conduta lícita danosa é admitida sem divergência relevante, e o item usa "não pressupõe, necessariamente" e "podendo haver", sem afirmar requisitos (dano anormal ou especial), que seriam disputáveis. O curso C6.2-03 deve tirar "a ser confirmado pelo R1" (ponto 20).
- Rótulos doutrinários ao lado da letra: corretos no curso ("excesso de poder" e "desvio de poder" com a Lei 4.717, art. 2º; "risco administrativo" com o § 6º). Nenhum item atribui à lei um rótulo doutrinário.

## 5. Blocos (checklist 1, 5, 6 e 7)
### 5.1 Contagens, proporção C/E, [TS] e sequência (refeitas por script sobre o D3_v1.md)
- 80 itens D3-01 a D3-80, 10 por folha, todos com os campos fixos e "QA PENDENTE"; nenhuma incoerência entre o cabeçalho e o campo "Marcas" ([TS], BASE DOUTRINÁRIA). [TS] sem "troca": 0; "troca" sem [TS]: 0; [TS] C sem elemento-isca: 0.
- C/E: 40/40 (50%); 5 C por folha. [TS] = 40 (Parte A 35; Parte B 5), 5 por folha. [TS] C = 6 (D3-02, 18, 22, 36, 54 e 76), no máximo 1 por folha; 6.3 e 6.5 sem [TS] C. Todo [TS] tem troca real e única (conferido item a item). D3-05 nega a condição da alínea a como um só elemento, aceito. E sem [TS] = 6 (Parte A: D3-04, 17, 23, 38 e 53; Parte B: D3-75), todos E5, correto.
- Formatos por folha no máximo 3; APL ≤ 2 por folha (6.4 = 2). Pelo critério da ficha 6.3 (moldura do Legislativo = APL), só os itens rotulados APL usam "Legislativo" ou "Câmara" no enunciado. D3-13 cita o Congresso como sujeito da norma, sem moldura: SUJ, correto. NUM = 0 na Parte A e 2 na Parte B, com números literais (8 anos; 60 dias).
- Depois das reprovações, sem substitutos: 5.2 com 4 C/5 E; 6.2 com 3 C/5 E; 6.3 com 2 C/5 E; 6.4 com 3 C/5 E; 6.5 com 3 C/5 E. Lote: 30 C/40 E em 70 itens (42,9%). As folhas 6.2 a 6.5 caem abaixo de 4 C. Os substitutos devem ser C (ponto 26).
- **Teste de ordem (ficha 6.4)**: APROVADO por folha (as 8) e por parte (A e B), na sequência de gabaritos e na da marca [TS]. **REPROVADO no lote**: na emenda, de D3-64 a D3-75 (12 itens), o gabarito repete o bloco de período 4 "ECCE" três vezes (ECCE ECCE ECCE: folha 6.5, posições 4 a 10, e folha 7, posições 1 a 5). A marca [TS] repete "TnnT" de D3-64 a D3-74 (11 itens). A regra é "nenhum bloco repetido de período 2 a 4 por 8 ou mais itens". A falha não foi vista porque a junção não refez o teste na sequência inteira (seção 2, d). Pela ficha 2.6, item 5, a correção cabe à Parte B, que troca posições dentro da folha 7, mantidos D3-71 e D3-72 = E. Como a v2 vai mexer na 6.5 (D3-65 e D3-69), o teste deve ser refeito depois das substituições (ponto 23).
- Pontos de julgamento: 80 declarados, sem duplicata literal. Há duplicatas de sentido (seção 3.2) e sobreposições aceitas com nota (ponto 33).

### 5.2 Cobertura (ficha 5.2)
- 5.1: discricionário D3-10; hierárquico D3-01, 02, 08 (3, todos fora dos pontos do D1); disciplinar D3-09; regulamentar D3-05, 06 (art. 49, V, só D3-07); polícia D3-03, 04. Cumprida.
- 5.2: uso do poder D3-11; exorbitância D3-13, 18; incompetência e desvio de finalidade D3-14, 15, 17, 20; abuso como gênero D3-12; poder-dever D3-16 (1). Cumprida, mesmo sem o D3-19.
- 6.1: sujeitos do § 6º D3-21, 22, 28; sujeitos do art. 43 D3-25; "danos" D3-23; art. 5º, XXV D3-24 (1); natureza e modalidade D3-26, 29; evolução D3-27 (1). Cumprida.
- 6.2: SIT com sujeitos diferentes D3-35, 38 (e D3-31, reprovado); regresso D3-32, 33, 34, 36, 38; conduta lícita D3-37 (1). Cumprida. Concentração: 6 dos 10 itens julgam a cláusula do regresso; a v2 não deve aumentá-la.
- 6.3: letra D3-41, 49; dever jurídico D3-43; dano D3-44; nexo D3-45; segurador D3-46; conceito D3-47. O regime da omissão não é afirmado em nenhum item. O teto de "1 item por tópico" foi ultrapassado nos tópicos de D3-43/50 e D3-47/48 (reprovados) e no de D3-44/45 ("sem dano e sem nexo"), que a QA não reprova porque os dois julgam condições diferentes e um não responde ao outro (ponto 28).
- 6.4: "nessa qualidade" D3-51, 52; dano D3-59 (e D3-58); nexo D3-55; culpa da pessoa jurídica D3-54, 56; enumeração D3-56 (1). Cumprida.
- 6.5: força maior e caso fortuito D3-63; fato de terceiro D3-62; culpa concorrente D3-61; risco integral D3-64; ausência de culpa do agente D3-66; letra D3-66, 68, 70. Cumprida; caso fortuito × força maior e ônus da prova sem item.
- 7: tópicos 1 a 9 com ao menos 1 item (D3-80; 73; 71; 72; 74 e 75; 76; 77; 79; 78); no máximo 2 por tópico; tópico 10 sem item (livre). O tópico 6 (sanções) tem só o D3-76, aceito pela ficha (ao menos 1). Nenhum item toca o art. 12, § 1º.

### 5.3 Curso — AJUSTE
- Parte A: 43 blocos; Parte B: 20 blocos (mínimo 16), na ordem da lei. Cada bloco traz definição por artigo ou "BASE DOUTRINÁRIA (ponto pacífico)", exemplo hipotético e pegadinha com o que a desfaz. Jurisprudência só com "[SEM FONTE — não afirmar]" (C5.1-10, C6.1-06, C6.2-04, C6.3-06, C6.5-02, C6.5-04, C6.5-05, C7-19, C7-20). Os 26 dispositivos com remissão a ADI aparecem só pela letra (resumida) e com a nota, sem efeito afirmado. Revogados e vetados aparecem só como tais. Nada sobre normas ou práticas reais da Câmara além do Ato da Mesa nº 251/2026 citado na nomenclatura.
- Ajustes: (a) **C5.1-03, exemplo**: o cenário ("o presidente de um colegiado delegue parte da competência do colegiado a um de seus órgãos") não é a hipótese do art. 12, parágrafo único, e confunde. Trocar por "Considere que um órgão colegiado administrativo federal delegue parte de sua competência ao respectivo presidente: aplica-se o art. 12, parágrafo único, e as matérias do art. 13 continuam indelegáveis." (b) **C6.2-03**: tirar "a ser confirmado pelo R1" (seção 4). (c) **C7-15, exemplo**: "o réu cite todos os fatos e se omita" não tem sentido. Trocar por "Considere que, em ação contra agente de órgão legislativo, o réu, citado, não conteste: não se aplica a presunção de veracidade dos fatos alegados pelo autor em caso de revelia (art. 17, § 19, I)."

### 5.4 Resumo — AJUSTE
- Duas páginas na Parte A (itens 5 e 6) e uma na Parte B (item 7), fiéis ao curso; tabela com números literais do Anexo N; números de dispositivos bloqueados fora da tabela (correto).
- Ajustes: (a) item 7, "Sistema e dolo": "Só há improbidade por conduta dolosa dos arts. 9º, 10 e 11 (art. 1º, § 1º)" acrescenta restrição que a letra não tem, porque omite "ressalvados tipos previstos em leis especiais" (ficha 6.5). Redação: "Consideram-se atos de improbidade as condutas dolosas tipificadas nos arts. 9º, 10 e 11, ressalvados tipos previstos em leis especiais (art. 1º, § 1º)". (b) Tabela: "40 salários mínimos (impenhorabilidade da indisponibilidade)". "Impenhorabilidade" não é termo da lei; trocar por "40 salários mínimos (vedada a decretação de indisponibilidade da quantia depositada)", art. 16, § 13.

### 5.5 Pares — APROVADO
23 pares (A 13, mínimo 10; B 10, mínimo 8; lote mínimo 18). Os 13 obrigatórios (P-01 a P-07 e P-51 a P-56) estão presentes, com base dos dois lados e "como a banca troca". Os não obrigatórios são todos da lista admitida (5.3). Nenhum tem dispositivo bloqueado ou tema vedado como diferença. P-13 (culpa exclusiva × concorrente) pode ficar no curso, mesmo com o D3-65 reprovado.

### 5.6 Pegadinhas — APROVADO
63 (G-01 a G-43; G-51 a G-70), uma por bloco, sem repetição, cada uma com dispositivo ou base doutrinária. G-67 ("omitir o integral ressarcimento") apoia-se no art. 17-B, I, que não está na lista dos 26 bloqueados (só o caput do art. 17-B está): correto. Se o C5.1-03 e o C7-15 mudarem, as pegadinhas G-03 e G-65 continuam válidas.

### 5.7 Proveniência — APROVADO
Parte A, 5 normas; Parte B, 6 normas. As 10 URLs distintas do D3_v1 são idênticas às do Anexo N (script: 0 fora), sem parâmetro, com "verificado em 20/10/2026". As 6 principais foram reabertas pela QA (seção 1). Itens reais citados com fonte em cdn.cebraspe.org.br, pelo banco. Pontos sem fonte declarados ("[SEM FONTE — não afirmar]"), nenhum em item.

### 5.8 Estilo Cebraspe — APROVADO no conjunto
"Julgue cada item como Certo ou Errado." na versão do estudante. Afirmação única ou duas orações coordenadas sobre o mesmo ponto; nenhum "exceto"; nenhuma referência a tribunal, ADI ou doutrinador. Termos absolutos: ou literais ("só", D3-76) ou o próprio erro (D3-14, 20, 21, 40, 46, 71 depois do ajuste). Exceções tratadas acima: D3-06 (redação), D3-08 (ambiguidade), D3-33 (três afirmações), D3-74 (cenário).

### 5.9 Leitura crítica (ficha 9; critério 7) — NEUTRO CONFERIDO, com ressalvas de forma
- saida/gcb/D3_para_leitura_critica.md (SHA-256 ad2934375836119a2fd0cb13c7f811b12f3b945f7c777cfd562bc1c60b911804; 528 linhas). Sem itens, gabaritos, justificativas, contagens, pontos de julgamento, bloco à GCB ou URLs. A varredura da ficha deu 0 ocorrência de fornecedor, modelo ou serviço de IA, agente ou unidade da fábrica, "fábrica", Fundador, Presidência, orquestrador, id de tarefa ou decisão, "QA PENDENTE", Anexo N/R/D1, "BQ-", "D3-", "ficha", "banco", "gabarito", [TS], REVERIFICAR, VOLÁTIL e "[SEM FONTE". As ocorrências de "agente" (97) e "presidencial" são termos da matéria. A instrução ao leitor é a literal da ficha. Quanto à identidade da origem, o arquivo é neutro.
- Ressalvas (não exigem regerar o arquivo, já entregue; ponto 32): (a) linha 1 com "e improbidade" no lugar de "e improbidade administrativa" (texto da ficha 9); (b) restaram "Parte A" e "Parte B" e frases de processo ("Mínimo deste material para a Parte A: 10, com os 7 obrigatórios … Entregues: 13"; "faixa G-01 a G-50 da Parte A"), que a ficha manda retirar; (c) "BASE DOUTRINÁRIA (ponto pacífico)" virou "Base doutrinária: (ponto pacífico)", contra a ficha 9, que manda manter a expressão; (d) o script saida/gcb/D3_para_leitura_critica_gen.py, que a ficha 9 exige (lição do R1 do D5, ponto 23), não existe no repositório, e por isso a geração não é reproduzível; (e) a linha da T-76 em TAREFAS.md não traz a hora de gravação nem o SHA-256 do arquivo neutro (ficha 9).
- A resposta externa (saida/gcb/D3_leitura_critica.md) não existia durante este R1. Pela ficha 9, ela vai à v2 pelo registro de acatamento, e o R2 confere.

### 5.10 Primeira e última linha (critério 9)
Última linha "FIM DO LOTE D3": correta. Primeira linha fora do formato (seção 2, a). Produção (gcb-cpp, duas instâncias) e QA (gcb-cqfp) em agentes distintos.

## 6. Respostas às dúvidas da produtora (seções 8 das partes)
**Parte A**
1. Instrumento formal da sustação (CF, art. 49, V): a abordagem está correta. Fica "[SEM FONTE — não afirmar]" no curso, e nenhum item o nomeia.
2. Folhas 6.3 e 6.5 sem dispositivo no recorte: julgar só o que o § 6º e o art. 43 dizem ou não dizem está correto (D3-41, 49, 66, 68 e 70 aprovados; D3-66 com ajuste). O D3-42 sai por duplicata, não por base.
3. Reforço da 6.5 (T-100): é decisão da GCB (registro, item 2). Ver o ponto 30, que propõe antecipar o adendo para a v2.
4. Lei 9.784 (art. 13, I e III; art. 14, caput; art. 17) só no curso, e hierarquia em D3-01, 02 e 08: correto, sem repetir pontos do D1.
5. CTN, art. 78, parágrafo único, com dois donos: respeitado (D3-04 na 5.1, D3-11 na 5.2).
6. Itens marcados para atenção: D3-10, AP (pacífico). D3-37, AP (pacífico; a folha 6.2 não perde o item). D3-26, AJ; D3-29 e D3-64, AP. D3-45, AP; D3-57, REP. D3-56 e D3-54, AP; D3-60, REP; D3-66, AJ. D3-17, AP. D3-19, REP. D3-14, AP. D3-08, AJ. D3-52, AP.
7. Classificação APL: confirmada. D3-13 é SUJ.
8. Notas à GBQ: acolhidas, com os acréscimos do ponto 33.

**Parte B**
1. D3-75 sem [TS]: correto. O erro está na consequência ("razão pela qual dependem"), não na troca de um elemento do dispositivo; [TS] da folha fica em 5.
2. D3-72 (texto superado): admitido. É o único item da folha com essa feição (ficha 3.2), e a justificativa registra a superação pela Lei 14.230/2021 com base na letra vigente. AP.
3. D3-76 como único [TS] C: correto (isca "só" literal).
4. D3-79 e o nome "acordo de não persecução civil": a expressão é letra do caput do art. 17-B, usada só para nomear o acordo; o item não afirma nada do caput além do nome, e a base é o § 1º, II, que não está bloqueado. A ficha 5.2 (tópico 8) usa o mesmo nome. AP.
5. D3-74 e o dolo: o item não diz que há improbidade, mas o cenário ("determinada autoridade nomeante" em órgão do Legislativo) admite a leitura de nomeação por detentor de mandato eletivo, que o art. 11, § 5º, trata à parte, e não traz o dolo que o caput exige. AJ com texto exato (3.1, n. 9).
6. Tópico 6 com um só item e tópico 10 sem item: aceitos pela ficha.
7. Estrutura (seção 8 e linha final): correta.

## 7. Gate (checklist 7)
Reprovação 10/80 = 12,5% (Parte A 14,3%; Parte B 0%; folha mais alta, 6.3, com 30%). O limite é de 30% sobre os 80 itens (ficha 10, critério 8; 11.2). **Não há gate.** O ciclo segue para a v2.

## 8. Pontos para a v2 (a gcb-cpp responde item a item: acatado / não acatado + motivo)
**Itens com ajuste (texto exato em 3.1)**
1. D3-06: "matérias sobre as quais o Presidente dispõe mediante decreto".
2. D3-08: "à autoridade que delega ou que avoca"; troca reescrita.
3. D3-13: tirar da moldura o titular da competência; justificativa, linha 2.
4. D3-25: julgar só a ausência das prestadoras de direito privado; ponto de julgamento reescrito.
5. D3-26: tirar "objetiva" do enunciado.
6. D3-33: só os destinatários do regresso; sem "assegura/ressalva" e sem "culpa ou dolo"; campo "difere".
7. D3-66: sem a oração "pois…"; campo "difere" de D3-54.
8. D3-71: erro no rol ("exclusivamente nas hipóteses dos incisos" × "e notadamente"), e não na dispensa do dolo; ponto, justificativa, mecanismo e troca reescritos.
9. D3-74: servidor em cargo de direção como autoridade nomeante, nomeação dolosa.

**Itens reprovados (seção 3.2)**
10. D3-19: substituir (C; sugestão: CTN, art. 78, parágrafo único, desvio de poder em atividade discricionária). Sem substituto, a 5.2 fica com 9 itens, 4 C.
11. D3-31: substituir (C; sugestão: CC, art. 43, regresso condicionado a culpa ou dolo, só pela letra).
12. D3-39: substituir por ponto novo da 6.2 ou declarar a falta (ponto 30).
13. D3-42: substituir por ponto novo da 6.3 ou declarar a falta.
14. D3-48: substituir por ponto novo da 6.3 ou declarar a falta.
15. D3-50: substituir por ponto novo da 6.3 ou declarar a falta.
16. D3-57: substituir por ponto novo da 6.4 ou declarar a falta.
17. D3-60: substituir por ponto novo da 6.4 ou declarar a falta.
18. D3-65: substituir por ponto novo da 6.5 ou declarar a falta (sem a culpa exclusiva da vítima, ponto do BQ-0139).
19. D3-69: substituir por ponto novo da 6.5 ou declarar a falta (sem distinguir caso fortuito e força maior).

**Curso e resumo**
20. C6.2-03: tirar "a ser confirmado pelo R1"; pacificidade confirmada.
21. Curso C5.1-03 (exemplo) e C7-15 (exemplo): textos da seção 5.3.
22. Resumo do item 7: "ressalvados tipos previstos em leis especiais" (art. 1º, § 1º); tabela do art. 16, § 13, sem "impenhorabilidade" (seção 5.4).

**Contagens e sequência**
23. Refazer, depois dos pontos 8 e 10 a 19, as contagens por folha, por parte e do lote (C 4 a 6 por folha; 36 a 44 no lote; [TS] 40, 4 a 6 por folha; [TS] C ≤ 1 por folha; BASE DOUTRINÁRIA no teto; formatos; APL). Refazer também o teste da ficha 6.4 na sequência D3-01 a D3-80, com gabarito e marca [TS] e períodos 2 a 8. A emenda atual falha ("ECCE" ×3 em D3-64 a D3-75; "TnnT" em D3-64 a D3-74). A correção é da Parte B, dentro da folha 7, mantidos D3-71 e D3-72 = E (ficha 2.6, item 5).
24. Lista unificada dos 80 pontos de julgamento na v2, sem duplicata literal nem de sentido, com os pontos novos dos substitutos e os reescritos (D3-25 e D3-71).
25. Junção da v2 (orquestrador): gravar e usar saida/gcb/D3_juntar_v1.py (caminhos relativos; python3 -I). A junção deve sair no formato da ficha 2.6: linha 1 "# D3_v2.md — T-76 — [data] — gerado por gcb-cpp"; linha 2 da ficha; preâmbulo da A e "Parte B — convenções próprias"; tabela única em "## 3"; "## 7" com a linha "Lote", o teste das 80 posições e a lista unificada; "## 8" com "### Junção" (SHA-256 das partes e do arquivo juntado; conferências).
26. Proporção C das folhas: os 10 substitutos devem ser C, para manter 5 C/5 E por folha. Se faltar substituto, a parte declara a nova contagem e a GCB decide (ponto 30).

**Decisões da GCB (não da produtora)**
27. Reconhecer o padrão de reprovação (C espelho do E vizinho) e decidir se a v2 pode entregar folhas com menos de 10 itens nas folhas 6.2 a 6.5, já que o Anexo N e a lista fechada da 6.7 se esgotam nelas.
28. Folha 6.3: a ficha pede 10 itens, ao menos 2 pela letra e 4 tópicos doutrinários com no máximo 1 item cada. Com pontos distintos, o máximo possível é 6 ou 7. Decidir entre: (i) aceitar a 6.3 com 7 itens (2 C/5 E) e transferir o restante ao reforço; (ii) admitir mais de 1 item por tópico quando as proposições forem distintas e não se responderem (caso de D3-44/45, que a QA aprovou); (iii) ampliar a lista fechada com novo ponto pacífico, a ser conferido no R2.
29. D3-67: ratificar o ponto "excludente afasta; atenuante reduz" como BASE DOUTRINÁRIA admitida (está no par não obrigatório da ficha 5.3, mas não na lista da 6.7).
30. Substitutos sem ponto novo (6.2, 6.4 e 6.5): considerar antecipar para a v2 o adendo ao Anexo N previsto no registro da GCB, item 2 (dispositivos do Código Civil sobre caso fortuito ou força maior e sobre culpa concorrente da vítima, a verificar pelo qa-normativo-da), o que daria base de letra para itens C da 6.5 e reduziria a base doutrinária. Alternativa: aceitar folhas com 8 ou 9 itens.
31. Fichas futuras: não distribuir o mesmo trecho de lei curto (aqui, § 6º e art. 43) por várias folhas com tópicos sobrepostos (6.1 × 6.2 nos sujeitos; 6.4 × 6.5 na culpa), nem exigir 5 C por folha quando a base admite poucos pontos.

**Leitura crítica**
32. Ressalvas da seção 5.9 (cabeçalho, "Parte A/B" e frases de processo, "Base doutrinária:", script de geração ausente, hora e SHA-256 em TAREFAS.md). Não é condição do R2, porque o arquivo já foi entregue; vale para a regeneração, se a GCB a decidir depois da v2. A resposta externa, quando chegar, vai à v2 pelo saida/gcb/D3_acatamento_leitura_critica.md (ficha 9), com "QA PENDENTE"; o R2 confere.

**Notas à GBQ (para simulado; sem efeito no veredito)**
33. Não pôr no mesmo simulado: D3-07 com D3-13 e D3-18 (art. 49, V); D3-15, D3-17 e D3-20 com D1-32; D3-21 com D3-35; D3-22 com D3-21; D3-26 com D3-29 e D3-64; D3-28 com D3-30; D3-32 com D3-36 e com o substituto do D3-31; D3-41 com D3-49; D3-43, D3-44 e D3-45; D3-45 com D3-55; D3-51 com D3-58; D3-54 com D3-56 e D3-66; D3-61 com D3-67; D3-62 com D3-63; D3-71, D3-72 e D3-73 com BQ-0149 (dolo); D3-76 com BQ-0141; D3-77 com BQ-0140. D3-58 tem baixa discriminação: preferir em teste de lote a simulado.
34. Todos os itens continuam "QA PENDENTE" até o R2 e a reconciliação da GCB (D-QA-PENDENTE). Nada vai à plataforma nem à candidata.

FIM DO PARECER R1 — LOTE D3
