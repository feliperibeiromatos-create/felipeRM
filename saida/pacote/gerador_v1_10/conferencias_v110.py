# -*- coding: utf-8 -*-
"""T-104 (v1.10) — conferências do ensaio (passo 5): (0) reconstrução byte a byte da v1.9 e da v1.9-E a partir da v1.10 e da v1.10-E;
(1) testes negativos por mutação sobre validate_v110.verifica; (2) lista fechada de arquivos do gerador frente ao v1_9; (3) promovidos e pastas intactos
(nada do ensaio sai de out/). Saídas: out/conferencias_v110.json e, pelo runner, out/conferencias_stdout.txt. Sai com código 1 se houver falha."""
import collections, copy, csv, hashlib, json, os, subprocess, sys
from common import OUT, P as PATH, REPO
import refs, config_v110 as cfg, build_v110 as B, validate_v110 as V

HERE = os.path.dirname(os.path.abspath(__file__))
R = []
def ok(i, c, m): R.append((i, bool(c), m))
def ser(o): return json.dumps(o, ensure_ascii=False, indent=1) + '\n'

raw19 = refs.git_show(refs.C_V19, refs.PACOTE); rawE19 = refs.git_show(refs.C_V19, 'saida/pacote/pacote_estudante.json')
P = json.load(open(os.path.join(OUT, 'pacote.json'), encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
E = json.load(open(os.path.join(OUT, 'pacote_estudante.json'), encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
P19 = json.loads(raw19.decode('utf-8')); E19 = json.loads(rawE19.decode('utf-8'))


def desfaz(o, nome19):
    o = copy.deepcopy(o)
    o['itens'] = o['itens'][:334]; o['nome'] = nome19; o['geradoEm'] = '2026-10-18'
    for it in o['itens']:
        it.pop('nucleo', None)
    for k in reversed(B.ATIVAS):
        bloco, oid, campo, old, new, _ = B.TROCAS[k]
        x = [y for y in o[bloco] if y['id'] == oid][0]
        assert x[campo].count(new) == 1, k
        x[campo] = x[campo].replace(new, old)
    return o


# (0) reconstrução
ok('0a', ser(desfaz(P, P19['nome'])).encode('utf-8') == raw19, 'v1.10 sem os 225, sem as trocas %s e com nome/data da v1.9 = v1.9 byte a byte (13660554…)' % B.ATIVAS)
ok('0b', ser(desfaz(E, E19['nome'])).encode('utf-8') == rawE19, 'v1.10-E sem os 225, sem "nucleo", sem as trocas e com nome/data da v1.9-E = v1.9-E byte a byte (8fa81b45…)')

# (1) mutações: cada uma tem de ser apanhada por verifica()
banco = {r['id']: r['data_verificacao'] for r in csv.DictReader(open(PATH('banco/banco.csv'), encoding='utf-8'), delimiter=';')}
fontes = V.leitura_propria()
base = V.verifica(P, E, P19, E19, fontes, banco)
ok('1.0', all(r[1] for r in base), 'verifica() sem mutação: %d/%d' % (sum(r[1] for r in base), len(base)))


def mut(nome, f):
    p, e = copy.deepcopy(P), copy.deepcopy(E)
    f(p, e)
    try:
        rr = V.verifica(p, e, P19, E19, fontes, banco)
        pegou = [r[0] for r in rr if not r[1]]
    except Exception as ex:      # verificação que não chega ao fim também reprova o objeto
        pegou = ['exceção: %s' % type(ex).__name__]
    ok('1.' + nome, pegou, 'mutação "%s" apanhada por %s' % (nome, pegou))


def g(p, iid): return [i for i in p['itens'] if i['id'] == iid][0]
mut('gabarito', lambda p, e: g(p, 'L2-R50').update(gabarito='C'))
mut('enunciado legado', lambda p, e: g(p, 'L1-Q01').update(enunciado=g(p, 'L1-Q01')['enunciado'] + ' '))
mut('volatil a mais', lambda p, e: g(p, 'L1-R19').update(volatil=True))
mut('item a menos', lambda p, e: p['itens'].pop())
mut('aderencia', lambda p, e: g(p, 'L2-R130').update(aderencia='direta'))
mut('nucleo trocado', lambda p, e: [i for i in e['itens'] if i['id'] == 'L2-R19'][0].update(nucleo=True))
mut('item novo em simulado', lambda p, e: p['simulados'][0]['itens'].append('L1-R19'))
mut('curso do L2', lambda p, e: [l for l in p['lotes'] if l['id'] == 'L2'][0].update(curso=[l for l in p['lotes'] if l['id'] == 'L2'][0]['curso'] + ' '))
mut('justificativa do estudante', lambda p, e: [i for i in e['itens'] if i['id'] == 'L1-R103'][0].update(justificativa='REVERIFICAR. ' + [i for i in e['itens'] if i['id'] == 'L1-R103'][0]['justificativa']))
mut('padrão D1', lambda p, e: [d for d in p['discursivas'] if d['id'] == 'D1'][0].update(padrao=[d for d in p['discursivas'] if d['id'] == 'D1'][0]['padrao'] + ' '))

# (2) lista fechada de arquivos do gerador frente ao v1_9
V19 = os.path.join(HERE, '..', 'gerador_v1_9')
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
a19 = {f for f in os.listdir(V19) if os.path.isfile(os.path.join(V19, f))}
a10 = {f for f in os.listdir(HERE) if os.path.isfile(os.path.join(HERE, f))}
NOVOS = {'build_v110.py', 'config_v110.py', 'conferencias_v110.py', 'estudante_md_v110.py', 'manifesto_v1_10.py', 'marcas_x_v110.py', 'nucleo.py',
         'reforco_marcas_v110.py', 'reforco_v110.py', 'registro_adendo_v110.py', 'validate_v110.py'}
ALTERADOS = {'estudante_json.py', 'refs.py', 'rodar_tudo.sh'}      # e o MANIFESTO.md, reescrito no passo 8, depois desta conferência
alt = {f for f in a19 & a10 if f != 'MANIFESTO.md' and sha(os.path.join(V19, f)) != sha(os.path.join(HERE, f))}
ok('2a', a10 - a19 == NOVOS, 'arquivos novos = %s (%s)' % (sorted(NOVOS), sorted(a10 - a19)))
ok('2b', alt == ALTERADOS and not (a19 - a10), 'alterados = %s; removidos: nenhum (%s; %s)' % (sorted(ALTERADOS), sorted(alt), sorted(a19 - a10)))

# (3) promovidos e pastas intactos (o ensaio só grava em out/)
ok('3a', sha(PATH('saida/pacote/pacote.json')) == '1366055496457792bf55f541d901e2d1f277ee42611060b03bbf82b4427610bb'
   and sha(PATH('saida/pacote/pacote_estudante.json')) == '8fa81b45a92095f8973c2787083d144869fdc195031455f7ff75ecb337e509e2', 'saida/pacote/pacote.json e pacote_estudante.json = v1.9 (não sobrescritos)')
st = subprocess.run(['git', '-C', REPO, 'status', '--porcelain', '--', 'saida/estudante', 'saida/simulados', 'saida/gbq', 'regras', 'saida/pacote/gerador_v1_9'],
                    capture_output=True, text=True).stdout.strip()
ok('3b', st == '', 'saida/estudante, saida/simulados, saida/gbq, regras e gerador_v1_9 sem mudança no disco (%r)' % st[:200])
d18 = subprocess.run(['git', '-C', REPO, 'diff', '--quiet', refs.C_V18, '--', 'saida/estudante']).returncode
ok('3c', d18 == 0, 'saida/estudante = edição v1.8 (46496ca)')

for i, o, m in R:
    print('%-26s %s %s' % (i, 'OK  ' if o else 'FALHA', m))
falhas = [r for r in R if not r[1]]
print('conferencias_v110: %d/%d OK' % (len(R) - len(falhas), len(R)))
with open(os.path.join(OUT, 'conferencias_v110.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump(dict(total=len(R), ok=len(R) - len(falhas), conferencias=[dict(id=i, ok=o, msg=m) for i, o, m in R]), f, ensure_ascii=False, indent=1)
    f.write('\n')
sys.exit(1 if falhas else 0)
