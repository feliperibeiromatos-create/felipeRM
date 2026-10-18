# T-108 e T-109 — ensaio do gerador_v1_11 — 2026-10-18 — gerado por gbq-csc

Natureza: nota de execução da implementação (D1 da GBQ, `saida/pacote/T108_D1_pacote_M2_2026-10-18.md`, seções 1 a 4). Fase ENSAIO: nada promovido, nada gravado em `saida/` fora de `saida/pacote/gerador_v1_11/` e desta nota. Não alterei `gerador_v1_10`, as tabelas das Gerências, `pacote.json`, `pacote_estudante.json`, TAREFAS.md, DECISOES.md nem PARA_PRESIDENCIA.md; sem commit. Tudo roda com `python -I -B` por `_run.py`; `sh saida/pacote/gerador_v1_11/rodar_tudo.sh` refaz tudo (cerca de 30 s), para na primeira falha e deixa o resultado em `out/` e `MANIFESTO.md`.

## 1. O que foi implementado

Pasta `saida/pacote/gerador_v1_11/` = cópia de `gerador_v1_10/` sem `out/` e sem `__pycache__/`. O número da versão vem só de `config_v111.VERSAO` (`NOME`, `NOME_E` e `TAG` derivam dele; C-16 varre os literais).

| Arquivo | Estado frente ao v1_10 | Papel |
|---|---|---|
| `config_v111.py` | novo | VERSAO, ALVO=M2, BASE (cacd606 e SHA-256), SHA do inventário (fixado em 471aeec5…) e do T109 (bb95046b…), tabelas (ENSAIO e FINAL), E_L2R16, ATO_L2R16, exceções, `confere_final()` (E1 a E5) |
| `tabelas_v111.py` | novo | leitura e forma das tabelas (BOM, `\r`, colunas, ações, regras, prefixos), cobertura dos 872 ids, FP fora de linha, resolução de `caminho` (inclui ids com ponto, como `quesitos[2.1]`) |
| `limpeza_v111.py` | novo | aplicação ocorrência a ocorrência (antes único, casamentos no intervalo, sem sobreposição, FP intactos, proibições do `depois`, "verificado em" e base legal), campo `interno`, `reverte()` |
| `build_v111.py` | novo | passo 1: base do git, tabelas, limpeza, troca do L2-R16 pela linha do T109, `nome` e `geradoEm`, reversibilidade (C-5), `stats` e `folhas` |
| `estudante_json_v111.py` | novo (cópia alterada) | passo 2: -E a partir do `pacote.json` limpo, sem `interno`; listas de deleção viram verificação residual |
| `registro_adendo_v111.py` | novo | passo 3: `out/registro_adendo3.md` |
| `estudante_md_v111.py` | novo | passo 4: 35 arquivos a partir dos blobs da v1.10, troca campo a campo com contagem esperada por arquivo, linha do L2-R16, NUCLEO.md, README |
| `registro_alteracoes_v111.py` | novo | passo 5: CSV por id (773 linhas = 772 edições + L2-R16), bloco MANTER à parte e resumo |
| `validate_v111.py`, `conferencias_v111.py` | novos | passos 6 e 7: C-1 a C-16, C-17 informativa, mais C-G1 (arquivos do gerador frente ao v1_10) e C-G2 (nada promovido tocado) |
| `inventario_v111.py` | novo | cópia do `T108_inventario.py` com caminhos por argumento, posições dos casamentos e varredura dos .md (mesmas regras e classes) |
| `fidelidade_mutacao_v111.py` | novo | bloco M: 22 casos (controle mais 21 mutações) |
| `marcas_x_v111.py` | novo | entradas X propostas pelo ensaio (ver 3.2) |
| `manifesto_v1_11.py`, `rodar_tudo.sh` | novo / alterado | passo 10 e o runner |
| `_run.py`, `validar_erros_teste.py` | alterados | saída em UTF-8 e subprocessos com `-X utf8` (no Windows o padrão é cp1252 e o validador de erros quebrava) |
| `ensaio/gera_tabelas_ensaio.py` | novo | passo 0 (só ENSAIO), ver 2 |

