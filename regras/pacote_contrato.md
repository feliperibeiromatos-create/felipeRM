# pacote.json — contrato de dados entre a fábrica e a plataforma (v1.1.1, 2026-10-13)

Arquivo único, UTF-8, gerado pela fábrica em `saida/pacote/pacote.json`. A plataforma lê e valida; nada além destes campos é necessário. A v1.1 (T-26, errata de forma de 2026-10-10; v1 de 9/10/2026) não muda nenhum campo obrigatório: acrescenta o campo opcional `volatil` e fixa regras de mapeamento e de fonte. A v1.1.1 (T-38 e T-43, 2026-10-13) corrige a forma da regra 2 e do exemplo JSON e acrescenta o campo opcional `nota`; também não muda nenhum campo obrigatório. A seção "Regras da v1.2" é proposta e só vigora com a T-48. O campo `versao` do JSON continua 1 (a v1.1 e a v1.1.1 são retrocompatíveis).

```json
{
  "versao": 1,
  "geradoEm": "2026-10-09",
  "nome": "Câmara 2026 — pacote F4",
  "edital": [ { "id": "P1-5.1", "prova": "P1", "texto": "Engenharia de prompts" } ],
  "itens": [ {
    "id": "BQ-0001", "rotulo": "CEBRASPE_ANALOGA", "certame": "TRF6 2024", "cargo": "Analista — Análise de Dados", "ano": 2025,
    "numero": 63, "comando": "A respeito de técnicas de visualização de dados, julgue o item subsequente.", "textoBase": "nenhum",
    "enunciado": "Na visualização de ...", "gabarito": "C", "justificativa": "", "itemEdital": "P1-8.1", "aderencia": "parcial",
    "url": "https://cdn.cebraspe.org.br/..."
  } ],
  "simulados": [ { "id": "SIM-0", "nome": "Simulado 0 — diagnóstico", "tipo": "diagnóstico", "itens": ["BQ-0001", "BQ-0002"] } ],
  "lotes": [ { "id": "L5", "nome": "Lote 5 — Dados e visualização", "prova": "P1", "itensEdital": ["P1-7.1", "P1-8.1"],
    "resumo": "markdown", "curso": "markdown", "pares": [ { "a": "histograma", "b": "gráfico de barras", "como": "..." } ],
    "pegadinhas": [ { "itemEdital": "P1-8.2", "texto": "..." } ] } ],
  "discursivas": [ { "id": "D1", "tipo": "questao|peca", "comando": "...", "aspectos": [ { "n": 1, "texto": "...", "valor": 3.6 } ],
    "padrao": "markdown", "quesitos": [ { "id": "2.1", "nome": "...", "conceitos": ["Conceito 0 — ...", "Conceito 1 — ..."] } ] } ]
}
```

Regras: `gabarito` só C ou E (anulados não entram); `itemEdital` segue a numeração do edital com prefixo P1/P2; `aderencia` é "direta" ou "parcial"; `rotulo` AUTORAL só para itens aprovados no arquivo canônico do lote e no registro GBQ vigente; `justificativa` obrigatória para AUTORAL, vazia para itens de banco; `lotes` só para lotes reconciliados (os da tabela de fonte abaixo); `discursivas` só com padrão de resposta no formato Cebraspe.

Regras da v1.1 (T-26):

1. **`volatil` (opcional).** Booleano, presente somente quando verdadeiro (nunca `false`; ausente = não volátil). Marca item VOLÁTIL e item REVERIFICAR normativo (regra R1-N do registro GBQ, mesmo tratamento do VOLÁTIL). Sentido para a plataforma: inapto a simulado final até a reverificação de 4–8/1/2027; pode entrar em estudo e em simulado diagnóstico. Campo obrigatório nenhum depende dele; a plataforma pode ignorá-lo, mas não deve usar o item em simulado final. Exemplo (BQ-0064, ANM 2024, item 97): `{ "id": "BQ-0064", ..., "itemEdital": "P1-5.3", "aderencia": "direta", "url": "https://cdn.cebraspe.org.br/...", "volatil": true }`.
2. **Mapeamento de `aderencia` (D-ADERENCIA).** O campo `observacoes` do banco contendo "parcial", "aderência temática ampla" ou "aderência apenas por tema" (sem distinção de maiúsculas e minúsculas) → `"parcial"`; senão `"direta"`. Todo item AUTORAL é `"direta"`. Item parcial só entra em simulado diagnóstico.
3. **`comando` e `textoBase` dos itens de banco.** Usar as colunas próprias do banco (`texto_comando`, `texto_base`) quando existirem (T-29). Até lá: `comando` = texto literal do bloco "Comando" do simulado que contém o item; `textoBase` = o texto da nota "texto-base do comando" das `observacoes` (separado do comando), ou "nenhum" quando não houver. Só vale para item que esteja em simulado; item de banco fora de simulado espera a T-29. Nada de texto novo: é mapeamento de texto literal.
4. **Fonte de cada lote.** O arquivo canônico de cada lote é o da tabela abaixo (fonte única; conferida contra `estado/ESTADO_CANONICO.md`, `DECISOES.md` e o registro GBQ vigente, hoje `saida/gbq/claude_GBQ_Registro_AUTORAL_v2.md`, e v3 após a T-30). Os arquivos `saida/lote*/RECONCILIADO.md` não existem e não são fonte. Se a tabela divergir do registro ou do estado canônico, prevalecem estes e a tabela é corrigida por errata do contrato.
5. **`simulados`.** Só entra simulado pronto: ajustes mecânicos reconciliados pela GBQ (mapa do simulado = banco) e condições da decisão de aceite cumpridas (hoje, para o SIM-0: T-25 concluída e reconciliada, e T-13 concluída sem gatilho D). Se faltar qualquer condição, `simulados` sai como `[]` e o relatório do pacote registra o motivo. Cada simulado é o mais recente do seu número, com `tipo` "diagnóstico" ou "final" conforme o cabeçalho. Liberar o simulado à candidata continua reservado ao Fundador.

