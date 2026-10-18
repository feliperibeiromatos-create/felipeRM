# -*- coding: utf-8 -*-
"""T-94 — gerador do pacote.json v1.9 (ocorrência da T-12; D-REFORCO-1). Passo 1 do rodar_tudo.sh da v1_9; substitui, neste passo, o build_pacote.py herdado da v1_8.
Base: o pacote.json v1.8 ACEITO (D-PACOTE-V18), lido do git no commit C_V18 (refs.py) e conferido pelo SHA-256 aceito; nenhum item, lote, simulado, discursiva ou entrada de edital
da v1.8 é regenerado nem tocado (T-94: "sem mudar item existente"; D1 da GBQ, saida/pacote/T94_D1_v1_9_2026-10-18.md, seção 1).
Mudanças: `geradoEm` "2026-10-18"; `nome` "… (v1.9)"; os 48 itens da onda 1 do reforço (reforco.py) acrescentados ao FIM da lista `itens`, na ordem L1-R, L2-R, L3-R, L6A-R.
Saídas: out/pacote.json e out/stats_v19.json. Não lê relógio; não toca o repositório."""
import collections, hashlib, json, os
from common import OUT
import refs, reforco

SHA_V18 = '09d4a457612781275659a3f7fbfd3a182f20fd9d4003e5ba38007d0c26c7a9c0'
GERADO_EM = '2026-10-18'
NOME = 'Câmara 2026 — pacote F4 (v1.9)'

os.makedirs(OUT, exist_ok=True)
raw18 = refs.git_show(refs.C_V18, refs.PACOTE)
assert hashlib.sha256(raw18).hexdigest() == SHA_V18, 'base v1.8 do git com SHA-256 diferente do aceito'
P = json.loads(raw18.decode('utf-8'), object_pairs_hook=collections.OrderedDict)
assert json.dumps(P, ensure_ascii=False, indent=1) + '\n' == raw18.decode('utf-8'), 'base v1.8 não é a serialização canônica'
assert len(P['itens']) == 286 and P['nome'] == 'Câmara 2026 — pacote F4 (v1.8)' and P['geradoEm'] == '2026-10-17'

novos, meta = reforco.carrega()
ids18 = {i['id'] for i in P['itens']}
assert not ids18 & {i['id'] for i in novos}, 'id do reforço já existe na v1.8'

P['geradoEm'] = GERADO_EM
P['nome'] = NOME
P['itens'] = P['itens'] + novos
txt = json.dumps(P, ensure_ascii=False, indent=1) + '\n'
with open(os.path.join(OUT, 'pacote.json'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(txt)
stats = collections.OrderedDict(base=dict(commit=refs.C_V18, sha256=SHA_V18, itens=286), reforco=meta, log=reforco.LOG,
                                arquivos={k: dict(arquivo=v[0], sha256=v[1]) for k, v in reforco.ARQ.items()}, size=len(txt.encode('utf-8')))
with open(os.path.join(OUT, 'stats_v19.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump(stats, f, ensure_ascii=False, indent=1)
    f.write('\n')
c = collections.Counter(i['gabarito'] for i in P['itens'])
print('itens', len(P['itens']), '(286 da v1.8 + %d do reforço)' % len(novos), 'C/E %d/%d' % (c['C'], c['E']), 'volatil', sum(1 for i in P['itens'] if i.get('volatil')),
      'bytes', len(txt.encode('utf-8')), 'sha256', hashlib.sha256(txt.encode('utf-8')).hexdigest())
print('LOG:', reforco.LOG)
