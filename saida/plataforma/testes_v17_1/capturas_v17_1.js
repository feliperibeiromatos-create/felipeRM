const { chromium } = require('playwright'); const path=require('path');
const ESTADO = { v: 1, boasVindas: true, concurso: 'cd26-c11', escolha: { DA: 'zero' }, escolhaDisc: { 'cd26-c11/p1/adm': 'zero' }, tentativas: [], erros: {}, saidas: [], lote: {}, disc: {}, vespera: {}, eventos: [], resp: [], top: {}, v15: { migradoEm: 1 }, v17: { migradoEm: 1 } };
(async()=>{ const b=await chromium.launch(); const OUT='testes_v17_1';
 for (const [tag,vp,dark] of [['cel',{width:390,height:844},false],['desk',{width:1280,height:900},true]]) {
  const ctx=await b.newContext({viewport:vp,colorScheme:dark?'dark':'light'}); const page=await ctx.newPage();
  await page.goto('file://'+path.resolve('plataforma_v17_1_DAv2_previa.html'));
  await page.evaluate(([k,s])=>localStorage.setItem(k,JSON.stringify(s)),['c2026.v01.estado',ESTADO]); await page.reload(); await page.waitForTimeout(300);
  await page.evaluate(()=>ir('curso','P1-DA-3.4')); await page.waitForTimeout(300);
  await page.locator('.iti[data-iti="DX-01"] .bolha[data-v="E"]').click(); await page.locator('.iti[data-iti="DX-04"] .bolha[data-v="E"]').click(); await page.waitForTimeout(150);
  await page.evaluate(() => { registrar([{id:'DX-02',st:'e'},{id:'DX-05',st:'e'},{id:'DX-06',st:'c'}],'bloco'); atualizarCaderno([{id:'DX-02',st:'e'},{id:'DX-05',st:'e'}]); salvar(); });
  await page.evaluate(()=>document.querySelectorAll('.bx.rcaso details').forEach(d=>d.open=true));
  const S=async(sel,n)=>{ const l=page.locator(sel).first(); if(await l.count()){ await l.scrollIntoViewIfNeeded(); await l.screenshot({path:`${OUT}/${tag}_${n}.png`}); } };
  await S('.leitura .tarefas','el_tarefas'); await S('.bx.glo','el_glossario'); await S('.bx.caso','el_caso'); await S('.bx.rcaso','el_resposta_caso');
  await S('.iti[data-iti="DX-01"]','el_item_inline'); await S('.iti[data-iti="DX-04"]','el_item_inline2'); await S('.curso .bx.peg:has(.par3g)','el_pegadinha_abm'); await S('.fecho','el_fechamento'); await S('#pegsFim','el_pegs_fim');
  await page.evaluate(()=>ir('materia',{disc:'cd26-c11/p1/adm'})); await page.waitForTimeout(300);
  await page.evaluate(()=>document.querySelectorAll('details.card').forEach(d=>d.open=true));
  await S('.estilo-da','el_estilo_da'); await S('details.card:has(.mecs)','el_onde_erra');
  await ctx.close(); }
 await b.close(); })();
