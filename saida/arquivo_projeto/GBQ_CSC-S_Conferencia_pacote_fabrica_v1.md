# GBQ-CSC-S — CONFERÊNCIA DO PACOTE DA FÁBRICA (Tarefa B refeita) — 13/10/2026

Objeto: GBQ/pacote_v1_fabrica.json ("Câmara 2026 — pacote F4 (v1.1)", geradoEm 2026-10-10; 240 itens = 180 AUTORAL + 60 banco; 10 lotes; 5 discursivas; SIM-0 e SIM-1; edital com 47 entradas).
Referências: claude/GBQ_Registro_AUTORAL_v3.md (rev. 13/10); GBQ/banco.csv (112 linhas); GBQ/pacote_v1_auto.json (EXEC); GAB_DEFINITIVO_034_TRF6_002_01.pdf (Projeto); gabaritos definitivos em cdn.cebraspe.org.br (WebFetch).
Método: scripts próprios (python3 -I) sobre o JSON e o CSV; nada copiado da pré-conferência da GBQ. Somente leitura: nada foi editado. Não reproduzo enunciados.
Escopo: a CSC-S não revisa conteúdo nem gabarito de item. Os resultados abaixo comparam fontes entre si e com o gabarito oficial.

## RESULTADO EM UMA LINHA
Sem divergência de ID, gabarito, subitem, volátil, aderência ou elegibilidade em (a), (b), (c), (d) e (f). Pontos novos, nenhum bloqueante dos dados: C7 em SIM-1 (comandos com faixa de numeração, 7 de 11 grupos parciais), texto do enunciado do banco ainda não conferido contra o caderno oficial, e 26 aderências "direta" sem declaração explícita no banco.csv.

## (a) 180 AUTORAL × Registro v3
- IDs 1:1 com o registro: 0 faltante, 0 excedente. Gabarito 180/180. Subitem com prefixo P1-/P2- 180/180 (nenhum sem prefixo, R0).
- Total 89 C / 91 E. P1 = 90 (44 C / 46 E); P2 = 90 (45 C / 45 E). Iguais ao registro.
- volatil=true em 15 itens, exatamente os 15 inaptos do registro (14 VOLÁTIL + L3-Q21). L3-Q21 vem como volatil=true com a nota "REVERIFICAR (normativo) 04–08/01/2027; não VOLÁTIL" na justificativa. A EXEC o trazia volatil=false com REVERIFICAR em observacao. Conservador; aceito.
- aderência "direta" 180/180.
- [TS]: o pacote da fábrica não tem o campo. Registro: "não exportado". Não conferível pelo pacote; a marca fica só no Registro v3.
- Base da conferência: minha transcrição das 180 linhas do Registro v3 (feita em 12/10), com os totais por lote recontados e iguais à tabela "Totais" da rev. 13/10. Limite: as 180 linhas da rev. 13/10 não foram retranscritas; a rev. declara que só mudaram R4, R5 e R6.

## (b) Lotes 6a e 6b × v3
- 6A: 15/15 e 6B: 15/15 em gabarito e subitem, 0 divergência. [TS] não exportado.
- R6 (errata A-6b-1 / T-17): em 6B, 0 ocorrência de "[sic]", de "usuario" e de "pendente (BACKLOG)".

