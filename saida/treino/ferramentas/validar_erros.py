# -*- coding: utf-8 -*-
"""T-59 (D-T59-02, D-T59-05, D-T59-06) — validador do arquivo "Exportar meus erros" (plataforma -> fábrica), formato `camara2026.erros` versão 1.
Implementa a seção 2 de regras/importacao_erros.md (itens 1 a 5) e lista os ids desconhecidos em relação ao pacote vigente. SOMENTE LEITURA:
não grava nada, não escreve em entrada/erros/. Só biblioteca-padrão (roda com `python3 -I`).
Versão mantida (D1 da GBQ, `saida/pacote/T59_T60_reconciliacao_2026-10-14.md`, D-R59-08). A cópia de `gerador_v1_5/` é registro da T-61 e não muda.

Uso:
  python3 -I validar_erros.py <arquivo.json> [--pacote <pacote.json>] [--importados <registro.json>] [--json]
    --pacote      pacote vigente (padrão: saida/pacote/pacote.json da raiz do repositório, derivada de __file__)
    --importados  JSON com uma lista de {"sha256": "...", "exportadoEm": "..."} das importações já feitas (detecta DUPLICADO)
    --json        saída em JSON em vez de texto
Código de saída: 0 ACEITO; 1 RECUSADO; 3 DUPLICADO; 2 erro de uso.

Veredito:
  RECUSADO   -- o arquivo não abre como JSON UTF-8, ou falta campo da tabela D-T59-02, ou o tipo está errado, ou `formato`/`versaoFormato` não são os conhecidos.
                `ne`/`tl` numéricos fora do domínio são incoerência da discursiva, não recusa (regra v1.1, 2.5); BOM inicial tolerado com aviso; `NaN`/`Infinity` recusados;
                ordem das listas gera aviso.
  DUPLICADO  -- mesmo SHA-256 ou mesmo `exportadoEm` de uma importação já feita (só com --importados).
  ACEITO     -- demais casos. Tentativas/entradas incoerentes (D-T59-05) são listadas com o motivo e ficam FORA dos cálculos (campo `fora_dos_calculos`);
                ids desconhecidos NÃO são descartados em silêncio: vão listados por campo, com a quantidade de ocorrências.
"""
import collections, datetime, hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PACOTE_PADRAO = os.path.join(REPO, 'saida', 'pacote', 'pacote.json')
ISO = re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$')
DATA = re.compile(r'^\d{4}-\d{2}-\d{2}$')


def is_int(x): return isinstance(x, int) and not isinstance(x, bool)
def is_num(x): return isinstance(x, (int, float)) and not isinstance(x, bool)
def is_str(x): return isinstance(x, str)
def is_iso(x):
    if not (is_str(x) and ISO.match(x)): return False
    try:
        datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%fZ'); return True
    except ValueError:
        return False


class Forma:
    """Acumula erros de forma (motivos de RECUSA)."""
    def __init__(self): self.erros = []
    def e(self, caminho, msg): self.erros.append('%s: %s' % (caminho, msg))
    def tipo(self, caminho, v, ok, nome):
        if not ok(v):
            self.e(caminho, 'esperado %s, veio %s' % (nome, type(v).__name__ if v is not None else 'null'))
            return False
        return True


