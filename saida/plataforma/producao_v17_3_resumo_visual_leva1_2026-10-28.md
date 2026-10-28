# Produção — Plataforma v17.3 · Resumo visual de Direito Administrativo, leva 1 (itens 1, 2 e 3 do edital)

Sessão Cowork (Fable 5.1), 28/10/2026. Ordem do Fundador (28/10): incorporar os 16 resumos MapasPro de DA à plataforma como "Resumo visual" por tópico, traduzindo a estética ao sistema visual v0.2 (decisão a), infográficos em SVG/HTML, ordem do edital em levas de três itens. QA independente: Opus (agente af152742b6e006842), rodadas R1 (REPROVADO, 35 defeitos), R2 (APROVADO COM RESSALVAS) e R3 (APROVADO, hashes finais registrados no adendo do R3).

## Entregáveis (hashes sha256 finais)

| Arquivo | sha256 | O que é |
|---|---|---|
| saida/plataforma/patch_v17_3_resumo_visual.py | 1ba3070e5fa81b70e… | aplica 6 substituições sobre plataforma_v17_2_template.html (89f07db1…): VERSAO_APP v17.3, CSS `.rv*`, 16 ícones SVG, tipos piramide/mapa/dois/escala/linhaTempo, tela `vResumoVisual`, desvio em `vResumoVer` quando o tópico tem `resumoVisual` |
| saida/plataforma/plataforma_v17_3_template.html | 11b99a41e9137f405… | template v17.3 (reprodutível pelo patch) |
| saida/plataforma/plataforma_v17_3_previa.html | 67ee1325c903976de… | PRÉVIA: template + pacote v1.14 + resumoVisual dos 9 tópicos (não publicar; meta "não publicar") |
| saida/plataforma/resumo_visual_leva1.py / .json | 402b6d37011d3d858… / f618895c8f8ffa0a3… | gerador e fragmento `{id: resumoVisual}` dos tópicos P1-DA-1, 1.1, 1.2, 2.1, 2.2, 3.1, 3.2, 3.3, 3.4, para a GBQ consolidar no pacote (campo novo `topicos[id].resumoVisual`, versão v3) |
| saida/plataforma/checa_resumo_visual.py | f9042aeead4aea8db… | verificador v1.1 (seção 3c da ESPEC): limites, ícones, termos vedados, `conferido` em data válida, cruzamento texto/literal com o `baseLegal` do pacote (`--pacote`); função `checa_pacote` para o checa_pacote_v2.py |
| saida/plataforma/testes_v17_3/ | — | lib.js, capturas_rv.js, regr_v17_3.js, t_janela20.js, t_pir.js, gera_estado.js, estados antigos, resultados json, caps/ (18 capturas de página inteira + 4 recortes da pirâmide) |
| saida/plataforma/QA_resumo_visual_leva1_R1/R2/R3_2026-10-28.md | — | relatórios do QA Opus |
| claude/ESPEC_resumo_visual_DA_v3_2026-10-28.md (v3.1) | — | formato, tradução estética, limites, regras de conteúdo, testes |
| claude/TRIAGEM_resumos_MapasPro_DA_2026-10-28.md | — | mapa PDF → item, veredito bloco a bloco da leva 1, pré-triagem das levas 2–4 |

## Testes finais

- `checa_resumo_visual.py resumo_visual_leva1.json --pacote pacote_previa_v114_rv1.json`: 0 bloqueios, 0 avisos; mutação do QA (art. 54 "dez anos") → 1 bloqueio.
- `regr_v17_3.js` v17.2 → v17.3 com estado_antigo_v114 e estado_antigo2_v114: 104 e 110 telas, 9 mudanças esperadas (telas de Resumo dos 9 tópicos), **0 diferenças não esperadas**, 0 erros JS. Notas, caderno, bloco de 10, janela 20, Refazer e chaves do estado intactos.
- `t_janela20.js`: só a falha esperada (VERSAO_APP). `t_pir.js`: 0 falhas (320/390/1280 × claro/escuro; sem transbordo em nenhum nível da pirâmide). Capturas sem erro JS.
- QA: contraste mínimo 6,14:1 (claro) e 6,95:1 (escuro); ícones aria-hidden; sem rolagem horizontal a 320 px; o botão "Resumo" abre a tela nova só nos 9 tópicos; o resto do pacote idêntico ao v1.14.

## Conferências normativas feitas nesta produção (28/10/2026, Câmara dos Deputados, Legislação Informatizada — o Planalto bloqueia este ambiente)

