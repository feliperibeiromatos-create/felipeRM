# estilo_onda_F1.md — T-113 (ORDEM F, onda 1) — 2026-10-18 — gerado por gbq-estilo

Auditoria de estilo da onda 1 da ordem F (D-REFORCO-2, regra de auditoria de 10%). Destino: gce-gerencia (partes A a D) e gcb-gerencia (P1), que fecham a T-113.

Referências: regras/estilo_banca.md v1.1.3 (tipologia E1–E6 e C1–C6; marcadores, seção 4; recomendações, seção 5; extensão da base: C média 31,6, de 8 a 65; E média 34,7, de 19 a 62); regras/estilo_banca_semente.md; saida/banco/estilo_onda_4.md (recomendações 1 a 7 da seção 5, aqui conferidas).

Objeto, lido em modo somente leitura: saida/gce/T113_onda1_A_v2.md, _B_v2.md, _C_v2.md, _D_v2.md (101 itens aprovados de P2, conforme QA_T113_A/B/C/D_R2_2026-10-18_gce-cqfp.md; excluídos os ids vagos L2-R136, L2-R137, L2-R140 e L3-R101) e saida/gcb/T113_onda1_P1_v2.md (7 itens de P1-5.2, L4-R01 a R07, APROVADOS em QA_T113_P1_R2_2026-10-18_gcb-cqfp.md). Universo: 108 itens. Nenhum item foi alterado nem reescrito nos arquivos de produção.

**Resultado:** 11 itens auditados (10,2% do universo): 7 CONFORMES, 3 AJUSTE (texto), 1 NÃO CONFORME (L1-R140) = 9,1%. Não há GATE (limite de 30%). Gabarito do universo por contagem própria: 54 C / 54 E = 50,0%, dentro da faixa de 40% a 60%.

## 1. Amostra e critério

- **Universo:** 108 ids extraídos por script (`python -I`, somente leitura) da Parte 2 (enunciado) e da Parte 3 (gabarito) de cada arquivo de P2 e da Parte 4/4 do arquivo de P1. Todos têm gabarito.
- **Itens indicados (fixos, entram na amostra e na taxa):** L4-R06 (P1) e os pontos de API de fornecedor L1-R137 (Google Cloud Speech-to-Text), L1-R139 e L1-R140 (Azure Speech, API REST de áudio curto).
- **Sorteio reproduzível:** `rng = random.Random(20261113)` (semente distinta da 20261098 da onda 4); ids em ordem crescente por lote e número; um `rng.choice` por parte ainda não coberta pelos fixos, na ordem B, C, D; depois `rng.sample(restantes, 4)`.
  - etapa 1: L1-R167 (B), L1-R192 (C), L3-R108 (D);
  - etapa 2: L1-R151, L1-R182, L2-R141, L1-R133.
- **Composição:** A 5 (R133, R137, R139, R140, R151); B 2 (R167, R182); C 2 (R192, L2-R141); D 1 (L3-R108); P1 1 (L4-R06). Gabarito: 6 C / 5 E; [TS] nos 5 E. Cobre as cinco partes.

Critérios (os das ondas 1 a 4): forma Cebraspe C/E ("Julgue o item"); enunciado assertivo, uma afirmação e um só ponto de erro; troca sutil real, de um único conceito, com mecanismo reconhecível na tipologia; ausência de pista textual que entregue o gabarito; extensão dentro do observado (O-1); registro formal, impessoal, sem moldura formular; cenário que pese no juízo. NÃO CONFORME: dois pontos de erro, [TS] com mais de uma troca, pista que entrega o gabarito, ou mecanismo sem paralelo na tipologia. AJUSTE (texto): defeito de estilo sanável por errata textual (D1), sem mudança de gabarito.

## 2. Vereditos por item

Palavras: só o enunciado, sem o comando.

