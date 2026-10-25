const { chromium, abrir } = require('./lib.js');
(async()=>{ const b=await chromium.launch(); const out=[];
for (const [w,esc] of [[360,false],[360,true],[640,false]]) { const {page,erros}=await abrir(b,'/home/claude/plat/plataforma_v17_1_DAv2_previa.html',{vp:{width:w,height:800},escuro:esc});
 await page.evaluate(()=>ir('curso','P1-DA-3.4')); await page.locator('.iti[data-iti="DX-01"] .bolha[data-v="E"]').click();
 const foco=await page.evaluate(()=>{const a=document.activeElement,s=getComputedStyle(a);return a.className+' outline:'+s.outlineStyle+' '+s.outlineWidth+' shadow:'+s.boxShadow;});
 await page.evaluate(()=>document.querySelectorAll('details').forEach(d=>d.open=true));
 const h1=await page.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
 const r=await page.evaluate(()=>{ iniciarBloco('P1-DA-3.4'); prova.ordem=['DX-02','DX-05','DX-06']; prova.ordem.forEach(id=>prova.resp[id]='C'); entregar(); return {com3:document.querySelectorAll('details.corr .com3').length, topico:[...document.querySelectorAll('details.corr p.just .xs')].length}; });
 const r2=await page.evaluate(()=>{ ir('erros'); const c=document.querySelector('.par[data-id="DX-02"]'); c.querySelector('.bolha[data-v="E"]').click(); return /com3/.test(c.querySelector('.just').innerHTML); });
 const h2=await page.evaluate(()=>{ UI.mat.clear(); ir('materia',{disc:'cd26-c11/p1/adm'}); document.querySelectorAll('details').forEach(d=>d.open=true); return document.documentElement.scrollWidth-document.documentElement.clientWidth; });
 out.push({w,esc,foco,hCurso:h1,hMateria:h2,resultado:r,caderno:r2,erros}); await page.context().close(); }
console.log(JSON.stringify(out,null,0)); await b.close(); })();
