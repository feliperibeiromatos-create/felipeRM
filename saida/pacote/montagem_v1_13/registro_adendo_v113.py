# registro_adendo_v113.py — T-118 (D1 da GBQ, saida/pacote/T118_D1_v1_13_2026-10-20.md, passo 4.3.3) — 2026-10-20 — gerado por gbq-csc
# Gera out/registro_adendo5.md, o texto do adendo 5 ao registro GBQ v3 (e aos adendos 1 a 4, que ficam intactos): os 410 itens de DA (P1-DA) — fontes (canônico, ids, SHA-256, ato, arquivo de plataforma
# com SHA-256), totais por lote (n, C, E, [TS], VOLÁTEIS, PARCIAIS, aptos a final), formatos, ids vagos, regras R1/R6, restrições de montagem, regra de qualificação "lote D<n>", ids D<n>-R<nn> reservados e itens por folha.
# Formato do adendo 4 (saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo4_2026-10-18.md). Não reproduz enunciados. Só leitura do repositório; grava só out/registro_adendo5.md.
# Uso: python3 -I registro_adendo_v113.py   (falha com exit 1 se uma conferência interna não bater). Não lê relógio.
import json, hashlib, pathlib, re, sys, collections
R = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).parent
OUT = HERE / 'out'
GCB = R / 'saida/gcb'; DA = GCB / 'DA_plataforma'
DATA = '2026-10-20'
D1_ARQ = 'saida/pacote/T118_D1_v1_13_2026-10-20.md'
CANON = {1: 'D1_v2.md', 2: 'D2_v2_1.md', 3: 'D3_v2_1.md', 4: 'D4_v2_1.md', 5: 'D5_v2_1.md', 6: 'D6_v2_1.md'}
ATO = {1: ('D-LOTED1-CANONICO', 93), 2: ('D-LOTED2-CANONICO', 163), 3: ('D-LOTED3-CANONICO', 164), 4: ('D-LOTED4-CANONICO', 165), 5: ('D-LOTED5-CANONICO', 162), 6: ('D-LOTED6-CANONICO', 117)}
# valores esperados pela D1 (preâmbulo e 4.3.3)
CE = {1: (30, 30), 2: (40, 40), 3: (31, 40), 4: (41, 38), 5: (35, 35), 6: (25, 25)}
VOLATEIS = ['D2-01', 'D2-28', 'D6-09', 'D6-32', 'D6-34']
VAGOS = ['D3-19', 'D3-31', 'D3-39', 'D3-42', 'D3-48', 'D3-50', 'D3-57', 'D3-60', 'D3-65', 'D3-69', 'D5-54']
SHA_ANTIGO_D6 = '8b8e5a42'
FORMATO_COD = [('def', 'DEF'), ('suj', 'SUJ'), ('sit', 'SIT'), ('num', 'NUM'), ('par', 'PAR'), ('apl', 'APL'), ('tro', 'SUJ'), ('núm', 'NUM'), ('sua', 'SIT'), ('situ', 'SIT')]
FORMATO_NOME = collections.OrderedDict([('DEF', 'definição'), ('SUJ', 'troca de sujeito ou de competência'), ('SIT', 'situação hipotética'), ('NUM', 'número ou prazo'), ('PAR', 'par confundível'), ('APL', 'aplicação parlamentar')])


