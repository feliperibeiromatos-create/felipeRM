# -*- coding: utf-8 -*-
"""T-115 (gerador_v1_12, D1 da GBQ, seção 4: bloco M) — passo 9: testes de mutação. Cada caso altera uma CÓPIA (do pacote.json de out/, do contrato, de um insumo lido por fontes_v112.LEITOR, de DECISOES.md ou
de um arquivo da edição .md; nada do repositório é tocado) e confere que pelo menos uma conferência detecta a alteração. Controle: sem mutação, nenhuma conferência de checks_v112 falha.
Mutações herdadas da v1.11 que valem sem as tabelas da T-108 (que não existem na v1.12): `interno` adulterado (reversibilidade), número da versão fora do config (C-16), geração final sem os atos de aceite
em DECISOES.md, edição .md com o nome do lote ausente do arquivo; as demais herdadas (1 caractere de um `antes`, ids de ocorrência, sobreposição, FP em linha, BOM, \\r, coluna ausente, cobertura) são
das tabelas e ficam registradas como "não aplicável". Mais (M-a) a (M-o) da D1: trocar um gabarito novo; apagar um `volatil` novo; acrescentar `volatil` a um não VOLÁTIL; mudar `aderencia` do L3-R53; desfazer a
errata do L1-R167; reintroduzir "REVERIFICAR. " numa justificativa; mover uma pegadinha nova uma posição; trocar o `rotulo` de uma pegadinha nova; acrescentar um campo a `topicos[P2-1.4]`; mudar um caractere de
um resumo; inverter a ordem de duas chaves de `topicos`; incluir um id vago (L1-R140) ou diferido (L3-R103); pôr um item novo em SIM-2; mudar um byte do contrato fora das linhas da C-14; mudar um byte de um
insumo (falha de SHA LF). Critério: 100% detectadas. Saída: out/fidelidade_mutacao_<TAG>.json; código 1 se algum caso não for detectado."""
import collections, copy, hashlib, json, os, shutil, sys, tempfile
from common import OUT, HERE
import config_v112 as cfg
import fontes_v112 as F
from fontes_v112 import Falha
import checks_v112 as C
import build_v112 as B
import estudante_md_v112 as MD
import validate_v112 as V
import refs

RES = []


def caso(nome, esperado, fn):
    """fn() devolve a lista de conferências (id, ok, msg) ou levanta Falha. Detectada = alguma conferência falhou ou levantou Falha."""
    try:
        r = fn()
        falhas = [i for i, o, m in r if not o]
        RES.append(dict(caso=nome, esperado=esperado, detectada=bool(falhas), detectada_por=falhas, ok=bool(falhas)))
    except Falha as e:
        RES.append(dict(caso=nome, esperado=esperado, detectada=True, detectada_por=['Falha: ' + str(e)[:160]], ok=True))
    except Exception as e:
        RES.append(dict(caso=nome, esperado=esperado, detectada=True, detectada_por=['exceção %s: %s' % (type(e).__name__, str(e)[:120])], ok=False, observacao='parou por exceção não prevista'))


