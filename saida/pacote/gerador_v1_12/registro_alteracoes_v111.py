# -*- coding: utf-8 -*-
"""T-108 e T-109 (gerador_v1_11, seção 1.8 da D1) — passo 5: registro de alterações por id.
Saídas: out/registro_alteracoes_<TAG>.csv (uma linha por edição aplicada, mais a linha do L2-R16), out/registro_alteracoes_<TAG>_manter.csv (linhas MANTER, bloco à parte, com a nota) e
out/registro_alteracoes_<TAG>_resumo.md (por item, por lote e a contagem final por categoria: meta 0 PROCESSO). Asserção: o conjunto (edicao, antes, depois) do CSV é igual ao de todos os
registros `interno` do out/pacote.json. As colunas lote e categoria vêm da tabela, quando ela as traz, ou do inventário (T108_ocorrencias.csv)."""
import collections, csv, io, json, os, sys
from common import OUT
import config_v111 as cfg
import tabelas_v111 as T
import inventario_v111 as I

COLS = ['id_edicao', 'ids_ocorrencia', 'objeto', 'caminho', 'lote', 'categoria', 'acao', 'regra', 'antes', 'depois', 'fonte_origem', 'tabela', 'parecer_qa', 'aceite']


def grava(nome, linhas, cols):
    buf = io.StringIO(newline='')
    w = csv.writer(buf, quoting=csv.QUOTE_ALL, lineterminator='\n')
    w.writerow(cols)
    for l in linhas:
        w.writerow([l.get(c, '') for c in cols])
    with open(os.path.join(OUT, nome), 'w', encoding='utf-8', newline='') as fh:
        fh.write(buf.getvalue())


def qa(g):
    v = cfg.PARECER_QA.get(g)
    return ';'.join(v) if isinstance(v, list) else (v or '')


def lote_cat(r, ids, oc):
    """lote e categoria: da tabela, quando traz; senão do inventário; ids fora do inventário (IDS_EXTRA) só pela tabela (D1 pré-FINAL 1.8)."""
    no_inv = [i for i in ids if i in oc]
    lote = r.get('lote') or (oc[no_inv[0]]['lote'] if no_inv else '')
    cat = r.get('categoria') or ';'.join(sorted({oc[i]['categoria'] for i in no_inv}))
    if not lote or not cat:
        raise SystemExit('registro: %s sem lote/categoria (tabela e inventário)' % r['id_edicao'])
    return lote, cat


