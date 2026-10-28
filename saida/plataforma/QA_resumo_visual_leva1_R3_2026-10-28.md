# QA — Resumo visual de Direito Administrativo, leva 1 + plataforma v17.3 — R3, verificação pontual (28/10/2026)

QA Opus (qa-normativo-da, gcb-cqfp-didatico, QA-plataforma), com as regras da R1 e da R2. Não editei nada em /home/claude/v17_3/; este relatório é o único arquivo criado lá. Escopo: conferir N1–N11 e N15 da R2 e procurar regressão.

## Cabeçalho

**Hashes (sha256), conferidos com a mensagem da coordenação**
| Arquivo | sha256 |
|---|---|
| resumo_visual_leva1.py | e37a2b5d1901138388145083a48d4f14b28e6999764773465b053dfc2a358244 |
| resumo_visual_leva1.json | e31ec9cfb87e642eae701bda454060a3189c3777140428f6199b7f3ea46b3cd1 |
| checa_resumo_visual.py | f9042aeead4aea8d17e549b2740b39c9e72a6e3b24ebcbfecc65ce13b735dbbb |
| patch_v17_3_resumo_visual.py | 1ba3070e5fa81b7040df79253b05228233b1aa37bf7010ae4aca284f8bc1126e |
| plataforma_v17_3_template.html | 11b99a41e9137f40f704fbd2807774529cd93a2376f0e47ac049e1cb5daf0e35 (reaplicado sobre o v17.2 89f07db1…: mesmo hash, 6 substituições) |
| pacote_previa_v114_rv1.json | 77480c0579a55eeac5645f8459fd452123d5a35438f0723d725f1f5c13a7aed3 |
| plataforma_v17_3_previa.html | e184edaf58f655d2d335920d3cba55db607b31e337ab9c30e27456042364f86b |
| extras_leva1_v114.json (canon) | d5398fcd… (inalterado) |

**Comandos executados**
- Diff do JSON R2 → R3: 17 trechos alterados, todos lidos; nenhuma alteração fora dos pontos tratados.
- Integridade: a prévia embute o pacote; os `resumoVisual` do pacote são iguais ao JSON; o resto do pacote é igual ao v1.14 da prévia v17.2c.
- `checa_resumo_visual.py` (com `--pacote` e sobre o pacote) → 0 bloqueios, 0 avisos.
- Mutação (21 casos): 19 casos de defeito bloqueiam. Passam só o controle (esperado) e "número sem norma" (fica para o QA, por decisão registrada). Inclui o art. 54 com "dez anos", o art. 20 com "36 (trinta e seis)", o art. 21 com "3 (três) anos", `literal` falso, data "2026-13-45", "SEM: Petrobras e Vale" e "tema quente".
- Regressão `regr_v17_3.js`, estados antigo e antigo2 → 104 e 110 telas · 9 RV · **0 diferenças não esperadas** · 0 erros JS.
- `t_janela20.js` → só a falha esperada `0.const` (v17.3).
- `t_pir.js`, rodado do scratchpad → 0 falhas em 6 cenários.
- Teste próprio com Playwright (o da R1), 9 tópicos × 4 cenários:
  - contraste mínimo de texto 6,14:1 (claro) e 6,95:1 (escuro);
  - sem ícone sem aria-hidden, rolagem horizontal, "30" ligado à nota, preto, azul, verde/vermelho ou emoji;
  - "Resumo" abre o RV só nos 9 tópicos (os outros 70 abrem a tela antiga; clique real em 2.1, 3.4 e 4.4);
  - etiquetas: 1, 3.2 e 3.3 "poucas questões deste item no corpus"; 2.2 "nenhuma questão enquadrada neste item no corpus"; demais com número e C/E.

## Conferência ponto a ponto

