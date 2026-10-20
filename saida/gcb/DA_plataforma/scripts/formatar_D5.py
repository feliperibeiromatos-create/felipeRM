# formatar_D5.py — T-74 (ordem DA 20/10/2026) — 2026-10-20 — gerado por gcb-cpp
# Reformata o canônico saida/gcb/D5_v2_1.md para o formato da plataforma (FORMATO_PLATAFORMA_DA.md).
# Só reformatação: nenhum conteúdo novo. Toda deleção e troca de palavra é registrada (LOG) e vai ao registro.
# Determinístico. Os tópicos são escritos à mão em D5_topicos_fonte.json e incorporados aqui.
# Uso:  python3 -I saida/gcb/DA_plataforma/scripts/formatar_D5.py              -> grava D5_plataforma.json
#       python3 -I saida/gcb/DA_plataforma/scripts/formatar_D5.py --registro   -> regrava o JSON, roda o validador e a
#                                                                                conferência de fidelidade e grava D5_registro_formato.md
import hashlib, json, pathlib, re, subprocess, sys
from collections import Counter

RAIZ = pathlib.Path(__file__).resolve().parents[4]
DA = RAIZ / 'saida/gcb/DA_plataforma'
CANON = RAIZ / 'saida/gcb/D5_v2_1.md'
MAPA = RAIZ / 'saida/gcb/D5_anexo_N_mapa_normativo.md'
SHA_CANON = '44ddcc982642df66b246108cb7e3ef86031e8a99762aa2262a6c0bdde24e1333'
URL_CANON = 'saida/gcb/D5_v2_1.md'
SAIDA_JSON = DA / 'D5_plataforma.json'
TOPICOS = DA / 'D5_topicos_fonte.json'
REGISTRO = DA / 'D5_registro_formato.md'
VALIDADOR = DA / 'scripts/validar_da.py'
CONFERE = DA / 'scripts/conferir_fidelidade_D5.py'

NOME = 'Direito Administrativo — Licitações e contratos (item 10 do edital)'
NORMA = 'Lei 14.133/2021'

def sha(b): return hashlib.sha256(b).hexdigest()

def ler_canon():
    raw = CANON.read_bytes()
    if sha(raw) != SHA_CANON:
        print('PARAR: SHA-256 de saida/gcb/D5_v2_1.md diverge:', sha(raw), '!=', SHA_CANON); sys.exit(2)
    return raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n').split('\n')

EDITAL = {e['id']: e['texto'] for e in json.loads((DA / 'edital_DA.json').read_text(encoding='utf-8'))}

def achar(L, prefixo, ini=0):
    for i in range(ini, len(L)):
        if L[i].startswith(prefixo): return i
    raise SystemExit('PARAR: seção não encontrada: ' + prefixo)

# ---------------------------------------------------------------- registro de edições
LOG = []   # {ctx, tipo, antes, depois, motivo}
def log(ctx, tipo, antes, depois, motivo):
    LOG.append(dict(ctx=ctx, tipo=tipo, antes=antes, depois=depois, motivo=motivo))

def edita(ctx, txt, antigo, novo, tipo, motivo):
    assert txt.count(antigo) == 1, (ctx, antigo[:70], txt.count(antigo))
    log(ctx, tipo, antigo.strip(), novo.strip(), motivo)
    return txt.replace(antigo, novo)

D_MARCA = 'deleção de marca'
D_FRASE = 'deleção de frase inteira'
D_ORACAO = 'deleção de oração de processo'
TROCA = 'troca mínima (op. 6)'
M_LOTE = 'fala do lote (cobertura de itens, cruzamento com item do banco ou nota de produção); não é conteúdo para a candidata (seção 6)'
M_SEMFONTE = '"[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6)'
M_COD = 'remissão a código de bloco do curso (seção 6)'
E_SUB = 'errata de forma (QA final 20/10/2026, achado 1): "folha" é termo de produção (seção 6); a remissão serve ao estudo e passa a "subitem", o número 10.6/10.7 é o do `##` do curso'

