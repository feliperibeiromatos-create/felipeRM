# validar_da.py — conferência de forma dos arquivos D<n>_plataforma.json (FORMATO_PLATAFORMA_DA.md, seção 8)
# Uso: python3 -I validar_da.py <D<n>_plataforma.json> <arquivo canônico .md> <mapa normativo .md>
import json, re, sys, pathlib, unicodedata

def norm(s):
    s = unicodedata.normalize('NFC', s)
    s = s.replace(' ', ' ').replace('“', '"').replace('”', '"').replace('’', "'").replace('‘', "'")
    s = s.replace('**', '')
    return re.sub(r'\s+', ' ', s).strip()

FALHAS, AVISOS = [], []
def F(m): FALHAS.append(m)
def A(m): AVISOS.append(m)

PROIB = [
    (r'\b[Ll]ote\s+(D?\d|[A-Z]\d)', 'código de lote'),
    (r'\bD[1-6]-\d{2}\b', 'id de item'),
    (r'\bC\d+(\.\d+)?-\d{2}\b', 'código de bloco do curso'),
    (r'\b[GP]-\d{2}\b', 'código de pegadinha/par'),
    (r'\bPARTE \d', 'PARTE n'),
    (r'(^|\n)\s*(#+\s*)?[LG]\d{1,2}\.\s', 'código de bloco L/G'),
    (r'\[F\d+', 'fonte [Fn]'),
    (r'\bF\d{1,2}\b', 'fonte Fn'),
    (r'\[V\s', 'marca [V …]'),
    (r'NORMATIVO\s*[—-]\s*QA', 'marca NORMATIVO — QA'),
    (r'QA PENDENTE', 'QA PENDENTE'),
    (r'trecho importado', 'trecho importado'),
    (r'REVERIFICAR', 'REVERIFICAR'),
    (r'VOL[ÁA]TIL', 'VOLÁTIL'),
    (r'\[TS\]', '[TS]'),
    (r'elemento-isca', 'elemento-isca'),
    (r'BASE DOUTRIN', 'BASE DOUTRINÁRIA'),
    (r'Anexo N', 'Anexo N'),
    (r'[Mm]apa normativo', 'mapa normativo'),
    (r'\bficha\b', 'ficha'),
    (r'\bR[12]\b', 'R1/R2'),
    (r'\bv[12](\.\d)?\b', 'v1/v2'),
    (r'\bacatad', 'acatado'),
    (r'\b(GCB|GBQ|GCE|EXEC|CQFP|CPP)\b|gcb-|qa-normativo|ChatGPT|Claude|Fundador|Presid[êe]ncia da f', 'unidade/agente/ferramenta'),
    (r'SEM FONTE', 'SEM FONTE'),
    (r'\bBQ-\d{4}\b', 'id de item do banco'),
    (r'\bT-\d{2,3}\b', 'código de tarefa'),
    (r'\bD-[A-Z]{2,}', 'código de decisão'),
]

def varre(campo, txt):
    for rx, nome in PROIB:
        m = re.search(rx, txt)
        if m:
            F(f'{campo}: proibido ({nome}): …{txt[max(0,m.start()-40):m.end()+40]!r}…')

