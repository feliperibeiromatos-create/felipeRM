# formatar_D4.py — T-77 (ordem DA 20/10/2026) — 2026-10-20 — gerado por gcb-cpp
# Reformata o canônico saida/gcb/D4_v2_1.md para o formato da plataforma (FORMATO_PLATAFORMA_DA.md).
# Só reformatação: nenhum conteúdo novo. Toda deleção e troca de palavra é registrada (LOG) e vai ao registro.
# Determinístico. Os tópicos são escritos à mão em D4_topicos_fonte.json e incorporados aqui.
# Uso:  python3 -I saida/gcb/DA_plataforma/scripts/formatar_D4.py              -> grava D4_plataforma.json
#       python3 -I saida/gcb/DA_plataforma/scripts/formatar_D4.py --registro   -> regrava o JSON, roda o validador e a
#                                                                                conferência de fidelidade e grava D4_registro_formato.md
import hashlib, json, pathlib, re, subprocess, sys
from collections import Counter, OrderedDict

RAIZ = pathlib.Path(__file__).resolve().parents[4]
DA = RAIZ / 'saida/gcb/DA_plataforma'
CANON = RAIZ / 'saida/gcb/D4_v2_1.md'
MAPA = RAIZ / 'saida/gcb/D4_anexo_N_mapa_normativo.md'
SHA_CANON = 'c1a7a93598e9fd37b2009b9feaca3afd3898fa05f6f66e6de26dd40c2839e5d9'
URL_CANON = 'saida/gcb/D4_v2_1.md'
SAIDA_JSON = DA / 'D4_plataforma.json'
TOPICOS = DA / 'D4_topicos_fonte.json'
REGISTRO = DA / 'D4_registro_formato.md'
VALIDADOR = DA / 'scripts/validar_da.py'
CONFERE = DA / 'scripts/conferir_fidelidade_D4.py'

NOME = 'Direito Administrativo — Gestão pública e governança (itens 8 e 9 do edital)'
DATA_MAPA = '2026-10-20'   # consulta registrada no mapa para os dispositivos usados (20/10/2026)

def sha(b): return hashlib.sha256(b).hexdigest()

def ler_canon():
    raw = CANON.read_bytes()
    if sha(raw) != SHA_CANON:
        print('PARAR: SHA-256 de saida/gcb/D4_v2_1.md diverge:', sha(raw), '!=', SHA_CANON); sys.exit(2)
    return raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n').split('\n')

EDITAL = {e['id']: e['texto'] for e in json.loads((DA / 'edital_DA.json').read_text(encoding='utf-8'))}

def achar(L, prefixo, ini=0):
    for i in range(ini, len(L)):
        if L[i].startswith(prefixo): return i
    raise SystemExit('PARAR: seção não encontrada: ' + prefixo)

# ---------------------------------------------------------------- registro de edições
LOG = []   # {ctx, tipo, antes, depois, motivo}
def log(ctx, tipo, antes, depois, motivo):
    LOG.append(dict(ctx=ctx, tipo=tipo, antes=antes, depois=depois, motivo=motivo))

def edita(ctx, txt, antigo, novo, tipo, motivo):
    assert txt.count(antigo) == 1, (ctx, antigo[:80], txt.count(antigo))
    log(ctx, tipo, antigo.strip(), novo.strip(), motivo)
    return txt.replace(antigo, novo)

D_MARCA = 'deleção de marca'
D_FRASE = 'deleção de frase inteira'
D_ORACAO = 'deleção de oração de processo'
TROCA = 'troca mínima (op. 6)'
IDENT = 'código de referencial trocado pela identificação da publicação'
M_SEMFONTE = '"[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6)'
M_PROC = 'fala de produção (cobertura de itens, cruzamento com item do banco, regra de redação, pedido de exceção); não é conteúdo para a candidata (seção 6)'
M_COD = 'remissão a código interno de bloco (seção 6)'
M_RID = 'o bloco já identifica a publicação; o código interno (R-id do Anexo N) sai e o termo mínimo mantém a frase (seção 6)'
M_RID2 = 'o bloco só tinha o código interno (R-id do Anexo N); a remissão sai (seção 6)'
E_ACH1 = 'errata de forma (QA final 20/10/2026, achado 1): '
E_SUB = E_ACH1 + '"folha" é termo de produção (seção 6); a remissão serve ao estudo e passa a "subitem", o número é o do `##` do curso'
E_ACH7 = 'errata de forma (QA final 20/10/2026, achado 7): '
M_LOTE = '"lote" é referência de produção (seção 6); trocado por "curso", que o próprio texto já usa'

# ---------------------------------------------------------------- referencial oficial (Anexo N, seção 5)
# família -> como o texto se refere à publicação (art = com artigo, para sujeito/objeto; base = sem artigo, para listas e parênteses)
FAM = {
 'bresser': dict(art='o artigo de Bresser-Pereira (ENAP, 2022)', base='Bresser-Pereira, ENAP, 2022',
                 fonte='ENAP, Revista do Serviço Público 73 (Especial 85 Anos), artigo de Bresser-Pereira, 2022'),
 'guia':    dict(art='o Guia da Política de Governança Pública (Casa Civil, 2018)', base='Guia da Política de Governança Pública, Casa Civil, 2018',
                 fonte='Casa Civil da Presidência da República, Guia da Política de Governança Pública, 2018'),
 'pdrae':   dict(art='a análise de Cavalcante (Ipea, 2020)', base='Cavalcante, Ipea, 2020',
                 fonte='Ipea, Reformas do Estado no Brasil, v. 1, capítulo de Cavalcante, 2020'),
 'boucka':  dict(art='o artigo de Bouckaert (ENAP, 2024)', base='Bouckaert, ENAP, 2024',
                 fonte='ENAP, Revista do Serviço Público 75(1), artigo de Bouckaert, 2024'),
 'cav18':   dict(art='o texto de Cavalcante (Ipea, 2018)', base='Cavalcante, Ipea, 2018',
                 fonte='Ipea, Boletim de Análise Político-Institucional n. 19, texto de Cavalcante, 2018'),
 'lui':     dict(art='o capítulo de Lui et al. (Ipea, 2023)', base='Lui et al., Ipea, 2023',
                 fonte='Ipea, Diálogos para uma PNDU, v. 1, capítulo de Lui et al., 2023'),
 'tcu':     dict(art='o Referencial Básico de Governança Organizacional (TCU, 2020)', base='Referencial Básico de Governança Organizacional, TCU, 2020',
                 fonte='TCU, Referencial Básico de Governança Organizacional, 3. ed., 2020'),
 'cgu':     dict(art='o documento didático da CGU', base='documento didático da CGU',
                 fonte='CGU, documento didático Cadeia de valor da CGU, sem data'),
 'martins': dict(art='o texto de Martins (Ipea, 2018)', base='Martins, Ipea, 2018',
                 fonte='Ipea, Boletim de Análise Político-Institucional n. 19, texto de Martins, 2018'),
 'gpex':    dict(art='o guia prático de análise ex post (Casa Civil, 2018)', base='guia prático de análise ex post, Casa Civil, 2018',
                 fonte='Casa Civil da Presidência da República, Avaliação de Políticas Públicas: guia prático de análise ex post, v. 2, 2018'),
}
RFAM = {1: 'bresser', 2: 'bresser', 3: 'bresser', 4: 'guia', 5: 'pdrae', 6: 'boucka', 7: 'boucka', 8: 'cav18', 9: 'cav18', 10: 'guia',
        11: 'lui', 12: 'cav18', 13: 'guia', 14: 'tcu', 15: 'guia', 16: 'cgu', 17: 'martins', 18: 'gpex', 19: 'tcu', 20: 'tcu',
        21: 'tcu', 22: 'tcu', 23: 'guia', 24: 'tcu', 25: 'tcu', 26: 'tcu', 27: 'tcu', 28: 'tcu', 29: 'martins', 30: 'gpex', 31: 'gpex'}
RPAG = {1: '58', 2: '58', 3: '59', 4: '29', 5: '40', 6: '17', 7: '25', 8: '21', 9: '19', 10: '41', 11: '236', 12: '20', 13: '51', 14: '90',
        15: '54', 16: '6 do arquivo PDF (sem numeração impressa)', 17: '58', 18: '13', 19: '15', 20: '16', 21: '111', 22: '21', 23: '15', 24: '37',
        25: '54', 26: '69', 27: '88', 28: '15-16', 29: '60', 30: '33', 31: '33'}

def confere_referencial_com_mapa():
    """Cada R-id: a página da tabela da seção 5 do mapa tem de ser a que este script usa (p. N); conferência na carga."""
    mapa = MAPA.read_text(encoding='utf-8')
    achados = {}
    for l in mapa.split('\n'):
        m = re.match(r'^\| R(\d+) \| ', l)
        if m:
            cel = [c.strip() for c in l.strip().strip('|').split(' | ')]
            achados[int(m.group(1))] = cel[3]
    assert sorted(achados) == list(range(1, 32)), sorted(achados)
    for n, pub in achados.items():
        pg = RPAG[n]
        if n == 16: assert 'p. 6 do PDF' in pub, pub
        else: assert pub.rstrip().endswith('p. ' + pg), (n, pub, pg)
    chave = {'bresser': 'Bresser-Pereira', 'guia': 'Guia da Política de Governança Pública', 'pdrae': 'Reformas do Estado', 'boucka': 'Bouckaert',
             'cav18': 'Cavalcante', 'lui': 'Lui', 'tcu': 'Referencial Básico de Governança Organizacional', 'cgu': 'Cadeia de valor da CGU', 'martins': 'Martins',
             'gpex': 'guia prático de análise ex post'}
    pub_fam = {'bresser': 'ENAP', 'guia': 'Casa Civil', 'pdrae': 'Ipea', 'boucka': 'ENAP', 'cav18': 'Ipea', 'lui': 'Ipea', 'tcu': 'TCU',
               'cgu': 'CGU', 'martins': 'Ipea', 'gpex': 'Casa Civil'}
    for n, pub in achados.items():
        f = RFAM[n]
        assert pub_fam[f] in pub, (n, f, pub)
        assert chave[f].lower().split()[0] in pub.lower() or f in ('tcu', 'guia', 'gpex', 'cgu'), (n, f, pub)
    return achados
PUBLICACAO_MAPA = confere_referencial_com_mapa()

def juntar(xs, sep_ult=' e '):
    xs = list(xs)
    if len(xs) <= 1: return ''.join(xs)
    if len(xs) == 2: return xs[0] + sep_ult + xs[1]
    return ', '.join(xs[:-1]) + sep_ult + xs[-1]

