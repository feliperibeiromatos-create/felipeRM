# T-108 — tabela de fontes da GCE (produção: gce-cpp) — 2026-10-18

Insumo da QA da T-108-GCE. Base: saida/gce/T108_D1_GCE_2026-10-18.md (seções 2 a 5), ordens/ORDEM_V15_C_LIMPEZA.md, saida/pacote/T108_ocorrencias.csv, saida/pacote/pacote.json v1.10. Nenhuma fonte nova, nenhum nome inferido além do título/órgão que o arquivo de origem dá; sem URL. Os arquivos de origem, o pacote.json e as demais fontes canônicas não foram alterados.

Aviso sobre o SHA-256 da D1. O arquivo saida/pacote/pacote.json no disco tem SHA-256 bruto 58e73632091fad60bcea796dab96c9512c86cf8bfbe752b7ac5f209fc2ffff0c (terminadores CRLF do checkout no Windows). Com CRLF convertido em LF o hash é d43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed, o da D1 (D-PACOTE-V110). O texto dos campos (JSON analisado) é o mesmo; o script confere os dois hashes.

## 1. Tabelas de fontes, por arquivo de origem (ajuste A1)

Os nomes foram escritos sem parênteses internos, para caber nas formas fixas "(nome, verificado em dd/mm/aaaa)" e "(nome)" sem aninhar parênteses. Nos códigos de F9 e F7, o título entre aspas é o título que o arquivo dá.

### 1.1 saida/gce/GCE_Lote1_v2_CPP.md (Lote 1; também resolve os códigos F1 a F12 do Lote 1-C, conforme GCE_Lote1C_v2_CPP.md, linha 25)

| lote | código | nome por extenso | arquivo:linha da definição | linhas do CSV que usam | observação |
|---|---|---|---|---|---|
| 1 (e 1-C) | F1 | documentação da OpenAI sobre fala para texto | saida/gce/GCE_Lote1_v2_CPP.md:48 | 14 |  |
| 1 (e 1-C) | F2 | documentação da OpenAI sobre áudio | saida/gce/GCE_Lote1_v2_CPP.md:49 | 3 |  |
| 1 (e 1-C) | F3 | documentação do Google Cloud sobre o modelo Chirp 3 | saida/gce/GCE_Lote1_v2_CPP.md:50 | 9 |  |
| 1 (e 1-C) | F4 | documentação da Microsoft sobre o Azure AI Speech | saida/gce/GCE_Lote1_v2_CPP.md:51 | 6 |  |
| 1 (e 1-C) | F5 | documentação do Amazon Transcribe sobre idiomas suportados | saida/gce/GCE_Lote1_v2_CPP.md:52 | 4 |  |
| 1 (e 1-C) | F6 | visão geral da documentação do Amazon Transcribe | saida/gce/GCE_Lote1_v2_CPP.md:53 | 6 |  |
| 1 (e 1-C) | F7 | referência da API StartStreamTranscription, da AWS | saida/gce/GCE_Lote1_v2_CPP.md:54 | 7 |  |
| 1 (e 1-C) | F8 | documentação do Google sobre áudio e transcrição na API Gemini | saida/gce/GCE_Lote1_v2_CPP.md:55 | 3 | o arquivo dá duas páginas (audio e transcribe), linhas 55 e 56 |
| 1 (e 1-C) | F9 | artigo do Whisper, "Robust Speech Recognition via Large-Scale Weak Supervision" | saida/gce/GCE_Lote1_v2_CPP.md:57 | 2 | o nome inclui o título do artigo; o arquivo dá 06/12/2022 |
| 1 (e 1-C) | F10 | repositório openai/whisper no GitHub | saida/gce/GCE_Lote1_v2_CPP.md:58 | 5 | o arquivo dá "código e pesos, licença MIT" |
| 1 (e 1-C) | F11 | documentação do Amazon Transcribe sobre modelos de linguagem personalizados | saida/gce/GCE_Lote1_v2_CPP.md:59 | 4 |  |
| 1 (e 1-C) | F12 | documentação da Microsoft sobre diarização no Azure AI Speech | saida/gce/GCE_Lote1_v2_CPP.md:60 | 3 | definição continua na linha 61 |

