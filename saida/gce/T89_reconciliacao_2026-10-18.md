# T89_reconciliacao_2026-10-18.md — T-89 — 2026-10-18 — gerado por gce-gerencia

Objeto: reconciliação da T-89 (REFORÇO onda 1 — R1, Lote 1; D-REFORCO-1 e D-REFORCO-2), ciclo s12c1.
Entradas: saida/gce/L1_reforco_onda1_v1.md; saida/gce/L1_reforco_onda1_v2.md (gce-cpp); saida/gce/QA_T89_R1_2026-10-18_gce-cqfp.md (0/18 reprovados; 4 ajustes); saida/gce/QA_T89_R2_2026-10-18_gce-cqfp.md (0/18 reprovados; 0 ajustes pendentes; ressalva de registro do mapa em R10 e R16). Referência de critério da outra Gerência: saida/gcb/T92_D1_2026-10-18.md (seção 2: excesso legado registrado e diluído; item novo só em formato livre).
Não existe saida/gce/T91_reconciliacao_2026-10-18.md neste ciclo: os critérios fixados aqui (seções 1 e 3) passam a valer para a T-90 e a T-91 (D1 da gce-gerencia), para manter coerência.
Esta Gerência reconcilia e decide D1; não reescreve item, não muda gabarito, não produz texto pedagógico.

## 1. D1 — critério de VOLÁTIL para itens que nomeiam produto (R03, R04, R11, R16, R17, R18)

Decisão: os seis ficam NÃO VOLÁTEIS. Critério fixado (vale para as ondas seguintes de P2 — R2, R3, onda 2 em diante):
- VOLÁTIL = item cujo gabarito depende de fato que pode mudar até a reverificação de 4–8/1/2027: versão, limite, preço, disponibilidade, modelo padrão/"mais recente", nome ou existência de recurso de serviço gerenciado (precedentes: L1-Q14, Q16, Q18, Q19).
- NÃO VOLÁTIL = item que só nomeia produto e afirma propriedade fixa de artefato já publicado (arquitetura e formato de treino dos pesos publicados, janela de entrada da arquitetura, contagem de parâmetros de checkpoint publicado) ou a divisão estrutural de operações de um serviço (lote × streaming), desde que o gabarito não dependa do modelo padrão nem de versão.
- Condições: (a) base do fornecedor com URL efetivamente aberta e "verificado em [data]" (cumprido: README em raw.githubusercontent.com/openai/whisper/main, repositório oficial; AWS Transcribe); (b) se a redação ficar dependente de modelo/versão, o item é VOLÁTIL e entra no teto — por isso R16 só é não VOLÁTIL com o ajuste do R1 (modelos multilíngues treinados para tradução; turbo excluído), aplicado no v2; (c) R11 não nomeia produto no enunciado.
- Salvaguarda sem efeito de VOLÁTIL: R03, R04, R16, R17 e R18 entram na lista de conferência de base da reverificação de 4–8/1/2027 (reabrir URL e conferir o trecho); não ficam inaptos a simulado final. Se a base mudar, o caso volta à Gerência como errata ou D2.
- Teto: VOLÁTEIS do Lote 1 = 4 (Q14, Q16, Q18, Q19), 1 de risco alto (Q16); novos 0. Teto de 4 por lote e 1 de risco alto cumprido, sem folga. Com o critério literal ("nomeia produto = VOLÁTIL"), o lote iria a 9 e exigiria substituição de 5 itens — rejeitado por tornar o teto de 20% por folha (D-REFORCO-2, regra 4) incumprível na folha 1.8 ("Ferramentas e APIs").

## 2. D1 — proximidades e classificação de R09

