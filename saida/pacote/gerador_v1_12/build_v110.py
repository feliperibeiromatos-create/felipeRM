# -*- coding: utf-8 -*-
"""T-104 — gerador do pacote.json v1.10 (ocorrência da T-12 que consolida as ondas 2 e 3; D-REFORCO-2; D-ABSORCAO-V110; D-ABSORCAO-V110-E). Passo 1 do rodar_tudo.sh da v1_10.
Base: o pacote.json v1.9 ACEITO (D-PACOTE-V19), lido do git no commit C_V19 (refs.py) e conferido pelo SHA-256 aceito. Nada é regenerado a partir das fontes dos lotes
canônicos (o que também fixa o L4-11 da v1.8, ponto (c) da D-ABSORCAO-V110). Mudanças, e só elas (D1 da GBQ, saida/pacote/T104_D1_v1_10_2026-10-18.md, seção 1):
  (a1) itens[5C-08].justificativa: a errata T-83 do Lote 5-C v1.2 (D-TRANSPORTE-L5C-T83), 1 ocorrência;
  (a2) lotes[L2].curso: a errata T-84 (D-L2-T84-ERRATA), 1 ocorrência;
  (e1) discursivas[D3].padrao: aspecto (xv) (D-T106-XV-ERRATA), 1 ocorrência, se config.E_PADRAO;
  (e2) lotes[L2].curso: errata T-106 do 2.8, "Riscos", 1 ocorrência (1 linha por 3), se config.E_CURSO;
  (b+) os 225 itens novos (reforco_v110.py) ao FIM de `itens`: L6B-R01/R02, onda 2 (111), L1-R131, onda 3 (111);
  `nome` "… (v1.10)"; `geradoEm` = config.GERADO_EM.
Cada troca é conferida contra o arquivo canônico de origem (SHA-256 e presença do texto novo). Saídas: out/pacote.json e out/stats_v110.json. Não lê relógio."""
import collections, hashlib, json, os
from common import OUT, P as PATH
import refs, reforco_v110 as rf, config_v110 as cfg

SHA_V19 = '1366055496457792bf55f541d901e2d1f277ee42611060b03bbf82b4427610bb'
FONTE = {
    '5C': ('saida/gcb/GCB_Lote5C_v1_GCB-CPP.md', '480c52c9dbac12715763bd98cb811039f9394199ac372e639a035485cd5fa959', 'crlf'),   # D-TRANSPORTE-L5C-T83 (SHA do arquivo CRLF aceito)
    'L2': ('saida/gce/GCE_Lote2_v2_CPP.md', '27ef5dc0ed702bf63766a422f9078d1748f37115f09d1b9a55265c7243dbacf4', 'lf'),      # com T-84 e T-106 (conferido pelo orquestrador, ab3d09f)
    'D3': ('saida/gce/GCE_Lote2_padroes_GCE.md', '4f3dde8e7e48bffeb562868d704935943a8aaec9fa92cc8dd41d4d32c684e6a0', 'lf'),  # D-T106-XV-ERRATA
}
TROCAS = collections.OrderedDict()
TROCAS['a1'] = ('itens', '5C-08', 'justificativa', 'É o item deste lote mais próximo de um canônico (A5-20):', 'É, entre os itens 5C, o mais próximo do item A5-20:', '5C')
TROCAS['a2'] = ('lotes', 'L2', 'curso', 'pegadinha do título do edital: ver Lote 1-C.', 'pegadinha do título do edital: ver o complemento do Lote 1 (adendo ao 1.4).', 'L2')
TROCAS['e1'] = ('discursivas', 'D3', 'padrao', '      corrige sotaque nem ruído;', '      trata a causa acústica (ruído, sotaque), que pede dados acústicos;', 'D3')
TROCAS['e2'] = ('lotes', 'L2', 'curso', '   adaptação não corrige sotaque nem ruído.',
                '   adaptação não remove o ruído nem trata a causa acústica (sotaque pede\n   dados acústicos), embora possa melhorar o reconhecimento dos termos\n'
                '   esperados quando o áudio é ruidoso ou pouco claro.', 'L2')
ATIVAS = ['a1', 'a2'] + (['e1'] if cfg.E_PADRAO else []) + (['e2'] if cfg.E_CURSO else [])


