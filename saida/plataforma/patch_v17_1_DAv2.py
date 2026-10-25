#!/usr/bin/env python3
"""Aplica as mudanças DA-v2 (ESPEC v2 + adendo v2.1) ao template v17 da plataforma. Só acrescenta; nada da v17 é removido.
Uso: python3 -I patch_dav2.py <template_v17_entrada> <template_saida>
"""
import sys, re
src, dst = sys.argv[1], sys.argv[2]
h = open(src, encoding="utf-8").read()
n0 = len(h)

def sub1(old, new, label):
    global h
    if h.count(old) != 1:
        sys.exit(f"ERRO: âncora '{label}' encontrada {h.count(old)} vezes")
    h = h.replace(old, new)

# ---------- 1. CSS ----------
css_anchor = "/* v16 · Direito Administrativo: quadro BASE LEGAL no curso e visual baseLegal (só variáveis do sistema visual v0.2) */"
css_new = css_anchor + r"""
/* v17 · DA-v2 (ESPEC_curso_DA_formato_v2 + adendo v2.1, 24/10/2026): tarefas, glossário, caso, item intercalado, pares A/B/MUDA, fechamento, comentário em 3 linhas, mecanismo */
.tarefas{border:2px solid var(--ink);border-radius:10px;padding:12px 14px 14px;margin-top:14px}
.tarefas ol{margin:6px 0 0;padding-left:22px}
.tarefas li{margin-top:6px}
.bx.glo{background:var(--soft)}
.bx.glo ul{list-style:none;padding:0;margin-top:6px}
.bx.glo li{padding-block:5px;border-bottom:1px solid var(--rule);font-size:15.5px}
.bx.glo li:last-child{border-bottom:0}
.bx.glo li b{color:var(--ink)}
.bx.caso{background:var(--paper);border:2px dashed var(--ink-2)}
.bx.caso .bxl{color:var(--ink-2)}
.bx.rcaso{background:var(--paper);border:1px solid var(--rule)}
.bx.rcaso details>summary{cursor:pointer;min-height:44px;display:flex;align-items:center;font-weight:700}
.bx.rcaso details>summary::-webkit-details-marker{display:none}
.bx.rcaso details>summary::before{content:"▸";margin-right:8px;color:var(--ink-2)}
.bx.rcaso details[open]>summary::before{content:"▾"}
.par3g{display:grid;grid-template-columns:auto minmax(0,1fr);gap:4px 12px;margin-top:8px;font-size:15.5px}
.par3g .k{font-size:12.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2);padding-top:3px}
.par3g .muda{font-weight:700}
.iti{border:2px solid var(--ink);border-radius:10px;padding:12px 14px 14px;margin-top:18px;background:var(--paper)}
.iti .itc{font-size:14px;color:var(--ink-2)}
.iti .ite{font-size:17px;margin-top:6px;line-height:1.45}
.iti .ce{margin-top:10px;gap:14px}
.iti .bolha.sm{width:56px;height:56px;font-size:24px}
.iti .bolha.okk{background:var(--c);border-color:var(--c);color:var(--on-strong)}
.iti .bolha.err{background:var(--e);border-color:var(--e);color:var(--on-strong)}
.bolha.okk{background:var(--c);border-color:var(--c);color:var(--on-strong)}
.bolha.err{background:var(--e);border-color:var(--e);color:var(--on-strong)}
.com3{margin-top:10px;display:grid;grid-template-columns:minmax(0,1fr);gap:2px 12px;font-size:15px}
.com3 .k{font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2);padding-top:6px}
.com3 .k:first-child{padding-top:0}
@media(min-width:640px){.com3{grid-template-columns:max-content minmax(0,1fr);gap:6px 14px}.com3 .k{padding-top:2px;white-space:nowrap}}
.mec{display:inline-block;font-size:12px;font-weight:700;border:1.5px solid var(--ink);border-radius:4px;padding:0 6px;margin-left:6px;vertical-align:1px;letter-spacing:.04em}
.com3 .mec{margin-left:0;margin-right:6px}
.fecho{border-top:2px solid var(--ink);margin-top:28px;padding-top:14px}
.fecho ol,.fecho ul{margin-top:6px;padding-left:22px}
.fecho li{margin-top:6px}
.fecho .duas{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px}
@media (max-width:560px){ .fecho .duas{grid-template-columns:1fr} }
.fecho .duas>div{border:1px solid var(--rule);border-radius:8px;padding:10px 12px}
.escopo{font-size:14.5px;color:var(--ink-2);margin-top:12px;line-height:2.2}
.escopo .esc-link{display:inline-block;min-height:44px;min-width:44px;padding:0 10px;line-height:44px;text-align:center;vertical-align:middle}
.iti .itb{margin-top:6px}
.iti .itcmd{font-size:14.5px;color:var(--ink-2);margin-top:8px}
.iti .itf:focus{outline:2px solid var(--ink);outline-offset:4px;border-radius:6px}
.mecs{margin-top:8px}
.mecs .bv{grid-template-columns:minmax(0,1.6fr) 40% auto}
.estilo-da table.t td,.estilo-da table.t th{font-size:14px}
"""
sub1(css_anchor, css_new, "css")

