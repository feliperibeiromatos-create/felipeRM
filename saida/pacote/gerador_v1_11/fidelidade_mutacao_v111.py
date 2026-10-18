# -*- coding: utf-8 -*-
"""T-108 e T-109 (gerador_v1_11, bloco M da seção 4 da D1) — passo 9: testes de mutação. Cada caso altera uma cópia das tabelas (em pasta temporária; nada do repositório é tocado) e
confere que o gerador PARA, com a conferência e a mensagem certas: 1 caractere de um `antes`; id de ocorrência duplicado (entre linhas e na própria linha); sobreposição de intervalos;
código de fonte no `depois`; FP em linha e FP engolido por um `antes`; BOM; `\\r`; SHA-256 diferente do fixado; id fora do universo; coluna ausente; `interno` adulterado (reversibilidade);
linha do T109 ausente; número da versão fora do config; condições de entrada da geração final; edição .md com campo sem correspondência. Mais o controle (sem mutação: o gerador passa).
Saída: out/fidelidade_mutacao_<TAG>.json; código 1 se algum caso não parar o gerador ou parar com a mensagem errada."""
import collections, copy, csv, io, json, os, shutil, sys, tempfile
from common import OUT, HERE
import config_v111 as cfg
import tabelas_v111 as T
import limpeza_v111 as L
import build_v111 as B
import inventario_v111 as I
import estudante_md_v111 as MD
import validate_v111 as V
import refs

RES = []


def caso(nome, esperado, fn):
    """fn() deve levantar T.Falha cuja mensagem contenha todas as partes de `esperado` (tupla de substrings)."""
    try:
        fn()
        RES.append(dict(caso=nome, esperado=list(esperado), parou=False, mensagem='(o gerador NÃO parou)', ok=False))
    except T.Falha as e:
        RES.append(dict(caso=nome, esperado=list(esperado), parou=True, mensagem=str(e)[:240], ok=all(x in str(e) for x in esperado)))
    except Exception as e:      # parou por exceção que não é a Falha prevista
        RES.append(dict(caso=nome, esperado=list(esperado), parou=True, mensagem='%s: %s' % (type(e).__name__, str(e)[:200]), ok=False))


def le_csv_bytes(raw):
    rd = csv.DictReader(io.StringIO(raw.decode('utf-8'), newline=''))
    return rd.fieldnames, list(rd)


def csv_bytes(cols, rows):
    buf = io.StringIO(newline='')
    w = csv.writer(buf, quoting=csv.QUOTE_ALL, lineterminator='\n')
    w.writerow(cols)
    for r in rows:
        w.writerow([r[c] for c in cols])
    return buf.getvalue().encode('utf-8')


