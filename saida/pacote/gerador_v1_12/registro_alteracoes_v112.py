# -*- coding: utf-8 -*-
"""T-115 (gerador_v1_12, D1 da GBQ, seção 5) — passo 5: registro de alterações por id. Saídas: out/registro_alteracoes_<TAG>.csv (447 linhas; colunas iguais às da v1.11) e
out/registro_alteracoes_<TAG>_resumo.md (contagem por prefixo, por lote e por ação; contagem por tópico da ORDEM_V15_F; lista MANTER da D1, 3.5).
Prefixos: T115-I (itens novos, ADICIONAR, com ato, arquivo e SHA-256 LF), T115-L (deleções L-1 a L-5, DELETAR), T115-E (erratas de enunciado, SUBSTITUIR), T115-U (URL do compilado da LGPD, fora do pacote),
T115-P (pares: 72 da GCB e 67 da GCE, CONVERTIDO com o caminho `lotes[Lx].pegadinhas[k]` ou DESCARTADO com o motivo), T115-T (`topicos`: 40 resumos e 3 pilotos), T115-N (nomes de lote), T115-S-01 (nome do SIM-0),
T115-LM (`legendaMecanismo`), T115-R-01 (correção da coluna `parecer_qa` da T109-0001 do registro v1.11, que não muda). O pacote é regerado aqui a partir das fontes e conferido byte a byte com out/pacote.json.
Asserção: o conjunto (edicao, antes, depois) dos registros T115 do `interno` é igual ao das linhas T115-L, N, S e LM do CSV."""
import collections, csv, io, json, os, sys
from common import OUT
import refs, config_v112 as cfg
import build_v112 as B
import fontes_v112 as F
from fontes_v112 import Falha
import inventario_v112 as I

COLS = ['id_edicao', 'ids_ocorrencia', 'objeto', 'caminho', 'lote', 'categoria', 'acao', 'regra', 'antes', 'depois', 'fonte_origem', 'tabela', 'parecer_qa', 'aceite']
LOTE_NUM = {'L1': '1', 'L2': '2', 'L3': '3', 'L4': '4', 'L5': '5', 'L6A': '6a', 'L6B': '6b', 'L1C': '1-C', 'L4C': '4-C', 'L5C': '5-C'}
ATO_PEG = {'GCB': cfg.AP1, 'GCE': cfg.AP2}
ATO_TOP = {'P1': cfg.AP1, 'P2': cfg.AP2}
D1 = cfg.D1_ARQUIVO


def grava(nome, linhas, cols):
    buf = io.StringIO(newline='')
    w = csv.writer(buf, quoting=csv.QUOTE_ALL, lineterminator='\n')
    w.writerow(cols)
    for l in linhas:
        w.writerow([l.get(c, '') for c in cols])
    with open(os.path.join(OUT, nome), 'w', encoding='utf-8', newline='') as fh:
        fh.write(buf.getvalue())
    return buf.getvalue()


def sha_tab(rel):
    return '%s (SHA-256 LF %s)' % (rel, cfg.SHA[rel])


