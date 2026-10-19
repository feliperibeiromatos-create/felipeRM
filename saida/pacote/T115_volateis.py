# -*- coding: utf-8 -*-
"""T-115 (pacote v1.12) — lista, por script, dos VOLÁTEIS novos da v1.12 para a T-11 (reverificação de janeiro, 4–8/1/2027; D-REVERIFICACAO-JAN).
GBQ (gbq-gerencia), 2026-10-18, ciclo s14c4. Somente leitura dos arquivos finais aceitos; grava só saida/pacote/T115_volateis_T11.md.
Uso (Git Bash, na raiz do repositório): python -I -B saida/pacote/T115_volateis.py
Fontes (SHA-256 do conteúdo com CRLF → LF; o mesmo do blob no git):
- onda 4 (D-T98-ONDA4-ACEITE): saida/gce/L3_reforco_onda4_A_v3.md, B_v2.md, C_v3.md;
- onda 1 da ORDEM_V15_F, P2 (D-V112-BAEF-P2-ACEITE): saida/gce/T113_onda1_A_v2.md a D_v2.md, menos os 5 vagos e os 2 diferidos;
- onda 1 da ORDEM_V15_F, P1 (D-V112-BAEF-P1-ACEITE): saida/gcb/T113_onda1_P1_v2.md (bloco json; sem campo volatil).
VOLÁTIL = coluna VOLÁTIL da Parte 1 (MAPA) começando por "s" ou "VOLÁTIL"; "n…" = não VOLÁTIL. Falha (SystemExit) se uma contagem divergir da decisão de aceite."""
import collections, hashlib, json, os, re, sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
SAIDA = os.path.join(RAIZ, 'saida', 'pacote', 'T115_volateis_T11.md')
FENCE = '`' * 3
ONDA4 = [('saida/gce/L3_reforco_onda4_A_v3.md', '5be2941157f7db21e9d2f3b09007fbfd6ccafbc31608d37e3434e3fa8913c2b0'),
         ('saida/gce/L3_reforco_onda4_B_v2.md', '09d9d52144238358eb7fbf8ffcc35b71fa99b0b30e97fbb24410d2b563f7f398'),
         ('saida/gce/L3_reforco_onda4_C_v3.md', 'd9faf9a70e698432afd4767a785bb526d97b2adadd60685ce468c1eba6241344')]
F1 = [('saida/gce/T113_onda1_A_v2.md', '8c15789308f7a7f5d295ee1a740b0707701dfb723f7fb3ecee2ce201760df081'),
      ('saida/gce/T113_onda1_B_v2.md', '74602cafd57d6bf10722068ecd30b54f771a46cc2c2e050e41a270b98016f01b'),
      ('saida/gce/T113_onda1_C_v2.md', 'a332fb3f2b2344a065642d2d890241c1d9744de1b9cd8cba5f537bd2b8a4896d'),
      ('saida/gce/T113_onda1_D_v2.md', '9aae8f8a05a693f0b209147b6fe5b88e336a015f387d4bcaa6c2a550140b531d')]
F1_P1 = ('saida/gcb/T113_onda1_P1_v2.md', '0b863e476f14d01ef801635b0e67998b24924213723d96c4a791e26c7dd6da4f')
VAGOS = {'L1-R140', 'L2-R136', 'L2-R137', 'L2-R140', 'L3-R101'}
DIFERIDOS = {'L3-R103', 'L3-R104'}
# transcritos das decisões (DECISOES.md), não do arquivo lido
ESPERADO_O4 = ['L3-R12', 'L3-R13', 'L3-R14', 'L3-R16', 'L3-R27', 'L3-R56', 'L3-R59', 'L3-R65', 'L3-R91', 'L3-R94']
ESPERADO_F1 = ['L1-R139', 'L1-R159', 'L1-R160', 'L1-R161', 'L1-R168', 'L1-R170', 'L1-R171', 'L1-R177', 'L1-R178', 'L1-R180', 'L1-R183', 'L1-R184',
               'L1-R185', 'L1-R187', 'L1-R191', 'L1-R194', 'L1-R200', 'L1-R201', 'L2-R135', 'L2-R141', 'L2-R142', 'L3-R100']
URL_ERRATA = ('https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm', 'https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm')


def falha(m):
    raise SystemExit('FALHA: ' + m)


def texto(rel, sha):
    b = open(os.path.join(RAIZ, rel), 'rb').read().replace(b'\r\n', b'\n')
    if hashlib.sha256(b).hexdigest() != sha:
        falha('SHA-256 (LF) de %s diverge do aceito' % rel)
    return b.decode('utf-8')