| id | parte/folha | gab. | mecanismo (estilo_banca) | marcadores | palavras | veredito | motivo |
|---|---|---|---|---|---|---|---|
| L4-R06 | P1 / 5.2 | E [TS] | E1 em situação hipotética (agrupamento sem temas prévios → "supervisionado") | "Nessa situação" | 40 | CONFORME | Troca única do tipo de aprendizado; o cenário pesa (o dado "sem temas definidos antes" é o que decide), sem pista lexical: o enunciado não usa "rótulo", "cluster" nem "agrupamento não supervisionado". Observação: o L4-R04 tem a mesma moldura final ("Nessa situação, o treinamento descrito constitui exemplo de aprendizado não supervisionado") e o mesmo gabarito E; os dois não devem cair no mesmo simulado sem variar a abertura. |
| L1-R137 | A / 1.1 | C | C1 em situação hipotética (configuração da requisição descreve o áudio) | "realmente", "com exatidão", "De acordo com" | 65 | AJUSTE (texto) | Fiel a "will result in the most accurate transcription and billing for your request". Defeitos: (i) o cenário é decorativo — o juízo está todo na segunda frase, que é geral; (ii) "realmente adequados" e "com exatidão" reforçam a leitura de C (dupla marca de correção); (iii) 65 palavras, no teto dos C da base, contra a rec. 1 da onda 4. Texto proposto: "De acordo com a documentação do Google Cloud Speech-to-Text, descrever na configuração da requisição a codificação correta do áudio e usar o idioma e o modelo de reconhecimento corretos contribui para a transcrição mais precisa e para a cobrança correta da requisição." (40 palavras; gabarito C mantido.) |
| L1-R139 | A / 1.1 | C | C1/C2 (reprodução próxima da tabela RecognitionStatus) | "normalmente" | 49 | CONFORME | Uma afirmação, literal; "normalmente" respeita o "usually" da fonte e não é marcador de C (é a ressalva da própria base). Observação: R139 e R140 abrem com a mesma frase ("Na API REST de reconhecimento de áudio curto do Azure Speech") e saem da mesma tabela; gabaritos opostos, sem pista, mas não devem cair no mesmo simulado. |
| L1-R140 | A / 1.1 | E [TS] | E2 (inversão dentro do par: silêncio ↔ ruído entre dois status) | "somente" (2x), "ao passo que" | 51 | NÃO CONFORME | A troca é única, mas o próprio identificador entrega o gabarito: o status chamado Initial**Silence**Timeout é dito "somente ruído". Quem lê o nome resolve o item sem conhecer a documentação (Babble = balbucio/ruído). É pista textual que entrega a resposta, critério de NÃO CONFORME. Não há errata textual que preserve o ponto sem a pista enquanto os nomes dos status estiverem no enunciado; volta à produção (gce-cpp) para substituição do ponto ou nova construção de E cuja troca não seja dedutível do nome, com QA. Não é matéria de fidelidade: a base confere. |
| L1-R167 | B / 1.4 | E [TS] | E1 (troca de métrica: WDER → WER) com conclusão derivada | "Segundo", "de modo que", "não adota" | 37 | AJUSTE (texto) | O erro de base é um só (WER no lugar de WDER), e a oração "de modo que o serviço não adota métrica específica para a atribuição das palavras aos falantes" é consequência falsa dele: cadeia premissa falsa + conclusão falsa, que a rec. 6 da onda 4 pediu para evitar (dobra a superfície de recurso, e a negação forte inclina para E). Texto proposto: "Segundo a nota de transparência do Azure Speech, a qualidade da diarização é medida pela taxa de erro de palavras (WER)." (20 palavras; gabarito E e [TS] mantidos.) |
| L1-R192 | C / 1.7 | C | C2 (reprodução próxima do guia do Amazon Transcribe) | "Segundo", "como" (exemplos) | 48 | CONFORME | Uma afirmação, fiel a "breaks up the incoming audio stream based on natural speech segments, such as a change in speaker or a pause"; os exemplos vêm da fonte com "como", sem marca de exclusividade. Discriminação moderada (C de reprodução). |
| L3-R108 | D / 4.1 | E [TS] | E1 (troca de princípio vizinho: não discriminação → prevenção, LGPD art. 6º, IX × VIII) | "Nessa situação, segundo a Lei…" | 43 | AJUSTE (texto) | Troca única e legítima (forma corrente da banca nos princípios da LGPD). Defeitos: o cenário ("órgão público… classificar as falas de audiências públicas") não pesa no juízo, e a moldura "Nessa situação, segundo a Lei…" é a que a rec. 2 da onda 4 pediu para variar (13 itens do universo a usam, seção 4). Texto proposto: "Segundo a Lei Geral de Proteção de Dados Pessoais, o princípio da prevenção corresponde à impossibilidade de realização do tratamento para fins discriminatórios ilícitos ou abusivos." (25 palavras; gabarito E e [TS] mantidos.) O PENDENTE NORMATIVO não é matéria de estilo. |
| L1-R151 | A / 1.2 | C | C2 (reprodução próxima do resumo do wav2vec 2.0) | — | 31 | CONFORME | Uma afirmação, literal ao resumo; extensão igual à média de C da base; sem marcador. C técnico de memória, sem pista. |
| L1-R182 | B / 1.6 | E [TS] | E2 em situação hipotética (detecção única nos primeiros 30 s → "a cada janela de 30 segundos") | "Se", "segundo", "o que faz" | 56 | CONFORME | O cenário pesa (troca de idioma no meio da sessão é o que torna o ponto decisivo); a conclusão ("transcrito como espanhol") é a aplicação do ponto ao cenário, e não um segundo erro independente. Troca única, sem termo forte. Extensão no alto dos E, o que vai no sentido da rec. 1 da onda 4 (E longos). |
| L2-R141 | C / 2.1 | C | C2 (reprodução de reportagem institucional; ordem das etapas) | "Segundo", "por fim" | 30 | CONFORME | Uma afirmação, literal à Agência Senado. Observação: C de sequência, de discriminação baixa (a ordem transcrição → revisão → montagem é intuitiva); é o tipo que a rec. 7 da onda 4 pediu para elevar. Sem defeito de estilo. |
| L1-R133 | A / 1.1 | C | C1 com dado numérico (xRT = decodificação ÷ gravação) | "Segundo", "pode" | 40 | CONFORME | Duas frases, um juízo (a conta 6 ÷ 2 = 3 aplica a definição). Reproduz o exemplo da própria fonte, o que favorece memória sobre compreensão; risco baixo. "pode" num C, viés registrado na seção 4. |

