# -*- coding: utf-8 -*-
"""T-115 (gerador_v1_12, D1 da GBQ, seção 1) — leitura dos 23 insumos: cada arquivo é lido do disco, `\r\n` vira `\n` e o SHA-256 do conteúdo LF é conferido contra a tabela de config_v112.
Qualquer divergência para tudo (Falha, código de saída 1). Utilidades comuns aos módulos _v112. Não lê relógio."""
import hashlib, json, re, sys
from common import P as PATH
import config_v112 as cfg

FENCE = '`' * 3


class Falha(Exception):
    def __init__(self, tag, msg):
        super().__init__('%s: %s' % (tag, msg))
        self.tag, self.msg = tag, msg


def sha256_lf_bytes(b):
    return hashlib.sha256(b.replace(b'\r\n', b'\n')).hexdigest()


LEITOR = None      # gancho dos testes de mutação (bloco M): função rel -> bytes que substitui a leitura do disco; None = disco


def le_bytes_insumo(rel):
    if LEITOR is not None:
        return LEITOR(rel)
    with open(PATH(rel), 'rb') as f:
        return f.read()


def le_insumo(rel):
    """Texto LF do insumo `rel` (tem de estar na tabela da seção 1); SHA-256 LF conferido."""
    if rel not in cfg.SHA:
        raise Falha('C-1', '%s: fora da tabela de insumos' % rel)
    raw = le_bytes_insumo(rel)
    h = sha256_lf_bytes(raw)
    if h != cfg.SHA[rel]:
        raise Falha('C-1', '%s: SHA-256 (LF) %s diferente do aceito %s' % (rel, h, cfg.SHA[rel]))
    return raw.replace(b'\r\n', b'\n').decode('utf-8')


def confere_todos():
    """Lê os 23 insumos; devolve [(n, caminho, sha_lf, bytes_disco)]."""
    out = []
    for n, rel, sha, ato in cfg.INSUMOS:
        raw = le_bytes_insumo(rel)
        le_insumo(rel)
        out.append((n, rel, sha, len(raw)))
    return out


def bloco_json(t, rel, k=0, n=1):
    """k-ésimo bloco ```json``` de t (n = quantidade esperada)."""
    bs = re.findall(FENCE + r'json\n(.*?)\n' + FENCE, t, re.S)
    if len(bs) != n:
        raise Falha('C-1', '%s: %d bloco(s) json (esperado %d)' % (rel, len(bs), n))
    return json.loads(bs[k])
