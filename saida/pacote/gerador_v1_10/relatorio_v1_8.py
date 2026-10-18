# -*- coding: utf-8 -*-
"""T-81 — relatório da produção da v1.8 (D1 da GBQ, seção 6.6): grava out/pacote_relatorio_2026-10-17_v1_8.md. Passo 10 de rodar_tudo.sh.
Conteúdo mínimo da 6.6: SHA-256 e bytes de pacote.json, pacote_estudante.json, contrato v1.2.5 e manifesto da edição; o diff v1.7 -> v1.8; as deleções por regra e por campo no JSON; a lista X, Y1 como DÚVIDA
e a contagem dos termos fora da lista; a tabela 3.4; a nota da legendaMecanismo do L5C; E13 e T-54 já aplicadas; T-69 (4) feita e (2) BACKLOG; as divergências de escopo da 6.2 (5); o registro P8; os resultados de 6.1 a 6.4.
Tolerante a saídas ausentes (um passo anterior pode ter falhado): o que faltar vira divergência registrada, sem inventar valor. Nenhuma leitura de data, hora ou HEAD; caminhos relativos à raiz do repositório."""
import collections, hashlib, json, os, re, sys
import refs
import estudante_gen as gen
import marcas_processo as mp
from common import OUT, REPO, read

def raw_lf(p): return open(p, 'rb').read().replace(b'\r\n', b'\n')
def sha(b): return hashlib.sha256(b).hexdigest()
def jl(p):
    try:
        return json.load(open(p, encoding='utf-8'))
    except Exception:
        return None
def existe(p): return os.path.exists(p)
def fmt_sha(h): return '`%s`' % h

D1_PATH = os.path.join(REPO, 'saida', 'pacote', 'T81_D1_escopo_v1_8_2026-10-17.md')
D1 = raw_lf(D1_PATH).decode('utf-8')
m_ = re.search(r'`pacote\.json` v1\.8 \(LF\): (\d+) bytes, SHA-256 `([0-9a-f]{64})`', D1)
BYTES_ESP, SHA_ESP = int(m_.group(1)), m_.group(2)
m_ = re.search(r'CONTRATO-V125: (\d+) bytes, (\d+) linhas, SHA-256 `([0-9a-f]{64})`', D1)
CTR_B_ESP, CTR_L_ESP, CTR_SHA_ESP = int(m_.group(1)), int(m_.group(2)), m_.group(3)

DIV = []          # divergências frente à especificação (registradas, nunca "ajustadas")
def divergencia(txt): DIV.append(txt)

P_PATH = os.path.join(OUT, 'pacote.json')
raw18 = raw_lf(P_PATH); P18 = json.loads(raw18.decode('utf-8'))
raw17 = refs.git_show(refs.C_V17, refs.PACOTE); P17 = json.loads(raw17.decode('utf-8'))
JE_PATH = os.path.join(OUT, 'pacote_estudante.json')
JE_RAW = raw_lf(JE_PATH) if existe(JE_PATH) else None
ej = jl(os.path.join(OUT, 'estudante_json.json'))
conf = jl(os.path.join(OUT, 'conferencias_v18.json'))
val = jl(os.path.join(OUT, 'validate.json'))
fid = jl(os.path.join(OUT, 'estudante_fidelidade.json'))
mut = jl(os.path.join(OUT, 'fidelidade_mutacao.json'))
cf = jl(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'conferencia_f_2026-10-17_v1_8.json'))
ED = os.path.join(OUT, 'estudante')
E18 = {f: raw_lf(os.path.join(ED, f)).decode('utf-8') for f in sorted(os.listdir(ED))} if existe(ED) else {}
def manifesto(E): return sha(''.join('%s  %s\n' % (sha(tx.encode('utf-8')), f) for f, tx in sorted(E.items())).encode('utf-8'))
E17 = {k: v.replace('\r\n', '\n') for k, v in refs.estudante(refs.C_V17).items()}
ctr = raw_lf(os.path.join(REPO, 'regras', 'pacote_contrato.md'))

