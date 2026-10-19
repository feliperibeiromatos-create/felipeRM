# -*- coding: utf-8 -*-
"""T-108 e T-109 (gerador_v1_11) — passo 10: reescreve o MANIFESTO.md: todos os arquivos da pasta (fora o próprio MANIFESTO.md), de ensaio/ e de out/, com SHA-256 e bytes, e o estado de cada
arquivo da pasta frente ao gerador_v1_10 (igual, alterado, novo; ativo ou só registro). O modo (ENSAIO ou GERAÇÃO FINAL) vem de config_v111.FINAL. Não lê relógio."""
import hashlib, json, os
from common import HERE, OUT, REPO
import config_v111 as cfg

G10 = os.path.join(REPO, 'saida', 'pacote', 'gerador_v1_10')
ATIVOS = {'_run.py': 'executor isolado de todos os passos (saída em UTF-8)', 'config_v111.py': 'módulo (chaves da ocorrência; único lugar do número da versão)',
          'tabelas_v111.py': 'módulo (leitura e validação das tabelas, inventário e caminhos)', 'limpeza_v111.py': 'módulo (aplicação ocorrência a ocorrência; `interno`)',
          'inventario_v111.py': 'passo 8 e módulo (posições dos casamentos; extensão aos .md)', 'build_v111.py': 'passo 1', 'estudante_json_v111.py': 'passo 2',
          'marcas_x_v111.py': 'passo 2 (módulo: entradas X propostas pelo ensaio)', 'registro_adendo_v111.py': 'passo 3', 'estudante_md_v111.py': 'passo 4',
          'registro_alteracoes_v111.py': 'passo 5', 'validate_v111.py': 'passo 6', 'conferencias_v111.py': 'passo 7', 'fidelidade_mutacao_v111.py': 'passo 9', 'manifesto_%s.py' % cfg.TAG: 'passo 10',
          'validar_erros_teste.py': 'passo 7 (C-15)', 'validar_erros.py': 'passo 7 (módulo e CLI)', 'rodar_tudo.sh': 'runner',
          'common.py': 'módulo', 'refs.py': 'módulo', 'nucleo.py': 'passo 2 (módulo: nucleo)', 'config_v110.py': 'módulo (E_L2R131, ATO_L2R131 lidos por nucleo.py e estudante_json_v111.py)',
          'reforco_marcas.py': 'passo 2 (módulo)', 'reforco_marcas_v110.py': 'passo 2 (módulo)', 'marcas_x_v110.py': 'passo 2 (módulo)', 'estudante_marcas.py': 'passo 2 (módulo)',
          'estudante_gen.py': 'passos 2 e 4 (módulo: lote_of, lote_fund, COMPL, FUSAO)', 'estudante_fidelidade.py': 'passo 2 (módulo: only_deletions)', 'marcas_processo.py': 'passo 2 (módulo: varredura R)'}


def h(p):
    b = open(p, 'rb').read()
    return hashlib.sha256(b).hexdigest(), len(b)


