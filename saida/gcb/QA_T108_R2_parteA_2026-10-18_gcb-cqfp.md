# QA_T108_R2_parteA_2026-10-18_gcb-cqfp.md — T-108 (ORDEM_V15_C, limpeza), QA R2 (última rodada) da GCB, Parte A (lotes 4 e 4-C) — 2026-10-18 — gerado por gcb-cqfp

Objeto (D1 pós-R1, seção 6): as 33 linhas corrigidas da `saida/gcb/T108_substituicoes_GCB_parteA_v2.csv` (27 de formato, A0078, A0025 e as 4 de ", às avessas") e as 4 linhas novas GCB-A0179 a A0182 (GCB-EXTRA-01 a 04). As 145 linhas restantes, aprovadas na R1, não voltam ao mérito: só se confere que estão byte a byte iguais à v1. Resposta do produtor conferida contra a seção "Parte A" de `saida/gcb/T108_producao_notas_GCB_v2.md`. Texto-base: `saida/pacote/pacote.json` v1.10, SHA-256 LF d43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed (conferido). Somente leitura; nada foi corrigido nem redigido.

## 1. Veredito da Parte A

**APROVADO.** Objeto: 37 linhas, 37 APROVADO e 0 REPROVADO. Percentual de reprovação: 0,0% (0/37). Nenhuma linha volta à D1 da GCB. A v2 inteira (182 linhas) passa na mecânica sem falhas.

## 2. Conferência mecânica

Script próprio (python -I -X utf8), fora do repositório, em `C:\Users\Felipe\AppData\Local\Temp\gcbqa_r2a\q.py`. Ele carrega `saida/pacote/T108_inventario.py` (funções `campos` e `varre`) a partir de uma cópia e aplica a v2 numa cópia do pacote em memória. Nada foi gravado no repositório além deste parecer.

| Checagem | Resultado |
|---|---|
| (a) v1 × v2, com reserialização QUOTE_ALL/LF idêntica byte a byte aos dois arquivos | Cabeçalho igual; 0 linhas removidas; ordem da v1 preservada; 4 linhas novas no fim (A0179 a A0182). **145 linhas byte a byte iguais à v1.** As 33 alteradas são exatamente as do objeto: as 27 de formato mudam só `acao` (DELETAR → SUBSTITUIR); A0078 muda `antes` e `depois`; A0025, A0111, A0126, A0147 e A0155 mudam só `depois`. SHA-256: v1 3e83a970…, v2 05b45e71…. |
| (b) `antes` literal e único no campo da v1.10; caminho válido; sem sobreposição em todo o conjunto v2 (182 linhas) | 0 falhas |
| (c) cobertura | As 196 ocorrências PROCESSO + VERIFICAR dos lotes 4 e 4-C no `T108_ocorrencias.csv` estão cobertas uma vez cada (0 faltando, 0 repetidas). GCB-EXTRA-01 a 04 aparecem uma vez cada. Nenhum outro id fora do CSV. Cada casamento do inventário cai dentro do `antes` da sua linha, com caminho e categoria coerentes. |
| (d) aplicação da v2 numa cópia e nova `varre` dos lotes 4 e 4-C | 0 PROCESSO e 0 VERIFICAR. 33 FP-CONTEUDO, os mesmos ids antes e depois. FP-R1 0 → 0. "A tecla F4" (6a) intacta: 1 → 1. |
| (d) resíduo das marcas da seção 5, (6), no texto resultante dos lotes 4 e 4-C | 0 casamentos de "(O11)", "fundamenta item", "neste chat", "não sutil", "entra em item", "entram em item", "(CI,", "ITENS REAIS", "TC invertida", "indevida invertida", "Não usada em item", "invertida", "em sentido invertido" e "hoje". ", às avessas" aparece só em L4-05, L4-11, L4-20 e 4C-03, uma vez cada. |
| (e) formato | Nenhum DELETAR com `depois` não vazio; nenhum SUBSTITUIR vazio; nenhum MANTER; `fonte_origem` presente em todas as linhas de regra 2. Contagens: SUBSTITUIR 167, DELETAR 15; lote 4 = 151, 4-C = 31; regra 2 = 112, 3 = 8, 4 = 31, 5 = 31. Batem com a nota de produção. |
| (e) campos intactos | Enunciado, comando, textoBase, gabarito, itemEdital, aderencia, volatil e todos os demais campos de itens e lotes iguais, fora os tocados (curso, resumo, pegadinhas[].texto, pares[].como, justificativa). Rótulos de pegadinhas e chaves de topo iguais. |
| Tipografia nos campos tocados (espaço duplo, espaço antes de pontuação, parêntese vazio ou aberto com espaço, ponto duplo) | Nenhum caso novo |

