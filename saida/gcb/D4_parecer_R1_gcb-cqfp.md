# D4_parecer_R1_gcb-cqfp.md — T-77 — 2026-10-20 — gerado por gcb-cqfp
PARECER R1 — LOTE D4 v1 (saida/gcb/D4_v1.md, SHA-256 1cc27b3108288cacbbef8bc67d8485ddf08ab2697cb3291938d02d2c939d57d4, 254.487 bytes, LF, 1.955 linhas). O objeto é a junção mecânica, pelo orquestrador, de saida/gcb/D4_v1_parteA.md (SHA-256 c4308c21b33deb7965d648315e9f48ed4aab0e45172641b170dceb225d135253, 130.645 bytes, 977 linhas) e saida/gcb/D4_v1_parteB.md (SHA-256 11aa65e14376e9e6c8aac19acb97beeb26bbe05e8cb98cb716445563ce960dd5, 123.508 bytes, 944 linhas), produzidas por duas instâncias da gcb-cpp. Os SHA das partes conferem com os registrados na linha 4 do objeto. Este parecer faz revisão de mérito. A gcb-cqfp revisa e não reescreve. Os textos de ajuste abaixo são pontuais e fixados, como manda o costume. A redação final é da gcb-cpp na v2.

Referências:
- Ficha: saida/gcb/D4_ficha_lote.md (cb0b0c30d6939ae975d2642e0500fa554b7e6f7e1d958eee8e605e7461d6c7a0; seções 2 a 7, 9 e 10).
- Anexo N: saida/gcb/D4_anexo_N_mapa_normativo.md (0d98c24969788d2baeb150535b6a7cd538ea856fb64d3d707bc53ede24e5a05f, igual ao registrado na ficha). É a única base: normas na seção 4 e referencial na seção 5.
- Anexo N do D6: saida/gcb/D6_anexo_N_mapa_normativo.md (57e8c64d4f27fe2c7549ff9f9b16c16848a51558e9aa181a0ed48c2f85d3e80e). Usado só para a linha LAI, art. 10, caput (linha 120 do arquivo, consulta de 17/10/2026).
- Banco: banco/banco.csv (b1c1588f…721f) e banco/mapeamento_adicional.csv (c6f8a355…02e5).
- Regras: regras/PADRAO_UNICO_v1.md, regras/estilo_banca.md (v1.1.3) e regras/proveniencia.md.
- Modelo deste parecer: saida/gcb/D5_parecer_R1_gcb-cqfp.md.
- Não li saida/gcb/D4_leitura_critica.md, que não existia quando o R1 terminou.

## 0. Resultado
- Itens: 79 (D4-01 a D4-79). APROVADO: 73. APROVADO COM AJUSTE: 6 (D4-08, D4-20, D4-44, D4-51, D4-66 e D4-69). REPROVADO: 0.
- **Reprovação: 0/79 = 0,0%.** O limite do gate é 30%. Não há gate.
- Por folha: nenhuma folha tem item reprovado. Ajustes por folha: 8.2 (D4-08), 8.3 (D4-20), 9.2 (D4-44 e D4-51) e 9.4 (D4-66 e D4-69). As folhas 8.1, 8.4 e 9.1 e o caput 8 não têm ajuste.
- Por parte: Parte A com 39 itens, 0 reprovados e 2 ajustes. Parte B com 40 itens, 0 reprovados e 4 ajustes.
- Blocos:
  - Curso: APROVADO.
  - Resumo: APROVADO.
  - Pares: APROVADO.
  - Pegadinhas: APROVADO.
  - Proveniência: APROVADO.
  - Contagens por parte: APROVADO.
  - Contagem e ordem do lote: AJUSTE. A linha do lote não existe, e o teste na ordem numérica falha nas duas costuras (seção 3).
  - Junção: AJUSTE (ordem dos grupos e cabeçalhos; seção 3).
  - Arquivo de leitura crítica: **NÃO NEUTRO**. Isso já foi registrado por outra conferência da gcb-cqfp (saida/gcb/QA_neutralidade_D2_D4_2026-10-20_gcb-cqfp.md, seção 4: 14 ajustes obrigatórios), e este R1 confirma (seção 3; ponto 13).
- Veredito geral: **APROVADO COM AJUSTES**. A v2 responde aos 18 pontos da seção 5.

## 1. Evidência: conferência independente da base (checklist 2 e 5)
1. **URLs reabertas.** Em 20/10/2026, às 10:23:52 UTC, reabri seis URLs da tabela de proveniência por curl, com User-Agent de navegador (Chrome 124) e cabeçalhos Accept e Accept-Language. São cinco de referencial e a do Decreto. Os arquivos ficaram em diretório próprio do scratchpad. A extração foi por script (pdftotext e python3 -I), sem redigitação.

| Fonte | URL (como no Anexo N) | HTTP | Bytes hoje × Anexo N | SHA-256 hoje × Anexo N | Resultado |
|---|---|---|---|---|---|
| F1 TCU | https://portal.tcu.gov.br/data/files/FB/B6/FB/85/1CD4671023455957E18818A8/Referencial_basico_governanca_organizacional_3_edicao.pdf | 200 (application/pdf) | 3.770.744 × 3.770.744 | b2e7241e… = b2e7241e… | Arquivo idêntico. R14, R19 a R22 e R24 a R27 são literais. R28 também: está nas p. 15-16, com o cabeçalho de página no meio da frase, como o Anexo N registra. |
| F2 Casa Civil, Guia | https://www.gov.br/casacivil/pt-br/assuntos/governanca/comite-interministerial-de-governanca/arquivos/guia-da-politica-de-governanca-publica_versao-defeso.pdf | 200 (application/pdf) | 6.225.291 × 6.225.291 | 900139b6… = 900139b6… | Arquivo idêntico. R10, R13, R15 e R23 são literais. R4 também, conferido na p. 29: "custo-benefício" está quebrado no fim da linha, e a grafia é "manegement" (sic). |
| F5 ENAP, Bouckaert | https://revista.enap.gov.br/index.php/RSP/article/download/10595/6962/33297 | 200 (application/pdf) | 773.942 × 773.942 | 784eda01… = 784eda01… | Arquivo idêntico. R6 e R7 são literais. |
| F6 Ipea, Cavalcante | https://repositorio.ipea.gov.br/server/api/core/bitstreams/a2ec054c-70e9-4cc4-9995-3101407c9647/content | 200 (application/pdf) | 79.748 × 79.748 | dc9bd7ba… = dc9bd7ba… | Arquivo idêntico. R8, R9 e R12 são literais. |
| F10 CGU | https://repositorio.cgu.gov.br/bitstream/1/29544/10/documento_didatico_cadeia_valor.pdf | 200 (application/pdf) | 556.930 × 556.930 | fc106e48… = fc106e48… | Arquivo idêntico. R16 é literal. |
| N1 Decreto 9.203 | http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/decreto/d9203.htm | 200 (text/html) | 86.892 × 86.892 | d163bd0c… × a6d0ac51… | O SHA difere com o mesmo tamanho. Tratei como simples registro, porque o texto não mudou: as 141 linhas da seção 4.1 do Anexo N (140 dispositivos e 1 redação anterior) aparecem literalmente na página de hoje (comparação sem espaços em branco e sem aspas), 141/141. |

