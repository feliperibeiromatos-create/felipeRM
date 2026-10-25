// Regressão: compara o HTML renderizado (curso, resumo, matéria, telas) entre v17 original e v17.1 com o mesmo pacote e o mesmo estado.
const { chromium, abrir } = require('./lib.js');
const fs = require('fs');
const [,, A, B, OUT, ESTFILE] = process.argv;
(async () => {
  const browser = await chromium.launch();
  const est = ESTFILE ? JSON.parse(fs.readFileSync(ESTFILE, 'utf8')) : undefined;
  const coleta = async (arq) => {
    const { page, erros } = await abrir(browser, arq, { estado: est });
    const r = await page.evaluate(async () => {
      const out = {};
      const snap = k => { out[k] = document.getElementById('app') ? app().innerHTML : document.body.innerHTML; };
      // md puro de cada seção e resumo
      const md = {};
      Object.values(T.top).forEach(o => { (o.secoes || []).forEach((s, i) => { md[o.id + '#' + i] = mdCurso2(s.corpo, o.id); }); if (o.extra && o.extra.resumo) md[o.id + '#resumo'] = mdCurso2(paraResumo(o.extra.resumo), ehDA(o.id) ? o.id : undefined); });
      (P.lotes || []).forEach(l => { if (l.resumo) md['lote:' + l.id + '#resumo'] = mdCurso2(paraResumo(l.resumo), undefined); });
      out.__md = md;
      Object.values(T.top).filter(o => o.temCurso).forEach(o => { ir('curso', o.id); snap('curso:' + o.id); });
      Object.values(T.top).forEach(o => { const r = resumoRef(o); if (r) { try { ir('resumoVer', r); snap('resumo:' + o.id); } catch (e) { out['resumo:' + o.id] = 'ERRO ' + e.message; } } });
      DISCIPLINAS.forEach(d => { ir('materia', { disc: d.id }); snap('materia:' + d.id); });
      ['painel', 'pratica', 'erros', 'recomendacoes', 'dados', 'vespera', 'discursivas'].forEach(v => { try { ir(v); snap('tela:' + v); } catch (e) { out['tela:' + v] = 'ERRO ' + e.message; } });
      return out;
    });
    return { r, erros };
  };
  const a = await coleta(A), b = await coleta(B);
  const norm = s => String(s).replace(/v17\.1/g, 'v17').replace(/data-tid="[^"]*"/g, '');
  const dif = [];
  const keysMd = new Set([...Object.keys(a.r.__md), ...Object.keys(b.r.__md)]);
  let nmd = 0; keysMd.forEach(k => { nmd++; if (norm(a.r.__md[k]) !== norm(b.r.__md[k])) dif.push({ k: 'md:' + k, a: a.r.__md[k], b: b.r.__md[k] }); });
  const keys = new Set([...Object.keys(a.r), ...Object.keys(b.r)].filter(k => k !== '__md'));
  keys.forEach(k => { if (norm(a.r[k]) !== norm(b.r[k])) dif.push({ k, a: a.r[k], b: b.r[k] }); });
  fs.writeFileSync(OUT, JSON.stringify({ nmd, ntelas: keys.size, errosA: a.erros, errosB: b.erros, dif }, null, 1));
  console.log('md comparados', nmd, 'telas', keys.size, 'diferenças', dif.length, 'errosJS A', a.erros.length, 'B', b.erros.length);
  dif.forEach(d => console.log(' -', d.k));
  await browser.close();
})();
