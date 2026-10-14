# ne_v1_7.py — T-70 (D-T70-04; D-V17-AGORA) — 2026-10-14 — gerado por QA-plataforma (opus)
"""Suíte oficial do campo NE da plataforma v1.7 (D1 saida/pacote/T70_T71_decisoes_2026-10-14.md, seção 4).

Mandato (D-V17-AGORA): "1,5", ou qualquer vírgula ou ponto decimal digitado, nunca vira 15 em silêncio;
é recusado com o mesmo aviso de valor inválido, no celular e no computador.

Uso (python3 -I, Playwright já instalado):
  PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers python3 -I saida/plataforma/testes/ne_v1_7.py \
      --pagina saida/plataforma/plataforma_v1_7.html --pacote saida/pacote/pacote.json \
      --esperado v17 --saida saida/plataforma/testes/ne_v1_7_v17_2026-10-14.json
  (controle negativo: --pagina saida/plataforma/plataforma_v1_6.html --esperado v16 --saida ..._v16_controle_...json)

O script copia a página (como index.html) e o pacote para uma pasta temporária própria, serve-os por
http.server em 127.0.0.1 numa porta livre, numa thread, e não grava nada além de --saida.
Dados: só estados sintéticos montados aqui (nenhum dado da candidata). Não usa window.claude.
Oráculo independente do código da página: str.strip + re.fullmatch('[0-9]+') + <= 2^53 - 1; vazio -> 0.

Código de saída: --esperado v17 -> 0 se e só se falhas = 0 (controle=n/a);
                 --esperado v16 -> 0 se e só se o controle (D1 4.5) reproduz st.ne = 15 sem aviso nos 6 casos de CONTROLE.
Limites (D1 4.6): sem teclado físico nem teclado virtual real; "iPhone" e "Android" são emulados no
Chromium (viewport, agente, toque, eventos de entrada); sem WebKit real, sem IME.
"""
import argparse, functools, hashlib, http.server, importlib.metadata, json, math, os, re, shutil, socketserver, sys, tempfile, threading, time

from playwright.sync_api import sync_playwright

K_S = "c2026.v01.estado"
MAXS = 2 ** 53 - 1
AVISO = "Digite um número inteiro (0, 1, 2…). Valor não aceito; a nota segue com NE {}."
R = ["1,5", "1.5", "1,", "1.", ",5", ".5", "0,5", "1,0", "1.0", "-1", "+1", "1e1", "1 5", "e"]
A = ["0", "3", "15", "007"]
TEXTO12 = "\n".join("Linha %d da resposta sintética de teste da QA." % (i + 1) for i in range(12))
FRACOES = [1, 0.75, 0.5, 0.25, 0]
VAZIO = {"v": 1, "boasVindas": True, "escolha": {"P1": "diag", "P2": "zero"}, "tentativas": [], "erros": {},
         "saidas": [], "lote": {}, "disc": {}, "vespera": {}, "eventos": []}
CONTROLE = [("C1", "tecla", "vazio", "1,5"), ("M1", "tecla", "vazio", "1,5"), ("M2", "tecla", "vazio", "1,5"),
            ("M1", "insert", "vazio", "1,5"), ("M2", "insert", "vazio", "1,5"), ("C4", "colar", "vazio", "1,5")]


# ---------- oráculo (D1 2.2 / 2.3), sem ler a página ----------
def aceita(v):
    s = v.strip()
    if s == "":
        return 0
    if re.fullmatch("[0-9]+", s) and int(s) <= MAXS:
        return int(s)
    return None


def oraculo(modo, ne0, entrada):
    """Devolve (lista de st.ne esperado por passo, st.ne final, recusada_final)."""
    passos = []
    ne = ne0
    if modo == "tecla":
        for i in range(1, len(entrada) + 1):
            a = aceita(entrada[:i])
            if a is not None:
                ne = a
            passos.append(ne)
    else:
        a = aceita(entrada)
        if a is not None:
            ne = a
        passos.append(ne)
    return passos, ne, aceita(entrada) is None


