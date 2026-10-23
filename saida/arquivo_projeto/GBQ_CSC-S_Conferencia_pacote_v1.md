# GBQ-CSC-S — CONFERÊNCIA DO PACOTE.JSON v1 (Tarefa B) — 12/10/2026

Objeto: GBQ/pacote_v1_auto.json (versão 1, geradoEm 2026-10-12; 157 itens; 8 lotes; 5 discursivas; edital com 40 entradas; simulados vazio). Contra: claude/GBQ_Registro_AUTORAL_v2.md; GAB_DEFINITIVO_034_TRF6_002_01.pdf (Projeto). Método: transcrição integral das 150 linhas do registro para arquivo e comparação por script (python3 -I) com itens[].id, gabarito, itemEdital, ts, volatil, observacao, rotulo e aderencia. Não editei nada.

## RESULTADO

AUTORAL (150): CONFERIDO. Divergências por ID: nenhuma.
Itens reais do pacote (7: TRF6-2024-C2-070 a 076): CONFERIDO contra o gabarito definitivo do Projeto.
Cruzamento com o banco (itens reais e anulados): NÃO EXECUTÁVEL, porque banco/banco.csv não está no Projeto (o próprio pacote o declara em "exclusoes"). Não é divergência de ID; é conferência pendente.

## Detalhe

1. IDs: 157 únicos. Dos 157, 150 coincidem com os 150 do registro (nenhum faltante, nenhum excedente) e 7 são os TRF6 (R3).
2. Gabarito: 150/150 iguais ao registro. Subitem (P1- ou P2- + subitem): 150/150. [TS]: 150/150. Contagens por lote iguais à tabela "Totais" do registro (L1 20: 10 C/10 E/10 TS; L1C 10: 4/6/5; L2 30: 15/15/15; L3 30 AUTORAL: 16/14/15; L4 20: 10/10/10; L4C 10: 5/5/5; A5 20: 10/10/10; L5C 10: 5/5/5). Total AUTORAL: 75 C, 75 E, 75 [TS]. Cobertura por subitem igual à do registro (P1: 5.1=16, 5.2=5, 5.3=5, 6=4, 7.1=4, 8.1=3, 8.2=12, 8.3=4, 8.4=7; P2: 1.1=4 ... 4.1=5 AUTORAL + 7 reais = 12, 4.2=5, 4.3=4).
3. Marcas: volatil=true exatamente em 9 IDs (L1-Q14, Q16, Q18, Q19; L4-15; A5-14 a A5-17), cada um com a reverificação em observacao. REVERIFICAR: só L3-Q21 (volatil=false, "REVERIFICAR" em observacao), conforme o registro. Nenhuma marca indevida em item não marcado. R1/R1-N: 10 itens, os mesmos 10 do registro.
4. Rótulo e aderência: 150 AUTORAL com aderencia "direta"; 7 reais CEBRASPE_ANALOGA com aderencia "parcial".
5. Itens reais 70 a 76, gabaritos do pacote: 70 E, 71 E, 72 E, 73 C, 74 C, 75 C, 76 C. Gabarito definitivo (PDF do Projeto, lido por posição das colunas; a extração de texto do PDF vem desalinhada e a leitura foi feita contando posições): 70 E, 71 E, 72 E, 73 C, 74 C, 75 C, 76 C. Iguais. Anulados no PDF: 58, 105 e 117; nenhum está no pacote. Os itens 63, 80 e 81 do TRF6 não estão no pacote (R2 não se aplica ao pacote).
6. Verificações adicionais: itemEdital de todos os itens existe no edital do pacote; nenhum enunciado duplicado; nenhum item com gabarito fora de {C, E} ou enunciado vazio; todos os 157 itens têm comando; 60 itens trazem comandoOriginal.

## Pontos para a GBQ (não são divergências por ID)

1. Aderência "parcial" dos 7 itens TRF6. O pacote os marca assim por decisão da EXEC (base: GCE_BIP_retorno_v2.md). Pelo D-ADERENCIA, "parcial" os exclui de simulado final. Se a GBQ os considera "direta", o pacote precisa de correção (competência da EXEC/GBQ, não da CSC-S).
2. Banco: o cruzamento com o banco depende de banco.csv no Projeto. Também fica aberta a dedup P9 × BQ (D-DEDUP-P9, GBQ): os 7 itens TRF6 estão no pacote com ID próprio e, segundo a R3, também são itens do banco; sem o banco não verifico se há contagem dupla.
3. L3-Q21: volatil=false por desenho; o montador de simulados deve excluir também quem tiver "REVERIFICAR" em observacao (já anotado no QA da EXEC; repito por ser regra R1-N).
4. Lotes 6a/6b: fora do pacote v1 e fora do registro v2; um pacote v2 ou o Registro v3 exigirá nova conferência.

## Para o gatilho A

Os 150 AUTORAL e os 7 reais do pacote não têm divergência. Se a GBQ aceita emitir o gatilho A sem o cruzamento com o banco (por o pacote conter só AUTORAL e 7 itens reais cujo gabarito foi verificado no PDF), a CSC-S não tem objeção; se exige o cruzamento, ele aguarda o banco.csv.

FIM DA CONFERÊNCIA
