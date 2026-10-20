# formatar_D3.py — T-76 (ordem DA 20/10/2026) — 2026-10-20 — gerado por gcb-cpp
# Reformata o canônico saida/gcb/D3_v2_1.md para o formato da plataforma (FORMATO_PLATAFORMA_DA.md).
# Só reformatação: nenhum conteúdo novo. Toda deleção e troca de palavra é registrada (LOG) e vai ao registro.
# Determinístico. Os tópicos são escritos à mão em D3_topicos_fonte.json e incorporados aqui.
# Uso:  python3 -I saida/gcb/DA_plataforma/scripts/formatar_D3.py              -> grava D3_plataforma.json
#       python3 -I saida/gcb/DA_plataforma/scripts/formatar_D3.py --registro   -> regrava o JSON, roda o validador e a
#                                                                                conferência de fidelidade e grava D3_registro_formato.md
import hashlib, json, pathlib, re, subprocess, sys
from collections import Counter

RAIZ = pathlib.Path(__file__).resolve().parents[4]
DA = RAIZ / 'saida/gcb/DA_plataforma'
CANON = RAIZ / 'saida/gcb/D3_v2_1.md'
MAPA = RAIZ / 'saida/gcb/D3_anexo_N_mapa_normativo.md'
SHA_CANON = '0f7a8b090fe6f2243ae55b36273dacdb719aaf04b19548dce70aad4867798930'
URL_CANON = 'saida/gcb/D3_v2_1.md'
SAIDA_JSON = DA / 'D3_plataforma.json'
TOPICOS = DA / 'D3_topicos_fonte.json'
REGISTRO = DA / 'D3_registro_formato.md'
VALIDADOR = DA / 'scripts/validar_da.py'
CONFERE = DA / 'scripts/conferir_fidelidade_D3.py'

NOME = 'Direito Administrativo — Poderes administrativos, responsabilidade civil do Estado e improbidade (itens 5 a 7 do edital)'

def sha(b): return hashlib.sha256(b).hexdigest()

def ler_canon():
    raw = CANON.read_bytes()
    if sha(raw) != SHA_CANON:
        print('PARAR: SHA-256 de saida/gcb/D3_v2_1.md diverge:', sha(raw), '!=', SHA_CANON); sys.exit(2)
    return raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n').split('\n')

EDITAL = {e['id']: e['texto'] for e in json.loads((DA / 'edital_DA.json').read_text(encoding='utf-8'))}

def achar(L, prefixo, ini=0):
    for i in range(ini, len(L)):
        if L[i].startswith(prefixo): return i
    raise SystemExit('PARAR: seção não encontrada: ' + prefixo)

# ---------------------------------------------------------------- registro de edições
LOG = []   # {ctx, tipo, antes, depois, motivo, adicionado}
def log(ctx, tipo, antes, depois, motivo, adicionado=''):
    LOG.append(dict(ctx=ctx, tipo=tipo, antes=antes, depois=depois, motivo=motivo, adicionado=adicionado))

def edita(ctx, txt, antigo, novo, tipo, motivo, adicionado=''):
    assert txt.count(antigo) == 1, (ctx, antigo[:70], txt.count(antigo))
    log(ctx, tipo, antigo.strip(), novo.strip(), motivo, adicionado)
    return txt.replace(antigo, novo)

D_MARCA = 'deleção de marca'
D_FRASE = 'deleção de frase inteira'
D_ORACAO = 'deleção de oração de processo'
D_BLOCO = 'deleção de bloco inteiro'
TROCA = 'troca mínima (op. 6)'
M_SEMFONTE = '"[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6)'
M_ANEXO = 'referência ao Anexo N (seção 6)'
M_BD = 'marca "BASE DOUTRINÁRIA" com o parêntese que a qualifica (seção 6)'
E_ACH1 = 'errata de forma (QA final 20/10/2026, achado 1): '
E_SUB = E_ACH1 + '"folha" é termo de produção (seção 6); a remissão serve ao estudo e passa a "subitem", o número 6.1 é o do `##` do curso'
M_RECORTE = '"recorte" é referência de produção (recorte do despacho do lote); trocado por "curso", como o D1 fez com "lote"; a ressalva é mantida'

# blocos do curso cuja definição é só "[SEM FONTE — não afirmar]" + nota de produção: nada resta depois de tirar a marca e a frase marcada
DROP = {
 'C5.1-10': 'delegação do poder de polícia a particulares e fases do ciclo de polícia',
 'C6.1-06': 'temas de tratamento jurisprudencial (6.1)',
 'C6.2-04': 'temas de tratamento jurisprudencial (6.2)',
 'C6.3-06': 'regime da omissão e temas conexos',
}
DROP_PEG = {10: 'C5.1-10', 22: 'C6.1-06', 26: 'C6.2-04', 32: 'C6.3-06'}

