ORQUESTRADOR: BANCO
REMETENTE: Fundador (decisão D-ONDAS de 25/10/2026), redigida pela gbq-gerencia na sessão s19
DESTINATÁRIO: EXEC (Fábrica)
PROMPT:
a) Objeto: onda 2 da verificação no CDN oficial do Cebraspe dos candidatos de Direito Administrativo de banco/candidatos/candidatos_DA_TEC2025_fila_v2.csv: verificar as 25 provas abaixo e incorporar ao banco/banco.csv os localizados, com gabarito definitivo, como CEBRASPE_ANALOGA. Produção gbq-cfp (Sonnet) + QA independente (Opus), máx. 2 rodadas. Tarefa T-135.
b) Gerência titular: GCB (Direito Administrativo); GBQ em cópia.
c) Escopo da onda 2: provas 16–40 da fila v2 — banco/candidatos/resumo_por_prova_v2.csv ordenado pelo mesmo critério da onda 1 (mais candidatos Certo/Errado; empate na ordem do arquivo), excluídas as 15 provas da onda 1 e as provas com 0 Certo/Errado (estas ficam na fila com status "ME — só insumo de pegadinha"). Total estimado: 365 candidatos C/E em 25 provas de 16 certames (só BDMG, CAU MG, INSS, SUSEP, Pref. Aracaju, MPE CE, INSA, IBAMA e TJ PA são pastas novas em relação à onda 1); nenhum já confrontado com gabarito oficial. Usar item_edital_wb, aderencia_wb e mecanismo_wb só como ponto de partida; os marcados "Sem enquadramento"/"duvidoso" vão para reserva_DA.csv salvo justificativa do QA. Só itens Certo/Errado; múltipla escolha fica na fila com status "ME — só insumo de pegadinha".

| # | prova_tec (fila v2) | C/E | já verificados | pasta CDN provável |
|---|---|---|---|---|
| 16 | Ana Desen (BDMG)/BDMG/Engenharia/2025 | 18 | 0 | bdmg_25 (?) |
| 17 | Ass AF (CAU MG)/CAU MG/2025 | 18 | 0 | cau_mg_24 (?) |
| 18 | AJ TRT10/TRT 10/Apoio Especializado/Arquitetura/2025 | 18 | 0 | trt10_24 (repo) |
| 19 | Comp (InoversaSul)/InoversaSul/2025 | 17 | 0 | inoversasul_25 (?) |
| 20 | Adm (PF)/PF/2025 | 17 | 0 | pf_25 / pf_25_adm (repo) |
| 21 | Ana (EMBRAPA)/EMBRAPA/Direito e Auditoria/Assessoria Jurídica - Advogado/2025 | 17 | 0 | embrapa_24 (repo) |
| 22 | PMF (INSS)/INSS/2025 | 16 | 0 | inss_25_pmf (?) |
| 23 | Assist (FUB)/FUB/Administração/2025 | 16 | 0 | fub_25 (repo) |
| 24 | AJ TRF6/TRF 6/Administrativa/Sem Especialidade/2025 | 16 | 0 | trf6_24 (repo) |
| 25 | AJ (TJ PA)/TJ PA/Direito/2025 | 15 | 0 | tj_pa_24 (?) |
| 26 | ERM (ANM)/ANM/Direito/Sem Especialidade/2025 | 15 | 0 | anm_24 (repo) |
| 27 | Ana Tec (SUSEP)/SUSEP/Contabilidade Pública/2025 | 15 | 0 | susep_25 (repo) |
| 28 | Adv (CAU MG)/CAU MG/2025 | 15 | 0 | cau_mg_24 (?) |
| 29 | Proc Mun (Aracaju)/Pref Aracaju/2025 | 15 | 0 | pgm_aracaju_25 (?) |
| 30 | AJ (TJ PA)/TJ PA/Administração/2025 | 14 | 0 | tj_pa_24 (?) |
| 31 | Ana Min (MPE CE)/MPE CE/Direito/2025 | 13 | 0 | mpe_ce_24 (?) |
| 32 | Tecno P-2 (INSA)/INSA/Inovação/2025 | 13 | 0 | insa_24 (?) |
| 33 | AA (ANM)/ANM/Direito/2025 | 13 | 0 | anm_24 (repo) |
| 34 | Aud (FUB)/FUB/2025 | 12 | 0 | fub_25 (repo) |
| 35 | AJ TRT10/TRT 10/Judiciária/"Sem Especialidade"/2025 | 12 | 0 | trt10_24 (repo) |
| 36 | ERM (ANM)/ANM/Comunicação/2025 | 12 | 0 | anm_24 (repo) |
| 37 | AA (IBAMA)/IBAMA/2025 | 12 | 0 | ibama_25 (?) |
| 38 | Ana Min (MPE CE)/MPE CE/Engenharia Civil/2025 | 12 | 0 | mpe_ce_24 (?) |
| 39 | AA (ANM)/ANM/Administração, Economia, Contabilidade ou Direito/2025 | 12 | 0 | anm_24 (repo) |
| 40 | Tec (EMBRAPA)/EMBRAPA/Suprimento, Manutenção e Serviços/Suporte à Gestão/2025 | 12 | 0 | embrapa_24 (repo) |

