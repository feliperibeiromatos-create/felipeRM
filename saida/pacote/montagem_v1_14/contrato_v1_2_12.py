# contrato_v1_2_12.py — T-123 fase 2 (passo 5) — 2026-10-23 — gerado por gbq-csc
# -*- coding: utf-8 -*-
"""Aplica a errata de forma v1.2.12 (D1 da GBQ, saida/pacote/T123_D1_v1_14_2026-10-23.md, seção 7, C-1 a C-3) a regras/pacote_contrato.md e grava o registro saida/pacote/contrato_v1_2_12_2026-10-23.md.
O texto do bloco e da frase de C-2 é extraído da própria D1 (sem retranscrição). Aborta (exit 2) se o SHA-256 LF de entrada não for 85b30fcc…616b ou se alguma âncora não ocorrer exatamente 1 vez.
Preserva o fim de linha do arquivo em disco (CRLF na árvore de trabalho com core.autocrlf=true); o SHA-256 informado é o do conteúdo LF. Uso: python -I contrato_v1_2_12.py [--ensaio] (--ensaio não grava)."""
import sys
sys.dont_write_bytecode = True
import difflib, hashlib, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
CONTRATO = os.path.join(R, 'regras', 'pacote_contrato.md')
D1 = os.path.join(R, 'saida', 'pacote', 'T123_D1_v1_14_2026-10-23.md')
REG = os.path.join(R, 'saida', 'pacote', 'contrato_v1_2_12_2026-10-23.md')
SHA_ANTES = '85b30fccadce4eb9782e1e056613a2d680cec0c01aed44fd173bda7d248e616b'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def abort(m):
    sys.stderr.write('ABORTA: ' + m + '\n'); sys.exit(2)


def aplica():
    raw = open(CONTRATO, 'rb').read()
    crlf = b'\r\n' in raw
    lf = raw.replace(b'\r\n', b'\n')
    if sha(lf) != SHA_ANTES:
        abort('SHA-256 LF de regras/pacote_contrato.md: esperado %s, obtido %s' % (SHA_ANTES, sha(lf)))
    d1 = open(D1, 'rb').read().replace(b'\r\n', b'\n').decode('utf-8').split('\n')
    # bloco (C-3): da linha "> Errata de forma da v1.2.12 (" até "> 9. **Aplicação.**", sem o marcador de citação
    ini = [i for i, l in enumerate(d1) if l.startswith('> Errata de forma da v1.2.12 (')]
    fim = [i for i, l in enumerate(d1) if l.startswith('> 9. **Aplicação.**')]
    if len(ini) != 1 or len(fim) != 1 or fim[0] < ini[0]:
        abort('bloco da errata nao achado de forma unica na D1: %r %r' % (ini, fim))
    bloco = []
    for l in d1[ini[0]:fim[0] + 1]:
        bloco.append('' if l == '>' else l[2:] if l.startswith('> ') else abort('linha do bloco sem marcador de citacao: %r' % l[:60]))
    # frase de C-2
    c2 = [l for l in d1 if l.startswith('- **C-2.**')]
    if len(c2) != 1:
        abort('linha C-2 nao achada de forma unica na D1')
    m = re.search(r'acrescentar «( A v1\.2\.12 .*)»\s*$', c2[0])
    if not m:
        abort('frase de C-2 nao extraida da D1')
    frase = m.group(1)
    txt = lf.decode('utf-8')
    L = txt.split('\n')
    # C-1
    a1 = '(v1.2.11, 2026-10-20)'
    if L[0].count(a1) != 1 or txt.count(a1) != 1:
        abort('ancora C-1 nao ocorre exatamente 1 vez')
    # C-2
    a2 = 'ver a seção "Errata de forma da v1.2.11".'
    if L[2].count(a2) != 1 or not L[2].endswith(a2) or txt.count(a2) != 1:
        abort('ancora C-2 nao ocorre exatamente 1 vez no fim da linha 3')
    # C-3
    idx = [i for i, l in enumerate(L) if l.startswith('5. **Aplicação.** A partir da edição .md v1.13-E')]
    if len(idx) != 1:
        abort('ancora C-3 nao ocorre exatamente 1 vez')
    N = list(L)
    N[0] = L[0].replace(a1, '(v1.2.12, 2026-10-23)')
    N[2] = L[2] + frase
    N = N[:idx[0] + 1] + [''] + bloco + N[idx[0] + 1:]
    novo = '\n'.join(N)
    return raw, lf, novo, L, N, crlf, bloco, frase


