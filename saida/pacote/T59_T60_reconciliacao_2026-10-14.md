# T59_T60_reconciliacao_2026-10-14.md — T-59 e T-60 (reconciliação D1 da GBQ; D-V15-AGORA, D-T64-V15) — 2026-10-14 — gerado por gbq-gerencia

REMETENTE: GBQ (gbq-gerencia, opus; não produziu nem revisou objeto destas tarefas)
DESTINATÁRIO: gbq-csc (correção do validador e errata v1.1 da regra; seção 3.1 e seção 5), produção-plataforma (correção A2; seção 3.2), gbq-cqe e QA-plataforma (reconferência; seção 4). Cópia: orquestrador (sequência, seção 5).

## 0. Objeto e base

- **QA lidos:**
  - `saida/pacote/QA_T59_2026-10-14_gbq-cqe.md`: APROVADO COM RESSALVAS (R-1 AGORA; R-2 PRÓXIMO; R-3 e O-1 BACKLOG; O-2 DESCARTADO; DÚVIDAS 23, 24 e 25);
  - `saida/plataforma/QA_T60_2026-10-14.md`: APROVADO COM RESSALVAS (A1 e A2 PRÓXIMO; A3 e A4 BACKLOG; A5 e A6 DESCARTADO).
- **Especificação:** `saida/pacote/T59_decisoes_2026-10-14.md` (D-T59-01 a D-T59-10).
- **Contexto:** D-V15-AGORA ("ir até o fim": QA, republicação no mesmo link, edição do estudante); D-T64-V15 (a T-64 entra na v1.5 e a T-61 será regerada). Orientação do orquestrador: corrigir já o que for pequeno e verificável, com uma rodada curta e reconferência do mesmo QA, sem abrir tarefa avulsa.
- **Estado lido** (somente leitura, sem alterar arquivo):

| Arquivo | SHA-256 |
|---|---|
| `regras/importacao_erros.md` (v1) | `b19bc0e4adf97e41…` |
| `regras/pacote_contrato.md` (v1.2.3) | `be037db8e7c06e1a…` |
| `saida/pacote/gerador_v1_5/validar_erros.py` | `19ab9c8b359e4a59…` |
| `saida/pacote/gerador_v1_5/validar_erros_teste.py` | `33132d5a9d9aaf7e…` |
| `saida/plataforma/plataforma_v1_5.html` (800 linhas) | `2ad1bdf8e6b6172a…` |
| `saida/pacote/pacote.json` (v1.5, antes da regeração da T-64) | `d6b8a5beae074851…` |

- **Fato de acoplamento conferido por leitura.** `gerador_v1_5/conferencias_v15.py`, conferência (6), exige que `regras/importacao_erros.md` seja igual, caractere a caractere, ao bloco D-T59-07 (linhas 503–507). Qualquer errata da regra quebra essa conferência na regeração da T-61. Isso foi tratado na seção 5.

## 1. Decisões (D1 da GBQ)