# edições explícitas no curso, por bloco e campo ('tit' = título; 'def' = definição; 'peg' = pegadinha, parte antes de "[Desfeita por")
EXPL = {
 ('C6.2-02', 'def'): [
  (' A ação regressiva é desta folha.', '', D_FRASE, E_ACH1 + 'a frase só diz a que parte da produção a ação regressiva pertence ("é desta folha"); o assunto já está no título do bloco e nas linhas anteriores'),
 ],
 ('C6.4-04', 'def'): [
  ('é da folha 6.1.', 'é do subitem 6.1.', TROCA, E_SUB, 'do subitem'),
 ],
 ('C5.1-01', 'def'): [
  ('O texto legal do recorte só menciona', 'O texto legal do curso só menciona', TROCA, M_RECORTE, 'curso'),
  ('Nenhum dispositivo do recorte define', 'Nenhum dispositivo do curso define', TROCA, M_RECORTE, 'curso'),
 ],
 ('C5.1-05', 'def'): [
  ('Nenhum dispositivo do recorte trata', 'Nenhum dispositivo do curso trata', TROCA, M_RECORTE, 'curso'),
  ('; o regime disciplinar da Lei 8.112/1990 não faz parte deste lote ([SEM FONTE — não afirmar])', '', D_ORACAO,
   M_SEMFONTE + '; a oração também cita "este lote"; fica "Nenhum dispositivo do curso trata do poder disciplinar."'),
 ],
 ('C5.1-07', 'def'): [
  (' O instrumento formal da sustação não consta do Anexo N: [SEM FONTE — não afirmar].', '', D_FRASE, M_SEMFONTE + '; a frase também cita o Anexo N'),
 ],
 ('C6.3-01', 'def'): [
  (' O curso não afirma o regime aplicável à omissão: [SEM FONTE — não afirmar] (ver C6.3-06).', '', D_FRASE,
   M_SEMFONTE + '; a frase também remete a código de bloco (C6.3-06), cujo bloco saiu inteiro (seção 6)'),
 ],
 ('C6.5-01', 'tit'): [
  (' e ausência de texto no recorte', '', D_ORACAO, 'oração do título que fala do recorte do lote (a ausência de enumeração no § 6º continua dita na definição)'),
 ],
 ('C6.5-01', 'def'): [
  ('; o despacho não pede outros artigos do Código Civil', '', D_ORACAO, 'oração sobre o pedido do despacho do lote; só processo'),
 ],
 ('C6.5-02', 'def'): [
  (' A distinção entre os dois, e entre caso fortuito interno e externo: [SEM FONTE — não afirmar].', '', D_FRASE, M_SEMFONTE),
 ],
 ('C6.5-02', 'peg'): [
  (', ou condicionar sua eficácia a distinções sem fonte', '', D_ORACAO, 'a oração depende da frase "[SEM FONTE — não afirmar]" sobre as distinções, que a seção 6 manda tirar; sem ela a pegadinha ficaria sem objeto (mesma edição na lista consolidada)'),
 ],
 ('C6.5-04', 'def'): [
  (' Ônus da prova da excludente: [SEM FONTE — não afirmar].', '', D_FRASE, M_SEMFONTE),
 ],
 ('C6.5-05', 'def'): [
  (' Hipóteses concretas de risco integral: [SEM FONTE — não afirmar].', '', D_FRASE, M_SEMFONTE),
 ],
 ('C7-01', 'def'): [
  ('(Lei 14.230/2021, art. 4º; Anexo N, seção 2.1)', '(Lei 14.230/2021, art. 4º)', D_MARCA, M_ANEXO + '; fica a referência à Lei 14.230/2021'),
 ],
 ('C7-19', 'peg'): [
  (' Tema jurisprudencial do ressarcimento: [SEM FONTE — não afirmar].', '', D_FRASE, M_SEMFONTE + ' (mesma edição na lista consolidada)'),
 ],
 ('C7-20', 'def'): [
  (' no Anexo N, seção 2.1', '', D_MARCA, M_ANEXO + '; fica "Registro: 28 dispositivos revogados (Lei 14.230/2021, art. 4º) e 9 vetados (art. 17-A)."'),
  (' Tratamento jurisprudencial do tema: [SEM FONTE — não afirmar].', '', D_FRASE, M_SEMFONTE),
 ],
 ('C7-23', 'def'): [
  (' (o texto do § 1º do art. 37 da CF não consta do Anexo N e não é afirmado aqui)', '', D_ORACAO,
   'parêntese de cobertura da base normativa ("não consta do Anexo N", seção 6); só processo'),
 ],
}

# edições explícitas na lista consolidada de pegadinhas (por número G-NN; texto antes de " — Dispositivo:")
GEDIT = {
 39: [(', ou condicionar sua eficácia a distinções sem fonte', '', D_ORACAO, 'ver a mesma edição no bloco do curso (a oração dependia da frase "[SEM FONTE — não afirmar]")')],
 69: [(' Tema jurisprudencial do ressarcimento: [SEM FONTE — não afirmar].', '', D_FRASE, M_SEMFONTE + ' (mesma edição no bloco do curso)')],
}

RX_ANEXO = re.compile(r'\s?\(Anexo N, [^)]*\)')
RX_BD = re.compile(r'BASE DOUTRINÁRIA \(ponto pacífico\): ')
RX_SUFIXO = [
 re.compile(r' — acréscimo da v2 \(leitura externa [^()]*; QA PENDENTE \(R2\)\)$'),
 re.compile(r' \[alterado na v2: [^\]]*\]$'),
]

def limpa_generico(ctx, txt):
    """Deleta '(Anexo N, …)' e o rótulo 'BASE DOUTRINÁRIA (ponto pacífico): ' (marcas, seção 6); registra cada ocorrência."""
    def anexo(m):
        log(ctx, D_MARCA, m.group(0).strip(), '', M_ANEXO)
        return ''
    txt = RX_ANEXO.sub(anexo, txt)
    while True:
        m = RX_BD.search(txt)
        if not m: break
        antes, depois = txt[:m.start()], txt[m.end():]
        cap = antes == '' or antes.endswith('. ')
        if cap: depois = depois[:1].upper() + depois[1:]
        log(ctx, D_MARCA, m.group(0).strip(), '', M_BD + '; ' + ('a letra minúscula seguinte passa a maiúscula' if cap else 'sem mais mudança'))
        txt = antes + depois
    return txt

