// capturas_v17_2.js — telas da v17.2 com o status da nota (390×844 claro; 1280×900 escuro). Uso: node capturas_v17_2.js <previa.html> <pasta_saida>
const { chromium, abrir } = require('./lib.js');
const [,, ARQ, OUT] = process.argv;
(async () => {
  const b = await chromium.launch();
  for (const [tag, vp, dark] of [['cel', { width: 390, height: 844 }, false], ['desk', { width: 1280, height: 900 }, true]]) {
    const { page, erros, ctx } = await abrir(b, ARQ, { vp, escuro: dark, dsf: 2 });
    // tópico grande com 10 respondidas (nota parcial) + tópico pequeno completo
    const info = await page.evaluate(() => {
      Math.random = (() => { let s = 3; return () => (s = (s * 16807) % 2147483647) / 2147483647; })();
      const inl = t => idsInline(t); const itensDe = t => P.itens.filter(i => i.itemEdital === t && !inl(t).has(i.id));
      const tops = Object.values(T.top).filter(o => o.n && o.disc === 'cd26-c11/p1/adm').map(o => ({ id: o.id, n: itensDe(o.id).length, curso: o.temCurso }));
      const big = tops.filter(t => t.n >= 25 && t.curso).sort((a, b) => b.n - a.n)[0]; const small = tops.filter(t => t.n >= 8 && t.n <= 15).sort((a, b) => a.n - b.n)[0];
      S.resp = []; S.erros = {}; _divP = null; delete S.avisoV172;
      itensDe(big.id).slice(0, 10).forEach((it, k) => S.resp.push({ id: it.id, tp: big.id, st: k < 8 ? 'c' : 'e', t: Date.now() + k }));
      itensDe(small.id).forEach((it, k) => S.resp.push({ id: it.id, tp: small.id, st: k % 5 === 4 ? 'e' : 'c', t: Date.now() + 100 + k }));
      salvar(); return { big, small };
    });
    const S = async (sel, n, full) => { const l = page.locator(sel).first(); if (await l.count()) { await l.scrollIntoViewIfNeeded(); await l.screenshot({ path: `${OUT}/${tag}_${n}.png` }); } else console.log('sem', sel); };
    await page.evaluate(() => ir('painel')); await page.waitForTimeout(250);
    await page.screenshot({ path: `${OUT}/${tag}_painel_aviso.png`, fullPage: false }); await S('#avisoV172', 'el_aviso');
    await page.evaluate(() => ir('painel')); await page.waitForTimeout(150); // segunda visita: sem aviso
    await page.screenshot({ path: `${OUT}/${tag}_painel_sem_aviso.png`, fullPage: false });
    await page.evaluate(b => ir('materia', { disc: 'cd26-c11/p1/adm' })); await page.waitForTimeout(250); await S(`[id="t-${info.big.id}"] .top-t`, 'el_linha_topico_parcial'); await S(`[id="t-${info.small.id}"] .top-t`, 'el_linha_topico_completa');
    await page.evaluate(() => ir('apresentacao')); await page.waitForTimeout(250); await S('.hl.small', 'el_ajuda');
    await page.evaluate(b => ir('curso', b), info.big.id); await page.waitForTimeout(300); await S('#fimCurso', 'el_fim_curso_parcial');
    await page.evaluate(s => ir('curso', s), info.small.id); await page.waitForTimeout(300); await S('#fimCurso', 'el_fim_curso_completa');
    await page.evaluate(b => { iniciarBloco(b); prova.ordem.forEach((id, k) => { prova.resp[id] = k < 9 ? M[id].gabarito : null; }); entregar(); }, info.big.id); await page.waitForTimeout(300);
    await page.screenshot({ path: `${OUT}/${tag}_resultado_bloco.png`, fullPage: false }); await S('.card.on.stack:has-text("Desempenho no tópico")', 'el_pos_bloco');
    await page.evaluate(() => ir('recomendacoes')); await page.waitForTimeout(300); await page.screenshot({ path: `${OUT}/${tag}_recomendacoes.png`, fullPage: false });
    console.log(tag, JSON.stringify(info), 'erros JS', erros);
    await ctx.close();
  }
  await b.close();
})();