## (c) 60 itens do banco × GBQ/banco.csv e × gabarito oficial
Composição:
- 60 IDs únicos = BQ-0001 a BQ-0066 menos os 6 anulados (BQ-0029, 0030, 0031, 0060, 0062, 0063). Nenhum anulado no pacote. O banco.csv tem 112 linhas; BQ-0067 a BQ-0112 (46) ficam fora do pacote v1.1.
- Rótulo CEBRASPE_ANALOGA em 60/60.
Pacote × banco.csv:
- Gabarito, subitem, número, ano, url (caderno), certame, cargo, rótulo e enunciado (igualdade exata) coincidem nos 60. Volátil coincide: BQ-0015, 0017, 0035 e 0064.
- 0 "QA PENDENTE" e 0 "QA REPROVADO", no banco.csv e no pacote. As 6 linhas "aguarda qa-normativo" (BQ-0072, 0077, 0084, 0109, 0110, 0111) estão fora do pacote.
- Base de comando: BQ-0049, 0050 e 0051 trazem textoBase (texto-base do banco.csv); nos outros 237 itens textoBase = "nenhum" (string).
- Justificativa: vazia nos 60 do banco (esperado: item oficial não traz comentário da fábrica).
Aderência:
- No pacote: 37 DIRETA / 23 PARCIAL, igual à T-25. As 23 PARCIAL: 17 de P2-4.1, 2 de P1-8.3, 1 de P1-5.3, 1 de P1-6, 1 de P1-7.1, 1 de P1-8.1.
- O banco.csv não tem coluna de aderência; vem em texto livre. Das 23 PARCIAL do pacote, as 23 têm declaração PARCIAL (ou "temática ampla"/"apenas por tema") nas observações. Das 37 DIRETA, 11 têm declaração DIRETA e 26 não têm declaração explícita (BQ-0010, 0013, 0018 a 0022, 0026 a 0028, 0033, 0034, 0041 a 0044, 0047, 0048, 0050, 0051, 0054, 0058, 0061, 0064 a 0066). Nenhuma contradição; são 26 casos que o banco.csv não permite conferir.
- BQ-0011 e BQ-0012 (TRF6 96 e 98): DIRETA ao P1-4 no pacote e no banco.csv. TRF6 70–76 (BQ-0002 a BQ-0008): PARCIAL nos dois.
R3 (itens reais contados uma vez):
- TRF6 2024, Cargo 2: 63 = BQ-0001; 70–76 = BQ-0002 a BQ-0008; 80 = BQ-0009; 81 = BQ-0010; 96 e 98 = BQ-0011 e BQ-0012. Chave (certame, cargo, nº) sem duplicata nos 60; nenhum enunciado repetido nos 240.
Gabarito definitivo oficial (conferência independente do banco.csv):
- TRF6 (BQ-0001 a 0012): 12/12 contra GAB_DEFINITIVO_034_TRF6_002_01.pdf (Projeto). Anulados do PDF: 58, 105 e 117; nenhum está no pacote.
- Demais 10 gabaritos (BCB, ANATEL, SUSEP, CNJ, ANTT, Embrapa 026, 034 e 071, ANM, PF 106_PF_004_01): 48/48 gabaritos C/E coincidem, e os 6 anulados do banco (BQ-0029, 0030, 0031 = SUSEP 62, 63, 79; BQ-0060, 0062, 0063 = ANM 92, 95, 96) aparecem como X no gabarito oficial. Total conferido: 60 itens do pacote + 6 anulados = 66/66.
- Método e limite: leitura por WebFetch, que devolve texto extraído por modelo, com células coladas. Pedi a tabela bruta inteira, separei as letras, exigi 20 por linha e conferi a posição dos X contra uma primeira leitura independente. As posições dos X coincidem nos 9 PDFs em que comparei as duas leituras (todos menos o BCB), exceto ANTT (primeira leitura em 15, 16 e 34; tabela bruta em 16, 17 e 35; nenhum é item do pacote). BCB: uma tabela bruta e uma leitura direta, concordantes. Embrapa 071: só leitura por trecho (linhas 71–100), sem a tabela inteira. Como 66/66 coincidem com o banco.csv, o risco de número trocado é baixo; mas isto confere NÚMERO e RESPOSTA, não o TEXTO do enunciado contra o caderno. Texto × caderno: NÃO EXECUTADO.

