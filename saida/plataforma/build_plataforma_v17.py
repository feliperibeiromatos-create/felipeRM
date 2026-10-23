#!/usr/bin/env python3
# build_plataforma_v17.py — T-125, D-V17-DESIGN — 2026-10-23 — gerado por produção-plataforma (sonnet)
"""Monta a plataforma v17: troca `const PUB_INLINE = __PACOTE__;` pelo pacote.json embutido e `__VERSAO__` pela meta mapaspro:versao.

Uso: python3 -I build_plataforma_v17.py [--template T] [--pacote P] [--saida S] [--data dd/mm/aaaa] [--rotulo-pacote TEXTO]
Padrões: template saida/plataforma/plataforma_v17_template.html; pacote saida/pacote/pacote.json; saída saida/plataforma/plataforma_v17.html;
         data = hoje; rótulo = "pacote <nome> embutido (<N> itens; <M> de Direito Administrativo)" montado a partir do pacote.
Meta resultante: "v17 · publicada em <data> · três abas · <rótulo>". O pacote é gravado em JSON compacto (UTF-8), com a sequência de fechamento de script escapada (barra invertida antes da barra).
"""
import argparse, datetime, json, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ap = argparse.ArgumentParser()
ap.add_argument("--template", default=os.path.join(RAIZ, "saida/plataforma/plataforma_v17_template.html"))
ap.add_argument("--pacote", default=os.path.join(RAIZ, "saida/pacote/pacote.json"))
ap.add_argument("--saida", default=os.path.join(RAIZ, "saida/plataforma/plataforma_v17.html"))
ap.add_argument("--data", default=datetime.date.today().strftime("%d/%m/%Y"))
ap.add_argument("--rotulo-pacote", default=None)
a = ap.parse_args()

MARCA, VMARCA = "const PUB_INLINE = __PACOTE__;", "__VERSAO__"
html = open(a.template, encoding="utf-8").read()
for m in (MARCA, VMARCA):
    if html.count(m) != 1:
        sys.exit(f"ERRO: o template deve ter exatamente uma ocorrência de '{m}' (tem {html.count(m)}).")
p = json.load(open(a.pacote, encoding="utf-8"))
for k in ("itens", "simulados"):
    if not isinstance(p.get(k), list):
        sys.exit(f"ERRO: pacote sem a lista '{k}'.")
try:
    datetime.datetime.strptime(a.data, "%d/%m/%Y")
except ValueError:
    sys.exit("ERRO: --data deve ser dd/mm/aaaa.")
nda = sum(1 for i in p["itens"] if str(i.get("itemEdital", "")).startswith("P1-DA-"))
rot = a.rotulo_pacote or f"pacote {p.get('nome', '?')} embutido ({len(p['itens'])} itens; {nda} de Direito Administrativo)"
versao = f"v17 · publicada em {a.data} · três abas · {rot}".replace('"', "'")
js = json.dumps(p, ensure_ascii=False, separators=(",", ":")).replace("</", "<" + chr(92) + "/")
html = html.replace(MARCA, "const PUB_INLINE = " + js + ";").replace(VMARCA, versao)
open(a.saida, "w", encoding="utf-8").write(html)
print(f"OK: {a.saida} · {len(html.encode('utf-8'))} bytes · meta '{versao}' · {len(p['itens'])} itens · {len(p.get('lotes', []))} lotes · {len(p.get('topicos', {}) or {})} tópicos com resumo")
