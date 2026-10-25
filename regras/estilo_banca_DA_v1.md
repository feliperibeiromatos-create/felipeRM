# Estilo da banca — Direito Administrativo, Cebraspe 2025 (v1.1, 25/10/2026)

v1.1: corrigida a frase invertida da seção 4 apontada pela QA R3/R5 da v17.1 ("o item CERTO é quase sempre LITERAL" → "o item LITERAL é quase sempre CERTO"); nada mais mudou.

Sessão Cowork, a pedido do Fundador ("aprender ainda mais a maneira como o Cebraspe faz as questões"). Complementa regras/estilo_banca.md v1.0 (42 itens, 8/10) com um corpus 26 vezes maior. Insumo das CPPs e dos agentes de produção AUTORAL; não é fonte de item.

## 0. O que é este documento e o que não é
Corpus: 1.321 questões Cebraspe de Direito Administrativo, todas de provas de 2025, de 143 provas e 63 órgãos, extraídas de sete cadernos do TEC Concursos (1.118 Certo/Errado; 203 múltipla escolha). As estatísticas abaixo são sobre forma e construção dos itens. Três limites:
1. A compilação é de terceiro (TEC), vedada como fonte de item (D-GCE-01). Aqui ela é usada só para medir padrões; nenhum texto entra em lote. Os itens só viram banco depois de localizados no CDN oficial (fila BANCO-DA).
2. O gabarito usado é o reproduzido pelo TEC. Dos 1.321, 25 foram confrontados com gabarito definitivo oficial pelo pacote de auditoria e 25 bateram; os demais não foram verificados. Tratar as porcentagens como aproximadas (±3 pontos).
3. A classificação por "mecanismo" (seção 4) foi feita por outra IA no pacote de auditoria, depois de ler o gabarito; descreve como o item errado foi construído, não é um preditor lido do texto. As medidas lexicais da seção 2 são desta sessão e usam só o texto do enunciado.

## 1. Equilíbrio e formato
- Certo 49% × Errado 51% (546 × 572). A banca não pende para E em Direito Administrativo. Meta de produção coerente: 40–60% C por lote (D-REFORCO-2 já prevê).
- 85% Certo/Errado; 15% múltipla escolha A–E (concentrada em TCE, MPE, CAU, Embrapa, SUSEP). Para o Cargo 11 só C/E interessa; as ME servem de insumo de pegadinha (cada distrator é uma troca).
- Caso concreto ou situação hipotética: só 5 a 6% dos itens C/E (59 com personagem ou "Considere/Suponha"; 69 com texto-base de mais de 40 palavras antes do "julgue"). O item típico é uma ASSERTIVA de 21 a 35 palavras (55% dos itens; mediana 30), sem narrativa. Isso contraria a intuição de "metade caso" em responsabilidade civil: no corpus, 6.1 tem 0% de caso por regex e 21% de jurisprudência.
- Comprimento não prevê gabarito (mediana 30 palavras tanto em C quanto em E). Os seis itens acima de 80 palavras são 83% E, amostra pequena.

## 2. Palavras-gatilho: o que o texto sozinho entrega (e o que não entrega)
Regra de mercado: "sempre, somente, necessariamente → Errado". No corpus ela é fraca:

| Gatilho no enunciado | Itens | % Errado |
|---|---|---|
| independentemente | 22 | 82% |
| necessariamente / obrigatoriamente | 9 | 67% |
| dispensa / prescinde / não exige | 54 | 63% |
| vedado / proibido / não pode | 66 | 62% |
| ainda que / mesmo que | 29 | 62% |
| somente / apenas / exclusivamente | 65 | 60% |
| sempre | 11 | 55% |
| todo(s) / qualquer | 54 | 52% |
| número ou prazo (dias, anos, %) | 46 | 46% |
| em regra / salvo / exceto / ressalvado | 40 | 43% |
| pode / admite / é cabível | 213 | 43% |
| sem nenhum absolutizador | 1.011 | 50% |

Leitura: 90% dos itens não têm absolutizador; onde há, a chance de E sobe só de 50% para 55–65%. O único gatilho forte é "independentemente" (n pequeno). "Pode/admite/é cabível" inclina levemente para C. Conclusão para a candidata: chute por palavra-chave rende pouco em Direito Administrativo; o que decide é reconhecer a troca (seção 4). Conclusão para a produção: não construir itens AUTORAL em torno de "sempre/somente" — a banca não faz isso; faz a troca de conceito vizinho em frase de aparência neutra.

## 3. Como a banca escreve o comando
- Abertura: "Julgue o item a seguir" direto (27%), "A respeito de…" (13%), "Acerca de…" (10%), "Com base em…" (9%), "No que se refere a…" (8%), "Em relação a…" (7%); as demais ("Considerando", "À luz", "De acordo com", "No que concerne", "Com relação") somam 15%.
- Fechamento: "o item a seguir" (52%), "o item seguinte" (14%), "o item subsequente" (10%), "o próximo item" (8%), "o item que se segue" (8%), "o seguinte item" (4%). Esses seis cobrem 96%; o pacote de produção deve sortear entre eles, não repetir um só.
- O comando quase sempre nomeia dois ou três temas ("responsabilidade civil, princípios e poderes") e o item cobre um deles: a candidata não pode inferir o tema pelo comando.
- Texto-base (narrativa antes do "julgue"): 6% dos itens; quando existe, costuma servir a 3–5 itens seguidos ("Nessa situação hipotética, julgue os itens").

## 4. Como a banca constrói o item (mecanismos, com a ressalva do item 0.3)
Códigos do pacote de auditoria, com a leitura desta sessão do que cada um significa:

