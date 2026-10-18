# -*- coding: utf-8 -*-
"""T-81 — conferências da ocorrência v1.8 do pacote, do pacote do estudante (JSON), da edição do estudante e do contrato (independentes do gerador, salvo onde dito).
Lê out/pacote.json, out/pacote_estudante.json e out/estudante/ (v1.8 gerados) e compara com a v1.7 aceita lida do git (refs.py: commit 62ab128, SHA-256 f20216c2…; edição v1.7 do mesmo commit),
e, como histórico, com a v1.6 (569c5dd, ecc284f9…), a v1.5 (a889100, b4bc65c7…), a v1.4 (e9b6402, f8c0c131…) e a v1.3 (9622604).
Numeração da D1 da GBQ (saida/pacote/T81_D1_escopo_v1_8_2026-10-17.md, 6.2):
(0) diff pacote.json v1.7 (git 62ab128) -> v1.8: EXATAMENTE `$.nome` e `$.geradoEm`; byte a byte pelas 2 trocas de texto; 621907 bytes e SHA-256 09d4a457…; contagens e partes idênticas às da v1.7.
(1) histórico: as conferências (1) da v1.7 (nome e geradoEm da v1.8): v1.6 -> v1.7, v1.5 -> v1.6 e o diff acumulado v1.3 -> v1.8.
(2) contrato: v1.2.4 (git) + C-1 a C-3 lidas da D1 = regras/pacote_contrato.md v1.2.5 (SHA-256 e tamanho lidos da seção 8 da D1).
(3) edição v1.7 (git) -> v1.8: 9 arquivos retirados, 8 alterados, 26 idênticos; conferência de reconstrução (itens, gabaritos, pegadinhas e curso do 1-C no L1; 4-C e 5-C nos L4 e L5); manifesto ordenado.
(4) identidade pacote.json v1.8 × pacote_estudante.json.
(5) pacote_estudante.json × edição v1.7 aceita (git), por leitura independente do script de deleção.
(6) pacote_estudante.json × edição v1.8 (34 arquivos): 100% coerente.
(7) varredura R na edição v1.8: os 11 casamentos da seção 2.4 e 0 de processo; MARK_RX do W.raw sem disparo.
(8) não regressão: T-59 e T-66 (regra v1.2, validador mantido, exemplo), gerador_v1_7/ sem diff, lista de arquivos do gerador_v1_8, rodar_tudo.sh, T-69 (4), varreduras da seção 3.5, CAIXA, REUNIÃO, contagens.
(9) mutações do JSON (M1 a M8), todas detectadas.
Sai com código 1 se houver falha."""
import collections, difflib, filecmp, hashlib, json, os, re, subprocess, sys, tempfile, copy
import refs
import estudante_marcas as em
import estudante_gen as gen
import marcas_processo as mp
import gce
from common import OUT, REPO as REPO_, read
from p2 import ERRATA


def rb_lf(path):
    """bytes de um arquivo do repositório com CRLF -> LF (o disco pode ter CRLF por core.autocrlf; todo SHA-256 da D1 é do conteúdo LF)."""
    return open(path, 'rb').read().replace(b'\r\n', b'\n')

def sha(b):
    return hashlib.sha256(b).hexdigest()

def est(commit):
    """edição de um commit (git archive), com CRLF -> LF (o archive aplica core.autocrlf no Windows)."""
    return {k: v.replace('\r\n', '\n') for k, v in refs.estudante(commit).items()}

PAC = sys.argv[1] if len(sys.argv) > 3 else os.path.join(OUT, 'pacote.json')
EST = sys.argv[2] if len(sys.argv) > 3 else os.path.join(OUT, 'estudante')
PACE = sys.argv[3] if len(sys.argv) > 3 else os.path.join(OUT, 'pacote_estudante.json')

raw18 = open(PAC, 'rb').read()
P18 = json.loads(raw18.decode('utf-8'))
rawE = open(PACE, 'rb').read()
JE = json.loads(rawE.decode('utf-8'), object_pairs_hook=collections.OrderedDict)
raw17g = refs.git_show(refs.C_V17, refs.PACOTE)
P17g = json.loads(raw17g.decode('utf-8'))
E17g = est(refs.C_V17)
raw15 = refs.git_show(refs.C_V15, refs.PACOTE)
P15 = json.loads(raw15.decode('utf-8'))
E15 = est(refs.C_V15)
raw16g = refs.git_show(refs.C_V16, refs.PACOTE)
P16g = json.loads(raw16g.decode('utf-8'))
E16g = est(refs.C_V16)
raw14 = refs.git_show(refs.C_V14, refs.PACOTE)
P14 = json.loads(raw14.decode('utf-8'))
E14 = est(refs.C_V14)
raw13 = refs.git_show(refs.C_V13, refs.PACOTE)
P13 = json.loads(raw13.decode('utf-8'))
raw12 = refs.git_show(refs.C_V12, refs.PACOTE)
P12 = json.loads(raw12.decode('utf-8'))
E13 = est(refs.C_V13)
E12 = est(refs.C_V12)
E18 = {f: open(os.path.join(EST, f), encoding='utf-8', newline='').read() for f in sorted(os.listdir(EST))}
def manifesto(E): return hashlib.sha256(''.join('%s  %s\n' % (hashlib.sha256(tx.encode('utf-8')).hexdigest(), f) for f, tx in sorted(E.items())).encode('utf-8')).hexdigest()

D1_TXT = open(os.path.join(REPO_, 'saida', 'pacote', 'T81_D1_escopo_v1_8_2026-10-17.md'), 'rb').read().decode('utf-8').replace('\r\n', '\n')
m_ = re.search(r'`pacote\.json` v1\.8 \(LF\): (\d+) bytes, SHA-256 `([0-9a-f]{64})`', D1_TXT)
SHA18_ESP, BYTES18_ESP = m_.group(2), int(m_.group(1))
m_ = re.search(r'CONTRATO-V125: (\d+) bytes, (\d+) linhas, SHA-256 `([0-9a-f]{64})`', D1_TXT)
CTR_BYTES, CTR_LINHAS, CTR_SHA = int(m_.group(1)), int(m_.group(2)), m_.group(3)

res = []
def chk(c, alvo, ok, detalhe=''):
    res.append((c, alvo, bool(ok), detalhe))
    print(('OK    ' if ok else 'FALHA ') + c + ' | ' + alvo + (' | ' + detalhe if detalhe else ''))

chk('BASE', 'v1.7 (git %s) tem SHA-256 f20216c22600b7af7cf54b4e79d83accf3568aee8de48ad970fe800451528c7a, 621907 bytes, e a edição v1.7 tem 43 arquivos com manifesto ordenado 67d2bdf85925a232 (D1 da T-81, seção 0: P1 e P2)' % refs.C_V17,
    sha(raw17g) == 'f20216c22600b7af7cf54b4e79d83accf3568aee8de48ad970fe800451528c7a' and len(raw17g) == 621907 and len(E17g) == 43 and manifesto(E17g)[:16] == '67d2bdf85925a232',
    'v1.7 %s | edição v1.7 %s' % (sha(raw17g)[:12], manifesto(E17g)[:16]))
chk('BASE', 'v1.4 (git %s) tem SHA-256 f8c0c131f16dab52b1646b3d302670a3afc498b23ac03a7b34a8ff97520ffa54, 621744 bytes, e a edição v1.4 tem 43 arquivos com manifesto ordenado 562c51398d1e64f8' % refs.C_V14,
    hashlib.sha256(raw14).hexdigest() == 'f8c0c131f16dab52b1646b3d302670a3afc498b23ac03a7b34a8ff97520ffa54' and len(raw14) == 621744 and len(E14) == 43 and manifesto(E14)[:16] == '562c51398d1e64f8',
    'v1.4 %s | edição v1.4 %s' % (hashlib.sha256(raw14).hexdigest()[:12], manifesto(E14)[:16]))
chk('BASE', 'v1.3 (git %s) tem SHA-256 fdcb7afdb4fb449229c6d530e877d839f8d334cd9667731e1b7222c9c7fb0eca, 620956 bytes, e a edição v1.3 tem 43 arquivos com manifesto ordenado 6a60f28116d9ec35' % refs.C_V13,
    hashlib.sha256(raw13).hexdigest() == 'fdcb7afdb4fb449229c6d530e877d839f8d334cd9667731e1b7222c9c7fb0eca' and len(raw13) == 620956 and len(E13) == 43 and manifesto(E13)[:16] == '6a60f28116d9ec35',
    'v1.3 %s | v1.8 %s' % (hashlib.sha256(raw13).hexdigest()[:12], hashlib.sha256(raw18).hexdigest()[:12]))
chk('BASE', 'v1.5 (git %s) tem SHA-256 b4bc65c7c5829994856665ae895f9b188be8167d5b78786819ea6cdeb97beef3, 621887 bytes, e a edição v1.5 tem 43 arquivos com manifesto ordenado 656e60e5085f3622' % refs.C_V15,
    hashlib.sha256(raw15).hexdigest() == 'b4bc65c7c5829994856665ae895f9b188be8167d5b78786819ea6cdeb97beef3' and len(raw15) == 621887 and len(E15) == 43 and manifesto(E15)[:16] == '656e60e5085f3622',
    'v1.5 %s | edição v1.5 %s' % (hashlib.sha256(raw15).hexdigest()[:12], manifesto(E15)[:16]))
chk('BASE', 'v1.6 (git %s) tem SHA-256 ecc284f9055f21046612e5afff7927eb72bf8a2283b7841c2c32c19c172d0a2e, 621907 bytes, e a edição v1.6 tem 43 arquivos com manifesto ordenado 01af0e342b9a7796' % refs.C_V16,
    hashlib.sha256(raw16g).hexdigest() == 'ecc284f9055f21046612e5afff7927eb72bf8a2283b7841c2c32c19c172d0a2e' and len(raw16g) == 621907 and len(E16g) == 43 and manifesto(E16g)[:16] == '01af0e342b9a7796',
    'v1.6 %s | edição v1.6 %s' % (hashlib.sha256(raw16g).hexdigest()[:12], manifesto(E16g)[:16]))
# a edição v1.7 aceita é a do HEAD do repositório em que a produção roda (D1, 3.3: "edição v1.7 (HEAD)"); no commit da v1.8 o HEAD já é outro, e vale o commit 62ab128
try:
    E17h = est('HEAD')
    chk('BASE', 'se o HEAD ainda é a v1.7 (antes do commit da v1.8): saida/estudante do HEAD = edição do commit %s (43 arquivos, mesmo manifesto) e saida/pacote/pacote.json do HEAD = f20216c2…' % refs.C_V17,
        (manifesto(E17h) == manifesto(E17g) and sha(refs.git_show('HEAD', refs.PACOTE)) == sha(raw17g)) or manifesto(E17h)[:16] != '67d2bdf85925a232', 'manifesto HEAD %s' % manifesto(E17h)[:16])
except Exception as e_:
    chk('BASE', 'edição do HEAD legível', False, str(e_))
d18_ = {d['id']: d for d in P18['discursivas']}


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

# ======================================================================= (0) diff v1.7 (git 62ab128) -> v1.8 do pacote (T-81: só `nome` e `geradoEm`; D1 da GBQ, 1.3 e 6.2 (0))
NOME17G, NOME18 = 'Câmara 2026 — pacote F4 (v1.7)', 'Câmara 2026 — pacote F4 (v1.8)'
s18 = raw18.decode('utf-8'); s17g = raw17g.decode('utf-8')
dif0 = []
walk_diff(P17g, P18, '', dif0)
chk('(0) DIFF v1.7->v1.8', 'diff estrutural v1.7 (git %s) -> v1.8 do pacote: EXATAMENTE 2 caminhos, `$.nome` e `$.geradoEm`; qualquer outro = falha (D1, 1.3)' % refs.C_V17,
    sorted((d[0], d[1]) for d in dif0) == sorted([('.nome', 'valor'), ('.geradoEm', 'valor')]), 'diferenças: %s' % [d[0] for d in dif0])
chk('(0) DIFF v1.7->v1.8', '`nome`: "%s" -> "%s"; `geradoEm`: "2026-10-14" -> "2026-10-17"; `versao` 1 nas duas; chaves de topo e sua ordem iguais' % (NOME17G, NOME18),
    P17g['nome'] == NOME17G and P18['nome'] == NOME18 and P17g['geradoEm'] == '2026-10-14' and P18['geradoEm'] == '2026-10-17' and P17g['versao'] == P18['versao'] == 1 and list(P17g.keys()) == list(P18.keys()))
def avanca18(t):
    """v1.7 -> v1.8 por substituição de texto (a única reconstrução esperada): `nome` (1x) e `geradoEm` (1x)"""
    a1, a2 = '"nome": "%s"' % NOME17G, '"geradoEm": "2026-10-14"'
    assert t.count(a1) == 1 and t.count(a2) == 1
    return t.replace(a1, '"nome": "%s"' % NOME18, 1).replace(a2, '"geradoEm": "2026-10-17"', 1)
l17g_, l18_ = s17g.split('\n'), s18.split('\n')
difl = [(k + 1, x, y) for k, (x, y) in enumerate(zip(l17g_, l18_)) if x != y]
chk('(0) DIFF v1.7->v1.8', 'byte a byte: aplicando à v1.7 só 2 trocas de texto (`nome` 1x e `geradoEm` 1x; cada uma ocorre 1 vez) obtém-se a v1.8 (%d bytes, os mesmos da v1.7: "7" -> "8" e "14" -> "17" mantêm o tamanho); %d linhas diferentes (linhas %s do JSON); SHA-256 %s (esperado na seção 8 da D1: %s, %d bytes); serialização json.dumps(indent=1, ensure_ascii=False) + "\\n"' % (len(raw18), len(difl), [d[0] for d in difl], sha(raw18), SHA18_ESP, BYTES18_ESP),
    avanca18(s17g).encode('utf-8') == raw18 and len(l17g_) == len(l18_) and len(difl) == 2 and len(raw18) == len(raw17g) == BYTES18_ESP == 621907 and sha(raw18) == SHA18_ESP and json.dumps(P18, ensure_ascii=False, indent=1) + '\n' == s18)
chk('(0) DIFF v1.7->v1.8', 'itens (286), simulados (4), lotes (10), edital (47) e discursivas (5) idênticos aos da v1.7, inteiros; ordem das chaves das discursivas igual',
    P17g['itens'] == P18['itens'] and P17g['simulados'] == P18['simulados'] and P17g['lotes'] == P18['lotes'] and P17g['edital'] == P18['edital'] and P17g['discursivas'] == P18['discursivas']
    and (len(P18['itens']), len(P18['simulados']), len(P18['lotes']), len(P18['discursivas']), len(P18['edital'])) == (286, 4, 10, 5, 47)
    and all(list(a.keys()) == list(b.keys()) for a, b in zip(P17g['discursivas'], P18['discursivas'])))
chk('(0) DIFF v1.7->v1.8', '286 itens, C/E 149/137, `volatil` 23, 0 "QA PENDENTE", 10 lotes, 4 simulados, 5 discursivas, 47 itens de edital, todos iguais aos da v1.7',
    len(P18['itens']) == 286 and sum(i['gabarito'] == 'C' for i in P18['itens']) == 149 and sum(i['gabarito'] == 'E' for i in P18['itens']) == 137 and sum(bool(i.get('volatil')) for i in P18['itens']) == 23
    and s18.count('QA PENDENTE') == 0 and len(P18['lotes']) == 10 and len(P18['simulados']) == 4 and len(P18['discursivas']) == 5 and len(P18['edital']) == 47 and s17g.count('QA PENDENTE') == 0)
