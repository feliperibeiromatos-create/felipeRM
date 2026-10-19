# -*- coding: utf-8 -*-
"""T-115 (gerador_v1_12) — chaves da ocorrência (D1 da GBQ, saida/pacote/T115_D1_v1_12_2026-10-18.md, seções 1, 3.1 e 3.3).
Único lugar em que o número da versão do pacote é escrito (conferência C-16). Lido por todos os passos do pipeline.
ENSAIO (FINAL = False): roda tudo e grava out/; nada é promovido. FINAL (FINAL = True): só com os 23 SHA-256 LF conferidos e as constantes de aceite (seção 3.3) batendo.
As constantes de aceite abaixo são transcritas das decisões (DECISOES.md) e da D1, não lidas dos arquivos."""
import collections

VERSAO = '1.12'
NOME = 'Câmara 2026 — pacote F4 (v%s)' % VERSAO
NOME_E = 'Câmara 2026 — pacote do estudante (v%s-E)' % VERSAO
TAG = 'v' + VERSAO.replace('.', '_')
GERADO_EM = '2026-10-18'
FINAL = True
ENSAIO = not FINAL

# BASE: pacote v1.11 canônico (D-PACOTE-V111), lido do blob do commit fe17830
BASE = ('fe17830', 'saida/pacote/pacote.json', '1b5657c726b5852885fe0e69e7835d6ec331e6d43dd19191cf451ff4ac069517')
BASE_E = ('fe17830', 'saida/pacote/pacote_estudante.json', '8533b0c085594a42dd066b3e7a6161f0ea94f4f60bb2ad2cfbafc969369f6bd7')
BASE_ESTUDANTE_DIR = 'saida/estudante'
BASE_NOME = 'Câmara 2026 — pacote F4 (v1.11)'
BASE_NOME_E = 'Câmara 2026 — pacote do estudante (v1.11-E)'
BASE_ITENS = 560
CONTRATO_BASE = ('fe17830', 'regras/pacote_contrato.md')
CONTRATO_SHA_LF = '7a4c1f636dd1354afbcf91ad421eadaf4444fe58a7b17efd22577dfeca233c4e'      # v1.2.9 (contrato_v1_2_9_2026-10-18.md)
GERADOR_ANTERIOR = 'gerador_v1_11'
MANIFESTO_ANTERIOR_SHA = 'd0d827c8'      # prefixo do SHA-256 do MANIFESTO.md do gerador anterior no fe17830 (D1, 3.1, item 1)

