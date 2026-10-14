import re,sys
from common import *
import common
from gce import strip_boiler
from p2 import ERRATA, LOTES
def norm(s): return re.sub(r'\s+',' ',s)
for spec in LOTES:
    raw=read(spec['file']).split('\n')
    lines=strip_boiler(raw); lines=fix_hyphen_wraps(lines,spec['file'])
    t=norm('\n'.join(lines))
    for e in ERRATA.get(spec['id'],[]):
        eid,x,y,_=e
        print(spec['id'],eid,'X=',t.count(norm(x)),'Y=',t.count(norm(y)))