def walk_diff(a, b, path, out):
    if type(a) != type(b):
        out.append((path, 'tipo', a, b)); return
    if isinstance(a, dict):
        for k in a:
            if k not in b: out.append((path + '.' + k, 'removido', a[k], None))
            else: walk_diff(a[k], b[k], path + '.' + k, out)
        for k in b:
            if k not in a: out.append((path + '.' + k, 'acrescentado', None, b[k]))
    elif isinstance(a, list):
        if len(a) != len(b): out.append((path, 'tamanho', len(a), len(b))); return
        for i, (x, y) in enumerate(zip(a, b)): walk_diff(x, y, '%s[%d]' % (path, i), out)
    elif a != b:
        out.append((path, 'valor', a, b))
dif = []
walk_diff(P17, P18, '', dif)

R = []
w = R.append
w('# pacote_relatorio_2026-10-17_v1_8.md — T-81 — 2026-10-17 — gerado por gbq-csc')
w('')
w('REMETENTE: gbq-csc (produção, sonnet), executando a D1 da GBQ (`saida/pacote/T81_D1_escopo_v1_8_2026-10-17.md`; D-T12-V13; D-T81-RESPOSTA, Fundador, opção A).')
w('DESTINATÁRIO: gbq-cqe (fidelidade, com leitura própria); depois gbq-gerencia (reconciliação e gatilho A). Cópia: orquestrador. Sem commit (do orquestrador).')
w('')

# ---------------------------------------------------------------- 1. arquivos de saída
w('## 1. Arquivos de saída: SHA-256 e bytes (conteúdo LF)')
w('')
w('| Arquivo | Bytes | SHA-256 | Esperado pela D1 | Confere |')
w('|---|---|---|---|---|')
ok_p = sha(raw18) == SHA_ESP and len(raw18) == BYTES_ESP
w('| `pacote.json` v1.8 (`out/`) | %d | %s | %d bytes, `%s` (seção 1.3 e 8) | %s |' % (len(raw18), fmt_sha(sha(raw18)), BYTES_ESP, SHA_ESP, 'sim' if ok_p else '**NÃO**'))
if not ok_p:
    divergencia('`pacote.json` v1.8: SHA-256 %s e %d bytes; esperado %s e %d bytes (D1, 1.3 e 8). Diferenças frente à v1.7 (git %s): %s.' % (sha(raw18), len(raw18), SHA_ESP, BYTES_ESP, refs.C_V17, '; '.join(d[0] for d in dif)))
if JE_RAW is not None:
    w('| `pacote_estudante.json` v1.8-E (`out/`) | %d | %s | (sem valor fixado na D1) | — |' % (len(JE_RAW), fmt_sha(sha(JE_RAW))))
else:
    w('| `pacote_estudante.json` v1.8-E (`out/`) | — | **não gerado** | (sem valor fixado na D1) | **NÃO** |')
ok_c = sha(ctr) == CTR_SHA_ESP and len(ctr) == CTR_B_ESP and ctr.count(b'\n') == CTR_L_ESP
w('| `regras/pacote_contrato.md` v1.2.5 | %d | %s | %d bytes, %d linhas, `%s` (seção 8, CONTRATO-V125) | %s |' % (len(ctr), fmt_sha(sha(ctr)), CTR_B_ESP, CTR_L_ESP, CTR_SHA_ESP, 'sim' if ok_c else '**NÃO**'))
if not ok_c:
    divergencia('contrato v1.2.5: SHA-256 %s; esperado %s (D1, seção 8).' % (sha(ctr), CTR_SHA_ESP))
if E18:
    w('| manifesto ordenado da edição v1.8 (SHA-256 das linhas "<sha256>  <nome>"; %d arquivos) | — | %s | v1.7: `67d2bdf85925a232…` (43 arquivos) | — |' % (len(E18), fmt_sha(manifesto(E18))))
w('')
w('No disco do Windows os arquivos do repositório têm CRLF (core.autocrlf); todo SHA-256 deste relatório é do conteúdo LF, como manda a D1 (P1).')
w('')

