import re,sys
L=open('/home/user/felipeRM/saida/gcb/D5_v1.md',encoding='utf-8').read().split('\n')
ed=open('/home/user/felipeRM/edital/DA_itens_1_12_P1.md',encoding='utf-8').read()
item10=re.search(r'10 Noções de Licitações.*?(?= 11 )',ed,re.S).group(0)
# sections: curso 9..245, resumo 248..279, pares 281..303, pegadinhas 305..351 (1-based)
def find(prefix):
    return next(i for i,l in enumerate(L) if l.startswith(prefix))
a=find('## 1. (a) CURSO'); b=find('## 5. (e) ITENS')
body=L[a:b]
# strip trailing separators
while body and body[-1].strip() in ('','---'): body.pop()
txt='\n'.join(body)
subs=[
('## 1. (a) CURSO — folha a folha','## 1. Curso — folha a folha'),
('## 2. (b) RESUMO — uma página do item 10','## 2. Resumo — item 10'),
('## 3. (c) PARES CONFUNDÍVEIS','## 3. Pares confundíveis'),
('## 4. (d) PEGADINHAS — lista consolidada','## 4. Pegadinhas — lista consolidada'),
('(Anexo N);','(texto compilado da Lei 14.133/2021, vigente em 2/10/2026);'),
('não abertos neste lote ([SEM FONTE — não afirmar]).','não abertos neste material (nada se afirma sobre eles).'),
(' (nota do Anexo N, seção 7, item 11)',''),
('(rol de incisos; aqui, os cobrados no lote)','(rol de incisos; aqui, os selecionados)'),
('estão NÃO CONFERIDOS no Anexo N: [SEM FONTE — não afirmar]','não foram conferidos neste material e não são afirmados'),
('REVERIFICAR: o art. 75, XVI','Nota: o art. 75, XVI'),
(' Nenhum item deste lote se apoia nesse inciso.',''),
('valor atualizado NÃO CONFERIDO no Anexo N','valor atualizado não conferido neste material'),
(', que já é objeto de item real do banco (BQ-0134) e não é repetido neste lote.','.'),
(' (ponto do item real BQ-0135, não repetido)',''),
(' (Requisitos da contratação e parcelamento, incisos III e VIII, são o ponto do item real BQ-0142.)',''),
('vem de regulamento não aberto neste Anexo: [SEM FONTE — não afirmar].','vem de regulamento não aberto neste material e não é afirmada aqui.'),
('| Número literal do Anexo N |','| Número literal da lei |'),
('Mínimo da ficha: 14, com os 12 obrigatórios (P-01 a P-12). Entregues: 16.','16 pares.'),
('atribuições do gestor: [SEM FONTE — não afirmar]','atribuições do gestor: não afirmadas neste material'),
]
for o,n in subs:
    c=txt.count(o)
    if c==0: sys.exit('MISS: '+o)
    txt=txt.replace(o,n)
head=['LOTE D5 — Licitações e contratos (Lei 14.133/2021) — curso, resumo, pares e pegadinhas — 18/10/2026','',
'Instrução ao leitor: liste somente o que falta: pares confundíveis, pegadinhas prováveis e tópicos do edital sem cobertura; não reescreva nada; cite o artigo de cada sugestão','',
'Edital — item 10 (texto literal):','','> '+item10,'','---']
out='\n'.join(head)+'\n'+txt+'\n\n---\nFIM\n'
open('/home/user/felipeRM/saida/gcb/D5_para_leitura_critica.md','w',encoding='utf-8').write(out)
