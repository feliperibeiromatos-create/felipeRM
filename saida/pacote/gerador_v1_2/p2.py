# -*- coding: utf-8 -*-
"""Constrói lotes, itens AUTORAL e discursivas de P2 (Lotes 1, 1-C, 2, 3)."""
import re
from common import *
from gce import *
from registry import REG

PT_NUM = lambda s: float(s.replace('.', '').replace(',', '.'))

# Erratas da GCE (consolidações sincronizadas em 13/10/2026). Cada entrada: (id, X, Y, fonte, escopo).
# fonte 'cons' = texto conferido contra saida/gce/GCE_Lote*_consolidacao_GCE.md (ver sync_check.py); 'F5' = decisão D-T12-V12.
ERRATA = {
    'L1': [
        ('E1', 'um sistema com diarização habilitada é suficiente',
         'um sistema com diarização habilitada, por si só, sem amostras de voz de referência, é suficiente', 'cons'),
        ('E2', 'de modo que um sistema pode diarizar', 'e um sistema pode diarizar', 'cons'),
        ('E3', 'e de pistas prosódicas', 'e, eventualmente, de pistas prosódicas', 'cons'),
        ('E4a', 'O WER mede só palavras: não mede pontuação, capitalização nem atribuição de locutor.',
         'No cálculo usual, sobre texto normalizado, o WER não mede pontuação nem capitalização; a atribuição de locutor fica fora do WER em qualquer convenção.', 'cons'),
        ('E4b', 'ele ignora pontuação e locutores',
         'no cálculo usual ele ignora pontuação, e em qualquer convenção ignora locutores', 'cons'),
        ('E4c', 'WER mede apenas palavras; pontuação, capitalização e locutor estão fora da métrica',
         'No cálculo usual, pontuação e capitalização ficam fora do WER, e a atribuição de locutor fica fora em qualquer convenção', 'cons-cap'),
        ('E5', 'CLM (texto)', 'CLM (texto; indisponível para pt-BR na AWS)', 'cons'),
        ('E9', 'o áudio continua sendo convertido em espectrograma antes de entrar na rede',
         'em geral (por exemplo, no Whisper) o áudio é convertido em espectrograma antes de entrar na rede; há modelos que recebem a forma de onda bruta (por exemplo, wav2vec 2.0, arXiv 2006.11477, seção 2 [V 08/10/2026])', 'cons'),
        ('E10', 'Escolha de ferramenta para o Departamento de Taquigrafia',
         'Escolha de ferramenta para o departamento de registro da Câmara (Derep, antigo DETAQ; Ato da Mesa nº 251/2026)', 'cons'),
        ('F5', 'Derep, antigo DETAQ', 'Derep (antigo DETAQ)', 'F5'),
        ('E12', 'não mede pontuação nem locutor',
         'no cálculo usual, sobre texto normalizado, não mede pontuação nem capitalização; locutor fica fora do WER em qualquer convenção', 'cons'),
    ],
    'L1C': [
        ('E1', 'o áudio não entra como modalidade do próprio LLM.',
         "reforço por LLM não implica, por si, que o áudio entre como modalidade do próprio LLM; o nexo 'por esse motivo' é falso.", 'cons'),
        ('E3', 'end-to-end, em regra não há dicionário de pronúncias separado',
         'end-to-end, não há dicionário de pronúncias separado', 'cons'),
    ],
    'L2': [
        ('E1a-curso', 'software que converte as notas da máquina estenotípica em texto por meio de dicionário, em tempo real ou não, com edição posterior [V 08/10/2026 — F7]',
         'software que traduz as notas da máquina estenotípica em texto [V 08/10/2026 — F7]', 'cons'),
        ('E1b-resumo', 'converte as notas estenotípicas em texto por dicionário, em tempo real ou não, com edição posterior [V 08/10/2026]',
         'traduz as notas estenotípicas em texto [V 08/10/2026 — F7]', 'cons'),
        ('E1c-par15', '(converte as notas estenotípicas em texto, com edição posterior)',
         '(traduz as notas estenotípicas em texto)', 'cons'),
        ('E1d-dgQ21', 'converte as notas estenotípicas em texto, com edição posterior [F7]',
         'traduz as notas estenotípicas em texto [F7]', 'cons'),
        ('E2', 'A lista pode mudar; nenhum item depende dela.',
         'A lista pode mudar; nenhum item depende dela. Lista variável conforme a consulta à página (08/10/2026).', 'cons-add'),
        ('E3b', 'NÃO foi verificada (N1)', 'foi observada nas notas oficiais de 2026 (N1)', 'cons'),
        ('E5', 'o Presidente interrompe para advertir sobre o tempo.',
         "o Presidente interrompe para advertir sobre o tempo. Aparte: interrupção breve e oportuna do orador, por outro Deputado que obtém sua permissão (RICD, art. 176, caput e § 1º) [V 08/10/2026 — Legin]. O registro taquigráfico do aparte é a regra; o não apanhamento depende de determinação do Presidente (RICD, art. 17, I, 'h').", 'cons-add'),
        ('E6', 'O aparte é a intervenção de OUTRO parlamentar no discurso de quem tem a palavra',
         'O aparte é a intervenção de OUTRO parlamentar no discurso de quem tem a palavra (RICD, art. 176: interrupção do orador por outro Deputado, com a permissão do orador)', 'cons-add'),
        ('E7', 'Convenção exata da Câmara: NÃO VERIFICADA.',
         'Forma de identificar o orador: observada nas notas oficiais de 2026 (N1; E3). Convenção da Câmara para marcação de pausas e eventos não falados e para grafia: NÃO VERIFICADA (N2).', 'cons'),
    ],
    'L3': [
        ('E1a', 'O § 3º, incluído pela Lei 13.853/2019, foi vetado (mensagem de veto VEP nº 288/2019, conferida pela CQFP).',
         'O § 3º, incluído pela Lei 13.853/2019, consta como vetado na página compilada, com remissão à VEP nº 288/2019; o conteúdo do veto não foi conferido.', 'cons'),
        ('E1b', 'art. 20: a redação original exigia revisão "por pessoa natural" e a Lei 13.853/2019 suprimiu a expressão (§ 3º vetado, VEP nº 288/2019);',
         'art. 20: a redação original exigia revisão "por pessoa natural", expressão suprimida (MP nº 869/2018, convertida na Lei 13.853/2019); o § 3º foi vetado;', 'cons'),
        ('E2', 'o art. 5º, II, enumera, entre outros, origem', 'o art. 5º, II, enumera origem', 'cons'),
        ('E3a', 'e a Lei 13.853/2019 suprimiu a expressão', 'e a MP nº 869/2018, convertida na Lei 13.853/2019, suprimiu a expressão', 'cons'),
        ('E3b', 'a Lei 13.853/2019 suprimiu a expressão da redação original',
         'a MP nº 869/2018, convertida na Lei 13.853/2019, suprimiu a expressão da redação original', 'cons'),
        ('E4', '(redação original, suprimida pela Lei 13.853/2019)',
         '(redação original, suprimida pela MP nº 869/2018, convertida na Lei 13.853/2019)', 'cons'),
    ],
}

