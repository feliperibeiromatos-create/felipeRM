# -*- coding: utf-8 -*-
"""T-108 (v1.11; cópia de saida/pacote/T108_inventario.py com caminhos por argumento, posições dos casamentos e extensão aos .md; as regras e as classes são as mesmas) — inventário das marcas de produção no texto que a candidata lê.
GBQ, 2026-10-18 (ciclo s14c1). Somente leitura dos pacotes; grava o CSV de ocorrências e um JSON de contagens.
Uso: python -I T108_inventario.py <dir saida/pacote> [<contagens.json>]
Campos do escopo da ordem (curso, resumo, pegadinhas, justificativas): lotes[].curso, lotes[].resumo,
lotes[].pegadinhas[].rotulo/.texto, itens[].justificativa. Campos extras (lidos pela candidata, fora da letra da ordem,
contados à parte): lotes[].pares[].a/.b/.como, itens[].nota, simulados[].avisos[], discursivas (comando, padrao, aspectos, quesitos).
Classe de cada ocorrência: PROCESSO (marca a limpar), FP-R1 (falso positivo da regra 1: lote/batch técnico, tecla F4),
FP-CONTEUDO (homônimo de conteúdo), VERIFICAR (decisão da Gerência titular).
id de ocorrência: <arq>-<cat>-<sha1(campo|cat|casamento|k)[:8]>, k = ordem do mesmo casamento no mesmo campo (estável
enquanto o campo não mudar)."""
import collections, csv, hashlib, json, os, re, sys

