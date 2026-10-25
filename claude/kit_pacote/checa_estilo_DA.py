#!/usr/bin/env python3
"""Conferência de ESTILO DA BANCA para itens de Direito Administrativo de um pacote da Fábrica (somente leitura, só AVISOS).

Aplica as regras de produção propostas em regras/estilo_banca_DA_v1.md (seção 6; corpus Cebraspe 2025, 1.118 itens C/E):
  1. por lote de AUTORAL: 40–60% C; mecanismos distribuídos (C: maioria LIT + 1–2 AP; E: CON 3–4, SUP 2–3, GEN 1, NEG 1, PRA/AUT/AMB/TEM 1–2 por 20 itens)
  2. nenhum item E construído só com absolutizador em frase que a lei não contém (heurística: E + absolutizador + mecanismo GEN acima da cota)
  3. enunciado de 21 a 35 palavras (55% dos itens da banca; mediana 30); comando nomeando 2–3 temas; fechamento sorteado entre os seis da banca
  4. caso concreto (texto-base/personagem/"Considere", "Suponha", "situação hipotética") em 5–10% dos itens, não em metade
  5. campo `mecanismo` presente nos itens de lotes DA-v2 (código da tabela da seção 4) e `comentario.decisiva` nomeando o mecanismo

Nada aqui é BLOQUEIO: o script produz um relatório de desvios para a produção e para o QA didático; quem decide é a GCB.
Complementa (não substitui) checa_pacote_v2.py.

Uso:
  python3 -I checa_estilo_DA.py <pacote.json ou index.html> [--lote L] [--saida relatorio.md] [--so-v2]

Testado em 24/10/2026 contra um pacote sintético; não foi rodado contra o pacote vigente da Fábrica (sem acesso ao repositório
nesta sessão). Ajustar os nomes de campos se o contrato do pacote divergir (ver checa_pacote_v2.py, seção 1).
"""
import json, re, sys, collections, argparse, statistics

ap = argparse.ArgumentParser()
ap.add_argument("pacote")
ap.add_argument("--lote", help="só este lote (id)")
ap.add_argument("--saida")
ap.add_argument("--so-v2", action="store_true", help="só lotes com formato DA-v2")
a = ap.parse_args()

def carrega(caminho):
    txt = open(caminho, encoding="utf-8").read()
    if caminho.endswith(".html"):
        linha = next((l for l in txt.split("\n") if l.startswith("const PUB_INLINE")), None)
        if not linha: raise SystemExit("base sem a linha const PUB_INLINE")
        js = linha[linha.index("=") + 1:].strip().rstrip(";")
        return json.loads(js)
    return json.loads(txt)

try:
    P = carrega(a.pacote)
except Exception as e:
    print("ERRO de leitura:", e); sys.exit(2)

MECANISMOS = ["LIT", "CON", "SUP", "PRA", "GEN", "AP", "MIX", "NEG", "AUT", "AMB", "TEM"]
# cotas por 20 itens (seção 6, regra 1); escalam com o tamanho do lote
COTA_E = {"CON": (3, 4), "SUP": (2, 3), "GEN": (1, 1), "NEG": (1, 1)}
COTA_E_OUTROS = (1, 2)   # PRA/AUT/AMB/TEM somados
ABSOLUT = re.compile(r"\b(sempre|somente|apenas|exclusivamente|necessariamente|obrigatoriamente|em qualquer hip[óo]tese|independentemente|todos?|toda|qualquer|nunca|jamais|em nenhuma hip[óo]tese)\b", re.I)
CASO = re.compile(r"\b(Considere|Suponha|Imagine|situa[çc][ãa]o hipot[ée]tica|Nessa situa[çc][ãa]o|caso hipot[ée]tico)\b|\b[A-Z][a-zã-ú]+,\s+(servidor|servidora|agente|empregad[oa]|funcion[áa]ri[oa]|prefeit[oa]|secret[áa]ri[oa]|diretor[a]?)\b")
FECHOS = ["o item a seguir", "o item seguinte", "o item subsequente", "o próximo item", "o item que se segue", "o seguinte item"]
ABERTURAS = ["Julgue o item", "A respeito de", "Acerca de", "Com base", "No que se refere", "Em relação", "Considerando", "À luz", "De acordo com", "No que concerne", "Com relação"]

def modulo(x): x = str(x or ""); return "DA" if re.match(r"^(P1-)?DA-", x) else x[:2]
def palavras(t): return len(re.findall(r"\w+(?:-\w+)*", t or "", re.UNICODE))
def separa(item):
    """Comando e item. No pacote da Fábrica o comando vem no campo `comando` e o item em `enunciado` (pacote_contrato.md);
    se vier tudo em `enunciado`, separa até 'julgue ... :' ou primeiro '.' (heurística, só para medir). Aceita dict ou string."""
    if isinstance(item, dict):
        if (item.get("comando") or "").strip(): return item["comando"].strip(), (item.get("enunciado") or "").strip()
        e = (item.get("enunciado") or "").strip()
    else: e = (item or "").strip()
    m = re.search(r"(?is)^(.*?julgue[^.:]*[.:])\s*(.*)$", e)
    if m: return m.group(1).strip(), m.group(2).strip()
    return "", e