| Lote | Arquivo canônico |
|---|---|
| L1 | `saida/gce/GCE_Lote1_v2_CPP.md` (com erratas e `saida/gce/GCE_Lote1_consolidacao_GCE.md`) |
| L1C | `saida/gce/GCE_Lote1C_v2_CPP.md` |
| L2 | `saida/gce/GCE_Lote2_v2_CPP.md` (padrões: `saida/gce/GCE_Lote2_padroes_GCE.md`) |
| L3 | `saida/gce/GCE_Lote3_v2_CPP.md` (padrões: `saida/gce/GCE_Lote3_padroes_GCE.md`) |
| L4 | `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` |
| L4C | `saida/gcb/GCB_Lote4C_v1_GCB-CPP.md` |
| L5 | `saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md` |
| L5C | `saida/gcb/GCB_Lote5C_v1_GCB-CPP.md` |
| L6A | `saida/gcb/GCB_Lote6a_v2_producao_auto.md` |
| L6B | `saida/gcb/GCB_Lote6b_v2_producao_auto.md` (com errata A-6b-1) |
| Banco | `banco/banco.csv` |
| Simulados | `saida/simulados/` (o mais recente de cada número, com o gabarito) |
| Edital | `edital/TI_itens_1_4_P1.md`, `edital/TI_itens_5_8_P1.md`, `edital/modulo_RF_IA_P2.md` |

Regras da v1.1.1 (T-38, T-43):

1. **Errata de forma da regra 2 (T-38).** A regra 2 da v1.1 passa a dizer que a busca de "parcial", "aderência temática ampla" e "aderência apenas por tema" em `observacoes` é feita sem distinção de maiúsculas e minúsculas. Conferência: o resultado é 60/60 igual ao mapa do Simulado 0 v0.2 e ao pacote v1; a leitura literal (só minúsculas) classificaria como "direta" 4 itens PARCIAIS (BQ-0001, BQ-0015, BQ-0036 e BQ-0055), cujo `observacoes` traz só "PARCIAL". A leitura sem distinção de caixa já valia para a T-27 (D1 da GBQ, reconciliação lote1, seção 5).
2. **Errata de forma do exemplo JSON (T-38).** No exemplo, BQ-0001 deixa de levar `"volatil": true` (o item não é VOLÁTIL) e passa a levar `"aderencia": "parcial"`, como no banco. A sintaxe de `volatil` fica ilustrada na regra 1 da v1.1, com BQ-0064.
3. **`nota` (opcional; T-43).** String com o texto de vigência ou de denominação do item, presente somente quando houver (nunca vazia, nunca `null`; ausente = sem nota). Campo obrigatório nenhum depende dele, e a plataforma pode ignorá-lo, mas, se o exibir, deve mostrá-lo junto do item sem alterar enunciado, comando ou gabarito. A nota não altera gabarito, aderência nem `volatil`.
4. **Origem da `nota`.** Texto literal da nota de vigência ou de denominação registrada em `observacoes` do banco pela D1 da GBQ, a partir do rótulo "nota de vigência:" e inclusive ele, sem edição e sem texto novo. Não entra em `nota` a nota de outra natureza (processo, QA, paráfrase, doutrina). Hoje há dois itens, e a exportação do campo no pacote fica para a T-48 (esta errata não gera `pacote.json`):
   - BQ-0040 (Res. CNJ 332/2020 revogada pela Res. CNJ 615/2025; regra no art. 8º, § 3º): `nota de vigência: a Res. CNJ 332/2020, citada no comando, foi revogada pela Res. CNJ 615/2025 (art. 46); a regra cobrada está hoje no art. 8º, § 3º, da Res. CNJ 615/2025, que manda descontinuar a solução e cancelar o registro do projeto no Sinapses; Res. CNJ 335/2020, 396/2021 e 468/2022 vigentes, sem efeito no item`
   - BQ-0003 (denominação vigente: Agência Nacional de Proteção de Dados, Lei 15.352/2026): `nota de vigência: o enunciado usa a denominação anterior Autoridade Nacional de Proteção de Dados; denominação vigente: Agência Nacional de Proteção de Dados (ANPD), art. 55-A da LGPD, redação da Lei 15.352/2026 (D-LEI-15352); texto do item mantido literal`

