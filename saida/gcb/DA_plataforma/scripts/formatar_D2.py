# formatar_D2.py — T-75 (ordem DA 20/10/2026) — 2026-10-20 — gerado por gcb-cpp
# Reformata o canônico saida/gcb/D2_v2_1.md para o formato da plataforma (FORMATO_PLATAFORMA_DA.md).
# Só reformatação: nenhum conteúdo novo. Toda deleção e troca de palavra é registrada (LOG), gravada em
# D2_log_edicoes.json (lido pela conferência de fidelidade) e levada ao registro.
# Determinístico. Os tópicos são escritos à mão em D2_topicos_fonte.json e incorporados aqui.
# Uso:  python3 -I saida/gcb/DA_plataforma/scripts/formatar_D2.py              -> grava D2_plataforma.json (+ log)
#       python3 -I saida/gcb/DA_plataforma/scripts/formatar_D2.py --registro   -> regrava o JSON, roda o validador e a
#                                                                                conferência de fidelidade e grava D2_registro_formato.md
import hashlib, json, pathlib, re, subprocess, sys
from collections import Counter

RAIZ = pathlib.Path(__file__).resolve().parents[4]
DA = RAIZ / 'saida/gcb/DA_plataforma'
CANON = RAIZ / 'saida/gcb/D2_v2_1.md'
MAPA = RAIZ / 'saida/gcb/D2_anexo_N_mapa_normativo.md'
SHA_CANON = '59cffaa689ea869cd11c13e6a833470b0b91d24b0f25ea2cc2e100ac9be8bd2c'
URL_CANON = 'saida/gcb/D2_v2_1.md'
SAIDA_JSON = DA / 'D2_plataforma.json'
LOG_JSON = DA / 'D2_log_edicoes.json'
TOPICOS = DA / 'D2_topicos_fonte.json'
REGISTRO = DA / 'D2_registro_formato.md'
VALIDADOR = DA / 'scripts/validar_da.py'
CONFERE = DA / 'scripts/conferir_fidelidade_D2.py'

NOME = 'Direito Administrativo — Agentes públicos e direito administrativo disciplinar (itens 3 e 4 do edital)'
FOLHAS = ['3.1', '3.2', '3.3', '3.4', '4.1', '4.2', '4.3', '4.4']

def sha(b): return hashlib.sha256(b).hexdigest()

def ler_canon():
    raw = CANON.read_bytes()
    if sha(raw) != SHA_CANON:
        print('PARAR: SHA-256 de saida/gcb/D2_v2_1.md diverge:', sha(raw), '!=', SHA_CANON); sys.exit(2)
    return raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n').split('\n')

EDITAL = {e['id']: e['texto'] for e in json.loads((DA / 'edital_DA.json').read_text(encoding='utf-8'))}

def achar(L, prefixo, ini=0):
    for i in range(ini, len(L)):
        if L[i].startswith(prefixo): return i
    raise SystemExit('PARAR: seção não encontrada: ' + prefixo)

# ---------------------------------------------------------------- registro de edições
LOG = []   # {ctx, tipo, antes, depois, adicionado, motivo}
def log(ctx, tipo, antes, depois, motivo, adicionado=''):
    LOG.append(dict(ctx=ctx, tipo=tipo, antes=antes, depois=depois, adicionado=adicionado, motivo=motivo))

def edita(ctx, txt, antigo, novo, tipo, motivo, adicionado=''):
    assert txt.count(antigo) == 1, (ctx, antigo[:80], txt.count(antigo))
    log(ctx, tipo, antigo.strip(), novo.strip(), motivo, adicionado)
    return txt.replace(antigo, novo)

D_MARCA = 'deleção de marca'
D_FRASE = 'deleção de frase inteira'
D_ORACAO = 'deleção de oração de processo'
TROCA = 'troca mínima (op. 6)'
M_ANEXO = 'referência ao Anexo N e à indicação de núcleo/complementar do mapa normativo (nota de produção; seção 6)'
M_SEMFONTE = '"[SEM FONTE — não afirmar]": a marca e a frase marcada saem (seção 6)'
M_LOTE = 'fala do lote/da produção (cobertura de itens, remissão a outro lote ou ao lote); não é conteúdo para a candidata (seção 6)'
M_COD = 'remissão a código de bloco, de par ou de pegadinha do curso (seção 6)'
M_REV = 'marca REVERIFICAR (seção 6)'
E_ACH1 = 'errata de forma (QA final 20/10/2026, achado 1): '
E_SUB = E_ACH1 + '"folha" é termo de produção (seção 6); a remissão serve ao estudo e passa a "subitem", o número 3.4 é o do `##` do curso'
M_NUC = 'indicação de "núcleo"/"complementar" do mapa normativo (nota de produção; seção 6)'

