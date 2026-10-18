# -*- coding: utf-8 -*-
"""T-48 — remoção de marcas internas para a edição do estudante.
Regra: SOMENTE DELEÇÃO (nunca reescrita). Cada regra apaga trechos; o resultado é sempre
subsequência do texto do pacote. `strip_text(t, cnt)` aplica as regras na ordem e conta
as ocorrências por tipo em `cnt` (collections.Counter)."""
import re

# ---------------------------------------------------------------- regras literais
# (tipo, original, depois). `depois` é `original` com trechos apagados (verificado por
# subsequência no import). Usadas onde a deleção genérica deixaria a frase quebrada ou
# onde o trecho a apagar é uma frase/cláusula de processo.
LITERAL = []          # (fase, tipo, original, depois, escopo)  — escopo: None (todos os arquivos) ou tupla de prefixos de arquivo
OPEN, CLOSE = '\u27e6', '\u27e7'   # ⟦ ⟧ delimitam o trecho apagado na especificação

def is_subseq(new, old):
    i = 0
    for ch in old:
        if i < len(new) and new[i] == ch:
            i += 1
    return i == len(new)

def D(tipo, spec, fase='post', escopo=None):
    """spec: contexto literal com o(s) trecho(s) a apagar entre ⟦ ⟧. Só deleção."""
    old = spec.replace(OPEN, '').replace(CLOSE, '')
    new = re.sub(OPEN + '[^' + CLOSE + ']*' + CLOSE, '', spec)
    assert is_subseq(new, old) and OPEN not in new and CLOSE not in new, spec
    LITERAL.append((fase, tipo, old, new, escopo))

# ---------------------------------------------------------------- regras genéricas
LEAD = r'(?:[ \t]*\n[ \t]*|[ \t]+)?'
FN = r'F\d{1,2}'
FLIST = FN + r'(?:(?:, | e |; )' + FN + r')*'
VER = r'(?:re)?verificad[oa]s? em \d{1,2}/\d{1,2}/\d{4}'

GENERIC = [
    # tipo, regex, grupo(s) mantidos (None = apaga o casamento inteiro)
    ('V', re.compile(LEAD + r'\[V\s+\d{1,2}/\d{1,2}/\d{4}[^\]]*\]'), None),
    ('NORMATIVO — QA (prefixo da base legal)', re.compile(r'\[NORMATIVO — QA: ([^\]]*)\]'), 1),
    ('NORMATIVO — QA', re.compile(LEAD + r'\[NORMATIVO — QA(?:; [^\]]*)?\]'), None),
    ('F (frase "Fonte(s): …")', re.compile(LEAD + r'Fontes?: ' + FLIST + r'(?:, ' + VER + r')?\.'), None),
    ('F (parêntese com verificação)', re.compile(LEAD + r'\(' + FLIST + r', ' + VER + r'\)'), None),
    ('F (parêntese)', re.compile(LEAD + r'\(' + FLIST + r'\)'), None),
    ('F (colchete)', re.compile(LEAD + r'\[' + FLIST + r'\]'), None),
    ('F (parêntese com leitura)', re.compile(r'(?<=[a-z"])[ \t]*\(' + FN + r', leitura de \d{1,2}/\d{1,2}/\d{4}\)'), None),
    ('agente/unidade interna (CQFP, QA, GCB, GCE, CPP)', re.compile(LEAD + r'\(conferid[oa]s? pela (?:CQFP|QA)(?: no Planalto)? em \d{1,2}/\d{1,2}/\d{4}\)'), None),
    # R1 / C-12: a regra com ';' vem ANTES da regra com ',?' (senão sobra o ';' antes do ')')
    ('agente/unidade interna (CQFP, QA, GCB, GCE, CPP)', re.compile(r';[ \t]*conferid[oa]s? pela CQFP(?: no Planalto)? em \d{1,2}/\d{1,2}/\d{4}(?=\))'), None),
    ('agente/unidade interna (CQFP, QA, GCB, GCE, CPP)', re.compile(r',? conferid[oa]s? pela CQFP(?: no Planalto)? em \d{1,2}/\d{1,2}/\d{4}(?=\))'), None),
    ('agente/unidade interna (CQFP, QA, GCB, GCE, CPP)', re.compile(r'conferid[oa]s? pela CQFP(?: no Planalto)? em \d{1,2}/\d{1,2}/\d{4}; '), None),
    ('id interno (R-xx, E-xx, O-xx, D-xx)', re.compile(r'(?m)^R\d\. '), None),
    ('F (parêntese com seção/verificação)', re.compile(LEAD + r'\(' + FN + r', seção [\d.]+(?:, ' + VER + r'|, paráfrase)?\)'), None),
    ('F (fim de parêntese)', re.compile(r';[ \t]*' + FLIST + r'(?=\))'), None),
    ('F (fim de parêntese, após vírgula)', re.compile(r', ' + FLIST + r'(?:, ' + VER + r')?(?=\))'), None),
    ('F (fim de parêntese, após travessão)', re.compile(r'[ \t]*— ' + FLIST + r'(?=\))'), None),
    ('F (fim de parêntese, "com Fn")', re.compile(r', (?:com|COM) ' + FN + r'(?=\))'), None),
    ('F (início de parêntese)', re.compile(r'\((?:' + FN + r')[:;] '), '('),
    ('F (início de parêntese, antes de aspas)', re.compile(r'\(' + FN + r', (?=")'), '('),
    ('F ("Conforme a Fn (leitura …):")', re.compile(r'(?<![\w])Conforme a ' + FN + r'(?: e a ' + FN + r')?(?: \(leitura de \d{1,2}/\d{1,2}/\d{4}\))?:(?:[ \t]*\n|[ \t]+)'), None),
]