| Código | Como o item é construído | Itens C/E | % Errado |
|---|---|---|---|
| LIT | Paráfrase fiel da lei, da definição ou da tese, às vezes com ordem trocada ou sinônimo próximo | 237 | 1% |
| CON | Troca de conceito vizinho: anulação por revogação, dispensa por inexigibilidade, controlador por operador, competência por finalidade, desconcentração por descentralização | 150 | 83% |
| SUP | Supressão ou inversão de requisito, limite ou exceção que muda a conclusão ("basta…", "sem…", "não precisa…") | 147 | 65% |
| PRA | Número, prazo, quantidade, termo inicial ou âmbito trocados | 59 | 59% |
| GEN | Generalização: "sempre", "somente", "exclusivamente", "em qualquer hipótese" aplicados a regra que tem exceção | 56 | 96% |
| AP | Caso aplicado: fatos → hipótese → consequência; o erro, quando há, está na consequência | 54 | 26% |
| MIX | Proposições I/II/III ou alternativas combinadas | 52 | 87% |
| NEG | Direção invertida: "pode" por "não pode", "dever" por "faculdade", "vedado" por "permitido" | 37 | 100% |
| AUT | Troca de quem pode, deve ou responde (sujeito, órgão, Poder) | 25 | 72% |
| AMB | Âmbito trocado: a quem a norma se aplica (entes, Poderes, espécie de entidade, regime) | 23 | 65% |
| TEM | Efeito no tempo trocado (ex tunc × ex nunc; vigência; marco) | 21 | 57% |

O que isso ensina: quando o item reescreve a lei ou a tese com fidelidade (LIT), é quase sempre CERTO (99% dos LIT); o item ERRADO nasce de uma troca de vizinho (CON), de uma condição suprimida (SUP) ou de uma generalização (GEN) — juntas, cerca de 60% dos E classificados (273 de 452). Caso aplicado é raro e tende a C. Logo, o treino eficaz é o par (A × B × palavra que muda) e a checagem de requisito/exceção, exatamente o que o formato DA-v2 pede (GLOSSÁRIO, PEGADINHA A/B/MUDA, comentário com "palavra decisiva").

## 5. O que a banca cobra por item do edital (enquadramento do pacote, a confirmar no CDN)
Volume C/E e proporção de E, nos itens com 10+ questões: 10.1 licitação/contratação direta 136 (60% E); 7 improbidade 75 (53%); 11 LAI 67 (64%); 1.2 organização 62 (53%); 2.1 ato 59 (61%); 10.2 contratos 57 (46%); 4.4 Lei 9.784 47 (49%); 10.4 gestão e fiscalização 40 (48%); 3.4 Lei 8.112 36 (44%); 10.5 planejamento/fiscalização 34 (50%); 3.1 agentes (CF) 30 (53%, 30% com jurisprudência); 1.1 princípios 28 (36% E — a banca prefere afirmar princípios corretamente); 5.1 poderes 28 (32% E, 21% caso); 8.2 redes/parcerias 28; 4.2 ilícito disciplinar 23; 10.6 fiscal 23; 10.7 ETP/TR 17; 6.1 responsabilidade 14 (64% E).
Dentro de 10.1, 40 dos 136 são contratação direta (arts. 72–75), 17 modalidades, 12 instrumentos auxiliares; em 7, 35 são disposições gerais (arts. 1º a 8º-A, a redação da Lei 14.230/2021) e 23 os tipos (arts. 9º a 11); em 11, 20 são restrições de acesso (arts. 21–31). Sem candidato: 2.2, 4.1, 8.1, 8.4, 9.4, 12 (LGPD fica em outro caderno do TEC).
Jurisprudência explícita (STF/STJ/súmula) aparece em 2,5% dos itens; concentra-se em 3.1 (30%), 4.3 (23%) e 6.1 (21%).

## 6. Regras de produção derivadas (propostas para o PADRAO_UNICO; o Fundador adota)
1. Em cada lote de 20 AUTORAL de DA: 8 a 12 C, dos quais a maioria LIT (paráfrase fiel com ordem ou sinônimo trocado) e 1 a 2 AP (caso curto, consequência correta); 8 a 12 E distribuídos em CON (3–4), SUP (2–3), GEN (1), NEG (1), PRA/AUT/AMB/TEM (1–2). Registrar o mecanismo de cada item no campo `mecanismo` do pacote.
2. Nenhum item E construído só com absolutizador em frase que a lei não contém: a banca faz isso em 5% dos itens; o excesso treina a candidata num reflexo que não funciona na prova.
3. Enunciado de 21 a 35 palavras; comando nomeando 2–3 temas; fechamento sorteado entre os seis da seção 3; texto-base só quando servir a 3+ itens.
4. Caso concreto em 5–10% dos itens, não em metade; quando houver, o erro fica na consequência (AP), nunca no fato narrado.
5. Toda PEGADINHA PROVÁVEL em A/B/MUDA deve corresponder a um mecanismo CON, SUP ou AUT observado no tema; o comentário em três linhas nomeia o mecanismo na "palavra decisiva".
6. Para a candidata (orientação de estudo, não regra de chute): ler o item procurando a troca de vizinho e a condição que falta; palavras absolutas pedem atenção, não resposta automática.

## 7. Verificações pendentes
- Confirmar no CDN os gabaritos dos itens incorporados (fila BANCO-DA); recalcular as tabelas com os verificados.
- Reclassificar o mecanismo por agente da Fábrica em amostra de 100 itens (modelo distinto) e medir a concordância com a classificação do pacote antes de adotar os códigos como padrão.
- Ampliar o corpus com os cadernos do TEC de LGPD e de Administração Pública (itens 8, 9 e 12), com o mesmo tratamento.
