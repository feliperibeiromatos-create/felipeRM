# -*- coding: utf-8 -*-
"""T-108 e T-109 (gerador_v1_11, seção 4 da D1) — passo 6: validação do out/pacote.json e do out/pacote_estudante.json. Conferências C-4, C-9, C-10, C-13 e C-16, mais a forma do `interno`
(seção 1.5) e a contagem de itens. Leitura própria dos arquivos finais. Saídas: out/validate_<TAG>.json e, pelo runner, out/validate_stdout.txt. Código 1 se qualquer conferência falhar."""
import collections, copy, io, json, os, re, subprocess, sys, tokenize
from common import OUT, HERE, REPO
import refs, config_v111 as cfg
import tabelas_v111 as T
import limpeza_v111 as L

R = []


def ok(i, c, m):
    R.append((i, bool(c), m))


def carrega(nome):
    return json.load(open(os.path.join(OUT, nome), encoding='utf-8'), object_pairs_hook=collections.OrderedDict)


def sem_interno(o):
    o = copy.deepcopy(o)
    for l in ('itens', 'lotes', 'simulados', 'discursivas'):
        for x in o[l]:
            x.pop('interno', None)
    return o


def neutraliza(P, caminhos):
    """zera os campos citados nas tabelas (e o itemEdital do L2-R16, o nome e o geradoEm) para comparar o resto."""
    P = copy.deepcopy(P)
    for cam in caminhos:
        obj, rel, cont, chave = T.resolve(P, cam)
        cont[chave] = ''
    P['nome'] = P['geradoEm'] = ''
    for i in P['itens']:
        if i['id'] == 'L2-R16':
            i['itemEdital'] = ''
    return P


def varre_literais_versao(pasta_scan=None):
    """C-16: nenhum literal do número da versão (cfg.VERSAO e cfg.TAG) fora de config_v111.py, salvo o nome da pasta do gerador, o docstring de cabeçalho e comentários."""
    nums = [cfg.VERSAO, cfg.TAG]
    pasta = 'gerador_' + cfg.TAG
    ach = []
    base_dir = pasta_scan or HERE
    for f in sorted(os.listdir(base_dir)):
        p = os.path.join(base_dir, f)
        if not os.path.isfile(p) or f == 'config_v111.py' or f.startswith('MANIFESTO'):
            continue
        if f.endswith('.py'):
            src = open(p, 'rb').read()
            doc_line_end = 0
            try:
                toks = list(tokenize.tokenize(io.BytesIO(src).readline))
            except tokenize.TokenError:
                continue
            primeiro = True
            for t in toks:
                if t.type == tokenize.STRING:
                    if primeiro:
                        primeiro = False          # docstring do módulo (cabeçalho)
                        continue
                    s = t.string.replace(pasta, '')
                    if any(n in s for n in nums):
                        ach.append((f, t.start[0], t.string[:60]))
                elif t.type not in (tokenize.COMMENT, tokenize.NL, tokenize.NEWLINE, tokenize.ENCODING, tokenize.INDENT, tokenize.DEDENT):
                    primeiro = False
                    if t.type == tokenize.NUMBER and t.string == cfg.VERSAO:
                        ach.append((f, t.start[0], t.string))
        elif f.endswith('.sh'):
            for k, l in enumerate(open(p, encoding='utf-8'), 1):
                if l.startswith('#'):
                    continue
                s = l.replace(pasta, '')
                for fn in os.listdir(base_dir):      # nome de arquivo do próprio gerador (ex.: o script do passo 10)
                    s = s.replace(fn, '')
                if any(n in s for n in nums):
                    ach.append((f, k, l.strip()[:60]))
    return ach


