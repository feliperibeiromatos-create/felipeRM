# FORMATO_PLATAFORMA_DA.md — ordem do Fundador de 20/10/2026 (ORQUESTRADOR: LOTE, EXEC) — 2026-10-20 — gerado por orquestrador
Especificação de FORMA para entregar os lotes de Direito Administrativo (P1-DA) no formato da plataforma. Não cria regra de mérito; traduz as alíneas a, b, d e f da ordem. Vale para os seis lotes (D6, D1, D5, D2, D3, D4).

## 1. Saída por lote
Um arquivo JSON por lote: `saida/gcb/DA_plataforma/D<n>_plataforma.json`, UTF-8, com exatamente três chaves de topo, nesta ordem:
```json
{ "lote": {...}, "itens": [...], "topicos": {...} }
```
O pacote é montado depois, por script do orquestrador, a partir desses seis arquivos e de `saida/gcb/DA_plataforma/edital_DA.json` (46 entradas, já gerado e conferido contra o literal do edital).

## 2. `lote`
Campos, nesta ordem: `id`, `nome`, `prova`, `itensEdital`, `resumo`, `curso`, `pares`, `pegadinhas`.
- `id`: "D1", "D2", "D3", "D4", "D5" ou "D6" (chave interna; nunca aparece em texto exibido).
- `nome`: "Direito Administrativo — <assunto> (itens <x> a <y> do edital)", sem a palavra "Lote", sem código. Ex.: "Direito Administrativo — LAI e LGPD (itens 11 e 12 do edital)".
- `prova`: "P1".
- `itensEdital`: ids `P1-DA-<n>` do lote, na ordem do edital, incluindo o caput quando o lote tiver curso do caput (ex.: D1 → P1-DA-1, P1-DA-1.1, P1-DA-1.2, P1-DA-2, P1-DA-2.1, P1-DA-2.2).
- `resumo`: o resumo de uma página do lote (markdown), só com deleção de marcas de produção (seção 6).
- `curso`: markdown na estrutura da seção 3.
- `pares`: lista de `{ "a", "b", "como" }`, uma entrada por par confundível do arquivo canônico. `a` e `b` = os dois termos do par; `como` = a diferença, seguida de " Como a banca troca: " e o texto da coluna correspondente (ambos do arquivo de origem; só deleção de marcas e de códigos).
- `pegadinhas`: lista de `{ "itemEdital", "rotulo", "texto" }`, uma por pegadinha da lista consolidada do arquivo canônico. `itemEdital` = id P1-DA da folha a que ela pertence; `rotulo` = texto do edital desse id (copiado de `edital_DA.json`); `texto` = a pegadinha, com o dispositivo que a desfaz, sem o código (G-NN etc.).

## 3. `curso` — estrutura (a plataforma lê assim)
- Um bloco por entrada do edital com curso, na ordem do edital, aberto por `## <número> <TÍTULO>`: `<número>` é o número do edital sem o prefixo (`1`, `1.1`, `10.7`, `11`); `<TÍTULO>` é o texto do edital daquele id, em MAIÚSCULAS (pode ser encurtado só por corte no primeiro ":" quando passar de 90 caracteres). Ex.: `## 1.1 PRINCÍPIOS CONSTITUCIONAIS E DOUTRINÁRIOS DA ADMINISTRAÇÃO PÚBLICA`.
- Dentro do bloco, subtópicos opcionais com `### <Subtítulo em caixa normal>` (ex.: `### Transparência ativa (art. 8º)`). Nunca `###` em maiúsculas.
- Em cada subtópico (ou no bloco, se não houver subtópico), os quadros, cada rótulo sozinho numa linha, exatamente assim, nesta ordem, só os que o original tiver:
  - `DEFINIÇÃO` — a definição. Escrever o conteúdo do quadro num único parágrafo ou numa única lista sem linha em branco no meio (a plataforma fecha o quadro de definição na primeira linha em branco). Parágrafos explicativos adicionais vêm depois, como texto normal.
  - `BASE LEGAL` — dispositivos (art., inciso, parágrafo, alínea) que o original cita para aquele ponto, em lista `- Lei 12.527/2011, art. 8º, § 1º, I a VI`. Só o que o original já cita; nada novo. Doutrina sem dispositivo: omitir o quadro.
  - `EXEMPLO PARLAMENTAR` — o exemplo do original (contexto do Legislativo; manter "O exemplo é hipotético.").
  - `PEGADINHA PROVÁVEL` — a pegadinha do original, com o dispositivo que a desfaz.
