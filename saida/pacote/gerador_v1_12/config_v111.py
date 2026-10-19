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
UNIVERSO = 907                        # 872 do inventário (GCE 293, GCB 575, GBQ 4) + 35 ids fora do inventário (IDS_EXTRA: GCE 13, GCB 22)
FP_R1, FP_CONTEUDO = 28, 115          # no pacote.json

# tabelas de substituição: (gerência, caminho, SHA-256). SHA None = não fixado (gatilho A da Gerência pendente; só ENSAIO).
TABELAS_FINAL = [('GCE', 'saida/gce/T108_substituicoes_GCE_v3.csv', '77ad3ac331ec120c6fb086c0b3f7c05cb77776c1e06b3dcaa6df2ab1d52fc599'),
                 ('GCB', 'saida/gcb/T108_substituicoes_GCB.csv', '10d9e5588753bc9ad273a529b56148b20e1f643bb4f312751a8fbd371b8751ef'),
                 ('GBQ', 'saida/pacote/T108_substituicoes_GBQ.csv', '528eb620dc6c95e1e27390fe90774acb861e391a467ff969932cd12f97a323dd')]
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
ACEITE = {'GCE': 'D-T108-GCE-TABELA', 'GCB': 'D-T108-GCB-TABELA', 'GBQ': 'D1 da GBQ (T108_D1_pacote_M2, 1.9; T108_D1_pre_FINAL, 3)'}
PARECER_QA = {'GCE': ['saida/gce/QA_T108_R1_2026-10-18_gce-cqfp.md', 'saida/gce/QA_T108_R2_2026-10-18_gce-cqfp.md'],
              'GCB': ['saida/gcb/QA_T108_R1_parteA_2026-10-18_gcb-cqfp.md', 'saida/gcb/QA_T108_R1_parteB_2026-10-18_gcb-cqfp.md', 'saida/gcb/QA_T108_R1_parteC_2026-10-18_gcb-cqfp.md',
                      'saida/gcb/QA_T108_R2_parteA_2026-10-18_gcb-cqfp.md', 'saida/gcb/QA_T108_R2_parteB_2026-10-18_gcb-cqfp.md', 'saida/gcb/QA_T108_R2_parteC_2026-10-18_gcb-cqfp.md'],
              'GBQ': None}

T109 = ('saida/gce/T109_reconciliacao_2026-10-18.md', 'bb95046b0783eecf24b64814b2a2294ad65ace1050f0258d92df401f31a3eb84')
E_L2R16 = True                        # E4: aceite do gatilho D da GCE (T-109). Falso: o L2-R16 fica em P2-2.8.
ATO_L2R16 = 'D-T109-L2R16-ACEITE'                      # id da decisão de aceite em DECISOES.md (obrigatório em FINAL se E_L2R16)

# exceções fechadas (registradas na reconciliação da Gerência titular): id_edicao -> lista de regex permitidas no `depois`; residual das listas de deleção antigas
EXCECOES_DEPOIS = {}      # lista vazia (reconciliações GCE e GCB)
EXCECOES_RESIDUAL = {'carimbo datado de verificação/leitura (ligado a F-ref)': 4, 'carimbo "Verificado em 8/10/2026" (L5)': 4, 'F (prosa: referência a fonte)': 1}
EXCECOES_RESIDUAL_CAMPOS = {'carimbo datado de verificação/leitura (ligado a F-ref)': ['lotes[L4].curso', 'lotes[L6A].curso'],
                            'carimbo "Verificado em 8/10/2026" (L5)': ['itens[A5-14].justificativa', 'itens[A5-15].justificativa', 'itens[A5-16].justificativa', 'itens[A5-17].justificativa'],
                            'F (prosa: referência a fonte)': ['lotes[L6A].curso']}
