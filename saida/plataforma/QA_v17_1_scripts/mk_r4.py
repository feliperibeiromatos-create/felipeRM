import json,copy
SRC='/home/claude/plat/pacote_teste_DAv2.json'; O='/home/claude/plat/qa_r4/'
p0=json.load(open(SRC))
def item(p,i): return [x for x in p['itens'] if x['id']==i][0]
# mec5: itens extras CON e LIT no 3.4 para a opção D
p=copy.deepcopy(p0); base=item(p,'DX-05')
for k in range(11,16):
    it=copy.deepcopy(base); it['id']=f'DX-{k}'; it['numero']=k; it['enunciado']=f'Item CON de teste {k}: o deslocamento do servidor no mesmo quadro denomina-se redistribuição.'; p['itens'].append(it)
b2=item(p,'DX-01')
for k in range(21,24):
    it=copy.deepcopy(b2); it['id']=f'DX-{k}'; it['numero']=k; it['enunciado']=f'Item LIT de teste {k}: a remoção desloca o servidor no mesmo quadro.'; p['itens'].append(it)
json.dump(p,open(O+'mec5.json','w'),ensure_ascii=False)
# rob5: escopo para tópico sem curso, sem fechamento; onde inexistente; onde de outra matéria com curso
p=copy.deepcopy(p0); t=p['topicos']['P1-DA-3.4']; t.pop('fechamento',None)
t['escopo']=[{"tema":"Tópico sem curso","onde":"P1-DA-2"},{"tema":"Tópico com curso","onde":"P1-DA-4.2"},{"tema":"Inexistente","onde":"P1-DA-99"}]
json.dump(p,open(O+'rob5.json','w'),ensure_ascii=False)
# v114_caso: lote antigo (v1.14) com linhas exatas CASO / GLOSSÁRIO / RESPOSTA DO CASO inseridas num lote de TI e num de DA
q=json.load(open('/home/claude/plat/pacote_v114.json')); alvo=[]
for l in q['lotes']:
    if isinstance(l.get('curso'),str) and l['curso'] and (l['id'].startswith('D1') or 'TI' in l['id'].upper() or l['id'].startswith('T')):
        if len(alvo)<2:
            ls=l['curso'].split('\n'); k=next(i for i,x in enumerate(ls) if x.strip()=='' and i>8)
            ls[k:k]=['','CASO','Um servidor pergunta se pode. Pode?','','Parágrafo comum depois.','','GLOSSÁRIO','Termo: definição','','RESPOSTA DO CASO','Sim.','']
            l['curso']='\n'.join(ls); alvo.append((l['id'],l.get('itensEdital')))
json.dump(q,open(O+'v114_caso.json','w'),ensure_ascii=False); print('alvos',alvo)
print('lotes v114', [(l['id'], bool(l.get('curso'))) for l in q['lotes']])
