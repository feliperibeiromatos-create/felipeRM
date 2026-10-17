# T78_reconciliacao_2026-10-17.md — T-78 (mapeamento adicional P1-DA, reconciliação e D1) — 2026-10-17 — gerado por gbq-gerencia

Bases lidas: linha T-78 de TAREFAS.md; saida/banco/T78_producao_2026-10-17.md (gbq-cfp); saida/banco/QA_T78_2026-10-17_gbq-cqe.md (gbq-cqe); banco/mapeamento_adicional.csv; git diff de banco/ (banco.csv 20 -/20 +, só observacoes; SCHEMA.md +1 parágrafo); DECISOES.md (D-DA-BANCO, D-ADERENCIA). A gbq-gerencia não produz nem revisa: decide o D1 e lista as correções.

## Resultado
PENDENTE da rodada 2. Mapeamento ACEITO quanto ao objeto (20 itens → P1-DA-12, DIRETA; P1-DA-11 = 0; P1-DA-1 a 10 = 0; 6 descartes procedentes); integridade aprovada pelo QA (banco.csv 112 linhas × 18 colunas, só acréscimo em observacoes; schema e contrato v1.2.4 preservados). Fecha quando a gbq-cfp executar a seção "Correções para a gbq-cfp (rodada 2)" e a conferência abaixo der 21 linhas × 7 colunas, 0 marcador "a conferir", 20/20 arbitrado_por preenchido e banco.csv sem diff novo.

## D1 (a) — aderência de BQ-0007 e BQ-0008: DIRETA (leitura A)
- D-DA-BANCO manda mapear a P1-DA-12 com aderência DIRETA os itens reais de LGPD/ANPD, "incluindo TRF6 70–76"; BQ-0007 e BQ-0008 são TRF6 75 e 76. Rebaixar a parcial contrariaria decisão da Presidência (seria gatilho, não D1).
- No mérito, o objeto julgado é a base legal do tratamento pelo poder público (art. 7º, II e III, e art. 23, conferidos pelo QA em 17/10/2026), núcleo da Lei 13.709/2018; P1-DA-12 cobra a LGPD sem o recorte do P2-4.1, e a interpretação da ANPD sobre esses artigos é cobrável numa prova de LGPD. A leitura B (o gabarito se apoia no guia orientativo, não no texto literal) fica registrada como transparência no campo fundamento (correção 4), não como rebaixamento.
- Mapeamento principal (P2-4.1, parcial) intocado; sem efeito em simulado ou pacote (o pacote não exporta o mapeamento adicional).

## D1 (b) — CORRIGIR de BQ-0025 e marcador "a conferir": aceitos (ver correções 1 e 2)

## D1 (c) — leituras alternativas fora do escopo: REGISTRO, sem tarefa nova
- BQ-0111 (Lei 14.129/2021, art. 3º, V) → possível P1-DA-8.3; BQ-0072 (Decreto 1.171/1994, Anexo, XV, e) → possível P1-DA-3 ou P1-DA-4.2. Ambas no máximo parciais (só simulado diagnóstico, D-ADERENCIA), de normas fora da lista da D-DA-BANCO; mapeamento principal (P1-4 e o atual de BQ-0072) intocado.
- Não vira tarefa: ganho baixo (parcial não entra em simulado final) e o mapeamento P1-DA dessas normas exige ampliar a D-DA-BANCO. Reexame na reconciliação da terceira varredura (D-DA-BANCO) ou na abertura do módulo m-da, que leem esta seção.

## Correções para a gbq-cfp (rodada 2)
Arquivo único: banco/mapeamento_adicional.csv. Não tocar banco/banco.csv nem banco/SCHEMA.md. Manter ";" como separador, UTF-8, CRLF, 21 linhas e 7 colunas; nenhum ";" dentro dos campos novos.

1. BQ-0025, coluna fundamento — valor novo, inteiro:
   `LGPD art. 5º, II, e art. 11, I e II (dado sensível, convicção religiosa; consentimento específico e destacado não é a única hipótese: há tratamento sem consentimento no inciso II) [conferido gbq-cqe 17/10/2026, planalto.gov.br compilado]`
2. Todas as 20 linhas, coluna fundamento — substituir o trecho literal `[dispositivo a conferir no compilado pelo gbq-cqe/qa-normativo]` por `[conferido gbq-cqe 17/10/2026, planalto.gov.br compilado]` (em BQ-0025, já coberto pela correção 1).
3. BQ-0002, coluna fundamento — valor novo, inteiro:
   `LGPD art. 9º, caput e III (direito de acesso facilitado às informações sobre o tratamento, identificação do controlador é informação obrigatória), art. 18, II (acessório) [conferido gbq-cqe 17/10/2026, planalto.gov.br compilado]`
4. BQ-0007 e BQ-0008, coluna fundamento — inserir, antes do colchete final, o trecho `, interpretação da ANPD sobre esses dispositivos, gabarito não literal na lei (D1 gbq-gerencia: DIRETA por D-DA-BANCO)`.
5. Todas as 20 linhas, coluna arbitrado_por — valor novo: `gbq-gerencia (D1, saida/banco/T78_reconciliacao_2026-10-17.md)`.
6. Colunas id, item_edital_adicional, aderencia_adicional (`direta` nas 20), decisao e data: sem mudança.

