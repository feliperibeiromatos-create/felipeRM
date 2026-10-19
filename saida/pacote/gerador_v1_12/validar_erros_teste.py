# -*- coding: utf-8 -*-
"""v1.11: subprocessos em modo UTF-8 (-X utf8; o Windows usa cp1252 por padrão). T-59 (d) — teste do validador `validar_erros.py` (arquivo "Exportar meus erros", formato camara2026.erros v1).
Casos: o exemplo mínimo da D-T59-04 (saida/pacote/exemplo_erros_v1.json), um arquivo válido com ids reais do pacote gerado (out/pacote.json), 3 casos inválidos (versão do formato
desconhecida; campo ausente e tipo errado; JSON truncado), um caso aceito com incoerências (D-T59-05) e a detecção de DUPLICADO. Cada caso é gravado em out/casos_erros/ e validado por
`python3 -I validar_erros.py` (processo separado: confere também o código de saída). Saída: uma linha OK/FALHA por conferência; código 1 se houver falha.
Só escreve em out/ (dados fictícios; nenhum dado da candidata)."""
import copy, hashlib, json, os, subprocess, sys
from common import HERE, OUT, REPO
import validar_erros as V

CASOS = os.path.join(OUT, 'casos_erros'); os.makedirs(CASOS, exist_ok=True)
PAC = os.path.join(OUT, 'pacote.json')
pacote = json.load(open(PAC, encoding='utf-8'))
EX = os.path.join(REPO, 'saida', 'pacote', 'exemplo_erros_v1.json')
ex = json.load(open(EX, encoding='utf-8'))
res = []
def chk(nome, ok, det=''):
    res.append(bool(ok)); print(('OK    ' if ok else 'FALHA ') + nome + (' | ' + det if det else ''))
def grava(nome, obj=None, raw=None):
    p = os.path.join(CASOS, nome)
    open(p, 'wb').write(raw if raw is not None else (json.dumps(obj, ensure_ascii=False, indent=1) + '\n').encode('utf-8'))
    return p
def cli(p, *extra):
    r = subprocess.run([sys.executable, '-X', 'utf8', '-I', os.path.join(HERE, 'validar_erros.py'), p, '--pacote', PAC, '--json'] + list(extra), capture_output=True, text=True, encoding='utf-8')
    return r.returncode, (json.loads(r.stdout) if r.stdout.strip() else None), r.stderr

# 1. o exemplo da decisão (ids fictícios: tudo desconhecido)
rc, R, _ = cli(EX)
chk('exemplo D-T59-04: ACEITO (código 0), forma e tipos ok, 0 incoerência', rc == 0 and R['veredito'] == 'ACEITO' and not R['incoerencias'], R['veredito'])
chk('exemplo: ids desconhecidos listados por campo, com ocorrências (caderno XX-0001; det XX-0001 e XX-0002; discursivas DX)',
    {k: sorted(v['ids']) for k, v in R['ids_desconhecidos'].items()} == {'caderno': ['XX-0001'], 'tentativas[].det': ['XX-0001', 'XX-0002'], 'discursivas': ['DX']}
    and R['ids_desconhecidos']['tentativas[].det']['ocorrencias'] == 2)
chk('exemplo: pacote de origem ≠ vigente registrado (aviso), SHA-256 do arquivo = %s…' % hashlib.sha256(open(EX, 'rb').read()).hexdigest()[:12],
    R['pacote_origem']['igual'] is False and any('pacote de origem ≠ vigente' in a for a in R['avisos']) and R['sha256'] == hashlib.sha256(open(EX, 'rb').read()).hexdigest())

# 2. arquivo válido com ids reais do pacote
it = pacote['itens']; ids = [i['id'] for i in it[:3]]
va = copy.deepcopy(ex)
va['pacote'] = {'nome': pacote['nome'], 'geradoEm': pacote['geradoEm'], 'versao': pacote['versao'], 'origem': 'publicado'}
va['caderno'] = [{'id': ids[0], 'itemEdital': it[0]['itemEdital'], 'noPacote': True, 'errou': 2, 'seq': 0, 'desde': '2026-10-15T10:00:00.000Z'},
                 {'id': 'OUTRO-PACOTE-9', 'itemEdital': None, 'noPacote': False, 'errou': 1, 'seq': 1, 'desde': '2026-10-15T10:00:00.000Z'}]
va['resumo'].update(itensNoCaderno=2, tentativas=1)
va['tentativas'] = [{'tipo': 'sim', 'ref': pacote['simulados'][0]['id'], 'nome': 'Simulado', 'modulo': None, 'data': '2026-10-15T10:00:00.000Z', 'seg': 60, 'total': 3, 'nota': 0, 'ac': 1, 'er': 1, 'br': 1,
                     'por': {it[0]['itemEdital']: {'c': 1, 'e': 1, 'b': 1}},
                     'det': [{'id': ids[0], 'r': 'C', 'st': 'c' if it[0]['gabarito'] == 'C' else 'e'}, {'id': ids[1], 'r': 'E', 'st': 'e' if it[1]['gabarito'] == 'C' else 'c'}, {'id': ids[2], 'r': None, 'st': 'b'}]}]
