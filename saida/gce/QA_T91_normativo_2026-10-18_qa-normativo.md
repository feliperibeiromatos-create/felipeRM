# QA_T91_normativo_2026-10-18_qa-normativo.md — T-91 — 2026-10-18 — gerado por qa-normativo

Objeto: conferência normativa de L3-R09, L3-R10 e L3-R11 (saida/gce/L3_reforco_onda1_v2.md, marcados "PENDENTE NORMATIVO") no texto vigente do planalto.gov.br. Considerei também o parecer saida/gce/QA_T91_R1_2026-10-18_gce-cqfp.md (nota de R10). Não reescrevo os itens.

## 1. Acesso às fontes (18/10/2026, por volta de 04:18 UTC; curl com User-Agent de navegador)

| Diploma | URL aberta | HTTP | Observação |
|---|---|---|---|
| Lei 9.610/1998 | https://www.planalto.gov.br/ccivil_03/leis/l9610.htm | 200 | Texto único do planalto, que já inclui as alterações (Leis 12.091/2009 e 12.853/2013); não há arquivo "compilado" separado. Art. 41 sem marca de alteração. |
| LGPD (texto compilado vigente) | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm | 200 | É o destino do link "Texto compilado" de l13709.htm. Serve de base literal abaixo. |
| LGPD (texto com histórico de redações) | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm | 200 | Usado só para conferir. Arts. 47 e 48 iguais ao compilado. |
| Lei 15.352/2026 | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/L15352.htm | 200 | Conversão da MP 1.317/2025. O art. 1º altera a LGPD (art. 5º, VIII e XIX; Capítulo IX; art. 55-A e seguintes). **Não altera os arts. 47 e 48.** |
| Res. CD/ANPD (prazo de comunicação de incidente) | https://www.in.gov.br/ (DOU) | falhou | "CONNECT tunnel failed, response 403" (proxy). Não aberta. |

Em 18/10/2026 o planalto respondeu 200, não 503 como antes. As cópias locais ficaram só no scratchpad da sessão (não versionadas). Prefixos SHA-256: l9610 53aa5a1a…, l13709compilado 49b41b71…, l13709 96173cd3…, L15352 9c2f58be….

## 2. Texto literal (verificado em 18/10/2026)

### 2.1 Lei 9.610/1998, art. 41 (L3-R09)
URL: https://www.planalto.gov.br/ccivil_03/leis/l9610.htm. Verificado em 18/10/2026.

> Art. 41. Os direitos patrimoniais do autor perduram por setenta anos contados de 1° de janeiro do ano subseqüente ao de seu falecimento, obedecida a ordem sucessória da lei civil.
>
> Parágrafo único. Aplica-se às obras póstumas o prazo de proteção a que alude o caput deste artigo.

O dispositivo não tem marca "(Redação dada…)" nem "(Incluído…)": é a redação original, vigente.

### 2.2 LGPD, art. 47 (L3-R11)
URL: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm. Verificado em 18/10/2026.

> Art. 47. Os agentes de tratamento ou qualquer outra pessoa que intervenha em uma das fases do tratamento obriga-se a garantir a segurança da informação prevista nesta Lei em relação aos dados pessoais, mesmo após o seu término.

Redação original, sem marca de alteração.

### 2.3 LGPD, art. 48, caput e §§ 1º a 3º (L3-R10)
URL: igual à de 2.2. Verificado em 18/10/2026.

> Art. 48. O controlador deverá comunicar à autoridade nacional e ao titular a ocorrência de incidente de segurança que possa acarretar risco ou dano relevante aos titulares.
>
> § 1º A comunicação será feita em prazo razoável, conforme definido pela autoridade nacional, e deverá mencionar, no mínimo:
>
> I - a descrição da natureza dos dados pessoais afetados;
>
> II - as informações sobre os titulares envolvidos;
>
> III - a indicação das medidas técnicas e de segurança utilizadas para a proteção dos dados, observados os segredos comercial e industrial;
>
> IV - os riscos relacionados ao incidente;
>
> V - os motivos da demora, no caso de a comunicação não ter sido imediata; e
>
> VI - as medidas que foram ou que serão adotadas para reverter ou mitigar os efeitos do prejuízo.
>
> § 2º A autoridade nacional verificará a gravidade do incidente e poderá, caso necessário para a salvaguarda dos direitos dos titulares, determinar ao controlador a adoção de providências, tais como:
>
> I - ampla divulgação do fato em meios de comunicação; e
>
> II - medidas para reverter ou mitigar os efeitos do incidente.
>
> § 3º No juízo de gravidade do incidente, será avaliada eventual comprovação de que foram adotadas medidas técnicas adequadas que tornem os dados pessoais afetados ininteligíveis, no âmbito e nos limites técnicos de seus serviços, para terceiros não autorizados a acessá-los.

