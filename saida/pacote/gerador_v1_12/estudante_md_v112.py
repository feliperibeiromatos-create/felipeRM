# -*- coding: utf-8 -*-
"""T-115 (gerador_v1_12, D1 da GBQ, seção 7) — passo 4: edição do estudante em .md (out/estudante/, 35 arquivos).
Base: os 35 arquivos da v1.11 lidos do blob do commit config_v112.BASE[0] (saida/estudante). Mudanças, e só elas (a lista dos arquivos que mudam vai a out/estudante_md_<TAG>.json e ao MANIFESTO):
  (1) nome do lote: o nome antigo vira o novo no cabeçalho de L<n>_estudo.md, L<n>_itens.md e L<n>_gabarito.md (1 ocorrência por arquivo); nome do SIM-0 em SIM-0_folha.md e SIM-0_gabarito.md;
  (2) "## Pegadinhas" de cada L<n>_estudo.md regerada do pacote_estudante.json (as novas na posição do pacote; a regeração a partir do -E da v1.11 tem de devolver a seção da v1.11);
  (3) ao fim de cada L<n>_estudo.md, uma seção "## Tópico <id> — <texto do edital>" por tópico do lote, com "### Resumo do tópico" (parágrafos do `resumo`) e, nos três do piloto, "### Em 1 minuto" (3 itens) e os visuais em texto
      (tabela em tabela .md com a legenda abaixo; fluxo em lista numerada; esquema em lista com o centro em negrito; linha em lista "quando — texto");
  (4) L1, L2, L3 e L4 _itens.md e _gabarito.md: os itens novos ao fim da seção "## Itens de reforço" (criada no L4), no formato da v1.10, com o texto do pacote_estudante.json;
  (5) NUCLEO.md recalculado; README.md: versão, data, a linha dos itens de reforço (L4 entra) e a linha dos tópicos.
  (6) legendas de mecanismo (decisão da GBQ, T115_reconciliacao seção 1): retiradas de L4, L5, L6A e L6B _gabarito.md (linha 3) e de SIM-1_gabarito.md (duas), cada uma com a linha em branco seguinte; falha se a contagem não for 1, 1, 1, 1 e 2.
O resto fica byte a byte igual ao da v1.11. A linha 1 de cada L<n>_estudo.md é "# " + nome do lote no -E (a troca do passo (1) não é desfeita pelo passo (2)).
Falha (sys.exit(1)) se qualquer troca não tiver exatamente a contagem esperada ou se o resto diferir da v1.11. Não lê relógio."""
import collections, json, os, re, shutil, subprocess, sys
import refs, config_v112 as cfg
from common import REPO, OUT
import estudante_gen as gen

OUTE = os.path.join(OUT, 'estudante')
FALHAS = []
AVISO = '> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.'
LOTES_REFORCO = ['L1', 'L2', 'L3', 'L4']
LEGENDA_RX = re.compile(r'^(Mecanismo: troca de conceito \(TC\)|Mecanismos: TC troca de conceito)')


def falha(m):
    FALHAS.append(m)


def pasta_blob(commit, dir_):
    """{nome: texto} dos blobs de <commit>:<dir_>/ lidos por `git show` (bytes do blob, LF)."""
    nomes = subprocess.run(['git', '-C', REPO, 'ls-tree', '--name-only', commit, dir_ + '/'], check=True, capture_output=True).stdout.decode('utf-8').split(chr(10))
    out = {}
    for n in nomes:
        if n.strip():
            out[os.path.basename(n)] = refs.git_show(commit, n).decode('utf-8')
    return dict(sorted(out.items()))


def secao_pegadinhas(L):
    lin = []
    for g in L['pegadinhas']:
        assert '\n' not in g['texto'] and '\n' not in g['rotulo']
        lin.append('- [%s] **%s** — %s' % (g['itemEdital'], g['rotulo'], g['texto']))
    return '\n'.join(lin) if lin else '_Nenhuma pegadinha registrada neste lote._'


def nucleo_md(E):
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


def cel(s):
    return str(s).replace('\n', ' ').replace('|', '\\|')


