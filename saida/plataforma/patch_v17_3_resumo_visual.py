#!/usr/bin/env python3
"""patch_v17_3_resumo_visual.py — Plataforma v17.3: Resumo visual de Direito Administrativo (ESPEC_resumo_visual_DA_v3, 28/10/2026).
Aplica sobre o template v17.2 (= versão no ar + janela 20 + refazer). Só acrescenta: CSS do Resumo visual, 16 ícones SVG, 5 tipos
novos de visual (piramide, mapa, dois, escala, linhaTempo) e a tela vResumoVisual, aberta pelo botão "Resumo" quando o tópico tiver
`topicos[id].resumoVisual`; sem ele, a tela atual continua. Nada do pacote, da nota, do curso ou das questões muda.
Uso: python3 -I patch_v17_3_resumo_visual.py <template_v17_2_entrada> <template_v17_3_saida>
"""
import sys
src, dst = sys.argv[1], sys.argv[2]
h = open(src, encoding="utf-8").read()
N = 0

def sub1(old, new, label):
    global h, N
    c = h.count(old)
    if c != 1:
        sys.exit(f"ERRO: âncora '{label}' encontrada {c} vezes (esperado 1)")
    h = h.replace(old, new)
    N += 1

sub1('const VERSAO_APP="v17.2";', 'const VERSAO_APP="v17.3";', "VERSAO_APP")

