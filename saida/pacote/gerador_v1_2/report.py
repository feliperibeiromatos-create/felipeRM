# -*- coding: utf-8 -*-
import pickle, json, os
s = pickle.load(open('stats.pkl', 'rb'))
R = '/home/claude/fabrica_camara2026/saida/pacote/'
st = s['st']; b = s['binfo']
SRCS = [
 ('L1', 'saida/gce/GCE_Lote1_v2_CPP.md', 'v2 canônico + erratas E1–E5, E9, E10 aplicadas no texto; E7/E8 (valores da discursiva) do saida/gce/GCE_Lote1_consolidacao_GCE.md; E4a–c do mesmo arquivo'),
 ('L1C', 'saida/gce/GCE_Lote1C_v2_CPP.md', 'v2 canônico + erratas E1 e E3'),
 ('L2', 'saida/gce/GCE_Lote2_v2_CPP.md', 'v2 canônico + erratas E1a–d, E2, E3b, E5, E6; padrões em saida/gce/GCE_Lote2_padroes_GCE.md'),
 ('L3', 'saida/gce/GCE_Lote3_v2_CPP.md', 'v2 canônico + erratas E1a–b, E2, E3a–b; padrões em saida/gce/GCE_Lote3_padroes_GCE.md'),
 ('L4', 'saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md', 'v3.1 canônica (D-LOTE4-CANONICO)'),
 ('L4C', 'saida/gcb/GCB_Lote4C_v1_GCB-CPP.md', 'v1.1 (só itens AUTORAL)'),
 ('L5', 'saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md', 'v3 canônica'),
 ('L5C', 'saida/gcb/GCB_Lote5C_v1_GCB-CPP.md', 'v1.1 (só itens AUTORAL)'),
 ('L6A', 'saida/gcb/GCB_Lote6a_v2_producao_auto.md', 'v2 (D-LOTE6A-CANONICO)'),
 ('L6B', 'saida/gcb/GCB_Lote6b_v2_producao_auto.md', 'v2 com errata A-6b-1 (D-LOTE6B-CANONICO)'),
]
LI = {x[0]: x for x in s['lotes']}
o = []
w = o.append
w('# pacote_relatorio.md — T-05 — 2026-10-10 — gerado por gbq-csc')
w('')
w('Saída: `saida/pacote/pacote.json` (versao 1, geradoEm 2026-10-10, %d bytes UTF-8). Contrato: `regras/pacote_contrato.md`. Gerador: scripts no scratchpad da sessão (fora do repositório). Nenhum outro arquivo do repositório foi alterado. Nada deste pacote vai à candidata sem gatilho A e decisão do Fundador.' % s['size'])
w('')
w('## 1. Fonte canônica por lote')
w('')
w('Os arquivos `saida/lote*/RECONCILIADO.md` citados no prompt EXPORTAR não existem (as pastas `saida/lote1`…`lote5` existem mas não contêm esse arquivo). O arquivo canônico de cada lote foi identificado por `estado/ESTADO_CANONICO.md`, `DECISOES.md` e pelo registro GBQ `saida/gbq/claude_GBQ_Registro_AUTORAL_v2.md` (que substitui `claude_GBQ_Registro_AUTORAL_Lotes4e5.md`). Gabarito, subitem, [TS] e VOLÁTIL de cada item AUTORAL foram conferidos contra esse registro (180 de 180 sem divergência).')
w('')
w('| Lote | Arquivo canônico | Observação |')
w('|---|---|---|')
for lid, f, ob in SRCS:
    w('| %s | `%s` | %s |' % (lid, f, ob))
