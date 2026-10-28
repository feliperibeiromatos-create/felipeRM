const { chromium } = require('/opt/npm-tools/node_modules/playwright');
const path = require('path');
const ESTADO = { v: 1, boasVindas: true, concurso: 'cd26-c11', escolha: { DA: 'zero' }, escolhaDisc: { 'cd26-c11/p1/adm': 'zero' }, tentativas: [], erros: {}, saidas: [], lote: {}, disc: {}, vespera: {}, eventos: [], resp: [], top: {}, v15: { migradoEm: 1 }, v17: { migradoEm: 1 } };
const K = 'c2026.v01.estado';
async function abrir(browser, arquivo, opts = {}) {
  const ctx = await browser.newContext({ viewport: opts.vp || { width: 390, height: 844 }, colorScheme: opts.escuro ? 'dark' : 'light', deviceScaleFactor: opts.dsf || 1 });
  const page = await ctx.newPage();
  const erros = [];
  page.on('pageerror', e => erros.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error' || m.type() === 'warning') erros.push('console.' + m.type() + ': ' + m.text()); });
  await page.goto('file://' + path.resolve(arquivo));
  const est = opts.estado === undefined ? ESTADO : opts.estado;
  if (est !== null) {
    await page.evaluate(([k, s]) => { localStorage.setItem(k, JSON.stringify(s)); }, [K, est]);
    await page.reload();
  }
  await page.waitForTimeout(300);
  return { ctx, page, erros };
}
const estado = page => page.evaluate(k => JSON.parse(localStorage.getItem(k)), K);
module.exports = { chromium, abrir, estado, ESTADO, K };
