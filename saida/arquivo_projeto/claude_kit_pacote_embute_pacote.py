#!/usr/bin/env python3
"""Gera uma cópia do index.html da plataforma com outro pacote embutido (linha `const PUB_INLINE = ...;`).
Não toca no original. A cópia serve para a regressão e, depois do "sim" do Fundador, como base da publicação.

Uso: python3 -I embute_pacote.py <index.html em uso> <pacote_novo.json> <saida.html> [--versao "v15.3 · ..."]
"""
import json, sys, argparse
ap = argparse.ArgumentParser(); ap.add_argument("html"); ap.add_argument("pacote"); ap.add_argument("saida"); ap.add_argument("--versao"); ap.add_argument("--demo", action="store_true", help="mantém a demonstração de formato de DA (só para a prévia)")
a = ap.parse_args()
h = open(a.html, encoding="utf-8").read()
p = json.load(open(a.pacote, encoding="utf-8"))
js = json.dumps(p, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
linhas = h.split("\n")
k = [i for i, l in enumerate(linhas) if l.startswith("const PUB_INLINE")]
if len(k) != 1: raise SystemExit(f"esperava 1 linha const PUB_INLINE, achei {len(k)}")
linhas[k[0]] = "const PUB_INLINE = " + js + ";"
out = "\n".join(linhas)
if not a.demo:
    out = out.replace("const DEMO_DA=true;", "const DEMO_DA=false;")
if a.versao:
    import re
    out, n = re.subn(r'(<meta name="mapaspro:versao" content=")[^"]*(")', lambda m: m.group(1) + a.versao.replace('"', "'") + m.group(2), out, count=1)
    if n != 1: raise SystemExit("meta mapaspro:versao não encontrada")
open(a.saida, "w", encoding="utf-8").write(out)
print(f"ok: {a.saida} · {len(p['itens'])} itens · linhas de código fora do pacote inalteradas")