def valida_forma(o):
    """Confere campos, tipos e valores fixos da tabela D-T59-02. Retorna a lista de motivos de recusa (vazia = forma ok)."""
    f = Forma()
    if not isinstance(o, dict):
        f.e('$', 'a raiz não é um objeto'); return f.erros
    for k in ('formato', 'versaoFormato', 'exportadoEm', 'pacote', 'estadoVersao', 'escolha', 'resumo', 'caderno', 'respostasCaderno', 'tentativas', 'saidas', 'discursivas'):
        if k not in o: f.e('$.' + k, 'campo ausente')
    if o.get('formato', 'camara2026.erros') != 'camara2026.erros' and 'formato' in o:
        f.e('$.formato', 'valor %r; esperado "camara2026.erros"' % (o['formato'],))
    if 'versaoFormato' in o and not (is_int(o['versaoFormato']) and o['versaoFormato'] == 1):
        f.e('$.versaoFormato', 'versão %r desconhecida; só a versão 1 é aceita' % (o['versaoFormato'],))
    if 'exportadoEm' in o and not is_iso(o['exportadoEm']): f.e('$.exportadoEm', 'não é ISO 8601 UTC com milissegundos: %r' % (o['exportadoEm'],))
    if 'estadoVersao' in o: f.tipo('$.estadoVersao', o['estadoVersao'], is_int, 'inteiro')
    p = o.get('pacote')
    if 'pacote' in o:
        if f.tipo('$.pacote', p, lambda v: isinstance(v, dict), 'objeto'):
            for k, ok, nm in (('nome', is_str, 'string'), ('geradoEm', lambda v: is_str(v) and DATA.match(v), 'string AAAA-MM-DD'), ('versao', is_int, 'inteiro')):
                if k not in p: f.e('$.pacote.' + k, 'campo ausente')
                else: f.tipo('$.pacote.' + k, p[k], ok, nm)
            if 'origem' not in p: f.e('$.pacote.origem', 'campo ausente')
            elif p['origem'] not in ('publicado', 'carregado'): f.e('$.pacote.origem', 'valor %r; esperado "publicado" ou "carregado"' % (p['origem'],))
    esc = o.get('escolha')
    if 'escolha' in o and f.tipo('$.escolha', esc, lambda v: isinstance(v, dict), 'objeto'):
        for k, v in esc.items():
            if k not in ('P1', 'P2'): f.e('$.escolha.' + k, 'chave inesperada (só P1/P2)')
            elif v not in ('diag', 'zero'): f.e('$.escolha.' + k, 'valor %r; esperado "diag" ou "zero"' % (v,))
    r = o.get('resumo')
    if 'resumo' in o and f.tipo('$.resumo', r, lambda v: isinstance(v, dict), 'objeto'):
        for k in ('tentativas', 'itensNoCaderno', 'saidas', 'discursivasEntregues', 'discursivasRascunho'):
            if k not in r: f.e('$.resumo.' + k, 'campo ausente')
            else: f.tipo('$.resumo.' + k, r[k], is_int, 'inteiro')
        if 'eventos' not in r: f.e('$.resumo.eventos', 'campo ausente')
        elif f.tipo('$.resumo.eventos', r['eventos'], lambda v: isinstance(v, dict), 'objeto'):
            for k, v in r['eventos'].items():
                if not is_int(v): f.e('$.resumo.eventos.' + k, 'contagem não inteira')
        if 'eventosTruncados' not in r: f.e('$.resumo.eventosTruncados', 'campo ausente')
        else: f.tipo('$.resumo.eventosTruncados', r['eventosTruncados'], lambda v: isinstance(v, bool), 'booleano')

    def lista(nome, esquema):
        v = o.get(nome)
        if nome not in o: return
        if not f.tipo('$.' + nome, v, lambda x: isinstance(x, list), 'lista'): return
        for i, e in enumerate(v):
            c = '$.%s[%d]' % (nome, i)
            if not f.tipo(c, e, lambda x: isinstance(x, dict), 'objeto'): continue
            esquema(c, e)

    def campos(c, e, spec):
        for k, (ok, nm) in spec.items():
            if k not in e: f.e(c + '.' + k, 'campo ausente')
            else: f.tipo(c + '.' + k, e[k], ok, nm)
    nul = lambda ok: (lambda v: v is None or ok(v))
    bool_ = lambda v: isinstance(v, bool)
    lista('caderno', lambda c, e: campos(c, e, {'id': (is_str, 'string'), 'itemEdital': (nul(is_str), 'string ou null'), 'noPacote': (bool_, 'booleano'),
                                                'errou': (is_int, 'inteiro'), 'seq': (is_int, 'inteiro'), 'desde': (is_iso, 'ISO UTC')}))
    lista('respostasCaderno', lambda c, e: campos(c, e, {'id': (is_str, 'string'), 'ok': (bool_, 'booleano'), 'em': (is_iso, 'ISO UTC')}))

    def tent(c, e):
        campos(c, e, {'tipo': (lambda v: v in ('sim', 'teste', 'rev'), '"sim"|"teste"|"rev"'), 'ref': (is_str, 'string'), 'nome': (is_str, 'string'),
                      'modulo': (lambda v: v in ('P1', 'P2', None), '"P1"|"P2"|null'), 'data': (is_iso, 'ISO UTC'), 'seg': (is_int, 'inteiro'), 'total': (is_int, 'inteiro'),
                      'nota': (is_int, 'inteiro'), 'ac': (is_int, 'inteiro'), 'er': (is_int, 'inteiro'), 'br': (is_int, 'inteiro'),
                      'por': (lambda v: isinstance(v, dict), 'objeto'), 'det': (lambda v: isinstance(v, list), 'lista')})
        if isinstance(e.get('por'), dict):
            for k, v in e['por'].items():
                if not (isinstance(v, dict) and all(x in v and is_int(v[x]) for x in 'ceb')): f.e('%s.por.%s' % (c, k), 'esperado {c, e, b} inteiros')
        if isinstance(e.get('det'), list):
            for j, d in enumerate(e['det']):
                if not (isinstance(d, dict) and is_str(d.get('id')) and d.get('r') in ('C', 'E', None) and 'r' in d and d.get('st') in ('c', 'e', 'b')):
                    f.e('%s.det[%d]' % (c, j), 'esperado {id: string, r: "C"|"E"|null, st: "c"|"e"|"b"}')
    lista('tentativas', tent)
    lista('saidas', lambda c, e: campos(c, e, {'id': (is_str, 'string'), 'em': (is_iso, 'ISO UTC'), 'dias': (is_int, 'inteiro')}))

    def disc(c, e):
        campos(c, e, {'id': (is_str, 'string'), 'tipo': (lambda v: v in ('questao', 'peca', None), '"questao"|"peca"|null'), 'entregue': (lambda v: v is True, 'true'),
                      'entregueEm': (nul(is_iso), 'ISO UTC ou null'), 'texto': (is_str, 'string'), 'tl': (nul(is_num), 'número ou null'), 'notas': (lambda v: isinstance(v, dict), 'objeto'),
                      'ne': (is_num, 'número'), 'nota': (nul(is_num), 'número ou null')})
        if isinstance(e.get('notas'), dict):
            for k, v in e['notas'].items():
                if not (is_num(v) and v in (0, 0.25, 0.5, 0.75, 1)): f.e('%s.notas.%s' % (c, k), 'valor %r; esperado 0, 0.25, 0.5, 0.75 ou 1' % (v,))
    lista('discursivas', disc)
    return f.erros


