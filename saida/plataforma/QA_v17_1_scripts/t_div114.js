const { chromium, abrir } = require('./lib.js'); const fs=require('fs');
const est=JSON.parse(fs.readFileSync('/home/claude/plat/qa_r3/estado_v17_antigo.json','utf8'));
(async()=>{ const b=await chromium.launch(); const out={};
 for (const [nome,arq] of [['v17','/home/claude/plat/qa_r5/base_v17_v114.html'],['v171','/home/claude/plat/plataforma_v17_1_regressao_v114.html']]) for (const [en,e] of [['vazio',undefined],['antigo',est]]) {
  const {page,erros}=await abrir(b,arq,{estado:e});
  out[nome+'_'+en]=await page.evaluate(()=>({nTop:Object.keys(T.top).length, nInl:Object.values(T.top).reduce((s,o)=>s+(o.nInline||0),0), div:Object.fromEntries(Object.values(T.top).map(o=>[o.id,divTopico(o.id)])), pct:Object.fromEntries(Object.values(T.top).map(o=>[o.id,pctTopico(o)])), mat:Object.fromEntries(DISCIPLINAS.map(d=>[d.id,mediaMateria(d)])), p1:mediaProva('P1'), p2:mediaProva('P2'), nf:notaFinal(), nfTela:(ir('painel'),(document.getElementById('nfv')||{}).textContent)}));
  out[nome+'_'+en].erros=erros; await page.context().close(); }
 const cmp=(a,c)=>{ const A=out[a],C=out[c]; const d=[]; Object.keys(A.div).forEach(k=>{ if(A.div[k]!==C.div[k]) d.push('div '+k); if(A.pct[k]!==C.pct[k]) d.push('pct '+k); }); Object.keys(A.mat).forEach(k=>{ if(A.mat[k]!==C.mat[k]) d.push('mat '+k); }); ['p1','p2','nf','nfTela'].forEach(k=>{ if(A[k]!==C[k]) d.push(k); }); return {nTop:A.nTop, nInlineV171:C.nInl, difs:d, p1:[A.p1,C.p1], nf:[A.nfTela,C.nfTela], topicosComResposta:Object.values(A.pct).filter(x=>x!==0).length}; };
 const r={vazio:cmp('v17_vazio','v171_vazio'), antigo:cmp('v17_antigo','v171_antigo'), erros:Object.values(out).map(x=>x.erros.length)};
 console.log(JSON.stringify(r)); fs.writeFileSync('/home/claude/plat/qa_r5/t_div114.json',JSON.stringify(r,null,1)); await b.close(); })();
