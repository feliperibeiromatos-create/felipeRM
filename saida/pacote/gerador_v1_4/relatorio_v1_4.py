# -*- coding: utf-8 -*-
"""T-57 — relatório do pacote v1.4, gerado POR INTEIRO pelo gerador (N-3 / D-R2-02): todas as seções com as contagens da própria ocorrência.
Lê out/ (pacote.json, stats.json, validate.json, estudante_contagem.json, estudante_fidelidade.json, sync_check.txt, conferencias_v14.json,
varredura_volatil_v14.json, fidelidade_mutacao.json) e as referências do git (refs.py). Grava out/pacote_relatorio_2026-10-13_v1_4.md; a promoção ao repositório é um passo explícito."""
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
v13 = refs.v13()          # v1.3 (git 9622604; SHA-256 fdcb7afd…)
st = jl('stats.json'); val = jl('validate.json'); ec = jl('estudante_contagem.json'); fid = jl('estudante_fidelidade.json')
conf = jl('conferencias_v14.json'); mut = jl('fidelidade_mutacao.json'); volx = jl('varredura_volatil_v14.json')
sync = open(os.path.join(OUT, 'sync_check.txt'), encoding='utf-8').read()
RAW_NEW = open(os.path.join(OUT, 'pacote.json'), 'rb').read()
SIZE_NEW = len(RAW_NEW)
SHA_NEW = hashlib.sha256(RAW_NEW).hexdigest()
RAW_V13 = refs.git_show(refs.C_V13, refs.PACOTE); SIZE_V13 = len(RAW_V13); SHA_V13 = hashlib.sha256(RAW_V13).hexdigest()
RAW_V12 = refs.git_show(refs.C_V12, refs.PACOTE); SIZE_V12 = len(RAW_V12); SHA_V12 = hashlib.sha256(RAW_V12).hexdigest()
RAW_V11 = refs.git_show(refs.C_V11, refs.PACOTE); SIZE_OLD = len(RAW_V11); SHA_OLD = hashlib.sha256(RAW_V11).hexdigest()
E12 = refs.estudante(refs.C_V12)
E13 = refs.estudante(refs.C_V13)
E14 = {f: open(os.path.join(OUT, 'estudante', f), encoding='utf-8').read() for f in sorted(os.listdir(os.path.join(OUT, 'estudante')))}
def manifesto(E): return hashlib.sha256(''.join('%s  %s\n' % (hashlib.sha256(tx.encode('utf-8')).hexdigest(), f) for f, tx in sorted(E.items())).encode('utf-8')).hexdigest()
MAN12, MAN13, MAN14 = manifesto(E12), manifesto(E13), manifesto(E14)
NF = len(E14)
NVAL, NVF = len(val), sum(1 for v in val if not v['ok'])
NCONF, NCF = len(conf), sum(1 for c in conf if not c[2])
SEM_B14 = sum(len(re.findall(r'D-[A-Z]{2,}', tx)) for tx in E14.values())
CTR_ANTES = refs.git_show(refs.C_V13, 'regras/pacote_contrato.md'); CTR_DEPOIS = open(ROOT + 'regras/pacote_contrato.md', 'rb').read()
SHA_CTR_A, SHA_CTR_D = hashlib.sha256(CTR_ANTES).hexdigest(), hashlib.sha256(CTR_DEPOIS).hexdigest()

o = []
w = o.append
def sha(path):
    return hashlib.sha256(open(ROOT + path, 'rb').read()).hexdigest()[:12]
LOTES = [l['id'] for l in new['lotes']]
LOTE_OF = gen.lote_of

# ------------------------------------------------------------------ cabeçalho
w('# pacote_relatorio_2026-10-13_v1_4.md — T-57 — EXPORTAR v1.4 — 2026-10-13 — gerado por gbq-csc')
w('')
w('Saídas: `saida/pacote/pacote.json` (versao 1, nome "%s", geradoEm %s, %d bytes UTF-8, SHA-256 `%s`, indent=1, newline final), este relatório (gerado por inteiro pelo gerador, `relatorio_v1_4.py`, N-3) e a edição do estudante em `saida/estudante/` (%d arquivos). Contrato: `regras/pacote_contrato.md` v1.2.2 (errata de forma da T-57, registro em `saida/pacote/contrato_v1_2_2_2026-10-13.md`) sobre a v1.2.1 + Regras da v1.2 (a–j) e as D1 da GBQ em `saida/pacote/T48_reconciliacao_R2_2026-10-13.md`, seção 2. Escopo desta ocorrência: D-V14-AGORA (Fundador, 13/10/2026) = a lista PARA A PRÓXIMA T-12 de `saida/pacote/T56_reconciliacao_2026-10-13.md`, seção 2 (O-1, O-2, nome v1.4, não regressão, avisos do SIM-0 não exibidos) + a LISTA PARA A T-57 de `saida/pacote/T54_decisoes_2026-10-13.md`, seção 3 (T54-1 a T54-8) + a D1 da GCE sobre o item 5 (`saida/gce/T54_item5_decisao_2026-10-13.md`). Gerador: `saida/pacote/gerador_v1_4/` (cópia alterada de `gerador_v1_3/`, que ficou intacto). Nada foi commitado; TAREFAS.md, PARA_PRESIDENCIA.md, DECISOES.md, estado/, banco/ e os canônicos dos lotes (`saida/gce`, `saida/gcb`) não foram alterados; em `regras/` só `pacote_contrato.md` (errata v1.2.2). A v1.3 (SHA-256 `%s`, %d bytes) foi guardada antes de ser sobrescrita e é lida do git (commit %s). Nada deste pacote nem da edição do estudante vai à candidata sem decisão do Fundador; a edição do estudante NÃO é entrega à candidata (a entrega da v1.3 e da v1.4 continua reservada ao Fundador, D-ENTREGA-V13-ESPERA).' % (new['nome'], new['geradoEm'], SIZE_NEW, SHA_NEW, NF, SHA_V13, SIZE_V13, refs.C_V13))
w('')
NPID = sum(1 for l in new['lotes'] for p in l['pares'] if 'id' in p)
w('Resultado em uma linha: **%d itens** (%d de banco + %d AUTORAL), %d lotes (6 com `legendaMecanismo`), %d discursivas, %d simulados com `n` e `versao` (SIM-0 com `avisos`); %d registros de errata (%d APLICADA, %d JÁ PRESENTE, 0 NÃO ENCONTRADA) e 6 erratas com alvo fora do pacote; validação por script: %d verificações, %d falhas; conferências da ocorrência: %d, %d falhas; edição do estudante: %d arquivos, fidelidade textual %d comparações, %d diferenças. Diff v1.3 → v1.4 do pacote: só `nome`, o campo novo `id` em %d pares (L4, L5, L6A, L6B), o `padrao` da D5 (anexo sem a nota R2) e o `curso` do L3 (uma palavra, "eu" → "se"); da edição: %d de %d arquivos mudam (pares com os separadores do canônico, 2 linhas do quadro do L1, rótulo "Nota:", 6B-06, legenda no `SIM-1_gabarito.md`, D5 sem a nota R2, L3 "se possa afirmar", versão no README); os outros %d são idênticos.' % (len(new['itens']), sum(1 for i in new['itens'] if i['rotulo'] != 'AUTORAL'), sum(1 for i in new['itens'] if i['rotulo'] == 'AUTORAL'), len(new['lotes']), len(new['discursivas']), len(new['simulados']), len(st['errata']), sum(1 for e in st['errata'] if e['estado'] == 'APLICADA'), sum(1 for e in st['errata'] if e['estado'] == 'JÁ PRESENTE'), NVAL, NVF, NCONF, NCF, NF, fid['total'], fid['diferencas'], NPID, sum(E13[f] != E14[f] for f in E14), NF, sum(E13[f] == E14[f] for f in E14)))
w('')

