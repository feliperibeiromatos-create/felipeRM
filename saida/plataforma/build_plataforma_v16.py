#!/usr/bin/env python3
# build_plataforma_v16.py — ordem do Fundador 20/10/2026 — 2026-10-20 — gerado por desenvolvedor-plataforma
"""Monta a plataforma v16: troca a linha `const PUB_INLINE = __PACOTE__;` do template pelo pacote.json embutido.

Uso: python3 -I build_plataforma_v16.py [template] [pacote.json] [saída]
Padrões: saida/plataforma/plataforma_v16_template.html, saida/pacote/pacote.json, saida/plataforma/plataforma_v16.html
O pacote é gravado em JSON compacto (UTF-8), com "</" escapado como "<\\/" para não fechar o <script>.
"""
import json, sys, os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
tpl = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, "saida/plataforma/plataforma_v16_template.html")
pac = sys.argv[2] if len(sys.argv) > 2 else os.path.join(RAIZ, "saida/pacote/pacote.json")
out = sys.argv[3] if len(sys.argv) > 3 else os.path.join(RAIZ, "saida/plataforma/plataforma_v16.html")

MARCA = "const PUB_INLINE = __PACOTE__;"
html = open(tpl, encoding="utf-8").read()
if html.count(MARCA) != 1:
    sys.exit(f"ERRO: o template deve ter exatamente uma linha '{MARCA}' (tem {html.count(MARCA)}).")
p = json.load(open(pac, encoding="utf-8"))
for k in ("itens", "simulados"):
    if not isinstance(p.get(k), list):
        sys.exit(f"ERRO: pacote sem a lista '{k}'.")
js = json.dumps(p, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
html = html.replace(MARCA, "const PUB_INLINE = " + js + ";")
open(out, "w", encoding="utf-8").write(html)
print(f"OK: {out} · {len(html.encode('utf-8'))} bytes · pacote '{p.get('nome')}' ({p.get('geradoEm')}) · "
      f"{len(p['itens'])} itens · {len(p.get('lotes', []))} lotes · {len(p.get('topicos', {}) or {})} tópicos com resumo")