# 23 insumos (D1, seção 1): (n, caminho, SHA-256 do conteúdo LF, ato). Lidos com CRLF -> LF.
AT4, AP1, AP2 = 'D-T98-ONDA4-ACEITE', 'D-V112-BAEF-P1-ACEITE', 'D-V112-BAEF-P2-ACEITE'
INSUMOS = [
    (1, 'saida/gce/L3_reforco_onda4_A_v3.md', '5be2941157f7db21e9d2f3b09007fbfd6ccafbc31608d37e3434e3fa8913c2b0', AT4),
    (2, 'saida/gce/L3_reforco_onda4_B_v2.md', '09d9d52144238358eb7fbf8ffcc35b71fa99b0b30e97fbb24410d2b563f7f398', AT4),
    (3, 'saida/gce/L3_reforco_onda4_C_v3.md', 'd9faf9a70e698432afd4767a785bb526d97b2adadd60685ce468c1eba6241344', AT4),
    (4, 'saida/gce/T98_reconciliacao_2026-10-18.md', 'f5a1b1eafc0632fc1770efa3dd7a6421cb076defe174c91b510ddba7041e4f94', AT4),
    (5, 'saida/gcb/T113_onda1_P1_v2.md', '0b863e476f14d01ef801635b0e67998b24924213723d96c4a791e26c7dd6da4f', AP1),
    (6, 'saida/gcb/T110_pegadinhas_P1_v2.md', 'd3bbfd5b786ce1e1eed8f306009527f022878f421175234e7305dc905752a756', AP1),
    (7, 'saida/gcb/T110_registro_P1_v2.csv', 'c5400b141984cea345f92d13e2acb26c4cfa4cf22d403e948014ccb117ddc222', AP1),
    (8, 'saida/gcb/T111_resumos_P1_parte1_v2.md', '46446cbb4ad8b4b22f9b604f818025166c7453f905949c7a659c02a3bb199be3', AP1),
    (9, 'saida/gcb/T111_resumos_P1_parte2_v2.md', '187ac80c4b63dcc976b2d8034037811264a1029b4ed0bce8f640615395f8ebd1', AP1),
    (10, 'saida/gcb/T112_piloto_P1-8.2_v2.md', '7c7d3d4b98098d6703224984f11e2679104508db7cab40c2327654d0fb88a009', AP1),
    (11, 'saida/gce/T110_pares_P2_v2.md', 'e2c6961a0b35838fdfff138adc0e36068e42b0f71b87e0643236efdd20a282c7', AP2),
    (12, 'saida/gce/T111_resumos_P2_A1_v2_GCE.md', '0ad69e62ad8c341316a30748a53c32760c32fe2c0a8924b83dfbe855034081a3', AP2),
    (13, 'saida/gce/T111_resumos_P2_A2_v2.md', '06b1c74a85782c6fd5d1184465282e240bf4aa40d5378c40ae23e2d5007ad923', AP2),
    (14, 'saida/gce/T111_resumos_P2_A3_v2.md', '34f397cd331c6e92c3fe27464198e0c89d6b9b9085455a22d6b31736b28458a6', AP2),
    (15, 'saida/gce/T111_resumos_P2_A4_v2.md', 'd63def08b9ac46a90bb1b3089ecf1bb87c7484214fdaa21fb5cb99e511640d6f', AP2),
    (16, 'saida/gce/T112_piloto_visual_P2_v2.md', 'bcd7d5f2e1536c7198bbdbbd8f84415e6aff2647185e7e8a2dae27f0364e6cb4', AP2),
    (17, 'saida/gce/T113_onda1_A_v2.md', '8c15789308f7a7f5d295ee1a740b0707701dfb723f7fb3ecee2ce201760df081', AP2),
    (18, 'saida/gce/T113_onda1_B_v2.md', '74602cafd57d6bf10722068ecd30b54f771a46cc2c2e050e41a270b98016f01b', AP2),
    (19, 'saida/gce/T113_onda1_C_v2.md', 'a332fb3f2b2344a065642d2d890241c1d9744de1b9cd8cba5f537bd2b8a4896d', AP2),
    (20, 'saida/gce/T113_onda1_D_v2.md', '9aae8f8a05a693f0b209147b6fe5b88e336a015f387d4bcaa6c2a550140b531d', AP2),
    (21, 'saida/banco/estilo_onda_F1.md', '6087b1e15252adf00ae10899691396a6d1e2ed7cbfee2cbe30ba2c0e7e051d3c', AP2),
    (22, 'saida/gcb/V15_BAEF_reconciliacao_GCB_2026-10-18.md', 'ad43811dae36ae4f0e252526d16901f327f33e61d0487e9984f626cd75a71a0d', AP1),
    (23, 'saida/gce/V15_BAEF_reconciliacao_GCE_2026-10-18.md', '4ef329f80e60e9e7373748fd1847bef69643b316182692e16a84dc948d745765', AP2),
]
SHA = {c: h for n, c, h, a in INSUMOS}
T11_VOLATEIS = 'saida/pacote/T115_volateis_T11.md'      # saída do script da D1 (seção 9); lista dos 32 VOLÁTEIS novos (C-V)