def fmt_br(x):
    v = math.floor(x * 100 + 0.5) / 100
    s = "%.2f" % v
    inteiro, dec = s.split(".")
    neg = inteiro.startswith("-")
    inteiro = inteiro.lstrip("-")
    grupos = []
    while len(inteiro) > 3:
        grupos.insert(0, inteiro[-3:])
        inteiro = inteiro[:-3]
    grupos.insert(0, inteiro)
    return ("-" if neg else "") + ".".join(grupos) + "," + dec


# ---------- servidor ----------
class _Silencioso(http.server.SimpleHTTPRequestHandler):
    status_log = []

    def log_message(self, fmt, *args):
        pass

    def log_request(self, code="-", size="-"):
        _Silencioso.status_log.append((self.path, int(code) if str(code).isdigit() else code))


def servir(pasta):
    h = functools.partial(_Silencioso, directory=pasta)
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", 0), h)
    srv.daemon_threads = True
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    return srv, "http://127.0.0.1:%d" % srv.server_address[1]


# ---------- suíte ----------
class Suite:
    def __init__(self, base, pacote, esperado, browser, devices):
        self.base, self.P, self.esperado, self.b, self.devices = base, pacote, esperado, browser, devices
        self.casos, self.nverif, self.nfalhas = [], 0, 0
        self.D = {d["id"]: d for d in pacote["discursivas"]}

    # contexto novo por caso (isolamento total; D1 4.1 pede ao menos um por cenário)
    def contexto(self, cen):
        tz = {"timezone_id": "America/Sao_Paulo"}
        if cen in ("M1", "M2", "XM1", "XM2"):
            nome = "Galaxy S8" if cen.endswith("M1") else "iPhone 13"
            d = dict(self.devices[nome])
            d.pop("default_browser_type", None)
            opts = dict(d, locale="pt-BR", **tz)
            disp = nome
        else:
            opts = dict(viewport={"width": 1280, "height": 800}, locale="en-US" if cen == "C2" else "pt-BR", **tz)
            disp = "computador 1280x800"
        ctx = self.b.new_context(**opts)
        ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=self.base)
        return ctx, opts, disp

    def abrir_avaliacao(self, ctx, estado, did, entregar=True):
        ctx.add_init_script(
            "(e => { if (!sessionStorage.getItem('qaInit')) { localStorage.clear(); localStorage.setItem('%s', e); sessionStorage.setItem('qaInit','1'); } })(%s)"
            % (K_S, json.dumps(json.dumps(estado))))
        p = ctx.new_page()
        erros = []
        p.on("pageerror", lambda e: erros.append("pageerror: " + str(e)))
        p.on("console", lambda m: erros.append("console.error: " + m.text) if m.type == "error" else None)
        p.goto(self.base + "/index.html")
        p.wait_for_function("() => document.querySelector('#app') && document.querySelector('#app').children.length > 0")
        p.evaluate("id => ir('disc', id)", did)
        if entregar:
            p.fill("#tx", TEXTO12)
            p.click("#entrega")
        p.wait_for_selector("#ne")
        nc = 0.0
        if entregar:
            for i, a in enumerate(self.D[did]["aspectos"]):
                f = FRACOES[i % len(FRACOES)]
                nc += a["valor"] * f
                p.select_option("#asp%d" % a["n"], str(f))
        return p, erros, nc

    @staticmethod
    def ler(p, did):
        return p.evaluate("""id => { const i = document.getElementById('ne'), a = document.getElementById('neAviso');
          const raw = localStorage.getItem('%s'); const s = JSON.parse(raw).disc[id];
          return { campo: i.value, st_ne: s.ne, nota: s.nota, tl: s.tl, aviso_visivel: !a.hidden, aviso: a.textContent,
                   aria: i.getAttribute('aria-invalid'), nq: document.getElementById('nq').textContent, ls: raw,
                   foco: document.activeElement && document.activeElement.id }; }""" % K_S, did)

    def chk(self, caso, nome, ok, info=None):
        self.nverif += 1
        caso["verificacoes"].append({"nome": nome, "ok": bool(ok), "info": info})
        if not ok:
            caso["ok"] = False
            self.nfalhas += 1

    def focar(self, p, movel):
        if movel:
            p.tap("#ne")
        else:
            p.click("#ne")

    def caso(self, cen, did, modo, partida, entrada):
        movel = cen in ("M1", "M2")
        ctx, opts, disp = self.contexto(cen)
        try:
            p, erros, nc = self.abrir_avaliacao(ctx, VAZIO, did)
            d = self.D[did]
            k = 6 if d.get("tipo") == "peca" else 3
            # partida
            if partida == "vazio":
                p.fill("#ne", "")
                ne0 = 0
                self.focar(p, movel)
            else:  # NE2: fill("2"), foco/toque, select()
                p.fill("#ne", "2")
                ne0 = 2
                self.focar(p, movel)
                p.evaluate("() => document.getElementById('ne').select()")
            ini = self.ler(p, did)
            esp_passos, esp_final, recusada = oraculo(modo, ne0, entrada)
            caso = {"cenario": cen, "locale": opts.get("locale"), "dispositivo": disp,
                    "viewport": opts.get("viewport"), "D": did, "modo": modo, "partida": partida, "entrada": entrada,
                    "passos": [], "final": None, "esperado": {"passos_st_ne": esp_passos, "st_ne": esp_final,
                                                              "aviso_visivel": recusada}, "ok": True, "verificacoes": []}
            self.chk(caso, "partida: st.ne inicial = %d" % ne0, ini["st_ne"] == ne0, ini["st_ne"])
            # snapshots do último passo aceito
            ult_ls, ult_nq = ini["ls"], ini["nq"]
            if modo == "tecla":
                for i, ch in enumerate(entrada):
                    p.keyboard.press(ch)
                    u = self.ler(p, did)
                    pref = entrada[:i + 1]
                    caso["passos"].append({"tecla": ch, "campo": u["campo"], "st_ne": u["st_ne"], "aviso_visivel": u["aviso_visivel"]})
                    self.chk(caso, "passo %d (%r): st.ne = %r" % (i + 1, pref, esp_passos[i]), u["st_ne"] == esp_passos[i], u["st_ne"])
                    self.chk(caso, "passo %d: campo mostra %r" % (i + 1, pref), u["campo"] == pref, u["campo"])
                    if aceita(pref) is not None:
                        ult_ls, ult_nq = u["ls"], u["nq"]
            else:
                if modo == "insert":
                    p.keyboard.insert_text(entrada)
                elif modo == "colar":
                    p.evaluate("t => navigator.clipboard.writeText(t)", entrada)
                    p.keyboard.press("ControlOrMeta+V")
                elif modo == "fill":
                    p.fill("#ne", entrada)
                u = self.ler(p, did)
                caso["passos"].append({"tecla": "<%s %r>" % (modo, entrada), "campo": u["campo"], "st_ne": u["st_ne"], "aviso_visivel": u["aviso_visivel"]})
                self.chk(caso, "%s: st.ne = %r" % (modo, esp_final), u["st_ne"] == esp_final, u["st_ne"])
                self.chk(caso, "%s: campo mostra %r" % (modo, entrada), u["campo"] == entrada, u["campo"])
                if not recusada:
                    ult_ls, ult_nq = u["ls"], u["nq"]
            u = self.ler(p, did)
            caso["final"] = {k2: u[k2] for k2 in ("campo", "st_ne", "nota", "tl", "aviso_visivel", "aviso", "aria", "nq")}
            self.chk(caso, "final: st.ne = %r" % esp_final, u["st_ne"] == esp_final, u["st_ne"])
            if recusada:
                self.chk(caso, "final: aviso visível com texto exato (NE %s)" % esp_final,
                         u["aviso_visivel"] and u["aviso"] == AVISO.format(esp_final), u["aviso"])
                self.chk(caso, "final: aria-invalid = true", u["aria"] == "true", u["aria"])
                self.chk(caso, "final: localStorage byte a byte = último aceito", u["ls"] == ult_ls)
                self.chk(caso, "final: #nq = último aceito", u["nq"] == ult_nq, [u["nq"], ult_nq])
            else:
                self.chk(caso, "final: aviso oculto, texto vazio", (not u["aviso_visivel"]) and u["aviso"] == "", u["aviso"])
                self.chk(caso, "final: aria-invalid ausente", u["aria"] is None, u["aria"])
            tl = u["tl"]
            self.chk(caso, "TL = 12", tl == 12, tl)
            esp_nota = max(0.0, nc - k * u["st_ne"] / tl) if isinstance(u["st_ne"], (int, float)) and tl else None
            self.chk(caso, "st.nota = max(0, NC − %d × st.ne ÷ TL) (tol 1e-9)" % k,
                     esp_nota is not None and isinstance(u["nota"], (int, float)) and abs(u["nota"] - esp_nota) < 1e-9,
                     {"nota": u["nota"], "esperada": esp_nota, "nc": nc})
            self.chk(caso, "#nq = fmt(st.nota)", esp_nota is not None and u["nq"] == fmt_br(esp_nota), [u["nq"], esp_nota])
            # change: Tab no computador; blur() nos móveis
            ls_antes = u["ls"]
            if movel:
                p.evaluate("() => document.getElementById('ne').blur()")
            else:
                p.keyboard.press("Tab")
            u2 = self.ler(p, did)
            caso["depois_change"] = {k2: u2[k2] for k2 in ("campo", "st_ne", "aviso_visivel", "aria", "foco")}
            self.chk(caso, "change: foco saiu do campo", u2["foco"] != "ne", u2["foco"])
            self.chk(caso, "change: localStorage não muda", u2["ls"] == ls_antes)
            if recusada:
                self.chk(caso, "change: campo mostra String(st.ne) = %r" % str(esp_final), u2["campo"] == str(esp_final), u2["campo"])
                self.chk(caso, "change: aria-invalid sai", u2["aria"] is None, u2["aria"])
                self.chk(caso, "change: aviso continua visível (texto exato)", u2["aviso_visivel"] and u2["aviso"] == AVISO.format(esp_final), u2["aviso"])
            else:
                self.chk(caso, "change: campo mantém o texto aceito", u2["campo"] == entrada, u2["campo"])
                self.chk(caso, "change: aviso oculto", not u2["aviso_visivel"], u2["aviso_visivel"])
            self.chk(caso, "0 pageerror e 0 console.error", not erros, erros)
            self.casos.append(caso)
            return caso
        finally:
            ctx.close()

    def caso_atributos(self, cen):
        """C1 (antes das telas) e X: atributos; em X também layout com o aviso visível depois de '1,5'."""
        movel = cen.startswith("X")
        ctx, opts, disp = self.contexto(cen)
        try:
            p, erros, nc = self.abrir_avaliacao(ctx, VAZIO, "D1")
            caso = {"cenario": cen, "locale": opts.get("locale"), "dispositivo": disp, "viewport": opts.get("viewport"),
                    "D": "D1", "modo": "atributos" + ("+layout" if movel else ""), "partida": "vazio", "entrada": "1,5" if movel else None,
                    "passos": [], "final": None, "esperado": None, "ok": True, "verificacoes": []}
            at = p.evaluate("""() => { const i = document.getElementById('ne');
              return { type: i.getAttribute('type'), prop_type: i.type, inputmode: i.getAttribute('inputmode'), autocomplete: i.getAttribute('autocomplete'),
                       desc: i.getAttribute('aria-describedby'), min: i.getAttribute('min'), max: i.getAttribute('max'), step: i.getAttribute('step') }; }""")
            caso["final"] = {"atributos": at}
            self.chk(caso, "type = text", at["type"] == "text" and at["prop_type"] == "text", at)
            self.chk(caso, "inputmode = numeric", at["inputmode"] == "numeric", at)
            if movel:
                self.chk(caso, "autocomplete = off", at["autocomplete"] == "off", at)
                self.chk(caso, "aria-describedby = neAviso", at["desc"] == "neAviso", at)
                self.chk(caso, "min, max e step ausentes", at["min"] is None and at["max"] is None and at["step"] is None, at)
                p.fill("#ne", "")
                p.tap("#ne")
                for ch in "1,5":
                    p.keyboard.press(ch)
                u = self.ler(p, "D1")
                self.chk(caso, "aviso visível depois de '1,5' (NE 1)", u["aviso_visivel"] and u["aviso"] == AVISO.format(1), u["aviso"])
                lay = p.evaluate("""() => { const r = document.getElementById('neAviso').getBoundingClientRect(), de = document.documentElement;
                   return { sw: de.scrollWidth, cw: de.clientWidth, bsw: document.body.scrollWidth, bcw: document.body.clientWidth,
                            h: r.height, l: r.left, r: r.right, iw: innerWidth }; }""")
                caso["final"]["layout"] = lay
                self.chk(caso, "%d px: documento sem rolagem horizontal (scrollWidth <= clientWidth)" % lay["iw"], lay["sw"] <= lay["cw"], lay)
                self.chk(caso, "%d px: body sem rolagem horizontal" % lay["iw"], lay["bsw"] <= lay["cw"], lay)
                self.chk(caso, "aviso com altura > 0 e dentro da largura", lay["h"] > 0 and lay["l"] >= 0 and lay["r"] <= lay["cw"], lay)
            self.chk(caso, "0 pageerror e 0 console.error", not erros, erros)
            self.casos.append(caso)
        finally:
            ctx.close()

    def caso_legado(self):
        """L: estado sintético com disc.D1.ne = 1.5, entregue, tl 2 (D1 2.2 e 4.3); exportação leva "ne": 1.5 (6.1, 4)."""
        ctx, opts, disp = self.contexto("L")
        try:
            est = json.loads(json.dumps(VAZIO))
            est["disc"]["D1"] = {"texto": TEXTO12, "entregue": True, "notas": {}, "ne": 1.5, "tl": 2}
            ctx.add_init_script("window.__cap = null; Object.defineProperty(navigator, 'clipboard', { configurable: true, value: { writeText: async t => { window.__cap = t; } } });")
            p, erros, _ = self.abrir_avaliacao(ctx, est, "D1", entregar=False)
            caso = {"cenario": "L", "locale": opts.get("locale"), "dispositivo": disp, "viewport": opts.get("viewport"),
                    "D": "D1", "modo": "legado+tecla", "partida": "legado ne 1.5", "entrada": ",", "passos": [], "final": None,
                    "esperado": {"abrir": {"campo": "1.5", "aviso_visivel": False, "st_ne": 1.5}, "depois_virgula": {"st_ne": 1.5, "aviso": AVISO.format(1.5)}, "depois_change": {"campo": "1.5"}},
                    "ok": True, "verificacoes": []}
            u = self.ler(p, "D1")
            caso["passos"].append({"tecla": "<abrir>", "campo": u["campo"], "st_ne": u["st_ne"], "aviso_visivel": u["aviso_visivel"]})
            self.chk(caso, "abrir: campo '1.5'", u["campo"] == "1.5", u["campo"])
            self.chk(caso, "abrir: aviso oculto, sem aria-invalid", not u["aviso_visivel"] and u["aria"] is None, u)
            self.chk(caso, "abrir: st.ne 1.5", u["st_ne"] == 1.5, u["st_ne"])
            ls0 = u["ls"]
            p.click("#ne")
            p.evaluate("() => document.getElementById('ne').select()")
            p.keyboard.press(",")
            u = self.ler(p, "D1")
            caso["passos"].append({"tecla": ",", "campo": u["campo"], "st_ne": u["st_ne"], "aviso_visivel": u["aviso_visivel"]})
            self.chk(caso, "',' com texto selecionado: campo ','", u["campo"] == ",", u["campo"])
            self.chk(caso, "',': recusado, st.ne 1.5, localStorage igual", u["st_ne"] == 1.5 and u["ls"] == ls0, u["st_ne"])
            self.chk(caso, "',': aviso exato 'NE 1.5' e aria-invalid", u["aviso_visivel"] and u["aviso"] == AVISO.format(1.5) and u["aria"] == "true", u["aviso"])
            p.keyboard.press("Tab")
            u = self.ler(p, "D1")
            caso["passos"].append({"tecla": "Tab", "campo": u["campo"], "st_ne": u["st_ne"], "aviso_visivel": u["aviso_visivel"]})
            self.chk(caso, "Tab: campo '1.5', aria-invalid sai, aviso visível", u["campo"] == "1.5" and u["aria"] is None and u["aviso_visivel"], u)
            self.chk(caso, "Tab: localStorage igual", u["ls"] == ls0)
            # exportação (sem window.claude; cópia por stub de navigator.clipboard)
            p.evaluate("() => { window.__cap = null; ir('erros'); }")
            p.click("#exp")
            p.wait_for_function("() => window.__cap !== null")
            o = json.loads(p.evaluate("() => window.__cap"))
            d1 = [x for x in o["discursivas"] if x["id"] == "D1"]
            caso["final"] = {"exportado_D1": d1}
            self.chk(caso, 'exportação leva "ne": 1.5 sem arredondar', len(d1) == 1 and d1[0]["ne"] == 1.5, d1)
            self.chk(caso, "0 pageerror e 0 console.error", not erros, erros)
            self.casos.append(caso)
        finally:
            ctx.close()

    def rodar(self):
        self.caso_atributos("C1")
        for partida in ("vazio", "NE2"):
            for e in R + A:
                self.caso("C1", "D1", "tecla", partida, e)
        for e in R + A:
            self.caso("C2", "D1", "tecla", "vazio", e)
        for e in ["1,5", "1.5", "1,", ",5", "1.0", "15"]:
            self.caso("C3", "D3", "tecla", "vazio", e)
        for partida in ("vazio", "NE2"):
            self.caso("C4", "D1", "colar", partida, "1,5")
        for e in [" 3 ", "", "9007199254740991", "9007199254740992"]:
            self.caso("C4", "D1", "fill", "vazio", e)
        self.caso("C4", "D1", "fill", "NE2", "")  # acréscimo do QA: vazio a partir de NE 2 -> 0
        for cen in ("M1", "M2"):
            for partida in ("vazio", "NE2"):
                for e in R + A:
                    self.caso(cen, "D1", "tecla", partida, e)
            for e in R + A:
                self.caso(cen, "D1", "insert", "vazio", e)
            self.caso(cen, "D1", "colar", "vazio", "1,5")
            self.caso(cen, "D1", "colar", "NE2", "1,5")  # acréscimo do QA
        self.caso_legado()
        self.caso_atributos("XM1")
        self.caso_atributos("XM2")


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pagina", required=True)
    ap.add_argument("--pacote", required=True)
    ap.add_argument("--esperado", choices=["v17", "v16"], required=True)
    ap.add_argument("--saida", required=True)
    ap.add_argument("--executavel", default=None, help="caminho do Chromium, se o PLAYWRIGHT_BROWSERS_PATH não bastar")
    a = ap.parse_args()
    tmp = tempfile.mkdtemp(prefix="ne_v1_7_")
    try:
        shutil.copyfile(a.pagina, os.path.join(tmp, "index.html"))
        shutil.copyfile(a.pacote, os.path.join(tmp, "pacote.json"))
        pacote = json.load(open(a.pacote, encoding="utf-8"))
        srv, base = servir(tmp)
        t0 = time.time()
        with sync_playwright() as pw:
            try:
                br = pw.chromium.launch(executable_path=a.executavel) if a.executavel else pw.chromium.launch()
            except Exception:
                br = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium")
            s = Suite(base, pacote, a.esperado, br, pw.devices)
            s.rodar()
            versao_browser = br.version
            br.close()
        srv.shutdown()
        # controle negativo (D1 4.5)
        ctl = []
        for cen, modo, partida, e in CONTROLE:
            c = [x for x in s.casos if x["cenario"] == cen and x["modo"] == modo and x["partida"] == partida and x["entrada"] == e]
            f = c[0]["final"] if c else None
            ctl.append({"caso": "%s %s %s %r" % (cen, modo, partida, e), "st_ne": f and f["st_ne"], "aviso_visivel": f and f["aviso_visivel"],
                        "reproduz_15": bool(f) and f["st_ne"] == 15 and not f["aviso_visivel"]})
        if a.esperado == "v17":
            controle = "n/a"
            rc = 0 if s.nfalhas == 0 else 1
        else:
            controle = "OK" if all(x["reproduz_15"] for x in ctl) else "FALHOU"
            rc = 0 if controle == "OK" else 1
        divergentes = [{"cenario": c["cenario"], "modo": c["modo"], "partida": c["partida"], "entrada": c["entrada"],
                        "final_st_ne": c["final"] and c["final"].get("st_ne"), "esperado_st_ne": c["esperado"] and c["esperado"].get("st_ne"),
                        "falhas": [v["nome"] for v in c["verificacoes"] if not v["ok"]]} for c in s.casos if not c["ok"]]
        nao200 = [x for x in _Silencioso.status_log if x[1] != 200]
        out = {"suite": "ne_v1_7.py (T-70, D-T70-04)", "suite_sha256": sha(os.path.abspath(__file__)), "gerado_por": "QA-plataforma (opus)", "alvo": a.esperado,
               "pagina": {"arquivo": a.pagina, "sha256": sha(a.pagina), "bytes": os.path.getsize(a.pagina)},
               "pacote": {"arquivo": a.pacote, "sha256": sha(a.pacote), "nome": pacote.get("nome")},
               "browser_version": versao_browser, "playwright_version": importlib.metadata.version("playwright"),
               "python": sys.version.split()[0], "duracao_s": round(time.time() - t0, 1),
               "servidor_respostas_nao_200": nao200,
               "totais": {"casos": len(s.casos), "verificacoes": s.nverif, "falhas": s.nfalhas, "casos_com_falha": len(divergentes)},
               "controle": controle, "controle_casos": ctl,
               "limites": "Sem teclado físico nem teclado virtual real (Gboard, iOS); Android e iPhone emulados no Chromium "
                          "(viewport, agente, toque, eventos); sem WebKit real nem IME. A validação recai sobre o valor do campo.",
               "divergencias" if a.esperado == "v16" else "casos_com_falha": divergentes,
               "casos": s.casos}
        with open(a.saida, "w", encoding="utf-8") as fh:
            json.dump(out, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
        for c in divergentes[:60]:
            print("DIVERGE" if a.esperado == "v16" else "FALHA", c["cenario"], c["modo"], c["partida"], repr(c["entrada"]),
                  "st.ne", c["final_st_ne"], "esperado", c["esperado_st_ne"], "|", "; ".join(c["falhas"][:3]))
        for x in ctl:
            print("CONTROLE", x["caso"], "st.ne", x["st_ne"], "aviso", x["aviso_visivel"], "reproduz_15" if x["reproduz_15"] else "NAO_REPRODUZ")
        print("NE_V1_7 %s sha=%s verificacoes=%d falhas=%d controle=%s" % (a.esperado, sha(a.pagina)[:12], s.nverif, s.nfalhas, controle))
        return rc
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
