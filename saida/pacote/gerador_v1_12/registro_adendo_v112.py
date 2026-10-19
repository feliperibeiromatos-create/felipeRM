# -*- coding: utf-8 -*-
"""T-115 (gerador_v1_12, D1 da GBQ, seção 6) — passo 3: gera out/registro_adendo4.md, o texto do adendo 4 ao registro GBQ v3 (e aos adendos 1 a 3, que ficam intactos): os 189 itens novos —
fontes (arquivo, ids, SHA-256 LF, ato), totais por grupo (n, C, E, [TS], VOLÁTIL, PARCIAL, aptos a final), formatos com as reclassificações da seção 3.4, ids vagos (não reutilizáveis) e diferidos (id
mantido, fora do pacote), regras R1 (VOLÁTIL, 32 ids), R4-b (PARCIAL, 6 ids) e R6 (conferência de base), restrições de montagem (seção 3.9) e identificadores L4-Rnn reservados de L4-R08 em diante à T-99.
Não reproduz enunciados. Na promoção (ato separado, depois do aceite) vai a saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo4_<data>.md; no ensaio fica em out/."""
import collections, json, os, re
from common import OUT
import config_v112 as cfg
import reforco_v112 as R
import fontes_v112 as F
from fontes_v112 import Falha

st = json.load(open(os.path.join(OUT, 'stats_%s.json' % cfg.TAG), encoding='utf-8'))
P = json.load(open(os.path.join(OUT, 'pacote.json'), encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
base_ids = {i['id'] for i in P['itens'][:cfg.BASE_ITENS]}
itens, meta, info = R.carrega(base_ids)      # releitura dos arquivos finais (mesmos SHA-256 LF); o adendo descreve o lido
por_id = {i['id']: i for i in P['itens']}
fmt = {k: m['formato'] for k, m in meta.items()}
fmt_mapa = dict(fmt)
for k, v in cfg.FORMATO_ADENDO.items():
    fmt[k] = v

L = []; w = L.append
w('# claude_GBQ_Registro_AUTORAL_v3_adendo4_%s.md — T-115 — %s — gerado por gbq-csc (registro_adendo_v112.py)' % (cfg.GERADO_EM, cfg.GERADO_EM))
w('# GBQ — REGISTRO DE ITENS AUTORAL — v3, ADENDO 4: onda 4 do reforço e onda 1 da ORDEM_V15_F (%s)' % cfg.GERADO_EM)
w('Texto do adendo 4 ao registro v3, aos adendos 1 a 3 (intactos). Base: D1 da GBQ, %s, seção 6. Pacote v%s, modo %s. Não reproduz enunciados: os textos estão nos arquivos finais abaixo.' % (cfg.D1_ARQUIVO, cfg.VERSAO, st['modo']))
w('')
w('## 1. Fontes (arquivo final, ids, SHA-256 do conteúdo LF, ato)')
w('| Grupo | Arquivo | Ids | n | SHA-256 (LF) | Ato |')
w('|---|---|---|--:|---|---|')
for gk, g in cfg.GRUPOS.items():
    for rel in g['arquivos']:
        ids = [i for i, m in meta.items() if m['arquivo'] == rel]
        w('| %s | %s | %s a %s | %d | %s | %s |' % (gk, rel, ids[0], ids[-1], len(ids), cfg.SHA[rel], g['ato']))
w('')
w('## 2. Totais por grupo')
w('| Grupo | n | C | E | [TS] | VOLÁTEIS | PARCIAIS | Aptos a final (não VOLÁTIL e não PARCIAL) |')
w('|---|--:|--:|--:|--:|--:|--:|--:|')
APTOS = {'ONDA4': 71, 'F1P1': 7, 'F1P2': 76}
for gk in cfg.GRUPOS:
    ids = [i for i, m in meta.items() if m['grupo'] == gk]
    c = collections.Counter(meta[i]['gab'] for i in ids)
    nv = [i for i in ids if meta[i]['volatil']]; npar = [i for i in ids if meta[i]['aderencia'] == 'parcial']
    ap = [i for i in ids if i not in nv and i not in npar]
    if len(ap) != APTOS[gk]:
        raise Falha('C-N1', 'aptos a final de %s: %d (a D1 diz %d)' % (gk, len(ap), APTOS[gk]))
    w('| %s | %d | %d | %d | %d | %d | %d | %d |' % (gk, len(ids), c['C'], c['E'], sum(1 for i in ids if meta[i]['ts']), len(nv), len(npar), len(ap)))
tot = len(meta)
w('| Total | %d | %d | %d | %d | %d | %d | %d |' % (tot, sum(1 for m in meta.values() if m['gab'] == 'C'), sum(1 for m in meta.values() if m['gab'] == 'E'), sum(1 for m in meta.values() if m['ts']),
                                                  sum(1 for m in meta.values() if m['volatil']), sum(1 for m in meta.values() if m['aderencia'] == 'parcial'), sum(APTOS.values())))
w('')
w('Onda 4: 84 itens, 71 aptos a final (fora os 13 que são VOLÁTEIS ou PARCIAIS: 10 + 6 − 3 que são as duas coisas, L3-R12, L3-R13 e L3-R14). Onda 1 da ORDEM_V15_F, P1: 7 itens, 7 aptos. P2: 98 itens, 76 aptos (22 VOLÁTEIS).')
w('')
w('## 3. Formatos (a coluna formato do MAPA, com as reclassificações da D1, seção 3.4, que prevalecem sobre o MAPA: reconciliação GCE, 4.3)')
for gk in cfg.GRUPOS:
    ids = [i for i, m in meta.items() if m['grupo'] == gk]
    c = collections.Counter(fmt[i] for i in ids)
    w('- %s: %s.' % (gk, '; '.join('%s %d' % (k, v) for k, v in sorted(c.items()))))
w('- Reclassificações (MAPA → adendo): %s.' % '; '.join('%s: %s → %s' % (k, fmt_mapa[k], v) for k, v in cfg.FORMATO_ADENDO.items()))
w('')
w('## 4. Ids vagos e diferidos (F1, P2)')
w('- Vagos (não reutilizáveis; fora do pacote): %s.' % ', '.join(info['vagos']))
w('- Diferidos (id mantido; fora do pacote): %s. Entram na T-11 só quando consolidados.' % ', '.join(info['diferidos']))
w('- Identificadores L4-Rnn reservados de L4-R08 em diante à T-99 (onda 5).')
w('')
w('## 5. Regras')
vol = [i for i, m in meta.items() if m['volatil']]
par = [i for i, m in meta.items() if m['aderencia'] == 'parcial']
resto = [i for i in meta if i not in vol]
w('- R1 (VOLÁTIL; inaptos a simulado final até a reverificação de 4–8/1/2027; reabertura obrigatória da URL): %d ids: %s.' % (len(vol), ', '.join(vol)))
w('- R4-b (aderência PARCIAL; só simulado diagnóstico, D-ADERENCIA): %d ids: %s. O L3-R53 é só diagnóstico; o L3-R95 pode agrupar com a 4.1.' % (len(par), ', '.join(par)))
w('- R6 (conferência de base em janeiro de 2027, sem efeito de VOLÁTIL): os demais %d itens.' % len(resto))
w('')
w('## 6. Restrições de montagem (D1, seção 3.9)')
w('- As 11 proximidades da seção 4 da T98_reconciliacao (saida/gce/T98_reconciliacao_2026-10-18.md): não no mesmo simulado ou caderno.')
w('- L4-R04 e L4-R06: mesma moldura final; não no mesmo simulado sem variar a abertura.')
w('- L1-R136: pista de raiz "di-"/"tri-", sem veredito; evitar em simulado final.')
w('- Os 6 PARCIAIS da onda 4 só em diagnóstico (L3-R95 pode agrupar com a 4.1).')
w('- Nenhum dos 189 em simulado final enquanto tiver QA PENDENTE; os 32 VOLÁTEIS nunca antes da reverificação.')
w('- L4-11 e o item 81 do TRF6 seguem fora do mesmo simulado (conferência C-S).')
w('- Nenhum dos 189 itens entra em simulado nesta versão (composição dos simulados inalterada).')
w('')
w('## 7. Erratas e URL (dado canônico; ficam no registro de alterações por id, não no `interno`)')
for e in st['erratas']:
    w('- %s: enunciado de %s (formato no adendo: %s).' % (e['edicao'], e['item'], cfg.FORMATO_ADENDO[e['item']]))
for u in st['urls']:
    w('- %s: URL do compilado da LGPD em %s, %d ocorrência(s) no arquivo %s (base, fora do pacote; vai à T-11).' % (u['edicao'], u['item'], u['ocorrencias'], u['arquivo']))
w('')
w('## 8. Itens por folha (ids)')
for f_ in sorted({m['folha'] for m in meta.values()}, key=lambda s: (s[:2], [int(x) for x in s[3:].split('.')])):
    ids = [i for i, m in meta.items() if m['folha'] == f_]
    w('- %s (%d): %s' % (f_, len(ids), ', '.join(ids)))
open(os.path.join(OUT, 'registro_adendo4.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
print('registro_adendo4.md: %d linhas; %d itens; VOLÁTEIS %d; PARCIAIS %d' % (len(L), tot, len(vol), len(par)))