def linhas_registro(P, info, P0):
    meta, linhas = info['meta'], []
    # T115-I
    for k, (iid, m) in enumerate(meta.items(), 1):
        linhas.append(dict(id_edicao='T115-I-%03d' % k, ids_ocorrencia='', objeto=iid, caminho='itens[%s]' % iid, lote=LOTE_NUM[m['lote']], categoria='item novo (%s)' % m['grupo'], acao='ADICIONAR',
                           regra='', antes='', depois='', fonte_origem=m['arquivo'], tabela=sha_tab(m['arquivo']), parecer_qa='', aceite=m['ato']))
    # T115-L
    for r in info['linhas_limpeza']:
        m = meta[r['item']]
        linhas.append(dict(id_edicao=r['edicao'], ids_ocorrencia='', objeto=r['item'], caminho='itens[%s].justificativa' % r['item'], lote=LOTE_NUM[m['lote']], categoria=r['cat'], acao='DELETAR',
                           regra=r['regra'], antes=r['antes'], depois='', fonte_origem=m['arquivo'], tabela='%s (D1 da GBQ, 3.5)' % D1, parecer_qa='', aceite=m['ato']))
    # T115-E
    for e in info['erratas']:
        m = meta[e['item']]
        linhas.append(dict(id_edicao=e['edicao'], ids_ocorrencia='', objeto=e['item'], caminho='itens[%s].enunciado' % e['item'], lote=LOTE_NUM[m['lote']], categoria='errata de forma (gbq-estilo)',
                           acao='SUBSTITUIR', regra='', antes=e['antes'], depois=e['depois'], fonte_origem='%s (seção 2)' % cfg.ESTILO_ARQUIVO, tabela='%s (D1 da GBQ, 3.4)' % D1, parecer_qa='', aceite=cfg.AP2))
    # T115-U
    for u in info['urls']:
        m = meta[u['item']]
        linhas.append(dict(id_edicao=u['edicao'], ids_ocorrencia='', objeto=u['item'], caminho='base fora do pacote (%s)' % u['arquivo'], lote=LOTE_NUM[m['lote']], categoria='URL da base (T-11)',
                           acao='SUBSTITUIR', regra='%d ocorrência(s)' % u['ocorrencias'], antes=u['antes'], depois=u['depois'], fonte_origem=u['arquivo'], tabela='%s (D1 da GBQ, 3.4)' % D1, parecer_qa='', aceite=cfg.AP2))
    # T115-P
    for k, r in enumerate(info['peg']['rastro'], 1):
        conv = r['decisao'] == 'CONVERTIDO'
        linhas.append(dict(id_edicao='T115-P-%03d' % k, ids_ocorrencia=r['par'], objeto=r['lote'], caminho=';'.join(r['caminhos']) if conv else 'lotes[%s]' % r['lote'], lote=LOTE_NUM[r['lote']],
                           categoria='par %s × %s (%s)' % (r['a'], r['b'], r['itemEdital']), acao='ADICIONAR' if conv else 'DESCARTAR', regra='' if conv else r['motivo'], antes='',
                           depois=' || '.join(r['textos']), fonte_origem=r['arquivo'], tabela=sha_tab(r['arquivo']) if r['ger'] == 'GCE' else sha_tab(r['arquivo']), parecer_qa='', aceite=ATO_PEG[r['ger']]))
    # T115-T
    fontes = info['topicos_fontes']
    n = 0
    for k, t in P['topicos'].items():
        n += 1
        rel = fontes[k][0]
        linhas.append(dict(id_edicao='T115-T-%02d' % n, ids_ocorrencia='', objeto=k, caminho='topicos[%s].resumo' % k, lote=LOTE_NUM[B_lote(P, k)], categoria='resumo do tópico (ORDEM_V15_A)', acao='ADICIONAR',
                           regra='', antes='', depois='', fonte_origem=rel, tabela=sha_tab(rel), parecer_qa='', aceite=ATO_TOP[k[:2]]))
    for k, t in P['topicos'].items():
        if 'emUmMinuto' in t:
            n += 1
            rel = fontes[k][1]
            linhas.append(dict(id_edicao='T115-T-%02d' % n, ids_ocorrencia='', objeto=k, caminho='topicos[%s].emUmMinuto;topicos[%s].visuais' % (k, k), lote=LOTE_NUM[B_lote(P, k)],
                               categoria='piloto visual (ORDEM_V15_E)', acao='ADICIONAR', regra='', antes='', depois='', fonte_origem=rel, tabela=sha_tab(rel), parecer_qa='', aceite=ATO_TOP[k[:2]]))
    # T115-N, S, LM (os registros do interno)
    for r in info['regs_meta']:
        ger = 'GCE' if r['objeto'] in ('L1', 'L1C', 'L2', 'L3') else 'GCB' if r['objeto'] != 'SIM-0' else 'GBQ'
        cam = '%s[%s].%s' % (r['lista'], r['objeto'], r['campo'])
        acao = 'DELETAR' if r['regra'] == 'T115-LM' else 'SUBSTITUIR'
        linhas.append(dict(id_edicao=r['edicao'], ids_ocorrencia='', objeto=r['objeto'], caminho=cam, lote=LOTE_NUM.get(r['objeto'], '8'), categoria='metadado exibido sem código de produção', acao=acao,
                           regra=r['regra'], antes=r['antes'], depois=r['depois'], fonte_origem='%s (3.8)' % D1, tabela='%s (D1 da GBQ, 3.8)' % D1, parecer_qa='', aceite='D1 da GBQ (T115, 3.8); D-PACOTE-V111'))
    # T115-R-01
    v111 = list(csv.DictReader(io.StringIO(refs.git_show(cfg.BASE[0], 'saida/pacote/registro_alteracoes_v1_11.csv').decode('utf-8'), newline='')))
    t109 = [x for x in v111 if x['id_edicao'] == 'T109-0001']
    if len(t109) != 1 or t109[0]['parecer_qa'] != 'QA_T109_R1_2026-10-18_gce-cqfp.md':
        raise Falha('C-12', 'T109-0001 do registro v1.11 com parecer_qa %r' % (t109[0]['parecer_qa'] if t109 else None))
    linhas.append(dict(id_edicao='T115-R-01', ids_ocorrencia='T109-0001', objeto='registro_alteracoes_v1_11.csv', caminho='registro v1.11, linha T109-0001, coluna parecer_qa', lote='2', categoria='correção de caminho',
                       acao='SUBSTITUIR', regra='', antes='QA_T109_R1_2026-10-18_gce-cqfp.md', depois='saida/gce/QA_T109_R1_2026-10-18_gce-cqfp.md', fonte_origem='%s (3.8, achado 7 da v1.11)' % D1,
                       tabela='%s (D1 da GBQ, 3.8)' % D1, parecer_qa='', aceite='D1 da GBQ (T115, 3.8)'))
    return linhas


