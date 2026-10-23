# marcas_v114.py — T-123 fase 2 (apoio de conferir_t123.py e estudante_md_v114.py) — 2026-10-23 — gerado por gbq-csc
# -*- coding: utf-8 -*-
"""Varredura C-MARCAS (D1 da GBQ, seção 8.1) e varredura PROCESSO (lista R de gerador_v1_12/marcas_processo.py, SHA-256 LF 7ee30de4…c140) sobre texto que a candidata lê.
C-MARCAS: códigos de fonte, pontos de julgamento, "alerta", "Anexo", ids de item, moldura/cota/ficha/leva N/[TS]/TS=, mecanismo (C|E)n, QA/PENDENTE/REVERIFICAR/VOLÁTIL/SEM FONTE, url, "folha" (salvo "folha de pagamento" e
"desconto em folha") e "**". A lista X (conteúdo) abaixo registra os casamentos de PROCESSO que são conteúdo, com contexto literal e contagem esperada (regra do critério de marcas_processo.py): a entrada
da Presidência da República (D2-R21 e D2-R24; remissão à Lei 9.007, art. 2º, parágrafo único) foi registrada pela GBQ por pedido da reconciliação da GCB (seção 4, P1). Não lê relógio."""
import sys
sys.dont_write_bytecode = True
import collections, hashlib, importlib.util, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
MP_PATH = os.path.join(R, 'saida', 'pacote', 'gerador_v1_12', 'marcas_processo.py')
MP_SHA = '7ee30de455a5c0332aca1dae2148d7670eb86bac08294f0c61a80da4484cc140'

CMARCAS = [
    ('codigo de fonte R/F/G/H', re.compile(r'\b[RFGH]\d{1,3}[a-e]?\b')),
    ('ponto A<folha>-<n>', re.compile(r'\bA\d+(?:\.\d+)?-\d+')),
    ('alerta', re.compile(r'(?i)\balerta')),
    ('Anexo', re.compile(r'(?i)\banexo')),
    ('id de item', re.compile(r'\b(?:D[1-6]|L\d|BQ)-R?\d+')),
    ('moldura', re.compile(r'(?i)moldura')),
    ('cota', re.compile(r'(?i)\bcota')),
    ('ficha', re.compile(r'(?i)\bficha')),
    ('leva N', re.compile(r'(?i)\blevas? \d')),
    ('[TS]', re.compile(r'\[TS\]')),
    ('TS=', re.compile(r'TS=')),
    ('mecanismo (C|E)n', re.compile(r'\((?:C|E)\d\)')),
    ('QA', re.compile(r'QA')),
    ('PENDENTE', re.compile(r'PENDENTE')),
    ('REVERIFICAR', re.compile(r'REVERIFICAR')),
    ('VOLATIL', re.compile(r'VOLÁTIL')),
    ('SEM FONTE', re.compile(r'SEM FONTE')),
    ('url', re.compile(r'https?://|www\.')),
    ('folha', re.compile(r'(?i)folha')),
    ('negrito **', re.compile(r'\*\*')),
]
FOLHA_OK = re.compile(r'(?i)folha de pagamento|desconto em folha')

# lista X (conteúdo) para a varredura PROCESSO: (rótulo, id do item, campo, contexto literal, rótulo da regra R, contagem esperada no campo)
X_CONTEUDO = [
    ('X-T123-1', 'D2-R21', 'justificativa', 'Presidência da República', 'ampliada', 1),
    ('X-T123-2', 'D2-R24', 'justificativa', 'Presidência da República', 'ampliada', 1),
]


def modulo_processo():
    b = open(MP_PATH, 'rb').read().replace(b'\r\n', b'\n')
    if hashlib.sha256(b).hexdigest() != MP_SHA:
        raise SystemExit('marcas_processo.py: SHA-256 LF difere do esperado')
    spec = importlib.util.spec_from_file_location('marcas_processo', MP_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


MP = modulo_processo()


def cmarcas(texto):
    """[(regra, casamento, posição)] de C-MARCAS em `texto` (já sem máscara de ids, que só vale para campos id e títulos)."""
    out = []
    for nome, rx in CMARCAS:
        for m in rx.finditer(texto):
            if nome == 'folha' and FOLHA_OK.search(texto[max(0, m.start() - 12):m.end() + 20]):
                continue
            out.append((nome, m.group(0), m.start()))
    return out


def processo(container, texto):
    """([(rótulo R, casamento, início)] fora de X_CONTEUDO, Counter {rótulo X: casamentos}) para `texto` do container 'id.campo'."""
    out = []; xs = collections.Counter()
    for lab, a, b, g in MP.matches(container, texto):
        achou = None
        for (rot, iid, campo, ctx, lr, _n) in X_CONTEUDO:
            if container == iid + '.' + campo and lab == lr:
                p = texto.find(ctx)
                while p >= 0:
                    if p <= a and b <= p + len(ctx):
                        achou = rot; break
                    p = texto.find(ctx, p + 1)
            if achou:
                break
        if achou:
            xs[achou] += 1
        else:
            out.append((lab, g, a))
    return out, xs
