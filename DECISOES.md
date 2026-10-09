# DECISOES — entrada da Presidência para a fábrica (v2). Linha nova: "NOVA | D-XXX | enunciado". O orquestrador aplica e troca para "APLICADA <data>".
## Vigentes (resumo operacional; o texto completo está no Estado Canônico do Projeto)
APLICADA 9/10 | D-ESCOPO | módulos RF/IA (P2) e TI itens 5–8 (P1); D-ESCOPO-2 (Fundador): TI itens 1–4 via Lotes 6a/6b; nada de Linguística, Processo Legislativo ou Ciência Política; peça no gênero da função DESCARTADA.
APLICADA 9/10 | D-ROTULOS | CEBRASPE_OFICIAL só certame-alvo/ciclo (cd_25_ns, cd_26_*); ANALOGA para os demais certames Cebraspe.
APLICADA 9/10 | D-ANO | "ano do edital (aplicação dd/mm/aaaa)".
APLICADA 9/10 | D-ADERENCIA | parcial = só simulado diagnóstico.
APLICADA 9/10 | D-MC | múltipla escolha não entra no banco.
APLICADA 9/10 | D-QA-PENDENTE | item sem QA marcado; nunca em simulado.
APLICADA 9/10 | D-LACUNAS / D-COMPLEMENTOS | 30 AUTORAL por lote em subitens sem análogo; cumprida em todos os lotes; não abrir novos sem ordem.
APLICADA 9/10 | D-RUBRICA / D-T2 | padrão de resposta formato Cebraspe; peça = parecer técnico (confirmado Cargos 1 e 2 cd_25_ns; analogia para o Cargo 11); risco residual registrado, sem produção.
APLICADA 9/10 | D-DEREP | "Derep (antigo DETAQ)", Ato da Mesa 251/2026.
APLICADA 9/10 | D-LEI-15352 | ANPD = Agência Nacional de Proteção de Dados (Lei 15.352/2026), verificada no Planalto.
APLICADA 9/10 | D-REVERIFICACAO-JAN | janela única 4–8/1/2027; GCE-CQFP para P2, FV/gcb-cqfp para P1.
APLICADA 9/10 | D-CANONICOS | Lotes 1, 1-C, 2, 3, 4 (v3.3), 4-C, 5 (v3.1), 5-C canônicos; 6a/6b aguardam gatilho A da GCB.
APLICADA 9/10 | D-ONBOARDING (Fundador) | plataforma pergunta por módulo "Você já tem algum conhecimento?": SIM → diagnóstico; NÃO → curso do zero com teste de lote.
## Novas (a Presidência acrescenta aqui)
APLICADA 9/10 | D-RECUPERACAO | Banco BQ-0001 a 0066, varreduras de 08 e 09/10, qualidade de 09/10, estilo_banca v1.0 e Simulado 0 recuperados do git (fb5bd44, 8c2f203); ids preservados, sem renumeração. R-01 e R-02 CONCLUÍDAS por recuperação. Antes de qualquer outra tarefa: (a) prefixar observacoes de BQ-0047 a 0066 com "QA PENDENTE; " se ainda não estiver; (b) retirar do banco toda linha de item de múltipla escolha (D-MC) e registrar em saida/banco/varredura_2026-10-09.md "localizado, formato incompatível (múltipla escolha)", com o link; (c) em BQ-0025, acrescentar em observacoes "gabarito preliminar C alterado para E no definitivo". R-03 reduzida ao QA de BQ-0047 a 0066 remanescentes; o estilo_banca v1.0 fica mantido. R-04 mantida. T-03 pelos ids originais.
APLICADA 9/10 | D-LEI15352-PROV | Acrescentar ao final de regras/proveniencia.md: "Lei 15.352/2026: alterou a LGPD (art. 5º, VIII e XIX; Capítulo IX; arts. 55-A e 55-C); ANPD = Agência Nacional de Proteção de Dados, autarquia de natureza especial vinculada ao MJSP. Verificada pela Presidência em 7/10/2026 (planalto.gov.br, LGPD compilada) e pela GCB-CQFP em 8/10/2026 (L15352.htm). Fonte oficial verificada."
APLICADA 9/10 | D-BACKUP | Ao fim de todo ciclo, o orquestrador faz commit em main e push para origin (felipeRM). Se o push falhar, imprime "GATE: backup não enviado — decisão humana" e não encerra o ciclo como concluído.