Regras da v1.2 (D-T12-V12; proposta, a vigorar com a T-48):

Decisões do Fundador de 13/10/2026 (D-T12-V12 e D-PACOTE-V11) para o pacote v1.2 gerado pela T-12. Esta seção é proposta de contrato, sem efeito antes da T-48; até lá valem a v1.1 e a v1.1.1. Nenhuma regra desta seção torna obrigatório um campo que a v1.1.1 não exige, exceto onde está dito que um campo passa a ser sempre emitido.

a. **`comandoOriginal` (opcional).** String com o texto literal do comando do caderno, presente somente quando o `comando` exportado for normalizado (D1-c da GBQ, ratificada pelo Fundador em D-PACOTE-V11 (c)); nunca vazia; ausente quando o `comando` exportado já é o literal do caderno.
b. **`textoBase` vazio.** Quando o item não tem texto-base, `textoBase` é `""` (string vazia), não `"nenhum"` (F2). Quando há texto-base, vale o texto literal, como na regra 3 da v1.1.
c. **`aderencia` explícita.** Todo item leva `"direta"` ou `"parcial"` tirada da coluna de aderência do banco (D1-b: aderência explícita em todas as linhas do banco), sem inferência a partir de `observacoes`; item AUTORAL continua `"direta"`. Com a coluna disponível, o mapeamento por texto da regra 2 da v1.1 (e da v1.1.1) deixa de valer.
d. **Pegadinhas.** Em `lotes[].pegadinhas`, uma pegadinha por entrada, cada entrada com `rotulo` (F3): `{ "itemEdital": "...", "rotulo": "...", "texto": "..." }`. Entrada com várias pegadinhas no mesmo texto é desdobrada.
e. **Simulados com `n` e `versao`.** Cada entrada de `simulados` leva `n` (inteiro: número de itens, igual ao tamanho da lista `itens` do simulado) e `versao` (string: versão do simulado, por exemplo "v0.2").
f. **Listas JSON.** Os campos de lote `itensEdital`, `pares` e `pegadinhas` são sempre listas JSON (vazias quando não houver conteúdo), nunca strings.
g. **`versao` do JSON.** Passa a valer 1 com `nome` indicando v1.2 (por exemplo "Câmara 2026 — pacote F4 v1.2"), por retrocompatibilidade: todo campo obrigatório da v1.1.1 continua obrigatório, com o mesmo nome e tipo. DÚVIDA para a GBQ: as regras (b) (valor `""` no lugar de `"nenhum"`) e (d) (pegadinhas desdobradas, com `rotulo`) mudam o conteúdo de campos existentes, ainda que não os nomes nem os tipos; se a GBQ entender que isso exige `versao` 2, a decisão é dela e do Fundador, e este contrato não a antecipa.

---

# PROMPT DE PARTIDA — EXPORTAR (colar como primeira mensagem numa sessão nova do Claude Code)

Execute a tarefa EXPORTAR conforme CLAUDE.md, sem pedir confirmação. Delegue ao agente gbq-csc a geração de saida/pacote/pacote.json no contrato descrito em regras/pacote_contrato.md (este arquivo), com: (1) "edital": todos os itens dos dois módulos em edital/, com id P1-x.y ou P2-x.y; (2) "itens": todas as linhas de banco/banco.csv com gabarito C ou E, campos mapeados um a um (comando e textoBase pela regra 3 da v1.1, item_edital_camara → itemEdital, aderencia pela regra 2 da v1.1, volatil pela regra 1 da v1.1), mais os itens AUTORAL aprovados nos arquivos canônicos da tabela de fonte por lote deste contrato e no registro GBQ vigente, com justificativa; (3) "simulados": conforme a regra 5 da v1.1 (só simulado pronto; o mais recente de cada número; tipo "diagnóstico" ou "final" conforme o cabeçalho; senão [] com o motivo no relatório); (4) "lotes": um por lote da tabela de fonte por lote deste contrato, com resumo, curso, pares e pegadinhas extraídos das seções (b), (a), (c) e das "pegadinhas prováveis"; (5) "discursivas": as hipóteses com padrão de resposta dos arquivos canônicos de P2 da tabela de fonte. Valide o JSON (parse sem erro; nenhum item sem id, enunciado e gabarito; nenhum id duplicado) e grave também saida/pacote/pacote_relatorio.md com as contagens. Delegue à secretaria a atualização do estado, imprima o resumo de 10 linhas e "GATILHO A — aguardando decisão humana". Pare. Nenhuma outra tarefa nesta sessão.