## (d) 150 AUTORAL comuns × pacote da EXEC
- Gabarito 0 diferença; subitem 0 diferença.
- Enunciado: 149/150 idênticos. Diferença só em L1-Q04: a fábrica tem um espaço depois do travessão em "áudio– texto" (posição 63). Defeito de forma.
- Comando: fábrica = comandoOriginal da EXEC nos 60 itens em que a EXEC o tem (Lotes 4, 4-C, 5, 5-C), e = comando da EXEC nos outros 90. 0 diferença.
- Volátil: 1 diferença, L3-Q21 (fábrica true; EXEC false), já descrita em (a).
- Justificativa: 143/150 iguais. As 7 diferentes: L1C-Q24 (a fábrica retirou a marca de verificação), L1C-Q26 (aspas duplas trocadas por simples), L3-Q21 (acréscimo da nota REVERIFICAR), L4-08 e L4-09 (acréscimo de "(v3 — O12)"), L4-11 (de "gabarito a confirmar" para "gabarito definitivo E, conferido"), L4-13 (acréscimo de "(O1)").

## (e) Decisões de forma da EXEC — presença ou ausência
- Comando normalizado para "julgue os itens a seguir." (60 itens, Lotes 4, 4-C, 5, 5-C), com o texto original em comandoOriginal: AUSENTE na fábrica. A fábrica traz o comando original e não tem o campo comandoOriginal (0/240). Divergência de forma, não de dado; ver C7.
- Justificativa sem prefixo de metadados (gabarito, [TS], VOLÁTIL, subitem): PRESENTE nos dois (0/180 com prefixo na fábrica).
- Referências internas mantidas nas justificativas: PRESENTES na fábrica em 17 itens (L2-Q23; L4-08, 09, 13, 15, 17, 18, 19, 20; 4C-06, 08, 09; A5-14 a A5-17; 5C-06). Mesma lista da GBQ.
- Lotes complementares (1-C, 4-C, 5-C) como lotes próprios: PRESENTE. 4-C e 5-C sem curso nem resumo; 1-C com adendo no curso e sem resumo.
- itensEdital das discursivas inferidos: não verifiquei nesta conferência (é matéria da GCE).
- Lotes: curso, resumo e pegadinhas da fábrica diferem da EXEC em forma e extensão (pegadinhas: L1 8 × 31; L1-C 1 × 4; L2 8 × 42; L3 7 × 42; L5 14 × 52; L4 32 × 32). Não diffei o conteúdo (fora do escopo da CSC-S). Concordo com a GBQ (F3): a fábrica agrupa por subitem.

## (f) Checklist C0–C12 (protocolo v1.2; C13 revogada em 12/10)

### SIM-0 "Simulado 0 — diagnóstico (v0.2)" (diagnóstico; 60 itens do banco)
- C0/R0: CONFORME (60 IDs, nenhum repetido, todos no pacote; todo itemEdital com prefixo; P1 43 e P2 17; rótulo CEBRASPE_ANALOGA 60). NÃO CONFERÍVEL: N declarado e arquivo/versão (o pacote só traz id, nome, tipo e a lista de IDs).
- C1: CONFORME (diagnóstico permite). Voláteis presentes: BQ-0015, 0017, 0035, 0064. Inaptos do registro AUTORAL presentes: nenhum.
- C2: CONFORME (BQ-0010 presente; L4-11 ausente).
- C3: CONFORME (BQ-0002 a 0008, 0011 e 0012 uma vez cada; chave duplicada: nenhuma).
- C4: CONFORME (23 PARCIAL, todos em simulado diagnóstico).
- C5: CONFORME por construção (só reais; não há bloco AUTORAL). Comparação AUTORAL × reais: não aplicável.
- C6: CONFORME (gabarito e subitem do pacote = banco.csv nos 60; nenhum anulado; gabarito oficial: 12/12 TRF6 e 48/48 dos demais, ver (c)). Texto × caderno: NÃO CONFERÍVEL.
- C7: CONFORME (nenhum comando com faixa de ID; BQ-0049 a 0051 com textoBase).
- C8: CONFORME (subitens: P1-4 ×4, P1-5 ×1, P1-5.1 ×1, P1-5.2 ×13, P1-5.3 ×10, P1-6 ×2, P1-7.1 ×3, P1-8.1 ×3, P1-8.2 ×3, P1-8.3 ×3, P2-4.1 ×17; todos no edital do Cargo 11).
- C9: não se aplica (diagnóstico). P1-8.3 presente: BQ-0017, 0035, 0048.
- C10: CONFORME (nenhum enunciado repetido).
- C11: contagem de IDs CONFORME (60). N/tempo declarados: NÃO CONFERÍVEL. Referência derivada: 60 × 100 s = 100 min.
- C12: C 33 / E 27 (P1 43: 23 C / 20 E; P2 17: 10 C / 7 E), igual ao informado pela GBQ. Distribuição do banco: sem referência no registro (reais).
- Observação: na lista, os 4 itens de P1-4 (BQ-0011, 0012, 0038, 0039) vêm depois do bloco de 17 itens de P2-4.1; blocos por prova não contíguos. Não é regra do checklist.

