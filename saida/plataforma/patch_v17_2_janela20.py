#!/usr/bin/env python3
"""patch_v17_2_janela20.py — Plataforma v17.2 (D-V17-2-JANELA-20, Fundador 26/10/2026).
Aplica ao template v17.1 as mudanças da ESPEC claude/ESPEC_plataforma_v17_2_janela20_2026-10-26.md, seção 2:
janela da nota do tópico 30 → 20; divisor = menor entre 20 e as questões distintas do tópico (sem intercalados);
"nota completa" / "n de k respondidas" na interface; aviso de uma visita; textos. Nada do pacote muda; nada da v17.1 é removido.
R2.1 (26/10, após QA R2 opus, N2 e N3): comentário e texto oculto para leitor de tela no "n/k" (.vh) no lugar do aria-label. R2 (26/10, após QA R1 opus): status "n de k questões" (brancos contam, como na janela); status também na linha do tópico do Painel (D1);
aviso só quando algum % exibido muda de fato (D4); "Falta 1" (D5); status sem repetição no pós-bloco (D7); comentários (D8); texto do aviso "até 20" (D10).
Uso: python3 -I patch_v17_2_janela20.py <template_v17_1_entrada> <template_v17_2_saida>
Cada âncora precisa existir exatamente uma vez; senão o script para sem gravar (verificável por diff).
"""
import sys
src, dst = sys.argv[1], sys.argv[2]
h = open(src, encoding="utf-8").read()
n0 = len(h)
N = 0

def sub1(old, new, label):
    global h, N
    c = h.count(old)
    if c != 1:
        sys.exit(f"ERRO: âncora '{label}' encontrada {c} vezes (esperado 1)")
    h = h.replace(old, new)
    N += 1

# 1. versão
sub1('const VERSAO_APP="v17.1";', 'const VERSAO_APP="v17.2";', "VERSAO_APP")

# 2. janela e comentário
sub1('const JANELA=30, BLOCO=10;', 'const JANELA=20, BLOCO=10;', "JANELA")
sub1("/* DECISÃO DO FELIPE (18/10/2026): só questões distintas entram na janela de 30.", "/* DECISÃO DO FELIPE (18/10/2026): só questões distintas entram na janela (30 até a v17.1; 20 desde a v17.2).", "comentário 18/10")
sub1("// D-V17-NOTA-TOPICO: menor entre 30 e as questões distintas do tópico no banco", "// D-V17-NOTA-TOPICO: menor entre JANELA (30 até a v17.1; 20 desde a v17.2, D-V17-2-JANELA-20) e as questões distintas do tópico no banco", "comentário divTopico")
sub1("""   v17 (D-V17-NOTA-TOPICO): o divisor da nota do tópico é o menor entre JANELA e o nº de questões distintas do tópico no banco; assim quem acerta tudo vê 100%. */""",
     """   v17 (D-V17-NOTA-TOPICO): o divisor da nota do tópico é o menor entre JANELA e o nº de questões distintas do tópico no banco; assim quem acerta tudo vê 100%.
   v17.2 (D-V17-2-JANELA-20, Fundador 26/10/2026): JANELA passa de 30 para 20; a nota fica COMPLETA com divTopico(tid) respostas distintas (20, ou todas as do tópico se houver menos);
   antes disso a interface mostra "n de k questões" (vistas, inclusive em branco). A rodada continua de BLOCO=10 (nunca vistas → erradas → demais). O diagnóstico de entrada (30 por matéria) não muda. */""",
     "comentário JANELA")

# 3. notaTopico: nota e completa pelo divisor do tópico
sub1("""  return {n,c,e,b:n-c-e,nota:n>=JANELA?c-e:null,rep:CONTA_REPETIDAS&&new Set(w.map(r=>r.id)).size<n}; }""",
     """  const k=divTopico(tid); return {n,c,e,b:n-c-e,k,completa:n>=k,nota:n>=k?c-e:null,rep:CONTA_REPETIDAS&&new Set(w.map(r=>r.id)).size<n}; } // v17.2: nota completa com k = divTopico""",
     "notaTopico")

# 4. notaHtmlTop + status da nota
sub1("""function notaHtmlTop(tid){ return `<b class="num">${pctTxt(pctTopico(tp(tid)))}</b>`; } // v17: desempenho em % (sem "em formação")""",
     """function statusNota(tid){ const nt=notaTopico(tid); return nt.completa?"nota completa":`${nt.n} de ${nt.k} questões`; } // v17.2 (D-V17-2-JANELA-20): conta as vistas, inclusive em branco (valem 0), como a janela
function notaHtmlTop(tid){ return `<b class="num">${pctTxt(pctTopico(tp(tid)))}</b> <span class="xs muted num" data-status-nota="${esc(tid)}">(${statusNota(tid)})</span>`; } // v17: desempenho em %; v17.2: + status""",
     "notaHtmlTop")

