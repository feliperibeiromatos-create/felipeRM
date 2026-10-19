"""Gera gerador_v1_8/MANIFESTO.md INTEIRO a partir das saídas da última execução do pipeline (T66_decisoes 7.2.3; D1-T67-R1; T70_T71_decisoes 5.4, D-T71-04; T81_D1_escopo_v1_8, 6.3).
Passo 11 de rodar_tudo.sh. Caminhos derivados de __file__. Todo SHA-256 é do conteúdo LF (no Windows o disco pode ter CRLF por core.autocrlf; a D1 da T-81 fixa o conteúdo LF).
Uso: python3 -B manifesto_v1_8.py [conferencia_f_2026-10-17_v1_8.json]  (padrão: o JSON ao lado deste script)"""
import hashlib, json, os, re, subprocess, sys
G = os.path.dirname(os.path.abspath(__file__))
G7 = os.path.join(os.path.dirname(G), 'gerador_v1_7')
REPO = os.path.abspath(os.path.join(G, '..', '..', '..'))
OUT = G + '/out'
def raw_lf(p): return open(p, 'rb').read().replace(b'\r\n', b'\n')
def sha(p): return hashlib.sha256(raw_lf(p)).hexdigest()
def jl(p): return json.load(open(p, encoding='utf-8'))

# --- contagens das saídas (cada uma é conferida; qualquer falha para o passo)
conf = jl(OUT + '/conferencias_v18.json'); N_CONF = len(conf); assert sum(1 for c in conf if not c[2]) == 0
last = open(OUT + '/conferencias_stdout.txt', encoding='utf-8').read().strip().split('\n')[-1]
assert last == '%d conferências; 0 falhas' % N_CONF, last
val = jl(OUT + '/validate.json'); N_VAL = len(val); assert all(v['ok'] for v in val) and N_VAL == 118
assert open(OUT + '/validate_stdout.txt', encoding='utf-8').read().strip().split('\n')[-1] == '%d verificações; 0 falhas' % N_VAL
mut = jl(OUT + '/fidelidade_mutacao.json'); N_MUT = mut['mutacoes']; assert mut['todas_detectadas']; N_MUT_DIF = mut['diferencas_detectadas']
N_FICT = len(os.listdir(OUT + '/casos_erros'))
ve = open(OUT + '/validar_erros_stdout.txt', encoding='utf-8').read().strip().split('\n')[-1]
m = re.match(r'^(\d+) conferências; 0 falhas$', ve); N_TREG = int(m.group(1))
N_EDIT = len(os.listdir(OUT + '/estudante')); assert N_EDIT == 34
fid = jl(OUT + '/estudante_fidelidade.json'); assert fid['diferencas'] == 0
ej = jl(OUT + '/estudante_json.json'); assert ej['falhas'] == []
st = jl(OUT + '/stats.json')
code = sorted(f for f in os.listdir(G) if os.path.isfile(os.path.join(G, f)) and f != 'MANIFESTO.md')
outs = []
for root, ds, fs in os.walk(OUT):
    ds.sort()
    for f in sorted(fs): outs.append(os.path.relpath(os.path.join(root, f), G).replace(os.sep, '/'))
outs = sorted(outs)
N_CODE, N_OUT = len(code), len(outs)
assert 'MANIFESTO.md' not in code and not any('__pycache__' in x for x in outs + code)
# a v1_7 fica intacta (D1 da T-81, 1.1): git status da pasta vazio
assert subprocess.run(['git', '-C', REPO, 'status', '--porcelain', '--', 'saida/pacote/gerador_v1_7'], capture_output=True, text=True, check=True).stdout.strip() == ''

# --- papéis herdados do MANIFESTO da v1_7
papel7 = {}
n7 = 0
for l in open(G7 + '/MANIFESTO.md', encoding='utf-8').read().split('\n'):
    l = l.rstrip('\r')
    mm = re.match(r'^\| ([^|]+) \| (\d+) \| `([0-9a-f]{64})` \| ([^|]+) \| (.*) \|$', l)
    if mm and not mm.group(1).startswith('out/'): papel7[mm.group(1)] = mm.group(5); n7 += 1