Os demais arquivos são herdados iguais (registro; `nucleo.py`, `common.py`, `refs.py`, `estudante_gen.py` etc. continuam ativos como módulos).

## 2. Tabelas de ensaio

As tabelas em produção existiam parcialmente no momento da execução (GCE 263 linhas; GCB partes A 178, B 175 e C 155; a da GBQ ainda não está em `saida/pacote/`). O passo 0 lê cada uma linha a linha, guarda só as linhas que passam em todas as conferências do gerador (GCE 178, GCB-A 150, GCB-B 175, GCB-C 155) e acrescenta as 4 linhas da GBQ (seção 1.9) e 111 linhas sintéticas de ensaio (GCE-9nnn: 83; GCB-C9nnn: 28; janela única de texto com o casamento retirado), para cobrir os 872 ids. As sintéticas só exercitam o gerador; não são conteúdo. Saídas em `ensaio/` (3 CSV, `relatorio_ensaio.json`, `excecoes_ensaio.json`). SHA-256 das tabelas de produção lidas: GCE 5732a193…, GCB-A 3e83a970…, GCB-B a2463cc6…, GCB-C 31d8b6b0…. Em ENSAIO, `config_v111.TABELAS` aponta para `ensaio/`; em FINAL aponta para `saida/gce/T108_substituicoes_GCE.csv`, `saida/gcb/T108_substituicoes_GCB.csv` e `saida/pacote/T108_substituicoes_GBQ.csv`.

Achados das linhas reais (para as Gerências ou para a GBQ):
- 103 linhas (GCE 75, GCB-A 28) são DELETAR com `depois` não vazio (a deleção é do trecho do `antes` menos o `depois`, p.ex. `REVERIFICAR. Os` -> `Os`). A D1 (seção 1.3, ponto 3) manda `depois` vazio em DELETAR. Ou a Gerência troca a ação para SUBSTITUIR, ou a GBQ relaxa a regra. O gerador recusa como está.
- 5 linhas da GCE citam ids `NAO_INVENTARIADA-nn` (GCE-0110, 0238, 0260, 0261, 0263), que não existem no inventário; 4 linhas (GCE-0105, 0206, 0207, 0213) citam um id cujo casamento fica fora do intervalo do `antes`; GCE-0211 perde o termo "inciso" (regra do ponto 8).
- Fora isso, as 658 linhas restantes passaram em tudo.

## 3. Resultados do ensaio

Resultado (último `rodar_tudo.sh`, código 0): `validate_v111` 20/20 OK; `conferencias_v111` 17 OK, 3 PENDENTE, 0 FALHA; `fidelidade_mutacao_v111` 22/22 casos.

