# pacote.json — contrato de dados entre a fábrica e a plataforma (v1, 9/10/2026)

Arquivo único, UTF-8, gerado pela fábrica em `saida/pacote/pacote.json`. A plataforma lê e valida; nada além destes campos é necessário.

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

Regras: `gabarito` só C ou E (anulados não entram); `itemEdital` segue a numeração do edital com prefixo P1/P2; `aderencia` é "direta" ou "parcial"; `rotulo` AUTORAL só para itens aprovados em RECONCILIADO; `justificativa` obrigatória para AUTORAL, vazia para itens de banco; `lotes` só para lotes reconciliados; `discursivas` só com padrão de resposta no formato Cebraspe.

---

# PROMPT DE PARTIDA — EXPORTAR (colar como primeira mensagem numa sessão nova do Claude Code)

Execute a tarefa EXPORTAR conforme CLAUDE.md, sem pedir confirmação. Delegue ao agente gbq-csc a geração de saida/pacote/pacote.json no contrato descrito em regras/pacote_contrato.md (este arquivo), com: (1) "edital": todos os itens dos dois módulos em edital/, com id P1-x.y ou P2-x.y; (2) "itens": todas as linhas de banco/banco.csv com gabarito C ou E, campos mapeados um a um (texto_comando → comando, texto_base → textoBase, item_edital_camara → itemEdital, observacoes contendo "parcial" → aderencia "parcial", senão "direta"), mais os itens AUTORAL listados como aprovados em saida/lote*/RECONCILIADO.md, com justificativa; (3) "simulados": todos os de saida/simulados/ (o mais recente de cada número), tipo "diagnóstico" ou "final" conforme o cabeçalho; (4) "lotes": um por RECONCILIADO.md existente, com resumo, curso, pares e pegadinhas extraídos das seções (b), (a), (c) e das "pegadinhas prováveis"; (5) "discursivas": as hipóteses com padrão de resposta dos RECONCILIADO de P2. Valide o JSON (parse sem erro; nenhum item sem id, enunciado e gabarito; nenhum id duplicado) e grave também saida/pacote/pacote_relatorio.md com as contagens. Delegue à secretaria a atualização do estado, imprima o resumo de 10 linhas e "GATILHO A — aguardando decisão humana". Pare. Nenhuma outra tarefa nesta sessão.