# ---------------------------------------------------------------- "Desfeita por" / "Dispositivo": base da pegadinha
def limpa_base(ctx, base):
    """Tira da base a marca BASE DOUTRINÁRIA e a remissão ao Anexo N; devolve '' se nada resta (ponto só doutrinário)."""
    b = base.strip()
    assert b.endswith('.'), (ctx, b)
    if b == 'BASE DOUTRINÁRIA (ponto pacífico).':
        log(ctx, D_MARCA, 'Base: BASE DOUTRINÁRIA (ponto pacífico).', '(nada)', M_BD + '; a base era só a marca, e sem dispositivo a frase "Base: …" não tem conteúdo; a pegadinha fica sem o rótulo "Base"')
        return ''
    if b.startswith('BASE DOUTRINÁRIA (ponto pacífico); '):
        log(ctx, D_MARCA, 'BASE DOUTRINÁRIA (ponto pacífico); ', '', M_BD + '; ficam os dispositivos da base')
        b = b[len('BASE DOUTRINÁRIA (ponto pacífico); '):]
    elif '; BASE DOUTRINÁRIA (ponto pacífico)' in b:
        log(ctx, D_MARCA, '; BASE DOUTRINÁRIA (ponto pacífico)', '', M_BD + '; ficam os dispositivos da base')
        b = b.replace('; BASE DOUTRINÁRIA (ponto pacífico)', '')
    if '; Anexo N, seção 2.1' in b:
        log(ctx, D_MARCA, '; Anexo N, seção 2.1', '', M_ANEXO)
        b = b.replace('; Anexo N, seção 2.1', '')
    assert 'Anexo' not in b and 'BASE DOUTRIN' not in b and 'SEM FONTE' not in b, (ctx, b)
    return b

NORMAS = re.compile(r'^(CF|CTN|Código Civil|Lei [\d.]+/\d{4}),\s*(.*)$')
RX_ART = re.compile(r'^(arts?\. \d+º?(?:-[A-Z])?)')

def base_legal(base):
    """Lista de dispositivos da base (norma herdada entre itens separados por '; '; só o que a base já cita)."""
    out, norma, art = [], None, None
    for it in [x.strip() for x in base.rstrip('.').split('; ')]:
        m = NORMAS.match(it)
        if m: norma, rest = m.group(1), m.group(2)
        else: rest = it
        assert norma, base
        if rest.startswith(('art.', 'arts.')):
            art = RX_ART.match(rest).group(1)
            out.append(f'{norma}, {rest}')
        else:
            assert art, base
            out.append(f'{norma}, {art}, {rest}')
    return out

BASE_LEGAL_OVERRIDE = {
 'C5.1-05': ['CTN, art. 78, caput'],   # a base diz "CTN, art. 78, caput, para o poder de polícia"
}

# ---------------------------------------------------------------- curso
def titulo_edital(eid):
    t = EDITAL[eid]
    if len(t) > 90 and ':' in t: t = t.split(':')[0]
    return t.upper()

def sentencas(txt):
    partes, ini = [], 0
    for m in re.finditer(r'\.\s+(?=[A-ZÁÉÍÓÚ§])', txt):
        antes = txt[ini:m.start() + 1]
        if re.search(r'\b(art|arts|inc|n)\.$', antes): continue
        partes.append(antes); ini = m.end()
    partes.append(txt[ini:])
    return [p.strip() for p in partes if p.strip()]

def parse_curso(L):
    ini = achar(L, '## 1. (a) CURSO'); fim = achar(L, '## 2. (b) RESUMO', ini)
    partes, bloco = [], None
    for l in L[ini + 1:fim]:
        m = re.match(r'^### PARTE (1\.\d) — ([\d.]+) (.+)$', l)
        if m:
            partes.append(dict(cod=m.group(1), folha=m.group(2), titulo_origem=l[4:], blocos=[])); bloco = None; continue
        m = re.match(r'^\*\*(C[\d.]+-\d\d) (.+?)\*\*(.*)$', l)
        if m and partes:
            bloco = dict(cod=m.group(1), titulo=m.group(2), sufixo=m.group(3), linhas=[l], campos={})
            partes[-1]['blocos'].append(bloco); continue
        if l.strip() in ('', '---'): continue
        if bloco is not None and l.startswith('- '):
            bloco['linhas'].append(l)
            for chave, pref in (('def', '- Definição: '), ('ex', '- Exemplo (Legislativo, hipotético): '), ('peg', '- Pegadinha provável: ')):
                if l.startswith(pref): bloco['campos'][chave] = l[len(pref):]; break
            else:
                raise SystemExit('PARAR: linha inesperada no curso: ' + l[:80])
        elif bloco is None:
            continue   # parágrafo introdutório da seção 1 (processo; não entra)
        else:
            raise SystemExit('PARAR: linha inesperada no curso: ' + l[:80])
    for p in partes:
        for b in p['blocos']:
            assert set(b['campos']) == {'def', 'ex', 'peg'}, b['cod']
            assert b['cod'][1:].split('-')[0] == p['folha'], (b['cod'], p['folha'])
    return partes