chk('(0) DIFF v1.7->v1.8', 'a data da geração: `geradoEm` literal "2026-10-17" em build_pacote.py (sem relógio) e nenhuma leitura de data/hora do sistema no pipeline (D1, 6.3: determinismo)',
    "geradoEm='2026-10-17'" in read('saida/pacote/gerador_v1_8/build_pacote.py') and not any(re.search(r'\b(?:datetime|time\.time|time\.strftime|date\.today)\b', open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f), encoding='utf-8').read()) for f in ('build_pacote.py', 'estudante_gen.py', 'estudante_json.py', 'marcas_processo.py', 'p2.py', 'p1.py', 'banco.py', 'common.py')))
chk('(0) DIFF v1.7->v1.8', 'E13 e T-54 já aplicadas (F4 e F5 da T81_exequibilidade): a E13 ("de até 20 linhas") está no comando da D1 e do D2 do pacote v1.8 (2 ocorrências de Y, 0 de X) e o curso do L3 traz "que se possa afirmar" (0 "que eu possa afirmar"); a v1.8 não mexe nelas',
    s18.count('redija texto dissertativo, de até 20 linhas, em que você') == 2 and s18.count('redija texto dissertativo em que você') == 0 and s18.count('que eu possa afirmar') == 0 and s18.count('jurisprudência firmada que se possa afirmar):') == 1)

# ======================================================================= (0) diff v1.6 -> v1.7 do pacote (T-71: só `nome`; D-T71-01, T70_T71_decisoes 5.1)
nz = lambda s: re.sub(r'\s+', ' ', s)
NOME15, NOME16, NOME17 = 'Câmara 2026 — pacote F4 (v1.5)', 'Câmara 2026 — pacote F4 (v1.6)', 'Câmara 2026 — pacote F4 (v1.7)'
SHA17_ESP = 'f20216c22600b7af7cf54b4e79d83accf3568aee8de48ad970fe800451528c7a'
s17g = raw17g.decode('utf-8'); s16g = raw16g.decode('utf-8')
dif0 = []
walk_diff(P16g, P17g, '', dif0)
chk('(1) HIST v1.6->v1.7', 'diff estrutural v1.6 (git %s) -> v1.7 do pacote: exatamente 1 diferença, `$.nome`; `$.geradoEm` não difere (2026-10-14 nas duas); qualquer outra = falha (D-T71-01)' % refs.C_V16,
    [(d[0], d[1]) for d in dif0] == [('.nome', 'valor')] and P16g['geradoEm'] == P17g['geradoEm'] == '2026-10-14', 'diferenças: %s' % [d[0] for d in dif0])
chk('(1) HIST v1.6->v1.7', '`nome`: "%s" -> "%s"; `geradoEm` "2026-10-14" nas duas; `versao` 1 nas duas; chaves de topo e sua ordem iguais' % (NOME16, NOME17),
    P16g['nome'] == NOME16 and P17g['nome'] == NOME17 and P16g['versao'] == P17g['versao'] == 1 and list(P16g.keys()) == list(P17g.keys()))
def avanca17g(t):
    """v1.6 -> v1.7 por substituição de texto (a única reconstrução esperada): `nome` (1x)"""
    assert t.count('"nome": "%s"' % NOME16) == 1 and t.count('v1.6') == 1 and t.count('v1.7') == 0
    return t.replace('"nome": "%s"' % NOME16, '"nome": "%s"' % NOME17, 1)
l16g_, l17g_ = s16g.split('\n'), s17g.split('\n')
d17g_ = {d['id']: d for d in P17g['discursivas']}
difl = [(k + 1, x, y) for k, (x, y) in enumerate(zip(l16g_, l17g_)) if x != y]
chk('(1) HIST v1.6->v1.7', 'byte a byte: aplicando à v1.6 só 1 troca de texto (`nome`, 1x; "v1.6" ocorre 1 vez no texto da v1.6 e "v1.7" nenhuma) obtém-se a v1.7 (%d bytes, os mesmos da v1.6: "6" -> "7" mantém o tamanho); %d linha diferente (linha %s do JSON); SHA-256 %s; serialização json.dumps(indent=1, ensure_ascii=False) + "\\n"' % (len(raw17g), len(difl), [d[0] for d in difl], hashlib.sha256(raw17g).hexdigest()),
    avanca17g(s16g).encode('utf-8') == raw17g and len(l16g_) == len(l17g_) and len(difl) == 1 and len(raw17g) == len(raw16g) == 621907 and hashlib.sha256(raw17g).hexdigest() == SHA17_ESP and json.dumps(P17g, ensure_ascii=False, indent=1) + '\n' == s17g)
chk('(1) HIST v1.6->v1.7', 'itens (286), simulados (4), lotes (10), edital (47) e discursivas (5) idênticos aos da v1.6, inteiros (aspectos, quesitos, valores, `padrao`, `comando`, gabarito); ordem das chaves das discursivas igual',
    P16g['itens'] == P17g['itens'] and P16g['simulados'] == P17g['simulados'] and P16g['lotes'] == P17g['lotes'] and P16g['edital'] == P17g['edital'] and P16g['discursivas'] == P17g['discursivas']
    and (len(P17g['itens']), len(P17g['simulados']), len(P17g['lotes']), len(P17g['discursivas']), len(P17g['edital'])) == (286, 4, 10, 5, 47)
    and all(list(a.keys()) == list(b.keys()) for a, b in zip(P16g['discursivas'], P17g['discursivas'])))
chk('(1) HIST v1.6->v1.7', 'a data da geração: `geradoEm` literal "2026-10-14" em build_pacote.py (sem relógio) e nenhuma leitura de data/hora do sistema no pipeline (a D1, 5.1: execução em 2026-10-14, America/Sao_Paulo)',
    "geradoEm='2026-10-14'" in read('saida/pacote/gerador_v1_7/build_pacote.py') and not any(re.search(r'\b(?:datetime|time\.time|time\.strftime|date\.today)\b', open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f), encoding='utf-8').read()) for f in ('build_pacote.py', 'estudante_gen.py', 'p2.py', 'p1.py', 'banco.py', 'common.py')))
# ======================================================================= (1) histórico: diff v1.5 -> v1.6 do pacote (T-67: nome e E13 da T-65; D1-T65-R2), v1.6 = git C_V16
# E13: X e Y escritos aqui como literais (D1-T65-R2 da GCE e linha T-65 de TAREFAS.md) e conferidos contra o Adendo 6 da consolidação (leitura independente do p2.py)
E13_X = 'redija texto dissertativo em que você'
E13_Y = 'redija texto dissertativo, de até 20 linhas, em que você'
cons1_raw = read('saida/gce/GCE_Lote1_consolidacao_GCE.md')
v2cpp_raw = read('saida/gce/GCE_Lote1_v2_CPP.md')
ad6 = nz(cons1_raw)[nz(cons1_raw).index('ADENDO 6 GCE'):]
m13 = re.findall(r'onde se lê "([^"]+)", leia-se "([^"]+)"', ad6)
chk('(1) HIST E13', 'literais da E13 = os do Adendo 6 de GCE_Lote1_consolidacao_GCE.md ("onde se lê" X, "leia-se" Y; 1 par); X ocorre 1 vez em GCE_Lote1_v2_CPP.md (enunciado (e), comando da D1) e Y nenhuma; o arquivo do lote (v2_CPP) fica intacto',
    m13 == [(E13_X, E13_Y)] and nz(v2cpp_raw).count(E13_X) == 1 and nz(v2cpp_raw).count(E13_Y) == 0
    and hashlib.sha256(v2cpp_raw.encode('utf-8')).hexdigest() == '5ac069292b122defe859064f25cf99a8aec189991cd19b703086cd9a06553228' and len(v2cpp_raw.encode('utf-8')) == 42195)
dif0 = []
walk_diff(P15, P16g, '', dif0)
chk('(1) HIST v1.5->v1.6', 'diff estrutural v1.5 (git %s) -> v1.6 do pacote: exatamente 2 diferenças, `$.nome` e `$.discursivas[0].comando` (D1); `$.geradoEm` não difere (2026-10-14 nas duas); qualquer outra = falha (D-V16-ESCOPO, item 7; D1-T65-R2)' % refs.C_V15,
    sorted((d[0], d[1]) for d in dif0) == sorted([('.nome', 'valor'), ('.discursivas[0].comando', 'valor')]) and P16g['discursivas'][0]['id'] == 'D1' and P15['geradoEm'] == P16g['geradoEm'] == '2026-10-14',
    'diferenças: %s' % [d[0] for d in dif0])
chk('(1) HIST v1.5->v1.6', '`nome`: "%s" -> "%s"; `geradoEm` "2026-10-14" nas duas; `versao` 1 nas duas; chaves de topo e sua ordem iguais' % (NOME15, NOME16),
    P15['nome'] == NOME15 and P16g['nome'] == NOME16 and P15['versao'] == P16g['versao'] == 1 and list(P15.keys()) == list(P16g.keys()))
s16g = raw16g.decode('utf-8'); s15 = raw15.decode('utf-8')
def avanca(t):
    """v1.5 -> v1.6 por substituição de texto (a única reconstrução esperada): nome (1x) e a E13 no comando da D1 (X 1x no texto do JSON)"""
    assert t.count('"nome": "%s"' % NOME15) == 1 and t.count(E13_X) == 1 and t.count(E13_Y) == 1
    return t.replace('"nome": "%s"' % NOME15, '"nome": "%s"' % NOME16, 1).replace(E13_X, E13_Y, 1)
l15_, l16g_ = s15.split('\n'), s16g.split('\n')
difl = [(k + 1, x, y) for k, (x, y) in enumerate(zip(l15_, l16g_)) if x != y]
ins = ', de até 20 linhas,'
chk('(1) HIST v1.5->v1.6', 'byte a byte: aplicando à v1.5 só as 2 trocas de texto (`nome` [1x] e X -> Y no comando da D1 [1x]) obtém-se a v1.6 (%d bytes; v1.5: 621887; +%d bytes = os %d bytes da inserção "%s"); %d linhas diferentes (linhas %s do JSON: a de `nome` e a do `comando` de D1); serialização json.dumps(indent=1, ensure_ascii=False) + "\\n"' % (len(raw16g), len(raw16g) - len(raw15), len(ins.encode('utf-8')), ins, len(difl), [d[0] for d in difl]),
    avanca(s15).encode('utf-8') == raw16g and len(l15_) == len(l16g_) and len(difl) == 2 and len(raw16g) - len(raw15) == len(ins.encode('utf-8')) and json.dumps(P16g, ensure_ascii=False, indent=1) + '\n' == s16g)
d15_ = {d['id']: d for d in P15['discursivas']}; d16g_ = {d['id']: d for d in P16g['discursivas']}
chk('(1) HIST v1.5->v1.6', 'D1: comando v1.6 = comando v1.5 com UMA troca (X -> Y; a inserção "%s" depois de "dissertativo"); id, tipo, aspectos, padrao e quesitos da D1 idênticos aos da v1.5 (0 aspecto, quesito, valor, padrão ou gabarito alterado); D2, D3, D4 e D5 idênticas, inteiras; ordem das chaves igual' % ins,
    d16g_['D1']['comando'] == d15_['D1']['comando'].replace(E13_X, E13_Y) and d15_['D1']['comando'].count(E13_X) == 1 and d16g_['D1']['comando'].count(E13_Y) == 1 and d16g_['D1']['comando'].count(E13_X) == 0
    and {k: v for k, v in d15_['D1'].items() if k != 'comando'} == {k: v for k, v in d16g_['D1'].items() if k != 'comando'} and all(d15_[x] == d16g_[x] for x in ('D2', 'D3', 'D4', 'D5')) and list(d15_) == list(d16g_) and all(list(d15_[x].keys()) == list(d16g_[x].keys()) for x in d15_))
chk('(1) HIST v1.5->v1.6', 'valores e aspectos da D1 iguais (soma de `aspectos[].valor` por discursiva: D1 %s, D2 %s, D3 %s, D4 %s, D5 %s, as mesmas da v1.5)' % tuple(round(sum(a['valor'] or 0 for a in d16g_[x]['aspectos']), 2) for x in ('D1', 'D2', 'D3', 'D4', 'D5')),
    all(round(sum(a['valor'] or 0 for a in d16g_[x]['aspectos']), 2) == round(sum(a['valor'] or 0 for a in d15_[x]['aspectos']), 2) for x in d15_) and [len(d16g_[x]['aspectos']) for x in d16g_] == [len(d15_[x]['aspectos']) for x in d15_] and [len(d16g_[x]['quesitos']) for x in d16g_] == [len(d15_[x]['quesitos']) for x in d15_])
n20 = {d['id']: d['comando'].count('20 linhas') for d in P16g['discursivas']}
chk('(1) HIST v1.5->v1.6', 'estado esperado (D1-T65-R2): "20 linhas" nos comandos D1 1, D2 1, D3 0, D4 1, D5 0 (v1.5: D1 0, D2 1, D3 0, D4 1, D5 0); no pacote inteiro X 0 e Y 2 (D1 e D2); "Redija texto dissertativo, de até 20 linhas" 1 vez (D4)',
    n20 == {'D1': 1, 'D2': 1, 'D3': 0, 'D4': 1, 'D5': 0} and {d['id']: d['comando'].count('20 linhas') for d in P15['discursivas']} == {'D1': 0, 'D2': 1, 'D3': 0, 'D4': 1, 'D5': 0}
    and s16g.count(E13_X) == 0 and s16g.count(E13_Y) == 2 and s16g.count('Redija texto dissertativo, de até 20 linhas') == 1, str(n20))
chk('(1) HIST v1.5->v1.6', 'itens (286), simulados (4), lotes (10) e edital (47) idênticos aos da v1.5; discursivas (5): só o comando da D1 difere',
    P15['itens'] == P16g['itens'] and P15['simulados'] == P16g['simulados'] and P15['lotes'] == P16g['lotes'] and P15['edital'] == P16g['edital']
    and (len(P16g['itens']), len(P16g['simulados']), len(P16g['lotes']), len(P16g['discursivas']), len(P16g['edital'])) == (286, 4, 10, 5, 47))
cnt16 = lambda t: [d['id'] for d in P18['discursivas'] if t in d['padrao']]
chk('(1) T-64', 'estado esperado da GCE (D1-T64-5) em `discursivas[*].padrao`, mantido na v1.8: "NQ = NC − 3 × NE ÷ TL" em D1, D4 e D5 (3); "NPT = NC − 6 × NE ÷ TL" em D3, D4 e D5 (3); "NQ = NC" em D3: 0; D2 sem nota de fórmula; "9.8.5.1, d" com NQ em D3: 0',
    cnt16('NQ = NC − 3 × NE ÷ TL') == ['D1', 'D4', 'D5'] and cnt16('NPT = NC − 6 × NE ÷ TL') == ['D3', 'D4', 'D5'] and 'NQ = NC' not in d18_['D3']['padrao'] and 'NE ÷ TL' not in d18_['D2']['padrao'] and '9.8.5.1' not in d18_['D3']['padrao']
    and 'NQ = NC' in d18_['D1']['padrao'] and '(9.8.5.1, d)' in d18_['D4']['padrao'] and '(9.8.5.2, d)' in d18_['D5']['padrao'])
# ======================================================================= (1) diff acumulado v1.3 -> v1.8 (testes da v1.4, com nome e geradoEm da v1.8)
dif = []
walk_diff(P13, P18, '', dif)
def nome_caminho(p):
    m = re.match(r'^\.(lotes|simulados|discursivas)\[(\d+)\](.*)$', p)
    if m: return '%s[%s]%s' % (m.group(1), P18[m.group(1)][int(m.group(2))]['id'], m.group(3))
    return p