# ---------- 2. validar(): aceitar e sanear os campos DA-v2 ----------
old = """  if(j.topicos) Object.values(j.topicos).forEach(t=>{ if(t && t.visuais!==undefined) t.visuais=Array.isArray(t.visuais)?t.visuais.filter(v=>v&&VIS_OK[v.tipo]&&VIS_OK[v.tipo](v)):[]; });"""
new = old + """
  /* v17 DA-v2: campos novos são opcionais; malformados são ignorados (a página nunca quebra por causa deles) */
  const strs=x=>Array.isArray(x)&&x.every(s=>typeof s==="string");
  if(j.topicos) Object.values(j.topicos).forEach(t=>{ if(!t) return;
    const soStr=x=>Array.isArray(x)?x.filter(s=>typeof s==="string"&&s.trim()):[]; // elemento ruim cai; os válidos ficam (QA R3)
    if(t.tarefas!==undefined){ t.tarefas=soStr(t.tarefas); if(!t.tarefas.length) delete t.tarefas; }
    if(t.fechamento!==undefined){ const f=t.fechamento; if(!f||typeof f!=="object"||!soStr(f.levar).length) delete t.fechamento; else { f.levar=soStr(f.levar); f.literalidade=soStr(f.literalidade); f.caso=soStr(f.caso); } }
    if(t.escopo!==undefined){ t.escopo=Array.isArray(t.escopo)?t.escopo.filter(e=>e&&typeof e==="object"&&typeof e.tema==="string"&&e.tema.trim()):[]; if(!t.escopo.length) delete t.escopo; } });
  j.itens.forEach(i=>{ const c=i.comentario; if(c!==undefined && !(c&&typeof c==="object"&&["decisiva","regra","correta"].every(k=>typeof c[k]==="string"&&c[k].trim()))) delete i.comentario;
    if(i.mecanismo!==undefined && !MECANISMOS[String(i.mecanismo).toUpperCase()]) delete i.mecanismo; else if(i.mecanismo) i.mecanismo=String(i.mecanismo).toUpperCase(); });
  (j.lotes||[]).forEach(l=>(l.pegadinhas||[]).forEach(p=>{ const q=p&&p.par; if(q!==undefined && !(q&&typeof q==="object"&&["a","b","muda"].every(k=>typeof q[k]==="string"&&q[k].trim()))) delete p.par; }));"""
sub1(old, new, "validar")

# MECANISMOS: tabela própria (ESTILO §4), antes de validar() — colocar junto das constantes de dados
old = "const ARR=x=>Array.isArray(x)&&x.length>0;"
new = """/* v17 DA-v2 · mecanismos de construção do item (regras/estilo_banca_DA_v1.md, seção 4). O código vem do pacote (itens[].mecanismo). */
const MECANISMOS={LIT:"paráfrase fiel da lei ou da tese",CON:"troca de conceito vizinho",SUP:"requisito, limite ou exceção suprimido ou invertido",PRA:"número, prazo ou termo trocado",
  GEN:"generalização (sempre, somente, em qualquer hipótese)",AP:"caso aplicado: fatos → hipótese → consequência",MIX:"proposições combinadas",NEG:"direção invertida (pode × não pode)",
  AUT:"troca de quem pode, deve ou responde",AMB:"âmbito trocado (a quem a norma se aplica)",TEM:"efeito no tempo trocado (ex tunc × ex nunc, marco)"};
const MOSTRAR_ESTILO_DA=true; // tela "Como a Cebraspe constrói o item" na matéria de Direito Administrativo (desligar = false)
""" + old
sub1(old, new, "mecanismos")

# ---------- 3. Renderizador do curso ----------
old = """const CAIXAS=[[/^DEFINI[ÇC](ÃO|ÕES)\\b/,"def","Definição"],[/^BASE LEGAL\\b/,"lei","Base legal"],[/^EXEMPLO PARLAMENTAR\\b|^EXEMPLO APLICADO AO LEGISLATIVO\\b/,"ex","Exemplo parlamentar"],[/^EXEMPLO\\b/,"ex","Exemplo"],[/^PEGADINHAS? (PROV[ÁA]VE(L|IS)|ADICIONAIS)\\b/,"peg","Pegadinha provável"]];"""
new = """const CAIXAS=[[/^DEFINI[ÇC](ÃO|ÕES)\\b/,"def","Definição"],[/^BASE LEGAL\\b/,"lei","Base legal"],[/^EXEMPLO PARLAMENTAR\\b|^EXEMPLO APLICADO AO LEGISLATIVO\\b/,"ex","Exemplo parlamentar"],[/^EXEMPLO\\b/,"ex","Exemplo"],[/^PEGADINHAS? (PROV[ÁA]VE(L|IS)|ADICIONAIS)\\b/,"peg","Pegadinha provável"]];
/* v17 DA-v2 (ESPEC v2, seção 3): GLOSSÁRIO (linhas "Termo: definição"), CASO (pergunta sem resposta) e RESPOSTA DO CASO (recolhida até o toque).
   Só valem como rótulo quando a linha inteira é o rótulo em caixa alta (QA R3, D2b): "### Caso prático" ou "CASO CONCRETO" continuam títulos comuns. */
const CAIXAS_V2=[[/^GLOSS[ÁA]RIO:?$/,"glo","Glossário"],[/^RESPOSTA DO CASO:?$/,"rcaso","Resposta do caso"],[/^CASO:?$/,"caso","Caso"]];
const GLO_LINHA=/^([^:—]{1,60})(?::|\\s—)\\s*(\\S.*)$/; // "Termo: definição" ou "Termo — definição"
/* v17 DA-v2: linhas A: / B: / MUDA: de uma PEGADINHA PROVÁVEL viram o quadro de par (termo A × termo B × o que muda a resposta); sem MUDA, o quadro sai só com A e B */
function par3Html(a,b,muda,inline){ const f=inline||esc; return `<div class="par3g"><span class="k">A</span><span>${f(a)}</span><span class="k">B</span><span>${f(b)}</span>${muda?`<span class="k">Muda</span><span class="muda">${f(muda)}</span>`:""}</div>`; }"""
sub1(old, new, "caixas")

