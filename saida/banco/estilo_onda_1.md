# estilo_onda_1.md — T-93 — 2026-10-18 — gerado por gbq-estilo

Auditoria de estilo da onda 1 do reforço (D-REFORCO-2, regras 5 e 6). Ciclo 2026-10-18 s12c2. Destino: gbq-gerencia.
Referência: regras/estilo_banca.md v1.1.3 (tipologia E1–E6, C1–C6; marcadores, seção 4; recomendações, seção 5).
Arquivos lidos, só leitura: saida/gce/L1_reforco_onda1_v2.md (L1-R01–R18), saida/gce/L2_reforco_onda1_v3.md (L2-R01–R18), saida/gce/L3_reforco_onda1_v3.md (L3-R01–R11), saida/gcb/L6_reforco_onda1_v3.md (L6A-R01). Decisões: D-REFORCO-2, D-T89-R1-ACEITE, D-T90-R2-ACEITE, D-T91-R3-ACEITE, D-T92-R4-PARCIAL, D-ONDA1-FILA. Nenhum item foi alterado.

Resultado: 5 itens auditados, 5 APROVADOS, 0 REPROVADOS (0%). Sem GATE. Gabarito da onda: 23 C / 25 E (47,9% de C), dentro da faixa de 40% a 60% (regra 5).

## 1. Amostra e critério

- Universo: os 48 itens aceitos (L1 18, L2 18, L3 11, L6A 1). L6B-R01 e L6B-R02 estão SUSPENSOS (sem texto nem gabarito) e ficam fora (D-T92-R4-PARCIAL).
- Tamanho: 10% de 48 = 4,8, arredondado para 5 (o mínimo da T-93).
- Critério: sorteio estratificado com semente registrada.
  1. L6A-R01 entra por obrigação, porque é o único item do R4.
  2. Um item sorteado em cada um dos lotes L1, L2 e L3, nessa ordem, com `random.Random(20261018).choice` sobre a lista de ids em ordem crescente.
  3. Um quinto item sorteado com o mesmo gerador entre os 44 itens restantes de L1, L2 e L3.
  - Ferramenta: Python 3.13, `python3 -I`. Os ids e gabaritos foram extraídos da Parte 3 de cada arquivo.
- Amostra: L1-R07, L2-R11, L3-R02, L2-R14 (quinto sorteado) e L6A-R01. São 2 C e 3 E, todos os quatro lotes.

## 2. Vereditos por item

Critérios de estilo: comando "Julgue o item" (ou o formato Cebraspe de situação hipotética seguida de "julgue o item a seguir"); uma afirmação e um só ponto de erro; mecanismo reconhecível na tipologia; marca [TS] coerente; marcadores lexicais que não denunciam o gabarito; extensão dentro do observado na base (C de 8 a 65 palavras, E de 19 a 62); nenhuma dependência de versão de produto.

| id | gab. | mecanismo (estilo_banca) | palavras | veredito | motivo |
|---|---|---|---|---|---|
| L1-R07 | C [TS] | C3 (C que parece E), espelho de E1: o par separação por canais × diarização vem descrito corretamente | 47 | APROVADO | O comando está certo. Há uma afirmação só e o par de conceitos vizinhos está descrito sem erro, o que pune quem marca E por reflexo diante do contraste. O "pode" é possibilidade afirmativa, que a seção 4 associa a C, mas aqui não decide o gabarito. A marca [TS] num item C é convenção da GCE ("falsa pegadinha"); a seção 5.1 não a exige nem a proíbe. |
| L2-R11 | C | C3 (concessiva "ainda que" em item verdadeiro), em formato situacional | 68 | APROVADO | O comando está certo e o ponto é único: o revisor escolhe entre as alternativas, e a ordenação não garante acerto. A concessiva verdadeira segue a recomendação de C3. Observação, sem reprovar: 68 palavras passam do máximo de C da base (65). O item é situacional e tem duas frases, como os blocos com texto-base da base. |
| L3-R02 | E [TS] | E3 (alteração do comando normativo: troca do sujeito que autoriza, Presidente → Plenário) | 41 | APROVADO | O item abre com "Segundo o RICD" (remissão à fonte; 5 C e 3 E na base) e tem um só erro deliberado, no sujeito da autorização. "Mesa" fica correta, e isso impede o atalho de achar tudo falso. Observação, sem reprovar: a oração explicativa "que pode servir de insumo para a transcrição e a indexação por inteligência artificial" não vem do art. 78. Ela não muda o gabarito (E dos dois jeitos), mas, depois de "Segundo o RICD", pode ser lida como afirmação da norma. Nas próximas ondas, convém pôr o vínculo com IA fora do escopo da remissão. Aderência PARCIAL (D-ADERENCIA) não é matéria de estilo. |
| L2-R14 | E [TS] | E5 (moldura verdadeira, "a Administração pode contratar uma empresa de apoio", com consequência acessória falsa); traço de E3 | 43 | APROVADO | É a forma típica da banca: a frase principal é verdadeira (art. 117, caput) e a cauda é falsa (§ 4º). "pode" num item E diversifica o marcador, como pede a seção 5.1. Observação, sem reprovar: "exercer, em lugar do fiscal, as atribuições próprias e exclusivas" é quase autocontraditório e pode denunciar o E a quem lê com atenção. A expressão é literal da lei, e o mecanismo continua válido. |
| L6A-R01 | E [TS] | E4 (ferramenta ou protocolo × tarefa: atribui ao POP3 o envio, que ele não faz); a cauda "dispensando outro protocolo" reforça o mesmo erro e não cria um segundo | 59 no total (cerca de 27 no texto-base e 25 no item) | APROVADO | Usa o formato Cebraspe de situação hipotética ("Considerando essa situação hipotética, julgue o item a seguir" e "Nessa situação, ..."), aceito para itens com texto-base (estilo_banca, 3.13: forma situacional). O erro está num único segmento. O produto (Exchange Online) só ambienta a situação: o gabarito depende da função do protocolo, não de versão. "também" e "dispensando" não são marcadores absolutos. |