dif_n = sorted((nome_caminho(d[0]), d[1]) for d in dif)
ID_LOTES = {'L4': 20, 'L5': 15, 'L6A': 19, 'L6B': 18}
esperado = sorted([('.nome', 'valor'), ('.geradoEm', 'valor'), ('discursivas[D3].padrao', 'valor'), ('discursivas[D4].padrao', 'valor'), ('discursivas[D5].padrao', 'valor'), ('discursivas[D1].comando', 'valor'), ('lotes[L3].curso', 'valor')] +
                  [('lotes[%s].pares[%d].id' % (lid, k), 'acrescentado') for lid, n in ID_LOTES.items() for k in range(n)])
chk('(1) DIFF', 'v1.3 -> v1.8 (acumulado) do pacote: só nome (valor), geradoEm (valor: 2026-10-13 -> 2026-10-17), `id` em 72 pares (acrescentado), comando da D1 (valor; E13 da T-65), padrao da D3, da D4 e da D5 (valor) e curso do L3 (valor); qualquer outra diferença = falha',
    dif_n == esperado and P13['geradoEm'] == '2026-10-13' and P18['geradoEm'] == '2026-10-17', 'diferenças: %d (1 nome + 1 geradoEm + 72 id + 1 comando D1 (E13) + 3 padrao D3/D4/D5 + 1 curso L3)' % len(dif_n))
nome_d = [d for d in dif if d[0] == '.nome'][0]
chk('(1) DIFF', 'nome: "%s" -> "%s"; versao 1 nas duas' % (nome_d[2], nome_d[3]), nome_d[2] == 'Câmara 2026 — pacote F4 (v1.3)' and nome_d[3] == 'Câmara 2026 — pacote F4 (v1.8)' and P13['versao'] == P18['versao'] == 1)
# `id` de par: 72 entradas, primeira chave, igual ao rótulo do arquivo canônico (leitura independente)
CANON = {'L4': 'saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md', 'L5': 'saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md', 'L6A': 'saida/gcb/GCB_Lote6a_v2_producao_auto.md', 'L6B': 'saida/gcb/GCB_Lote6b_v2_producao_auto.md'}
def canon_gcb(lid):
    ln = read(CANON[lid]).split('\n')
    c0 = next(i for i, l in enumerate(ln) if l.startswith('(c) PARES'))
    e2 = next(i for i in range(c0, len(ln)) if ln[i].startswith('FIM DA PARTE 2/3'))
    return [(m.group(1), m.group(2)) for m in (re.match(r'^(C\d+)\.\s+(.*)$', l) for l in ln[c0 + 1:e2]) if m]
LB15 = {l['id']: l for l in P18['lotes']}; LB13 = {l['id']: l for l in P13['lotes']}
okid = True; detid = []
for lid, n in ID_LOTES.items():
    can = canon_gcb(lid)
    ids = [p['id'] for p in LB15[lid]['pares']]
    ok = len(ids) == n == len(can) and ids == [c[0] for c in can] == ['C%d' % k for k in range(1, n + 1)] and all(list(p.keys()) == ['id', 'a', 'b', 'como'] for p in LB15[lid]['pares'])
    # a/b/como iguais aos da v1.3, par a par; e o texto do rótulo canônico é "<id>. a × b | como" (junção)
    ok = ok and all({k: v for k, v in p.items() if k != 'id'} == q for p, q in zip(LB15[lid]['pares'], LB13[lid]['pares']))
    okid &= ok; detid.append('%s %d %s' % (lid, len(ids), 'ok' if ok else 'FALHA'))
chk('(1) DIFF', 'cada `id` de par (72) é o rótulo "C<n>." da seção (c) do canônico do lote, na ordem (L4 C1–C20, L5 C1–C15, L6A C1–C19, L6B C1–C18), é a primeira chave, e a/b/como são idênticos aos da v1.3', okid, ', '.join(detid))
chk('(1) DIFF', 'L1, L1C, L2 e L3 sem `id` (0 de 67 pares); L4C e L5C sem pares', all('id' not in p for l in P18['lotes'] if l['id'] not in ID_LOTES for p in l['pares']) and sum(len(l['pares']) for l in P18['lotes'] if l['id'] not in ID_LOTES) == 67 and not LB15['L4C']['pares'] and not LB15['L5C']['pares'])
ref = {('L5', 'C1'): ('Histograma', 'gráfico de barras'), ('L5', 'C14'): ('Storytelling', 'dashboard'), ('L4', 'C19'): ('Injeção de prompt', 'jailbreak (conceitos gerais)')}
chk('(1) DIFF', 'remissões: L5 C1 = Histograma × gráfico de barras; L5 C14 = Storytelling × dashboard; L4 C19 = Injeção de prompt × jailbreak (conceitos gerais)',
    all(any(p['id'] == k[1] and (p['a'], p['b']) == v for p in LB15[k[0]]['pares']) for k, v in ref.items()))
# curso do L3: uma troca
a13, a14 = LB13['L3']['curso'], LB15['L3']['curso']
OLD, NEW = 'jurisprudência firmada que eu possa afirmar):', 'jurisprudência firmada que se possa afirmar):'
chk('(1) DIFF', 'curso do L3: igual ao da v1.3 com UMA troca ("eu" -> "se" em "jurisprudência firmada que eu possa afirmar):"); 0 "que eu possa afirmar" no pacote', a13.count(OLD) == 1 and a14 == a13.replace(OLD, NEW) and 'que eu possa afirmar' not in raw18.decode('utf-8') and a14.count(NEW) == 1,
    'caracteres %d -> %d' % (len(a13), len(a14)))
canon3 = read('saida/gce/GCE_Lote3_v2_CPP.md')
nz = lambda s: re.sub(r'\s+', ' ', s)
chk('(1) DIFF', 'o canônico atual do L3 (GCE_Lote3_v2_CPP.md, T-58) traz a errata no curso (1x) e o registro "T-54" na Tabela de Correções; o curso do pacote = curso lido do canônico (sem outra mudança desde a v1.3)',
    nz(canon3).count(NEW) == 1 and nz(canon3).count('"que eu possa afirmar" → "que se possa afirmar"') == 1 and nz(canon3).count('T-54 → (a), 4.2, bloco "CONTROVERSO / NÃO GABARITO"') == 1)
# D5
d13 = {d['id']: d for d in P13['discursivas']}; d14 = {d['id']: d for d in P18['discursivas']}
pad = read('saida/gce/GCE_Lote3_padroes_GCE.md').split('\n')
r2 = '\n'.join(l.rstrip() for l in pad[13:20])      # linhas 14–20: nota R2
r34 = '\n'.join(l.rstrip() for l in pad[20:23])     # linhas 21–23: notas R3 e R4
p13, p14 = d13['D5']['padrao'].replace(R6_ANT, R6_NOVA), d14['D5']['padrao']      # a troca da R6 (T-64) é conferida em (0); aqui só o que a T-54 mudou
assert d13['D5']['padrao'].count(R6_ANT) == 1
anexo13 = 'Notas de correção (GCE, R2–R4)\n' + r2 + '\n' + r34
anexo14 = 'Notas de correção (GCE, R3–R4)\n' + r34
chk('(1) DIFF', 'D5: padrao v1.8 = padrao v1.3 (com a R6 trocada pela da T-64) sem o trecho literal da nota R2 (linhas 14–20 de GCE_Lote3_padroes_GCE.md, 7 linhas) e com o rótulo "Notas de correção (GCE, R3–R4)"; anexo v1.4 = linhas 21–23 literais; comando, aspectos e quesitos da D5 iguais',
    p13.endswith(anexo13) and p14 == p13[:len(p13) - len(anexo13)] + anexo14 and 'R2.' not in p14 and 'Alínea c da discursiva' not in p14 and r2.count('\n') == 6 and {k: v for k, v in d13['D5'].items() if k != 'padrao'} == {k: v for k, v in d14['D5'].items() if k != 'padrao'})
chk('(1) DIFF', 'D4: igual à da v1.3 salvo a troca da R6 (T-64); padrao com o anexo R2–R4 (linhas 14–23 literais) e rótulo "Notas de correção (GCE, R2–R4)"; D2 idêntica; D1 igual à da v1.3 salvo o comando (E13, T-65); D3 igual à da v1.3 salvo a troca da nota da peça (T-64)',
    {k: v for k, v in d13['D4'].items() if k != 'padrao'} == {k: v for k, v in d14['D4'].items() if k != 'padrao'} and d14['D4']['padrao'] == d13['D4']['padrao'].replace(R6_ANT, R6_NOVA) and d13['D4']['padrao'].count(R6_ANT) == 1
    and d14['D4']['padrao'].endswith('Notas de correção (GCE, R2–R4)\n' + r2 + '\n' + r34) and d13['D2'] == d14['D2'] and {k: v for k, v in d13['D1'].items() if k != 'comando'} == {k: v for k, v in d14['D1'].items() if k != 'comando'} and d14['D1']['comando'] == d13['D1']['comando'].replace(E13_X, E13_Y) and d14['D3']['padrao'] == d13['D3']['padrao'].replace(N2_ANT, N2_NOVA) and {k: v for k, v in d13['D3'].items() if k != 'padrao'} == {k: v for k, v in d14['D3'].items() if k != 'padrao'})
def ordem_chaves(P):
    return [list(P.keys())] + [list(i.keys()) for i in P['itens']] + [list(l.keys()) for l in P['lotes']] + [list(p.keys()) for l in P['lotes'] for p in l['pares']] + [list(s.keys()) for s in P['simulados']] + [list(d.keys()) for d in P['discursivas']]
oc13 = ordem_chaves(P13); oc14 = [[k for k in ks if k != 'id'] if ks[:2] == ['id', 'a'] else ks for ks in ordem_chaves(P18)]
chk('(1) DIFF', 'ordem das chaves: as mesmas da v1.3, salvo `id` como primeira chave dos 72 pares', oc13 == oc14)
chk('(1) DIFF', 'serialização: indent=1, ensure_ascii=False, newline final; 286 itens idênticos (enunciado, comando, comandoOriginal, textoBase, gabarito, justificativa, itemEdital, aderencia, volatil, nota); simulados idênticos', json.dumps(P18, ensure_ascii=False, indent=1) + '\n' == raw18.decode('utf-8')
    and P13['itens'] == P18['itens'] and len(P18['itens']) == 286 and P13['simulados'] == P18['simulados'] and P13['edital'] == P18['edital'])

# ======================================================================= (2) contrato v1.2.4 -> v1.2.5 (T-81; D1 da GBQ, seção 4: C-1 a C-3 lidas desta D1)
def blocos_d1():
    """{C-n: texto} lidos da D1 por varredura de linhas: o texto entre a linha "```text" que segue o título "#### C-n" e a "```" seguinte, sem as cercas, sem newline final."""
    ln = D1_TXT.split('\n'); out = collections.OrderedDict()
    for k, l in enumerate(ln):
        m = re.match(r'^#### (C-\d)\b', l)
        if m:
            assert ln[k + 1] == '```text', ln[k + 1]
            j = ln.index('```', k + 2)
            out[m.group(1)] = '\n'.join(ln[k + 2:j])
    return out
BL = blocos_d1()
ctr_antes = refs.git_show(refs.C_V17, 'regras/pacote_contrato.md').decode('utf-8')      # v1.2.4 (commit da v1.7; no commit da v1.8 o HEAD já é a v1.2.5)
ctr_depois = rb_lf(os.path.join(REPO_, 'regras', 'pacote_contrato.md')).decode('utf-8')
def aplica_c(base):
    """C-1 a C-3 por operação em lista de linhas (independente do programa de aplicação da produção)."""
    ls = base.split('\n'); occ = []
    # C-1: substitui a linha 1 inteira
    ls[0] = BL['C-1']; occ.append(1)
    # C-2: "antes" = 'ver a seção "Errata de forma da v1.2.4".' com 1 ocorrência, no fim da linha 3; "depois" = antes + " " + bloco
    a2 = 'ver a seção "Errata de forma da v1.2.4".'
    ks = [k for k, l in enumerate(ls) if a2 in l]; occ.append(len(ks))
    assert len(ks) == 1 and ls[ks[0]].endswith(a2) and ks[0] == 2
    ls[ks[0]] = ls[ks[0]] + ' ' + BL['C-2']
    # C-3: "antes" = "Registro: `…contrato_v1_2_4_2026-10-14.md`.\n\n---\n" (1 ocorrência); "depois" = antes sem a "---" + bloco + "\n\n---\n"
    a3 = 'Registro: `saida/pacote/contrato_v1_2_4_2026-10-14.md`.'
    ks = [k for k, l in enumerate(ls) if l.endswith(a3) and ls[k + 1] == '' and ls[k + 2] == '---']; occ.append(len(ks))      # a frase "Registro: …" fecha o ponto 3 da errata da v1.2.4 (linha 137)
    assert len(ks) == 1
    k = ks[0]
    ls[k + 1:k + 2] = [''] + BL['C-3'].split('\n') + ['']
    return '\n'.join(ls), occ
ctr_rec, occ_c = aplica_c(ctr_antes)
LA, LD = ctr_antes.split('\n'), ctr_depois.split('\n')
ops = [o for o in difflib.SequenceMatcher(None, LA, LD, autojunk=False).get_opcodes() if o[0] != 'equal']
chk('(2) CONTRATO v1.2.5', 'base: regras/pacote_contrato.md v1.2.4 (git %s) tem SHA-256 75e6a5009be70f5be3cb3e7b9b5087b96086a0884831419d6818fa27babdb27e, 32266 bytes e 143 linhas (D1, P3); C-1 a C-3 lidas dos blocos literais da D1 (3 blocos, na ordem)' % refs.C_V17,
    sha(ctr_antes.encode('utf-8')) == '75e6a5009be70f5be3cb3e7b9b5087b96086a0884831419d6818fa27babdb27e' and len(ctr_antes.encode('utf-8')) == 32266 and ctr_antes.count('\n') == 143 and list(BL) == ['C-1', 'C-2', 'C-3'])
chk('(2) CONTRATO v1.2.5', 'cada "antes" de C-1 a C-3 ocorre exatamente 1 vez no estado anterior à troca: %s' % occ_c, occ_c == [1, 1, 1])
chk('(2) CONTRATO v1.2.5', 'regras/pacote_contrato.md (arquivo atual, conteúdo LF) é igual, caractere a caractere, à v1.2.4 com C-1 a C-3 aplicadas, reconstruído por script: SHA-256 %s, %d bytes, %d linhas (seção 8 da D1, linha CONTRATO-V125); sem BOM' % (CTR_SHA, CTR_BYTES, CTR_LINHAS),
    ctr_rec == ctr_depois and sha(ctr_depois.encode('utf-8')) == CTR_SHA and len(ctr_depois.encode('utf-8')) == CTR_BYTES == 35460 and ctr_depois.count('\n') == CTR_LINHAS == 154 and not ctr_depois.startswith('﻿'),
    'SHA-256 %s' % sha(ctr_depois.encode('utf-8'))[:12])
chk('(2) CONTRATO v1.2.5', 'diff linha a linha v1.2.4 -> v1.2.5: 2 linhas trocadas (1 e 3) e 11 inseridas (o bloco C-3, 10 linhas, mais 1 linha em branco); 0 outra linha alterada; 154 - 143 = 11',
    [(o[0], o[2] - o[1], o[4] - o[3]) for o in ops][:2] == [('replace', 1, 1), ('replace', 1, 1)] and len(ops) == 3 and ops[2][0] == 'insert' and ops[2][4] - ops[2][3] == 11 and len(LD) - len(LA) == 11 and [o[1] + 1 for o in ops[:2]] == [1, 3],
    'operações: ' + '; '.join('%s antes[%d:%d] depois[%d:%d]' % o for o in ops))
