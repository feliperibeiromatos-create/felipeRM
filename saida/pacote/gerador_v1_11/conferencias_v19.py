# -*- coding: utf-8 -*-
"""T-94 — conferências da v1.9 (passo 5 do rodar_tudo.sh da v1_9), independentes do gerador salvo onde dito. Lê out/pacote.json e out/pacote_estudante.json e compara com a v1.8 aceita
lida do git (refs.C_V18; SHA-256 09d4a457… e 851e2370…, D-PACOTE-V18).
(0) diff v1.8 -> v1.9 do pacote.json: só `$.nome`, `$.geradoEm` e 48 itens acrescentados ao fim de `$.itens`; os 286 itens da v1.8 idênticos (campo a campo e byte a byte, por reconstrução).
(1) idem para o pacote_estudante.json v1.8-E -> v1.9-E.
(2) contrato v1.2.6: linha 1, seção única, diff contra o HEAD só nas linhas registradas; registro do contrato com os SHA.
(3) testes negativos (mutação em cópias temporárias, fora do repositório): validate_v19.py e as conferências (0)/(1) têm de falhar.
(4) gerador: arquivos da v1_9 frente à v1_8 (lista fechada); pastas que a T-94 não toca, intactas frente ao HEAD.
Código 1 se houver falha. Grava out/conferencias_v19.json."""
import collections, copy, hashlib, json, os, subprocess, sys, tempfile
from common import HERE, OUT, REPO
import refs

res = []
def chk(sec, n, ok, extra=''):
    res.append(dict(sec=sec, n=n, ok=bool(ok), extra=extra)); print('OK   ' if ok else 'FALHA', sec, '|', n, ('| ' + extra) if extra else '')
def sha(b): return hashlib.sha256(b).hexdigest()
def j(o): return json.dumps(o, ensure_ascii=False, indent=1) + '\n'

R18 = refs.git_show(refs.C_V18, refs.PACOTE); E18r = refs.git_show(refs.C_V18, 'saida/pacote/pacote_estudante.json')
P19r = open(os.path.join(OUT, 'pacote.json'), 'rb').read(); E19r = open(os.path.join(OUT, 'pacote_estudante.json'), 'rb').read()
OD = collections.OrderedDict
def load(b): return json.loads(b.decode('utf-8'), object_pairs_hook=OD)


def diff_v18(a18, b19, nome18, nome19, rotulo):
    """lista de problemas: v1.9 deve ser a v1.8 com nome/geradoEm trocados e 48 itens no fim."""
    P18, P19 = load(a18), load(b19); prob = []
    if list(P18) != list(P19): prob.append('chaves de topo')
    for k in P18:
        if k in ('nome', 'geradoEm', 'itens'): continue
        if P18[k] != P19[k] or j(P18[k]) != j(P19[k]): prob.append('bloco %s difere' % k)
    if (P18['nome'], P18['geradoEm'], P19['nome'], P19['geradoEm']) != (nome18, '2026-10-17', nome19, '2026-10-18'): prob.append('nome/geradoEm')
    if len(P18['itens']) != 286 or len(P19['itens']) != 334: prob.append('contagem de itens %d/%d' % (len(P18['itens']), len(P19['itens'])))
    dif = [a['id'] for a, b in zip(P18['itens'], P19['itens']) if j(a) != j(b) or list(a) != list(b)]
    if dif: prob.append('itens da v1.8 alterados: %s' % dif[:5])
    R = copy.deepcopy(P19); R['nome'] = nome18; R['geradoEm'] = '2026-10-17'; R['itens'] = R['itens'][:286]
    if j(R).encode('utf-8') != a18: prob.append('reconstrução byte a byte falhou (%s)' % rotulo)
    return prob

N18, N19 = 'Câmara 2026 — pacote F4 (v1.8)', 'Câmara 2026 — pacote F4 (v1.9)'
NE18, NE19 = 'Câmara 2026 — pacote do estudante (v1.8-E)', 'Câmara 2026 — pacote do estudante (v1.9-E)'
# ------------------------------------------------------------------ (0) pacote.json
chk('(0)', 'base v1.8 do git (%s): SHA-256 09d4a457…, 621907 bytes' % refs.C_V18,
    sha(R18) == '09d4a457612781275659a3f7fbfd3a182f20fd9d4003e5ba38007d0c26c7a9c0' and len(R18) == 621907)
