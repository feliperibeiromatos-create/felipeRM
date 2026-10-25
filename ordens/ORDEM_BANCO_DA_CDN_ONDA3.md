ORQUESTRADOR: BANCO
REMETENTE: Fundador (decisão D-ONDAS de 25/10/2026), redigida pela gbq-gerencia na sessão s19
DESTINATÁRIO: EXEC (Fábrica)
PROMPT:
a) Objeto: onda 3 (final) da verificação no CDN oficial do Cebraspe dos candidatos de Direito Administrativo de banco/candidatos/candidatos_DA_TEC2025_fila_v2.csv: verificar as 70 provas restantes com Certo/Errado, incorporar ao banco/banco.csv os localizados, com gabarito definitivo, como CEBRASPE_ANALOGA, e encerrar a fila v2. Produção gbq-cfp (Sonnet) + QA independente (Opus), máx. 2 rodadas. Tarefa T-139.
b) Gerência titular: GCB (Direito Administrativo); GBQ em cópia.
c) Escopo da onda 3: provas 41–110 da fila v2 — o restante de banco/candidatos/resumo_por_prova_v2.csv pelo mesmo critério das ondas 1 e 2 (mais candidatos Certo/Errado; empate na ordem do arquivo), excluídas as 40 provas das ondas 1–2 e as 33 provas com 0 Certo/Errado (203 candidatos, todos de múltipla escolha: status "ME — só insumo de pegadinha", sem verificação no CDN). Total estimado: 339 candidatos C/E em 70 provas de 20 certames, das quais 39 têm ≤ 5 candidatos; 17 já confrontados com gabarito oficial pelo pacote de auditoria (DPF/PF 9; AAmb ICMBio 8), a reconferir. Trabalhar agrupado por pasta: só Pref. Andradina, PC DF, IRBr, ANTAQ e ANS são pastas novas; as demais (PF, EMBRAPA, ANM, TRF6, TRT10, STM, FUB, MPE CE, TJ PA, INSA, IBAMA, TCE-RS, FUNPRESP-EXE, ICMBio, InoversaSul) vêm das ondas 1–2. Usar item_edital_wb, aderencia_wb e mecanismo_wb só como ponto de partida; os marcados "Sem enquadramento"/"duvidoso" vão para reserva_DA.csv salvo justificativa do QA. Só itens Certo/Errado.

