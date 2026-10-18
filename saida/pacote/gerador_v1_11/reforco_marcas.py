# -*- coding: utf-8 -*-
"""T-94 (v1.9) — deleções da camada do estudante nas justificativas dos 48 itens de reforço (lista FECHADA; D1 da GBQ, saida/pacote/T94_D1_v1_9_2026-10-18.md, seção 3).
Só deleção, sem texto novo. Fora desta lista, a justificativa do reforço passa literal ao pacote_estudante.json (as regras de estudante_marcas.strip_text, escritas para os
arquivos de origem dos lotes canônicos da v1.8, não se aplicam a ela). Contagens esperadas fechadas: ESPERADO (conferidas em estudante_json.py)."""
import re

REGRAS = [
    # (rótulo, regex, ocorrências esperadas no conjunto dos 48)
    ('V (classificação interna de VOLÁTIL no início da justificativa do reforço)',
     re.compile(r'^VOLÁTIL \((?:baixo|ALTO: limite numérico de produto)\); REVERIFICAR\. '), 2),          # L2-R07, L2-R18
    ('V (instrução de montagem e de reescrita do item volátil, L2-R18)',
     re.compile(re.escape(' Inapto a simulado final até a reverificação de 4–8/1/2027; se a página mudar o número antes de janeiro, reescrever o item sem o limite.')), 1),
]
ESPERADO = {r[0]: r[2] for r in REGRAS}
HITS = {}       # (id, rótulo) -> n


def strip_reforco(texto, cnt, iid=None):
    for lab, rx, _ in REGRAS:
        n = len(rx.findall(texto))
        if n:
            texto = rx.sub('', texto)
            cnt[lab] += n
            if iid is not None:
                HITS[(iid, lab)] = HITS.get((iid, lab), 0) + n
    return texto