- R12 × L1C-Q21: ACEITO. Folhas diferentes (1.6 × 1.1); ponto próprio (escolha entre homófonas pt-BR por contexto, modelo de linguagem); regra (1) da D-REFORCO-2 cumprida. Registrado como reforço do par em outra folha.
- R15 × Q17 (folha 1.7): ACEITO. Pontos distintos (comparação de modos lote × streaming quanto à acurácia × efeito do parâmetro de endpointing); não é duplicata. Proximidade registrada.
- R13 × R14 (1.7) e R01 × R11 (1.1 × 1.6): sem duplicata; registrados.
- R09: formato registrado como TROCA DE SUJEITO (inversão de papéis lexical × exibição), coerente com a classificação de L1C-Q21. Folha 1.5 fica PC 2/6 (legado), TS 1/6; não reclassificar.

## 3. D1 — [TS] e excessos legados

- [TS] 7/18 (39%; R01, R03, R07, R09, R12, R13, R17; 1 com gabarito C: R07, falsa pegadinha). ACEITO nesta onda: a D-REFORCO-1 não fixa número de [TS] e veda relação fixa entre [TS] e gabarito; o PADRÃO §1(d) ("metade") fica como meta acumulada. Instrução para a onda 2 (folhas 1.1–1.8): [TS] em pelo menos metade dos itens da onda mais 2, para o acumulado de reforço do Lote 1 chegar a ≥ 50%.
- Formato (teto 30%), excesso LEGADO, não imputado à onda 1 (nenhum item existente muda): 1.2 D 2/6 (Q03, L1C-Q24); 1.4 D 2/6 (Q09, L1C-Q27) e PC 2/6 (Q08, L1C-Q28); 1.5 PC 2/6 (Q11, L1C-Q30); 1.6 PC 2/6 (Q13, Q14). Nenhum item novo acrescentou formato saturado. Regra de diluição (coerente com a GCB, T92_D1 2.4): até a folha voltar a ≤ 30%, nenhum item de reforço usa "definição" em 1.2 e 1.4 nem "par confundível" em 1.4, 1.5 e 1.6.
- VOLÁTIL LEGADO em 1.8: 2/6 = 33,3% (Q18, Q19), reduzido pela onda de 2/3. Até a folha voltar a ≤ 20%, nenhum VOLÁTIL novo em 1.8 (com 10 itens, 2/10 = 20%). 1.6 e 1.7: 1/6 = 16,7% (cumprido).

## 4. Tabela de Correções — registro do "ponto de julgamento" (mapa interno, Parte 1 do v2)

O mapa é documento interno; a correção vale por este registro, que prevalece sobre a coluna do v2 na consolidação (T-94). Itens, gabaritos e (d)/(d-G) não mudam.

| id | folha | ponto registrado no v2 (desatualizado) | ponto de julgamento VIGENTE |
|---|---|---|---|
| L1-R10 | P2-1.6 | O vocabulário personalizado deve conter termos de reconhecimento, não informação pessoal ou confidencial | O vocabulário personalizado deve conter termos úteis ao reconhecimento, inclusive nomes próprios de parlamentares, e excluir informações confidenciais e dados pessoais que nada acrescentam ao reconhecimento (números de documentos, informações de saúde) |
| L1-R16 | P2-1.8 | A tarefa de tradução do Whisper converte fala em outro idioma em texto em inglês | A tarefa de tradução dos modelos multilíngues do Whisper treinados para essa tarefa converte fala em outro idioma em texto em inglês (o modelo turbo não é treinado para tradução) |

Conferência de duplicata com o ponto vigente: R10 × Q12, Q13, Q14, R11, R12 — distintos; R16 × Q18, Q19, Q20, R17, R18 — distintos.

## 5. D1 — versão final

- saida/gce/L1_reforco_onda1_v2.md é a VERSÃO FINAL da T-89 (sha256 75e4a5350016482d37f157796a536579614a043e899e3c1239e3262cb0725e05), com a correção de registro da seção 4. Sem v3.
- QA concluído em 2 rodadas (máximo da D-REFORCO-1); 0/18 reprovados (0%); gate de 30% não acionado. O "QA PENDENTE" do v2 cai com esta reconciliação.
- Sem PENDENTE NORMATIVO (nenhuma norma citada). Rótulo AUTORAL em todos. Estrutura PARTE 1/3–3/3, Parte 2 sem gabarito e sem [TS] (conferido pela gce-cqfp e por esta Gerência).

