# T111_resumos_P2_A1_v1.md — T-111 parte A1 (P2-1.4 e P2-2.5) — produção gce-cpp — 2026-10-18

**Base.** Pacote v1.11 (`saida/pacote/pacote.json`). Fonte única: curso do próprio tópico, segmentado por `## `; o 1.4 reúne o bloco da folha 1.4 e o complemento do bloco de complemento (781 palavras no total); o 2.5 é o bloco da folha 2.5 (445 palavras). Regra de tamanho e forma: seção 2.1 da D1 da GCE (120 a 300 palavras e até 50% do curso; 3 a 6 parágrafos de 25 a 80 palavras; texto corrido). Contagem por script (palavras separadas por espaço). Nenhum fato fora do bloco; datas de verificação e URLs do bloco foram omitidas por serem referência de produção.

## P2-1.4

**Contagens.** Curso 781 palavras; teto efetivo 300; resumo 288 palavras; 5 parágrafos (59, 50, 55, 63, 61).

**Resumo.**

Diarização responde a "quem falou quando": segmenta o áudio em trechos e atribui a cada um um rótulo genérico de locutor, como Locutor 1 e Locutor 2. As etapas vão da detecção de atividade de voz à rotulagem, passando por embeddings e agrupamento por semelhança. A métrica usual é o DER, distinta do WER, que mede erros de palavras.

Três conceitos se misturam. A diarização separa os locutores sem dizer quem são. A identificação de locutor diz quem é, comparando a voz com um banco de vozes cadastradas. A verificação de locutor confirma se a voz é de uma pessoa específica alegada, de um para um, como na autenticação.

O verbo "identificar" também é armadilha. Se o item trata de identidade, nome, cadastro ou "qual parlamentar", exige identificação propriamente dita. Se trata de distinguir, separar ou contar oradores, é diarização, ainda que use o verbo. Sem contexto, julga-se pelo objeto: identificar que há três oradores é distinguir; identificar os oradores pelo nome é identificação.

A diarização pode ser ligada à identificação quando se fornecem amostras de referência: a API da OpenAI permite até quatro referências curtas com nomes de locutores conhecidos para mapear os segmentos. O nome existe por causa das amostras, não da diarização em si. Num texto com nomes, como "O SR. FULANO (Relator)", há amostra cadastrada ou revisão humana com a lista de inscritos.

As limitações recorrentes são fala sobreposta, vozes parecidas e ruído de plenário em canal único. A disponibilidade varia por serviço e modo: o Google Speech-to-Text V2 não tem diarização em StreamingRecognize no modelo chirp_3, a OpenAI não a suporta em sessões Realtime e o Amazon Transcribe a oferece em streaming. Logo, diarização em streaming não é regra geral nem impossibilidade geral.

**Relatório por parágrafo (ideia | frase do bloco).**

1. Definição, etapas e métrica (DER x WER) | "Diarização (speaker diarization) responde a 'quem falou quando'"; "Métrica usual: DER"
2. Diarização, identificação e verificação de locutor | "Diarização: separa os locutores, SEM dizer quem são."; "Verificação de locutor: confirma se a voz é de UMA pessoa específica alegada (1 para 1)"
3. Regra de decisão para o verbo identificar | "REGRA DE DECISÃO PARA A PROVA" (itens 1 a 3: identidade/nome x distinguir/separar; procurar o OBJETO da frase)
4. Ligação com amostras de referência | "diarização ligada à identificação por amostras de referência (a API da OpenAI aceita até quatro amostras com nomes...)"; "Aí o nome existe por causa das amostras, não da diarização em si."
5. Limitações e disponibilidade por serviço | "Limitações recorrentes: fala sobreposta..."; "A lição para a prova: 'diarização em streaming' não é regra geral nem impossibilidade geral"

## P2-2.5

**Contagens.** Curso 445 palavras; teto efetivo 222; resumo 212 palavras; 4 parágrafos (58, 52, 49, 53).

**Resumo.**

Normalização de texto é padronizar a forma de escrever sem mudar o conteúdo, e a banca mistura dois sentidos. A normalização converte a forma escrita em falada, como "25%" em "vinte e cinco por cento". A normalização inversa, ou ITN, converte a fala reconhecida em forma escrita convencional; é etapa de formatação posterior ao reconhecimento, não reconhecimento acústico.

Na transcrição parlamentar, as decisões cobrem números (algarismos ou extenso, percentuais, moeda, datas, ordinais), siglas (forma escrita, expansão na primeira ocorrência, glossário), abreviações como Sr. e Dep., que se uniformizam, e termos técnicos, que pedem grafia única. O ASR pode devolver as letras ou a pronúncia de uma sigla, não a sigla.

