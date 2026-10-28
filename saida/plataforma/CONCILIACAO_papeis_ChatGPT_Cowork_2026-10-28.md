# Conciliação dos papéis — ChatGPT × Cowork (fábrica Claude) — 28/10/2026

Cowork (Fable 5.1), 28/10/2026, a partir da recomendação Cowork (AVALIACAO_pacote_ChatGPT_resumos_DAD_2026-10-28.md) e da recomendação do ChatGPT transportada pelo Fundador em 28/10. As duas convergem; este documento registra a divisão conciliada, o texto da decisão para o Fundador ratificar e o que já foi preparado.

## 1. Divisão conciliada (idêntica nas duas recomendações)

| Quem | Papel | Entrega | Quando |
|---|---|---|---|
| ChatGPT (chat do Fundador) | Segunda leitura dos PDFs MapasPro da leva: conferência normativa dirigida e análise didática; propostas visuais justificadas; SVG sob encomenda | Achados com documento + página física, fonte oficial, data, correção proposta, destino no edital e **estado** (seção 3) | Antes da produção da leva; SVG quando o Cowork indicar necessidade concreta (tópico, objetivo, espaço, formato) |
| Cowork / Fable (fábrica) | Triagem própria, autoria e integração no contrato `resumoVisual` v3.1, patch, prévia, testes de produção, conferência em fonte oficial dos achados aceitos | Fragmento JSON, template/prévia, relatório de produção com hashes | Após receber os achados do ChatGPT (ou após prazo combinado, com registro do que não chegou) |
| GBQ / Secretaria de Estado Canônico | Consolidar o campo `resumoVisual` no pacote, corrigir o canon na origem (T-153), reconciliar contagens (T-155) | Pacote consistente | Antes de cada build de publicação |
| QA Opus (modelo distinto) | QA independente do resultado: normativo, didático, interface, regressão | Relatórios R1…Rn com veredito | Após a produção; defeitos voltam ao produtor |
| Fundador | Direção: prioridades, estética, autorização de publicação, transporte entre chats | "sim" por leva | — |

Diferenças entre as duas recomendações: nenhuma de substância. A do Cowork previa também uma leitura externa opcional do JSON final pelo ChatGPT; a do ChatGPT concentra a leitura antes da produção. Conciliação: a leitura prévia é a regra; a leitura do JSON final é opcional, a pedido do Fundador, e nunca substitui o QA Opus (SEPARAÇÃO). O ChatGPT não produz conteúdo integrado nem código da plataforma.

## 2. Texto da decisão — versão de consenso — RATIFICADA pelo Fundador em 28/10/2026 ("Dou SIM"); lançada em DECISOES.md como D-PAPEIS-IA-RESUMOS. Pendente: Presidência redige a regra comum v2.2.

```
NOVA | D-PAPEIS-IA-RESUMOS | (Fundador, __/10/2026) Para os Resumos visuais de DA (D-RESUMO-VISUAL-DA): a produção integrada (redação, componentes, patch, testes, preparação da publicação) fica na fábrica (Cowork/Fable); o QA formal independente fica com o Opus, com veredito ligado aos arquivos examinados; a GBQ/Secretaria de Estado Canônico corrige na origem, consolida o pacote e reconcilia contagens; o Fundador dirige (estética, prioridades, autorização de publicação). O ChatGPT, no chat do Fundador, atua em apoio consultivo e delimitado: segunda leitura normativa e didática de pontos definidos, pesquisa de fontes e recursos visuais (SVG) sob encomenda. Cada pedido ao ChatGPT traz objeto, versão, dúvida concreta e formato esperado; cada achado volta com evidência (fonte oficial, data) e estado (confirmado em fonte primária / atualização posterior / síntese doutrinária / hipótese pendente); quem produz decide a incorporação, sempre após conferência em fonte oficial, e o QA Opus continua sendo o único portão. Não há etapa externa obrigatória por leva: a segunda leitura é acionada quando trouxer benefício concreto (divergência, mudança jurídica relevante, dificuldade didática); sua ausência não trava a leva. Exceção expressa e limitada à regra comum "tudo roda exclusivamente em Claude" (v2.1), que a Presidência redige na v2.2.
```

