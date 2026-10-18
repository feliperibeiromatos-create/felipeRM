import csv, json, re, sys, hashlib, copy, importlib.util, collections
BASE='C:/Users/Felipe/felipeRM_push/saida/'
raw=open(BASE+'pacote/pacote.json','rb').read()
lf=raw.replace(b'\r\n',b'\n')
assert hashlib.sha256(lf).hexdigest().startswith('d43c32de'),'sha'
P=json.loads(lf.decode('utf-8'))
rows=list(csv.DictReader(open(BASE+'gcb/T108_substituicoes_GCB_parteB.csv',encoding='utf-8',newline='')))
occ=list(csv.DictReader(open(BASE+'pacote/T108_ocorrencias.csv',encoding='utf-8',newline='')))
mine=[r for r in occ if r['gerencia']=='GCB' and r['arquivo']=='pacote.json' and r['lote']=='6a']
univ={r['id_ocorrencia']:r for r in mine if r['classe'] in('PROCESSO','VERIFICAR')}
fp1=[r for r in mine if r['classe']=='FP-R1']; fpc=[r for r in mine if r['classe']=='FP-CONTEUDO']
res=[]
def ok(n,c,d=''): res.append((n,bool(c),d)); print(('OK  ' if c else 'FALHA ')+n+(' '+d if d else ''))
L6={l['id']:l for l in P['lotes']}['L6A']; IT={i['id']:i for i in P['itens']}
def getf(c):
    m=re.match(r'lotes\[L6A\]\.(\w+)(?:\[(\d+)\])?(?:\.(\w+))?$',c)
    if m:
        v=L6[m.group(1)]
        if m.group(2): v=v[int(m.group(2))][m.group(3)]
        return v
    m=re.match(r'itens\[(.+?)\]\.(\w+)$',c); return IT[m.group(1)][m.group(2)]
# (b) cobertura
cnt=collections.Counter(i for r in rows for i in r['ids_ocorrencia'].split(';'))
ok('(b) 199 ids cobertos exatamente uma vez',set(cnt)==set(univ) and all(v==1 for v in cnt.values()) and len(univ)==199,f'{len(cnt)} ids, {len(rows)} edições')
ok('(b) id_edicao sequencial únicos',[r['id_edicao'] for r in rows]==[f'GCB-B{i:04d}' for i in range(1,len(rows)+1)])
# (a) antes literal e único
bad=[r['id_edicao'] for r in rows if getf(r['caminho']).count(r['antes'])!=1]
ok('(a) antes literal e único no campo',not bad,str(bad[:5]))
# antes contém todas as ocorrências (casamento dentro do antes)
bad=[r['id_edicao'] for r in rows if any(univ[i]['casamento'] not in r['antes'] for i in r['ids_ocorrencia'].split(';'))]
ok('(a) antes contém o casamento de cada id',not bad,str(bad[:5]))
ok('campos só curso/resumo/pegadinhas/justificativa',all(re.search(r'\.(curso|resumo)$|pegadinhas\[\d+\]\.texto$|\.justificativa$',r['caminho']) for r in rows))
# sobreposição
byc=collections.defaultdict(list)
for r in rows:
    t=getf(r['caminho']); s=t.find(r['antes']); byc[r['caminho']].append((s,s+len(r['antes']),r['id_edicao']))
ov=[(a,b) for c,l in byc.items() for a,b in zip(sorted(l),sorted(l)[1:]) if b[0]<a[1]]
ok('sem sobreposição de edições',not ov,str(ov[:3]))
# (c) FP intactos
ok('(c) D-C05-4a878e59 fora de todo antes',all('tecla F4' not in r['antes'] for r in rows) and any(r['id_ocorrencia']=='D-C05-4a878e59' for r in fp1))
# aplicar
P2=copy.deepcopy(P)
L2={l['id']:l for l in P2['lotes']}['L6A']; I2={i['id']:i for i in P2['itens']}
def setf(c,v):
    m=re.match(r'lotes\[L6A\]\.(\w+)(?:\[(\d+)\])?(?:\.(\w+))?$',c)
    if m:
        if m.group(2): L2[m.group(1)][int(m.group(2))][m.group(3)]=v
        else: L2[m.group(1)]=v
        return
    m=re.match(r'itens\[(.+?)\]\.(\w+)$',c); I2[m.group(1)][m.group(2)]=v
for c in {r['caminho'] for r in rows}:
    t=getf(c)
    for r in rows:
        if r['caminho']==c: t=t.replace(r['antes'],r['depois'],1) if r['acao']!='DELETAR' else t.replace(r['antes'],'',1)
    setf(c,t)
