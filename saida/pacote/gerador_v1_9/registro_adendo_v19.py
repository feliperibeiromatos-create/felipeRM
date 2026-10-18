# -*- coding: utf-8 -*-
"""T-94 — gera out/registro_adendo1.md, o texto do adendo 1 ao registro GBQ v3 (onda 1 do reforço), a partir de out/stats_v19.json e out/pacote.json.
O arquivo promovido é saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo1_2026-10-18.md (D1 da GBQ, T94_D1_v1_9_2026-10-18.md, seção 2); validate_v19.py confere que ele é idêntico a esta saída."""
import collections, json, os
from common import OUT

st = json.load(open(os.path.join(OUT, 'stats_v19.json'), encoding='utf-8'))
m = st['reforco']
p = json.load(open(os.path.join(OUT, 'pacote.json'), encoding='utf-8'))
cnt = collections.Counter(i['itemEdital'] for i in p['itens'])
cnt18 = collections.Counter(i['itemEdital'] for i in p['itens'][:286])
L = []; w = L.append
w('# claude_GBQ_Registro_AUTORAL_v3_adendo1_2026-10-18.md — T-94 — 2026-10-18 — gerado por gbq-gerencia')
w('# GBQ — REGISTRO DE ITENS AUTORAL — v3, ADENDO 1: onda 1 do reforço (18/10/2026)')
w('Emitido pela GBQ (D1, saida/pacote/T94_D1_v1_9_2026-10-18.md, seção 2). Acrescenta ao registro v3 (claude_GBQ_Registro_AUTORAL_v3.md, que fica intacto) os 48 itens AUTORAL da onda 1 do reforço aceitos como canônicos (D-T89-R1-ACEITE, D-T90-R2-ACEITE, D-T91-R3-ACEITE, D-T92-R4-PARCIAL). Registro vigente = v3 + este adendo.')
w('Não reproduz enunciados; só metadados para montagem, conferência e calibração. O texto e o gabarito comentado estão nos arquivos de origem. Texto gerado por saida/pacote/gerador_v1_9/registro_adendo_v19.py.')
w('')
w('## Fontes (versões finais aceitas; SHA-256 do conteúdo LF)')
w('| Lote | Arquivo de origem | Ids | SHA-256 | Decisão de aceite |')
w('|---|---|---|---|---|')
dec = {'L1': 'D-T89-R1-ACEITE', 'L2': 'D-T90-R2-ACEITE', 'L3': 'D-T91-R3-ACEITE', 'L6A': 'D-T92-R4-PARCIAL'}
ids = {'L1': 'L1-R01–L1-R18', 'L2': 'L2-R01–L2-R18', 'L3': 'L3-R01–L3-R11', 'L6A': 'L6A-R01'}
for k, v in st['arquivos'].items():
    w('| %s | %s | %s | %s | %s |' % (k, v['arquivo'], ids[k], v['sha256'], dec[k]))
