# qa_normativo_T07_2026-10-13.md — T-40 — 2026-10-13 — gerado por qa-normativo

## Escopo

- Tarefa: T-40 (TAREFAS.md). Faz o QA normativo dos 6 itens de fonte normativa da terceira varredura (T-07), conforme a D1 da GBQ em saida/banco/GBQ_reconciliacao_2026-10-10_lote2.md, seção 1.3. Os itens são BQ-0072, BQ-0077, BQ-0084, BQ-0109, BQ-0110 e BQ-0111.
- O gabarito não muda. Se houver divergência, recomenda-se GATILHO D à gbq-gerencia.
- O texto e o gabarito de cada item foram lidos em banco/banco.csv, somente para leitura. Nenhum arquivo do repositório foi editado além deste relatório.
- O texto normativo vai transcrito só aqui, por artigo, inciso e alínea, com as marcas do original.

## Fontes (todas do planalto.gov.br, abertas diretamente em 13/10/2026, por volta das 21h06 UTC)

As URLs foram localizadas por busca restrita a planalto.gov.br e abertas diretamente (curl, HTTP/1.1). As cópias locais estão no scratchpad t40/, fora do repositório.

| # | Diploma | URL usada | HTTP / bytes | SHA-256 da cópia |
|---|---|---|---|---|
| F1 | Lei 13.709/2018 (LGPD), texto compilado | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm | 200 / 230.913 | 20f3343c1d0e706594e61e3b8f273cbdd5e8ea755309241f02e8ab78f96c2ae2 |
| F2 | Lei 15.352/2026 (alteradora da LGPD) | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15352.htm | 200 / 164.468 | 0d22df2035f7629d43b1a644519c561adad7c43a8315824aeabf30281aa8c21e |
| F3 | Decreto 1.171/1994 (Código de Ética) | https://www.planalto.gov.br/ccivil_03/decreto/d1171.htm | 200 / 28.830 | dbb827a1618b7f11c8e0b748f027b82187c1425c6e3e5045d8a25cd2f36ef4ff |
| F4 | Lei 12.813/2013 (conflito de interesses) | https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/lei/l12813.htm | 200 / 28.347 | be87e93182d49486bbcfa375df84200f15733c968579d2dc429789255095c877 |
| F5 | Lei 14.129/2021 (Governo Digital) | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14129.htm | 200 / 141.539 | ad4f342c661c906d4b138f76be14bea28d17455621e13f081ae216bce5c4465e |

Registro de acesso:

- **Primeira tentativa.** Sem user-agent de navegador, as 5 URLs devolveram "curl: (52) Empty reply from server". Na segunda tentativa, com user-agent de navegador, todas abriram com HTTP 200. Nenhuma fonte deixou de abrir.
- **Páginas "compilado".** As variantes d1171compilado.htm e l14129compilado.htm foram testadas e devolveram HTTP 404, ou seja, não existem. Para o Decreto 1.171/1994 e para a Lei 14.129/2021, a página única do diploma é a versão mantida pelo Planalto. A página do Decreto traz as marcas "(Revogado pelo Decreto nº 6.029, de 2007)". A página da Lei 14.129 só traz marcas de veto e de promulgação de partes vetadas, sem nenhuma marca de alteração de redação.
- **SHA-256.** As páginas do Planalto embutem um script anti-robô (F5, "f5_cspm") com um token que varia a cada download, por isso o SHA-256 muda entre cópias. A F1 e a F2 foram comparadas, já sem esse token, com as cópias de 10/10/2026 da T-13 (scratchpad s3/t13/) e são **idênticas**. O texto da LGPD e o da Lei 15.352/2026 não mudaram entre 10/10 e 13/10/2026.
- Nada foi suprido de memória nem de fonte secundária.

### LGPD frente à Lei 15.352/2026 (F1 e F2, verificado em 13/10/2026)

- **O que a Lei 15.352/2026 alterou.** O art. 1º (F2) altera na LGPD apenas:
  - o art. 5º, VIII e XIX;
  - o Capítulo IX e a Seção I;
  - o art. 55-A;
  - o art. 55-C, V-A, V-B e VI.
- A vigência começa na data da publicação (art. 21; DOU de 25.2.2026, edição extra).
- **Marcas de alteração no compilado (F1):**
  - 13.853/2019: 16 "Redação dada" e 108 "Incluído";
  - 14.010/2020: 1 "Incluído";
  - 14.460/2022: 1 "Redação dada", 3 "Incluído" e 4 "Revogado";
  - 15.352/2026: 6 "Redação dada" e 1 "Incluído".
