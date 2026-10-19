# V15_BAEF_reconciliacao_GCB_2026-10-18.md — T-110 (B), T-111 (A), T-112 (E), T-113 onda 1 (F1), P1 — reconciliação final da GCB — ciclo 2026-10-18 s14c3 — gerado por gcb-gerencia

Normas: saida/gcb/V15_BAEF_D1_GCB_2026-10-18.md (seções 0 a 6); saida/gcb/T113_P1_D1_pos_R1_2026-10-18.md; D1 da GBQ saida/pacote/V15_BAE_D1_GBQ_2026-10-18.md (contrato v1.2.9, seções 1 a 4); D-V112-ESCOPO; D-V15-ENCOMENDA; D-REFORCO-2; D-FONTE-DATA-ANTERIOR; D-COMPLEMENTOS; D-V15-PLATAFORMA.
Conferência por script próprio (`python -I`, scratchpad, somente leitura) sobre os seis arquivos finais e sobre saida/pacote/gerador_v1_11/out/pacote.json (v1.11 canônico). A GCB não produz nem revisa; nenhum arquivo de produção ou de QA foi alterado. Nada vai à plataforma nem à candidata.

## 1. Arquivos finais (os únicos que a GBQ consome para P1 na v1.12)

| Frente | Arquivo final | SHA-256 | Bytes | Fim de linha / linhas | Parecer final |
|---|---|---|--:|---|---|
| B | saida/gcb/T110_pegadinhas_P1_v2.md | d3bbfd5b786ce1e1eed8f306009527f022878f421175234e7305dc905752a756 | 68272 | LF / 524 | R2 APROVADO (saida/gcb/QA_T110_P1_R2_2026-10-18_gcb-cqfp.md) |
| B | saida/gcb/T110_registro_P1_v2.csv | c5400b141984cea345f92d13e2acb26c4cfa4cf22d403e948014ccb117ddc222 | 20279 | LF / 73 | idem |
| A1 | saida/gcb/T111_resumos_P1_parte1_v2.md | 46446cbb4ad8b4b22f9b604f818025166c7453f905949c7a659c02a3bb199be3 | 8657 | LF / 74 | R2 APROVADO (saida/gcb/QA_T111_P1_parte1_R2_2026-10-18_gcb-cqfp.md) |
| A2 | saida/gcb/T111_resumos_P1_parte2_v2.md | 187ac80c4b63dcc976b2d8034037811264a1029b4ed0bce8f640615395f8ebd1 | 102254 | LF / 712 | R2 APROVADO (saida/gcb/QA_T111_P1_parte2_R2_2026-10-18_gcb-cqfp.md) |
| E | saida/gcb/T112_piloto_P1-8.2_v2.md | 7c7d3d4b98098d6703224984f11e2679104508db7cab40c2327654d0fb88a009 | 8575 | LF / 144 | R2 APROVADO (saida/gcb/QA_T112_P1_R2_2026-10-18_gcb-cqfp.md) |
| F1 | saida/gcb/T113_onda1_P1_v2.md | 0b863e476f14d01ef801635b0e67998b24924213723d96c4a791e26c7dd6da4f | 31751 | LF / 324 | R2 APROVADO (saida/gcb/QA_T113_P1_R2_2026-10-18_gcb-cqfp.md) |

Os _v1 e os pareceres R1 ficam como rastro e não entram na v1.12. Nenhuma parte tem elemento "não aprovado em QA", tópico sem resumo ou item diferido: não há saldo da T-110 a T-113 de P1.

## 2. Conferência por script

Em cada .md, exatamente 1 bloco ```json```, JSON válido.

**B (T-110)**
- CSV: 72 linhas; 46 CONVERTIDO, 26 DESCARTADO (d1 22, d3 4; d2, d4 e d5 zero). Por lote: L4 10 C / 10 D; L5 13 / 2; L6A 11 / 8; L6B 12 / 6.
- json: chaves L4, L5, L6A, L6B com 11, 13, 12 e 13 pegadinhas = 49 textos (3 pares de três termos desdobrados). Multiconjunto dos textos do CSV (com " || " desdobrado) = o do json.
- Cada elemento só com `apos` (inteiro), `itemEdital` (id de P1 do edital), `rotulo`, `texto`; todos começam com "Não confunda "; maior texto 320 caracteres (limite).
- Varredura das 10 categorias nos textos e rótulos: zero.