# Erratas cujo alvo está FORA do texto exportado (cabeçalho/tabela de correções, limites de evidência, nota de produção,
# texto do próprio adendo): registradas no relatório; o script confirma que o alvo existe no arquivo e que X/Y não vão ao JSON.
NAO_EXPORTADAS = [
    dict(lote='L1', id='E6', onde='(d-G), nota de produção final do arquivo (contagens e risco), não é justificativa de item',
         x='risco ALTO: Q16 (nome de parâmetro e fluxo de API); demais: risco baixo/médio', arquivo='saida/gce/GCE_Lote1_v2_CPP.md'),
    dict(lote='L1', id='E11', onde='texto do "Motivo" do Adendo (E7/E8) na própria consolidação; nada do Adendo é exportado',
         x='Os tópicos de conteúdo somam 14,30 (6,00 + 7,00 + 1,30).', y='Na Questão 1 do caderno oficial, os tópicos de conteúdo somam 14,30'),
    dict(lote='L1C', id='E2', onde='Tabela de correções do cabeçalho do arquivo (linha N2); cabeçalho não é exportado',
         x='N2 → (d-G), justificativas reduzidas a duas linhas (Q21 a Q30), em', arquivo='saida/gce/GCE_Lote1C_v2_CPP.md'),
    dict(lote='L1C', id='E4', onde='lista de fontes da seção de evidência (acréscimo sem texto-âncora); evidência não é exportada',
         x=None, arquivo='saida/gce/GCE_Lote1C_v2_CPP.md'),
    dict(lote='L2', id='E3a', onde='Limites de evidência, nota N1 (cabeçalho); não é exportado',
         x='NÃO localizei fonte oficial pública da Câmara com a convenção.', arquivo='saida/gce/GCE_Lote2_v2_CPP.md'),
    dict(lote='L2', id='E4', onde='regra geral de denominação (DETAQ → Derep (antigo DETAQ)); verificada por varredura do JSON',
         x=None, arquivo='saida/gce/GCE_Lote2_v2_CPP.md'),
]