def visual_md(v):
    L = ['#### %s' % v['titulo'], '']
    t = v['tipo']
    if t == 'tabela':
        L.append('| ' + ' | '.join(cel(c) for c in v['colunas']) + ' |')
        L.append('|' + '|'.join('---' for _ in v['colunas']) + '|')
        for r in v['linhas']:
            L.append('| ' + ' | '.join(cel(c) for c in r) + ' |')
        if v.get('legenda'):
            L += ['', '*%s*' % v['legenda']]
    elif t == 'fluxo':
        L += ['%d. %s' % (k, p) for k, p in enumerate(v['passos'], 1)]
    elif t == 'esquema':
        L.append('- **%s**' % v['centro'])
        L += ['  - %s' % r for r in v['ramos']]
    elif t == 'linha':
        L += ['- %s — %s' % (m['quando'], m['texto']) for m in v['marcos']]
    elif t == 'barras':
        L += ['- %s: %s%s' % (d['rotulo'], d['valor'], (' ' + v['unidade']) if v['unidade'] else '') for d in v['dados']]
        L += ['', 'Fonte: %s' % v['fonte']]
    else:
        falha('visual de tipo desconhecido: %s' % t)
    return L


def lote_do_topico(k, lotes):
    """lote (fundido) cujo `itensEdital` contém o tópico ou, não havendo, um item do edital que ele prefixa (P1-4 -> P1-4.1…); L1C, L4C e L5C não contam (fundidos)."""
    c = [L['id'] for L in lotes if k in L['itensEdital']]
    if not c:
        c = [L['id'] for L in lotes if any(x.startswith(k + '.') for x in L['itensEdital'])]
    if len(c) != 1:
        falha('tópico %s com %d lote(s): %s' % (k, len(c), c))
        return None
    return c[0]


def secao_topicos(lid, lotes, E):
    edital = {e['id']: e['texto'] for e in E['edital']}
    L = []
    n = 0
    for k, t in E['topicos'].items():
        if lote_do_topico(k, lotes) != lid:
            continue
        n += 1
        L += ['## Tópico %s — %s' % (k, edital[k]), '', '### Resumo do tópico', '']
        for p in t['resumo'].split('\n\n'):
            L += [p, '']
        if 'emUmMinuto' in t:
            L += ['### Em 1 minuto', ''] + ['- %s' % x for x in t['emUmMinuto']] + ['']
            for v in t['visuais']:
                L += visual_md(v) + ['']
    return L, n


def bloco_itens(its):
    I, G = [], []
    for it in its:
        if it['textoBase']:
            I += ['**Texto-base.** %s' % it['textoBase'], '']
        if it['comando'] != 'Julgue o item.':
            I += ['*%s*' % it['comando'], '']
        I += ['**%s** — %s' % (it['id'], it['enunciado']), '']
        if it.get('volatil'):
            I += [AVISO, '']
        ade = ' (aderência: parcial)' if it['aderencia'] == 'parcial' else ''
        G += ['### %s — Gabarito: %s' % (it['id'], it['gabarito']), '', '- Item do edital: %s%s' % (it['itemEdital'], ade), '- Justificativa: %s' % it['justificativa'], '']
        if it.get('volatil'):
            G += [AVISO, '']
    return I, G


