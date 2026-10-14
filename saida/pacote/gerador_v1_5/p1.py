# -*- coding: utf-8 -*-
"""Constrói lotes e itens AUTORAL de P1 (Lotes 4, 4-C, 5, 5-C, 6a, 6b)."""
import re
from common import *
from gce import trim_blank, text_block
from registry import REG

P1_IDS = {'P1-1', 'P1-2', 'P1-2.1', 'P1-3', 'P1-4', 'P1-4.1', 'P1-4.2', 'P1-4.3',
          'P1-5', 'P1-5.1', 'P1-5.2', 'P1-5.3', 'P1-6', 'P1-7', 'P1-7.1', 'P1-8', 'P1-8.1', 'P1-8.2', 'P1-8.3', 'P1-8.4'}


def to_edital(sub):
    cand = 'P1-' + sub
    if cand in P1_IDS:
        return cand
    return 'P1-' + sub.split('.')[0]


LOTES = [
    dict(id='L4', file='saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md', nome='Lote 4 — TID-IA (P1 5.1–5.3 e 6)', cargo='Lote 4',
         idrx=r'\d+', fmt=lambda n: 'L4-%02d' % n, reg='Lote 4', full=True),
    dict(id='L4C', file='saida/gcb/GCB_Lote4C_v1_GCB-CPP.md', nome='Lote 4-C — TID-IA, complemento (P1 5.1)', cargo='Lote 4-C',
         idrx=r'4C-\d\d', fmt=lambda n: '4C-%02d' % n, reg='Lote 4-C', full=False),
    dict(id='L5', file='saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md', nome='Lote 5 — TID-DADOS-VIZ (P1 7.1 e 8.1–8.4)', cargo='Lote 5',
         idrx=r'A5-\d\d', fmt=lambda n: 'A5-%02d' % n, reg='Lote 5', full=True),
    dict(id='L5C', file='saida/gcb/GCB_Lote5C_v1_GCB-CPP.md', nome='Lote 5-C — TID-DADOS-VIZ, complemento (P1 8.2 e 8.4)', cargo='Lote 5-C',
         idrx=r'5C-\d\d', fmt=lambda n: '5C-%02d' % n, reg='Lote 5-C', full=False),
    dict(id='L6A', file='saida/gcb/GCB_Lote6a_v2_producao_auto.md', nome='Lote 6a — TI-FERRAMENTAS (P1 itens 1 e 3: MSOffice 365 e comunicação/colaboração)',
         cargo='Lote 6a', idrx=r'6A-\d\d', fmt=lambda n: '6A-%02d' % n, reg='Lote 6a', full=True),
    dict(id='L6B', file='saida/gcb/GCB_Lote6b_v2_producao_auto.md', nome='Lote 6b — TI-REDES-SEGURANCA (P1 itens 2 e 4: redes e segurança)',
         cargo='Lote 6b', idrx=r'6B-\d\d', fmt=lambda n: '6B-%02d' % n, reg='Lote 6b', full=True),
]


def curso_md_gcb(lines):
    out = []
    i = 0
    while i < len(lines):
        l = lines[i]
        if re.match(r'^-{20,}$', l) and i + 2 < len(lines) and re.match(r'^-{20,}$', lines[i + 2]) and lines[i + 1].startswith('ITEM '):
            out.append('## ' + lines[i + 1].strip())
            i += 3
            continue
        m = re.match(r'^(\d+(?:\.\d+){1,2}) ([A-ZÀ-Ú][A-ZÀ-Ú0-9 ()/,.:–—+×-]+)(\s*\(ITEM [\d.]+\))?$', l)
        if m and l.strip() == l:
            out.append('### ' + l.strip())
        else:
            out.append(l.rstrip())
        i += 1
    return '\n'.join(trim_blank(out))


