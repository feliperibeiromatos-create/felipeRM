const { chromium, abrir } = require('./lib.js');
(async()=>{ const b=await chromium.launch(); const {page,erros}=await abrir(b,'/home/claude/plat/qa_r5/mec5.html');
const r=await page.evaluate(()=>{ iniciarBloco('P1-DA-3.4'); prova.ordem=['DX-21','DX-22','DX-23']; prova.ordem.forEach(id=>prova.resp[id]='E'); entregar(); ir('recomendacoes');
 const card=[...document.querySelectorAll('.card.rec')].map(c=>c.innerText.replace(/\s+/g,' ')).find(c=>/Opção D/i.test(c));
 const f=(dec,mec)=>{ const d=document.createElement('div'); d.innerHTML=comentarioHtml({gabarito:'E',mecanismo:mec,comentario:{decisiva:dec,regra:'r',correta:'c'}}); return d.querySelector('.com3 span:nth-child(2)').textContent; };
 return {card, neg:f("NEG — 'vedada' onde a lei admite",'NEG'), negHifen:f('NEG-vedada','NEG'), outro:f('CON: troca','SUP'), sem:f('LIT: x',undefined), enDash:f('AP – x','AP')}; });
console.log(JSON.stringify(r), erros); await b.close(); })();