| # | prova_tec (fila v2) | C/E | já verificados | pasta CDN provável |
|---|---|---|---|---|
| 41 | Proc Jur (Andradina)/Pref Andradina/2025 | 11 | 0 | andradina_25 (?) |
| 42 | AAAPC (PC DF)/PC DF/Agente Administrativo/2025 | 11 | 0 | pcdf_24 (?) |
| 43 | AA (ANM)/ANM/Engenharia Civil/Segurança do Trabalho/2025 | 11 | 0 | anm_24 (repo) |
| 44 | Ana Min (MPE CE)/MPE CE/Ciências Contábeis/2025 | 10 | 0 | mpe_ce_24 (?) |
| 45 | ERM (ANM)/ANM/Direito/Outorga/2025 | 10 | 0 | anm_24 (repo) |
| 46 | AJ TRF6/TRF 6/Apoio Especializado/Engenharia Civil/2025 | 10 | 0 | trf6_24 (repo) |
| 47 | Tec (EMBRAPA)/EMBRAPA/Orçamento e Finanças/Contabilidade/2025 | 10 | 0 | embrapa_24 (repo) |
| 48 | DPF/PF/2025 | 9 | 9 | pf_25 / pf_25_adm (repo) |
| 49 | ERM (ANM)/ANM/Qualquer Área de Formação/Fiscalização e Distribuição de Receitas/2025 | 9 | 0 | anm_24 (repo) |
| 50 | AA (ANM)/ANM/Administração/2025 | 9 | 0 | anm_24 (repo) |
| 51 | ERM (ANM)/ANM/Tecnologia da Informação/Ciência de Dados/2025 | 9 | 0 | anm_24 (repo) |
| 52 | AJ TRT10/TRT 10/Administrativa/Contabilidade/2025 | 8 | 0 | trt10_24 (repo) |
| 53 | AAmb (ICMBio)/ICMBio/2025 | 8 | 8 | icmbio_24 (repo) |
| 54 | AAmb (IBAMA)/IBAMA/Proteção, Conservação, Licenciamento, Monitoramento e Qualidade Ambiental/2025 | 8 | 0 | ibama_25 (?) |
| 55 | Tec (FUB)/FUB/Laboratório/Análise Clínica/2025 | 8 | 0 | fub_25 (repo) |
| 56 | Pesq A-I (INSA)/INSA/Biodiversidade/2025 | 8 | 0 | insa_24 (?) |
| 57 | AJ TRF6/TRF 6/Judiciária/Sem Especialidade/2025 | 8 | 0 | trf6_24 (repo) |
| 58 | GAAPC (PC DF)/PC DF/Analista de Informática/Banco de Dados/2025 | 8 | 0 | pcdf_24 (?) |
| 59 | Arqt e Urb (FUB)/FUB/2025 | 8 | 0 | fub_25 (repo) |
| 60 | Tec (EMBRAPA)/EMBRAPA/Suprimento, Manutenção e Serviços/Monitoramento Preditivo/2025 | 8 | 0 | embrapa_24 (repo) |
| 61 | Ana Min (MPE CE)/MPE CE/Administração/2025 | 7 | 0 | mpe_ce_24 (?) |
| 62 | AJ (STM)/STM/Judiciária/"Sem Especialidade"/2025 | 7 | 0 | stm_25 (?) |
| 63 | Ana (EMBRAPA)/EMBRAPA/Gestão Estratégica/Riscos, Conformidade e Transparência/2025 | 7 | 0 | embrapa_24 (repo) |
| 64 | AJ (TJ PA)/TJ PA/Administrativa/2025 | 7 | 0 | tj_pa_24 (?) |
| 65 | APC (FUNPRESP-EXE)/FUNPRESP-EXE/Jurídica/2025 | 7 | 0 | funpresp_exe_24 (?) |
| 66 | EPF/PF/2025 | 6 | 0 | pf_25 / pf_25_adm (repo) |
| 67 | PCF/PF/Área 1/2025 | 6 | 0 | pf_25 / pf_25_adm (repo) |
| 68 | Tec (EMBRAPA)/EMBRAPA/Gestão da Informação/Tecnologia da Informação/2025 | 6 | 0 | embrapa_24 (repo) |
| 69 | AJ TRT10/TRT 10/Apoio Especializado/Enfermagem do Trabalho/2025 | 6 | 0 | trt10_24 (repo) |
| 70 | AJ TRF6/TRF 6/Apoio Especializado/Medicina Cardiologia/2025 | 6 | 0 | trf6_24 (repo) |
| 71 | Tec Min (MPE CE)/MPE CE/2025 | 6 | 0 | mpe_ce_24 (?) |
| 72 | Ana (EMBRAPA)/EMBRAPA/Transferência de Tecnologia e Comunicação/Gestão de Instrumentos de Parcerias e Negócios/2025 | 5 | 0 | embrapa_24 (repo) |
| 73 | AJ TRF6/TRF 6/Apoio Especializado/Contabilidade/2025 | 5 | 0 | trf6_24 (repo) |
| 74 | Ana (EMBRAPA)/EMBRAPA/Suprimento, Manutenção e Serviços/Ativos Patrimoniais e Imobiliários/2025 | 5 | 0 | embrapa_24 (repo) |
| 75 | OFA (TJ PA)/TJ PA/2025 | 5 | 0 | tj_pa_24 (?) |
| 76 | Diplomata/IRBr/2025 | 5 | 0 | irbr_25_diplomata (?) |
| 77 | ERM (ANM)/ANM/Qualquer Área de Formação/Suporte à Gestão, Estratégia e Governança/2025 | 4 | 0 | anm_24 (repo) |
| 78 | APE (TCE-RS)/TCE RS/Engenharia Civil/2025 | 4 | 0 | tce_rs_25 (?) |
| 79 | Ana (EMBRAPA)/EMBRAPA/Transferência de Tecnologia e Comunicação/Gestão de Parcerias, Portfólios e Negócios para a Inovação/2025 | 3 | 0 | embrapa_24 (repo) |
| 80 | AJ (STM)/STM/Apoio Especializado/Comunicação Social/2025 | 3 | 0 | stm_25 (?) |
| 81 | AJ (TJ PA)/TJ PA/Comunicação Social/2025 | 3 | 0 | tj_pa_24 (?) |
| 82 | Ana (EMBRAPA)/EMBRAPA/Gestão da Informação/Gestão da Informação Arquivística/2025 | 3 | 0 | embrapa_24 (repo) |
| 83 | TJ TRF6/TRF 6/Apoio Especializado/Contabilidade/2025 | 2 | 0 | trf6_24 (repo) |
| 84 | AA (ANM)/ANM/Qualquer Área de Formação/2025 | 2 | 0 | anm_24 (repo) |
| 85 | Pesq (EMBRAPA)/EMBRAPA/Ciências Exatas e da Terra/Engenharia de Processos Químicos/2025 | 2 | 0 | embrapa_24 (repo) |
| 86 | Ana (EMBRAPA)/EMBRAPA/Gestão de Pessoas/Saúde Ocupacional/2025 | 2 | 0 | embrapa_24 (repo) |
| 87 | Ana (EMBRAPA)/EMBRAPA/Orçamento e Finanças/Orçamento e Finanças/2025 | 2 | 0 | embrapa_24 (repo) |
| 88 | Ana (EMBRAPA)/EMBRAPA/Direito e Auditoria/Auditoria Contábil/2025 | 2 | 0 | embrapa_24 (repo) |
| 89 | Ass Soc (PF)/PF/2025 | 2 | 0 | pf_25 / pf_25_adm (repo) |
| 90 | AJ (STM)/STM/Apoio Especializado/Administração/2025 | 2 | 0 | stm_25 (?) |
| 91 | AJ TRF6/TRF 6/Apoio Especializado/Arquitetura/2025 | 2 | 0 | trf6_24 (repo) |
| 92 | APE (TCE-RS)/TCE RS/Tecnologia da Informação/2025 | 2 | 0 | tce_rs_25 (?) |
| 93 | Ana (EMBRAPA)/EMBRAPA/Gestão da Informação/Engenharia de Infraestrutura e Tecnologia da Informação/2025 | 2 | 0 | embrapa_24 (repo) |
| 94 | Ana (EMBRAPA)/EMBRAPA/Gestão da Informação/Gestão da Informação Bibliográfica/2025 | 2 | 0 | embrapa_24 (repo) |
| 95 | AJ TRF6/TRF 6/Apoio Especializado/Arquivologia/2025 | 2 | 0 | trf6_24 (repo) |
| 96 | AJ TRT10/TRT 10/Apoio Especializado/Arquivologia/2025 | 2 | 0 | trt10_24 (repo) |
| 97 | ERSTA (ANTAQ)/ANTAQ/Curso de Formação/2025 | 1 | 0 | antaq_24 (?) |
| 98 | Ana (EMBRAPA)/EMBRAPA/Ciências Sociais Aplicadas/Ciências Sociais Aplicadas a Agropecuária/2025 | 1 | 0 | embrapa_24 (repo) |
| 99 | ERSS (ANS)/ANS/Sem Área/2025 | 1 | 0 | ans_24 (?) |
| 100 | AA (ANM)/ANM/Pedagogia/2025 | 1 | 0 | anm_24 (repo) |
| 101 | TJ (STM)/STM/Agente da Polícia Judicial/2025 | 1 | 0 | stm_25 (?) |
| 102 | Ana Min (MPE CE)/MPE CE/Arquitetura e Urbanismo/2025 | 1 | 0 | mpe_ce_24 (?) |
| 103 | PCF/PF/Área 3/2025 | 1 | 0 | pf_25 / pf_25_adm (repo) |
| 104 | AJ (STM)/STM/Apoio Especializado/Suporte em Tecnologia da Informação/2025 | 1 | 0 | stm_25 (?) |
| 105 | AA (ANM)/ANM/Publicidade e Propaganda/Design Gráfico ou Desenho Industrial/2025 | 1 | 0 | anm_24 (repo) |
| 106 | APC (FUNPRESP-EXE)/FUNPRESP-EXE/Previdência/2025 | 1 | 0 | funpresp_exe_24 (?) |
| 107 | GAAPC (PC DF)/PC DF/Arquivista/2025 | 1 | 0 | pcdf_24 (?) |
| 108 | Arq (InoversaSul)/InoversaSul/2025 | 1 | 0 | inoversasul_25 (?) |
| 109 | Ana (EMBRAPA)/EMBRAPA/Gestão da Informação/Avaliação de Impactos/2025 | 1 | 0 | embrapa_24 (repo) |
| 110 | AJ TRT10/TRT 10/Apoio Especializado/Comunicação Social/2025 | 1 | 0 | trt10_24 (repo) |