| Id | Ponto | Decisão | Classe |
|---|---|---|---|
| D-R59-01 | **R-1** (ordem das listas não conferida) | Acatada. O validador passa a conferir a ordem das cinco listas da tabela D-T59-02 e emite **aviso**, sem recusa e sem tirar nada dos cálculos. A seção 2 da regra só lista forma e tipo como motivos de recusa | **AGORA** |
| D-R59-02 | **R-2** (`NaN`/`Infinity` aceitos) | Promovida a AGORA. É uma linha, verificável, e entra na mesma rodada: constante não JSON → RECUSADO "não abre como JSON UTF-8" | **AGORA** |
| D-R59-03 | **R-3** (BOM recusado) | Decidido **tolerar** o BOM UTF-8 inicial, com aviso. O caminho "texto copiado" (regra, 1.1) passa por editor; perder a matéria da semana por um BOM é desproporcional. O SHA-256 continua calculado sobre os **bytes recebidos**. O mesmo conteúdo, com e sem BOM, cai em DUPLICADO pelo `exportadoEm` | **AGORA** (mesma rodada) |
| D-R59-04 | **O-1** ("ordem" no contrato = ordem das listas) | Leitura fixada aqui: no contrato v1.2.3, "ordem" é a **ordem das listas**; a das chaves não importa (D-T59-02, regra 3). Errata de texto do contrato só na próxima errata dele, para não mudar o SHA-256 da v1.2.3 que a T-61 cita | BACKLOG |
| D-R59-05 | **O-2** (rótulo "IMPORTAÇÃO DUPLICADO") | Confirmado | DESCARTADO |
| D-R59-06 | **DÚVIDA 23** (T-61 executada antes do QA da T-59) | **Ratificada**, sem efeito: o contrato v1.2.3 foi aprovado sem alteração de texto. A ordem da D-T59-10, item 4, continua valendo para as próximas ocorrências da T-12 | registro |
| D-R59-07 | **DÚVIDA 24** (pasta `entrada/erros/` sem LEIA-ME) | Aceita | DESCARTADO |
| D-R59-08 | **DÚVIDA 25** (nome e local do validador) | **Ratificada a recomendação da gbq-cqe.** Nome `validar_erros.py` aceito. A **cópia mantida** fica em `saida/treino/ferramentas/validar_erros.py`, com o teste `saida/treino/ferramentas/validar_erros_teste.py`. As correções R-1, R-2, R-3 e A1 vão **só** nessa cópia. A cópia de `saida/pacote/gerador_v1_5/` fica **congelada** como registro da T-61 (SHA `19ab9c8b…` e `33132d5a…` inalterados) e é marcada no `MANIFESTO.md` na regeração da T-61, que já vai tocá-lo (lógica de "marcar em vez de mover", D-T57-10). A T-62 e o QA-plataforma usam a cópia mantida | **AGORA** |
| D-R60-01 | **A1** (NE decimal faz o validador recusar o arquivo inteiro) | **Decidido pelo validador, não pela plataforma.** `ne` e `tl` fora do domínio passam a ser **incoerência só daquela discursiva**: ela é listada, a autoavaliação dela (`notas`, `ne`, `nota`) sai do diagnóstico, o `texto` segue para a correção dupla e o arquivo **não é recusado**. Motivos: (1) cobre também o estado já gravado no aparelho pela v1.4 publicada, que pode ter `ne` decimal; normalizar só na entrada da plataforma não cobriria esse estado, e normalizar na exportação violaria a D-T59-02, regra 2 ("sem arredondar"); (2) mantém o diff da v1.5 restrito ao botão (4.3.7) e a tela da discursiva intacta; (3) protege a rodada de 18/10 contra qualquer outra causa. O formato emitido **não muda**: `ne` e `tl` continuam "inteiro" na tabela D-T59-02, e `versaoFormato` continua 1 (D-T59-06 trata do formato, não da tolerância da importação). Errata v1.1 de `regras/importacao_erros.md` (seção 3.1, item B). A guarda na entrada da plataforma (`step="1"` e valor inteiro) vai para a próxima versão que tocar a discursiva | **AGORA** (validador e regra); BACKLOG (plataforma) |
| D-R60-02 | **A2** (foco perdido depois de exportar) | Acatada e promovida a AGORA. É uma correção de duas linhas em `exportarErros`, verificável pelo próprio caso 17 do QA, e melhora o que vai ao ar agora. Entra na v1.5, sem v1.5.1: o arquivo ainda não foi publicado | **AGORA** |
| D-R60-03 | **A3** (toast "Não foi possível preparar o arquivo.") | **Ratificado o texto.** Ele passa a integrar o quadro 4.2 da D-T59-09 como "toast — falha ao montar o arquivo (estado corrompido)". Nenhuma mudança de código | DESCARTADO (como achado) |
| D-R60-04 | **A4** (`pacote.versao` ausente num pacote carregado à mão) | Mantido BACKLOG. É inalcançável com qualquer pacote da fábrica, e `versao: P.versao ?? null` sozinho só trocaria "campo ausente" por "tipo errado" no validador | BACKLOG |
| D-R60-05 | **A5** e **A6** | Confirmados | DESCARTADO |
| D-R60-06 | Propostas T-66 e T-67 do QA-plataforma | **Não abertas.** A1 e A2 se resolvem nesta rodada curta (orientação do orquestrador). Os resíduos BACKLOG vão numa linha só (seção 7) | — |

