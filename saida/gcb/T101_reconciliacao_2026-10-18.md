# T101_reconciliacao_2026-10-18.md — T-101 — 2026-10-18 — gerado por gcb-gerencia

Objeto: reconciliação do Lote D6 v2 (LAI e LGPD; P1-DA, itens 11–12). Ciclo 2026-10-18 s12c3. Rito pela D-CEGO-2 e pela D-D6-VEREDITO: o QA comparativo cego do Fundador fez o papel da R1; depois vieram a v2 com resposta item a item, o R2 da gcb-cqfp e esta reconciliação, que leva ao gatilho A. Precedentes: T72_reconciliacao_2026-10-17.md (2.1) e T73_reconciliacao_2026-10-17.md (seção 3; D-LOTED1-CANONICO).

## 1. Conferência própria (script da GCB, python -I, somente leitura)
| Arquivo | SHA-256 | Agente |
|---|---|---|
| saida/gcb/D6_parecer_QA_comparativo.md | 0c5a59e2b7915ae30cb7e89e061b4bd95cfc87f75a56927f2899e4c75402aa71 | Fundador (fora da fábrica) |
| saida/gcb/D6_anexo_N_mapa_normativo.md (com a errata T-82) | 57e8c64d4f27fe2c7549ff9f9b16c16848a51558e9aa181a0ed48c2f85d3e80e | qa-normativo-da |
| saida/gcb/D6_v2.md (objeto do R2) | 1b0f0b425ea38485d3c58f172c2cb4083b1193aea5a4f10a26d4092569c64fbe (957 linhas de texto, LF, sem CR) | gcb-cpp (sonnet) |
| saida/gcb/D6_parecer_R2_gcb-cqfp.md | 5107fac758aa657c844399d794d5bd1dbca7d24dbb27c29b1043d1fe481437d2 | gcb-cqfp (opus) |

Os hashes da v2 e do Anexo N batem com os que o R2 declara.

Contagens tiradas do gabarito comentado (5.2) por parser próprio:
| Lei | Itens | C | E | [TS] | REVERIFICAR | VOLÁTIL | QA PENDENTE |
|---|---|---|---|---|---|---|---|
| LAI (D6-01 a D6-30) | 30 | 15 | 15 | 15 | 1 (D6-09) | 0 | 30 |
| LGPD (D6-31 a D6-50) | 20 | 10 | 10 | 10 | 2 (D6-32, D6-34) | 0 | 20 |
| Total | 50 | 25 | 25 | 25 | 3 | 0 | 50 |
- Os ids vão de D6-01 a D6-50, contínuos. A versão do estudante tem 50 itens. A última linha é "FIM DO LOTE D6". Tudo isso bate com a seção 7 da v2 e com a seção 4 do R2.
- Busca de origem no arquivo inteiro: nenhuma ocorrência de fornecedor, modelo, agente, unidade, "fábrica", "Fundador" ou utm. A única ocorrência de "externa" é "ameaça externa à soberania" (L19, art. 35), que é texto de lei.
- Reprovação no R2: 0/50 (0%). O gate não foi acionado. Os 14 blocos importados foram aprovados, 2 deles com ajuste de forma. A D-D6-VEREDITO foi cumprida em 9/9 pontos e a D-CABECALHO-NEUTRO também.
- Separação entre produção e QA: a produção foi da gcb-cpp (sonnet); o R2, da gcb-cqfp (opus); o normativo, do qa-normativo-da; a R1 foi o QA comparativo do Fundador, feito fora da fábrica.

## 2. D1 (1): ajustes A-1 a A-3 e a versão final
A errata é de forma e foi pedida pela própria QA, com o texto fixado (R2, seção 8). Precedente: D-LOTED1-CANONICO. Ela não toca item, gabarito, [TS] nem contagem. A gcb-cpp a transcreve num arquivo novo, **saida/gcb/D6_v2_1.md**, sem alterar a D6_v2.md, que fica como objeto do R2. Cada trecho "Onde está" ocorre uma única vez na v2 (conferido por script). Mudam só estas 4 linhas:

