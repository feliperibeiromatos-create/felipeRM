[Passagem de bastão · v15 · 18/10/2026 · enviada pelo Felipe a partir de outra sessão do Claude]

Construí a v15 (Etapa 2 do PLANO_v15_quatro_abas_2026-10-18.md) em outra sessão, em cima da prévia v14. A partir de agora a produção continua aqui e na Fábrica. Vou ficar cerca de 2 horas fora.

PRÉVIA v15 (privada, separada): https://claude.ai/artifact/KyVNQZCzQzLbuuv4KXwibU
Leia com a ferramenta Artifact (action "read"); o arquivo completo vem junto. A plataforma da candidata e a prévia v14 não foram tocadas.

O QUE A v15 JÁ TEM
- Abas Painel, Resumo, Erros, Recomendações; tela de apresentação antes do concurso (usuária antiga vê uma vez).
- Painel com as 9 matérias do edital, "Continuar de onde parou", Prática de prova sempre acessível.
- Curso por tópico (38 tópicos), cortado pelos títulos do edital; quadros Definição / Exemplo parlamentar / Pegadinha; tabelas; quadro-síntese rolável; setas "A → B → C" viram fluxo; pegadinhas do tópico no fim.
- Questões por tópico em blocos de 10 (inéditas, erradas, mais antigas). Nota = 30 respostas mais recentes (+1/−1/0); antes disso "em formação · N de 30".
- Erros por matéria e tópico; 7 resumos nomeados pelo edital; Recomendações A/B/C com "Por quê".
- Sem "lote", códigos, versões nem pares confundíveis na tela. Referências de lote dentro do texto do curso são reescritas só na exibição (limpaRef).
- Chaves c2026.v01.* inalteradas; migração só acrescenta campos (S.resp, S.top, S.v15). Pacote F4 v1.9 idêntico ao da v14.
- Testes: 218/218 (Playwright, 360 px e PC escuro, migração de estado v14). Sem teste em celular real.

DECISÕES PROVISÓRIAS (constantes no código)
CONTA_REPETIDAS=true (repetidas contam, com aviso) · peso = 90 itens da prova ÷ nº de matérias dela · discursiva após ler 50% dos cursos de P2 (LIM_DISC) · simulado após praticar 60% dos tópicos, 1 a cada 7 dias (LIM_SIM, DIAS_SIM) · curso "lido" após 30 s no fim ou ao tocar Praticar/Próximo · voláteis entram no bloco depois das inéditas · itens 2, 4 e 5 de TI como "Visão geral do item N".

PEDIDOS PARA ESTA SESSÃO
1. Salvar no Projeto: claude/REGISTRO_v15_previa_2026-10-18.md (este texto) e atualizar o PLANO_v15 marcando a Etapa 2 como construída em prévia.
2. Revisar a v15 com a skill design-plataformas-interativas e corrigir na própria prévia (mesma URL), sem publicar na plataforma da candidata.
3. Gravar a encomenda da Fábrica (lista abaixo) onde a Fábrica lê as ordens, e disparar o que puder sem autorização minha.
4. Não publicar na plataforma da candidata nem a v14 nem a v15. Isso continua dependendo do meu "sim".

ENCOMENDA PARA A FÁBRICA
a) Resumo por tópico (pacote.topicos["P2-1.4"].resumo), começando pelos tópicos de maior peso.
b) Converter os pares confundíveis em pegadinhas ("não confunda A com B") com itemEdital.
c) Tirar do texto do curso, do resumo e das justificativas as referências de produção (Lote N, neste lote, códigos como 6A-02).
d) Reclassificar L2-R16 (provável 2.8 → 3.1).
e) Piloto de curso visual em 2 ou 3 tópicos (sugestão: dois de Fala e um de TI) no formato:
   "topicos": {"P2-1.4": {"emUmMinuto":[...], "resumo":"...", "visuais":[{"tipo":"fluxo"|"tabela"|"linha"|"esquema"|"barras", ...}]}}
   (fluxo: titulo, passos[]; tabela: titulo, colunas[], linhas[[]], legenda; linha: titulo, marcos[{quando,texto}]; esquema: titulo, centro, ramos[]; barras: titulo, dados[{rotulo,valor}], unidade, fonte). O 1.4 já tem uma demonstração no código (TOPICOS_DEMO), feita só com frases do curso e do resumo.
