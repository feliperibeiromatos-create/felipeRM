# T85_errata_proposta_2026-10-18.md — T-85 — 2026-10-18 — gerado por gcb-cpp

PROPOSTA de errata de FORMA. Nada foi aplicado nos canônicos. Nenhum gabarito, item, enunciado, marca [TS]/VOLÁTIL ou URL muda. Sem fonte externa.
Alvo principal: saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md (v3.5, CRLF). Linhas numeradas conforme o arquivo em disco em 2026-10-18; cada "onde se lê" foi conferido por contagem (ocorre 1 vez).
Regra de retirada do gerador (saida/pacote/gerador_v1_8/estudante_marcas.py e estudante_gen.py): apaga o código de fonte (Fn, Un, GGn, TBn) e o carimbo de verificação; não reconstrói o sujeito nem o complemento da frase. Quando o código é o sujeito ou o complemento de um verbo ou preposição, a frase sai truncada. A solução de forma é nomear a fonte em palavras no canônico (como na errata T-83).

## A. Os três pontos da tarefa

### P1 — curso 5.2.5, linha 144
- Arquivo: saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md, linha 144.
- Onde se lê: `É o que afirma o F4: "generative models are initially trained using an unsupervised approach"`
- Leia-se: `É o que afirma a página "What is Machine Learning?", do curso Introduction to Machine Learning do Google for Developers: "generative models are initially trained using an unsupervised approach"`
- Resto da frase inalterado ("e "the model is sometimes trained further using supervised or reinforcement learning" (reverificado em 7/10/2026)").
- Motivo: na camada do estudante (saida/estudante/L4_estudo.md:106) sai "É o que afirma:", sem sujeito. Com a fonte nomeada, o gerador não tem código a retirar e a frase fica completa. Redação igual à da errata T-83 (item 11).
- Observação: na mesma linha 144, "o lote usa o F4 como fundamento, não o TRF6" já sai da camada do estudante inteira (L4_estudo.md:106 termina em "...TRF6_002_01)."), sem defeito; não precisa de errata.

### P2 — curso 5.2.5, linha 145
- Arquivo: saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md, linha 145.
- Onde se lê: `o candidato deve ficar com a formulação do F4 e evitar itens que dependam da classificação do "auto-supervisionado".`
- Leia-se: `o candidato deve ficar com a formulação da página "What is Machine Learning?" e evitar itens que dependam da classificação do "auto-supervisionado".`
- Motivo: L4_estudo.md:107 sai "ficar com a formulação e evitar itens", sem complemento de "formulação". A página já foi nomeada por extenso em P1, na linha anterior, o que dispensa repetir o curso.

### P3 — tabela de fontes, linha 50, rótulo F4
- Arquivo: saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md, linha 50.
- Onde se lê: `F4 — Google for Developers, "Introduction to ML: What is Machine Learning?", developers.google.com/machine-learning/intro-to-ml/what-is-ml`
- Leia-se: `F4 — Google for Developers, "What is Machine Learning?" (curso Introduction to Machine Learning), developers.google.com/machine-learning/intro-to-ml/what-is-ml`
- Motivo: o título da página é "What is Machine Learning?" (QA T-83, gcb-cqfp, saida/gcb/QA_T83_2026-10-17_gcb-cqfp.md, linha 13); "Introduction to ML:" é o nome do curso abreviado, não parte do título. Só o rótulo muda; a URL (campo após a última vírgula) fica idêntica. Fica coerente com P1, P2 e com o item 11 (errata T-83).
- Observação: os trechos "F4 — Google for Developers, "Introduction to ML: ..." em saida/gcb/QA_T83_*.md, T83_errata_proposta e T83_reconciliacao são registros históricos da T-83; não se alteram.

