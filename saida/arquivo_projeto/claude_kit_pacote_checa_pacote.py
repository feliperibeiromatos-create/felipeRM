#!/usr/bin/env python3
"""Conferência de entrada de um pacote novo da Fábrica na plataforma Câmara 2026 (somente leitura).

Uso:
  python3 -I checa_pacote.py <base> <novo.json> [--registro <arquivo>] [--saida <relatorio.md>]

<base>      pacote em uso: o index.html publicado (lê a linha `const PUB_INLINE = ...`) ou um pacote.json
<novo.json> pacote recebido da Fábrica
--registro  registro de alterações da Fábrica: JSON {"alteracoes":[{"id":"L2-R16","campo":"itemEdital"}, ...]}
            ou texto/markdown (um id citado no texto conta como registrado, com aviso para conferir à mão)

Saída: relatório em Markdown e código de saída 0 (pode seguir para a regressão), 1 (há BLOQUEIO) ou 2 (erro de leitura).
Não altera nenhum arquivo de entrada.
"""
import json, re, sys, collections, hashlib, argparse

ap = argparse.ArgumentParser()
ap.add_argument("base"); ap.add_argument("novo")
ap.add_argument("--registro"); ap.add_argument("--saida")
a = ap.parse_args()

def carrega(caminho):
    txt = open(caminho, encoding="utf-8").read()
    if caminho.endswith(".html"):
        linha = next((l for l in txt.split("\n") if l.startswith("const PUB_INLINE")), None)
        if not linha: raise SystemExit("base sem a linha const PUB_INLINE")
        js = linha[linha.index("=") + 1:].strip().rstrip(";")
        diag = None
        m = re.search(r"^const DIAG30 = (\{.*\});\s*$", txt, re.M)
        if m: diag = json.loads(m.group(1))
        return json.loads(js), diag, txt
    return json.loads(txt), None, None

try:
    B, DIAG30, html = carrega(a.base)
    N, _, _ = carrega(a.novo)
except Exception as e:
    print("ERRO de leitura:", e); sys.exit(2)

BLOQ, AVISO, INFO = [], [], []
def bloq(t): BLOQ.append(t)
def aviso(t): AVISO.append(t)
def info(t): INFO.append(t)

# ---------- 1. Estrutura ----------
for k in ["versao", "geradoEm", "nome", "edital", "itens", "simulados", "lotes", "discursivas"]:
    if k not in N: bloq(f"falta a chave `{k}` no pacote novo")
if BLOQ:
    pass
itens = N.get("itens", []); edital = {e["id"]: e for e in N.get("edital", [])}
ids = [i.get("id") for i in itens]
dup = [k for k, v in collections.Counter(ids).items() if v > 1]
if dup: bloq(f"ids repetidos: {dup[:10]}")
sem = [i.get("id") for i in itens if not i.get("id") or not i.get("enunciado") or i.get("gabarito") not in ("C", "E")]
if sem: bloq(f"{len(sem)} item(ns) sem id, enunciado ou gabarito C/E (a plataforma recusa o pacote): {sem[:10]}")
fora = [i["id"] for i in itens if i.get("itemEdital") not in edital]
if fora: bloq(f"{len(fora)} item(ns) com itemEdital fora do edital do pacote: {fora[:10]}")
rot = collections.Counter(i.get("rotulo") for i in itens)
if rot.get("CEBRASPE_ESTILO"): bloq("rótulo CEBRASPE_ESTILO é proibido (Regras Comuns v2.1)")
outros = [r for r in rot if r not in ("CEBRASPE_OFICIAL", "CEBRASPE_ANALOGA", "OUTRA_OFICIAL", "AUTORAL")]
if outros: aviso(f"rótulos fora da lista das Regras Comuns: {outros}")
M = {i["id"]: i for i in itens if i.get("id")}
for s in N.get("simulados", []):
    falta = [x for x in s.get("itens", []) if x not in M]
    if falta: bloq(f"simulado {s.get('id')} cita {len(falta)} id(s) que não existem: {falta[:5]}")

# ---------- 2. Comparação com o pacote em uso ----------
BM = {i["id"]: i for i in B["itens"]}
sumiram = [k for k in BM if k not in M]
novos = [k for k in M if k not in BM]
CAMPOS_REG = ["gabarito", "itemEdital", "enunciado", "rotulo"]   # mudança aqui exige registro
CAMPOS_INFO = ["justificativa", "comando", "textoBase", "volatil", "aderencia", "nota", "certame", "numero"]
mud = collections.defaultdict(list)
for k in BM:
    if k in M:
        for c in CAMPOS_REG + CAMPOS_INFO:
            if BM[k].get(c) != M[k].get(c): mud[c].append(k)