def main():
    pj, canon, mapa = map(pathlib.Path, sys.argv[1:4])
    d = json.loads(pj.read_text(encoding='utf-8'))
    raiz = pathlib.Path(__file__).resolve().parents[4]
    edital = {e['id']: e['texto'] for e in json.loads((raiz/'saida/gcb/DA_plataforma/edital_DA.json').read_text(encoding='utf-8'))}
    ordem_ed = list(edital)
    can = norm(canon.read_text(encoding='utf-8'))
    mapa_raw = mapa.read_text(encoding='utf-8')
    mapa_n = norm(mapa_raw)
    datas_mapa = set(re.findall(r'\b(\d{2})/(\d{2})/(\d{4})\b', mapa_raw))
    datas_iso = {f'{a}-{m}-{dd}' for dd, m, a in datas_mapa}
    if list(d) != ['lote', 'itens', 'topicos']: F(f'chaves de topo {list(d)}')
    L = d['lote']
    if list(L) != ['id','nome','prova','itensEdital','resumo','curso','pares','pegadinhas']: F(f'campos do lote {list(L)}')
    lid = L['id']
    if not re.fullmatch(r'D[1-6]', lid): F('lote.id')
    if L['prova'] != 'P1': F('lote.prova')
    if 'Lote' in L['nome'] or not L['nome'].startswith('Direito Administrativo — '): F(f'lote.nome {L["nome"]!r}')
    ie = L['itensEdital']
    for x in ie:
        if x not in edital: F(f'itensEdital desconhecido {x}')
    if ie != sorted(ie, key=ordem_ed.index): F('itensEdital fora da ordem do edital')
    varre('lote.nome', L['nome']); varre('lote.resumo', L['resumo'])
    # curso
    cur = L['curso']; varre('lote.curso', cur)
    heads = re.findall(r'^## (\d+(?:\.\d+)?) (.+)$', cur, re.M)
    nums = ['P1-DA-' + h[0] for h in heads]
    if len(re.findall(r'^## ', cur, re.M)) != len(heads): F('cabeçalho ## fora do padrão "## <número> <TÍTULO>"')
    for n, (num, tit) in zip(nums, heads):
        if n not in ie: F(f'## {num} não está em itensEdital')
        if tit != tit.upper(): F(f'## {num}: título não está em maiúsculas')
    if nums != sorted(nums, key=ordem_ed.index) or len(set(nums)) != len(nums): F('blocos ## fora de ordem ou repetidos')
    ROT = {'DEFINIÇÃO', 'BASE LEGAL', 'EXEMPLO PARLAMENTAR', 'PEGADINHA PROVÁVEL'}
    cont = {r: 0 for r in ROT}
    for i, l in enumerate(cur.split('\n'), 1):
        s = l.strip()
        if s in ROT: cont[s] += 1; continue
        if s.startswith('#'):
            if s.startswith('### ') and s[4:] == s[4:].upper() and re.search(r'[A-ZÁÉÍÓÚÇ]{4}', s[4:]): F(f'curso linha {i}: ### em maiúsculas')
            continue
        if re.fullmatch(r'[A-ZÁÉÍÓÚÂÊÔÃÕÇ0-9 ,:\-—()/.]{6,}', s) and re.search(r'[A-ZÁÉÍÓÚÇ]{4}', s): F(f'curso linha {i}: linha em maiúsculas vira título: {s!r}')
        if s.count('|') >= 2 and not (s.startswith('|') and s.endswith('|')): F(f'curso linha {i}: barras fora de tabela')
    for r in ('DEFINIÇÃO', 'EXEMPLO PARLAMENTAR', 'PEGADINHA PROVÁVEL'):
        if cont[r] < len(heads): A(f'quadro {r}: {cont[r]} ocorrências para {len(heads)} blocos ##')
    # pares e pegadinhas
    if len(L['pares']) < 8: F(f'pares: {len(L["pares"])} (< 8)')
    for k, p in enumerate(L['pares']):
        if list(p) != ['a','b','como'] or not all(p.values()): F(f'pares[{k}] campos')
        varre(f'pares[{k}]', ' '.join(p.values()))
    for k, p in enumerate(L['pegadinhas']):
        if list(p) != ['itemEdital','rotulo','texto']: F(f'pegadinhas[{k}] campos')
        if p.get('itemEdital') not in ie: F(f'pegadinhas[{k}] itemEdital {p.get("itemEdital")}')
        elif p['rotulo'] != edital[p['itemEdital']]: F(f'pegadinhas[{k}] rotulo ≠ texto do edital')
        varre(f'pegadinhas[{k}]', p.get('texto',''))
    # itens
    CAMPOS = ['id','rotulo','certame','cargo','ano','numero','comando','textoBase','enunciado','gabarito','justificativa','itemEdital','aderencia','url']
    ids = set(); cs = es = 0
    for it in d['itens']:
        c = list(it)
        if c != CAMPOS and c != CAMPOS + ['volatil']: F(f'item {it.get("id")}: campos {c}')
        if 'volatil' in it and it['volatil'] is not True: F(f'item {it["id"]}: volatil diferente de true')
        if not re.fullmatch(lid + r'-\d{2}', it['id']): F(f'item id {it["id"]}')
        if it['id'] in ids: F(f'id repetido {it["id"]}')
        ids.add(it['id'])
        if it['numero'] != int(it['id'].split('-')[1]): F(f'{it["id"]}: numero')
        if it['rotulo'] != 'AUTORAL' or it['aderencia'] != 'direta' or it['ano'] != 2026: F(f'{it["id"]}: rotulo/aderencia/ano')
        if it['gabarito'] not in ('C','E'): F(f'{it["id"]}: gabarito')
        cs += it['gabarito'] == 'C'; es += it['gabarito'] == 'E'
        if it['itemEdital'] not in ie: F(f'{it["id"]}: itemEdital {it["itemEdital"]} fora do lote')
        if norm(it['enunciado']) not in can: F(f'{it["id"]}: enunciado não encontrado literal no canônico')
        if it['textoBase'] and norm(it['textoBase']) not in can: F(f'{it["id"]}: textoBase não encontrado literal no canônico')
        if not it['justificativa'].strip(): F(f'{it["id"]}: justificativa vazia')
        for campo in ('enunciado','justificativa','textoBase','comando'):
            varre(f'{it["id"]}.{campo}', it[campo])
    # tópicos
    T = d['topicos']
    if list(T) != [n for n in nums]: F(f'topicos: chaves {list(T)} ≠ blocos ## {nums}')
    TIPOS = {'compare': ['tipo','titulo','a','b','linhas','legenda'], 'baseLegal': ['tipo','titulo','norma','dispositivos'],
             'esquema': ['tipo','titulo','centro','ramos'], 'linha': ['tipo','titulo','marcos'], 'fluxo': ['tipo','titulo','passos'],
             'tabela': ['tipo','titulo','colunas','linhas','legenda']}
    for k, t in T.items():
        if list(t) != ['emUmMinuto','resumo','visuais']: F(f'{k}: campos {list(t)}')
        e1 = t.get('emUmMinuto', [])
        if len(e1) != 3 or not all(isinstance(x, str) and x.strip() for x in e1): F(f'{k}: emUmMinuto precisa de 3 frases')
        r = t.get('resumo', '')
        n = len(r.split())
        if not 150 <= n <= 250: F(f'{k}: resumo com {n} palavras')
        for par in r.split('\n\n'):
            if re.match(r'\s*(\d|[-*•]|[A-ZÁÉÍÓÚÇ ]{3,}:)', par): F(f'{k}: parágrafo do resumo começa com algarismo, lista ou RÓTULO:')
        varre(f'{k}.resumo', r); varre(f'{k}.emUmMinuto', ' '.join(e1))
        vs = t.get('visuais', [])
        if not 1 <= len(vs) <= 2: F(f'{k}: {len(vs)} visuais')
        for j, v in enumerate(vs):
            tp = v.get('tipo')
            if tp not in TIPOS: F(f'{k}.visuais[{j}]: tipo {tp}'); continue
            ok = TIPOS[tp]
            if tp == 'tabela' and list(v) == ok[:-1]: pass
            elif list(v) != ok: F(f'{k}.visuais[{j}] ({tp}): campos {list(v)}')
            varre(f'{k}.visuais[{j}]', json.dumps(v, ensure_ascii=False))
            if tp == 'compare':
                if not 1 <= len(v['linhas']) <= 6 or any(len(x) != 3 for x in v['linhas']): F(f'{k}.compare: linhas')
            if tp == 'tabela':
                if len(v['colunas']) < 2 or any(len(x) != len(v['colunas']) for x in v['linhas']): F(f'{k}.tabela: colunas/linhas')
            if tp == 'fluxo':
                if not 3 <= len(v['passos']) <= 7 or any(len(x) > 48 for x in v['passos']): F(f'{k}.fluxo: passos')
            if tp == 'esquema' and not 2 <= len(v['ramos']) <= 8: F(f'{k}.esquema: ramos')
            if tp == 'linha' and (len(v['marcos']) < 2 or any(list(m) != ['quando','texto'] for m in v['marcos'])): F(f'{k}.linha: marcos')
            if tp == 'baseLegal':
                ds = v['dispositivos']
                if not 1 <= len(ds) <= 4: F(f'{k}.baseLegal: {len(ds)} dispositivos')
                for q in ds:
                    if list(q) != ['ref','texto','literal','conferido']: F(f'{k}.baseLegal: campos {list(q)}'); continue
                    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', q['conferido']): F(f'{k}.baseLegal {q["ref"]}: conferido sem data AAAA-MM-DD')
                    elif q['conferido'] not in datas_iso: F(f'{k}.baseLegal {q["ref"]}: data {q["conferido"]} não aparece no mapa')
                    if q['literal'] is True and norm(q['texto']).rstrip('.;:') not in mapa_n: F(f'{k}.baseLegal {q["ref"]}: literal=true mas texto não está letra a letra no mapa')
                    if q['literal'] not in (True, False): F(f'{k}.baseLegal {q["ref"]}: literal')
    print(f'{pj.name}: lote {lid}; itensEdital {len(ie)}; blocos ## {len(heads)}; itens {len(d["itens"])} (C {cs} / E {es}); pares {len(L["pares"])}; pegadinhas {len(L["pegadinhas"])}; topicos {len(T)}')
    print(f'quadros: {cont}')
    for m in AVISOS: print('AVISO', m)
    for m in FALHAS: print('FALHA', m)
    print(f'RESULTADO: {len(FALHAS)} FALHA, {len(AVISOS)} AVISO')
    sys.exit(1 if FALHAS else 0)

main()