d) Arquivos-base: a fila v2 e os resumos v2 em banco/candidatos/; relatórios das ondas 1 e 2 (saida/banco/varredura_DA_onda1_<data>.md e varredura_DA_onda2_<data>.md) e a reserva_DA.csv; regras/estilo_banca_DA_v1.md (registrar o campo mecanismo de cada item incorporado); edital/DA_itens_1_12_P1.md; banco/banco.csv; regras/estilo_banca.md; estado/Estado_Canonico_Camara_2026.md.
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
f) Saída: banco/banco.csv atualizado; saida/banco/varredura_DA_onda3_<data>.md (por prova: pasta resolvida, caderno/gabarito abertos, localizados / não localizados / anulados / divergentes; resultado da reconferência dos 17 já verificados; contagem por item do edital antes e depois e acumulada das três ondas, contra a meta ≥ 30 reais em 10, 7, 3.4/4, 4.4, 1.2, e quanto ainda falta em 1.1, 2, 3, 5, 6, como insumo das FASES 2–4 da ORDEM_DA_V2; taxa de concordância da reclassificação cega de mecanismo); parecer de QA; reserva_DA.csv final; fila v2 encerrada: todo candidato com status final (INCORPORADO / NÃO LOCALIZADO / ANULADO / RESERVA / DUPLICATA / ME — só insumo de pegadinha), com a soma fechando em 1.321 (414 + 365 + 339 C/E + 203 ME).
g) Classificação: AGORA (D-ONDAS; gasto já autorizado pelo Fundador). Dependência: só começa após a conclusão da T-135 (ONDA2). Teto de gasto da D-ONDAS: 5 sessões por semana, somadas todas as ordens autorizadas pela D-ONDAS; pausa imediata por linha NOVA em DECISOES.md.
