# cobertura_v1_14.py — T-123 fase 2 (script 10) — 2026-10-23 — gerado por gbq-csc
# -*- coding: utf-8 -*-
"""Insumo da secretaria para a cobertura da v1.14 (T-95, ocorrência v1.14; D1 da GBQ, seção 9): out/cobertura_v1_14.json, com as contagens por folha (total, AUTORAL, reais, diretos, PARCIAIS, VOLÁTEIS, núcleo,
meta 20, faltam, piso de 10 diretos) de P1, P2 e DA, os itens fora de folha, as folhas de DA abaixo de 20, os parciais por folha e a conferência dos números esperados da seção 9. Fonte: out/pacote.json (campos itemEdital,
rotulo, aderencia, volatil) e out/pacote_estudante.json (campo nucleo). As 37 folhas de DA são conferidas contra edital/DA_itens_1_12_P1.md. O JSON traz também o mesmo cálculo sobre a v1.13 para a comparação de P1 e P2.
O texto cobertura_v1_14.md é da secretaria. Uso: python -I cobertura_v1_14.py (exit 1 se alguma conferência FALHAR). Não lê relógio."""
import sys
sys.dont_write_bytecode = True
import collections, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import montar_v1_14 as M

CRIT = []


def chk(cid, desc, esperado, obtido):
    ok = esperado == obtido
    CRIT.append(dict(id=cid, criterio=desc, esperado=esperado, obtido=obtido, resultado='OK' if ok else 'FALHA'))
    print(('OK    ' if ok else 'FALHA ') + cid + ' — ' + desc + ('' if ok else '  [esperado=%r obtido=%r]' % (esperado, obtido)))


def calcula(pac, est):
    items = pac['itens']; nuc = {i['id']: bool(i.get('nucleo')) for i in est['itens']}
    assert [i['id'] for i in items] == [i['id'] for i in est['itens']]
    ed = pac['edital']; ids = [x['id'] for x in ed]
    leaf = lambda i: not any(j != i and j.startswith(i + '.') for j in ids)
    isDA = lambda i: i.startswith('P1-DA-')
    P1 = [x['id'] for x in ed if x['prova'] == 'P1' and not isDA(x['id']) and leaf(x['id'])]
    P2 = [x['id'] for x in ed if x['prova'] == 'P2' and leaf(x['id'])]
    DA = [x['id'] for x in ed if isDA(x['id']) and leaf(x['id'])]
    by = collections.defaultdict(list)
    for it in items:
        by[it['itemEdital']].append(it)

    def row(f):
        L = by.get(f, []); t = len(L)
        a = sum(i['rotulo'] == 'AUTORAL' for i in L); r = sum(i['rotulo'] == 'CEBRASPE_ANALOGA' for i in L)
        d = sum(i['aderencia'] == 'direta' for i in L); pa = sum(i['aderencia'] == 'parcial' for i in L)
        v = sum(bool(i.get('volatil')) for i in L); n = sum(nuc[i['id']] for i in L)
        assert a + r == t and d + pa == t
        return dict(folha=f, total=t, autoral=a, reais=r, diretos=d, parciais=pa, volateis=v, nucleo=n, meta20=t >= 20, faltam=max(0, 20 - t), piso10_diretos=d >= 10)
    rows = dict(P1=[row(f) for f in P1], P2=[row(f) for f in P2], DA=[row(f) for f in DA])
    folhas = set(P1) | set(P2) | set(DA)
    fora = [i for i in items if i['itemEdital'] not in folhas]
    return dict(items=items, rows=rows, fora=fora, folhas=folhas, edital_ids=ids)


def soma(rs):
    return {k: sum(r[k] for r in rs) for k in ('total', 'autoral', 'reais', 'diretos', 'parciais', 'volateis', 'nucleo')}