- **Aplicações das provas:** CTI em 28/1/2024; PF Administrativo e FUB em 29/06/2025, segundo a coluna observacoes. O único diploma alterador posterior a essas aplicações é a Lei 15.352/2026.
- **Dispositivos dos 4 itens de LGPD.** O art. 4º, o art. 5º, X e XVII, e o art. 11, II, "e", não têm marca de alteração. São de redação original, salvo o § 4º do art. 4º (Lei 13.853/2019), que não é decisivo.
- **Conclusão:** nenhuma alteração posterior à aplicação afeta o julgamento.

## Tabela-síntese

| id | dispositivo | sustenta gabarito | nota de vigência proposta | apto a simulado |
|---|---|---|---|---|
| BQ-0072 (C) | Decreto 1.171/1994, Anexo, Seção III, XV, "e" (comando: também Lei 12.813/2013, que não rege o item) | SIM | nenhuma | SIM (aderência DIRETA P1-6) |
| BQ-0077 (C) | LGPD, art. 5º, XVII | SIM | nenhuma | SIM, só diagnóstico (aderência PARCIAL, D-ADERENCIA) |
| BQ-0084 (C) | LGPD, art. 11, caput e II, "e" | SIM | nenhuma | SIM, só diagnóstico (aderência PARCIAL, D-ADERENCIA) |
| BQ-0109 (C) | LGPD, art. 5º, X | SIM | nenhuma | SIM, só diagnóstico (aderência PARCIAL, D-ADERENCIA) |
| BQ-0110 (E) | LGPD, art. 4º, caput, III, "a" e "b", §§ 1º a 3º | SIM | nenhuma no enunciado; na justificativa, se citar os §§ 2º e 3º: "Nota de vigência (verificado em 13/10/2026): a autoridade nacional referida no art. 4º, §§ 2º e 3º, é a Agência Nacional de Proteção de Dados (ANPD) — LGPD, art. 55-A e art. 5º, XIX, com redação da Lei nº 15.352/2026; o art. 4º não foi alterado." | SIM, só diagnóstico (aderência PARCIAL, D-ADERENCIA) |
| BQ-0111 (C) | Lei 14.129/2021, art. 3º, caput e V | SIM | nenhuma | SIM (aderência DIRETA P1-4) |

"Apto a simulado" responde só pelo QA normativo. As demais condições continuam com a GBQ: a restrição de aderência PARCIAL (D-ADERENCIA) e a dependência das colunas de comando para o pacote (T-42).

Divergências: **nenhuma**. Recomendação de GATILHO D: **nenhuma**.

## Análise por item (verificado em 13/10/2026)

### BQ-0072 — PF Administrativo 2025, it. 22 — gabarito C

**Item:** "Suponha que determinado servidor público, no exercício de suas funções, tenha deixado de utilizar recursos disponíveis de inteligência artificial institucionalmente autorizados. Nessa situação, a conduta praticada pelo servidor público pode configurar violação ao Código de Ética Profissional do Servidor Público."

**Comando:** cita o Decreto 1.171/1994 e a Lei 12.813/2013.

**Dispositivo (F3, Anexo, Capítulo I, Seção III, "Das Vedações ao Servidor Público").** Transcrição literal; o caput está grafado sem acento na página:

> XV - E [sic] vedado ao servidor público;
> [...]
> e) deixar de utilizar os avanços técnicos e científicos ao seu alcance ou do seu conhecimento para atendimento do seu mister;

**Dispositivo correlato (F3, Capítulo II), sem marca de revogação:**

> XXII - A pena aplicável ao servidor público pela Comissão de Ética é a de censura e sua fundamentação constará do respectivo parecer, assinado por todos os seus integrantes, com ciência do faltoso.

**Sustenta o C?** SIM. Deixar de usar recursos de IA autorizados e disponíveis é deixar de utilizar "os avanços técnicos e científicos ao seu alcance". A conduta é vedação expressa do Código, e o "pode configurar" do item é compatível com isso.

**Alteração após a aplicação (29/06/2025)?** Não houve. As únicas marcas da página são "(Revogado pelo Decreto nº 6.029, de 2007)", nos incisos XVII, XIX, XX, XXI, XXIII e XXV do Anexo, anteriores à aplicação e alheios ao item. O inciso XV, "e", tem a redação original de 1994.

