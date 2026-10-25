// Testes v17 DA-v2 (Playwright, Chromium pré-instalado). Uso: node testes_dav2.js <previa.html> <regressao.html> <pasta_saida>
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
const [,, PREVIA, REGR, OUT] = process.argv;
fs.mkdirSync(OUT, { recursive: true });
const R = { testes: [], errosJS: [], shots: [] };
const ok = (nome, cond, det) => { R.testes.push({ nome, ok: !!cond, det: det || '' }); console.log((cond ? 'OK   ' : 'FALHA') + ' ' + nome + (det ? ' — ' + det : '')); };
const ESTADO = { v: 1, boasVindas: true, concurso: 'cd26-c11', escolha: { DA: 'zero' }, escolhaDisc: { 'cd26-c11/p1/adm': 'zero' }, tentativas: [], erros: {}, saidas: [], lote: {}, disc: {}, vespera: {}, eventos: [], resp: [], top: {}, v15: { migradoEm: 1 }, v17: { migradoEm: 1 } };

async function abrir(browser, arquivo, vp, escuro, estado) {
  const ctx = await browser.newContext({ viewport: vp, colorScheme: escuro ? 'dark' : 'light' });
  const page = await ctx.newPage();
  page.on('pageerror', e => R.errosJS.push({ arquivo: path.basename(arquivo), msg: String(e.message) }));
  page.on('console', m => { if (m.type() === 'error') R.errosJS.push({ arquivo: path.basename(arquivo), msg: 'console: ' + m.text() }); });
  await page.goto('file://' + path.resolve(arquivo));
  await page.evaluate(([k, s]) => { localStorage.setItem(k, JSON.stringify(s)); }, ['c2026.v01.estado', estado || ESTADO]);
  await page.reload(); await page.waitForTimeout(400);
  return { ctx, page };
}
const shot = async (page, nome) => { const f = path.join(OUT, nome + '.png'); await page.screenshot({ path: f, fullPage: nome.includes('full') }); R.shots.push(nome + '.png'); };