## 3. Estados dos achados (adotados na ESPEC v3.1, regra 11)

- **Confirmado em fonte primária** — texto da norma/tese lido em fonte oficial, com data; pode entrar.
- **Atualização posterior** — a norma mudou depois do PDF (ex.: EC 138/2025); entra com a redação nova e sem chamar a antiga de erro.
- **Síntese doutrinária** — classificação ou posição majoritária; entra só rotulada ("doutrina", "classificação doutrinária").
- **Hipótese pendente** — ainda sem fonte primária lida; não entra na plataforma até ser confirmada.

Convergência entre dois modelos não é prova: o estado só sobe a "confirmado" com a leitura da fonte.

## 4. Contagens (T-155, GBQ)

As etiquetas de cobrança usam `banco/candidatos/resumo_por_item_edital_v2.csv` (candidatos; certo_errado). O ChatGPT reportou 3/30/75 para 1, 1.1 e 1.2 ("aderência integral"); a ESPEC usou 3/33/79 do CSV. A GBQ define o critério único (integral × parcial; principal × secundário; agregação dos itens pais) e republica o CSV com a coluna do critério antes da leva 2. Até lá, a etiqueta cita o CSV v2 como está, com a fonte.

## 5. Leva 2 (itens 4, 5 e 6) — delimitação e pedido delimitado ao ChatGPT (consenso: conferir achados pendentes, não triagem integral)

Tópicos (ids do pacote v1.14; contagem do CSV v2 = candidatos / C-E):
- P1-DA-4 Direito administrativo disciplinar; 4.1 Fontes e princípios (sem candidato no CSV); 4.2 Ilícito de direito administrativo disciplinar (27/23); 4.3 Procedimentos disciplinares (16/13); 4.4 Processo Administrativo Federal, Lei 9.784/1999 (56/47).
- P1-DA-5 Poderes administrativos; 5.1 Discricionário, hierárquico, disciplinar, regulamentar e de polícia (32/28); 5.2 Uso e abuso do poder (7/3).
- P1-DA-6 Responsabilidade civil do Estado; 6.1 no direito brasileiro (19/14); 6.2 ato comissivo (8/6); 6.3 omissão (4/3); 6.4 requisitos (5/4); 6.5 excludentes e atenuantes (5/4).

PDFs MapasPro da leva: LEI 8.112-90 (R04, pp. 21–35: deveres, proibições, responsabilidades, penalidades, sindicância e PAD → 4.1–4.3); LEI DO PROCESSO ADMINISTRATIVO (R01 → 4.4); PODERES ADMINISTRATIVOS (R16 → 5.1, 5.2); RESPONSABILIDADE CIVIL DO ESTADO (R11 → 6.1–6.5). Achados anteriores pertinentes (triagem ChatGPT de 28/10): N13 (9.784: âmbito, arts. 44 e 56, § 1º, inexistente "art. 2º, XXI"), N19 (Tema 532), N20 (Tema 592; omissão), e os "sinais para revisão" sobre autoexecutoriedade e solidariedade. Regras que valem: ESPEC_resumo_visual_DA_v3_2026-10-28.md (v3.1), seções 3 e 5; conteúdo canônico do pacote v1.14 como base; nada de etiqueta de probabilidade; nenhum recado de produção no texto da candidata.

## 6. Pendência que fica visível (apontada pelo ChatGPT, correta)

A T-153 (correção na origem do canon de 3.1 — CF, art. 169, § 4º — e de 3.4 — anotação do art. 21) está ABERTA, classificada AGORA, a cargo da GBQ; o Resumo visual publicado já sai corrigido, mas o curso em prosa e o resumo antigo continuam com o texto anterior até a GBQ corrigir o pacote. Fecha quando o pacote consolidado for publicado.