# edições explícitas no curso, por bloco e campo ('def' = definição; 'peg' = pegadinha)
EXPL = {
 ('C10.1-03', 'def'): [
  (' (nota do Anexo N, seção 7, item 11)', '', D_MARCA, 'referência ao Anexo N e à sua seção (seção 6); fica "Conceito e finalidade: o art. 6º não traz definição isolada…"'),
 ],
 ('C10.1-08', 'def'): [
  ('; aqui, os cobrados no lote', '', D_ORACAO, M_LOTE + '; fica "(rol de incisos)"'),
  ('; os valores atualizados em vigor em 2/10/2026 estão NÃO CONFERIDOS no Anexo N: [SEM FONTE — não afirmar]', '', D_ORACAO,
   M_SEMFONTE + '; a oração também cita o Anexo N ("NÃO CONFERIDOS no Anexo N"); ficam o que a lei fixa em reais e a regra de atualização do art. 182'),
  ('REVERIFICAR: o art. 75, XVI', 'O art. 75, XVI', D_MARCA, 'marca REVERIFICAR (seção 6); a letra minúscula inicial passa a maiúscula; o conteúdo do inciso XVI é mantido'),
  (' Nenhum item deste lote se apoia nesse inciso.', '', D_FRASE, M_LOTE),
 ],
 ('C10.1-08', 'peg'): [
  ('; afirmar valor atualizado sem conferência', '', D_ORACAO,
   'a oração só faz sentido com a frase "[SEM FONTE — não afirmar]" sobre os valores atualizados, que a seção 6 manda tirar; sem ela a pegadinha ficaria sem objeto (registrada também na lista consolidada, pegadinha 8)'),
 ],
 ('C10.1-10', 'def'): [
  (' e não é desenvolvido neste lote (ver o registro de acatamento, seção 0.1)', '', D_ORACAO, M_LOTE + '; cita "lote" e a seção 0.1 do canônico; fica "O modo de disputa (aberto ou fechado) pertence à fase de propostas e lances."'),
 ],
 ('C10.1-12', 'def'): [
  (' O art. 79, que trata das hipóteses de uso do credenciamento, tem o inciso IV, o § 1º (caput e inciso VII, com as alíneas) e o § 2º com redação dada ou incluída pela Lei 15.266/2025, marcados REVERIFICAR no Anexo N; o artigo não é usado neste lote.', '', D_FRASE,
   'frase só de processo: marca REVERIFICAR, "Anexo N" e "lote" (seção 6); sobre artigo que o próprio texto diz não usar'),
 ],
 ('C10.1-13', 'def'): [
  (' (O inciso I e o § 1º, fornecedor exclusivo e documento idôneo, são ponto do item real BQ-0113 e não são repetidos em item; o inciso III e o § 4º estão em C10.1-07.)', '', D_FRASE, M_LOTE + '; cita item do banco (BQ-0113) e código de bloco (C10.1-07)'),
 ],
 ('C10.1-14', 'def'): [
  (' (usados em C10.1-08)', '', D_MARCA, M_COD),
  ('; valor atualizado NÃO CONFERIDO no Anexo N: [SEM FONTE — não afirmar]', '', D_ORACAO, M_SEMFONTE + '; a oração também cita o Anexo N; fica "(sujeito à atualização do art. 182)"'),
 ],
 ('C10.4-01', 'def'): [
  ('; valor atualizado NÃO CONFERIDO no Anexo N', '', D_ORACAO, 'cita "Anexo N" (seção 6) e é a mesma ressalva "NÃO CONFERIDO" (sem fonte); fica "(a Lei 14.133 fixa o valor-limite em reais, sujeito à atualização do art. 182)"'),
 ],
 ('C10.4-05', 'def'): [
  (' Qualquer afirmação sobre atribuições do gestor vem de regulamento não aberto neste Anexo: [SEM FONTE — não afirmar].', '', D_FRASE, M_SEMFONTE + '; a frase também cita o Anexo'),
  ('estão na folha 10.6.', 'estão no subitem 10.6.', TROCA, E_SUB),
 ],
 ('C10.5-03', 'def'): [
  ('estão na folha 10.7.)', 'estão no subitem 10.7.)', TROCA, E_SUB),
 ],
 ('C10.5-04', 'def'): [
  ('está na folha 10.7.)', 'está no subitem 10.7.)', TROCA, E_SUB),
 ],
 ('C10.4-07', 'def'): [
  (' (A regra e a ressalva do art. 121, §§ 1º e 2º, estão em C10.4-03.)', '', D_FRASE, M_COD),
 ],
 ('C10.4-09', 'def'): [
  (' (O recebimento provisório e definitivo, a rejeição do objeto e a responsabilidade pela solidez e segurança estão em C10.4-04.)', '', D_FRASE, M_COD),
 ],
 ('C10.5-07', 'def'): [
  (' (O planejamento de compras está em C10.5-04.)', '', D_FRASE, M_COD),
 ],
 ('C10.6-02', 'def'): [
  (', que já é objeto de item real do banco (BQ-0134) e não é repetido neste lote', '', D_ORACAO, M_LOTE + '; fica "está no § 2º."'),
 ],
 ('C10.6-04', 'def'): [
  (' (ponto do item real BQ-0135, não repetido)', '', D_FRASE, M_LOTE + '; cita item do banco (BQ-0135)'),
 ],
 ('C10.6-07', 'def'): [
  (' Este é o ponto do item real BQ-0134, que não é repetido em item deste lote; entra no curso e nas pegadinhas para completar o quadro das atribuições do fiscal (§ 1º em C10.6-02, § 3º em C10.6-03, § 4º em C10.6-04).', '', D_FRASE,
   M_LOTE + '; cita item do banco (BQ-0134) e códigos de bloco'),
 ],
 ('C10.7-02', 'def'): [
  (' (Requisitos da contratação e parcelamento, incisos III e VIII, são o ponto do item real BQ-0142.)', '', D_FRASE, M_LOTE + '; cita item do banco (BQ-0142)'),
 ],
 ('C10.7-05', 'def'): [
  ('; qualquer afirmação além da letra desses dispositivos fica fora do lote', '', D_ORACAO, M_LOTE + '; fica "A lei não restringe, no art. 6º, XXV, o projeto básico a uma categoria de objeto (fala em \'a obra ou o serviço\')."'),
 ],
}

