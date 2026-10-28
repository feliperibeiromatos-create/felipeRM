# Produção — Resumo visual de Direito Administrativo, leva 2 (itens 4.1–4.4, 5.1, 5.2, 6.1–6.5) — 28/10/2026

Cowork (Fable 5.1), produção integrada. Continuação de producao_v17_3_resumo_visual_leva1 (T-151/T-152). Autorização: "Dou SIM para fazer todos os tópicos de Direito Administrativo" (Fundador, 28/10/2026). QA: Opus (qa-normativo-da + gcb-cqfp-didatico + QA-plataforma), três rodadas no mesmo dia. Veredito final: APROVADO (R3).

## 1. O que foi feito
- 11 tópicos, 129 blocos, gerados por resumo_visual_leva2.py sobre o canon do pacote v1.14 (canon_leva2_dump.txt) e os extras conferidos (extras_leva2_v114.json), contrato v3.1 da ESPEC. Fontes MapasPro: Lei do Processo Administrativo, Poderes Administrativos, Responsabilidade Civil do Estado e a parte disciplinar da Lei 8.112 — triagem em TRIAGEM_resumos_MapasPro_DA_leva2_2026-10-28.md. Insumo consultivo: Conferencia_Dirigida_DAD_Leva2 (ChatGPT), despachada em DESPACHO_conferencia_leva2.
- Pacote de prévia pacote_previa_v114_rv2.json = pacote v1.14 do ar + resumoVisual dos 9 tópicos da leva 1 (aprovados e publicados) + os 11 da leva 2. Template v17.3 (11b99a41…) inalterado: só o pacote muda.
- Cobrança (corpus 2025 / fila 2024 heurística): 4.1: 0/0 ("nenhuma questão enquadrada"); 4.2: 27/11; 4.3: 16/2; 4.4: 56/37; 5.1: 32/30; 5.2: 7/0; 6.1: 19/19; 6.2: 8/0; 6.3: 4/4; 6.4: 5/0; 6.5: 5/7.

## 2. Rodadas de QA (28/10/2026)
- R1 — REPROVADO. 1 BLOQUEIA (N1: a produção repetiu o parecer do ChatGPT e pôs a consulta pública no art. 32 da Lei 9.784; o texto oficial da Câmara traz consulta pública no art. 31 e audiência pública no art. 32), 12 CORRIGIR (N2 tese do Tema 592 não literal; N3 ordem de polícia indelegável, Inf. 996; N4 leitura do STJ, MS 18.327, não conferível — retirada; N5 função comissionada não está no art. 135; N6 art. 133, § 5º, opção = boa-fé e pedido de exoneração, não "arquivamento"; N7 defesa e julgamento em 5 dias no rito sumário; N8 art. 156, § 1º; N9 "salvo disposição legal diversa" no art. 57; D1 excesso de poder convalidável, coerência com 2.1; D2 triagem × JSON sobre a forma omissiva do abuso; D3 cassação e destituição fora da gradação da escala; I1 checador sem os termos vedados da leva 2), 9 SUGESTÃO (N10 art. 142, §§ 3º e 4º; N11 Temas 940 e 130 — lacuna do canon; N12 arts. 56, § 1º, e 59, § 1º; N13 art. 12 completo; D4, D5, I2, I3, I4), 2 de processo (P1: "conferido" só com o trecho literal; P2: a Lei 8.112 pode ser aberta na Câmara por download direto). O QA abriu o texto atualizado completo das Leis 8.112 e 9.784 e conferiu artigo a artigo os 22 dispositivos que a produção não tinha conseguido abrir.
- R2 — APROVADO COM CORREÇÕES. Todas as obrigatórias e as sugestões N10, N12, N13, D4, D5 aplicadas e conferidas pelo QA no diff; restaram I5 (o checador v1.2 poupava `errado` e `fontes` de TODOS os controles — deve poupar só dos VEDADOS), D6 (`fontes` visíveis à candidata com jargão interno) e I6 (capturas gravadas com os ids errados), mais D7 (ilustração "cinco degraus") e N14 (Súmula 635 do STJ, não conferível).
- R3 — APROVADO. I5, D6, I6, D7 conferidos; diff R2→R3 só em `fontes` e na nota de ilustração; mutação de 34 casos (os 8 da R2 bloqueiam; 20 dos 22 da R1 bloqueiam, 2 avisam por desenho; a tese correta com aspas tipográficas passa). Duas ressalvas de redação das `fontes` (SV 5 não é "texto da Câmara"; CF/CTN/Lei 6.830 do pacote, conferência de 20/10) corrigidas pela produção após a R3 — alteração só em `fontes`, regressão rerodada (0 não esperadas, 0 JS).
- Relatórios: QA_resumo_visual_leva2_R1/R2/R3_2026-10-28.md.