| Conferência | Resultado no ensaio |
|---|---|
| C-1 | SHA da base (pacote e -E no git), do inventário e do T109 OK. SHA das tabelas PENDENTE (não fixado; só os gatilhos A fixam) |
| C-2 | 872 ids (GCE 293, GCB 575, GBQ 4), cada um em uma linha; nenhum dos 143 FP em linha |
| C-3, C-7 | 772 edições aplicadas (SUBSTITUIR 665, DELETAR 107) e 1 MANTER; antes único, intervalos, FP e proibições OK; limpeza refeita igual ao `out/pacote.json` byte a byte |
| C-4 | `pacote.json` idêntico à base fora do `interno`, `nome`, `geradoEm`, dos 251 campos editados e do `itemEdital` do L2-R16 |
| C-5 | `interno` ao contrário devolve a v1.10 byte a byte (208 objetos, 772 registros) |
| C-6 | `pacote.json` e -E: 0 PROCESSO, 1 VERIFICAR (o MANTER GBQ-0004), FP-R1 28 e FP-CONTEUDO 115 (os mesmos FP por campo, classe e casamento). Edição .md: ver 3.3 |
| C-8 | PENDENTE: 19 casamentos residuais das listas de deleção herdadas (ver 3.1) |
| C-9, C-10 | -E sem `interno`, `nucleo` booleano e último campo, fusão, `url` vazia; `nucleo` difere só no L2-R121 (entra/sai por troca de folha); P2-2.8 com 19 itens (18 diretos, 4 VOLÁTEIS), P2-3.1 com 7, todos `nucleo` |
| C-11 | 35 arquivos; mudam 20 (18 pelos campos e pelo L2-R16, mais NUCLEO.md e README.md); a troca de volta devolve a v1.10 byte a byte |
| C-12 | 773 linhas = 772 edições + L2-R16; conjunto (edicao, antes, depois) igual ao do `interno` |
| C-13 | simulados e composição iguais; L4-11 e BQ-0010 separados; nenhum VOLÁTIL em final; nenhum "QA PENDENTE" |
| C-14 | PENDENTE (só na geração final; o contrato v1.2.8 ainda não foi gravado) |
| C-15 | `validar_erros_teste.py` 12 conferências, 0 falhas |
| C-16 | nenhum literal de versão fora do `config_v111.py` |
| C-17 | informativa: no `plataforma_v1_7.html` (o mais novo do repositório) `validar(j)` só exige `itens[]` e `simulados[]` e `id`, `enunciado` e `gabarito` por item; não enumera chaves e "interno" não ocorre no código. Chave desconhecida é aceita. A plataforma publicada é do Fundador (D-V15-PLATAFORMA) |
| M | 22/22: controle; 1 caractere do `antes`; id em duas linhas; id repetido na linha; sobreposição; código de fonte no `depois`; FP em linha; `antes` que engole FP; BOM; `\r`; SHA diferente; id fora do universo; coluna ausente; cobertura incompleta; prefixo errado; `interno` adulterado; T109 sem a linha; L2-R16 fora de P2-2.8; L2-R16 em simulado; literal de versão; geração final sem E1–E5; .md sem a contagem esperada |

Números do ensaio (não valem para a geração final): `pacote.json` 560 itens, 1 114 632 bytes, SHA-256 34c131e2…; `pacote_estudante.json` 880 331 bytes, 4f423e70…; `registro_adendo3.md` 5da45403…; 195 itens AUTORAL com justificativa editada.

### 3.1 Decisões que o ensaio deixa para a GBQ (o gerador as implementou do modo mais estreito e as marcou)
1. Varredura R do -E. O "carimbo" de `marcas_processo.R` tratava `verificado em dd/mm/aaaa`, `reverificado em …` e `(leitura de dd/mm/aaaa)` como PROCESSO e a edição os apagava. Na M2 esses literais são texto de fonte (as tabelas da GCB os mantêm e o ponto 8 da seção 1.4 manda preservá-los), então o -E passou a contá-los (146 `verificado em`/`leitura de` mantidos) em vez de reprová-los; o resto de "carimbo" (`conferido pela…`) continua. Precisa de D1.
2. Residual das listas herdadas (C-8): 19 casamentos no `pacote.json` limpo que a T-108 não inventariou e a edição ainda apaga: 4 `Verificado em 8/10/2026` (A5-14 a A5-17), 4 `aberta(s) hoje` (L6A.curso, L6B.curso ×2 e 6B-06), 4 ids internos R-xx/E-xx (L4.curso, D4.padrao ×2, D5.padrao), 4 carimbos datados ligados a F-ref (L4.curso, L6A.curso), 1 "neste chat" (L4.curso), 1 referência F em prosa (L6A.curso), 1 instrução de montagem do L2-R18. Ou entram linhas nas tabelas, ou a lista fechada de exceções é declarada na reconciliação (`config_v111.EXCECOES_RESIDUAL`). Em FINAL, residual > 0 sem exceção = falha.
3. Listas X/Y da varredura R: Y1 (L4-11, "O F4 afirma que") tem contagem 0 porque o texto foi editado; CAIXA 6/8 e REALINHA 0/2 e as contagens de deleção do reforço (T-94 e T-104) deixaram de ser asserções e viram verificação informativa. O ensaio propõe X15 e X16 (`Primeira-Secretaria da Câmara`, no curso do L2, "Secretaria" como órgão da Mesa; `marcas_x_v111.py`); a GBQ confirma ou recusa.
4. C-6b: com `antes` editado, o índice k do hash de uma ocorrência FP muda (1 id: o F4 do L6A.curso). O gerador compara os FP por (campo, classe, casamento) e informa a diferença de ids; a exigência literal "os mesmos ids" não vale.
5. C-6d (.md): o inventário sobre os 34 arquivos .md (README fora) acha 98 PROCESSO (320 na v1.10), nenhum novo, todos de cabeçalho, metadado (versão), legenda de mecanismo TC/IC/GI/AT e texto de enunciado, fora dos campos do inventário JSON; os ids exatos de item são desconsiderados. "0 PROCESSO" não vale para os .md como o inventário os lê; adotei "nenhum novo, 0 nos campos do escopo". A GBQ confirma.
6. A edição .md não renderiza os `avisos` dos simulados (nenhum arquivo traz o texto): mudança em aviso não altera .md. O mapeamento do passo 4 usa os blobs do git (`git show`), porque `git archive`/`refs.pasta` converte para CRLF neste Windows (core.autocrlf) e quebraria a contagem.
7. Troca do L2-R16: `E_L2R16 = True` no ensaio com `ATO_L2R16 = None`; em FINAL a ausência do id da decisão em DECISOES.md é falha (não verifiquei a existência da linha, só o preenchimento).

