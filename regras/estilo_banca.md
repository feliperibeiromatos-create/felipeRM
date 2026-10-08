# estilo_banca.md — QUALIDADE-ESTILO etapa 2 — 2026-10-08 — gerado por gbq-estilo

## 1. Cabeçalho

- Versão: v1.0
- Data: 2026-10-08
- Base: 45 itens de 6 certames Cebraspe, todos APROVADOS no relatório de QA: TRF6 2024 (Cargo 2, Análise de Dados; aplicação 2025), BCB 2024 (Analista TI), ANATEL 2024 (Ciências de Dados), SUSEP 2025 (TI e Ciência de Dados), CNJ 2024 (Análise de Sistemas), ANTT 2023 (Cargo 1; aplicação 2024).
  - Dos 45, 3 são anulados (BQ-0029, BQ-0030, BQ-0031; gabarito X). Ficam fora da proporção C/E e da tipologia, pois sem gabarito não há mecanismo C/E a observar, e as justificativas de anulação não foram localizadas.
  - Base efetiva para proporção, tipologia e marcadores: 42 itens com gabarito C ou E.
- Status de QA da base: pós-QA. Fonte: saida/banco/qualidade_2026-10-09.md (etapa 1, gbq-cqe, rodada 1; 45 APROVADAS, 1 CORRIGIR). Texto literal e gabarito definitivo conferidos contra cdn.cebraspe.org.br.
  - Excluída: BQ-0025 (ANATEL it.84, gabarito E). Ficou em CORRIGIR só no campo observacoes, por não registrar a alteração C→E entre o gabarito preliminar e o definitivo. O gabarito E está correto. Ela não entra em nenhuma contagem deste guia, apenas nas notas.
- Fontes lidas (somente leitura): banco/banco.csv (separador ";", campos entre aspas respeitados; BQ-0043 tem ";" no texto), saida/banco/qualidade_2026-10-09.md, regras/estilo_banca_semente.md (só como referência) e edital/.
- Não há coluna de comando no CSV. A proporção por tipo de comando não foi calculada. Em seu lugar vai a proporção por subitem do edital, que é a coluna item_edital_camara.

## 2. Proporção C/E observada

Total (42 itens com gabarito): C = 24 (57,1%); E = 18 (42,9%). Anulados (fora): 3.

Por certame:

| Certame | itens aprovados | C | E | X (anulado) | %C / %E (sobre C+E) |
|---|---|---|---|---|---|
| TRF6 2024 | 12 | 7 | 5 | 0 | 58,3 / 41,7 |
| BCB 2024 | 5 | 3 | 2 | 0 | 60,0 / 40,0 |
| ANATEL 2024 | 7 (BQ-0025 excluída) | 3 | 4 | 0 | 42,9 / 57,1 |
| SUSEP 2025 | 7 | 3 | 1 | 3 | 75,0 / 25,0 |
| CNJ 2024 | 8 | 6 | 2 | 0 | 75,0 / 25,0 |
| ANTT 2023 | 6 | 2 | 4 | 0 | 33,3 / 66,7 |
| Total | 45 | 24 | 18 | 3 | 57,1 / 42,9 |

Por subitem do edital (mapeamento do banco; divergências do QA na seção 6):

| Subitem | C | E | X | Observação |
|---|---|---|---|---|
| P1-5.2 | 5 | 5 | 0 | aderência DIRETA |
| P1-5.3 | 3 | 3 | 0 | BQ-0009 e BQ-0015 têm leitura INDIRETA no QA |
| P1-6 | 0 | 2 | 0 | BQ-0016 INDIRETA; alternativa P2-4.2 para BQ-0016 e BQ-0040 |
| P1-7.1 | 0 | 1 | 2 | só 1 item válido |
| P1-8.1 | 2 | 1 | 0 | QA lê BQ-0001 como mais próxima de P1-8.2 |
| P1-8.3 | 2 | 0 | 0 | Grafana e Kibana, fora da lista do edital |
| P2-4.1 | 10 | 4 | 1 | todas INDIRETAS (LGPD geral; BQ-0036 é Marco Civil) |
| P2-4.3 | 2 | 2 | 0 | todas INDIRETAS (segurança geral) |
| P1 (soma) | 12 | 12 | 2 | |
| P2 (soma) | 12 | 6 | 1 | |