# edições explícitas no curso: (bloco, campo) -> [(antigo, novo, tipo, motivo[, adicionado])]; 'def' = definição; 'ex' = exemplo; 'solto' = linha única do caput 3
A_N = lambda txt: (txt, '', D_FRASE, M_ANEXO)
EXPL = {
 ('C3.0-01', 'solto'): [
  (', sem texto próprio no Anexo N', '', D_ORACAO, 'cita o Anexo N (seção 6); fica "são rótulos de curso; o conteúdo normativo está na CF…"'),
  (' Sobre classificação doutrinária: [SEM FONTE — não afirmar]; nenhum item a julga.', '', D_FRASE, M_SEMFONTE),
  ('O caput 3 não é folha. Todo conteúdo cobrável está nas folhas 3.1 a 3.4. ', '', D_FRASE, E_ACH1 + 'as duas frases só falam da organização da produção (o que é "folha" e onde está o conteúdo cobrável); nada de estudo se perde'),
 ],
 ('C3.1-02', 'def'): [
  ('Nota REVERIFICAR: a alínea b', 'Nota: a alínea b', D_MARCA, M_REV + '; o conteúdo da nota (redação da EC 138/2025 vigente; redação anterior superada) é mantido'),
  ('(contraste, folha 3.4)', '(contraste, subitem 3.4)', TROCA, E_SUB, 'subitem'),
 ],
 ('C3.1-08', 'def'): [
  ('arts. 28 a 32 (folha 3.4)', 'arts. 28 a 32 (subitem 3.4)', TROCA, E_SUB, 'subitem'),
 ],
 ('C3.1-05', 'def'): [
  (' Nenhum item deste lote julga o art. 40, § 4º, ou o § 5º-A.', '', D_FRASE, M_LOTE),
 ],
 ('C3.1-06', 'def'): [
  ('ver C3.4-03, que traz', 'ver o item 3.4, que traz', TROCA, 'o código de bloco C3.4-03 é referência de produção (seção 6); trocado por "o item 3.4" (o curso do item 3.4 traz os três textos; como no exemplo "(subitem 1.0)" → "do item 1" da seção 7, op. 6)', 'o item 3 4'),
 ],
 ('C3.1-09', 'def'): [
  (' Anexo N: art. 37, VI a VIII, núcleo 3.1; art. 5º, § 2º, núcleo 3.4 e 3.2.', '', D_FRASE, M_ANEXO),
  (' O inciso VII é citado só pela letra: o conteúdo da lei específica não foi aberto neste material ([SEM FONTE — não afirmar]).', '', D_FRASE, M_SEMFONTE),
 ],
 ('C3.1-10', 'def'): [
  (' Anexo N: art. 37, XI e §§ 10 a 13, núcleo 3.1; §§ 9º e 14, complementar 3.1.', '', D_FRASE, M_ANEXO),
 ],
 ('C3.1-11', 'def'): [
  (' (o texto desses incisos do art. 7º não foi aberto neste material: [SEM FONTE — não afirmar])', '', D_ORACAO, M_SEMFONTE + '; fica "…XXII e XXX, podendo a lei estabelecer requisitos diferenciados…"'),
  ('(subsídio, já em C3.1-03)', '(subsídio)', D_ORACAO, M_COD),
  (' O caput do art. 39 segue como em C3.1-03 (remissão a ação no STF; efeito não conferido).', '', D_FRASE, M_COD + '; a frase só remete a outro bloco (a nota sobre a remissão a ação no STF está no bloco da remuneração, subsídio e teto)'),
  (' Anexo N: §§ 1º, I a III, e 3º, núcleo 3.1 e complementar 3.2; demais, núcleo 3.1.', '', D_FRASE, M_ANEXO),
 ],
 ('C3.1-12', 'def'): [
  ('Nota (REVERIFICAR, EC 140/2026)', 'Nota (EC 140/2026)', D_MARCA, M_REV),
  ('; ver C3.1-05 (redação posterior ao edital', ' (redação posterior ao edital', D_ORACAO, M_COD + '; fica "…não são tratados neste bloco (redação posterior ao edital, registrada e não incorporada)."'),
  (' Anexo N: todos os dispositivos citados, núcleo 3.1.', '', D_FRASE, M_ANEXO),
 ],
 ('C3.2-02', 'def'): [
  (' (ver C3.2-07)', '', D_MARCA, M_COD),
 ],
 ('C3.2-04', 'def'): [
  (' A Lei 8.745/1993, que regula a contratação temporária, não consta do Anexo N: [SEM FONTE — não afirmar].', '', D_FRASE, M_SEMFONTE + '; a frase também cita o Anexo N'),
 ],
 ('C3.2-07', 'def'): [
  (' (Anexo N, seção 3)', '', D_MARCA, M_ANEXO),
  (' A classificação de agentes públicos (agentes políticos, honoríficos e outros) é rótulo doutrinário, sem texto próprio no Anexo N: [SEM FONTE — não afirmar]; nenhum item a julga.', '', D_FRASE, M_SEMFONTE + '; a frase também cita o Anexo N'),
 ],
 ('C3.3-01', 'def'): [
  (' O Anexo N não traz norma que aplique o Decreto 10.835 à Câmara dos Deputados: [SEM FONTE — não afirmar].', '', D_FRASE, M_SEMFONTE + '; a frase também cita o Anexo N'),
 ],
 ('C3.3-02', 'def'): [
  (' O Anexo N localizou prerrogativa expressa de requisitar só na Lei 9.007/1995 (Presidência da República) e na Lei 6.999/1982 (Justiça Eleitoral); sobre qualquer outro órgão requisitante: [SEM FONTE — não afirmar].', '', D_FRASE, M_SEMFONTE + '; a frase é relato da busca do Anexo N e termina na marca'),
 ],
 ('C3.3-08', 'def'): [
  ('Decreto 12.374/2025 (REVERIFICAR; norma de 2025, vigente)', 'Decreto 12.374/2025 (norma de 2025, vigente)', D_MARCA, M_REV),
  (' Que o Decreto 12.374 se aplique à Câmara dos Deputados: [SEM FONTE — não afirmar].', '', D_FRASE, M_SEMFONTE),
 ],
 ('C3.3-10', 'def'): [
  ('ônus do ressarcimento (núcleo 3.3). Art. 17', 'ônus do ressarcimento. Art. 17', D_MARCA, M_NUC),
  ('Constituição (complementar 3.3). Art. 18', 'Constituição. Art. 18', D_MARCA, M_NUC),
  (' (os incisos VI e VII não foram usados)', '', D_ORACAO, M_LOTE + ' (cobertura de incisos)'),
  ('Art. 30-A, parágrafo único (núcleo 3.3): nas', 'Art. 30-A, parágrafo único: nas', D_MARCA, M_NUC),
  (' (art. 30-A, caput, I a III, em C3.3-04)', ' (art. 30-A, caput, I a III)', D_MARCA, M_COD),
  (' O parágrafo único do art. 22 e o art. 23 remetem ao ato conjunto do art. 32, não aberto: [SEM FONTE — não afirmar].', '', D_FRASE, M_SEMFONTE),
  (' Anexo N: arts. 17 a 25, complementar 3.3.', '', D_FRASE, M_ANEXO),
 ],
 ('C3.3-11', 'def'): [
  (' Anexo N: todos os dispositivos citados, núcleo 3.3.', '', D_FRASE, M_ANEXO),
  (' A Lei 6.999 traz a prerrogativa expressa de requisitar da Justiça Eleitoral; sobre a Câmara dos Deputados: [SEM FONTE — não afirmar].', '', D_FRASE, M_SEMFONTE),
 ],
 ('C3.4-03', 'def'): [
  ('Decreto 12.374/2025 (REVERIFICAR), art. 2º, caput', 'Decreto 12.374/2025, art. 2º, caput', D_MARCA, M_REV),
  (' A conciliação entre esses textos é matéria de doutrina e jurisprudência não aberta neste material — [SEM FONTE — não afirmar].', '', D_FRASE, M_SEMFONTE + '; ficam os três textos, cada um no seu referencial, sem conciliação'),
 ],
 ('C3.4-05', 'def'): [
  (' (ponto bloqueado do BQ-0150; só curso)', '', D_ORACAO, M_LOTE + '; cita item do banco (BQ-0150)'),
 ],
 ('C3.4-06', 'def'): [
  (' (parte B deste lote)', '', D_ORACAO, M_LOTE + '; fica "é penalidade; aqui, só como causa de vacância (art. 33, II)."'),
 ],
 ('C3.4-08', 'def'): [
  (' (ponto bloqueado do BQ-0126; só curso)', '', D_ORACAO, M_LOTE + '; cita item do banco (BQ-0126)'),
 ],
 ('C3.4-11', 'def'): [
  (' Os arts. 186 a 231 não foram usados em item.', '', D_FRASE, M_LOTE + ' (cobertura de itens)'),
 ],
 ('C3.4-12', 'def'): [
  ('por opção de remuneração; C3.2-03 e P-18)', 'por opção de remuneração)', D_ORACAO, M_COD),
  (' Anexo N: todos os dispositivos citados, núcleo 3.4.', '', D_FRASE, M_ANEXO),
 ],
 ('C3.4-13', 'def'): [
  (' (já em C3.4-03)', '', D_MARCA, M_COD),
  (' O prazo do estágio (24 meses na lei; 36 no decreto remetido) segue o tratamento de C3.4-03, sem afirmação nova.', '', D_FRASE, M_COD + '; a frase só remete ao bloco do estágio probatório'),
  (' Anexo N: todos os dispositivos citados, núcleo 3.4 (art. 20, §§ 4º e 5º, também complementar 3.2).', '', D_FRASE, M_ANEXO),
 ],
 ('C3.4-14', 'def'): [
  (' O caput do art. 76-A traz remissões a regulamento e a decreto, não abertos: [SEM FONTE — não afirmar] sobre limites e valores.', '', D_FRASE, M_SEMFONTE),
  (' Anexo N: todos os dispositivos citados, núcleo 3.4.', '', D_FRASE, M_ANEXO),
 ],
 ('C3.4-15', 'def'): [
  (' Os arts. 77, 78 e 80 trazem remissão a lei de 1997, não aberta: [SEM FONTE — não afirmar] sobre o seu conteúdo.', '', D_FRASE, M_SEMFONTE),
  (' Anexo N: todos os dispositivos citados, núcleo 3.4.', '', D_FRASE, M_ANEXO),
 ],
 ('C3.4-16', 'def'): [
  (' (o caput traz remissão a decreto, não aberto: [SEM FONTE — não afirmar])', '', D_ORACAO, M_SEMFONTE),
  (' Anexo N: todos os dispositivos citados, núcleo 3.4.', '', D_FRASE, M_ANEXO),
 ],
 ('C3.4-17', 'def'): [
  ('(IV; o inciso traz remissão a decreto, não aberto: [SEM FONTE — não afirmar])', '(IV)', D_ORACAO, M_SEMFONTE + '; fica o número do inciso'),
  (' O art. 103 tem, no Anexo N, só os §§ 1º a 3º.', '', D_FRASE, M_ANEXO),
  (' Anexo N: todos os dispositivos citados, núcleo 3.4.', '', D_FRASE, M_ANEXO),
 ],
 ('C3.4-18', 'def'): [
  (' Complementa C3.4-09 (arts. 106 a 110).', '', D_FRASE, M_COD),
  (' Contraste: a prescrição da ação disciplinar (art. 142) está em C4.2-13; o recurso da Lei 9.784 (arts. 56 a 64), em C4.4-14 (par P-63).', '', D_FRASE, M_COD + '; a frase só remete a outros blocos e a um par'),
  (' Anexo N: todos os dispositivos citados, núcleo 3.4.', '', D_FRASE, M_ANEXO),
 ],
 ('C3.4-19', 'def'): [
  ('; a remissão do caput ao Decreto 6.690/2008 não foi aberta: [SEM FONTE — não afirmar] sobre o conteúdo do decreto', '', D_ORACAO, M_SEMFONTE),
  (' Ficam fora deste bloco os arts. 215 e 217 (pensão por morte): o art. 215 remete à Lei 10.887/2004, não aberta ([SEM FONTE — não afirmar]), e o art. 217, cujo texto está no Anexo N, fica fora por escolha de escopo.', '', D_FRASE, M_SEMFONTE + '; a frase também cita o Anexo N e trata de escopo de produção'),
  (' O bloco é só de curso (sem item) e complementa o bloco C3.4-11 (arts. 183 a 185).', '', D_FRASE, M_LOTE + ' ("sem item") e ' + M_COD),
  (' Anexo N: todos os dispositivos citados, núcleo 3.4.', '', D_FRASE, M_ANEXO),
 ],
 ('C4.1-01', 'def'): [
  ('; a classificação doutrinária das fontes é matéria não aberta neste material — [SEM FONTE — não afirmar]', '', D_ORACAO, M_SEMFONTE),
  (' O conteúdo normativo da folha está nos artigos dos blocos C4.1-01 a C4.1-10.', '', D_FRASE, M_COD),
 ],
 ('C4.1-04', 'def'): [
  (' O conteúdo de cada responsabilidade (arts. 122 a 124) está no bloco C4.2-04.', '', D_FRASE, M_COD),
 ],
 ('C4.1-05', 'def'): [
  ('; o efeito de outras formas de absolvição não é tratado neste material — [SEM FONTE — não afirmar]', '', D_ORACAO, M_SEMFONTE + '; fica "O artigo trata só desse tipo de absolvição."'),
 ],
 ('C4.1-06', 'def'): [
  (' Os incisos I, II, III, V e XIII são pontos do D1, e o inciso XII é ponto do item real BQ-0145; nenhum deles é ponto de item desta folha.', '', D_FRASE, M_LOTE + '; cita o lote D1 e item do banco (BQ-0145)'),
 ],
 ('C4.1-08', 'def'): [
  ('; o fundamento constitucional do contraditório e da ampla defesa no art. 5º, LV, da CF não foi aberto neste material — [SEM FONTE — não afirmar]', '', D_ORACAO, M_SEMFONTE + '; fica "A ampla defesa e o contraditório constam do rol."'),
 ],
 ('C4.1-10', 'def'): [
  (' Nesta folha vale só a proposição da fonte: o dever funcional pode estar previsto em lei, regulamentação ou norma interna.', '', D_FRASE, E_ACH1 + 'a frase só delimita o recorte da produção ("nesta folha vale só a proposição da fonte") e repete o que a frase anterior (art. 129, caput) e o título do bloco já dizem'),
  (' A forma escrita e as proibições do art. 117 estão no bloco C4.2-06.', '', D_FRASE, M_COD),
 ],
 ('C4.2-01', 'def'): [
  (', e a doutrina sobre o conceito não foi aberta neste material — [SEM FONTE — não afirmar]', '', D_ORACAO, M_SEMFONTE + '; fica "…traz os tipos, e não um artigo de definição."'),
 ],
 ('C4.2-04', 'def'): [
  (' A responsabilidade civil do Estado é matéria de outro lote.', '', D_FRASE, M_LOTE),
 ],
 ('C4.2-06', 'def'): [
  (' (a fonte do dever está no bloco C4.1-10)', '', D_ORACAO, M_COD),
 ],
 ('C4.2-10', 'def'): [
  (' (bloco C4.3-13)', '', D_MARCA, M_COD),
 ],
 ('C4.3-14', 'def'): [
  (' (o caput está em C4.3-08)', '', D_ORACAO, M_COD),
  (' Anexo N: todos os dispositivos citados, núcleo 3.4 e 4.3.', '', D_FRASE, M_ANEXO),
 ],
 ('C4.3-15', 'def'): [
  (' Os §§ 3º e 4º ficam fora deste bloco (já estão em C4.3-10).', '', D_FRASE, M_COD),
  (' Anexo N: art. 167, caput e §§ 1º e 2º, núcleo 3.4 e 4.3.', '', D_FRASE, M_ANEXO),
 ],
 ('C4.3-16', 'def'): [
  ('a penalidade de demissão e a de destituição são as tratadas em C4.2-09 e C4.2-11; ', '', D_ORACAO, M_COD + '; fica "(a cassação de aposentadoria ou disponibilidade, que o texto do § 6º também cita, é a do art. 127, IV, …)"'),
  (' e que este lote não usa)', ')', D_ORACAO, M_LOTE),
  (' (C4.3-13)', '', D_MARCA, M_COD),
  (' Anexo N: art. 133, §§ 5º e 6º, núcleo 3.4, 4.2 e 4.3.', '', D_FRASE, M_ANEXO),
 ],
 ('C4.4-01', 'def'): [
  (' O § 1º e o § 2º, I e II, também são cobrados em outro lote.', '', D_FRASE, M_LOTE),
 ],
 ('C4.4-05', 'def'): [
  (' Os demais dispositivos da delegação e da avocação (arts. 11, 12, 13, II, 14, §§ 2º e 3º, e 15) são tratados em outro lote.', '', D_FRASE, M_LOTE),
 ],
 ('C4.4-13', 'def'): [
  (' O caput do art. 54 e os arts. 53 e 55 (anulação, revogação, decadência de cinco anos e convalidação) são tratados em outro lote.', '', D_FRASE, M_LOTE),
 ],
 ('C4.4-14', 'def'): [
  (' Ficam fora do recorte desta folha o art. 56, § 3º, e os arts. 64-A e 64-B (súmula vinculante).', '', D_FRASE, M_LOTE + ' (recorte de cobertura)'),
 ],
 ('C4.4-18', 'def'): [
  (' Anexo N: arts. 31 a 35, núcleo 4.4.', '', D_FRASE, M_ANEXO),
 ],
 ('C4.4-19', 'def'): [
  ('Art. 36 (já em C4.4-09): cabe', 'Art. 36: cabe', D_MARCA, M_COD),
  ('Art. 45 (já em C4.4-09): em caso', 'Art. 45: em caso', D_MARCA, M_COD),
  (' O art. 42 (parecer) é ponto do D1 e não é tratado aqui.', '', D_FRASE, M_LOTE + '; cita o lote D1'),
  (' Anexo N: todos os dispositivos citados, núcleo 4.4.', '', D_FRASE, M_ANEXO),
 ],
 ('C4.4-20', 'def'): [
  (' Complementa C4.4-11.', '', D_FRASE, M_COD),
  (' Anexo N: todos os dispositivos citados, núcleo 4.4.', '', D_FRASE, M_ANEXO),
 ],
 ('C4.4-20', 'ex'): [
  ('(art. 49-A, § 6º, III; C4.4-11)', '(art. 49-A, § 6º, III)', D_MARCA, M_COD),
 ],
 ('C4.4-21', 'def'): [
  (' (tratado em outro lote)', '', D_ORACAO, M_LOTE),
  (' Complementa C4.4-14 (que traz o caput do art. 63).', '', D_FRASE, M_COD),
  (' Anexo N: art. 63, núcleo 4.4.', '', D_FRASE, M_ANEXO),
 ],
}

