# -*- coding: utf-8 -*-
"""T-67 — conferências da ocorrência v1.6 do pacote e da edição do estudante (independentes do gerador, salvo onde dito).
Lê out/pacote.json e out/estudante/ (v1.6 gerada) e compara com a v1.5 canônica lida do git (refs.py: commit a889100, SHA-256 b4bc65c7…), com a v1.4 (e9b6402, f8c0c131…) e com a v1.3 (9622604).
(0) diff v1.5 -> v1.6 do pacote.json: EXATAMENTE `nome` e `discursivas[0].comando` (só a inserção ", de até 20 linhas,": E13 da T-65, D1-T65-R2); `geradoEm` igual nas duas (2026-10-14); o resto idêntico byte a byte.
(1) diff acumulado v1.3 -> v1.6 do pacote (nome, geradoEm, `id` dos 72 pares, D1 comando, D3, D4, D5, curso do L3): os testes da v1.4 e da v1.5, com `nome`/`geradoEm` da v1.6.
(2) contrato: regras/pacote_contrato.md v1.2.3 (git a889100, be037db8…) + C-1 a C-5, lidas dos blocos literais de T66_decisoes_2026-10-14.md (seção 6.1), reconstruído por script = arquivo atual v1.2.4 (75e6a500…).
(3) edição: v1.5 -> v1.6 (README, linha 3, e DISCURSIVAS.md, só a linha do comando de D1; 15 arquivos *_itens/*_folha e DISCURSIVAS_padrao.md idênticos) e, acumulado v1.3 -> v1.6, a reconstrução exata e os testes T54-1 a T54-8; fidelidade (0 diferenças).
(4) não regressão (T57_reconciliacao, seção 3, itens 3, 5, 6 e 7): varreduras da seção 3.5 do QA R2 (com \bD-[A-Z]{2,}), exceções fechadas da R1 e REALINHA, conferências do QA da T-56, avisos do SIM-0, scripts históricos.
(5) contagens iguais às da v1.5, da v1.4, da v1.3 e da v1.2.
(6) artefatos da T-59 e da T-66: regras/importacao_erros.md v1.2 (= bloco D-T59-07 + E-1 a E-5, da T59_T60_reconciliacao, + E-6 a E-10, lidas dos blocos literais de T66_decisoes, seção 6.2; reconstruída por script) e exemplo_erros_v1.json iguais, caractere a caractere; .gitignore; validador (registro e versão mantida) sobre o exemplo; teste do validador mantido; MANIFESTO marca o registro.
(7) E13 / T-65: consolidação do L1 (Adendo 6) e GCE_Lote1_v2_CPP.md nos SHA da reconciliação da GCE; a errata consta como APLICADA no registro do gerador e confere na sync_check.
Saída: out/conferencias_v16.txt e out/conferencias_v16.json; código de saída 1 se houver falha.
Uso: python3 conferencias_v16.py [<pacote.json> <pasta_estudante>]  (padrão: out/pacote.json e out/estudante)"""
import collections, difflib, hashlib, json, os, re, sys
import refs
import estudante_marcas as em
import gce
from common import OUT, REPO as REPO_, read
from p2 import ERRATA


PAC = sys.argv[1] if len(sys.argv) > 2 else os.path.join(OUT, 'pacote.json')
EST = sys.argv[2] if len(sys.argv) > 2 else os.path.join(OUT, 'estudante')

raw16 = open(PAC, 'rb').read()
P16 = json.loads(raw16.decode('utf-8'))
raw15 = refs.git_show(refs.C_V15, refs.PACOTE)
P15 = json.loads(raw15.decode('utf-8'))
E15 = refs.estudante(refs.C_V15)
raw14 = refs.git_show(refs.C_V14, refs.PACOTE)
P14 = json.loads(raw14.decode('utf-8'))
E14 = refs.estudante(refs.C_V14)
raw13 = refs.git_show(refs.C_V13, refs.PACOTE)
P13 = json.loads(raw13.decode('utf-8'))
raw12 = refs.git_show(refs.C_V12, refs.PACOTE)
P12 = json.loads(raw12.decode('utf-8'))
E13 = refs.estudante(refs.C_V13)
E12 = refs.estudante(refs.C_V12)
E16 = {f: open(os.path.join(EST, f), encoding='utf-8').read() for f in sorted(os.listdir(EST))}
def manifesto(E): return hashlib.sha256(''.join('%s  %s\n' % (hashlib.sha256(tx.encode('utf-8')).hexdigest(), f) for f, tx in sorted(E.items())).encode('utf-8')).hexdigest()

res = []
def chk(c, alvo, ok, detalhe=''):
    res.append((c, alvo, bool(ok), detalhe))
    print(('OK    ' if ok else 'FALHA ') + c + ' | ' + alvo + (' | ' + detalhe if detalhe else ''))

chk('BASE', 'v1.4 (git %s) tem SHA-256 f8c0c131f16dab52b1646b3d302670a3afc498b23ac03a7b34a8ff97520ffa54, 621744 bytes, e a edição v1.4 tem 43 arquivos com manifesto ordenado 562c51398d1e64f8' % refs.C_V14,
    hashlib.sha256(raw14).hexdigest() == 'f8c0c131f16dab52b1646b3d302670a3afc498b23ac03a7b34a8ff97520ffa54' and len(raw14) == 621744 and len(E14) == 43 and manifesto(E14)[:16] == '562c51398d1e64f8',
    'v1.4 %s | edição v1.4 %s' % (hashlib.sha256(raw14).hexdigest()[:12], manifesto(E14)[:16]))
chk('BASE', 'v1.3 (git %s) tem SHA-256 fdcb7afdb4fb449229c6d530e877d839f8d334cd9667731e1b7222c9c7fb0eca, 620956 bytes, e a edição v1.3 tem 43 arquivos com manifesto ordenado 6a60f28116d9ec35' % refs.C_V13,
    hashlib.sha256(raw13).hexdigest() == 'fdcb7afdb4fb449229c6d530e877d839f8d334cd9667731e1b7222c9c7fb0eca' and len(raw13) == 620956 and len(E13) == 43 and manifesto(E13)[:16] == '6a60f28116d9ec35',
    'v1.3 %s | v1.6 %s' % (hashlib.sha256(raw13).hexdigest()[:12], hashlib.sha256(raw16).hexdigest()[:12]))
chk('BASE', 'v1.5 (git %s) tem SHA-256 b4bc65c7c5829994856665ae895f9b188be8167d5b78786819ea6cdeb97beef3, 621887 bytes, e a edição v1.5 tem 43 arquivos com manifesto ordenado 656e60e5085f3622; é o commit em que o pacote v1.5 foi gerado (referência de "Fontes frente à v1.5", T66_decisoes 7.1.1)' % refs.C_V15,
    hashlib.sha256(raw15).hexdigest() == 'b4bc65c7c5829994856665ae895f9b188be8167d5b78786819ea6cdeb97beef3' and len(raw15) == 621887 and len(E15) == 43 and manifesto(E15)[:16] == '656e60e5085f3622',
    'v1.5 %s | edição v1.5 %s' % (hashlib.sha256(raw15).hexdigest()[:12], manifesto(E15)[:16]))

# ======================================================================= (1) diff do pacote v1.3 -> v1.4
def walk_diff(a, b, path, out):
    if type(a) != type(b):
        out.append((path, 'tipo', a, b)); return
    if isinstance(a, dict):
        for k in a:
            if k not in b: out.append((path + '.' + k, 'removido', a[k], None))
            else: walk_diff(a[k], b[k], path + '.' + k, out)
        for k in b:
            if k not in a: out.append((path + '.' + k, 'acrescentado', None, b[k]))
    elif isinstance(a, list):
        if len(a) != len(b): out.append((path, 'tamanho', len(a), len(b))); return
        for i, (x, y) in enumerate(zip(a, b)): walk_diff(x, y, '%s[%d]' % (path, i), out)
    elif a != b:
        out.append((path, 'valor', a, b))
# Textos da T-64, escritos aqui como literais (decisão D1-T64-5 da GCE e linha T-64 de TAREFAS.md) e conferidos contra os arquivos de padrões (leitura independente do p2.py).
N2_ANT = 'Nota (edital, 9.8.5.1, d): NQ = NC − 3 × NE ÷ TL.'
N2_NOVA = 'Nota (edital, 9.8.5.2, d): NPT = NC − 6 × NE ÷ TL.'
R6_ANT = 'Os aspectos enumerados valem como padrão de resposta, com as bases normativas indicadas em cada um. Nota: NQ = NC − 3 × NE ÷ TL. O peso de cada quesito é HIPÓTESE do Projeto, alinhada à soma oficial.'
R6_NOVA = ('Os aspectos enumerados valem como padrão de resposta, com as bases normativas indicadas em cada um. Nota: questão: NQ = NC − 3 × NE ÷ TL (9.8.5.1, d); peça: NPT = NC − 6 × NE ÷ TL (9.8.5.2, d). '
           'O peso de cada quesito é HIPÓTESE do Projeto, alinhada à soma oficial.')
pad2_ln = read('saida/gce/GCE_Lote2_padroes_GCE.md').split('\n')
pad3_ln = read('saida/gce/GCE_Lote3_padroes_GCE.md').split('\n')
k6 = next(k for k, l in enumerate(pad3_ln) if l.startswith('R6. '))
k6b = next(k for k in range(k6, len(pad3_ln)) if not pad3_ln[k].strip())
r6_arq = ' '.join(l.strip() for l in pad3_ln[k6:k6b])[len('R6. '):]
n2_arq = [l for l in pad2_ln[:next(k for k, l in enumerate(pad2_ln) if l.startswith('FIM DOS PADRÕES'))] if l.startswith('Nota (edital,')]
chk('(1) T-64', 'os literais da T-64 conferem com os arquivos de padrões: Lote 2 (f), linha da nota = "%s" (1 linha, antes de "FIM DOS PADRÕES"); Lote 3, R6 (linhas %d–%d, unidas por espaço, sem recuo e sem o rótulo "R6. ") = a R6 corrigida' % (N2_NOVA, k6 + 1, k6b),
    n2_arq == [N2_NOVA] and pad2_ln[158] == N2_NOVA and r6_arq == R6_NOVA and R6_NOVA != R6_ANT and k6b - k6 == 4,
    'Lote 2 linha 159; Lote 3 R6 linhas %d–%d' % (k6 + 1, k6b))
# ======================================================================= (0) diff v1.5 -> v1.6 do pacote (T-67: nome e E13 da T-65; D1-T65-R2)
nz = lambda s: re.sub(r'\s+', ' ', s)
NOME15, NOME16 = 'Câmara 2026 — pacote F4 (v1.5)', 'Câmara 2026 — pacote F4 (v1.6)'
# E13: X e Y escritos aqui como literais (D1-T65-R2 da GCE e linha T-65 de TAREFAS.md) e conferidos contra o Adendo 6 da consolidação (leitura independente do p2.py)
E13_X = 'redija texto dissertativo em que você'
E13_Y = 'redija texto dissertativo, de até 20 linhas, em que você'
cons1_raw = read('saida/gce/GCE_Lote1_consolidacao_GCE.md')
v2cpp_raw = read('saida/gce/GCE_Lote1_v2_CPP.md')
ad6 = nz(cons1_raw)[nz(cons1_raw).index('ADENDO 6 GCE'):]
m13 = re.findall(r'onde se lê "([^"]+)", leia-se "([^"]+)"', ad6)
chk('(0) E13', 'literais da E13 = os do Adendo 6 de GCE_Lote1_consolidacao_GCE.md ("onde se lê" X, "leia-se" Y; 1 par); X ocorre 1 vez em GCE_Lote1_v2_CPP.md (enunciado (e), comando da D1) e Y nenhuma; o arquivo do lote (v2_CPP) fica intacto',
    m13 == [(E13_X, E13_Y)] and nz(v2cpp_raw).count(E13_X) == 1 and nz(v2cpp_raw).count(E13_Y) == 0
    and hashlib.sha256(v2cpp_raw.encode('utf-8')).hexdigest() == '5ac069292b122defe859064f25cf99a8aec189991cd19b703086cd9a06553228' and len(v2cpp_raw.encode('utf-8')) == 42195)
dif0 = []
walk_diff(P15, P16, '', dif0)
chk('(0) DIFF v1.5->v1.6', 'diff estrutural v1.5 (git %s) -> v1.6 do pacote: exatamente 2 diferenças, `$.nome` e `$.discursivas[0].comando` (D1); `$.geradoEm` não difere (2026-10-14 nas duas); qualquer outra = falha (D-V16-ESCOPO, item 7; D1-T65-R2)' % refs.C_V15,
    sorted((d[0], d[1]) for d in dif0) == sorted([('.nome', 'valor'), ('.discursivas[0].comando', 'valor')]) and P16['discursivas'][0]['id'] == 'D1' and P15['geradoEm'] == P16['geradoEm'] == '2026-10-14',
    'diferenças: %s' % [d[0] for d in dif0])
chk('(0) DIFF v1.5->v1.6', '`nome`: "%s" -> "%s"; `geradoEm` "2026-10-14" nas duas; `versao` 1 nas duas; chaves de topo e sua ordem iguais' % (NOME15, NOME16),
    P15['nome'] == NOME15 and P16['nome'] == NOME16 and P15['versao'] == P16['versao'] == 1 and list(P15.keys()) == list(P16.keys()))
s16 = raw16.decode('utf-8'); s15 = raw15.decode('utf-8')
def avanca(t):
    """v1.5 -> v1.6 por substituição de texto (a única reconstrução esperada): nome (1x) e a E13 no comando da D1 (X 1x no texto do JSON)"""
    assert t.count('"nome": "%s"' % NOME15) == 1 and t.count(E13_X) == 1 and t.count(E13_Y) == 1
    return t.replace('"nome": "%s"' % NOME15, '"nome": "%s"' % NOME16, 1).replace(E13_X, E13_Y, 1)