Leitura:
- A proporção fica próxima de metade/metade, com leve viés para C (57%).
- O viés vem de P2-4.1, onde a LGPD aparece com 10 C para 4 E. Em P1 a proporção é exatamente 12/12.
- Os certames variam muito (de 33% a 75% de C), e com n entre 4 e 12 por certame. Não force uma proporção por lote. Fixe uma faixa de 45% a 60% de C por lote e pare aí.

## 3. Tipologia de padrões

A classificação é feita por um mecanismo primário por item: cada um dos 42 itens entra em exatamente um padrão, e as somas fecham em 18 E e 24 C.

Percentuais:
- "% base" = sobre 42 itens.
- "% do grupo" = sobre 18 E ou sobre 24 C.

Traços transversais (podem coexistir com o padrão primário) ficam em 3.11.

### 3.1 [E1] Troca de conceito vizinho

- Definição: o enunciado atribui ao termo X a definição, a família ou a propriedade de um conceito vizinho Y da mesma área. O restante da frase é verdadeiro.
- Mecanismo: E. O erro está no núcleo, mas a frase toda soa técnica e coerente. Quem não domina o par X/Y aceita a afirmação.
- Itens:
  - BQ-0010 (E): IA generativa associada a aprendizado supervisionado, via "prioritariamente".
  - BQ-0015 (E): definição de outro objeto da API atribuída a "thread".
  - BQ-0018 (E): Naive Bayes enquadrado como aprendizado por reforço.
  - BQ-0039 (E): definição de não repúdio atribuída à autenticidade.
  - BQ-0043 (E): classificação enquadrada como não supervisionado.
  - BQ-0044 (E): limpeza de dados definida como "reorganização".
- Frequência: n = 6; 14,3% da base; 33,3% dos E. É o padrão E mais frequente.
- Subitens: P1-5.2 (BQ-0018, BQ-0043), P1-5.3 (BQ-0010, BQ-0015), P1-7.1 (BQ-0044), P2-4.3 (BQ-0039).

### 3.2 [E2] Inversão de definição ou de polaridade

- Definição: o conceito recebe o seu oposto. Exemplos: um princípio é descrito pela sua violação, um processo é descrito no sentido contrário, ou o par simétrico/assimétrico é trocado.
- Mecanismo: E. A frase mantém o vocabulário do conceito ("integridade", "governança e ética", "equilíbrio", "difusão"), mas o conteúdo diz o contrário.
- Itens:
  - BQ-0011 (E): integridade descrita como alteração sem registro.
  - BQ-0016 (E): opacidade apresentada como prática encorajada.
  - BQ-0022 (E): equilíbrio assimétrico descrito como distribuição uniforme.
  - BQ-0028 (E): geração por difusão descrita como aplicação de ruído, que é o sentido do treinamento, e não como sua remoção.
- Frequência: n = 4; 9,5% da base; 22,2% dos E.
- Subitens: P2-4.3 (BQ-0011), P1-6 (BQ-0016), P1-8.1 (BQ-0022), P1-5.3 (BQ-0028).
- Nota: a semente descreve BQ-0011 (TRF6 it.96) como "integridade definida como disponibilidade". O texto não sustenta essa leitura. O item define integridade pelo seu oposto (alteração sem registro), e não por outro princípio. Correção registrada.

### 3.3 [E3] Alteração do comando normativo

- Definição: em item sobre norma, a frase cria um dever inexistente, dispensa um dever existente, inventa prazo ou nega a consequência que a norma prevê.
- Mecanismo: E. Mantém o vocabulário e o tom da lei ("deve", "não será necessário", "não enseja") e muda o efeito jurídico. Costuma vir com justificativa verdadeira ou alternativa plausível.
- Itens:
  - BQ-0003 (E): dever de comunicação prévia à ANPD, com justificativa verdadeira após "pois".
  - BQ-0004 (E): dispensa de novo consentimento "de forma absoluta".
  - BQ-0023 (E): retenção por prazo fixo após o término do tratamento.
  - BQ-0040 (E): nega a descontinuidade prevista para viés não eliminável e oferece medidas corretivas como alternativa.