- Lei 9.986/2000, art. 9º, I a III, na redação da Lei 13.848/2019, art. 42; parágrafo único revogado pelo art. 52, VI.
- LC 229/2026: só ressalva fiscal (art. 3º). Lei 15.371/2026 (31/3/2026, vigência 1º/1/2027; art. 11: 10 dias em 2027, 15 em 2028, 20 em 2029): altera CLT e Leis 8.212, 8.213 e 11.770 — **não altera a Lei 8.112**; o art. 208 (5 dias) continua.
- Decreto 10.835/2021, art. 9º, §§ 1º a 5º (não nominal: § 2º; exceção Presidência/Vice: § 3º).
- EC 138/2025, art. 37, XVI, b: "um cargo de professor com outro de qualquer natureza" (QA R1).
- Pendente de reconferência em fonte oficial: STF, ADI 191 (citada com Tema 545 no 1.2; o Tema 545 foi conferido pelo QA em boletim do TJDFT). Marcada em `fontes`.

## Despachos e pendências

1. **Secretaria de Estado Canônico / GBQ (AGORA, antes da próxima publicação do pacote):** pacote v1.14, P1-DA-3.1, `resumo` e `emUmMinuto[2]` dizem "o estável só perde o cargo nas hipóteses do art. 41, § 1º" — falta a CF, art. 169, § 4º (excesso de despesa com pessoal). P1-DA-3.4, `baseLegal` do art. 21 da Lei 8.112 traz a anotação editorial do Planalto "(prazo 3 anos - vide EMC nº 19)" dentro do texto `literal: true`. O Resumo visual já sai corrigido; o curso e o resumo em prosa continuam com o texto antigo até a correção na origem.
2. **CIÊNCIA à Gerência:** a ESPEC v3 foi emendada para v3.1 pela produção após o QA R1 (limites: mapa ramo 90 → título ≤ 60 e texto ≤ 180; dois 2–6 → 2–7, pelo rol de sete formas de provimento/vacância da Lei 8.112). O QA (R2, N12) registrou que quem produz não aprova a própria régua; a emenda vale até manifestação da Gerência.
3. **Publicação:** só com o "sim" do Fundador (D-AUDITORIA-20OUT). Recomendação: publicar v17.3 (que contém a v17.2) de uma vez; o `plataforma_v17_3_previa.html` não é o arquivo de publicação — o build de publicação usa o pacote consolidado pela GBQ com o campo `resumoVisual`.
4. **Ilustrações (ao Fundador):** três indicações registradas em `ilustracaoSugerida` (1: três camadas Estado/Governo/Administração; 1.2: Ministério com órgãos dentro da mesma silhueta e autarquia fora, ligada por fio de supervisão; 2.1: duas réguas, vinculado × discricionário; 3.4: caminho nomeação → posse → exercício com os relógios de 30 e 15 dias). Formato de entrada: `imagem` (data URI ≤ 150 KB, alt obrigatório, máx. 2 por tópico).
5. **Levas 2–4:** itens 4–6, 7–9 e 10–12, cada uma com triagem detalhada, produção, QA Opus e sim do Fundador.

## Linhas para o orquestrador (TAREFAS.md / DECISOES.md)

```
NOVA | T-152 | AGORA | Plataforma v17.3: Resumo visual de DA, leva 1 (itens 1, 2 e 3; 9 tópicos). Patch, template, prévia, gerador/fragmento resumo_visual_leva1.json, checa_resumo_visual.py v1.1, testes e QA Opus R1–R3 (APROVADO) em saida/plataforma/. PENDENTE: GBQ consolida o campo topicos[id].resumoVisual no pacote; correção do canon 3.1/3.4 (art. 169, § 4º; anotação do art. 21); publicação só com o sim do Fundador (v17.2 + v17.3 juntas). Próximas: levas 2 (itens 4–6), 3 (7–9) e 4 (10–12). | Cowork/Fable 28/10
NOVA | D-RESUMO-VISUAL-DA | 28/10/2026 | Fundador (28/10) | Os 16 resumos MapasPro de DA (marca do Fundador) entram na plataforma como "Resumo visual" por tópico, campo topicos[id].resumoVisual (formato v3, ESPEC_resumo_visual_DA_v3), estética traduzida ao sistema v0.2 (preto→tinta, amarelo→marcador, emoji→ícone SVG, etiqueta de probabilidade→contagem do corpus com fonte), infográficos em SVG/HTML, conteúdo canônico como base e blocos MapasPro só após triagem e QA normativo; ordem do edital em levas de três itens; publicação por leva com sim do Fundador. | Cowork/Fable
NOVA | D-V17-3-RESUMO-VISUAL | 28/10/2026 | Cowork, ratificação Presidência | v17.3 = v17.2 + Resumo visual (patch_v17_3_resumo_visual.py, 6 substituições). vResumoVer desvia para vResumoVisual quando o tópico tem resumoVisual; sem ele, a tela antiga continua. Regressão 0/0 nos dois estados antigos. | Cowork/Fable
```
