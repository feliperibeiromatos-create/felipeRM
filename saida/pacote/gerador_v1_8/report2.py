# -*- coding: utf-8 -*-
"""HISTÓRICO (T-48; relatório do pacote v1.2, gerado com o texto da R0). Substituído por relatorio_v1_3.py (N-3). T-56: sem caminho absoluto;
a v1.1 vem do git (refs.py); a saída vai para out/historico_report2_v1_2.md."""
import json, os, re, hashlib, collections, difflib
import estudante_marcas as em
import estudante_gen as gen

import refs
from common import HERE as H, REPO
ROOT = REPO + '/'
new = json.load(open(H + '/out/pacote.json', encoding='utf-8'))
old = refs.v11()
st = json.load(open(H + '/out/stats.json', encoding='utf-8'))
val = json.load(open(H + '/out/validate.json', encoding='utf-8'))
ec = json.load(open(H + '/out/estudante_contagem.json', encoding='utf-8'))
fid = json.load(open(H + '/out/estudante_fidelidade.json', encoding='utf-8'))
sync = open(H + '/out/sync_check.txt', encoding='utf-8').read()
SIZE_NEW = os.path.getsize(H + '/out/pacote.json')
SIZE_OLD = len(refs.git_show(refs.C_V11, refs.PACOTE))
SHA_OLD = refs.sha256(refs.C_V11, refs.PACOTE)

o = []
w = o.append
def sha(path):
    return hashlib.sha256(open(ROOT + path, 'rb').read()).hexdigest()[:12]
LOTES = [l['id'] for l in new['lotes']]
LOTE_OF = gen.lote_of

# ------------------------------------------------------------------ cabeçalho
w('# pacote_relatorio_2026-10-13.md — T-48 — EXPORTAR v1.2 — gerado por gbq-csc')
w('')
w('Saídas: `saida/pacote/pacote.json` (versao 1, nome "%s", geradoEm %s, %d bytes UTF-8, indent=1, newline final), este relatório e a edição do estudante em `saida/estudante/` (43 arquivos). Contrato: `regras/pacote_contrato.md` v1.1.1 + Regras da v1.2 (D-T12-V12; D1 da GBQ, 13/10/2026). Gerador e validadores: scripts Python no scratchpad da sessão (fora do repositório). Nada foi commitado; TAREFAS.md, PARA_PRESIDENCIA.md, DECISOES.md, estado/, banco/, regras/ e os canônicos dos lotes não foram alterados. A v1.1 foi guardada antes de ser sobrescrita (SHA-256 `%s`, %d bytes). Nada deste pacote nem da edição do estudante vai à candidata sem gatilho A e decisão do Fundador; a edição do estudante NÃO é entrega à candidata.' % (new['nome'], new['geradoEm'], SIZE_NEW, SHA_OLD[:12], SIZE_OLD))
w('')
w('Resultado em uma linha: **286 itens** (106 de banco + 180 AUTORAL), 10 lotes, 5 discursivas, 4 simulados com `n` e `versao`; 32 registros de errata (31 APLICADA, 1 JÁ PRESENTE, 0 NÃO ENCONTRADA) e 6 erratas com alvo fora do pacote; validação por script: %d verificações, %d falhas; edição do estudante: 43 arquivos, fidelidade textual %d comparações, %d diferenças.' % (len(val), sum(1 for v in val if not v['ok']), fid['total'], fid['diferencas']))
w('')

# ------------------------------------------------------------------ 1. fontes
w('## 1. Fontes')
w('')
w('Lidas em 13/10/2026 (SHA-256, 12 primeiros dígitos). O arquivo canônico de cada lote é o da tabela de fonte do contrato (regra 4 da v1.1); os `saida/lote*/RECONCILIADO.md` não existem e não são fonte.')
w('')
w('| Objeto | Arquivo(s) | Versão / observação | SHA-256 (12) |')
w('|---|---|---|---|')
FONTES = [
 ('Contrato', 'regras/pacote_contrato.md', 'v1.1.1 + Regras da v1.2 (a–j)'),
 ('Instruções da T-48', 'saida/banco/GBQ_reconciliacao_2026-10-13.md', 'seção "INSTRUÇÕES PARA A T-48" e D1-a/b/c'),
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
 ('L4', 'saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md', 'v3.4 (cabeçalho: Despacho 9, 09/10/2026)'),
 ('L4C', 'saida/gcb/GCB_Lote4C_v1_GCB-CPP.md', 'v1.1 (só itens AUTORAL)'),
 ('L5', 'saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md', 'v3 com a errata Tukey (T-47) já gravada'),
 ('L5C', 'saida/gcb/GCB_Lote5C_v1_GCB-CPP.md', 'v1.1 (só itens AUTORAL)'),
 ('L6A', 'saida/gcb/GCB_Lote6a_v2_producao_auto.md', 'v2 (T-17)'),
 ('L6B', 'saida/gcb/GCB_Lote6b_v2_producao_auto.md', 'v2 com errata A-6b-1 (T-17)'),
 ('Banco', 'banco/banco.csv', '112 linhas; colunas texto_comando, texto_base, aderencia (T-29/T-42, D1-b)'),
 ('SIM-0', 'saida/simulados/simulado_0_v0.2.md', 'v0.2 com o ajuste T-36'),
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
 ('Relatório anterior', 'saida/pacote/pacote_relatorio_2026-10-10.md', 'base de comparação (v1.1)'),
]
for obj, f, ob in FONTES:
    w('| %s | `%s` | %s | `%s` |' % (obj, f, ob, sha(f)))
