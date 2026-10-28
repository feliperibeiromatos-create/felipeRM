// t_refazer.js — D-INLINE-REFAZER (T-140), v17.2: botão "Refazer" no item intercalado. Uso: node t_refazer.js <previa_demo.html> <saida.json>
const { chromium, abrir } = require('./lib.js');
const fs = require('fs');
const [,, ARQ, OUT] = process.argv;
(async () => {
  const browser = await chromium.launch(); const tudo = {}; let falhas = 0, errosJS = 0;
  for (const [tag, vp, escuro] of [['cel-claro', { width: 390, height: 844 }, false], ['desk-escuro', { width: 1280, height: 900 }, true]]) {
    const { page, erros, ctx } = await abrir(browser, ARQ, { vp, escuro });
    const tInl = await page.evaluate(() => Object.keys(T.top).find(t => idsInline(t).size && tp(t).temCurso) || null);
    const R = [];
    if (!tInl) { R.push({ caso: 'setup', ok: false, det: 'sem tópico com ITEM intercalado' }); }
    else {
      await page.evaluate(t => { S.resp = []; S.erros = {}; S.cursoResp = []; _divP = null; salvar(); ir('curso', t); }, tInl);
      const iid = await page.evaluate(t => [...idsInline(t)][0], tInl);
      const sel = `.iti[data-iti="${iid}"]`;
      const g = await page.evaluate(id => M[id].gabarito, iid); const errado = g === 'C' ? 'E' : 'C';
      // 1. antes de responder: sem botão Refazer
      R.push({ caso: '1.sem_botao_antes', ok: (await page.locator(`${sel} [data-refazer]`).count()) === 0, det: '' });
      // 2. responde errado: feedback + botão Refazer visível; bolhas desabilitadas; 1 registro em cursoResp; S.resp vazio
      await page.locator(`${sel} .bolha[data-v="${errado}"]`).click(); await page.waitForTimeout(100);
      let st = await page.evaluate(id => ({ f: !app().querySelector(`.iti[data-iti="${id}"] .itf`).hidden, btn: !!app().querySelector(`.iti[data-iti="${id}"] [data-refazer]`), dis: [...app().querySelectorAll(`.iti[data-iti="${id}"] .bolha`)].every(b => b.disabled), cr: S.cursoResp.length, resp: S.resp.length, ult: respostaInline(id) && respostaInline(id).st }), iid);
      R.push({ caso: '2.responde_errado', ok: st.f && st.btn && st.dis && st.cr === 1 && st.resp === 0 && st.ult === 'e', det: JSON.stringify(st) });
      // 3. clica Refazer: feedback some, bolhas reativadas e sem cor, registro anterior mantido, evento gravado
      const nEv = await page.evaluate(() => (S.eventos || []).length);
      await page.locator(`${sel} [data-refazer]`).click(); await page.waitForTimeout(100);
      st = await page.evaluate(id => ({ f: app().querySelector(`.iti[data-iti="${id}"] .itf`).hidden, btn: !!app().querySelector(`.iti[data-iti="${id}"] [data-refazer]`), dis: [...app().querySelectorAll(`.iti[data-iti="${id}"] .bolha`)].some(b => b.disabled), cor: [...app().querySelectorAll(`.iti[data-iti="${id}"] .bolha`)].some(b => b.classList.contains('okk') || b.classList.contains('err')), cr: S.cursoResp.length, ev: (S.eventos || []).slice(-1)[0] && (S.eventos || []).slice(-1)[0].tipo, foco: document.activeElement && document.activeElement.classList.contains('bolha') }), iid);
      R.push({ caso: '3.refazer', ok: st.f && !st.btn && !st.dis && !st.cor && st.cr === 1 && st.foco, det: JSON.stringify(st) });
      // 4. responde certo: novo registro (2), último = c; Refazer de novo disponível; S.resp continua vazio; nota do tópico não muda
      await page.locator(`${sel} .bolha[data-v="${g}"]`).click(); await page.waitForTimeout(100);
      st = await page.evaluate(({ id, t }) => ({ cr: S.cursoResp.length, ult: respostaInline(id).st, btn: !!app().querySelector(`.iti[data-iti="${id}"] [data-refazer]`), resp: S.resp.length, nt: notaTopico(t).n, erros: Object.keys(S.erros).length, ok: /Certo\./.test(app().querySelector(`.iti[data-iti="${id}"] .itf`).innerText) }), { id: iid, t: tInl });
      R.push({ caso: '4.responde_certo', ok: st.cr === 2 && st.ult === 'c' && st.btn && st.resp === 0 && st.nt === 0 && st.erros === 0 && st.ok, det: JSON.stringify(st) });
      // 5. recarrega o curso: estado restaurado pela última resposta (certo) e Refazer disponível mesmo sem clique nesta visita
      await page.evaluate(t => { ir('painel'); ir('curso', t); }, tInl); await page.waitForTimeout(150);
      st = await page.evaluate(id => ({ btn: !!app().querySelector(`.iti[data-iti="${id}"] [data-refazer]`), okk: !!app().querySelector(`.iti[data-iti="${id}"] .bolha.okk`), dis: [...app().querySelectorAll(`.iti[data-iti="${id}"] .bolha`)].every(b => b.disabled) }), iid);
      R.push({ caso: '5.restaurado', ok: st.btn && st.okk && st.dis, det: JSON.stringify(st) });
      // 6. refazer após restauração funciona (onclick religado)
      await page.locator(`${sel} [data-refazer]`).click(); await page.waitForTimeout(80); await page.locator(`${sel} .bolha[data-v="${errado}"]`).click(); await page.waitForTimeout(80);
      st = await page.evaluate(id => ({ cr: S.cursoResp.length, ult: respostaInline(id).st, resp: S.resp.length }), iid);
      R.push({ caso: '6.refazer_pos_restauracao', ok: st.cr === 3 && st.ult === 'e' && st.resp === 0, det: JSON.stringify(st) });
      // 7. captura
      const el = page.locator(sel).first(); await el.scrollIntoViewIfNeeded(); await el.screenshot({ path: `${tag}_el_item_refazer.png` });
      // 8. o item intercalado continua fora do bloco de 10 e do divisor
      st = await page.evaluate(({ id, t }) => ({ noBloco: montarBloco(t).includes(id), k: notaTopico(t).k, banco: P.itens.filter(i => i.itemEdital === t).length, inl: idsInline(t).size }), { id: iid, t: tInl });
      R.push({ caso: '8.fora_do_bloco', ok: !st.noBloco && st.k === Math.min(20, st.banco - st.inl), det: JSON.stringify(st) });
    }
    const f = R.filter(x => !x.ok).length; falhas += f; errosJS += erros.length; tudo[tag] = { casos: R, errosJS: erros, topico: tInl };
    console.log(`== ${tag} (${tInl}) ==`); R.forEach(x => console.log((x.ok ? 'OK  ' : 'FALHA') + ' ' + x.caso + ' — ' + x.det)); console.log(`${R.length - f}/${R.length} OK · erros JS ${erros.length}`);
    await ctx.close();
  }
  fs.writeFileSync(OUT, JSON.stringify({ arquivo: ARQ, combos: tudo, falhas, errosJS }, null, 1));
  await browser.close(); process.exit(falhas || errosJS ? 1 : 0);
})();
