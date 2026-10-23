# Especificação do curso de Direito Administrativo na plataforma (formato v1)

19/10/2026 · sessão de design da plataforma (DPE-01), a pedido do Fundador ("deixar o layout e o design do curso de Direito Administrativo mais bonito e automatizar a criação").
Vale para os lotes D1 a D6 do módulo de Direito Administrativo (D-ESCOPO-3, D-DA-LOTES). A plataforma desenha o curso sozinha a partir deste formato; ninguém monta tela à mão.
Plataforma: v15.5 na prévia (laboratório), com o módulo Direito Administrativo e os componentes Base legal e Compare. A plataforma da candidata continua na v15.4 até o "sim" do Fundador.

## 1. Como a automação funciona
1. A Fábrica produz o lote no formato abaixo, com QA separado (gcb-cqfp e qa-normativo-da). Pela decisão do Fundador de 18/10, o curso também passa por um leitor externo (ChatGPT), que só lista o que falta.
2. O script de conferência (claude/kit_pacote/checa_pacote.py) recusa o pacote se algum ponto de formato ou de lei estiver fora da regra (seção 6).
3. A regressão (regressao_pacote.py) abre todos os cursos, resumos e blocos de questões e confere que cada tópico de Direito Administrativo ficou na matéria certa.
4. Revisão visual curta com a skill design-plataformas-interativas; painel de acompanhamento atualizado; publicação só com o "sim".

## 2. Identificadores
- Edital: `P1-DA-<número>`, como no Estado Canônico (ex.: `P1-DA-2.1`). O pacote traz as 46 entradas do edital de DA (12 itens e seus subitens; 37 itens-folha), `prova: "P1"`, texto literal do edital. A plataforma também aceita `DA-2.1`, mas o pacote usa um prefixo só.
- Questões: `itemEdital` com o id do edital acima. O prefixo do id da questão é livre; prefixo novo precisa entrar no script do painel.
- Lote: `itensEdital` só com ids de DA. Lote que mistura DA e outra matéria é recusado: os títulos do curso seriam ligados ao módulo errado.

## 3. Curso (campo `lotes[].curso`, texto)
Um bloco por subitem do edital, aberto por `## <número> <TÍTULO>` (ex.: `## 2.1 ATO ADMINISTRATIVO`). Dentro do bloco, uma linha só em maiúsculas abre um quadro, que vai até o próximo título:

| Linha | Vira | Para quê |
|---|---|---|
| `DEFINIÇÃO` | quadro amarelo | conceito em 2 ou 3 frases, com as palavras da banca |
| `BASE LEGAL` | quadro com barra lateral escura | dispositivo citado no texto (artigo, inciso), sempre conferido |
| `EXEMPLO PARLAMENTAR` | quadro cinza | caso ligado à Câmara dos Deputados |
| `PEGADINHA PROVÁVEL` | quadro com borda amarela | a troca que a banca faz |

Também viram componentes: tabela em Markdown (`| A | B |`, vira cartões no celular) e sequência `A → B → C` de 3 a 7 etapas curtas (até 48 caracteres cada), que vira fluxo numerado.

Ordem sugerida em cada subitem: 2 ou 3 parágrafos de abertura → DEFINIÇÃO → BASE LEGAL → explicação → EXEMPLO PARLAMENTAR → PEGADINHA PROVÁVEL. Parágrafos de até 4 frases.

## 4. Abertura visual do tópico (`pacote.topicos["P1-DA-2.1"]`)
```json
{"emUmMinuto": ["...", "...", "..."],
 "resumo": "...",
 "visuais": [ {"tipo": "compare", ...}, {"tipo": "baseLegal", ...} ]}
```
- `emUmMinuto`: 3 frases, cada uma com até cerca de 180 caracteres.
- `resumo`: um ou dois parágrafos, só com o que está no curso, de 150 a 250 palavras (decidido em 20/10/2026 por delegação do Fundador; é a faixa dos 40 resumos do pacote v1.12, mediana de cerca de 200 palavras).
- `visuais`: 1 ou 2 por tópico, do tipo que o conteúdo pede.

| Tipo | Campos | Quando usar em Direito Administrativo | Limites para caber no celular |
|---|---|---|---|
| `compare` (novo) | `titulo`, `a`, `b`, `linhas: [[aspecto, lado A, lado B]]`, `legenda` | pares que a banca troca: centralização × descentralização, concentração × desconcentração, anulação × revogação, dispensa × inexigibilidade | até 6 linhas; células de até cerca de 90 caracteres |
| `baseLegal` (novo) | `titulo`, `norma`, `dispositivos: [{ref, texto, literal, conferido}]`, `nota` | dispositivos centrais do tópico | até 4 dispositivos; `conferido` = data AAAA-MM-DD |
| `esquema` | `titulo`, `centro`, `ramos[]` | conceito e suas partes (requisitos, atributos, espécies) | 3 a 7 ramos curtos |
| `linha` | `titulo`, `marcos: [{quando, texto}]` | fases e prazos (processo administrativo, disciplinar, licitação) | prazos só do mapa normativo |
| `fluxo` | `titulo`, `passos[]` | procedimento em etapas | 3 a 7 passos de até 48 caracteres |
| `tabela` | `titulo`, `colunas[]`, `linhas[[]]`, `legenda` | comparação de 3 ou mais coisas | até 4 colunas |
| `barras` | `titulo`, `dados: [{rotulo, valor}]`, `unidade`, `fonte` | só com dado oficial e datado | fonte obrigatória |

## 5. Regras de lei (Base legal)
- Todo dispositivo vem do mapa normativo do lote, feito pelo qa-normativo-da no texto compilado oficial (despacho GCB/D6_despacho_GCB-CPP.md), com artigo, inciso, parágrafo e alínea.
- `literal: true` só para transcrição exata; o resto é `literal: false` (paráfrase), e a tela mostra "texto da lei" ou "paráfrase".
- `conferido` é obrigatório: sem data, o pacote é recusado.
- Redação dada por lei de 2025 ou 2026: marcar REVERIFICAR no relatório do lote (despacho da GCB).
- Vale a norma vigente na data que o edital fixa (despacho da GCB, edital 13.33); alteração posterior vai para o relatório, não para o texto.

## 6. O que o script recusa (bloqueio)
- Lote misturando DA com outra matéria; prefixos de edital de DA misturados; questões de DA sem entradas de edital.
- `compare` com linha que não tem 3 células; `baseLegal` sem `ref`, `texto` ou data de conferência.
- Visual sem campo obrigatório, de qualquer tipo (quebraria o curso do tópico na tela).
- Texto "[demonstração de formato]" no pacote.
- As regras gerais do roteiro de entrada: id sumido ou gabarito mudado sem registro, rótulo proibido e outras.

## 7. Demonstração na prévia
A prévia (laboratório) mostra três tópicos de demonstração: 1.2 com Compare e Base legal, 2.1 com esquema e 4.4 com linha do tempo. Os textos são marcados "[demonstração de formato]", e há um aviso vermelho em cada tela. A demonstração some sozinha quando o pacote traz DA de verdade, e o embute_pacote.py a desliga em toda cópia para publicação.

## 8. Classificação
AGORA: componentes e módulo na prévia; esta especificação; conferência estendida. PRÓXIMO: a Fábrica aplicar o formato aos lotes de DA (ordem ORDEM_DA_FORMATO), começando pelos já canônicos (D6 e D1); publicar na plataforma da candidata com o primeiro lote aprovado e o "sim". BACKLOG: figuras desenhadas pela CII para tópicos em que esquema e Compare não bastem.