def gera(E_old, E_new, F0):
    """-> (F, relatório). F0: {nome: texto} da v1.11 (35 arquivos)."""
    F = dict(F0)
    rel = collections.OrderedDict()
    # --- conferências de estrutura: o resto do -E é o da v1.11
    if [i['id'] for i in E_new['itens'][:cfg.BASE_ITENS]] != [i['id'] for i in E_old['itens']]:
        falha('itens da v1.11 mudaram de ids ou de ordem no -E')
    for a, b in zip(E_old['itens'], E_new['itens']):
        x, y = dict(a), dict(b)
        x.pop('nucleo'); y.pop('nucleo')
        if x != y:
            falha('item %s mudou no -E (fora o nucleo)' % a['id'])
    lo = {L['id']: L for L in E_old['lotes']}
    ln = {L['id']: L for L in E_new['lotes']}
    for lid, L in lo.items():
        if 'legendaMecanismo' in ln[lid] or ('legendaMecanismo' in L) != (lid in ('L4', 'L5', 'L6A', 'L6B')):
            falha('lotes[%s]: legendaMecanismo no -E (a base traz nos 4 lotes de P1; a versão nova, em nenhum)' % lid)
        for c in L:
            if c in ('nome', 'pegadinhas', 'legendaMecanismo'):
                continue
            if L[c] != ln[lid].get(c):
                falha('lotes[%s].%s mudou no -E' % (lid, c))
    for a, b in zip(E_old['simulados'], E_new['simulados']):
        x, y = dict(a), dict(b)
        x.pop('nome'); y.pop('nome')
        if x != y:
            falha('simulado %s mudou no -E (fora o nome)' % a['id'])
    if E_old['discursivas'] != E_new['discursivas'] or E_old['edital'] != E_new['edital']:
        falha('discursivas ou edital mudaram no -E')
    # --- (1) nomes
    for lid, L in ln.items():
        antes = lo[lid]['nome']; depois = L['nome']
        if (antes, depois) != cfg.NOMES_LOTE[lid]:
            falha('nome do lote %s no -E (%r) difere do da D1' % (lid, depois))
        for arq in ('%s_estudo.md' % lid, '%s_itens.md' % lid, '%s_gabarito.md' % lid):
            if F[arq].count(antes) != 1:
                falha('%s: o nome antigo ocorre %d vez(es) (esperado 1)' % (arq, F[arq].count(antes)))
            F[arq] = F[arq].replace(antes, depois)
            rel.setdefault('nome', []).append(arq)
    for arq in ('SIM-0_folha.md', 'SIM-0_gabarito.md'):
        if F[arq].count(cfg.SIM0_NOME[0]) != 1:
            falha('%s: o nome antigo do SIM-0 ocorre %d vez(es) (esperado 1)' % (arq, F[arq].count(cfg.SIM0_NOME[0])))
        F[arq] = F[arq].replace(cfg.SIM0_NOME[0], cfg.SIM0_NOME[1])
        rel.setdefault('nome', []).append(arq)
    # --- (2) pegadinhas
    for lid, L in ln.items():
        arq = '%s_estudo.md' % lid
        marca = '\n## Pegadinhas\n\n'
        if F0[arq].count(marca) != 1:
            falha('%s: seção Pegadinhas ausente ou repetida' % arq); continue
        ini0 = F0[arq].index(marca) + len(marca)
        antiga = F0[arq][ini0:]
        if antiga != secao_pegadinhas(lo[lid]) + '\n':
            falha('%s: a seção Pegadinhas da v1.11 não é a regeração do -E da v1.11 (a seção não é a última ou o formato difere)' % arq)
        if F[arq].count(marca) != 1:
            falha('%s: seção Pegadinhas ausente ou repetida depois do passo (1)' % arq); continue
        ini = F[arq].index(marca) + len(marca)       # parte de F[arq] (já com o nome novo), não de F0[arq]
        F[arq] = F[arq][:ini] + secao_pegadinhas(L) + '\n'
        if F[arq].split('\n', 1)[0] != '# ' + L['nome']:
            falha('%s: linha 1 diferente de "# " + nome do lote no -E' % arq)
    # --- (3) tópicos
    nt = 0
    for lid, L in ln.items():
        sec, n = secao_topicos(lid, E_new['lotes'], E_new)
        nt += n
        if n:
            arq = '%s_estudo.md' % lid
            F[arq] = F[arq].rstrip('\n') + '\n\n' + '\n'.join(sec).rstrip('\n') + '\n'
            rel.setdefault('topicos', []).append((arq, n))
    if nt != len(E_new['topicos']):
        falha('%d tópicos renderizados, %d no -E' % (nt, len(E_new['topicos'])))
    # --- (4) itens novos
    novos = [i for i in E_new['itens'][cfg.BASE_ITENS:]]
    por_lote = collections.OrderedDict((l, []) for l in LOTES_REFORCO)
    for it in novos:
        if it['rotulo'] != 'AUTORAL' or gen.lote_fund(it['id']) not in por_lote:
            falha('item novo %s fora de L1-L4' % it['id']); continue
        por_lote[gen.lote_fund(it['id'])].append(it)
    for lid, xs in por_lote.items():
        I, G = bloco_itens(xs)
        for arq, extra in (('%s_itens.md' % lid, I), ('%s_gabarito.md' % lid, G)):
            base = F[arq]
            tem = base.count('\n## Itens de reforço\n') == 1
            if tem and not base.rstrip('\n').split('\n## Itens de reforço\n')[1:]:
                falha('%s: seção de reforço vazia' % arq)
            if tem:
                if '\n## ' in base.split('\n## Itens de reforço\n', 1)[1]:
                    falha('%s: a seção de reforço não é a última' % arq)
                F[arq] = base.rstrip('\n') + '\n\n' + '\n'.join(extra).rstrip('\n') + '\n'
            else:
                if base.count('## Itens de reforço') != 0:
                    falha('%s: seção de reforço em posição inesperada' % arq)
                F[arq] = base.rstrip('\n') + '\n\n## Itens de reforço\n\n' + '\n'.join(extra).rstrip('\n') + '\n'
            rel.setdefault('itens', []).append((arq, len(xs)))
    # --- (6) legendas de mecanismo
    esperado = collections.OrderedDict([('L4_gabarito.md', 1), ('L5_gabarito.md', 1), ('L6A_gabarito.md', 1), ('L6B_gabarito.md', 1), ('SIM-1_gabarito.md', 2)])
    leg = 0
    for arq in sorted(F):
        if not arq.endswith('_gabarito.md'):
            continue
        lin = F[arq].split('\n'); novo = []; k = 0; n = 0
        while k < len(lin):
            if LEGENDA_RX.match(lin[k]):
                if k + 1 >= len(lin) or lin[k + 1] != '':
                    falha('%s: legenda sem linha em branco seguinte' % arq)
                n += 1; k += 2; continue
            novo.append(lin[k]); k += 1
        if n != esperado.get(arq, 0):
            falha('%s: %d legenda(s) de mecanismo (esperado %d)' % (arq, n, esperado.get(arq, 0)))
        if n:
            F[arq] = '\n'.join(novo); leg += n
            rel.setdefault('legendas_retiradas', []).append((arq, n))
    if leg != 6:
        falha('%d legendas retiradas (esperado 6)' % leg)
    # --- (5) NUCLEO.md e README.md
    F['NUCLEO.md'] = nucleo_md(E_new)
    r = F['README.md']
    old_v = [l for l in r.split('\n') if l.startswith('- Versão: v')]
    old_d = [l for l in r.split('\n') if l.startswith('- Data: ')]
    if len(old_v) != 1 or len(old_d) != 1:
        falha('README: linha de versão ou de data ausente ou repetida')
    else:
        r = r.replace(old_v[0], '- Versão: v%s (pacote.json versão 1)' % cfg.VERSAO).replace(old_d[0], '- Data: %s' % cfg.GERADO_EM)
    old_r = '- L1, L2, L3, L6A e L6B: os itens de reforço estão ao fim de cada arquivo _itens.md e _gabarito.md, na seção "Itens de reforço".'
    new_r = ('- L1, L2, L3, L4, L6A e L6B: os itens de reforço estão ao fim de cada arquivo _itens.md e _gabarito.md, na seção "Itens de reforço".\n'
             '- Cada arquivo _estudo.md traz, ao fim, uma seção "Tópico" por tópico do lote: o resumo ("Resumo do tópico") e, em alguns tópicos, "Em 1 minuto" e os visuais em texto.')
    if r.count(old_r) != 1:
        falha('README: a linha dos itens de reforço ocorre %d vez(es)' % r.count(old_r))
    r = r.replace(old_r, new_r)
    F['README.md'] = r
    rel['novos_por_lote'] = {k: len(v) for k, v in por_lote.items()}
    rel['topicos_renderizados'] = nt
    return F, rel


