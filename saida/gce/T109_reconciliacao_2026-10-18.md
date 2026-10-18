# T109_reconciliacao_2026-10-18.md — T-109 — 2026-10-18 — gerado por gce-gerencia

Ciclo 2026-10-18 s14c1. ORDEM_V15_D (ordens/ORDEM_V15_D_L2R16.md; D-V15-ENCOMENDA). Entradas: saida/gce/T109_D1_2026-10-18.md (D1) e saida/gce/QA_T109_R1_2026-10-18_gce-cqfp.md (R1, APROVADO; 0/1 reprovado; gate de 30% não acionado; não houve R2). A fonte canônica e o pacote não foram alterados. A aplicação depende do aceite do gatilho D (PARA_PRESIDENCIA.md, ciclo s14c1).

## 1. Reconciliação

- Resposta do QA: 3.1. Fundamento: o 2.8 fica no tópico de degravação, e o parêntese "(language model adaptation)" fixa o sentido de vocabulário adaptado ao modelo de fala. O item julga o instrumento da indexação temática de um acervo parlamentar, e "indexação" é termo literal do 3.1. O elo com o 2.8 é só lexical ("vocabulário"). A busca semântica (3.2) foi considerada e descartada.
- Aderência: continua DIRETA em P2-3.1 (regras/pacote_contrato.md, regra 3 da errata de aderência). A ressalva de registro, de que o item não menciona IA, fica anotada sem efeito no campo. A D-ADERENCIA não se aplica.
- Não repetição na 3.1: o QA não achou "TECAD", "tesauro" nem "vocabulário controlado" nos itens da onda 4 (L3_reforco_onda4_A_v3, B_v2, C_v3), nem nos 6 itens da 3.1 do v1.10. Nenhum par a registrar.
- ACATADO sem divergência CPP × CQFP (não houve produção nesta ordem).

## 2. Registro de alteração por id (para a GBQ aplicar no pacote novo, junto com a T-108)

| Id | Campo | De | Para | Inalterados | Ato |
|---|---|---|---|---|---|
| L2-R16 | itemEdital | P2-2.8 | P2-3.1 | enunciado, gabarito (E), justificativa, [TS], base, VOLÁTIL (n), aderência (direta), comando, textoBase, url | ORDEM_V15_D; QA_T109_R1 (APROVADO); esta reconciliação; aceite do gatilho D (s14c1) |

Via: o registro por id prevalece sobre a coluna da folha no mapa de saida/gce/L2_reforco_onda1_v3.md (linha 70), como na correção de registro de L1-R10/L1-R16 (T-89, lida em reforco.py). O arquivo do lote não é reescrito. O gerador lê este registro e o adendo de registro AUTORAL do pacote novo o transcreve.

## 3. Arquivos derivados a regenerar (GBQ; nunca edição manual)

1. saida/pacote/pacote.json e pacote_estudante.json (itemEdital do L2-R16; nucleo recalculado nas folhas 2.8 e 3.1).
2. Adendo novo do registro AUTORAL (o adendo1, linha 96, e saida/pacote/gerador_v1_9/out/registro_adendo1.md ficam como histórico).
3. saida/estudante/L2_gabarito.md (bloco L2-R16, "Item do edital") e saida/estudante/NUCLEO.md (listas P2-2.8 e P2-3.1), mais as cópias em out/estudante do gerador.
4. Conferências do gerador que fixam contagens do L2 ou por folha (reforco*.py, validate*.py, conferencias*.py).
5. Cobertura da T-95 (secretaria) sobre o pacote novo.
Sem regeneração: simulados. O R16 não está em SIM-0, SIM-1, SIM-2 nem SIM-0-P2. O diagnóstico da plataforma fica fora do repositório: confere a GBQ, e o L2-R17 continua em 2.8.

## 4. Efeito nas contagens

| Folha | Base | Total | Diretos | VOLÁTEIS | Meta 20 | Piso 10 diretos |
|---|---|---|---|---|---|---|
| P2-2.8 | v1.10 hoje | 20 | 19 | 4 (R18, R120, R121, R125) = 20,0% | sim | sim |
| P2-2.8 | depois | 19 | 18 | 4/19 = 21,1% | não (falta 1) | sim |
| P2-3.1 | v1.11 com a onda 4 (D-T98-ONDA4-ACEITE; T98_reconciliacao 1.6) | 20 | 15 | 4/20 = 20,0% | sim | sim |
| P2-3.1 | v1.11 + R16 | 21 | 16 | 4/21 = 19,0% | sim | sim |

- Núcleo: na 2.8, o R16 sai e entra o seguinte pela chave do nucleo.py. Na 3.1, o R16 concorre às 10 vagas com a onda 4. O gerador define as duas listas.
- [TS]: o mínimo de 9/14 da 3.1 é da onda 4 e não muda. O R16 acrescenta 1 [TS] à folha.
- Total de P2, C/E global e simulados: inalterados. Na métrica da D-V15-NOTA-DISTINTAS, o tópico 2 perde 1 e o tópico 3 ganha 1.
- Consequência na 2.8 (registro D1 da GCE): a folha fica com 19 itens, 1 a menos que a meta, e com 4 VOLÁTEIS em 19 (21,1%), acima do teto de 20% por folha (regra 4 da D-REFORCO-2). Saneamento: 1 item novo NÃO VOLÁTIL e direto na 2.8, na T-113 (ORDEM_V15_F), com prioridade sobre as demais folhas, o que devolve a folha a 20 itens e 4/20 = 20,0%. Até lá, nenhum outro item da 2.8 pode ganhar marca VOLÁTIL sem saldo. A abertura dessa linha é feita no ciclo seguinte pelo canal da fila, porque esta reconciliação não toca TAREFAS.md.

## 5. Encaminhamento

Gatilho D em PARA_PRESIDENCIA.md (mapeamento de item canônico ao edital). Com o aceite, a GBQ aplica a seção 2 no pacote novo da T-108. Se a Presidência recusar, o R16 fica em P2-2.8, e o motivo vai para este arquivo (ordem, alínea e).
