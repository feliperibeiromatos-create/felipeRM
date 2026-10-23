# mutacao_t123.py — T-123 fase 2 (script 5; passo 7) — 2026-10-23 — gerado por gbq-csc
# -*- coding: utf-8 -*-
"""Teste de mutação da conferência (D1 da GBQ, seção 8.3): 15 mutações em memória (ou em cópia no diretório temporário), cada uma tem de dar FALHA no critério indicado; o original tem de dar 0 FALHA.
M1-M3, M5-M12: mutam o pacote.json/pacote_estudante.json lidos e chamam conferir_t123.executa(ctx, fs=False). M4: extrator rodado em cópia da raiz com a AJ-E1 duplicada (esperado: aborto, exit 2). M13: leva lida
com CRLF sem normalizar (C-SHA). M14: substituição da GCB com `antes` ausente (aborto do montar). M15: linha de ato deslocada em cópia de DECISOES.md (aborto do nucleo). Grava out/mutacao_t123.json.
Uso: python -I mutacao_t123.py [pasta temporária]. exit 0 só com 15/15 detectadas e o original com 0 FALHA. Não lê relógio."""
import sys
sys.dont_write_bytecode = True
import collections, copy, json, os, shutil, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import montar_v1_14 as M
import nucleo_v114 as NU
import conferir_t123 as C

R = M.R


def falhas(crit):
    return [c['id'] for c in crit if c['resultado'] == 'FALHA']


def novo_ctx(base):
    c = dict(base)
    c['pac'] = copy.deepcopy(base['pac']); c['est'] = copy.deepcopy(base['est'])
    return c


def fecha(c):
    c['pac_b'] = M.dumps(c['pac']); c['est_b'] = M.dumps(c['est'])
    return c


def item(c, iid, quem='pac'):
    return next(i for i in c[quem]['itens'] if i['id'] == iid)