# Arquivos de itens, na ordem dos atos (D1, 3.3): (grupo, ato, caminho, formato, vagos/diferidos presentes no arquivo)
GRUPOS = collections.OrderedDict([
    ('ONDA4', dict(ato=AT4, lote='L3', arquivos=['saida/gce/L3_reforco_onda4_A_v3.md', 'saida/gce/L3_reforco_onda4_B_v2.md', 'saida/gce/L3_reforco_onda4_C_v3.md'])),
    ('F1P1', dict(ato=AP1, lote='L4', arquivos=['saida/gcb/T113_onda1_P1_v2.md'])),
    ('F1P2', dict(ato=AP2, lote=None, arquivos=['saida/gce/T113_onda1_A_v2.md', 'saida/gce/T113_onda1_B_v2.md', 'saida/gce/T113_onda1_C_v2.md', 'saida/gce/T113_onda1_D_v2.md'])),
])
VAGOS = ['L1-R140', 'L2-R136', 'L2-R137', 'L2-R140', 'L3-R101']
DIFERIDOS = ['L3-R103', 'L3-R104']
CARGO = {'L1': 'Lote 1', 'L2': 'Lote 2', 'L3': 'Lote 3'}

# Constantes de aceite (D1, 3.3), transcritas das decisões
ACEITE = collections.OrderedDict()
ACEITE['ONDA4'] = dict(n=84, C=42, E=42, ts=61, vol=['L3-R12', 'L3-R13', 'L3-R14', 'L3-R16', 'L3-R27', 'L3-R56', 'L3-R59', 'L3-R65', 'L3-R91', 'L3-R94'],
                       parcial=['L3-R12', 'L3-R13', 'L3-R14', 'L3-R53', 'L3-R64', 'L3-R95'],
                       folha={'P2-3.1': 14, 'P2-3.2': 14, 'P2-3.3': 14, 'P2-3.4': 14, 'P2-4.2': 14, 'P2-4.3': 14},
                       partes=[28, 28, 28], faixa=('L3-R12', 'L3-R95'))
ACEITE['F1P1'] = dict(n=7, C=4, E=3, ts=3, vol=[], parcial=[], folha={'P1-5.2': 7})
ACEITE['F1P2'] = dict(n=98, C=49, E=49, ts=49,
                      vol=['L1-R139', 'L1-R159', 'L1-R160', 'L1-R161', 'L1-R168', 'L1-R170', 'L1-R171', 'L1-R177', 'L1-R178', 'L1-R180', 'L1-R183', 'L1-R184', 'L1-R185', 'L1-R187',
                           'L1-R191', 'L1-R194', 'L1-R200', 'L1-R201', 'L2-R135', 'L2-R141', 'L2-R142', 'L3-R100'],
                      parcial=[],
                      folha={'P2-1.1': 9, 'P2-1.2': 10, 'P2-1.3': 10, 'P2-1.4': 10, 'P2-1.5': 10, 'P2-1.6': 10, 'P2-1.7': 10, 'P2-1.8': 10, 'P2-2.1': 7, 'P2-2.2': 1, 'P2-2.8': 1,
                             'P2-3.1': 6, 'P2-4.1': 4},
                      partes=[(29, 16, 13), (30, 13, 17), (27, 14, 13), (12, 6, 6)])