def main():
    ensaio = '--ensaio' in sys.argv
    raw, lf, novo, L, N, crlf, bloco, frase = aplica()
    nb = novo.encode('utf-8')
    ops = [o for o in difflib.SequenceMatcher(None, L, N, autojunk=False).get_opcodes() if o[0] != 'equal']
    print('antes  %s %d bytes %d linhas' % (sha(lf), len(lf), lf.count(b'\n')))
    print('depois %s %d bytes %d linhas' % (sha(nb), len(nb), nb.count(b'\n')))
    print('opcodes', ops)
    if ensaio:
        return
    with open(CONTRATO, 'wb') as f:
        f.write(nb.replace(b'\n', b'\r\n') if crlf else nb)
    # --- registro
    r = []
    w = r.append
    w('# contrato_v1_2_12_2026-10-23.md — T-123 (D1 da GBQ, seção 7) — 2026-10-23 — gerado por gbq-csc')
    w('')
    w('REMETENTE: gbq-csc (passo 5 da instrução da D1, `saida/pacote/T123_D1_v1_14_2026-10-23.md`, seção 13; script `saida/pacote/montagem_v1_14/contrato_v1_2_12.py`, `python -I`).')
    w('DESTINATÁRIO: gbq-cqe (conferência da errata, seção 13, "Depois"); depois gbq-gerencia (reconciliação e gatilho A da v1.14). Sem commit (do orquestrador).')
    w('')
    w('## 1. Objeto')
    w('')
    w('Errata de forma de `regras/pacote_contrato.md`: v1.2.11 → **v1.2.12** (23/10/2026). Admite no pacote v1.14 os itens de reforço de DA e os itens de banco com `itemEdital` P1-DA, sem campo novo e sem mudar `versao` nem `versaoFormato`. O texto do bloco e da frase de C-2 foi extraído por script da própria D1 (seção 7), sem retranscrição.')
    w('')
    w('## 2. SHA-256 antes e depois (conteúdo LF; em disco o arquivo tem os fins de linha da árvore de trabalho, %s)' % ('CRLF (core.autocrlf=true)' if crlf else 'LF'))
    w('')
    w('| Versão | Origem | SHA-256 | bytes | linhas (`\\n`) |')
    w('|---|---|---|---|---|')
    w('| v1.2.11 (antes) | `regras/pacote_contrato.md` | `%s` | %d | %d |' % (sha(lf), len(lf), lf.count(b'\n')))
    w('| v1.2.12 (depois) | `regras/pacote_contrato.md` | `%s` | %d | %d |' % (sha(nb), len(nb), nb.count(b'\n')))
    w('')
    w('## 3. Diff por linha (contra a v1.2.11; nenhuma outra linha difere)')
    w('')
    w('| Id | Onde | Operação |')
    w('|---|---|---|')
    w('| C-1 | linha 1 (título) | "(v1.2.11, 2026-10-20)" → "(v1.2.12, 2026-10-23)" |')
    w('| C-2 | linha 3 | acréscimo, ao fim do parágrafo (depois de `ver a seção "Errata de forma da v1.2.11".`), da frase da v1.2.12 |')
    w('| C-3 | depois da linha que começa por "5. **Aplicação.** A partir da edição .md v1.13-E" | inserção de uma linha em branco e do bloco "Errata de forma da v1.2.12 (T-123; …)" (%d linhas, do parágrafo de abertura ao ponto 9), antes da linha em branco e do separador `---` |' % len(bloco))
    w('')
    w('Resultado: 1 linha trocada (título), 1 linha trocada (linha 3) e %d inseridas (%d − %d = %d). Opcodes de `difflib.SequenceMatcher(autojunk=False)` sobre as linhas LF (índices base 0, `[i1:i2] → [j1:j2]`): %s.' % (len(N) - len(L), len(N), len(L), len(N) - len(L), '; '.join('%s %d–%d → %d–%d' % o for o in ops)))
    w('')
    w('## 4. Texto exato')
    w('')
    w('Frase acrescentada ao fim da linha 3:')
    w('')
    w('> ' + frase.lstrip(' '))
    w('')
    w('Bloco inserido (texto exato, entre as marcas):')
    w('')
    w('---8<--- início do bloco')
    w('')
    r.extend(bloco)
    w('')
    w('---8<--- fim do bloco')
    w('')
    w('## 5. Conferência')
    w('')
    w('- O script aborta se o SHA-256 LF de entrada não for o da v1.2.11 (`85b30fcc…616b`) ou se alguma âncora (título; fim da linha 3; linha "5. **Aplicação.** A partir da edição .md v1.13-E") não ocorrer exatamente 1 vez.')
    w('- A conferência independente é da gbq-cqe (seção 13 da D1).')
    open(REG, 'wb').write(('\n'.join(r) + '\n').encode('utf-8'))
    print('registro', REG, sha(('\n'.join(r) + '\n').encode('utf-8')))


if __name__ == '__main__':
    main()
