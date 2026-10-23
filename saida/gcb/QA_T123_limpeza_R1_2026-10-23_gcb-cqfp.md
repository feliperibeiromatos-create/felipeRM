# QA_T123_limpeza_R1_2026-10-23_gcb-cqfp.md — T-123, QA R1 da limpeza das marcas de produção no reforço de DA — 2026-10-23 — gerado por gcb-cqfp

Objeto: `saida/gcb/T123_substituicoes_DA.csv` (91 edições; SHA-256 LF `01d5be77e40d74b1f4ae7be8faf05f4b222e4e1af39c61081c3b3fb13d152505`, igual ao declarado; UTF-8 sem BOM, LF) e `saida/gcb/T123_producao_notas_DA.md`. Roteiro: `saida/gcb/T123_limpeza_D1_GCB_2026-10-23.md`, seção 5. Texto-base: `saida/pacote/montagem_v1_14/out/reforco_bruto.json`, só leitura. A gcb-cqfp não editou nenhum arquivo de produção.

## Veredito: DEVOLVIDO

- 91 linhas: 89 APROVADO, 2 CORRIGIR (GCB-T123-0028 e GCB-T123-0032), 0 REPROVADO.
- Linhas não aprovadas: 2/91 = 2,2%. Abaixo de 30%, sem gate.
- R2 só para as 2 linhas. As outras 89 ficam byte a byte na v2.
- A mecânica passou inteira. Os dois CORRIGIR são de redação: os pontos que a produtora deixou para o QA.

## 1. Mecânica (script próprio, python -I, cópia em memória; scratchpad `cqfp_t123/qa.py`)

| critério | resultado |
|---|---|
| (a) 103 MARCA cobertas uma vez cada | PASSA. 0 não cobertas, 0 duplicadas. Nenhum VERIFICAR/FP coberto. Única EXTRA: GCB-EXTRA-01. Item, lote, leva e trecho conferem com o CSV de ocorrências; `id_edicao` sequencial de 0001 a 0091. |
| (b) `antes` literal, 1 ocorrência na justificativa, contém o `antes_unico` de cada ocorrência coberta, sem sobreposição | PASSA (0 erros). |
| (c) DELETAR só com `depois` vazio; `fonte_origem` em toda op. 6 e só nela | PASSA. 45 DELETAR, 46 SUBSTITUIR; op. 3 = 39, processo = 23, op. 6 = 29. |
| (d) Tabela aplicada: C-MARCAS (seção 8.1 do D1 da GBQ, mais "pertinência parcial", "objeto do", "base do D") nos 238 itens, enunciado e justificativa | PASSA. 108 casamentos antes, 0 depois. "Desconto em folha" no D3-R75: 1 no enunciado e 1 na justificativa, intactos. |
| (d) PROCESSO (`marcas_processo.py`) | 2 antes e 2 depois, os mesmos: "Presidência" em "Presidência da República", no D2-R21 e no D2-R24. São VERIFICAR/conteúdo pelo D1 da GCB, seção 1.4. Fora esses dois: 0. Ver pendência P1. |
| (e) Campos intocáveis | PASSA. `enunciado`, `gabarito`, `itemEdital`, `aderencia`, `lote`, `leva`, `j1` e `j2` idênticos nos 238. Os 153 itens sem MARCA têm justificativa byte a byte igual. Itens editados = itens com MARCA = 85. |
| (f) 4 VERIFICAR e 2 FP | PASSA. D4-R24 "produção", D2-R21 e D2-R24 "Presidência" e D3-R75 "folha" (enunciado e justificativa) intactos, com a mesma contagem. BQ-0113 está fora do reforço e não foi tocado. |

Observação: GCB-T123-0046 tem `categoria` C02, e o primeiro id coberto é C10. Está conforme a tabela C02 do D1 (seção 3, D3-R33). Não é falha.

## 2. Fontes (29 códigos, 100%)