RX_SUFIXO = [
 re.compile(r' — acréscimo da v2 \(leitura externa [^()]*; QA PENDENTE \(R2\)\)$'),
 re.compile(r' \[alterado na v2: [^\]]*\]$'),
]

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
        m = re.match(r'^### PARTE (1\.\d) — (10\.\d) (.+)$', l)
        if m:
            partes.append(dict(cod=m.group(1), folha=m.group(2), titulo_origem=l[4:], blocos=[])); bloco = None; continue
        m = re.match(r'^\*\*(C10\.\d-\d\d) (.+?)\*\*(.*)$', l)
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
            assert b['cod'].startswith('C' + p['folha'] + '-'), (b['cod'], p['folha'])
    return partes

def base_legal(titulo, peg_base):
    """Dispositivos entre parênteses do título do bloco; sem parêntese de artigo, os da lista 'Desfeita por'."""
    ps = [x for x in re.findall(r'\(([^()]*)\)', titulo) if x.startswith(('art', 'arts'))]
    itens = [y.strip() for x in ps for y in x.split('; ')]
    if not itens:
        b = peg_base.rstrip('.')
        assert b.startswith(NORMA + ', '), b
        itens = [y.strip() for y in b[len(NORMA) + 2:].split('; ')]
    return [f'{NORMA}, {x}' for x in itens]