chk('(2) CONTRATO v1.2.5', 'linha 1 = "# pacote.json — contrato de dados entre a fábrica e a plataforma (v1.2.5, 2026-10-17)" (0 "v1.2.4" na linha 1); a seção "Errata de forma da v1.2.5 (T-81;" existe 1 vez; a linha 3 cita a v1.2.5 e remete à seção "Errata de forma da v1.2.5"',
    LD[0] == '# pacote.json — contrato de dados entre a fábrica e a plataforma (v1.2.5, 2026-10-17)' and ctr_depois.count('Errata de forma da v1.2.5 (T-81;') == 1 and 'ver a seção "Errata de forma da v1.2.5".' in LD[2] and 'v1.2.4' not in LD[0])
def fence_json(txt): return re.search(r'```json\n(.*?)\n```', txt, re.S).group(1)
chk('(2) CONTRATO v1.2.5', 'nenhum campo obrigatório mudou: exemplo JSON, parágrafo "Regras:" (campos obrigatórios) e todas as regras e errata até a v1.2.4 idênticos (do início da seção "Regras da v1.1" ao "Registro" da v1.2.4); `versao` continua 1; a errata diz que não muda nome, tipo nem obrigatoriedade de nenhum campo do `pacote.json` e não muda `versao`; só acrescenta o arquivo opcional `pacote_estudante.json`',
    fence_json(ctr_antes) == fence_json(ctr_depois) and '"versao": 1' in fence_json(ctr_depois) and [l for l in LA if l.startswith('Regras: `gabarito`')] == [l for l in LD if l.startswith('Regras: `gabarito`')] != []
    and ctr_antes[ctr_antes.index('Regras da v1.1 (T-26):'):ctr_antes.index('Registro: `saida/pacote/contrato_v1_2_4_2026-10-14.md`.')] == ctr_depois[ctr_depois.index('Regras da v1.1 (T-26):'):ctr_depois.index('Registro: `saida/pacote/contrato_v1_2_4_2026-10-14.md`.')]
    and 'Esta errata não muda nome, tipo nem obrigatoriedade de nenhum campo do `pacote.json` e não muda `versao` (continua 1; regra (g) da v1.2). Um leitor da v1.2.4 continua lendo a v1.2.5.' in ctr_depois)
reg_c = rb_lf(os.path.join(REPO_, 'saida', 'pacote', 'contrato_v1_2_5_2026-10-17.md')).decode('utf-8')
chk('(2) CONTRATO v1.2.5', 'o registro saida/pacote/contrato_v1_2_5_2026-10-17.md existe e traz o SHA-256 antes (75e6a500…) e depois (%s…) e a confirmação de que os blocos foram lidos por programa da D1' % CTR_SHA[:8],
    '75e6a5009be70f5be3cb3e7b9b5087b96086a0884831419d6818fa27babdb27e' in reg_c and CTR_SHA in reg_c and 'por programa' in reg_c and reg_c.startswith('# contrato_v1_2_5_2026-10-17.md — T-81 — 2026-10-17 — gerado por gbq-csc'))
CAMPOS = ['id', 'rotulo', 'certame', 'cargo', 'ano', 'numero', 'comando', 'textoBase', 'enunciado', 'gabarito', 'justificativa', 'itemEdital', 'aderencia', 'url']
chk('(2) CONTRATO v1.2.5', 'o pacote v1.8 cumpre os 14 campos obrigatórios de item e as chaves de topo do contrato: 286/286 itens com os 14 campos; chaves de topo = versao, geradoEm, nome, edital, itens, simulados, lotes, discursivas; o pacote_estudante.json tem as mesmas chaves de topo e os mesmos 14 campos nos 286 itens',
    all(all(k in i for k in CAMPOS) for i in P18['itens']) and list(P18.keys()) == ['versao', 'geradoEm', 'nome', 'edital', 'itens', 'simulados', 'lotes', 'discursivas'] and list(JE.keys()) == list(P18.keys()) and all(all(k in i for k in CAMPOS) for i in JE['itens']))
t59 = read('saida/pacote/T59_decisoes_2026-10-14.md').split('\n')
def bloco_apos(prefixo, cerca):
    i = next(k for k, l in enumerate(t59) if l.startswith(prefixo))
    a = next(k for k in range(i, len(t59)) if t59[k].startswith(cerca)); b = t59.index('```', a + 1)
    return t59[a + 1:b]
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

# ======================================================================= (3) edição v1.7 (git) -> v1.8 (D1, 3.3)
REMOV = sorted('%s_%s.md' % (c, k) for c in ('L1C', 'L4C', 'L5C') for k in ('estudo', 'itens', 'gabarito'))
ALT = sorted(['README.md', 'L1_estudo.md', 'L1_itens.md', 'L1_gabarito.md', 'L4_itens.md', 'L4_gabarito.md', 'L5_itens.md', 'L5_gabarito.md'])
retirados = sorted(set(E17g) - set(E18)); novos_ed = sorted(set(E18) - set(E17g))
alterados = sorted(f for f in E18 if f in E17g and E17g[f] != E18[f]); iguais_ed = sorted(f for f in E18 if f in E17g and E17g[f] == E18[f])
chk('(3) EDIÇÃO v1.7->v1.8', '9 arquivos retirados (L1C_, L4C_ e L5C_ × estudo/itens/gabarito), nenhum arquivo novo, 34 arquivos na v1.8 (43 na v1.7)', retirados == REMOV and not novos_ed and len(E18) == 34 and len(E17g) == 43, str(retirados))
chk('(3) EDIÇÃO v1.7->v1.8', '8 alterados: README.md, L1_estudo.md, L1_itens.md, L1_gabarito.md, L4_itens.md, L4_gabarito.md, L5_itens.md e L5_gabarito.md', alterados == ALT, str(alterados))
chk('(3) EDIÇÃO v1.7->v1.8', '26 idênticos byte a byte: L2_*, L3_*, L6A_*, L6B_* (12), L4_estudo.md, L5_estudo.md, BANCO_* (2), DISCURSIVAS* (2) e os 8 de simulado', len(iguais_ed) == 26 and all(f.startswith(('L2_', 'L3_', 'L6A_', 'L6B_', 'BANCO_', 'DISCURSIVAS', 'SIM-')) or f in ('L4_estudo.md', 'L5_estudo.md') for f in iguais_ed), '%d idênticos' % len(iguais_ed))

def entradas_itens(tx):
    """[(id, comando, texto-base, linha do item, aviso)] de um *_itens.md, por leitura própria."""
    L = tx.split('\n'); out = []; cmd = None; tb = ''; tbp = None
    for k, l in enumerate(L):
        if l.startswith('**Comando.** '): cmd = l; tb = tbp or ''; tbp = None
        elif l.startswith('**Texto-base.** '): tbp = l
        else:
            m = re.match(r'^\*\*([^\s*]+)\*\* — ', l)
            if m: out.append((m.group(1), cmd, tb, l, k + 2 < len(L) and L[k + 2] == '> ' + gen.AVISO))
    return out
def blocos_gab(tx):
    L = tx.split('\n'); idx = [k for k, l in enumerate(L) if re.match(r'^### \S+ — Gabarito: [CE]$', l)]
    out = collections.OrderedDict()
    for a, b in zip(idx, idx[1:] + [len(L)]):
        bl = L[a:b]
        while bl and bl[-1] == '': bl.pop()
        out[L[a].split()[1]] = bl
    return out, L[:idx[0]]
def fence_de(L, cab):
    i = L.index(cab) + 2
    f = re.match(r'^(`{3,})text$', L[i]).group(1)
    j = i + 1; buf = []
    while L[j] != f: buf.append(L[j]); j += 1
    return '\n'.join(buf)
def linhas_sec(L, cab, nxt=None):
    """linhas de uma seção: de '## cab' + 2 até a linha em branco antes de '## nxt' (ou o fim do arquivo, sem as linhas em branco finais)."""
    i = L.index(cab) + 2
    j = (L.index(nxt) - 1) if nxt else len(L)
    out = L[i:j]
    while out and out[-1] == '': out.pop()
    return out
rec = collections.OrderedDict()
for X, Cc in gen.COMPL.items():
    a, b, c = entradas_itens(E17g[X + '_itens.md']), entradas_itens(E17g[Cc + '_itens.md']), entradas_itens(E18[X + '_itens.md'])
    rec['itens ' + X] = c == a + b and len(b) == 10 and len(c) == 30
    ga, ha = blocos_gab(E17g[X + '_gabarito.md']); gb, hb = blocos_gab(E17g[Cc + '_gabarito.md']); gc, hc = blocos_gab(E18[X + '_gabarito.md'])
    rec['gabarito ' + X] = list(gc) == list(ga) + list(gb) and all(gc[k] == ga[k] for k in ga) and all(gc[k] == gb[k] for k in gb) and hc == ha and len(gc) == 30
pa, pb, pc = linhas_sec(E17g['L1_estudo.md'].split('\n'), '## Pegadinhas'), linhas_sec(E17g['L1C_estudo.md'].split('\n'), '## Pegadinhas'), linhas_sec(E18['L1_estudo.md'].split('\n'), '## Pegadinhas')
rec['pegadinhas L1'] = len(pb) == 4 and pc == pa + pb and len(pa) == 19
ca, cb, cc = fence_de(E17g['L1_estudo.md'].split('\n'), '## Curso'), fence_de(E17g['L1C_estudo.md'].split('\n'), '## Curso'), fence_de(E18['L1_estudo.md'].split('\n'), '## Curso')
rec['curso L1 = curso v1.7 do L1 + separador + curso v1.7 do 1-C'] = cc == ca + gen.SEP_COMPL + cb and cc.endswith('## Complemento\n\n' + cb) and 0 < len(cb) <= 2374
ops1 = [o for o in difflib.SequenceMatcher(None, E17g['L1_estudo.md'].split('\n'), E18['L1_estudo.md'].split('\n'), autojunk=False).get_opcodes() if o[0] != 'equal']
rec['L1_estudo.md v1.8 = v1.7 com 2 inserções (o complemento no fim do curso e as 4 pegadinhas)'] = len(ops1) == 2 and all(o[0] == 'insert' for o in ops1) and E18['L1_estudo.md'].split('\n')[ops1[1][3]:ops1[1][4]] == pb
rec['L4_estudo.md e L5_estudo.md idênticos (curso, resumo, pares e pegadinhas de L4C e L5C vazios)'] = E18['L4_estudo.md'] == E17g['L4_estudo.md'] and E18['L5_estudo.md'] == E17g['L5_estudo.md'] and all(fence_de(E17g[c + '_estudo.md'].split('\n'), h) == '' for c in ('L4C', 'L5C') for h in ('## Resumo', '## Curso')) and all(len(linhas_sec(E17g[c + '_estudo.md'].split('\n'), '## Pegadinhas')) == 1 and '_Nenhuma pegadinha' in E17g[c + '_estudo.md'] for c in ('L4C', 'L5C'))
for k, v in rec.items():
    chk('(3) EDIÇÃO v1.7->v1.8', 'reconstrução: ' + k, v)
r17, r18 = E17g['README.md'].split('\n'), E18['README.md'].split('\n')
r17_novo = [l.replace('- Versão: v1.7 (pacote.json versão 1)', '- Versão: v1.8 (pacote.json versão 1)').replace('- Data: 2026-10-14', '- Data: 2026-10-17') for l in r17 if not l.startswith(('- L1C: ', '- L4C: ', '- L5C: '))]
chk('(3) EDIÇÃO v1.7->v1.8', 'README.md: "- Versão: v1.8 (pacote.json versão 1)" e "- Data: 2026-10-17"; a lista "Por lote" com 7 linhas (L1, L2, L3, L4, L5, L6A, L6B); o resto igual (o README v1.8 = o da v1.7 com as 2 trocas e sem as 3 linhas dos complementos)',
    r18 == r17_novo and r18[2] == '- Versão: v1.8 (pacote.json versão 1)' and r18[3] == '- Data: 2026-10-17' and sum(1 for l in r18 if re.match(r'^- L\d[A-Z]*: ', l)) == 7 and sum(1 for l in r17 if re.match(r'^- L\d[A-Z]*: ', l)) == 10)
chk('(3) EDIÇÃO v1.7->v1.8', 'manifesto ordenado da edição (SHA-256 das linhas "<sha256>  <nome>"): v1.7 67d2bdf85925a232… -> v1.8 %s… (34 arquivos)' % manifesto(E18)[:16], manifesto(E17g)[:16] == '67d2bdf85925a232' and manifesto(E18) != manifesto(E17g) and len(E18) == 34, manifesto(E18))
fid = json.load(open(os.path.join(OUT, 'estudante_fidelidade.json'), encoding='utf-8'))
conta = json.load(open(os.path.join(OUT, 'estudante_contagem.json'), encoding='utf-8'))
chk('(3) EDIÇÃO v1.7->v1.8', 'fidelidade (estudante_fidelidade.py): 0 diferenças contra o pacote com as regras de deleção e as exceções fechadas (CAIXA, nota de BQ-0003, realinhamento do quadro do L1), com a fusão', fid['diferencas'] == 0 and fid['total'] > 0, 'comparações %d, diferenças %d, marcas residuais %d' % (fid['total'], fid['diferencas'], len(fid['restos'])))
chk('(3) EDIÇÃO v1.7->v1.8', 'realinhamento do quadro do L1: exceção fechada, 2 linhas, 1 ocorrência cada (REALINHA_HITS), só espaços; CAIXA: 8 pares', len(em.REALINHA) == 2 and all(len(d) - len(a_) == 6 for _, a_, d in em.REALINHA) and len(em.CAIXA) == 8)

# ======================================================================= (4) a (7): pacote_estudante.json (v1.8-E)
TOPO = ['versao', 'geradoEm', 'nome', 'edital', 'itens', 'simulados', 'lotes', 'discursivas']
SEP = gen.SEP_COMPL
AV_ANTES, AV_DEPOIS = '(D-ADERENCIA: parcial só em diagnóstico)', '(parcial só em diagnóstico)'
ORDEM7 = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6A', 'L6B']
def lote_json(P, lid): return next(l for l in P['lotes'] if l['id'] == lid)

