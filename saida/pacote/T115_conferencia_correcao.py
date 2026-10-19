# -*- coding: utf-8 -*-
"""T-115 (pacote v1.12) — conferência da GBQ depois da correção dos achados 1 a 3 da fidelidade (saida/pacote/T115_reconciliacao_v1_12_2026-10-18.md, seção 3).
GBQ (gbq-gerencia), 2026-10-18. Somente leitura. Uso (Git Bash, raiz do repositório):
  python -I -B saida/pacote/T115_conferencia_correcao.py <pasta da rodada 1 de out/, cópia feita antes da correção>
A rodada 1 é a saída que a gbq-cqe examinou; o script confere o SHA-256 de cada arquivo dela contra as constantes abaixo antes de usá-la.
Critério: JSON e registros iguais à rodada 1; dos 35 .md, 23 iguais e 12 mudados só nas linhas previstas; nenhum código de produção nem legenda de mecanismo nos 35;
gerador_v1_12 sem CR fora de out/; conferências e mutação do gerador sem falha; MANIFESTO igual ao disco. Sai com código 1 na primeira divergência e imprime OK no fim."""
import hashlib, json, os, re, sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
G = os.path.join(RAIZ, 'saida', 'pacote', 'gerador_v1_12')
OUT = os.path.join(G, 'out')
R1 = sys.argv[1] if len(sys.argv) > 1 else None
INALTERADOS = {  # rodada 1 (fidelidade_v1_12_gbq-cqe.md) — devem ficar iguais
    'pacote.json': '3476525319b027fe4427bf93598d516087ad6f18fb8dd5bbed4ad8c04be6024f',
    'pacote_estudante.json': '23224c96b4189097012f139f52a9b995c29d930c6ac72801659720d6db612abd',
    'registro_adendo4.md': '52a47eec0f7c33e63ff73968fc5064d8665a18e08b6c2e45694f5da63b6af228',
    'registro_alteracoes_v1_12.csv': '437e2303172e25e1c45a9500b0d1fffb54e75fb59e3aa952b3eacf1c4da98662',
    'registro_alteracoes_v1_12_resumo.md': 'e5a92904ce3abda41415d6403474fee63280c1eb88afb3d4eeecac5b5744ff84',
    'stats_v1_12.json': '50a3ca3f29656f6b22b3e4c913125a457075e1f360a6579d6a07f2f59094e22e',
    'folhas_v1_12.json': 'b7e859051d98bdf730ba4d00f3fc2113c5fd002be0079783e8e19f34b7cb1c8a',
}
MD_R1 = {
    'BANCO_gabarito.md': 'f7d9bb470356e98962227bc7d19dbd6de2eff053aa718df002b26d6f2b4cb5ed', 'BANCO_itens.md': '879e1769c76c3bc655510a18a8fd66f49abb6dec52d7e3030adf93132a226c2c',
    'DISCURSIVAS.md': '7777c52ca635cdd0e33a525aadd3b86699d333def9bb61816c79b67653f17bd0', 'DISCURSIVAS_padrao.md': '4d5a4e6e9cb23fffee9b401f7b8b9537ce9475cdc8127e34cd27c6592f77dcb4',
    'L1_estudo.md': '3af116b241f6f6c2a64ff550df4a1b589a5fa85520341acb80817950f7ce1ea1', 'L1_gabarito.md': '2947f638e5f9f1a08133716a7bb3b4d6f961330aa87dc5fc9d5252bec363cf7a',
    'L1_itens.md': '94e106e720f28ace0fedabb9e5050ee018e2e5147cef926700cff45929325050', 'L2_estudo.md': '7f08bc22ab7a52b5b33478d2e24286397174f39b657f7fdb6d49d6268f80b111',
    'L2_gabarito.md': '7aa74384f5dd7e5bac2f49dc3d6b50af0322ccc10ba07cfcd0a41f9cb166d2b4', 'L2_itens.md': '9bb73429f2a9e29713c49247a61b58b1c4537aeac3850a47e3c698af5ffe7924',
    'L3_estudo.md': '692aa09f29d79ec8ce2ba13d7f72b4aca64acaff04781e66361559d18f170170', 'L3_gabarito.md': '5a2516422ebb27293f0a337fcae04ad539de3122e6e9c97c0cfdfd450028ce92',
    'L3_itens.md': 'b4ca1f7707a5789eb1750caa833d9a4d6a60d930642dc4908065e2b128bf2281', 'L4_estudo.md': 'ab3cc2ca518e9d6f7f0de1342fc1fbe884233052a5f842448692474f960e67d6',
    'L4_gabarito.md': 'b6b74d1b62bcb921fd5198e9ed9a3ed07e54df97d7d14bf78161e3a1c5da7437', 'L4_itens.md': '6620555a3b368b66c1ca21a2ebc1faf9a2515016e747d64acf567d6a523c6545',
    'L5_estudo.md': '27bd4b5e24d24446d89898026c64fe3040bd42cec9e4ced1245d8eb8ed79a616', 'L5_gabarito.md': '0a5870491b761d50ebbf1630681097cce20a794504630f79af403d4b4087bfbd',
    'L5_itens.md': 'e110570384225bda943dd709e1a4272faa6581b94eadad6ebf6f42fc488afaa3', 'L6A_estudo.md': '9da2d2792c5b01c2334896c046264cd15bd816216891e9ac4eb83a8c1e8ad638',
    'L6A_gabarito.md': 'f2a974f973f90a9ec9e0d7a79339251a4e4157c9376a5c3bd0cd598602cc6a4f', 'L6A_itens.md': 'afa0a0e333ff7ac2d4857ee80e72142a8825befb417832c15921f1663ff31b1e',
    'L6B_estudo.md': '476718a71d1f8a7e500360006481b9bfeb55cd7b27f9e447d292c7daa396d3f9', 'L6B_gabarito.md': 'ea2877f09a401de64856d99d86a0de14e97526f4f4e3085ddda43e11568009e4',
    'L6B_itens.md': 'cac479bf65a9d8fc9e8d94822eed87e8f6b0257cf49c2028dab6f43873565077', 'NUCLEO.md': 'bf13d9dff214e1e3dd699028c27617c11f96e640c4bbdf8bba42e96e0d15260a',
    'README.md': '8048d862c58afbedd9d952e576e758c43989b1245815a367e8990e261ea0379a', 'SIM-0-P2_folha.md': 'f69efe607e7b575c246b46eded5ce15d5b6cf1e14ae755bc1bff23087c8bdab5',
    'SIM-0-P2_gabarito.md': 'cdd8a6588d0e24ebd4e445a50a7d11334e324eb4a85dbfd46b7babe0bbdcc081', 'SIM-0_folha.md': '7ef04f37578a2da082ab8c016ac06a06e8463db96089c268cd7e9b100815cd16',
    'SIM-0_gabarito.md': '2df79ffa2501e38c66564a8b2a23cd5632372255bf7214c9179ca8ece3788374', 'SIM-1_folha.md': 'e0e21ea32da954f4d20ac9df23937dab412179873d28211876600e938c2b9a38',
    'SIM-1_gabarito.md': '535287fa7cfe59fd2e1f5297cd7058ac7af3234d728934eaeb8b09238462c2ca', 'SIM-2_folha.md': 'd576cc3fecc6f9973a028f82e303abb65aedd00ad14000cbc263c51423daaa92',
    'SIM-2_gabarito.md': '2113d4a7c1e399a1ce25b71d5819fe565121d3fc41c9a4d4c2b3e3e75e248c9e',
}
LOTES = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6A', 'L6B']
ESTUDO = ['%s_estudo.md' % l for l in LOTES]                       # achado 1: só a linha 1
LEGENDA = {'L4_gabarito.md': 1, 'L5_gabarito.md': 1, 'L6A_gabarito.md': 1, 'L6B_gabarito.md': 1, 'SIM-1_gabarito.md': 2}   # achado 2: linhas a retirar
CODIGOS = ['RF-ASR', 'RF-DEGRAVACAO', 'RF-IA-PARLAMENTAR', 'RF-PROTECAO', 'TID-IA', 'TID-DADOS-VIZ', 'TI-FERRAMENTAS', 'TI-REDES-SEGURANCA', '(v0.2)']
LEG = re.compile(r'^Mecanismos?: (?:troca de conceito \(TC\)|TC troca de conceito)')