w('| v1.1 (antes) | `saida/pacote/pacote.json` | sobrescrito só depois de validado; cópia no scratchpad | `%s` |' % SHA_OLD[:12])
w('')
w('Condições do contrato (regra 5 e instrução da T-48), conferidas em `TAREFAS.md`: T-13, T-25, T-29, T-36, T-38, T-42, T-43, T-44, T-46 e T-47 CONCLUÍDAS e reconciliadas; T-40 CONCLUÍDA (BQ-0072, 0077, 0084, 0109, 0110 e 0111 entram, com 6/6 gabaritos sustentados). Simulados canônicos por D-SIM1-CANONICO, D-SIM2-CANONICO e D-SIM0P2-DIAGNOSTICO; SIM-0 v0.2 sem pendência (T-36 aplicada). Liberar qualquer simulado à candidata continua reservado ao Fundador.')
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
O, N = cnt(old), cnt(new)
w('## 2. Contagens v1.1 → v1.2')
w('')
w('| Medida | v1.1 | v1.2 |')
w('|---|---|---|')
rows = [
 ('`versao` / `nome`', '1 / "%s"' % old['nome'], '1 / "%s"' % new['nome']),
 ('`geradoEm`', old['geradoEm'], new['geradoEm']),
 ('edital (entradas)', len(old['edital']), len(new['edital'])),
 ('itens (total)', O['n'], N['n']),
 ('itens CEBRASPE_ANALOGA (banco)', O['rot']['CEBRASPE_ANALOGA'], N['rot']['CEBRASPE_ANALOGA']),
 ('itens AUTORAL', O['rot']['AUTORAL'], N['rot']['AUTORAL']),
 ('gabarito C / E (total)', '%d / %d' % (O['C'], O['E']), '%d / %d' % (N['C'], N['E'])),
 ('gabarito C / E (banco)', '%d / %d' % (O['bC'], O['bE']), '%d / %d' % (N['bC'], N['bE'])),
 ('gabarito C / E (AUTORAL)', '%d / %d' % (O['aC'], O['aE']), '%d / %d' % (N['aC'], N['aE'])),
 ('aderência direta / parcial (total)', '%d / %d' % (O['dir'], O['par']), '%d / %d' % (N['dir'], N['par'])),
 ('aderência direta / parcial (banco; AUTORAL todos direta)', '%d / %d' % (O['bdir'], O['bpar']), '%d / %d' % (N['bdir'], N['bpar'])),
 ('`volatil: true` (total; banco + AUTORAL)', '%d (%d + %d)' % (O['vol'], O['bvol'], O['avol']), '%d (%d + %d)' % (N['vol'], N['bvol'], N['avol'])),
 ('`nota` (itens)', O['nota'], '%d (%s)' % (N['nota'], ', '.join(i['id'] for i in new['itens'] if i.get('nota')))),
 ('`comandoOriginal` (itens)', O['co'], N['co']),
 ('`textoBase` "nenhum" / "" / texto', '%d / %d / %d' % (O['tbn'], O['tbv'], O['tbt']), '%d / %d / %d' % (N['tbn'], N['tbv'], N['tbt'])),
 ('lotes / discursivas', '%d / %d' % (len(old['lotes']), len(old['discursivas'])), '%d / %d' % (len(new['lotes']), len(new['discursivas']))),
 ('pegadinhas (total)', sum(len(l['pegadinhas']) for l in old['lotes']), sum(len(l['pegadinhas']) for l in new['lotes'])),
 ('simulados', '%d (%s)' % (len(old['simulados']), ', '.join(s['id'] for s in old['simulados'])), '%d (%s)' % (len(new['simulados']), ', '.join(s['id'] for s in new['simulados']))),
 ('bytes', SIZE_OLD, SIZE_NEW),
]
for r in rows: w('| %s | %s | %s |' % r)
w('')
w('Banco: 112 linhas em `banco/banco.csv`; 106 exportadas (60 C / 46 E) e 6 excluídas por anulação (gabarito X): %s. Os 60 itens da v1.1 mantêm o mesmo `comando` e a mesma aderência (37 direta / 23 parcial, conferido); os 46 novos são BQ-0061… do terceiro lote de varredura (inclui BQ-0072, 0077, 0084, 0109, 0110 e 0111, liberados pela T-40). BQ-0049 a 0051 são os únicos com `textoBase` (a coluna `texto_base`); nos 283 demais `textoBase` é `""` (F2).' % ', '.join(x[0] for x in st['binfo']['excl']))
w('')
w('### 2.1 Itens por lote (AUTORAL) e `comandoOriginal`')
w('')
w('| Lote | AUTORAL | C | E | `volatil` | `comandoOriginal` | pegadinhas v1.1 → v1.2 | pares |')
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
w('| id | nome | tipo | `versao` | `n` | itens | C / E | `volatil` | parcial |')
w('|---|---|---|---|---|---|---|---|---|')
itd = {i['id']: i for i in new['itens']}
for s in new['simulados']:
    its = [itd[x] for x in s['itens']]
    w('| %s | %s | %s | %s | %d | %d | %d / %d | %d | %d |' % (s['id'], s['nome'], s['tipo'], s['versao'], s['n'], len(s['itens']),
      sum(1 for i in its if i['gabarito'] == 'C'), sum(1 for i in its if i['gabarito'] == 'E'), sum(1 for i in its if i.get('volatil')), sum(1 for i in its if i['aderencia'] == 'parcial')))