def coerencia(o):
    """D-T59-05 + regra v1.1 (2.5, discursiva). Retorna (incoerencias, indices_tentativas_fora, indices_caderno_fora, indices_discursivas_fora); cada incoerência é (campo, motivo)."""
    inc = []; t_fora = set(); c_fora = set(); d_fora = set()
    for i, t in enumerate(o['tentativas']):
        mot = []
        if not (t['ac'] + t['er'] + t['br'] == t['total'] == len(t['det'])):
            mot.append('ac+er+br=%d, total=%d, det=%d (devem ser iguais)' % (t['ac'] + t['er'] + t['br'], t['total'], len(t['det'])))
        if t['nota'] != t['ac'] - t['er']: mot.append('nota=%d, ac-er=%d' % (t['nota'], t['ac'] - t['er']))
        if any((d['st'] == 'b') != (d['r'] is None) for d in t['det']): mot.append('st="b" não coincide com r=null em algum det')
        som = {x: sum(v[x] for v in t['por'].values()) for x in 'ceb'}
        if (som['c'], som['e'], som['b']) != (t['ac'], t['er'], t['br']): mot.append('soma de por (c=%d,e=%d,b=%d) != (ac=%d,er=%d,br=%d)' % (som['c'], som['e'], som['b'], t['ac'], t['er'], t['br']))
        cont = collections.Counter(d['st'] for d in t['det'])
        if (cont['c'], cont['e'], cont['b']) != (t['ac'], t['er'], t['br']): mot.append('contagem de st em det (c=%d,e=%d,b=%d) != (ac,er,br)' % (cont['c'], cont['e'], cont['b']))
        if mot:
            t_fora.add(i)
            for m in mot: inc.append(('tentativas[%d] (%s|%s|%s)' % (i, t['tipo'], t['ref'], t['data']), m))
    for i, c in enumerate(o['caderno']):
        if c['errou'] < 1: inc.append(('caderno[%d] (%s)' % (i, c['id']), 'errou=%d (deve ser >= 1)' % c['errou'])); c_fora.add(i)
        if c['seq'] not in (0, 1): inc.append(('caderno[%d] (%s)' % (i, c['id']), 'seq=%d (deve ser 0 ou 1)' % c['seq'])); c_fora.add(i)
    for i, d in enumerate(o['discursivas']):
        mot = []
        if not (is_int(d['ne']) and d['ne'] >= 0): mot.append('ne=%s (deve ser inteiro >= 0)' % json.dumps(d['ne']))
        if not (is_int(d['tl']) and d['tl'] >= 1): mot.append('tl=%s (deve ser inteiro >= 1)' % json.dumps(d['tl']))
        if mot:
            d_fora.add(i)
            for m in mot: inc.append(('discursivas[%d] (%s)' % (i, d['id']), m))
    r = o['resumo']
    if r['itensNoCaderno'] != len(o['caderno']): inc.append(('resumo.itensNoCaderno', '%d != len(caderno)=%d' % (r['itensNoCaderno'], len(o['caderno']))))
    if r['discursivasEntregues'] != len(o['discursivas']): inc.append(('resumo.discursivasEntregues', '%d != len(discursivas)=%d' % (r['discursivasEntregues'], len(o['discursivas']))))
    return inc, sorted(t_fora), sorted(c_fora), sorted(d_fora)