LOTES = [
    dict(id='L1', file='saida/gce/GCE_Lote1_v2_CPP.md', nome='Lote 1 — RF-ASR (reconhecimento de fala e transcrição, P2 1.1–1.8)',
         cargo='Lote 1', idrx=r'Q\d\d', prefix='L1-', reg='Lote 1'),
    dict(id='L1C', file='saida/gce/GCE_Lote1C_v2_CPP.md', nome='Lote 1-C — RF-ASR, complemento (P2 1.1–1.5)',
         cargo='Lote 1-C', idrx=r'Q\d\d', prefix='L1C-', reg='Lote 1-C'),
    dict(id='L2', file='saida/gce/GCE_Lote2_v2_CPP.md', nome='Lote 2 — RF-DEGRAVACAO (degravação e pós-processamento, P2 2.1–2.8)',
         cargo='Lote 2', idrx=r'Q\d\d', prefix='L2-', reg='Lote 2'),
    dict(id='L3', file='saida/gce/GCE_Lote3_v2_CPP.md', nome='Lote 3 — RF-IA-PARLAMENTAR + RF-PROTECAO (P2 3.1–4.3)',
         cargo='Lote 3', idrx=r'Q\d\d', prefix='L3-', reg='Lote 3'),
]


def split_dg_p2(txt):
    """Retorna (gab, ts, volatil, sub, justificativa) do texto do gabarito comentado (P2)."""
    m = re.match(r'^([CE])(\s*\[TS\])?\s*(?:—\s*(?:convertido|novo|VOLÁTIL)[^.]*?\)\s*\.|\.)?\s*(.*)$', txt)
    # formatos: "E — convertido (era C). texto"; "C — VOLÁTIL (verificado em ...). texto"; "E [TS]. texto"; "C — 1.1. texto"
    m2 = re.match(r'^([CE])(\s*\[TS\])?\s*—\s*(\d\.\d)\.\s*(.*)$', txt)
    if m2:
        return m2.group(1), bool(m2.group(2)), False, m2.group(3), m2.group(4)
    m3 = re.match(r'^([CE])(\s*\[TS\])?\s*(?:—\s*(convertido|novo|VOLÁTIL)\s*\([^)]*\)\s*)?\.\s*(.*)$', txt)
    if m3:
        return m3.group(1), bool(m3.group(2)), (m3.group(3) == 'VOLÁTIL'), None, m3.group(4)
    raise SystemExit('formato d-G P2 não reconhecido: ' + txt[:80])


