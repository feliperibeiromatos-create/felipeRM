import re,collections,sys
from texts import *
import importlib, estudante_marcas as em
p=load()
cnt=collections.Counter()
pat=sys.argv[1] if len(sys.argv)>1 else r'\bF\d{1,2}\b'
w=int(sys.argv[2]) if len(sys.argv)>2 else 80
for path,t in walk(p):
    if path=='.nome' or path.endswith('.url') or path.endswith('.nota'): continue
    u=em.strip_text(t,cnt)
    for m in re.finditer(pat,u):
        s=max(0,m.start()-w); e=min(len(u),m.end()+w)
        print(path,'::',repr(u[s:e]))