2. **Contexto conferido na fonte**, sem efeito de base, porque nada disso está no Anexo N e nada disso vai para item:
   - R25 (F1, p. 54). O "neste Capítulo" do trecho é o **Capítulo 5, "Práticas de Governança"**, que trata dos três mecanismos. O trecho está sob a seção "1. O mecanismo de liderança e suas práticas". Não existe capítulo dedicado à liderança. Ver D4-51.
   - R14 (F1, p. 90). O trecho é a alínea a) da lista aberta por "Promover a transparência implica:". Ver a dúvida A(3), na seção 4.
3. **Citações de artigo.** Um script (python3 -I) extraiu as **556 citações "art./arts."** de todo o D4 v1: curso, resumo, pares, pegadinhas, pontos, justificativas, bases, proveniência, contagens e blocos.
   - Cada citação foi atribuída à norma pela menção na mesma linha ou no mesmo bloco.
   - Conferi 732 componentes (artigo, parágrafo, inciso e alínea) contra as linhas da seção 4 do Anexo N, separando vigentes e revogadas. A tabela tem 140 dispositivos do Decreto (99 vigentes e 41 revogados) e 49 dispositivos complementares, como no Anexo.
   - **Inexistentes: 0.** O script acusou 8 casos, e conferi cada um à mão. Todos são artefatos do analisador:
     - "art. 1º desta Lei", dentro do texto transcrito da LAI, art. 10;
     - "art. 4º, I a XI";
     - "§§ 1º a 4º (§ 4º, I" da Lei 11.079;
     - "§§ 1º e 3º" da Lei 13.460;
     - "art. 2º, §§ 1º e 2º" da Lei 11.079, no bloco à GCB.
   - **Revogados como norma vigente: 0.** As 23 menções a artigo revogado (arts. 7º a 15, 20 e 20-A) estão todas em linha de identificação marcada, como "revogado", "[REVOGADO]", "em vez do art. 15-A" ou "a redação está desatualizada; o artigo vigente é o 9º-A". Nenhuma está em item.
   - O teste foi validado com seis citações falsas plantadas numa cópia do arquivo, e as seis foram apanhadas: art. 4º, XII; art. 13-B; art. 8º-A, § 4º; Lei 9.637, art. 1º, § 2º; Lei 13.460, art. 6º, VIII; art. 15, I sem marca de revogação.
4. **Trechos entre aspas.** Os 155 trechos entre aspas com 4 palavras ou mais, curvas ou retas, em todo o arquivo, foram conferidos contra o Anexo N e contra a linha LAI, art. 10, do Anexo N do D6. A comparação ignorou espaços e aspas e partiu cada trecho nos cortes "[…]". **Resultado: 155/155 literais.** Três divergências aparentes na linha 304 vinham do "a" entre aspas retas do art. 84, VI, e, reconferidas, são literais.
5. **Bases dos itens.**
   - As 36 bases do tipo REFERENCIAL têm o trecho entre aspas dentro da linha do próprio R-id citado, com até 25 palavras. Cada uma traz a URL do R-id e a data 20/10/2026. Divergências: 0.
   - As 43 bases do tipo DISPOSITIVO citam artigo vigente e "Anexo N, seção 4.x".
   - O arquivo tem 20 URLs distintas, todas idênticas às do Anexo N. Nenhuma tem "?" ou "#".
6. **Proibições nos 79 enunciados**, por varredura e por leitura:
   - sigla "NGP": 0;
   - sigla NPM ou NPG sem a expressão por extenso: 0;
   - "exceto": 0;
   - autor de F4 a F9 nomeado: 0. "Porter", no D4-30, é literal do R16, documento da CGU, e está no ponto 8.4-4 da ficha;
   - artigo revogado: 0;
   - ministério ou órgão atual: 0;
   - afirmação de que o decreto ou as leis vinculam a Câmara: 0;
   - "[SEM FONTE]": 0;
   - "terceiro setor": 0;
   - conteúdo do PDRAE: 0;
   - valor em reais: 0;
   - NPG que "substitui" ou "convive com" a NPM: 0.
   - "Corrupção" e "integridade" aparecem só no D4-66, como literais do art. 19.
   - REVERIFICAR = 0 e VOLÁTIL = 0, o que está correto. Nenhum dispositivo usado tem redação de 2025 ou 2026.
7. **Itens reais.** O banco/banco.csv tem exatamente três itens mapeados a P1-DA-8 e P1-DA-9, que são os do Anexo R: BQ-0121 (P1-DA-8), BQ-0151 e BQ-0152 (P1-DA-9). O banco/mapeamento_adicional.csv não tem nenhum mapeamento a DA-8 ou DA-9 (suas 20 linhas são P1-DA-12). Nenhum item do lote repete o ponto de um real. O "difere de" aparece em D4-74, 75 e 76 (BQ-0121) e em D4-45, 48 e 67 (BQ-0152). Falta no D4-44 (ajuste). O BQ-0151 é inapto e não serve de âncora, como a ficha manda.
8. **Fidelidade da junção.** Comparei o multiconjunto das linhas não vazias do D4 v1 com o das duas partes:
   - Todo o conteúdo das partes está no objeto.
   - As únicas linhas que faltam são os cabeçalhos repetidos ("## 1." a "## 8.", "### 5.1" e "### 5.2", uma vez cada), as linhas 1 das partes e as linhas "FIM DA PARTE".
   - As únicas linhas acrescentadas são as da junção: linha 1, linha 2, linha de fontes, "## 0.", os 16 subtítulos "### Parte A/B" e "FIM DO LOTE D4".
   - Nenhum texto de conteúdo foi alterado. Os defeitos de forma estão na seção 3.

## 2. Veredito por item (checklist 3)
Legenda: AP = APROVADO; AJ = APROVADO COM AJUSTE (texto exato na seção 2.1); REP = REPROVADO. Coluna [TS]: "TS" = troca no item E; "isca" = [TS] com gabarito C (elemento-isca literal). A tabela segue a ordem numérica da ficha (2.4).

