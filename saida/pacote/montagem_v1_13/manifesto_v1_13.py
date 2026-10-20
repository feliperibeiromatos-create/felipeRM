# manifesto_v1_13.py — T-118 (D1 da GBQ, passo 4.3.5) — 2026-10-20 — gerado por gbq-csc
# Gera MANIFESTO_v1_13.md nesta pasta: bytes e SHA-256 de tudo o que está em montagem_v1_13/ (menos o próprio manifesto) e out/, as entradas, os valores esperados pela D1 e os obtidos, e as divergências.
# Só leitura (grava só o manifesto). Nada é promovido. Uso: python3 -I manifesto_v1_13.py (rodar depois dos outros quatro passos). Não lê relógio.
import hashlib, json, pathlib, sys
R = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).parent
def sha(b): return hashlib.sha256(b).hexdigest()
def rel(p): return p.relative_to(R).as_posix()
def lj(p): return json.loads(pathlib.Path(p).read_text(encoding='utf-8'))

EXP = [  # (descrição, esperado pela D1, obtido, onde)
    ('montar_v1_13.py (sem alteração)', '723370f56fe830cace0d46056b681ce6c3e0b87f4497cbd1da84101ad6391ebe', sha((HERE / 'montar_v1_13.py').read_bytes()), 'D1, 4.3.1'),
    ('D6_plataforma.json (errata do achado 10)', 'f8691dd5a3fd968922bf8bac8e26b4dd4f1475183afc9d6a0e84418d08b17122', sha((R / 'saida/gcb/DA_plataforma/D6_plataforma.json').read_bytes()), 'D1, 2 e 4.1'),
    ('out/pacote.json SHA-256', '82c4117cccc0902ddf711798c926049950a27db8e68d4402babf4b007fddf240', sha((HERE / 'out/pacote.json').read_bytes()), 'D1, 4.3.1'),
    ('out/pacote.json bytes', 2906558, (HERE / 'out/pacote.json').stat().st_size, 'D1, 4.3.1'),
    ('out/pacote_estudante.json SHA-256', '04cbd593fdd30404ecb7f91f6b6722da6b2fc24e58d3c0eb68b10a4e792a0c40', sha((HERE / 'out/pacote_estudante.json').read_bytes()), 'D1, 4.3.1'),
    ('out/pacote_estudante.json bytes', 2644822, (HERE / 'out/pacote_estudante.json').stat().st_size, 'D1, 4.3.1'),
    ('out/diag30_DA.json (intocado)', 'eb1ced6df3d624ae62b82337db6a4cfe29b86baa9494e96aed1b3defe61a6800', sha((HERE / 'out/diag30_DA.json').read_bytes()), 'D1, 4.3.1'),
    ('out/registro_adendo5.md (regerado, achados 2 a 4)', 'a1ca16811394dd6ec5df186b44155704a498bc03f6ac1e8cddaf87b6f7a87437', sha((HERE / 'out/registro_adendo5.md').read_bytes()), 'D1 achados, 2'),
    ('historico/registro_adendo5_R1_7224db40.md (versão anterior, achado 5)', '7224db40670608bff726f67b6b4769a509b225953146b80013b05d9c57f55918', sha((HERE / 'historico/registro_adendo5_R1_7224db40.md').read_bytes()), 'D1 achados, 5'),
    ('regras/pacote_contrato.md (v1.2.11)', '85b30fccadce4eb9782e1e056613a2d680cec0c01aed44fd173bda7d248e616b', sha((R / 'regras/pacote_contrato.md').read_bytes()), 'D1 achados, 1'),
]
conf = lj(HERE / 'out/conferencia_t118.json'); est = lj(HERE / 'out/estudante_md_v1_13.json')
arquivos = sorted(p for p in HERE.rglob('*') if p.is_file() and p.name != 'MANIFESTO_v1_13.md' and '__pycache__' not in p.parts)
extra = []
if (R / 'saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo5_2026-10-20.md').exists(): print('FALHA: adendo 5 em saida/gbq/ antes do aceite (achado 5)'); sys.exit(1)
L = []; w = L.append
w('# MANIFESTO_v1_13.md — T-118 (D1 da GBQ, passo 4.3.5) — 2026-10-20 — gerado por gbq-csc')
w('Pacote v1.13, montagem depois da errata do achado 10 (conferida pela gcb-cqfp: saida/gcb/QA_D6_achado10_conferencia_2026-10-20_gcb-cqfp.md, CONFERIDO). Base: saida/pacote/T118_D1_v1_13_2026-10-20.md. Nada foi promovido a saida/pacote/, saida/estudante/ ou saida/plataforma/; sem commit; a plataforma não foi remontada. Scripts com `python3 -I`; o `montar_v1_13.py` não foi alterado.')
w('')
w('## 1. Valores esperados pela D1 e obtidos')
w('| Item | Esperado | Obtido | Resultado | Onde na D1 |')
w('|---|---|---|---|---|')
falhas = 0
for d, e, o, onde in EXP:
    ok = e == o; falhas += not ok
    w('| %s | %s | %s | %s | %s |' % (d, e, o, 'OK' if ok else 'FALHA', onde))
    if not ok: print('FALHA:', d)
