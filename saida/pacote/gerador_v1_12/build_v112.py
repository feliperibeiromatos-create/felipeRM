# -*- coding: utf-8 -*-
"""T-115 (gerador_v1_12; D1 da GBQ, saida/pacote/T115_D1_v1_12_2026-10-18.md, seções 0, 3.1 a 3.8) — passo 1: gera out/pacote.json, out/stats_<TAG>.json e out/folhas_<TAG>.json.
Base: o pacote.json v1.11 canônico (D-PACOTE-V111), lido do blob do commit config_v112.BASE[0] e conferido pelo SHA-256 e pela serialização canônica. Mudanças, e só elas (D1, seção 0):
  (1) 189 itens novos ao FIM de `itens` (reforco_v112.py): onda 4 (84), onda 1 da ORDEM_V15_F, P1 (7) e P2 (98); erratas de enunciado (3) e limpeza L-1 a L-5 das justificativas (53 deleções, `interno` do item);
  (2) 73 pegadinhas em `lotes[].pegadinhas` (pegadinhas_v112.py), com a reindexação mecânica dos registros `pegadinhas[k]` do `interno` dos lotes (o índice k da v1.11 passa ao da v1.12);
  (3) `topicos` (topicos_v112.py), último campo de topo; (4) nomes de lote sem código de produção, `nome` do SIM-0 sem "(v0.2)", `legendaMecanismo` não emitida, cada troca no `interno` do objeto;
  (5) `nome` e `geradoEm` de config_v112. Nada mais muda. `reverte_para_base` desfaz exatamente isso e devolve a v1.11 byte a byte (C-5). Não lê relógio."""
import collections, copy, hashlib, json, os, re, subprocess, sys
from common import OUT, REPO, P as PATH
import refs, config_v112 as cfg
import fontes_v112 as F
from fontes_v112 import Falha
import reforco_v112 as R
import limpeza_v112 as L
import pegadinhas_v112 as PG
import topicos_v112 as TP
import nucleo as NU


def le_base():
    raw = refs.git_show(cfg.BASE[0], cfg.BASE[1])
    if hashlib.sha256(raw).hexdigest() != cfg.BASE[2]:
        raise Falha('C-1', 'pacote.json base (git %s) com SHA-256 diferente do aceito' % cfg.BASE[0])
    txt = raw.decode('utf-8')
    P = json.loads(txt, object_pairs_hook=collections.OrderedDict)
    if json.dumps(P, ensure_ascii=False, indent=1) + '\n' != txt:
        raise Falha('C-1', 'base não é a serialização canônica')
    if P['nome'] != cfg.BASE_NOME or len(P['itens']) != cfg.BASE_ITENS or list(P) != ['versao', 'geradoEm', 'nome', 'edital', 'itens', 'simulados', 'lotes', 'discursivas']:
        raise Falha('C-1', 'base: nome, número de itens ou chaves de topo diferentes do esperado (%r, %d)' % (P['nome'], len(P['itens'])))
    return P, raw


def confere_decisoes(dec=None, ct=None):
    """As decisões de aceite precisam estar em DECISOES.md (linha "| id |"); o contrato precisa ser o v1.2.9. `dec` e `ct` (textos) só são passados pelos testes de mutação."""
    if dec is None:
        dec = open(PATH('DECISOES.md'), encoding='utf-8').read()
    falta = [d for d in cfg.DECISOES_EXIGIDAS if ('| %s |' % d) not in dec]
    if falta:
        raise Falha('C-1', 'DECISOES.md sem a linha "| id |" de: %s' % falta)
    if ct is None:
        ct = open(PATH('regras/pacote_contrato.md'), 'rb').read().replace(bytes([13, 10]), bytes([10])).decode('utf-8')
    if cfg.CONTRATO_VERSAO not in ct.split(chr(10))[0]:
        raise Falha('C-14', 'contrato sem "%s" na linha 1' % cfg.CONTRATO_VERSAO)
    if hashlib.sha256(ct.encode('utf-8')).hexdigest() != cfg.CONTRATO_SHA_LF:
        raise Falha('C-14', 'SHA-256 (LF) do contrato diferente do fixado na D1 (seção 2.1)')
    return dec


def objeto(P, lista, ident):
    o = [x for x in P[lista] if x['id'] == ident]
    if len(o) != 1:
        raise Falha('C-2', '%s[%s] ausente' % (lista, ident))
    return o[0]


def registro_interno(edicao, campo, antes, depois, regra):
    return collections.OrderedDict([('edicao', edicao), ('campo', campo), ('pos', 0), ('antes', antes), ('depois', depois), ('regra', regra), ('ocorrencias', [])])