Cada código foi conferido contra três referências:
- a linha "Base:" da leva, com a verificação de que a linha pertence ao item;
- a seção 5 do adendo do Anexo N (20/10 para os R; 22/10 para G6 e G9);
- a forma da seção 3.1 do `D4_registro_formato.md`.

| código(s) | Base e adendo | forma no texto | 3.1 / D1 |
|---|---|---|---|
| R37, R39, R40 | F5: Bouckaert, ENAP, RSP 75(1), 2024 | o artigo de Bouckaert (ENAP, 2024) | igual à forma do 3.1 |
| R43, R44, R45, R46 | F11: Silvestre, Enap, Coleção Gestão Pública, 2019 | o texto de Silvestre (ENAP, 2019) | exemplo do D1, seção 3 |
| R53, R54, R55, R57, R83 | F6: Cavalcante, Ipea, BAPI n. 19, 2018 | o texto de Cavalcante (Ipea, 2018) | igual à forma do 3.1 |
| R60, R62, R63, R64 | F1: TCU, Referencial Básico de Governança Organizacional, 3. ed., 2020 | o Referencial Básico de Governança Organizacional (TCU, 2020) | igual à forma do 3.1 |
| R65, R66, R67 | F10: CGU, documento didático "Cadeia de valor da CGU" (s.d.) | o documento didático da CGU | igual à forma do 3.1 (C8.4-03) |
| R72 | F7: Martins, Ipea, BAPI n. 19, 2018 | o texto de Martins (Ipea, 2018) | igual à forma do 3.1 |
| R74, R76, R77, R78, R79, R80, R81 | F3: Casa Civil/PR, Avaliação de Políticas Públicas: guia prático de análise ex post, v. 2, 2018 | o guia prático de análise ex post (Casa Civil, 2018); a segunda menção é "a mesma publicação" | igual à forma do 3.1 e do D1 |
| G6, G9 | F2: Guia da Política de Governança Pública, Casa Civil, 2018 | saem pela op. 3; a frase já nomeia "o Guia" | D1, seção 3 |

Resultado:
- Nenhuma fonte nova e nenhum NÃO IDENTIFICADO.
- As datas de consulta registradas (20/10/2026) conferem.

Nota de registro, sem reprovação de linha (a tabela de fontes está nas notas, e não no CSV):
- **G6.** A tabela cita como Base `DA_reforco_leva8_v2.md:543`. Essa linha é a Base do D4-R52. A Base do D4-R51 (l. 527) é G5. No D4-R51, G6 aparece na justificativa e no campo "Troca", e está identificado no adendo de 22/10, seção 5, l. 175. A deleção continua correta. A GCB acerta a referência na reconciliação.
- **R39 e R46.** A tabela cita só a Base do primeiro item que usa cada código. A Base do D4-R05 (l. 185) e a do D4-R11 (l. 279) também confirmam o código.

Amostragem no `normativo_cache` (7 trechos de Base localizados, 1 ocorrência cada): R37, R40, R45, R57, R64, R66 e G9. O R77 também está lá, em leiaute de colunas (l. 2595).

URLs abertas em 23/10/2026: o SHA-256 do PDF baixado é igual ao registrado no cache de 20/10/2026.

| código | URL | SHA-256 |
|---|---|---|
| R72 | https://repositorio.ipea.gov.br/server/api/core/bitstreams/12de44eb-314e-40b9-b57f-ff5455a059c3/content | 7100f026…5d02 |
| R53–R57 e R83 | https://repositorio.ipea.gov.br/server/api/core/bitstreams/a2ec054c-70e9-4cc4-9995-3101407c9647/content | dc9bd7ba…d3cf1; abre com "Pedro Cavalcante" |
| R65–R67 | https://repositorio.cgu.gov.br/bitstream/1/29544/10/documento_didatico_cadeia_valor.pdf (redireciona a basedeconhecimento.cgu.gov.br) | fc106e48…69898 |

Duas URLs não abriram:
- revista.enap.gov.br: ECONNREFUSED;
- o PDF da Casa Civil: acima de 10 MB para a ferramenta.

