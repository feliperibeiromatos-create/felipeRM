# -*- coding: utf-8 -*-
"""# marcas_processo.py — T-81 (v1.8) — varredura R de marcas de PROCESSO e listas fechadas X (conteúdo) e Y (dúvida) — 2026-10-17 — gerado por gbq-csc
Transcrição literal da D1 da GBQ (saida/pacote/T81_D1_escopo_v1_8_2026-10-17.md, seções 2.3 e 2.4). A gbq-csc NÃO acrescenta entrada a X nem a Y, nem regra de deleção:
só a GBQ, por nova D1. Os limites (?<![\\w]) e (?![\\w]) usam \\w Unicode.

Critério (2.3): cada casamento só é CONTEÚDO se coincidir com uma entrada de X (caminho do campo + contexto literal + contagem esperada); só é DÚVIDA se coincidir com uma
entrada de Y; qualquer outro é PROCESSO. Entrada de X ou de Y com contagem real diferente da esperada (inclusive 0) também é falha."""
import re, collections

# ---------------------------------------------------------------- varredura R (lista fechada)
R = collections.OrderedDict([
    ('V', re.compile(r'\[V\s')),
    ('NORMATIVO', re.compile(r'NORMATIVO — QA')),
    ('Fn', re.compile(r'(?<![\w])F\d{1,2}(?![\w])')),
    ('unidade', re.compile(r'(?<![\w])(?:CQFP|CQE|CPP|GCE|GCB|GBQ|CSC|QA)(?![\w])')),
    ('agente', re.compile(r'(?i)(?<![\w])(?:gbq-[a-z]+|gce-[a-z]+|gcb-[a-z]+|qa-normativo(?:-da)?|corretor-[ab]|presidencia|orquestrador)(?![\w])')),
    ('id', re.compile(r'(?<![\w])(?:[TEORN]-\d{1,3}|D-[A-Z0-9][A-Z0-9-]*)(?![\w])')),
    ('Rn', re.compile(r'(?m)^R\d\. ')),
    ('ampliada', re.compile(r'(?<![\w])(?:Presidência|Fundador|Secretaria|PRES-S|EXEC|BIP|FV)(?![\w])')),
    ('fábrica', re.compile(r'(?i)(?<![\w])fábrica(?![\w])')),
    ('modelo', re.compile(r'(?<![\w])(?:Claude|Sonnet|Opus|Haiku|ChatGPT)(?![\w])')),
    ('ferramenta', re.compile(r'(?i)claude\.ai|Insumo_')),
    ('carimbo', re.compile(r'(?:re)?verificad[oa]s? em \d{1,2}/\d{1,2}/\d{4}|conferid[oa]s? pel[ao]|\(leitura de \d|[Vv]erificado em \d')),
])

# Termos fora da lista: ficam como estão; só se registra a contagem (2.3, último parágrafo)
FORA = collections.OrderedDict([
    ('Presidente', re.compile(r'Presidente')),
    ('Projeto', re.compile(r'Projeto')),
    ('OpenAI', re.compile(r'OpenAI')),
    ('Anthropic', re.compile(r'Anthropic')),
    ('Gemini', re.compile(r'Gemini')),
    ('GPT', re.compile(r'GPT')),
    ('Whisper', re.compile(r'Whisper')),
    ('insumo', re.compile(r'insumo')),
])

# ---------------------------------------------------------------- listas X e Y (2.4): (rótulo, campo, contexto literal, casamento, esperado)
X = [
    ('X1', 'itens[BQ-0040].comando', 'da Presidência do CNJ', 'ampliada', 1),
    ('X2', 'itens[BQ-0064].enunciado', 'O ChatGPT e o DeepSeek', 'modelo', 1),
    ('X3', 'lotes[L2].curso', 'da Presidência), orientação de bancada', 'ampliada', 1),
    ('X4', 'lotes[L3].curso', '(órgão da Presidência da', 'ampliada', 1),
    ('X5', 'lotes[L3].curso', 'ANPD como órgão da Presidência (redação superada)', 'ampliada', 1),
    ('X6', 'lotes[L3].pares[20].b', 'órgão da Presidência (redação superada)', 'ampliada', 1),
    ('X7', 'lotes[L3].pegadinhas[25].texto', 'ANPD como órgão da Presidência (redação superada)', 'ampliada', 1),
    ('X8', 'lotes[L6A].curso', 'A tecla F4, com a referência', 'Fn', 1),
]
Y = [
    ('Y1', 'itens[L4-11].justificativa', 'O F4 afirma que', 'Fn', 1),
]