f) Banco: meta de questões por tópico (20 hoje × 40 para a nota com questões distintas). Fica para minha decisão.

PENDENTE COMIGO (não decidir por mim)
Qual endereço a candidata usa · repetidas contam ou não · motor v0 (se existir no GPT) · confirmação do piloto · "Exportar meus erros" pede a capacidade de download, que não está declarada nas prévias v14 e v15 (sem ela o texto vai para a área de transferência).

---
[Decisões do Fundador · 18/10/2026, noite · enviadas a partir de outra sessão do Claude]

1. Endereço: a candidata usa a "Plataforma Câmara 2026" (https://claude.ai/artifact/5fyXGpFMomSHwZuRnu36rC). A versão final vai para lá, só com o "sim, publicar v15" do Fundador.
2. Nota de 30 por tópico: só questões distintas. Aplicado na prévia v15.2 (mesma URL, versão 1792360787-b29b): CONTA_REPETIDAS=false; textos da apresentação, da legenda da matéria e do resultado do bloco ajustados (o resultado diz quantas questões faltam e quantas o banco do tópico tem). Hoje nenhum tópico chega à nota (máximo 26).
3. Piloto de curso visual confirmado: 3 tópicos, dois de Fala e um de TI. Sugestão enviada: P2-1.4, P2-2.5 e P1-8.2.
4. Meta do banco: 40 questões distintas por tópico nas duas matérias da plataforma (nova ORDEM_V15_F_BANCO40). A meta de 20 por item-folha nas demais matérias continua. Prazo não definido; a Fábrica fará uma projeção.
5. Fábrica: o Fundador cola as ordens (C, D, B, A, E, F) direto na sessão da Fábrica no Claude Code.

Situação dos pendentes listados acima: endereço, repetidas e piloto RESOLVIDOS. Seguem com o Fundador: motor v0 (se existir no GPT), tamanho do resumo por tópico, capacidade de download para "Exportar meus erros".
Publicação na plataforma da candidata continua dependendo do "sim, publicar v15".

---
[Publicação · 18/10/2026, 19h52 · aviso do Fundador enviado a partir de outra sessão do Claude; conferido por esta sessão]

A v15.2 foi publicada na plataforma da candidata, "Plataforma Câmara 2026" (https://claude.ai/artifact/5fyXGpFMomSHwZuRnu36rC), com o "sim, publicar a v15.2" do Fundador.
- Base: prévia v15.1 + mudanças da v15.2 (CONTA_REPETIDAS=false e textos da regra nova), mais a frase do resultado do bloco corrigida ("refazer uma questão troca a resposta antiga dela").
- Título "Plataforma Câmara 2026"; meta "v15.2 · publicada em 18/10/2026".
- Capacidade de download mantida (vinha da v13): "Exportar meus erros" salva arquivo.
- Regressão relatada pela sessão que publicou: 218/218; leitura de volta idêntica ao enviado; abre e mostra "A plataforma mudou de forma". Cópia da v13 guardada para reverter.

Conferência desta sessão (leitura da versão publicada 1792363883-b584): título e meta como acima; capacidade `downloads` declarada; pacote embutido idêntico ao da prévia v15.2 (F4 v1.9, 334 itens); código igual ao da prévia v15.2, exceto título, meta e a frase do resultado do bloco. Não conferi a igualdade com a v13 (não tenho a cópia dela nesta sessão).

A prévia https://claude.ai/artifact/KyVNQZCzQzLbuuv4KXwibU continua como laboratório.
Toda publicação nova na plataforma da candidata continua dependendo do "sim" do Fundador.
