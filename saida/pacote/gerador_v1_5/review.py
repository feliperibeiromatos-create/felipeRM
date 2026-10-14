import difflib, collections, re, sys
import estudante_marcas as em
from texts import *
p=load()
out=[]
for path,t in walk(p):
    if path=='.nome' or path.endswith('.url') or path.endswith('.nota'): continue
    u=em.strip_text(t,collections.Counter())
    if u==t: continue
    sm=difflib.SequenceMatcher(None,t,u,autojunk=False)
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal': continue
        assert op=='delete',(path,op,t[i1:i2],u[j1:j2])
        out.append((path,t[max(0,i1-50):i1],t[i1:i2],t[i2:i2+50]))
print(len(out),file=sys.stderr)
for path,a,d,b in out:
    if d.lstrip().startswith('[V'): continue
    print(path,'::',repr(a)+' ⟦'+repr(d)+'⟧ '+repr(b))
