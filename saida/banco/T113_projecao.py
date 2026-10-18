# T113_projecao.py — T-113 — 2026-10-18 — gerado por gbq-gerencia
# Somente leitura. Uso: python -I saida/banco/T113_projecao.py <raiz do repositório>
# Base: pacote.json v1.10 canônico (blob LF, SHA-256 d43c32de...) + 84 aceites da onda 4 (D-T98-ONDA4-ACEITE).
# Tópico = regra da prévia v15.2 (função construir): itens com itemEdital == id do tópico, sem somar subitens;
# tópico existe se tem itens (n>0) ou seções de curso; nota exige 30 respostas a questões distintas (CONTA_REPETIDAS=false).
import sys, os, re, json, hashlib, math, subprocess, collections

RAIZ = sys.argv[1]
def blob(rel, commit="HEAD"):
    return subprocess.run(["git", "-C", RAIZ, "show", f"{commit}:{rel}"], capture_output=True, check=True).stdout
def sha(b): return hashlib.sha256(b).hexdigest()

# 1. pacote v1.10 (canônico) e v1.9 (o que a plataforma embute)
b110 = blob("saida/pacote/pacote.json")
assert sha(b110) == "d43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed", "SHA v1.10"
b19 = blob("saida/pacote/pacote.json", "c26fc13")
assert sha(b19) == "1366055496457792bf55f541d901e2d1f277ee42611060b03bbf82b4427610bb", "SHA v1.9"
P = json.loads(b110.decode("utf-8")); P19 = json.loads(b19.decode("utf-8"))

# 2. onda 4 (D-T98-ONDA4-ACEITE): SHA dos finais, ids e folhas pelas linhas do mapa
FIN = {"saida/gce/L3_reforco_onda4_A_v3.md": "5be2941157f7db21e9d2f3b09007fbfd6ccafbc31608d37e3434e3fa8913c2b0",
       "saida/gce/L3_reforco_onda4_B_v2.md": "09d9d52144238358eb7fbf8ffcc35b71fa99b0b30e97fbb24410d2b563f7f398",
       "saida/gce/L3_reforco_onda4_C_v3.md": "d9faf9a70e698432afd4767a785bb526d97b2adadd60685ce468c1eba6241344"}
o4 = {}
for f, h in FIN.items():
    b = blob(f); assert sha(b) == h, f
    for m in re.finditer(r"^\|\s*(L3-R\d+)\s*\|\s*(P2-\d\.\d)\s*\|", b.decode("utf-8"), re.M):
        o4.setdefault(m.group(1), m.group(2))
assert len(o4) == 84 and not set(o4) & {i["id"] for i in P["itens"]}
VOL4 = {"L3-R%d" % n for n in (12, 13, 14, 16, 27, 56, 59, 65, 91, 94)}   # texto da D-T98-ONDA4-ACEITE (3)
PAR4 = {"L3-R%d" % n for n in (12, 13, 14, 53, 64, 95)}
assert VOL4 <= set(o4) and PAR4 <= set(o4)

# 3. estrutura de tópicos (réplica de construir() da prévia v15.2)
def sobe(i):
    m = re.match(r"^(P[12])-(.+)$", i)
    if not m or "." not in m.group(2): return None
    return m.group(1) + "-" + ".".join(m.group(2).split(".")[:-1])
def topicos(pk):
    ids = {e["id"] for e in pk["edital"]}
    def pai(i):
        c = sobe(i)
        while c and c not in ids: c = sobe(c)
        return c
    sec = collections.Counter()
    for l in pk["lotes"]:
        curso = str(l.get("curso") or "").replace("\r", "").strip()
        if not curso: continue
        atual = None
        for p in [x.strip() for x in re.split(r"\n(?=## )", curso) if x.strip()]:
            m = re.match(r"^## (.+)\n?", p); tid = None
            if m:
                num = (re.match(r"^(?:ITEM\s+)?(\d+(?:\.\d+)*)", m.group(1), re.I) or [None, None])[1]
                if num:
                    c = l["prova"] + "-" + num
                    while c and c not in ids: c = sobe(c)
                    tid = c
            if not tid and not m:
                best, bn = None, 0
                for t in l.get("itensEdital") or []:
                    n = len(re.findall(r"\b" + re.escape(t.split("-", 1)[1]) + r"\b", p))
                    if n > bn: best, bn = t, n
                tid = best
            if not tid: tid = atual or (l.get("itensEdital") or [None])[0]
            if not tid: continue
            atual = tid; sec[tid] += 1
    n = collections.Counter(i["itemEdital"] for i in pk["itens"])
    out = {}
    for e in pk["edital"]:
        if e["prova"] not in ("P1", "P2"): continue
        filhos = [x["id"] for x in pk["edital"] if pai(x["id"]) == e["id"]]
        out[e["id"]] = dict(texto=e["texto"], n=n[e["id"]], curso=sec[e["id"]] > 0, filhos=filhos,
                            topico=n[e["id"]] > 0 or sec[e["id"]] > 0)
    return out