### SIM-1 "Simulado 1 — P1 final (TI e Dados, itens 5 a 8)" (final; 40 AUTORAL)
- C0/R0: CONFORME (40 IDs, nenhum repetido, todos no pacote; itemEdital com prefixo; P1 40; AUTORAL 40). NÃO CONFERÍVEL: N declarado e arquivo/versão.
- C1: CONFORME (0 volatil=true; 0 dos 15 inaptos).
- C2: CONFORME (L4-11 ausente; BQ-0010 ausente).
- C3: CONFORME (nenhum item real; TRF6 70–76, 96 e 98 ausentes).
- C4: CONFORME (aderência direta 40/40).
- C5: CONFORME (só AUTORAL; comparação AUTORAL × reais: não aplicável).
- C6: CONFORME (gabarito e subitem = Registro v3 nos 40; nenhum anulado).
- C7: CONFORME quanto ao original preservado; NÃO CONFERÍVEL quanto à numeração do simulado montado. Os 40 itens vêm de 11 grupos de comando com faixa de numeração. Grupos completos (4): L4 "17 a 20" (4/4), A5-01 a A5-04 (4/4), A5-05 a A5-07 (3/3), A5-18 a A5-20 (3/3) = 14 itens. Grupos parciais (7): L4 "1 a 6" (4 de 6), L4 "7 a 11" (4 de 5), L4 "12 a 16" (4 de 5), 4C-01 a 4C-10 (4 de 10), A5-08 a A5-13 (4 de 6), 5C-01 a 5C-06 (3 de 6), 5C-07 a 5C-10 (3 de 4) = 26 itens. Pela decisão da EXEC, esses comandos eram normalizados "para funcionar em simulado embaralhado"; a fábrica os trouxe no original. Pelo edital 8.2 (julgamento vinculado ao comando), faixa que cita itens fora do simulado, ou numeração de lote, exige normalização declarada na montagem. Decisão da GBQ.
- C8: CONFORME (P1-5.1 ×8, P1-5.2 ×4, P1-5.3 ×4, P1-6 ×4, P1-7.1 ×4, P1-8.1 ×3, P1-8.2 ×7, P1-8.4 ×6).
- C9: CONFORME (D-83-SIMULADO: 0 item de P1-8.3; ausência registrada). Alertas do registro (P2-1.8, P1-2, P1-4, P1-3) não se aplicam a este recorte.
- C10: CONFORME.
- C11: contagem de IDs CONFORME (40). N/tempo declarados: NÃO CONFERÍVEL. Referência derivada: 40 × 100 s = 66,7 min.
- C12: C 20 / E 20 (igual ao informado pela GBQ). [TS] (do Registro v3, não do pacote): 19 de 40, 8 deles com gabarito C. Referência do registro P1: 46/90 e 18/90 (descritiva; sem limiar fixo).
- C13: REVOGADA em 12/10.