# dispositivos de BASE LEGAL quando o título do bloco não os traz com a norma (só o que o próprio bloco cita)
BASE_OVERRIDE = {
 'C4.1-10': ['Lei 8.112, art. 129, caput'],
 'C4.2-06': ['Lei 8.112, art. 129, caput'],
 'C4.4-17': ['Lei 9.784/1999, art. 68', 'Lei 9.784/1999, art. 69-A'],
}

RX_SUFIXO = re.compile(r' — acréscimo da v2 \(leitura externa [^()]*; QA PENDENTE \(R2\)\)$')
RX_PROIBIDO_LOCAL = re.compile(r'Anexo|BASE DOUTRIN|SEM FONTE|REVERIFICAR|BQ-|\bC\d\.\d-\d\d|\b[GP]-\d\d|QA PENDENTE|\bv2\b|\bR[12]\b|\blotes?\b|núcleo|complementar 3|\bD[1-6]\b|NÃO CONFERID|ponto bloqueado|leitura externa|acréscimo')

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
        partes.append(antes); ini = m.end()
    partes.append(txt[ini:])
    return [p.strip() for p in partes if p.strip()]

PROC_LINHAS = []   # linhas de processo do curso que não entram (registradas)

def parse_curso(L):
    ini = achar(L, '## 1. (a) CURSO'); fim = achar(L, '## 2. (b) RESUMO', ini)
    partes, bloco = [], None
    for l in L[ini + 1:fim]:
        if l.strip() in ('', '---'): continue
        if l.startswith('Cada bloco:'):
            PROC_LINHAS.append(l); continue   # parágrafo de convenções de produção (duas ocorrências)
        m = re.match(r'^### Caput 3 — (.+)$', l)
        if m:
            partes.append(dict(cod='3', caput=True, titulo_origem=l[4:], blocos=[])); bloco = None; continue
        m = re.match(r'^### Folha (\d\.\d) — (.+)$', l)
        if m:
            partes.append(dict(cod=m.group(1), caput=False, titulo_origem=l[4:], blocos=[])); bloco = None; continue
        m = re.match(r'^\*\*(C\d\.\d-\d\d) (.+?)\*\*(.*)$', l)
        if m and partes:
            bloco = dict(cod=m.group(1), titulo=m.group(2), sufixo=m.group(3), linhas=[l], campos={})
            partes[-1]['blocos'].append(bloco); continue
        if bloco is not None and l.startswith('- '):
            bloco['linhas'].append(l)
            for chave, pref in (('def', '- Definição: '), ('ex', '- Exemplo (Legislativo, hipotético): '), ('peg', '- Pegadinha provável: ')):
                if l.startswith(pref): bloco['campos'][chave] = l[len(pref):]; break
            else:
                if partes[-1]['caput'] and 'solto' not in bloco['campos']: bloco['campos']['solto'] = l[2:]
                else: raise SystemExit('PARAR: linha inesperada no curso: ' + l[:80])
        else:
            raise SystemExit('PARAR: linha inesperada no curso: ' + l[:80])
    for p in partes:
        for b in p['blocos']:
            if p['caput']: assert set(b['campos']) == {'solto'}, b['cod']
            else:
                assert set(b['campos']) == {'def', 'ex', 'peg'}, b['cod']
                assert b['cod'].startswith('C' + p['cod'] + '-'), (b['cod'], p['cod'])
    return partes