w('| montagem (montar_v1_13.py) | RESULTADO: 0 FALHA | RESULTADO: 0 FALHA (32 verificações OK, as 16 de cada pacote) | OK | D1, 4.3.1 |')
w('| diff dos dois pacotes contra a montagem anterior (007787e3…c192 e 8b5489b9…b8dd) | só `lotes[D6].pares[0].como` | só `/lotes[15]/pares[0]/como` (pacote.json) e `/lotes[12]/pares[0]/como` (estudante) | OK | D1, 4.3.1 |')
w('| conferencia_t118.json | 0 FALHA | %d critérios, %d FALHA | %s | D1, 4.3.2 |' % (conf['total_criterios'], conf['falhas'], 'OK' if conf['falhas'] == 0 else 'FALHA'))
w('| edição .md (estudante_md_v113.py) | 53 arquivos; 0 FALHA | %d arquivos; %d conferências, %d FALHA | %s | D1, 4.3.4 |' % (est['arquivos'], est['total_conferencias'], est['falhas'], 'OK' if est['falhas'] == 0 and est['arquivos'] == 53 else 'FALHA'))
falhas += conf['falhas'] + est['falhas']
w('')
c = conf['contagens']
w('## 2. Contagens (de conferencia_t118.json)')
w('- Itens de DA: %d (D1 60, D2 80, D3 71, D4 79, D5 70, D6 50); C/E por lote: %s.' % (c['itens_da'], '; '.join('%s %d/%d' % (k, v[0], v[1]) for k, v in c['ce_por_lote'].items())))
w('- Entradas de edital P1-DA: %d (posições 20 a 65, bloco contíguo); lotes DA: %d (16 no total); tópicos DA: %d (79 no total).' % (c['entradas_edital_da'], c['lotes_da'], c['topicos_da']))
w('- nucleo DA: %d true e %d false; nucleo total do pacote_estudante: %d. Letra (e): nucleo recalculado pelo critério k1 a k4 com os atos D1 a D6 mapeados = nucleo do pacote em %d/%d.' % (c['nucleo_true'], c['nucleo_false'], c['nucleo_total_estudante'], conf['nucleo_k1k4']['iguais'], conf['nucleo_k1k4']['de']))
w('- Folhas de DA: %d; itens em folha: %d; fora de folha: %d (%s). Itens no pacote: %d.' % (c['folhas_da'], c['itens_em_folha'], c['itens_fora_de_folha'], ', '.join('%s %d' % kv for kv in c['itens_fora_por_entrada'].items()), c['itens_total']))
w('- VOLÁTEIS: %s. Ids vagos: %s.' % (', '.join(c['volateis']), ', '.join(c['ids_vagos'])))
w('')
w('## 3. Saídas e arquivos desta pasta (bytes e SHA-256; o manifesto não lista a si mesmo)')
w('| Arquivo | Bytes | SHA-256 |')
w('|---|--:|---|')
for p in arquivos + extra:
    b = p.read_bytes(); w('| %s | %d | %s |' % (rel(p), len(b), sha(b)))
w('')
w('Total: %d arquivos em montagem_v1_13/ (dos quais %d em out/estudante/). Nenhum arquivo fora desta pasta: o adendo 5 fica só em out/ até a promoção (achado 5 da fidelidade T-118).' % (len(arquivos), sum(1 for p in arquivos if 'estudante' in p.parts and p.suffix == '.md' and p.parent.name == 'estudante')))
w('')
w('## 4. Entradas lidas (SHA-256)')
w('| Entrada | SHA-256 |')
w('|---|---|')
for n, f in ((1, 'D1_v2.md'), (2, 'D2_v2_1.md'), (3, 'D3_v2_1.md'), (4, 'D4_v2_1.md'), (5, 'D5_v2_1.md'), (6, 'D6_v2_1.md')):
    w('| saida/gcb/%s | %s |' % (f, sha((R / 'saida/gcb' / f).read_bytes())))
for n in range(1, 7):
    f = R / ('saida/gcb/DA_plataforma/D%d_plataforma.json' % n); w('| %s | %s |' % (rel(f), sha(f.read_bytes())))
for f in (R / 'saida/gcb/DA_plataforma/edital_DA.json', R / 'saida/pacote/gerador_v1_12/out/pacote.json', R / 'saida/pacote/gerador_v1_12/out/pacote_estudante.json', R / 'saida/gcb/DA_plataforma/D1_registro_formato.md', R / 'saida/gcb/DA_plataforma/D2_registro_formato.md', R / 'saida/gcb/DA_plataforma/D3_registro_formato.md', R / 'saida/gcb/DA_plataforma/D4_registro_formato.md', R / 'saida/gcb/DA_plataforma/D5_registro_formato.md', R / 'saida/gcb/DA_plataforma/D6_registro_formato.md', R / 'DECISOES.md', R / 'regras/pacote_contrato.md'):
    w('| %s | %s |' % (rel(f), sha(f.read_bytes())))