| Item | Folha | Gab. | [TS] | Ponto | Veredito | Motivo curto |
|---|---|---|---|---|---|---|
| D4-01 | 8.1 | E | TS | 8.1-1 | AP | R6, com troca única "redes → mercado". O contraste vem de R8 (o mercado é a fonte da NPM). Item sem atribuição e sem autor. |
| D4-02 | 8.1 | C | — | 8.1-2 | AP | R7 literal ("facilitador e participante"). APL. |
| D4-03 | 8.1 | C | — | 8.1-6 | AP | R8, segunda frase, sem atribuição. Sem datas e sem "substituição". |
| D4-04 | 8.1 | E | TS | 8.1-4 | AP | R7 diz que os fundamentos teóricos são as teorias de rede (proposição de identidade); o item troca por "weberiana". |
| D4-05 | 8.1 | E | TS | 8.1-3 | AP | R7, com troca "confiança → concorrência". R4 dá a concorrência à NPM. Um só item para a lista, como manda a ficha. |
| D4-06 | 8.1 | C | — | 8.1-5 | AP | R4, terceira frase ("pode estar relacionado"). A atribuição ao Guia (F2) está correta. |
| D4-07 | 8.2 | E | TS | 8.2-10 | AP | Lei 13.019, art. 2º, III, com troca "público e recíproco → exclusivo da administração". |
| D4-08 | 8.2 | E | TS | 8.2-2 | **AJ** | O R9 diz que essas são tendências do pós-NPM, mas não diz que não sejam da NPM. Isso é E por ausência (ficha 3.2) em tema de classificação disputada (parcerias). O item passa a C. |
| D4-09 | 8.2 | C | — | 8.2-6 | AP | Lei 11.079, art. 2º, § 2º, literal (C3). |
| D4-10 | 8.2 | C | — | 8.2-3 | AP | R10 atribuído ao Guia, que cita a ONU. A justificativa registra a citação. |
| D4-11 | 8.2 | C | — | 8.2-1 | AP | Art. 4º, IV, no meio. APL. A fronteira com o D4-31 foi respeitada. |
| D4-12 | 8.2 | E | TS | 8.2-5 | AP | Lei 11.079, art. 2º, § 1º, com os polos da contraprestação invertidos. |
| D4-13 | 8.2 | E | TS | 8.2-8 | AP | Lei 11.079, art. 2º, § 4º, II, com troca "inferior → superior". O número é literal. |
| D4-14 | 8.2 | E | TS | 8.2-11 | AP | Lei 13.019, art. 2º, VIII, com o proponente trocado. |
| D4-15 | 8.2 | C | — | 8.2-13 | AP | Lei 9.637, art. 1º, com "poderá" e os requisitos. SIT. |
| D4-16 | 8.2 | C | — | 8.2-14 | AP | Lei 9.790, art. 1º, caput, na redação da Lei 13.019 (3 anos). |
| D4-17 | 8.3 | E | TS | 8.3-1 | AP | R11, com o "principalmente" deslocado. A troca do par de estágios conta como um elemento. |
| D4-18 | 8.3 | C | — | 8.3-2 | AP | R12 literal, sem atribuição. |
| D4-19 | 8.3 | C | — | 8.3-4 | AP | Art. 4º, VIII, literal. APL. |
| D4-20 | 8.3 | E | TS | 8.3-3 | **AJ** | O trecho de R13 não nega "célere e eficiente". É E por ausência (ficha 3.2 e 6.5). A troca passa a ser o efeito ("aumentar → reduzir"). |
| D4-21 | 8.3 | E | TS | 8.3-6 | AP | R15, com troca "ativa → passiva". A "comunicação … voluntária" do art. 4º, XI, desmente o item. |
| D4-22 | 8.3 | C | — | 8.3-7 | AP | R14 literal (C3). Dúvida A(3) respondida. |
| D4-23 | 8.3 | E | TS | 8.3-5 | AP | Art. 4º, IX, com troca "sempre que conveniente → obrigatoriamente". |
| D4-24 | 8.3 | C | — | 8.3-8 | AP | LAI, art. 8º, § 1º, I, II e VI, "no mínimo" (C6). Não toca D6-12 nem D6-15. |
| D4-25 | 8.3 | C | — | 8.3-9 | AP | Lei 13.460, art. 6º, I. APL. |
| D4-26 | 8.3 | E | TS | 8.3-11 | AP | Lei 13.460, art. 1º, § 3º, com a aplicação subsidiária negada. |
| D4-27 | 8.4 | C | — | 8.4-1 | AP | Art. 2º, II, parte inicial (C6). Espelho do D4-28, autorizado pela ficha (ponto 16). |
| D4-28 | 8.4 | E | TS | 8.4-2 | AP | Art. 2º, II, com a definição restrita ao "gerado" (E6). |
| D4-29 | 8.4 | E | TS | 8.4-7 | AP | R18, rol entre parênteses, com troca "resultados → metas". |
| D4-30 | 8.4 | C | — | 8.4-4 | AP | R16 literal. A CGU fala pelo órgão. |
| D4-31 | 8.4 | C | — | 8.4-3 | AP | Art. 4º, IV, na finalidade. Fronteira com o D4-11. |
| D4-32 | 8.4 | C | isca | 8.4-6 | AP | R17. A isca "essencialmente" é literal. APL. |
| D4-33 | 8.4 | E | TS | 8.4-5 | AP | R17, com troca "cadeia de valor → cadeia de suprimentos" (base de identidade). |
| D4-34 | 9.1 | C | — | 9.1-4 | AP | R19 literal, atribuído ao TCU. Nota à GBQ com o D4-37. |
| D4-35 | 9.1 | E | TS | 9.1-1 | AP | Art. 2º, I, com troca "controle → gestão". |
| D4-36 | 9.1 | E | TS | 9.1-5 | AP | R20 com as funções invertidas. |
| D4-37 | 9.1 | C | isca | 9.1-2 | AP | Art. 2º, I, literal. SIT. |
| D4-38 | 9.1 | C | — | 9.1-6 | AP | R21 literal. |
| D4-39 | 9.1 | E | TS | 9.1-7 | AP | R21 com a relação invertida. O teto de 2 itens entre 9.1-6, 9.1-7 e 9.1-8 foi cumprido. |
| D4-40 | 9.1 | C | — | 9.1-9 | AP | R22 em situação hipotética. |
| D4-41 | 9.1 | C | — | 9.1-10 | AP | Art. 5º, II, só no alinhamento. APL. |
| D4-42 | 9.1 | E | — | 9.1-3 | AP | E5: o segmento nega uma das duas finalidades do art. 2º, I. |
| D4-43 | 9.1 | E | TS | 9.1-11 | AP | R23 com troca "TCU → CGU". |
| D4-44 | 9.2 | E | TS | 9.2-1 | **AJ** | Troca "três → quatro" correta. Falta "difere de BQ-0152", que é do mesmo tópico ("mecanismos para o exercício da governança"). |
| D4-45 | 9.2 | C | — | 9.2-2 | AP | Art. 5º, I, literal. Tem "difere de BQ-0152". |
| D4-46 | 9.2 | E | TS | 9.2-5 | AP | Art. 5º, III, com troca "mitigar → eliminar". |
| D4-47 | 9.2 | E | TS | 9.2-9 | AP | R27 com a negação suprimida. |
| D4-48 | 9.2 | C | — | 9.2-3 | AP | Contagem das alíneas a a d. Tem "difere de BQ-0152". |
| D4-49 | 9.2 | C | — | 9.2-4 | AP | Art. 5º, II, sem o alinhamento. SIT. |
| D4-50 | 9.2 | E | — | 9.2-12 | AP | E5: "apenas o comportamento dos dirigentes", quando o inciso diz "agentes públicos". |
| D4-51 | 9.2 | C | isca | 9.2-7 | **AJ** | "No capítulo dedicado ao mecanismo liderança" não está no Anexo N e não confere com a fonte: o "neste Capítulo" é o Capítulo 5, "Práticas de Governança". |
| D4-52 | 9.2 | C | — | 9.2-11 | AP | Art. 6º, parágrafo único, II e III. APL. |
| D4-53 | 9.2 | E | TS | 9.2-10 | AP | Art. 6º, caput, com o sujeito trocado. |
| D4-54 | 9.3 | E | TS | 9.3-1 | AP | Art. 2º, II, definição fechada, com troca "efetivas e úteis → céleres e econômicas". |
| D4-55 | 9.3 | E | TS | 9.3-5 | AP | Art. 4º, VII, com troca "sempre que possível → em qualquer caso" (E6). |
| D4-56 | 9.3 | C | — | 9.3-4 | AP | Art. 4º, III, literal. APL. |
| D4-57 | 9.3 | E | — | 9.3-3 | AP | E5: o segmento dispensa as mudanças de prioridades. |
| D4-58 | 9.3 | E | TS | 9.3-8 | AP | R29 sem atribuição, com troca "beneficiários → gestores públicos". |
| D4-59 | 9.3 | C | — | 9.3-7 | AP | R28 literal. O "todas" é do trecho. |
| D4-60 | 9.3 | C | isca | 9.3-2 | AP | Art. 2º, II. A isca é literal. |
| D4-61 | 9.3 | E | TS | 9.3-9 | AP | R30 com a relação de continência invertida. |
| D4-62 | 9.3 | C | — | 9.3-10 | AP | R30 e R31 num só item, como manda a ficha. APL. |
| D4-63 | 9.3 | C | — | 9.3-11 | AP | R18, ex ante e ex post. Fronteira com o D4-29. |
| D4-64 | 9.4 | C | — | 9.4-1 | AP | Art. 1º, só o objeto. Não julga o âmbito quanto à Câmara. APL. |
| D4-65 | 9.4 | E | TS | 9.4-3 | AP | Art. 2º, IV, com troca "razoável → absoluta". |
| D4-66 | 9.4 | E | — | 9.4-17 | **AJ** | A moldura "a autarquia cumpre o art. 19" não é verdadeira por si, porque os eixos não foram dados. São dois pontos possíveis de erro, contra a ideia de afirmação única. Basta reescrever a moldura. |
| D4-67 | 9.4 | C | — | 9.4-4 | AP | Art. 3º, seis incisos. Tem "difere de BQ-0152". |
| D4-68 | 9.4 | E | TS | 9.4-5 | AP | Art. 4º, VI, com a prioridade invertida. |
| D4-69 | 9.4 | E | TS | 9.4-7 | **AJ** | Art. 8º-A, § 2º. O gabarito E se sustenta, mas a justificativa omite que o art. 11-A, parágrafo único, III, dá à Secretaria-Executiva comunicar "a convocação" das reuniões extraordinárias. É preciso explicitar isso. |
| D4-70 | 9.4 | C | — | 9.4-13 | AP | Art. 15-A, I, sem dever de criar comitê nem prazo. APL. |
| D4-71 | 9.4 | C | isca | 9.4-8 | AP | Art. 8º-B, § 1º, literal. |
| D4-72 | 9.4 | E | TS | 9.4-10 | AP | Art. 10-B, II, com troca "cinco → dez". |
| D4-73 | 9.4 | C | — | 9.4-15 | AP | Art. 17, quatro incisos, com o sujeito preservado. |
| D4-74 | caput 8 | E | TS | c8-1 | AP | R1 com a sucessão invertida. Tem "difere de BQ-0121". |
| D4-75 | caput 8 | C | — | c8-2 | AP | R1 literal. APL. Tem "difere de BQ-0121". |
| D4-76 | caput 8 | E | TS | c8-3 | AP | R1 com o modelo trocado, sem "corrupção". Tem "difere de BQ-0121". O R1 diz que a burocracia foi adotada para substituir o modelo em que o nepotismo era a norma. |
| D4-77 | caput 8 | C | — | c8-5 | AP | R3 literal, com o tempo verbal ajustado. |
| D4-78 | caput 8 | C | — | c8-4 | AP | R2 literal (C3). |
| D4-79 | caput 8 | E | TS | c8-6 | AP | R4 com os conjuntos de traços trocados entre os dois modelos (uma troca de atribuição). |

