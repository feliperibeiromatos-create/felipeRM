#!/usr/bin/env python3
"""checa_resumo_visual.py — seção 3c da ESPEC_resumo_visual_DA_v3 (v1.1, após QA R1 D19): confere `topicos[id].resumoVisual`
de um pacote (ou de um JSON {id: resumoVisual}).
Uso: python3 -I checa_resumo_visual.py <pacote.json | resumo_visual.json> [--pacote pacote.json]
  --pacote: cruza cada dispositivo dos blocos `lei` com o `baseLegal` do mesmo tópico no pacote (ESPEC §5.7).
Bloqueios: tipo de bloco desconhecido; ícone fora de ICONES; limites da seção 3 (mapa 3–8 ramos, título ≤ 60 e texto ≤ 180;
dois 2–7 por lado; escala 3–6; linhaTempo 3–7; relâmpago 6–10 frases de ≤ 140; pegadinhas 4–10; pirâmide 3–5); cobranca ausente
ou sem fonte; termo de probabilidade ou rótulo vedado pela triagem; emoji; referência a página/slide de PDF; bloco lei sem
`conferido` em data ISO válida ou com dispositivo ausente, texto ou `literal` diferentes do baseLegal (com --pacote); imagem > 150 KB ou mais de 2 por tópico.
Avisos: texto > 4 frases; tabela > 4 colunas; sem relâmpago/pegadinhas; primeiro bloco não é seção.
Para integrar ao checa_pacote_v2.py da fábrica: `from checa_resumo_visual import checa_pacote`."""
import json, re, sys, base64
TIPOS = {"secao", "sub", "texto", "lista", "tabela", "compare", "fluxo", "esquema", "linha", "barras", "lei", "box", "piramide", "mapa", "dois", "escala", "linhaTempo", "relampago", "pegadinhas", "imagem"}
ICONES = {"alvo", "pino", "balanca", "predio", "pessoas", "doc", "relogio", "cadeado", "aviso", "confere", "x", "raio", "chave", "livro", "seta", "engrenagem"}
PROB = re.compile(r"ALT[IÍ]SSIMA|ALTA PROBABILIDADE|M[EÉ]DIA PROBABILIDADE|BAIXA PROBABILIDADE|probabilidade de cobran|pegadinha prov[áa]vel|cada vez mais cobrad|muito cobrad[oa]\b|cai (muito|sempre|direto)", re.I)
VEDADOS = [re.compile(p, re.I) for p in (r"COFIFOMOB", r"qu[áa]druplo", r"contrato de desempenho", r"Funda[çc][ãa]o Banco do Brasil", r"\bOAB\b.{0,60}autarquia", r"autarquia.{0,60}\bOAB\b", r"\b(Vale|Embrapa|Embraer|Eletrobras)\b.{0,40}economia mista", r"(economia mista|\bSEM\b).{0,60}\b(Vale|Embrapa|Embraer|Eletrobras)\b", r"cai em toda prova|tema quente|certeza de cobran", r"incompet[êe]ncia.{0,30}insan[áa]vel", r"desvio de finalidade.{0,30}(é|e) san[áa]vel", r"a partir da EC ?19")]
EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2300-\u23FF\u2600-\u27BF\u2B00-\u2BFF\uFE0F]")
PDF = re.compile(r"\bpp?\.\s?\d+\b|\bp[áa]g(ina|\.)\s?\d+|\bslide\s?\d+|p[áa]gina \d+ do (resumo|PDF)", re.I)
ISO = re.compile(r"^\d{4}-\d{2}-\d{2}$")
def frases(s): return len([x for x in re.split(r"[.!?](\s|$)", s) if x and x.strip()])
def walk(o):
    if isinstance(o, dict):
        for v in o.values(): yield from walk(v)
    elif isinstance(o, list):
        for v in o: yield from walk(v)
    elif isinstance(o, str): yield o