Gates: nenhum. Não há reprovação acima de 30%, fonte não oficial, conflito entre Gerências nem matéria fora do domínio.

## 2. Leitura de impacto (o que NÃO muda)

1. **`pacote.json` e edição do estudante:** nada desta reconciliação muda o conteúdo deles. O delta da v1.5 continua sendo o da D-T59-10 mais o da T-64 (c) (D-T64-V15).
2. **Contrato v1.2.3:** não muda (SHA `be037db8…`); a T-61 continua citando-o.
3. **Formato do arquivo exportado (D-T59-01 a 06):** não muda. As correções são de **tolerância da importação** (validador e regra) e de **foco** (plataforma).
4. **`gerador_v1_5/validar_erros.py` e `validar_erros_teste.py`:** não mudam (congelados).

## 3. LISTA DE CORREÇÕES AGORA

### 3.1 (i) Validador e regra — gbq-csc (produção, sonnet)

Saída da produção: `saida/pacote/T59_correcao_2026-10-14.md`, com o SHA-256 antes e depois de cada arquivo tocado, o diff e a saída integral do teste.

**A. Cópia mantida (D-R59-08)**

| # | Correção | Critério verificável |
|---|---|---|
| V-0 | Copiar `saida/pacote/gerador_v1_5/validar_erros.py` para `saida/treino/ferramentas/validar_erros.py` (a pasta é criada). No cabeçalho, acrescentar: "Versão mantida (D1 da GBQ, `saida/pacote/T59_T60_reconciliacao_2026-10-14.md`, D-R59-08). A cópia de `gerador_v1_5/` é registro da T-61 e não muda." | A cópia de `gerador_v1_5/` continua com o SHA `19ab9c8b…` |
| V-0a | `PACOTE_PADRAO` passa a ser derivado da raiz do repositório: `REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))` e `PACOTE_PADRAO = os.path.join(REPO, 'saida', 'pacote', 'pacote.json')` | Sem `--pacote`, rodado de qualquer diretório, o validador lê `saida/pacote/pacote.json` |

**B. Correções na cópia mantida**

| # | Origem | Texto ou regra atual | Regra nova (exata) | Critério verificável |
|---|---|---|---|---|
| V-1 | R-1 | Ordem não conferida | Depois da coerência, conferir a ordem e acrescentar a `R['avisos']` uma linha `ordem: <lista> fora da ordem <critério> (primeira posição divergente: índice k)` para cada lista fora de ordem. Os critérios: `caderno` pela chave `(-errou, id)` não decrescente; `respostasCaderno` por `em` não decrescente; `tentativas` por `data` não decrescente; `saidas` por `em` não decrescente; `discursivas` por `id` não decrescente. As strings ISO são comparadas como texto, porque o formato é fixo; os ids, como texto. O aviso não muda o veredito, o código de saída nem `fora_dos_calculos` | 1 caso por lista fora de ordem → ACEITO, código 0, 1 aviso `ordem:`. Os casos em ordem e com empate de data → nenhum aviso |
| V-2 | R-2 | `json.loads(txt)` | `json.loads(txt, parse_constant=f)`, em que `f` levanta `ValueError('constante não JSON: %s')` | `NaN`, `Infinity` e `-Infinity` em qualquer campo → RECUSADO, código 1, motivo começando por "não abre como JSON UTF-8" |
| V-3 | R-3 | `raw.decode('utf-8')` recusa o BOM | Se `raw` começa por `b'\xef\xbb\xbf'`, decodificar `raw[3:]` e acrescentar a `R['avisos']` "arquivo com BOM UTF-8 (tolerado; SHA-256 calculado sobre os bytes recebidos)". `R['sha256']` e `R['bytes']` continuam sobre `raw` | O exemplo com BOM → ACEITO com o aviso, e SHA ≠ o do mesmo arquivo sem BOM. Com `--importados` contendo o `exportadoEm` do arquivo sem BOM → DUPLICADO. O BOM seguido de Latin-1 continua RECUSADO |
| V-4 | A1 | `'tl': (is_int, 'inteiro')` e `'ne': (is_int, 'inteiro')` em `disc` (forma, que leva a recusa) | Forma: `ne` precisa ser número (`is_num`) e `tl`, número ou null. String, booleano, objeto ou `ne` null continuam RECUSADO. Coerência, em `coerencia()`: para cada `discursivas[i]`, se `ne` não for inteiro ≥ 0 (`is_int` estrito: `1.0` conta como não inteiro, como no resto do validador) ou `tl` não for inteiro ≥ 1 (inclusive null e 0), registrar `('discursivas[i] (<id>)', 'ne=<v> (deve ser inteiro >= 0)')` e/ou `'tl=<v> (deve ser inteiro >= 1)'`, e incluir `i` em `R['fora_dos_calculos']['discursivas']` (chave nova; as chaves `tentativas` e `caderno` não mudam). A linha de texto "INCOERÊNCIAS" passa a mostrar também `discursivas [...]` | `ne` 1.5, `ne` −1, `ne` 1.0, `tl` null, `tl` 0 e `tl` 2.5 → ACEITO, incoerência listada e `fora_dos_calculos.discursivas == [i]`. `ne` "1", `ne` true, `ne` null e `tl` "3" → RECUSADO. O arquivo `qa_ne_decimal` do QA-plataforma → ACEITO com 1 incoerência de discursiva |
| V-5 | — | Docstring: "RECUSADO -- … ou o tipo está errado" | Acrescentar: "`ne`/`tl` numéricos fora do domínio são incoerência da discursiva, não recusa (regra v1.1, 2.5); BOM inicial tolerado com aviso; `NaN`/`Infinity` recusados; ordem das listas gera aviso" | Leitura |

