# QA — Resumo visual de Direito Administrativo, leva 3 — R2, verificação pontual (28/10/2026)

QA Opus (qa-normativo-da + gcb-cqfp-didatico + QA-plataforma), com as regras da R1. Não editei nada em /home/claude/v17_3/; este relatório é o único arquivo criado lá.

## Cabeçalho

**Hashes (sha256), conferidos com a mensagem da coordenação**
| Arquivo | sha256 |
|---|---|
| resumo_visual_leva3.json | 63b7cef2e361a9ee022edcce96585a26df43934f7f62b5a6b109cb9a6018ed5a |
| resumo_visual_leva3.py | f928d5eaeab671e19377fca124b875433fe30d552646193dd87e051ba8dcecdf |
| pacote_previa_v114_rv3.json | 4051c2965f9994ade3931b14766e72f6a5e5faed6cbba91381ee101a8b5ae3ab |
| plataforma_v17_3_previa_leva3.html | 601f12c6c52f68b9055275d1ec0bccd2acf45325640c584e1ca996da9e15b736 (3.363.570 bytes) |
| TRIAGEM leva 3 | 44272ae0d2cb2d157da0219e98d04fce5cb7fe8ecae6bc4253ca85c0ff785d29 |
| template / checa | 11b99a41… / 43ed8198… (inalterados) |

**Comandos executados e fontes (verificado em 28/10/2026)**
1. Diff do dump R1 → R2 (99 linhas), lido inteiro. Mudaram só os blocos anunciados (7, 8, 8.1, 8.3, 9.4) e as `fontes` do 7.
2. **Novo nesta rodada:** as **certidões de julgamento** das duas ADIs, no portal do STF (aba Andamentos e aba Decisões dos processos). Elas trazem a parte dispositiva literal de cada sessão, e prevalecem sobre as notícias:
   - ADI 7.236, incidente 6475588: sessões de 28/5, 24/6, 25/6 e 1º/7/2026; atas publicadas no DJE em 02/07/2026 e 04/08/2026;
   - ADI 7.156, incidente 6396615: sessões de 28/5, 24/6 e 25/6/2026.
   - O acórdão em si não aparece publicado nos andamentos lidos.
3. `checa_resumo_visual.py`: leva 3 com `--pacote` → 0/0; pacote rv3 inteiro (30 tópicos) → 0/0.
4. `regr_v17_3.js` (prévia leva 2 × prévia leva 3 R2), estados antigo e antigo2 → 104 e 110 telas · 30 RV · 10 esperadas · **0 não esperadas** · 0 erros JS. `t_janela20.js` → 0 falhas.
5. Integridade:
   - a prévia é exatamente o template com o pacote rv3 embutido (meta "…levas 1 a 3 (prévia, QA R2)");
   - os RV das três levas estão iguais aos JSON;
   - sem a leva 3, o pacote rv3 é igual ao rv2.
6. Teste próprio com Playwright, 10 tópicos × 4 cenários: contraste mínimo 6,14:1 (claro) e 6,95:1 (escuro); nenhum problema.
7. Busca textual no JSON do 7 por "benefícios diretos", "metade", "10-C", "Tribunal de Contas", "mesma qualidade", "solidari", "perigo de dano", "intercorrente" e "urgência". **Nenhum texto ensina como vigente a regra derrubada**; todas as ocorrências são a correção.

## Conferência dos blocos reescritos do P1-DA-7 contra as certidões de julgamento

| Bloco (R1) | Certidão do STF | Resultado |
|---|---|---|
| N1, linha do tempo + relâmpago [5] + pegadinha [9] | 7.236, 1º/7/2026: inconstitucionalidade da expressão "pela metade do prazo previsto no caput deste artigo" do art. 23, § 5º, "com prazo máximo de 20 (vinte) anos de prescrição" | **CONFERIDO.** "Recomeça inteiro" corresponde ao § 5º sem a expressão. O teto de 20 anos está certo. A ressalva sobre o § 8º ("aguarda a leitura do acórdão") é adequada. |
| N2, fluxo [4] | 7.156 e 7.236, 24/6/2026: inconstitucionalidade do art. 17, §§ 10-C, 10-D e 10-F, I | **CONFERIDO** (ver S1). |
| N3, fluxo [2] | 7.156, 24/6/2026, art. 16, §§ 3º, 4º e 10 | **CORRIGIR** (C1). |
| N4, box do trânsito em julgado | 24/6/2026: art. 12, § 1º, inconstitucionalidade de "apenas" e de ", na hipótese do inciso I do caput deste artigo, e em caráter excepcional,"; "podendo" lido como poder-dever, com exceção fundamentada. 28/5/2026: inconstitucionalidade do art. 12, § 4º. | **CONFERIDO.** |
| N5, acordo de não persecução civil | 24/6/2026: art. 17-B, § 3º, inconstitucional | **CONFERIDO.** |
| N6, box do art. 21 | 25/6/2026: art. 21, § 4º, parcialmente inconstitucional, com interpretação conforme | **BLOQUEIA** (B2). |
| N7, pegadinha do ressarcimento | 7.156, 24/6/2026: art. 17-C, § 2º, inconstitucionalidade de "e dos benefícios diretos", com interpretação conforme: "vedada qualquer solidariedade para fins de sanção, ressalvada a possibilidade para fins de responsabilidade patrimonial" | **CONFERIDO.** |
| N8, mapa (terceiro) | 7.156, 28/5/2026: art. 3º, § 1º, inconstitucionalidade (ex tunc) de "e benefícios diretos" | **CONFERIDO.** |
| N9, texto B1 (§ 8º) | 7.156 e 7.236, 28/5/2026: interpretação conforme do art. 1º, § 8º, com texto fixado | **BLOQUEIA** (B1). |
| N10, fontes + relâmpago [8] | 28/5/2026: art. 1º, §§ 1º a 3º, art. 10 e art. 11, caput e revogação dos incisos I e II, constitucionais | **CONFERIDO**, com C2. |