def reindexa_campo(campo, rm):
    m = re.fullmatch(r'pegadinhas\[(\d+)\]\.(\w+)', campo)
    if not m:
        return campo
    return 'pegadinhas[%d].%s' % (rm[int(m.group(1))], m.group(2))


def gera(P0):
    """P0: pacote v1.11 (não é alterado). -> (P, info)."""
    P = copy.deepcopy(P0)
    ids_base = {i['id'] for i in P0['itens']}
    # --- itens novos
    novos, meta, vl = R.carrega(ids_base)
    erratas, urls = L.aplica_erratas(novos, meta)
    just_arquivo = {i['id']: i['justificativa'] for i in novos}
    linhas_l = L.limpa_itens(novos)
    P['itens'] = P['itens'] + novos
    # --- pegadinhas
    peg = PG.aplica(P)
    n_antes_interno = {L_['id']: len(L_.get('interno', [])) for L_ in P['lotes']}
    for L_ in P['lotes']:
        if 'interno' in L_:
            for rc in L_['interno']:
                rc['campo'] = reindexa_campo(rc['campo'], peg['remap'][L_['id']])
    # --- metadados: nomes de lote, SIM-0, legendaMecanismo
    regs_meta = []
    n = 0
    for lid, (antes, depois) in cfg.NOMES_LOTE.items():
        o = objeto(P, 'lotes', lid)
        if o['nome'] != antes:
            raise Falha('C-2', 'lotes[%s].nome diferente do esperado: %r' % (lid, o['nome']))
        o['nome'] = depois
        n += 1
        regs_meta.append(dict(edicao='T115-N-%02d' % n, objeto=lid, lista='lotes', campo='nome', antes=antes, depois=depois, regra='T115-N'))
    s0 = objeto(P, 'simulados', 'SIM-0')
    if s0['nome'] != cfg.SIM0_NOME[0]:
        raise Falha('C-2', 'SIM-0.nome: %r' % s0['nome'])
    s0['nome'] = cfg.SIM0_NOME[1]
    regs_meta.append(dict(edicao='T115-S-01', objeto='SIM-0', lista='simulados', campo='nome', antes=cfg.SIM0_NOME[0], depois=cfg.SIM0_NOME[1], regra='T115-S'))
    n = 0
    for lid in cfg.LEGENDA_FORA:
        o = objeto(P, 'lotes', lid)
        if not o.get('legendaMecanismo'):
            raise Falha('C-2', 'lotes[%s].legendaMecanismo ausente' % lid)
        n += 1
        regs_meta.append(dict(edicao='T115-LM-%02d' % n, objeto=lid, lista='lotes', campo='legendaMecanismo', antes=o['legendaMecanismo'], depois='', regra='T115-LM'))
        del o['legendaMecanismo']
    outras = [x['id'] for x in P['lotes'] if 'legendaMecanismo' in x]
    if outras:
        raise Falha('C-2', 'legendaMecanismo ainda presente em %s' % outras)
    # interno: acrescenta os registros T115 e ordena por (campo, pos), estável (a ordem dos registros da v1.11 é preservada nos empates)
    for r in regs_meta:
        o = objeto(P, r['lista'], r['objeto'])
        o.setdefault('interno', [])
        o['interno'].append(registro_interno(r['edicao'], r['campo'], r['antes'], r['depois'], r['regra']))
    for lista in ('lotes', 'simulados'):
        for o in P[lista]:
            if 'interno' in o:
                o['interno'] = sorted(o['interno'], key=lambda x: (x['campo'], x['pos']))
                it = o.pop('interno')
                o['interno'] = it          # interno é o último campo do objeto
    # --- tópicos
    edital_ids = [e['id'] for e in P['edital']]
    topicos, fontes_top = TP.monta(edital_ids)
    viol = TP.valida_topicos(topicos, edital_ids)
    if viol:
        raise Falha('C-T', 'topicos fora das regras do contrato v1.2.9, ponto 1: %s' % viol[:3])
    P['topicos'] = topicos
    P['nome'] = cfg.NOME
    P['geradoEm'] = cfg.GERADO_EM
    # --- atos e núcleo
    atos = collections.OrderedDict((i, m['ato']) for i, m in meta.items())
    NU.registra_extra(atos)
    info = dict(meta=meta, erratas=erratas, urls=urls, linhas_limpeza=linhas_l, just_arquivo=just_arquivo, peg=peg, regs_meta=regs_meta, topicos_fontes=fontes_top, vl=vl, atos=atos,
                n_interno_lotes_antes=n_antes_interno)
    # C-5 (asserção do passo 1): desfazendo só o que a v1.12 acrescenta, volta a v1.11
    Q = reverte_para_base(P, [x[2]['texto'] for x in peg['novas']], [i['id'] for i in novos], P0)
    if json.dumps(Q, ensure_ascii=False, indent=1) != json.dumps(P0, ensure_ascii=False, indent=1):
        raise Falha('C-5', 'reversibilidade: desfazendo a versão nova não se obtém o pacote v1.11')
    return P, info