# fechaCaixa: glossário em lista; pegadinha com A/B/MUDA em grade; resposta do caso recolhida; ITEM intercalado
old = """  const fechaCaixa=()=>{ if(caixa){ h+=`<div class="bx ${caixa.c}"><p class="bxl">${caixa.r}</p>${caixa.h}</div>`; caixa=null; } };"""
new = """  const fechaCaixa=()=>{ if(caixa){
    if(caixa.c==="glo"){ const li=(caixa.g||[]).map(x=>{ const m=x.match(GLO_LINHA); return m?`<li><b>${inline(m[1].trim())}:</b> ${inline(m[2])}</li>`:`<li>${inline(x)}</li>`; }).join(""); caixa.h+=li?`<ul>${li}</ul>`:""; }
    if(caixa.c==="peg"&&caixa.abm){ const a=caixa.abm; if(a.A&&a.B) caixa.h+=par3Html(a.A,a.B,a.MUDA||"",inline); else caixa.h+=["A","B","MUDA"].filter(k=>a[k]).map(k=>`<p><b>${k}:</b> ${inline(a[k])}</p>`).join(""); } // QA R3 D6: nada se perde
    if(caixa.c==="rcaso"){ h+=`<div class="bx rcaso"><details><summary>Ver a resposta do caso</summary><p class="bxl" style="margin-top:8px">${caixa.r}</p>${caixa.h}</details></div>`; caixa=null; return; }
    h+=`<div class="bx ${caixa.c}"><p class="bxl">${caixa.r}</p>${caixa.h}</div>`; caixa=null; } };"""
sub1(old, new, "fechaCaixa")

# dentro do loop de linhas: ITEM <id>, linhas do glossário, A:/B:/MUDA:
old = """    if((m=l.match(/^#{2,4}\\s+(.+)/))){ titulo(m[1]); return; }"""
new = """    if((m=s.match(/^ITEM\\s+([A-Za-z0-9][\\w.-]*)$/))){ fechaTudo(); fechaCaixa(); if(Object.hasOwn(M,m[1])) h+=`<div class="iti" data-iti="${esc(m[1])}" data-tid="${esc(tid||"")}"></div>`; return; } // v17 DA-v2: item intercalado (montado por ligaItensInline); id inexistente não renderiza nada (defeito de pacote, pego pelo checa_pacote_v2.py) — QA R3 D11/D13
    if(caixa&&caixa.c==="glo"&&GLO_LINHA.test(s)){ fechaPar(); (caixa.g=caixa.g||[]).push(s); return; }
    if(caixa&&caixa.c==="peg"&&(m=s.match(/^(A|B|MUDA):\\s*(.+)$/))){ fechaPar(); (caixa.abm=caixa.abm||{})[m[1]]=m[2]; return; }
    { const cx=CAIXAS_V2.find(c=>c[0].test(s)); if(cx){ fechaTudo(); fechaCaixa(); caixa={c:cx[1],r:cx[2],h:""}; return; } } // v17 DA-v2: rótulo exato em caixa alta (GLOSSÁRIO / CASO / RESPOSTA DO CASO)
    if((m=l.match(/^#{2,4}\\s+(.+)/))){ titulo(m[1]); return; }"""
sub1(old, new, "loop-item")

# linha em branco fecha também GLOSSÁRIO, CASO e RESPOSTA DO CASO quando já têm conteúdo (QA R3 D2): o parágrafo seguinte volta ao texto corrido
old = """    if(!s){ fechaPar(); fechaLista(); fechaTab(); fechaQuadro(); if(caixa&&(caixa.c==="def"||caixa.c==="lei")&&caixa.h.replace(/<p class="bxs">.*?<\\/p>/,"").trim()) fechaCaixa(); return; }"""
new = """    if(!s){ fechaPar(); fechaLista(); fechaTab(); fechaQuadro(); if(caixa&&(caixa.c==="def"||caixa.c==="lei")&&caixa.h.replace(/<p class="bxs">.*?<\\/p>/,"").trim()) fechaCaixa();
      if(caixa&&((caixa.c==="glo"&&(caixa.g||[]).length)||((caixa.c==="caso"||caixa.c==="rcaso")&&caixa.h.trim()))) fechaCaixa(); return; } // v17 DA-v2 (QA R3 D2)"""
sub1(old, new, "linha-em-branco")