### 3.2 O que não foi possível fazer no ensaio
- Nenhuma das 3 tabelas está aceita (E1 a E3) nem fixada em SHA-256; a da GBQ (`saida/pacote/T108_substituicoes_GBQ.csv`) não foi gravada em `saida/pacote/` (a tarefa proibia); as 4 linhas estão em `ensaio/T108_substituicoes_GBQ_ensaio.csv`.
- Contrato v1.2.8 (seção 2 da D1) não gravado; C-14 só roda em FINAL.

## 4. O que falta para a fase FINAL

1. E1 a E3: tabelas aceitas e completas, no nome final (`saida/gce/T108_substituicoes_GCE.csv`, `saida/gcb/T108_substituicoes_GCB.csv` junção das partes A, B e C, `saida/pacote/T108_substituicoes_GBQ.csv` gravada pela gbq-csc a partir da seção 1.9), sem as 103 linhas DELETAR com `depois`, sem ids `NAO_INVENTARIADA`, com os 4 casos de intervalo e o "inciso" da GCE-0211 resolvidos; SHA-256 de cada uma em `config_v111.TABELAS_FINAL`, e `ACEITE` e `PARECER_QA` por Gerência.
2. E4: aceite do gatilho D da GCE (T-109): `E_L2R16 = True` e `ATO_L2R16` = id em DECISOES.md (ou `E_L2R16 = False`, e o L2-R16 fica em P2-2.8; as asserções de C-10 e do passo 4 já tratam os dois casos).
3. E5: `VERSAO` decidida no gatilho D da numeração (`'1.11'` na opção (a), `'1.10.1'` na (b)). Nenhum script muda.
4. D1 da GBQ sobre os pontos 3.1 (1 a 5): varredura R do -E, residual (C-8), listas X/Y (X15 e X16), C-6b e C-6d.
5. Gravar o contrato v1.2.8 (texto da seção 2 da D1) em `regras/pacote_contrato.md` e em `saida/pacote/contrato_v1_2_8_<data>.md`, para o C-14.
6. `FINAL = True` em `config_v111.py` (o runner deixa de rodar o passo 0 e o `build_v111` recusa se `confere_final()` listar pendência) e nova execução completa; promoção byte a byte só depois do gatilho A da GBQ.
7. Fidelidade independente pela gbq-cqe (reconstrução por script próprio, C-1 a C-16, bloco M, amostra de 30 registros do `interno`), reconciliação, cobertura pela secretaria (T-95) e skill do painel; nada vai à plataforma sem o sim do Fundador.

Arquivos: `saida/pacote/gerador_v1_11/` (MANIFESTO.md, out/, ensaio/) e esta nota.