**A (T-111)**
- A1: chave única "P1-8.2", campo único `resumo`. A2: 16 chaves na ordem do edital (P1-1 … P1-8.4), campo único `resumo`. Total P1: 17 resumos (os 17 tópicos de P1 com curso; P1-5, P1-7 e P1-8 sem resumo, como manda a D1).
- Regra de tamanho da GCB (D1, seção 3) cumprida nos 17: 3 a 6 parágrafos (P1-1 e P1-3 com 7, pela exceção), até 60 palavras por parágrafo, 83 a 274 palavras, de 9,4% a 37,7% do curso; quebra só por `\n\n`; nenhum parágrafo começa com algarismo, marca de lista ou RÓTULO em maiúsculas com dois-pontos.
- Varredura: só as exceções já admitidas pela QA ("F4" e "versão" em P1-1; "versões" em P1-4.1; "instrução" em P1-5.1; "Difere do dashboard" em P1-8.4). Zero marca de produção.
- Nota: minha segmentação do curso dá 31,0% no P1-8.2 contra 31,3% do parecer (diferença de contagem de palavras do bloco, sem efeito: ambos abaixo de 40%).

**E (T-112)**
- Chave "P1-8.2" com só `emUmMinuto` e `visuais`. `emUmMinuto`: 3 strings de 118, 108 e 118 caracteres (≤ 140).
- `visuais`: `tabela` (titulo, colunas ["Gráfico","Variáveis","O que mostra","Armadilha"], 5 linhas com 4 células, maior célula 45, legenda) e `esquema` (titulo, centro, 6 ramos, maior 65). Nenhum campo extra; sem `barras`. Varredura: zero.

**F1 (T-113 onda 1)**
- json: lista de 7 itens L4-R01 a L4-R07; todos AUTORAL, itemEdital "P1-5.2", aderência "direta", numero 1 a 7, url "saida/gcb/T113_onda1_P1_v2.md" (forma do contrato para AUTORAL de reforço; sai vazia no pacote_estudante), cargo "Lote 4" (campo do contrato, regras/pacote_contrato.md l. 164, não texto). Mesmo conjunto de chaves do L6B-R01 canônico (sem `interno`), nenhuma extra.
- Gabarito 4 C / 3 E (57% de C). Nenhum id colide com os 560 itens da v1.11. Folha P1-5.2: 23 na v1.11 (12 C / 11 E) + 7 = 30 (16 C / 14 E). VOLÁTEIS 0.
- Varredura em textoBase, enunciado e justificativa: zero.

## 3. Pendências decididas (D1 da GCB)