l15_, l16_ = s15.split('\n'), s16.split('\n')
difl = [(k + 1, x, y) for k, (x, y) in enumerate(zip(l15_, l16_)) if x != y]
ins = ', de até 20 linhas,'
chk('(0) DIFF v1.5->v1.6', 'byte a byte: aplicando à v1.5 só as 2 trocas de texto (`nome` [1x] e X -> Y no comando da D1 [1x]) obtém-se a v1.6 (%d bytes; v1.5: 621887; +%d bytes = os %d bytes da inserção "%s"); %d linhas diferentes (linhas %s do JSON: a de `nome` e a do `comando` de D1); serialização json.dumps(indent=1, ensure_ascii=False) + "\\n"' % (len(raw16), len(raw16) - len(raw15), len(ins.encode('utf-8')), ins, len(difl), [d[0] for d in difl]),
    avanca(s15).encode('utf-8') == raw16 and len(l15_) == len(l16_) and len(difl) == 2 and len(raw16) - len(raw15) == len(ins.encode('utf-8')) and json.dumps(P16, ensure_ascii=False, indent=1) + '\n' == s16)
d15_ = {d['id']: d for d in P15['discursivas']}; d16_ = {d['id']: d for d in P16['discursivas']}
chk('(0) DIFF v1.5->v1.6', 'D1: comando v1.6 = comando v1.5 com UMA troca (X -> Y; a inserção "%s" depois de "dissertativo"); id, tipo, aspectos, padrao e quesitos da D1 idênticos aos da v1.5 (0 aspecto, quesito, valor, padrão ou gabarito alterado); D2, D3, D4 e D5 idênticas, inteiras; ordem das chaves igual' % ins,
    d16_['D1']['comando'] == d15_['D1']['comando'].replace(E13_X, E13_Y) and d15_['D1']['comando'].count(E13_X) == 1 and d16_['D1']['comando'].count(E13_Y) == 1 and d16_['D1']['comando'].count(E13_X) == 0
    and {k: v for k, v in d15_['D1'].items() if k != 'comando'} == {k: v for k, v in d16_['D1'].items() if k != 'comando'} and all(d15_[x] == d16_[x] for x in ('D2', 'D3', 'D4', 'D5')) and list(d15_) == list(d16_) and all(list(d15_[x].keys()) == list(d16_[x].keys()) for x in d15_))
chk('(0) DIFF v1.5->v1.6', 'valores e aspectos da D1 iguais (soma de `aspectos[].valor` por discursiva: D1 %s, D2 %s, D3 %s, D4 %s, D5 %s, as mesmas da v1.5)' % tuple(round(sum(a['valor'] or 0 for a in d16_[x]['aspectos']), 2) for x in ('D1', 'D2', 'D3', 'D4', 'D5')),
    all(round(sum(a['valor'] or 0 for a in d16_[x]['aspectos']), 2) == round(sum(a['valor'] or 0 for a in d15_[x]['aspectos']), 2) for x in d15_) and [len(d16_[x]['aspectos']) for x in d16_] == [len(d15_[x]['aspectos']) for x in d15_] and [len(d16_[x]['quesitos']) for x in d16_] == [len(d15_[x]['quesitos']) for x in d15_])
n20 = {d['id']: d['comando'].count('20 linhas') for d in P16['discursivas']}
chk('(0) DIFF v1.5->v1.6', 'estado esperado (D1-T65-R2): "20 linhas" nos comandos D1 1, D2 1, D3 0, D4 1, D5 0 (v1.5: D1 0, D2 1, D3 0, D4 1, D5 0); no pacote inteiro X 0 e Y 2 (D1 e D2); "Redija texto dissertativo, de até 20 linhas" 1 vez (D4)',
    n20 == {'D1': 1, 'D2': 1, 'D3': 0, 'D4': 1, 'D5': 0} and {d['id']: d['comando'].count('20 linhas') for d in P15['discursivas']} == {'D1': 0, 'D2': 1, 'D3': 0, 'D4': 1, 'D5': 0}
    and s16.count(E13_X) == 0 and s16.count(E13_Y) == 2 and s16.count('Redija texto dissertativo, de até 20 linhas') == 1, str(n20))
chk('(0) DIFF v1.5->v1.6', 'itens (286), simulados (4), lotes (10) e edital (47) idênticos aos da v1.5; discursivas (5): só o comando da D1 difere',
    P15['itens'] == P16['itens'] and P15['simulados'] == P16['simulados'] and P15['lotes'] == P16['lotes'] and P15['edital'] == P16['edital']
    and (len(P16['itens']), len(P16['simulados']), len(P16['lotes']), len(P16['discursivas']), len(P16['edital'])) == (286, 4, 10, 5, 47))
cnt16 = lambda t: [d['id'] for d in P16['discursivas'] if t in d['padrao']]
chk('(1) T-64', 'estado esperado da GCE (D1-T64-5) em `discursivas[*].padrao`, mantido na v1.6: "NQ = NC − 3 × NE ÷ TL" em D1, D4 e D5 (3); "NPT = NC − 6 × NE ÷ TL" em D3, D4 e D5 (3); "NQ = NC" em D3: 0; D2 sem nota de fórmula; "9.8.5.1, d" com NQ em D3: 0',
    cnt16('NQ = NC − 3 × NE ÷ TL') == ['D1', 'D4', 'D5'] and cnt16('NPT = NC − 6 × NE ÷ TL') == ['D3', 'D4', 'D5'] and 'NQ = NC' not in d16_['D3']['padrao'] and 'NE ÷ TL' not in d16_['D2']['padrao'] and '9.8.5.1' not in d16_['D3']['padrao']
    and 'NQ = NC' in d16_['D1']['padrao'] and '(9.8.5.1, d)' in d16_['D4']['padrao'] and '(9.8.5.2, d)' in d16_['D5']['padrao'])

# ======================================================================= (1) diff acumulado v1.3 -> v1.6 (testes da v1.4, com nome e geradoEm da v1.6)
dif = []
walk_diff(P13, P16, '', dif)
def nome_caminho(p):
    m = re.match(r'^\.(lotes|simulados|discursivas)\[(\d+)\](.*)$', p)
    if m: return '%s[%s]%s' % (m.group(1), P16[m.group(1)][int(m.group(2))]['id'], m.group(3))
    return p
dif_n = sorted((nome_caminho(d[0]), d[1]) for d in dif)
ID_LOTES = {'L4': 20, 'L5': 15, 'L6A': 19, 'L6B': 18}
esperado = sorted([('.nome', 'valor'), ('.geradoEm', 'valor'), ('discursivas[D3].padrao', 'valor'), ('discursivas[D4].padrao', 'valor'), ('discursivas[D5].padrao', 'valor'), ('discursivas[D1].comando', 'valor'), ('lotes[L3].curso', 'valor')] +
                  [('lotes[%s].pares[%d].id' % (lid, k), 'acrescentado') for lid, n in ID_LOTES.items() for k in range(n)])
chk('(1) DIFF', 'v1.3 -> v1.6 (acumulado) do pacote: só nome (valor), geradoEm (valor: 2026-10-13 -> 2026-10-14), `id` em 72 pares (acrescentado), comando da D1 (valor; E13 da T-65), padrao da D3, da D4 e da D5 (valor) e curso do L3 (valor); qualquer outra diferença = falha',
    dif_n == esperado and P13['geradoEm'] == '2026-10-13' and P16['geradoEm'] == '2026-10-14', 'diferenças: %d (1 nome + 1 geradoEm + 72 id + 1 comando D1 (E13) + 3 padrao D3/D4/D5 + 1 curso L3)' % len(dif_n))
nome_d = [d for d in dif if d[0] == '.nome'][0]
chk('(1) DIFF', 'nome: "%s" -> "%s"; versao 1 nas duas' % (nome_d[2], nome_d[3]), nome_d[2] == 'Câmara 2026 — pacote F4 (v1.3)' and nome_d[3] == 'Câmara 2026 — pacote F4 (v1.6)' and P13['versao'] == P16['versao'] == 1)
# `id` de par: 72 entradas, primeira chave, igual ao rótulo do arquivo canônico (leitura independente)
CANON = {'L4': 'saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md', 'L5': 'saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md', 'L6A': 'saida/gcb/GCB_Lote6a_v2_producao_auto.md', 'L6B': 'saida/gcb/GCB_Lote6b_v2_producao_auto.md'}
def canon_gcb(lid):
    ln = read(CANON[lid]).split('\n')
    c0 = next(i for i, l in enumerate(ln) if l.startswith('(c) PARES'))
    e2 = next(i for i in range(c0, len(ln)) if ln[i].startswith('FIM DA PARTE 2/3'))
    return [(m.group(1), m.group(2)) for m in (re.match(r'^(C\d+)\.\s+(.*)$', l) for l in ln[c0 + 1:e2]) if m]
LB15 = {l['id']: l for l in P16['lotes']}; LB13 = {l['id']: l for l in P13['lotes']}
okid = True; detid = []
for lid, n in ID_LOTES.items():
    can = canon_gcb(lid)
    ids = [p['id'] for p in LB15[lid]['pares']]
    ok = len(ids) == n == len(can) and ids == [c[0] for c in can] == ['C%d' % k for k in range(1, n + 1)] and all(list(p.keys()) == ['id', 'a', 'b', 'como'] for p in LB15[lid]['pares'])
    # a/b/como iguais aos da v1.3, par a par; e o texto do rótulo canônico é "<id>. a × b | como" (junção)
    ok = ok and all({k: v for k, v in p.items() if k != 'id'} == q for p, q in zip(LB15[lid]['pares'], LB13[lid]['pares']))
    okid &= ok; detid.append('%s %d %s' % (lid, len(ids), 'ok' if ok else 'FALHA'))
chk('(1) DIFF', 'cada `id` de par (72) é o rótulo "C<n>." da seção (c) do canônico do lote, na ordem (L4 C1–C20, L5 C1–C15, L6A C1–C19, L6B C1–C18), é a primeira chave, e a/b/como são idênticos aos da v1.3', okid, ', '.join(detid))
chk('(1) DIFF', 'L1, L1C, L2 e L3 sem `id` (0 de 67 pares); L4C e L5C sem pares', all('id' not in p for l in P16['lotes'] if l['id'] not in ID_LOTES for p in l['pares']) and sum(len(l['pares']) for l in P16['lotes'] if l['id'] not in ID_LOTES) == 67 and not LB15['L4C']['pares'] and not LB15['L5C']['pares'])
ref = {('L5', 'C1'): ('Histograma', 'gráfico de barras'), ('L5', 'C14'): ('Storytelling', 'dashboard'), ('L4', 'C19'): ('Injeção de prompt', 'jailbreak (conceitos gerais)')}
chk('(1) DIFF', 'remissões: L5 C1 = Histograma × gráfico de barras; L5 C14 = Storytelling × dashboard; L4 C19 = Injeção de prompt × jailbreak (conceitos gerais)',
    all(any(p['id'] == k[1] and (p['a'], p['b']) == v for p in LB15[k[0]]['pares']) for k, v in ref.items()))
# curso do L3: uma troca
a13, a14 = LB13['L3']['curso'], LB15['L3']['curso']
OLD, NEW = 'jurisprudência firmada que eu possa afirmar):', 'jurisprudência firmada que se possa afirmar):'
chk('(1) DIFF', 'curso do L3: igual ao da v1.3 com UMA troca ("eu" -> "se" em "jurisprudência firmada que eu possa afirmar):"); 0 "que eu possa afirmar" no pacote', a13.count(OLD) == 1 and a14 == a13.replace(OLD, NEW) and 'que eu possa afirmar' not in raw16.decode('utf-8') and a14.count(NEW) == 1,
    'caracteres %d -> %d' % (len(a13), len(a14)))
canon3 = read('saida/gce/GCE_Lote3_v2_CPP.md')
nz = lambda s: re.sub(r'\s+', ' ', s)
chk('(1) DIFF', 'o canônico atual do L3 (GCE_Lote3_v2_CPP.md, T-58) traz a errata no curso (1x) e o registro "T-54" na Tabela de Correções; o curso do pacote = curso lido do canônico (sem outra mudança desde a v1.3)',
    nz(canon3).count(NEW) == 1 and nz(canon3).count('"que eu possa afirmar" → "que se possa afirmar"') == 1 and nz(canon3).count('T-54 → (a), 4.2, bloco "CONTROVERSO / NÃO GABARITO"') == 1)
# D5
d13 = {d['id']: d for d in P13['discursivas']}; d14 = {d['id']: d for d in P16['discursivas']}
pad = read('saida/gce/GCE_Lote3_padroes_GCE.md').split('\n')
r2 = '\n'.join(l.rstrip() for l in pad[13:20])      # linhas 14–20: nota R2
r34 = '\n'.join(l.rstrip() for l in pad[20:23])     # linhas 21–23: notas R3 e R4
p13, p14 = d13['D5']['padrao'].replace(R6_ANT, R6_NOVA), d14['D5']['padrao']      # a troca da R6 (T-64) é conferida em (0); aqui só o que a T-54 mudou
assert d13['D5']['padrao'].count(R6_ANT) == 1
anexo13 = 'Notas de correção (GCE, R2–R4)\n' + r2 + '\n' + r34
anexo14 = 'Notas de correção (GCE, R3–R4)\n' + r34
chk('(1) DIFF', 'D5: padrao v1.6 = padrao v1.3 (com a R6 trocada pela da T-64) sem o trecho literal da nota R2 (linhas 14–20 de GCE_Lote3_padroes_GCE.md, 7 linhas) e com o rótulo "Notas de correção (GCE, R3–R4)"; anexo v1.4 = linhas 21–23 literais; comando, aspectos e quesitos da D5 iguais',
    p13.endswith(anexo13) and p14 == p13[:len(p13) - len(anexo13)] + anexo14 and 'R2.' not in p14 and 'Alínea c da discursiva' not in p14 and r2.count('\n') == 6 and {k: v for k, v in d13['D5'].items() if k != 'padrao'} == {k: v for k, v in d14['D5'].items() if k != 'padrao'})
