# registro_alteracoes_v114.py — T-123 fase 2 (script 6) — 2026-10-23 — gerado por gbq-csc
# -*- coding: utf-8 -*-
"""Registro de alterações por id da v1.14 (D1 da GBQ, seção 5): out/registro_alteracoes_v1_14.csv (UTF-8, LF, ";"; colunas id;tipo;campo;antes;depois;origem;ocorrencias) e out/registro_alteracoes_v1_14_resumo.md.
Tipos: entrada_reforco (238), entrada_banco (36), errata (3), formato (uma linha por substituição da GCB, 91) e nucleo_estudante (12 trocas de true para false em itens da v1.13).
Lê out/pacote.json e out/pacote_estudante.json (já montados), a base v1.13 e o CSV da GCB. Nenhum item da v1.13 muda no pacote.json. Uso: python -I registro_alteracoes_v114.py. Não lê relógio."""
import sys
sys.dont_write_bytecode = True
import collections, csv, io, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import montar_v1_14 as M
import nucleo_v114 as NU

OUT = M.OUT


def main():
    ins = M.ler_insumos()
    ctx = M.carregar(ins)
    pac = json.loads(open(os.path.join(OUT, 'pacote.json'), 'rb').read().decode('utf-8'))
    est = json.loads(open(os.path.join(OUT, 'pacote_estudante.json'), 'rb').read().decode('utf-8'))
    be = {i['id']: i for i in ctx['base_est']['itens']}
    banco = {d['id']: d for d in ctx['banco']}
    leva_de = {b['id']: b['leva'] for b in ctx['bruto']}
    linhas = NU.confere_atos(ctx['dec'])
    rows = []

    def row(iid, tipo, campo, antes, depois, origem, oc):
        rows.append([iid, tipo, campo, antes, depois, origem, str(oc)])
    for it in pac['itens']:
        iid = it['id']
        if iid in leva_de:
            ch = 'D3-R75' if iid == 'D3-R75' else 'LEVA%d' % leva_de[iid]
            ato, ln, dt = NU.TABELA[ch]
            row(iid, 'entrada_reforco', 'item', '', 'entrada no pacote (itemEdital %s; gabarito %s; aderencia %s)' % (it['itemEdital'], it['gabarito'], it['aderencia']),
                '%s; %s (linha %d de DECISOES.md; %s)' % (it['url'], ato, ln, dt), 1)
    for d in sorted(M.seleciona_banco(ctx['banco']), key=lambda d: d['id']):
        row(d['id'], 'entrada_banco', 'item', '', 'entrada no pacote (itemEdital %s; gabarito %s; aderencia %s)' % (d['item_edital_camara'], d['gabarito'], d['aderencia']),
            'banco/banco.csv (linha %d); D1 da T-123, seção 2.3' % d['_linha'], 1)
    for (iid, ato, campo, antes, depois) in M.ERRATAS:
        row(iid, 'errata', campo, antes, depois, ato + '; D1 da T-123, seção 2.2', 1)
    _just, log = M.aplica_substituicoes(ctx['bruto'], ctx['subs'])
    for g in log:
        row(g['id'], 'formato', 'justificativa', g['antes'], g['depois'],
            'saida/gcb/DA_plataforma/DA_reforco_substituicoes.csv; operacao %s; %s' % (g['operacao'], g['motivo']), g['ocorrencias'])
    flips = [i['id'] for i in ctx['base_est']['itens'] if i['nucleo'] and not next(e for e in est['itens'] if e['id'] == i['id'])['nucleo']]
    for iid in flips:
        row(iid, 'nucleo_estudante', 'nucleo', 'true', 'false', 'pacote_estudante.json; D1 da T-123, seção 6 (criterio inteiro k1 a k4)', 1)
    buf = io.StringIO(newline='')
    w = csv.writer(buf, delimiter=';', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
    w.writerow(['id', 'tipo', 'campo', 'antes', 'depois', 'origem', 'ocorrencias'])
    w.writerows(rows)
    M.grava(os.path.join(OUT, 'registro_alteracoes_v1_14.csv'), buf.getvalue().encode('utf-8'))
    por_tipo = collections.Counter(r[1] for r in rows)
    por_op = collections.Counter(g['operacao'] for g in log)
    ids_alt = len({r[0] for r in rows if r[1] in ('formato', 'errata')})
    T = ['# registro_alteracoes_v1_14_resumo.md — T-123 — 2026-10-23 — gerado por gbq-csc (registro_alteracoes_v114.py)', '',
         'Registro de alterações por id da v1.14 (D1 da T-123, seção 5). Arquivo: `out/registro_alteracoes_v1_14.csv` (UTF-8, LF, separador ";"; colunas `id;tipo;campo;antes;depois;origem;ocorrencias`). Linhas: %d.' % len(rows), '',
         '## Por tipo', '', '| Tipo | Linhas |', '|---|--:|']
    for t in ('entrada_reforco', 'entrada_banco', 'errata', 'formato', 'nucleo_estudante'):
        T.append('| %s | %d |' % (t, por_tipo[t]))
    T += ['| **Total** | **%d** |' % len(rows), '',
          '## Notas', '',
          '- `entrada_reforco`: os 238 itens D<n>-R<nn>; a origem é o arquivo da leva e o ato de aceite (linha de DECISOES.md e data).',
          '- `entrada_banco`: os 36 itens de banco P1-DA (BQ-0113 a BQ-0152, fora BQ-0131, BQ-0133, BQ-0141 e BQ-0151).',
          '- `errata`: D3-R13 (AJ-E1), D3-R18 (AJ-L2-E1) e D3-R75 (AJ-L7-E1), aplicadas na leitura das levas (o arquivo da leva não muda); a AJ-L8-E3 (D4-R42) e a AJ-L8-E4 (D4-R52) não têm aceite e não constam.',
          '- `formato`: as %d substituições da limpeza da GCB (operações: %s); %d itens de reforço têm a justificativa alterada. Enunciado, gabarito, itemEdital e aderência não mudam.' % (len(log), ', '.join('%s %d' % kv for kv in sorted(por_op.items())), len({g['id'] for g in log})),
          '- `nucleo_estudante`: %d itens da v1.13 passam de true para false no pacote do estudante: %s.' % (len(flips), ', '.join(flips)),
          '- Nenhum item da v1.13 muda no `pacote.json`.', '']
    M.grava(os.path.join(OUT, 'registro_alteracoes_v1_14_resumo.md'), ('\n'.join(T)).encode('utf-8'))
    print('registro_alteracoes_v1_14.csv: %d linhas; %s' % (len(rows), dict(por_tipo)))
    assert por_tipo == collections.Counter({'entrada_reforco': 238, 'entrada_banco': 36, 'errata': 3, 'formato': 91, 'nucleo_estudante': 12}), por_tipo


if __name__ == '__main__':
    main()