1. **Decreto 1.171/1994 na L4 C16 — basta a conferência da gcb-cqfp.** O texto da pegadinha não traz fato novo: o curso canônico do L4 (bloco P1-6) já cita o Anexo, Capítulo I, Seção I, inciso II, "principalmente entre o honesto e o desonesto", "conferido no Planalto em 08/10/2026"; a gcb-cqfp reabriu a norma no Planalto em 18/10/2026 (HTTP 200) e o texto bate (QA_T110_P1_R1, seção 5). Nenhuma norma da D1 exige o qa-normativo para pegadinha derivada de curso já conferido. A homologação não é pedida; o ponto fecha aqui.
2. **"Abril de 2026" do Data Studio — mantido, sem ação.** A data está no curso canônico do L5 (bloco P1-8.3), com fonte por extenso (Google Cloud Blog, 10/04/2026; notas de versão) e verificação de 08/10/2026; a pegadinha C11 e o resumo do P1-8.3 só a repetem. A página de entrada do Data Studio não traz o mês, mas o curso não se apoia nela (QA_T111_P1_parte2_R1, seção 6, sem reprovação). Cumpre a regra 0.5 (BACKLOG: só o que o curso diz, com a data do curso). Nada de Data Studio Pro, preço ou versão entra. Fica registrado para a conferência de base usual de P1 (T-11); não vira item nem entra na fila de janeiro.
3. **Regra de tamanho GCB × GCE — registrada; a GBQ arbitra se quiser uma só.**
   - GCB (D1, seção 3): 80 a 220 palavras (P1-1 e P1-3 até 300 e 7 parágrafos), ≤ 40% do curso, 3 a 6 parágrafos de até 60 palavras.
   - GCE (saida/gce/V15_BAEF_D1_GCE_2026-10-18.md, 2.1): 120 a 300 palavras, ≤ 50% do curso, 3 a 6 parágrafos de 25 a 80 palavras.
   - Pela regra da GCE, 12 dos 17 resumos de P1 sairiam da faixa: P1-4 (109), P1-8.1 (105) e P1-8.4 (83) abaixo de 120; P1-1 e P1-3 com 7 parágrafos; 10 tópicos com algum parágrafo abaixo de 25 palavras. Os cursos de P1 chegam a 252 palavras (P1-8.4), onde um piso de 120 é quase metade do curso.
   - Posição da GCB: as duas regras são compatíveis com o contrato v1.2.9 (que só exige `\n\n` e um parágrafo por ideia) e podem valer por prova. Se a GBQ fixar uma regra única, a GCB ajusta em v2 (D1, seção 3), o que pede tarefa nova, porque a T-111 de P1 já usou as 2 rodadas; até lá, os 17 resumos aprovados entram como estão.
4. **Auditoria do gbq-estilo — indico o L4-R06**, como pediu a GBQ (D1 da GBQ, 4.3, 8) e recomendou a gcb-cqfp (QA_T113_P1_R2, seção 5): é o item novo mais próximo de uma pegadinha do curso (P2 de 5.2.7). A auditoria é da GBQ e não trava o gatilho A.

## 4. O que vai à GBQ para a v1.12 (D-V112-ESCOPO; D1 da GBQ, 1.2 e 4.4)

| Destino no pacote | Origem (bloco json do arquivo final) | Contagem |
|---|---|---|
| `lotes[].pegadinhas` de L4, L5, L6A, L6B (inserção por `apos`, campos `itemEdital`, `rotulo`, `texto`) | saida/gcb/T110_pegadinhas_P1_v2.md | 49 (L4 11, L5 13, L6A 12, L6B 13), de 46 pares convertidos |
| `registro_alteracoes_v1_12.csv` (rastro dos 72 pares) | saida/gcb/T110_registro_P1_v2.csv | 72 linhas (46 / 26) |
| `topicos[id].resumo` | saida/gcb/T111_resumos_P1_parte1_v2.md (P1-8.2) + saida/gcb/T111_resumos_P1_parte2_v2.md (16) | 17 |
| `topicos["P1-8.2"].emUmMinuto` e `.visuais` (fundir com o resumo do A1) | saida/gcb/T112_piloto_P1-8.2_v2.md | 3 pontos; 2 visuais (tabela, esquema) |
| `itens` (AUTORAL de reforço; registro AUTORAL adendo 4) | saida/gcb/T113_onda1_P1_v2.md | 7 (L4-R01 a L4-R07), P1-5.2 de 23 para 30 |

- `lotes[].pares`, resumos por lote, cursos e itens existentes ficam intactos (D1 da GBQ, 1.2, itens 4 e 5).
- A gbq-csc confere a contagem de P1-5.2 (30) contra o arquivo final (D1 da GBQ, 4.4, 2).
- L4-R08 em diante seguem reservados à T-99.
- Ordem dos gatilhos A em PARA_PRESIDENCIA.md: B, A, E, F1 (D-V15-ENCOMENDA).

## 5. Fora desta reconciliação

Conferência dos Lotes 6a/6b, fila de janeiro (Lote 4 item 15; Lote 5 itens 14–17; Lote 6a 6A-01, 09, 10, 14, 15) e BACKLOG de ferramentas seguem como estão. Nenhum complemento aberto (D-COMPLEMENTOS). DECISOES.md e estados de TAREFAS.md não foram editados.