Taxa de NÃO CONFORME da amostra: 1/11 = 9,1%, abaixo do gate de 30%. AJUSTE (texto) em 3/11 (R137, R167, L3-R108), sem mudança de gabarito. Dos 4 itens indicados: L4-R06 e L1-R139 CONFORMES; L1-R137 AJUSTE; L1-R140 NÃO CONFORME.

Achado lateral, fora da amostra e sem veredito: o L1-R136 (difone × trifone, E [TS]) usa troca entre nomes de raiz transparente ("di-", "tri-"); a pista é mais fraca que a do R140, mas a gce-gerencia pode pedir à QA que o examine pelo mesmo critério.

## 3. Faixa de C (regra 5), por contagem própria

| parte | arquivo | itens | C | E | %C | [TS] |
|---|---|---|---|---|---|---|
| A | T113_onda1_A_v2.md | 30 | 16 | 14 | 53,3 | 14 |
| B | T113_onda1_B_v2.md | 30 | 13 | 17 | 43,3 | 16 |
| C (sem R136, R137, R140) | T113_onda1_C_v2.md | 27 | 14 | 13 | 51,9 | 13 |
| D (sem R101) | T113_onda1_D_v2.md | 14 | 7 | 7 | 50,0 | 8 |
| P1 | T113_onda1_P1_v2.md | 7 | 4 | 3 | 57,1 | 3 |
| Onda F1 | 5 arquivos | 108 | 54 | 54 | 50,0 | 54 |

- Todas as partes dentro de 40% a 60%. A parte A confere com a declaração da produção (16 C / 14 E; 14 [TS]).
- [TS] em C (espelho): 1 (L3-R97); os demais [TS] estão em E. Itens E sem [TS]: L1-R168 (B).

## 4. Conferências das recomendações da onda 4 e marcadores

Método: expressão regular sem distinção de maiúsculas sobre os 108 enunciados; um item conta uma vez. AVISO da seção 4 do estilo_banca: nenhum marcador decide o gabarito.

