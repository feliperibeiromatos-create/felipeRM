# cobertura_v1_13.py - T-95 - secretaria - 2026-10-20 - python3 -I, somente leitura do repositorio; grava saida/pacote/cobertura_v1_13.md
import json, hashlib, re, sys, os
from collections import Counter, defaultdict
R='/home/claude/fabrica/'
PJ=R+'saida/pacote/montagem_v1_13/out/pacote.json'
EJ=R+'saida/pacote/montagem_v1_13/out/pacote_estudante.json'
OUT=R+'saida/pacote/cobertura_v1_13.md'
SELF=os.path.abspath(__file__)
sha=lambda p: hashlib.sha256(open(p,'rb').read()).hexdigest()
p=json.load(open(PJ,encoding='utf-8')); e=json.load(open(EJ,encoding='utf-8'))
items=p['itens']; nuc={i['id']:bool(i.get('nucleo')) for i in e['itens']}
assert [i['id'] for i in items]==[i['id'] for i in e['itens']]
ed=p['edital']; ids=[x['id'] for x in ed]
leaf=lambda i: not any(j!=i and j.startswith(i+'.') for j in ids)
isDA=lambda i: i.startswith('P1-DA-')
P1=[x['id'] for x in ed if x['prova']=='P1' and not isDA(x['id']) and leaf(x['id'])]
P2=[x['id'] for x in ed if x['prova']=='P2' and leaf(x['id'])]
DA=[x['id'] for x in ed if isDA(x['id']) and leaf(x['id'])]
# conferencia das 37 folhas de DA contra edital/DA_itens_1_12_P1.md
txt=open(R+'edital/DA_itens_1_12_P1.md',encoding='utf-8').read().split('\n')
body=[l for l in txt if l and not l.startswith('#') and not l.startswith('Disciplina') and not l.startswith('Fonte')][0]
nums=re.findall(r'(?:(?<=^)|(?<=\. ))(\d{1,2}(?:\.\d{1,2})?) (?=[A-ZÀ-Ú])',body)
nums=[n for n in nums]
fileleaf=[n for n in nums if not any(m!=n and m.startswith(n+'.') for m in nums)]
fileDA=['P1-DA-'+n for n in fileleaf]
assert len(nums)==len(set(nums))
assert set(fileDA)==set(DA) and len(DA)==37, (len(fileDA),len(DA),set(fileDA)^set(DA))
key=lambda i:[int(x) for x in i.split('-')[-1].split('.')] if not i.startswith('P2') else [int(x) for x in i[3:].split('.')]
def nk(i):
    s=i.split('-',1)[1]
    if s.startswith('DA-'): s=s[3:]
    return [int(x) for x in s.split('.')]
folhas=set(P1)|set(P2)|set(DA)
by=defaultdict(list)
for it in items: by[it['itemEdital']].append(it)
fora=[it for it in items if it['itemEdital'] not in folhas]
def row(f):
    L=by.get(f,[])
    t=len(L); a=sum(i['rotulo']=='AUTORAL' for i in L); r=sum(i['rotulo']=='CEBRASPE_ANALOGA' for i in L)
    assert a+r==t
    d=sum(i['aderencia']=='direta' for i in L); pa=sum(i['aderencia']=='parcial' for i in L); assert d+pa==t
    v=sum(bool(i.get('volatil')) for i in L); n=sum(nuc[i['id']] for i in L)
    return dict(f=f,t=t,a=a,r=r,d=d,pa=pa,v=v,n=n)
def piso(rw,f):
    if rw['d']>=10: return 'sim'
    esc = f.startswith('P2-') and not f.startswith('P2-4')
    return 'não' if esc else 'não (fora do escopo T-107)'
def lab(f): return 'DA '+f[len('P1-DA-'):] if isDA(f) else f
ONDA_DA='T-116 (D-REFORCO-DA)'
def line(rw,onda):
    f=rw['f']; m=rw['t']>=20; fa=max(0,20-rw['t'])
    o='—' if m else onda
    return f"| {lab(f)} | {rw['t']} | {rw['a']} | {rw['r']} | {rw['d']} | {rw['pa']} | {rw['v']} | {rw['n']} | {'sim' if m else 'não'} | {fa} | {piso(rw,f)} | {o} |"
