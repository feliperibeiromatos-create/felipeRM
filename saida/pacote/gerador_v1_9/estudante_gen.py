# -*- coding: utf-8 -*-
"""T-81 (v1.8; evolução do gerador v1.7/T-71, v1.6/T-67, v1.5/T-61, v1.4/T-57, v1.3/T-56 e T-48) — gera a edição do estudante (saida/estudante/) a partir de out/pacote.json (fonte única).
Marcas internas removidas SOMENTE por deleção (estudante_marcas.strip_text). Saída em out/estudante/.
T-81 / D1 da GBQ (T81_D1_escopo_v1_8, 3.2): os complementos 1-C, 4-C e 5-C são fundidos nos Lotes 1, 4 e 5 (34 arquivos, contra 43); o escopo das deleções continua o nome de
arquivo de ORIGEM da v1.7 (L1C_estudo.md, L1C_gabarito.md etc.)."""
import json, os, re, sys, shutil, collections
import estudante_marcas as em

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'out', 'pacote.json')
OUT = os.path.join(HERE, 'out', 'estudante')
AVISO = 'Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.'
MARK_RX = re.compile(r'\[V\s|NORMATIVO — QA|\[TS\]|\bF\d{1,2}\b|\b(?:CQFP|CQE|CPP|GCE|GCB|GBQ|EXEC)\b')

# ---- fusão 1-C/4-C/5-C (T81_D1_escopo_v1_8, seção 3): só na camada do estudante
COMPL = {'L1': 'L1C', 'L4': 'L4C', 'L5': 'L5C'}      # lote principal -> complemento fundido
FUSAO = {v: k for k, v in COMPL.items()}               # complemento -> lote principal
SEP_COMPL = '\n\n## Complemento\n\n'                   # D-T12-V13 (c): a linha "## " é a que a plataforma usa para separar blocos de curso

def curso_fundido(curso, curso_c):
    """curso do lote principal + separador + curso do complemento; sem complemento (ou com o curso do complemento vazio: L4C e L5C), o curso do lote como está."""
    if not curso_c:
        return curso
    assert not any(l.startswith('## ') for l in curso_c.split('\n')), 'o curso do complemento tem linha que começa por "## "'
    return curso + SEP_COMPL + curso_c

def lotes_fund(pacote):
    """os lotes que geram arquivo na edição v1.8 (sem L1C, L4C e L5C), na ordem do pacote."""
    return [x for x in pacote['lotes'] if x['id'] not in FUSAO]

def fence(text):
    f = '```'
    while f in text:
        f += '`'
    return f + 'text\n' + text + ('\n' if text else '') + f

class Writer:
    def __init__(self):
        self.files = collections.OrderedDict()   # nome -> lista de linhas
        self.cnt = collections.defaultdict(collections.Counter)  # nome -> Counter(tipo)
    def add(self, nome, *lines):
        self.files.setdefault(nome, []).extend(lines)
    def S(self, nome, text, escopo=None):
        """texto com marcas removidas por deleção (contabiliza no arquivo `nome`; o escopo das regras é o nome de arquivo de origem v1.7 `escopo`, se dado)."""
        return em.strip_text(text, self.cnt[nome], escopo or nome)
    NOTA_DEL = ' (D-LEI-15352)'     # R1 / C-18: id de decisão entre parênteses sai só da EXIBIÇÃO da nota
    def nota(self, nome, text):
        n = text.count(self.NOTA_DEL)
        if n:
            assert n == 1, (nome, text)
            self.cnt[nome]['id de decisão na nota (D-LEI-15352)'] += 1
            return text.replace(self.NOTA_DEL, '')
        return text
    def raw(self, nome, text, what=''):
        """texto de prova/enunciado: não se mexe; confere que não há marca."""
        m = MARK_RX.search(text or '')
        assert not m, (nome, what, m.group(0), (text or '')[:120])
        return text

def blocks(items):
    """agrupa itens consecutivos com o mesmo (comando, textoBase)."""
    out = []
    for it in items:
        key = (it['comando'], it['textoBase'])
        if out and out[-1][0] == key:
            out[-1][1].append(it)
        else:
            out.append((key, [it]))
    return out