Convenção "[V dd/mm/aaaa — Fn]": linha 45. Código sem definição localizável neste arquivo: nenhum.

### 1.2 saida/gce/GCE_Lote1C_v2_CPP.md (Lote 1-C)

| lote | código | nome por extenso | arquivo:linha da definição | linhas do CSV que usam | observação |
|---|---|---|---|---|---|
| 1-C | arXiv 2006.11477 | artigo do wav2vec 2.0, arXiv 2006.11477 | saida/gce/GCE_Lote1C_v2_CPP.md:27 | 2 | definição local no arquivo ("Fonte nova da C1: wav2vec 2.0, arXiv 2006.11477"); o texto do pacote usa a forma "[V 08/10/2026 — arXiv 2006.11477]" e, no Lote 1, "[V 08/10/2026]" sem código |
| 1-C | F1, F4, F9 | ver 1.1 | GCE_Lote1_v2_CPP.md:48, 51, 57 | 4 | o arquivo declara, na linha 25, que as fontes F1 a F12 são as do v2 do Lote 1 |

### 1.3 saida/gce/GCE_Lote2_v2_CPP.md (Lote 2)

| lote | código | nome por extenso | arquivo:linha da definição | linhas do CSV que usam | observação |
|---|---|---|---|---|---|
| 2 | F1 | Banco de Discursos da Câmara, Pesquisa Avançada | saida/gce/GCE_Lote2_v2_CPP.md:77 | 1 |  |
| 2 | F2 | página "Como pesquisar no Banco de Discursos", da Câmara | saida/gce/GCE_Lote2_v2_CPP.md:79 | 1 |  |
| 2 | F3 | especificação WebVTT, do W3C | saida/gce/GCE_Lote2_v2_CPP.md:82 | 2 | o arquivo dá o status "rascunho de recomendação candidata" |
| 2 | F4 | Ordem de Serviço nº 1/1970 da Primeira-Secretaria da Câmara, no Legin | saida/gce/GCE_Lote2_v2_CPP.md:84 | 2 | o arquivo marca "só contexto histórico" e "não consta revogação expressa" |
| 2 | F5 | Portaria DG nº 77/2017 da Câmara, no Legin | saida/gce/GCE_Lote2_v2_CPP.md:87 | 1 | o arquivo dá "Legin, publicação original" |
| 2 | F6 | Rol do DETAQ, no portal da Câmara | saida/gce/GCE_Lote2_v2_CPP.md:96 | 4 |  |
| 2 | F7 | "Computer-Aided Transcription in the Courts", do OJP/NCJRS, Departamento de Justiça dos EUA | saida/gce/GCE_Lote2_v2_CPP.md:99 | 3 |  |
| 2 | F8 | Ato da Mesa nº 251/2026 da Câmara, no Legin | saida/gce/GCE_Lote2_v2_CPP.md:103 | 2 | o arquivo dá "Legin, publicação original" |
| 2 | F9 | Google Cloud, "Improve transcription results with model adaptation" | saida/gce/GCE_Lote2_v2_CPP.md:107 | 0 | definida no arquivo; sem ocorrência no escopo |
| 2 | F10 | Microsoft, "Training and testing datasets" (custom speech) | saida/gce/GCE_Lote2_v2_CPP.md:111 | 0 | definida no arquivo; sem ocorrência no escopo |

Menção "Legin" sem código (a ocorrência "[V 08/10/2026 — Legin]" do RICD, art. 176): o nome é "Legin"; a menção fica nas linhas 84, 87 e 103 do arquivo (F4, F5, F8). Convenção "[V dd/mm/aaaa — Fn]": linha 73.

Códigos N do Lote 2 (limites de evidência, não fontes). Não têm nome por extenso: todas as ocorrências foram apagadas (forma fixa "Nn" em frase, D1 seção 3).