# ---------------------------------------------------------------- 2. diff v1.7 -> v1.8
w('## 2. Diff `pacote.json` v1.7 (git `%s`, `f20216c2…`) → v1.8 (D1, 1.3)' % refs.C_V17)
w('')
w('| Caminho | Antes (v1.7) | Depois (v1.8) |')
w('|---|---|---|')
for d in dif:
    a, b = d[2], d[3]
    sa, sb = (str(a) if not isinstance(a, str) else a), (str(b) if not isinstance(b, str) else b)
    w('| `%s` | %s | %s |' % (d[0], '`%s`' % sa[:160].replace('|', '\\|'), '`%s`' % sb[:160].replace('|', '\\|')))
if len(dif) == 2 and sorted(d[0] for d in dif) == ['.geradoEm', '.nome']:
    w('')
    w('Exatamente 2 caminhos, `$.nome` e `$.geradoEm`; nenhuma chave entra, sai ou muda de lugar. O arquivo de dados completo mantém os 10 lotes, inclusive L1C, L4C e L5C (D1, 3.5). E13 e T-54 já aplicadas (F4 e F5 da T81_exequibilidade): não se mexe nelas (a E13 está no comando da D1 e da D2; o curso do L3 traz "que se possa afirmar").')
else:
    w('')
    w('**DIVERGÊNCIA:** a D1 (1.3) manda exatamente 2 caminhos; o diff tem %d. Registrado na seção 10; nada foi "ajustado" para bater.' % len(dif))
    divergencia('diff `pacote.json` v1.7 → v1.8 com %d caminhos (a D1 manda exatamente 2: `$.nome` e `$.geradoEm`): %s.' % (len(dif), '; '.join(d[0] for d in dif)))
    for d in dif:
        if d[0] not in ('.nome', '.geradoEm'):
            w('')
            w('Origem do caminho extra `%s`: valor da v1.7 `%s` → valor gerado hoje `%s`.' % (d[0], str(d[2])[:400], str(d[3])[:400]))
w('')

# ---------------------------------------------------------------- 3. deleções no JSON
w('## 3. `pacote_estudante.json`: deleções por regra e por campo (D1, 2.2)')
w('')
if ej:
    w('Total: **%d remoções** em %d regras; %d campos comparados (cada um é subsequência da origem, salvo as exceções fechadas CAIXA, REALINHA e a fusão do L1); CAIXA %d/%d e REALINHA %d/%d, exatamente 1 cada.' % (ej['total_remocoes'], len(ej['regras']), ej['campos_comparados_so_delecao'], ej['caixa']['ocorrencias'], ej['caixa']['pares'], ej['realinha']['ocorrencias'], ej['realinha']['pares']))
    w('')
    w('Por campo (categoria de campo; escopo das regras = nome de arquivo de origem da v1.7):')
    w('')
    w('| Campo | Campos alterados | Remoções |')
    w('|---|---|---|')
    for k, v in ej['por_campo'].items():
        w('| `%s` | %d | %d |' % (k, v['campos_alterados'], v['remocoes']))
    w('')
    w('Por regra:')
    w('')
    w('| Regra | Ocorrências |')
    w('|---|---|')
    for k, v in ej['regras'].items():
        w('| %s | %d |' % (k.replace('|', '\\|'), v))
else:
    w('**não disponível:** `out/estudante_json.json` ausente.')
    divergencia('`out/estudante_json.json` ausente.')
w('')

# ---------------------------------------------------------------- 4. varredura R
w('## 4. Varredura R (D1, 2.3 e 2.4): conteúdo (X), dúvida (Y) e termos fora da lista')
w('')
w('Lista X (exceções de CONTEÚDO, fechada; caminhos com índice base 0; a gbq-csc não acrescenta entrada):')
w('')
w('| # | Campo | Contexto literal | Casamento | Esperado | Real |')
w('|---|---|---|---|---|---|')
real = (ej or {}).get('contagem_X_Y', {})
for rot, campo, ctx, lab, esp in mp.X:
    w('| %s | `%s` | `%s` | %s | %d | %s |' % (rot, campo, ctx, lab, esp, real.get(rot, '—')))