def monta_curso(partes):
    out, mapa = [], []
    for p in partes:
        eid = 'P1-DA-' + p['folha']
        cab = f"## {p['folha']} {titulo_edital(eid)}"
        out += [cab, '']
        mapa.append(dict(origem=p['titulo_origem'], destino=cab))
        for b in p['blocos']:
            ctx = 'curso ' + b['cod']
            tit0 = b['titulo']
            d, e, g = b['campos']['def'], b['campos']['ex'], b['campos']['peg']
            suf = b['sufixo']
            if suf:
                assert any(rx.fullmatch(suf) for rx in RX_SUFIXO), (b['cod'], suf)
                log(ctx + ' (título)', D_MARCA, suf.strip(), '', 'marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa")')
            if b['cod'] in DROP:
                assert 'SEM FONTE' in d and 'SEM FONTE' not in e, b['cod']
                log(ctx, D_BLOCO, f'bloco {b["cod"]} ({DROP[b["cod"]]}): definição "… [SEM FONTE — não afirmar]. O Anexo N não traz jurisprudência, e o lote não enuncia tese de tribunal"; exemplo "não se aplica"; pegadinha "Afirmar, sem fonte, …"',
                    '(nada)', M_SEMFONTE + '; a definição inteira é a frase marcada e uma nota sobre o Anexo N e o lote, o exemplo é "não se aplica" e a pegadinha só repete o que não se afirma: nada resta para a candidata, e o bloco não entra (a pegadinha correspondente da lista consolidada também sai)')
                mapa.append(dict(origem=f"{b['cod']} {tit0}" + (f" {suf.strip()}" if suf else ''), destino='(bloco não entra: nada resta depois de tirar a frase marcada "[SEM FONTE — não afirmar]")'))
                b['saida'] = None
                continue
            for (blk, campo), lst in EXPL.items():
                if blk != b['cod']: continue
                for ant, nov, tipo, motivo, *ad in lst:
                    ad = ad[0] if ad else ''
                    if campo == 'def': d = edita(ctx + ' (definição)', d, ant, nov, tipo, motivo, ad)
                    elif campo == 'peg': g = edita(ctx + ' (pegadinha)', g, ant, nov, tipo, motivo, ad)
                    elif campo == 'tit': tit0 = edita(ctx + ' (título)', tit0, ant, nov, tipo, motivo, ad)
            d = limpa_generico(ctx + ' (definição)', d)
            e = limpa_generico(ctx + ' (exemplo)', e)
            m = re.fullmatch(r'(.*?) \[Desfeita por: (.+)\]', g)
            assert m, (b['cod'], g[-80:])
            claim, base0 = m.group(1), m.group(2)
            base = limpa_base(ctx + ' (pegadinha)', base0)
            if base:
                log(ctx + ' (pegadinha)', 'troca de rótulo', '[Desfeita por: ' + base0 + ']', 'Base: ' + base, 'operação 2 da seção 7', 'Base:')
                g = claim + ' Base: ' + base
            else:
                log(ctx + ' (pegadinha)', 'troca de rótulo', '[Desfeita por: ' + base0 + ']', '(nada)', 'operação 2 da seção 7; base só doutrinária (marca deletada): ver a linha de deleção de marca acima')
                g = claim
            # exemplo: o rótulo "Exemplo (Legislativo, hipotético)" vira o quadro; sem exemplo ("não se aplica"), o quadro é omitido
            if e.strip().rstrip('.') == 'não se aplica':
                log(ctx + ' (exemplo)', 'quadro omitido', '- Exemplo (Legislativo, hipotético): não se aplica.', '(nada)', 'o original não tem exemplo; a especificação (seção 3) manda incluir só os quadros que o original tiver')
                e = ''
            else:
                if 'O exemplo é hipotético' not in e:
                    log(ctx + ' (exemplo)', 'troca de rótulo', 'Exemplo (Legislativo, hipotético):', 'quadro EXEMPLO PARLAMENTAR + "O exemplo é hipotético."',
                        'operação 2 da seção 7; a frase preserva a qualificação "hipotético" que estava no rótulo (precedente do D1)', 'O exemplo é hipotético.')
                    e = e.rstrip() + ' O exemplo é hipotético.'
                else:
                    log(ctx + ' (exemplo)', 'troca de rótulo', 'Exemplo (Legislativo, hipotético):', 'quadro EXEMPLO PARLAMENTAR', 'operação 2 da seção 7; o exemplo já termina com a frase "O exemplo é hipotético"')
            for campo_txt in (tit0, d, e, g):
                assert not re.search(r'Anexo|BASE DOUTRIN|SEM FONTE|REVERIFICAR|\bC\d|QA PENDENTE|\bv2\b|\bR[12]\b|\blote\b|recorte|neste material|NÃO CONFERID', campo_txt), (b['cod'], campo_txt[:90])
            out += ['### ' + tit0, '']
            mapa.append(dict(origem=f"{b['cod']} {b['titulo']}" + (f" {suf.strip()}" if suf else ''), destino='### ' + tit0))
            out.append('DEFINIÇÃO')
            ss = sentencas(d)
            if len(ss) >= 3: out.extend('- ' + s for s in ss)
            else: out.append(d)
            out.append('')
            bl = BASE_LEGAL_OVERRIDE.get(b['cod'], base_legal(base) if base else [])
            if bl:
                out.append('BASE LEGAL'); out.extend('- ' + x for x in bl); out.append('')
            if e: out += ['EXEMPLO PARLAMENTAR', e, '']
            out += ['PEGADINHA PROVÁVEL', g, '']
            b['saida'] = dict(titulo=tit0, d=d, e=e, g=g, base=bl, tem_base=bool(base))
    while out and out[-1] == '': out.pop()
    return '\n'.join(out), mapa

# ---------------------------------------------------------------- resumo
def monta_resumo(L):
    ini = achar(L, '## 2. (b) RESUMO'); fim = achar(L, '---', ini)
    linhas = list(L[ini + 1:fim])
    while linhas and not linhas[0].strip(): linhas.pop(0)
    while linhas and not linhas[-1].strip(): linhas.pop()
    txt = '\n'.join(linhas)
    txt = edita('resumo', txt, '### 2.1 Item 5 — Poderes administrativos', '**Item 5 — Poderes administrativos**', D_MARCA,
                'sai o número de seção do canônico ("2.1"); o título vira linha em negrito, como nos resumos do D1 e do D5 (operação 1: mover para a estrutura)')
    txt = edita('resumo', txt, '### 2.2 Item 6 — Responsabilidade civil do Estado', '**Item 6 — Responsabilidade civil do Estado**', D_MARCA,
                'sai o número de seção do canônico ("2.2"); o título vira linha em negrito')
    txt = edita('resumo', txt, '### 2.3 Item 7 — Improbidade administrativa\n\n', '', D_MARCA,
                'sai o título repetido com número de seção ("2.3"); a linha em negrito "Item 7 — Improbidade Administrativa (Lei nº 8.429/1992 e suas alterações)." que vem logo abaixo é mantida')
    n = txt.count(' (BASE DOUTRINÁRIA)')
    assert n == 6, n
    for _ in range(n): log('resumo', D_MARCA, '(BASE DOUTRINÁRIA)', '', 'marca "BASE DOUTRINÁRIA" (seção 6); o texto que segue é mantido')
    txt = txt.replace(' (BASE DOUTRINÁRIA)', '')
    def rotulo(m):
        ini_, resto_ = m.group(1), m.group(2)
        log('resumo', D_MARCA, 'BASE DOUTRINÁRIA: ' + ini_ + resto_ + '…', ini_.upper() + resto_ + '…', 'marca "BASE DOUTRINÁRIA" (seção 6); a letra minúscula seguinte passa a maiúscula')
        return ini_.upper() + resto_
    txt, n = re.subn(r'BASE DOUTRINÁRIA: (.)(.{0,30})', rotulo, txt)
    assert n == 2, n
    txt = edita('resumo', txt, '| Número literal do Anexo N | Dispositivo |', '| Número literal | Dispositivo |', D_MARCA, 'sai "do Anexo N" do cabeçalho da tabela (seção 6); a tabela é mantida')
    txt = edita('resumo', txt, '\n\nAlterações da v2 no resumo: item 7, "Sistema e dolo" (texto fixado no R1, seção 5.4, letra a; ponto 22) e linha de 40 salários mínimos da tabela (letra b; ponto 22). O resto do resumo é o da v1.', '',
                D_FRASE, 'nota de produção sobre alterações da v2 no resumo (cita "v2", "R1", "v1" e pontos do parecer; seção 6)')
    return txt

