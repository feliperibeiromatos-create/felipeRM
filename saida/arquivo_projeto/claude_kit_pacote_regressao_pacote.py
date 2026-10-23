#!/usr/bin/env python3
"""Regressão da plataforma Câmara 2026 com um pacote novo embutido (Playwright + Chromium, sem rede obrigatória).

Uso: python3 regressao_pacote.py <index_teste.html> [--saida relatorio.md] [--chromium /opt/pw-browsers/chromium]

<index_teste.html> = cópia gerada por embute_pacote.py. Nada é publicado.
Cobre: abertura sem erro; estado de uma usuária antiga preservado; todos os cursos (com emUmMinuto e visuais do
pacote.topicos); Resumo por tópico; bloco de questões de todos os tópicos; diagnósticos e simulados; caderno de erros;
exportar meus erros; trocar e voltar o pacote; nota com 30 questões distintas (se algum tópico tiver 30+);
rolagem lateral em 360, 390 e 1280 px, claro e escuro; chaves do armazenamento.
"""
import json, os, sys, re, argparse
from playwright.sync_api import sync_playwright
ap = argparse.ArgumentParser(); ap.add_argument("html"); ap.add_argument("--saida"); ap.add_argument("--chromium")
a = ap.parse_args()
URL = "file://" + os.path.abspath(a.html)
R = {"ok": [], "falha": [], "info": []}
def chk(n, c, i=""): (R["ok"] if c else R["falha"]).append(f"{n} {i}".strip())
def info(t): R["info"].append(t)
def go(pg, js, ms=150): pg.evaluate(js); pg.wait_for_timeout(ms)
LEAK = re.compile(r"\[V \d|\[NORMATIVO|\[F\d+\]|\b(?:A5|BQ|L\d[A-Z]?|6[AB]|4C|5C)-[QR]?\d+\b|\bpar C\d+|Só o fato e a fonte")

def abrir(b, seed, w=360, scheme="light"):
    pg = b.new_page(viewport={"width": w, "height": 740}, color_scheme=scheme)
    pg.erros = []; pg.on("pageerror", lambda e: pg.erros.append(str(e)))
    pg.goto(URL)
    if seed is None: pg.evaluate("localStorage.clear()")
    else: pg.evaluate("s=>{localStorage.clear();localStorage.setItem('c2026.v01.estado',JSON.stringify(s))}", seed)
    pg.reload(); pg.wait_for_timeout(600); return pg
base = lambda **k: dict({"v": 1, "boasVindas": True, "escolha": {}, "tentativas": [], "erros": {}, "saidas": [], "lote": {}, "disc": {}, "vespera": {}, "eventos": []}, **k)

