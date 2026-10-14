# -*- coding: utf-8 -*-
"""Itens de banco (v1.2): lê as colunas texto_comando, texto_base e aderencia de banco/banco.csv (T-29/T-42, D1-b)."""
import csv, re, io
from common import *

def norm(s): return re.sub(r'\s+', ' ', s).strip()

def load_banco():
    with open(P('banco/banco.csv'), encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter=';'))

NOTA_RX = re.compile(r'nota de vigência:.*$', re.S)

def nota_de(obs):
    """Texto literal de observacoes a partir do rótulo 'nota de vigência:' (inclusive), até o fim do segmento
    (segmentos de observacoes são separados por '; ' mas a nota contém ';' interno; vai até o fim da célula,
    conforme a regra 4 da v1.1.1: a nota é o último segmento registrado pela D1)."""
    m = NOTA_RX.search(obs)
    return m.group(0).rstrip() if m else None

def build_banco():
    rows = load_banco()
    out = []; info = dict(excl=[], vol=[], nota=[], tb=[], mp_sim0=[])
    for r in rows:
        if r['anulado'] != 'nao' or r['gabarito'] not in ('C', 'E'):
            info['excl'].append((r['id'], r['gabarito'], r['anulado'])); continue
        obs = r['observacoes']
        assert r['aderencia'] in ('direta', 'parcial'), (r['id'], r['aderencia'])
        it = dict(id=r['id'], rotulo=r['rotulo'], certame=r['certame'], cargo=r['cargo'], ano=int(r['ano_aplicacao']),
                  numero=int(r['numero_item']), comando=r['texto_comando'], textoBase=r['texto_base'],
                  enunciado=r['texto_integral'], gabarito=r['gabarito'], justificativa='',
                  itemEdital=r['item_edital_camara'], aderencia=r['aderencia'], url=r['url_caderno'])
        if r['texto_base']: info['tb'].append(r['id'])
        if obs.startswith('VOLÁTIL'):
            it['volatil'] = True; info['vol'].append(r['id'])
        n = nota_de(obs)
        if n:
            it['nota'] = n; info['nota'].append(r['id'])
        out.append(it)
    return out, info

def parse_sim0():
    """SIM-0 v0.2: lista de BQ na ordem do simulado + comando/texto por item (conferência contra o banco)."""
    lines = read('saida/simulados/simulado_0_v0.2.md').split('\n')
    cmds = {}; items = {}; curcmd = None
    i = 0
    while i < len(lines):
        l = lines[i]
        m = re.match(r'^### Comando (\d+)$', l)
        if m:
            curcmd = int(m.group(1)); buf = []
            j = i + 1
            while j < len(lines) and (lines[j].startswith('>') or not lines[j].strip()):
                if lines[j].startswith('>'): buf.append(lines[j][1:].strip())
                elif buf: break
                j += 1
            cmds[curcmd] = norm(' '.join(buf)); i = j; continue
        m = re.match(r'^\*\*(\d+)\.\*\* (.*)$', l)
        if m:
            items[int(m.group(1))] = (curcmd, m.group(2).strip())
        i += 1
    mp = {}
    for l in read('saida/simulados/simulado_0_v0.2_gabarito.md').split('\n'):
        m = re.match(r'^\| (\d+) \| (\d+) \| (BQ-\d{4}) \|', l)
        if m: mp[int(m.group(1))] = (int(m.group(2)), m.group(3))
    return cmds, items, mp

if __name__ == '__main__':
    o, i = build_banco()
    print(len(o), {k: (len(v)) for k, v in i.items()}, i['nota'], i['vol'])
