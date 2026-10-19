# -*- coding: utf-8 -*-
"""T-115 (gerador_v1_12) — entradas de CONTEÚDO que a geração propõe para a lista fechada X da varredura R (marcas_processo.py, intacto). PROPOSTA mecânica, registrada no MANIFESTO e no relatório:
só a GBQ, por D1, as confirma ou recusa. Mesmo formato de marcas_processo.X: (rótulo, campo, contexto literal, casamento, esperado).
- X7: a mesma entrada da v1.8, com o índice da pegadinha do L3 deslocado de 25 para 32 pela inserção das pegadinhas novas (mesmo contexto literal; "órgão da Presidência (redação superada)");
- X17 a X19: a medida F1 (métrica de classificação), homônimo de conteúdo do código de fonte Fn: L3-R64 (enunciado e justificativa) e L1-R176 (justificativa); são os MANTER C05 da D1, 3.5;
- X20: a tecla F4 do Excel no resumo de P1-1 (MANTER C05 da D1, 3.5);
- X21: "órgão da Presidência" (ANPD, redação superada) no resumo de P2-4.1, homônimo de conteúdo do agente presidencia."""
X7_ANTIGO = 'X7'
X_V112 = [
    ('X7', 'lotes[L3].pegadinhas[32].texto', 'ANPD como órgão da Presidência (redação superada)', 'ampliada', 1),
    ('X17', 'itens[L3-R64].enunciado', 'a medida F1 é usada', 'Fn', 1),
    ('X18', 'itens[L3-R64].justificativa', 'a medida F1 para RTE e NER', 'Fn', 1),
    ('X19', 'itens[L1-R176].justificativa', 'Precision, Recall e F1', 'Fn', 1),
    ('X20', 'topicos.P1-1.resumo', 'A tecla F4 alterna entre os tipos', 'Fn', 1),
    ('X21', 'topicos.P2-4.1.resumo', 'órgão da Presidência está superada', 'ampliada', 1),
]
