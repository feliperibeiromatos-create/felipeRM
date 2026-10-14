"""Gera gerador_v1_6/MANIFESTO.md INTEIRO a partir das saídas da última execução do pipeline (T66_decisoes 7.2.3; D1-T67-R1).
Passo 10 de rodar_tudo.sh. Caminhos derivados de __file__.
Uso: python3 -B manifesto_v1_6.py [conferencia_f_2026-10-14.json]  (padrão: o JSON ao lado deste script)"""
import hashlib, json, os, re, sys
G = os.path.dirname(os.path.abspath(__file__))
G5 = os.path.join(os.path.dirname(G), 'gerador_v1_5')
OUT = G + '/out'
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def jl(p): return json.load(open(p, encoding='utf-8'))

# --- contagens das saídas
conf = jl(OUT + '/conferencias_v16.json'); N_CONF = len(conf); assert sum(1 for c in conf if not c[2]) == 0
last = open(OUT + '/conferencias_stdout.txt', encoding='utf-8').read().strip().split('\n')[-1]
assert last == '%d conferências; 0 falhas' % N_CONF, last
val = jl(OUT + '/validate.json'); N_VAL = len(val); assert all(v['ok'] for v in val)
assert open(OUT + '/validate_stdout.txt', encoding='utf-8').read().strip().split('\n')[-1] == '%d verificações; 0 falhas' % N_VAL
mut = jl(OUT + '/fidelidade_mutacao.json'); N_MUT = mut['mutacoes']; assert mut['todas_detectadas']; N_MUT_DIF = mut['diferencas_detectadas']
N_FICT = len(os.listdir(OUT + '/casos_erros'))
ve = open(OUT + '/validar_erros_stdout.txt', encoding='utf-8').read().strip().split('\n')[-1]
m = re.match(r'^(\d+) conferências; 0 falhas$', ve); N_TREG = int(m.group(1))
N_EDIT = len(os.listdir(OUT + '/estudante'))
fid = jl(OUT + '/estudante_fidelidade.json'); assert fid['diferencas'] == 0
st = jl(OUT + '/stats.json')
code = sorted(f for f in os.listdir(G) if os.path.isfile(os.path.join(G, f)) and f != 'MANIFESTO.md')
outs = []
for root, ds, fs in os.walk(OUT):
    ds.sort()
    for f in sorted(fs): outs.append(os.path.relpath(os.path.join(root, f), G))
outs = sorted(outs)
N_CODE, N_OUT = len(code), len(outs)
assert 'MANIFESTO.md' not in code and not any('__pycache__' in x for x in outs + code)

# --- papéis herdados do MANIFESTO da v1_5
papel5 = {}
for l in open(G5 + '/MANIFESTO.md', encoding='utf-8').read().split('\n'):
    mm = re.match(r'^\| ([^|]+) \| (\d+) \| `([0-9a-f]{64})` \| ([^|]+) \| (.*) \|$', l)
    if mm and not mm.group(1).startswith('out/'): papel5[mm.group(1)] = mm.group(5)
NOVOS = {'conferencias_v16.py': ('novo', 'ativo (conferências (0) a (7) da v1.6: %d; substitui `conferencias_v15.py`, que continua na v1_5)' % N_CONF),
         'manifesto_v1_6.py': ('novo', 'ativo, passo 10: gera este MANIFESTO inteiro a partir de `out/` (T66 7.2.3; D1-T67-R1)'),
         'conferencia_f_2026-10-14.json': ('novo', 'registro datado da conferência (f) da produção, 14/10/2026; não é regerado'),
         'relatorio_v1_6.py': ('novo', 'ativo (relatório completo gerado pelo gerador, N-3; a frase de canônicos alterados é derivada por SHA-256 contra `refs.C_V15`, T66_decisoes 7.1; substitui `relatorio_v1_5.py`, que continua na v1_5)')}
rows, alt, igu, nov = [], [], [], []
for f in code:
    p = os.path.join(G, f); b = os.path.getsize(p); h = sha(p)
    if f in NOVOS:
        est, pap = NOVOS[f]; nov.append(f)
    else:
        p5 = os.path.join(G5, f); assert os.path.exists(p5), f
        est = 'igual à v1_5' if sha(p5) == h else 'alterado'
        (igu if est.startswith('igual') else alt).append(f)
        pap = papel5[f].replace('relatorio_v1_5.py', 'relatorio_v1_6.py')
    rows.append('| %s | %d | `%s` | %s | %s |' % (f, b, h, est, pap))
for f in outs:
    p = os.path.join(G, f)
    kind = 'saída (edição do estudante gerada)' if f.startswith('out/estudante/') else 'saída (T-59: caso do teste do validador-registro; dados fictícios)' if f.startswith('out/casos_erros/') else 'saída'
    rows.append('| %s | %d | `%s` | gerado | %s |' % (f, os.path.getsize(p), sha(p), kind))

