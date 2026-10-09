GCB-CQFP → GCB | 08/10/2026 | PARECER DE QA — LOTE 4-C v1 (complemento do 5.1; não reabre a v3.x) — RODADA 1 de no máximo 2
Retorno pela hipótese A. A CPP sucessora entregou direto à CQFP, com a GCB em cópia. Base: GCB/Lote4C_v1_GCB-CPP.md, que termina em "FIM DO LOTE 4-C" (íntegro).

1. CHECAGENS FORMAIS — CONFEREM
- 10 itens: 5 C (02, 03, 06, 07, 09) e 5 E;
- 5 [TS] (01, 03, 04, 06, 08), sendo 2 C e 3 E;
- 0 VOLÁTIL;
- rótulo AUTORAL em todos; nenhum item atribui afirmação a autor ou fornecedor;
- nenhuma afirmação além do curso 5.1 / 5.3.3 do Lote 4.
As fontes F1–F3 não foram reabertas. Os trechos usados (few-shot, temperatura, fatores do resultado, zero/one/few-shot) já tinham sido conferidos pela CQFP em 07/10/2026.

2. ITEM A ITEM
4C-01 E [TS] — OK. Troca contexto × exemplos (curso 5.1.2, itens 3 e 4). Não repete o item 2 do Lote 4.
4C-02 C — OK. Fiel ao F3: "generally produces more desirable results than zero-shot prompting and one-shot prompting" / "requires a lengthier prompt". O ponto julgado (efeito e custo) é distinto do item 2.
4C-03 C [TS] — OK. Fiel ao F3 (o resultado depende também do conjunto de treino e da temperatura e demais parâmetros de decodificação). A marca [TS] é fraca, mas aceitável.
4C-04 E [TS] — OK. Inverte as definições de temperatura e de janela de contexto. Distinto do item 4 do Lote 4.
4C-05 E — OK. "Elimina" e "dispensável a conferência humana" são generalização indevida (curso 5.1.4; P5; 6.2, princípio 7).
4C-06 C [TS] — RESSALVA OBRIGATÓRIA (O-4C1). Ver item 3.
4C-07 C — OK. Conceito geral de iteração e avaliação (curso 5.1.1 e 5.1.3).
4C-08 E [TS] — OK; robustez CONFIRMADA.
  O E não depende da fronteira entre injeção e jailbreak: o curso define a injeção como instruções embutidas em textos que o modelo lê, e o item nega exatamente isso ("não abrangendo"). Mesmo um examinador que trate o ataque digitado pelo usuário como forma de injeção mantém o E, porque o erro está em "restringe-se" e "não abrangendo".
4C-09 C — OK, com recomendação (R-4C1). Ver item 4.
4C-10 E — OK. No exemplo do curso 5.1.5, a determinação aparece sob [Restrições]. O formato de saída trata da forma da resposta (5.1.2, item 5). Risco baixo.

3. CORREÇÃO OBRIGATÓRIA
O-4C1 — 4C-06 repete o ponto de julgamento do item 2 do Lote 4.
- O item 2 julga "um único exemplo = one-shot, e não few-shot" (gabarito E); o 4C-06 julga a mesma coisa com polaridade invertida (gabarito C). Quem acerta o item 2 acerta o 4C-06 sem usar o detalhe do "par entrada-saída".
- O detalhe que a CPP quis testar (um par entrada-saída conta como um exemplo) é fino demais para distinguir os dois itens.
- Substituir por item de zero-shot, mantendo gabarito C e [TS]:
  "Um prompt composto apenas por uma instrução detalhada, que descreve inclusive o formato desejado da resposta, mas que não traz nenhuma demonstração de entrada e saída, caracteriza a técnica zero-shot, ainda que a instrução seja extensa."
- Tentação: tomar a instrução longa ou a descrição do formato por "exemplo" e concluir que é one-shot (marcar E).
- Fundamento: F3, zero-shot: "A prompt that does not provide an example of how you want the large language model to respond" (conferido pela CQFP em 07/10/2026); curso 5.1.2 (itens 4 e 5: exemplos ≠ formato) e 5.1.3.
- O ponto é distinto dos itens 1 a 6, 15 e 16.
- As contagens se mantêm: 5 C e 5 E; [TS] com 2 C e 3 E.

4. RECOMENDADA (não condiciona a aprovação)
R-4C1 — 4C-09.
- A primeira oração ("sem ferramentas de busca ou RAG, o modelo responde com o que incorporou no treinamento") é o mesmo conhecimento do item 15, com polaridade invertida.
- Para concentrar o julgamento na aplicação (o material entra como contexto do prompt), sugiro:
  "Para que um modelo de linguagem, sem acesso a busca ou a RAG, resuma um relatório interno elaborado depois do seu treinamento, o texto do relatório deve ser incluído no prompt, como contexto."
- Gabarito C, sem [TS]. Fundamento: curso 5.1.2 (item 3) e 5.3.3.