Nesses dois casos vale o cache de 20/10.

## 3. Mérito

Todas as 91 linhas foram lidas com 160 caracteres de contexto antes e depois da edição, no texto resultante. Resultado:
- **Alertas.** Em todas as linhas de alerta, a explicação ficou e só o código saiu.
- **"A moldura não decide o gabarito."** Saiu inteira, e só ela, nas 16 linhas.
- **Remissões a outros itens.** Saíram, e o conceito ficou:
  - "(caput)" e "(inciso VIII)";
  - "do inciso VI, que é outro critério";
  - "(art. 5º, XXIV)".
- **Base legal e aspas.** Ficaram. Exemplos: "Vide ADIN 4296"; "Lei 11.079, art. 2º, § 1º"; "art. 2º, VII e VIII, com transferência de recursos".
- **Remissões ao Anexo N.** As deleções do D4-R34 e do D4-R43 deixam a norma nomeada na mesma frase: Lei 11.079 e Decreto 9.203.
- **Pontuação.** Correta depois das retiradas: ponto e vírgula, ponto final e parêntese.
- **Fatos novos.** Nenhum. O texto não vai além da Base.
- **Conteúdo.** Nenhum "moldura", "folha" ou "cota" de conteúdo foi afetado.

### Pontos da seção (a) das notas, julgados

1. **"O documento didático da CGU", sem ano (R65/R66/R67; linhas 0029, 0030, 0034): APROVADO.**
   - A Base registra "sem data impressa", e o adendo registra "(s.d.)".
   - Pôr ano seria fato novo, e pôr "s.d." seria marca.
   - A forma é a do `D4_registro_formato.md` (3.1, C8.4-03).
   - O PDF baixado hoje é o mesmo do cache (mesmo hash).
2. **"Referencial" repetido no D4-R20 e no D4-R24 (linhas 0028 e 0032): CORRIGIR.**
   - Depois da troca, o D4-R24 diz que o Referencial "registra, no Referencial do TCU", e o D4-R20 diz que o Referencial lista diretrizes "do Referencial do TCU". A publicação passa a ser o lugar de si mesma: redação defeituosa no texto que a candidata lê.
   - O D1 já manda fundir, sem repetir, quando a frase identifica a publicação ("R64 (TCU)" → nome com órgão e ano). A correção aplica a mesma regra: alarga o `antes` e tira só a menção redundante.
   - Nenhuma palavra nova. Sentido e fonte preservados.
   - Textos exatos na tabela abaixo. Cada `antes` foi conferido: ocorre 1 vez e cobre o `antes_unico` (R60 / R62).

## 4. Veredito por linha

