# -*- coding: utf-8 -*-
"""T-59 (d) + correção R1 (T59_T60_reconciliacao_2026-10-14.md, V-6) + errata T-66 (T66_decisoes_2026-10-14.md, casos N-1 a N-5 e T-1 a T-9) — teste do validador `validar_erros.py` (arquivo "Exportar meus erros", formato camara2026.erros v1).
Versão mantida (D-R59-08). AUTÔNOMO: não importa `common` nem nada do gerador; deriva REPO de __file__ (raiz do repositório = três níveis acima desta pasta); usa
saida/pacote/pacote.json e saida/pacote/exemplo_erros_v1.json; grava os casos fictícios num diretório temporário (tempfile.mkdtemp()), apagado ao fim; NADA é gravado no repositório.
Cada caso é validado por `python3 -I validar_erros.py` (processo separado: confere também o código de saída). Dados fictícios; nenhum dado da candidata.
Casos: exemplo da D-T59-04; arquivo válido com ids reais; 4 inválidos; incoerente D; duplicado; uso (código 2); [R1] ordem das listas (5 + empate + extra), constantes NaN/Infinity,
BOM (aceito, duplicado, BOM + Latin-1), ne/tl fora do domínio (10 casos de V-4 + texto + PACOTE_PADRAO sem --pacote); [T-66] pacote.nome/geradoEm/versao null (N-1 a N-5), discursivas[].nota fora de [0, soma] (T-1 a T-9).
Saída: uma linha OK/FALHA por conferência; código 1 se houver falha. Rodar: python3 -I saida/treino/ferramentas/validar_erros_teste.py (de qualquer diretório)."""
import copy, hashlib, json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
VAL = os.path.join(HERE, 'validar_erros.py')
PAC = os.path.join(REPO, 'saida', 'pacote', 'pacote.json')
EX = os.path.join(REPO, 'saida', 'pacote', 'exemplo_erros_v1.json')
ANTES = sorted(os.listdir(HERE))
SHA_PAC0 = hashlib.sha256(open(PAC, 'rb').read()).hexdigest()
SHA_EX0 = hashlib.sha256(open(EX, 'rb').read()).hexdigest()
CASOS = tempfile.mkdtemp(prefix='casos_erros_')
pacote = json.load(open(PAC, encoding='utf-8'))
ex = json.load(open(EX, encoding='utf-8'))
res = []


def chk(nome, ok, det=''):
    res.append(bool(ok)); print(('OK    ' if ok else 'FALHA ') + nome + (' | ' + det if det else ''))


def grava(nome, obj=None, raw=None):
    p = os.path.join(CASOS, nome)
    open(p, 'wb').write(raw if raw is not None else (json.dumps(obj, ensure_ascii=False, indent=1) + '\n').encode('utf-8'))
    return p


def cli(p, *extra, pac=True, cwd=None):
    cmd = [sys.executable, '-I', VAL, p] + (['--pacote', PAC] if pac else []) + ['--json'] + list(extra)
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    return r.returncode, (json.loads(r.stdout) if r.stdout.strip() else None), r.stderr


def ordens(R): return [a for a in R['avisos'] if a.startswith('ordem:')]