def ordem(o):
    """R-1 (regra v1.1, 2.5, 'Ordem'). Confere a ordem das cinco listas da tabela D-T59-02; retorna as linhas de aviso `ordem: ...` (uma por lista fora de ordem).
    Chaves comparadas como texto (ISO de formato fixo, ids) e, no caderno, (-errou, id). Índice k = primeira posição cuja chave é menor que a da anterior."""
    criterios = (('caderno', 'errou decrescente e id crescente (chave (-errou, id) não decrescente)', lambda e: (-e['errou'], e['id'])),
                 ('respostasCaderno', 'em não decrescente', lambda e: e['em']),
                 ('tentativas', 'data não decrescente', lambda e: e['data']),
                 ('saidas', 'em não decrescente', lambda e: e['em']),
                 ('discursivas', 'id não decrescente', lambda e: e['id']))
    av = []
    for nome, crit, chave in criterios:
        ks = [chave(e) for e in o[nome]]
        k = next((j for j in range(1, len(ks)) if ks[j] < ks[j - 1]), None)
        if k is not None: av.append('ordem: %s fora da ordem %s (primeira posição divergente: índice %d)' % (nome, crit, k))
    return av


def valida(raw, pacote, importados=None):
    """raw: bytes do arquivo; pacote: dict do pacote vigente. Retorna o relatório (dict) sem tocar em disco."""
    R = collections.OrderedDict()
    R['sha256'] = hashlib.sha256(raw).hexdigest(); R['bytes'] = len(raw)
    R['veredito'] = None; R['motivos_recusa'] = []; R['incoerencias'] = []; R['fora_dos_calculos'] = {'tentativas': [], 'caderno': [], 'discursivas': []}
    R['ids_desconhecidos'] = {}; R['divergencias_itemEdital'] = []; R['pacote_origem'] = {}; R['avisos'] = []; R['contagens'] = {}
    def constante(c): raise ValueError('constante não JSON: %s' % c)
    corpo = raw
    if raw.startswith(b'\xef\xbb\xbf'):
        corpo = raw[3:]; R['avisos'].append('arquivo com BOM UTF-8 (tolerado; SHA-256 calculado sobre os bytes recebidos)')
    try:
        txt = corpo.decode('utf-8')
        o = json.loads(txt, parse_constant=constante)
    except (UnicodeDecodeError, ValueError) as ex:
        R['veredito'] = 'RECUSADO'; R['motivos_recusa'] = ['não abre como JSON UTF-8: %s' % ex]; return R
    mot = valida_forma(o)
    if mot:
        R['veredito'] = 'RECUSADO'; R['motivos_recusa'] = mot; return R
    for reg in (importados or []):
        if reg.get('sha256') == R['sha256'] or reg.get('exportadoEm') == o['exportadoEm']:
            R['veredito'] = 'DUPLICADO'
            R['motivos_recusa'] = ['mesmo %s de uma importação já feita' % ('SHA-256' if reg.get('sha256') == R['sha256'] else 'exportadoEm')]
            return R
    R['veredito'] = 'ACEITO'
    R['exportadoEm'] = o['exportadoEm']
    # pacote de origem x vigente (item 3: divergência não é recusa)
    po = o['pacote']
    R['pacote_origem'] = {'arquivo': {'nome': po['nome'], 'geradoEm': po['geradoEm'], 'versao': po['versao'], 'origem': po['origem']},
                          'vigente': {'nome': pacote['nome'], 'geradoEm': pacote['geradoEm'], 'versao': pacote['versao']},
                          'igual': po['nome'] == pacote['nome'] and po['geradoEm'] == pacote['geradoEm'] and po['versao'] == pacote['versao']}
    if not R['pacote_origem']['igual']: R['avisos'].append('pacote de origem ≠ vigente: "%s" (arquivo) x "%s" (vigente)' % (po['nome'], pacote['nome']))
    if po['origem'] == 'carregado': R['avisos'].append('pacote.origem = "carregado" (pacote carregado no aparelho, não o publicado)')
    # coerência (item 5)
    inc, tf, cf, df = coerencia(o)
    R['incoerencias'] = [list(x) for x in inc]; R['fora_dos_calculos'] = {'tentativas': tf, 'caderno': cf, 'discursivas': df}
    R['avisos'] += ordem(o)
    # ids (item 4)
    itens = {i['id']: i for i in pacote['itens']}; discs = {d['id']: d for d in pacote['discursivas']}
    desc = collections.OrderedDict()
    def conf(campo, iid, base):
        if iid not in base: desc.setdefault(campo, collections.Counter())[iid] += 1
    for c in o['caderno']: conf('caderno', c['id'], itens)
    for r in o['respostasCaderno']: conf('respostasCaderno', r['id'], itens)
    for i, t in enumerate(o['tentativas']):
        for d in t['det']: conf('tentativas[].det', d['id'], itens)
    for s in o['saidas']: conf('saidas', s['id'], itens)
    for d in o['discursivas']: conf('discursivas', d['id'], discs)
    R['ids_desconhecidos'] = {k: {'ocorrencias': sum(v.values()), 'ids': dict(sorted(v.items()))} for k, v in desc.items()}
    for c in o['caderno']:
        if c['id'] in itens:
            vig = itens[c['id']]['itemEdital']
            if c['itemEdital'] != vig: R['divergencias_itemEdital'].append({'id': c['id'], 'arquivo': c['itemEdital'], 'vigente': vig})
            if not c['noPacote']: R['avisos'].append('caderno %s: noPacote=false, mas o id existe no pacote vigente' % c['id'])
        else:
            if c['noPacote']: R['avisos'].append('caderno %s: noPacote=true, mas o id não existe no pacote vigente' % c['id'])
    # ref das tentativas (item 4, último parágrafo)
    pids = {s['id'] for s in pacote['simulados']} | {l['id'] for l in pacote['lotes']}
    refs = collections.Counter(t['ref'] for t in o['tentativas'])
    desconhecidos_ref = sorted(r for r in refs if r not in pids and r not in ('DIAG-P1', 'DIAG-P2', 'ERROS') and not re.match(r'^SIM-0-P2$', r))
    if desconhecidos_ref: R['avisos'].append('ref de tentativa fora dos ids do pacote vigente (simulados e lotes) e de DIAG-P1/DIAG-P2/ERROS: %s' % ', '.join(desconhecidos_ref))
    if o['resumo']['eventosTruncados']: R['avisos'].append('eventosTruncados = true: respostasCaderno pode estar incompleta')
    R['contagens'] = {'tentativas': len(o['tentativas']), 'tentativas_validas': len(o['tentativas']) - len(tf), 'caderno': len(o['caderno']), 'respostasCaderno': len(o['respostasCaderno']),
                      'saidas': len(o['saidas']), 'discursivas': len(o['discursivas']), 'refs': dict(sorted(refs.items()))}
    return R