w('Correção de registro que prevalece: ponto de julgamento de L1-R10 e L1-R16 = o VIGENTE da seção 4 de saida/gce/T89_reconciliacao_2026-10-18.md (D-T89-R1-ACEITE); a coluna do mapa do v2 fica superada. Itens, gabaritos e (d)/(d-G) não mudam.')
w('L6B-R01 e L6B-R02 (T-102) não entram: SUSPENSOS, sem texto nem gabarito (D-T92-R4-PARCIAL).')
w('')
w('## Regras de elegibilidade acrescentadas (GBQ, D1)')
w('- R4-b. A regra R4 do v3 ("os AUTORAL são de aderência direta por construção") passa a valer com uma exceção: item de reforço que a decisão de aceite declare de aderência PARCIAL. Hoje: L2-R02, L2-R14, L2-R15, L3-R01, L3-R02, L3-R05. Só simulado diagnóstico (D-ADERENCIA).')
w('- R1 (VOLÁTIL) vale para L2-R07 (baixo) e L2-R18 (ALTO): só simulado diagnóstico até a reverificação de 4–8/1/2027.')
w('- R6. Conferência de base na janela de 4–8/1/2027, sem efeito de VOLÁTIL (D-T89-R1-ACEITE, critério de VOLÁTIL; D-T90-R2-ACEITE; D-T92-R4-PARCIAL): L1-R03, R04, R11, R16, R17, R18; L2-R03, R04, R09, R10, R11, R12, R13, R17; L6A-R01 (fila da T-11). Não afasta o item de simulado final.')
w('- Núcleo (D-REFORCO-2): o campo "nucleo" não é atribuído neste adendo (D1 da GBQ, T94_D1, seção 4).')
w('- Identificadores: L1-Rnn, L2-Rnn, L3-Rnn, L6A-Rnn (L6B-Rnn reservados).')
w('')
w('## Totais')
w('| Lote | Itens | C | E | [TS] | VOLÁTIL | Parcial | Aptos a final |')
w('|---|---|---|---|---|---|---|---|')
T = [0] * 7
for lote in ('L1', 'L2', 'L3', 'L6A'):
    xs = [(k, v) for k, v in m.items() if v['lote'] == lote]
    n = len(xs); c = sum(v['gab'] == 'C' for k, v in xs); ts = sum(v['ts'] for k, v in xs)
    vol = [k for k, v in xs if v['volatil']]; par = [k for k, v in xs if v['aderencia'] == 'parcial']
    apt = sum(1 for k, v in xs if not v['volatil'] and v['aderencia'] == 'direta')
    w('| %s | %d | %d | %d | %d | %s | %s | %d |' % (lote, n, c, n - c, ts, ('%d (%s)' % (len(vol), ', '.join(vol))) if vol else '0',
                                                   ('%d (%s)' % (len(par), ', '.join(par))) if par else '0', apt))
    for i, x in enumerate((n, c, n - c, ts, len(vol), len(par), apt)):
        T[i] += x
w('| TOTAL | %d | %d | %d | %d | %d | %d | %d |' % tuple(T))
w('Gabarito da onda 1: %d C / %d E (%s%% de C; faixa de 40%% a 60%%, D-REFORCO-2, regra 5; conferida pelo gbq-estilo em saida/banco/estilo_onda_1.md). Contagens conferidas por script (gerador_v1_9/validate_v19.py) contra os arquivos de origem e as decisões de aceite.'
  % (T[1], T[2], ('%.1f' % (100 * T[1] / T[0])).replace('.', ',')))
w('')
w('## Itens por folha (v1.8 → v1.9; todos os itens do pacote, banco e AUTORAL)')
w('| Folha | v1.8 | + reforço | v1.9 |')
w('|---|---|---|---|')
for f in sorted({v['folha'] for v in m.values()}, key=lambda s: (s[:2], [int(x) for x in s[3:].split('.')])):
    w('| %s | %d | %d | %d |' % (f, cnt18[f], cnt[f] - cnt18[f], cnt[f]))
w('')
w('## Itens')
w('| ID | Gab | Folha | [TS] | Marca | Aderência | Formato | Ponto de julgamento |')
w('|---|---|---|---|---|---|---|---|')
for k, v in m.items():
    w('| %s | %s | %s | %s | %s | %s | %s | %s |' % (k, v['gab'], v['folha'], 'TS' if v['ts'] else '', 'VOLÁTIL' if v['volatil'] else '', v['aderencia'],
                                               v['formato'], v['ponto'].replace('|', '/')))
w('Formato e ponto de julgamento: colunas do mapa (Parte 1) do arquivo de origem, literais (siglas do L2: SH situação hipotética, PC par confundível, TS troca de sujeito, NP número ou prazo, AP aplicação parlamentar, D definição). L1-R10 e L1-R16: ponto VIGENTE da T89_reconciliacao, seção 4.')
open(os.path.join(OUT, 'registro_adendo1.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
print('registro_adendo1.md: %d linhas, %d itens' % (len(L), len(m)))