# ---------- 1. CSS (antes do bloco v17 do Fundador) ----------
CSS = r"""/* v17.3 · Resumo visual de Direito Administrativo (ESPEC_resumo_visual_DA_v3, 28/10/2026): estética MapasPro traduzida ao sistema v0.2.
   Preto → tinta; amarelo → marcador; emojis → ícones SVG em currentColor; azul de atenção → caixa --soft com borda tinta-2; verde/vermelho continuam só para certo/erro. */
.rv{font-size:17px;line-height:1.55;max-width:62ch}
.rv-cab{border-left:4px solid var(--marker);padding-left:14px;margin-top:6px}
.rv-cab h1{font-size:26px;line-height:1.2}
.rv-cob{display:inline-flex;align-items:center;gap:8px;margin-top:10px;border:1.5px solid var(--ink-2);border-radius:999px;padding:4px 12px;font-size:13.5px;color:var(--ink-2);background:var(--paper);cursor:pointer;min-height:36px}
.rv-cob b{color:var(--ink)}
.rv-cob .rv-ic{width:16px;height:16px;color:var(--marker)}
.rv-cobnota{font-size:13.5px;color:var(--ink-2);margin-top:6px;line-height:1.45}
.rv-sec{display:flex;align-items:center;gap:10px;background:var(--ink);color:var(--on-strong);border-radius:10px;padding:11px 14px;margin:30px 0 0;font-size:15px;letter-spacing:.08em;text-transform:uppercase;font-weight:700}
.rv-sec .rv-ic{width:20px;height:20px;color:var(--marker);flex:none}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .rv-sec .rv-ic{color:var(--on-strong)}}
:root[data-theme="dark"] .rv-sec .rv-ic{color:var(--on-strong)}
.rv-sub{display:flex;align-items:center;gap:8px;background:var(--marker-soft);border-left:4px solid var(--marker);border-radius:0 8px 8px 0;padding:8px 12px;margin:20px 0 0;font-size:16.5px;font-weight:700;color:var(--ink)}
.rv-sub .rv-ic{width:18px;height:18px;color:var(--ink-2);flex:none}
.rv-ic{display:inline-block;vertical-align:-3px}
.rv-ic svg{width:100%;height:100%;display:block;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.rv p{margin-top:12px}
.rv .tabwrap{margin-top:12px}
.rv table.tc th{background:var(--ink);color:var(--on-strong);border-bottom:0}
.rv table.tc tbody tr:nth-child(even) td{background:var(--soft)}
.rv table.tc td:first-child{font-weight:700}
.rv .pilha table.tc td:first-child{font-weight:700}
.rv-box{border-radius:10px;padding:12px 14px 14px;margin-top:16px;background:var(--soft);border-left:4px solid var(--ink-2)}
.rv-box.regra{background:var(--marker-soft);border-left-color:var(--marker)}
.rv-box.exemplo{background:var(--paper);border:1px solid var(--rule);border-left:4px solid var(--ink-2)}
.rv-box .bxl{display:flex;align-items:center;gap:6px;color:var(--ink-2)}
.rv-box .bxl .rv-ic{width:15px;height:15px}
.rv-box p{margin-top:6px}
/* pirâmide: níveis em trapézio, base larga embaixo */
.rv-pir{list-style:none;margin:12px 0 0;padding:0;display:flex;flex-direction:column;align-items:center;gap:4px}
.rv-pir .nv{position:relative;text-align:center;box-sizing:border-box;padding:10px calc(var(--c) + 10px);clip-path:polygon(var(--c) 0,calc(100% - var(--c)) 0,100% 100%,0 100%);background:var(--soft);color:var(--ink);overflow-wrap:anywhere}
@media (max-width:600px){.rv-pir .nv{width:100% !important;--c:6% !important}}
.rv-pir .nv b{display:block;font-size:14px;letter-spacing:.06em;text-transform:uppercase}
.rv-pir .nv span{display:block;font-size:14.5px;line-height:1.35;margin-top:2px}
.rv-pir .nv.n1{background:var(--ink);color:var(--on-strong)}
.rv-pir .nv.n2{background:var(--marker);color:#1B2A41}
.rv-pir .nv.n3{background:var(--soft);color:var(--ink);border-bottom:2px solid var(--ink)}
/* mapa: centro e ramos */
.rv-mapa{margin-top:12px;display:grid;grid-template-columns:1fr 1fr;gap:10px}
.rv-mapa .ctr{grid-column:1/-1;justify-self:center;background:var(--ink);color:var(--on-strong);border-radius:999px;padding:10px 18px;font-weight:700;text-align:center;max-width:90%}
.rv-mapa .ramo{border:1.5px solid var(--rule);border-left:4px solid var(--marker);border-radius:8px;padding:10px 12px;background:var(--paper)}
.rv-mapa .ramo b{display:block;font-size:15px}
.rv-mapa .ramo span{display:block;font-size:14.5px;color:var(--ink-2);line-height:1.4;margin-top:3px}
@media (max-width:480px){ .rv-mapa{grid-template-columns:1fr} }
/* dois painéis */
.rv-dois{margin-top:12px;display:grid;grid-template-columns:1fr 1fr;gap:10px}
.rv-dois .pn{border:1.5px solid var(--rule);border-radius:10px;overflow:hidden;background:var(--paper)}
.rv-dois .pn h4{margin:0;padding:10px 12px;font-size:15px;background:var(--ink);color:var(--on-strong)}
.rv-dois .pn.b h4{background:var(--marker);color:#1B2A41}
.rv-dois .pn ul{margin:0;padding:10px 12px 12px 28px;font-size:15px}
.rv-dois .pn li{margin-top:6px}
.rv-dois .pe{grid-column:1/-1;text-align:center;font-weight:700;padding:8px 12px;border:2px dashed var(--ink-2);border-radius:8px;color:var(--ink)}
@media (max-width:480px){ .rv-dois{grid-template-columns:1fr} }
/* escala */
.rv-esc{margin-top:12px}
.rv-esc .barra{height:10px;border-radius:5px;background:linear-gradient(90deg,var(--ink),var(--marker));margin:6px 0 4px}
.rv-esc .ext{display:flex;justify-content:space-between;font-size:13px;color:var(--ink-2);letter-spacing:.06em;text-transform:uppercase}
.rv-esc ol{list-style:none;margin:8px 0 0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:8px;counter-reset:pt}
.rv-esc li{counter-increment:pt;border:1.5px solid var(--rule);border-radius:8px;padding:8px 10px;font-size:14px;line-height:1.35;position:relative}
.rv-esc li::before{content:counter(pt);display:inline-grid;place-items:center;width:20px;height:20px;border-radius:50%;background:var(--ink);color:var(--on-strong);font-size:12px;font-weight:700;margin-right:6px}
.rv-esc li b{display:inline}
.rv-esc li span{display:block;color:var(--ink-2);margin-top:3px}
/* linha do tempo */
.rv-lt{list-style:none;margin:12px 0 0;padding:0 0 0 18px;border-left:3px solid var(--ink)}
.rv-lt li{position:relative;margin-top:12px;padding-left:6px}
.rv-lt li::before{content:"";position:absolute;left:-27px;top:6px;width:13px;height:13px;border-radius:50%;background:var(--marker);border:2.5px solid var(--ink)}
.rv-lt .q{display:inline-block;font-size:12.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-2)}
.rv-lt b{display:block;font-size:15.5px}
.rv-lt span{display:block;font-size:14.5px;color:var(--ink-2);line-height:1.4}
/* relâmpago e pegadinhas */
.rv-rel{margin:12px 0 0;padding:0;list-style:none;counter-reset:rl}
.rv-rel li{counter-increment:rl;display:grid;grid-template-columns:26px minmax(0,1fr);gap:8px;align-items:start;padding:8px 0;border-bottom:1px solid var(--rule);font-size:15.5px}
.rv-rel li::before{content:counter(rl);display:inline-grid;place-items:center;width:24px;height:24px;border-radius:50%;background:var(--marker);color:#1B2A41;font-size:12.5px;font-weight:700;margin-top:2px}
.rv-peg{margin-top:12px;display:flex;flex-direction:column;gap:10px}
.rv-peg .par{border:1.5px solid var(--rule);border-radius:10px;padding:10px 12px;margin:0}
.rv-peg .l{display:grid;grid-template-columns:22px minmax(0,1fr);gap:8px;align-items:start;font-size:15px}
.rv-peg .l+.l{margin-top:6px}
.rv-peg .l .rv-ic{width:18px;height:18px;color:var(--ink);margin-top:2px}
.rv-peg .l.e{color:var(--ink-2)}
.rv-peg .l.e .rv-ic{color:var(--ink-2)}
.rv-peg .l b{font-weight:700;margin-right:4px}
.rv-img{margin:16px 0 0}
.rv-img img{display:block;width:100%;height:auto;border-radius:10px;border:1px solid var(--rule)}
.rv-img figcaption{font-size:13.5px;color:var(--ink-2);margin-top:6px}
.rv-fontes{margin-top:26px;padding-top:12px;border-top:1px solid var(--rule);font-size:13.5px;color:var(--ink-2)}
"""
sub1("/* v17 · ordem do Fundador (D-V17-DESIGN, 21/10/2026): painel com média por matéria",
     CSS + "/* v17 · ordem do Fundador (D-V17-DESIGN, 21/10/2026): painel com média por matéria", "CSS")

