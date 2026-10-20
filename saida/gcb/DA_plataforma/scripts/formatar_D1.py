# formatar_D1.py — T-73 (ordem DA 20/10/2026) — 2026-10-20 — gerado por gcb-cpp
# Reformata o canônico saida/gcb/D1_v2.md para o formato da plataforma (FORMATO_PLATAFORMA_DA.md).
# Só reformatação: nenhum conteúdo novo. Toda deleção e troca de palavra é registrada (LOG) e vai ao registro.
# Uso:  python3 -I formatar_D1.py              -> grava D1_plataforma.json
#       python3 -I formatar_D1.py --registro   -> regrava o JSON, roda validador e conferência de fidelidade e grava D1_registro_formato.md
import re, sys, json, hashlib, pathlib, subprocess
from collections import Counter

RAIZ = pathlib.Path(__file__).resolve().parents[4]
DA = RAIZ / 'saida/gcb/DA_plataforma'
CANON = RAIZ / 'saida/gcb/D1_v2.md'
MAPA = RAIZ / 'saida/gcb/D1_anexo_N_mapa_normativo.md'
SHA_CANON = '63bd27c34baec035dd39904ef565f6b5a662c0a30886a4a3d0b13b8b702e3d56'
URL_CANON = 'saida/gcb/D1_v2.md'
SAIDA_JSON = DA / 'D1_plataforma.json'
TOPICOS = DA / 'D1_topicos_fonte.json'
REGISTRO = DA / 'D1_registro_formato.md'
VALIDADOR = DA / 'scripts/validar_da.py'

NOME = 'Direito Administrativo — Estado, Administração Pública e ato administrativo (itens 1 e 2 do edital)'

# ---------------------------------------------------------------- leitura
def sha(b): return hashlib.sha256(b).hexdigest()

def ler_canon():
    raw = CANON.read_bytes()
    if sha(raw) != SHA_CANON:
        print('PARAR: SHA-256 de saida/gcb/D1_v2.md diverge:', sha(raw), '!=', SHA_CANON); sys.exit(2)
    return raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n').split('\n')

EDITAL = {e['id']: e['texto'] for e in json.loads((DA / 'edital_DA.json').read_text(encoding='utf-8'))}

def achar(L, prefixo, ini=0):
    for i in range(ini, len(L)):
        if L[i].startswith(prefixo): return i
    raise SystemExit('PARAR: seção não encontrada: ' + prefixo)

# ---------------------------------------------------------------- registro de edições
LOG = []   # {ctx, tipo, antes, depois, adicionado, motivo}
def log(ctx, tipo, antes, depois, motivo, adicionado=''):
    LOG.append(dict(ctx=ctx, tipo=tipo, antes=antes, depois=depois, motivo=motivo, adicionado=adicionado))

def edita(ctx, txt, antigo, novo, tipo, motivo, adicionado=''):
    assert txt.count(antigo) == 1, (ctx, antigo[:60], txt.count(antigo))
    log(ctx, tipo, antigo.strip(), novo.strip(), motivo, adicionado)
    return txt.replace(antigo, novo)

D_FRASE = 'deleção de frase inteira'
D_ORACAO = 'deleção de oração de processo'
D_MARCA = 'deleção de marca'
TROCA = 'troca mínima'
M_SEMFONTE = '"[SEM FONTE — não afirmar]": marca e frase marcada saem (seção 6)'
M_LOTE = 'fala do lote/da produção (cobertura de itens, regra de redação ou fonte de produção); não é conteúdo para a candidata (seção 6)'

