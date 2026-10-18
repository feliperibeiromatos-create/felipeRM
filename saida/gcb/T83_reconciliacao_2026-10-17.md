# T83_reconciliacao_2026-10-17.md — T-83 — 2026-10-17 — gerado por gcb-gerencia

Objeto: reconciliação da T-83, errata OPCIONAL de forma (D-RT81-02 e D-RT81-04; AGORA por D-FUNDADOR-AGORA-2). Cadeia: gcb-cpp → gcb-cqfp → gcb-gerencia.
Entradas:
- produção: saida/gcb/T83_errata_proposta_2026-10-17.md (gcb-cpp; proposta, não aplicada);
- QA: saida/gcb/QA_T83_2026-10-17_gcb-cqfp.md (Erratum 1 APROVADO COM AJUSTE; Erratum 2 APROVADO; 0/2 reprovadas);
- contexto: saida/pacote/T81_reconciliacao_2026-10-17.md (D-RT81-02, D-RT81-04);
- objetos: saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md e saida/gcb/GCB_Lote5C_v1_GCB-CPP.md.

## 1. Veredito
**T-83 reconciliada (D1 GCB): as duas erratas são ACEITAS e foram APLICADAS pela GCB nos canônicos espelhados.** Erratum 1 entra com o ajuste do QA; Erratum 2 entra como proposto. Nada volta à gcb-cpp. Só a frase indicada mudou em cada arquivo, mais o registro (rótulo de versão e linha da Tabela de Correções). Nenhum gabarito, enunciado, item, [TS], VOLÁTIL ou fonte mudou.

Quem aplica: a GCB. O arquivo de agente manda a Gerência "aplicar erratas sem mudar gabarito" e registrar a Tabela de Correções. O precedente da casa é a T-47: a GCB aplicou o registro, e a D-TRANSPORTE-L5-V32 aceitou o resultado. A D-EDITOR-UNICO diz que o conteúdo canônico é editado só pela fábrica. Aqui o texto já vinha redigido pela produção e conferido pelo QA, então a GCB não redigiu nada: só transcreveu o "leia-se" aprovado.

## 2. Decisão sobre cada errata

### Erratum 1 — L4-11, justificativa — ACEITO COM O AJUSTE DO QA
| Opção | Decisão | Motivo |
|---|---|---|
| Redação da gcb-cpp ("A página "Introduction to ML: What is Machine Learning?", do Google for Developers, afirma que") | descartada | Entre aspas, como título, a gcb-cpp põe uma cadeia que a página não contém. A gcb-cqfp abriu a URL em 17/10/2026: o título é "What is Machine Learning?", e "Introduction to Machine Learning" é o curso. Isso é imprecisão de proveniência num texto que vai ao estudante. Corrigir custa zero rodada, porque o QA já fixou o texto. |
| Redação do QA | **adotada** | Fiel à página; mantém a fonte identificada; não toca nas citações literais. |

Texto final aplicado (Parte 3, d-G, item 11; linha 368 da v3.5):
"A página "What is Machine Learning?", do curso Introduction to Machine Learning do Google for Developers, afirma que "generative models are initially trained using an unsupervised approach" e que "the model is sometimes trained further using supervised or reinforcement learning"; o item descreve o pré-treino como "sem rótulos atribuídos manualmente", sem classificar o "auto-supervisionado"."
Ficam intactos: gabarito C, "v3 (O10)", eixo 5.2, "GI invertida", ausência de [TS], "Fonte: F4, reverificado em 7/10/2026." e a menção ao TRF6 (CEBRASPE_ANALOGA).
- O "the" minúsculo da 2ª citação (o original tem "The") é ajuste usual de caixa e não muda.
- A observação (a) da gcb-cpp fica sem ação, de acordo com o QA. O gerador já retira "Fonte: F4, …" da camada do estudante, e no canônico o código é registro interno legítimo (regras/proveniencia.md).

### Erratum 2 — 5C-08, justificativa — ACEITO COMO PROPOSTO
Texto final aplicado (linha 50 da v1.2): "É, entre os itens 5C, o mais próximo do item A5-20: o ponto de julgamento é outro instrumento, mas o princípio, dirigir a atenção, é o mesmo."
- O sentido não muda.
- A oposição lote/canônico, que perdeu o referente com a fusão da T-81, sai do texto.
- A frase anterior ("Difere do item A5-20…") continua coerente.
- Ficam intactos: gabarito E, [TS], eixo 8.4, TC e as referências ao curso 8.4 e ao resumo 8.1.