| ponto | situação na onda F1 | avaliação |
|---|---|---|
| Rec. 1: extensão (O-1) | C: média 51,3, de 23 a 77; E: média 42,6, de 19 a 69 (+8,7 para C). Por parte (C × E): A 46,6 × 37,6; B 53,5 × 42,9; C 54,0 × 47,5; D 55,9 × 47,9; P1 45,8 × 30,7. C acima de 65 (teto da base): L1-R165 (74), R169 (77), R200 (67), L2-R138 (72), L3-R103 (71). | NÃO CUMPRIDO. A diferença a favor dos C dobrou (+4,2 na onda 4) e aparece nas cinco partes, o inverso da base (31,6 × 34,7). É o sinal que o O-1 pediu para não criar: "o mais longo é C". Sem efeito sobre os itens; na onda 2, aparar os cinco C acima de 65 e escrever E longos. |
| Rec. 2: moldura "Nessa situação, segundo a Lei…" e aberturas vizinhas | "Nessa situação": 21 itens (9 C, 12 E), concentrados em B (11) e D (7); "Nessa situação, segundo": 13 (R162, R164, R168, R169, R170, R174, R177, R184, R185, R190, L3-R106, R107, R108). Aberturas repetidas: "Segundo a nota de transparência do Azure Speech," (3), "Na API REST de reconhecimento de áudio curto" (2: R139 C × R140 E), "Segundo o artigo de pesquisa que apresenta o" (2). | NÃO CUMPRIDO. A moldura migrou da parte C da onda 4 para as partes B e D; distribuição C/E equilibrada, sem pista, mas formular. |
| Rec. 3: cenário que pese | Na amostra, cenário decorativo em R137 e L3-R108; pesa em L4-R06 e R182. "Uma equipe…" voltou: 17 itens (11 C, 6 E), depois de 0 na onda 4. | PARCIALMENTE CUMPRIDO. "Uma equipe" é a moldura formular que a onda 3 marcou; pende para C (65%). |
| Rec. 4: um restritivo por item | Na amostra, R140 tem "somente" duas vezes, por simetria do par (não é duplo restritivo sobre um mesmo ponto). Nenhum duplo restritivo nos demais 10. | CUMPRIDO na amostra. |
| Rec. 5: concessivas | "ainda que" 0; "embora" C 2 (R202, L2-R138), E 0; "mesmo que" 0. | Concessiva quase ausente e só em C; o desequilíbrio inverteu (onda 4: 2 C / 6 E). Sem efeito. |
| Rec. 6: cadeia premissa falsa + conclusão falsa | R167 (amostra, AJUSTE). R182 tem conclusão aplicada ao cenário, aceita. "de modo que": C 2, E 2. | PARCIALMENTE CUMPRIDO. |
| Rec. 7: discriminação dos C de lista/memória | L2-R141 (ordem de etapas) e R133 (exemplo da fonte) na amostra. | Persiste; sem defeito de estilo. |
| Contraste ", e não …" | C 3 (R134, R175, L3-R97), E 1 (R177). | Equilibrado; sem pista. |
| "ao passo que" | C 1 (L3-R102), E 8 (R136, R140, R141, R166, R197, R209, L2-R135, R142). | REGISTRO: 8 de 9 em E. É a moldura natural da inversão dentro de um par (E2), e por isso se acumula em E; na onda 4 estava 3 C / 3 E. Na onda 2, escrever C de par confundível com "ao passo que" (como o L3-R42 da onda 4). |
| Abertura "Segundo / De acordo com / Conforme" | C 10, E 20; na parte A, C 2 × E 9. | REGISTRO: na parte A, o E típico é curto e abre com "Segundo o artigo…" (média de E 37,6). Combinado com a extensão, forma perfil "curto + Segundo = E" na parte A. Sem efeito; variar. |
| Outros marcadores | "pode/podem/poderá": C 10, E 6. "apenas": C 6, E 3. "só": C 2, E 2. "somente": C 1, E 2. "todo/toda(s)": C 1, E 2. "qualquer": E 1 (R155). "sempre": E 1 (R148). "pois": C 4, E 4. "porque": C 2, E 1. "nunca", "exclusiv-", "prioritariamente", "independentemente", "mesmo que": 0. | Restritivos e causais nos dois gabaritos; "pois" equilibrado (rec. da seção 5.1 cumprida). "pode" segue com viés para C (62%, como nas ondas 3 e 4). Nenhum marcador decide o gabarito. |

## 5. Encaminhamento

- **À gce-gerencia (partes A a D):** auditoria concluída sem GATE (1/11 NÃO CONFORME = 9,1%). O L1-R140 é NÃO CONFORME por pista no identificador: proposta de retorno à gce-cpp para substituição ou nova construção, com QA, ou retirada com id vago, por D1 da Gerência. Erratas textuais (D1), sem mudança de gabarito, com o texto proposto na seção 2: L1-R137, L1-R167, L3-R108 (este, depois do parecer do qa-normativo). Exame opcional do L1-R136 pelo mesmo critério do R140.
- **À gcb-gerencia (P1):** L4-R06 CONFORME; nenhuma errata. Observação de moldura L4-R04 × L4-R06 para a montagem de simulado.
- **Recomendações à onda 2 da ordem F, sem efeito sobre os 108 itens:**
  1. inverter o sinal da extensão: aparar os C acima de 65 palavras (R165, R169, R200, L2-R138, L3-R103) e escrever E longos; a diferença atual é de +8,7 palavras para C;
  2. abandonar as molduras "Nessa situação, segundo a Lei…" (13) e "Uma equipe…" (17), e não abrir itens vizinhos da mesma fonte com a mesma frase (R139 × R140);
  3. em item de troca entre nomes ou identificadores (status, parâmetros, prefixos), verificar se o nome denuncia a definição; se denunciar, a troca deve incidir sobre outro elemento;
  4. usar "ao passo que" também em C de par confundível (hoje 1 C / 8 E);
  5. evitar a cadeia premissa falsa + conclusão negativa forte (R167);
  6. fazer o cenário pesar no juízo, ou dispensá-lo (R137, L3-R108).
- A incorporação destes registros a uma v1.1.4 do estilo_banca continua opção da GBQ, em tarefa própria.

AVISO: os vereditos e a atribuição de mecanismo são julgamento deste agente (gbq-estilo) e exigem revisão da GBQ. As contagens de C/E, [TS], extensão e marcadores vêm de script sobre os arquivos finais (`python -I`, somente leitura), com revisão manual dos casos citados; o [TS] de P1 foi lido da linha "[TS]: sim/não" de cada item. O sorteio é reproduzível com a semente e o procedimento da seção 1. A fidelidade às bases foi lida nos trechos literais transcritos no gabarito comentado; nenhuma página foi reaberta (matéria da QA e do qa-normativo).
