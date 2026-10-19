# -*- coding: utf-8 -*-
"""T-115 (gerador_v1_12) — passo 10: reescreve o MANIFESTO.md: todos os arquivos da pasta (fora o próprio MANIFESTO.md) e de out/, com SHA-256 e bytes, o estado de cada arquivo da pasta frente ao
gerador_v1_11 (igual, alterado, novo; ativo ou só registro), as contagens conferidas contra os arquivos canônicos (D1, instrução 5), os entregáveis (fonte dos promovidos; nada é promovido) e a lista dos .md
do estudante que mudam. O modo (ENSAIO ou GERAÇÃO FINAL) vem de config_v112.FINAL. Não lê relógio."""
import collections, csv, hashlib, json, os, re
from common import HERE, OUT, REPO
import config_v112 as cfg
import fontes_v112 as F

G11 = os.path.join(REPO, 'saida', 'pacote', cfg.GERADOR_ANTERIOR)
ATIVOS = {'_run.py': 'executor isolado de todos os passos (saída em UTF-8)', 'config_v112.py': 'módulo (chaves da ocorrência; único lugar do número da versão)',
          'fontes_v112.py': 'módulo (leitura dos 23 insumos, SHA-256 LF)', 'reforco_v112.py': 'passo 1 (módulo: itens novos)', 'limpeza_v112.py': 'passo 1 (módulo: erratas e limpeza L-1 a L-5)',
          'pegadinhas_v112.py': 'passo 1 (módulo: pegadinhas de pares)', 'topicos_v112.py': 'passo 1 (módulo: `topicos`)', 'build_v112.py': 'passo 1',
          'estudante_json_v112.py': 'passo 2', 'marcas_x_v112.py': 'passo 2 (módulo: entradas X propostas, a confirmar pela GBQ)', 'registro_adendo_v112.py': 'passo 3',
          'estudante_md_v112.py': 'passo 4', 'registro_alteracoes_v112.py': 'passo 5', 'validate_v112.py': 'passo 6', 'checks_v112.py': 'passos 6, 7 e 9 (módulo: conferências)',
          'conferencias_v112.py': 'passo 7', 'inventario_v112.py': 'passo 8 e módulo', 'fidelidade_mutacao_v112.py': 'passo 9', 'manifesto_%s.py' % cfg.TAG: 'passo 10',
          'validar_erros_teste.py': 'passo 7 (C-15)', 'validar_erros.py': 'passo 7 (módulo e CLI)', 'rodar_tudo.sh': 'runner', 'common.py': 'módulo', 'refs.py': 'módulo',
          'nucleo.py': 'passo 1 e 2 (módulo: nucleo; atos novos por registra_extra)', 'config_v110.py': 'módulo (E_L2R131, ATO_L2R131 lidos por nucleo.py e estudante_json_v112.py)',
          'reforco_marcas.py': 'passo 2 (módulo)', 'reforco_marcas_v110.py': 'passo 2 (módulo)', 'marcas_x_v110.py': 'passo 2 (módulo)', 'marcas_x_v111.py': 'passo 2 (módulo)',
          'estudante_marcas.py': 'passo 2 (módulo)', 'estudante_gen.py': 'passos 2 e 4 (módulo: lote_of, lote_fund, COMPL, FUSAO)', 'estudante_fidelidade.py': 'passo 2 (módulo: only_deletions)',
          'marcas_processo.py': 'passo 2 (módulo: varredura R)', 'inventario_v111.py': 'passo 8 (módulo importado sem mudança: regras do inventário)'}
PROMOCAO = [('out/pacote.json', 'saida/pacote/pacote.json'), ('out/pacote_estudante.json', 'saida/pacote/pacote_estudante.json'),
            ('out/registro_adendo4.md', 'saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo4_%s.md' % cfg.GERADO_EM),
            ('out/registro_alteracoes_%s.csv' % cfg.TAG, 'saida/pacote/registro_alteracoes_%s.csv' % cfg.TAG),
            ('out/registro_alteracoes_%s_resumo.md' % cfg.TAG, 'saida/pacote/registro_alteracoes_%s_resumo.md' % cfg.TAG),
            ('out/estudante/ (35 .md)', 'saida/estudante/')]


def h(p):
    b = open(p, 'rb').read()
    return hashlib.sha256(b).hexdigest(), len(b)


