# QA_T111_P1_parte2_R1_2026-10-18_gcb-cqfp.md — T-111 (A2), QA R1 dos resumos de 16 tópicos de P1 — 2026-10-18 — gerado por gcb-cqfp

Objeto: saida/gcb/T111_resumos_P1_parte2_v1.md (gcb-cpp). Normas: saida/gcb/V15_BAEF_D1_GCB_2026-10-18.md (seção 0, regras 1 a 3, 5 e 7; seção 3, regra de tamanho, forma e QA da A); ordens/ORDEM_V15_A_RESUMOS.md (e). Calibração: saida/gcb/QA_T111_P1_parte1_R1_2026-10-18_gcb-cqfp.md (duas ideias distintas no mesmo parágrafo, sem frase de contraste, quando o limite de parágrafos deixa espaço → CORRIGIR).
Base: saida/pacote/pacote.json v1.11 (idêntico byte a byte a saida/pacote/gerador_v1_11/out/pacote.json, conferido com cmp). Blocos segmentados por script próprio (`python -I`), separando `lotes[].curso` nas seções `## `, nos lote#bloco da seção 2 de saida/pacote/V15_BAE_D1_GBQ_2026-10-18.md. Li por inteiro o curso de cada tópico e o resumo correspondente do bloco json. Contagens, varredura e textos corrigidos foram refeitos por script. Somente leitura; nenhum arquivo foi alterado além deste.

## 1. Veredito

**Parte A2: CORRIGIR.** Resultado: 8 APROVADOS, 8 CORRIGIR e 0 REPROVADOS. Reprovados: 0% (0/16). Com ajuste: 50% (8/16).
Fidelidade: nenhum fato novo e nenhuma contradição com o curso nos 16 tópicos. Todos cumprem a regra de tamanho, inclusive a exceção de P1-1 e P1-3. A tecla F4 está intacta.
O que se corrige:
- um parágrafo por ideia: P1-2, P1-2.1, P1-3, P1-4 e P1-5.3;
- precisão de condição: P1-4.1;
- data de fato de ferramenta: P1-8.3;
- citação normativa sem artigo: P1-6.
A R2 confere só esses 8 tópicos.

## 2. Pontos levantados pela produtora