T = topicos(P); T19 = topicos(P19)

# 4. contagem por tópico (base = v1.10 + onda 4)
def datado(i): return bool(i.get("volatil")) or bool(i.get("nota"))
cnt = collections.defaultdict(lambda: dict(v110=0, o4=0, dir=0, dat=0))
for i in P["itens"]:
    c = cnt[i["itemEdital"]]; c["v110"] += 1; c["dir"] += i["aderencia"] == "direta"; c["dat"] += datado(i)
for k, f in o4.items():
    c = cnt[f]; c["o4"] += 1; c["dir"] += k not in PAR4; c["dat"] += k in VOL4
# distintas: enunciados repetidos (normalizados) dentro do mesmo tópico
norm = lambda s: re.sub(r"\W+", " ", s.lower()).strip()
dup = collections.Counter((i["itemEdital"], norm(i["enunciado"])) for i in P["itens"])
dups = {k: v for k, v in dup.items() if v > 1}

FOLHAS = [t for t, o in T.items() if not o["filhos"]]
PAIS_CURSO = [t for t, o in T.items() if o["filhos"] and o["curso"]]
TOP40 = [t for t, o in T.items() if o["curso"]]
EXTRA = [t for t in ("P1-2", "P1-4", "P1-5")]

def base(t, b):  # b = "dentro" | "fora"
    c = cnt[t]; tot = c["v110"] + c["o4"]
    return tot if b == "dentro" else tot - c["dat"]

# 5. histórico de VOLÁTIL nas ondas 2 a 4 (itens novos) e perda do QA
nov = [i for i in P["itens"] if re.match(r"L[12]-R(\d+)$", i["id"]) and int(i["id"].split("R")[1]) >= 19]
v_hist = (sum(bool(i.get("volatil")) for i in nov) + len(VOL4)) / (len(nov) + 84)
CAP = 112          # itens por onda: ondas 2 e 3 (4 partes de 28; 111 + saldo de 1)
CIC_ONDA = 1.5     # ciclos por onda: 6 ciclos de 18/10 para 4 ondas + 2 consolidações (v1.9, v1.10)

def projeta(a, b):
    tops = sorted(FOLHAS) + (EXTRA if a == "exige" else [])
    falta = {}
    for t in tops:
        cur = base(t, b); n30 = max(0, 30 - cur); n40 = max(0, 40 - cur)
        if b == "fora":
            tot = cnt[t]["v110"] + cnt[t]["o4"]
            vt = max(v_hist, cnt[t]["dat"] / tot if tot else 0)
            vt = min(vt, 0.5)
            g30 = math.ceil(n30 / (1 - vt)) if n30 else 0
            g40 = math.ceil(n40 / (1 - vt)) if n40 else 0
        else:
            g30, g40 = n30, n40
        falta[t] = (cur, n30, n40, g30, g40)
    # fila: 1º até 30 (mais perto primeiro; empate: P2 antes de P1, D-RITMO-MAX), 2º de 30 a 40
    fila = []
    for t in sorted(tops, key=lambda t: (falta[t][3], t[:2] != "P2", t)):
        if falta[t][3]: fila.append((t, falta[t][3], "a30"))
    for t in sorted(tops, key=lambda t: (falta[t][4] - falta[t][3], t[:2] != "P2", t)):
        if falta[t][4] - falta[t][3]: fila.append((t, falta[t][4] - falta[t][3], "a40"))
    ondas, cur, livre = [], [], CAP
    for t, q, fase in fila:
        while q:
            u = min(q, livre); cur.append((t, u, fase)); q -= u; livre -= u
            if livre == 0: ondas.append(cur); cur, livre = [], CAP
    if cur: ondas.append(cur)
    return falta, ondas

