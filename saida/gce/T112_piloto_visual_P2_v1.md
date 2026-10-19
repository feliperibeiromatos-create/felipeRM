# T112_piloto_visual_P2_v1.md — T-112 (E) — piloto visual de P2 (P2-1.4 e P2-2.5) — ciclo 2026-10-18 s14c3 — gerado por gce-cpp

**Leituras.** `saida/gce/V15_BAEF_D1_GCE_2026-10-18.md` (seção 3), `ordens/ORDEM_V15_E_PILOTO_VISUAL.md`, `saida/pacote/V15_BAE_D1_GBQ_2026-10-18.md` (seções 1 e 2). Base de conteúdo: `lotes[].curso` da v1.11 (`saida/pacote/pacote.json`): P2-1.4 = bloco L1#3 + L1C; P2-2.5 = bloco L2#4. Nada fora do curso; sem `resumo` (frente A).

**Tipos.** P2-1.4: fluxo, tabela, esquema. P2-2.5: tabela, esquema. Tipo `barras` não usado (os blocos não trazem série numérica oficial com órgão e data). Tipo `linha` não usado (sem marcos datados).

**Contagens (script).** emUmMinuto: 3 por tópico; palavras por ponto: P2-1.4: 25, 27, 22 (máx. 30); P2-2.5: 20, 27, 21 (máx. 30). Passos do fluxo: 5 (máx. 7; maior 46 caracteres, limite 48). Tabelas: 1.4 = 3 colunas x 3 linhas; 2.5 = 3 colunas x 5 linhas; todas as linhas com o número de colunas; maior célula dentro de 80 caracteres. Esquemas: 4 ramos cada, todos com até 60 caracteres. Tipos distintos dentro de cada tópico.

## Relatório de sustentação (string, bloco, frase do curso)

### P2-1.4 (blocos L1#3 e L1C)

| String | Sustentação no curso |
|---|---|
| emUmMinuto 1 | L1#3, Definição: "responde a 'quem falou quando': segmenta o áudio em trechos e atribui a cada trecho um rótulo de locutor genérico"; "SEM dizer quem são" |
| emUmMinuto 2 | L1#3: "Identificação de locutor: diz QUEM é, comparando a voz com um banco de vozes cadastradas"; "Verificação de locutor: confirma se a voz é de UMA pessoa específica alegada (1 para 1)" |
| emUmMinuto 3 | L1#3: "'diarização em streaming' não é regra geral nem impossibilidade geral — depende do serviço"; "Limitações recorrentes: fala sobreposta (apartes), locutores com vozes parecidas" |
| fluxo, 5 passos | L1#3: "Etapas típicas: detecção de atividade de voz (VAD) → segmentação → extração de 'embeddings' de voz por segmento → agrupamento (clustering) dos segmentos por semelhança de voz → rotulagem" (ordem preservada) |
| tabela, linha Diarização | L1#3: "Diarização: separa os locutores, SEM dizer quem são"; "quem falou quando" |
| tabela, linha Identificação | L1#3: "diz QUEM é, comparando a voz com um banco de vozes cadastradas (precisa de cadastro prévio)" |
| tabela, linha Verificação | L1#3: "confirma se a voz é de UMA pessoa específica alegada (1 para 1), como em autenticação"; a pergunta "É a pessoa alegada?" reformula "pessoa específica alegada" |
| tabela, legenda | L1#3: "A diarização pode ser ligada à identificação quando se fornecem amostras de referência" |
| esquema, 4 ramos | L1#3: "Limitações recorrentes: fala sobreposta (apartes), locutores com vozes parecidas, mudança rápida de orador, áudio de canal único com ruído de plenário" |

### P2-2.5 (bloco L2#4)

| String | Sustentação no curso |
|---|---|
| emUmMinuto 1 | L2#4: "Normalização de texto é padronizar a FORMA de escrever, sem mudar o conteúdo"; pegadinha (1): "é padronizar a forma, não corrigir a informação" |
| emUmMinuto 2 | L2#4: "Normalização (texto → fala): converte a forma escrita em forma falada"; "Normalização INVERSA (fala → texto escrito), ou ITN: converte a forma falada reconhecida em forma escrita convencional ('vinte e cinco por cento' → '25%')" |
| emUmMinuto 3 | L2#4: "a ITN decide por contexto e pode errar, logo o revisor confere"; "'dois mil e vinte e seis' pode ser ano ou quantidade" |
| tabela, Números | L2#4: "Números: algarismos ou extenso, separador de milhar, percentuais, moeda, datas..."; exemplo parlamentar: "'5%' na primeira página e 'cinco por cento' na terceira" |
| tabela, Siglas | L2#4: "Siglas: forma escrita (PEC, MPV, CCJ), expansão na primeira ocorrência ou não, glossário" |
| tabela, Abreviações | L2#4: "Abreviações: Sr., Sra., Dep.; uniformizar" |
| tabela, Termos técnicos | L2#4: "Termos técnicos: latinismos, estrangeirismos, expressões regimentais: grafia única, glossário" |
| tabela, Ambiguidades | L2#4: "Ambiguidades: 'dois mil e vinte e seis' pode ser ano ou quantidade; a ITN decide por contexto e pode errar, logo o revisor confere" |
| esquema, ramos 1 e 3 | L2#4: "Normalização (texto → fala)" e "Normalização INVERSA (fala → texto escrito), ou ITN"; exemplo "25%" do curso |
| esquema, ramo 2 | L2#4: "típica de síntese de voz e de preparo de texto para treinar modelos" |
| esquema, ramo 4 | L2#4: "É etapa de formatação posterior ao reconhecimento (1.5), não é reconhecimento acústico" |