def main():
    tmp = tempfile.mkdtemp(prefix='mut_v111_')
    try:
        base_itens = [(g, c, T.le_bytes(c), h) for g, c, h in cfg.TABELAS]
        ocorr = T.le_bytes(cfg.OCORRENCIAS[0]); t109 = T.le_bytes(cfg.T109[0])
        P0, _ = B.le_base()
        inv = {o['id_ocorrencia']: o for o in I.varre(P0, 'D')}
        oc = T.le_ocorrencias(ocorr)

        def muda_tabela(idx, fn, nome):
            """devolve a lista de tabelas com a tabela idx alterada por fn(cols, rows) -> (cols, rows) ou bytes; grava a cópia em tmp e lê de volta."""
            g, c, raw, h = base_itens[idx]
            cols, rows = le_csv_bytes(raw)
            out = fn(cols, rows)
            if not isinstance(out, bytes):
                out = csv_bytes(*out)
            p = os.path.join(tmp, nome)
            with open(p, 'wb') as fh:
                fh.write(out)
            nova = list(base_itens)
            nova[idx] = (g, nome, open(p, 'rb').read(), h)
            return nova

        def roda(itens, **kw):
            return B.gera(itens, ocorr, t109, **kw)

        # localiza linhas úteis nas tabelas (GCB real = índice 1)
        ig = 1
        cols, rows = le_csv_bytes(base_itens[ig][2])
        texto_de = {}
        def texto(cam):
            if cam not in texto_de:
                texto_de[cam] = T.resolve(P0, cam)[2][T.resolve(P0, cam)[3]]
            return texto_de[cam]
        reais = [r for r in rows if r['acao'] in ('SUBSTITUIR', 'DELETAR') and not r['id_edicao'].startswith('GCB-C9')]

        # 0. controle
        try:
            P, info = roda(base_itens)
            RES.append(dict(caso='controle (sem mutação): o gerador passa', esperado=[], parou=False, mensagem='%d edições aplicadas, %d MANTER' % (info['aplicadas'], info['mantidas']), ok=True))
        except T.Falha as e:
            RES.append(dict(caso='controle (sem mutação): o gerador passa', esperado=[], parou=True, mensagem=str(e)[:200], ok=False))

        # 1. um caractere do `antes`
        alvo = reais[0]
        def m1(cols, rows):
            for r in rows:
                if r['id_edicao'] == alvo['id_edicao']:
                    k = len(r['antes']) // 2
                    r['antes'] = r['antes'][:k] + ('q' if r['antes'][k] != 'q' else 'z') + r['antes'][k + 1:]
            return cols, rows
        caso('1 caractere de um antes alterado', ('C-3', alvo['id_edicao'], 'antes ocorre 0 vez'), lambda: roda(muda_tabela(ig, m1, 'm1.csv')))

        # 2. id de ocorrência duplicado
        rs_cam = collections.defaultdict(list)
        for r in reais:
            rs_cam[r['caminho']].append(r)
        par = next(v for v in rs_cam.values() if len(v) >= 2)
        def m2a(cols, rows):
            a, b = par[0]['id_edicao'], par[1]
            for r in rows:
                if r['id_edicao'] == a:
                    r['ids_ocorrencia'] = r['ids_ocorrencia'] + ';' + b['ids_ocorrencia'].split(';')[0]
            return cols, rows
        caso('id de ocorrência em duas linhas', ('C-2', 'mais de uma linha'), lambda: roda(muda_tabela(ig, m2a, 'm2a.csv')))
        def m2b(cols, rows):
            for r in rows:
                if r['id_edicao'] == alvo['id_edicao']:
                    r['ids_ocorrencia'] = r['ids_ocorrencia'].split(';')[0] + ';' + r['ids_ocorrencia'].split(';')[0]
            return cols, rows
        caso('id de ocorrência repetido na própria linha', ('C-2', alvo['id_edicao'], 'repetido'), lambda: roda(muda_tabela(ig, m2b, 'm2b.csv')))

        # 3. sobreposição de intervalos
        def m3(cols, rows):
            a, b = par[0], par[1]
            t = texto(a['caminho'])
            ia, ib = t.find(a['antes']), t.find(b['antes'])
            ini, fim = min(ia, ib), max(ia + len(a['antes']), ib + len(b['antes']))
            for r in rows:
                if r['id_edicao'] == b['id_edicao']:
                    r['antes'] = t[ini:fim]; r['depois'] = 'x' + t[ini:fim]; r['acao'] = 'SUBSTITUIR'
            return cols, rows
        caso('sobreposição de intervalos do mesmo campo', ('C-3', 'sobrepõe'), lambda: roda(muda_tabela(ig, m3, 'm3.csv')))

        # 4. código de fonte no depois
        sub = next(r for r in reais if r['acao'] == 'SUBSTITUIR')
        def m4(cols, rows):
            for r in rows:
                if r['id_edicao'] == sub['id_edicao']:
                    r['depois'] = r['depois'] + ' (F3)'
            return cols, rows
        caso('código de fonte (F3) no depois', ('C-7', sub['id_edicao'], 'proibição no depois'), lambda: roda(muda_tabela(ig, m4, 'm4.csv')))

        # 5a. FP em linha
        fps = [o for o in inv.values() if o['classe'] in ('FP-R1', 'FP-CONTEUDO')]
        fp = fps[0]
        def m5a(cols, rows):
            for r in rows:
                if r['id_edicao'] == alvo['id_edicao']:
                    r['ids_ocorrencia'] = r['ids_ocorrencia'] + ';' + fp['id_ocorrencia']
            return cols, rows
        caso('FP-R1/FP-CONTEUDO citado em linha', ('C-2', 'FP'), lambda: roda(muda_tabela(ig, m5a, 'm5a.csv')))

        # 5b. antes que engole um FP sem repô-lo no depois
        achado = None
        for r in reais:
            t = texto(r['caminho'])
            i = t.find(r['antes']); j = i + len(r['antes'])
            outros = [(t.find(x['antes']), t.find(x['antes']) + len(x['antes'])) for x in rows if x['caminho'] == r['caminho'] and x['id_edicao'] != r['id_edicao']]
            for f in fps:
                if f['caminho'] != r['caminho'] or (i <= f['_a'] and f['_b'] <= j):
                    continue
                ini, fim = min(i, f['_a']), max(j, f['_b'])
                if any(oa < fim and ini < ob for oa, ob in outros):
                    continue
                achado = (r, f, ini, fim, i, j)
                break
            if achado:
                break
        if achado:
            r_, f_, ini, fim, i, j = achado
            t = texto(r_['caminho'])
            def m5b(cols, rows):
                for r in rows:
                    if r['id_edicao'] == r_['id_edicao']:
                        antes = t[ini:fim]
                        dep = t[ini:i] + r['depois'] + t[j:fim]
                        lit = t[f_['_a']:f_['_b']]
                        dep = dep.replace(lit, '', 1) if lit in dep and (f_['_a'] < i or f_['_b'] > j) else dep
                        r['antes'], r['depois'] = antes, dep if dep != antes else dep + ' '
                        r['acao'] = 'SUBSTITUIR'
                return cols, rows
            caso('antes que engole um FP sem repô-lo no depois', ('C-3', 'FP'), lambda: roda(muda_tabela(ig, m5b, 'm5b.csv')))
        else:
            RES.append(dict(caso='antes que engole um FP sem repô-lo no depois', esperado=['C-3', 'FP'], parou=False, mensagem='(nenhuma linha com FP vizinho livre nas tabelas de ensaio: caso não montável)', ok=False))

        # 6. BOM e \r
        caso('BOM no início da tabela', ('C-1', 'BOM'), lambda: roda(muda_tabela(ig, lambda cols, rows: b'\xef\xbb\xbf' + base_itens[ig][2], 'm6.csv')))
        def m7(cols, rows):
            for r in rows:
                if r['id_edicao'] == sub['id_edicao']:
                    r['depois'] = r['depois'] + '\r'
            return cols, rows
        caso('caractere \\r no depois', ('C-1', '\\r'), lambda: roda(muda_tabela(ig, m7, 'm7.csv')))

        # 7. SHA-256, id fora do universo, coluna ausente
        def m8():
            it = list(base_itens); g, c, raw, h = it[ig]; it[ig] = (g, c, raw, '0' * 64)
            return roda(it)
        caso('SHA-256 da tabela diferente do fixado', ('C-1', 'SHA-256'), m8)
        def m9(cols, rows):
            for r in rows:
                if r['id_edicao'] == alvo['id_edicao']:
                    r['ids_ocorrencia'] = 'D-C99-00000000'
            return cols, rows
        caso('id de ocorrência fora do universo', ('C-2', 'fora do universo'), lambda: roda(muda_tabela(ig, m9, 'm9.csv')))
        caso('coluna obrigatória ausente', ('C-1', 'coluna obrigatória ausente'), lambda: roda(muda_tabela(ig, lambda cols, rows: ([c for c in cols if c != 'depois'], [{k: v for k, v in r.items() if k != 'depois'} for r in rows]), 'm10.csv')))
        def m11(cols, rows):
            return cols, [r for r in rows if r['id_edicao'] != alvo['id_edicao']]
        caso('cobertura incompleta (uma linha a menos)', ('C-2', 'cobertura'), lambda: roda(muda_tabela(ig, m11, 'm11.csv')))
        def m11b(cols, rows):
            for r in rows:
                if r['id_edicao'] == alvo['id_edicao']:
                    r['id_edicao'] = 'GCE-7777'
            return cols, rows
        caso('prefixo do id_edicao fora da Gerência dona da tabela', ('C-2', 'prefixo'), lambda: roda(muda_tabela(ig, m11b, 'm11b.csv')))

        # 8. `interno` adulterado: reversibilidade
        def m12():
            P, _ = roda(base_itens)
            o = next(x for x in P['itens'] if x.get('interno') and x['interno'][0]['depois'])
            o['interno'][0]['pos'] += 1
            Q = L.reverte(P)
            [i for i in Q['itens'] if i['id'] == 'L2-R16'][0]['itemEdital'] = 'P2-2.8'
            Q['nome'], Q['geradoEm'] = P0['nome'], P0['geradoEm']
            if json.dumps(Q, ensure_ascii=False, indent=1) != json.dumps(P0, ensure_ascii=False, indent=1):
                raise T.Falha('C-5', 'reversibilidade: o interno aplicado ao contrário não devolve o pacote v1.10')
        caso('`interno` com pos adulterado (reversibilidade)', ('C-5',), m12)

        # 9. T109 sem a linha do L2-R16
        def m13():
            Pc = copy.deepcopy(P0)
            txt = t109.decode('utf-8').replace('| L2-R16 | itemEdital | P2-2.8 | P2-3.1 |', '| L2-R16 | itemEdital | P2-2.8 | P2-3.2 |')
            B.troca_l2r16(Pc, txt.encode('utf-8'))
        caso('T109 sem a linha "L2-R16 | itemEdital | P2-2.8 | P2-3.1"', ('C-4', 'ausente'), m13)
        def m13b():
            Pc = copy.deepcopy(P0)
            [i for i in Pc['itens'] if i['id'] == 'L2-R16'][0]['itemEdital'] = 'P2-1.1'
            B.troca_l2r16(Pc, t109)
        caso('L2-R16 fora de P2-2.8 na base', ('C-4',), m13b)
        def m13c():
            Pc = copy.deepcopy(P0)
            Pc['simulados'][0]['itens'].append('L2-R16')
            B.troca_l2r16(Pc, t109)
        caso('L2-R16 num simulado', ('C-4', 'SIM-0'), m13c)

        # 10. número da versão fora do config
        def m14():
            d = os.path.join(tmp, 'ver'); os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, 'x.py'), 'w', encoding='utf-8') as fh:
                fh.write('"""cabeçalho"""\nNOME = "pacote v%s"\n' % cfg.VERSAO)
            ach = V.varre_literais_versao(d)
            if ach:
                raise T.Falha('C-16', 'literal de versão fora do config: %s' % ach[:1])
        caso('literal do número da versão fora de config_v111.py', ('C-16',), m14)

        # 11. condições de entrada da geração final
        def m15():
            pend = cfg.confere_final()
            if pend:
                raise T.Falha('C-1', 'condições de entrada da geração final não cumpridas: ' + '; '.join(pend))
        caso('geração final sem E1–E5 cumpridas (SHA das tabelas, ATO_L2R16)', ('C-1', 'condições de entrada'), m15)

        # 12. edição .md: campo sem correspondência no arquivo
        def m16():
            E_old = json.loads(refs.git_show(cfg.BASE_E[0], cfg.BASE_E[1]).decode('utf-8'), object_pairs_hook=collections.OrderedDict)
            E_new = json.load(open(os.path.join(OUT, 'pacote_estudante.json'), encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
            F0 = MD.pasta_blob(cfg.BASE[0], cfg.BASE_ESTUDANTE_DIR)
            mud = [m for m in MD.muda(E_old, E_new) if m[0].startswith('lotes[') and m[0].endswith('].curso')]
            lid = mud[0][0][len('lotes['):mud[0][0].index(']')]
            ant = mud[0][1]
            F0[lid + '_estudo.md'] = F0[lid + '_estudo.md'].replace(ant, ant[:50] + '#' + ant[51:], 1)
            MD.FALHAS.clear()
            MD.gera(E_old, E_new, F0, cfg.E_L2R16)
            if MD.FALHAS:
                raise T.Falha('C-11', MD.FALHAS[0])
        caso('edição .md: valor antigo sem a contagem esperada no arquivo', ('C-11', 'ocorrência'), m16)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    n_ok = sum(1 for r in RES if r['ok'])
    for r in RES:
        print('%-5s %s | %s' % ('OK' if r['ok'] else 'FALHA', r['caso'], r['mensagem'][:170]))
    print('fidelidade_mutacao_%s: %d/%d casos pararam o gerador com a mensagem certa (inclui o controle)' % (cfg.TAG, n_ok, len(RES)))
    with open(os.path.join(OUT, 'fidelidade_mutacao_%s.json' % cfg.TAG), 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(dict(total=len(RES), ok=n_ok, casos=RES), fh, ensure_ascii=False, indent=1); fh.write('\n')
    sys.exit(0 if n_ok == len(RES) else 1)


if __name__ == '__main__':
    main()