ARQS = [('D', 'pacote.json'), ('E', 'pacote_estudante.json')]
SEP_COMPL = '\n\n## Complemento\n\n'
LOTE_NOME = {'L1': '1', 'L1C': '1-C', 'L2': '2', 'L3': '3', 'L4': '4', 'L4C': '4-C', 'L5': '5', 'L5C': '5-C', 'L6A': '6a', 'L6B': '6b'}
PREF = {'L1': 'L1', 'L1C': 'L1C', 'L2': 'L2', 'L3': 'L3', 'L4': 'L4', '4C': 'L4C', 'A5': 'L5', '5C': 'L5C', '6A': 'L6A', '6B': 'L6B', 'L6A': 'L6A', 'L6B': 'L6B', 'BQ': 'BANCO'}
GER = {'L1': 'GCE', 'L1C': 'GCE', 'L2': 'GCE', 'L3': 'GCE', 'L4': 'GCB', 'L4C': 'GCB', 'L5': 'GCB', 'L5C': 'GCB', 'L6A': 'GCB', 'L6B': 'GCB', 'BANCO': 'GBQ', 'SIMULADO': 'GBQ', 'DISCURSIVA': 'GCE'}
CATS = collections.OrderedDict([
    ('C01', '"Lote N", "neste lote", "do lote" (lote de produção)'),
    ('C02', 'código de item (6A-02, L2-Q06, A5-10, L1-R103, BQ-0040…)'),
    ('C03', 'código de par ou de pegadinha (par C14, (C19), P5)'),
    ('C04', 'etiqueta entre colchetes ([V data — Fx], [NORMATIVO — QA…], [F12])'),
    ('C05', 'código de fonte no texto (F1…F22, N1…N9, U/GG/TB do L5)'),
    ('C06', 'prefixo de mecanismo TC/IC/GI/AT (e rótulo "sem armadilha (ancoragem)")'),
    ('C07', 'menção a QA, unidade ou agente (QA, CQFP, "conferida por script"…)'),
    ('C08', 'menção a produção, errata, fábrica ou id de decisão (D-…, T-…)'),
    ('C09', 'versão de produção (v2, v1.9, "versão 2 do lote")'),
    ('C10', 'instrução interna ("Só o fato e a fonte", "SEM ITEM", "NÃO GABARITO", "não cobrar…", REVERIFICAR, PENDENTE…)'),
])
FN = r'F\d{1,2}'
# (cat, subtipo, regex)
REGRAS = [
    ('C04', '[V …]', re.compile(r'\[V\s[^\]]*\]')),
    ('C04', '[NORMATIVO …]', re.compile(r'\[NORMATIVO[^\]]*\]')),
    ('C04', '[Fn …]', re.compile(r'\[' + FN + r'(?:[^\]\w][^\]]*)?\]')),
    ('C04', '[Nn …]', re.compile(r'\[N\d(?:[^\]\w][^\]]*)?\]')),
    ('C10', '[não cobrar …]', re.compile(r'\[não cobrar[^\]]*\]')),
    ('C01', 'lote', re.compile(r'(?i)(?<![\w])lotes?(?![\w])')),
    ('C02', 'código de item', re.compile(r'(?<![\w-])(?:L\dC?-[QR]?\d{2,3}|L6[AB]-R\d{2}|(?:4C|5C|A5|6A|6B)-\d{2}|BQ-\d{4})(?![\w])')),
    ('C02', 'espelho da troca (referência a item-par)', re.compile(r'(?i)espelho da troca')),
    ('C02', 'Qnn (número de item do lote)', re.compile(r'(?<![\w-])Q\d{2}(?![\w])')),
    ('C03', 'par Cn', re.compile(r'(?<![\w])par(?:es)? C\d{1,2}(?:(?:, | e )C\d{1,2})*(?![\w])')),
    ('C03', '(Cn)', re.compile(r'\(C\d{1,2}\)')),
    ('C03', 'Pn', re.compile(r'(?<![\w/])P\d{1,2}(?![\w-])')),
    ('C05', 'Fn', re.compile(r'(?<![\w\[])' + FN + r'(?![\w])')),
    ('C05', 'Nn', re.compile(r'(?<![\w\[])N\d{1,2}(?![\w])')),
    ('C05', 'U/GG/TB', re.compile(r'(?<![\w])(?:U\d|GG\d|TB\d)(?![\w])')),
    ('C06', 'TC/IC/GI/AT', re.compile(r'(?<![\w])(?:TC|IC|GI|AT)(?= invertida|[ .(:;,)]|$)')),
    ('C06', 'sem armadilha (ancoragem)', re.compile(r'(?i)sem armadilha \(ancoragem\)')),
    ('C07', 'conferido por script/pela QA', re.compile(r'(?i)(?:conferid|verificad|confirmad|reconfirmad)[oa]s? (?:por script|pel[ao] (?:CQFP|QA|CQE|produção))')),
    ('C07', 'agente', re.compile(r'(?i)(?<![\w])(?:gbq-[a-z]+|gce-[a-z]+|gcb-[a-z]+|qa-normativo(?:-da)?|corretor-[ab])(?![\w])')),
    ('C07', 'unidade/QA', re.compile(r'(?<![\w])(?:QA|CQFP|CQE|CPP|GCE|GCB|GBQ|CSC)(?![\w])')),
    ('C08', 'errata', re.compile(r'(?i)(?<![\w])erratas?(?![\w])')),
    ('C08', 'produção', re.compile(r'(?i)(?<![\w])(?:produção|produtor[a]?|fábrica)(?![\w])')),
    ('C08', 'id de decisão/tarefa', re.compile(r'(?<![\w])(?:D-[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*|T-\d{1,3})(?![\w])')),
    ('C08', 'rótulo ou arquivo interno', re.compile(r'CEBRASPE_ANALOGA|GAB_DEFINITIVO_\w+|(?<![\w])AUTORAL(?![\w])')),
    ('C09', 'vN', re.compile(r'(?<![\w.])v\d+(?:\.\d+)*(?![\w])')),
    ('C09', 'versão N do lote', re.compile(r'(?i)versão \d+ d[oa] (?:lote|curso|item)')),
    ('C10', 'Só o fato e a fonte', re.compile(r'Só o fato e a fonte\.?')),
    ('C10', 'SEM ITEM / sem item', re.compile(r'(?i)(?<![\w])(?:sem item|não vira item|não entra em item|não há item|nenhum item)(?![\w])')),
    ('C10', 'NÃO GABARITO / CONTROVERSO', re.compile(r'NÃO GABARITO|CONTROVERSO')),
    ('C10', 'não cobrar', re.compile(r'(?i)(?<![\w])não (?:são |é )?cobr(?:ar|a|am|ado|ados|ada|adas)(?![\w])')),
    ('C10', 'PENDENTE / não afirmar', re.compile(r'(?<![\w])PENDENTE(?![\w])|\(não afirmar\)|(?i:nunca dizer)')),
    ('C10', 'REVERIFICAR', re.compile(r'(?i)(?<![\w])reverificar(?![\w])')),
    ('C10', 'VOLÁTIL (classificação em caixa alta)', re.compile(r'VOLÁTIL|VOLÁTEIS')),
    ('C10', 'CONTEXTO NORMATIVO INTERNO', re.compile(r'CONTEXTO NORMATIVO INTERNO')),
]
# falsos positivos e conteúdo: (cat, regex sobre a janela de contexto [-60,+60], classe, motivo)
FP = [
    ('C05', re.compile(r'tecla F4'), 'FP-R1', 'regra 1: tecla F4 do Excel'),
    ('C08', re.compile(r'(?i)em produção|da produção, amostrad|na produção\. A saída|reprodução'), 'FP-CONTEUDO', 'produção no sentido técnico do conteúdo'),
    ('C08', re.compile(r'seção "Errata"'), 'FP-CONTEUDO', 'seção de documento oficial'),
    ('C10', re.compile(r'(?i)é cobrad[oa] (?:pela|pelo)|cobra (?:o|a) taxa'), 'FP-CONTEUDO', 'cobrar no sentido do conteúdo'),
]
VERIFICAR = [
    ('C06', 'sem armadilha (ancoragem)'), ('C02', 'espelho da troca (referência a item-par)'), ('C10', 'VOLÁTIL (classificação em caixa alta)'),
]