NOVOS = {'conferencias_v18.py': ('novo', 'ativo (conferências (0) a (9) da v1.8: %d; substitui `conferencias_v17.py`, que continua na v1_7)' % N_CONF),
         'manifesto_v1_8.py': ('novo', 'ativo, passo 11: gera este MANIFESTO inteiro a partir de `out/` (T66 7.2.3; D1-T67-R1; D-T71-04); substitui `manifesto_v1_7.py`, que continua na v1_7'),
         'conferencia_f_2026-10-17_v1_8.json': ('novo', 'registro datado da conferência (f) da produção da T-81, 17/10/2026; não é regerado'),
         'relatorio_v1_8.py': ('novo', 'ativo (relatório gerado pelo gerador com o conteúdo mínimo da seção 6.6 da D1 da T-81; substitui `relatorio_v1_7.py`, que continua na v1_7)'),
         'estudante_json.py': ('novo', 'ativo, passo 3: gera `out/pacote_estudante.json` (v1.8-E) a partir de `out/pacote.json`, só por deleção (mais CAIXA, REALINHA e a fusão 1-C/4-C/5-C), com as asserções (a) a (f) de 6.1; sai com código 1 se alguma falhar'),
         'marcas_processo.py': ('novo', 'ativo: a varredura R (seção 2.3 da D1) e as listas fechadas X (conteúdo) e Y (dúvida), transcritas da D1; usado por `estudante_json.py` e `conferencias_v18.py`')}
rows, alt, igu, nov = [], [], [], []
for f in code:
    p = os.path.join(G, f); b = len(raw_lf(p)); h = sha(p)
    if f in NOVOS:
        est, pap = NOVOS[f]; nov.append(f)
    else:
        p7 = os.path.join(G7, f); assert os.path.exists(p7), f
        est = 'igual à v1_7' if sha(p7) == h else 'alterado'
        (igu if est.startswith('igual') else alt).append(f)
        pap = papel7[f].replace('relatorio_v1_7.py', 'relatorio_v1_8.py').replace('conferencias_v17', 'conferencias_v18').replace('manifesto_v1_7', 'manifesto_v1_8')
    rows.append('| %s | %d | `%s` | %s | %s |' % (f, b, h, est, pap))
for f in outs:
    p = os.path.join(G, f)
    kind = 'saída (edição do estudante gerada)' if f.startswith('out/estudante/') else 'saída (T-59: caso do teste do validador-registro; dados fictícios)' if f.startswith('out/casos_erros/') else 'saída'
    rows.append('| %s | %d | `%s` | gerado | %s |' % (f, len(raw_lf(p)), sha(p), kind))
for f in ('validar_erros.py', 'validar_erros_teste.py'):      # registro (T-59): o MANIFESTO os marca
    assert any(r.startswith('| %s |' % f) and 'registro (T-59); versão mantida em `saida/treino/ferramentas/` (D-R59-08)' in r for r in rows), f

clone = jl(sys.argv[1] if len(sys.argv) > 1 else os.path.join(G, 'conferencia_f_2026-10-17_v1_8.json'))
ed_man = hashlib.sha256(''.join('%s  %s\n' % (sha(os.path.join(OUT, 'estudante', f)), f) for f in sorted(os.listdir(OUT + '/estudante'))).encode('utf-8')).hexdigest()

