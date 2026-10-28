# QA — Resumo visual de Direito Administrativo, leva 2 — R2, verificação pontual (28/10/2026)

QA Opus (qa-normativo-da + gcb-cqfp-didatico + QA-plataforma), com as regras da R1. Não editei nada em /home/claude/v17_3/; este relatório é o único arquivo criado lá. Os testes rodaram com saída no scratchpad.

## Cabeçalho

**Hashes (sha256), conferidos com a mensagem da coordenação**
| Arquivo | sha256 |
|---|---|
| resumo_visual_leva2.json | 83f806dfb0e998e2dc2912ba1767cdfefd1ca43d5945ff8f93511677d5d8427a |
| resumo_visual_leva2.py | d043ab07890c20229b82307529f14a118830e1abd400751811264b2e6add9230 |
| pacote_previa_v114_rv2.json | 96f2918e877939b782af40c7912d1203fe9f027750c2b1eb9530490e2e6e9c3e |
| plataforma_v17_3_previa_leva2.html | 30836a14e54e3301499897aa8489a62449cc02b300dd5272f81fad35dafcfb73 (3.297.392 bytes) |
| checa_resumo_visual.py (v1.2) | c9e081ae9cfdf51987a41bdbc54dc5d5aa6827d79de7b1cfc37c11fede3ec483 |
| template v17.3 | 11b99a41… (inalterado) |

**Integridade da prévia**
- A prévia é exatamente o template com o pacote rv2 embutido e a meta "…levas 1 e 2 (prévia, QA R2)".
- Os 11 `resumoVisual` da leva 2 são iguais ao JSON, e os 9 da leva 1 estão intactos.
- Sem a leva 2, o pacote rv2 é igual ao pacote rv1 aprovado.

**Comandos executados**
1. Diff do dump legível R1 → R2 do JSON (116 linhas), lido inteiro; o `diff_leva2_R1_R2.txt` da produção corresponde. Nenhuma alteração fora dos pontos anunciados.
2. Cada correção conferida contra a fonte que abri na R1, verificada em 28/10/2026:
   - Câmara, Legislação Informatizada: Lei 9.784/1999 e Lei 8.112/1990, texto atualizado;
   - portal do STF: abas de tese dos Temas 532 e 592;
   - STF, Informativo 996.
3. `checa_resumo_visual.py` v1.2:
   - leva 2 com `--pacote` → 0/0;
   - pacote rv2 inteiro (20 tópicos) → 0/0;
   - leva 1 com `--pacote` → 0/0.
4. Mutação: os 22 casos da R1 (inclusive os 7 que haviam passado) e mais 8 casos novos para o desenho da v1.2 (detalhe em I5).
5. `regr_v17_3.js` (A = prévia leva 1 final, 67ee1325…; B = prévia leva 2 R2), estados antigo e antigo2 → 104 e 110 telas · 20 RV · 11 esperadas · **0 não esperadas** · 0 erros JS.
6. `t_janela20.js` → 0 falhas, 0 erros JS.
7. Teste próprio com Playwright, 11 tópicos × 4 cenários:
   - contraste mínimo 6,14:1 (claro) e 6,95:1 (escuro);
   - sem ícone sem aria-hidden, rolagem horizontal, "30" ligado à nota, preto, azul, verde/vermelho ou emoji;
   - o RV abre só nos 11 tópicos; nos outros 59, a tela antiga (clique real em 4.4, 6.5 e 7).
8. Capturas próprias dos componentes alterados a 390 px, claro e escuro: escala 4.2, rito ordinário × sumário 4.3, box do Tema 532 em 5.1, escala 6.5. Ver I6 sobre as capturas da produção.

## Conferência das correções da R1