CONTR = {('de', 'o'): 'do', ('de', 'a'): 'da', ('em', 'o'): 'no', ('em', 'a'): 'na', ('a', 'o'): 'ao', ('a', 'a'): 'à', ('por', 'o'): 'pelo', ('por', 'a'): 'pela'}
RUN = re.compile(r'(?<![\w$])R(\d{1,2})(?:(?:, | e |; )R(\d{1,2}))*(?![\w$])')

def paginas_txt(pgs):
    pgs = [p for i, p in enumerate(pgs) if p not in pgs[:i]]
    if len(pgs) == 1: return 'p. ' + pgs[0]
    return 'pp. ' + juntar(pgs)

def subst_ids(ctx, txt, modo='auto'):
    """Troca cada sequência de R-ids pela identificação da publicação. modo 'base': lista de 'Base' (com página); 'auto': par (entre parênteses) ou art (com artigo)."""
    out, pos = [], 0
    for m in RUN.finditer(txt):
        ids = [int(x) for x in re.findall(r'R(\d{1,2})', m.group(0))]
        prev, nxt = txt[:m.start()], txt[m.end():]
        fams = []
        for n in ids:
            if RFAM[n] not in fams: fams.append(RFAM[n])
        if modo == 'base':
            partes = []
            for f in fams:
                pgs = [RPAG[n] for n in ids if RFAM[n] == f]
                partes.append(FAM[f]['base'] + ', ' + paginas_txt(pgs))
            rep = '; '.join(partes); pref_cut = 0
        elif prev.endswith('(') and nxt.startswith(')'):
            rep = '; '.join(FAM[f]['base'] for f in fams); pref_cut = 0
        else:
            arts = [FAM[f]['art'] for f in fams]
            mp = re.search(r'(?<![\w])(de|em|a|por)\s+$', prev)
            pref_cut = 0
            if mp:
                arts = [CONTR[(mp.group(1), a[0])] + a[1:] for a in arts]
                pref_cut = len(prev) - mp.start()
            elif re.search(r'(^|[.!?]\s+)$', prev):
                arts[0] = arts[0][0].upper() + arts[0][1:]
            rep = juntar(arts)
        out.append(txt[pos:m.start() - pref_cut]); out.append(rep); pos = m.end()
        antes = (prev[len(prev) - pref_cut:] if pref_cut else '') + m.group(0)
        log(ctx, TROCA, antes, rep, IDENT + ' (órgão, autor, ano e página tirados da seção 5 do Anexo N, como manda a ordem)')
    out.append(txt[pos:])
    return ''.join(out)

# ---------------------------------------------------------------- edições explícitas do curso, por bloco e campo
# 'd' definição; 'e' exemplo; 'g' pegadinha (antes de "Base"); 'b' lista "Base"
def DEL(old, motivo, tipo=D_FRASE): return (old, '', tipo, motivo)
def RID(old, new, motivo=M_RID): return (old, new, TROCA, motivo)
def LOTE(old, new): return (old, new, TROCA, M_LOTE)