### 2.1 Textos exatos dos ajustes (APROVADO COM AJUSTE)
1. **D4-08** (ajuste obrigatório; sem ele, o item é reprovado). O gabarito E depende de ler "tendência do pós-NPM" como "não é da NPM", e o R9 não diz isso. É E por ausência (ficha 3.2). Além disso, se parcerias e colaboração são ou não traço da NPM é classificação que o Anexo N não resolve (ficha 3.4 e 6.7). Texto do ajuste:
   - Enunciado: "Considere que um analista descreva as tendências da gestão pública pós-nova gestão pública (pós-NPM). Nessa situação, ele estará correto ao incluir entre elas a colaboração e as parcerias, em processos colaborativos de variadas formas, e a atuação em redes na provisão de serviços públicos."
   - Gabarito C. Sem [TS]: suprimir o campo Troca e marcar TS=não.
   - Formato: situação hipotética. Mecanismo: reprodução próxima do texto (C2).
   - Justificativa (linha 1): "R9 lista, entre as tendências do ‘pós-NGP’ [NGP = nova gestão pública (NPM)], a colaboração e as parcerias (processos colaborativos de variadas formas) e a atuação em redes na provisão de serviços públicos."
   - Justificativa (linha 2): "O item reproduz as duas primeiras alíneas da lista, sem dizer que ela se esgota nelas nem que essas práticas faltem à nova gestão pública (NPM)."
   - Ponto 8.2-2 e base (R9) mantidos.