def B_lote(P, k):
    return I.lote_do_topico(P, k)


def main():
    P0, _ = B.le_base()
    P, info = B.gera(P0)
    txt = json.dumps(P, ensure_ascii=False, indent=1) + '\n'
    if txt.encode('utf-8') != open(os.path.join(OUT, 'pacote.json'), 'rb').read():
        raise Falha('C-3', 'o pacote regerado difere do out/pacote.json')
    linhas = linhas_registro(P, info, P0)
    csv_txt = grava('registro_alteracoes_%s.csv' % cfg.TAG, linhas, COLS)
    ids = [l['id_edicao'] for l in linhas]
    if len(set(ids)) != len(ids) or len(linhas) != cfg.TOTAIS['registro']:
        raise Falha('C-RG', '%d linhas, %d ids distintos (esperado %d)' % (len(linhas), len(set(ids)), cfg.TOTAIS['registro']))
    interno = {(r['edicao'], r['antes'], r['depois']) for lista in ('itens', 'lotes', 'simulados', 'discursivas') for o in P[lista] for r in o.get('interno', []) if r['edicao'].startswith('T115-')}
    csvset = {(l['id_edicao'], l['antes'], l['depois']) for l in linhas if l['id_edicao'].split('-')[1] in ('L', 'N', 'S', 'LM')}
    if interno != csvset:
        raise Falha('C-12', 'o conjunto (edicao, antes, depois) dos registros T115 do `interno` difere do das linhas T115-L, N, S e LM')
    por_lote = collections.defaultdict(collections.Counter)
    por_acao = collections.Counter(l['acao'] for l in linhas)
    for l in linhas:
        por_lote[l['lote']][l['acao']] += 1
    # contagem por tópico (ORDEM_V15_F): folha, base, +onda 4, +F1, versão nova
    meta = info['meta']
    folhas = collections.OrderedDict()
    for i in P0['itens']:
        folhas.setdefault(i['itemEdital'], [0, 0, 0, 0])[0] += 1
    for iid, m in meta.items():
        row = folhas.setdefault(m['folha'], [0, 0, 0, 0])
        row[1 if m['grupo'] == 'ONDA4' else 2] += 1
    insp = I.varre(P, 'D')
    Lr = []; w = Lr.append
    w('# Registro de alterações por id — v%s (%s) — gerado por registro_alteracoes_v112.py' % (cfg.VERSAO, 'FINAL' if cfg.FINAL else 'ENSAIO'))
    w('')
    w('Linhas: %d (%s). O registro v1.11 não muda; a linha T115-R-01 corrige a coluna `parecer_qa` da T109-0001 dele.' % (len(linhas), ', '.join('%s %d' % kv for kv in sorted(por_acao.items()))))
    w('')
    w('## Por prefixo')
    w('| Prefixo | Linhas |')
    w('|---|--:|')
    ordem = ['T115-I', 'T115-L', 'T115-E', 'T115-U', 'T115-P', 'T115-T', 'T115-N', 'T115-S', 'T115-LM', 'T115-R']
    cont = collections.Counter()
    for l in linhas:
        p = l['id_edicao'].split('-')
        cont['-'.join(p[:2])] += 1
    for p in ordem:
        w('| %s | %d |' % (p, cont[p]))
    w('| **Total** | **%d** |' % len(linhas))
    w('')
    w('## Por lote e ação')
    w('| Lote | Ação | Linhas |')
    w('|---|---|--:|')
    for lt in sorted(por_lote):
        for a, n in sorted(por_lote[lt].items()):
            w('| %s | %s | %d |' % (lt, a, n))
    w('')
    w('## Por tópico da ORDEM_V15_F (folha: v1.11, +onda 4, +F1, v%s)' % cfg.VERSAO)
    w('| Folha | v1.11 | +onda 4 | +F1 | v%s |' % cfg.VERSAO)
    w('|---|--:|--:|--:|--:|')
    for f_ in sorted(folhas, key=lambda s: (s[:2], [int(x) for x in s[3:].split('.')])):
        a, b, c_, _ = folhas[f_]
        if b or c_:
            w('| %s | %d | %d | %d | %d |' % (f_, a, b, c_, a + b + c_))
    w('')
    w('## Edições por regra de limpeza (itens novos)')
    ec = collections.Counter(l['regra'] for l in linhas if l['id_edicao'].startswith('T115-L-'))
    w(', '.join('%s %d' % (k, ec[k]) for k in ('L-2', 'L-1', 'L-5', 'L-3', 'L-4')) + '; total %d em %d itens.' % (sum(ec.values()), len({l['objeto'] for l in linhas if l['id_edicao'].startswith('T115-L-')})))
    w('')
    w('## Lista MANTER (D1, 3.5): ocorrências do inventário que continuam, por campo de texto novo')
    w('| Campo | Categoria | Casamento | Ocorrências na v%s | Classe(s) |' % cfg.VERSAO)
    w('|---|---|---|--:|---|')
    for (cam, cat, cas), n in cfg.MANTER.items():
        oc = [o for o in insp if o['caminho'] == cam and o['categoria'] == cat and o['casamento'] == cas]
        w('| %s | %s | %s | %d | %s |' % (cam, cat, cas, len(oc), ', '.join(sorted({o['classe'] for o in oc}))))
    for (cam, cat, cas) in cfg.MANTER_FP_ESPERADO:
        oc = [o for o in insp if o['caminho'] == cam and o['categoria'] == cat and o['casamento'] == cas]
        w('| %s | %s | %s | %d | %s |' % (cam, cat, cas, len(oc), ', '.join(sorted({o['classe'] for o in oc}))))
    with open(os.path.join(OUT, 'registro_alteracoes_%s_resumo.md' % cfg.TAG), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('\n'.join(Lr) + '\n')
    print('registro de alterações: %d linhas (%s); interno T115 = CSV (%d registros)' % (len(linhas), ', '.join('%s %d' % (p, cont[p]) for p in ordem), len(interno)))


if __name__ == '__main__':
    try:
        main()
    except Falha as e:
        print('FALHA:', e)
        sys.exit(1)