def main():
    raw = open(os.path.join(OUT, 'pacote.json'), 'rb').read().decode('utf-8')
    P = json.loads(raw, object_pairs_hook=collections.OrderedDict)
    E = carrega('pacote_estudante.json')
    base_raw = refs.git_show(cfg.BASE[0], cfg.BASE[1]).decode('utf-8')
    B = json.loads(base_raw, object_pairs_hook=collections.OrderedDict)
    EB = json.loads(refs.git_show(cfg.BASE_E[0], cfg.BASE_E[1]).decode('utf-8'), object_pairs_hook=collections.OrderedDict)
    st = carrega('stats_%s.json' % cfg.TAG)
    est_rel = carrega('estudante_json.json')

    # forma geral e do `interno`
    ok('A1', json.dumps(P, ensure_ascii=False, indent=1) + '\n' == raw and P['versao'] == 1 and P['nome'] == cfg.NOME and P['geradoEm'] == cfg.GERADO_EM and list(P) == list(B), 'pacote.json: serialização canônica, versao 1, nome e geradoEm de config_v111, chaves de topo da v1.10')
    ok('A2', len(P['itens']) == cfg.BASE_ITENS and [i['id'] for i in P['itens']] == [i['id'] for i in B['itens']], 'pacote.json: %d itens, mesmos ids e mesma ordem da v1.10' % cfg.BASE_ITENS)
    forma = True
    n_obj = n_rec = 0
    for l in ('itens', 'lotes', 'simulados', 'discursivas'):
        for o in P[l]:
            if 'interno' in o:
                n_obj += 1
                itn = o['interno']
                forma &= list(o)[-1] == 'interno' and isinstance(itn, list) and len(itn) > 0
                for r in itn:
                    n_rec += 1
                    forma &= list(r) == ['edicao', 'campo', 'pos', 'antes', 'depois', 'regra', 'ocorrencias'] and isinstance(r['pos'], int) and isinstance(r['ocorrencias'], list)
    ok('A3', forma and n_rec == st['edicoes_aplicadas'], '`interno`: último campo do objeto, nunca vazio, registros {edicao, campo, pos, antes, depois, regra, ocorrencias}; %d registros em %d objetos = edições aplicadas' % (n_rec, n_obj))
    ok('A4', not any('interno' in x for l in ('itens', 'lotes', 'simulados', 'discursivas') for x in E[l]), '`interno` ausente do pacote_estudante.json')

    # C-4 invariantes
    cams = []
    for l in ('itens', 'lotes', 'simulados', 'discursivas'):
        for o in P[l]:
            for r in o.get('interno', []):
                cams.append('%s[%s].%s' % (l, o['id'], r['campo']))
    a, b = neutraliza(sem_interno(P), cams), neutraliza(B, cams)
    ok('C-4', json.dumps(a, ensure_ascii=False) == json.dumps(b, ensure_ascii=False),
       'retirados o interno, nome, geradoEm, os %d campos editados e itens[L2-R16].itemEdital, o pacote.json é idêntico à BASE (ids, ordem, enunciado, comando, textoBase, gabarito, itemEdital, aderencia, volatil, url, rotulo, simulados, edital, itensEdital, legendaMecanismo, pares[].id, valores, quesitos)' % len(set(cams)))
    ok('C-4b', [i['itemEdital'] for i in P['itens'] if i['id'] == 'L2-R16'] == (['P2-3.1'] if cfg.E_L2R16 else ['P2-2.8']), 'L2-R16 em %s' % ('P2-3.1' if cfg.E_L2R16 else 'P2-2.8'))

    # C-9 estudante
    ok('C-9a', est_rel['falhas'] == [] and E['nome'] == cfg.NOME_E and E['versao'] == 1 and E['geradoEm'] == cfg.GERADO_EM, 'pacote_estudante.json: asserções (a) a (f) da v1.10 sem falha (estudante_json_v111.py); nome e data de config_v111')
    ok('C-9b', all(list(i)[-1] == 'nucleo' and isinstance(i['nucleo'], bool) for i in E['itens']), '"nucleo" booleano e último campo de todo item do -E')
    ok('C-9c', [l['id'] for l in E['lotes']] == ['L1', 'L2', 'L3', 'L4', 'L5', 'L6A', 'L6B'], 'fusão 1-C/4-C/5-C: lotes L1, L2, L3, L4, L5, L6A, L6B')
    ok('C-9d', all(i['url'] == '' for i in E['itens'] if i['rotulo'] == 'AUTORAL') and sum(1 for i in E['itens'] if i['rotulo'] == 'AUTORAL' and i['url'] == '') == sum(1 for i in P['itens'] if i['rotulo'] == 'AUTORAL'), 'url vazia nos AUTORAL do -E (todos)')
    _ep = {i['id']: i for i in E['itens']}
    _dif = []
    for _i in P['itens']:
        for _c in ('justificativa', 'nota', 'enunciado', 'comando', 'textoBase'):
            if _c in _i and _ep[_i['id']].get(_c) != _i[_c]:
                _dif.append('%s.%s' % (_i['id'], _c))
    _lp = {l['id']: l for l in P['lotes']}
    for _l in E['lotes']:
        if _l['id'] in ('L1',):
            continue
        for _c in ('resumo', 'curso'):
            if _l[_c] != _lp[_l['id']][_c]:
                _dif.append('%s.%s' % (_l['id'], _c))
        if _l['pares'] != _lp[_l['id']]['pares'] or _l['pegadinhas'] != _lp[_l['id']]['pegadinhas']:
            _dif.append('%s.pares/pegadinhas' % _l['id'])
    _dp = {d['id']: d for d in P['discursivas']}
    for _d in E['discursivas']:
        _x = _dp[_d['id']]
        if (_d['comando'], _d['padrao'], _d['aspectos'], _d['quesitos']) != (_x['comando'], _x['padrao'], _x['aspectos'], _x['quesitos']):
            _dif.append(_d['id'])
    _sp = {x['id']: x for x in P['simulados']}
    _dif += [x['id'] for x in E['simulados'] if x.get('avisos') != _sp[x['id']].get('avisos')]
    ok('C-9f', not _dif, 'cada campo de texto exibido do -E é igual ao do pacote.json sem `interno` (fora a fusão 1-C/4-C/5-C no L1 e a url vazia): %s' % (_dif[:5] or '0 diferença'))
    ok('C-9e', est_rel['verificacao_residual']['liquido'] == 0 or cfg.ENSAIO, 'verificação residual: %d casamento(s) das regras de deleção herdadas no pacote.json limpo (%s)' % (est_rel['verificacao_residual']['liquido'], 'FINAL: líquido 0 frente à lista fechada EXCECOES_RESIDUAL, %d no total' % est_rel['verificacao_residual']['total'] if cfg.FINAL else 'ENSAIO: informativo'))

    # C-10 nucleo
    dif = [i['id'] for i, j in zip(E['itens'], EB['itens']) if i['nucleo'] != j['nucleo']]
    alvo = {'P2-2.8', 'P2-3.1'}
    folha_de = {i['id']: (i['itemEdital'], j['itemEdital']) for i, j in zip(E['itens'], EB['itens'])}
    ok('C-10a', all(set(folha_de[d]) & alvo for d in dif), 'nucleo: %d diferença(s) frente à v1.10-E, todas em itens das folhas P2-2.8 e P2-3.1: %s' % (len(dif), dif))
    f28 = [i for i in E['itens'] if i['itemEdital'] == 'P2-2.8']
    f31 = [i for i in E['itens'] if i['itemEdital'] == 'P2-3.1']
    if cfg.E_L2R16:
        ok('C-10b', len(f28) == 19 and sum(1 for i in f28 if i['aderencia'] == 'direta') == 18 and sum(1 for i in f28 if i.get('volatil')) == 4 and len(f31) == 7 and all(i['nucleo'] for i in f31),
           'P2-2.8 com %d itens (%d diretos, %d VOLÁTEIS); P2-3.1 com %d itens, todos nucleo true' % (len(f28), sum(1 for i in f28 if i['aderencia'] == 'direta'), sum(1 for i in f28 if i.get('volatil')), len(f31)))
    else:
        ok('C-10b', len(f28) == 20 and not dif, 'sem troca: P2-2.8 com 20 itens e nucleo igual ao da v1.10-E')
    folhas = carrega('folhas_%s.json' % cfg.TAG)
    ok('C-10c', all(v['nucleo'] == min(10, v['total']) for v in folhas.values()), 'nucleo = min(10, total) em cada uma das %d folhas (out/folhas_%s.json)' % (len(folhas), cfg.TAG))

    # C-13 simulados
    ok('C-13a', [(s['id'], s['itens']) for s in P['simulados']] == [(s['id'], s['itens']) for s in B['simulados']] and [s['id'] for s in P['simulados']] == [s['id'] for s in B['simulados']], 'simulados: ids, composição e ordem iguais à v1.10')
    ok('C-13b', all(not ({'L4-11', 'BQ-0010'} <= set(s['itens'])) for s in P['simulados']), 'L4-11 e BQ-0010 (TRF6, item 81) nunca no mesmo simulado')
    vol = {i['id'] for i in P['itens'] if i.get('volatil')}
    ok('C-13c', all(not (set(s['itens']) & vol) for s in P['simulados'] if s['tipo'] == 'final'), 'nenhum item VOLÁTIL em simulado final')
    ok('C-13f', not any('L2-R18' in s['itens'] for s in P['simulados'] if s['tipo'] == 'final') and next(i for i in P['itens'] if i['id'] == 'L2-R18').get('volatil'), 'L2-R18 (restrição de montagem no `interno`) fora de todo simulado final e VOLÁTIL')
    ok('C-13d', not any('QA PENDENTE' in json.dumps(i, ensure_ascii=False) for i in P['itens']), 'nenhum item com "QA PENDENTE"')
    # avisos: só mudam por linhas GBQ ou das tabelas; composição igual
    ok('C-13e', all(s.get('avisos') == b.get('avisos') for s, b in zip(P['simulados'], B['simulados']) if s['id'] != 'SIM-0') and len(P['simulados'][0]['avisos']) == len(B['simulados'][0]['avisos']), 'avisos: iguais aos da v1.10 fora do SIM-0; SIM-0 com o mesmo número de avisos')

    # C-16 número
    ach = varre_literais_versao()
    ok('C-16', not ach, 'nenhum literal de versão ("%s", "%s") fora de config_v111.py (%s)' % (cfg.VERSAO, cfg.TAG, ach[:3]))

    falhas = [r for r in R if not r[1]]
    for i, o, m in R:
        print('%-8s %s %s' % (i, 'OK  ' if o else 'FALHA', m))
    print('validate_%s: %d/%d OK (modo %s)' % (cfg.TAG, len(R) - len(falhas), len(R), 'FINAL' if cfg.FINAL else 'ENSAIO'))
    with open(os.path.join(OUT, 'validate_%s.json' % cfg.TAG), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(dict(total=len(R), ok=len(R) - len(falhas), verificacoes=[dict(id=i, ok=o, msg=m) for i, o, m in R]), f, ensure_ascii=False, indent=1); f.write('\n')
    sys.exit(1 if falhas else 0)


if __name__ == '__main__':
    main()