try:
    # 1. o exemplo da decisão (ids fictícios: tudo desconhecido)
    rc, R, _ = cli(EX)
    chk('exemplo D-T59-04: ACEITO (código 0), forma e tipos ok, 0 incoerência', rc == 0 and R['veredito'] == 'ACEITO' and not R['incoerencias'], R['veredito'])
    chk('exemplo: ids desconhecidos listados por campo, com ocorrências (caderno XX-0001; det XX-0001 e XX-0002; discursivas DX)',
        {k: sorted(v['ids']) for k, v in R['ids_desconhecidos'].items()} == {'caderno': ['XX-0001'], 'tentativas[].det': ['XX-0001', 'XX-0002'], 'discursivas': ['DX']}
        and R['ids_desconhecidos']['tentativas[].det']['ocorrencias'] == 2)
    chk('exemplo: pacote de origem ≠ vigente registrado (aviso), SHA-256 do arquivo = %s…' % SHA_EX0[:12],
        R['pacote_origem']['igual'] is False and any('pacote de origem ≠ vigente' in a for a in R['avisos']) and R['sha256'] == SHA_EX0)
    chk('exemplo: sem aviso de ordem; fora_dos_calculos com as três chaves vazias', not ordens(R) and R['fora_dos_calculos'] == {'tentativas': [], 'caderno': [], 'discursivas': []})

    # 2. arquivo válido com ids reais do pacote
    it = pacote['itens']; ids = [i['id'] for i in it[:3]]
    va = copy.deepcopy(ex)
    va['pacote'] = {'nome': pacote['nome'], 'geradoEm': pacote['geradoEm'], 'versao': pacote['versao'], 'origem': 'publicado'}
    va['caderno'] = [{'id': ids[0], 'itemEdital': it[0]['itemEdital'], 'noPacote': True, 'errou': 2, 'seq': 0, 'desde': '2026-10-15T10:00:00.000Z'},
                     {'id': 'OUTRO-PACOTE-9', 'itemEdital': None, 'noPacote': False, 'errou': 1, 'seq': 1, 'desde': '2026-10-15T10:00:00.000Z'}]
    va['resumo'].update(itensNoCaderno=2, tentativas=1)
    va['tentativas'] = [{'tipo': 'sim', 'ref': pacote['simulados'][0]['id'], 'nome': 'Simulado', 'modulo': None, 'data': '2026-10-15T10:00:00.000Z', 'seg': 60, 'total': 3, 'nota': 0, 'ac': 1, 'er': 1, 'br': 1,
                         'por': {it[0]['itemEdital']: {'c': 1, 'e': 1, 'b': 1}},
                         'det': [{'id': ids[0], 'r': 'C', 'st': 'c' if it[0]['gabarito'] == 'C' else 'e'}, {'id': ids[1], 'r': 'E', 'st': 'e' if it[1]['gabarito'] == 'C' else 'c'}, {'id': ids[2], 'r': None, 'st': 'b'}]}]
    t = va['tentativas'][0]; t['ac'] = sum(d['st'] == 'c' for d in t['det']); t['er'] = sum(d['st'] == 'e' for d in t['det']); t['nota'] = t['ac'] - t['er']
    t['por'] = {it[0]['itemEdital']: {'c': t['ac'], 'e': t['er'], 'b': t['br']}}
    va['discursivas'][0].update(id=pacote['discursivas'][0]['id'], tipo=pacote['discursivas'][0]['tipo'])
    rc, R, _ = cli(grava('valido_ids_reais.json', va))
    chk('arquivo válido com ids reais: ACEITO; pacote de origem IGUAL ao vigente; só o id fora do pacote ("OUTRO-PACOTE-9") é desconhecido; 0 incoerência; 0 aviso',
        rc == 0 and R['pacote_origem']['igual'] and list(R['ids_desconhecidos']) == ['caderno'] and list(R['ids_desconhecidos']['caderno']['ids']) == ['OUTRO-PACOTE-9'] and not R['incoerencias'] and not R['avisos'],
        'avisos %s; incoerências %s' % (R['avisos'], R['incoerencias']))

    # 3. casos inválidos (RECUSADO, código 1)
    a = copy.deepcopy(ex); a['versaoFormato'] = 2
    rc, R, _ = cli(grava('invalido_A_versaoFormato2.json', a))
    chk('INVÁLIDO A (versaoFormato 2): RECUSADO (código 1) com o motivo "versão 2 desconhecida"', rc == 1 and R['veredito'] == 'RECUSADO' and any('versaoFormato' in m and '2' in m for m in R['motivos_recusa']), '; '.join(R['motivos_recusa']))
    b = copy.deepcopy(ex); del b['resumo']; b['tentativas'][0]['seg'] = '600'; b['discursivas'][0]['notas']['1'] = 0.3
    rc, R, _ = cli(grava('invalido_B_campo_ausente_e_tipo.json', b))
    chk('INVÁLIDO B (resumo ausente, seg como string, nota 0.3 fora da escala): RECUSADO (código 1) com 3 motivos',
        rc == 1 and R['veredito'] == 'RECUSADO' and len(R['motivos_recusa']) == 3 and any('$.resumo' in m for m in R['motivos_recusa']) and any('seg' in m for m in R['motivos_recusa']) and any('notas' in m for m in R['motivos_recusa']), ' || '.join(R['motivos_recusa']))
    raw = open(EX, 'rb').read(); c = raw[:len(raw) // 2]
    rc, R, _ = cli(grava('invalido_C_json_truncado.json', raw=c))
    chk('INVÁLIDO C (JSON truncado): RECUSADO (código 1) "não abre como JSON UTF-8"', rc == 1 and R['veredito'] == 'RECUSADO' and R['motivos_recusa'][0].startswith('não abre como JSON UTF-8'))
    rc, R, _ = cli(grava('invalido_C2_formato_errado.json', dict(ex, formato='outro.formato')))
    chk('INVÁLIDO C2 (formato diferente): RECUSADO', rc == 1 and R['veredito'] == 'RECUSADO' and any('formato' in m for m in R['motivos_recusa']))

    # 4. aceito com incoerências (D-T59-05): listadas com o motivo e fora dos cálculos
    d = copy.deepcopy(ex); d['tentativas'][0]['ac'] = 2; d['tentativas'][0]['nota'] = 5; d['caderno'][0]['errou'] = 0; d['resumo']['itensNoCaderno'] = 4
    rc, R, _ = cli(grava('incoerente_D.json', d))
    mot = ' | '.join('%s %s' % (c_, m) for c_, m in R['incoerencias'])
    chk('INCOERENTE D (ac+er+br≠total, nota≠ac−er, soma de `por`≠ac, errou 0, itensNoCaderno≠len): ACEITO com tentativa 0 e caderno 0 fora dos cálculos',
        rc == 0 and R['veredito'] == 'ACEITO' and R['fora_dos_calculos'] == {'tentativas': [0], 'caderno': [0], 'discursivas': []} and 'ac+er+br=3, total=2' in mot and 'nota=5, ac-er=1' in mot and 'soma de por' in mot and 'errou=0' in mot and 'itensNoCaderno' in mot
        and R['contagens']['tentativas_validas'] == 0, '%d incoerências' % len(R['incoerencias']))

    # 5. duplicado
    reg1 = grava('importados_sha.json', [{'sha256': SHA_EX0, 'exportadoEm': '2000-01-01T00:00:00.000Z'}])
    reg2 = grava('importados_exportadoEm.json', [{'sha256': 'x', 'exportadoEm': ex['exportadoEm']}])
    rc1, R1, _ = cli(EX, '--importados', reg1); rc2, R2, _ = cli(EX, '--importados', reg2)
    chk('DUPLICADO por SHA-256 e por exportadoEm (código 3); sem registro, ACEITO', rc1 == 3 == rc2 and R1['veredito'] == R2['veredito'] == 'DUPLICADO', '%s / %s' % (R1['motivos_recusa'][0], R2['motivos_recusa'][0]))

    # 6. uso (código 2)
    rc = subprocess.run([sys.executable, '-I', VAL], capture_output=True, text=True).returncode
    chk('sem argumento: código 2 (uso)', rc == 2)

    # ---------- R1 (T59_T60_reconciliacao_2026-10-14.md) ----------
    # 7. R-1: ordem das listas -> aviso `ordem:`, sem mudar veredito, código nem fora_dos_calculos
    def base_ordenada():
        o = copy.deepcopy(ex)
        o['caderno'] = [{'id': 'XX-0001', 'itemEdital': 'P1-0.1', 'noPacote': True, 'errou': 3, 'seq': 0, 'desde': '2026-01-01T11:00:00.000Z'},
                        {'id': 'XX-0002', 'itemEdital': 'P1-0.1', 'noPacote': True, 'errou': 3, 'seq': 1, 'desde': '2026-01-01T11:00:00.000Z'},
                        {'id': 'XX-0003', 'itemEdital': 'P1-0.1', 'noPacote': True, 'errou': 1, 'seq': 0, 'desde': '2026-01-01T11:00:00.000Z'}]
        o['respostasCaderno'] = [{'id': 'XX-0001', 'ok': True, 'em': '2026-01-01T11:10:00.000Z'}, {'id': 'XX-0002', 'ok': False, 'em': '2026-01-01T11:20:00.000Z'}]
        t0 = o['tentativas'][0]; t1 = copy.deepcopy(t0); t1['data'] = '2026-01-02T11:00:00.000Z'
        o['tentativas'] = [t0, t1]
        o['saidas'] = [{'id': 'XX-0001', 'em': '2026-01-01T12:00:00.000Z', 'dias': 1}, {'id': 'XX-0002', 'em': '2026-01-03T12:00:00.000Z', 'dias': 2}]
        d0 = o['discursivas'][0]; d1 = copy.deepcopy(d0); d1['id'] = 'DY'
        o['discursivas'] = [d0, d1]
        o['resumo'].update(tentativas=2, itensNoCaderno=3, saidas=2, discursivasEntregues=2)
        return o
    bo = base_ordenada()
    rc, R, _ = cli(grava('ordem_0_base_em_ordem.json', bo))
    chk('R-1 base em ordem (5 listas com 2-3 itens): ACEITO, código 0, 0 aviso `ordem:`, 0 incoerência', rc == 0 and R['veredito'] == 'ACEITO' and not ordens(R) and not R['incoerencias'], 'avisos %s; inc %s' % (R['avisos'], R['incoerencias']))
    base_fdc = R['fora_dos_calculos']
    def troca(o, lista, i=0, j=1): o[lista][i], o[lista][j] = o[lista][j], o[lista][i]
    for lista, i, j, k in (('caderno', 0, 2, 1), ('respostasCaderno', 0, 1, 1), ('tentativas', 0, 1, 1), ('saidas', 0, 1, 1), ('discursivas', 0, 1, 1)):
        o = base_ordenada(); troca(o, lista, i, j)
        rc, R, _ = cli(grava('ordem_%s_fora.json' % lista, o))
        av = ordens(R)
        chk('R-1 `%s` fora de ordem: ACEITO, código 0, 1 aviso `ordem: %s fora da ordem …` (índice %d), fora_dos_calculos inalterado' % (lista, lista, k),
            rc == 0 and R['veredito'] == 'ACEITO' and len(av) == 1 and av[0].startswith('ordem: %s fora da ordem ' % lista) and av[0].endswith('(primeira posição divergente: índice %d)' % k)
            and R['fora_dos_calculos'] == base_fdc and not R['incoerencias'], '; '.join(av))
    o = base_ordenada(); o['caderno'][0]['errou'] = 3; o['caderno'][1]['errou'] = 3; o['caderno'][0]['id'], o['caderno'][1]['id'] = 'XX-0002', 'XX-0001'
    rc, R, _ = cli(grava('ordem_caderno_empate_id_invertido.json', o))
    chk('R-1 extra: caderno com mesmo `errou` e id decrescente = fora de ordem (chave (-errou, id))', rc == 0 and len(ordens(R)) == 1 and 'caderno' in ordens(R)[0])
    o = base_ordenada(); o['respostasCaderno'][1]['em'] = o['respostasCaderno'][0]['em']; o['tentativas'][1]['data'] = o['tentativas'][0]['data']; o['saidas'][1]['em'] = o['saidas'][0]['em']
    rc, R, _ = cli(grava('ordem_empate.json', o))
    chk('R-1 empate de data (respostasCaderno, tentativas, saidas) e de `errou`+id distintos (caderno): ACEITO, 0 aviso `ordem:`', rc == 0 and R['veredito'] == 'ACEITO' and not ordens(R), '; '.join(ordens(R)))
    o = base_ordenada(); troca(o, 'caderno', 0, 2); troca(o, 'saidas'); troca(o, 'discursivas')
    rc, R, _ = cli(grava('ordem_tres_listas.json', o))
    chk('R-1 extra: 3 listas fora de ordem -> 3 avisos `ordem:` (um por lista), veredito ACEITO', rc == 0 and len(ordens(R)) == 3, '; '.join(ordens(R)))
    chk('R-1 texto: o aviso aparece na seção AVISOS da saída em texto',
        'ordem: saidas fora da ordem' in subprocess.run([sys.executable, '-I', VAL, os.path.join(CASOS, 'ordem_tres_listas.json'), '--pacote', PAC], capture_output=True, text=True).stdout)

    # 8. R-2: NaN / Infinity / -Infinity recusados
    rawex = open(EX, encoding='utf-8').read()
    for nome, antigo, novo in (('NaN', '"ne": 0', '"ne": NaN'), ('Infinity', '"seg": 600', '"seg": Infinity'), ('-Infinity', '"nota": 1.8', '"nota": -Infinity')):
        assert rawex.count(antigo) == 1, antigo
        rc, R, _ = cli(grava('constante_%s.json' % nome, raw=rawex.replace(antigo, novo).encode('utf-8')))
        chk('R-2 constante %s: RECUSADO, código 1, motivo "não abre como JSON UTF-8: constante não JSON: %s"' % (nome, nome),
            rc == 1 and R['veredito'] == 'RECUSADO' and R['motivos_recusa'][0].startswith('não abre como JSON UTF-8') and ('constante não JSON: %s' % nome) in R['motivos_recusa'][0], R['motivos_recusa'][0])

    # 9. R-3: BOM UTF-8 inicial tolerado, com aviso; SHA-256 sobre os bytes recebidos
    BOM = b'\xef\xbb\xbf'
    rawb = open(EX, 'rb').read()
    pb = grava('bom_ok.json', raw=BOM + rawb)
    rc, R, _ = cli(pb)
    chk('R-3 BOM: ACEITO (código 0) com o aviso "arquivo com BOM UTF-8 (tolerado; …)"; mesmos resultados do arquivo sem BOM',
        rc == 0 and R['veredito'] == 'ACEITO' and 'arquivo com BOM UTF-8 (tolerado; SHA-256 calculado sobre os bytes recebidos)' in R['avisos'] and not R['incoerencias'] and R['exportadoEm'] == ex['exportadoEm'])
    chk('R-3 BOM: SHA-256 e `bytes` sobre os bytes recebidos (≠ o do mesmo arquivo sem BOM; bytes = sem BOM + 3)',
        R['sha256'] == hashlib.sha256(BOM + rawb).hexdigest() and R['sha256'] != SHA_EX0 and R['bytes'] == len(rawb) + 3)
    rc, R, _ = cli(pb, '--importados', reg2)
    chk('R-3 BOM + `exportadoEm` já importado (arquivo sem BOM): DUPLICADO (código 3)', rc == 3 and R['veredito'] == 'DUPLICADO' and 'exportadoEm' in R['motivos_recusa'][0], R['motivos_recusa'][0])
    rc, R, _ = cli(grava('bom_latin1.json', raw=BOM + json.dumps(ex, ensure_ascii=False).replace('\u2014', '-').encode('latin-1')))
    chk('R-3 BOM + Latin-1: continua RECUSADO (código 1), "não abre como JSON UTF-8"', rc == 1 and R['veredito'] == 'RECUSADO' and R['motivos_recusa'][0].startswith('não abre como JSON UTF-8'), R['motivos_recusa'][0][:90])
    rc, R, _ = cli(grava('bom_duplo.json', raw=BOM + BOM + rawb))
    chk('R-3 extra: dois BOM seguidos: RECUSADO (só o primeiro é tolerado)', rc == 1 and R['veredito'] == 'RECUSADO')
    rc, R, _ = cli(EX)
    chk('R-3 arquivo sem BOM: nenhum aviso de BOM', not any('BOM' in a for a in R['avisos']))

    # 10. A1 / V-4: `ne`/`tl` fora do domínio = incoerência só daquela discursiva (ACEITO); tipo errado = RECUSADO
    def com_disc(**kw):
        o = copy.deepcopy(ex); o['discursivas'][0].update(kw); return o
    aceitos = (('ne 1.5', dict(ne=1.5), 'ne=1.5 (deve ser inteiro >= 0)'), ('ne -1', dict(ne=-1), 'ne=-1 (deve ser inteiro >= 0)'), ('ne 1.0', dict(ne=1.0), 'ne=1.0 (deve ser inteiro >= 0)'),
               ('tl null', dict(tl=None), 'tl=null (deve ser inteiro >= 1)'), ('tl 0', dict(tl=0), 'tl=0 (deve ser inteiro >= 1)'), ('tl 2.5', dict(tl=2.5), 'tl=2.5 (deve ser inteiro >= 1)'))
    for rot, kw, msg in aceitos:
        rc, R, _ = cli(grava('ne_tl_%s.json' % rot.replace(' ', '_'), com_disc(**kw)))
        chk('V-4 %s: ACEITO (código 0), incoerência da discursiva listada ("%s"), fora_dos_calculos.discursivas == [0], tentativas/caderno intactos' % (rot, msg),
            rc == 0 and R['veredito'] == 'ACEITO' and R['fora_dos_calculos'] == {'tentativas': [], 'caderno': [], 'discursivas': [0]} and [m for _, m in R['incoerencias']] == [msg]
            and R['incoerencias'][0][0] == 'discursivas[0] (DX)', str(R['incoerencias']))
    for rot, kw in (('ne "1"', dict(ne='1')), ('ne true', dict(ne=True)), ('ne null', dict(ne=None)), ('tl "3"', dict(tl='3'))):
        rc, R, _ = cli(grava('ne_tl_recusa_%s.json' % rot.replace(' ', '_').replace('"', ''), com_disc(**kw)))
        chk('V-4 %s: RECUSADO (código 1), motivo em `$.discursivas[0].%s`' % (rot, rot[:2]), rc == 1 and R['veredito'] == 'RECUSADO' and any('$.discursivas[0].%s' % rot[:2] in m for m in R['motivos_recusa']), '; '.join(R['motivos_recusa']))
    o = com_disc(ne=1.5, tl=0)
    rc, R, _ = cli(grava('ne_tl_ambos.json', o))
    chk('V-4 ne 1.5 e tl 0 juntos: ACEITO, 2 incoerências da mesma discursiva, fora_dos_calculos.discursivas == [0] (uma vez só)', rc == 0 and len(R['incoerencias']) == 2 and R['fora_dos_calculos']['discursivas'] == [0])
    o = copy.deepcopy(ex); d1 = copy.deepcopy(o['discursivas'][0]); d1['id'] = 'DY'; d1['ne'] = 2.5; o['discursivas'].append(d1); o['resumo']['discursivasEntregues'] = 2
    rc, R, _ = cli(grava('ne_tl_so_a_segunda.json', o))
    chk('V-4 duas discursivas, só a segunda com ne 2.5: ACEITO, fora_dos_calculos.discursivas == [1]; a primeira segue válida',
        rc == 0 and R['fora_dos_calculos']['discursivas'] == [1] and R['incoerencias'][0][0] == 'discursivas[1] (DY)' and R['contagens']['discursivas'] == 2)
    o = com_disc(ne=2, tl=3)
    rc, R, _ = cli(grava('ne_tl_validos.json', o))
    chk('V-4 ne 2 e tl 3 (no domínio): 0 incoerência, discursivas fora = []', rc == 0 and not R['incoerencias'] and R['fora_dos_calculos']['discursivas'] == [])
    # equivalente ao `qa_ne_decimal` do QA-plataforma (T-60, A1): D1 entregue com NE digitado "1.5", exportado ne: 1.5
    qa = copy.deepcopy(ex); qa['discursivas'][0].update(id='D1', ne=1.5)
    rawq = json.dumps(qa, ensure_ascii=False, indent=1)
    pq = grava('qa_ne_decimal.json', raw=(rawq + '\n').encode('utf-8'))
    rc, R, _ = cli(pq)
    chk('V-4 equivalente de `qa_ne_decimal` (D1, ne: 1.5): ACEITO com 1 incoerência de discursiva (antes: RECUSADO)', rc == 0 and R['veredito'] == 'ACEITO' and len(R['incoerencias']) == 1 and R['fora_dos_calculos']['discursivas'] == [0])
    r = subprocess.run([sys.executable, '-I', VAL, pq, '--pacote', PAC], capture_output=True, text=True)
    chk('V-4 texto: linha INCOERÊNCIAS mostra `discursivas [0]` e o motivo', 'discursivas [0]' in r.stdout and 'discursivas[0] (D1): ne=1.5 (deve ser inteiro >= 0)' in r.stdout and r.returncode == 0)

    # 11. V-0a: sem --pacote, de outro diretório, lê saida/pacote/pacote.json da raiz do repositório
    rc, R, _ = cli(EX, pac=False, cwd=tempfile.gettempdir())
    chk('V-0a sem --pacote, rodado de outro diretório: ACEITO e o pacote vigente é o de saida/pacote/pacote.json ("%s")' % pacote['nome'],
        rc == 0 and R['pacote_origem']['vigente']['nome'] == pacote['nome'] and R['pacote_origem']['vigente']['geradoEm'] == pacote['geradoEm'])

    # ---------- T-66 (T66_decisoes_2026-10-14.md) ----------
    # 12a. N-1 a N-5: pacote.nome/geradoEm/versao null toleráveis com aviso (V-7 a V-10)
    def com_pac(base, **kw):
        o = copy.deepcopy(base); o['pacote'] = dict(o['pacote'], **kw); return o
    AV_ORIG = 'pacote de origem ≠ vigente: '
    def av_nulo(k): return 'pacote.%s = null (pacote de origem sem esse campo; tolerado)' % k
    AV_CARR = 'pacote.origem = "carregado" (pacote carregado no aparelho, não o publicado)'
    def txt(p): return subprocess.run([sys.executable, '-I', VAL, p, '--pacote', PAC], capture_output=True, text=True).stdout
    rc, R, _ = cli(grava('n1.json', com_pac(va, versao=None, origem='carregado')))
    chk('N-1 versao null + carregado: ACEITO (código 0); avisos nesta ordem: ≠ vigente, pacote.versao = null, carregado; igual falso; arquivo.versao null',
        rc == 0 and R['veredito'] == 'ACEITO' and len(R['avisos']) == 3 and R['avisos'][0].startswith(AV_ORIG) and R['avisos'][1] == av_nulo('versao') and R['avisos'][2] == AV_CARR
        and R['pacote_origem']['igual'] is False and R['pacote_origem']['arquivo']['versao'] is None, str(R['avisos']))
    rc, R, _ = cli(grava('n2.json', com_pac(va, nome=None, geradoEm=None, versao=None, origem='carregado')))
    esperado = [AV_ORIG + 'null (arquivo) x "%s" (vigente)' % pacote['nome'], av_nulo('nome'), av_nulo('geradoEm'), av_nulo('versao'), AV_CARR]
    chk('N-2 nome, geradoEm e versao null + carregado: ACEITO; avisos exatamente: ≠ vigente (nome null sem aspas), 3 avisos null (nome, geradoEm, versao), carregado',
        rc == 0 and R['veredito'] == 'ACEITO' and R['avisos'] == esperado and R['pacote_origem']['arquivo'] == {'nome': None, 'geradoEm': None, 'versao': None, 'origem': 'carregado'}, str(R['avisos']))
    linha = [x for x in txt(os.path.join(CASOS, 'n2.json')).split('\n') if x.startswith('pacote de origem:')]
    chk('N-2 texto: linha `pacote de origem: null (null, versao null, carregado) | vigente: "%s" (%s) | DIVERGENTE`' % (pacote['nome'], pacote['geradoEm']),
        linha == ['pacote de origem: null (null, versao null, carregado) | vigente: "%s" (%s) | DIVERGENTE' % (pacote['nome'], pacote['geradoEm'])], str(linha))
    rc, R, _ = cli(grava('n3.json', com_pac(va, versao=None, origem='publicado')))
    chk('N-3 versao null + publicado: ACEITO, aviso `pacote.versao = null …`, sem aviso de "carregado"',
        rc == 0 and R['veredito'] == 'ACEITO' and av_nulo('versao') in R['avisos'] and AV_CARR not in R['avisos'] and len(R['avisos']) == 2, str(R['avisos']))
    n4 = copy.deepcopy(va); del n4['pacote']['versao']
    rc, R, _ = cli(grava('n4.json', n4))
    chk('N-4 chave pacote.versao ausente: RECUSADO (código 1), `$.pacote.versao: campo ausente`', rc == 1 and R['veredito'] == 'RECUSADO' and R['motivos_recusa'] == ['$.pacote.versao: campo ausente'], str(R['motivos_recusa']))
    for rot, kw, msg in (('versao "1"', dict(versao='1'), '$.pacote.versao: esperado inteiro ou null, veio str'), ('versao 1.0', dict(versao=1.0), '$.pacote.versao: esperado inteiro ou null, veio float'),
                         ('versao true', dict(versao=True), '$.pacote.versao: esperado inteiro ou null, veio bool'),
                         ('geradoEm "14/10/2026"', dict(geradoEm='14/10/2026'), '$.pacote.geradoEm: esperado string AAAA-MM-DD ou null, veio str'),
                         ('nome 5', dict(nome=5), '$.pacote.nome: esperado string ou null, veio int')):
        rc, R, _ = cli(grava('n5_%s.json' % rot.replace(' ', '_').replace('"', '').replace('/', '-'), com_pac(va, **kw)))
        chk('N-5 %s: RECUSADO (código 1), motivo exato `%s`' % (rot, msg), rc == 1 and R['veredito'] == 'RECUSADO' and R['motivos_recusa'] == [msg], str(R['motivos_recusa']))

    # 12b. T-1 a T-9: discursivas[].nota (V-11). Base: va (D1 do pacote vigente; teto 14.3); `nota` escrita no texto do JSON (1e999 só existe como literal)
    def com_nota(literal, did=None, **kw):
        o = copy.deepcopy(va); o['discursivas'][0].update(kw)
        if did: o['discursivas'][0]['id'] = did
        raw = json.dumps(o, ensure_ascii=False, indent=1)
        assert raw.count('"nota": 1.8') == 1
        return grava('nota_%s.json' % abs(hash(literal + str(did) + str(kw))), raw=(raw.replace('"nota": 1.8', '"nota": ' + literal) + '\n').encode('utf-8'))
    def inc_nota(literal, did=None, **kw):
        rc, R, _ = cli(com_nota(literal, did, **kw)); return rc, R, [m for _, m in R['incoerencias']]
    D1M = 'nota=%s (deve ser número finito entre 0 e 14.3)'
    rc, R, ms = inc_nota('1e999')
    chk('T-1 nota 1e999: ACEITO (código 0); incoerencias == [["discursivas[0] (D1)", "nota=Infinity (…entre 0 e 14.3)"]]; fora_dos_calculos.discursivas == [0]',
        rc == 0 and R['veredito'] == 'ACEITO' and R['incoerencias'] == [['discursivas[0] (D1)', D1M % 'Infinity']] and R['fora_dos_calculos']['discursivas'] == [0], str(R['incoerencias']))
    rc, R, ms = inc_nota('-1e999'); chk('T-2 nota -1e999: `nota=-Infinity (…entre 0 e 14.3)`', rc == 0 and ms == [D1M % '-Infinity'], str(ms))
    rc, R, ms = inc_nota('1e308'); chk('T-3 nota 1e308: `nota=1e+308 (…entre 0 e 14.3)`', rc == 0 and ms == [D1M % '1e+308'], str(ms))
    for lit, rep in (('14.31', '14.31'), ('-0.01', '-0.01')):
        rc, R, ms = inc_nota(lit); chk('T-4 nota %s: `nota=%s (…entre 0 e 14.3)`' % (lit, rep), rc == 0 and ms == [D1M % rep], str(ms))
    for lit in ('14.3', '0', '-0.0', 'null', '10.65'):
        rc, R, ms = inc_nota(lit); chk('T-5 nota %s: nenhuma incoerência, discursivas fora == []' % lit, rc == 0 and R['veredito'] == 'ACEITO' and not R['incoerencias'] and R['fora_dos_calculos']['discursivas'] == [], str(ms))
    d3 = pacote['discursivas'][2]['id']
    assert d3 == 'D3'
    rc, R, ms = inc_nota('28.5', did='D3'); chk('T-6 D3 com 28.5: nenhuma incoerência', rc == 0 and not R['incoerencias'], str(ms))
    rc, R, ms = inc_nota('28.6', did='D3'); chk('T-6 D3 com 28.6: `nota=28.6 (deve ser número finito entre 0 e 28.5)`', rc == 0 and ms == ['nota=28.6 (deve ser número finito entre 0 e 28.5)'], str(ms))
    rc, R, ms = inc_nota('50', did='D9'); chk('T-7 id D9 (fora do pacote) com 50: nenhuma incoerência; D9 só em ids desconhecidos', rc == 0 and not R['incoerencias'] and 'D9' in R['ids_desconhecidos']['discursivas']['ids'], str(ms))
    rc, R, ms = inc_nota('-1', did='D9'); chk('T-7 D9 com -1: `nota=-1 (deve ser número finito >= 0)`', rc == 0 and ms == ['nota=-1 (deve ser número finito >= 0)'], str(ms))
    rc, R, ms = inc_nota('1e999', did='D9'); chk('T-7 D9 com 1e999: `nota=Infinity (deve ser número finito >= 0)`', rc == 0 and ms == ['nota=Infinity (deve ser número finito >= 0)'], str(ms))
    rc, R, ms = inc_nota('1e999', ne=1.5)
    chk('T-8 ne 1.5 e nota 1e999: 2 motivos nesta ordem (ne, nota); discursivas fora == [0] uma vez só',
        rc == 0 and ms == ['ne=1.5 (deve ser inteiro >= 0)', D1M % 'Infinity'] and R['fora_dos_calculos']['discursivas'] == [0], str(ms))
    rc, R, ms = inc_nota('"1"')
    chk('T-9 nota "1" (string): RECUSADO (código 1), `$.discursivas[0].nota: esperado número ou null, veio str` (sem mudança)', rc == 1 and R['veredito'] == 'RECUSADO' and R['motivos_recusa'] == ['$.discursivas[0].nota: esperado número ou null, veio str'], str(R['motivos_recusa']))
    rc, R, ms = inc_nota('1e999', tl=None)
    chk('T-8 extra: tl null e nota 1e999: motivos na ordem tl, nota', rc == 0 and ms == ['tl=null (deve ser inteiro >= 1)', D1M % 'Infinity'], str(ms))
    _, _, ms = inc_nota('14.3000000001')
    chk('V-11 folga de ponto flutuante (1e-9 acima do teto) aceita; 14.31 recusada (T-4)', ms == [])

    # 13. somente leitura e sem resíduo
    chk('o exemplo e o pacote não foram alterados pelo validador (SHA-256 iguais)', hashlib.sha256(open(EX, 'rb').read()).hexdigest() == SHA_EX0 and hashlib.sha256(open(PAC, 'rb').read()).hexdigest() == SHA_PAC0)
    chk('a pasta do validador não ganhou nem perdeu arquivo durante o teste', sorted(os.listdir(HERE)) == ANTES, str(sorted(set(os.listdir(HERE)) ^ set(ANTES))))
finally:
    shutil.rmtree(CASOS, ignore_errors=True)
chk('diretório temporário apagado ao fim', not os.path.exists(CASOS))
print('\n%d conferências; %d falhas' % (len(res), res.count(False)))
sys.exit(1 if False in res else 0)