Itens 8 e 9: D1, D2, N11, N12 e N13 aplicados como proposto; **conferidos**. A triagem não foi relida nesta rodada; I1 e P1 ficam pela declaração da produção.

## Achados

### BLOQUEIA

**B1 — P1-DA-7 · `texto` B1, última frase (art. 1º, § 8º).**
- **Texto atual:** "…assim como a divergência interpretativa fundada em entendimento, **ainda que não pacificado**, do STF, dos tribunais superiores ou, na falta deles, de **decisões colegiadas de segunda instância** (§ 8º, na leitura do STF…)".
- **Certidão de julgamento de 28/5/2026, idêntica nas ADIs 7.156 e 7.236:** "exceto nos casos que evidenciado o dolo ou erro grosseiro, consideradas as circunstâncias do caso e a gravidade da infração, nos termos do art. 14 do Decreto nº 9.830/2019, não configura improbidade a ação ou omissão decorrente de divergência interpretativa da lei, baseada em jurisprudência **assentada** nos Tribunais Superiores ou no Supremo Tribunal Federal e, na falta dessa jurisprudência, em **decisão de mérito transitada em julgado** proferida por órgão colegiado de 2º Grau, mesmo que não venha a ser posteriormente prevalecente".
- O visual ensina o contrário em dois pontos: "não pacificado" × "assentada", e "decisões colegiadas" × "decisão de mérito transitada em julgado". Também omite a ressalva do dolo ou erro grosseiro. A notícia oficial de 28/5 dizia "ainda que não pacificados"; a certidão prevalece.
- **Redação proposta:** "…assim como a divergência interpretativa da lei baseada em jurisprudência **assentada** no STF ou nos tribunais superiores ou, na falta dela, em **decisão de mérito transitada em julgado** de órgão colegiado de 2º grau, salvo dolo ou erro grosseiro (§ 8º, com a interpretação conforme fixada pelo STF nas ADIs 7.156 e 7.236)".

**B2 — P1-DA-7 · `box` regra "Independência das instâncias (art. 21)", segunda frase.**
- **Texto atual:** "…só a encerra, com trânsito em julgado, quando reconhece a inexistência do fato, a negativa de autoria, a legítima defesa, o estrito cumprimento do dever legal ou o exercício regular do direito".
- **Certidão de julgamento de 25/6/2026 (ADIs 7.156 e 7.236):** a decisão criminal transitada em julgado "somente impede a tramitação da ação de improbidade administrativa nas hipóteses dos arts. 65 (… **estado de necessidade**, legítima defesa, estrito cumprimento de dever legal ou exercício regular de direito); 386, I (estar **provada** a inexistência do fato); e 386, IV (estar **provado** que o réu não concorreu para a infração penal)". A mesma regra se aplica "seja na absolvição, seja na rejeição da denúncia, seja na hipótese de preclusão da decisão de arquivamento por proposição do Ministério Público, ressalvada a hipótese do art. 18 do CPP".
- O rol do visual vem sob "só" e omite o **estado de necessidade**. Também não diz que a prova precisa ser positiva ("provada", "provado"), o que separa essas hipóteses da absolvição por falta de provas. É o mesmo tipo de defeito que bloqueou na leva 1 (rol fechado incompleto).
- **Redação proposta:** "A absolvição criminal não encerra automaticamente a ação de improbidade. Só a decisão criminal transitada em julgado que reconheça estado de necessidade, legítima defesa, estrito cumprimento do dever legal ou exercício regular de direito (CPP, art. 65), a **prova** da inexistência do fato (art. 386, I) ou a **prova** de que o réu não concorreu para a infração (art. 386, IV) impede a ação, e isso vale também para a rejeição da denúncia e o arquivamento precluso (STF, ADIs 7.156 e 7.236, interpretação conforme do § 4º)."