w('| Banco | `banco/banco.csv` | 66 linhas; comando extraído de `saida/simulados/simulado_0_v0.2.md` (ver seção 4) |')
w('| Simulado | `saida/simulados/simulado_0_v0.2.md` + `simulado_0_v0.2_gabarito.md` | mais recente do número 0 (a v0.1, `simulado_0.md`, está superada) |')
w('| Edital | `edital/TI_itens_1_4_P1.md`, `edital/TI_itens_5_8_P1.md`, `edital/modulo_RF_IA_P2.md` | texto literal |')
w('')
w('## 2. Contagens')
w('')
w('- edital: 47 entradas (P1 itens 1–4: 8; P1 itens 5–8: 12; P2: 27).')
w('- itens totais: %d = %d do banco + %d AUTORAL. Gabarito C/E: %d C / %d E.' % (len(json.load(open(R + 'pacote.json'))['itens']), 60, 180, s['tc'][0], s['tc'][1]))
w('- banco: 66 linhas em `banco/banco.csv`; 60 exportadas (%d C / %d E); 6 excluídas por anulação (gabarito X): %s. Aderência: %d parcial, %d direta.' % (s['bc'][0], s['bc'][1], ', '.join(x[0] for x in b['excl']), s['par'], 60 - s['par']))
w('- AUTORAL: %d C / %d E.' % (s['ac'][0], s['ac'][1]))
w('')
w('| Lote | AUTORAL | C | E | VOLÁTEIS | itens do edital cobertos | curso (car.) | resumo (car.) | pares | pegadinhas |')
w('|---|---|---|---|---|---|---|---|---|---|')
for lid in ['L1','L1C','L2','L3','L4','L4C','L5','L5C','L6A','L6B']:
    n, ce, v = st[lid]; li = LI[lid]
    w('| %s | %d | %d | %d | %d | %s | %d | %d | %d | %d |' % (lid, n, ce[0], ce[1], v, ', '.join(li[5]), li[1], li[2], li[3], li[4]))
w('')
w('- VOLÁTEIS: %d no total. Banco (%d): %s. AUTORAL (%d): %s. Todos levam `"volatil": true` (extensão ao contrato, ver seção 4).' % (len(s['vol_b']) + len(s['vol_a']), len(s['vol_b']), ', '.join(s['vol_b']), len(s['vol_a']), ', '.join(s['vol_a'])))
w('- simulados: 1 (SIM-0, "Simulado 0 — diagnóstico (v0.2)", tipo diagnóstico, 60 itens do banco, na ordem do simulado). Não existe Simulado 0-P2 nem Simulado 1 no repositório (D-SIM0-P2 e T-06 pendentes).')
w('- discursivas: 5, todas de P2 com padrão no formato Cebraspe (quesitos, conceitos por contagem de aspectos, base normativa): ' + '; '.join('%s %s (%d aspectos, %d quesitos, %d conceitos)' % (d[0], d[1], d[2], d[3], d[4]) for d in s['disc']) + '.')
w('  - D1 = Lote 1 (questão); D2 e D3 = Lote 2 (questão e peça); D4 e D5 = Lote 3 (questão e peça). Os Lotes 1-C, 4, 4-C, 5, 5-C, 6a e 6b não têm discursiva. Os Lotes de P1 não têm discursiva (edital: P1 não é cobrada na discursiva).')
w('  - D3 e D5 são pareceres técnicos (gênero confirmado para Cargos 1 e 2 do cd_25_ns; hipótese por analogia para o Cargo 11). Pesos por quesito são HIPÓTESE do Projeto.')
w('')
w('## 3. Validações executadas (todas OK)')
w('')
for t in ['JSON relido do disco e parseado sem erro.',
          'Nenhum item sem id, enunciado e gabarito C/E; nenhum id duplicado (240 ids).',
          'Contagem por lote igual à declarada: L1 20, L1C 10, L2 30, L3 30, L4 20, L4C 10, L5 20, L5C 10, L6A 15, L6B 15 (total 180).',
          'Todo `itemEdital` (itens) existe no `edital`; idem `itensEdital` e `pegadinhas.itemEdital` dos lotes (TI 1–4 como P1-1…P1-4.3).',
          '`aderencia` só direta ou parcial; `justificativa` não vazia em todo AUTORAL e vazia em todo item de banco.',
          'Nenhum texto exportado contém "QA PENDENTE", rótulos de transporte ("ENTREGA DE LOTE", "FIM DA PARTE", "FIM DO LOTE") ou linhas "=====".',
          'Texto de cada item do simulado idêntico (após normalizar espaços) ao `texto_integral` do banco: 60 de 60.',
          'Gabarito, subitem, [TS] e VOLÁTIL de cada AUTORAL idênticos ao registro GBQ v2: 180 de 180.',
          'Erratas aplicadas por substituição tolerante a quebra de linha, cada uma com exatamente 1 ocorrência (26 aplicações); %d quebras de linha hifenizadas reparadas.' % s['hy'],
          'Soma dos aspectos das discursivas: questões 14,30 + 0,70 de apresentação = 15,00; peças 28,50 + 1,50 = 30,00.']:
    w('- ' + t)