def main():
    pac = json.loads(open(os.path.join(M.OUT, 'pacote.json'), 'rb').read().decode('utf-8'))
    est = json.loads(open(os.path.join(M.OUT, 'pacote_estudante.json'), 'rb').read().decode('utf-8'))
    ins = M.ler_insumos()
    c14 = calcula(pac, est)
    c13 = calcula(json.loads(ins['base_pacote'].decode('utf-8')), json.loads(ins['base_estudante'].decode('utf-8')))
    rows = c14['rows']; items = c14['items']
    # --- as 37 folhas de DA contra edital/DA_itens_1_12_P1.md (D-COBERTURA-AUTO-2; mesmo método da cobertura_v1_13.py)
    txt = open(os.path.join(M.R, 'edital', 'DA_itens_1_12_P1.md'), 'rb').read().replace(b'\r\n', b'\n').decode('utf-8').split('\n')
    body = [l for l in txt if l and not l.startswith('#') and not l.startswith('Disciplina') and not l.startswith('Fonte')][0]
    nums = re.findall(r'(?:(?<=^)|(?<=\. ))(\d{1,2}(?:\.\d{1,2})?) (?=[A-ZÀ-Ú])', body)
    fileleaf = [n for n in nums if not any(m != n and m.startswith(n + '.') for m in nums)]
    da_folhas = [r['folha'] for r in rows['DA']]
    chk('F0', 'as folhas de DA do pacote = as entradas sem subitens de edital/DA_itens_1_12_P1.md', sorted('P1-DA-' + n for n in fileleaf), sorted(da_folhas))
    tot = len(items)
    chk('F1', 'folhas: P1, P2, DA e total', [15, 23, 37, 75], [len(rows['P1']), len(rows['P2']), len(rows['DA']), len(c14['folhas'])])
    chk('F2', 'itens no pacote', 1433, tot)
    ce = collections.Counter(i['gabarito'] for i in items)
    chk('F2c', 'C/E no pacote', [730, 703], [ce['C'], ce['E']])
    sd = soma(rows['DA'])
    da_fora = [i for i in c14['fora'] if i['itemEdital'].startswith('P1-DA-')]
    fora_por = collections.Counter(i['itemEdital'] for i in da_fora)
    chk('F3', 'DA: itens em folha / fora de folha', [644, 40], [sd['total'], len(da_fora)])
    chk('F3b', 'DA fora de folha por entrada (P1-DA-1 12, 2 3, 3 5, 4 4, 5 3, 6 1, 8 7, 9 1, 10 4)', {'P1-DA-1': 12, 'P1-DA-2': 3, 'P1-DA-3': 5, 'P1-DA-4': 4, 'P1-DA-5': 3, 'P1-DA-6': 1, 'P1-DA-8': 7, 'P1-DA-9': 1, 'P1-DA-10': 4}, dict(fora_por))
    ge20 = [r['folha'] for r in rows['DA'] if r['total'] >= 20]; lt20 = {r['folha']: r['total'] for r in rows['DA'] if r['total'] < 20}
    chk('F4', 'DA: folhas com 20 ou mais / abaixo de 20', [25, 12], [len(ge20), len(lt20)])
    chk('F4b', 'DA abaixo de 20: 1.1 e 1.2 com 11; 9.2, 9.3, 9.4 e 10.1 a 10.7 com 10', {'P1-DA-1.1': 11, 'P1-DA-1.2': 11, 'P1-DA-9.2': 10, 'P1-DA-9.3': 10, 'P1-DA-9.4': 10, **{'P1-DA-10.%d' % k: 10 for k in range(1, 8)}}, lt20)
    chk('F5', 'DA: reais (banco P1-DA) e VOLÁTEIS (nas folhas e no pacote)', [36, 5, 5], [sum(1 for i in items if i['itemEdital'].startswith('P1-DA-') and i['rotulo'] != 'AUTORAL'), sum(bool(i.get('volatil')) for i in items if i['itemEdital'].startswith('P1-DA-')), sd['volateis']])
    par = {r['folha']: r['parciais'] for r in rows['DA'] if r['parciais']}
    chk('F6', 'DA: parciais 35, por folha 5.2 4, 6.1 8, 6.2 5, 6.3 8, 6.4 6, 6.5 3 e 8.3 1', [35, {'P1-DA-5.2': 4, 'P1-DA-6.1': 8, 'P1-DA-6.2': 5, 'P1-DA-6.3': 8, 'P1-DA-6.4': 6, 'P1-DA-6.5': 3, 'P1-DA-8.3': 1}], [sd['parciais'] + sum(1 for i in da_fora if i['aderencia'] == 'parcial'), par])
    chk('F7', 'DA: 684 itens (644 em folha + 40 fora), AUTORAL 648', [684, 648], [sd['total'] + len(da_fora), sum(1 for i in items if i['itemEdital'].startswith('P1-DA-') and i['rotulo'] == 'AUTORAL')])
    chk('F8', 'P1 (TI) e P2: linhas iguais às da v1.13 (sem mudança)', [], [r['folha'] for k in ('P1', 'P2') for r, o in zip(rows[k], c13['rows'][k]) if r != o])
    chk('F9', 'itens fora de folha: 13 de P1/P2 (mesmos da v1.12/v1.13) + 40 de DA', [53, 13, 40], [len(c14['fora']), len(c14['fora']) - len(da_fora), len(da_fora)])
    chk('F10', 'em folha + fora = total', tot, sum(soma(rows[k])['total'] for k in rows) + len(c14['fora']))
    dord = sorted(rows['DA'], key=lambda r: (r['total'], [int(x) for x in re.findall(r'\d+', r['folha'].replace('P1-DA', ''))]))
    rel = collections.OrderedDict(
        tarefa='T-123 (D1 da GBQ, seção 9; insumo da secretaria para cobertura_v1_14.md)', script='saida/pacote/montagem_v1_14/cobertura_v1_14.py',
        fontes=dict(pacote='out/pacote.json', estudante='out/pacote_estudante.json', geradoEm=pac['geradoEm'], itens=tot),
        totais=dict(itens=tot, C=ce['C'], E=ce['E'], em_folha=sum(soma(rows[k])['total'] for k in rows), fora_de_folha=len(c14['fora']), por_materia_em_folha={k: soma(rows[k]) for k in rows}),
        folhas={k: rows[k] for k in rows},
        fora_de_folha=dict(P1_P2=sorted(i['id'] for i in c14['fora'] if not i['itemEdital'].startswith('P1-DA-')), DA_por_entrada=dict(fora_por),
                           DA_ids_por_entrada={k: sorted(i['id'] for i in da_fora if i['itemEdital'] == k) for k in sorted(fora_por, key=lambda s: int(s.split('-')[-1]))}),
        da_abaixo_de_20=[dict(folha=r['folha'], total=r['total'], faltam=r['faltam']) for r in dord if r['total'] < 20],
        da_com_20_ou_mais=[dict(folha=r['folha'], total=r['total']) for r in rows['DA'] if r['total'] >= 20],
        da_ordem_da_mais_rala_a_mais_cheia=[dict(folha=r['folha'], total=r['total'], faltam=r['faltam'], diretos=r['diretos'], volateis=r['volateis'], nucleo=r['nucleo']) for r in dord],
        da_falta_para_20=sum(r['faltam'] for r in rows['DA']), parciais_da_por_folha=par,
        comparacao_v1_13=dict(P1_P2_linhas_iguais=True, da_v1_13=soma(c13['rows']['DA']), da_fora_v1_13=len([i for i in c13['fora'] if i['itemEdital'].startswith('P1-DA-')])),
        ressalva_d='A coluna "Onda programada" de P1 (ressalva (d) da cobertura_v1_13.md) não é calculável pelo pacote: vem de TAREFAS.md e é reconstruída pela secretaria nesta ocorrência.',
        criterios=CRIT)
    M.grava(os.path.join(M.OUT, 'cobertura_v1_14.json'), (json.dumps(rel, ensure_ascii=False, indent=1) + '\n').encode('utf-8'))
    nf = sum(c['resultado'] == 'FALHA' for c in CRIT)
    print('cobertura_v1_14.json: %d conferências, %d FALHA' % (len(CRIT), nf))
    sys.exit(1 if nf else 0)


if __name__ == '__main__':
    main()
