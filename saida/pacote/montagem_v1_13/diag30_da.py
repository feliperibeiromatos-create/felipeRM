# diag30_da.py — lista do diagnóstico de 30 itens de Direito Administrativo (critério do orquestrador, revisável pelo Fundador)
# Critério: itens não voláteis, aderência direta, fora de simulado; ao menos 1 por item do edital (1 a 12); folhas por item
# do edital na proporção do nº de folhas (round(k*30/37), mínimo 1, item 10 com 5); dentro do item, folhas com mais itens primeiro;
# dentro da folha, o primeiro id cujo gabarito equilibra C/E (meta 15/15).
import json, pathlib, collections
R = pathlib.Path(__file__).resolve().parents[3]
p = json.loads((pathlib.Path(__file__).parent/'out/pacote.json').read_text(encoding='utf-8'))
sim = {i for s in p['simulados'] for i in s['itens']}
da = [i for i in p['itens'] if i['itemEdital'].startswith('P1-DA-') and not i.get('volatil') and i['aderencia'] == 'direta' and i['id'] not in sim]
folhas = collections.defaultdict(list)
for i in da: folhas[i['itemEdital']].append(i)
edital = [e['id'] for e in p['edital'] if e['id'].startswith('P1-DA-')]
folha_ids = [e for e in edital if not any(x.startswith(e + '.') for x in edital)]   # sem subitens
por_item = collections.OrderedDict()
for f in folha_ids: por_item.setdefault(f.split('-')[2].split('.')[0], []).append(f)
cota = {k: max(1, round(len(v) * 30 / 37)) for k, v in por_item.items()}; cota['10'] = 5
assert sum(cota.values()) == 30, cota
esc, c = [], 0
for k, fs in por_item.items():
    for f in sorted(fs, key=lambda f: (-len(folhas[f]), edital.index(f)))[:cota[k]]:
        quer = 'C' if c < len(esc) - c or (c == len(esc) - c) else 'E'
        cand = sorted(folhas[f], key=lambda i: (i['gabarito'] != quer, int(i['id'].split('-')[1]), i['id']))
        esc.append(cand[0]); c += cand[0]['gabarito'] == 'C'
ids = [i['id'] for i in esc]
assert len(ids) == 30 and len(set(ids)) == 30
out = {'ids': ids, 'C': c, 'E': 30 - c, 'folhas': [i['itemEdital'] for i in esc], 'cota_por_item_do_edital': cota}
(pathlib.Path(__file__).parent/'out/diag30_DA.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
print(json.dumps(out, ensure_ascii=False))
