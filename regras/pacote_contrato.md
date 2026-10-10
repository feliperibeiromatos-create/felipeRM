# pacote.json — contrato de dados entre a fábrica e a plataforma (v1.1, 2026-10-10)

Arquivo único, UTF-8, gerado pela fábrica em `saida/pacote/pacote.json`. A plataforma lê e valida; nada além destes campos é necessário. A v1.1 (T-26, errata de forma de 2026-10-10; v1 de 9/10/2026) não muda nenhum campo obrigatório: acrescenta o campo opcional `volatil` e fixa regras de mapeamento e de fonte. O campo `versao` do JSON continua 1 (a v1.1 é retrocompatível).

```json
{
  "versao": 1,
  "geradoEm": "2026-10-09",
  "nome": "Câmara 2026 — pacote F4",
  "edital": [ { "id": "P1-5.1", "prova": "P1", "texto": "Engenharia de prompts" } ],
  "itens": [ {
    "id": "BQ-0001", "rotulo": "CEBRASPE_ANALOGA", "certame": "TRF6 2024", "cargo": "Analista — Análise de Dados", "ano": 2025,
    "numero": 63, "comando": "A respeito de técnicas de visualização de dados, julgue o item subsequente.", "textoBase": "nenhum",
    "enunciado": "Na visualização de ...", "gabarito": "C", "justificativa": "", "itemEdital": "P1-8.1", "aderencia": "direta",
    "url": "https://cdn.cebraspe.org.br/...", "volatil": true
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

1. **`volatil` (opcional).** Booleano, presente somente quando verdadeiro (nunca `false`; ausente = não volátil). Marca item VOLÁTIL e item REVERIFICAR normativo (regra R1-N do registro GBQ, mesmo tratamento do VOLÁTIL). Sentido para a plataforma: inapto a simulado final até a reverificação de 4–8/1/2027; pode entrar em estudo e em simulado diagnóstico. Campo obrigatório nenhum depende dele; a plataforma pode ignorá-lo, mas não deve usar o item em simulado final.
2. **Mapeamento de `aderencia` (D-ADERENCIA).** O campo `observacoes` do banco contendo "parcial", "aderência temática ampla" ou "aderência apenas por tema" → `"parcial"`; senão `"direta"`. Todo item AUTORAL é `"direta"`. Item parcial só entra em simulado diagnóstico.
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

---

# PROMPT DE PARTIDA — EXPORTAR (colar como primeira mensagem numa sessão nova do Claude Code)

Execute a tarefa EXPORTAR conforme CLAUDE.md, sem pedir confirmação. Delegue ao agente gbq-csc a geração de saida/pacote/pacote.json no contrato descrito em regras/pacote_contrato.md (este arquivo), com: (1) "edital": todos os itens dos dois módulos em edital/, com id P1-x.y ou P2-x.y; (2) "itens": todas as linhas de banco/banco.csv com gabarito C ou E, campos mapeados um a um (comando e textoBase pela regra 3 da v1.1, item_edital_camara → itemEdital, aderencia pela regra 2 da v1.1, volatil pela regra 1 da v1.1), mais os itens AUTORAL aprovados nos arquivos canônicos da tabela de fonte por lote deste contrato e no registro GBQ vigente, com justificativa; (3) "simulados": conforme a regra 5 da v1.1 (só simulado pronto; o mais recente de cada número; tipo "diagnóstico" ou "final" conforme o cabeçalho; senão [] com o motivo no relatório); (4) "lotes": um por lote da tabela de fonte por lote deste contrato, com resumo, curso, pares e pegadinhas extraídos das seções (b), (a), (c) e das "pegadinhas prováveis"; (5) "discursivas": as hipóteses com padrão de resposta dos arquivos canônicos de P2 da tabela de fonte. Valide o JSON (parse sem erro; nenhum item sem id, enunciado e gabarito; nenhum id duplicado) e grave também saida/pacote/pacote_relatorio.md com as contagens. Delegue à secretaria a atualização do estado, imprima o resumo de 10 linhas e "GATILHO A — aguardando decisão humana". Pare. Nenhuma outra tarefa nesta sessão.