# ---------- 4. vCurso: tarefas, fechamento, escopo, pegadinhas com par, itens intercalados ----------
old = """  const PEG=p=>`<div class="bx peg"><p class="bxl">Pegadinha${rotuloPeg(p)&&semAcento(rotuloPeg(p))!==semAcento(o.nome)?" · "+esc(rotuloPeg(p)):""}</p><p>${esc(limpaTop(p.texto,o.id))}</p></div>`;"""
new = """  const PEG=p=>`<div class="bx peg"><p class="bxl">Pegadinha${rotuloPeg(p)&&semAcento(rotuloPeg(p))!==semAcento(o.nome)?" · "+esc(rotuloPeg(p)):""}</p>${p.par?par3Html(p.par.a,p.par.b,p.par.muda):""}<p>${esc(limpaTop(p.texto,o.id))}</p></div>`;
  /* v17 DA-v2: tarefas na abertura; fechamento (o que levar, literalidade × caso, mapa de chegada repetido) e escopo no fim */
  const tarefas=(ex.tarefas||[]).length?`<div class="tarefas"><p class="eyebrow up">O que você vai conseguir fazer</p><ol>${ex.tarefas.map(x=>`<li>${esc(x)}</li>`).join("")}</ol></div>`:"";
  const mapa=(ex.visuais||[]).find(v=>v&&["esquema","linha","fluxo","compare"].includes(v.tipo)); // mapa de chegada (ESPEC §2): só esquema, linha, fluxo ou compare (QA R3 D7)
  const escopoH=(ex.escopo||[]).length?`<p class="escopo"><b>Fica para outro tópico:</b> ${ex.escopo.map(e=>`${esc(e.tema)}${e.onde&&tp(e.onde)&&tp(e.onde).temCurso?` <button class="link esc-link" data-curso="${esc(e.onde)}" aria-label="abrir o tópico ${esc(curtoId(e.onde))}">(${esc(curtoId(e.onde))})</button>`:e.onde?` (${esc(curtoId(String(e.onde)))})`:""}`).join("; ")}.</p>`:"";
  const fecho=(ex.fechamento||escopoH)?`<section class="sec fecho" id="fechamento">${ex.fechamento?`<h2 class="sech">O que levar deste tópico</h2><ol>${ex.fechamento.levar.map(x=>`<li>${esc(x)}</li>`).join("")}</ol>
     ${(ex.fechamento.literalidade.length||ex.fechamento.caso.length)?`<div class="duas">${ex.fechamento.literalidade.length?`<div><p class="eyebrow up">A banca cobra pela letra da lei</p><ul>${ex.fechamento.literalidade.map(x=>`<li>${esc(x)}</li>`).join("")}</ul></div>`:""}${ex.fechamento.caso.length?`<div><p class="eyebrow up">A banca cobra por situação</p><ul>${ex.fechamento.caso.map(x=>`<li>${esc(x)}</li>`).join("")}</ul></div>`:""}</div>`:""}
     ${mapa?`<p class="eyebrow up" style="margin-top:14px">O que você já sabe</p>${(()=>{ try{ return visual(Object.assign({},mapa,{titulo:mapa.titulo||""})); }catch(e){ return ""; } })()}`:""}`:""}
     ${escopoH}</section>`:""; // escopo aparece mesmo sem fechamento (QA R3 D8)"""
sub1(old, new, "PEG")

old = """   ${em1}${vis}${secs}${pegs}
   <div id="fimCurso" class="card on stack" style="margin-top:28px"><b>Pratique este tópico</b>"""
new = """   ${tarefas}${em1}${vis}${secs}${fecho}${pegs}
   <div id="fimCurso" class="card on stack" style="margin-top:28px"><b>Pratique este tópico</b>"""
sub1(old, new, "vCurso-html")

old = """  $("#sair").onclick=()=>ir("materia",{disc:o.disc,top:o.id});
  if($("#praticar")) $("#praticar").onclick=()=>{ marcarLido(o); iniciarBloco(o.id); };"""
new = """  $("#sair").onclick=()=>ir("materia",{disc:o.disc,top:o.id});
  ligaItensInline(app()); ligaTopicos(app()); // v17 DA-v2: itens intercalados respondíveis e links do escopo
  if($("#praticar")) $("#praticar").onclick=()=>{ marcarLido(o); iniciarBloco(o.id); };"""
sub1(old, new, "vCurso-liga")