- Frequência: n = 4; 9,5% da base; 22,2% dos E.
- Subitens: P2-4.1 (BQ-0003, BQ-0004, BQ-0023), P1-6 (BQ-0040; leitura alternativa P2-4.2).
- A vigência das normas destes itens não foi verificada (ver seção 6).

### 3.4 [E4] Erro de escopo algoritmo × tarefa (INDÍCIO)

- Definição: nega uma aplicação que o algoritmo admite, ou estende a um par de algoritmos uma aplicação que só um deles admite.
- Mecanismo: E. Na enumeração ("tanto... quanto"), um elemento verdadeiro empresta credibilidade ao falso. Na negação, vem com causa falsa ("uma vez que").
- Itens:
  - BQ-0019 (E): KNN "não pode" classificar.
  - BQ-0042 (E): Naive Bayes e SVM "tanto na classificação quanto na regressão".
  - Contraste útil: BQ-0020 (C) afirma de SVM só o que é verdadeiro ("classificação ou regressão").
- Frequência: n = 2; 4,8% da base; 11,1% dos E. É INDÍCIO.
- Subitens: P1-5.2.

### 3.5 [E5] Cauda falsa: enunciado verdadeiro com exceção, ressalva ou consequência final falsa (INDÍCIO)

- Definição: a primeira parte da frase é verdadeira. Na parte final entra uma exceção ("excetuando-se..."), ressalva ou consequência ("não havendo...") que é falsa.
- Mecanismo: E. Quem lê confirma a primeira parte e relaxa. O erro está no último segmento.
- Itens:
  - BQ-0002 (E): exceção indevida quanto à identificação do controlador.
  - BQ-0041 (E): redução de dimensionalidade correta seguida de "não havendo... preservação da integridade".
- Frequência: n = 2; 4,8% da base; 11,1% dos E. É INDÍCIO.
- Subitens: P2-4.1 (BQ-0002), P1-5.2 (BQ-0041).

### 3.6 [C1] Definição ou descrição canônica correta

- Definição: descreve um conceito, técnica ou ferramenta como a literatura ou a documentação o descrevem, sem marcador de armadilha.
- Mecanismo: C por correção direta. Esses itens servem de âncora do caderno.
- Itens (todos C): BQ-0001, BQ-0008, BQ-0009, BQ-0013, BQ-0014, BQ-0017, BQ-0020, BQ-0026, BQ-0033, BQ-0035, BQ-0038.
- Frequência: n = 11; 26,2% da base; 45,8% dos C.
- Subitens: P1-5.2 (BQ-0013, BQ-0020, BQ-0026), P1-5.3 (BQ-0009, BQ-0014, BQ-0033), P1-8.1 (BQ-0001), P1-8.3 (BQ-0017, BQ-0035), P2-4.1 (BQ-0008), P2-4.3 (BQ-0038).

### 3.7 [C2] Reprodução próxima do texto normativo

- Definição: a frase reproduz, de forma literal ou quase literal, um princípio ou dispositivo de lei.
- Mecanismo: C. Quem conhece o texto da lei reconhece. Quem desconfia de frases longas e "bonitas" erra.
- Itens:
  - BQ-0006 (C): princípio da necessidade.
  - BQ-0024 (C): responsabilização e prestação de contas.
  - BQ-0036 (C): princípios do Marco Civil da Internet.
  - BQ-0037 (C): formato interoperável no poder público.
- Frequência: n = 4; 9,5% da base; 16,7% dos C.
- Subitens: P2-4.1. BQ-0036 é Marco Civil, e o QA a lê como INDIRETA.
- Nota: BQ-0006 contém "apenas" e é C (ver 3.11).

### 3.8 [C3] Item C redigido para parecer E

- Definição: o item é verdadeiro, mas carrega traço de superfície típico de item E. São eles: exceção ou dispensa, negação, "sem consentimento", concessiva ("mesmo que") ou "independe".
- Mecanismo: C. Pune quem marca E por reflexo diante de exceção ou negação.
- Itens (todos C):
  - BQ-0005: dispensa para dados manifestamente públicos.
  - BQ-0007: "não constitui a base legal mais apropriada".
  - BQ-0012: "mesmo que... sob pressão".
  - BQ-0027: "independe de rótulos".
  - BQ-0032: sensível "sem o consentimento".
  - BQ-0045: sensível "sem fornecimento de consentimento".
