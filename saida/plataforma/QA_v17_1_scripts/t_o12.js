const { chromium, abrir } = require('./lib.js');
(async()=>{ const b=await chromium.launch(); const out={};
for (const m of [{nome:'cel',vp:{width:390,height:844},escuro:false},{nome:'desk',vp:{width:1280,height:900},escuro:true}]) {
 const {page,erros}=await abrir(b,'/home/claude/plat/plataforma_v17_1_DAv2_previa.html',m); await page.evaluate(()=>ir('curso','P1-DA-3.4'));
 const esc=page.locator('.escopo'); await esc.scrollIntoViewIfNeeded(); await esc.screenshot({path:`/home/claude/plat/qa_r5/${m.nome}_O2_escopo.png`});
 const o2=await page.evaluate(()=>({txt:document.querySelector('.escopo').innerText, btns:[...document.querySelectorAll('.escopo button')].map(x=>{const r=x.getBoundingClientRect();return [x.textContent,Math.round(r.width),Math.round(r.height)]})}));
 await page.locator('.iti[data-iti="DX-01"] .bolha[data-v="C"]').focus(); await page.keyboard.press('Enter'); await page.waitForTimeout(100);
 const it=page.locator('.iti[data-iti="DX-01"]'); await it.scrollIntoViewIfNeeded(); await it.screenshot({path:`/home/claude/plat/qa_r5/${m.nome}_O1_foco_feedback.png`});
 const o1=await page.evaluate(()=>{const a=document.activeElement,s=getComputedStyle(a);return {el:a.className,outline:s.outlineStyle+' '+s.outlineWidth+' '+s.outlineColor,offset:s.outlineOffset};});
 out[m.nome]={o1,o2,erros}; await page.context().close(); }
console.log(JSON.stringify(out)); await b.close(); })();