def sub4(J, P=P18):
    """(4) identidade pacote.json × pacote_estudante.json: {descrição: ok}."""
    r = collections.OrderedDict()
    it, jt = P['itens'], J['itens']
    r['chaves de topo na ordem, versao 1, geradoEm 2026-10-17, nome próprio'] = list(J.keys()) == TOPO and J['versao'] == 1 and J['geradoEm'] == '2026-10-17' and J['nome'] == 'Câmara 2026 — pacote do estudante (v1.8-E)'
    r['ids, ordem e gabaritos (286/286)'] = len(jt) == len(it) == 286 and [(i['id'], i['gabarito']) for i in jt] == [(i['id'], i['gabarito']) for i in it]
    r['enunciado, comando, comandoOriginal e textoBase idênticos (286/286)'] = all(all(i.get(k) == j.get(k) and (k in i) == (k in j) for k in ('enunciado', 'comando', 'comandoOriginal', 'textoBase')) for i, j in zip(it, jt))
    r['itemEdital, aderencia, volatil, rotulo, certame, cargo, ano e numero idênticos'] = all(all(i.get(k) == j.get(k) and (k in i) == (k in j) for k in ('itemEdital', 'aderencia', 'volatil', 'rotulo', 'certame', 'cargo', 'ano', 'numero')) for i, j in zip(it, jt))
    r['url idêntica nos 106 de banco e "" nos 180 AUTORAL'] = sum(1 for i in it if i['rotulo'] != 'AUTORAL') == 106 and all((j['url'] == i['url']) if i['rotulo'] != 'AUTORAL' else (j['url'] == '' and i['url'] != '') for i, j in zip(it, jt)) and sum(1 for j in jt if j['rotulo'] == 'AUTORAL') == 180
    r['nota: só BQ-0003 muda, pela deleção única de " (D-LEI-15352)"'] = all(((j.get('nota') == i['nota'].replace(' (D-LEI-15352)', '') and i['nota'].count(' (D-LEI-15352)') == 1) if i['id'] == 'BQ-0003' else (j.get('nota') == i.get('nota') and ('nota' in i) == ('nota' in j))) for i, j in zip(it, jt))
    r['justificativa de banco vazia nos 106; as AUTORAL ficam para a (5)'] = all(j['justificativa'] == '' for i, j in zip(it, jt) if i['rotulo'] != 'AUTORAL')
    sims = copy.deepcopy(P['simulados'])
    try:
        assert sims[0]['id'] == 'SIM-0' and sims[0]['avisos'][0].count(AV_ANTES) == 1
        sims[0]['avisos'][0] = sims[0]['avisos'][0].replace(AV_ANTES, AV_DEPOIS)
        r['simulados idênticos, salvo avisos[0] do SIM-0 (deleção única de "D-ADERENCIA: "); os outros avisos ficam'] = json.dumps(sims, ensure_ascii=False) == json.dumps(J['simulados'], ensure_ascii=False) and [s['id'] for s in J['simulados']] == ['SIM-0', 'SIM-1', 'SIM-2', 'SIM-0-P2']
    except AssertionError:
        r['simulados idênticos, salvo avisos[0] do SIM-0 (deleção única de "D-ADERENCIA: "); os outros avisos ficam'] = False
    r['edital idêntico'] = J['edital'] == P['edital']
    r['discursivas: id, tipo, aspectos[].n, aspectos[].valor e quesitos[].id idênticos'] = len(J['discursivas']) == len(P['discursivas']) and all(
        a['id'] == b['id'] and a['tipo'] == b['tipo'] and [(x['n'], x['valor']) for x in a['aspectos']] == [(x['n'], x['valor']) for x in b['aspectos']] and [q['id'] for q in a['quesitos']] == [q['id'] for q in b['quesitos']] and list(a.keys()) == list(b.keys())
        for a, b in zip(P['discursivas'], J['discursivas']))
    # lotes: id, nome, prova, itensEdital, legendaMecanismo, pares[].id, pegadinhas[].itemEdital
    ok = [l['id'] for l in J['lotes']] == ORDEM7
    for l in J['lotes'] if ok else []:
        o = lote_json(P, l['id']); c = lote_json(P, gen.COMPL[l['id']]) if l['id'] in gen.COMPL else None
        ok &= all(l.get(k) == o.get(k) and (k in l) == (k in o) for k in ('id', 'nome', 'prova', 'itensEdital', 'legendaMecanismo')) and list(l.keys()) == list(o.keys())
        ok &= [p.get('id') for p in l['pares']] == [p.get('id') for p in o['pares']]
        ok &= [g['itemEdital'] for g in l['pegadinhas']] == [g['itemEdital'] for g in o['pegadinhas']] + ([g['itemEdital'] for g in c['pegadinhas']] if c else [])
    r['lotes: 7, na ordem L1…L6B; id, nome, prova, itensEdital, legendaMecanismo, pares[].id e pegadinhas[].itemEdital idênticos (L1 com as 4 do 1-C no fim)'] = ok
    # lotes: itens de edital dos complementos ⊂ os do principal; L4C e L5C vazios
    r['fusão: itensEdital de L1C ⊂ L1, L4C ⊂ L4, L5C ⊂ L5; curso/resumo/pares/pegadinhas de L4C e L5C vazios; L1C sem resumo nem pares'] = all(set(lote_json(P, c)['itensEdital']) <= set(lote_json(P, m)['itensEdital']) for m, c in gen.COMPL.items()) and all(not lote_json(P, c)[k] for c in ('L4C', 'L5C') for k in ('curso', 'resumo', 'pares', 'pegadinhas')) and not lote_json(P, 'L1C')['resumo'] and not lote_json(P, 'L1C')['pares']
    return r

def parse_ed(E, fundida):
    """leitura própria de uma edição (v1.7 com 43 ou v1.8 com 34 arquivos): {'lotes': {lid: {resumo, curso, pares, pegs}}, 'just': {id: texto}, 'disc': {...}, 'simj': {sim: {id: texto}}}."""
    out = {'lotes': {}, 'just': {}, 'simj': {}, 'disc': {}}
    for f in sorted(E):
        m = re.match(r'^(L\w+?)_estudo\.md$', f)
        if m:
            L = E[f].split('\n')
            pares = linhas_sec(L, '## Pares', '## Pegadinhas'); pegs = linhas_sec(L, '## Pegadinhas')
            out['lotes'][m.group(1)] = dict(resumo=fence_de(L, '## Resumo'), curso=fence_de(L, '## Curso'), pares=[] if pares == ['_Nenhum par neste lote._'] else pares,
                                            pegs=[] if pegs == ['_Nenhuma pegadinha registrada neste lote._'] else pegs)
        m = re.match(r'^(L\w+?)_gabarito\.md$', f)
        if m:
            g, _ = blocos_gab(E[f])
            for k, bl in g.items():
                j = [l for l in bl if l.startswith('- Justificativa: ')]
                out['just'][k] = j[0][len('- Justificativa: '):] if j else None
        m = re.match(r'^(SIM-[\w-]+?)_gabarito\.md$', f)
        if m:
            L = E[f].split('\n'); cur = None; d = {}
            for l in L:
                mm = re.match(r'^### \d+ — (\S+) — Gabarito: [CE]$', l)
                if mm: cur = mm.group(1); continue
                if cur and l.startswith('- Justificativa: '): d[cur] = l[len('- Justificativa: '):]
            out['simj'][m.group(1)] = d
    Ld = E['DISCURSIVAS.md'].split('\n'); Lp = E['DISCURSIVAS_padrao.md'].split('\n')
    tipos = {'questao': 'Questão', 'peca': 'Peça técnica'}
    for d in P18['discursivas']:
        h = '## %s — %s' % (d['id'], tipos[d['tipo']])
        e = dict(comando=fence_de(Ld, h))
        i = Lp.index(h) + 4
        f = re.match(r'^(`{3,})text$', Lp[i]).group(1); j = i + 1; buf = []
        while Lp[j] != f: buf.append(Lp[j]); j += 1
        e['padrao'] = '\n'.join(buf)
        i = Lp.index('### Aspectos (valor)', j) + 2; asp = []
        while Lp[i].startswith('- ('):
            mm = re.match(r'^- \((\d+)\) (.*) — valor: ([\d,]+)$', Lp[i]); asp.append((int(mm.group(1)), mm.group(2))); i += 1
        e['aspectos'] = asp
        i = Lp.index('### Quesitos', i) + 2; qs = []
        while i < len(Lp) and Lp[i].startswith('- **'):
            mm = re.match(r'^- \*\*(\S+)\*\* — (.*)$', Lp[i]); q = [mm.group(1), mm.group(2), []]; i += 1
            while i < len(Lp) and Lp[i].startswith('  - '): q[2].append(Lp[i][4:]); i += 1
            qs.append(q)
        e['quesitos'] = qs
        out['disc'][d['id']] = e
    return out
ED17, ED18 = parse_ed(E17g, False), parse_ed(E18, True)

def linha_par(p):
    if 'id' in p:
        l = '- %s. **%s**' % (p['id'], p['a']) + (' × **%s**' % p['b'] if p['b'] else '') + ' | ' + p['como']
    else:
        l = '- **%s**' % p['a'] + (' vs **%s**' % p['b'] if p['b'] else '') + (': ' + p['como'] if p['como'] else '.')
    return l
def linha_peg(g): return '- [%s] **%s** — %s' % (g['itemEdital'], g['rotulo'], g['texto'])

def coerencia(J, ED, fundida):
    """JSON × edição (v1.7: 43 arquivos, complementos em arquivos próprios; v1.8: 34, fundida): {descrição: ok}."""
    r = collections.OrderedDict()
    okrc = okp = okg = True
    for l in J['lotes']:
        lid = l['id']; m = ED['lotes'][lid]; c = None if fundida or lid not in gen.COMPL else ED['lotes'][gen.COMPL[lid]]
        if c is not None:
            okrc &= not c['resumo'] and not c['pares']
        curso_ed = m['curso'] + (SEP + c['curso'] if c is not None and c['curso'] else '')
        okrc &= l['resumo'] == m['resumo'] and l['curso'] == curso_ed
        okp &= [linha_par(p) for p in l['pares']] == m['pares']
        okg &= [linha_peg(g) for g in l['pegadinhas']] == m['pegs'] + (c['pegs'] if c is not None else [])
    r['resumo e curso dos 7 lotes (L1 fundido: curso do L1 + "## Complemento" + curso do 1-C)'] = okrc and len(J['lotes']) == 7
    r['linhas de pares recompostas do JSON pelo formato da edição'] = okp
    r['linhas de pegadinhas recompostas do JSON (L1: as 4 do 1-C no fim)'] = okg
    oj = True; n = 0
    for i in J['itens']:
        if i['rotulo'] != 'AUTORAL': continue
        n += 1
        oj &= ED['just'].get(i['id']) == (i['justificativa'] or None)
    r['justificativa de cada item AUTORAL = a linha "- Justificativa: …" do *_gabarito.md de lote (%d/180)' % n] = oj and n == 180
    od = len(J['discursivas']) == 5
    for d in J['discursivas']:
        e = ED['disc'][d['id']]
        od &= d['comando'] == e['comando'] and d['padrao'] == e['padrao'] and [(a['n'], a['texto']) for a in d['aspectos']] == e['aspectos'] and [[q['id'], q['nome'], q['conceitos']] for q in d['quesitos']] == e['quesitos']
    r['discursivas: comando, padrão, aspectos e quesitos (nome e conceitos) = DISCURSIVAS.md e DISCURSIVAS_padrao.md'] = od
    return r

def sub7(J):
    """(7) varredura R no JSON: casamentos = X1–X8 e Y1; 0 de processo."""
    c = mp.classifica(list(mp.walk(J)), mp.X, mp.Y)
    return collections.OrderedDict([('varredura R no pacote_estudante.json: 9 casamentos (X1–X8, Y1), 0 de processo, contagens das listas X e Y conferidas', not c['processo'] and not c['falhas'] and len(c['todos']) == 9)]), c

for k, v in sub4(JE).items():
    chk('(4) IDENT json', k, v)
chk('(4) IDENT json', 'serialização: json.dumps(indent=1, ensure_ascii=False) + "\\n", UTF-8, LF, sem BOM', json.dumps(JE, ensure_ascii=False, indent=1) + '\n' == rawE.decode('utf-8') and b'\r' not in rawE and not rawE.startswith(b'\xef\xbb\xbf'), 'SHA-256 %s, %d bytes' % (sha(rawE), len(rawE)))
for k, v in coerencia(JE, ED17, False).items():
    chk('(5) JSON×ED v1.7', k, v)
# divergências entre o escopo de lote e o de simulado de uma mesma justificativa (só registro)
div = sorted((s, i) for s, d in ED17['simj'].items() for i, t in d.items() if ED17['just'].get(i) is not None and ED17['just'][i] != t)
chk('(5) JSON×ED v1.7', 'INFO (só registro; o JSON segue o escopo de lote): justificativas de AUTORAL com texto diferente entre o *_gabarito.md de lote e o de simulado na edição v1.7: %d' % len(div), True, '; '.join('%s/%s' % x for x in div[:40]))
L1j = lote_json(JE, 'L1')
chk('(5) JSON×ED v1.7', 'no L1, o curso fundido = curso de L1_estudo.md v1.7 + separador + curso de L1C_estudo.md v1.7', L1j['curso'] == ED17['lotes']['L1']['curso'] + SEP + ED17['lotes']['L1C']['curso'])
for k, v in coerencia(JE, ED18, True).items():
    chk('(6) JSON×ED v1.8', k, v)
sj7, cl7 = sub7(JE)
for k, v in sj7.items():
    chk('(7) VARREDURA R json', k, v, 'processo %d; falhas %s; contagens %s' % (len(cl7['processo']), cl7['falhas'], dict(cl7['contagem'])))
# varredura R na edição v1.8
cl_ed = mp.classifica(sorted(E18.items()), mp.X_ED, mp.Y_ED)
chk('(7) VARREDURA R edição', 'edição v1.8 (34 arquivos): os 11 casamentos da seção 2.4 (X1 2: BANCO_itens.md e SIM-0_folha.md; X2 2: idem; X3 L2_estudo; X4, X5, X6 e X7 L3_estudo [4: X4 1 e, juntos, X5+X6+X7 3, pelos contextos sobrepostos]; X8 L6A_estudo; Y1 L4_gabarito) e 0 de processo',
    len(cl_ed['todos']) == 11 and not cl_ed['processo'] and not cl_ed['falhas'] and sorted(set(d for *_, d in cl_ed['todos'])) == sorted(['X1', 'X2', 'X3', 'X4', 'X5+X6+X7', 'X8', 'Y1']),
    '; '.join('%s %s' % (d, c_) for c_, lab, g, ctx, d in cl_ed['todos']) + ('; PROCESSO: %s' % [(p[0], p[2]) for p in cl_ed['processo']] if cl_ed['processo'] else ''))
_L3 = E18['L3_estudo.md'].split('\n')
_i_cur, _i_par, _i_peg = _L3.index('## Curso'), _L3.index('## Pares'), _L3.index('## Pegadinhas')
_pos = [k for k, l in enumerate(_L3) if 'Presidência' in l]
_ctx = 'órgão da Presidência (redação superada)'
_loc = [k for k, l in enumerate(_L3) if _ctx in l]
chk('(7) VARREDURA R edição', 'localização de X5+X6+X7 em L3_estudo.md (Adendo 1, 9.5 (a)): o contexto de X6 ocorre 3 vezes: 1 no bloco do curso (X5), 1 na seção "## Pares" (X6) e 1 na seção "## Pegadinhas" (X7); X4 1 no curso; as 4 linhas com "Presidência" no arquivo',
    len(_loc) == 3 and sum(1 for k in _loc if _i_cur < k < _i_par) == 1 and sum(1 for k in _loc if _i_par < k < _i_peg) == 1 and sum(1 for k in _loc if k > _i_peg) == 1
    and sum(1 for k in _pos if _i_cur < k < _i_par) == 2 and sum(1 for k in _pos if _i_par < k < _i_peg) == 1 and sum(1 for k in _pos if k > _i_peg) == 1,
    'linhas %s (curso %d, pares %d, pegadinhas %d)' % ([k + 1 for k in _loc], _i_cur + 1, _i_par + 1, _i_peg + 1))
chk('(7) VARREDURA R edição', 'MARK_RX do W.raw (estudante_gen.py) sem disparo em comando, textoBase e enunciado dos 286 itens (campos de prova que a edição exibe sem deleção)',
    not any(gen.MARK_RX.search(i[k] or '') for i in P18['itens'] for k in ('comando', 'textoBase', 'enunciado')))