Conferência de fechamento (gbq-cqe, por script, somente leitura): 21 linhas × 7 colunas; 20 ids iguais aos atuais; 0 ocorrência de "a conferir"; 20 ocorrências de "conferido gbq-cqe 17/10/2026"; 20/20 arbitrado_por conforme correção 5; git diff de banco/banco.csv e banco/SCHEMA.md idêntico ao desta reconciliação.

## Errata D1 pós-R2 (gbq-gerencia, 17/10/2026)
Base: saida/banco/QA_T78_R2_2026-10-17_gbq-cqe.md (CORRIGIR, 1 ponto de formato; conteúdo conforme). Limite de 2 rodadas de QA atingido: não há rodada 3 de QA; a gbq-cfp aplica esta errata e a gbq-gerencia confere o fechamento por script, somente leitura.

(a) Errata mecânica da correção 1 (origem do erro: o texto da própria correção 1 desta reconciliação continha ";"). Na correção 1, trocar `convicção religiosa; consentimento` por `convicção religiosa, consentimento`. Nada mais muda. Valor final, inteiro, da coluna fundamento de BQ-0025:
`LGPD art. 5º, II, e art. 11, I e II (dado sensível, convicção religiosa, consentimento específico e destacado não é a única hipótese: há tratamento sem consentimento no inciso II) [conferido gbq-cqe 17/10/2026, planalto.gov.br compilado]`
Execução (gbq-cfp): só a linha BQ-0025 de banco/mapeamento_adicional.csv; substituir esse único ";" por ","; não tocar as outras 20 linhas, banco/banco.csv nem banco/SCHEMA.md; manter UTF-8 sem BOM e CRLF.

(b) Leitura estrita de BQ-0007/0008 (inserção imediatamente antes do "[", com espaço antes da vírgula): REJEITADA. Prevalece a execução aprovada pelo QA R2 ("(orientação da ANPD), interpretação ... ) [conferido ...]"): o trecho literal está íntegro e antes do colchete final; a leitura estrita só degradaria a tipografia. Sem mudança nessas linhas.

Critério de fechamento (conferência por script da gbq-gerencia, depois da aplicação):
1. banco/mapeamento_adicional.csv com 21 linhas, todas com exatamente 7 campos separados por ";" (6 ";" por linha); CRLF em todas, sem LF solto, sem BOM, UTF-8 válido.
2. Linha BQ-0025: fundamento igual byte a byte ao valor final acima; decisao = `D-DA-BANCO`; arbitrado_por = `gbq-gerencia (D1, saida/banco/T78_reconciliacao_2026-10-17.md)`; data = `2026-10-17`.
3. Nas 20 linhas de dados: 20 ids iguais aos atuais; aderencia_adicional = `direta` 20/20; decisao = `D-DA-BANCO` 20/20; arbitrado_por conforme correção 5 20/20; data = `2026-10-17` 20/20; 0 ocorrência de "a conferir"; 20 de "conferido gbq-cqe 17/10/2026".
4. As 20 linhas além de BQ-0025 (cabeçalho e 19 de dados) idênticas byte a byte ao estado conferido pelo QA R2.
5. git diff de banco/banco.csv e banco/SCHEMA.md idêntico ao desta reconciliação (sem diff novo).
Tudo conforme → T-78 FECHADA (aceita pela gbq-gerencia). Qualquer não conformidade → volta à gbq-cfp só para a errata, sem nova rodada de QA.

## Gatilhos
Nenhum. O mapeamento adicional não altera pacote.json, canônico, simulado nem mapeamento principal; a exportação fica para errata de contrato e gatilho A próprios (próxima T-12 ou módulo m-da), como manda a T-78. Nada escrito em PARA_PRESIDENCIA.md.

## Conferência de fechamento pós-errata (gbq-gerencia, 17/10/2026, script próprio, somente leitura)
banco/mapeamento_adicional.csv (mtime 16:39) comparado com cópia do estado conferido no QA R2, tirada antes da errata:
1. 21 linhas, todas com 7 campos (6 ";"); CRLF em todas, sem LF solto, sem BOM, UTF-8 válido: CONFORME.
2. BQ-0025: fundamento idêntico byte a byte ao valor final da errata; decisao D-DA-BANCO; arbitrado_por conforme correção 5; data 2026-10-17: CONFORME.
3. 20 ids iguais aos anteriores; direta 20/20; D-DA-BANCO 20/20; arbitrado_por 20/20; data 2026-10-17 20/20; "a conferir" 0; "conferido gbq-cqe 17/10/2026" 20: CONFORME.
4. Só a linha 11 (BQ-0025) mudou, e a única diferença é a troca de "religiosa; cons" por "religiosa, cons": CONFORME.
5. banco/banco.csv e banco/SCHEMA.md sem diff novo (diff contra HEAD: 20 -/20 + em banco.csv e +1 parágrafo em SCHEMA.md; mtimes 16:30 e 16:31, anteriores à reconciliação): CONFORME.

Resultado: T-78 ACEITA pela gbq-gerencia (mapeamento adicional P1-DA fechado: 20 itens → P1-DA-12, DIRETA). A atualização do estado em TAREFAS.md cabe ao orquestrador. Gatilhos: nenhum.
