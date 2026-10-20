# moldura_ce.py — T-122 (D-MOLDURA-CE) — 2026-10-20 — gerado por gcb-cpp
# Somente leitura sobre o pacote; grava só o CSV de itens. Reprodutível:
#   python3 -I saida/banco/moldura_ce.py [raiz do repositório]
# Entrada : saida/pacote/pacote.json (v1.13 canônico, SHA-256 82c4117c…f240; o script aborta se diferir)
# Saída   : saida/banco/moldura_ce_itens_2026-10-20.csv  (UTF-8, LF; separador ";"; ordem do pacote)
#           colunas: id;materia;itemEdital;gabarito;moldura;termo;borda;sinal_fraco
# Também imprime, em stdout, os totais por matéria e por folha (tabelas usadas no .md de contagem).
#
# CRITÉRIO (ver também saida/banco/moldura_ce_contagem_2026-10-20.md, seção 1)
#  Texto avaliado = comando + textoBase + enunciado (NUNCA a justificativa, o certame ou a url).
#  moldura = S quando o texto põe a situação no Poder Legislativo: Câmara dos Deputados / "a Câmara",
#  Congresso, Senado, parlamento (nacional, estrangeiro ou genérico), Deputado, Senador, parlamentar,
#  vereador atuando como tal, "órgão/Casa do Poder Legislativo", Plenário, sessão plenária, comissão
#  (legislativa), "a Casa" (maiúscula), Mesa, Derep/DETAQ/taquigrafia, Pequeno Expediente etc.
#  moldura = N quando o texto só cita lei/edital/norma, cita o Legislativo em rol com outros Poderes,
#  usa "legislativo/a" em sentido de função ou de norma (delegação, autorização, técnica legislativa),
#  usa "câmara" em sentido não legislativo, ou usa só termos fracos ("sessão", "orador", "audiência"...)
#  sem âncora institucional. Termos fracos presentes em itens N vão para a coluna sinal_fraco.
#  Colunas auxiliares: borda = decisão de fronteira aplicada (vazio se a moldura é inequívoca).
import sys, os, re, json, csv, hashlib, math, collections

RAIZ = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
PACOTE = os.path.join(RAIZ, "saida", "pacote", "pacote.json")
SAIDA = os.path.join(RAIZ, "saida", "banco", "moldura_ce_itens_2026-10-20.csv")
SHA_ESPERADO = "82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240"

raw = open(PACOTE, "rb").read()
assert hashlib.sha256(raw).hexdigest() == SHA_ESPERADO, "pacote.json difere da v1.13 canônica"
itens = json.loads(raw.decode("utf-8"))["itens"]
assert len(itens) == 1159

def materia(ie):
    if ie.startswith("P1-DA"): return "P1-DA"
    if ie.startswith("P1-"): return "P1-TI"
    if ie.startswith("P2-"): return "P2"
    raise ValueError(ie)