Taxa de reprovação da amostra: 0/5 = 0%, abaixo do gate de 30%.

## 3. Faixa de C da onda (regra 5), por contagem própria

Contagem por script sobre a Parte 3 (gabarito comentado) de cada arquivo, com uma entrada por id:

| lote | arquivo | itens | C | E | %C |
|---|---|---|---|---|---|
| R1 | L1_reforco_onda1_v2.md | 18 | 9 | 9 | 50,0 |
| R2 | L2_reforco_onda1_v3.md | 18 | 8 | 10 | 44,4 |
| R3 | L3_reforco_onda1_v3.md | 11 | 6 | 5 | 54,5 |
| R4 | L6_reforco_onda1_v3.md | 1 | 0 | 1 | 0,0 |
| Onda 1 | 4 arquivos | 48 | 23 | 25 | 47,9 |

- CONFERE com o esperado (23 C / 25 E = 47,9%) e com as contagens declaradas nas D-T89, D-T90, D-T91 e D-T92. Está dentro da faixa de 40% a 60%.
- Pela D-T92-R4-PARCIAL, a faixa é conferida de novo no gatilho A da T-102, se L6B-R01 e L6B-R02 entrarem. Com 2 itens a mais, a faixa continua cumprida em qualquer combinação: 23/50 = 46,0%, 24/50 = 48,0% e 25/50 = 50,0%.

## 4. Observações sobre a onda inteira (registro; não fazem parte do veredito da amostra)

As contagens foram feitas por expressão regular no enunciado (Parte 2) dos 48 itens, com revisão manual dos falsos positivos indicados. A AVISO da seção 4 do estilo_banca continua valendo: nenhum marcador decide o gabarito.

- Absolutos e restritivos: "apenas" aparece em 2 C (L1-R05, L1-R10) e 3 E (L1-R09, L1-R11, L2-R12). "somente" aparece em 1 C (L3-R01) e 1 E (L2-R09). "exclusiv-" aparece em 0 C e 2 E (L1-R13, L2-R14). "garantidamente" aparece em 0 C e 1 E (L1-R15). "sempre", "qualquer" e "prioritariamente" não aparecem. O "só" de L1-R04 ("de uma só vez") não é restritivo. Há C com restritivo, como recomenda a seção 5.1.
- Causais: "pois" aparece em 2 C (L1-R08, L2-R10) e 1 E (L1-R11). "porque" em 2 C (L1-R04, L2-R18). "uma vez que" em 1 E (L1-R01). A causa não está presa a E.
- Concessiva: "ainda que" só em C (L1-R10, L2-R11), e "mesmo que" não aparece. É n pequeno, mas o estilo_banca já registra concessiva em C (BQ-0012).
- "independe/independentemente": 0 C e 3 E (L1-R01, L1-R11, L2-R05). O "independentes" de L3-R07 (C) não conta. Em E, aparece como veículo do erro nos três casos. A base tem 1 C e 1 E. Recomenda-se à onda 2 escrever pelo menos um C com "independe".
- Possibilidade afirmativa ("pode", "podem", "poderá"): 8 C e 3 E (L2-R05, L2-R14, L3-R02). É um viés para C parecido com o da base (15 C, 5 E) e não é motivo de reprovação.
- Extensão, em palavras, contando o enunciado sem o comando:
  - C: média 49,6, mediana 47, de 29 a 76.
  - E: média 40,4, mediana 39, de 23 a 62.
  - A base tem C com média 31,6 (de 8 a 65) e E com média 34,7 (de 19 a 62).
  - A onda tem itens mais longos que a base e inverte a relação: na onda, C é mais longo que E. A diferença ainda é moderada. Mesmo assim, recomenda-se à GCE e à GCB, na onda 2, encurtar os C e escrever E longos, para que a extensão não vire pista.
  - Dois itens passam do máximo de C da base: L2-R10 (76) e L2-R11 (68).
- [TS]: 23 de 48 (L1 7, L2 10, L3 5, L6A 1). Dois estão em itens C (L1-R07, L2-R02), por convenção de "espelho". Não há relação fixa entre [TS] e gabarito.

## 5. Encaminhamento

- À gbq-gerencia: T-93 concluída sem GATE. Pela D-ONDA1-FILA (2), a T-94 pode passar a AGORA.
- As observações das seções 2 e 4 são recomendações para a onda 2 (T-96). Nenhuma pede mudança em item aceito.

AVISO: os vereditos e a atribuição de mecanismo são julgamento deste agente (gbq-estilo) e exigem revisão da GBQ. As contagens de C/E e de marcadores vêm de script sobre os arquivos finais, e os marcadores tiveram revisão manual só nos falsos positivos indicados.