# 5. texto de ajuda da apresentação
sub1("""na regra da prova: certo +1, errado −1, em branco 0. Começa em 0% e sobe quando você aprende.</p>""",
     """na regra da prova: certo +1, errado −1, em branco 0. Começa em 0% e sobe quando você aprende. A nota fica completa com ${JANELA} questões diferentes respondidas (ou todas as do tópico, se houver menos); até lá você vê quantas faltam. Questão deixada em branco conta na contagem e vale 0.</p>""",
     "ajuda apresentação")

# 6. linha do tópico (fim do curso): faltam x
sub1("""primeiro as que você nunca viu, depois as que errou.${notaTopico(o.id).n?" Desempenho no tópico: "+notaHtmlTop(o.id):""}`""",
     """primeiro as que você nunca viu, depois as que errou.${notaTopico(o.id).n?" Desempenho no tópico: "+notaHtmlTop(o.id)+"."+(notaTopico(o.id).completa?"":` ${notaTopico(o.id).k-notaTopico(o.id).n===1?"Falta 1 questão":"Faltam "+(notaTopico(o.id).k-notaTopico(o.id).n)+" questões"} para a nota completa.`):""}`""",
     "fim do curso")

# 7. pós-bloco
sub1("""Calculado sobre até ${JANELA} questões diferentes respondidas mais recentemente (ou todas as do tópico, se houver menos); as que faltam contam como em branco.</p>""",
     """Calculado sobre até ${JANELA} questões diferentes respondidas mais recentemente (ou todas as do tópico, se houver menos); as que faltam contam como em branco.</p>""",
     "pós-bloco")

# 8. porque(): /k
sub1("""  else if(nt.nota!==null) a.push(`nota recente ${sinal(nt.nota)}/${JANELA}`);""",
     """  else if(nt.nota!==null) a.push(`nota recente ${sinal(nt.nota)}/${nt.k}`); // v17.2: divisor do tópico""",
     "porque")

# 9. aviso de uma visita no painel (só quando algum tópico tem mais de JANELA respostas distintas)
sub1("""  const nf=notaFinal();
  app().innerHTML=`${topo()}<div class="stack l">
   <div><h1>Painel</h1>""",
     """  const nf=notaFinal();
  const avisoV172=(()=>{ if(S.avisoV172) return ""; const ids=new Set(); const porTop={}; (S.resp||[]).forEach(r=>{ if(!ids.has(r.tp+"|"+r.id)){ ids.add(r.tp+"|"+r.id); porTop[r.tp]=(porTop[r.tp]||0)+1; } });
    const antiga=t=>{ let rs=S.resp.filter(r=>r.tp===t); const v=new Set(); rs=rs.slice().reverse().filter(r=>!v.has(r.id)&&v.add(r.id)).reverse().slice(-30); divTopico(t); const d=Math.max(1,Math.min(30,_divM[t]||0)); return pctTxt((rs.filter(r=>r.st==="c").length-rs.filter(r=>r.st==="e").length)/d); }; // regra da v17.1 (janela 30)
    const afeta=Object.keys(porTop).some(t=>tp(t)&&antiga(t)!==pctTxt(pctTopico(tp(t)))); S.avisoV172=true; salvar(); // uma visita (ESPEC v17.2 §3): só se algum % exibido mudou (QA R1 D4)
    return afeta?`<p class="hl small" id="avisoV172">A partir desta versão, a nota de cada tópico é calculada sobre até ${JANELA} questões diferentes (antes eram 30): as ${JANELA} mais recentes, com as que faltam valendo 0. Por isso a nota de alguns tópicos mudou.</p>`:""; })();
  app().innerHTML=`${topo()}<div class="stack l">
   <div><h1>Painel</h1>""",
     "aviso painel")
sub1("""   <button class="btn primary big" id="cont" style="text-align:left">""",
     """   ${avisoV172}<button class="btn primary big" id="cont" style="text-align:left">""",
     "aviso painel (inserção)")

# 10. D1 (QA R1): status compacto na linha do tópico do Painel (só quando há respostas e a nota ainda não está completa)
sub1("""<span class="pc">${pctTxt(pctTopico(o))}</span><span class="chev" aria-hidden="true">▾</span></button>""",
     """<span class="pc">${pctTxt(pctTopico(o))}${(()=>{ const nt=notaTopico(o.id); return nt.n&&!nt.completa?`<span class="st"><span aria-hidden="true">${nt.n}/${nt.k}</span><span class="vh">${nt.n} de ${nt.k} questões</span></span>`:""; })()}</span><span class="chev" aria-hidden="true">▾</span></button>""",
     "linha do tópico (Painel)")
sub1(""".top-t .pc{text-align:right;font-size:15px}""",
     """.top-t .pc{text-align:right;font-size:15px}
.top-t .pc .st{display:block;font-size:11.5px;font-weight:400;color:var(--ink-2);line-height:1.2;margin-top:1px} /* v17.2: status "n/k" sob o % (cabe na coluna de 52/48 px) */
.vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap} /* v17.2: texto só para leitor de tela (QA R2 N3) */""",
     "CSS status linha do tópico")

open(dst, "w", encoding="utf-8", newline="\n").write(h)
print(f"OK: {N} substituições · {n0} → {len(h)} bytes · {dst}")