def norm(s): return re.sub(r"\s+", " ", (s or "")).strip()
def refs_base_legal(topico):
    """{ref: (texto normalizado, literal)} dos dispositivos do baseLegal do tópico no pacote"""
    refs = {}
    for v in (topico or {}).get("visuais", []):
        if v.get("tipo") == "baseLegal":
            for d in v.get("dispositivos", []): refs[d.get("ref")] = (norm(d.get("texto")), bool(d.get("literal")))
    return refs
def data_iso_valida(s):
    import datetime
    try: datetime.date.fromisoformat(s); return True
    except Exception: return False
def checa(tid, rv, topico=None):
    B, A = [], []
    def b(m): B.append(f"{tid}: {m}")
    def a(m): A.append(f"{tid}: {m}")
    if rv.get("versao") != "v3": b("versao deve ser 'v3'")
    c = rv.get("cobranca")
    if not isinstance(c, dict) or not c.get("fonte") or not isinstance(c.get("itens"), int) or not isinstance(c.get("ce"), int): b("cobranca obrigatória: itens (int), ce (int) e fonte")
    for s in walk(rv):
        if PROB.search(s): b(f"termo de probabilidade: '{s[:70]}'")
        for p in VEDADOS:
            if p.search(s): b(f"termo vedado pela triagem ({p.pattern}): '{s[:70]}'")
        if EMOJI.search(s): b(f"emoji: '{s[:70]}'")
        if PDF.search(s): b(f"referência a página/slide de PDF: '{s[:70]}'")
    nimg = 0; tipos = []; base = refs_base_legal(topico) if topico is not None else None
    for i, bl in enumerate(rv.get("blocos", [])):
        t = bl.get("t"); tipos.append(t)
        if t not in TIPOS: b(f"bloco {i}: tipo desconhecido '{t}'"); continue
        if "icone" in bl and bl["icone"] not in ICONES: b(f"bloco {i}: ícone desconhecido '{bl['icone']}'")
        if t in ("secao", "sub") and not bl.get("titulo"): b(f"bloco {i}: {t} sem título")
        if t == "texto":
            if not bl.get("md"): b(f"bloco {i}: texto vazio")
            elif frases(bl["md"]) > 4: a(f"bloco {i}: texto com mais de 4 frases")
        if t in ("tabela", "compare"):
            cols = bl.get("colunas") or (["Aspecto", bl.get("a"), bl.get("b")] if t == "compare" else [])
            if len(cols) > 4: a(f"bloco {i}: tabela com {len(cols)} colunas")
            if not bl.get("linhas"): b(f"bloco {i}: tabela sem linhas")
            for r in bl.get("linhas", []):
                if len(r) != len(cols): b(f"bloco {i}: linha com {len(r)} células para {len(cols)} colunas")
        if t == "box" and bl.get("tipo") not in ("atencao", "regra", "exemplo"): b(f"bloco {i}: box.tipo inválido")
        if t == "lei":
            for d in bl.get("dispositivos", []):
                cf = d.get("conferido")
                if not (isinstance(cf, str) and ISO.match(cf) and data_iso_valida(cf)): b(f"bloco {i}: dispositivo '{d.get('ref')}' sem conferido em data ISO válida")
                if base is not None:
                    if d.get("ref") not in base: b(f"bloco {i}: dispositivo '{d.get('ref')}' não está no baseLegal do pacote")
                    else:
                        tx, lit = base[d.get("ref")]
                        if norm(d.get("texto")) != tx and norm(d.get("texto")) != norm(re.sub(r"\s*\(prazo 3 anos - vide EMC nº 19\)", "", tx)): b(f"bloco {i}: texto de '{d.get('ref')}' difere do baseLegal do pacote")
                        if bool(d.get("literal")) != lit: b(f"bloco {i}: 'literal' de '{d.get('ref')}' difere do baseLegal do pacote")
        if t == "piramide" and not (3 <= len(bl.get("niveis", [])) <= 5): b(f"bloco {i}: piramide com {len(bl.get('niveis', []))} níveis (3–5)")
        if t == "mapa":
            rs = bl.get("ramos", [])
            if not (3 <= len(rs) <= 8): b(f"bloco {i}: mapa com {len(rs)} ramos (3–8)")
            for r in rs:
                if len(r.get("titulo", "")) > 60: b(f"bloco {i}: título de ramo com {len(r['titulo'])} chars (>60)")
                if len(r.get("texto", "")) > 180: b(f"bloco {i}: texto de ramo com {len(r['texto'])} chars (>180)")
        if t == "dois":
            for k in ("a", "b"):
                n = len(bl.get(k, {}).get("itens", []))
                if not (2 <= n <= 7): b(f"bloco {i}: dois.{k} com {n} itens (2–7)")
        if t == "escala" and not (3 <= len(bl.get("pontos", [])) <= 6): b(f"bloco {i}: escala com {len(bl.get('pontos', []))} pontos (3–6)")
        if t == "linhaTempo" and not (3 <= len(bl.get("marcos", [])) <= 7): b(f"bloco {i}: linhaTempo com {len(bl.get('marcos', []))} marcos (3–7)")
        if t == "relampago":
            it = bl.get("itens", [])
            if not (6 <= len(it) <= 10): b(f"bloco {i}: relampago com {len(it)} frases (6–10)")
            for x in it:
                if len(x) > 140: b(f"bloco {i}: frase do relâmpago com {len(x)} chars (>140): '{x[:50]}'")
        if t == "pegadinhas":
            it = bl.get("itens", [])
            if not (4 <= len(it) <= 10): b(f"bloco {i}: pegadinhas com {len(it)} pares (4–10)")
            for p in it:
                if not p.get("errado") or not p.get("certo"): b(f"bloco {i}: par sem errado/certo")
        if t == "imagem":
            nimg += 1; src = bl.get("src", "")
            if not bl.get("alt"): b(f"bloco {i}: imagem sem alt")
            if src.startswith("data:"):
                raw = src.split(",", 1)[1] if "," in src else ""
                if len(base64.b64decode(raw + "==")) > 150 * 1024: b(f"bloco {i}: imagem > 150 KB")
    if nimg > 2: b(f"{nimg} imagens (máx. 2)")
    if "relampago" not in tipos: a("sem bloco relampago")
    if "pegadinhas" not in tipos: a("sem bloco pegadinhas")
    if tipos and tipos[0] != "secao": a("o primeiro bloco não é uma seção")
    return B, A