5. OBSERVAÇÃO SOBRE O CURSO (fora do escopo: o 4-C não reabre a v3.x) — BACKLOG
- O par C19 do Lote 4 (injeção = embutida; jailbreak = tentativa direta do usuário) pode ser lido como se os dois fossem mutuamente exclusivos.
- Há literatura que distingue injeção direta (digitada pelo usuário) de injeção indireta (embutida em conteúdo).
- Se a GCB quiser ajustar o par, isso exige fonte oficial datada, que não foi aberta neste parecer.
- O 4C-08 não é afetado (item 2).

6. CONCLUSÃO — RODADA 1: APROVADO COM RESSALVAS
Condição: aplicar O-4C1. R-4C1 fica a critério da GCB.
Proposta de rito: a CPP aplica, e a CQFP faz conferência de aplicação restrita ao 4C-06 (e ao 4C-09, se a R-4C1 for adotada), sem que isso conte como rodada 2. A decisão é da GCB.

Classificação: O-4C1 AGORA; R-4C1 PRÓXIMO; observação C19 BACKLOG.
FIM DA ENTREGA

==========================================================================
CONFERÊNCIA DE APLICAÇÃO | GCB-CQFP → GCB | 08/10/2026 | LOTE 4-C v1.1 (Despacho 6) — não conta como rodada 2
Base: GCB/Lote4C_v1_GCB-CPP.md com o cabeçalho "v1.1 — Despacho 6 da GCB (rodada 1 da CQFP), 08/10/2026", íntegro (termina em "FIM DO LOTE 4-C").

- 4C-06 — CONFERE. O texto é idêntico ao de O-4C1. Gabarito C, [TS], mecanismo AT. O d-G traz a tentação, o fundamento (F3 zero-shot, com a citação literal; curso 5.1.2, itens 4 e 5; 5.1.3) e a diferença em relação ao item 2 do Lote 4.
- 4C-09 — CONFERE. O texto é idêntico ao do Despacho 6 (R-4C1 com "e sem retreinamento"). Gabarito C, sem [TS]. O d-G fundamenta no curso 5.1.2, 5.1.3 e 5.3.3 e diz em que o item difere dos itens 6 e 15 do Lote 4.
- Tabela de Correções: duas linhas (O-4C1 e R-4C1), status "aplicada (v1.1)" — CONFERE.
- Contagens: 5 C (02, 03, 06, 07, 09) e 5 E; 5 [TS] (01, 03, 04, 06, 08 — 2 C e 3 E); 0 VOLÁTIL — CONFEREM.
- Demais itens: sem alteração.

Registro, sem ação: a sugestão de alinhar "sem acesso a busca" a "sem acesso a ferramentas externas (como a busca)", feita após o Despacho 6, não foi incorporada. Como já dito, o item se sustenta na redação do Despacho 6. A sugestão fica BACKLOG, a critério da GCB. (Superado: ver Conferência da Retificação 6-A, abaixo.)

RESULTADO: LOTE 4-C v1.1 — CONFERIDO. Pronto para a reconciliação.
Classificação: Lote 4-C v1.1 AGORA (para a reconciliação); alinhamento "ferramentas externas" BACKLOG.
FIM DA CONFERÊNCIA DE APLICAÇÃO

==========================================================================
CONFERÊNCIA DA RETIFICAÇÃO 6-A | GCB-CQFP → GCB | 08/10/2026 | LOTE 4-C v1.1 — 4C-09 — não conta como rodada
Base: GCB/Lote4C_v1_GCB-CPP.md (v1.1 com a Retificação 6-A), íntegro (termina em "FIM DO LOTE 4-C").

- 4C-09 (versão do estudante) — CONFERE. O texto é: "Para que um modelo de linguagem, sem acesso a ferramentas externas (como a busca) ou a RAG e sem retreinamento, resuma um relatório interno elaborado depois do seu treinamento, o texto do relatório deve ser incluído no prompt, como contexto." Coincide com a sugestão da CQFP. Gabarito C, sem [TS].
- d-G do 4C-09 — CONFERE. Registra a 6-A e o motivo ("sem acesso a busca" não excluía outras ferramentas), com alinhamento ao curso 5.3.3 ("sem ferramentas ou RAG").
- Tabela de Correções, linha R-4C1 — CONFERE. Registra a 6-A, com status "aplicada (v1.1; 6-A)".
- Contagens: 5 C e 5 E; 5 [TS] (2 C e 3 E); 0 VOLÁTIL — CONFEREM.
- Demais itens: sem alteração em relação à v1.1 já conferida.
- Observação de forma, sem ação: o cabeçalho de versão não menciona a 6-A. O registro na Tabela de Correções basta.

RESULTADO: LOTE 4-C v1.1 (com 6-A) — CONFERIDO. Pronto para a reconciliação. O BACKLOG "ferramentas externas" está encerrado (aplicado).
FIM DA CONFERÊNCIA DA RETIFICAÇÃO 6-A