# ------------------------------------------------------------------ 1. fontes
w('## 1. Fontes')
w('')
w('Lidas em 13/10/2026 (SHA-256, 12 primeiros dígitos). O arquivo canônico de cada lote é o da tabela de fonte do contrato (regra 4 da v1.1); os `saida/lote*/RECONCILIADO.md` não existem e não são fonte.')
w('')
w('| Objeto | Arquivo(s) | Versão / observação | SHA-256 (12) |')
w('|---|---|---|---|')
FONTES = [
 ('Contrato', 'regras/pacote_contrato.md', 'v1.2.2 (errata de forma da T-57: `id` de par e regras de exibição) sobre a v1.2.1 (T-53) + Regras da v1.2 (a–j) + v1.1.1 + v1.1'),
 ('Registro do contrato', 'saida/pacote/contrato_v1_2_2_2026-10-13.md', 'SHA-256 antes e depois, cópia literal das alterações, conferência (T-57)'),
 ('Escopo da T-57', 'saida/pacote/T56_reconciliacao_2026-10-13.md', 'seção 2 (PARA A PRÓXIMA T-12: O-1, O-2, nome v1.4, não regressão, avisos) e D-T56-02 a D-T56-06'),
 ('Escopo da T-57', 'saida/pacote/T54_decisoes_2026-10-13.md', 'D-T54-01 a D-T54-08; seção 2 (texto da errata do contrato); seção 3 (LISTA PARA A T-57, T54-1 a T54-8)'),
 ('Item 5 da T-54 (GCE)', 'saida/gce/T54_item5_decisao_2026-10-13.md', 'D1-T54-a (nota R2 só na D4; D5 com R3–R4) e D1-T54-b (errata do curso do L3); seção 3.2 (ajuste de exportação)'),
 ('Errata do L3 (T-58)', 'saida/gce/lote3_errata3_2026-10-13.md', 'registro da errata E-1/E-2 aplicada pela gce-cpp em `GCE_Lote3_v2_CPP.md`'),
 ('Conferências do QA da T-56', 'saida/pacote/QA_T56_2026-10-13_gbq-cqe.md', 'N-1, legendas, avisos não exibidos (conferências de não regressão)'),
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
 ('L3', 'saida/gce/GCE_Lote3_v2_CPP.md', 'v2 canônico, com a T-44 (título e nota do 3.1) e a errata T-58 (curso 4.2) já gravadas'),
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
 ('Relatório anterior', 'saida/pacote/pacote_relatorio_2026-10-13_v1_3.md', 'relatório da v1.3 (T-56; fica como registro)'),
 ('Relatório anterior', 'saida/pacote/pacote_relatorio_2026-10-13.md', 'relatório da v1.2 (R0 + seção 13 da R1)'),
]
for obj, f, ob in FONTES:
    w('| %s | `%s` | %s | `%s` |' % (obj, f, ob, sha(f)))