def campos(P, arq):
    """(lote, campo, caminho, texto, escopo) — escopo 'ordem' (curso/resumo/pegadinhas/justificativa) ou 'extra'."""
    for L in P['lotes']:
        lid = L['id']
        partes = [(lid, L['curso'])]
        if arq == 'E' and lid == 'L1' and SEP_COMPL in L['curso']:
            a, b = L['curso'].split(SEP_COMPL, 1)
            partes = [('L1', a), ('L1C', b)]
        yield (lid, 'resumo', 'lotes[%s].resumo' % lid, L['resumo'], 'ordem')
        for k, (lo, t) in enumerate(partes):
            yield (lo, 'curso', 'lotes[%s].curso%s' % (lid, '' if k == 0 else '(Complemento)'), t, 'ordem')
        n_l1 = None
        for k, g in enumerate(L['pegadinhas']):
            lo = lid
            if arq == 'E' and lid == 'L1' and k >= 19:
                lo = 'L1C'
            yield (lo, 'pegadinhas', 'lotes[%s].pegadinhas[%d].rotulo' % (lid, k), g['rotulo'], 'ordem')
            yield (lo, 'pegadinhas', 'lotes[%s].pegadinhas[%d].texto' % (lid, k), g['texto'], 'ordem')
        for k, p in enumerate(L['pares']):
            for f in ('a', 'b', 'como'):
                yield (lid, 'pares', 'lotes[%s].pares[%d].%s' % (lid, k, f), p.get(f) or '', 'extra')
    for it in P['itens']:
        lo = PREF[it['id'].split('-')[0]]
        yield (lo, 'justificativa', 'itens[%s].justificativa' % it['id'], it['justificativa'], 'ordem')
        if it.get('nota'):
            yield (lo, 'nota', 'itens[%s].nota' % it['id'], it['nota'], 'extra')
    for s in P['simulados']:
        for k, a in enumerate(s.get('avisos') or []):
            yield ('SIMULADO', 'avisos', 'simulados[%s].avisos[%d]' % (s['id'], k), a, 'extra')
    for d in P['discursivas']:
        b = 'discursivas[%s]' % d['id']
        yield ('DISCURSIVA', 'discursivas', b + '.comando', d['comando'], 'extra')
        yield ('DISCURSIVA', 'discursivas', b + '.padrao', d['padrao'], 'extra')
        for a in d['aspectos']:
            yield ('DISCURSIVA', 'discursivas', '%s.aspectos[%s].texto' % (b, a['n']), a['texto'], 'extra')
        for q in d['quesitos']:
            yield ('DISCURSIVA', 'discursivas', '%s.quesitos[%s].nome' % (b, q['id']), q['nome'], 'extra')
            for k, c in enumerate(q['conceitos']):
                yield ('DISCURSIVA', 'discursivas', '%s.quesitos[%s].conceitos[%d]' % (b, q['id'], k), c, 'extra')

LOTE_PROC = re.compile(r'(?<![\w])(?:Lotes? (?:\d|6[ab])|(?:neste|deste|este|desse|nesse|esse) lote|(?:o|do) lote (?:NÃO|são|usa))')
LOTE_TEC = re.compile(r'(?i)em lote|entre lote e|só no lote|no lote \(Batch|batch|tempo real (?:e|×) lote|→ lote|do lote com a revisão|lote e limites|(?:^|\s)lote (?:opera|,)|lote, submete|à do lote|lote sem erro')