def pegadinhas_gcb(curso_md, lid=None):
    """Pegadinhas do curso GCB, uma entrada por fragmento, com rótulo (F3, contrato v1.2 regra (d)).
    Retorna lista de dict(itemEdital, rotulo, texto) e registra PEG_INFO."""
    from edital_p import build_edital
    from peg import fragments, clean_title, GENERIC, PEG_INFO
    ED = build_edital()
    EID = {e['id']: e['texto'] for e in ED}
    L = curso_md.split('\n')
    raw = []          # (item_num, item_title, h3_title, plain_title, texto)
    item_num = item_title = None
    h3 = None
    plain = None
    i = 0
    while i < len(L):
        l = L[i]
        m = re.match(r'^## ITEM ([\d.]+) — (.*)$', l)
        if m:
            item_num, item_title = m.group(1), m.group(2)
            h3 = None; plain = None
            i += 1
            continue
        if l.startswith('### '):
            h3 = l[4:].strip(); plain = None
            # bloco de pegadinhas numeradas (P1., P2., ...)
            if 'PEGADINHAS PROVÁVEIS' in l:
                j = i + 1
                ents = []
                while j < len(L) and L[j].strip():
                    mp = re.match(r'^P\d+\.\s*(.*)$', L[j])
                    if mp:
                        ents.append(mp.group(1).strip())
                    else:
                        ents[-1] = ents[-1] + ' ' + L[j].strip()
                    j += 1
                for t in ents:
                    raw.append((item_num, item_title, h3, plain, t))
                i = j
                continue
            i += 1
            continue
        prev_blank = (i == 0) or (not L[i - 1].strip())
        nxt = L[i + 1] if i + 1 < len(L) else ''
        mm = re.match(r'^-\s*Pegadinha(?: provável)?:\s*(.*)$', l)
        if mm:
            raw.append((item_num, item_title, h3, plain, mm.group(1).strip()))
            i += 1
            continue
        if l.strip() == 'Pegadinha provável' and nxt.startswith('- '):
            assert not (i + 2 < len(L) and L[i + 2].startswith('- ')), 'mais de um marcador após Pegadinha provável'
            raw.append((item_num, item_title, h3, None, nxt[2:].strip()))
            plain = None
            i += 2
            continue
        if l.strip() and prev_blank and nxt.startswith('- ') and not l.startswith('-') and not GENERIC.match(l.strip()) \
                and l.strip() not in ('Pegadinha provável',) and not l.startswith('#'):
            plain = l.strip()
        elif l.strip() and GENERIC.match(l.strip()):
            plain = None
        i += 1
    out = []
    for item_num, item_title, h3t, plainb, t in raw:
        ie = to_edital(item_num)
        h3c = re.sub(r'^\d+(?:\.\d+)*\s+', '', h3t) if h3t else None
        if h3c and not GENERIC.match(h3c):
            rot = clean_title(h3t); origem = 'subseção'
        elif plainb:
            rot = clean_title(plainb); origem = 'bloco'
        elif ('P1-' + item_num) in EID:
            rot = EID['P1-' + item_num]; origem = 'edital'
        else:
            rot = clean_title(item_title); origem = 'item do lote'
        modo, frs = fragments(t)
        for f in frs:
            out.append(dict(itemEdital=ie, rotulo=rot, texto=f))
        PEG_INFO.append(dict(lote=lid, itemEdital=ie, rotulo=rot, origem=origem, modo=modo, n=len(frs), orig=t))
    return out


def pares_gcb(sec_lines):
    res = []
    for l in sec_lines:
        m = re.match(r'^C(\d+)\.\s+(.*)$', l)
        if not m:
            continue
        fields = [x.strip() for x in m.group(2).split(' | ')]
        name = fields[0]
        parts = [p.strip() for p in name.split(' × ')]
        a = parts[0]
        b = ' × '.join(parts[1:]) if len(parts) > 1 else ''
        if not b:
            LOG.append('PARES GCB: par sem " × ": %r' % name[:60])
        # T-57 / contrato v1.2.2 ponto 1 (D-T54-03): `id` = rótulo literal do par no canônico, sem o ponto ("C1"…"Cn"); primeira chave
        res.append(dict(id='C' + m.group(1), a=a, b=b, como=' | '.join(fields[1:])))
    return res


def split_dg_p1(txt):
    """'C — [TS] — v3 (R9) — 5.1 — TC (...). texto' -> (gab, ts, vol, sub, just)"""
    segs = txt.split(' — ')
    gab = segs[0].strip()
    if gab not in ('C', 'E'):
        raise SystemExit('d-G P1: gabarito não reconhecido: ' + txt[:60])
    ts = False
    vol = False
    sub = None
    for k in range(1, len(segs)):
        s = segs[k]
        if s.strip() == '[TS]':
            ts = True
            continue
        if s.strip() == 'VOLÁTIL':
            vol = True
            continue
        m = re.match(r'^(\d+(?:\.\d+)?)(?:\.\s+(.*))?$', s, re.S)
        if m:
            sub = m.group(1)
            rest = [m.group(2)] if m.group(2) else []
            rest += segs[k + 1:]
            return gab, ts, vol, sub, ' — '.join(rest).strip()
    raise SystemExit('d-G P1: subitem não encontrado: ' + txt[:80])