def main():
    P = json.load(open(os.path.join(OUT, 'pacote.json'), encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
    st = json.load(open(os.path.join(OUT, 'stats_%s.json' % cfg.TAG), encoding='utf-8'))
    tabs = [(g, c, T.le_bytes(c), h) for g, c, h in cfg.TABELAS]
    rows = {r['id_edicao']: r for r in T.carrega_de_bytes(tabs)}
    oc = T.le_ocorrencias(T.le_bytes(cfg.OCORRENCIAS[0]))
    linhas, usados = [], set()
    for lista in ('itens', 'lotes', 'simulados', 'discursivas'):
        for o in P[lista]:
            for rc in o.get('interno', []):
                r = rows[rc['edicao']]
                lote_, cat_ = lote_cat(r, rc['ocorrencias'], oc)
                linhas.append(dict(id_edicao=rc['edicao'], ids_ocorrencia=';'.join(rc['ocorrencias']), objeto=o['id'], caminho='%s[%s].%s' % (lista, o['id'], rc['campo']),
                                   lote=lote_, categoria=cat_, acao=r['acao'],
                                   regra=rc['regra'], antes=rc['antes'], depois=rc['depois'], fonte_origem=r.get('fonte_origem', ''),
                                   tabela='%s (SHA-256 %s)' % (r['_tabela'], r['_sha']), parecer_qa=qa(r['_ger']) or ('ENSAIO' if cfg.ENSAIO else ''),
                                   aceite=cfg.ACEITE.get(r['_ger']) or ('ENSAIO' if cfg.ENSAIO else '')))
                usados.add((rc['edicao'], rc['antes'], rc['depois']))
    linhas.sort(key=lambda l: l['id_edicao'])
    csv_set = {(l['id_edicao'], l['antes'], l['depois']) for l in linhas}
    assert csv_set == usados and len(csv_set) == len(linhas), 'o conjunto (edicao, antes, depois) do CSV difere do `interno`'
    n_interno = len(linhas)
    if st['l2r16']:
        linhas.append(dict(id_edicao='T109-0001', ids_ocorrencia='', objeto='L2-R16', caminho='itens[L2-R16].itemEdital', lote='2', categoria='dado (T-109)', acao='SUBSTITUIR', regra='',
                           antes=st['l2r16']['antes'], depois=st['l2r16']['depois'], fonte_origem=cfg.T109[0] + ' (seção 2)', tabela='%s (SHA-256 %s)' % (cfg.T109[0], st['t109']['sha256']),
                           parecer_qa='QA_T109_R1_2026-10-18_gce-cqfp.md', aceite=cfg.ATO_L2R16 or ('ENSAIO' if cfg.ENSAIO else '')))
    grava('registro_alteracoes_%s.csv' % cfg.TAG, linhas, COLS)
    manter = []
    for r in rows.values():
        if r['acao'] == 'MANTER':
            lote_, cat_ = lote_cat(r, r['_ids'], oc)
            manter.append(dict(id_edicao=r['id_edicao'], ids_ocorrencia=';'.join(r['_ids']), objeto=r['caminho'].split(']')[0].split('[')[1], caminho=r['caminho'], lote=lote_,
                               categoria=cat_, acao='MANTER', regra=r['regra'], antes=r['antes'], depois='', fonte_origem=r.get('fonte_origem', ''),
                               tabela='%s (SHA-256 %s)' % (r['_tabela'], r['_sha']), parecer_qa=qa(r['_ger']) or ('ENSAIO' if cfg.ENSAIO else ''),
                               aceite=cfg.ACEITE.get(r['_ger']) or ('ENSAIO' if cfg.ENSAIO else ''), nota=r.get('nota', '')))
    grava('registro_alteracoes_%s_manter.csv' % cfg.TAG, manter, COLS + ['nota'])
    # resumo
    por_item = collections.Counter(l['objeto'] for l in linhas[:n_interno] if l['caminho'].startswith('itens['))
    por_lote = collections.defaultdict(collections.Counter)
    for l in linhas[:n_interno]:
        for c in l['categoria'].split(';'):
            por_lote[l['lote']][(c, l['acao'])] += 1
    inv = I.varre(P, 'D')
    fim = collections.Counter((o['categoria'], o['classe']) for o in inv)
    L = []; w = L.append
    w('# Registro de alterações por id — v%s (%s) — gerado por registro_alteracoes_v111.py' % (cfg.VERSAO, st['modo']))
    w('')
    w('Linhas de edição aplicadas: %d (SUBSTITUIR %d, DELETAR %d); linhas MANTER: %d; mais a linha do L2-R16 (T-109): %d.' % (
        n_interno, sum(1 for l in linhas[:n_interno] if l['acao'] == 'SUBSTITUIR'), sum(1 for l in linhas[:n_interno] if l['acao'] == 'DELETAR'), len(manter), 1 if st['l2r16'] else 0))
    w('')
    w('## Por lote (edições por categoria e ação)')
    w('| Lote | Categoria | Ação | Edições |')
    w('|---|---|---|---|')
    for lote in sorted(por_lote):
        for (c, a), n in sorted(por_lote[lote].items()):
            w('| %s | %s | %s | %d |' % (lote, c, a, n))
    w('')
    w('## Por item (ids com edição e número de edições)')
    w(', '.join('%s (%d)' % kv for kv in sorted(por_item.items())))
    w('')
    w('## Contagem final por categoria, no pacote.json gerado (meta: 0 PROCESSO; restam só FP-R1, FP-CONTEUDO e os MANTER aceitos)')
    w('| Categoria | PROCESSO | VERIFICAR | FP-R1 | FP-CONTEUDO |')
    w('|---|---|---|---|---|')
    for c in sorted({k[0] for k in fim}):
        w('| %s | %d | %d | %d | %d |' % (c, fim[(c, 'PROCESSO')], fim[(c, 'VERIFICAR')], fim[(c, 'FP-R1')], fim[(c, 'FP-CONTEUDO')]))
    w('| TOTAL | %d | %d | %d | %d |' % tuple(sum(v for (c, k), v in fim.items() if k == cl) for cl in ('PROCESSO', 'VERIFICAR', 'FP-R1', 'FP-CONTEUDO')))
    w('')
    w('## Linhas da GCE com id deslocado (C-2b; EXCECAO_INTERVALO)')
    w('O id citado não está no intervalo do `antes` da linha; o casamento está na linha indicada. Texto e ação estão certos (aprovados pelo QA); só o rótulo de id está deslocado. O `interno` guarda os ids como na tabela.')
    w('| Linha | id citado fora do intervalo | Linha em cujo `antes` está o casamento |')
    w('|---|---|---|')
    for lin, alvo in sorted(cfg.EXCECAO_INTERVALO.items()):
        w('| %s | %s | %s |' % (lin, ';'.join(rows[lin]['_ids']), alvo))
    with open(os.path.join(OUT, 'registro_alteracoes_%s_resumo.md' % cfg.TAG), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('\n'.join(L) + '\n')
    print('registro de alterações: %d edições + %d (L2-R16) + %d MANTER; PROCESSO residual no pacote.json: %d' % (n_interno, 1 if st['l2r16'] else 0, len(manter), sum(v for (c, k), v in fim.items() if k == 'PROCESSO')))


if __name__ == '__main__':
    main()