# ---------------------------------------------------------------- pares
def monta_pares(L):
    ini = achar(L, '## 3. (c) PARES'); fim = achar(L, '## 4. (d) PEGADINHAS', ini)
    pares = []
    for l in L[ini:fim]:
        if not re.match(r'^\| P-\d\d', l): continue
        cel = [c.strip() for c in l.strip().strip('|').split('|')]
        assert len(cel) == 5, l[:60]
        cod, par, dif, _base, banca = cel
        cod = cod.split(' ')[0]
        ctx = 'par ' + cod
        while ' (BASE DOUTRINÁRIA, ponto pacífico)' in dif:
            dif = edita(ctx, dif, ' (BASE DOUTRINÁRIA, ponto pacífico)', '', D_MARCA, 'marca "BASE DOUTRINÁRIA" com o parêntese que a qualifica (seção 6); a frase termina no ponto que já a fechava')
        if cod == 'P-53':
            banca = edita(ctx, banca, ' Ângulo diferente do mero exercício da função (art. 1º, § 3º).', '', D_FRASE,
                          'frase que só distingue este par de outro ponto do lote (comparação com outro ponto do material, não conteúdo para a candidata; seção 7)')
        termos = par.split(' × ')
        assert len(termos) >= 2, par
        a, b = termos[0], ' × '.join(termos[1:])
        assert dif.endswith('.') and banca.endswith('.'), cod
        pares.append(dict(a=a, b=b, como=dif + ' Como a banca troca: ' + banca, _cod=cod))
    assert len(pares) == 31, len(pares)
    return pares

# ---------------------------------------------------------------- pegadinhas (lista consolidada)
PEG_SUF = ' [acréscimo da v2 (QA PENDENTE (R2))]'

def monta_pegadinhas(L):
    ini = achar(L, '## 4. (d) PEGADINHAS'); fim = achar(L, '---', ini)
    out = []
    vistos_drop = set()
    for l in L[ini + 1:fim]:
        m = re.match(r'^G-(\d\d)\. \[(C[\d.]+-\d\d)\] (.+)$', l)
        if not m: continue
        n, cb, t = int(m.group(1)), m.group(2), m.group(3)
        ctx = f'pegadinha {n}'
        if n in DROP_PEG:
            assert DROP_PEG[n] == cb and cb in DROP, (n, cb)
            log(ctx, D_BLOCO, 'G-%02d [%s] %s' % (n, cb, t), '(nada)', M_SEMFONTE + '; a pegadinha só afirma "sem fonte" o que o bloco do curso (que não entra) não afirma; a base é "não afirmado neste material"')
            vistos_drop.add(n); continue
        if PEG_SUF in t:
            log(ctx, D_MARCA, PEG_SUF.strip(), '', 'marca "v2", "QA PENDENTE" e "R2" (seção 6)')
            t = t.replace(PEG_SUF, '')
        for ant, nov, tipo, motivo in GEDIT.get(n, []):
            t = edita(ctx, t, ant, nov, tipo, motivo)
        claim, sep, disp = t.rpartition(' — Dispositivo: ')
        assert sep, l[:60]
        assert claim.endswith(('.', '?', '!')), (n, claim[-30:])
        base = limpa_base(ctx, disp)
        if base:
            log(ctx, 'troca de rótulo', ' — Dispositivo: ' + disp, ' Base: ' + base, 'operação 2 da seção 7 (o rótulo "Dispositivo:" vira "Base:", como no curso e no D5)', 'Base:')
            texto = claim + ' Base: ' + base
        else:
            log(ctx, 'troca de rótulo', ' — Dispositivo: ' + disp, '(nada)', 'operação 2 da seção 7; base só doutrinária (marca deletada)')
            texto = claim
        assert not re.search(r'Anexo|BASE DOUTRIN|SEM FONTE|\bv2\b|\bR[12]\b|QA PENDENTE|sem fonte', texto), (n, texto)
        eid = 'P1-DA-' + cb[1:].split('-')[0]
        out.append(dict(itemEdital=eid, rotulo=EDITAL[eid], texto=texto))
    assert vistos_drop == set(DROP_PEG), vistos_drop
    assert len(out) == 67, len(out)
    return out