def main():
    E_new = json.load(open(os.path.join(OUT, 'pacote_estudante.json'), encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
    E_old = json.loads(refs.git_show(cfg.BASE_E[0], cfg.BASE_E[1]).decode('utf-8'), object_pairs_hook=collections.OrderedDict)
    F0 = pasta_blob(cfg.BASE[0], cfg.BASE_ESTUDANTE_DIR)
    if len(F0) != 35:
        falha('v1.11: %d arquivos em saida/estudante (esperado 35)' % len(F0))
    F, rel = gera(E_old, E_new, F0)
    mudou = sorted(n for n in F if F[n] != F0.get(n))
    if len(F) != 35:
        falha('%d arquivos na saída (esperado 35)' % len(F))
    for n in F0:
        if n not in mudou and F[n] != F0[n]:
            falha('%s mudou sem estar na lista' % n)
    if FALHAS:
        for m in FALHAS[:40]:
            print('FALHA:', m)
        print('%d falhas' % len(FALHAS))
        sys.exit(1)
    if os.path.isdir(OUTE):
        shutil.rmtree(OUTE)
    os.makedirs(OUTE)
    for nome, t in sorted(F.items()):
        with open(os.path.join(OUTE, nome), 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(t)
    with open(os.path.join(OUT, 'estudante_md_%s.json' % cfg.TAG), 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(dict(arquivos_alterados=mudou, **rel), fh, ensure_ascii=False, indent=1); fh.write('\n')
    print('edição .md v%s (%s): %d arquivos; %d mudam; novos por lote %s; %d tópicos' % (cfg.VERSAO, 'FINAL' if cfg.FINAL else 'ENSAIO', len(F), len(mudou), rel['novos_por_lote'], rel['topicos_renderizados']))
    print('0 falhas')


if __name__ == '__main__':
    main()
