# -*- coding: utf-8 -*-
"""T-108 e T-109 (gerador_v1_11) — chaves da ocorrência (D1 da GBQ, saida/pacote/T108_D1_pacote_M2_2026-10-18.md, seções 0, 1.2 e 3).
Único lugar em que o número da versão do pacote é escrito (conferência C-16). Lido por todos os passos do pipeline.
ENSAIO: as tabelas podem ser lidas sem o SHA-256 aceito; nada de out/ é promovido. FINAL exige todos os SHA preenchidos, ALVO == 'M2', VERSAO decidida (E5) e, se E_L2R16, ATO_L2R16 presente em DECISOES.md."""
import os

VERSAO = '1.11'                       # E5: decisão do gatilho D da GBQ (numeração). Com a opção (b): '1.10.1'.
NOME = 'Câmara 2026 — pacote F4 (v%s)' % VERSAO
NOME_E = 'Câmara 2026 — pacote do estudante (v%s-E)' % VERSAO
TAG = 'v' + VERSAO.replace('.', '_')
ALVO = 'M2'                           # D-V15-C-M2: limpeza também no pacote.json; único valor admitido na geração final

# BASE: pacote.json v1.10 aceito (commit, caminho, SHA-256) e SHA-256 do pacote_estudante.json v1.10-E no mesmo commit
BASE = ('cacd606', 'saida/pacote/pacote.json', 'd43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed')
BASE_E = ('cacd606', 'saida/pacote/pacote_estudante.json', 'd8a68156f00e40c6a03937e678d2b3949c68c9ad24e8a7489ff883b5a3497b7f')
BASE_ESTUDANTE_DIR = 'saida/estudante'
BASE_NOME = 'Câmara 2026 — pacote F4 (v1.10)'
BASE_ITENS = 560

OCORRENCIAS = ('saida/pacote/T108_ocorrencias.csv', '471aeec59ba26f17548ea2597298bec429aa8d9a78838fd646b7fa7936bde5c6')
UNIVERSO = 872                        # arquivo=pacote.json, classe PROCESSO ou VERIFICAR (GCE 293, GCB 575, GBQ 4)
FP_R1, FP_CONTEUDO = 28, 115          # no pacote.json

# tabelas de substituição: (gerência, caminho, SHA-256). SHA None = não fixado (gatilho A da Gerência pendente; só ENSAIO).
TABELAS_FINAL = [('GCE', 'saida/gce/T108_substituicoes_GCE.csv', None),
                 ('GCB', 'saida/gcb/T108_substituicoes_GCB.csv', None),
                 ('GBQ', 'saida/pacote/T108_substituicoes_GBQ.csv', None)]
# ENSAIO: tabelas feitas por ensaio/gera_tabelas_ensaio.py (linhas reais das Gerências onde existem e passam nas conferências, mais linhas sintéticas de ensaio)
TABELAS_ENSAIO = [('GCE', 'saida/pacote/gerador_v1_11/ensaio/T108_substituicoes_GCE_ensaio.csv', None),
                  ('GCB', 'saida/pacote/gerador_v1_11/ensaio/T108_substituicoes_GCB_ensaio.csv', None),
                  ('GBQ', 'saida/pacote/gerador_v1_11/ensaio/T108_substituicoes_GBQ_ensaio.csv', None)]
# tabelas em produção (lidas em ENSAIO só para o relatório de leitura real; podem não existir ou estar incompletas)
TABELAS_PRODUCAO = [('GCE', 'saida/gce/T108_substituicoes_GCE.csv'),
                    ('GCB', 'saida/gcb/T108_substituicoes_GCB_parteA.csv'), ('GCB', 'saida/gcb/T108_substituicoes_GCB_parteB.csv'),
                    ('GCB', 'saida/gcb/T108_substituicoes_GCB_parteC.csv')]
PREFIXOS = {'GCE': ('GCE-',), 'GCB': ('GCB-A', 'GCB-B', 'GCB-C'), 'GBQ': ('GBQ-',)}
# aceite do gatilho A e parecer do QA, por Gerência (id da decisão em DECISOES.md; arquivo do QA). Preenchidos na geração final.
ACEITE = {'GCE': None, 'GCB': None, 'GBQ': None}
PARECER_QA = {'GCE': None, 'GCB': None, 'GBQ': None}

T109 = ('saida/gce/T109_reconciliacao_2026-10-18.md', 'bb95046b0783eecf24b64814b2a2294ad65ace1050f0258d92df401f31a3eb84')
E_L2R16 = True                        # E4: aceite do gatilho D da GCE (T-109). Falso: o L2-R16 fica em P2-2.8.
ATO_L2R16 = None                      # id da decisão de aceite em DECISOES.md (obrigatório em FINAL se E_L2R16)

# exceções fechadas (registradas na reconciliação da Gerência titular): id_edicao -> lista de regex permitidas no `depois`; residual das listas de deleção antigas
EXCECOES_DEPOIS = {}
EXCECOES_RESIDUAL = {}

GERADO_EM = '2026-10-18'
FINAL = False
ENSAIO = not FINAL

TABELAS = TABELAS_ENSAIO if ENSAIO else TABELAS_FINAL


def confere_final():
    """Condições de entrada E1 a E5 (seção 0 da D1). Devolve a lista de pendências (vazia = pode gerar a versão final)."""
    p = []
    if ALVO != 'M2':
        p.append('ALVO != M2')
    for g, c, h in TABELAS_FINAL:
        if not h:
            p.append('E1-E3: SHA-256 da tabela %s não fixado' % g)
    if E_L2R16 and not ATO_L2R16:
        p.append('E4: ATO_L2R16 ausente')
    if not VERSAO:
        p.append('E5: VERSAO não decidida')
    return p

if ENSAIO:      # exceções do depois das linhas sintéticas de ensaio (gravadas por ensaio/gera_tabelas_ensaio.py); na geração final, só a lista fechada da reconciliação
    import json as _json
    _pe = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ensaio', 'excecoes_ensaio.json')
    if os.path.exists(_pe):
        with open(_pe, encoding='utf-8') as _f:
            EXCECOES_DEPOIS = _json.load(_f)