2. **D4-20** (ajuste obrigatório; sem ele, o item é reprovado).
   - Enunciado: "Segundo o Guia da Política de Governança Pública, manter um processo decisório que incentive a participação da sociedade, por exemplo por meio de consulta pública, é importante para reduzir a percepção de que as políticas e as leis foram desenvolvidas e implementadas de forma justa e imparcial."
   - Gabarito E e [TS] mantidos. Troca: "aumentar → reduzir (R13)". Mecanismo: inversão de polaridade (E2).
   - Justificativa (linha 2): "O item inverte o efeito: o trecho fala em aumentar, e não em reduzir, a percepção de que as políticas e as leis foram desenvolvidas e implementadas de forma justa e imparcial."
   - Base: mantida, com o trecho de R13 já citado.
3. **D4-44**. Acrescentar o campo: "Difere de: BQ-0152 porque este item só conta os mecanismos do art. 5º (três) e não julga se a integridade é princípio (art. 3º, II) nem condição da liderança (art. 5º, I, a)." Gabarito E e [TS] mantidos.
4. **D4-51** (ajuste obrigatório; sem ele, o item é reprovado).
   - Enunciado: "Segundo o Referencial Básico de Governança Organizacional do TCU, em um de seus capítulos, liderança é sinônimo de instâncias internas de governança e engloba os conselhos ou colegiados superiores e a alta administração da organização."
   - Troca: "elemento-isca: ‘liderança é sinônimo de instâncias internas de governança’ (literal em R25, que restringe a equivalência a ‘neste Capítulo’)".
   - Gabarito C e [TS] de isca mantidos.
   - Justificativa (linha 2), fim: trocar "e ao seu capítulo" por "e a um de seus capítulos, como o trecho".
5. **D4-66**.
   - Enunciado: "Considere que uma autarquia federal institua programa de integridade com o objetivo de promover a adoção de medidas e ações institucionais destinadas à prevenção, à detecção, à punição e à remediação de fraudes e atos de corrupção. Nessa situação, o objetivo do programa corresponde ao previsto no art. 19 do Decreto nº 9.203/2017, cujos eixos, entretanto, dispensam a existência de unidade responsável pela implementação do programa no órgão ou na entidade."
   - Justificativa (linha 2): "A moldura (objetivo do programa, literal do art. 19, caput) é verdadeira; o segmento ‘cujos eixos dispensam a existência de unidade responsável’ é falso, pois essa unidade é o eixo do inciso II."
   - Gabarito E, mecanismo E5 e ausência de [TS] mantidos.
6. **D4-69**.
   - Justificativa (linha 2): "O item troca o Coordenador pela Secretaria-Executiva; o art. 11-A, parágrafo único, III, só lhe atribui comunicar aos membros a data e a hora das reuniões ordinárias ou a convocação para as extraordinárias, e não convocá-las."
   - Gabarito E e [TS] mantidos.

### 2.2 Itens reprovados
Nenhum. Três ajustes são obrigatórios: D4-08, D4-20 e D4-51. Se a v2 não os acolher, os três passam a REPROVADO no R2 (3/79 = 3,8%, ainda abaixo do gate).

## 3. Blocos
- **Contagens (checklist 4; ficha 5.1, 6.2 a 6.4).** Refiz as contagens por script sobre o arquivo.
  - Os 79 itens estão contínuos e iguais em 5.1 e 5.2, todos com os campos fixos (ficha 2.3) e com "QA PENDENTE". O [TS] do cabeçalho confere com as marcas. Não há [TS] sem "Troca" nem "Troca" sem [TS]. Os pontos são 79, todos distintos e admitidos (ficha 5.2 e 5.3).
  - Por folha:

    | Folha | C/E | [TS] |
    |---|---|---|
    | 8.1 | 3/3 | 3 |
    | 8.2 | 5/5 | 5 |
    | 8.3 | 5/5 | 5 |
    | 8.4 | 4/3 | 4 (1 isca) |
    | caput 8 | 3/3 | 3 |
    | 9.1 | 5/5 | 5 (1 isca) |
    | 9.2 | 5/5 | 5 (1 isca) |
    | 9.3 | 5/5 | 5 (1 isca) |
    | 9.4 | 5/5 | 5 (1 isca) |

  - Por parte e no lote:

    | Escopo | C/E | [TS] |
    |---|---|---|
    | Parte A | 20/19 | 20 |
    | Parte B | 20/20 | 20 |
    | Lote | 40/39 (50,6% de C) | 40 (5 iscas) |

  - Tudo está dentro das faixas da ficha 5.1, e há no máximo 1 isca por folha.
  - Formatos: dentro dos tetos, que são 3 nas folhas de 10 itens e 2 em 8.1, 8.4 e no caput.
  - Moldura do Legislativo: os 12 itens com a moldura são exatamente os 12 rotulados APL (8.1: 1; 8.2: 1; 8.3: 2; 8.4: 1; caput: 1; 9.1: 1; 9.2: 1; 9.3: 2; 9.4: 2). Dentro dos tetos.
  - Tipo de base: 43 DISPOSITIVO e 36 REFERENCIAL. REVERIFICAR 0; VOLÁTIL 0.
  - Tetos e pisos de pontos cumpridos: Lei 11.079 com 3 itens; Lei 13.019 com 2; Leis 9.637 e 9.790 com 2; pontos 8.2-1 a 8.2-3 com 3; 9.1-6 a 9.1-8 com 2; CIG e grupos com 3; 9.4-15 a 9.4-17 com 2; 9.4-4 com 1.
  - Depois dos ajustes:
    - 8.2: C 6/E 4 e [TS] 4. Formatos: DEF 3, SUJ 1, SIT 2, NUM 2, PAR 1, APL 1.
    - Parte A: C 21 e [TS] 19.
    - Lote: C 41/79 (51,9%) e [TS] 39.
    - Tudo continua dentro das faixas (ficha 5.1).
- **Teste de ordem (ficha 6.4 e 10.3).** Ficha 2.4: "Resultado: itens na ordem numérica D4-01 a D4-79". Ficha 6.4: o teste vale "no lote (D4-01 a D4-79)".
  - Por folha, por parte e na ordem exibida pela junção (D4-01 a D4-33, D4-74 a D4-79, D4-34 a D4-73), o teste passa: maior corrida 3, maior alternância 4, nenhum bloco de período 2 a 8.
  - **Na ordem numérica, o teste falha nas duas costuras:**

    | Costura | Sequência | Falha | Trecho |
    |---|---|---|---|
    | 33/34 | gabaritos | bloco de período 7 em D4-24 a D4-37 e em D4-25 a D4-38 | CCECEECCCECEEC |
    | 33/34 | [TS] | bloco de período 4 em D4-27 a D4-34 e em D4-32 a D4-39 | — |
    | 73/74 | gabaritos | alternância estrita de 7 itens em D4-71 a D4-77 | CECECEC |
    | 73/74 | [TS] | alternância de 6 itens em D4-72 a D4-77 e bloco de período 3 em D4-67 a D4-74 | — |

  - A junção pôs o caput entre a 8.4 e a 9.1. Isso esconde as falhas e contraria a ficha 2.4. Ver os pontos 9 e 10.