| lote | código | descrição no arquivo | arquivo:linha | linhas do CSV que usam |
|---|---|---|---|---|
| 2 | N1 | forma de identificar o orador na nota taquigráfica | saida/gce/GCE_Lote2_v2_CPP.md:117 | 2 |
| 2 | N2 | convenção da Câmara para grafia de números, siglas e abreviações e marcação de pausas e eventos | saida/gce/GCE_Lote2_v2_CPP.md:122 | 4 |
| 2 | N3 | ferramentas de CAT e editores comerciais | saida/gce/GCE_Lote2_v2_CPP.md:128 | 1 |
| 2 | N5 | terminologia: "degravação" não definida no edital | saida/gce/GCE_Lote2_v2_CPP.md:135 | 1 |

### 1.4 saida/gce/GCE_Lote3_v2_CPP.md (Lote 3)

| lote | código | nome por extenso | arquivo:linha da definição | linhas do CSV que usam | observação |
|---|---|---|---|---|---|
| 3 | F1 | LGPD compilada, no Planalto | saida/gce/GCE_Lote3_v2_CPP.md:45 | 1 | texto: "Planalto — LGPD, Lei 13.709/2018, página COMPILADA" |
| 3 | F2 | Lei 9.610/1998, no Planalto | saida/gce/GCE_Lote3_v2_CPP.md:48 | 2 | texto: "Planalto — Lei 9.610/1998" |
| 3 | F4 | Ato da Mesa nº 225/2025 da Câmara, no Legin | saida/gce/GCE_Lote3_v2_CPP.md:55 | 1 | o arquivo dá "Câmara/Legin — Ato da Mesa nº 225, de 15/12/2025, publicação original" (norma interna, contexto do 3.1) |
| 3 | F3 | Lei 15.352/2026 | saida/gce/GCE_Lote3_v2_CPP.md:51 | 0 | definida no arquivo; sem ocorrência no escopo |

Convenção "[NORMATIVO — QA]": linha 43 (as etiquetas sem base legal foram apagadas; as com base viraram "(base)"). Convenção "[V dd/mm/aaaa — Fn]": linha 42.

Códigos N do Lote 3 (limites de evidência, não fontes). Sem nome por extenso: ocorrências apagadas.

| lote | código | descrição no arquivo | arquivo:linha | linhas do CSV que usam |
|---|---|---|---|---|
| 3 | N4 | direitos autorais e IA (4.2): o que não está em texto legal nem em jurisprudência firmada | saida/gce/GCE_Lote3_v2_CPP.md:75 | 1 |
| 3 | N5 | modelos de IA (3.4): nomes e versões não verificados | saida/gce/GCE_Lote3_v2_CPP.md:78 | 1 |
| 3 | N6 | sistemas de IA realmente usados em parlamentos (3.1 a 3.3): não verificado | saida/gce/GCE_Lote3_v2_CPP.md:80 | 3 |
| 3 | N7 | eventual legislação específica sobre IA posterior ao texto lido | saida/gce/GCE_Lote3_v2_CPP.md:83 | 1 |

### 1.5 Arquivos de reforço e de padrões

saida/gce/L1_reforco_*, L2_reforco_*, L3_reforco_*, GCE_Lote2_padroes_GCE.md e GCE_Lote3_padroes_GCE.md foram lidos. Os reforços trazem a própria tabela de bases, em formato "fonte | URL | data" (sem códigos Fn); as ocorrências dos itens L1-R, L2-R e L3-R não contêm código de fonte (só REVERIFICAR, VOLÁTIL, códigos de item, "espelho da troca", ids de decisão e "conta conferida por script"). Os arquivos de padrões não contêm códigos Fn. Logo, nenhum código dessas ocorrências depende dos reforços.

## 2. Contagem de códigos

| arquivo de origem | códigos de fonte usados nas ocorrências | resolvidos | NAO_IDENTIFICADA |
|---|---|---|---|
| GCE_Lote1_v2_CPP.md | F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12 (12) | 12 | 0 |
| GCE_Lote1C_v2_CPP.md | arXiv 2006.11477 (definição local); F1, F4, F9 (pela tabela do Lote 1) | 4 | 0 |
| GCE_Lote2_v2_CPP.md | F1, F2, F3, F4, F5, F6, F7, F8 (8), mais "Legin" sem código | 8 | 0 |
| GCE_Lote3_v2_CPP.md | F1, F2, F4 (3) | 3 | 0 |
| códigos N (Lote 2: N1, N2, N3, N5; Lote 3: N4, N5, N6, N7) | limites de evidência; sem nome por extenso | 8 definidos nos arquivos | 0 |