AV, INF = [], []
def av(t): AV.append(t)
def inf(t): INF.append(t)

itens = P.get("itens", [])
lotes = P.get("lotes", [])
if a.so_v2: lotes = [l for l in lotes if l.get("formato") == "DA-v2"]
if a.lote: lotes = [l for l in lotes if l.get("id") == a.lote]
M = {i.get("id"): i for i in itens}

def analisa(nome, its, exige_mec):
    n = len(its)
    if n == 0: return
    C = sum(1 for i in its if i.get("gabarito") == "C")
    pc = 100 * C / n
    inf(f"{nome}: {n} itens, {C} C ({pc:.0f}%)")
    if not (40 <= pc <= 60): av(f"{nome}: {pc:.0f}% C fora da faixa 40–60% (banca 2025: 49% C)")
    # comprimento do item (sem o comando)
    comp = []
    for i in its:
        cmd, it = separa(i)
        comp.append(palavras(it))
    med = statistics.median(comp) if comp else 0
    dentro = sum(1 for c in comp if 21 <= c <= 35)
    inf(f"{nome}: mediana de {med:.0f} palavras no item; {100*dentro/n:.0f}% entre 21 e 35 (banca: mediana 30, 55% na faixa)")
    longos = [i["id"] for i, c in zip(its, comp) if c > 60]
    curtos = [i["id"] for i, c in zip(its, comp) if c < 12]
    if longos: av(f"{nome}: {len(longos)} item(ns) com mais de 60 palavras (a banca passa de 80 em 0,5% dos itens): {longos[:8]}")
    if curtos: av(f"{nome}: {len(curtos)} item(ns) com menos de 12 palavras: {curtos[:8]}")
    # caso concreto
    casos = [i["id"] for i in its if CASO.search(i.get("enunciado") or "") or i.get("tipo") == "caso"]
    pcaso = 100 * len(casos) / n
    inf(f"{nome}: {len(casos)} item(ns) de caso concreto ({pcaso:.0f}%; banca 2025: 5–6%; meta de produção 5–10%)")
    if pcaso > 15: av(f"{nome}: {pcaso:.0f}% de caso concreto — acima da meta de 5–10% (ESTILO §6.4); a banca cobra assertiva, não narrativa")
    # absolutizadores
    abs_E = [i["id"] for i in its if i.get("gabarito") == "E" and ABSOLUT.search(separa(i)[1])]
    abs_C = [i["id"] for i in its if i.get("gabarito") == "C" and ABSOLUT.search(separa(i)[1])]
    pabs = 100 * (len(abs_E) + len(abs_C)) / n
    inf(f"{nome}: absolutizador em {pabs:.0f}% dos itens ({len(abs_E)} E, {len(abs_C)} C; banca: ~10% dos itens, e só 55–65% deles são E)")
    if len(abs_E) > max(2, round(0.10 * n)): av(f"{nome}: {len(abs_E)} itens E com absolutizador (cota sugerida ≈ 10% do lote); conferir se o erro é só o 'sempre/somente' (ESTILO §6.2): {abs_E[:8]}")
    if abs_E and not abs_C: av(f"{nome}: todo absolutizador do lote está em item E — a candidata aprende um reflexo que a banca não confirma (banca: ~40% dos absolutizadores estão em itens C)")
    # mecanismos
    mec = collections.Counter((i.get("mecanismo") or "").upper() for i in its)
    sem = [i["id"] for i in its if not i.get("mecanismo")]
    desconhecidos = sorted(k for k in mec if k and k not in MECANISMOS)
    if desconhecidos: av(f"{nome}: códigos de mecanismo fora da tabela da seção 4: {desconhecidos}")
    if sem:
        (av if exige_mec else inf)(f"{nome}: {len(sem)} item(ns) sem campo `mecanismo`{' (obrigatório em DA-v2, ESPEC v2.1)' if exige_mec else ''}: {sem[:8]}")
    if n - len(sem) >= 10:
        fator = n / 20
        E_its = [i for i in its if i.get("gabarito") == "E"]
        C_its = [i for i in its if i.get("gabarito") == "C"]
        mecE = collections.Counter((i.get("mecanismo") or "").upper() for i in E_its)
        mecC = collections.Counter((i.get("mecanismo") or "").upper() for i in C_its)
        inf(f"{nome}: mecanismos E = {dict(mecE)}; C = {dict(mecC)}")
        for k, (lo, hi) in COTA_E.items():
            v = mecE.get(k, 0)
            if v < lo * fator - 0.5 or v > hi * fator + 0.5: av(f"{nome}: E/{k} = {v} (cota ≈ {lo*fator:.0f}–{hi*fator:.0f} para {n} itens)")
        outros = sum(mecE.get(k, 0) for k in ("PRA", "AUT", "AMB", "TEM"))
        if outros > COTA_E_OUTROS[1] * fator + 0.5: av(f"{nome}: E/PRA+AUT+AMB+TEM = {outros} (cota ≈ {COTA_E_OUTROS[0]*fator:.0f}–{COTA_E_OUTROS[1]*fator:.0f})")
        lit = mecC.get("LIT", 0)
        if C_its and lit < 0.5 * len(C_its): av(f"{nome}: só {lit} de {len(C_its)} itens C são LIT (banca: item C é literal em 99% dos casos)")
        ap_ = mecC.get("AP", 0)
        if ap_ > 2 * fator + 0.5: av(f"{nome}: {ap_} itens C de caso aplicado (AP) — cota 1–2 por 20")
        if mecE.get("LIT", 0): av(f"{nome}: {mecE['LIT']} item(ns) E marcados LIT — LIT é 99% C; conferir classificação: {[i['id'] for i in E_its if (i.get('mecanismo') or '').upper()=='LIT'][:6]}")
        if mecC.get("GEN", 0) or mecC.get("NEG", 0): av(f"{nome}: itens C marcados GEN/NEG — na banca GEN é 96% E e NEG 100% E; conferir")
    # comentário nomeia o mecanismo
    if exige_mec:
        sem_nome = []
        for i in its:
            c = i.get("comentario") or {}
            mk = (i.get("mecanismo") or "").upper()
            if mk and isinstance(c, dict) and mk not in (c.get("decisiva") or "").upper(): sem_nome.append(i["id"])
        if sem_nome: av(f"{nome}: {len(sem_nome)} item(ns) cujo comentario.decisiva não nomeia o mecanismo ({'/'.join(MECANISMOS)}): {sem_nome[:8]}")
    # comando: variedade de abertura e fechamento; temas nomeados
    fechos = collections.Counter(); aberturas = collections.Counter(); sem_cmd = 0; um_tema = 0
    for i in its:
        cmd, _ = separa(i)
        if not cmd: sem_cmd += 1; continue
        f = next((f for f in FECHOS if f in cmd.lower()), "outro"); fechos[f] += 1
        ab = next((x for x in ABERTURAS if cmd.lower().startswith(x.lower())), "outra"); aberturas[ab] += 1
        if cmd.count(",") + cmd.count(" e ") == 0: um_tema += 1
    if sem_cmd > 0.5 * n: inf(f"{nome}: {sem_cmd} item(ns) sem comando 'julgue…' detectável (o comando pode estar em campo separado; medida não aplicada)")
    else:
        inf(f"{nome}: fechamentos {dict(fechos)}; aberturas {dict(aberturas)}")
        top = fechos.most_common(1)[0] if fechos else None
        if top and top[1] > 0.7 * (n - sem_cmd) and n - sem_cmd >= 10: av(f"{nome}: fechamento '{top[0]}' em {top[1]} de {n-sem_cmd} comandos — sortear entre os seis da banca (52/14/10/8/8/4%)")
        if fechos.get("outro", 0) > 0.1 * n: av(f"{nome}: {fechos['outro']} comando(s) com fechamento fora dos seis usados pela banca")
        if um_tema > 0.5 * (n - sem_cmd) and n - sem_cmd >= 10: av(f"{nome}: {um_tema} comando(s) nomeiam um único tema — a banca nomeia 2–3 para não entregar o assunto")

