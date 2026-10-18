# -*- coding: utf-8 -*-
"""T-104 (v1.10) — entradas de CONTEÚDO acrescentadas à lista fechada X da varredura R (marcas_processo.py, intacto) pela D1 da GBQ
(saida/pacote/T104_D1_v1_10_2026-10-18.md, seção 4): "Secretaria" em "Secretaria-Geral da Mesa" é o órgão da Câmara (homônimo de conteúdo do agente secretaria),
no enunciado e na justificativa de L2-R29, L2-R38 e L2-R45 (onda 3). Mesmo formato de marcas_processo.X: (rótulo, campo, contexto literal, casamento, esperado)."""
X_V110 = [
    ('X9', 'itens[L2-R29].enunciado', 'compete à Secretaria-Geral da Mesa', 'ampliada', 1),
    ('X10', 'itens[L2-R29].justificativa', 'o item troca o órgão por Secretaria-Geral da Mesa', 'ampliada', 1),
    ('X11', 'itens[L2-R38].enunciado', 'compete à Secretaria-Geral da Mesa', 'ampliada', 1),
    ('X12', 'itens[L2-R38].justificativa', 'o item troca o órgão pela Secretaria-Geral da Mesa', 'ampliada', 1),
    ('X13', 'itens[L2-R45].enunciado', 'Quando a Secretaria-Geral da Mesa', 'ampliada', 1),
    ('X14', 'itens[L2-R45].justificativa', 'solicitado pela Secretaria-Geral da Mesa', 'ampliada', 1),
]
