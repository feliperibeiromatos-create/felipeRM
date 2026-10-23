# Plataforma MapasPro · Câmara 2026 — Plano v15 (quatro abas)

Origem: pedido do Fundador, 18/10/2026. Base técnica: v14 (prévia, aguardando "sim"). Medições feitas no pacote embutido v1.9 (334 itens, 10 lotes) e no edital.

## 1. O que o pacote permite hoje (medido)
| Pedido | Dado disponível | Consequência |
|---|---|---|
| Curso por tópico | 40 de 41 tópicos com questões têm bloco de curso. P1-5 não tem; P1-3 tem 9 palavras. | Viável já; 2 lacunas para a Fábrica. |
| Questões por tópico | Questões por tópico: mínimo 2, máximo 26 (25 não voláteis). Nenhum tópico chega a 30; só 2 chegam a 20. | Decidido em 18/10 (noite): a nota conta só questões distintas, então hoje nenhum tópico tem nota; meta do banco passa a 40 por tópico (ordem F). |
| Resumo por tópico | Resumos existem por lote (350 a 650 palavras), sem divisão por tópico; 3 lotes de complemento sem resumo. | Aba Resumo precisa de resumos novos por tópico (Fábrica). Até lá, mostra o resumo do bloco com aviso. |
| Pegadinhas por tópico | Todas têm o tópico do edital (campo itemEdital). | Viável já. |
| Pares confundíveis → pegadinhas | Pares não têm tópico do edital. | Some da tela já; a conversão do conteúdo é da Fábrica. |
| Peso das matérias | O edital não informa quantos itens cada matéria terá; só P1 = 90, P2 = 90, mínimos de 18 (P1) e 27 (P2) pontos (8.11.5) e discursiva de 60 pontos. | Peso precisa de estimativa (provas anteriores da Câmara pela Cebraspe) ou regra provisória declarada. |
| Infográficos | Há 1 figura em toda a plataforma (box plot). | Precisa de componentes visuais + produção da Fábrica. |

## 2. Arquitetura proposta
Tela de apresentação (antes do concurso): as quatro abas explicadas em uma frase cada, incluindo que a plataforma busca três recomendações de estudo. Depois, escolha do concurso e diagnóstico (fluxo da v14).

| Aba | Conteúdo | Origem dos dados |
|---|---|---|
| 1 Painel | Matérias na ordem do edital (as sem conteúdo como "em preparação"). Toque na matéria → tópicos numerados como no edital, cada um com nota (ou "faltam N respostas") e dois botões: Curso e Questões. No fim da matéria: simulado da matéria quando houver itens. | edital + pacote |
| 2 Resumo | Matéria → tópico → resumo do tópico. | resumos por tópico (Fábrica); provisório: resumo do bloco |
| 3 Erros | Caderno atual agrupado por matéria e tópico; regra de saída (2 acertos seguidos) mantida. | itemEdital de cada item |
| 4 Recomendações | Três tópicos para escolher, mais, quando couber, duas discursivas ou um simulado completo. Cada cartão diz por que foi recomendado. | regra abaixo |

Sai da tela: a palavra "lote" e códigos de lote, ids de arquivo, versões, siglas internas (SIM-0, v0.2), "Pares confundíveis". Fica: número do tópico no edital (é a ordem do edital) e a fonte de cada questão (Cebraspe, ano), exigida pelas regras do Projeto.

## 3. Nota por tópico
Registro de cada resposta (item, tópico, certo/errado/branco, data), alimentado por simulado, diagnóstico, questões do tópico e caderno de erros. Nota = (acertos − erros) ÷ 30 sobre as 30 respostas mais recentes do tópico; antes de 30, mostra "Responda mais N questões para ver sua nota" (texto informado à candidata). Cada bloco de Questões traz 10 itens do tópico: primeiro os nunca vistos, depois os errados, depois os mais antigos. A janela de 30 é recalculada a cada resposta; com blocos de 10, isso equivale a "sai o bloco mais antigo, entra o novo". O histórico da v12 a v14 é convertido no registro na primeira carga.