p0 = diff_v18(R18, P19r, N18, N19, 'pacote.json')
chk('(0)', 'diff v1.8 -> v1.9: só $.nome, $.geradoEm e 48 itens no fim de $.itens; 286 itens, edital (47), simulados (4), lotes (10) e discursivas (5) idênticos; reconstrução byte a byte', not p0, str(p0))
P19 = load(P19r); P18 = load(R18)
novos = P19['itens'][286:]
chk('(0)', 'os 48 acrescentados: ids L1-R01…L6A-R01, nenhum id da v1.8; rótulo AUTORAL', [i['id'] for i in novos] == ['L1-R%02d' % k for k in range(1, 19)] + ['L2-R%02d' % k for k in range(1, 19)] + ['L3-R%02d' % k for k in range(1, 12)] + ['L6A-R01']
    and not {i['id'] for i in novos} & {i['id'] for i in P18['itens']} and all(i['rotulo'] == 'AUTORAL' for i in novos))
chk('(0)', 'pacote.json v1.9: %d bytes, SHA-256 %s' % (len(P19r), sha(P19r)), True)
# ------------------------------------------------------------------ (1) pacote_estudante.json
chk('(1)', 'base v1.8-E do git: SHA-256 851e2370…, 602815 bytes', sha(E18r) == '851e2370a9f5e9c8e5db725ff84777f70c12f81044983d339434ac7504e04c3e' and len(E18r) == 602815)
p1 = diff_v18(E18r, E19r, NE18, NE19, 'pacote_estudante.json')
chk('(1)', 'diff v1.8-E -> v1.9-E: só $.nome, $.geradoEm e 48 itens no fim; 286 itens e demais blocos idênticos; reconstrução byte a byte', not p1, str(p1))
E19 = load(E19r)
chk('(1)', 'os 48 do estudante = os 48 do pacote.json com url "" e justificativa só por deleção (subsequência)',
    all(list(a) == list(b) and all(a[k] == b[k] for k in a if k not in ('url', 'justificativa')) and b['url'] == '' for a, b in zip(novos, E19['itens'][286:]))
    and all((lambda o, n: (lambda it: all(ch in it for ch in n))(iter(o)))(a['justificativa'], b['justificativa']) for a, b in zip(novos, E19['itens'][286:])))
chk('(1)', 'pacote_estudante.json v1.9-E: %d bytes, SHA-256 %s' % (len(E19r), sha(E19r)), True)
# ------------------------------------------------------------------ (2) contrato
ctr = open(os.path.join(REPO, 'regras', 'pacote_contrato.md'), 'rb').read().replace(b'\r\n', b'\n')
ctr_h = refs.git_show(refs.C_V18, 'regras/pacote_contrato.md')      # v1.2.5 aceita com a v1.8 (o HEAD pode já trazer a v1.2.6 depois do commit do orquestrador).replace(b'\r\n', b'\n')
t = ctr.decode('utf-8'); L = t.split('\n')
chk('(2)', 'contrato: commit da v1.8 = v1.2.5 (10eac696…); disco = v1.2.6: linha 1 "(v1.2.6, 2026-10-18)", 1 seção "Errata de forma da v1.2.6 (T-94;", antes do separador "---"',
    sha(ctr_h) == '10eac696dbb83049ba12ee793ff4991a1884094b7b88cdaf39f10a3fcc33660e' and L[0] == '# pacote.json — contrato de dados entre a fábrica e a plataforma (v1.2.6, 2026-10-18)'
    and t.count('Errata de forma da v1.2.6 (T-94;') == 1 and t.index('Errata de forma da v1.2.6 (T-94;') < t.index('\n---\n'))
import difflib
ops = [o for o in difflib.SequenceMatcher(None, ctr_h.decode('utf-8').split('\n'), L, autojunk=False).get_opcodes() if o[0] != 'equal']
chk('(2)', 'diff contra a v1.2.5: linha 1 e linha 3 trocadas; 19 linhas inseridas depois da linha 149; nada mais', [(o[0], o[1], o[2], o[4] - o[3]) for o in ops] == [('replace', 0, 1, 1), ('replace', 2, 3, 1), ('insert', 149, 149, 19)], str([(o[0], o[1], o[2], o[3], o[4]) for o in ops]))
reg = open(os.path.join(REPO, 'saida', 'pacote', 'contrato_v1_2_6_2026-10-18.md'), encoding='utf-8').read()
chk('(2)', 'registro contrato_v1_2_6_2026-10-18.md com os SHA antes (10eac696…) e depois (%s…)' % sha(ctr)[:8], sha(ctr) in reg and '10eac696dbb83049ba12ee793ff4991a1884094b7b88cdaf39f10a3fcc33660e' in reg)
# ------------------------------------------------------------------ (3) testes negativos
def roda_validate(pj, pe):
    return subprocess.run([sys.executable, '-I', '-B', os.path.join(HERE, '_run.py'), 'validate_v19.py', pj, pe], capture_output=True, text=True).returncode