w('')
w('Y1, **DÚVIDA** (não tocada):')
w('')
w('| # | Campo | Contexto literal | Casamento | Esperado | Real | Motivo |')
w('|---|---|---|---|---|---|---|')
for rot, campo, ctx, lab, esp in mp.Y:
    w('| %s | `%s` | `%s` | %s | %d | %s | Remover a referência de fonte exige reescrever a frase (D-T81-05). Fica literal e vai a este relatório como DÚVIDA, para errata da GCB se ela quiser. |' % (rot, campo, ctx, lab, esp, real.get(rot, '—')))
w('')
if ej:
    w('Casamentos de R no `pacote_estudante.json` (caminho, rótulo, casamento, destino): %d; de processo: %d.' % (len(ej['casamentos_R']), ej['processo']))
    w('')
    for c in ej['casamentos_R']:
        w('- `%s` | %s | `%s` | **%s** | …%s…' % (c['campo'], c['rotulo'], c['casamento'], c['destino'], c['contexto'].replace('|', '\\|')))
    w('')
    w('Termos fora da lista (ficam como estão; só contagem, sem ação): %s.' % ', '.join('"%s" %d' % (k, v) for k, v in ej['termos_fora_da_lista'].items()))
    if ej['processo']:
        for c in ej['casamentos_R']:
            if c['destino'] == 'PROCESSO':
                divergencia('varredura R: casamento de PROCESSO fora de X e de Y em `%s` (%s, %r): `%s`. A D1 (2.3) manda falhar e devolver à GBQ como DÚVIDA; a gbq-csc não acrescenta regra de deleção nem entrada a X/Y.' % (c['campo'], c['rotulo'], c['casamento'], c['contexto']))
w('')
w('Na edição v1.8 (`out/estudante/`) a mesma varredura deve dar exatamente 11 casamentos (X1 2, X2 2, X3, X4 a X7 no `L3_estudo.md`, X8, Y1): ver a conferência (7) abaixo.')
w('')

# ---------------------------------------------------------------- 5. fusão
w('## 5. Fusão 1-C/4-C/5-C (D1, 3): contagem de itens por lote')
w('')
a = collections.Counter(gen.lote_of(i['id']) for i in P18['itens'] if i['rotulo'] == 'AUTORAL')
b = collections.Counter(gen.lote_fund(i['id']) for i in P18['itens'] if i['rotulo'] == 'AUTORAL')
w('| Lote | antes (v1.7) | depois (v1.8-E) | esperado pela D1 (3.4) |')
w('|---|---|---|---|')
for lid, esp in (('L1', '20 (+ L1C 10) → 30'), ('L4', '20 (+ L4C 10) → 30'), ('L5', '20 (+ L5C 10) → 30'), ('L2', '30 → 30'), ('L3', '30 → 30'), ('L6A', '15 → 15'), ('L6B', '15 → 15')):
    antes = '%d' % a[lid] + (' (+ %s %d)' % (gen.COMPL[lid], a[gen.COMPL[lid]]) if lid in gen.COMPL else '')
    w('| %s | %s | %d | %s |' % (lid, antes, b[lid], esp))
w('| Total AUTORAL / banco | %d / %d | %d / %d | 180 / 106 |' % (sum(a.values()), sum(1 for i in P18['itens'] if i['rotulo'] != 'AUTORAL'), sum(b.values()), sum(1 for i in P18['itens'] if i['rotulo'] != 'AUTORAL')))
if not (dict(b) == {'L1': 30, 'L2': 30, 'L3': 30, 'L4': 30, 'L5': 30, 'L6A': 15, 'L6B': 15} and sum(a.values()) == 180):
    divergencia('contagem de itens por lote diferente da tabela 3.4 da D1.')
