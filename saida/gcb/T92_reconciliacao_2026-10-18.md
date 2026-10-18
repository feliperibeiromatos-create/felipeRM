# T92_reconciliacao_2026-10-18.md — T-92 — 2026-10-18 — gerado por gcb-gerencia

Objeto: reconciliação da T-92 (R4, onda 1 do reforço). Base: TAREFAS.md (T-92); DECISOES.md (D-REFORCO-1, D-REFORCO-2); saida/gcb/T92_D1_2026-10-18.md; saida/gcb/L6_reforco_onda1_v2.md (gcb-cpp); saida/gcb/QA_T92_R1_2026-10-18_gcb-cqfp.md (L6A-R01 APROVADO COM AJUSTE; reprovação 0/1 = 0%). O gatilho D da D1 já está em PARA_PRESIDENCIA.md e aguarda a presidencia. A GCB não escreve em PARA_PRESIDENCIA.md nem em TAREFAS.md. Os textos das seções 4 a 6 são para o orquestrador colar.

## 1. Conferência: o ajuste da QA R1 está no v2?
NÃO. O v2 ainda traz a narrativa com a "conclusão embutida" e o comando "Julgue a conclusão do servidor." (Parte 2/3). A Parte 3/3 ainda diz "A conclusão do servidor atribui ao POP3 o envio" e "QA: PENDENTE". A R1 não chega a uma R2: não há reprovação, e o ajuste é um texto exato já escrito pela QA. Quem decide depois da QA é a gcb-gerencia (D-REFORCO-1). A Gerência não reescreve o item. Ela FIXA como versão final o texto da seção 2 do parecer R1, reproduzido abaixo. A gcb-cpp transcreve esse texto literalmente num v3.

## 2. D1 (a) — versão final do L6A-R01 (FIXADA)
Arquivo de transcrição: saida/gcb/L6_reforco_onda1_v3.md. É o v2 com só estas trocas, e mais a linha 1 com a data e o agente.

2.1 Parte 2/3 — substituir todo o bloco de L6A-R01 por:
L6A-R01 (P1-3). AUTORAL. Um servidor configurou, em seu computador, um programa de e-mail para acessar, por meio do protocolo POP3, a caixa postal institucional hospedada no Exchange Online. Considerando essa situação hipotética, julgue o item a seguir.
Nessa situação, o programa de e-mail enviará as mensagens redigidas pelo servidor também por meio do POP3, dispensando outro protocolo para a saída das mensagens.

2.2 Parte 3/3 — L6A-R01, gabarito E (inalterado):
- Justificativa (duas linhas): o POP3 serve para baixar mensagens da caixa postal; o envio, em programas que acessam a caixa por POP3 ou IMAP4, fica com o SMTP, outro protocolo. O item atribui ao POP3 o envio, o que a documentação do Exchange Online nega.
- [TS]: sim — a troca sutil está em "enviará as mensagens ... também por meio do POP3" (o correto é: o envio depende do SMTP, protocolo distinto).
- A linha "QA: PENDENTE (gcb-cqfp, R1)" passa a ser "QA: APROVADO COM AJUSTE (gcb-cqfp, R1, 18/10/2026); ajuste aplicado no v3."
- Ponto, formato (situação hipotética), base (F14 do Lote 6a, verificada em 18/10/2026, trecho literal), VOLÁTIL (não), REVERIFICAR (4–8/1/2027), rótulo AUTORAL e tabela de proveniência ficam inalterados.

2.3 Conferência do v3: é a gcb-gerencia quem confere, ou o orquestrador por diff textual. Critério: o texto das seções 2.1 e 2.2 tem de estar idêntico, e nada mais pode mudar em relação ao v2. Texto idêntico: sem R2, e vale a seção 4 (CONCLUÍDA parcial + gatilho A). Texto divergente: R2 pela gcb-cqfp, última rodada.

2.4 Registros da conferência:
- Ponto único: a regra 1 da D-REFORCO-2 é cumprida. A coincidência de fonte com o 6A-12 (F14, outro trecho) é ACEITA, pois a regra veda repetir ponto, não fonte.
- Formato: P1-3 com situação hipotética em 1/6.
- VOLÁTIL novo: 0.
- Legado não imputado à onda 1: P1-3 com definição em 3/6 e VOLÁTIL em 2/6; P1-4.3 com definição em 3/6. A correção é por diluição nas ondas seguintes (D1, 2.4).
- Gabarito do R4 efetivo: 0 C / 1 E. Fica registrado para a T-93, que confere a faixa de 40% a 60% de C da onda (regra 5).

## 3. D1 (b) — estado da T-92: CONCLUÍDA parcial (depois da conferência do v3), com gatilho A só do L6A-R01
Motivo:
(i) O L6A-R01 está pronto no mérito: QA com 0% de reprovação e texto final fixado. Segurá-lo até a resposta ao gatilho D e a abertura da rede não melhora o item. Só atrasa as T-93 e T-94, que dependem das reconciliações das T-89 a T-92.
(ii) O L6B-R01 e o L6B-R02 não têm texto, por causas externas à GCB. No L6B-R01 falta base literal aberta: a página anti-phishing do learn.microsoft.com não sustenta a conduta, e support.microsoft.com, gov.br e cert.br não abrem. No L6B-R02, a base (F4, cartilha.cert.br) não abre, e a solução depende do gatilho D. Deixar a T-92 BLOQUEADA prenderia um item aprovado a uma dependência que não é dele.
(iii) Esta reconciliação REVÊ a seção 4 da D1 de 18/10, segundo a qual o "gatilho A só com os 3 resolvidos". Os 2 itens não são retirados. Eles passam a uma tarefa nova (seção 6) e continuam devidos à D-REFORCO-1 (R4 = 3).
(iv) Fica para a Presidência, no gatilho A, decidir se o déficit de 2 itens em P1-4.3 entra na v1.9 (caso a tarefa nova se resolva antes da T-94 começar) ou na consolidação seguinte. O tema não é D1 da GCB.

