// R5 · N1: acertar todas as questões de verificação do 3.4 pela interface e medir tópico, matéria, P1 e Nota Final (tela e oráculo).
const { chromium, abrir } = require('./lib.js');
const fs = require('fs');
const OUT = '/home/claude/plat/qa_r5/';
(async () => {
  const b = await chromium.launch(); const R = {};
  for (const modo of [{ nome: 'cel', vp: { width: 390, height: 844 }, escuro: false }, { nome: 'desk', vp: { width: 1280, height: 900 }, escuro: true }]) {
    const { page, erros } = await abrir(b, '/home/claude/plat/plataforma_v17_1_DAv2_previa.html', modo);
    const ini = await page.evaluate(() => ({ div34: divTopico('P1-DA-3.4'), n34: tp('P1-DA-3.4').n, nInline: tp('P1-DA-3.4').nInline, banco34: P.itens.filter(i => i.itemEdital === 'P1-DA-3.4').length, div1: divTopico('P1-DA-1'), banco1: new Set(P.itens.filter(i => i.itemEdital === 'P1-DA-1').map(i => i.id)).size,
      outros: Object.values(T.top).filter(o => o.id !== 'P1-DA-3.4').every(o => divTopico(o.id) === Math.max(1, Math.min(30, new Set(P.itens.filter(i => i.itemEdital === o.id).map(i => i.id)).size))) }));
    const vistos = new Set(); let rod = 0;
    while (rod < 10) {
      rod++; await page.evaluate(() => ir('curso', 'P1-DA-3.4')); await page.locator('#praticar').click();
      const n = await page.evaluate(() => prova.ordem.length);
      for (let k = 0; k < n; k++) { const it = await page.evaluate(() => { const it = M[prova.ordem[prova.i]]; return { id: it.id, g: it.gabarito }; }); vistos.add(it.id); await page.locator('#b' + it.g).click(); if (k < n - 1) await page.locator('#prox').click(); else { await page.locator('#fim').click(); await page.locator('#sim2').click(); } }
      if (vistos.size >= ini.n34) break;
    }
    const med = await page.evaluate(() => {
      const d = discById(tp('P1-DA-3.4').disc); const ts = topicosDe(d.id); const p1 = DISCIPLINAS.filter(x => x.prova === 'P1');
      const oraculoMateria = ts.reduce((s, o) => s + pesoTop(o) * (o.id === 'P1-DA-3.4' ? 1 : 0), 0) / ts.reduce((s, o) => s + pesoTop(o), 0);
      const oraculoP1 = p1.reduce((s, x) => s + pesoDisc(x) * (x.id === d.id ? oraculoMateria : 0), 0) / p1.reduce((s, x) => s + pesoDisc(x), 0);
      ir('painel'); const nfv = (document.getElementById('nfv') || {}).textContent; const painel = app().innerText;
      UI.mat.clear(); ir('materia', { disc: d.id }); const linha = (document.querySelector('#t-P1-DA-3\\.4 .pc') || {}).textContent;
      return { nt: notaTopico('P1-DA-3.4'), div: divTopico('P1-DA-3.4'), pct: pctTopico(tp('P1-DA-3.4')), linhaTopico: linha, mediaMateria: mediaMateria(d), oraculoMateria, mediaP1: mediaProva('P1'), oraculoP1, notaP1: notaProva('P1'), notaFinal: notaFinal(), oraculoNF: 90 * oraculoP1, nfTela: nfv, nTopicosDA: ts.length, nDiscP1: p1.length,
        painelLinhas: painel.split('\n').filter(l => /Direito Administrativo|^P1|Nota Final|Conhecimentos básicos/.test(l)).slice(0, 8) };
    });
    // troca de pacote em tempo de execução: o cache do divisor é refeito
    const swap = await page.evaluate(() => { usarPacote(JSON.parse(JSON.stringify(P))); return { div: divTopico('P1-DA-3.4'), pct: pctTopico(tp('P1-DA-3.4')) }; });
    R[modo.nome] = { ini, rodadas: rod, distintos: vistos.size, inlineVistos: [...vistos].filter(i => ['DX-01', 'DX-03', 'DX-04'].includes(i)), med, swap, erros };
    await page.evaluate(() => { ir('painel'); }); await page.screenshot({ path: OUT + modo.nome + '_N1_painel.png', fullPage: true });
    await page.evaluate(() => { UI.mat.clear(); ir('materia', { disc: 'cd26-c11/p1/adm' }); });
    const l = page.locator('#t-P1-DA-3\\.4'); await l.scrollIntoViewIfNeeded(); await l.screenshot({ path: OUT + modo.nome + '_N1_topico_100.png' });
    console.log(modo.nome, JSON.stringify(R[modo.nome], null, 1));
    await page.context().close();
  }
  fs.writeFileSync(OUT + 't_n1.json', JSON.stringify(R, null, 1)); await b.close();
})();