| Linha (v2 e v2.1) | Seção | Onde está | Leia-se |
|---|---|---|---|
| 1 | cabeçalho neutro | `LOTE D6 — LAI e LGPD — v2 — 18/10/2026` | `LOTE D6 — LAI e LGPD — v2.1 — 18/10/2026` |
| 130 | 0.7 (A-3) | `G7 (§ 5º do art. 8º) e G23 (arts. 60 a 63), com marca no corpo; G22 (art. 55-D, § 4º).` | `G7 (§ 5º do art. 8º) e G23 (arts. 60 a 65), com marca no corpo; G22 (art. 55-D, § 4º: acréscimo conferido no Anexo N, âncora da pegadinha importada 61).` |
| 259 | L24 (A-1) | `nenhum servidor poderá ser responsabilizado civil, penal ou administrativamente por dar ciência à autoridade superior ou a outra autoridade competente de informação concernente à prática de crimes ou improbidade de que tenha conhecimento` | `nenhum servidor poderá ser responsabilizado civil, penal ou administrativamente por dar ciência à autoridade superior ou, quando houver suspeita de envolvimento desta, a outra autoridade competente para apuração de informação concernente à prática de crimes ou improbidade de que tenha conhecimento` |
| 530 | 4, pegadinha 55 (A-2) | `— art. 11, § 4º (vedação com as exceções dos incisos I e II e das hipóteses de serviços de saúde, assistência farmacêutica e assistência à saúde, observado o § 5º).` | `— art. 11, § 4º (a vedação admite exceção nas hipóteses relativas a prestação de serviços de saúde, de assistência farmacêutica e de assistência à saúde, observado o § 5º, para permitir a portabilidade solicitada pelo titular (I) ou as transações financeiras e administrativas resultantes desses serviços (II)).` |

- Nas linhas 130, 259 e 530 troca-se só o trecho indicado; o resto da linha, inclusive as marcas "[QA PENDENTE — …]", fica como está. A mudança da linha 1 (v2 → v2.1) é decisão desta Gerência, para que o cabeçalho corresponda à versão; ele continua neutro (D-CABECALHO-NEUTRO).
- Conferência pelo orquestrador: diff entre D6_v2.md e D6_v2_1.md igual a exatamente as linhas 1, 130, 259 e 530, com os textos da tabela. A GCB simulou a transcrição na scratchpad e obteve o SHA-256 esperado da D6_v2_1.md: **a983105818ad84e96a57a4f70ff19baa12224e11e939d023c6f7a29ca5414090** (178.040 bytes, LF, sem CR, mesmo número de linhas da v2). Da linha 544 ("## 5.1 Versão do estudante") até o fim, o texto fica idêntico ao da v2.
- Se o diff e o hash forem idênticos, não há nova rodada de QA e vale o R2. Se divergirem, a gcb-cpp refaz a transcrição e o gatilho A não é emitido. A gcb-cpp não faz nenhuma outra mudança: nem marca, nem numeração, nem seção 0.

## 3. D1 (2): exceção do cabeçalho neutro
- Para os arquivos de versão do D6 (D6_v2.md, D6_v2_1.md e qualquer versão comparável ou destinada a produtor externo, inclusive D<n>_para_leitura_critica.md), a D-CABECALHO-NEUTRO (18/10/2026), posterior e específica, **prevalece sobre a linha de controle do CLAUDE.md** ("Formato de arquivos gravados"). A linha 1 é o cabeçalho neutro e não traz agente, modelo nem serviço.
- A rastreabilidade que a linha de controle daria fica nesta reconciliação (tabela da seção 1 e esta seção), no R2 e em DECISOES.md. A D6_v2_1.md é da gcb-cpp (sonnet), com errata de forma pedida pela gcb-cqfp e fixada pela gcb-gerencia.
- Diferença em relação à T-72 (2.1): na v1, a linha de controle ficou no repositório e o entregável começava na linha 2. Na v2/v2.1, não há linha de controle a retirar. Os demais arquivos da fábrica (pareceres, reconciliações e Anexo N) mantêm a linha de controle. Isto não é precedente para outros arquivos.
- Entrega para fora da fábrica (observação (b) do R2): nenhuma está ordenada agora. Se o Fundador ou a Presidência pedirem, o entregável é a linha 1 mais o trecho que vai de "# 1. (a) CURSO — dispositivo a dispositivo" (linha 136) até "FIM DO LOTE D6", com a seção 0 (linhas 2 a 135) omitida. A gcb-cqfp confere o cabeçalho e o trecho antes de a cópia sair (D-CABECALHO-NEUTRO).

## 4. D1 (3): retirada da marca "QA PENDENTE"
- O R2 aprovou o lote, mas a marca **não sai agora** nem sai no arquivo canônico (D-QA-PENDENTE; precedente D-LOTED1-CANONICO). A D6_v2_1.md fica, como arquivo de trabalho, com as 50 marcas de item e as marcas dos trechos importados: curso L20 a L24, G7 § 5º, G22 § 4º e G23; pares L-P13 a L-P16, G-P16 a G-P20 e I-P7; pegadinhas 21 a 32 e 55 a 63; e "QA PENDENTE (enunciado importado)" no D6-19.
- Momento: só depois do aceite da Presidência no gatilho A da seção 6, numa ocorrência futura da T-12 (exportação no módulo m-da).
- Quem: a GBQ retira as marcas no pacote e na edição do estudante (gbq-cfp transcreve, gbq-cqe confere a fidelidade e a gbq-gerencia reconcilia e emite o gatilho A do pacote). A GCB não reedita o canônico. A legenda e a observação (v) da seção 0.7, que só valem no arquivo de trabalho, não vão ao pacote. Se o aceite não vier, as marcas ficam.