def fonte(k):
    rel, sha, modo = FONTE[k]
    raw = open(PATH(rel), 'rb').read()
    b = raw.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n') if modo == 'crlf' else raw
    h = hashlib.sha256(b).hexdigest()
    assert h == sha, '%s: SHA-256 %s != aceito %s' % (rel, h, sha)
    return raw.decode('utf-8').replace('\r\n', '\n')


def aplica(P):
    log = []
    for k in ATIVAS:
        bloco, oid, campo, old, new, fk = TROCAS[k]
        src = '\n'.join(l for l in fonte(fk).split('\n') if not l.startswith('|'))      # fora das linhas de tabela (Tabela de Correções cita o antes e o depois)
        assert src.count(new) == 1 and old not in src, '%s: texto novo ausente da fonte canônica %s (ou o antigo ainda presente)' % (k, FONTE[fk][0])
        obj = [x for x in P[bloco] if x['id'] == oid]
        assert len(obj) == 1, k
        v = obj[0][campo]
        assert v.count(old) == 1 and v.count(new) == 0, '%s: %s[%s].%s com %d ocorrência(s) do texto antigo' % (k, bloco, oid, campo, v.count(old))
        obj[0][campo] = v.replace(old, new)
        log.append('%s: %s[%s].%s, 1 troca' % (k, bloco, oid, campo))
    return log


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    raw = refs.git_show(refs.C_V19, refs.PACOTE)
    assert hashlib.sha256(raw).hexdigest() == SHA_V19, 'base v1.9 do git com SHA-256 diferente do aceito'
    P = json.loads(raw.decode('utf-8'), object_pairs_hook=collections.OrderedDict)
    assert json.dumps(P, ensure_ascii=False, indent=1) + '\n' == raw.decode('utf-8'), 'base v1.9 não é a serialização canônica'
    assert len(P['itens']) == 334 and P['nome'] == 'Câmara 2026 — pacote F4 (v1.9)' and P['geradoEm'] == '2026-10-18'
    l411 = [i for i in P['itens'] if i['id'] == 'L4-11'][0]['justificativa']
    assert 'O F4 afirma que' in l411 and 'What is Machine Learning?' not in l411, 'L4-11 não é o texto da v1.8 (D-ABSORCAO-V110 (c))'
    log = aplica(P)
    novos, meta = rf.carrega()
    assert not {i['id'] for i in P['itens']} & {i['id'] for i in novos}, 'id novo já existe na v1.9'
    P['geradoEm'] = cfg.GERADO_EM
    P['nome'] = cfg.NOME
    P['itens'] = P['itens'] + novos
    txt = json.dumps(P, ensure_ascii=False, indent=1) + '\n'
    with open(os.path.join(OUT, 'pacote.json'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(txt)
    stats = collections.OrderedDict(base=dict(commit=refs.C_V19, sha256=SHA_V19, itens=334), modo=dict(E_CURSO=cfg.E_CURSO, E_PADRAO=cfg.E_PADRAO, GERADO_EM=cfg.GERADO_EM),
                                    trocas=log, reforco=meta, log=rf.LOG,
                                    arquivos={gk: [dict(arquivo=a, sha256=s, ids=len(ids)) for a, s, ids in g['arquivos']] for gk, g in rf.G.items()},
                                    size=len(txt.encode('utf-8')))
    with open(os.path.join(OUT, 'stats_v110.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(stats, f, ensure_ascii=False, indent=1)
        f.write('\n')
    c = collections.Counter(i['gabarito'] for i in P['itens'])
    print('itens', len(P['itens']), '(334 da v1.9 + %d novos)' % len(novos), 'C/E %d/%d' % (c['C'], c['E']), 'volatil', sum(1 for i in P['itens'] if i.get('volatil')),
          'parcial', sum(1 for i in P['itens'] if i['aderencia'] == 'parcial'), 'bytes', len(txt.encode('utf-8')), 'sha256', hashlib.sha256(txt.encode('utf-8')).hexdigest())
    print('modo: E_CURSO=%s E_PADRAO=%s' % (cfg.E_CURSO, cfg.E_PADRAO))
    print('trocas:', log)
    print('LOG:', rf.LOG)