with tempfile.TemporaryDirectory() as td:
    pj, pe = os.path.join(td, 'p.json'), os.path.join(td, 'e.json')
    def grava(P, E):
        open(pj, 'w', encoding='utf-8').write(j(P)); open(pe, 'w', encoding='utf-8').write(j(E))
    grava(P19, E19)
    chk('(3)', 'controle: validate_v19.py sobre cópias sem mutação sai 0', roda_validate(pj, pe) == 0)
    MUT = []
    def m1(P, E): [i for i in P['itens'] if i['id'] == 'L2-R05'][0]['gabarito'] = 'C'
    def m2(P, E): P['itens'][-1]['nucleo'] = True
    def m3(P, E): P['itens'].pop(300)
    def m4(P, E): [i for i in P['itens'] if i['id'] == 'L3-R01'][0]['aderencia'] = 'direta'
    def m5(P, E): [i for i in P['itens'] if i['id'] == 'L2-R18'].__getitem__(0).pop('volatil')
    def m6(P, E): [i for i in E['itens'] if i['id'] == 'L1-R01'][0]['justificativa'] += ' Base: x.'
    def m7(P, E): [i for i in P['itens'] if i['id'] == 'L1-R03'][0]['justificativa'] += ' Base: repositório oficial.'
    for nome, f in [('gabarito de L2-R05 trocado', m1), ('campo "nucleo" acrescentado', m2), ('1 item de reforço retirado', m3), ('L3-R01 como direta', m4),
                    ('L2-R18 sem volatil', m5), ('justificativa do estudante de L1-R01 com texto novo', m6), ('justificativa de L1-R03 com a linha Base', m7)]:
        P, E = copy.deepcopy(P19), copy.deepcopy(E19); f(P, E); grava(P, E)
        chk('(3)', 'mutação "%s": validate_v19.py sai 1' % nome, roda_validate(pj, pe) == 1)
    P = copy.deepcopy(P19); P['itens'][5]['enunciado'] += ' '
    chk('(3)', 'mutação "1 espaço no enunciado de %s (item da v1.8)": a conferência (0) acusa' % P19['itens'][5]['id'], bool(diff_v18(R18, j(P).encode('utf-8'), N18, N19, 'mut')))
    E = copy.deepcopy(E19); k_ = next(k for k, i in enumerate(E['itens'][:286]) if i['justificativa']); E['itens'][k_]['justificativa'] = E['itens'][k_]['justificativa'][:-1]
    chk('(3)', 'mutação "1 caractere a menos numa justificativa da v1.8-E": a conferência (1) acusa', bool(diff_v18(E18r, j(E).encode('utf-8'), NE18, NE19, 'mut')))
# ------------------------------------------------------------------ (4) gerador e pastas intactas
G8 = os.path.join(REPO, 'saida', 'pacote', 'gerador_v1_8')
def arquivos(d): return sorted(f for f in os.listdir(d) if os.path.isfile(os.path.join(d, f)) and f != 'MANIFESTO.md')
a8, a9 = arquivos(G8), arquivos(HERE)
alter = [f for f in a8 if f in a9 and open(os.path.join(G8, f), 'rb').read() != open(os.path.join(HERE, f), 'rb').read()]
novos_g = [f for f in a9 if f not in a8]
ALT_ESP = ['estudante_gen.py', 'estudante_json.py', 'refs.py', 'rodar_tudo.sh']
NOV_ESP = ['_run.py', 'build_v19.py', 'conferencias_v19.py', 'manifesto_v1_9.py', 'reforco.py', 'reforco_marcas.py', 'registro_adendo_v19.py', 'validate_v19.py']
chk('(4)', 'v1_9 frente à v1_8 (fora de out/ e MANIFESTO.md): alterados = %s; novos = %s; nenhum retirado' % (ALT_ESP, NOV_ESP), alter == ALT_ESP and novos_g == NOV_ESP and set(a8) <= set(a9), 'alterados %s; novos %s' % (alter, novos_g))
st = subprocess.run(['git', '-C', REPO, 'status', '--porcelain', '--', 'banco', 'saida/pacote/gerador_v1_8', 'saida/estudante', 'saida/simulados', 'saida/plataforma', 'saida/treino',
                     'saida/gce/L1_reforco_onda1_v2.md', 'saida/gce/L2_reforco_onda1_v3.md', 'saida/gce/L3_reforco_onda1_v3.md', 'saida/gcb/L6_reforco_onda1_v3.md', 'saida/gbq/claude_GBQ_Registro_AUTORAL_v3.md'],
                    capture_output=True, text=True).stdout
chk('(4)', 'git status vazio em banco/, gerador_v1_8/, saida/estudante, saida/simulados, saida/plataforma, saida/treino, nos 4 arquivos finais do reforço e no registro v3', st.strip() == '', st.strip()[:300])
json.dump(dict(total=len(res), falhas=sum(not r['ok'] for r in res), res=res), open(os.path.join(OUT, 'conferencias_v19.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('%d conferências, %d falhas' % (len(res), sum(not r['ok'] for r in res)))
sys.exit(1 if any(not r['ok'] for r in res) else 0)