# FP preservado
tx=L2['curso']
ok('(c) tecla F4 do Excel intacta no curso','A tecla F4, com a referência selecionada na barra de fórmulas, alterna entre os tipos' in tx)
ok('(c) FP-CONTEUDO (P1. P2. …) intactos',all(getf(r['caminho']).count(r['casamento'])>=1 for r in fpc) and len(re.findall(r'(?m)^P\d+\. ',tx))==len(re.findall(r'(?m)^P\d+\. ',L6['curso'])))
# fora do escopo igual
def strip(Pp):
    Q=copy.deepcopy(Pp)
    l=[x for x in Q['lotes'] if x['id']=='L6A'][0]
    for k in('curso','resumo'): l[k]=''
    for p in l['pegadinhas']: p['texto']=''
    for i in Q['itens']:
        if i['id'].startswith('6A-'): i['justificativa']=''
    return json.dumps(Q,sort_keys=True,ensure_ascii=False)
ok('(f) enunciado, gabarito, itemEdital e demais campos idênticos',strip(P)==strip(P2))
ok('(f) nenhum item fora dos 6A-01..15 alterado',all(r['caminho'].startswith('lotes[L6A]') or re.match(r'itens\[6A-\d\d\]\.justificativa',r['caminho']) for r in rows))
# (d) varredura do inventário
spec=importlib.util.spec_from_file_location('inv',BASE+'pacote/T108_inventario.py'); sys.argv=['x',BASE+'pacote']
inv=importlib.util.module_from_spec(spec); spec.loader.exec_module(inv)
v=[o for o in inv.varre(P,'D') if o['lote']==mine[0]['lote']]
v2=[o for o in inv.varre(P2,'D') if o['lote']==mine[0]['lote']]
c0=collections.Counter(o['classe'] for o in v); c2=collections.Counter(o['classe'] for o in v2)
ok('(d) varredura antes: PROCESSO+VERIFICAR=199',c0['PROCESSO']+c0['VERIFICAR']==199,str(dict(c0)))
ok('(d) varredura depois: 0 PROCESSO e 0 VERIFICAR no lote 6a',c2['PROCESSO']==0 and c2['VERIFICAR']==0,str(dict(c2)))
ok('(d) restam FP-R1 = 1 e FP-CONTEUDO igual',c2['FP-R1']==1 and c2['FP-CONTEUDO']==c0['FP-CONTEUDO'],str(dict(c2)))
# (e) proibidos no depois
PROIB=[r'(?<!\w)(?:F|N|U|GG|TB)\d+(?!\d)',r'6A-\d\d',r'(?<!\w)Lotes? \d',r'(?i)\blote\b',r'\b(?:QA|CQFP)\b',r'(?<!\w)(?:TC|IC|GI|AT)(?!\w)',r'\[TS\]',r'VOL[ÁA]T',r'Difere do',r'(?i)sem item|n[ãa]o h[áa] item|n[ãa]o vira item',r'(?i)n[ãa]o cobr|n[ãa]o s[ãa]o cobrados|n[ãa]o é cobrado',r'(?i)reverificar',r'S[óo] o fato',r'\bv\d\b',r'(?i)errata',r'sem armadilha']
bad=[]
for r in rows:
    for p in PROIB:
        # nomes de fonte contêm "F4"? checar só no depois sem os nomes
        if re.search(p,r['depois']) and not (p.startswith('(?<!\\w)(?:F') and False): bad.append((r['id_edicao'],p))
ok('(e) nenhum depois com código de fonte/item/par/Lote N/QA/TC-IC-GI-AT/[TS]/VOLÁTIL/Difere/instrução interna',not bad,str(bad[:8]))
ok('depois não vazio exceto DELETAR',all(r['depois']!='' or r['acao']=='DELETAR' for r in rows))
ok('MANTER = 0',all(r['acao']!='MANTER' for r in rows))
ok('VERIFICAR (14 da parte) todos com ação SUBSTITUIR/DELETAR',all(next(r for r in rows if i in r['ids_ocorrencia'].split(';'))['acao']!='MANTER' for i,o in univ.items() if o['classe']=='VERIFICAR'),str(sum(1 for o in univ.values() if o['classe']=='VERIFICAR')))
ok('fonte_origem em toda edição com C05',all(r['fonte_origem'] for r in rows if 'C05' in r['categoria'].split(';')))
# texto residual
for c in ['curso','resumo']:
    tt=L2[c]
    ok(f'residual {c}: sem código Fn (exceto tecla F4)',not [m for m in re.finditer(r'(?<!\w)F\d+(?!\d)',tt) if not tt[:m.start()].endswith('A tecla ')])
print('contagens por categoria:',dict(collections.Counter(c for r in rows for c in r['categoria'].split(';'))))
print('edições por ação:',dict(collections.Counter(r['acao'] for r in rows)),' por modo:',dict(collections.Counter(r['modo'] for r in rows)),' por regra:',dict(collections.Counter(r['regra'] for r in rows)))
print('por campo:',dict(collections.Counter(re.sub(r'\[.*?\]','',r['caminho']) if not r['caminho'].startswith('lotes') else r['caminho'].split('.')[1].split('[')[0] for r in rows)))
print('ocorrências por categoria (universo):',dict(collections.Counter(o['categoria'] for o in univ.values())))
print('RESULTADO:','TUDO OK' if all(x[1] for x in res) else 'HÁ FALHAS')