def main():
    L = []; w = L.append
    final = cfg.FINAL
    st = json.load(open(os.path.join(OUT, 'stats_%s.json' % cfg.TAG), encoding='utf-8'))
    P = json.load(open(os.path.join(OUT, 'pacote.json'), encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
    E = json.load(open(os.path.join(OUT, 'pacote_estudante.json'), encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
    mdj = json.load(open(os.path.join(OUT, 'estudante_md_%s.json' % cfg.TAG), encoding='utf-8'))
    w('# MANIFESTO — T-115 — gerador v%s do pacote.json, do pacote_estudante.json e da edição .md (%s) — %s — gerado por gbq-csc (manifesto_%s.py)' % (cfg.VERSAO, 'GERAÇÃO FINAL' if final else 'ENSAIO', cfg.GERADO_EM, cfg.TAG))
    w('')
    w('Origem: cópia de `saida/pacote/%s/` (intacta; nenhum byte mudou — conferência C-G1), sem `out/`, `__pycache__/` e `ensaio/`, mais as mudanças da D1 da GBQ (`%s`). '
      'Base do pacote: o pacote.json v1.11 canônico (D-PACOTE-V111), lido do blob do commit `%s` (SHA-256 `%s`, %d itens). '
      'Mudam só: os %d itens novos (onda 4 do reforço, onda 1 da ORDEM_V15_F P1 e P2) com as 3 erratas de enunciado e a limpeza L-1 a L-5 (campo `interno`), as %d pegadinhas de pares, `topicos` (%d resumos, %d pilotos), '
      'os nomes de lote e do SIM-0 sem código de produção, a `legendaMecanismo` não emitida, `nome` e `geradoEm`.' % (
          cfg.GERADOR_ANTERIOR, cfg.D1_ARQUIVO, cfg.BASE[0], cfg.BASE[2], cfg.BASE_ITENS, st['totais']['novos'], st['totais']['pegadinhas_novas'], st['totais']['topicos'], st['totais']['pilotos']))
    w('')
    w('Modo desta execução: VERSAO=%s; geradoEm %s; FINAL=%s. %s' % (cfg.VERSAO, cfg.GERADO_EM, final, 'GERAÇÃO FINAL: nenhuma saída é promovida por este gerador (a promoção é ato separado, depois do aceite da fidelidade).' if final else
      'ENSAIO: roda tudo e grava `out/`; nenhuma saída é promovida; `saida/pacote/pacote.json` e `pacote_estudante.json` continuam a v1.11.'))
    w('')
    w('Pendências da geração final: %s.' % ('; '.join(st['pendencias']) if st['pendencias'] else 'nenhuma'))
    w('')
    w('## Pipeline (`sh rodar_tudo.sh`; cada passo com `python -I -B _run.py <script>`)')
    w('| Passo | Script | Saída |')
    w('|---|---|---|')
    for n, s, o in [(1, 'build_v112.py (com reforco_v112.py, topicos_v112.py, pegadinhas_v112.py, limpeza_v112.py)', '`out/pacote.json`, `out/stats_%s.json`, `out/folhas_%s.json`' % (cfg.TAG, cfg.TAG)),
                    (2, 'estudante_json_v112.py (com nucleo.py)', '`out/pacote_estudante.json`, `out/estudante_json.json`'),
                    (3, 'registro_adendo_v112.py', '`out/registro_adendo4.md`'),
                    (4, 'estudante_md_v112.py', '`out/estudante/` (35 arquivos), `out/estudante_md_%s.json`' % cfg.TAG),
                    (5, 'registro_alteracoes_v112.py', '`out/registro_alteracoes_%s.csv`, `_resumo.md`' % cfg.TAG),
                    (6, 'validate_v112.py', '`out/validate_%s.json`' % cfg.TAG),
                    (7, 'conferencias_v112.py', '`out/conferencias_%s.json`, `out/similaridade_%s.csv`, `out/casos_erros/`' % (cfg.TAG, cfg.TAG)),
                    (8, 'inventario_v112.py', '`out/inventario.csv`, `out/inventario.json`'),
                    (9, 'fidelidade_mutacao_v112.py', '`out/fidelidade_mutacao_%s.json` (bloco M)' % cfg.TAG),
                    (10, 'manifesto_%s.py' % cfg.TAG, 'este `MANIFESTO.md`')]:
        w('| %d | `%s` | %s |' % (n, s, o))
    w('')
    # contagens
    c = collections.Counter(i['gabarito'] for i in P['itens'])
    w('## Contagens conferidas contra os arquivos canônicos (D1, instrução 5)')
    w('- Itens: %d (%d + %d); C/E %d/%d; novos %d (onda 4 %d; F1 P1 %d; F1 P2 %d).' % (len(P['itens']), cfg.BASE_ITENS, st['totais']['novos'], c['C'], c['E'], st['totais']['novos'], st['grupos']['ONDA4']['n'], st['grupos']['F1P1']['n'], st['grupos']['F1P2']['n']))
    for gk, g in st['grupos'].items():
        w('  - %s (%s): n %d, C %d, E %d, [TS] %d, VOLÁTEIS %d, PARCIAIS %d; por folha %s.' % (gk, g['ato'], g['n'], g['C'], g['E'], g['ts'], len(g['volateis']), len(g['parciais']), g['por_folha']))
    fol = json.load(open(os.path.join(OUT, 'folhas_%s.json' % cfg.TAG), encoding='utf-8'))
    w('- Folhas que mudam (total v1.11 → v%s, C/E, diretos, PARCIAIS, VOLÁTEIS; seção 8 da D1): %s.' % (cfg.VERSAO, '; '.join(
        '%s %d→%d %d/%d %d/%d %d' % (f_, v[0], fol[f_]['total'], fol[f_]['c'], fol[f_]['e'], fol[f_]['diretos'], fol[f_]['parciais'], fol[f_]['volateis']) for f_, v in cfg.FOLHAS_V112.items())))
    p1 = json.loads(F.le_insumo('saida/gcb/T113_onda1_P1_v2.md').split('```json\n', 1)[1].split('\n```', 1)[0])
    ft = fol['P1-5.2']['total']
    w('- P1-5.2 = %d (23 da v1.11 + %d itens do bloco json de `saida/gcb/T113_onda1_P1_v2.md` em P1-5.2); a Parte 4 do arquivo diz "23 + 7 = 30".' % (ft, sum(1 for x in p1 if x['itemEdital'] == 'P1-5.2')))
    w('- VOLÁTEIS %d (%d da v1.11 + %d novos, lista de `%s`); PARCIAIS %d (88 + 6).' % (st['totais']['volatil'], st['totais']['volatil'] - st['totais']['volatil_novos'], st['totais']['volatil_novos'], cfg.T11_VOLATEIS, st['totais']['parcial']))
    w('- Pegadinhas %d por lote (v1.11 → v%s): %s.' % (st['totais']['pegadinhas'], cfg.VERSAO, '; '.join('%s %d→%d' % (k, cfg.RAIZ_PEGADINHAS[k][0], v) for k, v in st['pegadinhas_por_lote'].items())))
    w('- `topicos`: %d resumos (P1 %d, P2 %d) e %d pilotos (%s); tópicos com resumo no -E %d, com `emUmMinuto` %d, com `visuais` %d.' % (
        len(P['topicos']), sum(1 for k in P['topicos'] if k.startswith('P1-')), sum(1 for k in P['topicos'] if k.startswith('P2-')), st['totais']['pilotos'], ', '.join(cfg.PILOTOS),
        len(E['topicos']), sum(1 for t in E['topicos'].values() if 'emUmMinuto' in t), sum(1 for t in E['topicos'].values() if 'visuais' in t)))
    w('- Limpeza: %d deleções em %d itens (%s). Erratas de enunciado: %s. URL da LGPD: %d registros (fora do pacote).' % (st['delecoes'], st['itens_com_delecao'], ', '.join('%s %d' % kv for kv in sorted(st['edicoes_por_regra'].items())), ', '.join('%s (%s)' % (e['edicao'], e['item']) for e in st['erratas']), len(st['urls'])))
    rows = list(csv.DictReader(open(os.path.join(OUT, 'registro_alteracoes_%s.csv' % cfg.TAG), encoding='utf-8', newline='')))
    w('- Registro de alterações: %d linhas.' % len(rows))
    w('- Núcleo: %d itens com `nucleo` true no -E, em %d folhas.' % (sum(1 for i in E['itens'] if i['nucleo']), len({i['itemEdital'] for i in E['itens']})))
    w('- Registros do `interno`: %d no total (v1.11 799 + 53 + 10 + 1 + 6); os registros `pegadinhas[k]` do `interno` dos lotes foram reindexados (k da v1.11 → k da versão nova) por serem posicionais.' % sum(len(o.get('interno', [])) for l_ in ('itens', 'lotes', 'simulados', 'discursivas') for o in P[l_]))
    w('')
    w('## Edição .md do estudante: arquivos que mudam (%d de 35)' % len(mdj['arquivos_alterados']))
    w(', '.join('`%s`' % n for n in mdj['arquivos_alterados']) + '.')
    w('Itens novos por lote nos _itens.md e _gabarito.md: %s; tópicos renderizados: %d.' % (mdj['novos_por_lote'], mdj['topicos_renderizados']))
    w('')
    w('## Entradas X de `marcas_x_v112.py` (D1 da GBQ, T115_reconciliacao seção 5)')
    w('Confirmadas pela GBQ como conteúdo (FP), não marca de produção: X7 (ANPD "órgão da Presidência", pegadinha 32 do L3), X17 e X18 (medida F1, L3-R64), X19 (medida F1, L1-R176), X20 (tecla F4, resumo de P1-1) e X21 ("órgão da Presidência", resumo de P2-4.1). '
      'A X21, de mesma natureza da X7, passa a integrar a lista MANTER da D1, seção 3.5 (precisão de registro; nenhum dado muda; `marcas_x_v112.py` não muda).')
    w('')
    w('## Fim de linha')
    w('Todos os arquivos desta pasta, fora de `out/` e `__pycache__/`, estão em LF (conferência C-LF); a coluna "Frente ao %s" compara o conteúdo LF dos dois lados, e os SHA-256 e bytes abaixo são os do disco (iguais aos do blob depois do commit).' % cfg.GERADOR_ANTERIOR)
    w('')
    w('## Arquivos da pasta (SHA-256 e bytes, como em disco)')
    w('| Arquivo | SHA-256 | Bytes | Frente ao %s | Uso na v%s |' % (cfg.GERADOR_ANTERIOR, cfg.VERSAO))
    w('|---|---|---|---|---|')
    for f in sorted(os.listdir(HERE)):
        p = os.path.join(HERE, f)
        if not os.path.isfile(p) or f == 'MANIFESTO.md':
            continue
        s, b = h(p)
        q = os.path.join(G11, f)
        lfb = lambda x: x.replace(b'\r\n', b'\n')
        est = 'novo' if not os.path.exists(q) else ('igual' if lfb(open(q, 'rb').read()) == lfb(open(p, 'rb').read()) else 'alterado')   # compara o conteúdo LF dos dois lados
        w('| `%s` | `%s` | %d | %s | %s |' % (f, s, b, est, ATIVOS.get(f, 'herdado; só registro (não executado)')))
    w('')
    w('## out/ (regerado a cada execução; %s)' % ('fonte dos promovidos' if final else 'prévia do ensaio, nada promovido'))
    w('| Arquivo | SHA-256 | Bytes |')
    w('|---|---|---|')
    for r, ds, fs in sorted(os.walk(OUT)):
        for f in sorted(fs):
            p = os.path.join(r, f); s, b = h(p)
            w('| `out/%s` | `%s` | %d |' % (os.path.relpath(p, OUT).replace(os.sep, '/'), s, b))
    w('')
    w('## Entregáveis (fonte dos promovidos; a promoção é ato separado, depois do aceite da fidelidade; nada é promovido por este gerador)')
    w('| Saída | Destino na promoção | SHA-256 | Bytes |')
    w('|---|---|---|---|')
    for o, d in PROMOCAO:
        if o.startswith('out/estudante/'):
            for f in sorted(os.listdir(os.path.join(OUT, 'estudante'))):
                s, b = h(os.path.join(OUT, 'estudante', f))
                w('| `out/estudante/%s` | `saida/estudante/%s` | `%s` | %d |' % (f, f, s, b))
        else:
            s, b = h(os.path.join(HERE, o))
            w('| `%s` | `%s` | `%s` | %d |' % (o, d, s, b))
    vv = json.load(open(os.path.join(OUT, 'validate_%s.json' % cfg.TAG), encoding='utf-8'))
    cv = json.load(open(os.path.join(OUT, 'conferencias_%s.json' % cfg.TAG), encoding='utf-8'))
    mm = json.load(open(os.path.join(OUT, 'fidelidade_mutacao_%s.json' % cfg.TAG), encoding='utf-8'))
    w('')
    w('Resultado desta execução: validate_v112 %d/%d OK; conferencias_v112 %d OK, %d PENDENTE, %d FALHA; fidelidade_mutacao_v112 %d/%d casos (%d aplicáveis).' % (vv['ok'], vv['total'], cv['ok'], cv['pendentes'], cv['falhas'], mm['ok'], mm['total'], mm['aplicaveis']))
    open(os.path.join(HERE, 'MANIFESTO.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
    print('MANIFESTO.md: %d linhas' % len(L))


if __name__ == '__main__':
    main()
