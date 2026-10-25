#!/usr/bin/env python3
"""Conferência de entrada de um pacote novo da Fábrica na plataforma Câmara 2026 (somente leitura) — v2 (24/10/2026).

v2 = checa_pacote.py (18–19/10) + regras da ESPEC_curso_DA_formato_v2 para lotes/tópicos marcados formato "DA-v2"
(tarefas, GLOSSÁRIO, CASO, RESPOSTA DO CASO, ITEM intercalado, comentario em 3 linhas, fechamento, escopo, par da pegadinha,
proibição de referência a material de terceiro). Lotes sem a marca seguem só as regras da v1.

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
MECANISMOS_V21 = {"LIT", "CON", "SUP", "PRA", "GEN", "AP", "MIX", "NEG", "AUT", "AMB", "TEM"}  # regras/estilo_banca_DA_v1.md §4 (adendo v2.1)
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
        extra = set(o) - {"emUmMinuto", "resumo", "visuais", "formato", "tarefas", "fechamento", "escopo"}
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


# ---------- 3b. Formato DA-v2 (ESPEC_curso_DA_formato_v2, 24/10/2026) ----------
QUADROS_V1 = {"DEFINIÇÃO", "BASE LEGAL", "EXEMPLO PARLAMENTAR", "PEGADINHA PROVÁVEL"}
QUADROS_V2 = QUADROS_V1 | {"GLOSSÁRIO", "CASO", "RESPOSTA DO CASO"}
TERCEIRO = re.compile(r"Estrat[ée]gia Concursos|Herbert|\bp\.\s?\d+ da aula|\bAula \d\d\b|curso 353871", re.I)
LIM = 280
lotes_v2 = [l for l in N.get("lotes", []) if l.get("formato") == "DA-v2"]
top_v2 = {k: v for k, v in (T or {}).items() if isinstance(v, dict) and v.get("formato") == "DA-v2"} if isinstance(T, dict) else {}
if lotes_v2 or top_v2:
    info(f"formato DA-v2: {len(lotes_v2)} lote(s), {len(top_v2)} tópico(s)")
ids_lotes_v2 = set()
for l in lotes_v2:
    ids_lotes_v2 |= set(l.get("itensEdital") or [])
    curso = l.get("curso") or ""
    # blocos por subitem
    partes = re.split(r"(?m)^## ", curso)
    blocos = [p for p in partes[1:]]
    if not blocos: bloq(f"lote {l['id']} (DA-v2): curso sem blocos `## <número> <TÍTULO>`")
    usados_intercalados = []
    for b in blocos:
        titulo = b.split("\n", 1)[0].strip()
        linhas = [x.strip() for x in b.split("\n")]
        quadros = [(i, x) for i, x in enumerate(linhas) if x and x == x.upper() and re.match(r"^[A-ZÁÉÍÓÚÂÊÔÃÕÇ ]+$", x)]
        nomes = [q for _, q in quadros if not q.startswith("ITEM")]
        itens_mark = [(i, x) for i, x in enumerate(linhas) if re.match(r"^ITEM\s+\S+$", x)]
        desconhecidos = [q for q in nomes if q not in QUADROS_V2]
        if desconhecidos: aviso(f"lote {l['id']} · bloco '{titulo}': linhas em maiúsculas fora da lista de quadros {sorted(set(desconhecidos))} (erro de digitação?)")
        pos = {q: i for i, q in reversed(quadros)}  # primeira ocorrência
        prim_texto = next((i for i, x in enumerate(linhas[1:], 1) if x and not (x == x.upper() and re.match(r"^[A-ZÁÉÍÓÚÂÊÔÃÕÇ ]+$", x))), None)
        if "GLOSSÁRIO" not in pos: bloq(f"lote {l['id']} · bloco '{titulo}': sem GLOSSÁRIO")
        elif prim_texto is not None and pos["GLOSSÁRIO"] > prim_texto: bloq(f"lote {l['id']} · bloco '{titulo}': GLOSSÁRIO não é o primeiro quadro (termo pode estar sendo usado antes de definido)")
        else:
            # linhas do glossário até o próximo quadro
            g0 = pos["GLOSSÁRIO"]; gl = []
            for x in linhas[g0 + 1:]:
                if x and x == x.upper() and re.match(r"^[A-ZÁÉÍÓÚÂÊÔÃÕÇ ]+$", x): break
                if x: gl.append(x)
            ruins = [x for x in gl if ":" not in x]
            if not (2 <= len(gl) <= 10): bloq(f"lote {l['id']} · bloco '{titulo}': GLOSSÁRIO com {len(gl)} linhas (2 a 10)")
            if ruins: bloq(f"lote {l['id']} · bloco '{titulo}': linhas do GLOSSÁRIO sem 'Termo: definição': {ruins[:3]}")
        if "CASO" not in pos: bloq(f"lote {l['id']} · bloco '{titulo}': sem CASO de abertura")
        elif "DEFINIÇÃO" in pos and pos["CASO"] > pos["DEFINIÇÃO"]: bloq(f"lote {l['id']} · bloco '{titulo}': CASO depois da DEFINIÇÃO")
        else:
            c0 = pos["CASO"]; ct = []
            for x in linhas[c0 + 1:]:
                if x and x == x.upper() and re.match(r"^[A-ZÁÉÍÓÚÂÊÔÃÕÇ ]+$", x): break
                if x: ct.append(x)
            if not ct or not any("?" in x for x in ct): bloq(f"lote {l['id']} · bloco '{titulo}': CASO sem pergunta")
        if "RESPOSTA DO CASO" not in pos: bloq(f"lote {l['id']} · bloco '{titulo}': sem RESPOSTA DO CASO")
        if not itens_mark: bloq(f"lote {l['id']} · bloco '{titulo}': nenhum ITEM intercalado")
        elif len(quadros) and len(itens_mark) * 3 < len(nomes): aviso(f"lote {l['id']} · bloco '{titulo}': {len(itens_mark)} ITEM para {len(nomes)} quadros (recomendado 1 a cada 3)")
        for _, x in itens_mark:
            iid = x.split(None, 1)[1]
            usados_intercalados.append(iid)
            it = M.get(iid)
            if not it: bloq(f"lote {l['id']} · bloco '{titulo}': ITEM {iid} não existe em itens"); continue
            if it.get("itemEdital") not in (l.get("itensEdital") or []): bloq(f"lote {l['id']}: ITEM {iid} é de {it.get('itemEdital')}, fora dos itensEdital do lote")
            if not isinstance(it.get("comentario"), dict): bloq(f"lote {l['id']}: ITEM {iid} sem `comentario` em três linhas")
        # pegadinha em três linhas
        if "PEGADINHA PROVÁVEL" in pos:
            p0 = pos["PEGADINHA PROVÁVEL"]; pt = []
            for x in linhas[p0 + 1:]:
                if x and x == x.upper() and re.match(r"^[A-ZÁÉÍÓÚÂÊÔÃÕÇ ]+$", x): break
                if x: pt.append(x)
            chaves = [x.split(":")[0].strip() for x in pt if ":" in x]
            if not {"A", "B", "MUDA"} <= set(chaves): bloq(f"lote {l['id']} · bloco '{titulo}': PEGADINHA PROVÁVEL sem as linhas A: / B: / MUDA:")
        # parágrafos longos
        longos = [x for x in linhas if len(re.findall(r"[.!?](\s|$)", x)) > 4 and not x.startswith("|")]
        if longos: aviso(f"lote {l['id']} · bloco '{titulo}': {len(longos)} parágrafo(s) com mais de 4 frases")
        for x in linhas:
            if x.startswith("|") and x.count("|") - 1 > 5: aviso(f"lote {l['id']} · bloco '{titulo}': tabela com mais de 4 colunas")
    # terceiro
    if TERCEIRO.search(curso) or TERCEIRO.search(l.get("resumo") or ""): bloq(f"lote {l['id']}: referência a material de terceiro no curso/resumo (D-ESTRATEGIA)")
    # pegadinhas com par
    for n, pg in enumerate(l.get("pegadinhas") or []):
        par = pg.get("par")
        if not (isinstance(par, dict) and all(isinstance(par.get(k), str) and par.get(k).strip() for k in ("a", "b", "muda"))):
            bloq(f"lote {l['id']}: pegadinhas[{n}] sem `par` {{a, b, muda}}")
        if TERCEIRO.search(pg.get("texto") or ""): bloq(f"lote {l['id']}: pegadinhas[{n}] cita material de terceiro")
    # itens do lote: comentário e duplicata intercalado × verificação
    # itens do lote pela convenção da Fábrica (id começa pelo id do lote: "D1-01" ∈ D1); só sem prefixo cai no enquadramento por itemEdital (25/10)
    its = [i for i in itens if str(i.get("id", "")).startswith(str(l.get("id") or "") + "-")] or [i for i in itens if i.get("itemEdital") in (l.get("itensEdital") or [])]
    for i in its:
        c = i.get("comentario")
        if not (isinstance(c, dict) and all(isinstance(c.get(k), str) and c.get(k).strip() for k in ("decisiva", "regra", "correta"))):
            bloq(f"lote {l['id']}: item {i['id']} sem `comentario` com decisiva/regra/correta")
        else:
            longos = [k for k in ("decisiva", "regra", "correta") if len(c[k]) > LIM]
            if longos: bloq(f"lote {l['id']}: item {i['id']} comentario.{longos} acima de {LIM} caracteres")
            if TERCEIRO.search(" ".join(c.values())): bloq(f"lote {l['id']}: item {i['id']} comentário cita material de terceiro")
        if i.get("tipo") not in (None, "literal", "caso"): aviso(f"lote {l['id']}: item {i['id']} tipo fora de literal|caso")
        # adendo v2.1 (D-ESPEC-DA-V2-1, 25/10): mecanismo obrigatório em lote DA-v2; fora da tabela é bloqueio (a plataforma ignora o código desconhecido)
        mk = i.get("mecanismo")
        if mk is None: aviso(f"lote {l['id']}: item {i['id']} sem `mecanismo` (obrigatório em DA-v2, adendo v2.1)")
        elif str(mk).upper() not in MECANISMOS_V21: bloq(f"lote {l['id']}: item {i['id']} mecanismo '{mk}' fora da tabela {sorted(MECANISMOS_V21)}")
        elif isinstance(i.get("comentario"), dict) and not str(i["comentario"].get("decisiva", "")).upper().startswith(str(mk).upper()): aviso(f"lote {l['id']}: item {i['id']} comentario.decisiva não começa pelo código do mecanismo ({mk})")
    por_top = collections.Counter(i.get("itemEdital") for i in its)
    for te in (l.get("itensEdital") or []):
        verif = por_top.get(te, 0) - sum(1 for x in usados_intercalados if M.get(x, {}).get("itemEdital") == te)
        if verif < 10: aviso(f"lote {l['id']}: tópico {te} com {verif} questão(ões) de verificação além dos intercalados (meta 10)")
for tid, o in top_v2.items():
    pre = f"topicos[{tid}]"
    tf = o.get("tarefas")
    if not (strs(tf) and 3 <= len(tf) <= 6): bloq(f"{pre}: `tarefas` precisa ser lista de 3 a 6 frases")
    else:
        ruins = [t for t in tf if not re.match(r"^Dad[oa]s?\b", t) or not re.search(r"\b(decidir|dizer|identificar|calcular|classificar|indicar|apontar|escolher|julgar|determinar)\b", t, re.I)]
        if ruins: bloq(f"{pre}: tarefas fora do formato 'Dado X, decidir Y': {ruins[:2]}")
        if any(len(t) > 220 for t in tf): aviso(f"{pre}: tarefa com mais de 220 caracteres")
    fe = o.get("fechamento")
    if not isinstance(fe, dict) or not (strs(fe.get("levar")) and len(fe["levar"]) == 5): bloq(f"{pre}: `fechamento.levar` precisa ter exatamente 5 frases")
    else:
        for k in ("literalidade", "caso"):
            if not (strs(fe.get(k)) and 1 <= len(fe[k]) <= 6): bloq(f"{pre}: `fechamento.{k}` = lista de 1 a 6 textos")
        if any(len(t) > 160 for t in fe["levar"]): aviso(f"{pre}: frase de fechamento com mais de 160 caracteres")
    if not isinstance(o.get("escopo"), list): bloq(f"{pre}: `escopo` precisa existir (lista, pode ser vazia)")
    else:
        for n, e in enumerate(o["escopo"]):
            if not (isinstance(e, dict) and e.get("tema") and e.get("onde")): bloq(f"{pre}.escopo[{n}]: precisa de tema e onde")
    if not o.get("visuais"): bloq(f"{pre}: DA-v2 exige o mapa de chegada como primeiro visual")
    if TERCEIRO.search(json.dumps(o, ensure_ascii=False)): bloq(f"{pre}: referência a material de terceiro")
    if tid not in ids_lotes_v2: aviso(f"{pre}: tópico DA-v2 sem lote DA-v2 correspondente")
for te in ids_lotes_v2:
    if te not in top_v2: bloq(f"lote DA-v2 cobre {te} mas topicos[{te}] não está no formato DA-v2 (tarefas/fechamento/escopo)")

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