# Na edição v1.8 (out/estudante/): os 11 casamentos esperados (2.4, último parágrafo): (rótulo, arquivo, contexto literal, casamento, esperado)
X_ED = [
    ('X1', 'BANCO_itens.md', 'da Presidência do CNJ', 'ampliada', 1),
    ('X1', 'SIM-0_folha.md', 'da Presidência do CNJ', 'ampliada', 1),
    ('X2', 'BANCO_itens.md', 'O ChatGPT e o DeepSeek', 'modelo', 1),
    ('X2', 'SIM-0_folha.md', 'O ChatGPT e o DeepSeek', 'modelo', 1),
    ('X3', 'L2_estudo.md', 'da Presidência), orientação de bancada', 'ampliada', 1),
    ('X4', 'L3_estudo.md', '(órgão da Presidência da', 'ampliada', 1),
    # X5, X6 e X7 ficam no mesmo arquivo da edição (L3_estudo.md: X5 no curso, X6 nos pares, X7 nas pegadinhas) e seus contextos se sobrepõem
    # (o de X6 está contido nos de X5 e X7); na edição contam-se juntos, 3 casamentos, sem repartir entre as três entradas.
    ('X5+X6+X7', 'L3_estudo.md', 'órgão da Presidência (redação superada)', 'ampliada', 3),
    ('X8', 'L6A_estudo.md', 'A tecla F4, com a referência', 'Fn', 1),
]
Y_ED = [
    ('Y1', 'L4_gabarito.md', 'O F4 afirma que', 'Fn', 1),
]

# ---------------------------------------------------------------- percurso do pacote: (caminho, string)
def walk(o, path=''):
    """todas as strings de um pacote, com o caminho. Itens, lotes, simulados e discursivas são indexados pelo `id` quando têm; o resto, pelo índice base 0.
    Nos lotes, pares e pegadinhas usam o índice base 0 (como na D1)."""
    if isinstance(o, str):
        yield path, o
    elif isinstance(o, dict):
        for k, v in o.items():
            yield from walk(v, (path + '.' + k) if path else k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            if isinstance(v, dict) and 'id' in v and path in ('itens', 'lotes', 'simulados', 'discursivas', 'edital') and isinstance(v['id'], str):
                key = v['id']
            else:
                key = str(i)
            yield from walk(v, '%s[%s]' % (path, key))
    # números, booleanos e None: sem texto

def matches(container, text):
    """lista de (rótulo, início, fim, texto) de R em `text`."""
    out = []
    for lab, rx in R.items():
        for m in rx.finditer(text):
            out.append((lab, m.start(), m.end(), m.group(0)))
    return out

def classifica(strings, X_, Y_):
    """strings: [(container, texto)]. Devolve dict com:
    - processo: casamentos de R fora de X e de Y (lista de (container, rótulo, casamento, contexto));
    - conteudo / duvida: por entrada, a contagem real (rótulo da entrada -> n);
    - falhas: lista de mensagens (contagem diferente da esperada, casamento consumido por duas entradas);
    - todos: todos os casamentos (container, rótulo, casamento, contexto, destino)."""
    por_cont = collections.defaultdict(list)
    for c, t in strings:
        por_cont[c].append(t)
    ms = {}      # (container, índice da string, rótulo, início, fim) -> (casamento, contexto)
    textos = {}
    for c, t in strings:
        pass
    consumido = {}
    falhas = []
    contagem = collections.OrderedDict()
    res_ms = []
    for idx, (c, t) in enumerate(strings):
        for lab, a, b, g in matches(c, t):
            res_ms.append([c, idx, lab, a, b, g, t[max(0, a - 35):b + 35].replace('\n', '↵'), None])
    for tag, ents, destino in (('X', X_, 'conteúdo'), ('Y', Y_, 'dúvida')):
        for rot, cont, ctx, lab, esp in ents:
            n = 0
            ocorr = 0
            for idx, (c, t) in enumerate(strings):
                if c != cont:
                    continue
                pos = 0
                while True:
                    i = t.find(ctx, pos)
                    if i < 0:
                        break
                    ocorr += 1
                    for m in res_ms:
                        if m[0] == c and m[1] == idx and m[2] == lab and i <= m[3] and m[4] <= i + len(ctx):
                            if m[7] is not None and m[7] != rot:
                                falhas.append('%s: casamento já consumido por %s (%s, %r)' % (rot, m[7], c, m[5]))
                            else:
                                m[7] = rot
                                n += 1
                    pos = i + len(ctx)
            contagem[rot] = n
            if n != esp:
                falhas.append('%s (%s): contagem real %d, esperada %d (contexto %r em %s: %d ocorrência(s) do contexto)' % (rot, destino, n, esp, ctx, cont, ocorr))
    processo = [(m[0], m[2], m[5], m[6]) for m in res_ms if m[7] is None]
    return dict(processo=processo, contagem=contagem, falhas=falhas, todos=[(m[0], m[2], m[5], m[6], m[7] or 'PROCESSO') for m in res_ms])

def fora_da_lista(strings):
    """contagem dos termos fora da lista (sem ação), por termo."""
    c = collections.OrderedDict((k, 0) for k in FORA)
    for _, t in strings:
        for k, rx in FORA.items():
            c[k] += len(rx.findall(t))
    return c