w('| v1.1 | `git show %s:saida/pacote/pacote.json` | referência de comparação, lida do git | `%s` |' % (refs.C_V11, SHA_OLD[:12]))
w('| v1.2 (antes) | `git show %s:saida/pacote/pacote.json` | pacote canônico da D-PACOTE-V12, lido do git | `%s` |' % (refs.C_V12, SHA_V12[:12]))
w('| v1.3 (antes) | `git show %s:saida/pacote/pacote.json` | pacote canônico da D-PACOTE-V13, guardado antes de sobrescrever (cópia no scratchpad e no git) | `%s` |' % (refs.C_V13, SHA_V13[:12]))
w('| Edição do estudante v1.2 | `git archive %s saida/estudante` | %d arquivos; manifesto ordenado (SHA-256 das linhas "<sha>  <nome>") | `%s` |' % (refs.C_V12, len(E12), MAN12[:12]))
w('| Edição do estudante v1.3 (antes) | `git archive %s saida/estudante` | %d arquivos; mesmo manifesto | `%s` |' % (refs.C_V13, len(E13), MAN13[:12]))
w('| Contrato v1.2.1 (antes) | `git show %s:regras/pacote_contrato.md` | lido do git | `%s` |' % (refs.C_V13, SHA_CTR_A[:12]))
w('')
w('Condições do contrato (regra 5 e instrução da T-48), que continuam válidas: T-13, T-25, T-29, T-36, T-38, T-42, T-43, T-44, T-46 e T-47 CONCLUÍDAS e reconciliadas; T-40 CONCLUÍDA (BQ-0072, 0077, 0084, 0109, 0110 e 0111 entram, com 6/6 gabaritos sustentados). Simulados canônicos por D-SIM1-CANONICO, D-SIM2-CANONICO e D-SIM0P2-DIAGNOSTICO; SIM-0 v0.2 sem pendência (T-36 aplicada). T-48, T-53, T-55 e T-56 CONCLUÍDAS (a T-56 reconciliada em `T56_reconciliacao_2026-10-13.md`, aceite da v1.3 pela D-PACOTE-V13). T-58 (errata de forma do curso do L3, D1-T54-b da GCE) gravada em `saida/gce/GCE_Lote3_v2_CPP.md` e lida pelo pacote. Nenhuma errata nem texto canônico de simulado mudou desde a v1.3; do canônico dos lotes mudou só a T-58 (uma palavra no curso do L3, mais o registro "T-54" na Tabela de Correções, que não é exportado). Liberar qualquer simulado à candidata continua reservado ao Fundador.')
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
O, M, V3, N = cnt(old), cnt(v12), cnt(v13), cnt(new)
w('## 2. Contagens v1.1 → v1.2 → v1.3 → v1.4')
w('')
w('| Medida | v1.1 | v1.2 | v1.3 | v1.4 |')
w('|---|---|---|---|---|')
def tri(f):
    return (f(old, O), f(v12, M), f(v13, V3), f(new, N))
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
 ('pares (total)',) + tri(lambda p, c: sum(len(l['pares']) for l in p['lotes'])),
 ('pares com `id` (opcional, v1.2.2 ponto 1)',) + tri(lambda p, c: '%d (%s)' % (sum('id' in q for l in p['lotes'] for q in l['pares']), ', '.join('%s %d' % (l['id'], len(l['pares'])) for l in p['lotes'] if any('id' in q for q in l['pares']))) if any('id' in q for l in p['lotes'] for q in l['pares']) else 0),
 ('lotes com `legendaMecanismo` (opcional, v1.2.1 ponto 4)',) + tri(lambda p, c: '%d (%s)' % (sum('legendaMecanismo' in l for l in p['lotes']), ', '.join(l['id'] for l in p['lotes'] if 'legendaMecanismo' in l)) if any('legendaMecanismo' in l for l in p['lotes']) else 0),
 ('pegadinhas (total)',) + tri(lambda p, c: npg(p)),
 ('simulados',) + tri(lambda p, c: '%d (%s)' % (len(p['simulados']), ', '.join(s['id'] for s in p['simulados']))),
 ('simulados `n`',) + tri(lambda p, c: ' / '.join(str(s.get('n', '—')) for s in p['simulados'])),
 ('simulados com `avisos` (opcional, v1.2.1 ponto 5)',) + tri(lambda p, c: '%s (%d avisos)' % (', '.join(s['id'] for s in p['simulados'] if 'avisos' in s), sum(len(s['avisos']) for s in p['simulados'] if 'avisos' in s)) if any('avisos' in s for s in p['simulados']) else 0),
 ('bytes', SIZE_OLD, SIZE_V12, SIZE_V13, SIZE_NEW),
 ('SHA-256 (12)', SHA_OLD[:12], SHA_V12[:12], SHA_V13[:12], SHA_NEW[:12]),
]
for r in rows: w('| %s | %s | %s | %s | %s |' % r)
w('')
w('A v1.4 é a v1.3 (SHA-256 `%s`) mais `nome`, o campo opcional `id` nos %d pares de L4, L5, L6A e L6B, o `padrao` da D5 (anexo de notas sem a R2) e uma troca de uma palavra no `curso` do L3 (errata T-58): as medidas de itens, simulados, lotes, pegadinhas e discursivas são idênticas (seção 13, conferências (1) e (5)). Banco: 112 linhas em `banco/banco.csv`; 106 exportadas (60 C / 46 E) e 6 excluídas por anulação (gabarito X): %s. Os 60 itens da v1.1 mantêm o mesmo `comando` e a mesma aderência (37 direta / 23 parcial, conferido); os 46 novos são BQ-0061… do terceiro lote de varredura (inclui BQ-0072, 0077, 0084, 0109, 0110 e 0111, liberados pela T-40). BQ-0049 a 0051 são os únicos com `textoBase` (a coluna `texto_base`); nos 283 demais `textoBase` é `""` (F2).' % (SHA_V13[:12], NPID, ', '.join(x[0] for x in st['binfo']['excl'])))
w('')
w('### 2.1 Itens por lote (AUTORAL) e `comandoOriginal`')
w('')
w('| Lote | AUTORAL | C | E | `volatil` | `comandoOriginal` | pegadinhas v1.1 → v1.4 | pares | pares com `id` |')
w('|---|---|---|---|---|---|---|---|---|')
ol = {l['id']: l for l in old['lotes']}
for l in new['lotes']:
    its = [i for i in new['itens'] if i['rotulo'] == 'AUTORAL' and LOTE_OF(i['id']) == l['id']]
    w('| %s | %d | %d | %d | %d | %d | %d → %d | %d | %d |' % (l['id'], len(its), sum(1 for i in its if i['gabarito'] == 'C'), sum(1 for i in its if i['gabarito'] == 'E'),
      sum(1 for i in its if i.get('volatil')), sum(1 for i in its if i.get('comandoOriginal')), len(ol[l['id']]['pegadinhas']), len(l['pegadinhas']), len(l['pares']), sum('id' in q for q in l['pares'])))
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
w('`n` = tamanho da lista `itens` em 4/4. `avisos` (v1.2.1 ponto 5): só o SIM-0, com os avisos 1, 2 e 4 da folha canônica, literais (seção 13.4). `versao`: SIM-0 "v0.2" (cabeçalho do arquivo); SIM-1, SIM-2 e SIM-0-P2 "v1" (sem versão declarada, regra (e)). Nenhum simulado final contém item `volatil` ou `parcial`. O gabarito de cada posição do simulado (arquivos `*_gabarito.md`) é igual ao `gabarito` do item no pacote em 165/165 posições (60 + 40 + 40 + 25).')
w('')
w('### 2.3 Discursivas')
w('')
d5a, d5b = v13['discursivas'][4], new['discursivas'][4]
w('D1–D4 idênticas às da v1.1, da v1.2 e da v1.3 (D1 questão (L1), D2 questão e D3 peça (L2), D4 questão (L3)); a **D5** (peça, L3) é igual à da v1.3 em comando, aspectos, quesitos e conceitos e difere só no anexo de notas do `padrao`: a v1.3 acrescentava "Notas de correção (GCE, R2–R4)" (cópia das linhas 14–23 de `GCE_Lote3_padroes_GCE.md`, as mesmas da D4); a v1.4 acrescenta "Notas de correção (GCE, R3–R4)" com as linhas 21–23 literais, sem o trecho da R2 (linhas 14–20, 7 linhas; a R2 trata da alínea c da questão da D4 e não tem objeto na peça; D1-T54-a da GCE). `padrao` da D5: %d → %d caracteres. A D4 mantém o anexo R2–R4. Aspectos e quesitos conferidos: soma dos aspectos das questões 14,30 + 0,70 de apresentação = 15,00; peças 28,50 + 1,50 = 30,00. A observação "inferido pela EXEC" da D1 (Adendo 4) não é exportada: 0 ocorrência de "EXEC" nas discursivas. D3 e D5 são pareceres técnicos (gênero confirmado para analista e técnico; hipótese por analogia para o Cargo 11). Pesos por quesito são HIPÓTESE do Projeto.' % (len(d5a['padrao']), len(d5b['padrao'])))
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
w('| L3 | T-58 (D1-T54-b da GCE) | curso 4.2, bloco "CONTROVERSO / NÃO GABARITO": "jurisprudência firmada que se possa afirmar):" (antes "que eu possa afirmar") | JÁ PRESENTE | errata de forma gravada pela gce-cpp em `GCE_Lote3_v2_CPP.md` (registro `saida/gce/lote3_errata3_2026-10-13.md`); o pacote lê o arquivo atual: 1 troca de uma palavra no `curso` do L3 (%d → %d caracteres). O "que eu possa afirmar" que resta no canônico é o da linha de limites N4, não exportada |' % tuple(len(next(l for l in p['lotes'] if l['id'] == 'L3')['curso']) for p in (v13, new)))
w('')
w('Totais: os registros de substituição do gerador são %d (%d APLICADA e %d JÁ PRESENTE, a única sendo o Adendo 2 no 3.1); 0 NÃO ENCONTRADA. As quatro últimas linhas da tabela (E8, T-44, T-47, T-58) são informativas: E8 é a montagem da D1 (APLICADA, sem substituição) e T-44, T-47 e T-58 já estavam gravadas nos arquivos canônicos (JÁ PRESENTE); somadas, a tabela tem %d linhas, das quais %d APLICADA ou JÁ PRESENTE por substituição do gerador. Para cada APLICADA o script confere depois que Y consta do JSON e X não consta (fora das ocorrências de Y): validação "erratas: Y presente / X ausente", OK.' % (len(st['errata']), n_ap, n_ja, len(ORDER) + 4, len(st['errata'])))
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
w('## 5. Diff textual resumido v1.1 → v1.4 por lote')
w('')
w('Campos de lote comparados caractere a caractere (difflib), v1.1 (git %s) contra a v1.4. O diff v1.3 → v1.4 é menor: os campos de texto dos lotes (`resumo`, `curso`, `pares` (`a`, `b`, `como`), `pegadinhas`, `itensEdital`) são idênticos (conferência (1), seção 13), salvo a troca de uma palavra no `curso` do L3; o único acréscimo é o campo `id` nos 72 pares de L4, L5, L6A e L6B. Campos não citados: idênticos.' % refs.C_V11)
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
        sid = lambda d: {k: v for k, v in d.items() if k != 'id'}
        n_diff = sum(1 for a_, b_ in zip(ol[lid]['pares'], l['pares']) if sid(a_) != sid(b_))
        w('- pares: %d pares; %d com texto alterado (`a`, `b`, `como`)%s.' % (len(l['pares']), n_diff, '; todos com `id` (novo na v1.4, %s a %s)' % (l['pares'][0]['id'], l['pares'][-1]['id']) if all('id' in q for q in l['pares']) else ''))
        for a_, b_ in zip(ol[lid]['pares'], l['pares']):
            if sid(a_) != sid(b_):
                sm = difflib.SequenceMatcher(None, a_['como'], b_['como'], autojunk=False)
                for t, i1, i2, j1, j2 in sm.get_opcodes():
                    if t != 'equal': w('  - "%s": %s "%s" → "%s"' % (a_['a'][:40], t, a_['como'][i1:i2][:80], b_['como'][j1:j2][:120]))
    if len(ol[lid]['pegadinhas']) != len(l['pegadinhas']):
        w('- pegadinhas: %d → %d entradas (desdobramento da F3, com as reuniões da errata v1.2.1 ponto 2 quando houve), todas com `rotulo`.' % (len(ol[lid]['pegadinhas']), len(l['pegadinhas'])))
    if 'legendaMecanismo' in l:
        w('- `legendaMecanismo` (novo na v1.3): "%s".' % l['legendaMecanismo'])
    w('')
