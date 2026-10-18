# QA_T98AC_normativo_2026-10-18_qa-normativo.md — T-98 — 2026-10-18 — gerado por qa-normativo

Objeto: conferência normativa da T-98, partes A e C.
- Parte A: saida/gce/L3_reforco_onda4_A_v1.md (L3-R12 a R39). Só um item cita norma, o L3-R12 (Ato da Mesa nº 251/2026, art. 7º, V). Conferi por busca no arquivo inteiro (Ato, RICD, Resolução, Lei, "art."): nenhum outro item, de R13 a R39, cita norma. A palavra "Constituição" do R21 ("proposta de emenda à Constituição") é o conteúdo de um mapa de sinônimos, não uma base normativa. Nenhum item da parte A cita o RICD.
- Parte C: saida/gce/L3_reforco_onda4_C_v1.md (L3-R68 a R95). São 19 itens de lei federal: R68 a R79 (Lei 9.610/1998) e R82, R83, R84, R86, R88, R90 e R92 (LGPD, Lei 13.709/2018). Os itens de fornecedor (R80, R81, R85, R87, R89, R91, R93, R94 e R95) estão fora do escopo.

Confiro os dispositivos citados no enunciado e no gabarito comentado. Nada foi reescrito.

Método: em 18/10/2026, abri as URLs diretamente com `curl -sL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"`. As URLs do planalto são as mesmas que foram localizadas e registradas em QA_T91_normativo_2026-10-18 e citadas nos próprios itens; não montei nenhuma URL de memória. Todas responderam HTTP 200. Converti o HTML do planalto de cp1252 e extraí o texto. As cópias estão só no scratchpad da sessão e não foram versionadas. Prefixos SHA-256 desta sessão: l9610 c4f09b3f…, l13709compilado 640d315f…, l13709 52fb8de5…, L15352 83684636…, Ato 251 (publicação original) 68aa4754…, Ato 251 (dados da norma) a0285a75…. Os prefixos diferem dos da T-91 porque as páginas são servidas de forma dinâmica; o texto dos dispositivos é o mesmo. Não usei fonte secundária nem memória.

## 1. Fontes e vigência

| fonte | URL | resultado em 18/10/2026 | vigência |
|---|---|---|---|
| Ato da Mesa nº 251, de 16/3/2026, publicação original (Legin) | https://www2.camara.leg.br/legin/int/atomes/2026/atodamesa-251-16-marco-2026-798819-publicacaooriginal-178493-cd-mesa.html | HTTP 200; art. 7º lido; "Este texto não substitui o original publicado no Diário da Câmara dos Deputados de 17/03/2026" | art. 12: "Este Ato entra em vigor na data de sua publicação." |
| Ato da Mesa nº 251/2026, Dados da Norma (Legin) | https://www2.camara.leg.br/legin/int/atomes/2026/atodamesa-251-16-marco-2026-798819-norma-cd-mesa.html | HTTP 200; "Situação: Não consta revogação expressa"; só há o link "Texto - Publicação Original"; indexação: "Departamento de Taquigrafia, Revisão e Redação (DETAQ) (1971-2026) - transformação - Departamento de Registro Oficial e Redação Parlamentar (DEREP)" | VIGENTE; nenhuma alteração nem revogação registrada |
| Lei 9.610/1998 (texto único do planalto, já com as alterações) | https://www.planalto.gov.br/ccivil_03/leis/l9610.htm | HTTP 200. As únicas leis alteradoras marcadas no texto são a 12.091/2009 (1 marca) e a 12.853/2013 (78 marcas). Nenhuma marca recai nos dispositivos conferidos | VIGENTE. Art. 114: "Esta Lei entra em vigor cento e vinte dias após sua publicação." Publicada no DOU de 20/2/1998. Os arts. 5º, VI e VIII, "h"; 7º, XIII e § 2º; 11; 14; 17; 18; 19; 24, § 2º; 37; 43; 47; e 49, III e V estão na redação original, sem "(Redação dada…)" |
| LGPD, texto compilado | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm | HTTP 200 | VIGENTE. Os arts. 44, 46, 48, 49 e 50 não têm nenhuma marca "(Redação dada…)", "(Incluído…)" ou "(Revogado…)", nem no compilado nem no texto com histórico |
| LGPD, texto com histórico (só para conferir) | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm | HTTP 200 | Os arts. 44, 46, 48, 49 e 50 não têm redação riscada nem nota de alteração |
| Lei 15.352, de 25/2/2026 (conversão da MP 1.317/2025) | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/L15352.htm | HTTP 200 | O art. 1º altera a LGPD em quatro pontos: art. 5º, VIII e XIX; Capítulo IX; arts. 55-A e 55-C. **Não altera os arts. 44, 46, 48, 49 e 50** |