# ---------- 2. JS: ícones, tipos novos, tela ----------
JS = r"""/* ---------- v17.3 · Resumo visual (ESPEC_resumo_visual_DA_v3) ---------- */
const ICONES={
 alvo:'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>',
 pino:'<path d="M12 21s-6-5.2-6-10a6 6 0 0 1 12 0c0 4.8-6 10-6 10z"/><circle cx="12" cy="11" r="2.2"/>',
 balanca:'<path d="M12 3v18M4 21h16M6 7h12M6 7l-3 7a3 3 0 0 0 6 0zM18 7l-3 7a3 3 0 0 0 6 0z"/>',
 predio:'<path d="M3 21h18M5 21V8l7-4 7 4v13M9 21v-5h6v5M9 11h.01M15 11h.01M9 14h.01M15 14h.01"/>',
 pessoas:'<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20a6 6 0 0 1 12 0M14 20a4.5 4.5 0 0 1 7 0"/>',
 doc:'<path d="M7 3h7l4 4v14H7zM14 3v4h4M9.5 12h5M9.5 16h5"/>',
 relogio:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 cadeado:'<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
 aviso:'<path d="M12 3l10 18H2zM12 10v4M12 17.5h.01"/>',
 confere:'<path d="M4 12.5l5 5L20 7"/>',
 x:'<path d="M6 6l12 12M18 6L6 18"/>',
 raio:'<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 chave:'<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M16 7l3 3M18 5l2 2"/>',
 livro:'<path d="M4 4h7a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4zM20 4h-7a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h8z"/>',
 seta:'<path d="M5 12h14M13 6l6 6-6 6"/>',
 engrenagem:'<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/>'
};
function ico(n,cls){ const p=ICONES[n]||ICONES.pino; return `<span class="rv-ic ${cls||""}" aria-hidden="true"><svg viewBox="0 0 24 24">${p}</svg></span>`; }
const rvInline=s=>esc(s).replace(/\*\*(.+?)\*\*/g,"<b>$1</b>");
/* tipos novos (também aceitos em `visuais` do curso) */
function visualV3(v){
  if(v.tipo==="piramide"){ const n=v.niveis.length; const W=v.niveis.map((_,i)=>Math.round(60+40*i/Math.max(1,n-1))); // largura de cada nível, do topo (60%) à base (100%); no celular, 100% (CSS)
    return `<figure class="vis" role="group" aria-label="${esc((v.titulo||"Pirâmide")+", do topo à base")}">${v.titulo?`<figcaption class="vt">${esc(v.titulo)}</figcaption>`:""}<ol class="rv-pir">${v.niveis.map((x,i)=>{ const c=i?Math.min(12,Math.round(50*(1-W[i-1]/W[i]))):10; return `<li class="nv n${Math.min(3,i+1)}" style="width:${W[i]}%;--c:${c}%"><b>${esc(x.titulo)}</b>${x.texto?`<span>${rvInline(x.texto)}</span>`:""}</li>`; }).join("")}</ol>${v.legenda?`<p class="leg">${esc(v.legenda)}</p>`:""}</figure>`; }
  if(v.tipo==="mapa") return `<figure class="vis">${v.titulo?`<figcaption class="vt">${esc(v.titulo)}</figcaption>`:""}<div class="rv-mapa" role="group" aria-label="${esc(v.titulo||v.centro)}"><div class="ctr">${esc(v.centro)}</div>${v.ramos.map(r=>`<div class="ramo"><b>${rvInline(r.titulo)}</b>${r.texto?`<span>${rvInline(r.texto)}</span>`:""}</div>`).join("")}</div>${v.legenda?`<p class="leg">${esc(v.legenda)}</p>`:""}</figure>`;
  if(v.tipo==="dois") return `<figure class="vis">${v.titulo?`<figcaption class="vt">${esc(v.titulo)}</figcaption>`:""}<div class="rv-dois" role="group" aria-label="${esc(v.titulo||(v.a.titulo+" × "+v.b.titulo))}"><div class="pn a"><h4>${esc(v.a.titulo)}</h4><ul>${v.a.itens.map(x=>`<li>${rvInline(x)}</li>`).join("")}</ul></div><div class="pn b"><h4>${esc(v.b.titulo)}</h4><ul>${v.b.itens.map(x=>`<li>${rvInline(x)}</li>`).join("")}</ul></div>${v.pe?`<div class="pe">${rvInline(v.pe)}</div>`:""}</div>${v.legenda?`<p class="leg">${esc(v.legenda)}</p>`:""}</figure>`;
  if(v.tipo==="escala") return `<figure class="vis rv-esc" role="group" aria-label="${esc(v.titulo||"Escala")}">${v.titulo?`<figcaption class="vt">${esc(v.titulo)}</figcaption>`:""}<div class="ext"><span>${esc(v.esquerda)}</span><span>${esc(v.direita)}</span></div><div class="barra" aria-hidden="true"></div><ol>${v.pontos.map(p=>`<li><b>${rvInline(p.rotulo)}</b>${p.texto?`<span>${rvInline(p.texto)}</span>`:""}</li>`).join("")}</ol>${v.legenda?`<p class="leg">${esc(v.legenda)}</p>`:""}</figure>`;
  if(v.tipo==="linhaTempo") return `<figure class="vis">${v.titulo?`<figcaption class="vt">${esc(v.titulo)}</figcaption>`:""}<ol class="rv-lt">${v.marcos.map(m=>`<li>${m.quando?`<span class="q">${esc(m.quando)}</span>`:""}<b>${rvInline(m.titulo)}</b>${m.texto?`<span>${rvInline(m.texto)}</span>`:""}</li>`).join("")}</ol>${v.legenda?`<p class="leg">${esc(v.legenda)}</p>`:""}</figure>`;
  return "";
}
function blocoRV(b,tid){
  switch(b.t){
    case "secao": return `<h2 class="rv-sec">${ico(b.icone||"pino")}<span>${esc(b.titulo)}</span></h2>`;
    case "sub": return `<h3 class="rv-sub">${b.icone?ico(b.icone):""}<span>${esc(b.titulo)}</span></h3>`;
    case "texto": return `<p>${rvInline(b.md)}</p>`;
    case "lista": return `<ul>${(b.itens||[]).map(x=>`<li>${rvInline(x)}</li>`).join("")}</ul>`;
    case "tabela": return visual(Object.assign({tipo:"tabela"},b));
    case "compare": return visual(Object.assign({tipo:"compare"},b));
    case "fluxo": case "esquema": case "linha": case "barras": return visual(Object.assign({tipo:b.t},b));
    case "lei": return visual(Object.assign({tipo:"baseLegal"},b));
    case "box": { const ic={atencao:"aviso",regra:"cadeado",exemplo:"doc"}[b.tipo]||"aviso"; return `<div class="rv-box ${esc(b.tipo||"atencao")}"><p class="bxl">${ico(ic)}<span>${esc(b.rotulo||{atencao:"Atenção",regra:"Regra",exemplo:"Exemplo"}[b.tipo]||"Atenção")}</span></p><p>${rvInline(b.md)}</p></div>`; }
    case "piramide": case "mapa": case "dois": case "escala": case "linhaTempo": return visualV3(Object.assign({tipo:b.t},b));
    case "relampago": return `<h2 class="rv-sec">${ico("raio")}<span>Resumo relâmpago</span></h2><ol class="rv-rel">${(b.itens||[]).map(x=>`<li><span>${rvInline(x)}</span></li>`).join("")}</ol>`;
    case "pegadinhas": return `<h2 class="rv-sec">${ico("aviso")}<span>Possíveis pegadinhas</span></h2><div class="rv-peg">${(b.itens||[]).map(p=>`<div class="par"><div class="l e">${ico("x")}<span><b>Errado:</b> ${rvInline(p.errado)}</span></div><div class="l c">${ico("confere")}<span><b>Certo:</b> ${rvInline(p.certo)}</span></div></div>`).join("")}</div>`;
    case "imagem": return b.src?`<figure class="rv-img"><img src="${esc(b.src)}" alt="${esc(b.alt||"")}" loading="lazy">${b.legenda?`<figcaption>${esc(b.legenda)}</figcaption>`:""}</figure>`:"";
    default: return "";
  }
}
function vResumoVisual(o){
  const rv=o.extra.resumoVisual; const d=discById(o.disc); const c=rv.cobranca||null;
  ev("resumo_visual_aberto",{ref:o.id});
  const poucas=c&&c.itens<=3; // ESPEC §4: até 3 questões, "poucas questões no corpus" (0 = "nenhuma questão enquadrada"); o número exato fica na nota
  const cob=c?`<button class="rv-cob" id="rvCob" aria-expanded="false">${ico("alvo")}<span>Cebraspe 2025: ${poucas?(c.itens===0?`<b>nenhuma questão enquadrada</b> neste item no corpus`:`<b>poucas questões</b> deste item no corpus`):`<b>${esc(String(c.itens))}</b> ${c.itens===1?"questão":"questões"} deste item no corpus${c.ce!=null?` (${esc(String(c.ce))} C/E)`:""}`}</span></button><p class="rv-cobnota" id="rvCobNota" hidden>${poucas?`${esc(String(c.itens))} ${c.itens===1?"questão enquadrada":"questões enquadradas"} neste item${c.ce!=null?` (${esc(String(c.ce))} C/E)`:""}. `:""}${esc(c.fonte||"")} Base: 1.321 questões de Direito Administrativo de 143 provas Cebraspe de 2025, enquadradas por item do edital pelo pacote de auditoria; medida de forma e de frequência, não garantia de cobrança.</p>`:"";
  app().innerHTML=`${topo()}<div class="stack l leitura">
   <p><button class="link" id="volta">← ${esc(curtoDisc(d))}</button></p>
   <div class="rv-cab"><p class="eyebrow">Resumo visual · item ${esc(curtoId(o.id))}</p><h1 style="margin-top:4px">${esc(o.num)} ${esc(o.nome)}</h1>${cob}</div>
   <div class="rv">${(rv.blocos||[]).map(b=>blocoRV(b,o.id)).join("")}
   ${(rv.fontes||[]).length?`<p class="rv-fontes">Fontes: ${rv.fontes.map(esc).join(" · ")}</p>`:""}</div>
   <div class="stack"><h2>Este tópico</h2><div class="prep" style="color:var(--ink)"><span><b class="num">${esc(o.num)}</b> ${esc(o.nome)}</span><span>${o.temCurso?`<button class="link" data-curso="${o.id}">curso</button>`:""}${o.n?` <button class="link" data-q="${o.id}">questões</button>`:""}</span></div></div>
  </div>`;
  $("#volta").onclick=()=>ir("materia",{disc:o.disc,top:o.id}); ligaTopicos();
  const bc=$("#rvCob"); if(bc) bc.onclick=()=>{ const n=$("#rvCobNota"); n.hidden=!n.hidden; bc.setAttribute("aria-expanded",String(!n.hidden)); };
}
"""
sub1("function vResumoVer(arg){\n", JS + "function vResumoVer(arg){\n", "JS antes de vResumoVer")

