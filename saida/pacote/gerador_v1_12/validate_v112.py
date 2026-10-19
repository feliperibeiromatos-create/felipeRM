# -*- coding: utf-8 -*-
"""T-115 (gerador_v1_12, D1 da GBQ, seção 4) — passo 6: validação do out/pacote.json e do out/pacote_estudante.json. Conferências A1 a A4, C-1', C-2', C-3', C-N1, C-N2, C-E, C-L, C-R, C-T, C-V, C-A, C-S, C-5
(checks_v112.checa_pacote), C-E1, C-NU e C-9 (checa_estudante e o relatório do passo 2), C-13 (simulados) e C-16 (número da versão só em config_v112.py). Leitura própria dos arquivos finais; as fontes são
relidas por checks_v112.Ctx. Saídas: out/validate_<TAG>.json e, pelo runner, out/validate_stdout.txt. Código 1 se qualquer conferência falhar."""
import collections, io, json, os, sys, tokenize
from common import OUT, HERE
import config_v112 as cfg
import checks_v112 as C
from fontes_v112 import Falha

R = []


def carrega(nome):
    return json.load(open(os.path.join(OUT, nome), encoding='utf-8'), object_pairs_hook=collections.OrderedDict)


def varre_literais_versao(pasta_scan=None):
    """C-16: nenhum literal do número da versão (cfg.VERSAO e cfg.TAG) fora de config_v112.py, salvo o nome da pasta do gerador, o docstring de cabeçalho e comentários."""
    nums = [cfg.VERSAO, cfg.TAG]
    pasta = 'gerador_' + cfg.TAG
    ach = []
    base_dir = pasta_scan or HERE
    for f in sorted(os.listdir(base_dir)):
        p = os.path.join(base_dir, f)
        if not os.path.isfile(p) or f == 'config_v112.py' or f.startswith('MANIFESTO'):
            continue
        if f.endswith('.py'):
            src = open(p, 'rb').read()
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
    ctx = C.Ctx()
    raw = open(os.path.join(OUT, 'pacote.json'), 'rb').read().decode('utf-8')
    P = json.loads(raw, object_pairs_hook=collections.OrderedDict)
    E = carrega('pacote_estudante.json')
    est_rel = carrega('estudante_json.json')
    res = []
    res.append(('A0', json.dumps(P, ensure_ascii=False, indent=1) + '\n' == raw, 'pacote.json: serialização canônica (indent=1, ensure_ascii=False, newline final)'))
    res += C.checa_pacote(P, ctx)
    res += C.checa_estudante(E, P, ctx)
    res.append(('C-9a', est_rel['falhas'] == [] and E['nome'] == cfg.NOME_E and E['versao'] == 1 and E['geradoEm'] == cfg.GERADO_EM,
                'pacote_estudante.json: asserções (a) a (f) da v1.10 sem falha (estudante_json_v112.py); nome e data de config_v112'))
    liq = est_rel['verificacao_residual']['liquido']
    res.append(('C-9e', liq == 0 or cfg.ENSAIO, 'verificação residual: %d casamento(s) das regras de deleção herdadas no pacote.json limpo (líquido %d frente à lista fechada EXCECOES_RESIDUAL; %d no total)' % (est_rel['verificacao_residual']['total'], liq, est_rel['verificacao_residual']['total'])))
    # C-13: simulados
    B = ctx.P0
    res.append(('C-13a', [(s['id'], s['itens']) for s in P['simulados']] == [(s['id'], s['itens']) for s in B['simulados']], 'simulados: ids, composição e ordem iguais à v1.11'))
    res.append(('C-13e', all(s.get('avisos') == b.get('avisos') for s, b in zip(P['simulados'], B['simulados'])), 'avisos dos simulados iguais aos da v1.11'))
    vol = {i['id'] for i in P['itens'] if i.get('volatil')}
    res.append(('C-13c', all(not (set(s['itens']) & vol) for s in P['simulados'] if s['tipo'] == 'final'), 'nenhum item VOLÁTIL em simulado final'))
    res.append(('C-13f', not any('L2-R18' in s['itens'] for s in P['simulados'] if s['tipo'] == 'final') and next(i for i in P['itens'] if i['id'] == 'L2-R18').get('volatil'), 'L2-R18 (restrição de montagem no `interno`) fora de todo simulado final e VOLÁTIL'))
    # C-16
    ach = varre_literais_versao()
    res.append(('C-16', not ach, 'nenhum literal de versão ("%s", "%s") fora de config_v112.py (%s)' % (cfg.VERSAO, cfg.TAG, ach[:3])))
    falhas = [r for r in res if not r[1]]
    for i, o, m in res:
        print('%-8s %s %s' % (i, 'OK  ' if o else 'FALHA', m))
    print('validate_%s: %d/%d OK (modo %s)' % (cfg.TAG, len(res) - len(falhas), len(res), 'FINAL' if cfg.FINAL else 'ENSAIO'))
    with open(os.path.join(OUT, 'validate_%s.json' % cfg.TAG), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(dict(total=len(res), ok=len(res) - len(falhas), verificacoes=[dict(id=i, ok=o, msg=m) for i, o, m in res]), f, ensure_ascii=False, indent=1); f.write('\n')
    sys.exit(1 if falhas else 0)


if __name__ == '__main__':
    try:
        main()
    except Falha as e:
        print('FALHA:', e)
        sys.exit(1)