chk('(1) DIFF', 'D4: igual à da v1.3 salvo a troca da R6 (T-64); padrao com o anexo R2–R4 (linhas 14–23 literais) e rótulo "Notas de correção (GCE, R2–R4)"; D2 idêntica; D1 igual à da v1.3 salvo o comando (E13, T-65); D3 igual à da v1.3 salvo a troca da nota da peça (T-64)',
    {k: v for k, v in d13['D4'].items() if k != 'padrao'} == {k: v for k, v in d14['D4'].items() if k != 'padrao'} and d14['D4']['padrao'] == d13['D4']['padrao'].replace(R6_ANT, R6_NOVA) and d13['D4']['padrao'].count(R6_ANT) == 1
    and d14['D4']['padrao'].endswith('Notas de correção (GCE, R2–R4)\n' + r2 + '\n' + r34) and d13['D2'] == d14['D2'] and {k: v for k, v in d13['D1'].items() if k != 'comando'} == {k: v for k, v in d14['D1'].items() if k != 'comando'} and d14['D1']['comando'] == d13['D1']['comando'].replace(E13_X, E13_Y) and d14['D3']['padrao'] == d13['D3']['padrao'].replace(N2_ANT, N2_NOVA) and {k: v for k, v in d13['D3'].items() if k != 'padrao'} == {k: v for k, v in d14['D3'].items() if k != 'padrao'})
def ordem_chaves(P):
    return [list(P.keys())] + [list(i.keys()) for i in P['itens']] + [list(l.keys()) for l in P['lotes']] + [list(p.keys()) for l in P['lotes'] for p in l['pares']] + [list(s.keys()) for s in P['simulados']] + [list(d.keys()) for d in P['discursivas']]
oc13 = ordem_chaves(P13); oc14 = [[k for k in ks if k != 'id'] if ks[:2] == ['id', 'a'] else ks for ks in ordem_chaves(P16)]
chk('(1) DIFF', 'ordem das chaves: as mesmas da v1.3, salvo `id` como primeira chave dos 72 pares', oc13 == oc14)
chk('(1) DIFF', 'serialização: indent=1, ensure_ascii=False, newline final; 286 itens idênticos (enunciado, comando, comandoOriginal, textoBase, gabarito, justificativa, itemEdital, aderencia, volatil, nota); simulados idênticos', json.dumps(P16, ensure_ascii=False, indent=1) + '\n' == raw16.decode('utf-8')
    and P13['itens'] == P16['itens'] and len(P16['itens']) == 286 and P13['simulados'] == P16['simulados'] and P13['edital'] == P16['edital'])

# ======================================================================= (2) contrato v1.2.3 -> v1.2.4 (T-66; T66_decisoes_2026-10-14.md, seção 6.1: C-1 a C-5)
t66 = read('saida/pacote/T66_decisoes_2026-10-14.md')
def blocos_t66(ini, fim, prefixo):
    """{rótulo: (onde se lê, leia-se)} lidos dos blocos de quatro crases (````text) da seção, sem a quebra de linha que precede a cerca de fechamento"""
    sec = t66[t66.index(ini):t66.index(fim)]
    out = collections.OrderedDict()
    for m in re.finditer(r'#### (%s-\d+)\n\nOnde se lê:\n\n````text\n(.*?)\n````\n\nLeia-se:\n\n````text\n(.*?)\n````' % prefixo, sec, re.S):
        out[m.group(1)] = (m.group(2), m.group(3))
    return out
def aplica_em_ordem(base, pares):
    """aplica as substituições na ordem; devolve (texto, [ocorrências de cada 'onde se lê' no estado anterior à troca])"""
    t, occ = base, []
    for a, b in pares:
        occ.append(t.count(a))
        if t.count(a) == 1: t = t.replace(a, b)
    return t, occ
CT = blocos_t66('### 6.1 Contrato', '### 6.2 Regra', 'C')
ctr_antes = refs.git_show(refs.C_V15, 'regras/pacote_contrato.md').decode('utf-8')
ctr_depois = read('regras/pacote_contrato.md')
ctr_rec, occ_c = aplica_em_ordem(ctr_antes, list(CT.values()))
LA, LD = ctr_antes.split('\n'), ctr_depois.split('\n')
ops = [o for o in difflib.SequenceMatcher(None, LA, LD, autojunk=False).get_opcodes() if o[0] != 'equal']
chk('(2) CONTRATO v1.2.4', 'base: regras/pacote_contrato.md v1.2.3 (git %s) tem SHA-256 be037db8e7c06e1ae2276f16063ed4b752ef0865a9141511d0e353d642965240, 30385 bytes e 135 linhas; C-1 a C-5 lidas dos blocos literais da seção 6.1 de T66_decisoes (5 pares, na ordem)' % refs.C_V15,
    hashlib.sha256(ctr_antes.encode('utf-8')).hexdigest() == 'be037db8e7c06e1ae2276f16063ed4b752ef0865a9141511d0e353d642965240' and len(ctr_antes.encode('utf-8')) == 30385 and ctr_antes.count('\n') == 135 and list(CT) == ['C-1', 'C-2', 'C-3', 'C-4', 'C-5'])
chk('(2) CONTRATO v1.2.4', 'cada "onde se lê" de C-1 a C-5 ocorre exatamente 1 vez no estado anterior à troca (aplicadas em ordem): %s' % occ_c, occ_c == [1, 1, 1, 1, 1])
chk('(2) CONTRATO v1.2.4', 'regras/pacote_contrato.md (arquivo atual) é igual, caractere a caractere, à v1.2.3 com C-1 a C-5 aplicadas, reconstruído por script: SHA-256 75e6a5009be70f5be3cb3e7b9b5087b96086a0884831419d6818fa27babdb27e, 32266 bytes, 143 linhas; sem BOM nem CR',
    ctr_rec == ctr_depois and hashlib.sha256(ctr_depois.encode('utf-8')).hexdigest() == '75e6a5009be70f5be3cb3e7b9b5087b96086a0884831419d6818fa27babdb27e' and len(ctr_depois.encode('utf-8')) == 32266 and ctr_depois.count('\n') == 143 and '\r' not in ctr_depois and not ctr_depois.startswith('﻿'),
    'SHA-256 %s' % hashlib.sha256(ctr_depois.encode('utf-8')).hexdigest()[:12])
chk('(2) CONTRATO v1.2.4', 'diff linha a linha v1.2.3 -> v1.2.4: 4 linhas trocadas (1, 3, 110 e 112) e 8 inseridas depois da linha 129 (C-5; o difflib ancora o bloco inserido depois da linha em branco 130, pois o bloco da C-5 termina e começa com linha em branco); 0 outra linha alterada',
    [(o[0], o[1] + 1, o[2], o[4] - o[3]) for o in ops][:4] == [('replace', 1, 1, 1), ('replace', 3, 3, 1), ('replace', 110, 110, 1), ('replace', 112, 112, 1)] and len(ops) == 5 and ops[4][0] == 'insert' and ops[4][4] - ops[4][3] == 8 and ops[4][1] in (129, 130) and len(LD) - len(LA) == 8,
    'operações: ' + '; '.join('%s antes[%d:%d] depois[%d:%d]' % o for o in ops))
chk('(2) CONTRATO v1.2.4', 'linha 1 = "# pacote.json — contrato de dados entre a fábrica e a plataforma (v1.2.4, 2026-10-14)" (0 "v1.2.3" na linha 1); a seção "Errata de forma da v1.2.4 (T-66;" existe 1 vez; a linha 3 cita a v1.2.4 e remete à seção',
    LD[0] == '# pacote.json — contrato de dados entre a fábrica e a plataforma (v1.2.4, 2026-10-14)' and ctr_depois.count('Errata de forma da v1.2.4 (T-66;') == 1 and 'ver a seção "Errata de forma da v1.2.4".' in LD[2] and 'v1.2.3' not in LD[0])
def fence_json(txt): return re.search(r'```json\n(.*?)\n```', txt, re.S).group(1)
chk('(2) CONTRATO v1.2.4', 'nenhum campo obrigatório mudou: exemplo JSON, parágrafo "Regras:" (campos obrigatórios), Regras da v1.1, v1.1.1 e v1.2 (até a "Errata de forma da v1.2.1"), seção da v1.2.1, v1.2.2 e v1.2.3, tabela de fonte e PROMPT DE PARTIDA idênticos, salvo as 4 linhas trocadas; `versao` continua 1; a errata diz que não muda nome, tipo nem obrigatoriedade de nenhum campo do `pacote.json` e não muda `versao` nem `versaoFormato`',
    fence_json(ctr_antes) == fence_json(ctr_depois) and '"versao": 1' in fence_json(ctr_depois) and [l for l in LA if l.startswith('Regras: `gabarito`')] == [l for l in LD if l.startswith('Regras: `gabarito`')] != []
    and ctr_antes[ctr_antes.index('Regras da v1.1 (T-26):'):ctr_antes.index('Errata de forma da v1.2.3 (T-59;')] == ctr_depois[ctr_depois.index('Regras da v1.1 (T-26):'):ctr_depois.index('Errata de forma da v1.2.3 (T-59;')]
    and 'Esta errata não muda nome, tipo nem obrigatoriedade de nenhum campo do `pacote.json` e não muda `versao` (continua 1; regra (g) da v1.2). No arquivo de exportação de erros, não muda `versaoFormato` (continua 1)' in ctr_depois)
reg_c = open(os.path.join(REPO_, 'saida', 'pacote', 'contrato_v1_2_4_2026-10-14.md'), encoding='utf-8').read()
chk('(2) CONTRATO v1.2.4', 'o registro saida/pacote/contrato_v1_2_4_2026-10-14.md existe e traz o SHA-256 antes (be037db8…) e depois (75e6a500…)', 'be037db8e7c06e1ae2276f16063ed4b752ef0865a9141511d0e353d642965240' in reg_c and '75e6a5009be70f5be3cb3e7b9b5087b96086a0884831419d6818fa27babdb27e' in reg_c)
CAMPOS = ['id', 'rotulo', 'certame', 'cargo', 'ano', 'numero', 'comando', 'textoBase', 'enunciado', 'gabarito', 'justificativa', 'itemEdital', 'aderencia', 'url']
chk('(2) CONTRATO v1.2.4', 'o pacote v1.6 cumpre os 14 campos obrigatórios de item e as chaves de topo do contrato (o exemplo JSON do contrato não mudou): 286/286 itens com os 14 campos; chaves de topo = versao, geradoEm, nome, edital, itens, simulados, lotes, discursivas',
    all(all(k in i for k in CAMPOS) for i in P16['itens']) and list(P16.keys()) == ['versao', 'geradoEm', 'nome', 'edital', 'itens', 'simulados', 'lotes', 'discursivas'])
t59 = read('saida/pacote/T59_decisoes_2026-10-14.md').split('\n')
def bloco_apos(prefixo, cerca):
    i = next(k for k, l in enumerate(t59) if l.startswith(prefixo))
    a = next(k for k in range(i, len(t59)) if t59[k].startswith(cerca)); b = t59.index('```', a + 1)
    return t59[a + 1:b]

# ======================================================================= (3a) edição v1.5 -> v1.6 (D-V16-ESCOPO, item 7; D1-T65-R2)
chk('(3) EDIÇÃO v1.5->v1.6', 'mesmos 43 nomes de arquivo; 41 arquivos idênticos byte a byte aos da v1.5; só `README.md` (versão) e `DISCURSIVAS.md` (a linha do comando de D1) diferem', sorted(E15) == sorted(E16) and len(E16) == 43 and [f for f in E16 if E15[f] != E16[f]] == ['DISCURSIVAS.md', 'README.md'], str([f for f in E16 if E15[f] != E16[f]]))
i15 = [f for f in E16 if f.endswith(('_itens.md', '_folha.md'))]
chk('(3) EDIÇÃO v1.5->v1.6', 'os %d arquivos *_itens.md (10 lotes + BANCO) e *_folha.md (4 simulados) são idênticos byte a byte aos da v1.5; `DISCURSIVAS_padrao.md` idêntico (padrão, quesitos e notas não mudam)' % len(i15),
    len(i15) == 15 and all(E15[f] == E16[f] for f in i15) and E15['DISCURSIVAS_padrao.md'] == E16['DISCURSIVAS_padrao.md'], ', '.join(i15))
dc15, dc16 = E15['DISCURSIVAS.md'].split('\n'), E16['DISCURSIVAS.md'].split('\n')
opdc = [o for o in difflib.SequenceMatcher(None, dc15, dc16, autojunk=False).get_opcodes() if o[0] != 'equal']
chk('(3) EDIÇÃO v1.5->v1.6', 'DISCURSIVAS.md: exatamente 1 linha trocada e mais nenhuma, a do comando de D1 (linha %d: "…redija texto dissertativo em que você:" -> "…redija texto dissertativo, de até 20 linhas, em que você:"), com a inserção ", de até 20 linhas," e nada mais; mesmo número de linhas (%d); as linhas dos comandos de D2 a D5 iguais' % ((opdc[0][1] + 1) if opdc else 0, len(dc16)),
    len(dc15) == len(dc16) and len(opdc) == 1 and opdc[0][0] == 'replace' and opdc[0][2] - opdc[0][1] == 1 and opdc[0][4] - opdc[0][3] == 1 and dc15[opdc[0][1]].count(E13_X) == 1 and dc16[opdc[0][3]] == dc15[opdc[0][1]].replace(E13_X, E13_Y) and E16['DISCURSIVAS.md'].count(E13_X) == 0 and E16['DISCURSIVAS.md'].count(E13_Y) == 2,
    str([(o[0], o[1] + 1, o[2]) for o in opdc]))
