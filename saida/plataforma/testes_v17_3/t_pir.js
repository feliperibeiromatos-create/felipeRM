// t_pir.js — aceite D7/D20: pirâmide sem transbordo (scrollWidth<=clientWidth em cada .nv) em 320/390/1280, claro e escuro; role=group e <ol>.
const { chromium, abrir } = require('./lib.js');
const ARQ = process.argv[2];
(async () => {
  const b = await chromium.launch(); let falhas = 0;
  for (const [w, dark] of [[320, false], [320, true], [390, false], [390, true], [1280, false], [1280, true]]) {
    const { page, ctx } = await abrir(b, ARQ, { vp: { width: w, height: 900 }, escuro: dark, dsf: 1 });
    await page.evaluate(() => ir('resumoVer', { topico: 'P1-DA-3.4' })); await page.waitForTimeout(250);
    const r = await page.evaluate(() => {
      const f = document.querySelector('.rv-pir'); const fig = f && f.closest('figure');
      return { tag: f && f.tagName, role: fig && fig.getAttribute('role'), label: fig && fig.getAttribute('aria-label'),
        nv: [...document.querySelectorAll('.rv-pir .nv')].map(n => ({ sw: n.scrollWidth, cw: n.clientWidth, w: n.getBoundingClientRect().width, b: n.querySelector('b').textContent, tb: n.querySelector('b').scrollWidth, cb: n.querySelector('b').clientWidth })) };
    });
    const ok = r.tag === 'OL' && r.role === 'group' && r.nv.every(n => n.sw <= n.cw && n.tb <= n.cb);
    if (!ok) falhas++;
    console.log(w, dark ? 'escuro' : 'claro', ok ? 'OK' : 'FALHA', JSON.stringify(r));
    if (w === 390 || w === 1280) { const el = await page.$('.rv-pir'); await el.screenshot({ path: `caps/pir_${w}_${dark ? 'esc' : 'claro'}.png` }); }
    await ctx.close();
  }
  await b.close(); console.log('falhas', falhas); process.exit(falhas ? 1 : 0);
})();