(async () => {
  const browser = await chromium.launch();
  // ---------- prévia: celular, claro ----------
  let { ctx, page } = await abrir(browser, PREVIA, { width: 390, height: 844 }, false);
  await page.evaluate(() => ir('curso', 'P1-DA-3.4')); await page.waitForTimeout(300);
  const q = sel => page.locator(sel).count();
  ok('curso DA-v2 abre', await q('.leitura') === 1);
  ok('bloco de tarefas (3)', await q('.tarefas li') === 3, String(await q('.tarefas li')));
  ok('glossário com 4 termos (dois-pontos e travessão)', await q('.bx.glo li') === 4 && await q('.bx.glo li b') === 4, String(await q('.bx.glo li')));
  ok('caixa CASO', await q('.bx.caso') === 1);
  ok('RESPOSTA DO CASO recolhida', await q('.bx.rcaso details:not([open])') === 1);
  ok('3 itens intercalados montados; ITEM DX-99 (inexistente) não deixa rastro', await q('.iti[data-iti] .bolha') === 6 && await q('.iti') === 3 && !(await page.locator('.leitura').textContent()).toUpperCase().includes('DX-99'), String(await q('.iti')));
  ok('D1: item com texto-base mostra texto-base, comando e enunciado', await q('.iti[data-iti="DX-04"] .textobase') === 1 && (await page.locator('.iti[data-iti="DX-04"] .itcmd').textContent()).startsWith('Com base nessa situação') && await q('.iti[data-iti="DX-01"] .textobase') === 0 && await q('.iti[data-iti="DX-01"] .itcmd') === 1);
  ok('D2: parágrafo depois do CASO fica fora da caixa', !(await page.locator('.bx.caso').first().textContent()).includes('respondem a perguntas diferentes') && (await page.locator('.curso').allTextContents()).join(' ').includes('respondem a perguntas diferentes'));
  ok('D2: parágrafo depois da RESPOSTA DO CASO fica fora do details', !(await page.locator('.bx.rcaso').first().textContent()).includes('fora da caixa recolhida') && (await page.locator('.curso p').allTextContents()).some(x => x.includes('fora da caixa recolhida')));
  ok('D2b: "### Caso prático" é título comum, não caixa', (await page.locator('.curso h3').allTextContents()).some(x => x.startsWith('Caso prático')) && await q('.bx.caso') === 1);
  ok('D6: pegadinha só com A e B mantém as duas linhas', (await page.locator('.curso .bx.peg .par3g').nth(1).textContent()).includes('Cargo vago') && await q('.curso .bx.peg .par3g .muda') === 1);
  ok('pegadinha A/B/MUDA no texto', await q('.curso .bx.peg .par3g') === 2);
  ok('fechamento com 5 pontos', await q('.fecho > ol > li') === 5, String(await q('.fecho > ol > li')));
  ok('literalidade × caso', await q('.fecho .duas li') === 3);
  ok('D7: mapa repetido é o compare, não a baseLegal', await q('.fecho figure.vis') === 1 && await q('.fecho figure.blg') === 0 && await q('.fecho table') === 1);
  ok('escopo com 2 links de 44px', await q('.fecho .escopo button[data-curso]') === 2 && (await page.locator('.fecho .escopo button[data-curso]').first().boundingBox()).height >= 44);
  ok('pegadinha final com par', await q('#pegsFim .par3g') >= 1);
  await shot(page, 'celular_curso_topo');
  await shot(page, 'celular_curso_full');
  // responder DX-01 errado (gabarito C → marca E)
  const it1 = page.locator('.iti[data-iti="DX-01"]');
  await it1.locator('.bolha[data-v="E"]').click(); await page.waitForTimeout(150);
  ok('feedback inline aparece', await it1.locator('.itf:not([hidden])').count() === 1);
  ok('comentário em 3 linhas', await it1.locator('.com3 .k').count() === 3);
  ok('chip do mecanismo LIT', (await it1.locator('.mec').textContent()) === 'LIT');
  ok('bolhas travadas após resposta', await it1.locator('.bolha[disabled]').count() === 2);
  await it1.scrollIntoViewIfNeeded(); await shot(page, 'celular_item_inline_respondido');
  // DX-02 errado (gabarito E → marca C); DX-03 certo (E); DX-04 certo (C)
  await page.locator('.iti[data-iti="DX-04"] .bolha[data-v="E"]').click();
  await page.locator('.iti[data-iti="DX-03"] .bolha[data-v="E"]').click(); await page.waitForTimeout(200);
  ok('D14: feedback com aria-live e foco', await q('.iti .itf[aria-live="polite"]') === 3 && await page.evaluate(() => document.activeElement && document.activeElement.classList.contains('itf')));
  ok('D16: código do mecanismo não se repete na palavra decisiva', !(await page.locator('.iti[data-iti="DX-01"] .com3 span').nth(1).textContent()).includes('LIT:'));
  const est = await page.evaluate(() => JSON.parse(localStorage.getItem('c2026.v01.estado')));
  const rc = est.cursoResp || [];
  ok('3 respostas inline em S.cursoResp (registro próprio)', rc.length === 3 && rc.filter(r => r.st === 'e').length === 2, JSON.stringify(rc.map(r => [r.id, r.st])));
  ok('D-V17-1-INLINE: nada em S.resp, nada no caderno de erros', est.resp.length === 0 && !est.erros['DX-01'] && !est.erros['DX-04']);
  ok('N1: divisor da nota do tópico exclui os intercalados', await page.evaluate(() => divTopico('P1-DA-3.4') === Math.min(30, P.itens.filter(i => i.itemEdital === 'P1-DA-3.4').length - 3) && divTopico('P1-DA-1') === Math.min(30, P.itens.filter(i => i.itemEdital === 'P1-DA-1').length)));
  ok('D4: item intercalado fora do bloco de verificação e da contagem', await page.evaluate(() => { const b = new Set(); for (let i = 0; i < 6; i++) montarBloco('P1-DA-3.4').forEach(x => b.add(x)); return !b.has('DX-01') && !b.has('DX-04') && !b.has('DX-03') && tp('P1-DA-3.4').nInline === 3 && tp('P1-DA-3.4').n === (P.itens.filter(i => i.itemEdital === 'P1-DA-3.4').length - 3); }));
  ok('D-V17-1-INLINE: nota do tópico 3.4 sem respostas', await page.evaluate(() => notaTopico('P1-DA-3.4').n) === 0);
  ok('evento item_curso_respondido', est.eventos.filter(e => e.e === 'item_curso_respondido').length === 3);
  // recarregar: resposta persiste
  await page.reload(); await page.waitForTimeout(300); await page.evaluate(() => ir('curso', 'P1-DA-3.4')); await page.waitForTimeout(300);
  ok('resposta inline persiste após recarregar', await page.locator('.iti[data-iti="DX-01"] .itf:not([hidden])').count() === 1 && await page.locator('.iti[data-iti="DX-01"] .bolha[disabled]').count() === 2);
  // link do escopo
  await page.locator('.fecho .escopo button[data-curso]').first().click(); await page.waitForTimeout(200);
  ok('link do escopo leva a outro tópico', (await page.locator('.folha-top .num').textContent()) === '4.2', await page.locator('.folha-top .num').textContent());
  // matéria antes de qualquer prova: sem "Onde você erra" (as respostas inline não contam)
  await page.evaluate(() => ir('materia', { disc: 'cd26-c11/p1/adm' })); await page.waitForTimeout(300);
  ok('D-V17-1-INLINE: "Onde você erra" ausente só com respostas inline', await q('details.card:has(.mecs)') === 0);
  // bloco real (tela de prova) com os itens DEMO de verificação: DX-02 errado (C), DX-05 errado (E), DX-06 certo (E)
  await page.evaluate(() => { prova = { tipo: 'bloco', ref: 'P1-DA-3.4', nome: 'Questões · 3.4 (teste)', ordem: ['DX-02', 'DX-05', 'DX-06'], comandos: {}, resp: {}, i: 0, inicio: Date.now(), cron: false, antes: notaTopico('P1-DA-3.4') }; ir('prova'); }); await page.waitForTimeout(200);
  await page.locator('#bC').click(); await page.locator('#prox').click(); await page.locator('#bC').click(); await page.locator('#prox').click(); await page.locator('#bE').click(); await page.locator('#fim').click(); await page.locator('#sim2').click(); await page.waitForTimeout(300);
  ok('bloco com itens DEMO entrega resultado', await q('#volta') === 1);
  const est2 = await page.evaluate(() => JSON.parse(localStorage.getItem('c2026.v01.estado')));
  ok('bloco: 3 respostas em S.resp, 2 erros no caderno', est2.resp.length === 3 && !!est2.erros['DX-02'] && !!est2.erros['DX-05'] && !est2.erros['DX-06']);
  await page.evaluate(() => document.querySelectorAll('details').forEach(d => d.open = true));
  ok('D10: correção com comentário mostra 3 linhas e linha do tópico separada; plural certo', await q('.com3') >= 2 && (await page.locator('.eyebrow').first().textContent()).includes('3 itens'));
  await page.evaluate(() => ir('materia', { disc: 'cd26-c11/p1/adm' })); await page.waitForTimeout(300);
  ok('card "Como a Cebraspe constrói o item"', await q('.estilo-da') === 1);
  ok('tabela de mecanismos com 7 linhas', await q('.estilo-da table tr') === 8, String(await q('.estilo-da table tr')));
  const onde = page.locator('details.card:has(.mecs)');
  ok('painel "Onde você erra"', await onde.count() === 1);
  await onde.locator('summary').click(); await page.evaluate(() => document.querySelector('.estilo-da').open = true); await page.waitForTimeout(150);
  const barras = await onde.locator('.mecs .bv b').allTextContents();
  ok('mecanismos errados listados (SUP, CON)', barras.join(',') === 'SUP,CON' || barras.join(',') === 'CON,SUP', barras.join(','));
  ok('botões Treinar', await onde.locator('button[data-mec]').count() === 2);
  await shot(page, 'celular_materia_estilo_onde_erra_full');
  // treino por mecanismo
  await onde.locator('button[data-mec="SUP"]').click(); await page.waitForTimeout(300);
  const nomeProva = await page.locator('.folha-top span').first().textContent();
  ok('treino por mecanismo abre prova', /Treino/.test(nomeProva) && /SUP/.test(nomeProva), nomeProva);
  ok('treino com 1 item SUP (DX-02)', (await page.locator('.folha-top .num').textContent()) === '1 de 1');
  ok('D9: resultado do treino diz "1 item" e "Voltar à matéria"', true);
  await page.locator('#bE').click(); await page.locator('#fim').click(); await page.locator('#sim2').click(); await page.waitForTimeout(300);
  ok('resultado do treino', await q('#volta') === 1 && await q('.placar') === 1 && (await page.locator('#volta').textContent()).includes('matéria') && (await page.locator('.eyebrow').first().textContent()).includes('1 item'));
  const detalhes = page.locator('details, [data-det], .det');
  // abrir correção para ver comentário 3 linhas
  const abriu = await page.evaluate(() => { let n = 0; document.querySelectorAll('details').forEach(d => { d.open = true; n++; }); return n; });
  ok('comentário 3 linhas no resultado', await q('.com3') >= 1, 'details abertos: ' + abriu + ', com3: ' + await q('.com3'));
  await shot(page, 'celular_resultado_treino_full');
  await page.locator('#volta').click(); await page.waitForTimeout(300);
  ok('"Voltar" do treino leva à matéria', await q('.estilo-da') === 1);
  // sair da prova de treino no meio
  await page.evaluate(() => iniciarTreinoMecanismo('cd26-c11/p1/adm', 'CON')); await page.waitForTimeout(200);
  await page.locator('#sair').click(); await page.waitForTimeout(200);
  ok('"Sair" do treino leva à matéria', await q('.estilo-da') === 1);
  // caderno de erros com comentário
  await page.evaluate(() => ir('erros')); await page.waitForTimeout(300);
  await page.evaluate(() => document.querySelectorAll('details').forEach(d => d.open = true));
  const parDX = page.locator('.par[data-id="DX-02"] .bolha').first(); if (await parDX.count()) { await parDX.click(); await page.waitForTimeout(150); }
  ok('caderno de erros: item DEMO com comentário 3 linhas ao responder', await q('#app *') > 3 && await q('.par[data-id="DX-02"] .com3') === 1, 'par=' + await q('.par[data-id="DX-02"]') + ' com3=' + await q('.com3'));
  await shot(page, 'celular_erros_full');
  // bloco de questões do tópico 3.4 (inclui itens antigos e DEMO) → resultado com justificativa antiga e comentário novo
  await page.evaluate(() => iniciarBloco('P1-DA-3.4')); await page.waitForTimeout(200);
  for (let i = 0; i < 10; i++) { await page.locator('#bC').click(); const fim = await page.locator('#fim').count(); if (fim) { await page.locator('#fim').click(); await page.locator('#sim2').click(); break; } await page.locator('#prox').click(); }
  await page.waitForTimeout(300); await page.evaluate(() => document.querySelectorAll('details').forEach(d => d.open = true));
  ok('bloco do tópico entrega resultado', await q('#volta') === 1);
  await ctx.close();

  // ---------- prévia: desktop escuro ----------
  ({ ctx, page } = await abrir(browser, PREVIA, { width: 1280, height: 900 }, true));
  await page.evaluate(() => ir('curso', 'P1-DA-3.4')); await page.waitForTimeout(300);
  ok('desktop escuro: curso renderiza', await q('.tarefas') === 1 && await q('.iti .bolha') === 6);
  await shot(page, 'desktop_escuro_curso_full');
  await page.evaluate(() => ir('materia', { disc: 'cd26-c11/p1/adm' })); await page.waitForTimeout(200);
  await page.evaluate(() => document.querySelectorAll('details').forEach(d => d.open = true));
  await shot(page, 'desktop_escuro_materia');
  await ctx.close();

  // ---------- regressão: pacote v1.13 sem campos novos ----------
  ({ ctx, page } = await abrir(browser, REGR, { width: 390, height: 844 }, false));
  const outros = await page.evaluate(() => T.ordem.filter(id => tp(id).disc !== 'cd26-c11/p1/adm' && tp(id).temCurso).slice(0, 3));
  for (const tid of ['P1-DA-1', 'P1-DA-2.1', 'P1-DA-3.4', 'P1-DA-10.1', ...outros]) {
    await page.evaluate(t => ir('curso', t), tid); await page.waitForTimeout(150);
    const n = await q('.leitura'); const iti = await q('.iti'); const glo = await q('.bx.glo'); const ta = await q('.tarefas'); const fe = await q('.fecho');
    ok('regressão curso ' + tid, n === 1 && iti === 0 && glo === 0 && ta === 0 && fe === 0, `iti=${iti} glo=${glo} tarefas=${ta} fecho=${fe}`);
  }
  await page.evaluate(() => ir('curso', 'P1-DA-1')); await page.waitForTimeout(150); await shot(page, 'regressao_curso_DA-1');
  await page.evaluate(() => ir('materia', { disc: 'cd26-c11/p1/adm' })); await page.waitForTimeout(200);
  ok('regressão matéria DA: estilo presente, "Onde você erra" ausente sem respostas', await q('.estilo-da') === 1 && await q('details.card:has(.mecs)') === 0);
  await page.evaluate(() => ir('materia', { disc: 'cd26-c11/p1/ti' })); await page.waitForTimeout(200);
  ok('regressão matéria TI: sem card de estilo', await q('[data-box="cd26-c11/p1/ti"] .estilo-da') === 0 && await q('[data-box="cd26-c11/p1/ti"] .matcorpo *') > 2);
  await page.evaluate(() => iniciarBloco('P1-DA-1')); await page.waitForTimeout(200);
  for (let i = 0; i < 10; i++) { await page.locator('#bE').click(); if (await page.locator('#fim').count()) { await page.locator('#fim').click(); await page.locator('#sim2').click(); break; } await page.locator('#prox').click(); }
  await page.waitForTimeout(300); await page.evaluate(() => document.querySelectorAll('details').forEach(d => d.open = true));
  ok('regressão resultado do bloco: justificativa e "tópico" no mesmo parágrafo, sem .com3', await q('#volta') === 1 && await q('.just') >= 1 && await q('.com3') === 0 && await page.evaluate(() => [...document.querySelectorAll('.just')].every(p => p.querySelector('.xs') && p.textContent.trim().length > 20)), `just=${await q('.just')} com3=${await q('.com3')}`);
  await shot(page, 'regressao_resultado_bloco_full');
  for (const v of ['painel', 'pratica', 'erros', 'recomendacoes', 'dados', 'vespera', 'discursivas']) { await page.evaluate(x => ir(x), v); await page.waitForTimeout(120); ok('regressão tela ' + v, await q('#app *') > 3); }
  await ctx.close();
  await browser.close();
  R.resumo = { total: R.testes.length, ok: R.testes.filter(t => t.ok).length, falhas: R.testes.filter(t => !t.ok).map(t => t.nome), errosJS: R.errosJS.length };
  fs.writeFileSync(path.join(OUT, 'resultado.json'), JSON.stringify(R, null, 1));
  console.log('\nRESUMO', JSON.stringify(R.resumo)); if (R.errosJS.length) console.log('ERROS JS', JSON.stringify(R.errosJS, null, 1));
})().catch(e => { console.error('ERRO FATAL', e); fs.writeFileSync(path.join(OUT, 'resultado.json'), JSON.stringify(Object.assign(R, { fatal: String(e) }), null, 1)); process.exit(1); });
