// t_janela20.js — ESPEC v17.2 §4, casos 1–12 (D-V17-2-JANELA-20). R2: itens 6 (clique real), 4 (ordem por t), 10 (varredura de "30" em todas as telas),
// 13 (status no Painel, QA R1 D1), 12 (aviso só com % exibido mudado, D4), 4 combinações de tela × tema. Uso: node t_janela20.js <previa_v17_2.html> <saida.json>
const { chromium, abrir } = require('./lib.js');
const fs = require('fs');
const [,, ARQ, OUT] = process.argv;
const COMBOS = [['cel-claro', { width: 390, height: 844 }, false], ['cel-escuro', { width: 390, height: 844 }, true], ['desk-claro', { width: 1280, height: 900 }, false], ['desk-escuro', { width: 1280, height: 900 }, true]];
(async () => {
  const browser = await chromium.launch(); const tudo = {}; let falhasTot = 0, errosTot = 0;
  for (const [tag, vp, escuro] of COMBOS) {
    const { page, erros, ctx } = await abrir(browser, ARQ, { vp, escuro });
    const r = await page.evaluate((primeira) => {
      const R = []; const ok = (id, cond, det) => R.push({ caso: id, ok: !!cond, det });
      const inl = tid => idsInline(tid);
      const itensDe = tid => P.itens.filter(i => i.itemEdital === tid && !inl(tid).has(i.id));
      const tops = Object.values(T.top).filter(o => o.n).map(o => ({ id: o.id, n: itensDe(o.id).length, curso: !!o.temCurso })).sort((a, b) => b.n - a.n);
      const big = tops.find(t => t.n >= 30 && t.curso) || tops.find(t => t.n >= 25); const small = tops.find(t => t.n >= 10 && t.n <= 15);
      if (!big || !small) return { R: [{ caso: 'setup', ok: false, det: JSON.stringify(tops.slice(0, 5)) }] };
      let T0 = 1700000000000; const reset = () => { S.resp = []; S.erros = {}; S.cursoResp = []; S.top = {}; S.tentativas = []; _divP = null; delete S.avisoV172; T0 = 1700000000000; };
      const resp = (tid, ids, f) => ids.forEach((id, k) => { const g = M[id].gabarito; const st = f(k, g); if (st === 'b') return; S.resp.push({ id, tp: tid, st: st === g ? 'c' : 'e', t: (T0 += 1000) }); }); // t estritamente crescente
      const ids = itensDe(big.id).map(i => i.id), sids = itensDe(small.id).map(i => i.id), ks = sids.length;
      const d = discById(tp(big.id).disc);
      // oráculo independente da regra (ESPEC §1)
      const oraculo = tid => { const ult = {}; S.resp.filter(r => r.tp === tid).forEach(r => { ult[r.id] = r; }); const w = Object.values(ult).sort((a, b) => a.t - b.t).slice(-20); const k = Math.max(1, Math.min(20, itensDe(tid).length)); const c = w.filter(r => r.st === 'c').length, e = w.filter(r => r.st === 'e').length; return { n: w.length, c, e, k, completa: w.length >= k, pct: Math.round(100 * (c - e) / k), ids: w.map(r => r.id) }; };
      const bate = tid => { const o = oraculo(tid), nt = notaTopico(tid); return o.n === nt.n && o.c === nt.c && o.e === nt.e && o.k === nt.k && o.completa === nt.completa && (o.pct < 0 ? '−' + Math.abs(o.pct) : o.pct) + '%' === pctTxt(pctTopico(tp(tid))) && JSON.stringify(o.ids) === JSON.stringify(janela(tid).map(r => r.id)); };
      if (primeira) {
        ok('0.const', JANELA === 20 && BLOCO === 10 && VERSAO_APP === 'v17.2', `JANELA=${JANELA} BLOCO=${BLOCO} ${VERSAO_APP}`);
        reset(); let nt = notaTopico(big.id);
        ok('1.zero', bate(big.id) && nt.n === 0 && nt.k === 20 && !nt.completa && pctTxt(pctTopico(tp(big.id))) === '0%' && statusNota(big.id) === '0 de 20 questões', JSON.stringify(nt) + ' ' + statusNota(big.id));
        reset(); resp(big.id, ids.slice(0, 10), (k, g) => k < 8 ? g : (g === 'C' ? 'E' : 'C')); nt = notaTopico(big.id);
        ok('2.dez', bate(big.id) && nt.c === 8 && nt.e === 2 && pctTxt(pctTopico(tp(big.id))) === '30%' && !nt.completa && statusNota(big.id) === '10 de 20 questões' && !/nota recente/.test(porque(tp(big.id))) && /10 respostas até agora/.test(porque(tp(big.id))), JSON.stringify(nt) + ' | ' + porque(tp(big.id)));
        reset(); resp(big.id, ids.slice(0, 20), (k, g) => k < 15 ? g : (g === 'C' ? 'E' : 'C')); nt = notaTopico(big.id);
        ok('3.vinte', bate(big.id) && nt.completa && nt.nota === 10 && pctTxt(pctTopico(tp(big.id))) === '50%' && statusNota(big.id) === 'nota completa' && /nota recente \+10\/20/.test(porque(tp(big.id))), JSON.stringify(nt) + ' | ' + porque(tp(big.id)));
        // 4. 30 distintas, respondidas em ordem embaralhada de ids: só as 20 mais recentes por t
        reset(); const emb = ids.slice(0, 30).slice().reverse(); resp(big.id, emb.slice(0, 10), (k, g) => (g === 'C' ? 'E' : 'C')); resp(big.id, emb.slice(10, 30), (k, g) => g); nt = notaTopico(big.id);
        const porT = S.resp.filter(r => r.tp === big.id).slice().sort((a, b) => a.t - b.t).slice(-20).map(r => r.id);
        ok('4.trinta', bate(big.id) && nt.n === 20 && nt.c === 20 && nt.e === 0 && pctTxt(pctTopico(tp(big.id))) === '100%' && JSON.stringify(janela(big.id).map(r => r.id)) === JSON.stringify(porT) && JSON.stringify(porT) === JSON.stringify(emb.slice(10, 30)), `banco ${ids.length}; ` + JSON.stringify(nt));
        // 4b. a mais recente por t vence mesmo fora da ordem de inserção
        // 4b. responder de novo uma questão antiga: ela vai para o fim da janela com a resposta nova (n continua 20; a mais antiga restante sai só na 21ª distinta)
        reset(); resp(big.id, ids.slice(0, 21), (k, g) => g); resp(big.id, [ids[0]], (k, g) => (g === 'C' ? 'E' : 'C')); nt = notaTopico(big.id);
        const esperado4b = ids.slice(2, 21).concat([ids[0]]); // ids[1] é agora a mais antiga fora da janela
        ok('4b.reordem', bate(big.id) && nt.n === 20 && nt.e === 1 && JSON.stringify(janela(big.id).map(r => r.id)) === JSON.stringify(esperado4b), JSON.stringify(nt));
        reset(); resp(small.id, sids, (k, g) => g); nt = notaTopico(small.id);
        ok('5a.pequeno_todas', bate(small.id) && nt.k === ks && nt.completa && pctTxt(pctTopico(tp(small.id))) === '100%' && statusNota(small.id) === 'nota completa', `k=${ks} ` + JSON.stringify(nt));
        reset(); resp(small.id, sids.slice(0, 7), (k, g) => g); nt = notaTopico(small.id);
        ok('5b.pequeno_sete', bate(small.id) && nt.n === 7 && !nt.completa && statusNota(small.id) === `7 de ${ks} questões`, JSON.stringify(nt) + ' ' + statusNota(small.id));
        reset(); resp(big.id, ids.slice(0, 10), (k, g) => (g === 'C' ? 'E' : 'C')); resp(big.id, ids.slice(0, 10), (k, g) => g); nt = notaTopico(big.id);
        ok('7.repetida', bate(big.id) && nt.n === 10 && nt.c === 10 && nt.e === 0 && statusNota(big.id) === '10 de 20 questões', JSON.stringify(nt));
        reset(); const m0 = mediaMateria(d), nf0 = notaFinal(); resp(big.id, ids.slice(0, 20), (k, g) => g); const m1 = mediaMateria(d), nf1 = notaFinal();
        const esperadoM = pesoTop(tp(big.id)) / topicosDe(d.id).reduce((a, o) => a + pesoTop(o), 0);
        ok('8.medias', m0 === 0 && Math.abs(m1 - esperadoM) < 1e-9 && Math.abs(nf1 - nf0 - PESO_PROVA[d.prova] * 90 * mediaProva(d.prova)) < 1e-6, `media ${m0}→${m1} (esperado ${esperadoM}); NF ${nf0}→${nf1}`);
        const d30 = listaSimulados().filter(s => /^D30-/.test(s.id));
        ok('9.diag30', d30.length > 0 && d30.every(s => simById(s.id).itens.length <= 30) && d30.some(s => simById(s.id).itens.length === 30), d30.map(s => s.id + ':' + simById(s.id).itens.length).join(' '));
        // 6. clique real no item intercalado (curso do tópico com ITEM): S.resp não muda; n não muda; k = banco − intercalados
        const tInl = Object.keys(T.top).find(t => idsInline(t).size && tp(t).temCurso);
        if (tInl) { reset(); const kEsp = P.itens.filter(i => i.itemEdital === tInl).length - idsInline(tInl).size; ir('curso', tInl);
          const iid = [...idsInline(tInl)][0]; const b = app().querySelector(`.iti[data-iti="${iid}"] .bolha`); let det = 'bolha não encontrada';
          if (b) { b.click(); const n1 = notaTopico(tInl); det = `${tInl} ${iid}: resp=${S.resp.length} cursoResp=${(S.cursoResp || []).length} ` + JSON.stringify(n1) + ` kEsp=${kEsp}`;
            ok('6.inline', S.resp.length === 0 && (S.cursoResp || []).length === 1 && n1.n === 0 && n1.k === kEsp && statusNota(tInl) === `0 de ${kEsp} questões`, det); } else ok('6.inline', false, det); }
        else ok('6.inline', true, 'N/A — nenhum tópico com ITEM intercalado e curso neste pacote (caso coberto na prévia DEMO)');
        // 12. aviso: só quando algum % exibido mudou (regra antiga janela 30 × nova)
        const aviso = () => { ir('painel'); return !!app().querySelector('#avisoV172'); };
        reset(); const a0 = aviso(); const a0b = S.avisoV172 === true;
        reset(); resp(big.id, ids.slice(0, 25), (k, g) => g); const a25 = aviso(); const a25b = aviso(); // 83% → 100%; segunda visita some
        reset(); resp(big.id, ids.slice(0, 5), (k, g) => g); const a5 = aviso(); // 17% → 25%
        reset(); resp(small.id, sids.slice(0, 5), (k, g) => g); const aPeq = aviso(); // banco ≤ 20: igual
        reset(); resp(big.id, ids.slice(0, 2), (k, g) => k === 0 ? g : (g === 'C' ? 'E' : 'C')); const aZero = aviso(); // saldo 0: 0% → 0%
        ok('12.aviso', !a0 && a0b && a25 && !a25b && a5 && !aPeq && !aZero, `vazio=${a0} com25=${a25} segunda=${a25b} com5=${a5} pequeno=${aPeq} saldo0=${aZero}`);
      }
      // --- telas (em todas as combinações) ---
      reset(); resp(big.id, ids.slice(0, 10), (k, g) => k < 8 ? g : (g === 'C' ? 'E' : 'C')); resp(small.id, sids, (k, g) => g); S.ult = null; const telas = {};
      ir('apresentacao'); telas.apres = app().innerText; ir('painel', { disc: d.id }); telas.painel = app().innerText; ir('recomendacoes'); telas.recs = app().innerText;
      if (tp(big.id).temCurso) { ir('curso', big.id); telas.cursoBig = app().innerText; } if (tp(small.id).temCurso) { ir('curso', small.id); telas.cursoSmall = app().innerText; }
      UI.mat.add(d.id); UI.mat.add(tp(small.id).disc); ir('painel'); const linhaBig = app().querySelector(`#t-${CSS.escape(big.id)} .pc`), linhaSmall = app().querySelector(`#t-${CSS.escape(small.id)} .pc`);
      const zero = tops.find(t => t.id !== big.id && t.id !== small.id && tp(t.id).disc === d.id); const linhaZero = zero && app().querySelector(`#t-${CSS.escape(zero.id)} .pc`);
      ok('13.painel_status', linhaBig && linhaBig.innerText.replace(/\d+ de \d+ questões/, '').replace(/\s+/g, ' ').trim() === '30% 10/20' && /10 de 20 questões/.test(linhaBig.querySelector('.vh') ? linhaBig.querySelector('.vh').textContent : '') && linhaSmall && linhaSmall.innerText.trim() === '100%' && linhaZero && linhaZero.innerText.trim() === '0%',
        `big="${linhaBig && linhaBig.innerText.replace(/\s+/g, ' ').trim()}" small="${linhaSmall && linhaSmall.innerText.trim()}" zero="${linhaZero && linhaZero.innerText.trim()}"`);
      iniciarBloco(big.id); prova.ordem.forEach(id => { prova.resp[id] = M[id].gabarito; }); entregar(); telas.posBloco = app().innerText;
      const ruim = Object.entries(telas).filter(([k, t]) => /(até|de|sobre)\s30\s(questões|respondidas)|\/30\b|30 respondidas|janela de 30/.test(t)).map(([k]) => k);
      const temAviso = /antes eram 30/.test(telas.painel); // aviso é a única menção legítima a 30 fora do diagnóstico
      const bom = /até 20 questões diferentes/.test(telas.apres) && /nota fica completa com 20/.test(telas.apres) && /em branco conta/.test(telas.apres)
        && (!telas.cursoBig || (/30%\s*\(10 de 20 questões\)\./.test(telas.cursoBig) && /Faltam 10 questões para a nota completa/.test(telas.cursoBig)))
        && (!telas.cursoSmall || /100%\s*\(nota completa\)\./.test(telas.cursoSmall))
        && /Desempenho no tópico/.test(telas.posBloco) && /\(20 de 20 questões\)|\(nota completa\)/.test(telas.posBloco) && !/questões\.\s*$/m.test(telas.posBloco) && (telas.posBloco.match(/nota completa/g) || []).length === 1;
      ok('10.textos', ruim.length === 0 && bom && temAviso, `ruim=${JSON.stringify(ruim)} bom=${bom} aviso=${temAviso} cursoBig=${!!telas.cursoBig}`);
      // 5c. "Falta 1 questão"
      reset(); resp(big.id, ids.slice(0, 19), (k, g) => g); if (tp(big.id).temCurso) { ir('curso', big.id); ok('5c.falta_1', /\(19 de 20 questões\)\. Falta 1 questão para a nota completa\./.test(app().innerText), app().querySelector('#fimCurso').innerText.replace(/\n/g, ' | ').slice(0, 200)); }
      return { R, big, small };
    }, tag === COMBOS[0][0]);
    const falhas = r.R.filter(x => !x.ok); falhasTot += falhas.length; errosTot += erros.length;
    tudo[tag] = { casos: r.R, errosJS: erros, big: r.big, small: r.small };
    console.log(`\n== ${tag} ==`); r.R.forEach(x => console.log((x.ok ? 'OK  ' : 'FALHA') + ' ' + x.caso + ' — ' + x.det));
    console.log(`${r.R.length - falhas.length}/${r.R.length} casos OK · erros JS: ${erros.length}`);
    await ctx.close();
  }
  fs.writeFileSync(OUT, JSON.stringify({ arquivo: ARQ, combos: tudo, falhas: falhasTot, errosJS: errosTot }, null, 1));
  console.log(`\nTOTAL falhas ${falhasTot} · erros JS ${errosTot}`);
  await browser.close();
  process.exit(falhasTot || errosTot ? 1 : 0);
})();