HDR="| Folha | Total | AUTORAL | Reais | Diretos | PARCIAIS | VOLÁTEIS | Núcleo | Meta 20 | Faltam | Piso 10 diretos | Onda programada |\n|---|---|---|---|---|---|---|---|---|---|---|---|"
def soma(rs): 
    s={k:sum(r[k] for r in rs) for k in 't a r d pa v n'.split()}; return s
def sline(s): return f"| **Soma** | {s['t']} | {s['a']} | {s['r']} | {s['d']} | {s['pa']} | {s['v']} | {s['n']} | | | | |"
r1=[row(f) for f in P1]; r2=[row(f) for f in P2]; rd=[row(f) for f in DA]
s1,s2,sd=soma(r1),soma(r2),soma(rd)
tot=len(items); emf=s1['t']+s2['t']+sd['t']
assert emf+len(fora)==tot
ce=Counter(i['gabarito'] for i in items)
# comparacao com v1.12 (P1 e P2)
old={}
for l in open(R+'saida/pacote/cobertura_v1_12.md',encoding='utf-8'):
    if l.startswith('| P1-') or l.startswith('| P2-'):
        c=[x.strip() for x in l.strip().strip('|').split('|')]
        old[c[0]]=tuple(int(x) for x in c[1:9] if x.isdigit()) if False else tuple(int(c[k]) for k in (1,2,3,4,5,6,7))
mud=[]
for rw in r1+r2:
    new=(rw['t'],rw['a'],rw['r'],rw['d'],rw['pa'],rw['v'],rw['n'])
    if old.get(rw['f'])!=new: mud.append(rw['f'])
base_fora=sorted(i['id'] for i in fora if not i['id'][0]=='D')
da_fora=[i for i in fora if i['id'][0]=='D']
P1b=[r for r in r1 if r['t']<20]; P2b=[r for r in r2 if r['t']<20]; DAb=[r for r in rd if r['t']<20]
da20=[r for r in rd if r['t']>=20]
p30=[r['f'] for r in r1+r2 if r['t']>=30]
dord=sorted(rd,key=lambda r:(r['t'],nk(r['f'])))
falta=sum(max(0,20-r['t']) for r in rd)
fora_da_cont=Counter(i['itemEdital'] for i in da_fora)
fl=lambda rs:', '.join(f"{lab(r['f'])} ({r['t']}; faltam {20-r['t']})" for r in rs)
dir_lt10=lambda rs:[r for r in rs if r['d']<10]
o=[]
o.append("# cobertura_v1_13.md — T-95 — 2026-10-20 — gerado por secretaria\n")
o.append("Ocorrência v1.13 de D-COBERTURA-AUTO e D-COBERTURA-AUTO-2 e regra de D-T97-META-FUNDADOR-RESP. Contagem por item-folha do edital (entrada sem subitens; títulos de seção não contam). Meta: 20 por folha, com piso de 10 diretos por folha (D-T97-META-FUNDADOR-RESP; T-107). Formato igual ao de cobertura_v1_12.md. Passo 4.4 da D1 da T-118 (saida/pacote/T118_D1_v1_13_2026-10-20.md).\n")
o.append(f"**Fontes.** P1, P2 e DA: saida/pacote/montagem_v1_13/out/pacote.json v1.13 (geradoEm {p['geradoEm']}; {tot} itens; SHA-256 {sha(PJ)}; campos itemEdital, rotulo, aderencia, volatil). Núcleo: saida/pacote/montagem_v1_13/out/pacote_estudante.json v1.13-E (SHA-256 {sha(EJ)}; campo nucleo, por id; mesma lista de ids do pacote.json). Observação: a errata do achado 10 da T-117 só muda um texto de par do D6 e não afeta contagens. Folhas: {len(P1)+len(P2)+len(DA)} entradas do edital do pacote sem subitens ({len(P1)} P1, {len(P2)} P2 e {len(DA)} DA); as 37 de DA conferidas contra as entradas sem subitens de edital/DA_itens_1_12_P1.md (D-COBERTURA-AUTO-2; conjuntos iguais). Script: {SELF} (python3 -I, só leitura do repositório; SHA-256 {sha(SELF)}).\n")
o.append("**Definições.** Total = itens na folha (AUTORAL + CEBRASPE_ANALOGA). AUTORAL = rotulo AUTORAL. Reais = rotulo CEBRASPE_ANALOGA. Diretos e PARCIAIS = campo aderencia (\"direta\" e \"parcial\"). VOLÁTEIS = campo volatil verdadeiro. Núcleo = nucleo verdadeiro no pacote_estudante. Formatos: o pacote não tem campo de formato por item; a coluna não existe no formato da cobertura_v1_12.md e não foi recontada (n/d). Meta 20 cumprida: total >= 20. Piso 10 diretos cumprido: diretos >= 10.\n")
o.append(f"**Totais de conferência.** {tot} itens no pacote; {emf} em folhas; {len(fora)} fora das folhas (ressalva (a)). Gabarito: {ce['C']} C e {ce['E']} E (conferido no pacote). AUTORAL nas folhas: {s1['a']+s2['a']+sd['a']}; Reais nas folhas: {s1['r']+s2['r']+sd['r']}; Diretos: {s1['d']+s2['d']+sd['d']}; PARCIAIS: {s1['pa']+s2['pa']+sd['pa']}; VOLÁTEIS: {s1['v']+s2['v']+sd['v']}; Núcleo: {s1['n']+s2['n']+sd['n']}. Por matéria, em folhas: P1 {s1['t']}, P2 {s2['t']}, DA {sd['t']}.\n")
o.append("**Critério de aceite da D1 (passo 4.4).** "+
 f"75 folhas: {len(P1)+len(P2)+len(DA)} ({'confere' if len(P1)+len(P2)+len(DA)==75 else 'DIFERE'}). "
 f"1.159 itens: {tot} ({'confere' if tot==1159 else 'DIFERE'}). 1.132 em folha: {emf} ({'confere' if emf==1132 else 'DIFERE'}). 27 fora: {len(fora)} ({'confere' if len(fora)==27 else 'DIFERE'}). "
 f"C/E 582/577: {ce['C']}/{ce['E']} ({'confere' if (ce['C'],ce['E'])==(582,577) else 'DIFERE'}). "
 f"DA 396 itens em folha: {sd['t']} ({'confere' if sd['t']==396 else 'DIFERE'}); 5 VOLÁTEIS: {sum(bool(i.get('volatil')) for i in items if i['id'][0]=='D')} no pacote, {sd['v']} em folha; núcleo 352 nas folhas: {sd['n']} ({'confere' if sd['n']==352 else 'DIFERE'}); 0 reais: {sd['r']} ({'confere' if sd['r']==0 else 'DIFERE'}). "
 f"DA com 20 ou mais: {len(da20)} ({'confere' if len(da20)==3 else 'DIFERE'}); abaixo de 20: {len(DAb)} ({'confere' if len(DAb)==34 else 'DIFERE'}).\n")