cont18 = collections.Counter(gen.lote_fund(i['id']) for i in JE['itens'] if i['rotulo'] == 'AUTORAL')
cont17 = collections.Counter(gen.lote_of(i['id']) for i in P17g['itens'] if i['rotulo'] == 'AUTORAL')
chk('(7) CONTAGEM', 'itens por lote, v1.7 -> v1.8-E (D1, 3.4): L1 20+10 -> 30; L4 20+10 -> 30; L5 20+10 -> 30; L2, L3, L6A, L6B 30, 30, 15, 15; AUTORAL 180, banco 106',
    dict(cont17) == {'L1': 20, 'L1C': 10, 'L2': 30, 'L3': 30, 'L4': 20, 'L4C': 10, 'L5': 20, 'L5C': 10, 'L6A': 15, 'L6B': 15} and dict(cont18) == {'L1': 30, 'L2': 30, 'L3': 30, 'L4': 30, 'L5': 30, 'L6A': 15, 'L6B': 15} and sum(cont18.values()) == 180,
    'v1.7 %s; v1.8-E %s' % (dict(sorted(cont17.items())), dict(sorted(cont18.items()))))

# ======================================================================= (4) varreduras de não regressão (seção 3.5 do QA R2), exceções fechadas da R1 e conferências do QA da T-56
def cre(rx, prefixos=None, F=E18, flags=re.M):
    r = re.compile(rx, flags)
    return sum(len(r.findall(tx)) for f, tx in F.items() if prefixos is None or f.startswith(tuple(prefixos)))