I = re.I
# (nome, regex, escopo, borda)   escopo: "todas" ou "naoDA" (matéria diferente de P1-DA)
# borda != "" marca decisão de fronteira (o item é S, mas por critério de borda registrado no .md).
T = [
 ("Câmara",        re.compile(r"\bC[âa]mara\b(?!\s+de\s+Com[ée]rcio|\s+Arbitral)"), "todas", ""),     # maiúscula: câmara/sala fica fora
 ("Congresso",     re.compile(r"\bCongresso\b"), "todas", ""),
 ("Senado",        re.compile(r"\bSenad(?:o|or|ora|ores)\b"), "todas", ""),
 ("Deputado",      re.compile(r"\bDeputad[oa]s?\b", I), "todas", ""),
 ("parlamentar",   re.compile(r"\b(?:inter)?parlament\w*", I), "todas", ""),
 ("Poder Legislativo", re.compile(r"\bPoder(?:es)?\s+Legislativo\b"), "todas", ""),                      # com guarda de rol (abaixo)
 ("órgão/Casa legislativa", re.compile(r"\b(?:[óo]rg[ãa]os?|[Cc]asas?)\s+[Ll]egislativ[oa]s?\b"), "todas", ""),
 ("sessão legislativa", re.compile(r"\bsess(?:ão|ões)\s+legislativ[oa]s?\b", I), "todas", ""),
 ("Assembleia Legislativa", re.compile(r"\bassembleia\s+(?:legislativa|distrital|constituinte)\b", I), "todas", ""),
 ("assembleia (P2)", re.compile(r"\bassembleia\b(?!\s+(?:geral|de\s+(?:acionistas|credores|cond[ôo]minos|cotistas)))", I), "naoDA", "assembleia"),
 ("vereador",      re.compile(r"(?<!mandato de )\bvereador(?:es|a|as)?\b", I), "todas", ""),         # "mandato de vereador" excluído (regime do servidor)
 ("Plenário",      re.compile(r"\bplen[áa]ri[oa]s?\b(?!\s+d[oa]\s+(?:STF|Supremo|Tribunal|TCU|CNJ|CNMP))", I), "todas", ""),
 ("comissão",      re.compile(r"\bcomiss(?:ão|ões)\b", I), "naoDA", ""),                              # em P1-DA "comissão" = cargo em comissão/comissão processante/licitação
 ("comissão parlamentar/legislativa (DA)", re.compile(r"\bcomiss(?:ão|ões)\s+(?:permanentes?|tem[áa]ticas?|mistas?|parlamentar(?:es)?)\b", I), "soDA", ""),
 ("Casa",          re.compile(r"\bCasa\b(?!\s+Civil)"), "todas", ""),                                 # "a Casa" = Câmara; Casa Civil e "casa" (imóvel) ficam fora
 ("Mesa",          re.compile(r"\bMesa\b"), "todas", ""),
 ("CPI",           re.compile(r"\b(?:CPIs?|C\.P\.I\.?)", ), "todas", "cpi"),
 ("Derep/Registro Oficial", re.compile(r"\b(?:Derep|DETAQ)\b|\bRegistro Oficial\b|\bPequeno Expediente\b|\bColégio de Líderes\b"), "todas", ""),   # "taquigrafia", "questão de ordem", "tribuna" e "registro oficial" (minúsc.) são só sinal fraco
 ("domínio legislativo", re.compile(r"\bdom[ií]nio[^.;]{0,30}\blegislativ[oa]\b|\bproposi[çc](?:ão|ões)\s+legislativ[oa]s?\b", I), "todas", "dominio"),
]
# Cenas estrangeiras: o S é mantido, mas a borda "estrangeiro" é registrada.
ESTRANG = re.compile(r"Comuns do Canad|Deputados da It[áa]lia|Senado da It[áa]lia|Parlamento da Est[ôo]nia|Conselho de Representantes do Bahrein", I)
# Rol: "Poder Legislativo" ao lado de outro Poder/Ministério Público não é moldura.
ROL_ANTES = re.compile(r"(?:Executivo|Judici[áa]rio|Minist[ée]rio P[úu]blico)(?:,|\s+e|\s+ou)?(?:\s+o)?\s*$", I)
ROL_DEPOIS = re.compile(r"^\s*(?:,|e|ou)?\s*(?:o\s+)?(?:Poder(?:es)?\s+)?(?:Executivo|Judici[áa]rio|Minist[ée]rio)", I)
# Cena de órgão: "órgão/servidor/Casa ... do Poder Legislativo" no raio de 40 caracteres antes; senão é "Poder isolado" (borda).
CENA_PODER = re.compile(r"(?:[óo]rg[ãa]os?|servidor(?:es)?|Casas?|unidade|setor|cargo)[^.]{0,40}$", I)
# Termos fracos (só para a coluna sinal_fraco dos itens N).
FRACOS = [("sessão", r"\bsess(?:ão|ões)\b"), ("orador", r"\borador(?:es)?\b"), ("audiência", r"\baudi[êe]ncias?\b"),
          ("pronunciamento", r"\bpronunciamentos?\b"), ("discurso", r"\bdiscursos?\b"), ("proposição", r"\bproposi[çc](?:ão|ões)\b"),
          ("legislativ(o/a)", r"\blegislativ[oa]s?\b"), ("Poder em rol", r"\bPoder(?:es)?\s+Legislativo\b|\bo Legislativo\b"),
          ("mandato de vereador", r"mandato de vereador"), ("taquigrafia", r"\btaqu[ií]gr\w*"), ("questão de ordem", r"\bquest[ãa]o de ordem\b"), ("tribuna", r"\btribuna\b"), ("registro oficial", r"\bregistro oficial\b"), ("ata", r"\batas?\b"), ("diário", r"\bdi[áa]rios?\b"), ("câmara (sentido não legislativo)", r"\bc[âa]mara\b")]
FRACOS = [(n, re.compile(r, I)) for n, r in FRACOS]
USO_MENCAO = re.compile(r"[\"“”]\s*C[âa]mara\s*[\"“”]")   # palavra citada entre aspas (menção, não cena)

def texto(it):
    t = " ".join([it.get("comando", ""), it.get("textoBase", ""), it.get("enunciado", "")])
    return USO_MENCAO.sub("«palavra»", t).replace("\n", " ")

