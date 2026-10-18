# T94_reconciliacao_2026-10-18.md — T-94 — 2026-10-18 — gerado por gbq-gerencia

REMETENTE: gbq-gerencia (reconciliação da fidelidade da v1.9; ciclo 2026-10-18 s12c2).
DESTINATÁRIO: orquestrador (texto da linha T-94 e dos gatilhos, que ele grava); Presidência de Ciclo (gatilhos A e D). Sem commit nem push (do orquestrador). Nada vai à plataforma nem à candidata.
Base: `saida/pacote/fidelidade_v1_9_gbq-cqe.md` (ACEITO COM RESSALVAS; 0% de reprovação; A-1 a A-7); `saida/pacote/T94_D1_v1_9_2026-10-18.md`; `saida/pacote/pacote_relatorio_2026-10-18_v1_9.md`; linha T-94 de TAREFAS.md; D-REFORCO-1; D-REFORCO-2; D-ONDA1-FILA; D-PACOTE-V18; D-TRANSPORTE-L5C-T83; D-L2-T84-ERRATA; agente presidencia (critérios A e D).

## 1. Achados da fidelidade

| # | Decisão | Feito |
|---|---|---|
| A-1 (23 folhas, não 25) | ACOLHIDO e corrigido agora | D1 (seções 2 e 7.4) e relatório (seção 3 e passo 4) corrigidos: "23 folhas com item novo, com 6 cada; a onda 1 tem 24; a P1-4.3 fica com 4 até a T-102". Rótulo de `validate_v19.py:119` corrigido sem mudar a verificação nem a lista `FOLHAS` (23 entradas). Pipeline `sh rodar_tudo.sh` rodado de novo: código 0, validate_v19 47/47, conferencias_v19 23/23, validar_erros_teste 12/12. SHA de `pacote.json` (`1366055496457792bf55f541d901e2d1f277ee42611060b03bbf82b4427610bb`), `pacote_estudante.json` (`8fa81b45a92095f8973c2787083d144869fdc195031455f7ff75ecb337e509e2`) e adendo 1 (`801a0724…`) **sem mudança**. MANIFESTO atualizado só em 3 linhas: `validate_v19.py` `49e0721d…` (14477 B) → `5e3581239299b9c90faf991733599b4e93adac1e1a5e739816ab97282ed7ae9d` (14513 B); `out/validate_stdout.txt` → `5e380e71…` (4116 B); `out/validate_v19.json` → `4b32afd3…` (6320 B). Novo SHA do `MANIFESTO.md`: `8d9034c7c5bb8751d16dc9eb399c45634f1b463476e60ea802268d025bb5b564`. O registro adendo 1 já dizia 23 e não muda. A conferência de MANIFESTO da fidelidade (46 SHA) fica superada só nessas 3 linhas, todas de texto de rótulo. |
| A-2 (texto do gatilho E) | ACOLHIDO e corrigido agora | D1, seção 5, reescrita: 47 dos 48 (L1-R, L2-R, L3-R) já entram nos testes de lote da plataforma v1.7 (`startsWith` sobre "L1-", "L2-", "L3-", "6A-"; `plataforma_v1_7.html`, linhas 183 a 187 e 258). Só o L6A-R01 depende de adaptação (prefixo "L6A-"). Os 6 parciais aparecem no teste de lote, que não é simulado (compatível com a D-ADERENCIA). O gatilho E abaixo usa este texto. |
| A-3 (adiamento do 5C-08 e do curso do L2) | ARBITRADO: **não é D1 da GBQ; vai à Presidência (gatilho D)** | Ver seção 2. |
| A-4 (edição .md do estudante) | ARBITRADO: **D1 da GBQ, leitura 1** (D-RT94-02) | Ver seção 3. |
| A-5 | Registro | Nenhuma ação (segue o contrato e o precedente da v1.8; o estudante já remove o texto). |
| A-6 | Registro | Minúscula inicial do L6A-R01 é literal da origem. Errata de forma opcional à GCB na próxima ocorrência; o pacote não muda. |
| A-7 | Registro | Precisar a redação do ponto 2 do contrato numa errata futura ("rotulado, no L3 e no L6A; após o cabeçalho, no L1 e no L2"). A v1.2.6 não reabre. |

