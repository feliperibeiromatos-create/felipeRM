# -*- coding: utf-8 -*-
"""F4 — retirada, SOMENTE por deleção, de marcas internas de processo das justificativas AUTORAL do pacote (v1.2)."""
import re

# (id do item) -> lista de trechos EXATOS a deletar (cada um deve ocorrer exatamente 1 vez na justificativa)
F4_DEL = {
    'L2-Q23': [' (classificação final da CQFP)'],
    'L4-08': [' (v3 — O12)'],
    'L4-09': [' (v3 — O12)'],
    'L4-13': [' (O1)'],
    'L4-15': [' Risco MÉDIO; mantido como está (conferido pela CQFP: "por si só" e "sempre" sustentam o E).'],
    'L4-17': [' Aprovado pela CQFP (art. 12, caput, conferido no Planalto em 07/10/2026).'],
    'L4-18': [' — conferido pela CQFP no Planalto em 08/10/2026'],
    'L4-19': [' aprovado pela CQFP'],
    'L4-20': [' — conferidos pela CQFP no Planalto em 08/10/2026'],
    '4C-06': [', conferido pela CQFP em 07/10/2026, conforme o parecer da rodada 1'],
    '4C-09': ['; R-4C1', ' Retificação 6-A: a redação "sem acesso a busca" não excluía outras ferramentas; "ferramentas externas (como a busca)" alinha o item ao curso 5.3.3 ("sem ferramentas ou RAG").'],
    'A5-14': [' Risco BAIXO.'],
    'A5-15': [' Risco MÉDIO (nome de produto).'],
    'A5-16': [' Risco BAIXO.'],
    'A5-17': [' Risco BAIXO.'],
    '5C-03': [' (redação da v1.1, R-5C1: sem a expressão "lado a lado", que denunciava a troca)'],
    '6B-06': [', conferida pela QA em 08/10/2026'],
    '6B-15': [' (corrigido pela O-3)'],
    'L2-Q21': [' Gabarito E mantido.'],
}

# R1 / C-05 — CAIXA (exceção fechada à regra "só deleção"): apaga a marca e põe maiúscula na inicial que sobra.
# (id do item) -> lista de (trecho atual, trecho novo); cada trecho atual deve ocorrer exatamente 1 vez.
F4_CAIXA = {
    '4C-08': [('Lição O10: o item', 'O item')],
    '5C-06': [('Lição O10: a regra', 'A regra')],
}

F4_LOG = []


def clean(item_id, just):
    dels = F4_DEL.get(item_id)
    cx = F4_CAIXA.get(item_id, [])
    if not dels and not cx:
        return just
    out = just
    for a, b in cx:
        n = out.count(a)
        assert n == 1, (item_id, a, n)
        out = out.replace(a, b, 1)
    for d in (dels or []):
        n = out.count(d)
        assert n == 1, (item_id, d, n)
        out = out.replace(d, '', 1)
    # higiene: nenhum espaço duplo nem espaço antes de pontuação criado pela deleção
    assert '  ' not in out and not re.search(r'\s[.,;:)]', out) and out == out.strip(), (item_id, out)
    F4_LOG.append(dict(id=item_id, antes=just, depois=out, deletado=dels or [], caixa=cx))
    return out