Total: nenhum código com definição não localizável; nenhuma linha do CSV tem a nota "fonte não identificada".

## 3. Contagens do CSV (saida/gce/T108_substituicoes_GCE.csv)

Linhas: 263 (GCE-0001 a GCE-0263). Ocorrências do escopo cobertas: 293 de 293, cada uma em exatamente uma linha; mais 5 ocorrências que o inventário não listou (linhas com ids_ocorrencia NAO_INVENTARIADA-01 a -05, ver seção 5).

| por acao | linhas |
|---|---|
| SUBSTITUIR | 179 |
| DELETAR | 84 |
| MANTER | 0 |

| por regra | linhas |
|---|---|
| 2 | 100 |
| 2;5 | 30 |
| 4;5 | 6 |
| 5 | 127 |

| por lote | linhas |
|---|---|
| 1 | 88 |
| 1-C | 7 |
| 2 | 106 |
| 3 | 54 |
| DISCURSIVA | 8 |

| por categoria | ocorrências do inventário cobertas | linhas (categoria exata) |
|---|---|---|
| C01 | 14 | C01=12, C01;C02=1 |
| C02 | 16 | C01;C02=1, C02=13, C02;C10=1 |
| C04 | 115 | C04=111, C04;C05=3, C04;C10=1 |
| C05 | 18 | C04;C05=3, C05=12, C05;C10=3 |
| C07 | 7 | C07=10 |
| C08 | 4 | C08=3, C08;C10=1 |
| C09 | 2 | C09=2 |
| C10 | 117 | C02;C10=1, C04;C10=1, C05;C10=3, C08;C10=1, C10=90 |

Linhas com a nota "fonte não identificada": 0. Linhas NAO_IDENTIFICADA: 0. Linhas MANTER: 0 (a D1 não mandou manter nenhuma).

## 4. Autoconferência por script (somente leitura)

Saída do script (python -I, raiz do repositório). O script lê saida/pacote/pacote.json e os dois CSV, não escreve nada, e aplica as linhas em memória, em sequência, para varrer o resíduo.

```
SHA-256 bruto      : 58e73632091fad60bcea796dab96c9512c86cf8bfbe752b7ac5f209fc2ffff0c
SHA-256 (CRLF->LF) : d43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed
SHA confere com a D1: True
linhas: 263 | ocorrências do escopo: 293
ids cobertos exatamente uma vez: 293 de 293
linhas NAO_INVENTARIADA: 5
resíduo após aplicar as 263 linhas (padrões de marca nos campos do escopo): 0
só curso/resumo/pegadinhas.texto/justificativa/padrao tocados: True
campos fora do escopo alterados (esperado 0): 0
contagem 'em lote' antes/depois das edições: 18 / 18
contagem 'no lote' antes/depois das edições: 2 / 2
contagem 'do lote' antes/depois das edições: 4 / 4
contagem 'lote ' antes/depois das edições: 25 / 25
contagem 'F4' antes/depois das edições: 62 / 53
FALHAS: 0
```

Verificações feitas: (1) `antes` ocorre exatamente uma vez no campo do pacote.json v1.10, também na aplicação sequencial; (2) cada um dos 293 ids aparece uma vez; (3) nenhum `depois` casa com `\b[FN]\d{1,2}\b`, `L\d[A-C]?-[QR]?\d+`, `\[V `, `NORMATIVO`, `REVERIFICAR`, `QA\b`, `CPP`, `GCE` (e também CQFP, VOLÁTIL, ids D-…, R2–R9, E\d, errata, vN, "não cobrar", "SEM ITEM", "NÃO GABARITO", "Difere", "espelho da troca", "Lote(s)"); (4) acao, regra e fonte_origem preenchidos conforme A2 a A4; (5) aplicadas as linhas, a varredura nos campos do escopo dá 0 resíduos; (6) só os campos curso, resumo, pegadinhas.texto, justificativa e padrao foram tocados; (7) enunciado, comando, textoBase, gabarito, itemEdital, aderencia, volatil e todos os outros campos idênticos ao original; (8) o termo técnico "lote" (em lote, no lote, do lote) e as ocorrências fora do escopo ficam com a mesma contagem (os FP-R1 e FP-CONTEUDO não são tocados; nenhuma linha do CSV cai sobre a posição de um deles).

