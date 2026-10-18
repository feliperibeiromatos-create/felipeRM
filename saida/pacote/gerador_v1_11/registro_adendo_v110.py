# -*- coding: utf-8 -*-
"""T-104 — gera out/registro_adendo2.md, o texto do adendo 2 ao registro GBQ v3 (L6B-R01/R02, ondas 2 e 3 e saldo L1-R131), a partir de out/stats_v110.json e out/pacote.json.
Na geração final, o arquivo é promovido a saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo2_<data>.md (D1 da GBQ, T104_D1_v1_10_2026-10-18.md, seção 2); no ensaio, fica em out/."""
import collections, json, os
from common import OUT
import config_v110 as cfg

st = json.load(open(os.path.join(OUT, 'stats_v110.json'), encoding='utf-8'))
m = st['reforco']
p = json.load(open(os.path.join(OUT, 'pacote.json'), encoding='utf-8'))
cnt = collections.Counter(i['itemEdital'] for i in p['itens'])
cnt19 = collections.Counter(i['itemEdital'] for i in p['itens'][:334])
GRUPOS = collections.OrderedDict([('L6B', 'L6B (saldo do R4 da onda 1)'), ('ONDA2', 'L1, onda 2'), ('SALDO2', 'L1, saldo da onda 2'), ('ONDA3', 'L2, onda 3'), ('SALDO3', 'L2, saldo da onda 3')])
ATO = {'L6B': 'D-T102-R4-SALDO', 'ONDA2': 'D-T96-ONDA2-ACEITE', 'SALDO2': 'D-T103-SALDO-ACEITE', 'ONDA3': 'D-T97-ONDA3-ACEITE', 'SALDO3': cfg.ATO_L2R131}
L = []; w = L.append
w('# claude_GBQ_Registro_AUTORAL_v3_adendo2_%s.md — T-104 — %s — gerado por gbq-gerencia' % (cfg.GERADO_EM, cfg.GERADO_EM))
w('# GBQ — REGISTRO DE ITENS AUTORAL — v3, ADENDO 2: L6B-R01/R02, ondas 2 e 3 do reforço e saldos L1-R131%s (%s)' % (' e L2-R131' if cfg.E_L2R131 else '', cfg.GERADO_EM))
w('Emitido pela GBQ (D1, saida/pacote/T104_D1_v1_10_2026-10-18.md, seção 2). Acrescenta ao registro v3 + adendo 1 (que ficam intactos) os %d itens AUTORAL aceitos como canônicos depois da v1.9 (%s). Registro vigente = v3 + adendo 1 + este adendo.'
  % (len(m), ', '.join(ATO[g] for g in ATO if g in st['arquivos'])))
w('Não reproduz enunciados; só metadados para montagem, conferência e calibração. Texto gerado por saida/pacote/gerador_v1_10/registro_adendo_v110.py.')
w('')
w('## Fontes (versões finais aceitas; SHA-256 do conteúdo LF)')
w('| Grupo | Arquivo de origem | Itens | SHA-256 | Decisão de aceite |')
w('|---|---|---|---|---|')
for gk, arqs in st['arquivos'].items():
    for a in arqs:
        w('| %s | %s | %d | %s | %s |' % (GRUPOS[gk], a['arquivo'], a['ids'], a['sha256'], ATO[gk]))