folhas = [f for f in E18 if f.endswith('_folha.md')]
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
sem_b14 = cre(r'D-[A-Z]{2,}'); sem_b12 = cre(r'D-[A-Z]{2,}', None, E12); sem_b17 = cre(r'D-[A-Z]{2,}', None, {f: t for f, t in E17g.items() if f in E18}); sem_b17_todos = cre(r'D-[A-Z]{2,}', None, E17g)
chk('(4) VARR 3.5 extra', 'D-[A-Z]{2,} (sem \\b): mesma contagem da v1.7 nos arquivos que permanecem (os 9 arquivos retirados repetiam a legenda, que traz as demais ocorrências; só "TID-IA", "TID-DADOS-VIZ", "END-TO-END" e afins; a v1.7 tinha a mesma contagem da v1.2 nos 43); com \\b: 0 (errata de registro da T-56, seção 3)', sem_b14 == sem_b17 and sem_b17_todos == sem_b12 and cre(r'\bD-[A-Z]{2,}', None, E12) == 0 and cre(r'\bD-[A-Z]{2,}') == 0, 'v1.2 (43 arquivos) %d; v1.7 (43) %d; v1.7 nos 34 que permanecem %d; v1.8 %d' % (sem_b12, sem_b17_todos, sem_b17, sem_b14))
codF = sorted((f, k) for f, tx in E18.items() for k, l in enumerate(tx.split('\n'), 1) if re.search(r'\bF\d{1,2}\b', l))
chk('(4) VARR 3.5', 'códigos F: só L6A_estudo.md:83 ("a tecla F4") e L4_gabarito.md:58 (L4-11, "O F4 afirma")', len(codF) == 2 and codF[0][0] == 'L4_gabarito.md' and codF[1] == ('L6A_estudo.md', 83) and 'O F4 afirma' in E18['L4_gabarito.md'].split('\n')[codF[0][1] - 1] and 'tecla F4' in E18['L6A_estudo.md'].split('\n')[82], str(codF))
AV = 'Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.'
volx = sorted((f, k) for f, tx in E18.items() for k, l in enumerate(tx.split('\n'), 1) if 'VOLÁTIL' in l and AV not in l)
volx13 = sorted((f, k) for f, tx in E17g.items() for k, l in enumerate(tx.split('\n'), 1) if 'VOLÁTIL' in l and AV not in l)
chk('(4) VARR 3.5', '"VOLÁTIL" fora do aviso fixo: só L4_estudo 23 e 210; L5_estudo 24, 104 e 107; L6A_estudo 125 e 268 (igual à v1.7); os gabaritos com legenda não ganham a palavra', volx == sorted([('L4_estudo.md', 23), ('L4_estudo.md', 210), ('L5_estudo.md', 24), ('L5_estudo.md', 104), ('L5_estudo.md', 107), ('L6A_estudo.md', 125), ('L6A_estudo.md', 268)]) and volx == volx13, str(volx))
json.dump({'volatil_fora_do_aviso': volx}, open(os.path.join(OUT, 'varredura_volatil_v18.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
# conferências do QA da T-56 que continuam valendo: N-1, legendas dos lotes, avisos não exibidos
n1 = sum(tx.count('Nesta produção') + tx.count('nesta produção') for tx in E18.values()); n2 = sum(tx.lower().count('especificação previa') for tx in E18.values()); n3 = sum(tx.count('se houver base') for tx in E18.values())
chk('(4) QA T-56', 'N-1: 0 "Nesta produção", 0 "especificação previa" e 0 "se houver base" nos 34 arquivos; no pacote a marca fica (1 e 1; D-PACOTE-V11)', n1 == n2 == n3 == 0 and sum(l['curso'].count('Nesta produção') for l in P18['lotes']) == 1 and sum(l['curso'].count('especificação previa') for l in P18['lotes']) == 1, '%d/%d/%d' % (n1, n2, n3))
chk('(4) QA T-56', 'L6B_estudo.md igual ao da v1.7 (N-1 intacta: a linha 143 é igual)', E17g['L6B_estudo.md'] == E18['L6B_estudo.md'] and E17g['L6B_estudo.md'].split('\n')[142] == E18['L6B_estudo.md'].split('\n')[142])
okl = True; detl = []
for l in gen.lotes_fund(P18):
    f = '%s_gabarito.md' % l['id']
    if 'legendaMecanismo' not in l: okl &= E18[f].split('\n')[2].startswith('### '); continue
    b = E18[f].split('\n')
    ok = b[0] == '# %s — gabarito e justificativas' % l['nome'] and b[1] == '' and b[2] == l['legendaMecanismo'] and b[3] == '' and b[4].startswith('### ') and b[0:4] == E17g[f].split('\n')[0:4]
    okl &= ok; detl.append('%s %s' % (l['id'], 'ok' if ok else 'FALHA'))
chk('(4) QA T-56', 'legenda: nos 4 L<lote>_gabarito.md com legenda (L4, L5, L6A, L6B) é literal, sozinha, no topo (linha 3), antes do primeiro item (as 4 linhas de topo iguais às da v1.7); L1, L2, L3 sem legenda (a do 1-C, 4-C e 5-C não entra: D1, 3.1); L2, L3, L6A e L6B _gabarito.md iguais aos da v1.7', okl and all(E17g[f] == E18[f] for f in E18 if re.match(r'^L(2|3|6A|6B)_gabarito\.md$', f)), ', '.join(detl))
legs = sorted({l['legendaMecanismo'] for l in P18['lotes'] if 'legendaMecanismo' in l})
dentro = [f for f, tx in E18.items() if any(g in tx for g in legs) and not re.match(r'^(L(4|5|6A|6B)_gabarito|SIM-1_gabarito)\.md$', f)]
chk('(4) QA T-56', 'legenda exibida só nos L<lote>_gabarito.md dos 6 lotes e no SIM-1_gabarito.md (D-T54-07): 0 ocorrência em BANCO_gabarito.md, *_estudo.md, *_itens.md, *_folha.md, README.md, SIM-0, SIM-2 e SIM-0-P2', not dentro, str(dentro))
avs = [a for s in P18['simulados'] for a in s.get('avisos', [])]
exib = [f for f, tx in E18.items() if any(fr in tx for av in avs for fr in (av[:40], av.split('\n')[0][-40:]))]
chk('(4) QA T-56', 'avisos do SIM-0 continuam no pacote (3 strings) e NÃO são exibidos na edição (0 arquivo com o texto dos 3 avisos; 0 "Avisos de montagem", 0 "D-ADERENCIA")', len(avs) == 3 and avs == P17g['simulados'][0]['avisos'] and not exib and sum(tx.count('Avisos de montagem') + tx.count('D-ADERENCIA') for tx in E18.values()) == 0, str(exib))
chk('(4) QA T-56', 'README, folhas e demais arquivos sem mudança indevida: SIM-0_folha e SIM-0_gabarito mudam só pela nota (a v1.3 sem a nota = a v1.4 sem a nota)', all(re.sub(r'(?m)^([>-]) (?:Nota: )?nota de vigência:.*\n?', '', E17g[f]) == re.sub(r'(?m)^([>-]) (?:Nota: )?nota de vigência:.*\n?', '', E18[f]) for f in ('SIM-0_folha.md', 'SIM-0_gabarito.md', 'BANCO_itens.md', 'BANCO_gabarito.md')))

# exceções fechadas da R1
def strings(o):
    if isinstance(o, str): yield o
    elif isinstance(o, dict):
        for v in o.values(): yield from strings(v)
    elif isinstance(o, list):
        for v in o: yield from strings(v)
S14 = list(strings(P18))
def ce(t, pref=None): return sum(tx.count(t) for f, tx in E18.items() if pref is None or f.startswith(tuple(pref)))
it = {i['id']: i for i in P18['itens']}
c05 = [('4C-08', '(conceito geral, sem fonte de fornecedor, como no curso). O item não depende', '(conceito geral, sem fonte de fornecedor, como no curso). o item não depende'),
       ('5C-06', 'termine no mínimo da amostra. A regra de 1,5 · AIQ', 'termine no mínimo da amostra. a regra de 1,5 · AIQ')]
for iid, novo, antigo in c05:
    j = it[iid]['justificativa']
    ocorr = 1 + sum(1 for s in P18['simulados'] if iid in s['itens'])
    chk('(4) CAIXA C-05', '%s: pacote com inicial maiúscula (1 vez), sem a minúscula; edição: %d ocorrências (gabarito do lote + simulados), 0 da minúscula' % (iid, ocorr), j.count(novo) == 1 and j.count(antigo) == 0 and ce(novo) == ocorr and ce(antigo) == 0, 'edição %d' % ce(novo))
for esc, antes, depois in em.CAIXA:
    chk('(4) CAIXA C-15', 'L6A_estudo: "%s" -> "%s": antes 0, depois 1' % (antes[:34], depois[:34]), ce(antes, (esc,)) == 0 and ce(depois, (esc,)) == 1 and len(antes) == len(depois) and sum(x != y for x, y in zip(antes, depois)) == 1)
chk('(4) CAIXA C-15', 'lista CAIXA: 8 pares, todos em L6A_estudo; 8 trocas na regeração; L6A_estudo.md idêntico ao da v1.3 fora dos 19 pares', len(em.CAIXA) == 8 and all(c[0] == 'L6A_estudo' for c in em.CAIXA) and conta['total'].get('caixa (minúscula → maiúscula na inicial deixada por deleção)') == 8)
def peg(P, lid, rot): return [g['texto'] for l in P['lotes'] if l['id'] == lid for g in l['pegadinhas'] if g['rotulo'] == rot]
e15 = peg(P18, 'L1', 'Pontuação automática e capitalização em transcrições')
b1 = peg(P18, 'L5', 'Gráfico de barras (colunas)'); b2 = peg(P18, 'L5', 'Box plot (diagrama de caixa)')
chk('(4) REUNIÃO C-06', 'L1 P2-1.5: 1 entrada, com os dois fragmentos unidos por "; "', len(e15) == 1 and '"Câmara" (instituição) vs "câmara" (sala)' in e15[0] and e15 == peg(P12, 'L1', 'Pontuação automática e capitalização em transcrições'))
chk('(4) REUNIÃO C-07', 'L5 Gráfico de barras (colunas): 3 entradas (confundir com histograma; aceitar eixo truncado; reunida "usar para distribuição…; empilhado quando…")', len(b1) == 3 and 'usar para distribuição de variável contínua agrupada em classes; empilhado quando se quer comparar as partes entre si.' in b1 and 'confundir com histograma' in b1 and 'aceitar eixo truncado' in b1)
chk('(4) REUNIÃO C-08', 'L5 Box plot (diagrama de caixa): 1 entrada com os 4 fragmentos unidos por "; "', len(b2) == 1 and b2[0].startswith('dizer que a linha central é a média; que a caixa vai do mínimo ao máximo') and b2[0].endswith('que mostra frequência por intervalo (isso é histograma).'))
npg = {l['id']: len(l['pegadinhas']) for l in P18['lotes']}
chk('(4) REUNIÃO', 'pegadinhas por lote = v1.3 (L1 19, L1C 4, L2 43, L3 42, L4 32, L4C 0, L5 48, L5C 0, L6A 35, L6B 39; total 262)', npg == {'L1': 19, 'L1C': 4, 'L2': 43, 'L3': 42, 'L4': 32, 'L4C': 0, 'L5': 48, 'L5C': 0, 'L6A': 35, 'L6B': 39} and sum(npg.values()) == 262)
l1e = E18['L1_estudo.md']; l5e = E18['L5_estudo.md']
chk('(4) REUNIÃO', 'edição: L1_estudo com 1 linha para P2-1.5 "Pontuação automática…"; L5_estudo com 3 linhas "Gráfico de barras (colunas)" e 1 "Box plot (diagrama de caixa)"',
    sum(1 for l in l1e.split('\n') if l.startswith('- [P2-1.5] **Pontuação automática e capitalização em transcrições**')) == 1 and sum(1 for l in l5e.split('\n') if l.startswith('- [P1-8.2] **Gráfico de barras (colunas)**')) == 3 and sum(1 for l in l5e.split('\n') if l.startswith('- [P1-8.2] **Box plot (diagrama de caixa)**')) == 1)
j = it['L4-11']['justificativa']; ed = [l for l in E18['L4_gabarito.md'].split('\n') if l.startswith('- Justificativa: ') and 'O F4 afirma que "generative models are initially trained using an unsupervised approach"' in l]
chk('(4) C-13', 'L4-11: justificativa da edição = a do pacote menos exatamente " Fonte: F4, reverificado em 7/10/2026." (1 ocorrência no pacote); frase que fundamenta o gabarito C presente; gabarito C',
    len(ed) == 1 and j.count(' Fonte: F4, reverificado em 7/10/2026.') == 1 and ed[0] == '- Justificativa: ' + j.replace(' Fonte: F4, reverificado em 7/10/2026.', '') and it['L4-11']['gabarito'] == 'C' and 'L4-11' not in [x for s in P18['simulados'] for x in s['itens']])
n3_ = it['BQ-0003']['nota']
chk('(4) C-18', 'BQ-0003: `nota` no pacote com " (D-LEI-15352)" literal; na edição, sem ele e sem o rótulo "Nota:", nos 4 pontos (BANCO_itens, BANCO_gabarito, SIM-0_folha, SIM-0_gabarito); BQ-0040 sem o identificador',
    n3_.count(' (D-LEI-15352)') == 1 and ce(n3_.replace(' (D-LEI-15352)', '')) == 4 and ce('D-LEI-15352') == 0 and all(ce(n3_.replace(' (D-LEI-15352)', ''), (f,)) == 1 for f in ('BANCO_itens', 'BANCO_gabarito', 'SIM-0_folha', 'SIM-0_gabarito')) and '(D-' not in it['BQ-0040']['nota'])
chk('(4) C-10', 'folhas: 165 linhas de item sem id de origem; 0 com id (id só no *_gabarito.md)', cre(r'^\*\*\d+\*\* — ', tuple(folhas)) == 165 and cre(r'^\*\*(?:BQ-|L\d|4C-|5C-|6A-|6B-|A5-)\S*\*\*', tuple(folhas)) == 0)
def tb_antes(tx):
    nb = [l for l in tx.split('\n') if l.strip()]
    return (sum(1 for k in range(len(nb) - 1) if nb[k].startswith('**Texto-base.**') and nb[k + 1].startswith('**Comando.**')), sum(1 for k in range(len(nb) - 1) if nb[k].startswith('**Comando.**') and nb[k + 1].startswith('**Texto-base.**')))
chk('(4) C-11', 'texto-base antes do comando: BANCO_itens 3 e SIM-0_folha 1; 0 comando antes de texto-base', tb_antes(E18['BANCO_itens.md']) == (3, 0) and tb_antes(E18['SIM-0_folha.md']) == (1, 0) and sum(tb_antes(tx)[1] for tx in E18.values()) == 0)

# --- T57 s3 item 6: scripts históricos mantidos (opção "marcar", D-T57-10), sem alteração
import glob
HIST = ['relatorio_R1.py', 'report.py', 'report2.py', 'diff.py', 'diff2.py', 'conferencias_R1.py']
HD = os.path.dirname(os.path.abspath(__file__)); H14 = os.path.join(HD, '..', 'gerador_v1_4')
chk('(4) T57 s3-6', 'os 5 scripts históricos não executáveis (relatorio_R1, report, report2, diff, diff2) e conferencias_R1.py (histórico executável) estão em gerador_v1_7/ e são idênticos, byte a byte, aos de gerador_v1_4/ (opção "marcar", D-T57-10: nenhuma alteração)',
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
c12 = cnt(P12); c13 = cnt(P13); c14 = cnt(P14); c15 = cnt(P15); c16g = cnt(P16g); c18 = cnt(P18)
ESP = collections.OrderedDict([('itens', 286), ('ids únicos', 286), ('C', 149), ('E', 137), ('banco', 106), ('AUTORAL', 180), ('aderência direta', 247), ('aderência parcial', 39), ('volatil', 23), ('nota', 2),
                               ('comandoOriginal', 90), ('pegadinhas', 262), ('simulados n', [60, 40, 40, 25]), ('simulados itens', [60, 40, 40, 25]), ('lotes', 10), ('discursivas', 5), ('edital', 47)])
for k, v in ESP.items():
    chk('(5) CONT', '%s = %s (v1.2: %s; v1.3: %s; v1.4: %s; v1.5: %s; v1.6: %s; v1.8: %s)' % (k, v, c12[k], c13[k], c14[k], c15[k], c16g[k], c18[k]), c18[k] == v == c16g[k] == c15[k] == c14[k] == c13[k] == c12[k])
chk('(5) CONT', 'pares (139), aspectos e quesitos das discursivas iguais aos da v1.3 e da v1.2; pares com `id` 72', c18['pares'] == c14['pares'] == c13['pares'] == c12['pares'] == 139 and c18['aspectos'] == c14['aspectos'] == c13['aspectos'] == c12['aspectos'] and c18['quesitos'] == c14['quesitos'] == c13['quesitos'] == c12['quesitos'] and sum('id' in p for l in P18['lotes'] for p in l['pares']) == 72,
    '%s/%s/%s' % (c18['pares'], c18['aspectos'], c18['quesitos']))
chk('(5) CONT', 'SIM-0 33 C/27 E (diagnóstico, 23 parciais, 4 voláteis, 3 avisos); SIM-1 e SIM-2 20 C/20 E; SIM-0-P2 13 C/12 E', [tuple(collections.Counter(it[x]['gabarito'] for x in s['itens']).get(g, 0) for g in 'CE') for s in P18['simulados']] == [(33, 27), (20, 20), (20, 20), (13, 12)]
    and sum(1 for x in P18['simulados'][0]['itens'] if it[x]['aderencia'] == 'parcial') == 23 and sum(1 for x in P18['simulados'][0]['itens'] if it[x].get('volatil')) == 4)
chk('(5) CONT', 'edição: 34 arquivos (43 na v1.7); itens por simulado iguais aos da v1.3', len(E18) == 34 and c18['simulados itens'] == [60, 40, 40, 25])
# ======================================================================= (6) artefatos da T-59 e da T-66 (D-T59-07, D-T59-04, D-T59-02, seção 6 da decisão; regra v1.2: E-6 a E-10 de T66_decisoes, seção 6.2)
import subprocess
imp_v1 = '\n'.join(bloco_apos('## 2. REGRA DE IMPORTAÇÃO', '```markdown')) + '\n'
imp_atual = rb_lf(os.path.join(REPO_, 'regras', 'importacao_erros.md')).decode('utf-8')
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
ex_raw = rb_lf(os.path.join(REPO_, 'saida', 'pacote', 'exemplo_erros_v1.json')).decode('utf-8')
exo = json.loads(ex_raw)
TAB = ['formato', 'versaoFormato', 'exportadoEm', 'pacote', 'estadoVersao', 'escolha', 'resumo', 'caderno', 'respostasCaderno', 'tentativas', 'saidas', 'discursivas']
chk('(6) T-59', 'saida/pacote/exemplo_erros_v1.json é igual, caractere a caractere, ao exemplo mínimo da decisão (D-T59-04); abre como JSON; tem os 12 campos da tabela D-T59-02', ex_raw == ex_lit and sorted(exo) == sorted(TAB) and exo['formato'] == 'camara2026.erros' and exo['versaoFormato'] == 1)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validar_erros as VE
Rex = VE.valida(ex_raw.encode('utf-8'), P18)
chk('(6) T-59', 'validador (validar_erros.py) sobre o exemplo: ACEITO, 0 incoerência (D-T59-05), ids fictícios listados como desconhecidos (caderno XX-0001; det XX-0001 e XX-0002; discursivas DX)',
    Rex['veredito'] == 'ACEITO' and not Rex['incoerencias'] and {k: sorted(v['ids']) for k, v in Rex['ids_desconhecidos'].items()} == {'caderno': ['XX-0001'], 'tentativas[].det': ['XX-0001', 'XX-0002'], 'discursivas': ['DX']})
EX_TMP = os.path.join(tempfile.mkdtemp(prefix='exemplo_'), 'exemplo_erros_v1.json')
open(EX_TMP, 'wb').write(ex_raw.encode('utf-8'))
VM = os.path.join(REPO_, 'saida', 'treino', 'ferramentas', 'validar_erros.py')
rm = subprocess.run([sys.executable, '-I', '-X', 'utf8', VM, EX_TMP, '--pacote', PAC, '--json'], capture_output=True, text=True, encoding='utf-8')
Rm = json.loads(rm.stdout)
chk('(6) T-59', 'validador mantido (saida/treino/ferramentas/validar_erros.py, `python3 -I`) sobre o exemplo: ACEITO (código 0), 0 incoerência, 0 aviso `ordem:`, fora_dos_calculos com as 3 chaves vazias, mesmos ids desconhecidos que o registro',
    rm.returncode == 0 and Rm['veredito'] == 'ACEITO' and not Rm['incoerencias'] and not [x for x in Rm['avisos'] if x.startswith('ordem:')] and Rm['fora_dos_calculos'] == {'tentativas': [], 'caderno': [], 'discursivas': []} and Rm['ids_desconhecidos'] == Rex['ids_desconhecidos'] and Rm['sha256'] == Rex['sha256'])
HDV = os.path.dirname(os.path.abspath(__file__))
chk('(6) T-59', 'registro (D-R59-08): gerador_v1_8/validar_erros.py (19ab9c8b…) e validar_erros_teste.py (33132d5a…) continuam com o SHA-256 da T-61 (conteúdo LF); a cópia mantida em saida/treino/ferramentas/ existe e difere do registro (a marcação "registro (T-59)" no MANIFESTO é conferida por manifesto_v1_8.py, passo 11)',
    sha(rb_lf(os.path.join(HDV, 'validar_erros.py'))) == '19ab9c8b359e4a59f209ecbca3e29f2ecc16a0dd5fb49b8892538bbe7eb8f33e' and sha(rb_lf(os.path.join(HDV, 'validar_erros_teste.py'))) == '33132d5a9d9aaf7ec4bf645ae57b84eca9c2094abdc70f18d6970465278f0186'
    and os.path.exists(VM) and rb_lf(VM) != rb_lf(os.path.join(HDV, 'validar_erros.py')))
SHA_VM = hashlib.sha256(rb_lf(VM)).hexdigest(); SHA_VMT = hashlib.sha256(rb_lf(os.path.join(REPO_, 'saida', 'treino', 'ferramentas', 'validar_erros_teste.py'))).hexdigest()
tp = subprocess.run([sys.executable, '-I', '-X', 'utf8', os.path.join(REPO_, 'saida', 'treino', 'ferramentas', 'validar_erros_teste.py')], capture_output=True, text=True, encoding='utf-8', cwd='/')
tp_ok = sum(1 for x in tp.stdout.split('\n') if x.startswith('OK    ')); tp_f = sum(1 for x in tp.stdout.split('\n') if x.startswith('FALHA '))
chk('(6) T-66', 'validador mantido (T-66): saida/treino/ferramentas/validar_erros.py SHA-256 220dd559fa5ac23bda706366c613603654d41533713f45a78969371ee69e9985 e validar_erros_teste.py SHA-256 192581d92c242bbf6649ad11c3d5212ec6eb9c15b2d377d6e0f437d79d4595e2 (T66_producao_2026-10-14.md); o teste, rodado de / com `python3 -I`: %d conferências OK, %d FALHA, código %d' % (tp_ok, tp_f, tp.returncode),
    SHA_VM == '220dd559fa5ac23bda706366c613603654d41533713f45a78969371ee69e9985' and SHA_VMT == '192581d92c242bbf6649ad11c3d5212ec6eb9c15b2d377d6e0f437d79d4595e2' and tp.returncode == 0 and tp_f == 0 and tp_ok > 0 and SHA_VM in read('saida/pacote/T66_producao_2026-10-14.md'),
    'SHA-256 %s / %s' % (SHA_VM[:12], SHA_VMT[:12]))
gi = rb_lf(os.path.join(REPO_, '.gitignore')).decode('utf-8')
chk('(6) T-59', '.gitignore da raiz = as 2 linhas da decisão (seção 6, item 1): "# T-59 (D1 da GBQ): dados da candidata — nunca no git" e "/entrada/erros/"', gi == '# T-59 (D1 da GBQ): dados da candidata — nunca no git\n/entrada/erros/\n')
cg = subprocess.run(['git', '-C', REPO_, 'check-ignore', '-v', 'entrada/erros/x.json'], capture_output=True, text=True, encoding='utf-8')
cg2 = subprocess.run(['git', '-C', REPO_, 'check-ignore', '-q', 'entrada/erros/discursivas/2026-10-18_D1/resposta_candidata.md'], capture_output=True)
cg3 = subprocess.run(['git', '-C', REPO_, 'check-ignore', '-q', 'saida/treino/diagnostico_2026-10-18.md'], capture_output=True)
chk('(6) T-59', 'git check-ignore: entrada/erros/x.json e entrada/erros/discursivas/…/resposta_candidata.md são ignorados; saida/treino/diagnostico_….md (agregado sem texto) NÃO é ignorado', cg.returncode == 0 and cg2.returncode == 0 and cg3.returncode == 1, cg.stdout.strip().replace('\t', ' '))
chk('(6) T-59', 'o pacote v1.8 não traz campo novo (D-T59-10, item 1): nenhum `id` de simulado "SIM-S-…" (ainda não há simulado da semana aceito) e os 4 simulados são SIM-0, SIM-1, SIM-2, SIM-0-P2', [s['id'] for s in P18['simulados']] == ['SIM-0', 'SIM-1', 'SIM-2', 'SIM-0-P2'])
# ======================================================================= (7) E13 / T-65 (D1-T65-R1 a R3 da GCE; transporte ao Projeto é da GCE, gatilho E)
stats_ = json.load(open(os.path.join(OUT, 'stats.json'), encoding='utf-8'))
e13s = [e for e in stats_['errata'] if e['lote'] == 'L1' and e['id'] == 'E13']
chk('(7) E13', 'o registro de errata do gerador traz a L1 E13 uma vez, estado APLICADA (X encontrado 1 vez livre, Y ausente antes), aplicada ao comando da D1 depois da montagem com a E8 (D1-T65-R2)',
    len(e13s) == 1 and e13s[0]['estado'] == 'APLICADA' and e13s[0]['x_free'] == 1 and e13s[0]['y_free'] == 0, str(e13s))
sj = json.load(open(os.path.join(OUT, 'sync_check.json'), encoding='utf-8'))
chk('(7) E13', 'sync_check: a E13 (X e Y literais no Adendo 6 da consolidação) consta como conferida (x e y verdadeiros)', [(r['lote'], r['id'], r['x'], r['y']) for r in sj if r['id'] == 'E13'] == [('L1', 'E13', True, True)])
chk('(7) E13', 'GCE_Lote1_consolidacao_GCE.md (com o Adendo 6) tem SHA-256 604fa711f19949ab4560cece3dd3958b0f7582dd9af3560e5e7bc13c1df503bd, 11670 bytes e 213 quebras de linha (T65_reconciliacao, seção 1, ponto 1); termina em "FIM DO ADENDO 6"',
    hashlib.sha256(cons1_raw.encode('utf-8')).hexdigest() == '604fa711f19949ab4560cece3dd3958b0f7582dd9af3560e5e7bc13c1df503bd' and len(cons1_raw.encode('utf-8')) == 11670 and cons1_raw.count('\n') == 213 and cons1_raw.endswith('FIM DO ADENDO 6'))

# ======================================================================= (8) gerador v1_8 e não regressão (D1, 1.1, 1.2, 5 e 6.2 (8); T-69 (4))
GD = os.path.dirname(os.path.abspath(__file__)); G7 = os.path.join(GD, '..', 'gerador_v1_7')
def lf_txt(p): return rb_lf(p).decode('utf-8')
def lista_pasta(d): return sorted(f for f in os.listdir(d) if os.path.isfile(os.path.join(d, f)) and f != 'MANIFESTO.md')
f7, f8 = lista_pasta(G7), lista_pasta(GD)
iguais_g = [f for f in f8 if f in f7 and rb_lf(os.path.join(G7, f)) == rb_lf(os.path.join(GD, f))]
alter_g = [f for f in f8 if f in f7 and f not in iguais_g]
novos_g = [f for f in f8 if f not in f7]
so7 = [f for f in f7 if f not in f8]
chk('(8) GERADOR', 'arquivos da v1_8 frente à v1_7 (fora de `out/` e do MANIFESTO.md): alterados = banco.py (Adendo 1, 9.3), build_pacote.py, common.py, estudante_fidelidade.py, estudante_gen.py, refs.py, rodar_tudo.sh, validate.py (D1, 1.2); novos = conferencia_f_2026-10-17_v1_8.json, conferencias_v18.py, estudante_json.py, manifesto_v1_8.py, marcas_processo.py, relatorio_v1_8.py (D1, 1.1); não trazidos = conferencia_f_2026-10-14_v1_7.json, conferencias_v17.py, manifesto_v1_7.py, relatorio_v1_7.py; o resto idêntico (inclusive estudante_marcas.py, literais.py, p1.py, p2.py, peg.py, gce.py, banco.py, edital_p.py, f4.py, registry.py, sync_check.py, texts.py, lotes_tab.txt, validar_erros.py, validar_erros_teste.py, fidelidade_mutacao.py e os históricos)',
    alter_g == ['banco.py', 'build_pacote.py', 'common.py', 'estudante_fidelidade.py', 'estudante_gen.py', 'refs.py', 'rodar_tudo.sh', 'validate.py']
    and novos_g == ['conferencia_f_2026-10-17_v1_8.json', 'conferencias_v18.py', 'estudante_json.py', 'manifesto_v1_8.py', 'marcas_processo.py', 'relatorio_v1_8.py']
    and so7 == ['conferencia_f_2026-10-14_v1_7.json', 'conferencias_v17.py', 'manifesto_v1_7.py', 'relatorio_v1_7.py']
    and all(x in iguais_g for x in ('estudante_marcas.py', 'literais.py', 'p1.py', 'p2.py', 'peg.py', 'gce.py', 'edital_p.py', 'f4.py', 'registry.py', 'sync_check.py', 'texts.py', 'lotes_tab.txt', 'validar_erros.py', 'validar_erros_teste.py', 'fidelidade_mutacao.py', 'conferencias_R1.py', 'report.py', 'report2.py', 'relatorio_R1.py', 'diff.py', 'diff2.py', 'probe.py', 'resid.py', 'review.py')),
    'iguais %d, alterados %d, novos %d, não trazidos %d' % (len(iguais_g), len(alter_g), len(novos_g), len(so7)))
def nl_dif(f):
    a_, b_ = lf_txt(os.path.join(G7, f)).split('\n'), lf_txt(os.path.join(GD, f)).split('\n')
    return sum(max(o[2] - o[1], o[4] - o[3]) for o in difflib.SequenceMatcher(None, a_, b_, autojunk=False).get_opcodes() if o[0] != 'equal')
nd = {f: nl_dif(f) for f in alter_g}
chk('(8) GERADOR', 'linhas alteradas nos copiados (v1_7 -> v1_8): build_pacote.py 2 (docstring e `nome`/`geradoEm`, na mesma linha do `nome`), common.py 1 (comentário do caminho), refs.py 3 (docstring, `C_V17`, `v17()`), validate.py 5 (docstring, `nome`/`geradoEm` esperados, caminho do p2.py, `sys.exit`, nota sem o sufixo) e banco.py 10 (Adendo 1, 9.3) — a lista fechada da D1, 1.2; estudante_gen.py, estudante_fidelidade.py e rodar_tudo.sh: só os pontos da D1 (fusão e versão; mapeamento da fusão e versão; passos de 6.3)',
    nd['build_pacote.py'] == 2 and nd['common.py'] == 1 and nd['refs.py'] == 3 and nd['validate.py'] == 5 and nd['banco.py'] == 10, str(nd))
rf7, rf8 = lf_txt(os.path.join(G7, 'refs.py')), lf_txt(os.path.join(GD, 'refs.py'))
chk('(8) GERADOR', "refs.py: `C_V17 = '62ab128'` (pacote v1.7 f20216c2… e edição v1.7) e `v17()` acrescentados; as demais referências (v1 a v1.6) idênticas, nada removido",
    "C_V17 = '62ab128'" in rf8 and 'def v17(): return pacote(C_V17)' in rf8 and all(l in rf8.split('\n') for l in rf7.split('\n')[2:]) and refs.C_V17 == '62ab128' and refs.sha256(refs.C_V17, refs.PACOTE) == 'f20216c22600b7af7cf54b4e79d83accf3568aee8de48ad970fe800451528c7a')
# 62ab128 é o primeiro commit com esse SHA-256 no caminho do pacote (git log)
primeiro = subprocess.run(['git', '-C', REPO_, 'log', '--format=%h', '--reverse', '--', 'saida/pacote/pacote.json'], capture_output=True, text=True).stdout.split()
prim = next((h for h in primeiro if sha(subprocess.run(['git', '-C', REPO_, 'show', '%s:saida/pacote/pacote.json' % h], capture_output=True).stdout) == 'f20216c22600b7af7cf54b4e79d83accf3568aee8de48ad970fe800451528c7a'), None)
chk('(8) GERADOR', '62ab128 é o primeiro commit em que saida/pacote/pacote.json tem o SHA-256 f20216c2… (conferido por git log, D1, 1.2)', prim is not None and prim.startswith(refs.C_V17[:7]), 'primeiro commit: %s' % (prim[:7] if prim else None))
st7 = subprocess.run(['git', '-C', REPO_, 'status', '--porcelain', '--', 'saida/pacote/gerador_v1_7'], capture_output=True, text=True).stdout.strip()
df7 = subprocess.run(['git', '-C', REPO_, 'diff', '--stat', 'HEAD', '--', 'saida/pacote/gerador_v1_7'], capture_output=True, text=True).stdout.strip()
chk('(8) GERADOR', 'gerador_v1_7/ intacto: `git status --porcelain` e `git diff HEAD` da pasta vazios', st7 == '' and df7 == '', st7[:100] + df7[:100])
t8 = lf_txt(os.path.join(GD, 'rodar_tudo.sh'))
passos = [l for l in t8.split('\n') if l.startswith('python3 -B ')]
chk('(8) GERADOR', 'rodar_tudo.sh v1.8 tem os 11 passos de 6.3 na ordem (build_pacote, estudante_gen, estudante_json, estudante_fidelidade, sync_check, validate, conferencias_v18, fidelidade_mutacao, validar_erros_teste, relatorio_v1_8, manifesto_v1_8), `set -e`, cabeçalho no padrão R-1 a R-6 da T-71 (v1.8; passo 11) e nenhuma referência a v1.7, v1_7, v17',
    [p.split()[2] for p in passos] == ['build_pacote.py', 'estudante_gen.py', 'estudante_json.py', 'estudante_fidelidade.py', 'sync_check.py', 'validate.py', 'conferencias_v18.py', 'fidelidade_mutacao.py', 'validar_erros_teste.py', 'relatorio_v1_8.py', 'manifesto_v1_8.py']
    and 'set -e' in t8 and t8.split('\n')[1].startswith('# T-81 — roda o pipeline completo do gerador v1.8,') and not any(x in t8 for x in ('v1.7', 'v1_7', 'v17')) and 'estudante_json.py > out/estudante_json_stdout.txt' in t8 and 'manifesto_v1_8.py >&2' in t8 and '\r' not in t8)
# Adendo 1 (9.3): banco/banco.csv 62ab128 -> atual = exatamente as 20 linhas da 9.1, só com o sufixo acrescentado a `observacoes`
import csv, io
SUF = '; mapeamento adicional: ver banco/mapeamento_adicional.csv (D-DA-BANCO)'
def rows_csv(b): return list(csv.DictReader(io.StringIO(b.decode('utf-8'), newline=''), delimiter=';'))
b_old, b_new = rows_csv(refs.git_show(refs.C_V17, 'banco/banco.csv')), rows_csv(rb_lf(os.path.join(REPO_, 'banco', 'banco.csv')))
mud = [(o['id'], o, n) for o, n in zip(b_old, b_new) if o != n]
ESP20 = ['BQ-%04d' % k for k in (2, 3, 4, 5, 6, 7, 8, 23, 24, 25, 32, 37, 45, 46, 56, 57, 77, 84, 109, 110)]
chk('(8) BANCO Adendo 1', 'banco/banco.csv 62ab128 -> atual: mesmas linhas e ids (%d), diferença em exatamente 20 linhas (BQ-0002 a 0008, 0023 a 0025, 0032, 0037, 0045, 0046, 0056, 0057, 0077, 0084, 0109, 0110), cada uma só em `observacoes` = antiga + o sufixo literal, que aparece 1 vez; nenhum outro campo muda' % len(b_new),
    len(b_old) == len(b_new) and [o['id'] for o in b_old] == [n['id'] for n in b_new] and [m[0] for m in mud] == ESP20
    and all(n['observacoes'] == o['observacoes'] + SUF and n['observacoes'].count(SUF) == 1 and {k: v for k, v in o.items() if k != 'observacoes'} == {k: v for k, v in n.items() if k != 'observacoes'} for _, o, n in mud),
    '%d linhas diferentes' % len(mud))
chk('(8) BANCO Adendo 1', 'nenhum item do pacote v1.8 nem do pacote_estudante.json traz "mapeamento adicional" nem "D-DA-BANCO"; a nota do BQ-0003 no pacote = a da v1.7 (sem o sufixo)',
    'mapeamento adicional' not in s18 and 'D-DA-BANCO' not in s18 and 'D-DA-BANCO' not in rawE.decode('utf-8') and next(i for i in P18['itens'] if i['id'] == 'BQ-0003')['nota'] == next(i for i in P17g['itens'] if i['id'] == 'BQ-0003')['nota'])
# T-69 (4): validate.py termina com sys.exit(1 if fails else 0), e a validação reprovada para o pipeline
vtxt = lf_txt(os.path.join(GD, 'validate.py')).rstrip('\n').split('\n')
val = json.load(open(os.path.join(OUT, 'validate.json'), encoding='utf-8'))
vo = open(os.path.join(OUT, 'validate_stdout.txt'), encoding='utf-8').read().strip().split('\n')[-1]
chk('(8) T-69 (4)', 'validate.py: a última instrução, depois do json.dump, é `sys.exit(1 if fails else 0)`; continuam 118 verificações, nenhuma nova nem retirada (a D1, 1.2 e 5); a saída do passo 6 termina em "118 verificações; 0 falhas"',
    vtxt[-1].startswith('sys.exit(1 if fails else 0)') and vtxt[-2].startswith('json.dump(res') and len(val) == 118 and vo == '118 verificações; 0 falhas', vo)
bk = open(os.path.join(OUT, 'validate.json'), 'rb').read()
tmpd = tempfile.mkdtemp(prefix='val_neg_')
pn = copy.deepcopy(P18); pn['itens'][0]['gabarito'] = 'E' if pn['itens'][0]['gabarito'] == 'C' else 'C'
open(os.path.join(tmpd, 'pacote_mut.json'), 'w', encoding='utf-8', newline='\n').write(json.dumps(pn, ensure_ascii=False, indent=1) + '\n')
rv = subprocess.run([sys.executable, '-I', '-X', 'utf8', os.path.join(GD, 'validate.py'), os.path.join(tmpd, 'pacote_mut.json')], capture_output=True, text=True, encoding='utf-8', cwd=tmpd)
open(os.path.join(OUT, 'validate.json'), 'wb').write(bk)      # o validate.py grava out/validate.json: restaura o do passo 6
chk('(8) T-69 (4)', 'teste negativo: validate.py sobre uma cópia do pacote com 1 gabarito trocado sai com código 1 (e com 0 sobre o pacote íntegro: passo 6 do pipeline)', rv.returncode == 1 and 'falhas' in rv.stdout.strip().split('\n')[-1] and not rv.stdout.strip().split('\n')[-1].endswith(' 0 falhas'), 'código %d; %s' % (rv.returncode, rv.stdout.strip().split('\n')[-1]))
ej = json.load(open(os.path.join(OUT, 'estudante_json.json'), encoding='utf-8'))
chk('(8) ESTUDANTE_JSON', 'estudante_json.py: 0 falhas nas asserções (a) a (f) de 6.1 (out/estudante_json.json); CAIXA 8 e REALINHA 2, exatamente 1 cada', ej['falhas'] == [] and ej['caixa'] == {'pares': 8, 'ocorrencias': 8} and ej['realinha'] == {'pares': 2, 'ocorrencias': 2} and ej['processo'] == 0, str(ej['falhas']))
chk('(8) ESTUDANTE_JSON', 'out/estudante_json.json: 9 casamentos de R (X1–X8 e Y1), todos com o destino certo; os termos fora da lista só contados', sorted(c['destino'] for c in ej['casamentos_R']) == sorted(['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'Y1']) and set(ej['termos_fora_da_lista']) == {'Presidente', 'Projeto', 'OpenAI', 'Anthropic', 'Gemini', 'GPT', 'Whisper', 'insumo'})

# ======================================================================= (9) mutações do JSON (D1, 6.2 (9)): cada uma tem de ser detectada pela (4), pela (5)/(6) ou pela varredura R
def detecta(J):
    """lista de achados (vazia = não detectou)."""
    out = []
    out += ['(4) ' + k for k, v in sub4(J).items() if not v]
    out += ['(5) ' + k for k, v in coerencia(J, ED17, False).items() if not v]
    out += ['(6) ' + k for k, v in coerencia(J, ED18, True).items() if not v]
    sj_, cl_ = sub7(J)
    out += ['(7) ' + k for k, v in sj_.items() if not v]
    return out
def mut(fn):
    J = copy.deepcopy(JE); fn(J); return J
def m1(J):
    i = next(i for i in J['itens'] if i['gabarito'] == 'C'); i['gabarito'] = 'E'
def m2(J):
    i = J['itens'][150]; e = i['enunciado']; k = next(k for k, ch in enumerate(e) if ch == 'a'); i['enunciado'] = e[:k] + 'e' + e[k + 1:]
def m3(J):
    l = lote_json(J, 'L2'); l['curso'] = l['curso'].replace('\n', ' Fundador\n', 1)
def m4(J):
    l = lote_json(J, 'L1'); assert SEP in l['curso']; l['curso'] = l['curso'].replace(SEP, '\n\n', 1)
def m5(J):
    l = lote_json(J, 'L1'); l['pegadinhas'] = l['pegadinhas'][:-1]
def m6(J):
    i = next(i for i in J['itens'] if i['rotulo'] == 'AUTORAL'); i['url'] = 'saida/gce/GCE_Lote1_v2_CPP.md'
def m7(J):
    i = next(i for i in J['itens'] if i['rotulo'] == 'AUTORAL' and i['id'] == 'L2-Q01' or (i['rotulo'] == 'AUTORAL' and len(i['justificativa'].split()) > 8)); w = i['justificativa'].split(' '); del w[3]; i['justificativa'] = ' '.join(w)
def m8(J):
    l = lote_json(J, 'L3'); assert '(órgão da Presidência da' in l['curso']; l['curso'] = l['curso'].replace('(órgão da Presidência da', '(órgão da', 1)
MUTS = [('M1', 'trocar 1 gabarito', m1), ('M2', 'trocar 1 caractere de 1 enunciado', m2), ('M3', 'inserir "Fundador" num curso', m3), ('M4', 'tirar o separador "## Complemento"', m4),
        ('M5', 'tirar 1 pegadinha do L1C (a última do L1 fundido)', m5), ('M6', 'restaurar a `url` de 1 AUTORAL', m6), ('M7', 'apagar 1 palavra não marcada de 1 justificativa', m7),
        ('M8', 'apagar o contexto de X4 (entrada de X com contagem 0)', m8)]
base_ach = detecta(JE)
chk('(9) MUTAÇÕES', 'linha de base: o JSON íntegro não gera achado em (4), (5), (6) nem na varredura R', base_ach == [], str(base_ach[:3]))
mdet = []
for cod, desc, fn in MUTS:
    ach = detecta(mut(fn))
    mdet.append((cod, bool(ach)))
    chk('(9) MUTAÇÕES', '%s %s: detectada' % (cod, desc), bool(ach), '; '.join(a[:90] for a in ach[:3]))
chk('(9) MUTAÇÕES', '8/8 detectadas', len(mdet) == 8 and all(d for _, d in mdet), str(mdet))

import shutil
shutil.rmtree(tmpd, ignore_errors=True); shutil.rmtree(os.path.dirname(EX_TMP), ignore_errors=True)      # pastas temporárias dos testes (fora do repositório)
fails = [r for r in res if not r[2]]
print('\n%d conferências; %d falhas' % (len(res), len(fails)))
with open(os.path.join(OUT, 'conferencias_v18.txt'), 'w', encoding='utf-8') as f:
    for c, alvo, ok, det in res:
        f.write(('OK    ' if ok else 'FALHA ') + c + ' | ' + alvo + (' | ' + det if det else '') + '\n')
    f.write('\n%d conferências; %d falhas\n' % (len(res), len(fails)))
json.dump([list(r) for r in res], open(os.path.join(OUT, 'conferencias_v18.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
sys.exit(1 if fails else 0)
