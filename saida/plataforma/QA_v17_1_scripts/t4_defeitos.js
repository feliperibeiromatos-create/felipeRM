// QA R4: reprodução de D1–D17 na prévia nova (celular claro e desktop escuro), capturas em qa_r5/.
const { chromium, abrir, estado } = require('./lib.js');
const fs = require('fs');
const PREVIA = '/home/claude/plat/plataforma_v17_1_DAv2_previa.html';
const OUT = '/home/claude/plat/qa_r5/';
const R = { ok: [], falha: [], info: {} };
const ok = (n, c, d) => { const s = n + (d !== undefined ? ' — ' + (typeof d === 'string' ? d : JSON.stringify(d)) : ''); (c ? R.ok : R.falha).push(s); console.log((c ? 'OK    ' : 'FALHA ') + s); };
const lum = `const lum=c=>{const m=c.match(/[\\d.]+/g).map(Number);const [r,g,b]=m.slice(0,3).map(v=>{v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4)});return 0.2126*r+0.7152*g+0.0722*b};`;
(async () => {
  const browser = await chromium.launch();
  for (const modo of [{ nome: 'cel', vp: { width: 390, height: 844 }, escuro: false }, { nome: 'desk', vp: { width: 1280, height: 900 }, escuro: true }]) {
    const pre = modo.nome + ': ';
    const { page, erros } = await abrir(browser, PREVIA, modo);
    await page.evaluate(() => ir('curso', 'P1-DA-3.4')); await page.waitForTimeout(200);
    const el = async (loc, nome) => { if (await loc.count()) { await loc.first().scrollIntoViewIfNeeded(); await loc.first().screenshot({ path: OUT + modo.nome + '_' + nome + '.png' }); } };
    // D1
    const d1 = await page.evaluate(() => { const g = id => { const d = document.querySelector(`.iti[data-iti="${id}"]`); return d ? { tb: !!d.querySelector('.textobase'), tbTxt: (d.querySelector('.textobase') || {}).textContent || '', cmd: (d.querySelector('.itcmd') || {}).textContent || '', ord: [...d.children].map(c => c.className).join('>') } : null; }; return { itis: [...document.querySelectorAll('.iti')].map(d => d.dataset.iti), dx04: g('DX-04'), dx01: g('DX-01') }; });
    ok(pre + 'D1 DX-04 com texto-base e comando, na ordem texto-base > comando > enunciado', d1.dx04 && d1.dx04.tb && /Poder Legislativo/.test(d1.dx04.tbTxt) && /situação hipotética/.test(d1.dx04.cmd) && /textobase.*itcmd.*ite/.test(d1.dx04.ord), d1.dx04);
    ok(pre + 'D1 DX-01 com comando', d1.dx01 && /julgue/i.test(d1.dx01.cmd), d1.dx01 && d1.dx01.cmd);
    await el(page.locator('.iti[data-iti="DX-04"]'), 'D1_item_DX04_textobase');
    // D11 (DX-99 inexistente)
    ok(pre + 'D11 ITEM DX-99 inexistente não renderiza; intercalados = DX-01, DX-04, DX-03', JSON.stringify(d1.itis) === '["DX-01","DX-04","DX-03"]', d1.itis);
    // D2 / D2b / D12
    const d2 = await page.evaluate(() => { const ps = [...document.querySelectorAll('.curso p, .curso h3')]; const onde = t => { const p = ps.find(x => x.textContent.includes(t)); return !p ? 'não achado' : p.closest('details') ? 'DENTRO do details' : p.closest('.bx') ? 'dentro de ' + p.closest('.bx').className : 'fora (' + p.tagName + ')'; };
      const caso = document.querySelectorAll('.bx.caso'); const glo = [...document.querySelectorAll('.bx.glo li')].map(l => l.innerHTML);
      return { aposCaso: onde('Os dois institutos respondem'), aposResposta: onde('Esse parágrafo vem depois da resposta'), tituloCaso: onde('Caso prático: redistribuição'), aposTitulo: onde('Este título começa por'), nCaso: caso.length, glo, nRcaso: document.querySelectorAll('.bx.rcaso').length }; });
    ok(pre + 'D2 parágrafo depois do CASO fora da caixa', d2.aposCaso === 'fora (P)', d2.aposCaso);
    ok(pre + 'D2 parágrafo depois da RESPOSTA DO CASO visível, fora do details', d2.aposResposta === 'fora (P)', d2.aposResposta);
    ok(pre + 'D2b "### Caso prático" continua título (h3) e parágrafo seguinte fora de caixa', d2.tituloCaso === 'fora (H3)' && d2.aposTitulo === 'fora (P)' && d2.nCaso === 1, d2);
    ok(pre + 'D12 glossário aceita "Quadro — definição" (4 termos em negrito)', d2.glo.length === 4 && d2.glo.every(h => /^<b>/.test(h)) && d2.glo.some(h => /<b>Quadro:<\/b>/.test(h)), d2.glo.map(h => h.slice(0, 40)));
    await el(page.locator('.bx.caso'), 'D2_caso'); await page.evaluate(() => { const d = document.querySelector('.bx.caso'); d.nextElementSibling && d.nextElementSibling.scrollIntoView({ block: 'center' }); });
    await page.screenshot({ path: OUT + modo.nome + '_D2_caso_paragrafo_fora.png' });
    await el(page.locator('.bx.rcaso'), 'D2_rcaso_fechada');
    await page.evaluate(() => { const r = document.querySelector('.bx.rcaso'); r.scrollIntoView({ block: 'start' }); window.scrollBy(0, -80); });
    await page.screenshot({ path: OUT + modo.nome + '_D2_rcaso_paragrafo_fora.png' });
    await page.evaluate(() => { const h = [...document.querySelectorAll('.curso h3')].find(x => /Caso prático/.test(x.textContent)); h.scrollIntoView({ block: 'center' }); });
    await page.screenshot({ path: OUT + modo.nome + '_D2b_titulo_caso.png' });
    await el(page.locator('.bx.glo'), 'D12_glossario');
    // D6
    const d6 = await page.evaluate(() => { const b = [...document.querySelectorAll('.curso .bx.peg')].find(x => /sem a linha MUDA/.test(x.innerText)); return b ? { par: b.querySelectorAll('.par3g').length, ks: [...b.querySelectorAll('.par3g .k')].map(k => k.textContent), txt: b.innerText.replace(/\s+/g, ' ').slice(0, 200) } : null; });
    ok(pre + 'D6 pegadinha só A/B: quadro com A e B, sem Muda, texto preservado', d6 && d6.par === 1 && d6.ks.join() === 'A,B' && /Cargo ocupado/.test(d6.txt) && /Cargo vago/.test(d6.txt), d6);
    await el(page.locator('.curso .bx.peg', { hasText: 'sem a linha MUDA' }), 'D6_pegadinha_so_AB');
    // D7 / D8 / D15
    const d7 = await page.evaluate(() => { const f = document.querySelector('.fecho'); const fig = f && f.querySelector('figure'); return { fig: fig ? fig.className + ' | ' + (fig.querySelector('.vt') || {}).textContent : null, links: [...document.querySelectorAll('.escopo button')].map(b => { const r = b.getBoundingClientRect(); return [b.textContent, Math.round(r.width), Math.round(r.height), b.getAttribute('aria-label')]; }) }; });
    ok(pre + 'D7 "O que você já sabe" repete o compare (não a Base Legal)', d7.fig && /Remoção × redistribuição/.test(d7.fig) && !/blg/.test(d7.fig), d7.fig);
    ok(pre + 'D15 links do escopo >= 44 px', d7.links.length === 2 && d7.links.every(l => l[2] >= 44 && l[1] >= 44), d7.links);
    await el(page.locator('.fecho'), 'D7_fechamento');
    await el(page.locator('.escopo'), 'D15_escopo');
    const hs = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    ok(pre + 'sem rolagem horizontal no curso', hs <= 0, hs);
    // D14 / D16: responder DX-04 errado pelo teclado
    await page.locator('.iti[data-iti="DX-04"] .bolha[data-v="E"]').focus(); await page.keyboard.press('Enter'); await page.waitForTimeout(150);
    const d14 = await page.evaluate(() => { const d = document.querySelector('.iti[data-iti="DX-04"]'); const f = d.querySelector('.itf'); const a = document.activeElement; return { role: f.getAttribute('role'), live: f.getAttribute('aria-live'), focoNoFeedback: a === f, foco: a.tagName + '.' + a.className, frase: /Procure a troca/.test(f.innerText), dec: (d.querySelector('.com3 span:nth-child(2)') || {}).textContent }; });
    ok(pre + 'D14 feedback com role=status, aria-live=polite e foco no feedback', d14.role === 'status' && d14.live === 'polite' && d14.focoNoFeedback, d14);
    ok(pre + 'D14 frase de leitura do mecanismo no feedback (adendo §5.1)', d14.frase);
    ok(pre + 'D16 "AP: ..." não repete o código', d14.dec && !/^APAP|AP\s*:/.test(d14.dec.replace(/\s/g, '')) , d14.dec);
    const ring = await page.evaluate(() => { const a = document.activeElement, s = getComputedStyle(a); return s.outlineStyle + ' ' + s.outlineWidth; });
    R.info[pre + 'contorno do feedback com foco'] = ring;
    await el(page.locator('.iti[data-iti="DX-04"]'), 'D14_item_DX04_respondido');
    // Tab depois de responder: vai para o próximo elemento após o item
    await page.keyboard.press('Tab'); const prox = await page.evaluate(() => { const a = document.activeElement; return a.closest('.iti') ? a.closest('.iti').dataset.iti + ':' + a.dataset.v : a.tagName + '.' + a.className + ' ' + (a.textContent || '').slice(0, 30); });
    R.info[pre + 'Tab depois de responder DX-04'] = prox;
    // contraste dos novos elementos (itcmd, textobase, frase)
    const cs = await page.evaluate(lum + `(()=>{const bgOf=el=>{while(el){const b=getComputedStyle(el).backgroundColor;if(b&&!/rgba\\(0, 0, 0, 0\\)|transparent/.test(b))return b;el=el.parentElement}return getComputedStyle(document.body).backgroundColor};return ['.iti .itcmd','.iti .textobase','.iti .itf .xs','.escopo .esc-link','.par3g .k'].map(s=>{const e=document.querySelector(s);if(!e)return [s,null];const a=lum(getComputedStyle(e).color),b=lum(bgOf(e));return [s,Math.round((Math.max(a,b)+0.05)/(Math.min(a,b)+0.05)*100)/100]})})()`);
    ok(pre + 'contraste >= 4,5 nos elementos novos da R4', cs.every(c => c[1] === null || c[1] >= 4.5), cs);
    // D-V17-1-INLINE de novo
    for (const [id, v] of [['DX-01', 'E'], ['DX-03', 'E']]) await page.locator(`.iti[data-iti="${id}"] .bolha[data-v="${v}"]`).click();
    let st = await estado(page);
    ok(pre + 'INLINE: 3 em S.cursoResp, S.resp e S.erros vazios, nota 3.4 n=0', (st.cursoResp || []).length === 3 && st.resp.length === 0 && Object.keys(st.erros).length === 0 && await page.evaluate(() => notaTopico('P1-DA-3.4').n) === 0, (st.cursoResp || []).map(r => r.id + r.st));
    await page.reload(); await page.waitForTimeout(250); await page.evaluate(() => ir('curso', 'P1-DA-3.4'));
    ok(pre + 'INLINE: persistem após recarregar', await page.evaluate(() => [...document.querySelectorAll('.iti')].every(d => !d.querySelector('.itf').hidden)));
    // D3 card
    await page.evaluate(() => { UI.mat.clear(); ir('materia', { disc: 'cd26-c11/p1/adm' }); const d = document.querySelector('details.estilo-da'); d.open = true; });
    const d3 = await page.evaluate(() => document.querySelector('details.estilo-da').innerText);
    ok(pre + 'D3 card sem a frase invertida e com a coluna corrigida', !/item certo é quase sempre/i.test(d3) && /Quando o item reescreve a lei ou a tese com fidelidade, quase sempre é Certo/.test(d3) && /na maioria Errado/.test(d3) && /tende a Errado/.test(d3) && /amostra pequena/.test(d3), d3.split('\n').filter(l => /Errado|Certo/.test(l)).slice(0, 12));
    ok(pre + 'INLINE: matéria sem "Onde você erra"', !/Onde você erra/.test(await page.evaluate(() => app().innerText)));
    await el(page.locator('details.estilo-da'), 'D3_card_estilo');
    // D4: o.n, botão, blocos
    const d4 = await page.evaluate(() => { const o = tp('P1-DA-3.4'); return { n: o.n, nInline: o.nInline, div: divTopico(o.id), totalBanco: P.itens.filter(i => i.itemEdital === o.id).length }; });
    R.info[pre + 'D4 contagens'] = d4;
    await page.evaluate(() => ir('curso', 'P1-DA-3.4'));
    const btn = await page.evaluate(() => (document.getElementById('praticar') || {}).textContent);
    ok(pre + 'D4 "Resolver N questões" sem os intercalados', d4.n === d4.totalBanco - 3 && new RegExp('Resolver ' + Math.min(10, d4.n)).test(btn), { btn, ...d4 });
    const vistos = new Set(); let inl = []; let rod = 0;
    while (rod < 6) { rod++; await page.evaluate(() => ir('curso', 'P1-DA-3.4')); await page.locator('#praticar').click(); const n = await page.evaluate(() => prova.ordem.length);
      for (let k = 0; k < n; k++) { const it = await page.evaluate(() => { const it = M[prova.ordem[prova.i]]; return { id: it.id, g: it.gabarito }; }); vistos.add(it.id); await page.locator('#b' + it.g).click(); if (k < n - 1) await page.locator('#prox').click(); else { await page.locator('#fim').click(); await page.locator('#sim2').click(); } }
      if (rod === 1) { await page.evaluate(() => document.querySelector('.eyebrow').scrollIntoView()); }
    }
    inl = [...vistos].filter(i => ['DX-01', 'DX-03', 'DX-04'].includes(i));
    ok(pre + 'D4 intercalados nunca aparecem no bloco (6 rodadas pela interface)', inl.length === 0 && vistos.has('DX-02') && vistos.has('DX-05') && vistos.has('DX-06'), { distintos: vistos.size, inl });
    // nota máxima possível: tudo certo em todas as rodadas
    const nota = await page.evaluate(() => ({ nt: notaTopico('P1-DA-3.4'), pct: pctTopico(tp('P1-DA-3.4')), div: divTopico('P1-DA-3.4'), n: tp('P1-DA-3.4').n, txt: (() => { ir('materia', { disc: 'cd26-c11/p1/adm' }); const l = document.querySelector('#t-P1-DA-3\\.4 .pc'); return l ? l.textContent : null; })() }));
    R.info[pre + 'nota 3.4 com todos os itens respondidos certo'] = nota;
    ok(pre + 'NOVO: tópico com todas as questões de verificação certas chega a 100%', Math.round(nota.pct * 100) >= 100 || /100/.test(nota.txt || ''), nota);
    await el(page.locator('#t-P1-DA-3\\.4'), 'NOVO_pct_topico_teto');
    // D9: treino com 1 item — precisa de errar DX-05 (CON) num bloco
    await page.evaluate(() => { iniciarBloco('P1-DA-3.4'); prova.ordem = ['DX-05', 'DX-02', 'DX-06']; prova.ordem.forEach(id => prova.resp[id] = M[id].gabarito === 'C' ? 'E' : 'C'); entregar(); UI.mat.clear(); ir('materia', { disc: 'cd26-c11/p1/adm' }); const d = [...document.querySelectorAll('details.card')].find(x => /Onde você erra/.test(x.innerText)); d.open = true; });
    const b1 = await page.evaluate(() => [...document.querySelectorAll('[data-mec]')].map(b => b.dataset.mec));
    await page.locator('[data-mec="' + b1[0] + '"]').click();
    const pv = await page.evaluate(() => prova.ordem);
    await page.evaluate(() => { prova.ordem.forEach(id => prova.resp[id] = M[id].gabarito); entregar(); });
    const d9 = await page.evaluate(() => ({ eyebrow: document.querySelector('.eyebrow').textContent, volta: document.getElementById('volta').textContent }));
    ok(pre + 'D9 resultado do treino: "Voltar à matéria" e plural certo', d9.volta === 'Voltar à matéria' && (pv.length !== 1 || /· 1 item$/.test(d9.eyebrow)), { ...d9, ordem: pv });
    ok(pre + 'D4 treino por mecanismo sem intercalados', !pv.some(i => ['DX-01', 'DX-03', 'DX-04'].includes(i)), pv);
    await page.screenshot({ path: OUT + modo.nome + '_D9_resultado_treino.png' });
    await page.locator('#volta').click(); ok(pre + 'D9 Voltar leva à matéria', await page.evaluate(() => rota.v) === 'materia');
    ok(pre + 'erros de JS', erros.length === 0, erros);
    await page.context().close();
  }
  fs.writeFileSync(OUT + 't4_defeitos.json', JSON.stringify(R, null, 1));
  await browser.close();
})();