def quesitos_from(text):
    """Extrai quesitos e conceitos de um texto de padrão (linhas)."""
    lines = text.split('\n')
    idxs = [i for i, l in enumerate(lines) if re.match(r'^\s*Quesito \d+\.\d+ — ', l)]
    res = []
    stop_rx = re.compile(r'^(Base normativa|Nota \(edital|Nota de correção|========== |PADRÃO DE RESPOSTA|Gênero da peça|FIM DOS PADRÕES|PONTOS PARA|ERRATA|Decisão da GCE|=====)')
    for k, i in enumerate(idxs):
        j = i + 1
        end = idxs[k + 1] if k + 1 < len(idxs) else len(lines)
        blk = [lines[i]]
        while j < end:
            if stop_rx.match(lines[j].strip()) and lines[j].strip() and not lines[j].startswith('Decisão'):
                break
            blk.append(lines[j])
            j += 1
        flat = unwrap(' '.join(blk))
        m = re.match(r'^Quesito (\d+\.\d+) — (.*?)\s*\[valor[^\]]*\]\s*(.*)$', flat)
        if not m:
            raise SystemExit('quesito não parseado: ' + flat[:100])
        qid, nome, rest = m.group(1), m.group(2).strip(), m.group(3)
        marks = list(re.finditer(r'(?:^|\s)(?:-\s*)?(Conceito \d+(?: a \d+)?\s*[—:])', rest))
        conc = []
        for a, mk in enumerate(marks):
            s = mk.start(1)
            e = marks[a + 1].start(1) if a + 1 < len(marks) else len(rest)
            piece = rest[s:e].strip()
            if a + 1 == len(marks):
                piece = re.split(r'\s+(?=Anula(?:m)?\s|Decisão da GCE|\(A menção|Normalização de números|Conceito 0 também)', piece)[0]
            piece = re.sub(r'\s+-$', '', piece.rstrip())
            conc.append(piece)
        # "Conceito 0 também quando ..." (L2 peça 2.3) faz parte do mesmo quesito: acrescenta
        extra = re.findall(r'(Conceito 0 também quando[^.]*\.)', rest)
        res.append(dict(id=qid, nome=nome, conceitos=conc + extra))
    return res


def enunciado_parts(sec_lines, skip_prefix='Rótulo:'):
    """Converte o bloco (e)/(f) do v2 em lista de linhas lógicas (parágrafos e alíneas)."""
    L = trim_blank(sec_lines)
    # descarta o parágrafo inicial 'Rótulo: ...'
    i = 0
    while i < len(L) and L[i].startswith(skip_prefix) is False and L[i].strip():
        break
    k = 0
    if L[0].startswith(skip_prefix):
        while k < len(L) and L[k].strip():
            k += 1
    L = trim_blank(L[k:])
    logical = []
    cur = None
    for l in L:
        if not l.strip():
            if cur is not None:
                logical.append(cur)
                cur = None
            continue
        if re.match(r'^\s+([a-c]\)|\d )', l):
            if cur is not None:
                logical.append(cur)
            cur = l.strip()
        else:
            if cur is None:
                cur = l.strip()
            elif re.match(r'^([a-c]\)|\d )', cur) and cur.endswith('pontos]') and not l.startswith(' '):
                logical.append(cur)
                cur = l.strip()
            else:
                cur += ' ' + l.strip()
    if cur is not None:
        logical.append(cur)
    return logical


def aspectos_from(logical, add_valor=None):
    asp = []
    for t in logical:
        m = re.match(r'^([a-c]\)|\d)\s+(.*)$', t)
        if not m:
            continue
        txt = m.group(2)
        mv = re.search(r'\s*\[valor:\s*([\d.,]+)\s*pontos\]\s*$', txt)
        valor = None
        if mv:
            valor = PT_NUM(mv.group(1))
            txt = txt[:mv.start()].rstrip()
        asp.append(dict(n=len(asp) + 1, texto=txt, valor=valor))
    return asp