## B. Varredura preliminar (python -I, somente leitura)
Método: em L4, 4-C, 5 e 5-C canônicos (saida/gcb/GCB_Lote4_v3..., GCB_Lote4C_v1..., GCB_Lote5_v3..., GCB_Lote5C_v1...) listei toda ocorrência de F1–F9, U1–U9, GG, TB em prosa (precedida de palavra, "—", ":" ou início de linha), cruzei com a regra de retirada do gerador e com o resultado nos seis arquivos de saida/estudante/ (L4 e L5: estudo, itens, gabarito). Também varri a camada do estudante por padrões de frase truncada (preposição ou "conforme/segundo" antes de pontuação, "— as técnicas." etc.).
Resultado: 3 resíduos novos que o gerador deixa truncados (B1 a B3, B1 e B2 no Lote 4, B3 no Lote 5); os demais usos de código em prosa resultam em frase completa (lista B4). 4-C e 5-C: nenhum resíduo (as justificativas 4C-05, 4C-07, 4C-09 e 5C-NN saem completas; os trechos "Fonte: F1 e F2, conforme o curso 5.1.3." e "(definição de alucinação do F3)" são retirados inteiros).

### B1 — curso, exemplo da engenharia de prompts, linha 106 (Lote 4)  [defeito, prioridade igual à de P1/P2]
- Arquivo: saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md, linha 106.
- Onde se lê: `delimitação do contexto com tags — as técnicas de F1 e F2. Se o resumo precisasse`
- Leia-se: `delimitação do contexto com tags — as técnicas de engenharia de prompts vistas neste curso. Se o resumo precisasse`
- Motivo: L4_estudo.md:70 sai "... com tags — as técnicas. Se o resumo...", com "as técnicas" sem complemento. Proposta sem criar afirmação nova: remete ao conteúdo do próprio curso. Alternativa mais curta se a Gerência preferir: "— as técnicas desse tipo de prompt."

### B2 — curso 5.3.2, abertura da lista, linha 172 (Lote 4)  [defeito leve]
- Arquivo: saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md, linha 172.
- Onde se lê: `Segundo o F5 (verificado em 7/10/2026):`
- Leia-se: `Segundo a página "GAN — Background: What is a Generative Model?", do Google for Developers:`
- Motivo: a linha inteira é retirada da camada do estudante; as duas listas de L4_estudo.md:132-133 (generativo e discriminativo) ficam sem a frase de abertura que atribui as definições. Aqui o carimbo "(verificado em 7/10/2026)" foi omitido na proposta para a frase não depender da regra de retirada do carimbo; a data de verificação do F5 permanece na tabela de fontes (linhas 46 a 51, "verificadas em 7/10/2026"). Se a Gerência quiser manter o carimbo no canônico, acrescentar " (verificado em 7/10/2026)" antes dos dois-pontos e aceitar que o gerador o retire ou o deixe; confirmar no teste do gerador.
- Rótulo de F5 conforme linha 51: "GAN — Background: What is a Generative Model?".

### B3 — justificativa A5-14, linha 264 (Lote 5)  [defeito leve, elipse; opcional]
- Arquivo: saida/gcb/GCB_Lote5_v3_canonica_GCB-CPP.md, linha 264 (justificativa do item A5-14; o item, o gabarito C e a marca VOLÁTIL não se tocam).
- Onde se lê (1): `Três componentes e fluxo conforme U1 en-us (`
- Leia-se (1): `Três componentes e fluxo conforme a documentação "Using Power BI", da Microsoft Learn (`
- Onde se lê (2): `natureza Windows do Desktop conforme U2.`
- Leia-se (2): `natureza Windows do Desktop, conforme a documentação da Microsoft Learn.`
- Motivo: saída atual em saida/estudante/L5_gabarito.md:73 é "Três componentes e fluxo ("three primary components"; ...); natureza Windows do Desktop." Nenhuma das duas frases é agramatical, mas "Três componentes e fluxo (...)" e "natureza Windows do Desktop." ficam sem verbo e sem atribuição. Prioridade baixa; a Gerência pode registrar "sem errata". O rótulo "en-us" fica só na tabela de fontes (linhas 30-31), onde a URL canônica está.