# ids de ocorrência fora do T108_ocorrencias.csv (35): id -> (Gerência, caminho). Lista fechada (D1 pré-FINAL, 1.3); caminho conferido contra a reconciliação da Gerência.
IDS_EXTRA = {'NAO_INVENTARIADA-01': ('GCE', 'lotes[L2].curso'), 'NAO_INVENTARIADA-02': ('GCE', 'lotes[L3].curso'), 'NAO_INVENTARIADA-03': ('GCE', 'discursivas[D4].padrao'), 'NAO_INVENTARIADA-04': ('GCE', 'discursivas[D4].padrao'), 'NAO_INVENTARIADA-05': ('GCE', 'discursivas[D5].padrao'), 'NAO_INVENTARIADA-06': ('GCE', 'itens[L2-R18].justificativa'), 'NAO_INVENTARIADA-07': ('GCE', 'discursivas[D3].padrao'), 'NAO_INVENTARIADA-08': ('GCE', 'discursivas[D4].padrao'), 'NAO_INVENTARIADA-09': ('GCE', 'discursivas[D5].padrao'), 'NAO_INVENTARIADA-10': ('GCE', 'lotes[L3].curso'), 'NAO_INVENTARIADA-11': ('GCE', 'lotes[L3].curso'), 'NAO_INVENTARIADA-12': ('GCE', 'discursivas[D1].padrao'), 'NAO_INVENTARIADA-13': ('GCE', 'discursivas[D2].padrao'), 'GCB-EXTRA-01': ('GCB', 'lotes[L4].curso'), 'GCB-EXTRA-02': ('GCB', 'lotes[L4].curso'), 'GCB-EXTRA-03': ('GCB', 'lotes[L4].curso'), 'GCB-EXTRA-04': ('GCB', 'itens[4C-10].justificativa'), 'GCB-EXTRA-05': ('GCB', 'lotes[L6A].curso'), 'GCB-EXTRA-06': ('GCB', 'lotes[L6A].curso'), 'GCB-EXTRA-07': ('GCB', 'lotes[L6A].curso'), 'GCB-EXTRA-08': ('GCB', 'itens[6A-08].justificativa'), 'GCB-EXTRA-09': ('GCB', 'itens[6A-11].justificativa'), 'GCB-EXTRA-10': ('GCB', 'lotes[L6A].curso'), 'GCB-EXTRA-11': ('GCB', 'lotes[L6A].curso'), 'GCB-EXTRA-12': ('GCB', 'lotes[L5].curso'), 'GCB-EXTRA-16': ('GCB', 'lotes[L6B].curso'), 'GCB-EXTRA-17': ('GCB', 'lotes[L6B].curso'), 'GCB-EXTRA-18': ('GCB', 'lotes[L6B].curso'), 'GCB-EXTRA-19': ('GCB', 'lotes[L6B].curso'), 'GCB-EXTRA-13': ('GCB', 'lotes[L6B].curso'), 'GCB-EXTRA-14': ('GCB', 'lotes[L6B].curso'), 'GCB-EXTRA-15': ('GCB', 'lotes[L6B].curso'), 'GCB-EXTRA-20': ('GCB', 'itens[6B-06].justificativa'), 'GCB-EXTRA-21': ('GCB', 'lotes[L6B].curso'), 'GCB-EXTRA-22': ('GCB', 'itens[6B-06].justificativa')}
# 1.4: linhas da GCE cujo id citado não está no intervalo do antes (rótulo deslocado): linha -> linha em cujo `antes` está o casamento citado
EXCECAO_INTERVALO = {'GCE-0105': 'GCE-0110', 'GCE-0206': 'GCE-0207', 'GCE-0207': 'GCE-0213', 'GCE-0213': 'GCE-0238'}
# 1.5: perda de literal de base legal admitida (linha -> literais)
EXCECAO_BASE_LEGAL = {'GCE-0211': ['inciso']}

GERADO_EM = '2026-10-18'
FINAL = True
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
    _dec = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'DECISOES.md'), encoding='utf-8').read()
    for _id in (ATO_L2R16, 'D-T108-GCE-TABELA', 'D-T108-GCB-TABELA'):
        if _id and ('| %s |' % _id) not in _dec:
            p.append('DECISOES.md sem a linha "| %s |"' % _id)
    _ct = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'regras', 'pacote_contrato.md'), encoding='utf-8').read().split(chr(10))[0]
    if 'v1.2.8' not in _ct:
        p.append('contrato sem "v1.2.8" na linha 1')
    if not VERSAO:
        p.append('E5: VERSAO não decidida')
    return p

if ENSAIO:      # exceções do depois das linhas sintéticas de ensaio (gravadas por ensaio/gera_tabelas_ensaio.py); na geração final, só a lista fechada da reconciliação
    import json as _json
    _pe = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ensaio', 'excecoes_ensaio.json')
    if os.path.exists(_pe):
        with open(_pe, encoding='utf-8') as _f:
            EXCECOES_DEPOIS = _json.load(_f)
