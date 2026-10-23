# diag30_check.py — T-123 fase 2 (script 11) — 2026-10-23 — gerado por gbq-csc
# -*- coding: utf-8 -*-
"""Confere o diagnóstico de 30 itens (D1 da GBQ, seção 11, requisito 4; D-DIAG30-DA): só confere, não regrava diag30_DA.json. DIAG30.DA fica com os mesmos 30 ids (lista do plataforma_v16_final_template.html =
saida/pacote/montagem_v1_13/out/diag30_DA.json, SHA-256 LF eb1ced6d…6800): os 30 ids existem em out/pacote.json; todos são DA (P1-DA-*), diretos, não voláteis e fora de `simulados`; as folhas são iguais às de diag30_DA.json;
C/E 15/15. DIAG30.P1 e DIAG30.P2: os ids continuam existindo, com os mesmos atributos (objeto igual ao da v1.13). Grava out/diag30_check_v1_14.json. Uso: python -I diag30_check.py (exit 1 se FALHA). Não lê relógio."""
import sys
sys.dont_write_bytecode = True
import collections, hashlib, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import montar_v1_14 as M

CRIT = []
SHA_DIAG = 'eb1ced6df3d624ae62b82337db6a4cfe29b86baa9494e96aed1b3defe61a6800'


def chk(cid, desc, esperado, obtido):
    ok = esperado == obtido
    CRIT.append(dict(id=cid, criterio=desc, esperado=esperado, obtido=obtido, resultado='OK' if ok else 'FALHA'))
    print(('OK    ' if ok else 'FALHA ') + cid + ' — ' + desc + ('' if ok else '  [esperado=%r obtido=%r]' % (esperado, obtido)))


def main():
    ins = M.ler_insumos()
    pac = json.loads(open(os.path.join(M.OUT, 'pacote.json'), 'rb').read().decode('utf-8'))
    base = json.loads(ins['base_pacote'].decode('utf-8'))
    bd = open(os.path.join(M.R, 'saida', 'pacote', 'montagem_v1_13', 'out', 'diag30_DA.json'), 'rb').read().replace(b'\r\n', b'\n')
    chk('G0', 'diag30_DA.json (v1.13; não regravado): SHA-256 LF', SHA_DIAG, hashlib.sha256(bd).hexdigest())
    dj = json.loads(bd.decode('utf-8'))
    tpl = open(os.path.join(M.R, 'saida', 'plataforma', 'plataforma_v16_final_template.html'), 'rb').read().replace(b'\r\n', b'\n').decode('utf-8')
    ms = re.findall(r'const DIAG30 = (\{.*?\});\n', tpl, re.S)
    chk('G1', 'o template v16 tem exatamente 1 const DIAG30, com P1, P2 e DA de 30 ids cada', [1, {'P1': 30, 'P2': 30, 'DA': 30}], [len(ms), {k: len(v) for k, v in json.loads(ms[0]).items()}] if ms else None)
    D = json.loads(ms[0])
    chk('G2', 'DIAG30.DA do template = ids de diag30_DA.json (mesmos 30 ids, mesma ordem)', dj['ids'], D['DA'])
    by = {i['id']: i for i in pac['itens']}; bb = {i['id']: i for i in base['itens']}
    sim = {x for s in pac['simulados'] for x in s['itens']}
    da = [by.get(x) for x in D['DA']]
    chk('G3', 'DA: os 30 ids existem no pacote v1.14', [], [x for x in D['DA'] if x not in by])
    chk('G4', 'DA: todos DA (P1-DA-*), diretos, não voláteis e fora de simulado', [], [x['id'] for x in da if x and not (x['itemEdital'].startswith('P1-DA-') and x['aderencia'] == 'direta' and not x.get('volatil') and x['id'] not in sim)])
    chk('G5', 'DA: folhas (itemEdital, na ordem) iguais às de diag30_DA.json', dj['folhas'], [x['itemEdital'] for x in da])
    chk('G6', 'DA: C/E 15/15', [15, 15], [sum(x['gabarito'] == 'C' for x in da), sum(x['gabarito'] == 'E' for x in da)])
    chk('G7', 'DA: cada um dos 30 é igual, como objeto, ao item da v1.13', [], [x['id'] for x in da if x['id'] not in bb or x != bb[x['id']]])
    for m in ('P1', 'P2'):
        ids = D[m]
        chk('G8.' + m, 'DIAG30.%s: os 30 ids existem e têm os mesmos atributos da v1.13 (objeto igual)' % m, [], [x for x in ids if x not in by or x not in bb or by[x] != bb[x]])
    nf = sum(c['resultado'] == 'FALHA' for c in CRIT)
    rel = collections.OrderedDict(tarefa='T-123 (D1 da GBQ, seção 11, requisito 4)', script='saida/pacote/montagem_v1_14/diag30_check.py', diag30_DA_json_regravado=False,
                                  da=dict(ids=D['DA'], folhas=dj['folhas'], C=sum(x['gabarito'] == 'C' for x in da), E=sum(x['gabarito'] == 'E' for x in da)), criterios=CRIT, falhas=nf)
    M.grava(os.path.join(M.OUT, 'diag30_check_v1_14.json'), (json.dumps(rel, ensure_ascii=False, indent=1) + '\n').encode('utf-8'))
    print('diag30_check_v1_14.json: %d conferências, %d FALHA' % (len(CRIT), nf))
    sys.exit(1 if nf else 0)


if __name__ == '__main__':
    main()