d) Arquivos-base: a fila v2 e os resumos v2 em banco/candidatos/; relatório da onda 1 (saida/banco/varredura_DA_onda1_<data>.md) e a reserva_DA.csv; regras/estilo_banca_DA_v1.md (registrar o campo mecanismo de cada item incorporado); edital/DA_itens_1_12_P1.md; banco/banco.csv; regras/estilo_banca.md; estado/Estado_Canonico_Camara_2026.md.
e) Regras (e.1–e.9 idênticas às da ONDA1; a regra de mecanismo, impressa na ONDA1 como segundo "8", fica aqui como e.6-A):
   1. Fonte única: cdn.cebraspe.org.br. Para cada prova, resolver a pasta do concurso e abrir o caderno do cargo indicado no metadado TEC e o GABARITO DEFINITIVO. A coluna "pasta CDN provável" é só hipótese: "(repo)" = pasta já citada em arquivos do repositório; "(?)" = palpite não verificado [SEM FONTE — não afirmar]. Sem caderno ou sem gabarito definitivo: candidato "NÃO LOCALIZADO", não entra. Pastas e cadernos já resolvidos em onda anterior são reutilizados, com o mesmo localiza_cdn.py.
   2. Texto do candidato deve ser encontrado no pdftotext do caderno (normalizar espaços e hifenização), com número do item e comando do bloco lidos do caderno. Texto do banco = texto do caderno, nunca o da fila.
   3. Gabarito = o do definitivo. Anulado → X, fora de simulado. Divergência com o gabarito_tec da fila → observacoes + item de QA; o oficial prevalece.
   4. Rótulo CEBRASPE_ANALOGA com certame, ano, cargo, nº do item, URLs, data_verificacao, verificado_por. Nenhuma destas provas é do certame-alvo nem de seu ciclo: CEBRASPE_OFICIAL vedado (D-ROTULOS).
   5. item_edital_camara pelo conhecimento exigido (coluna item_edital_heuristico é só ponto de partida). Candidatos FORA (13.303, PPP, convênios, SRP, IN 65, controle, anticorrupção, bens) entram só com enquadramento justificado pelo QA; senão saida/banco/reserva_DA.csv com motivo. Aderência parcial: só simulado diagnóstico (D-ADERENCIA), marcada na linha.
   6. Fichas e justificativas do pacote de origem (outra IA): só leitor crítico; toda justificativa é da Fábrica, com QA normativo quando citar lei.
   6-A. Mecanismo (adendo v2.1, D-ESPEC-DA-V2-1): registrar `mecanismo` de cada item incorporado com a tabela de regras/estilo_banca_DA_v1.md §4 (LIT, CON, SUP, PRA, GEN, AP, MIX, NEG, AUT, AMB, TEM); a coluna mecanismo_wb da fila é só ponto de partida. O QA da onda inclui a reclassificação cega de uma amostra de 100 itens incorporados nesta onda (todos, se forem menos de 100) por agente de modelo distinto do que classificou, com a taxa de concordância no relatório (ESTILO §7); abaixo de 80% de concordância, a tabela de mecanismos volta à Presidência antes de ser usada na plataforma. Se uma onda anterior já a tiver devolvido, a classificação segue, com o campo marcado "mecanismo provisório".
   7. Temporal: provas de 2025; marcar VOLÁTIL-NORMATIVO (fora de simulado final; reverificar 4–8/1/2027) o item cujo gabarito dependa de norma alterada desde a prova (LGPD/ANPD pela Lei 15.352/2026; 14.133 e 8.112 por alterações 2025–2026).
   8. Deduplicação por hash do texto normalizado contra o banco (inclusive os itens das ondas anteriores) e dentro da onda; duplicatas informadas por ID.
   9. Nenhuma publicação; pacote só muda com gatilho A da GBQ e "sim" do Fundador.
f) Saída: banco/banco.csv atualizado; saida/banco/varredura_DA_onda2_<data>.md (por prova: pasta resolvida, caderno/gabarito abertos, localizados / não localizados / anulados / divergentes; contagem por item do edital antes e depois, contra a meta ≥ 30 reais em 10, 7, 3.4/4, 4.4, 1.2, e quanto falta em 1.1, 2, 3, 5, 6; taxa de concordância da reclassificação cega de mecanismo); parecer de QA; reserva_DA.csv atualizada; confirmação ou revisão da estimativa da ONDA3.
g) Classificação: AGORA (D-ONDAS; gasto já autorizado pelo Fundador). Dependência: só começa após a conclusão da T-129 (ONDA1). Teto de gasto da D-ONDAS: 5 sessões por semana, somadas todas as ordens autorizadas pela D-ONDAS; pausa imediata por linha NOVA em DECISOES.md.
