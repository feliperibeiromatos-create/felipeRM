// capturas_rv.js — Resumo visual DA: página inteira de cada tópico da leva, 390×844 claro e 1280×900 escuro. Uso: node capturas_rv.js <previa.html> <pasta> [ids...]
const { chromium, abrir } = require('./lib.js');
const [,, ARQ, OUT, ...IDS] = process.argv;
const ids = IDS.length ? IDS : ['P1-DA-1', 'P1-DA-1.1', 'P1-DA-1.2', 'P1-DA-2.1', 'P1-DA-2.2', 'P1-DA-3.1', 'P1-DA-3.2', 'P1-DA-3.3', 'P1-DA-3.4'];
(async () => {
  const b = await chromium.launch(); const erros = {};
  for (const [tag, vp, dark] of [['cel', { width: 390, height: 844 }, false], ['desk', { width: 1280, height: 900 }, true]]) {
    const { page, erros: e, ctx } = await abrir(b, ARQ, { vp, escuro: dark, dsf: 1 });
    for (const id of ids) {
      await page.evaluate(t => ir('resumoVer', { topico: t }), id); await page.waitForTimeout(250);
      const ok = await page.evaluate(() => !!app().querySelector('.rv'));
      await page.screenshot({ path: `${OUT}/${tag}_${id}.png`, fullPage: true });
      if (!ok) console.log('SEM .rv em', id, tag);
    }
    erros[tag] = e; await ctx.close();
  }
  console.log('erros JS', JSON.stringify(erros)); await b.close();
})();