w('')
w('## 4. Extensões, mapeamentos e escolhas (a conferir pela Gerência)')
w('')
w('1. **Campo extra `"volatil": true`** nos 18 itens VOLÁTEIS (extensão ao contrato, a registrar em `regras/pacote_contrato.md` pela Gerência; a plataforma pode ignorá-lo, mas não deve usar esses itens em simulado final antes da reverificação de 4–8/1/2027). Itens não VOLÁTEIS não têm o campo.')
w('2. **Aderência (D-ADERENCIA).** A regra literal do prompt ("observacoes contendo parcial") marca só 5 itens (%s). As demais observações do banco expressam a mesma condição sem a palavra: "aderência temática ampla" (16 itens P2-4.1) e "aderência apenas por tema" (BQ-0017, BQ-0035). Marquei esses 18 também como **parcial**, o que dá **%d parcial / %d direta**, coerente com o Simulado 0 v0.2 (que declara parcial só em diagnóstico). Extensão: %s. Se a Gerência preferir a regra literal, são 18 itens a reclassificar para "direta". Todo AUTORAL é "direta".' % ('BQ-0001, 0015, 0016, 0036, 0055', s['par'], 60 - s['par'], ', '.join(b['ext'])))
w('3. **BQ-0011, 0012, 0038, 0039** saem como `itemEdital` P1-4, direta, conforme o banco após a T-22 (D-BANCO-TI-1-4). O mapa do Simulado 0 v0.2 ainda os mostra como P2-4.3 PARCIAL (a T-25, que substitui a T-20, não foi aplicada ao simulado). O pacote segue o banco, não o mapa.')
w('4. **`comando` e `textoBase` dos itens de banco.** `banco.csv` não tem colunas texto_comando/texto_base. O `comando` foi extraído do bloco "### Comando N" do `simulado_0_v0.2.md` (que o copia dos cadernos oficiais; todos os 60 itens estão no simulado). Para BQ-0049, 0050 e 0051 o texto-base está em `observacoes` ("texto-base do comando (copiado do PDF)"): foi para `textoBase`, e o `comando` ficou só com a instrução ("A partir da situação hipotética precedente, julgue os itens a seguir, que versam sobre inteligência artificial e assuntos correlatos."). A anotação "(grafia \'ideal atender\' conforme o PDF)" de BQ-0050 foi retirada do `textoBase` e permanece no enunciado literal. Nos demais itens, `textoBase` = "nenhum".')
w('5. **Campos de banco copiados sem encurtar:** `certame` e `cargo` (longos, ex.: "TRF6 2024 - 1º Concurso Cadastro de Reserva … (Edital nº 1, 10/10/2024)"), `ano` = ano_aplicacao (convenção D-ANO), `url` = `url_caderno` (o contrato tem uma só URL; `url_gabarito` não é exportada).')
w('6. **Campos dos AUTORAL:** `id` = id do registro GBQ (L1-Q01…, 4C-01, A5-01, 6A-01…); `certame` "Projeto Câmara 2026"; `cargo` "Lote N"; `ano` 2026; `numero` = número do item no lote; `comando` = instrução que antecede o item no arquivo canônico; `url` = caminho do arquivo canônico no repositório (SCHEMA.md); `textoBase` "nenhum"; `aderencia` "direta". Nos Lotes 6a e 6b o `comando` cita ids locais do lote (ex.: "julgue os itens de 6B-01 a 6B-05"), literal do original.')
w('7. **Lotes 4-C e 5-C** saem em `lotes` com `curso`, `resumo` e `pares` vazios e sem pegadinhas: os arquivos são complementos que contêm só itens AUTORAL (os cursos estão nos Lotes 4 e 5). O Lote 1-C traz o adendo ao curso do 1.4 e 1 pegadinha adicional, mas sem resumo nem pares.')
w('8. **Pegadinhas** = blocos "PEGADINHA PROVÁVEL" / "PEGADINHAS ADICIONAIS" (P2) e linhas "Pegadinha provável" / "PEGADINHAS PROVÁVEIS" (P1) do curso, com o `itemEdital` do cabeçalho do item; as listas F de fontes não foram exportadas. O `curso` e o `resumo` são o texto do arquivo, com marcação mínima (`## ` nos títulos de item); texto de transporte foi retirado.')
w('9. **Pares:** formato "A vs B: como" (P2) e "A × B | como" (P1). Um par P2 não tem " vs " ("Confidencialidade, integridade, disponibilidade."): saiu com `a` = o texto e `b` = "". Quebras de linha de ~72 colunas dos arquivos GCE foram unidas; hífen de quebra removido só em palavras cortadas (tabela fixa) e mantido em compostos e URLs.')
w('10. **Discursivas — conceitos.** Onde o padrão original condensa os conceitos ("Conceito 0 a 4: por contagem…" em D2 2.2 e 2.3 e D3 2.3), o array `conceitos` traz a linha condensada tal como está, sem expandir (não inventei texto). O campo `padrao` traz o texto integral do padrão. D5 2.1 e 2.5 usam formato "Conceito N: …" (dois-pontos) do original.')
w('11. **Lote 1.** Erratas E7/E8 da consolidação (valor máximo do quesito 2.3 = 5,30 e linha de apresentação 0,70) aplicadas ao padrão D1. Na errata E4c, a substituição começa com maiúscula ("No cálculo usual…") porque abre frase.')
w('')
w('## 5. Ambiguidades, pendências e exclusões')
w('')
w('1. **BLOQUEIO À PUBLICAÇÃO — erratas T-17 dos Lotes 6 ainda não aplicadas** (T-17 é PRÓXIMO/PENDENTE; o texto da tarefa diz "ANTES da exportação dos Lotes 6 à plataforma (T-12)"). Segui a ordem de incluir 6a e 6b e **não corrigi o texto** (regra: extrair literalmente). Efeito no JSON: (a) **OB-6b-1**: o curso 4.0.2 do 6b contém a nota interna "Observação para a GCB-CQFP: a Lei 14.129/2021 …" (sem artigo); `lote6_reconciliacao.md` a declara BLOQUEANTE da exportação do 6b à plataforma porque o curso vai à candidata; (b) OB-6a-2/OB-6b-2 ("Derep (antigo DETAQ)" já consta no texto exportado, ver item 4 abaixo); (c) OB-6b-3 (trojan na Nota de produção do 6b, fora do JSON); (d) linha CQFP-1 da Tabela de Correções (fora do JSON); (e) texto "conferência visual humana pendente (BACKLOG)" para TRF6 96/98, que no 6b aparece na seção de itens reais, fora de `itens`. **Recomendação:** a Gerência não deve liberar o `pacote.json` à plataforma antes da T-17; depois dela, reexecutar a T-05/T-12.')
w('2. **TRF6 96/98 (BQ-0011/0012)**: o Lote 6b os descreve como itens de aderência "parcial ao item 4/4.1" (seção ITENS REAIS); o banco, após a T-22, os classifica P1-4 DIRETA. O pacote usa o banco (direta). A divergência é de texto do 6b (cobre a T-17(e) só em parte).')
w('3. **Lote 2, errata E4 (N4)**: a consolidação manda ler menções a "DETAQ" como "Derep (antigo DETAQ)". Há 2 menções a "Departamento de Taquigrafia, Revisão e Redação (DETAQ)" no curso do Lote 2, que mantive literais (definição histórica da fonte F2 [V 08/10/2026]); a E10 do Lote 1 foi aplicada por ter texto de substituição explícito. Os Lotes 6a e 6b já trazem "Derep (antigo DETAQ)".')
w('4. **Lote 3, decisões R1–R5 da GCE**: o arquivo de padrões do Lote 3 abre com "DECISÕES DE RECONCILIAÇÃO DA GCE" (R1–R6). Em `padrao` de D4/D5 entram os quesitos do padrão e a nota R6 (NQ = NC − 3 × NE ÷ TL; pesos são HIPÓTESE), mas **não** o bloco R1–R5 (R2: alínea c da discursiva não exige enquadrar o pronunciamento como obra protegida nem ato oficial, basta uma razão da lista (ix); R3: voz como dado sensível nem exigida nem penalizada; R4: base legal do poder público, art. 23 e art. 7º, II ou III). Os quesitos já refletem essas decisões; a Gerência decide se o bloco deve ser anexado ao `padrao`.')
w('5. **L3-Q21 (REVERIFICAR normativo 4–8/1/2027, "não VOLÁTIL")**: segue a marca do registro GBQ e do arquivo canônico — sem `"volatil"`. A justificativa traz a marca REVERIFICAR e as marcas [NORMATIVO — QA] de origem. Se a plataforma tratar REVERIFICAR como volátil, a lista muda de 18 para 19.')
w('6. **Itens do banco aguardando QA normativo (T-13, T-21)**: os 16 itens de LGPD exportados (os 17 da T-13 menos BQ-0031, anulado), BQ-0036 e BQ-0040 saem como no banco (gabarito do certame de origem, CEBRASPE_ANALOGA); o banco não tem marca "QA PENDENTE", mas a conferência normativa está pendente e o gabarito pode mudar se houver gatilho D. Mantidos em `itens`; não filtrei.')
w('7. **Simulado 0 v0.2 desatualizado nas marcas de aderência**: as marcas dos itens 15, 17, 18, 26, 27, 31 e 57–60 do simulado refletem T-03/T-22 não aplicados ao documento (T-25 pendente). Como o pacote lista só ids do banco, não há conflito; as aderências exportadas vêm do banco.')
w('8. **Uso do Simulado 0 pela candidata (D-SIM0-V02)**: reservado ao Fundador; o uso pela candidata só ocorre após a T-13 concluir sem gatilho D. O JSON não carrega essa restrição (o contrato não tem campo), e o simulado inclui 4 itens VOLÁTEIS e 23 de aderência parcial, aptos só a diagnóstico.')
w('9. **[TS] (troca sutil)** não tem campo no contrato e **não é exportado** como campo; o texto da justificativa não repete a marca. São 91 itens AUTORAL [TS] (P2: 45; P1: 46). Se a plataforma precisar do marcador, é extensão a decidir (como `volatil`).')
w('10. **Excluídos do `itens`**: BQ-0029, 0030, 0031, 0060, 0062 e 0063 (gabarito X, anulados no definitivo). Nenhum item AUTORAL foi excluído; nenhum estava marcado QA PENDENTE.')
w('11. **Discursivas**: D1–D5 só de P2, a partir dos arquivos da GCE (`GCE_Lote1_consolidacao_GCE.md` Parte B para D1; `GCE_Lote2_padroes_GCE.md`; `GCE_Lote3_padroes_GCE.md`) e dos enunciados (e)/(f) dos v2. `saida/discursivas/` está vazia (só .gitkeep). Os padrões de P2 de que não encontrei versão reconciliada com segurança: nenhum (todas as cinco hipóteses dos Lotes 1–3 têm padrão); Lote 1-C não tem discursiva.')
w('12. **Sem mudança de gabarito ou contagem** em relação aos arquivos canônicos; o campo `justificativa` preserva as marcas internas dos autores ([V dd/mm/aaaa], [NORMATIVO — QA]) como estão no texto de origem.')
w('')
open(R + 'pacote_relatorio.md', 'w', encoding='utf-8').write('\n'.join(o) + '\n')
print(len(o))