| R1 | Resultado | Evidência |
|---|---|---|
| N1 (BLOQUEIA) | **CONFERIDO** | Marco "Instrução": "consulta pública, por despacho motivado, em matéria de interesse geral (art. 31); audiência pública, a juízo da autoridade (art. 32)". Pegadinha [1]: "O art. 32 trata da audiência pública (a consulta pública é o art. 31)". `fontes` corrigidas. Bate com os arts. 31 e 32 do texto da Câmara. |
| N2 | **CONFERIDO** | Tese do Tema 592 idêntica, caractere a caractere, à do portal do STF ("do seu dever", "art. 5º, inciso XLIX"). |
| N3 | **CONFERIDO** | Box, ramo "Ciclo de polícia" e pegadinha [2] com a ordem de polícia (função legislativa) como única fase absolutamente indelegável, e consentimento, fiscalização e sanção delegáveis nas condições da tese, conforme o Informativo 996. A tese do Tema 532 continua literal. |
| N4 | **CONFERIDO** | Box sem o STJ; art. 135 e parágrafo único (conversão da exoneração em destituição), art. 142, I (cinco anos), e destituição de função comissionada como penalidade do art. 127, VI, "sem regra própria nos arts. 135 e 142". Tudo confere com o texto da Câmara. Ver D6 sobre a nota em `fontes`. |
| N5 + D3 | **CONFERIDO** | Escala advertência → suspensão → demissão (3 pontos); cassação (art. 134) e destituição (art. 135; função comissionada, art. 127, VI) na legenda, "fora da gradação". Ver D7. |
| N6, N7 | **CONFERIDO** | Rito sumário: "Defesa escrita em 5 dias (art. 133, § 2º); julgamento em 5 dias (§ 4º)"; "a opção até o último dia da defesa configura boa-fé e converte-se em pedido de exoneração do outro cargo (§ 5º)"; pé e relâmpago [7] coerentes. Confere com o art. 133, §§ 2º, 4º e 5º. |
| N8 | **CONFERIDO** | Art. 156, § 1º, no ramo "Instrução" e na pegadinha [3]. |
| N9 | **CONFERIDO** | "salvo disposição legal diversa (art. 57)" no box; "salvo lei diversa" no relâmpago [4] e no marco "Decisão do recurso". |
| N10 | **CONFERIDO** | Linha "Interrupção da prescrição — art. 142, §§ 3º e 4º"; o texto confere em substância (falta "proferida por autoridade competente", omissão aceitável). Ver N14. |
| N12 | **CONFERIDO** | "pelo órgão competente, após o encaminhamento à autoridade superior (arts. 56, § 1º, e 59, § 1º)". |
| N13 | **CONFERIDO** | "se não houver impedimento legal, por razões de índole técnica, social, econômica, jurídica ou territorial (art. 12)". |
| D1 | **CONFERIDO** | Ramo "Excesso de poder" do mapa de 5.2: "convalidável pela doutrina majoritária, salvo competência exclusiva ou em razão da matéria (ver 2.1)". A linha "Consequência" do compare ficou como estava; com o ramo ao lado, aceitável. |
| D2, I2 | **CONFERIDO** | Pela declaração da produção; não reli a triagem. Não afetam o conteúdo exibido. |
| D4, D5 | **CONFERIDO** | Escala de 6.5 "Da exclusão ao que não afeta"; box só com o caso do Tema 592. |
| I1 | **CONFERIDO com ressalvas** | Os 7 casos que passaram na R1 agora bloqueiam ou viram aviso por decisão de desenho (marco sem "quando" e box sem rótulo, que têm fallback no renderizador). Ver I5. |
| I4 | **CONFERIDO** | Padrão de sigla só para maiúscula; o resto de ABREV continua sem diferenciar maiúsculas de minúsculas, como deve. |
| P1/P2 | **CONFERIDO** | `fontes` de 4.2, 4.3, 4.4, 5.1, 6.3 e 6.5 registram a conferência de 28/10/2026 no texto oficial. |

## Achados novos

### CORRIGIR (verificação pontual, sem nova rodada completa)

**I5 — Script v1.2: `walk()` pula `errado` e `fontes` inteiros.**
Concordo em parte. Pular os VEDADOS no `errado` é necessário, porque a pegadinha afirma o erro de propósito. Mas `errado` e `fontes` aparecem para a candidata: as fontes aparecem no rodapé "Fontes:" da tela. Os controles de emoji, probabilidade e página de PDF precisam continuar valendo nesses dois campos.

Mutação (8 casos novos):
- **Bloqueiam corretamente:** VEDADO no `certo`; tese do Tema 592 adulterada.
- **Passam:**
  - emoji no `errado`;
  - "ALTÍSSIMA PROBABILIDADE" no `errado`;
  - "p. 13" em `fontes`;
  - emoji em `fontes`;
  - tese entre aspas tipográficas ("Tese: “…”"), que escapa à lista `TESES`;
  - "A consulta pública está prevista no art. 32", ordem inversa à do padrão.

