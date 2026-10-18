# -*- coding: utf-8 -*-
"""T-104 — reescreve o MANIFESTO.md do gerador v1.10 (passo 8): todos os arquivos da pasta (fora o próprio MANIFESTO.md) e de out/, com SHA-256 e bytes, e o estado de
cada arquivo frente à v1_9 (igual, alterado, novo; ativo ou só registro). Modo ENSAIO: nada é promovido (a geração final espera o gatilho A da T-106; D-ONDA4-FILA (3)). Não lê relógio."""
import hashlib, json, os
from common import HERE, OUT, REPO
import config_v110 as cfg

G9 = os.path.join(REPO, 'saida', 'pacote', 'gerador_v1_9')
ATIVOS = {'_run.py': 'passos 1–8 (executor isolado)', 'config_v110.py': 'módulo (chaves da ocorrência)', 'build_v110.py': 'passo 1', 'reforco_v110.py': 'passo 1 (módulo)',
          'estudante_json.py': 'passo 2', 'reforco_marcas.py': 'passo 2 (módulo; onda 1)', 'reforco_marcas_v110.py': 'passo 2 (módulo; 225 novos)', 'nucleo.py': 'passo 2 (módulo: nucleo)',
          'marcas_x_v110.py': 'passo 2 (módulo: X9–X14)', 'estudante_marcas.py': 'passo 2 (módulo)', 'estudante_gen.py': 'passo 2 (módulo: lote_of, lote_fund, COMPL, FUSAO)',
          'estudante_fidelidade.py': 'passo 2 (módulo: only_deletions)', 'marcas_processo.py': 'passo 2 (módulo: varredura R)', 'registro_adendo_v110.py': 'passo 3',
          'estudante_md_v110.py': 'passo 4', 'validate_v110.py': 'passo 5', 'conferencias_v110.py': 'passo 6', 'validar_erros_teste.py': 'passo 7', 'validar_erros.py': 'passo 7 (módulo e CLI)',
          'manifesto_v1_10.py': 'passo 8', 'common.py': 'módulo', 'refs.py': 'módulo', 'rodar_tudo.sh': 'runner'}
def h(p): b = open(p, 'rb').read(); return hashlib.sha256(b).hexdigest(), len(b)
L = []; w = L.append
w('# MANIFESTO — T-104 — gerador v1.10 do pacote.json, do pacote_estudante.json e da edição .md (ENSAIO) — 2026-10-18 — gerado por gbq-gerencia (manifesto_v1_10.py)')
w('')
w('Origem: cópia de `saida/pacote/gerador_v1_9/` (intacta), sem `out/`, mais as mudanças mínimas da D1 da GBQ (`saida/pacote/T104_D1_v1_10_2026-10-18.md`). Base do pacote: a v1.9 aceita (D-PACOTE-V19), lida do git no commit `c26fc13` (SHA-256 `13660554…`); os 334 itens e os demais blocos não são regenerados, salvo as trocas da D-ABSORCAO-V110 e da D-ABSORCAO-V110-E. Novos: 225 itens (L6B-R01/R02, onda 2, L1-R131, onda 3).')
w('')
w('Modo desta execução: E_CURSO=%s; E_PADRAO=%s; E_L2R131=%s; geradoEm %s. ENSAIO: nenhuma saída promovida; `saida/pacote/pacote.json` e `pacote_estudante.json` continuam a v1.9.' % (cfg.E_CURSO, cfg.E_PADRAO, cfg.E_L2R131, cfg.GERADO_EM))
w('')
w('## Pipeline (`sh rodar_tudo.sh`; cada passo com `python3 -I -B _run.py <script>`)')
w('| Passo | Script | Saída |')
w('|---|---|---|')
for n, s, o in [(1, 'build_v110.py', '`out/pacote.json`, `out/stats_v110.json`, `out/gen_stdout.txt`'), (2, 'estudante_json.py', '`out/pacote_estudante.json`, `out/estudante_json.json`, `out/estudante_json_stdout.txt`'),
                (3, 'registro_adendo_v110.py', '`out/registro_adendo2.md`, `out/registro_stdout.txt`'), (4, 'estudante_md_v110.py', '`out/estudante/` (35 arquivos), `out/estudante_md_stdout.txt`'),
                (5, 'validate_v110.py', '`out/validate_v110.json`, `out/validate_stdout.txt`'), (6, 'conferencias_v110.py', '`out/conferencias_v110.json`, `out/conferencias_stdout.txt`'),
                (7, 'validar_erros_teste.py', '`out/casos_erros/`, `out/validar_erros_stdout.txt`'), (8, 'manifesto_v1_10.py', 'este `MANIFESTO.md`')]:
    w('| %d | `%s` | %s |' % (n, s, o))
w('')
w('## Arquivos da pasta (SHA-256 e bytes, como em disco)')
w('| Arquivo | SHA-256 | Bytes | Frente à v1_9 | Uso na v1.10 |')
w('|---|---|---|---|---|')
for f in sorted(os.listdir(HERE)):
    p = os.path.join(HERE, f)
    if not os.path.isfile(p) or f == 'MANIFESTO.md':
        continue
    s, b = h(p)
    q = os.path.join(G9, f)
    est = 'novo' if not os.path.exists(q) else ('igual' if open(q, 'rb').read() == open(p, 'rb').read() else 'alterado')
    w('| `%s` | `%s` | %d | %s | %s |' % (f, s, b, est, ATIVOS.get(f, 'herdado; só registro (não executado)')))
w('')
w('## out/ (regerado a cada execução; prévia do ensaio)')
w('| Arquivo | SHA-256 | Bytes |')
w('|---|---|---|')
for r, ds, fs in sorted(os.walk(OUT)):
    for f in sorted(fs):
        p = os.path.join(r, f); s, b = h(p)
        w('| `out/%s` | `%s` | %d |' % (os.path.relpath(p, OUT), s, b))
cv = json.load(open(os.path.join(OUT, 'conferencias_v110.json'), encoding='utf-8')); vv = json.load(open(os.path.join(OUT, 'validate_v110.json'), encoding='utf-8'))
w('')
w('Resultado desta execução: validate_v110 %d/%d OK; conferencias_v110 %d/%d OK.' % (vv['ok'], vv['total'], cv['ok'], cv['total']))
open(os.path.join(HERE, 'MANIFESTO.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
print('MANIFESTO.md: %d linhas' % len(L))
