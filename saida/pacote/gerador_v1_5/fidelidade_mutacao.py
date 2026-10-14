# -*- coding: utf-8 -*-
"""T-61 (v1.5; evolução do T-57 e do T-56) — teste negativo do validador de fidelidade: muta arquivos da edição gerada (cópia em pasta temporária; a edição não é tocada)
e confere que estudante_fidelidade.py acusa diferença em cada mutação (o validador não é cego). Saída: out/fidelidade_mutacao.json."""
import json, os, shutil, sys, tempfile
import estudante_fidelidade as F
import estudante_gen as gen
from common import OUT

pacote = gen.SRC
src = gen.OUT
tmp = tempfile.mkdtemp(prefix='fid_mut_')

def muta(dst, arq, fn):
    p = os.path.join(dst, arq)
    t = open(p, encoding='utf-8').read()
    n = fn(t)
    assert n != t, arq
    open(p, 'w', encoding='utf-8', newline='\n').write(n)

MUT = [
 ('L1_itens.md', lambda t: t.replace('**L1-Q01** — ', '**L1-Q01** — Não ', 1)),
 ('L2_gabarito.md', lambda t: t.replace('Gabarito: C', 'Gabarito: E', 1)),
 ('L3_estudo.md', lambda t: t.replace(' lei ', ' ', 1)),
 ('L5_gabarito.md', lambda t: t.replace('Mecanismos: TC troca de conceito', 'Mecanismos: TC troca de conceitos', 1)),
 ('L4_estudo.md', lambda t: t.replace('**não supervisionado × por reforço** | rótulos', '**não supervisionado × por reforço** — rótulos', 1)),
 ('L2_estudo.md', lambda t: t.replace('**degravação**: software', '**degravação** — software', 1)),
 ('SIM-1_gabarito.md', lambda t: t.replace('Mecanismos: TC troca de conceito', 'Mecanismos: TC troca de conceitos', 1)),
 ('BANCO_gabarito.md', lambda t: t.replace('- nota de vigência:', '- Nota: nota de vigência:', 1)),
 ('L1_estudo.md', lambda t: t.replace('e fast)*       | streaming)', 'e fast)* | streaming)', 1)),
 ('L6B_gabarito.md', lambda t: t.replace('Fonte: conceito geral. Tema da tríade', 'Fonte: conceito geral (a definição da tríade não foi confirmada em fonte; ver curso 4.1.1). Tema da tríade', 1)),
 ('DISCURSIVAS_padrao.md', lambda t: t[:t.rindex('Notas de correção\n') + len('Notas de correção\n')] + 'Alínea c da discursiva: NÃO se exige enquadrar o\n' + t[t.rindex('Notas de correção\n') + len('Notas de correção\n'):]),
 # T-64 (v1.5 regerada): a nota de fórmula da peça (D3) e a R6 (D4/D5) voltam ao texto antigo (fórmula da questão) -> a fidelidade tem de acusar
 ('DISCURSIVAS_padrao.md', lambda t: t.replace('Nota (edital, 9.8.5.2, d): NPT = NC − 6 × NE ÷ TL.', 'Nota (edital, 9.8.5.1, d): NQ = NC − 3 × NE ÷ TL.', 1)),
 ('DISCURSIVAS_padrao.md', lambda t: t.replace('Nota: questão: NQ = NC − 3 × NE ÷ TL (9.8.5.1, d); peça: NPT = NC − 6 × NE ÷ TL (9.8.5.2, d). O peso', 'Nota: NQ = NC − 3 × NE ÷ TL. O peso', 1)),
]

# cada mutação é aplicada sozinha, numa cópia nova da edição, e a fidelidade tem de acusar diferença nela (a edição gerada não é tocada)
por_mut = []
for k, (arq, fn) in enumerate(MUT):
    dst = os.path.join(tmp, 'estudante_%d' % k)
    shutil.copytree(src, dst)
    muta(dst, arq, fn)
    F.DIR = dst
    F.DIFFS.clear(); F.NCOMP.clear(); F.CASE_LOG.clear(); F.NOTA_EXC.clear(); F.LEGENDAS.clear(); F.LEG_SIM.clear(); F.REALINHA_LOG.clear()
    P, restos = F.main(pacote, dst)
    por_mut.append((arq, len(F.DIFFS)))
out = {'mutacoes': len(MUT), 'arquivos_mutados': sorted({a for a, _ in MUT}), 'diferencas_detectadas': sum(n for _, n in por_mut),
       'por_mutacao': [{'arquivo': a, 'diferencas': n} for a, n in por_mut], 'todas_detectadas': all(n >= 1 for _, n in por_mut)}
json.dump(out, open(os.path.join(OUT, 'fidelidade_mutacao.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
shutil.rmtree(tmp)
print(json.dumps(out, ensure_ascii=False))
sys.exit(0 if out['todas_detectadas'] else 1)