def desindexa(campo, novo2antigo):
    m = re.fullmatch(r'pegadinhas\[(\d+)\]\.(\w+)', campo)
    if not m:
        return campo
    return 'pegadinhas[%d].%s' % (novo2antigo[int(m.group(1))], m.group(2))


def reverte_para_base(P, textos_pegadinhas_novas, ids_novos, P0):
    """Desfaz a versão nova: retira os itens novos, as pegadinhas novas (pelo texto da fonte), `topicos`; aplica ao contrário (o último primeiro) os registros T115 do `interno` dos lotes e do SIM-0 e os retira;
    devolve os índices dos registros `pegadinhas[k]` da v1.11; restaura nome e geradoEm da base. P0 só fornece nome/geradoEm (cópia)."""
    Q = copy.deepcopy(P)
    if list(Q)[-1] != 'topicos':
        raise Falha('C-5', 'topicos não é o último campo de topo')
    del Q['topicos']
    if [i['id'] for i in Q['itens'][cfg.BASE_ITENS:]] != list(ids_novos):
        raise Falha('C-5', 'os itens depois dos %d da v1.11 não são os novos' % cfg.BASE_ITENS)
    Q['itens'] = Q['itens'][:cfg.BASE_ITENS]
    pend = collections.Counter(textos_pegadinhas_novas)
    for L_ in Q['lotes']:
        novo, n2a = [], {}
        for k, g in enumerate(L_['pegadinhas']):
            if pend.get(g['texto'], 0) > 0 and g['texto'] in textos_pegadinhas_novas:
                pend[g['texto']] -= 1
                continue
            n2a[k] = len(novo)
            novo.append(g)
        L_['pegadinhas'] = novo
        if 'interno' in L_:
            for rc in L_['interno']:
                rc['campo'] = desindexa(rc['campo'], n2a)
    if sum(pend.values()) != 0:
        raise Falha('C-5', 'pegadinhas novas não encontradas: %d' % sum(pend.values()))
    for lista in ('lotes', 'simulados'):
        for o in Q[lista]:
            if 'interno' not in o:
                continue
            ficam = []
            for rc in reversed(o['interno']):
                if not rc['edicao'].startswith('T115-'):
                    ficam.append(rc)
                    continue
                if rc['campo'] == 'legendaMecanismo':
                    if 'legendaMecanismo' in o or rc['depois'] != '':
                        raise Falha('C-5', '%s: legendaMecanismo' % rc['edicao'])
                    nv = collections.OrderedDict()
                    for k, v in o.items():
                        if k == 'interno':
                            nv['legendaMecanismo'] = rc['antes']
                        nv[k] = v
                    o.clear(); o.update(nv)
                else:
                    t = o[rc['campo']]
                    if t[rc['pos']:rc['pos'] + len(rc['depois'])] != rc['depois']:
                        raise Falha('C-5', '%s: texto[pos:pos+len(depois)] != depois' % rc['edicao'])
                    o[rc['campo']] = t[:rc['pos']] + rc['antes'] + t[rc['pos'] + len(rc['depois']):]
            ficam.reverse()
            if ficam:
                o['interno'] = ficam
            else:
                del o['interno']
    Q['nome'], Q['geradoEm'] = P0['nome'], P0['geradoEm']
    return Q