NORMAS_INI = ('CF,', 'Lei ', 'Decreto ')
def split_disp(s):
    """'CF, art. 37, III; art. 38' -> ['CF, art. 37, III', 'CF, art. 38']; 'art. N' sem norma herda a anterior."""
    itens, norma = [], None
    for parte in [x.strip() for x in s.split('; ') if x.strip()]:
        m = re.match(r'^(CF|Lei [\d.]+(?:/\d{4})?|Decreto [\d.]+/\d{4}), (arts?\. .*)$', parte)
        if m: norma = m.group(1); itens.append(parte)
        elif re.match(r'^arts?\. ', parte) and norma: itens.append(norma + ', ' + parte)
        else: return None
    return itens

def base_legal(cod, titulo, peg_base):
    if cod in BASE_OVERRIDE: return BASE_OVERRIDE[cod]
    for p in re.findall(r'\(([^()]*)\)', titulo):
        if p.startswith(NORMAS_INI) and 'art' in p:
            it = split_disp(p)
            if it: return it
    b = re.sub(r'\s*\([^()]*\)', '', peg_base).rstrip('.')
    it = split_disp(b)
    assert it, (cod, peg_base)
    return it

def monta_curso(partes):
    out, mapa, caput_blocos = [], [], []
    for p in partes:
        if p['caput']:
            caput_blocos = list(p['blocos']); continue
        eid = 'P1-DA-' + p['cod']
        cab = f"## {p['cod']} {titulo_edital(eid)}"
        out += [cab, '']
        mapa.append(dict(origem=p['titulo_origem'], destino=cab))
        blocos = (caput_blocos if caput_blocos else []) + p['blocos']
        caput_blocos = []
        for b in blocos:
            ctx = 'curso ' + b['cod']
            tit = b['titulo']
            suf = b['sufixo']
            if b['cod'] == 'C3.0-01':
                novo = 'Caput 3 — Agentes públicos'
                log(ctx + ' (título)', D_ORACAO, tit[len(novo):].strip(), '', 'nota de produção no título ("curso curto; sem item, sem par e sem pegadinha próprios"; seção 6)')
                tit = novo
                s = b['campos']['solto']
                for ant, nov, tipo, motivo, *ad in EXPL[('C3.0-01', 'solto')]:
                    s = edita(ctx + ' (texto)', s, ant, nov, tipo, motivo, ad[0] if ad else '')
                assert not RX_PROIBIDO_LOCAL.search(tit + s), (b['cod'], s)
                out += ['### ' + tit, '', s, '']
                mapa.append(dict(origem=f"{b['cod']} {b['titulo']} (curso do caput 3, sem folha)", destino=f'### {tit} (primeiro ### do ## {p["cod"]})'))
                b['saida'] = dict(titulo=tit, d=s, e='', g='', base=[], caput=True)
                continue
            if suf:
                assert RX_SUFIXO.fullmatch(suf), (b['cod'], suf)
                log(ctx + ' (título)', D_MARCA, suf.strip(), '', 'marca de produção no título do bloco (seção 6: "v2", "R2", "QA PENDENTE", "leitura externa", códigos de pares e pegadinhas)')
            d, e, g = b['campos']['def'], b['campos']['ex'], b['campos']['peg']
            for (blk, campo), lst in EXPL.items():
                if blk != b['cod'] or campo == 'solto': continue
                for ant, nov, tipo, motivo, *ad in lst:
                    ad = ad[0] if ad else ''
                    if campo == 'def': d = edita(ctx + ' (definição)', d, ant, nov, tipo, motivo, ad)
                    elif campo == 'ex': e = edita(ctx + ' (exemplo)', e, ant, nov, tipo, motivo, ad)
                    else: g = edita(ctx + ' (pegadinha)', g, ant, nov, tipo, motivo, ad)
            m = re.fullmatch(r'(.*?) \[Desfeita por: (.+)\]', g)
            assert m, (b['cod'], g[-80:])
            claim, base = m.group(1), m.group(2)
            log(ctx + ' (pegadinha)', 'troca de rótulo', '[Desfeita por: ' + base + ']', 'Base: ' + base, 'operação 2 da seção 7', 'Base')
            g = claim + ' Base: ' + base
            assert 'hipotétic' in e, (b['cod'], e[-60:])
            for campo_txt in (tit, d, e, g):
                assert not RX_PROIBIDO_LOCAL.search(campo_txt), (b['cod'], RX_PROIBIDO_LOCAL.search(campo_txt).group(0), campo_txt[:120])
            out += ['### ' + tit, '']
            mapa.append(dict(origem=f"{b['cod']} {b['titulo']}" + (f" {suf.strip()}" if suf else ''), destino='### ' + tit))
            out.append('DEFINIÇÃO')
            ss = sentencas(d)
            if len(ss) >= 3: out.extend('- ' + s for s in ss)
            else: out.append(d)
            out.append('')
            bl = base_legal(b['cod'], tit, base)
            out.append('BASE LEGAL'); out.extend('- ' + x for x in bl); out.append('')
            out += ['EXEMPLO PARLAMENTAR', e, '', 'PEGADINHA PROVÁVEL', g, '']
            b['saida'] = dict(titulo=tit, d=d, e=e, g=g, base=bl)
    while out and out[-1] == '': out.pop()
    return '\n'.join(out), mapa