# ---------------------------------------------------------------- itens
def monta_itens(L):
    i51 = achar(L, '### 5.1'); i52 = achar(L, '### 5.2', i51); fim = achar(L, '## 6.', i52)
    enun = {}
    for l in L[i51:i52]:
        m = re.match(r'^\*\*(D3-\d\d)\.\*\* (.+)$', l)
        if m: enun[m.group(1)] = m.group(2)
    blocos, cur = [], None
    for l in L[i52:fim]:
        m = re.match(r'^\*\*(D3-\d\d)\*\* \(folha ([\d.]+)\) — AUTORAL — (.*)$', l)
        if m: cur = dict(id=m.group(1), folha=m.group(2), cab=m.group(3), F={}); blocos.append(cur); continue
        if cur is not None and l.startswith('- '):
            k, _, v = l[2:].partition(': ')
            cur['F'][k] = v
    assert len(blocos) == 71 and len(enun) == 71, (len(blocos), len(enun))
    JUST_EDIT = {
     'D3-73': [('O item não traz troca: a ilegalidade', 'O item não traz troca; a ilegalidade', 'pontuação (nenhuma palavra alterada)',
                'a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula (mesmo tratamento dado no D1, item D1-01)')],
     'D3-79': [('Não há troca: o § 1º traz', 'Não há troca; o § 1º traz', 'pontuação (nenhuma palavra alterada)',
                'a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula (mesmo tratamento dado no D1, item D1-01)')],
    }
    itens = []
    for b in sorted(blocos, key=lambda x: int(x['id'].split('-')[1])):
        i = b['id']
        assert b['F']['Folha'] == b['folha']
        j1, j2 = b['F']['Justificativa (linha 1)'].strip(), b['F']['Justificativa (linha 2)'].strip()
        j = j1 + ' ' + j2
        for ant, nov, tipo, motivo in JUST_EDIT.get(i, []):
            j = edita('justificativa ' + i, j, ant, nov, tipo, motivo)
        marcas = b['F']['Marcas']
        vol = ('REVERIFICAR=sim' in marcas) or ('VOLÁTIL=sim' in marcas)
        it = dict(id=i, rotulo='AUTORAL', certame='Projeto Câmara 2026', cargo='Noções de Direito Administrativo e Administração Pública', ano=2026,
                  numero=int(i.split('-')[1]), comando='Julgue o item a seguir.', textoBase='', enunciado=enun[i],
                  gabarito=b['F']['Gabarito'].strip(), justificativa=j, itemEdital='P1-DA-' + b['folha'], aderencia='direta', url=URL_CANON)
        if vol: it['volatil'] = True
        it['_marcas'] = marcas; it['_j1'] = j1; it['_j2'] = j2
        itens.append(it)
    return itens

# ---------------------------------------------------------------- montagem
def monta():
    LOG.clear()
    L = ler_canon()
    partes = parse_curso(L)
    curso, mapa = monta_curso(partes)
    resumo = monta_resumo(L)
    pares = monta_pares(L)
    pegs = monta_pegadinhas(L)
    itens = monta_itens(L)
    ie = ['P1-DA-' + p['folha'] for p in partes]
    assert ie == ['P1-DA-5.1', 'P1-DA-5.2', 'P1-DA-6.1', 'P1-DA-6.2', 'P1-DA-6.3', 'P1-DA-6.4', 'P1-DA-6.5', 'P1-DA-7'], ie
    lote = dict(id='D3', nome=NOME, prova='P1', itensEdital=ie, resumo=resumo, curso=curso,
                pares=[{k: v for k, v in p.items() if not k.startswith('_')} for p in pares], pegadinhas=pegs)
    if TOPICOS.exists():
        tp = json.loads(TOPICOS.read_text(encoding='utf-8'))
        if set(tp) != set(ie): raise SystemExit('PARAR: chaves de D3_topicos_fonte.json diferem dos blocos ##: ' + str(sorted(set(tp) ^ set(ie))))
        topicos = {k: tp[k] for k in ie}
    else:
        topicos = {}
        print('AVISO: D3_topicos_fonte.json ainda não existe; topicos vazio')
    itens_pub = [{k: v for k, v in it.items() if not k.startswith('_')} for it in itens]
    dados = dict(lote=lote, itens=itens_pub, topicos=topicos)
    return dados, dict(L=L, partes=partes, mapa=mapa, itens=itens, pares=pares, pegs=pegs, resumo=resumo, curso=curso)