EXPL = {
 ('C8.0-01', 'd'): [
  DEL(' Datas e marcos históricos do modelo (por exemplo, o DASP de 1936 e o Decreto-Lei 200/1967): [SEM FONTE — não afirmar].', M_SEMFONTE),
  RID('R1 descreve o modelo', 'o trecho descreve o modelo'),
 ],
 ('C8.0-02', 'd'): [
  RID('R1 diz que a administração burocrática', 'O artigo de Bresser-Pereira (ENAP, 2022) diz que a administração burocrática', 'o bloco não identificava a publicação neste ponto; o código sai e a identificação (autor, órgão, ano) vem da seção 5 do Anexo N, como manda a ordem'),
  RID('e R2 completa:', 'e o mesmo artigo completa:'),
  RID(', em R4, associa', ' associa', M_RID),
 ],
 ('C8.0-03', 'd'): [RID('R2 aponta o limite', 'o trecho aponta o limite')],
 ('C8.0-04', 'd'): [
  RID('R3 situa o início', 'o trecho situa o início'),
  RID('Governança Pública (R4) associa', 'Governança Pública (Casa Civil, 2018) associa', 'o bloco só tinha o código (R-id); ele é trocado pelo órgão e ano da publicação (seção 5 do Anexo N)'),
  LOTE('No texto próprio do lote', 'No texto próprio do curso'),
 ],
 ('C8.0-05', 'd'): [
  RID('R8 resume:', 'o trecho resume:'),
  RID('A segunda frase de R8 (redes) é tratada em C8.1-02.', 'A segunda frase do trecho (redes) é tratada em 8.1.', 'código de bloco (C8.1-02) trocado pelo número do tópico (8.1) e R-id trocado por "do texto", pois a frase anterior já identifica a publicação (seção 6)'),
 ],
 ('C8.0-06', 'd'): [
  DEL('O texto do PDRAE (1995) não foi aberto: [SEM FONTE — não afirmar] o que ele diz literalmente. ', M_SEMFONTE),
  RID('(R5, Cavalcante)', '(Cavalcante)'),
  RID('R5 é paráfrase do Ipea, e nenhum item do lote versa sobre o conteúdo do PDRAE. R5 usa a palavra', 'A análise é paráfrase do Ipea. A análise usa a palavra',
      'R-id trocado por "a análise" (o bloco já a identifica como análise do Ipea); a oração "e nenhum item do lote versa sobre o conteúdo do PDRAE" fala de cobertura de itens (seção 6)'),
 ],
 ('C8.1-01', 'd'): [
  RID('R6 diz:', 'o trecho diz:'),
  LOTE('No texto próprio do lote', 'No texto próprio do curso'),
  DEL(' Autoria e ano de origem da NPG: [SEM FONTE — não afirmar].', M_SEMFONTE),
 ],
 ('C8.1-02', 'd'): [
  RID('em artigo da RSP/ENAP, R7: “O governo', 'em artigo da RSP/ENAP: “O governo'),
  RID('Governança Pública (R4) a relaciona', 'Governança Pública (Casa Civil, 2018) a relaciona', 'o bloco só tinha o código (R-id); ele é trocado pelo órgão e ano da publicação (seção 5 do Anexo N)'),
  RID('publicação do Ipea (R8), escreve', 'publicação do Ipea, escreve'),
 ],
 ('C8.0-05', 'g'): [RID('no Ipea (R8, R9, R12), ‘NGP’ é', 'em Cavalcante (Ipea, 2018, pp. 19, 20 e 21), ‘NGP’ é')],
 ('C8.1-02', 'g'): [
  RID('(R7 diz confiança na rede)', '(o artigo diz confiança na rede)'),
  RID('(R7 diz teorias de rede)', '(o artigo diz teorias de rede)'),
 ],
 ('C8.1-03', 'd'): [
  LOTE('No texto próprio do lote:', 'No texto próprio do curso:'),
  RID('em citação literal de R8, R9 e R12 (Ipea), ‘NGP’ significa', 'em citação literal de Cavalcante (Ipea, 2018), ‘NGP’ significa'),
  RID('e em R6 e R7 (ENAP), NPG significa', 'e em Bouckaert (ENAP, 2024), NPG significa'),
  LOTE('nenhum bloco do lote afirma', 'nenhum bloco do curso afirma'),
 ],
 ('C8.1-04', 'd'): [
  DEL('Cronologia da ‘evolução’ da NPG, fundamentos além de redes, colaboração, confiança e reciprocidade, autoria ou ano de origem do conceito: [SEM FONTE — não afirmar]. Se a NPG ‘substitui’ a nova gestão pública (NPM) ou convive com ela é classificação disputada: [SEM FONTE — não afirmar] em nenhum dos dois sentidos. ', M_SEMFONTE + ' (duas frases marcadas)'),
  RID('A sequência de R8 (hierarquia, mercado, redes) é', 'A sequência de Cavalcante (Ipea, 2018: hierarquia, mercado, redes) é', 'R-id trocado por autor, órgão e ano (seção 5 do Anexo N); o parêntese original é mantido dentro do novo'),
 ],
 ('C8.1-04', 'b'): [
  DEL('; Anexo N, seção 5 (SEM FONTE b e c)', M_SEMFONTE + '; a remissão ao Anexo N e à sua seção 5 também sai (seção 6)', D_ORACAO),
 ],
 ('C8.2-01', 'd'): [
  LOTE('este lote não afirma', 'este curso não afirma'),
  ('Nesta folha vale o meio', 'Neste subitem vale o meio', TROCA, E_SUB),
  ('é da folha 8.4.', 'é do subitem 8.4.', TROCA, E_SUB),
 ],
 ('C8.4-02', 'd'): [('é da folha 8.2;', 'é do subitem 8.2;', TROCA, E_SUB)],
 ('C9.4-03', 'd'): [(' Distribuição por folha: ver 8.x (IV, VIII, IX, XI), 9.2 (V, X) e 9.3 (I, III, VII).', '', D_FRASE, E_ACH1 + 'a frase só diz como a produção distribuiu os incisos do art. 4º entre os blocos ("Distribuição por folha"); o estudo não depende dela')],
 ('C8.2-02', 'd'): [
  RID('publicação do Ipea, R9: “as tendências', 'publicação do Ipea: “as tendências'),
  RID('Casa Civil), em R10: “Com múltiplas', 'Casa Civil): “Com múltiplas'),
  RID('ver C8.1-02 (R7).', 'ver 8.1.', 'código de bloco (C8.1-02) trocado pelo número do tópico (8.1) e remissão R7 retirada (seção 6)'),
 ],
 ('C8.2-10', 'd'): [
  DEL(' Definição legal de ‘terceiro setor’: [SEM FONTE — não afirmar].', M_SEMFONTE),
  DEL(' As parcerias com o setor privado em sentido de PPP são as do bloco C8.2-03 a C8.2-05.', M_COD),
 ],
 ('C8.3-01', 'd'): [
  RID('política urbana, R11: “O conceito', 'política urbana: “O conceito'),
  RID('R7 (Bouckaert, ENAP) cita', 'Bouckaert (ENAP) cita', 'o código (R-id) sai e fica o autor e o órgão que o bloco já cita'),
  RID('; ver C8.1-02.', '; ver 8.1.', 'código de bloco (C8.1-02) trocado pelo número do tópico (8.1)'),
 ],
 ('C8.3-02', 'd'): [
  RID('R12 inclui entre as tendências', 'o trecho inclui entre as tendências'),
  RID('Governança Pública (R13): “manter', 'Governança Pública (Casa Civil, 2018): “manter', 'o bloco só tinha o código (R-id); ele é trocado pelo órgão e ano da publicação (seção 5 do Anexo N)'),
 ],
 ('C8.3-03', 'd'): [LOTE('Este lote não afirma', 'Este curso não afirma')],
 ('C8.3-04', 'd'): [
  RID('Governança Pública (R15) lê a diretriz', 'Governança Pública (Casa Civil, 2018) lê a diretriz', 'o bloco só tinha o código (R-id); ele é trocado pelo órgão e ano da publicação (seção 5 do Anexo N)'),
  RID('O Referencial do TCU (R14) inclui', 'O Referencial do TCU (2020) inclui', 'o bloco só tinha o código (R-id); ele é trocado pelo ano da publicação (seção 5 do Anexo N)'),
 ],
 ('C8.3-05', 'd'): [
  DEL('Lado passivo do par, pela exceção única da ficha (curso e par; nunca item), com o texto do Anexo N do D6, seção 4, consulta de 17/10/2026 (mesma URL da fonte N9): ', M_PROC + '; cita "ficha", "Anexo N", "D6" e o código de fonte N9 (seção 6)'),
 ],
 ('C8.3-07', 'd'): [
  DEL('Definição de ‘coprodução do bem público’ em referencial institucional de governança (TCU ou Casa Civil): [SEM FONTE — não afirmar]. ', M_SEMFONTE),
  RID('As fontes do lote são R11 (Ipea, política urbana, capítulo de autoria) e R7 (ENAP, artigo traduzido).',
      'As fontes do curso são Lui et al. (Ipea, política urbana, capítulo de autoria) e Bouckaert (ENAP, artigo traduzido).',
      '"lote" trocado por "curso" (seção 6) e R-ids trocados pelos autores, que a seção 5 do Anexo N atribui às publicações já citadas no parêntese'),
 ],
 ('C8.3-07', 'g'): [LOTE('as fontes do lote não trazem', 'as fontes do curso não trazem')],
 ('C8.3-07', 'b'): [DEL('Anexo N, seção 5 (SEM FONTE e); ', M_SEMFONTE + '; a remissão ao Anexo N e à sua seção 5 também sai (seção 6)', D_ORACAO)],
 ('C8.4-01', 'd'): [DEL(' Autoria ou obra de origem do conceito de valor público: [SEM FONTE — não afirmar].', M_SEMFONTE)],
 ('C8.4-03', 'd'): [
  RID('documento interno do órgão (R16):', 'documento interno do órgão:'),
  RID('publicação do Ipea (R17):', 'publicação do Ipea:'),
 ],
 ('C8.4-04', 'd'): [RID('(Casa Civil), em R18, menciona', '(Casa Civil) menciona')],
 ('C8.4-05', 'd'): [
  DEL('Etapas de uma ‘cadeia de valor público’ além das de R18, origem do conceito de valor público e autoria: [SEM FONTE — não afirmar]. ', M_SEMFONTE),
  RID('R16 é documento interno da CGU', 'O documento didático é documento interno da CGU'),
 ],
 ('C8.4-05', 'b'): [
  RID('Anexo N, seção 5 (SEM FONTE b e g).', 'Decreto 9.203/2017, art. 2º, II; R18.',
      'a Base citava só o Anexo N (SEM FONTE b e g), que a seção 6 manda tirar; passa a valer a Base com os dispositivos que o próprio bloco cita (art. 2º, II, e a publicação da cadeia de valor das políticas públicas)'),
 ],
 ('C9.1-02', 'd'): [
  RID('R19 (TCU, Referencial Básico de Governança Organizacional, 3. ed., 2020, p. 15):', 'Referencial Básico de Governança Organizacional (TCU, 3. ed., 2020, p. 15):', 'o código (R-id) sai e o título e o órgão que o parêntese já citava passam à frente'),
  RID('R23 (Casa Civil, Guia da Política de Governança Pública, 2018, p. 15):', 'Guia da Política de Governança Pública (Casa Civil, 2018, p. 15):', 'o código (R-id) sai e o título e o órgão que o parêntese já citava passam à frente'),
 ],
 ('C9.1-03', 'd'): [
  RID('R20 (TCU, 3. ed., 2020, p. 16):', 'Referencial Básico de Governança Organizacional (TCU, 3. ed., 2020, p. 16):', 'o código (R-id) é trocado pelo título da publicação (seção 5 do Anexo N); órgão, edição, ano e página já estavam no bloco'),
  DEL(', segundo o Anexo N,', 'referência ao Anexo N (seção 6)', D_MARCA),
 ],
 ('C9.1-04', 'd'): [RID('R21 (TCU, 3. ed., 2020, p. 111;', 'Referencial Básico de Governança Organizacional (TCU, 3. ed., 2020, p. 111;', 'o código (R-id) é trocado pelo título da publicação (seção 5 do Anexo N); órgão, edição, ano e página já estavam no bloco')],
 ('C9.1-04', 'g'): [
  DEL(' O texto literal do plano de 1995 e a sua definição de governabilidade: [SEM FONTE — não afirmar].', M_SEMFONTE),
  DEL(', e nenhum item os mistura', M_PROC, D_ORACAO),
  RID('misturar R21 com R5, em que', 'misturar o trecho do Referencial Básico de Governança Organizacional (TCU, 2020) com o de Cavalcante, em que',
      'R-ids trocados pela identificação das publicações (seção 5 do Anexo N); o bloco já falava de "análise publicada pelo Ipea"'),
 ],
 ('C9.1-05', 'd'): [('é da folha 9.2)', 'é do subitem 9.2)', TROCA, E_SUB), RID('R22 (TCU, 3. ed., 2020, p. 21):', 'Referencial Básico de Governança Organizacional (TCU, 3. ed., 2020, p. 21):', 'o código (R-id) é trocado pelo título da publicação (seção 5 do Anexo N); órgão, edição, ano e página já estavam no bloco')],
 ('C9.2-01', 'd'): [RID('R24 (TCU, 3. ed., 2020, p. 37):', 'Referencial Básico de Governança Organizacional (TCU, 3. ed., 2020, p. 37):', 'o código (R-id) é trocado pelo título da publicação (seção 5 do Anexo N); órgão, edição, ano e página já estavam no bloco')],
 ('C9.2-02', 'd'): [RID('R25 (TCU, 3. ed., 2020, p. 54):', 'Referencial Básico de Governança Organizacional (TCU, 3. ed., 2020, p. 54):', 'o código (R-id) é trocado pelo título da publicação (seção 5 do Anexo N); órgão, edição, ano e página já estavam no bloco')],
 ('C9.2-02', 'g'): [RID('equivalência de R25 (instâncias internas)', 'equivalência do referencial do TCU (instâncias internas)', 'R-id trocado por "referencial do TCU" (o bloco já identifica a publicação; evita parêntese dentro de parêntese)')],
 ('C9.2-03', 'd'): [RID('R26 (TCU, 3. ed., 2020, p. 69):', 'Referencial Básico de Governança Organizacional (TCU, 3. ed., 2020, p. 69):', 'o código (R-id) é trocado pelo título da publicação (seção 5 do Anexo N); órgão, edição, ano e página já estavam no bloco')],
 ('C9.2-03', 'g'): [RID('atribuir a R26 (que fala', 'atribuir ao referencial do TCU (que fala', 'R-id trocado por "referencial do TCU" (o bloco já identifica a publicação; evita parêntese dentro de parêntese)')],
 ('C9.2-04', 'd'): [RID('R27 (TCU, 3. ed., 2020, p. 88, nota 12):', 'Referencial Básico de Governança Organizacional (TCU, 3. ed., 2020, p. 88, nota 12):', 'o código (R-id) é trocado pelo título da publicação (seção 5 do Anexo N); órgão, edição, ano e página já estavam no bloco')],
 ('C9.2-07', 'd'): [DEL(' O ponto do BQ-0152 (integridade como princípio e também como condição da liderança) é de item real bloqueado e não é julgado aqui.', M_PROC + '; cita item do banco (BQ-0152)')],
 ('C9.3-02', 'd'): [DEL(' Origem e autoria do conceito de valor público: [SEM FONTE — não afirmar].', M_SEMFONTE)],
 ('C9.3-03', 'd'): [
  RID('R28 (TCU, 3. ed., 2020, p. 15-16):', 'Referencial Básico de Governança Organizacional (TCU, 3. ed., 2020, p. 15-16):', 'o código (R-id) é trocado pelo título da publicação (seção 5 do Anexo N); órgão, edição, ano e página já estavam no bloco'),
  DEL(' Definição oficial de sustentabilidade de políticas públicas: [SEM FONTE — não afirmar].', M_SEMFONTE),
 ],
 ('C9.3-03', 'g'): [RID('(R28, sentido genérico)', '(referencial do TCU, sentido genérico)', 'R-id trocado por "referencial do TCU" (o bloco já identifica a publicação)')],
 ('C9.3-05', 'd'): [
  RID('R30 (Casa Civil, guia prático de análise ex post, v. 2, 2018, p. 33):', 'Guia prático de análise ex post (Casa Civil, v. 2, 2018, p. 33):', 'o código (R-id) sai e o título e o órgão que o parêntese já citava passam à frente'),
  RID('R31 (mesma obra, p. 33):', 'Na mesma obra (p. 33):', 'o código (R-id) sai; "mesma obra" já remetia à publicação do trecho anterior'),
 ],
 ('C9.3-06', 'd'): [RID('R18 (Casa Civil, guia prático de análise ex post, v. 2, 2018, p. 13):', 'Guia prático de análise ex post (Casa Civil, v. 2, 2018, p. 13):', 'o código (R-id) sai e o título e o órgão que o parêntese já citava passam à frente')],
 ('C9.4-02', 'g'): [DEL(' Observação: o ponto do BQ-0152 (integridade como princípio e também como condição da liderança) é de item real bloqueado e não é julgado aqui.', M_PROC + '; cita item do banco (BQ-0152)')],
 ('C9.4-04', 'd'): [DEL(' Resoluções e manuais do CIG: [SEM FONTE — não afirmar].', M_SEMFONTE)],
 ('C9.4-06', 'g'): [DEL(' (lição do item real inapto BQ-0151, por causa do art. 14 revogado)', M_PROC + '; cita item do banco (BQ-0151)', D_ORACAO)],
 ('C9.4-07', 'g'): [RID('(art. 5º, III; R27)', '(art. 5º, III)', M_RID2)],
 ('C9.4-10', 'd'): [DEL(' Conteúdo dos manuais, guias e resoluções do CIG: [SEM FONTE — não afirmar].', M_SEMFONTE)],
 ('C9.4-12', 'd'): [DEL(' (os quatro princípios do artigo estão em C9.4-07)', M_COD, D_ORACAO)],
}