def mapa(t, rel):
    a = t.index('PARTE 1/3')
    b = min(x for x in (t.find('FIM DA PARTE 1/3', a), t.find('PARTE 2/3', a)) if x > 0)
    m = collections.OrderedDict()
    for ln in t[a:b].split('\n'):
        c = [x.strip() for x in ln.strip().strip('|').split('|')]
        if len(c) >= 7 and re.match(r'L\d-R\d+$', c[0]) and c[0] not in m:
            m[c[0]] = dict(folha=c[1], base=c[4], vol=c[5], arquivo=rel)
    if not m:
        falha('mapa vazio em %s' % rel)
    for k, d in m.items():   # MAPA sem URL (L3-R91, R94): URL da linha "Base:" do bloco do item na Parte 3
        if 'http' not in d['base']:
            b3 = re.search(r'\*\*%s\*\* \([^)]*\)[^\n]*Gabarito[^\n]*\n(?:[^\n]+\n)*?Base: ([^\n]+)' % re.escape(k), t[t.index('PARTE 3/3'):])
            if b3:
                d['base'] = d['base'] + ' — Parte 3: ' + b3.group(1)
    return m


def vol(v):
    v = v.strip()
    if v.startswith('n'):
        return False
    if v.startswith('s') or v.startswith('VOLÁTIL'):
        return True
    falha('coluna VOLÁTIL ilegível: %r' % v)


def urls(base):
    return [u.rstrip('.,') for u in re.findall(r'https?://[^\s;)]+', base.replace(URL_ERRATA[0], URL_ERRATA[1]))]


o4 = collections.OrderedDict()
for rel, sha in ONDA4:
    o4.update(mapa(texto(rel, sha), rel))
f1 = collections.OrderedDict()
for rel, sha in F1:
    for k, v in mapa(texto(rel, sha), rel).items():
        if k not in VAGOS:
            f1[k] = v
t = texto(*F1_P1)
p1 = json.loads(re.findall(FENCE + r'json\n(.*?)\n' + FENCE, t, re.S)[0])
if len(o4) != 84 or len([k for k in f1 if k not in DIFERIDOS]) != 98 or len(p1) != 7:
    falha('contagens: onda 4 %d (84), F1 P2 %d (98), F1 P1 %d (7)' % (len(o4), len([k for k in f1 if k not in DIFERIDOS]), len(p1)))
v4 = [k for k, v in o4.items() if vol(v['vol'])]
vf = [k for k, v in f1.items() if k not in DIFERIDOS and vol(v['vol'])]
if v4 != ESPERADO_O4:
    falha('VOLÁTEIS da onda 4: %s' % v4)
if vf != ESPERADO_F1:
    falha('VOLÁTEIS da F1 P2: %s' % vf)
if any(i.get('volatil') for i in p1):
    falha('F1 P1 com volatil')
t11 = [l for l in open(os.path.join(RAIZ, 'TAREFAS.md'), encoding='utf-8').read().replace('\r\n', '\n').split('\n') if l.startswith('T-11;')]
if len(t11) != 1:
    falha('linha T-11 não encontrada')
t11 = t11[0]
seg98 = re.search(r'\[acréscimo T-98[^\]]*\]', t11)


def na_t11(k):
    if k.startswith('L3-R') and seg98 and int(k[4:]) <= 95:
        return re.search(r'(?<![\w-])(?:L3-)?R%d(?!\d)' % int(k[4:]), seg98.group(0)) is not None
    return k in t11


L = []
w = L.append
w('# T115_volateis_T11.md — T-115 (pacote v1.12) — VOLÁTEIS novos para a T-11 — 2026-10-18 — gerado por gbq-gerencia (saida/pacote/T115_volateis.py)')
w('')
w('Gerado por script (python -I -B saida/pacote/T115_volateis.py), somente leitura dos arquivos finais aceitos, com o SHA-256 do conteúdo LF conferido. VOLÁTIL = coluna VOLÁTIL do MAPA (Parte 1). '
  'Todo VOLÁTIL abaixo é inapto a simulado final até a reverificação de 4–8/1/2027 (CLAUDE.md, VOLÁTIL; D-REVERIFICACAO-JAN), com reabertura obrigatória da URL. '
  'A coluna "na T-11 hoje" lê a linha T-11 de TAREFAS.md no momento da geração. Quem acrescenta à T-11 é o orquestrador (D-T98-ONDA4-ACEITE (5); D-V112-BAEF-P2-ACEITE (5); D-V112-BAEF-P1-ACEITE (5)).')
