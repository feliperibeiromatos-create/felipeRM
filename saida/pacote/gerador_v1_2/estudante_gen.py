# -*- coding: utf-8 -*-
"""T-48 — gera a edição do estudante (saida/estudante/) a partir de out/pacote.json (fonte única).
Marcas internas removidas SOMENTE por deleção (estudante_marcas.strip_text). Saída em out/estudante/."""
import json, os, re, sys, shutil, collections
import estudante_marcas as em

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'out', 'pacote.json')
OUT = os.path.join(HERE, 'out', 'estudante')
AVISO = 'Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027.'
MARK_RX = re.compile(r'\[V\s|NORMATIVO — QA|\[TS\]|\bF\d{1,2}\b|\b(?:CQFP|CQE|CPP|GCE|GCB|GBQ|EXEC)\b')

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
    def S(self, nome, text):
        """texto com marcas removidas por deleção (contabiliza no arquivo)."""
        return em.strip_text(text, self.cnt[nome], nome)
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
    ver = 'v1.2'
    data = pacote['geradoEm']

    # ------------------------------------------------------------ lotes
    for L in pacote['lotes']:
        lid = L['id']
        f_est, f_it, f_gab = f'{lid}_estudo.md', f'{lid}_itens.md', f'{lid}_gabarito.md'
        S = lambda t, f=f_est: W.S(f, t)
        W.add(f_est, f'# {S(L["nome"])}', '', f'Prova: {L["prova"]}', '', '## Itens do edital', '')
        for e in L['itensEdital']:
            W.add(f_est, f'- {e} — {edital[e]}')
        W.add(f_est, '', '## Resumo', '', fence(S(L['resumo'])), '', '## Curso', '', fence(S(L['curso'])), '', '## Pares', '')
        if L['pares']:
            for p in L['pares']:
                for k in ('a', 'b', 'como'):
                    assert '\n' not in p[k]
                # R1 / C-24: sem ' × **…**' quando b é vazio e sem ' — ' pendurado quando como é vazio (só formatação)
                linha = f'- **{S(p["a"])}**'
                if p['b']:
                    linha += f' × **{S(p["b"])}**'
                if p['como']:
                    linha += f' — {S(p["como"])}'
                W.add(f_est, linha)
        else:
            W.add(f_est, '_Nenhum par neste lote._')
        W.add(f_est, '', '## Pegadinhas', '')
        if L['pegadinhas']:
            for g in L['pegadinhas']:
                assert '\n' not in g['texto'] and '\n' not in g['rotulo']
                W.add(f_est, f'- [{g["itemEdital"]}] **{S(g["rotulo"])}** — {S(g["texto"])}')
        else:
            W.add(f_est, '_Nenhuma pegadinha registrada neste lote._')
        W.add(f_est, '')

        its = [i for i in pacote['itens'] if i['rotulo'] == 'AUTORAL' and lote_of(i['id']) == lid]
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
        for it in its:
            W.add(f_gab, f'### {it["id"]} — Gabarito: {it["gabarito"]}', '',
                  f'- Item do edital: {it["itemEdital"]}')
            if it['justificativa']:
                assert '\n' not in it['justificativa']
                W.add(f_gab, f'- Justificativa: {W.S(f_gab, it["justificativa"])}')
            if it.get('nota'):
                W.add(f_gab, f'- Nota: {W.nota(f_gab, it["nota"])}')
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
            W.add(fb, f'> Nota: {W.nota(fb, it["nota"])}', '')
        if it.get('volatil') or it.get('nota'):
            W.add(fb, '')
        W.add(fbg, f'### {it["id"]} — Gabarito: {it["gabarito"]}', '',
              f'- Item do edital: {it["itemEdital"]} (aderência: {it["aderencia"]})')
        if it.get('nota'):
            W.add(fbg, f'- Nota: {W.nota(fbg, it["nota"])}')
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
                W.add(ff, f'> Nota: {W.nota(ff, it["nota"])}', '')
            if it.get('volatil') or it.get('nota'):
                W.add(ff, '')
            W.add(fg, f'### {n} — {it["id"]} — Gabarito: {it["gabarito"]}', '',
                  f'- Item do edital: {it["itemEdital"]} (aderência: {it["aderencia"]})')
            if it['justificativa']:
                W.add(fg, f'- Justificativa: {W.S(fg, it["justificativa"])}')
            if it.get('nota'):
                W.add(fg, f'- Nota: {W.nota(fg, it["nota"])}')
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
    for L in pacote['lotes']:
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
    m = {'L1': 'L1', 'L1C': 'L1C', 'L2': 'L2', 'L3': 'L3', 'L4': 'L4', '4C': 'L4C', 'A5': 'L5', '5C': 'L5C', '6A': 'L6A', '6B': 'L6B'}
    return m[item_id.split('-')[0]]

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
    json.dump({'por_arquivo': {k: dict(v) for k, v in W.cnt.items() if v}, 'total': dict(tot)},
              open(os.path.join(HERE, 'out', 'estudante_contagem.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(W.files), 'arquivos;', sum(tot.values()), 'remoções')
    for k, v in tot.most_common(): print(v, k)
