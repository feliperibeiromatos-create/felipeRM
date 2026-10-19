# -*- coding: utf-8 -*-
"""T-108 e T-109 (gerador_v1_11, seção 1.8 da D1) — passo 3: gera out/registro_adendo3.md, o texto do adendo 3 ao registro GBQ v3 (L2-R16: itemEdital P2-2.8 -> P2-3.1, ato ATO_L2R16;
remissão à limpeza da T-108: tabelas e SHA, contagem de itens AUTORAL com justificativa editada, arquivo do registro por id). Nenhum item novo. Os adendos 1 e 2 ficam como histórico.
Na geração final o arquivo é promovido a saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo3_<data>.md; no ensaio fica em out/."""
import collections, json, os
from common import OUT
import config_v111 as cfg

st = json.load(open(os.path.join(OUT, 'stats_%s.json' % cfg.TAG), encoding='utf-8'))
P = json.load(open(os.path.join(OUT, 'pacote.json'), encoding='utf-8'))
aut_just = [i['id'] for i in P['itens'] if i['rotulo'] == 'AUTORAL' and any(r['campo'] == 'justificativa' for r in i.get('interno', []))]
n_edicoes = sum(len(o.get('interno', [])) for l in ('itens', 'lotes', 'simulados', 'discursivas') for o in P[l])
L = []; w = L.append
w('# claude_GBQ_Registro_AUTORAL_v3_adendo3_%s.md — T-108 e T-109 — %s — gerado por gbq-gerencia' % (cfg.GERADO_EM, cfg.GERADO_EM))
w('# GBQ — REGISTRO DE ITENS AUTORAL — v3, ADENDO 3: troca do itemEdital do L2-R16 e remissão à limpeza do pacote.json (%s)' % cfg.GERADO_EM)
w('Emitido pela GBQ (D1, saida/pacote/T108_D1_pacote_M2_2026-10-18.md, seção 1.8). Acrescenta ao registro v3, ao adendo 1 e ao adendo 2 (que ficam intactos) a troca abaixo e a remissão à limpeza. Nenhum item novo entra neste adendo.')
w('Texto gerado por saida/pacote/gerador_%s/registro_adendo_v111.py (modo %s).' % (cfg.TAG, st['modo']))
w('')
w('## 1. Troca de itemEdital (T-109)')
if st['l2r16']:
    w('| Item | Campo | Antes | Depois | Ato | Fonte |')
    w('|---|---|---|---|---|---|')
    w('| L2-R16 | itemEdital | P2-2.8 | P2-3.1 | %s | %s (seção 2, SHA-256 %s) |' % (cfg.ATO_L2R16 or 'PENDENTE (gatilho D da GCE, T-109)', cfg.T109[0], st['t109']['sha256']))
    w('Os demais campos do L2-R16 (enunciado, gabarito E, justificativa limpa pela tabela, aderência direta, comando, textoBase, url) são os da v1.10 com a limpeza aplicada. O L2-R17 continua em P2-2.8. O L2-R16 não figura em SIM-0, SIM-1, SIM-2 nem SIM-0-P2.')
else:
    w('Sem troca (E_L2R16 falso): o L2-R16 continua em P2-2.8.')
w('')
w('## 2. Limpeza do pacote.json (T-108)')
w('Alvo %s (D-V15-C-M2). Texto-base: o pacote.json v1.10 (commit %s, SHA-256 %s). As edições literais constam do campo `interno` de cada objeto e do registro de alterações por id (saida/pacote/registro_alteracoes_%s.csv).' % (cfg.ALVO, cfg.BASE[0], cfg.BASE[2], cfg.TAG))
w('')
w('| Tabela | Gerência | SHA-256 |')
w('|---|---|---|')
for t in st['tabelas']:
    w('| %s | %s | %s |' % (t['arquivo'], t['gerencia'], t['sha256']))
w('')
w('- Edições aplicadas (SUBSTITUIR ou DELETAR): %d; linhas MANTER: %d.' % (st['edicoes_aplicadas'], st['linhas_manter']))
w('- Itens AUTORAL com a justificativa editada: %d.' % len(aut_just))
w('- Por Gerência (linhas das tabelas): %s.' % ', '.join('%s %d' % kv for kv in sorted(st['por_gerencia'].items())))
w('- Ocorrências do inventário (T108_ocorrencias.csv, SHA-256 %s): universo %d, FP-R1 %d e FP-CONTEUDO %d fora de qualquer linha.' % (st['ocorrencias']['sha256'], st['cobertura']['universo'], cfg.FP_R1, cfg.FP_CONTEUDO))
w('')
w('## 3. Itens AUTORAL com justificativa editada (ids)')
w(', '.join(aut_just))
open(os.path.join(OUT, 'registro_adendo3.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
print('registro_adendo3.md: %d linhas; %d itens AUTORAL com justificativa editada; %d edições' % (len(L), len(aut_just), n_edicoes))