w('Itens (campo a campo, v1.1 → v1.4): `textoBase` 237 (F2, "nenhum" → ""), `comando` 90 e `comandoOriginal` 90 (D1-c), `justificativa` %d (F4), `nota` 2 (BQ-0003, BQ-0040), `enunciado` 1 (L1-Q04, F1). `gabarito`, `aderencia` (nos 60 da v1.1), `itemEdital`, `rotulo`, `certame`, `cargo`, `ano`, `numero` e `url`: 0 diferença. Discursivas: D1–D4 sem diferença; D5 com o anexo de notas da v1.4 (seção 2.3). Edital: igual. Da v1.3 para a v1.4, nenhum item muda. Nos lotes, além do que está acima: `id` nos 72 pares de L4, L5, L6A e L6B e uma troca de palavra no `curso` do L3 ("eu" → "se", T-58).' % len(st['f4']))
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
w('| Lote | entradas v1.1 → v1.4 | modos de origem (entradas da v1.1) |')
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
w('Gerada a partir do `pacote.json` v1.4 (fonte única). **%d arquivos**, os mesmos nomes da v1.2 e da v1.3: `README.md` (índice, versão v1.4, data %s, aviso "material de estudo; gabaritos em arquivo separado"); por lote, `<ID>_estudo.md` (itens do edital, resumo, curso, pares, pegadinhas com rótulo), `<ID>_itens.md` (texto-base se houver, comando e enunciado, nessa ordem; sem gabarito, justificativa nem marcas) e `<ID>_gabarito.md` (gabarito, item do edital e justificativa; **no topo, a `legendaMecanismo` literal do lote, nos 6 lotes que a têm**) para L1, L1C, L2, L3, L4, L4C, L5, L5C, L6A e L6B (30 arquivos); `BANCO_itens.md` e `BANCO_gabarito.md` (certame, cargo, ano, número, URL oficial, aviso VOLÁTIL e `nota` literal, **sem o rótulo "Nota:" do gerador e** sem o identificador de decisão); por simulado `<SIM>_folha.md` (sem o id de origem dos itens) e `<SIM>_gabarito.md` (SIM-0, SIM-1, SIM-2, SIM-0-P2; **v1.4: no topo, depois de "Número de itens", a `legendaMecanismo` de cada lote de origem que a tenha, sem repetir string igual**); `DISCURSIVAS.md` e `DISCURSIVAS_padrao.md`. **Pares (v1.4):** cada linha de par usa os separadores e a pontuação do canônico do próprio lote (`- **a** vs **b**: como` / `- **a** vs **b**.` nos lotes GCE; `- Cn. **a** × **b** | como` nos lotes GCB, com o `id` do pacote). Resumo e curso vão em blocos de texto cercados, para preservar quebras, recuos e tabelas. **Os `avisos` do SIM-0 não são exibidos** (D-T53-02/item 3 da lista; D-T56-03: até decisão do Fundador sobre o que se compartilha com a candidata); a fidelidade confere que o texto dos três avisos não aparece em arquivo algum.' % (NF, new['geradoEm']))
w('')
w('**Regra:** as marcas internas saem SOMENTE POR DELEÇÃO (nunca reescrita) por `estudante_marcas.py` e `literais.py`, com as exceções fechadas da reconciliação R1: (i) CAIXA (C-05 e C-15): minúscula → maiúscula da primeira letra de um trecho, lista de 8 pares só em `L6A_estudo` (e as 2 trocas de caixa na F4 do pacote); (ii) reunião de fragmentos de pegadinha com "; " (C-06 a C-08, só no pacote); (iii) a `nota` de BQ-0003 sai da edição sem " (D-LEI-15352)" (C-18; errata v1.2.1 ponto 3), só na exibição; (iv) **v1.4:** o realinhamento só com espaços de 2 linhas do quadro-síntese do L1 (D-T54-02; apêndice A), que não apaga nada. A marca VOLÁTIL vira, nos itens `volatil: true`, o aviso fixo "Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027."; a `nota` (BQ-0003, BQ-0040) é exibida junto do item. Enunciado, comando e texto-base de item não são tocados (afirmado por teste: nenhuma marca da lista neles). **Novidade da v1.3 (N-1, D-R2-01):** duas regras literais, só em `L6B_estudo`, apagam "Nesta produção " e " (a especificação previa o item \"se houver base\")" do curso 4.0.2 (o "NÃO" que segue já tem inicial maiúscula); no pacote a marca fica, por desenho (D-PACOTE-V11). **Novidade da v1.4 (T-57):** (a) o realinhamento só com espaços de 2 linhas do quadro-síntese do L1 (D-T54-02; exceção (iv): não apaga nada, insere 6 espaços antes de `|` para recompor as posições do canônico; lista no apêndice A); (b) a regra do 6B-06 passa a apagar o parêntese de verificação inteiro, "Fonte: conceito geral⟦ (a definição da tríade não foi confirmada em fonte aberta hoje; ver curso 4.1.1)⟧. Tema da tríade" (D-T54-06 c); (c) o anexo "Notas de correção" da D5 perde, por desenho do gerador, a nota R2 (D1-T54-a da GCE) e o rótulo apagado passa a " (GCE, R3–R4)"; (d) o rótulo "Nota: " do gerador não é mais emitido (D-T54-04) e as legendas de lote entram nos `SIM-*_gabarito.md` (D-T54-07). Regras genéricas (por tipo) e regras literais (frase ou cláusula a apagar, `⟦…⟧` na especificação; %d regras literais vigentes, apêndice A):' % len(em.LITERAL))
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
w('Referência: na v1.2 as remoções somaram 569; na v1.3, 571; a v1.4 soma %d (571 − 3: saem as 3 deleções que só existiam por causa da nota R2 na D5 — "Alínea c … (R4 do Projeto)", "R2. " e " da versão da CPP" —; a regra do 6B-06 passa a apagar o parêntese inteiro e a do rótulo do anexo da D5 apaga " (GCE, R3–R4)", ambas com a mesma contagem das anteriores; o realinhamento do quadro do L1 não é remoção).' % sum(ec['total'].values()))
w('')
w('Arquivos sem nenhuma remoção: os `*_itens.md`, `BANCO_*`, `*_folha.md`, `README.md` e os `*_gabarito.md` cujos itens não tinham marca (a tabela só lista os arquivos com remoção).')
w('')
w('### 10.2 Fidelidade (script `estudante_fidelidade.py`)')
w('')
w('O script lê os %d arquivos com um parser próprio (independente do gerador) e confere, campo a campo, o texto do estudante com o do pacote: (1) igual ao texto do pacote com as deleções das regras; (2) obtido do texto do pacote só por deleção (teste de subsequência linear e, depois, difflib: apenas `equal`/`delete`, salvo as 8 trocas de caixa da lista CAIXA, C-15, e, **v1.4**, o desfazimento dos 2 realinhamentos de espaço do quadro do L1, D-T54-02, exceção fechada de 2 regras com 1 ocorrência cada); (3) comando, texto-base, enunciado, gabarito, item do edital, aderência, nota (com a única exceção da C-18), aviso VOLÁTIL, certame, cargo, ano, número, URL, ordem e `n` dos simulados, valores dos aspectos e conceitos dos quesitos idênticos ao pacote; (4) a `legendaMecanismo` de cada lote com o campo está literal, sozinha, no topo do `*_gabarito.md` do próprio lote (antes do primeiro item) e em nenhum outro arquivo (salvo, **v1.4**, as legendas dos lotes de origem no topo de cada `SIM-*_gabarito.md`, uma vez cada, na ordem de `lotes`); lote sem o campo não tem texto antes do primeiro item; o texto dos `avisos` não aparece na edição; (5) **v1.4:** o parser lê a linha de par nos dois formatos e compara `a`, `b`, `como` e o `id` exibido com o pacote (linha fora do formato é DIFERENÇA); a `nota` é exibida sem rótulo (`- `/`> ` seguido do valor, com a única deleção do identificador da C-18); o README declara v1.4. Teste negativo (`fidelidade_mutacao.py`: %d mutações aplicadas isoladamente, cada uma em cópia nova da edição — %s) detectou %d diferenças no total; todas as mutações foram detectadas: %s; portanto o script não é cego.' % (NF, mut['mutacoes'], ', '.join('`%s`' % a for a in mut['arquivos_mutados']), mut['diferencas_detectadas'], 'sim' if mut['todas_detectadas'] else 'NÃO'))
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
w('**Na edição do estudante** as varreduras da seção 3.5 do QA da R2 dão 0 (conferência (4), seção 13): `;)`, ` — $`, `****`, `abertas? hoje`, `(v2,`, `D-LEI-15352`, `neste chat`, `Retificação`, `Gabarito [CE] mantido`, códigos U/GG/TB/CI, códigos N (L1, L1C, L2, L3, SIM-2, SIM-0-P2), ` — <id>` nas folhas, `erificado em 8/10/2026` (L5); mais [TS], `[V `, CQFP/CQE/GCE/GCB/GBQ/CPP, `T-n`, QA, `O-n`, "Lição O", `R-nCn`, "NÃO VOLÁTIL", "Sem marca VOLÁTIL", REVERIFICAR e `\\bD-XX`; da N-1, "Nesta produção" e "especificação previa"; e, da v1.4, "Nota: nota de vigência", "não foi confirmada em fonte", "R2." e "Alínea c da discursiva" na D5 e "que eu possa afirmar" no curso do L3 (0 em todos).')
w('')
w('**Permanecem na edição, por decisão da reconciliação (D1 da GBQ):** `a tecla F4` (`L6A_estudo.md` 83) e `O F4 afirma que …` (`L4_gabarito.md`, L4-11; D-R1-07); "VOLÁTIL" fora do aviso fixo em %d linhas de títulos, rubricas e orientação de estudo (%s; D-R1, 2.3-g); etiquetas GI/TC/AT/IC nas justificativas (2.3-h), com a legenda literal do lote no topo do `*_gabarito.md` dos 6 lotes que a têm **e, na v1.4, no `SIM-1_gabarito.md`**; códigos N1–N4 do L4 (2.3-e); `(Derep (antigo DETAQ); …)` no `L1_estudo.md` (literal pela F5; D-R1-15 DESCARTADO); 29 justificativas iniciadas em minúscula depois do prefixo de campo (forma do canônico; D-R1-18 DESCARTADO); referentes perdidos em deleções que a D-T54-06 mandou **não mexer**: L6A 135 "As duas páginas" (alínea a; referente recuperável em `L6A_estudo.md` 31), L5 119 e 126 (alínea b; citações nominais entre aspas) e L3 101 e 574 "(não cobrar descrição de sistema real.)" (alínea d; "N6:" é código N vedado). **Saíram desta lista na v1.4:** "que eu possa afirmar" no curso do L3 (T-58); as remissões a pares por id ("par C1", "par C14", "C19" em A5-09, 5C-03, 5C-07 e 4C-08), resolvidas pelo `id` de par (os rótulos "C1…Cn" aparecem agora nos pares de L4, L5, L6A e L6B, na edição e no pacote); o referente perdido da 6B-06 (parêntese apagado); a nota R2 repetida na D5; o rótulo "Nota: nota de vigência:"; o quadro-síntese do L1 desalinhado nas duas linhas afetadas e o separador "×"/" — " dos pares. **Continua no canônico, e portanto na edição:** o desalinhamento da linha "Tradução p/ inglês" do quadro do L1 (posições de `|` iguais às do canônico). **Os avisos 1, 2 e 4 do SIM-0** estão no pacote (campo `avisos`) e continuam fora da edição (decisão do Fundador).' % (len(volx['volatil_fora_do_aviso']), '; '.join('%s:%d' % tuple(x) for x in volx['volatil_fora_do_aviso'])))
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
w('**DÚVIDAS da v1.3 (14 a 16), decididas na reconciliação `T56_reconciliacao_2026-10-13.md`:**')
w('')
w('| DÚVIDA (v1.3) | Decisão que a resolve | Efeito nesta ocorrência |')
w('|---|---|---|')
w('| 14 — forma de exibição da `legendaMecanismo` | D-T56-02 (aceita; sem título "Legenda"; extensão aos `SIM-*_gabarito.md` passa a ser o item 7 da T-54) | legenda no topo dos 6 `L<lote>_gabarito.md` (inalterado) e, v1.4, no `SIM-1_gabarito.md` (D-T54-07) |')
w('| 15 — aviso 2 do SIM-0 remete a marca ausente da folha | D-T56-03 (BACKLOG, condicionado ao Fundador) | `avisos` continuam literais no pacote e não exibidos na edição |')
w('| 16 — varredura `D-[A-Z]{2,}` sem `\\b` | D-T56-04 (DESCARTADO; errata de registro) | a conferência usa `\\bD-[A-Z]{2,}` (0); sem `\\b` são %d ocorrências, as mesmas das versões anteriores (TID-IA, TID-DADOS-VIZ, END-TO-END) |' % SEM_B14)
w('')
w('**DÚVIDAS desta ocorrência (v1.4), cada uma com a decisão que a resolve; nenhuma impede o aceite:**')
w('')
D = [
 ('6B-06 está na linha 33 de `L6B_gabarito.md`, não na 31.', 'A LISTA (T54-6) e a D-T54-06 (c) citam a linha 31. A legenda de 2 linhas do topo do `L6B_gabarito.md` (D-T56-02) desloca a justificativa da 6B-06 para a linha 33, na v1.3 e na v1.4. Apliquei a regra da LISTA (apagar o parêntese inteiro, 1 ocorrência, deleção pura); só o número de linha difere. O mesmo vale para o exemplo do L3 da T54-3 (a LISTA diz linha 565; o par sem `b` nem `como` está na linha 564 da v1.3, dentro da faixa 539–566 da própria LISTA). Sem decisão a tomar; proposta: DESCARTADO (registro). Remissão: D-T54-06 (c).'),
 ('O realinhamento do quadro do L1 é a única operação da edição que não é deleção.', 'A D-T54-02 manda inserir 6 espaços em 2 linhas. O gerador, a fidelidade e as conferências passaram a aceitar essa exceção fechada (REALINHA: 2 regras, 1 ocorrência cada, só espaços inseridos num único ponto imediatamente antes de um `|`; a fidelidade desfaz o realinhamento antes do teste de subsequência e recusa qualquer outra inserção). Registro para o aceite; nenhuma decisão pendente. Remissão: D-T54-02; apêndice A.'),
 ('Rótulo do anexo da D5: "Notas de correção (GCE, R3–R4)" no pacote.', 'A GCE sugeriu o rótulo (T54_item5_decisao, 3.2) "salvo D1 diversa da GBQ"; a D-T54-05 manda aplicar o que a GCE fixar e a T54_decisoes não fixa outro rótulo. Apliquei "(GCE, R3–R4)" no pacote (a D4 mantém "(GCE, R2–R4)"); na edição o trecho entre parênteses sai por deleção, como já saía na D4 (a edição exibe "Notas de correção"). Remissão: D-T54-05; D1-T54-a. Proposta: aceitar.'),
 ('Par sem `b` e sem `como` (L3, "Confidencialidade, integridade, disponibilidade").', 'A LISTA cobre o caso (`- **{a}**.`). O gerador registra o caso no LOG ("par sem " vs " (b vazio)") e a edição exibe `- **Confidencialidade, integridade, disponibilidade**.`, igual ao canônico sem o numeral. Sem decisão a tomar. Remissão: D-T54-01.'),
 ('Escopo do `id` de par.', 'O `id` só existe onde o canônico rotula o par "C<n>." (L4, L5, L6A, L6B: %d pares). L4C e L5C não têm pares próprios; as remissões de 4C-08, 5C-03, 5C-07 e A5-09 apontam para pares de L4 e L5, que têm `id`. Os lotes GCE (%d pares) não têm `id` e nenhuma justificativa remete a eles por número. Sem decisão a tomar. Remissão: D-T54-03.' % (NPID, sum(1 for l in new['lotes'] for p in l['pares'] if 'id' not in p))),
 ('Scripts históricos: "marcar" em vez de "mover".', 'A D-T56-05 deixa a escolha à produção. Escolhi marcar, no `MANIFESTO.md` (coluna "Papel": "não executável; registro da R0/R1"), os 5 scripts `relatorio_R1.py`, `report.py`, `report2.py`, `diff.py` e `diff2.py`, sem alterá-los e sem mover (mover mudaria os caminhos relativos do próprio histórico). Conferido: cada um sai com código 1 sem gravar nada. Sem decisão a tomar. Remissão: D-T56-05.'),
]
for i, (t_, d) in enumerate(D, 17):
    w('%d. **%s** %s' % (i, t_, d))
