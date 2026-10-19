# -*- coding: utf-8 -*-
"""T-104 (v1.10) — validação do pacote.json v1.10 e do pacote_estudante.json v1.10-E (passo 4). Leitura própria dos arquivos finais (sem o parser de reforco_v110.py),
contagens transcritas das decisões de aceite, critério do "nucleo" recalculado com as linhas dos atos fixadas aqui (não lidas por nucleo.py).
verifica(P, E, P19, E19) devolve a lista de (id, ok, mensagem); conferencias_v110.py a reusa nos testes negativos por mutação.
Saídas: out/validate_v110.json e, pelo runner, out/validate_stdout.txt. Sai com código 1 se houver falha."""
import collections, copy, csv, hashlib, json, os, re, sys
from common import P as PATH, OUT
import refs, config_v110 as cfg

CHAVES = ['id', 'rotulo', 'certame', 'cargo', 'ano', 'numero', 'comando', 'textoBase', 'enunciado', 'gabarito', 'justificativa', 'itemEdital', 'aderencia', 'url']
ARQ = [('saida/gcb/L6B_reforco_onda1_saldo_v2.md', 'L6B', 2), ('saida/gce/L1_reforco_onda2_A_v3.md', 'L1', 27), ('saida/gce/L1_reforco_onda2_B_v2.md', 'L1', 28),
       ('saida/gce/L1_reforco_onda2_C_v2.md', 'L1', 28), ('saida/gce/L1_reforco_onda2_D_v3.md', 'L1', 28), ('saida/gce/L1_reforco_onda2_saldo_v2.md', 'L1', 1),
       ('saida/gce/L2_reforco_onda3_A_v3.md', 'L2', 28), ('saida/gce/L2_reforco_onda3_B_v3.md', 'L2', 27), ('saida/gce/L2_reforco_onda3_C_v3.md', 'L2', 28),
       ('saida/gce/L2_reforco_onda3_D_v3.md', 'L2', 28)] + ([('saida/gce/L2_reforco_onda3_saldo_v2.md', 'L2', 1)] if cfg.E_L2R131 else [])
VOL = set('L1-R%d' % k for k in (49, 54, 57, 65, 67, 69, 86, 87, 88, 110, 114)) | set('L2-R%d' % k for k in (24, 25, 37, 56, 57, 60, 61, 66, 77, 81, 82, 85, 94, 99, 100, 120, 121, 125))
PAR = set('L2-R%d' % k for k in (19, 21, 22, 25, 27, 28, 29, 31, 32, 35, 38, 39, 41, 42, 45, 46, 47, 50, 51, 52, 53, 54, 55, 58, 59, 60, 61, 63, 64, 65, 66, 69, 71, 73, 74,
                                   79, 84, 85, 91, 94, 101, 102, 130))
# folhas depois da v1.10 (decisões de aceite e reconciliações): itens e, nas 2.x, diretas (T97_reconciliacao, 3.1)
FOLHA_N = dict([('P2-1.%d' % k, 20) for k in range(1, 9)] + [('P2-2.%d' % k, 20) for k in range(1, 9)] + [('P2-2.4', 19 + cfg.E_L2R131), ('P1-4.3', 6)])
DIRETAS_2 = {'P2-2.1': 10, 'P2-2.2': 13, 'P2-2.3': 10, 'P2-2.4': 10 + cfg.E_L2R131, 'P2-2.5': 17, 'P2-2.6': 16, 'P2-2.7': 18, 'P2-2.8': 19}
LINHA_ATO = {'D-CANONICOS': 14, 'D-LOTE6A-CANONICO': 20, 'D-LOTE6B-CANONICO': 21, 'D-T92-R4-PARCIAL': 103, 'D-T89-R1-ACEITE': 104, 'D-T91-R3-ACEITE': 105,
             'D-T90-R2-ACEITE': 106, 'D-T102-R4-SALDO': 110, 'D-T96-ONDA2-ACEITE': 118, 'D-T103-SALDO-ACEITE': 119, 'D-T97-ONDA3-ACEITE': 121}
DEL_ESPERADAS = 80      # 20 V2 + 51 R2 + 9 C2 (reforco_marcas_v110.ESPERADO)