registrados, reg_texto = set(), False
if a.registro:
    t = open(a.registro, encoding="utf-8").read()
    try:
        R = json.loads(t)
        for r in R.get("alteracoes", []): registrados.add((r.get("id"), r.get("campo")))
    except Exception:
        reg_texto = True
        for k in set(BM) | set(M):
            if re.search(r"(?<![\w-])" + re.escape(k) + r"(?![\w-])", t): registrados.add((k, "*"))
def tem_reg(k, c): return (k, c) in registrados or (k, "*") in registrados

for k in sumiram:
    (info if tem_reg(k, "removido") else bloq)(f"id removido{'' if tem_reg(k,'removido') else ' SEM REGISTRO'}: {k}")
for c in CAMPOS_REG:
    for k in mud[c]:
        msg = f"{c} mudou em {k}: {str(BM[k].get(c))[:60]!r} → {str(M[k].get(c))[:60]!r}"
        (info if tem_reg(k, c) else bloq)(msg + ("" if tem_reg(k, c) else " — SEM REGISTRO"))
if reg_texto and registrados: aviso("registro lido como texto: um id citado conta como registrado; confira à mão se a alteração citada é a mesma encontrada")

# DIAG30 (lista fixa no código da plataforma)
if DIAG30:
    for mod, lst in DIAG30.items():
        falta = [x for x in lst if x not in M]
        if falta: bloq(f"diagnóstico D30-{mod}: {len(falta)} id(s) sumiram do pacote; o diagnóstico deixa de aparecer: {falta}")
        g = [x for x in lst if x in M and x in BM and M[x]["gabarito"] != BM[x]["gabarito"]]
        if g: bloq(f"diagnóstico D30-{mod}: gabarito mudou em {g} (exige revisão da seleção)")
        e = [x for x in lst if x in M and x in BM and M[x]["itemEdital"] != BM[x]["itemEdital"]]
        if e: aviso(f"diagnóstico D30-{mod}: itemEdital mudou em {e} (a regra 'ao menos 1 por subitem' precisa ser reconferida)")
else:
    aviso("base sem DIAG30 (passe o index.html publicado como base para conferir o diagnóstico)")

# Prefixos de id: o painel (skill atualizar-painel-camara) e LOTE_INFO do código dependem deles
PREF = {"L1-", "L1C-", "L2-", "L3-", "L4-", "4C-", "A5-", "5C-", "6A-", "6B-", "L6A-", "L6B-", "BQ-"}
pref_novos = collections.Counter(re.match(r"^([A-Z0-9]+-)", k).group(1) if re.match(r"^([A-Z0-9]+-)", k) else "?" for k in novos)
desconhecidos = {p: n for p, n in pref_novos.items() if p not in PREF}
if desconhecidos: aviso(f"prefixos de id novos {desconhecidos}: acrescentar em PREF/NOME do script do painel antes de atualizá-lo")
lotes_novos = [l["id"] for l in N.get("lotes", []) if l["id"] not in {x["id"] for x in B["lotes"]}]
if lotes_novos: aviso(f"lotes novos {lotes_novos}: acrescentar ao script do painel; conferir se o módulo existe na plataforma (DISCIPLINAS/MODULOS)")
def modulo(x): x = str(x or ""); return "DA" if re.match(r"^(P1-)?DA-", x) else x[:2]
mods = sorted({modulo(i.get("itemEdital")) for i in itens} - {"P1", "P2", "DA"})
if mods: aviso(f"itens de módulo que a plataforma ainda não exibe: {mods} (precisa de mudança no código antes de aparecer)")
da_ed = [e for e in edital if modulo(e) == "DA"]
da_it = [i for i in itens if modulo(i.get("itemEdital")) == "DA"]
if da_it or da_ed:
    info(f"Direito Administrativo: {len(da_ed)} entradas de edital, {len(da_it)} questões (a plataforma só mostra DA a partir da v15.5)")
    if da_it and not da_ed: bloq("há questões de DA sem as entradas de edital de DA no pacote")
    pref = {re.match(r"^(.*?DA-)", e).group(1) for e in da_ed}
    if len(pref) > 1: bloq(f"prefixos de edital de DA misturados: {pref} (use um só: P1-DA- ou DA-)")
    for l in N.get("lotes", []):
        ie = l.get("itensEdital") or []
        if any(modulo(x) == "DA" for x in ie) and any(modulo(x) != "DA" for x in ie):
            bloq(f"lote {l['id']} mistura itens de DA com outros módulos (os títulos do curso seriam ligados ao módulo errado)")