**Lei 12.813/2013 (F4):**
- A lei rege o conflito de interesses no Poder Executivo federal. O art. 1º diz: "As situações que configuram conflito de interesses envolvendo ocupantes de cargo ou emprego no âmbito do Poder Executivo federal, [...] regulam-se pelo disposto nesta Lei."
- Nenhum dispositivo trata do uso de recursos técnicos ou tecnológicos. A busca no texto por "tecnol", "intelig", "técnic" e "cient" não achou ocorrência pertinente.
- Única marca na página: o art. 9º com "(Redação dada pela Medida Provisória nº 792, de 2017)" e "(Vigência encerrada)", com o texto original restabelecido. É anterior à aplicação e alheia ao item.
- A lei não interfere no gabarito.

**Nota de vigência:** nenhuma.

**Observação, sem pedido de mudança.** A ementa do decreto delimita o objeto: "Aprova o Código de Ética Profissional do Servidor Público Civil do Poder Executivo Federal." O comando da banca usa a forma abreviada "Código de Ética Profissional do Serviço Público". Isso não é questão de vigência. A aplicabilidade do Código aos servidores da Câmara dos Deputados não foi verificada aqui ([SEM FONTE — não afirmar]). A aderência já foi decidida em D1 pela GBQ.

### BQ-0077 — PF Administrativo 2025, it. 50 — gabarito C

**Item:** "Com base na Lei Geral de Proteção de Dados, considera-se relatório de impacto à proteção de dados pessoais a documentação do controlador que contém a descrição dos processos de tratamento de dados pessoais que podem gerar riscos às liberdades civis e aos direitos fundamentais, bem como medidas, salvaguardas e mecanismos de mitigação de riscos."

**Dispositivo (F1, art. 5º, caput e XVII):**

> Art. 5º Para os fins desta Lei, considera-se:
> [...]
> XVII - relatório de impacto à proteção de dados pessoais: documentação do controlador que contém a descrição dos processos de tratamento de dados pessoais que podem gerar riscos às liberdades civis e aos direitos fundamentais, bem como medidas, salvaguardas e mecanismos de mitigação de risco;

**Sustenta o C?** SIM. O item reproduz o inciso literalmente. A única diferença é "mitigação de riscos" (plural) no lugar de "mitigação de risco", sem efeito de sentido.

**Alteração após a aplicação (29/06/2025)?** Não houve. O inciso XVII não tem marca de alteração. No art. 5º, a Lei 15.352/2026 alterou só os incisos VIII e XIX.

**Nota de vigência:** nenhuma. O item não nomeia a ANPD.

### BQ-0084 — FUB 2025, it. 30 — gabarito C

**Item:** "Sendo indispensável para a proteção da vida ou da incolumidade física do titular, o tratamento de dados pessoais sensíveis pode ocorrer sem o prévio consentimento do titular."

**Dispositivo (F1, art. 11, caput, II, "e"):**

> Art. 11. O tratamento de dados pessoais sensíveis somente poderá ocorrer nas seguintes hipóteses:
> [...]
> II - sem fornecimento de consentimento do titular, nas hipóteses em que for indispensável para:
> [...]
> e) proteção da vida ou da incolumidade física do titular ou de terceiro;

**Sustenta o C?** SIM. A lei admite o tratamento de dado sensível "sem fornecimento de consentimento do titular" quando ele for indispensável à proteção da vida ou da incolumidade física "do titular ou de terceiro". O item cobra só a hipótese do titular, que está contida no texto legal.

**Alteração após a aplicação (29/06/2025)?** Não houve. A alínea "e" e o caput do inciso II não têm marca. No art. 11, a única marca é a da alínea "f", "(Redação dada pela Lei nº 13.853, de 2019)", anterior à aplicação e alheia ao item.

**Nota de vigência:** nenhuma.

### BQ-0109 — CTI 2023 (aplicação 28/1/2024), it. 38 — gabarito C

**Item:** "Conforme a LGPD, o tratamento de dados pessoais consiste em toda operação realizada com dados pessoais, como as que se refiram a coleta, produção, acesso, transmissão, processamento e eliminação desses dados."

**Dispositivo (F1, art. 5º, caput e X):**