def texto(R):
    L = ['VEREDITO: %s' % R['veredito'], 'SHA-256: %s (%d bytes)' % (R['sha256'], R['bytes'])]
    if R['veredito'] != 'ACEITO':
        L.append('IMPORTAÇÃO %s — %d motivo(s)' % (R['veredito'] if R['veredito'] == 'DUPLICADO' else 'RECUSADA', len(R['motivos_recusa'])))
        L += ['  - ' + m for m in R['motivos_recusa'][:30]]
        if len(R['motivos_recusa']) > 30: L.append('  - … (+%d)' % (len(R['motivos_recusa']) - 30))
        return '\n'.join(L)
    po = R['pacote_origem']
    L.append('exportadoEm: %s' % R['exportadoEm'])
    L.append('pacote de origem: "%s" (%s, versao %s, %s) | vigente: "%s" (%s) | %s' % (po['arquivo']['nome'], po['arquivo']['geradoEm'], po['arquivo']['versao'], po['arquivo']['origem'],
             po['vigente']['nome'], po['vigente']['geradoEm'], 'IGUAL' if po['igual'] else 'DIVERGENTE'))
    c = R['contagens']
    L.append('contagens: tentativas %d (válidas %d), caderno %d, respostasCaderno %d, saidas %d, discursivas %d' % (c['tentativas'], c['tentativas_validas'], c['caderno'], c['respostasCaderno'], c['saidas'], c['discursivas']))
    L.append('IDS DESCONHECIDOS: %s' % ('nenhum' if not R['ids_desconhecidos'] else '%d campo(s)' % len(R['ids_desconhecidos'])))
    for k, v in R['ids_desconhecidos'].items(): L.append('  - %s: %d ocorrência(s); ids: %s' % (k, v['ocorrencias'], ', '.join('%s (%d)' % x for x in v['ids'].items())))
    L.append('INCOERÊNCIAS (D-T59-05): %s' % ('nenhuma' if not R['incoerencias'] else '%d (fora dos cálculos: tentativas %s, caderno %s, discursivas %s)' % (len(R['incoerencias']), R['fora_dos_calculos']['tentativas'], R['fora_dos_calculos']['caderno'], R['fora_dos_calculos']['discursivas'])))
    L += ['  - %s: %s' % tuple(x) for x in R['incoerencias']]
    L.append('DIVERGÊNCIAS DE itemEdital: %s' % ('nenhuma' if not R['divergencias_itemEdital'] else len(R['divergencias_itemEdital'])))
    L += ['  - %s: arquivo %r, vigente %r' % (d['id'], d['arquivo'], d['vigente']) for d in R['divergencias_itemEdital']]
    L.append('AVISOS: %s' % ('nenhum' if not R['avisos'] else len(R['avisos'])))
    L += ['  - ' + a for a in R['avisos']]
    return '\n'.join(L)