# ---------- 3. gancho: o botão Resumo abre a tela nova quando houver resumoVisual ----------
sub1("""  if(arg&&arg.topico&&tp(arg.topico)){ const o=tp(arg.topico); titulo=`${o.num} ${o.nome}`; corpo=o.extra.resumo; its=[o.id]; }""",
     """  if(arg&&arg.topico&&tp(arg.topico)&&tp(arg.topico).extra&&tp(arg.topico).extra.resumoVisual) return vResumoVisual(tp(arg.topico)); // v17.3
  if(arg&&arg.topico&&tp(arg.topico)){ const o=tp(arg.topico); titulo=`${o.num} ${o.nome}`; corpo=o.extra.resumo; its=[o.id]; }""",
     "gancho vResumoVer")
# resumoRef: tópico com resumoVisual mas sem resumo também abre
sub1("""function resumoRef(o){ if(o.extra&&o.extra.resumo) return {topico:o.id};""",
     """function resumoRef(o){ if(o.extra&&(o.extra.resumo||o.extra.resumoVisual)) return {topico:o.id}; // v17.3""",
     "resumoRef")
# os tipos novos também valem em `visuais` do curso
sub1("""  if(v.tipo==="barras"){ const mx=Math.max(...v.dados.map(x=>x.valor),1);""",
     """  if(["piramide","mapa","dois","escala","linhaTempo"].includes(v.tipo)) return visualV3(v); // v17.3
  if(v.tipo==="barras"){ const mx=Math.max(...v.dados.map(x=>x.valor),1);""",
     "visual() tipos v3")

open(dst, "w", encoding="utf-8", newline="\n").write(h)
print(f"OK: {N} substituições · {dst}")