# ---------- 5. Item intercalado + comentário em 3 linhas (funções novas, antes de "/* ---------- renderizador de curso v15") ----------
old = "/* ---------- renderizador de curso v15 ---------- */"
new = """/* ---------- v17 DA-v2 · item intercalado no curso (ESPEC v2, seção 4) e comentário em três linhas (seção 5) ---------- */
function mecChip(it){ const m=it&&it.mecanismo; return m&&MECANISMOS[m]?`<span class="mec" title="${esc(MECANISMOS[m])}" aria-label="mecanismo ${m}: ${esc(MECANISMOS[m])}">${m}</span>`:""; }
/* Comentário do item: três linhas quando o pacote traz `comentario`; senão, a justificativa corrida (lotes antigos). */
function comentarioHtml(it){
  const c=it.comentario;
  /* adendo v2.1: `decisiva` começa pelo código do mecanismo; com o chip ao lado, o código não se repete no texto */
  if(c){ const dec=String(c.decisiva||"").replace(/^([A-Z]{2,3})\\s*[:—–-]\\s*/,(m0,cod)=>cod===it.mecanismo?"":m0).trim(); // QA R3 D16: literal de regex (não string)
  return `<div class="com3"><span class="k">Palavra decisiva</span><span>${mecChip(it)}${esc(dec)}</span><span class="k">Regra</span><span>${esc(c.regra)}</span><span class="k">${it.gabarito==="E"?"Versão correta":"O que o tornaria errado"}</span><span>${esc(c.correta)}</span></div>`; }
  return `<p class="just">${justTexto(it)}${mecChip(it)}</p>`;
}
function justTexto(it){ return it.justificativa?esc(limpaTop(it.justificativa,it.itemEdital)):"Item oficial da Cebraspe; gabarito definitivo da banca."; }
/* Correção item a item (resultado): sem `comentario`, a linha é exatamente a da v17 (justificativa + "tópico X" no mesmo parágrafo, QA R3 D10); com `comentario`, as três linhas e depois a linha do tópico */
function correcaoHtml(it,extra){ return it.comentario?`${comentarioHtml(it)}<p class="just"><span class="xs">${extra}</span></p>`:`<p class="just">${justTexto(it)}${mecChip(it)} <span class="xs">${extra}</span></p>`; }
/* D-V17-1-INLINE (Fundador, 24/10): o item respondido dentro do curso é só aprendizado — fica em S.cursoResp (próprio registro),
   fora de S.resp: não entra na nota do tópico, no caderno de erros, em "Onde você erra" nem nas recomendações. Só persiste o estado da bolha. */
function respostaInline(id){ S.cursoResp=Array.isArray(S.cursoResp)?S.cursoResp:[]; return S.cursoResp.slice().reverse().find(r=>r.id===id)||null; }
function ligaItensInline(raiz){
  (raiz||app()).querySelectorAll(".iti[data-iti]").forEach(div=>{ const id=div.dataset.iti; const it=Object.hasOwn(M,id)?M[id]:null; if(!it){ div.remove(); return; } // QA R3 D11
    const feito=respostaInline(it.id); const cmd=it.comando||"Julgue o item a seguir."; const tb=(it.textoBase&&it.textoBase!=="nenhum")?it.textoBase:"";
    /* ESPEC §4: texto-base (quando houver), comando, enunciado, C/E (QA R3 D1) */
    div.innerHTML=`<p class="itc">Responda antes de seguir · ${fonteItem(it)}</p>${tb?`<div class="textobase itb">${esc(tb)}</div>`:""}<p class="itcmd">${esc(cmd)}</p><p class="ite">${esc(it.enunciado)}</p>
      <div class="ce"><button class="bolha sm" data-v="C" aria-label="Marcar Certo">C</button><button class="bolha sm" data-v="E" aria-label="Marcar Errado">E</button></div>
      <div class="itf" hidden role="status" aria-live="polite" tabindex="-1"></div>`;
    const mostrar=(r,gravar)=>{ const ok=r===it.gabarito; const f=div.querySelector(".itf"); f.hidden=false;
      f.innerHTML=`<p style="margin-top:10px"><span class="${ok?"ok":"er"}"><b>${ok?"Certo.":"Errado."}</b></span> Gabarito <span class="gab">${it.gabarito}</span>${r?` · você marcou ${r}`:""}.</p>${comentarioHtml(it)}${it.mecanismo&&MECANISMOS[it.mecanismo]?`<p class="xs muted" style="margin-top:6px">Mecanismo ${it.mecanismo}: ${esc(MECANISMOS[it.mecanismo])}. Procure a troca de vizinho e a condição que falta; palavras absolutas pedem atenção, não resposta automática.</p>`:""}`;
      div.querySelectorAll(".bolha").forEach(b=>{ b.disabled=true; if(b.dataset.v===r) b.classList.add(ok?"okk":"err"); if(!ok&&b.dataset.v===it.gabarito) b.classList.add("okk"); });
      if(gravar){ S.cursoResp=Array.isArray(S.cursoResp)?S.cursoResp:[]; S.cursoResp.push({id:it.id,tp:it.itemEdital,st:ok?"c":"e",t:Date.now()}); if(S.cursoResp.length>5000) S.cursoResp=S.cursoResp.slice(-5000); ev("item_curso_respondido",{id:it.id,ok,topico:div.dataset.tid||null}); salvar(); f.focus({preventScroll:true}); } }; // QA R3 D14: foco e aria-live no feedback
    if(feito){ mostrar(feito.st==="c"?it.gabarito:(it.gabarito==="C"?"E":"C"),false); return; }
    div.querySelectorAll(".bolha").forEach(b=>b.onclick=()=>mostrar(b.dataset.v,true));
  });
}
/* ESPEC §4: o item intercalado não entra no bloco de verificação do mesmo tópico (QA R3 D4) nem no treino por mecanismo */
function idsInline(tid){ const o=tp(tid); const s=new Set(); if(!o) return s; o.secoes.forEach(x=>String(x.corpo||"").split("\\n").forEach(l=>{ const m=l.trim().match(/^ITEM\\s+([A-Za-z0-9][\\w.-]*)$/); if(m&&Object.hasOwn(M,m[1])) s.add(m[1]); })); return s; }
function ehInline(it){ return it&&idsInline(it.itemEdital).has(it.id); }
/* ---------- v17 DA-v2 · desempenho por mecanismo (a partir das respostas já registradas) ---------- */
function errosPorMecanismo(discId,n){ n=n||300; const ids=new Set(topicosDe(discId).map(o=>o.id)); const cont={}, itens={}; let tot=0;
  /* últimas n respostas DESTA matéria (QA R3 D5), contando respostas em `cont` e itens distintos errados em `itens` */
  (S.resp||[]).filter(r=>ids.has(r.tp)).slice(-n).forEach(r=>{ const it=Object.hasOwn(M,r.id)?M[r.id]:null; if(!it||!it.mecanismo||r.st==="b") return; const k=it.mecanismo; cont[k]=cont[k]||{c:0,e:0}; cont[k][r.st==="c"?"c":"e"]++; tot++; if(r.st==="e"){ (itens[k]=itens[k]||new Set()).add(r.id); } });
  return {cont,itens,tot}; }
function mecanismosHtml(d){ const {cont,tot}=errosPorMecanismo(d.id); const ks=Object.keys(cont).filter(k=>cont[k].e).sort((a,b)=>cont[b].e-cont[a].e); if(!tot||!ks.length) return "";
  const mx=Math.max(...ks.map(k=>cont[k].e));
  return `<details class="card" style="margin-top:8px"><summary style="cursor:pointer;min-height:32px"><b>Onde você erra</b> <span class="small muted">· como a banca construiu os itens que você errou</span></summary>
    <div class="mecs barrasv" style="margin-top:8px">${ks.map(k=>`<div class="bv"><span><b>${k}</b> <span class="small muted">${esc(MECANISMOS[k])}</span></span><span class="bvb"><i style="width:${Math.round(100*cont[k].e/mx)}%"></i></span><span class="num">${cont[k].e} de ${cont[k].c+cont[k].e}</span></div>`).join("")}</div>
    <p class="xs muted" style="margin-top:8px">Erros por mecanismo nas suas últimas respostas desta matéria (itens com mecanismo registrado).</p>
    <div class="row2" style="margin-top:8px">${ks.slice(0,2).map(k=>`<button class="btn" data-mec="${k}" data-mecd="${esc(d.id)}">Treinar ${k}</button>`).join("")}</div></details>`; }
function iniciarTreinoMecanismo(discId,mec){
  const ids=new Set(topicosDe(discId).map(o=>o.id)); const ult={}; S.resp.forEach(r=>ult[r.id]=r);
  const its=P.itens.filter(i=>ids.has(i.itemEdital)&&i.mecanismo===mec&&!i.volatil);
  const err=its.filter(i=>ult[i.id]&&ult[i.id].st==="e"), ined=embaralhar(its.filter(i=>!ult[i.id])), resto=its.filter(i=>ult[i.id]&&ult[i.id].st!=="e");
  const ordem=[...err,...ined,...resto].slice(0,BLOCO).map(i=>i.id); if(!ordem.length) return toast("Ainda não há itens desse mecanismo para treinar.");
  prova={tipo:"mec",ref:discId+"|"+mec,nome:`Treino · ${mec} · ${esc(MECANISMOS[mec]||"")}`,ordem,comandos:{},resp:{},i:0,inicio:Date.now(),cron:false};
  ev("treino_mecanismo_iniciado",{disc:discId,mec,n:ordem.length}); ir("prova");
}
/* ---------- v17 DA-v2 · "Como a Cebraspe constrói o item" (estatística do Projeto, regras/estilo_banca_DA_v1.md; aproximada) ---------- */
/* Proporções do ESTILO §4 (corpus 2025, ±3 pontos): LIT 1% E; CON 83% E; SUP 65%; GEN 96%; NEG 100% (n=37); PRA 59%, AUT 72%, AMB 65%, TEM 57%; AP 26% E. Texto corrigido na QA R3 (D3): a recíproca "item certo = literal" não vale (LIT é cerca de 6 em 10 dos Certos). */
const ESTILO_DA=[["LIT","paráfrase fiel da lei ou da tese","quase sempre Certo"],["CON","troca de conceito vizinho (anular × revogar, dispensa × inexigibilidade)","na maioria Errado"],["SUP","requisito, limite ou exceção suprimido ou invertido","em geral Errado"],["GEN","sempre, somente, em qualquer hipótese","quase sempre Errado"],["NEG","pode × não pode, dever × faculdade","quase sempre Errado (amostra pequena)"],["PRA / AUT / AMB / TEM","número, sujeito, âmbito ou efeito no tempo trocados","tende a Errado"],["AP","caso aplicado, com a consequência","tende a Certo; raro"]];
function estiloDaHtml(){ if(!MOSTRAR_ESTILO_DA) return "";
  return `<details class="card estilo-da" style="margin-top:8px"><summary style="cursor:pointer;min-height:32px"><b>Como a Cebraspe constrói o item</b> <span class="small muted">· leia antes de responder</span></summary>
   <div class="stack" style="margin-top:8px"><p class="small">Quando o item reescreve a lei ou a tese com fidelidade, quase sempre é Certo. O item errado nasce, na maioria das vezes, de uma troca: um conceito pelo vizinho, uma condição que some, uma generalização. Procure a troca e a condição que falta; palavras absolutas pedem atenção, não resposta automática.</p>
   <table class="t"><tr><th>Código</th><th>Como o item foi construído</th><th class="r">Tende a</th></tr>${ESTILO_DA.map(r=>`<tr><td><b>${r[0]}</b></td><td>${esc(r[1])}</td><td class="r small">${esc(r[2])}</td></tr>`).join("")}</table>
   <p class="xs muted">Levantamento do Projeto sobre cerca de 1.100 itens Certo/Errado de Direito Administrativo aplicados pela Cebraspe em 2025; proporções aproximadas. Em 2025, Certo e Errado vieram quase meio a meio, e só cerca de 1 item em 20 trazia situação hipotética.</p></div></details>`; }

/* ---------- renderizador de curso v15 ---------- */"""
sub1(old, new, "funcoes-novas")