# ---------------------------------------------------------------- resumo
def monta_resumo(L):
    ini = achar(L, '## 2. (b) RESUMO'); fim = achar(L, '---', ini)
    linhas = [l for l in L[ini + 1:fim] if not l.startswith('### Resumo do item ')]
    while linhas and not linhas[0].strip(): linhas.pop(0)
    while linhas and not linhas[-1].strip(): linhas.pop()
    txt = '\n'.join(linhas)
    txt = re.sub(r'\n{3,}', '\n\n', txt)
    for n in (3, 4):
        log('resumo', D_MARCA, f'### Resumo do item {n}', '', 'subtítulo de produção da seção 2 do canônico ("uma página por item do edital"); cada página já abre com "**Item {0} — …**"'.format(n))
    txt = edita('resumo', txt, '(EC 138/2025; REVERIFICAR)', '(EC 138/2025)', D_MARCA, M_REV)
    txt = edita('resumo', txt, '| Número literal do Anexo N | Dispositivo |', '| Número literal | Dispositivo |', D_MARCA, 'sai "do Anexo N" do cabeçalho da tabela (seção 6); a tabela é mantida')
    txt = edita('resumo', txt, '(estágio probatório, no referencial do Decreto; REVERIFICAR)', '(estágio probatório, no referencial do Decreto)', D_MARCA, M_REV)
    return txt

# ---------------------------------------------------------------- pares
def monta_pares(L):
    ini = achar(L, '## 3. (c) PARES'); fim = achar(L, '## 4. (d) PEGADINHAS', ini)
    pares = []
    for l in L[ini:fim]:
        if not re.match(r'^\| P-\d\d', l): continue
        cel = [c.strip() for c in l.strip().strip('|').split('|')]
        assert len(cel) == 5, l[:60]
        cod, par, dif, _base, banca = cel
        ctx = 'par ' + cod
        if cod == 'P-06':
            dif = edita(ctx, dif, ' (REVERIFICAR)', '', D_MARCA, M_REV)
            dif = edita(ctx, dif, ' A conciliação entre esses textos é matéria de doutrina e jurisprudência não aberta neste material — [SEM FONTE — não afirmar].', '', D_FRASE, M_SEMFONTE + '; ficam os dois referenciais (Lei 8.112 e Decreto) e a estabilidade, cada um na sua norma, sem conciliação')
        if cod == 'P-62':
            dif = edita(ctx, dif, ', hipótese que este lote não usa', '', D_ORACAO, M_LOTE)
        termos = par.split(' × ')
        assert len(termos) >= 2, par
        a, b = termos[0], ' × '.join(termos[1:])
        assert dif.endswith('.') and banca.endswith('.'), cod
        pares.append(dict(a=a, b=b, como=dif + ' Como a banca troca: ' + banca, _cod=cod))
    assert len(pares) == 46, len(pares)
    return pares

PEG_SUF = ' [acréscimo da v2]'

def monta_pegadinhas(L):
    ini = achar(L, '## 4. (d) PEGADINHAS'); fim = achar(L, '---', ini)
    out = []
    for l in L[ini + 1:fim]:
        m = re.match(r'^G-(\d{2,3})\. \[(C\d\.\d-\d\d)(?:; (C\d\.\d-\d\d))?\] (.+)$', l)
        if not m: continue
        n, cb, cb2, t = int(m.group(1)), m.group(2), m.group(3), m.group(4)
        if cb2: assert cb2[:4] == cb[:4], (n, cb, cb2)   # os dois blocos são da mesma folha
        ctx = f'pegadinha {n}'
        if PEG_SUF in t:
            log(ctx, D_MARCA, PEG_SUF.strip(), '', 'marca "v2" (seção 6)')
            t = t.replace(PEG_SUF, '')
        claim, sep, disp = t.rpartition(' — Dispositivo: ')
        assert sep and disp.endswith('.'), l[:60]
        assert claim.endswith(('.', '?', '!')), (n, claim[-30:])
        log(ctx, 'troca de rótulo', ' — Dispositivo: ' + disp, ' Base: ' + disp, 'operação 2 da seção 7 (o rótulo "Dispositivo:" vira "Base:", como no curso e como no D5)', 'Base')
        eid = 'P1-DA-' + cb[1:4]
        assert eid in EDITAL, eid
        out.append(dict(itemEdital=eid, rotulo=EDITAL[eid], texto=claim + ' Base: ' + disp))
    assert len(out) == 114, len(out)
    return out

