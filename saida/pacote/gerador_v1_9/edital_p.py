# -*- coding: utf-8 -*-
import re
from common import *

def parse_line(prefix_id, prova, text):
    toks = []
    pos = [m for m in re.finditer(r'(?:(?<=\s)|^)(\d+(?:\.\d+)?) (?=[A-ZÀ-Ú])', text)]
    for k, m in enumerate(pos):
        end = pos[k + 1].start() if k + 1 < len(pos) else len(text)
        t = text[m.end():end].strip()
        t = t if t.endswith('etc.') else re.sub(r'\.$', '', t).strip()
        toks.append(dict(id='%s-%s' % (prova, m.group(1)), prova=prova, texto=t))
    return toks

def build_edital():
    out = []
    t14 = [l for l in read('edital/TI_itens_1_4_P1.md').split('\n') if re.match(r'^1 MSOffice', l)][0]
    t58 = [l for l in read('edital/TI_itens_5_8_P1.md').split('\n') if re.match(r'^5 Conceitos', l)][0]
    p2 = read('edital/modulo_RF_IA_P2.md').split('\n')
    l2 = [l for l in p2 if l.startswith('RECONHECIMENTO DE FALA')][0]
    l2 = l2.split(': 1 Reconhecimento', 1)[1]; l2 = '1 Reconhecimento' + l2
    out += parse_line('P1', 'P1', t14) + parse_line('P1', 'P1', t58) + parse_line('P2', 'P2', l2)
    return out

if __name__ == '__main__':
    e = build_edital()
    print(len(e))
    for x in e: print(x['id'], '|', x['texto'][:90])
