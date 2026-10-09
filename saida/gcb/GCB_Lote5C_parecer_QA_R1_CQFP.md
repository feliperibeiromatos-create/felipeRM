GCB-CQFP → GCB | 08/10/2026 | PARECER DE QA — LOTE 5-C v1 (complemento do 8.2 e do 8.4; não reabre a v3.x) — RODADA 1 de no máximo 2
Retorno pela hipótese A. A CPP sucessora entregou direto à CQFP, com a GCB em cópia. Base: GCB/Lote5C_v1_GCB-CPP.md, que termina em "FIM DO LOTE 5-C" (íntegro), conferido contra GCB/Lote5_v3_canonica_GCB-CPP.md (v3.1): curso 8.2 e 8.4, resumo 8.1, 8.2 e 8.4, pares C1–C3, C14 e C15, e itens A5-08 a A5-13 e A5-18 a A5-20.

1. CHECAGENS FORMAIS — CONFEREM
- 10 itens: 5 C (01, 04, 05, 06, 09) e 5 E (02, 03, 07, 08, 10).
- 5 [TS] (01, 03, 06, 07, 08): 2 C e 3 E.
- 0 VOLÁTIL.
- Distribuição: 8.2 = 6 itens (histograma 01; linha 02; barras 03 e 04; dispersão 05; box plot 06); 8.4 = 4 itens.
- Rótulo AUTORAL em todos.
- Nenhum item cita autor: o 5C-06 não nomeia Tukey.
- Nenhum item menciona ferramenta ou produto.
- Nenhuma afirmação vai além do curso. Não foi necessária fonte externa.

2. ITEM A ITEM
5C-01 C [TS] — OK. Fiel ao curso 8.2 ("o número de classes altera a aparência"); "pode alterar" é até mais cauteloso que o curso. A marca [TS] é fraca (a tentação "mesmos dados, mesmo gráfico" pouco seduz), mas é aceitável, como no 4C-03. Ponto de julgamento distinto de A5-08 (altura × área) e de A5-09 (contiguidade).
5C-02 E — OK. Fiel ao curso 8.2 ("com cuidado com o número de linhas"). O "não exige qualquer cuidado" e o "facilitam" sustentam o E. É distinto de A5-10.
5C-03 E [TS] — OK quanto ao gabarito; recomendação R-5C1 (item 4). O item inverte agrupado (subcategorias lado a lado) e empilhado (partes de um total), conforme o curso 8.2 e a pegadinha ali registrada. O E é robusto. Porém a expressão "lado a lado", aplicada às barras empilhadas, denuncia a troca para quem só conhece o sentido literal de "empilhado", e isso enfraquece o [TS]. É distinto de A5-09 e do par C1.
5C-04 C — OK. "Preferível" equivale ao "melhor" do curso 8.2, e o item não proíbe a disposição vertical.
5C-05 C — OK. Fiel ao curso 8.2. O item não diz "somente", então outra codificação (por exemplo, a cor) não o torna errado. É distinto de A5-11.
5C-06 C [TS] — OK; regra de bigodes CONFIRMADA.
  - Conferência lógica. Limites: Q1 − 1,5·AIQ e Q3 + 1,5·AIQ. Cada bigode vai até o dado mais extremo do seu lado que esteja dentro do limite. Se o mínimo for ≥ Q1 − 1,5·AIQ, o bigode inferior termina no mínimo, haja ou não outlier superior. O item é exatamente isso, e a cláusula "desde que esse valor esteja dentro do limite inferior" fecha o caso.
  - Lição O10: "segundo a regra usual" amarra o julgamento à convenção do curso. Assim, convenções alternativas (bigodes do mínimo ao máximo, bigodes por percentis) não derrubam o C.
  - Risco residual baixo: alguns materiais desenham o bigode até o próprio limite, e não até o dado. Mesmo nesse caso, o item fala do caso em que o mínimo está dentro do limite; o curso adota a regra do dado mais extremo.
  - "A partir de Q1 e de Q3" é aceitável como descrição dos limites, porque a direção (para baixo a partir de Q1, para cima a partir de Q3) é a da regra.
  - Ponto de julgamento distinto de A5-12 e A5-13. O par C3 registra "os bigodes vão sempre ao mínimo e ao máximo" como troca da banca; o 5C-06 testa a regra por lado, que é outro ângulo.
