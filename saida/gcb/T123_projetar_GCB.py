# T123_projetar_GCB.py — T-123 (reconciliação da limpeza de DA) — 2026-10-23 — gerado por gcb-gerencia
# Projeta a tabela aceita (T123_substituicoes_DA_v2.csv) no formato da GBQ, sem mudar texto.
# Uso: python -I saida/gcb/T123_projetar_GCB.py   (a partir da raiz do repositório)
import csv, hashlib, io, json, sys
from collections import Counter

SRC = "saida/gcb/T123_substituicoes_DA_v2.csv"
SRC_SHA = "de63b7c524797723c46690b45082d243583895846fdc144c11da8e2bfe233bde"
BRUTO = "saida/pacote/montagem_v1_14/out/reforco_bruto.json"
OUT_CSV = "saida/gcb/DA_plataforma/DA_reforco_substituicoes.csv"
OUT_REG = "saida/gcb/DA_plataforma/DA_reforco_registro_formato.md"
OPS = {"3": "(3) deleção de marca ou código", "processo": "deleção de frase ou oração de processo",
       "6": "(6) troca mínima pela identificação da publicação"}

def lf(path):
    return open(path, "rb").read().replace(b"\r\n", b"\n")

def sha(b):
    return hashlib.sha256(b).hexdigest()

src = lf(SRC)
if sha(src) != SRC_SHA:
    sys.exit(f"SHA divergente em {SRC}: {sha(src)}")
rows = list(csv.DictReader(io.StringIO(src.decode("utf-8"))))
bruto_b = lf(BRUTO)
itens = {i["id"]: i for i in json.loads(bruto_b.decode("utf-8"))}

def aplicar(regs):
    out = {k: v["justificativa"] for k, v in itens.items()}
    for r in regs:
        j = out[r["id"]]
        if j.count(r["antes"]) != 1:
            sys.exit(f"antes não único: {r}")
        out[r["id"]] = j.replace(r["antes"], r["depois"], 1)
    return out

# 1. CSV da GBQ: id;campo;antes;depois;operacao;motivo (";", UTF-8, LF)
proj = []
for r in rows:
    if r["operacao"] not in OPS:
        sys.exit(f"operação desconhecida: {r['id_edicao']}")
    motivo = f"{r['id_edicao']}; {r['categoria']}; {r['nota']}"
    if r["fonte_origem"]:
        motivo += f"; fonte: {r['fonte_origem']}"
    proj.append({"id": r["item"], "campo": r["campo"], "antes": r["antes"], "depois": r["depois"],
                 "operacao": r["operacao"], "motivo": motivo})
buf = io.StringIO()
w = csv.DictWriter(buf, fieldnames=["id", "campo", "antes", "depois", "operacao", "motivo"],
                   delimiter=";", lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
w.writeheader(); w.writerows(proj)
csv_b = buf.getvalue().encode("utf-8")

# Conferência: relida, a projeção dá o mesmo texto que a tabela aceita
relida = list(csv.DictReader(io.StringIO(csv_b.decode("utf-8")), delimiter=";"))
a = aplicar([{"id": r["item"], "antes": r["antes"], "depois": r["depois"]} for r in rows])
b = aplicar(relida)
assert a == b and len(relida) == len(rows)
for r, p in zip(rows, relida):
    assert (r["item"], r["antes"], r["depois"], r["operacao"]) == (p["id"], p["antes"], p["depois"], p["operacao"])
mudados = sorted(k for k in a if a[k] != itens[k]["justificativa"])

# 2. Registro de formato (uma entrada por substituição)
cont = Counter(r["operacao"] for r in rows)
L = ["# DA_reforco_registro_formato.md — T-123 (pacote v1.14; limpeza das justificativas do reforço de DA) — 2026-10-23 — gerado por gcb-gerencia (projeção por script de T123_substituicoes_DA_v2.csv)", "",
     "## 1. Fontes e conferências",
     f"- Tabela aceita: `{SRC}`, SHA-256 LF `{SRC_SHA}` ({len(rows)} linhas); QA: `saida/gcb/QA_T123_limpeza_R1_2026-10-23_gcb-cqfp.md` (DEVOLVIDO, 2 CORRIGIR) e `QA_T123_limpeza_R2_2026-10-23_gcb-cqfp.md` (CONFERIDO, 91/91).",
     f"- Texto-base: `{BRUTO}`, SHA-256 LF `{sha(bruto_b)}`; campo `justificativa` (j1 + \" \" + j2).",
     "- Operações de `FORMATO_PLATAFORMA_DA.md`, seção 7; tabela de fontes em `saida/gcb/T123_producao_notas_DA.md`.",
     f"- Itens com justificativa alterada: {len(mudados)} de {len(itens)}. Enunciado, gabarito, itemEdital e aderência: não alterados.", "",
     "## 2. Contagem por tipo", ""] + [f"- {OPS[k]}: {cont[k]}" for k in OPS] + ["",
     "## 3. Deleções e trocas (cada uma registrada)", ""]
for r in rows:
    dep = f"`{r['depois']}`" if r["depois"] else "(vazio)"
    fo = f"; fonte: {r['fonte_origem']}" if r["fonte_origem"] else ""
    L.append(f"- [{r['item']} — justificativa] {r['id_edicao']} ({r['acao']}; {OPS[r['operacao']]}; {r['categoria']}) `{r['antes']}` → {dep}. Motivo: {r['nota']}{fo}.")
L += ["", "## 4. Fica sem edição (conteúdo)", "",
      "- VERIFICAR: D4-R24 (\"produção\"), D2-R21 e D2-R24 (\"Presidência da República\"), BQ-0113 (banco, \"produtor\").",
      "- FP: D3-R75, \"desconto em folha\" (enunciado e justificativa)."]
reg_b = ("\n".join(L) + "\n").encode("utf-8")

open(OUT_CSV, "wb").write(csv_b)
open(OUT_REG, "wb").write(reg_b)
print(OUT_CSV, sha(csv_b), len(csv_b), len(proj))
print(OUT_REG, sha(reg_b), len(reg_b))
print("itens alterados", len(mudados), "operacoes", dict(cont))