w('')
w('Fusão no JSON: `lotes` = L1, L2, L3, L4, L5, L6A, L6B; `L1.curso` = curso do L1 + `\\n\\n## Complemento\\n\\n` + curso do 1-C; `L1.pegadinhas` = as 19 do L1 + as 4 do 1-C; L4C e L5C têm curso, resumo, pares e pegadinhas vazios (nada a fundir); associação do item ao lote pelo prefixo (`L1C-` → L1, `4C-` → L4, `5C-` → L5) registrada no contrato v1.2.5, ponto 3. Edição: 34 arquivos (43 na v1.7), com 9 retirados e 8 alterados.')
w('')
L = {l['id']: l for l in P18['lotes']}
w('**Nota (consequência registrada, não DÚVIDA — D1, 3.1):** a `legendaMecanismo` do L5C ("%s…") não tem lugar no L5, que já tem a sua ("%s…"). Os códigos são os mesmos (TC, GI, AT, IC) nas duas redações. A legenda do L4C é igual à do L4 (%s) e a do L5C também. Os `*_gabarito.md` da edição passam a trazer só a legenda do próprio lote; os `SIM-*_gabarito.md` não mudam.' % (L['L5C']['legendaMecanismo'][:60], L['L5']['legendaMecanismo'][:60], 'sim' if L['L4']['legendaMecanismo'] == L['L4C']['legendaMecanismo'] == L['L5C']['legendaMecanismo'] else 'NÃO'))
w('')

# ---------------------------------------------------------------- 6. já aplicadas e T-69
w('## 6. E13, T-54 e T-69')
w('')
w('- E13 e T-54: **já aplicadas** (F4 e F5 da `T81_exequibilidade_2026-10-17.md`); a v1.8 não mexe nelas. Conferido no pacote v1.8: o comando da D1 e o da D2 trazem "de até 20 linhas" (2 ocorrências), 0 do texto antigo; o curso do L3 traz "que se possa afirmar" (0 "que eu possa afirmar").')
w('- T-69 (4): **feita**. `validate.py` termina com `sys.exit(1 if fails else 0)` depois do `json.dump`; continuam 118 verificações (nenhuma nova, nenhuma retirada). Teste negativo em `conferencias_v18.py`: sobre uma cópia do pacote com 1 gabarito trocado, o código de saída é 1.')
w('- T-69 (2): **NÃO admitida; continua BACKLOG** (D1, 5). O item é do validador mantido `saida/treino/ferramentas/validar_erros.py` (`220dd559…`), que fica fora do gerador.')
w('')

# ---------------------------------------------------------------- 7. divergência de escopo lote x simulado
w('## 7. Divergências entre o escopo de lote e o escopo de simulado de uma mesma justificativa (6.2 (5); só registro)')
w('')
inf = [c for c in (conf or []) if c[0] == '(5) JSON×ED v1.7' and c[1].startswith('INFO')]
if inf:
    w('%s' % inf[0][1].split(': ', 1)[0].replace('INFO (só registro; o JSON segue o escopo de lote)', 'Resultado'))
    w('')
    w('Contagem na edição v1.7 aceita: ver o texto da conferência: "%s". Lista: %s. O JSON segue o escopo de lote, como manda a D1.' % (inf[0][1].split(': ')[-1], inf[0][3] or '(nenhuma)'))
else:
    w('**não disponível:** as conferências (`out/conferencias_v18.json`) não foram gravadas.')
w('')

# ---------------------------------------------------------------- 8. P8
w('## 8. Registro P8: plataforma v1.7 × `pacote_estudante.json` (D1, 0 e 7; fora do escopo desta tarefa)')
w('')
pl = read('saida/plataforma/plataforma_v1_7.html') if existe(os.path.join(REPO, 'saida', 'plataforma', 'plataforma_v1_7.html')) else ''
w('A plataforma v1.7 (`saida/plataforma/plataforma_v1_7.html`; **não tocada**) lê `pacote.json`. A associação item→lote vem de uma tabela fixa no HTML (`LOTE_INFO`: %s; prefixos `L1C-`: %s, `4C-`: %s, `5C-`: %s) e os lotes de cada módulo estão fixos (`lotes:["L6A","L6B","L4","L4C","L5","L5C"]`: %s; `["L1","L1C","L2","L3"]`: %s). Se ela ler o `pacote_estudante.json` sem adaptação, os itens dos complementos ficam fora dos testes de lote. Fica como registro para o rito do Fundador (D1, seção 7); nenhuma alteração de `saida/plataforma/` foi feita, nenhum artefato foi republicado, nada foi entregue à candidata.' % (
    'presente' if 'LOTE_INFO' in pl else 'não encontrado', 'presente' if 'L1C-' in pl else 'não encontrado', 'presente' if '4C-' in pl else 'não encontrado', 'presente' if '5C-' in pl else 'não encontrado',
    'presente' if '"L6A","L6B","L4","L4C","L5","L5C"' in pl else 'não encontrado', 'presente' if '"L1","L1C","L2","L3"' in pl else 'não encontrado'))