Nomenclatura "Derep (antigo DETAQ)": CONFERE. A base é o art. 1º do Ato e a indexação do Legin.

## 2. Texto literal (verificado em 18/10/2026)

### 2.1 Ato da Mesa nº 251/2026, publicação original (URL na seção 1)

> Art. 3º O Departamento de Registro Oficial e Redação Parlamentar tem a seguinte estrutura administrativa:
> […]
> IV - Coordenação de Gestão do Discurso - Coged/Derep.

> Art. 7º Compete à Coordenação de Gestão do Discurso:
> I - gerir o processo de registro oficial e de redação final de reuniões de comissões e de outros eventos legislativos;
> II - organizar, supervisionar e elaborar roteiros;
> III - concatenar os textos legislativos resultantes da redação final de reuniões de comissões e demais eventos legislativos;
> IV - proceder ao tratamento dos discursos e reuniões registrados, bem como de seus respectivos metadados, e disponibilizá-los nas plataformas digitais pertinentes;
> V - sumarizar, indexar e tematizar os discursos e demais intervenções ocorridos em sessões plenárias, reuniões de comissões e outros eventos legislativos, vinculando os pronunciamentos às proposições legislativas;
> VI - sugerir termos para inclusão no vocabulário controlado da Câmara dos Deputados;
> VII - realizar atividades de pesquisa com base em discursos.

O texto não traz marcas "(Redação dada…)", porque é a publicação original e não há alteração registrada.

### 2.2 Lei 9.610/1998 — https://www.planalto.gov.br/ccivil_03/leis/l9610.htm

> Art. 5º Para os efeitos desta Lei, considera-se:
> […]
> VI - reprodução - a cópia de um ou vários exemplares de uma obra literária, artística ou científica ou de um fonograma, de qualquer forma tangível, incluindo qualquer armazenamento permanente ou temporário por meios eletrônicos ou qualquer outro meio de fixação que venha a ser desenvolvido;
> […]
> VIII - obra:
> […]
> h) coletiva - a criada por iniciativa, organização e responsabilidade de uma pessoa física ou jurídica, que a publica sob seu nome ou marca e que é constituída pela participação de diferentes autores, cujas contribuições se fundem numa criação autônoma;

> Art. 7º São obras intelectuais protegidas as criações do espírito, expressas por qualquer meio ou fixadas em qualquer suporte, tangível ou intangível, conhecido ou que se invente no futuro, tais como:
> […]
> XIII - as coletâneas ou compilações, antologias, enciclopédias, dicionários, bases de dados e outras obras, que, por sua seleção, organização ou disposição de seu conteúdo, constituam uma criação intelectual.
> […]
> § 2º A proteção concedida no inciso XIII não abarca os dados ou materiais em si mesmos e se entende sem prejuízo de quaisquer direitos autorais que subsistam a respeito dos dados ou materiais contidos nas obras.

> Art. 11. Autor é a pessoa física criadora de obra literária, artística ou científica.
> Parágrafo único. A proteção concedida ao autor poderá aplicar-se às pessoas jurídicas nos casos previstos nesta Lei.