TOTAIS = dict(itens=749, novos=189, C=380, E=369, parcial=94, volatil=86, volatil_novos=32, pegadinhas=335, pegadinhas_novas=73, topicos=40, pilotos=3, delecoes=53, itens_limpeza=52, registro=447)
FOLHAS_V112 = {      # D1 seção 8: folha -> (v1.11, v1.12, C, E, diretos, parciais, volateis)
    'P1-5.2': (23, 30, 16, 14, 29, 1, 0), 'P2-1.1': (20, 29, 13, 16, 29, 0, 1), 'P2-1.2': (20, 30, 16, 14, 30, 0, 0), 'P2-1.3': (20, 30, 15, 15, 30, 0, 6),
    'P2-1.4': (20, 30, 15, 15, 30, 0, 6), 'P2-1.5': (20, 30, 16, 14, 30, 0, 6), 'P2-1.6': (20, 30, 13, 17, 30, 0, 6), 'P2-1.7': (20, 30, 14, 16, 30, 0, 6),
    'P2-1.8': (20, 30, 16, 14, 30, 0, 2), 'P2-2.1': (20, 27, 15, 12, 17, 10, 5), 'P2-2.2': (20, 21, 10, 11, 14, 7, 1), 'P2-2.8': (19, 20, 9, 11, 19, 1, 4),
    'P2-3.1': (7, 27, 13, 14, 22, 5, 5), 'P2-3.2': (6, 20, 10, 10, 20, 0, 1), 'P2-3.3': (6, 20, 10, 10, 18, 2, 0), 'P2-3.4': (6, 20, 11, 9, 19, 1, 3),
    'P2-4.1': (26, 30, 18, 12, 9, 21, 1), 'P2-4.2': (6, 20, 11, 9, 20, 0, 0), 'P2-4.3': (6, 20, 9, 11, 19, 1, 2)}

# Erratas (D1, 3.4): (id do registro, id do item, antes, depois, ocorrências esperadas)
ERRATAS = [
    ('T115-E-01', 'L1-R137',
     'Ao enviar as gravações de uma comissão ao Google Cloud Speech-to-Text, a equipe descreve na configuração da requisição a codificação do áudio, o idioma falado e o modelo de reconhecimento realmente adequados a essas gravações. De acordo com a documentação do Google Cloud, descrever com exatidão os dados de áudio enviados contribui para a obtenção da transcrição mais precisa e da cobrança correta da requisição.',
     'De acordo com a documentação do Google Cloud Speech-to-Text, descrever na configuração da requisição a codificação correta do áudio e usar o idioma e o modelo de reconhecimento corretos contribui para a transcrição mais precisa e para a cobrança correta da requisição.', 1),
    ('T115-E-02', 'L1-R167',
     'Segundo a nota de transparência do Azure Speech, a qualidade da diarização é medida pela taxa de erro de palavras (WER), de modo que o serviço não adota métrica específica para a atribuição das palavras aos falantes.',
     'Segundo a nota de transparência do Azure Speech, a qualidade da diarização é medida pela taxa de erro de palavras (WER).', 1),
    ('T115-E-03', 'L3-R108',
     'Um órgão público utiliza sistema de inteligência artificial para classificar as falas de audiências públicas. Nessa situação, segundo a Lei Geral de Proteção de Dados Pessoais, a impossibilidade de realização do tratamento para fins discriminatórios ilícitos ou abusivos corresponde ao princípio da prevenção.',
     'Segundo a Lei Geral de Proteção de Dados Pessoais, o princípio da prevenção corresponde à impossibilidade de realização do tratamento para fins discriminatórios ilícitos ou abusivos.', 1),
]
URL_ERRATA = [('T115-U-01', 'L3-R105', 2), ('T115-U-02', 'L3-R108', 1)]
URL_ANTES = 'https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm'
URL_DEPOIS = 'https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm'
URL_ARQUIVO = 'saida/gce/T113_onda1_D_v2.md'
ESTILO_ARQUIVO = 'saida/banco/estilo_onda_F1.md'
FORMATO_ADENDO = {'L1-R137': 'D', 'L1-R167': 'TSj', 'L3-R108': 'TSj'}      # D1 3.4: L1-R137 D (era SH); L1-R167 TSj; L3-R108 TSj (era SH)