**C. Teste da cópia mantida**

| # | Correção | Critério verificável |
|---|---|---|
| V-6 | `saida/treino/ferramentas/validar_erros_teste.py` é **autônomo**: não importa `common` nem nada do gerador; deriva `REPO` como em V-0a; usa `saida/pacote/pacote.json` e `saida/pacote/exemplo_erros_v1.json`; grava os casos fictícios num diretório temporário (`tempfile.mkdtemp()`), apagado ao fim, e **nada no repositório**; chama o validador em processo separado com `python3 -I`. Mantém todos os casos do teste atual e acrescenta: 5 de ordem (um por lista) e 1 de empate; 3 de constante (`NaN`, `Infinity`, `-Infinity`); 3 de BOM (aceito, duplicado e BOM + Latin-1); os 10 casos de V-4 | `python3 -I saida/treino/ferramentas/validar_erros_teste.py` → 0 FALHA e código 0, rodado da raiz e de outro diretório; `git status` sem arquivo novo fora dos dois `.py` |

**D. Errata v1.1 de `regras/importacao_erros.md`** (somente estas 5 substituições, cada uma com ocorrência única; abortar se ≠ 1; nada mais muda)

| # | Onde se lê | Leia-se |
|---|---|---|
| E-1 | linha 1: `… (plataforma → fábrica) — v1, 2026-10-14 — D1 da GBQ (saida/pacote/T59_decisoes_2026-10-14.md)` | `… (plataforma → fábrica) — v1.1, 2026-10-14 — D1 da GBQ (saida/pacote/T59_decisoes_2026-10-14.md; errata v1.1: saida/pacote/T59_T60_reconciliacao_2026-10-14.md)` |
| E-2 | `## 2. Validação (gbq-csc, por script `python3 -I`, somente leitura; resultado na seção "Validação" do diagnóstico)` | `## 2. Validação (gbq-csc, por script `python3 -I`, somente leitura, com o validador mantido em `saida/treino/ferramentas/validar_erros.py`; resultado na seção "Validação" do diagnóstico)` |
| E-3 | `   - abrir como JSON UTF-8;` | `   - abrir como JSON UTF-8 (`NaN`, `Infinity` e `-Infinity` não são JSON; um BOM UTF-8 inicial é tolerado e registrado como aviso);` |
| E-4 | `   - ter todos os campos da tabela do contrato, com os tipos dela.` | `   - ter todos os campos da tabela do contrato, com os tipos dela, salvo que, em `discursivas`, basta `ne` ser número e `tl` ser número ou null (o valor fora do domínio é tratado no item 5).` |
| E-5 | a linha do item 5, `5. **Coerência.** … o restante do arquivo é usado.` | a mesma linha, seguida destas duas (indentação de 3 espaços):<br>`   - **Discursiva.** `ne` que não seja inteiro ≥ 0, ou `tl` que não seja inteiro ≥ 1 (inclusive null), é incoerência daquela discursiva: ela é listada com o motivo, e a autoavaliação dela (`notas`, `ne`, `nota`) fica fora do diagnóstico (3.1, item 7, registra "autoavaliação incoerente"). O `texto` segue para a correção dupla (3.3), e o arquivo não é recusado.`<br>`   - **Ordem.** A ordem das listas da tabela D-T59-02 (caderno por `errou` decrescente e depois `id`; `respostasCaderno`, `tentativas` e `saidas` por data não decrescente; `discursivas` por `id`) é conferida. Lista fora de ordem gera aviso, sem recusa e sem tirar nada dos cálculos.` |

