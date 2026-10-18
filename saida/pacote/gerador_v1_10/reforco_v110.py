# -*- coding: utf-8 -*-
"""T-104 (v1.10) — leitor dos arquivos finais aceitos depois da v1.9 (D1 da GBQ, saida/pacote/T104_D1_v1_10_2026-10-18.md, seção 2):
- L6B-R01, L6B-R02 (saldo do R4 da onda 1; D-T102-R4-SALDO): saida/gcb/L6B_reforco_onda1_saldo_v2.md;
- onda 2, L1-R19 a L1-R130 sem L1-R43 (D-T96-ONDA2-ACEITE): saida/gce/L1_reforco_onda2_A_v3.md, B_v2.md, C_v2.md, D_v3.md;
- saldo da onda 2, L1-R131 (D-T103-SALDO-ACEITE): saida/gce/L1_reforco_onda2_saldo_v2.md;
- onda 3, L2-R19 a L2-R130 sem L2-R67 (D-T97-ONDA3-ACEITE): saida/gce/L2_reforco_onda3_A_v3.md a D_v3.md;
- L2-R131 (T-105): CONDICIONAL — só entra se ACEITE_L2_R131 for preenchido (arquivo final e SHA-256 da decisão de aceite) antes da geração final; vazio no ensaio.
Só leitura. Devolve os itens no formato de item do contrato (14 campos + `volatil` quando verdadeiro), na ordem dos atos de aceite (D-T102, D-T96, D-T103, D-T97, [T-105])
e, dentro de cada ato, na ordem numérica do id; e os metadados de registro. Falha (SystemExit) se qualquer contagem divergir das transcritas das decisões (ACEITE) ou se
o SHA-256 de um arquivo divergir do aceito.
Mapeamento (contrato v1.2.6, ponto 2, com a precisão da errata v1.2.7 proposta na D1, seção 5):
- comando: "Julgue o item." (L1, L2); nos L6B-R, a frase de comando inteira da Parte 2, depois de "AUTORAL. " (regra (h) da v1.2); textoBase "";
- enunciado: a linha do item na Parte 2 (d);
- justificativa: o texto da LINHA DE CABEÇALHO do item na Parte 3 (d-G), depois de "id. G[ [TS]][ (espelho)]. ", literal; as linhas seguintes do bloco (Base:,
  Formato:, REVERIFICAR:, Nota…, Troca sutil:, Espelho…, comentários à QA) NÃO entram; nos L6B-R, o texto depois de "Justificativa (duas linhas): ";
- aderencia: "parcial" só nos ids das decisões de aceite (onda 3: os 43 da seção 3.1 da T97_reconciliacao), conferido contra a coluna de aderência do mapa; demais "direta";
- volatil: true só nos ids das decisões de aceite, conferido contra a coluna VOLÁTIL do mapa;
- cargo "Lote 1", "Lote 2", "Lote 6b"; certame "Projeto Câmara 2026"; ano 2026; numero = o número do id (Rnn ou Rnnn); url = o caminho do arquivo final;
- formato de L1-R99 = PC (T96_reconciliacao, seção 3, prevalece sobre o mapa do C_v2)."""
import collections, hashlib, re
from common import read, P

G = collections.OrderedDict()      # grupo (ato de aceite) -> dict
G['L6B'] = dict(ato='D-T102-R4-SALDO', lote='L6B', cargo='Lote 6b', prova='P1', arquivos=[
    ('saida/gcb/L6B_reforco_onda1_saldo_v2.md', '785c91e9486af3937439336041d8415f4287f841d5e6d69875294282a1ca682d', ['R01', 'R02'])])