## 6. Contagens

| folha | partida v1.8 | novos | nova | ids novos (gab.) | [TS] novos | VOLÁTEIS na folha |
|---|---|---|---|---|---|---|
| P2-1.1 | 4 | +2 | 6 | R01 E, R02 C | 1 (R01) | 0/6 |
| P2-1.2 | 4 | +2 | 6 | R03 E, R04 C | 1 (R03) | 0/6 |
| P2-1.3 | 4 | +2 | 6 | R05 C, R06 E | 0 | 0/6 |
| P2-1.4 | 5 | +1 | 6 | R07 C | 1 (R07) | 0/6 |
| P2-1.5 | 4 | +2 | 6 | R08 C, R09 E | 1 (R09) | 0/6 |
| P2-1.6 | 3 | +3 | 6 | R10 C, R11 E, R12 E | 1 (R12) | 1/6 (Q14) |
| P2-1.7 | 3 | +3 | 6 | R13 E, R14 C, R15 E | 1 (R13) | 1/6 (Q16, risco alto) |
| P2-1.8 | 3 | +3 | 6 | R16 C, R17 E, R18 C | 1 (R17) | 2/6 (Q18, Q19; legado) |
| total | 30 | +18 | 48 | 9 C / 9 E (50% C; faixa 7–11 cumprida) | 7/18 | 4 no lote (0 novos), 1 risco alto |

Pacote: 286 (v1.8) → 304 com a T-89, na consolidação v1.9 (T-94), após aceite.

## 7. Estado da T-89 (texto para TAREFAS.md)

CONCLUÍDA (18/10/2026, s12c1): 18/18 itens L1-R01 a L1-R18 aprovados em 2 rodadas (0% de reprovação); final saida/gce/L1_reforco_onda1_v2.md (sem v3), com correção de registro do ponto de julgamento de R10 e R16 em saida/gce/T89_reconciliacao_2026-10-18.md; P2-1.1 a 1.8 de 4, 4, 4, 5, 4, 3, 3, 3 para 6 cada (30 → 48); 9 C / 9 E; [TS] 7/18; 0 VOLÁTIL novo (lote 4, 1 risco alto); critério de VOLÁTIL fixado (propriedade fixa de artefato publicado ou estrutura de serviço = não VOLÁTIL); excessos legados de formato (1.2, 1.4, 1.5, 1.6) e VOLÁTIL legado (1.8) registrados para diluição na onda 2; gatilho A emitido.

## 8. Gatilho A (texto para PARA_PRESIDENCIA.md)

GATILHO A | GCE | T-89 — REFORÇO onda 1, R1, Lote 1 (D-REFORCO-1/2): 18 itens AUTORAL L1-R01 a L1-R18, reconciliados | saida/gce/L1_reforco_onda1_v2.md (final; sha256 75e4a535…0725e05); saida/gce/QA_T89_R1_2026-10-18_gce-cqfp.md; saida/gce/QA_T89_R2_2026-10-18_gce-cqfp.md; saida/gce/T89_reconciliacao_2026-10-18.md | por folha (partida v1.8 → nova): 1.1 4→6, 1.2 4→6, 1.3 4→6, 1.4 5→6, 1.5 4→6, 1.6 3→6, 1.7 3→6, 1.8 3→6 (30→48); 9 C / 9 E; [TS] 7/18 (1 C); VOLÁTEIS novos 0, lote 4 com 1 de risco alto (no teto); reprovação QA 0/18 em 2 rodadas; legado registrado: formato 33,3% em 1.2, 1.4, 1.5, 1.6 e VOLÁTIL 2/6 em 1.8; D1 registrado: R03, R04, R11, R16, R17, R18 não VOLÁTEIS (propriedade fixa de artefato publicado/estrutura de serviço), com conferência de base em 4–8/1/2027 | A Presidência aceita os 18 itens da T-89 para consolidação no pacote v1.9 (T-94), com o critério de VOLÁTIL fixado na seção 1 da reconciliação? (SIM/NÃO)