Critério: o arquivo novo é igual à v1 (SHA `b19bc0e4…`) com E-1 a E-5 aplicadas, caractere a caractere: 2 linhas a mais, 4 linhas trocadas e as demais idênticas e na mesma ordem. Sem BOM nem CR. Os trechos entre crases simples nas colunas acima são literais do arquivo; nenhuma cerca é inserida.

### 3.2 (ii) Plataforma — produção-plataforma (sonnet)

Objeto: `saida/plataforma/plataforma_v1_5.html` (SHA `2ad1bdf8…`), editado no lugar, porque a v1.5 ainda não foi publicada. Saída da produção: `saida/plataforma/T60_correcao_2026-10-14.md`, com o SHA antes e depois e o diff.

| # | Origem | Texto atual (linhas 767–768) | Texto novo | Critério verificável |
|---|---|---|---|---|
| P-1 | A2 | `  const rot="Exportar meus erros"; btn.disabled=true; btn.textContent="Preparando…";` | `  const rot="Exportar meus erros"; const comFoco=document.activeElement===btn; btn.disabled=true; btn.textContent="Preparando…";` | `diff` v1.5 (`2ad1bdf8…`) → nova: exatamente 2 linhas trocadas, as 767 e 768, e nenhuma outra |
| P-2 | A2 | `  const fim=()=>{ if(btn.isConnected){ btn.disabled=false; btn.textContent=rot; } };` | `  const fim=()=>{ if(btn.isConnected){ btn.disabled=false; btn.textContent=rot; if(comFoco) btn.focus(); } };` | Depois de "Arquivo salvo.", "Arquivo não salvo.", "Já há um pedido…", "Texto copiado…" e "nada a exportar", com acionamento por teclado: `document.activeElement` é o `#exp`. No caminho do campo, o foco continua indo ao `textarea` (o `ta.focus()` vem depois do `fim()`) |

Fora da correção (decidido): a tela da discursiva **não** muda (D-R60-01); o toast de A3 fica como está (D-R60-03); A4 é BACKLOG. Na republicação, o conjunto completo de capacidades é `{downloads: true}` (D-T59-09, 4.3.2).

## 4. Roteiro de reconferência

### 4.1 gbq-cqe — T-59, rodada 2 (somente leitura; scripts próprios em `python3 -I`)