def build_lote_p2(spec):
    lid = spec['id']
    lines = load(spec['file'], lid, ERRATA.get(lid, []))
    if lid == 'L3':
        lines = adendo2_l3(lines)
    S = sections(lines)
    out = dict(id=lid, nome=spec['nome'], prova='P2')
    # curso
    if 'a' in S:
        curso = curso_md(lines[S['a'][0]:S['a'][1]])
        out['curso'] = curso
        peg = pegadinhas_from_curso(curso.split('\n'))
    else:
        # Lote 1-C: adendo ao curso do 1.4 + pegadinhas adicionais
        i0 = find_idx(lines, lambda l: l.startswith('(a) ADENDO AO CURSO'))
        a0 = i0 + 2
        a1 = find_idx(lines, lambda l: l.startswith('=====') , a0)
        # (d) delimita
        d_idx = find_idx(lines, lambda l: l.startswith('(d) VERSÃO'))
        sec = lines[a0:d_idx - 1]
        curso_txt = '\n'.join(trim_blank(sec))
        out['curso'] = curso_txt
        peg = []
        for blk in re.finditer(r'PEGADINHAS ADICIONAIS\n(.*?)(?:\n\n|\Z)', curso_txt, re.S):
            peg.append({'item': '1.4', 'texto': unwrap(blk.group(1))})
    out['resumo'] = text_block(lines[S['b'][0]:S['b'][1]]) if 'b' in S else ''
    out['pares'] = pares_p2(lines[S['c'][0]:S['c'][1]]) if 'c' in S else []
    for p in peg:
        if p['item'] is None:
            assert lid == 'L1C'
            p['item'] = '1.4'
    from peg import fragments, PEG_INFO
    from edital_p import build_edital
    EID = {e['id']: e['texto'] for e in build_edital()}
    pegs = []
    for p in peg:
        ie = 'P2-' + p['item']
        rot = EID[ie]                      # pegadinha direto sob o item do edital: rótulo = texto do subitem no edital
        modo, frs = fragments(p['texto'])
        for f in frs:
            pegs.append(dict(itemEdital=ie, rotulo=rot, texto=f))
        PEG_INFO.append(dict(lote=lid, itemEdital=ie, rotulo=rot, origem='edital', modo=modo, n=len(frs), orig=p['texto']))
    out['pegadinhas'] = pegs
    # itens
    dsec = lines[S['d'][0]:S['d'][1]] if 'd' in S else None
    if dsec is None:
        di = find_idx(lines, lambda l: l.startswith('(d) VERSÃO'))
        dgi = find_idx(lines, lambda l: l.startswith('(d-G)'))
        dsec = lines[di + 2:dgi - 1]
        S['d'] = (di + 2, dgi - 1)
        S['dg'] = (dgi + 2, None)
    pre, items = parse_items(dsec, spec['idrx'])
    comando = pre[0] if pre else ''
    if 'dg' in S and S['dg'][1] is None:
        dgi = S['dg'][0]
        tab = find_idx(lines, lambda l: l.startswith('TABELA DE COBERTURA'), dgi)
        dg = parse_dg(lines[dgi:tab], spec['idrx'])
    else:
        nxt = [v[0] - 2 for k, v in S.items() if k in ('e', 'f')]
        tab = find_idx(lines, lambda l: l.startswith('TABELA DE COBERTURA'), S['dg'][0])
        dg = parse_dg(lines[S['dg'][0]:tab if tab != -1 else S['dg'][1]], spec['idrx'])
    reg = REG[spec['reg']]
    its = []
    for iid, txt in items:
        gab, ts, vol, sub, just = split_dg_p2(dg[iid])
        r = reg[iid_to_reg(spec, iid)]
        # confere com o registro GBQ v2
        assert r['gab'] == gab, (iid, r, gab)
        assert (r['ts'] == ts), (iid, 'TS', r['ts'], ts)
        if sub is not None:
            assert r['sub'] == sub, (iid, r['sub'], sub)
        # VOLÁTIL: registro GBQ v2 é a referência (marca 'VOLÁTIL' na coluna Marca)
        volreg = 'VOLÁTIL' in r['marca'] and 'REVERIF' not in r['marca']
        assert volreg == vol or (not vol and not volreg), (iid, volreg, vol)
        reverif = 'REVERIF' in r['marca']   # R1-N: mesmo tratamento de VOLÁTIL (contrato v1.1, regra 1)
        its.append(dict(local=iid, regid=iid_to_reg(spec, iid), enunciado=txt, gabarito=gab, justificativa=just,
                        sub=r['sub'], volatil=(volreg or reverif), comando=comando, numero=int(re.sub(r'\D', '', iid)), marca=r['marca'], ts=ts))
    out['_items'] = its
    out['itensEdital'] = sorted({'P2-' + i['sub'] for i in its}, key=lambda s: [int(x) for x in s[3:].split('.')])
    out['_S'] = S
    out['_lines'] = lines
    return out


