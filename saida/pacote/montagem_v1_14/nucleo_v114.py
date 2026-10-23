# nucleo_v114.py — T-123 fase 2 — 2026-10-23 — gerado por gbq-csc
# -*- coding: utf-8 -*-
"""Critério inteiro do `nucleo` (D1 da GBQ, seção 6; ponto 3 da v1.2.7) para os itens de DA da v1.14: k1 (data), k2 (linha do ato em DECISOES.md), k3 ("direta" antes de "parcial"), k4 (posição em `itens`).
Os 10 primeiros por itemEdital pela chave (k1, k2, k3, k4) têm nucleo = true. Itens fora de DA mantêm o `nucleo` da v1.13 (não são calculados aqui).
A linha de cada ato é achada pela regex de gerador_v1_12/nucleo.py (`linhas_atos`) sobre DECISOES.md em LF; o módulo aborta (Aborta) se a linha achada diferir da tabela da D1.
Chamado por montar_v1_14.py e por conferir_t123.py. Não lê relógio."""
import collections, re

N = 10


class Aborta(Exception):
    """aborto de montagem (exit 2 na linha de comando)."""


# (chave, ato, linha esperada em DECISOES.md, k1) — tabela da seção 6 da D1
TABELA = collections.OrderedDict([
    ('D1', ('D-LOTED1-CANONICO', 93, '2026-10-18')),
    ('D6', ('D-LOTED6-CANONICO', 117, '2026-10-18')),
    ('D5', ('D-LOTED5-CANONICO', 162, '2026-10-20')),
    ('D2', ('D-LOTED2-CANONICO', 163, '2026-10-20')),
    ('D3', ('D-LOTED3-CANONICO', 164, '2026-10-20')),
    ('D4', ('D-LOTED4-CANONICO', 165, '2026-10-20')),
    ('LEVA1', ('D-T116-LEVA1-ACEITE', 175, '2026-10-20')),
    ('LEVA2', ('D-T116-LEVA2-ACEITE', 176, '2026-10-20')),
    ('LEVA3', ('D-T116-LEVA3-ACEITE', 177, '2026-10-22')),
    ('LEVA4', ('D-T116-LEVA4-ACEITE', 178, '2026-10-22')),
    ('LEVA5', ('D-T116-LEVA5-ACEITE', 179, '2026-10-22')),
    ('LEVA6', ('D-T116-LEVA6-ACEITE', 181, '2026-10-22')),
    ('LEVA7', ('D-T116-LEVA7-ACEITE', 182, '2026-10-22')),
    ('D3-R75', ('D-D3R75-AJL7E1-ACEITE', 185, '2026-10-22')),
    ('LEVA8', ('D-T116-LEVA8-ACEITE', 184, '2026-10-22')),
])
RX_ATO = re.compile(r'^APLICADA [^|]*\| (D-[A-Z0-9-]+) \|')


def linhas_atos(dec_texto):
    """{ato: número da linha (base 1) da primeira ocorrência APLICADA} — regex de gerador_v1_12/nucleo.py, linhas_atos()."""
    out = {}
    for k, l in enumerate(dec_texto.split('\n'), 1):
        m = RX_ATO.match(l)
        if m and m.group(1) not in out:
            out[m.group(1)] = k
    return out


def confere_atos(dec_texto):
    """aborta se a linha achada de algum ato diferir da tabela da D1. Devolve {chave: linha}."""
    la = linhas_atos(dec_texto)
    res = {}
    for ch, (ato, linha, _k1) in TABELA.items():
        if la.get(ato) != linha:
            raise Aborta('nucleo: ato %s na linha %r de DECISOES.md; a tabela da D1 (seção 6) manda a linha %d' % (ato, la.get(ato), linha))
        res[ch] = linha
    return res


def chave_do_ato(item_id, leva_de):
    """chave da TABELA para um item de DA que não é de banco."""
    m = re.fullmatch(r'D([1-6])-(R)?(\d{2})', item_id)
    if not m:
        raise Aborta('nucleo: id de DA fora do padrão: %r' % item_id)
    if not m.group(2):
        return 'D' + m.group(1)
    if item_id == 'D3-R75':
        return 'D3-R75'
    return 'LEVA%d' % leva_de[item_id]


def chaves(itens, datas_banco, leva_de, dec_texto):
    """itens: lista na ordem de `itens` do pacote_estudante. Devolve {id: (itemEdital, (k1, k2, k3, k4), ato)} só para os itens de DA (itemEdital P1-DA-*)."""
    linhas = confere_atos(dec_texto)
    out = collections.OrderedDict()
    for pos, it in enumerate(itens):
        if not it['itemEdital'].startswith('P1-DA-'):
            continue
        iid = it['id']
        if iid.startswith('BQ-'):
            if iid not in datas_banco or not re.fullmatch(r'2026-\d\d-\d\d', datas_banco[iid]):
                raise Aborta('nucleo: data_verificacao ilegível em %s: %r' % (iid, datas_banco.get(iid)))
            k1, k2, ato = datas_banco[iid], 0, 'banco (data_verificacao)'
        else:
            ch = chave_do_ato(iid, leva_de)
            ato, _l, k1 = TABELA[ch]
            k2 = linhas[ch]
        out[iid] = (it['itemEdital'], (k1, k2, 0 if it['aderencia'] == 'direta' else 1, pos), ato)
    return out


def calcula(itens, datas_banco, leva_de, dec_texto):
    """{id: bool} para os itens de DA: os N primeiros de cada itemEdital pela chave (k1, k2, k3, k4)."""
    K = chaves(itens, datas_banco, leva_de, dec_texto)
    por = collections.defaultdict(list)
    for iid, (f, ch, _a) in K.items():
        por[f].append(iid)
    nuc = {}
    for f, ids in por.items():
        for r, iid in enumerate(sorted(ids, key=lambda x: K[x][1])):
            nuc[iid] = r < N
    return nuc, K