1. **Regra v1.1.** Reconstruir a v1 (`b19bc0e4…`) com E-1 a E-5 desta seção 3.1-D e comparar com `regras/importacao_erros.md` caractere a caractere. Conferir: nada mais mudou; sem BOM nem CR; os 4 títulos de seção estão intactos; "(v1.2.3)" está presente.
2. **Congelamento.** `gerador_v1_5/validar_erros.py` = `19ab9c8b…` e `validar_erros_teste.py` = `33132d5a…`.
3. **Diff da cópia mantida.** O diff de `saida/treino/ferramentas/validar_erros.py` contra `19ab9c8b…` fica restrito a V-0, V-0a e V-1 a V-5.
4. **Suíte própria.** Rerrodar a `qa59_validador.py` apontada para a cópia mantida, sem `--pacote` (testa V-0a). As 175 conferências da rodada 1 mantêm o resultado, salvo as três notas, que se invertem: (a) ordem → 4 de 4 com aviso `ordem:` e veredito ACEITO; (b) `NaN`, `Infinity` e `-Infinity` → RECUSADO; (c) BOM → ACEITO com aviso, SHA sobre os bytes recebidos, e DUPLICADO contra o mesmo `exportadoEm`. Acrescentar os 10 casos de V-4 e o arquivo `qa_ne_decimal` do QA-plataforma, com o resultado esperado na tabela.
5. **Teste da produção.** Rodar `validar_erros_teste.py` da raiz e de outro diretório: 0 FALHA, e `git status` sem resíduo.
6. **Mesma sessão, T-61 regerada** (QA da T-61): conferir os 3 pontos da seção 5, item 3. São eles: a conferência (6) contra a v1.1 reconstruída; o `MANIFESTO.md` com os dois arquivos marcados "registro" e o SHA inalterado; e o `pacote.json` e a edição sem nenhuma diferença atribuível a esta reconciliação.
7. Saída: `saida/pacote/QA_T59_R2_2026-10-14_gbq-cqe.md`, com veredito e, se houver, achados classificados.

### 4.2 QA-plataforma — T-60, rodada 2 (somente leitura; os mesmos scripts da rodada 1)

1. **Diff.** `2ad1bdf8…` → nova: exatamente P-1 e P-2 e nada mais. Registrar o SHA novo.
2. **Suíte inteira.** Rerrodar `qa_export.js`, `qa_regressao.js`, `qa_posicao.js` e `conferir_qa.py`. A rodada 1 teve 780 verificações de navegador e 69 arquivos. Esperado: 0 falha. As 2 falhas A2 do caso 17 passam a OK, e os 69 arquivos ficam idênticos ao esperado, fora `exportadoEm`.
3. **Foco, caso a caso.** Acionando por Tab e Enter nas duas telas: depois de salvo, recusado, `rate_limited`, copiado e "nada a exportar", `activeElement` = `#exp`, com o rótulo "Exportar meus erros" e o botão habilitado. No caminho do campo, `activeElement` = `#expTxt`. Com clique de mouse, registrar se `#exp` casa `:focus-visible`. Isso é só registro e não reprova.
4. **Validador.** Passar os arquivos capturados pela cópia mantida `saida/treino/ferramentas/validar_erros.py`, se já aprovada pela gbq-cqe: esperado ACEITO e **nenhum aviso `ordem:`**. Também o arquivo `qa_ne_decimal`: esperado ACEITO, com 1 incoerência de discursiva. Se a cópia mantida ainda não estiver pronta, usar a de `gerador_v1_5` mais a conferência de ordem por script próprio, como no caso 13, e registrar a pendência.
5. Saída: `saida/plataforma/QA_T60_R2_2026-10-14.md`.

### 4.3 Critério de fechamento

- T-59 e T-60 ficam CONCLUÍDAS na **reconciliação conjunta da T-61** (gbq-gerencia, a mesma que emite o gatilho A). Ela confere os dois vereditos da rodada 2, sem nova reconciliação separada destas tarefas.
- Se uma rodada 2 trouxer achado, ele volta à gbq-gerencia antes do gatilho A.
- **Exceção que não segura o gatilho A:** um achado só no **validador** (cópia mantida), que não vai ao ar. Nesse caso, desde que a regra v1.1 esteja literal (item 4.1.1), o gatilho A pode sair, e o validador ganha nova rodada curta antes de 18/10 (primeira T-62).

## 5. Sequência para o orquestrador

1. **Em paralelo:**
   - gbq-csc aplica a seção 3.1 (A a D);
   - produção-plataforma aplica a seção 3.2.

   Os dois objetos são independentes.
2. **QA-plataforma** faz a rodada 2 da T-60 (4.2), assim que P-1 e P-2 estiverem gravados.
3. **T-61 regerada** (gbq-csc), pela T-64 (c) e por D-T64-V15, **depois** da errata v1.1 da regra. Ela acrescenta só três ajustes internos ao gerador, que não mudam o pacote nem a edição:
   1. em `conferencias_v15.py`, a conferência (6) compara `regras/importacao_erros.md` com o bloco D-T59-07 **com E-1 a E-5 aplicadas**, reconstruído por script (mesmo padrão da reconstrução do contrato);
   2. o `MANIFESTO.md` marca `validar_erros.py` e `validar_erros_teste.py` como "registro (T-59); versão mantida em `saida/treino/ferramentas/` (D-R59-08)", com o SHA inalterado;
   3. o relatório da v1.5 cita a regra como "v1.1, 2026-10-14 (errata em `T59_T60_reconciliacao_2026-10-14.md`)".
