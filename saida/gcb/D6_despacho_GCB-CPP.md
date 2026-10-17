# DESPACHO 11 — LOTE D6 (LAI e LGPD) — v1 — AGORA (15/10/2026; rito ajustado em 17/10/2026)
Origem: D-ESCOPO-3 (Fundador, 15/10/2026), D-DA-LOTES, D-D6-K e D-CEGO-2, transmitidos pela Presidência. Módulo "Noções de Direito Administrativo e Administração Pública" (P1-DA-1 a P1-DA-12; edital/DA_itens_1_12_P1.md) assumido pela GCB; o D6 é o primeiro lote (lotes/loteD6/DESPACHO.md; tarefa T-72).
Executor: agente gcb-cpp. QA normativo prévio: agente qa-normativo-da (.claude/agents/qa-normativo-da.md). QA de mérito: não nesta fase (seção 3).

## 1. O que produzir
O Lote D6 v1, EXCLUSIVAMENTE conforme "saida/gcb/D6_ficha_teste_cego.md" e os anexos listados na seção 9 da ficha. Por isso:
- não usar como fonte de conteúdo nenhum outro arquivo do Projeto (lotes, cursos, pacotes, banco), além dos anexos da ficha;
- não registrar no texto produtor, modelo, ferramenta, agente nem destino da revisão (cabeçalho neutro, seção 2 da ficha);
- dúvida de conteúdo se resolve pela ficha; se a ficha não resolver, registrar a dúvida no bloco à GCB, sem consulta a terceiros.

## 2. Sequência e prazos
1. Primeiro, o qa-normativo-da grava "saida/gcb/D6_anexo_N_mapa_normativo.md" (seção 5). Sem o Anexo N gravado, a gcb-cpp NÃO inicia o D6 (nem curso nem itens).
2. Insumos: nenhum insumo externo é usado na v1 (D-D6-K). O arquivo "Insumo_ChatGPT_LGPD_K005.md" não é lido nem usado, ainda que esteja no Projeto ou em saida/insumos/; pode voltar como insumo na v2, se o parecer pedir.
3. Depois do Anexo N, a gcb-cpp grava a v1 em "saida/gcb/D6_v1.md", terminando em "FIM DO LOTE D6". Prazo: 18/10/2026 (ou o ciclo em que a T-72 rodar).
4. Responder à GCB em bloco curto: arquivo salvo; contagens (C/E, [TS], REVERIFICAR, VOLÁTIL por lei); dispositivos que faltaram no Anexo N.
5. A gcb-gerencia faz só a reconciliação de forma (cabeçalho neutro, ordem das seções da ficha, numeração D6-01 a D6-50, contagens, "FIM DO LOTE D6"), sem QA de mérito.

## 3. Exceção ao fluxo habitual
A gcb-cqfp NÃO avalia o D6 v1. O QA comparativo é feito fora da fábrica, pelo Fundador. A fábrica não grava, não comenta e não infere a origem de nenhuma versão do D6.

## 4. Depois do parecer (sem ação agora)
A GCB indica a base da v2 a partir do parecer. A v2 é feita pela gcb-cpp, com resposta item a item ao parecer (acatado / não acatado + motivo), seguida de R2 da gcb-cqfp, normalmente, e reconciliação da GCB. Meta do canônico: 22/10/2026.

## 5. QA normativo prévio (agente qa-normativo-da, já instalado)
Agente: .claude/agents/qa-normativo-da.md (superior: GCB; modelo distinto do produtor gcb-cpp). Missão: conferir, antes de cada lote do módulo, o texto vigente das normas no texto compilado do Planalto, com granularidade de artigo, inciso, parágrafo e alínea, e entregar o mapa normativo do lote. Não produz curso nem itens; não revisa produção; não lê nem comenta nenhuma versão do Lote D6.
- Método (PADRÃO ÚNICO, seção 4): abrir a URL oficial do texto compilado; transcrever cada dispositivo; anotar "redação dada por" e "incluído por" quando houver; registrar a data. Se a página não abrir ou o texto vier corrompido, declarar "não aberta" ou "texto corrompido" e listar o dispositivo como NÃO CONFERIDO; nunca preencher de memória nem com fonte secundária.
- Marcar REVERIFICAR todo dispositivo com redação dada por lei de 2025 ou 2026.
- Edital 13.33: vale a norma vigente em 2/10/2026; registrar alteração posterior a essa data, se houver, sem incorporá-la.
- Formato do mapa: tabela por artigo (dispositivo; texto; redação dada por; vigência; data da consulta; observação), seguida da lista das leis que alteraram cada norma.
- TAREFA DO D6: "saida/gcb/D6_anexo_N_mapa_normativo.md".
  · LAI (Lei 12.527/2011): texto integral vigente.
  · LGPD (Lei 13.709/2018, compilada com a Lei 15.352/2026): texto integral vigente. O que já foi conferido em 8/10 e 10/10/2026 deve ser reconfirmado com a data nova.
  · Entrega: o arquivo e um bloco curto à GCB (dispositivos NÃO CONFERIDOS, se houver).

Ajuste D-CEGO-2 (GCB, 17/10/2026): título e origem reescritos sem citar a decisão revogada nem a origem das versões; saída da produção passa a ser saida/gcb/D6_v1.md; ordem fixada (Anexo N do qa-normativo-da primeiro; sem ele a gcb-cpp não inicia); insumo externo vedado na v1 (D-D6-K); gcb-cqfp não avalia a v1 (QA comparativo fora da fábrica, pelo Fundador); retirados os nomes neutros de arquivos de comparação e a menção a outro produtor; seção 5 reduzida à remissão ao agente já instalado, com a tarefa do D6 mantida; acrescentada a reconciliação de forma pela gcb-gerencia; caminhos GCB/ trocados por saida/gcb/.