## DIVERGÊNCIAS COM A PRÉ-CONFERÊNCIA DA GBQ (GBQ/pacote_fabrica_conferencia_GBQ.md)
Divergência de número, ID, gabarito, subitem, volátil, aderência ou composição: nenhuma. Confirmo: 180/180 e 30/30; 149/150 enunciados (L1-Q04); 143/150 justificativas (os mesmos 7 IDs); 60 = 66 − 6; 37/23 (com a mesma quebra das 23); voláteis 0015, 0017, 0035, 0064; TRF6 sem dupla contagem; SIM-0 60 itens, 33/27, P1 43 / P2 17; SIM-1 40 itens, 20/20 e os mesmos subitens; 17 justificativas com marca interna; "QA PENDENTE" 0; "a confirmar" 0; "CONTEXTO NORMATIVO INTERNO" 1; "Derep, antigo" 1 (no resumo/curso do Lote 1).
Acréscimos meus, que a pré-conferência não trazia:
1. C7 em SIM-1: 40/40 itens em grupos de comando com faixa; 7 de 11 grupos parciais (detalhe acima). A pré-conferência registra que a fábrica não normalizou os comandos, mas não a consequência para o SIM-1.
2. A EXEC tinha normalizado os comandos de faixa e guardado o original em comandoOriginal; a fábrica não tem o campo.
3. Conferência independente do banco.csv: 66/66 contra o gabarito oficial (12 no PDF do Projeto; 54 em 10 PDFs do CDN, 6 deles anulados). A pré-conferência compara com o banco.csv, que é da mesma fábrica.
4. Aderência: 26 itens DIRETA sem declaração explícita no banco.csv.
5. Os 60 itens do banco têm justificativa vazia.
6. Inconsistência de redação na própria GBQ: a CIÊNCIA de 12/10 diz que TRF6 96 e 98 são "parciais (C4/R4)" e seguem fora de simulado final; o Registro v3 rev. 13/10, o banco.csv e o pacote dizem DIRETA ao P1-4. Apliquei a rev. 13/10. Peço confirmação de que a redação "parciais" da CIÊNCIA está superada.
7. Texto de enunciado × caderno oficial dos 60: NÃO EXECUTADO por nenhuma das duas conferências.

## PARECER AO GATILHO A
SEM OBJEÇÃO ao gatilho A sobre os dados do pacote da fábrica (itens, gabaritos, banco, composição de SIM-0 e SIM-1), nos limites acima. Ressalvas que não bloqueiam o gatilho:
- R-1 (C7): SIM-1 está definido como lista de IDs. Antes de existir como documento montado, a GBQ decide a numeração e a normalização dos comandos de grupo (7 grupos parciais). Enquanto isso, C0 (N declarado), C7 (numeração) e C11 (tempo) ficam NÃO CONFERÍVEIS.
- R-2: texto do enunciado dos 60 itens do banco contra o caderno oficial não foi conferido.
- R-3: 26 aderências DIRETA sem declaração explícita no banco.csv.
- Os defeitos de forma F1 a F5 da GBQ ficam como estão classificados por ela (PRÓXIMO).
O gatilho A é emitido pela GBQ.

## Pendências classificadas
- AGORA: GBQ confirma que a redação "parciais" para TRF6 96 e 98 na CIÊNCIA de 12/10 está superada pela rev. 13/10 (uma linha).
- AGORA (GBQ): emitir ou não o gatilho A (matéria da GBQ).
- PRÓXIMO: GBQ define numeração e normalização dos comandos de grupo do SIM-1 (R-1).
- PRÓXIMO: F1 a F5 da GBQ (v1.2 do pacote ou T-12).
- BACKLOG: texto do enunciado × caderno dos 60 itens (R-2); depende de texto literal do PDF.
- BACKLOG: [TS] no pacote ("não exportado"), caso a GBQ queira o campo no JSON.
- DESCARTADO: GBQ-CSC-BQ para gabarito, número e anulação (feito pela CSC-S).

FIM DA CONFERÊNCIA
