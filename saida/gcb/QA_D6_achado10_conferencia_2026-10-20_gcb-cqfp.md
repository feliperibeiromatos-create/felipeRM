# QA_D6_achado10_conferencia_2026-10-20_gcb-cqfp.md — T-118 (D1, passo 4.2; achado 10) — 2026-10-20 — gerado por gcb-cqfp

Ciclo s15c1. Conferência independente da errata de forma do achado 10 aplicada pela gcb-cpp (passo 4.1 da D1 saida/pacote/T118_D1_v1_13_2026-10-20.md, seção 2). A gcb-cqfp não produziu nem reconciliou o objeto. Script próprio (`python3 -I`, fora do repositório, só leitura), comparação contra o blob em HEAD (`git show HEAD:<caminho>`). Nada foi alterado nos arquivos de produção; sem commit.

**VEREDITO: CONFERIDO** (D1, seção 4.2, usa "CONFERIDO ou DEVOLVIDO"; aqui não há devolução).

## 1. Objetos

| Arquivo | HEAD (bytes; SHA-256) | Disco (bytes; SHA-256) |
|---|---|---|
| saida/gcb/DA_plataforma/D6_plataforma.json | 184.195; 8b8e5a42e3a8f5e9f500fa0fec8450f06e1932409ca6cae303a8b1ee0fa9754a | 184.191; f8691dd5a3fd968922bf8bac8e26b4dd4f1475183afc9d6a0e84418d08b17122 |
| saida/gcb/DA_plataforma/D6_registro_formato.md | 4448eec4b726dce440ba937e74fd34e4752f5c33f57288745f4175548ae8f56a | 7998cc7be19676125ba13bdcc7f52537012488371ec8e1f9e01aa916b09890ca |

## 2. Critérios

| # | Critério (D1, 4.1 e 4.2) | Esperado | Obtido | Resultado |
|---|---|---|---|---|
| 1 | Diff JSON contra HEAD (8b8e5a42) | só `/lote/pares[0]/como` | `['/lote/pares/0/como']` (diff recursivo de objeto; nenhum outro caminho, nenhuma chave nova ou removida) | OK |
| 2 | Natureza da mudança em `como` | só retirada de dois pares de `**` | `**` 2 → 0; `antigo.replace('**','') == novo`; 4 caracteres a menos; `git diff` = 1 linha trocada | OK |
| 3 | Enunciado, gabarito, itens, resumo, curso, pegadinhas, tópicos | intocados | contidos no critério 1 (diff só no campo); `lote.resumo` idêntico ao HEAD e mantém `**temporária**` | OK |
| 4 | Bytes e SHA-256 | 184.191; f8691dd5…7122 | 184.191; f8691dd5a3fd968922bf8bac8e26b4dd4f1475183afc9d6a0e84418d08b17122 | OK |
| 5 | Edição por texto, sem reserializar | old_str ocorre 1 vez; trecho curto 2 vezes | old_str 1 vez no HEAD; "restrição **temporária** por" 2 vezes no HEAD e 1 no disco (a de `resumo`); substituir o old_str pelo new_str no blob HEAD reproduz o disco byte a byte | OK |
| 6 | Serialização igual à do HEAD | `json.dumps(d, ensure_ascii=False, indent=1) + "\n"` | HEAD e disco iguais à reserialização própria; 0 CR | OK |
| 7 | validar_da.py no D6 | 0 FALHA | `python3 -I saida/gcb/DA_plataforma/scripts/validar_da.py saida/gcb/DA_plataforma/D6_plataforma.json saida/gcb/D6_v2_1.md saida/gcb/D6_anexo_N_mapa_normativo.md` (comando da seção do registro) → "RESULTADO: 0 FALHA, 0 AVISO", exit 0; itens 50 (C 25 / E 25), pares 43, pegadinhas 63; validador, canônico (a9831058…4090) e Anexo N (57e8c64d…3e80e) inalterados | OK |
| 8 | `**` em `pares` e `pegadinhas` dos seis D<n>_plataforma.json | 0 | D1 22/26, D2 46/114, D3 31/67, D4 24/62, D5 31/73, D6 43/63 (pares/pegadinhas): 0 `**` em todos | OK |
| 9 | D1 a D5 e edital_DA.json | SHA-256 inalterado | D1–D5_plataforma.json, edital_DA.json, D1–D6_topicos_fonte.json, D1–D5_registro_formato.md e validar_da.py iguais ao HEAD | OK |
| 10 | Registro: só acréscimo ao fim | seção nova no fim | numstat 8/0; o blob HEAD é prefixo byte a byte do arquivo em disco | OK |
| 11 | Registro corresponde ao diff | itens da D1, seção 2 | título "## Errata de forma — T-118 (achado 10), 20/10/2026"; origem (QA final 8.7, achado 10; contrato v1.2.10, ponto 4); item 1 `[par 0 (L-P1), campo como] deleção de marca (negrito)`; o "antes" é substring do `como` do HEAD e o "depois" do `como` do disco, diferindo só pelos `**`; motivo; frase "Só forma: … (campo markdown)" literal; "Total: 1 mudança no D6 (`pares`)"; bytes, SHA-256 e caminho do diff citados iguais aos obtidos; par 0 = "Informação sigilosa" × "informação pessoal" (L-P1); a seção 7.3 declara a origem dos pares "sem marcas", como a entrada afirma | OK |

## 3. Observações (não alteram o veredito)

- O1 (INFO): o "antes/depois" do registro transcreve só a primeira frase do campo `como` (o trecho que contém a mudança), não o campo inteiro. Atende à D1 ("o antes e o depois do trecho").
- O2 (INFO): a linha 1 do D6_registro_formato.md continua com o cabeçalho original (T-72); a seção nova é datada e identificada no título, como nas erratas anteriores do mesmo arquivo.
- O3 (INFO, fora do objeto): a árvore de trabalho tem também mudanças em DECISOES.md, TAREFAS.md e PARA_PRESIDENCIA.md (renomeado para historico/) e a D1 não rastreada. Não são do passo 4.1 e não foram conferidas aqui.

## 4. Consequência

Critérios 4.1 e 4.2 da D1 cumpridos. A gbq-csc pode iniciar o passo 4.3 (remontagem com `montar_v1_13.py` sem mudança). Esta conferência não libera nada à plataforma nem à candidata.
