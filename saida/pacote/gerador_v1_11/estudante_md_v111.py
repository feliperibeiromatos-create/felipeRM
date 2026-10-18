# -*- coding: utf-8 -*-
"""T-108 e T-109 (gerador_v1_11, seção 1.8 da D1) — passo 4: edição do estudante em .md (out/estudante/, 35 arquivos).
Base: os 35 arquivos da v1.10 do git (config_v111.BASE[0]:saida/estudante). Para cada campo do -E que mudou entre a v1.10-E (git) e out/pacote_estudante.json, o valor antigo é trocado pelo novo
em cada arquivo .md em que aparece. A contagem do valor antigo em cada arquivo tem de ser a esperada pelo mapeamento campo->arquivo da v1.10 (lote->L*_estudo; item->gabarito do lote e dos
simulados em que está; nota->BANCO_gabarito e gabaritos de simulado; aviso->nenhum arquivo (a edição .md não os traz); discursiva->DISCURSIVAS e DISCURSIVAS_padrao); contagem diferente, valor antigo que seja
substring de outro campo do mesmo arquivo, ou valor antigo em arquivo fora do mapeamento = FALHA (a GBQ decide em D1 entre trecho maior e gerador de renderização com prova de volta).
No L2_gabarito.md, a linha "Item do edital" do bloco do L2-R16 troca P2-2.8 por P2-3.1 (1 ocorrência dentro do bloco). NUCLEO.md é regerado do campo `nucleo` do -E pelo mesmo código da v1.10.
No README.md, linha de versão. O resto fica byte a byte igual à v1.10. Saídas: out/estudante/ e out/estudante_md_<TAG>.json (trocas por arquivo)."""
import collections, json, os, re, shutil, sys
import subprocess
import refs, config_v111 as cfg
from common import REPO
import estudante_gen as gen
from common import OUT

HERE = os.path.dirname(os.path.abspath(__file__))
OUTE = os.path.join(OUT, 'estudante')
FALHAS = []


def falha(m):
    FALHAS.append(m)


def pasta_blob(commit, dir_):
    """{nome: texto} dos blobs de <commit>:<dir_>/ lidos por `git show` (bytes do blob, LF), não por `git archive` (que aplica a conversão de fim de linha do core.autocrlf local)."""
    nomes = subprocess.run(['git', '-C', REPO, 'ls-tree', '--name-only', commit, dir_ + '/'], check=True, capture_output=True).stdout.decode('utf-8').split(chr(10))
    out = {}
    for n in nomes:
        if n.strip():
            out[os.path.basename(n)] = refs.git_show(commit, n).decode('utf-8')
    return dict(sorted(out.items()))


def muda(a, b, caminho=''):
    """diferenças de strings entre dois objetos do mesmo formato: [(caminho, antigo, novo)]; estrutura diferente (chaves, tamanhos, tipos) é falha."""
    out = []
    if isinstance(a, dict):
        if not isinstance(b, dict) or list(a) != list(b):
            falha('estrutura: chaves diferentes em %s' % (caminho or '$'))
            return out
        for k in a:
            if k in ('nucleo',):
                continue
            out += muda(a[k], b[k], caminho + '.' + k if caminho else k)
    elif isinstance(a, list):
        if not isinstance(b, list) or len(a) != len(b):
            falha('estrutura: tamanho da lista diferente em %s' % caminho)
            return out
        for i, (u, v) in enumerate(zip(a, b)):
            ident = u['id'] if isinstance(u, dict) and 'id' in u and caminho in ('itens', 'lotes', 'simulados', 'discursivas') else None
            if ident is None and isinstance(u, dict) and caminho.endswith('aspectos'):
                ident = str(u['n'])
            if ident is None and isinstance(u, dict) and caminho.endswith('quesitos'):
                ident = u['id']
            out += muda(u, v, '%s[%s]' % (caminho, ident if ident is not None else i))
    elif isinstance(a, str):
        if a != b:
            out.append((caminho, a, b))
    elif a != b:
        out.append((caminho, a, b))      # não é string (ex.: itemEdital é string; número/bool não deveria mudar)
    return out