Nos 22 casos da R1, os 20 de defeito agora bloqueiam; marco sem "quando" e box sem rótulo dão aviso, por decisão aceita.

**Correção:**
- `walk()` deve devolver o nome da chave, e o laço deve aplicar EMOJI, PROB e PDF a tudo, e os VEDADOS a tudo menos `errado` e `fontes`;
- `TESE_RE` deve aceitar “ ” além de ";
- acrescentar o padrão `consulta p[úu]blica[^;.()]{0,40}art\. ?32` (e o inverso para o art. 31).

**D6 — `fontes` de P1-DA-4.2 (e as demais) exibem nota de produção à candidata.**
- O rodapé "Fontes:" da tela mostra "STJ, EDcl no MS 18.327/DF (leitura dos arts. 135 e 142 apontada pela conferência dirigida de 28/10/2026): NÃO entrou — não conferida no portal do STJ pela produção nem pelo QA; lacuna despachada à GCB".
- As demais fontes trazem "conferido … pelo QA e pela produção".
- Isso é jargão interno do Projeto na tela da candidata, mesma família do D13 da leva 1. O acórdão citado também não é ensinado.
- **Correção:**
  - retirar de `fontes` a linha do MS 18.327, que fica no relatório de produção e no despacho à GCB;
  - em todas as fontes da leva 2, trocar "conferido em 28/10/2026 pelo QA e pela produção, artigo a artigo" por "texto atualizado da Câmara dos Deputados, consultado em 28/10/2026".

**I6 — Capturas da produção.**
- `testes_v17_3/caps_l2r2/` contém **18 PNG dos tópicos da leva 1** (cel_ e desk_ de P1-DA-1 a 3.4), não as 22 da leva 2 anunciadas. O `capturas_rv.js` foi rodado sem os ids.
- As capturas que fiz dos componentes alterados (4.2, 4.3, 5.1 e 6.5, claro e escuro, 390 px) estão sem defeito:
  - escala de 3 pontos com a legenda legível;
  - rito sumário com 5 itens e o pé;
  - box do Tema 532 sem estouro;
  - escala de 6.5 com o título novo.
- **Correção:** regravar `caps_l2r2` com `node capturas_rv.js <prévia> caps_l2r2 P1-DA-4.1 … P1-DA-6.5`, para o arquivo da leva ficar completo.

### SUGESTÃO
- **D7 — 4.2, `ilustracaoSugerida`:** ainda pede "cinco degraus com as penas"; a escala agora tem três. Ajustar para "três degraus (advertência, suspensão, demissão) e, ao lado, cassação e destituição fora da gradação".
- **N14 — 4.2, linha "Interrupção da prescrição":** a banca cobra a Súmula 635 do STJ (a prescrição interrompida pela instauração válida volta a correr por inteiro depois de 140 dias; a sindicância só interrompe quando tem caráter punitivo). O texto legal está certo, mas sem a súmula induz a ler "até a decisão final" literalmente. Acrescentar como `atencao` rotulada "jurisprudência do STJ" **depois de conferir** o enunciado no portal do STJ; nesta rodada o STJ continua recusando este ambiente. Lacuna do canon: GCB, PRÓXIMO.

## Contagem (R2)
BLOQUEIA 0 · CORRIGIR 3 (I5, D6, I6) · SUGESTÃO 2 (D7, N14).

## Veredito
**APROVADO COM CORREÇÕES.** Todo o conteúdo jurídico da leva 2 está aprovado: o BLOQUEIA e os 9 CORRIGIR normativos e didáticos da R1 foram corrigidos e conferidos no texto oficial, e não há regressão. As três correções restantes não mudam o conteúdo jurídico:
- I5: robustez do checador;
- D6: notas internas no rodapé de fontes;
- I6: capturas da leva 2.

Basta uma verificação pontual pela QA, com hash novo do JSON, saída do checa e mutação dos 8 casos de I5, sem rodada completa. Com elas, a leva 2 fica apta ao "sim" do Fundador.