if html and re.search(r"const DEMO_DA=true;", html): aviso("a base tem DEMO_DA=true (prévia de laboratório); use o index.html publicado como base, ou o embute_pacote.py desliga a demonstração")
demo = [k for k, i in M.items() if re.search(r"demonstra[çc][ãa]o de formato", (i.get("enunciado") or "") + (i.get("justificativa") or ""), re.I)]
if demo: bloq(f"texto de demonstração em itens: {demo[:5]}")

# ---------- 3. pacote.topicos (resumo, emUmMinuto, visuais) ----------
T = N.get("topicos")
TIPOS = {"fluxo": ["passos"], "tabela": ["colunas", "linhas"], "linha": ["marcos"], "esquema": ["centro", "ramos"], "barras": ["dados"],
         "compare": ["a", "b", "linhas"], "baseLegal": ["dispositivos"]}   # compare e baseLegal: plataforma v15.5+
def strs(x): return isinstance(x, list) and all(isinstance(s, str) and s.strip() for s in x)
if T is None:
    info("pacote sem `topicos` (a plataforma mantém só a demonstração do tópico P2-1.4)")
elif not isinstance(T, dict):
    bloq("`topicos` precisa ser um objeto {\"P2-1.4\": {...}}")
else:
    for tid, o in T.items():
        pre = f"topicos[{tid}]"
        if tid not in edital: bloq(f"{pre}: id não existe no edital do pacote"); continue
        if not isinstance(o, dict): bloq(f"{pre}: precisa ser objeto"); continue
        extra = set(o) - {"emUmMinuto", "resumo", "visuais"}
        if "demo" in extra: aviso(f"{pre}: campo `demo` é do código de demonstração; tire do pacote")
        if extra - {"demo"}: aviso(f"{pre}: campos que a plataforma ignora: {sorted(extra - {'demo'})}")
        if "emUmMinuto" in o and not (strs(o["emUmMinuto"]) and 1 <= len(o["emUmMinuto"]) <= 5):
            bloq(f"{pre}.emUmMinuto: lista de 1 a 5 frases")
        if "resumo" in o and not (isinstance(o["resumo"], str) and o["resumo"].strip()):
            bloq(f"{pre}.resumo: texto não vazio")
        for n, v in enumerate(o.get("visuais", []) if isinstance(o.get("visuais", []), list) else [None]):
            pv = f"{pre}.visuais[{n}]"
            if not isinstance(v, dict) or v.get("tipo") not in TIPOS:
                bloq(f"{pv}: tipo precisa ser um de {list(TIPOS)} (a página quebra o curso do tópico se faltar campo)"); continue
            for c in TIPOS[v["tipo"]]:
                if c not in v: bloq(f"{pv} ({v['tipo']}): falta `{c}`")
            if v["tipo"] == "fluxo" and "passos" in v and not (strs(v["passos"]) and 2 <= len(v["passos"]) <= 8):
                bloq(f"{pv}: passos = lista de 2 a 8 textos")
            if v["tipo"] == "tabela" and "colunas" in v and "linhas" in v:
                if not strs(v["colunas"]): bloq(f"{pv}: colunas = lista de textos")
                ruins = [i for i, r in enumerate(v["linhas"]) if not isinstance(r, list) or len(r) != len(v["colunas"])]
                if ruins: bloq(f"{pv}: linhas {ruins} com número de células diferente das colunas")
            if v["tipo"] == "linha" and "marcos" in v and not all(isinstance(m, dict) and "quando" in m and "texto" in m for m in v["marcos"]):
                bloq(f"{pv}: cada marco precisa de quando e texto")
            if v["tipo"] == "esquema" and "ramos" in v and not strs(v["ramos"]): bloq(f"{pv}: ramos = lista de textos")
            if v["tipo"] == "barras" and "dados" in v:
                if not all(isinstance(d, dict) and "rotulo" in d and isinstance(d.get("valor"), (int, float)) for d in v["dados"]):
                    bloq(f"{pv}: cada dado precisa de rotulo e valor numérico")
                if not v.get("fonte"): bloq(f"{pv}: gráfico de barras sem fonte (ordem E exige fonte oficial e data)")
            if v["tipo"] == "compare" and "linhas" in v:
                ruins = [i for i, r in enumerate(v["linhas"]) if not (isinstance(r, list) and len(r) == 3 and all(isinstance(c, str) for c in r))]
                if ruins: bloq(f"{pv}: cada linha do compare = [aspecto, lado A, lado B]; erradas: {ruins}")
                if len(v["linhas"]) > 6: aviso(f"{pv}: compare com {len(v['linhas'])} linhas (no celular, o ideal é até 6)")
            if v["tipo"] == "baseLegal" and "dispositivos" in v:
                for k, d in enumerate(v["dispositivos"] if isinstance(v["dispositivos"], list) else []):
                    if not (isinstance(d, dict) and d.get("ref") and d.get("texto")): bloq(f"{pv}.dispositivos[{k}]: precisa de ref e texto"); continue
                    if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(d.get("conferido") or "")):
                        bloq(f"{pv}.dispositivos[{k}] ({d.get('ref')}): sem data de conferência do QA Normativo (AAAA-MM-DD); dispositivo não conferido não vai para a candidata")
                    if "literal" not in d: aviso(f"{pv}.dispositivos[{k}]: diga se é texto literal (true) ou paráfrase (false)")
                    if re.search(r"demonstra[çc][ãa]o de formato", d.get("texto", ""), re.I): bloq(f"{pv}: texto de demonstração no pacote")
            if not v.get("titulo") and v["tipo"] != "fluxo": aviso(f"{pv}: sem titulo")
    info(f"topicos com conteúdo: {len(T)} ({', '.join(sorted(T))})")