def sha(b): return hashlib.sha256(b).hexdigest()
def lj(p): return json.loads(pathlib.Path(p).read_text(encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
def falha(m): print('FALHA:', m); sys.exit(1)


def cod_formato(txt):
    t = txt.strip().lower()
    if t.startswith('def'): return 'DEF'
    if t.startswith('troca'): return 'SUJ'
    if t.startswith('situa'): return 'SIT'
    if t.startswith('n'): return 'NUM'
    if t.startswith('par'): return 'PAR'
    if t.startswith('apl'): return 'APL'
    if t[:3] in ('suj',): return 'SUJ'
    if t[:3] in ('sit',): return 'SIT'
    falha('formato não reconhecido: %r' % txt)


def parse_canon(n):
    L = (GCB / CANON[n]).read_text(encoding='utf-8').split('\n')
    s = [i for i, l in enumerate(L) if re.match(r'^#{1,3} 5\.2 Gabarito comentado', l)]
    assert len(s) == 1
    fim = next((i for i in range(s[0] + 1, len(L)) if re.match(r'^#{1,2} 6\.', L[i])), len(L))
    hdr = [i for i in range(s[0], fim) if re.match(r'^\*\*D%d-\d\d\*\*' % n, L[i])]
    out = collections.OrderedDict()
    for k, i in enumerate(hdr):
        j = hdr[k + 1] if k + 1 < len(hdr) else fim
        blk = '\n'.join(L[i:j])
        iid = re.match(r'^\*\*(D%d-\d\d)\*\*' % n, L[i]).group(1)
        g = re.search(r'Gabarito:\s*\**\s*([CE])\b', blk)
        mm = re.search(r'Marcas:([^\n]*)', blk); mt = mm.group(1) if mm else ''
        f = re.search(r'^- Formato:\s*(.+)$', blk, re.M)
        out[iid] = dict(gab=g.group(1) if g else None, ts=('[TS]' in L[i]) or ('TS=sim' in mt) or ('[TS]' in mt),
                        rev=('REVERIFICAR=sim' in mt) or bool(re.search(r'REVERIFICAR(?!=)', mt)), vol=('VOLÁTIL=sim' in mt) or bool(re.search(r'VOLÁTIL(?!=)', mt)),
                        formato=cod_formato(f.group(1)) if f else None)
    return out


def main():
    pac = lj(OUT / 'pacote.json'); dec = (R / 'DECISOES.md').read_text(encoding='utf-8').split('\n')
    da = [i for i in pac['itens'] if i['itemEdital'].startswith('P1-DA-')]
    if len(da) != 410: falha('%d itens DA (esperado 410)' % len(da))
    canon = {n: parse_canon(n) for n in CANON}
    by_id = {i['id']: i for i in da}
    # conferências internas: ids = os do pacote; gabarito = o do canônico; SHA-256 na linha do ato; C/E
    ids_canon = [x for n in CANON for x in canon[n]]
    if sorted(ids_canon) != sorted(by_id): falha('o conjunto de ids do canônico difere do pacote')
    meta = {}
    for n in CANON:
        for x, v in canon[n].items():
            if by_id[x]['gabarito'] != v['gab']: falha('gabarito de %s difere do canônico' % x)
            meta[x] = dict(lote=n, **v, folha=by_id[x]['itemEdital'], volatil=bool(by_id[x].get('volatil')), aderencia=by_id[x]['aderencia'])
    shas = {}
    for n in CANON:
        b = (GCB / CANON[n]).read_bytes()
        if b'\r' in b: falha('%s tem CR: o SHA-256 (LF) difere' % CANON[n])
        shas[n] = sha(b)
        ato, linha = ATO[n]
        if not (('| %s |' % ato) in dec[linha - 1] and shas[n] in dec[linha - 1]): falha('SHA-256 de %s ausente da linha %d de DECISOES.md' % (CANON[n], linha))
    plat = {n: sha((DA / ('D%d_plataforma.json' % n)).read_bytes()) for n in CANON}
    vol = [x for x in meta if meta[x]['volatil']]
    if vol != VOLATEIS: falha('volatil %s difere do preâmbulo %s' % (vol, VOLATEIS))
    if [x for x in meta if meta[x]['vol'] or meta[x]['rev']] != VOLATEIS: falha('marcas VOLÁTIL/REVERIFICAR do canônico diferem da lista de voláteis')
    par = [x for x in meta if meta[x]['aderencia'] == 'parcial']
    if par: falha('PARCIAIS: %s (esperado 0)' % par)
    # vagos
    vagos = []
    for n in (3, 5):
        pres = {int(x[3:]) for x in canon[n]}
        vagos += ['D%d-%02d' % (n, k) for k in range(1, max(pres) + 1) if k not in pres]
    if vagos != VAGOS: falha('ids vagos %s difere do preâmbulo' % vagos)

    L = []; w = L.append
    w('# claude_GBQ_Registro_AUTORAL_v3_adendo5_%s.md — T-118 — %s — gerado por gbq-csc (registro_adendo_v113.py)' % (DATA, DATA))
    w('# GBQ — REGISTRO DE ITENS AUTORAL — v3, ADENDO 5: Direito Administrativo (P1-DA), lotes D1 a D6 (%s)' % DATA)
    w('Texto do adendo 5 ao registro v3, aos adendos 1 a 4 (intactos). Base: D1 da GBQ, %s, seção 4.3 (passo 3), e o contrato v1.2.10 (saida/pacote/contrato_v1_2_10_2026-10-20.md, seção 5). Pacote v1.13 (out/pacote.json); itens dos 6 lotes em 46 entradas de edital P1-DA. Não reproduz enunciados: os textos estão nos arquivos canônicos e de plataforma abaixo.' % D1_ARQ)
    w('')
    w('## 1. Fontes (canônico, ids, SHA-256 do conteúdo LF, ato, arquivo de plataforma)')
    w('| Lote | Canônico | Ids | n | SHA-256 do canônico (LF) | Ato (linha em DECISOES.md) | Arquivo de plataforma | SHA-256 do arquivo de plataforma |')
    w('|---|---|---|--:|---|---|---|---|')
    for n in CANON:
        ids = list(canon[n]); nome = 'D%d' % n
        num = sorted(ids, key=lambda x: int(x[3:]))      # faixa pela ordem numérica do id (achado 2 da fidelidade T-118)
        vg = [x for x in VAGOS if x.startswith('D%d-' % n)]
        if num[0] != 'D%d-01' % n or [x for x in ('D%d-%02d' % (n, k) for k in range(1, int(num[-1][3:]) + 1)) if x not in ids] != vg: falha('faixa do lote D%d não fecha com os vagos' % n)
        faixa = '%s a %s' % (num[0], num[-1]) + ('' if not vg else ' (sem o vago da seção 4)' if len(vg) == 1 else ' (sem os vagos da seção 4)')
        pl = plat[n] + (' (novo; errata de forma do achado 10; antes %s…)' % SHA_ANTIGO_D6 if n == 6 else '')
        w('| %s | saida/gcb/%s | %s | %d | %s | %s (%d) | saida/gcb/DA_plataforma/D%d_plataforma.json | %s |' % (nome, CANON[n], faixa, len(ids), shas[n], ATO[n][0], ATO[n][1], n, pl))
    w('')
    w('## 2. Totais por lote')
    w('| Lote | n | C | E | [TS] | VOLÁTEIS | PARCIAIS | Aptos a final (não VOLÁTIL e não PARCIAL) |')
    w('|---|--:|--:|--:|--:|--:|--:|--:|')
    tot = collections.Counter()
    for n in CANON:
        ids = list(canon[n]); c = sum(canon[n][x]['gab'] == 'C' for x in ids); e = len(ids) - c
        if (c, e) != CE[n]: falha('C/E do lote D%d: %s (esperado %s)' % (n, (c, e), CE[n]))
        ts = sum(canon[n][x]['ts'] for x in ids); nv = sum(meta[x]['volatil'] for x in ids); ap = len(ids) - nv
        w('| D%d | %d | %d | %d | %d | %d | 0 | %d |' % (n, len(ids), c, e, ts, nv, ap))
        tot.update(n=len(ids), c=c, e=e, ts=ts, nv=nv, ap=ap)
    w('| Total | %d | %d | %d | %d | %d | 0 | %d |' % (tot['n'], tot['c'], tot['e'], tot['ts'], tot['nv'], tot['ap']))
    w('')
    w('Os 410 itens são AUTORAL, de aderência "direta"; nenhum é PARCIAL. Os 5 VOLÁTEIS são D2-01 e D2-28 (lote D2), D6-09, D6-32 e D6-34 (lote D6); os demais lotes não têm item VOLÁTIL. Nenhum item de banco com itemEdital P1-DA está nestes totais: os 38 itens de banco (BQ-0113 a BQ-0152, fora BQ-0131 e BQ-0133, anuladas) ficam fora da v1.13 e entram por D1 própria da GBQ (T-118 (d); T-123).')
    w('')
    w('## 3. Formatos (campo "Formato" do canônico, pelo código de 3 letras; a GBQ toma o código, T75_reconciliacao, 5.5, ponto 5)')
    for n in (2, 3, 4, 5):
        c = collections.Counter(canon[n][x]['formato'] for x in canon[n])
        if None in c: falha('item sem campo Formato em D%d' % n)
        w('- lote D%d: %s.' % (n, '; '.join('%s %d' % (k, c[k]) for k in FORMATO_NOME if c[k])))
    w('- lotes D1 e D6: o canônico não traz o campo "Formato" por item (só "Mecanismo"); formato não classificado neste adendo.')
    w('- Códigos: %s.' % '; '.join('%s = %s' % (k, v) for k, v in FORMATO_NOME.items()))
    w('')
    w('## 4. Ids vagos (não reutilizáveis; fora do pacote)')
    w('- Vagos: %s.' % ', '.join(vagos))
    w('- Numeração contínua nos lotes D1, D2, D4 e D6 (D1-01 a D1-60; D2-01 a D2-80; D4-01 a D4-79; D6-01 a D6-50). No lote D3: D3-01 a D3-81, com 10 vagos (71 itens). No lote D5: D5-01 a D5-71, com 1 vago (70 itens).')
    w('')
    w('## 5. Regras')
    rest = [x for x in meta if x not in VOLATEIS]
    w('- R1 (VOLÁTIL; inaptos a simulado final até a reverificação de 4–8/1/2027; reabertura obrigatória da URL): %d ids: %s.' % (len(VOLATEIS), ', '.join(VOLATEIS)))
    w('- REVERIFICAR (T-120): D2-01 (CF, art. 37, XVI, b, redação da EC 138/2025) e D2-28 (Decreto 12.374/2025, art. 21, § 1º) entram também como REVERIFICAR; D6-09, D6-32 e D6-34 são REVERIFICAR no canônico do lote D6 (D-LOTED6-CANONICO).')
    w('- R4-b (aderência PARCIAL; só simulado diagnóstico, D-ADERENCIA): 0 ids.')
    w('- R6 (conferência de base em janeiro de 2027, sem efeito de VOLÁTIL): os demais %d itens.' % len(rest))
    w('')
    w('## 6. Restrições de montagem (remissões; o texto está nos arquivos)')
    w('- lote D1: saida/gcb/T73_reconciliacao_2026-10-17.md (seções 2 e 4) e o bloco à GCB da seção 8 de saida/gcb/D1_v2.md.')
    w('- lote D2: saida/gcb/T75_reconciliacao_2026-10-20.md, seção 5.5 (pares próximos fora do mesmo simulado; moldura do Legislativo; termo absoluto; REVERIFICAR D2-01 e D2-28; formato).')
    w('- lote D3: saida/gcb/T76_reconciliacao_2026-10-20.md, seção 4.5.')
    w('- lote D4: saida/gcb/T77_reconciliacao_2026-10-20.md, seção 5.5.')
    w('- lote D5: D1 da T-74, saida/gcb/T74_reconciliacao_2026-10-20.md (seção 2, ponto 20, moldura do Legislativo; seção 5.5, notas à GBQ).')
    w('- lote D6: saida/gcb/T101_reconciliacao_2026-10-18.md (seções 2 a 4 e 6).')
    w('- Nenhum dos 410 itens DA entra em simulado nesta versão: a composição dos simulados fica inalterada; o diagnóstico de 30 itens de DA (D-DIAG30-DA) é o único uso, fora de `simulados`.')
    w('- Os 5 VOLÁTEIS nunca antes da reverificação de 4–8/1/2027.')
    w('')
    w('## 7. Regra de qualificação "lote D<n>" (achado 4 do QA final; D1-V1210-06)')
    w('- Os ids de lote D1 a D5 coincidem com os ids das discursivas D1 a D5; o id é único por lista (`lotes[].id` × `discursivas[].id`), e nenhum id novo repete o da outra lista.')
    w('- Fora da plataforma, o id vai sempre qualificado: "lote D<n>" (e "discursiva D<n>"). Na edição .md do estudante, os arquivos se chamam DA_D<n>_estudo.md, DA_D<n>_itens.md e DA_D<n>_gabarito.md. O id de lote não é exibido nem exportado pela plataforma. Não se renomeia.')
    w('')
    w('## 8. Identificadores reservados')
    w('- Os ids D<n>-R<nn> (reforço de DA) ficam reservados à T-116, continuando a numeração por lote, com gatilho A e aceite próprios; recebem o ato de aceite da leva correspondente no `nucleo` (a incluir no gerador da v1.14, T-123).')
    w('')
    w('## 9. Itens por folha (ids; na ordem do edital)')
    ed = [e['id'] for e in pac['edital'] if e['id'].startswith('P1-DA-')]
    tot_f = 0
    for f_ in ed:
        ids = sorted((x for x in meta if meta[x]['folha'] == f_), key=lambda x: (int(x[1]), int(x[3:])))      # ordem numérica do id (contrato v1.2.10, ponto 3)
        if ids:
            tot_f += len(ids); w('- %s (%d): %s' % (f_, len(ids), ', '.join(ids)))
    if tot_f != 410: falha('itens por folha somam %d' % tot_f)
    w('')
    w('## 10. Registros de formato (para DA, fazem o papel do registro de alterações por id; contrato v1.2.10, ponto 2)')
    for n in CANON:
        rf = sha((DA / ('D%d_registro_formato.md' % n)).read_bytes())
        if n == 6 and rf != '7998cc7be19676125ba13bdcc7f52537012488371ec8e1f9e01aa916b09890ca': falha('registro de formato do lote D6 difere do conferido pela gcb-cqfp')
        w('- lote D%d: saida/gcb/DA_plataforma/D%d_registro_formato.md (SHA-256 %s)' % (n, n, rf))
    w('- Errata de forma do achado 10 (T-118): lote D6, par 0, campo `como`, deleção de negrito; registrada na seção "Errata de forma — T-118 (achado 10), 20/10/2026" do registro de formato do lote D6 e conferida pela gcb-cqfp (saida/gcb/QA_D6_achado10_conferencia_2026-10-20_gcb-cqfp.md). Nenhum id, enunciado ou gabarito mudou.')
    txt = '\n'.join(L) + '\n'
    (OUT / 'registro_adendo5.md').write_text(txt, encoding='utf-8', newline='\n')
    print('registro_adendo5.md: %d linhas; %d itens; VOLÁTEIS %d; PARCIAIS 0; SHA-256 %s' % (len(L), tot_f, len(VOLATEIS), sha(txt.encode('utf-8'))))


if __name__ == '__main__':
    main()
