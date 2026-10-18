# -*- coding: utf-8 -*-
"""F3 — pegadinhas: uma por entrada, com rótulo (contrato v1.2, regra (d))."""
import re
from common import *

PEG_INFO = []      # dicts: lote, itemEdital, rotulo, origem, modo, n_frag, orig
GENERIC = re.compile(r'^(PEGADINHAS?\b.*|DEFINI[ÇC][ÃA]O\b.*|EXEMPLO\b.*)$', re.I)


def depth0_positions(s, ch):
    """Posições de `ch` fora de parênteses e de aspas (retas e curvas)."""
    pos = []
    d = 0
    inq = False
    for i, c in enumerate(s):
        if c == '(':
            d += 1
        elif c == ')':
            d = max(0, d - 1)
        elif c in '"“”':
            # aspas retas alternam; curvas: abre/fecha por tipo
            if c == '"':
                inq = not inq
            elif c == '“':
                inq = True
            else:
                inq = False
        elif c == ch and d == 0 and not inq:
            pos.append(i)
    return pos


def open_paren_depth0(s):
    """Posições de '(' que abrem no nível 0 (fora de outros parênteses e de aspas)."""
    pos = []
    d = 0
    inq = False
    for i, c in enumerate(s):
        if c == '(':
            if d == 0 and not inq:
                pos.append(i)
            d += 1
        elif c == ')':
            d = max(0, d - 1)
        elif c == '"':
            inq = not inq
        elif c == '\u201c':
            inq = True
        elif c == '\u201d':
            inq = False
    return pos


def split_text(t):
    """Retorna (modo, [(sep, frag)]) com sep = trecho literal que precede o fragmento (para reconstruir)."""
    t = t.strip()
    # 0) assertiva única com explicação: '"assertiva" → ERRADO (...)': uma pegadinha só, não se desdobra
    if re.match(r'^["\u201c]', t) and '\u2192' in t:
        return 'unica', [('', t)]
    # 1) enumeradores (1), (2), ... fora de parênteses, em sequência
    cands = [m for m in re.finditer(r'(?:^|(?<=\s))\((\d+)\)\s', t) if m.start() == 0 or True]
    enum = []
    expect = 1
    d0 = open_paren_depth0(t)       # '(' fora de parênteses
    for m in cands:
        if int(m.group(1)) == expect and m.start() in d0:
            enum.append(m)
            expect += 1
    if len(enum) >= 2 and enum[0].start() == 0:
        parts = []
        for k, m in enumerate(enum):
            end = enum[k + 1].start() if k + 1 < len(enum) else len(t)
            raw = t[m.end():end]
            sep = t[m.start():m.end()]
            parts.append((sep, raw))
        return 'enumeradores', parts
    # 2) ';' fora de parênteses e aspas
    sc = depth0_positions(t, ';')
    if sc:
        parts = []
        prev = 0
        sep = ''
        for p in sc:
            parts.append((sep, t[prev:p]))
            sep = ';'
            prev = p + 1
        parts.append((sep, t[prev:]))
        return 'ponto-e-virgula', parts
    return 'unica', [('', t)]


# R1 / C-06 a C-08 (regra (d) do contrato): fragmento que só se lê com o verbo do anterior, ou que é ilustração
# do anterior, não é fronteira de desdobramento: reúne-se ao fragmento anterior com o separador original "; ".
# texto exato do fragmento -> (motivo)
MERGE_PREV = {
    '"Câmara" (instituição) vs "câmara" (sala) é decisão de contexto que o modelo pode errar.': 'ilustração do fragmento anterior (L1 P2-1.5)',
    'empilhado quando se quer comparar as partes entre si.': 'depende do verbo do fragmento anterior (L5 barras)',
    'que a caixa vai do mínimo ao máximo ou contém todos os dados': 'depende do verbo do fragmento anterior (L5 box plot)',
    'que os bigodes vão até 1,5 desvio padrão': 'depende do verbo do fragmento anterior (L5 box plot)',
    'que mostra frequência por intervalo (isso é histograma).': 'depende do verbo do fragmento anterior (L5 box plot)',
}
MERGE_LOG = []     # (fragmento reunido, motivo)


def fragments(t):
    """Fragmentos literais (strip) e verificação de reconstrução."""
    modo, parts = split_text(t)
    frs = [raw.strip() for sep, raw in parts]
    if modo == 'ponto-e-virgula':
        merged = []
        for f in frs:
            if f in MERGE_PREV and merged:
                merged[-1] = merged[-1] + '; ' + f
                MERGE_LOG.append((f, MERGE_PREV[f]))
            else:
                merged.append(f)
        frs = merged
    # reconstrução: enumeradores -> sep + raw ; ';' -> raw ; (espaços dos extremos preservados em raw)
    rec = ''.join((sep + raw) if modo == 'enumeradores' else (sep + raw) for sep, raw in parts)
    assert rec == t.strip(), (modo, t[:80])
    return modo, frs


def edital_text(eid, edital):
    for e in edital:
        if e['id'] == eid:
            return e['texto']
    raise SystemExit('edital sem ' + eid)


def clean_title(t):
    t = t.strip()
    t = re.sub(r'^\d+(?:\.\d+)*\s+', '', t)          # numeração inicial
    if ' — ' in t:
        t = t.split(' — ')[0].strip()                 # marcas/fontes após o travessão
    return t
