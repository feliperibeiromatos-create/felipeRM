# QA — Resumo visual de Direito Administrativo, leva 2 — R3, verificação pontual (28/10/2026)

QA Opus (qa-normativo-da + gcb-cqfp-didatico + QA-plataforma), com as mesmas regras. Não editei nada em /home/claude/v17_3/; este relatório é o único arquivo criado lá. Escopo: I5, D6, I6 e D7 da R2, mais a busca de regressão.

## Cabeçalho

**Hashes (sha256), conferidos com a mensagem da coordenação**
| Arquivo | sha256 |
|---|---|
| resumo_visual_leva2.json | 69419664d0961fb13701cfd249f00a18bcb8467d86fcb665bdb9bb4d20746359 |
| resumo_visual_leva2.py | 8f5553c8995d0dd53bdf12c500ceca1bf1f2781d0b5c83246c3f3d879043156a |
| pacote_previa_v114_rv2.json | 0883a24239d7ec4bc82f2ddb05ad7027f8018b722710bcbfa4e785831211f9dc |
| plataforma_v17_3_previa_leva2.html | 6993ef600806db389b7b9d55bdb02895c0662c02d5ea56a237b5a54112191053 (3.296.352 bytes) |
| checa_resumo_visual.py (v1.2 reescrito) | 43ed8198dd940474852783a012b7d35afb838242ef2c0857ea2b6f869168ecfe |
| template v17.3 | 11b99a41… (inalterado) |

**Comandos executados**
1. Diff R2 → R3 do JSON, chave a chave, contra a cópia R2 guardada na minha mutação.
   - **Mudaram só** `fontes` (10 tópicos: todos menos 6.4; 5.2 sem mudança relevante) e `ilustracaoSugerida` de 4.2.
   - **Nenhum bloco de conteúdo mudou** nos 11 tópicos, nem a `cobranca`.
2. Integridade:
   - a prévia é exatamente o template com o pacote rv2 embutido (meta "…levas 1 e 2 (prévia, QA R3)");
   - os 11 RV da leva 2 são iguais ao JSON; os 9 da leva 1 estão intactos;
   - fora a leva 2, o pacote rv2 é igual ao rv1.
3. Leitura do checador novo:
   - `walk()` devolve (chave, string);
   - PROB, EMOJI, PDF e TESES valem em todos os campos, inclusive `errado` e `fontes`; só os VEDADOS poupam essas duas chaves;
   - `TESE_RE` normaliza as aspas tipográficas antes de comparar;
   - os VEDADOS incluem a ordem inversa ("consulta pública … art. 32", "audiência pública … art. 31").
4. `checa_resumo_visual.py` nos três alvos:
   - leva 2 com `--pacote` → 0/0;
   - pacote rv2 inteiro (20 tópicos) → 0/0;
   - leva 1 com `--pacote` → 0/0.
5. Mutação: 34 casos (detalhe em I5).
6. `regr_v17_3.js` (A = prévia leva 1 final; B = prévia leva 2 R3), estados antigo e antigo2 → 104 e 110 telas · 20 RV · 11 esperadas · **0 não esperadas** · 0 erros JS.
7. `t_janela20.js` → 0 falhas, 0 erros JS.
8. Capturas `caps_l2r3`: 22 PNG (cel_ e desk_ de P1-DA-4.1 a 6.5). Vista a de 4.2 no celular: pegadinhas e rodapé "Fontes:" no registro novo, sem estouro.

## Conferência

| R2 | Resultado | Evidência |
|---|---|---|
| I5 (script) | **CONFERIDO** | Mutação (34 casos). Os 8 casos novos da R2 agora **bloqueiam** todos: emoji e "ALTÍSSIMA" no `errado`, "p. 13" e emoji em `fontes`, VEDADO no `certo`, tese do Tema 592 adulterada, tese com aspas tipográficas adulterada, "A consulta pública está no art. 32". Os 4 casos extras se comportam como esperado: "audiência pública no art. 31" bloqueia; "p. 11" no `errado` bloqueia; tese 592 correta entre aspas tipográficas passa; "até dez testemunhas" no `errado` passa, por desenho. Nos 22 da R1, 20 bloqueiam; marco sem "quando" e box sem rótulo dão aviso, por decisão aceita. |
| D6 (fontes) | **CONFERIDO** | Nenhuma ocorrência de "QA", "produção", "NÃO entrou", "lacuna" ou "despachada". A linha do MS 18.327 saiu. As conferências aparecem como "texto … conferido na Câmara dos Deputados, Legislação Informatizada, em 28/10/2026" e "tese conferida no portal do STF em 28/10/2026". As correções do MapasPro aparecem como "conferido e corrigido (ver triagem)", mesmo registro da leva 1 aprovada. |
| D7 | **CONFERIDO** | Ilustração sugerida de 4.2: "três degraus com as penas…". |
| I6 | **CONFERIDO** | `caps_l2r3` com as 22 capturas da leva 2. |
| N14 | **Encaminhado** | Súmula 635 do STJ fora do visual até a conferência; pendência registrada para a GCB. |

## Observações (SUGESTÃO; não bloqueiam e podem ir para a leva 3)
- **O1 — `fontes` de 4.1:** "…Lei 9.784/1999, arts. 2º e 69; STF, Súmula Vinculante 5 — textos conferidos na Câmara dos Deputados". A súmula vinculante não é texto da Câmara. Trocar por "…; STF, Súmula Vinculante 5" com a conferência da Câmara só nos textos legais.
- **O2 — `fontes` de 5.1:** dizem que CF, CTN e Lei 6.830 foram "conferidos na Câmara em 28/10/2026". Nesta leva, eu conferi no texto oficial só a Lei 9.784 e a Lei 8.112; a conferência desses três é da produção (P1: guardar o trecho literal como evidência). Os dispositivos citados coincidem com o canon conferido em 20/10/2026, e não há divergência de conteúdo.

## Contagem (R3)
BLOQUEIA 0 · CORRIGIR 0 · SUGESTÃO 2 (O1, O2).

## Veredito final
**APROVADO.** A leva 2 do Resumo visual de Direito Administrativo (11 tópicos; JSON 69419664…, pacote rv2 0883a242…, prévia 6993ef60…, template 11b99a41…) e o checador v1.2 (43ed8198…) estão aptos ao "sim" do Fundador. Ficam como ressalvas as observações O1 e O2 (leva 3) e as pendências da GCB: Súmula 635 do STJ; Temas 940 e 130 do STF; MS 18.327, ainda não conferido.