> Art. 5º Para os fins desta Lei, considera-se:
> [...]
> X - tratamento: toda operação realizada com dados pessoais, como as que se referem a coleta, produção, recepção, classificação, utilização, acesso, reprodução, transmissão, distribuição, processamento, arquivamento, armazenamento, eliminação, avaliação ou controle da informação, modificação, comunicação, transferência, difusão ou extração;

**Sustenta o C?** SIM. A definição é a mesma ("toda operação realizada com dados pessoais"). O rol do inciso é exemplificativo ("como as que se referem a"). As seis operações que o item cita (coleta, produção, acesso, transmissão, processamento e eliminação) constam todas do inciso X. A troca de "referem" por "refiram" não altera o sentido.

**Alteração após a aplicação (28/1/2024)?** Não houve. O inciso X não tem marca de alteração.

**Nota de vigência:** nenhuma.

### BQ-0110 — CTI 2023 (aplicação 28/1/2024), it. 39 — gabarito E

**Item:** "A LGPD se aplica, entre outros casos, ao tratamento de dados realizado para fins exclusivos de segurança pública ou defesa nacional."

**Dispositivo (F1, art. 4º, caput, III, "a" e "b", §§ 1º a 3º):**

> Art. 4º Esta Lei não se aplica ao tratamento de dados pessoais:
> [...]
> III - realizado para fins exclusivos de:
> a) segurança pública;
> b) defesa nacional;
> [...]
> § 1º O tratamento de dados pessoais previsto no inciso III será regido por legislação específica, que deverá prever medidas proporcionais e estritamente necessárias ao atendimento do interesse público, observados o devido processo legal, os princípios gerais de proteção e os direitos do titular previstos nesta Lei.
> § 2º É vedado o tratamento dos dados a que se refere o inciso III do caput deste artigo por pessoa de direito privado, exceto em procedimentos sob tutela de pessoa jurídica de direito público, que serão objeto de informe específico à autoridade nacional e que deverão observar a limitação imposta no § 4º deste artigo.
> § 3º A autoridade nacional emitirá opiniões técnicas ou recomendações referentes às exceções previstas no inciso III do caput deste artigo e deverá solicitar aos responsáveis relatórios de impacto à proteção de dados pessoais.

**Sustenta o E?** SIM. O caput do art. 4º exclui expressamente da aplicação da LGPD o tratamento "realizado para fins exclusivos de" segurança pública (alínea "a") e defesa nacional (alínea "b"). O § 1º remete esse tratamento a "legislação específica". O item afirma o contrário.

A remissão do § 1º aos "princípios gerais de proteção e os direitos do titular previstos nesta Lei" não torna a LGPD aplicável. Ela orienta a legislação específica. Também não cria ambiguidade de gabarito.

**Alteração após a aplicação (28/1/2024)?** Não houve. O caput, o inciso III com as alíneas "a" e "b" e os §§ 1º a 3º não têm marca. O § 4º, "(Redação dada pela Lei nº 13.853, de 2019)", é anterior e não é decisivo. Isso confirma o registro do QA de banco da T-07 (10/10/2026).

**Ponto de contato indireto com a Lei 15.352/2026.** A "autoridade nacional" citada nos §§ 2º e 3º passou a ser definida no art. 5º, XIX, com redação da Lei 15.352/2026, como "entidade da administração pública responsável por zelar, implementar e fiscalizar o cumprimento desta Lei em todo o território nacional". O art. 55-A, na mesma redação, dispõe: "Fica criada a Agência Nacional de Proteção de Dados (ANPD), autarquia de natureza especial vinculada ao Ministério da Justiça e Segurança Pública [...]". O enunciado não menciona a autoridade, por isso o ponto não afeta o julgamento.

**Nota de vigência:**
- no enunciado: nenhuma;
- na justificativa ou no material de estudo, se ela citar os §§ 2º e 3º: o texto literal proposto na tabela-síntese, coerente com D-LEI-15352.

### BQ-0111 — CTI 2023 (aplicação 28/1/2024), it. 40 — gabarito C

**Item:** "O incentivo à participação social no controle e na fiscalização da administração pública está incluído entre os princípios e diretrizes do Governo Digital e da eficiência pública."

**Dispositivo (F5, art. 3º, caput e V):**

> Art. 3º São princípios e diretrizes do Governo Digital e da eficiência pública:
> [...]
> V - o incentivo à participação social no controle e na fiscalização da administração pública;

**Sustenta o C?** SIM. O item reproduz literalmente o inciso V e a expressão do caput ("princípios e diretrizes do Governo Digital e da eficiência pública").