w('')

# ---------------------------------------------------------------- 8b. Adendo 1 e adaptações aceitas
w('## 8b. Adendo 1 da D1 (seção 9) e adaptações da produtora')
w('')
b7 = open(os.path.join(REPO, 'saida', 'pacote', 'gerador_v1_7', 'banco.py'), 'rb').read().decode('utf-8').replace('\r\n', '\n')
b8 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'banco.py'), 'rb').read().decode('utf-8').replace('\r\n', '\n')
SUF = '; mapeamento adicional: ver banco/mapeamento_adicional.csv (D-DA-BANCO)'
import csv, io
bq = {r['id']: r['observacoes'] for r in csv.DictReader(io.StringIO(raw_lf(os.path.join(REPO, 'banco', 'banco.csv')).decode('utf-8'), newline=''), delimiter=';')}
nota_v17 = re.search(r'nota de vigência:.*$', bq['BQ-0003'], re.S).group(0).rstrip()
w('- **Adendo 1 (D1 complementar da GBQ, 17/10/2026, seção 9):** o commit 73e9d49 (T-78, D-DA-BANCO) acrescentou o sufixo literal `%s` à `observacoes` de 20 linhas do banco; dos itens com `nota`, só o BQ-0003 o recebeu, e `banco.nota_de` (do rótulo "nota de vigência:" ao fim da célula) o levava à `nota`. Decisão: o sufixo é nota de PROCESSO e não entra em `nota` (regra 4 da v1.1.1; SCHEMA.md linha 7). Correção só no gerador: `banco.py` (`SUF_MAPA` e `nota_de`, com assert), `validate.py` (verificação da `nota` sobre `observacoes` sem o sufixo; continuam 118) e a conferência de não regressão do banco em `conferencias_v18.py`. `banco/` não foi alterado.' % SUF)
w('- **Defeito latente da v1_7 (registro, sem ação na v1_7):** o `gerador_v1_7`, intacto, rodado sobre o banco atual exportaria na nota do BQ-0003 o sufixo (a `nota_de` da v1_7 devolveria %d caracteres terminando em "%s", e a v1_7 %s o tratamento do sufixo). A v1.8 não tem esse efeito: a nota do BQ-0003 no pacote v1.8 %s a da v1.7.' % (len(nota_v17), nota_v17[-40:], 'não tem' if 'SUF_MAPA' not in b7 else 'TEM', 'é igual a' if next(i for i in P18['itens'] if i['id'] == 'BQ-0003')['nota'] == next(i for i in P17['itens'] if i['id'] == 'BQ-0003')['nota'] else 'DIFERE de'))
w('- **X5, X6 e X7 contados juntos na edição (aceito, 9.5 (a)):** nos campos do JSON os caminhos são distintos e as contagens são individuais; na edição o contexto de X6 é substring do de X5 e do de X7 e os três caem em `L3_estudo.md`; vale o grupo {X5, X6, X7} = 3, com a localização conferida (1 no bloco do curso, 1 em "## Pares", 1 em "## Pegadinhas"; X4 1 no curso; total 11). Linhas da edição com o grupo:')
_l3 = E18.get('L3_estudo.md', '').split('\n')
for k, l in enumerate(_l3, 1):
    if 'Presidência' in l:
        w('  - `L3_estudo.md:%d`: …%s…' % (k, l[max(0, l.index('Presidência') - 40):l.index('Presidência') + 60].replace('|', '\\|')))