def monta_curso(partes):
    out, mapa = [], []
    for p in partes:
        eid = 'P1-DA-' + p['folha']
        cab = f"## {p['folha']} {titulo_edital(eid)}"
        out += [cab, '']
        mapa.append(dict(origem=p['titulo_origem'], destino=cab))
        for b in p['blocos']:
            ctx = 'curso ' + b['cod']
            tit = b['titulo']
            suf = b['sufixo']
            if suf:
                assert any(rx.fullmatch(suf) or rx.search(suf) for rx in RX_SUFIXO), (b['cod'], suf)
                for rx in RX_SUFIXO:
                    if rx.search(suf):
                        log(ctx + ' (título)', D_MARCA, suf.strip(), '', 'marca de produção no título do bloco (seção 6: "v2", "R1", "R2", "QA PENDENTE", "leitura externa", código de item)')
                        suf = rx.sub('', suf)
                assert suf == '', (b['cod'], suf)
            d, e, g = b['campos']['def'], b['campos']['ex'], b['campos']['peg']
            for (blk, campo), lst in EXPL.items():
                if blk != b['cod']: continue
                for ant, nov, tipo, motivo in lst:
                    if campo == 'def': d = edita(ctx + ' (definição)', d, ant, nov, tipo, motivo)
                    else: g = edita(ctx + ' (pegadinha)', g, ant, nov, tipo, motivo)
            m = re.fullmatch(r'(.*?) \[Desfeita por: (.+)\]', g)
            assert m, (b['cod'], g[-80:])
            claim, base = m.group(1), m.group(2)
            log(ctx + ' (pegadinha)', 'troca de rótulo', '[Desfeita por: ' + base + ']', 'Base: ' + base, 'operação 2 da seção 7')
            g = claim + ' Base: ' + base
            assert e.endswith(('O exemplo é hipotético.', 'Os exemplos são hipotéticos.', 'Exemplos hipotéticos.')), (b['cod'], e[-60:])
            for campo_txt in (tit, d, e, g):
                assert not re.search(r'Anexo|BASE DOUTRIN|SEM FONTE|REVERIFICAR|BQ-|\bC10\.\d|QA PENDENTE|\bv2\b|\bR[12]\b|\blote\b|NÃO CONFERID', campo_txt), (b['cod'], campo_txt[:90])
            out += ['### ' + tit, '']
            mapa.append(dict(origem=f"{b['cod']} {tit}" + (f" {b['sufixo'].strip()}" if b['sufixo'] else ''), destino='### ' + tit))
            out.append('DEFINIÇÃO')
            ss = sentencas(d)
            if len(ss) >= 3: out.extend('- ' + s for s in ss)
            else: out.append(d)
            out.append('')
            bl = base_legal(tit, base)
            out.append('BASE LEGAL'); out.extend('- ' + x for x in bl); out.append('')
            out += ['EXEMPLO PARLAMENTAR', e, '', 'PEGADINHA PROVÁVEL', g, '']
            b['saida'] = dict(titulo=tit, d=d, e=e, g=g, base=bl)
    while out and out[-1] == '': out.pop()
    return '\n'.join(out), mapa

