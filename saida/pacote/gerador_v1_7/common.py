# -*- coding: utf-8 -*-
"""Utilidades comuns do gerador T-05 (pacote.json v1)."""
import re, os

# T-56 (pontos 4 da T-55): a raiz do repositório e a pasta de saída vêm de __file__ (nada de caminho absoluto nem relativo ao cwd).
# O gerador fica em <raiz>/saida/pacote/gerador_v1_7/ (T-71; mesma profundidade da v1_6, da v1_5, da v1_4 e da v1_3).
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
OUT = os.path.join(HERE, 'out')
LOG = []          # mensagens de ambiguidade / ajuste (vão ao relatório)
ERRATA_LOG = []   # (lote, id, ocorrências)


def P(rel):
    return os.path.join(REPO, rel)


def read(rel):
    with open(P(rel), encoding='utf-8') as f:
        return f.read()


def ws_regex(s):
    """Regex tolerante a quebras de linha/espaços para um trecho literal."""
    parts = [re.escape(p) for p in s.split()]
    return r'\s+'.join(parts)


def apply_errata(text, lote, eid, old, new, expect=1, note=''):
    """Aplica a errata "onde se lê X, leia-se Y" por substituição exata (tolerante a quebra de linha).
    Estado: APLICADA (X encontrado `expect` vez(es) e Y ausente), JÁ PRESENTE (X ausente e Y presente),
    FALHA (SystemExit) caso contrário: X ausente sem Y, X mais de `expect` vez(es), ou X e Y ambos presentes.
    Ocorrências de Y que se sobrepõem a uma ocorrência de X (Y contido em X) ou de X contido em Y não contam."""
    rx = re.compile(ws_regex(old))
    ry = re.compile(ws_regex(new))
    xs = [m.span() for m in rx.finditer(text)]
    ys = [m.span() for m in ry.finditer(text)]
    def inside(a, b):      # span a contido em span b
        return b[0] <= a[0] and a[1] <= b[1]
    x_free = [a for a in xs if not any(inside(a, b) for b in ys)]      # X que não faz parte de um Y
    y_free = [b for b in ys if not any(inside(b, a) for a in xs)]      # Y que não faz parte de um X
    if len(x_free) == expect and not y_free:
        st = 'APLICADA'
    elif not x_free and y_free:
        st = 'JÁ PRESENTE'
    else:
        st = 'FALHA'
    ERRATA_LOG.append(dict(lote=lote, id=eid, x=len(xs), y=len(ys), x_free=len(x_free), y_free=len(y_free), estado=st, note=note))
    if st == 'FALHA':
        raise SystemExit('ERRATA %s %s: FALHA (X=%d livre=%d, Y=%d livre=%d; esperado X=%d)' % (lote, eid, len(xs), len(x_free), len(ys), len(y_free), expect))
    if st == 'JÁ PRESENTE':
        return text
    return rx.sub(lambda m: new, text)


# --- reparo de hifenização de quebra de linha (arquivos GCE, ~72 colunas) ---
# (final da linha antes do hífen, início da linha seguinte) -> 'drop' remove o hífen (palavra cortada);
# o que não estiver aqui mantém o hífen (palavra composta/URL) e junta sem espaço.
DROP = [
    ('identifi', 'cação'), ('decodi', 'ficador'), ('vocabu', 'lário'), ('lingua', 'gem'),
    ('processa', 'mento'), ('interpre', 'tativa'), ('necessi', 'dade'), ('segmen', 'ta'),
    ('ativi', 'dade'), ('amos', 'tras'), ('diari', 'zação'), ('pon', 'tuação'), ('obstru', 'ção'),
    ('lati', 'nismos'), ('reverbe', 'ração'), ('trans', 'crição'), ('lin', 'guagem'),
    ('trans', 'cribe'), ('pronun', 'ciamentos'),
]
# (início da linha seguinte) mantendo hífen: URL e compostos
# 'gemini-3.5-trans-' + 'cribe)' é palavra cortada (DROP ('trans','cribe'))


def fix_hyphen_wraps(lines, src):
    """Junta linhas que terminam em hífen de quebra. Retorna nova lista de linhas."""
    out = []
    i = 0
    while i < len(lines):
        l = lines[i]
        if i + 1 < len(lines) and re.search(r'[A-Za-zÀ-ú0-9]-$', l) and re.match(r'\s*[a-zà-ú0-9]', lines[i + 1]):
            nxt = lines[i + 1].lstrip()
            left = l[:-1]
            key = None
            for a, b in DROP:
                if left.lower().endswith(a) and nxt.lower().startswith(b):
                    key = 'drop'
                    break
            if key == 'drop':
                merged = left + nxt
                LOG_HY.append((src, l[-20:] + '|' + nxt[:12], 'removido'))
            else:
                merged = l + nxt
                LOG_HY.append((src, l[-20:] + '|' + nxt[:12], 'mantido'))
            lines = lines[:i] + [merged] + lines[i + 2:]
            continue   # reavalia (pode haver nova quebra com hífen)
        out.append(l)
        i += 1
    return out


LOG_HY = []


F1_LOG = []


def unwrap(text):
    """Une linhas de um bloco (hard-wrap) em uma linha, com espaço simples."""
    return re.sub(r'\s+', ' ', text).strip()


def fix_endash_wraps(lines, src):
    """F1 (v1.2): quebra de linha logo depois de travessão curto (en dash) entre letras junta sem espaço
    ("áudio–" + "texto" = "áudio–texto"). Registra cada junção em F1_LOG."""
    out = []
    i = 0
    while i < len(lines):
        l = lines[i]
        if i + 1 < len(lines) and re.search(r'[A-Za-zÀ-ú]\u2013$', l) and re.match(r'\s*[A-Za-zÀ-ú]', lines[i + 1]):
            F1_LOG.append((src, l[-30:] + '|' + lines[i + 1].strip()[:20]))
            lines = lines[:i] + [l + lines[i + 1].lstrip()] + lines[i + 2:]
            continue
        out.append(l)
        i += 1
    return out


def strip_boiler_gce(lines):
    """Remove cabeçalhos de transporte das partes de um arquivo GCE:
    'FIM DA PARTE x/y', bloco 'ENTREGA DE LOTE ...' até a linha em branco, 'FIM DO LOTE', 'Fundador: gravar ...'."""
    out = []
    i = 0
    n = len(lines)
    while i < n:
        l = lines[i]
        if l.startswith('FIM DA PARTE') or l.startswith('FIM DO LOTE'):
            i += 1
            continue
        if l.startswith('ENTREGA DE LOTE'):
            while i < n and lines[i].strip():
                i += 1
            continue
        if l.startswith('Fundador: gravar'):
            i += 1
            continue
        out.append(l)
        i += 1
    return out


def find_idx(lines, pred, start=0, end=None):
    end = len(lines) if end is None else end
    for i in range(start, end):
        if pred(lines[i]):
            return i
    return -1


def trim_blank(lines):
    a, b = 0, len(lines)
    while a < b and not lines[a].strip():
        a += 1
    while b > a and not lines[b - 1].strip():
        b -= 1
    return lines[a:b]
