# -*- coding: utf-8 -*-
"""T-104 (v1.10) — chaves da ocorrência (D1 da GBQ, saida/pacote/T104_D1_v1_10_2026-10-18.md). Lidas por todos os passos do pipeline, para que a geração seja uma só.
E_CURSO: ponto (e) da D-ABSORCAO-V110-E, errata T-106 do curso do L2. Condição: gatilho A da T-106 aceito pela presidencia antes da geração final. Falso no ensaio;
         o ensaio pode ser repetido com a variável de ambiente T104_E_CURSO=1 (só no scratchpad ou em out/, nunca promovido sem a condição).
E_PADRAO: ponto (e), aspecto (xv) da D3. Condição (aplicado e conferido pelo orquestrador; D-T106-XV-ERRATA) cumprida em 18/10/2026 (commit ab3d09f): verdadeiro.
E_L2R131: L2-R131 (T-105), só com o gatilho A da T-105 aceito antes da geração final (linha da T-105; D-ONDA4-FILA). Falso no ensaio;
          T104_L2R131=1 repete o ensaio com o item; ATO_L2R131 tem de ser o id da decisão de aceite em DECISOES.md (nucleo.py e validate_v110.py o procuram lá).
GERADO_EM: data da geração (a final fixa a do dia em que rodar; o ensaio usa 18/10/2026)."""
import os

# GERAÇÃO FINAL (18/10/2026, ciclo s13c2; D-ONDA4-FILA-2 (2)): chaves fixadas pelos aceites da presidencia — E_CURSO pela D-T106-CURSO-ACEITE; E_L2R131 e ATO_L2R131
# pela D-T105-SALDO-ACEITE (adendo 1 da D1). As variáveis de ambiente do ensaio deixam de ser lidas. FINAL: a conferência (3) admite os promovidos e o contrato v1.2.7.
E_CURSO = True
E_PADRAO = True
E_L2R131 = True
ATO_L2R131 = 'D-T105-SALDO-ACEITE'
GERADO_EM = '2026-10-18'
FINAL = True
NOME = 'Câmara 2026 — pacote F4 (v1.10)'
NOME_E = 'Câmara 2026 — pacote do estudante (v1.10-E)'