# ---------------------------------------------------------------- itens
def monta_itens(L):
    i51 = achar(L, '### 5.1'); i52 = achar(L, '### 5.2', i51); fim = achar(L, '## 6.', i52)
    enun = {}
    for l in L[i51:i52]:
        m = re.match(r'^\*\*(D2-\d\d)\.\*\* (.+)$', l)
        if m: enun[m.group(1)] = m.group(2)
    blocos, cur = [], None
    for l in L[i52:fim]:
        m = re.match(r'^\*\*(D2-\d\d)\*\* \(folha (\d\.\d)\) — AUTORAL — (.*)$', l)
        if m: cur = dict(id=m.group(1), folha=m.group(2), cab=m.group(3), F={}); blocos.append(cur); continue
        if cur is not None and l.startswith('- '):
            k, _, v = l[2:].partition(': ')
            cur['F'][k] = v
    assert len(blocos) == 80 and len(enun) == 80, (len(blocos), len(enun))
    JUST_EDIT = {
     'D2-74': [(', ponto do D1-16)', ')', D_MARCA, 'código de item de outro lote ("ponto do D1-16"; seção 6); fica "(art. 1º, § 1º)"')],
    }
    itens = []
    for b in sorted(blocos, key=lambda x: int(x['id'].split('-')[1])):
        i = b['id']
        assert b['F']['Folha'] == b['folha'] and b['folha'] in FOLHAS
        j1, j2 = b['F']['Justificativa (linha 1)'].strip(), b['F']['Justificativa (linha 2)'].strip()
        j = j1 + ' ' + j2
        if 'Não há troca:' in j:
            j = edita('justificativa ' + i, j, 'Não há troca:', 'Não há troca;', 'pontuação (nenhuma palavra alterada)',
                      'a sequência literal "troca:" consta da lista de proibidos da seção 6 (marca "troca:"); aqui é palavra comum da frase, e só os dois-pontos passam a ponto e vírgula (mesmo tratamento dado no D1, item D1-01, e no D5, item D5-04)')
        for ant, nov, tipo, motivo in JUST_EDIT.get(i, []):
            j = edita('justificativa ' + i, j, ant, nov, tipo, motivo)
        if 'elemento-isca' in j:
            j = edita('justificativa ' + i, j, 'elemento-isca:', 'elemento que parece trocado:', TROCA,
                      '"elemento-isca" é marca de produção (seção 6); trocado pela expressão equivalente "elemento que parece trocado" (mesma troca do D5); o restante da frase fica igual', 'elemento que parece trocado')
        marcas = b['F']['Marcas']
        vol = ('REVERIFICAR=sim' in marcas) or ('VOLÁTIL=sim' in marcas)
        it = dict(id=i, rotulo='AUTORAL', certame='Projeto Câmara 2026', cargo='Noções de Direito Administrativo e Administração Pública', ano=2026,
                  numero=int(i.split('-')[1]), comando='Julgue o item a seguir.', textoBase='', enunciado=enun[i],
                  gabarito=b['F']['Gabarito'].strip(), justificativa=j, itemEdital='P1-DA-' + b['folha'], aderencia='direta', url=URL_CANON)
        if vol: it['volatil'] = True
        it['_marcas'] = marcas; it['_j1'] = j1; it['_j2'] = j2
        itens.append(it)
    return itens

# ---------------------------------------------------------------- montagem
def monta():
    LOG.clear(); PROC_LINHAS.clear()
    L = ler_canon()
    partes = parse_curso(L)
    curso, mapa = monta_curso(partes)
    resumo = monta_resumo(L)
    pares = monta_pares(L)
    pegs = monta_pegadinhas(L)
    itens = monta_itens(L)
    ie = ['P1-DA-' + p['cod'] for p in partes if not p['caput']]
    assert ie == ['P1-DA-' + f for f in FOLHAS], ie
    lote = dict(id='D2', nome=NOME, prova='P1', itensEdital=ie, resumo=resumo, curso=curso,
                pares=[{k: v for k, v in p.items() if not k.startswith('_')} for p in pares], pegadinhas=pegs)
    if TOPICOS.exists():
        tp = json.loads(TOPICOS.read_text(encoding='utf-8'))
        if set(tp) != set(ie): print('AVISO: chaves de D2_topicos_fonte.json diferem dos blocos ##:', sorted(set(tp) ^ set(ie)))
        topicos = {k: tp[k] for k in ie if k in tp}
    else:
        topicos = {}
        print('AVISO: D2_topicos_fonte.json ainda não existe; topicos vazio')
    itens_pub = [{k: v for k, v in it.items() if not k.startswith('_')} for it in itens]
    dados = dict(lote=lote, itens=itens_pub, topicos=topicos)
    return dados, dict(L=L, partes=partes, mapa=mapa, itens=itens, pares=pares, pegs=pegs, resumo=resumo, curso=curso)