def main(argv):
    arq = None; pac = PACOTE_PADRAO; imp = None; js = False; i = 0
    while i < len(argv):
        a = argv[i]
        if a == '--pacote' and i + 1 < len(argv): pac = argv[i + 1]; i += 2
        elif a == '--importados' and i + 1 < len(argv): imp = argv[i + 1]; i += 2
        elif a == '--json': js = True; i += 1
        elif arq is None and not a.startswith('--'): arq = a; i += 1
        else: sys.stderr.write(__doc__.split('Uso:')[1].split('Veredito:')[0] + '\n'); return 2
    if arq is None: sys.stderr.write('uso: validar_erros.py <arquivo.json> [--pacote P] [--importados R] [--json]\n'); return 2
    try:
        raw = open(arq, 'rb').read()
        pacote = json.load(open(pac, encoding='utf-8'))
        importados = json.load(open(imp, encoding='utf-8')) if imp else None
    except (OSError, ValueError) as ex:
        sys.stderr.write('erro de leitura: %s\n' % ex); return 2
    R = valida(raw, pacote, importados)
    print(json.dumps(R, ensure_ascii=False, indent=1) if js else texto(R))
    return {'ACEITO': 0, 'RECUSADO': 1, 'DUPLICADO': 3}[R['veredito']]


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