def main():
    pend = []
    if cfg.FINAL:
        F.confere_todos()
        confere_decisoes()
    else:
        F.confere_todos()       # os 23 SHA-256 LF são conferidos também no ENSAIO
        try:
            confere_decisoes()
        except Falha as e:
            pend.append(str(e))
    P0, raw0 = le_base()
    P, info = gera(P0)
    os.makedirs(OUT, exist_ok=True)
    txt = json.dumps(P, ensure_ascii=False, indent=1) + '\n'
    with open(os.path.join(OUT, 'pacote.json'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(txt)
    meta = info['meta']
    nuc, rel, K = NU.calcula(P)
    folhas = collections.OrderedDict()
    for f_, v in rel.items():
        its = [i for i in P['itens'] if i['itemEdital'] == f_]
        folhas[f_] = collections.OrderedDict(total=len(its), diretos=sum(1 for i in its if i['aderencia'] == 'direta'), volateis=sum(1 for i in its if i.get('volatil')), nucleo=v['nucleo'],
                                             c=sum(1 for i in its if i['gabarito'] == 'C'), e=sum(1 for i in its if i['gabarito'] == 'E'), parciais=sum(1 for i in its if i['aderencia'] == 'parcial'),
                                             autoral=sum(1 for i in its if i['rotulo'] == 'AUTORAL'), reais=sum(1 for i in its if i['rotulo'] != 'AUTORAL'))
    with open(os.path.join(OUT, 'folhas_%s.json' % cfg.TAG), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(folhas, f, ensure_ascii=False, indent=1); f.write('\n')
    c = collections.Counter(i['gabarito'] for i in P['itens'])
    novos = [i for i in P['itens'] if i['id'] in meta]
    grupos = collections.OrderedDict()
    for gk in cfg.GRUPOS:
        ids = [i for i, m in meta.items() if m['grupo'] == gk]
        cg = collections.Counter(meta[i]['gab'] for i in ids)
        grupos[gk] = dict(n=len(ids), C=cg['C'], E=cg['E'], ts=sum(1 for i in ids if meta[i]['ts']), volateis=[i for i in ids if meta[i]['volatil']], parciais=[i for i in ids if meta[i]['aderencia'] == 'parcial'],
                          por_folha=dict(collections.Counter(meta[i]['folha'] for i in ids)), ato=cfg.GRUPOS[gk]['ato'])
    stats = collections.OrderedDict(
        modo='FINAL' if cfg.FINAL else 'ENSAIO', versao=cfg.VERSAO, pendencias=pend,
        base=dict(commit=cfg.BASE[0], sha256=cfg.BASE[2], itens=cfg.BASE_ITENS),
        insumos=[dict(n=n, arquivo=a, sha256_lf=h, ato=at) for n, a, h, at in cfg.INSUMOS],
        grupos=grupos, totais=dict(itens=len(P['itens']), C=c['C'], E=c['E'], parcial=sum(1 for i in P['itens'] if i['aderencia'] == 'parcial'), volatil=sum(1 for i in P['itens'] if i.get('volatil')),
                                   volatil_novos=sum(1 for i in novos if i.get('volatil')), novos=len(novos), pegadinhas=sum(len(L_['pegadinhas']) for L_ in P['lotes']),
                                   pegadinhas_novas=len(info['peg']['novas']), topicos=len(P['topicos']), pilotos=sum(1 for t in P['topicos'].values() if 'emUmMinuto' in t)),
        pegadinhas_por_lote=collections.OrderedDict((L_['id'], len(L_['pegadinhas'])) for L_ in P['lotes']),
        edicoes_por_regra=dict(collections.Counter(x['regra'] for x in info['linhas_limpeza'])), delecoes=len(info['linhas_limpeza']), itens_com_delecao=len({x['item'] for x in info['linhas_limpeza']}),
        erratas=[dict(edicao=e['edicao'], item=e['item']) for e in info['erratas']], urls=info['urls'], vagos=info['vl']['vagos'], diferidos=info['vl']['diferidos'],
        regs_meta=[dict(edicao=r['edicao'], objeto=r['objeto'], campo=r['campo'], regra=r['regra']) for r in info['regs_meta']],
        atos_novos=info['atos'], reforco=list(meta), size=len(txt.encode('utf-8')), sha256_pacote=hashlib.sha256(txt.encode('utf-8')).hexdigest(), logs=R.LOG)
    with open(os.path.join(OUT, 'stats_%s.json' % cfg.TAG), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(stats, f, ensure_ascii=False, indent=1); f.write('\n')
    print('modo %s; itens %d (%d novos); C/E %d/%d; PARCIAL %d; VOLÁTIL %d (%d novos); pegadinhas %d (+%d); topicos %d (%d pilotos); deleções %d em %d itens; bytes %d; sha256 %s' % (
        stats['modo'], len(P['itens']), len(novos), c['C'], c['E'], stats['totais']['parcial'], stats['totais']['volatil'], stats['totais']['volatil_novos'], stats['totais']['pegadinhas'],
        stats['totais']['pegadinhas_novas'], stats['totais']['topicos'], stats['totais']['pilotos'], stats['delecoes'], stats['itens_com_delecao'], stats['size'], stats['sha256_pacote']))
    if pend:
        print('PENDÊNCIAS (ENSAIO):', pend)


if __name__ == '__main__':
    try:
        main()
    except Falha as e:
        print('FALHA:', e)
        sys.exit(1)