## 5. Pontos para a Gerência e o QA

1. Ocorrências não inventariadas (5 linhas NAO_INVENTARIADA-01 a -05, mais E3 dentro de uma linha com id). Estavam nos mesmos campos e fora da lista do inventário: "(F8)" no curso do Lote 2 (código de fonte entre parênteses), "Lote 1, 1.8" no curso do Lote 3, e os rótulos "R3.", "R4." das notas de correção de D4 e D5 (mais "R2." de D4 e "R3." de D5, que entraram nas linhas já inventariadas); "E3" em "(N1; E3)" do resumo do Lote 2. Tratadas pela mesma regra, e sinalizadas na nota para o QA e para o inventário da GBQ poder ser atualizado (o inventário não listava essas 5).
2. VOLÁTIL no meio da frase ("VOLÁTIL pela hipótese (c): …", 6 casos em L2-R81, R82, R85, R94, R99, R100) não está na forma fixa da D1 (que cobre "VOLÁTIL (…)"). Reescritos como "O dado pode mudar, pois …", sem a letra da hipótese e sem o id D-T96-ONDA2-ACEITE; o prefixo "Dado sujeito a mudança (…)" desses itens fica como a D1 manda. "Não VOLÁTIL:" (L2-R88, L2-R96) virou "Não é dado sujeito a mudança:". "NÃO VOLÁTIL" no fim de L2-Q23 e "REVERIFICAR (normativo) 04–08/01/2027; não VOLÁTIL." de L3-Q21 foram apagados (instrução interna).
3. Etiquetas [NORMATIVO — QA] sem base legal no colchete (curso e resumo do Lote 3): apagadas inteiras, com o espaço que as antecede. Com base (justificativas L3-Q17 a L3-Q30): "(LGPD, art. 5º, I)." com o ponto final deslocado para fora do parêntese; artigos, incisos e leis, todos mantidos (o script não os altera).
4. CONTROVERSO / NÃO GABARITO / "não cobrar" no Lote 3 (resumo e curso 4.1 e 4.2): trocados pela frase de conteúdo equivalente da D1 ("não costuma ser cobrado em prova objetiva"), sem fato novo. "Nomes de modelos: voláteis, não cobrar." e "(N6: não cobrar descrição de sistema real.)" foram apagados porque não protegem a candidata de ponto controverso.
5. Etiqueta [V 10/10/2026 — F4 …] do Ato da Mesa nº 225/2025 (curso 3.1): a URL e "leitura automatizada via WebFetch" (processo) saíram; "paráfrase, sem transcrição literal" ficou como complemento, na forma "(nome, complemento, verificado em dd/mm/aaaa)".
6. Células do quadro-síntese do Lote 1: os dois "[F10]" e o "[F12]*" viraram "(nome)", pela D1; o alinhamento em colunas do quadro de texto simples muda nessas três células (a coluna em si não muda).
7. Etiquetas dentro de parêntese (3 casos: wav2vec no curso do Lote 1, "F1, v2" no curso do Lote 1-C, "Banco de Discursos [V 08/10/2026]" no resumo do Lote 2; mais "(Azure [F4])" e "(ex.: Whisper [F9])" na 1-C): forma ajustada ao mínimo, sem parêntese duplo ("…, verificado em dd/mm/aaaa)" ou ", nome)"). O "v2" de "F1, v2" foi apagado como vN.
8. L2-R55: a nota "os dois itens não devem figurar no mesmo simulado" é nota de deduplicação (equivalente à regra 3 da ordem) e saiu junto com a referência L2-R64. L2-R60 e L2-R82: a referência a outro item virou descrição do conteúdo ("Este item julga só a escala de apresentação, não a fórmula.") ou foi apagada com a comparação de base.
9. D3, D4 e D5 (padrao): seguidas à letra as decisões da D1 seção 4 (Nota de correção; "(D-T2)" apagado; "Notas de correção" sem "(GCE, Rn–Rm)", rótulos R2., R3., R4. em numeração 1., 2., 3.; "da versão da CPP" apagado). O "Projeto" em "HIPÓTESE do Projeto" não foi tocado (não é marca da lista).
10. Espelho da troca (6 VERIFICAR do L2-R48, R58, R81, R83, R92, R102): frase da D1, com as aspas mantidas ("A afirmação oposta (…) estaria errada."); no L2-R81 a oração em minúscula fica dentro da frase ("; a afirmação oposta (…) estaria errada.").

