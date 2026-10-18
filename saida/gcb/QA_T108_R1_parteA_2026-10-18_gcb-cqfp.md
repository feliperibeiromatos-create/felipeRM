# QA_T108_R1_parteA_2026-10-18_gcb-cqfp.md — T-108 (ORDEM_V15_C, limpeza), QA R1 da GCB, Parte A (lotes 4 e 4-C) — 2026-10-18 — gerado por gcb-cqfp

Objeto: `saida/gcb/T108_substituicoes_GCB_parteA.csv` (178 edições, GCB-A0001 a GCB-A0178), com `saida/gcb/T108_producao_notas_GCB_parteA.md` e `saida/gcb/T108_fontes_GCB.md` (tabelas dos lotes 4 e 4-C). Roteiro: `saida/gcb/T108_D1_GCB_2026-10-18.md`, seção 5 (R1), e seção 4 do método da GBQ (`saida/pacote/T108_metodo_GBQ_2026-10-18.md`). Texto-base: `saida/pacote/pacote.json` v1.10, SHA-256 LF d43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed (conferido). Somente leitura: nenhuma linha do CSV, fonte, pacote, TAREFAS, DECISOES ou PARA_PRESIDENCIA foi tocada; sem commit.

## 1. Veredito da Parte A

**APROVADO COM RESSALVAS.** 178 linhas: 149 APROVADO, 29 CORRIGIR (correção exata na tabela da seção 6), 0 REPROVADO. Percentual de reprovação: 0,0% (0/178). Linhas com correção: 16,3% (29/178), das quais 27 só de formato (`acao`), 1 de mérito (A0078) e 1 de português (A0025). Nenhuma correção muda sentido de justificativa, base legal ou "verificado em".

A ressalva de formato é bloqueante para a consolidação: o validador da GBQ (`saida/pacote/gerador_v1_11/tabelas_v111.py`, regra C-1) recusa "DELETAR com depois não vazio", e 28 linhas da Parte A (as 27 de formato e a A0078) estão nessa condição. O texto resultante dessas 27 linhas está certo; só o rótulo da ação está errado.

R2: confere só as 29 linhas da seção 6, na versão `_v2` da Parte A.

## 2. Conferência mecânica (script próprio, python -I -X utf8, somente leitura, cópia em pasta temporária fora do repositório)

O `T108_conferir_tabela.py` da GBQ não existe; foi usado script próprio, que importa `saida/pacote/T108_inventario.py` (funções `campos` e `varre`) sem gravar no repositório.

| Checagem | Resultado |
|---|---|
| (a) cobertura: ocorrências PROCESSO + VERIFICAR dos lotes 4 e 4-C no `T108_ocorrencias.csv` (196: lote 4 = 158 PROCESSO + 5 VERIFICAR; 4-C = 30 PROCESSO + 3 VERIFICAR) cobertas por exatamente uma edição | 196/196; nenhum id extra; nenhum id repetido |
| (b) `antes` literal e único no campo; caminho da edição = caminho da ocorrência; casamento da ocorrência dentro do `antes`; categoria coerente; sem sobreposição de `antes` no mesmo campo | 178/178; 0 divergência |
| (c) FP-R1 e FP-CONTEUDO | FP-R1 nos lotes 4 e 4-C: 0 (o D-C05-4a878e59 é do 6a). FP-CONTEUDO: 33 antes e 33 depois da aplicação, mesmos ids; nenhum casamento FP dentro de `antes` |
| (d) aplicadas as 178 trocas numa cópia, nova varredura (`varre`) dos lotes 4 e 4-C | 0 PROCESSO, 0 VERIFICAR, 33 FP-CONTEUDO |
| (e) resíduo no `depois`: as 10 categorias do inventário (todas as regras de `REGRAS`), mais "[TS]", "Difere d", "VOLÁTI" | 0 casamento em 178 `depois` |
| (f) enunciado, comando, textoBase, gabarito, itemEdital, aderencia e volatil de todos os itens idênticos após a aplicação; campos tocados só curso (92), resumo (4), pegadinhas[].texto (4), pares[].como (2), justificativa (76) | idênticos; nenhum `antes` fora desses campos |
| Tipografia pós-aplicação (espaço duplo, espaço antes de pontuação, parênteses vazios, ponto duplo) | nenhum caso novo |
| Formato (D1, seção 2) | `fonte_origem` presente em todas as linhas de regra 2; nenhum SUBSTITUIR vazio; nenhum MANTER; **28 DELETAR com `depois` não vazio** (seção 6) |