def classificar(it):
    t = texto(it); mat = materia(it["itemEdital"])
    ach = []   # (pos, nome, trecho, borda)
    for nome, rx, esc, borda in T:
        if esc == "naoDA" and mat == "P1-DA": continue
        if esc == "soDA" and mat != "P1-DA": continue
        for m in rx.finditer(t):
            b = borda
            if nome == "Poder Legislativo":
                if ROL_ANTES.search(t[max(0, m.start() - 30):m.start()]) or ROL_DEPOIS.search(t[m.end():m.end() + 40]):
                    continue
                if not CENA_PODER.search(t[max(0, m.start() - 60):m.start()]): b = "poder_isolado"
            ach.append((m.start(), nome, m.group(0), b))
    ach.sort()
    if not ach:
        fr = sorted({n for n, rx in FRACOS if rx.search(t)})
        return "N", "", "", ";".join(fr)
    nomes = []
    for _, n, tr, _b in ach:
        s = tr if n in ("Câmara", "Deputado", "Plenário") else tr.lower() if len(tr) > 3 else tr
        if s not in nomes: nomes.append(s)
    borda = ""
    bs = [b for *_, b in ach]
    # a moldura é inequívoca se algum termo sem borda disparou; senão fica a borda do primeiro termo
    if all(bs): borda = bs[0]
    if mat == "P1-TI" and all(n == "comissão" for _, n, _t, _b in ach): borda = "comissao_sem_ancora"   # TI: "comissão" sem Câmara/parlamentar
    if ESTRANG.search(t) and not any(not b for b in bs if b != "estrangeiro"):
        borda = "estrangeiro"
    elif ESTRANG.search(t) and not borda:
        borda = "estrangeiro"
    return "S", "; ".join(nomes[:3]), borda, ""

linhas = []
for it in itens:
    mol, termo, borda, fraco = classificar(it)
    linhas.append([it["id"], materia(it["itemEdital"]), it["itemEdital"], it["gabarito"], mol, termo, borda, fraco])

with open(SAIDA, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter=";", lineterminator="\n")
    w.writerow(["id", "materia", "itemEdital", "gabarito", "moldura", "termo", "borda", "sinal_fraco"])
    w.writerows(linhas)

# ---- totais ----
def tot(sel):
    n = len(sel); c = sum(1 for r in sel if r[3] == "C"); e = n - c
    pct = 100.0 * c / n if n else 0.0
    # E faltante p/ %C <= 60% (dado auxiliar): x = ceil(C/0,60 - (C+E)) se %C > 60%, senão 0; em inteiros: 5C > 3(C+E) <=> 2C > 3E; x = ceil((2C-3E)/3)
    x = -(-(2 * c - 3 * e) // 3) if 2 * c > 3 * e else 0
    return n, c, e, pct, x
def lin(nome, sel):
    n, c, e, pct, x = tot(sel)
    return "| %s | %d | %d | %d | %.1f%% | %d |" % (nome, n, c, e, pct, x)
S = [r for r in linhas if r[4] == "S"]
print("# TOTAIS POR MATÉRIA (apenas itens com moldura S): itens | C | E | %C | E faltante p/ %C<=60%")
for m in ("P1-TI", "P2", "P1-DA"):
    print(lin(m, [r for r in S if r[1] == m]))
print(lin("TOTAL", S))
print("# UNIVERSO por matéria: itens | S | %S")
for m in ("P1-TI", "P2", "P1-DA"):
    u = [r for r in linhas if r[1] == m]; s = [r for r in u if r[4] == "S"]
    print("| %s | %d | %d | %.1f%% |" % (m, len(u), len(s), 100.0 * len(s) / len(u)))
print("# POR FOLHA")
for m in ("P1-TI", "P2", "P1-DA"):
    fo = sorted({r[2] for r in linhas if r[1] == m}, key=lambda s: [int(x) if x.isdigit() else 0 for x in re.split(r"[.\-]", s.replace("P1-DA", "").replace("P1", "").replace("P2", ""))])
    for fl in fo:
        u = [r for r in linhas if r[2] == fl]; s = [r for r in u if r[4] == "S"]
        n, c, e, pct, x = tot(s)
        print("| %s | %s | %d | %d | %d | %d | %s | %d |" % (m, fl, len(u), n, c, e, ("%.1f%%" % pct) if n else "—", x))
print("# S POR BORDA: borda | n | C | E")
for b in sorted({r[6] for r in S if r[6]}):
    sel = [r for r in S if r[6] == b]; n, c, e, pct, x = tot(sel)
    print("| %s | %d | %d | %d |" % (b, n, c, e))
sel = [r for r in S if not r[6]]; n, c, e, pct, x = tot(sel)
print("| (sem borda) | %d | %d | %d |" % (n, c, e))
print("# N COM SINAL FRACO (implícitos; NÃO contados em S): matéria | n | C | E")
for m in ("P1-TI", "P2", "P1-DA"):
    sel = [r for r in linhas if r[1] == m and r[4] == "N" and r[7]]
    print("| %s | %d | %d | %d |" % (m, len(sel), sum(1 for r in sel if r[3] == "C"), sum(1 for r in sel if r[3] == "E")))
print("# DA: folhas com moldura, ordenadas por %C desc, n desc, folha")
da = []
for fl in sorted({r[2] for r in S if r[1] == "P1-DA"}):
    n, c, e, pct, x = tot([r for r in S if r[2] == fl]); da.append((-pct, -n, fl, n, c, e, x))
nat = lambda fl: [int(v) for v in re.findall(r"\d+", fl.replace("P1-DA", ""))]
for _, _, fl, n, c, e, x in sorted(da, key=lambda t: (t[0], t[1], nat(t[2]))):
    print("| %s | %d | %d | %d | %.1f%% | %d |" % (fl, n, c, e, 100.0 * c / n, x))