## 6. Texto do script (para o QA reexecutar)

O script de conferência está em saida/gce/ apenas por referência a esta seção; o texto é o abaixo (python -I, na raiz do repositório, salvo em arquivo temporário).

```python
# T108_conferir_GCE.py — somente leitura. Uso (na raiz do repositório): python -I conferir.py
import csv, json, re, sys, hashlib, collections
sys.stdout.reconfigure(encoding='utf-8')
PJ = 'saida/pacote/pacote.json'
raw = open(PJ, 'rb').read()
print('SHA-256 bruto      :', hashlib.sha256(raw).hexdigest())
print('SHA-256 (CRLF->LF) :', hashlib.sha256(raw.replace(b'\r\n', b'\n')).hexdigest())
ESPERADO = 'd43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed'
ok_sha = ESPERADO in (hashlib.sha256(raw.replace(b'\r\n', b'\n')).hexdigest(), hashlib.sha256(raw).hexdigest())
print('SHA confere com a D1:', ok_sha)
P = json.loads(raw.decode('utf-8'))
RX = r'(itens|lotes|discursivas)\[([^\]]+)\]\.(\w+)(?:\[(\d+)\]\.(\w+))?$'
def get(path):
    k, i, f, j, h = re.match(RX, path).groups()
    o = [x for x in P[k] if x['id'] == i][0]
    return o[f] if j is None else o[f][int(j)][h]
def setv(path, v):
    k, i, f, j, h = re.match(RX, path).groups()
    o = [x for x in P[k] if x['id'] == i][0]
    if j is None: o[f] = v
    else: o[f][int(j)][h] = v
rows = list(csv.DictReader(open('saida/gce/T108_substituicoes_GCE.csv', encoding='utf-8', newline='')))
inv = list(csv.DictReader(open('saida/pacote/T108_ocorrencias.csv', encoding='utf-8', newline='')))
esc = [x for x in inv if x['gerencia'] == 'GCE' and x['arquivo'] == 'pacote.json' and x['classe'] in ('PROCESSO', 'VERIFICAR')]
ids_esc = [x['id_ocorrencia'] for x in esc]
falhas = []
print('linhas:', len(rows), '| ocorrências do escopo:', len(ids_esc))
# (1) antes ocorre exatamente uma vez no campo (pacote.json original)
for r in rows:
    n = get(r['caminho']).count(r['antes'])
    if n != 1: falhas.append(('antes_n=%d' % n, r['id_edicao']))
# (2) cada id exatamente uma vez
cnt = collections.Counter(i for r in rows for i in r['ids_ocorrencia'].split(';') if not i.startswith('NAO_INVENTARIADA'))
for i in ids_esc:
    if cnt[i] != 1: falhas.append(('id_%d' % cnt[i], i))
extra = [i for i in cnt if i not in set(ids_esc)]
if extra: falhas.append(('id_fora_do_escopo', extra))
print('ids cobertos exatamente uma vez:', sum(1 for i in ids_esc if cnt[i] == 1), 'de', len(ids_esc))
print('linhas NAO_INVENTARIADA:', sum(1 for r in rows if r['ids_ocorrencia'].startswith('NAO_INVENTARIADA')))
# (3) padrões proibidos no depois
PROIB = [r'\b[FN]\d{1,2}\b', r'L\d[A-C]?-[QR]?\d+', r'\[V ', r'NORMATIVO', r'REVERIFICAR', r'QA\b', r'CPP', r'GCE', r'CQFP', r'VOLÁTIL', r'\bD-[A-Z0-9]', r'\bR[2-9]\b', r'\bE\d\b', r'errata', r'\bv\d\b', r'não cobrar', r'SEM ITEM', r'NÃO GABARITO', r'Difere', r'[Ee]spelho da troca', r'\bLotes?\b']
for r in rows:
    for p in PROIB:
        if re.search(p, r['depois']): falhas.append(('depois~' + p, r['id_edicao']))
# (4) acao/regra/fonte_origem
for r in rows:
    if r['acao'] not in ('DELETAR', 'SUBSTITUIR', 'MANTER'): falhas.append(('acao', r['id_edicao']))
    if not re.fullmatch(r'[1-5](;[1-5])*', r['regra']): falhas.append(('regra', r['id_edicao']))
    if (re.search(r'C0[45]', r['categoria']) or re.search(r'Planalto|Legin|OpenAI|Microsoft|Amazon|AWS|Google|W3C|OJP|arXiv|Whisper', r['depois'])) and not r['fonte_origem']:
        falhas.append(('fonte_origem_vazia', r['id_edicao']))
# (5) aplicar sequencialmente e varrer o resíduo
por = collections.defaultdict(list)
for r in rows: por[r['caminho']].append(r)
for c, lst in por.items():
    t = get(c)
    for r in lst:
        if t.count(r['antes']) != 1: falhas.append(('sequencial_antes_n=%d' % t.count(r['antes']), r['id_edicao']))
        else: t = t.replace(r['antes'], r['depois'])
    setv(c, t)
pat = re.compile(r'\b[FN]\d{1,2}\b|\bL\d[A-C]?-[QR]?\d+\b|\[V |NORMATIVO|REVERIFICAR|\bQA\b|CPP|GCE|CQFP|\bLotes?\b|VOLÁTIL|errata|\bv\d\b|\bD-[A-Z0-9]+|não cobrar|SEM ITEM|NÃO GABARITO|Difere|\bQ\d\d\b|\bpar C\d+|CONTROVERSO|\bR[2-9]\b|\bE\d\b|[Ee]spelho da troca|hipótese \([a-c]\)')
resid = []
def campos():
    for l in P['lotes']:
        if l['id'] in ('L1', 'L1C', 'L2', 'L3'):
            for f in ('curso', 'resumo'): yield 'lotes[%s].%s' % (l['id'], f), l[f]
            for j, pg in enumerate(l['pegadinhas']): yield 'lotes[%s].pegadinhas[%d].texto' % (l['id'], j), pg['texto']
    for it in P['itens']:
        if re.match(r'L(1|1C|2|3)-', it['id']): yield 'itens[%s].justificativa' % it['id'], it['justificativa']
    for d in P['discursivas']: yield 'discursivas[%s].padrao' % d['id'], d['padrao']
for c, t in campos():
    for m in pat.finditer(t):
        resid.append((c, m.group(0), t[max(0, m.start()-30):m.end()+30]))
print('resíduo após aplicar as %d linhas (padrões de marca nos campos do escopo):' % len(rows), len(resid))
for x in resid[:20]: print('  ', x)
# (6) só campos de texto da candidata tocados
camp_ok = all(re.search(r'\.(curso|resumo|justificativa|padrao|texto)$', r['caminho']) for r in rows)
print('só curso/resumo/pegadinhas.texto/justificativa/padrao tocados:', camp_ok)
if not camp_ok: falhas.append(('campo_proibido', ''))
# (7) campos não tocados idênticos ao original (enunciado, gabarito, itemEdital...)
orig = json.loads(raw.decode('utf-8'))
dif = 0
for k in ('itens',):
    for a, b in zip(orig[k], P[k]):
        for f in a:
            if f != 'justificativa' and a[f] != b[f]: dif += 1
for a, b in zip(orig['lotes'], P['lotes']):
    for f in a:
        if f not in ('curso', 'resumo', 'pegadinhas') and a[f] != b[f]: dif += 1
for a, b in zip(orig['discursivas'], P['discursivas']):
    for f in a:
        if f != 'padrao' and a[f] != b[f]: dif += 1
print('campos fora do escopo alterados (esperado 0):', dif)
if dif: falhas.append(('campo_fora_alterado', dif))
# (8) termo técnico "lote" e tecla F4 intactos
def conta(Pp, termo):
    return sum(json.dumps(x, ensure_ascii=False).count(termo) for k in ('lotes', 'itens', 'discursivas') for x in Pp[k])
for termo in ('em lote', 'no lote', 'do lote', 'lote ', 'F4'):
    print('contagem %r antes/depois das edições: %d / %d' % (termo, conta(orig, termo), conta(P, termo)))
print('FALHAS:', len(falhas))
for f in falhas[:60]: print('  ', f)
```

