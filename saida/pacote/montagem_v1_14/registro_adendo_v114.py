# registro_adendo_v114.py — T-123 fase 2 (script 7) — 2026-10-23 — gerado por gbq-csc
# -*- coding: utf-8 -*-
"""Gera out/registro_adendo6.md, o texto do adendo 6 ao registro AUTORAL da GBQ (v3 + adendos 1 a 5 intactos): os 238 itens de reforço de DA (D1 da GBQ, seção 5, "Adendo 6").
Conteúdo: fontes (8 levas, SHA-256 LF, ato e linha), ids por lote e por leva (vagos D1-R03 e D4-R12), totais por lote, erratas (3 aplicadas, 2 sem aceite), os 35 parciais, restrições de montagem (remissões às
seções de notas de simulado de cada reconciliação, com a lista literal dos pares das notas obrigatórias extraída por script), núcleo do reforço (18 ids), itens por folha, qualificação "lote D<n>" (scan_q = 0)
e registro GBQ vigente. Não reproduz enunciados. Lê as levas, as reconciliações e out/pacote*.json. Formato do adendo 5. Uso: python -I registro_adendo_v114.py. Não lê relógio."""
import sys
sys.dont_write_bytecode = True
import collections, glob, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import montar_v1_14 as M
import nucleo_v114 as NU

DATA = '2026-10-23'
D1_ARQ = 'saida/pacote/T123_D1_v1_14_2026-10-23.md'
ESP_LEVA = {1: (30, 15, 15, 16, 8), 2: (30, 17, 13, 13, 2), 3: (30, 16, 14, 14, 11), 4: (28, 15, 13, 13, 5), 5: (30, 16, 14, 14, 0), 6: (30, 14, 16, 15, 0), 7: (30, 15, 15, 13, 8), 8: (30, 14, 16, 16, 1)}
ESP_LOTE = {'D1': (12, 6, 6, 0), 'D2': (80, 40, 40, 0), 'D3': (89, 49, 40, 34), 'D4': (57, 27, 30, 1)}   # n, C, E, parciais (os [TS] por lote são conferidos pela soma por leva)
PARCIAIS_ESP = ['D3-R01', 'D3-R04', 'D3-R06', 'D3-R08', 'D3-R09', 'D3-R10', 'D3-R12', 'D3-R13', 'D3-R18', 'D3-R20', 'D3-R22', 'D3-R23', 'D3-R24', 'D3-R25', 'D3-R31', 'D3-R36', 'D3-R37', 'D3-R42', 'D3-R44', 'D3-R46', 'D3-R48',
                'D3-R52', 'D3-R53', 'D3-R56', 'D3-R57', 'D3-R58', 'D3-R70', 'D3-R72', 'D3-R73', 'D3-R75', 'D3-R76', 'D3-R77', 'D3-R78', 'D3-R79', 'D4-R44']
SEM_ACEITE = [('AJ-L8-E3', 'D4-R42'), ('AJ-L8-E4', 'D4-R52')]
RX_HDR = re.compile(r'^\*\*(D[1-6]-R\d{2})\*\* \(folha')
FALHAS = []


def falha(m):
    FALHAS.append(m); print('FALHA:', m)


def faixa(ids):
    ns = sorted(int(x.split('-R')[1]) for x in ids)
    return 'R%02d a R%02d' % (ns[0], ns[-1])


def parse_leva(b):
    """{id: dict(ts, vol, rev, qa)} pelas linhas de cabeçalho e 'Marcas:' da seção 2 de uma leva."""
    L = b.decode('utf-8').split('\n')
    out = collections.OrderedDict(); cur = None
    for l in L:
        m = RX_HDR.match(l)
        if m:
            cur = m.group(1); out[cur] = dict(ts='[TS]' in l, vol=False, rev=False, qa='QA PENDENTE' in l, ts_marca=False)
            continue
        if cur and l.startswith('- Marcas:'):
            out[cur].update(vol='VOLÁTIL=sim' in l, rev='REVERIFICAR=sim' in l, ts_marca='TS=sim' in l)
            cur = None
    return out


