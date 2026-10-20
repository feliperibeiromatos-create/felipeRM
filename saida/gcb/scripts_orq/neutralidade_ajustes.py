# neutralidade_ajustes.py — aplica, por substituição literal, os ajustes obrigatórios e opcionais de forma de
# QA_neutralidade_D2_D4_2026-10-20_gcb-cqfp.md aos arquivos D<n>_para_leitura_critica.md (depois de leitura_critica_gen.py)
import re, sys, pathlib, hashlib
g = pathlib.Path(__file__).resolve().parents[1]
AJ = {
 'D2': [
  ('Mínimo deste material: 8, com os 6 obrigatórios (P-01 a P-06). Entregues: 12 (os 6 obrigatórios e os 6 recomendados da parte A).\n\n', '', 1),
  ('Mínimo deste material: 8, com os 6 obrigatórios (P-51 a P-56). Entregues: 11.\n\n', '', 1),
  ('(parte B deste lote)', '(item 4 deste material)', 1),
  ('Nota Nota de vigência: a alínea b', 'Nota (vigência a reconfirmar): a alínea b', 1),
  ('(Nota de vigência:; norma de 2025, vigente)', '(vigência a reconfirmar; norma de 2025, vigente)', 1),
  ('Nota de vigência:)', 'vigência a reconfirmar)', 4),
  ('((não afirmado neste material))', '(não afirmado neste material)', None)],
 'D3': [
  (', alerta 6)', ')', 1), (', alerta 4)', ')', 1), (', alerta 1)', ')', 1), (', alerta 2)', ')', 1),
  ('(texto legal compilado e alerta 3)', '(texto legal compilado)', 1), (', alerta 8)', ')', 1), (', alerta 15)', ')', 1),
  ('Mínimo deste material para a Parte A: 10, com os 7 obrigatórios (P-01 a P-07). Entregues: 13.\n\n', '', 1),
  ('Mínimo deste material para a Parte B: 8, com os 6 obrigatórios (P-51 a P-56). Entregues: 10.\n\n', '', 1),
  ('código G-NN (faixa G-01 a G-50 da Parte A).', 'código G-NN.', 1),
  ('((não afirmado neste material))', '(não afirmado neste material)', None),
  ('no texto legal compilado A LC 219', 'no texto legal compilado. A LC 219', 1),
  ('(Base doutrinária:)', '(base doutrinária)', None), ('(Base doutrinária:,', '(base doutrinária,', None),
  ('(ponto pacífico, a ser confirmado pelo R1)', '(ponto pacífico)', 1)],
 'D4': [
  ('(R-id da seção 5 do texto legal compilado, com as palavras-chave literais)', '(R-id, com as palavras-chave literais)', 2),
  ('Temas da Parte B (governança,', 'Temas do item 9 (governança,', 1),
  ('(LAI, art. 10, caput; exceção deste material)**', '(LAI, art. 10, caput)**', 1),
  ('- Definição: Lado passivo do par, pela exceção única deste material (curso e par; nunca item), com o texto do texto legal compilado do D6, seção 4, consulta de 17/10/2026 (mesma URL da fonte N9): ', '- Definição: Lado passivo do par, com o texto legal compilado (consulta de 17/10/2026): ', 1),
  ('do Decreto 9.203/2017, texto integral compilado (texto legal compilado), ou', 'do Decreto 9.203/2017, texto integral compilado, ou', 1),
  ('exemplo hipotético no contexto da seção 4 deste material;', 'exemplo hipotético no contexto do Legislativo;', 1),
  ('na mesma página, segundo o texto legal compilado, o referencial diz que', 'na mesma página, o referencial diz que', 1),
  ('Fontes: texto legal compilado (normas, seção 4; referencial R1 a R18, seção 5).', 'Fontes: normas (texto legal compilado) e referencial (R1 a R18).', 1),
  ('por qualquer interessado (só curso e par) | Lei 12.527/2011, art. 10, caput (texto legal compilado do D6) |', 'por qualquer interessado | Lei 12.527/2011, art. 10, caput |', 1),
  ('(LAI, art. 10, caput; só curso e par)', '(LAI, art. 10, caput)', 1),
  ('(texto legal compilado do D6, seção 4, consulta de 17/10/2026)', '(texto legal compilado, consulta de 17/10/2026)', 1),
  ('Mínimo deste material: 8 na Parte A (14 obrigatórios no lote, 7 na Parte A: P-01 a P-07). Entregues: 11 (P-01 a P-11). Cada lado', 'Cada lado', 1),
  ('Mínimo deste material para a Parte B: 8, com os 7 obrigatórios (P-51 a P-57). Entregues: 12 (os 7 obrigatórios e 5 sugeridos com lastro nos dois lados).\n\n', '', 1),
  ('Códigos G-51 em diante (G-01 a G-50 são da Parte A).', 'Códigos G-51 em diante.', 1),
  ('((não afirmado neste material))', '(não afirmado neste material)', None)],
}
PROIB = r'(?i:\bparte [ab]\b|alerta \d|nunca item|fonte N\d|mínimo d|nota de vigência:|exceção deste material)|\bD[1-9]\b(?!-)'
for lote, lst in AJ.items():
    p = g/f'{lote}_para_leitura_critica.md'; t = p.read_text(encoding='utf-8')
    for velho, novo, n in lst:
        c = t.count(velho)
        if n is not None and c != n: sys.exit(f'{lote}: esperado {n}, achado {c}: {velho[:60]!r}')
        t = t.replace(velho, novo)
    res = [t[max(0,m.start()-40):m.end()+40].replace('\n',' ') for m in re.finditer(PROIB, t)]
    res = [r for r in res if not r.startswith('LOTE') and 'LOTE ' + lote not in r]
    p.write_text(t, encoding='utf-8')
    print(lote, 'SHA-256', hashlib.sha256(t.encode()).hexdigest(), 'resíduos:', len(res)); [print('  ', r) for r in res]