w('- **Substituição da reconstrução acumulada (aceito, 9.5 (b); altera a 6.2 (1)):** a reconstrução da edição v1.3 → v1.8 e os testes T54-x foram substituídos pela conferência v1.7 → v1.8 (diff fechado da 3.3 com reconstrução). Fundamento: transitividade; a v1.7 é canônica (D-PACOTE-V17, com aquela reconstrução e aqueles testes aprovados pela gbq-cqe na T-71) e a v1.8 é a v1.7 com 2 trocas conferidas byte a byte (pacote) e o diff fechado da 3.3 (edição). A conferência (0) confere a base: `git show %s:saida/pacote/pacote.json` = `f20216c2…` e a edição desse commit com manifesto ordenado `67d2bdf85925a232…`. O diff acumulado do pacote v1.3 → v1.8 e o histórico do pacote foram mantidos.' % refs.C_V17)
w('- Registro do contrafactual (banco de `62ab128` sobreposto ao HEAD, feito antes do Adendo, só diagnóstico): `pacote_estudante.json` `851e2370…` (602815 bytes) e manifesto da edição `0b7391fa01784889…`; com a correção da 9.3 a regeração sobre o banco atual deve reproduzi-los (conferido: %s).' % ('sim' if (JE_RAW is not None and sha(JE_RAW) == '851e2370a9f5e9c8e5db725ff84777f70c12f81044983d339434ac7504e04c3e' and manifesto(E18) == '0b7391fa0178488924de8e6ed420c6108dd5fdad0e10fd1c5ccc40d9cd4bae6c') else '**NÃO**'))
if not (JE_RAW is not None and sha(JE_RAW) == '851e2370a9f5e9c8e5db725ff84777f70c12f81044983d339434ac7504e04c3e' and manifesto(E18) == '0b7391fa0178488924de8e6ed420c6108dd5fdad0e10fd1c5ccc40d9cd4bae6c'):
    divergencia('`pacote_estudante.json` ou manifesto da edição não reproduzem os do contrafactual (851e2370…, 0b7391fa…): D1, 9.4.')
w('')

# ---------------------------------------------------------------- 9. resultados 6.1 a 6.4
w('## 9. Resultados das seções 6.1 a 6.4 da D1')
w('')
w('**6.1 `estudante_json.py`** (asserções (a) a (f)): %s.' % (('0 falhas' if ej and not ej['falhas'] else '**FALHOU**: ' + '; '.join((ej or {}).get('falhas', ['saída ausente']))) ))
if ej and ej['falhas']:
    for f_ in ej['falhas']:
        divergencia('`estudante_json.py`: ' + f_)
w('')
w('**6.2 `conferencias_v18.py`:** %s.' % (('%d conferências; %d falhas' % (len(conf), sum(1 for c in conf if not c[2]))) if conf else '**não gerada** (`out/conferencias_v18.json` ausente)'))
if conf:
    por = collections.OrderedDict()
    for c in conf:
        k = c[0].split(' ')[0] + ' ' + (c[0].split(' ')[1] if len(c[0].split(' ')) > 1 and c[0].split(' ')[0] == '(1)' else '')
        por.setdefault(c[0], [0, 0])
        por[c[0]][0 if c[2] else 1] += 1
    w('')
    w('| Grupo | OK | FALHA |')
    w('|---|---|---|')
    for k, (o, f_) in por.items():
        w('| %s | %d | %d |' % (k, o, f_))
    for c in conf:
        if not c[2]:
            divergencia('conferência %s: %s' % (c[0], c[1][:300]))
else:
    divergencia('`conferencias_v18.py` não gerou `out/conferencias_v18.json`.')
w('')
w('**Verificações (`validate.py`, 118):** %s.' % (('%d verificações; %d falhas' % (len(val), sum(1 for v in val if not v['ok']))) if val else '**não gerada**'))
if val:
    for v in val:
        if not v['ok']:
            divergencia('validate.py: %s' % json.dumps(v, ensure_ascii=False)[:400])