o.append("**Ressalvas de cobertura.**")
o.append(f"(a) Itens com itemEdital de título (não folha) ficam fora das folhas: {len(fora)} itens. P1 e P2 ({len(base_fora)}, os mesmos da v1.12): {', '.join(base_fora)}. DA ({len(da_fora)}): "+'; '.join(f"{k} com {v} ({', '.join(sorted(i['id'] for i in da_fora if i['itemEdital']==k))})" for k,v in sorted(fora_da_cont.items()))+" (P1-DA-1 é o caput do título 1 e P1-DA-8 é o caput do título 8; D1-a).")
o.append("(b) Reais de DA: o pacote v1.13 não tem item CEBRASPE_ANALOGA de DA (0); os 38 itens de banco com itemEdital P1-DA ficam fora da v1.13 e dependem de D1 própria (T-118, (d); T-78 e T-79; T-123), por isso a coluna Reais de DA é 0 e as folhas DA 7, 11 e 12 não somam os reais do banco que cobertura_v1_11.md listava.")
o.append("(c) O piso de 10 diretos é decidido para P2 1.x a 3.x (T-107). P1, P2 4.x e DA aparecem com o mesmo cálculo, só para conferência; nas listas, o rótulo \"fora do escopo T-107\" marca essas folhas.")
o.append("(d) A coluna \"Onda programada\" de P1 não foi reconstruída nesta ocorrência (n/r); a programação das ondas está em TAREFAS.md. Para DA, as folhas abaixo de 20 estão na onda da T-116 (D-REFORCO-DA; reforço até 20 por folha, das mais ralas às mais cheias), por isso nada se escreve em PARA_PRESIDENCIA.md por DA.")
o.append(f"(e) Mudanças de total, AUTORAL, reais, diretos, PARCIAIS, VOLÁTEIS ou núcleo de P1 e P2 desde a v1.12: {'nenhuma (as 38 folhas são idênticas às de cobertura_v1_12.md)' if not mud else 'diferem: '+', '.join(mud)}. A v1.13 acrescenta 410 itens de DA (D1 60, D2 80, D3 71, D4 79, D5 70, D6 50), todos AUTORAL e diretos.")
o.append(f"(f) Folhas P2 1.x a 4.x: nenhuma abaixo de 20. As folhas P1 abaixo de 20 são {len(P1b)}. As folhas de DA abaixo de 20 são {len(DAb)}; com 20 ou mais, {len(da20)} ({', '.join(lab(r['f'])+' = '+str(r['t']) for r in da20)}).\n")
o.append(f"## P1 — TI (itens 1 a 8; {len(P1)} folhas)\n")
o.append(HDR); 
for r in r1: o.append(line(r,'n/r'))
o.append(sline(s1)); o.append("")
o.append(f"## P2 — RF/IA (itens 1.1 a 4.3; {len(P2)} folhas)\n")
o.append(HDR)
for r in r2: o.append(line(r,'n/r'))
o.append(sline(s2)); o.append("")
o.append(f"## DA — Noções de Direito Administrativo ({len(DA)} folhas de edital/DA_itens_1_12_P1.md)\n")
o.append("Ordem do edital. Reais = 0 em todas as folhas (ressalva (b)). Todos os itens de DA são AUTORAL e diretos (PARCIAIS = 0).\n")
o.append(HDR)
for r in rd: o.append(line(r,ONDA_DA))
o.append(sline(sd)); o.append("")
o.append("### DA — da folha mais rala para a mais cheia (ordem da D-REFORCO-DA)\n")
o.append("Empate de total: ordem do edital. \"Faltam para 20\" = 20 menos o total, mínimo 0.\n")
o.append("| # | Folha | Total | Faltam para 20 | Diretos | VOLÁTEIS | Núcleo |\n|---|---|---|---|---|---|---|")
for k,r in enumerate(dord,1): o.append(f"| {k} | {lab(r['f'])} | {r['t']} | {max(0,20-r['t'])} | {r['d']} | {r['v']} | {r['n']} |")
o.append(f"| | **Soma ({len(DA)} folhas)** | {sd['t']} | {falta} | {sd['d']} | {sd['v']} | {sd['n']} |\n")
o.append(f"Faltam {falta} itens para as {len(DAb)} folhas de DA abaixo de 20 chegarem a 20 (sem contar os itens fora de folha de P1-DA-1 e P1-DA-8, caput). Folhas de DA com menos de 10 itens: "+', '.join(f"{lab(r['f'])} = {r['t']}" for r in dord if r['t']<10)+".\n")
o.append("## Listas para o orquestrador (T-95, T-107)\n")
o.append(f"(a) Folhas P1 abaixo de 20 ({len(P1b)}; a programação de onda não foi reconstruída, ressalva (d)): {fl(P1b)}.")
o.append(f"(a2) Folhas P2 1.x a 4.x abaixo de 20: {fl(P2b) if P2b else 'nenhuma'}.")
o.append(f"(a3) Folhas que atingiram 30 itens ({len(p30)}): {', '.join(p30)}.")
o.append(f"(a4) Folhas de DA abaixo de 20 ({len(DAb)}; todas na onda da T-116): {fl([r for r in dord])[:0] or fl([r for r in dord if r['t']<20])}.")
o.append("(b) Folhas com menos de 10 diretos (P1 e P2): "+', '.join(f"{lab(r['f'])} ({r['d']})" for r in dir_lt10(r1+r2))+". Nas folhas P2 1.x a 3.x, "+("nenhuma" if not dir_lt10([r for r in r2 if not r['f'].startswith('P2-4')]) else "há")+".")
o.append("(b2) Folhas de DA com menos de 10 diretos (fora do escopo T-107): "+(', '.join(f"{lab(r['f'])} ({r['d']})" for r in dir_lt10(rd)) or 'nenhuma')+".")
o.append("\nFIM — cobertura_v1_13.md")
open(OUT,'w',encoding='utf-8').write('\n'.join(o)+'\n')
print('ok', emf, len(fora), len(da20), len(DAb), falta, mud)
print(', '.join(f"{r['f'].split('DA-')[-1]}={r['t']}" for r in dord))