t = va['tentativas'][0]; t['ac'] = sum(d['st'] == 'c' for d in t['det']); t['er'] = sum(d['st'] == 'e' for d in t['det']); t['nota'] = t['ac'] - t['er']
t['por'] = {it[0]['itemEdital']: {'c': t['ac'], 'e': t['er'], 'b': t['br']}}
va['discursivas'][0].update(id=pacote['discursivas'][0]['id'], tipo=pacote['discursivas'][0]['tipo'])
rc, R, _ = cli(grava('valido_ids_reais.json', va))
chk('arquivo válido com ids reais: ACEITO; pacote de origem IGUAL ao vigente; só o id fora do pacote ("OUTRO-PACOTE-9") é desconhecido; 0 incoerência; 0 aviso',
    rc == 0 and R['pacote_origem']['igual'] and list(R['ids_desconhecidos']) == ['caderno'] and list(R['ids_desconhecidos']['caderno']['ids']) == ['OUTRO-PACOTE-9'] and not R['incoerencias'] and not R['avisos'],
    'avisos %s; incoerências %s' % (R['avisos'], R['incoerencias']))

# 3. três casos inválidos (RECUSADO, código 1)
a = copy.deepcopy(ex); a['versaoFormato'] = 2
rc, R, _ = cli(grava('invalido_A_versaoFormato2.json', a))
chk('INVÁLIDO A (versaoFormato 2): RECUSADO (código 1) com o motivo "versão 2 desconhecida"', rc == 1 and R['veredito'] == 'RECUSADO' and any('versaoFormato' in m and '2' in m for m in R['motivos_recusa']), '; '.join(R['motivos_recusa']))
b = copy.deepcopy(ex); del b['resumo']; b['tentativas'][0]['seg'] = '600'; b['discursivas'][0]['notas']['1'] = 0.3
rc, R, _ = cli(grava('invalido_B_campo_ausente_e_tipo.json', b))
chk('INVÁLIDO B (resumo ausente, seg como string, nota 0.3 fora da escala): RECUSADO (código 1) com 3 motivos',
    rc == 1 and R['veredito'] == 'RECUSADO' and len(R['motivos_recusa']) == 3 and any('$.resumo' in m for m in R['motivos_recusa']) and any('seg' in m for m in R['motivos_recusa']) and any('notas' in m for m in R['motivos_recusa']), ' || '.join(R['motivos_recusa']))
raw = open(EX, 'rb').read(); c = raw[:len(raw) // 2]
rc, R, _ = cli(grava('invalido_C_json_truncado.json', raw=c))
chk('INVÁLIDO C (JSON truncado): RECUSADO (código 1) "não abre como JSON UTF-8"', rc == 1 and R['veredito'] == 'RECUSADO' and R['motivos_recusa'][0].startswith('não abre como JSON UTF-8'))
rc, R, _ = cli(grava('invalido_C2_formato_errado.json', dict(ex, formato='outro.formato')))
chk('INVÁLIDO C2 (formato diferente): RECUSADO', rc == 1 and R['veredito'] == 'RECUSADO' and any('formato' in m for m in R['motivos_recusa']))

# 4. aceito com incoerências (D-T59-05): listadas com o motivo e fora dos cálculos
d = copy.deepcopy(ex); d['tentativas'][0]['ac'] = 2; d['tentativas'][0]['nota'] = 5; d['caderno'][0]['errou'] = 0; d['resumo']['itensNoCaderno'] = 4
rc, R, _ = cli(grava('incoerente_D.json', d))
mot = ' | '.join('%s %s' % (c_, m) for c_, m in R['incoerencias'])
chk('INCOERENTE D (ac+er+br≠total, nota≠ac−er, soma de `por`≠ac, errou 0, itensNoCaderno≠len): ACEITO com tentativa 0 e caderno 0 fora dos cálculos',
    rc == 0 and R['veredito'] == 'ACEITO' and R['fora_dos_calculos'] == {'tentativas': [0], 'caderno': [0]} and 'ac+er+br=3, total=2' in mot and 'nota=5, ac-er=1' in mot and 'soma de por' in mot and 'errou=0' in mot and 'itensNoCaderno' in mot
    and R['contagens']['tentativas_validas'] == 0, '%d incoerências' % len(R['incoerencias']))

# 5. duplicado
sha = hashlib.sha256(open(EX, 'rb').read()).hexdigest()
reg1 = grava('importados_sha.json', [{'sha256': sha, 'exportadoEm': '2000-01-01T00:00:00.000Z'}])
reg2 = grava('importados_exportadoEm.json', [{'sha256': 'x', 'exportadoEm': ex['exportadoEm']}])
rc1, R1, _ = cli(EX, '--importados', reg1); rc2, R2, _ = cli(EX, '--importados', reg2)
chk('DUPLICADO por SHA-256 e por exportadoEm (código 3); sem registro, ACEITO', rc1 == 3 == rc2 and R1['veredito'] == R2['veredito'] == 'DUPLICADO', '%s / %s' % (R1['motivos_recusa'][0], R2['motivos_recusa'][0]))

# 6. somente leitura e código 2 de uso
rc, _, err = subprocess.run([sys.executable, '-X', 'utf8', '-I', os.path.join(HERE, 'validar_erros.py')], capture_output=True, text=True, encoding='utf-8').returncode, None, ''
chk('sem argumento: código 2 (uso)', rc == 2)
chk('o exemplo e o pacote não foram alterados pelo validador (SHA-256 do exemplo igual)', hashlib.sha256(open(EX, 'rb').read()).hexdigest() == sha)
print('\n%d conferências; %d falhas' % (len(res), res.count(False)))
sys.exit(1 if False in res else 0)