Há ambiguidades: "dois mil e vinte e seis" pode ser ano ou quantidade, e a ITN decide por contexto e pode errar, de modo que o revisor confere. Padronizar por regra institucional elimina oscilações como "5%" numa página e "cinco por cento" em outra, e melhora a busca posterior.

A Portaria DG nº 77/2017 determina o uso das normas de padronização do Manual de Redação da Câmara nos documentos administrativos e as recomenda para as demais modalidades de material escrito, respeitado cada gênero textual. Não é obrigatório para todo texto, e o conteúdo do Manual sobre números e siglas não foi verificado.

**Relatório por parágrafo (ideia | frase do bloco).**

1. Normalização e normalização inversa (ITN) | "Normalização (texto → fala)"; "Normalização INVERSA (fala → texto escrito), ou ITN"
2. Domínios de decisão na transcrição parlamentar | "Domínios de decisão na transcrição parlamentar:" (números, siglas, abreviações, termos técnicos)
3. Ambiguidade, ITN e padronização | "'dois mil e vinte e seis' pode ser ano ou quantidade; a ITN decide por contexto e pode errar, logo o revisor confere"; EXEMPLO PARLAMENTAR
4. Base normativa e limite do Manual | "Portaria DG nº 77/2017 determina o uso das normas de padronização do Manual para os documentos administrativos (art. 2º, caput) e as recomenda para as demais modalidades..."; "O conteúdo do Manual sobre números e siglas NÃO foi verificado."

## Bloco JSON

```json
{
 "topicos": {
  "P2-1.4": {
   "resumo": "Diarização responde a \"quem falou quando\": segmenta o áudio em trechos e atribui a cada um um rótulo genérico de locutor, como Locutor 1 e Locutor 2. As etapas vão da detecção de atividade de voz à rotulagem, passando por embeddings e agrupamento por semelhança. A métrica usual é o DER, distinta do WER, que mede erros de palavras.\n\nTrês conceitos se misturam. A diarização separa os locutores sem dizer quem são. A identificação de locutor diz quem é, comparando a voz com um banco de vozes cadastradas. A verificação de locutor confirma se a voz é de uma pessoa específica alegada, de um para um, como na autenticação.\n\nO verbo \"identificar\" também é armadilha. Se o item trata de identidade, nome, cadastro ou \"qual parlamentar\", exige identificação propriamente dita. Se trata de distinguir, separar ou contar oradores, é diarização, ainda que use o verbo. Sem contexto, julga-se pelo objeto: identificar que há três oradores é distinguir; identificar os oradores pelo nome é identificação.\n\nA diarização pode ser ligada à identificação quando se fornecem amostras de referência: a API da OpenAI permite até quatro referências curtas com nomes de locutores conhecidos para mapear os segmentos. O nome existe por causa das amostras, não da diarização em si. Num texto com nomes, como \"O SR. FULANO (Relator)\", há amostra cadastrada ou revisão humana com a lista de inscritos.\n\nAs limitações recorrentes são fala sobreposta, vozes parecidas e ruído de plenário em canal único. A disponibilidade varia por serviço e modo: o Google Speech-to-Text V2 não tem diarização em StreamingRecognize no modelo chirp_3, a OpenAI não a suporta em sessões Realtime e o Amazon Transcribe a oferece em streaming. Logo, diarização em streaming não é regra geral nem impossibilidade geral."
  },
  "P2-2.5": {
   "resumo": "Normalização de texto é padronizar a forma de escrever sem mudar o conteúdo, e a banca mistura dois sentidos. A normalização converte a forma escrita em falada, como \"25%\" em \"vinte e cinco por cento\". A normalização inversa, ou ITN, converte a fala reconhecida em forma escrita convencional; é etapa de formatação posterior ao reconhecimento, não reconhecimento acústico.\n\nNa transcrição parlamentar, as decisões cobrem números (algarismos ou extenso, percentuais, moeda, datas, ordinais), siglas (forma escrita, expansão na primeira ocorrência, glossário), abreviações como Sr. e Dep., que se uniformizam, e termos técnicos, que pedem grafia única. O ASR pode devolver as letras ou a pronúncia de uma sigla, não a sigla.\n\nHá ambiguidades: \"dois mil e vinte e seis\" pode ser ano ou quantidade, e a ITN decide por contexto e pode errar, de modo que o revisor confere. Padronizar por regra institucional elimina oscilações como \"5%\" numa página e \"cinco por cento\" em outra, e melhora a busca posterior.\n\nA Portaria DG nº 77/2017 determina o uso das normas de padronização do Manual de Redação da Câmara nos documentos administrativos e as recomenda para as demais modalidades de material escrito, respeitado cada gênero textual. Não é obrigatório para todo texto, e o conteúdo do Manual sobre números e siglas não foi verificado."
  }
 }
}
```

FIM DO ARQUIVO