Contagens conferidas, iguais às da nota de produção: lote 4 = 148 edições, 4-C = 30; SUBSTITUIR 140, DELETAR 38, MANTER 0; regra 2 = 112, 3 = 8, 4 = 30, 5 = 28; TEMPLATE 72, LIVRE 106. Ocorrências por lote e categoria: lote 4 — C05 111, C06 21, C07 16, C10 9, C08 4, C01 2; 4-C — C05 13, C06 10, C01 8, C03 2.

## 3. Tabela de fontes (amostra contra o arquivo do lote)

| Lote | Códigos conferidos | Arquivo e linha | Resultado |
|---|---|---|---|
| 4 | F1, F3, F4, N5, N8 | `GCB_Lote4_v3_canonica_GCB-CPP.md`, linhas 46 a 51 (F, cabeçalho "verificadas em 7/10/2026, acesso direto; F4 reverificado em 7/10/2026"), 56 (N) e 57 (data da Lei 8.112/1990, 08/10/2026) | nomes iguais aos do arquivo; N8 "CF, art. 37, caput" por extenso como "Constituição Federal, art. 37, caput" (compatível); datas iguais; nenhuma fonte nova |
| 4-C | F1, F2, F3 (todos os códigos do lote; o lote só tem três) | `GCB_Lote4C_v1_GCB-CPP.md`, linhas 7 e 36 ("as do curso do Lote 4", verificadas em 7/10/2026) | iguais; nenhuma fonte nova |

Nenhuma divergência na amostra; não foi preciso conferir a tabela inteira. Além da amostra: 100% dos nomes das linhas de regra 2 conferidos contra a tabela (122 referências de código): todos os nomes estão no `depois`, salvo A0050 e A0051 ("dessa página"), que remetem ao nome dado no mesmo item de lista pela A0049. Aceito. Forma TEMPLATE: as 72 linhas lidas (acima da amostra de 20%), todas na forma fixa do D1.

## 4. Mérito (todas as 106 linhas LIVRE e as 8 VERIFICAR)

- Regra 4 (TC, GI, AT, IC; 30 linhas): as quatro siglas trocadas pela legenda do próprio lote (`GCB_Lote4_v3_canonica_GCB-CPP.md`, linha 355; `GCB_Lote4C_v1_GCB-CPP.md`, linha 36): troca de conceito, generalização indevida, atribuição errada de técnica, inversão de causa e efeito. Nenhuma sigla trocada por mecanismo diferente. O parêntese de "tentação" e o resto da justificativa ficam, e o mecanismo continua explicado.
- VERIFICAR "sem armadilha (ancoragem)" (L4-07, L4-14, 4C-02, 4C-07, 4C-09): os cinco "Item de fixação …" descrevem o que o item avalia, conforme a justificativa que segue. Aprovados.
- VERIFICAR VOLÁTIL (A0085, A0086, A0096) e VOLÁTIL na justificativa do L4-05 (A0113): linguagem comum, sem MANTER; sentido mantido ("Sem marca VOLÁTIL" = o item não depende de dado que muda).
- Regra 3 (8 linhas "Difere do item…", todas no 4-C): cada frase sai inteira, com o espaço que a antecede, e só ela; o 4C-09 tem duas frases, cobertas por A0176 e A0177. Explicação do gabarito preservada nas oito.
- Regra 5 (C07, C08, C10): "pela CQFP" sai e ficam a data, "no Planalto" e a base legal (A0066 a A0076, A0092, A0100, A0102). Os nomes internos de arquivo e rótulo (A0038, A0129) viram "item análogo do Cebraspe" e "gabarito definitivo do TRF6", sem fato novo. A A0084 troca "Síntese da CQFP a partir do texto colado pelo Fundador" por "Síntese a partir do texto consultado" e mantém a data e "não é transcrição literal". Aceito.
- "Lote N" (A0024, A0039): trocado pelo tópico do edital certo (`edital/TI_itens_5_8_P1.md`: 5.1 Engenharia de prompts; 5.2 Aprendizado supervisionado, não supervisionado e por reforço). O trecho de A0039 fica no curso 5.2.5. A frase "o tópico 5.2 de TI e Dados usa a página … como fundamento" segue a regra literalmente; está aprovada.
- Normas (N1 a N10): a base legal fica inteira (lei, artigo, inciso). Onde a norma já está nomeada, só o código sai; onde o código era o único nome, entra o nome da tabela.
- Português: uma correção (A0025). Nas A0007 e A0016 a forma fixa repete o editor ("da Anthropic ("XML structuring", Anthropic, "Prompt engineering overview")"). A frase fica redundante mas correta, e está aprovada.
- Fato novo: nenhum.

## 5. Normativo

Nenhuma citação de lei foi criada. As citações já existentes ficaram com artigo, inciso e data de conferência, então não houve caso de PENDENTE por falta de qa-normativo. O QA não reabriu o texto vigente das normas; isso está fora do objeto da T-108.

## 6. Linhas com correção (para a R2)

