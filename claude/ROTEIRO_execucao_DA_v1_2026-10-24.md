# Roteiro de execução — melhorias de Direito Administrativo e novas questões (v1, 24/10/2026)

Sessão Cowork (análise do dossiê), a pedido do Fundador: "qual a melhor maneira de implementar as últimas mudanças, incluindo as melhorias do curso de DA e a incorporação das novas questões". Base: Dossiê DAD v1; PLANO_implementacao_Dossie_DAD_v1; ESPEC v2; ESTILO_banca_DA_Cebraspe2025_v1; kit_fabrica_v2 (24/10). Escrito ANTES da resposta da Presidência_v2; a seção 6 diz o que muda conforme ela.

## 1. Resposta curta
O kit_fabrica_v2 já contém quase tudo (ESPEC v2, checa_pacote_v2.py, agente de QA didático, quatro ordens, fila de 1.321 candidatos). A melhor maneira é executá-lo na Fábrica em duas trilhas paralelas e uma sequencial, com três correções antes de começar:

1. Trilha BANCO (independente de conteúdo): ORDEM_CD2026_LOCALIZAR → ORDEM_BANCO_DA_CDN_ONDA1 (15 provas, ~415 candidatos) → ondas 2+ ("sim" por onda). Entrega itens reais que alimentam os itens intercalados e as verificações.
2. Trilha QA (uma sessão): ORDEM_DA_QA12 sobre os lotes D1–D6. Pré-condição da fase 1 de conteúdo.
3. Trilha CONTEÚDO (depois da QA12): ORDEM_DA_V2_FASE1 (itens 2, 3.4, 4.4) → fases 2–4.
4. Trilha PLATAFORMA (sessão de design, em paralelo): v17 lendo os campos da ESPEC v2 e, com o adendo v2.1, o campo `mecanismo`.

Correções antes de começar (todas pequenas): (a) resolver o conflito "metade caso" (ESPEC v2 §7) × "caso em 5–10%" (ESTILO §6.4) adotando o corpus — adendo v2.1 neste kit; (b) acrescentar `mecanismo` aos itens DA-v2 e o checa_estilo_DA.py ao fluxo de entrega; (c) na onda 1 do banco, trocar a prova SEFAZ RJ AFP (0 C/E) por outra com C/E. Sem (a), a fase 1 produz itens no formato errado e será refeita.

## 2. Ordem de execução e dependências

| Passo | O quê | Onde | Depende de | Produz |
|---|---|---|---|---|
| 0 | Commit do kit_fabrica_v2 + adendo v2.1 + checa_estilo_DA.py; linhas em TAREFAS.md e DECISOES.md (D-DOSSIE-DAD, D-ESPEC-DA-V2, D-DA-ORDEM, D-BANCO-LOCALIZADOR) | repositório felipeRM (LEIA-ME_commit.md do kit) | "sim" do Fundador às decisões 1–3 do plano | Fábrica com ordens e regras |
| 1 | ORDEM_DA_QA12 | Fábrica, orquestrador LOTE, qa-normativo-da | passo 0 | QA12_DA_<data>.md; erratas |
| 2 | ORDEM_CD2026_LOCALIZAR | Fábrica, orquestrador BANCO, gbq-cfp + QA Opus | passo 0 (pode rodar antes do 1 se a trava permitir sessões consecutivas) | itens CEBRASPE_OFICIAL do órgão-alvo no banco |
| 3 | ORDEM_BANCO_DA_CDN_ONDA1 (com a troca da SEFAZ RJ) | Fábrica, BANCO | passo 2 | ~ itens reais 2025 em 10, 7, 11, 1.2, 2.1, 4.4 (meta ≥ 30 reais nos cinco maiores) |
| 4 | ORDEM_DA_V2_FASE1 com o adendo v2.1 | Fábrica, LOTE, gcb-cpp + qa-normativo-da + gcb-cqfp-didatico | passos 1 e 3 (ou 1 só, com AUTORAL e pontos de troca registrados) | pacote novo com itens 2, 3.4, 4.4 em DA-v2 |
| 5 | v17 na prévia lendo `tarefas`, `GLOSSÁRIO`, `CASO`, `RESPOSTA DO CASO`, `ITEM`, `comentario`, `fechamento`, `escopo`, `par`, `mecanismo`; regressão R3 estendida | sessão de design (não a Fábrica) | ordem da v17 emendada (decisão 2 do plano) | prévia que renderiza o DA-v2 |
| 6 | Gatilho A da fase 1; "sim" do Fundador; publicação na v17 | GCB → Presidência → Fundador | passos 4 e 5 | módulo de DA v2 para a candidata (D-AUDITORIA-20OUT) |
| 7 | Fases 2–4 da DA_V2 e ondas 2+ do banco | Fábrica | "sim" por fase/onda (gasto) | cobertura das lacunas (2.2, 3.3, 4.1, 8, 9, 10.4–10.7) e itens reais no restante |

Regra de ritmo: uma ordem por sessão, sessões consecutivas (SESSAO_EM_CURSO.lock, D-RITMO-MAX). Com isso, os passos 1–4 são quatro sessões; a trilha de plataforma (5) corre em paralelo em sessão própria.

