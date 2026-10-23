# moldura_v1_14.py — T-123 fase 2 (script 9) — 2026-10-23 — gerado por gbq-csc
# -*- coding: utf-8 -*-
"""Recontagem oficial da moldura do Legislativo (D-MOLDURA-CE, (c)) sobre out/pacote.json da v1.14 (D1 da GBQ, seção 4, script 9). Aplica o critério de saida/banco/moldura_ce.py (SHA-256 LF 5723698e…ca96),
sem alteração de regra: o código do critério (de `def materia` até antes de `linhas = []`) é executado como está, sobre o pacote lido em LF (não pelo SHA fixo do script original). Confere os 238 itens de reforço
contra o campo "Moldura:" das levas e lista as divergências, sem corrigir. Totais por matéria (P1-TI, P2, P1-DA) na v1.14 e, para referência, na v1.13. Grava out/moldura_v1_14.json. Uso: python -I moldura_v1_14.py. Não lê relógio."""
import sys
sys.dont_write_bytecode = True
import collections, csv, hashlib, io, json, math, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import montar_v1_14 as M

SCRIPT = os.path.join(M.R, 'saida', 'banco', 'moldura_ce.py')
SHA_PREFIXO, SHA_SUFIXO = '5723698e', 'ca96'


def carrega_criterio():
    b = open(SCRIPT, 'rb').read().replace(b'\r\n', b'\n')
    h = hashlib.sha256(b).hexdigest()
    if not (h.startswith(SHA_PREFIXO) and h.endswith(SHA_SUFIXO)):
        raise SystemExit('moldura_ce.py: SHA-256 LF %s difere de %s…%s' % (h, SHA_PREFIXO, SHA_SUFIXO))
    src = b.decode('utf-8')
    a = src.index('def materia(ie):'); z = src.index('linhas = []')
    ns = dict(re=re, json=json, csv=csv, hashlib=hashlib, math=math, collections=collections, os=os, sys=sys)
    exec(compile(src[a:z], SCRIPT, 'exec'), ns)
    return ns['classificar'], ns['materia'], h