G['ONDA2'] = dict(ato='D-T96-ONDA2-ACEITE', lote='L1', cargo='Lote 1', prova='P2', arquivos=[
    ('saida/gce/L1_reforco_onda2_A_v3.md', '8fbe66c7130066cbb7164d100bc2684c60de2f196a1989646a3081088b6408af', ['R%02d' % k for k in range(19, 47) if k != 43]),
    ('saida/gce/L1_reforco_onda2_B_v2.md', '201a3172c97792474627b22d7c749f7a21389a4984d2926c8b4e0364afc7b23e', ['R%02d' % k for k in range(47, 75)]),
    ('saida/gce/L1_reforco_onda2_C_v2.md', '37043a8c1ea154a3bd02e559163d8e68d2606ae290802cffc41b8553a64cfce3', ['R%02d' % k for k in range(75, 103)]),
    ('saida/gce/L1_reforco_onda2_D_v3.md', '12349d7ea5e3a2203bb6fb3ef92219cda9d01d33cb3987d985ea316cd0d50a40', ['R%02d' % k for k in range(103, 131)])])
G['SALDO2'] = dict(ato='D-T103-SALDO-ACEITE', lote='L1', cargo='Lote 1', prova='P2', arquivos=[
    ('saida/gce/L1_reforco_onda2_saldo_v2.md', '37f7e91d4a6b1a513ef43abdd877c06a345f3625815a9b547f6a3cb9fc034494', ['R131'])])
G['ONDA3'] = dict(ato='D-T97-ONDA3-ACEITE', lote='L2', cargo='Lote 2', prova='P2', arquivos=[
    ('saida/gce/L2_reforco_onda3_A_v3.md', 'b6911efb412198ff7685a1dfd7d7451c9f55c33152dbd9d42cf6b614019d7b9c', ['R%02d' % k for k in range(19, 47)]),
    ('saida/gce/L2_reforco_onda3_B_v3.md', 'f3b3320408e36265638a0f742b4df5a10121520e2631ebc16994df83069510f1', ['R%02d' % k for k in range(47, 75) if k != 67]),
    ('saida/gce/L2_reforco_onda3_C_v3.md', '4bbde472b049203c784f2e1840119ab13aad2a17c34accc35465661228c4ff3d', ['R%02d' % k for k in range(75, 103)]),
    ('saida/gce/L2_reforco_onda3_D_v3.md', '892526fcb3fd62ba266976e2f223fd49fb392e766ac3eb26fade700af646d293', ['R%02d' % k for k in range(103, 131)])])
# T-105: preencher só com o aceite (arquivo final, SHA-256 da decisão, gabarito, [TS], folha, VOLÁTIL, aderência) antes da geração final; vazio = L2-R131 fora (v1.11)
ACEITE_L2_R131 = None