# ---------- 6. Correção item a item (resultado) e caderno de erros: comentário em três linhas ----------
old = """     <p style="margin-top:6px">${esc(it.enunciado)}</p>${notaTxt(it)?`<div style="margin-top:6px">${notaHtml(it)}</div>`:""}<p class="just">${it.justificativa?esc(limpaTop(it.justificativa,it.itemEdital)):"Item oficial da Cebraspe; gabarito definitivo da banca."} <span class="xs">tópico ${esc(curtoId(it.itemEdital))}${it.aderencia==="parcial"?" · aderência parcial ao edital":""}${it.volatil?" · fato datado, reverificado em janeiro":""}${it.url&&/^https?:/.test(it.url)?` · <a href="${esc(it.url)}" target="_blank" rel="noopener">caderno oficial</a>`:""}</span></p></details>`;}).join("")}</div></div>"""
new = """     <p style="margin-top:6px">${esc(it.enunciado)}</p>${notaTxt(it)?`<div style="margin-top:6px">${notaHtml(it)}</div>`:""}${correcaoHtml(it,`tópico ${esc(curtoId(it.itemEdital))}${it.aderencia==="parcial"?" · aderência parcial ao edital":""}${it.volatil?" · fato datado, reverificado em janeiro":""}${it.url&&/^https?:/.test(it.url)?` · <a href="${esc(it.url)}" target="_blank" rel="noopener">caderno oficial</a>`:""}`)}</details>`;}).join("")}</div></div>"""
sub1(old, new, "resultado-correcao")

