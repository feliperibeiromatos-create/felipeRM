# T111_resumos_P2_A1_v2_GCE.md — T-111 parte A1 (P2-1.4 e P2-2.5), rodada de correção — produção gce-cpp — 2026-10-18 — transcrição da GCE na reconciliação (correção editorial da R2, 1ª frase do P5 de P2-1.4; único trecho alterado)

## Resposta ao QA R1 (item a item)

- **2.5-A (sentido, P2): acatado.** "expansão ou não na primeira ocorrência".
- **2.5-B (norma sem dispositivo): acatado.** Reposto "art. 2º" e "no parágrafo único" (ambos do bloco, sem fato novo).
- **2.5-C (referência de produção): acatado.** Removido "não foi verificado"; entra "a forma exata de números e siglas dependeria dele".
- **2.5-D (sujeito ambíguo): acatado.** "O Manual não é obrigatório para todo texto".
- **2.5-E (um parágrafo por ideia): acatado.** P3 só com ambiguidade e ITN; a padronização institucional abre o P4.
- **2.5-F (fidelidade): acatado.** "a banca pode misturar dois sentidos".
- **Ressalva opcional do P2-2.5 (normalização na avaliação, antes do WER): não acatado.** Não cabe no teto de 222 com as correções; o QA a declarou não exigida.
- **Ressalva opcional do P5 de P2-1.4: acatado.** Frase trocada pela redação sugerida; sem fato novo; P5 e total seguem dentro dos limites.
- **P2-1.4, demais parágrafos: sem alteração** (APROVADO).

**Texto aplicado a P2-2.5:** o exato da seção 4 do QA (texto idêntico, conferido por script).

## Contagens

| Tópico | Curso | Teto efetivo | Resumo | Parágrafos (palavras) |
|---|---|---|---|---|
| P2-1.4 | 781 | 300 | 296 | 5 (59, 50, 55, 63, 69) |
| P2-2.5 | 445 | 222 | 221 | 4 (59, 54, 28, 80) |

Contagem por script (palavras separadas por espaço). Limites: 120 a teto; 3 a 6 parágrafos de 25 a 80.

## P2-1.4

**Resumo.**



Diarização responde a "quem falou quando": segmenta o áudio em trechos e atribui a cada um um rótulo genérico de locutor, como Locutor 1 e Locutor 2. As etapas vão da detecção de atividade de voz à rotulagem, passando por embeddings e agrupamento por semelhança. A métrica usual é o DER, distinta do WER, que mede erros de palavras.

Três conceitos se misturam. A diarização separa os locutores sem dizer quem são. A identificação de locutor diz quem é, comparando a voz com um banco de vozes cadastradas. A verificação de locutor confirma se a voz é de uma pessoa específica alegada, de um para um, como na autenticação.

O verbo "identificar" também é armadilha. Se o item trata de identidade, nome, cadastro ou "qual parlamentar", exige identificação propriamente dita. Se trata de distinguir, separar ou contar oradores, é diarização, ainda que use o verbo. Sem contexto, julga-se pelo objeto: identificar que há três oradores é distinguir; identificar os oradores pelo nome é identificação.

A diarização pode ser ligada à identificação quando se fornecem amostras de referência: a API da OpenAI permite até quatro referências curtas com nomes de locutores conhecidos para mapear os segmentos. O nome existe por causa das amostras, não da diarização em si. Num texto com nomes, como "O SR. FULANO (Relator)", há amostra cadastrada ou revisão humana com a lista de inscritos.

A diarização tem limites técnicos e de oferta: sofre com fala sobreposta, vozes parecidas e ruído de plenário em canal único. A disponibilidade varia por serviço e modo: o Google Speech-to-Text V2 não tem diarização em StreamingRecognize no modelo chirp_3, a OpenAI não a suporta em sessões Realtime e o Amazon Transcribe a oferece em streaming. Logo, diarização em streaming não é regra geral nem impossibilidade geral.

## P2-2.5

**Resumo.**

Normalização de texto é padronizar a forma de escrever sem mudar o conteúdo, e a banca pode misturar dois sentidos. A normalização converte a forma escrita em falada, como "25%" em "vinte e cinco por cento". A normalização inversa, ou ITN, converte a fala reconhecida em forma escrita convencional; é etapa de formatação posterior ao reconhecimento, não reconhecimento acústico.

Na transcrição parlamentar, as decisões cobrem números (algarismos ou extenso, percentuais, moeda, datas, ordinais), siglas (forma escrita, expansão ou não na primeira ocorrência, glossário), abreviações como Sr. e Dep., que se uniformizam, e termos técnicos, que pedem grafia única. O ASR pode devolver as letras ou a pronúncia de uma sigla, não a sigla.