5C-07 E [TS] — OK. Inverte storytelling e dashboard (curso 8.4; par C14). O E é robusto: o storytelling não se caracteriza por exploração aberta, qualquer que seja a leitura de "dashboard". O mecanismo (inversão de par) é o mesmo de A5-19, mas o par é outro (C14, não C15), e o ponto de julgamento é distinto.
5C-08 E [TS] — OK; risco baixo. O curso 8.4 (dirigir a atenção: "título que afirma a conclusão") e o resumo 8.1 ("título afirmativo") sustentam o E, e o item se restringe ao caso explanatório. Risco de recurso a registrar: normas de apresentação de tabelas e gráficos em documentos técnicos prescrevem títulos descritivos (o quê, onde, quando). O recorte "apresentação ... que visa conduzir o público" afasta esse argumento. Proximidade com A5-20: é o mesmo princípio (dirigir a atenção) com outro instrumento (título × cor e anotações). Não é repetição do ponto de julgamento.
5C-09 C — OK. Reproduz o curso 8.4 (estrutura narrativa) termo a termo (O12). É distinto de A5-18 (tríade).
5C-10 E — OK. Inverte a ordem do método do curso 8.4 ("definir a mensagem principal antes de escolher gráficos"). É distinto de A5-19.

3. CORREÇÕES OBRIGATÓRIAS
Nenhuma.

4. RECOMENDADA (não condiciona a aprovação)
R-5C1 — 5C-03: retirar "lado a lado" da segunda oração, para preservar a sutileza.
  Redação sugerida: "O gráfico de barras agrupadas é o indicado para mostrar as partes que compõem um total, ao passo que o de barras empilhadas é o indicado para comparar as subcategorias entre si."
  Gabarito E e [TS] mantidos. As contagens não mudam.

5. OBSERVAÇÃO SOBRE OS PEDIDOS DA CPP
- Fidelidade ao curso: confere em todos os itens.
- Não repetição de A5-08 a A5-13 e A5-18 a A5-20: confere. As diferenças declaradas no d-G estão corretas.
- Regra de bigodes do 5C-06: confere (item 2).

6. CONCLUSÃO — RODADA 1: APROVADO
R-5C1 fica a critério da GCB. Proposta de rito: se a R-5C1 for adotada, a CPP aplica e a CQFP faz conferência de aplicação restrita ao 5C-03, sem que isso conte como rodada 2. A decisão é da GCB.

Classificação: Lote 5-C APROVADO (AGORA, para a reconciliação); R-5C1 PRÓXIMO (decisão D1 da GCB); risco de recurso do 5C-08 registrado, sem ação (BACKLOG).
FIM DA ENTREGA

==========================================================================
CONFERÊNCIA DE APLICAÇÃO | GCB-CQFP → GCB | 08/10/2026 | LOTE 5-C v1.1 (Despacho 8, R-5C1) — não conta como rodada 2
Base: GCB/Lote5C_v1_GCB-CPP.md com o cabeçalho "v1.1 — Despacho 8 da GCB (rodada 1 da CQFP), 08/10/2026", íntegro (termina em "FIM DO LOTE 5-C"). Conferido diretamente no Projeto, sem aguardar o bloco conjunto da CPP: o arquivo já está na redação final.

- 5C-03 (versão do estudante) — CONFERE. O texto é idêntico ao da R-5C1 e do Despacho 8. Gabarito E, [TS] mantida.
- d-G do 5C-03 — CONFERE. Registra a redação da v1.1 e o motivo. O "lado a lado" que permanece no d-G descreve o curso (agrupado = subcategorias lado a lado), e não a redação do item: correto.
- Tabela de Correções, linha R-5C1, status "aplicada (v1.1)" — CONFERE.
- Contagens: 5 C e 5 E; 5 [TS] (2 C e 3 E); 0 VOLÁTIL; 8.2 = 6, 8.4 = 4 — CONFEREM.
- Demais itens: sem alteração em relação à v1.

RESULTADO: LOTE 5-C v1.1 — CONFERIDO. Pronto para a reconciliação.
FIM DA CONFERÊNCIA DE APLICAÇÃO
