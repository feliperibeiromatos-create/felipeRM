# Conferencia GCE da v3 (T-108), somente leitura. Uso: python -I conf_v3.py <v2.csv> <v3.csv|SIMULAR> <pacote.json>
import sys,csv,io,json,hashlib,re
v2p,v3p,pk=sys.argv[1:4]
H2='c4a29f1bf21721a1d2ec52517462f56c4fae8fca8cbf2c517875200c87f07fe7'
HP='d43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed'
NOVAS=[
 dict(id_edicao='GCE-0270',ids_ocorrencia='NAO_INVENTARIADA-12',caminho='discursivas[D1].padrao',lote='DISCURSIVA',categoria='C07',antes='são HIPÓTESE\ndo Projeto:',depois='são HIPÓTESE\ndeste material:',acao='SUBSTITUIR',regra='5',fonte_origem='',nota='D1 pós-R2 (O1 do QA R2); forma de GCE-0265 a 0267; rótulo HIPÓTESE mantido'),
 dict(id_edicao='GCE-0271',ids_ocorrencia='NAO_INVENTARIADA-13',caminho='discursivas[D2].padrao',lote='DISCURSIVA',categoria='C07',antes='é HIPÓTESE do Projeto,',depois='é HIPÓTESE deste material,',acao='SUBSTITUIR',regra='5',fonte_origem='',nota='D1 pós-R2 (O1 do QA R2); forma de GCE-0265 a 0267; rótulo HIPÓTESE mantido'),
]
COLS=['id_edicao','ids_ocorrencia','caminho','lote','categoria','antes','depois','acao','regra','fonte_origem','nota']
def regs(b):
    out=[];cur=bytearray();q=False;i=0
    while i<len(b):
        c=b[i:i+1]
        if c==b'"': q=not q
        if not q and b[i:i+2]==b'\r\n':
            out.append(bytes(cur));cur=bytearray();i+=2;continue
        cur+=c;i+=1
    if cur: out.append(bytes(cur))
    return out
b2=open(v2p,'rb').read(); ok=[]
ok.append(('SHA v2',hashlib.sha256(b2).hexdigest()==H2))
if v3p=='SIMULAR':
    s=io.StringIO(newline='');w=csv.writer(s,lineterminator='\r\n')
    for n in NOVAS: w.writerow([n[c] for c in COLS])
    b3=b2+s.getvalue().encode('utf-8')
else: b3=open(v3p,'rb').read()
r2,r3=regs(b2),regs(b3)
ok.append(('(a) 272 registros brutos (cab+271)',len(r3)==272))
ok.append(('(b) 270 primeiros registros = v2 byte a byte',r3[:270]==r2))
L3=list(csv.DictReader(io.StringIO(b3.decode('utf-8'),newline='')))
ok.append(('(c) GCE-0270/0271 no fim, campos exatos',[{c:x[c] for c in COLS} for x in L3[-2:]]==NOVAS))
ok.append(('(c2) sem CR em antes/depois',all('\r' not in x['antes']+x['depois'] for x in L3)))
raw=open(pk,encoding='utf-8',newline='').read().replace('\r\n','\n')
ok.append(('SHA pacote LF',hashlib.sha256(raw.encode('utf-8')).hexdigest()==HP))
d=json.loads(raw)
def get(path):
    segs=path.split('.'); cur=d
    for i,sg in enumerate(segs):
        m=re.match(r'(\w+)(?:\[([^\]]+)\])?$',sg); nm,key=m.groups()
        if i==len(segs)-1 and key is None: return cur,nm
        cur=cur[nm]
        if key is not None:
            hit=[o for o in cur if isinstance(o,dict) and o.get('id')==key]
            cur=hit[0] if hit else cur[int(key)]
    raise KeyError(path)
campos={}
for x in L3: campos.setdefault(x['caminho'],[]).append(x)
falha=[]
for n in NOVAS:
    o,f=get(n['caminho']); 
    if o[f].count(n['antes'])!=1: falha.append(('antes nao unico',n['id_edicao']))
# sobreposicao e aplicacao
sob=0;aplic={}
for cam,ls in campos.items():
    o,f=get(cam);t=o[f];iv=[]
    for x in ls:
        k=t.find(x['antes']); 
        if k<0 or t.count(x['antes'])!=1: falha.append(('antes',x['id_edicao']));continue
        iv.append((k,k+len(x['antes'])))
    iv.sort()
    for a,b in zip(iv,iv[1:]):
        if b[0]<a[1]: sob+=1
    for x in ls:
        if x['antes'] in t: t=t.replace(x['antes'],x['depois'],1)
        else: falha.append(('aplicar',x['id_edicao']))
    aplic[cam]=t
ok.append(('(d) sobreposicao 0',sob==0))
ok.append(('(e) aplicacao sem falhas',not falha))
res=[(c,p) for c,t in aplic.items() for p in ['do Projeto','não afirmar','Inapto a simulado','costuma ser cobrad','costumam ser cobrad'] if p in t]
ok.append(('(e2) residuo 0 nos campos tocados',not res))
for c in ['discursivas[D1].padrao','discursivas[D2].padrao']:
    ok.append(('HIPÓTESE intacto '+c,'HIPÓTESE' in aplic[c] and 'deste material' in aplic[c]))
for k,v in ok: print('OK ' if v else 'FALHA',k)
print('falhas',falha,'residuos',res,'campos tocados',len(aplic))
print('SHA v3',hashlib.sha256(b3).hexdigest())
