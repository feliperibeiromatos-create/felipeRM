# -*- coding: utf-8 -*-
"""T-94 — reescreve o MANIFESTO.md do gerador v1.9 (passo 7): lista, com SHA-256 e bytes, todos os arquivos da pasta (fora o próprio MANIFESTO.md) e de out/, as saídas promovidas e
o estado de cada arquivo frente à v1_8 (igual, alterado, novo; ativo ou só registro). Não lê relógio."""
import hashlib, json, os
from common import HERE, OUT, REPO

G8 = os.path.join(REPO, 'saida', 'pacote', 'gerador_v1_8')
ATIVOS = {'_run.py': 'passos 1–7 (executor isolado)', 'build_v19.py': 'passo 1', 'reforco.py': 'passo 1 (módulo)', 'estudante_json.py': 'passo 2', 'reforco_marcas.py': 'passo 2 (módulo)',
          'estudante_marcas.py': 'passo 2 (módulo)', 'estudante_gen.py': 'passo 2 (módulo: lote_of, lote_fund, COMPL, FUSAO)', 'estudante_fidelidade.py': 'passo 2 (módulo: only_deletions)',
          'marcas_processo.py': 'passo 2 (módulo: varredura R)', 'registro_adendo_v19.py': 'passo 3', 'validate_v19.py': 'passo 4', 'conferencias_v19.py': 'passo 5',
          'validar_erros_teste.py': 'passo 6', 'validar_erros.py': 'passo 6 (módulo e CLI)', 'manifesto_v1_9.py': 'passo 7', 'common.py': 'módulo', 'refs.py': 'módulo',
          'edital_p.py': 'módulo (validate_v19)', 'rodar_tudo.sh': 'runner'}
def h(p): b = open(p, 'rb').read(); return hashlib.sha256(b).hexdigest(), len(b)
L = []; w = L.append
w('# MANIFESTO — T-94 — gerador v1.9 do pacote.json e do pacote_estudante.json — 2026-10-18 — gerado por gbq-gerencia (manifesto_v1_9.py)')
w('')
w('Origem: cópia de `saida/pacote/gerador_v1_8/` (intacta), sem `out/`, mais as mudanças mínimas da D1 da GBQ (`saida/pacote/T94_D1_v1_9_2026-10-18.md`). Base do pacote: a v1.8 aceita (D-PACOTE-V18), lida do git no commit `46496ca` (SHA-256 `09d4a457…`); os 286 itens e os demais blocos não são regenerados. Novos: os 48 itens da onda 1 do reforço.')
w('')
w('## Pipeline (`sh rodar_tudo.sh`; cada passo com `python3 -I -B _run.py <script>`)')
w('| Passo | Script | Saída |')
w('|---|---|---|')
for n, s, o in [(1, 'build_v19.py', '`out/pacote.json`, `out/stats_v19.json`, `out/gen_stdout.txt`'), (2, 'estudante_json.py', '`out/pacote_estudante.json`, `out/estudante_json.json`, `out/estudante_json_stdout.txt`'),
                (3, 'registro_adendo_v19.py', '`out/registro_adendo1.md`, `out/registro_stdout.txt`'), (4, 'validate_v19.py', '`out/validate_v19.json`, `out/validate_stdout.txt`'),
                (5, 'conferencias_v19.py', '`out/conferencias_v19.json`, `out/conferencias_stdout.txt`'), (6, 'validar_erros_teste.py', '`out/casos_erros/`, `out/validar_erros_stdout.txt`'),
                (7, 'manifesto_v1_9.py', 'este `MANIFESTO.md`')]:
    w('| %d | `%s` | %s |' % (n, s, o))
w('')
w('## Arquivos da pasta (SHA-256 e bytes, como em disco)')
w('| Arquivo | SHA-256 | Bytes | Frente à v1_8 | Uso na v1.9 |')
w('|---|---|---|---|---|')
for f in sorted(os.listdir(HERE)):
    p = os.path.join(HERE, f)
    if not os.path.isfile(p) or f == 'MANIFESTO.md':
        continue
    s, b = h(p)
    q = os.path.join(G8, f)
    est = 'novo' if not os.path.exists(q) else ('igual' if open(q, 'rb').read() == open(p, 'rb').read() else 'alterado')
    w('| `%s` | `%s` | %d | %s | %s |' % (f, s, b, est, ATIVOS.get(f, 'herdado; só registro (não executado)')))
w('')
w('## out/ (regerado a cada execução)')
w('| Arquivo | SHA-256 | Bytes |')
w('|---|---|---|')
for r, ds, fs in sorted(os.walk(OUT)):
    for f in sorted(fs):
        p = os.path.join(r, f); s, b = h(p)
        w('| `out/%s` | `%s` | %d |' % (os.path.relpath(p, OUT), s, b))
w('')
w('## Saídas promovidas ao repositório (cópia byte a byte de out/)')
w('| Destino | Origem | SHA-256 | Bytes | Igual à origem |')
w('|---|---|---|---|---|')
for dst, src in [('saida/pacote/pacote.json', 'pacote.json'), ('saida/pacote/pacote_estudante.json', 'pacote_estudante.json'),
                 ('saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo1_2026-10-18.md', 'registro_adendo1.md')]:
    pd, ps = os.path.join(REPO, dst), os.path.join(OUT, src)
    s, b = h(pd) if os.path.exists(pd) else ('—', 0)
    w('| `%s` | `out/%s` | `%s` | %d | %s |' % (dst, src, s, b, 'sim' if os.path.exists(pd) and open(pd, 'rb').read() == open(ps, 'rb').read() else 'NÃO'))
cv = json.load(open(os.path.join(OUT, 'conferencias_v19.json'), encoding='utf-8')); vv = json.load(open(os.path.join(OUT, 'validate_v19.json'), encoding='utf-8'))
w('')
w('Resultado desta execução: validate_v19 %d/%d OK; conferencias_v19 %d/%d OK.' % (vv['total'] - vv['falhas'], vv['total'], cv['total'] - cv['falhas'], cv['total']))
open(os.path.join(HERE, 'MANIFESTO.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
print('MANIFESTO.md: %d linhas' % len(L))
