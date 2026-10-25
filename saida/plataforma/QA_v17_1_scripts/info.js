const { chromium, abrir } = require('./lib.js');
(async()=>{ const b=await chromium.launch(); const {page}=await abrir(b,process.argv[2]);
console.log(await page.evaluate(()=>JSON.stringify({semCurso:Object.values(T.top).filter(o=>!o.temCurso).map(o=>o.id+':'+o.n).slice(0,30), t34:{n:tp('P1-DA-3.4').n,nInline:tp('P1-DA-3.4').nInline,div:divTopico('P1-DA-3.4')}, simsComDX:listaSimulados().filter(s=>s.itens.some(i=>/^DX/.test(i))).map(s=>s.id)})));
await b.close();})();