w('')

# ------------------------------------------------------------------ apêndice A
# ------------------------------------------------------------------ 13. ocorrência v1.4
def lin_ops(a, b):
    A, B = a.split('\n'), b.split('\n')
    return A, B, [o for o in difflib.SequenceMatcher(None, A, B, autojunk=False).get_opcodes() if o[0] != 'equal']
def pares_alt(f):
    """(n.º da linha na v1.3, linha v1.3, linha v1.4) das linhas substituídas de f (blocos de substituição com o mesmo n.º de linhas)."""
    A, B, ops = lin_ops(E13[f], E14[f]); out = []
    for t, i1, i2, j1, j2 in ops:
        if t == 'replace' and i2 - i1 == j2 - j1:
            out += [(i1 + k + 1, A[i1 + k], B[j1 + k]) for k in range(i2 - i1)]
    return out
def cut(s, n=260): return s if len(s) <= n else s[:n] + '…'
w('## 13. Ocorrência v1.4 (T-57)')
w('')
w('Ocorrência da D-V14-AGORA (Fundador, 13/10/2026), com o gerador de `saida/pacote/gerador_v1_3/` copiado para `saida/pacote/gerador_v1_4/` (a v1.3 ficou intacta; `refs.py` ganhou a referência da v1.3, commit %s). Despacho: T-57, com a lista da `T56_reconciliacao_2026-10-13.md`, seção 2, a LISTA PARA A T-57 de `T54_decisoes_2026-10-13.md`, seção 3 (T54-1 a T54-8), e a D1 da GCE sobre o item 5 (`saida/gce/T54_item5_decisao_2026-10-13.md`, com a errata T-58 já gravada no canônico do L3). Toda mudança saiu do gerador (`pacote.json` e `saida/estudante/` não foram editados à mão).' % refs.C_V13)
w('')
w('### 13.1 Itens da lista PARA A PRÓXIMA T-12 (`T56_reconciliacao`, seção 2)')
w('')
w('| Item | Como foi feito | Onde se confere |')
w('|---|---|---|')
w('| 1 — O-1 (D-T56-05) | os 5 scripts históricos que não rodam no estado atual (`relatorio_R1.py`, `report.py`, `report2.py`, `diff.py`, `diff2.py`) ficam em `gerador_v1_4/` **marcados** no `MANIFESTO.md` como "não executável; registro da R0/R1" (opção "marcar"; ver DÚVIDA 22); os históricos que ainda rodam (`conferencias_R1.py`, `texts.py`, `probe.py`, `resid.py`, `review.py`) continuam como "histórico (executável; lê do git)"; nenhum script ativo foi alterado por este item. Conferido: cada um dos 5 sai com código 1 e não grava nada | `MANIFESTO.md`, coluna "Papel" |')
w('| 2 — O-2 (D-T56-06) | a "Ordem de execução" do `MANIFESTO.md` descreve o redirecionamento de cada `out/*_stdout.txt` (runner `rodar_tudo.sh`: `gen_stdout.txt` = saída de `build_pacote.py` (`>`) mais a de `estudante_gen.py` (`>>`); `fidelidade_stdout.txt`, `sync_stdout.txt`, `validate_stdout.txt`, `conferencias_stdout.txt`, `mutacao_stdout.txt` e `relatorio_stdout.txt` = a saída-padrão do script homônimo). O caminho absoluto de `fidelidade_stdout.txt` saiu: `estudante_fidelidade.py` imprime `pacote:` e `estudante:` relativos à raiz do repositório (`saida/pacote/gerador_v1_4/out/…`); `grep` por caminho absoluto em `out/*.txt`: 0 | `rodar_tudo.sh`, `MANIFESTO.md`, `out/fidelidade_stdout.txt` |')
w('| 3 — nome (T56, seção 2, item 3) | `nome` "%s", `versao` 1, `geradoEm` %s (igual ao da v1.3); só o canônico com gatilho aceito entra (aqui: a T-58, errata do curso do L3) | conferência (1) |' % (new['nome'], new['geradoEm']))
w('| 4 — não regressão | varreduras da seção 3.5 do QA R2 (com `\\bD-[A-Z]{2,}`), exceções fechadas da R1 (CAIXA C-05/C-15, reunião C-06 a C-08, C-13, C-18) e conferências do QA da T-56 (N-1, legendas, avisos não exibidos); diff v1.3 → v1.4 restrito ao previsto (itens abaixo) | conferências (1), (3), (4) |')
w('| 5 — avisos do SIM-0 | continuam no pacote (3 strings) e **não** são exibidos na edição (0 arquivo com o texto dos avisos; fidelidade: "avisos não exibidos" %d) | conferência (4), fidelidade |' % fid['comparacoes']['avisos não exibidos'])
w('')
w('### 13.2 T-54, item a item (LISTA PARA A T-57; antes = v1.3, depois = v1.4)')
w('')
w('| Item | Antes → depois | Contagem / verificação |')
w('|---|---|---|')
EX = {}
for lid in ['L1', 'L2', 'L3', 'L4', 'L5', 'L6A', 'L6B']:
    for ln, a_, b_ in pares_alt(lid + '_estudo.md'):
        if a_.startswith('- ') and b_.startswith('- '):
            EX.setdefault(lid, []).append((ln, a_, b_))