| id_edicao | Tipo | Correção exata |
|---|---|---|
| GCB-A0060, A0061, A0063, A0064, A0065, A0066, A0067, A0068, A0069, A0070, A0071, A0072, A0073, A0074, A0075, A0076, A0077, A0079, A0080, A0081, A0082, A0083, A0087, A0092, A0100, A0102, A0174 (27) | formato | `acao` DELETAR → SUBSTITUIR; `antes`, `depois`, `regra` e `nota` sem mudança (a troca é parcial: o `depois` não é vazio). |
| GCB-A0078 | mérito | `antes` = " Não usada em item, por despacho da GCB." (com o espaço inicial; conferido literal e único em `lotes[L4].curso`); `depois` = "" (vazio); `acao` = DELETAR; `regra` = 5. Motivo: "Não usada em item" é instrução interna, da família de "sem item", que o próprio produtor deleta em A0069, A0084 e A0087. |
| GCB-A0025 | português | `depois` = `as técnicas descritas pela Anthropic ("Prompt engineering overview") e pela OpenAI ("Prompt engineering").` Motivo: no original faltava o artigo antes do nome da empresa ("de Anthropic"), e o curso usa "a Anthropic" e "a OpenAI". |

## 7. Achados fora da tabela (não contam na reprovação; para a GCB decidir, com aviso à GBQ sobre o inventário)

Depois da aplicação, quatro marcas de produção que o `T108_inventario.py` não casa continuam no texto da candidata nos lotes 4 e 4-C:
1. `lotes[L4].curso`, "Distinção de vocabulário (O11)": código de lição interna.
2. `lotes[L4].curso`, mapa normativo, "Não fundamenta item." (depois do art. 121 da Lei 8.112/1990): instrução interna, da mesma família da A0078.
3. `lotes[L4].curso`, "situação de tramitação não verificada neste chat": menção ao meio de produção.
4. `itens[4C-10].justificativa`, "TC (formato × restrição; não sutil)": nota de classificação [TS].

Pela regra 6 do método da GBQ, a meta é 0 PROCESSO. Sugestão: ocorrências novas (categorias C02/C10 ou C08) numa errata do inventário, ou linhas adicionais na Parte A _v2 se a GCB as admitir no universo. A decisão é da GCB.

## 8. Tabela linha a linha (178)