Redação original, sem marca de alteração. A expressão "setenta e duas horas" não aparece no art. 48.

### 2.4 LGPD, dispositivos sobre a ANPD citados na proveniência de R10 (art. 5º, VIII e XIX; art. 55-A)
URL: igual à de 2.2. Verificado em 18/10/2026.

> VIII - encarregado: pessoa indicada pelo controlador e operador para atuar como canal de comunicação entre o controlador, os titulares dos dados e a Agência Nacional de Proteção de Dados (ANPD); (Redação dada pela Lei nº 15.352, de 2026)

> XIX - autoridade nacional: entidade da administração pública responsável por zelar, implementar e fiscalizar o cumprimento desta Lei em todo o território nacional. (Redação dada pela Lei nº 15.352, de 2026)

> Art. 55-A. Fica criada a Agência Nacional de Proteção de Dados (ANPD), autarquia de natureza especial vinculada ao Ministério da Justiça e Segurança Pública, dotada de autonomia funcional, técnica, decisória, administrativa e financeira, com patrimônio próprio e com sede e foro no Distrito Federal, nos termos da Lei nº 13.848, de 25 de junho de 2019. (Redação dada pela Lei nº 15.352, de 2026)
>
> § 1º (Revogado pela Lei nº 14.460, de 2022)
>
> § 2º (Revogado pela Lei nº 14.460, de 2022)
>
> § 3º (Revogado pela Lei nº 14.460, de 2022)

**Ressalva de grafia no original:** em l13709.htm (texto com histórico), a nota do art. 55-A diz "(Redação dada pela Lei nº 15.452, de 2026)". O hiperlink dessa nota aponta para L15352.htm#art1, e o texto compilado traz "15.352". Trata-se de erro de digitação do planalto. A lei correta é a **15.352/2026**. Não citar "15.452".

## 3. Veredito por item

| Item | Gabarito | Dispositivo | Veredito | Motivo |
|---|---|---|---|---|
| L3-R09 | C | Lei 9.610/1998, art. 41, caput e parágrafo único | **CONFERE** | O enunciado reproduz o caput (setenta anos; 1º de janeiro do ano subsequente ao falecimento; ordem sucessória da lei civil) e o parágrafo único (obras póstumas). Não há alteração legislativa. |
| L3-R10 | E [TS] | LGPD, art. 48, caput e § 1º | **CONFERE** | O § 1º diz "em prazo razoável, conforme definido pela autoridade nacional". A lei não fixa 72 horas, então "setenta e duas horas, fixado na própria lei" é falso. A Lei 15.352/2026 não tocou no art. 48; a "autoridade nacional" hoje é a ANPD como Agência (arts. 5º, XIX, e 55-A). |
| L3-R11 | E [TS] | LGPD, art. 47 | **CONFERE** | O dever de segurança vale "mesmo após o seu término". Dizer que ele "cessa" com o fim do contrato e do tratamento contradiz o texto. Sujeitos conferidos: agentes de tratamento "ou qualquer outra pessoa que intervenha em uma das fases do tratamento". Art. 47 sem alteração. |

## 4. Nota de R10: prazo regulamentar da ANPD
Continua **[SEM FONTE — não afirmar]**. A resolução do Conselho Diretor da ANPD que fixa o prazo de comunicação de incidente não foi aberta: in.gov.br deu "CONNECT tunnel failed, response 403" em 18/10/2026. A justificativa de R10 não cita prazo regulamentar, e assim deve ficar. O gabarito E não depende desse prazo: ele se sustenta só no art. 48, § 1º. Se um dia o item ou a justificativa mencionar o prazo da resolução, será preciso reconferir na fonte oficial (DOU ou gov.br/anpd).

## 5. Encaminhamento
- Os três itens têm o literal e o gabarito confirmados no planalto (texto vigente, 18/10/2026). Do ponto de vista normativo, cabe retirar a marca "PENDENTE NORMATIVO" de R09, R10 e R11, por decisão da gce-gerencia e com edição pela produção. Eu não altero o arquivo dos itens.
- A proveniência do lote (linhas da tabela com "planalto.gov.br com 503") deve ganhar as URLs do planalto acima com "verificado em 18/10/2026 (qa-normativo)".
- Alterações recentes relevantes: Lei 15.352/2026 (25/2/2026; conversão da MP 1.317/2025). Ela mudou a ANPD de "Autoridade" para "Agência Nacional de Proteção de Dados", autarquia especial vinculada ao MJSP, e deu nova redação ao art. 5º, VIII e XIX e ao art. 55-A. Nenhum dos três itens depende dela; R10 e R11 não citam a ANPD no enunciado.