| Ponto R2 | Resultado | Evidência |
|---|---|---|
| N1 (ALTA) | **CONFERIDO** | Ramos: "implícitas na CF; expressas na Lei 9.784, art. 2º…" e "implícita na CF; expressa na Lei 9.784, art. 2º…". A legenda define "implícito na CF", põe o contraditório e a ampla defesa como expressos (art. 5º, LV) e a razoabilidade, a proporcionalidade e a segurança jurídica como implícitas na CF e expressas na Lei 9.784. Correto e sem contradição interna. |
| N2 | **CONFERIDO** | Quatro subtetos do art. 37, XI: Prefeito; Governador; Deputados Estaduais e Distritais; Desembargadores limitados a 90,25%, com o mesmo limite para MP, Procuradores e Defensores. Relâmpago: "subtetos por ente e por Poder (XI)". |
| N3 | **CONFERIDO** | Frase própria para a centralização e a concentração; [2] e [3] fundidas. Ver a observação O1. |
| N4 | **CONFERIDO** | Compara `texto` normalizado e `literal`. A única tolerância é a anotação exata "(prazo 3 anos - vide EMC nº 19)" do art. 21, e a mutação do art. 21 bloqueia mesmo assim. |
| N5 | **CONFERIDO** | Sem referência ao "pacote". |
| N6 | **CONFERIDO** | "Reverificar." no fim da frase do estágio probatório. |
| N7 | **CONFERIDO** | A frase de extinção traz "desaparecimento do sujeito/objeto"; a decadência entrou na frase da convalidação. Ver a observação O2. |
| N8 | **CONFERIDO** | CLT e Leis 8.212, 8.213 e 11.770 na tabela e em `fontes`, como na publicação original da Câmara. |
| N9 | **CONFERIDO** | 2.2 com "nenhuma questão enquadrada neste item no corpus". |
| N10 | **CONFERIDO** | "(doutrina)". |
| N11 | **CONFERIDO** | Data real (`fromisoformat`); termos vedados ampliados nos dois sentidos; a regra "número sem norma" fica para o QA, decisão aceita. |
| N15 | **CONFERIDO** | Texto literal da alínea c no ramo; título curto por causa do limite de 60. |
| N12–N14 | **Encaminhados** | Vão ao relatório de produção como pendências: ciência da ESPEC v3.1 à Gerência; ADI 191 marcada "a reconferir no portal do STF" em `fontes` (conferido no JSON); despacho do canon 3.1/3.4 à Secretaria de Estado Canônico. **A pendência N14 precisa ser executada antes da próxima publicação do pacote v1.14**: o curso e o resumo em prosa do 3.1 continuam dizendo "o estável só perde o cargo nas hipóteses do art. 41, § 1º". |

## Observações (BAIXA, não bloqueiam; podem ir para a leva 2)
- **O1 — P1-DA-1.2, relâmpago [3]:** "lei específica cria/autoriza (CF, 37, XIX)". A compressão apaga quem a lei cria (a autarquia) e quem ela autoriza (as demais). A pegadinha [4] do mesmo tópico ensina a distinção, então não há erro. Sugestão: "lei específica cria autarquia; autoriza as demais (CF, 37, XIX)", que cabe em 140 caracteres se "Presidência e Ministérios" virar "PR e Ministérios".
- **O2 — P1-DA-2.1, relâmpago [7]:** "decadência: cinco anos (art. 54)" perdeu "para atos de efeitos favoráveis, salvo comprovada má-fé". O compare B12 e o bloco `lei` da mesma tela têm a regra inteira. Sugestão: reescrever a frase só com a decadência ("Decadência: 5 anos p/ anular ato favorável, salvo má-fé (art. 54)") e devolver a convalidação à sua frase.

## Regressão
Nenhuma. Os testes de interface, a regressão e o checa repetem os resultados da R2, com o checa mais estrito. No JSON, as únicas mudanças são as anunciadas.

## Contagem (R3)
BLOQUEIA 0 · ALTA 0 · MÉDIA 0 · BAIXA 2 (O1, O2). Pendências de processo fora do objeto: N12, N13 e N14.

## Veredito final
**APROVADO.** A leva 1 do Resumo visual de Direito Administrativo e a plataforma v17.3 (prévia e184edaf…, template 11b99a41…) estão aptas a seguir para o "sim" do Fundador. Ficam como ressalvas O1 e O2 (BAIXA, para a leva 2) e a execução do despacho N14 no canon antes da próxima publicação do pacote.

## Adendo de fechamento (28/10/2026)
O1 e O2 aplicados e conferidos: o diff R3 → final mostra só as frases 1.2 relâmpago [3] e 2.1 relâmpago [7]; o checa dá 0/0 com --pacote; a prévia é o template 11b99a41… com o pacote embutido, e o resto do pacote é igual ao v1.14. Ressalva mínima, sem efeito no veredito: a frase 1.2 [3] perdeu "específica" e a citação do art. 37, XIX; a pegadinha [4] do mesmo tópico as mantém. Hashes finais: resumo_visual_leva1.py 402b6d37011d3d85337a4f63aafe7973640f9fce5ecfa514df8bfe8d6a3b6758 · resumo_visual_leva1.json f618895c8f8ffa0af6dc7a05cea747733bb2fc2ad891260ed60c69b02f1f2dd3 · pacote_previa_v114_rv1.json b62a7bf714d267e4058e8f0b41969676cf1be922e9901dbd99193233f017a7b0 · plataforma_v17_3_previa.html 67ee1325c903976dbc3cdf0fccf0a7d24fbeea15989a8ad9cd3f4c8e5ea6c3fe · template 11b99a41e9137f40f704fbd2807774529cd93a2376f0e47ac049e1cb5daf0e35 · patch 1ba3070e5fa81b7040df79253b05228233b1aa37bf7010ae4aca284f8bc1126e · checa f9042aeead4aea8d17e549b2740b39c9e72a6e3b24ebcbfecc65ce13b735dbbb. **APROVADO, hashes finais registrados.**