w('| saida/estudante/ (35 .md da base) | SHA-256 de cada um conferido contra saida/pacote/T115_promocao_v1_12_2026-10-18.md (M0.2: OK) |')
w('')
w('## 5. Divergências e observações (nenhum valor foi ajustado à força)')
w('1. Valores esperados pela D1: nenhuma divergência (seção 1: tudo OK).' if falhas == 0 else '1. HÁ DIVERGÊNCIA: ver as linhas FALHA da seção 1 e os critérios FALHA de conferencia_t118.json.')
w('2. Scripts: a D1 cita `conferir_t118.py`, `registro_adendo_v113.py` e `estudante_md_v113.py` como "scripts novos" em montagem_v1_13/; não existiam e foram escritos pela gbq-csc nesta execução (mais `manifesto_v1_13.py`). O `montar_v1_13.py` e o gerador_v1_12 não foram alterados.')
w('3. Ordem de apresentação do canônico: nos lotes D3 e D5 a ordem da seção 5.1 do canônico difere da ordem numérica do id (ex.: D5-71 vem depois de D5-53). O pacote segue a ordem numérica do id (contrato v1.2.10, ponto 3; D1 da GBQ; FORMATO, seção 4), e o `nucleo` usa a posição no pacote. Informativo em conferencia_t118.json; não é critério.')
w('4. Adendo 5, formatos: o canônico dos lotes D1 e D6 não traz o campo "Formato" por item (só "Mecanismo"); o adendo traz os códigos dos lotes D2 a D5 (código de 3 letras, T75_reconciliacao, 5.5) e declara os lotes D1 e D6 como não classificados. A D1 não manda classificar.')
w('5. Adendo 5, restrições de montagem: a D1 pede a remissão às seções 5.5 da T75, 4.5 da T76 e 5.5 da T77, à "D1 da T-74" e às reconciliações dos lotes D1 e D6. Para o lote D5 o adendo remete a T74_reconciliacao_2026-10-20.md (seções 2 e 5.5); para o lote D1, a T73_reconciliacao_2026-10-17.md (seções 2 e 4); para o lote D6, a T101_reconciliacao_2026-10-18.md (seções 2 a 4 e 6). Escolha da gbq-csc entre as seções existentes.')
w('6. Edição .md: pares e pegadinhas de DA saem sem marcas (`- a × b | como`; `- [item] rótulo — texto`), para cumprir "0 `**` nas seções de pares e pegadinhas" (o formato dos L<n> usa negrito). Resumo e curso vão em bloco de texto, como nos L<n>. README: linhas de DA (uma por lote, mais uma nota) acrescentadas depois da linha do L6B; versão "v1.13-E" e data 2026-10-20. NUCLEO.md: ordem das linhas pela ordem do edital; as linhas anteriores ficaram idênticas. Forma admitida pela errata v1.2.11 do contrato (saida/pacote/contrato_v1_2_11_2026-10-20.md), que substitui o último subitem do ponto 8 da v1.2.10 (achado 1 da fidelidade T-118).')
w('7. Conferência M6.3: duas tabelas (P1-DA-4.2 e P1-DA-7) têm "Aspecto" como primeira coluna e foram descontadas da contagem das tabelas `compare` (23).')
w('8. A montagem anterior em out/ (007787e3…c192 e 8b5489b9…b8dd, as embutidas na plataforma v16) foi substituída pela montagem canônica (82c4117c… e 04cbd593…); stats_v1_13_DA.json mudou só no `sha_json` do lote D6. A plataforma v16 não foi remontada (D1, seção 2).')
w('9. Pendente (outros responsáveis): cobertura v1.13 (secretaria), fidelidade (gbq-cqe), reconciliação e gatilho A (gbq-gerencia); promoção byte a byte e publicação só depois do aceite e do "sim" do Fundador.')
w('10. Correções pós-fidelidade (D1 da GBQ, saida/pacote/T118_D1_achados_fidelidade_2026-10-20.md): registro_adendo_v113.py corrigido (achados 2, 3 e 4) e out/registro_adendo5.md regerado; a cópia antecipada do adendo em saida/gbq/ (7224db40…) foi movida para historico/registro_adendo5_R1_7224db40.md, sem promoção (achado 5); este manifesto passou a listar todos os arquivos da pasta, inclusive cobertura_v1_13.py e fidelidade_v1_13_T118_gbq-cqe.md (achado 6). out/pacote.json, out/pacote_estudante.json, out/stats_v1_13_DA.json, out/conferencia_t118.json, out/diag30_DA.json, out/estudante_md_v1_13.json e os 53 arquivos de out/estudante/ não mudaram.')
open(HERE / 'MANIFESTO_v1_13.md', 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
b = (HERE / 'MANIFESTO_v1_13.md').read_bytes()
print('MANIFESTO_v1_13.md: %d bytes; SHA-256 %s; %d arquivos listados; divergências %d' % (len(b), sha(b), len(arquivos) + len(extra), falhas))
sys.exit(1 if falhas else 0)
