# -*- coding: utf-8 -*-
"""T-115 (gerador_v1_12, D1 da GBQ, seção 3.7) — `topicos` (ORDEM_V15_A e ORDEM_V15_E). Bloco json único de cada arquivo; nos da GCE o objeto vem sob a chave "topicos" (desembrulhar), nos da GCB vem direto.
Resumos: T111_resumos_P1_parte1 (P1-8.2), parte2 (16), T111_resumos_P2_A1 (2) e A2 a A4 (7 cada): 40 chaves únicas, cada uma só com `resumo`. Piloto: P1-8.2 (GCB), P2-1.4 e P2-2.5 (GCE), cada um só
com `emUmMinuto` e `visuais`. Fusão por chave: {resumo, emUmMinuto, visuais} nesta ordem. Objeto final: chaves na ordem de `edital[].id`. As regras da errata de forma v1.2.9, ponto 1, são conferidas aqui
(`valida_topicos`); as regras de tamanho de cada Gerência (D1 da GBQ, 2.3) são só medidas (informativas). Não lê relógio."""
import collections, re
import fontes_v112 as F
from fontes_v112 import Falha
import config_v112 as cfg

RESUMOS = [('saida/gcb/T111_resumos_P1_parte1_v2.md', False), ('saida/gcb/T111_resumos_P1_parte2_v2.md', False), ('saida/gce/T111_resumos_P2_A1_v2_GCE.md', True),
           ('saida/gce/T111_resumos_P2_A2_v2.md', True), ('saida/gce/T111_resumos_P2_A3_v2.md', True), ('saida/gce/T111_resumos_P2_A4_v2.md', True)]
PILOTOS = [('saida/gcb/T112_piloto_P1-8.2_v2.md', False), ('saida/gce/T112_piloto_visual_P2_v2.md', True)]
TIPOS = {'fluxo': (['titulo', 'passos'], []), 'tabela': (['titulo', 'colunas', 'linhas'], ['legenda']), 'linha': (['titulo', 'marcos'], []), 'esquema': (['titulo', 'centro', 'ramos'], []),
         'barras': (['titulo', 'dados', 'unidade', 'fonte'], [])}      # tipo -> (campos obrigatórios, opcionais)


def le_blocos(lista):
    out = collections.OrderedDict()
    for rel, gce in lista:
        t = F.le_insumo(rel)
        d = F.bloco_json(t, rel)
        if gce:
            if list(d) != ['topicos']:
                raise Falha('C-T', '%s: chaves de topo %s (esperado ["topicos"])' % (rel, list(d)))
            d = d['topicos']
        for k, v in d.items():
            if k in out:
                raise Falha('C-T', '%s: chave %s repetida' % (rel, k))
            out[k] = (v, rel)
    return out


def monta(edital_ids):
    """-> (topicos OrderedDict, fontes {chave: [arquivos]})."""
    res = le_blocos(RESUMOS)
    pil = le_blocos(PILOTOS)
    for k, (v, rel) in res.items():
        if list(v) != ['resumo']:
            raise Falha('C-T', '%s: %s com campos %s (esperado só "resumo")' % (rel, k, list(v)))
    for k, (v, rel) in pil.items():
        if list(v) != ['emUmMinuto', 'visuais']:
            raise Falha('C-T', '%s: %s com campos %s (esperado "emUmMinuto" e "visuais")' % (rel, k, list(v)))
    n1 = sum(1 for k in res if k.startswith('P1-'))
    n2 = sum(1 for k in res if k.startswith('P2-'))
    if (len(res), n1, n2) != (cfg.TOTAIS['topicos'], cfg.TOPICOS_P1, cfg.TOPICOS_P2):
        raise Falha('C-T', 'resumos: %d chaves (P1 %d, P2 %d); esperado 40 (17 e 23)' % (len(res), n1, n2))
    if sorted(pil) != sorted(cfg.PILOTOS) or not set(pil) <= set(res):
        raise Falha('C-T', 'pilotos %s (esperado %s, todos com resumo)' % (sorted(pil), cfg.PILOTOS))
    desc = [k for k in res if k not in edital_ids]
    if desc:
        raise Falha('C-T', 'chave(s) fora do edital: %s' % desc)
    topicos = collections.OrderedDict()
    fontes = {}
    for k in edital_ids:
        if k in res:
            e = collections.OrderedDict([('resumo', res[k][0]['resumo'])])
            fontes[k] = [res[k][1]]
            if k in pil:
                e['emUmMinuto'] = pil[k][0]['emUmMinuto']
                e['visuais'] = pil[k][0]['visuais']
                fontes[k].append(pil[k][1])
            topicos[k] = e
    return topicos, fontes


