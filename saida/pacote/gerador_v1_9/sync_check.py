# -*- coding: utf-8 -*-
"""Confere que X e Y de cada errata do gerador estão literalmente nas consolidações GCE sincronizadas (13/10/2026; L1 com o Adendo 6, E13, em 14/10/2026)."""
import re, json, sys, os
from common import read, OUT
from p2 import ERRATA, NAO_EXPORTADAS, E13_X, E13_Y

CONS = {'L1': 'saida/gce/GCE_Lote1_consolidacao_GCE.md', 'L1C': 'saida/gce/GCE_Lote1C_consolidacao_GCE.md',
        'L2': 'saida/gce/GCE_Lote2_consolidacao_GCE.md', 'L3': 'saida/gce/GCE_Lote3_consolidacao_GCE.md'}

def nz(s):
    s = re.sub(r'-\n\s*', '-', s)                      # hífen de quebra de linha: junta
    s = s.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")
    s = s.replace('"', "'")                            # aspas aninhadas trocam de tipo na errata
    return re.sub(r'\s+', ' ', s)

def nz2(s):                                            # variante: remove hífen de quebra (palavra cortada)
    s = re.sub(r'(?<=[a-zà-ú])-\n\s*(?=[a-zà-ú])', '', s)
    return nz(s)

res = []
for lote, lst in ERRATA.items():
    t = read(CONS[lote])
    T1, T2 = nz(t), nz2(t)
    for eid, x, y, src in lst:
        if src == 'F5':
            res.append((lote, eid, src, None, None)); continue
        okx = nz(x) in T1 or nz(x) in T2
        if src == 'cons-add':                      # 'acrescentar': Y = X + texto acrescentado; confere o acréscimo
            add = nz(y)[len(nz(x)):].strip()
            oky = add in T1 or add in T2
        elif src == 'cons-cap':                    # Y com inicial maiúscula (X abre frase)
            yy = y[0].lower() + y[1:]
            oky = nz(yy) in T1 or nz(yy) in T2
        else:
            oky = nz(y) in T1 or nz(y) in T2
        res.append((lote, eid, src, okx, oky))
# T-67 (D1-T65-R2; preferência da GCE): a E13 (Adendo 6 do L1), aplicada à montagem do comando da D1 e não ao arquivo do lote, também é conferida contra a consolidação:
# X e Y literais no Adendo 6 e X com exatamente 1 ocorrência em GCE_Lote1_v2_CPP.md (o arquivo-fonte do enunciado (e)), Y com nenhuma
_t1 = nz(read(CONS['L1']))
_adendo6 = _t1[_t1.index('ADENDO 6 GCE'):]
_v2 = nz(read('saida/gce/GCE_Lote1_v2_CPP.md'))
res.append(('L1', 'E13', 'cons', nz(E13_X) in _adendo6 and _v2.count(nz(E13_X)) == 1 and nz(E13_X) in _t1, nz(E13_Y) in _adendo6 and _v2.count(nz(E13_Y)) == 0))
out = []
for r in res:
    out.append('%-4s %-10s fonte=%-5s X na consolidação=%s  Y na consolidação=%s' % r)
bad = [r for r in res if r[2] != 'F5' and not (r[3] and r[4])]
out.append('RESULTADO: %s' % ('TUDO OK' if not bad else 'FALHAS: %s' % bad))
open(os.path.join(OUT, 'sync_check.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('\n'.join(out))
json.dump([dict(lote=r[0], id=r[1], fonte=r[2], x=r[3], y=r[4]) for r in res], open(os.path.join(OUT, 'sync_check.json'), 'w'), ensure_ascii=False)