old = """    j.innerHTML=`<span class="${ok?"ok":"er"}">${ok?"Certo.":"Errado."}</span> Gabarito <span class="gab">${it.gabarito}</span>. ${esc(limpaTop(it.justificativa||"Item oficial da Cebraspe.",it.itemEdital))}`;"""
new = """    j.innerHTML=`<span class="${ok?"ok":"er"}">${ok?"Certo.":"Errado."}</span> Gabarito <span class="gab">${it.gabarito}</span>. ${it.comentario?"":esc(limpaTop(it.justificativa||"Item oficial da Cebraspe.",it.itemEdital))}`+(it.comentario?comentarioHtml(it):"");"""
sub1(old, new, "erros-comentario")

# ---------- 7. Resultado: treino por mecanismo volta às recomendações; sair da prova ----------
old = """  const volta=t.tipo==="rev"?"Voltar ao caderno":t.tipo==="bloco"?"Voltar à matéria":t.tipo==="teste"?"Voltar ao Painel":"Voltar aos simulados";"""
new = """  const volta=t.tipo==="rev"?"Voltar ao caderno":t.tipo==="bloco"||t.tipo==="mec"?"Voltar à matéria":t.tipo==="teste"?"Voltar ao Painel":"Voltar aos simulados";"""
sub1(old, new, "resultado-volta")
old = """   <div class="eyebrow">${esc(limpaNome(t.nome))} · ${t.total} itens${t.tipo==="sim"?` · ${min} min`:""}</div>"""
new = """   <div class="eyebrow">${esc(limpaNome(t.nome))} · ${pl(t.total,"item","itens")}${t.tipo==="sim"?` · ${min} min`:""}</div>"""
sub1(old, new, "resultado-plural")
old = """  $("#volta").onclick=()=>{ if(t.tipo==="rev") return ir("erros"); if(t.tipo==="bloco"&&tp(t.ref)) return ir("materia",{disc:tp(t.ref).disc,top:t.ref}); if(t.tipo==="teste") return ir("painel"); ir("pratica"); };"""
new = """  $("#volta").onclick=()=>{ if(t.tipo==="rev") return ir("erros"); if(t.tipo==="bloco"&&tp(t.ref)) return ir("materia",{disc:tp(t.ref).disc,top:t.ref}); if(t.tipo==="teste") return ir("painel"); if(t.tipo==="mec") return ir("materia",String(t.ref).split("|")[0]); ir("pratica"); };"""
sub1(old, new, "resultado-volta2")
old = """  $("#sair").onclick=()=>{ clearInterval(prova.timer); const t=prova.tipo, rf=prova.ref; prova=null; if(t==="bloco"&&tp(rf)) return ir("materia",{disc:tp(rf).disc,top:rf}); ir(t==="rev"?"erros":"pratica"); };"""
new = """  $("#sair").onclick=()=>{ clearInterval(prova.timer); const t=prova.tipo, rf=prova.ref; prova=null; if(t==="bloco"&&tp(rf)) return ir("materia",{disc:tp(rf).disc,top:rf}); if(t==="mec") return ir("materia",String(rf).split("|")[0]); ir(t==="rev"?"erros":"pratica"); };"""
sub1(old, new, "prova-sair")

# ---------- 8. Painel: corpo da matéria com "Onde você erra" e "Como a Cebraspe constrói o item" (só DA) ----------
old = """  return `${pend?`<button class="btn primary" data-diag="${d.id}" style="margin-bottom:6px">Fazer diagnóstico · ${dg.itens.length} itens</button>`:""}<div>${raiz.map(bloco).join("")}</div>`;
}"""
new = """  const extraDA=d.modulo==="DA"?estiloDaHtml()+mecanismosHtml(d):mecanismosHtml(d); // v17 DA-v2
  return `${pend?`<button class="btn primary" data-diag="${d.id}" style="margin-bottom:6px">Fazer diagnóstico · ${dg.itens.length} itens</button>`:""}${extraDA}<div>${raiz.map(bloco).join("")}</div>`;
}"""
sub1(old, new, "corpoMateria")
old = """  el.querySelectorAll("[data-diag]").forEach(b=>b.onclick=()=>{ const d=discById(b.dataset.diag); iniciar("D30-"+d.modulo); });
  ligaTopicos(el);"""
new = """  el.querySelectorAll("[data-diag]").forEach(b=>b.onclick=()=>{ const d=discById(b.dataset.diag); iniciar("D30-"+d.modulo); });
  el.querySelectorAll("[data-mec]").forEach(b=>b.onclick=()=>iniciarTreinoMecanismo(b.dataset.mecd,b.dataset.mec)); // v17 DA-v2
  ligaTopicos(el);"""
sub1(old, new, "ligaCorpo")