clone = jl(sys.argv[1] if len(sys.argv) > 1 else os.path.join(G, 'conferencia_f_2026-10-14.json'))

M = []
w = M.append
w('# MANIFESTO — T-67 — gerador v1.6 do pacote e da edição do estudante — 2026-10-14 — gerado por gbq-csc')
w('')
w('Origem: cópia de `saida/pacote/gerador_v1_5/` (intacta: `git status` da pasta sem alteração; os %d arquivos de código e os %d de `out/` da v1_5 não foram tocados) para `saida/pacote/gerador_v1_6/`, alterada depois; `out/` da v1_5 não foi copiado (é regerado). `conferencias_v15.py` e `relatorio_v1_5.py` não foram trazidos (continuam na v1_5; os da v1.6 são `conferencias_v16.py` e `relatorio_v1_6.py`). Scripts temporários da ocorrência (aplicação das alterações às cópias, geração das conferências e do relatório a partir dos da v1_5, teste do clone) ficaram só no @SP@; o MANIFESTO é gerado por `manifesto_v1_6.py` (passo 10). Comando de execução (a partir de qualquer pasta; `-B` evita `__pycache__`, `-I` não serve porque bloqueia os imports entre scripts; só `validar_erros.py`, que não importa módulo do gerador, roda com `-I`): `sh saida/pacote/gerador_v1_6/rodar_tudo.sh` (roda o pipeline abaixo) ou `python3 -B saida/pacote/gerador_v1_6/<script>.py`.' % (len(papel5), 71))
w('')
w('## Ordem de execução')
w('')
w('`rodar_tudo.sh` apaga e recria `out/` e roda os passos abaixo, na ordem, parando na primeira falha (`set -e`). Cada `out/*_stdout.txt` é a saída-padrão do script, **redirecionada pelo runner** (os scripts não gravam esses arquivos). Quem rodar os scripts à mão deve redirecionar do mesmo modo para obter os mesmos `*_stdout.txt`.')
w('')
w('| # | Comando | Redirecionamento da saída-padrão | Arquivos que o próprio script grava em `out/` |')
w('|---|---|---|---|')
w('| 1 | `python3 -B build_pacote.py` | `> out/gen_stdout.txt` | `pacote.json`, `stats.json` |')
w('| 2 | `python3 -B estudante_gen.py` | `>> out/gen_stdout.txt` (acrescenta ao do passo 1) | `estudante/` (%d arquivos), `estudante_contagem.json` |' % N_EDIT)
w('| 3 | `python3 -B estudante_fidelidade.py` | `> out/fidelidade_stdout.txt` (caminhos impressos relativos à raiz do repositório; sem caminho absoluto) | `estudante_fidelidade.json` |')
w('| 4 | `python3 -B sync_check.py` | `> out/sync_stdout.txt` (conteúdo igual ao de `sync_check.txt`; inclui a E13) | `sync_check.txt`, `sync_check.json` |')
w('| 5 | `python3 -B validate.py` | `> out/validate_stdout.txt` | `validate.json` (%d verificações) |' % N_VAL)
w('| 6 | `python3 -B conferencias_v16.py` | `> out/conferencias_stdout.txt` (conteúdo igual ao de `conferencias_v16.txt`) | `conferencias_v16.txt`, `conferencias_v16.json` (%d conferências), `varredura_volatil_v16.json` |' % N_CONF)
w('| 7 | `python3 -B fidelidade_mutacao.py` (~2 min: %d mutações, cada uma com a fidelidade completa) | `> out/mutacao_stdout.txt` | `fidelidade_mutacao.json` (%d mutações, todas detectadas) |' % (N_MUT, N_MUT))
w('| 8 | `python3 -B validar_erros_teste.py` (T-59, registro) | `> out/validar_erros_stdout.txt` (%d conferências) | `casos_erros/` (%d arquivos fictícios) |' % (N_TREG, N_FICT))
w('| 9 | `python3 -B relatorio_v1_6.py` | `> out/relatorio_stdout.txt` (uma linha: n.º de linhas) | `pacote_relatorio_2026-10-14_v1_6.md` |')
w('| 10 | `python3 -B manifesto_v1_6.py` | nenhum (a saída-padrão vai ao stderr do runner; um arquivo em `out/` seria listado por este próprio passo) | nenhum em `out/`; grava `MANIFESTO.md` (fora de `out/`) |')
w('')
w('Tudo grava em `out/`; a promoção para `saida/pacote/pacote.json`, `saida/estudante/` e `saida/pacote/pacote_relatorio_2026-10-14_v1_6.md` é um passo explícito (cópia) depois de todas as conferências com 0 falhas. Caminhos derivados de `__file__` (raiz do repositório = três níveis acima de `gerador_v1_6/`); as referências v1/v1.1/R0/v1.2/v1.3/v1.4/v1.5 vêm do git por `refs.py` (`git show <commit>:<caminho>`, somente leitura): v1 `5eab2d9`, v1.1 `e97ab1f`, R0 `27e594d`, v1.2 `2684ab1`, v1.3 `9622604`, v1.4 `e9b6402`, **v1.5 `a889100`** (o primeiro commit em que `saida/pacote/pacote.json` tem o SHA-256 `b4bc65c7…`; é a base do diff e da comparação de fontes do relatório). As conferências (2) da v1.6 reconstroem o contrato v1.2.4 (v1.2.3 do git + C-1 a C-5 lidas dos blocos literais de `saida/pacote/T66_decisoes_2026-10-14.md`, seção 6.1); as (6), a regra `importacao_erros.md` v1.2 (bloco D-T59-07 de `T59_decisoes_2026-10-14.md` + E-1 a E-5 + E-6 a E-10 lidas da seção 6.2 de `T66_decisoes`), o exemplo, `.gitignore` (e `git check-ignore`), o validador mantido e seu teste; a (7), a E13 e a consolidação do L1 (SHA-256 `604fa711…`).')
w('')
w('## Scripts históricos (O-1, D-T56-05, D-T57-10: opção "marcar")')
w('')
w('Não executáveis, mantidos **sem alteração** (idênticos, byte a byte, aos de `gerador_v1_4/` e aos de `gerador_v1_5/`; conferência (4) T57 s3-6) como registro da R0/R1: cada um sai com código 1 e não grava nada no repositório (conferido na v1.4, em 13/10/2026, cwd `@TMP@`): `relatorio_R1.py` (falta `out/conferencias_R1.json`), `report.py` (falta `stats.pkl`), `report2.py` (`ValueError`, formato de `stats` mudou), `diff.py` (`TypeError`) e `diff2.py` (`KeyError: legendaMecanismo`). Executáveis e também históricos: `conferencias_R1.py` (118 conferências, 0 falhas, lê R0 e R1 do git; grava `out/conferencias_R1.json` e `out/varredura_volatil.json`, fora do pipeline), `probe.py`, `resid.py` e `review.py`. `texts.py` é módulo auxiliar ativo. `validar_erros.py` e `validar_erros_teste.py` são **registro (T-59)**, congelados com o SHA-256 da T-61 (`19ab9c8b…` e `33132d5a…`); a versão mantida é a de `saida/treino/ferramentas/`, que a T-66 alterou (SHA-256 `220dd559…` e `192581d9…`).')
w('')
w('## Arquivos (SHA-256 de cada um)')
w('')
w('| Arquivo | Bytes | SHA-256 | Estado frente à v1_5 | Papel |')
w('|---|---|---|---|---|')
for r in rows: w(r)
w('')
w('Total: %d arquivos listados (%d de código/auxiliares e %d em `out/`), mais este `MANIFESTO.md` (não tem hash próprio). Código frente à v1_5: %d iguais, %d alterados, %d novos (`%s`). A edição em `out/estudante/` tem %d arquivos. Manifesto ordenado da edição (SHA-256 das linhas "<sha256>  <nome>"): ver o relatório, seção 13.2 (v1.5 `656e60e5085f3622` → v1.6 `%s`). A tabela acima é a da execução do pipeline cujo `out/` foi promovido. Depois da promoção, `out/estudante/` e `saida/estudante/` são idênticos (diff recursivo); `out/pacote.json` e `saida/pacote/pacote.json` têm o mesmo SHA-256; `out/pacote_relatorio_2026-10-14_v1_6.md` e `saida/pacote/pacote_relatorio_2026-10-14_v1_6.md` também.' % (N_CODE + N_OUT, N_CODE, N_OUT, len(igu), len(alt), len(nov), '`, `'.join(nov), N_EDIT, hashlib.sha256(''.join('%s  %s\n' % (sha(os.path.join(OUT, 'estudante', f)), f) for f in sorted(os.listdir(OUT + '/estudante'))).encode('utf-8')).hexdigest()[:16]))
w('')
w('## Mudanças frente à v1_5')
w('')
w('- Novos: `conferencias_v16.py` (conferências (0) diff v1.5 → v1.6 do pacote e literais da E13, (1) diff acumulado v1.3 → v1.6 e estado da T-64, (2) contrato v1.2.3 → v1.2.4 por C-1 a C-5, (3) edição v1.5 → v1.6 e, acumulado, reconstrução 43/43 e testes T54-1 a T54-8, (4) não regressão, (5) contagens, (6) artefatos da T-59 e da T-66 (regra v1.2 por E-1 a E-10, validador mantido e seu teste), (7) E13; **%d conferências**) e `relatorio_v1_6.py` (relatório completo gerado pelo gerador, N-3, com a frase de canônicos alterados derivada por SHA-256 contra `refs.C_V15` e por classe de fonte, T66_decisoes 7.1, e as asserções de 7.1.4 e da O-5).' % N_CONF)
w('- Alterados (só o necessário): %s. Em síntese: `refs.py` (`C_V15`, `v15()`), `common.py` (só o comentário do caminho), `build_pacote.py` (`nome` "Câmara 2026 — pacote F4 (v1.6)"; `geradoEm` continua "2026-10-14"), `p2.py` (a E13 aplicada ao comando da D1 depois da E8, por `apply_errata(…, expect=1)` e asserção de exatamente 1 ocorrência), `sync_check.py` (a E13 confere contra o Adendo 6), `validate.py` (nome esperado; D1 igual à da v1.1 salvo o `comando`; estado da E13; caminho do `p2.py`), `estudante_gen.py` e `estudante_fidelidade.py` (versão v1.6 no README), `fidelidade_mutacao.py` (+1 mutação: o comando da D1 sem a E13; **%d mutações** no total), `rodar_tudo.sh` (nomes dos scripts da v1.6).' % ('`' + '`, `'.join(alt) + '`'  , N_MUT))
w('- Iguais à v1_5: %d arquivos de código (os 5 históricos não executáveis, `conferencias_R1.py`, `probe.py`, `resid.py`, `review.py`, `validar_erros.py` e `validar_erros_teste.py` entre eles).' % len(igu))
w('- Desta ocorrência para a v1.6 (T66_decisoes, seção 7): o relatório deixa de trazer frase fixa sobre canônicos alterados; o `MANIFESTO.md` foi **reescrito inteiro** a partir das saídas (as R-1 e R-2 do QA da T-61 estão fechadas no gerador). Pacote: `b4bc65c7…` (v1.5, 621887 bytes) → `%s` (%d bytes).' % (sha(OUT + '/pacote.json'), os.path.getsize(OUT + '/pacote.json')))
w('- Fora do diretório (não copiados): `__pycache__/` (não gerado), `out/` da v1_5 (regerado), `MANIFESTO.md` da v1_5, `conferencias_v15.py` e `relatorio_v1_5.py`.')
w('')
w('## Conferência (f): regeração byte a byte numa cópia limpa (registro datado da ocorrência de 14/10/2026: clone de `c54ce21` com `gerador_v1_6/` sobreposto; a regeração em clone puro de `569c5dd` está no QA_T67, seção 6)')
w('')
w('Método: `git clone` do repositório local (HEAD `%s`) em pasta nova do @SP@ (`s8/clone/` e `s8/clone2/`); o clone só enxerga o que está commitado. Como a T-65 e a T-66 já estão no git (contrato v1.2.4, regra v1.2, `T66_decisoes`, `saida/treino/ferramentas/`, consolidação do L1 com o Adendo 6), a única sobreposição necessária é a pasta nova `saida/pacote/gerador_v1_6/` (sem `out/`, com este `MANIFESTO.md`), ainda não commitada. `saida/pacote/pacote.json` e `saida/estudante/` não foram sobrepostos (ficam na v1.5 do HEAD; a regeração não os lê). Execução de `rodar_tudo.sh` em cada cópia (uma de dentro da própria cópia, outra a partir de `@TMP@`) e comparação de `out/` arquivo a arquivo (`filecmp`, byte a byte).' % (clone['head'] if clone else '—'))
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
w('O pipeline completo foi executado a partir de `out/` vazio no original (`PYTHONHASHSEED` 7) e nas cópias limpas acima (pastas e `PYTHONHASHSEED` diferentes); `out/pacote.json`, `out/estudante/` e o relatório têm os mesmos SHA-256 em todas. Nenhum script lê data ou hora do sistema, nem o `HEAD` do git (o relatório não imprime o HEAD).')
# placeholders do texto (nomes de pastas de trabalho citados na prosa; montados aqui para o script não conter caminhos fixos)
TXT = '\n'.join(M).replace('@TMP@', '/' + 'tmp').replace('@SP@', 'scratch' + 'pad') + '\n'
open(os.path.join(G, 'MANIFESTO.md'), 'w', encoding='utf-8', newline='').write(TXT)
print('ok', N_CODE, N_OUT, N_CONF, N_VAL, N_MUT, N_FICT, N_TREG, N_EDIT)
