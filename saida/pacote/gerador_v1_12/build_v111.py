# -*- coding: utf-8 -*-
"""T-108 e T-109 (gerador_v1_11) — passo 1: gera out/pacote.json (limpeza das tabelas aceitas, campo `interno`, troca do L2-R16) e out/stats_<TAG>.json.
Base: o pacote.json v1.10 aceito, lido do git (config_v111.BASE) e conferido pelo SHA-256. Mudanças, e só elas (D1 da GBQ, seções 1.4 a 1.7): as edições SUBSTITUIR/DELETAR das tabelas
(cada uma literal, registrada no `interno`), a troca do `itemEdital` do L2-R16 (T-109; se config.E_L2R16), `nome` e `geradoEm`. Nada mais muda.
`gera(...)` é reusada pelos testes de mutação; `main()` lê as tabelas de config.TABELAS. Falha = exceção tabelas_v111.Falha (código de saída 1). Não lê relógio."""
import collections, hashlib, json, os, re, sys
from common import OUT
import refs, config_v111 as cfg
import tabelas_v111 as T
import limpeza_v111 as L
import inventario_v111 as I


def le_base():
    raw = refs.git_show(cfg.BASE[0], cfg.BASE[1])
    if hashlib.sha256(raw).hexdigest() != cfg.BASE[2]:
        raise T.Falha('C-1', 'pacote.json base (git %s) com SHA-256 diferente do aceito' % cfg.BASE[0])
    txt = raw.decode('utf-8')
    P = json.loads(txt, object_pairs_hook=collections.OrderedDict)
    if json.dumps(P, ensure_ascii=False, indent=1) + '\n' != txt:
        raise T.Falha('C-1', 'base não é a serialização canônica')
    if P['nome'] != cfg.BASE_NOME or len(P['itens']) != cfg.BASE_ITENS:
        raise T.Falha('C-1', 'base: nome ou número de itens diferente do esperado (%r, %d)' % (P['nome'], len(P['itens'])))
    return P, raw


def troca_l2r16(P, t109_raw):
    """Seção 1.7. Lê a linha do registro por id da seção 2 do T109 e troca o itemEdital do L2-R16."""
    txt = t109_raw.decode('utf-8')
    sec = txt.split('\n## 2.', 1)
    if len(sec) != 2:
        raise T.Falha('C-4', 'T109: seção 2 ausente')
    sec2 = sec[1].split('\n## 3.', 1)[0]
    if not re.search(r'^\| L2-R16 \| itemEdital \| P2-2\.8 \| P2-3\.1 \|', sec2, re.M):
        raise T.Falha('C-4', 'T109: linha "L2-R16 | itemEdital | P2-2.8 | P2-3.1" ausente da seção 2')
    it = [i for i in P['itens'] if i['id'] == 'L2-R16']
    if len(it) != 1 or it[0]['itemEdital'] != 'P2-2.8':
        raise T.Falha('C-4', 'L2-R16 ausente da base ou fora de P2-2.8')
    if 'P2-3.1' not in {e['id'] for e in P['edital']}:
        raise T.Falha('C-4', 'P2-3.1 não existe em edital[]')
    r17 = [i for i in P['itens'] if i['id'] == 'L2-R17']
    if len(r17) != 1 or r17[0]['itemEdital'] != 'P2-2.8':
        raise T.Falha('C-4', 'L2-R17 deveria estar em P2-2.8')
    for s in P['simulados']:
        if 'L2-R16' in s['itens']:
            raise T.Falha('C-4', 'L2-R16 está em %s' % s['id'])
    it[0]['itemEdital'] = 'P2-3.1'
    return dict(id='L2-R16', campo='itemEdital', antes='P2-2.8', depois='P2-3.1')


def gera(tab_itens, ocorr_raw, t109_raw, completa=True, verifica_sha=False, excecoes=None, aplicar_l2r16=None):
    """-> (P_novo, info). tab_itens: [(gerência, nome, bytes, sha)]."""
    P0, raw_base = le_base()
    if hashlib.sha256(ocorr_raw).hexdigest() != cfg.OCORRENCIAS[1]:
        raise T.Falha('C-1', 'SHA-256 do inventário de ocorrências diferente do fixado')
    if t109_raw is not None and cfg.T109[1] and hashlib.sha256(t109_raw).hexdigest() != cfg.T109[1]:
        raise T.Falha('C-1', 'SHA-256 do T109 diferente do fixado')
    inv_l = I.varre(P0, 'D')
    inv = {o['id_ocorrencia']: o for o in inv_l}
    oc = T.le_ocorrencias(ocorr_raw)
    # o inventário recalculado sobre a base tem de ser o do arquivo de ocorrências (mesmo id, caminho e classe)
    dif = [i for i in set(inv) | set(oc) if i not in inv or i not in oc or inv[i]['caminho'] != oc[i]['caminho'] or inv[i]['classe'] != oc[i]['classe']]
    if dif:
        raise T.Falha('C-1', 'inventário recalculado difere de T108_ocorrencias.csv em %d id(s) (ex.: %s)' % (len(dif), dif[0]))
    rows = T.carrega_de_bytes(tab_itens, verifica_sha)
    cob = T.valida_cobertura(rows, oc, inv, completa=completa)
    P, res = L.aplica(P0, rows, inv, cfg.EXCECOES_DEPOIS if excecoes is None else excecoes)
    t_l2 = None
    if (cfg.E_L2R16 if aplicar_l2r16 is None else aplicar_l2r16):
        t_l2 = troca_l2r16(P, t109_raw)
    P['nome'] = cfg.NOME
    P['geradoEm'] = cfg.GERADO_EM
    # C-5 (asserção do passo 1): o `interno` aplicado ao contrário devolve a base, byte a byte, na serialização canônica
    Q = L.reverte(P)
    if t_l2:
        [i for i in Q['itens'] if i['id'] == 'L2-R16'][0]['itemEdital'] = 'P2-2.8'
    Q['nome'], Q['geradoEm'] = P0['nome'], P0['geradoEm']
    if json.dumps(Q, ensure_ascii=False, indent=1) != json.dumps(P0, ensure_ascii=False, indent=1):
        raise T.Falha('C-5', 'reversibilidade: o interno aplicado ao contrário não devolve o pacote v1.10')
    info = dict(cobertura=cob, aplicadas=res['aplicadas'], mantidas=res['mantidas'], por_acao=res['por_acao'], l2r16=t_l2, linhas=res['linhas'], manter=res['manter'],
                registros=res['registros'], rows=rows, inv=inv, oc=oc)
    return P, info


