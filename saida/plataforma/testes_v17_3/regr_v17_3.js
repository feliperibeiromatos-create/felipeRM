// regr_v17_3.js — regressão v17.2 → v17.3 com estado antigo: notas, caderno, bloco de 10, chaves do estado e TODAS as telas iguais
// (só a versão muda); as telas de Resumo dos tópicos com resumoVisual mudam (esperado) e as dos demais tópicos não mudam.
const { chromium, abrir, estado } = require('./lib.js');
const fs = require('fs');
const [,, A, B, ESTF, OUT] = process.argv;
const est = JSON.parse(fs.readFileSync(ESTF, 'utf8'));
(async () => {
  const browser = await chromium.launch();
  const coleta = async arq => {
    const { page, erros } = await abrir(browser, arq, { estado: est });
    const r = await page.evaluate(() => {
      Math.random = (() => { let s = 11; return () => (s = (s * 16807) % 2147483647) / 2147483647; })();
      const out = {}; const snap = k => out[k] = app().innerText;
      out.__notas = JSON.stringify(Object.values(T.top).map(o => [o.id, JSON.stringify(notaTopico(o.id)), pctTopico(o)]));
      out.__erros = JSON.stringify(S.erros); out.__nresp = S.resp.length; out.__nf = notaFinal();
      out.__bloco = JSON.stringify(Object.keys(T.top).filter(t => tp(t).n).slice(0, 12).map(t => montarBloco(t)));
      S.tentativas.forEach((t, i) => { ir('resultado', i); snap('resultado:' + i); });
      ['painel', 'pratica', 'erros', 'recomendacoes', 'dados', 'vespera', 'discursivas'].forEach(v => { ir(v); snap('tela:' + v); });
      DISCIPLINAS.forEach(d => { ir('materia', { disc: d.id }); snap('materia:' + d.id); });
      out.__rv = {}; Object.keys(T.top).forEach(t => { const o = tp(t); const r = resumoRef(o); if (!r) return; ir('resumoVer', r); out.__rv[t] = { rv: !!app().querySelector('.rv'), txt: app().innerText.length }; snap('resumo:' + t); });
      const o = tp('P1-DA-2.1'); if (o && o.temCurso) { ir('curso', 'P1-DA-2.1'); snap('curso:P1-DA-2.1'); }
      return out;
    });
    const st = await estado(page); return { r, erros, st };
  };
  const a = await coleta(A), b = await coleta(B);
  const dif = [], esperadas = [];
  ['__notas', '__erros', '__nresp', '__nf', '__bloco'].forEach(k => { if (JSON.stringify(a.r[k]) !== JSON.stringify(b.r[k])) dif.push({ k, a: String(a.r[k]).slice(0, 160), b: String(b.r[k]).slice(0, 160) }); });
  const norm = s => String(s).replace(/v17\.3/g, 'v17.2').replace(/\s+/g, ' ').trim();
  Object.keys(a.r).filter(k => !k.startsWith('__')).forEach(k => { const x = norm(a.r[k]), y = norm(b.r[k]); if (x !== y) { const comRV = k.startsWith('resumo:') && b.r.__rv[k.slice(7)] && b.r.__rv[k.slice(7)].rv; (comRV ? esperadas : dif).push({ k, a: x.slice(0, 120), b: y.slice(0, 120) }); } });
  Object.keys(b.r.__rv).forEach(t => { if (b.r.__rv[t].rv && !a.r.__rv[t].rv) { /* ok: novo resumo visual */ } else if (a.r.__rv[t].rv !== b.r.__rv[t].rv) dif.push({ k: 'rv:' + t, a: a.r.__rv[t], b: b.r.__rv[t] }); });
  const ka = Object.keys(a.st).sort().join(), kb = Object.keys(b.st).sort().join(); if (ka !== kb) dif.push({ k: 'estado:chaves', a: ka, b: kb });
  ['tentativas', 'erros', 'resp', 'saidas', 'cursoResp'].forEach(k => { if (JSON.stringify(est[k]) !== JSON.stringify(b.st[k])) dif.push({ k: 'estado:' + k }); }); if (JSON.stringify(a.st.top) !== JSON.stringify(b.st.top)) dif.push({ k: 'estado:top (A×B)' });
  const res = { telas: Object.keys(a.r).filter(k => !k.startsWith('__')).length, resumosVisuais: Object.values(b.r.__rv).filter(x => x.rv).length, esperadas: esperadas.map(e => e.k), dif, errosA: a.erros, errosB: b.erros };
  fs.writeFileSync(OUT, JSON.stringify(res, null, 1));
  console.log(`telas ${res.telas} · resumos visuais em B ${res.resumosVisuais} · mudanças esperadas (telas de Resumo com .rv) ${esperadas.length} · diferenças NÃO esperadas ${dif.length} · erros JS A ${a.erros.length} B ${b.erros.length}`);
  dif.forEach(d => console.log(' !', JSON.stringify(d).slice(0, 300)));
  await browser.close(); process.exit(dif.length || a.erros.length || b.erros.length ? 1 : 0);
})();