# títulos: R-ids e marcas de produção saem dos títulos dos blocos
TIT_REGRAS = [
 (re.compile(r' \(R\d+(?:[,;] R\d+)*(?: em [\d.]+|, [^)]*)?\)'), '', 'R-id entre parênteses no título do bloco'),
 (re.compile(r'\((R\d+(?:, R\d+)*); '), '(', 'R-id no início do parêntese do título do bloco'),
 (re.compile(r'; R\d+(?:, R\d+)*(?=[;)])'), '', 'R-id dentro do parêntese do título do bloco'),
 (re.compile(r'; R\d+ em [\d.]+$'), '', 'R-id com remissão ("R7 em 8.1") no título do bloco'),
 (re.compile(r': só curso$'), '', 'marca de cobertura ("só curso") no título do bloco'),
 (re.compile(r'; exceção da ficha(?=\))'), '', 'remissão à ficha no título do bloco'),
]
RX_SUFIXO = re.compile(r' — acréscimo da v2 \(leitura externa [^()]*; QA PENDENTE \(R2\)\)$')
RX_SUFIXO_G = re.compile(r' \(acréscimo da v2; leitura externa [^()]*; QA PENDENTE \(R2\)\)$')

# BASE LEGAL: só dispositivos que o bloco já cita (título, definição, Base) + publicações do referencial (R-ids do bloco)
D = 'Decreto 9.203/2017, '
BASE_LEGAL = OrderedDict([
 ('C8.0-01', ([], [1])), ('C8.0-02', ([], [1, 2, 4])), ('C8.0-03', ([], [2])), ('C8.0-04', ([], [3, 4])), ('C8.0-05', ([], [8, 9, 12, 6])), ('C8.0-06', ([], [5, 21])),
 ('C8.1-01', ([], [6])), ('C8.1-02', ([], [7, 4, 8])), ('C8.1-03', ([], [4, 6, 7, 8, 9, 12])), ('C8.1-04', ([], [8])),
 ('C8.2-01', ([D + 'art. 4º, caput e IV'], [])), ('C8.2-02', ([], [9, 10])),
 ('C8.2-03', (['Lei 11.079/2004, art. 2º, caput', 'Lei 11.079/2004, art. 2º, § 3º'], [])),
 ('C8.2-04', (['Lei 11.079/2004, art. 2º, §§ 1º e 2º'], [])),
 ('C8.2-05', (['Lei 11.079/2004, art. 2º, § 4º, I a III'], [])),
 ('C8.2-06', (['Lei 13.019/2014, art. 2º, I, a a c', 'Lei 13.019/2014, art. 2º, III'], [])),
 ('C8.2-07', (['Lei 13.019/2014, art. 2º, VII, VIII e VIII-A'], [])),
 ('C8.2-08', (['Lei 9.637/1998, art. 1º'], [])),
 ('C8.2-09', (['Lei 9.790/1999, art. 1º, caput e § 2º'], [])),
 ('C8.2-10', (['Lei 13.019/2014, art. 2º, I', 'Lei 9.637/1998, art. 1º', 'Lei 9.790/1999, art. 1º', 'Lei 11.079/2004, art. 2º'], [])),
 ('C8.3-01', ([], [11, 7])), ('C8.3-02', ([D + 'art. 4º, VIII e IX'], [12, 13])),
 ('C8.3-03', (['Lei 13.460/2017, art. 1º, caput', 'Lei 13.460/2017, art. 1º, § 1º', 'Lei 13.460/2017, art. 1º, § 3º', 'Lei 13.460/2017, art. 6º, I'], [])),
 ('C8.3-04', ([D + 'art. 4º, XI', 'Lei 12.527/2011, art. 8º, caput'], [14, 15])),
 ('C8.3-05', (['Lei 12.527/2011, art. 10, caput'], [14])),
 ('C8.3-06', (['Lei 12.527/2011, art. 8º, § 1º, I a VI'], [])),
 ('C8.3-07', ([], [11, 7])),
 ('C8.4-01', ([D + 'art. 2º, II'], [])), ('C8.4-02', ([D + 'art. 4º, IV'], [])),
 ('C8.4-03', ([], [16, 17])), ('C8.4-04', ([], [18])), ('C8.4-05', ([D + 'art. 2º, II'], [18, 16])),
 ('C9.1-01', ([D + 'art. 2º, I'], [])), ('C9.1-02', ([D + 'art. 2º, I'], [19, 23])), ('C9.1-03', ([D + 'art. 2º, I'], [20])),
 ('C9.1-04', ([], [21, 5])), ('C9.1-05', ([D + 'art. 5º, II'], [22])),
 ('C9.2-01', ([D + 'art. 5º, caput e I a III', D + 'art. 3º, VI'], [24])), ('C9.2-02', ([D + 'art. 5º, I, a a d'], [25])),
 ('C9.2-03', ([D + 'art. 5º, II'], [26])), ('C9.2-04', ([D + 'art. 5º, III'], [27])),
 ('C9.2-05', ([D + 'art. 6º, caput e parágrafo único'], [])), ('C9.2-06', ([D + 'art. 4º, V e X'], [])),
 ('C9.2-07', ([D + 'art. 5º, I, b e d', D + 'art. 3º, I a VI'], [])),
 ('C9.3-01', ([D + 'art. 2º, II'], [])), ('C9.3-02', ([], [29])), ('C9.3-03', ([D + 'art. 4º, I'], [28])),
 ('C9.3-04', ([D + 'art. 4º, III e VII', D + 'art. 6º, parágrafo único, I'], [])), ('C9.3-05', ([], [30, 31])), ('C9.3-06', ([], [18])),
 ('C9.4-01', ([D + 'arts. 1º e 2º'], [])), ('C9.4-02', ([D + 'art. 3º, I a VI'], [])), ('C9.4-03', ([D + 'art. 4º, II e VI', D + 'art. 3º', D + 'art. 5º'], [])),
 ('C9.4-04', ([D + 'arts. 7º-A, 8º-A, 8º-B e 9º-A'], [])), ('C9.4-05', ([D + 'arts. 10-A, 10-B, 11-A e 12-A'], [])),
 ('C9.4-06', ([D + 'arts. 13-A, 15-A e 16'], [])), ('C9.4-07', ([D + 'arts. 17 e 18'], [])), ('C9.4-08', ([D + 'art. 19'], [])),
 ('C9.4-09', ([D + 'arts. 7º-A a 15-A (com letra)', D + 'art. 11-A, caput (redação do Decreto 10.907/2021)'], [])),
 ('C9.4-10', ([D + 'art. 7º-A', D + 'art. 9º-A, II, III, § 1º e § 2º', D + 'art. 13-A'], [])),
 ('C9.4-11', ([D + 'art. 4º, II', D + 'art. 3º'], [])), ('C9.4-12', ([D + 'art. 17, II e III'], [])),
])

def linha_fonte(n):
    f = RFAM[n]
    return f'Fonte: {FAM[f]["fonte"]}, p. {RPAG[n]}'

def linhas_fonte(rids):
    """Uma linha por publicação (família), com todas as páginas das R-ids do bloco nessa publicação (pp.)."""
    ordem, pag = [], {}
    for n in rids:
        f = RFAM[n]
        if f not in pag: pag[f] = []; ordem.append(f)
        if RPAG[n] not in pag[f]: pag[f].append(RPAG[n])
    out = []
    for f in ordem:
        ps = sorted(pag[f], key=int) if all(x.isdigit() for x in pag[f]) else pag[f]
        out.append(f'Fonte: {FAM[f]["fonte"]}, ' + ('p. ' + ps[0] if len(ps) == 1 else 'pp. ' + ', '.join(ps)))
    return out

# ---------------------------------------------------------------- curso
def titulo_edital(eid):
    t = EDITAL[eid]
    if len(t) > 90 and ':' in t: t = t.split(':')[0]
    return t.upper()

def sentencas(txt):
    partes, ini = [], 0
    for m in re.finditer(r'\.\s+(?=[A-ZÁÉÍÓÚ§])', txt):
        antes = txt[ini:m.start() + 1]
        if re.search(r'\b(art|arts|inc|n)\.$', antes): continue
        ate = txt[:m.start()]
        if ate.count('“') > ate.count('”') or ate.count('"') % 2 == 1: continue   # não corta dentro de citação
        partes.append(antes); ini = m.end()
    partes.append(txt[ini:])
    return [p.strip() for p in partes if p.strip()]

def parse_curso(L):
    ini = achar(L, '## 1. (a) CURSO'); fim = achar(L, '## 2. (b) RESUMO', ini)
    partes, bloco = [], None
    for l in L[ini + 1:fim]:
        m = re.match(r'^### PARTE (1\.\d) — (\d(?:\.\d)?) (.+)$', l)
        if m:
            partes.append(dict(cod=m.group(1), folha=m.group(2), titulo_origem=l[4:], blocos=[])); bloco = None; continue
        m = re.match(r'^\*\*(C\d\.\d-\d\d) (.+?)\*\*(.*)$', l)
        if m and partes:
            bloco = dict(cod=m.group(1), titulo=m.group(2), sufixo=m.group(3), linhas=[l], campos={})
            partes[-1]['blocos'].append(bloco); continue
        if l.strip() in ('', '---'): continue
        if bloco is not None and l.startswith('- '):
            bloco['linhas'].append(l)
            for chave, pref in (('def', '- Definição: '), ('ex', '- Exemplo (Legislativo, hipotético): '), ('peg', '- Pegadinha provável: ')):
                if l.startswith(pref): bloco['campos'][chave] = l[len(pref):].strip(); break
            else:
                raise SystemExit('PARAR: linha inesperada no curso: ' + l[:80])
        elif bloco is None:
            continue   # parágrafos introdutórios da seção 1 (processo; não entram)
        else:
            raise SystemExit('PARAR: linha inesperada no curso: ' + l[:80])
    for p in partes:
        pref = 'C8.0-' if p['folha'] == '8' else 'C' + p['folha'] + '-'
        for b in p['blocos']:
            assert set(b['campos']) == {'def', 'ex', 'peg'}, b['cod']
            assert b['cod'].startswith(pref), (b['cod'], p['folha'])
    return partes