## 7. Rodada 2 — resposta ao QA_T108_R1_2026-10-18_gce-cqfp.md (D1 pós-R1, seções 1 a 3 e 6)

Resposta item a item, antes do texto corrigido. O CSV corrigido é saida/gce/T108_substituicoes_GCE_v2.csv (269 linhas: 257 iguais à v1 byte a byte, 6 corrigidas, 6 novas). A v1 e as seções 1 a 6 deste arquivo não foram alteradas.

| Ref. do QA | Assunto | Resposta | Efeito na v2 |
|---|---|---|---|
| 3.1 | GCE-0094, repetição "Whisper, artigo do Whisper" | acatado | `depois` = `Whisper, segundo o artigo "Robust Speech Recognition via Large-Scale Weak Supervision"),` |
| 3.2 | GCE-0105, nome da norma repetido no parêntese | acatado | `depois` = `(Legin, verificado em 08/10/2026)` |
| 3.3 | GCE-0154, "afirmação oposta" aplicado a grafia | acatado | `depois` = `as grafias "C.P.I.s" ou "CPI-s" estariam incorretas.` |
| 3.4 | linha que falta, resíduo em L2-R18 | acatado | nova GCE-0264 (NAO_INVENTARIADA-06), DELETAR; a restrição de simulado vai ao campo interno do item pela GBQ (D-V15-C-M2) |
| 4.1 | formas "O dado pode mudar, pois …" e "Não é dado sujeito a mudança:" | acatado (aprovada pelo QA e registrada como forma fixa complementar na D1 pós-R1) | nenhum; GCE-0155, 0157, 0161, 0162, 0167, 0168, 0170 e 0172 não mudam |
| R1 (4.2) | "não costuma(m) ser cobrado(s) em prova objetiva" é afirmação sobre a banca sem fonte | acatado | GCE-0205, 0218 e 0235 corrigidas (`depois` sem a frase); GCE-0202 e 0219 sem mudança |
| R2 (5) | "HIPÓTESE do Projeto" em D3, D4 e D5 | acatado, com o rótulo HIPÓTESE mantido | novas GCE-0265, 0266, 0267 ("deste material") |
| R3 (5) | "não afirmar" no curso do L3 | acatado, mas na redação da D1 pós-R1 ("não se pode afirmar"), não na sugerida pelo QA, para não afirmar uma negativa que o original não afirma | novas GCE-0268 e 0269 |
| R4 (5) | inventário da GBQ sem NAO_INVENTARIADA-01 a -06 e sem o E3 | acatado como informação à GBQ; ids -07 a -11 criados | nenhum no CSV |
| R5 (5) | nada normativo pendente | acatado (registro) | nenhuma linha nova toca lei, artigo, inciso ou § |
| 2.1 (observações) | nome do F9 com título do artigo; "Rol do DETAQ" | acatado (observações, sem reprovação) | nenhum |
| 4.2 (apagamentos) | GCE-0202, 0208, 0211, 0232 e 0240 | acatado (aprovadas) | nenhum |

Autoconferência por script da v2: ver saida/gce/T108_producao_notas_GCE_v2.md.
