# -*- coding: utf-8 -*-
"""T-56 — relatório do pacote v1.3, gerado POR INTEIRO pelo gerador (N-3 / D-R2-02): todas as seções com as contagens da própria ocorrência.
Lê out/ (pacote.json, stats.json, validate.json, estudante_contagem.json, estudante_fidelidade.json, sync_check.txt, conferencias_v13.json,
fidelidade_mutacao.json) e as referências do git (refs.py). Grava out/pacote_relatorio_2026-10-13_v1_3.md; a promoção ao repositório é um passo explícito."""
import json, os, re, hashlib, collections, difflib, subprocess
import estudante_marcas as em
import estudante_gen as gen
import refs
from common import HERE as H, REPO, OUT
ROOT = REPO + '/'
def jl(nome): return json.load(open(os.path.join(OUT, nome), encoding='utf-8'))
new = jl('pacote.json')
old = refs.v11()          # v1.1 (git e97ab1f)
v12 = refs.v12()          # v1.2 (git 2684ab1; SHA-256 f46ed9f8…)
st = jl('stats.json'); val = jl('validate.json'); ec = jl('estudante_contagem.json'); fid = jl('estudante_fidelidade.json')
conf = jl('conferencias_v13.json'); mut = jl('fidelidade_mutacao.json'); volx = jl('varredura_volatil_v13.json')
sync = open(os.path.join(OUT, 'sync_check.txt'), encoding='utf-8').read()
RAW_NEW = open(os.path.join(OUT, 'pacote.json'), 'rb').read()
SIZE_NEW = len(RAW_NEW)
SHA_NEW = hashlib.sha256(RAW_NEW).hexdigest()
RAW_V12 = refs.git_show(refs.C_V12, refs.PACOTE); SIZE_V12 = len(RAW_V12); SHA_V12 = hashlib.sha256(RAW_V12).hexdigest()
RAW_V11 = refs.git_show(refs.C_V11, refs.PACOTE); SIZE_OLD = len(RAW_V11); SHA_OLD = hashlib.sha256(RAW_V11).hexdigest()
E12 = refs.estudante(refs.C_V12)
E13 = {f: open(os.path.join(OUT, 'estudante', f), encoding='utf-8').read() for f in sorted(os.listdir(os.path.join(OUT, 'estudante')))}
def manifesto(E): return hashlib.sha256(''.join('%s  %s\n' % (hashlib.sha256(tx.encode('utf-8')).hexdigest(), f) for f, tx in sorted(E.items())).encode('utf-8')).hexdigest()
MAN12, MAN13 = manifesto(E12), manifesto(E13)
NF = len(E13)
NVAL, NVF = len(val), sum(1 for v in val if not v['ok'])
NCONF, NCF = len(conf), sum(1 for c in conf if not c[2])
SEM_B13 = sum(len(re.findall(r'D-[A-Z]{2,}', tx)) for tx in E13.values())
GIT_HEAD = subprocess.run(['git', '-C', REPO, 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()

o = []
w = o.append
def sha(path):
    return hashlib.sha256(open(ROOT + path, 'rb').read()).hexdigest()[:12]
LOTES = [l['id'] for l in new['lotes']]
LOTE_OF = gen.lote_of

# ------------------------------------------------------------------ cabeçalho
w('# pacote_relatorio_2026-10-13_v1_3.md — T-56 — EXPORTAR v1.3 — 2026-10-13 — gerado por gbq-csc')
w('')
w('Saídas: `saida/pacote/pacote.json` (versao 1, nome "%s", geradoEm %s, %d bytes UTF-8, SHA-256 `%s`, indent=1, newline final), este relatório (gerado por inteiro pelo gerador, `relatorio_v1_3.py`, N-3) e a edição do estudante em `saida/estudante/` (%d arquivos). Contrato: `regras/pacote_contrato.md` v1.2.1 (inclusive a "Errata de forma da v1.2.1") + Regras da v1.2 (a–j) e as D1 da GBQ em `saida/pacote/T48_reconciliacao_R2_2026-10-13.md`, seção 2 (D-T53-01 a D-T53-08 e D-R2-01 a D-R2-06). Escopo desta ocorrência: D-V13-AGORA (Fundador, 13/10/2026) = lista PARA A PRÓXIMA T-12 (reconciliação R2, seção 4, itens 1 a 5) e pontos de caminho da `T55_conferencia_2026-10-13.md`, seção 4. Gerador: `saida/pacote/gerador_v1_3/` (cópia alterada de `gerador_v1_2/`, que ficou intacto). Nada foi commitado; TAREFAS.md, PARA_PRESIDENCIA.md, DECISOES.md, estado/, banco/, regras/ e os canônicos dos lotes não foram alterados. A v1.2 (SHA-256 `%s`, %d bytes) foi guardada antes de ser sobrescrita e é lida do git (commit %s). Nada deste pacote nem da edição do estudante vai à candidata sem decisão do Fundador; a edição do estudante NÃO é entrega à candidata (a entrega da v1.2 foi decidida em D-ENTREGA-V12-A; a da v1.3 continua reservada ao Fundador).' % (new['nome'], new['geradoEm'], SIZE_NEW, SHA_NEW, NF, SHA_V12, SIZE_V12, refs.C_V12))
w('')
w('Resultado em uma linha: **%d itens** (%d de banco + %d AUTORAL), %d lotes (6 com `legendaMecanismo`), %d discursivas, %d simulados com `n` e `versao` (SIM-0 com `avisos`); %d registros de errata (%d APLICADA, %d JÁ PRESENTE, 0 NÃO ENCONTRADA) e 6 erratas com alvo fora do pacote; validação por script: %d verificações, %d falhas; conferências da ocorrência: %d, %d falhas; edição do estudante: %d arquivos, fidelidade textual %d comparações, %d diferenças. Diff v1.2 → v1.3 do pacote: só `nome` e os campos novos `legendaMecanismo` (6 lotes) e `avisos` (SIM-0); da edição: só N-1 (`L6B_estudo.md`), a legenda no topo de 6 `*_gabarito.md` e a versão no README.' % (len(new['itens']), sum(1 for i in new['itens'] if i['rotulo'] != 'AUTORAL'), sum(1 for i in new['itens'] if i['rotulo'] == 'AUTORAL'), len(new['lotes']), len(new['discursivas']), len(new['simulados']), len(st['errata']), sum(1 for e in st['errata'] if e['estado'] == 'APLICADA'), sum(1 for e in st['errata'] if e['estado'] == 'JÁ PRESENTE'), NVAL, NVF, NCONF, NCF, NF, fid['total'], fid['diferencas']))
w('')

# ------------------------------------------------------------------ 1. fontes
w('## 1. Fontes')
w('')
w('Lidas em 13/10/2026 (SHA-256, 12 primeiros dígitos). O arquivo canônico de cada lote é o da tabela de fonte do contrato (regra 4 da v1.1); os `saida/lote*/RECONCILIADO.md` não existem e não são fonte.')
w('')
w('| Objeto | Arquivo(s) | Versão / observação | SHA-256 (12) |')
w('|---|---|---|---|')
FONTES = [
 ('Contrato', 'regras/pacote_contrato.md', 'v1.2.1 (Errata de forma, T-53) + Regras da v1.2 (a–j) + v1.1.1 + v1.1'),
 ('Instruções da T-48', 'saida/banco/GBQ_reconciliacao_2026-10-13.md', 'seção "INSTRUÇÕES PARA A T-48" e D1-a/b/c'),
 ('Escopo da T-56', 'saida/pacote/T48_reconciliacao_R2_2026-10-13.md', 'seção 2 (D1: D-T53-01 a 08, D-R2-01 a 06) e seção 4 (PARA A PRÓXIMA T-12, itens 1 a 5)'),
 ('Escopo da T-56', 'saida/pacote/T55_conferencia_2026-10-13.md', 'seção 4 (pontos de caminho do gerador)'),
 ('Tabela 2.3 (legendas)', 'saida/pacote/QA_T53_2026-10-13_gbq-cqe.md', 'literais de legendaMecanismo por lote e dos avisos'),
 ('Varreduras 3.5', 'saida/pacote/QA_T48_R2_2026-10-13_gbq-cqe.md', 'seção 3.5 (varreduras de não regressão) e N-1'),
 ('Reconciliação R1', 'saida/pacote/T48_reconciliacao_R1_2026-10-13.md', 'D-R1-xx e C-01 a C-25 (exceções fechadas)'),
 ('L1', 'saida/gce/GCE_Lote1_v2_CPP.md', 'v2 canônico; erratas pela consolidação'),
 ('L1', 'saida/gce/GCE_Lote1_consolidacao_GCE.md', 'E1–E12 (Adendos 1–5); padrão D1'),
 ('L1C', 'saida/gce/GCE_Lote1C_v2_CPP.md', 'v2 canônico'),
 ('L1C', 'saida/gce/GCE_Lote1C_consolidacao_GCE.md', 'E1–E4'),
 ('L2', 'saida/gce/GCE_Lote2_v2_CPP.md', 'v2 canônico'),
 ('L2', 'saida/gce/GCE_Lote2_consolidacao_GCE.md', 'E1–E7'),
 ('L2', 'saida/gce/GCE_Lote2_padroes_GCE.md', 'padrões D2 e D3'),
 ('L3', 'saida/gce/GCE_Lote3_v2_CPP.md', 'v2 canônico, com a T-44 já gravada (título e nota do 3.1)'),
 ('L3', 'saida/gce/GCE_Lote3_consolidacao_GCE.md', 'E1–E4 e Adendo 2 (Ato nº 225)'),
 ('L3', 'saida/gce/GCE_Lote3_padroes_GCE.md', 'padrões D4 e D5'),
 ('L4', 'saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md', 'v3.4 (cabeçalho: Despacho 9, 09/10/2026); linha "Legenda:" → legendaMecanismo'),
 ('L4C', 'saida/gcb/GCB_Lote4C_v1_GCB-CPP.md', 'v1.1 (só itens AUTORAL); "Legenda:" → legendaMecanismo'),
 ('L5', 'saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md', 'v3.2 (errata Tukey, T-47, já gravada; D-TRANSPORTE-L5-V32); "Legenda:" (forma "Mecanismos:") → legendaMecanismo'),
 ('L5C', 'saida/gcb/GCB_Lote5C_v1_GCB-CPP.md', 'v1.1 (só itens AUTORAL); "Legenda:" → legendaMecanismo'),
 ('L6A', 'saida/gcb/GCB_Lote6a_v2_producao_auto.md', 'v2 (T-17); "Legenda:" ("atribuição errada (AT)") → legendaMecanismo'),
 ('L6B', 'saida/gcb/GCB_Lote6b_v2_producao_auto.md', 'v2 com errata A-6b-1 (T-17); "Legenda:" ("atribuição errada (AT)") → legendaMecanismo'),
 ('Banco', 'banco/banco.csv', '112 linhas; colunas texto_comando, texto_base, aderencia (T-29/T-42, D1-b)'),
 ('SIM-0', 'saida/simulados/simulado_0_v0.2.md', 'v0.2 com o ajuste T-36; seção "Avisos de montagem" (avisos 1, 2 e 4) → avisos'),
 ('SIM-0', 'saida/simulados/simulado_0_v0.2_gabarito.md', 'gabarito e mapa'),
 ('SIM-1', 'saida/simulados/simulado_1.md', 'v1 (sem versão declarada)'),
 ('SIM-1', 'saida/simulados/simulado_1_gabarito.md', ''),
 ('SIM-2', 'saida/simulados/simulado_2.md', 'v1 (D-SIM2-CANONICO)'),
 ('SIM-2', 'saida/simulados/simulado_2_gabarito.md', ''),
 ('SIM-0-P2', 'saida/simulados/simulado_0_P2.md', 'v1 (D-SIM0P2-DIAGNOSTICO)'),
 ('SIM-0-P2', 'saida/simulados/simulado_0_P2_gabarito.md', ''),
 ('Registro AUTORAL', 'saida/gbq/claude_GBQ_Registro_AUTORAL_v3.md', 'v3 (180 itens; gabarito, subitem, [TS], VOLÁTIL)'),
 ('Edital', 'edital/TI_itens_1_4_P1.md', 'texto literal'),
 ('Edital', 'edital/TI_itens_5_8_P1.md', 'texto literal'),
 ('Edital', 'edital/modulo_RF_IA_P2.md', 'texto literal'),
 ('Relatório anterior', 'saida/pacote/pacote_relatorio_2026-10-13.md', 'relatório da v1.2 (R0 + seção 13 da R1; substituído por este)'),
 ('Relatório anterior', 'saida/pacote/pacote_relatorio_2026-10-10.md', 'base de comparação (v1.1)'),
]
for obj, f, ob in FONTES:
    w('| %s | `%s` | %s | `%s` |' % (obj, f, ob, sha(f)))
w('| v1.1 | `git show %s:saida/pacote/pacote.json` | referência de comparação, lida do git | `%s` |' % (refs.C_V11, SHA_OLD[:12]))
w('| v1.2 (antes) | `git show %s:saida/pacote/pacote.json` | pacote canônico da D-PACOTE-V12, guardado antes de sobrescrever (cópia no scratchpad e no git) | `%s` |' % (refs.C_V12, SHA_V12[:12]))
w('| Edição do estudante v1.2 (antes) | `git archive %s saida/estudante` | %d arquivos; manifesto ordenado (SHA-256 das linhas "<sha>  <nome>") | `%s` |' % (refs.C_V12, len(E12), MAN12[:12]))
w('')
w('Condições do contrato (regra 5 e instrução da T-48), que continuam válidas: T-13, T-25, T-29, T-36, T-38, T-42, T-43, T-44, T-46 e T-47 CONCLUÍDAS e reconciliadas; T-40 CONCLUÍDA (BQ-0072, 0077, 0084, 0109, 0110 e 0111 entram, com 6/6 gabaritos sustentados). Simulados canônicos por D-SIM1-CANONICO, D-SIM2-CANONICO e D-SIM0P2-DIAGNOSTICO; SIM-0 v0.2 sem pendência (T-36 aplicada). T-48 e T-53 CONCLUÍDAS (reconciliação R2); T-55 CONCLUÍDA (gerador persistido). Nenhuma errata nem texto canônico de lote ou de simulado mudou desde a v1.2: a v1.3 só acrescenta o que a lista da T-12 manda. Liberar qualquer simulado à candidata continua reservado ao Fundador.')
w('')

# ------------------------------------------------------------------ 2. contagens
def cnt(p):
    it = p['itens']
    b = [i for i in it if i['rotulo'] != 'AUTORAL']; a = [i for i in it if i['rotulo'] == 'AUTORAL']
    c = lambda L, g: sum(1 for i in L if i['gabarito'] == g)
    return dict(n=len(it), rot=collections.Counter(i['rotulo'] for i in it), b=b, a=a,
                C=c(it, 'C'), E=c(it, 'E'), bC=c(b, 'C'), bE=c(b, 'E'), aC=c(a, 'C'), aE=c(a, 'E'),
                dir=sum(1 for i in it if i['aderencia'] == 'direta'), par=sum(1 for i in it if i['aderencia'] == 'parcial'),
                bdir=sum(1 for i in b if i['aderencia'] == 'direta'), bpar=sum(1 for i in b if i['aderencia'] == 'parcial'),
                vol=sum(1 for i in it if i.get('volatil')), bvol=sum(1 for i in b if i.get('volatil')), avol=sum(1 for i in a if i.get('volatil')),
                nota=sum(1 for i in it if i.get('nota')), co=sum(1 for i in it if i.get('comandoOriginal')),
                tbv=sum(1 for i in it if i['textoBase'] == ''), tbn=sum(1 for i in it if i['textoBase'] == 'nenhum'),
                tbt=sum(1 for i in it if i['textoBase'] not in ('', 'nenhum')))
O, M, N = cnt(old), cnt(v12), cnt(new)
w('## 2. Contagens v1.1 → v1.2 → v1.3')
w('')
w('| Medida | v1.1 | v1.2 | v1.3 |')
w('|---|---|---|---|')
def tri(f):
    a, b, c = f(old, O), f(v12, M), f(new, N)
    return (a, b, c)
npg = lambda p: sum(len(l['pegadinhas']) for l in p['lotes'])
rows = [
 ('`versao` / `nome`',) + tri(lambda p, c: '1 / "%s"' % p['nome']),
 ('`geradoEm`',) + tri(lambda p, c: p['geradoEm']),
 ('edital (entradas)',) + tri(lambda p, c: len(p['edital'])),
 ('itens (total)',) + tri(lambda p, c: c['n']),
 ('itens CEBRASPE_ANALOGA (banco)',) + tri(lambda p, c: c['rot']['CEBRASPE_ANALOGA']),
 ('itens AUTORAL',) + tri(lambda p, c: c['rot']['AUTORAL']),
 ('gabarito C / E (total)',) + tri(lambda p, c: '%d / %d' % (c['C'], c['E'])),
 ('gabarito C / E (banco)',) + tri(lambda p, c: '%d / %d' % (c['bC'], c['bE'])),
 ('gabarito C / E (AUTORAL)',) + tri(lambda p, c: '%d / %d' % (c['aC'], c['aE'])),
 ('aderência direta / parcial (total)',) + tri(lambda p, c: '%d / %d' % (c['dir'], c['par'])),
 ('aderência direta / parcial (banco; AUTORAL todos direta)',) + tri(lambda p, c: '%d / %d' % (c['bdir'], c['bpar'])),
 ('`volatil: true` (total; banco + AUTORAL)',) + tri(lambda p, c: '%d (%d + %d)' % (c['vol'], c['bvol'], c['avol'])),
 ('`nota` (itens)',) + tri(lambda p, c: '%d (%s)' % (c['nota'], ', '.join(i['id'] for i in p['itens'] if i.get('nota'))) if c['nota'] else 0),
 ('`comandoOriginal` (itens)',) + tri(lambda p, c: c['co']),
 ('`textoBase` "nenhum" / "" / texto',) + tri(lambda p, c: '%d / %d / %d' % (c['tbn'], c['tbv'], c['tbt'])),
 ('lotes / discursivas',) + tri(lambda p, c: '%d / %d' % (len(p['lotes']), len(p['discursivas']))),
 ('lotes com `legendaMecanismo` (opcional, v1.2.1 ponto 4)',) + tri(lambda p, c: '%d (%s)' % (sum('legendaMecanismo' in l for l in p['lotes']), ', '.join(l['id'] for l in p['lotes'] if 'legendaMecanismo' in l)) if any('legendaMecanismo' in l for l in p['lotes']) else 0),
 ('pegadinhas (total)',) + tri(lambda p, c: npg(p)),
 ('simulados',) + tri(lambda p, c: '%d (%s)' % (len(p['simulados']), ', '.join(s['id'] for s in p['simulados']))),
 ('simulados `n`',) + tri(lambda p, c: ' / '.join(str(s.get('n', '—')) for s in p['simulados'])),
 ('simulados com `avisos` (opcional, v1.2.1 ponto 5)',) + tri(lambda p, c: '%s (%d avisos)' % (', '.join(s['id'] for s in p['simulados'] if 'avisos' in s), sum(len(s['avisos']) for s in p['simulados'] if 'avisos' in s)) if any('avisos' in s for s in p['simulados']) else 0),
 ('bytes', SIZE_OLD, SIZE_V12, SIZE_NEW),
 ('SHA-256 (12)', SHA_OLD[:12], SHA_V12[:12], SHA_NEW[:12]),
]
for r in rows: w('| %s | %s | %s | %s |' % r)
w('')
w('A v1.3 é a v1.2 (R1, SHA-256 `%s`) mais `nome`, `legendaMecanismo` e `avisos`: as medidas de itens, simulados, lotes e discursivas são idênticas (seção 13, conferência (5)). Banco: 112 linhas em `banco/banco.csv`; 106 exportadas (60 C / 46 E) e 6 excluídas por anulação (gabarito X): %s. Os 60 itens da v1.1 mantêm o mesmo `comando` e a mesma aderência (37 direta / 23 parcial, conferido); os 46 novos são BQ-0061… do terceiro lote de varredura (inclui BQ-0072, 0077, 0084, 0109, 0110 e 0111, liberados pela T-40). BQ-0049 a 0051 são os únicos com `textoBase` (a coluna `texto_base`); nos 283 demais `textoBase` é `""` (F2).' % (SHA_V12[:12], ', '.join(x[0] for x in st['binfo']['excl'])))
w('')
w('### 2.1 Itens por lote (AUTORAL) e `comandoOriginal`')
w('')
w('| Lote | AUTORAL | C | E | `volatil` | `comandoOriginal` | pegadinhas v1.1 → v1.3 | pares |')
w('|---|---|---|---|---|---|---|---|')
ol = {l['id']: l for l in old['lotes']}
for l in new['lotes']:
    its = [i for i in new['itens'] if i['rotulo'] == 'AUTORAL' and LOTE_OF(i['id']) == l['id']]
    w('| %s | %d | %d | %d | %d | %d | %d → %d | %d |' % (l['id'], len(its), sum(1 for i in its if i['gabarito'] == 'C'), sum(1 for i in its if i['gabarito'] == 'E'),
      sum(1 for i in its if i.get('volatil')), sum(1 for i in its if i.get('comandoOriginal')), len(ol[l['id']]['pegadinhas']), len(l['pegadinhas']), len(l['pares'])))
w('')
w('`volatil` no banco (8): %s. Em AUTORAL (15): %s. Total 23; os AUTORAL são os VOLÁTIL + REVERIFICAR normativo do registro GBQ v3 (regra R1-N), com L3-Q21.' % (', '.join(st['binfo']['vol']), ', '.join(i['id'] for i in new['itens'] if i['rotulo'] == 'AUTORAL' and i.get('volatil'))))
w('')
w('### 2.2 Simulados (regra (e): `n` e `versao`)')
w('')
w('| id | nome | tipo | `versao` | `n` | itens | C / E | `volatil` | parcial | `avisos` |')
w('|---|---|---|---|---|---|---|---|---|---|')
itd = {i['id']: i for i in new['itens']}
for s in new['simulados']:
    its = [itd[x] for x in s['itens']]
    w('| %s | %s | %s | %s | %d | %d | %d / %d | %d | %d | %s |' % (s['id'], s['nome'], s['tipo'], s['versao'], s['n'], len(s['itens']),
      sum(1 for i in its if i['gabarito'] == 'C'), sum(1 for i in its if i['gabarito'] == 'E'), sum(1 for i in its if i.get('volatil')), sum(1 for i in its if i['aderencia'] == 'parcial'), len(s['avisos']) if 'avisos' in s else '—'))
w('')
w('`n` = tamanho da lista `itens` em 4/4. `avisos` (v1.2.1 ponto 5): só o SIM-0, com os avisos 1, 2 e 4 da folha canônica, literais (seção 13.2). `versao`: SIM-0 "v0.2" (cabeçalho do arquivo); SIM-1, SIM-2 e SIM-0-P2 "v1" (sem versão declarada, regra (e)). Nenhum simulado final contém item `volatil` ou `parcial`. O gabarito de cada posição do simulado (arquivos `*_gabarito.md`) é igual ao `gabarito` do item no pacote em 165/165 posições (60 + 40 + 40 + 25).')
w('')
w('### 2.3 Discursivas')
w('')
w('D1–D5 idênticas às da v1.1 e da v1.2 (nada mudou nas 5): D1 questão (L1), D2 questão e D3 peça (L2), D4 questão e D5 peça (L3). Aspectos e quesitos conferidos: soma dos aspectos das questões 14,30 + 0,70 de apresentação = 15,00; peças 28,50 + 1,50 = 30,00. A observação "inferido pela EXEC" da D1 (Adendo 4) não é exportada: 0 ocorrência de "EXEC" nas discursivas. D3 e D5 são pareceres técnicos (gênero confirmado para analista e técnico; hipótese por analogia para o Cargo 11). Pesos por quesito são HIPÓTESE do Projeto.')
w('')

# ------------------------------------------------------------------ 3. erratas
w('## 3. Erratas (consolidações sincronizadas) — estado por errata')
w('')
w('Método: substituição exata do trecho "onde se lê" (X) pelo "leia-se" (Y), tolerante a quebra de linha, na ordem do arquivo; cada X deve ter exatamente 1 ocorrência livre (não contida em Y). Estados: **APLICADA** (X encontrado 1 vez e trocado por Y); **JÁ PRESENTE** (X ausente e Y já presente na fonte); **NÃO ENCONTRADA** (nem X nem Y: o script aborta); **FORA DO PACOTE** (o alvo da errata não é exportado; checado: X/Y não vão ao JSON). O gerador aborta em qualquer falha; **0 NÃO ENCONTRADA**. Conferência prévia: `sync_check` leu cada X/Y contra o texto da consolidação sincronizada em `saida/gce/` (resultado: %s, %d linhas).' % ('TUDO OK' if 'RESULTADO: TUDO OK' in sync else 'FALHA', sum(1 for l in sync.split(chr(10)) if l.startswith('L'))))
w('')
DESC = {
 ('L1', 'E1'): 'Q07 (d): "diarização habilitada, por si só, sem amostras de voz de referência"',
 ('L1', 'E2'): 'Q08 (d): "e um sistema pode diarizar"',
 ('L1', 'E3'): 'Q11 (d): "e, eventualmente, de pistas prosódicas"',
 ('L1', 'E4a'): 'curso 1.1: WER "no cálculo usual, sobre texto normalizado…"',
 ('L1', 'E4b'): 'curso 1.1: "no cálculo usual ele ignora pontuação, e em qualquer convenção ignora locutores"',
 ('L1', 'E4c'): '(d-G) Q01 (justificativa): "No cálculo usual, pontuação e capitalização ficam fora do WER…"',
 ('L1', 'E5'): 'resumo (b), "CLM (texto; indisponível para pt-BR na AWS)"',
 ('L1', 'E9'): 'curso 1.2: espectrograma "em geral (por exemplo, no Whisper)"',
 ('L1', 'E10'): 'curso 1.8: "departamento de registro da Câmara (Derep, antigo DETAQ; Ato da Mesa nº 251/2026)"',
 ('L1', 'E12'): 'resumo (b), WER: "no cálculo usual, sobre texto normalizado, não mede pontuação nem capitalização; locutor fica fora…" (T-46)',
 ('L1C', 'E1'): '(d-G) justificativa: reforço por LLM não implica áudio como modalidade do próprio LLM',
 ('L1C', 'E3'): '(d) Q23 (enunciado): "end-to-end, não há dicionário de pronúncias separado"',
 ('L2', 'E1a-curso'): 'curso 2.6: "traduz as notas… em texto"',
 ('L2', 'E1b-resumo'): 'resumo 2.6: "traduz as notas estenotípicas em texto"',
 ('L2', 'E1c-par15'): 'par 15: "(traduz as notas estenotípicas em texto)"',
 ('L2', 'E1d-dgQ21'): '(d-G) justificativa de Q21 (G2 da T-44)',
 ('L2', 'E2'): 'curso: acréscimo "Lista variável conforme a consulta à página (08/10/2026)."',
 ('L2', 'E3b'): 'curso: "foi observada nas notas oficiais de 2026 (N1)"',
 ('L2', 'E5'): 'curso: acréscimo da definição de aparte (RICD, art. 176)',
 ('L2', 'E6'): 'curso: acréscimo (RICD, art. 176: interrupção…)',
 ('L2', 'E7'): 'resumo 2.4: "Forma de identificar o orador: observada nas notas oficiais de 2026 (N1; E3)…"',
 ('L3', 'E1a'): 'curso 4.1: § 3º "consta como vetado na página compilada, com remissão à VEP nº 288/2019"',
 ('L3', 'E1b'): 'resumo (b), linha 4.1: art. 20, "expressão suprimida (MP nº 869/2018, convertida na Lei 13.853/2019)"',
 ('L3', 'E2'): 'curso 4.1: "o art. 5º, II, enumera origem"',
 ('L3', 'E3a'): 'curso 4.1: "a MP nº 869/2018, convertida na Lei 13.853/2019, suprimiu a expressão"',
 ('L3', 'E3b'): '(d-G) Q20 (justificativa): idem, "da redação original"',
 ('L3', 'E4'): 'par 20: "(redação original, suprimida pela MP nº 869/2018, convertida na Lei 13.853/2019)"',
 ('L3', 'Adendo 2 (3.1)'): 'Ato da Mesa nº 225/2025 no curso 3.1',
 ('L3', 'Adendo 2 (4.1)'): 'Ato da Mesa nº 225/2025 no curso 4.1 ("Contexto institucional")',
 ('L1', 'F5'): 'F5: "Derep, antigo DETAQ" → "Derep (antigo DETAQ)" (depois da E10)',
 ('L1', 'E7a'): 'D1 padrão, quesito 2.3: "[valor máximo: 5,30]"',
 ('L1', 'E7b'): 'D1 padrão, nota de correção: "(5,00 / 4,00 / 5,30), mais 0,70 de apresentação"',
}
ORDER = [('L1', k) for k in ['E1','E2','E3','E4a','E4b','E4c','E5','E7a','E7b','E9','E10','E12','F5']] + \
        [('L1C', 'E1'), ('L1C', 'E3')] + \
        [('L2', k) for k in ['E1a-curso','E1b-resumo','E1c-par15','E1d-dgQ21','E2','E3b','E5','E6','E7']] + \
        [('L3', k) for k in ['E1a','E1b','E2','E3a','E3b','E4','Adendo 2 (3.1)','Adendo 2 (4.1)']]
byk = {(e['lote'], e['id']): e for e in st['errata']}
w('| Lote | Errata | Alvo | Estado | Nota |')
w('|---|---|---|---|---|')
NOTE = {
 ('L1', 'E4c'): 'Y começa com maiúscula porque X abre a frase (como na v1.1)',
 ('L2', 'E2'): 'consolidação diz "acrescentar": X = frase-âncora; o acréscimo foi conferido',
 ('L2', 'E5'): 'idem ("acrescentar")',
 ('L2', 'E6'): 'idem ("acrescentar")',
 ('L3', 'E3a'): 'o X tem 2 ocorrências no texto bruto; 1 depois da E1b (aplicação em sequência), que é a que a errata visa',
 ('L3', 'E1b'): 'o Y usa aspas duplas do arquivo (a consolidação escreve aspas simples)',
 ('L1', 'F5'): 'aplicada depois da E10',
 ('L1', 'E7a'): 'E7 também insere a linha "Apresentação e estrutura textual: 0,70"',
}
n_ap = n_ja = 0
for lote, k in ORDER:
    e = byk[(lote, k)]
    w('| %s | %s | %s | %s | %s |' % (lote, k, DESC[(lote, k)], e['estado'], (e['note'] or NOTE.get((lote, k), ''))))
    n_ap += e['estado'] == 'APLICADA'; n_ja += e['estado'] == 'JÁ PRESENTE'
w('| L1 | E8 | D1 (comando): preâmbulo "Ao domínio do conteúdo serão atribuídos até 15,00 pontos…" e [valor: 5,00/4,00/5,30 pontos] por alínea | APLICADA | montagem da D1; resultado idêntico ao da v1.1 |')
w('| L3 | T-44 | título e nota do curso 3.1; G1/G2 (erratas D1 de 10/10) | JÁ PRESENTE | gravada em `GCE_Lote3_v2_CPP.md`; o pacote lê o arquivo atual (v1.1 ainda trazia "ERRATA T-08" e "registro da GCB-CQFP", ver seção 5) |')
w('| L5 | T-47 (Tukey) | curso 8.2, "Bigodes e outliers": "O fator 1,5·AIQ é a convenção usual (Tukey)…" | JÁ PRESENTE | gravada em `GCB_Lote5_v3_canonica_GCB-CPP.md`; o pacote lê o arquivo atual (+102 caracteres no curso do L5) |')
w('')
w('Totais: os registros de substituição do gerador são %d (%d APLICADA e %d JÁ PRESENTE, a única sendo o Adendo 2 no 3.1); 0 NÃO ENCONTRADA. As três últimas linhas da tabela (E8, T-44, T-47) são informativas: E8 é a montagem da D1 (APLICADA, sem substituição) e T-44 e T-47 já estavam gravadas nos arquivos canônicos (JÁ PRESENTE); somadas, a tabela tem %d linhas, das quais %d APLICADA ou JÁ PRESENTE por substituição do gerador. Para cada APLICADA o script confere depois que Y consta do JSON e X não consta (fora das ocorrências de Y): validação "erratas: Y presente / X ausente", OK.' % (len(st['errata']), n_ap, n_ja, len(ORDER) + 3, len(st['errata'])))
w('')
w('### 3.1 Erratas cujo alvo não é exportado (estado FORA DO PACOTE)')
w('')
w('| Lote | Errata | Onde fica o alvo | Verificação |')
w('|---|---|---|---|')
import p2
for e in p2.NAO_EXPORTADAS:
    w('| %s | %s | %s | %s |' % (e['lote'], e['id'], e['onde'], 'alvo existe na fonte; X/Y não vão ao JSON' if e.get('x') else 'sem texto-âncora; checado por varredura do JSON'))
w('')
w('L1 E11 (Adendo 4): o texto "Motivo" do Adendo (E7/E8) só existe na consolidação; o que vai ao pacote (comando e padrão da D1) não contém "14,30" (validado). A confirmação do Adendo 4 sobre os itens do edital da D1 ("CONFIRMADO o que a EXEC inferiu, P2-1.4, P2-1.6 e P2-1.7") não é exportada (0 "EXEC" nas discursivas).')
w('')
w('### 3.2 Adendo 2 — Ato da Mesa nº 225/2025 (decisão)')
w('')
w('- **Curso 3.1: JÁ PRESENTE, não duplicado.** O bloco "CONTEXTO NORMATIVO INTERNO (SEM ITEM)" (T-08, com o título e a nota da T-44) já resume o Ato nº 225 no 3.1 (art. 3º, I, III, V, VIII, IX; art. 4º, IV). Inserir o Adendo 2 ali duplicaria o conteúdo; o instruído pela T-48 foi justamente "sem duplicar o bloco já aplicado pela T-08".')
w('- **Curso 4.1: APLICADA.** O texto literal do Adendo 2, com o título "Contexto institucional — Ato da Mesa nº 225, de 15/12/2025…", foi inserido ao fim do 4.1, antes de "--- 4.2" (%d caracteres). Ocorre 1 vez no curso do L3; conferido que é igual ao Adendo 2 da consolidação.' % len(st['adendo2']))
w('')

# ------------------------------------------------------------------ 4. F1-F5
w('## 4. F1 a F5 e D1-b/D1-c')
w('')
w('- **F1 (L1-Q04 "áudio–texto"): feita, 1 junção.** O arquivo canônico tem o travessão (en dash) no fim da linha ("áudio–" / "texto"); a quebra virava espaço ("áudio– texto"). A regra do gerador passou a juntar sem espaço quando uma linha termina em en dash colado a letra. Resultado: `enunciado` de L1-Q04 = "…pares áudio–texto para treinamento…"; 0 "áudio– texto" no JSON; nenhuma outra sequência letra+"– "+letra no JSON (validado). É a única alteração de `enunciado` da v1.1 para a v1.2.')
w('- **F2 (`textoBase` vazio): feita.** `textoBase` = `""` em 283 de 286 itens (a v1.1 tinha "nenhum" em 237); 0 "nenhum"; texto literal só em BQ-0049, 0050 e 0051 (coluna `texto_base`).')
w('- **F3 (pegadinhas, uma por entrada, com `rotulo`): feita**, ver seção 8.')
w('- **F4 (marcas internas das justificativas): feita em %d justificativas** (18 da R0 mais 6B-06, 6B-15 e L2-Q21 acrescentadas na correção R1; D-R1-02, D-R1-03 e D-R1-20), ver seção 6.' % len(st['f4']))
w('- **F5 ("Derep (antigo DETAQ)"): feita.** 1 substituição no L1 (curso 1.8, E10 já com a forma "Derep, antigo DETAQ" → "Derep (antigo DETAQ)"); %d "Derep, antigo DETAQ" no JSON; a forma correta ocorre %d vezes no JSON e nenhuma outra grafia de DETAQ fora dela.' % (RAW_NEW.decode('utf-8').count('Derep, antigo DETAQ'), len(re.findall(r'Derep \(antigo DETAQ\)', RAW_NEW.decode('utf-8')))))
w('- **D1-b (aderência explícita): feita.** Todo item de banco recebe `aderencia` da coluna do `banco.csv`, sem recálculo (106/106 iguais à coluna: 67 direta / 39 parcial). A regra por texto de `observacoes` deixou de valer para a exportação.')
w('- **D1-c (comando normalizado + `comandoOriginal`): feita em 90 itens** (L4 20, 4C 10, A5/L5 20, 5C 10, 6A 15, 6B 15; L1–L3 e banco: 0). Regex `(?i)(julgue os itens) (?:de )?(?:[0-9A-Z]+-)?\\d+ a (?:[0-9A-Z]+-)?\\d+\\.` → "julgue os itens a seguir."; o resto da frase fica literal e o literal vai em `comandoOriginal`. Conferido: só o trecho da numeração muda; BQ-0070, 0071 e 0112 ficam com o comando inteiro e sem `comandoOriginal`; nenhum comando restante com faixa de itens.')
w('')

# ------------------------------------------------------------------ 5. diff por lote
w('## 5. Diff textual resumido v1.1 → v1.3 por lote')
w('')
w('Campos de lote comparados caractere a caractere (difflib), v1.1 (git %s) contra a v1.3. O diff v1.2 → v1.3 é menor: os campos de texto dos lotes (`resumo`, `curso`, `pares`, `pegadinhas`, `itensEdital`) são idênticos (conferência (1), seção 13); o único acréscimo é `legendaMecanismo` em 6 lotes. Campos não citados: idênticos.' % refs.C_V11)
w('')
ol = {l['id']: l for l in old['lotes']}
for l in new['lotes']:
    lid = l['id']; rows = []
    for f in ('resumo', 'curso'):
        a, b = ol[lid][f], l[f]
        if a != b:
            sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
            ops = [(t, a[i1:i2], b[j1:j2]) for t, i1, i2, j1, j2 in sm.get_opcodes() if t != 'equal']
            rows.append((f, len(a), len(b), ops))
    # pares
    parch = ol[lid]['pares'] != l['pares']
    w('**%s**' % lid)
    if not rows and not parch and len(ol[lid]['pegadinhas']) == len(l['pegadinhas']) and ol[lid]['itensEdital'] == l['itensEdital']:
        w('- resumo, curso, pares e itensEdital idênticos; pegadinhas: mesma contagem (%d), agora com `rotulo`.' % len(l['pegadinhas']))
    for f, la, lb, ops in rows:
        w('- %s: %d → %d caracteres, %d operações:' % (f, la, lb, len(ops)))
        for t, x, y in ops:
            if t == 'delete': w('  - remove "%s"' % x.replace('\n', '⏎')[:160])
            elif t == 'insert': w('  - insere "%s"' % y.replace('\n', '⏎')[:160])
            else: w('  - troca "%s" por "%s"' % (x.replace('\n', '⏎')[:100], y.replace('\n', '⏎')[:100]))
    if parch:
        n_diff = sum(1 for a_, b_ in zip(ol[lid]['pares'], l['pares']) if a_ != b_)
        w('- pares: %d pares; %d com texto alterado.' % (len(l['pares']), n_diff))
        for a_, b_ in zip(ol[lid]['pares'], l['pares']):
            if a_ != b_:
                sm = difflib.SequenceMatcher(None, a_['como'], b_['como'], autojunk=False)
                for t, i1, i2, j1, j2 in sm.get_opcodes():
                    if t != 'equal': w('  - "%s": %s "%s" → "%s"' % (a_['a'][:40], t, a_['como'][i1:i2][:80], b_['como'][j1:j2][:120]))
    if len(ol[lid]['pegadinhas']) != len(l['pegadinhas']):
        w('- pegadinhas: %d → %d entradas (desdobramento da F3, com as reuniões da errata v1.2.1 ponto 2 quando houve), todas com `rotulo`.' % (len(ol[lid]['pegadinhas']), len(l['pegadinhas'])))
    if 'legendaMecanismo' in l:
        w('- `legendaMecanismo` (novo na v1.3): "%s".' % l['legendaMecanismo'])
    w('')
w('Itens (campo a campo, v1.1 → v1.3): `textoBase` 237 (F2, "nenhum" → ""), `comando` 90 e `comandoOriginal` 90 (D1-c), `justificativa` %d (F4), `nota` 2 (BQ-0003, BQ-0040), `enunciado` 1 (L1-Q04, F1). `gabarito`, `aderencia` (nos 60 da v1.1), `itemEdital`, `rotulo`, `certame`, `cargo`, `ano`, `numero` e `url`: 0 diferença. Discursivas: 0 diferença. Edital: igual. Da v1.2 para a v1.3, nenhum item muda.' % len(st['f4']))
w('')

# ------------------------------------------------------------------ 6. F4
w('## 6. F4 — justificativas alteradas (antes / depois)')
w('')
w('Só deleção (conferido por difflib: nenhuma inserção nem troca, salvo as duas trocas de caixa fechadas da C-05, em 4C-08 e 5C-06, "Lição O10: o item" → "O item" e "Lição O10: a regra" → "A regra", D-R1-04); cada trecho a apagar ocorre exatamente 1 vez; depois da deleção, sem espaço duplo nem espaço antes de pontuação; 0 marca de processo (CQFP/CQE/CPP/GCE/GCB/GBQ/EXEC, T-xx, "(vN", Oxx, "Lição", R-4C1, "Risco", QA, O-n, "Retificação", "Gabarito C|E mantido") remanescente nas 180 justificativas AUTORAL. **%d justificativas**: as 17 da GBQ são as justificativas com os tipos de marca que ela listou (CQFP, "(v3 — O12)", "(O1)", "Lição O10", "R-4C1", "Risco"); a 18.ª é a 5C-03 ("R-5C1", mesma classe de R-4C1); com a rodada R1 (6B-06, 6B-15, L2-Q21) a F4 soma %d (gcb-cqfp O-2; D-R1-20).' % (len(st['f4']), len(st['f4'])))
w('')
for e in st['f4']:
    w('**%s**' % e['id'])
    w('- antes: %s' % e['antes'])
    w('- depois: %s' % e['depois'])
    w('- apagado: %s' % ' | '.join('"%s"' % d for d in e['deletado']))
    w('')

# ------------------------------------------------------------------ 7. método TS/VOL
w('## 7. Método de contagem de [TS] e VOLÁTIL')
w('')
w('Contados **somente nas seções de itens e gabaritos** dos arquivos canônicos: a linha de cada item da seção (d-G) dos lotes GCE e da seção de itens/gabarito dos lotes GCB (formato "C — [TS] — v3 — 5.1 — TC (…)" ou "E [TS]. …"), onde a marca vem logo depois da letra do gabarito. Ficam de fora, por não serem item: o cabeçalho, a Tabela de Correções, a legenda ("[TS] = troca sutil de conceito; VOLÁTIL = …") e os adendos, que citam as palavras sem marcar item (no L3 a T-44 trocou as menções do cabeçalho por "troca sutil, volatilidade", justamente para a contagem bruta por grep refletir só os itens). Cada item lido é conferido contra o registro GBQ v3.')
w('')
w('| Lote | [TS] | VOLÁTIL (+REVERIFICAR) | itens VOLÁTEIS |')
w('|---|---|---|---|')
for lid in LOTES:
    w('| %s | %d | %d | %s |' % (lid, len(st['ts'][lid]), len(st['volreg'][lid]), ', '.join(st['volreg'][lid]) or '—'))
w('| **Total** | **%d** | **%d** | |' % (sum(len(v) for v in st['ts'].values()), sum(len(v) for v in st['volreg'].values())))
w('')
w('Resultado: 91 [TS] (registro v3: 91) e 15 VOLÁTIL em AUTORAL (registro: 15), 180/180 sem divergência. [TS] não é campo do pacote nem aparece em texto exportado (0 ocorrência de "[TS]" no JSON); `volatil: true` é a única marca exportada.')
w('')

# ------------------------------------------------------------------ 8. pegadinhas
w('## 8. Pegadinhas (F3, regra (d))')
w('')
w('Uma pegadinha por entrada, no formato `{itemEdital, rotulo, texto}`. **`rotulo`**: título do bloco ou subseção que contém a linha "Pegadinha"/"Pegadinha provável", sem numeração inicial e sem marcas, cortado em " — " quando o título tem aposto; quando a pegadinha está direto sob um item que é id do edital, o texto do edital do `itemEdital`; no L6A, sob o título do item do lote (WORD, EXCEL, POWERPOINT, ONEDRIVE, CORREIO ELETRÔNICO…, MICROSOFT TEAMS, GOOGLE MEET). **Desdobramento** só nas fronteiras marcadas pelo texto: enumeradores "(1)", "(2)"… (precedência) ou ";" fora de parênteses e de aspas; assertivas `"…" → ERRADO (…; …)` não se desdobram. A junção dos fragmentos com o separador original reproduz cada entrada da v1.1 (salvo o ponto final): validado em todas as entradas.')
w('')
w('| Lote | entradas v1.1 → v1.3 | modos de origem (entradas da v1.1) |')
w('|---|---|---|')
modo = collections.defaultdict(collections.Counter)
for e in st['peg']: modo[e['lote']][e['modo']] += 1
for l in new['lotes']:
    w('| %s | %d → %d | %s |' % (l['id'], len(ol[l['id']]['pegadinhas']), len(l['pegadinhas']), ', '.join('%s %d' % (k, v) for k, v in modo[l['id']].items()) or '—'))
w('')
w('Texto corrido que não se separa sem reescrever (ficou como uma entrada só, por contrato): L1 P2-1.1, P2-1.2, P2-1.4 e P2-1.7 (frases soltas "Outra:", "Também:", sem separador marcado). Enumeradores cujo conteúdo tem ";" interno ficaram íntegros (precedência do enumerador): L1 P2-1.3 (1), L2 P2-2.6 (6) e L3 P2-4.3 (2). Assertiva única com ";" dentro do parêntese, mantida inteira: L6A, slide mestre (`"…" → ERRADO (guia Exibir; F7) — VOLÁTIL`). L4, L6A e L6B já tinham uma pegadinha por entrada (contagem igual).')
w('')
w('**Reuniões da errata v1.2.1 ponto 2 (fragmento que só se lê com o verbo ou o sujeito do anterior, ou que ilustra o anterior; D-R1-05, D-R1-06; C-06 a C-08): %d fragmentos reunidos, todos com o separador original "; ":**' % len(st['merge']))
w('')
for frag, motivo in st['merge']:
    w('- "%s" — %s' % (frag, motivo))
w('')
dep = []
for l in new['lotes']:
    prev = None
    for i, g in enumerate(l['pegadinhas']):
        k = (g['itemEdital'], g['rotulo'])
        if k == prev and re.match(r'^(que|empilhado)\b', g['texto']):
            dep.append((l['id'], i, g['rotulo'], g['texto']))
        prev = k
w('Fragmentos que dependem do verbo ou do sujeito do fragmento anterior e ficaram como entrada própria: **%d** (na R0 eram 5, resolvidos pelas reuniões acima; contagem de pegadinhas 267 → 262). Os fragmentos de L5 que restam começam por infinitivo e se leem soltos; L1 P2-1.6 e P2-1.8 começam por minúscula mas se leem sozinhos (fronteira mantida).' % len(dep))
w('')

# ------------------------------------------------------------------ 9. validação
w('## 9. Validação por script (%d verificações, %d falhas)' % (len(val), sum(1 for v in val if not v['ok'])))
w('')
for v in val:
    w('- %s %s%s' % ('OK' if v['ok'] else '**FALHA**', v['n'], (' — ' + str(v['extra'])[:200]) if v['extra'] and v['extra'] not in ('[]',) else ''))
w('')

# ------------------------------------------------------------------ 10. estudante
w('## 10. Edição do estudante (`saida/estudante/`)')
w('')
w('Gerada a partir do `pacote.json` v1.3 (fonte única). **%d arquivos**, os mesmos nomes da v1.2: `README.md` (índice, versão v1.3, data %s, aviso "material de estudo; gabaritos em arquivo separado"); por lote, `<ID>_estudo.md` (itens do edital, resumo, curso, pares, pegadinhas com rótulo), `<ID>_itens.md` (texto-base se houver, comando e enunciado, nessa ordem; sem gabarito, justificativa nem marcas) e `<ID>_gabarito.md` (gabarito, item do edital e justificativa; **no topo, a `legendaMecanismo` literal do lote, nos 6 lotes que a têm**) para L1, L1C, L2, L3, L4, L4C, L5, L5C, L6A e L6B (30 arquivos); `BANCO_itens.md` e `BANCO_gabarito.md` (certame, cargo, ano, número, URL oficial, aviso VOLÁTIL e `nota` literal, sem o identificador de decisão); por simulado `<SIM>_folha.md` (sem o id de origem dos itens) e `<SIM>_gabarito.md` (SIM-0, SIM-1, SIM-2, SIM-0-P2); `DISCURSIVAS.md` e `DISCURSIVAS_padrao.md`. Resumo e curso vão em blocos de texto cercados, para preservar quebras, recuos e tabelas. **Os `avisos` do SIM-0 não são exibidos** (D-T53-02/item 3 da lista: até decisão do Fundador sobre o que se compartilha com a candidata); a fidelidade confere que o texto dos três avisos não aparece em arquivo algum.' % (NF, new['geradoEm']))
w('')
w('**Regra:** as marcas internas saem SOMENTE POR DELEÇÃO (nunca reescrita) por `estudante_marcas.py` e `literais.py`, com as exceções fechadas da reconciliação R1: (i) CAIXA (C-05 e C-15): minúscula → maiúscula da primeira letra de um trecho, lista de 8 pares só em `L6A_estudo` (e as 2 trocas de caixa na F4 do pacote); (ii) reunião de fragmentos de pegadinha com "; " (C-06 a C-08, só no pacote); (iii) a `nota` de BQ-0003 sai da edição sem " (D-LEI-15352)" (C-18; errata v1.2.1 ponto 3), só na exibição. A marca VOLÁTIL vira, nos itens `volatil: true`, o aviso fixo "Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027."; a `nota` (BQ-0003, BQ-0040) é exibida junto do item. Enunciado, comando e texto-base de item não são tocados (afirmado por teste: nenhuma marca da lista neles). **Novidade da v1.3 (N-1, D-R2-01):** duas regras literais, só em `L6B_estudo`, apagam "Nesta produção " e " (a especificação previa o item \"se houver base\")" do curso 4.0.2 (o "NÃO" que segue já tem inicial maiúscula); no pacote a marca fica, por desenho (D-PACOTE-V11). Regras genéricas (por tipo) e regras literais (frase ou cláusula a apagar, `⟦…⟧` na especificação; %d regras literais vigentes, apêndice A):' % len(em.LITERAL))
w('')
w('- `[V dd/mm/aaaa — …]` apagado inteiro, com o espaço anterior (o colchete pode quebrar linha entre "[V" e a data); duas exceções que mantêm a orientação ao estudante: `[V … — F4; NORMATIVO — QA; norma de caráter experimental, não cobrar o texto]` fica `[norma de caráter experimental, não cobrar o texto]` e `[V … contexto histórico]` fica `[contexto histórico]`.')
w('- `[NORMATIVO — QA: base legal]` perde o prefixo e o colchete e fica a base legal ("LGPD, art. 5º, I."); `[NORMATIVO — QA]` e as variantes com ";" são apagadas (`[NORMATIVO — QA; não cobrar além do texto]` fica `[não cobrar além do texto]`); a frase "…com a marca [NORMATIVO — QA]. Fontes: F1 … lidas em 08/10/2026." do L3 sai, ficando "Todos os dispositivos abaixo estão em paráfrase."')
w('- Referências de fonte F1…F22: `[Fn]`, `(Fn)`, `(Fn, Fm)`, `(Fn, verificado em …)`, `(Fn, seção …)`, `, Fn)` no fim de parêntese, `; Fn)`, `(Fn: ` e `(Fn, "…")` (mantém o parêntese e o conteúdo), "Conforme a Fn (leitura de …):", frases "Fonte(s): Fn, …verificado em …." e, em trechos de prosa, a cláusula ou palavra que só existe por causa da referência (lista completa no apêndice A). "A tecla F4" (Excel) NÃO é referência e permanece; a frase restaurada da L4-11 ("O F4 afirma que …") permanece (D-R1-07, opção (a)).')
w('- Agentes e unidades (CQFP, QA, GCB, GCE, CPP) em carimbos como "(conferido pela CQFP em 08/10/2026)", "conforme a CQFP", "(GCB-CPP)", "Decisão da GCE", "versão da CPP", "para o QA Normativo", "Síntese da CQFP … colado pelo Fundador"; ids internos "(errata E1)", "; E3" em "(N1; E3)", "(O11)", "(D-T2)", "(R4 do Projeto)" e, nos padrões D4/D5, "(GCE, R2–R4)" e os enumeradores "R2. ", "R3. ", "R4. ".')
w('- Carimbos datados ligados a uma referência apagada ("verificadas em 7/10/2026", "(reverificado em …)", "conforme a leitura de 08/10/2026", "(conferido no Planalto em …)") e, na R1, "aberta(s) hoje" (9 pontos, L6A e L6B), "(v2, …)" no L1C (2), " neste chat" no L4 (1), classificação interna de VOLÁTIL nas justificativas (4), carimbo "Verificado em 8/10/2026" do L5 (4).')
w('- Códigos de fonte do L5 (U1–U6, GG4, TB2; só `L5_*`, 33 remoções) e códigos de nota N do L2 e do L3 (`(N1)`, `Ver N5:` etc.; só `L2_*` e `L3_*`, 14 remoções); os códigos N1–N4 do L4 ficam (definidos no próprio texto).')
w('')
w('### 10.1 Marcas removidas por tipo e por arquivo')
w('')
w('Contagem de ocorrências apagadas, por arquivo gerado (um item presente em lote e em simulado é contado nos dois arquivos). Total nos arquivos: **%d**.' % sum(ec['total'].values()))
w('')
w('| Tipo | Ocorrências |')
w('|---|---|')
for k, v in sorted(ec['total'].items(), key=lambda x: -x[1]):
    w('| %s | %d |' % (k, v))
w('| **Total** | **%d** |' % sum(ec['total'].values()))
w('')
w('| Arquivo | Total | Detalhe por tipo |')
w('|---|---|---|')
for f, c in sorted(ec['por_arquivo'].items()):
    w('| %s | %d | %s |' % (f, sum(c.values()), '; '.join('%s %d' % (k, v) for k, v in sorted(c.items(), key=lambda x: -x[1]))))
w('')
w('Referência: na v1.2 as remoções somaram 569; a v1.3 soma %d (as 2 a mais são as da N-1, em `L6B_estudo.md`).' % sum(ec['total'].values()))
w('')
w('Arquivos sem nenhuma remoção: os `*_itens.md`, `BANCO_*`, `*_folha.md`, `README.md` e os `*_gabarito.md` cujos itens não tinham marca (a tabela só lista os arquivos com remoção).')
w('')
w('### 10.2 Fidelidade (script `estudante_fidelidade.py`)')
w('')
w('O script lê os %d arquivos com um parser próprio (independente do gerador) e confere, campo a campo, o texto do estudante com o do pacote: (1) igual ao texto do pacote com as deleções das regras; (2) obtido do texto do pacote só por deleção (difflib: apenas `equal`/`delete`, salvo as 8 trocas de caixa da lista CAIXA, C-15); (3) comando, texto-base, enunciado, gabarito, item do edital, aderência, nota (com a única exceção da C-18), aviso VOLÁTIL, certame, cargo, ano, número, URL, ordem e `n` dos simulados, valores dos aspectos e conceitos dos quesitos idênticos ao pacote; (4) **v1.3:** a `legendaMecanismo` de cada lote com o campo está literal, sozinha, no topo do `*_gabarito.md` do próprio lote (antes do primeiro item) e em nenhum outro arquivo; lote sem o campo não tem texto antes do primeiro item; o texto dos `avisos` não aparece na edição. Teste negativo (`fidelidade_mutacao.py`: mutação de %d arquivos — um enunciado, um gabarito, um trecho de curso e uma legenda) detectou %d diferenças em %s, portanto o script não é cego.' % (NF, mut['mutacoes'], mut['diferencas_detectadas'], ', '.join('`%s`' % a for a in mut['arquivos_com_diferenca'])))
w('')
w('- comparações: %s (total %d)' % (', '.join('%s %d' % (k, v) for k, v in fid['comparacoes'].items()), fid['total']))
w('- **diferenças: %d** (texto do estudante == texto do pacote com as deleções aplicadas)' % fid['diferencas'])
def motivo_resto(r):
    return 'tecla do Excel, não é referência' if r[0].startswith('L6A_estudo') else 'sujeito da frase restaurada da L4-11 (exceção registrada, D-R1-07 opção (a))'
w('- marcas residuais nos arquivos pela varredura de higiene (V, NORMATIVO — QA, [TS], CQFP/CQE/CPP/GCE/GCB/GBQ/EXEC, F1…F22, T-/R-/E-/O-xx, "(errata En)"): %d, a saber: %s.' % (len(fid['restos']), '; '.join('%s linha %s "%s" (%s)' % (r[0], r[1], r[2], motivo_resto(r)) for r in fid['restos'])))
w('')

# ------------------------------------------------------------------ 11. varredura residual
w('## 11. Marcas que permanecem (varredura)')
w('')
def count_rx(p, rx):
    n = 0
    for path, t in __import__('texts').walk(p):
        if path == '.nome': continue
        n += len(re.findall(rx, t))
    return n
w('**No `pacote.json` (por desenho):** curso, resumo, pegadinhas e justificativas AUTORAL conservam as marcas de processo do arquivo canônico, porque o pacote é dado, não edição do estudante (decisão do gatilho A: só a edição do estudante as retira, e a F4 limpou apenas as 18 justificativas com marca de agente/risco/lição). Contagem no JSON: `[V …]` %d; `[NORMATIVO — QA…]` %d; referências F1…F22 %d; CQFP/CPP/GCE/GCB/QA em texto de lote %d.' % (count_rx(new, r'\[V\s+\d'), count_rx(new, r'\[NORMATIVO — QA'), count_rx(new, r'\bF\d{1,2}\b'), count_rx(new, r'\b(?:CQFP|CPP|GCE|GCB)\b') - count_rx({'x': [i['url'] for i in new['itens']]}, r'\b(?:CQFP|CPP|GCE|GCB)\b')))
w('')
w('**Na edição do estudante** as varreduras da seção 3.5 do QA da R2 dão 0 (conferência (4), seção 13): `;)`, ` — $`, `****`, `abertas? hoje`, `(v2,`, `D-LEI-15352`, `neste chat`, `Retificação`, `Gabarito [CE] mantido`, códigos U/GG/TB/CI, códigos N (L1, L1C, L2, L3, SIM-2, SIM-0-P2), ` — <id>` nas folhas, `erificado em 8/10/2026` (L5); mais [TS], `[V `, CQFP/CQE/GCE/GCB/GBQ/CPP, `T-n`, QA, `O-n`, "Lição O", `R-nCn`, "NÃO VOLÁTIL", "Sem marca VOLÁTIL", REVERIFICAR e `\\bD-XX`; e, da N-1, "Nesta produção" e "especificação previa".')
w('')
w('**Permanecem na edição, por decisão da reconciliação (D1 da GBQ):** `a tecla F4` (`L6A_estudo.md` 83) e `O F4 afirma que …` (`L4_gabarito.md`, L4-11; D-R1-07); "VOLÁTIL" fora do aviso fixo em %d linhas de títulos, rubricas e orientação de estudo (%s; D-R1, 2.3-g); etiquetas GI/TC/AT/IC nas justificativas (2.3-h), **agora com a legenda literal do lote no topo do `*_gabarito.md` dos 6 lotes que a têm**; códigos N1–N4 do L4 (2.3-e); `(Derep (antigo DETAQ); …)` no `L1_estudo.md` (literal pela F5; D-R1-15 DESCARTADO); 29 justificativas iniciadas em minúscula depois do prefixo de campo (forma do canônico; D-R1-18 DESCARTADO); "que eu possa afirmar" em `L3_estudo.md` 422 (texto canônico da GCE; 2.3-i, BACKLOG); remissões a pares por id não exportado ("par C1", "par C14", "C19") em justificativas de A5-09, 5C-03, 5C-07 e 4C-08 (D-R1-21, BACKLOG); referentes perdidos em deleções (L6A 135 "As duas páginas"; L5 seção/módulo; 6B-06; L3 101/574; QA R2 N-5, BACKLOG, aditamento à T-54); nota R2 da D4 repetida na D5 e rótulo "Nota: nota de vigência:" (D-R1-17); quadro-síntese do L1 desalinhado e separador "×" dos pares (D-R1-14/16, BACKLOG). **Os avisos 1, 2 e 4 do SIM-0 saíram do "adiado" da R1 para o pacote** (campo `avisos`), mas continuam fora da edição (decisão do Fundador).' % (len(volx['volatil_fora_do_aviso']), '; '.join('%s:%d' % tuple(x) for x in volx['volatil_fora_do_aviso'])))
w('')

# ------------------------------------------------------------------ 12. DUVIDAS
w('## 12. DÚVIDAS para a GBQ')
w('')
w('**DÚVIDAS da v1.2 (R0), decididas na reconciliação R1 (`T48_reconciliacao_R1_2026-10-13.md`, tabela 2.2) e fechadas na R2 (`T48_reconciliacao_R2_2026-10-13.md`, D-R2-06):**')
w('')
w('| DÚVIDA (R0) | Decisão que a resolve | Efeito nesta ocorrência |')
w('|---|---|---|')
DR0 = [
 ('1 — F4: 18 em vez de 17', 'D-R1-02, D-R1-03, D-R1-20 (aceitar as 18; com 6B-06, 6B-15 e L2-Q21, 21)', 'F4 = %d justificativas (seção 6)' % len(st['f4'])),
 ('2 — minúscula depois de "Lição O10: "', 'D-R1-04 (capitalização autorizada, C-05)', '2 trocas de caixa na F4 do pacote (4C-08, 5C-06)'),
 ('3 — fragmentos dependentes / entradas não desdobradas', 'D-R1-05, D-R1-06 (C-06 a C-08); errata v1.2.1 ponto 2', 'pegadinhas 262 (seção 8)'),
 ('4 — rótulo por hierarquia', 'tabela 2.2 (aceitar)', 'rótulos literais mantidos'),
 ('5 — marcas fora da lista', 'tabela 2.3 (C-17 a C-23), só na edição', 'seção 10; apêndice A'),
 ('6 — "Risco"', 'tabela 2.2 (confirmar; conteúdo de estudo)', 'sem mudança'),
 ('7 — conteúdo substantivo perdido', 'D-R1-07 (restaurar a frase da L4-11)', 'frase restaurada na edição'),
 ('8 — minúscula e sujeito oculto no L6A', 'D-R1-11, D-R1-12 (C-15, C-16)', '8 trocas de caixa; 3 deleções'),
 ('9 — tabelas de colunas fixas', 'D-R1-16 (BACKLOG)', 'sem mudança'),
 ('10 — aviso único para REVERIFICAR normativo', 'tabela 2.3 (f), C-21', 'classificação interna apagada'),
 ('11 — aderência no gabarito do estudante', 'tabela 2.2 (manter só no gabarito)', 'sem mudança'),
 ('12 — quarto estado "FORA DO PACOTE"', 'tabela 2.2 (aceitar como rótulo de relatório)', 'seção 3.1'),
 ('13 — alvo duplicado da E3a do L3', 'tabela 2.2 (aceitar)', 'sem mudança'),
]
for a, b, c in DR0: w('| %s | %s | %s |' % (a, b, c))
w('')
w('**DÚVIDAS desta ocorrência (v1.3), cada uma com a decisão que a resolve; nenhuma impede o aceite:**')
w('')
D = [
 ('Forma de exibição da `legendaMecanismo`.', 'No topo de cada `L<lote>_gabarito.md` com o campo, como uma linha própria, o literal do canônico sem rótulo novo ("Mecanismo: troca de conceito (TC), …" ou "Mecanismos: TC troca de conceito; …"), seguida de linha em branco. Acrescentar um título ("Legenda") seria texto novo. Remissão: D-T53-01 (leitura conservadora, sem texto novo); extensão aos `SIM-*_gabarito.md` e `BANCO_gabarito.md` é BACKLOG (D-T53-01). Se a GBQ quiser moldura, decide em D1.'),
 ('Aviso 2 do SIM-0 remete a uma marca ausente da folha.', 'A string do aviso 2 no campo `avisos` diz que cada item parcial traz, logo abaixo, a marca `[ADERÊNCIA PARCIAL ...]`, e o aviso 1 traz "(D-ADERENCIA: parcial só em diagnóstico)". Ambos ficam literais no campo (v1.2.1 ponto 5). Remissão: D-T53-03 e D-T53-07 (BACKLOG, condicionados à decisão do Fundador de exibir os avisos; a deleção mínima, se exibir, é só "D-ADERENCIA: " no aviso 1).'),
 ('Varredura `D-[A-Z]{2,}` da seção 3.5 do QA da R2 sem `\\b`.', 'Sem fronteira de palavra o padrão casa dentro de "TID-IA", "TID-DADOS-VIZ" (títulos dos lotes) e "END-TO-END": %d ocorrências, as mesmas da v1.2. A conferência usa `\\bD-[A-Z]{2,}` (0 ocorrência). Sem decisão a tomar; proposta: DESCARTADO. Remissão: QA_T48_R2, seção 3.5 (resultado 0 lido com fronteira de palavra).' % SEM_B13),
]
for i, (t_, d) in enumerate(D, 14):
    w('%d. **%s** %s' % (i, t_, d))
w('')

# ------------------------------------------------------------------ apêndice A
# ------------------------------------------------------------------ 13. ocorrência v1.3
w('## 13. Ocorrência v1.3 (T-56)')
w('')
w('Ocorrência antecipada da T-12 (D-V13-AGORA, Fundador, 13/10/2026), com o gerador de `saida/pacote/gerador_v1_2/` copiado para `saida/pacote/gerador_v1_3/` (a v1.2 ficou intacta). Despacho: PROMPT DE PARTIDA lido com as Regras da v1.2 (a)–(j), a errata v1.2.1 (pontos 1–5) e as D1 da GBQ da reconciliação R2, seção 2 (D-T53-02, item 4 da lista).')
w('')
w('### 13.1 Itens da lista PARA A PRÓXIMA T-12 (reconciliação R2, seção 4) e pontos de caminho da T-55 (seção 4)')
w('')
w('| Item | Como foi feito | Onde se confere |')
w('|---|---|---|')
w('| 1 — N-1 (D-R2-01) | deleção pura em `L6B_estudo.md` (curso 4.0.2): "Nesta produção " e " (a especificação previa o item \\"se houver base\\")"; só na edição; o pacote conserva a marca (D-PACOTE-V11). 2 regras literais novas (apêndice A, últimas) | conferência (3), seção 13.3 |')
w('| 2 — N-3 (D-R2-02) | este relatório é gerado por inteiro por `relatorio_v1_3.py`, com as contagens da v1.3 em todas as seções; o Apêndice A lista só as regras vigentes (sem as nº 6, 26 e 63 da R0, retiradas na R1; as nº 42, 44 e 51 da R0 na forma da C-16; mais as regras do item 1); as DÚVIDAS novas levam remissão à decisão que as resolve (seção 12) | seções 1 a 12 e Apêndice A |')
w('| 3 — T-53 pontos 4 e 5 (D-T53-01) | `legendaMecanismo` em L4, L4C, L5, L5C, L6A e L6B, literal do canônico de cada lote (tabela 2.3 do QA da T-53); `avisos` no SIM-0 (avisos 1, 2 e 4 literais da folha, aviso 2 com a sublista em 3 espaços de recuo); legenda exibida só no topo dos `L<lote>_gabarito.md` desses 6 lotes; `avisos` não exibidos na edição | conferências (1), (3), validação |')
w('| 4 — A-2 (D-T53-02) | `nome` "Câmara 2026 — pacote F4 (v1.3)", `versao` 1, `geradoEm` %s (igual ao da v1.2); contrato lido na v1.2.1 | conferência (1) |' % new['geradoEm'])
w('| 5 — não regressão | varreduras da seção 3.5 do QA R2 e exceções fechadas da R1 (CAIXA C-05/C-15; reunião C-06 a C-08; C-13; C-18), mais as do item 1; diff v1.2 → v1.3 restrito aos campos novos | conferência (4), (1) |')
w('| T-55 §4.1 | `validate.py` lê a v1.1 de `git show %s:saida/pacote/pacote.json` (`refs.py`), não de arquivo solto | `validate.py`, `refs.py` |' % refs.C_V11)
w('| T-55 §4.2 | `conferencias_R1.py` marcado como script histórico (R0 → R1) e passa a obter R0 e R1 do git (`%s` e `%s`) quando chamado sem argumentos; as conferências desta ocorrência estão em `conferencias_v13.py` | `conferencias_R1.py`, `conferencias_v13.py` |' % (refs.C_R0, refs.C_V12))
w('| T-55 §4.3 | `relatorio_R1.py`, `report.py` e `report2.py` marcados como históricos e sem gravação no repositório (saem em `out/historico_*`); o relatório novo sai em `out/pacote_relatorio_2026-10-13_v1_3.md` e é promovido ao repositório por passo explícito | os três scripts; `relatorio_v1_3.py` |')
w('| T-55 §4.4 | raiz do repositório e `out/` derivados de `__file__` (`common.py`: `REPO`, `HERE`, `OUT`); nenhum caminho absoluto nem relativo ao cwd nos scripts (varredura por `grep` na entrega) | `common.py` e demais |')
w('| T-55 §4.5 | `validate.json`: iteração de conjuntos substituída por `sorted(...)` e serialização com `sort_keys=True`; três execuções com `PYTHONHASHSEED` distintos dão arquivos byte a byte iguais | `validate.py` |')
w('')
w('### 13.2 Campos novos do pacote (literais)')
w('')
w('| Lote | `legendaMecanismo` |')
w('|---|---|')
for l in new['lotes']:
    if 'legendaMecanismo' in l: w('| %s | %s |' % (l['id'], l['legendaMecanismo']))
w('')
w('L1, L1C, L2 e L3 não têm o campo (o arquivo canônico não traz legenda de mecanismo). `avisos` do SIM-0 (3 strings; aviso 2 com a sublista):')
w('')
for k, a in enumerate(next(s for s in new['simulados'] if s['id'] == 'SIM-0')['avisos'], 1):
    w('%d. %s' % (k, a.replace('\n', '\n   ')))
w('')
w('### 13.3 Conferências por script (`conferencias_v13.py`; saídas em `saida/pacote/gerador_v1_3/out/`)')
w('')
w('%d conferências, %d falhas. Resultado por grupo:' % (NCONF, NCF))
w('')
w('| Grupo | Conferências | OK |')
w('|---|---|---|')
gr = collections.OrderedDict()
for c, alvo, ok, det in conf:
    g = re.match(r'^(\(\d\)|BASE)', c).group(1)
    gr.setdefault(g, [0, 0]); gr[g][0] += 1; gr[g][1] += ok
NOMEG = {'BASE': 'base: SHA-256 da v1.2', '(1)': '(1) diff v1.2 → v1.3 do pacote', '(3)': '(3) diff v1.2 → v1.3 da edição, fidelidade e varredura N-1', '(4)': '(4) varreduras de não regressão e exceções fechadas da R1', '(5)': '(5) contagens iguais às da v1.2'}
for g, (n, k) in gr.items(): w('| %s | %d | %d |' % (NOMEG[g], n, k))
w('')
w('Conferências do grupo (1), na íntegra (as demais estão em `out/conferencias_v13.txt`):')
w('')
for c, alvo, ok, det in conf:
    if c.startswith('(1)') or c == 'BASE': w('- %s %s%s' % ('OK' if ok else '**FALHA**', alvo, (' — ' + det[:300]) if det else ''))
w('')
w('Diff da edição v1.2 → v1.3 (linha a linha): %d arquivos mudam (`L6B_estudo.md` 1 linha; `README.md` 1 linha; 6 `*_gabarito.md` com 2 linhas inseridas cada); os outros %d são idênticos. Manifesto ordenado (SHA-256 das linhas "<sha>  <nome>"): v1.2 `%s`; v1.3 `%s`.' % (sum(E12[f] != E13[f] for f in E13), sum(E12[f] == E13[f] for f in E13), MAN12[:12], MAN13[:12]))
w('')
w('Resultados dos demais scripts: `validate.py` %d verificações, %d falhas (as 103 da v1.2 com os rótulos de v1.3, 2 delas ajustadas (chaves de lote com `legendaMecanismo`; chaves de simulado com `avisos`), mais 4 novas: literais das 6 legendas, forma das 6 legendas no canônico, literais dos 3 avisos, início literal dos avisos); `estudante_fidelidade.py` %d comparações, %d diferenças; `sync_check.py` TUDO OK; `fidelidade_mutacao.py` %d diferenças detectadas em %d mutações.' % (NVAL, NVF, fid['total'], fid['diferencas'], mut['diferencas_detectadas'], mut['mutacoes']))
w('')
w('### 13.4 Estado e SHA-256')
w('')
w('| Objeto | SHA-256 | bytes |')
w('|---|---|---|')
w('| `saida/pacote/pacote.json` v1.2 (git `%s`) | `%s` | %d |' % (refs.C_V12, SHA_V12, SIZE_V12))
w('| `saida/pacote/pacote.json` v1.3 | `%s` | %d |' % (SHA_NEW, SIZE_NEW))
w('| `saida/estudante/` v1.3 (%d arquivos; manifesto ordenado) | `%s` | — |' % (NF, MAN13))
w('')
w('O SHA-256 do próprio relatório e o manifesto de arquivos do gerador estão em `saida/pacote/gerador_v1_3/MANIFESTO.md` (o relatório não pode conter o próprio hash).')
w('')

# ------------------------------------------------------------------ apêndice A
w('## Apêndice A — regras literais da edição do estudante (trecho apagado em ⟦ ⟧)')
w('')
w('Só as regras **vigentes** da v1.3 (%d regras literais), na ordem de aplicação. Cada linha: fase, tipo, escopo, contexto e trecho apagado; todas verificadas como deleção pura (a especificação é uma subsequência do original). Fora desta lista, por desenho: as regras nº 6 ("O F4 afirma que …", restaurada na L4-11, C-13), nº 26 ("(corrigido pela O-3)" do curso 4.3.4) e nº 63 ("conferida pela QA" da seção ITENS REAIS), retiradas na R1 (C-13, C-14); as nº 42, 44 e 51 da R0 (L6A) constam abaixo na forma da C-16; as duas últimas linhas são as regras da N-1 (item 1 da lista). Conferido por programa: nenhuma regra vigente contém os textos das três retiradas.' % len(em.LITERAL))
w('')
RET = ['O F4 afirma que', '(corrigido pela O-3)', 'conferida pela QA em 08/10/2026']
w('Verificação das regras retiradas: %s.' % '; '.join('"%s": %d regra(s) vigente(s) a contêm' % (r_, sum(1 for x in em.LITERAL if r_ in x[2])) for r_ in RET))
w('')
import difflib as _d
w('| # | Fase | Tipo | Escopo | Original (contexto) → apagado |')
w('|---|---|---|---|---|')
for k, (fase, tipo, old_, new_, esc) in enumerate(em.LITERAL, 1):
    sm = _d.SequenceMatcher(None, old_, new_, autojunk=False)
    parts = []
    for t_, i1, i2, j1, j2 in sm.get_opcodes():
        if t_ == 'delete': parts.append('⟦%s⟧' % old_[i1:i2].replace('\n', '⏎'))
        elif t_ == 'equal': parts.append(old_[i1:i2].replace('\n', '⏎'))
    ctx = ''.join(parts)
    w('| %d | %s | %s | %s | %s |' % (k, fase, tipo, ', '.join(esc) if esc else 'todos', ctx.replace('|', '\\|')))
w('')
w('**Regras genéricas por escopo de arquivo (R1, C-20 e C-22):**')
w('')
w('| Escopo | Tipo | Expressão |')
w('|---|---|---|')
for esc, tipo, rx, keep in em.GENERIC_R1:
    w('| `%s*` | %s | `%s` |' % (esc, tipo, rx.pattern.replace('|', '\\|')))
w('')
w('**Lista CAIXA (R1, C-15; minúscula → maiúscula da primeira letra, só em `L6A_estudo`):**')
w('')
for esc, antes, depois in em.CAIXA: w('- `%s` → `%s`' % (antes.replace('\n', '⏎'), depois.replace('\n', '⏎')))
w('')
w('Nota: "n" não é repetido aqui porque as regras da fase "post" casam com o texto já tratado pelas regras genéricas; as ocorrências efetivas de cada tipo estão na seção 10.1.')
w('')

# ------------------------------------------------------------------ fim
w('## Pendências')
w('')
w('- QA: a gbq-cqe confere a v1.3 (fidelidade do pacote e da edição às fontes e à v1.2, e o escopo exato da ocorrência); a gbq-gerencia reconcilia e emite o gatilho A da v1.3 (D-V13-AGORA; a produção não decide o aceite). Nada disso foi feito aqui.')
w('- Arquivos do repositório criados ou alterados por esta ocorrência: `saida/pacote/pacote.json`, `saida/estudante/` (regerada), `saida/pacote/pacote_relatorio_2026-10-13_v1_3.md` e `saida/pacote/gerador_v1_3/` (com `MANIFESTO.md`). Nenhum outro; a secretaria deve atualizar o estado. A promoção de `out/` para o repositório foi um passo explícito, depois de todas as conferências com 0 falhas.')
open(os.path.join(OUT, 'pacote_relatorio_2026-10-13_v1_3.md'), 'w', encoding='utf-8').write('\n'.join(o) + '\n')
print(len(o), 'linhas')