- Frequência: n = 6; 14,3% da base; 25,0% dos C. Ponto da semente confirmado.
- Subitens: P2-4.1 (BQ-0005, BQ-0007, BQ-0032, BQ-0045), P2-4.3 (BQ-0012), P1-5.2 (BQ-0027).

### 3.9 [C4] Item C com aparente estranheza semântica (INDÍCIO)

- Definição: o item é verdadeiro, mas combina ideias que parecem colidir. Exemplos: agrupamento usado para recomendação "individualizada"; "sobreposição" de elementos definindo seções implícitas.
- Mecanismo: C. Quem toma a estranheza por erro marca E.
- Itens: BQ-0021 (C), BQ-0034 (C).
- Frequência: n = 2; 4,8% da base; 8,3% dos C. É INDÍCIO.
- Subitens: P1-8.1 (BQ-0021), P1-5.2 (BQ-0034).

### 3.10 [C5] Paráfrase não literal de norma aceita como C (INDÍCIO; não usar como modelo)

- Definição: a frase resume a norma com palavras que não são as da lei e mesmo assim tem gabarito C.
- Item: BQ-0046 (C). O texto fala em "legislação equivalente". O QA anota que essa expressão difere da redação do art. 33, I, da LGPD.
- Frequência: n = 1; 2,4% da base; 4,2% dos C. É INDÍCIO.
- Subitem: P2-4.1.
- Pendente de qa-normativo. Não reproduzir esse tipo de item no AUTORAL, porque o gabarito depende da tolerância da banca, que não se pode prever.

### 3.11 Traços transversais (pontos da semente reavaliados)

Contagem nos 42 itens. Um item pode ter mais de um traço.

| Traço | Itens | Em quantos é a fonte do erro | Veredito |
|---|---|---|---|
| Termo absoluto ("sempre", "nunca", "apenas", "de forma absoluta", "exclusivamente/exclusivos") | BQ-0003 (E), BQ-0004 (E), BQ-0006 (C), BQ-0043 (E) | 1 (BQ-0004) | INDÍCIO |
| "prioritariamente" deslocando o núcleo | BQ-0010 (E) | 1 | INDÍCIO |
| Afirmação verdadeira com causa ou consequência falsa | BQ-0041 (E) | 1 | INDÍCIO |
| Nexo causal ou de finalidade como reforço | ver detalhe abaixo | — | traço, não padrão |
| Exceção/ressalva indevida | BQ-0002 (E) | 1 | INDÍCIO (dentro de E5) |
| Exceção/dispensa verdadeira | BQ-0005 (C) | — | dentro de C3 |
| Situação hipotética ("Considere que... Nessa situação") | BQ-0004 (E) | — | forma; n = 1 |

Detalhe por traço:
- Termo absoluto. "sempre", "nunca", "somente", "exclusivamente" e "em qualquer hipótese" têm 0 ocorrências nos 42 textos. Em BQ-0003, "exclusivos" vem da própria lei e não é o erro. Em BQ-0043, o erro é a troca de conceito e não o "apenas". BQ-0006 tem "apenas" e é C. Fora da base, BQ-0025 (excluída, E) usa "só podem".
- Afirmação verdadeira com causa ou consequência falsa. A forma pura da semente (oração principal verdadeira com causa falsa) tem 0 itens. Só há consequência final falsa em BQ-0041, já classificada em E5. Em BQ-0003 ocorre o inverso: a causa ("pois...") é verdadeira e a afirmação principal é falsa.
- Nexo causal ou de finalidade como reforço. Aparece em BQ-0003 (E, "pois"), BQ-0016 (E, "para garantir"), BQ-0019 (E, "uma vez que"), BQ-0028 (E, "para otimizar") e BQ-0006 (C, "logo"). É veículo de erro em 4 E e aparece também em 1 C.
- Situação hipotética. Indica que nem todo item é "afirmação única" seca. BQ-0043 também une duas orações com ";".

## 4. Marcadores lexicais

Contagem no campo texto_integral dos 42 itens com gabarito. Taxa de base: 57,1% C / 42,9% E.

AVISO: correlação não é regra. Os n são pequenos, e o mesmo marcador aparece nos dois gabaritos. Nenhum marcador decide gabarito. Use a tabela para diagnosticar vieses de redação, nunca para "adivinhar" o gabarito nem para fabricar itens com gabarito previsível.