# por lote
vistos = set()
for l in lotes:
    # itens do lote: pela convenção da Fábrica o id do item começa pelo id do lote ("D1-01" ∈ D1); só sem esse prefixo cai no enquadramento por itemEdital
    pref = str(l.get("id") or "") + "-"
    its = [i for i in itens if str(i.get("id", "")).startswith(pref) and modulo(i.get("itemEdital")) == "DA"]
    if not its: its = [i for i in itens if i.get("itemEdital") in (l.get("itensEdital") or []) and modulo(i.get("itemEdital")) == "DA"]
    if not its: continue
    vistos |= {i["id"] for i in its}
    analisa(f"lote {l.get('id')}", its, exige_mec=(l.get("formato") == "DA-v2"))
# itens de DA fora de lote (reais do banco, por exemplo)
resto = [i for i in itens if modulo(i.get("itemEdital")) == "DA" and i["id"] not in vistos]
if resto and not a.lote and not a.so_v2:
    analisa("itens de DA fora dos lotes listados (banco)", resto, exige_mec=False)

L = [f"# Estilo da banca — conferência de itens de DA — {P.get('nome', '?')} (geradoEm {P.get('geradoEm', '?')})", "",
     "Referência: regras/estilo_banca_DA_v1.md (corpus Cebraspe 2025, 1.118 itens C/E; porcentagens ±3 pontos). Só avisos; nenhum bloqueio.", "",
     f"**{len(AV)} aviso(s)**", "", "## Avisos"] + ([f"- {x}" for x in AV] or ["- nenhum"]) + ["", "## Medidas"] + ([f"- {x}" for x in INF] or ["- nenhuma"]) + [""]
rel = "\n".join(L)
if a.saida: open(a.saida, "w", encoding="utf-8").write(rel)
print(rel)
sys.exit(0)