| id_edicao | item | op | ação | veredito |
|---|---|---|---|---|
| GCB-T123-0001 | D4-R01 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0002 | D4-R01 | 3 | DELETAR | APROVADO |
| GCB-T123-0003 | D4-R02 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0004 | D4-R03 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0005 | D4-R04 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0006 | D4-R05 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0007 | D4-R05 | 3 | DELETAR | APROVADO |
| GCB-T123-0008 | D4-R06 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0009 | D4-R07 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0010 | D4-R08 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0011 | D4-R09 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0012 | D4-R10 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0013 | D4-R11 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0014 | D4-R18 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0015 | D4-R13 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0016 | D4-R14 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0017 | D4-R14 | 3 | SUBSTITUIR | APROVADO |
| GCB-T123-0018 | D3-R01 | 3 | DELETAR | APROVADO |
| GCB-T123-0019 | D3-R02 | 3 | DELETAR | APROVADO |
| GCB-T123-0020 | D3-R04 | 3 | DELETAR | APROVADO |
| GCB-T123-0021 | D3-R09 | 3 | DELETAR | APROVADO |
| GCB-T123-0022 | D3-R12 | 3 | DELETAR | APROVADO |
| GCB-T123-0023 | D4-R15 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0024 | D4-R16 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0025 | D4-R17 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0026 | D4-R19 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0027 | D4-R19 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0028 | D4-R20 | 6 | SUBSTITUIR | CORRIGIR — antes: `R60 lista, entre as diretrizes para a boa governança do Referencial do TCU,` → depois: `O Referencial Básico de Governança Organizacional (TCU, 2020) lista, entre as diretrizes para a boa governança,` (ocorre 1 vez; sem palavra nova; tira a repetição, como na regra de fusão sem repetir da seção 3 do D1) |
| GCB-T123-0029 | D4-R21 | 6 | SUBSTITUIR | APROVADO (forma sem ano: ver seção 3, ponto 1) |
| GCB-T123-0030 | D4-R22 | 6 | SUBSTITUIR | APROVADO (forma sem ano: ver seção 3, ponto 1) |
| GCB-T123-0031 | D4-R23 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0032 | D4-R24 | 6 | SUBSTITUIR | CORRIGIR — antes: `R62 registra, no Referencial do TCU,` → depois: `O Referencial Básico de Governança Organizacional (TCU, 2020) registra` (ocorre 1 vez; sem palavra nova; o "produção" do VERIFICAR fica intacto) |
| GCB-T123-0033 | D4-R25 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0034 | D4-R26 | 6 | SUBSTITUIR | APROVADO (forma sem ano: ver seção 3, ponto 1) |
| GCB-T123-0035 | D4-R27 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0036 | D4-R27 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0037 | D4-R28 | 6 | SUBSTITUIR | APROVADO |
| GCB-T123-0038 | D1-R02 | 3 | DELETAR | APROVADO |
| GCB-T123-0039 | D3-R15 | 3 | SUBSTITUIR | APROVADO |
| GCB-T123-0040 | D3-R17 | 3 | DELETAR | APROVADO |
| GCB-T123-0041 | D3-R20 | 3 | DELETAR | APROVADO |
| GCB-T123-0042 | D3-R25 | 3 | SUBSTITUIR | APROVADO (absorve GCB-EXTRA-01; aderência "parcial" segue no campo) |
| GCB-T123-0043 | D3-R26 | 3 | DELETAR | APROVADO |
| GCB-T123-0044 | D3-R31 | 3 | SUBSTITUIR | APROVADO |
| GCB-T123-0045 | D3-R32 | 3 | DELETAR | APROVADO |
| GCB-T123-0046 | D3-R33 | processo | DELETAR | APROVADO (categoria C02 com 1º id C10: conforme a tabela C02 do D1; 10 ocorrências) |
| GCB-T123-0047 | D3-R36 | 3 | SUBSTITUIR | APROVADO |
| GCB-T123-0048 | D3-R37 | 3 | SUBSTITUIR | APROVADO |
| GCB-T123-0049 | D3-R43 | 3 | SUBSTITUIR | APROVADO |
| GCB-T123-0050 | D3-R44 | 3 | SUBSTITUIR | APROVADO |
| GCB-T123-0051 | D3-R46 | 3 | DELETAR | APROVADO |
| GCB-T123-0052 | D3-R49 | 3 | SUBSTITUIR | APROVADO |
| GCB-T123-0053 | D3-R50 | 3 | SUBSTITUIR | APROVADO |
| GCB-T123-0054 | D3-R51 | 3 | SUBSTITUIR | APROVADO |
| GCB-T123-0055 | D3-R52 | 3 | SUBSTITUIR | APROVADO |
| GCB-T123-0056 | D3-R53 | 3 | DELETAR | APROVADO |
| GCB-T123-0057 | D3-R54 | 3 | SUBSTITUIR | APROVADO |
| GCB-T123-0058 | D3-R55 | 3 | SUBSTITUIR | APROVADO |
| GCB-T123-0059 | D3-R56 | 3 | DELETAR | APROVADO |
| GCB-T123-0060 | D3-R57 | 3 | SUBSTITUIR | APROVADO |
| GCB-T123-0061 | D3-R58 | 3 | SUBSTITUIR | APROVADO |
| GCB-T123-0062 | D3-R59 | 3 | SUBSTITUIR | APROVADO |
| GCB-T123-0063 | D2-R02 | processo | DELETAR | APROVADO |
| GCB-T123-0064 | D2-R03 | processo | DELETAR | APROVADO |
| GCB-T123-0065 | D2-R05 | processo | DELETAR | APROVADO |
| GCB-T123-0066 | D2-R07 | 3 | DELETAR | APROVADO |
| GCB-T123-0067 | D2-R10 | processo | DELETAR | APROVADO |
| GCB-T123-0068 | D2-R25 | processo | DELETAR | APROVADO |
| GCB-T123-0069 | D2-R32 | processo | DELETAR | APROVADO |
| GCB-T123-0070 | D2-R35 | processo | DELETAR | APROVADO |
| GCB-T123-0071 | D2-R37 | processo | DELETAR | APROVADO |
| GCB-T123-0072 | D2-R39 | processo | DELETAR | APROVADO |
| GCB-T123-0073 | D2-R41 | processo | DELETAR | APROVADO |
| GCB-T123-0074 | D2-R45 | processo | DELETAR | APROVADO |
| GCB-T123-0075 | D2-R47 | processo | DELETAR | APROVADO |
| GCB-T123-0076 | D2-R48 | processo | DELETAR | APROVADO |
| GCB-T123-0077 | D2-R50 | processo | DELETAR | APROVADO |
| GCB-T123-0078 | D2-R54 | processo | DELETAR | APROVADO |
| GCB-T123-0079 | D2-R58 | processo | DELETAR | APROVADO |
| GCB-T123-0080 | D2-R65 | processo | DELETAR | APROVADO |
| GCB-T123-0081 | D2-R77 | processo | DELETAR | APROVADO |
| GCB-T123-0082 | D2-R77 | processo | DELETAR | APROVADO |
| GCB-T123-0083 | D3-R74 | processo | DELETAR | APROVADO |
| GCB-T123-0084 | D3-R77 | processo | DELETAR | APROVADO |
| GCB-T123-0085 | D3-R85 | processo | DELETAR | APROVADO |
| GCB-T123-0086 | D4-R31 | 3 | DELETAR | APROVADO |
| GCB-T123-0087 | D4-R34 | 3 | DELETAR | APROVADO (Lei 11.079 nomeada na frase) |
| GCB-T123-0088 | D4-R35 | 3 | DELETAR | APROVADO |
| GCB-T123-0089 | D4-R38 | 3 | DELETAR | APROVADO (frase abre com "O Guia") |
| GCB-T123-0090 | D4-R43 | 3 | DELETAR | APROVADO (Decreto 9.203 nomeado na frase) |
| GCB-T123-0091 | D4-R51 | 3 | DELETAR | APROVADO (frase já nomeia o Guia; ver nota de registro G6, seção 2) |

Contagem: APROVADO 89, CORRIGIR 2, REPROVADO 0 (2,2% não aprovadas).

## 5. Pendências

- **P1 (GBQ).** O critério "0 PROCESSO" da seção 8.1 do D1 da GBQ vai dar 2 no `conferir_t123.py`: "Presidência da República" no D2-R21 e no D2-R24. São conteúdo pelo D1 da GCB (VERIFICAR, seção 1.4), mas `marcas_processo.py` não os traz na lista X. A GBQ precisa registrar os dois como exceção de conteúdo (lista X ou equivalente) antes da conferência da montagem. Isso não afeta esta tabela.
- **P2 (GCB, reconciliação).** Acertar nas notas a referência de G6: a Base do D4-R51 é a l. 527 (G5), e o G6 está identificado no adendo de 22/10, seção 5, l. 175. Incluir as Bases do D4-R05 (l. 185) e do D4-R11 (l. 279).
- **R2.** A gcb-cpp grava `saida/gcb/T123_substituicoes_DA_v2.csv` só com 0028 e 0032 alteradas, e com `nota` "alargado (sem repetir)". A gcb-cqfp confere essas 2 linhas, o diff e a mecânica inteira.