### B4 — verificados, sem defeito na camada do estudante (nenhuma proposta)
- Linhas 128, 129, 133 ("Exemplos do F4", "exemplo do F4"): saem "Exemplos:" e "exemplo:" (L4_estudo.md:90, 91, 95); completas.
- Linha 139 ("que o F4 descreve como a melhor estratégia"): sai "(policy), a melhor estratégia para acumular recompensas." (L4_estudo.md:101); apositivo completo.
- Linha 179 ("o F3 os define separadamente;"): cláusula retirada inteira (L4_estudo.md:138); completa.
- Linha 180 ("lista em tópicos do F4", "tabela de exemplos do F4"): saem "a lista em tópicos", "a tabela de exemplos" (L4_estudo.md:139); completas.
- Linhas 288, 364 a 373 (resumo e d-G; "— F4)", "o F4 cita a chuva", "Fonte: Fn"): cláusulas ou parênteses retirados inteiros; completos (ex.: L4_gabarito.md:38).
- Linha 204 (P-lista, "o F3 define os termos separadamente"): sai completa.
- 4-C linhas 8, 36, 43, 45 e justificativas: retiradas inteiras; completas (L4_gabarito.md:125, 130, 140).
- Lote 5 linhas 131, 139, 145 (cabeçalhos "— fonte principal U1...", "— U3; ... TB2"): o código e o carimbo saem e restam os títulos "Power BI (Microsoft)", "Tableau (Salesforce)", "Data Studio (Google)" (L5_estudo.md:109, 117, 123); completos.
- Lote 5 linhas 9, 19 a 23, 273 a 277 (F1, F2, F3 a/b, F4 do despacho 2 do Lote 5): são códigos de DESPACHO, não de fonte; ficam na camada de processo do canônico e não chegam ao estudante.
- Linha 33 do Lote 4 ("F1 e F2 só na justificativa") e linha 52 ("trazem F1–F5"): camada de processo; não chegam ao estudante.

## C. Conferências de que nada de conteúdo muda
- As propostas P1, P2, P3 e B1 a B3 tocam só: o rótulo de fonte, o nome da fonte no corpo do curso ou na justificativa, e uma frase-ponte. Nenhuma cifra, citação, URL, gabarito, enunciado, [TS] ou VOLÁTIL é alterada.
- Contagem esperada após aplicação (para o QA conferir por script): Lote 4 v3.5: linhas com "[TS]" 12 → 12; com "VOLÁTIL" 10 → 10; linhas 383 → 383 (todas as propostas são trocas dentro de linha); fim de linha CRLF preservado. Lote 5 v3: idem para o B3 (troca dentro de linha).
- Se o gerador for rodado depois da errata, as 6 linhas afetadas na camada do estudante (L4_estudo.md:70, 106, 107, 132 e L5_gabarito.md:73, mais a tabela de fontes que não chega ao estudante) devem ser as únicas diferenças; o resto dos seis arquivos fica idêntico.
- Defeito sistêmico? Os 5 casos (P1, P2, B1, B2, B3) têm a mesma causa: a regra de retirada do gerador é por deleção e não reescreve a frase. A GCB não é dona do gerador; se a Gerência quiser prevenção, a GBQ pode acrescentar ao teste do gerador (conferencias) uma verificação de frase terminada em preposição/artigo/"afirma:"/"as técnicas." antes da pontuação. Esta é só uma sugestão, sem aplicação.

## D. Resumo
- Pontos propostos: 6 (P1, P2, P3 pedidos; B1, B2, B3 da varredura; B3 opcional).
- Defeitos reais na camada do estudante: 4 (P1, P2, B1, B2); 1 leve/opcional (B3); P3 é de rótulo no canônico, não chega ao estudante.
- 4-C e 5-C: sem resíduo; Lote 5 sem defeito além do B3.
- Nenhum gabarito, item, enunciado, marca ou URL muda; fonte externa não usada.
- Pendente de decisão: carimbo "(verificado em 7/10/2026)" em B2 (retirado na proposta, data mantida na tabela de fontes).
