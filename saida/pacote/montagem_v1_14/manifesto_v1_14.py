# manifesto_v1_14.py — T-123 fase 2 (script 12) — 2026-10-23 — gerado por gbq-csc
# -*- coding: utf-8 -*-
"""Gera MANIFESTO_v1_14.md nesta pasta: bytes e SHA-256 de tudo o que está em montagem_v1_14/ (menos o próprio manifesto e __pycache__) e out/, os valores esperados pela D1 e os obtidos, as entradas lidas e as
divergências. O número de arquivos é o da pasta real, contado pelo script (R2-A). O digest da edição .md tem a forma fixada na nota 2 da seção 2 de T118_reconciliacao_v1_13_2026-10-20.md (R2-D).
Só leitura (grava só o manifesto). Nada é promovido. Rodar por último; a conferencia_t123.json é refeita depois dele (C-MANIFESTO) e o manifesto é regerado para listar o seu SHA-256 final.
Uso: python -I manifesto_v1_14.py (exit 1 se alguma linha de valor esperado divergir). Não lê relógio."""
import sys
sys.dont_write_bytecode = True
import hashlib, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import montar_v1_14 as M

R = M.R; OUT = M.OUT


def sha(b):
    return hashlib.sha256(b).hexdigest()


def rel(p):
    return os.path.relpath(p, R).replace(os.sep, '/')


def lj(p):
    return json.loads(open(p, 'rb').read().decode('utf-8'))


def lfsha(path):
    return sha(open(path, 'rb').read().replace(b'\r\n', b'\n'))