# ---------------------------------------------------------------- resumo
def monta_resumo(L):
    ini = achar(L, '## 2. (b) RESUMO'); fim = achar(L, '---', ini)
    linhas = list(L[ini + 1:fim])
    while linhas and not linhas[0].strip(): linhas.pop(0)
    while linhas and not linhas[-1].strip(): linhas.pop()
    txt = '\n'.join(linhas)
    # "Acrescentado na v2: x" -> "X" (marca "v2" sai; a letra minúscula inicial passa a maiúscula)
    def acresc(m):
        ini_, resto_ = m.group(1), m.group(2)
        log('resumo', D_MARCA, 'Acrescentado na v2: ' + ini_ + resto_ + '…', ini_.upper() + resto_ + '…', 'marca "v2" (seção 6): sai "Acrescentado na v2:" e a letra minúscula inicial passa a maiúscula; o texto que segue é mantido')
        return ini_.upper() + resto_
    txt, n = re.subn(r'(?<=\. )Acrescentado na v2: (.)(.{0,30})', acresc, txt)
    assert n == 7, n
    txt = edita('resumo', txt, '; só no curso, no par P-27 e na pegadinha G-71, sem item', '', D_ORACAO, 'remissão a códigos de par (P-27) e de pegadinha (G-71) e fala de cobertura de itens (seção 6)')
    txt = edita('resumo', txt, '| Número literal do Anexo N | Dispositivo |', '| Número literal | Dispositivo |', D_MARCA, 'sai "do Anexo N" do cabeçalho da tabela (seção 6); a tabela é mantida')
    txt = edita('resumo', txt, '; os valores vigentes em 2/10/2026 estão NÃO CONFERIDOS no Anexo N: [SEM FONTE — não afirmar]', '', D_ORACAO, M_SEMFONTE + '; a oração também cita o Anexo N; fica "Valores em reais: a Lei 14.133 fixa valores-limite (art. 75, I e II e § 7º; art. 95, § 2º), atualizados a cada 1º de janeiro pelo Poder Executivo federal (art. 182)."')
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
        if cod == 'P-08':
            dif = edita(ctx, dif, '; atribuições do gestor: [SEM FONTE — não afirmar]', '', D_ORACAO, M_SEMFONTE)
        if cod == 'P-27':
            dif = edita(ctx, dif, ' (O § 2º é o ponto do item real BQ-0134; este par não gera item.)', '', D_FRASE, M_LOTE + '; cita item do banco (BQ-0134)')
        termos = par.split(' × ')
        assert len(termos) >= 2, par
        a, b = termos[0], ' × '.join(termos[1:])
        assert dif.endswith('.') and banca.endswith('.'), cod
        pares.append(dict(a=a, b=b, como=dif + ' Como a banca troca: ' + banca, _cod=cod))
    assert len(pares) == 31, len(pares)
    return pares

PEG_SUF = re.compile(r' \[(?:alterada na v2|acréscimo da v2)\]')

def monta_pegadinhas(L):
    ini = achar(L, '## 4. (d) PEGADINHAS'); fim = achar(L, '---', ini)
    out = []
    for l in L[ini + 1:fim]:
        m = re.match(r'^G-(\d\d)\. \[C10\.(\d)-(\d\d)\] (.+)$', l)
        if not m: continue
        n, folha, t = int(m.group(1)), m.group(2), m.group(4)
        ctx = f'pegadinha {n}'
        ms = PEG_SUF.findall(t)
        for x in ms: log(ctx, D_MARCA, x.strip(), '', 'marca "v2" (seção 6)')
        t = PEG_SUF.sub('', t)
        if n == 8:
            t = edita(ctx, t, '; afirmar valor atualizado sem conferência', '', D_ORACAO, 'ver a mesma edição no bloco do curso (a oração dependia da frase "[SEM FONTE — não afirmar]")')
        claim, sep, disp = t.rpartition(' — Dispositivo: ')
        assert sep and disp.startswith(NORMA), l[:60]
        assert claim.endswith(('.', '?', '!')), (n, claim[-30:])
        log(ctx, 'troca de rótulo', ' — Dispositivo: ' + disp, ' Base: ' + disp, 'operação 2 da seção 7 (o rótulo "Dispositivo:" vira "Base:", como no curso e como no D6)')
        eid = 'P1-DA-10.' + folha
        out.append(dict(itemEdital=eid, rotulo=EDITAL[eid], texto=claim + ' Base: ' + disp))
    assert len(out) == 73, len(out)
    return out

