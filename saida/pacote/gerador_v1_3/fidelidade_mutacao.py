# -*- coding: utf-8 -*-
"""T-56 — teste negativo do validador de fidelidade: muta 4 arquivos da edição gerada (cópia em pasta temporária; a edição não é tocada)
e confere que estudante_fidelidade.py acusa diferença em cada mutação (o validador não é cego). Saída: out/fidelidade_mutacao.json."""
import json, os, shutil, sys, tempfile
import estudante_fidelidade as F
import estudante_gen as gen
from common import OUT

pacote = gen.SRC
src = gen.OUT
tmp = tempfile.mkdtemp(prefix='fid_mut_')
dst = os.path.join(tmp, 'estudante')
shutil.copytree(src, dst)

def muta(arq, fn):
    p = os.path.join(dst, arq)
    t = open(p, encoding='utf-8').read()
    n = fn(t)
    assert n != t, arq
    open(p, 'w', encoding='utf-8', newline='\n').write(n)

# (a) enunciado de item: troca uma letra; (b) gabarito: inverte C/E; (c) curso do estudo: apaga uma palavra; (d) legenda: altera a legenda de um lote
muta('L1_itens.md', lambda t: t.replace('**L1-Q01** — ', '**L1-Q01** — Não ', 1))
muta('L2_gabarito.md', lambda t: t.replace('Gabarito: C', 'Gabarito: E', 1))
muta('L3_estudo.md', lambda t: t.replace(' lei ', ' ', 1))
muta('L5_gabarito.md', lambda t: t.replace('Mecanismos: TC troca de conceito', 'Mecanismos: TC troca de conceitos', 1))

F.DIR = dst
F.DIFFS.clear(); F.NCOMP.clear(); F.CASE_LOG.clear(); F.NOTA_EXC.clear(); F.LEGENDAS.clear()
P, restos = F.main(pacote, dst)
arqs = sorted({d[0] for d in F.DIFFS})
out = {'mutacoes': 4, 'arquivos_mutados': ['L1_itens.md', 'L2_gabarito.md', 'L3_estudo.md', 'L5_gabarito.md'], 'diferencas_detectadas': len(F.DIFFS), 'arquivos_com_diferenca': arqs,
       'todas_detectadas': all(a in arqs or any(a in str(d) for d in F.DIFFS) for a in ['L1_itens.md', 'L2_gabarito.md', 'L3_estudo.md', 'L5_gabarito.md'])}
json.dump(out, open(os.path.join(OUT, 'fidelidade_mutacao.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
shutil.rmtree(tmp)
print(json.dumps(out, ensure_ascii=False))
sys.exit(0 if out['todas_detectadas'] and out['diferencas_detectadas'] >= 4 else 1)