## 4. Recomendações (regra v1, transparente)
Prioridade do tópico = peso da matéria por tópico × lacuna × disponibilidade.
- Peso: itens esperados da matéria na prova ÷ número de tópicos da matéria (provisório até haver estimativa por provas anteriores).
- Lacuna: 1 − nota, se houver nota; valor alto fixo se ainda não estudado; desconto se estudado nos últimos dias.
- Disponibilidade: só tópicos com curso e questões.
- Desempate a favor da prova mais distante do mínimo eliminatório (18 em P1, 27 em P2).
Discursivas: duas opções quando os cursos dos tópicos que elas cobram foram concluídos e não houve discursiva nos últimos 7 dias. Simulado completo: quando a cobertura de tópicos passar de um limiar (ex.: 60%) e a cada 2 semanas depois. Limiares a decidir; todos ajustáveis.

## 5. Cursos mais visuais
- Leitura: coluna de cerca de 65 caracteres, espaçamento maior, blocos separados por cartões, abertura "Em 1 minuto" com 3 pontos-chave, quadros de Definição, Exemplo parlamentar e Pegadinha, progresso dentro do tópico.
- Componentes desenhados pelo código a partir de dados que a Fábrica escreve: tabela comparativa, fluxo em etapas, linha do tempo, esquema conceito-exemplo e gráfico simples. Respeitam tema claro/escuro e não dependem de imagem externa.
- Produção: a Fábrica reescreve os 40 cursos no formato novo, com QA, começando pelos tópicos de maior peso.

## 6. Classificação
| Classe | Entrega |
|---|---|
| AGORA | Tela de apresentação; quatro abas; Painel matéria → tópico com Curso/Questões; Erros agrupado; sumiço de lotes, pares e metadados; registro de respostas e nota por tópico; Recomendações v1 com peso provisório declarado; leitura do curso redesenhada e componentes visuais com um tópico de demonstração. |
| PRÓXIMO | Pesos estimados por provas anteriores (pesquisa em fontes oficiais Cebraspe); resumos por tópico; conversão de pares em pegadinhas; cursos no formato visual (piloto em 3 tópicos confirmado); banco de 40 questões distintas por tópico nas duas matérias da plataforma (ordem F, prazo a projetar); simulado por matéria. |
| BACKLOG | Ajuste fino dos gatilhos de discursiva e simulado com dados de uso. |
| DESCARTADO | Exibir nota com menos de 30 respostas. |

## 7. Reconciliação com a especificação GPT v0.1 e a leitura complementar (18/10/2026)
- Arquitetura convergente: quatro abas, painel por matéria/tópico, Erros agrupado, sumiço de lotes/pares/ids, janela de 30, ledger de respostas (adotar o formato do GPT: concurso, disciplina, tópico, item, tentativa, data, resultado, tipo de atividade, versão do pacote, elegível para nota; S.eventos não é fonte de verdade).
- Contagem: 38 subitens-folha (15 TI + 23 Fala) + 3 itens-pai de TI com questões próprias (2, 4, 5; 13 questões) = 41 linhas com questões. As duas contagens estão certas; falta decidir como exibir os itens-pai.
- Motor v0 (NUCLEO_ID, VALOR_NUCLEO = 0,60 × INDICE_ENTRADA + 0,40 × INDICE_CLASSIFICACAO): NÃO LOCALIZADO neste Projeto (lista de documentos e três buscas em 18/10/2026). A regra v1 deste plano tem a mesma forma (valor × lacuna × fase) e pode receber o v0 quando ele for trazido.
- CONFLITO entre decisões do Fundador: nota por tópico exige 30 questões distintas (40 para a primeira atualização), mas a meta da Fábrica é de 20 por item-folha até 12/12/2026. Com essa meta, nenhum tópico terá nota. RESOLVIDO em 18/10/2026 (noite): só questões distintas contam, e a meta passa a 40 questões distintas por tópico nas duas matérias da plataforma; os 20 por item-folha continuam nas demais matérias; prazo a projetar pela Fábrica.
- Visual dos cursos: já existe a CII (Imagens e Ilustrações Didáticas, sob a CDJ, SVG à mão, paleta do sistema visual). A plataforma recebe o componente de figura uma vez; a produção segue CDJ → CII.
- Resumos: existem 7 resumos de lote (3 lotes de complemento não têm), não 38 nem 41.
- Artefato da candidata: a memória do Projeto registra que 5fyXGpFMomSHwZuRnu36rC é o laboratório e que a plataforma da candidata nasceu em NePvzy9uLoKYMz8ZZGZKnh ("Folha de Estudo – v0.1"); esta, lida em 18/10, ainda roda o pacote de demonstração. As publicações v12/v13 foram feitas em 5fyX… RESOLVIDO em 18/10/2026 (noite): a candidata usa a "Plataforma Câmara 2026", https://claude.ai/artifact/5fyXGpFMomSHwZuRnu36rC; a versão final vai para lá, só com o "sim, publicar v15" do Fundador.