# Limpeza da ORDEM C (D1, 3.5): (regra, padrão, categoria, itens esperados). Ordem de aplicação: L-2, L-1, L-5, L-3, L-4.
LIMPEZA = [
    ('L-2', r'^VOLÁTIL \((?:baixo|médio|alto)\)\. REVERIFICAR\. ', 'C10', ['L3-R56', 'L3-R59', 'L3-R65']),
    ('L-1', r'^REVERIFICAR\. ', 'C10', ['L3-R%d' % k for k in list(range(40, 56)) + [57, 58] + list(range(60, 65)) + [66, 67]]),
    ('L-5', r'Aderência PARCIAL \(R1: [^)]*\)\. ', 'C07', ['L3-R53']),
    ('L-3', r' VOLÁTIL (?:baixo|médio|alto): [^.]*\.$', 'C10', ['L1-R194', 'L1-R200', 'L1-R201', 'L2-R135', 'L2-R141', 'L2-R142']),
    ('L-4', r' \(C espelho(?:: [^)]*)?\)', 'C02', ['L3-R13', 'L3-R24', 'L3-R30', 'L3-R39', 'L3-R97', 'L1-R162', 'L1-R165', 'L1-R169', 'L1-R171', 'L1-R173', 'L1-R175', 'L1-R179',
                                                   'L1-R180', 'L1-R181', 'L1-R184', 'L1-R185', 'L1-R188', 'L1-R191']),
]
# MANTER (D1, 3.5): ocorrências do inventário que continuam (FP de conteúdo). (caminho, categoria, casamento) -> quantidade
MANTER = collections.OrderedDict([
    (('itens[L3-R54].justificativa', 'C01', 'lote'), 1), (('itens[L3-R91].justificativa', 'C01', 'lote'), 1), (('itens[L1-R207].justificativa', 'C01', 'lote'), 1),
    (('itens[L3-R64].justificativa', 'C05', 'F1'), 1), (('itens[L1-R176].justificativa', 'C05', 'F1'), 1), (('itens[L1-R196].justificativa', 'C09', 'v2'), 1),
    (('topicos[P2-1.7].resumo', 'C01', 'lote'), 3), (('topicos[P2-1.8].resumo', 'C01', 'lote'), 2),
])
MANTER_FP_ESPERADO = [('topicos[P1-1].resumo', 'C05', 'F4')]      # tecla F4 do Excel (FP-R1 já existente)
ENUNCIADOS_FP = [('itens[L3-R54].enunciado', 'C01', 'lote'), ('itens[L3-R91].enunciado', 'C01', 'lote'), ('itens[L1-R168].enunciado', 'C01', 'lote'), ('itens[L1-R210].enunciado', 'C01', 'lote'),
                 ('itens[L3-R64].enunciado', 'C05', 'F1'), ('itens[L1-R196].enunciado', 'C09', 'v2'), ('itens[L1-R197].enunciado', 'C09', 'v2'), ('itens[L1-R199].enunciado', 'C09', 'v2')]