| id_edicao | lote | categoria | modo | ação | regra | veredito | motivo / correção exata |
|---|---|---|---|---|---|---|---|
| GCB-A0001 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0002 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0003 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0004 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0005 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0006 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0007 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0008 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0009 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0010 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0011 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0012 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0013 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0014 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0015 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0016 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0017 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0018 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0019 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0020 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0021 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0022 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0023 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0024 | 4 | C01 | LIVRE | SUBSTITUIR | 5 | APROVADO |  |
| GCB-A0025 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | CORRIGIR | Português: "as técnicas de Anthropic (…) e de OpenAI (…)" sem artigo, contra o uso do próprio curso ("a OpenAI", "da Anthropic"). Correção: `depois` = "as técnicas descritas pela Anthropic ("Prompt engineering overview") e pela OpenAI ("Prompt engineering")." |
| GCB-A0026 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0027 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0028 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0029 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0030 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0031 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0032 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0033 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0034 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0035 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0036 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0037 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0038 | 4 | C08 | LIVRE | SUBSTITUIR | 5 | APROVADO |  |
| GCB-A0039 | 4 | C01;C05 | LIVRE | SUBSTITUIR | 5 | APROVADO |  |
| GCB-A0040 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0041 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0042 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0043 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0044 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0045 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0046 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0047 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0048 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0049 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0050 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0051 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0052 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0053 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0054 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0055 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0056 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0057 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0058 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0059 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0060 | 4 | C05 | LIVRE | DELETAR | 2 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0061 | 4 | C05 | LIVRE | DELETAR | 2 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0062 | 4 | C07 | LIVRE | DELETAR | 5 | APROVADO |  |
| GCB-A0063 | 4 | C05 | LIVRE | DELETAR | 2 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0064 | 4 | C07 | LIVRE | DELETAR | 5 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0065 | 4 | C05 | LIVRE | DELETAR | 2 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0066 | 4 | C07 | LIVRE | DELETAR | 5 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0067 | 4 | C07 | LIVRE | DELETAR | 5 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0068 | 4 | C07 | LIVRE | DELETAR | 5 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0069 | 4 | C10 | LIVRE | DELETAR | 5 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0070 | 4 | C07 | LIVRE | DELETAR | 5 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0071 | 4 | C07 | LIVRE | DELETAR | 5 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0072 | 4 | C07 | LIVRE | DELETAR | 5 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0073 | 4 | C05 | LIVRE | DELETAR | 2 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0074 | 4 | C07 | LIVRE | DELETAR | 5 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0075 | 4 | C07 | LIVRE | DELETAR | 5 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0076 | 4 | C07 | LIVRE | DELETAR | 5 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0077 | 4 | C05 | LIVRE | DELETAR | 2 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0078 | 4 | C07 | LIVRE | DELETAR | 5 | CORRIGIR | Mérito: "Não usada em item." é instrução interna da mesma família de "sem item" (D1, seção 2; A0069, A0084, A0087 a deletam). Correção: `antes` = " Não usada em item, por despacho da GCB." (com o espaço inicial; literal e único no campo), `depois` = "" , `acao` = DELETAR, `regra` = 5. |
| GCB-A0079 | 4 | C05 | LIVRE | DELETAR | 2 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0080 | 4 | C05 | LIVRE | DELETAR | 2 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0081 | 4 | C05 | LIVRE | DELETAR | 2 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0082 | 4 | C05 | LIVRE | DELETAR | 2 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0083 | 4 | C05 | LIVRE | DELETAR | 2 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0084 | 4 | C07;C10 | LIVRE | SUBSTITUIR | 5 | APROVADO |  |
| GCB-A0085 | 4 | C10 | LIVRE | SUBSTITUIR | 5 | APROVADO |  |
| GCB-A0086 | 4 | C10 | LIVRE | SUBSTITUIR | 5 | APROVADO |  |
| GCB-A0087 | 4 | C10 | LIVRE | DELETAR | 5 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0088 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0089 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0090 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0091 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0092 | 4 | C07 | LIVRE | DELETAR | 5 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0093 | 4 | C10 | LIVRE | DELETAR | 5 | APROVADO |  |
| GCB-A0094 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0095 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0096 | 4 | C10 | LIVRE | SUBSTITUIR | 5 | APROVADO |  |
| GCB-A0097 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0098 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0099 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0100 | 4 | C07 | LIVRE | DELETAR | 5 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0101 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0102 | 4 | C07 | LIVRE | DELETAR | 5 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0103 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0104 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0105 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0106 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0107 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0108 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0109 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0110 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0111 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0112 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0113 | 4 | C10 | LIVRE | SUBSTITUIR | 5 | APROVADO |  |
| GCB-A0114 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0115 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0116 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0117 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0118 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0119 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0120 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0121 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0122 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0123 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0124 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0125 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0126 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0127 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0128 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0129 | 4 | C08 | LIVRE | SUBSTITUIR | 5 | APROVADO |  |
| GCB-A0130 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0131 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0132 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0133 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0134 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0135 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0136 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0137 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0138 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0139 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0140 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0141 | 4 | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0142 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0143 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0144 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0145 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0146 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0147 | 4 | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0148 | 4 | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0149 | 4-C | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0150 | 4-C | C01 | LIVRE | DELETAR | 3 | APROVADO |  |
| GCB-A0151 | 4-C | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0152 | 4-C | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0153 | 4-C | C01 | LIVRE | DELETAR | 3 | APROVADO |  |
| GCB-A0154 | 4-C | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0155 | 4-C | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0156 | 4-C | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0157 | 4-C | C01 | LIVRE | DELETAR | 3 | APROVADO |  |
| GCB-A0158 | 4-C | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0159 | 4-C | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0160 | 4-C | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0161 | 4-C | C01 | LIVRE | DELETAR | 3 | APROVADO |  |
| GCB-A0162 | 4-C | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0163 | 4-C | C03;C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0164 | 4-C | C01 | LIVRE | DELETAR | 3 | APROVADO |  |
| GCB-A0165 | 4-C | C05 | LIVRE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0166 | 4-C | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0167 | 4-C | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0168 | 4-C | C01 | LIVRE | DELETAR | 3 | APROVADO |  |
| GCB-A0169 | 4-C | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0170 | 4-C | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0171 | 4-C | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0172 | 4-C | C05 | TEMPLATE | SUBSTITUIR | 2 | APROVADO |  |
| GCB-A0173 | 4-C | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0174 | 4-C | C03 | LIVRE | DELETAR | 5 | CORRIGIR | Formato: `acao` DELETAR com `depois` não vazio (D1, seção 2; tabelas_v111.py, C-1). Correção: `acao` = SUBSTITUIR; `antes`, `depois` e `regra` inalterados. Mérito aprovado. |
| GCB-A0175 | 4-C | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
| GCB-A0176 | 4-C | C01 | LIVRE | DELETAR | 3 | APROVADO |  |
| GCB-A0177 | 4-C | C01 | LIVRE | DELETAR | 3 | APROVADO |  |
| GCB-A0178 | 4-C | C06 | LIVRE | SUBSTITUIR | 4 | APROVADO |  |
