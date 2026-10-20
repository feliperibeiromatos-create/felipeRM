# juntar_partes.py — junção mecânica das partes A e B de um lote DA (orquestrador; sem mudança de texto)
# Uso: python3 -I juntar_partes.py D2 T-75 "Agentes públicos e direito administrativo disciplinar"
import re, sys, hashlib, pathlib
lote, tarefa, titulo = sys.argv[1:4]
g = pathlib.Path(__file__).resolve().parents[1]
def ler(p):
    L = (g/f'{lote}_v1_parte{p}.md').read_text(encoding='utf-8').rstrip('\n').split('\n')
    assert L[-1].startswith('FIM DA PARTE'), L[-1]
    L = L[:-1]
    idx = [i for i, l in enumerate(L) if re.match(r'## [1-8]\. ', l)]
    assert [int(L[i][3]) for i in idx] == list(range(1, 9)), [L[i][:12] for i in idx]
    cab = L[1:idx[0]]
    sec = {}
    for k, i in enumerate(idx):
        fim = idx[k+1] if k+1 < len(idx) else len(L)
        sec[int(L[i][3])] = (L[i], L[i+1:fim])
    t5, c5 = sec[5]
    a = next(i for i, l in enumerate(c5) if l.startswith('### 5.1'))
    b = next(i for i, l in enumerate(c5) if l.startswith('### 5.2'))
    sec[5] = (t5, {'pre': c5[:a], 'h51': c5[a], 's51': c5[a+1:b], 'h52': c5[b], 's52': c5[b+1:]})
    return L, cab, sec
A, cabA, sA = ler('A'); B, cabB, sB = ler('B')
out = [f'# {lote}_v1.md — {tarefa} — 2026-10-20 — junção mecânica pelo orquestrador das partes A e B (gcb-cpp); nenhum texto alterado',
       f'LOTE {lote} — {titulo} — v1 — 2026-10-20 (partes A e B)', '',
       f'Fontes: {lote}_v1_parteA.md (SHA-256 {hashlib.sha256((g/f"{lote}_v1_parteA.md").read_bytes()).hexdigest()}) e {lote}_v1_parteB.md (SHA-256 {hashlib.sha256((g/f"{lote}_v1_parteB.md").read_bytes()).hexdigest()}). Regra: seção a seção, parte A antes da B; em 5.1 e 5.2, A e B em sequência.', '',
       '## 0. CABEÇALHOS DAS PARTES', '', '### Parte A'] + cabA + ['', '### Parte B'] + cabB + ['']
for k in range(1, 9):
    tA, cA = sA[k]; tB, cB = sB[k]
    if k != 5:
        out += [tA, '', '### Parte A'] + cA + ['', '### Parte B'] + cB + ['']
    else:
        out += [tA] + cA['pre'] + cB['pre']
        out += [cA['h51']] + cA['s51'] + cB['s51'] + [cA['h52']] + cA['s52'] + cB['s52']
out += ['', f'FIM DO LOTE {lote}']
txt = '\n'.join(out) + '\n'
# conferência: toda linha não vazia das partes (menos linhas 1 e FIM) está na junção, na mesma quantidade
from collections import Counter
orig = Counter(l for L in (A[1:], B[1:]) for l in L if l.strip() and not re.match(r'(## [1-8]\. |### 5\.[12])', l))
novo = Counter(l for l in txt.split('\n') if l.strip())
falta = orig - novo
assert not falta, list(falta.items())[:5]
(g/f'{lote}_v1.md').write_text(txt, encoding='utf-8')
print(lote, 'OK', len(txt.split('\n')), 'linhas; SHA-256', hashlib.sha256(txt.encode()).hexdigest())