> Art. 14. É titular de direitos de autor quem adapta, traduz, arranja ou orquestra obra caída no domínio público, não podendo opor-se a outra adaptação, arranjo, orquestração ou tradução, salvo se for cópia da sua.

> Art. 17. É assegurada a proteção às participações individuais em obras coletivas.
> § 1º Qualquer dos participantes, no exercício de seus direitos morais, poderá proibir que se indique ou anuncie seu nome na obra coletiva, sem prejuízo do direito de haver a remuneração contratada.
> § 2º Cabe ao organizador a titularidade dos direitos patrimoniais sobre o conjunto da obra coletiva.

> Art. 18. A proteção aos direitos de que trata esta Lei independe de registro.

> Art. 19. É facultado ao autor registrar a sua obra no órgão público definido no caput e no § 1º do art. 17 da Lei nº 5.988, de 14 de dezembro de 1973.

> Art. 24. São direitos morais do autor:
> […]
> § 1º Por morte do autor, transmitem-se a seus sucessores os direitos a que se referem os incisos I a IV.
> § 2º Compete ao Estado a defesa da integridade e autoria da obra caída em domínio público.

> Art. 37. A aquisição do original de uma obra, ou de exemplar, não confere ao adquirente qualquer dos direitos patrimoniais do autor, salvo convenção em contrário entre as partes e os casos previstos nesta Lei.

> Art. 41. Os direitos patrimoniais do autor perduram por setenta anos contados de 1° de janeiro do ano subseqüente ao de seu falecimento, obedecida a ordem sucessória da lei civil.

> Art. 43. Será de setenta anos o prazo de proteção aos direitos patrimoniais sobre as obras anônimas ou pseudônimas, contado de 1° de janeiro do ano imediatamente posterior ao da primeira publicação.
> Parágrafo único. Aplicar-se-á o disposto no art. 41 e seu parágrafo único, sempre que o autor se der a conhecer antes do termo do prazo previsto no caput deste artigo.

> Art. 47. São livres as paráfrases e paródias que não forem verdadeiras reproduções da obra originária nem lhe implicarem descrédito.

> Art. 49. Os direitos de autor poderão ser total ou parcialmente transferidos a terceiros, por ele ou por seus sucessores, a título universal ou singular, pessoalmente ou por meio de representantes com poderes especiais, por meio de licenciamento, concessão, cessão ou por outros meios admitidos em Direito, obedecidas as seguintes limitações:
> […]
> III - na hipótese de não haver estipulação contratual escrita, o prazo máximo será de cinco anos;
> […]
> V - a cessão só se operará para modalidades de utilização já existentes à data do contrato;

> Art. 114. Esta Lei entra em vigor cento e vinte dias após sua publicação.

Nenhum dos dispositivos acima traz marca de alteração.

### 2.3 LGPD, texto compilado — https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm

> Art. 44. O tratamento de dados pessoais será irregular quando deixar de observar a legislação ou quando não fornecer a segurança que o titular dele pode esperar, consideradas as circunstâncias relevantes, entre as quais:
> I - o modo pelo qual é realizado;
> II - o resultado e os riscos que razoavelmente dele se esperam;
> III - as técnicas de tratamento de dados pessoais disponíveis à época em que foi realizado.
> Parágrafo único. Responde pelos danos decorrentes da violação da segurança dos dados o controlador ou o operador que, ao deixar de adotar as medidas de segurança previstas no art. 46 desta Lei, der causa ao dano.

> Art. 46. Os agentes de tratamento devem adotar medidas de segurança, técnicas e administrativas aptas a proteger os dados pessoais de acessos não autorizados e de situações acidentais ou ilícitas de destruição, perda, alteração, comunicação ou qualquer forma de tratamento inadequado ou ilícito.
> § 1º A autoridade nacional poderá dispor sobre padrões técnicos mínimos para tornar aplicável o disposto no caput deste artigo, considerados a natureza das informações tratadas, as características específicas do tratamento e o estado atual da tecnologia, especialmente no caso de dados pessoais sensíveis, assim como os princípios previstos no caput do art. 6º desta Lei.

