// regr_v17_2.js — regressão v17.1 → v17.2 com estado antigo (R2, após QA R1 D2):
// (1) oráculo: para cada tópico, a nota da v17.2 tem de ser exatamente a regra nova (20 distintas mais recentes; divisor min(20, banco sem intercalados));
// (2) diferença de nota entre A e B só é aceita onde o oráculo prevê mudança (janela cortou ou divisor mudou);
// (3) caderno de erros, S.resp, montagem do bloco de 10 (Math.random fixo), chaves do estado: iguais;
// (4) telas: texto igual depois de retirar só o que a v17.2 acrescenta; os % NÃO são mascarados globalmente — cada % de tópico exibido na matéria
//     é conferido no DOM contra o oráculo, e os agregados (matéria, P1, P2, Nota Final) contra as fórmulas da página sobre as notas do oráculo.
// Uso: node regr_v17_2.js <previa_v17_1.html> <previa_v17_2.html> <estado.json> <saida.json>
const { chromium, abrir, estado } = require('./lib.js');
const fs = require('fs');
const [,, A, B, ESTF, OUT] = process.argv;
const est = JSON.parse(fs.readFileSync(ESTF, 'utf8'));
const pctTxt = x => { const p = Math.round(x * 100); return (p < 0 ? '−' + Math.abs(p) : p) + '%'; };
(async () => {
  const browser = await chromium.launch();
  const coleta = async (arq) => {
    const { page, erros } = await abrir(browser, arq, { estado: est });
    const r = await page.evaluate(() => {
      Math.random = (() => { let s = 11; return () => (s = (s * 16807) % 2147483647) / 2147483647; })();
      const out = {}; const snap = k => out[k] = app().innerText;
      const inlS = t => (T.top[t] && T.top[t].nInline) ? idsInline(t) : new Set();
      const banco = {}; P.itens.forEach(i => { if (!inlS(i.itemEdital).has(i.id)) banco[i.itemEdital] = (banco[i.itemEdital] || 0) + 1; }); out.__banco = banco;
      // oráculo das duas regras, calculado aqui só com S.resp e o banco (sem usar notaTopico)
      const regra = (tid, J) => { let rs = S.resp.filter(r => r.tp === tid); const v = new Set(); rs = rs.slice().reverse().filter(r => !v.has(r.id) && v.add(r.id)).reverse().slice(-J);
        const k = Math.max(1, Math.min(J, banco[tid] || 0)); const c = rs.filter(r => r.st === 'c').length, e = rs.filter(r => r.st === 'e').length; return { n: rs.length, c, e, k, pct: (c - e) / k }; };
      out.__oraculo = Object.fromEntries(Object.values(T.top).map(o => [o.id, { v171: regra(o.id, 30), v172: regra(o.id, 20) }]));
      out.__notas = Object.fromEntries(Object.values(T.top).map(o => { const n = notaTopico(o.id); return [o.id, { n: n.n, c: n.c, e: n.e, pct: pctTopico(o) }]; }));
      out.__erros = JSON.stringify(S.erros); out.__nresp = S.resp.length; out.__nf = notaFinal();
      out.__bloco = JSON.stringify(Object.keys(T.top).filter(t => tp(t).n).slice(0, 12).map(t => montarBloco(t)));
      out.__agreg = { mat: Object.fromEntries(DISCIPLINAS.map(d => [d.id, mediaMateria(d)])), P1: mediaProva('P1'), P2: mediaProva('P2'), nf: notaFinal() };
      S.tentativas.forEach((t, i) => { ir('resultado', i); snap('resultado:' + i); });
      ['painel', 'pratica', 'erros', 'recomendacoes', 'dados', 'vespera', 'discursivas'].forEach(v => { ir(v); snap('tela:' + v); });
      out.__dom = {};
      DISCIPLINAS.forEach(d => { ir('materia', { disc: d.id }); snap('materia:' + d.id);
        app().querySelectorAll('.topl').forEach(el => { const tid = el.id.slice(2); const pc = el.querySelector('.pc'); out.__dom[tid] = pc ? pc.innerText.replace(/\d+ de \d+ questões/, '').replace(/\s+/g, ' ').trim() : null; });
        const mt = app().querySelector(`.mat[data-box="${CSS.escape(d.id)}"] .mat-t .pc`); out.__dom['mat:' + d.id] = mt ? mt.textContent.trim() : null; });
      ir('painel'); app().querySelectorAll('.cabprova').forEach(el => { const h = el.querySelector('h3').textContent.slice(0, 2); out.__dom['prova:' + h] = el.querySelector('.pc').textContent.trim(); });
      out.__dom.nf = (app().querySelector('#nfv') || {}).textContent; out.__fmtNota = fmtNota(notaFinal());
      return out;
    });
    const st = await estado(page);
    return { r, erros, st };
  };
  const a = await coleta(A), b = await coleta(B);
  const dif = [], permitidas = [];
  // (1) oráculo × página, cada regra na sua versão
  Object.keys(b.r.__notas).forEach(k => {
    const o = b.r.__oraculo[k].v172, n = b.r.__notas[k]; if (o.n !== n.n || o.c !== n.c || o.e !== n.e || Math.abs(o.pct - n.pct) > 1e-12) dif.push({ k: 'oraculo172:' + k, esperado: o, pagina: n });
    const oa = a.r.__oraculo[k].v171, na = a.r.__notas[k]; if (oa.n !== na.n || oa.c !== na.c || oa.e !== na.e || Math.abs(oa.pct - na.pct) > 1e-12) dif.push({ k: 'oraculo171:' + k, esperado: oa, pagina: na });
  });
  // (2) diferenças A × B só onde o oráculo prevê
  Object.keys(a.r.__notas).forEach(k => { const x = a.r.__notas[k], y = b.r.__notas[k]; const mudou = JSON.stringify(x) !== JSON.stringify(y);
    const o1 = a.r.__oraculo[k].v171, o2 = b.r.__oraculo[k].v172; const prevista = JSON.stringify([o1.n, o1.c, o1.e, o1.pct]) !== JSON.stringify([o2.n, o2.c, o2.e, o2.pct]);
    if (mudou !== prevista) dif.push({ k: 'mudanca:' + k, a: x, b: y, prevista }); else if (mudou) permitidas.push({ k: 'nota:' + k, a: `${x.n}|${x.c}|${x.e}|${pctTxt(x.pct)}`, b: `${y.n}|${y.c}|${y.e}|${pctTxt(y.pct)}`, banco: a.r.__banco[k] || 0, motivo: o1.n > 20 ? 'janela cortou' : 'divisor mudou' }); });
  // (3) invariantes
  ['__erros', '__nresp', '__bloco'].forEach(k => { if (a.r[k] !== b.r[k]) dif.push({ k, a: String(a.r[k]).slice(0, 200), b: String(b.r[k]).slice(0, 200) }); });
  if (a.r.__nf !== b.r.__nf) (permitidas.length ? permitidas : dif).push({ k: '__nf', a: a.r.__nf, b: b.r.__nf, motivo: 'consequência das notas' });
  // (4a) DOM da v17.2: cada % de tópico = oráculo; "n/k" só quando parcial; agregados = fórmulas da página
  Object.keys(b.r.__oraculo).forEach(k => { const o = b.r.__oraculo[k].v172; const dom = b.r.__dom[k]; if (dom === undefined) return; if (dom === null) { dif.push({ k: 'dom:' + k, b: null }); return; }
    const esperado = pctTxt(o.pct) + (o.n && o.n < o.k ? ` ${o.n}/${o.k}` : ''); if (dom !== esperado) dif.push({ k: 'dom:' + k, esperado, dom }); });
  Object.keys(b.r.__agreg.mat).forEach(d => { const dom = b.r.__dom['mat:' + d]; if (dom && dom !== pctTxt(b.r.__agreg.mat[d])) dif.push({ k: 'dom:mat:' + d, esperado: pctTxt(b.r.__agreg.mat[d]), dom }); });
  ['P1', 'P2'].forEach(p => { if (b.r.__dom['prova:' + p] !== pctTxt(b.r.__agreg[p])) dif.push({ k: 'dom:prova:' + p, esperado: pctTxt(b.r.__agreg[p]), dom: b.r.__dom['prova:' + p] }); });
  if (b.r.__dom.nf !== b.r.__fmtNota) dif.push({ k: 'dom:nf', esperado: b.r.__fmtNota, dom: b.r.__dom.nf });
  // (4b) telas: só o que a v17.2 acrescenta pode diferir; com tópico afetado, os % são neutralizados nas duas (os valores já foram conferidos em 4a)
  const afetados = permitidas.filter(p => p.k.startsWith('nota:')).length;
  const norm = s => { let t = String(s).replace(/v17\.2/g, 'v17.1').replace(/\s*\((?:nota completa|\d+ de \d+ questões)\)\.?/g, '').replace(/\s*(?:Falta 1 questão|Faltam \d+ questões) para a nota completa\./g, '')
    .replace(/(\d%)\s\d+\/\d+\s\d+ de \d+ questões/g, '$1').replace(/(\d%)\s\d+\/\d+/g, '$1').replace(/nota recente ([+−]?\d+)\/\d+/g, 'nota recente $1/K').replace(/até \d+ questões diferentes/g, 'até K questões diferentes')
    .replace(/A nota fica completa com \d+ questões diferentes respondidas \(ou todas as do tópico, se houver menos\); até lá você vê quantas faltam\. Questão deixada em branco conta na contagem e vale 0\./g, '')
    .replace(/A partir desta versão, a nota de cada tópico é calculada sobre até (?:\d+|K) questões diferentes \(antes eram 30\): as \d+ mais recentes, com as que faltam valendo 0\. Por isso a nota de alguns tópicos mudou\./g, '');
    if (afetados) t = t.replace(/[−+]?\d+%/g, 'P%').replace(/Nota Final\s*[\d,]+/g, 'Nota Final N');
    return t.replace(/\s+/g, ' ').trim(); };
  Object.keys(a.r).filter(k => !k.startsWith('__')).forEach(k => { const x = norm(a.r[k]), y = norm(b.r[k]); if (x !== y) { let i = 0; while (i < x.length && x[i] === y[i]) i++; dif.push({ k, pos: i, a: x.slice(Math.max(0, i - 60), i + 120), b: y.slice(Math.max(0, i - 60), i + 120) }); } });
  const ka = Object.keys(a.st).sort(), kb = Object.keys(b.st).sort().filter(k => k !== 'avisoV172');
  if (ka.join() !== kb.join()) dif.push({ k: 'estado:chaves', a: ka.join(), b: kb.join() });
  ['tentativas', 'erros', 'resp', 'saidas', 'top', 'escolha', 'escolhaDisc', 'disc', 'vespera', 'cursoResp'].forEach(k => { if (JSON.stringify(est[k]) !== JSON.stringify(b.st[k])) dif.push({ k: 'estado:' + k, a: 'orig', b: 'mudou' }); });
  const maxDist = Math.max(0, ...Object.values(a.r.__oraculo).map(o => o.v171.n));
  const res = { estado: ESTF, maxDistintasPorTopico: maxDist, permitidas, dif, errosA: a.erros, errosB: b.erros, telas: Object.keys(a.r).filter(k => !k.startsWith('__')).length, topicosConferidosNoDom: Object.keys(b.r.__dom).filter(k => !k.includes(':') && k !== 'nf').length };
  fs.writeFileSync(OUT, JSON.stringify(res, null, 1));
  console.log(`estado ${ESTF} · máx. distintas por tópico ${maxDist} · telas ${res.telas} · tópicos conferidos no DOM ${res.topicosConferidosNoDom} · mudanças previstas pelo oráculo ${permitidas.length} · diferenças NÃO previstas ${dif.length} · erros JS A ${a.erros.length} B ${b.erros.length}`);
  permitidas.forEach(d => console.log(' ~', d.k, d.a, '=>', d.b, d.motivo ? `(${d.motivo}; banco ${d.banco})` : ''));
  dif.forEach(d => console.log(' !', d.k, JSON.stringify(d).slice(0, 400)));
  await browser.close();
  process.exit(dif.length || a.erros.length || b.erros.length ? 1 : 0);
})();