| Marcador | C | E | Itens |
|---|---|---|---|
| "consiste" (definição formal) | 0 | 3 | BQ-0010, BQ-0022, BQ-0044 |
| possibilidade afirmativa ("pode", "poderá", "permite", "é capaz de") | 8 | 1 | C: BQ-0001, 0017, 0020, 0021, 0032, 0033, 0035, 0045; E: BQ-0015 |
| possibilidade negada ("não pode") | 0 | 1 | BQ-0019 |
| dever ("deve", "devem", "deverão", "devendo-se") | 4 | 4 | C: BQ-0005, 0006, 0024, 0037; E: BQ-0002, 0003, 0023, 0040 |
| negação operativa ("não", excluídos termos técnicos como "não supervisionado", "não paramétrico", "não rotulados") | 3 | 5 | C: BQ-0006, 0007, 0038; E: BQ-0004, 0019, 0039, 0040, 0041 |
| "sem" | 2 | 2 | C: BQ-0032, 0045; E: BQ-0011, 0043 |
| concessiva ("mesmo que", "mesmo sob", "mesmo após") | 1 | 2 | C: BQ-0012; E: BQ-0011, 0023 |
| exceção/dispensa explícita ("excetuando-se", "dispensada") | 1 | 1 | C: BQ-0005; E: BQ-0002 |
| termo absoluto (ver 3.11) | 1 | 3 | C: BQ-0006; E: BQ-0003, 0004, 0043 |
| "independe", "independentemente" | 1 | 1 | C: BQ-0027; E: BQ-0022 |
| "prioritariamente" | 0 | 1 | BQ-0010 |
| conector causal ("pois", "uma vez que", "logo") | 1 | 2 | C: BQ-0006; E: BQ-0003, 0019 |
| finalidade explícita ("para garantir", "para otimizar", "com o objetivo de", "visa") | 0 | 4 | BQ-0016, 0018, 0028, 0039 |
| raiz "garant-" | 2 | 4 | C: BQ-0012, 0045; E: BQ-0011, 0016, 0039, 0044 |
| abertura por remissão à fonte ("Conforme", "De acordo com", "Segundo") | 5 | 2 | C: BQ-0006, 0032, 0036, 0037, 0045; E: BQ-0016, 0023 |
| enumeração "tanto... quanto" | 0 | 1 | BQ-0042 |
| abertura "Considere que" | 0 | 1 | BQ-0004 |

Leituras que a tabela permite, todas com n pequeno:
- A possibilidade afirmativa ("pode", "é capaz de") aparece quase só em C. A definição formal com "consiste" e a finalidade explícita aparecem só em E. A remissão "Conforme a LGPD" aparece mais em C.
- Negação, "sem", "deve", exceção e concessiva aparecem nos dois lados. Esses traços não discriminam, e C3 existe justamente para punir quem acha que discriminam.

## 5. Guia de redação AUTORAL

Regras gerais (valem para todos os padrões):
- Não copie nem parafraseie de perto itens da banca. Não reutilize o mesmo par de conceitos de um item-exemplo (por exemplo, integridade/alteração, Naive Bayes/reforço, KNN/classificação, assimétrico/simétrico), nem a mesma moldura sintática com troca de uma palavra. O que se reaproveita é o mecanismo, não o texto.
- Escreva primeiro a versão C verdadeira e verificada, com fonte. Só depois aplique o mecanismo para obter a versão E. Um erro por item, e um só.
- Marque [TS] quando houver troca sutil (E1, E2 e, quando couber, E4).
- Equilibre o lote entre 45% e 60% de C e inclua itens C3, para não treinar a candidata a marcar E diante de exceção ou negação.
- Não faça o marcador lexical coincidir sempre com o mesmo gabarito. Exemplos: escreva itens E com "pode" e itens C com "consiste".
- Norma: só a partir de texto do planalto.gov.br verificado pelo qa-normativo, com data. Ferramenta: só com fonte datada do fornecedor. Sem fonte, o item vai para "pendente".
- Os exemplos abaixo são esqueletos ilustrativos, não itens aprovados. Todos passam por QA antes de qualquer uso.