def falha(m):
    print('FALHA: ' + m)
    sys.exit(1)


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


if not R1 or not os.path.isdir(R1):
    falha('informe a pasta da rodada 1 (cópia de out/ anterior à correção)')
for n, s in list(INALTERADOS.items()):
    if sha(os.path.join(R1, n)) != s:
        falha('rodada 1 adulterada: %s' % n)
    if sha(os.path.join(OUT, n)) != s:
        falha('%s mudou (devia ficar igual à rodada 1)' % n)
for n, s in MD_R1.items():
    if sha(os.path.join(R1, 'estudante', n)) != s:
        falha('rodada 1 adulterada: estudante/%s' % n)
if sorted(os.listdir(os.path.join(OUT, 'estudante'))) != sorted(MD_R1):
    falha('conjunto dos 35 .md mudou')
E = json.load(open(os.path.join(OUT, 'pacote_estudante.json'), encoding='utf-8'))
nome = {l['id']: l['nome'] for l in E['lotes']}
mud = []
for n in sorted(MD_R1):
    a = open(os.path.join(R1, 'estudante', n), encoding='utf-8').read().split('\n')
    b = open(os.path.join(OUT, 'estudante', n), encoding='utf-8').read().split('\n')
    if n in ESTUDO:
        lid = n.split('_')[0]
        if b[0] != '# ' + nome[lid] or a[1:] != b[1:] or a[0] == b[0]:
            falha('%s: devia mudar só a linha 1, para "# %s"' % (n, nome[lid]))
        mud.append(n)
    elif n in LEGENDA:
        idx = [k for k, l in enumerate(a) if LEG.match(l)]
        if len(idx) != LEGENDA[n] or any(a[k + 1] != '' for k in idx):
            falha('%s: legendas na rodada 1 = %d (esperado %d, cada uma seguida de linha em branco)' % (n, len(idx), LEGENDA[n]))
        esperado = [l for k, l in enumerate(a) if k not in idx and k - 1 not in idx]
        if b != esperado:
            falha('%s: devia perder só as %d linhas de legenda e a linha em branco seguinte' % (n, LEGENDA[n]))
        mud.append(n)
    elif a != b:
        falha('%s mudou (devia ficar igual à rodada 1)' % n)