- Proibido no curso: qualquer outra linha inteira em MAIÚSCULAS com 6 ou mais caracteres (a plataforma a transforma em título); linha com duas ou mais barras verticais que não seja tabela markdown (começa e termina com "|", com linha de separação `|---|`); emoji; HTML.
- Listas com "- "; numeração "1. ". Negrito com `**…**` permitido com moderação.

## 4. `itens`
Um objeto por item canônico do lote (aprovado; reprovados e retirados ficam fora), na ordem dos ids, com os campos nesta ordem:
`id` (o do arquivo canônico, ex.: "D1-01"), `rotulo` "AUTORAL", `certame` "Projeto Câmara 2026", `cargo` "Noções de Direito Administrativo e Administração Pública", `ano` 2026, `numero` (inteiro do id), `comando` (o comando do item, se o original tiver; senão "Julgue o item a seguir."), `textoBase` (situação hipotética separada, se o original separar; senão ""), `enunciado` (literal do original), `gabarito` ("C" ou "E", literal), `justificativa` (as duas linhas do original, só com deleção de marcas da seção 6), `itemEdital` (`P1-DA-<n>` da folha do item; itens de caput → id do caput, ex.: "P1-DA-1"), `aderencia` "direta", `url` (caminho do arquivo canônico, ex.: "saida/gcb/D1_v2.md"); e, só quando verdadeiro, `volatil`: true (item com marca VOLÁTIL ou REVERIFICAR).
Enunciado e gabarito não mudam nenhum caractere.

## 5. `topicos`
Objeto; chave = cada `P1-DA-<n>` do lote que tem bloco `##` no curso, na ordem do edital. Valor, nesta ordem e sem outros campos:
- `emUmMinuto`: lista de exatamente 3 frases curtas (cada uma até ~200 caracteres), tiradas só do curso daquele id.
- `resumo`: 150 a 250 palavras, só com o que está no curso daquele id (nada de fato novo, nenhum dispositivo que o curso não cite); parágrafos separados por linha em branco; nenhum parágrafo começa com algarismo, marca de lista ou RÓTULO EM MAIÚSCULAS seguido de dois-pontos.
- `visuais`: 1 ou 2 objetos, dos tipos abaixo, e nenhum outro campo:
  - `compare`: `{ "tipo":"compare", "titulo", "a", "b", "linhas": [[aspecto, lado A, lado B], ...], "legenda" }` — até 6 linhas.
  - `baseLegal`: `{ "tipo":"baseLegal", "titulo", "norma", "dispositivos": [ { "ref", "texto", "literal": true|false, "conferido": "AAAA-MM-DD" } ] }` — até 4 dispositivos. `texto` vem SÓ do mapa normativo do lote (`saida/gcb/D<n>_anexo_N_mapa_normativo.md`): `literal: true` quando copiado letra a letra da coluna de texto do mapa; `literal: false` quando condensado (sem mudar sentido). `conferido` = a data de consulta registrada no mapa para aquele dispositivo, em AAAA-MM-DD. Dispositivo sem data no mapa não entra. O dispositivo tem de estar citado no curso do tópico.
  - `esquema`: `{ "tipo":"esquema", "titulo", "centro", "ramos": [...] }` — 2 a 8 ramos.
  - `linha`: `{ "tipo":"linha", "titulo", "marcos": [ { "quando", "texto" } ] }` — 2 ou mais marcos.
  - `fluxo`: `{ "tipo":"fluxo", "titulo", "passos": [...] }` — 3 a 7 passos de até 48 caracteres.
  - `tabela`: `{ "tipo":"tabela", "titulo", "colunas": [...], "linhas": [[...]], "legenda" }` — cada linha com tantas células quantas colunas; `legenda` opcional.