### E1 — Troca de conceito vizinho
1. Escolha um par de conceitos que a candidata pode confundir (precisão × revocação; histograma × gráfico de barras; few-shot × ajuste fino; WER × CER).
2. Escreva a definição correta de um deles e atribua-a ao nome do outro. Mantenha o resto da frase verdadeiro.

Exemplos:
- "A revocação de um classificador indica a fração das previsões positivas que de fato pertencem à classe positiva." (E; descreve precisão) [TS]
- "No histograma, cada barra corresponde a uma categoria independente, de modo que a ordem das barras pode ser alterada sem prejuízo da leitura." (E; descreve gráfico de barras) [TS]

### E2 — Inversão de definição ou de polaridade
1. Tome uma definição com direção clara (treino × teste; entrada × saída; aumento × redução).
2. Inverta a direção e conserve o vocabulário.

Exemplo:
- "Diz-se que há sobreajuste quando o modelo erra muito nos dados de treino, mas acerta bem em dados novos." (E; a relação está invertida) [TS]

### E3 — Alteração do comando normativo
1. Parta do artigo verificado (texto vigente, data da consulta).
2. Altere uma só peça do comando: o sujeito obrigado, o verbo deôntico (deve ↔ pode), a condição, o prazo ou a consequência. Se quiser, acrescente uma justificativa verdadeira com "pois", como faz a banca.
3. Não use números ou prazos que não estejam no artigo verificado. Esqueleto: "Conforme [norma], [sujeito] [verbo deôntico alterado] [objeto], pois [razão verdadeira]."
4. Sem verificação do qa-normativo, o item não sai.

### E4 — Erro de escopo algoritmo × tarefa (INDÍCIO; usar com parcimônia)
1. Liste algoritmos e as tarefas que admitem.
2. Crie uma enumeração em que um elemento admite a tarefa e o outro não, ou negue uma tarefa que o algoritmo admite.

Exemplo:
- "Regressão linear e k-means são exemplos de algoritmos que aprendem a partir de exemplos rotulados." (E; k-means é não supervisionado)

### E5 — Cauda falsa (INDÍCIO)
1. Escreva uma frase verdadeira completa.
2. Acrescente ao final uma consequência, exceção ou ressalva falsa, introduzida por "razão pela qual", "excetuando-se" ou "não havendo".

Exemplo:
- "A taxa de erro de palavras (WER) soma substituições, omissões e inserções e divide o total pelo número de palavras da transcrição de referência, razão pela qual nunca ultrapassa 100%." (E; inserções podem levar a WER acima de 100%)

### C1 — Definição canônica correta
1. Escreva a definição de referência com suas palavras, sem palavra-armadilha, a partir de fonte verificada.

Exemplo:
- "Na validação cruzada k-fold, cada observação é usada para validação exatamente uma vez." (C)

### C2 — Reprodução próxima do texto normativo
1. Use o texto vigente do artigo, verificado pelo qa-normativo, e cite o artigo na justificativa.
2. Prefira dispositivos ligados ao edital (LGPD aplicada a sistemas de transcrição e IA).
3. Não faça paráfrase solta, para não cair em C5.

### C3 — Item C que parece E
1. Escolha uma regra verdadeira que contenha exceção, negação ou concessiva.
2. Exponha esse traço na frase.

Exemplos:
- "Mesmo sem dispor de rótulos, é possível avaliar um agrupamento por métricas internas, como o coeficiente de silhueta." (C)
- "Instruções explícitas de formato no prompt não garantem, por si sós, que o modelo produza a saída no formato pedido." (C)

### C4 — Estranheza aparente (INDÍCIO)
1. Combine duas ideias que parecem colidir, mas são compatíveis.

Exemplo:
- "Um box plot pode ocultar que a distribuição dos dados é bimodal." (C)

### Indícios da semente (usar com parcimônia, nunca como fórmula)
- "prioritariamente" deslocando o núcleo. Exemplo: "No few-shot prompting, o modelo se adapta à tarefa prioritariamente pelo ajuste de seus pesos a partir dos exemplos incluídos no prompt." (E; few-shot atua no contexto, sem atualizar pesos) [TS]
- Termo absoluto. Produza tanto E quanto C, porque a base tem "apenas" em item C (BQ-0006). Exemplo de C: "Na divisão holdout simples, cada observação pertence a apenas um dos subconjuntos, treino ou teste." (C)