npar = {lid: len(EX[lid]) for lid in EX}
assert sum(npar.values()) == 139, npar
w('| T54-1 contrato v1.2.2 (D-T54-08) | `regras/pacote_contrato.md` v1.2.1 → v1.2.2: linha 1 (título), acréscimo no fim da linha 3 e seção nova "Errata de forma da v1.2.2" (9 linhas + 1 em branco) depois do ponto 6 da errata v1.2.1; registro `saida/pacote/contrato_v1_2_2_2026-10-13.md` | SHA-256 `%s` → `%s`; diff por linha: 2 substituições + 1 inserção; seção nova igual, caractere a caractere, ao bloco (iii) da T54_decisoes; **nenhum campo obrigatório mudou** (exemplo JSON, "Regras:", v1.1, v1.1.1, v1.2, tabela de fonte e PROMPT DE PARTIDA idênticos; `versao` 1) |' % (SHA_CTR_A[:12], SHA_CTR_D[:12]))
w('| T54-2 `id` de par (D-T54-03) | `p1.py` `pares_gcb`: `dict(id=\'C\' + m.group(1), a=…, b=…, como=…)`; 72 pares ganham `id` como primeira chave; `a`, `b`, `como` iguais | L4 C1–C20 (20), L5 C1–C15 (15), L6A C1–C19 (19), L6B C1–C18 (18) = %d; L1, L2, L3: 0 `id`; ids = rótulos `^C\\d+\\.` da seção (c) do canônico, na ordem; remissões: L5 C1 = Histograma × gráfico de barras, L5 C14 = Storytelling × dashboard, L4 C19 = Injeção de prompt × jailbreak (conceitos gerais) |' % NPID)
w('| T54-3 pares na edição (D-T54-01) | GCE: `- **a** × **b** — como` → `- **a** vs **b**: como` (ou `.` se `como` vazio); GCB: `- **a** × **b** — como` → `- Cn. **a** × **b** \\| como` | **139** linhas (L1 %d, L2 %d, L3 %d, L4 %d, L5 %d, L6A %d, L6B %d); o teste da D-T54-01 dá 0 diferença de caractere nas 139; GCE (67 linhas): 0 com `** × **`, todas terminam em ".", 27 com `como` vazio (L1 1, L2 9, L3 17); GCB (72): todas casam `^- C\\d+\\. \\*\\*`; 136 linhas iguais à linha canônica (erratas aplicadas) e 3 só com deleção de marca (L4 "Clustering", L4 "Controlador", L6B "Backup completo"); fora de "## Pares" nenhuma linha muda por este item |' % tuple(npar[x] for x in ['L1', 'L2', 'L3', 'L4', 'L5', 'L6A', 'L6B']))
w('| T54-4 quadro do L1 (D-T54-02) | `L1_estudo.md` 424 e 427: 6 espaços inseridos antes de `\\|` em cada linha (exceção fechada REALINHA) | comprimentos 82 e 71 e posições de todos os `\\|` iguais às de `GCE_Lote1_v2_CPP.md` 475 e 478; as demais linhas do quadro (419–430) iguais às da v1.3; o desalinhamento canônico da linha "Tradução p/ inglês" permanece |')
w('| T54-5 rótulo da nota (D-T54-04) | `> Nota: nota de vigência: …` → `> nota de vigência: …` (e `- Nota: …` → `- …`) | 8 linhas: BANCO_itens 2, BANCO_gabarito 2, SIM-0_folha 2, SIM-0_gabarito 2 (BQ-0003 e BQ-0040); 0 "Nota: nota de vigência"; 4 linhas `^> nota de vigência: ` e 4 `^- nota de vigência: `; o resto de cada linha igual à v1.3; " (D-LEI-15352)" continua ausente; o pacote não muda |')
w('| T54-6 6B-06 (D-T54-06 c) | `Fonte: conceito geral (a definição da tríade não foi confirmada em fonte; ver curso 4.1.1). Tema da tríade…` → `Fonte: conceito geral. Tema da tríade…` | deleção pura, 1 ocorrência, `L6B_gabarito.md` linha 33 (DÚVIDA 17); 0 "não foi confirmada em fonte" e 0 "abertas? hoje" na edição; o pacote não muda (justificativa igual à da v1.3); pontos a), b) e d) da D-T54-06: não mexer |')
w('| T54-7 legenda nos `SIM-*_gabarito.md` (D-T54-07) | `SIM-1_gabarito.md`: depois de "- Número de itens: 40", as legendas de L4 (= L4C = L5C) e de L5, literais, em linha própria, sem título | +4 linhas (2 legendas e 2 em branco); iguais, caractere a caractere, a `lotes[L4].legendaMecanismo` e `lotes[L5].legendaMecanismo`; `SIM-0_gabarito.md` (só BQ), `SIM-2_gabarito.md` e `SIM-0-P2_gabarito.md` sem legenda (a única mudança do SIM-0 é a da T54-5); folhas não mudam por este item |')
w('| T54-8a D5 (D1-T54-a da GCE) | `p2.py`: anexo da D5 = só R3–R4 (linhas 21–23 literais de `GCE_Lote3_padroes_GCE.md`), rótulo "Notas de correção (GCE, R3–R4)"; D4 mantém R2–R4 (linhas 14–23) | pacote: `padrao` da D5 sem as 7 linhas da R2 (%d → %d caracteres); edição: `DISCURSIVAS_padrao.md` perde exatamente as 7 linhas 507–513 da v1.3; `validate.py` exige D4 = linhas 14–23 e D5 = linhas 21–23 |' % (len(d5a['padrao']), len(d5b['padrao'])))
w('| T54-8b curso do L3 (D1-T54-b da GCE; T-58) | `lotes[L3].curso` relido do canônico atual: "jurisprudência firmada que eu possa afirmar):" → "…que se possa afirmar):" | uma troca de uma palavra no pacote (%d → %d caracteres); na edição, `L3_estudo.md` linha 422 é a única linha que muda fora de "## Pares"; 0 "que eu possa afirmar" no pacote e na edição |' % tuple(len(next(l for l in p['lotes'] if l['id'] == 'L3')['curso']) for p in (v13, new)))
w('')
w('Exemplos literais (v1.3 → v1.4) da primeira linha de par alterada de cada lote (linha da v1.3):')
w('')
for lid in ['L1', 'L2', 'L3', 'L4', 'L5', 'L6A', 'L6B']:
    ln, a_, b_ = EX[lid][0]
    w('- %s, linha %d:' % (lid, ln))
    w('  - antes: `%s`' % cut(a_.replace('`', "'")))
    w('  - depois: `%s`' % cut(b_.replace('`', "'")))