4. **gbq-cqe** faz, na mesma sessão, a rodada 2 da T-59 (4.1) e o QA da T-61 regerada.
5. **gbq-gerencia** faz a reconciliação conjunta da T-61, fecha T-59 e T-60 e emite o gatilho A. Depois vêm a republicação no mesmo link (artefato `5fyXGpFMomSHwZuRnu36rC`, com capacidades `{downloads: true}`) e a edição v1.5, por D-V15-AGORA.
   - Recomendação, não bloqueante: depois da republicação, fazer uma exportação real no link publicado antes de avisar a candidata. Isso confere a confirmação real da viewer, que o QA só simulou. O que se diz à candidata, e quando, é do Fundador.

## 6. Estados propostos

- **T-59:** EM CURSO. A reconciliação R1 deu APROVADO COM RESSALVAS e abriu a correção curta AGORA (validador mantido em `saida/treino/ferramentas/`; regra v1.1). Seguem a reconferência gbq-cqe (R2) e o fechamento como CONCLUÍDA na reconciliação conjunta da T-61. O contrato v1.2.3 está aprovado para o efeito da D-T59-10, item 4.
- **T-60:** EM CURSO. O QA deu APROVADO COM RESSALVAS e abriu a correção A2 (2 linhas). Seguem a reconferência QA-plataforma (R2) e o fechamento como CONCLUÍDA na reconciliação conjunta da T-61. A publicação no mesmo link vem depois do gatilho A.

## 7. BLOCO TAREFAS

```
T-59 (estado proposto): EM CURSO — reconciliada R1 (APROVADO COM RESSALVAS) em saida/pacote/T59_T60_reconciliacao_2026-10-14.md; correção curta AGORA (gbq-csc: validador mantido em saida/treino/ferramentas/ com R-1, R-2, R-3, A1; regras/importacao_erros.md v1.1) → reconferência gbq-cqe (QA_T59_R2) → CONCLUÍDA na reconciliação conjunta da T-61.
T-60 (estado proposto): EM CURSO — QA APROVADO COM RESSALVAS; correção A2 (foco ao botão, 2 linhas em plataforma_v1_5.html) → reconferência QA-plataforma (QA_T60_R2) → CONCLUÍDA na reconciliação conjunta da T-61; publicação no mesmo link após gatilho A, capacidades {downloads: true}.
T-61 (anotação ao escopo, sem mudar pacote nem edição): na regeração pela T-64 (c), conferência (6) contra regras/importacao_erros.md v1.1 reconstruída; MANIFESTO marca gerador_v1_5/validar_erros*.py como registro (versão mantida em saida/treino/ferramentas/); relatório cita a regra v1.1 (T59_T60_reconciliacao_2026-10-14.md, seção 5).
T-66; GBQ; Resíduos BACKLOG da T-59/T-60 (T59_T60_reconciliacao_2026-10-14.md): (1) plataforma, na próxima versão que tocar a discursiva: input NE com step="1" e valor inteiro ≥ 0 (A1, lado da plataforma); (2) plataforma: pacote.versao ausente num pacote carregado à mão (A4), junto com a tolerância correspondente no validador; (3) contrato, na próxima errata: "ordem" → "ordem das listas" na seção Exportação de erros (O-1); BACKLOG; PENDENTE; gbq-gerencia (D1) → produção-plataforma / gbq-csc → QA dono; saida/plataforma/ + regras/pacote_contrato.md
```

(Se o id T-66 já estiver ocupado quando o orquestrador gravar, usar o próximo livre.)

## 8. BLOCO PARA_PRESIDENCIA

nenhum. As decisões são D1 no domínio da GBQ: formato, importação, validador e a interface do botão definida na D-T59-09. O gatilho A sai na reconciliação conjunta da T-61.

FIM — gbq-gerencia, 14/10/2026.
