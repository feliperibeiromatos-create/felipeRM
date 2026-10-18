# -*- coding: utf-8 -*-
"""Parser do registro GBQ AUTORAL v2 (saida/gbq/claude_GBQ_Registro_AUTORAL_v3.md): metadados por item."""
import re
from common import read

REG = {}
cur = None
for l in read('saida/gbq/claude_GBQ_Registro_AUTORAL_v3.md').split('\n'):
    m = re.match(r'^## (Lote [0-9]+(?:-C|[ab])?)(?=\s|$)', l)
    if m:
        cur = m.group(1)
        REG[cur] = {}
        continue
    if cur and l.startswith('|'):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if c[0] in ('ID', '---') or set(c[0]) <= set('-'):
            continue
        REG[cur][c[0]] = dict(gab=c[1], sub=c[2], ts=(c[3] == 'TS'), marca=(c[4] if len(c) > 4 else ''))
if __name__ == '__main__':
    for k, v in REG.items():
        print(k, len(v), sum(1 for x in v.values() if x['gab'] == 'C'), sum(1 for x in v.values() if x['ts']), [i for i, x in v.items() if 'VOL' in x['marca']])
