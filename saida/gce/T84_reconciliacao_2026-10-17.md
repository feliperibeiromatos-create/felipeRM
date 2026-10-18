# T84_reconciliacao_2026-10-17.md — T-84 — 2026-10-17 — gerado por gce-gerencia

Objeto: reconciliação da errata OPCIONAL de forma da T-84 (D-RT81-03, saida/pacote/T81_reconciliacao_2026-10-17.md, linhas 71–75).
Entradas: saida/gce/T84_errata_proposta_2026-10-17.md (gce-cpp); saida/gce/QA_T84_2026-10-17_gce-cqfp.md (gce-cqfp, APROVADO COM RESSALVAS, 0 de 2 pontos reprovados, 0%; nenhum gate).
Nenhum gabarito, enunciado, item, fonte, [TS], VOLÁTIL ou marca [V] muda.

## D1-T84-01 — Errata 1 (Lote 2): ACEITA, redação final da proposta, APLICADA

- Redação final, sem alteração da proposta: "ver Lote 1-C." → "ver o complemento do Lote 1 (adendo ao 1.4)."
- A1 (localização) acolhido: o trecho fica no curso do 2.4 (Formatação de transcrições parlamentares), no fim do bloco "Ligação com o 1.4", e não no 2.1/2.2 como dizia a proposta. Isso não muda a frase.
- A2 (Tabela de Correções) acolhido pelo precedente D1-T54-b (E-2): entrada T-84 inserida na Tabela de Correções do cabeçalho, logo depois da entrada T-28, no padrão das entradas existentes (5 espaços de recuo nas linhas de continuação).
- Quem aplicou: a gce-gerencia, com texto já aprovado literalmente pela gce-cqfp, que conferiu os destinos nas duas camadas. Na T-54, a aplicação foi da gce-cpp com conferência posterior da gce-cqfp; na T-28, a GCE aplicou a quebra de linha (D1). Aqui é a substituição literal de 1 linha mais o registro, sem conteúdo novo. A conferência de fidelidade depois da aplicação fica com a gbq-cqe, quando a T-12 absorver a errata (leitura própria, rito da v1.8).

Arquivo: saida/gce/GCE_Lote2_v2_CPP.md (CRLF preservado; 970 → 974 linhas terminadas em CRLF)
- Antes: 52 379 bytes, SHA-256 b2e343d6e3bc4a698b029a05f7114fe7a7d902eaeb0bd9487c81c505a5544558
- Depois: 52 692 bytes, SHA-256 29de9ca4796040fa4f0f2063d8c5f3b8a8fff9213145fcb9cadd9e12d84b5da4
- Diff (git diff -U0): exatamente 2 blocos. (i) Inserção de 4 linhas, que viram as linhas 35–38:
```
T-84 → 2.4, "Ligação com o 1.4" (errata de forma, D1 da GCE,
     T84_reconciliacao_2026-10-17.md; D-RT81-03; sem mudança de
     conteúdo, item, gabarito, fonte, troca sutil, volatilidade ou marca
     V): "ver Lote 1-C" → "ver o complemento do Lote 1 (adendo ao 1.4)"
```
  (ii) Troca de 1 linha, a 311 de antes, que vira a 315:
```
- pegadinha do título do edital: ver Lote 1-C.
+ pegadinha do título do edital: ver o complemento do Lote 1 (adendo ao 1.4).
```
  A linha anterior ("a identificação por NOME é cadastro ou atribuição humana. Adendo de") ficou intacta.
- Contagens. "ver Lote 1-C" no curso: 1 → 0. A única ocorrência que sobra no arquivo é a da linha 38 da Tabela de Correções, que é registro de processo. "complemento do Lote 1 (adendo ao 1.4)": 0 → 2 (linha 38 da Tabela e linha 315 do curso).
- O cabeçalho e a Tabela não vão para o pacote. Precedente: a entrada T-54 do Lote 3 traz "que eu possa afirmar", e esse texto aparece 0 vezes em pacote.json, conforme o QA_T84, ponto 2. A ocorrência da linha 38, portanto, não chega à candidata. A GBQ confere isso na T-12.

## D1-T84-02 — Errata 2 (N4 do Lote 3): SEM ERRATA, registrado e fechado

Fica como está a N4 de saida/gce/GCE_Lote3_v2_CPP.md (linhas 75–77). A decisão é coerente com a D1-T54-b: o bloco N1–N6 é registro de processo em primeira pessoa e não é exportado. Na verificação da gce-cqfp, o trecho aparece 0 vezes em pacote.json, em pacote_estudante.json e em saida/estudante/. QA ponto 2 APROVADO.

## D1-T84-03 — Absorção e observação A3 para a próxima T-12

- Não editados: saida/estudante/ e saida/pacote/. A errata entra na próxima ocorrência da T-12, sem abrir versão própria ("itens só de forma não abrem versão"). Efeito esperado: saida/estudante/L2_estudo.md:237, pacote.json e pacote_estudante.json passam de "ver Lote 1-C." (1 ocorrência em cada) para "ver o complemento do Lote 1 (adendo ao 1.4).", e nada mais muda no L2.
- Observação A3 para a GBQ: gerador_v1_8/conferencias_v18.py:385 exige que os arquivos L2_* sejam idênticos byte a byte aos da v1.7. Essa conferência falha por construção quando a errata for absorvida, e precisa ser atualizada no gerador da versão que absorver a errata: a única diferença admitida no L2 é a desta troca. Isso não bloqueia a errata.
- Também para a T-12: o QA confirmou que o gerador não depende do texto "Lote 1-C" do curso do L2. As ocorrências de p2.py:92–93 ficam nos campos do L1C, e marcas_processo.py não corta "complemento" nem "adendo".
- Nenhuma tarefa nova foi aberta: a observação segue com o gatilho A desta errata, para anexar à T-12.

## Saída
- Canônico alterado: saida/gce/GCE_Lote2_v2_CPP.md (1 linha trocada e 4 inseridas).
- Gatilho A em PARA_PRESIDENCIA.md (s11c3): errata de forma aprovada e reconciliada, para aceite, conforme o roteiro da T-84 ("gce-gerencia (gatilho A da errata)").