def classe_lote(t, a, b, lote, cam):
    for m in LOTE_PROC.finditer(t[max(0, a - 12):b + 8]):
        return 'PROCESSO', 'lote de produção'
    if LOTE_TEC.search(t[max(0, a - 25):b + 25]):
        return 'FP-R1', 'regra 1: lote/batch técnico (ou lote de transcrições no controle de qualidade)'
    return 'VERIFICAR', 'decisão da Gerência titular'

DIFERE = re.compile(r'Difere d[oa]s? [^.]*?(?:porque|:)[^.]*\.')

def varre(P, arq):
    out = []
    for lote, campo, cam, t, esc in campos(P, arq):
        if not t:
            continue
        ocup = []          # spans das etiquetas C04/C10-colchete, para não contar de novo o Fn/Nn interno
        dif = [(m.start(), m.end()) for m in DIFERE.finditer(t)]
        vistos = collections.Counter()
        tomado = []
        for cat, sub, rx in REGRAS:
            for m in rx.finditer(t):
                a, b = m.start(), m.end()
                if cat != 'C04' and sub != '[não cobrar …]' and any(x <= a and b <= y for x, y in ocup):
                    continue          # dentro de etiqueta já contada (C04 ou [não cobrar …])
                if any(c_ == cat and a < y and x < b for c_, x, y in tomado):
                    continue          # sobreposto a casamento já contado na mesma categoria
                tomado.append((cat, a, b))
                if cat == 'C04' or sub == '[não cobrar …]':
                    ocup.append((a, b))
                ctx = t[max(0, a - 60):b + 60]
                classe, motivo = 'PROCESSO', ''
                for c2, frx, cl, mot in FP:
                    if c2 == cat and frx.search(t[max(0, a - 25):b + 25]):
                        classe, motivo = cl, mot
                        break
                if cat == 'C01':
                    classe, motivo = classe_lote(t, a, b, lote, cam)
                elif sub == 'Pn':
                    ini = t.rfind('\n', 0, a) + 1
                    if t[ini:a].strip() == '' and t[b:b + 1] == '.':
                        classe, motivo = 'FP-CONTEUDO', 'numeração visível da lista de pegadinhas do curso'
                    elif campo == 'avisos':
                        classe, motivo = 'FP-CONTEUDO', 'módulo P1/P2 do edital'
                elif sub == 'VOLÁTIL (classificação em caixa alta)' and campo == 'justificativa':
                    classe, motivo = 'PROCESSO', 'classificação interna na justificativa'
                elif sub == 'SEM ITEM / sem item' and m.group(0).lower() == 'nenhum item':
                    classe, motivo = 'VERIFICAR', 'decisão da Gerência titular'
                if classe == 'PROCESSO' and (cat, sub) in VERIFICAR and not motivo:
                    classe, motivo = 'VERIFICAR', 'decisão da Gerência titular'
                g = m.group(0)
                k = vistos[(cat, g)]; vistos[(cat, g)] += 1
                oid = '%s-%s-%s' % (arq, cat, hashlib.sha1(('%s|%s|%s|%d' % (cam, cat, g, k)).encode('utf-8')).hexdigest()[:8])
                r3 = any(x <= a < y for x, y in dif)
                out.append(dict(_a=a, _b=b, id_ocorrencia=oid, arquivo=ARQS[0][1] if arq == 'D' else ARQS[1][1], lote=LOTE_NOME.get(lote, lote),
                                gerencia=GER.get(lote, 'GBQ'), campo=campo, caminho=cam, escopo=esc, categoria=cat, subtipo=sub,
                                classe=classe, motivo=motivo, regra3_difere='sim' if r3 else '', casamento=g,
                                trecho=ctx.replace('\n', ' ⏎ ').replace('\r', '')))
    return out

