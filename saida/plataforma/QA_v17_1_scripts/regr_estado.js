// Regressão com estado antigo (v17): mesmas notas, mesmo caderno, mesmas telas de resultado/erros/recs/dados entre v17 e v17.1.
const { chromium, abrir, estado } = require('./lib.js');
const fs = require('fs');
const [,, A, B, ESTF, OUT] = process.argv;
const est = JSON.parse(fs.readFileSync(ESTF, 'utf8'));
(async () => {
  const browser = await chromium.launch();
  const coleta = async arq => {
    const { page, erros } = await abrir(browser, arq, { estado: est });
    const r = await page.evaluate(() => {
      const out = {};
      const snap = k => out[k] = app().innerHTML;
      out.__notas = Object.fromEntries(Object.values(T.top).map(o => [o.id, JSON.stringify(notaTopico(o.id)) + '|' + pctTopico(o)]));
      out.__erros = JSON.stringify(S.erros); out.__nresp = S.resp.length;
      S.tentativas.forEach((t, i) => { ir('resultado', i); snap('resultado:' + i); });
      ['painel', 'pratica', 'erros', 'recomendacoes', 'dados', 'vespera', 'discursivas'].forEach(v => { ir(v); snap('tela:' + v); });
      DISCIPLINAS.forEach(d => { UI.top && UI.top.clear && UI.top.clear(); ir('materia', { disc: d.id }); snap('materia:' + d.id); });
      return out;
    });
    const st = await estado(page);
    return { r, erros, st };
  };
  const a = await coleta(A), b = await coleta(B);
  const norm = s => String(s).replace(/v17\.1/g, 'v17');
  const dif = [];
  Object.keys(a.r.__notas).forEach(k => { if (a.r.__notas[k] !== b.r.__notas[k]) dif.push({ k: 'nota:' + k, a: a.r.__notas[k], b: b.r.__notas[k] }); });
  ['__erros', '__nresp'].forEach(k => { if (a.r[k] !== b.r[k]) dif.push({ k, a: a.r[k], b: b.r[k] }); });
  Object.keys(a.r).filter(k => !k.startsWith('__')).forEach(k => { if (norm(a.r[k]) !== norm(b.r[k])) dif.push({ k, a: a.r[k], b: b.r[k] }); });
  const ka = Object.keys(a.st).sort().join(','), kb = Object.keys(b.st).sort().join(',');
  const chaves = { a: ka, b: kb, orig: Object.keys(est).sort().join(',') };
  ['tentativas', 'erros', 'resp', 'saidas', 'top', 'escolha', 'escolhaDisc', 'disc', 'vespera'].forEach(k => { if (JSON.stringify(est[k]) !== JSON.stringify(b.st[k])) dif.push({ k: 'estado:' + k, a: 'orig', b: 'mudou' }); });
  fs.writeFileSync(OUT, JSON.stringify({ chaves, errosA: a.erros, errosB: b.erros, dif }, null, 1));
  console.log('chaves', JSON.stringify(chaves)); console.log('dif', dif.length, 'erros A', a.erros.length, 'B', b.erros.length);
  dif.forEach(d => console.log(' -', d.k, d.k.startsWith('nota') || d.k.startsWith('__') || d.k.startsWith('estado') ? (d.a + ' => ' + d.b) : ''));
  await browser.close();
})();