def valida_topicos(topicos, edital_ids):
    """Regras do contrato v1.2.9, ponto 1. Devolve a lista de violações (vazia = ok)."""
    v = []
    if list(topicos) != [k for k in edital_ids if k in topicos]:
        v.append('chaves fora da ordem do edital')
    for k, e in topicos.items():
        if list(e) not in (['resumo'], ['resumo', 'emUmMinuto', 'visuais']):
            v.append('%s: campos %s' % (k, list(e))); continue
        if not isinstance(e['resumo'], str) or not e['resumo'].strip():
            v.append('%s: resumo vazio' % k)
        else:
            for p in e['resumo'].split('\n\n'):
                if not p.strip() or p != p.strip():
                    v.append('%s: parágrafo vazio ou com espaço nas pontas' % k)
                elif re.match(r'^(\d|[-*•]\s|[A-ZÀ-Ú]{2,}[A-ZÀ-Ú \-/]*:)', p):
                    v.append('%s: parágrafo começa com algarismo, marca de lista ou RÓTULO: %r' % (k, p[:30]))
        if 'emUmMinuto' in e:
            if not (isinstance(e['emUmMinuto'], list) and len(e['emUmMinuto']) == 3 and all(isinstance(x, str) and x.strip() for x in e['emUmMinuto'])):
                v.append('%s: emUmMinuto não é lista de 3 strings não vazias' % k)
            vis = e['visuais']
            if not (isinstance(vis, list) and vis):
                v.append('%s: visuais vazio' % k); continue
            for j, o in enumerate(vis):
                t = o.get('tipo') if isinstance(o, dict) else None
                if t not in TIPOS:
                    v.append('%s: visual %d com tipo %r' % (k, j, t)); continue
                if not set(o) <= {'tipo'} | set(TIPOS[t][0]) | set(TIPOS[t][1]) or any(c not in o for c in TIPOS[t][0]):
                    v.append('%s: visual %d (%s) com campos %s' % (k, j, t, list(o)))
                    continue
                if t == 'fluxo' and not (3 <= len(o['passos']) <= 7 and all(isinstance(s, str) and 0 < len(s) <= 48 for s in o['passos'])):
                    v.append('%s: fluxo com passos fora de 3–7 ou de 48 caracteres' % k)
                if t == 'tabela' and not (len(o['colunas']) >= 2 and o['linhas'] and all(len(r) == len(o['colunas']) for r in o['linhas'])):
                    v.append('%s: tabela com linhas diferentes das colunas' % k)
                if t == 'linha' and not (len(o['marcos']) >= 2 and all(list(m) == ['quando', 'texto'] for m in o['marcos'])):
                    v.append('%s: linha com marcos fora do formato' % k)
                if t == 'esquema' and not (len(o['ramos']) >= 2):
                    v.append('%s: esquema com menos de 2 ramos' % k)
                if t == 'barras':
                    if not (len(o['dados']) >= 2 and all(isinstance(d.get('valor'), (int, float)) and d['valor'] >= 0 for d in o['dados']) and re.search(r'\d{2}/\d{2}/\d{4}', o['fonte'])):
                        v.append('%s: barras fora do formato' % k)
    return v


def medidas(topicos, cursos):
    """Informativo: palavras do resumo, parágrafos e razão ao curso do tópico (curso do lote); regras de tamanho das Gerências (D1, 2.3)."""
    out = {}
    for k, e in topicos.items():
        ps = e['resumo'].split('\n\n')
        w = [len(p.split()) for p in ps]
        out[k] = dict(palavras=sum(w), paragrafos=len(ps), max_par=max(w), min_par=min(w))
    return out