r15, r16 = E15['README.md'].split('\n'), E16['README.md'].split('\n')
chk('(3) EDIÇÃO v1.5->v1.6', 'README.md: só a linha 3 muda: "- Versão: v1.5 (pacote.json versão 1)" -> "- Versão: v1.6 (pacote.json versão 1)"; a linha 4 ("- Data: 2026-10-14") é igual (a data do pacote não mudou); as demais linhas idênticas',
    len(r15) == len(r16) and [k + 1 for k, (x, y) in enumerate(zip(r15, r16)) if x != y] == [3] and r15[2] == '- Versão: v1.5 (pacote.json versão 1)' and r16[2] == '- Versão: v1.6 (pacote.json versão 1)' and r15[3] == r16[3] == '- Data: 2026-10-14')
chk('(3) EDIÇÃO v1.5->v1.6', 'manifesto ordenado da edição: v1.5 656e60e5085f3622… -> v1.6 %s…' % manifesto(E16)[:16], manifesto(E15)[:16] == '656e60e5085f3622' and manifesto(E16) != manifesto(E15))

# ======================================================================= (3) edição: reconstrução exata da v1.3 -> v1.6 (acumulado; testes da v1.4)
def secao(lines, ini, fim):
    i = lines.index(ini) + 2; j = lines.index(fim) - 1
    return i, j          # linhas [i, j) são os pares (a linha em branco antes de "## Pegadinhas" fica fora)
GCB_LOTES = set(ID_LOTES)
def pares_v13(lid, lines):
    """pares da edição v1.3 (parser do formato antigo): (a, b, como) a partir de '- **a** × **b** — como'"""
    i, j = secao(lines, '## Pares', '## Pegadinhas')
    out = []
    for l in lines[i:j]:
        m = re.match(r'^- \*\*(.*?)\*\*(?: × \*\*(.*?)\*\*)?(?: — (.*))?$', l); assert m, l
        out.append(tuple(g or '' for g in m.groups()))
    return i, j, out
def reconstroi(f, tx13):
    """aplica à edição v1.3 SÓ as operações da lista PARA A T-57 e devolve o texto esperado da v1.4"""
    L = tx13.split('\n')
    m = re.match(r'^(L(?:1|2|3|4|5|6A|6B))_estudo\.md$', f)
    if m:
        lid = m.group(1)
        i, j, ps = pares_v13(lid, L)
        assert len(ps) == len(LB15[lid]['pares'])
        novas = []
        for (a, b, c), p in zip(ps, LB15[lid]['pares']):
            if lid in GCB_LOTES:
                l = '- %s. **%s**' % (p['id'], a) + (' × **%s**' % b if b else '') + ' | ' + c
            else:
                l = '- **%s**' % a + (' vs **%s**' % b if b else '') + (': ' + c if c else '.')
            novas.append(l)
        L[i:j] = novas
        if lid == 'L1':
            for _esc, antes, depois in em.REALINHA:
                assert L.count(antes) == 1
                L[L.index(antes)] = depois
        if lid == 'L3':
            assert L.count('jurisprudência firmada que eu possa afirmar):') == 1
            L[L.index('jurisprudência firmada que eu possa afirmar):')] = 'jurisprudência firmada que se possa afirmar):'
        return '\n'.join(L)
    if f in ('BANCO_itens.md', 'SIM-0_folha.md'):
        return '\n'.join(('> ' + l[len('> Nota: '):]) if l.startswith('> Nota: ') else l for l in L)
    if f in ('BANCO_gabarito.md', 'SIM-0_gabarito.md'):
        return '\n'.join(('- ' + l[len('- Nota: '):]) if l.startswith('- Nota: ') else l for l in L)
    if f == 'L6B_gabarito.md':
        a_ = 'Fonte: conceito geral (a definição da tríade não foi confirmada em fonte; ver curso 4.1.1). Tema da tríade'
        assert tx13.count(a_) == 1
        return tx13.replace(a_, 'Fonte: conceito geral. Tema da tríade')
    if f == 'SIM-1_gabarito.md':
        k = L.index('- Número de itens: 40')
        assert L[k + 1] == ''
        return '\n'.join(L[:k + 2] + [LB15['L4']['legendaMecanismo'], '', LB15['L5']['legendaMecanismo'], ''] + L[k + 2:])
    if f == 'README.md':
        assert tx13.count('- Versão: v1.3 (pacote.json versão 1)') == 1 and tx13.count('- Data: 2026-10-13') == 1
        return tx13.replace('- Versão: v1.3 (pacote.json versão 1)', '- Versão: v1.6 (pacote.json versão 1)').replace('- Data: 2026-10-13', '- Data: 2026-10-14')
    if f == 'DISCURSIVAS.md':
        # E13 (T-65): a inserção ", de até 20 linhas," no comando da D1
        assert tx13.count(E13_X) == 1
        return tx13.replace(E13_X, E13_Y)
    if f == 'DISCURSIVAS_padrao.md':
        # a D5 perde as 7 linhas da nota R2 (as mesmas da D4, que ficam)
        nr = 'Alínea c da discursiva: NÃO se exige enquadrar o'
        ks = [k for k, l in enumerate(L) if l == nr]
        assert len(ks) == 2
        k = ks[1]
        assert L[k:k + 7] == L[ks[0]:ks[0] + 7] and L[k - 1] == 'Notas de correção' and L[k + 7].startswith('Voz como dado sensível')
        u = '\n'.join(L[:k] + L[k + 7:])
        assert u.count(N2_ANT) == 1 and u.count(R6_ANT) == 2          # + as 3 notas da T-64
        return u.replace(N2_ANT, N2_NOVA).replace(R6_ANT, R6_NOVA)
    return tx13
CAND = ['BANCO_gabarito.md', 'BANCO_itens.md', 'DISCURSIVAS.md', 'DISCURSIVAS_padrao.md', 'L1_estudo.md', 'L2_estudo.md', 'L3_estudo.md', 'L4_estudo.md', 'L5_estudo.md', 'L6A_estudo.md', 'L6B_estudo.md', 'L6B_gabarito.md', 'README.md', 'SIM-0_folha.md', 'SIM-0_gabarito.md', 'SIM-1_gabarito.md']
chk('(3) EDIÇÃO', 'mesmos 43 nomes de arquivo', sorted(E13) == sorted(E16) and len(E16) == 43)
mudados = sorted(f for f in E16 if E13[f] != E16[f])
chk('(3) EDIÇÃO', 'arquivos que mudam da v1.3 para a v1.6: exatamente 16 (7 *_estudo.md com pares, BANCO_itens, BANCO_gabarito, SIM-0_folha, SIM-0_gabarito, L6B_gabarito, SIM-1_gabarito, DISCURSIVAS (E13), DISCURSIVAS_padrao, README); os outros 27 idênticos byte a byte', mudados == CAND and len(E16) - len(mudados) == 27, str(mudados))
rec_ok = []; rec_bad = []
for f in sorted(E16):
    esp = reconstroi(f, E13[f])
    (rec_ok if esp == E16[f] else rec_bad).append(f)
chk('(3) EDIÇÃO', 'reconstrução exata: aplicando à v1.3 SÓ as operações da LISTA (pares com os separadores do canônico e `id`; 2 linhas do quadro do L1; rótulo "Nota:"; 6B-06; legendas no SIM-1_gabarito; 7 linhas da D5; L3 "que se possa afirmar"; README) as 3 notas da T-64 e a E13 (T-65) o resultado é igual à v1.6 em 43/43 arquivos', not rec_bad and len(rec_ok) == 43, 'divergentes: %s' % rec_bad)
# diff linha a linha por arquivo: contagem de linhas alteradas
def linhas_diff(f):
    a, b = E13[f].split('\n'), E16[f].split('\n')
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    return [o for o in sm.get_opcodes() if o[0] != 'equal']
nlin = {f: sum(max(o[2] - o[1], o[4] - o[3]) for o in linhas_diff(f)) for f in mudados}
esperado_lin = {'L1_estudo.md': 17 + 2, 'L2_estudo.md': 22, 'L3_estudo.md': 28 + 1, 'L4_estudo.md': 20, 'L5_estudo.md': 15, 'L6A_estudo.md': 19, 'L6B_estudo.md': 18,
                'BANCO_itens.md': 2, 'BANCO_gabarito.md': 2, 'SIM-0_folha.md': 2, 'SIM-0_gabarito.md': 2, 'L6B_gabarito.md': 1, 'SIM-1_gabarito.md': 4, 'DISCURSIVAS.md': 1, 'DISCURSIVAS_padrao.md': 7 + 3, 'README.md': 2}
chk('(3) EDIÇÃO', 'linhas alteradas por arquivo (v1.3 -> v1.6): pares 139 (L1 17, L2 22, L3 28, L4 20, L5 15, L6A 19, L6B 18) + L1 quadro 2 + L3 curso 1; nota 8; 6B-06 1; SIM-1_gabarito +4; D5 -7 e 3 notas da T-64 trocadas; DISCURSIVAS 1 (E13, T-65); README 2 (versão e data; total %d)' % sum(esperado_lin.values()), nlin == esperado_lin, str(nlin))

# --- T54-3: pares (D-T54-01)
def linhas_pares(E, lid):
    L = E['%s_estudo.md' % lid].split('\n'); i, j = secao(L, '## Pares', '## Pegadinhas'); return L[i:j]
tot = 0; difs = []; cont = collections.Counter()
for lid in ['L1', 'L2', 'L3', 'L4', 'L5', 'L6A', 'L6B']:
    A, B = linhas_pares(E13, lid), linhas_pares(E16, lid)
    ids = [p.get('id') for p in LB15[lid]['pares']]
    for k, (x, y) in enumerate(zip(A, B)):
        sx, sy = x[2:].replace('**', ''), y[2:].replace('**', '')
        if lid in GCB_LOTES:
            px = ids[k] + '. ' + sx.replace(' — ', ' | ', 1)
        else:
            px = sx.replace(' × ', ' vs ', 1) if ' × ' in sx else sx
            px = px.replace(' — ', ': ', 1) if ' — ' in px else px + '.'
        tot += 1
        if px != sy: difs.append((lid, k + 1, px[:70], sy[:70]))
        cont[lid] += 1
chk('(3) T54-3', 'teste da D-T54-01: em cada linha de par, sem "- " e sem "**", a v1.4 = a v1.3 com o 1.º " × " -> " vs " e o 1.º " — " -> ": " (ou "." quando `como` vazio) nos lotes GCE, e 1.º " — " -> " | " com "{id}. " na frente nos lotes GCB: 0 diferença de caractere em %d linhas' % tot, tot == 139 and not difs, 'linhas por lote %s; diferenças %s' % (dict(cont), difs[:3]))
gce_l = [l for lid in ('L1', 'L2', 'L3') for l in linhas_pares(E16, lid)]; gcb_l = [l for lid in sorted(GCB_LOTES) for l in linhas_pares(E16, lid)]
chk('(3) T54-3', 'lotes GCE (67 linhas): 0 com "** × **"; todas casam ^- \\*\\*, e terminam em "." ou em aspas; lotes GCB (72 linhas): todas casam ^- C\\d+\\. \\*\\*, sem " — " como separador a/como na posição do canônico',
    len(gce_l) == 67 and not any('** × **' in l for l in gce_l) and all(l.startswith('- **') and (l.endswith('.') or l.endswith('"') or l.endswith('”')) for l in gce_l) and len(gcb_l) == 72 and all(re.match(r'^- C\d+\. \*\*', l) for l in gcb_l),
    'GCE terminam em: %s' % dict(collections.Counter(l[-1] for l in gce_l)))
fora = 0
for lid in ['L1', 'L2', 'L3', 'L4', 'L5', 'L6A', 'L6B']:
    A, B = E13['%s_estudo.md' % lid].split('\n'), E16['%s_estudo.md' % lid].split('\n')
    i, j = secao(A, '## Pares', '## Pegadinhas')
    assert len(A) == len(B)
    fora += sum(1 for k, (x, y) in enumerate(zip(A, B)) if not (i <= k < j) and x != y)
chk('(3) T54-3', 'fora das seções "## Pares", só mudam as 2 linhas do quadro do L1 (T54-4) e a linha 422 do L3 (T54-8b): 3 linhas nos 7 *_estudo.md (as mesmas contagens de linha; nenhuma linha acrescentada ou removida)', fora == 3, 'linhas alteradas fora de "## Pares": %d' % fora)
# canônico: a linha do par (sem "- " e sem "**") é a linha canônica com erratas, com as deleções de marca da edição
def canon_linhas_gce(lid):
    spec = next(s for s in gce_specs if s['id'] == lid)
    lines = gce.load(spec['file'], lid, ERRATA.get(lid, []))
    S = gce.sections(lines)
    L_ = gce.trim_blank(lines[S['c'][0]:S['c'][1]])
    items = []
    for l in L_:
        m = re.match(r'^\s*(\d+)\.\s+(.*)$', l)
        if m and (not items or int(m.group(1)) == items[-1][0] + 1): items.append([int(m.group(1)), m.group(2).strip()])
        elif items and l.strip(): items[-1][1] += ' ' + l.strip()
    return [t for _, t in items]