def main():
    L = []; w = L.append
    final = cfg.FINAL
    w('# MANIFESTO — T-108 e T-109 — gerador v%s do pacote.json, do pacote_estudante.json e da edição .md (%s) — 2026-10-18 — gerado por gbq-csc (manifesto_%s.py)' % (cfg.VERSAO, 'GERAÇÃO FINAL' if final else 'ENSAIO', cfg.TAG))
    w('')
    w('Origem: cópia de `saida/pacote/gerador_v1_10/` (intacta; nenhum byte mudou), sem `out/` e sem `__pycache__/`, mais as mudanças da D1 da GBQ (`saida/pacote/T108_D1_pacote_M2_2026-10-18.md`). '
      'Base do pacote: o pacote.json v1.10 aceito, lido do git no commit `%s` (SHA-256 `%s`); itens, ids, ordem, enunciados, gabaritos, simulados e demais blocos não mudam. '
      'Mudam só as edições das tabelas de limpeza (registradas no campo `interno`), o `itemEdital` do L2-R16 (T-109), `nome` e `geradoEm`.' % (cfg.BASE[0], cfg.BASE[2]))
    w('')
    w('Modo desta execução: ALVO=%s; VERSAO=%s; E_L2R16=%s (ATO_L2R16 %s); geradoEm %s. %s' % (cfg.ALVO, cfg.VERSAO, cfg.E_L2R16, cfg.ATO_L2R16, cfg.GERADO_EM,
      'GERAÇÃO FINAL.' if final else 'ENSAIO: lê as tabelas de ensaio de `ensaio/` (linhas reais das Gerências onde passam nas conferências, mais linhas sintéticas); nenhuma saída é promovida; '
      '`saida/pacote/pacote.json` e `pacote_estudante.json` continuam a v1.10.'))
    pend = cfg.confere_final()
    w('')
    w('Condições de entrada da geração final ainda não cumpridas: %s.' % ('; '.join(pend) if pend else 'nenhuma'))
    w('')
    w('## Pipeline (`sh rodar_tudo.sh`; cada passo com `python3 -I -B _run.py <script>`)')
    w('| Passo | Script | Saída |')
    w('|---|---|---|')
    for n, s, o in [(0, 'ensaio/gera_tabelas_ensaio.py (só ENSAIO)', '`ensaio/*.csv`, `ensaio/relatorio_ensaio.json`, `ensaio/excecoes_ensaio.json`'),
                    (1, 'build_v111.py', '`out/pacote.json`, `out/stats_%s.json`, `out/folhas_%s.json`' % (cfg.TAG, cfg.TAG)),
                    (2, 'estudante_json_v111.py', '`out/pacote_estudante.json`, `out/estudante_json.json`'),
                    (3, 'registro_adendo_v111.py', '`out/registro_adendo3.md`'),
                    (4, 'estudante_md_v111.py', '`out/estudante/` (35 arquivos), `out/estudante_md_%s.json`' % cfg.TAG),
                    (5, 'registro_alteracoes_v111.py', '`out/registro_alteracoes_%s.csv`, `_manter.csv`, `_resumo.md`' % cfg.TAG),
                    (6, 'validate_v111.py', '`out/validate_%s.json` (C-4, C-9, C-10, C-13, C-16)' % cfg.TAG),
                    (7, 'conferencias_v111.py', '`out/conferencias_%s.json` (C-1 a C-3, C-5 a C-8, C-11, C-12, C-14, C-15, C-17), `out/casos_erros/`' % cfg.TAG),
                    (8, 'inventario_v111.py', '`out/inventario.csv`, `out/inventario.json`'),
                    (9, 'fidelidade_mutacao_v111.py', '`out/fidelidade_mutacao_%s.json` (bloco M)' % cfg.TAG),
                    (10, 'manifesto_%s.py' % cfg.TAG, 'este `MANIFESTO.md`')]:
        w('| %d | `%s` | %s |' % (n, s, o))
    w('')
    w('## Arquivos da pasta (SHA-256 e bytes, como em disco)')
    w('| Arquivo | SHA-256 | Bytes | Frente ao v1_10 | Uso na v%s |' % cfg.VERSAO)
    w('|---|---|---|---|---|')
    for f in sorted(os.listdir(HERE)):
        p = os.path.join(HERE, f)
        if not os.path.isfile(p) or f == 'MANIFESTO.md':
            continue
        s, b = h(p)
        q = os.path.join(G10, f)
        est = 'novo' if not os.path.exists(q) else ('igual' if open(q, 'rb').read() == open(p, 'rb').read() else 'alterado')
        w('| `%s` | `%s` | %d | %s | %s |' % (f, s, b, est, ATIVOS.get(f, 'herdado; só registro (não executado)')))
    w('')
    w('## ensaio/ (regerado no passo 0; só ENSAIO)')
    w('| Arquivo | SHA-256 | Bytes |')
    w('|---|---|---|')
    ed = os.path.join(HERE, 'ensaio')
    if os.path.isdir(ed):
        for f in sorted(os.listdir(ed)):
            p = os.path.join(ed, f)
            if os.path.isfile(p):
                s, b = h(p)
                w('| `ensaio/%s` | `%s` | %d |' % (f, s, b))
    w('')
    w('## out/ (regerado a cada execução; %s)' % ('fonte dos promovidos' if final else 'prévia do ensaio, nada promovido'))
    w('| Arquivo | SHA-256 | Bytes |')
    w('|---|---|---|')
    for r, ds, fs in sorted(os.walk(OUT)):
        for f in sorted(fs):
            p = os.path.join(r, f); s, b = h(p)
            w('| `out/%s` | `%s` | %d |' % (os.path.relpath(p, OUT).replace(os.sep, '/'), s, b))
    vv = json.load(open(os.path.join(OUT, 'validate_%s.json' % cfg.TAG), encoding='utf-8'))
    cv = json.load(open(os.path.join(OUT, 'conferencias_%s.json' % cfg.TAG), encoding='utf-8'))
    mm = json.load(open(os.path.join(OUT, 'fidelidade_mutacao_%s.json' % cfg.TAG), encoding='utf-8'))
    w('')
    w('Resultado desta execução: validate_v111 %d/%d OK; conferencias_v111 %d OK, %d PENDENTE, %d FALHA; fidelidade_mutacao_v111 %d/%d casos.' % (vv['ok'], vv['total'], cv['ok'], cv['pendentes'], cv['falhas'], mm['ok'], mm['total']))
    open(os.path.join(HERE, 'MANIFESTO.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
    print('MANIFESTO.md: %d linhas' % len(L))


if __name__ == '__main__':
    main()