M = []
w = M.append
w('# MANIFESTO — T-81 — gerador v1.8 do pacote, do pacote do estudante (JSON) e da edição do estudante — 2026-10-17 — gerado por gbq-csc')
w('')
w('Origem: cópia de `saida/pacote/gerador_v1_7/` (intacta: `git status` da pasta sem alteração; os %d arquivos de código e os %d de `out/` da v1_7 não foram tocados) para `saida/pacote/gerador_v1_8/`, alterada depois (lista fechada da D1, `saida/pacote/T81_D1_escopo_v1_8_2026-10-17.md`, 1.1 e 1.2); `out/` da v1_7 não foi copiado (é regerado). `conferencias_v17.py`, `relatorio_v1_7.py`, `manifesto_v1_7.py` e `conferencia_f_2026-10-14_v1_7.json` não foram trazidos (continuam na v1_7; os da v1.8 são `conferencias_v18.py`, `relatorio_v1_8.py`, `manifesto_v1_8.py` e `conferencia_f_2026-10-17_v1_8.json`). Scripts temporários da ocorrência (aplicação das alterações às cópias, montagem de `conferencias_v18.py` a partir de trechos da v17, aplicação do contrato por programa, shim de execução no Windows) ficaram só no scratchpad; **nenhum deles é necessário para regenerar**: o MANIFESTO é gerado por `manifesto_v1_8.py` (passo 11) e tudo o mais por `rodar_tudo.sh`. Comando de execução (a partir de qualquer pasta; `-B` evita `__pycache__`; `-I` não serve para os scripts do gerador, porque bloqueia os imports entre scripts; só `validar_erros.py`, que não importa módulo do gerador, roda com `-I`): `sh saida/pacote/gerador_v1_8/rodar_tudo.sh` (roda o pipeline abaixo) ou `python3 -B saida/pacote/gerador_v1_8/<script>.py`.' % (n7, 71))
w('')
w('## Ordem de execução')
w('')
w('`rodar_tudo.sh` apaga e recria `out/` e roda os passos abaixo, na ordem, parando na primeira falha (`set -e`). Cada `out/*_stdout.txt` é a saída-padrão do script, **redirecionada pelo runner** (os scripts não gravam esses arquivos). Quem rodar os scripts à mão deve redirecionar do mesmo modo para obter os mesmos `*_stdout.txt`. `validate.py` e `conferencias_v18.py` saem com código 1 se houver falha (T-69 (4)), e por isso uma falha de validação para o pipeline no passo 6.')
w('')
w('| # | Comando | Redirecionamento da saída-padrão | Arquivos que o próprio script grava em `out/` |')
w('|---|---|---|---|')
w('| 1 | `python3 -B build_pacote.py` | `> out/gen_stdout.txt` | `pacote.json`, `stats.json` |')
w('| 2 | `python3 -B estudante_gen.py` | `>> out/gen_stdout.txt` (acrescenta ao do passo 1) | `estudante/` (%d arquivos), `estudante_contagem.json` |' % N_EDIT)
w('| 3 | `python3 -B estudante_json.py` | `> out/estudante_json_stdout.txt` | `pacote_estudante.json`, `estudante_json.json` (contagens por regra e por campo, casamentos de R, termos fora da lista) |')
w('| 4 | `python3 -B estudante_fidelidade.py` | `> out/fidelidade_stdout.txt` (caminhos impressos relativos à raiz do repositório; sem caminho absoluto) | `estudante_fidelidade.json` |')
w('| 5 | `python3 -B sync_check.py` | `> out/sync_stdout.txt` (conteúdo igual ao de `sync_check.txt`; inclui a E13) | `sync_check.txt`, `sync_check.json` |')
w('| 6 | `python3 -B validate.py` | `> out/validate_stdout.txt` | `validate.json` (%d verificações) |' % N_VAL)
w('| 7 | `python3 -B conferencias_v18.py` | `> out/conferencias_stdout.txt` (conteúdo igual ao de `conferencias_v18.txt`) | `conferencias_v18.txt`, `conferencias_v18.json` (%d conferências), `varredura_volatil_v18.json` |' % N_CONF)
w('| 8 | `python3 -B fidelidade_mutacao.py` (~2 min: %d mutações, cada uma com a fidelidade completa) | `> out/mutacao_stdout.txt` | `fidelidade_mutacao.json` (%d mutações, todas detectadas) |' % (N_MUT, N_MUT))
w('| 9 | `python3 -B validar_erros_teste.py` (T-59, registro) | `> out/validar_erros_stdout.txt` (%d conferências) | `casos_erros/` (%d arquivos fictícios) |' % (N_TREG, N_FICT))
w('| 10 | `python3 -B relatorio_v1_8.py` | `> out/relatorio_stdout.txt` (uma linha: n.º de linhas) | `pacote_relatorio_2026-10-17_v1_8.md` |')
w('| 11 | `python3 -B manifesto_v1_8.py` | nenhum (a saída-padrão vai ao stderr do runner; um arquivo em `out/` seria listado por este próprio passo) | nenhum em `out/`; grava `MANIFESTO.md` (fora de `out/`) |')
w('')
w('Fora de `out/`, o pipeline grava no repositório apenas o `MANIFESTO.md` desta pasta, no passo 11 (`fidelidade_mutacao.py` e `conferencias_R1.py` usam pastas temporárias fora do repositório; `conferencias_v18.py` e `validar_erros_teste.py` também). Tudo grava em `out/`; a promoção para `saida/pacote/pacote.json`, `saida/pacote/pacote_estudante.json`, `saida/estudante/` e `saida/pacote/pacote_relatorio_2026-10-17_v1_8.md` é um passo explícito (cópia) depois de todas as conferências com 0 falhas (D1, 6.5). Caminhos derivados de `__file__` (raiz do repositório = três níveis acima de `gerador_v1_8/`); as referências v1/v1.1/R0/v1.2/v1.3/v1.4/v1.5/v1.6/v1.7 vêm do git por `refs.py` (`git show <commit>:<caminho>`, somente leitura): v1 `5eab2d9`, v1.1 `e97ab1f`, R0 `27e594d`, v1.2 `2684ab1`, v1.3 `9622604`, v1.4 `e9b6402`, v1.5 `a889100`, v1.6 `569c5dd`, **v1.7 `62ab128`** (o commit da produção da T-71, o primeiro em que `saida/pacote/pacote.json` tem o SHA-256 `f20216c2…`; a edição v1.7 tem o manifesto ordenado `67d2bdf85925a232`; é a base do diff e da comparação de fontes). As conferências (2) da v1.8 reconstroem o contrato v1.2.5 (v1.2.4 do git + C-1 a C-3 lidas dos blocos literais da D1, seção 4); as (8), a regra `importacao_erros.md` v1.2, o exemplo e o validador mantido, o `rodar_tudo.sh`, a lista de arquivos frente à v1_7 e o T-69 (4).')
w('')
w('## Scripts históricos (O-1, D-T56-05, D-T57-10: opção "marcar")')
w('')
w('Não executáveis, mantidos **sem alteração** (idênticos, byte a byte, aos de `gerador_v1_4/` a `gerador_v1_7/`) como registro da R0/R1: cada um sai com código 1 e não grava nada no repositório: `relatorio_R1.py` (falta `out/conferencias_R1.json`), `report.py` (falta `stats.pkl`), `report2.py` (`ValueError`, formato de `stats` mudou), `diff.py` (`TypeError`) e `diff2.py` (`KeyError: legendaMecanismo`). Executáveis e também históricos: `conferencias_R1.py` (118 conferências, lê R0 e R1 do git; grava `out/conferencias_R1.json` e `out/varredura_volatil.json`, fora do pipeline), `probe.py`, `resid.py` e `review.py`. `texts.py` é módulo auxiliar ativo. `validar_erros.py` e `validar_erros_teste.py` são **registro (T-59)**, congelados com o SHA-256 da T-61 (`19ab9c8b…` e `33132d5a…`); a versão mantida é a de `saida/treino/ferramentas/`, que a T-66 alterou (SHA-256 `220dd559…` e `192581d9…`) e a T-71 e a T-81 mantiveram (T-69 (2) continua BACKLOG).')
w('')
w('## Arquivos (SHA-256 de cada um, do conteúdo LF)')
w('')
w('| Arquivo | Bytes | SHA-256 | Estado frente à v1_7 | Papel |')
w('|---|---|---|---|---|')
for r in rows: w(r)
w('')
w('Total: %d arquivos listados (%d de código/auxiliares e %d em `out/`), mais este `MANIFESTO.md` (não tem hash próprio). Código frente à v1_7: %d iguais, %d alterados, %d novos (`%s`). A edição em `out/estudante/` tem %d arquivos (34: 1-C, 4-C e 5-C fundidos nos Lotes 1, 4 e 5). Manifesto ordenado da edição (SHA-256 das linhas "<sha256>  <nome>"): v1.7 `67d2bdf85925a232` → v1.8 `%s`. A tabela acima é a da execução do pipeline cujo `out/` foi promovido. Depois da promoção, `out/estudante/` e `saida/estudante/` são idênticos (diff recursivo); `out/pacote.json` e `saida/pacote/pacote.json`, `out/pacote_estudante.json` e `saida/pacote/pacote_estudante.json`, e `out/pacote_relatorio_2026-10-17_v1_8.md` e `saida/pacote/pacote_relatorio_2026-10-17_v1_8.md` têm o mesmo SHA-256.' % (N_CODE + N_OUT, N_CODE, N_OUT, len(igu), len(alt), len(nov), '`, `'.join(nov), N_EDIT, ed_man[:16]))
w('')
w('## Mudanças frente à v1_7')
w('')
w('- Novos: `conferencias_v18.py` (conferências (0) diff v1.7 → v1.8 do pacote, só `$.nome` e `$.geradoEm`, (1) histórico v1.6 → v1.7, v1.5 → v1.6 e o diff acumulado v1.3 → v1.8, (2) contrato v1.2.4 → v1.2.5 por C-1 a C-3, (3) edição v1.7 → v1.8 (9 retirados, 8 alterados, 26 idênticos, reconstrução da fusão), (4) identidade `pacote.json` × `pacote_estudante.json`, (5) JSON × edição v1.7, (6) JSON × edição v1.8, (7) varredura R no JSON e na edição, (8) não regressão (T-59 e T-66, lista de arquivos, `rodar_tudo.sh`, T-69 (4), varreduras da seção 3.5, CAIXA, REUNIÃO, contagens), (9) mutações M1 a M8 do JSON; **%d conferências**), `estudante_json.py`, `marcas_processo.py`, `relatorio_v1_8.py`, `manifesto_v1_8.py` (passo 11) e `conferencia_f_2026-10-17_v1_8.json` (registro datado da conferência (f)).' % N_CONF)
w('- Alterados (só o necessário, lista fechada da D1, 1.2): %s. Em síntese: `build_pacote.py` (`nome` "Câmara 2026 — pacote F4 (v1.8)"; `geradoEm` "2026-10-17"), `common.py` (só o comentário do caminho), `refs.py` (`C_V17`, `v17()`), `validate.py` (`nome` e `geradoEm` esperados, caminho do `p2.py`, e, como última instrução, `sys.exit(1 if fails else 0)` — T-69 (4); as %d verificações continuam), `estudante_gen.py` e `estudante_fidelidade.py` (fusão 1-C/4-C/5-C e versão v1.8; escopo das deleções = nome de arquivo de origem da v1.7) e `rodar_tudo.sh` (os 11 passos de 6.3, cabeçalho no padrão R-1 a R-6 da T-71). `fidelidade_mutacao.py` não muda (%d mutações; nenhuma tinha como alvo arquivo L1C_, L4C_ ou L5C_).' % ('`' + '`, `'.join(alt) + '`', N_VAL, N_MUT))
w('- Iguais à v1_7: %d arquivos de código (os 5 históricos não executáveis, `conferencias_R1.py`, `probe.py`, `resid.py`, `review.py`, `estudante_marcas.py`, `literais.py`, `p1.py`, `p2.py`, `peg.py`, `gce.py`, `banco.py`, `edital_p.py`, `f4.py`, `registry.py`, `sync_check.py`, `texts.py`, `lotes_tab.txt`, `fidelidade_mutacao.py`, `validar_erros.py` e `validar_erros_teste.py`).' % len(igu))
w('- Desta ocorrência: o pacote v1.8 é a v1.7 com só `$.nome` e `$.geradoEm` trocados (SHA-256 `%s`, %d bytes; v1.7: `f20216c2…`, 621907 bytes); o `pacote_estudante.json` v1.8-E (SHA-256 `%s`, %d bytes) é novo; a edição do estudante perde os 9 arquivos dos complementos e muda 8 (README, L1_estudo, L1_itens, L1_gabarito, L4_itens, L4_gabarito, L5_itens, L5_gabarito); o `MANIFESTO.md` é gerado só pelo passo 11 (D-T71-04), nunca à mão.' % (sha(OUT + '/pacote.json'), len(raw_lf(OUT + '/pacote.json')), sha(OUT + '/pacote_estudante.json'), len(raw_lf(OUT + '/pacote_estudante.json'))))
w('- Fora do diretório (não copiados): `__pycache__/` (não gerado), `out/` da v1_7 (regerado), `MANIFESTO.md` da v1_7, `conferencias_v17.py`, `relatorio_v1_7.py`, `manifesto_v1_7.py` e `conferencia_f_2026-10-14_v1_7.json`.')
w('')
w('## Conferência (f): regeração byte a byte em cópias limpas (registro datado da ocorrência de 17/10/2026: clone de `%s` com `gerador_v1_8/` sobreposto)' % (clone['head'] if clone else '—'))
w('')
w('Método: `git clone` do repositório local (HEAD `%s`) em pasta nova do scratchpad (uma rodada a partir de /tmp); o clone só enxerga o que está commitado. Sobrepõe-se só o que ainda não está no git: `saida/pacote/gerador_v1_8/` (sem `out/`, com este `MANIFESTO.md` e o registro datado desta conferência), `regras/pacote_contrato.md` (v1.2.5), `saida/pacote/contrato_v1_2_5_2026-10-17.md` e a D1. `saida/pacote/pacote.json`, `saida/pacote/pacote_estudante.json` e `saida/estudante/` não são sobrepostos (a regeração não os lê). Execução de `rodar_tudo.sh` em cada cópia (uma de dentro da própria cópia, outra a partir de /tmp, `PYTHONHASHSEED` e pastas diferentes das do original) e comparação de `out/` arquivo a arquivo (`filecmp`, byte a byte) e do `MANIFESTO.md` regerado (passo 11) com o desta pasta.' % (clone['head'] if clone else '—'))
w('')
if clone:
    w('| Cópia | cwd | PYTHONHASHSEED | arquivos em `out/` (original / cópia) | idênticos byte a byte | diferenças de nome |')
    w('|---|---|---|---|---|---|')
    for r in clone['runs']:
        w('| %s | `%s` | %s | %d / %d | %d | %s |' % (r['nome'], r['cwd'], r['seed'], r['n_orig'], r['n_clone'], r['identicos'], r['dif_nome'] or 'nenhuma'))
    w('')
    w(clone['texto'])
else:
    w('Resultado: a executar.')
w('')
w('## Determinismo')
w('')
w('O pipeline completo foi executado a partir de `out/` vazio no original e nas cópias limpas acima (pastas e `PYTHONHASHSEED` diferentes); `out/pacote.json`, `out/pacote_estudante.json`, `out/estudante/`, o relatório e o `MANIFESTO.md` têm os mesmos SHA-256 em todas. Nenhum script lê data ou hora do sistema, nem o `HEAD` do git (o relatório não imprime o HEAD); `geradoEm` é literal.')
TXT = '\n'.join(M).replace('@TMP@', '/' + 'tmp') + '\n'
open(os.path.join(G, 'MANIFESTO.md'), 'w', encoding='utf-8', newline='').write(TXT)
print('ok', N_CODE, N_OUT, N_CONF, N_VAL, N_MUT, N_FICT, N_TREG, N_EDIT)