ln, a_, b_ = next(x for x in EX['L3'] if ' × ' not in x[1] and x[1].startswith('- **'))
w('- L3, linha %d (par sem `b` nem `como`):' % ln)
w('  - antes: `%s`' % a_); w('  - depois: `%s`' % b_)
w('')
w('Quadro-síntese do L1 (T54-4), linhas da v1.3 (antes) e da v1.4 (depois):')
w('')
w('```text')
for ln, a_, b_ in pares_alt('L1_estudo.md'):
    if a_.lstrip().startswith('|'):
        w('v1.3 %d: %s' % (ln, a_)); w('v1.4 %d: %s' % (ln, b_))
w('```')
w('')
w('6B-06 (T54-6), parte final da justificativa:')
w('')
ln6 = next(i for i, x in enumerate(E14['L6B_gabarito.md'].split('\n')) if 'Fonte: conceito geral' in x and 'tríade' in x)
l13, l14 = E13['L6B_gabarito.md'].split('\n')[ln6], E14['L6B_gabarito.md'].split('\n')[ln6]
w('- antes: `…%s`' % l13[l13.index('Fonte: conceito geral'):])
w('- depois: `…%s`' % l14[l14.index('Fonte: conceito geral'):])
w('')
w('D5 (T54-8a): linhas apagadas de `DISCURSIVAS_padrao.md` (v1.3, 507–513), idênticas às 407–413 da D4, que ficam:')
w('')
A_, B_, ops_ = lin_ops(E13['DISCURSIVAS_padrao.md'], E14['DISCURSIVAS_padrao.md'])
w('```text')
for t, i1, i2, j1, j2 in ops_:
    if t == 'delete':
        for k in range(i1, i2): w('%d: %s' % (k + 1, A_[k]))
w('```')
w('')
w('L3 (T54-8b), `L3_estudo.md` linha 422:')
w('')
ln3, a_, b_ = next(x for x in pares_alt('L3_estudo.md') if 'possa afirmar' in x[1])
w('- antes: `%s`' % a_); w('- depois: `%s`' % b_)
w('')
w('### 13.3 Arquivos da edição que mudam (v1.3 → v1.4)')
w('')
chg = [f for f in E14 if E13[f] != E14[f]]
w('%d arquivos mudam; os outros %d são idênticos byte a byte. A reconstrução da v1.4 aplicando à v1.3 só as operações da lista dá 43/43 arquivos iguais (conferência (3)).' % (len(chg), NF - len(chg)))
w('')
w('| Arquivo | linhas substituídas | inseridas | apagadas | operações da lista |')
w('|---|---|---|---|---|')
WHY = {'README.md': 'versão v1.3 → v1.4', 'BANCO_itens.md': 'T54-5', 'BANCO_gabarito.md': 'T54-5', 'SIM-0_folha.md': 'T54-5', 'SIM-0_gabarito.md': 'T54-5', 'L6B_gabarito.md': 'T54-6', 'SIM-1_gabarito.md': 'T54-7', 'DISCURSIVAS_padrao.md': 'T54-8a', 'L1_estudo.md': 'T54-3 (17 pares) + T54-4 (2 linhas)', 'L3_estudo.md': 'T54-3 (28 pares) + T54-8b (1 linha)'}
ts = [0, 0, 0]
for f in chg:
    A_, B_, ops_ = lin_ops(E13[f], E14[f])
    r_ = sum(i2 - i1 for t, i1, i2, j1, j2 in ops_ if t == 'replace'); i_ = sum(j2 - j1 for t, i1, i2, j1, j2 in ops_ if t == 'insert'); d_ = sum(i2 - i1 for t, i1, i2, j1, j2 in ops_ if t == 'delete')
    ts[0] += r_; ts[1] += i_; ts[2] += d_
    w('| %s | %d | %d | %d | %s |' % (f, r_, i_, d_, WHY.get(f, 'T54-3 (pares)')))
w('| **Total** | **%d** | **%d** | **%d** | |' % tuple(ts))
w('')
w('### 13.4 Campos do pacote e literais')
w('')
w('**`id` de par (novo, opcional; contrato v1.2.2 ponto 1):**')
w('')
w('| Lote | pares | com `id` | primeiro → último | exemplo (`id`: a × b) |')
w('|---|---|---|---|---|')
for l in new['lotes']:
    ps = l['pares']
    if not ps: w('| %s | 0 | — | — | — |' % l['id']); continue
    if 'id' in ps[0]: w('| %s | %d | %d | %s → %s | %s: %s × %s |' % (l['id'], len(ps), sum('id' in p for p in ps), ps[0]['id'], ps[-1]['id'], ps[0]['id'], ps[0]['a'][:40], ps[0]['b'][:40]))
    else: w('| %s | %d | 0 | — | — |' % (l['id'], len(ps)))
w('')
w('Remissões que o `id` resolve: A5-09 ("curso 8.2; par C1") e 5C-03 ("do par C1") → L5 C1; 5C-07 ("par C14") → L5 C14; 4C-08 ("o par injeção × jailbreak (C19)") → L4 C19. Nenhuma justificativa foi tocada.')
w('')
w('**`legendaMecanismo` por lote** (literal do canônico; inalterada desde a v1.3):')
w('')
w('| Lote | `legendaMecanismo` |')
w('|---|---|')
for l in new['lotes']:
    if 'legendaMecanismo' in l: w('| %s | %s |' % (l['id'], l['legendaMecanismo']))
w('')
w('L1, L1C, L2 e L3 não têm o campo (o arquivo canônico não traz legenda de mecanismo). **Topo do `SIM-1_gabarito.md` na v1.4** (T54-7):')
w('')
w('```text')
for x in E14['SIM-1_gabarito.md'].split('\n')[:9]: w(x)
w('```')
w('')
w('`avisos` do SIM-0 (3 strings, inalteradas; aviso 2 com a sublista; **não exibidos**):')
w('')
for k, a in enumerate(next(s for s in new['simulados'] if s['id'] == 'SIM-0')['avisos'], 1):
    w('%d. %s' % (k, a.replace('\n', '\n   ')))