# ---------- 9. Recomendações: opção C de treino por mecanismo quando houver erros concentrados ----------
old = """  else { const C=cand.find(c=>c.o!==A.o && (!B||c.o!==B.o) && c.o.pegs.length && c.o.temCurso);"""
new = """  else { const C=cand.find(c=>c.o!==A.o && (!B||c.o!==B.o) && c.o.pegs.length && c.o.temCurso);"""
# (a opção de treino por mecanismo entra como opção D, independente do caderno — QA R3 D5)
old = """  return out;
}
function pratica(){"""
new = """  /* v17 DA-v2 (QA R3 D5): opção D quando a candidata errou 3+ itens DIFERENTES de um mesmo mecanismo numa matéria; conta itens, não respostas */
  { const melhor=DISCIPLINAS.map(d=>{ const r=errosPorMecanismo(d.id); const ks=Object.keys(r.itens||{}); const k=ks.sort((x,y)=>r.itens[y].size-r.itens[x].size)[0]; return k?{d,k,e:r.itens[k].size}:null; }).filter(Boolean).sort((a,b)=>b.e-a.e)[0];
    if(melhor&&melhor.e>=3){ const disp=P.itens.filter(i=>topicosDe(melhor.d.id).some(o=>o.id===i.itemEdital)&&i.mecanismo===melhor.k&&!i.volatil&&!ehInline(i)).length;
      out.push({op:"D",rot:"Treino por mecanismo",titulo:`Treinar ${melhor.k}: ${MECANISMOS[melhor.k]}`,por:`você errou ${melhor.e} itens diferentes construídos assim em ${curtoDisc(melhor.d)}; ${melhor.k==="LIT"?"conferir a paráfrase palavra a palavra":"reconhecer a troca"} é o que decide o item`,acao:{txt:`Treinar ${melhor.k} · ${pl(Math.min(BLOCO,disp),"item","itens")}`,go:()=>iniciarTreinoMecanismo(melhor.d.id,melhor.k)}}); } }
  return out;
}
function pratica(){"""
sub1(old, new, "recs-D")

# ---------- 9b. ESPEC §4 (QA R3 D4): item intercalado fora do bloco de verificação do tópico e da contagem de questões ----------
old = """  const extra=Object.assign({},TOPICOS_DEMO,P.topicos||{});"""
new = """  /* v17 DA-v2: ids citados em linhas `ITEM <id>` do curso de cada tópico não contam como questões de verificação (ESPEC §4) */
  const inl={}; Object.entries(secoes).forEach(([tid,ss])=>{ const s=new Set(); ss.forEach(x=>String(x.corpo||"").split("\\n").forEach(l=>{ const m=l.trim().match(/^ITEM\\s+([A-Za-z0-9][\\w.-]*)$/); if(m&&Object.hasOwn(M,m[1])&&M[m[1]].itemEdital===tid) s.add(m[1]); })); inl[tid]=s; });
  const extra=Object.assign({},TOPICOS_DEMO,P.topicos||{});"""
sub1(old, new, "construir-inline")
old = """      n:nItens[e.id]||0,secoes:secoes[e.id]||[],pegs:pegs[e.id]||[],resumoLotes:resumos[e.id]||[],extra:extra[e.id]||null};"""
new = """      n:Math.max(0,(nItens[e.id]||0)-((inl[e.id]||new Set()).size)),nInline:(inl[e.id]||new Set()).size,secoes:secoes[e.id]||[],pegs:pegs[e.id]||[],resumoLotes:resumos[e.id]||[],extra:extra[e.id]||null};"""
sub1(old, new, "construir-n")
old = """  const its=P.itens.filter(i=>i.itemEdital===tid); const ult={}; S.resp.forEach(r=>{ if(r.tp===tid) ult[r.id]=r; });"""
new = """  const inl=idsInline(tid); const its=P.itens.filter(i=>i.itemEdital===tid&&!inl.has(i.id)); const ult={}; S.resp.forEach(r=>{ if(r.tp===tid) ult[r.id]=r; }); // ESPEC §4: sem o item intercalado"""
sub1(old, new, "montarBloco")
old = """  const its=P.itens.filter(i=>ids.has(i.itemEdital)&&i.mecanismo===mec&&!i.volatil);"""
new = """  const its=P.itens.filter(i=>ids.has(i.itemEdital)&&i.mecanismo===mec&&!i.volatil&&!ehInline(i));"""
sub1(old, new, "treino-inline")

# ---------- 9c. Resumo usa o mesmo renderizador: linha ITEM não deixa caixa vazia (QA R3 D13) ----------
old = """   <div class="curso">${mdCurso2(paraResumo(corpo),ehDA(its[0])?its[0]:undefined)}</div>"""
new = """   <div class="curso">${mdCurso2(paraResumo(corpo),ehDA(its[0])?its[0]:undefined).replace(/<div class="iti"[^>]*><\\/div>/g,"")}</div>"""
sub1(old, new, "resumo-iti")

# ---------- 9d. Nota do tópico (D-V17-NOTA-TOPICO): o divisor conta só as questões de verificação — sem os itens intercalados (QA R4, N1) ----------
old = """function divTopico(id){ if(_divP!==P){ _divP=P; _divM={}; const v={}; P.itens.forEach(i=>{ const t=i.itemEdital; (v[t]=v[t]||new Set()).add(i.id); }); Object.keys(v).forEach(t=>_divM[t]=v[t].size); }"""
new = """function divTopico(id){ if(_divP!==P){ _divP=P; _divM={}; const v={}, ic={}; const inl=t=>ic[t]||(ic[t]=(T&&T.top&&T.top[t]&&T.top[t].nInline)?idsInline(t):new Set()); P.itens.forEach(i=>{ const t=i.itemEdital; if(inl(t).has(i.id)) return; (v[t]=v[t]||new Set()).add(i.id); }); Object.keys(v).forEach(t=>_divM[t]=v[t].size); } // v17.1: intercalados fora do divisor (ESPEC §4; QA R4 N1)"""
sub1(old, new, "divTopico")

# ---------- 10. versão ----------
sub1('const VERSAO_APP="v17";', 'const VERSAO_APP="v17.1";', "versao")

open(dst, "w", encoding="utf-8").write(h)
print(f"OK: {dst} · {n0} → {len(h)} bytes")