- **Junção (ficha 2.4).** O conteúdo está fiel (seção 1, n. 8). Defeitos de forma:
  - (a) Em 5.1 e 5.2, o grupo "Caput do item 8" está depois da folha 8.4 e antes da Parte B, e não por último.
  - (b) A linha 1 não segue o modelo da ficha nem o do CLAUDE.md (falta "gerado por gcb-cpp (Partes A e B; junção mecânica do orquestrador)"). A linha 2 tem o acréscimo "(partes A e B)".
  - (c) Há uma seção "## 0. CABEÇALHOS DAS PARTES" que a ficha não prevê.
  - (d) Em "## 7." falta a linha do lote: 79 itens, C/E, [TS], formatos, tipo de base e teste de ordem sobre D4-01 a D4-79 com as costuras.
  - (e) Em 5.1, a instrução "Só enunciado. Julgue cada item como Certo ou Errado." da Parte B aparece no meio da versão do estudante.
  - (f) O script de junção é saida/gcb/scripts_orq/juntar_partes.py, genérico para os lotes de DA. Ele só falha por perda de linha. Não põe o caput por último, não confere lacuna nem faixa de id e não roda o teste de ordem nem escreve a linha do lote, como manda a ficha 2.4. Os defeitos (a) a (e) vêm dele.
  - Ver o ponto 9.
- **Curso**: APROVADO.
  - Tem 58 blocos: caput 6; 8.1 4; 8.2 10; 8.3 7; 8.4 5; 9.1 5; 9.2 6; 9.3 6; 9.4 9.
  - Cada bloco tem definição com dispositivo ou com trecho literal, exemplo hipotético dito como tal e pegadinha com base.
  - A atribuição está correta. F4 a F9 vêm como "segundo [autor], em publicação da ENAP/do Ipea". F1, F2, F3 e F10 falam pelo órgão. R5 (PDRAE) só aparece no curso, como paráfrase do Ipea, e R5 não é misturado com R21.
  - Os pontos SEM FONTE da ficha 3.4 aparecem só com a marca.
  - Revogados aparecem só como identificação. O art. 14 é dado como revogado e sem sucessor, e o art. 20-A como revogado.
  - Não há afirmação sobre o âmbito do decreto quanto à Câmara, nem sobre órgão atual, nem sobre prática da Casa.
  - A convenção NPM/NPG/pós-NPM foi cumprida, e "NGP" aparece só em citação do Ipea, com a glosa.
  - Registro sem efeito: o C9.2-02 diz "no capítulo respectivo do referencial". A formulação é neutra e não precisa mudar, mas não deve ser lida como "capítulo de liderança" (D4-51).
- **Resumo**: APROVADO. Uma página por parte. Parte A: quadros "modelo × traço × fonte", parcerias, transparência e valor público. Parte B: números e listas literais do Decreto e quadro "revogado × vigente com letra". Números conferidos: 6 princípios, 11 diretrizes, 3 mecanismos, 4 condições mínimas, 4 princípios do art. 17, 4 eixos do art. 19, quóruns e grupos de 5, 1 e 3.
- **Pares**: APROVADO. São 23 (P-01 a P-11 e P-51 a P-62), contra o mínimo de 16. Os 14 obrigatórios da ficha 5.4 estão presentes. Cada lado tem lastro. O lado passivo do P-07 usa só a exceção da ficha (LAI, art. 10, caput, do Anexo N do D6).
- **Pegadinhas**: APROVADO. São 58 (G-01 a G-32 e G-51 a G-76), uma por bloco, sem repetição, cada uma com base.
- **Proveniência (checklist 5)**: APROVADO.
  - Parte A: N1, N5 a N10, a linha do Anexo N do D6, e F1 a F10.
  - Parte B: N1 a N4 e R5, R18 a R31.
  - As URLs são idênticas às do Anexo N, com data, página e rótulo (norma; OUTRA_OFICIAL).
  - Os itens reais remetem a banco/banco.csv (cdn.cebraspe.org.br).
  - Pontos sem fonte declarados.
- **Cobertura (checklist 1)**: cumprida.
  - 8 folhas e o caput 8 têm curso e itens: 6, 10, 10, 7, 10, 10, 10, 10 e 6.
  - O caput 9 não tem bloco nem item, como manda a ficha.
  - Todos os critérios da ficha 5.1 a 5.5 foram atendidos. Os pontos não usados estão declarados nos blocos à GCB e aparecem no curso.
  - Fronteiras conferidas:
    - art. 2º, II: início na 8.4 (D4-27 e D4-28) e fim na 9.3 (D4-54 e D4-60);
    - art. 4º, IV: o meio no D4-11 e a finalidade no D4-31;
    - art. 4º, VIII, IX e XI na 8.3; I, III e VII na 9.3; V na 9.2; VI na 9.4;
    - art. 5º, II: o alinhamento no D4-41 e o resto no D4-49;
    - R4 e R8 só na Parte A;
    - R18: elos no D4-29 e ex ante/ex post no D4-63.
  - Nenhuma duplicata de proposição entre as partes.
- **Estilo Cebraspe**: APROVADO no conjunto.
  - A versão do estudante abre com "Julgue cada item como Certo ou Errado.".
  - Cada item é uma afirmação única, com exceção do D4-66 (ajuste). Nenhum "exceto".
  - Os termos absolutos ou são literais da fonte (D4-59 "todas", D4-32 "essencialmente") ou são o próprio erro (D4-28 "restringe-se", D4-50 "apenas", D4-55 "em qualquer caso", D4-65 "absoluta").
  - Os enunciados têm de 11 a 71 palavras (média 35,4).
  - E por ausência: D4-08 e D4-20 (ajustes). Nos demais E, o trecho ou o dispositivo afirma o contrário, ou há rol fechado, ou definição fechada do decreto (D4-54).