from p2 import LOTES as gce_specs
iguais = 0; so_del = 0; ruins = []
for lid in ['L1', 'L2', 'L3', 'L4', 'L5', 'L6A', 'L6B']:
    B = [l[2:].replace('**', '') for l in linhas_pares(E16, lid)]
    if lid in GCB_LOTES:
        can = [c[0] + '. ' + c[1] for c in canon_gcb(lid)]
    else:
        can = canon_linhas_gce(lid)
    assert len(can) == len(B), (lid, len(can), len(B))
    for k, (c, e) in enumerate(zip(can, B)):
        esp = em.strip_text(c, collections.Counter(), lid + '_estudo.md')
        if c == e: iguais += 1
        elif esp == e and em.is_subseq(e, c): so_del += 1
        else: ruins.append((lid, k + 1, c[:60], e[:60]))
chk('(3) T54-3', 'a linha do par na v1.4, sem "- " e sem "**", é igual à linha do par do arquivo canônico (erratas aplicadas; quebras juntadas; sem o numeral dos lotes GCE): 136 linhas iguais e 3 com só deleção de marca (L4 "Clustering", L4 "Controlador", L6B "Backup completo")',
    iguais == 136 and so_del == 3 and not ruins, 'iguais %d; só deleção de marca %d; divergentes %s' % (iguais, so_del, ruins[:3]))

# --- T54-4: quadro do L1
def pos(l): return [i for i, ch in enumerate(l) if ch == '|']
can1 = read('saida/gce/GCE_Lote1_v2_CPP.md').split('\n')
L14 = E16['L1_estudo.md'].split('\n'); L13 = E13['L1_estudo.md'].split('\n')
ok4 = True; det4 = []
for (ln14, ln_can, nome) in ((424, 475, 'Diarização'), (427, 478, 'Execução local')):
    a, b, c = L13[ln14 - 1], L14[ln14 - 1], can1[ln_can - 1]
    o = pos(b) == pos(c) and len(b) == len(c) and pos(a) != pos(c)
    d = [x for x in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if x[0] != 'equal']
    o = o and len(d) == 1 and d[0][0] == 'insert' and b[d[0][3]:d[0][4]] == ' ' * 6
    ok4 &= o; det4.append('v1.4 l.%d vs canônico l.%d: comprimento %d/%d, |: %s' % (ln14, ln_can, len(b), len(c), 'iguais' if pos(b) == pos(c) else 'DIFERENTES'))
chk('(3) T54-4', 'quadro-síntese do L1 (L1_estudo.md 424 e 427): posições de todos os "|" e comprimento (82 e 71) iguais aos de GCE_Lote1_v2_CPP.md 475 e 478; diferença para a v1.3 = só 6 espaços inseridos em cada linha', ok4 and len(L14[423]) == 82 and len(L14[426]) == 71, '; '.join(det4))
chk('(3) T54-4', 'as demais linhas do quadro (419–430) iguais às da v1.3; o desalinhamento canônico da linha "Tradução p/ inglês" permanece (a linha 428 é igual à v1.3)', L14[418:430][:5] == L13[418:430][:5] and [L14[k] for k in range(418, 430) if k not in (423, 426)] == [L13[k] for k in range(418, 430) if k not in (423, 426)]
    and pos(L14[428]) == pos(L13[428]))
# --- T54-5: nota
nl = [(f, l) for f, tx in E16.items() for l in tx.split('\n') if 'nota de vigência' in l]
chk('(3) T54-5', 'rótulo da nota: 0 "Nota: nota de vigência"; 4 linhas "^> nota de vigência: " (BANCO_itens 2, SIM-0_folha 2) e 4 "^- nota de vigência: " (BANCO_gabarito 2, SIM-0_gabarito 2); resto de cada linha = v1.3; " (D-LEI-15352)" ausente',
    sum(tx.count('Nota: nota de vigência') for tx in E16.values()) == 0 and sum(1 for f, l in nl if l.startswith('> nota de vigência: ')) == 4 and sum(1 for f, l in nl if l.startswith('- nota de vigência: ')) == 4 and len(nl) == 8
    and sum(tx.count('D-LEI-15352') for tx in E16.values()) == 0 and all(('> Nota: ' + l[2:] in E13[f] if l.startswith('> ') else '- Nota: ' + l[2:] in E13[f]) for f, l in nl),
    '%s' % sorted(collections.Counter(f for f, l in nl).items()))
# --- T54-6: 6B-06
gl = E16['L6B_gabarito.md'].split('\n'); g13 = E13['L6B_gabarito.md'].split('\n')
l14 = [l for l in gl if l.startswith('- Justificativa: TC (integridade e disponibilidade trocadas)')]; l13 = [l for l in g13 if l.startswith('- Justificativa: TC (integridade e disponibilidade trocadas)')]
chk('(3) T54-6', '6B-06: deleção pura do parêntese "(a definição da tríade não foi confirmada em fonte; ver curso 4.1.1)" na edição; 0 "não foi confirmada em fonte" e 0 "abertas? hoje" na edição; o pacote não muda (justificativa da 6B-06 igual à da v1.3)',
    len(l14) == len(l13) == 1 and em.is_subseq(l14[0], l13[0]) and l13[0].count(' (a definição da tríade não foi confirmada em fonte; ver curso 4.1.1)') == 1 and l13[0].replace(' (a definição da tríade não foi confirmada em fonte; ver curso 4.1.1)', '') == l14[0]
    and 'Fonte: conceito geral. Tema da tríade CIA também nos itens reais 96 e 98 do TRF6 2024' in l14[0] and sum(tx.count('não foi confirmada em fonte') for tx in E16.values()) == 0 and sum(len(re.findall(r'abertas? hoje', tx)) for tx in E16.values()) == 0
    and next(i for i in P16['itens'] if i['id'] == '6B-06')['justificativa'] == next(i for i in P13['itens'] if i['id'] == '6B-06')['justificativa'],
    'linha %d de L6B_gabarito.md (a LISTA diz 31; as 2 linhas da legenda de 6B do topo deslocam para 33 na v1.3 e na v1.4)' % (gl.index(l14[0]) + 1))
# --- T54-7: legendas nos SIM-*_gabarito
leg4, leg5 = LB15['L4']['legendaMecanismo'], LB15['L5']['legendaMecanismo']
s1 = E16['SIM-1_gabarito.md'].split('\n'); s13 = E13['SIM-1_gabarito.md'].split('\n')
chk('(3) T54-7', 'SIM-1_gabarito.md ganha exatamente 4 linhas (2 legendas e 2 linhas em branco): legenda do L4 (= L4C = L5C) e depois a do L5, literais; depois de "- Número de itens: 40" e antes de "### 1 — "; a ordem é a da lista `lotes`',
    len(s1) - len(s13) == 4 and s1[:4] == s13[:4] and s1[4] == '' and s1[5] == leg4 and s1[6] == '' and s1[7] == leg5 and s1[8] == '' and s1[9].startswith('### 1 — 4C-02 — Gabarito: C') and leg4 == LB15['L4C']['legendaMecanismo'] == LB15['L5C']['legendaMecanismo'] and leg4 != leg5
    and s1[3] == '- Número de itens: 40' and s1[9:] == s13[5:])
outros = {s: E16['%s_gabarito.md' % s] == E13['%s_gabarito.md' % s] for s in ('SIM-2', 'SIM-0-P2')}
chk('(3) T54-7', 'SIM-2_gabarito.md e SIM-0-P2_gabarito.md (L1, L1C, L2, L3; sem legenda) iguais aos da v1.3; SIM-0_gabarito.md (só BQ) muda só pela nota (T54-5); as folhas não mudam por este item (SIM-1_folha, SIM-2_folha, SIM-0-P2_folha iguais; SIM-0_folha muda só pela nota)',
    all(outros.values()) and all(E16[f] == E13[f] for f in ('SIM-1_folha.md', 'SIM-2_folha.md', 'SIM-0-P2_folha.md')) and all(not any(leg in E16[f] for leg in (leg4, leg5)) for f in ('SIM-0_gabarito.md', 'SIM-2_gabarito.md', 'SIM-0-P2_gabarito.md', 'SIM-0_folha.md', 'SIM-1_folha.md'))
    and E16['SIM-0_gabarito.md'].count('Mecanismo') == E13['SIM-0_gabarito.md'].count('Mecanismo'))
# --- T54-8: D5 e L3
dp14 = E16['DISCURSIVAS_padrao.md'].split('\n'); dp13 = E13['DISCURSIVAS_padrao.md'].split('\n')
op = [o for o in difflib.SequenceMatcher(None, dp13, dp14, autojunk=False).get_opcodes() if o[0] != 'equal']
chk('(3) T54-8a', 'DISCURSIVAS_padrao.md (v1.3 -> v1.6): saem as 7 linhas da nota R2 da D5 (507–513 da v1.3) e mudam as 3 notas da T-64 (321, 404 e 504; ver acima); D1, D2 e o resto de D3 a D5 idênticos; a D4 mantém as 7 linhas (407–413); "Notas de correção" da D5 continua (R3 e R4)',
    [(o[0], o[1] + 1, o[2]) for o in op] == [('replace', 321, 321), ('replace', 404, 404), ('replace', 504, 504), ('delete', 507, 513)] and dp13[406:413] == dp13[506:513] and dp14[406:413] == dp13[406:413] and dp14.count('Alínea c da discursiva: NÃO se exige enquadrar o') == 1 and len(dp13) - len(dp14) == 7
    and 'Voz como dado sensível (biométrico): nem exigido nem penalizado.' in dp14[506] and dp14[505] == 'Notas de correção' and E16['DISCURSIVAS.md'] == E13['DISCURSIVAS.md'].replace(E13_X, E13_Y), str(op))
l3a = E13['L3_estudo.md'].split('\n'); l3b = E16['L3_estudo.md'].split('\n')
op3 = [o for o in difflib.SequenceMatcher(None, l3a, l3b, autojunk=False).get_opcodes() if o[0] != 'equal']
mls = [i for i, (x, y) in enumerate(zip(l3a, l3b)) if x != y]
chk('(3) T54-8b', 'L3_estudo.md: a única linha que muda fora de "## Pares" é a 422: "jurisprudência firmada que eu possa afirmar):" -> "…que se possa afirmar):"; 0 "que eu possa afirmar" na edição',
    422 in [i + 1 for i in mls] and l3a[421] == 'jurisprudência firmada que eu possa afirmar):' and l3b[421] == 'jurisprudência firmada que se possa afirmar):' and sum(tx.count('que eu possa afirmar') for tx in E16.values()) == 0 and E13['L3_estudo.md'].count('que eu possa afirmar') == 1)
# README
a, b = E13['README.md'].split('\n'), E16['README.md'].split('\n')
o = [x for x in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if x[0] != 'equal']
chk('(3) EDIÇÃO', 'README (v1.3 -> v1.6): só as linhas de versão ("v1.3" -> "v1.6") e de data ("2026-10-13" -> "2026-10-14"); demais linhas iguais', len(a) == len(b) and len(o) == 1 and (o[0][1], o[0][2]) == (2, 4) and a[2] == '- Versão: v1.3 (pacote.json versão 1)' and b[2] == '- Versão: v1.6 (pacote.json versão 1)' and a[3] == '- Data: 2026-10-13' and b[3] == '- Data: 2026-10-14')
fid = json.load(open(os.path.join(OUT, 'estudante_fidelidade.json'), encoding='utf-8'))
chk('(3) EDIÇÃO', 'fidelidade (estudante_fidelidade.py): 0 diferenças contra o pacote com as regras de deleção e as exceções fechadas (CAIXA, nota de BQ-0003, realinhamento do quadro do L1)', fid['diferencas'] == 0 and fid['total'] > 0, 'comparações %d, diferenças %d, marcas residuais %d' % (fid['total'], fid['diferencas'], len(fid['restos'])))
conta = json.load(open(os.path.join(OUT, 'estudante_contagem.json'), encoding='utf-8'))
chk('(3) EDIÇÃO', 'remoções por deleção: 571 (v1.3) - 3 (a nota R2 da D5: "Alínea c … (R4 do Projeto)", "R2. " e "da versão da CPP") = 568; a regra literal do 6B-06 e o rótulo "(GCE, R3–R4)" substituem as anteriores com a mesma contagem; o realinhamento do L1 (2 linhas) não é remoção',
    sum(conta['total'].values()) == 568 and 'realinhamento' not in json.dumps(conta, ensure_ascii=False), str(sum(conta['total'].values())))
chk('(3) EDIÇÃO', 'realinhamento do quadro do L1: exceção fechada, 2 linhas, 1 ocorrência cada (REALINHA_HITS), só espaços', sorted(em.REALINHA_HITS.values()) in ([1, 1], []) and len(em.REALINHA) == 2 and all(len(d) - len(a_) == 6 for _, a_, d in em.REALINHA))

# ======================================================================= (4) varreduras de não regressão (seção 3.5 do QA R2), exceções fechadas da R1 e conferências do QA da T-56
def cre(rx, prefixos=None, F=E16, flags=re.M):
    r = re.compile(rx, flags)
    return sum(len(r.findall(tx)) for f, tx in F.items() if prefixos is None or f.startswith(tuple(prefixos)))