- Todo dado de visual está no curso do tópico. Prazos, números e fases (em `linha`, `fluxo`, `tabela`, `compare`) só se estiverem no mapa normativo do lote; conferir lá.

## 6. Proibido em todo texto exibido (curso, resumo, pares, pegadinhas, enunciado, justificativa, topicos)
Referências de produção e códigos internos: "Lote", "lote D…", ids de item ("D1-01", "D6-33"…), códigos de bloco ou de lista ("C10.1-01", "L7.", "G12.", "G-07", "P-03", "PARTE 1.1"), fontes "F1"…"F22" e "[F…]", "[V …]", "[NORMATIVO — QA]", "QA PENDENTE", "trecho importado", "REVERIFICAR", "VOLÁTIL", "[TS]", "troca:", "elemento-isca", "BASE DOUTRINÁRIA" como marca, "Anexo N", "mapa normativo", "ficha", "seção X da ficha/do parecer", "R1", "R2", "v1", "v2", "acatado", nomes de agentes, de unidades (GCB, GBQ, GCE, EXEC) ou de ferramentas de IA, "[SEM FONTE — não afirmar]" (remover a marca e a frase que ela marca; frase sem fonte não vai à candidata).
Permitido: "Derep (antigo DETAQ)"; citações de lei por artigo; "O exemplo é hipotético."; datas de verificação na forma "verificado em dd/mm/aaaa" quando o original as tiver.

## 7. Regra de fidelidade (D6 e D1: "só reformatar, sem conteúdo novo")
Operações permitidas sobre o texto canônico: (1) mover trechos para a estrutura das seções 3 a 5; (2) trocar rótulos ("Definição:" → quadro DEFINIÇÃO; "Exemplo (Legislativo, hipotético):" → EXEMPLO PARLAMENTAR; "Pegadinha provável:" → PEGADINHA PROVÁVEL; "[Desfeita por: …]" → frase "Base: …" na mesma pegadinha); (3) deletar marcas e códigos da seção 6; (4) dividir parágrafo longo em lista sem mudar palavras; (5) em `topicos`, sintetizar (emUmMinuto, resumo, visuais) sem fato novo. (6) quando a deleção de uma marca quebrar a frase, a troca mínima pela expressão equivalente ("[TS]" → "troca sutil"; "(subitem 1.0)" → "do item 1"; "a ficha" → omitida com o trecho que a cita), sempre registrada. Nenhuma outra mudança de palavra. Na dúvida, manter o texto original.
Justificativa do item: as duas linhas do original unidas por um espaço; frases que só falam do processo (comparação com outro item do banco ou do lote, "difere de …", "mecanismo: …") ficam fora, registradas.
Registro obrigatório: `saida/gcb/DA_plataforma/D<n>_registro_formato.md` — lista de cada deleção de frase inteira (com o motivo, ex.: "[SEM FONTE]") e de cada caso em que o texto teve de mudar além das operações 1 a 4, e a correspondência bloco de origem → `##`/`###` de destino.

## 8. Conferência por script (o orquestrador roda; a produção deve passar antes de entregar)
`python3 -I saida/gcb/DA_plataforma/scripts/validar_da.py saida/gcb/DA_plataforma/D<n>_plataforma.json <arquivo canônico> <mapa normativo>` — esquema, padrões proibidos, contagem de palavras, enunciado literal no canônico, baseLegal literal no mapa e datas.