def aplica_expl(ctx, cod, campo, txt):
    for ant, nov, tipo, motivo in EXPL.get((cod, campo), []):
        txt = edita(ctx, txt, ant, nov, tipo, motivo)
    return txt

def limpa_titulo(cod, tit, sufixo):
    ctx = f'curso {cod} (título)'
    for rx, nov, motivo in TIT_REGRAS:
        while True:
            m = rx.search(tit)
            if not m: break
            log(ctx, D_MARCA, m.group(0).strip(), '', motivo)
            tit = tit[:m.start()] + nov + tit[m.end():]
    if sufixo:
        assert RX_SUFIXO.fullmatch(sufixo), (cod, sufixo)
        log(ctx, D_MARCA, sufixo.strip(), '', 'marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa")')
    assert not re.search(r'\bR\d|SEM FONTE|ficha|lote', tit), (cod, tit)
    return tit

def pegadinha_texto(ctx, cod, claim, base, rotulo_antigo, rotulo_novo):
    """claim/base já separados; aplica as edições explícitas, troca os R-ids e junta com 'Base:'."""
    claim = aplica_expl(ctx, cod, 'g', claim)
    base = aplica_expl(ctx, cod, 'b', base)
    claim = subst_ids(ctx, claim, 'auto')
    base = subst_ids(ctx, base, 'base')
    log(ctx, 'troca de rótulo', rotulo_antigo, rotulo_novo, 'operação 2 da seção 7')
    return claim, base

def monta_curso(partes):
    out, mapa = [], []
    for p in partes:
        eid = 'P1-DA-' + p['folha']
        cab = f"## {p['folha']} {titulo_edital(eid)}"
        out += [cab, '']
        mapa.append(dict(origem=p['titulo_origem'], destino=cab))
        for b in p['blocos']:
            cod = b['cod']; ctx = 'curso ' + cod
            tit = limpa_titulo(cod, b['titulo'], b['sufixo'])
            d, e, g = b['campos']['def'], b['campos']['ex'], b['campos']['peg']
            d = aplica_expl(ctx + ' (definição)', cod, 'd', d)
            d = subst_ids(ctx + ' (definição)', d, 'auto')
            e = aplica_expl(ctx + ' (exemplo)', cod, 'e', e)
            e = subst_ids(ctx + ' (exemplo)', e, 'auto')
            # pegadinha: pode haver texto depois do colchete (C9.1-04, C9.4-02): as edições explícitas do campo 'g' o tiram antes
            g = aplica_expl(ctx + ' (pegadinha)', cod, 'g', g)
            m = re.fullmatch(r'(.*?) \[Desfeita por: (.+)\]', g)
            assert m, (cod, g[-90:])
            claim, base = m.group(1), m.group(2)
            base = aplica_expl(ctx + ' (pegadinha)', cod, 'b', base)
            claim = subst_ids(ctx + ' (pegadinha)', claim, 'auto')
            base = subst_ids(ctx + ' (pegadinha)', base, 'base')
            log(ctx + ' (pegadinha)', 'troca de rótulo', '[Desfeita por: ' + m.group(2) + ']', 'Base: ' + base, 'operação 2 da seção 7')
            g = claim + ' Base: ' + base
            assert e.endswith('O exemplo é hipotético.') or 'exemplo é hipotético' in e, (cod, e[-60:])
            for campo_txt in (tit, d, e, g):
                assert not re.search(r'Anexo|BASE DOUTRIN|SEM FONTE|REVERIFICAR|BQ-|\bC\d\.\d-\d\d|QA PENDENTE|\bv[12]\b|\bR\d{1,2}\b|\bF\d{1,2}\b|\blote\b|\bficha\b|NÃO CONFERID', campo_txt), (cod, campo_txt[:120])
            out += ['### ' + tit, '']
            mapa.append(dict(origem=f"{cod} {b['titulo']}" + (f" {b['sufixo'].strip()}" if b['sufixo'] else ''), destino='### ' + tit))
            out.append('DEFINIÇÃO')
            ss = sentencas(d)
            if len(ss) >= 3: out.extend('- ' + s for s in ss)
            else: out.append(d)
            out.append('')
            dispositivos, rids = BASE_LEGAL[cod]
            linhas_bl, vistos = list(dispositivos), set()
            for lf in linhas_fonte(rids):
                if lf not in vistos: vistos.add(lf); linhas_bl.append(lf)
            if linhas_bl:
                out.append('BASE LEGAL'); out.extend('- ' + x for x in linhas_bl); out.append('')
            out += ['EXEMPLO PARLAMENTAR', e, '', 'PEGADINHA PROVÁVEL', g, '']
            b['saida'] = dict(titulo=tit, d=d, e=e, g=g, base=linhas_bl)
    while out and out[-1] == '': out.pop()
    return '\n'.join(out), mapa

# ---------------------------------------------------------------- resumo
EXPL_RESUMO = [
 ('(caput) e folhas 8.1 a 8.4.**', '(caput) e subitens 8.1 a 8.4.**', TROCA, E_ACH1 + '"folha" é termo de produção (seção 6); o título do resumo do item 8 aponta os subitens 8.1 a 8.4 (números dos `##` do curso)'),
 (' Fontes: Anexo N (normas, seção 4; referencial R1 a R18, seção 5).', '', D_FRASE, 'frase de proveniência com "Anexo N", sua seção e R-ids (seção 6)'),
 (' Autor de periódico ou livro (F4 a F9) nunca é atribuído ao órgão.', '', D_FRASE, 'regra de redação de produção com códigos de fonte (F4 a F9) (seção 6)'),
 ('| R1 (Bresser-Pereira, RSP/ENAP) |', '| Bresser-Pereira, Revista do Serviço Público (ENAP, 2022) |', TROCA, IDENT + ' (célula da tabela)'),
 ('| R1, R2; R8 (Ipea); R4 (Guia da Casa Civil) |', '| Bresser-Pereira (ENAP, 2022); Cavalcante (Ipea, 2018); Guia da Política de Governança Pública (Casa Civil, 2018) |', TROCA, IDENT + ' (célula da tabela)'),
 ('| R3; R4; R8 |', '| Bresser-Pereira (ENAP, 2022); Guia da Política de Governança Pública (Casa Civil, 2018); Cavalcante (Ipea, 2018) |', TROCA, IDENT + ' (célula da tabela)'),
 ('| R4; R8; R9; R12 |', '| Guia da Política de Governança Pública (Casa Civil, 2018); Cavalcante (Ipea, 2018) |', TROCA, IDENT + ' (célula da tabela; R8, R9 e R12 são do mesmo texto)'),
 ('| R6; R7 (Bouckaert, RSP/ENAP) |', '| Bouckaert, Revista do Serviço Público (ENAP, 2024) |', TROCA, IDENT + ' (célula da tabela; R6 e R7 são do mesmo artigo)'),
 ('| Só no curso e atribuído (paráfrase publicada pelo Ipea); texto do plano: [SEM FONTE — não afirmar] | R5 |', '| Atribuído (paráfrase publicada pelo Ipea) | Cavalcante (Ipea, 2020) |', TROCA,
  '"Só no curso" é fala de cobertura de itens; "texto do plano: [SEM FONTE — não afirmar]" é frase marcada (seção 6); R-id trocado pela identificação'),
 ('| R11 |', '| Lui et al. (Ipea, 2023) |', TROCA, IDENT + ' (célula da tabela)'),
 ('| R12; R13 |', '| Cavalcante (Ipea, 2018); Guia da Política de Governança Pública (Casa Civil, 2018) |', TROCA, IDENT + ' (célula da tabela)'),
 ('| Lei 12.527/2011, art. 8º, caput; R14; R15 |', '| Lei 12.527/2011, art. 8º, caput; Referencial Básico de Governança Organizacional (TCU, 2020); Guia da Política de Governança Pública (Casa Civil, 2018) |', TROCA, IDENT + ' (célula da tabela)'),
 (' (só curso e par)', '', D_ORACAO, 'parêntese de cobertura de itens (seção 6)'),
 (' (Anexo N do D6)', '', D_MARCA, 'referência ao Anexo N e a outro lote (seção 6)'),
 ('| R16 (CGU) |', '| Documento didático da CGU |', TROCA, IDENT + ' (célula da tabela)'),
 ('| R17 |', '| Martins (Ipea, 2018) |', TROCA, IDENT + ' (célula da tabela)'),
 ('| R18 |', '| Guia prático de análise ex post (Casa Civil, 2018) |', TROCA, IDENT + ' (célula da tabela)'),
 ('; ‘terceiro setor’ e ‘coprodução do bem público’ não têm definição legal ou institucional nas fontes do lote ([SEM FONTE — não afirmar])', '', D_ORACAO, M_SEMFONTE + '; a oração marcada também cita "fontes do lote"'),
 (' Definição oficial de sustentabilidade de políticas públicas: [SEM FONTE — não afirmar].', '', D_FRASE, M_SEMFONTE),
]

def monta_resumo(L):
    ini = achar(L, '## 2. (b) RESUMO'); fim = achar(L, '---', ini)
    linhas = list(L[ini + 1:fim])
    while linhas and not linhas[0].strip(): linhas.pop(0)
    while linhas and not linhas[-1].strip(): linhas.pop()
    txt = '\n'.join(linhas)
    for ant, nov, tipo, motivo in EXPL_RESUMO:
        txt = edita('resumo', txt, ant, nov, tipo, motivo)
    txt = subst_ids('resumo', txt, 'auto')
    return txt

# ---------------------------------------------------------------- pares
EXPL_PARES = {
 'P-07': [('; só curso e par)', ')', D_ORACAO, 'parêntese de cobertura de itens ("só curso e par") (seção 6)')],
 'P-60': [(' O par não julga a integridade como mecanismo (ponto bloqueado do BQ-0152).', '', D_FRASE, M_PROC + '; cita item do banco (BQ-0152)')],
}
def monta_pares(L):
    ini = achar(L, '## 3. (c) PARES'); fim = achar(L, '## 4. (d) PEGADINHAS', ini)
    pares = []
    for l in L[ini:fim]:
        if not re.match(r'^\| P-\d\d', l): continue
        cel = [c.strip() for c in l.strip().strip('|').split('|')]
        assert len(cel) == 5, l[:60]
        cod, par, dif, _base, banca = cel
        ctx = 'par ' + cod
        m = RX_SUFIXO.search(par)
        if m:
            log(ctx, D_MARCA, m.group(0).strip(), '', 'marca de produção no campo Par (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa")')
            par = par[:m.start()]
        for ant, nov, tipo, motivo in EXPL_PARES.get(cod, []):
            dif = edita(ctx, dif, ant, nov, tipo, motivo)
        dif = subst_ids(ctx, dif, 'auto'); banca = subst_ids(ctx, banca, 'auto')
        termos = par.split(' × ')
        assert len(termos) >= 2, par
        a, b = termos[0], ' × '.join(termos[1:])
        assert dif.endswith('.') and banca.endswith('.'), cod
        pares.append(dict(a=a, b=b, como=dif + ' Como a banca troca: ' + banca, _cod=cod))
    assert len(pares) == 24, len(pares)
    return pares