folhas = [f for f in E16 if f.endswith('_folha.md')]
V0 = [(r';\)', None), (r' — $', None), (r'\*\*\*\*', None), (r'abertas? hoje', None), (r'\(v2,', None), (r'D-LEI-15352', None), (r'neste chat', None), (r'Retificação', None),
      (r'Gabarito [CE] mantido', None), (r'\b(?:U[1-6]|GG\d|TB\d|CI)\b', None), (r'\bN\d\b', ('L1_', 'L1C_', 'L2_', 'L3_', 'SIM-2', 'SIM-0-P2')),
      (r' — (?:BQ|L\d|4C|5C|6A|6B|A5)', tuple(folhas)), (r'erificado em 8/10/2026', ('L5_', 'L5C_'))]
for rx, fl in V0:
    n = cre(rx, fl)
    chk('(4) VARR 3.5', '%s%s: 0' % (rx, ' em ' + ','.join(fl) if fl and len(fl) < 8 else (' nas folhas' if fl else '')), n == 0, str(n))
VX = [r'\[TS\]', r'\[V ', r'\bCQFP\b', r'\bCQE\b', r'\bGCE\b', r'\bGCB\b', r'\bGBQ\b', r'\bCPP\b', r'T-\d', r'\bQA\b', r'O-\d', r'Lição O', r'R-\dC\d', r'NÃO VOLÁTIL', r'não VOLÁTIL', r'Sem marca VOLÁTIL', r'REVERIFICAR', r'\bD-[A-Z]{2,}']
for rx in VX:
    n = cre(rx)
    chk('(4) VARR 3.5 extra', '%s: 0' % rx, n == 0, str(n))