### CORRIGIR

**C1 — P1-DA-7 · `fluxo`, passo [2] (art. 16).**
- **Texto atual:** "…o STF admitiu o bloqueio sem demonstração de urgência quando houver indícios especialmente fortes".
- **Certidão de 24/6/2026 (ADI 7.156):**
  - inconstitucionalidade, ex nunc, das expressões "apenas" e "mediante a demonstração no caso concreto de perigo de dano irreparável ou de risco ao resultado útil do processo" (§ 3º), "não podendo a urgência ser presumida" (§ 4º) e a ressalva sobre multa civil e acréscimo lícito (§ 10);
  - interpretação conforme para admitir, "em hipóteses excepcionais, por meio de decisão devidamente fundamentada", a indisponibilidade com base em **tutela de evidência** e a **presunção de urgência**;
  - como regra, o bloqueio recai sobre montante suficiente ao "integral ressarcimento do dano ao erário, para que o valor possa abranger a multa civil e o enriquecimento ilícito".
- "Indícios especialmente fortes" é a paráfrase da notícia.
- **Redação proposta:** "indisponibilidade de bens (art. 16): em caráter excepcional e por decisão fundamentada, cabe com base em tutela de evidência ou com presunção de urgência; alcança o ressarcimento, a multa civil e o enriquecimento ilícito (STF, ADI 7.156)".

**C2 — P1-DA-7 · `fontes`.**
- Acrescentar: "STF, ADIs 7.156 e 7.236: certidões de julgamento das sessões de 28/5, 24/6, 25/6 e 1º/7/2026 (atas publicadas no DJE em 02/07 e 04/08/2026), lidas no portal do STF em 28/10/2026". Manter "acórdão pendente de leitura".
- Na triagem, seção 3a: registrar que a certidão prevalece sobre a notícia (o caso do § 8º mostra a diferença).

### SUGESTÃO
- **S1:** fluxo [4]: acrescentar o § 10-F, I ("afastando os §§ 10-C, 10-D e 10-F, I"). O § 10-F, I anulava a condenação por tipo diverso do da inicial e caiu na mesma decisão.
- **S2:** box do art. 12 (N4): opcionalmente, "poder-dever" (expressão da certidão) e a inconstitucionalidade do **art. 12, § 10**, também declarada em 24/6/2026 (contagem retroativa da suspensão dos direitos políticos).
- **S3:** temas do mesmo julgamento que a banca pode cobrar e que ficaram de fora:
  - art. 17-D: a ação é repressiva e não substitui a ação civil pública;
  - art. 23-C: partidos políticos também respondem pela Lei de Improbidade;
  - art. 12, III: sem suspensão dos direitos políticos nos atos que atentam contra princípios, desde 1º/10/2021, mantida a cautelar da ADI 6.678.
  - Podem entrar numa leva de revisão.
- **P2:** despachar à GBQ/GCB, junto com a pendência já registrada, a lista exata de dispositivos atingidos (certidões acima). O banco do item 7 deve ser revisto contra a parte dispositiva, não contra as notícias.

## Contagem (R2)
BLOQUEIA 2 (B1, B2) · CORRIGIR 2 (C1, C2) · SUGESTÃO 4 (S1, S2, S3, P2).

## Veredito
**REPROVADO**, só por B1 e B2, ambos no P1-DA-7 e ambos em blocos reescritos com base nas notícias, que nesses dois pontos divergem da parte dispositiva das certidões. As correções são de texto: duas frases, mais C1 e C2. A **R3 pode ser pontual**, com o diff e a conferência contra as certidões, já lidas.

O resto do item 7 está conferido e nenhum texto ensina mais regra derrubada. Os itens 8 e 9 estão **aprovados**, com as sugestões aplicadas corretamente. A interface passou em todos os testes.

## O que mudar antes da R3
1. **B1:** § 8º com o texto da interpretação conforme (jurisprudência assentada; decisão de mérito transitada em julgado de colegiado de 2º grau; salvo dolo ou erro grosseiro).
2. **B2:** art. 21, § 4º com as hipóteses dos arts. 65 e 386, I e IV, do CPP (inclui estado de necessidade; "provada" e "provado"), e a extensão à rejeição da denúncia e ao arquivamento precluso.
3. **C1:** art. 16 com a tutela de evidência e a presunção de urgência excepcionais, e o alcance sobre multa e enriquecimento.
4. **C2:** fontes com as certidões de julgamento e as atas do DJE.
5. **S1 a S3 e P2:** a critério da produção.