def campos_texto(E):
    """[(caminho, valor, [arquivos])] — o mapeamento campo->arquivo da v1.10 (edição do estudante)."""
    sims = collections.defaultdict(list)
    for s in E['simulados']:
        for i in s['itens']:
            sims[i].append(s['id'])
    out = []
    for L in E['lotes']:
        lid, f = L['id'], '%s_estudo.md' % L['id']
        b = 'lotes[%s]' % lid
        out += [(b + '.resumo', L['resumo'], [f]), (b + '.curso', L['curso'], [f])]
        for k, p in enumerate(L['pares']):
            for c in ('a', 'b', 'como'):
                out.append(('%s.pares[%d].%s' % (b, k, c), p.get(c) or '', [f]))
        for k, g in enumerate(L['pegadinhas']):
            for c in ('rotulo', 'texto'):
                out.append(('%s.pegadinhas[%d].%s' % (b, k, c), g[c], [f]))
    for it in E['itens']:
        gs = ['%s_gabarito.md' % s for s in sims[it['id']]]
        if it['rotulo'] == 'AUTORAL':
            out.append(('itens[%s].justificativa' % it['id'], it['justificativa'], ['%s_gabarito.md' % gen.lote_fund(it['id'])] + gs))
        else:
            out.append(('itens[%s].justificativa' % it['id'], it['justificativa'], gs))
            if it.get('nota'):
                out.append(('itens[%s].nota' % it['id'], it['nota'], ['BANCO_gabarito.md'] + gs))
    for s in E['simulados']:
        for k, a in enumerate(s.get('avisos') or []):
            out.append(('simulados[%s].avisos[%d]' % (s['id'], k), a, []))      # os avisos não são renderizados na edição .md da v1.10
    for d in E['discursivas']:
        b = 'discursivas[%s]' % d['id']
        out.append((b + '.comando', d['comando'], ['DISCURSIVAS.md']))
        out.append((b + '.padrao', d['padrao'], ['DISCURSIVAS_padrao.md']))
        for a in d['aspectos']:
            out.append(('%s.aspectos[%s].texto' % (b, a['n']), a['texto'], ['DISCURSIVAS_padrao.md']))
        for q in d['quesitos']:
            out.append(('%s.quesitos[%s].nome' % (b, q['id']), q['nome'], ['DISCURSIVAS_padrao.md']))
            for k, c in enumerate(q['conceitos']):
                out.append(('%s.quesitos[%s].conceitos[%d]' % (b, q['id'], k), c, ['DISCURSIVAS_padrao.md']))
    return out


def nucleo_md(E):
    """NUCLEO.md — mesmo código da v1.10 (estudante_md_v110.py)."""
    pf = collections.OrderedDict()
    for it in E['itens']:
        pf.setdefault(it['itemEdital'], []).append(it)
    N = ['# Câmara 2026 — Núcleo de estudo por item do edital', '',
         'Em cada item do edital, os itens marcados como núcleo são os 10 primeiros pela ordem em que foram incorporados ao material (itens de provas anteriores e itens de lotes de estudo; '
         'havendo empate, os de aderência direta antes dos de aderência parcial). Item do edital com 10 itens ou menos: todos são núcleo.', '']
    for f in sorted(pf, key=lambda s: (s[:2], [int(x) for x in s[3:].split('.')])):
        ids = [i['id'] for i in pf[f] if i['nucleo']]
        N.append('- %s (%d de %d): %s' % (f, len(ids), len(pf[f]), ', '.join(ids)))
    return '\n'.join(N) + '\n'