### Registro (padrão do arquivo; precedente T-47)
| Arquivo | Rótulo de versão (cabeçalho) | Linha nova na Tabela de Correções |
|---|---|---|
| GCB_Lote4_v3_canonica_GCB-CPP.md | linha 11: "v3.5 — errata de forma T-83 (D-RT81-04) na justificativa do item 11, Parte 3; conferida pela CQFP em 17/10/2026; registro na Tabela de Correções" | linha 44: "Errata T-83 (D-RT81-04, 17/10/2026)", com "onde se lia" e "lê-se", origem e status "aplicada (v3.5, 17/10/2026); conferida (CQFP, 17/10/2026)" |
| GCB_Lote5C_v1_GCB-CPP.md | linha 7: "v1.2 — errata de forma T-83 (D-RT81-02) na justificativa do 5C-08; conferida pela CQFP em 17/10/2026; registro na Tabela de Correções" | linha 15: "Errata T-83 (D-RT81-02, 17/10/2026)", no mesmo formato |

Sobre o rótulo de versão:
- O rótulo segue a T-47 (v3.2 do Lote 5), para que a Secretaria e a D-CANONICOS tenham um nome.
- O "itens só de forma não abrem versão" da T-12 vale para o pacote, não para o canônico, e o pacote não muda nesta tarefa.
- Nem os rótulos nem as linhas da Tabela trazem as cadeias "[TS]" ou "VOLÁTIL", então as contagens por grep não mudam.

## 3. Observação (b) — curso 5.2.5 do L4 — TAREFA NOVA T-85 (PRÓXIMO)
Decisão: abrir a tarefa, não só registrar.
Motivo: é defeito de forma visível à candidata.
- O canônico diz "É o que afirma o F4:" (linha 144 da v3.5), e o gerador o reduz a "É o que afirma:", frase sem sujeito (saida/estudante/L4_estudo.md:106).
- Na conferência, a GCB achou na mesma seção um segundo caso, que nenhuma das duas unidades registrou: "ficar com a formulação do F4" (linha 145) sai como "ficar com a formulação e evitar" (L4_estudo.md:107).

A T-85 junta, num só ciclo gcb-cpp → gcb-cqfp → gcb-gerencia:
1. os dois trechos acima;
2. a recomendação do QA de corrigir o rótulo F4 da tabela de fontes (linha 50 da v3.5), de onde nasceu a imprecisão do título; só o rótulo muda, a URL não;
3. uma varredura da gcb-cqfp por outros resíduos de código de fonte que o gerador deixa sem sujeito ou complemento nos L4, 4-C, 5 e 5-C.

Classe PRÓXIMO: não bloqueia nada, e a absorção é na próxima T-12.
A GCB não é dona do gerador. Se a varredura mostrar que o defeito é sistêmico, a correção da regra de retirada é da GBQ, e a GCB a levará à GBQ na reconciliação da T-85.

## 4. Conferência por script (somente leitura; bases copiadas no scratchpad antes da edição)
| Verificação | Lote 4 (base 7c4bb117… → 5930eba9…) | Lote 5-C (base ff8f79fc… → 480c52c9…) |
|---|---|---|
| Operações do diff | 3: insert l.11 (rótulo), insert l.44 (Tabela), change 366→368 (frase) | 3: insert l.7 (rótulo), insert l.15 (Tabela), change 48→50 (frase) |
| Linhas com "[TS]" | 12 → 12 | 9 → 9 |
| Linhas com "VOLÁTIL" | 10 → 10 | 3 → 3 |
| Linhas de gabarito do d-G | 20 → 20 | 10 → 10 (5C-NN) |
| Fim de linha | CRLF, 381 → 383 linhas, sem mistura | CRLF, 54 → 56 linhas, sem mistura |
| Bytes | 67051 → 67899 | 9554 → 10231 |
SHA-256 completos: Lote 4 v3.5 = 5930eba9ca94eebf834e248206efa9e4b67c1e6edd0f06f6c66b1974886b3699; Lote 5-C v1.2 = 480c52c9dbac12715763bd98cb811039f9394199ac372e639a035485cd5fa959 (CRLF, como estão no disco).

## 5. Não tocados
- saida/estudante/ (L4_gabarito.md:58; L5_gabarito.md:151), saida/pacote/ e os geradores. São derivados e absorvem a errata na próxima ocorrência da T-12.
- A linha da T-83 em TAREFAS.md, que é do orquestrador fechar.

## 6. Gatilho
GATILHO E em PARA_PRESIDENCIA.md (ciclo s11c3), no rito das erratas de canônico já transportadas (D-TRANSPORTE-L5-V32, D-TRANSPORTE-L3-T58, D-TRANSPORTE-L2L3-T64). Ele pede duas coisas:
(a) aceitar como canônicas a v3.5 do Lote 4 e a v1.2 do 5-C (D-CANONICOS);
(b) transportar os dois espelhos ao Projeto.

Por que a GCB não fecha isto só em D1: o canônico é a última versão aceita pela Presidência, e o canônico de referência está no Projeto (D-EDITOR-UNICO, esclarecimento (a); D-LOTE4-FONTE). Uma errata só em D1 deixaria o espelho à frente do canônico sem aceite.

Não se emite gatilho A: o pacote não muda nesta tarefa, e o aceite do pacote vem com a próxima T-12, pela GBQ.