## 6. Ressalvas

1. Padrões com menos de 3 ocorrências são INDÍCIO, não regra: E4 (n = 2), E5 (n = 2), C4 (n = 2), C5 (n = 1). Também são indícios os traços "termo absoluto como fonte de erro" (1), "prioritariamente" (1) e "verdadeira com consequência falsa" (1).
2. A base é pequena: 42 itens com gabarito, de 4 a 12 por certame. Todos os percentuais têm margem larga. A classificação por mecanismo primário é julgamento desta coordenação e deve ser revista na próxima versão do banco.
3. Subitens sem análogo real na base, onde o guia é extrapolação:
   - P1-5.1. Só a leitura alternativa de BQ-0014.
   - P1-8.2. Só a leitura do QA para BQ-0001, que é INDIRETA.
   - P1-8.4.
   - P2-1.x, P2-2.x, P2-3.x.
   - P2-4.2. Só as leituras alternativas INDIRETAS de BQ-0016 e BQ-0040.

   Também não há análogo direto em:
   - P1-8.3: Grafana e Kibana estão fora da lista do edital.
   - P2-4.1 e P2-4.3: todos os itens são INDIRETOS (LGPD e segurança em geral, não aplicadas a transcrição, IA ou pipelines de áudio).
   - P1-6: BQ-0016 é INDIRETA.
   - P1-7.1: 1 item válido.
4. Divergências de aderência do relatório de QA, consideradas nas contagens por subitem. As contagens usam o mapeamento do banco, e a leitura do QA vai anotada.
   - BQ-0001: banco P1-8.1; QA P1-8.2, INDIRETA.
   - BQ-0009: banco P1-5.3; QA INDIRETA, mais próxima de P1-5 ou 5.2.
   - BQ-0014: P1-5.3 DIRETA; leitura possível em 5.1.
   - BQ-0015: P1-5.3; QA INDIRETA, conceito de API de fornecedor.
   - BQ-0016: P1-6; QA INDIRETA, alternativa P2-4.2.
   - BQ-0036: P2-4.1; QA INDIRETA, é Marco Civil.
   - BQ-0040: P1-6 DIRETA; alternativa P2-4.2.
5. Vigência e fonte não verificadas. O relatório de QA não verificou a vigência das normas citadas nos itens. É o caso dos itens de LGPD de provas de 2024/2025 (BQ-0002 a 0008, 0023, 0024, 0032, 0037, 0045, 0046; BQ-0003 menciona a ANPD, e regras/proveniencia.md registra alteração da LGPD pela Lei 15.352/2026), de BQ-0036 (Marco Civil) e de BQ-0040 (Resolução CNJ). Também não verificou afirmações sobre ferramentas em fonte do fornecedor (BQ-0014, BQ-0015, BQ-0017, BQ-0028, BQ-0035). Tudo isso fica pendente de qa-normativo e QA antes de qualquer uso pedagógico. Os mecanismos descritos aqui valem como estilo, não como conteúdo vigente.
6. Anulados (BQ-0029, BQ-0030, BQ-0031) e BQ-0025 ficam fora de todas as contagens. Justificativas de anulação ou alteração não localizadas. Nota sobre BQ-0025: o gabarito foi alterado de C para E no definitivo, e o item usa "só podem". Ela seria um quarto item com termo absoluto em E, mas não foi contada.
7. Não há coluna de comando no CSV, e a proporção por tipo de comando não foi calculada.
8. Pontos da semente:
   - Confirmados com n ≥ 3: troca sutil de conceito (E1); inversão de definição (E2, com correção do exemplo de BQ-0011); item correto literal de norma (C2); item C redigido para parecer E (C3); proporção próxima de metade.
   - Rebaixados a INDÍCIO: termo absoluto; "prioritariamente"; afirmação verdadeira com causa ou consequência falsa; exceção/ressalva indevida.
   - Padrões novos: alteração do comando normativo (E3), erro de escopo algoritmo × tarefa (E4), cauda falsa (E5), estranheza aparente (C4), paráfrase normativa aceita (C5).
   - A regra "Nunca: item que depende de versão de software" da semente continua válida para o AUTORAL.