def gera(E_old, E_new, F0, l2r16=True):
    """-> (F, trocas, relatorio). F0: {nome: texto} da v1.10 (35 arquivos)."""
    F = dict(F0)
    mud = [m for m in muda(E_old, E_new) if m[0] != 'nome' and m[0] != 'geradoEm']
    l2 = [m for m in mud if m[0] == 'itens[L2-R16].itemEdital']
    mud = [m for m in mud if m[0] != 'itens[L2-R16].itemEdital']
    if l2r16 and (len(l2) != 1 or l2[0][1:] != ('P2-2.8', 'P2-3.1')):
        falha('L2-R16.itemEdital: mudança esperada P2-2.8 -> P2-3.1 ausente ou diferente (%s)' % l2)
    if not l2r16 and l2:
        falha('L2-R16.itemEdital mudou sem E_L2R16')
    campos = campos_texto(E_old)
    por_arq = collections.defaultdict(list)
    for cam, val, arqs in campos:
        for a in arqs:
            por_arq[a].append((cam, val))
    mapa = {cam: arqs for cam, _, arqs in campos}
    trocas = []
    antigos = collections.defaultdict(set)
    for cam, old, new in mud:
        if not isinstance(old, str):
            falha('%s: mudança fora de campo de texto' % cam); continue
        antigos[old].add(new)
    for old, news in antigos.items():
        if len(news) > 1:
            falha('o mesmo valor antigo vira %d textos novos diferentes (%r…)' % (len(news), old[:40]))
    feito = set()
    consumido = set()          # campos já trocados por inteiro (um campo mais longo que contém o valor antigo de outro, trocado antes)
    for cam, old, new in sorted(mud, key=lambda m: (-len(m[1]), m[0])):
        if cam not in mapa:
            falha('%s: campo sem mapeamento para arquivo' % cam); continue
        if old in feito:
            continue
        feito.add(old)
        iguais = [c2 for c2, v2, as2 in campos if v2 == old]
        permit = set(a for c2, v2, as2 in campos if v2 == old for a in as2) | set(mapa[cam])
        # contagem esperada por arquivo: soma, nos campos mapeados ao arquivo e ainda não trocados, das ocorrências do valor antigo
        n_exp = collections.Counter()
        outros = []
        for a in sorted(permit):
            for c2, v2 in por_arq[a]:
                if c2 in consumido:
                    continue
                k = v2.count(old)
                if k:
                    n_exp[a] += k
                    if v2 != old:
                        outros.append((a, c2))
        if outros:
            falha('%s: o valor antigo é substring de outro campo do mesmo arquivo (%s)' % (cam, outros[:2])); continue
        achou = {a: t.count(old) for a, t in F.items() if old in t}
        for a, n in achou.items():
            if a not in permit:
                falha('%s: valor antigo em arquivo fora do mapeamento (%s, %d)' % (cam, a, n))
        ok_todos = True
        for a in sorted(permit):
            if a not in F:
                falha('%s: arquivo %s inexistente na v1.10' % (cam, a)); ok_todos = False; continue
            if F[a].count(old) != n_exp[a]:
                falha('%s: %s tem %d ocorrência(s) do valor antigo, esperadas %d' % (cam, a, F[a].count(old), n_exp[a])); ok_todos = False
        if not permit:
            continue          # campo que a edição .md não traz: já conferido que o valor antigo não está em arquivo algum
        if ok_todos:
            if not any(n_exp[a] for a in permit):
                falha('%s: valor antigo não encontrado em nenhum arquivo do mapeamento' % cam)
            for a in sorted(permit):
                if n_exp[a]:
                    F[a] = F[a].replace(old, new)
                    trocas.append(dict(campo=cam, arquivo=a, ocorrencias=n_exp[a]))
            consumido.update(iguais)
    # L2-R16: linha "Item do edital" do bloco, em L2_gabarito.md
    if l2r16:
        g = F['L2_gabarito.md']
        ini = g.find('### L2-R16 — Gabarito')
        if ini < 0:
            falha('L2_gabarito.md: bloco do L2-R16 ausente')
        else:
            fim = g.find('\n### ', ini + 5)
            fim = len(g) if fim < 0 else fim
            bloco = g[ini:fim]
            if bloco.count('Item do edital: P2-2.8') != 1:
                falha('L2_gabarito.md: "Item do edital: P2-2.8" ocorre %d vez(es) no bloco do L2-R16' % bloco.count('Item do edital: P2-2.8'))
            else:
                F['L2_gabarito.md'] = g[:ini] + bloco.replace('Item do edital: P2-2.8', 'Item do edital: P2-3.1') + g[fim:]
                trocas.append(dict(campo='itens[L2-R16].itemEdital', arquivo='L2_gabarito.md', ocorrencias=1))
    # NUCLEO.md e README.md
    F['NUCLEO.md'] = nucleo_md(E_new)
    r = F['README.md']
    old_v = [l for l in r.split('\n') if l.startswith('- Versão: v')]
    if len(old_v) != 1:
        falha('README: linha de versão ausente ou repetida')
    else:
        r = r.replace(old_v[0], '- Versão: v%s (pacote.json versão 1)' % cfg.VERSAO)
    old_d = [l for l in r.split('\n') if l.startswith('- Data: ')]
    if len(old_d) != 1:
        falha('README: linha de data ausente ou repetida')
    else:
        r = r.replace(old_d[0], '- Data: %s' % cfg.GERADO_EM)
    F['README.md'] = r
    return F, trocas, dict(mudancas=len(mud), valores_distintos=len(antigos))


def main():
    E_new = json.load(open(os.path.join(OUT, 'pacote_estudante.json'), encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
    E_old = json.loads(refs.git_show(cfg.BASE_E[0], cfg.BASE_E[1]).decode('utf-8'), object_pairs_hook=collections.OrderedDict)
    F0 = pasta_blob(cfg.BASE[0], cfg.BASE_ESTUDANTE_DIR)
    if len(F0) != 35:
        falha('v1.10: %d arquivos em saida/estudante (esperado 35)' % len(F0))
    F, trocas, rel = gera(E_old, E_new, F0, cfg.E_L2R16)
    mudou = sorted(n for n in F if F[n] != F0.get(n))
    if len(F) != 35:
        falha('%d arquivos na saída (esperado 35)' % len(F))
    if FALHAS:
        for m in FALHAS[:40]:
            print('FALHA:', m)
        print('%d falhas (de %d mudanças de campo)' % (len(FALHAS), rel['mudancas']))
        sys.exit(1)
    if os.path.isdir(OUTE):
        shutil.rmtree(OUTE)
    os.makedirs(OUTE)
    for nome, t in sorted(F.items()):
        with open(os.path.join(OUTE, nome), 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(t)
    with open(os.path.join(OUT, 'estudante_md_%s.json' % cfg.TAG), 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(dict(trocas=trocas, arquivos_alterados=mudou, **rel), fh, ensure_ascii=False, indent=1); fh.write('\n')
    print('edição .md v%s (%s): %d arquivos; %d campos mudaram (%d valores distintos); %d trocas; arquivos alterados: %d' % (cfg.VERSAO, 'FINAL' if cfg.FINAL else 'ENSAIO', len(F), rel['mudancas'], rel['valores_distintos'], len(trocas), len(mudou)))
    print('0 falhas')


if __name__ == '__main__':
    main()