def leitura_propria():
    """{id: (comando, enunciado, gabarito, justificativa)} lidos dos arquivos finais por varredura de linhas, sem o parser do gerador."""
    out = collections.OrderedDict()
    for rel, lote, n in ARQ:
        L = open(PATH(rel), encoding='utf-8').read().replace('\r\n', '\n').split('\n')
        i2 = next(k for k, l in enumerate(L) if 'PARTE 2/3' in l); i3 = next(k for k, l in enumerate(L) if 'PARTE 3/3' in l)
        f3 = next(k for k, l in enumerate(L) if l.startswith('FIM DA PARTE 3/3'))
        ids = []
        for k in range(i2, i3):
            l = L[k]
            if lote == 'L6B' and l.startswith('L6B-R0'):
                iid = l[:7]; cmd = l.split('. AUTORAL. ', 1)[1]; out[iid] = [cmd, L[k + 1], None, None]; ids.append(iid)
            elif lote != 'L6B' and re.match(r'^%s-R\d+\. Julgue o item\.$' % lote, l):
                iid = l.split('.')[0]; out[iid] = ['Julgue o item.', L[k + 1], None, None]; ids.append(iid)
        for k in range(i3, f3):
            l = L[k]
            if lote == 'L6B' and l.startswith('### L6B-R0'):
                iid = l[4:11]; out[iid][2] = l[-1]; out[iid][3] = L[k + 1][len('Justificativa (duas linhas): '):]
            elif lote != 'L6B':
                for iid in ids:
                    if l.startswith(iid + '. ') and l[len(iid) + 2] in 'CE':
                        out[iid][2] = l[len(iid) + 2]
                        resto = l[len(iid) + 3:]
                        for pre in (' [TS] (espelho). ', ' [TS]. ', '. '):
                            if resto.startswith(pre):
                                out[iid][3] = resto[len(pre):]
                                break
        if len(ids) != n:
            raise SystemExit('leitura própria: %s com %d ids (esperado %d)' % (rel, len(ids), n))
    return out


def linha_decisao(d):
    for k, l in enumerate(open(PATH('DECISOES.md'), encoding='utf-8').read().split('\n'), 1):
        if l.startswith('APLICADA') and ('| %s |' % d) in l:
            return k
    raise SystemExit('decisão %s ausente de DECISOES.md' % d)


def chave_nucleo(it, pos, banco):
    iid = it['id']; pre = iid.split('-')[0]
    if pre == 'BQ':
        k1, k2 = banco[iid], 0
    elif '-R' not in iid:
        k1, k2 = '2026-10-09', LINHA_ATO['D-LOTE6A-CANONICO' if pre == '6A' else 'D-LOTE6B-CANONICO' if pre == '6B' else 'D-CANONICOS']
    else:
        n = int(iid.split('-R')[1])
        ato = {'L1': 'D-T89-R1-ACEITE' if n <= 18 else 'D-T103-SALDO-ACEITE' if n == 131 else 'D-T96-ONDA2-ACEITE', 'L2': 'D-T90-R2-ACEITE' if n <= 18 else cfg.ATO_L2R131 if n == 131 else 'D-T97-ONDA3-ACEITE',
               'L3': 'D-T91-R3-ACEITE', 'L6A': 'D-T92-R4-PARCIAL', 'L6B': 'D-T102-R4-SALDO'}[pre]
        k1, k2 = '2026-10-18', LINHA_ATO[ato] if ato in LINHA_ATO else linha_decisao(ato)
    return (k1, k2, it['aderencia'] != 'direta', pos)