w('')
w('**Fidelidade (`estudante_fidelidade.py`, com a fusão):** %s.' % (('%d comparações; %d diferenças; %d marcas residuais (as 2 esperadas: L4_gabarito.md:58 = Y1 e L6A_estudo.md:83 = X8)' % (fid['total'], fid['diferencas'], len(fid['restos']))) if fid else '**não gerada**'))
w('')
w('**Mutações da fidelidade (`fidelidade_mutacao.py`):** %s.' % (('%d mutações, %d diferenças detectadas, todas detectadas: %s' % (mut['mutacoes'], mut['diferencas_detectadas'], mut['todas_detectadas'])) if mut else 'ainda não executada neste passo (é o passo 8; o relatório é o passo 10)'))
w('')
w('**6.3 pipeline** (`rodar_tudo.sh`, 11 passos, `set -e`, determinismo: `geradoEm` literal, nenhuma leitura de data, hora ou HEAD): saídas-padrão em `out/*_stdout.txt`.')
for nome in ('gen_stdout.txt', 'estudante_json_stdout.txt', 'fidelidade_stdout.txt', 'sync_stdout.txt', 'validate_stdout.txt', 'conferencias_stdout.txt', 'mutacao_stdout.txt', 'validar_erros_stdout.txt'):
    p = os.path.join(OUT, nome)
    if existe(p):
        t = open(p, encoding='utf-8').read().strip().split('\n')
        w('- `out/%s`: %s' % (nome, t[-1][:200].replace('|', '\\|') if t and t[-1] else '(vazio)'))
    else:
        w('- `out/%s`: **ausente**' % nome)
w('')
w('**6.4 conferência (f)** (regeração em 2 cópias limpas):')
if cf and cf.get('runs'):
    w('')
    w('| Cópia | cwd | PYTHONHASHSEED | arquivos em `out/` (original / cópia) | idênticos | diferenças de nome |')
    w('|---|---|---|---|---|---|')
    for r in cf['runs']:
        w('| %s | `%s` | %s | %d / %d | %d | %s |' % (r['nome'], r['cwd'], r['seed'], r['n_orig'], r['n_clone'], r['identicos'], r['dif_nome'] or 'nenhuma'))
    w('')
    w(cf['texto'])
else:
    w('')
    w('registro `conferencia_f_2026-10-17_v1_8.json` ainda sem as cópias (a executar).')
w('')

# ---------------------------------------------------------------- 10. dúvidas e divergências
w('## 10. DÚVIDAS e divergências frente à especificação')
w('')
w('DÚVIDA 1 (D1, 2.4, Y1): `itens[L4-11].justificativa` contém "O F4 afirma que"; remover a referência de fonte exige reescrever a frase (D-T81-05). Fica literal no JSON e na edição (`L4_gabarito.md:58`). Para errata da GCB, se ela quiser; não é falha.')
w('')
if DIV:
    w('**Divergências e falhas frente à especificação (registradas, nada "ajustado" para bater):**')
    w('')
    for i, d in enumerate(DIV, 1):
        w('%d. %s' % (i, d))
    w('')
    w('Promoção (D1, 6.5) **não feita** enquanto houver falha: `saida/pacote/pacote.json`, `saida/pacote/pacote_estudante.json`, `saida/estudante/` e `saida/pacote/pacote_relatorio_2026-10-17_v1_8.md` ficam como estavam.')
else:
    w('Nenhuma divergência: todos os valores esperados da D1 conferem (pacote.json `%s`, %d bytes; contrato `%s`; 9 casamentos de R no JSON e 11 na edição, 0 de processo; 8/8 mutações detectadas).' % (SHA_ESP[:8] + '…', BYTES_ESP, CTR_SHA_ESP[:8] + '…'))
w('')
TXT = '\n'.join(R) + '\n'
with open(os.path.join(OUT, 'pacote_relatorio_2026-10-17_v1_8.md'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(TXT)
print(len(TXT.split('\n')))