def tot(sel):
    n = len(sel); c = sum(1 for r in sel if r['gabarito'] == 'C'); e = n - c
    pct = 100.0 * c / n if n else 0.0
    x = -(-(2 * c - 3 * e) // 3) if 2 * c > 3 * e else 0
    return dict(itens=n, C=c, E=e, pct_C=round(pct, 1), E_faltante_para_pctC_ate_60=x)


def classifica_pacote(itens, classificar, materia):
    out = []
    for it in itens:
        mol, termo, borda, fraco = classificar(it)
        out.append(dict(id=it['id'], materia=materia(it['itemEdital']), itemEdital=it['itemEdital'], gabarito=it['gabarito'], moldura=mol, termo=termo, borda=borda, sinal_fraco=fraco))
    return out


def totais(linhas):
    S = [r for r in linhas if r['moldura'] == 'S']
    res = collections.OrderedDict()
    for m in ('P1-TI', 'P2', 'P1-DA'):
        res[m] = tot([r for r in S if r['materia'] == m])
    res['TOTAL'] = tot(S)
    univ = collections.OrderedDict()
    for m in ('P1-TI', 'P2', 'P1-DA'):
        u = [r for r in linhas if r['materia'] == m]; s = [r for r in u if r['moldura'] == 'S']
        univ[m] = dict(itens=len(u), S=len(s), pct_S=round(100.0 * len(s) / len(u), 1) if u else 0.0)
    return res, univ


def moldura_das_levas(ins):
    """{id: 'S'|'N'} do campo '- Moldura:' do bloco da seção 2 de cada leva."""
    out = {}
    for n in range(1, 9):
        cur = None
        for l in ins['leva%d' % n].decode('utf-8').split('\n'):
            m = re.match(r'^\*\*(D[1-6]-R\d{2})\*\* \(folha', l)
            if m:
                cur = m.group(1); continue
            if cur and l.startswith('- Moldura:'):
                out[cur] = l.split(':', 1)[1].strip().split(' ')[0]; cur = None      # o campo traz 'S — descrição — fecho: …' ou 'N — fecho: …'; vale a letra
    return out


def main():
    classificar, materia, h = carrega_criterio()
    ins = M.ler_insumos()
    pac = json.loads(open(os.path.join(M.OUT, 'pacote.json'), 'rb').read().decode('utf-8'))
    base = json.loads(ins['base_pacote'].decode('utf-8'))
    L14 = classifica_pacote(pac['itens'], classificar, materia)
    L13 = classifica_pacote(base['itens'], classificar, materia)
    t14, u14 = totais(L14); t13, u13 = totais(L13)
    # reforço × campo "Moldura:" das levas
    ml = moldura_das_levas(ins)
    ref = {r['id']: r for r in L14 if re.fullmatch(r'D[1-6]-R\d\d', r['id'])}
    ids_ref = [b['id'] for b in json.loads(ins['bruto'].decode('utf-8'))]
    assert sorted(ref) == sorted(ids_ref) and sorted(ml) == sorted(ids_ref), (len(ref), len(ml))
    div = [dict(id=i, moldura_na_leva=ml[i], moldura_pelo_criterio=ref[i]['moldura'], termo=ref[i]['termo'], borda=ref[i]['borda']) for i in ids_ref if ml[i] != ref[i]['moldura']]
    ref_S = [r for r in ref.values() if r['moldura'] == 'S']
    bq = [r for r in L14 if r['id'].startswith('BQ-') and r['materia'] == 'P1-DA']
    da_folhas = collections.OrderedDict()
    for f in sorted({r['itemEdital'] for r in L14 if r['materia'] == 'P1-DA'}, key=lambda s: [int(x) for x in re.findall(r'\d+', s.replace('P1-DA', ''))]):
        u = [r for r in L14 if r['itemEdital'] == f]; s = [r for r in u if r['moldura'] == 'S']
        da_folhas[f] = dict(universo=len(u), moldura_S=tot(s))
    por_borda = collections.OrderedDict()
    for b in sorted({r['borda'] for r in L14 if r['moldura'] == 'S' and r['borda']}):
        por_borda[b] = tot([r for r in L14 if r['moldura'] == 'S' and r['borda'] == b])
    por_borda['(sem borda)'] = tot([r for r in L14 if r['moldura'] == 'S' and not r['borda']])
    rel = collections.OrderedDict(
        tarefa='T-123 (D1 da GBQ, script 9; recontagem oficial da D-MOLDURA-CE, (c))', script='saida/pacote/montagem_v1_14/moldura_v1_14.py',
        criterio=dict(arquivo='saida/banco/moldura_ce.py', sha256_lf=h, regra='sem alteração; texto avaliado = comando + textoBase + enunciado'),
        pacote_lido='out/pacote.json (v1.14; lido em LF)', itens=len(L14),
        totais_por_materia_v1_14=t14, universo_por_materia_v1_14=u14, totais_por_materia_v1_13=t13, universo_por_materia_v1_13=u13,
        da_reforco_238=dict(S=len(ref_S), N=len(ref) - len(ref_S), **{'S_' + k: v for k, v in tot(ref_S).items()}),
        da_banco_36=dict(S=sum(1 for r in bq if r['moldura'] == 'S'), N=sum(1 for r in bq if r['moldura'] == 'N'), itens=len(bq)),
        divergencias_campo_moldura_das_levas=dict(n=len(div), de=len(ids_ref), itens=div, nota='listadas sem corrigir; a decisão é da gbq-gerencia na reconciliação'),
        da_por_folha_v1_14=da_folhas, S_por_borda_v1_14=por_borda)
    M.grava(os.path.join(M.OUT, 'moldura_v1_14.json'), (json.dumps(rel, ensure_ascii=False, indent=1) + '\n').encode('utf-8'))
    print('moldura_v1_14.json')
    print('v1.14 totais S por matéria:', json.dumps(t14, ensure_ascii=False))
    print('v1.13 totais S por matéria:', json.dumps(t13, ensure_ascii=False))
    print('divergências do campo Moldura: das levas: %d de %d: %s' % (len(div), len(ids_ref), [d['id'] for d in div]))


if __name__ == '__main__':
    main()