def notas_obrigatorias(n):
    """linhas de 'OBRIGATÓRIA' da seção de notas de simulado da reconciliação da leva n: [(código, itens-literal, obrigatórios, arquivo, seção)]."""
    f = glob.glob(os.path.join(M.R, 'saida', 'gcb', 'DA_reforco_leva%d_reconciliacao_*.md' % n))
    assert len(f) == 1, f
    t = open(f[0], 'rb').read().replace(b'\r\n', b'\n').decode('utf-8')
    m = re.search(r'^## (\d+)\. Notas de simulado[^\n]*\n', t, re.M)
    e = re.search(r'^## ', t[m.end():], re.M)
    sec = t[m.start():m.end() + (e.start() if e else len(t))]
    out = []
    for l in sec.split('\n'):
        if l.startswith('|') and re.search(r'OBRIGAT', l):
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            cod = re.match(r'\((\w+)\)', c[0]).group(1)
            segs = [s.strip() for s in c[1].split(';')]
            obrig = [s for s in segs if '(obrigat' in s.lower()] or ([c[1]] if len(segs) == 1 else [])
            out.append((cod, c[1], obrig, os.path.relpath(f[0], M.R).replace(os.sep, '/'), m.group(1)))
    return out, os.path.relpath(f[0], M.R).replace(os.sep, '/'), m.group(1), M.sha(open(f[0], 'rb').read().replace(b'\r\n', b'\n'))