w('')
w('### 13.5 Conferências por script (`conferencias_v14.py`; saídas em `saida/pacote/gerador_v1_4/out/`)')
w('')
w('%d conferências, %d falhas. Resultado por grupo:' % (NCONF, NCF))
w('')
w('| Grupo | Conferências | OK |')
w('|---|---|---|')
gr = collections.OrderedDict()
for c, alvo, ok, det in conf:
    g = re.match(r'^(\(\d\)|BASE)', c).group(1)
    gr.setdefault(g, [0, 0]); gr[g][0] += 1; gr[g][1] += ok
NOMEG = {'BASE': 'base: SHA-256 da v1.3', '(1)': '(1) diff v1.3 → v1.4 do pacote (nome, `id`, D5, curso do L3)', '(2)': '(2) contrato v1.2.1 → v1.2.2 (T54-1)', '(3)': '(3) diff v1.3 → v1.4 da edição, fidelidade, reconstrução 43/43 e testes T54-3 a T54-8', '(4)': '(4) varreduras de não regressão, exceções fechadas da R1 e conferências do QA da T-56', '(5)': '(5) contagens iguais às da v1.3 e da v1.2'}
for g, (n, k) in gr.items(): w('| %s | %d | %d |' % (NOMEG[g], n, k))
w('')
w('Conferências dos grupos BASE, (1), (2) e (3), na íntegra (as demais estão em `out/conferencias_v14.txt`):')
w('')
for c, alvo, ok, det in conf:
    if c.startswith(('(1)', '(2)', '(3)')) or c == 'BASE': w('- %s %s — %s%s' % ('OK' if ok else '**FALHA**', c, alvo, (' — ' + det[:300]) if det else ''))
w('')
w('Resultados dos demais scripts: `validate.py` %d verificações, %d falhas (as 107 da v1.3 com os rótulos de v1.4, mais 5 novas: chaves dos pares com `id`, ids contra o canônico, remissões por id, `a`/`b`/`como` iguais aos da v1.1 salvo a errata oficial já aplicada, errata T-58 do L3; e 2 ajustadas: discursivas e anexo da D5); `estudante_fidelidade.py` %d comparações, %d diferenças (exceções fechadas usadas: CAIXA 8 trocas, nota de BQ-0003 4 exibições, REALINHA 2 linhas; marcas residuais %d, as mesmas da v1.3: "a tecla F4" e "O F4 afirma que"); `sync_check.py` TUDO OK; `fidelidade_mutacao.py` %d mutações, todas detectadas (%d diferenças no total).' % (NVAL, NVF, fid['total'], fid['diferencas'], len(fid['restos']), mut['mutacoes'], mut['diferencas_detectadas']))
w('')
w('Conferência (f), regeração byte a byte numa cópia limpa do repositório (`git clone` + contrato v1.2.2, registro do contrato e fontes do `gerador_v1_4/` sem `out/`, em outra pasta e com `PYTHONHASHSEED` variados), está registrada no `MANIFESTO.md` (o relatório não pode conter o resultado da própria regeração).')
w('')
w('### 13.6 Estado e SHA-256')
w('')
w('| Objeto | SHA-256 | bytes |')
w('|---|---|---|')
w('| `saida/pacote/pacote.json` v1.3 (git `%s`) | `%s` | %d |' % (refs.C_V13, SHA_V13, SIZE_V13))
w('| `saida/pacote/pacote.json` v1.4 | `%s` | %d |' % (SHA_NEW, SIZE_NEW))
w('| `saida/estudante/` v1.3 (%d arquivos; manifesto ordenado) | `%s` | — |' % (len(E13), MAN13))
w('| `saida/estudante/` v1.4 (%d arquivos; manifesto ordenado) | `%s` | — |' % (NF, MAN14))
w('| `regras/pacote_contrato.md` v1.2.1 (git `%s`) | `%s` | %d |' % (refs.C_V13, SHA_CTR_A, len(CTR_ANTES)))
w('| `regras/pacote_contrato.md` v1.2.2 | `%s` | %d |' % (SHA_CTR_D, len(CTR_DEPOIS)))
w('')
w('O SHA-256 do próprio relatório e o manifesto de arquivos do gerador estão em `saida/pacote/gerador_v1_4/MANIFESTO.md` (o relatório não pode conter o próprio hash).')
w('')
w('### 13.7 O que NÃO mudou (T54, "Pontos que NÃO mudam")')
w('')
w('L6A 135, L5 119 e 126, L3 101 e 574 (D-T54-06 a, b, d); os campos `a`, `b`, `como` dos pares no pacote; o valor da `nota` no pacote; o desalinhamento canônico da linha "Tradução p/ inglês" do quadro do L1; a legenda nos gabaritos de lote (D-T56-02); os avisos do SIM-0 (não exibidos; matéria do Fundador, D-T56-03). Itens: 286 com enunciado, comando, `comandoOriginal`, `textoBase`, gabarito, justificativa, itemEdital, aderência, `volatil` e `nota` idênticos; simulados idênticos; pegadinhas 262.')
w('')

# ------------------------------------------------------------------ apêndice A
w('## Apêndice A — regras literais da edição do estudante (trecho apagado em ⟦ ⟧)')
w('')
w('Só as regras **vigentes** da v1.4 (%d regras literais), na ordem de aplicação. Cada linha: fase, tipo, escopo, contexto e trecho apagado; todas verificadas como deleção pura (a especificação é uma subsequência do original). Fora desta lista, por desenho: as regras nº 6 ("O F4 afirma que …", restaurada na L4-11, C-13), nº 26 ("(corrigido pela O-3)" do curso 4.3.4) e nº 63 ("conferida pela QA" da seção ITENS REAIS), retiradas na R1 (C-13, C-14); as nº 42, 44 e 51 da R0 (L6A) constam abaixo na forma da C-16; as duas regras da N-1 (`L6B_estudo`) vieram da v1.3. **Mudanças da v1.4 nesta lista:** a regra do 6B-06 passa a apagar o parêntese inteiro (T54-6); o rótulo do anexo da D5 apaga " (GCE, R3–R4)" (a regra " (GCE, R2–R4)" vale para a D4); as regras que só existiam por causa da nota R2 na D5 deixam de casar nesse trecho (a nota não está mais lá). Conferido por programa: nenhuma regra vigente contém os textos das três retiradas.' % len(em.LITERAL))
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
w('**Lista REALINHA (v1.4, D-T54-02; exceção fechada, só espaços inseridos num único ponto imediatamente antes de um `|`; não é remoção; escopo `L1_estudo`; cada regra casa exatamente 1 vez):**')
w('')
for esc, antes, depois in em.REALINHA: w('- `%s` → `%s` (+%d espaços)' % (antes, depois, len(depois) - len(antes)))
w('')
w('Nota: "n" não é repetido aqui porque as regras da fase "post" casam com o texto já tratado pelas regras genéricas; as ocorrências efetivas de cada tipo estão na seção 10.1.')
w('')

# ------------------------------------------------------------------ fim
w('## Pendências')
w('')
w('- QA: a gbq-cqe confere a v1.4 (fidelidade do pacote e da edição às fontes e à v1.3, o escopo exato da ocorrência, a errata do contrato v1.2.2 e os itens T54-1 a T54-8); a gce-cqfp confere a parte da GCE (item 5: a errata do curso do L3 e o anexo da D5) por script próprio; a gbq-gerencia reconcilia e emite o gatilho A da v1.4. Nada disso foi feito aqui.')
w('- Arquivos do repositório criados ou alterados por esta ocorrência: `saida/pacote/pacote.json`, `saida/estudante/` (regerada), `saida/pacote/pacote_relatorio_2026-10-13_v1_4.md`, `saida/pacote/gerador_v1_4/` (com `MANIFESTO.md`), `regras/pacote_contrato.md` (só a errata v1.2.2) e `saida/pacote/contrato_v1_2_2_2026-10-13.md`. Nenhum outro; a secretaria deve atualizar o estado. A promoção de `out/` para o repositório foi um passo explícito, depois de todas as conferências com 0 falhas.')
open(os.path.join(OUT, 'pacote_relatorio_2026-10-13_v1_4.md'), 'w', encoding='utf-8').write('\n'.join(o) + '\n')
print(len(o), 'linhas')