def adendo2_l3(lines):
    """Adendo 2 da consolidação do Lote 3 (Ato da Mesa nº 225/2025): 'Contexto institucional' ao final dos itens 3.1 e 4.1.
    3.1: o bloco 'CONTEXTO NORMATIVO INTERNO (SEM ITEM)' (T-08/T-44) já cobre o Ato 225 -> não duplicar.
    4.1: insere o texto literal do Adendo 2 se ainda não houver 'Contexto institucional — Ato da Mesa nº 225'."""
    cons = read('saida/gce/GCE_Lote3_consolidacao_GCE.md').split('\n')
    i0 = find_idx(cons, lambda l: l.startswith('"Contexto institucional — Ato da Mesa nº 225'))
    assert i0 > 0
    j = i0
    while not cons[j].rstrip().endswith('sem item."'):
        j += 1
    par = cons[i0:j + 1]
    par[0] = par[0][1:]
    par[-1] = par[-1].rstrip()[:-1]
    ADENDO2['texto'] = '\n'.join(par)
    txt = '\n'.join(lines)
    i31 = find_idx(lines, lambda l: l.startswith('--- 3.1 '))
    i32 = find_idx(lines, lambda l: l.startswith('--- 3.2 '))
    blk31 = '\n'.join(lines[i31:i32])
    cobre = ('CONTEXTO NORMATIVO INTERNO (SEM ITEM)' in blk31 and 'Ato da Mesa nº 225, de 15/12/2025' in blk31
             and 'comitê de ética de uso da IA' in blk31 and 'art. 3º' in blk31)
    ERRATA_LOG.append(dict(lote='L3', id='Adendo 2 (3.1)', x=0, y=0, x_free=0, y_free=0,
                           estado='JÁ PRESENTE' if cobre else 'FALHA',
                           note='bloco "CONTEXTO NORMATIVO INTERNO (SEM ITEM)" (T-08/T-44) já cobre o Ato nº 225/2025 no 3.1 (art. 3º, I, III, V, VIII, IX; art. 4º, IV): NÃO duplicado'))
    assert cobre, 'bloco do 3.1 não cobre o Ato 225'
    i41 = find_idx(lines, lambda l: l.startswith('--- 4.1 '))
    i42 = find_idx(lines, lambda l: l.startswith('--- 4.2 '))
    blk41 = '\n'.join(lines[i41:i42])
    if 'Contexto institucional — Ato da Mesa nº 225' in blk41 or 'Ato da Mesa nº 225' in blk41:
        ERRATA_LOG.append(dict(lote='L3', id='Adendo 2 (4.1)', x=0, y=0, x_free=0, y_free=0, estado='JÁ PRESENTE',
                               note='equivalente já presente no 4.1'))
        return lines
    ERRATA_LOG.append(dict(lote='L3', id='Adendo 2 (4.1)', x=0, y=1, x_free=0, y_free=1, estado='APLICADA',
                           note='texto literal do Adendo 2 inserido ao final do item 4.1 (antes de "--- 4.2")'))
    return lines[:i42] + par + [''] + lines[i42:]