def verifica(P, E, P19, E19, fontes=None, banco=None):
    R = []
    def ok(i, c, m): R.append((i, bool(c), m))
    it, it19 = P['itens'], P19['itens']
    # (A) base v1.9
    ok('A1', P['versao'] == 1 and P['nome'] == cfg.NOME and P['geradoEm'] == cfg.GERADO_EM, 'versao, nome e geradoEm da v1.10')
    ok('A2', list(P.keys()) == list(P19.keys()), 'chaves de topo iguais às da v1.9')
    NN = 559 + cfg.E_L2R131
    ok('A3', len(it) == NN and [i['id'] for i in it[:334]] == [i['id'] for i in it19], '%d itens; os 334' % NN + ' da v1.9 primeiro, na mesma ordem')
    dif = [a['id'] for a, b in zip(it[:334], it19) if a != b]
    ok('A4', dif == ['5C-08'], 'dos 334 da v1.9, só o 5C-08 muda (%s)' % dif)
    a, b = [i for i in it if i['id'] == '5C-08'][0], [i for i in it19 if i['id'] == '5C-08'][0]
    ok('A5', {k for k in a if a[k] != b[k]} == {'justificativa'} and b['justificativa'].replace('É o item deste lote mais próximo de um canônico (A5-20):', 'É, entre os itens 5C, o mais próximo do item A5-20:') == a['justificativa'],
       '5C-08: só a troca da errata T-83 na justificativa')
    ok('A6', P['edital'] == P19['edital'] and P['simulados'] == P19['simulados'], 'edital e simulados idênticos aos da v1.9')
    dl = [x['id'] for x, y in zip(P['lotes'], P19['lotes']) if x != y]
    ok('A7', dl == ['L2'] and [x['id'] for x in P['lotes']] == [x['id'] for x in P19['lotes']], 'lotes: só o L2 muda (%s)' % dl)
    l2, l219 = [x for x in P['lotes'] if x['id'] == 'L2'][0], [x for x in P19['lotes'] if x['id'] == 'L2'][0]
    esp = l219['curso'].replace('ver Lote 1-C.', 'ver o complemento do Lote 1 (adendo ao 1.4).')
    if cfg.E_CURSO:
        esp = esp.replace('   adaptação não corrige sotaque nem ruído.', '   adaptação não remove o ruído nem trata a causa acústica (sotaque pede\n   dados acústicos), embora possa melhorar o reconhecimento dos termos\n   esperados quando o áudio é ruidoso ou pouco claro.')
    ok('A8', {k for k in l2 if l2[k] != l219[k]} == {'curso'} and l2['curso'] == esp, 'L2: só o curso, com a(s) troca(s) %s' % ('T-84 e T-106' if cfg.E_CURSO else 'T-84'))
    dd = [x['id'] for x, y in zip(P['discursivas'], P19['discursivas']) if x != y]
    d3, d319 = [x for x in P['discursivas'] if x['id'] == 'D3'][0], [x for x in P19['discursivas'] if x['id'] == 'D3'][0]
    ok('A9', dd == (['D3'] if cfg.E_PADRAO else []) and (not cfg.E_PADRAO or ({k for k in d3 if d3[k] != d319[k]} == {'padrao'} and d3['padrao'] == d319['padrao'].replace(
        '      corrige sotaque nem ruído;', '      trata a causa acústica (ruído, sotaque), que pede dados acústicos;'))), 'discursivas: só D3.padrao, aspecto (xv) (%s)' % dd)
    l411 = [i for i in it if i['id'] == 'L4-11'][0]['justificativa']
    ok('A10', 'O F4 afirma que' in l411 and 'What is Machine Learning?' not in l411, 'L4-11 com o texto da v1.8 (D-ABSORCAO-V110 (c))')
    # (B) os 225 novos: forma e contagens
    nv = it[334:]
    ok('B1', all(list(i.keys()) == CHAVES + (['volatil'] if i.get('volatil') else []) for i in nv), 'forma: 14 campos na ordem do contrato (+ volatil só quando verdadeiro)')
    ok('B2', len({i['id'] for i in it}) == NN, 'ids únicos')
    ok('B3', all(i['rotulo'] == 'AUTORAL' and i['certame'] == 'Projeto Câmara 2026' and i['ano'] == 2026 and i['textoBase'] == '' and i['gabarito'] in 'CE' and i['justificativa'] for i in nv),
       'rotulo, certame, ano, textoBase, gabarito e justificativa')
    ed = {e['id'] for e in P['edital']}
    ok('B4', all(i['itemEdital'] in ed for i in it), 'todo itemEdital existe no edital')
    ok('B5', not any('QA PENDENTE' in json.dumps(i, ensure_ascii=False) for i in it), '0 "QA PENDENTE" nos itens')
    ids = [i['id'] for i in nv]
    esp_ids = ['L6B-R01', 'L6B-R02'] + ['L1-R%02d' % k for k in range(19, 131) if k != 43] + ['L1-R131'] + ['L2-R%02d' % k for k in range(19, 131) if k != 67] + (['L2-R131'] if cfg.E_L2R131 else [])
    ok('B6', ids == esp_ids, 'ids e ordem: L6B-R01/R02, L1-R19…R130 (sem R43), L1-R131, L2-R19…R130 (sem R67)')
    c = collections.Counter(i['gabarito'] for i in nv)
    ok('B7', (c['C'], c['E']) == (113, 112 + cfg.E_L2R131) and collections.Counter(i['gabarito'] for i in it) == collections.Counter({'C': 285, 'E': 274 + cfg.E_L2R131}), 'C/E: novos 113/%d; pacote 285/%d' % (112 + cfg.E_L2R131, 274 + cfg.E_L2R131))
    ok('B8', {i['id'] for i in nv if i.get('volatil')} == VOL and sum(1 for i in it if i.get('volatil')) == 54, 'volatil: os 29 das decisões; 54 no pacote')
    ok('B9', {i['id'] for i in nv if i['aderencia'] == 'parcial'} == PAR and sum(1 for i in it if i['aderencia'] == 'parcial') == 88, 'parcial: os 43 da T97_reconciliacao 3.1; 88 no pacote')
    ok('B10', all(i['cargo'] == {'L1': 'Lote 1', 'L2': 'Lote 2', 'L6B': 'Lote 6b'}[i['id'].split('-')[0]] and i['numero'] == int(i['id'].split('-R')[1]) for i in nv), 'cargo e numero')
    fc = collections.Counter(i['itemEdital'] for i in it)
    ok('B11', all(fc[f] == n for f, n in FOLHA_N.items()), 'itens por folha: P2-1.x e 2.x com 20 (2.4: 19), P1-4.3 com 6 (%s)' % {f: fc[f] for f in FOLHA_N if fc[f] != FOLHA_N[f]})
    dc = collections.Counter(i['itemEdital'] for i in it if i['aderencia'] == 'direta')
    ok('B12', all(dc[f] == n for f, n in DIRETAS_2.items()) and all(dc['P2-1.%d' % k] >= 10 for k in range(1, 9)), 'diretas por folha 2.x = T97 3.1; piso de 10 diretas em 1.x e 2.x')
    simids = {x for s in P['simulados'] for x in s['itens']}
    ok('B13', not simids & set(ids) and all(not ({'L4-11', 'BQ-0010'} <= set(s['itens'])) for s in P['simulados']), 'nenhum item novo em simulado; L4-11 e BQ-0010 nunca juntos')
    if fontes is not None:
        bad = [k for k in ids if fontes.get(k) != [nv[ids.index(k)]['comando'], nv[ids.index(k)]['enunciado'], nv[ids.index(k)]['gabarito'], nv[ids.index(k)]['justificativa']]]
        ok('B14', list(fontes) == ids and not bad, 'comando, enunciado, gabarito e justificativa = leitura própria dos arquivos finais (%s)' % bad[:3])
    # (C) estudante
    ok('C1', list(E.keys()) == list(E19.keys()) and E['nome'] == cfg.NOME_E and E['geradoEm'] == cfg.GERADO_EM and E['versao'] == 1, 'estudante: topo, nome, data')
    ei = E['itens']
    ok('C2', [i['id'] for i in ei] == [i['id'] for i in it] and all(list(x.keys())[-1] == 'nucleo' and isinstance(x['nucleo'], bool) for x in ei), 'estudante: mesmos ids; "nucleo" booleano e último campo')
    sem = [{k: v for k, v in x.items() if k != 'nucleo'} for x in ei[:334]]
    d19 = [x['id'] for x, y in zip(sem, E19['itens']) if x != y]
    ok('C3', d19 == ['5C-08'], 'estudante: dos 334 da v1.9-E (sem "nucleo"), só o 5C-08 muda (%s)' % d19)
    ok('C4', E['edital'] == E19['edital'] and E['simulados'] == E19['simulados'], 'estudante: edital e simulados idênticos aos da v1.9-E')
    ok('C5', [x['id'] for x, y in zip(E['lotes'], E19['lotes']) if x != y] == ['L2'] and [x['id'] for x, y in zip(E['discursivas'], E19['discursivas']) if x != y] == (['D3'] if cfg.E_PADRAO else []),
       'estudante: só lotes[L2] e discursivas[D3] mudam')
    ok('C6', all(x['url'] == '' for x in ei[334:]) and all(set(x) - {'nucleo'} == set(y) and all(x[k] == y[k] for k in y if k not in ('url', 'justificativa')) for x, y in zip(ei[334:], nv)), 'estudante, 225 novos: url "" e demais campos (fora justificativa) iguais')
    ndel = 0
    for x, y in zip(ei[334:], nv):
        a_, b_ = y['justificativa'], x['justificativa']
        if a_ != b_:
            ndel += 1
    ok('C7', ndel == 73, 'estudante, 225 novos: justificativa diferente em 73 itens (80 deleções da lista fechada; 7 itens com duas; %d)' % ndel)
    ok('C8', not any(w in x['justificativa'] for x in ei[334:] for w in ('REVERIFICAR', 'VOLÁTIL', 'D-T', '[TS]', 'verificado em', 'QA ')), 'estudante, 225 novos: sem marcas internas na justificativa')
    if banco is not None:
        pf = collections.defaultdict(list)
        for pos, x in enumerate(it):
            pf[x['itemEdital']].append((chave_nucleo(x, pos, banco), x['id']))
        esp_n = {}
        for f, xs in pf.items():
            for k, (_, iid) in enumerate(sorted(xs)):
                esp_n[iid] = k < 10
        ok('C9', all(x['nucleo'] == esp_n[x['id']] for x in ei), 'nucleo = os 10 primeiros por (data, ato, direta antes de parcial, posição) em cada folha, recalculado')
        ok('C10', all(sum(1 for x in ei if x['itemEdital'] == f and x['nucleo']) == min(10, len(xs)) for f, xs in pf.items()), 'nucleo: min(10, n) por folha')
    return R


