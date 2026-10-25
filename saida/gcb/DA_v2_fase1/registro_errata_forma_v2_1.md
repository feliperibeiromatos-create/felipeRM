# registro_errata_forma_v2_1.md — T-130 — 2026-10-25 — gerado por gcb-cpp

Errata de forma pós-R2 (v2 → v2_1). Sem nova rodada de QA; nenhum enunciado, gabarito ou item novo. Cada alteração vale para v2_1_producao.md e para o JSON (mesmo texto, 1 ocorrência em cada), salvo indicação. Linhas = v2_producao.md.

| Achado | Local | Antes | Depois |
|---|---|---|---|
| R2-1 | L843 (md e JSON) | "Alterado pelo Decreto 12.967/2026, art. 9º, que não toca os artigos acima." | "O Decreto 12.967/2026 (art. 1º), que alterou o art. 9º, §§ 6º e 8º, do Decreto 12.374, não toca os artigos acima." |
| R2-1 | L847 (md e JSON) | "Decreto 12.967/2026, art. 9º (alteração que não toca esses artigos)" | "Decreto 12.967/2026 (art. 1º), que alterou o art. 9º, §§ 6º e 8º, do Decreto 12.374 (alteração que não toca esses artigos)" |
| R2-3 | L847 (md e JSON) | "texto conferido em 2026-10-20 e reconferido em 2026-10-25 em planalto.gov.br" | "texto dos arts. 2º e 24 conferido em 2026-10-20 e reconferido em 2026-10-25; art. 1º do Decreto 12.374 conferido pela primeira vez em 2026-10-25; em planalto.gov.br" |
| R2-3 | L1273 (só md) | "2026-10-20 (mapa D2, seção 4.8); reconferido em 2026-10-25 (qa_normativo_R1)" | "2026-10-20 (mapa D2, seção 4.8: arts. 2º e 24); reconferido em 2026-10-25 (qa_normativo_R1); art. 1º: primeira conferência em 2026-10-25 (qa_normativo_R2)" |
| R2-2 | L1566 (md e JSON), CF art. 5º, XII e LVI | "texto conferido em 2026-10-20 em planalto.gov.br" | "texto conferido em 2026-10-20 e reconferido em 2026-10-25 (qa_normativo_R2) em planalto.gov.br" |
| R2-2 | L1726 (md e JSON), Lei 9.784 arts. 58, 60, 62 e 59, § 2º | "texto conferido em 2026-10-20 em planalto.gov.br" | "texto conferido em 2026-10-20 e reconferido em 2026-10-25 (qa_normativo_R2) em planalto.gov.br" |
| R2-2 | L2051 (só md) | "Arts. 58, 60 e 62: texto do mapa D2 (2026-10-20), não incluídos na tabela do qa_normativo_R1 e a conferir na R2" | "Arts. 58, 60 e 62 e art. 59, § 2º: texto do mapa D2 (2026-10-20), reconferido em 2026-10-25 (qa_normativo_R2)" |
| R2-2 | L2052 (só md), CF art. 5º, XII e LVI | "NÃO reconferido em 2026-10-25: a conferir na R2" | "reconferido em 2026-10-25 (qa_normativo_R2)" |
| R2-4 | L2051 (só md) | "Art. 69: aplicam-se à lei própria apenas subsidiariamente os preceitos da Lei 9.784." | "Art. 69: aos processos regidos por lei própria aplicam-se apenas subsidiariamente os preceitos da Lei 9.784." |
| O-R2-1 | L1525 (md e JSON, curso do DV3) | "ITEM DV3-09 / ITEM DV3-10" (2 ITEM no quadro Atos) | "ITEM DV3-09" apenas. O DV3-10 volta à verificação, com o comentario que já tinha. Enunciado, gabarito e comentario inalterados. DV3-21 não criado (fica PRÓXIMO). |
| O-R2-2 | L713 (md e JSON) | "...em trinta dias contados da publicação do ato de provimento; ... em quinze dias contados da posse." | "...(Lei 8.112/1990, art. 13, § 1º); ... contados da posse (art. 15, § 1º)." |
| O-R2-2 | L994 | "dez a trinta dias, contados da publicação do ato." | "... (Lei 8.112/1990, art. 18)." |
| O-R2-2 | L1305 | "prazo supletivo de cinco dias e ... três dias úteis." | "prazo supletivo de cinco dias (Lei 9.784/1999, art. 24) e ... três dias úteis (art. 26, § 2º)." |
| O-R2-2 | L1307 | "...igual período motivado." | "...igual período motivado (Lei 9.784/1999, art. 49)." |
| O-R2-2 | L1501 | "...dilatáveis até o dobro mediante comprovada justificação." | "... (Lei 9.784/1999, art. 24)." |
| O-R2-2 | L1503 | "antecedência mínima de três dias úteis. Intimação feita" | "antecedência mínima de três dias úteis (Lei 9.784/1999, art. 26, § 2º). Intimação feita" |
| O-R2-2 | L1594 | "...igual período, expressamente motivados." | "... (Lei 9.784/1999, art. 49)." |

Não aplicado (fora do escopo da ordem): R-R2-1 a R-R2-3 e demais R (PRÓXIMO). L876 ("cinco condições") e "cinco anos" em L1307 seguem sem artigo.

Efeito no verificador (checa_pacote_v2_v2_1.md): 0 bloqueios; avisos de 12 para 13. Mudanças: DV3 passa de 6 para 7 questões de verificação além dos intercalados (aviso "meta 10" persiste na conta do script; por itemEdital vale a ESPEC §7) e de 14 para 13 ITEM por 70 quadros; novo aviso mecânico em DV2 3.4 ("2 parágrafos com mais de 4 frases"), porque o contador da regra trata o "art." das citações inseridas em L713 como fim de frase. Não é frase nova.