# edições explícitas, por bloco do curso e campo ('def' = definição)
EXPL = {
 ('1.0.4', 'def'): [
  (' O § 4º do art. 18 tem remissão "Vide" à LC 230/2026, cujo texto o Anexo N não transcreveu além da ementa; qualquer afirmação sobre ela é [SEM FONTE — não afirmar] neste lote.', '', D_FRASE, M_SEMFONTE + '; a frase também cita o Anexo N'),
 ],
 ('1.1.1', 'def'): [
  (' Regra de redação do lote: nenhum item qualifica princípio como "explícito" ou "implícito" sem dizer o referencial (CF art. 37 × Lei 9.784, art. 2º), pela lição do BQ-0131 (anulado).', '', D_FRASE, 'regra de redação de itens do lote, com código de item do banco (BQ-0131); só processo'),
 ],
 ('1.1.2', 'def'): [
  ('Observação do Anexo R: a ligação desse parágrafo com o princípio da impessoalidade é leitura doutrinária, e o lote não a usa como modelo de item de letra de lei.',
   'A ligação desse parágrafo com o princípio da impessoalidade é leitura doutrinária.', TROCA,
   'sai a marca "Observação do Anexo R:" e a oração "e o lote não a usa como modelo de item de letra de lei" (processo); fica a leitura doutrinária'),
 ],
 ('1.1.5', 'def'): [
  (' Súmulas e julgados sobre autotutela: [SEM FONTE — não afirmar] neste lote (sem URL oficial datada).', '', D_FRASE, M_SEMFONTE),
 ],
 ('1.2.3', 'def'): [
  ('Registro do Anexo N (seção 6.8): a Lei 13.303/2016', 'A Lei 13.303/2016', D_MARCA, 'sai a marca "Registro do Anexo N (seção 6.8):" (referência de produção); a letra minúscula inicial passa a maiúscula'),
  ('Este lote não decide qual redação prevalece', 'Este curso não decide qual redação prevalece', TROCA, '"lote" é referência de produção (seção 6); trocado por "curso", que o próprio texto já usa; ressalva mantida', 'curso'),
  (' A natureza jurídica da fundação pública (direito público ou privado) é questão de interpretação que o lote não explora: [SEM FONTE — não afirmar]; o curso atribui ao DL 200, art. 5º, IV, o que ele diz.', '', D_FRASE, M_SEMFONTE + '; o aviso seguinte ("Aviso: não generalizar o DL 200, art. 5º, IV…") é mantido'),
 ],
 ('1.2.5', 'def'): [
  (': em item de conceito, o lote ancora o enunciado na "doutrina corrente"', '', D_ORACAO, 'oração sobre como o lote redige itens; fica "que a doutrina denomina desconcentração."'),
  ('; o lote não as cobra em item', '', D_ORACAO, 'oração sobre cobertura de itens do lote; fica "as definições variam entre autores."'),
 ],
 ('2.1.2', 'def'): [
  ('Observação do Anexo R: o enquadramento do vício de forma como defeito sanável é leitura doutrinária; o lote não o usa como modelo de item de letra de lei.',
   'O enquadramento do vício de forma como defeito sanável é leitura doutrinária.', TROCA,
   'sai a marca "Observação do Anexo R:" e a oração "o lote não o usa como modelo de item de letra de lei" (processo); fica a leitura doutrinária'),
 ],
 ('2.1.3', 'def'): [
  (' O lote só usa em item a presunção de legitimidade e sua natureza relativa.', '', D_FRASE, 'cobertura de itens do lote; só processo'),
 ],
 ('2.1.4', 'def'): [
  (' e não viram item neste lote', '', D_ORACAO, 'cobertura de itens do lote; fica "variam entre autores."'),
 ],
 ('2.1.6', 'def'): [
  (' (contexto do curso, sem item na v2: o ponto de julgamento é próximo ao do BQ-0137)', '', D_ORACAO, 'parêntese de processo, com "v2" e código de item do banco (BQ-0137); fica a teoria dos motivos determinantes'),
 ],
 ('2.1.7', 'def'): [
  (' Súmulas do STF sobre controle de legalidade pela Administração: [SEM FONTE — não afirmar] neste lote.', '', D_FRASE, M_SEMFONTE),
 ],
 ('2.2.1', 'def'): [
  (' Classificação doutrinária dos pareceres (facultativo, obrigatório, vinculante) e posições de tribunal sobre o tema: contexto, [SEM FONTE — não afirmar] neste lote por falta de URL oficial datada; não viram item.', '', D_FRASE, M_SEMFONTE),
 ],
 ('2.2.2', 'def'): [
  ('; o lote não afirma o conteúdo dos parágrafos vetados nem usa a mensagem de veto, não aberta pelo qa-normativo-da',
   '; o curso não afirma o conteúdo dos parágrafos vetados', TROCA,
   '"lote" trocado por "curso"; sai a oração "nem usa a mensagem de veto, não aberta pelo qa-normativo-da" (nome de agente e processo)', 'curso'),
  (' Posições de tribunal sobre a responsabilidade do parecerista: [SEM FONTE — não afirmar] neste lote.', '', D_FRASE, M_SEMFONTE),
 ],
}

RX_ANEXO = re.compile(r'\s?\(Anexo N, [^)]*\)')
RX_BD = re.compile(r'BASE DOUTRINÁRIA \([^)]*\): ')

def limpa_generico(ctx, txt):
    """Deleta '(Anexo N, …)' e o rótulo 'BASE DOUTRINÁRIA (…): ' (marcas, seção 6); registra cada ocorrência."""
    def anexo(m):
        log(ctx, D_MARCA, m.group(0).strip(), '', 'referência ao Anexo N (seção 6)')
        return ''
    txt = RX_ANEXO.sub(anexo, txt)
    while True:
        m = RX_BD.search(txt)
        if not m: break
        antes, depois = txt[:m.start()], txt[m.end():]
        cap = antes == '' or antes.endswith('. ')
        if cap: depois = depois[:1].upper() + depois[1:]
        log(ctx, D_MARCA, m.group(0).strip(), '', 'marca "BASE DOUTRINÁRIA" com o parêntese que a qualifica (seção 6; o parêntese traz também fala de processo, como "teto do lote"); ' +
            ('a letra minúscula seguinte passa a maiúscula' if cap else 'sem mais mudança'))
        txt = antes + depois
    return txt