## Bloco JSON final

```json
{
  "topicos": {
    "P2-1.4": {
      "emUmMinuto": [
        "Diarização responde a quem falou quando: segmenta o áudio em trechos e dá a cada um um rótulo genérico de locutor, sem dizer quem são.",
        "Identificação de locutor compara a voz com um banco de vozes cadastradas; verificação confirma se a voz é de uma pessoa específica alegada, de um para um.",
        "Diarização em streaming não é regra geral nem impossibilidade geral, pois depende do serviço; fala sobreposta e vozes parecidas seguem como limitações."
      ],
      "visuais": [
        {
          "tipo": "fluxo",
          "titulo": "Etapas típicas da diarização",
          "passos": [
            "Detecção de atividade de voz (VAD)",
            "Segmentação do áudio em trechos",
            "Extração de embeddings de voz por segmento",
            "Agrupamento (clustering) por semelhança de voz",
            "Rotulagem (Locutor 1, Locutor 2...)"
          ]
        },
        {
          "tipo": "tabela",
          "titulo": "Diarização, identificação e verificação de locutor",
          "colunas": [
            "Conceito",
            "Pergunta que responde",
            "Como funciona"
          ],
          "linhas": [
            [
              "Diarização",
              "Quem falou quando?",
              "Separa os locutores, sem dizer quem são"
            ],
            [
              "Identificação de locutor",
              "Quem é?",
              "Compara a voz com banco de vozes cadastradas (cadastro prévio)"
            ],
            [
              "Verificação de locutor",
              "É a pessoa alegada?",
              "Confirma a voz de uma pessoa específica (1 para 1), como em autenticação"
            ]
          ],
          "legenda": "A diarização pode ser ligada à identificação quando há amostras de referência."
        },
        {
          "tipo": "esquema",
          "titulo": "Limitações recorrentes da diarização",
          "centro": "Diarização de falantes",
          "ramos": [
            "Fala sobreposta (apartes)",
            "Locutores com vozes parecidas",
            "Mudança rápida de orador",
            "Áudio de canal único com ruído de plenário"
          ]
        }
      ]
    },
    "P2-2.5": {
      "emUmMinuto": [
        "Normalização de texto padroniza a forma de escrever sem mudar o conteúdo; não é corrigir o que o orador disse.",
        "A normalização converte a forma escrita em falada; a normalização inversa (ITN) converte a fala reconhecida em escrita convencional, como 'vinte e cinco por cento' em '25%'.",
        "A ITN decide por contexto e pode errar, por exemplo entre ano e quantidade; por isso o revisor confere o resultado."
      ],
      "visuais": [
        {
          "tipo": "tabela",
          "titulo": "Normalização na transcrição parlamentar",
          "colunas": [
            "Categoria",
            "Decisão de padronização",
            "Exemplo do curso"
          ],
          "linhas": [
            [
              "Números",
              "Algarismos ou extenso, separador de milhar, percentuais, moeda, datas",
              "\"5%\" e \"cinco por cento\" no mesmo texto"
            ],
            [
              "Siglas",
              "Forma escrita, expansão na primeira ocorrência ou não, glossário",
              "PEC, MPV, CCJ"
            ],
            [
              "Abreviações",
              "Uniformizar",
              "Sr., Sra., Dep."
            ],
            [
              "Termos técnicos",
              "Grafia única, glossário",
              "Latinismos, estrangeirismos, expressões regimentais"
            ],
            [
              "Ambiguidades",
              "A ITN decide por contexto e pode errar; o revisor confere",
              "\"dois mil e vinte e seis\": ano ou quantidade"
            ]
          ]
        },
        {
          "tipo": "esquema",
          "titulo": "Normalização e normalização inversa",
          "centro": "Normalização de texto",
          "ramos": [
            "Normalização: forma escrita para forma falada (\"25%\")",
            "Típica de síntese de voz e de preparo de texto para treino",
            "ITN: forma falada reconhecida para escrita (\"25%\")",
            "ITN é formatação posterior ao reconhecimento, não acústica"
          ]
        }
      ]
    }
  }
}
```

FIM DO ARQUIVO