## 3. Incorporação das novas questões (1.321 candidatos TEC 2025)
- O que são: localizadores, não fonte (D-BANCO-LOCALIZADOR). Só 25 gabaritos foram confrontados com o definitivo oficial; os demais entram no banco apenas quando localizados no caderno oficial do CDN, com gabarito definitivo e número do item.
- Onda 1 (15 provas, ~415 candidatos; meta ≥ 30 reais em 10, 7, 3.4/4, 4.4 e 1.2). Distribuição esperada por item do edital, segundo resumo_por_item_edital_v2.csv: 10.1 136 C/E, 7 75, 11 67, 1.2 62, 2.1 59, 10.2 57, 4.4 47, 10.4 40, 3.4 36 — e 257 "sem enquadramento/duvidoso" que vão para reserva salvo justificativa do QA. Sem candidato real para 2.2, 4.1, 8.1, 8.4, 9.4 e 12 (LGPD está em outro caderno do TEC): esses continuam AUTORAL 30 por folha (D-LACUNAS).
- Eficiência: a localização é trabalho determinístico (resolver pasta do concurso no CDN → baixar caderno e gabarito definitivo → pdftotext → casar o texto normalizado → ler número e gabarito). Recomenda-se que o gbq-cfp escreva um `localiza_cdn.py` na primeira prova e o reutilize nas demais, deixando ao agente só a tabela prova → pasta do CDN, o enquadramento no edital e o QA. Isso reduz custo e erro de transcrição; o texto do banco sai do PDF oficial, nunca da fila.
- Mecanismo: cada item real recebe `mecanismo` (reclassificado por agente de modelo distinto em amostra de 100, ESTILO §7); é esse campo que a plataforma usa para o painel e o treino por mecanismo (adendo v2.1, seção 5).
- Temporal: provas de 2025 marcadas VOLÁTIL-NORMATIVO quando o gabarito depender de norma alterada (LGPD/ANPD; 14.133; 8.112), reverificação 4–8/1/2027 (T-120).

## 4. Implementação do ESTILO da banca na plataforma
Três camadas, na ordem de custo:
1. Produção (custo zero de plataforma): regras do ESTILO §6 entram na ESPEC via adendo v2.1 e no PADRAO_UNICO v1.1; `checa_estilo_DA.py` roda antes de cada entrega; QA didático confere a linha 11.
2. Dados (um campo): `itens[].mecanismo` em AUTORAL e reais; `comentario.decisiva` começa pelo código. Compatível com a plataforma atual (campo ignorado até a v17).
3. Tela (v17): chip do mecanismo no feedback; painel erros por mecanismo × item do edital; diagnóstico de 30 composto por mecanismo; depois, treino por mecanismo e a tela "Como a Cebraspe constrói o item" (estatística própria, sem texto de terceiro); revisão espaçada priorizando os pares do mecanismo mais errado.

## 5. O que NÃO fazer
- Não rodar a FASE1 com a ESPEC v2 sem o adendo v2.1 (refação certa).
- Não criar coordenação nova de reescrita (plano, decisão 3): a Fábrica tem os agentes.
- Não usar o curso analisado, a matriz do ChatGPT nem as fichas do pacote de auditoria como fonte de texto, exemplo, tabela ou item (D-ESTRATEGIA, D-GCE-01, D-BANCO-LOCALIZADOR).
- Não publicar nada antes do gatilho A de cada fase e do "sim" (D-AUDITORIA-20OUT).

## 6. O que depende da resposta da Presidência_v2
| Se a Presidência… | Então |
|---|---|
| Aceita as decisões 1–3 do plano (D-ESTRATEGIA aplicada ao dossiê; campos novos na v17; Fábrica + GCB) | Executar os passos 0–7 como acima; registrar as quatro linhas em DECISOES.md |
| Mantém a ORDEM_DA_FORMATO (19/10) em vez da ORDEM_DA_V2 | Formata-se duas vezes; pedir reconsideração com o argumento do retrabalho (plano, seção 3) |
| Rejeita incorporar os campos novos à v17 (quer v17.1 depois) | Produzir a fase 1 mesmo assim (os campos são ignorados pela plataforma atual) e publicar quando a v17.1 ler; custo: a QA didática confere na prévia só mais tarde |
| Pede QA12 antes de qualquer gasto novo | Rodar só o passo 1; os passos 2–3 não dependem dele e podem esperar o "sim" |
| Não se pronuncia sobre o conflito "metade caso" | Levar o adendo v2.1 como decisão D2 (forma de produção) à Presidência e ao Fundador antes do passo 4 |
| Altera a ordem dos tópicos da fase 1 | Manter o critério peso × defeito do dossiê (2, 3.4, 4.4) salvo razão registrada; o volume do corpus 2025 (10.1 136, 7 75, 11 67) sugere que a fase 3 (item 10) seja antecipada se a onda 1 do banco render muitos itens reais |

Pendência desta sessão: ler a resposta da Presidência_v2 quando o Fundador a transportar para cá e fechar a seção 6 em v1.1.