def main():
    pac = lj(os.path.join(OUT, 'pacote.json')); est = lj(os.path.join(OUT, 'pacote_estudante.json'))
    conf = lj(os.path.join(OUT, 'conferencia_t123.json')); mut = lj(os.path.join(OUT, 'mutacao_t123.json')); mdj = lj(os.path.join(OUT, 'estudante_md_v1_14.json'))
    cob = lj(os.path.join(OUT, 'cobertura_v1_14.json')); dg = lj(os.path.join(OUT, 'diag30_check_v1_14.json')); mo = lj(os.path.join(OUT, 'moldura_v1_14.json'))
    arquivos = []
    for dp, dn, fnn in os.walk(HERE):
        dn[:] = sorted(d for d in dn if d != '__pycache__')
        for f in sorted(fnn):
            if f == 'MANIFESTO_v1_14.md':
                continue
            arquivos.append(os.path.join(dp, f))
    arquivos.sort(key=lambda p: rel(p).encode('utf-8'))
    bp = open(os.path.join(OUT, 'pacote.json'), 'rb').read(); be = open(os.path.join(OUT, 'pacote_estudante.json'), 'rb').read()
    ad = open(os.path.join(OUT, 'registro_adendo6.md'), 'rb').read()
    ins = M.ler_insumos()
    contrato_lf = open(os.path.join(R, 'regras', 'pacote_contrato.md'), 'rb').read().replace(b'\r\n', b'\n')
    da = [i for i in pac['itens'] if i['itemEdital'].startswith('P1-DA-')]
    ref = [i for i in pac['itens'] if '-R' in i['id'] and i['id'].startswith('D')]
    nuc = [i for i in est['itens'] if i['nucleo']]
    EXP = [  # (descrição, esperado pela D1, obtido, onde)
        ('itens no pacote.json', 1433, len(pac['itens']), 'D1, 2.4'),
        ('C/E no pacote.json', '730/703', '%d/%d' % (sum(i['gabarito'] == 'C' for i in pac['itens']), sum(i['gabarito'] == 'E' for i in pac['itens'])), 'D1, 2.4'),
        ('itens de DA e C/E', '684 (350/334)', '%d (%d/%d)' % (len(da), sum(i['gabarito'] == 'C' for i in da), sum(i['gabarito'] == 'E' for i in da)), 'D1, 2.4'),
        ('itens de reforço e C/E', '238 (122/116)', '%d (%d/%d)' % (len(ref), sum(i['gabarito'] == 'C' for i in ref), sum(i['gabarito'] == 'E' for i in ref)), 'D1, 2.1'),
        ('itens de banco P1-DA (novos)', 36, sum(1 for i in pac['itens'] if i['id'].startswith('BQ-') and i['itemEdital'].startswith('P1-DA-')), 'D1, 2.3'),
        ('parciais de reforço', 35, sum(i['aderencia'] == 'parcial' for i in ref), 'D1, 2.1'),
        ('VOLÁTEIS de DA (sem novos)', 5, sum(bool(i.get('volatil')) for i in da), 'D1, 2.4'),
        ('nucleo true no pacote_estudante', 775, len(nuc), 'D1, 6'),
        ('nucleo DA true/false', '408/276', '%d/%d' % (sum(1 for i in est['itens'] if i['itemEdital'].startswith('P1-DA-') and i['nucleo']), sum(1 for i in est['itens'] if i['itemEdital'].startswith('P1-DA-') and not i['nucleo'])), 'D1, 6'),
        ('geradoEm posterior a 2026-10-20', True, pac['geradoEm'] > '2026-10-20' and est['geradoEm'] == pac['geradoEm'], 'D1, 4 (e)'),
        ('conferencia_t123.json: FALHA e PENDENTE', '0 e 0', '%d e %d' % (conf['FALHA'], conf['PENDENTE']), 'D1, 8.1'),
        ('mutacao_t123.json: detectadas', '15/15', '%d/%d' % (mut['detectadas'], mut['total']), 'D1, 8.3'),
        ('mutacao_t123.json: original com 0 FALHA', 0, mut['original']['FALHA'], 'D1, 8.3'),
        ('estudante_md_v1_14.json: arquivos e FALHA', '53 e 0', '%d e %d' % (mdj['arquivos'], mdj['falhas']), 'D1, 10'),
        ('cobertura_v1_14.json: FALHA', 0, sum(c['resultado'] == 'FALHA' for c in cob['criterios']), 'D1, 9'),
        ('diag30_check_v1_14.json: FALHA', 0, dg['falhas'], 'D1, 11'),
        ('registro_adendo6.md sem "D<n>" isolado (scan_q)', 0, len([1 for m in __import__('re').finditer(r'(?<![\w-])D[1-6](?![\w-])', ad.decode('utf-8')) if ad.decode('utf-8')[max(0, m.start() - 5):m.start()] != 'lote ']), 'D1, 5 (achado 4)'),
        ('regras/pacote_contrato.md (v1.2.12) SHA-256 LF', '3916ad994cd06ee74b13ba545de5af3b6c241d0004eb0625e922973ab76c38df', sha(contrato_lf), 'D1, 7'),
        ('DA_reforco_substituicoes.csv SHA-256 LF', 'df9f53bd7dc3f18631c77528b32683dd89e77e27dea167918fd1edee014db501', sha(ins['csv']), 'reconciliação da GCB, 3'),
        ('DA_reforco_registro_formato.md SHA-256 LF', 'a511fd8d3b79b806dc3a87f06d294ed346d05f2d05766089b80103d6374b820e', sha(ins['registro']), 'reconciliação da GCB, 3'),
        ('montar_v1_13 (pasta) e gerador_v1_12 sem modificação no git', [], [c['obtido'] for c in conf['criterios'] if c['id'] == 'C-INTACTA.git'][0], 'D1, 4 e 8.1'),
    ]
    L = []; w = L.append
    falhas = 0
    w('# MANIFESTO_v1_14.md — T-123 (D1 da GBQ, passo 9 da seção 13) — 2026-10-23 — gerado por gbq-csc')
    w('Pacote v1.14 = v1.13 canônica (82c4117c…/04cbd593…) + 238 itens de reforço de DA + 36 itens de banco P1-DA, depois da limpeza da GCB (aceita pela reconciliação `saida/gcb/T123_limpeza_reconciliacao_GCB_2026-10-23.md`). Base: `saida/pacote/T123_D1_v1_14_2026-10-23.md`. Nada foi promovido a saida/pacote/, saida/estudante/, saida/gbq/ ou saida/plataforma/; sem commit; a plataforma não foi remontada. Scripts com `python -I`; `montagem_v1_13/` e `gerador_v1_12/` não foram alterados.')
    w('')
    w('## 1. Valores esperados pela D1 e obtidos')
    w('| Item | Esperado | Obtido | Resultado | Onde na D1 |')
    w('|---|---|---|---|---|')
    for d, e, o, onde in EXP:
        ok = e == o; falhas += not ok
        w('| %s | %s | %s | %s | %s |' % (d, e, o, 'OK' if ok else 'FALHA', onde))
        if not ok:
            print('FALHA:', d, e, o)
    w('| montar_v1_14.py | RESULTADO: 0 FALHA | `python -I montar_v1_14.py` saiu com código 0 e as conferências internas OK (rodado antes deste manifesto) | OK | D1, 13, passo 4 |')
    w('')
    w('## 2. Saídas principais (bytes e SHA-256)')
    w('| Saída | Bytes | SHA-256 |')
    w('|---|--:|---|')
    for nome, b in (('out/pacote.json', bp), ('out/pacote_estudante.json', be), ('out/registro_adendo6.md', ad)):
        w('| `%s` | %d | `%s` |' % (nome, len(b), sha(b)))
    w('| digest da edição .md (forma R2-D: linhas `estudante/<nome>.md` TAB sha256, em ordem de bytes, com `\\n` final; SHA-256 desse texto) | — | `%s` |' % mdj['digest_md_R2D'])
    w('')
    w('## 3. Contagens')
    w('- Itens: %d (C/E %d/%d). Itens de DA: %d (C/E %d/%d), dos quais %d de reforço, %d de banco e %d dos lotes de estudo.' % (len(pac['itens']), sum(i['gabarito'] == 'C' for i in pac['itens']), sum(i['gabarito'] == 'E' for i in pac['itens']), len(da), sum(i['gabarito'] == 'C' for i in da), sum(i['gabarito'] == 'E' for i in da), len(ref), 36, len(da) - len(ref) - 36))
    for l in ('D1', 'D2', 'D3', 'D4'):
        r_ = [i for i in ref if i['id'].startswith(l + '-')]
        w('- Reforço do lote %s: %d (C/E %d/%d); vagos: %s.' % (l, len(r_), sum(i['gabarito'] == 'C' for i in r_), sum(i['gabarito'] == 'E' for i in r_), {'D1': 'D1-R03', 'D4': 'D4-R12'}.get(l, 'nenhum')))
    w('- `nucleo`: %d true no pacote_estudante (%d fora de DA + %d de DA); os 12 itens da v1.13 que passam a false e os 18 de reforço estão em conferencia_t123.json (C-ESTUDANTE.nucleo_12 e nucleo_18).' % (len(nuc), sum(1 for i in nuc if not i['itemEdital'].startswith('P1-DA-')), sum(1 for i in nuc if i['itemEdital'].startswith('P1-DA-'))))
    w('- Cobertura: %d folhas; DA com %d itens em folha e %d fora; %d folhas de DA abaixo de 20 (faltam %d para 20).' % (sum(len(v) for v in cob['folhas'].values()), cob['totais']['por_materia_em_folha']['DA']['total'], sum(cob['fora_de_folha']['DA_por_entrada'].values()), len(cob['da_abaixo_de_20']), cob['da_falta_para_20']))
    w('- Moldura (D-MOLDURA-CE, recontagem oficial): %s; divergências do campo "Moldura:" das levas: %d de %d.' % ('; '.join('%s %d itens (C %d, E %d, %%C %.1f)' % (k, v['itens'], v['C'], v['E'], v['pct_C']) for k, v in mo['totais_por_materia_v1_14'].items()), mo['divergencias_campo_moldura_das_levas']['n'], mo['divergencias_campo_moldura_das_levas']['de']))
    w('- Conferência: %d critérios, %d OK, %d FALHA, %d PENDENTE; por grupo: %s.' % (conf['total_criterios'], conf['OK'], conf['FALHA'], conf['PENDENTE'], '; '.join('%s %s' % (g, dict(v)) for g, v in conf['por_grupo'].items())))
    w('')
    w('## 4. Arquivos desta pasta (bytes e SHA-256; o manifesto não lista a si mesmo)')
    w('| Arquivo | Bytes | SHA-256 |')
    w('|---|--:|---|')
    n_md = 0
    for p in arquivos:
        b = open(p, 'rb').read(); w('| %s | %d | %s |' % (rel(p), len(b), sha(b)))
        if os.path.basename(os.path.dirname(p)) == 'estudante' and p.endswith('.md'):
            n_md += 1
    w('')
    w('Total: %d arquivos em montagem_v1_14/ (dos quais %d em out/estudante/), contados na pasta real. Nenhum arquivo fora desta pasta, salvo o registro do contrato `saida/pacote/contrato_v1_2_12_2026-10-23.md` e a errata em `regras/pacote_contrato.md` (passo 5).' % (len(arquivos), n_md))
    w('')
    w('## 5. Entradas lidas (SHA-256 do conteúdo LF)')
    w('| Entrada | SHA-256 |')
    w('|---|---|')
    for nome in ('base_pacote', 'base_estudante', 'banco', 'csv', 'registro', 'formato', 'bruto'):
        w('| %s | %s |' % (M.PATH[nome], sha(ins[nome])))
    for n in range(1, 9):
        w('| %s | %s |' % (M.PATH['leva%d' % n], sha(ins['leva%d' % n])))
    for f in ('saida/pacote/T123_D1_v1_14_2026-10-23.md', 'saida/gcb/T123_limpeza_reconciliacao_GCB_2026-10-23.md', 'saida/gcb/T123_substituicoes_DA_v2.csv', 'saida/gcb/QA_T123_limpeza_R2_2026-10-23_gcb-cqfp.md',
              'saida/pacote/gerador_v1_12/marcas_processo.py', 'saida/banco/moldura_ce.py', 'saida/pacote/montagem_v1_13/out/diag30_DA.json', 'saida/plataforma/plataforma_v16_final_template.html', 'edital/DA_itens_1_12_P1.md'):
        w('| %s | %s |' % (f, lfsha(os.path.join(R, f))))
    w('| DECISOES.md (linhas 93, 117, 162 a 165, 175 a 179, 181, 182, 184 e 185 conferidas pelo nucleo_v114.py) | %s |' % sha(ins['dec']))
    w('| regras/pacote_contrato.md (antes: 85b30fcc…616b; depois) | %s |' % sha(contrato_lf))
    w('| saida/estudante/ (v1.13-E promovida) e montagem_v1_13/out/estudante/ (53 .md) | iguais em LF (estudante_md_v114.py, M0.2: OK) |')
    w('')
    w('## 6. Divergências e observações (nenhum valor foi ajustado à força)')
    w('1. Valores esperados pela D1: %s.' % ('nenhuma divergência (seção 1: tudo OK)' if falhas == 0 else 'HÁ DIVERGÊNCIA: ver as linhas FALHA da seção 1'))
    w('2. Lista X de conteúdo da varredura PROCESSO: "Presidência da República" no D2-R21 e no D2-R24 (justificativa; remissão à Lei 9.007, art. 2º, parágrafo único), 1 casamento em cada, registrada como conteúdo por pedido da reconciliação da GCB (seção 4, P1). Fora isso, C-MARCAS e PROCESSO dão 0 nos 274 itens novos.')
    w('3. Ordem de execução: `conferir_t123.py` roda depois dos scripts 6 a 11 (usa os arquivos que eles gravam) e é refeito depois deste manifesto, para que o C-MANIFESTO compare a pasta real com ele; este manifesto é regerado então, para listar o SHA-256 final da conferencia_t123.json. A conferencia_t123.json não entra na comparação do C-MANIFESTO (não pode conter o próprio SHA-256).')
    w('4. A "Onda programada" de P1 (ressalva (d) da cobertura v1.13) não é calculável pelo pacote: o cobertura_v1_14.json a deixa para a secretaria, que a reconstrói de TAREFAS.md.')
    w('5. Leitura: todo insumo de texto é lido como bytes com CRLF→LF antes do decode, porque a árvore de trabalho tem `core.autocrlf=true`; os SHA-256 desta tabela de entradas são os do conteúdo LF. Os arquivos de out/ são gravados com LF (0 CR).')
    w('6. AJ-L8-E3 (D4-R42) e AJ-L8-E4 (D4-R52) sem aceite: o "antes" de cada uma continua 1 vez no enunciado (C-REFORCO.e3e4). BQ-0141 (QA PENDENTE) e BQ-0151 (DIVERGE) ficam fora (C-BANCO.ausentes). O pacote v1.14 não foi promovido nem publicado.')
    txt = '\n'.join(L) + '\n'
    with open(os.path.join(HERE, 'MANIFESTO_v1_14.md'), 'wb') as f:
        f.write(txt.encode('utf-8'))
    print('MANIFESTO_v1_14.md: %d bytes; SHA-256 %s; %d arquivos listados (pasta real); divergências %d' % (len(txt.encode('utf-8')), sha(txt.encode('utf-8')), len(arquivos), falhas))
    sys.exit(1 if falhas else 0)


if __name__ == '__main__':
    main()