sem_b14 = cre(r'D-[A-Z]{2,}'); sem_b12 = cre(r'D-[A-Z]{2,}', None, E12)
chk('(4) VARR 3.5 extra', 'D-[A-Z]{2,} (sem \\b): mesma contagem da v1.2 (só "TID-IA", "TID-DADOS-VIZ", "END-TO-END"); com \\b: 0 (errata de registro da T-56, seção 3)', sem_b14 == sem_b12 and cre(r'\bD-[A-Z]{2,}', None, E12) == 0 and cre(r'\bD-[A-Z]{2,}') == 0, 'v1.2 %d; v1.4 %d' % (sem_b12, sem_b14))
codF = sorted((f, k) for f, tx in E16.items() for k, l in enumerate(tx.split('\n'), 1) if re.search(r'\bF\d{1,2}\b', l))
chk('(4) VARR 3.5', 'códigos F: só L6A_estudo.md:83 ("a tecla F4") e L4_gabarito.md:58 (L4-11, "O F4 afirma")', len(codF) == 2 and codF[0][0] == 'L4_gabarito.md' and codF[1] == ('L6A_estudo.md', 83) and 'O F4 afirma' in E16['L4_gabarito.md'].split('\n')[codF[0][1] - 1] and 'tecla F4' in E16['L6A_estudo.md'].split('\n')[82], str(codF))
AV = 'Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.'
volx = sorted((f, k) for f, tx in E16.items() for k, l in enumerate(tx.split('\n'), 1) if 'VOLÁTIL' in l and AV not in l)
volx13 = sorted((f, k) for f, tx in E13.items() for k, l in enumerate(tx.split('\n'), 1) if 'VOLÁTIL' in l and AV not in l)
chk('(4) VARR 3.5', '"VOLÁTIL" fora do aviso fixo: só L4_estudo 23 e 210; L5_estudo 24, 104 e 107; L6A_estudo 125 e 268 (igual à v1.3); os gabaritos com legenda não ganham a palavra', volx == sorted([('L4_estudo.md', 23), ('L4_estudo.md', 210), ('L5_estudo.md', 24), ('L5_estudo.md', 104), ('L5_estudo.md', 107), ('L6A_estudo.md', 125), ('L6A_estudo.md', 268)]) and volx == volx13, str(volx))
json.dump({'volatil_fora_do_aviso': volx}, open(os.path.join(OUT, 'varredura_volatil_v16.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
# conferências do QA da T-56 que continuam valendo: N-1, legendas dos lotes, avisos não exibidos
n1 = sum(tx.count('Nesta produção') + tx.count('nesta produção') for tx in E16.values()); n2 = sum(tx.lower().count('especificação previa') for tx in E16.values()); n3 = sum(tx.count('se houver base') for tx in E16.values())
chk('(4) QA T-56', 'N-1: 0 "Nesta produção", 0 "especificação previa" e 0 "se houver base" nos 43 arquivos; no pacote a marca fica (1 e 1; D-PACOTE-V11)', n1 == n2 == n3 == 0 and sum(l['curso'].count('Nesta produção') for l in P16['lotes']) == 1 and sum(l['curso'].count('especificação previa') for l in P16['lotes']) == 1, '%d/%d/%d' % (n1, n2, n3))
chk('(4) QA T-56', 'L6B_estudo.md igual ao da v1.3 salvo as 18 linhas de pares (N-1 intacta: a linha 143 é igual)', [k for k, (x, y) in enumerate(zip(E13['L6B_estudo.md'].split('\n'), E16['L6B_estudo.md'].split('\n'))) if x != y] == list(range(274, 292)) and E13['L6B_estudo.md'].split('\n')[142] == E16['L6B_estudo.md'].split('\n')[142])
okl = True; detl = []
for l in P16['lotes']:
    f = '%s_gabarito.md' % l['id']
    if 'legendaMecanismo' not in l: okl &= E13[f] == E16[f] and E16[f].split('\n')[2].startswith('### '); continue
    b = E16[f].split('\n')
    ok = b[0] == '# %s — gabarito e justificativas' % l['nome'] and b[1] == '' and b[2] == l['legendaMecanismo'] and b[3] == '' and b[4].startswith('### ') and b[0:4] == E13[f].split('\n')[0:4]
    okl &= ok; detl.append('%s %s' % (l['id'], 'ok' if ok else 'FALHA'))
chk('(4) QA T-56', 'legenda: nos 6 L<lote>_gabarito.md é literal, sozinha, no topo (linha 3), antes do primeiro item (como na v1.3); L1, L1C, L2, L3 sem legenda; L<lote>_gabarito.md iguais aos da v1.3 salvo L6B (6B-06)', okl and all(E13[f] == E16[f] for f in E16 if re.match(r'^L(1|1C|2|3|4|4C|5|5C|6A)_gabarito\.md$', f)), ', '.join(detl))
legs = sorted({l['legendaMecanismo'] for l in P16['lotes'] if 'legendaMecanismo' in l})
dentro = [f for f, tx in E16.items() if any(g in tx for g in legs) and not re.match(r'^(L(4|4C|5|5C|6A|6B)_gabarito|SIM-1_gabarito)\.md$', f)]
chk('(4) QA T-56', 'legenda exibida só nos L<lote>_gabarito.md dos 6 lotes e no SIM-1_gabarito.md (D-T54-07): 0 ocorrência em BANCO_gabarito.md, *_estudo.md, *_itens.md, *_folha.md, README.md, SIM-0, SIM-2 e SIM-0-P2', not dentro, str(dentro))
avs = [a for s in P16['simulados'] for a in s.get('avisos', [])]
exib = [f for f, tx in E16.items() if any(fr in tx for av in avs for fr in (av[:40], av.split('\n')[0][-40:]))]
chk('(4) QA T-56', 'avisos do SIM-0 continuam no pacote (3 strings) e NÃO são exibidos na edição (0 arquivo com o texto dos 3 avisos; 0 "Avisos de montagem", 0 "D-ADERENCIA")', len(avs) == 3 and avs == P13['simulados'][0]['avisos'] and not exib and sum(tx.count('Avisos de montagem') + tx.count('D-ADERENCIA') for tx in E16.values()) == 0, str(exib))
chk('(4) QA T-56', 'README, folhas e demais arquivos sem mudança indevida: SIM-0_folha e SIM-0_gabarito mudam só pela nota (a v1.3 sem a nota = a v1.4 sem a nota)', all(re.sub(r'(?m)^([>-]) (?:Nota: )?nota de vigência:.*\n?', '', E13[f]) == re.sub(r'(?m)^([>-]) (?:Nota: )?nota de vigência:.*\n?', '', E16[f]) for f in ('SIM-0_folha.md', 'SIM-0_gabarito.md', 'BANCO_itens.md', 'BANCO_gabarito.md')))

# exceções fechadas da R1
def strings(o):
    if isinstance(o, str): yield o
    elif isinstance(o, dict):
        for v in o.values(): yield from strings(v)
    elif isinstance(o, list):
        for v in o: yield from strings(v)
S14 = list(strings(P16))
def ce(t, pref=None): return sum(tx.count(t) for f, tx in E16.items() if pref is None or f.startswith(tuple(pref)))
it = {i['id']: i for i in P16['itens']}
c05 = [('4C-08', '(conceito geral, sem fonte de fornecedor, como no curso). O item não depende', '(conceito geral, sem fonte de fornecedor, como no curso). o item não depende'),
       ('5C-06', 'termine no mínimo da amostra. A regra de 1,5 · AIQ', 'termine no mínimo da amostra. a regra de 1,5 · AIQ')]
for iid, novo, antigo in c05:
    j = it[iid]['justificativa']
    ocorr = 1 + sum(1 for s in P16['simulados'] if iid in s['itens'])
    chk('(4) CAIXA C-05', '%s: pacote com inicial maiúscula (1 vez), sem a minúscula; edição: %d ocorrências (gabarito do lote + simulados), 0 da minúscula' % (iid, ocorr), j.count(novo) == 1 and j.count(antigo) == 0 and ce(novo) == ocorr and ce(antigo) == 0, 'edição %d' % ce(novo))
for esc, antes, depois in em.CAIXA:
    chk('(4) CAIXA C-15', 'L6A_estudo: "%s" -> "%s": antes 0, depois 1' % (antes[:34], depois[:34]), ce(antes, (esc,)) == 0 and ce(depois, (esc,)) == 1 and len(antes) == len(depois) and sum(x != y for x, y in zip(antes, depois)) == 1)
chk('(4) CAIXA C-15', 'lista CAIXA: 8 pares, todos em L6A_estudo; 8 trocas na regeração; L6A_estudo.md idêntico ao da v1.3 fora dos 19 pares', len(em.CAIXA) == 8 and all(c[0] == 'L6A_estudo' for c in em.CAIXA) and conta['total'].get('caixa (minúscula → maiúscula na inicial deixada por deleção)') == 8)
def peg(P, lid, rot): return [g['texto'] for l in P['lotes'] if l['id'] == lid for g in l['pegadinhas'] if g['rotulo'] == rot]
e15 = peg(P16, 'L1', 'Pontuação automática e capitalização em transcrições')
b1 = peg(P16, 'L5', 'Gráfico de barras (colunas)'); b2 = peg(P16, 'L5', 'Box plot (diagrama de caixa)')
chk('(4) REUNIÃO C-06', 'L1 P2-1.5: 1 entrada, com os dois fragmentos unidos por "; "', len(e15) == 1 and '"Câmara" (instituição) vs "câmara" (sala)' in e15[0] and e15 == peg(P12, 'L1', 'Pontuação automática e capitalização em transcrições'))
chk('(4) REUNIÃO C-07', 'L5 Gráfico de barras (colunas): 3 entradas (confundir com histograma; aceitar eixo truncado; reunida "usar para distribuição…; empilhado quando…")', len(b1) == 3 and 'usar para distribuição de variável contínua agrupada em classes; empilhado quando se quer comparar as partes entre si.' in b1 and 'confundir com histograma' in b1 and 'aceitar eixo truncado' in b1)
chk('(4) REUNIÃO C-08', 'L5 Box plot (diagrama de caixa): 1 entrada com os 4 fragmentos unidos por "; "', len(b2) == 1 and b2[0].startswith('dizer que a linha central é a média; que a caixa vai do mínimo ao máximo') and b2[0].endswith('que mostra frequência por intervalo (isso é histograma).'))
npg = {l['id']: len(l['pegadinhas']) for l in P16['lotes']}
chk('(4) REUNIÃO', 'pegadinhas por lote = v1.3 (L1 19, L1C 4, L2 43, L3 42, L4 32, L4C 0, L5 48, L5C 0, L6A 35, L6B 39; total 262)', npg == {'L1': 19, 'L1C': 4, 'L2': 43, 'L3': 42, 'L4': 32, 'L4C': 0, 'L5': 48, 'L5C': 0, 'L6A': 35, 'L6B': 39} and sum(npg.values()) == 262)
l1e = E16['L1_estudo.md']; l5e = E16['L5_estudo.md']
chk('(4) REUNIÃO', 'edição: L1_estudo com 1 linha para P2-1.5 "Pontuação automática…"; L5_estudo com 3 linhas "Gráfico de barras (colunas)" e 1 "Box plot (diagrama de caixa)"',
    sum(1 for l in l1e.split('\n') if l.startswith('- [P2-1.5] **Pontuação automática e capitalização em transcrições**')) == 1 and sum(1 for l in l5e.split('\n') if l.startswith('- [P1-8.2] **Gráfico de barras (colunas)**')) == 3 and sum(1 for l in l5e.split('\n') if l.startswith('- [P1-8.2] **Box plot (diagrama de caixa)**')) == 1)
j = it['L4-11']['justificativa']; ed = [l for l in E16['L4_gabarito.md'].split('\n') if l.startswith('- Justificativa: ') and 'O F4 afirma que "generative models are initially trained using an unsupervised approach"' in l]
chk('(4) C-13', 'L4-11: justificativa da edição = a do pacote menos exatamente " Fonte: F4, reverificado em 7/10/2026." (1 ocorrência no pacote); frase que fundamenta o gabarito C presente; gabarito C',
    len(ed) == 1 and j.count(' Fonte: F4, reverificado em 7/10/2026.') == 1 and ed[0] == '- Justificativa: ' + j.replace(' Fonte: F4, reverificado em 7/10/2026.', '') and it['L4-11']['gabarito'] == 'C' and 'L4-11' not in [x for s in P16['simulados'] for x in s['itens']])
n3_ = it['BQ-0003']['nota']
chk('(4) C-18', 'BQ-0003: `nota` no pacote com " (D-LEI-15352)" literal; na edição, sem ele e sem o rótulo "Nota:", nos 4 pontos (BANCO_itens, BANCO_gabarito, SIM-0_folha, SIM-0_gabarito); BQ-0040 sem o identificador',
    n3_.count(' (D-LEI-15352)') == 1 and ce(n3_.replace(' (D-LEI-15352)', '')) == 4 and ce('D-LEI-15352') == 0 and all(ce(n3_.replace(' (D-LEI-15352)', ''), (f,)) == 1 for f in ('BANCO_itens', 'BANCO_gabarito', 'SIM-0_folha', 'SIM-0_gabarito')) and '(D-' not in it['BQ-0040']['nota'])
chk('(4) C-10', 'folhas: 165 linhas de item sem id de origem; 0 com id (id só no *_gabarito.md)', cre(r'^\*\*\d+\*\* — ', tuple(folhas)) == 165 and cre(r'^\*\*(?:BQ-|L\d|4C-|5C-|6A-|6B-|A5-)\S*\*\*', tuple(folhas)) == 0)
def tb_antes(tx):
    nb = [l for l in tx.split('\n') if l.strip()]
    return (sum(1 for k in range(len(nb) - 1) if nb[k].startswith('**Texto-base.**') and nb[k + 1].startswith('**Comando.**')), sum(1 for k in range(len(nb) - 1) if nb[k].startswith('**Comando.**') and nb[k + 1].startswith('**Texto-base.**')))
chk('(4) C-11', 'texto-base antes do comando: BANCO_itens 3 e SIM-0_folha 1; 0 comando antes de texto-base', tb_antes(E16['BANCO_itens.md']) == (3, 0) and tb_antes(E16['SIM-0_folha.md']) == (1, 0) and sum(tb_antes(tx)[1] for tx in E16.values()) == 0)

# --- T57 s3 item 6: scripts históricos mantidos (opção "marcar", D-T57-10), sem alteração
import glob
HIST = ['relatorio_R1.py', 'report.py', 'report2.py', 'diff.py', 'diff2.py', 'conferencias_R1.py']
HD = os.path.dirname(os.path.abspath(__file__)); H14 = os.path.join(HD, '..', 'gerador_v1_4')
chk('(4) T57 s3-6', 'os 5 scripts históricos não executáveis (relatorio_R1, report, report2, diff, diff2) e conferencias_R1.py (histórico executável) estão em gerador_v1_6/ e são idênticos, byte a byte, aos de gerador_v1_4/ (opção "marcar", D-T57-10: nenhuma alteração)',
    all(open(os.path.join(HD, f), 'rb').read() == open(os.path.join(H14, f), 'rb').read() for f in HIST), ', '.join(HIST))

# ======================================================================= (5) contagens iguais às da v1.4, da v1.3 e da v1.2
def cnt(P):
    it_ = P['itens']
    c = collections.OrderedDict()
    c['itens'] = len(it_); c['ids únicos'] = len({i['id'] for i in it_})
    c['C'] = sum(i['gabarito'] == 'C' for i in it_); c['E'] = sum(i['gabarito'] == 'E' for i in it_)
    c['banco'] = sum(i['rotulo'] != 'AUTORAL' for i in it_); c['AUTORAL'] = sum(i['rotulo'] == 'AUTORAL' for i in it_)
    c['aderência direta'] = sum(i['aderencia'] == 'direta' for i in it_); c['aderência parcial'] = sum(i['aderencia'] == 'parcial' for i in it_)
    c['volatil'] = sum(bool(i.get('volatil')) for i in it_); c['nota'] = sum('nota' in i for i in it_); c['comandoOriginal'] = sum('comandoOriginal' in i for i in it_)
    c['pegadinhas'] = sum(len(l['pegadinhas']) for l in P['lotes']); c['pares'] = sum(len(l['pares']) for l in P['lotes'])
    c['simulados n'] = [s['n'] for s in P['simulados']]; c['simulados itens'] = [len(s['itens']) for s in P['simulados']]
    c['lotes'] = len(P['lotes']); c['discursivas'] = len(P['discursivas']); c['edital'] = len(P['edital'])
    c['aspectos'] = sum(len(d['aspectos']) for d in P['discursivas']); c['quesitos'] = sum(len(d['quesitos']) for d in P['discursivas'])
    return c
c12 = cnt(P12); c13 = cnt(P13); c14 = cnt(P14); c15 = cnt(P15); c16 = cnt(P16)
ESP = collections.OrderedDict([('itens', 286), ('ids únicos', 286), ('C', 149), ('E', 137), ('banco', 106), ('AUTORAL', 180), ('aderência direta', 247), ('aderência parcial', 39), ('volatil', 23), ('nota', 2),
                               ('comandoOriginal', 90), ('pegadinhas', 262), ('simulados n', [60, 40, 40, 25]), ('simulados itens', [60, 40, 40, 25]), ('lotes', 10), ('discursivas', 5), ('edital', 47)])
for k, v in ESP.items():
    chk('(5) CONT', '%s = %s (v1.2: %s; v1.3: %s; v1.4: %s; v1.5: %s; v1.6: %s)' % (k, v, c12[k], c13[k], c14[k], c15[k], c16[k]), c16[k] == v == c15[k] == c14[k] == c13[k] == c12[k])
chk('(5) CONT', 'pares (139), aspectos e quesitos das discursivas iguais aos da v1.3 e da v1.2; pares com `id` 72', c16['pares'] == c14['pares'] == c13['pares'] == c12['pares'] == 139 and c16['aspectos'] == c14['aspectos'] == c13['aspectos'] == c12['aspectos'] and c16['quesitos'] == c14['quesitos'] == c13['quesitos'] == c12['quesitos'] and sum('id' in p for l in P16['lotes'] for p in l['pares']) == 72,
    '%s/%s/%s' % (c16['pares'], c16['aspectos'], c16['quesitos']))
chk('(5) CONT', 'SIM-0 33 C/27 E (diagnóstico, 23 parciais, 4 voláteis, 3 avisos); SIM-1 e SIM-2 20 C/20 E; SIM-0-P2 13 C/12 E', [tuple(collections.Counter(it[x]['gabarito'] for x in s['itens']).get(g, 0) for g in 'CE') for s in P16['simulados']] == [(33, 27), (20, 20), (20, 20), (13, 12)]
    and sum(1 for x in P16['simulados'][0]['itens'] if it[x]['aderencia'] == 'parcial') == 23 and sum(1 for x in P16['simulados'][0]['itens'] if it[x].get('volatil')) == 4)
chk('(5) CONT', 'edição: 43 arquivos; itens por lote e por simulado iguais aos da v1.3', len(E16) == 43 and c16['simulados itens'] == [60, 40, 40, 25])

# ======================================================================= (6) artefatos da T-59 e da T-66 (D-T59-07, D-T59-04, D-T59-02, seção 6 da decisão; regra v1.2: E-6 a E-10 de T66_decisoes, seção 6.2)
import subprocess
imp_v1 = '\n'.join(bloco_apos('## 2. REGRA DE IMPORTAÇÃO', '```markdown')) + '\n'
imp_atual = open(os.path.join(REPO_, 'regras', 'importacao_erros.md'), 'rb').read().decode('utf-8')
imp_v11_git = refs.git_show(refs.C_V15, 'regras/importacao_erros.md').decode('utf-8')   # v1.1 aceita (git a889100; SHA-256 4bc7098a…)
# errata v1.1 (T59_T60_reconciliacao_2026-10-14.md, seção 3.1-D): 5 substituições, cada "antes" com ocorrência única (abortar se != 1); literais escritos aqui e conferidos contra o texto da reconciliação
E1 = ('— v1, 2026-10-14 — D1 da GBQ (saida/pacote/T59_decisoes_2026-10-14.md)\n', '— v1.1, 2026-10-14 — D1 da GBQ (saida/pacote/T59_decisoes_2026-10-14.md; errata v1.1: saida/pacote/T59_T60_reconciliacao_2026-10-14.md)\n')
E2 = ('## 2. Validação (gbq-csc, por script `python3 -I`, somente leitura; resultado na seção "Validação" do diagnóstico)\n', '## 2. Validação (gbq-csc, por script `python3 -I`, somente leitura, com o validador mantido em `saida/treino/ferramentas/validar_erros.py`; resultado na seção "Validação" do diagnóstico)\n')
E3 = ('   - abrir como JSON UTF-8;\n', '   - abrir como JSON UTF-8 (`NaN`, `Infinity` e `-Infinity` não são JSON; um BOM UTF-8 inicial é tolerado e registrado como aviso);\n')
E4 = ('   - ter todos os campos da tabela do contrato, com os tipos dela.\n', '   - ter todos os campos da tabela do contrato, com os tipos dela, salvo que, em `discursivas`, basta `ne` ser número e `tl` ser número ou null (o valor fora do domínio é tratado no item 5).\n')
E5_LIN = ('   - **Discursiva.** `ne` que não seja inteiro ≥ 0, ou `tl` que não seja inteiro ≥ 1 (inclusive null), é incoerência daquela discursiva: ela é listada com o motivo, e a autoavaliação dela (`notas`, `ne`, `nota`) fica fora do diagnóstico (3.1, item 7, registra "autoavaliação incoerente"). O `texto` segue para a correção dupla (3.3), e o arquivo não é recusado.\n',
          '   - **Ordem.** A ordem das listas da tabela D-T59-02 (caderno por `errou` decrescente e depois `id`; `respostasCaderno`, `tentativas` e `saidas` por data não decrescente; `discursivas` por `id`) é conferida. Lista fora de ordem gera aviso, sem recusa e sem tirar nada dos cálculos.\n')
def reconstroi_v11(v1):
    t = v1
    for a, b in (E1, E2, E3, E4):
        assert t.count(a) == 1, a[:50]
        t = t.replace(a, b)
    ln = [l for l in t.split('\n') if l.startswith('5. **Coerência.**')]
    assert len(ln) == 1 and ln[0].endswith('o restante do arquivo é usado.') and t.count(ln[0] + '\n') == 1
    return t.replace(ln[0] + '\n', ln[0] + '\n' + E5_LIN[0] + E5_LIN[1])
imp_lit = reconstroi_v11(imp_v1)
t5960 = read('saida/pacote/T59_T60_reconciliacao_2026-10-14.md')
lit_ok = all(x.strip() in t5960 for x in (E1[1].split('— ', 1)[1].strip(), E2[1].strip(), E3[1].strip(), E4[1].strip(), E5_LIN[0].strip(), E5_LIN[1].strip()))
chk('(6) T-59', 'regras/importacao_erros.md v1 (bloco D-T59-07 de T59_decisoes, SHA-256 b19bc0e4adf9…, 127 linhas) + E-1 a E-5 da reconciliação (5 substituições, cada "antes" com 1 ocorrência; textos conferidos contra T59_T60_reconciliacao_2026-10-14.md, seção 3.1-D)',
    hashlib.sha256(imp_v1.encode('utf-8')).hexdigest() == 'b19bc0e4adf97e41f721ebb3a854e5fdc4fad05459698e0f6fb6bb763f792f34' and imp_v1.count('\n') == 127 and lit_ok, 'v1: %d linhas; v1.1 reconstruída: %d linhas' % (imp_v1.count('\n'), imp_lit.count('\n')))
chk('(6) T-59', 'regras/importacao_erros.md v1.1 (git %s; SHA-256 4bc7098a8468353c8c6bf6f41ef55ae8733813ea525cbc9c76e58ad87f047d0f, 12388 bytes, 129 linhas) é igual, caractere a caractere, ao bloco D-T59-07 com E-1 a E-5 aplicadas, reconstruída por script (%d linhas, %d caracteres): 2 linhas a mais, 4 trocadas, as demais idênticas e na mesma ordem; sem BOM nem CR' % (refs.C_V15, imp_lit.count('\n'), len(imp_lit)),
    imp_v11_git == imp_lit and hashlib.sha256(imp_v11_git.encode('utf-8')).hexdigest() == '4bc7098a8468353c8c6bf6f41ef55ae8733813ea525cbc9c76e58ad87f047d0f' and len(imp_v11_git.encode('utf-8')) == 12388 and imp_v11_git.count('\n') == 129
    and ' — v1.1, 2026-10-14 — ' in imp_v11_git.split('\n')[0] and imp_lit.count('\n') - imp_v1.count('\n') == 2 and '\r' not in imp_v11_git and not imp_v11_git.startswith('﻿')
    and [(o[0], o[2] - o[1], o[4] - o[3]) for o in difflib.SequenceMatcher(None, imp_v1.split('\n'), imp_v11_git.split('\n'), autojunk=False).get_opcodes() if o[0] != 'equal'] == [('replace', 1, 1), ('replace', 1, 1), ('replace', 1, 1), ('replace', 1, 1), ('insert', 0, 2)])
# ---- regra v1.2: E-6 a E-10 lidas dos blocos literais de T66_decisoes, seção 6.2 (aplicadas em ordem, cada "onde se lê" com 1 ocorrência no estado anterior)
RG = blocos_t66('### 6.2 Regra', '### 6.3 Plataforma', 'E')
imp_v12_rec, occ_e = aplica_em_ordem(imp_v11_git, list(RG.values()))
imp_cadeia, occ_cadeia = aplica_em_ordem(imp_lit, list(RG.values()))
LI1, LI2 = imp_v11_git.split('\n'), imp_atual.split('\n')
opi = [o for o in difflib.SequenceMatcher(None, LI1, LI2, autojunk=False).get_opcodes() if o[0] != 'equal']
chk('(6) T-66', 'E-6 a E-10 lidas dos blocos literais da seção 6.2 de T66_decisoes (5 pares, na ordem); cada "onde se lê" ocorre exatamente 1 vez no estado anterior à troca: %s' % occ_e, list(RG) == ['E-6', 'E-7', 'E-8', 'E-9', 'E-10'] and occ_e == [1, 1, 1, 1, 1] and occ_cadeia == occ_e)
chk('(6) T-66', 'regras/importacao_erros.md (arquivo atual) é igual, caractere a caractere, à v1.1 do git (4bc7098a…) com E-6 a E-10 aplicadas e, pela cadeia completa, ao bloco D-T59-07 + E-1 a E-5 + E-6 a E-10 (reconstruída por script): SHA-256 922d77b84543c4cc4bec9fa2b64f705f4afc4ddbc3577e830422d5bd5a7b28b8, 12979 bytes, 130 linhas; sem BOM nem CR',
    imp_atual == imp_v12_rec == imp_cadeia and hashlib.sha256(imp_atual.encode('utf-8')).hexdigest() == '922d77b84543c4cc4bec9fa2b64f705f4afc4ddbc3577e830422d5bd5a7b28b8' and len(imp_atual.encode('utf-8')) == 12979 and imp_atual.count('\n') == 130 and '\r' not in imp_atual and not imp_atual.startswith('﻿'),
    'SHA-256 %s' % hashlib.sha256(imp_atual.encode('utf-8')).hexdigest()[:12])
chk('(6) T-66', 'diff linha a linha v1.1 -> v1.2: 4 linhas trocadas (1, 3, 27 e 39 da v1.1) e 1 inserida depois da 33 (E-9); "(v1.2.4)" presente e "(v1.2.3)" ausente; primeira linha com "v1.2, 2026-10-14" e a errata em T66_decisoes; os 4 títulos de seção intactos',
    [(o[0], o[1] + 1, o[2], o[4] - o[3]) for o in opi] == [('replace', 1, 1, 1), ('replace', 3, 3, 1), ('replace', 27, 27, 1), ('insert', 34, 33, 1), ('replace', 39, 39, 1)] and len(LI2) - len(LI1) == 1
    and ' — v1.2, 2026-10-14 — ' in LI2[0] and 'errata v1.2: saida/pacote/T66_decisoes_2026-10-14.md' in LI2[0] and '(v1.2.4)' in imp_atual and '(v1.2.3)' not in imp_atual
    and all(s_ in imp_atual for s_ in ('## 1. Entrada e guarda (privacidade)', '## 2. Validação', '## 3. O que a rodada semanal produz', '## 4. O que nada disto faz')),
    'operações: ' + '; '.join('%s antes[%d:%d] depois[%d:%d]' % o for o in opi))
chk('(6) T-66', 'importacao_erros.md v1.2 cita o contrato v1.2.4, o validador mantido (saida/treino/ferramentas/validar_erros.py) e as 4 seções da regra (1 Entrada e guarda; 2 Validação; 3 O que a rodada semanal produz; 4 O que nada disto faz)',
    all(s_ in imp_atual for s_ in ('(v1.2.4)', '`saida/treino/ferramentas/validar_erros.py`', '## 1. Entrada e guarda (privacidade)', '## 2. Validação', '## 3. O que a rodada semanal produz', '## 4. O que nada disto faz')))
ex_lit = '\n'.join(bloco_apos('### D-T59-04', '```json')) + '\n'
ex_raw = open(os.path.join(REPO_, 'saida', 'pacote', 'exemplo_erros_v1.json'), 'rb').read().decode('utf-8')
exo = json.loads(ex_raw)
TAB = ['formato', 'versaoFormato', 'exportadoEm', 'pacote', 'estadoVersao', 'escolha', 'resumo', 'caderno', 'respostasCaderno', 'tentativas', 'saidas', 'discursivas']
chk('(6) T-59', 'saida/pacote/exemplo_erros_v1.json é igual, caractere a caractere, ao exemplo mínimo da decisão (D-T59-04); abre como JSON; tem os 12 campos da tabela D-T59-02', ex_raw == ex_lit and sorted(exo) == sorted(TAB) and exo['formato'] == 'camara2026.erros' and exo['versaoFormato'] == 1)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validar_erros as VE
Rex = VE.valida(ex_raw.encode('utf-8'), P16)
chk('(6) T-59', 'validador (validar_erros.py) sobre o exemplo: ACEITO, 0 incoerência (D-T59-05), ids fictícios listados como desconhecidos (caderno XX-0001; det XX-0001 e XX-0002; discursivas DX)',
    Rex['veredito'] == 'ACEITO' and not Rex['incoerencias'] and {k: sorted(v['ids']) for k, v in Rex['ids_desconhecidos'].items()} == {'caderno': ['XX-0001'], 'tentativas[].det': ['XX-0001', 'XX-0002'], 'discursivas': ['DX']})
VM = os.path.join(REPO_, 'saida', 'treino', 'ferramentas', 'validar_erros.py')
rm = subprocess.run([sys.executable, '-I', VM, os.path.join(REPO_, 'saida', 'pacote', 'exemplo_erros_v1.json'), '--pacote', PAC, '--json'], capture_output=True, text=True)
Rm = json.loads(rm.stdout)
chk('(6) T-59', 'validador mantido (saida/treino/ferramentas/validar_erros.py, `python3 -I`) sobre o exemplo: ACEITO (código 0), 0 incoerência, 0 aviso `ordem:`, fora_dos_calculos com as 3 chaves vazias, mesmos ids desconhecidos que o registro',
    rm.returncode == 0 and Rm['veredito'] == 'ACEITO' and not Rm['incoerencias'] and not [x for x in Rm['avisos'] if x.startswith('ordem:')] and Rm['fora_dos_calculos'] == {'tentativas': [], 'caderno': [], 'discursivas': []} and Rm['ids_desconhecidos'] == Rex['ids_desconhecidos'] and Rm['sha256'] == Rex['sha256'])
HDV = os.path.dirname(os.path.abspath(__file__))
man = open(os.path.join(HDV, 'MANIFESTO.md'), encoding='utf-8').read().split('\n')
mv = [l for l in man if l.startswith('| validar_erros.py |')]; mt = [l for l in man if l.startswith('| validar_erros_teste.py |')]
chk('(6) T-59', 'registro (D-R59-08): gerador_v1_6/validar_erros.py (19ab9c8b…) e validar_erros_teste.py (33132d5a…) continuam com o SHA-256 da T-61; o MANIFESTO os marca "registro (T-59); versão mantida em `saida/treino/ferramentas/` (D-R59-08)" com o mesmo SHA; a cópia mantida existe e difere do registro',
    hashlib.sha256(open(os.path.join(HDV, 'validar_erros.py'), 'rb').read()).hexdigest() == '19ab9c8b359e4a59f209ecbca3e29f2ecc16a0dd5fb49b8892538bbe7eb8f33e' and hashlib.sha256(open(os.path.join(HDV, 'validar_erros_teste.py'), 'rb').read()).hexdigest() == '33132d5a9d9aaf7ec4bf645ae57b84eca9c2094abdc70f18d6970465278f0186'
    and len(mv) == 1 and len(mt) == 1 and '19ab9c8b359e4a59f209ecbca3e29f2ecc16a0dd5fb49b8892538bbe7eb8f33e' in mv[0] and '33132d5a9d9aaf7ec4bf645ae57b84eca9c2094abdc70f18d6970465278f0186' in mt[0]
    and all('registro (T-59); versão mantida em `saida/treino/ferramentas/` (D-R59-08)' in l for l in (mv[0], mt[0])) and os.path.exists(VM) and open(VM, 'rb').read() != open(os.path.join(HDV, 'validar_erros.py'), 'rb').read())
SHA_VM = hashlib.sha256(open(VM, 'rb').read()).hexdigest(); SHA_VMT = hashlib.sha256(open(os.path.join(REPO_, 'saida', 'treino', 'ferramentas', 'validar_erros_teste.py'), 'rb').read()).hexdigest()
tp = subprocess.run([sys.executable, '-I', os.path.join(REPO_, 'saida', 'treino', 'ferramentas', 'validar_erros_teste.py')], capture_output=True, text=True, cwd='/')
tp_ok = sum(1 for x in tp.stdout.split('\n') if x.startswith('OK    ')); tp_f = sum(1 for x in tp.stdout.split('\n') if x.startswith('FALHA '))
chk('(6) T-66', 'validador mantido (T-66): saida/treino/ferramentas/validar_erros.py SHA-256 220dd559fa5ac23bda706366c613603654d41533713f45a78969371ee69e9985 e validar_erros_teste.py SHA-256 192581d92c242bbf6649ad11c3d5212ec6eb9c15b2d377d6e0f437d79d4595e2 (T66_producao_2026-10-14.md); o teste, rodado de / com `python3 -I`: %d conferências OK, %d FALHA, código %d' % (tp_ok, tp_f, tp.returncode),
    SHA_VM == '220dd559fa5ac23bda706366c613603654d41533713f45a78969371ee69e9985' and SHA_VMT == '192581d92c242bbf6649ad11c3d5212ec6eb9c15b2d377d6e0f437d79d4595e2' and tp.returncode == 0 and tp_f == 0 and tp_ok > 0 and SHA_VM in read('saida/pacote/T66_producao_2026-10-14.md'),
    'SHA-256 %s / %s' % (SHA_VM[:12], SHA_VMT[:12]))
gi = open(os.path.join(REPO_, '.gitignore'), 'rb').read().decode('utf-8')
chk('(6) T-59', '.gitignore da raiz = as 2 linhas da decisão (seção 6, item 1): "# T-59 (D1 da GBQ): dados da candidata — nunca no git" e "/entrada/erros/"', gi == '# T-59 (D1 da GBQ): dados da candidata — nunca no git\n/entrada/erros/\n')
cg = subprocess.run(['git', '-C', REPO_, 'check-ignore', '-v', 'entrada/erros/x.json'], capture_output=True, text=True)
cg2 = subprocess.run(['git', '-C', REPO_, 'check-ignore', '-q', 'entrada/erros/discursivas/2026-10-18_D1/resposta_candidata.md'], capture_output=True)
cg3 = subprocess.run(['git', '-C', REPO_, 'check-ignore', '-q', 'saida/treino/diagnostico_2026-10-18.md'], capture_output=True)
chk('(6) T-59', 'git check-ignore: entrada/erros/x.json e entrada/erros/discursivas/…/resposta_candidata.md são ignorados; saida/treino/diagnostico_….md (agregado sem texto) NÃO é ignorado', cg.returncode == 0 and cg2.returncode == 0 and cg3.returncode == 1, cg.stdout.strip().replace('\t', ' '))
chk('(6) T-59', 'o pacote v1.6 não traz campo novo (D-T59-10, item 1): nenhum `id` de simulado "SIM-S-…" (ainda não há simulado da semana aceito) e os 4 simulados são SIM-0, SIM-1, SIM-2, SIM-0-P2', [s['id'] for s in P16['simulados']] == ['SIM-0', 'SIM-1', 'SIM-2', 'SIM-0-P2'])

# ======================================================================= (7) E13 / T-65 (D1-T65-R1 a R3 da GCE; transporte ao Projeto é da GCE, gatilho E)
stats_ = json.load(open(os.path.join(OUT, 'stats.json'), encoding='utf-8'))
e13s = [e for e in stats_['errata'] if e['lote'] == 'L1' and e['id'] == 'E13']
chk('(7) E13', 'o registro de errata do gerador traz a L1 E13 uma vez, estado APLICADA (X encontrado 1 vez livre, Y ausente antes), aplicada ao comando da D1 depois da montagem com a E8 (D1-T65-R2)',
    len(e13s) == 1 and e13s[0]['estado'] == 'APLICADA' and e13s[0]['x_free'] == 1 and e13s[0]['y_free'] == 0, str(e13s))
sj = json.load(open(os.path.join(OUT, 'sync_check.json'), encoding='utf-8'))
chk('(7) E13', 'sync_check: a E13 (X e Y literais no Adendo 6 da consolidação) consta como conferida (x e y verdadeiros)', [(r['lote'], r['id'], r['x'], r['y']) for r in sj if r['id'] == 'E13'] == [('L1', 'E13', True, True)])
chk('(7) E13', 'GCE_Lote1_consolidacao_GCE.md (com o Adendo 6) tem SHA-256 604fa711f19949ab4560cece3dd3958b0f7582dd9af3560e5e7bc13c1df503bd, 11670 bytes e 213 quebras de linha (T65_reconciliacao, seção 1, ponto 1); termina em "FIM DO ADENDO 6"',
    hashlib.sha256(cons1_raw.encode('utf-8')).hexdigest() == '604fa711f19949ab4560cece3dd3958b0f7582dd9af3560e5e7bc13c1df503bd' and len(cons1_raw.encode('utf-8')) == 11670 and cons1_raw.count('\n') == 213 and cons1_raw.endswith('FIM DO ADENDO 6'))

fails = [r for r in res if not r[2]]
print('\n%d conferências; %d falhas' % (len(res), len(fails)))
with open(os.path.join(OUT, 'conferencias_v16.txt'), 'w', encoding='utf-8') as f:
    for c, alvo, ok, det in res:
        f.write(('OK    ' if ok else 'FALHA ') + c + ' | ' + alvo + (' | ' + det if det else '') + '\n')
    f.write('\n%d conferências; %d falhas\n' % (len(res), len(fails)))
json.dump([list(r) for r in res], open(os.path.join(OUT, 'conferencias_v16.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
sys.exit(1 if fails else 0)
