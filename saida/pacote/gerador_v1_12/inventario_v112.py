# -*- coding: utf-8 -*-
"""T-115 (gerador_v1_12, D1 da GBQ, seções 3.5 e 4: C-R e C-6) — passo 8: inventário das marcas de produção no texto que a candidata lê, com as regras do inventario_v111.py SEM mudança (módulo importado) e
a extensão ao campo `topicos` (resumo, emUmMinuto e visuais). Uso: python -I -B _run.py inventario_v112.py <pacote.json> <pacote_estudante.json> <pasta estudante/> <saida.csv> [<saida.json>]
`varre(P, arq)` = a varredura do v111 sobre os campos de antes, mais os de `topicos` (escopo 'ordem'; lote = o do tópico, pelo `itensEdital`). Somente leitura."""
import collections, csv, json, os, sys
import inventario_v111 as I

ARQS, COLUNAS = I.ARQS, I.COLUNAS


def lote_do_topico(P, k):
    c = [L['id'] for L in P['lotes'] if k in L['itensEdital']] or [L['id'] for L in P['lotes'] if any(x.startswith(k + '.') for x in L['itensEdital'])]
    return c[0] if c else 'L1'


def campos_topicos(P):
    for k, t in (P.get('topicos') or {}).items():
        lo = lote_do_topico(P, k)
        b = 'topicos[%s]' % k
        yield (lo, 'topicos', b + '.resumo', t['resumo'], 'ordem')
        for j, x in enumerate(t.get('emUmMinuto', [])):
            yield (lo, 'topicos', '%s.emUmMinuto[%d]' % (b, j), x, 'ordem')
        for j, v in enumerate(t.get('visuais', [])):
            vb = '%s.visuais[%d]' % (b, j)
            yield (lo, 'topicos', vb + '.titulo', v['titulo'], 'ordem')
            for c in ('legenda', 'centro', 'unidade', 'fonte'):
                if v.get(c):
                    yield (lo, 'topicos', '%s.%s' % (vb, c), v[c], 'ordem')
            for n, s in enumerate(v.get('passos', [])):
                yield (lo, 'topicos', '%s.passos[%d]' % (vb, n), s, 'ordem')
            for n, s in enumerate(v.get('colunas', [])):
                yield (lo, 'topicos', '%s.colunas[%d]' % (vb, n), s, 'ordem')
            for n, r in enumerate(v.get('linhas', [])):
                for m, s in enumerate(r):
                    yield (lo, 'topicos', '%s.linhas[%d][%d]' % (vb, n, m), s, 'ordem')
            for n, s in enumerate(v.get('ramos', [])):
                yield (lo, 'topicos', '%s.ramos[%d]' % (vb, n), s, 'ordem')
            for n, mc in enumerate(v.get('marcos', [])):
                yield (lo, 'topicos', '%s.marcos[%d].quando' % (vb, n), mc['quando'], 'ordem')
                yield (lo, 'topicos', '%s.marcos[%d].texto' % (vb, n), mc['texto'], 'ordem')


def varre(P, arq):
    orig = I.campos
    I.campos = lambda P_, a_: list(orig(P_, a_)) + list(campos_topicos(P_))
    try:
        return I.varre(P, arq)
    finally:
        I.campos = orig


def varre_pacote(caminho, arq):
    raw = open(caminho, 'rb').read()
    lf = raw.replace(b'\r\n', b'\n')
    P = json.loads(lf.decode('utf-8'), object_pairs_hook=collections.OrderedDict)
    import hashlib
    return P, varre(P, arq), hashlib.sha256(lf).hexdigest()


contagem = I.contagem
varre_md = I.varre_md


def main():
    pj, pe, pmd, csv_out = sys.argv[1:5]
    todos, info = [], {}
    P, oc, h = varre_pacote(pj, 'D'); info['D'] = dict(arquivo=pj, sha256_LF=h, ocorrencias=contagem(oc)); todos += oc
    E, oe, h = varre_pacote(pe, 'E'); info['E'] = dict(arquivo=pe, sha256_LF=h, ocorrencias=contagem(oe)); todos += oe
    ids_item = [i['id'] for i in P['itens']]
    om = []
    for nome in sorted(os.listdir(pmd)):
        if nome.endswith('.md') and nome != 'README.md':
            om += varre_md(nome, open(os.path.join(pmd, nome), encoding='utf-8').read(), ids_item)
    info['MD'] = dict(arquivo=pmd, ocorrencias=contagem(om)); todos += om
    with open(csv_out, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=COLUNAS, extrasaction='ignore', restval='')
        w.writeheader()
        for o in todos:
            w.writerow(o)
    if len(sys.argv) > 5:
        json.dump(info, open(sys.argv[5], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps(info, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