# ---------------------------------------------------------------- itens
def monta_itens(L):
    i51 = achar(L, '### 5.1'); i52 = achar(L, '### 5.2', i51); fim = achar(L, '## 6.', i52)
    enun = {}
    for l in L[i51:i52]:
        m = re.match(r'^\*\*(D5-\d\d)\.\*\* (.+)$', l)
        if m: enun[m.group(1)] = m.group(2)
    blocos, cur = [], None
    for l in L[i52:fim]:
        m = re.match(r'^\*\*(D5-\d\d)\*\* \(folha (10\.\d)\) — AUTORAL — (.*)$', l)
        if m: cur = dict(id=m.group(1), folha=m.group(2), cab=m.group(3), F={}); blocos.append(cur); continue
        if cur is not None and l.startswith('- '):
            k, _, v = l[2:].partition(': ')
            cur['F'][k] = v
    assert len(blocos) == 70 and len(enun) == 70, (len(blocos), len(enun))
    JUST_EDIT = {
     'D5-04': [('Não há troca: o item', 'Não há troca; o item', 'pontuação (nenhuma palavra alterada)',
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
        if 'elemento-isca' in j:
            j = edita('justificativa ' + i, j, 'elemento-isca:', 'elemento que parece trocado:', TROCA,
                      '"elemento-isca" é marca de produção (seção 6); trocado pela expressão equivalente "elemento que parece trocado" (o canônico define o elemento-isca como o que a candidata tende a achar trocado); o restante da frase fica igual')
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
    assert ie == [f'P1-DA-10.{k}' for k in range(1, 8)], ie
    lote = dict(id='D5', nome=NOME, prova='P1', itensEdital=ie, resumo=resumo, curso=curso,
                pares=[{k: v for k, v in p.items() if not k.startswith('_')} for p in pares], pegadinhas=pegs)
    tp = json.loads(TOPICOS.read_text(encoding='utf-8'))
    if set(tp) != set(ie): raise SystemExit('PARAR: chaves de D5_topicos_fonte.json diferem dos blocos ##: ' + str(sorted(set(tp) ^ set(ie))))
    topicos = {k: tp[k] for k in ie}
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
    W.append('# D5_registro_formato.md — T-74 (ordem DA 20/10/2026) — 2026-10-20 — gerado por gcb-cpp')
    W.append('')
    W.append('Reformatação do Lote D5 (Licitações e contratos, item 10 do edital) para o formato da plataforma (FORMATO_PLATAFORMA_DA.md). Só forma; nenhum conteúdo novo. Gerado por `saida/gcb/DA_plataforma/scripts/formatar_D5.py --registro`; fidelidade por `saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D5.py`.')
    W.append('')
    W.append('## 1. Fontes e conferências')
    W.append(f'- Canônico: saida/gcb/D5_v2_1.md, SHA-256 {sha(CANON.read_bytes())} (igual ao esperado 44ddcc98…e1333: o script confere antes de ler e pararia se divergisse).')
    W.append(f'- Base normativa: saida/gcb/D5_anexo_N_mapa_normativo.md (consulta de 18/10/2026), SHA-256 {sha(MAPA.read_bytes())}; usado só pelo validador e pelo visual baseLegal (texto copiado letra a letra, `literal: true`, `conferido: 2026-10-18`).')
    W.append('- Seções do canônico NÃO usadas: 0 e 0.1 (resposta ao R1 e registro de acatamento), o parágrafo introdutório da seção 1, o cabeçalho das seções 3 e 4 (contagens de produção), 6 (proveniência), 7 (contagens), 8 (bloco à GCB), as linhas Folha, Ponto de julgamento, Formato, Base, Mecanismo, Troca, Alteração na v2, "Difere de BQ-…" e Marcas de cada item, e a coluna "Código"/"Base" dos pares.')
    W.append(f'- JSON gerado: D5_plataforma.json, SHA-256 {sha(SAIDA_JSON.read_bytes())}; tópicos incorporados de D5_topicos_fonte.json, SHA-256 {sha(TOPICOS.read_bytes())} (escritos à mão).')
    W.append('')
    W.append('## 2. Correspondência bloco de origem → ## / ###')
    W.append('| Origem (D5_v2_1.md, seção 1) | Destino no curso |')
    W.append('|---|---|')
    for m in ctx['mapa']:
        W.append(f"| {m['origem'].replace('|', '/')} | `{m['destino']}` |")
    W.append('')
    W.append('Regras gerais do curso: "- Definição:" → quadro DEFINIÇÃO (em lista, sem linha em branco, quando a definição tem 3 ou mais frases: operação 4; em parágrafo único nos demais casos); quadro BASE LEGAL em lista com os dispositivos que o próprio título do bloco cita entre parênteses ("(art. 28; arts. 29 a 32; art. 6º, XXXVIII a XLII)" → três linhas "- Lei 14.133/2021, art. 28" etc.; no bloco sem parêntese de artigo no título, C10.7-06, os dispositivos da lista "[Desfeita por: …]"); "- Exemplo (Legislativo, hipotético):" → EXEMPLO PARLAMENTAR (o canônico já termina cada exemplo com "O exemplo é hipotético." ou equivalente: mantido); "- Pegadinha provável: … [Desfeita por: X]" → PEGADINHA PROVÁVEL com "Base: X". Código de bloco ("C10.x-NN ") removido do título. Títulos `##`: texto do edital em maiúsculas (P1-DA-10.1 cortado no primeiro ":" por passar de 90 caracteres). Resumo: seção 2 inteira. Pares: seção 3, 31; `a`/`b` = termos do campo "Par" (a = primeiro; b = demais unidos por " × ", caso do P-14); `como` = coluna Diferença + " Como a banca troca: " + coluna "Como a banca troca"; a coluna Base não entra. Pegadinhas: seção 4, 73, sem número, sem código do bloco e sem marca de versão; " — Dispositivo: X" vira " Base: X"; `itemEdital` pelo bloco ([C10.x-NN] → P1-DA-10.x).')
    W.append('')
    W.append('## 3. Deleções e trocas (cada uma registrada)')
    W.append('Tipos: deleção de marca (v2, R1/R2, QA PENDENTE, leitura externa, Anexo N, REVERIFICAR, códigos); deleção de frase inteira ou de oração (processo, "[SEM FONTE]", cobertura do lote, cruzamento com item real do banco); troca mínima (op. 6); troca de rótulo (operação 2).')
    W.append('')
    ERRS = [e for e in LOG if e['motivo'].startswith('errata de forma')]
    GER = [e for e in LOG if not e['motivo'].startswith('errata de forma')]
    por_tipo = Counter(e['tipo'] for e in GER)
    W.append('Contagem por tipo (sem as da errata, seção "Errata de forma"): ' + '; '.join(f'{k}: {v}' for k, v in sorted(por_tipo.items())) + '.')
    W.append('')
    k = 0
    for e in GER:
        if e['tipo'] == 'troca de rótulo': continue
        k += 1
        dep = ('→ `' + e['depois'] + '`') if e['depois'] else '→ (nada)'
        W.append(f"{k}. [{e['ctx']}] {e['tipo']}: `{e['antes']}` {dep}. Motivo: {e['motivo']}.")
    W.append('')
    n_ex = sum(1 for e in LOG if e['tipo'] == 'troca de rótulo' and 'pegadinha' in e['ctx'] and e['ctx'].startswith('curso'))
    n_pg = sum(1 for e in LOG if e['tipo'] == 'troca de rótulo' and e['ctx'].startswith('pegadinha'))
    W.append(f'Trocas de rótulo (operação 2): {n_ex} pegadinhas do curso ("[Desfeita por: X]" → "Base: X") e {n_pg} pegadinhas da lista consolidada (" — Dispositivo: X" → " Base: X").')
    W.append('')
    W.append('Decisões de leitura que o orquestrador pode querer revisar (nenhuma altera conteúdo normativo):')
    W.append('- Valores em reais: o curso mantém o que a lei fixa (R$ 100.000,00 e R$ 50.000,00 no art. 75, I e II) e a regra de atualização do art. 182; saíram as orações "valor atualizado NÃO CONFERIDO … [SEM FONTE]". A pegadinha "afirmar valor atualizado sem conferência" (curso C10.1-08 e pegadinha 8) saiu pelo mesmo motivo.')
    W.append('- Marca REVERIFICAR em C10.1-08 (art. 75, XVI, redação da Lei 15.471/2026): a marca saiu e o conteúdo do inciso foi mantido, como o D6 fez com a Lei 15.141/2025. A frase sobre o art. 79 (C10.1-12), toda de marca e de cobertura, saiu inteira.')
    W.append('- Remissões "folha 10.6" e "folha 10.7" (C10.4-05, C10.5-03, C10.5-04) foram mantidas na primeira entrega e TRATADAS PELA ERRATA DE 20/10/2026 (seção "Errata de forma": "folha" vira "subitem"); os números 10.6 e 10.7 são os dos títulos `##` do curso. As remissões a código de bloco (C10.x-NN) saíram.')
    W.append('- Enunciados começam com "Considere…" e trazem a situação no próprio enunciado; o canônico não separa texto-base: `textoBase` "" e `comando` "Julgue o item a seguir." (o canônico só traz "Julgue cada item como Certo ou Errado." no cabeçalho da seção 5.1).')
    W.append('- Ordem dos itens no JSON: crescente pelo id (D5-01 a D5-53, D5-55 a D5-71), como pede a seção 4 da especificação; no canônico o D5-71 ocupa a posição 54.')
    W.append('')
    W.append('## 4. Itens')
    W.append(f'- Total {len(it)}; C {n_c} / E {n_e}.')
    W.append('- Por itemEdital: ' + '; '.join(f'{k}: {v}' for k, v in sorted(por_folha.items(), key=lambda kv: kv[0])) + '.')
    W.append('- volatil true: ' + (', '.join(vol) if vol else 'nenhum (todas as linhas "Marcas:" trazem REVERIFICAR=não e VOLÁTIL=não; coerente com a seção 7 do canônico)') + '.')
    ed_isca = sorted({e['ctx'].split(' ')[1] for e in LOG if e['ctx'].startswith('justificativa') and e['tipo'] == TROCA})
    W.append(f'- Justificativa: linhas 1 e 2 unidas por um espaço; edições: a pontuação de D5-04 ("Não há troca:" → "Não há troca;") e a troca mínima "elemento-isca:" → "elemento que parece trocado:" em {len(ed_isca)} itens ({", ".join(ed_isca)}); as demais {len(it) - 1 - len(ed_isca)} são idênticas às duas linhas. As linhas "Difere de BQ-…" e "Mecanismo" são campos à parte no canônico e não entram.')
    W.append(f"- Pares: {len(dados['lote']['pares'])}; pegadinhas: {len(dados['lote']['pegadinhas'])} (" + '; '.join(f'{k}: {v}' for k, v in sorted(por_peg.items())) + f"); tópicos: {len(dados['topicos'])} ({', '.join(dados['topicos'])}).")
    W.append('')
    W.append('## 5. Saída do validador')
    W.append('Comando: `python3 -I saida/gcb/DA_plataforma/scripts/validar_da.py saida/gcb/DA_plataforma/D5_plataforma.json saida/gcb/D5_v2_1.md saida/gcb/D5_anexo_N_mapa_normativo.md`')
    W.append('```')
    W.append(val)
    W.append('```')
    W.append('')
    W.append('## 6. Conferência de fidelidade')
    W.append('Comando: `python3 -I saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D5.py`')
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
    W.append(f'Total: {len(ERRS)} mudanças no D5 (curso). Resumo, pares, pegadinhas, justificativas e tópicos do D5 não tinham a palavra "folha" nem código R/F. A conferência de fidelidade (lista independente de passagens removidas) foi atualizada com as três mesmas trocas.')
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
