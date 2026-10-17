# -*- coding: utf-8 -*-
"""Extração dos lotes GCE (P2): Lotes 1, 1-C, 2, 3."""
import re
from common import *


def strip_boiler(lines):
    out = []
    i, n = 0, len(lines)
    while i < n:
        l = lines[i]
        if l.startswith('FIM DA PARTE') or l.startswith('FIM DO LOTE') or l.startswith('Fundador: gravar'):
            i += 1
            continue
        if l.startswith('ENTREGA DE LOTE'):
            j = i
            keep = None
            while j < n and lines[j].strip():
                if lines[j].startswith('Todos os dispositivos abaixo'):
                    keep = j
                    break
                j += 1
            if keep is not None:
                i = keep
                continue
            i = j
            continue
        out.append(l)
        i += 1
    return out


def load(rel, lote, errata):
    raw = read(rel).split('\n')
    lines = strip_boiler(raw)
    lines = fix_hyphen_wraps(lines, rel)
    lines = fix_endash_wraps(lines, rel)
    text = '\n'.join(lines)
    for (eid, old, new, src) in errata:
        text = apply_errata(text, lote, eid, old, new)
    return text.split('\n')


MARK = [('a', r'^\(a\) '), ('b', r'^\(b\) '), ('c', r'^\(c\) '), ('d', r'^\(d\) '), ('dg', r'^\(d-G\) '), ('e', r'^\(e\) '), ('f', r'^\(f\) ')]


def sections(lines):
    """Retorna dict nome -> (ini, fim) de conteúdo (sem as linhas '=====')."""
    idx = {}
    for name, rx in MARK:
        for i, l in enumerate(lines):
            if re.match(rx, l) and i > 0 and lines[i - 1].startswith('====='):
                idx[name] = i
                break
    order = sorted(idx.items(), key=lambda kv: kv[1])
    res = {}
    for k, (name, i) in enumerate(order):
        start = i + 1
        # pula a linha '=====' de fechamento do cabeçalho; títulos de seção podem quebrar em 2 linhas
        while start < len(lines) and not lines[start].startswith('====='):
            start += 1
        start += 1
        end = order[k + 1][1] - 1 if k + 1 < len(order) else len(lines)
        res[name] = (start, end)
    return res


def curso_md(sec_lines):
    """Converte o bloco (a) em markdown mínimo: '--- X ---' vira '## X'."""
    out = []
    i = 0
    L = trim_blank(sec_lines)
    while i < len(L):
        l = L[i]
        if l.startswith('--- '):
            t = l[4:]
            while not t.rstrip().endswith('---'):
                i += 1
                t += ' ' + L[i].strip()
            t = t.rstrip()[:-3].strip()
            out.append('## ' + t)
        else:
            out.append(l.rstrip())
        i += 1
    return '\n'.join(out).strip('\n')


def text_block(sec_lines):
    return '\n'.join(trim_blank(sec_lines))


def pegadinhas_from_curso(curso_lines, label=lambda h: h):
    """Cada bloco 'PEGADINHA PROVÁVEL' (parágrafo seguinte) vira um registro {itemEdital, texto}."""
    res = []
    cur = None
    i = 0
    L = curso_lines
    while i < len(L):
        l = L[i]
        m = re.match(r'^## (\d+\.\d+) ', l)
        if m:
            cur = m.group(1)
        if l.strip() == 'PEGADINHA PROVÁVEL' or l.strip() == 'PEGADINHAS ADICIONAIS':
            j = i + 1
            buf = []
            while j < len(L) and L[j].strip():
                buf.append(L[j].strip())
                j += 1
            res.append({'item': cur, 'texto': unwrap(' '.join(buf))})
            i = j
            continue
        i += 1
    return res


def _depth0_split(s, sep):
    """Divide s no primeiro `sep` fora de parênteses. Retorna (antes, depois) ou (s, None)."""
    d = 0
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == '(':
            d += 1
        elif ch == ')':
            d = max(0, d - 1)
        elif d == 0 and s.startswith(sep, i):
            return s[:i], s[i + len(sep):]
        i += 1
    return s, None


def pares_p2(sec_lines):
    """Lista numerada ' 1. A vs B: como.' (continuação em linhas indentadas)."""
    L = trim_blank(sec_lines)
    items = []
    for l in L:
        m = re.match(r'^\s*(\d+)\.\s+(.*)$', l)
        if m and (not items or int(m.group(1)) == items[-1][0] + 1):
            items.append([int(m.group(1)), m.group(2).strip()])
        elif items and l.strip():
            items[-1][1] += ' ' + l.strip()
    res = []
    for n, t in items:
        a, rest = _depth0_split(t, ' vs ')
        if rest is None:
            LOG.append('PARES: par sem " vs " (b vazio): %r' % t[:70])
            res.append({'a': t.strip().rstrip('.'), 'b': '', 'como': ''})
            continue
        b, como = _depth0_split(rest, ': ')
        if como is None:
            b, como = b.strip().rstrip('.'), ''
        res.append({'a': a.strip(), 'b': b.strip(), 'como': como.strip()})
    return res


def parse_items(sec_lines, idrx):
    """Blocos separados por linha em branco; bloco começa com id. Retorna (comando_linhas, [(id, texto)])."""
    items = []
    pre = []
    blocks = []
    cur = []
    for l in sec_lines:
        if l.strip():
            cur.append(l)
        else:
            if cur:
                blocks.append(cur)
            cur = []
    if cur:
        blocks.append(cur)
    for b in blocks:
        m = re.match(r'^(' + idrx + r')\.\s+(.*)$', b[0])
        if m:
            txt = unwrap(m.group(2) + ' ' + ' '.join(b[1:]))
            items.append((m.group(1), txt))
        else:
            pre.append(unwrap(' '.join(b)))
    return pre, items


def parse_dg(sec_lines, idrx):
    """Entradas do gabarito comentado: bloco que começa com id; devolve {id: texto completo unwrap}."""
    blocks = []
    cur = []
    for l in sec_lines:
        if l.strip():
            cur.append(l)
        else:
            if cur:
                blocks.append(cur)
            cur = []
    if cur:
        blocks.append(cur)
    res = {}
    for b in blocks:
        m = re.match(r'^(' + idrx + r')\.\s+(.*)$', b[0])
        if m:
            res[m.group(1)] = unwrap(m.group(2) + ' ' + ' '.join(b[1:]))
    return res