def codigo_folha(cod):
    m = re.match(r'C(\d)\.(\d)-', cod)
    return 'P1-DA-8' if cod.startswith('C8.0-') else f'P1-DA-{m.group(1)}.{m.group(2)}'

def monta_pegadinhas(L):
    ini = achar(L, '## 4. (d) PEGADINHAS'); fim = achar(L, '---', ini)
    out = []
    for l in L[ini + 1:fim]:
        m = re.match(r'^G-(\d\d)\. \[(C\d\.\d-\d\d)\] (.+)$', l)
        if not m: continue
        n, cod, t = int(m.group(1)), m.group(2), m.group(3)
        ctx = f'pegadinha {n}'
        ms = RX_SUFIXO_G.search(t)
        if ms:
            log(ctx, D_MARCA, ms.group(0).strip(), '', 'marca de produção ao fim da pegadinha (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa")')
            t = t[:ms.start()]
        for rot in (' — Desfeita por: ', ' — Dispositivo ou trecho que a desfaz: '):
            if rot in t: claim, _, base = t.partition(rot); break
        else:
            raise SystemExit('PARAR: pegadinha sem rótulo: ' + l[:80])
        claim = claim.strip(); base = base.strip()
        # as edições explícitas do campo 'g' valem para o texto antes de "Base" (as mesmas do bloco do curso, quando o texto coincide)
        for ant, nov, tipo, motivo in EXPL.get((cod, 'g'), []):
            if ant in claim: claim = edita(ctx, claim, ant, nov, tipo, motivo)
        for ant, nov, tipo, motivo in EXPL.get((cod, 'b'), []):
            if ant in base: base = edita(ctx, base, ant, nov, tipo, motivo)
        claim = subst_ids(ctx, claim, 'auto'); base = subst_ids(ctx, base, 'base')
        log(ctx, 'troca de rótulo', rot.strip() + ' ' + '…', 'Base: …', 'operação 2 da seção 7 (os dois rótulos do canônico — "Desfeita por:" e "Dispositivo ou trecho que a desfaz:" — viram "Base:", como no curso)')
        assert claim.endswith(('.', '?', '!')), (n, claim[-30:])
        eid = codigo_folha(cod)
        out.append(dict(itemEdital=eid, rotulo=EDITAL[eid], texto=claim + ' Base: ' + base, _n=n, _cod=cod))
    assert len(out) == 62, len(out)
    return out

# ---------------------------------------------------------------- itens
EXPL_JUST = {
 'D4-36': [('a nota do Anexo N registra que, na mesma página', 'na mesma página', D_ORACAO, 'a oração "a nota do Anexo N registra que" cita o Anexo N (seção 6); fica a informação (na mesma página, o referencial diz…)')],
 'D4-48': [('; a contagem exata de alíneas do rol vigente é admitida pela ficha', '', D_ORACAO, 'oração de regra de produção ("admitida pela ficha") (seção 6)')],
 'D4-67': [(' é admitida pela ficha e', '', D_ORACAO, 'regra de produção ("admitida pela ficha") (seção 6); fica "a contagem exata não julga o conteúdo de nenhum princípio"')],
}
# errata de forma de 20/10/2026: aplicada DEPOIS da troca dos R-ids (subst_ids), sobre o texto já exibido
ERRATA_JUST = {
 'D4-14': [('tratada na folha 8.4', 'tratada no subitem 8.4', TROCA, E_SUB)],
 'D4-27': [('; o meio (integração entre níveis e esferas) é ponto da folha 8.2', '', D_ORACAO, E_ACH1 + 'a oração só situa o "meio" como ponto de outra folha da produção (seção 7 da especificação: frase que só fala do processo fica fora); o item trata da finalidade da diretriz')],
 'D4-30': [('é tratada na folha 9.3', 'é tratada no subitem 9.3', TROCA, E_SUB)],
 'D4-38': [(' (TCU, 2020) (única fonte institucional da distinção) e não mistura', ' (TCU, 2020), única fonte institucional da distinção, e não mistura', TROCA, E_ACH7 + 'a troca do código de referencial pelo nome da publicação deixou dois parênteses em sequência; o segundo vira aposto entre vírgulas (nenhuma palavra muda; só a pontuação)')],
 'D4-49': [(', ponto da folha 9.1)', ')', D_ORACAO, E_ACH1 + 'o aposto só situa o "alinhamento" como ponto de outra folha da produção; fica "(sem o alinhamento)"')],
 'D4-52': [('da folha 9.3)', 'do subitem 9.3)', TROCA, E_SUB)],
 'D4-63': [(' (ponto da folha 8.4)', '', D_ORACAO, E_ACH1 + 'o parêntese só situa os "elos da cadeia de valor" como ponto de outra folha da produção (frase de processo)')],
 'D4-62': [('; o guia prático de análise ex post (Casa Civil, 2018) acrescenta', '; o mesmo guia acrescenta', TROCA, E_ACH7 + 'a troca de R30 e R31 pelo nome da publicação repetiu "o guia prático de análise ex post (Casa Civil, 2018)"; a segunda menção volta a "o mesmo guia" (a primeira já identifica a publicação)')],
 'D4-75': [(', e o artigo de Bresser-Pereira (ENAP, 2022) a chama', ', e o mesmo artigo a chama', TROCA, E_ACH7 + 'a troca de R1 e R2 pelo nome da publicação repetiu "o artigo de Bresser-Pereira (ENAP, 2022)"; a segunda menção volta a "o mesmo artigo"')],
 'D4-78': [('; o artigo de Bresser-Pereira (ENAP, 2022) acrescenta', '; o mesmo artigo acrescenta', TROCA, E_ACH7 + 'a troca de R2 pelo nome da publicação repetiu "o artigo de Bresser-Pereira (ENAP, 2022)"; a segunda menção volta a "o mesmo artigo"')],
}

def monta_itens(L):
    i51 = achar(L, '### 5.1'); i52 = achar(L, '### 5.2', i51); fim = achar(L, '## 6.', i52)
    enun = {}
    for l in L[i51:i52]:
        m = re.match(r'^\*\*(D4-\d\d)\.\*\* (.+)$', l)
        if m: enun[m.group(1)] = m.group(2)
    blocos, cur = [], None
    for l in L[i52:fim]:
        m = re.match(r'^\*\*(D4-\d\d)\*\* \((folha \d\.\d|caput 8)\) — AUTORAL — (.*)$', l)
        if m: cur = dict(id=m.group(1), folha=m.group(2), cab=m.group(3), F={}); blocos.append(cur); continue
        if cur is not None and l.startswith('- '):
            k, _, v = l[2:].partition(': ')
            cur['F'][k] = v
    assert len(blocos) == 79 and len(enun) == 79, (len(blocos), len(enun))
    itens = []
    for b in sorted(blocos, key=lambda x: int(x['id'].split('-')[1])):
        i = b['id']
        fo = b['folha']
        assert b['F']['Folha'] == (fo[6:] if fo.startswith('folha') else 'caput 8 (não é folha)'), (i, b['F']['Folha'], fo)
        j1, j2 = b['F']['Justificativa (linha 1)'].strip(), b['F']['Justificativa (linha 2)'].strip()
        j = j1 + ' ' + j2
        ctx = 'justificativa ' + i
        for ant, nov, tipo, motivo in EXPL_JUST.get(i, []):
            j = edita(ctx, j, ant, nov, tipo, motivo)
        j = subst_ids(ctx, j, 'auto')
        for ant, nov, tipo, motivo in ERRATA_JUST.get(i, []):
            j = edita(ctx, j, ant, nov, tipo, motivo)
        marcas = b['F']['Marcas']
        vol = ('REVERIFICAR=sim' in marcas) or ('VOLÁTIL=sim' in marcas)
        eid = 'P1-DA-8' if fo.startswith('caput') else 'P1-DA-' + fo[6:]
        it = dict(id=i, rotulo='AUTORAL', certame='Projeto Câmara 2026', cargo='Noções de Direito Administrativo e Administração Pública', ano=2026,
                  numero=int(i.split('-')[1]), comando='Julgue o item a seguir.', textoBase='', enunciado=enun[i],
                  gabarito=b['F']['Gabarito'].strip(), justificativa=j, itemEdital=eid, aderencia='direta', url=URL_CANON)
        if vol: it['volatil'] = True
        it['_marcas'] = marcas; it['_j1'] = j1; it['_j2'] = j2
        itens.append(it)
    return itens

# ---------------------------------------------------------------- montagem
def monta():
    LOG.clear()
    L = ler_canon()
    partes = parse_curso(L)
    curso, mapa = monta_curso(partes)
    resumo = monta_resumo(L)
    pares = monta_pares(L)
    pegs = monta_pegadinhas(L)
    itens = monta_itens(L)
    ie = ['P1-DA-' + p['folha'] for p in partes]
    assert ie == ['P1-DA-8', 'P1-DA-8.1', 'P1-DA-8.2', 'P1-DA-8.3', 'P1-DA-8.4', 'P1-DA-9.1', 'P1-DA-9.2', 'P1-DA-9.3', 'P1-DA-9.4'], ie
    lote = dict(id='D4', nome=NOME, prova='P1', itensEdital=ie, resumo=resumo, curso=curso,
                pares=[{k: v for k, v in p.items() if not k.startswith('_')} for p in pares],
                pegadinhas=[{k: v for k, v in p.items() if not k.startswith('_')} for p in pegs])
    if TOPICOS.exists():
        tp = json.loads(TOPICOS.read_text(encoding='utf-8'))
        if set(tp) != set(ie): raise SystemExit('PARAR: chaves de D4_topicos_fonte.json diferem dos blocos ##: ' + str(sorted(set(tp) ^ set(ie))))
        topicos = OrderedDict((k, tp[k]) for k in ie)
    else:
        print('AVISO: D4_topicos_fonte.json ainda não existe; topicos vazio'); topicos = OrderedDict()
    itens_pub = [{k: v for k, v in it.items() if not k.startswith('_')} for it in itens]
    dados = dict(lote=lote, itens=itens_pub, topicos=topicos)
    return dados, dict(L=L, partes=partes, mapa=mapa, itens=itens, pares=pares, pegs=pegs, resumo=resumo, curso=curso)