**Alteração após a aplicação (28/1/2024)?** Não houve. A página da lei não traz nenhuma marca "Redação dada", "Incluído" ou "Revogado". As únicas marcas são de veto e de "Promulgação partes vetadas", e nenhuma delas toca o art. 3º, que vai do inciso I ao XXVI sem veto.

**Nota de vigência:** nenhuma.

## Recomendação para a coluna observacoes (aplicação pela gbq-gerencia)

Em cada uma das 6 linhas, substituir o trecho "aguarda qa-normativo (T-40); fora de simulado até a conclusão" pelo texto abaixo. O restante da célula fica como está; gabarito, texto_integral e demais colunas não mudam.

| id | substituir "aguarda qa-normativo (T-40); fora de simulado até a conclusão" por |
|---|---|
| BQ-0072 | `qa-normativo T-40: Decreto 1.171/1994, Anexo, XV, e (vedado deixar de utilizar os avanços técnicos e científicos), redação original, sustenta C; Lei 12.813/2013 não rege o item (verificado em 13/10/2026, planalto.gov.br)` |
| BQ-0077 | `qa-normativo T-40: LGPD art. 5º, XVII, sem alteração pela Lei 15.352/2026, sustenta C (verificado em 13/10/2026, planalto.gov.br, compilado)` |
| BQ-0084 | `qa-normativo T-40: LGPD art. 11, II, e, sem alteração pela Lei 15.352/2026, sustenta C (verificado em 13/10/2026, planalto.gov.br, compilado)` |
| BQ-0109 | `qa-normativo T-40: LGPD art. 5º, X (rol exemplificativo), sem alteração pela Lei 15.352/2026, sustenta C (verificado em 13/10/2026, planalto.gov.br, compilado)` |
| BQ-0110 | `qa-normativo T-40: LGPD art. 4º, III, a e b, §§ 1º a 3º, sem alteração pela Lei 15.352/2026, sustenta E; autoridade nacional dos §§ 2º e 3º = Agência Nacional de Proteção de Dados (ANPD), art. 55-A, red. Lei 15.352/2026 (verificado em 13/10/2026, planalto.gov.br, compilado)` |
| BQ-0111 | `qa-normativo T-40: Lei 14.129/2021, art. 3º, V, redação original, sustenta C (verificado em 13/10/2026, planalto.gov.br)` |

Notas de aplicação:

- **BQ-0110.** A célula já traz o segmento "QA de banco T-07: art. 4º, III, a e b, e §§ 1º a 3º sem alteração pela Lei 15.352/2026 (verificado em 2026-10-10)". O segmento é compatível com este QA e pode ficar ou ser absorvido pelo novo texto, a critério da gbq-gerencia, em D1.
- **Textos sem ";".** Os textos propostos não contêm ";" fora do separador interno já usado na célula. A célula é um campo entre aspas, e o csv.writer com QUOTE_MINIMAL preserva a citação.
- **Reverificação.** Os 4 itens de LGPD e o BQ-0111 não são VOLÁTIL, mas recomenda-se incluí-los na reverificação normativa da janela de 4–8/1/2027 (D-REVERIFICACAO-JAN), junto com os 17 itens da T-13, porque a LGPD foi alterada em 2026.

## Resumo

1. 6 itens conferidos: 6 SUSTENTA (SIM). Nenhuma divergência, nenhum NÃO VERIFICADO, nenhum GATILHO D.
2. A Lei 15.352/2026 não alterou nenhum dispositivo decisivo dos itens de LGPD (arts. 4º, 5º X e XVII, e 11 II "e"). Ela alterou só o art. 5º, VIII e XIX, o Capítulo IX, o art. 55-A e o art. 55-C. O texto da F1 e da F2 é idêntico às cópias de 10/10/2026.
3. Nota de vigência: só em BQ-0110, e só na justificativa (autoridade nacional = Agência Nacional de Proteção de Dados). Nas demais linhas, nenhuma.
4. BQ-0072 está sustentado pelo Decreto 1.171/1994, Anexo, XV, "e", na redação original. A Lei 12.813/2013, citada no comando, não rege o item.
5. BQ-0111 está sustentado pela Lei 14.129/2021, art. 3º, V, na redação original.
6. Os 6 itens ficam aptos a simulado quanto ao QA normativo. Os 4 de LGPD seguem só para diagnóstico (aderência PARCIAL, D-ADERENCIA).