## 8. Estado de execução (18/10/2026)
- Etapa 2 (quatro abas, Painel por matéria/tópico, curso por tópico, questões em blocos de 10 com janela de 30, Erros agrupado, Resumo provisório por lote, Recomendações A/B/C, limpeza de metadados): PUBLICADA em 18/10/2026, 19h52, como v15.2 na plataforma da candidata (https://claude.ai/artifact/5fyXGpFMomSHwZuRnu36rC, versão 1792363883-b584), com o "sim" do Fundador; pacote F4 v1.9; capacidade de download mantida. A prévia https://claude.ai/artifact/KyVNQZCzQzLbuuv4KXwibU continua como laboratório. Registro: claude/REGISTRO_v15_previa_2026-10-18.md.
- Decisões provisórias no código: repetidas contam (com aviso; SUBSTITUÍDA na v15.2: só questões distintas); peso = 90 ÷ nº de matérias da prova; discursiva após 50% dos cursos de P2; simulado após 60% dos tópicos praticados, 1 a cada 7 dias; itens 2, 4 e 5 de TI como "Visão geral do item N".
- Encomenda à Fábrica (resumos por tópico, pares→pegadinhas, limpeza de referências de produção, L2-R16, piloto visual) registrada em 18/10/2026.
- Revisão de design (skill design-plataformas-interativas): v15.1 publicada na mesma prévia (versão 1792354627-91f8), 13 achados corrigidos, 129/129 testes. Registro: claude/REGISTRO_v15_1_revisao_design_2026-10-18.md.
- Ordens à Fábrica formatadas no padrão FAB-AUTO: claude/ORDENS_FABRICA_encomenda_v15_2026-10-18.md, com o inventário claude/INVENTARIO_marcas_producao_v1.9_2026-10-18.md. Atualizadas em 18/10 (noite): C e D AGORA; B e A PRÓXIMO; E confirmada (P2-1.4, P2-2.5, P1-8.2); nova F (banco de 40). O Fundador cola as ordens direto na sessão da Fábrica no Claude Code.
- Decisões do Fundador, 18/10/2026 (noite): (1) endereço da candidata = https://claude.ai/artifact/5fyXGpFMomSHwZuRnu36rC, só com "sim, publicar v15"; (2) nota de 30 só com questões distintas, aplicada na prévia v15.2 (versão 1792360787-b29b; CONTA_REPETIDAS=false; textos da apresentação, da legenda da matéria e do resultado do bloco ajustados); hoje nenhum tópico chega à nota (máximo 26 questões, em P2-4.1); (3) piloto de curso visual confirmado em 3 tópicos, sugestão P2-1.4, P2-2.5 e P1-8.2; (4) meta de 40 questões distintas por tópico nas duas matérias da plataforma (ordem F), 20 por item-folha nas demais; prazo a projetar pela Fábrica.
- Pendências com o Fundador: motor v0 (se existir no GPT); tamanho do resumo por tópico; capacidade de download para "Exportar meus erros".
- Entrada do próximo pacote da Fábrica preparada: claude/ROTEIRO_entrada_pacote_Fabrica_2026-10-18.md e claude/kit_pacote/ (conferência de ids e gabaritos com registro, validação de pacote.topicos, embutir, regressão R1–R9; testados com pacotes sintéticos em 18/10). A cada pacote novo: atualizar o painel de acompanhamento; publicar só com "sim".
- Próximo pacote conhecido: v1.10 (560 itens, pelo painel). Nenhum tópico chega a 30 questões nele.
- 19/10/2026: plataforma publicada na v15.4 com o pacote v1.12 (749 itens, resumos por tópico e piloto visual), por outra sessão. Laboratório na v15.5: módulo Direito Administrativo, componentes Base legal e Compare, demonstração de formato desligável (claude/REGISTRO_v15_5_DA_laboratorio_2026-10-19.md). Especificação do curso de DA e ordem à Fábrica prontas; a ordem depende do Fundador.
- 20/10/2026: tamanho do resumo por tópico decidido por delegação do Fundador: 150 a 250 palavras (faixa dos 40 resumos do v1.12). Pendências que seguem com o Fundador: motor v0 (se existir no GPT); capacidade de download já está declarada na plataforma publicada.
