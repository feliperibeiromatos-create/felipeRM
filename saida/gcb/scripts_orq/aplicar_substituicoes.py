# aplicar_substituicoes.py — aplica a tabela CSV de substituições exatas de uma reconciliação (cada texto_antigo 1 vez)
# Uso: python3 -I aplicar_substituicoes.py <reconciliacao.md> <origem.md> <destino.md>
import csv, io, re, sys, hashlib, pathlib
rec, src, dst = map(pathlib.Path, sys.argv[1:4])
bloco = re.search(r'```csv\n(.*?)\n```', rec.read_text(encoding='utf-8'), re.S).group(1)
linhas = list(csv.DictReader(io.StringIO(bloco), delimiter=';'))
t = src.read_text(encoding='utf-8')
for r in linhas:
    velho = r['texto_antigo'].replace('\\n', '\n'); novo = r['texto_novo'].replace('\\n', '\n')
    c = t.count(velho)
    if c != 1: sys.exit(f"substituição {r['n']}: texto_antigo ocorre {c} vezes")
    t = t.replace(velho, novo)
dst.write_text(t, encoding='utf-8')
print(len(linhas), 'substituições;', dst.name, 'SHA-256', hashlib.sha256(t.encode()).hexdigest())