# Nomes de lote e do SIM-0 (D1, 3.8)
NOMES_LOTE = collections.OrderedDict([
    ('L1', ('Lote 1 — RF-ASR (reconhecimento de fala e transcrição, P2 1.1–1.8)', 'Lote 1 — Reconhecimento de Fala e Transcrição de Áudio (P2 1.1–1.8)')),
    ('L1C', ('Lote 1-C — RF-ASR, complemento (P2 1.1–1.5)', 'Lote 1-C — Reconhecimento de Fala e Transcrição de Áudio, complemento (P2 1.1–1.5)')),
    ('L2', ('Lote 2 — RF-DEGRAVACAO (degravação e pós-processamento, P2 2.1–2.8)', 'Lote 2 — Degravação e Pós-processamento de Transcrições (P2 2.1–2.8)')),
    ('L3', ('Lote 3 — RF-IA-PARLAMENTAR + RF-PROTECAO (P2 3.1–4.3)', 'Lote 3 — IA Aplicada no Contexto Parlamentar; Proteção e segurança da informação (P2 3.1–4.3)')),
    ('L4', ('Lote 4 — TID-IA (P1 5.1–5.3 e 6)', 'Lote 4 — Conceitos básicos de inteligência artificial; Ética e responsabilidade digital no serviço público (P1 5.1–5.3 e 6)')),
    ('L4C', ('Lote 4-C — TID-IA, complemento (P1 5.1)', 'Lote 4-C — Conceitos básicos de inteligência artificial, complemento (P1 5.1)')),
    ('L5', ('Lote 5 — TID-DADOS-VIZ (P1 7.1 e 8.1–8.4)', 'Lote 5 — Dados; Visualização de dados (P1 7.1 e 8.1–8.4)')),
    ('L5C', ('Lote 5-C — TID-DADOS-VIZ, complemento (P1 8.2 e 8.4)', 'Lote 5-C — Visualização de dados, complemento (P1 8.2 e 8.4)')),
    ('L6A', ('Lote 6a — TI-FERRAMENTAS (P1 itens 1 e 3: MSOffice 365 e comunicação/colaboração)', 'Lote 6a — MSOffice 365; Ferramentas de comunicação e colaboração (P1 itens 1 e 3)')),
    ('L6B', ('Lote 6b — TI-REDES-SEGURANCA (P1 itens 2 e 4: redes e segurança)', 'Lote 6b — Redes de computadores; Conceitos gerais de segurança e governança digital (P1 itens 2 e 4)')),
])
SIM0_NOME = ('Simulado 0 — diagnóstico (v0.2)', 'Simulado 0 — diagnóstico')
LEGENDA_FORA = ['L4', 'L4C', 'L5', 'L5C', 'L6A', 'L6B']
RAIZ_PEGADINHAS = {'L1': (19, 28), 'L1C': (4, 4), 'L2': (43, 49), 'L3': (42, 51), 'L4': (32, 43), 'L4C': (0, 0), 'L5': (48, 61), 'L5C': (0, 0), 'L6A': (35, 47), 'L6B': (39, 52)}
PEG_P1 = {'L4': 11, 'L5': 13, 'L6A': 12, 'L6B': 13}
PEG_P2 = {'L1': 9, 'L2': 6, 'L3': 9}
RASTRO_P1 = (72, 46, 26)       # linhas do CSV, CONVERTIDO, DESCARTADO
RASTRO_P2 = (67, 24, 43)       # linhas da tabela (a), CONVERTIDO, DESCARTADO
TOPICOS_P1, TOPICOS_P2, PILOTOS = 17, 23, ['P1-8.2', 'P2-1.4', 'P2-2.5']
ATOS_NUCLEO = collections.OrderedDict([('D-T98-ONDA4-ACEITE', r'^L3-R(1[2-9]|[2-8]\d|9[0-5])$'), ('D-V112-BAEF-P1-ACEITE', r'^L4-R0[1-7]$')])      # os ids de P2 da onda 1 vêm do conjunto lido
ATO_F1_P2 = 'D-V112-BAEF-P2-ACEITE'
DECISOES_EXIGIDAS = ['D-T98-ONDA4-ACEITE', 'D-V112-BAEF-P1-ACEITE', 'D-V112-BAEF-P2-ACEITE']
CONTRATO_VERSAO = 'v1.2.9'
D1_ARQUIVO = 'saida/pacote/T115_D1_v1_12_2026-10-18.md'

# Verificação residual das listas de deleção herdadas (estudante_json_v112.py; C-8): lista fechada herdada da v1.11 (nada novo na v1.12)
EXCECOES_RESIDUAL = {'carimbo datado de verificação/leitura (ligado a F-ref)': 4, 'carimbo "Verificado em 8/10/2026" (L5)': 4, 'F (prosa: referência a fonte)': 1}
EXCECOES_RESIDUAL_CAMPOS = {'carimbo datado de verificação/leitura (ligado a F-ref)': ['lotes[L4].curso', 'lotes[L6A].curso'],
                            'carimbo "Verificado em 8/10/2026" (L5)': ['itens[A5-14].justificativa', 'itens[A5-15].justificativa', 'itens[A5-16].justificativa', 'itens[A5-17].justificativa'],
                            'F (prosa: referência a fonte)': ['lotes[L6A].curso']}
