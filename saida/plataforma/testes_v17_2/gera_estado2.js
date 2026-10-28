// gera_estado2.js — estado antigo com 21–30 distintas em dois tópicos (QA R1 D2), gerado pela interface da v17.1: blocos em DA/TI/Fala, um simulado, D30, revisão do caderno, discursiva.
const { chromium, abrir, estado } = require('./lib.js');
const fs = require('fs');
const [,, ARQ, OUT] = process.argv;
(async () => {
  const browser = await chromium.launch();
  const { page, erros } = await abrir(browser, ARQ);
  await page.evaluate(() => { Math.random = (() => { let s = 7; return () => (s = (s * 16807) % 2147483647) / 2147483647; })(); });
  const info = await page.evaluate(() => {
    const resp = (ids, f) => ids.forEach((id, k) => { prova.resp[id] = f(k, M[id]); });
    const tops = Object.values(T.top).filter(o => o.n);
    const alvo = ['P1-DA-3.4', 'P1-DA-1.1', 'P1-DA-10.1'].filter(t => tp(t) && tp(t).n);
    const ti = tops.find(o => o.disc.endsWith('/ti')); const fala = tops.find(o => o.disc.endsWith('/fala'));
    [...alvo, ti && ti.id, fala && fala.id].filter(Boolean).forEach((tid, j) => {
      iniciarBloco(tid); resp(prova.ordem, (k, it) => k % 3 === 0 ? (it.gabarito === 'C' ? 'E' : 'C') : (k % 5 === 4 ? null : it.gabarito)); entregar();
    });
    // segundo bloco no 3.4 para repetidas
    iniciarBloco('P1-DA-3.4'); resp(prova.ordem, (k, it) => k % 2 ? it.gabarito : (it.gabarito === 'C' ? 'E' : 'C')); entregar();
    // três blocos em dois tópicos com banco de 30: 30 distintas (corte da janela de 20)
    ['P1-DA-11', 'P2-4.1'].filter(t => tp(t) && tp(t).n >= 30).forEach(tid => { for (let b = 0; b < 3; b++) { iniciarBloco(tid); resp(prova.ordem, (k, it) => (b === 0 && k < 6) ? (it.gabarito === 'C' ? 'E' : 'C') : (k % 9 === 8 ? null : it.gabarito)); entregar(); } });
    // simulado
    const sims = listaSimulados(); const s = sims.find(x => !/^D30-/.test(x.id)) || sims[0];
    iniciar(s.id); resp(prova.ordem, (k, it) => k % 4 === 0 ? (it.gabarito === 'C' ? 'E' : 'C') : (k % 7 === 6 ? null : it.gabarito)); entregar();
    // D30 DA
    const d30 = sims.find(x => x.id === 'D30-DA'); if (d30) { iniciar('D30-DA'); resp(prova.ordem, (k, it) => k % 2 ? it.gabarito : (it.gabarito === 'C' ? 'E' : 'C')); entregar(); }
    return { tent: S.tentativas.length, resp: S.resp.length, erros: Object.keys(S.erros).length, sim: s.id, d30: !!d30 };
  });
  const st = await estado(page);
  fs.writeFileSync(OUT, JSON.stringify(st));
  console.log(JSON.stringify(info), 'erros JS', erros);
  await browser.close();
})();