def main():
    pend = cfg.confere_final() if cfg.FINAL else []
    if pend:
        raise T.Falha('C-1', 'condições de entrada da geração final não cumpridas: ' + '; '.join(pend))
    os.makedirs(OUT, exist_ok=True)
    tabs = [(g, c, T.le_bytes(c), h) for g, c, h in cfg.TABELAS]
    P, info = gera(tabs, T.le_bytes(cfg.OCORRENCIAS[0]), T.le_bytes(cfg.T109[0]), completa=True, verifica_sha=cfg.FINAL)
    txt = json.dumps(P, ensure_ascii=False, indent=1) + '\n'
    with open(os.path.join(OUT, 'pacote.json'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(txt)
    base_raw = refs.git_show(cfg.BASE[0], cfg.BASE[1])
    stats = collections.OrderedDict(
        modo='FINAL' if cfg.FINAL else 'ENSAIO', versao=cfg.VERSAO, alvo=cfg.ALVO,
        base=dict(commit=cfg.BASE[0], sha256=cfg.BASE[2], itens=cfg.BASE_ITENS),
        tabelas=[dict(gerencia=g, arquivo=c, sha256=hashlib.sha256(raw).hexdigest(), sha256_fixado=h) for g, c, raw, h in tabs],
        ocorrencias=dict(arquivo=cfg.OCORRENCIAS[0], sha256=hashlib.sha256(T.le_bytes(cfg.OCORRENCIAS[0])).hexdigest()),
        t109=dict(arquivo=cfg.T109[0], sha256=hashlib.sha256(T.le_bytes(cfg.T109[0])).hexdigest(), E_L2R16=cfg.E_L2R16, ATO_L2R16=cfg.ATO_L2R16),
        cobertura=info['cobertura'], edicoes_aplicadas=info['aplicadas'], linhas_manter=info['mantidas'], por_acao=info['por_acao'],
        por_gerencia=dict(collections.Counter(r['_ger'] for r in info['rows'])), l2r16=info['l2r16'],
        reforco=[i['id'] for i in P['itens'][334:]], size=len(txt.encode('utf-8')), sha256_pacote=hashlib.sha256(txt.encode('utf-8')).hexdigest())
    with open(os.path.join(OUT, 'stats_%s.json' % cfg.TAG), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(stats, f, ensure_ascii=False, indent=1); f.write('\n')
    # insumo da cobertura (T-95, fora do gerador): por folha, total, diretos, VOLÁTEIS, núcleo
    import nucleo as NU
    nuc, rel, _ = NU.calcula(P)
    folhas = collections.OrderedDict()
    for f_, v in rel.items():
        its = [i for i in P['itens'] if i['itemEdital'] == f_]
        folhas[f_] = dict(total=len(its), diretos=sum(1 for i in its if i['aderencia'] == 'direta'), volateis=sum(1 for i in its if i.get('volatil')), nucleo=v['nucleo'])
    with open(os.path.join(OUT, 'folhas_%s.json' % cfg.TAG), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(folhas, f, ensure_ascii=False, indent=1); f.write('\n')
    c = collections.Counter(i['gabarito'] for i in P['itens'])
    print('modo %s; itens %d; C/E %d/%d; edições aplicadas %d; MANTER %d; interno em %d objetos; bytes %d; sha256 %s' % (
        stats['modo'], len(P['itens']), c['C'], c['E'], info['aplicadas'], info['mantidas'],
        sum(1 for l in ('itens', 'lotes', 'simulados', 'discursivas') for o in P[l] if 'interno' in o), stats['size'], stats['sha256_pacote']))
    print('cobertura:', info['cobertura'])
    print('L2-R16:', info['l2r16'])


if __name__ == '__main__':
    try:
        main()
    except T.Falha as e:
        print('FALHA:', e)
        sys.exit(1)