for n in MD_R1:
    t = open(os.path.join(OUT, 'estudante', n), encoding='utf-8').read()
    for c in CODIGOS:
        if c in t:
            falha('%s ainda traz %r' % (n, c))
    if any(LEG.match(l) for l in t.split('\n')):
        falha('%s ainda traz legenda de mecanismo' % n)
for r, ds, fs in os.walk(G):
    ds[:] = [d for d in ds if d not in ('out', '__pycache__')]
    for f in fs:
        if b'\r' in open(os.path.join(r, f), 'rb').read():
            falha('CR em %s (gerador_v1_12 fora de out/ deve estar em LF)' % os.path.relpath(os.path.join(r, f), RAIZ))
conf = open(os.path.join(OUT, 'conferencias_stdout.txt'), encoding='utf-8').read().strip().split('\n')[-1]
if not re.search(r' OK, 0 PENDENTE, 0 FALHA \(modo FINAL\)$', conf):
    falha('conferências: %s' % conf)
mut = open(os.path.join(OUT, 'fidelidade_mutacao_stdout.txt'), encoding='utf-8').read().strip().split('\n')[-1]
m = re.search(r'mutações detectadas: (\d+)/(\d+)', mut)
if not m or m.group(1) != m.group(2):
    falha('mutação: %s' % mut)
man = open(os.path.join(G, 'MANIFESTO.md'), encoding='utf-8').read()
nlin = 0
for mm in re.finditer(r'^\| `([^`]+)` \| `([0-9a-f]{64})` \| (\d+) \|', man, re.M):
    p = os.path.join(G, mm.group(1)) if not mm.group(1).startswith('ensaio/') else os.path.join(G, mm.group(1))
    if not os.path.isfile(p):
        continue
    nlin += 1
    if sha(p) != mm.group(2) or os.path.getsize(p) != int(mm.group(3)):
        falha('MANIFESTO difere do disco: %s' % mm.group(1))
print('OK: JSON e registros iguais à rodada 1; .md mudados = %d (%s); 23 iguais; 0 código e 0 legenda nos 35; gerador sem CR; %s; %s; MANIFESTO %d linhas = disco'
      % (len(mud), ', '.join(mud), conf, mut, nlin))
for n in sorted(mud):
    print('  %s  %s' % (sha(os.path.join(OUT, 'estudante', n)), n))
