#!/usr/bin/env python3
"""parse_caderno_tec.py — lê os cadernos TEC (pdftotext -layout) e gera a fila de candidatos no schema de
candidatos_DA_TEC2025_fila_v2.csv (';', aspas). O TEC é só LOCALIZADOR (D-GCE-01): texto e gabarito entram como
'tec', a confirmar no CDN oficial. Uso: python3 -I parse_caderno_tec.py <pasta_txt> <saida.csv> [--mapa mapa_rotulo_item.json]"""
import re, sys, csv, json, hashlib, os, collections
URL = re.compile(r"www\.tecconcursos\.com\.br/questoes/(\d+)")
HDR = re.compile(r"^CEBRASPE \(CESPE\) - (.+?)\s*$")
GAB = re.compile(r"^Gabarito:\s*(.+?)\s*$")
NUM = re.compile(r"^(\d+)\)\s*(.*)$")
ALT = re.compile(r"^\s{0,8}([a-eA-E])\)\s*(.*)$")
def norm(s): return re.sub(r"\s+", " ", s.replace("-\n", "")).strip()
def parse_file(path, nome_pdf):
    raw = open(path, encoding="utf-8", errors="replace").read()
    # tira cabeçalho/rodapé do caderno
    raw = re.sub(r"^\s*DAD - CEBRASPE - 2024\s*$", "", raw, flags=re.M)
    raw = re.sub(r"^\s*https://www\.tecconcursos\.com\.br/s/\S+\s*$", "", raw, flags=re.M)
    raw = re.sub(r"^\s*Ordenação: Por Matéria e Assunto\s*$", "", raw, flags=re.M)
    raw = raw.replace("\f", "\n")
    parts = URL.split(raw)  # [pre, id, chunk, id, chunk, ...]
    out = []
    for i in range(1, len(parts), 2):
        qid, chunk = parts[i], parts[i + 1]
        lines = [l.rstrip() for l in chunk.split("\n")]
        q = {"id_tec": qid, "arquivo": nome_pdf, "prova_tec": "", "rotulo_tec": "", "formato": "", "gabarito_tec": "", "texto": "", "alternativas": "", "aviso": ""}
        j = 0
        # header
        while j < len(lines) and not HDR.match(lines[j].strip()): j += 1
        if j >= len(lines): q["aviso"] = "sem cabeçalho CEBRASPE"; out.append(q); continue
        q["prova_tec"] = HDR.match(lines[j].strip()).group(1); j += 1
        while j < len(lines) and not lines[j].strip(): j += 1
        rot = []
        while j < len(lines) and lines[j].strip() and not NUM.match(lines[j].strip()):
            rot.append(lines[j].strip()); j += 1
        r = " ".join(rot)
        k = r.find("Direito Administrativo (Doutrina")
        if k > 0: q["prova_tec"] += " " + r[:k].strip(); r = r[k:]   # cabeçalho da prova quebrado em duas linhas
        q["rotulo_tec"] = r.split(" - ", 1)[1] if r.startswith("Direito Administrativo") else r
        # número e corpo
        body, alts, gab = [], [], ""
        while j < len(lines):
            s = lines[j]
            m = GAB.match(s.strip())
            if m: gab = m.group(1); break
            st = s.strip()
            if st in ("Certo", "Errado") and not alts:
                q["formato"] = "Certo/Errado"; j += 1; continue
            ma = ALT.match(s)
            if ma and (alts or q["formato"] != "Certo/Errado"):
                alts.append(f"{ma.group(1).upper()}) {ma.group(2)}"); j += 1; continue
            if alts and st: alts[-1] += " " + st; j += 1; continue
            body.append(s); j += 1
        texto = "\n".join(body)
        mn = NUM.match(texto.strip())
        if mn: q["n_no_caderno"] = int(mn.group(1)); texto = mn.group(2) + texto.strip()[mn.end():] if False else texto.strip()[len(mn.group(1)) + 1:]
        q["texto"] = norm(texto)
        q["alternativas"] = " | ".join(norm(a) for a in alts)
        if alts: q["formato"] = "Múltipla escolha"
        if not q["formato"]: q["formato"] = "Certo/Errado" if gab in ("Certo", "Errado") else ("Múltipla escolha" if re.fullmatch(r"[A-Ea-e]", gab) else "?")
        q["gabarito_tec"] = gab
        if not gab: q["aviso"] = "sem gabarito no caderno"
        if len(q["texto"]) < 40: q["aviso"] = (q["aviso"] + "; " if q["aviso"] else "") + "texto curto"
        out.append(q)
    return out
def main():
    pasta, saida = sys.argv[1], sys.argv[2]; mapa = {}
    if "--mapa" in sys.argv: mapa = json.load(open(sys.argv[sys.argv.index("--mapa") + 1], encoding="utf-8"))
    rows = []
    for f in sorted(os.listdir(pasta)):
        if not f.endswith(".txt"): continue
        nome_pdf = {"c2024_001.txt": "Caderno DAD - CEBRASPE - 2024 - 001.pdf", "c2024_201.txt": "Caderno DAD - CEBRASPE - 2024 - 201.pdf", "c2024_401.txt": "Caderno DAD - CEBRASPE - 2024 - 401.pdf", "c2024_601.txt": "Caderno DAD - CEBRASPE - 2024 - 601.pdf"}.get(f, f)
        rows += parse_file(os.path.join(pasta, f), nome_pdf)
    seen = {}; n = 0
    cols = ["n_caderno", "id_tec", "arquivo", "prova_tec", "rotulo_tec", "formato", "gabarito_tec", "aderencia_wb", "item_edital_wb", "secundarios_wb", "mecanismo_wb", "estrutura_wb", "resposta_analitica_wb", "controversia_wb", "diverge_tec_wb", "oficial_prova", "oficial_data", "oficial_numero", "oficial_gabarito", "validacao_oficial", "status_fabrica", "texto_questao", "alternativas", "hash"]
    with open(saida, "w", encoding="utf-8-sig", newline="") as fo:
        w = csv.writer(fo, delimiter=";", quoting=csv.QUOTE_ALL); w.writerow(cols)
        for q in rows:
            n += 1
            h = hashlib.sha256(q["texto"].lower().encode()).hexdigest()
            dup = seen.get(h); seen.setdefault(h, q["id_tec"])
            it = mapa.get(q["rotulo_tec"], {})
            status = "CANDIDATO — localizar no CDN oficial"
            if q["formato"] == "Múltipla escolha": status = "ME — só insumo de pegadinha (D-MC)"
            if dup: status = f"DUPLICATA de id_tec {dup} (mesmo texto)"
            if q["aviso"]: status += f"; aviso: {q['aviso']}"
            w.writerow([n, q["id_tec"], q["arquivo"], q["prova_tec"], q["rotulo_tec"], q["formato"], q["gabarito_tec"],
                        it.get("aderencia", "Sem enquadramento"), it.get("item", ""), "", "", "", "", "Não", "Não", "", "", "", "", "Não confirmado", status, q["texto"], q["alternativas"], h])
    print(f"{n} candidatos → {saida}")
if __name__ == "__main__": main()
