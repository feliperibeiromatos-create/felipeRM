# -*- coding: utf-8 -*-
"""T-104 (v1.10) — conferências do ensaio (passo 5): (0) reconstrução byte a byte da v1.9 e da v1.9-E a partir da v1.10 e da v1.10-E;
(1) testes negativos por mutação sobre validate_v110.verifica; (2) lista fechada de arquivos do gerador frente ao v1_9; (3) promovidos e pastas intactos
(nada do ensaio sai de out/; na geração final, cfg.FINAL, os promovidos = out/ byte a byte); (4) contrato v1.2.7 (só na geração final). Saídas: out/conferencias_v110.json e, pelo runner, out/conferencias_stdout.txt. Sai com código 1 se houver falha."""
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

# (3) promovidos e pastas intactos (o ensaio só grava em out/). Na geração final (cfg.FINAL; adendo 1 da D1), os promovidos podem já ser a cópia byte a byte de out/:
#     pacote.json, pacote_estudante.json e saida/estudante/ = v1.9/v1.8 OU = out/; saida/gbq só com o adendo 2 = out/registro_adendo2.md; regras só com pacote_contrato.md (v1.2.7, bloco 4).
V19_SHA = ('1366055496457792bf55f541d901e2d1f277ee42611060b03bbf82b4427610bb', '8fa81b45a92095f8973c2787083d144869fdc195031455f7ff75ecb337e509e2')
prom = (sha(PATH('saida/pacote/pacote.json')), sha(PATH('saida/pacote/pacote_estudante.json')))
outs = (sha(os.path.join(OUT, 'pacote.json')), sha(os.path.join(OUT, 'pacote_estudante.json')))
if not getattr(cfg, 'FINAL', False):
    ok('3a', prom == V19_SHA, 'saida/pacote/pacote.json e pacote_estudante.json = v1.9 (não sobrescritos)')
else:
    ok('3a', prom in (V19_SHA, outs), 'FINAL: saida/pacote/pacote.json e pacote_estudante.json = v1.9 (antes da promoção) ou = out/ byte a byte (promovidos): %s' % ('v1.9' if prom == V19_SHA else 'promovidos' if prom == outs else 'DIVERGE'))
st = subprocess.run(['git', '-C', REPO, 'status', '--porcelain', '--untracked-files=all', '--', 'saida/estudante', 'saida/simulados', 'saida/gbq', 'regras', 'saida/pacote/gerador_v1_9'],
                    capture_output=True, text=True).stdout.rstrip('\n')
ADENDO2 = 'saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo2_%s.md' % cfg.GERADO_EM
def estudante_igual_out():
    d = PATH('saida/estudante'); o = os.path.join(OUT, 'estudante')
    fs = sorted(f for f in os.listdir(d) if os.path.isfile(os.path.join(d, f))); fo = sorted(os.listdir(o))
    return fs == fo and all(open(os.path.join(d, f), 'rb').read() == open(os.path.join(o, f), 'rb').read() for f in fs)
if not getattr(cfg, 'FINAL', False):
    ok('3b', st == '', 'saida/estudante, saida/simulados, saida/gbq, regras e gerador_v1_9 sem mudança no disco (%r)' % st[:200])
    d18 = subprocess.run(['git', '-C', REPO, 'diff', '--quiet', refs.C_V18, '--', 'saida/estudante']).returncode
    ok('3c', d18 == 0, 'saida/estudante = edição v1.8 (46496ca)')
else:
    linhas = [l for l in st.split('\n') if l.strip()]
    perm = []
    for l in linhas:
        cam = l[3:].strip()
        if cam == 'regras/pacote_contrato.md' and l[:2].strip() == 'M':
            perm.append(l)
        elif cam == ADENDO2 and l[:2] == '??' and open(PATH(cam), 'rb').read() == open(os.path.join(OUT, 'registro_adendo2.md'), 'rb').read():
            perm.append(l)
        elif cam.startswith('saida/estudante/'):
            perm.append(l)
    ok('3b', len(perm) == len(linhas), 'FINAL: saida/simulados e gerador_v1_9 sem mudança; em regras só pacote_contrato.md (v1.2.7); em saida/gbq só o adendo 2 = out/registro_adendo2.md (%r)' % [l for l in linhas if l not in perm][:5])
    d18 = subprocess.run(['git', '-C', REPO, 'diff', '--quiet', refs.C_V18, '--', 'saida/estudante']).returncode
    ok('3c', d18 == 0 and not any(l[3:].startswith('saida/estudante/') for l in linhas) or estudante_igual_out(),
       'FINAL: saida/estudante = edição v1.8 (46496ca) ou = out/estudante/ byte a byte (35 arquivos, promovidos)')

