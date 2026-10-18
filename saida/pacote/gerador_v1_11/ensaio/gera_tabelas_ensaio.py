# -*- coding: utf-8 -*-
"""T-108 (gerador_v1_11) — montador das tabelas de ENSAIO. Só roda em ENSAIO e só grava nesta pasta (ensaio/).
As tabelas das Gerências estão em produção (podem não existir ou estar incompletas). Este script:
  1. lê as tabelas em produção que existirem (config_v111.TABELAS_PRODUCAO), linha a linha, em modo tolerante, e guarda as linhas que passam em todas as conferências do gerador
     (formas, antes único, casamentos no intervalo, sem sobreposição, FP intactos, proibições do depois, "verificado em" e base legal);
  2. grava a tabela da GBQ com as 4 linhas da seção 1.9 da D1;
  3. para cada id do universo (872) que ficou sem linha, cria uma linha SINTÉTICA de ensaio (prefixos GCE-9nnn e GCB-C9nnn): janela única de texto em torno do casamento, com o
     casamento retirado (SUBSTITUIR/DELETAR) ou, para VERIFICAR, linha MANTER; não é conteúdo aprovado, serve só para exercitar o gerador de ponta a ponta;
  4. grava ensaio/relatorio_ensaio.json (o que cada tabela de produção trouxe, o que foi aceito e o que foi recusado, com o motivo) e ensaio/excecoes_ensaio.json.
Determinístico (sem relógio, sem aleatoriedade)."""
import collections, csv, io, json, os, subprocess, sys
import config_v111 as cfg
import tabelas_v111 as T
import limpeza_v111 as L
import inventario_v111 as I
import refs
from common import HERE, P as PATH

ENS = os.path.join(HERE, 'ensaio')
COLS = ['id_edicao', 'ids_ocorrencia', 'caminho', 'lote', 'categoria', 'antes', 'depois', 'acao', 'regra', 'fonte_origem', 'nota']

GBQ_LINHAS = [
    ('GBQ-0001', 'D-C08-b44a9812', 'itens[BQ-0003].nota', '8', 'C08', ' (D-LEI-15352)', '', 'DELETAR', '5', '', 'Igual ao NOTA_DEL do -E v1.10. A denominação, a lei e o artigo ficam.'),
    ('GBQ-0002', 'D-C08-894022ae', 'simulados[SIM-0].avisos[0]', 'SIMULADO', 'C08', '(D-ADERENCIA: parcial só em diagnóstico)', '(parcial só em diagnóstico)', 'SUBSTITUIR', '5', '', 'Só deleção de "D-ADERENCIA: ", igual ao AVISO do -E v1.10.'),
    ('GBQ-0003', 'D-C10-a5ba3541', 'simulados[SIM-0].avisos[0]', 'SIMULADO', 'C10', '4 itens VOLÁTEIS (inaptos', '4 itens (inaptos', 'SUBSTITUIR', '5', '', 'Só deleção do rótulo. O motivo ("inaptos a simulado final até a reverificação") fica.'),
    ('GBQ-0004', 'D-C10-8984f5b2', 'simulados[SIM-0].avisos[2]', 'SIMULADO', 'C10', 'nenhum item aprovado foi removido para equilibrar', '', 'MANTER', '5', '', 'Conteúdo à candidata sobre o equilíbrio C/E. Não é instrução interna.'),
]


def escreve(nome, rows):
    buf = io.StringIO(newline='')
    w = csv.writer(buf, quoting=csv.QUOTE_ALL, lineterminator='\n')
    w.writerow(COLS)
    for r in rows:
        w.writerow([r.get(c, '') for c in COLS])
    with open(os.path.join(ENS, nome), 'w', encoding='utf-8', newline='') as fh:
        fh.write(buf.getvalue())