- **"versão/versões" (P1-1, §7; P1-4.1, §3): uso de domínio, não é marca de produção.** Em P1-1, o trecho "Restaurar uma versão não apaga a atual" vem do histórico de versões do OneDrive (curso L6A#4, 1.4.3). Em P1-4.1, "histórico de versões" é a condição para a sincronização servir de backup (curso L6B#3, 4.1.2). Nenhum dos dois fala de versão do material. Exceção admitida.
- **P1-6, texto normativo.** Todo dispositivo do resumo está no mapa normativo do curso (L4#3, 6.3), e nenhum artigo, inciso ou prazo foi acrescentado. A ANPD aparece com o nome por extenso.
  - Problema: o v1 cita a LGPD, a LAI, a Lei 8.112/1990, o Decreto 1.171/1994 e o Código de Ética sem artigo. Pelo checklist desta coordenação, citação de lei sem artigo fica PENDENTE no normativo.
  - Correção: o texto da seção 4 coloca o artigo que o próprio curso traz, sem fato novo e dentro do limite de 220 palavras.
  - qa-normativo: não precisa ser rodado de novo. Os dispositivos são os que o curso já registra como conferidos no Planalto em 07/10/2026 e 08/10/2026, e há o QA normativo da LGPD de 10/10/2026 (saida/banco/qa_normativo_lgpd_2026-10-10.md).
  - Decisão: P1-6 sai de PENDENTE no normativo quando o v2 trouxer os artigos.
- **F4 (P1-1, §4):** "A tecla F4 alterna entre os tipos", como manda a regra 0.3. Intacta.

## 3. Tabela de pareceres

| Tópico | Bloco | Palavras | % do curso | Parágrafos (palavras) | Parecer | Motivo |
|---|---|--:|--:|---|---|---|
| P1-1 | L6A#0–#4 | 274 (≤300) | 9,5% | 7 (51, 43, 30, 44, 37, 35, 34) | APROVADO | Exceção cumprida: 7 parágrafos, cada subitem com pelo menos um. Agrupar por aplicativo é a única forma possível com o teto de 7 parágrafos. |
| P1-2 | L6B#0 | 181 | 19,1% | 5 (33, 36, 42, 39, 31) | CORRIGIR | O §3 junta o modelo cliente-servidor/par a par (2.0.3) e os equipamentos switch/roteador (2.0.4). |
| P1-2.1 | L6B#1 | 209 | 21,3% | 5 (37, 46, 22, 51, 53) | CORRIGIR | O §5 junta VPN (2.1.4) e DNS/pharming (2.1.5). |
| P1-3 | L6A#5–#8 | 213 (≤300) | 10,7% | 6 (28, 28, 35, 40, 26, 56) | CORRIGIR | O §6 junta definição e uso do Meet com a apresentação de tela, havendo espaço até 7. No §3, o "segundo a Microsoft" alcança também Para/Cc, que no curso é conceito geral, sem fonte. |
| P1-4 | L6B#2 | 109 | 39,1% | 3 (46, 29, 34) | CORRIGIR | O §3 junta engenharia social (4.0.1) e governança digital (4.0.2). A expressão "como conceito geral" é anotação de procedência do curso, não texto para a candidata. |
| P1-4.1 | L6B#3 | 206 | 11,1% | 5 (35, 60, 43, 44, 24) | CORRIGIR | "salvo com histórico de versões" enfraquece a condição do curso, que exige "HISTÓRICO de versões e retenção". |
| P1-4.2 | L6B#4 | 152 | 20,2% | 4 (42, 40, 29, 41) | APROVADO | Fiel. A pegadinha central (troca antivírus × firewall) está coberta. |
| P1-4.3 | L6B#5 | 219 | 19,2% | 5 (43, 41, 42, 46, 47) | APROVADO | Fiel: Cartilha do CERT.br com data, pharming como tipo de phishing, limites do HTTPS. |
| P1-5.1 | L4#0 | 178 | 15,7% | 4 (55, 22, 50, 51) | APROVADO | Os §3 e §4 ficam cada um dentro de uma subseção do curso (5.1.3 técnicas; 5.1.4 parâmetros e limites). Entrada × parâmetros coberto. |
| P1-5.2 | L4#1 | 203 | 17,6% | 5 (47, 25, 45, 55, 31) | APROVADO | Fiel. Clustering × classificação, "não supervisionado ≠ sem humano" e pré-treino sem rótulos cobertos. "Auto-supervisionado" não aparece. |
| P1-5.3 | L4#2 | 218 | 20,3% | 5 (36, 51, 43, 49, 39) | CORRIGIR | O §5 junta o conhecimento paramétrico (5.3.3) com usos e riscos (5.3.4). |
| P1-6 | L4#3 | 219 | 10,1% | 6 (32, 33, 38, 48, 36, 32) | CORRIGIR | Citação de lei sem artigo (normativo PENDENTE). Data entre parênteses fora de texto corrido. "O Capítulo IV trata do Poder Público, inclusive o Legislativo" atribui ao capítulo o que o curso apoia no art. 1º, caput. |
| P1-7.1 | L5#0 | 177 | 22,8% | 5 (39, 36, 38, 23, 41) | APROVADO | Fiel. Escalas, discreto × contínuo, atributo × métrica, limpeza × transformação e ETL × ELT cobertos. |
| P1-8.1 | L5#1 | 105 | 34,5% | 3 (28, 50, 27) | APROVADO | Fiel. A ordem de precisão (posição > comprimento > ângulo > área > volume/cor) está correta. Barras a partir de zero e funções das paletas cobertas. |
| P1-8.3 | L5#3 | 190 | 17,4% | 5 (35, 50, 35, 37, 33) | CORRIGIR | O §5 traz fato de ferramenta datado (edição sem custo; Data Studio Pro paga) sem a data que o curso traz (regra 0.5). "distinta" fica sem complemento. |
| P1-8.4 | L5#4 | 83 | 34,0% | 3 (34, 21, 28) | APROVADO | Fiel. Mensagem central, storytelling ≠ dashboard e exploratória × explanatória cobertos. |

Critério de "um parágrafo por ideia", aplicado do mesmo modo nos 16 tópicos:
- Um parágrafo pode juntar frases de uma mesma subseção do curso que formem um só contraste ou um só tema.
- Ideias de subseções diferentes, sem frase de contraste, vão para parágrafos separados, desde que o limite de parágrafos deixe espaço.
- P1-1 está no teto de 7 e por isso não se divide.

Forma, conferida nos 16 tópicos:
- prosa corrida, sem lista, tabela ou negrito;
- nenhuma linha começa com número ou com rótulo em maiúsculas seguido de dois-pontos;
- nenhuma quebra simples de linha;
- bloco json com 16 chaves na ordem do edital, só com o campo `resumo`.

## 4. Correções exigidas (texto exato, para o _v2)

No json, a quebra de parágrafo é `\n\n`. Nada fora do indicado muda.

**P1-2.** No §3, trocar "…ao mesmo tempo. O switch interliga…" por "…ao mesmo tempo.\n\nO switch interliga…". Fica com 6 parágrafos (33, 36, 24, 18, 39, 31) e 181 palavras.

**P1-2.1.** No §5, trocar "…de fora da organização. O DNS permite…" por "…de fora da organização.\n\nO DNS permite…". Fica com 6 parágrafos (37, 46, 22, 51, 22, 31) e 209 palavras.

**P1-3.**
- (a) No §3, trocar "…pelos outros destinatários; em Para e Cc, os endereços aparecem para todos." por "…pelos outros destinatários. Em Para e Cc, os endereços aparecem para todos."
- (b) No §6, trocar "…e acessada pelo link. Ao apresentar, …" por "…e acessada pelo link.\n\nAo apresentar, …".

Fica com 7 parágrafos (28, 28, 35, 40, 26, 37, 19), dentro da exceção, e 213 palavras.

**P1-4.** Substituir o §3 inteiro por dois parágrafos:

> A engenharia social manipula pessoas, e não máquinas, para obter informação ou acesso.
>
> Em sentido amplo, a governança digital reúne políticas, responsabilidades, processos e controles para dirigir o uso da tecnologia e dos dados.

"Em sentido amplo" vem de "no sentido amplo do edital" (L6B#2, 4.0.2). Fica com 4 parágrafos (46, 29, 13, 21) e 109 palavras (39,1%).

**P1-4.1.** No §3, trocar "salvo com histórico de versões." por "salvo com histórico de versões e retenção." (L6B#3, 4.1.2: "só funciona como backup se houver HISTÓRICO de versões e retenção"). Fica com 5 parágrafos (35, 60, 45, 44, 24) e 208 palavras.

**P1-5.3.** No §5, trocar "…e não consulta a internet. Os usos incluem…" por "…e não consulta a internet.\n\nOs usos incluem…". Fica com 6 parágrafos (36, 51, 43, 49, 18, 21) e 218 palavras.

**P1-6.** Substituir o resumo inteiro por:

> Ética digital aplica os deveres éticos do servidor ao ambiente digital; com meios digitais, inclusive com IA, a ferramenta não responde: o agente público responde.
>
> Os princípios do art. 37, caput, da Constituição são a base. O Decreto 1.171/1994 (Anexo, Seção I, inciso II), norma do Executivo federal, mostra que a ética vai além da legalidade; na Câmara, o regime do servidor é a Lei 8.112/1990.
>
> A LGPD vale para pessoas de direito público ou privado, inclusive o Legislativo (art. 1º, caput). Opinião política e filiação sindical são dados sensíveis (art. 5º, II), e o dado anonimizado não é pessoal, salvo se revertido (art. 12).
>
> O consentimento não é a única base legal, nem a principal para o Poder Público (art. 7º). O titular pode pedir revisão de decisão automatizada (art. 20), não necessariamente por pessoa natural. Incidente de segurança é comunicado à Agência Nacional de Proteção de Dados (ANPD) e ao titular (art. 48).
>
> Na LAI, a publicidade é a regra e o sigilo, a exceção (art. 3º, I). A Lei 8.112/1990 impõe sigilo sobre assunto da repartição (art. 116, VIII) e responsabiliza o servidor civil, penal e administrativamente (art. 121).
>
> O mesmo decreto veda deixar de usar os avanços técnicos (inciso XV, alínea e); a conduta correta é usar IA em canais autorizados, com revisão humana.

Fica com 6 parágrafos (25, 41, 39, 50, 37, 27) e 219 palavras (10,1%).

Rastreio de cada dispositivo ao bloco L4#3:
- art. 37, caput: 6.1;
- Decreto, Seção I, II: 6.1 e 6.3;
- Lei 8.112 como regime da Câmara: 6.1;
- LGPD art. 1º, caput, e o Legislativo: 6.3 e pegadinha P2;
- art. 5º, II: 6.3 e P8;
- art. 12: 6.3 e P1;
- art. 7º, "não é a única nem a principal": 6.3, chave de prova;
- art. 20, texto vigente sem "por pessoa natural": 6.3 e P3;
- art. 48: 6.3;
- LAI art. 3º, I: 6.3 e P4;
- Lei 8.112 arts. 116, VIII, e 121: 6.3;
- Decreto, inciso XV, alínea "e": 6.3 e 6.4, item 5;
- conduta correta: 6.4, item 5.

Mudanças em relação ao v1:
- Saíram "o Capítulo IV trata do Poder Público" (redundante com o art. 1º) e "Atos oficiais não têm proteção autoral" (pegadinha secundária, P9). Os dois cortes abrem espaço para os artigos sem passar de 220 palavras.
- Saiu a data entre parênteses "(conferido em 07/10/2026)". O resumo já não repete a história da MP 869/2018, que é o fato datado; afirma só o texto vigente, que o curso registra.

**P1-8.3.** Substituir o §5 por:

> Segundo o Google Cloud, verificado em 8/10/2026, a edição Data Studio é sem custo e existe a edição paga Data Studio Pro; por isso não basta dizer que é gratuito. O Looker é uma plataforma de inteligência de negócios distinta do Data Studio.

Fica com 5 parágrafos (35, 50, 35, 37, 43) e 200 palavras (18,3%).

Depois das correções, a gcb-cpp atualiza no _v2 as contagens e o rastreio dos 8 tópicos. Nenhuma outra mudança.

## 5. Varredura (regra 0.7), repetida por esta coordenação

Regex própria sobre os 16 resumos: as 10 categorias, mais "conceito geral" e marcas de linha.
- Exceções de domínio confirmadas:
  - "F4" em P1-1 (regra 0.3);
  - "versão" em P1-1 e "versões" em P1-4.1 (seção 2);
  - "instrução/instruções" em P1-5.1 (vocabulário de prompt);
  - "Difere do dashboard" em P1-8.4 (contraste de domínio, não é "Difere do item").
- Falsos positivos da regex: "conversas" em P1-3 e "diverso" em P1-5.3.
- Ocorrência a corrigir: "como conceito geral" em P1-4 (seção 4).

Fora isso, zero ocorrências: nada de "lote", códigos de item, par ou fonte, etiquetas, TC/IC/GI/AT, QA, errata, "curso", "pegadinha" ou códigos de tópico.

## 6. Evidência (checklist 3): três fontes citadas, abertas nesta revisão (18/10/2026)

1. IETF, RFC 1918 (https://www.rfc-editor.org/rfc/rfc1918), seção 3: os três blocos 10/8, 172.16/12 e 192.168/16 batem com P1-2, §4. Confirmada.
2. Google for Developers, "Introduction to ML: What is Machine Learning?" (https://developers.google.com/machine-learning/intro-to-ml/what-is-ml): estão lá as quatro categorias "based on how they learn" e "generative models are initially trained using an unsupervised approach". Bate com P1-5.2, §1 e §5. Confirmada.
3. Google Cloud, Data Studio (https://docs.cloud.google.com/data-studio, página de entrada):
   - confirmados: "Looker Studio is now called Data Studio", "no-cost tool" e a existência do Data Studio Pro (P1-8.3, §4 e §5);
   - não confirmado: esta página não traz o mês da volta do nome (abril de 2026).
   O resumo atribui o mês ao "Google Cloud", como o curso, que cita a página "Welcome", as notas de versão de 16/04/2026 e o Google Cloud Blog de 10/04/2026. A data é a do curso e está correta como data de verificação. Fica o registro de que a página de entrada não sustenta o mês sozinha; não há reprovação.

Checklist sem objeto nesta parte: não há itens AUTORAL nem [TS], e o estilo Cebraspe não se aplica a resumo.

## 7. Encaminhamento

- A gcb-cpp grava saida/gcb/T111_resumos_P1_parte2_v2.md só com as correções da seção 4.
- A R2 (saida/gcb/QA_T111_P1_parte2_R2_2026-10-18_gcb-cqfp.md) confere apenas os 8 tópicos com CORRIGIR, as contagens e a varredura.
- Os 8 tópicos APROVADOS seguem como estão no v1.