def main():
    tmp_pai = sys.argv[1] if len(sys.argv) > 1 else tempfile.gettempdir()
    base = C.carregar_ctx()
    orig = C.executa(base, fs=False)
    res = []

    def reg(mid, desc, esperado, detectado, falharam, extra=None):
        d = collections.OrderedDict(id=mid, mutacao=desc, criterio_esperado=esperado, detectada=bool(detectado), criterios_com_falha=falharam)
        if extra: d['detalhe'] = extra
        res.append(d)
        print('%s %s — %s [%s]%s' % ('DETECTADA' if detectado else 'NAO DETECTADA', mid, desc, esperado, ('' if not falharam else ' -> ' + ', '.join(falharam[:6]))))

    def roda(mid, desc, esperado, mut):
        c = novo_ctx(base); mut(c); fecha(c)
        f = falhas(C.executa(c, fs=False))
        reg(mid, desc, esperado, any(x.startswith(g.strip()) for x in f for g in esperado.split(' / ')), f)

    def m1(c):
        for q in ('pac', 'est'):
            i = item(c, 'D1-R01', q); i['gabarito'] = 'E' if i['gabarito'] == 'C' else 'C'

    def m2(c):
        for q in ('pac', 'est'):
            item(c, 'D2-R10', q)['enunciado'] += 'x'

    def m3(c):
        for q in ('pac', 'est'):
            i = item(c, 'D3-R13', q); e = M.ERRATAS[0]
            assert i['enunciado'].count(e[4]) == 1
            i['enunciado'] = i['enunciado'].replace(e[4], e[3])

    def m5(c):
        for q in ('pac', 'est'):
            lst = c[q]['itens']; k = next(n for n, i in enumerate(lst) if i['id'] == 'D1-R02')
            novo = copy.deepcopy(lst[k]); novo['id'] = 'D1-R03'; novo['numero'] = 3
            lst.insert(k + 1, novo)

    def m6(c):
        for q in ('pac', 'est'):
            i = item(c, 'D3-R01', q); assert i['aderencia'] == 'parcial'; i['aderencia'] = 'direta'

    def m7(c):
        for q in ('pac', 'est'):
            i = item(c, 'D2-R05', q); i['justificativa'] = i['justificativa'] + ' R37'

    def m8(c):
        rows = {d['id']: d for d in c['banco']}
        novo = M.item_banco(rows['BQ-0141'])
        k = max(n for n, i in enumerate(c['pac']['itens']) if i['id'].startswith('BQ-'))
        c['pac']['itens'].insert(k + 1, novo)
        e = copy.deepcopy(novo); e['nucleo'] = False
        c['est']['itens'].insert(k + 1, e)

    def m9(c):
        for q in ('pac', 'est'):
            item(c, 'BQ-0113', q)['comando'] = item(c, 'BQ-0113', q)['comando'] + ' (alterado)'

    def m10(c):
        i = item(c, 'D5-01', 'est'); i['nucleo'] = not i['nucleo']

    def m11(c):
        item(c, 'D4-R01', 'est')['url'] = 'saida/gcb/DA_reforco_leva1_v2.md'

    def m12(c):
        item(c, 'D1-01', 'pac')['enunciado'] += 'x'

    def m13(c):
        ins = dict(c['ins']); ins['leva3'] = ins['leva3'].replace(b'\n', b'\r\n'); c['ins'] = ins
    roda('M1', 'gabarito de um item de reforço (D1-R01) invertido', 'C-REFORCO', m1)
    roda('M2', '1 caractere a mais no enunciado de um item de reforço (D2-R10)', 'C-REFORCO', m2)
    roda('M3', 'D3-R13 com o "antes" da AJ-E1', 'C-REFORCO', m3)
    # M4: extrator em cópia da raiz com a AJ-E1 duplicada
    raiz = tempfile.mkdtemp(prefix='mut_m4_', dir=tmp_pai)
    try:
        ins = base['ins']
        os.makedirs(os.path.join(raiz, 'banco')); os.makedirs(os.path.join(raiz, 'saida', 'gcb'))
        for nome, rel in (('banco', 'banco/banco.csv'),):
            open(os.path.join(raiz, rel), 'wb').write(ins[nome])
        for n in range(1, 9):
            b = ins['leva%d' % n]
            if n == 1:
                b = b + ('\n' + M.ERRATAS[0][3] + '\n').encode('utf-8')          # o "antes" passa a ocorrer 2 vezes no arquivo
            open(os.path.join(raiz, 'saida', 'gcb', 'DA_reforco_leva%d_v2.md' % n), 'wb').write(b)
        dec = ins['dec'].decode('utf-8')
        sl = M.shas_levas(dec)
        novo_sha = M.sha(open(os.path.join(raiz, 'saida', 'gcb', 'DA_reforco_leva1_v2.md'), 'rb').read())
        dec2 = dec.replace(sl[1], novo_sha)
        assert dec2 != dec
        open(os.path.join(raiz, 'DECISOES.md'), 'wb').write(dec2.encode('utf-8'))
        saida = os.path.join(raiz, 'montagem_v1_14'); os.makedirs(saida)
        ext = os.path.join(HERE, 'extrair_reforco_da.py')
        p = subprocess.run([sys.executable, '-I', ext, raiz, saida], capture_output=True)
        err = p.stderr.decode('utf-8', 'replace')
        reg('M4', 'AJ-E1 aplicada a uma cópia da leva 1 com o "antes" duplicado (SHA e DECISOES.md da cópia ajustados)', 'aborto do extrator', p.returncode == 2 and 'errata D3-R13' in err, [], 'exit %d; stderr: %s' % (p.returncode, err.strip()[:160]))
    finally:
        shutil.rmtree(raiz, ignore_errors=True)
    roda('M5', 'D1-R03 inserido (cópia do D1-R02 com o id vago)', 'C-REFORCO / C-TOTAIS', m5)
    roda('M6', 'um parcial (D3-R01) trocado para "direta"', 'C-REFORCO', m6)
    roda('M7', '"R37" inserido numa justificativa (D2-R05)', 'C-MARCAS', m7)
    roda('M8', 'BQ-0141 incluído', 'C-BANCO', m8)
    roda('M9', 'comando de um banco P1-DA (BQ-0113) alterado', 'C-BANCO', m9)
    roda('M10', 'nucleo de um item (D5-01) trocado', 'C-ESTUDANTE', m10)
    roda('M11', 'url não vazia num item de reforço do estudante (D4-R01)', 'C-ESTUDANTE', m11)
    roda('M12', 'um item da v1.13 (D1-01) alterado', 'C-INTACTA', m12)
    roda('M13', 'leva 3 lida com CRLF sem normalizar (o SHA não confere)', 'C-SHA', m13)
    # M14 e M15: abortos do montar e do nucleo
    ins = base['ins']
    ctx14 = M.carregar(ins); ctx14['subs'] = copy.deepcopy(ctx14['subs']); ctx14['subs'][0]['antes'] = 'TEXTO_QUE_NAO_EXISTE_NA_JUSTIFICATIVA'
    try:
        M.construir(ctx14); ab = None
    except NU.Aborta as e:
        ab = str(e)
    reg('M14', 'substituição da GCB com `antes` ausente', 'aborto do montar', ab is not None and 'ocorre 0' in ab, [], ab)
    ctx15 = M.carregar(ins); ctx15['dec'] = '\n' + ctx15['dec']                # todas as linhas de ato deslocadas em 1
    try:
        M.construir(ctx15); ab = None
    except NU.Aborta as e:
        ab = str(e)
    reg('M15', 'linha de ato deslocada em cópia de DECISOES.md', 'aborto do nucleo', ab is not None and 'nucleo: ato' in ab, [], ab)
    ok = all(r['detectada'] for r in res) and len(res) == 15 and not falhas(orig)
    out = collections.OrderedDict(tarefa='T-123 (D1 da GBQ, seção 8.3)', script='saida/pacote/montagem_v1_14/mutacao_t123.py',
                                  original=dict(criterios=len(orig), FALHA=len(falhas(orig)), observacao='fs=False: os critérios que leem arquivos fora do contexto (C-INTACTA de arquivos, C-MOLDURA, C-MD, C-MANIFESTO, C-DIAG30.p1p2) ficam fora das mutações'),
                                  mutacoes=res, detectadas=sum(r['detectada'] for r in res), total=len(res))
    M.grava(os.path.join(M.OUT, 'mutacao_t123.json'), (json.dumps(out, ensure_ascii=False, indent=1) + '\n').encode('utf-8'))
    print('RESULTADO: %d/%d mutações detectadas; original com %d FALHA (%d critérios)' % (out['detectadas'], out['total'], len(falhas(orig)), len(orig)))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