## 3. Correções de direito que a leva 2 fez ao material de origem (para a GCB e para o canon)
Consulta pública = art. 31 e audiência pública = art. 32 da Lei 9.784 (o parecer do ChatGPT e o despacho diziam "art. 32, consulta pública"; despacho corrigido). Tema 532: tese literal do portal; o STF (Inf. 996) considera a ordem de polícia a única fase absolutamente indelegável; consentimento, fiscalização e sanção são delegáveis nas condições da tese. Tema 592: tese literal "do seu dever … art. 5º, inciso XLIX". Destituição de função comissionada: art. 127, VI, sem regra no art. 135. Rito sumário (art. 133): defesa em 5 dias (§ 2º), julgamento em 5 dias (§ 4º), opção até o fim da defesa = boa-fé e pedido de exoneração (§ 5º). Art. 156, § 1º: o presidente pode denegar pedidos protelatórios. Art. 57: "salvo disposição legal diversa". Art. 142, §§ 3º e 4º: interrupção da prescrição. NÃO entraram, por falta de conferência em fonte oficial (portal do STJ recusa o ambiente): STJ, EDcl no MS 18.327/DF (prescrição da destituição: 2 ou 5 anos) e Súmula 635 do STJ (prescrição volta a correr após 140 dias); Temas 940 e 130 do STF são lacunas do canon (não do visual). Tudo isso vai à GCB como PRÓXIMO, nas fases já abertas (T-136/T-137).

## 4. Ferramentas
- checa_resumo_visual.py v1.2: VEDADOS da leva 2 (mais de sessenta dias; até/no máximo dez testemunhas; apenas/só consentimento e fiscalização; art. 2º, XIV–XXI; art. 32 ↔ consulta pública e art. 31 ↔ audiência pública nas duas ordens; Sistema S ↔ delegação; art. 150 ↔ impedimentos; art. 132 parágrafo único; doze princípios; ordem/sanção de polícia delegável); lista TESES (532 e 592, literais, com normalização de aspas) que bloqueia qualquer "Tese: …" divergente; avisos "marco sem quando" e "box sem rótulo"; walk() devolve (chave, string) e só a lista VEDADOS poupa `errado` e `fontes`; padrão de sigla sem re.I. Leva 1 continua 0/0.
- t_janela20.js: o caso 0.const aceita v17.2 ou v17.3.
- Capturas: testes_v17_3/caps_l2r3/ (22 PNG, 0 erros JS).

## 5. Entregáveis finais (sha256)
- resumo_visual_leva2.py 81822540f19929b2be05a5a90ff1bdee1c4c9c73e6acaf414942de598318c13e
- resumo_visual_leva2.json bfe804d87bc5fe6c6f40afeccea50ca346dfbfe62a5c14daa04890c7ef794105
- pacote_previa_v114_rv2.json b4437cd97316031b63041e77449eeb7ea16a65559787c50053635f13d7eac2f2 (20 tópicos com resumoVisual)
- plataforma_v17_3_previa_leva2.html 0838e9e2cfbbe2374fd0c0b6d571b9319093132a58fbb00d9f060ac46edc9aa2 (3.296.374 bytes; template 11b99a41…)
- checa_resumo_visual.py 43ed8198dd940474852783a012b7d35afb838242ef2c0857ea2b6f869168ecfe
- extras_leva2_v114.json 5471832c…, canon_leva2_dump.txt 130315f6…, diff_leva2_R1_R2.txt, resumo_visual_leva2_r1.py.bak (gerador da R1, para auditoria).
- Testes após a última alteração: checa 0/0 (leva 2 com --pacote; pacote rv2 inteiro; leva 1); regr_v17_3.js (prévia leva 1 × prévia leva 2, estados antigo e antigo2): 104/110 telas, 20 RV, 11 mudanças esperadas, 0 não esperadas, 0 erros JS; t_janela20 0 falhas; t_pir 0 falhas.

## 6. Publicação
A leva 2 está pronta para publicar pelo rito do T-152 (strip do esqueleto; serviço adiciona; conferência por bytes). Pendente: "sim" do Fundador para a publicação (matéria reservada: o que é compartilhado com a candidata e quando). Proposta: publicar a leva 2 agora (v17.3, pacote v1.14 + levas 1 e 2) ou junto com a leva 3 — à escolha do Fundador. Classificação: AGORA.

## 7. Próximos
Leva 3 (itens 7, 8.x; Controle como insumo de 11) — AGORA, mesma rotina (triagem → geração → checa → prévia → regressão → QA Opus). Leva 4 (10.x, 11, 12) — PRÓXIMO. GCB: lacunas da seção 3 — PRÓXIMO. Ilustrações — BACKLOG (decisão do Fundador).