> Art. 48. […]
> § 2º A autoridade nacional verificará a gravidade do incidente e poderá, caso necessário para a salvaguarda dos direitos dos titulares, determinar ao controlador a adoção de providências, tais como:
> I - ampla divulgação do fato em meios de comunicação; e
> II - medidas para reverter ou mitigar os efeitos do incidente.
> § 3º No juízo de gravidade do incidente, será avaliada eventual comprovação de que foram adotadas medidas técnicas adequadas que tornem os dados pessoais afetados ininteligíveis, no âmbito e nos limites técnicos de seus serviços, para terceiros não autorizados a acessá-los.

> Art. 49. Os sistemas utilizados para o tratamento de dados pessoais devem ser estruturados de forma a atender aos requisitos de segurança, aos padrões de boas práticas e de governança e aos princípios gerais previstos nesta Lei e às demais normas regulamentares.

> Art. 50. Os controladores e operadores, no âmbito de suas competências, pelo tratamento de dados pessoais, individualmente ou por meio de associações, poderão formular regras de boas práticas e de governança que estabeleçam as condições de organização, o regime de funcionamento, os procedimentos, incluindo reclamações e petições de titulares, as normas de segurança, os padrões técnicos, as obrigações específicas para os diversos envolvidos no tratamento, as ações educativas, os mecanismos internos de supervisão e de mitigação de riscos e outros aspectos relacionados ao tratamento de dados pessoais.
> […]
> § 2º Na aplicação dos princípios indicados nos incisos VII e VIII do caput do art. 6º desta Lei, o controlador, observados a estrutura, a escala e o volume de suas operações, bem como a sensibilidade dos dados tratados e a probabilidade e a gravidade dos danos para os titulares dos dados, poderá:
> I - implementar programa de governança em privacidade que, no mínimo:
> […]
> g) conte com planos de resposta a incidentes e remediação; e

Os dispositivos sobre a ANPD (contexto da "autoridade nacional" dos itens R90 e R92) estão no mesmo texto compilado:

> Art. 5º […] XIX - autoridade nacional: entidade da administração pública responsável por zelar, implementar e fiscalizar o cumprimento desta Lei em todo o território nacional. (Redação dada pela Lei nº 15.352, de 2026)

> Art. 55-A. Fica criada a Agência Nacional de Proteção de Dados (ANPD), autarquia de natureza especial vinculada ao Ministério da Justiça e Segurança Pública, dotada de autonomia funcional, técnica, decisória, administrativa e financeira, com patrimônio próprio e com sede e foro no Distrito Federal, nos termos da Lei nº 13.848, de 25 de junho de 2019. (Redação dada pela Lei nº 15.352, de 2026)

## 3. Veredito por item

Todos os vereditos abaixo foram verificados em 18/10/2026.