w('')
w('## 1. VOLÁTEIS novos da v1.12 (%d)' % (len(v4) + len(vf)))
w('')
w('| # | id | folha | risco (MAPA) | URL a reabrir | arquivo final | ato | na T-11 hoje |')
w('|--:|---|---|---|---|---|---|---|')
n = 0
for grupo, ks, src, ato in (('onda 4', v4, o4, 'D-T98-ONDA4-ACEITE'), ('F1 P2', vf, f1, 'D-V112-BAEF-P2-ACEITE')):
    for k in ks:
        n += 1
        d = src[k]
        w('| %d | %s | %s | %s | %s | %s | %s | %s |' % (n, k, d['folha'], d['vol'], '<br>'.join(urls(d['base'])) or '(sem URL no MAPA)', d['arquivo'], ato, 'sim' if na_t11(k) else 'não: acrescentar'))
w('')
w('F1 P1 (L4-R01 a L4-R07, D-V112-BAEF-P1-ACEITE): 0 VOLÁTIL.')
w('')
w('## 2. Conferência de base, sem efeito de VOLÁTIL')
w('')
cb4 = [k for k in o4 if k not in v4]
cbf = [k for k in f1 if k not in DIFERIDOS and k not in vf]
w('- onda 4: %d itens (L3-R12 a L3-R95 menos os 10 VOLÁTEIS da seção 1); já na T-11 pelo acréscimo da T-98, com as notas da seção 8 da saida/gce/T98_reconciliacao_2026-10-18.md.' % len(cb4))
w('- F1 P2: %d itens: %s. Notas das R2 (B, seção 5; C, seção 4; D, seções 2 e 4). A base dos L3-R105 a R108 é o texto compilado da LGPD (%s), pela errata de URL da D-V112-BAEF-P2-ACEITE.' % (len(cbf), ', '.join(cbf), URL_ERRATA[1]))
w('- F1 P1: 7 itens (%s), com as duas páginas do Google for Developers citadas nas justificativas (gcb-cqfp/FV).' % ', '.join(i['id'] for i in p1))
w('')
w('## 3. Diferidos (aprovados na R2, fora da v1.12; D-V112-BAEF-P2-ACEITE)')
w('')
for k in sorted(DIFERIDOS):
    d = f1[k]
    w('- %s (%s; MAPA: %s; %s): entra na T-11 só quando for consolidado (onda 2 da ORDEM_V15_F); não entra agora.' % (k, d['folha'], d['vol'], '; '.join(urls(d['base']))))
w('')
w('## 4. Totais')
w('')
w('- VOLÁTEIS no pacote.json v1.12 = 54 (v1.11, os mesmos da v1.10) + %d (onda 4) + %d (F1 P2) + 0 (F1 P1) = %d. É a lista de `volatil: true` que a C-V da D1 (saida/pacote/T115_D1_v1_12_2026-10-18.md) confere no gerador.' % (len(v4), len(vf), 54 + len(v4) + len(vf)))
por = collections.Counter(o4[k]['folha'] for k in v4) + collections.Counter(f1[k]['folha'] for k in vf)
w('- VOLÁTEIS novos por folha: %s.' % ', '.join('%s %d' % (f, c) for f, c in sorted(por.items())))
w('')
w('## 5. Texto para a T-11 (orquestrador; só o que ainda não está nela)')
w('')
faltam = [k for k in v4 + vf if not na_t11(k)]
w('[acréscimo de 18/10/2026, ciclo s14c4 (D-V112-BAEF-P2-ACEITE; D-V112-BAEF-P1-ACEITE; T-115, saida/pacote/T115_volateis_T11.md): P2, gce-cqfp — VOLÁTEIS (inaptos a simulado final até a reverificação, reabertura obrigatória da URL): %s; conferência de base, sem efeito de VOLÁTIL, dos outros %d itens da onda 1 da F (notas das R2: B §5, C §4, D §2 e §4; L3-R105 a R108 no compilado da LGPD); L3-R103 e R104 quando consolidados. P1, gcb-cqfp/FV — conferência de base dos L4-R01 a L4-R07 (duas páginas do Google for Developers), sem efeito de VOLÁTIL]'
  % (', '.join(faltam) if faltam else '(nenhum)', len(cbf)))
w('')
w('FIM DO ARQUIVO')
open(SAIDA, 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
print('ok: %d VOLÁTEIS novos (onda 4 %d, F1 P2 %d); faltam na T-11: %d; gravado %s' % (len(v4) + len(vf), len(v4), len(vf), len(faltam), SAIDA))