def valor_fmt(v):
    return ('%.2f' % v).replace('.', ',')

def build(pacote):
    W = Writer()
    itens = {i['id']: i for i in pacote['itens']}
    edital = {e['id']: e['texto'] for e in pacote['edital']}
    ver = 'v1.8'
    data = pacote['geradoEm']
    lotes_by_id = {x['id']: x for x in pacote['lotes']}

    # ------------------------------------------------------------ lotes (7 arquivos de lote; 1-C, 4-C e 5-C fundidos)
    for L in lotes_fund(pacote):
        lid = L['id']
        C = lotes_by_id[COMPL[lid]] if lid in COMPL else None      # complemento fundido neste lote (L1C, L4C, L5C) ou None
        f_est, f_it, f_gab = f'{lid}_estudo.md', f'{lid}_itens.md', f'{lid}_gabarito.md'
        S = lambda t, f=f_est: W.S(f, t)
        SC = lambda t, f=f_est, e=(COMPL[lid] + '_estudo.md' if lid in COMPL else None): W.S(f, t, e)      # texto do complemento: escopo do arquivo de origem v1.7
        W.add(f_est, f'# {S(L["nome"])}', '', f'Prova: {L["prova"]}', '', '## Itens do edital', '')
        for e in L['itensEdital']:
            W.add(f_est, f'- {e} — {edital[e]}')
        curso = curso_fundido(S(L['curso']), SC(C['curso']) if C else None)
        W.add(f_est, '', '## Resumo', '', fence(S(L['resumo'])), '', '## Curso', '', fence(curso), '', '## Pares', '')
        if C:      # o complemento não tem resumo nem pares (asserção da fusão)
            assert not C['resumo'] and not C['pares'], (C['id'])
        if L['pares']:
            for p in L['pares']:
                for k in ('a', 'b', 'como'):
                    assert '\n' not in p[k]
                # T-57 / contrato v1.2.2 ponto 2 (D-T54-01): separadores e pontuação do arquivo canônico do próprio lote (só formatação; as palavras não mudam)
                if 'id' in p:      # lotes GCB (L4, L5, L6A, L6B): "- id. **a** × **b** | como"
                    assert p['como'], (lid, p)
                    linha = f'- {p["id"]}. **{S(p["a"])}**'
                    if p['b']:
                        linha += f' × **{S(p["b"])}**'
                    linha += f' | {S(p["como"])}'
                else:              # lotes GCE (L1, L2, L3): "- **a** vs **b**: como"; com como vazio "- **a** vs **b**." (ponto final do canônico)
                    linha = f'- **{S(p["a"])}**'
                    if p['b']:
                        linha += f' vs **{S(p["b"])}**'
                    linha += f': {S(p["como"])}' if p['como'] else '.'
                W.add(f_est, linha)
        else:
            W.add(f_est, '_Nenhum par neste lote._')
        W.add(f_est, '', '## Pegadinhas', '')
        pegs = [(g, S) for g in L['pegadinhas']] + ([(g, SC) for g in C['pegadinhas']] if C else [])      # as do complemento entram depois, na ordem
        if pegs:
            for g, SS in pegs:
                assert '\n' not in g['texto'] and '\n' not in g['rotulo']
                W.add(f_est, f'- [{g["itemEdital"]}] **{SS(g["rotulo"])}** — {SS(g["texto"])}')
        else:
            W.add(f_est, '_Nenhuma pegadinha registrada neste lote._')
        W.add(f_est, '')

        its = [i for i in pacote['itens'] if i['rotulo'] == 'AUTORAL' and lote_fund(i['id']) == lid]      # na ordem do pacote: os do lote, depois os do complemento
        W.add(f_it, f'# {L["nome"]} — itens', '', 'Itens para julgar (C = certo, E = errado). Gabarito e justificativas no arquivo '
              f'{lid}_gabarito.md.', '')
        for (cmd, tb), grp in blocks(its):
            if tb:      # R1 / C-11: o texto-base vem antes do comando
                W.add(f_it, f'**Texto-base.** {W.raw(f_it, tb, "textoBase")}', '')
            W.add(f_it, f'**Comando.** {W.raw(f_it, cmd, "comando")}', '')
            for it in grp:
                W.add(f_it, f'**{it["id"]}** — {W.raw(f_it, it["enunciado"], it["id"])}', '')
                if it.get('volatil'):
                    W.add(f_it, f'> {AVISO}', '')
        W.add(f_gab, f'# {L["nome"]} — gabarito e justificativas', '')
        if L.get('legendaMecanismo'):      # v1.2.1 ponto 4 / D-T53-01: legenda literal do lote, só no topo do *_gabarito.md do lote (a do complemento não entra: D1 da T-81, 3.1)
            W.add(f_gab, L['legendaMecanismo'], '')
        for it in its:
            W.add(f_gab, f'### {it["id"]} — Gabarito: {it["gabarito"]}', '',
                  f'- Item do edital: {it["itemEdital"]}')
            if it['justificativa']:
                assert '\n' not in it['justificativa']
                # escopo das regras = arquivo de gabarito de ORIGEM na v1.7 (L1C_gabarito.md, L4C_gabarito.md, L5C_gabarito.md para os complementos)
                W.add(f_gab, f'- Justificativa: {W.S(f_gab, it["justificativa"], lote_of(it["id"]) + "_gabarito.md")}')
            if it.get('nota'):
                W.add(f_gab, f'- {W.nota(f_gab, it["nota"])}')      # T-57 (D-T54-04): sem o rótulo "Nota: " do gerador
            W.add(f_gab, '')
            if it.get('volatil'):
                W.add(f_gab, f'> {AVISO}', '')

    # ------------------------------------------------------------ banco
    bq = [i for i in pacote['itens'] if i['rotulo'] != 'AUTORAL']
    fb, fbg = 'BANCO_itens.md', 'BANCO_gabarito.md'
    W.add(fb, '# Banco de itens Cebraspe — itens (sem gabarito)', '',
          'Itens de provas anteriores (rótulo CEBRASPE_ANALOGA). Gabaritos no arquivo BANCO_gabarito.md.', '')
    W.add(fbg, '# Banco de itens Cebraspe — gabarito', '')
    for it in bq:
        W.add(fb, f'### {it["id"]}', '', f'- Certame: {it["certame"]}', f'- Cargo: {it["cargo"]}',
              f'- Ano: {it["ano"]}', f'- Número: {it["numero"]}', f'- URL oficial: {it["url"]}', '')
        if it['textoBase']:      # R1 / C-11: o texto-base vem antes do comando
            W.add(fb, f'**Texto-base.** {W.raw(fb, it["textoBase"], "textoBase")}', '')
        W.add(fb, f'**Comando.** {W.raw(fb, it["comando"], "comando")}', '')
        W.add(fb, f'**Enunciado.** {W.raw(fb, it["enunciado"], it["id"])}', '')
        if it.get('volatil'):
            W.add(fb, f'> {AVISO}', '')
        if it.get('nota'):
            W.add(fb, f'> {W.nota(fb, it["nota"])}', '')
        if it.get('volatil') or it.get('nota'):
            W.add(fb, '')
        W.add(fbg, f'### {it["id"]} — Gabarito: {it["gabarito"]}', '',
              f'- Item do edital: {it["itemEdital"]} (aderência: {it["aderencia"]})')
        if it.get('nota'):
            W.add(fbg, f'- {W.nota(fbg, it["nota"])}')
        W.add(fbg, '')
        if it.get('volatil'):
            W.add(fbg, f'> {AVISO}', '')

    # ------------------------------------------------------------ simulados
    for sim in pacote['simulados']:
        sid = sim['id']
        ff, fg = f'{sid}_folha.md', f'{sid}_gabarito.md'
        W.add(ff, f'# {sim["nome"]} — folha', '', f'- Tipo: {sim["tipo"]}', f'- Versão: {sim["versao"]}',
              f'- Número de itens: {sim["n"]}', '', 'Julgue cada item (C = certo, E = errado). Gabarito no arquivo '
              f'{sid}_gabarito.md.', '')
        W.add(fg, f'# {sim["nome"]} — gabarito', '', f'- Versão: {sim["versao"]}', f'- Número de itens: {sim["n"]}', '')
        # T-57 / contrato v1.2.2 ponto 4 (D-T54-07): legenda literal de cada lote de origem que a tenha, em linha própria, sem título; strings idênticas
        # uma só vez; ordem = a da lista `lotes`. Lote de origem = o lote em cujo *_gabarito.md o item é emitido (v1.8: o lote fundido); item de banco não tem.
        lotes_origem = {lote_fund(x) for x in sim['itens'] if itens[x]['rotulo'] == 'AUTORAL'}
        vistas = []
        for L in lotes_fund(pacote):
            if L['id'] in lotes_origem and L.get('legendaMecanismo') and L['legendaMecanismo'] not in vistas:
                vistas.append(L['legendaMecanismo'])
        for leg in vistas:
            W.add(fg, leg, '')
        its = [(n + 1, itens[x]) for n, x in enumerate(sim['itens'])]
        # blocos pela ordem do simulado
        cur = None
        for n, it in its:
            key = (it['comando'], it['textoBase'])
            if key != cur:
                if it['textoBase']:      # R1 / C-11: o texto-base vem antes do comando
                    W.add(ff, f'**Texto-base.** {W.raw(ff, it["textoBase"], "textoBase")}', '')
                W.add(ff, f'**Comando.** {W.raw(ff, it["comando"], "comando")}', '')
                cur = key
            # R1 / C-10: o id de origem não aparece na folha (fica só no *_gabarito.md)
            W.add(ff, f'**{n}** — {W.raw(ff, it["enunciado"], it["id"])}', '')
            if it.get('volatil'):
                W.add(ff, f'> {AVISO}', '')
            if it.get('nota'):
                W.add(ff, f'> {W.nota(ff, it["nota"])}', '')
            if it.get('volatil') or it.get('nota'):
                W.add(ff, '')
            W.add(fg, f'### {n} — {it["id"]} — Gabarito: {it["gabarito"]}', '',
                  f'- Item do edital: {it["itemEdital"]} (aderência: {it["aderencia"]})')
            if it['justificativa']:
                W.add(fg, f'- Justificativa: {W.S(fg, it["justificativa"])}')      # escopo = o nome do arquivo do simulado, como na v1.7
            if it.get('nota'):
                W.add(fg, f'- {W.nota(fg, it["nota"])}')
            W.add(fg, '')
            if it.get('volatil'):
                W.add(fg, f'> {AVISO}', '')

    # ------------------------------------------------------------ discursivas
    fd, fdp = 'DISCURSIVAS.md', 'DISCURSIVAS_padrao.md'
    W.add(fd, '# Discursivas — comandos', '', 'Hipóteses de questão discursiva e de peça técnica. Padrões de resposta no arquivo DISCURSIVAS_padrao.md.', '')
    W.add(fdp, '# Discursivas — padrões de resposta', '')
    tipos = {'questao': 'Questão', 'peca': 'Peça técnica'}
    for d in pacote['discursivas']:
        W.add(fd, f'## {d["id"]} — {tipos[d["tipo"]]}', '', fence(W.S(fd, d['comando'])), '')
        W.add(fdp, f'## {d["id"]} — {tipos[d["tipo"]]}', '', '### Padrão de resposta', '', fence(W.S(fdp, d['padrao'])), '',
              '### Aspectos (valor)', '')
        for a in d['aspectos']:
            assert '\n' not in a['texto']
            W.add(fdp, f'- ({a["n"]}) {W.S(fdp, a["texto"])} — valor: {valor_fmt(a["valor"])}')
        W.add(fdp, '', '### Quesitos', '')
        for q in d['quesitos']:
            assert '\n' not in q['nome']
            W.add(fdp, f'- **{q["id"]}** — {W.S(fdp, q["nome"])}')
            for c in q['conceitos']:
                assert '\n' not in c
                W.add(fdp, f'  - {W.S(fdp, c)}')
        W.add(fdp, '')

    # ------------------------------------------------------------ README
    r = ['# Câmara 2026 — Edição do estudante', '',
         f'- Versão: {ver} (pacote.json versão {pacote["versao"]})', f'- Data: {data}',
         '- Aviso: material de estudo; gabaritos em arquivo separado.',
         f'- Itens marcados com o aviso "{AVISO}" têm conteúdo volátil.', '',
         '## Arquivos', '', '### Por lote', '']
    for L in lotes_fund(pacote):
        r.append(f'- {L["id"]}: [{L["id"]}_estudo.md]({L["id"]}_estudo.md) (resumo, curso, pares, pegadinhas); '
                 f'[{L["id"]}_itens.md]({L["id"]}_itens.md) (itens sem gabarito); '
                 f'[{L["id"]}_gabarito.md]({L["id"]}_gabarito.md) (gabarito e justificativas)')
    r += ['', '### Banco de itens', '', '- [BANCO_itens.md](BANCO_itens.md) (itens sem gabarito)', '- [BANCO_gabarito.md](BANCO_gabarito.md) (gabarito)', '', '### Simulados', '']
    for s in pacote['simulados']:
        r.append(f'- {s["id"]} ({s["tipo"]}, {s["versao"]}, {s["n"]} itens): [{s["id"]}_folha.md]({s["id"]}_folha.md); [{s["id"]}_gabarito.md]({s["id"]}_gabarito.md)')
    r += ['', '### Discursivas', '', '- [DISCURSIVAS.md](DISCURSIVAS.md) (comandos)', '- [DISCURSIVAS_padrao.md](DISCURSIVAS_padrao.md) (padrões de resposta)', '']
    W.add('README.md', *r)
    return W