w('Registros que prevalecem sobre a Parte 1 dos arquivos: T96_reconciliacao_2026-10-18.md, seção 3 (L1-R99 com formato PC); T97_reconciliacao_2026-10-18.md, seções 2 a 7. L1-R43 e L2-R67 retirados (ids não reutilizados). ' + ('L2-R131 (T-105) não entra neste adendo sem aceite.' if 'SALDO3' not in st['arquivos'] else 'L2-R131 (T-105) entra com o aceite %s, em reposição ao L2-R67; a Tabela de Correções da seção 2 de saida/gce/T105_reconciliacao_2026-10-18.md prevalece sobre a Parte 1 do saldo_v2 (registro, sem efeito no item).' % cfg.ATO_L2R131))
w('')
w('## Regras de elegibilidade (GBQ, D1)')
par = [k for k, v in m.items() if v['aderencia'] == 'parcial']
vol = [k for k, v in m.items() if v['volatil']]
w('- R4-b (adendo 1) vale para os %d PARCIAIS da onda 3 (seção 3.1 da T97_reconciliacao): só simulado diagnóstico (D-ADERENCIA).' % len(par))
w('- R1 (VOLÁTIL) vale para %d itens: %s. Só simulado diagnóstico até a reverificação de 4–8/1/2027.' % (len(vol), ', '.join(vol)))
w('- R6 (adendo 1): conferência de base em 4–8/1/2027, sem efeito de VOLÁTIL, para todos os demais itens com base em página de fornecedor ou norma (T-11, partes P1 e P2).')
w('- Montagem (D2 da GBQ, a aplicar nos simulados): os pares da T97_reconciliacao, seção 6 (R23 × L2-Q03; R40 × R33; R55 × R64; R105 × L2-Q06; R108 × R115; R111 × R43; R24 × R37; R27 × L1-R37; R122 × L1-R94; R121 × L1-R120; R62 × R84)%s não figuram no mesmo simulado ou caderno.' % ('; e L2-R131 × L2-R68 (D-T105-SALDO-ACEITE; 12ª proximidade da T97_reconciliacao, seção 6)' if cfg.E_L2R131 else ''))
w('- Núcleo (D-REFORCO-2): campo "nucleo" no pacote_estudante.json, critério da D1 (seção 3); não é marca deste registro.')
w('- Identificadores: L1-Rnnn, L2-Rnnn e L6B-Rnn passam a admitir três dígitos no número (R100 a R131).')
w('')
w('## Totais')
w('| Grupo | Itens | C | E | [TS] | VOLÁTIL | Parcial | Aptos a final |')
w('|---|---|---|---|---|---|---|---|')
T = [0] * 7
for gk in [g for g in GRUPOS if g in st['arquivos']]:
    xs = [v for v in m.values() if v['grupo'] == gk]
    n = len(xs); c = sum(v['gab'] == 'C' for v in xs); ts = sum(v['ts'] for v in xs)
    nv = sum(v['volatil'] for v in xs); npar = sum(v['aderencia'] == 'parcial' for v in xs)
    apt = sum(1 for v in xs if not v['volatil'] and v['aderencia'] == 'direta')
    w('| %s | %d | %d | %d | %d | %d | %d | %d |' % (GRUPOS[gk], n, c, n - c, ts, nv, npar, apt))
    for i, x in enumerate((n, c, n - c, ts, nv, npar, apt)):
        T[i] += x
w('| TOTAL | %d | %d | %d | %d | %d | %d | %d |' % tuple(T))
w('')
w('## Itens por folha (v1.9 → v1.10; todos os itens do pacote, banco e AUTORAL)')
w('| Folha | v1.9 | + novos | v1.10 | diretas v1.10 |')
w('|---|---|---|---|---|')
dir_ = collections.Counter(i['itemEdital'] for i in p['itens'] if i['aderencia'] == 'direta')
for f in sorted({v['folha'] for v in m.values()}, key=lambda s: (s[:2], [int(x) for x in s[3:].split('.')])):
    w('| %s | %d | %d | %d | %d |' % (f, cnt19[f], cnt[f] - cnt19[f], cnt[f], dir_[f]))
w('')
w('## Itens')
w('| ID | Gab | Folha | [TS] | Marca | Aderência | Formato | Ponto de julgamento |')
w('|---|---|---|---|---|---|---|---|')
for k, v in m.items():
    w('| %s | %s | %s | %s | %s | %s | %s | %s |' % (k, v['gab'], v['folha'], 'TS' if v['ts'] else '', 'VOLÁTIL' if v['volatil'] else '', v['aderencia'],
                                               v['formato'], v['ponto'].replace('|', '/')))
w('Formato e ponto de julgamento: colunas do mapa (Parte 1) do arquivo de origem, literais (SH situação hipotética, PC par confundível, TS troca de sujeito, NP número ou prazo, AP aplicação parlamentar, D definição), salvo L1-R99 (PC, T96_reconciliacao, seção 3).')
open(os.path.join(OUT, 'registro_adendo2.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
print('registro_adendo2.md: %d linhas, %d itens' % (len(L), len(m)))