def checa_pacote(d, pacote=None):
    """d: pacote completo ou {id: resumoVisual}; pacote: pacote completo para cruzar baseLegal. Retorna (bloqueios, avisos, n)."""
    rvs = {k: v["resumoVisual"] for k, v in d.get("topicos", {}).items() if isinstance(v, dict) and v.get("resumoVisual")} if "topicos" in d else d
    tops = (pacote or d).get("topicos", {}) if ("topicos" in (pacote or d)) else {}
    B, A = [], []
    for k, v in rvs.items():
        b, a = checa(k, v, tops.get(k) if tops else None); B += b; A += a
    return B, A, len(rvs)
def main():
    args = sys.argv[1:]; pac = None
    if "--pacote" in args:
        i = args.index("--pacote"); pac = json.load(open(args[i + 1], encoding="utf-8")); del args[i:i + 2]
    d = json.load(open(args[0], encoding="utf-8"))
    B, A, n = checa_pacote(d, pac)
    print(f"resumoVisual em {n} tópicos · BLOQUEIOS {len(B)} · AVISOS {len(A)}" + (" · baseLegal cruzado com o pacote" if pac or "topicos" in d else ""))
    for x in B: print("BLOQUEIO", x)
    for x in A: print("aviso", x)
    sys.exit(1 if B else 0)
if __name__ == "__main__": main()