# (4) contrato v1.2.7 (D1, seção 5; registro saida/pacote/contrato_v1_2_7_<data>.md): diff contra a v1.2.6 do commit fixo refs.C_V19 (c26fc13) limitado a C-1 a C-3
# (T-104, reconciliação, A-1 da fidelidade: a base era o HEAD, que passou a ter a v1.2.7 depois do commit cacd606; agora é o commit fixo da v1.2.6)
if getattr(cfg, 'FINAL', False):
    import difflib
    c6 = refs.git_show(refs.C_V19, 'regras/pacote_contrato.md').replace(b'\r\n', b'\n').decode('utf-8')
    c7b = open(PATH('regras/pacote_contrato.md'), 'rb').read().replace(b'\r\n', b'\n'); c7 = c7b.decode('utf-8')
    A6, A7 = c6.split('\n'), c7.split('\n')
    ok('4a', hashlib.sha256(c6.encode()).hexdigest() == '7e749c88ae1e194a38529e13105b5b43c53571e0e06d76747cab21fb83d510a8', 'base: v1.2.6 do commit %s = 7e749c88…' % refs.C_V19)
    ok('4b', A7[0].endswith('(v1.2.7, 2026-10-18)') and c7.count('Errata de forma da v1.2.7 (T-104') == 1 and A7[2].startswith(A6[2]) and A7[2].endswith('ver a seção "Errata de forma da v1.2.7".'), 'linha 1 = v1.2.7; linha 3 = a da v1.2.6 + a frase da v1.2.7; uma só seção "Errata de forma da v1.2.7"')
    sm = difflib.SequenceMatcher(None, A6, A7, autojunk=False)
    ops = [(t, i1, i2, j1, j2) for t, i1, i2, j1, j2 in sm.get_opcodes() if t != 'equal']
    ank = A6.index('5. **Aplicação.** A partir do pacote v1.9 (T-94). Os 286 itens da v1.8 e os demais blocos (edital, simulados, lotes, discursivas) ficam como na v1.8. Registro: `saida/pacote/contrato_v1_2_6_2026-10-18.md`.')
    n_ins = len(A7) - len(A6)
    # a seção inserida começa com linha em branco; o difflib pode alinhar o bloco uma linha adiante (insert em ank+2 com a 1ª linha em branco da v1.2.6 casada) — mesmo texto
    ok('4c', ops in ([('replace', 0, 1, 0, 1), ('replace', 2, 3, 2, 3), ('insert', ank + 1, ank + 1, ank + 1, ank + 1 + n_ins)], [('replace', 0, 1, 0, 1), ('replace', 2, 3, 2, 3), ('insert', ank + 2, ank + 2, ank + 2, ank + 2 + n_ins)])
       and A7[ank + 1 + n_ins:] == A6[ank + 1:] and A7[3:ank + 1] == A6[3:ank + 1], 'diff contra a v1.2.6 = C-1 (l. 1), C-2 (l. 3) e C-3 (inserção depois da l. %d): %s' % (ank + 1, ops))
    reg = open(PATH('saida/pacote/contrato_v1_2_7_2026-10-18.md'), encoding='utf-8').read()
    ok('4d', reg.startswith('# contrato_v1_2_7_2026-10-18.md — T-104 — 2026-10-18 — gerado por gbq-gerencia') and hashlib.sha256(c7b).hexdigest() in reg and '7e749c88ae1e194a38529e13105b5b43c53571e0e06d76747cab21fb83d510a8' in reg,
       'registro contrato_v1_2_7_2026-10-18.md com os SHA antes (7e749c88…) e depois (%s…)' % hashlib.sha256(c7b).hexdigest()[:8])
    fontes_ctr = [l for l in A7 if l.startswith('| L') and '`saida/g' in l and ('D-T102-R4-SALDO' in l or 'D-T96-ONDA2' in l or 'D-T103' in l or 'D-T97-ONDA3' in l or 'D-T105' in l)]
    import reforco_v110 as RV
    shas = {a: s_ for g_ in RV.G.values() for a, s_, _ in g_['arquivos']}
    ok('4e', len(fontes_ctr) == 11 and len(shas) == 11 and all(any(('`%s`' % a) in l and ('`%s`' % s_[:8]) in l for l in fontes_ctr) for a, s_ in shas.items()), 'tabela de fonte da v1.2.7 = os 11 arquivos lidos pelo gerador, com o prefixo do SHA-256 (%d linhas)' % len(fontes_ctr))

for i, o, m in R:
    print('%-26s %s %s' % (i, 'OK  ' if o else 'FALHA', m))
falhas = [r for r in R if not r[1]]
print('conferencias_v110: %d/%d OK' % (len(R) - len(falhas), len(R)))
with open(os.path.join(OUT, 'conferencias_v110.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump(dict(total=len(R), ok=len(R) - len(falhas), conferencias=[dict(id=i, ok=o, msg=m) for i, o, m in R]), f, ensure_ascii=False, indent=1)
    f.write('\n')
sys.exit(1 if falhas else 0)
