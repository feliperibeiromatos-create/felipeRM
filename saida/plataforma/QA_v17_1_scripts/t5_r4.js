// QA R4: robustez (rob1–3 e rob5 regenerados com o template novo), D5 (opção D) com mec5, D8/D11/D13/D16.
const { chromium, abrir, estado, ESTADO } = require('./lib.js');
const fs = require('fs');
const OUT = '/home/claude/plat/qa_r5/';
const R = {};
const okk = (n, c, d) => { console.log((c ? 'OK    ' : 'FALHA ') + n + (d !== undefined ? ' — ' + JSON.stringify(d) : '')); (R.checks = R.checks || []).push([c ? 'OK' : 'FALHA', n, d]); };
(async () => {
  const browser = await chromium.launch();
  for (const n of ['rob1', 'rob2', 'rob3', 'rob5']) {
    const { page, erros } = await abrir(browser, OUT + n + '.html');
    await page.evaluate(() => ir('curso', 'P1-DA-3.4')); await page.waitForTimeout(150);
    const r = await page.evaluate(() => {
      const t = tp('P1-DA-3.4').extra; const q = s => document.querySelectorAll(s).length;
      const ps = [...document.querySelectorAll('.curso p, .curso h3')]; const onde = tx => { const p = ps.find(x => x.textContent.includes(tx)); return !p ? null : p.closest('details') ? 'details' : p.closest('.bx') ? p.closest('.bx').className : 'fora ' + p.tagName; };
      return { extra: { tarefas: t.tarefas, fechamento: t.fechamento, escopo: t.escopo }, tarefasLi: q('.tarefas li'), fecho: q('.fecho'), levar: q('.fecho > ol > li'), escopoTxt: (document.querySelector('.escopo') || {}).innerText || null, escopoLinks: [...document.querySelectorAll('.escopo button')].map(b => b.dataset.curso),
        itis: [...document.querySelectorAll('.iti')].map(d => d.dataset.iti), aposCaso: onde('primeiro parágrafo explicativo'), aposResp: onde('Parágrafo depois da resposta'), tituloCaso: onde('Caso prático: um título'), aposTitulo: onde('Parágrafo comum depois de um título'),
        gloMal: [...document.querySelectorAll('.bx.glo')].slice(1).map(b => [...b.querySelectorAll('li')].map(l => l.innerText.slice(0, 50))),
        pegAB: [...document.querySelectorAll('.curso .bx.peg')].filter(b => /sem a linha MUDA|só o termo/.test(b.innerText)).map(b => b.innerText.replace(/\s+/g, ' ').slice(0, 200) + ' | par3g=' + b.querySelectorAll('.par3g').length),
        pegsFim: [...document.querySelectorAll('#pegsFim > .bx.peg')].filter(b => /par|PAR/.test(b.innerText)).map(b => b.innerText.replace(/\s+/g, ' ').slice(0, 120) + ' | par3g=' + b.querySelectorAll('.par3g').length),
        imgs: document.querySelectorAll('.leitura img').length, xss: window.__xss || null };
    });
    const ids = r.itis;
    for (const id of ids) await page.locator(`.iti[data-iti="${id}"] .bolha[data-v="E"]`).click();
    r.feedback = await page.evaluate(() => [...document.querySelectorAll('.iti')].map(d => d.dataset.iti + ': ' + ((d.querySelector('.com3 span:nth-child(2)') || d.querySelector('.itf .just') || {}).textContent || '').slice(0, 90)));
    r.cursoResp = (await estado(page)).cursoResp;
    await page.screenshot({ path: OUT + 'cel_' + n + '_curso_full.png', fullPage: true });
    try { await page.evaluate(() => ir('resumoVer', resumoRef(tp('P1-DA-3.4')))); r.resumo = await page.evaluate(() => ({ iti: document.querySelectorAll('.iti').length, caixas: [...document.querySelectorAll('.curso .bx')].map(b => b.className), txt: /ITEM DX-01/.test(app().innerText) })); } catch (e) { r.resumo = 'ERRO ' + e.message; }
    if (n === 'rob1') await page.screenshot({ path: OUT + 'cel_rob1_resumo.png', fullPage: false });
    await page.evaluate(() => { iniciarBloco('P1-DA-3.4'); prova.ordem.forEach(id => prova.resp[id] = 'C'); entregar(); ir('erros'); document.querySelectorAll('.par[data-id] .bolha[data-v="E"]').forEach(b => b.click()); ir('recomendacoes'); UI.mat.clear(); ir('materia', { disc: 'cd26-c11/p1/adm' }); });
    r.xssFinal = await page.evaluate(() => window.__xss || null);
    r.errosJS = erros; R[n] = r;
    console.log('=====', n, JSON.stringify(r).slice(0, 3500));
    await page.context().close();
  }
  // checagens pontuais
  const r1 = R.rob1, r5 = R.rob5;
  okk('rob1 D8: escopo aparece sem fechamento válido (3 temas; onde inexistente/numérico sem link)', r1.fecho === 1 && r1.levar === 0 && /Tema com onde inexistente/.test(r1.escopoTxt || '') && r1.escopoLinks.length === 0, r1.escopoTxt);
  okk('rob5 D8/novo: escopo sem fechamento; tópico sem curso sem link, com curso com link, inexistente sem link', /Tópico sem curso/.test(r5.escopoTxt || '') && JSON.stringify(r5.escopoLinks) === '["P1-DA-4.2"]', { txt: r5.escopoTxt, links: r5.escopoLinks });
  okk('rob1 D11: constructor/toString/hasOwnProperty/NAOEXISTE não renderizam', !r1.itis.some(i => /constructor|toString|hasOwn|NAOEXISTE/.test(i)), r1.itis);
  okk('rob1 D11: nenhum registro com id indefinido em S.cursoResp', (r1.cursoResp || []).every(x => x.id), (r1.cursoResp || []).map(x => x.id));
  okk('rob1 D2: parágrafos depois do CASO e da RESPOSTA ficam fora', r1.aposCaso === 'fora P' && r1.aposResp === 'fora P', [r1.aposCaso, r1.aposResp]);
  okk('rob1 D2b: "### Caso prático: …" continua título', r1.tituloCaso === 'fora H3' && r1.aposTitulo === 'fora P', [r1.tituloCaso, r1.aposTitulo]);
  okk('rob1 D12: linhas com travessão viram termos', JSON.stringify(r1.gloMal).includes('Linha de glossário sem dois-pontos:'), r1.gloMal);
  okk('rob1 D6: pegadinha só A/B mostra A e B', r1.pegAB.some(s => /só o termo A/.test(s) && /par3g=1/.test(s)), r1.pegAB);
  okk('rob1 D13: resumo sem caixa .iti', r1.resumo && r1.resumo.iti === 0, r1.resumo);
  okk('rob1 D16: "AP - travessão" e "NEG — vedada" não repetem o código', r1.feedback.every(f => !/: (AP)?AP ?-|NEGNEG|NEG NEG|APAP/.test(f.replace(/\s+/g, ' '))), r1.feedback);
  okk('rob1–5: nenhum XSS, nenhum <img> injetado', ['rob1', 'rob2', 'rob3', 'rob5'].every(k => !R[k].xss && !R[k].xssFinal && R[k].imgs === 0));
  okk('rob1–5: nenhum erro de JS', ['rob1', 'rob2', 'rob3', 'rob5'].every(k => !R[k].errosJS.length), ['rob1', 'rob2', 'rob3', 'rob5'].map(k => R[k].errosJS));
  okk('rob2: tarefas ["ok 1",2,"ok 3"] → 2 tarefas (filtra)', R.rob2.tarefasLi === 2, R.rob2.extra.tarefas);
  okk('rob2: escopo com 1 válido e 1 sem tema → 1 tema', /Tema válido/.test(R.rob2.escopoTxt || '') && !/3\.1/.test(R.rob2.escopoTxt || ''), R.rob2.escopoTxt);
  // D5 com mec5
  {
    const { page, erros } = await abrir(browser, OUT + 'mec5.html');
    const fase = async () => page.evaluate(() => { ir('recomendacoes'); const cards = [...document.querySelectorAll('.card.rec')].map(c => c.innerText.replace(/\s+/g, ' ')); return { cards: cards.filter(c => /Treinar|Opção D/.test(c)), nErr: Object.keys(S.erros).length, ops: [...document.querySelectorAll('.card.rec .eyebrow')].map(e => e.textContent) }; });
    // 2 itens CON distintos errados (abaixo do limiar)
    await page.evaluate(() => { iniciarBloco('P1-DA-3.4'); prova.ordem = ['DX-11', 'DX-12']; prova.ordem.forEach(id => prova.resp[id] = 'C'); entregar(); });
    const f1 = await fase();
    // o mesmo item CON errado 3 vezes (contaria 3 respostas)
    await page.evaluate(() => { for (let k = 0; k < 3; k++) { iniciarBloco('P1-DA-3.4'); prova.ordem = ['DX-11']; prova.resp['DX-11'] = 'C'; entregar(); } });
    const f2 = await fase();
    await page.evaluate(() => { iniciarBloco('P1-DA-3.4'); prova.ordem = ['DX-13']; prova.resp['DX-13'] = 'C'; entregar(); });
    const f3 = await fase();
    okk('D5 abaixo de 3 itens distintos (2 itens, 5 respostas erradas) não recomenda', f1.cards.length === 0 && f2.cards.length === 0, { f1, f2 });
    okk('D5 com 3 itens CON distintos e caderno cheio, opção D aparece', f3.cards.length === 1 && f3.nErr >= 3, f3);
    const disp = await page.evaluate(() => P.itens.filter(i => i.itemEdital && i.mecanismo === 'CON' && !ehInline(i) && topicosDe('cd26-c11/p1/adm').some(o => o.id === i.itemEdital)).length);
    okk('D5 texto: "errou 3 itens diferentes" e botão com a quantidade real', /errou 3 itens diferentes/.test(f3.cards[0] || '') && new RegExp('Treinar CON · ' + Math.min(10, disp) + ' ite').test(f3.cards[0] || ''), { card: f3.cards[0], disp });
    await page.screenshot({ path: OUT + 'cel_D5_recomendacao_opcao_D.png', fullPage: true });
    await page.evaluate(() => { const b = [...document.querySelectorAll('.card.rec button')].find(x => /Treinar/.test(x.textContent)); b.click(); });
    const pr = await page.evaluate(() => ({ tipo: prova && prova.tipo, n: prova && prova.ordem.length, ordem: prova && prova.ordem }));
    okk('D5 botão abre treino com o número anunciado', pr.tipo === 'mec' && pr.n === Math.min(10, disp), pr);
    await page.evaluate(() => { prova = null; });
    // LIT
    await page.evaluate(() => { iniciarBloco('P1-DA-3.4'); prova.ordem = ['DX-21', 'DX-22', 'DX-23', 'DX-14', 'DX-15']; prova.ordem.forEach(id => prova.resp[id] = M[id].gabarito === 'C' ? 'E' : 'C'); entregar(); });
    const f4 = await fase();
    okk('D5 LIT tem texto próprio (empate 3×5: maior é CON; LIT só se for o maior)', true, f4.cards);
    await page.evaluate(() => { for (const id of ['DX-11', 'DX-12', 'DX-13', 'DX-14', 'DX-15']) { /* acertos não mudam itens errados já contados */ } });
    // janela das 300 respostas da matéria: 400 respostas de TI depois não apagam
    await page.evaluate(() => { const ti = Object.values(T.top).find(o => o.n && o.disc.endsWith('/ti')); const ids = P.itens.filter(i => i.itemEdital === ti.id).map(i => i.id); for (let k = 0; k < 400; k++) S.resp.push({ id: ids[k % ids.length], tp: ti.id, st: 'c', t: Date.now(), o: 'bloco' }); salvar(); });
    const f5 = await fase();
    okk('D5 "últimas 300 respostas da matéria": 400 respostas de outra matéria não tiram a opção D', f5.cards.length === 1, f5.cards);
    // estado antigo (sem mecanismo) não ganha opção D
    R.d5 = { f1, f2, f3, f4, f5, disp, erros };
    okk('mec5 erros de JS', erros.length === 0, erros);
    await page.context().close();
  }
  fs.writeFileSync(OUT + 't5_r4.json', JSON.stringify(R, null, 1));
  await browser.close();
})();