def lote_of(item_id):
    """lote de ORIGEM na v1.7 (prefixo do id): define o escopo das deleções (arquivo de origem)."""
    m = {'L1': 'L1', 'L1C': 'L1C', 'L2': 'L2', 'L3': 'L3', 'L4': 'L4', '4C': 'L4C', 'A5': 'L5', '5C': 'L5C', '6A': 'L6A', '6B': 'L6B'}
    return m[item_id.split('-')[0]]

def lote_fund(item_id):
    """lote da edição v1.8: o de origem, com L1C, L4C e L5C fundidos em L1, L4 e L5 (associação pelo prefixo: L1C- -> L1, 4C- -> L4, 5C- -> L5)."""
    l = lote_of(item_id)
    return FUSAO.get(l, l)

def write(W, out=OUT):
    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(out)
    for nome, lines in W.files.items():
        with open(os.path.join(out, nome), 'w', encoding='utf-8', newline='\n') as fh:
            fh.write('\n'.join(lines).rstrip('\n') + '\n')

if __name__ == '__main__':
    pac = json.load(open(SRC, encoding='utf-8'))
    W = build(pac)
    write(W)
    tot = collections.Counter()
    for nome, c in W.cnt.items():
        tot.update(c)
    # R1 / C-15: cada par da lista CAIXA deve ocorrer exatamente 1 vez
    for esc, antes, depois in em.CAIXA:
        assert em.CAIXA_HITS.get((esc, antes), 0) == 1, ('CAIXA', antes, em.CAIXA_HITS.get((esc, antes), 0))
    # T-57 / D-T54-02: cada uma das 2 linhas do quadro-síntese do L1 é realinhada exatamente 1 vez (só espaços; não é remoção)
    for esc, antes, depois in em.REALINHA:
        assert em.REALINHA_HITS.get((esc, antes), 0) == 1, ('REALINHA', antes, em.REALINHA_HITS.get((esc, antes), 0))
    json.dump({'por_arquivo': {k: dict(v) for k, v in W.cnt.items() if v}, 'total': dict(tot)},
              open(os.path.join(HERE, 'out', 'estudante_contagem.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(W.files), 'arquivos;', sum(tot.values()), 'remoções')
    for k, v in tot.most_common(): print(v, k)