CAIXA_HITS = {}      # par (antes) -> ocorrências totais (conferido em estudante_gen)

# ---------------------------------------------------------------- T-57 / D-T54-02: realinhamento do quadro-síntese do L1 (exceção fechada: só ESPAÇOS)
# (prefixo de arquivo, linha inteira DEPOIS das deleções de marca, linha inteira realinhada): a única mudança é a inserção de espaços
# imediatamente antes de um '|' (tantos quantos os caracteres apagados pela deleção da marca); registrada em REALINHA_HITS.
REALINHA = []
REALINHA_HITS = {}

def R(esc, antes, depois):
    ins = len(depois) - len(antes)
    # os espaços entram todos num único ponto, imediatamente antes de um '|' da linha; nada mais muda
    assert ins > 0 and any(antes[p] == '|' and depois == antes[:p] + ' ' * ins + antes[p:] for p in range(len(antes))), (antes, depois)
    REALINHA.append((esc, antes, depois))

def _lit(t, cnt, fase, fname=None):
    for f, tipo, old, new, esc in LITERAL:
        if f == fase and (esc is None or (fname or '').startswith(esc)):
            n = t.count(old)
            if n:
                t = t.replace(old, new)
                cnt[tipo] += n
    return t

def _gen_r1(t, cnt, fname, lista):
    for esc, tipo, rx, keep in lista:
        if not (fname or '').startswith(esc):
            continue
        def sub(m, tipo=tipo, keep=keep):
            cnt[tipo] += 1
            if keep is None: return ''
            return keep if isinstance(keep, str) else m.group(keep)
        t = rx.sub(sub, t)
    return t

def _caixa(t, cnt, fname):
    for esc, antes, depois in CAIXA:
        if (fname or '').startswith(esc):
            n = t.count(antes)
            if n:
                t = t.replace(antes, depois)
                cnt['caixa (minúscula → maiúscula na inicial deixada por deleção)'] += n
                CAIXA_HITS[(esc, antes)] = CAIXA_HITS.get((esc, antes), 0) + n
    return t

def _realinha(t, cnt, fname):      # não conta como remoção (não apaga nada): fica em REALINHA_HITS
    for esc, antes, depois in REALINHA:
        if (fname or '').startswith(esc):
            a, d = '\n' + antes + '\n', '\n' + depois + '\n'
            n = t.count(a)
            if n:
                t = t.replace(a, d)
                REALINHA_HITS[(esc, antes)] = REALINHA_HITS.get((esc, antes), 0) + n
    return t