if __name__ == "__main__":
    out = sys.stdout.reconfigure(encoding="utf-8")
    print("v1.10 itens:", len(P["itens"]), "| v1.9 itens:", len(P19["itens"]), "| onda 4:", len(o4))
    print("tópicos v15 (v1.9 embutido): com curso", sorted(t for t, o in T19.items() if o["curso"]).__len__(),
          "| topico (n>0 ou curso)", sum(o["topico"] for o in T19.values()))
    print("tópicos (v1.10): com curso", len(TOP40), "| folhas", len(FOLHAS), "| pais com curso", PAIS_CURSO,
          "| topico sem curso", [t for t, o in T.items() if o["topico"] and not o["curso"]])
    print("P1-5 v1.9 n =", T19["P1-5"]["n"], "curso", T19["P1-5"]["curso"], "| v1.10 n =", T["P1-5"]["n"])
    print("itens P1-5:", [i["id"] for i in P["itens"] if i["itemEdital"] == "P1-5"])
    print("enunciados repetidos no mesmo tópico:", dups)
    print("datados por nota sem volatil:", [i["id"] for i in P["itens"] if i.get("nota") and not i.get("volatil")])
    print("v_hist (novos das ondas 2-4 que viraram VOLÁTIL): %.3f (%d itens)" % (v_hist, len(nov) + 84))
    print()
    print("| Tópico | Curso | v1.10 | +onda 4 | Atual | Diretas | Datados | Falta 30 | Falta 40 | Atual sem datados | Falta 30 | Falta 40 |")
    print("|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|")
    for t in sorted(set(FOLHAS) | set(EXTRA), key=lambda x: [int(p) if p.isdigit() else p for p in re.split(r"[-.]", x)]):
        c = cnt[t]; a = c["v110"] + c["o4"]; s = a - c["dat"]
        print(f"| {t} | {'sim' if T[t]['curso'] else 'não'} | {c['v110']} | {c['o4']} | {a} | {c['dir']} | {c['dat']} | "
              f"{max(0,30-a)} | {max(0,40-a)} | {s} | {max(0,30-s)} | {max(0,40-s)} |")
    print()
    for a in ("exige", "sem"):
        for b in ("dentro", "fora"):
            falta, ondas = projeta(a, b)
            liq30 = sum(v[1] for v in falta.values()); liq40 = sum(v[2] for v in falta.values())
            g30 = sum(v[3] for v in falta.values()); g40 = sum(v[4] for v in falta.values())
            p1 = sum(v[4] for t, v in falta.items() if t.startswith("P1")); p2 = g40 - p1
            n30 = len(ondas_30 := [k for k, o in enumerate(ondas) if any(f == "a30" for _, _, f in o)])
            print(f"## a={a} b={b}: tópicos {len(falta)} | líquido 30 {liq30} | líquido 40 {liq40} | bruto 30 {g30} | "
                  f"bruto 40 {g40} (P1 {p1}, P2 {p2}) | ondas {len(ondas)} (fase a30 até a onda {max(ondas_30)+1 if ondas_30 else 0}) | "
                  f"ciclos {math.ceil(len(ondas)*CIC_ONDA)}")
            for k, o in enumerate(ondas, 1):
                por = collections.Counter(t[:2] for t, u, f in o for _ in range(u))
                ch30 = sum(1 for t in falta if falta[t][3] == 0 or sum(u for oo in ondas[:k] for tt, u, ff in oo if tt == t and ff == "a30") >= falta[t][3])
                print(f"   onda {k}: {sum(u for _,u,_ in o)} itens (P1 {por['P1']}, P2 {por['P2']}); tópicos {len({t for t,_,_ in o})}; "
                      f"tópicos com 30 ao fim: {ch30}/{len(falta)}; " + ", ".join(f"{t}+{u}{'' if f=='a30' else '*'}" for t, u, f in o))