def grava(dados):
    SAIDA_JSON.write_text(json.dumps(dados, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    LOG_JSON.write_text(json.dumps(dict(log=LOG, linhas_de_processo_fora=PROC_LINHAS), ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

# ---------------------------------------------------------------- registro
def roda(cmd):
    r = subprocess.run([sys.executable, '-I'] + cmd, capture_output=True, text=True, cwd=str(RAIZ))
    return r.returncode, (r.stdout + r.stderr).strip()

def registro(dados, ctx):
    rc_val, val = roda([str(VALIDADOR), str(SAIDA_JSON), str(CANON), str(MAPA)])
    rc_fid, fid = roda([str(CONFERE)])
    it = dados['itens']
    por_folha = Counter(x['itemEdital'] for x in it)
    n_c = sum(1 for x in it if x['gabarito'] == 'C'); n_e = len(it) - n_c
    vol = [x['id'] for x in it if x.get('volatil')]
    por_peg = Counter(p['itemEdital'] for p in dados['lote']['pegadinhas'])
    W = []
    W.append('# D2_registro_formato.md — T-75 (ordem DA 20/10/2026) — 2026-10-20 — gerado por gcb-cpp')
    W.append('')
    W.append('Reformatação do Lote D2 (Agentes públicos e direito administrativo disciplinar, itens 3 e 4 do edital) para o formato da plataforma (FORMATO_PLATAFORMA_DA.md). Só forma; nenhum conteúdo novo. Gerado por `saida/gcb/DA_plataforma/scripts/formatar_D2.py --registro`; fidelidade por `saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D2.py`.')
    W.append('')
    W.append('## 1. Fontes e conferências')
    W.append(f'- Canônico: saida/gcb/D2_v2_1.md, SHA-256 {sha(CANON.read_bytes())} (igual ao esperado 59cffaa6…8bd2c: o script confere antes de ler e pararia se divergisse).')
    W.append(f'- Base normativa: saida/gcb/D2_anexo_N_mapa_normativo.md (consulta de 20/10/2026), SHA-256 {sha(MAPA.read_bytes())}; usado só pelo validador e pelo visual baseLegal (texto copiado letra a letra da coluna de texto do mapa, `literal: true`, `conferido: 2026-10-20`).')
    W.append('- Seções do canônico NÃO usadas: 0 e 0.1 (resposta ao R1 e registro de acatamento), os dois parágrafos "Cada bloco: …" da seção 1 (convenções de produção; um abre a seção e outro fica solto antes da folha 4.1), o cabeçalho das seções 3 e 4 (contagens de produção: "Mínimo da ficha…", "Entregues…"), 6 (proveniência), 7 (contagens), 8 (bloco à GCB), as linhas Folha, Ponto de julgamento, Formato, Base, Mecanismo, Troca, Alteração na v2, "Difere de …" e Marcas de cada item, e as colunas "Código" e "Base" dos pares.')
    W.append(f'- JSON gerado: D2_plataforma.json, SHA-256 {sha(SAIDA_JSON.read_bytes())}; tópicos incorporados de D2_topicos_fonte.json, SHA-256 {sha(TOPICOS.read_bytes())} (escritos à mão); log das edições (lido pela conferência): D2_log_edicoes.json, SHA-256 {sha(LOG_JSON.read_bytes())}.')
    W.append('')
    W.append('## 2. Correspondência bloco de origem → ## / ###')
    W.append('| Origem (D2_v2_1.md, seção 1) | Destino no curso |')
    W.append('|---|---|')
    for m in ctx['mapa']:
        W.append(f"| {m['origem'].replace('|', '/')} | `{m['destino']}` |")
    W.append('')
    W.append('Regras gerais do curso: "- Definição:" → quadro DEFINIÇÃO (em lista, sem linha em branco, quando a definição tem 3 ou mais frases: operação 4; em parágrafo único nos demais casos); quadro BASE LEGAL em lista com os dispositivos que o próprio título do bloco cita entre parênteses ("(CF, art. 37, VI, VII e VIII; Lei 8.112/1990, art. 5º, § 2º)" → duas linhas; dispositivo sem norma no título herda a norma anterior do mesmo parêntese); nos blocos cujo título não traz norma e artigo juntos (C3.2-07, C4.1-08, C4.1-09, C4.4-13) usam-se os dispositivos da lista "[Desfeita por: …]" do próprio bloco, sem os comentários entre parênteses; em C4.1-10, C4.2-06 e C4.4-17 a lista foi fixada à mão com o que o bloco cita ("Lei 8.112, art. 129, caput"; "Lei 9.784/1999, art. 68" e "art. 69-A"). "- Exemplo (Legislativo, hipotético):" → EXEMPLO PARLAMENTAR (o canônico já termina cada exemplo com "O exemplo é hipotético…": mantido, sem acréscimo); "- Pegadinha provável: … [Desfeita por: X]" → PEGADINHA PROVÁVEL com "Base: X". Código de bloco ("C3.1-01 ") removido do título; sufixo " — acréscimo da v2 (leitura externa …; QA PENDENTE (R2))" removido (30 blocos). Títulos `##`: texto do edital em maiúsculas (nenhum passa de 90 caracteres, então não há corte no primeiro ":"). Resumo: seção 2 inteira (as duas páginas, "Item 3" e "Item 4", em sequência, sem os subtítulos "### Resumo do item N"). Pares: seção 3, 46 (26 do item 3 e 20 do item 4); `a`/`b` = termos do campo "Par" (a = primeiro; b = demais unidos por " × ", caso de P-01 e P-69); `como` = coluna Diferença + " Como a banca troca: " + coluna "Como a banca troca"; a coluna Base não entra. Pegadinhas: seção 4, 114, sem número, sem código do bloco e sem marca de versão; " — Dispositivo: X" vira " Base: X"; `itemEdital` pela folha do bloco ([C3.3-06; C3.3-11] e [C4.3-07; C4.3-08] → a folha comum, 3.3 e 4.3).')
    W.append('')
    W.append('## 3. Deleções e trocas (cada uma registrada)')
    W.append('Tipos: deleção de marca (v2, R2, QA PENDENTE, leitura externa, Anexo N, REVERIFICAR, códigos de bloco, de par e de item do banco, "núcleo"/"complementar" do mapa); deleção de frase inteira ou de oração (processo, "[SEM FONTE]", cobertura do lote, remissão a outro lote ou a outro bloco); troca mínima (op. 6); troca de rótulo (operação 2).')
    W.append('')
    ERRS = [e for e in LOG if e['motivo'].startswith('errata de forma')]
    GER = [e for e in LOG if not e['motivo'].startswith('errata de forma')]
    por_tipo = Counter(e['tipo'] for e in GER)
    W.append('Contagem por tipo (sem as da errata, seção "Errata de forma"): ' + '; '.join(f'{k}: {v}' for k, v in sorted(por_tipo.items())) + '.')
    W.append('')
    k = 0
    for e in GER:
        if e['tipo'] == 'troca de rótulo': continue
        k += 1
        dep = ('→ `' + e['depois'] + '`') if e['depois'] else '→ (nada)'
        W.append(f"{k}. [{e['ctx']}] {e['tipo']}: `{e['antes']}` {dep}. Motivo: {e['motivo']}.")
    W.append('')
    n_ex = sum(1 for e in LOG if e['tipo'] == 'troca de rótulo' and e['ctx'].startswith('curso'))
    n_pg = sum(1 for e in LOG if e['tipo'] == 'troca de rótulo' and e['ctx'].startswith('pegadinha'))
    W.append(f'Trocas de rótulo (operação 2): {n_ex} pegadinhas do curso ("[Desfeita por: X]" → "Base: X") e {n_pg} pegadinhas da lista consolidada (" — Dispositivo: X" → " Base: X").')
    W.append('')
    W.append('Decisões de leitura que o orquestrador pode querer revisar (nenhuma altera conteúdo normativo):')
    W.append('- Curso do caput 3 (bloco C3.0-01, sem itens, sem par e sem pegadinha): o bloco tem uma única linha de cerca de 55 palavras depois das deleções, sem Definição, Exemplo ou Pegadinha. Não foi possível dar-lhe um tópico próprio (`## 3 AGENTES PÚBLICOS` com `P1-DA-3`) com resumo de 150 palavras sem fato novo; por isso ele vai como PRIMEIRO `###` do `## 3.1 DISPOSIÇÕES CONSTITUCIONAIS APLICÁVEIS`, com o título "Caput 3 — Agentes públicos" (sai a nota de produção "curso curto; sem item, sem par e sem pegadinha próprios"), em parágrafo simples, sem quadros (o original não tem os rótulos). Em consequência `itensEdital` não traz `P1-DA-3` nem `P1-DA-4`, e `topicos` tem as 8 folhas 3.1 a 4.4.')
    W.append('- Estágio probatório e estabilidade (blocos de 3.4, 3.1 e 3.3, par P-06, resumo e tópico 3.4): só a letra de cada norma, cada uma no seu referencial (Lei 8.112, art. 20, caput: 24 meses; CF, art. 41, caput: três anos para a estabilidade; Decreto 12.374/2025, art. 2º, caput: trinta e seis meses). Saíram a frase "A conciliação entre esses textos é matéria de doutrina e jurisprudência não aberta neste material — [SEM FONTE]" (curso 3.4 e par P-06) e a frase de C3.4-13 que remetia ao tratamento do bloco do estágio. O tópico 3.4 não concilia: apresenta os três textos lado a lado.')
    W.append('- Marcas REVERIFICAR (CF, art. 37, XVI, b, EC 138/2025; Decreto 12.374/2025; EC 140/2026): as marcas saíram e o conteúdo foi mantido, como o D5 fez com a Lei 15.471/2026. A posição sobre a EC 140/2026 (posterior ao edital, registrada, não incorporada; vale a redação da EC 103/2019) permanece no curso e no resumo.')
    W.append('- Remissões "folha 3.4" (C3.1-02, C3.1-08), "Nesta folha vale só a proposição da fonte" (C4.1-10) e "edital 13.33" (base de C3.1-05): as de "folha" foram mantidas na primeira entrega e TRATADAS PELA ERRATA DE 20/10/2026 (seção "Errata de forma": "folha" vira "subitem" ou a frase sai); "edital 13.33" segue mantida (não está na lista da seção 6) e os números 3.4 etc. são os dos títulos `##` do curso. As remissões a código de bloco (C3.4-03 etc.), a par (P-18, P-63) e a lote (D1, "outro lote") saíram; só em C3.1-06 ("ver C3.4-03") a troca foi por "o item 3.4", registrada.')
    W.append('- Frases de nota sobre ação no STF ("o compilado remete a ação no STF; efeito não conferido neste material", curso e resumo) foram mantidas: são conteúdo para a candidata (ressalva de que o efeito da decisão não foi conferido) e não constam da lista da seção 6.')
    W.append('- Enunciados começam com "Considere…" ou são frases soltas e trazem a situação no próprio enunciado; o canônico não separa texto-base: `textoBase` "" e `comando` "Julgue o item a seguir." (o canônico só traz "Julgue cada item como Certo ou Errado." no cabeçalho da seção 5.1).')
    W.append('- Pegadinhas G-42 e G-107 trazem dois blocos de origem ([C3.3-06; C3.3-11] e [C4.3-07; C4.3-08]); o `itemEdital` é o da folha comum (P1-DA-3.3 e P1-DA-4.3).')
    tp = dados['topicos']
    palavras = {k: len(v['resumo'].split()) for k, v in tp.items()}
    tipos = {k: ' + '.join(x['tipo'] for x in v['visuais']) for k, v in tp.items()}
    W.append('- Tópicos (8, um por `##`, de P1-DA-3.1 a P1-DA-4.4; escritos à mão em D2_topicos_fonte.json): `emUmMinuto` com 3 frases; `resumo` só com fatos, números e dispositivos que estão no curso da folha (a conferência confere que todo número e todo artigo do tópico aparece no curso dela), de ' + str(min(palavras.values())) + ' a ' + str(max(palavras.values())) + ' palavras (' + '; '.join(f'{k.replace("P1-DA-", "")}: {n}' for k, n in palavras.items()) + '); visuais por tópico: ' + '; '.join(f'{k.replace("P1-DA-", "")}: {v}' for k, v in tipos.items()) + '.')
    W.append('- Visuais pedidos como comparação de três figuras (cargo × emprego × função, na 3.2; advertência × suspensão × demissão, na 4.2): o tipo `compare` só tem dois lados (a, b), então foram feitos como `tabela` (3 e 4 colunas). As comparações de dois lados usam `compare`: requisição × cessão (3.3), remoção × redistribuição (3.4) e sindicância × processo disciplinar (4.3). Prazos e fases em `fluxo` (4.3: 60 dias, defesa de 10 dias, julgamento em 20 dias) e em `tabela` (4.4: arts. 24, 26, § 2º, 44, 49, 56, § 1º, 59 e 66) só os que estão no curso da folha e no mapa normativo.')
    W.append('- `baseLegal` (7 dos 8 tópicos; todos com `literal: true` e `conferido: 2026-10-20`, data da consulta do mapa normativo): o texto de cada dispositivo foi copiado letra a letra da coluna de texto do mapa, inclusive a grafia do compilado ("observados os seguinte fatores", no art. 20, caput, da Lei 8.112) e a nota do compilado do art. 21 ("(prazo 3 anos - vide EMC nº 19)"); a conferência de fidelidade e o validador confirmam a literalidade. No tópico 4.3 não há `baseLegal`: os dois visuais (`compare` e `fluxo`) já trazem os artigos e os prazos, e o limite é de 2 visuais.')
    W.append('- Estágio probatório (tópico 3.4): o `baseLegal` traz lado a lado a letra de cada texto (Lei 8.112, art. 20, caput e art. 21, caput; CF, art. 41, caput; Decreto 12.374/2025, art. 2º, caput), e o resumo e o `emUmMinuto` dizem o que cada norma diz, sem conciliar.')
    W.append('')
    W.append('## 4. Itens')
    W.append(f'- Total {len(it)}; C {n_c} / E {n_e}.')
    W.append('- Por itemEdital: ' + '; '.join(f'{k}: {v}' for k, v in sorted(por_folha.items(), key=lambda kv: kv[0])) + '.')
    W.append('- volatil true: ' + (', '.join(vol) if vol else 'nenhum') + ' (as linhas "Marcas:" com REVERIFICAR=sim; as demais trazem REVERIFICAR=não e VOLÁTIL=não).')
    just = [e for e in LOG if e['ctx'].startswith('justificativa')]
    n_pt = sum(1 for e in just if e['antes'] == 'Não há troca:')
    n_is = sum(1 for e in just if e['antes'] == 'elemento-isca:')
    W.append(f'- Justificativa: linhas 1 e 2 unidas por um espaço; edições: a pontuação "Não há troca:" → "Não há troca;" em {n_pt} itens (nenhuma palavra alterada), a troca mínima "elemento-isca:" → "elemento que parece trocado:" em {n_is} itens e a deleção de ", ponto do D1-16" em D2-74; as demais são idênticas às duas linhas. As linhas "Difere de …" e "Mecanismo" são campos à parte no canônico e não entram.')
    W.append(f"- Pares: {len(dados['lote']['pares'])}; pegadinhas: {len(dados['lote']['pegadinhas'])} (" + '; '.join(f'{k}: {v}' for k, v in sorted(por_peg.items())) + f"); tópicos: {len(dados['topicos'])} ({', '.join(dados['topicos'])}).")
    W.append('')
    W.append('## 5. Saída do validador')
    W.append('Comando: `python3 -I saida/gcb/DA_plataforma/scripts/validar_da.py saida/gcb/DA_plataforma/D2_plataforma.json saida/gcb/D2_v2_1.md saida/gcb/D2_anexo_N_mapa_normativo.md`')
    W.append('```')
    W.append(val)
    W.append('```')
    W.append('')
    W.append('## 6. Conferência de fidelidade')
    W.append('Comando: `python3 -I saida/gcb/DA_plataforma/scripts/conferir_fidelidade_D2.py`')
    W.append('')
    W.append(fid)
    W.append('')
    W.append('## Errata de forma — QA final 20/10/2026')
    W.append('Origem: QA final do pacote v1.13 (gbq-cqe, 20/10/2026), achado 1: a palavra de produção "folha" no texto exibido (a candidata não conhece "folha"; o validador passou a acusá-la). Regra da ordem: frase que só fala do processo ou da organização da produção é DELETADA; remissão útil ao estudo vira "subitem". Só forma: nenhum enunciado, gabarito, itemEdital ou id foi tocado. Cada entrada abaixo está também no log de edições (D2_log_edicoes.json) e é conferida pela conferência de fidelidade.')
    W.append('')
    for i, e in enumerate(ERRS, 1):
        dep = ('→ `' + e['depois'] + '`') if e['depois'] else '→ (nada)'
        W.append(f"{i}. [{e['ctx']}] {e['tipo']}: `{e['antes']}` {dep}. Motivo: {e['motivo']}.")
    W.append('')
    W.append(f'Total: {len(ERRS)} mudanças no D2 (curso). Resumo, pares, pegadinhas, justificativas e tópicos do D2 não tinham a palavra "folha" nem código R/F.')
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

main()