## 4. Texto do estado para a linha T-92 (o orquestrador substitui o campo de estado)
Enquanto o v3 não estiver conferido:
EM CURSO (ciclo 2026-10-18 s12c1; QA R1 = 0%, L6A-R01 APROVADO COM AJUSTE; versão final fixada em saida/gcb/T92_reconciliacao_2026-10-18.md, seção 2; aguarda a transcrição literal no v3 pela gcb-cpp e a conferência; L6B-R01 e L6B-R02 transferidos para a tarefa nova)
Depois do v3 conferido como idêntico:
CONCLUÍDA parcial (18/10/2026, s12c1): 1 de 3 itens — L6A-R01 (P1-3, E, situação hipotética, não VOLÁTIL), final em saida/gcb/L6_reforco_onda1_v3.md; L6B-R01 e L6B-R02 (P1-4.3) transferidos à T-<nova> (BLOQUEADA: gatilho D + rede); gatilho A emitido só para o L6A-R01; reconciliação em saida/gcb/T92_reconciliacao_2026-10-18.md

## 5. Gatilho A (texto para PARA_PRESIDENCIA.md; colar só depois de conferido o v3)
GATILHO A | GCB | T-92 (R4, onda 1 do reforço, D-REFORCO-1) — aceite PARCIAL: 1 de 3 itens | saida/gcb/L6_reforco_onda1_v3.md; saida/gcb/QA_T92_R1_2026-10-18_gcb-cqfp.md; saida/gcb/T92_reconciliacao_2026-10-18.md | L6A-R01 (P1-3; AUTORAL; gabarito E; situação hipotética; não VOLÁTIL; [TS] 1; base: Microsoft Learn "POP3 e IMAP4 em Exchange Online", verificado em 18/10/2026, trecho literal; QA R1 APROVADO COM AJUSTE, reprovação 0%; ajuste aplicado literalmente). P1-3 passa de 5 para 6 (meta da onda atingida). P1-4.3 fica com 4 de 6: L6B-R01 e L6B-R02 transferidos à T-<nova>, BLOQUEADA pelo gatilho D pendente e pela rede (cert.br, support.microsoft.com e gov.br negados; a página anti-phishing do learn.microsoft.com não sustenta a conduta). Legado não imputado: P1-3 com definição em 3/6 e VOLÁTIL em 2/6; P1-4.3 com definição em 3/6 (diluição nas ondas seguintes). Gabarito do R4: 0 C / 1 E (para a T-93, regra 5). | Pedido: aceitar o L6A-R01 para consolidação (T-94) e decidir se os 2 itens de P1-4.3 entram na v1.9 (caso resolvidos antes de a T-94 começar) ou na consolidação seguinte.

## 6. Tarefa nova (o id fica a cargo do orquestrador)
T-<nova>; GCB; REFORÇO onda 1 — R4, saldo do Lote 6b (D-REFORCO-1; transferido da T-92 pela reconciliação de 18/10): 2 itens AUTORAL em P1-4.3 — L6B-R01 (aplicação parlamentar; conduta diante de mensagem com link que pede dados: não usar o link e confirmar por canal oficial; não VOLÁTIL) e L6B-R02 (troca de sujeito; relação gênero-espécie phishing/pharming invertida; sem mencionar DNS nem redirecionamento; ponto distinto de 6B-14). Base: página oficial (OUTRA_OFICIAL ou documentação do fornecedor) aberta na data da produção, com trecho LITERAL e "verificado em [data]"; ou, se a resposta ao gatilho D for SIM, trecho literal já registrado na proveniência canônica com a data verdadeira anterior (D1 de 18/10, 1.2(b)), lembrando que a F15 não sustenta o L6B-R01. Valem as regras da D-REFORCO-2 (1 a 4) e as seções 2.2 a 2.4 da D1 (formato com 0 ocorrência na folha; nenhum "definição"; 0 VOLÁTIL novo). Formato da D-REFORCO-1 (PARTE n/N; (d) sem gabarito e sem [TS]; (d-G) com [TS], VOLÁTIL e REVERIFICAR). Item sem base aberta continua SUSPENSO, e a retirada definitiva é decisão registrada da gcb-gerencia. QA em no máximo 2 rodadas; reconciliação, depois gatilho A; PRÓXIMO (vira AGORA com a resposta ao gatilho D ou com a abertura de cert.br/support.microsoft.com, ou com outra página oficial aberta que sustente o trecho); BLOQUEADA (gatilho D da T-92 pendente; rede); gcb-cpp → gcb-cqfp → gcb-gerencia; saida/gcb/L6B_reforco_onda1_saldo_v1.md (pareceres e reconciliação em saida/gcb/)

## 7. Ordem imediata
gcb-cpp: gravar saida/gcb/L6_reforco_onda1_v3.md conforme a seção 2, por transcrição literal, sem nenhuma outra mudança. Em seguida, o orquestrador ou a gcb-gerencia confere conforme a seção 2.3.