| id | gab. | dispositivo(s) | veredito | nota |
|---|---|---|---|---|
| L3-R12 | E [TS] | Ato 251, art. 7º, V | CONFERE | A citação da justificativa é literal. O item troca o objeto da vinculação, "proposições legislativas", por "notas taquigráficas"; o restante do inciso está literal. |
| L3-R68 | C | L9610, art. 11, caput e parágrafo único | CONFERE | O item reproduz a regra e a exceção. |
| L3-R69 | E [TS] | L9610, art. 5º, VI | CONFERE | A lei diz "permanente ou temporário". O item exclui o armazenamento temporário. |
| L3-R70 | E [TS] | L9610, art. 43, caput (e art. 41) | CONFERE | O termo inicial é a primeira publicação, não o falecimento. O parágrafo único do art. 43, que remete ao art. 41 se o autor se der a conhecer, não salva o item, porque o item enuncia a regra geral. |
| L3-R71 | C | L9610, art. 49, III | CONFERE | "o prazo máximo será de cinco anos". |
| L3-R72 | E [TS] | L9610, art. 24, § 2º (e § 1º) | CONFERE | A defesa compete ao Estado. O § 1º, que transmite direitos aos sucessores, não abrange a obra em domínio público. |
| L3-R73 | E [TS] | L9610, art. 17, caput e § 2º; art. 5º, VIII, "h" | CONFERE | Cabe ao organizador a titularidade sobre o conjunto. Ressalva sem efeito no gabarito: o enunciado não diz que as contribuições "se fundem numa criação autônoma" (art. 5º, VIII, "h"), mas o conjunto não pertence "a cada participante" em nenhuma leitura. |
| L3-R74 | C | L9610, arts. 18 e 19 | CONFERE | A proteção independe de registro, e o registro é facultativo. |
| L3-R75 | E [TS] | L9610, art. 37 (e art. 29) | CONFERE | A aquisição não confere direitos patrimoniais. A digitalização e a divulgação dependem de autorização (art. 29, I). |
| L3-R76 | C [TS esp.] | L9610, art. 14 | CONFERE | O item reproduz as duas metades do artigo. A ressalva "salvo se for cópia da sua" não é julgada. |
| L3-R77 | C [TS esp.] | L9610, art. 49, V; art. 114 | CONFERE | O contrato de 1999 é posterior à vigência da lei (DOU de 20/2/1998, mais 120 dias). "Somente" equivale ao "só" da lei. |
| L3-R78 | E [TS] | L9610, art. 7º, XIII e § 2º | CONFERE | A proteção "não abarca os dados ou materiais em si mesmos". |
| L3-R79 | C | L9610, art. 47 | CONFERE | Literal. |
| L3-R82 | E [TS] | LGPD, art. 44, caput e III | CONFERE | O texto diz "à época em que foi realizado". O item troca por "em que o dano foi apurado". |
| L3-R83 | E [TS] | LGPD, art. 44, parágrafo único (reforço: art. 42, § 1º, I) | CONFERE | Responde "o controlador ou o operador". O "apenas o controlador" do item é falso. |
| L3-R84 | C [TS esp.] | LGPD, art. 49 | CONFERE | O item reproduz o rol. Omitir "às demais normas regulamentares" não torna o item falso. |
| L3-R86 | C | LGPD, art. 48, § 3º | CONFERE | O item reproduz o efeito, "será avaliada … no juízo de gravidade", sem afirmar dispensa da comunicação. |
| L3-R88 | E [TS] | LGPD, art. 50, § 2º, I, "g" | CONFERE | A lei diz que o controlador "poderá". O item diz "é obrigado". |
| L3-R90 | E [TS] | LGPD, art. 48, § 2º, I | CONFERE | A lei diz "poderá … determinar". O item diz "apenas recomendar". |
| L3-R92 | C [TS esp.] | LGPD, art. 46, § 1º | CONFERE, com ressalva de redação | A competência normativa dos "padrões técnicos mínimos" é da autoridade nacional, que hoje é a ANPD como Agência (arts. 5º, XIX, e 55-A, na redação da Lei 15.352/2026). Há risco de recurso: o art. 50, caput, permite a controladores e operadores formular regras de boas práticas que estabeleçam "os padrões técnicos", e o trecho "e não o controlador" pode ser contestado. O gabarito C se sustenta pelo art. 46, § 1º, porque o item trata dos padrões mínimos fixados pela autoridade. Cabe à gce-cqfp decidir se mantém o contraste. |

Resultado: 20 de 20 itens CONFERE (o R12 e os 19 itens de lei federal); nenhum DIVERGE. Há uma ressalva de redação, no R92.

## 4. Alterações recentes relevantes