def main():
    assert cfg.ENSAIO and not cfg.FINAL, 'gera_tabelas_ensaio só roda em ENSAIO'
    os.makedirs(ENS, exist_ok=True)
    raw = refs.git_show(cfg.BASE[0], cfg.BASE[1])
    P = json.loads(raw.decode('utf-8'), object_pairs_hook=collections.OrderedDict)
    inv_l = I.varre(P, 'D')
    inv = {o['id_ocorrencia']: o for o in inv_l}
    oc = T.le_ocorrencias(T.le_bytes(cfg.OCORRENCIAS[0]))
    universo = {i for i, o in oc.items() if o['classe'] in ('PROCESSO', 'VERIFICAR')}
    rel = collections.OrderedDict(producao=[], gbq='4 linhas da seção 1.9 da D1 (tabela ainda não gravada em saida/pacote/ pela gbq-csc)')
    # 1. tabelas em produção
    reais = []
    for ger, cam in cfg.TABELAS_PRODUCAO:
        if not os.path.exists(PATH(cam)):
            rel['producao'].append(dict(arquivo=cam, existe=False)); continue
        errs = []
        rr = T.le_csv(T.le_bytes(cam), cam, ger, cfg.PREFIXOS[ger], errs)
        n_total = len(rr) + len(errs)
        reais += rr
        rel['producao'].append(dict(arquivo=cam, existe=True, sha256=T.sha256_bytes(T.le_bytes(cam)), linhas=n_total, recusadas_na_forma=len(errs), erros_forma=errs))
    gbq = [dict(zip(COLS, g), _ids=g[1].split(';'), _ger='GBQ', _tabela='ensaio') for g in GBQ_LINHAS]
    todas = reais + gbq
    # identidade e Gerência de cada id contra o inventário (descarta a linha inteira que cita id fora do universo, FP ou de outra Gerência/caminho)
    boas = []
    rec = collections.OrderedDict()
    usados = {}
    for r in todas:
        mot = None
        for i in r['_ids']:
            o = oc.get(i)
            if o is None or o['classe'] not in ('PROCESSO', 'VERIFICAR'):
                mot = 'id %s fora do universo (inexistente ou FP)' % i; break
            if o['caminho'] != r['caminho'] or o['gerencia'] != r['_ger']:
                mot = 'id %s é de %s/%s' % (i, o['gerencia'], o['caminho']); break
            if i in usados:
                mot = 'id %s já usado em %s' % (i, usados[i]); break
        if mot:
            rec[r['id_edicao']] = 'C-2: ' + mot
            continue
        for i in r['_ids']:
            usados[i] = r['id_edicao']
        boas.append(r)
    P2, res = L.aplica(P, boas, inv, cfg.EXCECOES_DEPOIS, tolerante=True)
    aceitas = {l['id_edicao'] for l in res['linhas']}
    for rid, msg in res['descartadas']:
        rec[rid] = msg
    aceitas_rows = [r for r in boas if r['id_edicao'] in aceitas]
    rel['aceitas_por_tabela'] = dict(collections.Counter(r['_tabela'] for r in aceitas_rows))
    rel['recusadas'] = len(rec)
    rel['motivos_recusa'] = dict(collections.Counter(m.split(':', 2)[0] + ':' + (m.split(':', 2)[2].split(' em ')[0][:60] if m.count(':') >= 2 else '') for m in rec.values()).most_common())
    rel['recusadas_ids'] = rec
    # 2/3. ids sem linha -> linhas sintéticas
    cobertos = {i for r in aceitas_rows for i in r['_ids']}
    faltam = sorted(universo - cobertos)
    sint, lacunas = [], []
    por_campo = collections.OrderedDict()
    for i in faltam:
        por_campo.setdefault(oc[i]['caminho'], []).append(i)
    n_ger = collections.Counter()
    for cam, ids in por_campo.items():
        obj, rl, cont, chave = T.resolve(P, cam)
        texto = cont[chave]
        # obstáculos: linhas aceitas do campo
        ocupados = [(r['_i'], r['_j']) for r in aceitas_rows if r['caminho'] == cam]
        alvos = sorted([(inv[i]['_a'], inv[i]['_b'], i, inv[i]['classe']) for i in ids])
        fps = [(o['_a'], o['_b']) for o in inv_l if o['caminho'] == cam and o['classe'] in ('FP-R1', 'FP-CONTEUDO')]
        feitos = set()
        for (a0, b0, i0, c0) in alvos:
            if i0 in feitos:
                continue
            l, r_, grupo = a0, b0, [(a0, b0, i0, c0)]
            feitos.add(i0)
            bloq = {'e': False, 'd': False}
            lado = 'e'
            falhou = False
            while True:
                win = texto[l:r_]
                if len(L._acha(texto, win)) == 1:
                    # janela única; exige que o grupo contenha só PROCESSO (VERIFICAR vira MANTER à parte)
                    break
                if bloq['e'] and bloq['d']:
                    falhou = True; break
                lado = 'd' if lado == 'e' else 'e'
                if bloq[lado]:
                    continue
                pos = l - 1 if lado == 'e' else r_
                if pos < 0 or pos >= len(texto):
                    bloq[lado] = True; continue
                tocado = None
                for (oa, ob) in ocupados:
                    if oa <= pos < ob:
                        tocado = ('ocupado', oa, ob)
                for (fa, fb) in fps:
                    if fa <= pos < fb and tocado is None:
                        tocado = ('fp', fa, fb)
                for (a, b, i, c) in alvos:
                    if a <= pos < b and i not in [g[2] for g in grupo] and tocado is None:
                        tocado = ('alvo', a, b, i, c)
                if tocado is None:
                    if lado == 'e': l -= 1
                    else: r_ += 1
                elif tocado[0] == 'ocupado':
                    bloq[lado] = True
                elif tocado[0] == 'fp':
                    l = min(l, tocado[1]); r_ = max(r_, tocado[2])
                else:
                    _, a, b, i, c = tocado
                    if c == 'VERIFICAR' or c0 == 'VERIFICAR':
                        bloq[lado] = True
                    else:
                        l = min(l, a); r_ = max(r_, b); grupo.append((a, b, i, c)); feitos.add(i)
            if falhou:
                lacunas.append((cam, i0)); continue
            for (a, b, i, c) in alvos:
                if l <= a and b <= r_ and i not in [g[2] for g in grupo] and c == 'PROCESSO' and c0 == 'PROCESSO':
                    grupo.append((a, b, i, c)); feitos.add(i)
            ocupados.append((l, r_))
            antes = texto[l:r_]
            dep = antes
            for (a, b, i, c) in sorted(grupo, reverse=True):
                dep = dep[:a - l] + dep[b - l:]
            ger = oc[i0]['gerencia']
            n_ger[ger] += 1
            rid = ('GCE-9%03d' if ger == 'GCE' else 'GCB-C9%03d' if ger == 'GCB' else 'GBQ-9%03d') % n_ger[ger]
            cat = ';'.join(sorted({oc[g[2]]['categoria'] for g in grupo}))
            if c0 == 'VERIFICAR':
                row = dict(id_edicao=rid, ids_ocorrencia=';'.join(g[2] for g in grupo), caminho=cam, lote=oc[i0]['lote'], categoria=cat, antes=antes, depois='', acao='MANTER', regra='5',
                           fonte_origem='', nota='ENSAIO: MANTER sintético (VERIFICAR)')
            else:
                row = dict(id_edicao=rid, ids_ocorrencia=';'.join(g[2] for g in grupo), caminho=cam, lote=oc[i0]['lote'], categoria=cat, antes=antes, depois=dep,
                           acao='DELETAR' if dep == '' else 'SUBSTITUIR', regra='5', fonte_origem='', nota='ENSAIO: linha sintética (casamento retirado da janela única)')
            row['_ger'] = ger; row['_ids'] = [g[2] for g in grupo]; row['_tabela'] = 'sintetica'
            sint.append(row)
    # revalida as sintéticas (tolerante) e registra exceções do depois, se preciso
    excecoes = {}
    for _ in range(2):
        P3, res3 = L.aplica(P, aceitas_rows + sint, inv, excecoes, tolerante=True)
        ruins = {rid: msg for rid, msg in res3['descartadas']}
        if not ruins:
            break
        for r in sint:
            msg = ruins.get(r['id_edicao'])
            if msg and 'proibição no depois' in msg:
                import re as _re
                import limpeza_v111 as LL
                lits = set()
                for nome, rx in LL.PROIBICOES:
                    for m in rx.finditer(r['depois']):
                        lits.add(_re.escape(m.group(0)))
                excecoes[r['id_edicao']] = sorted(lits)
    rel['sinteticas'] = dict(linhas=len(sint), por_gerencia=dict(n_ger), lacunas=lacunas, excecoes_depois_ensaio=len(excecoes), nao_resolvidas=sorted(ruins))
    # 4. grava
    ger_rows = {'GCE': [], 'GCB': [], 'GBQ': []}
    for r in aceitas_rows + sint:
        ger_rows[r['_ger']].append(r)
    ordem = lambda r: (r['id_edicao'][:5] if r['_ger'] == 'GCB' else '', r['id_edicao'])
    for g in ger_rows:
        ger_rows[g].sort(key=lambda r: r['id_edicao'])
        escreve('T108_substituicoes_%s_ensaio.csv' % g, ger_rows[g])
    with open(os.path.join(ENS, 'excecoes_ensaio.json'), 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(excecoes, fh, ensure_ascii=False, indent=1, sort_keys=True); fh.write('\n')
    with open(os.path.join(ENS, 'relatorio_ensaio.json'), 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(rel, fh, ensure_ascii=False, indent=1); fh.write('\n')
    print('ensaio: linhas reais aceitas %s; recusadas %d; sintéticas %d (lacunas %d; exceções do depois %d)' % (rel['aceitas_por_tabela'], len(rec), len(sint), len(lacunas), len(excecoes)))
    print('universo %d; cobertos por real %d; sintéticos cobrem %d' % (len(universo), len(cobertos), sum(len(r['_ids']) for r in sint)))
    sys.exit(0 if not lacunas and not ruins else 1)


if __name__ == '__main__':
    main()
