# -*- coding: utf-8 -*-
"""T-104 (v1.10) — edição do estudante em .md (out/estudante/), D1 da GBQ, saida/pacote/T104_D1_v1_10_2026-10-18.md, seção 4 (D-RT94-02: a edição .md recebe o reforço na v1.10).
Base: os 34 arquivos da edição v1.8 (git C_V18:saida/estudante; manifesto 0b7391fa…), sem regeneração a partir das fontes. Mudanças, e só elas:
  (1) as trocas da v1.10 já feitas no pacote_estudante.json, por substituição exata de 1 ocorrência: L5_gabarito.md (a1, 5C-08), L2_estudo.md (a2; e2 se config.E_CURSO),
      DISCURSIVAS_padrao.md (e1 se config.E_PADRAO);
  (2) ao FIM de L1, L2, L3, L6A e L6B _itens.md e _gabarito.md, uma seção "## Itens de reforço" com os itens de reforço do lote (onda 1 e v1.10), na ordem do pacote,
      no mesmo formato de bloco dos itens da edição (comando próprio só quando difere de "Julgue o item."; aviso fixo de VOLÁTIL; "(aderência: parcial)" como no BANCO_gabarito.md),
      com o texto do pacote_estudante.json (só deleções);
  (3) arquivo novo NUCLEO.md: por folha, os ids com "nucleo" true no pacote_estudante.json, e o critério;
  (4) README.md: versão, data e as linhas de NUCLEO.md e da seção de reforço.
Falha (sys.exit(1)) se qualquer troca não tiver exatamente 1 ocorrência ou se o resto dos 34 arquivos diferir da v1.8."""
import collections, json, os, shutil, sys
import refs, config_v110 as cfg, build_v110 as B

HERE = os.path.dirname(os.path.abspath(__file__))
OUTE = os.path.join(HERE, 'out', 'estudante')
E = json.load(open(os.path.join(HERE, 'out', 'pacote_estudante.json'), encoding='utf-8'))
V18 = refs.estudante(refs.C_V18)
assert len(V18) == 34, len(V18)
FALHAS = []
F = dict(V18)
AVISO = '> Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.'
LOTES = {'L1': 'L1', 'L2': 'L2', 'L3': 'L3', 'L6A': 'L6A', 'L6B': 'L6B'}

# (1) trocas
alvo = {'a1': 'L5_gabarito.md', 'a2': 'L2_estudo.md', 'e1': 'DISCURSIVAS_padrao.md', 'e2': 'L2_estudo.md'}
for k in B.ATIVAS:
    _, _, _, old, new, _ = B.TROCAS[k]
    arq = alvo[k]
    if F[arq].count(old) != 1 or F[arq].count(new) != 0:
        FALHAS.append('%s: %s com %d ocorrência(s) do texto antigo' % (k, arq, F[arq].count(old)))
    F[arq] = F[arq].replace(old, new)

# (2) itens de reforço por lote
it_lote = collections.OrderedDict((l, []) for l in LOTES)
for it in E['itens']:
    if '-R' in it['id'] and it['rotulo'] == 'AUTORAL':
        it_lote[it['id'].split('-')[0]].append(it)
assert {k: len(v) for k, v in it_lote.items()} == {'L1': 130, 'L2': 129 + cfg.E_L2R131, 'L3': 11, 'L6A': 1, 'L6B': 2}, {k: len(v) for k, v in it_lote.items()}
for l, xs in it_lote.items():
    I, G = ['', '## Itens de reforço', ''], ['', '## Itens de reforço', '']
    for it in xs:
        if it['comando'] != 'Julgue o item.':
            I += ['*%s*' % it['comando'], '']
        I += ['**%s** — %s' % (it['id'], it['enunciado']), '']
        if it.get('volatil'):
            I += [AVISO, '']
        ade = ' (aderência: parcial)' if it['aderencia'] == 'parcial' else ''
        G += ['### %s — Gabarito: %s' % (it['id'], it['gabarito']), '', '- Item do edital: %s%s' % (it['itemEdital'], ade), '- Justificativa: %s' % it['justificativa'], '']
        if it.get('volatil'):
            G += [AVISO, '']
    for nome, extra in (('%s_itens.md' % l, I), ('%s_gabarito.md' % l, G)):
        base = F[nome]
        F[nome] = base.rstrip('\n') + '\n' + '\n'.join(extra).rstrip('\n') + '\n'

# (3) NUCLEO.md
pf = collections.OrderedDict()
for it in E['itens']:
    pf.setdefault(it['itemEdital'], []).append(it)
N = ['# Câmara 2026 — Núcleo de estudo por item do edital', '',
     'Em cada item do edital, os itens marcados como núcleo são os 10 primeiros pela ordem em que foram incorporados ao material (itens de provas anteriores e itens de lotes de estudo; '
     'havendo empate, os de aderência direta antes dos de aderência parcial). Item do edital com 10 itens ou menos: todos são núcleo.', '']
for f in sorted(pf, key=lambda s: (s[:2], [int(x) for x in s[3:].split('.')])):
    ids = [i['id'] for i in pf[f] if i['nucleo']]
    N.append('- %s (%d de %d): %s' % (f, len(ids), len(pf[f]), ', '.join(ids)))
F['NUCLEO.md'] = '\n'.join(N) + '\n'

# (4) README.md
r = F['README.md']
for old, new in (('- Versão: v1.8 (pacote.json versão 1)', '- Versão: v1.10 (pacote.json versão 1)'), ('- Data: 2026-10-17', '- Data: %s' % cfg.GERADO_EM)):
    if r.count(old) != 1:
        FALHAS.append('README: %r' % old)
    r = r.replace(old, new)
anc = '### Banco de itens'
if r.count(anc) != 1:
    FALHAS.append('README: âncora')
r = r.replace(anc, '- L1, L2, L3, L6A e L6B: os itens de reforço estão ao fim de cada arquivo _itens.md e _gabarito.md, na seção "Itens de reforço".\n\n'
              '### Núcleo de estudo\n\n- [NUCLEO.md](NUCLEO.md) (os 10 itens-núcleo de cada item do edital)\n\n' + anc)
F['README.md'] = r

# conferência: fora das mudanças declaradas, os 34 arquivos são os da v1.8
for nome, t in V18.items():
    novo = F[nome]
    if nome in ('L1_itens.md', 'L1_gabarito.md', 'L2_itens.md', 'L2_gabarito.md', 'L3_itens.md', 'L3_gabarito.md', 'L6A_itens.md', 'L6A_gabarito.md', 'L6B_itens.md', 'L6B_gabarito.md'):
        if not novo.startswith(t.rstrip('\n') + '\n'):
            FALHAS.append('%s: o início não é o arquivo da v1.8' % nome)
    elif nome not in [alvo[k] for k in B.ATIVAS] + ['README.md'] and novo != t:
        FALHAS.append('%s: difere da v1.8' % nome)

if os.path.isdir(OUTE):
    shutil.rmtree(OUTE)
os.makedirs(OUTE)
for nome, t in sorted(F.items()):
    with open(os.path.join(OUTE, nome), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(t)
print('edição .md v1.10 (ensaio): %d arquivos em out/estudante/ (34 da v1.8 + NUCLEO.md); trocas %s; itens de reforço por lote %s'
      % (len(F), B.ATIVAS, {k: len(v) for k, v in it_lote.items()}))
print('%d falhas' % len(FALHAS))
for f in FALHAS:
    print('FALHA:', f)
sys.exit(1 if FALHAS else 0)