# ---------------------------------------------------------------- BASE LEGAL (só o que o bloco já cita)
BASE_LEGAL = {
 '1.0.1': ['CF, art. 1º, caput', 'CF, art. 1º, I', 'CF, art. 18, caput'],
 '1.0.2': [],
 '1.0.3': ['CF, art. 2º, caput'],
 '1.0.4': ['CF, art. 18, caput', 'CF, art. 18, § 1º', 'CF, art. 18, § 2º'],
 '1.0.5': ['CF, art. 1º, I a V', 'CF, art. 1º, parágrafo único'],
 '1.1.1': ['CF, art. 37, caput', 'Lei 9.784/1999, art. 2º, caput'],
 '1.1.2': ['CF, art. 37, § 1º'],
 '1.1.3': ['Lei 9.784/1999, art. 2º, caput', 'Lei 9.784/1999, art. 2º, parágrafo único, I, II, III, V, VI, VII e XIII'],
 '1.1.4': ['Lei 9.784/1999, art. 1º, caput', 'Lei 9.784/1999, art. 1º, § 1º'],
 '1.1.5': ['CF, art. 37, caput', 'Lei 9.784/1999, art. 2º, parágrafo único, I e II', 'Lei 9.784/1999, art. 53'],
 '1.2.1': ['Lei 9.784/1999, art. 1º, § 2º, I, II e III'],
 '1.2.2': ['DL 200/1967, art. 4º, I, II e parágrafo único'],
 '1.2.3': ['CF, art. 37, XIX e XX', 'DL 200/1967, art. 5º, I, II, III e IV', 'Lei 13.303/2016, arts. 3º e 4º'],
 '1.2.4': ['Lei 11.107/2005, art. 6º, I e II', 'Lei 11.107/2005, art. 6º, § 1º', 'Lei 11.107/2005, art. 6º, § 2º'],
 '1.2.5': ['DL 200/1967, art. 6º, III', 'DL 200/1967, art. 10, caput', 'DL 200/1967, art. 10, § 1º'],
 '2.1.1': [],
 '2.1.2': ['Lei 4.717/1965, art. 2º, caput e parágrafo único, a a e'],
 '2.1.3': [],
 '2.1.4': [],
 '2.1.5': ['Lei 9.784/1999, art. 11', 'Lei 9.784/1999, art. 12 e parágrafo único', 'Lei 9.784/1999, art. 13', 'Lei 9.784/1999, art. 14, § 1º, § 2º e § 3º', 'Lei 9.784/1999, art. 15', 'Lei 9.784/1999, art. 17'],
 '2.1.6': ['Lei 9.784/1999, art. 50, I a VIII, § 1º e § 3º', 'LINDB, art. 20, parágrafo único'],
 '2.1.7': ['Lei 9.784/1999, art. 53', 'LINDB, art. 21'],
 '2.1.8': ['Lei 9.784/1999, art. 54, caput, § 1º e § 2º', 'Lei 9.784/1999, art. 55', 'Lei 9.784/1999, art. 53'],
 '2.2.1': ['Lei 9.784/1999, art. 42, caput, § 1º e § 2º'],
 '2.2.2': ['LINDB, art. 28, caput'],
 '2.2.3': ['Lei 9.784/1999, art. 50, VII e § 1º'],
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
    partes, bloco, campo = [], None, None
    for l in L[ini + 1:fim]:
        m = re.match(r'^### PARTE (\d\.\d) — ', l)
        if m:
            partes.append(dict(cod=m.group(1), titulo_origem=l[4:], blocos=[])); bloco = None; continue
        m = re.match(r'^\*\*(\d\.\d\.\d) (.+)\*\*$', l)
        if m:
            bloco = dict(cod=m.group(1), titulo=m.group(2), linhas=[l], campos={}); partes[-1]['blocos'].append(bloco); continue
        if l.strip() == '---': continue
        if bloco is not None and l.strip():
            bloco['linhas'].append(l)
            for chave, pref in (('def', '- Definição: '), ('ex', '- Exemplo (Legislativo, hipotético): '), ('peg', '- Pegadinha provável: ')):
                if l.startswith(pref): bloco['campos'][chave] = l[len(pref):]; break
            else:
                raise SystemExit('PARAR: linha inesperada no curso: ' + l[:80])
    for p in partes:
        for b in p['blocos']:
            assert set(b['campos']) == {'def', 'ex', 'peg'}, b['cod']
            assert b['cod'].startswith(p['cod'] + '.'), (b['cod'], p['cod'])
    return partes

def monta_curso(partes):
    out, mapa = [], []
    for p in partes:
        eid = 'P1-DA-' + ('1' if p['cod'] == '1.0' else p['cod'])
        num = eid[6:]
        out.append(f'## {num} {titulo_edital(eid)}'); out.append('')
        mapa.append(dict(origem='PARTE ' + p['cod'], destino='## ' + num + ' ' + titulo_edital(eid), eid=eid, nivel='##'))
        for b in p['blocos']:
            ctx = 'curso ' + b['cod']
            tit = b['titulo']
            d = b['campos']['def']; e = b['campos']['ex']; g = b['campos']['peg']
            for (blk, campo), lst in EXPL.items():
                if blk == b['cod'] and campo == 'def':
                    for ant, nov, tipo, motivo, *ad in lst:
                        d = edita(ctx + ' (definição)', d, ant, nov, tipo, motivo, ad[0] if ad else '')
            d = limpa_generico(ctx + ' (definição)', d)
            e = limpa_generico(ctx + ' (exemplo)', e)
            # exemplo: o rótulo "Exemplo (Legislativo, hipotético)" vira o quadro; a qualificação "hipotético" é mantida em frase
            log(ctx + ' (exemplo)', 'troca de rótulo', 'Exemplo (Legislativo, hipotético):', 'quadro EXEMPLO PARLAMENTAR + "O exemplo é hipotético."',
                'operação 2 da seção 7; a frase preserva a qualificação "hipotético" que estava no rótulo', 'O exemplo é hipotético.')
            e = e.rstrip() + ' O exemplo é hipotético.'
            m = re.fullmatch(r'(.*?) \[Desfeita por: (.+)\]', g)
            assert m, (b['cod'], g)
            log(ctx + ' (pegadinha)', 'troca de rótulo', '[Desfeita por: ' + m.group(2) + ']', 'Base: ' + m.group(2), 'operação 2 da seção 7', 'Base:')
            g = m.group(1) + ' Base: ' + m.group(2)
            for campo_txt in (d, e, g):
                assert 'Anexo' not in campo_txt and 'BASE DOUTRIN' not in campo_txt and 'SEM FONTE' not in campo_txt, (b['cod'], campo_txt[:80])
            sub = re.sub(r'^\d\.\d\.\d ', '', tit)
            out.append('### ' + sub); out.append('')
            mapa.append(dict(origem=b['cod'] + ' ' + tit, destino='### ' + sub, eid=eid, nivel='###'))
            out.append('DEFINIÇÃO')
            ss = sentencas(d)
            if len(ss) >= 3: out.extend('- ' + s for s in ss)
            else: out.append(d)
            out.append('')
            if BASE_LEGAL[b['cod']]:
                out.append('BASE LEGAL'); out.extend('- ' + x for x in BASE_LEGAL[b['cod']]); out.append('')
            out.append('EXEMPLO PARLAMENTAR'); out.append(e); out.append('')
            out.append('PEGADINHA PROVÁVEL'); out.append(g); out.append('')
            b['saida'] = dict(titulo=sub, d=d, e=e, g=g)
    while out and out[-1] == '': out.pop()
    return '\n'.join(out), mapa

# ---------------------------------------------------------------- resumo, pares, pegadinhas
def monta_resumo(L):
    ini = achar(L, '## 2. (b) RESUMO'); fim = achar(L, '---', ini)
    linhas = [l for l in L[ini + 1:fim]]
    while linhas and not linhas[0].strip(): linhas.pop(0)
    while linhas and not linhas[-1].strip(): linhas.pop()
    txt = '\n'.join(linhas)
    txt = edita('resumo', txt, 'o lote não decide qual prevalece', 'o curso não decide qual prevalece', TROCA, '"lote" é referência de produção (seção 6); trocado por "curso"', 'curso')
    txt = limpa_generico('resumo', txt)
    n = txt.count(' (BASE DOUTRINÁRIA)')
    assert n == 4, n
    for _ in range(n): log('resumo', D_MARCA, '(BASE DOUTRINÁRIA)', '', 'marca "BASE DOUTRINÁRIA" (seção 6)')
    txt = txt.replace(' (BASE DOUTRINÁRIA)', '')
    return txt

def monta_pares(L):
    ini = achar(L, '## 3. (c) PARES'); fim = achar(L, '## 4. PEGADINHAS', ini)
    pares, item = [], None
    for l in L[ini:fim]:
        if l.startswith('### Item'): item = l[4:]; continue
        if not l.startswith('|') or l.startswith('| Par |') or l.startswith('|---'): continue
        cel = [c.strip() for c in l.strip().strip('|').split('|')]
        assert len(cel) == 4, l[:60]
        par, dif, base, banca = cel
        assert par.count(' × ') == 1, par
        a, b = par.split(' × ')
        ctx = 'par ' + par
        if 'O lote não decide qual redação prevalece.' in dif:
            dif = edita(ctx, dif, 'O lote não decide qual redação prevalece.', 'O curso não decide qual redação prevalece.', TROCA, '"lote" é referência de produção (seção 6); trocado por "curso"', 'curso')
        dif = limpa_generico(ctx, dif)
        banca = limpa_generico(ctx, banca)
        assert dif.endswith('.') and banca.endswith('.'), par
        pares.append(dict(a=a, b=b, como=dif + ' Como a banca troca: ' + banca, _item=item))
    return pares

CODIGO_FOLHA = {'1.0': 'P1-DA-1', '1.1': 'P1-DA-1.1', '1.2': 'P1-DA-1.2', '2.1': 'P1-DA-2.1', '2.2': 'P1-DA-2.2'}

def monta_pegadinhas(L):
    ini = achar(L, '## 4. PEGADINHAS'); fim = achar(L, '---', ini)
    out = []
    for l in L[ini + 1:fim]:
        if not l.strip(): continue
        m = re.match(r'^(\d+)\. \[(\d\.\d)\] (.+)$', l)
        assert m, l[:60]
        eid = CODIGO_FOLHA[m.group(2)]
        out.append(dict(itemEdital=eid, rotulo=EDITAL[eid], texto=m.group(3)))
    return out

# ---------------------------------------------------------------- itens
def monta_itens(L):
    i51 = achar(L, '### 5.1'); i52 = achar(L, '### 5.2', i51); fim = achar(L, '## 6.', i52)
    enun = {}
    for l in L[i51:i52]:
        m = re.match(r'^\*\*(D1-\d{2})\.\*\* (.+)$', l)
        if m: enun[m.group(1)] = m.group(2)
    itens, cur = [], None
    blocos = []
    for l in L[i52:fim]:
        m = re.match(r'^\*\*(D1-\d{2})\*\* \(subitem (\d\.\d)\) — AUTORAL — (.*)$', l)
        if m: cur = dict(id=m.group(1), sub=m.group(2), cab=m.group(3), L={}); blocos.append(cur); continue
        if cur is not None and l.startswith('- '):
            k, _, v = l[2:].partition(': ')
            cur['L'][k] = v
    assert len(blocos) == 60 and len(enun) == 60, (len(blocos), len(enun))
    JUST_EDIT = {
     'D1-01': [('Não há troca: a tentação', 'Não há troca; a tentação', 'pontuação (nenhuma palavra alterada)',
                'a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula')],
     'D1-09': [(', evitando a ambiguidade explícito × implícito do BQ-0131', '', D_ORACAO,
                'oração que só compara com outro item do banco (BQ-0131); a seção 7 manda deixar fora; fica "O referencial (caput do art. 37) está dito no enunciado; a troca é um único princípio a mais."')],
    }
    for b in blocos:
        i = b['id']
        j1, j2 = b['L']['Justificativa (linha 1)'], b['L']['Justificativa (linha 2)']
        j = j1.strip() + ' ' + j2.strip()
        for ant, nov, tipo, motivo in JUST_EDIT.get(i, []):
            j = edita('justificativa ' + i, j, ant, nov, tipo, motivo)
        marcas = b['L']['Marcas']
        vol = ('REVERIFICAR=sim' in marcas) or ('VOLÁTIL=sim' in marcas) or ('REVERIFICAR' in b['cab']) or ('VOLÁTIL' in b['cab'])
        it = dict(id=i, rotulo='AUTORAL', certame='Projeto Câmara 2026', cargo='Noções de Direito Administrativo e Administração Pública', ano=2026,
                  numero=int(i.split('-')[1]), comando='Julgue o item a seguir.', textoBase='', enunciado=enun[i],
                  gabarito=b['L']['Gabarito'].strip(), justificativa=j, itemEdital=CODIGO_FOLHA[b['sub']], aderencia='direta', url=URL_CANON)
        if vol: it['volatil'] = True
        itens.append(it)
        it['_marcas'] = marcas; it['_j1'] = j1; it['_j2'] = j2
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
    ie = []
    for p in partes:
        eid = 'P1-DA-' + ('1' if p['cod'] == '1.0' else p['cod'])
        ie.append(eid)
    lote = dict(id='D1', nome=NOME, prova='P1', itensEdital=ie, resumo=resumo, curso=curso,
                pares=[{k: v for k, v in p.items() if not k.startswith('_')} for p in pares], pegadinhas=pegs)
    if TOPICOS.exists():
        tp = json.loads(TOPICOS.read_text(encoding='utf-8'))
        topicos = {k: tp[k] for k in ie if k in tp}
        if set(tp) != set(ie): print('AVISO: chaves de D1_topicos_fonte.json diferem dos blocos ##:', sorted(set(tp) ^ set(ie)))
    else:
        topicos = {}
        print('AVISO: D1_topicos_fonte.json ainda não existe; topicos vazio')
    itens_pub = [{k: v for k, v in it.items() if not k.startswith('_')} for it in itens]
    dados = dict(lote=lote, itens=itens_pub, topicos=topicos)
    return dados, dict(L=L, partes=partes, mapa=mapa, itens=itens, pares=pares, pegs=pegs, resumo=resumo, curso=curso)

def grava(dados):
    SAIDA_JSON.write_text(json.dumps(dados, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

# ---------------------------------------------------------------- conferência de fidelidade
def tok(s): return re.findall(r'\w+', s.lower())

def fidelidade(dados, ctx):
    """Para cada bloco/campo: palavras do texto de saída (menos rótulos de quadro e listas BASE LEGAL) contra as do bloco de origem."""
    rel, falhas = [], 0
    log_por_ctx = {}
    for e in LOG: log_por_ctx.setdefault(e['ctx'].split(' (')[0], []).append(e)
    ROT = {'DEFINIÇÃO', 'BASE LEGAL', 'EXEMPLO PARLAMENTAR', 'PEGADINHA PROVÁVEL'}
    for p in ctx['partes']:
        for b in p['blocos']:
            src = Counter(tok('\n'.join(b['linhas'])))
            s = b['saida']
            out = Counter(tok(s['titulo'] + '\n' + s['d'] + '\n' + s['e'] + '\n' + s['g']))
            ev = log_por_ctx.get('curso ' + b['cod'], [])
            permitido = Counter()
            for e in ev: permitido += Counter(tok(e['adicionado']))
            adicionadas = (out - src) - permitido
            esperado_removido = Counter()
            for e in ev: esperado_removido += (Counter(tok(e['antes'])) - Counter(tok(e['depois'])))
            esperado_removido += Counter(tok(b['cod']))  # código do bloco
            esperado_removido += Counter(['definição', 'exemplo', 'legislativo', 'hipotético', 'pegadinha', 'provável', 'desfeita', 'por'])  # rótulos
            removidas = (src - out) - esperado_removido
            # BASE LEGAL: todo token tem de estar no bloco
            bl_fora = [t for x in BASE_LEGAL[b['cod']] for t in tok(x) if t not in src]
            ok = not adicionadas and not removidas and not bl_fora
            falhas += (not ok)
            rel.append((b['cod'], ok, dict(adicionadas), dict(removidas_nao_registradas=dict(removidas)), bl_fora))
    return rel, falhas

def fidelidade_demais(dados, ctx):
    rel, falhas = [], 0
    # resumo
    sec = [l for l in ctx['L']]
    ini = achar(sec, '## 2. (b) RESUMO'); fim = achar(sec, '---', ini)
    src = Counter(tok('\n'.join(sec[ini + 1:fim])))
    out = Counter(tok(dados['lote']['resumo']))
    ev = [e for e in LOG if e['ctx'] == 'resumo']
    perm = Counter(); [perm.update(tok(e['adicionado'])) for e in ev]
    rem = Counter(); [rem.update(Counter(tok(e['antes'])) - Counter(tok(e['depois']))) for e in ev]
    ad, rm = (out - src) - perm, (src - out) - rem
    rel.append(('resumo', not ad and not rm, dict(ad), dict(rm))); falhas += bool(ad or rm)
    # pares: texto de saída contra as colunas Diferença + Como a banca troca (mais as palavras fixas)
    ini = achar(sec, '## 3. (c) PARES'); fim = achar(sec, '## 4. PEGADINHAS', ini)
    for k, p in enumerate(ctx['pares']):
        linha = [l for l in sec[ini:fim] if l.startswith('| ' + p['a'] + ' × ' + p['b'] + ' |')]
        assert len(linha) == 1, p['a']
        cel = [c.strip() for c in linha[0].strip().strip('|').split('|')]
        src = Counter(tok(cel[1] + ' ' + cel[3]))
        o = dados['lote']['pares'][k]
        out = Counter(tok(o['como']))
        ev = [e for e in LOG if e['ctx'] == 'par ' + cel[0]]
        perm = Counter(tok('Como a banca troca')); [perm.update(tok(e['adicionado'])) for e in ev]
        rem = Counter(); [rem.update(Counter(tok(e['antes'])) - Counter(tok(e['depois']))) for e in ev]
        ad, rm = (out - src) - perm, (src - out) - rem
        okp = not ad and not rm and o['a'] == p['a'] and o['b'] == p['b']
        rel.append(('par ' + cel[0], okp, dict(ad), dict(rm))); falhas += (not okp)
    # pegadinhas: texto idêntico ao da lista (menos número e código de folha)
    ini = achar(sec, '## 4. PEGADINHAS'); fim = achar(sec, '---', ini)
    linhas = [l for l in sec[ini + 1:fim] if l.strip()]
    for k, (l, o) in enumerate(zip(linhas, dados['lote']['pegadinhas'])):
        m = re.match(r'^\d+\. \[\d\.\d\] (.+)$', l)
        okp = m.group(1) == o['texto']
        rel.append((f'pegadinha {k + 1}', okp, {}, {})); falhas += (not okp)
    # justificativas: duas linhas do original contra o texto de saída
    for it, pub in zip(ctx['itens'], dados['itens']):
        src = Counter(tok(it['_j1'] + ' ' + it['_j2']))
        out = Counter(tok(pub['justificativa']))
        ev = [e for e in LOG if e['ctx'] == 'justificativa ' + it['id']]
        perm = Counter(); [perm.update(tok(e['adicionado'])) for e in ev]
        rem = Counter(); [rem.update(Counter(tok(e['antes'])) - Counter(tok(e['depois']))) for e in ev]
        ad, rm = (out - src) - perm, (src - out) - rem
        okj = not ad and not rm
        rel.append(('justificativa ' + it['id'], okj, dict(ad), dict(rm))); falhas += (not okj)
    return rel, falhas

# ---------------------------------------------------------------- registro
def registro(dados, ctx):
    r = subprocess.run([sys.executable, '-I', str(VALIDADOR), str(SAIDA_JSON), str(CANON), str(MAPA)], capture_output=True, text=True, cwd=str(RAIZ))
    val = (r.stdout + r.stderr).strip()
    relc, fc = fidelidade(dados, ctx)
    reld, fd = fidelidade_demais(dados, ctx)
    mapa_sha = sha(MAPA.read_bytes().replace(b'\r\n', b'\n').replace(b'\r', b'\n'))
    it = dados['itens']
    por_item = Counter(x['itemEdital'] for x in it)
    n_c = sum(1 for x in it if x['gabarito'] == 'C'); n_e = sum(1 for x in it if x['gabarito'] == 'E')
    vol = [x['id'] for x in it if x.get('volatil')]
    W = []
    W.append('# D1_registro_formato.md — T-73 (ordem DA 20/10/2026) — 2026-10-20 — gerado por gcb-cpp')
    W.append('')
    W.append('Reformatação do Lote D1 para o formato da plataforma (FORMATO_PLATAFORMA_DA.md). Só forma; nenhum conteúdo novo. Gerado por `saida/gcb/DA_plataforma/scripts/formatar_D1.py --registro`.')
    W.append('')
    W.append('## 1. Fontes e conferências')
    W.append(f'- Canônico: saida/gcb/D1_v2.md, SHA-256 {sha(CANON.read_bytes())} (igual ao esperado 63bd27c3…3d56: conferido pelo script antes de ler; se divergisse, o script pararia).')
    W.append(f'- Base normativa: saida/gcb/D1_anexo_N_mapa_normativo.md, SHA-256 em disco {sha(MAPA.read_bytes())} (normalizado CRLF→LF: {mapa_sha}; o arquivo não tem CR). Usado apenas pelo validador e pelo visual baseLegal. Atenção: a reconciliação de 17/10/2026 e a linha 4 do canônico registram o SHA do Anexo N iniciado em 71aea65f…; o arquivo em disco hoje inicia em {sha(MAPA.read_bytes())[:8]}…. Divergência registrada, não resolvida aqui; a data de consulta 17/10/2026 e os textos dos dispositivos usados em baseLegal foram lidos do arquivo em disco.')
    W.append('- Seções do canônico NÃO usadas: 0 (resposta ao R1), 6 (proveniência), 7 (contagens), 8 (bloco à Gerência), os "Pendentes", a linha "Item real análogo" e as linhas Base e Mecanismo de cada item.')
    W.append(f'- JSON gerado: D1_plataforma.json, SHA-256 {sha(SAIDA_JSON.read_bytes())}; topicos incorporados de D1_topicos_fonte.json, SHA-256 {sha(TOPICOS.read_bytes()) if TOPICOS.exists() else "ausente"}.')
    W.append('')
    W.append('## 2. Correspondência bloco de origem → ## / ###')
    W.append('| Origem (D1_v2.md, seção 1) | Destino no curso |')
    W.append('|---|---|')
    for m in ctx['mapa']:
        W.append(f"| {m['origem']} | `{m['destino']}` |")
    W.append('')
    W.append('Regras gerais do curso: "- Definição:" → quadro DEFINIÇÃO (em lista, sem linha em branco, quando a definição tem 3 ou mais frases: operação 4); BASE LEGAL em lista com os dispositivos que o próprio bloco cita (título, definição e "[Desfeita por]"), omitida nos blocos só doutrinários (' + ', '.join(k for k, v in BASE_LEGAL.items() if not v) + '); "- Exemplo (Legislativo, hipotético):" → EXEMPLO PARLAMENTAR; "- Pegadinha provável: … [Desfeita por: X]" → PEGADINHA PROVÁVEL com "Base: X". Títulos `##`: texto do edital em maiúsculas (P1-DA-1 e P1-DA-1.2 cortados no primeiro ":" por passarem de 90 caracteres). Resumo: seção 2 inteira (Item 1 e Item 2), uma só cadeia markdown. Pares: seção 3, 11 + 11; `como` = coluna Diferença + " Como a banca troca: " + coluna "Como a banca troca"; a coluna Base não entra (a seção 2 da especificação só prevê esses dois textos). Pegadinhas: seção 4, sem número e sem o código da folha.')
    W.append('')
    W.append('## 3. Deleções e trocas (cada uma registrada)')
    W.append('Tipos: deleção de marca (referência ao Anexo N, rótulo BASE DOUTRINÁRIA com seu parêntese); deleção de frase inteira ou de oração (processo, SEM FONTE); troca mínima; troca de rótulo (operação 2).')
    W.append('')
    por_tipo = Counter(e['tipo'] for e in LOG)
    W.append('Contagem por tipo: ' + '; '.join(f'{k}: {v}' for k, v in sorted(por_tipo.items())) + '.')
    W.append('')
    # agrupar entradas genéricas repetidas por (ctx, antes)
    for k, e in enumerate([x for x in LOG if x['tipo'] != 'troca de rótulo'], 1):
        dep = ('→ `' + e['depois'] + '`') if e['depois'] else '→ (nada)'
        W.append(f"{k}. [{e['ctx']}] {e['tipo']}: `{e['antes']}` {dep}. Motivo: {e['motivo']}.")
    W.append('')
    W.append('Trocas de rótulo (operação 2): ' + str(sum(1 for x in LOG if x['tipo'] == 'troca de rótulo' and 'exemplo' in x['ctx'])) + ' exemplos ("O exemplo é hipotético." acrescentada a cada um para manter a qualificação que estava no rótulo "Exemplo (Legislativo, hipotético):"; a frase é o texto padrão que a seção 6 permite) e ' + str(sum(1 for x in LOG if x['tipo'] == 'troca de rótulo' and 'pegadinha' in x['ctx'])) + ' pegadinhas ("[Desfeita por: X]" → "Base: X").')
    W.append('')
    W.append('Itens: "Item real análogo" (BQ-…) e "Mecanismo" não entram (fora do conjunto de campos da seção 4). Marcas [TS], "QA PENDENTE", "BASE DOUTRINÁRIA" do cabeçalho de cada item não entram. Enunciado e gabarito: literais. Justificativa: linhas 1 e 2 unidas por um espaço; as duas edições acima (D1-01 e D1-09) são as únicas. Os 58 demais são idênticos às duas linhas.')
    W.append('')
    W.append('Observações de leitura (nenhuma é defeito do validador nem alteração de texto):')
    W.append('- itensEdital traz os 5 ids com bloco de curso (P1-DA-1, 1.1, 1.2, 2.1, 2.2); o lote não tem curso do caput do item 2 (a v2 não tem PARTE 2.0), e por isso P1-DA-2 não aparece em itensEdital, em topicos nem em itemEdital de item. Nenhum item cai no caput 2 (os itens 2.x são todos de 2.1 ou 2.2).')
    W.append('- Comando de todos os itens: "Julgue o item a seguir." (o canônico só traz "Julgue cada item como Certo ou Errado." no cabeçalho da seção 5.1, sem comando por item); textoBase vazio (o canônico não separa situação hipotética).')
    W.append('- Mantidas, por terem sentido ordinário e não de produção: "compilados" (textos consolidados da lei, 1.2.3 e resumo), "itens" (os exercícios da plataforma, 1.2.2 e 1.2.3) e "troca" (várias justificativas).')
    W.append('- A palavra "troca" aparece como palavra comum em várias justificativas ("a troca sutil é…", "Não há troca…"); só a sequência literal "troca:" foi tratada (D1-01).')
    W.append('')
    W.append('## 4. Itens')
    W.append(f'- Total {len(it)}; C {n_c} / E {n_e}.')
    W.append('- Por itemEdital: ' + '; '.join(f'{k}: {v}' for k, v in sorted(por_item.items())) + '.')
    W.append('- volatil true: ' + (', '.join(vol) if vol else 'nenhum (todas as linhas "Marcas:" trazem REVERIFICAR=não e VOLÁTIL=não; coerente com a reconciliação)') + '.')
    W.append(f"- Pares: {len(dados['lote']['pares'])}; pegadinhas: {len(dados['lote']['pegadinhas'])}; topicos: {len(dados['topicos'])} ({', '.join(dados['topicos'])}).")
    W.append('')
    W.append('## 5. Saída do validador')
    W.append('Comando: `python3 -I saida/gcb/DA_plataforma/scripts/validar_da.py saida/gcb/DA_plataforma/D1_plataforma.json saida/gcb/D1_v2.md saida/gcb/D1_anexo_N_mapa_normativo.md`')
    W.append('```')
    W.append(val)
    W.append('```')
    W.append('')
    W.append('## 6. Conferência de fidelidade (palavras de saída × palavras de origem)')
    W.append('Método: para cada bloco do curso, multiconjunto de palavras (minúsculas, sem pontuação) da saída (título, definição, exemplo, pegadinha; sem os rótulos de quadro e sem as listas BASE LEGAL) contra o do bloco de origem. "Acrescentada" = palavra a mais na saída que não venha de troca registrada; "removida não registrada" = palavra a menos que não venha de deleção registrada, de código de bloco ou de rótulo de origem. BASE LEGAL: cada palavra tem de existir no bloco de origem. O mesmo método vale para resumo, pares, justificativas; pegadinhas são comparadas por igualdade de texto.')
    W.append('')
    W.append('| Bloco | Resultado | Acrescentadas | Removidas não registradas | BASE LEGAL fora do bloco |')
    W.append('|---|---|---|---|---|')
    for cod, ok, ad, rm, bl in relc:
        W.append(f"| {cod} | {'OK' if ok else 'FALHA'} | {ad or '—'} | {rm['removidas_nao_registradas'] or '—'} | {bl or '—'} |")
    W.append('')
    W.append('| Outros campos | Resultado | Acrescentadas | Removidas não registradas |')
    W.append('|---|---|---|---|')
    outros_falha = [x for x in reld if not x[1]]
    W.append(f"| resumo, {len(ctx['pares'])} pares, {len(ctx['pegs'])} pegadinhas, {len(it)} justificativas ({len(reld)} verificações) | {'OK' if not outros_falha else 'FALHA'} | {'—' if not outros_falha else outros_falha} | — |")
    W.append('')
    W.append(f'Resultado: {len(relc)} blocos do curso, {fc} com diferença; {len(reld)} outras verificações, {fd} com diferença.')
    W.append(f'Palavras acrescentadas fora das trocas registradas: {"nenhuma" if (fc == 0 and fd == 0) else "VER TABELA"}.')
    W.append('')
    REGISTRO.write_text('\n'.join(W) + '\n', encoding='utf-8')
    print(val)
    print(f'fidelidade: blocos {len(relc)} (falhas {fc}); outros {len(reld)} (falhas {fd})')
    for x in relc + reld:
        if not x[1]: print('DIFERENÇA', x)
    return r.returncode, fc + fd

def main():
    dados, ctx = monta()
    grava(dados)
    print('gravado', SAIDA_JSON, sha(SAIDA_JSON.read_bytes()))
    if '--registro' in sys.argv:
        rc, fd = registro(dados, ctx)
        sys.exit(0 if rc == 0 and fd == 0 else 1)

main()