ADENDO2 = {}


def iid_to_reg(spec, iid):
    """id local (Qnn) -> id do registro GBQ (L1-Qnn etc.)."""
    return spec['prefix'] + iid


def discursivas_p2(lotes):
    """D1..D5 a partir dos padrões reconciliados."""
    res = []
    # --- D1: Lote 1 (consolidação, Parte B + adendo E7/E8)
    cons = read('saida/gce/GCE_Lote1_consolidacao_GCE.md').split('\n')
    cons = fix_hyphen_wraps(cons, 'cons1')
    i0 = find_idx(cons, lambda l: l.startswith('PADRÃO DE RESPOSTA'))
    i1 = find_idx(cons, lambda l: l.startswith('FIM DA CONSOLIDAÇÃO GCE — LOTE 1'))
    ptxt = '\n'.join(cons[i0:i1]).rstrip()
    ptxt = apply_errata(ptxt, 'L1', 'E7a', '[valor máximo: 6,00]', '[valor máximo: 5,30]')
    ptxt = apply_errata(ptxt, 'L1', 'E7b', 'Os valores máximos por quesito (5 / 4 / 6)',
                        'Os valores máximos por quesito (5,00 / 4,00 / 5,30), mais 0,70 de apresentação')
    # E7: "Fica acrescida a linha: Apresentação e estrutura textual: 0,70" — inserida antes de 'Base normativa'
    ptxt = ptxt.replace('Base normativa: não se aplica', 'Apresentação e estrutura textual: 0,70\n\nBase normativa: não se aplica', 1)
    assert 'Apresentação e estrutura textual: 0,70' in ptxt
    lotes_by = {l['id']: l for l in lotes}
    L1 = lotes_by['L1']
    S = L1['_S']
    esec = L1['_lines'][S['e'][0]:S['e'][1]]
    logical = enunciado_parts(esec)
    # E8: valores e preâmbulo
    vals = ['5,00', '4,00', '5,30']
    k = 0
    for ii, t in enumerate(logical):
        if re.match(r'^[a-c]\)', t):
            logical[ii] = t + ' [valor: %s pontos]' % vals[k]
            k += 1
    assert k == 3
    pre = 'Ao domínio do conteúdo serão atribuídos até 15,00 pontos, dos quais até 0,70 ponto à apresentação e estrutura textual.'
    cmd = '\n'.join([pre] + logical)
    res.append(dict(id='D1', tipo='questao', comando=cmd, aspectos=aspectos_from(logical), padrao=ptxt,
                    quesitos=quesitos_from(ptxt), _src='saida/gce/GCE_Lote1_consolidacao_GCE.md (Parte B + adendo E7/E8) + GCE_Lote1_v2_CPP.md (e)'))
    # --- D2/D3: Lote 2 (padrões)
    pad = read('saida/gce/GCE_Lote2_padroes_GCE.md').split('\n')
    pad = fix_hyphen_wraps(pad, 'pad2')
    ie = find_idx(pad, lambda l: l.startswith('========== (e)'))
    ifp = find_idx(pad, lambda l: l.startswith('========== (f)'))
    iend = find_idx(pad, lambda l: l.startswith('FIM DOS PADRÕES'))
    pre2 = '\n'.join(trim_blank(pad[1:ie]))      # após o título: origem, valores, base normativa
    pre2 = pre2.split('\n', 1)[1] if pre2.startswith('GCE, 08/10/2026') else pre2   # linha de identificação interna
    p_e = '\n'.join(trim_blank(pad[ie + 1:ifp]))
    # (f): o cabeçalho '(f) PEÇA — ...' quebra em 2 linhas
    p_f = '\n'.join(trim_blank(pad[ifp + 2:iend]))
    L2 = lotes_by['L2']
    S2 = L2['_S']
    lg_e = enunciado_parts(L2['_lines'][S2['e'][0]:S2['e'][1]])
    lg_f = enunciado_parts(L2['_lines'][S2['f'][0]:S2['f'][1]])
    # na peça, o parágrafo 'Gênero parecer técnico...' do Rótulo é descartado (skip_prefix); mantém texto do enunciado
    res.append(dict(id='D2', tipo='questao', comando='\n'.join(lg_e), aspectos=aspectos_from(lg_e),
                    padrao=pre2 + '\n\n' + p_e, quesitos=quesitos_from(p_e),
                    _src='saida/gce/GCE_Lote2_padroes_GCE.md (e) + GCE_Lote2_v2_CPP.md (e)'))
    res.append(dict(id='D3', tipo='peca', comando='\n'.join(lg_f), aspectos=aspectos_from(lg_f),
                    padrao=pre2 + '\n\n' + p_f, quesitos=quesitos_from(p_f),
                    _src='saida/gce/GCE_Lote2_padroes_GCE.md (f) + GCE_Lote2_v2_CPP.md (f)'))
    # --- D4/D5: Lote 3 (padrões)
    pad3 = read('saida/gce/GCE_Lote3_padroes_GCE.md').split('\n')
    ie = find_idx(pad3, lambda l: l.startswith('(e) DISCURSIVA'))
    ifp = find_idx(pad3, lambda l: l.startswith('(f) PEÇA TÉCNICA'))
    ipt = find_idx(pad3, lambda l: l.startswith('PONTOS PARA A RECONCILIAÇÃO'))
    p3e = '\n'.join(trim_blank(pad3[ie + 2:ifp - 1]))
    p3f = '\n'.join(trim_blank(pad3[ifp + 2:ipt]))
    r6 = ('Os aspectos enumerados valem como padrão de resposta, com as bases normativas indicadas em cada um. '
          'Nota: NQ = NC − 3 × NE ÷ TL. O peso de cada quesito é HIPÓTESE do Projeto, alinhada à soma oficial.')
    # T-27 (3): anexo literal das Notas R2-R4 (D1 GBQ, pacote_reconciliacao_2026-10-10.md, seção 2(e))
    i2 = find_idx(pad3, lambda l: l.startswith('R2. '))
    i5 = find_idx(pad3, lambda l: l.startswith('R5. '))
    assert 0 < i2 < i5 < 30, (i2, i5)
    notas = '\n'.join(l.rstrip() for l in pad3[i2:i5])
    assert notas.startswith('R2. Alínea c') and 'R3. Voz como dado sensível' in notas and notas.rstrip().endswith('o art. 7º, II ou III.')
    anexo = '\n\nNotas de correção (GCE, R2–R4)\n' + notas
    L3 = lotes_by['L3']
    S3 = L3['_S']
    lg3e = enunciado_parts(L3['_lines'][S3['e'][0]:S3['e'][1]])
    lg3f = enunciado_parts(L3['_lines'][S3['f'][0]:S3['f'][1]])
    # remove 'Fundador: ...' residual se houver
    res.append(dict(id='D4', tipo='questao', comando='\n'.join(lg3e), aspectos=aspectos_from(lg3e),
                    padrao=p3e + '\n\n' + r6 + anexo, quesitos=quesitos_from(p3e),
                    _src='saida/gce/GCE_Lote3_padroes_GCE.md (e) + GCE_Lote3_v2_CPP.md (e)'))
    res.append(dict(id='D5', tipo='peca', comando='\n'.join(lg3f), aspectos=aspectos_from(lg3f),
                    padrao=p3f + '\n\n' + r6 + anexo, quesitos=quesitos_from(p3f),
                    _src='saida/gce/GCE_Lote3_padroes_GCE.md (f) + GCE_Lote3_v2_CPP.md (f)'))
    return res