def main():
    ins = M.ler_insumos()
    ctx = M.carregar(ins)
    pac = json.loads(open(os.path.join(M.OUT, 'pacote.json'), 'rb').read().decode('utf-8'))
    est = json.loads(open(os.path.join(M.OUT, 'pacote_estudante.json'), 'rb').read().decode('utf-8'))
    bruto = ctx['bruto']; by = {b['id']: b for b in bruto}
    ref = {i['id']: i for i in pac['itens'] if i['id'] in by}
    if [i['id'] for i in pac['itens'] if i['id'] in by] != [b['id'] for b in bruto]:
        falha('ordem do reforco no pacote difere da ordem das levas')
    sl = M.shas_levas(ctx['dec'])
    marcas = {n: parse_leva(ins['leva%d' % n]) for n in range(1, 9)}
    for n in range(1, 9):
        ids_n = [b['id'] for b in bruto if b['leva'] == n]
        if list(marcas[n]) != ids_n:
            falha('leva %d: ids da secao 2 diferem dos da secao 1' % n)
        if any(v['ts'] != v['ts_marca'] for v in marcas[n].values()):
            falha('leva %d: [TS] do cabecalho difere de TS=sim' % n)
    allm = {k: v for n in marcas for k, v in marcas[n].items()}
    vol = [k for k, v in allm.items() if v['vol']]; rev = [k for k, v in allm.items() if v['rev']]
    if vol or rev or any(i.get('volatil') for i in ref.values()):
        falha('VOLATIL/REVERIFICAR no reforco: %s %s' % (vol, rev))
    parciais = [b['id'] for b in bruto if b['aderencia'] == 'parcial']
    if sorted(parciais) != sorted(PARCIAIS_ESP):
        falha('parciais difere da D1: %s' % parciais)
    leva_de = {b['id']: b['leva'] for b in bruto}
    # núcleo do reforço (do pacote do estudante)
    nuc = [i['id'] for i in est['itens'] if i['id'] in by and i['nucleo']]
    if sorted(nuc) != sorted(M.NUC18):
        falha('nucleo do reforco difere da D1: %s' % nuc)
    L = []; w = L.append
    w('# claude_GBQ_Registro_AUTORAL_v3_adendo6_%s.md — T-123 — %s — gerado por gbq-csc (registro_adendo_v114.py)' % (DATA, DATA))
    w('# GBQ — REGISTRO DE ITENS AUTORAL — v3, ADENDO 6: Direito Administrativo (P1-DA), reforço D-REFORCO-DA, 238 itens (%s)' % DATA)
    w('Texto do adendo 6 ao registro v3 e aos adendos 1 a 5 (intactos). Base: a decisão de forma da GBQ para a T-123 (%s), seção 5 (Adendo 6), e a errata de forma v1.2.12 do contrato (saida/pacote/contrato_v1_2_12_2026-10-23.md). Pacote v1.14 (out/pacote.json): os 238 itens D<n>-R<nn> estão nas 46 entradas de edital P1-DA, depois dos 410 itens dos lotes e dos 142 itens de banco. Não reproduz enunciados: os textos estão nos arquivos das levas.' % D1_ARQ)
    w('')
    w('## 1. Fontes (arquivo final de cada leva, SHA-256 do conteúdo LF, ato, linha em DECISOES.md)')
    w('| Leva | Arquivo final | Ids (ordem da seção 1) | n | SHA-256 do arquivo (LF) | Bytes | Linhas | Ato (linha; data) | Reconciliação (SHA-256 LF) |')
    w('|--:|---|---|--:|---|--:|--:|---|---|')
    for n in range(1, 9):
        ids = [b['id'] for b in bruto if b['leva'] == n]
        b = ins['leva%d' % n]
        if M.sha(b) != sl[n]:
            falha('SHA-256 da leva %d' % n)
        ch = 'LEVA%d' % n
        ato, ln, dt = NU.TABELA[ch]
        ato_txt = '%s (%d; %s)' % (ato, ln, dt)
        if n == 7:
            ato_txt += '; D3-R75 pelo aceite próprio: %s (%d; %s)' % (NU.TABELA['D3-R75'][0], NU.TABELA['D3-R75'][1], NU.TABELA['D3-R75'][2])
        rec = notas_obrigatorias(n)
        w('| %d | saida/gcb/DA_reforco_leva%d_v2.md | %s | %d | %s | %d | %d | %s | %s (%s) |' % (n, n, ', '.join(ids), len(ids), M.sha(b), len(b), b.count(b'\n'), ato_txt, rec[1], rec[3]))
    w('')
    w('As erratas AJ-E1, AJ-L2-E1 e AJ-L7-E1 entram por substituição exata na leitura (seção 4); o arquivo de cada leva não muda. A limpeza das marcas de produção nas justificativas (85 itens, 91 substituições) está em `saida/gcb/DA_plataforma/DA_reforco_substituicoes.csv` (SHA-256 LF `%s`) e `saida/gcb/DA_plataforma/DA_reforco_registro_formato.md` (SHA-256 LF `%s`), aceitas pela reconciliação `saida/gcb/T123_limpeza_reconciliacao_GCB_2026-10-23.md`; o registro por id está em `saida/pacote/montagem_v1_14/out/registro_alteracoes_v1_14.csv`.' % (M.sha(ins['csv']), M.sha(ins['registro'])))
    w('')
    w('## 2. Ids por lote e por leva')
    w('Os ids vagos D1-R03 e D4-R12 não são reutilizados e não estão no pacote.')
    por_lote = collections.OrderedDict()
    for lt in ('D1', 'D2', 'D3', 'D4'):
        por_lote[lt] = [b['id'] for b in bruto if b['lote'] == lt]
    vagos = []
    for lt, ids in por_lote.items():
        ns = sorted(int(x.split('-R')[1]) for x in ids)
        ausentes = ['%s-R%02d' % (lt, k) for k in range(1, ns[-1] + 1) if k not in ns]
        vagos += ausentes
        w('- lote %s: %s-R%02d a %s-R%02d (%d itens)%s.' % (lt, lt, ns[0], lt, ns[-1], len(ids), ('; vago: ' + ', '.join(ausentes)) if ausentes else ''))
    if vagos != ['D1-R03', 'D4-R12']:
        falha('vagos %s' % vagos)
    w('')
    w('Por leva (ordem da seção 1 de cada arquivo):')
    for n in range(1, 9):
        w('- leva %d: %s.' % (n, ', '.join(b['id'] for b in bruto if b['leva'] == n)))
    w('')
    w('## 3. Totais por lote')
    w('| Lote | n | C | E | [TS] | VOLÁTEIS | PARCIAIS | Aptos a final (direta e não VOLÁTIL) |')
    w('|---|--:|--:|--:|--:|--:|--:|--:|')
    tot = collections.Counter()
    for lt, ids in por_lote.items():
        c = sum(by[x]['gabarito'] == 'C' for x in ids); e = len(ids) - c; ts = sum(allm[x]['ts'] for x in ids)
        pa = sum(by[x]['aderencia'] == 'parcial' for x in ids)
        if (len(ids), c, e, pa) != ESP_LOTE[lt]:
            falha('totais do lote %s: %s' % (lt, (len(ids), c, e, pa)))
        w('| lote %s | %d | %d | %d | %d | 0 | %d | %d |' % (lt, len(ids), c, e, ts, pa, len(ids) - pa))
        tot.update(n=len(ids), c=c, e=e, ts=ts, pa=pa, ap=len(ids) - pa)
    w('| Total | %d | %d | %d | %d | 0 | %d | %d |' % (tot['n'], tot['c'], tot['e'], tot['ts'], tot['pa'], tot['ap']))
    w('')
    w('Por leva (n, C, E, [TS], PARCIAIS): ' + '; '.join('leva %d: %d, %d, %d, %d, %d' % ((n,) + tuple(ESP_LEVA[n])) for n in range(1, 9)) + '.')
    for n in range(1, 9):
        ids = [b['id'] for b in bruto if b['leva'] == n]
        obt = (len(ids), sum(by[x]['gabarito'] == 'C' for x in ids), sum(by[x]['gabarito'] == 'E' for x in ids), sum(allm[x]['ts'] for x in ids), sum(by[x]['aderencia'] == 'parcial' for x in ids))
        if obt != ESP_LEVA[n]:
            falha('totais da leva %d: %s' % (n, obt))
    w('')
    w('Os 238 itens são AUTORAL. Nenhum é VOLÁTIL, nenhum é REVERIFICAR (VOLÁTEIS novos: 0; REVERIFICAR novos: 0); os 5 VOLÁTEIS de DA da v1.13 (D2-01, D2-28, D6-09, D6-32 e D6-34) não mudam. Aptos a simulado final: %d (direta e não volátil). Parciais: %d (seção 5).' % (tot['ap'], tot['pa']))
    w('')
    w('## 4. Erratas')
    w('- Aplicadas na leitura, por substituição exata (o "antes" ocorre 1 vez na seção indicada e 1 vez no arquivo; o "depois" 0 vez): ' + '; '.join('%s no %s (%s)' % (a.split(' ')[0], i, a[a.index('(') + 1:-1]) for (i, a, c, an, de) in M.ERRATAS) + '. O texto literal está em `out/registro_alteracoes_v1_14.csv` (tipo `errata`).')
    w('- Sem aceite, não aplicadas: ' + '; '.join('%s (%s)' % x for x in SEM_ACEITE) + ' (D-T116-LEVA8-ACEITE, III). O D4-R42 e o D4-R52 entram como aprovados no R2.')
    w('')
    w('## 5. Parciais (aderência parcial; só simulado diagnóstico, D-ADERENCIA): %d ids' % len(parciais))
    w('- ' + ', '.join(parciais) + '.')
    w('- Por folha: ' + '; '.join('%s %d' % kv for kv in sorted(collections.Counter(by[x]['itemEdital'] for x in parciais).items(), key=lambda kv: [int(p) for p in kv[0].replace('P1-DA-', '').split('.')])) + '.')
    w('')
    w('## 6. Restrições de montagem (remissões; o texto das notas está nas reconciliações)')
    w('As notas de simulado "não pôr no mesmo simulado" e as restrições de uso de cada leva ficam na seção de notas de simulado da reconciliação da GCB correspondente (seção 5 nas levas 1 a 7; seção 7 na leva 8), com continuidade entre as levas. Valem na montagem de simulados (T-119):')
    for n in range(1, 9):
        rec = notas_obrigatorias(n)
        w('- leva %d: %s, seção %s.' % (n, rec[1], rec[2]))
    w('')
    w('Notas OBRIGATÓRIAS (par indicado), lista literal extraída por script das reconciliações (o item da esquerda do par não entra no mesmo simulado que o item da direita):')
    w('| Nota | Leva | Itens (literal) | Pares obrigatórios |')
    w('|---|--:|---|---|')
    obrig_all = []
    for n in range(1, 9):
        for (cod, itens, ob, arq, sec) in notas_obrigatorias(n)[0]:
            obrig_all.append(cod)
            w('| (%s) | %d | %s | %s |' % (cod, n, itens, '; '.join(ob)))
    if sorted(obrig_all) != sorted(['af', 'ay', 'bw', 'ci', 'cl', 'db']):
        falha('notas obrigatorias: %s' % obrig_all)
    w('')
    w('- As notas comuns (não obrigatórias) e as de teto por simulado (moldura, "no máximo 2 por simulado") ficam nas seções citadas.')
    w('- Nenhum dos 684 itens de DA entra em `simulados` nesta versão; o diagnóstico de 30 itens de DA (D-DIAG30-DA) é o único uso, fora de `simulados`. Os 238 só vão a simulado depois do aceite da v1.14 (D-QA-PENDENTE).')
    w('- Os 35 parciais só em simulado diagnóstico (D-ADERENCIA). Os 5 VOLÁTEIS da v1.13 nunca antes da reverificação de 4–8/1/2027.')
    w('')
    w('## 7. Núcleo do reforço (`nucleo` true no pacote do estudante): %d ids' % len(nuc))
    w('- ' + ', '.join(nuc) + '.')
    w('- Critério: k1 (data do ato), k2 (linha do ato em DECISOES.md), k3 ("direta" antes de "parcial"), k4 (posição em `itens`), com os 10 primeiros por itemEdital (decisão de forma da T-123, seção 6). Os 36 itens de banco P1-DA são todos núcleo; 12 itens da v1.13 passam a não núcleo (D1-07, D1-08, D3-79, D3-80, D6-07 a D6-10 e D6-37 a D6-40).')
    w('')
    w('## 8. Itens de reforço por folha (ids; na ordem do edital)')
    ed = [e['id'] for e in pac['edital'] if e['id'].startswith('P1-DA-')]
    tot_f = 0
    for f_ in ed:
        ids = [b['id'] for b in bruto if b['itemEdital'] == f_]
        if ids:
            tot_f += len(ids); w('- %s (%d): %s' % (f_, len(ids), ', '.join(ids)))
    if tot_f != 238:
        falha('itens por folha somam %d' % tot_f)
    w('')
    w('## 9. Regra de qualificação "lote D<n>"')
    w('- Os ids de lote D<n> (1 a 5) coincidem com os ids das discursivas D<n>; o id é único por lista (`lotes[].id` × `discursivas[].id`), e nenhum id novo repete o da outra lista. Fora da plataforma o id de lote vai sempre qualificado como "lote D<n>" (e "discursiva D<n>"); ids de item como D3-R13 não contam. Na edição .md do estudante, os arquivos se chamam DA_D<n>_estudo.md, DA_D<n>_itens.md e DA_D<n>_gabarito.md.')
    w('- Os ids D<n>-R<nn> de reforço de DA não mudam o registro de ids da edição .md: os itens de reforço de DA ficam ao fim de DA_D<n>_itens.md e DA_D<n>_gabarito.md, na seção "Itens de reforço" (decisão de forma da T-123, seção 10).')
    w('')
    w('## 10. Registro GBQ vigente')
    w('- Registro v3 + adendos 1 a 6. Este adendo 6 só entra em saida/gbq/ depois do aceite da v1.14 (promoção pelo orquestrador: `saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo6_%s.md`).' % DATA)
    txt = '\n'.join(L) + '\n'
    # scan_q: "D<n>" (1 a 6) isolado que não seja precedido de "lote " (ids de item com hífen e nomes de arquivo com "_" não contam)
    scan_q = [(m.group(0), txt[max(0, m.start() - 12):m.end() + 6]) for m in re.finditer(r'(?<![\w-])D[1-6](?![\w-])', txt) if txt[max(0, m.start() - 5):m.start()] != 'lote ']
    if scan_q:
        falha('scan_q = %d: %r' % (len(scan_q), scan_q[:5]))
    M.grava(os.path.join(M.OUT, 'registro_adendo6.md'), txt.encode('utf-8'))
    print('registro_adendo6.md: %d linhas; %d bytes; SHA-256 %s; scan_q = %d; %d FALHA' % (len(L), len(txt.encode('utf-8')), M.sha(txt.encode('utf-8')), len(scan_q), len(FALHAS)))
    sys.exit(1 if FALHAS else 0)


if __name__ == '__main__':
    main()