def grava(dados):
    SAIDA_JSON.write_text(json.dumps(dados, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

# ---------------------------------------------------------------- registro
def roda(cmd):
    r = subprocess.run([sys.executable, '-I'] + cmd, capture_output=True, text=True, cwd=str(RAIZ))
    return r.returncode, (r.stdout + r.stderr).strip()

def agrupa_log():
    """Agrupa as trocas de identificação (R-id → publicação) por contexto, para o registro ficar legível."""
    saida, grupos = [], OrderedDict()
    for e in LOG:
        if e['tipo'] == 'troca de rótulo': continue
        if e['motivo'].startswith('errata de forma'): continue
        if e['motivo'].startswith(IDENT):
            grupos.setdefault(e['ctx'], []).append(e)
        else:
            saida.append(e)
    return saida, grupos

def registro(dados, ctx):
    rc_val, val = roda([str(VALIDADOR), str(SAIDA_JSON), str(CANON), str(MAPA)])
    rc_fid, fid = roda([str(CONFERE)])
    it = dados['itens']
    por_folha = Counter(x['itemEdital'] for x in it)
    n_c = sum(1 for x in it if x['gabarito'] == 'C'); n_e = len(it) - n_c
    vol = [x['id'] for x in it if x.get('volatil')]
    por_peg = Counter(p['itemEdital'] for p in dados['lote']['pegadinhas'])
    W = []
    W.append('# D4_registro_formato.md — T-77 (ordem DA 20/10/2026) — 2026-10-20 — gerado por gcb-cpp')
    W.append('')
    W.append('Reformatação do Lote D4 (Gestão pública e governança, itens 8 e 9 do edital) para o formato da plataforma (FORMATO_PLATAFORMA_DA.md). Só forma; nenhum conteúdo novo. Gerado por `saida/gcb/DA_plataforma/scripts/formatar_D4.py --registro`; fidelidade por `saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D4.py`.')
    W.append('')
    W.append('## 1. Fontes e conferências')
    W.append(f'- Canônico: saida/gcb/D4_v2_1.md, SHA-256 {sha(CANON.read_bytes())} (igual ao esperado c1a7a935…e5d9: o script confere antes de ler e pararia se divergisse).')
    W.append(f'- Base normativa e de referencial: saida/gcb/D4_anexo_N_mapa_normativo.md (consulta de 20/10/2026), SHA-256 {sha(MAPA.read_bytes())}. Usada pelo validador, pelo visual baseLegal (texto copiado por script, letra a letra, da coluna de texto do mapa; `literal: true`; `conferido: 2026-10-20`) e para a identificação das publicações (órgão, autor, ano e página da seção 5; o script confere a página de cada R1 a R31 contra a tabela do mapa).')
    W.append('- Seções do canônico NÃO usadas: cabeçalho (linhas 1 a 6), 0 e 0.1 (resposta ao R1 e registro de acatamento), os parágrafos introdutórios da seção 1, o cabeçalho das seções 3, 4 e 5, 6 (proveniência), 7 (contagens), 8 (bloco à GCB); em cada item, as linhas Folha, Ponto de julgamento, Formato, Tipo de base, Base, Mecanismo, Troca, Difere de, Alteração na v2 e Marcas; nos pares, a coluna Código e a coluna Base de cada lado.')
    W.append(f'- JSON gerado: D4_plataforma.json, SHA-256 {sha(SAIDA_JSON.read_bytes())}; tópicos incorporados de D4_topicos_fonte.json, SHA-256 {sha(TOPICOS.read_bytes()) if TOPICOS.exists() else "ausente"} (escritos à mão).')
    W.append('')
    W.append('## 2. Correspondência bloco de origem → ## / ###')
    W.append('| Origem (D4_v2_1.md, seção 1) | Destino no curso |')
    W.append('|---|---|')
    for m in ctx['mapa']:
        W.append(f"| {m['origem'].replace('|', '/')} | `{m['destino']}` |")
    W.append('')
    W.append('Regras gerais do curso: "- Definição:" → quadro DEFINIÇÃO (em lista, sem linha em branco, quando a definição tem 3 ou mais frases: operação 4; a divisão não corta citação entre aspas; em parágrafo único nos demais casos); quadro BASE LEGAL em lista com os dispositivos que o próprio bloco cita (no título, na definição ou na Base da pegadinha) e, para o referencial oficial, uma linha "Fonte: <órgão>, <publicação>, <ano>, p. <n>" por publicação citada (órgão, título, ano e página da seção 5 do Anexo N, como manda a ordem; artigo revogado não entra no quadro; o quadro é omitido nos blocos sem dispositivo nem publicação — nenhum neste lote); "- Exemplo (Legislativo, hipotético):" → EXEMPLO PARLAMENTAR (o canônico já termina cada exemplo com "O exemplo é hipotético."); "- Pegadinha provável: … [Desfeita por: X]" → PEGADINHA PROVÁVEL com "Base: X". Código de bloco ("C8.0-01 " etc.) removido do título; R-ids saem dos títulos. Títulos `##`: texto do edital em maiúsculas (P1-DA-8, o caput, e P1-DA-9.3 cortados no primeiro ":" por passarem de 90 caracteres). Resumo: seção 2 inteira (item 8 e item 9), uma só cadeia markdown. Pares: seção 3, 24; `a`/`b` = termos do campo "Par" (a = primeiro; b = demais unidos por " × "); `como` = coluna Diferença + " Como a banca troca: " + coluna "Como a banca troca"; a coluna Base de cada lado não entra. Pegadinhas: seção 4, 62, sem número, sem código do bloco e sem marca de versão; os rótulos " — Desfeita por: X" e " — Dispositivo ou trecho que a desfaz: X" viram " Base: X"; `itemEdital` pelo bloco ([C8.0-NN] → P1-DA-8; [C8.n-NN] → P1-DA-8.n; [C9.n-NN] → P1-DA-9.n).')
    W.append('')
    W.append('## 3. Deleções e trocas (cada uma registrada)')
    W.append('Tipos: deleção de marca (v2, R2, QA PENDENTE, leitura externa, Anexo N, códigos de bloco); deleção de frase inteira ou de oração (processo, "[SEM FONTE]", cobertura de itens, cruzamento com item do banco, regra de produção); troca mínima (op. 6: R-id trocado pela identificação da publicação; "lote" → "curso"); troca de rótulo (operação 2).')
    W.append('')
    ERRS = [e for e in LOG if e['motivo'].startswith('errata de forma')]
    por_tipo = Counter(e['tipo'] for e in LOG if not e['motivo'].startswith('errata de forma'))
    W.append('Contagem por tipo (sem as da errata, seção "Errata de forma"): ' + '; '.join(f'{k}: {v}' for k, v in sorted(por_tipo.items())) + '.')
    W.append('')
    W.append('### 3.1 R-ids (códigos do Anexo N) trocados pela identificação da publicação')
    W.append('Regra aplicada: o R-id nunca aparece. Onde o bloco já identificava a publicação (autor e órgão, ou órgão, edição, ano e página), o R-id saiu e a frase foi mantida com o termo mínimo ("o artigo", "o texto", ou o título da publicação à frente do parêntese que já a citava) — itens 3.2 abaixo. Onde o bloco só trazia o código, a remissão foi trocada pela identificação curta da publicação (autor ou título, órgão, ano), tirada da seção 5 do Anexo N, e, nas listas "Base:", com a página; nos quadros BASE LEGAL a linha "Fonte:" traz órgão, publicação, ano e página. Onde a remissão era supérflua e só repetia o código ("(art. 5º, III; R27)"), foi retirada. As trocas mecânicas, por contexto:')
    W.append('')
    saida, grupos = agrupa_log()
    for c, es in grupos.items():
        W.append(f"- [{c}] " + '; '.join(f"`{e['antes']}` → `{e['depois']}`" for e in es) + '.')
    W.append('')
    W.append('### 3.2 Demais deleções e trocas')
    W.append('')
    k = 0
    for e in saida:
        k += 1
        dep = ('→ `' + e['depois'] + '`') if e['depois'] else '→ (nada)'
        W.append(f"{k}. [{e['ctx']}] {e['tipo']}: `{e['antes']}` {dep}. Motivo: {e['motivo']}.")
    W.append('')
    n_cur = sum(1 for e in LOG if e['tipo'] == 'troca de rótulo' and e['ctx'].startswith('curso'))
    n_pg = sum(1 for e in LOG if e['tipo'] == 'troca de rótulo' and e['ctx'].startswith('pegadinha'))
    W.append(f'Trocas de rótulo (operação 2): {n_cur} pegadinhas do curso ("[Desfeita por: X]" → "Base: X") e {n_pg} pegadinhas da lista consolidada (" — Desfeita por: X" e " — Dispositivo ou trecho que a desfaz: X" → " Base: X").')
    W.append('')
    W.append('Decisões de leitura que o orquestrador pode querer revisar (nenhuma altera conteúdo normativo):')
    W.append('- Siglas: NPM, NPG e pós-NPM como no canônico; a sigla ‘NGP’ só aparece onde o canônico a cita para explicá-la (o "(NGP = nova gestão pública (NPM))" das citações literais do Ipea foi mantido).')
    W.append('- Frases e orações marcadas "[SEM FONTE — não afirmar]" saíram com a marca (16 no curso, 3 no resumo; mais as remissões "SEM FONTE b/c/e/g" que apareciam dentro de Bases do curso e da lista de pegadinhas, 6 ao todo, que saíram com a remissão ao Anexo N). Os blocos C8.1-04 e C8.4-05, que no canônico eram quase só ressalva de "o que não se afirma", ficam com o que restava (uma frase de definição cada), o exemplo e a pegadinha; os títulos "o que não se afirma" foram mantidos. A Base de C8.4-05 citava só "Anexo N, seção 5 (SEM FONTE b e g)": passou a citar os dispositivos e a publicação que o próprio bloco cita (art. 2º, II, e a publicação da cadeia de valor das políticas públicas); a de C8.1-04 perdeu só a remissão ao Anexo N.')
    W.append('- Transparência passiva (C8.3-05): saiu o início da definição que falava da "exceção da ficha" e do "Anexo N do D6"; o texto do art. 10, caput, da LAI e a ressalva sobre o rótulo "passiva" ficaram. O art. 10 da LAI não consta do mapa deste lote; por isso o tópico 8.3 não o usa em baseLegal.')
    W.append('- Remissões do tipo "ver 8.x", "ver 9.x", "tratado em 9.1" foram mantidas (são números de tópico do edital, que são os `##` do curso); só as remissões a código de bloco (C8.1-02 etc.) saíram ou viraram o número do tópico (8.1).')
    W.append('- "[REVOGADO]" e "[REVOGADOS]" no curso, nos pares e no resumo foram mantidos: não constam da lista da seção 6 e distinguem artigo revogado de artigo vigente com letra.')
    W.append('- Palavra "isca" em justificativas (D4-37, D4-51, D4-60, D4-71): mantida; só "elemento-isca" consta da lista da seção 6 e não ocorre nas justificativas deste lote.')
    W.append('- Enunciados: o canônico não separa texto-base nem traz comando por item (a seção 5.1 traz "Julgue cada item como Certo ou Errado."): `textoBase` "" e `comando` "Julgue o item a seguir.", como no D5.')
    W.append('- Ordem dos itens no JSON: crescente pelo id (D4-01 a D4-79); no canônico os itens do caput (D4-74 a D4-79) vêm por último, como os ids já indicam.')
    W.append('- Falso positivo do validador: nenhum. Observação sobre o validador (não alterado): o padrão `\\bR[12]\\b` só pega R1 e R2; os demais R-ids (R3 a R31) são conferidos por este script e pelo de fidelidade (nenhum R-id restou em curso, resumo, pares, pegadinhas, justificativas ou tópicos).')
    W.append('')
    W.append('## 4. Itens')
    W.append(f'- Total {len(it)}; C {n_c} / E {n_e}.')
    W.append('- Por itemEdital: ' + '; '.join(f'{k}: {v}' for k, v in sorted(por_folha.items(), key=lambda kv: kv[0])) + '.')
    W.append('- volatil true: ' + (', '.join(vol) if vol else 'nenhum (todas as linhas "Marcas:" trazem REVERIFICAR=não e VOLÁTIL=não)') + '.')
    W.append('- Justificativa: linhas 1 e 2 unidas por um espaço; as edições são as da seção 3 (R-ids; D4-36, D4-48 e D4-67). As linhas "Difere de" e "Mecanismo" são campos à parte no canônico e não entram. Enunciado e gabarito: iguais caractere a caractere.')
    W.append(f"- Pares: {len(dados['lote']['pares'])}; pegadinhas: {len(dados['lote']['pegadinhas'])} (" + '; '.join(f'{k}: {v}' for k, v in sorted(por_peg.items())) + f"); tópicos: {len(dados['topicos'])} ({', '.join(dados['topicos'])}).")
    W.append('')
    W.append('### 4.1 Tópicos (escritos à mão em D4_topicos_fonte.json; um por "##")')
    for k, t in dados['topicos'].items():
        tipos = '; '.join(f"{v['tipo']} ({v['titulo']})" for v in t['visuais'])
        W.append(f"- {k}: emUmMinuto 3 frases; resumo {len(t['resumo'].split())} palavras; visuais: {tipos}.")
    W.append('- Visuais pedidos na ordem e como ficaram: compare governança × governabilidade em 9.1, nova gestão pública (NPM) × Nova Governança Pública (NPG) em 8.1, termo de colaboração × termo de fomento em 8.2 e transparência ativa × passiva em 8.3 (com o acordo de cooperação na legenda de 8.2); esquema dos mecanismos liderança, estratégia e controle em 9.2; baseLegal com o Decreto 9.203/2017 em 8.3 (com a LAI), 8.4, 9.1, 9.2, 9.3 e 9.4, e com a Lei 11.079/2004 em 8.2; fluxo (elos da cadeia de valor das políticas públicas) em 8.4 e tabela (princípios, diretrizes e mecanismos) em 9.4, onde o pedido não indicava visual.')
    W.append('- Linha em 8 (patrimonialismo → burocracia → anos 80): só com os três marcos que o curso dá (monarquias absolutas; em substituição à patrimonialista; anos 80, países centrais). A NPG ficou fora da linha de propósito: o curso (8.1, "Evolução da NPG: o que não se afirma") não data a NPG nem afirma que ela substitui a NPM; ela aparece no compare de 8.1 e no esquema de 8.1.')
    W.append('- baseLegal: texto copiado da coluna de texto do mapa por script de busca do rótulo do dispositivo (letra a letra; `literal: true`; `conferido: 2026-10-20`, a data da coluna Consulta). Em 8.4, o art. 2º, II, entra só na parte inicial que o curso cita ("valor público - produtos e resultados gerados, preservados ou entregues pelas atividades de uma organização"), trecho copiado letra a letra da mesma linha do mapa; a continuação é da folha 9.3. Nenhum dispositivo revogado (arts. 7º a 15 e 20 do Decreto 9.203 sem letra): 9.4 usa os arts. 8º-B, caput, 10-B, II e III, e 12-A, caput; o art. 11-A, caput, ficou de fora porque cita órgão que o curso não afirma existir. Em 8.3 não há o art. 10 da LAI, que não consta do mapa; o compare traz a transparência passiva com o que o curso diz do art. 10, caput. O referencial oficial (TCU, Casa Civil, Ipea, ENAP, CGU) não entra em baseLegal, só nos quadros BASE LEGAL do curso.')
    W.append('- Arquivos dos tópicos: D4_topicos_fonte.json é gravado por scripts/gerar_topicos_D4.py (os textos estão nele, escritos à mão; o script só busca no mapa o texto de cada dispositivo de baseLegal); o formatador lê o JSON pronto e confere que as chaves são as dos blocos ##.\n- Texto dos tópicos: cada frase vem do curso da própria folha; a conferência de fidelidade checa que todo número do tópico existe no curso da folha, que todo artigo de baseLegal é citado no curso da folha, a data da consulta e a ausência de artigo revogado.')
    W.append('')
    W.append('## 5. Saída do validador')
    W.append('Comando: `python3 -I saida/gcb/DA_plataforma/scripts/validar_da.py saida/gcb/DA_plataforma/D4_plataforma.json saida/gcb/D4_v2_1.md saida/gcb/D4_anexo_N_mapa_normativo.md`')
    W.append('```')
    W.append(val)
    W.append('```')
    W.append('')
    W.append('## 6. Conferência de fidelidade')
    W.append('Comando: `python3 -I saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D4.py`')
    W.append('')
    W.append(fid)
    W.append('')
    W.append('## Errata de forma — QA final 20/10/2026')
    W.append('Origem: QA final do pacote v1.13 (gbq-cqe, 20/10/2026), achados 1, 6 e 7. Achado 1: a palavra de produção "folha" no texto exibido (a candidata não conhece "folha"; o validador passou a acusá-la). Regra da ordem: frase que só fala do processo ou da organização da produção é DELETADA; remissão útil ao estudo vira "subitem". Achado 6: o resumo do tópico P1-DA-8.4 deve usar só o curso de 8.4. Achado 7: repetição da identificação da publicação criada pela troca dos R-códigos em D4-62, D4-75 e D4-78, e parênteses duplos em D4-38. Só forma: nenhum enunciado, gabarito, itemEdital ou id foi tocado.')
    W.append('')
    W.append('### Achados 1 e 7: curso, resumo do lote e justificativas (edições no formatador; conferidas pela conferência de fidelidade)')
    for i, e in enumerate(ERRS, 1):
        dep = ('→ `' + e['depois'] + '`') if e['depois'] else '→ (nada)'
        W.append(f"{i}. [{e['ctx']}] {e['tipo']}: `{e['antes']}` {dep}. Motivo: {e['motivo']}.")
    W.append('')
    W.append('### Achados 1 e 6: tópicos (edições em D4_topicos_fonte.json, gerado por scripts/gerar_topicos_D4.py)')
    W.append('1. [topicos P1-DA-8.2 resumo] troca mínima: `é de outra folha` → `é do subitem 8.4`. Motivo: achado 1: "folha" é termo de produção; a remissão serve ao estudo e passa a "subitem" (o curso de 8.2 traz agora "a finalidade (valor público) é do subitem 8.4").')
    W.append('2. [topicos P1-DA-8.4 resumo] deleção de frase inteira: `A continuação do inciso, sobre as respostas efetivas e úteis às necessidades ou às demandas de interesse público, é tratada em 9.3.` → (nada). Motivo: achado 6: a frase traz conteúdo do curso de 9.3 ("respostas efetivas e úteis…") que não está no curso de 8.4, e a remissão "é tratada em 9.3" (o FORMATO, seção 5, pede só o curso do próprio tópico).')
    W.append('3. [topicos P1-DA-8.4 resumo] deleção de oração: `; o meio, a integração entre níveis e esferas, é tratado em 8.2` → (nada; o período termina em "…gerar, preservar e entregar valor público."). Motivo: achado 6: remissão "é tratado em 8.2" e conteúdo do tópico 8.2.')
    W.append(f'Resultado do 8.4: resumo com {len(dados["topicos"]["P1-DA-8.4"]["resumo"].split())} palavras (faixa 150–250), só com frases do curso de 8.4, sem remissão a outro tópico e sem fato novo (a conferência de tópicos confere números e artigos contra o curso do tópico).')
    W.append('')
    W.append('Nota de formato (C9.4-03): com a deleção de "Distribuição por folha…" a definição do bloco fica com 2 frases e, pela regra geral do curso (lista só a partir de 3 frases, operação 4), passa de lista de 3 itens a parágrafo único; nenhuma palavra muda além da deleção.')
    W.append('')
    W.append(f'Total: {len(ERRS)} mudanças no curso/resumo do lote/justificativas + 3 nos tópicos = {len(ERRS) + 3} no D4.')
    W.append('')
    REGISTRO.write_text('\n'.join(W) + '\n', encoding='utf-8')
    print(val)
    print(fid.splitlines()[-1] if fid else '(sem saída)')
    return rc_val, rc_fid

def main():
    dados, ctx = monta()
    grava(dados)
    print('gravado', SAIDA_JSON, sha(SAIDA_JSON.read_bytes()))
    if '--registro' in sys.argv:
        rc_val, rc_fid = registro(dados, ctx)
        sys.exit(0 if rc_val == 0 and rc_fid == 0 else 1)

if __name__ == '__main__':
    main()