def grava(dados):
    SAIDA_JSON.write_text(json.dumps(dados, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

# ---------------------------------------------------------------- registro
def roda(cmd):
    r = subprocess.run([sys.executable, '-I'] + cmd, capture_output=True, text=True, cwd=str(RAIZ))
    return r.returncode, (r.stdout + r.stderr).strip()

def registro(dados, ctx):
    rc_val, val = roda([str(VALIDADOR), str(SAIDA_JSON), str(CANON), str(MAPA)])
    rc_fid, fid = roda([str(CONFERE)])
    it = dados['itens']
    por_folha = Counter(x['itemEdital'] for x in it)
    n_c = sum(1 for x in it if x['gabarito'] == 'C'); n_e = len(it) - n_c
    vol = [x['id'] for x in it if x.get('volatil')]
    por_peg = Counter(p['itemEdital'] for p in dados['lote']['pegadinhas'])
    W = []
    W.append('# D3_registro_formato.md — T-76 (ordem DA 20/10/2026) — 2026-10-20 — gerado por gcb-cpp')
    W.append('')
    W.append('Reformatação do Lote D3 (Poderes administrativos, responsabilidade civil do Estado e improbidade, itens 5 a 7 do edital) para o formato da plataforma (FORMATO_PLATAFORMA_DA.md). Só forma; nenhum conteúdo novo. Gerado por `saida/gcb/DA_plataforma/scripts/formatar_D3.py --registro`; fidelidade por `saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D3.py`.')
    W.append('')
    W.append('## 1. Fontes e conferências')
    W.append(f'- Canônico: saida/gcb/D3_v2_1.md, SHA-256 {sha(CANON.read_bytes())} (igual ao esperado 0f7a8b09…8930: o script confere antes de ler e pararia se divergisse).')
    W.append(f'- Base normativa: saida/gcb/D3_anexo_N_mapa_normativo.md (consulta de 20/10/2026), SHA-256 {sha(MAPA.read_bytes())}; usado só pelo validador e pelos visuais baseLegal (texto copiado letra a letra, `literal: true`, `conferido: 2026-10-20`).')
    W.append('- Seções do canônico NÃO usadas: 0 e 0.1 (resposta ao R1 e registro de acatamento), o cabeçalho e as convenções do início do arquivo, o parágrafo introdutório da seção 1, o cabeçalho das seções 3 e 4 (contagens e faixas de código de produção), 5.1 (só o enunciado é lido daqui), 6 (proveniência), 7 (contagens), 8 (bloco à Gerência), as linhas Folha, Ponto de julgamento, Formato, Base, Mecanismo, Troca, Difere, Alteração na v2 e Marcas de cada item, e as colunas "Código" e "Base" dos pares.')
    W.append(f'- JSON gerado: D3_plataforma.json, SHA-256 {sha(SAIDA_JSON.read_bytes())}; tópicos incorporados de D3_topicos_fonte.json, SHA-256 {sha(TOPICOS.read_bytes())} (escritos à mão).')
    W.append('')
    W.append('## 2. Correspondência bloco de origem → ## / ###')
    W.append('| Origem (D3_v2_1.md, seção 1) | Destino no curso |')
    W.append('|---|---|')
    for m in ctx['mapa']:
        W.append(f"| {m['origem'].replace('|', '/')} | `{m['destino']}` |" if m['destino'].startswith(('#', '`')) else f"| {m['origem'].replace('|', '/')} | {m['destino']} |")
    W.append('')
    W.append('Regras gerais do curso: "- Definição:" → quadro DEFINIÇÃO (em lista, sem linha em branco, quando a definição tem 3 ou mais frases: operação 4; em parágrafo único nos demais casos); BASE LEGAL em lista com os dispositivos que a base da própria pegadinha ("[Desfeita por: …]") cita, com a norma repetida em cada linha ("Lei 8.429/1992, art. 12, caput, I, II e III"); omitido nos blocos só doutrinários (a base era só a marca BASE DOUTRINÁRIA, como no D1); "- Exemplo (Legislativo, hipotético):" → EXEMPLO PARLAMENTAR (acrescentada a frase "O exemplo é hipotético." onde o original não a trazia, para manter a qualificação que estava no rótulo; omitido onde o original diz "não se aplica"); "- Pegadinha provável: … [Desfeita por: X]" → PEGADINHA PROVÁVEL com "Base: X" (sem "Base" quando X era só a marca BASE DOUTRINÁRIA). Código de bloco ("C5.1-01 ") removido do título. Títulos `##`: texto do edital em maiúsculas (nenhum passa de 90 caracteres). Resumo: seção 2 inteira. Pares: seção 3, 31 (a coluna "Código" e a coluna "Base" não entram; `a` = primeiro termo do campo "Par", `b` = os demais unidos por " × " — P-58 tem três termos); `como` = coluna Diferença + " Como a banca troca: " + coluna "Como a banca troca". Pegadinhas: seção 4, sem número, sem código do bloco e sem marca de versão; " — Dispositivo: X" vira " Base: X"; `itemEdital` pelo bloco ([C5.1-01] → P1-DA-5.1; [C7-xx] → P1-DA-7).')
    W.append('')
    W.append('## 3. Deleções e trocas (cada uma registrada)')
    W.append('Tipos: deleção de marca (v2, R1/R2, QA PENDENTE, leitura externa, Anexo N, BASE DOUTRINÁRIA, códigos); deleção de frase inteira ou de oração (processo, "[SEM FONTE]", cobertura do lote); deleção de bloco inteiro; troca mínima (op. 6); troca de rótulo (operação 2).')
    W.append('')
    ERRS = [e for e in LOG if e['motivo'].startswith('errata de forma')]
    GER = [e for e in LOG if not e['motivo'].startswith('errata de forma')]
    por_tipo = Counter(e['tipo'] for e in GER)
    W.append('Contagem por tipo (sem as da errata, seção "Errata de forma"): ' + '; '.join(f'{k}: {v}' for k, v in sorted(por_tipo.items())) + '.')
    W.append('')
    k = 0
    for e in GER:
        if e['tipo'] in ('troca de rótulo', 'quadro omitido'): continue
        k += 1
        dep = ('→ `' + e['depois'] + '`') if e['depois'] else '→ (nada)'
        W.append(f"{k}. [{e['ctx']}] {e['tipo']}: `{e['antes']}` {dep}. Motivo: {e['motivo']}.")
    W.append('')
    n_cur = sum(1 for e in LOG if e['tipo'] == 'troca de rótulo' and e['ctx'].startswith('curso') and e['ctx'].endswith('(pegadinha)'))
    n_ex = sum(1 for e in LOG if e['tipo'] == 'troca de rótulo' and e['ctx'].startswith('curso') and e['ctx'].endswith('(exemplo)'))
    n_ex_fr = sum(1 for e in LOG if e['tipo'] == 'troca de rótulo' and e['ctx'].endswith('(exemplo)') and e['adicionado'])
    n_pg = sum(1 for e in LOG if e['tipo'] == 'troca de rótulo' and e['ctx'].startswith('pegadinha'))
    n_om = sum(1 for e in LOG if e['tipo'] == 'quadro omitido')
    W.append(f'Trocas de rótulo (operação 2): {n_cur} pegadinhas do curso ("[Desfeita por: X]" → "Base: X", ou sem "Base" quando X era só a marca BASE DOUTRINÁRIA), {n_ex} exemplos do curso (rótulo → quadro EXEMPLO PARLAMENTAR; em {n_ex_fr} deles acrescentada a frase "O exemplo é hipotético.") e {n_pg} pegadinhas da lista consolidada (" — Dispositivo: X" → " Base: X"). Quadros EXEMPLO PARLAMENTAR omitidos por "não se aplica": {n_om}.')
    W.append('')
    W.append('Decisões de leitura que o orquestrador pode querer revisar (nenhuma altera conteúdo normativo):')
    W.append('- Quatro blocos do curso (poder de polícia delegado a particulares; temas jurisprudenciais das folhas 6.1 e 6.2; regime da omissão e temas conexos) tinham como definição só a frase "[SEM FONTE — não afirmar]" e uma nota sobre o Anexo N e o lote; o exemplo era "não se aplica" e a pegadinha, "afirmar, sem fonte, tese de tribunal". Tirada a frase marcada, nada resta: os blocos e as suas quatro pegadinhas da lista consolidada não entram (nenhuma tese de tribunal, como pede a ordem). Os demais pontos "[SEM FONTE]" (frases dentro de blocos com outro conteúdo) saíram só como frase.')
    W.append('- Remissões a ADI: o curso e o resumo trazem, como no canônico, a nota de que o texto compilado de certos dispositivos da Lei 8.429 remete a ADI, só a letra, sem efeito afirmado. Mantidas por serem informação sobre o texto legal (não há tese de tribunal nem efeito afirmado) e por constarem do original; nenhum desses dispositivos entra em BASE LEGAL nem em baseLegal. Se a ordem for retirar também as notas de ADI do texto exibido, é deleção de oração em C7-02, C7-04, C7-09, C7-14, C7-15, C7-16, C7-17, C7-18, C7-19, C7-20 e no resumo.')
    W.append('- "recorte" (recorte do despacho do lote) trocado por "curso" em C5.1-01 e C5.1-05, como o D1 fez com "lote"; no título de C6.5-01 a oração "e ausência de texto no recorte" saiu.')
    W.append('- Remissões "desta folha" (C6.2-02) e "da folha 6.1" (C6.4-04): mantidas na primeira entrega e TRATADAS PELA ERRATA DE 20/10/2026 (seção "Errata de forma": a primeira frase sai, a segunda passa a "do subitem 6.1").')
    W.append('- "Registro: 28 dispositivos revogados … e 9 vetados" (C7-20) e "(26)" dispositivos com remissão a ADI (resumo) são contagens literais do canônico; mantidas, só saiu a referência ao Anexo N.')
    W.append('- Resumo: os títulos "### 2.1/2.2 Item …" viraram linhas em negrito ("**Item 5 — …**"), como nos resumos do D1 e do D5; o título repetido "### 2.3" saiu (a linha em negrito do item 7 do próprio canônico fica).')
    W.append('- Enunciados: o canônico não separa texto-base nem traz comando por item: `textoBase` "" e `comando` "Julgue o item a seguir." (o canônico só traz "Julgue cada item como Certo ou Errado." no cabeçalho da seção 5.1).')
    W.append('- Ordem dos itens no JSON: crescente pelo id (D3-01 a D3-81, sem os 10 retirados), como pede a seção 4 da especificação; no canônico os itens seguem a ordem de apresentação fixada pela Gerência.')
    W.append('')
    W.append('## 4. Itens')
    W.append(f'- Total {len(it)}; C {n_c} / E {n_e}.')
    W.append('- Por itemEdital: ' + '; '.join(f'{k}: {v}' for k, v in sorted(por_folha.items(), key=lambda kv: list(EDITAL).index(kv[0]))) + '.')
    W.append('- volatil true: ' + (', '.join(vol) if vol else 'nenhum (todas as linhas "Marcas:" trazem REVERIFICAR=não e VOLÁTIL=não; coerente com o canônico)') + '.')
    W.append(f'- Justificativa: linhas 1 e 2 unidas por um espaço; a única edição é a pontuação de D3-73 e D3-79 ("troca:" → "troca;", nenhuma palavra alterada); as demais {len(it) - 2} são idênticas às duas linhas. As linhas "Difere de …" e "Mecanismo" são campos à parte no canônico e não entram.')
    W.append(f"- Pares: {len(dados['lote']['pares'])}; pegadinhas: {len(dados['lote']['pegadinhas'])} (" + '; '.join(f'{k}: {v}' for k, v in sorted(por_peg.items(), key=lambda kv: list(EDITAL).index(kv[0]))) + f"); tópicos: {len(dados['topicos'])} ({', '.join(dados['topicos'])}).")
    W.append('')
    W.append('## 5. Saída do validador')
    W.append('Comando: `python3 -I saida/gcb/DA_plataforma/scripts/validar_da.py saida/gcb/DA_plataforma/D3_plataforma.json saida/gcb/D3_v2_1.md saida/gcb/D3_anexo_N_mapa_normativo.md`')
    W.append('```')
    W.append(val)
    W.append('```')
    W.append('')
    W.append('## 6. Conferência de fidelidade')
    W.append('Comando: `python3 -I saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D3.py`')
    W.append('')
    W.append(fid)
    W.append('')
    W.append('## Errata de forma — QA final 20/10/2026')
    W.append('Origem: QA final do pacote v1.13 (gbq-cqe, 20/10/2026), achado 1: a palavra de produção "folha" no texto exibido (a candidata não conhece "folha"; o validador passou a acusá-la). Regra da ordem: frase que só fala do processo ou da organização da produção é DELETADA; remissão útil ao estudo vira "subitem". Só forma: nenhum enunciado, gabarito, itemEdital ou id foi tocado.')
    W.append('')
    for i, e in enumerate(ERRS, 1):
        dep = ('→ `' + e['depois'] + '`') if e['depois'] else '→ (nada)'
        W.append(f"{i}. [{e['ctx']}] {e['tipo']}: `{e['antes']}` {dep}. Motivo: {e['motivo']}.")
    W.append('')
    W.append(f'Total: {len(ERRS)} mudanças no D3 (curso). Resumo, pares, pegadinhas, justificativas e tópicos do D3 não tinham a palavra "folha" nem código R/F. A conferência de fidelidade (lista de passagens independente) foi atualizada com as duas mesmas passagens.')
    W.append('')
    REGISTRO.write_text('\n'.join(W) + '\n', encoding='utf-8')
    print(val)
    print(fid.splitlines()[-1] if fid else '(sem saída)')
    return rc_val, rc_fid

def main():
    dados, ctx = monta()
    grava(dados)
    print('gravado', SAIDA_JSON, sha(SAIDA_JSON.read_bytes()))
    if '--registro' in sys.argv:
        rc_val, rc_fid = registro(dados, ctx)
        sys.exit(0 if rc_val == 0 and rc_fid == 0 else 1)

main()
