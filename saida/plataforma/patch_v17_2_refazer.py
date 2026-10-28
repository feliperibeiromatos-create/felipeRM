#!/usr/bin/env python3
"""patch_v17_2_refazer.py — Plataforma v17.2, parte 2 (D-INLINE-REFAZER, Fundador 25/10/2026; T-140).
Botão "Refazer" no item intercalado do curso depois da resposta: limpa a bolha e aceita nova resposta; cada resposta vira um registro
novo em S.cursoResp (o anterior fica); nada entra em S.resp, no caderno de erros, na nota nem no painel de mecanismos (D-V17-1-INLINE).
Aplica-se DEPOIS de patch_v17_2_janela20.py (ou sobre o template v17.1 puro; as âncoras são as mesmas).
Uso: python3 -I patch_v17_2_refazer.py <template_entrada> <template_saida>
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

# 1. CSS do botão pequeno
sub1(""".iti .bolha.sm{width:56px;height:56px;font-size:24px}""",
     """.iti .bolha.sm{width:56px;height:56px;font-size:24px}
.iti .btn.refazer{min-height:44px;font-size:15px;padding:0 14px;margin-top:10px;display:inline-flex} /* v17.2 (D-INLINE-REFAZER, T-140): refazer o item intercalado */""",
     "CSS refazer")

# 2. comentário de cabeçalho
sub1("""   fora de S.resp: não entra na nota do tópico, no caderno de erros, em "Onde você erra" nem nas recomendações. Só persiste o estado da bolha. */""",
     """   fora de S.resp: não entra na nota do tópico, no caderno de erros, em "Onde você erra" nem nas recomendações. Só persiste o estado da bolha.
   v17.2 (D-INLINE-REFAZER, T-140): depois da resposta, o botão "Refazer" rearma o item; a nova resposta vira outro registro em S.cursoResp (o anterior fica). */""",
     "comentário")

# 3. mostrar(): botão Refazer no feedback + função rearmar
sub1("""      div.querySelectorAll(".bolha").forEach(b=>{ b.disabled=true; if(b.dataset.v===r) b.classList.add(ok?"okk":"err"); if(!ok&&b.dataset.v===it.gabarito) b.classList.add("okk"); });""",
     """      f.insertAdjacentHTML("beforeend",`<p><button class="btn refazer" data-refazer aria-label="Refazer este item">Refazer</button></p>`); // v17.2 (D-INLINE-REFAZER)
      div.querySelectorAll(".bolha").forEach(b=>{ b.disabled=true; if(b.dataset.v===r) b.classList.add(ok?"okk":"err"); if(!ok&&b.dataset.v===it.gabarito) b.classList.add("okk"); });
      div.querySelector("[data-refazer]").onclick=()=>{ f.hidden=true; f.innerHTML=""; div.querySelectorAll(".bolha").forEach(b=>{ b.disabled=false; b.classList.remove("okk","err"); b.onclick=()=>mostrar(b.dataset.v,true); }); ev("item_curso_refazer",{id:it.id,topico:div.dataset.tid||null}); div.querySelector(".bolha").focus({preventScroll:true}); }; // rearma: nada é apagado de S.cursoResp""",
     "refazer")

open(dst, "w", encoding="utf-8", newline="\n").write(h)
print(f"OK: {N} substituições · {dst}")