if __name__ == '__main__':
    P = json.load(open(os.path.join(OUT, 'pacote.json'), encoding='utf-8'))
    E = json.load(open(os.path.join(OUT, 'pacote_estudante.json'), encoding='utf-8'))
    P19 = json.loads(refs.git_show(refs.C_V19, refs.PACOTE).decode('utf-8'))
    E19 = json.loads(refs.git_show(refs.C_V19, 'saida/pacote/pacote_estudante.json').decode('utf-8'))
    banco = {r['id']: r['data_verificacao'] for r in csv.DictReader(open(PATH('banco/banco.csv'), encoding='utf-8'), delimiter=';')}
    R = verifica(P, E, P19, E19, leitura_propria(), banco)
    # (D) registro adendo 2
    reg = open(os.path.join(OUT, 'registro_adendo2.md'), encoding='utf-8').read().split('\n')
    rids = [l.split(' | ')[0][2:] for l in reg if re.match(r'^\| L(1|2|6B)-R\d+ \| [CE] \|', l)]
    R.append(('D1', rids == [i['id'] for i in P['itens'][334:]], 'registro adendo 2: 225 linhas de item, mesmos ids e ordem do pacote'))
    # (E) edição .md
    ed = os.path.join(OUT, 'estudante')
    R.append(('E1', os.path.isdir(ed) and len(os.listdir(ed)) == 35 and os.path.exists(os.path.join(ed, 'NUCLEO.md')), 'edição .md: 35 arquivos (34 + NUCLEO.md)'))
    nf = sum(1 for f in sorted(os.listdir(ed)) for l in open(os.path.join(ed, f), encoding='utf-8') if l.startswith('## Itens de reforço')) if os.path.isdir(ed) else 0
    R.append(('E2', nf == 10, 'edição .md: seção "Itens de reforço" em 10 arquivos (_itens e _gabarito de L1, L2, L3, L6A, L6B)'))
    falhas = [r for r in R if not r[1]]
    for i, o, m in R:
        print('%-4s %s %s' % (i, 'OK  ' if o else 'FALHA', m))
    print('validate_v110: %d/%d OK (modo E_CURSO=%s, E_PADRAO=%s, E_L2R131=%s)' % (len(R) - len(falhas), len(R), cfg.E_CURSO, cfg.E_PADRAO, cfg.E_L2R131))
    with open(os.path.join(OUT, 'validate_v110.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(dict(total=len(R), ok=len(R) - len(falhas), verificacoes=[dict(id=i, ok=o, msg=m) for i, o, m in R]), f, ensure_ascii=False, indent=1)
        f.write('\n')
    sys.exit(1 if falhas else 0)