## 2. A-3 — D-RT94-01 (arbitragem: matéria da Presidência)

- **Letra das decisões vigentes.** D-TRANSPORTE-L5C-T83: derivados (pacote.json, pacote_estudante.json) "absorvem na próxima ocorrência da T-12". D-L2-T84-ERRATA: "absorção na próxima ocorrência da T-12". A linha T-94 se diz, literalmente, "Pacote v1.9 — ocorrência da T-12". Logo, pela letra, esta ocorrência é a fixada pelas duas decisões.
- **Letra contrária.** D-REFORCO-1 (Fundador, 18/10, posterior): "Nenhum item existente muda"; T-94: "sem mudar item existente". Isso cobre o (b) 5C-08, que é item existente. **Não cobre o (c)** `lotes[L2].curso`, que é campo de lote.
- **Arbitragem.** O adiamento das D-V19-03 (b) e (c) contraria a letra de duas decisões vigentes da Presidência. A GBQ não pode afastá-las por D1. No (b) há conflito de letras entre decisão do Fundador (posterior) e decisão da Presidência; no (c) não há cobertura. A D1 fica como **proposta**, levada no gatilho D, e não como decisão.
- **Opções à Presidência.** (1) Fazer a absorção do (b) e do (c) na v1.10, por linha que precise "próxima ocorrência da T-12" nas duas decisões. (2) Absorver agora, numa v1.9.1.
- **Recomendação da GBQ:** opção (1), porque ajusta só o momento de duas decisões da própria Presidência (competência D: erratas textuais e ordem), sem tocar a D-REFORCO-1 do Fundador, e mantém a v1.9 com delta exclusivo de itens novos, já conferido byte a byte. A opção (2) obrigaria a regenerar (v1.9.1) e refazer a fidelidade, adiando o gatilho A e a onda 2 (D-ONDA1-FILA (6)).
- Até a resposta, o gatilho A da v1.9 vale para o objeto como está. Se a Presidência escolher (2), ela devolve a v1.9 e a GBQ regenera.

## 3. A-4 — D-RT94-02 (D1 da GBQ)

A edição .md do estudante (`saida/estudante/`, 34 arquivos) não é objeto da v1.9 e fica na v1.8, sem os 48. Motivos:
- A T-94 nomeia o objeto: "no pacote.json e no pacote_estudante.json v1.9 (dados e estudante)". O "(dados e estudante)" da D-REFORCO-1 se cumpre com o `pacote_estudante.json`, que é o pacote do estudante.
- A D-REFORCO-2 prevê "edição do estudante" nas consolidações **a cada duas ondas** (v1.10, v1.11…). A v1.9 consolida uma onda só.
- O precedente da D-PACOTE-V18 (JSON e edição .md) foi o objeto da T-81, fixado na D1 dela, e não uma regra para toda ocorrência.

Nenhuma letra vigente é contrariada, então é D1. Fica registrado no gatilho A: a edição .md canônica continua a v1.8 (manifesto `0b7391fa…`) e não traz os 48. Ela entra na v1.10 com o campo `nucleo`.

## 4. Média real de itens por ciclo da onda 1 (D-REFORCO-2; D-ONDA1-FILA (5))

- s12c1: 48 itens produzidos, revisados em até 2 rodadas e aceitos (T-89 a T-92). Isso dá 48 em 1 ciclo de produção.
- s12c2: T-102 (GCB), 2 itens (L6B-R01, R02), reconciliados pela GCB e aguardando aceite da Presidência no mesmo PARA_PRESIDENCIA. Entram na v1.10.
- **Média real da onda 1: 25 itens por ciclo** (50 itens em 2 ciclos, s12c1 e s12c2), se a T-102 for aceita. Sem ela: 24 (48 em 2 ciclos). Saldo da D-REFORCO-1 depois da T-102: 0.

## 5. Estado

Fidelidade reconciliada; A-1 e A-2 corrigidos; A-3 em gatilho D; A-4 D1 (D-RT94-02); A-5 a A-7 registrados. Gatilho A e gatilho E emitidos. A publicação à candidata é reservada ao Fundador (T-94; D-REFORCO-1; D-T81-RESPOSTA).