- **Leitura crítica (ficha 9.2; critério 7)**: **NÃO NEUTRO.** A conferência própria foi feita em saida/gcb/QA_neutralidade_D2_D4_2026-10-20_gcb-cqfp.md (SHA-256 996a2d34…cc34), com 14 ajustes obrigatórios no D4 (D4-a a D4-n). Este R1 a confirma de forma independente. O que segue é só o que a varredura do R1 achou.
  - Arquivo: saida/gcb/D4_para_leitura_critica.md (SHA-256 c0b7c181a705d38b3209091f57f99e0dd8b4b826ce30e9aa70c064b86b62bc14; 536 linhas; gravado em 20/10/2026 às 07:12:04 −0300).
  - O que está certo:
    - a linha 1, a instrução literal ao leitor, o texto do edital e a linha "FIM";
    - só as seções 1 a 4, sem item, gabarito, [TS], "QA PENDENTE", "BQ-", "Anexo N", fornecedor, agente, "Fundador", "fábrica", "orquestrador", "T-77" ou "D-…";
    - nenhuma URL;
    - as duas ocorrências de "Presidência" são "Casa Civil da Presidência da República", termo da norma.
  - O que está errado:
    - O arquivo traz **5 ocorrências de "Parte A"/"Parte B"** (linhas 425, 444 e 504). Elas estão na lista de aborto da ficha 9.2, e o script deveria ter falhado.
    - As linhas 425 e 444 mostram organização interna da produção ("Mínimo deste material: 8 na Parte A (14 obrigatórios no lote…)").
    - A troca "Anexo N" → "texto compilado consultado" gerou, na linha 14, a expressão imprópria "R-id da seção 5 do texto legal compilado" (o referencial não é texto legal).
    - O gerador está em saida/gcb/scripts_orq/leitura_critica_gen.py, genérico, e não no caminho que a ficha 9.2 manda (saida/gcb/D4_para_leitura_critica_gen.py). Ele não aborta diante de "Parte A/B", que está na lista da ficha.
  - O vazamento não revela item, gabarito, fornecedor nem agente. Ver o ponto 13.
- **Primeira e última linha (critério 9)**: as partes estão corretas ("# D4_v1_parteA.md — T-77 — 2026-10-20 — gerado por gcb-cpp", "FIM DA PARTE A — LOTE D4"; idem para a B). No objeto, a linha final "FIM DO LOTE D4" está correta, e a linha 1 tem defeito de forma (ver Junção). Produção gcb-cpp (sonnet) e QA gcb-cqfp (opus) são agentes e modelos distintos.

## 4. Respostas às dúvidas das produtoras (seção 8 das partes)
**Parte A**
- (1) Linha final. A forma da ficha ("FIM DA PARTE A — LOTE D4") está correta, e a junção a remove. Nada a fazer.
- (2) D4-01, D4-04 e D4-05. O uso de R8 (primeira frase) e de R4 (primeira e segunda frases) **só como apoio da justificativa** é admitido. O ponto de cada item continua sendo o da 8.1, e o R1 não vê duplicata com o D4-79: lá, os traços weberiano e NPM são trocados entre si; aqui, a NPG recebe fundamento, princípio ou apoio alheio. O c8-7 continua de reserva. Se for ativado, não repete o D4-01, cujo ponto é o R6. Nota à GBQ no ponto 15.
- (3) D4-22. A redação "inclui, entre os seus itens" é aceitável, e o gabarito C é seguro. Conferi na fonte (seção 1, n. 2) que R14 é a alínea a) de "Promover a transparência implica:". Essa frase de abertura não está no Anexo N e não entra no item. Se a GCB quiser precisão maior, pode pedir ao qa-normativo-da um adendo do R14 com a frase de abertura. Sem o adendo, o texto fica como está.
- (4) D4-10. Correto. O Guia (F2) adota a citação da ONU, e a justificativa a registra.
- (5) D4-29. "É formada por" para a lista entre parênteses de R18 é aceitável, porque o rol é tratado como fechado e a troca de um elo é desmentida pelo próprio trecho.
- (6) D4-24. Correto. A premissa não repete o caput da LAI (D6-12) e não usa o inciso IV (D6-15).
- (7) art. 4º, IV, dividido entre D4-11 e D4-31. Está correto pela fronteira da ficha. Nota à GBQ mantida.
- (8) "Nenhum item tem E por ausência". **Não confirmado** para o D4-08 e o D4-20 (seção 2.1, n. 1 e 2). Nos demais E da Parte A, confirmado.

**Parte B**
- Escolha (1): os E5 sem [TS] (D4-42, D4-50, D4-57 e D4-66) estão corretos. Nenhum tem troca de elemento, só segmento acrescentado. O D4-66 recebe ajuste de moldura, sem [TS].
- Escolha (2): 9.2-1 com o art. 5º como base e R24 como apoio está correto. Falta só o "difere de BQ-0152" (D4-44).
- Escolha (3): 9.3-10 com R30 e R31 num item está correto, como manda a ficha.
- Escolha (4): 9.4-7 está correto, e o gabarito se sustenta. A justificativa precisa explicitar o art. 11-A, parágrafo único, III (D4-69).
- Escolha (5): correto. Nenhum item usa o art. 14, os revogados ou o art. 20-A.
- Dúvida (a), R25 × art. 5º, I. Não há conflito que ponha o gabarito em risco: o decreto define a liderança como práticas, e o TCU, no Capítulo 5 do Referencial, trata a liderança como sinônimo de instâncias internas. O item é C se atribuir a equivalência ao TCU e mantiver a restrição a um capítulo. O defeito está na expressão "capítulo dedicado ao mecanismo liderança", que não está no Anexo N e não confere com a fonte (seção 1, n. 2). Ajuste no D4-51. O C9.2-02 e a G-57 ficam como estão.
- Dúvida (b): R26 sem item. Concordo. O trecho diz o que "é importante" e não define o mecanismo.
- Dúvida (c): concordo. R21 e R22 aparecem atribuídos ao Referencial do TCU.
- Dúvida (d): concordo. O D4-64 julga só o objeto do art. 1º.