w('')
w('`n` = tamanho da lista `itens` em 4/4. `versao`: SIM-0 "v0.2" (cabeçalho do arquivo); SIM-1, SIM-2 e SIM-0-P2 "v1" (sem versão declarada, regra (e)). Nenhum simulado final contém item `volatil` ou `parcial`. O gabarito de cada posição do simulado (arquivos `*_gabarito.md`) é igual ao `gabarito` do item no pacote em 165/165 posições (60 + 40 + 40 + 25).')
w('')
w('### 2.3 Discursivas')
w('')
w('D1–D5 idênticas às da v1.1 (nada mudou nas 5): D1 questão (L1), D2 questão e D3 peça (L2), D4 questão e D5 peça (L3). Aspectos e quesitos conferidos: soma dos aspectos das questões 14,30 + 0,70 de apresentação = 15,00; peças 28,50 + 1,50 = 30,00. A observação "inferido pela EXEC" da D1 (Adendo 4) não é exportada: 0 ocorrência de "EXEC" nas discursivas. D3 e D5 são pareceres técnicos (gênero confirmado para analista e técnico; hipótese por analogia para o Cargo 11). Pesos por quesito são HIPÓTESE do Projeto.')
w('')

# ------------------------------------------------------------------ 3. erratas
w('## 3. Erratas (consolidações sincronizadas) — estado por errata')
w('')
w('Método: substituição exata do trecho "onde se lê" (X) pelo "leia-se" (Y), tolerante a quebra de linha, na ordem do arquivo; cada X deve ter exatamente 1 ocorrência livre (não contida em Y). Estados: **APLICADA** (X encontrado 1 vez e trocado por Y); **JÁ PRESENTE** (X ausente e Y já presente na fonte); **NÃO ENCONTRADA** (nem X nem Y: o script aborta); **FORA DO PACOTE** (o alvo da errata não é exportado; checado: X/Y não vão ao JSON). O gerador aborta em qualquer falha; **0 NÃO ENCONTRADA**. Conferência prévia: `sync_check` leu cada X/Y contra o texto da consolidação sincronizada em `saida/gce/` (resultado: TUDO OK, 27 linhas).')
w('')
DESC = {
 ('L1', 'E1'): 'Q07 (d): "diarização habilitada, por si só, sem amostras de voz de referência"',
 ('L1', 'E2'): 'Q08 (d): "e um sistema pode diarizar"',
 ('L1', 'E3'): 'Q11 (d): "e, eventualmente, de pistas prosódicas"',
 ('L1', 'E4a'): 'curso 1.1: WER "no cálculo usual, sobre texto normalizado…"',
 ('L1', 'E4b'): 'curso 1.1: "no cálculo usual ele ignora pontuação, e em qualquer convenção ignora locutores"',
 ('L1', 'E4c'): 'curso 1.1 (par/pegadinha): "No cálculo usual, pontuação e capitalização ficam fora do WER…"',
 ('L1', 'E5'): 'resumo (b), "CLM (texto; indisponível para pt-BR na AWS)"',
 ('L1', 'E9'): 'curso 1.2: espectrograma "em geral (por exemplo, no Whisper)"',
 ('L1', 'E10'): 'curso 1.8: "departamento de registro da Câmara (Derep, antigo DETAQ; Ato da Mesa nº 251/2026)"',
 ('L1', 'E12'): 'resumo (b), WER: "no cálculo usual, sobre texto normalizado, não mede pontuação nem capitalização; locutor fica fora…" (T-46)',
 ('L1C', 'E1'): '(d-G) justificativa: reforço por LLM não implica áudio como modalidade do próprio LLM',
 ('L1C', 'E3'): 'curso: "end-to-end, não há dicionário de pronúncias separado"',
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
 ('L3', 'E1b'): 'curso 4.1: art. 20, "expressão suprimida (MP nº 869/2018, convertida na Lei 13.853/2019)"',
 ('L3', 'E2'): 'curso 4.1: "o art. 5º, II, enumera origem"',
 ('L3', 'E3a'): 'curso 4.1: "a MP nº 869/2018, convertida na Lei 13.853/2019, suprimiu a expressão"',
 ('L3', 'E3b'): 'curso 4.1: idem, "da redação original"',
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
w('Totais: os registros de substituição do gerador são 32 (%d APLICADA e %d JÁ PRESENTE, a única sendo o Adendo 2 no 3.1); 0 NÃO ENCONTRADA. As três últimas linhas da tabela (E8, T-44, T-47) são informativas: E8 é a montagem da D1 (APLICADA, sem substituição) e T-44 e T-47 já estavam gravadas nos arquivos canônicos (JÁ PRESENTE); somadas, a tabela tem 35 linhas, das quais 32 APLICADA ou JÁ PRESENTE por substituição do gerador. Para cada APLICADA o script confere depois que Y consta do JSON e X não consta (fora das ocorrências de Y): validação "erratas: Y presente / X ausente", OK.' % (n_ap, n_ja))
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
w('- **F4 (marcas internas das justificativas): feita em 18 justificativas** (a gatilho A dizia 17 "entre outras"), ver seção 6.')
w('- **F5 ("Derep (antigo DETAQ)"): feita.** 1 substituição no L1 (curso 1.8, E10 já com a forma "Derep, antigo DETAQ" → "Derep (antigo DETAQ)"); 0 "Derep, antigo DETAQ" no JSON; a forma correta ocorre 13 vezes no JSON e nenhuma outra grafia de DETAQ fora dela.')
w('- **D1-b (aderência explícita): feita.** Todo item de banco recebe `aderencia` da coluna do `banco.csv`, sem recálculo (106/106 iguais à coluna: 67 direta / 39 parcial). A regra por texto de `observacoes` deixou de valer para a exportação.')
w('- **D1-c (comando normalizado + `comandoOriginal`): feita em 90 itens** (L4 20, 4C 10, A5/L5 20, 5C 10, 6A 15, 6B 15; L1–L3 e banco: 0). Regex `(?i)(julgue os itens) (?:de )?(?:[0-9A-Z]+-)?\\d+ a (?:[0-9A-Z]+-)?\\d+\\.` → "julgue os itens a seguir."; o resto da frase fica literal e o literal vai em `comandoOriginal`. Conferido: só o trecho da numeração muda; BQ-0070, 0071 e 0112 ficam com o comando inteiro e sem `comandoOriginal`; nenhum comando restante com faixa de itens.')
w('')

# ------------------------------------------------------------------ 5. diff por lote
w('## 5. Diff textual resumido v1.1 → v1.2 por lote')
w('')
w('Campos de lote comparados caractere a caractere (difflib). Campos não citados: idênticos.')
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
        w('- pegadinhas: %d → %d entradas (desdobramento da F3), todas com `rotulo`.' % (len(ol[lid]['pegadinhas']), len(l['pegadinhas'])))
    w('')
w('Itens (campo a campo, v1.1 → v1.2): `textoBase` 237 (F2, "nenhum" → ""), `comando` 90 e `comandoOriginal` 90 (D1-c), `justificativa` 18 (F4), `nota` 2 (BQ-0003, BQ-0040), `enunciado` 1 (L1-Q04, F1). `gabarito`, `aderencia` (nos 60 da v1.1), `itemEdital`, `rotulo`, `certame`, `cargo`, `ano`, `numero` e `url`: 0 diferença. Discursivas: 0 diferença. Edital: igual.')
w('')

# ------------------------------------------------------------------ 6. F4
w('## 6. F4 — justificativas alteradas (antes / depois)')
w('')
w('Só deleção (conferido por difflib: nenhuma inserção nem troca); cada trecho a apagar ocorre exatamente 1 vez; depois da deleção, sem espaço duplo nem espaço antes de pontuação; 0 marca de processo (CQFP/CQE/CPP/GCE/GCB/GBQ/EXEC, T-xx, "(vN", Oxx, "Lição", R-4C1, "Risco") remanescente nas justificativas. **18 justificativas** (o gatilho A dizia 17 e listava 12 nominalmente, "entre outras"): as 12 nomeadas (L2-Q23, L4-08, 09, 13, 15, 17, 18, 19, 20, 4C-06, 08, 09) mais A5-14, 15, 16, 17, 5C-03 e 5C-06, que também tinham "Risco …", "R-5C1" ou "Lição O10". Pode-se contar 17 se A5-14 a A5-17 forem tomados como um bloco de 3 ou se a L2-Q23 não for contada; registro em DÚVIDA 1.')
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
w('| Lote | entradas v1.1 → v1.2 | modos de origem (entradas da v1.1) |')
w('|---|---|---|')
modo = collections.defaultdict(collections.Counter)
for e in st['peg']: modo[e['lote']][e['modo']] += 1
for l in new['lotes']:
    w('| %s | %d → %d | %s |' % (l['id'], len(ol[l['id']]['pegadinhas']), len(l['pegadinhas']), ', '.join('%s %d' % (k, v) for k, v in modo[l['id']].items()) or '—'))
w('')
w('Texto corrido que não se separa sem reescrever (ficou como uma entrada só, por contrato): L1 P2-1.1, P2-1.2, P2-1.4 e P2-1.7 (frases soltas "Outra:", "Também:", sem separador marcado). Enumeradores cujo conteúdo tem ";" interno ficaram íntegros (precedência do enumerador): L1 P2-1.3 (1), L2 P2-2.6 (6) e L3 P2-4.3 (2). Assertiva única com ";" dentro do parêntese, mantida inteira: L6A, slide mestre (`"…" → ERRADO (guia Exibir; F7) — VOLÁTIL`). L4, L6A e L6B já tinham uma pegadinha por entrada (contagem igual).')
w('')
dep = []
for l in new['lotes']:
    prev = None
    for i, g in enumerate(l['pegadinhas']):
        k = (g['itemEdital'], g['rotulo'])
        if k == prev and re.match(r'^(que|empilhado)\b', g['texto']):
            dep.append((l['id'], i, g['rotulo'], g['texto']))
        prev = k
w('Fragmentos que dependem do verbo ou do sujeito do fragmento anterior (efeito do ";" sem reescrita; DÚVIDA 3): ' + '; '.join('%s [%d] (%s) "%s"' % (a, b, c[:30], d[:55]) for a, b, c, d in dep) + '. Os demais fragmentos de L5 começam por infinitivo e se leem soltos.')
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
w('Gerada a partir do `pacote.json` v1.2 (fonte única). **43 arquivos**: `README.md` (índice, versão v1.2, data 2026-10-13, aviso "material de estudo; gabaritos em arquivo separado"); por lote, `<ID>_estudo.md` (itens do edital, resumo, curso, pares, pegadinhas com rótulo), `<ID>_itens.md` (comando, texto-base se houver, enunciado; sem gabarito, justificativa nem marcas) e `<ID>_gabarito.md` (gabarito, item do edital e justificativa) para L1, L1C, L2, L3, L4, L4C, L5, L5C, L6A e L6B (30 arquivos); `BANCO_itens.md` e `BANCO_gabarito.md` (certame, cargo, ano, número, URL oficial, aviso VOLÁTIL e `nota` literal); por simulado `<SIM>_folha.md` e `<SIM>_gabarito.md` (SIM-0, SIM-1, SIM-2, SIM-0-P2); `DISCURSIVAS.md` e `DISCURSIVAS_padrao.md`. Resumo e curso vão em blocos de texto cercados, para preservar quebras, recuos e tabelas.')
w('')
w('**Regra:** as marcas internas saem SOMENTE POR DELEÇÃO (nunca reescrita) por `estudante_marcas.py`; a marca VOLÁTIL vira, nos itens `volatil: true`, o aviso fixo "Atenção: conteúdo sujeito a mudança; será reverificado em janeiro de 2027."; a `nota` (BQ-0003, BQ-0040) é exibida literal junto do item. Enunciado, comando e texto-base de item não são tocados (afirmado por teste: nenhuma marca da lista neles). Regras genéricas (por tipo) e regras literais (frase ou cláusula a apagar, `⟦…⟧` na especificação):')
w('')
w('- `[V dd/mm/aaaa — …]` apagado inteiro, com o espaço anterior (o colchete pode quebrar linha entre "[V" e a data); duas exceções que mantêm a orientação ao estudante: `[V … — F4; NORMATIVO — QA; norma de caráter experimental, não cobrar o texto]` fica `[norma de caráter experimental, não cobrar o texto]` e `[V … contexto histórico]` fica `[contexto histórico]`.')
w('- `[NORMATIVO — QA: base legal]` perde o prefixo e o colchete e fica a base legal ("LGPD, art. 5º, I."); `[NORMATIVO — QA]` e as variantes com ";" são apagadas (`[NORMATIVO — QA; não cobrar além do texto]` fica `[não cobrar além do texto]`); a frase "…com a marca [NORMATIVO — QA]. Fontes: F1 … lidas em 08/10/2026." do L3 sai, ficando "Todos os dispositivos abaixo estão em paráfrase."')
w('- Referências de fonte F1…F22: `[Fn]`, `(Fn)`, `(Fn, Fm)`, `(Fn, verificado em …)`, `(Fn, seção …)`, `, Fn)` no fim de parêntese, `; Fn)`, `(Fn: ` e `(Fn, "…")` (mantém o parêntese e o conteúdo), "Conforme a Fn (leitura de …):", frases "Fonte(s): Fn, …verificado em …." e, em trechos de prosa (89 regras literais no total), a cláusula ou palavra que só existe por causa da referência (lista completa no apêndice A). "A tecla F4" (Excel) NÃO é referência e permanece.')
w('- Agentes e unidades (CQFP, QA, GCB, GCE, CPP) em carimbos como "(conferido pela CQFP em 08/10/2026)", "conforme a CQFP", "(GCB-CPP)", "Decisão da GCE", "versão da CPP", "para o QA Normativo", "Síntese da CQFP … colado pelo Fundador"; ids internos "(errata E1)", "; E3" em "(N1; E3)", "(O11)", "(corrigido pela O-3)", "(D-T2)", "(R4 do Projeto)" e, nos padrões D4/D5, "(GCE, R2–R4)" e os enumeradores "R2. ", "R3. ", "R4. ".')
w('- Carimbos datados ligados a uma referência apagada ("verificadas em 7/10/2026", "(reverificado em …)", "conforme a leitura de 08/10/2026", "(conferido no Planalto em …)").')
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
# contagem única (nível do pacote)
uniq = collections.Counter()
for path, t in __import__('texts').walk(new):
    if path == '.nome' or path.endswith('.url') or path.endswith('.nota') or path.endswith('.enunciado') or path.endswith('.comando') or path.endswith('.textoBase') or path.endswith('.comandoOriginal'): continue
    em.strip_text(t, uniq)
w('Contagem única por campo do pacote (sem repetir a justificativa que aparece em lote e em simulado): **%d** ocorrências.' % sum(uniq.values()))
w('')
w('Arquivos sem nenhuma remoção: os `*_itens.md`, `BANCO_*`, `*_folha.md`, `README.md` e os `*_gabarito.md` cujos itens não tinham marca (a tabela só lista os arquivos com remoção).')
w('')
w('### 10.2 Fidelidade (script `estudante_fidelidade.py`)')
w('')
w('O script lê os 43 arquivos com um parser próprio (independente do gerador) e confere, campo a campo, o texto do estudante com o do pacote: (1) igual ao texto do pacote com as deleções das regras; (2) obtido do texto do pacote só por deleção (difflib: apenas `equal`/`delete`; 0 `insert`/`replace`); (3) comando, texto-base, enunciado, gabarito, item do edital, aderência, nota, aviso VOLÁTIL, certame, cargo, ano, número, URL, ordem e `n` dos simulados, valores dos aspectos e conceitos dos quesitos idênticos ao pacote. Teste negativo (mutação de 3 arquivos) detectou 9 diferenças, portanto o script não é cego.')
w('')
w('- comparações: %s (total %d)' % (', '.join('%s %d' % (k, v) for k, v in fid['comparacoes'].items()), fid['total']))
w('- **diferenças: %d** (texto do estudante == texto do pacote com as deleções aplicadas)' % fid['diferencas'])
w('- marcas residuais nos arquivos pela varredura de higiene (V, NORMATIVO — QA, [TS], CQFP/CQE/CPP/GCE/GCB/GBQ/EXEC, F1…F22, T-/R-/E-/O-xx, "(errata En)"): %d, a saber: %s.' % (len(fid['restos']), '; '.join('%s linha %s "%s" (tecla do Excel, não é referência)' % (r[0], r[1], r[2]) for r in fid['restos'])))
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
w('**Na edição do estudante, fora da lista de marcas pedida, permanecem (DÚVIDA 5):** códigos de nota "N1…N9" do curso de L2, L3 e L4 (definidos no próprio texto; ex.: "LGPD (N1, Lei 13.709/2018)"); códigos de fonte do L5 "U1…U6", "TB2", "GG4", "CI" e o carimbo "(verificado em 8/10/2026)" que os acompanha; as etiquetas de mecanismo das justificativas ("GI", "TC", "IC", "AT"); "REVERIFICAR (normativo) 04–08/01/2027; não VOLÁTIL" (L3-Q21) e "NÃO VOLÁTIL"/"não VOLÁTIL"/"Sem marca VOLÁTIL" nas justificativas L2-Q23, L3-Q21 e L4-05; as palavras "VOLÁTIL" de títulos do curso do L4, L5 e L6A (ex.: "— VOLÁTIL"); e a expressão "aberta hoje" (leitura de fonte) no curso do L6B.')
w('')

# ------------------------------------------------------------------ 12. DUVIDAS
w('## 12. DÚVIDAS para a GBQ')
w('')
D = [
 ('F4: 18 em vez de 17.', 'A varredura achou 18 justificativas com marca de agente, risco ou lição; o gatilho A falava em 17 "entre outras". Apliquei as 18. Se a GBQ quiser 17, diga qual excluir (candidata natural: nenhuma; todas têm marca). Efeito: só deleção.'),
 ('F4: inicial minúscula depois de "Lição O10: ".', '4C-08 e 5C-06 ficam com a frase começando em minúscula, porque a deleção pura impede maiúscula. Aceitar, ou autorizar a capitalização (seria troca de letra, contra a regra de só deleção).'),
 ('F3: fragmentos dependentes e entradas não desdobradas.', 'O desdobramento por ";" dá fragmentos que começam por "que …" (L5, box plot [34]–[36]) e "empilhado quando…" (L5 [29]), que só se leem junto do verbo do fragmento anterior. As entradas P2 em texto corrido (L1 P2-1.1, 1.2, 1.4, 1.7) e os enumeradores com ";" interno (L1 P2-1.3, L2 P2-2.6, L3 P2-4.3) ficaram íntegros. Aceitar como está, ou mandar reescrita (fora da regra de literalidade).'),
 ('F3: rótulo por hierarquia.', 'Onde o texto canônico não tem bloco próprio usei o texto do edital (P2 e L4/L6B) ou o título do item do lote (L6A: WORD, EXCEL, …). Dois rótulos terminam em dois-pontos porque o texto do edital termina assim ("Desafios do ASR em Português Brasileiro:", "Ferramentas e APIs: …"). Aceitar.'),
 ('Marcas fora da lista (edição do estudante).', 'Não apaguei N1…N9, U1…U6/TB/GG/CI (L5), GI/TC/IC/AT, "NÃO VOLÁTIL", "REVERIFICAR", "aberta hoje" nem o carimbo "(verificado em 8/10/2026)" do L5, porque não estão na lista (F1..F9, [V…], [TS], NORMATIVO — QA, agentes, T/R/E/O-xx, Risco). Os códigos U/TB/GG/CI são o equivalente das F do L5; apagá-los é uma ampliação simples (flag no script). Decidir.'),
 ('"Risco …".', 'Nas justificativas AUTORAL a marca "Risco BAIXO/MÉDIO" foi apagada (F4). No curso e no resumo, "Risco/Riscos" é conteúdo de estudo (riscos de IA, de segurança) e foi mantido. Confirmar.'),
 ('Texto de lote que perdeu conteúdo substantivo ao apagar a fonte.', 'Algumas deleções tiraram citação ou observação de fonte além da etiqueta (ex.: L6A, "A F9 também usa os rótulos "Pode editar" e "Pode exibir""; L6A, a frase da F19 sobre a experiência do Teams; as citações em inglês da F4 na L4-11; justificativas 4C-02, 4C-03, 4C-07, 6B-07, 6B-08, 6B-09, 6B-10 e 6B-13 com a frase "Fonte: …" inteira; citações de fonte em L4-07, L4-11, L4-13, 4C-04 a 4C-06, 6A-09, 6A-11, 6B-04, 6B-05, 6B-11, 6B-14 e 6B-15). Todas estão no apêndice A com o trecho apagado. Se a GBQ preferir manter alguma, o ajuste é remover a regra literal correspondente.'),
 ('Inicial minúscula e sujeito oculto após deleção.', 'Em poucos trechos do curso do L6A a deleção deixa a frase começando em minúscula ("por padrão os clientes POP3…", "mesclar combina…") ou sem sujeito explícito ("NÃO é possível mudar… e orienta excluir o link…"). Está no apêndice A; a leitura continua clara, mas o texto não foi retocado.'),
 ('Tabelas de colunas fixas.', 'Ao apagar `[F10]`, `[F12]` etc. de linhas do QUADRO-SÍNTESE do curso do L1, o alinhamento das colunas de texto monoespaçado desloca. Só estético; não retocado.'),
 ('Aviso VOLÁTIL em item de lote com `volatil` por REVERIFICAR normativo.', 'L3-Q21 e L4-15 etc. recebem o mesmo aviso fixo (janeiro de 2027). Confirmar que o aviso único serve também para REVERIFICAR normativo.'),
 ('Aderência dos itens de banco no estudante.', 'Mostrei "(aderência: direta|parcial)" no gabarito do banco e dos simulados. A GBQ pode preferir não mostrar. Decidir.'),
 ('Itens fora do exportado.', 'As seis erratas FORA DO PACOTE (seção 3.1) não têm um dos três estados do contrato; criei o quarto rótulo para elas. Confirmar.'),
 ('Alvo duplicado da E3a do L3.', 'O X da E3a tem 2 ocorrências no texto bruto do L3 (uma é eliminada pela E1b na aplicação em sequência). O gerador aplica em sequência e a ocorrência restante é a visada. Confirmar com a GCE se a ordem E1b → E3a é a pretendida.'),
]
for i, (t, d) in enumerate(D, 1):
    w('%d. **%s** %s' % (i, t, d))
w('')

# ------------------------------------------------------------------ apêndice A
w('## Apêndice A — regras literais da edição do estudante (trecho apagado em ⟦ ⟧)')
w('')
w('Cada linha: tipo, contexto e trecho apagado; todas verificadas como deleção pura (a especificação é uma subsequência do original) e com pelo menos 1 ocorrência no texto (conferido pelo gerador, que aborta se alguma regra não ocorrer).')
w('')
sp = {}
def n_occ(old_):
    n = 0
    for path, t in __import__('texts').walk(new):
        if path == '.nome' or path.endswith('.url') or path.endswith('.nota'): continue
        n += t.count(old_)
    return n
import difflib as _d
w('| # | Fase | Tipo | Original (contexto) → apagado |')
w('|---|---|---|---|')
for k, (fase, tipo, old_, new_) in enumerate(em.LITERAL, 1):
    sm = _d.SequenceMatcher(None, old_, new_, autojunk=False)
    parts = []
    for t, i1, i2, j1, j2 in sm.get_opcodes():
        if t == 'delete': parts.append('⟦%s⟧' % old_[i1:i2].replace('\n', '⏎'))
        elif t == 'equal': parts.append(old_[i1:i2].replace('\n', '⏎'))
    ctx = ''.join(parts)
    # em fase 'post' o original está depois das regras genéricas; n medido no texto já tratado
    w('| %d | %s | %s | %s |' % (k, fase, tipo, ctx.replace('|', '\\|')))
w('')
w('Nota: "n" não é repetido aqui porque as regras da fase "post" casam com o texto já tratado pelas regras genéricas; as ocorrências efetivas de cada tipo estão na seção 10.1.')
w('')

# ------------------------------------------------------------------ fim
w('## Pendências')
w('')
w('- QA: a gbq-cqe confere a fidelidade textual das edições do estudante e do pacote às fontes; o QA independente (modelo que não produziu) confere a aplicação das erratas por lote; depois a gbq-gerencia reconcilia e emite o gatilho A da v1.2 (T-48). Nada disso foi feito aqui.')
w('- Nenhum arquivo do repositório fora de `saida/pacote/pacote.json`, `saida/pacote/pacote_relatorio_2026-10-13.md` e `saida/estudante/` foi criado ou alterado; a secretaria deve atualizar o estado.')
open(H + '/out/historico_report2_v1_2.md', 'w', encoding='utf-8').write('\n'.join(o) + '\n')
print(len(o), 'linhas')