- Lei 15.352, de 25/2/2026 (conversão da MP 1.317/2025): a ANPD passou a ser a Agência Nacional de Proteção de Dados, autarquia de natureza especial vinculada ao MJSP. A lei deu nova redação ao art. 5º, VIII e XIX, ao Capítulo IX e aos arts. 55-A e 55-C. Ela **não tocou** nos arts. 44, 46, 48, 49 e 50 da LGPD. Nenhum dos 7 itens de LGPD nomeia a ANPD; todos usam "autoridade nacional", que é o termo legal vigente (art. 5º, XIX). Se alguma versão futura nomear o órgão, deve escrever "Agência Nacional de Proteção de Dados (ANPD)", e não "Autoridade".
- Lei 9.610/1998: as últimas alterações marcadas no planalto são das Leis 12.091/2009 e 12.853/2013, e nenhuma delas recai nos dispositivos usados.
- Ato da Mesa nº 251/2026: não tem alteração nem revogação registrada. A conferência de base de 4 a 8/1/2027 prevista no R12 continua válida, sem efeito de VOLÁTIL.

## 5. Encaminhamento

Do ponto de vista normativo, os 20 itens podem perder a pendência de conferência normativa. A decisão é da gce-gerencia, e a edição, se houver, é da produção; eu não alterei os arquivos dos itens. A QA de estilo e mérito (gce-cqfp R1) e a aderência não são matéria deste parecer. Este registro vale para os dispositivos conferidos: se a v2 trocar de dispositivo ou de ponto de troca em algum item, esse item volta ao qa-normativo.

## Adendo v2 — L3-R80 e L3-R95 (18/10/2026)

Objeto: os dois itens novos de lei federal da v2 (saida/gce/L3_reforco_onda4_C_v2.md). Texto compilado aberto diretamente no planalto.gov.br em 18/10/2026, com User-Agent de navegador, HTTP 200 nas duas URLs. Não alterei a produção.

### Lei 9.610/1998, art. 46, III
URL: https://www.planalto.gov.br/ccivil_03/leis/l9610.htm — verificado em 18/10/2026.
Transcrição literal (caput e inciso III; o inciso não tem marcação de redação dada, inclusão ou revogação no original):
> Art. 46. Não constitui ofensa aos direitos autorais:
> (...)
> III - a citação em livros, jornais, revistas ou qualquer outro meio de comunicação, de passagens de qualquer obra, para fins de estudo, crítica ou polêmica, na medida justificada para o fim a atingir, indicando-se o nome do autor e a origem da obra;

### LGPD (Lei 13.709/2018), art. 37
URL: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm — verificado em 18/10/2026.
Transcrição literal (artigo de caput único, sem parágrafos nem incisos; sem marcação de redação dada no original):
> Art. 37. O controlador e o operador devem manter registro das operações de tratamento de dados pessoais que realizarem, especialmente quando baseado no legítimo interesse.

### Resultado

| id | gabarito | dispositivo | resultado | motivo |
|---|---|---|---|---|
| L3-R80 | C | Lei 9.610/1998, art. 46, III | CONFERE | O texto é o vigente e não tem redação alterada. O trecho citado na justificativa é igual à letra da lei. O enunciado traz as três condições do inciso: a finalidade (estudo, crítica ou polêmica), a medida justificada para o fim a atingir e a indicação do nome do autor e da origem da obra. O estudo técnico se encaixa em "qualquer outro meio de comunicação". O gabarito C é compatível com a lei. |
| L3-R95 | C | LGPD, art. 37 | CONFERE | O texto é o vigente e não tem redação alterada. O trecho citado é igual à letra da lei. O enunciado atribui o dever aos dois agentes, como faz o art. 37. A contratada que trata dados "em nome" da Câmara é operadora (art. 5º, VII). A omissão de "especialmente quando baseado no legítimo interesse" não muda o sentido, porque o dever é geral. O gabarito C é compatível com a lei. |

Alterações recentes: a Lei 15.352/2026 (a ANPD como Agência) não tocou no art. 37 da LGPD. O art. 46, III, da Lei 9.610/1998 não tem alteração registrada no compilado. Do ponto de vista normativo, R80 e R95 podem perder a marca PENDENTE NORMATIVO. A decisão é da gce-gerencia, e a QA PENDENTE (gce-cqfp) continua.