def strip_text(t, cnt, fname=None):
    t = _lit(t, cnt, 'pre', fname)
    for tipo, rx, keep in GENERIC:
        def sub(m, tipo=tipo, keep=keep):
            cnt[tipo] += 1
            if keep is None: return ''
            return keep if isinstance(keep, str) else m.group(keep)
        t = rx.sub(sub, t)
    t = _lit(t, cnt, 'post', fname)
    t = _realinha(t, cnt, fname)
    # R1: códigos de fonte do L5 e códigos N do L2/L3 (só deleção), depois a lista CAIXA do L6A
    t = _lit(t, cnt, 'l5', fname)
    t = _gen_r1(t, cnt, fname, GENERIC_R1)
    return _caixa(t, cnt, fname)

# ---------------------------------------------------------------- R1 / C-20 e C-22: genéricas por escopo de arquivo
L5C = r'(?:U\d|GG\d|TB\d)'
GENERIC_R1 = [
    # C-20 (L5_*): códigos de fonte U1–U6, GG4, TB2
    ('L5_', 'código de fonte do L5 (U/GG/TB)', re.compile(LEAD + r'\(' + L5C + r'(?:, ' + L5C + r')*\)'), None),
    ('L5_', 'código de fonte do L5 (U/GG/TB)', re.compile(r', (?:U\d|GG\d)(?=\))'), None),
    ('L5_', 'código de fonte do L5 (U/GG/TB)', re.compile(r'(?<=\()(?:U\d|TB\d), '), None),
    ('L5_', 'código de fonte do L5 (U/GG/TB)', re.compile(r'(?<=; )U\d: '), None),
    ('L5_', 'carimbo "Verificado em 8/10/2026" (L5)', re.compile(r' Verificado em 8/10/2026\.'), None),
    # C-22 (L2_*, L3_*): códigos N de nota
    ('L2_', 'código N do L2/L3', re.compile(LEAD + r'\(N\d\)'), None),
    ('L3_', 'código N do L2/L3', re.compile(LEAD + r'\(N\d\)'), None),
    ('L2_', 'código N do L2/L3', re.compile(r'; ver N\d(?=\))'), None),
    ('L3_', 'código N do L2/L3', re.compile(r'; ver N\d(?=\))'), None),
    ('L2_', 'código N do L2/L3', re.compile(r'Ver N\d: '), None),
    ('L3_', 'código N do L2/L3', re.compile(r'Ver N\d: '), None),
    ('L2_', 'código N do L2/L3', re.compile(r'(?<=\()N\d[:;] '), None),
    ('L3_', 'código N do L2/L3', re.compile(r'(?<=\()N\d[:;] '), None),
    ('L2_', 'código N do L2/L3', re.compile(r' — N\d(?=\))'), None),
    ('L3_', 'código N do L2/L3', re.compile(r' — N\d(?=\))'), None),
]

# ---------------------------------------------------------------- R1 / C-15: CAIXA (exceção fechada à regra "só deleção")
# (prefixo de arquivo, antes, depois): a única mudança é minúscula → maiúscula na 1.ª letra do trecho
CAIXA = [
    ('L6A_estudo', 'mesclar combina duas ou mais células', 'Mesclar combina duas ou mais células'),
    ('L6A_estudo', 'a função SE compara um valor', 'A função SE compara um valor'),
    ('L6A_estudo', 'o PROCV pesquisa um valor', 'O PROCV pesquisa um valor'),
    ('L6A_estudo', 'o propósito é fazer todos os slides', 'O propósito é fazer todos os slides'),
    ('L6A_estudo', 'a animação é aplicada a um único elemento', 'A animação é aplicada a um único elemento'),
    ('L6A_estudo', 'o histórico de versões permite ver', 'O histórico de versões permite ver'),
    ('L6A_estudo', 'deleted". por padrão os clientes POP3', 'deleted". Por padrão os clientes POP3'),
    ('L6A_estudo', 'offline. por padrão os clientes IMAP4', 'offline. Por padrão os clientes IMAP4'),
]
for _e, _a, _d in CAIXA:
    _dif = [i for i in range(len(_a)) if _a[i] != _d[i]]
    assert len(_a) == len(_d) and len(_dif) == 1 and _a[_dif[0]].islower() and _d[_dif[0]] == _a[_dif[0]].upper(), (_a, _d)

import literais  # noqa: E402  (registra as regras literais)