def folha_por_faixa(prefixo, k):
    """folha das ondas 2 e 3 pela faixa de id (T96 e T97_reconciliacao, seção de contagens): R19–R32 x.1, R33–R46 x.2, …, R117–R130 x.8."""
    return 'P2-%s.%d' % (prefixo, (k - 19) // 14 + 1)


# Constantes transcritas das decisões de aceite (DECISOES.md) e das reconciliações que elas mandam prevalecer — NÃO do arquivo lido
ACEITE = {
    'L6B': dict(n=2, C=1, E=1, ts=['R02'], vol=[], parcial=[], gab={'R01': 'C', 'R02': 'E'}, folha={'P1-4.3': (1, 1)}),
    'ONDA2': dict(n=111, C=56, E=55, nts=65, vol=['R49', 'R54', 'R57', 'R65', 'R67', 'R69', 'R86', 'R87', 'R88', 'R110', 'R114'], parcial=[],
                  folha={'P2-1.1': (7, 7), 'P2-1.2': (7, 6), 'P2-1.3': (7, 7), 'P2-1.4': (7, 7), 'P2-1.5': (7, 7), 'P2-1.6': (7, 7), 'P2-1.7': (6, 8), 'P2-1.8': (8, 6)}),
    'SALDO2': dict(n=1, C=0, E=1, ts=['R131'], vol=[], parcial=[], gab={'R131': 'E'}, folha={'P2-1.2': (0, 1)}),
    'ONDA3': dict(n=111, C=56, E=55, nts=69,
                  vol=['R24', 'R25', 'R37', 'R56', 'R57', 'R60', 'R61', 'R66', 'R77', 'R81', 'R82', 'R85', 'R94', 'R99', 'R100', 'R120', 'R121', 'R125'],
                  parcial=['R19', 'R21', 'R22', 'R25', 'R27', 'R28', 'R29', 'R31', 'R32', 'R35', 'R38', 'R39', 'R41', 'R42', 'R45', 'R46',
                           'R47', 'R50', 'R51', 'R52', 'R53', 'R54', 'R55', 'R58', 'R59', 'R60', 'R61', 'R63', 'R64', 'R65', 'R66', 'R69', 'R71', 'R73', 'R74',
                           'R79', 'R84', 'R85', 'R91', 'R94', 'R101', 'R102', 'R130'],
                  folha={'P2-2.1': (7, 7), 'P2-2.2': (7, 7), 'P2-2.3': (7, 7), 'P2-2.4': (7, 6), 'P2-2.5': (7, 7), 'P2-2.6': (7, 7), 'P2-2.7': (7, 7), 'P2-2.8': (7, 7)}),
}
FORMATO_PREVALECE = {'L1-R99': 'PC'}     # T96_reconciliacao, seção 3 (D-T96-ONDA2-ACEITE: os registros da seção 3 prevalecem sobre o mapa)
LOG = []


def falha(msg):
    raise SystemExit('REFORCO_V110: ' + msg)


def texto(rel, sha):
    raw = open(P(rel), 'rb').read()
    h = hashlib.sha256(raw.replace(b'\r\n', b'\n')).hexdigest()
    if h != sha:
        falha('%s: SHA-256 (LF) %s != aceito %s' % (rel, h, sha))
    return raw.decode('utf-8').replace('\r\n', '\n')


def entre(t, ini, fim):
    a = t.index(ini)
    b = t.index(fim, a)
    return t[a + len(ini):b]


def mapa(p1, lote):
    """1ª linha de tabela de cada id na Parte 1 (o mapa dos itens novos): id -> colunas."""
    m = collections.OrderedDict()
    for l in p1.split('\n'):
        mm = re.match(r'^\| (%s-R\d{2,3}) \| (.*)\|$' % lote, l)
        if mm and mm.group(1) not in m:
            m[mm.group(1)] = [c.strip() for c in mm.group(2).split('|')]
    return m


def vol_mapa(c):
    v = c[4].strip().lower()
    if v.startswith('n'):
        return False
    if v.startswith('s'):
        return True
    falha('coluna VOLÁTIL ilegível: %r' % c[4])


def parse_gce(lote, t, rel):
    p1 = entre(t, 'PARTE 1/3', 'FIM DA PARTE 1/3')
    p2 = entre(t, 'PARTE 2/3', 'FIM DA PARTE 2/3')
    p3 = entre(t, 'PARTE 3/3', 'FIM DA PARTE 3/3')
    L2 = p2.split('\n'); itens = collections.OrderedDict()
    for k, l in enumerate(L2):
        m = re.match(r'^(%s-R\d{2,3})\. (.*)$' % lote, l)
        if m:
            if m.group(2) != 'Julgue o item.':
                falha('%s: comando %r' % (m.group(1), m.group(2)))
            en = L2[k + 1]
            if not en.strip() or L2[k + 2].strip():
                falha('%s: enunciado não é uma linha única' % m.group(1))
            if m.group(1) in itens:
                falha('%s: id repetido na Parte 2' % m.group(1))
            itens[m.group(1)] = dict(comando=m.group(2), enunciado=en)
    L3 = p3.split('\n'); vistos = []
    for k, l in enumerate(L3):
        m = re.match(r'^(%s-R\d{2,3})\. ([CE])( \[TS\])?( \(espelho\))?\. (.+)$' % lote, l)
        if m:
            iid = m.group(1)
            if iid not in itens or iid in vistos:
                falha('%s: id da Parte 3 ausente da Parte 2 ou repetido' % iid)
            vistos.append(iid)
            bloco = []
            j = k + 1
            while j < len(L3) and L3[j].strip():
                bloco.append(L3[j]); j += 1
            if not any(b.startswith('Base: ') for b in bloco):
                falha('%s: bloco do gabarito sem linha "Base:"' % iid)
            itens[iid].update(gab=m.group(2), ts=bool(m.group(3)), espelho=bool(m.group(4)), just1=m.group(5), resto=bloco)
        elif re.match(r'^%s-R\d' % lote, l):
            falha('linha de cabeçalho fora do formato na Parte 3 de %s: %r' % (rel, l[:60]))
    if vistos != list(itens):
        falha('%s: ids da Parte 3 (%d) != Parte 2 (%d), ou outra ordem' % (rel, len(vistos), len(itens)))
    mp = mapa(p1, lote)
    for iid, d in itens.items():
        if iid not in mp:
            falha('%s: fora do mapa' % iid)
        c = mp[iid]
        d['folha'], d['ponto'], d['formato'] = c[0], c[1], c[2]
        d['vol_mapa'] = vol_mapa(c)
        d['parcial_mapa'] = (len(c) > 5 and c[5].upper().startswith('PARCIAL'))
    return itens


def parse_l6b(t):
    p1 = entre(t, '## PARTE 1/3 — Mapa', 'FIM DA PARTE 1/3')
    p2 = entre(t, '## PARTE 2/3 — (d) Itens do estudante', 'FIM DA PARTE 2/3')
    p3 = entre(t, '## PARTE 3/3 — (d-G) Gabarito comentado', 'FIM DA PARTE 3/3')
    L2 = [l for l in p2.split('\n') if l.strip()]
    if len(L2) != 4:
        falha('L6B: Parte 2 com %d linhas (esperado 4)' % len(L2))
    itens = collections.OrderedDict()
    for k in (0, 2):
        m = re.match(r'^(L6B-R0[12]) \((P1-4\.3)\)\. AUTORAL\. (.+)$', L2[k])
        if not m:
            falha('L6B: Parte 2 fora do formato: %r' % L2[k][:60])
        itens[m.group(1)] = dict(comando=m.group(3), enunciado=L2[k + 1], folha=m.group(2))
    mp = mapa(p1, 'L6B')
    for iid, d in itens.items():
        g = re.search(r'^### %s — Gabarito: ([CE])\nJustificativa \(duas linhas\): (.+)\n\[TS\]: (sim|não)[^\n]*\nVOLÁTIL: (sim|não)' % iid, p3, re.M)
        if not g:
            falha('%s: gabarito fora do formato' % iid)
        c = mp[iid]
        if c[0] != d['folha']:
            falha('%s: folha do mapa %s' % (iid, c[0]))
        d.update(gab=g.group(1), just1=g.group(2), ts=(g.group(3) == 'sim'), espelho=False, resto=[], ponto=c[1], formato=c[2],
                 vol_mapa=vol_mapa(c), parcial_mapa=False)
        if (g.group(4) == 'sim') != d['vol_mapa']:
            falha('%s: VOLÁTIL do (d-G) != mapa' % iid)
    return itens


def num(iid):
    return int(iid.split('-R')[1])


def carrega():
    """(itens_pacote, meta): lista de dicts de item na ordem dos atos e metadados por id."""
    itens, meta = [], collections.OrderedDict()
    for gk, g in G.items():
        A = ACEITE[gk]; lote = g['lote']; d = collections.OrderedDict()
        for rel, sha, sufixos in g['arquivos']:
            t = texto(rel, sha)
            if not t.rstrip().endswith('FIM DO LOTE'):
                falha('%s: sem FIM DO LOTE' % rel)
            x = parse_l6b(t) if lote == 'L6B' else parse_gce(lote, t, rel)
            esp = ['%s-%s' % (lote, s) for s in sufixos]
            if list(x) != esp:
                falha('%s: ids %s… != esperados %s…' % (rel, list(x)[:3], esp[:3]))
            for iid, v in x.items():
                v['arquivo'] = rel
                d[iid] = v
        if len(d) != A['n']:
            falha('%s: %d itens != %d' % (gk, len(d), A['n']))
        cg = collections.Counter(v['gab'] for v in d.values())
        if (cg['C'], cg['E']) != (A['C'], A['E']):
            falha('%s: C/E %s' % (gk, dict(cg)))
        ts = [k.split('-')[1] for k, v in d.items() if v['ts']]
        if ('ts' in A and ts != A['ts']) or ('nts' in A and len(ts) != A['nts']):
            falha('%s: [TS] %d %s' % (gk, len(ts), ts[:5]))
        if 'gab' in A and {k.split('-')[1]: v['gab'] for k, v in d.items()} != A['gab']:
            falha('%s: gabaritos' % gk)
        pf = collections.defaultdict(lambda: [0, 0])
        for iid, v in d.items():
            r = iid.split('-')[1]
            if lote in ('L1', 'L2') and num(iid) <= 130:
                esp = folha_por_faixa(lote[1], num(iid))
                if v['folha'] != esp:
                    falha('%s: folha %s != %s (faixa da reconciliação)' % (iid, v['folha'], esp))
            vol = r in A['vol']; par = r in A['parcial']
            if v['vol_mapa'] != vol:
                falha('%s: VOLÁTIL (mapa %s, aceite %s)' % (iid, v['vol_mapa'], vol))
            if v['parcial_mapa'] != par:
                falha('%s: aderência parcial (mapa %s, aceite %s)' % (iid, v['parcial_mapa'], par))
            v['volatil'] = vol; v['aderencia'] = 'parcial' if par else 'direta'
            if iid in FORMATO_PREVALECE:
                LOG.append('%s: formato %r do mapa -> %r (T96_reconciliacao, seção 3)' % (iid, v['formato'], FORMATO_PREVALECE[iid]))
                v['formato_mapa'] = v['formato']; v['formato'] = FORMATO_PREVALECE[iid]
            pf[v['folha']][0 if v['gab'] == 'C' else 1] += 1
        if {k: tuple(x) for k, x in pf.items()} != A['folha']:
            falha('%s: C/E por folha %s' % (gk, dict(pf)))
        for iid, v in d.items():
            it = collections.OrderedDict(id=iid, rotulo='AUTORAL', certame='Projeto Câmara 2026', cargo=g['cargo'], ano=2026, numero=num(iid),
                                         comando=v['comando'], textoBase='', enunciado=v['enunciado'], gabarito=v['gab'], justificativa=v['just1'],
                                         itemEdital=v['folha'], aderencia=v['aderencia'], url=v['arquivo'])
            if v['volatil']:
                it['volatil'] = True
            if not it['itemEdital'].startswith(g['prova'] + '-'):
                falha('%s: itemEdital %s fora de %s' % (iid, it['itemEdital'], g['prova']))
            itens.append(it)
            meta[iid] = dict(grupo=gk, ato=g['ato'], lote=lote, arquivo=v['arquivo'], folha=v['folha'], gab=v['gab'], ts=v['ts'], espelho=v['espelho'],
                             volatil=v['volatil'], aderencia=v['aderencia'], formato=v['formato'], ponto=v['ponto'], just1=v['just1'])
    if ACEITE_L2_R131 is not None:
        falha('ACEITE_L2_R131 preenchido: implementar a leitura do arquivo final aceito antes da geração final (T-105)')
    if len(itens) != 225:
        falha('total %d != 225' % len(itens))
    return itens, meta


if __name__ == '__main__':
    its, mt = carrega()
    c = collections.Counter(i['gabarito'] for i in its)
    print(len(its), dict(c), 'TS', sum(m['ts'] for m in mt.values()), 'vol', sum(m['volatil'] for m in mt.values()),
          'parcial', sum(m['aderencia'] == 'parcial' for m in mt.values()))
    print(LOG)