# ---------- 4. Marcas de produção no texto que a candidata lê ----------
MARCAS = r"\[V \d|\[NORMATIVO|\[F\d+\]|\b(?:A5|BQ|L\d[A-Z]?|6[AB]|4C|5C)-[QR]?\d+\b|\bpar(?:es)? C\d+|Só o fato e a fonte|\bLote \d"
def conta(P):
    n = 0
    for l in P.get("lotes", []):
        for c in ("curso", "resumo"): n += len(re.findall(MARCAS, l.get(c) or ""))
        for p in l.get("pegadinhas") or []: n += len(re.findall(MARCAS, p.get("texto") or ""))
    for i in P.get("itens", []): n += len(re.findall(MARCAS, i.get("justificativa") or ""))
    for o in (P.get("topicos") or {}).values():
        if isinstance(o, dict): n += len(re.findall(MARCAS, json.dumps(o, ensure_ascii=False)))
    return n
mb, mn = conta(B), conta(N)
info(f"marcas de produção (padrões principais da ordem C; contagem completa no inventário): {mb} no pacote em uso → {mn} no novo")
if mn > mb: aviso("o pacote novo tem MAIS marcas de produção que o atual")

# ---------- 5. Números ----------
cb = collections.Counter(i["itemEdital"] for i in B["itens"]); cn = collections.Counter(i["itemEdital"] for i in itens)
plat = [k for k in cn if k[:2] in ("P1", "P2")]
info(f"itens {len(B['itens'])} → {len(itens)} (novos {len(novos)}, removidos {len(sumiram)}); lotes {len(B['lotes'])} → {len(N.get('lotes', []))}; "
     f"simulados {len(B['simulados'])} → {len(N.get('simulados', []))}; discursivas {len(B.get('discursivas', []))} → {len(N.get('discursivas', []))}")
info(f"voláteis {sum(1 for i in B['itens'] if i.get('volatil'))} → {sum(1 for i in itens if i.get('volatil'))}")
info(f"tópicos de P1/P2 com 30+ questões (nota possível, só questões distintas): {sorted(k for k in plat if cn[k] >= 30) or 'nenhum'}; "
     f"com 40+: {sorted(k for k in plat if cn[k] >= 40) or 'nenhum'}; máximo {max(cn[k] for k in plat) if plat else 0}")
for c in CAMPOS_INFO:
    if mud[c]: info(f"{c} mudou em {len(mud[c])} item(ns): {mud[c][:12]}{' …' if len(mud[c]) > 12 else ''}")
if N.get("nome") == B.get("nome") and N.get("geradoEm") == B.get("geradoEm") and not novos and not sumiram and not any(mud.values()):
    info("conteúdo idêntico ao pacote em uso")

# ---------- Relatório ----------
h = hashlib.sha256(open(a.novo, "rb").read()).hexdigest()
L = [f"# Conferência de entrada — {N.get('nome', '?')} (geradoEm {N.get('geradoEm', '?')})", "",
     f"Arquivo: `{a.novo}` · sha256 {h}", f"Base: `{a.base}` ({B.get('nome')}, {len(B['itens'])} itens)",
     f"Registro de alterações: {a.registro or 'não informado'}", "",
     f"**Resultado: {'BLOQUEADO — não seguir para a regressão' if BLOQ else 'pode seguir para a regressão'}** ({len(BLOQ)} bloqueio(s), {len(AVISO)} aviso(s))", ""]
for tit, lst in [("Bloqueios", BLOQ), ("Avisos", AVISO), ("Informações", INFO)]:
    L.append(f"## {tit}"); L += [f"- {x}" for x in lst] or ["- nenhum"]; L.append("")
rel = "\n".join(L)
if a.saida: open(a.saida, "w", encoding="utf-8").write(rel)
print(rel)
sys.exit(1 if BLOQ else 0)
