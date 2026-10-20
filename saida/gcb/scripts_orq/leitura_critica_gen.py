# leitura_critica_gen.py — gera D<n>_para_leitura_critica.md (cabeçalho neutro; só curso, resumo, pares e pegadinhas; sem itens)
# Uso: python3 -I leitura_critica_gen.py D2 "Agentes públicos e direito administrativo disciplinar" "3,4"
import re, sys, pathlib, hashlib
lote, titulo, itens = sys.argv[1], sys.argv[2], sys.argv[3].split(',')
g = pathlib.Path(__file__).resolve().parents[1]
raiz = g.parents[1]
L = (g/f'{lote}_v1.md').read_text(encoding='utf-8').split('\n')
ini = next(i for i, l in enumerate(L) if l.startswith('## 1. '))
fim = next(i for i, l in enumerate(L) if l.startswith('## 5. '))
corpo = [l for l in L[ini:fim] if l not in ('### Parte A', '### Parte B')]
txt = '\n'.join(corpo).rstrip()
ed = [l for l in (raiz/'edital/DA_itens_1_12_P1.md').read_text(encoding='utf-8').splitlines() if l.startswith('1 Estado')][0]
trechos = []
for n in itens:
    m = re.search(r'(?:^|(?<=\. ))' + n + r' [A-ZÁÉÍÓÚ].*?(?=(?<=\. )' + str(int(n)+1) + r' [A-ZÁÉÍÓÚ]|$)', ed)
    trechos.append(m.group(0).strip())
SUBS = [
    (r'\[SEM FONTE — não afirmar\]', '(não afirmado neste material)'),
    (r'\s*\((?:ponto bloqueado|ponto|lição)[^()]*BQ-\d{4}[^()]*\)', ''),
    (r'\s*Observação: o ponto do BQ-\d{4}[^.]*\.', ''),
    (r'\(SEM FONTE[^)]*\)', '(sem fonte oficial localizada)'),
    (r'\bAnexo N\b(?:,? seção [\d.]+)?', 'texto legal compilado'),
    (r'\s*\((?:ponto d[oa]s? )?(?:item real )?BQ-\d{4}[^()]*\)', ''),
    (r'\s*\[QA PENDENTE[^\]]*\]', ''), (r'\s*QA PENDENTE', ''),
    (r'\bREVERIFICAR\b:?', 'Nota de vigência:'),
    (r'\s*\((?:ficha|ver ficha)[^()]*\)', ''),
    (r'\b(?:da|na|pela) ficha\b', 'deste material'),
    (r'\bBASE DOUTRINÁRIA\b:?', 'Base doutrinária:'),
]
for rx, novo in SUBS:
    txt = re.sub(rx, novo, txt)
cab = [f'LOTE {lote} — {titulo} — curso, resumo, pares e pegadinhas — 20/10/2026', '',
       'Instrução ao leitor: liste somente o que falta: pares confundíveis, pegadinhas prováveis e tópicos do edital sem cobertura; não reescreva nada; cite o artigo de cada sugestão', '',
       'Edital — itens ' + ' e '.join(itens) + ' (texto literal):', ''] + ['> ' + t for t in trechos] + ['', '---']
out = '\n'.join(cab) + '\n' + txt + '\n\n---\nFIM\n'
PROIB = r'(?i:fábrica|\bgcb|\bgce|\bgbq|Claude|ChatGPT|OpenAI|Anthropic|Fundador|orquestrador|sonnet|opus|leitura crítica|registro de acatamento)|\bficha\b|BQ-\d|\b' + lote + r'-\d{2}\b|\bT-\d{2}|\bD-[A-Z]{3}|QA PENDENTE|\[TS\]|Anexo N|SEM FONTE'
ach = [(m.group(0), out[max(0, m.start()-50):m.end()+50].replace('\n', ' ')) for m in re.finditer(PROIB, out)]
for a in ach: print('ACHADO', a)
dest = g/f'{lote}_para_leitura_critica.md'
dest.write_text(out, encoding='utf-8')
print(dest.name, len(out.encode()), 'bytes; SHA-256', hashlib.sha256(out.encode()).hexdigest(), '; achados:', len(ach))