def main():
    ctx = C.Ctx()
    P = json.load(open(os.path.join(OUT, 'pacote.json'), encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
    ct_txt = open(C.PATH('regras/pacote_contrato.md'), 'rb').read().replace(b'\r\n', b'\n').decode('utf-8')
    n0 = cfg.BASE_ITENS

    def mut(fn):
        def f():
            Q = copy.deepcopy(P)
            fn(Q)
            return C.checa_pacote(Q, ctx)
        return f

    def item(Q, iid):
        return [i for i in Q['itens'] if i['id'] == iid][0]

    # controle
    r0 = C.checa_pacote(copy.deepcopy(P), ctx)
    RES.append(dict(caso='controle (sem mutação): nenhuma conferência de checks_v112 falha', esperado='0 falha', detectada=False, detectada_por=[i for i, o, m in r0 if not o], ok=all(o for i, o, m in r0)))

    # herdadas aplicáveis
    def h1(Q):
        o = next(i for i in Q['itens'][n0:] if i.get('interno'))
        o['interno'][0]['pos'] += 1
    caso('(herdada) `interno` com pos adulterado (reversibilidade)', 'C-L ou C-N1b ou C-5', mut(h1))

    def h2():
        d = tempfile.mkdtemp(prefix='mut_v112_')
        try:
            with open(os.path.join(d, 'x.py'), 'w', encoding='utf-8') as fh:
                fh.write('"""cabeçalho"""\nNOME = "pacote v%s"\n' % cfg.VERSAO)
            ach = V.varre_literais_versao(d)
            return [('C-16', not ach, 'literal de versão fora do config')]
        finally:
            shutil.rmtree(d, ignore_errors=True)
    caso('(herdada) literal do número da versão fora de config_v112.py', 'C-16', h2)

    def h3():
        dec = ctx.dec.replace('| D-V112-BAEF-P2-ACEITE |', '| D-X |')
        B.confere_decisoes(dec=dec)
        return [('C-1', True, '')]
    caso('(herdada) geração final sem o ato D-V112-BAEF-P2-ACEITE em DECISOES.md', 'C-1', h3)

    def h4():
        E_old = ctx.E0
        E_new = json.load(open(os.path.join(OUT, 'pacote_estudante.json'), encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
        F0 = MD.pasta_blob(cfg.BASE[0], cfg.BASE_ESTUDANTE_DIR)
        F0['L2_estudo.md'] = F0['L2_estudo.md'].replace(cfg.NOMES_LOTE['L2'][0], cfg.NOMES_LOTE['L2'][0][:20] + '#' + cfg.NOMES_LOTE['L2'][0][21:], 1)
        MD.FALHAS.clear()
        MD.gera(E_old, E_new, F0)
        return [('C-11', not MD.FALHAS, MD.FALHAS[0] if MD.FALHAS else '')]
    caso('(herdada) edição .md: nome antigo do lote sem a contagem esperada no arquivo', 'C-11', h4)
    for nm in ('1 caractere de um `antes` das tabelas', 'id de ocorrência duplicado ou fora do universo', 'sobreposição de intervalos', 'código de fonte no `depois`', 'FP em linha ou engolido por um `antes`',
               'BOM / \\r / coluna ausente / cobertura incompleta nas tabelas', 'linha do T109 ausente'):
        RES.append(dict(caso='(herdada) ' + nm, esperado='não aplicável: a versão nova não usa as tabelas da T-108', detectada=None, detectada_por=[], ok=True, nao_aplicavel=True))

    # (M-a) a (M-o)
    def ma(Q):
        i = item(Q, 'L3-R20'); i['gabarito'] = 'E' if i['gabarito'] == 'C' else 'C'
    caso('(M-a) trocar o gabarito de um item novo (L3-R20)', 'C-N1b, C-N1c, C-N2', mut(ma))

    def mb(Q):
        i = item(Q, 'L3-R12'); del i['volatil']
    caso('(M-b) apagar o `volatil` de um item novo (L3-R12)', 'C-N1b, C-V', mut(mb))

    def mc(Q):
        i = item(Q, 'L3-R20')
        assert 'volatil' not in i
        i['volatil'] = True
    caso('(M-c) acrescentar `volatil` a um item novo não VOLÁTIL (L3-R20)', 'C-N1b, C-V', mut(mc))

    def md(Q):
        item(Q, 'L3-R53')['aderencia'] = 'direta'
    caso('(M-d) mudar a `aderencia` do L3-R53 (parcial -> direta)', 'C-N1b, C-A', mut(md))

    def me(Q):
        rid, iid, antes, depois, n = [e for e in cfg.ERRATAS if e[1] == 'L1-R167'][0]
        i = item(Q, iid); i['enunciado'] = i['enunciado'].replace(depois, antes)
    caso('(M-e) desfazer a errata do L1-R167', 'C-E, C-N1b', mut(me))

    def mf(Q):
        i = item(Q, 'L3-R20'); i['justificativa'] = 'REVERIFICAR. ' + i['justificativa']
    caso('(M-f) reintroduzir "REVERIFICAR. " numa justificativa (L3-R20)', 'C-R, C-N1b, C-L', mut(mf))

    def mg(Q):
        L3 = [x for x in Q['lotes'] if x['id'] == 'L3'][0]
        texts = {e['texto'] for e in ctx.entradas if e['lote'] == 'L3'}
        k = next(j for j, g in enumerate(L3['pegadinhas']) if g['texto'] in texts)
        L3['pegadinhas'][k], L3['pegadinhas'][k + 1] = L3['pegadinhas'][k + 1], L3['pegadinhas'][k]
    caso('(M-g) mover uma pegadinha nova uma posição', 'C-2p', mut(mg))

    def mh(Q):
        L3 = [x for x in Q['lotes'] if x['id'] == 'L3'][0]
        texts = {e['texto'] for e in ctx.entradas if e['lote'] == 'L3'}
        k = next(j for j, g in enumerate(L3['pegadinhas']) if g['texto'] in texts)
        L3['pegadinhas'][k]['rotulo'] = L3['pegadinhas'][k]['rotulo'] + ' x'
    caso('(M-h) trocar o `rotulo` de uma pegadinha nova', 'C-2p', mut(mh))

    def mi(Q):
        Q['topicos']['P2-1.4']['extra'] = 'x'
    caso('(M-i) acrescentar um campo a `topicos[P2-1.4]`', 'C-T', mut(mi))

    def mj(Q):
        t = Q['topicos']['P2-1.1']['resumo']
        Q['topicos']['P2-1.1']['resumo'] = t[:20] + ('x' if t[20] != 'x' else 'y') + t[21:]
    caso('(M-j) mudar um caractere de um resumo', 'C-T', mut(mj))

    def mk(Q):
        ks = list(Q['topicos'])
        d = collections.OrderedDict(Q['topicos'])
        ks[0], ks[1] = ks[1], ks[0]
        Q['topicos'] = collections.OrderedDict((k, d[k]) for k in ks)
    caso('(M-k) inverter a ordem de duas chaves de `topicos`', 'C-T', mut(mk))

    def ml(Q):
        n = copy.deepcopy(item(Q, 'L1-R132')); n['id'] = 'L1-R140'; n['numero'] = 140
        Q['itens'].append(n)
    caso('(M-l) incluir o id vago L1-R140', 'C-N1a, C-N1b', mut(ml))

    def ml2(Q):
        n = copy.deepcopy(item(Q, 'L3-R96')); n['id'] = 'L3-R103'; n['numero'] = 103
        Q['itens'].append(n)
    caso('(M-l) incluir o id diferido L3-R103', 'C-N1a, C-N1b', mut(ml2))

    def mm(Q):
        [s for s in Q['simulados'] if s['id'] == 'SIM-2'][0]['itens'].append('L3-R20')
    caso('(M-m) pôr um item novo (L3-R20) em SIM-2', 'C-S, C-3p', mut(mm))

    def mn():
        i = ct_txt.index('\n', 20000) + 40
        mt = ct_txt[:i] + ('x' if ct_txt[i] != 'x' else 'y') + ct_txt[i + 1:]
        return C.checa_contrato(mt)
    caso('(M-n) mudar um byte do contrato fora das linhas da C-14', 'C-14', mn)

    def mo():
        # sobre o conteúdo LF do insumo, numa cópia temporária fora do repositório, com posição fixa (o SHA impresso é igual em qualquer checkout)
        rel = 'saida/gce/T113_onda1_B_v2.md'
        lf = open(C.PATH(rel), 'rb').read().replace(b'\r\n', b'\n')
        b = bytearray(lf); k = 1000
        b[k] = ord('x') if b[k] != ord('x') else ord('y')
        d = tempfile.mkdtemp(prefix='mut_v112_o_')
        try:
            tmp = os.path.join(d, 'T113_onda1_B_v2.md')
            open(tmp, 'wb').write(bytes(b))
            mut_lf = open(tmp, 'rb').read()
            print('(M-o) SHA-256 do conteúdo LF mutado: %s' % hashlib.sha256(mut_lf).hexdigest())
            F.LEITOR = lambda r: mut_lf if r == rel else open(C.PATH(r), 'rb').read()
            try:
                F.le_insumo(rel)
            finally:
                F.LEITOR = None
        finally:
            shutil.rmtree(d, ignore_errors=True)
        return [('C-1', True, '')]
    caso('(M-o) mudar um byte de um insumo (T113_onda1_B_v2.md): falha de SHA-256 LF', 'C-1', mo)

    # (M-p) e (M-q): sobre cópia dos .md de out/estudante
    dmd = os.path.join(OUT, 'estudante')
    F1 = {n: open(os.path.join(dmd, n), encoding='utf-8', newline='').read() for n in sorted(os.listdir(dmd))}
    E = json.load(open(os.path.join(OUT, 'pacote_estudante.json'), encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
    if any(not o for i, o, m in C.checa_md(F1, E)):
        RES.append(dict(caso='controle dos .md: C-MD1 e C-MD2 sem mutação', esperado='0 falha', detectada=False, detectada_por=[], ok=False))

    def mp():
        G = dict(F1)
        l1, resto = G['L3_estudo.md'].split('\n', 1)
        G['L3_estudo.md'] = '# ' + cfg.NOMES_LOTE['L3'][0] + '\n' + resto
        return C.checa_md(G, E)
    caso('(M-p) repor o nome antigo na linha 1 do L3_estudo.md', 'C-MD1', mp)

    def mq():
        G = dict(F1)
        G['L5_gabarito.md'] = G['L5_gabarito.md'].replace('\n', '\nMecanismos: TC troca de conceito; GI generalização indevida\n\n', 1)
        return C.checa_md(G, E)
    caso('(M-q) repor uma legenda no L5_gabarito.md', 'C-MD2', mq)

    n_ok = sum(1 for r in RES if r['ok'])
    n_ap = sum(1 for r in RES if not r.get('nao_aplicavel'))
    for r in RES:
        print('%-5s %s | %s' % ('OK' if r['ok'] else 'FALHA', r['caso'], ('n/a' if r.get('nao_aplicavel') else ', '.join(r['detectada_por'])[:150])))
    print('fidelidade_mutacao_%s: %d/%d casos ok (%d aplicáveis; mutações detectadas: %d/%d; inclui o controle)' % (
        cfg.TAG, n_ok, len(RES), n_ap, sum(1 for r in RES if r['detectada']), sum(1 for r in RES if r['detectada'] is not None and not r['caso'].startswith('controle'))))
    with open(os.path.join(OUT, 'fidelidade_mutacao_%s.json' % cfg.TAG), 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(dict(total=len(RES), ok=n_ok, aplicaveis=n_ap, casos=RES), fh, ensure_ascii=False, indent=1); fh.write('\n')
    sys.exit(0 if n_ok == len(RES) else 1)


if __name__ == '__main__':
    main()
