# edital_da.py — gera as 46 entradas P1-DA-<n> do edital, texto literal (edital/DA_itens_1_12_P1.md, linha do edital)
import re, json, sys, pathlib
raiz = pathlib.Path(__file__).resolve().parents[4]
src = (raiz/'edital/DA_itens_1_12_P1.md').read_text(encoding='utf-8')
linha = [l for l in src.splitlines() if l.startswith('1 Estado, governo')][0].strip()
pat = re.compile(r'(?:(?<=^)|(?<=\. ))(\d+(?:\.\d+)?) (?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ])')
ms = list(pat.finditer(linha))
out = []
for i, m in enumerate(ms):
    fim = ms[i+1].start() if i+1 < len(ms) else len(linha)
    txt = linha[m.end():fim].strip()
    if txt.endswith('.'): txt = txt[:-1]
    out.append({"id": "P1-DA-" + m.group(1), "prova": "P1", "texto": txt})
assert len(out) == 46, len(out)
assert len({o['id'] for o in out}) == 46
# reconstrução: número + texto + ". " reproduz a linha literal
rec = ' '.join(o['id'][6:] + ' ' + o['texto'] + '.' for o in out)
assert rec == linha, 'reconstrução difere do literal'
dest = raiz/'saida/gcb/DA_plataforma/edital_DA.json'
dest.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(out), 'entradas; reconstrução literal OK ->', dest)
