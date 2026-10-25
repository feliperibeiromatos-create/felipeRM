// Regressão: telas de questão (bloco, simulado, D30, revisão do caderno), discursivas e matéria TI/DA em contexto limpo — v17 × v17.1 (pacote v1.14).
const { chromium, abrir } = require('./lib.js');
const fs = require('fs');
const [,, A, B, ESTF, OUT] = process.argv;
const est = JSON.parse(fs.readFileSync(ESTF, 'utf8'));
(async () => {
  const browser = await chromium.launch();
  const coleta = async arq => {
    const { page, erros } = await abrir(browser, arq, { estado: est });
    await page.evaluate(() => { Math.random = (() => { let s = 11; return () => (s = (s * 16807) % 2147483647) / 2147483647; })(); });
    const r = await page.evaluate(() => {
      const out = {}; const snap = k => out[k] = app().innerHTML;
      const passa = (pref) => { const n = prova.ordem.length; for (let k = 0; k < n; k++) { prova.i = k; render(); snap(pref + ':' + k); } };
      iniciarBloco('P1-DA-3.4'); passa('bloco34'); prova = null;
      const ti = Object.values(T.top).find(o => o.n && o.disc.endsWith('/ti')); iniciarBloco(ti.id); passa('blocoTI'); prova = null;
      iniciar('SIM-0'); passa('sim0'); clearInterval(prova.timer); prova = null;
      iniciar('D30-DA'); passa('d30'); clearInterval(prova.timer); prova = null;
      iniciarRevisao(Object.keys(S.erros).slice(0, 10)); passa('rev'); prova = null;
      (P.discursivas || []).slice(0, 2).forEach(d => { ir('disc', d.id); snap('disc:' + d.id); });
      return out;
    });
    const mat = {};
    for (const d of ['cd26-c11/p1/ti', 'cd26-c11/p1/adm', 'cd26-c11/p2/fala']) {
      const p2 = await abrir(browser, arq, { estado: est });
      mat[d] = await p2.page.evaluate(d => { ir('materia', { disc: d }); return { card: document.querySelectorAll('details.estilo-da').length, onde: /Onde você erra/.test(app().innerText) }; }, d);
      erros.push(...p2.erros); await p2.ctx.close();
    }
    return { r, erros, mat };
  };
  const a = await coleta(A), b = await coleta(B);
  const dif = Object.keys(a.r).filter(k => a.r[k] !== b.r[k]);
  const res = { telas: Object.keys(a.r).length, dif, matA: a.mat, matB: b.mat, errosA: a.erros, errosB: b.erros };
  fs.writeFileSync(OUT, JSON.stringify(res, null, 1)); console.log(JSON.stringify(res, null, 1).slice(0, 3000));
  await browser.close();
})();