## 3. Mérito

- **Formato (27 linhas):** só `acao` mudou para SUBSTITUIR. `antes`, `depois`, `regra` e `nota` ficaram como na v1, como o R1 pediu. Amostra do texto resultante: A0060 "(Decreto 1.171/1994, Anexo, Capítulo I)", A0102 "verificada em 08/10/2026", A0174 " como critério".
- **A0078:** texto exato do R1 (`antes` com o espaço inicial, `depois` vazio, DELETAR, regra 5). O texto resultante fica "…com mobilidade reduzida (XIX).", seguido de "Código de Ética (Decreto 1.171/1994, …)". Sai a instrução interna, sem perda de conteúdo.
- **A0025:** `depois` é o texto exato do R1, seção 6. Os dois títulos de fonte constam de `T108_fontes_GCB.md`, lote 4, F1 e F2 (07/10/2026). Não entra fonte nova.
- **", às avessas" (A0111, A0126, A0147, A0155):** só "invertida" foi trocado por ", às avessas". O resto do `depois` ficou igual à v1. A forma é a da seção 3 do D1 e a da Parte C já aprovada.
- **A0179 (EXTRA-01):** fica "Distinção de vocabulário: CLASSIFICAR é uma TAREFA; …". Sai só o código de lição. Obs. sem efeito: a nota de produção descreve o resultado entre parênteses, mas o texto não tem parênteses ali.
- **A0180 (EXTRA-02):** fica "…pelo exercício irregular de suas atribuições.", seguido de "Marco Civil da Internet (…)". A base legal do art. 121 da Lei 8.112/1990 fica, com o artigo citado. Sai só a instrução interna.
- **A0181 (EXTRA-03):** fica "(marco legal da IA; situação de tramitação não verificada), ele fica só como contexto, sujeito a mudança." (resultado combinado com a linha da v1 que já cobria "VOLÁTIL e não entra em item"). A informação útil fica e não entra fato novo.
- **A0182 (EXTRA-04):** combinada com A0178, fica "Armadilha: troca de conceito (formato × restrição)." Sai só a nota de classificação. Português correto.
- Normativo: nenhuma linha do objeto introduz citação de lei. O único dispositivo próximo (art. 121 da Lei 8.112/1990) é texto já existente e traz o artigo. Nada PENDENTE.
- Evidência: a R2 não introduz fonte, URL nem data. A tabela de fontes não muda na Parte A (a única linha acrescentada em `T108_fontes_GCB.md` é a CI do Lote 5, objeto da Parte C).

## 4. Tabela do objeto (37 linhas)

| id_edicao | tipo | veredito | motivo |
|---|---|---|---|
| GCB-A0060, A0061, A0063, A0064, A0065, A0066, A0067, A0068, A0069, A0070, A0071, A0072, A0073, A0074, A0075, A0076, A0077, A0079, A0080, A0081, A0082, A0083, A0087, A0092, A0100, A0102, A0174 (27) | formato | APROVADO | `acao` = SUBSTITUIR; demais colunas iguais à v1; mecânica sem falha |
| GCB-A0078 | mérito R1 | APROVADO | texto exato do R1; DELETAR com `depois` vazio; texto resultante correto |
| GCB-A0025 | português R1 | APROVADO | texto exato do R1; fontes F1/F2 na tabela do lote 4 |
| GCB-A0111 | ", às avessas" | APROVADO | só a troca prevista na seção 3 |
| GCB-A0126 | ", às avessas" | APROVADO | idem |
| GCB-A0147 | ", às avessas" | APROVADO | idem ("…, às avessas. LAI") |
| GCB-A0155 | ", às avessas" | APROVADO | idem |
| GCB-A0179 | nova, EXTRA-01 | APROVADO | `antes` " (O11)" único; DELETAR; C02/5 conforme seção 2 |
| GCB-A0180 | nova, EXTRA-02 | APROVADO | `antes` " Não fundamenta item." único; DELETAR; C10/5; base legal preservada |
| GCB-A0181 | nova, EXTRA-03 | APROVADO | `antes` " neste chat" único; DELETAR; C08/5; informação útil preservada |
| GCB-A0182 | nova, EXTRA-04 | APROVADO | `antes` "; não sutil" único, sem sobreposição com A0178; DELETAR; C06/4 |

Linhas fora do objeto: 145, byte a byte iguais à v1 (APROVADAS na R1; não reexaminadas no mérito).

Pendências: nenhuma na Parte A. Segue para a reconciliação e consolidação da GCB (D1 pós-R1, seção 7).