Há ambiguidades: "dois mil e vinte e seis" pode ser ano ou quantidade, e a ITN decide por contexto e pode errar, de modo que o revisor confere.

A padronização por regra institucional elimina oscilações como "5%" numa página e "cinco por cento" em outra, e melhora a busca posterior. A Portaria DG nº 77/2017, art. 2º, determina o uso das normas de padronização do Manual de Redação da Câmara nos documentos administrativos e, no parágrafo único, as recomenda para as demais modalidades de material escrito, respeitado cada gênero textual. O Manual não é obrigatório para todo texto, e a forma exata de números e siglas dependeria dele.

## Relatório por parágrafo (alterações)

- P2-1.4, P5: limites técnicos e disponibilidade por serviço (bloco: "Limitações recorrentes"; "A lição para a prova"). Demais parágrafos iguais à v1.
- P2-2.5: 1 normalização e ITN | 2 domínios de decisão | 3 ambiguidade e ITN ("pode errar, logo o revisor confere") | 4 padronização institucional e Portaria (art. 2º, caput e parágrafo único) e limite do Manual.

## Bloco JSON

```json
{
 "topicos": {
  "P2-1.4": {
   "resumo": "Diarização responde a \"quem falou quando\": segmenta o áudio em trechos e atribui a cada um um rótulo genérico de locutor, como Locutor 1 e Locutor 2. As etapas vão da detecção de atividade de voz à rotulagem, passando por embeddings e agrupamento por semelhança. A métrica usual é o DER, distinta do WER, que mede erros de palavras.\n\nTrês conceitos se misturam. A diarização separa os locutores sem dizer quem são. A identificação de locutor diz quem é, comparando a voz com um banco de vozes cadastradas. A verificação de locutor confirma se a voz é de uma pessoa específica alegada, de um para um, como na autenticação.\n\nO verbo \"identificar\" também é armadilha. Se o item trata de identidade, nome, cadastro ou \"qual parlamentar\", exige identificação propriamente dita. Se trata de distinguir, separar ou contar oradores, é diarização, ainda que use o verbo. Sem contexto, julga-se pelo objeto: identificar que há três oradores é distinguir; identificar os oradores pelo nome é identificação.\n\nA diarização pode ser ligada à identificação quando se fornecem amostras de referência: a API da OpenAI permite até quatro referências curtas com nomes de locutores conhecidos para mapear os segmentos. O nome existe por causa das amostras, não da diarização em si. Num texto com nomes, como \"O SR. FULANO (Relator)\", há amostra cadastrada ou revisão humana com a lista de inscritos.\n\nA diarização tem limites técnicos e de oferta: sofre com fala sobreposta, vozes parecidas e ruído de plenário em canal único. A disponibilidade varia por serviço e modo: o Google Speech-to-Text V2 não tem diarização em StreamingRecognize no modelo chirp_3, a OpenAI não a suporta em sessões Realtime e o Amazon Transcribe a oferece em streaming. Logo, diarização em streaming não é regra geral nem impossibilidade geral."
  },
  "P2-2.5": {
   "resumo": "Normalização de texto é padronizar a forma de escrever sem mudar o conteúdo, e a banca pode misturar dois sentidos. A normalização converte a forma escrita em falada, como \"25%\" em \"vinte e cinco por cento\". A normalização inversa, ou ITN, converte a fala reconhecida em forma escrita convencional; é etapa de formatação posterior ao reconhecimento, não reconhecimento acústico.\n\nNa transcrição parlamentar, as decisões cobrem números (algarismos ou extenso, percentuais, moeda, datas, ordinais), siglas (forma escrita, expansão ou não na primeira ocorrência, glossário), abreviações como Sr. e Dep., que se uniformizam, e termos técnicos, que pedem grafia única. O ASR pode devolver as letras ou a pronúncia de uma sigla, não a sigla.\n\nHá ambiguidades: \"dois mil e vinte e seis\" pode ser ano ou quantidade, e a ITN decide por contexto e pode errar, de modo que o revisor confere.\n\nA padronização por regra institucional elimina oscilações como \"5%\" numa página e \"cinco por cento\" em outra, e melhora a busca posterior. A Portaria DG nº 77/2017, art. 2º, determina o uso das normas de padronização do Manual de Redação da Câmara nos documentos administrativos e, no parágrafo único, as recomenda para as demais modalidades de material escrito, respeitado cada gênero textual. O Manual não é obrigatório para todo texto, e a forma exata de números e siglas dependeria dele."
  }
 }
}
```

FIM DO ARQUIVO