with sync_playwright() as p:
    b = p.chromium.launch(**({"executable_path": a.chromium} if a.chromium else {}))
    # ---------- R1 abertura ----------
    pg = abrir(b, None)
    dados = pg.evaluate("({n:P.itens.length,nome:P.nome,top:Object.keys(P.topicos||{}),ordem:T.ordem.length,curso:T.ordem.filter(id=>tp(id).temCurso),comQ:T.ordem.filter(id=>tp(id).n),v:VERSAO_APP,rep:CONTA_REPETIDAS})")
    info(f"pacote embutido: {dados['nome']} · {dados['n']} itens · {dados['ordem']} tópicos · topicos extras: {dados['top'] or 'nenhum'} · código {dados['v']} · CONTA_REPETIDAS={dados['rep']}")
    chk("R1 abre sem erro de JavaScript e mostra a apresentação", not pg.erros and pg.evaluate("rota.v") == "apresentacao", str(pg.erros[:2]))
    d30 = pg.evaluate("['P1','P2'].map(m=>{const s=simById('D30-'+m);return s?s.itens.length:0})")
    chk("R1 diagnósticos de 30 disponíveis nas duas matérias", d30 == [30, 30], str(d30))
    if pg.evaluate("typeof DEMO_DA!=='undefined'"):
        demo = pg.evaluate("({flag:DEMO_DA,ativo:DEMO_ATIVO})"); info(f"demonstração de formato de DA: DEMO_DA={demo['flag']}, ativa={demo['ativo']} (precisa estar desligada em cópia para publicação)")
    da = pg.evaluate("(()=>{const r={ok:true,n:0,ruins:[]};Object.values(T.top).forEach(o=>{const m=modOf(o.id);const d=discById(o.disc);if(d.modulo!==m){r.ok=false;r.ruins.push(o.id)} if(m==='DA')r.n++});P.itens.forEach(i=>{const o=T.top[i.itemEdital];if(o&&discById(o.disc).modulo!==modOf(i.itemEdital)){r.ok=false;r.ruins.push(i.id)}});return r})()")
    chk("R1 cada tópico e cada questão na matéria certa (TI, Fala, Direito Administrativo)", da["ok"], str(da["ruins"][:5]))
    info(f"tópicos de Direito Administrativo: {da['n']}")
    pg.close()

    # ---------- R2 usuária antiga ----------
    pg = abrir(b, None)
    ids = pg.evaluate("DIAG30.P2.slice(0,3)")
    pg.close()
    seed = base(concurso="cd26-c11", discVista=True, avisoD30=True, apresVista=True, escolha={"P1": "diag", "P2": "zero"},
                escolhaDisc={"cd26-c11/p1/ti": "diag", "cd26-c11/p2/fala": "zero"},
                tentativas=[{"tipo": "sim", "ref": "D30-P2", "nome": "Diagnóstico · Fala, transcrição e IA", "data": 1792200000000, "nota": 1, "total": 3, "ac": 2, "er": 1, "br": 0, "seg": 60, "por": {},
                             "det": [{"id": ids[0], "r": "C", "st": "c"}, {"id": ids[1], "r": "C", "st": "c"}, {"id": ids[2], "r": "C", "st": "e"}], "modulo": "P2"}],
                erros={ids[2]: {"errou": 1, "seq": 0, "desde": 1792200000000}, "ID-QUE-NAO-EXISTE": {"errou": 1, "seq": 0, "desde": 1}},
                disc={"D1": {"texto": "rascunho", "entregue": False, "notas": {}, "ne": 0}})
    pg = abrir(b, seed)
    st = pg.evaluate("JSON.parse(localStorage.getItem('c2026.v01.estado'))")
    chk("R2 usuária antiga entra no Painel sem erro", pg.evaluate("rota.v") == "painel" and not pg.erros, str(pg.erros[:2]))
    chk("R2 tentativas, erros, rascunho e escolhas preservados", st["tentativas"] == seed["tentativas"] and st["erros"] == seed["erros"] and st["disc"] == seed["disc"] and st["escolhaDisc"] == seed["escolhaDisc"])
    go(pg, "ir('erros')")
    chk("R2 Erros mostra o item que existe e ignora id ausente do pacote", pg.locator(f".par[data-id='{ids[2]}']").count() == 1 and pg.locator(".par[data-id='ID-QUE-NAO-EXISTE']").count() == 0)
    chk("R2 só a chave de estado no armazenamento", sorted(pg.evaluate("Object.keys(localStorage)")) == ["c2026.v01.estado"])
    pg.close()

    # ---------- R3 cursos, R4 resumos, R5 blocos ----------
    pg = abrir(b, base(concurso="cd26-c11", discVista=True, avisoD30=True, apresVista=True))
    falhas, vaz = [], {}
    for tid in dados["curso"]:
        n0 = len(pg.erros); go(pg, f"ir('curso','{tid}')", 60)
        ex = pg.evaluate(f"tp('{tid}').extra||{{}}")
        ok = len(pg.erros) == n0 and pg.locator("#fimCurso").count() == 1
        if ex.get("emUmMinuto"): ok = ok and pg.locator(".em1 li").count() == len(ex["emUmMinuto"])
        if ex.get("visuais"):
            tit = [v.get("titulo") for v in ex["visuais"] if v.get("titulo")]
            txt = pg.text_content("#app")
            ok = ok and all(t in txt for t in tit)
        if not ok: falhas.append(tid)
        m = LEAK.findall(pg.inner_text("#app"))
        if m: vaz[tid] = len(m)
    chk(f"R3 os {len(dados['curso'])} cursos abrem sem erro, com 'Em 1 minuto' e visuais do pacote quando houver", not falhas, str(falhas[:8]))
    info(f"marcas de produção ainda visíveis nos cursos (depois da limpeza de exibição): {sum(vaz.values())} em {len(vaz)} tópico(s) {dict(list(vaz.items())[:8])}")
    go(pg, "ir('resumo')")
    rt = pg.evaluate("[...document.querySelectorAll('[data-rt]')].map(b=>b.dataset.rt)")
    com_res = [k for k in dados["top"] if pg.evaluate(f"!!(tp('{k}')&&tp('{k}').topico&&tp('{k}').extra&&tp('{k}').extra.resumo)")]
    chk("R4 cada resumo de tópico do pacote aparece na aba Resumo", sorted(rt) == sorted(com_res), f"(aba {rt} × pacote {com_res})")
    rr = []
    for k in rt:
        n0 = len(pg.erros); go(pg, f"ir('resumoVer',{{topico:'{k}'}})", 60)
        pal = pg.evaluate(f"tp('{k}').extra.resumo.replace(/[*#|]/g,' ').split(/\\s+/).filter(w=>w.length>3).slice(0,3)")
        if len(pg.erros) != n0 or not all(w in pg.text_content("#app") for w in pal): rr.append(k)
    chk("R4 resumos de tópico abrem e mostram o texto", not rr, str(rr))
    bl = []
    for tid in dados["comQ"]:
        n0 = len(pg.erros); go(pg, f"iniciarBloco('{tid}')", 40)
        o = pg.evaluate(f"({{ord:prova.ordem,tp:prova.ordem.map(i=>M[i].itemEdital),n:tp('{tid}').n}})")
        if len(pg.erros) != n0 or len(set(o["ord"])) != len(o["ord"]) or set(o["tp"]) != {tid} or len(o["ord"]) != min(10, o["n"]): bl.append(tid)
        go(pg, "prova=null", 10)
    chk(f"R5 bloco de questões dos {len(dados['comQ'])} tópicos: até 10 questões distintas do próprio tópico", not bl, str(bl[:8]))

    # ---------- R6 simulados, entrega, caderno, exportar ----------
    sims = pg.evaluate("listaSimulados().map(s=>s.id)")
    ruins = []
    for s in sims:
        n0 = len(pg.erros); go(pg, f"iniciar('{s}')", 60)
        if len(pg.erros) != n0 or pg.evaluate("rota.v") != "prova": ruins.append(s)
        go(pg, "clearInterval(prova.timer);prova=null", 10)
    chk(f"R6 os {len(sims)} simulados e diagnósticos abrem", not ruins, str(ruins))
    go(pg, "iniciar('D30-P1')")
    g = pg.evaluate("M[prova.ordem[0]].gabarito"); pg.click("#bE" if g == "C" else "#bC")
    go(pg, "prova.i=prova.ordem.length-1; render()"); pg.click("#fim"); pg.click("#sim2"); pg.wait_for_timeout(300)
    st = pg.evaluate("JSON.parse(localStorage.getItem('c2026.v01.estado'))")
    chk("R6 diagnóstico entregue: nota −1, item errado no caderno, 30 respostas registradas",
        st["tentativas"][-1]["nota"] == -1 and len(st["erros"]) == 1 and sum(1 for r in st["resp"] if r["o"] == "diag") == 30)
    go(pg, "ir('dados')"); pg.click("#exp"); pg.wait_for_timeout(800)
    if pg.locator("#expTxt").count():
        j = json.loads(pg.input_value("#expTxt")); chk("R6 exportar: JSON válido com o caderno", j["formato"] == "camara2026.erros" and j["resumo"]["itensNoCaderno"] == 1)
    else:
        t = pg.text_content("#toast") or ""; chk("R6 exportar: arquivo ou área de transferência", "copiado" in t.lower() or "salvo" in t.lower(), t)

    # ---------- R7 trocar o pacote e voltar ----------
    pk = pg.evaluate("JSON.stringify({versao:1,nome:'teste',geradoEm:'2026-10-18',itens:P.itens.slice(0,5),simulados:[],lotes:[],edital:P.edital})")
    pg.click("summary:has-text('Dados técnicos')"); pg.fill("#js", pk); pg.click("#car"); pg.wait_for_timeout(400)
    ok1 = pg.evaluate("P.itens.length") == 5
    pg.click("summary:has-text('Dados técnicos')"); pg.click("#pub"); pg.wait_for_timeout(400)
    st2 = pg.evaluate("JSON.parse(localStorage.getItem('c2026.v01.estado'))")
    chk("R7 carregar outro pacote.json e voltar ao publicado sem perder progresso", ok1 and pg.evaluate("P.itens.length") == dados["n"] and st2["tentativas"] == st["tentativas"] and st2["erros"] == st["erros"])

    # ---------- R8 nota com 30 questões distintas ----------
    alvo = pg.evaluate("T.ordem.find(id=>tp(id).n>=JANELA)")
    if alvo:
        for _ in range(8):
            go(pg, f"iniciarBloco('{alvo}')", 40)
            k = pg.evaluate("prova.ordem.length")
            for i in range(k):
                pg.evaluate("i=>{prova.i=i;render()}", i); g = pg.evaluate("M[prova.ordem[prova.i]].gabarito"); pg.click("#bC" if g == "C" else "#bE")
            go(pg, "prova.i=prova.ordem.length-1; render()", 20); pg.click("#fim"); pg.click("#sim2"); pg.wait_for_timeout(200)
            if pg.evaluate(f"notaTopico('{alvo}').nota") is not None: break
        nt = pg.evaluate(f"notaTopico('{alvo}')")
        chk(f"R8 nota aparece no tópico {alvo} com 30 questões distintas", nt["nota"] == 30 and nt["n"] == 30, str(nt))
    else:
        info("R8 nenhum tópico com 30 ou mais questões: nota por tópico ainda impossível com este pacote")
    chk("R  nenhum erro de JavaScript na sessão longa", not pg.erros, str(pg.erros[:3]))
    pg.close()

    # ---------- R9 layout ----------
    extra_t = [k for k in dados["top"] if k in dados["curso"]][:3] or dados["curso"][:1]
    telas = ["ir('painel')", "ir('materia','cd26-c11/p2/fala')", "ir('materia','cd26-c11/p1/ti')", "ir('resumo')", "ir('erros')", "ir('recomendacoes')", "ir('pratica')"] + [f"ir('curso','{k}')" for k in extra_t]
    for scheme in ["light", "dark"]:
        for w in [360, 390, 1280]:
            pg = abrir(b, base(concurso="cd26-c11", discVista=True, avisoD30=True, apresVista=True), w, scheme)
            ruins = []
            for t in telas:
                go(pg, t, 60)
                x = pg.evaluate("({sw:document.documentElement.scrollWidth,w:document.documentElement.clientWidth})")
                if x["sw"] > x["w"]: ruins.append(t)
            chk(f"R9 {scheme}-{w}: sem rolagem lateral em {len(telas)} telas", not ruins and not pg.erros, str(ruins + pg.erros[:1]))
            pg.close()
    b.close()

L = ["# Regressão com pacote novo", "", f"Arquivo: `{a.html}`", f"**{len(R['ok'])} ok · {len(R['falha'])} falha(s)**", ""]
L += ["## Falhas"] + ([f"- {x}" for x in R["falha"]] or ["- nenhuma"]) + ["", "## Informações"] + [f"- {x}" for x in R["info"]] + ["", "## Aprovados"] + [f"- {x}" for x in R["ok"]]
rel = "\n".join(L)
if a.saida: open(a.saida, "w", encoding="utf-8").write(rel)
print(rel)
sys.exit(1 if R["falha"] else 0)