LEG_RX = re.compile(r'(Mecanismos?: .*?)\.(?: |$)')


def legenda_mecanismo(lines, arq):
    """T-56 / v1.2.1 ponto 4: legenda das etiquetas de mecanismo (TC, GI, AT, IC) do arquivo canônico do lote.
    Texto literal da linha que abre com "Legenda:", do rótulo "Mecanismo:" ou "Mecanismos:" (inclusive) até o fim da enumeração,
    sem o ponto final, sem edição e sem uniformizar as variantes entre lotes. Retorna None se o arquivo não tiver a legenda."""
    achados = []
    for l in lines:
        if l.startswith('Legenda:'):
            m = LEG_RX.search(l)
            if m:
                achados.append(m.group(1))
    if not achados:
        return None
    assert len(achados) == 1, (arq, 'mais de uma legenda de mecanismo', achados)
    return achados[0]


def build_lote_p1(spec):
    lid = spec['id']
    lines = read(spec['file']).split('\n')
    out = dict(id=lid, nome=spec['nome'], prova='P1')
    out['legendaMecanismo'] = legenda_mecanismo(lines, spec['file'])
    if spec['full']:
        a0 = find_idx(lines, lambda l: l.startswith('PARTE 1/3 — (a) CURSO'))
        a0 = find_idx(lines, lambda l: l.startswith('====='), a0) + 1
        a1 = find_idx(lines, lambda l: l.startswith('FIM DA PARTE 1/3'))
        curso = curso_md_gcb(lines[a0:a1])
        out['curso'] = curso
        out['pegadinhas'] = pegadinhas_gcb(curso, lid)
        b0 = find_idx(lines, lambda l: l.startswith('(b) RESUMO'))
        c0 = find_idx(lines, lambda l: l.startswith('(c) PARES'))
        e2 = find_idx(lines, lambda l: l.startswith('FIM DA PARTE 2/3'))
        out['resumo'] = text_block(lines[b0 + 1:c0])
        out['pares'] = pares_gcb(lines[c0 + 1:e2])
    else:
        out['curso'] = ''
        out['resumo'] = ''
        out['pares'] = []
        out['pegadinhas'] = []
    d0 = find_idx(lines, lambda l: l.startswith('(d) VERSÃO'))
    dg0 = find_idx(lines, lambda l: l.startswith('(d-G) GABARITO'))
    # itens: linhas "ID. texto"; comando = última linha não-item anterior (não vazia)
    items = []
    cmd = None
    idrx = spec['idrx']
    for l in lines[d0 + 1:dg0]:
        if not l.strip() or l.startswith('====='):
            continue
        m = re.match(r'^(' + idrx + r')\.\s+(.*)$', l)
        if m:
            items.append((m.group(1), m.group(2).strip(), cmd))
        else:
            cmd = l.strip()
    dg = {}
    end = find_idx(lines, lambda l: l.startswith('Nota de produção') or l.startswith('REGISTRO DE ACATAMENTO') or l.startswith('FIM DA PARTE 3/3') or l.startswith('FIM DO LOTE'), dg0 + 1)
    for l in lines[dg0 + 1:end]:
        m = re.match(r'^(' + idrx + r')\.\s+(.*)$', l)
        if m:
            dg[m.group(1)] = m.group(2).strip()
    its = []
    for iid, txt, cm in items:
        n = int(re.sub(r'\D', '', iid.split('-')[-1] if '-' in iid else iid))
        regid = spec['fmt'](n)
        gab, ts, vol, sub, just = split_dg_p1(dg[iid])
        marca = ''
        if spec['reg']:
            r = REG[spec['reg']][regid]
            assert r['gab'] == gab, (regid, r['gab'], gab)
            assert r['sub'] == sub, (regid, r['sub'], sub)
            assert r['ts'] == ts, (regid, 'TS')
            volreg = 'VOLÁTIL' in r['marca']
            assert volreg == vol, (regid, 'VOL', volreg, vol)
            marca = r['marca']
        its.append(dict(local=iid, regid=regid, enunciado=txt, gabarito=gab, justificativa=just, sub=sub, volatil=vol,
                        comando=cm, numero=n, ts=ts, marca=marca))
    out['_items'] = its
    out['itensEdital'] = sorted({to_edital(i['sub']) for i in its}, key=lambda s: [int(x) for x in s[3:].split('.')])
    return out
