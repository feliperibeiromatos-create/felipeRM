# HISTÓRICO (T-05): diff do pacote v1 (git 5eab2d9) para o pacote gerado em out/.
import json, collections, re, difflib, os
import refs
from common import OUT
old=refs.v1(); new=json.load(open(os.path.join(OUT,'pacote.json'),encoding='utf-8'))
print({k:(len(v) if hasattr(v,'__len__') and not isinstance(v,str) else v) for k,v in new.items()})
oi={i['id']:i for i in old['itens']}; ni={i['id']:i for i in new['itens']}
print('ids iguais', set(oi)==set(ni))
for k in sorted(set(oi)|set(ni)):
    a,b=oi.get(k),ni.get(k)
    if a!=b:
        ch=[f for f in set(a)|set(b) if a.get(f)!=b.get(f)]
        print('ITEM',k,ch)
ol={l['id']:l for l in old['lotes']}; nl={l['id']:l for l in new['lotes']}
for k in nl:
    for f in nl[k]:
        if ol[k][f]!=nl[k][f]:
            a,b=ol[k][f],nl[k][f]
            if isinstance(a,str):
                sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
                ops=[(t,a[i1:i2][:150],b[j1:j2][:250]) for t,i1,i2,j1,j2 in sm.get_opcodes() if t!='equal']
                print('LOTE',k,f,len(a),'->',len(b),len(ops),'ops')
                for o in ops[:6]: print('   ',o)
            else: print('LOTE',k,f,'lista',len(a),len(b))
od={d['id']:d for d in old['discursivas']}; nd={d['id']:d for d in new['discursivas']}
for k in nd:
    for f in nd[k]:
        if od[k][f]!=nd[k][f]:
            a,b=od[k][f],nd[k][f]
            if isinstance(a,str):
                sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
                ops=[(t,a[i1:i2][:100],b[j1:j2][:120]) for t,i1,i2,j1,j2 in sm.get_opcodes() if t!='equal']
                print('DISC',k,f,len(a),'->',len(b),ops[:3] if len(ops)>3 else ops)
            else: print('DISC',k,f,'diff')
print('edital igual',old['edital']==new['edital'])