## 5. Dois registros (sem tarefa nova; D-COMPLEMENTOS)
- D6-39 (R2, obs. 1): enumeração parcial do art. 41, § 2º. É aprovado, mas a GBQ não deve pô-lo no mesmo simulado de item que cubra os incisos III e IV.
- Não acatamentos R-3 (tabela de prazos) e R-7 (banco de reserva de B): a gcb-cqfp os aceitou e a GCB confirma. Os itens de B não usados não viram ativo.

## 6. D1 (4): estado da T-101 e gatilho A
- Estado provisório (agora): EM CURSO. A reconciliação está feita, e falta a gcb-cpp transcrever a D6_v2_1.md e o orquestrador conferir o diff e o hash da seção 2.
- Com o diff e o hash conferidos: o lote fica **RECONCILIADO e PRONTO para o gatilho A**, e o gatilho abaixo vai a PARA_PRESIDENCIA.md.
- Estado final: CONCLUÍDA, registrada pelo orquestrador depois do aceite da Presidência (esta Gerência não altera a linha da T-101). Se o gatilho for devolvido, a T-101 volta a EM CURSO com o motivo.

Texto do gatilho (emitir só se o diff conferir):
GATILHO A | GCB | Lote D6 v2.1 — LAI e LGPD (P1-DA itens 11–12; D-CEGO-2; D-D6-VEREDITO), QA comparativo cego do Fundador (R1) → v2 → R2 gcb-cqfp APROVADO 50/50, 0% → errata de forma A-1 a A-3 fixada pela QA | saida/gcb/D6_v2_1.md (SHA-256 a983105818ad84e96a57a4f70ff19baa12224e11e939d023c6f7a29ca5414090); D6_v2.md (1b0f0b42…4fbe); D6_parecer_R2_gcb-cqfp.md (5107fac7…37d2); D6_parecer_QA_comparativo.md (0c5a59e2…aa71); D6_anexo_N_mapa_normativo.md (57e8c64d…80e); T101_reconciliacao_2026-10-18.md | 50 itens (D6-01 a D6-50); LAI 30 (15 C/15 E; 15 [TS]); LGPD 20 (10 C/10 E; 10 [TS]); [TS] 25; REVERIFICAR 3 (D6-09, D6-32, D6-34); VOLÁTIL 0; Interface 3; pares 16/20/7; pegadinhas 63; reprovação R2 0/50; diff v2 → v2.1 só nas linhas 1, 130, 259 e 530 | Aceita como canônico o Lote D6 v2.1 (saida/gcb/D6_v2_1.md, SHA-256 a983…4090), incluindo "D6 (v2.1)" na D-CANONICOS, com os 3 REVERIFICAR na T-11 e sem liberação à plataforma nem à candidata? SIM / NÃO

Para a T-11 (acréscimo pedido ao orquestrador, parte DA): reverificação, em 4–8/1/2027, dos 3 REVERIFICAR do D6 (D6-09, LAI art. 8º-A, I, Lei 15.141/2025; D6-32, LGPD art. 5º, VIII, e D6-34, LGPD art. 55-A, Lei 15.352/2026) e dos trechos REVERIFICAR do curso e dos pares (L7, arts. 8º-A e 8º-B; G4, art. 5º, VIII e XIX; G17 e G22, arts. 55-A e 55-C, V-A, V-B e VI; pares L-P11 e G-P16). A reverificação reabre o compilado do planalto.gov.br com "verificado em [data]". Responsáveis: qa-normativo-da → gcb-gerencia. Até ela, os 3 itens não entram em simulado final; nenhum é VOLÁTIL.

Lembretes à GBQ, para depois do aceite:
- A exportação futura é no módulo m-da, por ocorrência da T-12, com gatilho A da GBQ. A retirada das marcas segue a seção 4.
- Não pôr o D6-39 com item sobre o art. 41, § 2º, III e IV.
- Nada vai à plataforma nem à candidata (PILOT_01) sem o sim do Fundador.

FIM DA RECONCILIAÇÃO T-101

## Conferência da v2.1 (orquestrador, 18/10/2026)
SHA-256 de saida/gcb/D6_v2_1.md = a983105818ad84e96a57a4f70ff19baa12224e11e939d023c6f7a29ca5414090 (igual ao esperado); diff v2 → v2.1 só nas linhas 1, 130, 259 e 530. Sem nova rodada; gatilho A da seção 6 colado em PARA_PRESIDENCIA.md.