## 5. Pontos para a v2 (a gcb-cpp responde item a item: acatado / não acatado + motivo)
1. **D4-08** (Parte A; obrigatório): converter em C sem [TS], formato SIT, com o texto da seção 2.1, n. 1.
2. **D4-20** (Parte A; obrigatório): trocar "célere e eficiente" pela inversão do efeito ("reduzir"), com troca "aumentar → reduzir (R13)", mecanismo E2 e justificativa, linha 2, conforme a seção 2.1, n. 2.
3. **D4-51** (Parte B; obrigatório): trocar "no capítulo dedicado ao mecanismo liderança" por "em um de seus capítulos", com o campo Troca e a justificativa conforme a seção 2.1, n. 4.
4. **D4-44** (Parte B): acrescentar "difere de BQ-0152" (seção 2.1, n. 3).
5. **D4-66** (Parte B): reescrever a moldura (seção 2.1, n. 5).
6. **D4-69** (Parte B): justificativa, linha 2, com o art. 11-A, parágrafo único, III (seção 2.1, n. 6).
7. **Contagens** da 8.2, da Parte A e do lote, refeitas depois do ponto 1. Meta da 8.2: C 6/E 4, [TS] 4, SIT 2, PAR 1. Parte A: C 21 e [TS] 19. Lote: C 41 e [TS] 39. Declarar na v2 a lista dos 79 pontos (inalterada).
8. **Teste de ordem na 8.2.** Depois do ponto 1, a ordem atual da 8.2 dá CCCC em D4-08 a D4-11, e a folha falha no teste. A Parte A troca posições dentro da 8.2, renumera dentro da faixa e registra a correspondência.
9. **Junção da v2** (orquestrador, ficha 2.4):
   - (a) 5.1 e 5.2 na ordem numérica D4-01 a D4-79, com o grupo "Caput do item 8" por último;
   - (b) linha 1 = "# D4_v2.md — T-77 — [data ISO] — gerado por gcb-cpp (Partes A e B; junção mecânica do orquestrador)" e linha 2 no modelo da ficha;
   - (c) sem a seção "## 0." (os cabeçalhos das partes podem ir em nota sob "## 1." se a GCB quiser registrá-los);
   - (d) sem a instrução duplicada no meio de 5.1;
   - (e) em "## 7.", a linha do lote e o teste de ordem sobre D4-01 a D4-79, com as costuras, impressos pelo script;
   - (f) o saida/gcb/scripts_orq/juntar_partes.py corrigido (python3 -I) para fazer (a) a (e) e para falhar nos casos da ficha 2.4: cabeçalho faltante, id fora da faixa, id repetido, lacuna e teste de ordem reprovado.
10. **Costuras 33/34 e 73/74** (decisão da GCB; execução da Parte A; a Parte B não é reaberta). Na ordem numérica, as duas costuras falham (seção 3).
    - **Trocar posições só na 8.4 não resolve a costura 33/34.** Das permutações da 8.4 que passam no teste da folha, nenhuma remove as falhas.
    - Por isso, a GCB decide se autoriza a Parte A a trocar posições também na 8.2 e na 8.3, além da 8.4 e do caput.
    - Prova de existência, calculada pelo R1 já com o ponto 1, sem obrigar a escolha:
      - 8.2: D4-11 ↔ D4-14.
      - 8.3: as posições D4-17, D4-21, D4-22, D4-23, D4-25 e D4-26 recebem os itens hoje numerados D4-21, D4-26, D4-23, D4-22, D4-17 e D4-25, nessa ordem.
      - 8.4: as posições D4-27, D4-28, D4-29, D4-30, D4-31 e D4-33 recebem os itens hoje numerados D4-31, D4-29, D4-28, D4-27, D4-33 e D4-30, nessa ordem.
      - Caput: as posições D4-74, D4-75, D4-77 e D4-79 recebem os itens hoje numerados D4-77, D4-74, D4-79 e D4-75, nessa ordem.
      - Com essas trocas, o teste passa por folha, na Parte A e no lote D4-01 a D4-79, para gabaritos e para [TS].
    - A Parte A refaz o teste, informa os períodos 2 a 8 e registra a correspondência.
11. **Formatos** refeitos depois dos pontos 1 e 10 (tetos da ficha 6.3).
12. **Pontos de julgamento**: sem mudança de código. Na v2, conferir que nenhuma renumeração do ponto 10 quebra os campos "Difere de" e as notas à GBQ, que citam ids.
13. **Arquivo neutro** (decisão da GCB e do orquestrador; os 14 ajustes estão em saida/gcb/QA_neutralidade_D2_D4_2026-10-20_gcb-cqfp.md, seção 4, e este R1 não os repete):
    - (a) Se o arquivo **ainda não foi entregue** ao leitor externo, os ajustes D4-a a D4-n entram nas regras de saida/gcb/scripts_orq/leitura_critica_gen.py. O gerador passa a abortar diante de "Parte A/B", como manda a ficha 9.2, e é gravado também no caminho da ficha ou registrado como seu substituto. Em seguida, regera-se o arquivo, e a gcb-cqfp reconfere e emite "NEUTRO CONFERIDO [SHA]".
    - (b) Se o arquivo **já foi entregue**, o orquestrador registra o desvio na reconciliação. O vazamento é de organização interna e não inclui item, gabarito, fornecedor ou agente. O arquivo é regerado só para o registro.
14. **Leitura crítica externa.** Pelo desvio declarado na ficha 9.4, este R1 correu sem a resposta. A gcb-cpp grava saida/gcb/D4_acatamento_leitura_critica_parteA.md e _parteB.md (acatada / não acatada + motivo; só com dispositivo vigente da seção 4 ou trecho R1–R31, sem repetir ponto já usado e sem cair nos SEM FONTE) e leva à v2, com "QA PENDENTE", o que acatar. O R2 confere o registro e tudo o que ele mudar.
15. **Notas à GBQ, para simulado** (sem efeito no veredito).
    - Mantenho as listas dos blocos à GCB das duas partes.
    - Acrescento:
      - D4-34 com D4-37 (avaliar, direcionar e monitorar: R19 × art. 2º, I);
      - D4-35 com D4-44 (composição × número dos mecanismos);
      - D4-05 e D4-04 com D4-79 (R4 como contraste);
      - D4-27 e D4-28 com D4-54 e D4-60 (art. 2º, II, entre as partes);
      - D4-29 com D4-63 (R18);
      - D4-08 com D4-18, depois do ponto 1 (os dois C sobre tendências do pós-NPM).
    - Observação de mérito, sem efeito no veredito: D4-27 e D4-28 são espelho (quem acerta um acerta o outro). A ficha os admitiu como pontos distintos (8.4-1 e 8.4-2), por isso não há reprovação. A GCB pode rever isso no reforço da 8.4 (T-100).
16. **Registro de fonte**: o HTML do Decreto 9.203 baixado hoje tem SHA-256 diferente do registrado no Anexo N (d163bd0c… × a6d0ac51…), com o mesmo tamanho e o texto idêntico (141/141). Só registro, para a reverificação de janeiro.
17. **Registro de atribuição**: o "neste Capítulo" de R25 é o Capítulo 5 ("Práticas de Governança") do Referencial do TCU, conferido na fonte. Se a GCB quiser usar o dado em curso futuro, deve pedir antes um adendo ao Anexo N, porque hoje ele não é base.
18. **Ordem de execução sugerida**: pontos 1 a 6; depois 7, 8, 10 e 11 (uma única reordenação da Parte A com o teste refeito); depois 9 (junção da v2); 13 e 14 em paralelo. O R2 confere 1 a 12 e 14.

Todo item continua "QA PENDENTE" até o R2 e a reconciliação da GCB (D-QA-PENDENTE). Nada vai à plataforma nem à candidata.

FIM DO PARECER R1 — LOTE D4