def varre_md(nome, texto, ids_item):
    """Varre um arquivo .md da edição do estudante com as mesmas REGRAS/FP/classe_lote. Antes, apaga (por espaços) os identificadores de item (o id exato de cada item do pacote:
    rótulo estrutural da edição, não texto de conteúdo). Cabeçalhos, metadados e enunciados do .md ficam no escopo e são contados. Devolve a lista de ocorrências (campo = nome do arquivo)."""
    t = texto
    if ids_item:
        rx_ids = re.compile(r'(?<![\w-])(?:' + '|'.join(re.escape(i) for i in sorted(ids_item, key=len, reverse=True)) + r')(?![\w])')
        t = rx_ids.sub(lambda m: ' ' * len(m.group(0)), t)
    P = {'lotes': [], 'itens': [], 'simulados': [], 'discursivas': []}
    out = []
    lote = nome.split('_')[0].split('.')[0]
    vistos = collections.Counter(); tomado = []; ocup = []
    for cat, sub, rx in REGRAS:
        for m in rx.finditer(t):
            a, b = m.start(), m.end()
            if cat != 'C04' and sub != '[não cobrar …]' and any(x <= a and b <= y for x, y in ocup):
                continue
            if any(c_ == cat and a < y and x < b for c_, x, y in tomado):
                continue
            tomado.append((cat, a, b))
            if cat == 'C04' or sub == '[não cobrar …]':
                ocup.append((a, b))
            classe, motivo = 'PROCESSO', ''
            for c2, frx, cl, mot in FP:
                if c2 == cat and frx.search(t[max(0, a - 25):b + 25]):
                    classe, motivo = cl, mot
                    break
            if cat == 'C01':
                classe, motivo = classe_lote(t, a, b, lote, nome)
            elif sub == 'Pn':
                ini = t.rfind('\n', 0, a) + 1
                if t[ini:a].strip() == '' and t[b:b + 1] == '.':
                    classe, motivo = 'FP-CONTEUDO', 'numeração visível da lista de pegadinhas do curso'
            if classe == 'PROCESSO' and (cat, sub) in VERIFICAR and not motivo:
                classe, motivo = 'VERIFICAR', 'decisão da Gerência titular'
            g = m.group(0)
            k = vistos[(cat, g)]; vistos[(cat, g)] += 1
            oid = 'M-%s-%s' % (cat, hashlib.sha1(('%s|%s|%s|%d' % (nome, cat, g, k)).encode('utf-8')).hexdigest()[:8])
            out.append(dict(_a=a, _b=b, id_ocorrencia=oid, arquivo=nome, campo='md', caminho=nome, categoria=cat, subtipo=sub, classe=classe, motivo=motivo, casamento=g,
                            trecho=t[max(0, a - 60):b + 60].replace('\n', ' ⏎ ')))
    return out

COLUNAS = ['id_ocorrencia', 'arquivo', 'lote', 'gerencia', 'campo', 'caminho', 'escopo', 'categoria', 'subtipo', 'classe', 'motivo', 'regra3_difere', 'casamento', 'trecho']

def varre_pacote(caminho, arq):
    raw = open(caminho, 'rb').read()
    lf = raw.replace(b'\r\n', b'\n')
    P = json.loads(lf.decode('utf-8'), object_pairs_hook=collections.OrderedDict)
    return P, varre(P, arq), hashlib.sha256(lf).hexdigest()

def contagem(ocs):
    c = collections.Counter(o['classe'] for o in ocs)
    return dict(c)

def main():
    """Uso: python -I inventario_v111.py <pacote.json> <pacote_estudante.json> <pasta estudante/> <saida.csv> [<saida.json>]"""
    pj, pe, pmd, csv_out = sys.argv[1:5]
    todos, info = [], {}
    P, oc, h = varre_pacote(pj, 'D'); info['D'] = dict(arquivo=pj, sha256_LF=h, ocorrencias=contagem(oc)); todos += oc
    E, oe, h = varre_pacote(pe, 'E'); info['E'] = dict(arquivo=pe, sha256_LF=h, ocorrencias=contagem(oe)); todos += oe
    ids_item = [i['id'] for i in P['itens']]
    om = []
    for nome in sorted(os.listdir(pmd)):
        if nome.endswith('.md') and nome != 'README.md':
            om += varre_md(nome, open(os.path.join(pmd, nome), encoding='utf-8').read(), ids_item)
    info['MD'] = dict(arquivo=pmd, ocorrencias=contagem(om)); todos += om
    with open(csv_out, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=COLUNAS, extrasaction='ignore', restval='')
        w.writeheader()
        for o in todos:
            w.writerow(o)
    if len(sys.argv) > 5:
        json.dump(info, open(sys.argv[5], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps(info, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
